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

// functionlayer_tests.cpp — Stage 1a (implementation_roadmap.md items 1.2 + 1.7)
//
// Pins the CURRENT behavior of the competition pipeline's progression-signal
// bonuses (docs/scoring_model.md §4) and the floating-point tie policy (§3
// "Floating-point tie policy"). These tests are the differential baseline for
// the Stage 3 decoder migration: every behavior pinned here is a proof
// obligation for the decoder's beam-1 byte-identity gate.
//
// Directly tested free functions (exposed in harmonicfunctionlayer.h):
//   rootContinuityBonus, wSeqBonus, wDimBonus, wStepInBonus, wStepOutBonus.
// Tested end-to-end through applyHarmonicFunction() (file-local in the .cpp):
//   applyStepBonusGuard (all four load-bearing guards, §4 w_stepIn/w_stepOut),
//   the wDim post-bonus quality guard (Iter 97a-v3, §4 w_dim),
//   the score formula + term ordering (§3),
//   the sort comparator / FP tie policy (§3).
//
// Gate R's predicate + phase gating are already pinned in gater_tests.cpp.

#include <gtest/gtest.h>

#include <vector>

#include "composing/analysis/function/harmonicfunctionlayer.h"

using namespace mu::composing::function;
namespace ana = mu::composing::analysis;
using ana::ChordQuality;

namespace {

// Neutral-factor cell builder: complexityFactor = augFactor = 1.0, everything
// additive zeroed, so a cell's pipeline score equals basisIndep plus whatever
// progression signals the test wires up.
ScoringCell makeCell(int bassPc, int rootPc, int tiePriority, ChordQuality quality,
                     int intervalCount, double basisIndep)
{
    ScoringCell c{};
    c.bassPc           = bassPc;
    c.bassTpc          = -1;
    c.rootPc           = rootPc;
    c.tiePriority      = tiePriority;
    c.quality          = quality;
    c.intervalCount    = intervalCount;
    c.basisIndep       = basisIndep;
    c.basisDep         = 0.0;
    c.complexityFactor = 1.0;
    c.augFactor        = 1.0;
    c.wCompleteBonus   = 0.0;
    c.appliedBassBonus = 0.0;
    return c;
}

ScoringSnapshot makeSnapshot(std::vector<ScoringCell> cells, int distinctPcs,
                             bool jointScoringEnabled)
{
    ScoringSnapshot s;
    s.cells               = std::move(cells);
    s.distinctPcs         = distinctPcs;
    s.jointScoringEnabled = jointScoringEnabled;
    s.tpcForPc.fill(-1);
    return s;
}

// Empty progression context: no neighbours, nothing fires.
HarmonicFunctionContext makeContext()
{
    return HarmonicFunctionContext{};
}

std::vector<ana::ChordAnalysisResult> runPipeline(const ScoringSnapshot& snapshot,
                                                  const HarmonicFunctionContext& ctx,
                                                  ScoringPhase phase = ScoringPhase::Final)
{
    const ana::ChordAnalyzerPreferences prefs;
    std::vector<ana::ChordAnalysisResult> results;
    ana::ChordAnalysisResult chosen;
    applyHarmonicFunction(snapshot, ctx, prefs, results, chosen, nullptr, phase);
    return results;
}

} // namespace

// ═════════════════════════════════════════════════════════════════════════════
// §4 constants — pin the documented values so a silent retune fails loudly.
// ═════════════════════════════════════════════════════════════════════════════

TEST(Composing_FunctionLayerTests, Constants_MatchScoringModelSection4)
{
    EXPECT_DOUBLE_EQ(kWSeq, 0.20);
    EXPECT_DOUBLE_EQ(kWDim, 0.15);
    EXPECT_DOUBLE_EQ(kWStepIn, 0.10);
    EXPECT_DOUBLE_EQ(kWStepOut, 0.10);
    EXPECT_NEAR(kStepBudget, 0.21, 1e-12);   // kWStepIn + kWStepOut + 0.01
    EXPECT_DOUBLE_EQ(kScoreThresholdRatio, 0.75);
    const ana::ChordAnalyzerPreferences prefs;
    EXPECT_DOUBLE_EQ(prefs.rootContinuityBonus, 0.40);
}

// ═════════════════════════════════════════════════════════════════════════════
// 1. rootContinuityBonus — §4 "rootContinuityBonus": fires iff
//    candidateRootPc == previousRootPc, returns the configured bonus.
// ═════════════════════════════════════════════════════════════════════════════

TEST(Composing_FunctionLayerTests, RootContinuity_FiresOnEqualRoot)
{
    EXPECT_DOUBLE_EQ(rootContinuityBonus(5, 5, 0.40), 0.40);
    EXPECT_DOUBLE_EQ(rootContinuityBonus(0, 0, 0.25), 0.25);   // configured value passes through
}

TEST(Composing_FunctionLayerTests, RootContinuity_NoFireOnDifferentOrUnknownRoot)
{
    EXPECT_DOUBLE_EQ(rootContinuityBonus(5, 4, 0.40), 0.0);
    // previousRootPc == -1 (unknown predecessor): no candidate rootPc equals -1,
    // so the bonus never fires — pins the sentinel handling.
    EXPECT_DOUBLE_EQ(rootContinuityBonus(5, -1, 0.40), 0.0);
}

// ═════════════════════════════════════════════════════════════════════════════
// 2. wSeqBonus — §4 "w_seq": fires on (nextRootPc - candRootPc) mod 12 == 5
//    (descending-fifth root motion), distinctPcs >= 4, jointScoringEnabled.
// ═════════════════════════════════════════════════════════════════════════════

TEST(Composing_FunctionLayerTests, WSeq_FiresOnPerfectFourthUpToNextRoot)
{
    EXPECT_DOUBLE_EQ(wSeqBonus(/*cand*/ 0, /*next*/ 5, /*distinctPcs*/ 4, true), kWSeq);
    // mod-12 wraparound: G (7) → C (0) is also delta 5.
    EXPECT_DOUBLE_EQ(wSeqBonus(7, 0, 4, true), kWSeq);
    EXPECT_DOUBLE_EQ(wSeqBonus(9, 2, 5, true), kWSeq);
}

TEST(Composing_FunctionLayerTests, WSeq_NoFireWhenAnyConditionBroken)
{
    EXPECT_DOUBLE_EQ(wSeqBonus(0, 4, 4, true), 0.0);    // interval != 5
    EXPECT_DOUBLE_EQ(wSeqBonus(0, 7, 4, true), 0.0);    // P5, not P4 (direction matters)
    EXPECT_DOUBLE_EQ(wSeqBonus(0, 5, 3, true), 0.0);    // distinctPcs < 4
    EXPECT_DOUBLE_EQ(wSeqBonus(0, 5, 4, false), 0.0);   // jointScoring disabled
    EXPECT_DOUBLE_EQ(wSeqBonus(0, -1, 4, true), 0.0);   // nextRootPc unknown
}

// §4: w_seq is a CHORD-level signal — no bass / root-position parameter exists in
// the signature. The end-to-end inversion-independence pin is in
// ScoreFormula_SingleCellHandComputed below (slash cell still receives w_seq).

// ═════════════════════════════════════════════════════════════════════════════
// 3. wDimBonus — §4 "w_dim": Dim/HalfDim candidate one semitone below
//    nextRootPc, distinctPcs >= 4 (quality-flip guard), jointScoringEnabled.
// ═════════════════════════════════════════════════════════════════════════════

TEST(Composing_FunctionLayerTests, WDim_FiresForDimAndHalfDimLeadingTone)
{
    EXPECT_DOUBLE_EQ(wDimBonus(11, ChordQuality::Diminished, 0, 4, true), kWDim);
    EXPECT_DOUBLE_EQ(wDimBonus(11, ChordQuality::HalfDiminished, 0, 4, true), kWDim);
    EXPECT_DOUBLE_EQ(wDimBonus(6, ChordQuality::Diminished, 7, 4, true), kWDim);
}

TEST(Composing_FunctionLayerTests, WDim_NoFireOnWrongQualityIntervalOrSparseRegion)
{
    EXPECT_DOUBLE_EQ(wDimBonus(11, ChordQuality::Major, 0, 4, true), 0.0);   // quality guard
    EXPECT_DOUBLE_EQ(wDimBonus(11, ChordQuality::Minor, 0, 4, true), 0.0);
    // distinctPcs >= 4 is intentional (§4): the bonus is a rotation-correction
    // signal, NOT a quality-flip signal; 3-PC sparse dim regions must not flip.
    EXPECT_DOUBLE_EQ(wDimBonus(11, ChordQuality::Diminished, 0, 3, true), 0.0);
    EXPECT_DOUBLE_EQ(wDimBonus(11, ChordQuality::Diminished, 1, 4, true), 0.0);  // interval != 1
    EXPECT_DOUBLE_EQ(wDimBonus(11, ChordQuality::Diminished, -1, 4, true), 0.0); // next unknown
    EXPECT_DOUBLE_EQ(wDimBonus(11, ChordQuality::Diminished, 0, 4, false), 0.0); // joint off
}

// ═════════════════════════════════════════════════════════════════════════════
// 4. wStepInBonus / wStepOutBonus — §4 "w_stepIn / w_stepOut": root-position
//    candidate whose bass moves by semitone or whole tone from previousBassPc /
//    to nextBassPc (either direction; deltas {1, 2, 10, 11}).
// ═════════════════════════════════════════════════════════════════════════════

TEST(Composing_FunctionLayerTests, WStepIn_FiresOnSemitoneOrWholeToneEitherDirection)
{
    EXPECT_DOUBLE_EQ(wStepInBonus(5, 5, true, /*prev*/ 3), kWStepIn);   // up a tone
    EXPECT_DOUBLE_EQ(wStepInBonus(5, 5, true, 4), kWStepIn);            // up a semitone
    EXPECT_DOUBLE_EQ(wStepInBonus(5, 5, true, 6), kWStepIn);            // down a semitone
    EXPECT_DOUBLE_EQ(wStepInBonus(5, 5, true, 7), kWStepIn);            // down a tone
}

TEST(Composing_FunctionLayerTests, WStepIn_NoFireOnLeapSlashOrMissingContext)
{
    EXPECT_DOUBLE_EQ(wStepInBonus(5, 5, true, 1), 0.0);    // leap (M3)
    EXPECT_DOUBLE_EQ(wStepInBonus(5, 5, true, 0), 0.0);    // leap (P4)
    EXPECT_DOUBLE_EQ(wStepInBonus(7, 5, true, 5), 0.0);    // slash: bassPc != rootPc
    EXPECT_DOUBLE_EQ(wStepInBonus(5, 5, true, -1), 0.0);   // no predecessor bass
    EXPECT_DOUBLE_EQ(wStepInBonus(5, 5, true, 5), 0.0);    // same bass = no motion
    EXPECT_DOUBLE_EQ(wStepInBonus(5, 5, false, 3), 0.0);   // jointScoring disabled
}

TEST(Composing_FunctionLayerTests, WStepOut_MirrorsStepInAgainstNextBass)
{
    EXPECT_DOUBLE_EQ(wStepOutBonus(5, 5, true, /*next*/ 7), kWStepOut);  // up a tone
    EXPECT_DOUBLE_EQ(wStepOutBonus(5, 5, true, 4), kWStepOut);           // down a semitone
    EXPECT_DOUBLE_EQ(wStepOutBonus(5, 5, true, 9), 0.0);    // leap
    EXPECT_DOUBLE_EQ(wStepOutBonus(7, 5, true, 8), 0.0);    // slash
    EXPECT_DOUBLE_EQ(wStepOutBonus(5, 5, true, -1), 0.0);   // no successor bass
    EXPECT_DOUBLE_EQ(wStepOutBonus(5, 5, true, 5), 0.0);    // same bass
    EXPECT_DOUBLE_EQ(wStepOutBonus(5, 5, false, 7), 0.0);   // jointScoring disabled
}

// ═════════════════════════════════════════════════════════════════════════════
// 5. applyStepBonusGuard (file-local — exercised through applyHarmonicFunction).
//    §4 w_stepIn/w_stepOut lists four load-bearing guards; one test each.
// ═════════════════════════════════════════════════════════════════════════════

// Guard 2 (root-position only): the Pass B loop skips candidates whose rootPc
// differs from the group bass, so a slash candidate gets no step bonus even
// though its BASS steps from previousBassPc.
TEST(Composing_FunctionLayerTests, StepGuard_RootPositionOnly_SlashGetsNoBonus)
{
    ScoringSnapshot snapshot = makeSnapshot(
        { makeCell(/*bass*/ 7, /*root*/ 0, /*tpl Major*/ 0, ChordQuality::Major, 3, 1.0) },
        /*distinctPcs*/ 3, /*joint*/ true);
    HarmonicFunctionContext ctx = makeContext();
    ctx.previousBassPc = 5;   // bass 7 steps from 5 — would fire were it root-position

    const auto results = runPipeline(snapshot, ctx);
    ASSERT_FALSE(results.empty());
    EXPECT_NEAR(results.front().identity.score, 1.0, 1e-9);   // no +0.10
}

// Control for guard 2 + baseline for the guards below: the root-position twin
// DOES receive the step-in bonus.
TEST(Composing_FunctionLayerTests, StepGuard_RootPositionCandidateGetsBonus)
{
    ScoringSnapshot snapshot = makeSnapshot(
        { makeCell(5, 5, 0, ChordQuality::Major, 3, 1.0) },
        3, true);
    HarmonicFunctionContext ctx = makeContext();
    ctx.previousBassPc = 3;   // 5 from 3 = whole tone

    const auto results = runPipeline(snapshot, ctx);
    ASSERT_FALSE(results.empty());
    EXPECT_NEAR(results.front().identity.score, 1.0 + kWStepIn, 1e-9);
}

// Guard 3 (m7-family surgical guard): a competitor of quality HalfDim at
// (candBassPc - 3) mod 12 scoring within kStepBudget of the candidate's
// unbonused score blocks the step bonus...
TEST(Composing_FunctionLayerTests, StepGuard_M7FamilyCompetitorInsideBudgetBlocks)
{
    // cand: F major root-position, unbonused 1.0. Competitor: Dø-shaped HalfDim
    // (rootPc 2 = (5-3) mod 12) at 0.80 >= 1.0 - kStepBudget (0.79) → blocked.
    ScoringSnapshot snapshot = makeSnapshot(
        { makeCell(5, 5, 0, ChordQuality::Major, 3, 1.0),
          makeCell(5, 2, 8, ChordQuality::HalfDiminished, 4, 0.80) },
        3, true);
    HarmonicFunctionContext ctx = makeContext();
    ctx.previousBassPc = 3;

    const auto results = runPipeline(snapshot, ctx);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 5);
    EXPECT_NEAR(results.front().identity.score, 1.0, 1e-9);   // bonus suppressed
}

// ...and a competitor just OUTSIDE the budget does not block (boundary pair).
TEST(Composing_FunctionLayerTests, StepGuard_M7FamilyCompetitorOutsideBudgetDoesNotBlock)
{
    // Competitor at 0.78 < 1.0 - kStepBudget (0.79) → not blocked.
    ScoringSnapshot snapshot = makeSnapshot(
        { makeCell(5, 5, 0, ChordQuality::Major, 3, 1.0),
          makeCell(5, 2, 8, ChordQuality::HalfDiminished, 4, 0.78) },
        3, true);
    HarmonicFunctionContext ctx = makeContext();
    ctx.previousBassPc = 3;

    const auto results = runPipeline(snapshot, ctx);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 5);
    EXPECT_NEAR(results.front().identity.score, 1.0 + kWStepIn, 1e-9);
}

// Guard 3 quality scope: "Min7-shaped" means quality Minor AND intervalCount == 4.
// A plain minor TRIAD (intervalCount 3) at the competitor root does NOT block —
// pins the isMin7 discrimination inside applyStepBonusGuard.
TEST(Composing_FunctionLayerTests, StepGuard_MinorTriadCompetitorDoesNotBlock_Min7Does)
{
    // Minor triad competitor (intervalCount 3): not in the m7 family → no block.
    ScoringSnapshot triadSnapshot = makeSnapshot(
        { makeCell(5, 5, 0, ChordQuality::Major, 3, 1.0),
          makeCell(5, 2, 4, ChordQuality::Minor, 3, 0.80) },
        3, true);
    HarmonicFunctionContext ctx = makeContext();
    ctx.previousBassPc = 3;

    auto results = runPipeline(triadSnapshot, ctx);
    ASSERT_FALSE(results.empty());
    EXPECT_NEAR(results.front().identity.score, 1.0 + kWStepIn, 1e-9);

    // Same competitor as Min7 (quality Minor, intervalCount 4): blocks.
    ScoringSnapshot min7Snapshot = makeSnapshot(
        { makeCell(5, 5, 0, ChordQuality::Major, 3, 1.0),
          makeCell(5, 2, 5, ChordQuality::Minor, 4, 0.80) },
        3, true);
    results = runPipeline(min7Snapshot, ctx);
    ASSERT_FALSE(results.empty());
    EXPECT_NEAR(results.front().identity.score, 1.0, 1e-9);
}

// Guard 4 (Power exclusion): a Power-quality candidate gets no step bonus.
TEST(Composing_FunctionLayerTests, StepGuard_PowerQualityExcluded)
{
    ScoringSnapshot snapshot = makeSnapshot(
        { makeCell(5, 5, /*tpl Power*/ 16, ChordQuality::Power, 2, 1.0) },
        2, true);
    HarmonicFunctionContext ctx = makeContext();
    ctx.previousBassPc = 3;

    const auto results = runPipeline(snapshot, ctx);
    ASSERT_FALSE(results.empty());
    EXPECT_NEAR(results.front().identity.score, 1.0, 1e-9);
}

// Guard 1 (phase gate): in ScoringPhase::Segmentation the Pass B call is
// skipped entirely (applyProgressionSignals == false), so no step bonus.
// Step-bonus analogue of GateR_PhaseGated_FinalFiresSegmentationSkips.
TEST(Composing_FunctionLayerTests, StepGuard_SegmentationPhaseSuppressesStepBonus)
{
    ScoringSnapshot snapshot = makeSnapshot(
        { makeCell(5, 5, 0, ChordQuality::Major, 3, 1.0) },
        3, true);
    HarmonicFunctionContext ctx = makeContext();
    ctx.previousBassPc = 3;

    const auto finalResults = runPipeline(snapshot, ctx, ScoringPhase::Final);
    const auto segResults   = runPipeline(snapshot, ctx, ScoringPhase::Segmentation);
    ASSERT_FALSE(finalResults.empty());
    ASSERT_FALSE(segResults.empty());
    EXPECT_NEAR(finalResults.front().identity.score, 1.0 + kWStepIn, 1e-9);
    EXPECT_NEAR(segResults.front().identity.score, 1.0, 1e-9);
}

// ═════════════════════════════════════════════════════════════════════════════
// 6. wDim post-bonus quality guard (Iter 97a-v3, §4 "w_dim") — the pipeline
//    keeps with-wDim and without-wDim variants and accepts the with-variant
//    only if its global winner is Dim/HalfDim.
// ═════════════════════════════════════════════════════════════════════════════

// Cross-bass contamination: the wDim bonus inflates a Dim competitor enough to
// block the F-major candidate's step bonus (m7-family guard) in the WITH
// variant only, handing the with-variant win to a different bass group whose
// winner is Major. Winner not Dim/HalfDim → the guard falls back to the
// without-wDim result (F major, step bonus intact).
TEST(Composing_FunctionLayerTests, WDimPostBonusGuard_RejectsContaminatedWithVariant)
{
    // Group bass=5: F major (root-position, 1.0, step-in eligible from prev bass 3)
    //               + D° (rootPc 2 = competitor slot, 0.70, wDim-eligible: next root 3).
    // Group bass=7: G major 1.05, no step eligibility.
    //
    // without-wDim: D° 0.70 < 0.79 → F gets +0.10 → group 5 wins at 1.10.
    // with-wDim:    D° 0.85 >= 0.79 → F blocked at 1.00 → group 7 wins at 1.05,
    //               winner quality Major → NOT Dim/HalfDim → fallback to without.
    ScoringSnapshot snapshot = makeSnapshot(
        { makeCell(5, 5, 0, ChordQuality::Major, 3, 1.0),
          makeCell(5, 2, 6, ChordQuality::Diminished, 3, 0.70),
          makeCell(7, 7, 0, ChordQuality::Major, 3, 1.05) },
        /*distinctPcs*/ 4, true);
    HarmonicFunctionContext ctx = makeContext();
    ctx.previousBassPc = 3;
    ctx.nextRootPc     = 3;   // (3 - 2) mod 12 == 1 → wDim fires on the D° cell

    const auto results = runPipeline(snapshot, ctx);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 5);                        // F, not G
    EXPECT_NEAR(results.front().identity.score, 1.0 + kWStepIn, 1e-9);    // without-variant
}

// Clean acceptance: the with-wDim winner IS Diminished → with-variant kept,
// and the wDim bonus legitimately overturns a higher-scoring rival bass group.
TEST(Composing_FunctionLayerTests, WDimPostBonusGuard_AcceptsDimWinner)
{
    // Group bass=0: C° 1.0, wDim-eligible (next root 1) → with-score 1.15.
    // Group bass=7: G major 1.05.
    // without-wDim winner would be G (1.05); with-wDim winner is C° (1.15) —
    // quality Diminished → accepted.
    ScoringSnapshot snapshot = makeSnapshot(
        { makeCell(0, 0, 6, ChordQuality::Diminished, 3, 1.0),
          makeCell(7, 7, 0, ChordQuality::Major, 3, 1.05) },
        4, true);
    HarmonicFunctionContext ctx = makeContext();
    ctx.nextRootPc = 1;

    const auto results = runPipeline(snapshot, ctx);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 0);
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Diminished);
    EXPECT_NEAR(results.front().identity.score, 1.0 + kWDim, 1e-9);
}

// ═════════════════════════════════════════════════════════════════════════════
// 7. Score formula integration — §3:
//    score = (basisIndep + rcb + basisDep) × complexityFactor × augFactor
//          + wCompleteBonus + wSeq
//    One hand-computed single-cell snapshot pins the formula and term ordering
//    (rcb folded in BEFORE the multiply; wComplete/wSeq added AFTER).
//    The cell is a SLASH (bassPc != rootPc), which also pins that w_seq is
//    inversion-independent (§4: chord-level signal, no root-position condition).
// ═════════════════════════════════════════════════════════════════════════════

TEST(Composing_FunctionLayerTests, ScoreFormula_SingleCellHandComputed)
{
    ScoringCell cell = makeCell(/*bass*/ 7, /*root*/ 2, /*tpl Min7*/ 5,
                                ChordQuality::Minor, 4, /*basisIndep*/ 1.3);
    cell.basisDep         = 0.25;   // > 0 → Gate R spares the rcb
    cell.complexityFactor = 0.9;
    cell.augFactor        = 0.8;
    cell.wCompleteBonus   = 0.5;

    ScoringSnapshot snapshot = makeSnapshot({ cell }, 4, true);
    HarmonicFunctionContext ctx = makeContext();
    ctx.previousRootPc = 2;   // == rootPc → rcb = prefs.rootContinuityBonus (0.40)
    ctx.nextRootPc     = 7;   // (7 - 2) mod 12 == 5 → wSeq fires (despite slash bass)

    const auto results = runPipeline(snapshot, ctx);
    ASSERT_FALSE(results.empty());
    // (1.3 + 0.40 + 0.25) * 0.9 * 0.8 + 0.5 + 0.20 = 1.95 * 0.72 + 0.7 = 2.104
    EXPECT_NEAR(results.front().identity.score,
                (1.3 + 0.40 + 0.25) * 0.9 * 0.8 + 0.5 + kWSeq, 1e-12);
    EXPECT_NEAR(results.front().identity.score, 2.104, 1e-9);
}

// ═════════════════════════════════════════════════════════════════════════════
// Tie stability — §3 "Floating-point tie policy" (roadmap 1.7). Comparator:
//   1. higher score (exact double inequality), 2. lower tiePriority,
//   3. lower rootPc. No epsilon anywhere.
// ═════════════════════════════════════════════════════════════════════════════

// Exact-tie determinism: bitwise-identical scores, different tiePriority →
// lower template index wins. Natural §2 fixture: Sus4♭5 (tpl 7) vs HalfDim
// (tpl 8) — when only their shared interval subset {0,6,10} sounds, both
// templates score identically at the same root, and Sus4♭5 is preferred.
TEST(Composing_FunctionLayerTests, TiePolicy_ExactTie_LowerTiePriorityWins)
{
    // HalfDim pushed FIRST so insertion order cannot mask the comparator.
    ScoringSnapshot snapshot = makeSnapshot(
        { makeCell(6, 0, /*tpl HalfDim*/ 8, ChordQuality::HalfDiminished, 4, 1.0),
          makeCell(6, 0, /*tpl Sus4b5*/ 7, ChordQuality::Suspended4, 4, 1.0) },
        3, false);

    const auto results = runPipeline(snapshot, makeContext());
    ASSERT_GE(results.size(), 2u);
    EXPECT_EQ(results.front().identity.tiePriority, 7);
    EXPECT_EQ(results[1].identity.tiePriority, 8);
    EXPECT_DOUBLE_EQ(results.front().identity.score, results[1].identity.score);
}

// Exact-tie rootPc fallback: identical score AND tiePriority → lower rootPc wins.
TEST(Composing_FunctionLayerTests, TiePolicy_ExactTie_LowerRootPcBreaksFullTie)
{
    // Same template (Major, tpl 0), same score, roots 9 and 4 — 9 pushed first.
    ScoringSnapshot snapshot = makeSnapshot(
        { makeCell(0, 9, 0, ChordQuality::Major, 3, 1.0),
          makeCell(0, 4, 0, ChordQuality::Major, 3, 1.0) },
        3, false);

    const auto results = runPipeline(snapshot, makeContext());
    ASSERT_GE(results.size(), 2u);
    EXPECT_EQ(results.front().identity.rootPc, 4);
    EXPECT_EQ(results[1].identity.rootPc, 9);
}

// Near-tie canary: a 0.02 margin (the Δ=+7b class) is decided purely by which
// double is larger — tiePriority must NOT intervene. This is the canary that
// FP re-association (compiler/optimization-flag/platform changes re-ordering
// the score arithmetic) would trip; see §3 fragility caveat. If this test ever
// fails after a toolchain change, a full corpus A/B on both presets is
// mandatory before trusting any baseline.
TEST(Composing_FunctionLayerTests, TiePolicy_NearTie_HigherScoreWinsRegardlessOfTiePriority)
{
    // The higher-scoring cell deliberately carries the WORSE (higher) tiePriority.
    ScoringSnapshot snapshot = makeSnapshot(
        { makeCell(3, 0, /*tpl Major*/ 0, ChordQuality::Major, 3, 1.00),
          makeCell(3, 6, /*tpl HalfDim*/ 8, ChordQuality::HalfDiminished, 4, 1.02) },
        3, false);

    const auto results = runPipeline(snapshot, makeContext());
    ASSERT_GE(results.size(), 2u);
    EXPECT_EQ(results.front().identity.tiePriority, 8);
    EXPECT_NEAR(results.front().identity.score, 1.02, 1e-12);
    EXPECT_EQ(results[1].identity.tiePriority, 0);
}
