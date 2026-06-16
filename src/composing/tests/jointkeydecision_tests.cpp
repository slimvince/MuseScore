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

// jointkeydecision_tests.cpp — J-key-i.
//
// Pins the scoped constrained-joint KEY decision (jointkeydecision.{h,cpp}): the
// hard-fifths HOME-pair prune, soft relative-pair mode resolution (the measured
// floor), the production-key ECHO-not-read no-circularity property, the structural
// CHORD-PINNED class (matching the residual probe), and the attribution toggle's
// soft==joint identity when there is no coupled core. Inputs are built directly
// from root pc / quality / pitch mask — no resolved key — the structural proof of
// key-agnosticism.

#include <gtest/gtest.h>

#include <vector>

#include "composing/analysis/section/jointkeydecision.h"

using namespace mu::composing::analysis;

namespace {

uint16_t jkMask(std::initializer_list<int> pcs)
{
    uint16_t m = 0;
    for (int pc : pcs) {
        m |= static_cast<uint16_t>(1u << (((pc % 12) + 12) % 12));
    }
    return m;
}

JointKeyRegionInput reg(int startTick, int rootPc, ChordQuality q,
                        std::initializer_list<int> pcs, int bassPc = -1)
{
    JointKeyRegionInput r;
    r.startTick = startTick;
    r.endTick = startTick + 480;
    r.rootPc = rootPc;
    r.quality = q;
    r.pitchClassMask = jkMask(pcs);
    r.bassPc = (bassPc < 0 ? rootPc : bassPc);
    return r;
}

// Diatonic triads on a 480 grid.
JointKeyRegionInput Cmaj(int t) { return reg(t, 0, ChordQuality::Major, { 0, 4, 7 }); }
JointKeyRegionInput Fmaj(int t) { return reg(t, 5, ChordQuality::Major, { 5, 9, 0 }); }
JointKeyRegionInput Gmaj(int t) { return reg(t, 7, ChordQuality::Major, { 7, 11, 2 }); }
JointKeyRegionInput Dmin(int t) { return reg(t, 2, ChordQuality::Minor, { 2, 5, 9 }); }
JointKeyRegionInput Amin(int t) { return reg(t, 9, ChordQuality::Minor, { 9, 0, 4 }); }
// E major with G# (raised LT of A minor): an A-minor dominant.
JointKeyRegionInput Emaj(int t) { return reg(t, 4, ChordQuality::Major, { 4, 8, 11 }); }

} // namespace

// The home relative pair is computed from the notated fifths alone (hard prune):
// fifths 0 ⇒ C major (0) / A minor (9); fifths 1 ⇒ G major (7) / E minor (4).
TEST(JointKeyDecision, HomePairFromNotatedFifths)
{
    std::vector<JointKeyRegionInput> regions = { Cmaj(0), Gmaj(480), Cmaj(960) };

    const auto r0 = decideJointKey(regions, /*fifths=*/0);
    ASSERT_EQ(r0.decisions.size(), 3u);
    EXPECT_EQ(r0.decisions[0].homeMajorTonicPc, 0);
    EXPECT_EQ(r0.decisions[0].homeMinorTonicPc, 9);

    const auto r1 = decideJointKey(regions, /*fifths=*/1);
    EXPECT_EQ(r1.decisions[0].homeMajorTonicPc, 7);
    EXPECT_EQ(r1.decisions[0].homeMinorTonicPc, 4);
}

// A diatonic C-major run with a G→C authentic cadence resolves to C major; the
// soft decision never leaves the home fifths' relative pair.
TEST(JointKeyDecision, MajorRunResolvesToHomeMajor)
{
    std::vector<JointKeyRegionInput> regions = {
        Cmaj(0), Fmaj(480), Gmaj(960), Cmaj(1440), Fmaj(1920), Cmaj(2400),
    };
    const auto res = decideJointKey(regions, /*fifths=*/0);
    for (const auto& d : res.decisions) {
        // home pair is {C major (0), A minor (9)} — never another fifths
        const bool inHomePair = (d.softTonicPc == 0 && d.softIsMajor)
                                || (d.softTonicPc == 9 && !d.softIsMajor);
        EXPECT_TRUE(inHomePair) << "soft tonic=" << d.softTonicPc << " maj=" << d.softIsMajor;
    }
    EXPECT_EQ(res.decisions.back().softTonicPc, 0);
    EXPECT_TRUE(res.decisions.back().softIsMajor);
}

// Relative-pair recovery (the measured floor): an A-minor run with an E(G#)→Am
// cadence is read as A minor — same fifths (0) as C major, mode resolved to minor.
TEST(JointKeyDecision, RelativeMinorRecovered)
{
    std::vector<JointKeyRegionInput> regions = {
        Amin(0), Dmin(480), Emaj(960), Amin(1440), Dmin(1920), Emaj(2400), Amin(2880),
    };
    const auto res = decideJointKey(regions, /*fifths=*/0);
    // The cadence anchor should be A minor; the final tonic resolves there.
    EXPECT_EQ(res.decisions.back().softTonicPc, 9);
    EXPECT_FALSE(res.decisions.back().softIsMajor);
}

// No-circularity: the production resolved key is ECHOED, never read by the
// decision. A deliberately-wrong prod key does not perturb the soft/joint result.
TEST(JointKeyDecision, ProductionKeyEchoedNotRead)
{
    std::vector<JointKeyRegionInput> regions = { Cmaj(0), Gmaj(480), Cmaj(960) };
    for (auto& r : regions) {
        r.prodTonicPc = 3;       // Eb — deliberately wrong
        r.prodIsMajor = false;
    }
    const auto res = decideJointKey(regions, /*fifths=*/0);
    EXPECT_EQ(res.decisions.back().softTonicPc, 0);   // still home C major
    EXPECT_TRUE(res.decisions.back().softIsMajor);
    EXPECT_EQ(res.decisions[0].prodTonicPc, 3);       // echoed verbatim
    EXPECT_FALSE(res.decisions[0].prodIsMajor);
}

// The CHORD-PINNED flag reproduces the residual-probe PINNED class: a complete
// clear triad is pinned; a symmetric dim7 and a sparse dyad are chord-ambiguous.
TEST(JointKeyDecision, ChordPinnedClassification)
{
    std::vector<JointKeyRegionInput> regions = {
        reg(0, 0, ChordQuality::Major, { 0, 4, 7 }),           // clear C major — PINNED
        reg(480, 0, ChordQuality::Unknown, { 0, 3, 6, 9 }),    // dim7 (symmetric) — ambiguous
        reg(960, 0, ChordQuality::Unknown, { 0, 7 }),          // dyad (sparse) — ambiguous
    };
    const auto res = decideJointKey(regions, /*fifths=*/0);
    EXPECT_TRUE(res.decisions[0].chordPinned);
    EXPECT_FALSE(res.decisions[1].chordPinned);
    EXPECT_FALSE(res.decisions[2].chordPinned);
}

// Attribution toggle: with no committed modulation span there is no coupled core,
// so the scoped joint (config B) is identical to soft-only (config A) everywhere.
TEST(JointKeyDecision, NoCoupledCoreSoftEqualsJoint)
{
    std::vector<JointKeyRegionInput> regions = {
        Cmaj(0), Fmaj(480), Gmaj(960), Cmaj(1440), Fmaj(1920), Cmaj(2400),
    };
    const auto res = decideJointKey(regions, /*fifths=*/0);
    EXPECT_EQ(res.coupledCount, 0);
    for (const auto& d : res.decisions) {
        EXPECT_FALSE(d.jointChanged);
        EXPECT_EQ(d.softTonicPc, d.jointTonicPc);
        EXPECT_EQ(d.softIsMajor, d.jointIsMajor);
    }
}

// An empty region stream yields an empty decision set (no crash).
TEST(JointKeyDecision, EmptyInput)
{
    const auto res = decideJointKey({}, /*fifths=*/0);
    EXPECT_TRUE(res.decisions.empty());
    EXPECT_EQ(res.coupledCount, 0);
}
