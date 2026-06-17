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

#include "chordanalyzer.h"
#include "composing/analysis/function/harmonicfunctionlayer.h"

#include <algorithm>
#include <vector>

namespace fn = mu::composing::function;

namespace mu::composing::analysis {

ChordAnalysisDiagnosticResult RuleBasedChordAnalyzer::diagnoseChord(
    const std::vector<ChordAnalysisTone>& tones,
    int keySignatureFifths,
    KeySigMode keyMode,
    const ChordTemporalContext* context,
    const ChordAnalyzerPreferences& prefs) const
{
    ChordAnalysisDiagnosticResult diag;
    if (tones.empty()) { return diag; }

    // ── Replay the EXACT production pipeline ──────────────────────────────────
    // Byte-identical to test_helpers.h analyzeWithGates() and to every commit site in
    // regionanalyzer.cpp: analyzeChord → applyIter8691Pedal → applyPostScoringGates,
    // with the SAME tones / key / context / prefs the caller supplied. The snapshot and
    // gate context are captured purely for the introspection decoration below; passing
    // them out does not alter the result. diag.finalWinner is therefore the production
    // winner BY CONSTRUCTION — that identity (the whole point of Stage 2.3) is pinned by
    // Composing_DiagnoseTests.DiagnoseMatchesProductionPipeline.
    fn::ScoringSnapshot     snapshot;
    PostScoringGateContext  gateCtx;
    std::vector<ChordAnalysisResult> results =
        analyzeChord(tones, keySignatureFifths, keyMode, context, prefs, &gateCtx, &snapshot);

    // Region facts — straight from the snapshot the oracle actually built.
    diag.pcWeights   = snapshot.pcWeight;
    diag.distinctPcs = snapshot.distinctPcs;
    diag.keyTonicPc  = snapshot.keyTonicPc;
    diag.keyMode     = snapshot.keyMode;

    // ── ORACLE — per-cell vertical breakdown, copied from the snapshot ────────
    // These are the vertical-only terms the scoring oracle produced (no progression
    // signal); the competition adds rcb / w_seq / w_dim / steps on top. Kept (it is
    // the tool's value) but now sourced from the production snapshot, not re-scored.
    diag.oracleCells.reserve(snapshot.cells.size());
    for (const fn::ScoringCell& cell : snapshot.cells) {
        DiagnosticOracleCell oc;
        oc.bassPc           = cell.bassPc;
        oc.rootPc           = cell.rootPc;
        oc.templateIdx      = cell.tiePriority;
        oc.quality          = cell.quality;
        oc.basisIndep       = cell.basisIndep;
        oc.basisDep         = cell.basisDep;
        oc.complexityFactor = cell.complexityFactor;
        oc.augFactor        = cell.augFactor;
        oc.wCompleteBonus   = cell.wCompleteBonus;
        oc.appliedBassBonus = cell.appliedBassBonus;
        oc.verticalScore    = (cell.basisIndep + cell.basisDep)
                              * cell.complexityFactor * cell.augFactor
                              + cell.wCompleteBonus;
        diag.oracleCells.push_back(oc);
    }
    std::sort(diag.oracleCells.begin(), diag.oracleCells.end(),
              [](const DiagnosticOracleCell& a, const DiagnosticOracleCell& b) {
                  return a.verticalScore > b.verticalScore;
              });

    // ── COMPETITION — winning bass group, with the progression signals ───────
    // Scores are authoritative: gateCtx.rawCandidates is exactly the chosen bass group
    // the competition pipeline produced (post w_seq/w_dim/steps, post Gate R). For each
    // we recompute the additive signal components from the matching snapshot cell + ctx
    // via the SAME public fn:: functions applyHarmonicFunction() calls — a view of the
    // pipeline's inputs, NOT a second scorer. Gate R fires only in the Final phase, as
    // at the production call site.
    const bool finalPhase = (prefs.scoringPhase == fn::ScoringPhase::Final);
    const int  winBassPc  = gateCtx.bassPc;
    const int  prevRootPc = context ? context->previousRootPc : -1;
    const int  nextRootPc = context ? context->nextRootPc     : -1;
    const int  prevBassPc = context ? context->previousBassPc : -1;
    const int  nextBassPc = context ? context->nextBassPc     : -1;
    const ChordQuality prevQuality = context ? context->previousQuality : ChordQuality::Unknown;
    const bool stepFromPrev = context ? context->bassIsStepwiseFromPrevious : false;
    const bool stepToNext   = context ? context->bassIsStepwiseToNext       : false;
    diag.competition.reserve(gateCtx.rawCandidates.size());
    for (const RawCandidate& rc : gateCtx.rawCandidates) {
        DiagnosticCompetitionCandidate cc;
        cc.bassPc           = winBassPc;
        cc.rootPc           = rc.rootPc;
        cc.templateIdx      = rc.tiePriority;
        cc.quality          = rc.quality;
        cc.competitionScore = rc.score;
        cc.wDimBonus        = rc.wDimDelta;   // exact value the pipeline applied

        // Locate the matching snapshot cell (same winning bass, root, template).
        const fn::ScoringCell* cell = nullptr;
        for (const fn::ScoringCell& sc : snapshot.cells) {
            if (sc.bassPc == winBassPc && sc.rootPc == rc.rootPc
                && sc.tiePriority == rc.tiePriority) {
                cell = &sc;
                break;
            }
        }
        if (cell) {
            // Migrated temporal signals (Stage 3.3), recomputed via the same public fn::
            // functions the pipeline uses. Gate R now reads the reconstructed full basisDep
            // (cell.basisDep + inversionContextBonus) — the candidate's total inversion
            // credit — exactly as Pass A does.
            cc.resolutionBonus       = fn::resolutionEdgeBonus(cell->rootPc, cell->quality,
                                                               prevRootPc, prevQuality,
                                                               prefs.resolutionBonus);
            cc.inversionContextBonus = fn::inversionContextBonus(*cell, prevRootPc,
                                                                 stepFromPrev, stepToNext, prefs);
            const double fullBasisDep = cell->basisDep + cc.inversionContextBonus;
            const double rcbRaw = fn::rootContinuityBonus(cell->rootPc, prevRootPc,
                                                          prefs.rootContinuityBonus);
            const bool withheld = finalPhase
                && fn::gateRZeroesRootContinuity(*cell, fullBasisDep, rcbRaw);
            cc.rootContinuityBonusRaw        = rcbRaw;
            cc.rootContinuityWithheldByGateR = withheld;
            cc.rootContinuityBonus           = withheld ? 0.0 : rcbRaw;
            if (finalPhase) {
                cc.wSeqBonus    = fn::wSeqBonus(cell->rootPc, nextRootPc,
                                               snapshot.distinctPcs, snapshot.jointScoringEnabled);
                cc.stepInBonus  = fn::wStepInBonus(winBassPc, cell->rootPc,
                                                  snapshot.jointScoringEnabled, prevBassPc);
                cc.stepOutBonus = fn::wStepOutBonus(winBassPc, cell->rootPc,
                                                   snapshot.jointScoringEnabled, nextBassPc);
            }
        }
        diag.competition.push_back(cc);
    }

    // ── POST-GATES — run the production tail, recording which stage moves it ──
    // Mirrors analyzeWithGates(): the post passes run only when analyzeChord returned a
    // non-empty result. The winner identity is compared after each stage so the dump can
    // attribute a winner change to Iter 86/91/pedal vs gates A–L.
    const auto sameIdentity = [](const ChordAnalysisResult& a, const ChordAnalysisResult& b) {
        return a.identity.rootPc == b.identity.rootPc
            && a.identity.bassPc == b.identity.bassPc
            && a.identity.quality == b.identity.quality
            && a.identity.extensions == b.identity.extensions;
    };
    if (!results.empty()) {
        const ChordAnalysisResult competitionWinner = results.front();
        diag.postGates.hasCompetitionWinner    = true;
        diag.postGates.competitionWinnerRootPc  = competitionWinner.identity.rootPc;
        diag.postGates.competitionWinnerBassPc  = competitionWinner.identity.bassPc;
        diag.postGates.competitionWinnerQuality = competitionWinner.identity.quality;
        diag.postGates.competitionWinnerScore   = competitionWinner.identity.score;

        applyIter8691Pedal(results, gateCtx, context, prefs);
        const ChordAnalysisResult afterIter = results.front();
        diag.postGates.iter8691ChangedWinner = !sameIdentity(afterIter, competitionWinner);

        applyPostScoringGates(results, prefs, context, gateCtx);
        const ChordAnalysisResult finalWinner = results.front();
        diag.postGates.gatesChangedWinner = !sameIdentity(finalWinner, afterIter);

        diag.finalWinner = finalWinner;
        diag.hasWinner   = true;
        diag.bassPc      = finalWinner.identity.bassPc;
    }

    return diag;
}

} // namespace mu::composing::analysis
