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

// ── Test-backfill (criterion 2): analyzeChord ROBUSTNESS on degenerate input ──
//
// Before this file the only degenerate-input assertion for the L4 chord analyzer
// was the "< 3 distinct pitch classes -> empty" gate. Criterion 2 (odd/empty/null/
// outlier input must not crash any layer and must yield a defined result) was the
// genuine hole (cc_tree_repair_and_coverage_report.md C1 §6).
//
// These tests assert the DEFINED CONTRACT, derived independently of the
// implementation's tuned output:
//   • fewer than 3 distinct pitch classes (empty / single / unison / 2-distinct)
//     -> EMPTY result (the documented insufficient-data contract);
//   • atonal clusters, out-of-range key signatures, and absent/invalid TPC ->
//     NO CRASH and a STRUCTURALLY VALID result (every candidate has rootPc/bassPc
//     in [0,12) and a valid quality enum). The exact winning chord for a
//     non-tertian cluster is a tuned heuristic and is NOT pinned here.
//
// rule 3: if any input below CRASHES, that is a surfaced defect to report (not to
// guard with production code in this pass). All of these currently pass.

#include <gtest/gtest.h>

#include <vector>

#include "composing/analysis/chord/chordanalyzer.h"

#include "test_helpers.h"

using namespace mu::composing::analysis;

namespace {

const RuleBasedChordAnalyzer kAnalyzer{};

// A tone with an explicit (pitch, tpc); weight 1, first = bass.
std::vector<ChordAnalysisTone> tonesTpc(std::initializer_list<std::pair<int, int>> pts)
{
    std::vector<ChordAnalysisTone> out;
    bool first = true;
    for (const auto& pt : pts) {
        ChordAnalysisTone t;
        t.pitch = pt.first;
        t.tpc = pt.second;
        t.weight = 1.0;
        t.isBass = first;
        out.push_back(t);
        first = false;
    }
    return out;
}

// Defined-behaviour check: every candidate is structurally valid (no UB / garbage).
void expectStructurallyValid(const std::vector<ChordAnalysisResult>& results)
{
    for (const ChordAnalysisResult& r : results) {
        EXPECT_GE(r.identity.rootPc, 0);
        EXPECT_LT(r.identity.rootPc, 12);
        EXPECT_GE(r.identity.bassPc, 0);
        EXPECT_LT(r.identity.bassPc, 12);
        EXPECT_GE(static_cast<int>(r.identity.quality), static_cast<int>(ChordQuality::Unknown));
        EXPECT_LE(static_cast<int>(r.identity.quality), static_cast<int>(ChordQuality::Power));
    }
}

} // namespace

// ── Insufficient distinct pitch classes -> EMPTY (criterion 2, 3 contract) ───

TEST(Composing_AnalyzeChordRobustness, EmptyToneSet_ReturnsEmpty)
{
    const auto results = analyzeWithGates(kAnalyzer, {}, 0, KeySigMode::Ionian);
    EXPECT_TRUE(results.empty());
}

TEST(Composing_AnalyzeChordRobustness, SingleNote_ReturnsEmpty)
{
    const auto results = analyzeWithGates(kAnalyzer, tones({ 60 }), 0, KeySigMode::Ionian);
    EXPECT_TRUE(results.empty());
}

TEST(Composing_AnalyzeChordRobustness, UnisonAllSamePitch_ReturnsEmpty)
{
    const auto results = analyzeWithGates(kAnalyzer, tones({ 60, 60, 60 }), 0, KeySigMode::Ionian);
    EXPECT_TRUE(results.empty());
}

TEST(Composing_AnalyzeChordRobustness, SamePitchClassDifferentOctaves_ReturnsEmpty)
{
    // Three Cs (one distinct pitch class) — still insufficient.
    const auto results = analyzeWithGates(kAnalyzer, tones({ 48, 60, 72 }), 0, KeySigMode::Ionian);
    EXPECT_TRUE(results.empty());
}

// ── Atonal / non-tertian clusters -> no crash, valid result (criterion 2) ────

TEST(Composing_AnalyzeChordRobustness, ChromaticClusterThreePcs_NoCrashValidResult)
{
    // {C, C#, D} — three distinct, non-tertian pitch classes. The analyzer must not
    // crash; whatever it returns must be structurally valid (the winning label is a
    // tuned heuristic and is not asserted).
    const auto results = analyzeWithGates(kAnalyzer, tones({ 60, 61, 62 }), 0, KeySigMode::Ionian);
    expectStructurallyValid(results);
    SUCCEED() << "no crash on a chromatic cluster";
}

TEST(Composing_AnalyzeChordRobustness, WholeToneCluster_NoCrashValidResult)
{
    const auto results = analyzeWithGates(kAnalyzer, tones({ 60, 62, 64, 66, 68, 70 }), 0,
                                          KeySigMode::Ionian);
    expectStructurallyValid(results);
    SUCCEED() << "no crash on a whole-tone cluster";
}

// ── Out-of-range key signature -> no crash, valid result (criterion 2) ───────

TEST(Composing_AnalyzeChordRobustness, OutOfRangeKeyFifths_NoCrash)
{
    // ±100 fifths is far outside the legal -7..+7 range; a C major triad must still
    // analyze without crashing and stay structurally valid.
    for (int fifths : { 100, -100, 64, -64 }) {
        const auto results = analyzeWithGates(kAnalyzer, tones({ 60, 64, 67 }), fifths,
                                              KeySigMode::Ionian);
        expectStructurallyValid(results);
    }
    SUCCEED() << "no crash on out-of-range key signatures";
}

// ── Absent / invalid TPC -> no crash, valid result (criterion 2) ─────────────

TEST(Composing_AnalyzeChordRobustness, AbsentTpc_AnalyzesNormally)
{
    // tpc == -1 (no spelling data) is the common status-bar path; a plain C major
    // triad with no TPC must still analyze to a non-empty, valid result.
    const auto results = analyzeWithGates(kAnalyzer,
                                          tonesTpc({ { 60, -1 }, { 64, -1 }, { 67, -1 } }),
                                          0, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    expectStructurallyValid(results);
}

TEST(Composing_AnalyzeChordRobustness, InvalidTpcValues_NoCrash)
{
    // TPC out of the legal 0..34 range (garbage spelling data) must not crash the
    // spelling-aware code paths.
    const auto results = analyzeWithGates(kAnalyzer,
                                          tonesTpc({ { 60, 999 }, { 64, -50 }, { 67, 12345 } }),
                                          0, KeySigMode::Ionian);
    expectStructurallyValid(results);
    SUCCEED() << "no crash on invalid TPC values";
}

TEST(Composing_AnalyzeChordRobustness, ExtremeMidiPitches_NoCrash)
{
    // The full legal MIDI span plus the theoretical extremes.
    const auto results = analyzeWithGates(kAnalyzer, tones({ 0, 64, 127 }), 0, KeySigMode::Ionian);
    expectStructurallyValid(results);
    SUCCEED() << "no crash on extreme MIDI pitches";
}
