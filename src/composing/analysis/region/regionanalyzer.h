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

// ── composing/analysis/region/regionanalyzer ─────────────────────────────────
//
// Single shared regional-analysis orchestrator. Phase 4 of the duplication
// remediation (docs/duplication_audit.md §§2.14, 5.4) collapsed the two
// previously parallel orchestrators — `analyzeHarmonicRhythm()` in the
// notation bridge and `analyzeScore()` in tools/batch_analyze.cpp — into this
// single function. Both call sites are now thin wrappers.
//
// The bridge's behaviour is canonical wherever the two had drifted:
//   • Pass 2 onset-Jaccard sub-boundary detection (was bridge-only)
//   • Pass 2b iteration (while anyNewSplit, up to kMaxBassMovementPasses)
//   • absorbShortRegions with the Iter 78 Fix A sharesPrevRoot guard
//   • Iter 87 post-merge MinorSeventh re-stamp (was batch-only — included
//     here so both paths get the same post-merge guarantee)
//   • backfillNextRootPc (V/x and vii°/x tonicization labels)
//   • Parent-scope plumbing (Iter 92–95: previousBassPc / nextBassPc /
//     nextRootPc / parentStartTick) read off the already-analyzed parent
//     region's identity at the Pass 2 / Pass 2b call sites.

#include <cstddef>
#include <set>
#include <vector>

#include "composing/analysis/chord/chordanalyzer.h"
#include "composing/analysis/key/keymodeanalyzer.h"
#include "composing/analysis/region/harmonicrhythm.h"
#include "engraving/types/fraction.h"

namespace mu::engraving {
class Score;
}

namespace mu::composing::analysis {

/// Granularity of the region output.
///   Smoothed           — Pass 3 absorbShortRegions runs, producing
///                        merge-stable chord-rhythm regions for display.
///   PreserveAllChanges — every pitch-class-set change becomes a boundary,
///                        no absorbShortRegions; intended for tick-regional
///                        debug inspection or downstream consumers that want
///                        the raw boundary stream.
enum class HarmonicRegionGranularity {
    Smoothed,
    PreserveAllChanges,
};

namespace region {

/// Optional debug capture for the pre-merge and post-merge region streams.
/// Either pointer may be null; supplied vectors are populated in place
/// (existing contents are overwritten via std::move).
struct RegionAnalysisHooks {
    std::vector<HarmonicRegion>* preMergeRegions = nullptr;
    std::vector<HarmonicRegion>* postMergeRegions = nullptr;
};

/// Architectural Layer 3 reach-back — a SELECTION-AWARE capability, default OFF.
///
/// When disabled (the production default) analyzeRegions builds Layer 1 over the
/// WHOLE score and never reaches back, so the live path is byte-identical to before
/// this option existed. When enabled, analyzeRegions builds Layer 1 over the
/// SELECTION [startTick, endTick) only; if the selection's opening carries no
/// settled key (the leading-edge slice is "uncertain"), it asks Layer 1 to extend
/// EARLIER one increment at a time, re-slices (Layer 2) and re-decodes (Layer 3) the
/// enlarged span, until a settled prevailing key is in view in the reached-back
/// context (the convergence proxy), the hard bound is hit, or the score start is
/// reached. Output stays the selection only (the reached-back context is evidence,
/// never emitted). The decoder remains a pure function of the slices it is given;
/// the extend → re-slice → re-decode loop lives in the orchestrator.
/// See cowork_layer3_reachback_design.md.
struct ReachBackOptions {
    /// OFF ⇒ whole-score build, no reach-back (the production path; byte-identical).
    /// ON  ⇒ build over the selection and reach back when the opening is unsettled.
    bool enabled = false;

    /// Hard bound: the maximum number of reach-back increments ("never settles" cap;
    /// design §3). The loop also terminates at convergence or the score start.
    int maxReachSteps = 8;

    /// Reach-back increment size in ticks. 0 ⇒ one measure, derived from the score's
    /// time signature at the loaded-span edge (Layer 3's natural unit; design §2).
    /// A fixed positive value overrides it — the increment is an efficiency knob, not
    /// a guessed amount, so convergence is independent of it (design §5.3 / tests).
    int incrementTicks = 0;

    /// Trigger sensitivity: the selection's opening is treated as "unsettled" (so
    /// reach-back fires) when its leading-edge slice is "uncertain" OR its sequence-
    /// margin confidence is below this. Symmetrically, a reached-back context slice
    /// counts as a "settled key in view" (the convergence stop) only when it is NOT
    /// uncertain AND its confidence is at or above this. Default 0.0 ⇒ the decoder's
    /// own "uncertain" flag is the sole signal (design §3 primary criterion); a
    /// positive value broadens the trigger to low-margin openings (design §3 "or low
    /// sequence-margin"). The exact magnitude is a Phase-B calibration item, not set
    /// on the production path (which never enables reach-back at all).
    double minOpeningConfidence = 0.0;
};

/// Tunable parameters that differ between bridge and batch callers but do
/// not influence the structural orchestration.  Defaults match the bridge.
struct AnalyzeRegionsOptions {
    /// Region output granularity.
    HarmonicRegionGranularity granularity = HarmonicRegionGranularity::Smoothed;

    /// Pass 2 onset-Jaccard sub-boundary threshold.  Lower = more boundaries.
    /// Bridge reads this from IComposingAnalysisConfiguration; batch passes 0.25.
    double onsetBoundaryThreshold = 0.25;

    /// When true and ≥3 distinct pitch classes are already sounding at the
    /// region start tick, collectRegionTones skips notes whose onset is
    /// strictly after startTick (excludes mid-region look-ahead onsets).
    ///
    /// Batch passes true and bridge passes false — both INTENTIONAL. This
    /// divergence is confirmed correct; do not unify. On fully-notated scores
    /// (the batch path) dense region starts routinely contain mid-region
    /// passing tones, so suppressing strictly-later onsets keeps the chord
    /// identity clean. The bridge leaving it false is appropriate for its use
    /// case. A divergence investigation forced batch to false and measured a
    /// severe regression (Baroque BIR=false 25→47, Jazz BIR=false 13→18),
    /// confirming this flag is load-bearing on the batch path — NOT inherited
    /// legacy behaviour.
    bool excludeLookAheadOnDenseStart = false;

    /// Pass 1 minimum distinct PC count for analyzeChord to emit a candidate.
    /// When < 0 the caller's prefs.minDistinctPcsForCandidate is honoured
    /// unchanged.
    ///
    /// D2 UNIFIED — both paths now pass 1 (admit sparse 1–2 PC slices, Iter 75):
    /// the bridge sets it in notationharmonicrhythmbridge, the batch wrapper sets
    /// it in tools/batch_analyze.cpp. This was the last batch/bridge parameter
    /// divergence; it is resolved. Setting batch to 1 yields a net error reduction
    /// on both corpora.
    ///
    /// Known residual (queued for Iter 98) — bwv320 m27 b1 sparse-admission
    /// cascade. The earlier note here blamed greedy-expand boundary movement; the
    /// actual mechanism is temporal-context contamination, not a boundary shift.
    /// The coarse boundary that appears to "narrow" the C region (tick 37920) is a
    /// note-change boundary present with OR without sparse admission. What changes
    /// is the READ of the dense window [37440,37920): an admitted 2-PC Gm slice at
    /// [36960,37440) overwrites previousRootPc=G, and rootContinuityBonus (+0.40,
    /// no stepwise gate) tips that ~0.02-margin window from C to G6/E, which then
    /// fails to merge with the following C region. A "context-transparent sparse
    /// region" orchestrator change (skip advanceTemporalContext for ≤2-PC regions)
    /// suppresses it on the batch path but was REJECTED: it regresses the bridge —
    /// the sparse Corelli trio-sonata dominant entries genuinely need
    /// context-advance, so it breaks 4 notation tests and over-merges sparse
    /// classical music (mozart_k280 m9 IV absorbed into V65 per DCML). Iter 98
    /// will instead tighten rootContinuityBonus in chordanalyzer so it does not
    /// fire when the preceding region is itself a sparse/uncertain reading.
    int pass1MinDistinctPcsForCandidate = -1;

    /// Optional debug capture for pre-merge and post-merge region streams.
    RegionAnalysisHooks* hooks = nullptr;

    /// Architectural Layer 3 reach-back (selection-aware capability; default OFF ⇒
    /// production whole-score build, byte-identical). See ReachBackOptions.
    ReachBackOptions reachBack {};
};

/// Run the shared regional-analysis orchestrator over [startTick, endTick) and
/// return the merged HarmonicRegion sequence (or empty if no eligible content
/// was found).  Both notation::analyzeHarmonicRhythm (regional path) and
/// batch_analyze::analyzeScore call this directly.
std::vector<HarmonicRegion>
analyzeRegions(const mu::engraving::Score* score,
               const mu::engraving::Fraction& startTick,
               const mu::engraving::Fraction& endTick,
               const std::set<std::size_t>& excludeStaves,
               const ChordAnalyzerPreferences& prefs,
               const KeyModeAnalyzerPreferences& keyPrefs,
               const AnalyzeRegionsOptions& opts = {});

} // namespace region
} // namespace mu::composing::analysis
