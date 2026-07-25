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

// Joint estimator, commit 2: the shared pitch/chord/label primitives. Every value below is the
// exact output of the pinned Python (gen_note_tables / gen_label_tables) for the same input —
// establishing the C++ port byte-for-byte (#19).

#include <gtest/gtest.h>

#include <string>
#include <vector>

#include "composing/analysis/joint/labelclass.h"
#include "composing/analysis/joint/jointprimitives.h"

namespace joint = mu::composing::analysis::joint;

static joint::PcMask mk(std::initializer_list<int> pcs)
{
    joint::PcMask m = 0;
    for (int p : pcs) {
        m |= static_cast<joint::PcMask>(1u << p);
    }
    return m;
}

TEST(JointPrimitivesTests, MemberPcs)
{
    EXPECT_EQ(joint::memberPcs(joint::classFromKey("I | Maj |  | "), 0, true), mk({ 0, 4, 7 }));
    EXPECT_EQ(joint::memberPcs(joint::classFromKey("V | Dom7 | 7 | "), 0, true), mk({ 2, 5, 7, 11 }));
    EXPECT_EQ(joint::memberPcs(joint::classFromKey("VII | Dim7 | 6/5 | "), 0, false), mk({ 2, 5, 8, 11 }));
    EXPECT_EQ(joint::memberPcs(joint::classFromKey("V | Dom7 | 7 | V"), 0, true), mk({ 0, 2, 6, 9 }));
    EXPECT_EQ(joint::memberPcs(joint::classFromKey("It | AugSixth | 6 | "), 0, true), mk({ 0, 6, 8 }));
    EXPECT_EQ(joint::memberPcs(joint::classFromKey("N | Neapolitan |  | "), 0, true), mk({ 1, 5, 8 }));
    EXPECT_EQ(joint::memberPcs(joint::classFromKey("I | Min |  | "), 9, false), mk({ 0, 4, 9 }));
    EXPECT_EQ(joint::memberPcs(joint::classFromKey("V | Maj7 | 6/5 | "), 7, true), mk({ 1, 2, 6, 9 }));
    EXPECT_EQ(joint::memberPcs(joint::classFromKey("I | Dom7 | 9[b9] | "), 2, true), mk({ 0, 2, 3, 6, 9 }));
    EXPECT_FALSE(joint::memberPcs(joint::classFromKey("raw:x | unknown |  | "), 0, true).has_value());
}

static void expectFactors(const char* key, int tonic, bool major,
                          const std::vector<std::pair<std::string, int> >& expected)
{
    const auto fac = joint::chordFactorPcs(joint::classFromKey(key), tonic, major);
    ASSERT_TRUE(fac.has_value()) << key;
    ASSERT_EQ(fac->size(), expected.size()) << key;
    for (size_t i = 0; i < expected.size(); ++i) {
        EXPECT_EQ((*fac)[i].role, expected[i].first) << key << " role " << i;
        EXPECT_EQ((*fac)[i].pc, expected[i].second) << key << " pc " << i;
    }
}

TEST(JointPrimitivesTests, ChordFactorPcs)
{
    expectFactors("I | Maj |  | ", 0, true, { { "root", 0 }, { "third", 4 }, { "fifth", 7 } });
    expectFactors("V | Dom7 | 7 | ", 0, true,
                  { { "root", 7 }, { "third", 11 }, { "fifth", 2 }, { "seventh", 5 } });
    expectFactors("VII | Dim7 | 6/5 | ", 0, false,
                  { { "root", 11 }, { "third", 2 }, { "fifth", 5 }, { "seventh", 8 } });
    expectFactors("V | Dom7 | 7 | V", 0, true,
                  { { "root", 2 }, { "third", 6 }, { "fifth", 9 }, { "seventh", 0 } });
    // chromatic classes have no standard factor roles (nullopt) but DO have member pcs.
    EXPECT_FALSE(joint::chordFactorPcs(joint::classFromKey("It | AugSixth | 6 | "), 0, true).has_value());
    EXPECT_FALSE(joint::chordFactorPcs(joint::classFromKey("N | Neapolitan |  | "), 0, true).has_value());
}

TEST(JointPrimitivesTests, NoteCategory)
{
    const joint::PcMask memI = mk({ 0, 4, 7 });
    EXPECT_EQ(joint::noteCategory(0, memI, 0, true), "member");
    EXPECT_EQ(joint::noteCategory(2, memI, 0, true), "within");
    EXPECT_EQ(joint::noteCategory(1, memI, 0, true), "outside");
    EXPECT_EQ(joint::noteCategory(1, memI, 0, false), "outside");
    EXPECT_EQ(joint::noteCategory(8, memI, 9, false), "within");
}

TEST(JointPrimitivesTests, SpellingBin)
{
    // rel -6..6, both modes (indexed rel+6).
    const char* major[] = { "chr_flat", "chr_flat", "chr_flat", "chr_flat", "chr_flat", "dia:-1",
                            "dia:0", "dia:1", "dia:2", "dia:3", "dia:4", "dia:5", "chr_sharp" };
    const char* minor[] = { "chr_flat", "chr_flat", "dia:-4", "dia:-3", "dia:-2", "dia:-1",
                            "dia:0", "dia:1", "dia:2", "raised6", "chr_sharp", "raised7", "chr_sharp" };
    for (int rel = -6; rel <= 6; ++rel) {
        EXPECT_EQ(joint::spellingBin(rel, true), major[rel + 6]) << "major rel " << rel;
        EXPECT_EQ(joint::spellingBin(rel, false), minor[rel + 6]) << "minor rel " << rel;
    }
}

TEST(JointPrimitivesTests, SpellingParent)
{
    EXPECT_FALSE(joint::spellingParent("BASE").has_value());
    EXPECT_EQ(joint::spellingParent("dia:-1").value(), "CLASS:diatonic");
    EXPECT_EQ(joint::spellingParent("raised6").value(), "CLASS:raised");
    EXPECT_EQ(joint::spellingParent("raised7").value(), "CLASS:raised");
    EXPECT_EQ(joint::spellingParent("chr_flat").value(), "CLASS:chromatic");
    EXPECT_EQ(joint::spellingParent("chr_sharp").value(), "CLASS:chromatic");
    EXPECT_EQ(joint::spellingParent("CLASS:diatonic").value(), "BASE");
    EXPECT_EQ(joint::spellingParent("CLASS:raised").value(), "BASE");
}

TEST(JointPrimitivesTests, EmitCovariateKeying)
{
    EXPECT_EQ(joint::emitDisplay("downbeat", "leap", "leap", false), "downbeat | leap | leap | 0");
    EXPECT_EQ(joint::emitDisplay("sub_tactus", "step", "none", true), "sub_tactus | step | none | 1");
    EXPECT_EQ(joint::emitContextChain("downbeat", "leap", "leap", false),
              (std::vector<std::string>{ "L0:downbeat|leap|leap|0", "L1:leap|leap", "L2:0", "BASE" }));
    EXPECT_EQ(joint::emitContextChain("sub_tactus", "step", "none", true),
              (std::vector<std::string>{ "L0:sub_tactus|step|none|1", "L1:step|none", "L2:1", "BASE" }));
    EXPECT_EQ(joint::emitContextChain("other_tactus", "none", "none", false),
              (std::vector<std::string>{ "L0:other_tactus|none|none|0", "L1:none|none", "L2:0", "BASE" }));
}

TEST(JointPrimitivesTests, KeyArithmetic)
{
    EXPECT_EQ(joint::collectionFifths(0, true), 0);
    EXPECT_EQ(joint::collectionFifths(9, false), 0);
    EXPECT_EQ(joint::collectionFifths(7, true), 1);
    EXPECT_EQ(joint::collectionFifths(2, false), -1);

    EXPECT_EQ(joint::foldFifthsDiff(-8), 4);
    EXPECT_EQ(joint::foldFifthsDiff(-6), 6);
    EXPECT_EQ(joint::foldFifthsDiff(-1), -1);
    EXPECT_EQ(joint::foldFifthsDiff(0), 0);
    EXPECT_EQ(joint::foldFifthsDiff(7), -5);
    EXPECT_EQ(joint::foldFifthsDiff(13), 1);

    EXPECT_EQ(joint::cofDistance(0, 7), 1);
    EXPECT_EQ(joint::cofDistance(0, 5), 1);
    EXPECT_EQ(joint::cofDistance(0, 6), 6);
    EXPECT_EQ(joint::cofDistance(0, 1), 5);
    EXPECT_EQ(joint::cofDistance(9, 2), 1);

    EXPECT_EQ(joint::keyChangeKind(0, true, 0, false), "parallel");
    EXPECT_EQ(joint::keyChangeKind(0, true, 9, false), "relative");
    EXPECT_EQ(joint::keyChangeKind(9, false, 0, true), "relative");
    EXPECT_EQ(joint::keyChangeKind(0, true, 7, true), "other");
    EXPECT_EQ(joint::keyChangeKind(0, true, 2, true), "other");
}

TEST(JointPrimitivesTests, TableKeyChains)
{
    EXPECT_EQ(joint::t1CtxChain(joint::classFromKey("I | Maj | 6 | ")),
              (std::vector<std::string>{ "L0:I | Maj | 6 | ", "L1:I | Maj |  | ",
                                         "L2:I | triad |  | ", "BASE" }));
    EXPECT_EQ(joint::t4CtxChain("III", "Aug7", "m"),
              (std::vector<std::string>{ "L0:III|Aug7|m", "L1:*|Aug7|m", "L2:*|*|m" }));

    using joint::Node;
    EXPECT_EQ(joint::t1OutcomeParent(Node::ofClass(joint::classFromKey("I | Maj | 6 | "))).value(),
              "«invfree» I | Maj |  | ");
    EXPECT_EQ(joint::t1OutcomeParent(Node::ofClass(joint::classFromKey("I | Maj |  | "))).value(),
              "«family» I | triad |  | ");
    EXPECT_EQ(joint::t1OutcomeParent(Node::ofClass(joint::classFromKey("V | Dom7 | 7 | IV"))).value(),
              "«invfree» V | Dom7 |  | IV");
    EXPECT_EQ(joint::t1OutcomeParent(Node::ofClass(joint::classFromKey("V | Dom7 |  | IV"))).value(),
              "«family» V | seventh |  | IV");
    EXPECT_EQ(joint::t1OutcomeParent(Node::ofStr("«invfree» I | Maj |  | ")).value(),
              "«family» I | triad |  | ");
    EXPECT_EQ(joint::t1OutcomeParent(Node::ofStr("«family» I | triad |  | ")).value(), "BASE");

    EXPECT_EQ(joint::t3EntryParent(Node::ofClass(joint::classFromKey("I | Maj | 6 | "))).value(),
              "«invfree» I | Maj |  | ");
    EXPECT_EQ(joint::t3EntryParent(Node::ofClass(joint::classFromKey("I | Maj |  | "))).value(), "BASE");
}

TEST(JointPrimitivesTests, AppliedRelation)
{
    using joint::Node;
    const joint::LabelClass appliedVofV = joint::classFromKey("V | Dom7 | 7 | V");
    EXPECT_EQ(joint::relationCell(appliedVofV, joint::classFromKey("V | Maj |  | ")),
              "«rel»resolve|triad|root");
    EXPECT_EQ(joint::relationCell(appliedVofV, joint::classFromKey("V | Dom7 | 6/5 | ")),
              "«rel»resolve|seventh|inv");
    EXPECT_EQ(joint::relationCell(appliedVofV, joint::classFromKey("I | Maj |  | ")),
              "«rel»elsewhere");

    EXPECT_EQ(joint::appliedRelParent(Node::ofStr("«rel»resolve|triad|root")).value(),
              "«rel»resolve|triad");
    EXPECT_EQ(joint::appliedRelParent(Node::ofStr("«rel»resolve|triad")).value(),
              "«rel»resolve");
    EXPECT_FALSE(joint::appliedRelParent(Node::ofStr("«rel»resolve")).has_value());
    EXPECT_FALSE(joint::appliedRelParent(Node::ofStr("«rel»elsewhere")).has_value());
}
