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

// harmonicfunctionlayer.cpp

#include "harmonicfunctionlayer.h"

#include <algorithm>
#include <limits>
#include <unordered_map>

namespace mu::composing::function {

void applyHarmonicFunction(std::vector<analysis::ChordAnalysisResult>& candidates,
                           analysis::ChordAnalysisResult& chosenResult,
                           const HarmonicFunctionContext& ctx,
                           const ScoringSnapshot* snapshot,
                           const analysis::ChordAnalyzerPreferences* prefs)
{
    // No snapshot → E1/E2a/E2b no-op.
    if (!snapshot || !prefs) return;
    if (!prefs->suppressProgressionSignals) return;
    if (candidates.empty()) return;

    // ── Re-score all snapshot cells with progression signals applied ────────
    //
    // When suppressProgressionSignals was true, the scorer stored CLEAN basisIndep
    // values (no rootContinuityBonus), wSeqBonus=0, wDimDelta=0 in every cell.
    // Re-apply the signals now. rootContinuityBonus is folded into basisIndep
    // (which is then multiplied by cf × af), so it must be added BEFORE the
    // multiply — not as a flat post-multiply additive.

    auto rescore = [&](const ScoringCell& cell) -> std::pair<double, double> {
        const double rcb = rootContinuityBonus(
            cell.rootPc, ctx.previousRootPc, prefs->rootContinuityBonus);
        const double newBasisIndep = cell.basisIndep + rcb;
        const double scoreNoWDim =
            (newBasisIndep + cell.basisDep)
            * cell.complexityFactor * cell.augFactor
            + cell.wCompleteBonus
            + wSeqBonus(cell.rootPc, ctx.nextRootPc,
                        snapshot->distinctPcs,
                        snapshot->jointScoringEnabled, false);
        const double newWDimDelta = wDimBonus(
            cell.rootPc, cell.quality, ctx.nextRootPc,
            snapshot->distinctPcs, snapshot->jointScoringEnabled, false);
        return { scoreNoWDim, scoreNoWDim + newWDimDelta };
    };

    // Per-bass best scores for the quality guard.
    std::unordered_map<int, double> bestWithPerBass;
    std::unordered_map<int, double> bestWithoutPerBass;
    std::unordered_map<int, analysis::ChordQuality> bestWithQualityPerBass;

    for (const auto& cell : snapshot->cellsWithWDim) {
        auto [snw, sw] = rescore(cell);
        auto it = bestWithPerBass.find(cell.bassPc);
        if (it == bestWithPerBass.end() || sw > it->second) {
            bestWithPerBass[cell.bassPc]        = sw;
            bestWithQualityPerBass[cell.bassPc] = cell.quality;
        }
        (void)snw;
    }
    for (const auto& cell : snapshot->cellsWithoutWDim) {
        auto [snw, sw] = rescore(cell);
        auto it = bestWithoutPerBass.find(cell.bassPc);
        if (it == bestWithoutPerBass.end() || snw > it->second) {
            bestWithoutPerBass[cell.bassPc] = snw;
        }
        (void)sw;
    }

    // ── Quality guard (replicates analyzeChord's post-bonus guard) ──────────
    int    globalBestBassPcWith = -1;
    double globalBestScoreWith  = -std::numeric_limits<double>::infinity();
    for (const auto& [bp, sc] : bestWithPerBass) {
        if (sc > globalBestScoreWith) {
            globalBestScoreWith  = sc;
            globalBestBassPcWith = bp;
        }
    }

    // Accept with-wDim iff its winner quality is Dim or HalfDim.
    const bool acceptWithWDim = (globalBestBassPcWith >= 0)
        && (bestWithQualityPerBass[globalBestBassPcWith]
                == analysis::ChordQuality::Diminished
            || bestWithQualityPerBass[globalBestBassPcWith]
                == analysis::ChordQuality::HalfDiminished);

    // Select the winning variant's cells.
    const auto& winningCells = acceptWithWDim
        ? snapshot->cellsWithWDim
        : snapshot->cellsWithoutWDim;

    // ── Find the global winner cell ──────────────────────────────────────────
    const ScoringCell* winnerCell = nullptr;
    double             winnerScore = -std::numeric_limits<double>::infinity();

    for (const auto& cell : winningCells) {
        auto [snw, sw] = rescore(cell);
        const double s = acceptWithWDim ? sw : snw;
        if (s > winnerScore) {
            winnerScore = s;
            winnerCell  = &cell;
        }
    }

    if (!winnerCell) return;   // Should not happen.

    // ── Look up winner in candidates[] ──────────────────────────────────────
    //
    // Match on (tiePriority, rootPc). tiePriority uniquely identifies the
    // template; rootPc disambiguates across templates with the same index
    // (impossible by definition, but belt-and-suspenders).
    int winnerIdx = -1;
    for (int i = 0; i < static_cast<int>(candidates.size()); ++i) {
        if (candidates[i].identity.tiePriority == winnerCell->tiePriority
            && candidates[i].identity.rootPc    == winnerCell->rootPc) {
            winnerIdx = i;
            break;
        }
    }

    if (winnerIdx < 0) {
        // Edge case: winner was filtered out by the suppressed-signal threshold
        // (this can happen if the true winner's suppressed score is below the
        // suppressed-signal threshold, i.e. a different bass won the suppressed
        // pass). Do NOT crash; keep the suppressed-signal winner as-is.
        return;
    }

    // ── Promote winner to position 0 ─────────────────────────────────────────
    if (winnerIdx != 0) {
        std::rotate(candidates.begin(),
                    candidates.begin() + winnerIdx,
                    candidates.begin() + winnerIdx + 1);
    }
    chosenResult = candidates[0];

    // ── Correct bassPc / bassTpc if re-scored winner used a different bass ──
    if (candidates[0].identity.bassPc != winnerCell->bassPc) {
        candidates[0].identity.bassPc  = winnerCell->bassPc;
        candidates[0].identity.bassTpc = winnerCell->bassTpc;
        chosenResult = candidates[0];
    }

    // ── Trim back to normal top-3 cap ────────────────────────────────────────
    if (candidates.size() > 3) {
        candidates.resize(3);
    }
}

double rootContinuityBonus(int candidateRootPc, int previousRootPc,
                           double bonusValue)
{
    return (candidateRootPc == previousRootPc) ? bonusValue : 0.0;
}

double wSeqBonus(int candRootPc, int nextRootPc, int distinctPcs,
                 bool jointScoringEnabled, bool explorationMode)
{
    if (!jointScoringEnabled || explorationMode) return 0.0;
    if (nextRootPc < 0 || distinctPcs < 4) return 0.0;
    const int delta = ((nextRootPc - candRootPc) % 12 + 12) % 12;
    return (delta == 5) ? kWSeq : 0.0;
}

double wDimBonus(int candRootPc, analysis::ChordQuality quality,
                 int nextRootPc, int distinctPcs,
                 bool jointScoringEnabled, bool explorationMode)
{
    if (!jointScoringEnabled || explorationMode) return 0.0;
    if (nextRootPc < 0 || distinctPcs < 4) return 0.0;
    using Q = analysis::ChordQuality;
    if (quality != Q::Diminished && quality != Q::HalfDiminished) return 0.0;
    const int delta = ((nextRootPc - candRootPc) % 12 + 12) % 12;
    return (delta == 1) ? kWDim : 0.0;
}

} // namespace mu::composing::function
