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

using namespace mu::composing::analysis;

namespace {

const RuleBasedChordAnalyzer kAnalyzer{};


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
                                    bool hasDim7 = false, bool hasAdd6 = false,
                                    int keyTonicPc = 0,
                                    KeySigMode keyMode = KeySigMode::Ionian)
{
    ChordAnalysisResult r;
    r.function.degree               = degree;
    r.identity.quality              = quality;
    r.identity.rootPc               = rootPc;
    r.identity.bassPc               = bassPc;
    if (hasMin7) setExtension(r.identity.extensions, Extension::MinorSeventh);
    if (hasMaj7) setExtension(r.identity.extensions, Extension::MajorSeventh);
    if (hasDim7) setExtension(r.identity.extensions, Extension::DiminishedSeventh);
    if (hasAdd6) setExtension(r.identity.extensions, Extension::AddedSixth);
    r.function.keyTonicPc           = keyTonicPc;
    r.function.keyMode              = keyMode;
    return r;
}

const ChordAnalysisResult* findCandidate(const std::vector<ChordAnalysisResult>& results,
                                         int rootPc,
                                         ChordQuality quality,
                                         bool hasMin7 = false)
{
    for (const auto& result : results) {
        if (result.identity.rootPc != rootPc || result.identity.quality != quality) {
            continue;
        }
        if (hasMin7 && !hasExtension(result.identity.extensions, Extension::MinorSeventh)) {
            continue;
        }
        return &result;
    }
    return nullptr;
}

ChordAnalyzerPreferences bassSupportPrefs()
{
    ChordAnalyzerPreferences prefs;
    prefs.bassNoteRootBonus = 1.0;
    prefs.bassRootThirdOnlyMultiplier = 0.3;
    prefs.bassRootAloneMultiplier = 0.1;
    return prefs;
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

TEST(Composing_ChordAnalyzerTests, JazzMode_KeepsBassRootBonus)
{
    const auto withoutJazz = kAnalyzer.analyzeChord(tones({ 60, 64, 67 }), 0, KeySigMode::Ionian);

    ChordTemporalContext jazzCtx;
    jazzCtx.jazzMode = true;
    const auto withJazz = kAnalyzer.analyzeChord(tones({ 60, 64, 67 }), 0, KeySigMode::Ionian, &jazzCtx);

    ASSERT_FALSE(withoutJazz.empty());
    ASSERT_FALSE(withJazz.empty());
    EXPECT_EQ(withoutJazz.front().identity.rootPc, 0);
    EXPECT_EQ(withJazz.front().identity.rootPc, 0);
    EXPECT_NEAR(withoutJazz.front().identity.score, withJazz.front().identity.score,
                1e-9);
}

TEST(Composing_ChordAnalyzerTests, JazzMode_DoesNotChangeDominantGuideToneReading)
{
    const auto withoutJazz = kAnalyzer.analyzeChord(tones({ 52, 55, 58, 60 }), 0, KeySigMode::Ionian);

    ChordTemporalContext jazzCtx;
    jazzCtx.jazzMode = true;
    const auto withJazz = kAnalyzer.analyzeChord(tones({ 52, 55, 58, 60 }), 0, KeySigMode::Ionian, &jazzCtx);

    const auto* dominantWithoutJazz = findCandidate(withoutJazz, 0, ChordQuality::Major, true);
    const auto* dominantWithJazz = findCandidate(withJazz, 0, ChordQuality::Major, true);

    ASSERT_NE(dominantWithoutJazz, nullptr);
    ASSERT_NE(dominantWithJazz, nullptr);
    EXPECT_NEAR(dominantWithJazz->identity.score, dominantWithoutJazz->identity.score,
                1e-9);
}

TEST(Composing_ChordAnalyzerTests, JazzMode_DoesNotBoostMinorSeventhReading)
{
    const auto withoutJazz = kAnalyzer.analyzeChord(tones({ 62, 65, 69, 72 }), 0, KeySigMode::Ionian);

    ChordTemporalContext jazzCtx;
    jazzCtx.jazzMode = true;
    const auto withJazz = kAnalyzer.analyzeChord(tones({ 62, 65, 69, 72 }), 0, KeySigMode::Ionian, &jazzCtx);

    const auto* minorWithoutJazz = findCandidate(withoutJazz, 2, ChordQuality::Minor, true);
    const auto* minorWithJazz = findCandidate(withJazz, 2, ChordQuality::Minor, true);

    ASSERT_NE(minorWithoutJazz, nullptr);
    ASSERT_NE(minorWithJazz, nullptr);
    EXPECT_NEAR(minorWithJazz->identity.score, minorWithoutJazz->identity.score,
                1e-9);
}

TEST(Composing_ChordAnalyzerTests, JazzMode_DoesNotBoostDiminishedReading)
{
    const auto withoutJazz = kAnalyzer.analyzeChord(tones({ 59, 62, 65, 68 }), 0, KeySigMode::Ionian);

    ChordTemporalContext jazzCtx;
    jazzCtx.jazzMode = true;
    const auto withJazz = kAnalyzer.analyzeChord(tones({ 59, 62, 65, 68 }), 0, KeySigMode::Ionian, &jazzCtx);

    const auto* diminishedWithoutJazz = findCandidate(withoutJazz, 11, ChordQuality::Diminished);
    const auto* diminishedWithJazz = findCandidate(withJazz, 11, ChordQuality::Diminished);

    ASSERT_NE(diminishedWithoutJazz, nullptr);
    ASSERT_NE(diminishedWithJazz, nullptr);
    EXPECT_NEAR(diminishedWithJazz->identity.score, diminishedWithoutJazz->identity.score,
                1e-9);
}

TEST(Composing_ChordAnalyzerTests, JazzMode_DoesNotPenalizeSuspendedFourthReadings)
{
    const auto withoutJazz = kAnalyzer.analyzeChord(tones({ 48, 53, 55, 58 }), 0, KeySigMode::Ionian);

    ChordTemporalContext jazzCtx;
    jazzCtx.jazzMode = true;
    const auto withJazz = kAnalyzer.analyzeChord(tones({ 48, 53, 55, 58 }), 0, KeySigMode::Ionian, &jazzCtx);

    const auto* susWithoutJazz = findCandidate(withoutJazz, 0, ChordQuality::Suspended4);
    const auto* susWithJazz = findCandidate(withJazz, 0, ChordQuality::Suspended4);

    ASSERT_NE(susWithoutJazz, nullptr);
    ASSERT_NE(susWithJazz, nullptr);
    EXPECT_NEAR(susWithoutJazz->identity.score, susWithJazz->identity.score,
                1e-9);
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
