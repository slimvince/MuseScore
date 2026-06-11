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

// diagnose_tests.cpp — Stage 2.3 (implementation_roadmap.md 2.3)
//
// diagnoseChord() is now a VIEW into the production pipeline (analyzeChord +
// applyIter8691Pedal + applyPostScoringGates), not a separate scorer. The catalog-wide
// agreement invariant (diagnose.finalWinner == analyzeWithGates().front(), identity AND
// score) is pinned in chordanalyzer_musicxml_tests.cpp
// (DiagnoseMatchesProductionPipeline). This file pins the acceptance case from the
// roadmap: the introspection dump must surface the rcb / Gate-R decision whose ABSENCE
// in the legacy diagnose scorer caused the historical mis-diagnoses (the bwv320
// "slash-synthesis" retraction; the bwv14.5 mischaracterisation — both in
// COWORK_HANDOFF).

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

// Find the competition candidate for a (rootPc, bassPc) pair in the winning bass group.
const DiagnosticCompetitionCandidate* findCompetition(
    const ChordAnalysisDiagnosticResult& diag, int rootPc, int bassPc)
{
    for (const auto& c : diag.competition) {
        if (c.rootPc == rootPc && c.bassPc == bassPc) { return &c; }
    }
    return nullptr;
}

} // namespace

// Acceptance case (roadmap 2.3): the bwv320 Δ=+7b mapping G/E → C. A predecessor root
// G continues into a region spanning {E, G, C} with bass E. The continued-root
// candidate G/E has its bass a M6 above the root (interval 9 — in no template) and
// earns no bass-dependent credit, so Gate R withholds the +0.40 rootContinuityBonus and
// the first-inversion C/E reading wins on its raw vertical lead. The dump must SHOW that
// rcb was withheld by Gate R on the continued-root candidate AND that the production
// winner is C — the exact information whose absence drove the historical mis-diagnoses.
TEST(Composing_DiagnoseTests, DeltaPlus7b_DumpShowsGateRWithheldRcbAndWinnerC)
{
    // G weighted heavily (held across the region) so the continued-root candidate is
    // genuinely competitive — identical fixture to
    // postscoringgates_tests.cpp E2E_GateR_DeltaPlus7b_FirstInversionBeatsContinuedRoot.
    const auto ts = weightedTones({ { 40, 1.0 }, { 55, 2.2 }, { 60, 0.8 }, { 64, 0.5 } });
    ChordTemporalContext temporal;
    temporal.previousRootPc  = 7;                      // G
    temporal.previousQuality = ChordQuality::Major;
    temporal.recentRootPcs   = { 7, -1, -1 };

    const ChordAnalysisDiagnosticResult diag =
        kAnalyzer.diagnoseChord(ts, /*fifths*/ 0, KeySigMode::Ionian, &temporal, baroquePrefs());

    // ── FINAL winner: production winner by construction = C / E ───────────────
    ASSERT_TRUE(diag.hasWinner);
    EXPECT_EQ(diag.finalWinner.identity.rootPc, 0);   // C
    EXPECT_EQ(diag.finalWinner.identity.bassPc, 4);   // E (first inversion)

    // Cross-check: the dump's winner equals the real production pipeline's winner.
    const auto production = analyzeWithGates(kAnalyzer, ts, 0, KeySigMode::Ionian,
                                             &temporal, baroquePrefs());
    ASSERT_FALSE(production.empty());
    EXPECT_EQ(diag.finalWinner.identity.rootPc, production.front().identity.rootPc);
    EXPECT_EQ(diag.finalWinner.identity.bassPc, production.front().identity.bassPc);
    EXPECT_DOUBLE_EQ(diag.finalWinner.identity.score, production.front().identity.score);

    // ── COMPETITION: the continued-root G/E candidate shows rcb withheld ──────
    // Bass E (pc 4) is the winning bass group; the continued root is G (pc 7).
    const DiagnosticCompetitionCandidate* contRoot = findCompetition(diag, /*root*/ 7, /*bass*/ 4);
    ASSERT_NE(contRoot, nullptr)
        << "the continued-root candidate G/E must appear in the winning bass group";
    EXPECT_TRUE(contRoot->rootContinuityWithheldByGateR)
        << "Gate R must withhold rcb from the bass-foreign continued root";
    EXPECT_DOUBLE_EQ(contRoot->rootContinuityBonus, 0.0);          // withheld → in effect 0
    EXPECT_GT(contRoot->rootContinuityBonusRaw, 0.0);              // but the +0.40 was earned

    // ── The winning C/E candidate is NOT subject to Gate R ────────────────────
    const DiagnosticCompetitionCandidate* winner = findCompetition(diag, /*root*/ 0, /*bass*/ 4);
    ASSERT_NE(winner, nullptr);
    EXPECT_FALSE(winner->rootContinuityWithheldByGateR);
    // C is the production winner, so it must be the top competition candidate by score.
    EXPECT_GE(winner->competitionScore, contRoot->competitionScore);
}

// The agreement invariant holds for an insufficient-data region too: when the pipeline
// produces no winner, diagnose reports no winner (no fabricated result from a re-scorer).
TEST(Composing_DiagnoseTests, InsufficientData_NoWinnerMatchesProduction)
{
    // Two distinct pitch classes → below minDistinctPcsForCandidate (3).
    const auto ts = weightedTones({ { 60, 1.0 }, { 67, 1.0 } });
    const ChordAnalysisDiagnosticResult diag =
        kAnalyzer.diagnoseChord(ts, 0, KeySigMode::Ionian, nullptr, baroquePrefs());
    const auto production = analyzeWithGates(kAnalyzer, ts, 0, KeySigMode::Ionian,
                                             nullptr, baroquePrefs());
    EXPECT_TRUE(production.empty());
    EXPECT_FALSE(diag.hasWinner);
    EXPECT_TRUE(diag.oracleCells.empty());
    EXPECT_TRUE(diag.competition.empty());
}
