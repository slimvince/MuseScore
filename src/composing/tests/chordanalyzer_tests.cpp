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

#include "composing/analysis/chord/chordanalyzer.h"

#include "test_helpers.h"

using namespace mu::composing::analysis;

namespace {

const RuleBasedChordAnalyzer kAnalyzer{};

/// Build tones with explicit TPC data using the test TPC encoding:
/// F=14, C=15, G=16, D=17, A=18, E=19, B=20; each flat -7, each sharp +7.
/// So Ab=11, Gb=9, Db=10, Eb=12, Bb=13.  -1 = no TPC data.
std::vector<ChordAnalysisTone> tonesWithTpc(std::initializer_list<std::pair<int,int>> pitchTpcPairs)
{
    std::vector<ChordAnalysisTone> out;
    out.reserve(pitchTpcPairs.size());

    bool first = true;
    for (const auto& pt : pitchTpcPairs) {
        ChordAnalysisTone t;
        t.pitch  = pt.first;
        t.tpc    = pt.second;
        t.weight = 1.0;
        t.isBass = first;
        out.push_back(t);
        first = false;
    }

    return out;
}

ChordAnalyzerPreferences bassSupportPrefs()
{
    ChordAnalyzerPreferences prefs;
    prefs.bassNoteRootBonus = 1.0;
    prefs.bassRootThirdOnlyMultiplier = 0.3;
    prefs.bassRootAloneMultiplier = 0.1;
    return prefs;
}

/// Build tones with individual pitch/weight pairs.
/// The first tone is flagged isBass=true; bass detection in the analyzer
/// uses lowest pitch, so list pitches in ascending order if the first
/// entry should genuinely be the bass.
std::vector<ChordAnalysisTone> weightedTones(std::initializer_list<std::pair<int, double>> pitchWeightPairs)
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

TEST(Composing_ChordAnalyzerTests, DetectsMajorTriadInCMajor)
{
    const auto results = kAnalyzer.analyzeChord(tones({ 60, 64, 67 }), 0, KeySigMode::Ionian);

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(results.front(), 0), "C");
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(results.front()), "I");
}

TEST(Composing_ChordAnalyzerTests, DetectsMinorTriadInCMinor)
{
    const auto results = kAnalyzer.analyzeChord(tones({ 60, 63, 67 }), -3, KeySigMode::Aeolian);

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(results.front(), -3), "Cm");
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(results.front()), "i");
}

TEST(Composing_ChordAnalyzerTests, DetectsMinorSeventhQuality)
{
    const auto results = kAnalyzer.analyzeChord(tones({ 64, 67, 71, 74 }), 0, KeySigMode::Ionian);

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(results.front(), 0), "Em7");
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Minor);
    EXPECT_TRUE(hasExtension(results.front().identity.extensions, Extension::MinorSeventh));
}

TEST(Composing_ChordAnalyzerTests, KeepsFlatBassSpellingInFlatKey)
{
    // Eb major triad in first inversion: Bb(70) Eb(75) G(79)
    const auto results = kAnalyzer.analyzeChord(tones({ 70, 75, 79 }), -3, KeySigMode::Aeolian);

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(results.front(), -3), "Eb/Bb");
}

TEST(Composing_ChordAnalyzerTests, DetectsDiminishedSeventh)
{
    // Fully diminished seventh: B D F Ab = {11, 2, 5, 8}
    const auto results = kAnalyzer.analyzeChord(tones({ 59, 62, 65, 68 }), 0, KeySigMode::Ionian);

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Diminished);
    EXPECT_TRUE(hasExtension(results.front().identity.extensions, Extension::DiminishedSeventh));
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(results.front(), 0), "Bdim7");
}

TEST(Composing_ChordAnalyzerTests, DetectsHalfDiminished)
{
    // Half-diminished (m7b5): B D F A = {11, 2, 5, 9}
    const auto results = kAnalyzer.analyzeChord(tones({ 59, 62, 65, 69 }), 0, KeySigMode::Ionian);

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.quality, ChordQuality::HalfDiminished);
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(results.front(), 0), "Bm7b5");
}

TEST(Composing_ChordAnalyzerTests, FullyDiminishedNotMisreadAsHalfDiminished)
{
    // {B,D,F,Ab}: dim7 interval (9 semitones) distinguishes fully dim from half-dim.
    // Must be Diminished+DiminishedSeventh (B°7), never HalfDiminished (Bø7).
    const auto results = kAnalyzer.analyzeChord(tones({ 59, 62, 65, 68 }), 0, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Diminished)
        << "B,D,F,Ab must be Diminished, not HalfDiminished";
    EXPECT_NE(results.front().identity.quality, ChordQuality::HalfDiminished)
        << "B,D,F,Ab must not be classified as HalfDiminished";
}

TEST(Composing_ChordAnalyzerTests, HalfDiminishedNotMisreadAsFullyDiminished)
{
    // {B,D,F,A}: minor 7th (10 semitones) distinguishes half-dim from fully dim.
    // Must be HalfDiminished (Bø7), never Diminished+DiminishedSeventh (B°7).
    const auto results = kAnalyzer.analyzeChord(tones({ 59, 62, 65, 69 }), 0, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.quality, ChordQuality::HalfDiminished)
        << "B,D,F,A must be HalfDiminished, not Diminished";
    EXPECT_FALSE(hasExtension(results.front().identity.extensions, Extension::DiminishedSeventh))
        << "B,D,F,A must not have DiminishedSeventh extension";
}

TEST(Composing_ChordAnalyzerTests, ReturnsEmptyForFewerThanThreeDistinctPitchClasses)
{
    // Two-note interval — insufficient for chord analysis.
    const auto results = kAnalyzer.analyzeChord(tones({ 60, 64 }), 0, KeySigMode::Ionian);
    EXPECT_TRUE(results.empty());
}

TEST(Composing_ChordAnalyzerTests, BassRootBonusUsesFullTierWhenPerfectFifthPresent)
{
    ChordAnalyzerPreferences tieredPrefs = bassSupportPrefs();
    ChordAnalyzerPreferences noBassBonusPrefs = tieredPrefs;
    noBassBonusPrefs.bassNoteRootBonus = 0.0;

    const auto tiered = kAnalyzer.analyzeChord(tones({ 60, 64, 67 }), 0, KeySigMode::Ionian,
                                               nullptr, tieredPrefs);
    const auto noBass = kAnalyzer.analyzeChord(tones({ 60, 64, 67 }), 0, KeySigMode::Ionian,
                                               nullptr, noBassBonusPrefs);

    ASSERT_FALSE(tiered.empty());
    ASSERT_FALSE(noBass.empty());
    ASSERT_NE(findCandidate(tiered, 0, ChordQuality::Major), nullptr);
    ASSERT_NE(findCandidate(noBass, 0, ChordQuality::Major), nullptr);

    const double tieredScore = findCandidate(tiered, 0, ChordQuality::Major)->identity.score;
    const double noBassScore = findCandidate(noBass, 0, ChordQuality::Major)->identity.score;
    EXPECT_NEAR(tieredScore - noBassScore, 1.0, 1e-9);
}

TEST(Composing_ChordAnalyzerTests, BassRootBonusUsesFullTierWhenCandidateHasAlteredFifth)
{
    ChordAnalyzerPreferences tieredPrefs = bassSupportPrefs();
    ChordAnalyzerPreferences noBassBonusPrefs = tieredPrefs;
    noBassBonusPrefs.bassNoteRootBonus = 0.0;

    const auto tiered = kAnalyzer.analyzeChord(tones({ 60, 64, 68, 70 }), 0, KeySigMode::Ionian,
                                               nullptr, tieredPrefs);
    const auto noBass = kAnalyzer.analyzeChord(tones({ 60, 64, 68, 70 }), 0, KeySigMode::Ionian,
                                               nullptr, noBassBonusPrefs);

    ASSERT_FALSE(tiered.empty());
    ASSERT_FALSE(noBass.empty());
    ASSERT_NE(findCandidate(tiered, 0, ChordQuality::Augmented), nullptr);
    ASSERT_NE(findCandidate(noBass, 0, ChordQuality::Augmented), nullptr);

    const double tieredScore = findCandidate(tiered, 0, ChordQuality::Augmented)->identity.score;
    const double noBassScore = findCandidate(noBass, 0, ChordQuality::Augmented)->identity.score;
    EXPECT_NEAR(tieredScore - noBassScore, 1.0, 1e-9);
}

TEST(Composing_ChordAnalyzerTests, BassRootBonusUsesThirdOnlyTierWithoutFifth)
{
    ChordAnalyzerPreferences tieredPrefs = bassSupportPrefs();
    ChordAnalyzerPreferences noBassBonusPrefs = tieredPrefs;
    noBassBonusPrefs.bassNoteRootBonus = 0.0;

    const auto tiered = kAnalyzer.analyzeChord(tones({ 60, 64, 70 }), 0, KeySigMode::Ionian,
                                               nullptr, tieredPrefs);
    const auto noBass = kAnalyzer.analyzeChord(tones({ 60, 64, 70 }), 0, KeySigMode::Ionian,
                                               nullptr, noBassBonusPrefs);

    ASSERT_FALSE(tiered.empty());
    ASSERT_FALSE(noBass.empty());
    ASSERT_NE(findCandidate(tiered, 0, ChordQuality::Major), nullptr);
    ASSERT_NE(findCandidate(noBass, 0, ChordQuality::Major), nullptr);

    const double tieredScore = findCandidate(tiered, 0, ChordQuality::Major)->identity.score;
    const double noBassScore = findCandidate(noBass, 0, ChordQuality::Major)->identity.score;
    EXPECT_NEAR(tieredScore - noBassScore, 0.3, 1e-9);
}

TEST(Composing_ChordAnalyzerTests, BassRootBonusUsesAloneTierWithoutThirdOrFifth)
{
    ChordAnalyzerPreferences tieredPrefs = bassSupportPrefs();
    ChordAnalyzerPreferences noBassBonusPrefs = tieredPrefs;
    noBassBonusPrefs.bassNoteRootBonus = 0.0;

    const auto tiered = kAnalyzer.analyzeChord(tones({ 60, 65, 70 }), 0, KeySigMode::Ionian,
                                               nullptr, tieredPrefs);
    const auto noBass = kAnalyzer.analyzeChord(tones({ 60, 65, 70 }), 0, KeySigMode::Ionian,
                                               nullptr, noBassBonusPrefs);

    ASSERT_FALSE(tiered.empty());
    ASSERT_FALSE(noBass.empty());
    ASSERT_NE(findCandidate(tiered, 0, ChordQuality::Suspended4), nullptr);
    ASSERT_NE(findCandidate(noBass, 0, ChordQuality::Suspended4), nullptr);

    const double tieredScore = findCandidate(tiered, 0, ChordQuality::Suspended4)->identity.score;
    const double noBassScore = findCandidate(noBass, 0, ChordQuality::Suspended4)->identity.score;
    EXPECT_NEAR(tieredScore - noBassScore, 0.1, 1e-9);
}

TEST(Composing_ChordAnalyzerTests, BareSuspensionTriadDoesNotUseFullBassRootTier)
{
    ChordAnalyzerPreferences tieredPrefs = bassSupportPrefs();
    ChordAnalyzerPreferences noBassBonusPrefs = tieredPrefs;
    noBassBonusPrefs.bassNoteRootBonus = 0.0;

    const auto tiered = kAnalyzer.analyzeChord(tones({ 60, 62, 67 }), 0, KeySigMode::Ionian,
                                               nullptr, tieredPrefs);
    const auto noBass = kAnalyzer.analyzeChord(tones({ 60, 62, 67 }), 0, KeySigMode::Ionian,
                                               nullptr, noBassBonusPrefs);

    ASSERT_FALSE(tiered.empty());
    ASSERT_FALSE(noBass.empty());
    ASSERT_NE(findCandidate(tiered, 0, ChordQuality::Suspended2), nullptr);
    ASSERT_NE(findCandidate(noBass, 0, ChordQuality::Suspended2), nullptr);

    const double tieredScore = findCandidate(tiered, 0, ChordQuality::Suspended2)->identity.score;
    const double noBassScore = findCandidate(noBass, 0, ChordQuality::Suspended2)->identity.score;
    EXPECT_NEAR(tieredScore - noBassScore, 0.3, 1e-9);
}

TEST(Composing_ChordAnalyzerTests, BoundsExposeBassRootSupportMultipliers)
{
    const ParameterBoundsMap bounds = ChordAnalyzerPreferences{}.bounds();

    const auto thirdOnly = bounds.find("bassRootThirdOnlyMultiplier");
    ASSERT_NE(thirdOnly, bounds.end());
    EXPECT_DOUBLE_EQ(thirdOnly->second.min, 0.0);
    EXPECT_DOUBLE_EQ(thirdOnly->second.max, 1.0);

    const auto bassAlone = bounds.find("bassRootAloneMultiplier");
    ASSERT_NE(bassAlone, bounds.end());
    EXPECT_DOUBLE_EQ(bassAlone->second.min, 0.0);
    EXPECT_DOUBLE_EQ(bassAlone->second.max, 1.0);
}

TEST(Composing_ChordAnalyzerTests, StepwiseBassEvidenceFavorsCompleteMajorFirstInversionTriad)
{
    const auto withoutCtx = kAnalyzer.analyzeChord(tones({ 60, 63, 68 }), 0, KeySigMode::Ionian);
    ASSERT_FALSE(withoutCtx.empty());
    const ChordAnalysisResult* withoutCtxCandidate = findCandidate(withoutCtx, 8, ChordQuality::Major);
    ASSERT_NE(withoutCtxCandidate, nullptr);

    ChordTemporalContext ctx;
    ctx.bassIsStepwiseFromPrevious = true;
    const auto withCtx = kAnalyzer.analyzeChord(tones({ 60, 63, 68 }), 0, KeySigMode::Ionian, &ctx);

    ASSERT_FALSE(withCtx.empty());
    const ChordAnalysisResult* withCtxCandidate = findCandidate(withCtx, 8, ChordQuality::Major);
    ASSERT_NE(withCtxCandidate, nullptr);
    EXPECT_GT(withCtxCandidate->identity.score, withoutCtxCandidate->identity.score);
    EXPECT_EQ(withCtx.front().identity.rootPc, 8);
    EXPECT_EQ(withCtx.front().identity.bassPc, 0);
    EXPECT_EQ(withCtx.front().identity.quality, ChordQuality::Major);
}

TEST(Composing_ChordAnalyzerTests, StepwiseBassEvidenceFavorsCompleteMinorFirstInversionTriad)
{
    ChordTemporalContext ctx;
    ctx.bassIsStepwiseFromPrevious = true;
    const auto results = kAnalyzer.analyzeChord(tones({ 56, 60, 65 }), 0, KeySigMode::Ionian, &ctx);

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 5);
    EXPECT_EQ(results.front().identity.bassPc, 8);
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Minor);
}

TEST(Composing_ChordAnalyzerTests, StepwiseLookaheadFavorsCompleteMajorFirstInversionTriad)
{
    const auto withoutCtx = kAnalyzer.analyzeChord(tones({ 60, 63, 68 }), 0, KeySigMode::Ionian);
    ASSERT_FALSE(withoutCtx.empty());
    const ChordAnalysisResult* withoutCtxCandidate = findCandidate(withoutCtx, 8, ChordQuality::Major);
    ASSERT_NE(withoutCtxCandidate, nullptr);

    ChordTemporalContext ctx;
    ctx.bassIsStepwiseToNext = true;
    const auto withCtx = kAnalyzer.analyzeChord(tones({ 60, 63, 68 }), 0, KeySigMode::Ionian, &ctx);

    ASSERT_FALSE(withCtx.empty());
    const ChordAnalysisResult* withCtxCandidate = findCandidate(withCtx, 8, ChordQuality::Major);
    ASSERT_NE(withCtxCandidate, nullptr);
    EXPECT_GT(withCtxCandidate->identity.score, withoutCtxCandidate->identity.score);
    EXPECT_EQ(withCtx.front().identity.rootPc, 8);
    EXPECT_EQ(withCtx.front().identity.bassPc, 0);
    EXPECT_EQ(withCtx.front().identity.quality, ChordQuality::Major);
}

TEST(Composing_ChordAnalyzerTests, CorelliWeightedPassingBassPrefersTonicFirstInversion)
{
    ChordTemporalContext ctx;
    ctx.previousRootPc = 5;
    ctx.previousQuality = ChordQuality::Minor;
    ctx.bassIsStepwiseFromPrevious = true;
    ctx.bassIsStepwiseToNext = true;

    const std::vector<ChordAnalysisTone> regionTones = {
        { 51, -1, 1.283, true },
        { 60, -1, 0.606, false },
        { 62, -1, 0.045, false },
        { 65, -1, 0.066, false },
    };

    const auto results = kAnalyzer.analyzeChord(regionTones, -3, KeySigMode::Aeolian, &ctx);

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 0);
    EXPECT_EQ(results.front().identity.bassPc, 3);
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Minor);
}

// ── Degree assignment in non-Ionian/Aeolian modes ────────────────────────────
//
// These tests verify that ChordAnalyzer::analyzeChord assigns the correct
// diatonic degree when the key mode is Dorian, Phrygian, Lydian, Mixolydian,
// or Locrian.  All use keySig=0 (sharing C major's pitch-class set) with
// the appropriate KeySigMode.

TEST(Composing_ChordAnalyzerTests, DegreeAssignment_DDorian_TonicChord)
{
    // D minor triad in D Dorian → degree 0 (i).
    const auto results = kAnalyzer.analyzeChord(tones({ 62, 65, 69 }), 0, KeySigMode::Dorian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 2);    // D
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Minor);
    EXPECT_EQ(results.front().function.degree, 0);
    EXPECT_TRUE(results.front().function.diatonicToKey);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(results.front()), "i");
}

TEST(Composing_ChordAnalyzerTests, DegreeAssignment_DDorian_IVChord)
{
    // G major triad in D Dorian → degree 3 (IV).
    const auto results = kAnalyzer.analyzeChord(tones({ 67, 71, 74 }), 0, KeySigMode::Dorian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 7);    // G
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Major);
    EXPECT_EQ(results.front().function.degree, 3);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(results.front()), "IV");
}

TEST(Composing_ChordAnalyzerTests, DegreeAssignment_EPhrygian_TonicChord)
{
    // E minor triad in E Phrygian → degree 0 (i).
    const auto results = kAnalyzer.analyzeChord(tones({ 64, 67, 71 }), 0, KeySigMode::Phrygian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 4);    // E
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Minor);
    EXPECT_EQ(results.front().function.degree, 0);
    EXPECT_TRUE(results.front().function.diatonicToKey);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(results.front()), "i");
}

TEST(Composing_ChordAnalyzerTests, DegreeAssignment_EPhrygian_FlatIIChord)
{
    // F major triad in E Phrygian → degree 1 (II, the Phrygian bII).
    const auto results = kAnalyzer.analyzeChord(tones({ 65, 69, 72 }), 0, KeySigMode::Phrygian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 5);    // F
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Major);
    EXPECT_EQ(results.front().function.degree, 1);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(results.front()), "II");
}

TEST(Composing_ChordAnalyzerTests, DegreeAssignment_FLydian_TonicChord)
{
    // F major triad in F Lydian → degree 0 (I).
    const auto results = kAnalyzer.analyzeChord(tones({ 65, 69, 72 }), 0, KeySigMode::Lydian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 5);    // F
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Major);
    EXPECT_EQ(results.front().function.degree, 0);
    EXPECT_TRUE(results.front().function.diatonicToKey);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(results.front()), "I");
}

TEST(Composing_ChordAnalyzerTests, DegreeAssignment_FLydian_IIChord)
{
    // G major triad in F Lydian → degree 1 (II).
    const auto results = kAnalyzer.analyzeChord(tones({ 67, 71, 74 }), 0, KeySigMode::Lydian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 7);    // G
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Major);
    EXPECT_EQ(results.front().function.degree, 1);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(results.front()), "II");
}

TEST(Composing_ChordAnalyzerTests, DegreeAssignment_GMixolydian_TonicChord)
{
    // G major triad in G Mixolydian → degree 0 (I).
    const auto results = kAnalyzer.analyzeChord(tones({ 67, 71, 74 }), 0, KeySigMode::Mixolydian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 7);    // G
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Major);
    EXPECT_EQ(results.front().function.degree, 0);
    EXPECT_TRUE(results.front().function.diatonicToKey);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(results.front()), "I");
}

TEST(Composing_ChordAnalyzerTests, DegreeAssignment_GMixolydian_FlatVIIChord)
{
    // F major triad in G Mixolydian → degree 6 (VII, the bVII).
    const auto results = kAnalyzer.analyzeChord(tones({ 65, 69, 72 }), 0, KeySigMode::Mixolydian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 5);    // F
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Major);
    EXPECT_EQ(results.front().function.degree, 6);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(results.front()), "VII");
}

TEST(Composing_ChordAnalyzerTests, DegreeAssignment_BLocrian_TonicChord)
{
    // B diminished triad in B Locrian → degree 0 (io).
    const auto results = kAnalyzer.analyzeChord(tones({ 59, 62, 65 }), 0, KeySigMode::Locrian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 11);   // B
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Diminished);
    EXPECT_EQ(results.front().function.degree, 0);
    EXPECT_TRUE(results.front().function.diatonicToKey);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(results.front()), "io");
}

TEST(Composing_ChordAnalyzerTests, DegreeAssignment_BLocrian_IIChord)
{
    // C major triad in B Locrian → degree 1 (II).
    const auto results = kAnalyzer.analyzeChord(tones({ 60, 64, 67 }), 0, KeySigMode::Locrian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 0);    // C
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Major);
    EXPECT_EQ(results.front().function.degree, 1);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(results.front()), "II");
}

TEST(Composing_ChordAnalyzerTests, DegreeAssignment_Dorian_ChromaticChordIsNonDiatonic)
{
    // F# major triad in D Dorian — F# is not in the D Dorian scale → degree = -1.
    const auto results = kAnalyzer.analyzeChord(tones({ 66, 70, 73 }), 0, KeySigMode::Dorian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().function.degree, -1);
    EXPECT_FALSE(results.front().function.diatonicToKey);
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
    const auto withoutCtx = kAnalyzer.analyzeChord(tones({ 60, 64, 67 }), 0, KeySigMode::Ionian);

    ChordTemporalContext ctx;
    ctx.previousRootPc  = 11;   // B
    ctx.previousQuality = ChordQuality::Diminished;
    const auto withCtx = kAnalyzer.analyzeChord(tones({ 60, 64, 67 }), 0, KeySigMode::Ionian, &ctx);

    ASSERT_FALSE(withCtx.empty());
    EXPECT_EQ(withCtx.front().identity.rootPc, 0);
    EXPECT_EQ(withCtx.front().identity.quality, ChordQuality::Major);
    // The resolution bias must have increased the winning candidate's score.
    EXPECT_GT(withCtx.front().identity.score, withoutCtx.front().identity.score);
}

TEST(Composing_ChordAnalyzerTests, HalfDimResolution_BoostsScoreOfDominantTarget)
{
    // ii∅ → V: after Bm7b5 (root 11) the resolution target is E major (a perfect fourth up).
    // Key: A minor — E is the diatonic dominant.
    const auto withoutCtx = kAnalyzer.analyzeChord(tones({ 64, 68, 71 }), 0, KeySigMode::Aeolian);

    ChordTemporalContext ctx;
    ctx.previousRootPc  = 11;   // B
    ctx.previousQuality = ChordQuality::HalfDiminished;
    const auto withCtx = kAnalyzer.analyzeChord(tones({ 64, 68, 71 }), 0, KeySigMode::Aeolian, &ctx);

    ASSERT_FALSE(withCtx.empty());
    EXPECT_EQ(withCtx.front().identity.rootPc, 4);   // E
    EXPECT_EQ(withCtx.front().identity.quality, ChordQuality::Major);
    EXPECT_GT(withCtx.front().identity.score, withoutCtx.front().identity.score);
}

TEST(Composing_ChordAnalyzerTests, AugResolution_BoostsScoreOfSameRootReturn)
{
    // I+ → I: after C augmented the resolution target is C major at the same root.
    const auto withoutCtx = kAnalyzer.analyzeChord(tones({ 60, 64, 67 }), 0, KeySigMode::Ionian);

    ChordTemporalContext ctx;
    ctx.previousRootPc  = 0;    // C
    ctx.previousQuality = ChordQuality::Augmented;
    const auto withCtx = kAnalyzer.analyzeChord(tones({ 60, 64, 67 }), 0, KeySigMode::Ionian, &ctx);

    ASSERT_FALSE(withCtx.empty());
    EXPECT_EQ(withCtx.front().identity.rootPc, 0);
    EXPECT_EQ(withCtx.front().identity.quality, ChordQuality::Major);
    EXPECT_GT(withCtx.front().identity.score, withoutCtx.front().identity.score);
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
                  makeRomanResult(0, ChordQuality::Major)), "I");
}

TEST(Composing_ChordRomanNumeralTests, MajorKey_ii)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(1, ChordQuality::Minor)), "ii");
}

TEST(Composing_ChordRomanNumeralTests, MajorKey_iii)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(2, ChordQuality::Minor)), "iii");
}

TEST(Composing_ChordRomanNumeralTests, MajorKey_IV)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(3, ChordQuality::Major)), "IV");
}

TEST(Composing_ChordRomanNumeralTests, MajorKey_V)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(4, ChordQuality::Major)), "V");
}

TEST(Composing_ChordRomanNumeralTests, MajorKey_vi)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(5, ChordQuality::Minor)), "vi");
}

TEST(Composing_ChordRomanNumeralTests, MajorKey_viio)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(6, ChordQuality::Diminished)), "viio");
}

// ── Major-key 7th chords ──────────────────────────────────────────────────────

TEST(Composing_ChordRomanNumeralTests, MajorKey_IM7)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(0, ChordQuality::Major, 0, 0, false, true)), "IM7");
}

TEST(Composing_ChordRomanNumeralTests, MajorKey_ii7)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(1, ChordQuality::Minor, 0, 0, true)), "ii7");
}

TEST(Composing_ChordRomanNumeralTests, MajorKey_iii7)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(2, ChordQuality::Minor, 0, 0, true)), "iii7");
}

TEST(Composing_ChordRomanNumeralTests, MajorKey_IVM7)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(3, ChordQuality::Major, 0, 0, false, true)), "IVM7");
}

TEST(Composing_ChordRomanNumeralTests, MajorKey_V7)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(4, ChordQuality::Major, 0, 0, true)), "V7");
}

TEST(Composing_ChordRomanNumeralTests, MajorKey_vi7)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(5, ChordQuality::Minor, 0, 0, true)), "vi7");
}

TEST(Composing_ChordRomanNumeralTests, MajorKey_viiHalfDim7)
{
    // viiø7 in major — half-diminished seventh built on the leading tone.
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(6, ChordQuality::HalfDiminished)), "vii\xc3\xb8" "7");
}

// ── Minor-key triads ──────────────────────────────────────────────────────────

TEST(Composing_ChordRomanNumeralTests, MinorKey_i)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(0, ChordQuality::Minor)), "i");
}

TEST(Composing_ChordRomanNumeralTests, MinorKey_iio)
{
    // Supertonic diminished triad diatonic to natural minor.
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(1, ChordQuality::Diminished)), "iio");
}

TEST(Composing_ChordRomanNumeralTests, MinorKey_III)
{
    // Mediant major triad — the relative major.
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(2, ChordQuality::Major)), "III");
}

TEST(Composing_ChordRomanNumeralTests, MinorKey_iv)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(3, ChordQuality::Minor)), "iv");
}

TEST(Composing_ChordRomanNumeralTests, MinorKey_V)
{
    // Dominant major triad from harmonic minor (raised 7th scale degree).
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(4, ChordQuality::Major)), "V");
}

TEST(Composing_ChordRomanNumeralTests, MinorKey_VI)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(5, ChordQuality::Major)), "VI");
}

TEST(Composing_ChordRomanNumeralTests, MinorKey_viio)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(6, ChordQuality::Diminished)), "viio");
}

// ── Minor-key 7th chords ──────────────────────────────────────────────────────

TEST(Composing_ChordRomanNumeralTests, MinorKey_i7)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(0, ChordQuality::Minor, 0, 0, true)), "i7");
}

TEST(Composing_ChordRomanNumeralTests, MinorKey_iiHalfDim7)
{
    // iiø7 — diatonic half-diminished built on supertonic of natural minor.
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(1, ChordQuality::HalfDiminished)), "ii\xc3\xb8" "7");
}

TEST(Composing_ChordRomanNumeralTests, MinorKey_IIIM7)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(2, ChordQuality::Major, 0, 0, false, true)), "IIIM7");
}

TEST(Composing_ChordRomanNumeralTests, MinorKey_iv7)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(3, ChordQuality::Minor, 0, 0, true)), "iv7");
}

TEST(Composing_ChordRomanNumeralTests, MinorKey_V7)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(4, ChordQuality::Major, 0, 0, true)), "V7");
}

TEST(Composing_ChordRomanNumeralTests, MinorKey_VIM7)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(5, ChordQuality::Major, 0, 0, false, true)), "VIM7");
}

TEST(Composing_ChordRomanNumeralTests, MinorKey_viiFullDim7)
{
    // viio7 — fully diminished seventh from harmonic minor.
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(6, ChordQuality::Diminished, 0, 0, false, false, true)), "viio7");
}

// ── Augmented chords ──────────────────────────────────────────────────────────

TEST(Composing_ChordRomanNumeralTests, AugmentedTriad_I_plus)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(0, ChordQuality::Augmented)), "I+");
}

TEST(Composing_ChordRomanNumeralTests, AugmentedDominantSeventh_I_plus_7)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(0, ChordQuality::Augmented, 0, 0, true)), "I+7");
}

TEST(Composing_ChordRomanNumeralTests, AugmentedMajorSeventh_I_plus_M7)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(0, ChordQuality::Augmented, 0, 0, false, true)), "I+M7");
}

// ── Suspended chords ──────────────────────────────────────────────────────────

TEST(Composing_ChordRomanNumeralTests, SuspendedFour_Isus4)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(0, ChordQuality::Suspended4)), "Isus4");
}

TEST(Composing_ChordRomanNumeralTests, SuspendedTwo_Isus2)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(0, ChordQuality::Suspended2)), "Isus2");
}

TEST(Composing_ChordRomanNumeralTests, SuspendedFour_Vsus4)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(4, ChordQuality::Suspended4)), "Vsus4");
}

// ── HalfDiminished at various degrees ────────────────────────────────────────

TEST(Composing_ChordRomanNumeralTests, HalfDim_ii_inMajor)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(1, ChordQuality::HalfDiminished)), "ii\xc3\xb8" "7");
}

TEST(Composing_ChordRomanNumeralTests, HalfDim_iv_inMinor)
{
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(3, ChordQuality::HalfDiminished)), "iv\xc3\xb8" "7");
}

// ── Non-diatonic guard ────────────────────────────────────────────────────────

// Non-diatonic chords now produce chromatic (borrowed) numerals.
TEST(Composing_ChordRomanNumeralTests, NonDiatonic_FlatVII_CMajor)
{
    // Bb major in C major = bVII.  rootPc=10, keyTonicPc=0, Ionian.
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(-1, ChordQuality::Major, 10, 10, false, false, false, false, 0, KeySigMode::Ionian)),
              "bVII");
}

TEST(Composing_ChordRomanNumeralTests, NonDiatonic_FlatIII_CMajor)
{
    // Eb major in C major = bIII.  rootPc=3, keyTonicPc=0, Ionian.
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(-1, ChordQuality::Major, 3, 3, false, false, false, false, 0, KeySigMode::Ionian)),
              "bIII");
}

TEST(Composing_ChordRomanNumeralTests, NonDiatonic_FlatVI_CMajor)
{
    // Ab major in C major = bVI.  rootPc=8, keyTonicPc=0, Ionian.
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(-1, ChordQuality::Major, 8, 8, false, false, false, false, 0, KeySigMode::Ionian)),
              "bVI");
}

TEST(Composing_ChordRomanNumeralTests, NonDiatonic_FlatVII_Minor_CMajor)
{
    // Bb minor in C major = bvii.  rootPc=10, minor quality.
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(-1, ChordQuality::Minor, 10, 10, false, false, false, false, 0, KeySigMode::Ionian)),
              "bvii");
}

TEST(Composing_ChordRomanNumeralTests, NonDiatonic_FlatVIIDom7_CMajor)
{
    // Bb7 in C major = bVII7.  rootPc=10, minor seventh.
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(-1, ChordQuality::Major, 10, 10, true, false, false, false, 0, KeySigMode::Ionian)),
              "bVII7");
}

// ── Triad inversions ──────────────────────────────────────────────────────────

TEST(Composing_ChordRomanNumeralTests, MajorTriad_FirstInversion_I6)
{
    // I6: bass = major third above root.  rootPc=0 (C), bassPc=4 (E).
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(0, ChordQuality::Major, 0, 4)), "I6");
}

TEST(Composing_ChordRomanNumeralTests, MajorTriad_SecondInversion_I64)
{
    // I64: bass = fifth above root.  rootPc=0 (C), bassPc=7 (G).
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(0, ChordQuality::Major, 0, 7)), "I64");
}

TEST(Composing_ChordRomanNumeralTests, MinorTriad_FirstInversion_i6)
{
    // i6: bass = minor third above root.  rootPc=0 (C), bassPc=3 (Eb).
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(0, ChordQuality::Minor, 0, 3)), "i6");
}

TEST(Composing_ChordRomanNumeralTests, DiminishedTriad_FirstInversion_viio6)
{
    // viio6: bass = minor third above root.  rootPc=11 (B), bassPc=2 (D).
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(6, ChordQuality::Diminished, 11, 2)), "viio6");
}

// ── Seventh-chord inversions ──────────────────────────────────────────────────

TEST(Composing_ChordRomanNumeralTests, DominantSeventh_FirstInversion_V65)
{
    // V65: bass = major third above root.  rootPc=7 (G), bassPc=11 (B).
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(4, ChordQuality::Major, 7, 11, true)), "V65");
}

TEST(Composing_ChordRomanNumeralTests, DominantSeventh_SecondInversion_V43)
{
    // V43: bass = fifth above root.  rootPc=7 (G), bassPc=2 (D).
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(4, ChordQuality::Major, 7, 2, true)), "V43");
}

TEST(Composing_ChordRomanNumeralTests, DominantSeventh_ThirdInversion_V42)
{
    // V42: bass = minor seventh above root.  rootPc=7 (G), bassPc=5 (F).
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(4, ChordQuality::Major, 7, 5, true)), "V42");
}

TEST(Composing_ChordRomanNumeralTests, MajorSeventh_FirstInversion_IM65)
{
    // IM65: bass = major third above root.  rootPc=0 (C), bassPc=4 (E).
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(0, ChordQuality::Major, 0, 4, false, true)), "I65");
}

TEST(Composing_ChordRomanNumeralTests, HalfDim_FirstInversion_viiHalfDim65)
{
    // viiø65: bass = minor third above root.  rootPc=11 (B), bassPc=2 (D).
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(6, ChordQuality::HalfDiminished, 11, 2)),
              "vii\xc3\xb8" "65");
}

TEST(Composing_ChordRomanNumeralTests, FullDim7_FirstInversion_viio65)
{
    // viio65: bass = minor third above root.  rootPc=11 (B), bassPc=2 (D).
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(6, ChordQuality::Diminished, 11, 2, false, false, true)),
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
                  makeRomanResult(0, ChordQuality::Major, 0, 0, false, false, false, true)),
              "I(add6)");
}

TEST(Composing_ChordRomanNumeralTests, MajorSixNine_I69)
{
    // C69 (C D E G A) — both add6 and add9 present → "I69" not "I(add6)".
    ChordAnalysisResult r = makeRomanResult(0, ChordQuality::Major, 0, 0, false, false, false, true);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "I69");
}

TEST(Composing_ChordRomanNumeralTests, MinorSixNine_i69)
{
    // Cm69 — minor 6/9 chord.
    ChordAnalysisResult r = makeRomanResult(0, ChordQuality::Minor, 0, 0, false, false, false, true);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "i69");
}

TEST(Composing_ChordRomanNumeralTests, MinorAdd6_i_add6)
{
    // Cm6 (C Eb G A) in root position.
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(0, ChordQuality::Minor, 0, 0, false, false, false, true)),
              "i(add6)");
}

TEST(Composing_ChordRomanNumeralTests, MajorAdd6_IV_add6)
{
    // F6 in C major — IV(add6).
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(3, ChordQuality::Major, 0, 0, false, false, false, true)),
              "IV(add6)");
}

TEST(Composing_ChordRomanNumeralTests, MajorAdd6_VI_add6_inMinor)
{
    // VI(add6) in minor.
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(5, ChordQuality::Major, 0, 0, false, false, false, true)),
              "VI(add6)");
}

TEST(Composing_ChordRomanNumeralTests, MajorFirstInversion_I6_isNotAdd6)
{
    // I6 = first inversion (E in bass), NOT an added-sixth chord.
    // Confirming no "(add6)" appears when hasAddedSixth is false.
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(
                  makeRomanResult(0, ChordQuality::Major, 0, 4)), "I6");
}

// ── Higher extensions (9th, 11th, 13th) ─────────────────────────────────────

TEST(Composing_ChordRomanNumeralTests, DominantNinth_V9)
{
    // V9: dominant 7th + natural 9th.
    ChordAnalysisResult r = makeRomanResult(4, ChordQuality::Major, 0, 0, true);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "V9");
}

TEST(Composing_ChordRomanNumeralTests, DominantEleventh_V11)
{
    // V11: dominant 7th + natural 11th (implies 9th).
    ChordAnalysisResult r = makeRomanResult(4, ChordQuality::Major, 0, 0, true);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    setExtension(r.identity.extensions, Extension::NaturalEleventh);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "V11");
}

TEST(Composing_ChordRomanNumeralTests, DominantThirteenth_V13)
{
    // V13: dominant 7th + natural 13th.
    ChordAnalysisResult r = makeRomanResult(4, ChordQuality::Major, 0, 0, true);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    setExtension(r.identity.extensions, Extension::NaturalEleventh);
    setExtension(r.identity.extensions, Extension::NaturalThirteenth);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "V13");
}

TEST(Composing_ChordRomanNumeralTests, MajorNinth_IM9)
{
    // IM9: major 7th + natural 9th.
    ChordAnalysisResult r = makeRomanResult(0, ChordQuality::Major, 0, 0, false, true);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "IM9");
}

TEST(Composing_ChordRomanNumeralTests, MajorThirteenth_IM13)
{
    // IM13: major 7th + natural 13th.
    ChordAnalysisResult r = makeRomanResult(0, ChordQuality::Major, 0, 0, false, true);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    setExtension(r.identity.extensions, Extension::NaturalEleventh);
    setExtension(r.identity.extensions, Extension::NaturalThirteenth);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "IM13");
}

TEST(Composing_ChordRomanNumeralTests, MinorNinth_ii9)
{
    // ii9: minor 7th + natural 9th.
    ChordAnalysisResult r = makeRomanResult(1, ChordQuality::Minor, 0, 0, true);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "ii9");
}

TEST(Composing_ChordRomanNumeralTests, MinorEleventh_ii11)
{
    // ii11: minor 7th + natural 11th.
    ChordAnalysisResult r = makeRomanResult(1, ChordQuality::Minor, 0, 0, true);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    setExtension(r.identity.extensions, Extension::NaturalEleventh);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "ii11");
}

TEST(Composing_ChordRomanNumeralTests, MinorThirteenth_vi13)
{
    // vi13: minor 7th + natural 13th.
    ChordAnalysisResult r = makeRomanResult(5, ChordQuality::Minor, 0, 0, true);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    setExtension(r.identity.extensions, Extension::NaturalEleventh);
    setExtension(r.identity.extensions, Extension::NaturalThirteenth);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "vi13");
}

// ── Altered extensions ───────────────────────────────────────────────────────

TEST(Composing_ChordRomanNumeralTests, DominantFlatNinth_V7b9)
{
    // V7b9: dominant 7th + flat 9th (no natural 9th → level stays at 7).
    ChordAnalysisResult r = makeRomanResult(4, ChordQuality::Major, 0, 0, true);
    setExtension(r.identity.extensions, Extension::FlatNinth);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "V7b9");
}

TEST(Composing_ChordRomanNumeralTests, DominantSharpNinth_V7SharpNine)
{
    // V7#9: dominant 7th + sharp 9th.
    ChordAnalysisResult r = makeRomanResult(4, ChordQuality::Major, 0, 0, true);
    setExtension(r.identity.extensions, Extension::SharpNinth);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "V7#9");
}

TEST(Composing_ChordRomanNumeralTests, DominantNinthSharpEleven_V9SharpEleven)
{
    // V9#11: dominant 9th + sharp 11th.
    ChordAnalysisResult r = makeRomanResult(4, ChordQuality::Major, 0, 0, true);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    setExtension(r.identity.extensions, Extension::SharpEleventh);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "V9#11");
}

TEST(Composing_ChordRomanNumeralTests, DominantThirteenthFlatNinth_V13b9)
{
    // V13b9: dominant 13th + flat 9th alteration.
    ChordAnalysisResult r = makeRomanResult(4, ChordQuality::Major, 0, 0, true);
    setExtension(r.identity.extensions, Extension::FlatNinth);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    setExtension(r.identity.extensions, Extension::NaturalEleventh);
    setExtension(r.identity.extensions, Extension::NaturalThirteenth);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "V13b9");
}

TEST(Composing_ChordRomanNumeralTests, DominantSeventhFlatFive_V7b5)
{
    // V7b5: dominant 7th + flat fifth.
    ChordAnalysisResult r = makeRomanResult(4, ChordQuality::Major, 0, 0, true);
    setExtension(r.identity.extensions, Extension::FlatFifth);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "V7b5");
}

TEST(Composing_ChordRomanNumeralTests, DominantSeventhSharpFive_V7SharpFive)
{
    // V7#5: dominant 7th + sharp fifth (augmented quality would use "+" instead).
    ChordAnalysisResult r = makeRomanResult(4, ChordQuality::Major, 0, 0, true);
    setExtension(r.identity.extensions, Extension::SharpFifth);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "V7#5");
}

TEST(Composing_ChordRomanNumeralTests, DominantSeventhFlatNinthSharpEleven_V7b9SharpEleven)
{
    // V7b9#11: multiple alterations stacked.
    ChordAnalysisResult r = makeRomanResult(4, ChordQuality::Major, 0, 0, true);
    setExtension(r.identity.extensions, Extension::FlatNinth);
    setExtension(r.identity.extensions, Extension::SharpEleventh);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "V7b9#11");
}

TEST(Composing_ChordRomanNumeralTests, DominantSeventhFlatThirteenth_V7b13)
{
    // V7b13: dominant 7th + flat 13th.
    ChordAnalysisResult r = makeRomanResult(4, ChordQuality::Major, 0, 0, true);
    setExtension(r.identity.extensions, Extension::FlatThirteenth);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "V7b13");
}

// ── Half-diminished extensions ───────────────────────────────────────────────

TEST(Composing_ChordRomanNumeralTests, HalfDimNinth_iiHalfDim9)
{
    // iiø9: half-diminished with natural 9th.
    ChordAnalysisResult r = makeRomanResult(1, ChordQuality::HalfDiminished);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "ii\xc3\xb8" "9");
}

TEST(Composing_ChordRomanNumeralTests, HalfDimEleventh_iiHalfDim11)
{
    // iiø11: half-diminished with natural 11th.
    ChordAnalysisResult r = makeRomanResult(1, ChordQuality::HalfDiminished);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    setExtension(r.identity.extensions, Extension::NaturalEleventh);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "ii\xc3\xb8" "11");
}

// ── Suspended chord extensions ───────────────────────────────────────────────

TEST(Composing_ChordRomanNumeralTests, SuspendedFour_V7sus4)
{
    // V7sus4: suspended 4th + dominant 7th.
    ChordAnalysisResult r = makeRomanResult(4, ChordQuality::Suspended4, 0, 0, true);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "V7sus4");
}

TEST(Composing_ChordRomanNumeralTests, SuspendedFour_V9sus4)
{
    // V9sus4: suspended 4th + dominant 9th.
    ChordAnalysisResult r = makeRomanResult(4, ChordQuality::Suspended4, 0, 0, true);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "V9sus4");
}

TEST(Composing_ChordRomanNumeralTests, SuspendedFour_V13sus4)
{
    // V13sus4: suspended 4th + dominant 13th.
    ChordAnalysisResult r = makeRomanResult(4, ChordQuality::Suspended4, 0, 0, true);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    setExtension(r.identity.extensions, Extension::NaturalEleventh);
    setExtension(r.identity.extensions, Extension::NaturalThirteenth);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "V13sus4");
}

TEST(Composing_ChordRomanNumeralTests, SuspendedTwo_V7sus2)
{
    // V7sus2: suspended 2nd + dominant 7th.
    ChordAnalysisResult r = makeRomanResult(4, ChordQuality::Suspended2, 0, 0, true);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "V7sus2");
}

// ── Augmented extensions ─────────────────────────────────────────────────────

TEST(Composing_ChordRomanNumeralTests, AugmentedNinth_I_plus_9)
{
    // I+9: augmented + dominant 9th.
    ChordAnalysisResult r = makeRomanResult(0, ChordQuality::Augmented, 0, 0, true);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "I+9");
}

TEST(Composing_ChordRomanNumeralTests, AugmentedMajorNinth_I_plus_M9)
{
    // I+M9: augmented + major 9th.
    ChordAnalysisResult r = makeRomanResult(0, ChordQuality::Augmented, 0, 0, false, true);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "I+M9");
}

// ── "add" notation (extensions without 7th) ──────────────────────────────────

TEST(Composing_ChordRomanNumeralTests, MajorAddNinth_I_add9)
{
    // I(add9): major triad + natural 9th, no 7th.
    ChordAnalysisResult r = makeRomanResult(0, ChordQuality::Major);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "I(add9)");
}

TEST(Composing_ChordRomanNumeralTests, MinorAddNinth_i_add9)
{
    // i(add9): minor triad + natural 9th, no 7th.
    ChordAnalysisResult r = makeRomanResult(0, ChordQuality::Minor);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "i(add9)");
}

TEST(Composing_ChordRomanNumeralTests, MajorAddSharpEleven_I_addSharpEleven)
{
    // I(add#11): major triad + sharp 11th, no 7th (Lydian flavor).
    ChordAnalysisResult r = makeRomanResult(0, ChordQuality::Major);
    setExtension(r.identity.extensions, Extension::SharpEleventh);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "I(add#11)");
}

TEST(Composing_ChordRomanNumeralTests, MajorAddFlatNinth_I_addFlatNine)
{
    // I(addb9): major triad + flat 9th, no 7th.
    ChordAnalysisResult r = makeRomanResult(0, ChordQuality::Major);
    setExtension(r.identity.extensions, Extension::FlatNinth);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "I(addb9)");
}

// ── Suspended chords with added colour tones ──────────────────────────────────

TEST(Composing_ChordSymbolFormatterTests, Sus4WithNaturalNinthFormatsAsSusAdd9)
{
    // Bb-C-Eb-F: Bb suspended-4 with natural 9th (added 2nd).
    // Should format as "Bbsus(add9)", not plain "Bbsus".
    ChordAnalysisResult r = makeRomanResult(0, ChordQuality::Suspended4, 10 /*Bb*/, 10 /*bass=root*/);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    const std::string sym = ChordSymbolFormatter::formatSymbol(r, -2 /*Bb key*/);
    EXPECT_EQ(sym, "Bbsus(add9)");
}

TEST(Composing_ChordSymbolFormatterTests, Sus2WithNaturalEleventhFormatsAsSus2Add4)
{
    // C-D-F-G: C suspended-2 with natural eleventh (added 4th).
    // Should format as "Csus2(add4)", not plain "Csus2".
    ChordAnalysisResult r = makeRomanResult(0, ChordQuality::Suspended2);
    setExtension(r.identity.extensions, Extension::NaturalEleventh);
    const std::string sym = ChordSymbolFormatter::formatSymbol(r, 0);
    EXPECT_EQ(sym, "Csus2(add4)");
}

TEST(Composing_ChordSymbolFormatterTests, Sus4WithMin7AndNaturalNinthFormatsAsSusAdd9)
{
    // C-F-G-Bb-D: C suspended-4 with minor 7th and natural 9th.
    // "9sus" is not in chords_std.xml and triggers a corrupted render ("sussus9").
    // Must use "sus(add9)" instead.
    ChordAnalysisResult r = makeRomanResult(0, ChordQuality::Suspended4);
    setExtension(r.identity.extensions, Extension::MinorSeventh);
    setExtension(r.identity.extensions, Extension::NaturalNinth);
    const std::string sym = ChordSymbolFormatter::formatSymbol(r, 0);
    EXPECT_EQ(sym, "Csus(add9)");
}

TEST(Composing_ChordSymbolFormatterTests, InvalidBassPcSuppressesSlashBass)
{
    // When bassPc is out of the valid 0–11 range (e.g. -1 from an analysis error),
    // the slash bass suffix must be suppressed to avoid outputting garbage like "BbMaj7/p".
    // bassTpc = -1 (normal "no TPC data" sentinel) is a separate, valid case handled
    // by pitchClassName key-signature fallback and must NOT suppress the slash bass.
    ChordAnalysisResult r = makeRomanResult(0, ChordQuality::Major, 10 /*Bb*/, 3 /*Eb*/, false, true);
    r.identity.bassPc = -1;  // Simulate an out-of-range bassPc that would cause UB in pitchClassName
    const std::string sym = ChordSymbolFormatter::formatSymbol(r, -2);  // Bb key
    EXPECT_EQ(sym.find('/'), std::string::npos)
        << "Slash bass present despite invalid bassPc in: " << sym;
    EXPECT_FALSE(sym.empty());
}

// ── Bug-10: P5 presence is a hard contradiction against Diminished quality ────
//
// A chord with a perfect fifth above the root cannot be diminished (diminished
// requires a ♭5).  This was causing I° output on plain tonic major/minor triads
// when non-chord tones were present in the collected pitch set.

TEST(Composing_ChordAnalyzerTests, CmajorTriadIsNeverDiminished)
{
    // {C, E, G} — plain major triad; must not score as diminished.
    const auto results = kAnalyzer.analyzeChord(tones({ 60, 64, 67 }), 0, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_NE(results.front().identity.quality, ChordQuality::Diminished)
        << "C major triad must not be scored as diminished";
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Major);
}

TEST(Composing_ChordAnalyzerTests, CminorTriadIsNeverDiminished)
{
    // {C, Eb, G} — plain minor triad; must not score as diminished.
    const auto results = kAnalyzer.analyzeChord(tones({ 60, 63, 67 }), 0, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_NE(results.front().identity.quality, ChordQuality::Diminished)
        << "C minor triad must not be scored as diminished";
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Minor);
}

TEST(Composing_ChordAnalyzerTests, CdiminishedTriadIsDiminished)
{
    // {C, Eb, Gb} — only the chord with a ♭5 (no P5) should score as diminished.
    const auto results = kAnalyzer.analyzeChord(tones({ 60, 63, 66 }), 0, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Diminished)
        << "C diminished triad must score as diminished";
}

TEST(Composing_ChordAnalyzerTests, MajorTriadWithPassingToneIsNeverDiminished)
{
    // {C, Eb, E, G} — C major triad with chromatic passing tone Eb.
    // The perfect fifth G must veto the Diminished reading even though Eb is present.
    const auto results = kAnalyzer.analyzeChord(tones({ 60, 63, 64, 67 }), 0, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_NE(results.front().identity.quality, ChordQuality::Diminished)
        << "C major with passing Eb must not be scored as diminished";
}

// ── Flat-root pitch-class extraction tests ────────────────────────────────────
// These tests verify that flat-spelled roots (Ab, Gb, Db, Eb, Bb) are correctly
// identified as their own pitch class and not misread a semitone sharp.
// TPC encoding used below matches the test convention: F=14, C=15, G=16, D=17,
// A=18, E=19, B=20; each flat subtracts 7.  So Ab=11, Gb=9, Db=10, Eb=12, Bb=13.

TEST(Composing_ChordAnalyzerTests, FlatRoot_AbMajorTriad_RootIspc8)
{
    // Ab major triad: Ab4(68), C5(72), Eb5(75).  TPC: Ab=11, C=15, Eb=12.
    // Root must be pc=8 (Ab), not pc=9 (A).
    const auto results = kAnalyzer.analyzeChord(
        tonesWithTpc({ {68,11}, {72,15}, {75,12} }), -4, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 8)
        << "Ab major triad: root must be pc=8 (Ab), not pc=9 (A)";
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Major);
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(results.front(), -4), "Ab");
}

TEST(Composing_ChordAnalyzerTests, FlatRoot_GbMajorTriad_RootIspc6)
{
    // Gb major triad: Gb4(66), Bb4(70), Db5(73).  TPC: Gb=9, Bb=13, Db=10.
    // Root must be pc=6 (Gb), not pc=7 (G).
    const auto results = kAnalyzer.analyzeChord(
        tonesWithTpc({ {66,9}, {70,13}, {73,10} }), -6, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 6)
        << "Gb major triad: root must be pc=6 (Gb), not pc=7 (G)";
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(results.front(), -6), "Gb");
}

TEST(Composing_ChordAnalyzerTests, FlatRoot_DbMajorTriad_RootIspc1)
{
    // Db major triad: Db4(61), F4(65), Ab4(68).  TPC: Db=10, F=14, Ab=11.
    // Root must be pc=1 (Db), not pc=2 (D).
    const auto results = kAnalyzer.analyzeChord(
        tonesWithTpc({ {61,10}, {65,14}, {68,11} }), -5, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 1)
        << "Db major triad: root must be pc=1 (Db), not pc=2 (D)";
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(results.front(), -5), "Db");
}

TEST(Composing_ChordAnalyzerTests, FlatRoot_EbMajorTriad_RootIspc3)
{
    // Eb major triad: Eb4(63), G4(67), Bb4(70).  TPC: Eb=12, G=16, Bb=13.
    // Root must be pc=3 (Eb), not pc=4 (E).
    const auto results = kAnalyzer.analyzeChord(
        tonesWithTpc({ {63,12}, {67,16}, {70,13} }), -3, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 3)
        << "Eb major triad: root must be pc=3 (Eb), not pc=4 (E)";
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(results.front(), -3), "Eb");
}

TEST(Composing_ChordAnalyzerTests, FlatRoot_BbMajorTriad_RootIspc10)
{
    // Bb major triad: Bb3(58), D4(62), F4(65).  TPC: Bb=13, D=17, F=14.
    // Root must be pc=10 (Bb), not pc=11 (B).
    const auto results = kAnalyzer.analyzeChord(
        tonesWithTpc({ {58,13}, {62,17}, {65,14} }), -2, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 10)
        << "Bb major triad: root must be pc=10 (Bb), not pc=11 (B)";
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(results.front(), -2), "Bb");
}

TEST(Composing_ChordAnalyzerTests, FlatRoot_AbMaj7_DisplaysAbInFlatKey)
{
    // AbMaj7: Ab4(68), C5(72), Eb5(75), G5(79).  TPC: Ab=11, C=15, Eb=12, G=16.
    // Symbol must be "AbMaj7" in Ab major context, not "G#Maj7" or "AMaj7".
    const auto results = kAnalyzer.analyzeChord(
        tonesWithTpc({ {68,11}, {72,15}, {75,12}, {79,16} }), -4, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 8)
        << "AbMaj7: root must be pc=8 (Ab)";
    const std::string sym = ChordSymbolFormatter::formatSymbol(results.front(), -4);
    EXPECT_EQ(sym, "AbMaj7") << "AbMaj7 symbol must use flat spelling in Ab major key";
}

TEST(Composing_ChordAnalyzerTests, FullyDiminishedSeventh_NashvilleHasExactlyOneDegreeSymbol)
{
    // B fully diminished seventh: B3(47), D4(50), F4(53), Ab4(56).
    // TPC: B=20, D=17, F=14, Ab=11.  Key: C major (fifths=0).
    // Nashville symbol must be "vii°7", not "vii°°7" — exactly one ° before the 7.
    const auto results = kAnalyzer.analyzeChord(
        tonesWithTpc({ {47,20}, {50,17}, {53,14}, {56,11} }), 0, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    const std::string nashville = ChordSymbolFormatter::formatNashvilleNumber(results.front(), 0);
    // Count occurrences of the UTF-8 degree symbol \xc2\xb0 (2 bytes per symbol)
    static const std::string kDeg = "\xc2\xb0";
    size_t count = 0;
    size_t pos = 0;
    while ((pos = nashville.find(kDeg, pos)) != std::string::npos) {
        ++count;
        pos += kDeg.size();
    }
    EXPECT_EQ(count, 1u)
        << "Fully diminished 7th Nashville symbol must contain exactly one ° symbol, got: " << nashville;
    // Also verify the symbol ends with °7 (one degree + 7)
    EXPECT_NE(nashville.find(kDeg + "7"), std::string::npos)
        << "Fully diminished 7th Nashville symbol must contain °7, got: " << nashville;
}

// ── Non-standard quality token verification (Step 4) ────────────────────────
// These tests confirm that each non-standard chord symbol token is generated
// correctly by the formatter. Bugs here would surface as garbled chord labels
// in real scores (jazz, film, pop contexts).

TEST(Composing_ChordAnalyzerTests, NonStdToken_Susb9_ProducesCorrectSymbol)
{
    // Csusb9: C4(60), Db4(61), F4(65), G4(67) — sus4 with b9, no 7th.
    // Catalog: measure 323, xml='Csusb9'.
    const auto results = kAnalyzer.analyzeChord(tones({ 60, 61, 65, 67 }), 0, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(results.front(), 0), "Csusb9");
}

TEST(Composing_ChordAnalyzerTests, NonStdToken_SusSharp4_ProducesCorrectSymbol)
{
    // Csus#4: C4(60), F#4(66), G4(67) — sus with augmented fourth.
    // Catalog: measure 340, xml='Csus#4'.
    const auto results = kAnalyzer.analyzeChord(tones({ 60, 66, 67 }), 0, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(results.front(), 0), "Csus#4");
}

TEST(Composing_ChordAnalyzerTests, NonStdToken_5b_ProducesCorrectSymbol)
{
    // C5b: C4(60), E4(64), Gb4(66) — major triad with flat 5.
    // MuseScore convention: flat-5 major triad uses "5b" (not "b5" or "C(b5)").
    // Catalog: measure 4, xml='C5b'.
    const auto results = kAnalyzer.analyzeChord(tones({ 60, 64, 66 }), 0, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(results.front(), 0), "C5b");
}

TEST(Composing_ChordAnalyzerTests, NonStdToken_No3_ProducesCorrectSymbol)
{
    // CMaj9(no 3): C4(60), G4(67), B4(71), D5(74) — major 9th with omitted third.
    // Catalog: measure 20, xml='CMaj9(no 3)'.
    const auto results = kAnalyzer.analyzeChord(tones({ 60, 67, 71, 74 }), 0, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(results.front(), 0), "CMaj9(no 3)");
}

// ── Passing-tone bass filter (Step 5) ───────────────────────────────────────

TEST(Composing_ChordAnalyzerTests, PassingToneBassFilter_LowWeightBassNoteIgnored)
{
    // G major triad (G4=67, B4=71, D5=74) with a low-weight chromatic passing tone
    // F#3(54) in the bass.  F# has weight 0.02 (fleeting 32nd note); the G tones
    // have weight 1.0 each.  The passing-tone filter (threshold=5%) must discard F#
    // as bass and identify G as bass → symbol "G" (root position), not "G/F#".
    ChordAnalyzerPreferences prefs;
    prefs.bassPassingToneMinWeightFraction = 0.05;

    std::vector<ChordAnalysisTone> ts;
    auto addTone = [&](int pitch, double weight) {
        ChordAnalysisTone t;
        t.pitch  = pitch;
        t.weight = weight;
        t.isBass = false;
        ts.push_back(t);
    };
    addTone(54, 0.02);  // F#3 — low-weight passing tone
    addTone(67, 1.0);   // G4
    addTone(71, 1.0);   // B4
    addTone(74, 1.0);   // D5
    ts.front().isBass = true;  // F#3 is the lowest note

    const auto results = kAnalyzer.analyzeChord(ts, 0, KeySigMode::Ionian, nullptr, prefs);
    ASSERT_FALSE(results.empty());
    // Root should be G (pc=7), bass should also be G (root position) — F# filtered out.
    EXPECT_EQ(results.front().identity.rootPc, 7)
        << "Root must be G (pc=7), not F# (pc=6)";
    EXPECT_EQ(results.front().identity.bassPc, 7)
        << "Bass must be G (pc=7): F# passing tone must be filtered by weight threshold";
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(results.front(), 0), "G")
        << "G major triad with filtered passing-tone bass must display as 'G' (root position)";
}

TEST(Composing_ChordAnalyzerTests, PassingToneBassFilter_NormalBassNoteKept)
{
    // G/F# first-inversion-style slash chord: F#3(54) with structural weight 1.0.
    // The filter must NOT remove it — only genuine passing tones (low weight) are filtered.
    ChordAnalyzerPreferences prefs;
    prefs.bassPassingToneMinWeightFraction = 0.05;

    std::vector<ChordAnalysisTone> ts;
    auto addTone = [&](int pitch, double weight) {
        ChordAnalysisTone t;
        t.pitch  = pitch;
        t.weight = weight;
        t.isBass = false;
        ts.push_back(t);
    };
    addTone(54, 1.0);  // F#3 — structural bass (not a passing tone)
    addTone(67, 1.0);  // G4
    addTone(71, 1.0);  // B4
    addTone(74, 1.0);  // D5
    ts.front().isBass = true;

    const auto results = kAnalyzer.analyzeChord(ts, 0, KeySigMode::Ionian, nullptr, prefs);
    ASSERT_FALSE(results.empty());
    // Bass should remain F# (pc=6); root should be G (pc=7) → symbol "G/F#"
    EXPECT_EQ(results.front().identity.bassPc, 6)
        << "Structural bass F# must not be filtered by passing-tone threshold";
}

// ── Slash-chord annotation path: Cm7/F must not be written as "F" ────────────
//
// Regression guard for the annotation-path temporal-bias bug.  The harmonic-
// rhythm pass may carry rootContinuityBonus from a preceding F-major region,
// promoting F over Cm7/F.  The annotation write path re-runs analyzeChord()
// with a display-style ChordTemporalContext (from findTemporalContext) rather
// than the sequential context from analyzeHarmonicRhythm.
//
// Two sub-cases exercised here:
//
//   (A) C-chord tones heavily dominate F — analyzeChord() gives Cm7/F even
//       without any temporal context.  This verifies the analyzer correctly
//       identifies the chord from note content alone when C is prominent.
//
//   (B) Equal-weight voicing (F bass + C,Eb,G,Bb at equal weight) + a
//       ChordTemporalContext with bassIsStepwiseFromPrevious=true — mirrors
//       the display path temporal bonus that selects Cm7/F over Fsus.
//       Without temporal context (nullptr) the same tones produce Fsus(add9)
//       (bass-root bonus tips it to F), confirming the annotation fix must
//       supply context not null.

TEST(Composing_ChordAnalyzerTests, Cm7SlashF_ChordTonesDominant_IsCm7WithoutContext)
{
    // F bass is deliberately light so that C-rooted chord tones dominate
    // and Cm7/F wins on note content alone (no temporal context needed).
    std::vector<ChordAnalysisTone> ts;
    auto addTone = [&](int pitch, double weight, bool isBass = false) {
        ChordAnalysisTone t;
        t.pitch  = pitch;
        t.weight = weight;
        t.isBass = isBass;
        ts.push_back(t);
    };
    addTone(41, 0.2, true);   // F2  — bass (low weight: brief pedal)
    addTone(48, 1.0);          // C4  — root (strong)
    addTone(51, 1.0);          // Eb4 — minor third (strong)
    addTone(55, 0.9);          // G4  — fifth
    addTone(58, 0.8);          // Bb4 — minor seventh

    const auto results = kAnalyzer.analyzeChord(ts, 0, KeySigMode::Ionian, nullptr);
    ASSERT_FALSE(results.empty());

    const ChordAnalysisResult& top = results.front();
    EXPECT_EQ(top.identity.rootPc, 0)
        << "Root must be C (pc=0); got " << top.identity.rootPc;
    EXPECT_EQ(top.identity.bassPc, 5)
        << "Bass must be F (pc=5)";
    EXPECT_EQ(top.identity.quality, ChordQuality::Minor)
        << "Quality must be Minor";
    EXPECT_TRUE(hasExtension(top.identity.extensions, Extension::MinorSeventh))
        << "MinorSeventh must be present";
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(top, 0), "Cm7/F");
}

TEST(Composing_ChordAnalyzerTests, Cm7SlashF_StepwiseBassContext_IsCm7NotFsus)
{
    // Equal-weight voicing: the bass-root bonus would push F to the top
    // without temporal context.  With bassIsStepwiseFromPrevious=true the
    // stepwiseBassInversionBonus fires for the inverted C-rooted candidate
    // (bass != root, Major/Minor quality), flipping the result to Cm7/F.
    // This is the mechanism the annotation-path fix relies on: it supplies
    // findTemporalContext() to analyzeChord(), which populates the stepwise
    // flag from the actual score, just as the display path does.
    std::vector<ChordAnalysisTone> ts;
    auto addTone = [&](int pitch, double weight, bool isBass = false) {
        ChordAnalysisTone t;
        t.pitch  = pitch;
        t.weight = weight;
        t.isBass = isBass;
        ts.push_back(t);
    };
    addTone(41, 1.0, true);   // F2  — bass (equal weight)
    addTone(48, 1.0);          // C4
    addTone(51, 0.9);          // Eb4
    addTone(55, 0.8);          // G4
    addTone(58, 0.7);          // Bb4

    // Without context: Fsus(add9) wins.
    {
        const auto noCtx = kAnalyzer.analyzeChord(ts, 0, KeySigMode::Ionian, nullptr);
        ASSERT_FALSE(noCtx.empty());
        EXPECT_NE(noCtx.front().identity.rootPc, 0)
            << "Without context, F-rooted template should win (bass-root bonus)";
    }

    // With display-style context: Cm7/F must win.
    // findTemporalContext() in the actual score sets previousRootPc from the
    // previous chord.  If the preceding chord was Cm (root=C), Cm7/F gets:
    //   rootContinuityBonus   (+0.40) — same root as before
    //   sameRootInversionBonus(+0.40) — inversion of the same root
    //   stepwiseBassInversionBonus (+0.50) — bass moved stepwise into F
    // Combined (+1.30) these flip Cm7/F past the Fsus(add9) bass-root winner.
    ChordTemporalContext ctx;
    ctx.previousRootPc           = 0;    // previous chord root was C
    ctx.previousBassPc           = 0;
    ctx.previousQuality          = ChordQuality::Minor;
    ctx.bassIsStepwiseFromPrevious = true;  // e.g. bass moved E → F
    ctx.bassIsStepwiseToNext      = false;

    const auto withCtx = kAnalyzer.analyzeChord(ts, 0, KeySigMode::Ionian, &ctx);
    ASSERT_FALSE(withCtx.empty());

    const ChordAnalysisResult& top = withCtx.front();
    EXPECT_EQ(top.identity.rootPc, 0)
        << "With stepwise-bass context, root must be C (pc=0)";
    EXPECT_EQ(top.identity.bassPc, 5)
        << "Bass must be F (pc=5)";
    EXPECT_EQ(top.identity.quality, ChordQuality::Minor)
        << "Quality must be Minor";
    EXPECT_TRUE(hasExtension(top.identity.extensions, Extension::MinorSeventh))
        << "MinorSeventh must be present";
    // F (pc=5) is both the bass note and a perfect fourth above C (= add11),
    // so with equal-weight tones the extension threshold is exceeded and the
    // formatter produces "Cm7add11/F".  The critical assertion is root=C, not F.
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(top, 0), "Cm7add11/F");
}

// ── B/H Note Naming (German/Nordic convention) ──────────────────────────────
// NoteSpelling enum mirrors NoteSpellingType in src/engraving/types/types.h.
// German mapping mirrors tpc2name() GERMAN case (pitchspelling.cpp:343-356):
//   Rule 1: B natural → "H"
//   Rule 2: Bb → "B"
// All other note names are unchanged.

TEST(Composing_ChordAnalyzerTests, NoteSpelling_Standard_BNatural_IsB)
{
    // B major triad in 5-sharp key. Standard spelling: root = "B".
    const auto results = kAnalyzer.analyzeChord(
        tonesWithTpc({ {59,20}, {63,24}, {66,18} }), 5, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 11);
    const ChordSymbolFormatter::Options opts{ ChordSymbolFormatter::NoteSpelling::Standard };
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(results.front(), 5, opts), "B");
}

TEST(Composing_ChordAnalyzerTests, NoteSpelling_Standard_Bb_IsBb)
{
    // Bb major triad in 2-flat key. Standard spelling: root = "Bb".
    const auto results = kAnalyzer.analyzeChord(
        tonesWithTpc({ {58,13}, {62,17}, {65,14} }), -2, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 10);
    const ChordSymbolFormatter::Options opts{ ChordSymbolFormatter::NoteSpelling::Standard };
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(results.front(), -2, opts), "Bb");
}

TEST(Composing_ChordAnalyzerTests, NoteSpelling_German_BNatural_IsH)
{
    // B major triad in 5-sharp key. German spelling: B natural → "H".
    const auto results = kAnalyzer.analyzeChord(
        tonesWithTpc({ {59,20}, {63,24}, {66,18} }), 5, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 11);
    const ChordSymbolFormatter::Options opts{ ChordSymbolFormatter::NoteSpelling::German };
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(results.front(), 5, opts), "H");
}

TEST(Composing_ChordAnalyzerTests, NoteSpelling_German_Bb_IsB)
{
    // Bb major triad in 2-flat key. German spelling: Bb → "B".
    const auto results = kAnalyzer.analyzeChord(
        tonesWithTpc({ {58,13}, {62,17}, {65,14} }), -2, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 10);
    const ChordSymbolFormatter::Options opts{ ChordSymbolFormatter::NoteSpelling::German };
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(results.front(), -2, opts), "B");
}

TEST(Composing_ChordAnalyzerTests, NoteSpelling_German_C_Unchanged)
{
    // C major triad. German spelling: "C" is unchanged (not affected by B/H rule).
    const auto results = kAnalyzer.analyzeChord(
        tonesWithTpc({ {60,15}, {64,19}, {67,16} }), 0, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 0);
    const ChordSymbolFormatter::Options opts{ ChordSymbolFormatter::NoteSpelling::German };
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(results.front(), 0, opts), "C");
}

TEST(Composing_ChordAnalyzerTests, NoteSpelling_German_Ab_Unchanged)
{
    // Ab major triad in 4-flat key. German spelling: "Ab" is unchanged.
    const auto results = kAnalyzer.analyzeChord(
        tonesWithTpc({ {68,11}, {72,15}, {75,12} }), -4, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 8);
    const ChordSymbolFormatter::Options opts{ ChordSymbolFormatter::NoteSpelling::German };
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(results.front(), -4, opts), "Ab");
}

TEST(Composing_ChordAnalyzerTests, NoteSpelling_GermanPure_BNatural_IsH)
{
    // B major triad in 5-sharp key. GermanPure spelling: B natural → "H".
    const auto results = kAnalyzer.analyzeChord(
        tonesWithTpc({ {59,20}, {63,24}, {66,18} }), 5, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 11);
    const ChordSymbolFormatter::Options opts{ ChordSymbolFormatter::NoteSpelling::GermanPure };
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(results.front(), 5, opts), "H");
}

TEST(Composing_ChordAnalyzerTests, NoteSpelling_GermanPure_Bb_IsB)
{
    // Bb major triad in 2-flat key. GermanPure spelling: Bb → "B".
    const auto results = kAnalyzer.analyzeChord(
        tonesWithTpc({ {58,13}, {62,17}, {65,14} }), -2, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 10);
    const ChordSymbolFormatter::Options opts{ ChordSymbolFormatter::NoteSpelling::GermanPure };
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(results.front(), -2, opts), "B");
}

TEST(Composing_ChordAnalyzerTests, ChordNameInBassField_Suppressed)
{
    // Regression guard for MFV QA bug where "C7b9/Bb" appeared in the bass
    // field of a slash chord instead of a plain note name, producing output
    // like "BbMaj7add13/C7b9/Bb".
    //
    // The formatter's isValidBassNoteName guard ensures any bass name that is
    // not a plain note name (uppercase letter + optional accidentals, ≤ 3 chars)
    // suppresses the slash rather than emitting an invalid symbol.
    //
    // This test constructs a BbMaj7-type voicing with an F bass (second
    // inversion) and verifies: the symbol starts with "Bb", and if a slash
    // is present, the bass field after "/" is a valid plain note name only.
    std::vector<ChordAnalysisTone> ts;
    auto addTone = [&](int pitch, double weight, bool isBass = false) {
        ChordAnalysisTone t;
        t.pitch  = pitch;
        t.weight = weight;
        t.isBass = isBass;
        ts.push_back(t);
    };
    // F2 bass (light), Bb3 root (strong), D4 third, A4 maj7, G4 maj13
    addTone(41, 0.3, true);   // F2  — bass (inverted, light)
    addTone(58, 1.0);          // Bb3 — root (strong)
    addTone(62, 0.8);          // D4  — major third
    addTone(69, 0.6);          // A4  — major seventh
    addTone(67, 0.5);          // G4  — major thirteenth

    const auto results = kAnalyzer.analyzeChord(ts, -2, KeySigMode::Ionian, nullptr);
    ASSERT_FALSE(results.empty());

    const ChordSymbolFormatter::Options opts{};
    const std::string symbol = ChordSymbolFormatter::formatSymbol(results.front(), -2, opts);

    // Root must be Bb.
    EXPECT_EQ(symbol.substr(0, 2), "Bb")
        << "Root must be Bb; got: " << symbol;

    // If a slash is present, the bass field must be a valid plain note name:
    // at most 3 characters, starting with an uppercase letter.
    const size_t slashPos = symbol.find('/');
    if (slashPos != std::string::npos) {
        const std::string bassField = symbol.substr(slashPos + 1);
        EXPECT_LE(bassField.size(), 3u)
            << "Bass field must be at most 3 chars (plain note name); got: '"
            << bassField << "' in symbol: " << symbol;
        EXPECT_FALSE(bassField.empty());
        if (!bassField.empty()) {
            EXPECT_TRUE(std::isupper(static_cast<unsigned char>(bassField[0])))
                << "Bass field must start with an uppercase letter; got: '"
                << bassField << "' in symbol: " << symbol;
        }
        // Must contain no further slash (no nested chord symbol).
        EXPECT_EQ(bassField.find('/'), std::string::npos)
            << "Bass field must not contain a second slash; got: '"
            << bassField << "' in symbol: " << symbol;
    }
}

// ── Tonicization label tests (V7/x, vii°/x) ─────────────────────────────────
//
// Tests use makeRomanResult() + manual nextRootPc assignment, so they are fully
// decoupled from the chord analysis algorithm and bridge wiring.
//
// Convention:
//   rootPc values: C=0 D=2 E=4 F=5 G=7 A=9 B=11  (C#=1 Eb=3 F#=6 Ab=8 Bb=10)
//
// All tests are in C major (keyTonicPc=0, Ionian) unless noted otherwise.

// Helper: build a dom7 result for a given root in C major, then set nextRootPc.
static ChordAnalysisResult dom7Result(int rootPc, int nextRootPc,
                                      int keyTonicPc = 0,
                                      KeySigMode keyMode = KeySigMode::Ionian)
{
    // degree = scale position of rootPc in the key (may be -1 for chromatic roots)
    constexpr std::array<int, 7> ionianScale = { 0, 2, 4, 5, 7, 9, 11 };
    constexpr std::array<int, 7> aeolianScale = { 0, 2, 3, 5, 7, 8, 10 };
    const std::array<int, 7>& scale = (keyMode == KeySigMode::Aeolian) ? aeolianScale : ionianScale;
    int degree = -1;
    for (int i = 0; i < 7; ++i) {
        if ((keyTonicPc + scale[i]) % 12 == rootPc) { degree = i; break; }
    }
    ChordAnalysisResult r = makeRomanResult(degree, ChordQuality::Major,
                                            rootPc, rootPc, /*hasMin7=*/true,
                                            false, false, false,
                                            keyTonicPc, keyMode);
    r.function.nextRootPc = nextRootPc;
    return r;
}

// Helper: build a diminished triad result with optional dim7.
static ChordAnalysisResult dimResult(int rootPc, int nextRootPc,
                                     bool hasDim7 = false,
                                     int keyTonicPc = 0,
                                     KeySigMode keyMode = KeySigMode::Ionian)
{
    constexpr std::array<int, 7> ionianScale = { 0, 2, 4, 5, 7, 9, 11 };
    int degree = -1;
    for (int i = 0; i < 7; ++i) {
        if ((keyTonicPc + ionianScale[i]) % 12 == rootPc) { degree = i; break; }
    }
    ChordAnalysisResult r = makeRomanResult(degree, ChordQuality::Diminished,
                                            rootPc, rootPc, /*hasMin7=*/false,
                                            false, hasDim7, false,
                                            keyTonicPc, keyMode);
    r.function.nextRootPc = nextRootPc;
    return r;
}

// ── V7/x cases ────────────────────────────────────────────────────────────────

// A7 → Dm in C major: A is a P5 above D; D is degree 1 (ii). → V7/ii
TEST(Composing_TonicizationTests, A7_to_Dm_in_CMajor_is_V7ofII)
{
    const auto r = dom7Result(/*rootPc=*/9, /*nextRootPc=*/2);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "V7/ii");
}

// E7 → Am in C major: E is a P5 above A; A is degree 5 (vi). → V7/vi
TEST(Composing_TonicizationTests, E7_to_Am_in_CMajor_is_V7ofVI)
{
    const auto r = dom7Result(/*rootPc=*/4, /*nextRootPc=*/9);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "V7/vi");
}

// D7 → G in C major: D is a P5 above G; G is degree 4 (V). → V7/V
TEST(Composing_TonicizationTests, D7_to_G_in_CMajor_is_V7ofV)
{
    const auto r = dom7Result(/*rootPc=*/2, /*nextRootPc=*/7);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "V7/V");
}

// B7 → Em in C major: B is a P5 above E; E is degree 2 (iii). → V7/iii
TEST(Composing_TonicizationTests, B7_to_Em_in_CMajor_is_V7ofIII)
{
    const auto r = dom7Result(/*rootPc=*/11, /*nextRootPc=*/4);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "V7/iii");
}

// C7 → F in C major: C is a P5 above F; F is degree 3 (IV). → V7/IV
TEST(Composing_TonicizationTests, C7_to_F_in_CMajor_is_V7ofIV)
{
    const auto r = dom7Result(/*rootPc=*/0, /*nextRootPc=*/5);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "V7/IV");
}

// G7 → C in C major: G is a P5 above C; C is degree 0 (tonic).
// Must NOT produce V7/I — plain dominant stays "V7".
TEST(Composing_TonicizationTests, G7_to_C_in_CMajor_is_V7_not_secondary)
{
    const auto r = dom7Result(/*rootPc=*/7, /*nextRootPc=*/0);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "V7");
}

// No nextRootPc: label must be the plain diatonic label (no slash suffix).
TEST(Composing_TonicizationTests, G7_with_no_nextRoot_is_V7)
{
    ChordAnalysisResult r = makeRomanResult(4, ChordQuality::Major, 7, 7, /*hasMin7=*/true);
    // nextRootPc not set → stays -1
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "V7");
}

// Non-dom7 major chord (no minor seventh) must not trigger tonicization.
// C major triad → F: missing the minor 7th, so NOT a secondary dominant.
TEST(Composing_TonicizationTests, CMajorTriad_to_F_is_not_tonicization)
{
    ChordAnalysisResult r = makeRomanResult(0, ChordQuality::Major, 0, 0, /*hasMin7=*/false);
    r.function.nextRootPc = 5; // F
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "I");
}

// ── vii°/x cases ──────────────────────────────────────────────────────────────

// C#dim → Dm in C major: C# is a semitone below D; D is degree 1 (ii). → viio/ii
TEST(Composing_TonicizationTests, Csharpdim_to_Dm_in_CMajor_is_viioOfII)
{
    // C# (rootPc=1) is chromatic in C major → degree=-1
    const auto r = dimResult(/*rootPc=*/1, /*nextRootPc=*/2);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "viio/ii");
}

// Bdim → C in C major: B is a semitone below C; C is degree 0 (tonic).
// Must NOT produce viio/I — leading tone to tonic stays "viio".
TEST(Composing_TonicizationTests, Bdim_to_C_in_CMajor_is_viio_not_secondary)
{
    const auto r = dimResult(/*rootPc=*/11, /*nextRootPc=*/0);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "viio");
}

// F#dim → Gm in C major: F# is a semitone below G; G is degree 4 (V). → viio/V
TEST(Composing_TonicizationTests, Fsharpdim_to_G_in_CMajor_is_viioOfV)
{
    const auto r = dimResult(/*rootPc=*/6, /*nextRootPc=*/7);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "viio/V");
}

// C#dim7 → Dm in C major: same as C#dim but with diminished seventh. → viio7/ii
TEST(Composing_TonicizationTests, CsharpDim7_to_Dm_in_CMajor_is_viio7OfII)
{
    const auto r = dimResult(/*rootPc=*/1, /*nextRootPc=*/2, /*hasDim7=*/true);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "viio7/ii");
}

// ── Augmented Sixth Chord Label Tests ──────────────────────────────────────
//
// ChordAnalysisResult objects are built manually to simulate what analyzeChord()
// produces when TPC data is present:
//   - SharpThirteenth set (F# spelling, TPC delta +10 from Ab root) — aug6 family
//   - MinorSeventh set (Gb spelling, TPC delta -2 from Ab root)   — dom7 / tritone sub
//
// In all cases: root = ♭6̂ of key = (keyTonicPc + 8) % 12
//               key  = C major (keyTonicPc=0) unless stated otherwise.

/// Build a ChordAnalysisResult for an augmented sixth chord family.
/// SharpThirteenth is always set (F# spelling, TPC delta +10 from root).
/// Additional parameters control the specific type (It/Fr/Ger).
static ChordAnalysisResult aug6Result(bool hasSharpEleventh = false,
                                      bool naturalFifthPresentParam = false,
                                      int keyTonicPc = 0,
                                      KeySigMode keyMode = KeySigMode::Ionian)
{
    const int rootPc = (keyTonicPc + 8) % 12;    // ♭6̂ of the key
    ChordAnalysisResult r;
    r.function.degree               = -1;         // ♭6 is non-diatonic in Ionian
    r.identity.quality              = ChordQuality::Major;
    r.identity.rootPc               = rootPc;
    r.identity.bassPc               = rootPc;
    r.identity.naturalFifthPresent  = naturalFifthPresentParam;
    setExtension(r.identity.extensions, Extension::SharpThirteenth); // aug6 spelling
    if (hasSharpEleventh)
        setExtension(r.identity.extensions, Extension::SharpEleventh);
    r.function.keyTonicPc           = keyTonicPc;
    r.function.keyMode              = keyMode;
    return r;
}

// ── Italian +6 ────────────────────────────────────────────────────────────────

// Ab-C-F# in C major (no P5, no French tone) → It+6
TEST(Composing_AugmentedSixthTests, Italian_CMajor)
{
    const auto r = aug6Result(/*hasSharpEleventh=*/false, /*naturalFifthPresent=*/false);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "It+6");
}

// Same in C minor (Aeolian): same pitch classes, same result
TEST(Composing_AugmentedSixthTests, Italian_CMinor)
{
    const auto r = aug6Result(false, false, 0, KeySigMode::Aeolian);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "It+6");
}

// ── French +6 ─────────────────────────────────────────────────────────────────

// Ab-C-D-F# in C major (SharpEleventh = D spelled sharply above Ab) → Fr+6
TEST(Composing_AugmentedSixthTests, French_CMajor)
{
    const auto r = aug6Result(/*hasSharpEleventh=*/true, /*naturalFifthPresent=*/false);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "Fr+6");
}

// ── German +6 ─────────────────────────────────────────────────────────────────

// Ab-C-Eb-F# in C major (P5 = Eb present, F# spelling) → Ger+6
TEST(Composing_AugmentedSixthTests, German_CMajor)
{
    const auto r = aug6Result(/*hasSharpEleventh=*/false, /*naturalFifthPresent=*/true);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "Ger+6");
}

// Same in C minor
TEST(Composing_AugmentedSixthTests, German_CMinor)
{
    const auto r = aug6Result(false, true, 0, KeySigMode::Aeolian);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "Ger+6");
}

// ── Ger+6 vs tritone-sub dominant — TPC spelling distinction ──────────────────

// Ab-C-Eb-Gb (Ab dominant seventh, Gb spelling = min7, TPC delta -2): → NOT Ger+6
// Expected: chromatic Roman numeral "bVI7" (SharpThirteenth is NOT set)
TEST(Composing_AugmentedSixthTests, TritoneSubDominant_NotGerPlus6)
{
    ChordAnalysisResult r;
    r.function.degree               = -1;
    r.identity.quality              = ChordQuality::Major;
    r.identity.rootPc               = 8;   // Ab
    r.identity.bassPc               = 8;
    r.identity.naturalFifthPresent  = true; // Eb present
    setExtension(r.identity.extensions, Extension::MinorSeventh); // Gb spelling
    r.function.keyTonicPc           = 0;
    r.function.keyMode              = KeySigMode::Ionian;
    // SharpThirteenth NOT set → aug6 detection suppressed → chromatic Roman numeral
    EXPECT_NE(ChordSymbolFormatter::formatRomanNumeral(r), "Ger+6");
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "bVI7");
}

// Ab-C-Eb-F# (Ger+6, F# spelling = SharpThirteenth, TPC delta +10): → Ger+6
TEST(Composing_AugmentedSixthTests, GermanSpelling_IsGerPlus6)
{
    const auto r = aug6Result(false, /*naturalFifthPresent=*/true);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "Ger+6");
}

// ── Non-aug6 chords must not produce aug6 labels ──────────────────────────────

// Plain C major triad (root=0, not ♭6̂) → "I", not any aug6 label
TEST(Composing_AugmentedSixthTests, PlainMajorChord_NotAugSixth)
{
    const auto r = makeRomanResult(0, ChordQuality::Major);
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(r), "I");
}

// Plain minor chord at ♭6̂ position (quality=Minor, no SharpThirteenth) → no aug6
// Expected: chromatic Roman numeral "bVI" (minor quality at ♭6)
TEST(Composing_AugmentedSixthTests, MinorChordOnFlatSixth_NotAugSixth)
{
    // Ab minor triad in C major — minor quality, no SharpThirteenth
    ChordAnalysisResult r;
    r.function.degree       = -1;
    r.identity.quality      = ChordQuality::Minor;
    r.identity.rootPc       = 8;  // Ab
    r.identity.bassPc       = 8;
    r.function.keyTonicPc   = 0;
    r.function.keyMode      = KeySigMode::Ionian;
    // Minor quality → detection requires Major quality; this must NOT produce aug6
    const std::string label = ChordSymbolFormatter::formatRomanNumeral(r);
    EXPECT_NE(label, "It+6");
    EXPECT_NE(label, "Fr+6");
    EXPECT_NE(label, "Ger+6");
}


// ═══════════════════════════════════════════════════════════════════
// Pedal point detection (§5.12)
// Two-pass logic: if the bass is NOT a chord tone of the Pass-1 winner,
// re-analyze upper voices only; if Pass-2 confidence ≥ threshold and
// ≥2 distinct upper PCs, the result is flagged as a pedal point.
//
// Bass weight must exceed bassPassingToneMinWeightFraction×totalWeight
// (default 5 %) to be recognised as the structural bass; tests that
// need a low-weight pedal bass use weight=0.2 with upper voices at 1.0
// (0.2 / 3.2 = 6.25 % > 5 %).
// ═══════════════════════════════════════════════════════════════════

// Bass IS the root of the winning chord — interval=0 → always a chord tone.
TEST(Composing_PedalPointTests, BassIsChordTone_NoPedalDetected)
{
    const auto results = kAnalyzer.analyzeChord(tones({ 60, 64, 67 }), 0, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_FALSE(results.front().identity.isPedalPoint);
}

// Eb3 is the minor 7th of F dominant 7th (interval 10 from F, MinorSeventh flag set).
// isBassChordTone checks the extension flags → chord tone → no pedal.
TEST(Composing_PedalPointTests, F13overEb_BassIsChordTone_NoPedalDetected)
{
    // Eb3=51, F4=65, A4=69, C5=72  →  Fdom7/Eb
    const auto results = kAnalyzer.analyzeChord(tones({ 51, 65, 69, 72 }), 0, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_FALSE(results.front().identity.isPedalPoint);
}

// C3 at low weight under G–B–D: C is not a chord tone of G major (interval=5).
// Pass-2 finds G major with high confidence → pedal confirmed.
TEST(Composing_PedalPointTests, SustainedBassNotInUpperVoiceChord_PedalDetected)
{
    const auto ts = weightedTones({ { 48, 0.2 }, { 67, 1.0 }, { 71, 1.0 }, { 74, 1.0 } });
    const auto results = kAnalyzer.analyzeChord(ts, 0, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_TRUE(results.front().identity.isPedalPoint);
    EXPECT_EQ(results.front().identity.pedalBassPc, 0);   // C pedal
    EXPECT_EQ(results.front().identity.rootPc, 7);        // G major above
}

// G3 at low weight under D–F–A: G is not a chord tone of D minor (interval=5, not 3 or 7).
// Classic dominant-pedal scenario.
TEST(Composing_PedalPointTests, DominantPedal_Detected)
{
    const auto ts = weightedTones({ { 55, 0.2 }, { 62, 1.0 }, { 65, 1.0 }, { 69, 1.0 } });
    const auto results = kAnalyzer.analyzeChord(ts, 0, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_TRUE(results.front().identity.isPedalPoint);
    EXPECT_EQ(results.front().identity.pedalBassPc, 7);   // G pedal
    EXPECT_EQ(results.front().identity.rootPc, 2);        // Dm above
}

// C3 at low weight under A major (A4–C#5–E5 at full weight).
// C is not a chord tone of A major (interval=(0-9+12)%12=3, not 4 or 7) → pedal detected.
// Note: Eb-G-Bb was the first design choice but Cm7 (C-Eb-G-Bb) wins Pass 1 via the
// full bass-root bonus, making the bass appear to be the minor-7th chord tone.
TEST(Composing_PedalPointTests, TonicPedal_Detected)
{
    // C3=48, A4=69, C#5=73, E5=76
    const auto ts = weightedTones({ { 48, 0.2 }, { 69, 1.0 }, { 73, 1.0 }, { 76, 1.0 } });
    const auto results = kAnalyzer.analyzeChord(ts, 0, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_TRUE(results.front().identity.isPedalPoint);
    EXPECT_EQ(results.front().identity.pedalBassPc, 0);   // C pedal
    EXPECT_EQ(results.front().identity.rootPc, 9);        // A major above
}

// pedalConfidenceThreshold=0.0 disables the two-pass check entirely (guard in analyzeChord).
// Same voicing as SustainedBassNotInUpperVoiceChord_PedalDetected but pedal suppressed.
TEST(Composing_PedalPointTests, PedalDetection_DisabledByZeroThreshold)
{
    ChordAnalyzerPreferences prefs;
    prefs.pedalConfidenceThreshold = 0.0;
    const auto ts = weightedTones({ { 48, 0.2 }, { 67, 1.0 }, { 71, 1.0 }, { 74, 1.0 } });
    const auto results = kAnalyzer.analyzeChord(ts, 0, KeySigMode::Ionian, nullptr, prefs);
    ASSERT_FALSE(results.empty());
    EXPECT_FALSE(results.front().identity.isPedalPoint);
}

// C major in first inversion: E3 is the bass note.
// isBassChordTone(bassPc=4, rootPc=0, Major): interval=4 (M3) → chord tone → no pedal.
TEST(Composing_PedalPointTests, SustainedInnerVoiceIsChordTone_NoPedalDetected)
{
    // E3=52 (bass), C4=60, E4=64, G4=67
    const auto results = kAnalyzer.analyzeChord(tones({ 52, 60, 64, 67 }), 0, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_FALSE(results.front().identity.isPedalPoint);
}

// Same voicing as SustainedBassNotInUpperVoiceChord_PedalDetected but
// pedalConfidenceThreshold=0.99 — G major's confidence (≈0.97) stays below this bar.
TEST(Composing_PedalPointTests, LowConfidenceUpperVoices_NoPedalDetected)
{
    ChordAnalyzerPreferences prefs;
    prefs.pedalConfidenceThreshold = 0.99;
    const auto ts = weightedTones({ { 48, 0.2 }, { 67, 1.0 }, { 71, 1.0 }, { 74, 1.0 } });
    const auto results = kAnalyzer.analyzeChord(ts, 0, KeySigMode::Ionian, nullptr, prefs);
    ASSERT_FALSE(results.empty());
    EXPECT_FALSE(results.front().identity.isPedalPoint);
}

// ── Extension threshold preset tests ──────────────────────────────────────────
//
// Jazz ninths consistently appear at pcWeight 0.12–0.19 (below the conservative
// 0.20 standard threshold).  The Jazz preset lowers extensionThreshold to 0.12
// to detect them; Standard/Baroque keep 0.20 to suppress counterpoint passing tones.

// Am7 with a lightly-voiced ninth (pcWeight ≈ 0.15, between 0.12 and 0.20).
// Jazz preset (extensionThreshold=0.12): ninth detected → Am9.
TEST(Composing_ExtensionThresholdTests, JazzPreset_LightlyVoicedNinth_Detected)
{
    // A4=69 (root, strong), C5=72 (m3), E5=76 (P5), G5=79 (m7), B5=83 (ninth — light)
    // Weights: Root=1.0, m3=0.70, P5=0.70, m7=0.50, ninth=0.15.
    // pcWeight[B] = max(0.1, 0.15) = 0.15.  Jazz threshold 0.12: 0.15 > 0.12 → detected.
    const auto ts = weightedTones({
        { 69, 1.0 },   // A  — root
        { 72, 0.70 },  // C  — minor third
        { 76, 0.70 },  // E  — perfect fifth
        { 79, 0.50 },  // G  — minor seventh
        { 83, 0.15 },  // B  — ninth (lightly voiced, between jazz 0.12 and standard 0.20)
    });

    ChordAnalyzerPreferences jazzPrefs;
    jazzPrefs.extensionThreshold = 0.12;  // Jazz preset value

    const auto results = kAnalyzer.analyzeChord(ts, 0, KeySigMode::Ionian, nullptr, jazzPrefs);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 9);  // A
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Minor);
    EXPECT_TRUE(hasExtension(results.front().identity.extensions, Extension::NaturalNinth))
        << "Jazz preset (extensionThreshold=0.12) should detect lightly-voiced ninth";
}

// Same voicing: Standard preset (extensionThreshold=0.20) must NOT detect the ninth.
TEST(Composing_ExtensionThresholdTests, StandardPreset_LightlyVoicedNinth_NotDetected)
{
    // Same tones as above.
    const auto ts = weightedTones({
        { 69, 1.0 },
        { 72, 0.70 },
        { 76, 0.70 },
        { 79, 0.50 },
        { 83, 0.15 },  // ninth — pcWeight 0.15 < standard threshold 0.20 → not detected
    });

    // Standard preset uses default extensionThreshold = 0.20.
    ChordAnalyzerPreferences standardPrefs;  // extensionThreshold = 0.20 by default

    const auto results = kAnalyzer.analyzeChord(ts, 0, KeySigMode::Ionian, nullptr, standardPrefs);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 9);  // A
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Minor);
    EXPECT_FALSE(hasExtension(results.front().identity.extensions, Extension::NaturalNinth))
        << "Standard preset (extensionThreshold=0.20) should NOT detect lightly-voiced ninth";
}

// ── Enharmonic root spelling (TPC-driven) ─────────────────────────────────────
//
// Root spelling must use the note's TPC when available, not the key signature
// alone.  This fixes spurious A#/D#/G# roots in flat-key or neutral-key contexts
// where the underlying note is spelled Bb/Eb/Ab in the score.
//
// TPC reference (MuseScore circle-of-fifths encoding):
//   TPC  9 = Gb,  10 = Db,  11 = Ab,  12 = Eb,  13 = Bb
//   TPC 14 = F,   15 = C,   16 = G,   17 = D,   18 = A,   19 = E,   20 = B
//   TPC 21 = F#,  22 = C#,  23 = G#,  24 = D#,  25 = A#
//
// Session 23 identified 18 wrong A# roots in sun-bear-osaka (C-major context),
// 6 wrong D# bass notes in take-five (Eb-major context), and similar clusters.
// ─────────────────────────────────────────────────────────────────────────────

// Bb triad in C major — TPC=13 (Bb) on root note → should format as "Bb", not "A#"
TEST(Composing_EnharmonicSpellingTests, BbRootInCMajorSpellsAsBb)
{
    // Bb2(TPC=13) D3(TPC=17) F3(TPC=14) — Bb major triad, bass = Bb2
    const auto ts = tonesWithTpc({
        { 46, 13 },  // Bb2 — bass, root
        { 50, 17 },  // D3
        { 53, 14 },  // F3
    });
    const auto results = kAnalyzer.analyzeChord(ts, 0, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 10);
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(results.front(), 0), "Bb")
        << "Bb root (TPC=13) in C major must format as Bb, not A#";
}

// Eb triad in C major — TPC=12 (Eb) on root note → should format as "Eb", not "D#"
TEST(Composing_EnharmonicSpellingTests, EbRootInCMajorSpellsAsEb)
{
    // Eb2(TPC=12) G2(TPC=16) Bb2(TPC=13) — Eb major triad, bass = Eb2
    const auto ts = tonesWithTpc({
        { 39, 12 },  // Eb2 — bass, root
        { 43, 16 },  // G2
        { 46, 13 },  // Bb2
    });
    const auto results = kAnalyzer.analyzeChord(ts, 0, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 3);
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(results.front(), 0), "Eb")
        << "Eb root (TPC=12) in C major must format as Eb, not D#";
}

// Ab triad in C major — TPC=11 (Ab) on root note → should format as "Ab", not "G#"
TEST(Composing_EnharmonicSpellingTests, AbRootInCMajorSpellsAsAb)
{
    // Ab1(TPC=11) C2(TPC=15) Eb2(TPC=12) — Ab major triad, bass = Ab1
    const auto ts = tonesWithTpc({
        { 32, 11 },  // Ab1 — bass, root
        { 36, 15 },  // C2
        { 39, 12 },  // Eb2
    });
    const auto results = kAnalyzer.analyzeChord(ts, 0, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 8);
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(results.front(), 0), "Ab")
        << "Ab root (TPC=11) in C major must format as Ab, not G#";
}

// Bbsus4 in C major — the sun-bear-osaka pattern (A#sus → Bbsus)
TEST(Composing_EnharmonicSpellingTests, BbSus4InCMajorSpellsAsBbsus)
{
    // Bbsus4 = {Bb, Eb, F} — intervals {0, 5, 7} from root Bb.
    // Bb2(TPC=13) Eb3(TPC=12) F3(TPC=14)
    const auto ts = tonesWithTpc({
        { 46, 13 },  // Bb2 — bass, root
        { 51, 12 },  // Eb3 (sus4)
        { 53, 14 },  // F3 (fifth)
    });
    const auto results = kAnalyzer.analyzeChord(ts, 0, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 10);  // Bb
    const std::string sym = ChordSymbolFormatter::formatSymbol(results.front(), 0);
    EXPECT_NE(sym.substr(0, 2), "A#")
        << "Root Bb (TPC=13) in C major must not format as A#; got: " << sym;
    EXPECT_EQ(sym.substr(0, 2), "Bb")
        << "Root Bb (TPC=13) in C major must format starting with Bb; got: " << sym;
}

// Sharp root preserved in sharp-key context — G# in E major stays G#
TEST(Composing_EnharmonicSpellingTests, GsharpRootInSharpKeyStaysGsharp)
{
    // G#2(TPC=23) B2(TPC=20) D#3(TPC=24) — G# minor triad in E major (keyFifths=4)
    const auto ts = tonesWithTpc({
        { 44, 23 },  // G#2 — bass, root
        { 47, 20 },  // B2
        { 51, 24 },  // D#3
    });
    const auto results = kAnalyzer.analyzeChord(ts, 4, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 8);   // G#
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(results.front(), 4), "G#m")
        << "G# root (TPC=23) in E major (keyFifths=4) must remain G#m, not Abm";
}

// Fallback: when TPC is unknown (tpc=-1), key signature governs flat/sharp choice.
// Flat key (keyFifths=-3) → flat spelling, even with no TPC data.
TEST(Composing_EnharmonicSpellingTests, NoTpcFallsBackToKeySignatureFlat)
{
    // Same as KeepsFlatBassSpellingInFlatKey but now testing the root path:
    // Bb(pc=10) as root in Bb minor (keyFifths=-5), no TPC supplied.
    // pitchClassNameFromTpc(10, -1, -5) → falls back to pitchClassName(10, -5) → FLAT_NAMES[10] = "Bb"
    const auto ts = tonesWithTpc({
        { 46, -1 },  // Bb2 — no TPC supplied → tpc=-1
        { 50, -1 },  // D3
        { 53, -1 },  // F3
    });
    const auto results = kAnalyzer.analyzeChord(ts, -5, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 10);
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(results.front(), -5), "Bb")
        << "With no TPC, flat key (keyFifths=-5) must spell pc=10 as Bb";
}

// Key-signature override: sharp TPC in a flat-key context must still spell flat.
// Covers score-data misspellings (e.g. D# where Eb is intended in C Dorian).
TEST(Composing_EnharmonicSpellingTests, SharpTpcInFlatKeyUsesKeySignature)
{
    // D#2(TPC=24) in C Dorian (keyFifths=-2) — score mistakenly uses sharp TPC=24
    // instead of flat TPC=12 (Eb).  Key signature must win: root should be "Eb" not "D#".
    // Chord: D#/Eb (pc=3) + G (pc=7, major 3rd) + Bb (pc=10, perfect 5th) = major triad.
    const auto ts = tonesWithTpc({
        { 39, 24 },  // D#2 — bass, root; TPC=24 (D#, sharp range — misspelled Eb)
        { 43, 16 },  // G2  (TPC=16, major 3rd from Eb)
        { 46, 13 },  // Bb2 (TPC=13, perfect 5th from Eb)
    });
    const auto results = kAnalyzer.analyzeChord(ts, -2, KeySigMode::Dorian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 3);   // pc=3 = D#/Eb
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(results.front(), -2), "Eb")
        << "Sharp TPC (24=D#) in flat key (keyFifths=-2) must yield Eb, not D#";
}

// ── B → Cb / E → Fb enharmonic spelling in very flat key contexts ─────────────
//
// Session 24: In keys with 5+ flats (Db, Gb, Cb, Fb) the note B natural is
// spelled Cb, and in 6+ flat keys (Gb, Cb, Fb) E natural is spelled Fb.
// The standard flat-key name tables use "B" and "E" for those pitch classes;
// pitchClassNameFromTpc() must detect the TPC evidence and return the flat
// enharmonic instead.
//
// TPC encoding: the test file uses +1 offset from MuseScore's internal enum.
//   B natural = TPC 20 (test encoding); MuseScore internal TPC_B = 19.
//   E natural = TPC 19 (test encoding); MuseScore internal TPC_E = 18.
// pitchClassNameFromTpc() handles both via pc+TPC disambiguation.
// ─────────────────────────────────────────────────────────────────────────────

// B minor triad (B D F#) in Db major (keyFifths=-5, 5 flats).
// Root B natural (TPC=20, pc=11) must format as "Cb" not "B".
TEST(Composing_EnharmonicSpellingTests, BNaturalIn5FlatKeySpellsAsCb)
{
    // B2(TPC=20) D3(TPC=17) F#3(TPC=21) — B minor triad, keyFifths=-5 (Db major)
    const auto ts = tonesWithTpc({
        { 47, 20 },  // B2 — bass, root (TPC=20 = B natural, test encoding)
        { 50, 17 },  // D3 (TPC=17 = D)
        { 54, 21 },  // F#3 (TPC=21 = F#)
    });
    const auto results = kAnalyzer.analyzeChord(ts, -5, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 11);  // pc=11 = B/Cb
    const std::string sym = ChordSymbolFormatter::formatSymbol(results.front(), -5);
    EXPECT_EQ(sym.substr(0, 2), "Cb")
        << "B natural (TPC=20) in Db major (keyFifths=-5) must spell as Cb; got: " << sym;
}

// E major triad (E G# B) in Gb major (keyFifths=-6, 6 flats).
// Root E natural (TPC=19, pc=4) must format as "Fb" not "E".
TEST(Composing_EnharmonicSpellingTests, ENaturalIn6FlatKeySpellsAsFb)
{
    // E2(TPC=19) G#2(TPC=23) B2(TPC=20) — E major triad, keyFifths=-6 (Gb major)
    const auto ts = tonesWithTpc({
        { 40, 19 },  // E2 — bass, root (TPC=19 = E natural, test encoding)
        { 44, 23 },  // G#2 (TPC=23 = G#)
        { 47, 20 },  // B2 (TPC=20 = B natural)
    });
    const auto results = kAnalyzer.analyzeChord(ts, -6, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 4);   // pc=4 = E/Fb
    const std::string sym = ChordSymbolFormatter::formatSymbol(results.front(), -6);
    EXPECT_EQ(sym.substr(0, 2), "Fb")
        << "E natural (TPC=19) in Gb major (keyFifths=-6) must spell as Fb; got: " << sym;
}

// B minor triad (B D F#) in Eb minor (keyFifths=-3).
// Root B natural (TPC=20) in a SHALLOW flat key must stay "B", not "Cb".
// Only 5+ flats trigger the B→Cb conversion.
TEST(Composing_EnharmonicSpellingTests, BNaturalIn3FlatKeyStaysB)
{
    // B2(TPC=20) D3(TPC=17) F#3(TPC=21) — B minor triad, keyFifths=-3 (Eb minor)
    const auto ts = tonesWithTpc({
        { 47, 20 },  // B2 — bass, root
        { 50, 17 },  // D3
        { 54, 21 },  // F#3
    });
    const auto results = kAnalyzer.analyzeChord(ts, -3, KeySigMode::Aeolian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 11);
    const std::string sym = ChordSymbolFormatter::formatSymbol(results.front(), -3);
    EXPECT_EQ(sym[0], 'B')
        << "B natural (TPC=20) in Eb minor (keyFifths=-3) must remain B; got: " << sym;
}

// ── D#/G#/A# → Eb/Ab/Bb normalisation in neutral and mildly-sharp keys ─────────
//
// Session 26 (Step 12): In C major (keyFifths=0) and mildly-sharp key contexts,
// a sharp-spelled accidental (D#, G#, A# TPC ≥ 20) must be normalised to its
// conventional flat chord-symbol name (Eb, Ab, Bb).  The threshold for each PC is
// the key signature where the sharp becomes diatonic:
//   D# (pc=3)  diatonic at E major (keyFifths=4) → Eb in C/G/D/A major
//   G# (pc=8)  diatonic at A major (keyFifths=3) → Ab in C/G/D major
//   A# (pc=10) diatonic at B major (keyFifths=5) → Bb in C through 4 sharps
//
// Regression guard: D# spelling (TPC=24) must survive in keys where D# is diatonic.
// ──────────────────────────────────────────────────────────────────────────────────

// D# (TPC=24) as bass note in C major (keyFifths=0) must become Eb in slash notation.
// Uses Bb/Eb (Bb major with D#/Eb bass) — a clear slash chord where D# is the bass.
// Mirrors the Billy Boy "Em7add11/D#" → "Em7add11/Eb" fix (bass spelling normalisation).
TEST(Composing_EnharmonicSpellingTests, DSharpBassInNeutralKeyBecomesEb)
{
    // Bb major chord with D#2/Eb2 bass (TPC=24, sharp-spelled):
    // D#2(TPC=24) Bb3(TPC=13) D4(TPC=17) F4(TPC=14)
    const auto ts = tonesWithTpc({
        { 39, 24 },  // D#2/Eb2 — bass (TPC=24, sharp-spelled D#)
        { 58, 13 },  // Bb3 — root
        { 62, 17 },  // D4
        { 65, 14 },  // F4
    });
    const auto results = kAnalyzer.analyzeChord(ts, 0, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    const std::string sym = ChordSymbolFormatter::formatSymbol(results.front(), 0);
    EXPECT_EQ(sym.find("D#"), std::string::npos)
        << "D# bass (TPC=24) in C major must not produce D# in slash; got: " << sym;
    EXPECT_NE(sym.find("Eb"), std::string::npos)
        << "D# bass (TPC=24) in C major must be spelled Eb in slash; got: " << sym;
}

// D# (TPC=24) as root in A minor (keyFifths=0) must format as Eb.
// Mirrors the Billy Boy "D#Maj7" → "EbMaj7" fix.
TEST(Composing_EnharmonicSpellingTests, DSharpRootInNeutralKeyBecomesEb)
{
    // Eb major triad: D#2/Eb2 (TPC=24) + G2 (TPC=16) + Bb2 (TPC=13) — same as Eb major
    const auto ts = tonesWithTpc({
        { 39, 24 },  // D#2/Eb2 — root, bass (TPC=24, sharp-spelled D#)
        { 43, 16 },  // G2
        { 46, 13 },  // Bb2
    });
    const auto results = kAnalyzer.analyzeChord(ts, 0, KeySigMode::Aeolian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 3);
    const std::string sym = ChordSymbolFormatter::formatSymbol(results.front(), 0);
    EXPECT_EQ(sym.substr(0, 2), "Eb")
        << "D# root (TPC=24) in A minor (keyFifths=0) must spell as Eb; got: " << sym;
}

// D# remains D# in E major (keyFifths=4) where it is a diatonic note.
TEST(Composing_EnharmonicSpellingTests, DSharpSurvivesInEMajorKey)
{
    // D# minor triad (D# F# A#) in E major (keyFifths=4) — all diatonic.
    const auto ts = tonesWithTpc({
        { 39, 24 },  // D#2 — root, bass (TPC=24)
        { 42, 21 },  // F#2 (TPC=21)
        { 45, 25 },  // A#2 (TPC=25)
    });
    const auto results = kAnalyzer.analyzeChord(ts, 4, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 3);
    const std::string sym = ChordSymbolFormatter::formatSymbol(results.front(), 4);
    EXPECT_EQ(sym.substr(0, 2), "D#")
        << "D# (TPC=24) in E major (keyFifths=4) must remain D#; got: " << sym;
}

// ── Sus4 requires a detectable perfect fourth ─────────────────────────────────
//
// Session 24 (Bug A): a Sus4 template (quality Suspended4 with interval 5 = P4)
// must not win when the P4 is absent or sub-threshold.  The P4 is the defining
// suspension tone; without it the chord sounds augmented or altered, not suspended.
//
// structuralPenalties() now applies kSus4MissingFourth when
//   pcWeight[fourthPc] < extThreshold.
// ─────────────────────────────────────────────────────────────────────────────

// Csus4#5 candidate over E bass (root ≠ bass): C aug5 (G#) and m7 (Bb) are present,
// but P4 (F) is very faint.  Bass=E, root=C → no bass-root bonus for Sus4#5/C.
// The Sus4 penalty plus the non-bass penalty together must prevent Sus4 from winning.
//
// Voicing: E3(bass,0.80) F3(P4,0.04) G#3(aug5,0.80) Bb3(m7,0.70) C4(root,1.00)
// Sus4#5 from C = {C,F,G#,Bb} = intervals {0,5,8,10}.  P4=F weight=0.04 < 0.20.
TEST(Composing_Sus4RequiresFourthTests, Sus4SharpFiveNonBassRoot_SubThresholdFourth_NotSus4)
{
    const auto ts = weightedTones({
        { 52, 0.80 },  // E3 — bass (lowest pitch)
        { 53, 0.04 },  // F3 — P4 from C root (sub-threshold: 0.04 < 0.20 Standard)
        { 56, 0.80 },  // G#3 — aug5 from C root (interval 8)
        { 58, 0.70 },  // Bb3 — m7 from C root (interval 10)
        { 60, 1.00 },  // C4 — root
    });
    // Standard preset (extThreshold=0.20).  Root=C (pc=0), bass=E (pc=4) → no bass bonus for Sus4/C.
    const auto results = kAnalyzer.analyzeChord(ts, 0, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_NE(results.front().identity.quality, ChordQuality::Suspended4)
        << "P4 weight 0.04 sub-threshold + non-bass root: Sus4#5/C must not win";
}

// Same scenario, Jazz preset (extThreshold=0.12): P4 barely above Jazz threshold (0.13).
// Sus4 should be allowed (no penalty).
TEST(Composing_Sus4RequiresFourthTests, FourthAboveJazzThreshold_JazzPreset_CanBeSus4)
{
    const auto ts = weightedTones({
        { 52, 1.00 },  // E3 — root, bass
        { 57, 0.13 },  // A3 — P4 (0.13 > 0.12 Jazz; above threshold)
        { 60, 0.80 },  // C4 — aug5
        { 62, 0.50 },  // D4 — m7
    });
    ChordAnalyzerPreferences jazzPrefs;
    jazzPrefs.extensionThreshold = 0.12;
    const auto results = kAnalyzer.analyzeChord(ts, 0, KeySigMode::Ionian, nullptr, jazzPrefs);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Suspended4)
        << "P4 weight 0.13 ≥ Jazz threshold 0.12; Sus4 must not be penalised";
}
