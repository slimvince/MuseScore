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
#include "composing/intonation/pythagorean.h"
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

} // namespace
