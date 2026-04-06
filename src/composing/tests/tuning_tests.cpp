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

#include "composing/intonation/equal_temperament.h"
#include "composing/intonation/just_intonation.h"
#include "composing/intonation/kirnberger.h"
#include "composing/intonation/pythagorean.h"
#include "composing/intonation/quarter_comma_meantone.h"
#include "composing/intonation/werckmeister.h"
#include "composing/intonation/tuning_system.h"
#include "composing/intonation/tuning_utils.h"

using namespace mu::composing::intonation;
using namespace mu::composing::analysis;

namespace {

// Default-constructed KeyModeAnalysisResult — unused by all current systems.
const KeyModeAnalysisResult kNoKey{};

// ── semitoneFromPitches ───────────────────────────────────────────────────────

TEST(Tuning_Utils, SemitoneFromPitches_Unison)
{
    EXPECT_EQ(semitoneFromPitches(0, 0), 0);
    EXPECT_EQ(semitoneFromPitches(7, 7), 0);
}

TEST(Tuning_Utils, SemitoneFromPitches_PerfectFifth)
{
    // G (7) above C (0)
    EXPECT_EQ(semitoneFromPitches(7, 0), 7);
    // D (2) above G (7)
    EXPECT_EQ(semitoneFromPitches(2, 7), 7);
}

TEST(Tuning_Utils, SemitoneFromPitches_MajorThird)
{
    // E (4) above C (0)
    EXPECT_EQ(semitoneFromPitches(4, 0), 4);
}

TEST(Tuning_Utils, SemitoneFromPitches_WrapsCorrectly)
{
    // C (0) above D root (2): (0 - 2 + 12) % 12 = 10 — minor 7th
    EXPECT_EQ(semitoneFromPitches(0, 2), 10);
    // B (11) above C root (0): 11 semitones — major 7th
    EXPECT_EQ(semitoneFromPitches(11, 0), 11);
}

// ── EqualTemperament ─────────────────────────────────────────────────────────

TEST(Tuning_EqualTemperament, AlwaysZeroForAllSemitones)
{
    EqualTemperament et;
    for (int s = 0; s <= 11; ++s) {
        EXPECT_DOUBLE_EQ(et.tuningOffset(kNoKey, ChordQuality::Major, 0, s), 0.0)
            << "semitone " << s;
    }
}

TEST(Tuning_EqualTemperament, AlwaysZeroRegardlessOfQuality)
{
    EqualTemperament et;
    EXPECT_DOUBLE_EQ(et.tuningOffset(kNoKey, ChordQuality::Diminished, 0, 6), 0.0);
    EXPECT_DOUBLE_EQ(et.tuningOffset(kNoKey, ChordQuality::Minor,      0, 3), 0.0);
}

// ── JustIntonation ───────────────────────────────────────────────────────────

TEST(Tuning_JustIntonation, UnisonIsZero)
{
    JustIntonation ji;
    EXPECT_DOUBLE_EQ(ji.tuningOffset(kNoKey, ChordQuality::Major, 0, 0), 0.0);
}

TEST(Tuning_JustIntonation, MajorThirdFlatterThanET)
{
    // 5/4 ratio → −13.7 ¢
    JustIntonation ji;
    EXPECT_NEAR(ji.tuningOffset(kNoKey, ChordQuality::Major, 0, 4), -13.7, 0.1);
}

TEST(Tuning_JustIntonation, PerfectFifthSharpOfET)
{
    // 3/2 ratio → +2.0 ¢
    JustIntonation ji;
    EXPECT_NEAR(ji.tuningOffset(kNoKey, ChordQuality::Major, 0, 7), +2.0, 0.1);
}

TEST(Tuning_JustIntonation, MinorThirdSharpOfET)
{
    // 6/5 ratio → +15.6 ¢
    JustIntonation ji;
    EXPECT_NEAR(ji.tuningOffset(kNoKey, ChordQuality::Minor, 0, 3), +15.6, 0.1);
}

TEST(Tuning_JustIntonation, TritoneAugFourthInMajor)
{
    // 45/32 ratio → −9.8 ¢ for augmented fourth context (major chord)
    JustIntonation ji;
    EXPECT_NEAR(ji.tuningOffset(kNoKey, ChordQuality::Major, 0, 6), -9.8, 0.1);
}

TEST(Tuning_JustIntonation, TritoneDimFifthInDiminished)
{
    // 64/45 ratio → +9.8 ¢ for diminished fifth context
    JustIntonation ji;
    EXPECT_NEAR(ji.tuningOffset(kNoKey, ChordQuality::Diminished,     0, 6), +9.8, 0.1);
    EXPECT_NEAR(ji.tuningOffset(kNoKey, ChordQuality::HalfDiminished, 0, 6), +9.8, 0.1);
}

TEST(Tuning_JustIntonation, MinorSeventhSharpOfET)
{
    // 9/5 ratio → +17.6 ¢
    JustIntonation ji;
    EXPECT_NEAR(ji.tuningOffset(kNoKey, ChordQuality::Major, 0, 10), +17.6, 0.1);
}

// ── PythagoreanTuning ─────────────────────────────────────────────────────────

TEST(Tuning_Pythagorean, UnisonIsZero)
{
    PythagoreanTuning pt;
    EXPECT_DOUBLE_EQ(pt.tuningOffset(kNoKey, ChordQuality::Major, 0, 0), 0.0);
}

TEST(Tuning_Pythagorean, PerfectFifthSharpOfET)
{
    // 3/2 ratio → +2.0 ¢ (same as just intonation)
    PythagoreanTuning pt;
    EXPECT_NEAR(pt.tuningOffset(kNoKey, ChordQuality::Major, 0, 7), +2.0, 0.1);
}

TEST(Tuning_Pythagorean, MajorThirdSharpOfET)
{
    // 81/64 ratio → +7.8 ¢  (wider than just intonation's −13.7 ¢)
    PythagoreanTuning pt;
    EXPECT_NEAR(pt.tuningOffset(kNoKey, ChordQuality::Major, 0, 4), +7.8, 0.1);
}

TEST(Tuning_Pythagorean, TritoneAugFourthInMajor)
{
    // 729/512 ratio → +11.7 ¢
    PythagoreanTuning pt;
    EXPECT_NEAR(pt.tuningOffset(kNoKey, ChordQuality::Major, 0, 6), +11.7, 0.1);
}

TEST(Tuning_Pythagorean, TritoneDimFifthInDiminished)
{
    // 1024/729 ratio → −11.7 ¢
    PythagoreanTuning pt;
    EXPECT_NEAR(pt.tuningOffset(kNoKey, ChordQuality::Diminished, 0, 6), -11.7, 0.1);
}

// ── Symmetry: Just vs Pythagorean tritone disambiguation ─────────────────────

TEST(Tuning_TritoneDisambiguation, JustAndPythagoreanAreOppositeSign)
{
    JustIntonation    ji;
    PythagoreanTuning pt;

    // Both systems flip sign between aug4 and dim5, but differ in magnitude.
    const double jiAug4  = ji.tuningOffset(kNoKey, ChordQuality::Major,      0, 6);
    const double jiDim5  = ji.tuningOffset(kNoKey, ChordQuality::Diminished, 0, 6);
    const double ptAug4  = pt.tuningOffset(kNoKey, ChordQuality::Major,      0, 6);
    const double ptDim5  = pt.tuningOffset(kNoKey, ChordQuality::Diminished, 0, 6);

    EXPECT_GT(jiDim5,  jiAug4);   // dim5 sharper than aug4 in just
    EXPECT_LT(ptDim5,  ptAug4);   // dim5 flatter than aug4 in pythagorean
}

// ── WerckmeisterTemperament ───────────────────────────────────────────────────
// Well temperament: deviations are absolute (depend on pitch class, not interval).
// All tests use rootPc=0 (C) so absolute PC = semitone interval.

TEST(Tuning_Werckmeister, UnisonIsZero)
{
    WerckmeisterTemperament wt;
    // C has 0.0 ¢ deviation by definition (reference pitch).
    EXPECT_DOUBLE_EQ(wt.tuningOffset(kNoKey, ChordQuality::Major, 0, 0), 0.0);
}

TEST(Tuning_Werckmeister, FifthFlatOfET)
{
    // G (absolute PC 7): −3.9 ¢ — one of four narrow fifths.
    WerckmeisterTemperament wt;
    EXPECT_NEAR(wt.tuningOffset(kNoKey, ChordQuality::Major, 0, 7), -3.9, 0.1);
}

TEST(Tuning_Werckmeister, MajorThirdFlatOfET)
{
    // E (absolute PC 4): −9.8 ¢ — sharper third than just intonation but still
    // flatter than ET.  Gives C major its warm character.
    WerckmeisterTemperament wt;
    EXPECT_NEAR(wt.tuningOffset(kNoKey, ChordQuality::Major, 0, 4), -9.8, 0.1);
}

TEST(Tuning_Werckmeister, RemoteKeyMoreColorful)
{
    // F# (absolute PC 6): −11.7 ¢ — remote keys deviate more from ET.
    WerckmeisterTemperament wt;
    EXPECT_NEAR(wt.tuningOffset(kNoKey, ChordQuality::Major, 0, 6), -11.7, 0.1);
}

TEST(Tuning_Werckmeister, QualityDoesNotAffectResult)
{
    // Well temperament is key-dependent, not chord-quality-dependent.
    WerckmeisterTemperament wt;
    EXPECT_DOUBLE_EQ(
        wt.tuningOffset(kNoKey, ChordQuality::Major, 0, 4),
        wt.tuningOffset(kNoKey, ChordQuality::Minor, 0, 4));
    EXPECT_DOUBLE_EQ(
        wt.tuningOffset(kNoKey, ChordQuality::Major, 0, 6),
        wt.tuningOffset(kNoKey, ChordQuality::Diminished, 0, 6));
}

TEST(Tuning_Werckmeister, AbsolutePcFromDifferentRoot)
{
    // Root = D (2), semitone interval = 5 → absolute PC = (2+5)%12 = 7 (G) → −3.9 ¢.
    WerckmeisterTemperament wt;
    EXPECT_NEAR(wt.tuningOffset(kNoKey, ChordQuality::Major, 2, 5), -3.9, 0.1);
}

// ── KirnbergerTemperament ────────────────────────────────────────────────────
// Similar to Werckmeister but with a pure major third C–E (5/4 = 386.3 ¢).

TEST(Tuning_Kirnberger, UnisonIsZero)
{
    KirnbergerTemperament kt;
    EXPECT_DOUBLE_EQ(kt.tuningOffset(kNoKey, ChordQuality::Major, 0, 0), 0.0);
}

TEST(Tuning_Kirnberger, PureMajorThirdFromC)
{
    // The defining feature of Kirnberger III: C–E is pure 5/4 = −13.7 ¢ from ET.
    // Same value as just intonation's major third.
    KirnbergerTemperament kt;
    EXPECT_NEAR(kt.tuningOffset(kNoKey, ChordQuality::Major, 0, 4), -13.7, 0.1);
}

TEST(Tuning_Kirnberger, FIsUnchanged)
{
    // F has 0.0 ¢ deviation (F–C fifth is narrow by only the schisma, closing
    // the circle; F itself lands on ET).
    KirnbergerTemperament kt;
    EXPECT_NEAR(kt.tuningOffset(kNoKey, ChordQuality::Major, 0, 5), 0.0, 0.1);
}

TEST(Tuning_Kirnberger, FifthSlightlyFlat)
{
    // G: −3.4 ¢ — the C–G fifth is narrow by 1/4 syntonic comma.
    KirnbergerTemperament kt;
    EXPECT_NEAR(kt.tuningOffset(kNoKey, ChordQuality::Major, 0, 7), -3.4, 0.1);
}

TEST(Tuning_Kirnberger, RemoteKeyDeviation)
{
    // B (absolute PC 11): −11.7 ¢ — remote key, large deviation.
    KirnbergerTemperament kt;
    EXPECT_NEAR(kt.tuningOffset(kNoKey, ChordQuality::Major, 0, 11), -11.7, 0.1);
}

// ── QuarterCommaMeantone ─────────────────────────────────────────────────────

TEST(Tuning_Meantone, UnisonIsZero)
{
    QuarterCommaMeantone mt;
    EXPECT_DOUBLE_EQ(mt.tuningOffset(kNoKey, ChordQuality::Major, 0, 0), 0.0);
}

TEST(Tuning_Meantone, PureMajorThird)
{
    // 4 meantone fifths produce pure 5/4 = 386.3 ¢ → −13.7 ¢ from ET.
    QuarterCommaMeantone mt;
    EXPECT_NEAR(mt.tuningOffset(kNoKey, ChordQuality::Major, 0, 4), -13.7, 0.1);
}

TEST(Tuning_Meantone, FifthNarrowerThanJust)
{
    // Perfect fifth: 696.6 ¢ → −3.4 ¢ from ET.
    // Compare: just/Pythagorean fifth is +2.0 ¢ (sharp of ET).
    QuarterCommaMeantone mt;
    EXPECT_NEAR(mt.tuningOffset(kNoKey, ChordQuality::Major, 0, 7), -3.4, 0.1);
}

TEST(Tuning_Meantone, MinorThirdSharpOfET)
{
    // Minor third: 310.3 ¢ → +10.3 ¢ from ET.
    QuarterCommaMeantone mt;
    EXPECT_NEAR(mt.tuningOffset(kNoKey, ChordQuality::Minor, 0, 3), +10.3, 0.1);
}

TEST(Tuning_Meantone, MajorSeventhFlatOfET)
{
    // Major seventh: 1082.9 ¢ → −17.1 ¢ from ET.
    QuarterCommaMeantone mt;
    EXPECT_NEAR(mt.tuningOffset(kNoKey, ChordQuality::Major, 0, 11), -17.1, 0.1);
}

TEST(Tuning_Meantone, TritoneAugFourthInMajor)
{
    // Augmented fourth: 579.5 ¢ → −20.5 ¢ from ET.
    // Meantone has the largest aug4/dim5 split of any system (~41 ¢).
    QuarterCommaMeantone mt;
    EXPECT_NEAR(mt.tuningOffset(kNoKey, ChordQuality::Major, 0, 6), -20.5, 0.1);
}

TEST(Tuning_Meantone, TritoneDimFifthInDiminished)
{
    // Diminished fifth: 620.5 ¢ → +20.5 ¢ from ET.
    QuarterCommaMeantone mt;
    EXPECT_NEAR(mt.tuningOffset(kNoKey, ChordQuality::Diminished,     0, 6), +20.5, 0.1);
    EXPECT_NEAR(mt.tuningOffset(kNoKey, ChordQuality::HalfDiminished, 0, 6), +20.5, 0.1);
}

TEST(Tuning_Meantone, DiatonicSemitoneSharpOfET)
{
    // Diatonic semitone (minor 2nd): 117.1 ¢ → +17.1 ¢ from ET.
    // Meantone's large diatonic semitone is characteristic of the system.
    QuarterCommaMeantone mt;
    EXPECT_NEAR(mt.tuningOffset(kNoKey, ChordQuality::Major, 0, 1), +17.1, 0.1);
}

// ── Cross-system: well temperaments vs adaptive temperaments ─────────────────

TEST(Tuning_CrossSystem, WellTemperamentsIgnoreQuality)
{
    // Werckmeister and Kirnberger use absolute pitch class, not chord quality.
    // Meantone, Just, and Pythagorean DO use quality (at least for tritone).
    WerckmeisterTemperament wt;
    KirnbergerTemperament   kt;
    QuarterCommaMeantone    mt;

    const double wt_maj = wt.tuningOffset(kNoKey, ChordQuality::Major, 0, 6);
    const double wt_dim = wt.tuningOffset(kNoKey, ChordQuality::Diminished, 0, 6);
    EXPECT_DOUBLE_EQ(wt_maj, wt_dim);  // well temperament: same

    const double kt_maj = kt.tuningOffset(kNoKey, ChordQuality::Major, 0, 6);
    const double kt_dim = kt.tuningOffset(kNoKey, ChordQuality::Diminished, 0, 6);
    EXPECT_DOUBLE_EQ(kt_maj, kt_dim);  // well temperament: same

    const double mt_maj = mt.tuningOffset(kNoKey, ChordQuality::Major, 0, 6);
    const double mt_dim = mt.tuningOffset(kNoKey, ChordQuality::Diminished, 0, 6);
    EXPECT_NE(mt_maj, mt_dim);          // meantone: different (−20.5 vs +20.5)
}

// ── Tuning anchor keyword matching ───────────────────────────────────────────

TEST(Tuning_Anchor, FullItalianForm_ExactMatch)
{
    EXPECT_TRUE(isTuningAnchorText("altezza di riferimento"));
}

TEST(Tuning_Anchor, FullItalianForm_CaseInsensitive)
{
    EXPECT_TRUE(isTuningAnchorText("ALTEZZA DI RIFERIMENTO"));
    EXPECT_TRUE(isTuningAnchorText("Altezza di Riferimento"));
}

TEST(Tuning_Anchor, FullItalianForm_Whitespace)
{
    EXPECT_TRUE(isTuningAnchorText("  altezza di riferimento  "));
    EXPECT_TRUE(isTuningAnchorText("\t altezza di riferimento\n"));
}

TEST(Tuning_Anchor, AbbreviatedForm_AltRifDot_ExactMatch)
{
    EXPECT_TRUE(isTuningAnchorText("alt. rif."));
}

TEST(Tuning_Anchor, AbbreviatedForm_AltRifDot_CaseInsensitive)
{
    EXPECT_TRUE(isTuningAnchorText("ALT. RIF."));
    EXPECT_TRUE(isTuningAnchorText("Alt. Rif."));
}

TEST(Tuning_Anchor, AbbreviatedForm_AltRifDot_Whitespace)
{
    EXPECT_TRUE(isTuningAnchorText("  alt. rif.  "));
}

TEST(Tuning_Anchor, AbbreviatedForm_AltRifNospace_ExactMatch)
{
    EXPECT_TRUE(isTuningAnchorText("alt.rif."));
}

TEST(Tuning_Anchor, AbbreviatedForm_AltRifNospace_CaseInsensitive)
{
    EXPECT_TRUE(isTuningAnchorText("ALT.RIF."));
}

TEST(Tuning_Anchor, SemiAbbreviatedForm_ExactMatch)
{
    EXPECT_TRUE(isTuningAnchorText("altezza rif."));
}

TEST(Tuning_Anchor, SemiAbbreviatedForm_CaseInsensitive)
{
    EXPECT_TRUE(isTuningAnchorText("ALTEZZA RIF."));
    EXPECT_TRUE(isTuningAnchorText("Altezza Rif."));
}

TEST(Tuning_Anchor, OldKeyword_NoLongerMatches)
{
    EXPECT_FALSE(isTuningAnchorText("anchor-pitch"));
    EXPECT_FALSE(isTuningAnchorText("ANCHOR-PITCH"));
    EXPECT_FALSE(isTuningAnchorText("Anchor-Pitch"));
}

TEST(Tuning_Anchor, EmptyString_ReturnsFalse)
{
    EXPECT_FALSE(isTuningAnchorText(""));
}

TEST(Tuning_Anchor, WhitespaceOnly_ReturnsFalse)
{
    EXPECT_FALSE(isTuningAnchorText("   "));
}

TEST(Tuning_Anchor, UnrelatedText_ReturnsFalse)
{
    EXPECT_FALSE(isTuningAnchorText("altezza"));
    EXPECT_FALSE(isTuningAnchorText("riferimento"));
    EXPECT_FALSE(isTuningAnchorText("alt."));
    EXPECT_FALSE(isTuningAnchorText("rif."));
    EXPECT_FALSE(isTuningAnchorText("altezza di riferimentoX"));
    EXPECT_FALSE(isTuningAnchorText("Xaltezza di riferimento"));
}

// ── Anchor protection boundary tests (regression for applyRegionTuning 8.2) ──
//
// applyRegionTuning() Phase 2 and Phase 3 call hasTuningAnchorExpression()
// which delegates to isTuningAnchorText().  These tests document the exact-match
// contract: only the four accepted forms protect a note; prefixed/suffixed text
// and "alt. rif." with missing internal space do NOT match, preventing
// accidental over-protection of non-anchor notes.

TEST(Tuning_AnchorProtection, ExactMatchRequired_NoTrailingText)
{
    // Anchor forms with appended text must NOT be treated as anchors.
    EXPECT_FALSE(isTuningAnchorText("alt. rif. (see note)"));
    EXPECT_FALSE(isTuningAnchorText("altezza di riferimento — bar 12"));
    EXPECT_FALSE(isTuningAnchorText("altezza rif. extra"));
}

TEST(Tuning_AnchorProtection, ExactMatchRequired_NoLeadingText)
{
    // Anchor forms with prepended text must NOT be treated as anchors.
    EXPECT_FALSE(isTuningAnchorText("see alt. rif."));
    EXPECT_FALSE(isTuningAnchorText("NB altezza di riferimento"));
    EXPECT_FALSE(isTuningAnchorText("(alt. rif.)"));
}

TEST(Tuning_AnchorProtection, SpacingInsideAbbreviationMatters)
{
    // "alt. rif." requires the space after the first dot.
    // "alt.rif." (without that space) is a separate accepted form.
    // Neither "altrif." nor "alt rif" are accepted.
    EXPECT_TRUE(isTuningAnchorText("alt. rif."));   // space variant — accepted
    EXPECT_TRUE(isTuningAnchorText("alt.rif."));    // no-space variant — accepted
    EXPECT_FALSE(isTuningAnchorText("alt rif."));   // missing dot after "alt" — not accepted
    EXPECT_FALSE(isTuningAnchorText("altrif."));    // missing both dots — not accepted
}

TEST(Tuning_Anchor, RetuningSusceptibility_AnchorIsAbsolutelyProtected)
{
    // Verify the enum value exists and is distinct from Free.
    EXPECT_NE(RetuningSusceptibility::AbsolutelyProtected,
              RetuningSusceptibility::Free);
}

TEST(Tuning_Anchor, RetuningSusceptibility_AdjustableIsDistinct)
{
    EXPECT_NE(RetuningSusceptibility::Adjustable,
              RetuningSusceptibility::Free);
    EXPECT_NE(RetuningSusceptibility::Adjustable,
              RetuningSusceptibility::AbsolutelyProtected);
}

} // namespace
