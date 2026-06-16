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

// tonicizationlabeler_tests.cpp — Stage 6-tonic-i.
//
// Pins the tonicization (applied-chord) labeler (tonicizationlabeler.{h,cpp}):
// the applied-dominant / applied-leading-tone predicate, the chromatic-raised-LT
// false-positive guard, the tonic-target exclusion, the V/V7 and viio/viio7
// seventh distinctions, and the degree-token casing. The labeler consumes the
// prevailing resolved key (tonicPc + isMajor + signature fifths), which these
// tests supply directly.

#include <gtest/gtest.h>

#include <vector>

#include "composing/analysis/function/tonicizationlabeler.h"

using namespace mu::composing::analysis;

namespace {

uint16_t mask(std::initializer_list<int> pcs)
{
    uint16_t m = 0;
    for (int pc : pcs) {
        m |= static_cast<uint16_t>(1u << (((pc % 12) + 12) % 12));
    }
    return m;
}

// A region in a fixed prevailing key (tonicPc, isMajor, signature fifths).
TonicizationRegionInput region(int startTick, int rootPc, ChordQuality q,
                               std::initializer_list<int> pcs,
                               int keyTonicPc, bool keyIsMajor, int fifths,
                               bool minorSeventh = false,
                               bool dimSeventh = false)
{
    TonicizationRegionInput r;
    r.startTick = startTick;
    r.endTick = startTick + 480;
    r.rootPc = rootPc;
    r.quality = q;
    r.pitchClassMask = mask(pcs);
    r.hasMinorSeventh = minorSeventh;
    r.hasDiminishedSeventh = dimSeventh;
    r.keyTonicPc = keyTonicPc;
    r.keyIsMajor = keyIsMajor;
    r.keySignatureFifths = fifths;
    return r;
}

} // namespace

// ── Applied dominant ─────────────────────────────────────────────────────────

// D major (root 2, third F#=6) → G major (root 7) in C major. F# is chromatic
// vs the 0-sharp signature. Textbook V/V.
TEST(TonicizationLabeler, AppliedDominantTriad_V_of_V)
{
    std::vector<TonicizationRegionInput> regions = {
        region(0,   2, ChordQuality::Major, { 2, 6, 9 }, 0, true, 0),   // D major
        region(480, 7, ChordQuality::Major, { 7, 11, 2 }, 0, true, 0),  // G major
    };
    const auto labels = labelTonicizations(regions);
    ASSERT_EQ(labels.size(), 2u);
    EXPECT_TRUE(labels[0].isApplied);
    EXPECT_EQ(labels[0].kind, AppliedKind::AppliedDominant);
    EXPECT_EQ(labels[0].targetPc, 7);
    EXPECT_EQ(labels[0].targetDegree, 4);
    EXPECT_FALSE(labels[0].hasSeventh);
    EXPECT_EQ(labels[0].label, "V/V");
    EXPECT_FALSE(labels[1].isApplied);  // last region: no successor
}

// Same but the dominant carries a minor seventh → V7/V.
TEST(TonicizationLabeler, AppliedDominantSeventh_V7_of_V)
{
    std::vector<TonicizationRegionInput> regions = {
        region(0,   2, ChordQuality::Major, { 2, 6, 9, 0 }, 0, true, 0, /*m7=*/true),
        region(480, 7, ChordQuality::Major, { 7, 11, 2 }, 0, true, 0),
    };
    const auto labels = labelTonicizations(regions);
    EXPECT_TRUE(labels[0].isApplied);
    EXPECT_TRUE(labels[0].hasSeventh);
    EXPECT_EQ(labels[0].label, "V7/V");
}

// A7 (root 9) → D minor (root 2) in C major. C#=1 chromatic; target ii is minor
// → lowercase. V7/ii.
TEST(TonicizationLabeler, AppliedDominant_V7_of_ii_lowercase)
{
    std::vector<TonicizationRegionInput> regions = {
        region(0,   9, ChordQuality::Major, { 9, 1, 4, 7 }, 0, true, 0, /*m7=*/true),
        region(480, 2, ChordQuality::Minor, { 2, 5, 9 }, 0, true, 0),
    };
    const auto labels = labelTonicizations(regions);
    EXPECT_TRUE(labels[0].isApplied);
    EXPECT_EQ(labels[0].targetDegree, 1);
    EXPECT_FALSE(labels[0].targetIsMajor);
    EXPECT_EQ(labels[0].label, "V7/ii");
}

// ── Applied leading-tone ─────────────────────────────────────────────────────

// F#o (root 6) → G major (root 7) in C major. Root IS the chromatic leading tone
// of V. viio/V (triad).
TEST(TonicizationLabeler, AppliedLeadingTone_viio_of_V)
{
    std::vector<TonicizationRegionInput> regions = {
        region(0,   6, ChordQuality::Diminished, { 6, 9, 0 }, 0, true, 0),
        region(480, 7, ChordQuality::Major, { 7, 11, 2 }, 0, true, 0),
    };
    const auto labels = labelTonicizations(regions);
    EXPECT_TRUE(labels[0].isApplied);
    EXPECT_EQ(labels[0].kind, AppliedKind::AppliedLeadingTone);
    EXPECT_FALSE(labels[0].hasSeventh);
    EXPECT_EQ(labels[0].label, "viio/V");
}

// F#o7 (fully diminished) → G major. viio7/V.
TEST(TonicizationLabeler, AppliedLeadingTone_viio7_of_V)
{
    std::vector<TonicizationRegionInput> regions = {
        region(0,   6, ChordQuality::Diminished, { 6, 9, 0, 3 }, 0, true, 0,
               /*m7=*/false, /*dim7=*/true),
        region(480, 7, ChordQuality::Major, { 7, 11, 2 }, 0, true, 0),
    };
    const auto labels = labelTonicizations(regions);
    EXPECT_TRUE(labels[0].isApplied);
    EXPECT_TRUE(labels[0].hasSeventh);
    EXPECT_EQ(labels[0].label, "viio7/V");
}

// ── False-positive guards ────────────────────────────────────────────────────

// THE KEY GUARD: diatonic VII→III in A minor (G major → C major). The leading
// tone of III (=B) is DIATONIC to the 0-sharp signature, so this is ordinary
// diatonic motion, NOT a tonicization — exactly the relative-major trap that
// fooled the cadence detector. Must NOT be labeled.
TEST(TonicizationLabeler, RejectsDiatonicVII_to_III_inMinor)
{
    std::vector<TonicizationRegionInput> regions = {
        region(0,   7, ChordQuality::Major, { 7, 11, 2 }, 9, false, 0),  // G major
        region(480, 0, ChordQuality::Major, { 0, 4, 7 }, 9, false, 0),   // C major (III)
    };
    const auto labels = labelTonicizations(regions);
    EXPECT_FALSE(labels[0].isApplied);
}

// Plain V→I: the tonic target is excluded (so plain dominant→tonic stays a bare
// V, never "V/I").
TEST(TonicizationLabeler, RejectsTonicTarget_V_to_I)
{
    std::vector<TonicizationRegionInput> regions = {
        region(0,   7, ChordQuality::Major, { 7, 11, 2 }, 0, true, 0),  // G major
        region(480, 0, ChordQuality::Major, { 0, 4, 7 }, 0, true, 0),   // C major (I)
    };
    const auto labels = labelTonicizations(regions);
    EXPECT_FALSE(labels[0].isApplied);
}

// Deceptive V→vi: G major → A minor in C major. G is NOT the dominant of vi
// (the dominant of A is E), so no applied label despite a chromatic LT of vi.
TEST(TonicizationLabeler, RejectsDeceptive_V_to_vi)
{
    std::vector<TonicizationRegionInput> regions = {
        region(0,   7, ChordQuality::Major, { 7, 11, 2 }, 0, true, 0),  // G major
        region(480, 9, ChordQuality::Minor, { 9, 0, 4 }, 0, true, 0),   // A minor (vi)
    };
    const auto labels = labelTonicizations(regions);
    EXPECT_FALSE(labels[0].isApplied);
}

// A non-diatonic resolution target (root not a scale degree of the key) is out of
// this slice: C# major → ... in C major. C# is not a diatonic degree.
TEST(TonicizationLabeler, RejectsNonDiatonicTarget)
{
    std::vector<TonicizationRegionInput> regions = {
        region(0,   8, ChordQuality::Major, { 8, 0, 3 }, 0, true, 0),   // Ab major
        region(480, 1, ChordQuality::Major, { 1, 5, 8 }, 0, true, 0),   // C# major (chromatic root)
    };
    const auto labels = labelTonicizations(regions);
    EXPECT_FALSE(labels[0].isApplied);
}
