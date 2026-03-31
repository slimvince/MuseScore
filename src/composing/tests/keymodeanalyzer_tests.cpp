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

#include "composing/analysis/keymodeanalyzer.h"

using namespace mu::composing::analysis;

// ── Test helpers ─────────────────────────────────────────────────────────────

namespace {

KeyModeAnalyzer::PitchContext makePitch(int pitch, double durationWeight, double beatWeight, bool isBass)
{
    KeyModeAnalyzer::PitchContext p;
    p.pitch          = pitch;
    p.durationWeight = durationWeight;
    p.beatWeight     = beatWeight;
    p.isBass         = isBass;
    return p;
}

/// Build a flat pitch list: all notes equal weight, first note is bass.
std::vector<KeyModeAnalyzer::PitchContext> flatPitches(std::initializer_list<int> midiPitches)
{
    std::vector<KeyModeAnalyzer::PitchContext> out;
    out.reserve(midiPitches.size());
    bool first = true;
    for (int p : midiPitches) {
        out.push_back(makePitch(p, 1.0, 1.0, first));
        first = false;
    }
    return out;
}

} // namespace

// ── Edge cases ───────────────────────────────────────────────────────────────

TEST(Composing_KeyModeAnalyzerTests, ReturnsEmptyForNoPitches)
{
    const auto results = KeyModeAnalyzer::analyzeKeyMode({}, 0);
    EXPECT_TRUE(results.empty());
}

TEST(Composing_KeyModeAnalyzerTests, ReturnsSomethingForSinglePitch)
{
    // A single note cannot determine mode, but the function should not crash
    // and should return at least one candidate.
    const auto results = KeyModeAnalyzer::analyzeKeyMode(flatPitches({ 60 }), 0);
    EXPECT_FALSE(results.empty());
}

// ── Score ordering and result count invariants ────────────────────────────────

TEST(Composing_KeyModeAnalyzerTests, ResultsAreSortedByScoreDescending)
{
    // Use a full C major scale to generate a well-spread score distribution.
    const auto results = KeyModeAnalyzer::analyzeKeyMode(
        flatPitches({ 60, 62, 64, 65, 67, 69, 71 }), 0);

    ASSERT_FALSE(results.empty());
    for (size_t i = 1; i < results.size(); ++i) {
        EXPECT_GE(results[i - 1].score, results[i].score)
            << "Result " << i - 1 << " score=" << results[i - 1].score
            << " must be >= result " << i << " score=" << results[i].score;
    }
}

TEST(Composing_KeyModeAnalyzerTests, ReturnsAtMostThreeCandidates)
{
    const auto results = KeyModeAnalyzer::analyzeKeyMode(
        flatPitches({ 60, 62, 64, 65, 67, 69, 71 }), 0);

    EXPECT_LE(results.size(), 3u);
}

// ── Basic key identification — circle of fifths ───────────────────────────────
//
// All tests here pass the matching key signature so the key-signature path
// (lines 240-281) is exercised, and the relative-pair decision is made by the
// tonal-centre score.  The pitch set provides unambiguous evidence for one
// member of the relative pair.

TEST(Composing_KeyModeAnalyzerTests, PrefersCMajorForCMajorPitchSet)
{
    // C E G B — complete major triad + leading tone; A absent → C major wins
    const auto results = KeyModeAnalyzer::analyzeKeyMode(
        flatPitches({ 60, 64, 67, 71 }), 0);   // keySig=0: C major / A minor pair

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().keySignatureFifths, 0);
    EXPECT_EQ(results.front().mode, KeyMode::Ionian);
}

TEST(Composing_KeyModeAnalyzerTests, PrefersAMinorForAMinorPitchSet)
{
    // A C E G — complete minor triad + minor 7th; A minor tonal-centre score
    // clearly exceeds C major because A is the tonic and the complete triad is present.
    const auto results = KeyModeAnalyzer::analyzeKeyMode(
        flatPitches({ 57, 60, 64, 67 }), 0);   // keySig=0: C major / A minor pair

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().keySignatureFifths, 0);
    EXPECT_EQ(results.front().mode, KeyMode::Aeolian);
}

TEST(Composing_KeyModeAnalyzerTests, PrefersGMajorForGMajorPitchSet)
{
    // G B D — complete G major triad; E (E-minor tonic) absent
    // keySig=1: relative pair G major (pc=7) / E minor (pc=4)
    const auto results = KeyModeAnalyzer::analyzeKeyMode(
        flatPitches({ 67, 71, 62 }), 1);

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().keySignatureFifths, 1);
    EXPECT_EQ(results.front().mode, KeyMode::Ionian);
}

TEST(Composing_KeyModeAnalyzerTests, PrefersEMinorForEMinorPitchSet)
{
    // E G B — complete E minor triad; G (G-major tonic) is present but only as
    // E minor's third, not G major's complete triad (D absent), so E minor wins.
    const auto results = KeyModeAnalyzer::analyzeKeyMode(
        flatPitches({ 64, 67, 71 }), 1);   // keySig=1: G major / E minor pair

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().keySignatureFifths, 1);
    EXPECT_EQ(results.front().mode, KeyMode::Aeolian);
}

TEST(Composing_KeyModeAnalyzerTests, PrefersDMajorForDMajorPitchSet)
{
    // D F# A — complete D major triad; B (B-minor tonic) absent
    // keySig=2: D major (pc=2) / B minor (pc=11)
    const auto results = KeyModeAnalyzer::analyzeKeyMode(
        flatPitches({ 62, 66, 69 }), 2);

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().keySignatureFifths, 2);
    EXPECT_EQ(results.front().mode, KeyMode::Ionian);
}

TEST(Composing_KeyModeAnalyzerTests, PrefersBMinorForBMinorPitchSet)
{
    // B D F# — complete B minor triad; D (D-major tonic) present only as
    // B minor's minor third — D major has no fifth (A absent), E minor triad not complete.
    const auto results = KeyModeAnalyzer::analyzeKeyMode(
        flatPitches({ 71, 74, 66 }), 2);   // keySig=2: D major / B minor pair

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().keySignatureFifths, 2);
    EXPECT_EQ(results.front().mode, KeyMode::Aeolian);
}

TEST(Composing_KeyModeAnalyzerTests, PrefersFMajorForFMajorPitchSet)
{
    // F A C — complete F major triad; D (D-minor tonic) absent
    // keySig=-1: F major (pc=5) / D minor (pc=2)
    const auto results = KeyModeAnalyzer::analyzeKeyMode(
        flatPitches({ 65, 69, 60 }), -1);

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().keySignatureFifths, -1);
    EXPECT_EQ(results.front().mode, KeyMode::Ionian);
}

TEST(Composing_KeyModeAnalyzerTests, PrefersDMinorForDMinorPitchSet)
{
    // D F A — complete D minor triad; F (F-major tonic) present only as minor third
    // F major has no fifth (C absent) → D minor tonal-centre score > F major.
    const auto results = KeyModeAnalyzer::analyzeKeyMode(
        flatPitches({ 62, 65, 69 }), -1);   // keySig=-1: F major / D minor pair

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().keySignatureFifths, -1);
    EXPECT_EQ(results.front().mode, KeyMode::Aeolian);
}

TEST(Composing_KeyModeAnalyzerTests, PrefersBbMajorForBbMajorPitchSet)
{
    // Bb D F — complete Bb major triad; G (G-minor tonic) absent
    // keySig=-2: Bb major (pc=10) / G minor (pc=7)
    // Bb=58 (Bb3), D=62 (D4), F=65 (F4)
    const auto results = KeyModeAnalyzer::analyzeKeyMode(
        flatPitches({ 58, 62, 65 }), -2);

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().keySignatureFifths, -2);
    EXPECT_EQ(results.front().mode, KeyMode::Ionian);
}

TEST(Composing_KeyModeAnalyzerTests, PrefersGMinorForGMinorPitchSet)
{
    // G Bb D — complete G minor triad; Bb (Bb-major tonic) present only as G minor's
    // minor third — Bb major has no fifth (F absent) → G minor tonal-centre score wins.
    // G=67 (G4), Bb=70 (Bb4), D=74 (D5)
    const auto results = KeyModeAnalyzer::analyzeKeyMode(
        flatPitches({ 67, 70, 74 }), -2);   // keySig=-2: Bb major / G minor pair

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().keySignatureFifths, -2);
    EXPECT_EQ(results.front().mode, KeyMode::Aeolian);
}

// ── Relative major/minor disambiguation — post-hoc mutations ─────────────────
//
// Tests exercise the explicit score mutations applied at lines 206-231 of the
// current implementation.  These adjust scores BEFORE the key-signature path
// selects the final winner.

TEST(Composing_KeyModeAnalyzerTests, DisambiguatesMajorFromRelativeMinorByCompleteTiad)
{
    // C E G present, A absent.
    // → C major: hasCompleteTriad=true, tonicWeight>0, A-minor tonicWeight=0
    // → Post-hoc mutation fires: C major += 4.5, A minor -= 1.5 (lines 212-215)
    // → Plus: C major tonic present, A minor tonic absent → C major += 1.0 (line 225)
    // → tonalCenterScore: C major complete triad + tonic+third+fifth >> A minor (no tonic, no fifth)
    const auto results = KeyModeAnalyzer::analyzeKeyMode(
        flatPitches({ 60, 64, 67 }), 0);   // C E G

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().keySignatureFifths, 0);
    EXPECT_EQ(results.front().mode, KeyMode::Ionian);
}

TEST(Composing_KeyModeAnalyzerTests, DisambiguatesMinorFromRelativeMajorByTonicEvidence)
{
    // A C E present, G absent — A minor complete triad, C major lacks fifth (G absent).
    // → tonalCenterScore: A minor complete triad (tonic+third+fifth+bonus) > C major (tonic+third, no fifth, no triad bonus)
    // → A minor wins via tonalCenterScore comparison (lines 263-265)
    const auto results = KeyModeAnalyzer::analyzeKeyMode(
        flatPitches({ 57, 60, 64 }), 0);   // A C E  (A3=57, C4=60, E4=64)

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().keySignatureFifths, 0);
    EXPECT_EQ(results.front().mode, KeyMode::Aeolian);
}

TEST(Composing_KeyModeAnalyzerTests, DisambiguatesMajorWhenOnlyTonicAbsentInMinor)
{
    // C E G D — C major tonic present, A minor tonic (A) absent.
    // No complete triad check needed; simple tonic-presence rule (line 224) fires:
    // C major += 1.0.  Combined with the tonal-centre advantage, C major wins.
    const auto results = KeyModeAnalyzer::analyzeKeyMode(
        flatPitches({ 60, 64, 67, 62 }), 0);   // C E G D

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().keySignatureFifths, 0);
    EXPECT_EQ(results.front().mode, KeyMode::Ionian);
}

TEST(Composing_KeyModeAnalyzerTests, DisambiguatesMinorWhenOnlyMinorTonicPresent)
{
    // A E — A minor tonic present, C major tonic (C) absent, no complete triads.
    // Simple tonic rule (line 228) fires: A minor += 1.0.
    // With keySig=0, tonalCenterScore for A minor (tonic+fifth) > C major (nothing).
    const auto results = KeyModeAnalyzer::analyzeKeyMode(
        flatPitches({ 57, 64 }), 0);   // A3=57, E4=64

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().keySignatureFifths, 0);
    EXPECT_EQ(results.front().mode, KeyMode::Aeolian);
}

// ── Key signature proximity bias ──────────────────────────────────────────────
//
// The keySignatureScore component penalises candidates far from the notated key
// signature.  This ensures that when pitch evidence is balanced, the key
// closest to the key signature is preferred.

TEST(Composing_KeyModeAnalyzerTests, KeySignatureProximityBiasesResultTowardNotatedKey)
{
    // Pitches from the C/D/E/F/G/A/B set are equally consistent with C major (keySig=0)
    // and with nearby keys.  When keySig=-3 (Eb major) is provided, the proximity
    // penalty makes far-away keys less attractive.
    // Use Eb major pitches (Eb G Bb) with keySig=-3.
    // keySig=-3: Eb major (pc=3) / C minor (pc=0)
    // Eb=63, G=67, Bb=70
    const auto results = KeyModeAnalyzer::analyzeKeyMode(
        flatPitches({ 63, 67, 70 }), -3);

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().keySignatureFifths, -3);
    EXPECT_EQ(results.front().mode, KeyMode::Ionian);
}

TEST(Composing_KeyModeAnalyzerTests, KeySignatureProximityBiasesMinorResult)
{
    // C minor triad (C Eb G) with keySig=-3 → C minor (pc=0) should win.
    // keySig=-3: Eb major / C minor pair.
    // C3=48, Eb=51, G=55 or C4=60, Eb=63, G=67
    const auto results = KeyModeAnalyzer::analyzeKeyMode(
        flatPitches({ 60, 63, 67 }), -3);

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().keySignatureFifths, -3);
    EXPECT_EQ(results.front().mode, KeyMode::Aeolian);
}

// ── Bass weighting ────────────────────────────────────────────────────────────
//
// Bass notes receive 2× evidence weight.  A key whose tonic is the bass note
// should score higher than an otherwise equivalent key where the tonic is
// not in the bass.

TEST(Composing_KeyModeAnalyzerTests, BassTonicBoostsKeyScore)
{
    // C E G with C as bass → C major should win.
    // Re-use flatPitches (which marks the first note as bass).
    // Compare against the same pitches but with G as bass.
    const auto resultsCBass = KeyModeAnalyzer::analyzeKeyMode(
        flatPitches({ 60, 64, 67 }), 0);   // C as bass

    std::vector<KeyModeAnalyzer::PitchContext> pitchesGBass = {
        makePitch(60, 1.0, 1.0, false),   // C — not bass
        makePitch(64, 1.0, 1.0, false),   // E
        makePitch(67, 1.0, 1.0, true),    // G — bass
    };
    const auto resultsGBass = KeyModeAnalyzer::analyzeKeyMode(pitchesGBass, 0);

    // Both should identify C major (only candidate from the keySig=0 major pair).
    ASSERT_FALSE(resultsCBass.empty());
    ASSERT_FALSE(resultsGBass.empty());
    EXPECT_EQ(resultsCBass.front().keySignatureFifths, 0);
    EXPECT_EQ(resultsCBass.front().mode, KeyMode::Ionian);
    EXPECT_EQ(resultsGBass.front().keySignatureFifths, 0);
    EXPECT_EQ(resultsGBass.front().mode, KeyMode::Ionian);

    // C-bass version should score higher because the tonic's evidence weight is doubled.
    EXPECT_GT(resultsCBass.front().score, resultsGBass.front().score);
}

// ── Duration and beat weight ──────────────────────────────────────────────────
//
// A note with higher (durationWeight × beatWeight) contributes more evidence.
// A high-weight tonic should produce a higher score than a low-weight tonic
// with the same pitch set.

TEST(Composing_KeyModeAnalyzerTests, HighDurationWeightOnTonicIncreasesScore)
{
    // Heavy C (tonic of C major).
    std::vector<KeyModeAnalyzer::PitchContext> heavyTonic = {
        makePitch(60, 4.0, 1.0, true),   // C — long note
        makePitch(64, 1.0, 1.0, false),  // E
        makePitch(67, 1.0, 1.0, false),  // G
    };

    // Light C (same pitch set, tonic barely weighted).
    std::vector<KeyModeAnalyzer::PitchContext> lightTonic = {
        makePitch(60, 0.25, 1.0, true),  // C — very short
        makePitch(64, 1.0, 1.0, false),
        makePitch(67, 1.0, 1.0, false),
    };

    const auto resultsHeavy = KeyModeAnalyzer::analyzeKeyMode(heavyTonic, 0);
    const auto resultsLight = KeyModeAnalyzer::analyzeKeyMode(lightTonic, 0);

    ASSERT_FALSE(resultsHeavy.empty());
    ASSERT_FALSE(resultsLight.empty());
    EXPECT_EQ(resultsHeavy.front().keySignatureFifths, 0);
    EXPECT_EQ(resultsHeavy.front().mode, KeyMode::Ionian);

    // Heavy tonic → higher absolute score for the winning candidate.
    EXPECT_GT(resultsHeavy.front().score, resultsLight.front().score);
}

// ── Leading tone evidence ─────────────────────────────────────────────────────
//
// The leading tone (tonicPc + 11) contributes a positive weight to the tonal
// triad score.  Its presence should raise the score of its associated key.

TEST(Composing_KeyModeAnalyzerTests, LeadingToneRaisesScore)
{
    // C E G without leading tone (B).
    const auto resultsNoLeading = KeyModeAnalyzer::analyzeKeyMode(
        flatPitches({ 60, 64, 67 }), 0);

    // C E G B — B is the leading tone of C major (pc=11 = tonicPc+11).
    const auto resultsWithLeading = KeyModeAnalyzer::analyzeKeyMode(
        flatPitches({ 60, 64, 67, 71 }), 0);

    ASSERT_FALSE(resultsNoLeading.empty());
    ASSERT_FALSE(resultsWithLeading.empty());
    EXPECT_EQ(resultsNoLeading.front().mode, KeyMode::Ionian);
    EXPECT_EQ(resultsWithLeading.front().mode, KeyMode::Ionian);

    // Adding the leading tone should increase the score.
    EXPECT_GT(resultsWithLeading.front().score, resultsNoLeading.front().score);
}

// ── Scale score — in-key vs chromatic notes ───────────────────────────────────
//
// Notes inside the scale contribute positively; notes outside penalise.
// A scale-conforming pitch set should score higher than one with chromatic notes.

TEST(Composing_KeyModeAnalyzerTests, ChromaticNotesReduceScoreForMatchingKey)
{
    // C E G — three notes fully inside C major scale.
    const auto resultsClean = KeyModeAnalyzer::analyzeKeyMode(
        flatPitches({ 60, 64, 67 }), 0);

    // C E G + F# (pc=6) — F# is not in C major or A minor scale.
    const auto resultsChromaticExtra = KeyModeAnalyzer::analyzeKeyMode(
        flatPitches({ 60, 64, 67, 66 }), 0);

    ASSERT_FALSE(resultsClean.empty());
    ASSERT_FALSE(resultsChromaticExtra.empty());

    // The chromatic note reduces the winning score.
    EXPECT_GT(resultsClean.front().score, resultsChromaticExtra.front().score);
}

// ── Out-of-range key signature — global path ──────────────────────────────────
//
// When keySignatureFifths is outside [-7, 7], the global-winner path (lines
// 270-281) is used instead of the relative-pair path.  The result should still
// be sensible (not crash, returns sorted candidates).

TEST(Composing_KeyModeAnalyzerTests, OutOfRangeKeySignatureUsesGlobalPath)
{
    // keySig=8 is outside [-7,7]; the global path scans all 24 candidates.
    const auto results = KeyModeAnalyzer::analyzeKeyMode(
        flatPitches({ 60, 64, 67 }), 8);

    ASSERT_FALSE(results.empty());
    // Results should still be sorted descending.
    for (size_t i = 1; i < results.size(); ++i) {
        EXPECT_GE(results[i - 1].score, results[i].score);
    }
}

// ── All 12 chromatic pitches ──────────────────────────────────────────────────

TEST(Composing_KeyModeAnalyzerTests, AllChromaticPitchesDoesNotCrash)
{
    const auto results = KeyModeAnalyzer::analyzeKeyMode(
        flatPitches({ 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71 }), 0);

    // Should not crash and should return at most 3 candidates.
    EXPECT_FALSE(results.empty());
    EXPECT_LE(results.size(), 3u);
}

// ── Full diatonic scales — sanity across the circle ───────────────────────────

TEST(Composing_KeyModeAnalyzerTests, IdentifiesDMajorFromFullScale)
{
    // D E F# G A B C# — all 7 notes of D major (keySig=2)
    // D4=62, E4=64, F#4=66, G4=67, A4=69, B4=71, C#5=73
    const auto results = KeyModeAnalyzer::analyzeKeyMode(
        flatPitches({ 62, 64, 66, 67, 69, 71, 73 }), 2);

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().keySignatureFifths, 2);
    EXPECT_EQ(results.front().mode, KeyMode::Ionian);
}

TEST(Composing_KeyModeAnalyzerTests, IdentifiesBbMajorFromFullScale)
{
    // Bb C D Eb F G A — all 7 notes of Bb major (keySig=-2)
    // Bb3=58, C4=60, D4=62, Eb4=63, F4=65, G4=67, A4=69
    const auto results = KeyModeAnalyzer::analyzeKeyMode(
        flatPitches({ 58, 60, 62, 63, 65, 67, 69 }), -2);

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().keySignatureFifths, -2);
    EXPECT_EQ(results.front().mode, KeyMode::Ionian);
}

TEST(Composing_KeyModeAnalyzerTests, IdentifiesEMinorFromFullScale)
{
    // E F# G A B C D — all 7 notes of E natural minor (keySig=1)
    // E4=64, F#4=66, G4=67, A4=69, B4=71, C5=72, D5=74
    const auto results = KeyModeAnalyzer::analyzeKeyMode(
        flatPitches({ 64, 66, 67, 69, 71, 72, 74 }), 1);

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().keySignatureFifths, 1);
    EXPECT_EQ(results.front().mode, KeyMode::Aeolian);
}

// ── Strongly weighted tonic overrides ambiguity ───────────────────────────────

TEST(Composing_KeyModeAnalyzerTests, HeavyTonicWeightOverridesAmbiguousContext)
{
    // In an ambiguous pitch set, a very heavy tonic pulls the key toward the
    // key whose tonic is heavily weighted.
    //
    // Pitch set: C Eb G (C minor triad, present in both C minor and Eb major).
    // keySig=-3: Eb major (pc=3) / C minor (pc=0).
    // Heavy weight on C (pc=0) → C minor tonic weight dominates → C minor wins.
    std::vector<KeyModeAnalyzer::PitchContext> pitches = {
        makePitch(60, 4.0, 1.0, true),   // C — heavy tonic evidence
        makePitch(63, 1.0, 1.0, false),  // Eb
        makePitch(67, 1.0, 1.0, false),  // G
    };

    const auto results = KeyModeAnalyzer::analyzeKeyMode(pitches, -3);

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().keySignatureFifths, -3);
    EXPECT_EQ(results.front().mode, KeyMode::Aeolian);   // C minor
}

// ── Normalized confidence ───────────────────────────────────────────────────

TEST(Composing_KeyModeAnalyzerTests, ConfidenceIsInZeroOneRange)
{
    // Full C major scale — should produce a confident result.
    const auto pitches = flatPitches({ 60, 62, 64, 65, 67, 69, 71 });
    const auto results = KeyModeAnalyzer::analyzeKeyMode(pitches, 0);

    ASSERT_GE(results.size(), 2u);
    EXPECT_GE(results.front().normalizedConfidence, 0.0);
    EXPECT_LE(results.front().normalizedConfidence, 1.0);
    EXPECT_GE(results[1].normalizedConfidence, 0.0);
    EXPECT_LE(results[1].normalizedConfidence, 1.0);
}

TEST(Composing_KeyModeAnalyzerTests, StrongEvidenceProducesHighConfidence)
{
    // Full C major scale with heavy tonic — very clear evidence.
    std::vector<KeyModeAnalyzer::PitchContext> pitches = {
        makePitch(60, 4.0, 1.0, true),   // C — heavy
        makePitch(62, 1.0, 0.4, false),  // D
        makePitch(64, 2.0, 1.0, false),  // E
        makePitch(65, 1.0, 0.4, false),  // F
        makePitch(67, 2.0, 0.7, false),  // G
        makePitch(69, 1.0, 0.4, false),  // A
        makePitch(71, 1.0, 0.2, false),  // B
    };

    const auto results = KeyModeAnalyzer::analyzeKeyMode(pitches, 0);
    ASSERT_FALSE(results.empty());
    EXPECT_GT(results.front().normalizedConfidence, 0.5);
}

TEST(Composing_KeyModeAnalyzerTests, AmbiguousInputProducesLowConfidence)
{
    // Single pitch — minimal evidence, should produce low confidence.
    const auto pitches = flatPitches({ 60 });
    const auto results = KeyModeAnalyzer::analyzeKeyMode(pitches, 0);

    ASSERT_FALSE(results.empty());
    // With mode priors, even a single pitch yields moderate confidence because
    // the prior strongly favors Tier 1 modes.  The threshold is set above the
    // strong-evidence test (> 0.5) but allows the prior-boosted gap.
    EXPECT_LT(results.front().normalizedConfidence, 0.9);
}

// ── Non-Ionian/Aeolian mode identification ──────────────────────────────────
//
// Each of the five remaining diatonic modes is tested with its tonic triad plus
// the mode's characteristic pitch.  A weighted tonic ensures the mode wins
// over competing candidates that share the same key signature (all 7 modes
// share keySig=0 when built from the C major pitch-class set).

TEST(Composing_KeyModeAnalyzerTests, IdentifiesDDorianFromTonicTriadAndCharacteristic)
{
    // D Dorian: D minor triad (D F A) + B (major 6th — characteristic).
    // keySig=0 (same key sig as C Ionian).  Heavy tonic D.
    std::vector<KeyModeAnalyzer::PitchContext> pitches = {
        makePitch(62, 3.0, 1.0, true),   // D — heavy tonic (bass)
        makePitch(65, 1.0, 1.0, false),  // F — minor 3rd
        makePitch(69, 1.0, 1.0, false),  // A — perfect 5th
        makePitch(71, 1.0, 1.0, false),  // B — characteristic (major 6th)
    };

    const auto results = KeyModeAnalyzer::analyzeKeyMode(pitches, 0);

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().mode, KeyMode::Dorian);
    EXPECT_EQ(results.front().tonicPc, 2);   // D
}

TEST(Composing_KeyModeAnalyzerTests, IdentifiesEPhrygianFromTonicTriadAndCharacteristic)
{
    // E Phrygian: E minor triad (E G B) + F (minor 2nd — characteristic).
    // keySig=0.  Heavy tonic E.
    std::vector<KeyModeAnalyzer::PitchContext> pitches = {
        makePitch(64, 3.0, 1.0, true),   // E — heavy tonic (bass)
        makePitch(67, 1.0, 1.0, false),  // G — minor 3rd
        makePitch(71, 1.0, 1.0, false),  // B — perfect 5th
        makePitch(65, 1.0, 1.0, false),  // F — characteristic (minor 2nd)
    };

    const auto results = KeyModeAnalyzer::analyzeKeyMode(pitches, 0);

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().mode, KeyMode::Phrygian);
    EXPECT_EQ(results.front().tonicPc, 4);   // E
}

TEST(Composing_KeyModeAnalyzerTests, IdentifiesFLydianFromTonicTriadAndCharacteristic)
{
    // F Lydian: F major triad (F A C) + B (augmented 4th — characteristic).
    // keySig=0.  Heavy tonic F.
    std::vector<KeyModeAnalyzer::PitchContext> pitches = {
        makePitch(65, 3.0, 1.0, true),   // F — heavy tonic (bass)
        makePitch(69, 1.0, 1.0, false),  // A — major 3rd
        makePitch(72, 1.0, 1.0, false),  // C — perfect 5th
        makePitch(71, 1.0, 1.0, false),  // B — characteristic (augmented 4th)
    };

    const auto results = KeyModeAnalyzer::analyzeKeyMode(pitches, 0);

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().mode, KeyMode::Lydian);
    EXPECT_EQ(results.front().tonicPc, 5);   // F
}

TEST(Composing_KeyModeAnalyzerTests, IdentifiesGMixolydianFromTonicTriadAndCharacteristic)
{
    // G Mixolydian: G major triad (G B D) + F (minor 7th — characteristic).
    // keySig=0.  Heavy tonic G.
    std::vector<KeyModeAnalyzer::PitchContext> pitches = {
        makePitch(67, 3.0, 1.0, true),   // G — heavy tonic (bass)
        makePitch(71, 1.0, 1.0, false),  // B — major 3rd
        makePitch(74, 1.0, 1.0, false),  // D — perfect 5th
        makePitch(65, 1.0, 1.0, false),  // F — characteristic (minor 7th)
    };

    const auto results = KeyModeAnalyzer::analyzeKeyMode(pitches, 0);

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().mode, KeyMode::Mixolydian);
    EXPECT_EQ(results.front().tonicPc, 7);   // G
}

TEST(Composing_KeyModeAnalyzerTests, IdentifiesBLocrianFromTonicTriadAndCharacteristic)
{
    // B Locrian: B diminished triad (B D F), where F is also the characteristic
    // (diminished 5th).  keySig=0.  Heavy tonic B.
    std::vector<KeyModeAnalyzer::PitchContext> pitches = {
        makePitch(59, 3.0, 1.0, true),   // B — heavy tonic (bass)
        makePitch(62, 1.0, 1.0, false),  // D — minor 3rd
        makePitch(65, 1.0, 1.0, false),  // F — dim 5th + characteristic
    };

    const auto results = KeyModeAnalyzer::analyzeKeyMode(pitches, 0);

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().mode, KeyMode::Locrian);
    EXPECT_EQ(results.front().tonicPc, 11);  // B
}

// ── Full diatonic scales — non-Ionian/Aeolian modes ─────────────────────────

TEST(Composing_KeyModeAnalyzerTests, IdentifiesDDorianFromFullScale)
{
    // D E F G A B C — all 7 notes of D Dorian, with heavy D tonic.
    std::vector<KeyModeAnalyzer::PitchContext> pitches = {
        makePitch(62, 3.0, 1.0, true),   // D
        makePitch(64, 1.0, 0.4, false),  // E
        makePitch(65, 1.0, 0.4, false),  // F
        makePitch(67, 1.0, 0.4, false),  // G
        makePitch(69, 1.5, 0.7, false),  // A — fifth
        makePitch(71, 1.0, 0.4, false),  // B — characteristic
        makePitch(72, 1.0, 0.4, false),  // C
    };

    const auto results = KeyModeAnalyzer::analyzeKeyMode(pitches, 0);

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().mode, KeyMode::Dorian);
    EXPECT_EQ(results.front().tonicPc, 2);
}

TEST(Composing_KeyModeAnalyzerTests, IdentifiesGMixolydianFromFullScale)
{
    // G A B C D E F — all 7 notes of G Mixolydian, with heavy G tonic.
    std::vector<KeyModeAnalyzer::PitchContext> pitches = {
        makePitch(67, 3.0, 1.0, true),   // G
        makePitch(69, 1.0, 0.4, false),  // A
        makePitch(71, 1.5, 0.7, false),  // B — third
        makePitch(72, 1.0, 0.4, false),  // C
        makePitch(74, 1.5, 0.7, false),  // D — fifth
        makePitch(76, 1.0, 0.4, false),  // E
        makePitch(77, 1.0, 0.4, false),  // F — characteristic
    };

    const auto results = KeyModeAnalyzer::analyzeKeyMode(pitches, 0);

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().mode, KeyMode::Mixolydian);
    EXPECT_EQ(results.front().tonicPc, 7);
}

// ── Non-zero key signature modes ─────────────────────────────────────────────

TEST(Composing_KeyModeAnalyzerTests, IdentifiesADorianWithKeySig1)
{
    // A Dorian = A B C D E F# G — shares keySig=1 (G major).
    // Tonic triad: A C E (A minor).  Characteristic: F# (major 6th).
    std::vector<KeyModeAnalyzer::PitchContext> pitches = {
        makePitch(69, 3.0, 1.0, true),   // A — heavy tonic (bass)
        makePitch(72, 1.0, 1.0, false),  // C — minor 3rd
        makePitch(76, 1.0, 1.0, false),  // E — perfect 5th
        makePitch(78, 1.0, 1.0, false),  // F# — characteristic (major 6th)
    };

    const auto results = KeyModeAnalyzer::analyzeKeyMode(pitches, 1);

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().mode, KeyMode::Dorian);
    EXPECT_EQ(results.front().tonicPc, 9);   // A
}
