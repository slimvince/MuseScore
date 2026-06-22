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

// ── composing/analysis/engravingbridge ───────────────────────────────────────
//
// Single source of truth for the score-walking helpers used by both the
// notation bridge (analyzeHarmonicRhythm) and tools/batch_analyze.cpp.
//
// Before this module existed each helper was implemented twice (once in
// notationcomposingbridgehelpers.cpp, once in batch_analyze.cpp) and the
// two copies drifted in semantically important ways — see
// docs/duplication_audit.md §§2.1–2.13 and the bwv356 m19 b1 finding (§4).
//
// All implementations live here. notationcomposingbridgehelpers.cpp keeps a
// public API in mu::notation::internal as a thin pass-through, so other
// notation TUs do not need to change. tools/batch_analyze.cpp calls this
// module directly.
//
// The module depends only on the engraving layer (Score, Segment, Measure,
// Fraction), the composing analysis types (ChordAnalysisTone, ChordTemporalContext,
// KeyModeAnalyzer::PitchContext) and the scoreharvest helpers — never on
// notation/internal.

#include <cstddef>
#include <set>
#include <vector>

#include "composing/analysis/chord/chordanalyzer.h"
#include "composing/analysis/key/keymodeanalyzer.h"
#include "composing/analysis/notemodel/note_model.h"
#include "engraving/dom/part.h"
#include "engraving/dom/score.h"
#include "engraving/dom/staff.h"
#include "engraving/types/constants.h"
#include "engraving/types/fraction.h"

namespace mu::engraving {
class Segment;
class Measure;
}

namespace mu::composing::analysis::engravingbridge {

// ── Staff-eligibility predicates ─────────────────────────────────────────────
//
// Matches the inline definitions in src/notation/internal/notationanalysisinternal.h.
// Re-implemented here so this module does not include notation-layer headers.
// The functions are trivial and live in the header so they remain inline.

inline bool isChordTrackStaff(const mu::engraving::Score* sc, std::size_t si)
{
    static const muse::String CHORD_TRACK_MARKER = u"Chord Track";
    if (si >= sc->nstaves()) {
        return false;
    }
    const mu::engraving::Part* part = sc->staff(si)->part();
    if (!part) {
        return false;
    }
    if (part->partName().contains(CHORD_TRACK_MARKER)) {
        return true;
    }
    const mu::engraving::Instrument* instrument = part->instrument();
    return instrument && instrument->trackName().contains(CHORD_TRACK_MARKER);
}

/// Is this staff eligible for harmonic analysis at the given tick?
/// Excludes hidden staves, percussion instruments, and chord-track staves.
inline bool staffIsEligible(const mu::engraving::Score* sc, std::size_t si,
                            const mu::engraving::Fraction& tick)
{
    const mu::engraving::Staff* st = sc->staff(si);
    if (!st->show()) {
        return false;
    }
    if (st->part()->instrument(tick)->useDrumset()) {
        return false;
    }
    if (isChordTrackStaff(sc, si)) {
        return false;
    }
    return true;
}

// ── Sounding-note primitives ─────────────────────────────────────────────────

/// A raw sounding note: playback pitch + TPC spelling.
struct SoundingNote { int ppitch; int tpc; };

/// Point-in-time per-note view over the note model: every note sounding AT
/// `tick` (onset <= tick < release), across eligible, non-excluded, playing,
/// visible, non-grace notes. Result order reproduces the legacy collectSoundingAt
/// order (notes onsetting exactly at `tick` first in staff/voice order, then
/// sustained notes in descending-onset order). True-span overlap — no horizon.
void soundingAt(const mu::composing::analysis::notemodel::NoteModel& noteModel,
                int tick,
                const std::set<std::size_t>& excludeStaves,
                std::vector<SoundingNote>& out);

/// Collect all notes sounding at anchorSeg's tick across eligible staves.
/// Score-based convenience wrapper: builds a note model and delegates to
/// soundingAt(). Prefer the model-taking overload on hot paths (build once).
void collectSoundingAt(const mu::engraving::Score* sc,
                       const mu::engraving::Segment* anchorSeg,
                       const std::set<std::size_t>& excludeStaves,
                       std::vector<SoundingNote>& out);

/// Convert raw sounding notes to analysis tones. Marks the lowest pitch as bass.
std::vector<mu::composing::analysis::ChordAnalysisTone>
buildTones(const std::vector<SoundingNote>& sounding);

// ── Region-scope tone accumulation ───────────────────────────────────────────

/// Collect and accumulate pitch evidence for the harmonic region [startTick, endTick).
///
/// Walks all ChordRest segments in the region across eligible staves. For each
/// note event, computes a base weight = (durationInRegion / regionDuration) × beatWeight.
/// Aggregates evidence by pitch class, then applies:
///   Pass 2 — repetition boost: weight × (1 + 0.3 × (distinctMetricPositions − 1))
///   Pass 3 — cross-voice boost: weight × 1.5 when simultaneousVoiceCount > 1
///   Pass 4 — discounted sustain-pedal tails after written note-off
/// Weights are normalised to sum to 1.0 before return.
///
/// `parentStartTick`: tick used for the per-tone `onsetAtRegionStart` flag.
///   - For un-split (parent-scope) calls, pass -1 to default to startTick.
///   - For Pass 2 / Pass 2b sub-region calls, pass the parent region's
///     startTick so onset flags remain meaningful at full-region scope
///     (Iter 93).
/// `excludeLookAheadOnDenseStart`: when true and ≥3 distinct pitch classes are
///   already sounding at the region start tick, notes whose onset is strictly
///   after startTick are excluded from chord inference. This was the batch
///   pipeline's legacy behavior; the bridge always leaves this false (default).
///
/// `weightedPcView` is the real implementation, derived over the note model:
/// it reproduces collectRegionTones exactly EXCEPT for the two intended layer-1
/// corrections — tied groups count as one onset (no repetition-boost inflation)
/// and sustains of any length are found by true-span overlap (no 4-whole-note
/// backward cap).
std::vector<mu::composing::analysis::ChordAnalysisTone>
weightedPcView(const mu::composing::analysis::notemodel::NoteModel& noteModel,
               int startTick,
               int endTick,
               const std::set<std::size_t>& excludeStaves,
               int parentStartTick = -1,
               bool excludeLookAheadOnDenseStart = false,
               const mu::composing::analysis::ChordAnalyzerPreferences& prefs
                   = mu::composing::analysis::kDefaultChordAnalyzerPreferences);

/// Score-based convenience wrapper: builds a note model and delegates to
/// weightedPcView(). Prefer the model-taking view on hot paths (build once).
std::vector<mu::composing::analysis::ChordAnalysisTone>
collectRegionTones(const mu::engraving::Score* sc,
                   int startTick,
                   int endTick,
                   const std::set<std::size_t>& excludeStaves,
                   int parentStartTick = -1,
                   bool excludeLookAheadOnDenseStart = false);

// ── Sub-boundary detectors ───────────────────────────────────────────────────

/// Pass 2: onset-only sub-boundary detection within a coarse Jaccard region.
/// Collects only notes whose start tick equals the segment tick (no sustained
/// notes), then computes Jaccard distance between consecutive onset sets.
/// Lower threshold = more boundaries. Default 0.25.
/// Returns sub-boundary ticks (not including startTick).
std::vector<mu::engraving::Fraction>
detectOnsetSubBoundaries(const mu::engraving::Score* sc,
                         const mu::engraving::Fraction& startTick,
                         const mu::engraving::Fraction& endTick,
                         const std::set<std::size_t>& excludeStaves,
                         double threshold = 0.25);

/// Pass 2b: bass-movement sub-boundary detection within a coarse Jaccard region.
/// Scans onset-only notes and tracks the lowest-pitch note at each segment as the
/// "bass". When the bass pitch class changes from the bass at the most recently
/// accepted boundary, and the gap since that boundary is >= minGapTicks, fires a
/// sub-boundary. ANY bass PC change fires — no minimum interval threshold.
/// Returns sub-boundary ticks (not including startTick).
std::vector<mu::engraving::Fraction>
detectBassMovementSubBoundaries(const mu::engraving::Score* sc,
                                const mu::engraving::Fraction& startTick,
                                const mu::engraving::Fraction& endTick,
                                const std::set<std::size_t>& excludeStaves,
                                int minGapTicks = 2 * mu::engraving::Constants::DIVISION);

// ── Temporal context ─────────────────────────────────────────────────────────

/// Build the single-step temporal context around seg by walking backward AND
/// forward. Backward (seg->prev1) sets previousRootPc / previousQuality /
/// previousBassPc; forward (seg->next1) sets nextRootPc / nextBassPc. Both
/// neighbours are cold-analyzed (no temporal chain).
/// currentBassPc: bass pitch class of the chord about to be analysed (0-11),
/// or -1 if not yet known. Used to compute bassIsStepwiseFromPrevious /
/// bassIsStepwiseToNext.
mu::composing::analysis::ChordTemporalContext
findTemporalContext(const mu::composing::analysis::notemodel::NoteModel& noteModel,
                    const mu::engraving::Segment* seg,
                    const std::set<std::size_t>& excludeStaves,
                    int keyFifths,
                    mu::composing::analysis::KeySigMode keyMode,
                    int currentBassPc = -1);

// ── Pitch context for key/mode resolution ────────────────────────────────────

/// Collect pitch context for the window [windowStart, windowEnd], appending to ctx.
///
/// LEGACY (DOM-walk, point-anchored). Walks ChordRest segments from the window-
/// start measure and weights each onsetting note by distance from the single
/// anchor `tick`. It does NOT use the Layer-1 index. The indexed, span-anchored
/// successor is `pitchContextOverSpan` (below), which the Layer-3 key/mode
/// sequence decoder consumes; this builder is retired once the decoder is the live
/// key path (the Layer-3 wiring increment). Until then both exist — collectPitchContext
/// stays the live resolver's builder (byte-identical), pitchContextOverSpan the L3 one.
void collectPitchContext(const mu::engraving::Score* sc,
                         const mu::engraving::Fraction& tick,
                         const mu::engraving::Fraction& windowStart,
                         const mu::engraving::Fraction& windowEnd,
                         const std::set<std::size_t>& excludeStaves,
                         const mu::composing::analysis::KeyModeAnalyzerPreferences& prefs,
                         std::vector<mu::composing::analysis::KeyModeAnalyzer::PitchContext>& ctx);

/// Weighting knobs for the windowed pitch-context view (pitchContextOverSpan).
/// All three are length-scales / multipliers seeded with the metricweights values;
/// the caller (the L3 decoder) passes its own settings so nothing is hardcoded.
struct SpanWindowWeights {
    double decayRate         = 0.7;  ///< == scoreharvest DECAY_RATE
    double lookaheadWeight   = 0.5;  ///< == scoreharvest LOOKAHEAD_WEIGHT
    double beatsPerDecayUnit = 4.0;  ///< beats per time-decay unit (one 4/4 measure)
};

/// Windowed pitch context over a SPAN, derived from the note model's INDEXED
/// overlap query (NoteModel::overlapping, O(log N + result)) — NOT a DOM walk. The
/// reusable note-model-derived view the Layer-3 key/mode decoder consumes (beside
/// weightedPcView / soundingAt); the indexed, span-anchored successor to
/// collectPitchContext.
///
/// Every eligible note — `plays && visible && staffEligible && !grace`, staff not
/// in @p excludeStaves — overlapping [windowStart, windowEnd) is APPENDED to @p out
/// weighted by
///   durationQn × timeDecay(beatsFromAnchorSpan, decayRate, beatsPerDecayUnit)
///   × (lookaheadWeight if it onsets at/after anchorEnd, else 1.0),
/// with the beat-type weight at its onset and isBass = the lowest pitch sharing
/// that onset. The anchor span [anchorStart, anchorEnd) is the focal region (a
/// slice): notes inside it carry full time-weight; look-back and look-ahead decay
/// with distance from the span's edges. The beat weight is read from the score's
/// time signature via an INDEXED measure lookup (tick2measure) — no segment walk.
void pitchContextOverSpan(
    const mu::composing::analysis::notemodel::NoteModel& model,
    int windowStart, int windowEnd, int anchorStart, int anchorEnd,
    const std::set<std::size_t>& excludeStaves,
    const mu::composing::analysis::KeyModeAnalyzerPreferences& beatPrefs,
    const SpanWindowWeights& weights,
    std::vector<mu::composing::analysis::KeyModeAnalyzer::PitchContext>& out);

} // namespace mu::composing::analysis::engravingbridge
