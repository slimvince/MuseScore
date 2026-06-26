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

// ── Test-backfill (criteria 1-4): chordvoicing (L4 chord) ────────────────────
//
// chordTonePitchClasses() and closePositionVoicing() were 0% directly covered
// (cc_tree_repair_and_coverage_report.md C1 §4). These are fully DECIDABLE from
// music theory + the documented struct contract — every assertion below is an
// INDEPENDENT ORACLE (the tertian chord-tone set for a quality/extension, the
// close-position octave-placement formula, the documented Unknown-quality empty
// voicing), hand-derived, NOT pinned from the implementation's output.
//
// Oracle for chordTonePitchClasses (chordvoicing.cpp): root first, then upper
// chord tones sorted ascending by interval from the root, deduplicated in
// pitch-class space. Triad from quality; fifth alterations override; sevenths /
// added-6 / upper extensions per the Extension flags.
//
// Oracle for closePositionVoicing: Unknown quality -> empty voicing (bassPitch
// == -1, no treble, per the header contract). Otherwise root in the bass octave
// (MIDI 36 + rootPc; the +12 octave-up branch is never taken because for every
// rootPc the |best-42| comparison ties, so bass == 36 + rootPc for rootPc 0..11);
// upper tones stacked in close position from C4 (MIDI 60), each placed at or above
// the previous (octave-raised on wrap). The voicing is ALWAYS root-position: it
// reads chordTonePitchClasses (root first) and never consults identity.bassPc.

#include <gtest/gtest.h>

#include <algorithm>
#include <vector>

#include "composing/analysis/chord/chordanalyzer.h"

using namespace mu::composing::analysis;

namespace {

// Build a bare ChordAnalysisResult with a given root + quality + extension flags.
// bassPc defaults to rootPc (root position); a test overrides it to prove the
// voicing ignores it.
ChordAnalysisResult chord(int rootPc, ChordQuality quality,
                          std::initializer_list<Extension> exts = {},
                          int bassPc = -1)
{
    ChordAnalysisResult r;
    r.identity.rootPc = rootPc;
    r.identity.bassPc = (bassPc < 0) ? rootPc : bassPc;
    r.identity.quality = quality;
    for (Extension e : exts) {
        setExtension(r.identity.extensions, e);
    }
    return r;
}

} // namespace

// ── chordTonePitchClasses: per-quality triads (criterion 1, 3) ───────────────

TEST(Composing_ChordVoicingTests, ToneSet_MajorTriad_RootThirdFifth)
{
    // C major = {C,E,G} = {0,4,7}.
    EXPECT_EQ(chordTonePitchClasses(chord(0, ChordQuality::Major)),
              (std::vector<int>{ 0, 4, 7 }));
}

TEST(Composing_ChordVoicingTests, ToneSet_MinorTriad_FlatThird)
{
    EXPECT_EQ(chordTonePitchClasses(chord(0, ChordQuality::Minor)),
              (std::vector<int>{ 0, 3, 7 }));   // {C,Eb,G}
}

TEST(Composing_ChordVoicingTests, ToneSet_DiminishedTriad_FlatThirdFlatFifth)
{
    EXPECT_EQ(chordTonePitchClasses(chord(0, ChordQuality::Diminished)),
              (std::vector<int>{ 0, 3, 6 }));   // {C,Eb,Gb}
}

TEST(Composing_ChordVoicingTests, ToneSet_AugmentedTriad_SharpFifth)
{
    EXPECT_EQ(chordTonePitchClasses(chord(0, ChordQuality::Augmented)),
              (std::vector<int>{ 0, 4, 8 }));   // {C,E,G#}
}

TEST(Composing_ChordVoicingTests, ToneSet_HalfDiminished_CarriesStructuralMinorSeventh)
{
    // Half-diminished is a four-note quality: root, m3, d5, and a structural m7
    // (not flagged via the MinorSeventh extension). {C,Eb,Gb,Bb} = {0,3,6,10}.
    EXPECT_EQ(chordTonePitchClasses(chord(0, ChordQuality::HalfDiminished)),
              (std::vector<int>{ 0, 3, 6, 10 }));
}

TEST(Composing_ChordVoicingTests, ToneSet_Suspended2_And_Suspended4)
{
    EXPECT_EQ(chordTonePitchClasses(chord(0, ChordQuality::Suspended2)),
              (std::vector<int>{ 0, 2, 7 }));   // {C,D,G}
    EXPECT_EQ(chordTonePitchClasses(chord(0, ChordQuality::Suspended4)),
              (std::vector<int>{ 0, 5, 7 }));   // {C,F,G}
}

TEST(Composing_ChordVoicingTests, ToneSet_Power_NoThird)
{
    EXPECT_EQ(chordTonePitchClasses(chord(0, ChordQuality::Power)),
              (std::vector<int>{ 0, 7 }));      // {C,G} — no third
}

TEST(Composing_ChordVoicingTests, ToneSet_Unknown_RootOnly)
{
    // Unknown quality has no third/fifth; chordTonePitchClasses still returns the
    // root (it is closePositionVoicing — not this function — that yields empty).
    EXPECT_EQ(chordTonePitchClasses(chord(0, ChordQuality::Unknown)),
              (std::vector<int>{ 0 }));
}

// ── chordTonePitchClasses: sevenths + added sixth (criterion 1, 3) ───────────

TEST(Composing_ChordVoicingTests, ToneSet_MajorSeventh_And_DominantSeventh)
{
    EXPECT_EQ(chordTonePitchClasses(chord(0, ChordQuality::Major, { Extension::MajorSeventh })),
              (std::vector<int>{ 0, 4, 7, 11 }));   // Cmaj7
    EXPECT_EQ(chordTonePitchClasses(chord(0, ChordQuality::Major, { Extension::MinorSeventh })),
              (std::vector<int>{ 0, 4, 7, 10 }));   // C7
}

TEST(Composing_ChordVoicingTests, ToneSet_FullyDiminishedSeventh)
{
    EXPECT_EQ(chordTonePitchClasses(
                  chord(0, ChordQuality::Diminished, { Extension::DiminishedSeventh })),
              (std::vector<int>{ 0, 3, 6, 9 }));    // Cdim7
}

TEST(Composing_ChordVoicingTests, ToneSet_AddedSixth_PresentOnlyWithoutSeventh)
{
    // C6 = {C,E,G,A} = {0,4,7,9}.
    EXPECT_EQ(chordTonePitchClasses(chord(0, ChordQuality::Major, { Extension::AddedSixth })),
              (std::vector<int>{ 0, 4, 7, 9 }));
    // With a seventh present the added 6th is a 13th and is suppressed by the
    // AddedSixth guard: C7(add6) -> the 6th (pc 9) does NOT appear.
    EXPECT_EQ(chordTonePitchClasses(
                  chord(0, ChordQuality::Major, { Extension::MinorSeventh, Extension::AddedSixth })),
              (std::vector<int>{ 0, 4, 7, 10 }));
}

// ── chordTonePitchClasses: fifth alterations + omit third (criterion 1, 4) ───

TEST(Composing_ChordVoicingTests, ToneSet_FlatFifthAndSharpFifth_OverrideThePerfectFifth)
{
    // C7b5: the FlatFifth alteration moves the perfect fifth (7) to a diminished
    // fifth (6). {C,E,Gb,Bb} = {0,4,6,10}.
    EXPECT_EQ(chordTonePitchClasses(
                  chord(0, ChordQuality::Major, { Extension::MinorSeventh, Extension::FlatFifth })),
              (std::vector<int>{ 0, 4, 6, 10 }));
    // SharpFifth moves 7 -> 8.
    EXPECT_EQ(chordTonePitchClasses(
                  chord(0, ChordQuality::Major, { Extension::SharpFifth })),
              (std::vector<int>{ 0, 4, 8 }));
}

TEST(Composing_ChordVoicingTests, ToneSet_OmitsThird_DropsTheThird)
{
    EXPECT_EQ(chordTonePitchClasses(chord(0, ChordQuality::Major, { Extension::OmitsThird })),
              (std::vector<int>{ 0, 7 }));   // root + fifth only
}

// ── chordTonePitchClasses: upper extensions, dedup, interval sort ────────────

TEST(Composing_ChordVoicingTests, ToneSet_UpperExtensions_SortedByIntervalFromRoot)
{
    // C9 = C7 + natural 9th (pc 2). Pushed after the triad+7th, then the upper
    // tones are sorted ascending by interval-from-root: {0,2,4,7,10}.
    EXPECT_EQ(chordTonePitchClasses(
                  chord(0, ChordQuality::Major, { Extension::MinorSeventh, Extension::NaturalNinth })),
              (std::vector<int>{ 0, 2, 4, 7, 10 }));
}

TEST(Composing_ChordVoicingTests, ToneSet_Deduplicates_ExtensionColllidingWithChordTone)
{
    // Csus2 already contains pc 2 (the suspended 2nd). Adding NaturalNinth (also
    // pc 2) must NOT duplicate it.
    EXPECT_EQ(chordTonePitchClasses(
                  chord(0, ChordQuality::Suspended2, { Extension::NaturalNinth })),
              (std::vector<int>{ 0, 2, 7 }));
}

TEST(Composing_ChordVoicingTests, ToneSet_NonZeroRoot_KeepsRootFirstAndSortsByInterval)
{
    // A major = {A,C#,E} = {9,1,4}; root stays first, uppers sorted by interval
    // (C# at +4 before E at +7).
    EXPECT_EQ(chordTonePitchClasses(chord(9, ChordQuality::Major)),
              (std::vector<int>{ 9, 1, 4 }));
}

TEST(Composing_ChordVoicingTests, ToneSet_EveryUpperExtension_AddsItsSemitone)
{
    // Each upper-extension flag adds its semitone offset from the root (criterion 1:
    // the extension input classes). Oracle = the documented semitone map:
    // b9=1, #9=3, 11=5, #11=6, b13=8, 13=9, #13=10. Asserted as set membership on a
    // C-rooted chord so the dedup/interval-sort ordering is not re-derived here.
    auto has = [](const std::vector<int>& v, int pc) {
        return std::find(v.begin(), v.end(), pc) != v.end();
    };
    EXPECT_TRUE(has(chordTonePitchClasses(chord(0, ChordQuality::Major, { Extension::FlatNinth })), 1));
    EXPECT_TRUE(has(chordTonePitchClasses(chord(0, ChordQuality::Major, { Extension::SharpNinth })), 3));
    EXPECT_TRUE(has(chordTonePitchClasses(chord(0, ChordQuality::Major, { Extension::NaturalEleventh })), 5));
    EXPECT_TRUE(has(chordTonePitchClasses(chord(0, ChordQuality::Major, { Extension::SharpEleventh })), 6));
    EXPECT_TRUE(has(chordTonePitchClasses(chord(0, ChordQuality::Major, { Extension::FlatThirteenth })), 8));
    EXPECT_TRUE(has(chordTonePitchClasses(chord(0, ChordQuality::Major, { Extension::NaturalThirteenth })), 9));
    EXPECT_TRUE(has(chordTonePitchClasses(chord(0, ChordQuality::Major, { Extension::SharpThirteenth })), 10));
}

TEST(Composing_ChordVoicingTests, ToneSet_HalfDiminishedWithExplicitMinorSeventh_NoDoubleSeventh)
{
    // When the MinorSeventh extension is already set, the half-diminished structural
    // m7 is NOT added a second time (the guarded branch) — the tone set is still
    // {C,Eb,Gb,Bb} = {0,3,6,10}, with pc 10 contributed once by the extension path.
    EXPECT_EQ(chordTonePitchClasses(
                  chord(0, ChordQuality::HalfDiminished, { Extension::MinorSeventh })),
              (std::vector<int>{ 0, 3, 6, 10 }));
}

// ── closePositionVoicing (criterion 2 contract + 3 outcomes) ─────────────────

TEST(Composing_ChordVoicingTests, Voicing_UnknownQuality_IsEmptyWithBassMinusOne)
{
    // Documented contract (chordanalyzer.h:1115): Unknown -> empty voicing,
    // bassPitch == -1.
    const ClosePositionVoicing v = closePositionVoicing(chord(0, ChordQuality::Unknown));
    EXPECT_EQ(v.bassPitch, -1);
    EXPECT_TRUE(v.treblePitches.empty());
}

TEST(Composing_ChordVoicingTests, Voicing_CMajor_RootInBassUpperTonesStacked)
{
    // C major: bass = 36 + 0 = C2(36); treble stacks E4(64), G4(67) above C4.
    const ClosePositionVoicing v = closePositionVoicing(chord(0, ChordQuality::Major));
    EXPECT_EQ(v.bassPitch, 36);
    EXPECT_EQ(v.treblePitches, (std::vector<int>{ 64, 67 }));
}

TEST(Composing_ChordVoicingTests, Voicing_BassIsRootPlus36_ForEveryRoot)
{
    // The bass octave-up branch is never taken: bass == 36 + rootPc for all roots.
    for (int rootPc = 0; rootPc < 12; ++rootPc) {
        const ClosePositionVoicing v = closePositionVoicing(chord(rootPc, ChordQuality::Major));
        EXPECT_EQ(v.bassPitch, 36 + rootPc) << "rootPc=" << rootPc;
        EXPECT_GE(v.bassPitch, 36);
        EXPECT_LE(v.bassPitch, 47);   // C2..B2, all within the documented C2-C3 range
    }
}

TEST(Composing_ChordVoicingTests, Voicing_OctaveWrap_RaisesAToneThatFallsBelowThePrevious)
{
    // Dmaj7 tone set = {2,6,9,1}. Uppers {6,9,1}: F#4(66), A4(69), then C#(pc 1)
    // would be 61 < 69, so it is octave-raised to 73 — exercising the while-loop.
    const ClosePositionVoicing v =
        closePositionVoicing(chord(2, ChordQuality::Major, { Extension::MajorSeventh }));
    EXPECT_EQ(v.bassPitch, 38);   // D2
    EXPECT_EQ(v.treblePitches, (std::vector<int>{ 66, 69, 73 }));
    // Strictly ascending (close position never descends).
    for (size_t i = 1; i < v.treblePitches.size(); ++i) {
        EXPECT_GT(v.treblePitches[i], v.treblePitches[i - 1]);
    }
}

TEST(Composing_ChordVoicingTests, Voicing_IgnoresBassPc_AlwaysRootPosition)
{
    // closePositionVoicing reads chordTonePitchClasses (root first) and never
    // consults identity.bassPc, so a first-inversion identity (bass = E) yields
    // the SAME root-position voicing as the root-position identity.
    const ClosePositionVoicing rootPos = closePositionVoicing(chord(0, ChordQuality::Major, {}, 0));
    const ClosePositionVoicing firstInv = closePositionVoicing(chord(0, ChordQuality::Major, {}, 4));
    EXPECT_EQ(firstInv.bassPitch, rootPos.bassPitch);
    EXPECT_EQ(firstInv.treblePitches, rootPos.treblePitches);
    EXPECT_EQ(firstInv.bassPitch, 36);   // root C in the bass regardless of bassPc
}
