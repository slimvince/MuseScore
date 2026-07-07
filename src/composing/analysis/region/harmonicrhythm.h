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

#include <array>
#include <set>
#include <vector>

#include "../chord/chordanalyzer.h"
#include "../key/keymodeanalyzer.h"

namespace mu::composing::analysis {

/// Snapshot of the `ChordTemporalContext` values that were active when the
/// enclosing region was analyzed.  The analyzer continues to consume
/// `ChordTemporalContext` as input; this struct is the parallel output
/// surface that downstream emitters and the tick-regional bridge read.
/// Phase 3c moved this from `notation/internal/` to here so it can be
/// shared between `HarmonicRegion` (transitional plumbing) and
/// `AnalyzedRegion` (canonical surface).
struct ChordTemporalExtensions {
    int previousRootPc = -1;
    int previousBassPc = -1;
    ChordQuality previousQuality = ChordQuality::Unknown;
    bool bassIsStepwiseFromPrevious = false;
    bool bassIsStepwiseToNext = false;
    int nextRootPc = -1;                           ///< Root PC of next region; -1 = unknown.
    int consecutiveBassStepwiseCount = 0;          ///< Consecutive stepwise bass moves ending here.
    std::array<int, 3> recentRootPcs = {-1,-1,-1}; ///< Root PCs of 3 most recent regions.
    double regionMetricWeight = 1.0;               ///< Metric weight [0,1]; 1 = downbeat.
};

/// Snapshot the analyzer-input temporal context as a downstream-facing
/// extensions value.
inline ChordTemporalExtensions toExtensionsSnapshot(const ChordTemporalContext& ctx)
{
    ChordTemporalExtensions ext;
    ext.previousRootPc = ctx.previousRootPc;
    ext.previousBassPc = ctx.previousBassPc;
    ext.previousQuality = ctx.previousQuality;
    ext.bassIsStepwiseFromPrevious = ctx.bassIsStepwiseFromPrevious;
    ext.bassIsStepwiseToNext = ctx.bassIsStepwiseToNext;
    ext.nextRootPc = ctx.nextRootPc;
    ext.consecutiveBassStepwiseCount = ctx.consecutiveBassStepwiseCount;
    ext.recentRootPcs = ctx.recentRootPcs;
    ext.regionMetricWeight = ctx.regionMetricWeight;
    return ext;
}

/// A contiguous time region in which the harmonic content (root + quality)
/// remains constant.  Produced by analyzeHarmonicRhythm() and consumed by
/// both the chord track population and region intonation workflows.
///
/// Tick values are stored as raw integers (use Fraction::ticks() /
/// Fraction::fromTicks() to convert) so that this header stays free of the
/// engraving Fraction include — preserving composing_analysis's independence
/// from the engraving module.
struct HarmonicRegion {
    int startTick = 0;                              ///< First tick of this region (raw tick integer)
    int endTick = 0;                                ///< First tick of the next region (exclusive)
    ChordAnalysisResult chordResult;                ///< Root, quality, extensions, degree
    std::vector<ChordAnalysisResult> alternatives;  ///< Candidates [1..N-1] from the per-region analyzeChord (Phase 3c)
    bool hasAnalyzedChord = true;                   ///< False when note-based chord analysis produced no candidate for this region
    KeyModeAnalysisResult keyModeResult;            ///< Key and mode context for this region
    std::vector<ChordAnalysisTone> tones;           ///< The sounding tones that produced the analysis
    ChordTemporalExtensions temporalExtensions;     ///< Snapshot of the temporal context used to analyze this region (Phase 3c)

    // ── Layer-5 override-readiness forward-carry (IN-MEMORY ONLY, no consumer yet) ──
    // The ranked alternative KEYS the Layer-5 modulation recompute selects among, plus
    // ★ D-L3a (CLOSED — confidence contract §3 / §7): `keyConfidence` below is THE
    // Layer-3 boundary confidence — the chosen key's Class-M sequence margin. The
    // emission sigmoid (keyModeResult.normalizedConfidence) is NOT the boundary
    // confidence: it is demoted to an internal gate input (the 0.8 KeyArea / cadence
    // annotate gate) plus diagnostic export. The C1 reliability curves decided this —
    // the margin is 2.8–3.1× better calibrated than the sigmoid on every preset
    // (cc_c1_reliability_report.md §3). Declaration only; no wiring/threshold change.
    //
    // the chosen key's sequence-margin confidence (the override-bar input). Filled at
    // the slice→region key reduction (regionanalyzer.cpp localKeyForRegion) so the
    // Layer-5 confidence-weighted forward override can SELECT among the keys the key
    // layer carried forward — never re-derive (cowork_layer5_function_design.md §8 /
    // §9-D7). The chosen key (keyModeResult) and everything consumed today are
    // unchanged; this is additive plumbing of already-computed data.
    //
    // ★ PINNED reduction (§15-3, Phase-5c Step-4): keyAlternatives is the REGION-LEVEL
    // candidate-key menu — every key the region's slices ranked (each slice's chosen key
    // AND its ranked alternatives), bucketed by (tonic,mode) and ranked by accumulated
    // support, EXCLUDING the chosen region key (the keys the modulation recompute chooses
    // between) — NOT the byte-identical v1 placeholder (one representative slice's own
    // alternatives). The pin is byte-identical on production because this carry has NO
    // production consumer (see below).
    //
    // ★ DELIBERATELY NOT SERIALIZED into ANY production output (.ours.json, the pipeline
    // snapshot goldens, notation annotations): every region serializer reads only named
    // sub-fields (keyModeResult.*, tones, chordResult, …) and none touches these — so
    // adding them is byte-identical. Empty / 0.0 until the Layer-3 decode runs (the live
    // analyzeRegions key path); has NO consumer — it exists for Layer 5.
    std::vector<KeyModeAnalysisResult> keyAlternatives; ///< region-level ranked candidate keys (excl. the chosen)
    double keyConfidence = 0.0;                          ///< THE Layer-3 boundary confidence: chosen key's Class-M sequence margin (D-L3a; ≠ keyModeResult.normalizedConfidence, the internal/diagnostic emission sigmoid)

    // ── Read-only Layer-5 fan-out summary (Engage arc #8; IN-MEMORY ONLY) ──────
    // The TRUE untruncated above-threshold ranked-set size Layer 5 will select over,
    // captured from this region's gateCtx BEFORE applyHarmonicFunction()'s cap-of-3.
    // Filled at the competition commit sites (regionanalyzer.cpp) via
    // computeRawFanoutSummary(gateCtx); default (all-0) at inherited/gap/fallback
    // regions that ran no fresh competition. Like keyAlternatives above, this is
    // DELIBERATELY NOT SERIALIZED into any production output — every region serializer
    // reads only named sub-fields and none touches this, so adding it is byte-identical.
    // Emitted solely by the read-only --dump-fanout diagnostic.
    RawFanoutSummary fanout {};                           ///< uncapped competition fan-out summary (read-only measurement)
};

} // namespace mu::composing::analysis
