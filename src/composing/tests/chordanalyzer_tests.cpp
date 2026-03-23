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

#include <gtest/gtest.h>

#include "composing/analysis/chordanalyzer.h"

using namespace mu::composing::analysis;

namespace {

std::vector<ChordAnalysisTone> tones(std::initializer_list<int> pitches)
{
    std::vector<ChordAnalysisTone> out;
    out.reserve(pitches.size());

    bool first = true;
    for (int p : pitches) {
        ChordAnalysisTone t;
        t.pitch  = p;
        t.weight = 1.0;
        t.isBass = first;
        out.push_back(t);
        first = false;
    }

    return out;
}

ChordAnalysisResult makeRomanResult(int degree, ChordQuality quality,
                                    int rootPc = 0, int bassPc = 0,
                                    bool hasMin7 = false, bool hasMaj7 = false,
                                    bool hasDim7 = false, bool hasAdd6 = false)
{
    ChordAnalysisResult r;
    r.degree               = degree;
    r.quality              = quality;
    r.rootPc               = rootPc;
    r.bassPc               = bassPc;
    r.hasMinorSeventh      = hasMin7;
    r.hasMajorSeventh      = hasMaj7;
    r.hasDiminishedSeventh = hasDim7;
    r.hasAddedSixth        = hasAdd6;
    return r;
}

} // namespace

TEST(Composing_ChordAnalyzerTests, DetectsMajorTriadInCMajor)
{
    const auto results = ChordAnalyzer::analyzeChord(tones({ 60, 64, 67 }), 0, true);

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(results.front(), 0), "C");
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(results.front(), true), "I");
}

TEST(Composing_ChordAnalyzerTests, DetectsMinorTriadInCMinor)
{
    const auto results = ChordAnalyzer::analyzeChord(tones({ 60, 63, 67 }), -3, false);

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(results.front(), -3), "Cm");
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(results.front(), false), "i");
}

TEST(Composing_ChordAnalyzerTests, DetectsMinorSeventhQuality)
{
    const auto results = ChordAnalyzer::analyzeChord(tones({ 64, 67, 71, 74 }), 0, true);

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(results.front(), 0), "Em7");
    EXPECT_EQ(results.front().quality, ChordQuality::Minor);
    EXPECT_TRUE(results.front().hasMinorSeventh);
}

TEST(Composing_ChordAnalyzerTests, KeepsFlatBassSpellingInFlatKey)
{
    // Eb major triad in first inversion: Bb(70) Eb(75) G(79)
    const auto results = ChordAnalyzer::analyzeChord(tones({ 70, 75, 79 }), -3, false);

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(results.front(), -3), "Eb/Bb");
}

TEST(Composing_ChordAnalyzerTests, DetectsDiminishedSeventh)
{
    // Fully diminished seventh: B D F Ab = {11, 2, 5, 8}
    const auto results = ChordAnalyzer::analyzeChord(tones({ 59, 62, 65, 68 }), 0, true);

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().quality, ChordQuality::Diminished);
    EXPECT_TRUE(results.front().hasDiminishedSeventh);
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(results.front(), 0), "Bdim7");
}

TEST(Composing_ChordAnalyzerTests, DetectsHalfDiminished)
{
    // Half-diminished (m7b5): B D F A = {11, 2, 5, 9}
    const auto results = ChordAnalyzer::analyzeChord(tones({ 59, 62, 65, 69 }), 0, true);

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().quality, ChordQuality::HalfDiminished);
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(results.front(), 0), "Bm7b5");
}

TEST(Composing_ChordAnalyzerTests, ReturnsEmptyForFewerThanThreeDistinctPitchClasses)
{
    // Two-note interval — insufficient for chord analysis.
    const auto results = ChordAnalyzer::analyzeChord(tones({ 60, 64 }), 0, true);
    EXPECT_TRUE(results.empty());
}

// ── Context / resolution-bias tests ──────────────────────────────────────────
//
// The resolution biases in ChordTemporalContext are small (+0.35) and do not
// override bass-note evidence (+0.65).  These tests verify that the bias is
// wired correctly and raises the contextually expected candidate's score, while
// confirming no regression on the winner itself.

TEST(Composing_ChordAnalyzerTests, DimResolution_BoostsScoreOfLeadingToneTarget)
{
    // viio → I: after B diminished the resolution target is C major (one semitone up).
    // Verify the C major score is higher with context than without.
    const auto withoutCtx = ChordAnalyzer::analyzeChord(tones({ 60, 64, 67 }), 0, true);

    ChordTemporalContext ctx;
    ctx.previousRootPc  = 11;   // B
    ctx.previousQuality = ChordQuality::Diminished;
    const auto withCtx = ChordAnalyzer::analyzeChord(tones({ 60, 64, 67 }), 0, true, &ctx);

    ASSERT_FALSE(withCtx.empty());
    EXPECT_EQ(withCtx.front().rootPc, 0);
    EXPECT_EQ(withCtx.front().quality, ChordQuality::Major);
    // The resolution bias must have increased the winning candidate's score.
    EXPECT_GT(withCtx.front().score, withoutCtx.front().score);
}

TEST(Composing_ChordAnalyzerTests, HalfDimResolution_BoostsScoreOfDominantTarget)
{
    // ii∅ → V: after Bm7b5 (root 11) the resolution target is E major (a perfect fourth up).
    // Key: A minor — E is the diatonic dominant.
    const auto withoutCtx = ChordAnalyzer::analyzeChord(tones({ 64, 68, 71 }), 0, false);

    ChordTemporalContext ctx;
    ctx.previousRootPc  = 11;   // B
    ctx.previousQuality = ChordQuality::HalfDiminished;
    const auto withCtx = ChordAnalyzer::analyzeChord(tones({ 64, 68, 71 }), 0, false, &ctx);

    ASSERT_FALSE(withCtx.empty());
    EXPECT_EQ(withCtx.front().rootPc, 4);   // E
    EXPECT_EQ(withCtx.front().quality, ChordQuality::Major);
    EXPECT_GT(withCtx.front().score, withoutCtx.front().score);
}

TEST(Composing_ChordAnalyzerTests, AugResolution_BoostsScoreOfSameRootReturn)
{
    // I+ → I: after C augmented the resolution target is C major at the same root.
    const auto withoutCtx = ChordAnalyzer::analyzeChord(tones({ 60, 64, 67 }), 0, true);

    ChordTemporalContext ctx;
    ctx.previousRootPc  = 0;    // C
    ctx.previousQuality = ChordQuality::Augmented;
    const auto withCtx = ChordAnalyzer::analyzeChord(tones({ 60, 64, 67 }), 0, true, &ctx);

    ASSERT_FALSE(withCtx.empty());
    EXPECT_EQ(withCtx.front().rootPc, 0);
    EXPECT_EQ(withCtx.front().quality, ChordQuality::Major);
    EXPECT_GT(withCtx.front().score, withoutCtx.front().score);
}

// ── Roman Numeral Formatter Tests ─────────────────────────────────────────────
//
// Direct unit tests for ChordSymbolFormatter::formatRomanNumeral.  All seven
// diatonic degrees, major/minor qualities, 7th extensions, inversions,
// augmented, suspended, and the non-diatonic guard are covered.
//
// ChordAnalysisResult objects are constructed manually via makeRomanResult() so
// these tests are fully decoupled from the chord analysis algorithm.

// ── Major-key triads ──────────────────────────────────────────────────────────

TEST(Composing_ChordRomanNumeralTests, MajorKey_I)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(0, ChordQuality::Major), true), "I");
}

TEST(Composing_ChordRomanNumeralTests, MajorKey_ii)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(1, ChordQuality::Minor), true), "ii");
}

TEST(Composing_ChordRomanNumeralTests, MajorKey_iii)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(2, ChordQuality::Minor), true), "iii");
}

TEST(Composing_ChordRomanNumeralTests, MajorKey_IV)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(3, ChordQuality::Major), true), "IV");
}

TEST(Composing_ChordRomanNumeralTests, MajorKey_V)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(4, ChordQuality::Major), true), "V");
}

TEST(Composing_ChordRomanNumeralTests, MajorKey_vi)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(5, ChordQuality::Minor), true), "vi");
}

TEST(Composing_ChordRomanNumeralTests, MajorKey_viio)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(6, ChordQuality::Diminished), true), "viio");
}

// ── Major-key 7th chords ──────────────────────────────────────────────────────

TEST(Composing_ChordRomanNumeralTests, MajorKey_IM7)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(0, ChordQuality::Major, 0, 0, false, true), true), "IM7");
}

TEST(Composing_ChordRomanNumeralTests, MajorKey_ii7)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(1, ChordQuality::Minor, 0, 0, true), true), "ii7");
}

TEST(Composing_ChordRomanNumeralTests, MajorKey_iii7)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(2, ChordQuality::Minor, 0, 0, true), true), "iii7");
}

TEST(Composing_ChordRomanNumeralTests, MajorKey_IVM7)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(3, ChordQuality::Major, 0, 0, false, true), true), "IVM7");
}

TEST(Composing_ChordRomanNumeralTests, MajorKey_V7)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(4, ChordQuality::Major, 0, 0, true), true), "V7");
}

TEST(Composing_ChordRomanNumeralTests, MajorKey_vi7)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(5, ChordQuality::Minor, 0, 0, true), true), "vi7");
}

TEST(Composing_ChordRomanNumeralTests, MajorKey_viiHalfDim7)
{
    // viiø7 in major — half-diminished seventh built on the leading tone.
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(6, ChordQuality::HalfDiminished), true), "vii\xc3\xb8" "7");
}

// ── Minor-key triads ──────────────────────────────────────────────────────────

TEST(Composing_ChordRomanNumeralTests, MinorKey_i)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(0, ChordQuality::Minor), false), "i");
}

TEST(Composing_ChordRomanNumeralTests, MinorKey_iio)
{
    // Supertonic diminished triad diatonic to natural minor.
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(1, ChordQuality::Diminished), false), "iio");
}

TEST(Composing_ChordRomanNumeralTests, MinorKey_III)
{
    // Mediant major triad — the relative major.
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(2, ChordQuality::Major), false), "III");
}

TEST(Composing_ChordRomanNumeralTests, MinorKey_iv)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(3, ChordQuality::Minor), false), "iv");
}

TEST(Composing_ChordRomanNumeralTests, MinorKey_V)
{
    // Dominant major triad from harmonic minor (raised 7th scale degree).
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(4, ChordQuality::Major), false), "V");
}

TEST(Composing_ChordRomanNumeralTests, MinorKey_VI)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(5, ChordQuality::Major), false), "VI");
}

TEST(Composing_ChordRomanNumeralTests, MinorKey_viio)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(6, ChordQuality::Diminished), false), "viio");
}

// ── Minor-key 7th chords ──────────────────────────────────────────────────────

TEST(Composing_ChordRomanNumeralTests, MinorKey_i7)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(0, ChordQuality::Minor, 0, 0, true), false), "i7");
}

TEST(Composing_ChordRomanNumeralTests, MinorKey_iiHalfDim7)
{
    // iiø7 — diatonic half-diminished built on supertonic of natural minor.
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(1, ChordQuality::HalfDiminished), false), "ii\xc3\xb8" "7");
}

TEST(Composing_ChordRomanNumeralTests, MinorKey_IIIM7)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(2, ChordQuality::Major, 0, 0, false, true), false), "IIIM7");
}

TEST(Composing_ChordRomanNumeralTests, MinorKey_iv7)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(3, ChordQuality::Minor, 0, 0, true), false), "iv7");
}

TEST(Composing_ChordRomanNumeralTests, MinorKey_V7)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(4, ChordQuality::Major, 0, 0, true), false), "V7");
}

TEST(Composing_ChordRomanNumeralTests, MinorKey_VIM7)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(5, ChordQuality::Major, 0, 0, false, true), false), "VIM7");
}

TEST(Composing_ChordRomanNumeralTests, MinorKey_viiFullDim7)
{
    // viio7 — fully diminished seventh from harmonic minor.
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(6, ChordQuality::Diminished, 0, 0, false, false, true), false), "viio7");
}

// ── Augmented chords ──────────────────────────────────────────────────────────

TEST(Composing_ChordRomanNumeralTests, AugmentedTriad_I_plus)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(0, ChordQuality::Augmented), true), "I+");
}

TEST(Composing_ChordRomanNumeralTests, AugmentedDominantSeventh_I_plus_7)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(0, ChordQuality::Augmented, 0, 0, true), true), "I+7");
}

TEST(Composing_ChordRomanNumeralTests, AugmentedMajorSeventh_I_plus_M7)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(0, ChordQuality::Augmented, 0, 0, false, true), true), "I+M7");
}

// ── Suspended chords ──────────────────────────────────────────────────────────

TEST(Composing_ChordRomanNumeralTests, SuspendedFour_Isus4)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(0, ChordQuality::Suspended4), true), "Isus4");
}

TEST(Composing_ChordRomanNumeralTests, SuspendedTwo_Isus2)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(0, ChordQuality::Suspended2), true), "Isus2");
}

TEST(Composing_ChordRomanNumeralTests, SuspendedFour_Vsus4)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(4, ChordQuality::Suspended4), true), "Vsus4");
}

// ── HalfDiminished at various degrees ────────────────────────────────────────

TEST(Composing_ChordRomanNumeralTests, HalfDim_ii_inMajor)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(1, ChordQuality::HalfDiminished), true), "ii\xc3\xb8" "7");
}

TEST(Composing_ChordRomanNumeralTests, HalfDim_iv_inMinor)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(3, ChordQuality::HalfDiminished), false), "iv\xc3\xb8" "7");
}

// ── Non-diatonic guard ────────────────────────────────────────────────────────

TEST(Composing_ChordRomanNumeralTests, NonDiatonic_ReturnsEmpty)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(-1, ChordQuality::Major), true), "");
}

// ── Triad inversions ──────────────────────────────────────────────────────────

TEST(Composing_ChordRomanNumeralTests, MajorTriad_FirstInversion_I6)
{
    // I6: bass = major third above root.  rootPc=0 (C), bassPc=4 (E).
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(0, ChordQuality::Major, 0, 4), true), "I6");
}

TEST(Composing_ChordRomanNumeralTests, MajorTriad_SecondInversion_I64)
{
    // I64: bass = fifth above root.  rootPc=0 (C), bassPc=7 (G).
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(0, ChordQuality::Major, 0, 7), true), "I64");
}

TEST(Composing_ChordRomanNumeralTests, MinorTriad_FirstInversion_i6)
{
    // i6: bass = minor third above root.  rootPc=0 (C), bassPc=3 (Eb).
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(0, ChordQuality::Minor, 0, 3), false), "i6");
}

TEST(Composing_ChordRomanNumeralTests, DiminishedTriad_FirstInversion_viio6)
{
    // viio6: bass = minor third above root.  rootPc=11 (B), bassPc=2 (D).
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(6, ChordQuality::Diminished, 11, 2), true), "viio6");
}

// ── Seventh-chord inversions ──────────────────────────────────────────────────

TEST(Composing_ChordRomanNumeralTests, DominantSeventh_FirstInversion_V65)
{
    // V65: bass = major third above root.  rootPc=7 (G), bassPc=11 (B).
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(4, ChordQuality::Major, 7, 11, true), true), "V65");
}

TEST(Composing_ChordRomanNumeralTests, DominantSeventh_SecondInversion_V43)
{
    // V43: bass = fifth above root.  rootPc=7 (G), bassPc=2 (D).
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(4, ChordQuality::Major, 7, 2, true), true), "V43");
}

TEST(Composing_ChordRomanNumeralTests, DominantSeventh_ThirdInversion_V42)
{
    // V42: bass = minor seventh above root.  rootPc=7 (G), bassPc=5 (F).
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(4, ChordQuality::Major, 7, 5, true), true), "V42");
}

TEST(Composing_ChordRomanNumeralTests, MajorSeventh_FirstInversion_IM65)
{
    // IM65: bass = major third above root.  rootPc=0 (C), bassPc=4 (E).
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(0, ChordQuality::Major, 0, 4, false, true), true), "I65");
}

TEST(Composing_ChordRomanNumeralTests, HalfDim_FirstInversion_viiHalfDim65)
{
    // viiø65: bass = minor third above root.  rootPc=11 (B), bassPc=2 (D).
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(6, ChordQuality::HalfDiminished, 11, 2), true),
              "vii\xc3\xb8" "65");
}

TEST(Composing_ChordRomanNumeralTests, FullDim7_FirstInversion_viio65)
{
    // viio65: bass = minor third above root.  rootPc=11 (B), bassPc=2 (D).
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(6, ChordQuality::Diminished, 11, 2, false, false, true), true),
              "viio65");
}

// ── Added-sixth chords ────────────────────────────────────────────────────────
//
// I6 = first inversion of I (figured bass).
// I(add6) = tonic with added major sixth — structurally different; the 6th is
// not an inversion tone.  The Roman numeral must not conflate the two.

TEST(Composing_ChordRomanNumeralTests, MajorAdd6_I_add6)
{
    // C6 (C E G A) in root position — no 9th, so pure add6.
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(0, ChordQuality::Major, 0, 0, false, false, false, true), true),
              "I(add6)");
}

TEST(Composing_ChordRomanNumeralTests, MajorSixNine_I69)
{
    // C69 (C D E G A) — both add6 and add9 present → "I69" not "I(add6)".
    ChordAnalysisResult r = makeRomanResult(0, ChordQuality::Major, 0, 0, false, false, false, true);
    r.hasNinth = true;
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r, true), "I69");
}

TEST(Composing_ChordRomanNumeralTests, MinorSixNine_i69)
{
    // Cm69 — minor 6/9 chord.
    ChordAnalysisResult r = makeRomanResult(0, ChordQuality::Minor, 0, 0, false, false, false, true);
    r.hasNinth = true;
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r, false), "i69");
}

TEST(Composing_ChordRomanNumeralTests, MinorAdd6_i_add6)
{
    // Cm6 (C Eb G A) in root position.
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(0, ChordQuality::Minor, 0, 0, false, false, false, true), false),
              "i(add6)");
}

TEST(Composing_ChordRomanNumeralTests, MajorAdd6_IV_add6)
{
    // F6 in C major — IV(add6).
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(3, ChordQuality::Major, 0, 0, false, false, false, true), true),
              "IV(add6)");
}

TEST(Composing_ChordRomanNumeralTests, MajorAdd6_VI_add6_inMinor)
{
    // VI(add6) in minor.
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(5, ChordQuality::Major, 0, 0, false, false, false, true), false),
              "VI(add6)");
}

TEST(Composing_ChordRomanNumeralTests, MajorFirstInversion_I6_isNotAdd6)
{
    // I6 = first inversion (E in bass), NOT an added-sixth chord.
    // Confirming no "(add6)" appears when hasAddedSixth is false.
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(0, ChordQuality::Major, 0, 4), true), "I6");
}
