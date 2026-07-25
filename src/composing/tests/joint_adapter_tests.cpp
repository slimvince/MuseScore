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

// Joint estimator, commit 2: the FittedAdapter factor log-probabilities. Every expected value below
// is the pinned Python probe_decoder.FittedAdapter(leftover_mode="freq", table_set="all") at identity
// weights for the same input — establishing the C++ factor port (#19), including the Katz leftover
// (marginal apportionment) path and the applied-relation transition path.

#include <gtest/gtest.h>

#include <optional>
#include <string>

#include "composing/analysis/joint/labelclass.h"
#include "composing/analysis/joint/jointadapter.h"

#ifndef JOINT_ARTIFACT_DIR
#define JOINT_ARTIFACT_DIR "."
#endif

namespace joint = mu::composing::analysis::joint;

class JointAdapterTest : public ::testing::Test
{
protected:
    void SetUp() override
    {
        adapter = joint::FittedAdapter::load(JOINT_ARTIFACT_DIR, "all");
        ASSERT_TRUE(adapter.loaded()) << adapter.error();
    }

    static joint::LabelClass lc(const char* k) { return joint::classFromKey(k); }

    joint::FittedAdapter adapter;
    static constexpr double kTol = 1e-9;
};

TEST_F(JointAdapterTest, Prior)
{
    EXPECT_NEAR(adapter.priorLogp(0, true, 0, ""), -3.178053830348, kTol);
    EXPECT_NEAR(adapter.priorLogp(0, true, 0, "major"), -0.740627718793, kTol);
    EXPECT_NEAR(adapter.priorLogp(9, false, 0, "minor"), -1.030571344907, kTol);
    EXPECT_NEAR(adapter.priorLogp(2, true, 2, ""), -3.178053830348, kTol);
    EXPECT_NEAR(adapter.priorLogp(0, true, std::nullopt, ""), 0.0, kTol);
    const auto terms = adapter.priorTerms(0, true, 0, "major");
    EXPECT_NEAR(terms.first, -3.178053830348, kTol);
    EXPECT_NEAR(terms.second, 2.437426111555, kTol);
}

TEST_F(JointAdapterTest, Entry)
{
    EXPECT_NEAR(adapter.entryLogp(lc("I | Maj |  | "), true), -2.740549368495, kTol);
    EXPECT_NEAR(adapter.entryLogp(lc("V | Dom7 | 7 | IV"), true), -5.503264225526, kTol);
}

TEST_F(JointAdapterTest, KeyTransition)
{
    EXPECT_NEAR(adapter.keyTransLogp(0, true, 0, true), -0.099897292985, kTol);
    EXPECT_NEAR(adapter.keyTransLogp(0, true, 9, false), -3.370285037859, kTol);
    EXPECT_NEAR(adapter.keyTransLogp(0, true, 7, true), -3.737117040494, kTol);
    EXPECT_NEAR(adapter.keyTransLogp(0, true, 6, true), -6.667730914669, kTol);
}

TEST_F(JointAdapterTest, ChordTransition)
{
    EXPECT_NEAR(adapter.chordTransLogp(lc("I | Maj |  | "), lc("V | Dom7 | 7 | "), true),
                -4.503970744126, kTol);
    // a rare outcome that backs off to a pooled bucket AND apportions by the mode marginal (option 2a)
    EXPECT_NEAR(adapter.chordTransLogp(lc("I | Maj |  | "), lc("bVII | Maj |  | "), true),
                -9.612493599085, kTol);
    // the applied-relation branch (the from-chord row's context_used starts with «rel»)
    EXPECT_NEAR(adapter.chordTransLogp(lc("II | HalfDim7 | 6/5 | vi"), lc("VI | Dom7 | 7 | "), true),
                -4.121067632363, kTol);
}

TEST_F(JointAdapterTest, Emission)
{
    EXPECT_NEAR(adapter.emissionLogp("member", "downbeat", "leap", "leap", false), -0.03598271788, kTol);
    EXPECT_NEAR(adapter.emissionLogp("outside", "sub_tactus", "step", "none", true), -5.387853331859, kTol);
}

TEST_F(JointAdapterTest, Spelling)
{
    EXPECT_NEAR(adapter.spellingLogp("dia:0", true), -1.58532601355, kTol);
    EXPECT_NEAR(adapter.spellingLogp("raised7", false), -2.578294860905, kTol);
    EXPECT_NEAR(adapter.spellingLogp("chr_sharp", true), -4.560900829679, kTol);
}

TEST_F(JointAdapterTest, Bass)
{
    const std::string root = "root";
    const std::string third = "third";
    EXPECT_NEAR(adapter.bassLogp(&root, "triad", "I", "Maj", true), -0.362320104303, kTol);
    EXPECT_NEAR(adapter.bassLogp(&third, "seventh", "V", "Dom7", true), -1.307922346721, kTol);
    EXPECT_NEAR(adapter.bassLogp(nullptr, "triad", "I", "Maj", true), -3.912023005428, kTol);
}

TEST_F(JointAdapterTest, FactorAbsent)
{
    EXPECT_NEAR(adapter.factorAbsentLogp("root", "triad"), -3.209247875505, kTol);
    EXPECT_NEAR(adapter.factorAbsentLogp("fifth", "seventh"), -1.929342811998, kTol);
}

TEST_F(JointAdapterTest, Boundary)
{
    EXPECT_NEAR(adapter.boundaryLogp("downbeat", true, false), -0.027710001954, kTol);
    EXPECT_NEAR(adapter.boundaryLogp("downbeat", false, true), -3.610122683974, kTol);
    EXPECT_NEAR(adapter.boundaryLogp("sub_tactus", true, false), -1.298742631344, kTol);
}

TEST_F(JointAdapterTest, IdentityWeightsAreGenerativeBaseline)
{
    EXPECT_DOUBLE_EQ(adapter.weights().get("emission"), 1.0);
    EXPECT_DOUBLE_EQ(adapter.weights().get("cad_leading_tone"), 0.0);
    EXPECT_FALSE(adapter.anyCadenceWeight());
}
