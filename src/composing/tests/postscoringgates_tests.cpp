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

#include <initializer_list>
#include <utility>
#include <vector>

#include "test_helpers.h"

#include "composing/analysis/chord/chordanalyzer.h"

using namespace mu::composing::analysis;

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
// Gate A — Major-add6 ↔ Minor7 enharmonic fast path (§6 "A–D"). Fires
// unconditionally (no margin, no temporal evidence) when preferMinorOverMajorAdd6,
// winner is Major+AddedSixth, and the best clean alt is Minor at (root+9)%12.
// NOTE: gates B/C/D in this family are unreachable — their preconditions are a
// superset of Gate A's, which always fires first (report §Findings).
// ═════════════════════════════════════════════════════════════════════════════

TEST(Composing_PostScoringGateTests, GateA_FastPath_FiresWithoutTemporalOrMargin)
{
    // Bb6 vs Gm7/Bb in F major. Margin 1.0 (> 0.70) and context == nullptr:
    // only the unconditional fast path can flip.
    std::vector<ChordAnalysisResult> results = {
        makeResult(10, 10, ChordQuality::Major, 2.5, { Extension::AddedSixth }),
        makeResult(7, 10, ChordQuality::Minor, 1.5, { Extension::MinorSeventh }),
    };
    auto ctx = makeGateCtx({ { 10, 0.6 }, { 2, 0.5 }, { 5, 0.5 }, { 7, 0.4 } }, 4, 10, 5);
    applyPostScoringGates(results, baroquePrefs(), nullptr, ctx);

    EXPECT_EQ(results.front().identity.rootPc, 7);
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Minor);
    // Swap only — scores are not modified.
    EXPECT_NEAR(results.front().identity.score, 1.5, 1e-9);
}

// Preset branch: preferMinorOverMajorAdd6 = false (Jazz) keeps the idiomatic
// added-sixth reading.
TEST(Composing_PostScoringGateTests, GateA_PresetOff_NoFlip)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(10, 10, ChordQuality::Major, 2.5, { Extension::AddedSixth }),
        makeResult(7, 10, ChordQuality::Minor, 1.5, { Extension::MinorSeventh }),
    };
    auto ctx = makeGateCtx({ { 10, 0.6 }, { 2, 0.5 }, { 5, 0.5 }, { 7, 0.4 } }, 4, 10, 5);
    applyPostScoringGates(results, kDefaultChordAnalyzerPreferences, nullptr, ctx);
    EXPECT_EQ(results.front().identity.rootPc, 10);
}

// Added-sixth guard: a plain Major winner (no AddedSixth) does not flip to the
// relative minor just because it is a candidate.
TEST(Composing_PostScoringGateTests, GateA_PlainMajorWinner_NoFlip)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(0, 0, ChordQuality::Major, 2.5),
        makeResult(9, 0, ChordQuality::Minor, 1.5, { Extension::MinorSeventh }),
    };
    auto ctx = makeGateCtx({ { 0, 0.6 }, { 4, 0.5 }, { 7, 0.5 } }, 3, 0);
    applyPostScoringGates(results, baroquePrefs(), nullptr, ctx);
    EXPECT_EQ(results.front().identity.rootPc, 0);
}

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

// ═════════════════════════════════════════════════════════════════════════════
// Gate F — second-inversion detection (§6): best clean alt is Major at
// (root+5)%12 (winner root = P5 of alt root), stepwise bass. Unlike Gate E
// there is no alt-root pcWeight check and no winner-quality restriction beyond
// the targeted Major/Minor block guard.
// ═════════════════════════════════════════════════════════════════════════════

TEST(Composing_PostScoringGateTests, GateF_MajorWinnerFlipsToMajorAtPlus5)
{
    // B vs E/B (margin 1.0 — margin-free; lookahead stepwise licenses).
    std::vector<ChordAnalysisResult> results = {
        makeResult(11, 11, ChordQuality::Major, 2.5),
        makeResult(4, 11, ChordQuality::Major, 1.5),
    };
    auto ctx = makeGateCtx({ { 11, 0.6 }, { 4, 0.5 }, { 8, 0.5 } }, 3, 11, /*tonic E*/ 4);
    ChordTemporalContext temporal;
    temporal.bassIsStepwiseToNext = true;
    applyPostScoringGates(results, baroquePrefs(), &temporal, ctx);

    EXPECT_EQ(results.front().identity.rootPc, 4);
}

TEST(Composing_PostScoringGateTests, GateF_NoStepwiseSignal_NoFlip)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(11, 11, ChordQuality::Major, 2.5),
        makeResult(4, 11, ChordQuality::Major, 1.5),
    };
    auto ctx = makeGateCtx({ { 11, 0.6 }, { 4, 0.5 }, { 8, 0.5 } }, 3, 11, 4);
    ChordTemporalContext temporal;
    applyPostScoringGates(results, baroquePrefs(), &temporal, ctx);
    EXPECT_EQ(results.front().identity.rootPc, 11);
}

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

// G-B: forward evidence — next region's root equals the HalfDim root and the
// bass moves stepwise toward it.
TEST(Composing_PostScoringGateTests, GateGB_ForwardEvidenceFlips)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(0, 0, ChordQuality::Minor, 2.5, { Extension::AddedSixth }),
        makeResult(9, 0, ChordQuality::HalfDiminished, 1.5, { Extension::MinorSeventh }),
    };
    // C major: root 9 is non-functional (vi), so G-E stays silent and the
    // temporal fallbacks carry the decision.
    auto ctx = makeGateCtx({ { 9, 0.4 }, { 0, 0.6 }, { 3, 0.5 }, { 7, 0.5 } }, 4, 0);
    ChordTemporalContext temporal;
    temporal.nextRootPc          = 9;
    temporal.bassIsStepwiseToNext = true;
    applyPostScoringGates(results, baroquePrefs(), &temporal, ctx);

    EXPECT_EQ(results.front().identity.rootPc, 9);
}

// G-C: alt root recently active + stepwise bass from previous region.
TEST(Composing_PostScoringGateTests, GateGC_RecentRootAndStepwiseFlips)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(0, 0, ChordQuality::Minor, 2.5, { Extension::AddedSixth }),
        makeResult(9, 0, ChordQuality::HalfDiminished, 1.5, { Extension::MinorSeventh }),
    };
    auto ctx = makeGateCtx({ { 9, 0.4 }, { 0, 0.6 }, { 3, 0.5 }, { 7, 0.5 } }, 4, 0);
    ChordTemporalContext temporal;
    temporal.bassIsStepwiseFromPrevious = true;
    temporal.recentRootPcs              = { -1, 9, -1 };
    applyPostScoringGates(results, baroquePrefs(), &temporal, ctx);

    EXPECT_EQ(results.front().identity.rootPc, 9);
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

// ═════════════════════════════════════════════════════════════════════════════
// Gate K — first-inversion Augmented over root-position Augmented (§6):
// same bass, I4 interval, alt is an augmented collection (Augmented quality OR
// Major+SharpFifth), alt root diatonic, margin <= 0.20. Not preset-gated.
// ═════════════════════════════════════════════════════════════════════════════

TEST(Composing_PostScoringGateTests, GateK_MarginBracket)
{
    // bwv40.6 shape: A+ → F#5/A (alt root 5 = bass 9 minus M3; F diatonic in C).
    auto run = [](double altScore) {
        std::vector<ChordAnalysisResult> results = {
            makeResult(9, 9, ChordQuality::Augmented, 2.0),
            makeResult(5, 9, ChordQuality::Augmented, altScore),
        };
        auto ctx = makeGateCtx({ { 9, 0.5 }, { 1, 0.5 }, { 5, 0.5 } }, 3, 9);
        applyPostScoringGates(results, kDefaultChordAnalyzerPreferences, nullptr, ctx);
        return results.front().identity.rootPc;
    };

    EXPECT_EQ(run(1.82), 5);   // margin 0.18 <= 0.20 → first-inversion reading
    EXPECT_EQ(run(1.78), 9);   // margin 0.22 > 0.20 → A+ stays
}

// Second encoding variant of an augmented collection: Major + SharpFifth.
TEST(Composing_PostScoringGateTests, GateK_MajorSharpFifthEncodingAccepted)
{
    std::vector<ChordAnalysisResult> results = {
        makeResult(9, 9, ChordQuality::Augmented, 2.0),
        makeResult(5, 9, ChordQuality::Major, 1.9, { Extension::SharpFifth }),
    };
    auto ctx = makeGateCtx({ { 9, 0.5 }, { 1, 0.5 }, { 5, 0.5 } }, 3, 9);
    applyPostScoringGates(results, kDefaultChordAnalyzerPreferences, nullptr, ctx);

    EXPECT_EQ(results.front().identity.rootPc, 5);
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Major);
}

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
