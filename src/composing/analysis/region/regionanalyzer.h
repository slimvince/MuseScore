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
    /// Bridge uses 1 to admit sparse 1–2 PC slices (Iter 75); batch uses the
    /// caller-supplied prefs.minDistinctPcsForCandidate.  When < 0 the
    /// caller's prefs value is honoured unchanged.
    ///
    /// Future iteration candidate: setting batch to 1 (matching the bridge) was
    /// tested and produced a net error reduction (Baroque total 59→52, Jazz
    /// total 69→62), but it tripped the Jazz BIR=false hard stop by exactly +1
    /// (13→14). Revisit admitting sparse 1–2 PC regions on the batch path if the
    /// Jazz BIR=false hard stop is relaxed, or if a structural entry guard can
    /// recover the single failing case while preserving the sparse-admission
    /// gains elsewhere.
    int pass1MinDistinctPcsForCandidate = -1;

    /// Optional debug capture for pre-merge and post-merge region streams.
    RegionAnalysisHooks* hooks = nullptr;
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
