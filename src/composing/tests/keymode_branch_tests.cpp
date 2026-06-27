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

// LAYER 3 — KEY/MODE branch backfill (Phase-5 round-2, cluster 4 of 4).
//
// Tests-only. Each assertion pins the THEORY/CONTRACT-correct value (the oracle),
// re-derived at source, never echoed from the implementation:
//   * keymodeformatting.cpp — keyModeTonicName / keyModeSuffix: the user-visible
//     display-label contract (one assert per mode case). The tonic name of each
//     mode at a key signature is derived from music theory (white-key modal tonic
//     at 0 fifths; documented offset rules for the altered/family modes); the suffix
//     is the project's documented label vocabulary (the contract this cluster pins).
//   * keymodeanalyzer.cpp — the public key-signature helpers and the analyzeKeyMode
//     edge arms (out-of-range signature global-argmax fallback, specific-mode
//     declared-mode compatibility, runner-up emission).
//   * keymodesequence.cpp — decodeLattice edge arms (empty state set, "keep all
//     alternatives").
//
// ONE labelled regression-guard (KnownIssue_*) pins CURRENT (spec-flagged brittle)
// behaviour of the char/leading-tone presence gate — the non-Bach C->F emission
// misread — and is documented as a known issue whose fix is Phase B (B2), NOT a
// correctness claim. See project_k279_key_regression_diagnosis + L3 section 11.

#include <gtest/gtest.h>

#include <array>
#include <optional>
#include <vector>

#include "composing/analysis/key/keymodeanalyzer.h"
#include "composing/analysis/key/keymodesequence.h"

#include "test_helpers.h"

using namespace mu::composing::analysis;

namespace kms = mu::composing::analysis::keymodeseq;
using KMSD = kms::KeyModeSequenceDecoder;
using KmsState = KMSD::State;
using kms::SliceKeyMode;
using kms::KeyModeSequencePreferences;

// ============================================================================
// keymodeformatting.cpp — keyModeTonicName
// ============================================================================
//
// keyModeTonicName(fifths, mode) -> the human-readable tonic of `mode` whose
// associated key signature is `fifths`. At fifths = 0 (no sharps/flats) the
// diatonic modes resolve to their white-key tonics (theory: the church mode whose
// scale uses no accidentals); the melodic/harmonic-minor family reuses the parent
// diatonic mode's name array at the same signature (documented in source + the
// cluster instruction: "harmonic/melodic-minor reuse Aeolian/Dorian names"); the
// two genuinely-distinct families use the documented tonic offsets — Altered is one
// semitone above the Ionian tonic (C -> C#), AlteredDomBB7 an augmented fifth above
// (C -> G#).

TEST(Composing_KeyModeFormatting, TonicNameAtZeroFifths_AllModes)
{
    // Diatonic: white-key modal tonics at 0 sharps/flats
    EXPECT_STREQ(keyModeTonicName(0, KeySigMode::Ionian),     "C");   // C major scale
    EXPECT_STREQ(keyModeTonicName(0, KeySigMode::Dorian),     "D");   // D-E-F-G-A-B-C
    EXPECT_STREQ(keyModeTonicName(0, KeySigMode::Phrygian),   "E");   // E-F-G-A-B-C-D
    EXPECT_STREQ(keyModeTonicName(0, KeySigMode::Lydian),     "F");   // F-G-A-B-C-D-E
    EXPECT_STREQ(keyModeTonicName(0, KeySigMode::Mixolydian), "G");   // G-A-B-C-D-E-F
    EXPECT_STREQ(keyModeTonicName(0, KeySigMode::Aeolian),    "A");   // A natural minor
    EXPECT_STREQ(keyModeTonicName(0, KeySigMode::Locrian),    "B");   // B-C-D-E-F-G-A

    // Melodic-minor family: reuse the parent diatonic name array at idx 7
    EXPECT_STREQ(keyModeTonicName(0, KeySigMode::MelodicMinor),    "D");   // ~Dorian name
    EXPECT_STREQ(keyModeTonicName(0, KeySigMode::DorianB2),        "E");   // ~Phrygian name
    EXPECT_STREQ(keyModeTonicName(0, KeySigMode::LydianAugmented), "F");   // ~Lydian name
    EXPECT_STREQ(keyModeTonicName(0, KeySigMode::LydianDominant),  "G");   // ~Mixolydian name
    EXPECT_STREQ(keyModeTonicName(0, KeySigMode::MixolydianB6),    "A");   // ~Aeolian name
    EXPECT_STREQ(keyModeTonicName(0, KeySigMode::AeolianB5),       "B");   // ~Locrian name
    EXPECT_STREQ(keyModeTonicName(0, KeySigMode::Altered),         "C#");  // 1 semitone above Ionian C

    // Harmonic-minor family: reuse the parent diatonic name array at idx 7
    EXPECT_STREQ(keyModeTonicName(0, KeySigMode::HarmonicMinor),    "A");  // ~Aeolian name
    EXPECT_STREQ(keyModeTonicName(0, KeySigMode::LocrianSharp6),    "B");  // ~Locrian name
    EXPECT_STREQ(keyModeTonicName(0, KeySigMode::IonianSharp5),     "C");  // ~Ionian name
    EXPECT_STREQ(keyModeTonicName(0, KeySigMode::DorianSharp4),     "D");  // ~Dorian name
    EXPECT_STREQ(keyModeTonicName(0, KeySigMode::PhrygianDominant), "E");  // ~Phrygian name
    EXPECT_STREQ(keyModeTonicName(0, KeySigMode::LydianSharp2),     "F");  // ~Lydian name
    EXPECT_STREQ(keyModeTonicName(0, KeySigMode::AlteredDomBB7),    "G#"); // aug5 above Ionian C
}

TEST(Composing_KeyModeFormatting, TonicNameAtNonZeroFifths)
{
    // Theory: signature -> Ionian tonic, then offset by the mode.
    EXPECT_STREQ(keyModeTonicName(-3, KeySigMode::Aeolian), "C");   // 3 flats -> C minor (instruction example)
    EXPECT_STREQ(keyModeTonicName(2,  KeySigMode::Dorian),  "E");   // 2 sharps Dorian -> E Dorian
    EXPECT_STREQ(keyModeTonicName(-2, KeySigMode::Ionian),  "Bb");  // 2 flats major -> Bb
    EXPECT_STREQ(keyModeTonicName(1,  KeySigMode::Ionian),  "G");   // 1 sharp major -> G
    EXPECT_STREQ(keyModeTonicName(-1, KeySigMode::Ionian),  "F");   // 1 flat major -> F
    EXPECT_STREQ(keyModeTonicName(7,  KeySigMode::Ionian),  "C#");  // 7 sharps -> C# major
    EXPECT_STREQ(keyModeTonicName(-7, KeySigMode::Ionian),  "Cb");  // 7 flats -> Cb major
}

TEST(Composing_KeyModeFormatting, TonicNameClampsOutOfRangeFifths)
{
    // The index is std::clamp(fifths + 7, 0, 14): an out-of-range signature pins
    // to the boundary name (defensive clamp on the name table).
    EXPECT_STREQ(keyModeTonicName(-10, KeySigMode::Ionian), "Cb");  // clamps to idx 0
    EXPECT_STREQ(keyModeTonicName(10,  KeySigMode::Ionian), "C#");  // clamps to idx 14
}

// ============================================================================
// keymodeformatting.cpp — keyModeSuffix
// ============================================================================
//
// The project's documented display-label vocabulary (the contract this cluster
// pins, one assert per mode). The "#N" shorthand means "the Nth degree of the
// parent mode raised one semitone" (internally consistent: AeolianB5 = Locrian's
// flat-2 raised to natural-2 = "Loc#2"). The flat glyph below is U+266D; under the
// build's /utf-8 it encodes to the same bytes as the source's ♭ escape.

TEST(Composing_KeyModeFormatting, SuffixContract_AllModes)
{
    // Diatonic
    EXPECT_STREQ(keyModeSuffix(KeySigMode::Ionian),     "maj");
    EXPECT_STREQ(keyModeSuffix(KeySigMode::Dorian),     "Dor");
    EXPECT_STREQ(keyModeSuffix(KeySigMode::Phrygian),   "Phryg");
    EXPECT_STREQ(keyModeSuffix(KeySigMode::Lydian),     "Lyd");
    EXPECT_STREQ(keyModeSuffix(KeySigMode::Mixolydian), "Mixolyd");
    EXPECT_STREQ(keyModeSuffix(KeySigMode::Aeolian),    "min");
    EXPECT_STREQ(keyModeSuffix(KeySigMode::Locrian),    "Loc");
    // Melodic-minor family
    EXPECT_STREQ(keyModeSuffix(KeySigMode::MelodicMinor),    "mel");
    EXPECT_STREQ(keyModeSuffix(KeySigMode::DorianB2),        "Dor♭2");
    EXPECT_STREQ(keyModeSuffix(KeySigMode::LydianAugmented), "Lyd+");
    EXPECT_STREQ(keyModeSuffix(KeySigMode::LydianDominant),  "Lyd♭7");
    EXPECT_STREQ(keyModeSuffix(KeySigMode::MixolydianB6),    "Mix♭6");
    EXPECT_STREQ(keyModeSuffix(KeySigMode::AeolianB5),       "Loc#2");
    EXPECT_STREQ(keyModeSuffix(KeySigMode::Altered),         "alt");
    // Harmonic-minor family
    EXPECT_STREQ(keyModeSuffix(KeySigMode::HarmonicMinor),    "harm");
    EXPECT_STREQ(keyModeSuffix(KeySigMode::LocrianSharp6),    "Loc#6");
    EXPECT_STREQ(keyModeSuffix(KeySigMode::IonianSharp5),     "Ion+");
    EXPECT_STREQ(keyModeSuffix(KeySigMode::DorianSharp4),     "Dor#4");
    EXPECT_STREQ(keyModeSuffix(KeySigMode::PhrygianDominant), "PhrygDom");
    EXPECT_STREQ(keyModeSuffix(KeySigMode::LydianSharp2),     "Lyd#2");
    EXPECT_STREQ(keyModeSuffix(KeySigMode::AlteredDomBB7),    "altDom");
}

// ============================================================================
// keymodeanalyzer.cpp — public key-signature helpers
// ============================================================================

// ionianTonicPcForMode(tonicPc, modeIndex): map a modal tonic pc to the parent
// Ionian tonic pc that shares the same key signature. Oracle from theory: the
// Ionian tonic of each mode's parent key.
TEST(Composing_KeyModeAnalyzerBranch, IonianTonicPcForMode_ParentMapping)
{
    EXPECT_EQ(ionianTonicPcForMode(0, keyModeIndex(KeySigMode::Ionian)),     0);  // C Ion -> C
    EXPECT_EQ(ionianTonicPcForMode(2, keyModeIndex(KeySigMode::Dorian)),     0);  // D Dor -> C
    EXPECT_EQ(ionianTonicPcForMode(4, keyModeIndex(KeySigMode::Phrygian)),   0);  // E Phr -> C
    EXPECT_EQ(ionianTonicPcForMode(5, keyModeIndex(KeySigMode::Lydian)),     0);  // F Lyd -> C
    EXPECT_EQ(ionianTonicPcForMode(7, keyModeIndex(KeySigMode::Mixolydian)), 0);  // G Mix -> C
    EXPECT_EQ(ionianTonicPcForMode(9, keyModeIndex(KeySigMode::Aeolian)),    0);  // A Aeol -> C
    EXPECT_EQ(ionianTonicPcForMode(11, keyModeIndex(KeySigMode::Locrian)),   0);  // B Loc -> C
}

// The out-of-range modeIndex guard (modeIndex >= IONIAN_OFFSETS.size()) returns
// the tonic pc unchanged — a defensive passthrough on a public function.
TEST(Composing_KeyModeAnalyzerBranch, IonianTonicPcForMode_OutOfRangePassesThrough)
{
    EXPECT_EQ(ionianTonicPcForMode(5, static_cast<size_t>(KEY_MODE_COUNT)), 5);  // index == 21
    EXPECT_EQ(ionianTonicPcForMode(3, static_cast<size_t>(99)),             3);
}

// keySignatureFifthsForKey(tonicPc, isMajor, referenceFifths): map a binary
// (tonic, major/minor) key to its notated signature, choosing the enharmonic
// spelling nearest the reference. Major -> Ionian circle position; minor ->
// relative-major fifths.
TEST(Composing_KeyModeAnalyzerBranch, KeySignatureFifthsForKey_MajorAndMinor)
{
    EXPECT_EQ(keySignatureFifthsForKey(0, true,  0),  0);   // C major
    EXPECT_EQ(keySignatureFifthsForKey(7, true,  0),  1);   // G major
    EXPECT_EQ(keySignatureFifthsForKey(5, true,  0), -1);   // F major
    EXPECT_EQ(keySignatureFifthsForKey(9, false, 0),  0);   // A minor -> C major sig 0
    EXPECT_EQ(keySignatureFifthsForKey(2, false, 0), -1);   // D minor -> F major sig -1
    EXPECT_EQ(keySignatureFifthsForKey(4, false, 0),  1);   // E minor -> G major sig 1
}

// Enharmonic resolution chooses the spelling nearest the reference signature.
TEST(Composing_KeyModeAnalyzerBranch, KeySignatureFifthsForKey_EnharmonicNearestReference)
{
    EXPECT_EQ(keySignatureFifthsForKey(6, true,  6),  6);   // F# major (sharp ref)
    EXPECT_EQ(keySignatureFifthsForKey(6, true, -6), -6);   // Gb major (flat ref)
    EXPECT_EQ(keySignatureFifthsForKey(1, true,  7),  7);   // C# major (sharp ref)
    EXPECT_EQ(keySignatureFifthsForKey(1, true, -5), -5);   // Db major (flat ref)
}

// keyModeSignatureFifths(tonicPc, mode, referenceFifths): the full-mode public
// wrapper over the same resolution (used by the L3 sequence decoder to label a
// state's signature).
TEST(Composing_KeyModeAnalyzerBranch, KeyModeSignatureFifths_FullMode)
{
    EXPECT_EQ(keyModeSignatureFifths(0, KeySigMode::Ionian,     0), 0);   // C major
    EXPECT_EQ(keyModeSignatureFifths(9, KeySigMode::Aeolian,    0), 0);   // A minor -> 0
    EXPECT_EQ(keyModeSignatureFifths(2, KeySigMode::Dorian,     0), 0);   // D Dorian -> parent C -> 0
    EXPECT_EQ(keyModeSignatureFifths(7, KeySigMode::Mixolydian, 0), 0);   // G Mixolydian -> parent C -> 0
}

// keyModeScaleIntervals(mode): the canonical scale-degree intervals of each mode
// (theory). Oracle = the mode's scale in semitones from the tonic.
TEST(Composing_KeyModeAnalyzerBranch, ScaleIntervals_Contract)
{
    using A7 = std::array<int, 7>;
    EXPECT_EQ(keyModeScaleIntervals(KeySigMode::Ionian),        (A7{ 0, 2, 4, 5, 7, 9, 11 }));
    EXPECT_EQ(keyModeScaleIntervals(KeySigMode::Aeolian),       (A7{ 0, 2, 3, 5, 7, 8, 10 }));
    EXPECT_EQ(keyModeScaleIntervals(KeySigMode::Dorian),        (A7{ 0, 2, 3, 5, 7, 9, 10 }));
    EXPECT_EQ(keyModeScaleIntervals(KeySigMode::HarmonicMinor), (A7{ 0, 2, 3, 5, 7, 8, 11 }));
    EXPECT_EQ(keyModeScaleIntervals(KeySigMode::MelodicMinor),  (A7{ 0, 2, 3, 5, 7, 9, 11 }));
}

// ============================================================================
// keymodeanalyzer.cpp — analyzeKeyMode edge arms
// ============================================================================

// A NEGATIVE out-of-range key signature (< -7) drops out of BOTH the in-range
// disambiguation block and the in-range selection block, falling to the
// global-argmax path. (The existing OutOfRangeKeySignatureUsesGlobalPath covers
// the > 7 side, which evaluates the first `>= -7` operand TRUE; this covers the
// < -7 side, which makes that first operand FALSE.)
TEST(Composing_KeyModeAnalyzerBranch, NegativeOutOfRangeKeySignatureUsesGlobalPath)
{
    const auto results = KeyModeAnalyzer::analyzeKeyMode(
        flatPitches({ 60, 64, 67 }), -8);   // C E G, signature far below the valid range

    ASSERT_FALSE(results.empty());
    for (size_t i = 1; i < results.size(); ++i) {
        EXPECT_GE(results[i - 1].score, results[i].score)
            << "global-argmax fallback still returns score-sorted candidates";
    }
}

// A SPECIFIC declared mode (not the class-level Ionian/Aeolian) routes every
// candidate through the exact-match compatibility arm: only the declared mode is
// compatible, all others receive the penalty. With a strong penalty on a clear
// D-Dorian pitch set, D Dorian — the only unpenalized class — wins.
TEST(Composing_KeyModeAnalyzerBranch, DeclaredSpecificMode_ExactMatchCompatibility)
{
    KeyModeAnalyzerPreferences prefs;       // Standard defaults
    prefs.declaredModePenalty = 8.0;        // strong hint, to make the threading visible

    // D Dorian evidence: D minor triad (D F A) + B (major 6th — characteristic).
    std::vector<KeyModeAnalyzer::PitchContext> pitches = {
        makePitch(62, 3.0, 1.0, true),   // D — heavy tonic (bass)
        makePitch(65, 1.0, 1.0, false),  // F — minor 3rd
        makePitch(69, 1.0, 1.0, false),  // A — perfect 5th
        makePitch(71, 1.0, 1.0, false),  // B — characteristic (major 6th)
    };
    const auto results = KeyModeAnalyzer::analyzeKeyMode(
        pitches, 0, prefs, KeySigMode::Dorian);

    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().mode, KeySigMode::Dorian)
        << "a specific (Dorian) declaration is exact-match: every non-Dorian mode is "
           "penalized, so the Dorian reading wins";
    EXPECT_EQ(results.front().tonicPc, 2);   // D
}

// Runner-up emission: when the winner and its same-signature relatives are the top
// candidates, the result list carries several entries sharing the winner's
// signature with DIFFERENT modes (the dedup only drops the exact winner).
TEST(Composing_KeyModeAnalyzerBranch, RunnerUpsShareWinnerSignatureWithDifferentMode)
{
    // Full C major scale -> C major wins; A minor and G Mixolydian (both 0-signature)
    // follow as runners-up.
    const auto results = KeyModeAnalyzer::analyzeKeyMode(
        flatPitches({ 60, 62, 64, 65, 67, 69, 71 }), 0);

    ASSERT_GE(results.size(), 2u);
    EXPECT_EQ(results.front().keySignatureFifths, 0);
    EXPECT_EQ(results.front().mode, KeySigMode::Ionian);

    bool sameSigDifferentMode = false;
    for (size_t i = 1; i < results.size(); ++i) {
        if (results[i].keySignatureFifths == results.front().keySignatureFifths
            && results[i].mode != results.front().mode) {
            sameSigDifferentMode = true;
        }
    }
    EXPECT_TRUE(sameSigDifferentMode)
        << "a runner-up shares the winner's signature with a different mode "
           "(e.g. A minor under C major)";
}

// ---- KNOWN-ISSUE regression guard (do NOT assert correct — Phase B / B2) ----
//
// The char/leading-tone presence gate is spec-flagged brittle (L3 section 11; the
// non-Bach C->F regression, project_k279_key_regression_diagnosis). For a I+IV
// pitch context at signature 0 the EMISSION ranks F major ABOVE C major: the ever-
// present E (C's third) doubles as F's major-7 characteristic AND F's leading tone,
// harvesting both boosts (+1.80 char, +1.20 lt), while C's own characteristic/leading
// tone (B) is absent -> C is denied both (char flips to a -0.60 penalty). This guard
// PINS that current (musically-wrong) emission ranking; the correct answer is C. Its
// fix belongs to Phase B (B2) — when fixed, this expectation flips and must be updated.
TEST(Composing_KeyModeAnalyzerBranch, KnownIssue_CharLtPresenceGate_EmissionRanksFAboveC_PhaseB)
{
    // I (C E G) + IV (F A C) pulled into one context, signature 0.
    std::vector<KeyCandidateScore> dump;
    KeyModeAnalyzer::analyzeKeyMode(
        flatPitches({ 60, 64, 67, 65, 69, 72 }), 0,
        kDefaultKeyModeAnalyzerPreferences, std::nullopt, &dump);
    ASSERT_FALSE(dump.empty());

    const size_t ionianIdx = keyModeIndex(KeySigMode::Ionian);
    const KeyCandidateScore* fIonian = nullptr;   // tonicPc 5, Ionian
    const KeyCandidateScore* cIonian = nullptr;   // tonicPc 0, Ionian
    for (const KeyCandidateScore& e : dump) {
        if (e.modeIndex != ionianIdx) {
            continue;
        }
        if (e.tonicPc == 5) { fIonian = &e; }
        if (e.tonicPc == 0) { cIonian = &e; }
    }
    ASSERT_NE(fIonian, nullptr);
    ASSERT_NE(cIonian, nullptr);

    EXPECT_GT(fIonian->finalScore, cIonian->finalScore)
        << "KNOWN ISSUE (Phase B/B2): the char/lt presence gate makes the emission "
           "prefer F major over C major for a I+IV context. Correct answer is C; this "
           "guard documents current behaviour and flips when the gate is fixed.";
    // The same brittleness makes F major the global emission argmax.
    EXPECT_EQ(dump.front().tonicPc, 5);
    EXPECT_EQ(dump.front().modeIndex, ionianIdx);
}

// ============================================================================
// keymodesequence.cpp — decodeLattice edge arms
// ============================================================================

// An empty state set (S == 0) with a non-empty emission column returns {} via the
// `T == 0 || S == 0` guard's second operand. (The existing EmptyLattice_NoSlices
// covers T == 0 with empty emissions, which short-circuits on the first operand.)
TEST(Composing_KeyModeSequenceBranch, DecodeLattice_EmptyStateSetReturnsEmpty)
{
    const std::vector<KmsState> noStates;
    const std::vector<std::vector<double>> oneColumn = { { 1.0, 2.0 } };   // T = 1, S = 0
    EXPECT_TRUE(KMSD::decodeLattice(noStates, oneColumn).empty());
}

// maxAlternatives <= 0 means "keep ALL surviving alternatives" (no cap). With three
// states, every slice keeps its two non-winner states as ranked alternatives.
TEST(Composing_KeyModeSequenceBranch, DecodeLattice_MaxAlternativesZeroKeepsAll)
{
    const KmsState cIon  { 0, KeySigMode::Ionian, 0, 0 };
    const KmsState gIon  { 7, KeySigMode::Ionian, 1, 7 };
    const KmsState fsIon { 6, KeySigMode::Ionian, 6, 6 };
    const std::vector<KmsState> states = { cIon, gIon, fsIon };
    std::vector<std::vector<double>> em(3, { 5.0, 3.0, 1.0 });   // C > G > F# every slice

    KeyModeSequencePreferences prefs;
    prefs.maxAlternatives = 0;   // 0 = keep all (the uncapped arm)
    const auto d = KMSD::decodeLattice(states, em, prefs);

    ASSERT_EQ(d.size(), 3u);
    EXPECT_EQ(d[1].chosen.tonicPc, 0) << "C wins every slice";
    EXPECT_EQ(d[1].alternatives.size(), 2u)
        << "maxAlternatives <= 0 keeps ALL non-winner states, uncapped";
}
