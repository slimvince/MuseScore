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

// postscoringgates_tests.cpp — Stage 1b (implementation_roadmap.md items 1.1 + 1.5)
//
// Pins the CURRENT behavior of the post-scoring gates (docs/scoring_model.md §6/§7)
// and the Iter 86 / Iter 91 promotions (applyIter8691Pedal tail). Like Stage 1a,
// these tests are the differential baseline for the Stage 3 decoder migration:
// each gate may be retired only when the decoder reproduces the behavior pinned
// here (roadmap 3.4).
//
// Fixture strategy (cc_stage1b_report.md §1): gates A–L operate purely on
// results[] + PostScoringGateContext + prefs + ChordTemporalContext, so most
// tests construct those inputs directly and call applyPostScoringGates() /
// applyIter8691Pedal() — the documented fallback. This is what makes the
// margin-boundary bracket pairs possible (a real-tones fixture cannot dial a
// 0.43-vs-0.47 margin). End-to-end shapes (Gate J bwv110.7, Gate R Δ=+7b,
// Iter 92 joint bass) go through analyzeWithGates() with real tones — the
// production call order.
//
// The pedal two-pass detector is NOT re-pinned here: it is already covered by
// the eight Composing_PedalPointTests in chordanalyzer_tests.cpp (fire,
// chord-tone-bass non-fire, zero-threshold disable, low-confidence non-fire).
//
// Preset note: per tools/batch_analyze.cpp, the Baroque preset differs from
// defaults only in preferMinorOverMajorAdd6 = true (Standard/Modal/Contemporary
// also set it; Jazz leaves it false). baroquePrefs() below mirrors that.

#include <gtest/gtest.h>

#include <algorithm>
#include <initializer_list>
#include <utility>
#include <vector>

#include "test_helpers.h"

#include "composing/analysis/chord/chordanalyzer.h"
#include "composing/analysis/param/paramoverride.h"

using namespace mu::composing::analysis;
namespace P = mu::composing::params;

namespace {

const RuleBasedChordAnalyzer kAnalyzer;

// kDefaultChordAnalyzerPreferences + the one Baroque-preset difference
// (tools/batch_analyze.cpp: Baroque sets only preferMinorOverMajorAdd6).
ChordAnalyzerPreferences baroquePrefs()
{
    ChordAnalyzerPreferences prefs;
    prefs.preferMinorOverMajorAdd6 = true;
    return prefs;
}

// Minimal post-pipeline result the gates operate on. Gates read identity
// (score, rootPc, bassPc, quality, extensions) only.
ChordAnalysisResult makeResult(int rootPc, int bassPc, ChordQuality quality, double score,
                               std::initializer_list<Extension> exts = {})
{
    ChordAnalysisResult r;
    r.identity.score   = score;
    r.identity.rootPc  = rootPc;
    r.identity.bassPc  = bassPc;
    r.identity.quality = quality;
    for (Extension e : exts) {
        setExtension(r.identity.extensions, e);
    }
    return r;
}

// Hand-built gate context. scale defaults to the Ionian interval set (the
// gates' diatonic checks compare scale intervals relative to keyTonicPc).
PostScoringGateContext makeGateCtx(std::initializer_list<std::pair<int, double>> pcWeights,
                                   int distinctPcs, int bassPc, int keyTonicPc = 0,
                                   double threshold = 0.0)
{
    PostScoringGateContext ctx;
    for (const auto& pw : pcWeights) {
        ctx.pcWeight[static_cast<size_t>(pw.first)] = pw.second;
    }
    ctx.tpcForPc.fill(-1);
    ctx.scale       = { 0, 2, 4, 5, 7, 9, 11 };
    ctx.keyTonicPc  = keyTonicPc;
    ctx.keyMode     = KeySigMode::Ionian;
    ctx.bassPc      = bassPc;
    ctx.bassTpc     = -1;
    ctx.distinctPcs = distinctPcs;
    ctx.threshold   = threshold;
    return ctx;
}

RawCandidate rawCand(double score, int rootPc, ChordQuality quality, int tiePriority = 0)
{
    return RawCandidate{ score, /*appliedBassBonus*/ 0.0, rootPc, quality, tiePriority,
                         /*wDimDelta*/ 0.0 };
}

// Tones with onsetAtRegionStart control (Iter 92 joint-scoring fixtures).
struct OnsetTone {
    int pitch;
    double weight;
    bool onsetAtStart;
};

std::vector<ChordAnalysisTone> onsetTones(std::initializer_list<OnsetTone> list)
{
    std::vector<ChordAnalysisTone> out;
    out.reserve(list.size());
    bool first = true;
    for (const OnsetTone& ot : list) {
        ChordAnalysisTone t;
        t.pitch              = ot.pitch;
        t.weight             = ot.weight;
        t.isBass             = first;
        t.onsetAtRegionStart = ot.onsetAtStart;
        out.push_back(t);
        first = false;
    }
    return out;
}

std::vector<ChordAnalysisTone> weightedTones(
    std::initializer_list<std::pair<int, double>> pitchWeightPairs)
{
    std::vector<ChordAnalysisTone> out;
    out.reserve(pitchWeightPairs.size());
    bool first = true;
    for (const auto& pw : pitchWeightPairs) {
        ChordAnalysisTone t;
        t.pitch  = pw.first;
        t.weight = pw.second;
        t.isBass = first;
        out.push_back(t);
        first = false;
    }
    return out;
}

} // namespace

// ═════════════════════════════════════════════════════════════════════════════
// Outer guard — ALL gates A–L run inside one block gated on
// inversionSuspicionMargin > 0, inversionBonusReduction < 1, results.size() >= 2
// and gateCtx.distinctPcs >= 3. (§6 lists distinctPcs >= 3 only under "Bias
// correction"; in code it gates the whole family — see report §Findings.)
// ═════════════════════════════════════════════════════════════════════════════

// pins current behavior — distinctPcs < 3 disables even the no-margin Gate A
// fast path and Gate J.
TEST(Composing_PostScoringGateTests, OuterGuard_DistinctPcsBelow3_DisablesAllGates)
{
    // Gate-A shape (would otherwise flip unconditionally under Baroque prefs).
    std::vector<ChordAnalysisResult> resultsA = {
        makeResult(10, 10, ChordQuality::Major, 2.5, { Extension::AddedSixth }),
        makeResult(7, 10, ChordQuality::Minor, 1.5, { Extension::MinorSeventh }),
    };
    auto ctxA = makeGateCtx({ { 10, 0.6 }, { 2, 0.5 }, { 5, 0.5 }, { 7, 0.4 } },
                            /*distinctPcs*/ 2, /*bassPc*/ 10, /*tonic*/ 5);
    applyPostScoringGates(resultsA, baroquePrefs(), nullptr, ctxA);
    EXPECT_EQ(resultsA.front().identity.rootPc, 10);

    // Gate-J shape (dim triad + sounding dominant root).
    std::vector<ChordAnalysisResult> resultsJ = {
        makeResult(10, 10, ChordQuality::Diminished, 2.5),
        makeResult(6, 10, ChordQuality::Major, 1.2, { Extension::MinorSeventh }),
    };
    auto ctxJ = makeGateCtx({ { 10, 0.5 }, { 1, 0.5 }, { 4, 0.5 }, { 6, 0.4 } }, 2, 10);
    applyPostScoringGates(resultsJ, kDefaultChordAnalyzerPreferences, nullptr, ctxJ);
    EXPECT_EQ(resultsJ.front().identity.rootPc, 10);
}

// pins current behavior — inversionSuspicionMargin = 0 (the "corrections off"
// preference) disables the ENTIRE gate family, including identity gates with
// no margin component (A, J). See report §Findings.
TEST(Composing_PostScoringGateTests, OuterGuard_SuspicionMarginZero_DisablesAllGates)
{
    ChordAnalyzerPreferences prefs = baroquePrefs();
    prefs.inversionSuspicionMargin = 0.0;
    std::vector<ChordAnalysisResult> results = {
        makeResult(10, 10, ChordQuality::Major, 2.5, { Extension::AddedSixth }),
        makeResult(7, 10, ChordQuality::Minor, 1.5, { Extension::MinorSeventh }),
    };
    auto ctx = makeGateCtx({ { 10, 0.6 }, { 2, 0.5 }, { 5, 0.5 }, { 7, 0.4 } }, 4, 10, 5);
    applyPostScoringGates(results, prefs, nullptr, ctx);
    EXPECT_EQ(results.front().identity.rootPc, 10);
}

// ═════════════════════════════════════════════════════════════════════════════
// Bias correction (§6 "Bias correction", §7) — deducts bassNoteRootBonus from a
// bass-root Maj/Min winner when the margin to the best clean alt is below
// inversionSuspicionMargin (0.70), then re-sorts.
// ═════════════════════════════════════════════════════════════════════════════

TEST(Composing_PostScoringGateTests, BiasCorrection_Fires_DeductsBassBonusAndResorts)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(0, 0, ChordQuality::Major, 2.0),
        makeResult(4, 4, ChordQuality::Minor, 1.5),
    };
    auto ctx = makeGateCtx({ { 0, 0.6 }, { 4, 0.5 }, { 7, 0.5 }, { 11, 0.3 } }, 4, 0);
    applyPostScoringGates(results, baroquePrefs(), nullptr, ctx);

    // margin 0.5 < 0.70 → deduct bassNoteRootBonus (0.70) from the C winner,
    // re-sort: Em (1.5) now leads C (1.3).
    ASSERT_GE(results.size(), 2u);
    EXPECT_EQ(results.front().identity.rootPc, 4);
    const ChordAnalysisResult* c = findCandidate(results, 0, ChordQuality::Major);
    ASSERT_NE(c, nullptr);
    EXPECT_NEAR(c->identity.score, 2.0 - 0.70, 1e-9);
}

// Margin bracket around inversionSuspicionMargin = 0.70 (strict <):
// 0.68 fires, 0.72 does not. (1a-style boundary pair; avoids exact FP equality.)
TEST(Composing_PostScoringGateTests, BiasCorrection_MarginBracket)
{
    auto run = [](double altScore) {
        std::vector<ChordAnalysisResult> results = {
            makeResult(0, 0, ChordQuality::Major, 2.0),
            makeResult(4, 4, ChordQuality::Minor, altScore),
        };
        auto ctx = makeGateCtx({ { 0, 0.6 }, { 4, 0.5 }, { 7, 0.5 }, { 11, 0.3 } }, 4, 0);
        applyPostScoringGates(results, baroquePrefs(), nullptr, ctx);
        return results;
    };

    // Just inside: margin 0.68 → deduction fires → Em promoted.
    const auto inside = run(1.32);
    EXPECT_EQ(inside.front().identity.rootPc, 4);

    // Just outside: margin 0.72 → no deduction → C stays, score untouched.
    const auto outside = run(1.28);
    EXPECT_EQ(outside.front().identity.rootPc, 0);
    EXPECT_NEAR(outside.front().identity.score, 2.0, 1e-9);
}

// Seventh-chord exemption (§6): a winner carrying a 7th the alt lacks is a
// richer reading — the bass-root bonus is not its sole advantage.
TEST(Composing_PostScoringGateTests, BiasCorrection_SeventhExemption)
{
    // Exempt: winner has min7, alt does not → no deduction despite margin 0.4.
    std::vector<ChordAnalysisResult> exempt = {
        makeResult(0, 0, ChordQuality::Major, 2.0, { Extension::MinorSeventh }),
        makeResult(4, 4, ChordQuality::Minor, 1.6),
    };
    auto ctx = makeGateCtx({ { 0, 0.6 }, { 4, 0.5 }, { 7, 0.5 }, { 10, 0.3 } }, 4, 0);
    applyPostScoringGates(exempt, baroquePrefs(), nullptr, ctx);
    EXPECT_EQ(exempt.front().identity.rootPc, 0);
    EXPECT_NEAR(exempt.front().identity.score, 2.0, 1e-9);

    // Not exempt: ALT carries the 7th (winnerHasSeventh false) → fires.
    std::vector<ChordAnalysisResult> notExempt = {
        makeResult(0, 0, ChordQuality::Major, 2.0),
        makeResult(4, 4, ChordQuality::Minor, 1.6, { Extension::MinorSeventh }),
    };
    applyPostScoringGates(notExempt, baroquePrefs(), nullptr, ctx);
    EXPECT_EQ(notExempt.front().identity.rootPc, 4);
}

// ═════════════════════════════════════════════════════════════════════════════
// FM2 — Minor-partner pull from rawCandidates (§6). Under preferMinorOverMajorAdd6,
// a Major+AddedSixth winner whose relative-Minor partner at (root+9)%12 was blocked
// out of results[] by a higher-scoring different-root alt is pulled from
// rawCandidates and promoted.
//
// NOTE (Stage 5, 2026-07-05, D-7): Gate A — the DIRECT Major-add6 → Minor swap that
// used to precede FM2 — was RETIRED (0 corpus firing sites on all three carriers,
// cc_stage5_phase2_2b_report.md §1.2). FM2 is the surviving enharmonic mechanism; the
// GateA_FM2_* fixtures below exercise it. (Gates B/C/D were removed earlier at Stage 3.4b.)
// ═════════════════════════════════════════════════════════════════════════════

// FM2 fallback (§6): the expected Minor partner is missing from results[]
// (blocked by a higher-scoring different-root alt) but lives in rawCandidates
// above the inclusion threshold → pulled in via buildChordResult and promoted.
TEST(Composing_PostScoringGateTests, GateA_FM2_PullsMinorAltFromRawCandidates)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(10, 10, ChordQuality::Major, 2.5, { Extension::AddedSixth }),
        makeResult(2, 2, ChordQuality::Minor, 1.4),   // clean alt at the WRONG root
    };
    auto ctx = makeGateCtx({ { 10, 0.6 }, { 2, 0.5 }, { 5, 0.5 }, { 7, 0.4 } }, 4, 10,
                           /*tonic F*/ 5, /*threshold*/ 1.0);
    ctx.rawCandidates = { rawCand(1.6, 7, ChordQuality::Minor, 5) };
    applyPostScoringGates(results, baroquePrefs(), nullptr, ctx);

    EXPECT_EQ(results.front().identity.rootPc, 7);
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Minor);
    // Built from gateCtx: bass Bb, and F (pc 5, interval 10 from G) above the
    // extension threshold → MinorSeventh detected.
    EXPECT_EQ(results.front().identity.bassPc, 10);
    EXPECT_TRUE(hasExtension(results.front().identity.extensions, Extension::MinorSeventh));
}

// FM2 raw scan stops at the score threshold (rc.score < gateCtx.threshold → break).
TEST(Composing_PostScoringGateTests, GateA_FM2_BelowThresholdCandidateNotPulled)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(10, 10, ChordQuality::Major, 2.5, { Extension::AddedSixth }),
        makeResult(2, 2, ChordQuality::Minor, 1.4),
    };
    auto ctx = makeGateCtx({ { 10, 0.6 }, { 2, 0.5 }, { 5, 0.5 }, { 7, 0.4 } }, 4, 10, 5,
                           /*threshold*/ 1.0);
    ctx.rawCandidates = { rawCand(0.9, 7, ChordQuality::Minor, 5) };   // below threshold
    applyPostScoringGates(results, baroquePrefs(), nullptr, ctx);
    EXPECT_EQ(results.front().identity.rootPc, 10);
}

// ═════════════════════════════════════════════════════════════════════════════
// Gate E — first-inversion detection (§6): Minor winner, Major alt at
// (root+8)%12 (winner root = M3 of alt root), alt root sounding, stepwise bass.
// ═════════════════════════════════════════════════════════════════════════════

TEST(Composing_PostScoringGateTests, GateE_MinorWinnerFlipsToMajorAtPlus8)
{
    // F#m vs D/F#: margin 1.0 proves the gate is margin-free; the stepwise
    // signal is what licenses the flip.
    std::vector<ChordAnalysisResult> results = {
        makeResult(6, 6, ChordQuality::Minor, 2.5),
        makeResult(2, 6, ChordQuality::Major, 1.5),
    };
    auto ctx = makeGateCtx({ { 6, 0.6 }, { 9, 0.5 }, { 2, 0.5 } }, 3, 6, /*tonic D*/ 2);
    ChordTemporalContext temporal;
    temporal.bassIsStepwiseFromPrevious = true;
    applyPostScoringGates(results, baroquePrefs(), &temporal, ctx);

    EXPECT_EQ(results.front().identity.rootPc, 2);
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Major);
}

TEST(Composing_PostScoringGateTests, GateE_NoStepwiseSignal_NoFlip)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(6, 6, ChordQuality::Minor, 2.5),
        makeResult(2, 6, ChordQuality::Major, 1.5),
    };
    auto ctx = makeGateCtx({ { 6, 0.6 }, { 9, 0.5 }, { 2, 0.5 } }, 3, 6, 2);
    ChordTemporalContext temporal;   // all signals at defaults (false)
    applyPostScoringGates(results, baroquePrefs(), &temporal, ctx);
    EXPECT_EQ(results.front().identity.rootPc, 6);
}

// Alt-root-present guard: pcWeight[altRoot] must exceed extensionThreshold.
TEST(Composing_PostScoringGateTests, GateE_AltRootBelowThreshold_NoFlip)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(6, 6, ChordQuality::Minor, 2.5),
        makeResult(2, 6, ChordQuality::Major, 1.5),
    };
    auto ctx = makeGateCtx({ { 6, 0.6 }, { 9, 0.5 }, { 2, 0.1 } }, 3, 6, 2);
    ChordTemporalContext temporal;
    temporal.bassIsStepwiseFromPrevious = true;
    applyPostScoringGates(results, baroquePrefs(), &temporal, ctx);
    EXPECT_EQ(results.front().identity.rootPc, 6);
}

// (Gate F — second-inversion → root-position Major at (root+5)%12 — was RETIRED in
//  Stage 5, 2026-07-05, D-7: 0 corpus firing sites on all three carriers. Its synthetic
//  fixtures + GateF_DisabledDoesNotFire were vacated. cc_stage5_phase2_2b_report.md §1.2.)

// ═════════════════════════════════════════════════════════════════════════════
// Gates G-E / G-B / G-C / G-D — Minor-add6 ↔ HalfDim7 (§6). Entry condition uses
// the captured originalWinner* values: Minor + AddedSixth at (altRoot - 9).
// G-E fires on key function alone (viiø7 / iiø7 / iiiø7); G-B/C/D are temporal
// fallbacks for non-functional alt roots.
// ═════════════════════════════════════════════════════════════════════════════

TEST(Composing_PostScoringGateTests, GateGE_KeyFunctionFlip_NoTemporalNeeded)
{
    // Dm6 vs Bø7/D in C major: alt root 11 = leading tone → viiø7 reading wins
    // with no temporal context at all.
    std::vector<ChordAnalysisResult> results = {
        makeResult(2, 2, ChordQuality::Minor, 2.5, { Extension::AddedSixth }),
        makeResult(11, 2, ChordQuality::HalfDiminished, 1.5, { Extension::MinorSeventh }),
    };
    auto ctx = makeGateCtx({ { 2, 0.6 }, { 5, 0.5 }, { 9, 0.5 }, { 11, 0.4 } }, 4, 2);
    applyPostScoringGates(results, baroquePrefs(), nullptr, ctx);

    EXPECT_EQ(results.front().identity.rootPc, 11);
    EXPECT_EQ(results.front().identity.quality, ChordQuality::HalfDiminished);
}

// G-E rawCandidates pull-in: the HalfDim alt is absent from results[] and is
// promoted straight from rawCandidates (no threshold check on this path).
TEST(Composing_PostScoringGateTests, GateGE_PullsHalfDimFromRawCandidates)
{
    // Cm6 in G major: expected alt root 9 (A) = supertonic → iiø7 functional.
    std::vector<ChordAnalysisResult> results = {
        makeResult(0, 0, ChordQuality::Minor, 2.5, { Extension::AddedSixth }),
        makeResult(3, 3, ChordQuality::Major, 1.2),   // filler; wrong root, clean
    };
    auto ctx = makeGateCtx({ { 0, 0.5 }, { 3, 0.5 }, { 7, 0.5 }, { 9, 0.4 } }, 4, 0,
                           /*tonic G*/ 7);
    ctx.rawCandidates = { rawCand(1.6, 9, ChordQuality::HalfDiminished, 8) };
    applyPostScoringGates(results, baroquePrefs(), nullptr, ctx);

    EXPECT_EQ(results.front().identity.rootPc, 9);
    EXPECT_EQ(results.front().identity.quality, ChordQuality::HalfDiminished);
}

// The pulled-from-raw candidate is popped again when no G sub-gate fires
// (phantom-alternative cleanup).
TEST(Composing_PostScoringGateTests, GateG_PulledCandidatePoppedWhenNoSubGateFires)
{
    // Same Cm6 shape but in C major: alt root 9 is NOT viiø7/iiø7/iiiø7
    // ({11, 2, 4}) and there is no temporal context → nothing fires.
    std::vector<ChordAnalysisResult> results = {
        makeResult(0, 0, ChordQuality::Minor, 2.5, { Extension::AddedSixth }),
        makeResult(3, 3, ChordQuality::Major, 1.2),
    };
    auto ctx = makeGateCtx({ { 0, 0.5 }, { 3, 0.5 }, { 7, 0.5 }, { 9, 0.4 } }, 4, 0,
                           /*tonic C*/ 0);
    ctx.rawCandidates = { rawCand(1.6, 9, ChordQuality::HalfDiminished, 8) };
    applyPostScoringGates(results, baroquePrefs(), nullptr, ctx);

    EXPECT_EQ(results.front().identity.rootPc, 0);
    EXPECT_EQ(results.size(), 2u);   // phantom removed
}

// G-D: >= 2 consecutive stepwise bass moves; 1 is not enough (boundary pair).
TEST(Composing_PostScoringGateTests, GateGD_ConsecutiveStepwiseBoundary)
{
    auto run = [](int consecutiveCount) {
        std::vector<ChordAnalysisResult> results = {
            makeResult(0, 0, ChordQuality::Minor, 2.5, { Extension::AddedSixth }),
            makeResult(9, 0, ChordQuality::HalfDiminished, 1.5, { Extension::MinorSeventh }),
        };
        auto ctx = makeGateCtx({ { 9, 0.4 }, { 0, 0.6 }, { 3, 0.5 }, { 7, 0.5 } }, 4, 0);
        ChordTemporalContext temporal;
        temporal.consecutiveBassStepwiseCount = consecutiveCount;
        applyPostScoringGates(results, baroquePrefs(), &temporal, ctx);
        return results.front().identity.rootPc;
    };

    EXPECT_EQ(run(2), 9);   // fires
    EXPECT_EQ(run(1), 0);   // does not fire
}

TEST(Composing_PostScoringGateTests, GateG_NoContextNonFunctionalRoot_NoFlip)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(0, 0, ChordQuality::Minor, 2.5, { Extension::AddedSixth }),
        makeResult(9, 0, ChordQuality::HalfDiminished, 1.5, { Extension::MinorSeventh }),
    };
    auto ctx = makeGateCtx({ { 9, 0.4 }, { 0, 0.6 }, { 3, 0.5 }, { 7, 0.5 } }, 4, 0);
    applyPostScoringGates(results, baroquePrefs(), nullptr, ctx);
    EXPECT_EQ(results.front().identity.rootPc, 0);
}

// ═════════════════════════════════════════════════════════════════════════════
// Gate H — augmented rotation resolution (§6): Augmented bass-root winner,
// Augmented alt at (root+4) or (root+8); temporal sub-gates mirror G-B/C/D.
// Requires preferMinorOverMajorAdd6 AND a temporal context.
// ═════════════════════════════════════════════════════════════════════════════

TEST(Composing_PostScoringGateTests, GateH_ForwardEvidence_RotatesPlus4)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(0, 0, ChordQuality::Augmented, 2.0),
        makeResult(4, 4, ChordQuality::Augmented, 1.8),
    };
    auto ctx = makeGateCtx({ { 0, 0.5 }, { 4, 0.5 }, { 8, 0.5 } }, 3, 0);
    ChordTemporalContext temporal;
    temporal.nextRootPc           = 4;
    temporal.bassIsStepwiseToNext = true;
    applyPostScoringGates(results, baroquePrefs(), &temporal, ctx);

    EXPECT_EQ(results.front().identity.rootPc, 4);
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Augmented);
}

TEST(Composing_PostScoringGateTests, GateH_ForwardEvidence_RotatesPlus8)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(0, 0, ChordQuality::Augmented, 2.0),
        makeResult(8, 8, ChordQuality::Augmented, 1.8),
    };
    auto ctx = makeGateCtx({ { 0, 0.5 }, { 4, 0.5 }, { 8, 0.5 } }, 3, 0);
    ChordTemporalContext temporal;
    temporal.nextRootPc           = 8;
    temporal.bassIsStepwiseToNext = true;
    applyPostScoringGates(results, baroquePrefs(), &temporal, ctx);

    EXPECT_EQ(results.front().identity.rootPc, 8);
}

TEST(Composing_PostScoringGateTests, GateH_NoContext_NoRotation)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(0, 0, ChordQuality::Augmented, 2.0),
        makeResult(4, 4, ChordQuality::Augmented, 1.8),
    };
    auto ctx = makeGateCtx({ { 0, 0.5 }, { 4, 0.5 }, { 8, 0.5 } }, 3, 0);
    applyPostScoringGates(results, baroquePrefs(), nullptr, ctx);
    EXPECT_EQ(results.front().identity.rootPc, 0);
}

TEST(Composing_PostScoringGateTests, GateH_PresetOff_NoRotation)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(0, 0, ChordQuality::Augmented, 2.0),
        makeResult(4, 4, ChordQuality::Augmented, 1.8),
    };
    auto ctx = makeGateCtx({ { 0, 0.5 }, { 4, 0.5 }, { 8, 0.5 } }, 3, 0);
    ChordTemporalContext temporal;
    temporal.nextRootPc           = 4;
    temporal.bassIsStepwiseToNext = true;
    applyPostScoringGates(results, kDefaultChordAnalyzerPreferences, &temporal, ctx);
    EXPECT_EQ(results.front().identity.rootPc, 0);
}

// ═════════════════════════════════════════════════════════════════════════════
// Gate I — diatonic first-inversion Major over root-position Minor (§6):
// same bass, alt root a M3 below the bass (I4), alt root diatonic and sounding,
// margin <= 0.45. The Minor winners carry a MinorSeventh in these fixtures so
// the bias correction's seventh-exemption keeps results[] untouched and Gate I
// is the only mechanism that can swap.
// ═════════════════════════════════════════════════════════════════════════════

TEST(Composing_PostScoringGateTests, GateI_MarginBracket)
{
    auto run = [](double altScore) {
        std::vector<ChordAnalysisResult> results = {
            makeResult(4, 4, ChordQuality::Minor, 2.0, { Extension::MinorSeventh }),
            makeResult(0, 4, ChordQuality::Major, altScore),   // C/E
        };
        auto ctx = makeGateCtx({ { 0, 0.5 }, { 4, 0.6 }, { 7, 0.5 }, { 2, 0.3 } }, 4, 4);
        applyPostScoringGates(results, baroquePrefs(), nullptr, ctx);
        return results.front().identity.rootPc;
    };

    EXPECT_EQ(run(1.57), 0);   // margin 0.43 <= 0.45 → C/E promoted
    EXPECT_EQ(run(1.53), 4);   // margin 0.47 > 0.45 → Em7 stays
}

// Diatonic guard: a non-diatonic promoted root never wins (Db in C major).
TEST(Composing_PostScoringGateTests, GateI_NonDiatonicAltRoot_NoFlip)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(5, 5, ChordQuality::Minor, 2.0, { Extension::MinorSeventh }),
        makeResult(1, 5, ChordQuality::Major, 1.6),   // Db/F — 1 not in C major
    };
    auto ctx = makeGateCtx({ { 1, 0.5 }, { 5, 0.6 }, { 8, 0.5 }, { 3, 0.3 } }, 4, 5);
    applyPostScoringGates(results, baroquePrefs(), nullptr, ctx);
    EXPECT_EQ(results.front().identity.rootPc, 5);
}

// Promoted-root-present guard: "do not invent a rootless inversion".
TEST(Composing_PostScoringGateTests, GateI_AltRootBelowThreshold_NoFlip)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(4, 4, ChordQuality::Minor, 2.0, { Extension::MinorSeventh }),
        makeResult(0, 4, ChordQuality::Major, 1.57),
    };
    auto ctx = makeGateCtx({ { 0, 0.1 }, { 4, 0.6 }, { 7, 0.5 }, { 2, 0.3 } }, 4, 4);
    applyPostScoringGates(results, baroquePrefs(), nullptr, ctx);
    EXPECT_EQ(results.front().identity.rootPc, 4);
}

// (Gate K — first-inversion Augmented over root-position Augmented (I4, margin ≤ 0.20) —
//  was RETIRED in Stage 5, 2026-07-05, D-7: 0 corpus firing sites on all three carriers;
//  founding case bwv40.6 no longer touched (superseded upstream). Its synthetic fixtures +
//  GateK_DisabledDoesNotFire were vacated; kGateKMargin retired with it.
//  cc_stage5_phase2_2b_report.md §1.2/§1.3.)

// ═════════════════════════════════════════════════════════════════════════════
// Gate L — same-root Major over root-position Augmented (§6, TYPE-A quality
// fix): same root AND same bass, Major alt, diatonic, margin <= 0.35, and the
// Augmented winner must not carry a seventh. Not preset-gated.
// ═════════════════════════════════════════════════════════════════════════════

TEST(Composing_PostScoringGateTests, GateL_MarginBracket)
{
    // bwv144.6 shape: B+ → B (root 11 diatonic in C major).
    auto run = [](double altScore) {
        std::vector<ChordAnalysisResult> results = {
            makeResult(11, 11, ChordQuality::Augmented, 2.0),
            makeResult(11, 11, ChordQuality::Major, altScore),
        };
        auto ctx = makeGateCtx({ { 11, 0.6 }, { 3, 0.5 }, { 7, 0.5 } }, 3, 11);
        applyPostScoringGates(results, kDefaultChordAnalyzerPreferences, nullptr, ctx);
        return results.front().identity.quality;
    };

    EXPECT_EQ(run(1.67), ChordQuality::Major);       // margin 0.33 <= 0.35
    EXPECT_EQ(run(1.63), ChordQuality::Augmented);   // margin 0.37 > 0.35
}

// Seventh exclusion: an augmented+7 winner (jazz dominant) is intentionally
// augmented and must not be demoted to plain Major.
TEST(Composing_PostScoringGateTests, GateL_AugmentedSeventhWinner_NoDemotion)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(11, 11, ChordQuality::Augmented, 2.0, { Extension::MinorSeventh }),
        makeResult(11, 11, ChordQuality::Major, 1.8),
    };
    auto ctx = makeGateCtx({ { 11, 0.6 }, { 3, 0.5 }, { 7, 0.5 }, { 9, 0.3 } }, 4, 11);
    applyPostScoringGates(results, kDefaultChordAnalyzerPreferences, nullptr, ctx);
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Augmented);
}

// ═════════════════════════════════════════════════════════════════════════════
// Gate J — vii° → V7 completion (§6, bwv110.7 m10 fix): root-position
// Diminished TRIAD winner (no dim7) whose would-be dominant root (M3 below) is
// sounding above extensionThreshold; the Major+m7 alt rooted there wins.
// No margin guard, no diatonic guard (secondary dominants are valid), runs
// LAST in the gate chain.
// ═════════════════════════════════════════════════════════════════════════════

TEST(Composing_PostScoringGateTests, GateJ_DimTriadWithSoundingDominantRoot_SwapsToV65)
{
    // {C#, E, F#, A#}, bass A#: A#° → F#7/A# (V6/5 of B). Margin 1.3 — proves
    // the gate has no margin component.
    std::vector<ChordAnalysisResult> results = {
        makeResult(10, 10, ChordQuality::Diminished, 2.5),
        makeResult(6, 10, ChordQuality::Major, 1.2, { Extension::MinorSeventh }),
    };
    auto ctx = makeGateCtx({ { 10, 0.5 }, { 1, 0.5 }, { 4, 0.5 }, { 6, 0.4 } }, 4, 10);
    applyPostScoringGates(results, kDefaultChordAnalyzerPreferences, nullptr, ctx);

    EXPECT_EQ(results.front().identity.rootPc, 6);
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Major);
    EXPECT_TRUE(hasExtension(results.front().identity.extensions, Extension::MinorSeventh));
}

// Genuine vii°7 protection: a winner carrying the DiminishedSeventh extension
// is a real leading-tone seventh chord and is never rewritten.
TEST(Composing_PostScoringGateTests, GateJ_DimSeventhWinner_NoSwap)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(10, 10, ChordQuality::Diminished, 2.5, { Extension::DiminishedSeventh }),
        makeResult(6, 10, ChordQuality::Major, 1.2, { Extension::MinorSeventh }),
    };
    auto ctx = makeGateCtx({ { 10, 0.5 }, { 1, 0.5 }, { 4, 0.5 }, { 6, 0.4 } }, 4, 10);
    applyPostScoringGates(results, kDefaultChordAnalyzerPreferences, nullptr, ctx);
    EXPECT_EQ(results.front().identity.rootPc, 10);
}

// Present-root guard: the dominant root must actually sound above the
// extension threshold — a standalone vii° never voices it.
TEST(Composing_PostScoringGateTests, GateJ_DominantRootBelowThreshold_NoSwap)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(10, 10, ChordQuality::Diminished, 2.5),
        makeResult(6, 10, ChordQuality::Major, 1.2, { Extension::MinorSeventh }),
    };
    auto ctx = makeGateCtx({ { 10, 0.5 }, { 1, 0.5 }, { 4, 0.5 }, { 6, 0.15 } }, 4, 10);
    applyPostScoringGates(results, kDefaultChordAnalyzerPreferences, nullptr, ctx);
    EXPECT_EQ(results.front().identity.rootPc, 10);
}

// The alt must carry the dominant seventh (Major+m7) — a plain Major triad at
// the dominant root is not a V7 completion.
TEST(Composing_PostScoringGateTests, GateJ_AltWithoutMinorSeventh_NoSwap)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(10, 10, ChordQuality::Diminished, 2.5),
        makeResult(6, 10, ChordQuality::Major, 1.2),
    };
    auto ctx = makeGateCtx({ { 10, 0.5 }, { 1, 0.5 }, { 4, 0.5 }, { 6, 0.4 } }, 4, 10);
    applyPostScoringGates(results, kDefaultChordAnalyzerPreferences, nullptr, ctx);
    EXPECT_EQ(results.front().identity.rootPc, 10);
}

// ═════════════════════════════════════════════════════════════════════════════
// Ordering / Sub-9a (§7 "Pre-sort capture", roadmap 1.5): the bias-correction
// sort changes results[0], and Gate G-E must compute gExpectedAltRoot from the
// CAPTURED original winner root, not the promoted one. With the historical bug
// (pre-f3e0f5f72c) this fixture would flip to the F#ø7 decoy: the promoted
// Aø7's live rootPc (9) gives gExpectedAltRoot = 6, and 6 IS the leading tone
// of G major, so the buggy G-E would promote the decoy.
// ═════════════════════════════════════════════════════════════════════════════

TEST(Composing_PostScoringGateTests, Ordering_Sub9a_GateGEUsesPreSortWinnerRoot)
{
    // Cm6 vs Aø7/C in G major (Aø7 = iiø7). All four Aø7 tones sound.
    std::vector<ChordAnalysisResult> results = {
        makeResult(0, 0, ChordQuality::Minor, 2.0, { Extension::AddedSixth }),
        makeResult(9, 0, ChordQuality::HalfDiminished, 1.8, { Extension::MinorSeventh }),
    };
    auto ctx = makeGateCtx({ { 9, 0.4 }, { 0, 0.6 }, { 3, 0.5 }, { 7, 0.5 } }, 4, 0,
                           /*tonic G*/ 7);
    // Decoy FIRST: a buggy expected-root of 6 would match it before the Aø7.
    ctx.rawCandidates = { rawCand(1.6, 6, ChordQuality::HalfDiminished, 8),
                          rawCand(1.7, 9, ChordQuality::HalfDiminished, 8) };
    applyPostScoringGates(results, baroquePrefs(), nullptr, ctx);

    // Sequence pinned: (1) bias correction fires (margin 0.2 < 0.70): winner
    // deducted 2.0 → 1.3, HalfDim first-inversion bonus +0.55 → 2.35, re-sort
    // promotes Aø7 to results[0]; (2) Gate G-E computes expected alt root from
    // the CAPTURED root 0 → 9 (iiø7 of G), does not find a HalfDim at 9 when
    // scanning results[1..] (the bias-promoted Aø7 sits at [0]), pulls the Aø7
    // raw candidate, and swaps it into the winner slot.
    ASSERT_EQ(results.size(), 3u);   // pulled duplicate appended
    EXPECT_EQ(results.front().identity.rootPc, 9);
    EXPECT_EQ(results.front().identity.quality, ChordQuality::HalfDiminished);

    // The deduction and the +0.55 kHalfDimFirstInversionBonus are visible on
    // the displaced entries.
    EXPECT_NEAR(results[1].identity.score, 2.0 - 0.70, 1e-9);    // demoted Cm6
    EXPECT_EQ(results[1].identity.rootPc, 0);
    EXPECT_NEAR(results[2].identity.score, 1.8 + 0.55, 1e-9);    // bias-promoted Aø7
}

// ═════════════════════════════════════════════════════════════════════════════
// Iter 86 — bass-b7 promotion (applyIter8691Pedal): Major/Minor plain-triad
// winner whose bass sits at interval 10 from the root, bass pc sounding above
// extensionThreshold → MinorSeventh stamped (Am/G → Am7/G).
// ═════════════════════════════════════════════════════════════════════════════

TEST(Composing_PostScoringGateTests, Iter86_BassAtFlatSeven_StampsMinorSeventh)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(9, 7, ChordQuality::Minor, 2.0),
    };
    auto ctx = makeGateCtx({ { 9, 0.5 }, { 0, 0.5 }, { 4, 0.5 }, { 7, 0.4 } }, 4, 7);
    applyIter8691Pedal(results, ctx, nullptr, kDefaultChordAnalyzerPreferences);

    EXPECT_TRUE(hasExtension(results.front().identity.extensions, Extension::MinorSeventh));
    EXPECT_EQ(results.front().identity.rootPc, 9);   // identity otherwise untouched
}

TEST(Composing_PostScoringGateTests, Iter86_BassPcBelowThreshold_NoStamp)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(9, 7, ChordQuality::Minor, 2.0),
    };
    auto ctx = makeGateCtx({ { 9, 0.5 }, { 0, 0.5 }, { 4, 0.5 }, { 7, 0.15 } }, 4, 7);
    applyIter8691Pedal(results, ctx, nullptr, kDefaultChordAnalyzerPreferences);
    EXPECT_FALSE(hasExtension(results.front().identity.extensions, Extension::MinorSeventh));
}

// Plain-triad guard: a winner already carrying a seventh is left alone.
TEST(Composing_PostScoringGateTests, Iter86_WinnerWithSeventh_NoStamp)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(9, 7, ChordQuality::Minor, 2.0, { Extension::MajorSeventh }),
    };
    auto ctx = makeGateCtx({ { 9, 0.5 }, { 0, 0.5 }, { 4, 0.5 }, { 7, 0.4 } }, 4, 7);
    applyIter8691Pedal(results, ctx, nullptr, kDefaultChordAnalyzerPreferences);
    EXPECT_FALSE(hasExtension(results.front().identity.extensions, Extension::MinorSeventh));
}

// ═════════════════════════════════════════════════════════════════════════════
// Iter 91 — bass-as-root promotion (applyIter8691Pedal): plain-triad slash
// winner with the bass a third above the root, promoted to the bass-rooted
// rawCandidate IFF the next region's root equals the bass (forward gate).
//   Pattern A: delta 8, Minor winner (Em/C → C)
//   Pattern B: delta 9, Major winner (C/A → Am)
// ═════════════════════════════════════════════════════════════════════════════

TEST(Composing_PostScoringGateTests, Iter91_PatternA_MinorDelta8_PromotesBassRoot)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(4, 0, ChordQuality::Minor, 2.0),   // Em/C
    };
    auto ctx = makeGateCtx({ { 0, 0.6 }, { 4, 0.5 }, { 7, 0.5 } }, 3, 0);
    ctx.rawCandidates = { rawCand(2.2, 0, ChordQuality::Major, 0) };
    ChordTemporalContext temporal;
    temporal.nextRootPc = 0;   // next region confirms C as the root
    applyIter8691Pedal(results, ctx, &temporal, kDefaultChordAnalyzerPreferences);

    EXPECT_EQ(results.front().identity.rootPc, 0);
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Major);
    EXPECT_EQ(results.front().identity.bassPc, 0);
}

TEST(Composing_PostScoringGateTests, Iter91_PatternB_MajorDelta9_PromotesBassRoot)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(0, 9, ChordQuality::Major, 2.0),   // C/A
    };
    auto ctx = makeGateCtx({ { 9, 0.5 }, { 0, 0.6 }, { 4, 0.5 } }, 3, 9);
    ctx.rawCandidates = { rawCand(2.2, 9, ChordQuality::Minor, 4) };
    ChordTemporalContext temporal;
    temporal.nextRootPc = 9;
    applyIter8691Pedal(results, ctx, &temporal, kDefaultChordAnalyzerPreferences);

    EXPECT_EQ(results.front().identity.rootPc, 9);
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Minor);
}

// Forward gate: without context, or when nextRootPc differs from the bass,
// the slash reading stands (previousRootPc was deliberately omitted — §6 /
// docs/iter90_bass_as_root_promotion_shelved.md).
TEST(Composing_PostScoringGateTests, Iter91_NoForwardConfirmation_NoPromotion)
{
    auto ctx = makeGateCtx({ { 0, 0.6 }, { 4, 0.5 }, { 7, 0.5 } }, 3, 0);
    ctx.rawCandidates = { rawCand(2.2, 0, ChordQuality::Major, 0) };

    // No temporal context at all.
    std::vector<ChordAnalysisResult> noCtx = {
        makeResult(4, 0, ChordQuality::Minor, 2.0),
    };
    applyIter8691Pedal(noCtx, ctx, nullptr, kDefaultChordAnalyzerPreferences);
    EXPECT_EQ(noCtx.front().identity.rootPc, 4);

    // Forward root known but different from the bass.
    std::vector<ChordAnalysisResult> wrongNext = {
        makeResult(4, 0, ChordQuality::Minor, 2.0),
    };
    ChordTemporalContext temporal;
    temporal.nextRootPc = 5;
    applyIter8691Pedal(wrongNext, ctx, &temporal, kDefaultChordAnalyzerPreferences);
    EXPECT_EQ(wrongNext.front().identity.rootPc, 4);
}

// ═════════════════════════════════════════════════════════════════════════════
// End-to-end shapes through analyzeWithGates() — the production call order
// (analyzeChord → applyIter8691Pedal → applyPostScoringGates). Roadmap 1.5.
// ═════════════════════════════════════════════════════════════════════════════

// Gate J / bwv110.7 m10 shape: {A#2, C#4, E4, F#4} in B minor. The four pcs
// {6, 10, 1, 4} are exactly F#7; with the dominant root F# sounding, the
// root-position A#° reading is by construction V6/5 of B. Pinned winner:
// F#7/A# (root 6, Major+m7, bass 10). If Gate J were removed, the bass-root
// diminished reading could win again — the gate's swap is the documented fix.
TEST(Composing_PostScoringGateTests, E2E_GateJ_Bwv110Shape_FSharp7OverASharp)
{
    const auto results = analyzeWithGates(kAnalyzer, tones({ 46, 61, 64, 66 }),
                                          /*fifths*/ 2, KeySigMode::Aeolian,
                                          nullptr, baroquePrefs());
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 6);
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Major);
    EXPECT_TRUE(hasExtension(results.front().identity.extensions, Extension::MinorSeventh));
    EXPECT_EQ(results.front().identity.bassPc, 10);
}

// Gate R Δ=+7b end-to-end (bwv320 mapping G/E → C): a predecessor root G
// continues into a region spanning {E, G, C} with bass E. The continued-root
// candidate G/E has its bass a M6 above the root (interval 9 — in no template)
// and earns no bass-dependent credit, so Gate R withholds the +0.40
// rootContinuityBonus and the first-inversion C/E reading wins on its raw
// vertical lead. gater_tests.cpp pins the predicate; this pins the production
// outcome through the full pipeline.
TEST(Composing_PostScoringGateTests, E2E_GateR_DeltaPlus7b_FirstInversionBeatsContinuedRoot)
{
    // G weighted heavily (held across the region) so the continued-root
    // candidate is genuinely competitive, mirroring the corpus mechanism.
    const auto ts = weightedTones({ { 40, 1.0 }, { 55, 2.2 }, { 60, 0.8 }, { 64, 0.5 } });
    ChordTemporalContext temporal;
    temporal.previousRootPc  = 7;
    temporal.previousQuality = ChordQuality::Major;
    temporal.recentRootPcs   = { 7, -1, -1 };
    const auto results = analyzeWithGates(kAnalyzer, ts, 0, KeySigMode::Ionian,
                                          &temporal, baroquePrefs());
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 0);
    EXPECT_EQ(results.front().identity.bassPc, 4);
}

// Iter 92 Bug 1 (bwv103.6 m3 b2 shape): a passing eighth note that is the
// absolute lowest pitch must not win bass selection over the beat-onset bass a
// step above it. Joint bass enumeration fires on the onset-true/onset-false
// mix; the legacy single-bass path (no onset data) picks the literal lowest
// pitch — both behaviors pinned as a contrast pair.
TEST(Composing_PostScoringGateTests, E2E_Iter92_OnsetBassBeatsPassingLowNote)
{
    // G2 (bass, onset at region start) vs F#2 (passing, lower, mid-region);
    // upper voices B3 + D4 → G major.
    const auto joint = analyzeWithGates(
        kAnalyzer,
        onsetTones({ { 43, 1.0, true }, { 42, 0.3, false },
                     { 59, 1.0, true }, { 62, 1.0, true } }),
        /*fifths*/ 1, KeySigMode::Ionian, nullptr, baroquePrefs());
    ASSERT_FALSE(joint.empty());
    EXPECT_EQ(joint.front().identity.rootPc, 7);
    EXPECT_EQ(joint.front().identity.bassPc, 7);

    // Same pitches without onset data: legacy single-bass path commits to the
    // literal lowest qualifying pitch (F#2, pc 6).
    const auto legacy = analyzeWithGates(
        kAnalyzer,
        weightedTones({ { 42, 0.3 }, { 43, 1.0 }, { 59, 1.0 }, { 62, 1.0 } }),
        1, KeySigMode::Ionian, nullptr, baroquePrefs());
    ASSERT_FALSE(legacy.empty());
    EXPECT_EQ(legacy.front().identity.bassPc, 6);
}

// Iter 92 Bug 2 (bwv310 m8 b3 shape): with regional accumulation active,
// w_complete (+0.50, §4) rewards the root-position complete triad so it
// outranks slash readings of the same pc set — C major, not Em/C.
TEST(Composing_PostScoringGateTests, E2E_Iter92_WComplete_RootPositionTriadWins)
{
    const auto results = analyzeWithGates(
        kAnalyzer,
        onsetTones({ { 48, 1.0, true }, { 64, 1.0, true }, { 67, 1.0, true } }),
        0, KeySigMode::Ionian, nullptr, baroquePrefs());
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 0);
    EXPECT_EQ(results.front().identity.bassPc, 0);
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Major);
}

// ═════════════════════════════════════════════════════════════════════════════
// Phase-5 branch backfill (round 2, cluster 2) — additional gate branch directions.
// Each test asserts the documented gate rule (docs/scoring_model.md §6/§7), targeting
// fire/no-fire arms the Stage-1b suite left unhit (cc_union_branch_coverage_report.md).
// ═════════════════════════════════════════════════════════════════════════════

// Outer guard: inversionBonusReduction = 1.0 (no reduction) disables the whole gate
// family — even Gate A's unconditional fast path.
TEST(Composing_PostScoringGateTests, OuterGuard_BonusReductionOne_DisablesAllGates)
{
    ChordAnalyzerPreferences prefs = baroquePrefs();
    prefs.inversionBonusReduction = 1.0;
    std::vector<ChordAnalysisResult> results = {
        makeResult(10, 10, ChordQuality::Major, 2.5, { Extension::AddedSixth }),
        makeResult(7, 10, ChordQuality::Minor, 1.5, { Extension::MinorSeventh }),
    };
    auto ctx = makeGateCtx({ { 10, 0.6 }, { 2, 0.5 }, { 5, 0.5 }, { 7, 0.4 } }, 4, 10, 5);
    applyPostScoringGates(results, prefs, nullptr, ctx);
    EXPECT_EQ(results.front().identity.rootPc, 10);   // no flip
}

// ── Bias correction HalfDim first-inversion exception (bwv187.7 shape) ───────────
// A Minor winner whose bass is the b5 of a fully-present half-diminished seventh, at a
// close margin, is corrected to that first-inversion HalfDim reading.
TEST(Composing_PostScoringGateTests, BiasHalfDimInversion_BassIsFlatFifth_Accepted)
{
    // Cm (root 0, bass 0). F#ø7 = {6,9,0,4}; bass C (0) is its b5 ((6+6)%12 = 0).
    std::vector<ChordAnalysisResult> results = {
        makeResult(0, 0, ChordQuality::Minor, 2.0),
        makeResult(6, 0, ChordQuality::HalfDiminished, 1.8, { Extension::MinorSeventh }),
    };
    auto ctx = makeGateCtx({ { 6, 0.5 }, { 9, 0.5 }, { 0, 0.6 }, { 4, 0.5 } }, 4, 0);
    applyPostScoringGates(results, baroquePrefs(), nullptr, ctx);
    EXPECT_EQ(results.front().identity.rootPc, 6);
    EXPECT_EQ(results.front().identity.quality, ChordQuality::HalfDiminished);
}

// The HalfDim exception requires ALL FOUR chord tones present: a missing b5 disqualifies
// the inversion reading, so the Minor winner stands.
TEST(Composing_PostScoringGateTests, BiasHalfDimInversion_MissingFifth_NotAccepted)
{
    // Aø7 = {9,0,3,7}; its b5 is pc 3 (deliberately absent from pcWeight).
    std::vector<ChordAnalysisResult> results = {
        makeResult(0, 0, ChordQuality::Minor, 2.0),
        makeResult(9, 0, ChordQuality::HalfDiminished, 1.8, { Extension::MinorSeventh }),
    };
    auto ctx = makeGateCtx({ { 9, 0.5 }, { 0, 0.6 }, { 7, 0.5 } }, 4, 0);  // pc 3 absent
    applyPostScoringGates(results, baroquePrefs(), nullptr, ctx);
    EXPECT_EQ(results.front().identity.rootPc, 0);   // Cm stands
}

// Likewise a missing m7 disqualifies the HalfDim inversion reading.
TEST(Composing_PostScoringGateTests, BiasHalfDimInversion_MissingSeventh_NotAccepted)
{
    // Aø7 = {9,0,3,7}; its m7 is pc 7 (deliberately absent).
    std::vector<ChordAnalysisResult> results = {
        makeResult(0, 0, ChordQuality::Minor, 2.0),
        makeResult(9, 0, ChordQuality::HalfDiminished, 1.8, { Extension::MinorSeventh }),
    };
    auto ctx = makeGateCtx({ { 9, 0.5 }, { 0, 0.6 }, { 3, 0.5 } }, 4, 0);  // pc 7 absent
    applyPostScoringGates(results, baroquePrefs(), nullptr, ctx);
    EXPECT_EQ(results.front().identity.rootPc, 0);
}

// Gate A FM2 raw scan that runs to completion without a match (above-threshold raw
// candidates exist, but none is the expected minor at (root+9)).
TEST(Composing_PostScoringGateTests, GateA_FM2_NoMatchingRawCandidate_NoFlip)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(10, 10, ChordQuality::Major, 2.5, { Extension::AddedSixth }),
        makeResult(2, 2, ChordQuality::Major, 1.5),   // bestAlt is Major (no direct flip)
    };
    auto ctx = makeGateCtx({ { 10, 0.6 }, { 2, 0.5 }, { 5, 0.5 } }, 4, 10, 5,
                           /*threshold*/ 1.0);
    // Above threshold but neither matches root 7 Minor: wrong root, and right-ish quality
    // wrong root again.
    ctx.rawCandidates = { rawCand(1.6, 3, ChordQuality::Minor, 4),
                          rawCand(1.5, 7, ChordQuality::Major, 0) };
    applyPostScoringGates(results, baroquePrefs(), nullptr, ctx);
    EXPECT_EQ(results.front().identity.rootPc, 10);
}

// Gate E reached (winner Minor, alt Major) but the alt root is NOT a minor-6th above the
// winner root (not the +8 first-inversion relationship) → no flip.
TEST(Composing_PostScoringGateTests, GateE_AltMajorNotAtPlus8_NoFlip)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(4, 4, ChordQuality::Minor, 2.5),
        makeResult(3, 3, ChordQuality::Major, 1.5),   // root 3 != (4+8)%12 = 0, and != +5
    };
    auto ctx = makeGateCtx({ { 4, 0.6 }, { 7, 0.5 }, { 3, 0.5 } }, 3, 4, /*tonic*/ 0);
    ChordTemporalContext temporal;
    temporal.bassIsStepwiseFromPrevious = true;
    applyPostScoringGates(results, baroquePrefs(), &temporal, ctx);
    EXPECT_EQ(results.front().identity.rootPc, 4);
}

// Gate E fires on the forward (to-next) stepwise signal, not just the from-previous one.
TEST(Composing_PostScoringGateTests, GateE_StepwiseToNext_Flips)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(6, 6, ChordQuality::Minor, 2.5),
        makeResult(2, 6, ChordQuality::Major, 1.5),   // D/F# : root 2 = (6+8)%12
    };
    auto ctx = makeGateCtx({ { 6, 0.6 }, { 9, 0.5 }, { 2, 0.5 } }, 3, 6, /*tonic D*/ 2);
    ChordTemporalContext temporal;
    temporal.bassIsStepwiseToNext = true;     // forward signal only
    applyPostScoringGates(results, baroquePrefs(), &temporal, ctx);
    EXPECT_EQ(results.front().identity.rootPc, 2);
}

// Gate G-E mediant arm (iiiø7): the half-diminished seventh rooted on the mediant
// (tonic+4) is a functional reading and flips with no temporal context.
TEST(Composing_PostScoringGateTests, GateGE_MediantFunctionFlip)
{
    // Gm6 (root 7) in C major; Eø7 (root 4) = mediant iiiø7; gExpectedAltRoot=(7+9)%12=4.
    std::vector<ChordAnalysisResult> results = {
        makeResult(7, 7, ChordQuality::Minor, 2.5, { Extension::AddedSixth }),
        makeResult(4, 7, ChordQuality::HalfDiminished, 1.5, { Extension::MinorSeventh }),
    };
    auto ctx = makeGateCtx({ { 7, 0.6 }, { 10, 0.5 }, { 2, 0.5 }, { 4, 0.4 } }, 4, 7,
                           /*tonic C*/ 0);
    applyPostScoringGates(results, baroquePrefs(), nullptr, ctx);
    EXPECT_EQ(results.front().identity.rootPc, 4);
    EXPECT_EQ(results.front().identity.quality, ChordQuality::HalfDiminished);
}

// Gate G with no half-diminished partner anywhere (not in results[], not above threshold
// in rawCandidates) leaves the Minor-add6 winner untouched.
TEST(Composing_PostScoringGateTests, GateG_NoHalfDimAnywhere_NoFlip)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(0, 0, ChordQuality::Minor, 2.5, { Extension::AddedSixth }),
        makeResult(3, 3, ChordQuality::Major, 1.2),   // clean filler, wrong root
    };
    auto ctx = makeGateCtx({ { 0, 0.5 }, { 3, 0.5 }, { 7, 0.5 } }, 4, 0, /*tonic C*/ 0,
                           /*threshold*/ 1.0);
    // Raw candidates scanned but never matched: a NON-half-diminished one (wrong quality)
    // and a half-diminished one at the WRONG root (5, not gExpected 9). Loop completes.
    ctx.rawCandidates = { rawCand(1.6, 9, ChordQuality::Major, 0),
                          rawCand(1.6, 5, ChordQuality::HalfDiminished, 8) };
    applyPostScoringGates(results, baroquePrefs(), nullptr, ctx);
    EXPECT_EQ(results.front().identity.rootPc, 0);
    EXPECT_EQ(results.size(), 2u);   // nothing pulled
}

// Gate G with the HalfDim alt present in results[] at the functional root but NO temporal
// signal that confirms it (forward root mismatched, not in the recent window, only one
// stepwise move): G-E (non-functional root), G-B, G-C and G-D all stay silent.
TEST(Composing_PostScoringGateTests, GateG_HalfDimPresentNoTemporalSignal_NoFlip)
{
    // Cm6 vs Aø7/C in C major: root 9 = vi, not viiø7/iiø7/iiiø7 ({11,2,4}).
    std::vector<ChordAnalysisResult> results = {
        makeResult(0, 0, ChordQuality::Minor, 2.5, { Extension::AddedSixth }),
        makeResult(9, 0, ChordQuality::HalfDiminished, 1.5, { Extension::MinorSeventh }),
    };
    auto ctx = makeGateCtx({ { 9, 0.4 }, { 0, 0.6 }, { 3, 0.5 }, { 7, 0.5 } }, 4, 0, /*tonic C*/ 0);
    ChordTemporalContext temporal;
    temporal.nextRootPc                 = 5;   // forward root, but != 9
    temporal.bassIsStepwiseFromPrevious = true;
    temporal.recentRootPcs              = { -1, -1, -1 };  // 9 not in the window
    temporal.consecutiveBassStepwiseCount = 1;             // < 2
    applyPostScoringGates(results, baroquePrefs(), &temporal, ctx);
    EXPECT_EQ(results.front().identity.rootPc, 0);
}

// Gate H-B no-fire arms: the augmented alt exists, but the forward root does not match it
// (and no other signal fires), so the winner does not rotate.
TEST(Composing_PostScoringGateTests, GateHB_ForwardRootMismatch_NoRotation)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(0, 0, ChordQuality::Augmented, 2.0),
        makeResult(4, 4, ChordQuality::Augmented, 1.8),   // a +4 alt only
    };
    auto ctx = makeGateCtx({ { 0, 0.5 }, { 4, 0.5 }, { 8, 0.5 } }, 3, 0);
    ChordTemporalContext temporal;
    temporal.nextRootPc           = 5;     // != 4 (the alt root) and != 8
    temporal.bassIsStepwiseToNext = true;
    applyPostScoringGates(results, baroquePrefs(), &temporal, ctx);
    EXPECT_EQ(results.front().identity.rootPc, 0);
}

// Gate H-B with a matching forward root but NO stepwise-to-next signal does not rotate.
TEST(Composing_PostScoringGateTests, GateHB_ForwardRootNoStepwise_NoRotation)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(0, 0, ChordQuality::Augmented, 2.0),
        makeResult(4, 4, ChordQuality::Augmented, 1.8),
    };
    auto ctx = makeGateCtx({ { 0, 0.5 }, { 4, 0.5 }, { 8, 0.5 } }, 3, 0);
    ChordTemporalContext temporal;
    temporal.nextRootPc           = 4;       // matches the alt root
    temporal.bassIsStepwiseToNext = false;   // but no stepwise motion
    applyPostScoringGates(results, baroquePrefs(), &temporal, ctx);
    EXPECT_EQ(results.front().identity.rootPc, 0);
}

// Gate H-C fires when the augmented alt root appears in recent-roots slot 0.
TEST(Composing_PostScoringGateTests, GateHC_RecentRootSlot0_RotatesPlus4)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(0, 0, ChordQuality::Augmented, 2.0),
        makeResult(4, 4, ChordQuality::Augmented, 1.8),
    };
    auto ctx = makeGateCtx({ { 0, 0.5 }, { 4, 0.5 }, { 8, 0.5 } }, 3, 0);
    ChordTemporalContext temporal;
    temporal.bassIsStepwiseFromPrevious = true;
    temporal.recentRootPcs              = { 4, -1, -1 };   // slot 0
    applyPostScoringGates(results, baroquePrefs(), &temporal, ctx);
    EXPECT_EQ(results.front().identity.rootPc, 4);
}

// Gate H-C fires when the augmented alt root appears in recent-roots slot 2.
TEST(Composing_PostScoringGateTests, GateHC_RecentRootSlot2_RotatesPlus4)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(0, 0, ChordQuality::Augmented, 2.0),
        makeResult(4, 4, ChordQuality::Augmented, 1.8),
    };
    auto ctx = makeGateCtx({ { 0, 0.5 }, { 4, 0.5 }, { 8, 0.5 } }, 3, 0);
    ChordTemporalContext temporal;
    temporal.bassIsStepwiseFromPrevious = true;
    temporal.recentRootPcs              = { -1, -1, 4 };   // slot 2
    applyPostScoringGates(results, baroquePrefs(), &temporal, ctx);
    EXPECT_EQ(results.front().identity.rootPc, 4);
}

// Gate G scan skips a half-diminished candidate at the WRONG root (not gExpected): the
// results[] scan evaluates a HalfDim entry whose root != (winnerRoot+9), finds no match.
TEST(Composing_PostScoringGateTests, GateG_HalfDimWrongRootInResults_NoFlip)
{
    // Cm6 (gExpected = 9); the HalfDim alt sits at root 5, not 9.
    std::vector<ChordAnalysisResult> results = {
        makeResult(0, 0, ChordQuality::Minor, 2.5, { Extension::AddedSixth }),
        makeResult(5, 0, ChordQuality::HalfDiminished, 1.5, { Extension::MinorSeventh }),
    };
    auto ctx = makeGateCtx({ { 5, 0.4 }, { 0, 0.6 }, { 7, 0.5 } }, 4, 0, /*tonic C*/ 0);
    applyPostScoringGates(results, baroquePrefs(), nullptr, ctx);
    EXPECT_EQ(results.front().identity.rootPc, 0);
}

// Gate H with a stepwise-from-previous bass but the alt root NOT in the recent-roots
// window (all three slots mismatch) and no forward root: no rotation.
TEST(Composing_PostScoringGateTests, GateH_RecentRootsAllMismatch_NoRotation)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(0, 0, ChordQuality::Augmented, 2.0),
        makeResult(4, 4, ChordQuality::Augmented, 1.8),   // a +4 alt only
    };
    auto ctx = makeGateCtx({ { 0, 0.5 }, { 4, 0.5 }, { 8, 0.5 } }, 3, 0);
    ChordTemporalContext temporal;
    temporal.bassIsStepwiseFromPrevious = true;
    temporal.recentRootPcs              = { -1, -1, -1 };   // 4 not in any slot
    temporal.consecutiveBassStepwiseCount = 1;             // < 2
    applyPostScoringGates(results, baroquePrefs(), &temporal, ctx);
    EXPECT_EQ(results.front().identity.rootPc, 0);
}

// No resolved key (keyTonicPc = -1, the "no key" sentinel / struct default): Gate I's
// diatonic first-inversion correction is disabled, so the Minor winner stands even though
// a diatonic-looking C/E inversion alt is present.
TEST(Composing_PostScoringGateTests, GateI_NoKeyResolved_NoFlip)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(4, 4, ChordQuality::Minor, 2.0, { Extension::MinorSeventh }),
        makeResult(0, 4, ChordQuality::Major, 1.6),   // C/E, would be I4 under a key
    };
    auto ctx = makeGateCtx({ { 0, 0.5 }, { 4, 0.6 }, { 7, 0.5 } }, 4, 4, /*keyTonic*/ -1);
    applyPostScoringGates(results, baroquePrefs(), nullptr, ctx);
    EXPECT_EQ(results.front().identity.rootPc, 4);
}

// No resolved key (keyTonicPc = -1) disables the same-root Augmented→Major demotion
// (Gate L): the Augmented winner is preserved. (Gate K, which shared this no-key guard,
// was RETIRED Stage 5 — 2026-07-05, D-7.)
TEST(Composing_PostScoringGateTests, GateKL_NoKeyResolved_NoChange)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(0, 0, ChordQuality::Augmented, 2.0),
        makeResult(0, 0, ChordQuality::Major, 1.8),   // same-root Major (Gate L target under a key)
    };
    auto ctx = makeGateCtx({ { 0, 0.6 }, { 4, 0.5 }, { 8, 0.5 } }, 3, 0, /*keyTonic*/ -1);
    applyPostScoringGates(results, kDefaultChordAnalyzerPreferences, nullptr, ctx);
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Augmented);
}

// Gate H scan steps past a non-augmented runner-up to reach the augmented alt deeper in
// the list, then rotates on the recent-roots signal.
TEST(Composing_PostScoringGateTests, GateH_NonAugmentedInScanPath_RotatesPlus4)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(0, 0, ChordQuality::Augmented, 2.0),
        makeResult(2, 2, ChordQuality::Minor, 1.9),       // non-augmented runner-up
        makeResult(4, 4, ChordQuality::Augmented, 1.8),   // the +4 augmented alt
    };
    auto ctx = makeGateCtx({ { 0, 0.5 }, { 4, 0.5 }, { 8, 0.5 }, { 2, 0.4 } }, 4, 0);
    ChordTemporalContext temporal;
    temporal.bassIsStepwiseFromPrevious = true;
    temporal.recentRootPcs              = { 4, -1, -1 };
    applyPostScoringGates(results, baroquePrefs(), &temporal, ctx);
    EXPECT_EQ(results.front().identity.rootPc, 4);
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Augmented);
}

// Gate J: a Diminished winner that is NOT in root position (rootPc != bassPc) is not a
// candidate for V7 completion → no swap.
TEST(Composing_PostScoringGateTests, GateJ_DiminishedNotRootPosition_NoSwap)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(10, 1, ChordQuality::Diminished, 2.5),                       // inverted dim
        makeResult(6, 10, ChordQuality::Major, 1.2, { Extension::MinorSeventh }),
    };
    auto ctx = makeGateCtx({ { 10, 0.5 }, { 1, 0.5 }, { 4, 0.5 }, { 6, 0.4 } }, 4, 1);
    applyPostScoringGates(results, kDefaultChordAnalyzerPreferences, nullptr, ctx);
    EXPECT_EQ(results.front().identity.rootPc, 10);
}

// Gate H-C: an augmented alt that appeared in the recent-roots window AND a stepwise bass
// from the previous region rotates the augmented winner.
TEST(Composing_PostScoringGateTests, GateHC_RecentRootStepwise_RotatesPlus4)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(0, 0, ChordQuality::Augmented, 2.0),
        makeResult(4, 4, ChordQuality::Augmented, 1.8),
    };
    auto ctx = makeGateCtx({ { 0, 0.5 }, { 4, 0.5 }, { 8, 0.5 } }, 3, 0);
    ChordTemporalContext temporal;
    temporal.bassIsStepwiseFromPrevious = true;
    temporal.recentRootPcs              = { -1, 4, -1 };
    applyPostScoringGates(results, baroquePrefs(), &temporal, ctx);
    EXPECT_EQ(results.front().identity.rootPc, 4);
}

// Gate H-D: two consecutive stepwise bass moves rotate to the +8 augmented alt (and the
// +4 search is skipped because no augmented alt sits there).
TEST(Composing_PostScoringGateTests, GateHD_ConsecutiveStepwise_RotatesPlus8)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(0, 0, ChordQuality::Augmented, 2.0),
        makeResult(8, 8, ChordQuality::Augmented, 1.8),   // only a +8 alt exists
    };
    auto ctx = makeGateCtx({ { 0, 0.5 }, { 4, 0.5 }, { 8, 0.5 } }, 3, 0);
    ChordTemporalContext temporal;
    temporal.consecutiveBassStepwiseCount = 2;
    applyPostScoringGates(results, baroquePrefs(), &temporal, ctx);
    EXPECT_EQ(results.front().identity.rootPc, 8);
}

// Gate L requires the SAME bass (root position): a same-root Major alt with a different
// bass is not a root-position re-reading, so the augmented winner stands.
TEST(Composing_PostScoringGateTests, GateL_SameRootDifferentBass_NoDemotion)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(11, 11, ChordQuality::Augmented, 2.0),
        makeResult(11, 3, ChordQuality::Major, 1.8),   // same root, DIFFERENT bass
    };
    auto ctx = makeGateCtx({ { 11, 0.6 }, { 3, 0.5 }, { 7, 0.5 } }, 3, 11);
    applyPostScoringGates(results, kDefaultChordAnalyzerPreferences, nullptr, ctx);
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Augmented);
}

// Gate L diatonic guard: a non-diatonic augmented root is not demoted to Major
// (the diatonic scan finds no match and the gate skips).
TEST(Composing_PostScoringGateTests, GateL_NonDiatonicRoot_NoDemotion)
{
    // C#+ (root 1) in C major — pc 1 is not diatonic.
    std::vector<ChordAnalysisResult> results = {
        makeResult(1, 1, ChordQuality::Augmented, 2.0),
        makeResult(1, 1, ChordQuality::Major, 1.8),
    };
    auto ctx = makeGateCtx({ { 1, 0.6 }, { 5, 0.5 }, { 9, 0.5 } }, 3, 1, /*tonic C*/ 0);
    applyPostScoringGates(results, kDefaultChordAnalyzerPreferences, nullptr, ctx);
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Augmented);
}

// Gate J present-root guard variant: the candidate sitting at the would-be dominant root
// is NOT Major (e.g. it is Minor) → no V7 completion.
TEST(Composing_PostScoringGateTests, GateJ_DominantCandidateNotMajor_NoSwap)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(10, 10, ChordQuality::Diminished, 2.5),
        makeResult(6, 10, ChordQuality::Minor, 1.2, { Extension::MinorSeventh }),  // not Major
    };
    auto ctx = makeGateCtx({ { 10, 0.5 }, { 1, 0.5 }, { 4, 0.5 }, { 6, 0.4 } }, 4, 10);
    applyPostScoringGates(results, kDefaultChordAnalyzerPreferences, nullptr, ctx);
    EXPECT_EQ(results.front().identity.rootPc, 10);
}

// ═════════════════════════════════════════════════════════════════════════════
// chordpostpasses.cpp — cptIsBassChordTone per-quality / per-extension classification,
// exercised through the two-pass pedal detection (applyIter8691Pedal). When the bass IS
// a chord tone the pedal pass is skipped; when it is foreign the upper voices are
// re-analysed and the chord is reclassified as a pedal point.
// ═════════════════════════════════════════════════════════════════════════════

namespace {
// gateCtx for a pedal-pass test: bass at bassPc, the region tones available for Pass-2
// re-analysis, default extension/pedal thresholds.
PostScoringGateContext pedalGateCtx(int bassPc,
                                    std::initializer_list<std::pair<int, double>> tones)
{
    PostScoringGateContext ctx;
    ctx.tpcForPc.fill(-1);
    ctx.scale        = { 0, 2, 4, 5, 7, 9, 11 };
    ctx.keyTonicPc   = 0;
    ctx.keyMode      = KeySigMode::Ionian;
    ctx.bassPc       = bassPc;
    ctx.bassTpc      = -1;
    ctx.keySigFifths = 0;
    bool first = true;
    for (const auto& pw : tones) {
        ChordAnalysisTone t;
        t.pitch  = pw.first;
        t.weight = pw.second;
        t.isBass = first;
        ctx.tones.push_back(t);
        ctx.pcWeight[static_cast<size_t>(((pw.first % 12) + 12) % 12)] += std::max(0.1, pw.second);
        first = false;
    }
    return ctx;
}
} // namespace

// Bass = perfect 5th of a Suspended4 chord → chord tone → NO pedal reclassification.
TEST(Composing_PostScoringGateTests, CptBassChordTone_Sus4PerfectFifth_NoPedal)
{
    std::vector<ChordAnalysisResult> results = { makeResult(0, 7, ChordQuality::Suspended4, 2.0) };
    auto ctx = pedalGateCtx(/*bass G*/ 7, { { 43, 1.0 }, { 60, 1.0 }, { 65, 1.0 } });
    applyIter8691Pedal(results, ctx, nullptr, kDefaultChordAnalyzerPreferences);
    EXPECT_FALSE(results.front().identity.isPedalPoint);
}

// Bass = #9 (interval 3) with the SharpNinth extension set → chord tone → no pedal.
TEST(Composing_PostScoringGateTests, CptBassChordTone_SharpNinth_NoPedal)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(0, 3, ChordQuality::Major, 2.0, { Extension::SharpNinth })
    };
    auto ctx = pedalGateCtx(/*bass D#*/ 3, { { 51, 1.0 }, { 60, 1.0 }, { 64, 1.0 }, { 67, 1.0 } });
    applyIter8691Pedal(results, ctx, nullptr, kDefaultChordAnalyzerPreferences);
    EXPECT_FALSE(results.front().identity.isPedalPoint);
}

// Bass = #11 (interval 6) with SharpEleventh → chord tone → no pedal.
TEST(Composing_PostScoringGateTests, CptBassChordTone_SharpEleventh_NoPedal)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(0, 6, ChordQuality::Major, 2.0, { Extension::SharpEleventh })
    };
    auto ctx = pedalGateCtx(/*bass F#*/ 6, { { 54, 1.0 }, { 60, 1.0 }, { 64, 1.0 }, { 67, 1.0 } });
    applyIter8691Pedal(results, ctx, nullptr, kDefaultChordAnalyzerPreferences);
    EXPECT_FALSE(results.front().identity.isPedalPoint);
}

// Bass = b13 (interval 8) with FlatThirteenth → chord tone → no pedal.
TEST(Composing_PostScoringGateTests, CptBassChordTone_FlatThirteenth_NoPedal)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(0, 8, ChordQuality::Major, 2.0, { Extension::FlatThirteenth })
    };
    auto ctx = pedalGateCtx(/*bass Ab*/ 8, { { 56, 1.0 }, { 60, 1.0 }, { 64, 1.0 }, { 67, 1.0 } });
    applyIter8691Pedal(results, ctx, nullptr, kDefaultChordAnalyzerPreferences);
    EXPECT_FALSE(results.front().identity.isPedalPoint);
}

// Bass = the perfect 4th (interval 5) over a chord carrying a (diminished) seventh →
// chord tone (11th of a 7th chord), not a pedal.
TEST(Composing_PostScoringGateTests, CptBassChordTone_FourthOverSeventh_NoPedal)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(0, 5, ChordQuality::Diminished, 2.0, { Extension::DiminishedSeventh })
    };
    auto ctx = pedalGateCtx(/*bass F*/ 5, { { 53, 1.0 }, { 60, 1.0 }, { 63, 1.0 }, { 66, 1.0 } });
    applyIter8691Pedal(results, ctx, nullptr, kDefaultChordAnalyzerPreferences);
    EXPECT_FALSE(results.front().identity.isPedalPoint);
}

// Foreign-bass FALSE arms: a bass that is NOT a chord tone of the labelled winner triggers
// the two-pass pedal reclassification (low-weight bass + a confident upper triad — the
// classic pedal shape, mirroring Composing_PedalPointTests).
TEST(Composing_PostScoringGateTests, CptBassChordTone_ForeignBass_PedalDetected)
{
    // Bass at the major-7th of a plain Major triad (no Maj7 ext) — foreign.
    {
        std::vector<ChordAnalysisResult> results = { makeResult(0, 11, ChordQuality::Major, 2.0) };
        auto ctx = pedalGateCtx(/*bass B*/ 11, { { 47, 0.2 }, { 60, 1.0 }, { 64, 1.0 }, { 67, 1.0 } });
        applyIter8691Pedal(results, ctx, nullptr, kDefaultChordAnalyzerPreferences);
        EXPECT_TRUE(results.front().identity.isPedalPoint);
        EXPECT_EQ(results.front().identity.pedalBassPc, 11);
    }
    // Bass at the natural 9th (interval 2) of a plain Major triad (no nat-9 ext) — foreign.
    {
        std::vector<ChordAnalysisResult> results = { makeResult(0, 2, ChordQuality::Major, 2.0) };
        auto ctx = pedalGateCtx(/*bass D*/ 2, { { 50, 0.2 }, { 60, 1.0 }, { 64, 1.0 }, { 67, 1.0 } });
        applyIter8691Pedal(results, ctx, nullptr, kDefaultChordAnalyzerPreferences);
        EXPECT_TRUE(results.front().identity.isPedalPoint);
        EXPECT_EQ(results.front().identity.pedalBassPc, 2);
    }
    // Bass foreign to a Power chord (not the perfect 5th).
    {
        std::vector<ChordAnalysisResult> results = { makeResult(0, 3, ChordQuality::Power, 2.0) };
        auto ctx = pedalGateCtx(/*bass D#*/ 3, { { 51, 0.2 }, { 60, 1.0 }, { 64, 1.0 }, { 67, 1.0 } });
        applyIter8691Pedal(results, ctx, nullptr, kDefaultChordAnalyzerPreferences);
        EXPECT_TRUE(results.front().identity.isPedalPoint);
        EXPECT_EQ(results.front().identity.pedalBassPc, 3);
    }
}

// bassPc < 0 (sparse region, no valid bass): Iter 86, Iter 91 and the pedal pass all skip.
TEST(Composing_PostScoringGateTests, Iter8691Pedal_NegativeBassPc_AllPassesSkip)
{
    std::vector<ChordAnalysisResult> results = { makeResult(9, 7, ChordQuality::Minor, 2.0) };
    PostScoringGateContext ctx;
    ctx.tpcForPc.fill(-1);
    ctx.scale  = { 0, 2, 4, 5, 7, 9, 11 };
    ctx.bassPc = -1;   // no valid bass
    ChordTemporalContext temporal;
    temporal.nextRootPc = 7;   // would otherwise drive Iter 91
    applyIter8691Pedal(results, ctx, &temporal, kDefaultChordAnalyzerPreferences);
    EXPECT_EQ(results.front().identity.rootPc, 9);                      // untouched
    EXPECT_FALSE(hasExtension(results.front().identity.extensions, Extension::MinorSeventh));
    EXPECT_FALSE(results.front().identity.isPedalPoint);
}

// Iter 91 promotes only plain triads of the right delta/quality. A MAJOR winner at delta 8
// (the Pattern-A delta, which requires Minor) does not promote.
TEST(Composing_PostScoringGateTests, Iter91_Delta8MajorWinner_NoPromotion)
{
    std::vector<ChordAnalysisResult> results = { makeResult(0, 8, ChordQuality::Major, 2.0) };
    auto ctx = makeGateCtx({ { 8, 0.5 }, { 0, 0.6 }, { 4, 0.5 } }, 3, 8);
    ctx.rawCandidates = { rawCand(2.2, 8, ChordQuality::Minor, 4) };
    ChordTemporalContext temporal;
    temporal.nextRootPc = 8;
    applyIter8691Pedal(results, ctx, &temporal, kDefaultChordAnalyzerPreferences);
    EXPECT_EQ(results.front().identity.rootPc, 0);   // not promoted (Major at delta 8)
}

// Iter 91 leaves a SEVENTH chord alone even at a promotable delta/quality (plain-triad guard).
TEST(Composing_PostScoringGateTests, Iter91_SeventhWinner_NoPromotion)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(4, 0, ChordQuality::Minor, 2.0, { Extension::MinorSeventh })   // Em7/C, delta 8
    };
    auto ctx = makeGateCtx({ { 0, 0.6 }, { 4, 0.5 }, { 7, 0.5 } }, 3, 0);
    ctx.rawCandidates = { rawCand(2.2, 0, ChordQuality::Major, 0) };
    ChordTemporalContext temporal;
    temporal.nextRootPc = 0;
    applyIter8691Pedal(results, ctx, &temporal, kDefaultChordAnalyzerPreferences);
    EXPECT_EQ(results.front().identity.rootPc, 4);   // seventh chord not promoted
}

// Iter 91 fires (Pattern A, plain triad, forward-confirmed) but no rawCandidate is rooted
// at the bass → the scan completes without a promotion.
TEST(Composing_PostScoringGateTests, Iter91_NoBassRootedRawCandidate_NoPromotion)
{
    std::vector<ChordAnalysisResult> results = { makeResult(4, 0, ChordQuality::Minor, 2.0) };  // Em/C
    auto ctx = makeGateCtx({ { 0, 0.6 }, { 4, 0.5 }, { 7, 0.5 } }, 3, 0);
    ctx.rawCandidates = { rawCand(2.2, 5, ChordQuality::Major, 0) };   // rooted at 5, not bass 0
    ChordTemporalContext temporal;
    temporal.nextRootPc = 0;
    applyIter8691Pedal(results, ctx, &temporal, kDefaultChordAnalyzerPreferences);
    EXPECT_EQ(results.front().identity.rootPc, 4);   // no bass-rooted candidate to promote to
}

// ═════════════════════════════════════════════════════════════════════════════
// §6-block dissolution audit (Phase 2.2, design D-7): per-rule disable.
//
// For every §6 rule, reconstruct the SAME firing fixture pinned above, run it with
// ONLY that rule disabled (all others enabled), and assert it no longer fires —
// proving the `disable_rule` hook cleanly skips exactly that rule's rank mutation.
// The enabled arm re-asserts the pinned outcome so the pair is a live before/after.
// The fixture resets the process-global disable state around every test.
// ═════════════════════════════════════════════════════════════════════════════

class PostScoringRuleDisable : public ::testing::Test {
protected:
    void SetUp() override { P::resetPostScoringRules(); }
    void TearDown() override { P::resetPostScoringRules(); }
};

TEST_F(PostScoringRuleDisable, BiasCorrection_DisabledDoesNotFire)
{
    auto build = [] {
        return std::vector<ChordAnalysisResult>{
            makeResult(0, 0, ChordQuality::Major, 2.0),
            makeResult(4, 4, ChordQuality::Minor, 1.5),
        };
    };
    auto ctx = makeGateCtx({ { 0, 0.6 }, { 4, 0.5 }, { 7, 0.5 }, { 11, 0.3 } }, 4, 0);

    auto on = build();
    applyPostScoringGates(on, baroquePrefs(), nullptr, ctx);
    EXPECT_EQ(on.front().identity.rootPc, 4);   // enabled: Em promoted

    P::setRuleDisabled(P::PostScoringRule::BiasCorrection, true);
    auto off = build();
    applyPostScoringGates(off, baroquePrefs(), nullptr, ctx);
    EXPECT_EQ(off.front().identity.rootPc, 0);   // disabled: C stays, no deduction
    EXPECT_NEAR(off.front().identity.score, 2.0, 1e-9);
}

TEST_F(PostScoringRuleDisable, FM2_DisabledDoesNotFire)
{
    auto build = [] {
        return std::vector<ChordAnalysisResult>{
            makeResult(10, 10, ChordQuality::Major, 2.5, { Extension::AddedSixth }),
            makeResult(2, 2, ChordQuality::Minor, 1.4),   // clean alt at the WRONG root
        };
    };
    auto mkctx = [] {
        auto c = makeGateCtx({ { 10, 0.6 }, { 2, 0.5 }, { 5, 0.5 }, { 7, 0.4 } }, 4, 10, 5, 1.0);
        c.rawCandidates = { rawCand(1.6, 7, ChordQuality::Minor, 5) };
        return c;
    };

    auto on = build(); auto ctxOn = mkctx();
    applyPostScoringGates(on, baroquePrefs(), nullptr, ctxOn);
    EXPECT_EQ(on.front().identity.rootPc, 7);   // enabled: partner pulled from raw

    P::setRuleDisabled(P::PostScoringRule::FM2, true);
    auto off = build(); auto ctxOff = mkctx();
    applyPostScoringGates(off, baroquePrefs(), nullptr, ctxOff);
    EXPECT_EQ(off.front().identity.rootPc, 10);   // Gate A can't fire (partner off-root)
}

TEST_F(PostScoringRuleDisable, GateE_DisabledDoesNotFire)
{
    auto build = [] {
        return std::vector<ChordAnalysisResult>{
            makeResult(6, 6, ChordQuality::Minor, 2.5),
            makeResult(2, 6, ChordQuality::Major, 1.5),
        };
    };
    auto ctx = makeGateCtx({ { 6, 0.6 }, { 9, 0.5 }, { 2, 0.5 } }, 3, 6, 2);
    ChordTemporalContext temporal;
    temporal.bassIsStepwiseFromPrevious = true;

    auto on = build();
    applyPostScoringGates(on, baroquePrefs(), &temporal, ctx);
    EXPECT_EQ(on.front().identity.rootPc, 2);

    P::setRuleDisabled(P::PostScoringRule::GateE, true);
    auto off = build();
    applyPostScoringGates(off, baroquePrefs(), &temporal, ctx);
    EXPECT_EQ(off.front().identity.rootPc, 6);
}

TEST_F(PostScoringRuleDisable, GateGE_DisabledDoesNotFire)
{
    auto build = [] {
        return std::vector<ChordAnalysisResult>{
            makeResult(2, 2, ChordQuality::Minor, 2.5, { Extension::AddedSixth }),
            makeResult(11, 2, ChordQuality::HalfDiminished, 1.5, { Extension::MinorSeventh }),
        };
    };
    auto ctx = makeGateCtx({ { 2, 0.6 }, { 5, 0.5 }, { 9, 0.5 }, { 11, 0.4 } }, 4, 2);

    auto on = build();
    applyPostScoringGates(on, baroquePrefs(), nullptr, ctx);
    EXPECT_EQ(on.front().identity.rootPc, 11);

    P::setRuleDisabled(P::PostScoringRule::GateGE, true);
    auto off = build();
    applyPostScoringGates(off, baroquePrefs(), nullptr, ctx);
    EXPECT_EQ(off.front().identity.rootPc, 2);   // no context → temporal fallbacks silent
}

TEST_F(PostScoringRuleDisable, GateGD_DisabledDoesNotFire)
{
    auto build = [] {
        return std::vector<ChordAnalysisResult>{
            makeResult(0, 0, ChordQuality::Minor, 2.5, { Extension::AddedSixth }),
            makeResult(9, 0, ChordQuality::HalfDiminished, 1.5, { Extension::MinorSeventh }),
        };
    };
    auto ctx = makeGateCtx({ { 9, 0.4 }, { 0, 0.6 }, { 3, 0.5 }, { 7, 0.5 } }, 4, 0);
    ChordTemporalContext temporal;
    temporal.consecutiveBassStepwiseCount = 2;

    auto on = build();
    applyPostScoringGates(on, baroquePrefs(), &temporal, ctx);
    EXPECT_EQ(on.front().identity.rootPc, 9);

    P::setRuleDisabled(P::PostScoringRule::GateGD, true);
    auto off = build();
    applyPostScoringGates(off, baroquePrefs(), &temporal, ctx);
    EXPECT_EQ(off.front().identity.rootPc, 0);
}

TEST_F(PostScoringRuleDisable, GateH_DisabledDoesNotFire)
{
    auto build = [] {
        return std::vector<ChordAnalysisResult>{
            makeResult(0, 0, ChordQuality::Augmented, 2.0),
            makeResult(4, 4, ChordQuality::Augmented, 1.8),
        };
    };
    auto ctx = makeGateCtx({ { 0, 0.5 }, { 4, 0.5 }, { 8, 0.5 } }, 3, 0);
    ChordTemporalContext temporal;
    temporal.nextRootPc           = 4;
    temporal.bassIsStepwiseToNext = true;

    auto on = build();
    applyPostScoringGates(on, baroquePrefs(), &temporal, ctx);
    EXPECT_EQ(on.front().identity.rootPc, 4);

    P::setRuleDisabled(P::PostScoringRule::GateH, true);
    auto off = build();
    applyPostScoringGates(off, baroquePrefs(), &temporal, ctx);
    EXPECT_EQ(off.front().identity.rootPc, 0);
}

TEST_F(PostScoringRuleDisable, GateI_DisabledDoesNotFire)
{
    auto build = [] {
        return std::vector<ChordAnalysisResult>{
            makeResult(4, 4, ChordQuality::Minor, 2.0, { Extension::MinorSeventh }),
            makeResult(0, 4, ChordQuality::Major, 1.57),   // C/E, margin 0.43 <= 0.45
        };
    };
    auto ctx = makeGateCtx({ { 0, 0.5 }, { 4, 0.6 }, { 7, 0.5 }, { 2, 0.3 } }, 4, 4);

    auto on = build();
    applyPostScoringGates(on, baroquePrefs(), nullptr, ctx);
    EXPECT_EQ(on.front().identity.rootPc, 0);

    P::setRuleDisabled(P::PostScoringRule::GateI, true);
    auto off = build();
    applyPostScoringGates(off, baroquePrefs(), nullptr, ctx);
    EXPECT_EQ(off.front().identity.rootPc, 4);   // bias correction seventh-exempt → no swap
}

TEST_F(PostScoringRuleDisable, GateL_DisabledDoesNotFire)
{
    auto build = [] {
        return std::vector<ChordAnalysisResult>{
            makeResult(11, 11, ChordQuality::Augmented, 2.0),
            makeResult(11, 11, ChordQuality::Major, 1.67),   // margin 0.33 <= 0.35
        };
    };
    auto ctx = makeGateCtx({ { 11, 0.6 }, { 3, 0.5 }, { 7, 0.5 } }, 3, 11);

    auto on = build();
    applyPostScoringGates(on, kDefaultChordAnalyzerPreferences, nullptr, ctx);
    EXPECT_EQ(on.front().identity.quality, ChordQuality::Major);

    P::setRuleDisabled(P::PostScoringRule::GateL, true);
    auto off = build();
    applyPostScoringGates(off, kDefaultChordAnalyzerPreferences, nullptr, ctx);
    EXPECT_EQ(off.front().identity.quality, ChordQuality::Augmented);
}

TEST_F(PostScoringRuleDisable, GateJ_DisabledDoesNotFire)
{
    auto build = [] {
        return std::vector<ChordAnalysisResult>{
            makeResult(10, 10, ChordQuality::Diminished, 2.5),
            makeResult(6, 10, ChordQuality::Major, 1.2, { Extension::MinorSeventh }),
        };
    };
    auto ctx = makeGateCtx({ { 10, 0.5 }, { 1, 0.5 }, { 4, 0.5 }, { 6, 0.4 } }, 4, 10);

    auto on = build();
    applyPostScoringGates(on, kDefaultChordAnalyzerPreferences, nullptr, ctx);
    EXPECT_EQ(on.front().identity.rootPc, 6);

    P::setRuleDisabled(P::PostScoringRule::GateJ, true);
    auto off = build();
    applyPostScoringGates(off, kDefaultChordAnalyzerPreferences, nullptr, ctx);
    EXPECT_EQ(off.front().identity.rootPc, 10);
}
