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

// cadencekeyanchor_tests.cpp — Stage 4c-i.
//
// Pins the key-agnostic authentic-cadence detector (cadencekeyanchor.{h,cpp}):
// the descending-fifth + leading-tone-present + stable-triad predicate and the
// finality-weighted aggregation vote. The detector reads ONLY root pc, quality,
// and a pitch-class mask — these tests construct those inputs directly, with no
// key/function context, which is the structural proof of key-agnosticism.

#include <gtest/gtest.h>

#include <vector>

#include "composing/analysis/section/cadencekeyanchor.h"

using namespace mu::composing::analysis;

namespace {

// Build a 12-bit pitch-class mask from a list of pitch classes.
uint16_t mask(std::initializer_list<int> pcs)
{
    uint16_t m = 0;
    for (int pc : pcs) {
        m |= static_cast<uint16_t>(1u << (((pc % 12) + 12) % 12));
    }
    return m;
}

CadenceRegionInput region(int startTick, int rootPc, ChordQuality q,
                          std::initializer_list<int> pcs)
{
    CadenceRegionInput r;
    r.startTick = startTick;
    r.endTick = startTick + 480;
    r.rootPc = rootPc;
    r.quality = q;
    r.pitchClassMask = mask(pcs);
    return r;
}

} // namespace

// G major (root 7, third B=11, fifth D=2) → C major (root 0). Leading tone B=11
// present in the dominant's mask. Textbook authentic cadence in C major.
TEST(CadenceKeyAnchor, AuthenticV_to_I_MajorTonic)
{
    std::vector<CadenceRegionInput> regions = {
        region(0, 7, ChordQuality::Major, { 7, 11, 2 }),   // G major (dominant)
        region(480, 0, ChordQuality::Major, { 0, 4, 7 }),  // C major (tonic)
    };
    const auto cadences = detectAuthenticCadences(regions);
    ASSERT_EQ(cadences.size(), 1u);
    EXPECT_EQ(cadences[0].tonicPc, 0);
    EXPECT_FALSE(cadences[0].minorMode);
    EXPECT_EQ(cadences[0].dominantTick, 0);
    EXPECT_EQ(cadences[0].tonicTick, 480);

    const auto anchor = aggregateGlobalAnchor(cadences);
    EXPECT_TRUE(anchor.detected);
    EXPECT_EQ(anchor.tonicPc, 0);
    EXPECT_FALSE(anchor.minorMode);
    EXPECT_EQ(anchor.cadenceCount, 1);
    EXPECT_DOUBLE_EQ(anchor.confidence, 1.0);
}

// E major (root 4, third G#=8) → A minor (root 9). Raised leading tone G#=8
// present — the relative-minor discriminator (G# is foreign to the 0-sharp
// signature shared by C major / A minor).
TEST(CadenceKeyAnchor, AuthenticV_to_i_MinorTonic_RaisedLeadingTone)
{
    std::vector<CadenceRegionInput> regions = {
        region(0, 4, ChordQuality::Major, { 4, 8, 11 }),    // E major (dominant of A)
        region(480, 9, ChordQuality::Minor, { 9, 0, 4 }),   // A minor (tonic)
    };
    const auto cadences = detectAuthenticCadences(regions);
    ASSERT_EQ(cadences.size(), 1u);
    EXPECT_EQ(cadences[0].tonicPc, 9);
    EXPECT_TRUE(cadences[0].minorMode);

    const auto anchor = aggregateGlobalAnchor(cadences);
    EXPECT_TRUE(anchor.detected);
    EXPECT_EQ(anchor.tonicPc, 9);
    EXPECT_TRUE(anchor.minorMode);
}

// A dominant seventh is Major quality + a 7th — still admitted as the dominant.
TEST(CadenceKeyAnchor, DominantSeventhAdmitted)
{
    std::vector<CadenceRegionInput> regions = {
        region(0, 7, ChordQuality::Major, { 7, 11, 2, 5 }), // G7 (B leading tone present)
        region(480, 0, ChordQuality::Major, { 0, 4, 7 }),   // C
    };
    EXPECT_EQ(detectAuthenticCadences(regions).size(), 1u);
}

// Leading tone (the dominant's major third) absent from the pitch content ⇒ not
// an authentic cadence, even though the Major label and fifth motion match.
TEST(CadenceKeyAnchor, LeadingToneMustBePresentInPitchContent)
{
    std::vector<CadenceRegionInput> regions = {
        region(0, 7, ChordQuality::Major, { 7, 2 }),       // G with no B (no third sounding)
        region(480, 0, ChordQuality::Major, { 0, 4, 7 }),  // C
    };
    EXPECT_TRUE(detectAuthenticCadences(regions).empty());
}

// Minor "dominant" (v) does not carry a leading tone ⇒ rejected.
TEST(CadenceKeyAnchor, MinorDominantRejected)
{
    std::vector<CadenceRegionInput> regions = {
        region(0, 7, ChordQuality::Minor, { 7, 10, 2 }),   // G minor
        region(480, 0, ChordQuality::Major, { 0, 4, 7 }),  // C
    };
    EXPECT_TRUE(detectAuthenticCadences(regions).empty());
}

// Diminished resolution target is not a stable triad ⇒ rejected.
TEST(CadenceKeyAnchor, DiminishedTonicRejected)
{
    std::vector<CadenceRegionInput> regions = {
        region(0, 7, ChordQuality::Major, { 7, 11, 2 }),
        region(480, 0, ChordQuality::Diminished, { 0, 3, 6 }),
    };
    EXPECT_TRUE(detectAuthenticCadences(regions).empty());
}

// Wrong root motion (ascending fifth / plagal-like) ⇒ rejected.
TEST(CadenceKeyAnchor, NonDescendingFifthRejected)
{
    std::vector<CadenceRegionInput> regions = {
        region(0, 5, ChordQuality::Major, { 5, 9, 0 }),    // F major → C is a fourth, not V→I
        region(480, 0, ChordQuality::Major, { 0, 4, 7 }),
    };
    EXPECT_TRUE(detectAuthenticCadences(regions).empty());
}

// Gap region (rootPc < 0) is never a cadence member.
TEST(CadenceKeyAnchor, GapRegionSkipped)
{
    std::vector<CadenceRegionInput> regions = {
        region(0, 7, ChordQuality::Major, { 7, 11, 2 }),
        region(480, -1, ChordQuality::Unknown, {}),        // gap
    };
    EXPECT_TRUE(detectAuthenticCadences(regions).empty());
}

// Finality weighting: an early cadence to G major and a final cadence to C
// major — the later (heavier) cadence wins the global anchor.
TEST(CadenceKeyAnchor, FinalityWeightedVoteFavorsLastCadence)
{
    std::vector<AuthenticCadence> cadences = {
        { 0, 480, 7, false },     // → G major (weight 1)
        { 960, 1440, 0, false },  // → C major (weight 2, final)
    };
    const auto anchor = aggregateGlobalAnchor(cadences);
    EXPECT_TRUE(anchor.detected);
    EXPECT_EQ(anchor.tonicPc, 0);
    EXPECT_FALSE(anchor.minorMode);
    EXPECT_EQ(anchor.cadenceCount, 2);
    // weight share of the winner = 2 / (1 + 2).
    EXPECT_DOUBLE_EQ(anchor.confidence, 2.0 / 3.0);
}

// Two cadences agreeing on the same tonic ⇒ full confidence.
TEST(CadenceKeyAnchor, AgreeingCadencesFullConfidence)
{
    std::vector<AuthenticCadence> cadences = {
        { 0, 480, 0, false },
        { 960, 1440, 0, false },
    };
    const auto anchor = aggregateGlobalAnchor(cadences);
    EXPECT_EQ(anchor.tonicPc, 0);
    EXPECT_DOUBLE_EQ(anchor.confidence, 1.0);
}

// No cadences ⇒ undetected anchor.
TEST(CadenceKeyAnchor, EmptyAnchorUndetected)
{
    const auto anchor = aggregateGlobalAnchor({});
    EXPECT_FALSE(anchor.detected);
    EXPECT_EQ(anchor.cadenceCount, 0);
    EXPECT_EQ(anchor.tonicPc, -1);
}

// ── Stage 4c-iii refinements ────────────────────────────────────────────────

// Signature-relative chromatic leading tone: E→Am in a 0-sharp signature carries
// the raised LT G# (chromatic ⇒ genuine minor V→i marker); G→C carries the
// diatonic B (not chromatic ⇒ a relative-major tonicization).
TEST(CadenceKeyAnchor, ChromaticLeadingToneFromSignature_ZeroSharp)
{
    std::vector<CadenceRegionInput> minorCad = {
        region(0, 4, ChordQuality::Major, { 4, 8, 11 }),    // E major
        region(480, 9, ChordQuality::Minor, { 9, 0, 4 }),   // A minor
    };
    auto cm = detectAuthenticCadences(minorCad, /*keySignatureFifths=*/0);
    ASSERT_EQ(cm.size(), 1u);
    EXPECT_TRUE(cm[0].chromaticLeadingTone);   // G# foreign to 0-sharp

    std::vector<CadenceRegionInput> majorCad = {
        region(0, 7, ChordQuality::Major, { 7, 11, 2 }),    // G major
        region(480, 0, ChordQuality::Major, { 0, 4, 7 }),   // C major
    };
    auto cM = detectAuthenticCadences(majorCad, /*keySignatureFifths=*/0);
    ASSERT_EQ(cM.size(), 1u);
    EXPECT_FALSE(cM[0].chromaticLeadingTone);  // B is in the 0-sharp collection
}

// The chromatic test is RELATIVE to the signature: in a 1-sharp signature (G
// major / E minor) the B→C leading tone of a V→I in C is still diatonic, but the
// D#→E leading tone of a B→Em cadence is chromatic to that signature.
TEST(CadenceKeyAnchor, ChromaticLeadingToneFromSignature_OneSharp)
{
    // B major → E minor: LT = D# (= (11+4) mod 12 = 3). 1-sharp collection is
    // {G..F#} = {7,9,11,0,2,4,6}; D#=3 is foreign ⇒ chromatic (raised LT of e minor).
    std::vector<CadenceRegionInput> em = {
        region(0, 11, ChordQuality::Major, { 11, 3, 6 }),   // B major
        region(480, 4, ChordQuality::Minor, { 4, 7, 11 }),  // E minor
    };
    auto c = detectAuthenticCadences(em, /*keySignatureFifths=*/1);
    ASSERT_EQ(c.size(), 1u);
    EXPECT_TRUE(c[0].chromaticLeadingTone);
}

// Structural-vs-interior discrimination: one phrase-final V→i (structural,
// raised LT) must outweigh several interior diatonic V→III tonicizations — the
// 4c-i relative-major swamping failure mode, fixed.
TEST(CadenceKeyAnchor, StructuralRaisedLTOutweighsInteriorTonicizations)
{
    // Three interior G→C cadences (diatonic) + one phrase-final E→Am (raised LT).
    std::vector<AuthenticCadence> cadences = {
        // dominantTick, tonicTick, tonicPc, minorMode, endsPhrase, chromaticLT
        { 0,    480,  0, false, false, false },   // → C major (interior)
        { 960,  1440, 0, false, false, false },   // → C major (interior)
        { 1920, 2400, 0, false, false, false },   // → C major (interior)
        { 2880, 3360, 9, true,  true,  true  },   // → A minor (structural, raised LT)
    };
    const auto anchor = aggregateGlobalAnchor(cadences);
    EXPECT_TRUE(anchor.detected);
    EXPECT_EQ(anchor.tonicPc, 9);
    EXPECT_TRUE(anchor.minorMode);
}

// Picardy correction: an A-minor body (interior i cadences) ending on a major
// tonic triad (Picardy third) must NOT flip the global mode to major.
TEST(CadenceKeyAnchor, PicardyThirdDoesNotFlipToMajor)
{
    std::vector<AuthenticCadence> cadences = {
        { 0,    480,  9, true,  true, true },    // → A minor (structural)
        { 960,  1440, 9, true,  true, true },    // → A minor (structural)
        { 1920, 2400, 9, false, true, true },    // → A MAJOR final (Picardy third)
    };
    const auto anchor = aggregateGlobalAnchor(cadences);
    EXPECT_TRUE(anchor.detected);
    EXPECT_EQ(anchor.tonicPc, 9);
    EXPECT_TRUE(anchor.minorMode);   // corrected away from the Picardy major
}

// A genuinely major key (no i cadences to its tonic) is never flipped by the
// Picardy correction.
TEST(CadenceKeyAnchor, GenuineMajorNotFlippedByPicardy)
{
    std::vector<AuthenticCadence> cadences = {
        { 0,    480,  0, false, true, false },   // → C major
        { 960,  1440, 0, false, true, false },   // → C major
    };
    const auto anchor = aggregateGlobalAnchor(cadences);
    EXPECT_EQ(anchor.tonicPc, 0);
    EXPECT_FALSE(anchor.minorMode);
}

// endsPhrase propagates from the resolution region to the cadence.
TEST(CadenceKeyAnchor, EndsPhrasePropagatesFromTonicRegion)
{
    std::vector<CadenceRegionInput> regions = {
        region(0, 7, ChordQuality::Major, { 7, 11, 2 }),    // G major
        region(480, 0, ChordQuality::Major, { 0, 4, 7 }),   // C major
    };
    regions[1].endsPhrase = true;                            // resolution ends a phrase
    auto c = detectAuthenticCadences(regions, /*keySignatureFifths=*/0);
    ASSERT_EQ(c.size(), 1u);
    EXPECT_TRUE(c[0].endsPhrase);
}
