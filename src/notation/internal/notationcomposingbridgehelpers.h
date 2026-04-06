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

namespace mu::engraving {
class Score;
class Segment;
class Fraction;
using staff_idx_t = size_t;
}

namespace mu::notation::internal {

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

/// Returns true if any Harmony (chord symbol) annotation exists on any ChordRest
/// segment in [startTick, endTick).  O(n_segments).  Call once per
/// analyzeHarmonicRhythm() invocation to select the jazz vs. classical path.
bool scoreHasChordSymbols(const mu::engraving::Score* score,
                          const mu::engraving::Fraction& startTick,
                          const mu::engraving::Fraction& endTick);

/// Collect sorted boundary ticks from Harmony annotations in [startTick, endTick).
/// The first element is always startTick.  Each subsequent element is the tick of
/// the first Harmony annotation found on a ChordRest segment strictly after the
/// previous boundary tick.  Duplicates at the same tick collapse to one entry.
std::vector<mu::engraving::Fraction>
collectChordSymbolBoundaries(const mu::engraving::Score* score,
                             const mu::engraving::Fraction& startTick,
                             const mu::engraving::Fraction& endTick);

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

} // namespace mu::notation::internal
