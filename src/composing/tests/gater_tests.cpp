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

// gater_tests.cpp
//
// Unit tests for Gate R (the rcb bass-chord-tone guard, docs/scoring_model.md §4):
//   - bassIsTemplateChordTone(): the kMasks template-membership table. These tests
//     independently encode the 17 template interval sets, so a kMasks corruption (or a
//     template addition that forgets to update kMasks — the 5th atomic-update site of
//     §9) is caught here rather than as a silent scoring bug.
//   - gateRZeroesRootContinuity(): the four branches of the Gate R decision (rcb>0,
//     !explorationMode, basisDep<=0, bass foreign to template).

#include <gtest/gtest.h>

#include <array>
#include <vector>

#include "composing/analysis/function/harmonicfunctionlayer.h"

using namespace mu::composing::function;

namespace {

// The 17 template interval sets, mirroring kMasks in harmonicfunctionlayer.cpp and the
// TemplateDef array in chordanalyzer.cpp. Encoded independently on purpose: if kMasks
// drifts from the templates, the table test below fails.
const std::array<std::vector<int>, 17> kTemplateIntervals = { {
    { 0, 4, 7 },         // 0  Major triad   {0,4,7}
    { 0, 4, 7, 11 },     // 1  Maj7          {0,4,7,11}
    { 0, 4, 7, 10 },     // 2  Dom7          {0,4,7,10}
    { 0, 4, 6, 10 },     // 3  Dom7b5        {0,4,6,10}
    { 0, 3, 7 },         // 4  Minor triad   {0,3,7}
    { 0, 3, 7, 10 },     // 5  Min7          {0,3,7,10}
    { 0, 3, 6 },         // 6  Diminished    {0,3,6}
    { 0, 5, 6, 10 },     // 7  Sus4b5        {0,5,6,10}
    { 0, 3, 6, 10 },     // 8  HalfDim       {0,3,6,10}
    { 0, 4, 8 },         // 9  Augmented     {0,4,8}
    { 0, 4, 8, 10 },     // 10 Aug dom7      {0,4,8,10}
    { 0, 2, 7 },         // 11 Sus2          {0,2,7}
    { 0, 5, 7, 10 },     // 12 Sus4+m7       {0,5,7,10}
    { 0, 5, 7, 11 },     // 13 Sus4+Maj7     {0,5,7,11}
    { 0, 5, 8, 10 },     // 14 Sus4#5        {0,5,8,10}
    { 0, 6, 7 },         // 15 Sus#4         {0,6,7}
    { 0, 7 },            // 16 Power         {0,7}
} };

bool contains(const std::vector<int>& v, int x)
{
    for (int i : v) {
        if (i == x) {
            return true;
        }
    }
    return false;
}

ScoringCell makeCell(int rootPc, int tiePriority, int bassPc, double basisDep)
{
    ScoringCell c{};
    c.rootPc      = rootPc;
    c.tiePriority = tiePriority;
    c.bassPc      = bassPc;
    c.basisDep    = basisDep;
    return c;
}

} // namespace

// ── F1: bassIsTemplateChordTone table ─────────────────────────────────────────

// For every template, every interval IN the template must pass and at least one
// interval NOT in the template must fail. rootPc=0 makes interval == bassPc.
TEST(Composing_GateRTests, BassIsTemplateChordTone_TableMatchesEveryTemplate)
{
    for (int tpl = 0; tpl < 17; ++tpl) {
        bool sawForeign = false;
        for (int interval = 0; interval < 12; ++interval) {
            const bool expected = contains(kTemplateIntervals[static_cast<size_t>(tpl)], interval);
            EXPECT_EQ(bassIsTemplateChordTone(0, tpl, interval), expected)
                << "tpl=" << tpl << " interval=" << interval;
            if (!expected) {
                sawForeign = true;
            }
        }
        EXPECT_TRUE(sawForeign) << "tpl=" << tpl << " must have at least one foreign interval";
    }
}

// The bass interval is (bassPc - rootPc) mod 12, so a non-zero root must be respected.
TEST(Composing_GateRTests, BassIsTemplateChordTone_RootOffsetIsRespected)
{
    // Eb major (rootPc=3) {Eb,G,Bb}: G (7) is the M3 (chord tone); Ab (8) is interval 5
    // (foreign) — the exact bwv102.7 Eb/Ab slash geometry.
    EXPECT_TRUE(bassIsTemplateChordTone(3, /*Major*/ 0, /*G*/ 7));
    EXPECT_FALSE(bassIsTemplateChordTone(3, /*Major*/ 0, /*Ab*/ 8));
}

// Interval 9 (a major sixth above the root) is the Δ=+7b foreign-bass interval; it must
// be foreign to every triad template Gate R targets.
TEST(Composing_GateRTests, BassIsTemplateChordTone_DeltaSevenForeignBassFails)
{
    EXPECT_FALSE(bassIsTemplateChordTone(0, /*Major*/ 0, 9));
    EXPECT_FALSE(bassIsTemplateChordTone(0, /*Minor*/ 4, 9));
    EXPECT_FALSE(bassIsTemplateChordTone(0, /*Diminished*/ 6, 9));
    EXPECT_FALSE(bassIsTemplateChordTone(0, /*Power*/ 16, 9));
    EXPECT_FALSE(bassIsTemplateChordTone(0, /*Power*/ 16, 5));
}

// Out-of-range / unknown inputs return true (conservative — never gate when unsure).
TEST(Composing_GateRTests, BassIsTemplateChordTone_ConservativeOnOutOfRange)
{
    EXPECT_TRUE(bassIsTemplateChordTone(0, /*tiePriority*/ -1, 9));
    EXPECT_TRUE(bassIsTemplateChordTone(0, /*tiePriority*/ 17, 9));
    EXPECT_TRUE(bassIsTemplateChordTone(/*rootPc*/ -1, 0, 9));
    EXPECT_TRUE(bassIsTemplateChordTone(0, 0, /*bassPc*/ -1));
}

// ── F2: Gate R decision branches ──────────────────────────────────────────────

// Branch 1 — bass is a template chord tone, basisDep==0: Gate R does NOT zero rcb.
TEST(Composing_GateRTests, GateR_DoesNotFire_WhenBassIsChordTone)
{
    const ScoringCell cell = makeCell(/*root*/ 0, /*Major*/ 0, /*bass=M3*/ 4, /*basisDep*/ 0.0);
    EXPECT_FALSE(gateRZeroesRootContinuity(cell, /*rcb*/ 0.40, /*explorationMode*/ false));
}

// Branch 2 — bass NOT a template chord tone, basisDep==0: Gate R ZEROES rcb.
TEST(Composing_GateRTests, GateR_Fires_WhenBassForeignAndBasisDepZero)
{
    const ScoringCell cell = makeCell(0, /*Major*/ 0, /*foreign interval 9*/ 9, /*basisDep*/ 0.0);
    EXPECT_TRUE(gateRZeroesRootContinuity(cell, 0.40, false));
}

// Branch 3 — bass foreign but basisDep>0 (legitimate extended slash, e.g. Cm7add11/F):
// Gate R does NOT zero rcb (the sounding-third inversion bonus spares it).
TEST(Composing_GateRTests, GateR_DoesNotFire_WhenBasisDepPositive)
{
    const ScoringCell cell = makeCell(0, /*Major*/ 0, 9, /*basisDep*/ 0.5);
    EXPECT_FALSE(gateRZeroesRootContinuity(cell, 0.40, false));
}

// Branch 4 — explorationMode=true, bass foreign, basisDep==0: Gate R does NOT fire
// (segmentation must stay byte-identical to baseline).
TEST(Composing_GateRTests, GateR_DoesNotFire_InExplorationMode)
{
    const ScoringCell cell = makeCell(0, /*Major*/ 0, 9, 0.0);
    EXPECT_FALSE(gateRZeroesRootContinuity(cell, 0.40, /*explorationMode*/ true));
}

// rcb==0 (no root continuity for this candidate): Gate R is a no-op regardless of bass.
TEST(Composing_GateRTests, GateR_DoesNotFire_WhenNoRootContinuity)
{
    const ScoringCell cell = makeCell(0, /*Major*/ 0, 9, 0.0);
    EXPECT_FALSE(gateRZeroesRootContinuity(cell, /*rcb*/ 0.0, false));
}
