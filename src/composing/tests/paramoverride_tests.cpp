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

// paramoverride_tests.cpp — Stage-5 fitter: the parameter-override loader (design D-6).
//
// Covers the new src/ paths: the by-name registry (registration + lookup), the strict
// line-based loader (parse, comments, unknown-name rejection, malformed-value rejection,
// missing-file rejection), the global-constant vs prefs-field dispatch, int/bool
// coercion, and the kStepBudget derived-constant recompute. Every test that mutates a
// PROCESS-GLOBAL scoring constant runs under a fixture that snapshots ALL registered
// globals in SetUp and restores them in TearDown, so no test leaves the scorer perturbed
// (the byte-identity contract is a whole-process property).

#include <gtest/gtest.h>

#include <filesystem>
#include <fstream>
#include <map>
#include <stdexcept>
#include <string>

#include "composing/analysis/param/paramoverride.h"
#include "composing/analysis/types/analysistypes.h"

namespace P = mu::composing::params;
using mu::composing::analysis::ChordAnalyzerPreferences;

namespace {

// Write @p content to a fresh temp file; return its path. Caller removes it.
std::string writeTempOverride(const std::string& stem, const std::string& content)
{
    const auto dir = std::filesystem::temp_directory_path();
    const auto path = (dir / ("paramoverride_test_" + stem + ".txt")).string();
    std::ofstream ofs(path, std::ios::binary | std::ios::trunc);
    ofs << content;
    ofs.close();
    return path;
}

// Fixture: snapshot every registered global before each test, restore after — so a test
// may freely mutate globals without leaking the change into the rest of the suite.
class ParamOverride : public ::testing::Test {
protected:
    void SetUp() override
    {
        for (const auto& name : P::registeredGlobalNames()) {
            m_snapshot[name] = P::getRegisteredGlobal(name);
        }
    }
    void TearDown() override
    {
        for (const auto& [name, value] : m_snapshot) {
            P::applyGlobalOverride(name, value);
        }
        // The §6 rule-disable state is a whole-process global too — never leak a disable.
        P::resetPostScoringRules();
    }
    std::map<std::string, double> m_snapshot;
};

// ── Registry ────────────────────────────────────────────────────────────────────

TEST_F(ParamOverride, RegistryContainsProductionSurfaceGlobals)
{
    // G1 (chordanalyzer.cpp file constants + relocated locals/literals)
    EXPECT_TRUE(P::isRegisteredGlobal("kContradictionPenalty"));
    EXPECT_TRUE(P::isRegisteredGlobal("kForeignPenalty"));
    EXPECT_TRUE(P::isRegisteredGlobal("kNonBassPenalty"));
    EXPECT_TRUE(P::isRegisteredGlobal("kWComplete"));
    EXPECT_TRUE(P::isRegisteredGlobal("kWCompletePresenceThreshold"));
    EXPECT_TRUE(P::isRegisteredGlobal("kComplexityEvidenceFloor"));
    EXPECT_TRUE(P::isRegisteredGlobal("kAugThinEvidenceFactor"));
    // G6 (harmonicfunctionlayer.h progression constants)
    EXPECT_TRUE(P::isRegisteredGlobal("kWSeq"));
    EXPECT_TRUE(P::isRegisteredGlobal("kWDim"));
    EXPECT_TRUE(P::isRegisteredGlobal("kWStepIn"));
    EXPECT_TRUE(P::isRegisteredGlobal("kWStepOut"));
    EXPECT_TRUE(P::isRegisteredGlobal("kStepBudget"));
    // G7 (postscoringgates.cpp gate margins)
    EXPECT_TRUE(P::isRegisteredGlobal("kGateIMargin"));
    EXPECT_TRUE(P::isRegisteredGlobal("kGateKMargin"));
    EXPECT_TRUE(P::isRegisteredGlobal("kGateLMargin"));
    EXPECT_TRUE(P::isRegisteredGlobal("kHalfDimFirstInversionBonus"));
    // G10 (sectionanalyzer.h section-layer abstention bar)
    EXPECT_TRUE(P::isRegisteredGlobal("kAnnotateKeyConfidenceThreshold"));

    EXPECT_FALSE(P::isRegisteredGlobal("kThisNameDoesNotExist"));
    // 24 G1 file constants + kWComplete/kWCompletePresenceThreshold/kComplexityEvidenceFloor/
    // kAugThinEvidenceFactor (4) + 5 G6 + 4 G7 + 1 G10 = 38 registered globals.
    EXPECT_EQ(P::registeredGlobalCount(), 38u);
}

TEST_F(ParamOverride, CurrentValuesMatchDocumentedLiterals)
{
    EXPECT_DOUBLE_EQ(P::getRegisteredGlobal("kContradictionPenalty"), 0.75);
    EXPECT_DOUBLE_EQ(P::getRegisteredGlobal("kNonBassPenalty"), 0.35);
    EXPECT_DOUBLE_EQ(P::getRegisteredGlobal("kWSeq"), 0.20);
    EXPECT_DOUBLE_EQ(P::getRegisteredGlobal("kWDim"), 0.15);
    EXPECT_DOUBLE_EQ(P::getRegisteredGlobal("kStepBudget"), 0.10 + 0.10 + 0.01);
    EXPECT_DOUBLE_EQ(P::getRegisteredGlobal("kGateIMargin"), 0.45);
    EXPECT_DOUBLE_EQ(P::getRegisteredGlobal("kHalfDimFirstInversionBonus"), 0.55);
}

TEST_F(ParamOverride, IsKnownNameSpansGlobalsAndPrefs)
{
    EXPECT_TRUE(P::isKnownName("kContradictionPenalty"));     // global
    EXPECT_TRUE(P::isKnownName("bassNoteRootBonus"));         // prefs field
    EXPECT_TRUE(P::isKnownName("minDistinctPcsForCandidate")); // int prefs field
    EXPECT_TRUE(P::isKnownName("preferMinorOverMajorAdd6"));  // bool prefs field
    EXPECT_FALSE(P::isKnownName("totallyBogusName"));
}

// ── Loader: happy paths ───────────────────────────────────────────────────────────

TEST_F(ParamOverride, IdentityFileLeavesGlobalsUnchanged)
{
    // Build a file that sets every global to its CURRENT value + one prefs field to its
    // current struct default: applying it must change nothing (byte-identity of the
    // loader itself). The count must equal globals + 1.
    std::string content = "# identity override\n";
    for (const auto& name : P::registeredGlobalNames()) {
        content += name + " " + std::to_string(P::getRegisteredGlobal(name)) + "\n";
    }
    content += "bassNoteRootBonus 0.7\n";
    const std::string path = writeTempOverride("identity", content);

    ChordAnalyzerPreferences prefs;
    const double before = P::getRegisteredGlobal("kContradictionPenalty");
    const auto st = P::loadAndApply(path, prefs);
    EXPECT_EQ(st.globals, static_cast<int>(P::registeredGlobalCount()));
    EXPECT_EQ(st.prefsFields, 1);
    EXPECT_DOUBLE_EQ(P::getRegisteredGlobal("kContradictionPenalty"), before);
    std::filesystem::remove(path);
}

TEST_F(ParamOverride, OverrideChangesGlobalConstant)
{
    const std::string path = writeTempOverride("global", "kContradictionPenalty 0.9\n");
    ChordAnalyzerPreferences prefs;
    const auto st = P::loadAndApply(path, prefs);
    EXPECT_EQ(st.applied, 1);
    EXPECT_EQ(st.globals, 1);
    EXPECT_DOUBLE_EQ(P::getRegisteredGlobal("kContradictionPenalty"), 0.9);
    std::filesystem::remove(path);
    // TearDown restores 0.75.
}

TEST_F(ParamOverride, OverrideSetsPrefsFields)
{
    const std::string path = writeTempOverride("prefs",
        "bassNoteRootBonus 0.55\n"
        "extensionThreshold 0.12\n"
        "minDistinctPcsForCandidate 1\n"
        "preferMinorOverMajorAdd6 true\n");
    ChordAnalyzerPreferences prefs;   // struct defaults
    const auto st = P::loadAndApply(path, prefs);
    EXPECT_EQ(st.prefsFields, 4);
    EXPECT_EQ(st.globals, 0);
    EXPECT_DOUBLE_EQ(prefs.bassNoteRootBonus, 0.55);
    EXPECT_DOUBLE_EQ(prefs.extensionThreshold, 0.12);
    EXPECT_EQ(prefs.minDistinctPcsForCandidate, 1);           // int coercion
    EXPECT_TRUE(prefs.preferMinorOverMajorAdd6);               // bool coercion (true)
    std::filesystem::remove(path);
}

TEST_F(ParamOverride, CommentsAndBlankLinesIgnored)
{
    const std::string path = writeTempOverride("comments",
        "# a comment line\n"
        "\n"
        "   \n"
        "kForeignPenalty 0.5   # trailing comment\n"
        "  # indented comment\n");
    ChordAnalyzerPreferences prefs;
    const auto st = P::loadAndApply(path, prefs);
    EXPECT_EQ(st.applied, 1);
    EXPECT_DOUBLE_EQ(P::getRegisteredGlobal("kForeignPenalty"), 0.5);
    std::filesystem::remove(path);
}

TEST_F(ParamOverride, StepBudgetRecomputedFromStepBonuses)
{
    // Moving kWStepIn without pinning kStepBudget must keep the derivation faithful:
    // kStepBudget = kWStepIn + kWStepOut + 0.01.
    const std::string path = writeTempOverride("stepbudget", "kWStepIn 0.20\n");
    ChordAnalyzerPreferences prefs;
    const double stepOut = P::getRegisteredGlobal("kWStepOut");
    P::loadAndApply(path, prefs);
    EXPECT_DOUBLE_EQ(P::getRegisteredGlobal("kWStepIn"), 0.20);
    EXPECT_DOUBLE_EQ(P::getRegisteredGlobal("kStepBudget"), 0.20 + stepOut + 0.01);
    std::filesystem::remove(path);
}

TEST_F(ParamOverride, ExplicitStepBudgetNotRecomputed)
{
    // If kStepBudget is pinned explicitly alongside kWStepIn, the explicit value wins.
    const std::string path = writeTempOverride("stepbudget_explicit",
        "kWStepIn 0.20\nkStepBudget 0.99\n");
    ChordAnalyzerPreferences prefs;
    P::loadAndApply(path, prefs);
    EXPECT_DOUBLE_EQ(P::getRegisteredGlobal("kStepBudget"), 0.99);
    std::filesystem::remove(path);
}

// ── Loader: strict rejections ─────────────────────────────────────────────────────

TEST_F(ParamOverride, UnknownNameThrows)
{
    const std::string path = writeTempOverride("unknown", "kNoSuchParam 1.0\n");
    ChordAnalyzerPreferences prefs;
    EXPECT_THROW(P::loadAndApply(path, prefs), std::runtime_error);
    std::filesystem::remove(path);
}

TEST_F(ParamOverride, MalformedValueThrows)
{
    const std::string path = writeTempOverride("malformed", "kForeignPenalty notanumber\n");
    ChordAnalyzerPreferences prefs;
    EXPECT_THROW(P::loadAndApply(path, prefs), std::runtime_error);
    std::filesystem::remove(path);
}

TEST_F(ParamOverride, ExtraTokenThrows)
{
    const std::string path = writeTempOverride("extra", "kForeignPenalty 0.5 0.6\n");
    ChordAnalyzerPreferences prefs;
    EXPECT_THROW(P::loadAndApply(path, prefs), std::runtime_error);
    std::filesystem::remove(path);
}

TEST_F(ParamOverride, MissingFileThrows)
{
    ChordAnalyzerPreferences prefs;
    EXPECT_THROW(P::loadAndApply("/no/such/paramoverride/file.txt", prefs), std::runtime_error);
}

// ── §6-block dissolution audit: the `disable_rule` grammar ──────────────────────────

TEST_F(ParamOverride, PostScoringRuleNamesSpanTheFullSixBlock)
{
    // The 12 §6 members after retiring Gates A + F (Stage-5 RETIRE-5, 2026-07-05, design D-7):
    // bias correction · FM2 · E · G-E · G-B · G-C · G-D · H · I · K · L · J.
    const auto names = P::postScoringRuleNames();
    EXPECT_EQ(names.size(), 12u);
    for (const char* n : { "BiasCorrection", "FM2", "GateE",
                           "GateGE", "GateGB", "GateGC", "GateGD",
                           "GateH", "GateI", "GateK", "GateL", "GateJ" }) {
        EXPECT_TRUE(P::isKnownRuleName(n)) << n;
    }
    EXPECT_FALSE(P::isKnownRuleName("GateA"));       // retired Stage 5 (2026-07-05) — not a rule
    EXPECT_FALSE(P::isKnownRuleName("GateF"));       // retired Stage 5 (2026-07-05) — not a rule
    EXPECT_FALSE(P::isKnownRuleName("GateB"));       // removed at Stage 3.4b — not a rule
    EXPECT_FALSE(P::isKnownRuleName("NotARule"));
}

TEST_F(ParamOverride, DisableRuleLineSetsTheFlagAndCounts)
{
    const std::string path = writeTempOverride("disable_one", "disable_rule GateJ\n");
    ChordAnalyzerPreferences prefs;
    const auto st = P::loadAndApply(path, prefs);
    EXPECT_EQ(st.rulesDisabled, 1);
    EXPECT_EQ(st.applied, 1);
    EXPECT_EQ(st.globals, 0);
    EXPECT_EQ(st.prefsFields, 0);
    EXPECT_TRUE(P::isRuleDisabled(P::PostScoringRule::GateJ));
    // Every other rule stays enabled.
    EXPECT_FALSE(P::isRuleDisabled(P::PostScoringRule::GateI));
    EXPECT_FALSE(P::isRuleDisabled(P::PostScoringRule::BiasCorrection));
    std::filesystem::remove(path);
    // TearDown re-enables all rules.
}

TEST_F(ParamOverride, DisableRuleMixesWithValueOverrides)
{
    const std::string path = writeTempOverride("disable_mixed",
        "kForeignPenalty 0.5\n"
        "disable_rule GateI\n"
        "disable_rule GateL\n"
        "bassNoteRootBonus 0.55\n");
    ChordAnalyzerPreferences prefs;
    const auto st = P::loadAndApply(path, prefs);
    EXPECT_EQ(st.globals, 1);
    EXPECT_EQ(st.prefsFields, 1);
    EXPECT_EQ(st.rulesDisabled, 2);
    EXPECT_EQ(st.applied, 4);
    EXPECT_TRUE(P::isRuleDisabled(P::PostScoringRule::GateI));
    EXPECT_TRUE(P::isRuleDisabled(P::PostScoringRule::GateL));
    EXPECT_FALSE(P::isRuleDisabled(P::PostScoringRule::GateK));
    std::filesystem::remove(path);
}

TEST_F(ParamOverride, UnknownRuleNameThrows)
{
    const std::string path = writeTempOverride("disable_unknown", "disable_rule GateZ\n");
    ChordAnalyzerPreferences prefs;
    EXPECT_THROW(P::loadAndApply(path, prefs), std::runtime_error);
    std::filesystem::remove(path);
}

TEST_F(ParamOverride, DisableRuleWithoutNameThrows)
{
    // 'disable_rule' alone is a malformed (name-only) line — the loader wants two tokens.
    const std::string path = writeTempOverride("disable_bare", "disable_rule\n");
    ChordAnalyzerPreferences prefs;
    EXPECT_THROW(P::loadAndApply(path, prefs), std::runtime_error);
    std::filesystem::remove(path);
}

TEST_F(ParamOverride, IdentityFileWithNoDisableLeavesAllRulesEnabled)
{
    // The Phase-1 discipline for the audit hook: an override file that disables nothing
    // leaves every rule enabled (byte-identical behavior).
    const std::string path = writeTempOverride("no_disable", "kForeignPenalty 0.5\n");
    ChordAnalyzerPreferences prefs;
    const auto st = P::loadAndApply(path, prefs);
    EXPECT_EQ(st.rulesDisabled, 0);
    for (const auto& name : P::postScoringRuleNames()) {
        P::PostScoringRule r{};
        ASSERT_TRUE(P::postScoringRuleId(name, r));
        EXPECT_FALSE(P::isRuleDisabled(r)) << name;
    }
    std::filesystem::remove(path);
}

} // namespace
