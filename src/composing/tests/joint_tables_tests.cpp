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

// Commit 1 of the joint-estimator C++ module build: the LabelClass value type, the weight
// vector, and the runtime loader for the committed generative tables. These unit tests
// exercise every loaded structure against exact known values from the committed all-326
// artifacts under tools/joint_estimator/, and the LabelClass key round-trip / back-off
// helpers against probe_decoder / normalize semantics. The module is DORMANT — no
// production path reads it; these are its establishment tests.

#include <gtest/gtest.h>

#include "composing/analysis/joint/labelclass.h"
#include "composing/analysis/joint/jointtables.h"
#include "composing/analysis/joint/jointweights.h"

#ifndef JOINT_ARTIFACT_DIR
#define JOINT_ARTIFACT_DIR "."
#endif

namespace joint = mu::composing::analysis::joint;

// ── LabelClass — key() / classFromKey() round-trip and the back-off helpers ────────────

TEST(JointLabelClassTests, KeyRendersFourPipeSeparatedFields)
{
    const joint::LabelClass lc("V", "Dom7", "6/5", "IV");
    EXPECT_EQ(lc.key(), "V | Dom7 | 6/5 | IV");
}

TEST(JointLabelClassTests, ClassFromKeyParsesFourFields)
{
    const joint::LabelClass lc = joint::classFromKey("V | Dom7 | 2 | IV");
    EXPECT_EQ(lc.degreeBase(), "V");
    EXPECT_EQ(lc.quality(), "Dom7");
    EXPECT_EQ(lc.inversion(), "2");
    EXPECT_EQ(lc.target(), "IV");
    EXPECT_FALSE(lc.rawUnnormalized());
}

TEST(JointLabelClassTests, ClassFromKeyHandlesEmptyInnerAndTrailingFields)
{
    // "I | Maj |  | " has an empty inversion and empty target (two spaces between pipes).
    const joint::LabelClass lc = joint::classFromKey("I | Maj |  | ");
    EXPECT_EQ(lc.degreeBase(), "I");
    EXPECT_EQ(lc.quality(), "Maj");
    EXPECT_EQ(lc.inversion(), "");
    EXPECT_EQ(lc.target(), "");
    // The Neapolitan completion key (probe_decoder.CHROMATIC_COMPLETION_KEYS).
    const joint::LabelClass n = joint::classFromKey("N | Neapolitan |  | ");
    EXPECT_EQ(n.degreeBase(), "N");
    EXPECT_EQ(n.quality(), "Neapolitan");
    EXPECT_EQ(n.inversion(), "");
    EXPECT_EQ(n.target(), "");
}

TEST(JointLabelClassTests, KeyClassFromKeyRoundTrip)
{
    for (const char* k : { "V | Dom7 | 6/5 | IV", "I | Maj |  | ", "It | AugSixth | 6 | ii",
                           "N | Neapolitan |  | " }) {
        EXPECT_EQ(joint::classFromKey(k).key(), std::string(k));
    }
}

TEST(JointLabelClassTests, InversionFreeDropsTheFigure)
{
    EXPECT_EQ(joint::classFromKey("I | Maj | 6 | ").inversionFree().key(), "I | Maj |  | ");
    EXPECT_EQ(joint::classFromKey("V | Dom7 | 6/5 | IV").inversionFree().key(), "V | Dom7 |  | IV");
}

TEST(JointLabelClassTests, FamilyReducesQualityToTriadOrSeventh)
{
    EXPECT_EQ(joint::classFromKey("V | Dom7 | 7 | ").family().key(), "V | seventh |  | ");
    EXPECT_EQ(joint::classFromKey("I | Maj | 6 | ").family().key(), "I | triad |  | ");
    EXPECT_EQ(joint::classFromKey("VII | HalfDim7 | 6/5 | ").family().key(), "VII | seventh |  | ");
}

TEST(JointLabelClassTests, IsSeventhQualityMatchesTheEightNames)
{
    for (const char* q : { "Dom7", "Maj7", "Min7", "MinMaj7", "Dim7", "HalfDim7", "Aug7", "AugMaj7" }) {
        EXPECT_TRUE(joint::isSeventhQuality(q)) << q;
    }
    for (const char* q : { "Maj", "Min", "Dim", "HalfDim", "Aug", "AugSixth", "Neapolitan", "" }) {
        EXPECT_FALSE(joint::isSeventhQuality(q)) << q;
    }
}

// ── Weight vector — the identity (generative-baseline) setting ─────────────────────────

TEST(JointWeightsTests, WeightNameRosterMatchesProbeDecoder)
{
    ASSERT_EQ(joint::kWeightNames.size(), 13u);
    ASSERT_EQ(joint::kGenerativeWeightNames.size(), 9u);
    EXPECT_EQ(joint::kWeightNames.front(), "prior");
    EXPECT_EQ(joint::kWeightNames[8], "entry");
    EXPECT_EQ(joint::kWeightNames[9], "cad_leading_tone");
    EXPECT_EQ(joint::kWeightNames.back(), "cad_fermata_location");
}

TEST(JointWeightsTests, IdentityIsGenerativeOnesAndCadenceZeros)
{
    const joint::WeightVector w = joint::identityWeights();
    for (const std::string& n : joint::kGenerativeWeightNames) {
        EXPECT_DOUBLE_EQ(w.get(n), 1.0) << n;
    }
    EXPECT_DOUBLE_EQ(w.get("cad_leading_tone"), 0.0);
    EXPECT_DOUBLE_EQ(w.get("cad_tritone_pair"), 0.0);
    EXPECT_DOUBLE_EQ(w.get("cad_dominant_tonic_bass"), 0.0);
    EXPECT_DOUBLE_EQ(w.get("cad_fermata_location"), 0.0);
    // An unknown name reads 0.0.
    EXPECT_DOUBLE_EQ(w.get("no_such_weight"), 0.0);
}

// ── Table loading — every loaded structure against exact committed all-326 values ──────

class JointTablesLoadTest : public ::testing::Test
{
protected:
    void SetUp() override
    {
        tables = joint::JointTables::load(JOINT_ARTIFACT_DIR, "all");
        ASSERT_TRUE(tables.loaded) << tables.error;
    }

    joint::JointTables tables;
};

TEST_F(JointTablesLoadTest, Provenance)
{
    EXPECT_EQ(tables.corpusGitHash, "57ed94a6a46571172a351c09ba4f5cb92930674a");
    EXPECT_EQ(tables.tableSet, "all");
}

TEST_F(JointTablesLoadTest, ChordTransitionTable1)
{
    EXPECT_EQ(tables.t1Major.rows.size(), 124u);
    EXPECT_EQ(tables.t1Minor.rows.size(), 151u);

    ASSERT_TRUE(tables.t1Major.rows.count("I | Maj |  | "));
    const joint::KatzRow& row = tables.t1Major.rows.at("I | Maj |  | ");
    EXPECT_EQ(row.contextUsed, "L0:I | Maj |  | ");
    EXPECT_DOUBLE_EQ(row.dist.at("BASE"), 0.09043233906981321);
    EXPECT_DOUBLE_EQ(row.dist.at("I | Maj |  | "), 0.15601703940362088);

    // The derived level back-off map holds the row's own context_used -> its dist.
    ASSERT_TRUE(tables.t1Major.levels.count("L0:I | Maj |  | "));
    EXPECT_DOUBLE_EQ(tables.t1Major.levels.at("L0:I | Maj |  | ").at("BASE"), 0.09043233906981321);
}

TEST_F(JointTablesLoadTest, KeyTransitionTable2)
{
    EXPECT_DOUBLE_EQ(tables.t2.at("cof1|MM"), 0.023822684059252707);
    EXPECT_DOUBLE_EQ(tables.t2.at("BASE"), 0.0012712801238116134);
}

TEST_F(JointTablesLoadTest, EntryChordTable3)
{
    EXPECT_DOUBLE_EQ(tables.t3.at("BASE"), 0.14487658466963305);
    EXPECT_DOUBLE_EQ(tables.t3.at("I | Maj |  | "), 0.06453488372093023);
}

TEST_F(JointTablesLoadTest, BassInversionTable4)
{
    ASSERT_TRUE(tables.t4.rows.count("III|Aug7|m"));
    const joint::KatzRow& row = tables.t4.rows.at("III|Aug7|m");
    EXPECT_EQ(row.contextUsed, "L2:*|*|m");
    EXPECT_DOUBLE_EQ(row.dist.at(""), 0.4827633007600434);
    EXPECT_TRUE(tables.t4.levels.count("L2:*|*|m"));
}

TEST_F(JointTablesLoadTest, SignaturePriorTable5)
{
    ASSERT_TRUE(tables.t5.count("major"));
    ASSERT_TRUE(tables.t5.count("minor"));
    ASSERT_TRUE(tables.t5.count("none"));
    EXPECT_DOUBLE_EQ(tables.t5.at("none").at("BASE"), 1.0);
}

TEST_F(JointTablesLoadTest, EmissionAndSpelling)
{
    ASSERT_TRUE(tables.emission.rows.count("downbeat | leap | leap | 0"));
    EXPECT_DOUBLE_EQ(tables.emission.rows.at("downbeat | leap | leap | 0").dist.at("member"),
                     0.9646569646569647);

    ASSERT_TRUE(tables.spelling.count("major"));
    ASSERT_TRUE(tables.spelling.count("minor"));
    EXPECT_DOUBLE_EQ(tables.spelling.at("major").at("dia:-1"), 0.11590608848819153);
}

TEST_F(JointTablesLoadTest, BoundaryProbability)
{
    EXPECT_DOUBLE_EQ(tables.boundaryProb.at("downbeat"), 0.9727526781555659);
}

TEST_F(JointTablesLoadTest, FactorAbsence)
{
    EXPECT_DOUBLE_EQ(tables.factorAbsent.at("root|triad"), 0.04038697788697787);
    EXPECT_EQ(tables.factorAbsent.size(), 7u);   // the seven role|family cells
}

TEST_F(JointTablesLoadTest, FermataCrossedBoundaryCells)
{
    ASSERT_TRUE(tables.fermBoundaryFerm.count("downbeat"));
    const joint::BoundaryCell& f = tables.fermBoundaryFerm.at("downbeat");
    EXPECT_TRUE(f.present);
    EXPECT_TRUE(f.reliable);
    EXPECT_DOUBLE_EQ(f.prob, 0.9729514717581543);

    ASSERT_TRUE(tables.fermBoundaryNoFerm.count("downbeat"));
    const joint::BoundaryCell& nf = tables.fermBoundaryNoFerm.at("downbeat");
    EXPECT_TRUE(nf.present);
    EXPECT_TRUE(nf.reliable);
    EXPECT_DOUBLE_EQ(nf.prob, 0.9726703984194929);
}

TEST(JointTablesTests, LoadFailsGracefullyOnMissingDir)
{
    const joint::JointTables t = joint::JointTables::load(
        std::string(JOINT_ARTIFACT_DIR) + "/no_such_joint_subdir", "all");
    EXPECT_FALSE(t.loaded);
    EXPECT_FALSE(t.error.empty());
}
