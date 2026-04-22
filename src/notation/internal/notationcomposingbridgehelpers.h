/*
 * SPDX-License-Identifier: GPL-3.0-only
 * MuseScore-Studio-CLA-applies
 *
 * MuseScore Studio
 * Music Composition & Notation
 *
 * Copyright (C) 2026 MuseScore Limited
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License version 3 as
 * published by the Free Software Foundation.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */
#pragma once

// ── Shared bridge helpers — INTERNAL, do not include outside notation/internal ──
//
// Utility types and functions shared by the two bridge translation units:
//   • notationcomposingbridge.cpp  (harmonicAnnotation, analyzeNoteHarmonicContext)
//   • notationharmonicrhythmbridge.cpp (analyzeHarmonicRhythm)
//
// All symbols live in an anonymous namespace in each TU's .cpp — this header
// only declares them so they can be shared via a common .cpp compilation unit.
// See notationcomposingbridgehelpers.cpp for the definitions.

#include <set>
#include <vector>

#include "composing/analysis/chord/chordanalyzer.h"
#include "composing/analysis/key/keymodeanalyzer.h"
#include "composing/analysis/region/harmonicrhythm.h"

namespace mu::engraving {
class Score;
class Segment;
class Fraction;
using staff_idx_t = size_t;
}

namespace mu::notation::internal {

/// Map the score's chord symbol spelling preference (Sid::chordSymbolSpelling) to
/// ChordSymbolFormatter::NoteSpelling.  Returns Standard for a null score or for
/// spelling types not yet supported in chord symbol output (Solfeggio, French).
mu::composing::analysis::ChordSymbolFormatter::NoteSpelling scoreNoteSpelling(
    const mu::engraving::Score* score);

/// A raw sounding note: playback pitch + TPC spelling.
struct SoundingNote { int ppitch; int tpc; };

/// Collect all notes sounding at anchorSeg's tick across eligible staves.
/// Walks backward up to 4 quarter notes to catch sustained notes.
void collectSoundingAt(const mu::engraving::Score* sc,
                       const mu::engraving::Segment* anchorSeg,
                       const std::set<size_t>& excludeStaves,
                       std::vector<SoundingNote>& out);

/// Convert raw sounding notes to analysis tones.  Marks the lowest pitch as bass.
std::vector<mu::composing::analysis::ChordAnalysisTone>
buildTones(const std::vector<SoundingNote>& sounding);

/// Map MuseScore's BeatType enum to a weight for key/mode analysis.
double beatTypeToWeight(mu::engraving::BeatType bt,
                        const mu::composing::analysis::KeyModeAnalyzerPreferences& prefs);

/// Exponential time decay: notes further from the analysis tick carry less weight.
double timeDecay(double beatsAgo, double decayRate = 0.7);

/// Count distinct pitch classes in a PitchContext vector.
int distinctPitchClasses(
    const std::vector<mu::composing::analysis::KeyModeAnalyzer::PitchContext>& ctx);

/// Collect pitch context for the window [windowStart, windowEnd], appending to ctx.
void collectPitchContext(const mu::engraving::Score* sc,
                         const mu::engraving::Fraction& tick,
                         const mu::engraving::Fraction& windowStart,
                         const mu::engraving::Fraction& windowEnd,
                         const std::set<size_t>& excludeStaves,
                         const mu::composing::analysis::KeyModeAnalyzerPreferences& prefs,
                         std::vector<mu::composing::analysis::KeyModeAnalyzer::PitchContext>& ctx);

/// Resolve key signature and mode at a tick, with optional hysteresis.
void resolveKeyAndMode(const mu::engraving::Score* sc,
                       const mu::engraving::Fraction& tick,
                       mu::engraving::staff_idx_t staffIdx,
                       const std::set<size_t>& excludeStaves,
                       int& outKeyFifths,
                       mu::composing::analysis::KeySigMode& outMode,
                       double& outConfidence,
                       const mu::composing::analysis::KeyModeAnalysisResult* prevResult = nullptr,
                       double* outScore = nullptr);

/// Returns true if the interval between two pitch classes (0-11) is a
/// diatonic step (1 or 2 semitones) in either direction.
inline bool isDiatonicStep(int pc1, int pc2) {
    int interval = std::abs(pc1 - pc2);
    interval = std::min(interval, 12 - interval);
    return interval == 1 || interval == 2;
}

/// Collect and accumulate pitch evidence for the harmonic region [startTick, endTick).
///
/// Walks all ChordRest segments in the region across eligible staves.  For each
/// note event, computes a base weight = (durationInRegion / regionDuration) × beatWeight.
/// Aggregates evidence by pitch class, then applies:
///   Pass 2 — repetition boost: weight × (1 + 0.3 × (distinctMetricPositions − 1))
///   Pass 3 — cross-voice boost: weight × 1.5 when simultaneousVoiceCount > 1
///   Pass 4 — discounted sustain-pedal tails after written note-off
/// Weights are normalised to sum to 1.0 before return.
///
/// Returns one ChordAnalysisTone per distinct pitch class, with all §4.1c fields
/// populated.  Returns empty vector when the region contains no audible notes.
std::vector<mu::composing::analysis::ChordAnalysisTone>
collectRegionTones(const mu::engraving::Score* sc,
                   int startTick,
                   int endTick,
                   const std::set<size_t>& excludeStaves);

/// Detect harmonic region boundaries using Jaccard distance on quarter-note windows.
///
/// Divides [startTick, endTick) into Constants::DIVISION-tick (1 quarter note) windows.
/// Collects the set of pitch classes that attack in each window.  Fires a boundary at
/// the start of a window when Jaccard(prevWindow, currentWindow) >= jaccardThreshold,
/// where Jaccard = 1 − |A∩B| / |A∪B|.  When no boundary fires, the current window's
/// pitch classes are merged into the running "previous" set so that accumulated harmony
/// is compared against the next window.
///
/// Returns a sorted list of boundary ticks.  The first element is always startTick.
std::vector<mu::engraving::Fraction>
detectHarmonicBoundariesJaccard(const mu::engraving::Score* sc,
                                const mu::engraving::Fraction& startTick,
                                const mu::engraving::Fraction& endTick,
                                const std::set<size_t>& excludeStaves,
                                double jaccardThreshold);

/// Pass 2: onset-only sub-boundary detection within a coarse Jaccard region.
/// Collects only notes whose start tick equals the segment tick (no sustained
/// notes), then computes Jaccard distance between consecutive onset sets.
/// Lower threshold = more boundaries. Default 0.25.
/// Returns sub-boundary ticks (not including startTick).
std::vector<mu::engraving::Fraction>
detectOnsetSubBoundaries(const mu::engraving::Score* sc,
                         const mu::engraving::Fraction& startTick,
                         const mu::engraving::Fraction& endTick,
                         const std::set<size_t>& excludeStaves,
                         double threshold = 0.25);

/// Pass 2b: bass-movement sub-boundary detection within a coarse Jaccard region.
/// Scans onset-only notes (notes whose start tick equals the segment tick) and
/// tracks the lowest-pitch note at each segment as the "bass".  When the bass
/// pitch class changes from the bass at the most recently accepted boundary, and
/// the gap since that boundary is >= minGapTicks, fires a sub-boundary.
/// ANY bass PC change fires — no minimum interval threshold.  Downstream chord
/// analysis (bassPassingToneMinWeightFraction) handles passing-tone suppression.
/// Returns sub-boundary ticks (not including startTick).
std::vector<mu::engraving::Fraction>
detectBassMovementSubBoundaries(const mu::engraving::Score* sc,
                                const mu::engraving::Fraction& startTick,
                                const mu::engraving::Fraction& endTick,
                                const std::set<size_t>& excludeStaves,
                                int minGapTicks = 2 * mu::engraving::Constants::DIVISION);

/// Returns true if any standard chord symbol in [startTick, endTick) has a valid
/// written root. Roman/Nashville analysis annotations should not activate the jazz path.
bool scoreHasValidChordSymbols(const mu::engraving::Score* score,
                               const mu::engraving::Fraction& startTick,
                               const mu::engraving::Fraction& endTick,
                               const std::set<size_t>& excludeStaves = {});

/// Collect sorted boundary ticks from standard chord symbols in [startTick, endTick).
/// The first element is always startTick.  Each subsequent element is the tick of
/// the first standard chord symbol found on a ChordRest segment strictly after the
/// previous boundary tick.  Duplicates at the same tick collapse to one entry.
std::vector<mu::engraving::Fraction>
collectChordSymbolBoundaries(const mu::engraving::Score* score,
                             const mu::engraving::Fraction& startTick,
                             const mu::engraving::Fraction& endTick,
                             const std::set<size_t>& excludeStaves = {});

/// Find the previous chord's temporal context by walking backward from seg.
/// currentBassPc: bass pitch class of the chord about to be analysed (0-11),
/// or -1 if not yet known.  Used to compute bassIsStepwiseFromPrevious.
mu::composing::analysis::ChordTemporalContext
findTemporalContext(const mu::engraving::Score* sc,
                    const mu::engraving::Segment* seg,
                    const std::set<size_t>& excludeStaves,
                    int keyFifths,
                    mu::composing::analysis::KeySigMode keyMode,
                    int currentBassPc = -1);

/// Upgrade user-facing sparse results from Unknown to the diatonic triad quality
/// implied by the resolved key/mode when the sounding tones are compatible.
void refineSparseChordQualityFromKeyContext(
    mu::composing::analysis::ChordAnalysisResult& result,
    const std::vector<mu::composing::analysis::ChordAnalysisTone>& tones,
    int keyFifths,
    mu::composing::analysis::KeySigMode keyMode);

/// Force-assign the diatonic triad quality for a chord-track region that still has
/// quality=Unknown after the standard refinement.  Unlike refineSparseChordQualityFromKeyContext,
/// this does NOT apply the Aeolian lone-tonic/dominant exclusion — it is appropriate for
/// chord-track annotation where annotating even sparse/monophonic regions is desirable.
/// Does nothing when result.identity.quality is already non-Unknown, or when no diatonic
/// triad shape can be determined for the degree.
void forceChordTrackQualityFromKeyContext(
    mu::composing::analysis::ChordAnalysisResult& result,
    mu::composing::analysis::KeySigMode keyMode);

/// Build the same user-facing harmonic regions consumed by chord-track population.
/// Uses smoothed region analysis, fills leading sparse gaps conservatively, and
/// stabilizes key/mode so Roman numerals remain consistent across display paths.
///
/// Pass forceClassicalPath=true to skip the Jazz chord-symbol boundary gate even
/// when the score contains STANDARD Harmony elements.  Used by the annotation
/// write path to avoid order-of-annotation violations.
std::vector<mu::composing::analysis::HarmonicRegion>
prepareUserFacingHarmonicRegions(const mu::engraving::Score* sc,
                                 const mu::engraving::Fraction& startTick,
                                 const mu::engraving::Fraction& endTick,
                                 const std::set<size_t>& excludeStaves,
                                 bool forceClassicalPath = false);

// ── Cadence and pivot detection ───────────────────────────────────────────────

/// Minimum normalized key confidence required for cadence or pivot detection.
/// Matches kAssertiveKeyExposureThreshold used by populateChordTrack.
inline constexpr double kAnnotateKeyConfidenceThreshold = 0.8;

/// Maximum number of lookahead regions (past the selection boundary) examined
/// when trying to confirm that a candidate pivot chord's new key is stable.
inline constexpr int kMaxPivotLookaheadRegions = 8;

/// A cadence label ("PAC", "PC", "DC", "HC") at a score tick.
struct CadenceMarker {
    int tick;
    std::string label;
};

/// A pivot chord label ("vi \u2192 ii" etc.) at a score tick.
struct PivotLabel {
    int tick;
    std::string label;
};

/// Returns true if the key mode result meets the assertive confidence threshold
/// used for cadence and pivot detection.
bool hasAssertiveKeyConfidence(
    const mu::composing::analysis::KeyModeAnalysisResult& kmr);

/// Detect cadence markers from an ordered sequence of harmonic regions.
///
/// @param regions        All regions, including any read-only lookahead regions
///                       past the selection boundary.
/// @param selectionCount First N elements of regions[] are inside the user's
///                       selection; elements at index N and above are lookahead.
///
/// PAC/PC/DC labels are placed at the resolution chord's tick. When the
/// resolution chord is in the lookahead (outside the selection), the label is
/// placed at the preparatory chord (last in-selection region) instead, so that
/// every returned tick falls inside the selection.
///
/// HC is emitted when the last in-selection region is a dominant (degree 4).
std::vector<CadenceMarker> detectCadences(
    const std::vector<mu::composing::analysis::HarmonicRegion>& regions,
    size_t selectionCount);

/// Detect pivot chord labels from an ordered sequence of harmonic regions.
///
/// The pivot is the most recent in-selection chord that is diatonic to the
/// outgoing key AND whose root also belongs to the incoming key's scale.
/// Its label has the form "vi \u2192 ii" (outgoing Roman \u2192 incoming Roman).
///
/// @param regions        All regions including lookahead.
/// @param selectionCount Index of first lookahead region (0 = no in-selection
///                       regions; equal to regions.size() = no lookahead).
///
/// If the incoming key cannot be confirmed by an assertive region within
/// kMaxPivotLookaheadRegions past the boundary, the pivot label is suppressed
/// to avoid false positives.
std::vector<PivotLabel> detectPivotChords(
    const std::vector<mu::composing::analysis::HarmonicRegion>& regions,
    size_t selectionCount);

/// Returns the diatonic scale degree [0..6] of rootPc in (keyFifths, keyMode),
/// or -1 if rootPc is not in the scale.
int diatonicDegreeForRootPc(int rootPc, int keyFifths,
                            mu::composing::analysis::KeySigMode keyMode);

} // namespace mu::notation::internal
