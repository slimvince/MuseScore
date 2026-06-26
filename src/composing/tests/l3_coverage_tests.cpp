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

// ── Test-backfill (criteria 1-4): L3 option / branch threads ─────────────────
//
// These pin Layer-3 control-flow arms that were line-EXECUTED but branch- and
// assertion-UNTESTED (cc_tree_repair_and_coverage_report.md C1 §7): the resolver's
// excludeStaves / ignoreDeclaredMode / dynamic-lookahead-growth arms, the emission
// analyzer's declared-mode penalty arm + unison robustness, and the sequence
// decoder's redecodeRange argument guard + emission-confidence (C1) population.
//
// Each assertion is an INDEPENDENT ORACLE derived from the documented contract:
//   • excluding every staff removes all pitches from emission -> insufficient-PC
//     fallback (confidence/score 0);
//   • ignoreDeclaredMode drops the declared mode (dump ordinal -> -1);
//   • an unreachable confidence threshold forces the lookahead window to its hard
//     cap; an always-met threshold leaves it at the initial window;
//   • analyzeKeyMode subtracts prefs.declaredModePenalty from out-of-class
//     candidates only (modeIsCompatibleWithDeclared);
//   • redecodeRange returns empty for any out-of-bounds / inverted range;
//   • the decoded chosen.normalizedConfidence is the emission-scale C1 value the
//     downstream 0.8 key-confidence gates consume (a sigmoid in [0,1]).

#include <gtest/gtest.h>

#include <algorithm>
#include <optional>
#include <set>
#include <vector>

#include "engraving/dom/masterscore.h"
#include "engraving/types/fraction.h"
#include "engraving/tests/utils/scorerw.h"

#include "composing/analysis/key/keymodeanalyzer.h"
#include "composing/analysis/key/keyresolver.h"
#include "composing/analysis/key/keymodesequence.h"
#include "composing/analysis/notemodel/note_model.h"
#include "composing/analysis/slicing/slicer.h"

#include "test_helpers.h"

using namespace mu::composing::analysis;
namespace kr = mu::composing::analysis::keyresolver;
namespace kms = mu::composing::analysis::keymodeseq;

using mu::engraving::Fraction;
using mu::engraving::MasterScore;
using mu::engraving::ScoreRW;
using mu::composing::analysis::notemodel::NoteModel;
using mu::composing::analysis::slicing::changePointSlices;
using KMSD = kms::KeyModeSequenceDecoder;

namespace {
const std::set<std::size_t> kNoExclude {};

const KeyCandidateScore* findCand(const std::vector<KeyCandidateScore>& dump,
                                  int tonicPc, KeySigMode mode)
{
    for (const KeyCandidateScore& c : dump) {
        if (c.tonicPc == tonicPc && c.modeIndex == keyModeIndex(mode)) {
            return &c;
        }
    }
    return nullptr;
}
} // namespace

// ═════════════════════════════════════════════════════════════════════════════
//  analyzeKeyMode — declared-mode penalty arm + unison robustness
// ═════════════════════════════════════════════════════════════════════════════

// The declared-mode hint subtracts prefs.declaredModePenalty from every candidate
// OUTSIDE the declared class (modeIsCompatibleWithDeclared), and nothing when no
// declared mode is supplied. Asserted directly on the 252-candidate dump.
TEST(Composing_L3Coverage, AnalyzeKeyMode_DeclaredModePenalty_OnlyOutOfClassCandidates)
{
    const auto pitches = flatPitches({ 60, 62, 64, 65, 67, 69, 71 });   // C major scale
    const double pen = kDefaultKeyModeAnalyzerPreferences.declaredModePenalty;
    ASSERT_GT(pen, 0.0);

    std::vector<KeyCandidateScore> none, major, minor;
    KeyModeAnalyzer::analyzeKeyMode(pitches, 0, kDefaultKeyModeAnalyzerPreferences,
                                    std::nullopt, &none);
    KeyModeAnalyzer::analyzeKeyMode(pitches, 0, kDefaultKeyModeAnalyzerPreferences,
                                    KeySigMode::Ionian, &major);
    KeyModeAnalyzer::analyzeKeyMode(pitches, 0, kDefaultKeyModeAnalyzerPreferences,
                                    KeySigMode::Aeolian, &minor);

    ASSERT_EQ(none.size(), 252u);   // 12 tonics × 21 modes
    // No declared mode -> no penalty anywhere.
    for (const KeyCandidateScore& c : none) {
        EXPECT_DOUBLE_EQ(c.declaredPenalty, 0.0);
    }

    // Declared MAJOR: a major-class candidate is in-class (0); a minor-class
    // candidate is out-of-class (penalised).
    const KeyCandidateScore* majIon = findCand(major, 0, KeySigMode::Ionian);
    const KeyCandidateScore* majAeol = findCand(major, 0, KeySigMode::Aeolian);
    ASSERT_TRUE(majIon && majAeol);
    EXPECT_DOUBLE_EQ(majIon->declaredPenalty, 0.0);
    EXPECT_DOUBLE_EQ(majAeol->declaredPenalty, pen);

    // Declared MINOR: the classes flip.
    const KeyCandidateScore* minIon = findCand(minor, 0, KeySigMode::Ionian);
    const KeyCandidateScore* minAeol = findCand(minor, 0, KeySigMode::Aeolian);
    ASSERT_TRUE(minIon && minAeol);
    EXPECT_DOUBLE_EQ(minAeol->declaredPenalty, 0.0);
    EXPECT_DOUBLE_EQ(minIon->declaredPenalty, pen);
}

// A unison (all-same-pitch) cannot determine a key but must not crash; like the
// single-pitch case the analyzer still returns at least one valid candidate.
TEST(Composing_L3Coverage, AnalyzeKeyMode_Unison_NoCrashReturnsValidCandidate)
{
    const auto results = KeyModeAnalyzer::analyzeKeyMode(flatPitches({ 60, 60, 60 }), 0);
    EXPECT_FALSE(results.empty());
    for (const KeyModeAnalysisResult& r : results) {
        EXPECT_GE(r.tonicPc, 0);
        EXPECT_LT(r.tonicPc, 12);
        EXPECT_GE(r.normalizedConfidence, 0.0);
        EXPECT_LE(r.normalizedConfidence, 1.0);
    }
}

// ═════════════════════════════════════════════════════════════════════════════
//  keyresolver — excludeStaves / ignoreDeclaredMode / dynamic-lookahead arms
// ═════════════════════════════════════════════════════════════════════════════

// excludeStaves removes those staves' notes from the emission context. Excluding
// EVERY staff therefore empties the window -> the insufficient-PC fallback (size 1,
// confidence 0). The un-excluded resolve of the same score is a real reading,
// proving the exclusion (not the fixture) caused the fallback.
TEST(Composing_L3Coverage, Keyresolver_ExcludeStaves_NotesDoNotReachEmission)
{
    MasterScore* score = ScoreRW::readScore(u"data/s1c_c_major.mscx");   // 2 staves
    ASSERT_TRUE(score);

    const auto full = kr::resolveKeyAndModeRanked(
        score, Fraction(0, 1), 0, kNoExclude, kDefaultKeyModeAnalyzerPreferences, nullptr);
    EXPECT_EQ(full.size(), 3u);
    ASSERT_FALSE(full.empty());
    EXPECT_EQ(full.front().tonicPc, 0);                  // C major, a real reading

    const std::set<std::size_t> excludeAll { 0, 1 };
    const auto excluded = kr::resolveKeyAndModeRanked(
        score, Fraction(0, 1), 0, excludeAll, kDefaultKeyModeAnalyzerPreferences, nullptr);
    ASSERT_EQ(excluded.size(), 1u);                      // fallback shape
    EXPECT_DOUBLE_EQ(excluded.front().normalizedConfidence, 0.0);
    EXPECT_DOUBLE_EQ(excluded.front().score, 0.0);

    delete score;
}

// ignoreDeclaredMode drops the declared mode entirely (the mode-absent floor).
TEST(Composing_L3Coverage, Keyresolver_IgnoreDeclaredMode_DropsTheDeclaredMode)
{
    MasterScore* score = ScoreRW::readScore(u"data/s1c_c_minor.mscx");   // declares minor
    ASSERT_TRUE(score);

    KeyModeAnalyzerPreferences prefsKeep;                       // ignoreDeclaredMode = false
    KeyModeAnalyzerPreferences prefsDrop;
    prefsDrop.ignoreDeclaredMode = true;

    kr::KeyResolveDump keep, drop;
    kr::resolveKeyAndModeRanked(score, Fraction(0, 1), 0, kNoExclude, prefsKeep, nullptr, &keep);
    kr::resolveKeyAndModeRanked(score, Fraction(0, 1), 0, kNoExclude, prefsDrop, nullptr, &drop);

    // Default: the declared minor signature -> Aeolian ordinal.
    EXPECT_EQ(keep.declaredModeOrdinal, static_cast<int>(keyModeIndex(KeySigMode::Aeolian)));
    // ignoreDeclaredMode: dropped -> -1.
    EXPECT_EQ(drop.declaredModeOrdinal, -1);

    delete score;
}

// The dynamic-lookahead loop grows the window until the top result clears the
// confidence threshold OR the hard cap is hit. An unreachable threshold (>1.0)
// forces growth to the cap; an always-met threshold (0.0) leaves it at the initial
// window. Both arms (grow vs break-early) are exercised and distinguished.
TEST(Composing_L3Coverage, Keyresolver_DynamicLookahead_GrowsToCapOrBreaksEarly)
{
    MasterScore* score = ScoreRW::readScore(u"data/s1c_c_major.mscx");
    ASSERT_TRUE(score);

    KeyModeAnalyzerPreferences never;
    never.dynamicLookaheadConfidenceThreshold = 1.01;   // confidence in [0,1] never clears it
    KeyModeAnalyzerPreferences always;
    always.dynamicLookaheadConfidenceThreshold = 0.0;   // always cleared on the first window

    kr::KeyResolveDump dNever, dAlways;
    kr::resolveKeyAndModeRanked(score, Fraction(0, 1), 0, kNoExclude, never, nullptr, &dNever);
    kr::resolveKeyAndModeRanked(score, Fraction(0, 1), 0, kNoExclude, always, nullptr, &dAlways);

    EXPECT_EQ(dNever.lookaheadBeatsUsed, never.dynamicLookaheadMaxBeats)
        << "an unreachable threshold grows the window to the hard cap";
    EXPECT_LT(dAlways.lookaheadBeatsUsed, always.dynamicLookaheadMaxBeats)
        << "an always-met threshold breaks at the initial window";
    EXPECT_LT(dAlways.lookaheadBeatsUsed, dNever.lookaheadBeatsUsed);

    delete score;
}

// ═════════════════════════════════════════════════════════════════════════════
//  keymodesequence — redecodeRange argument guard + emission-confidence (C1)
// ═════════════════════════════════════════════════════════════════════════════

// redecodeRange returns empty for any out-of-bounds / inverted [first,last].
TEST(Composing_L3Coverage, RedecodeRange_InvalidRange_ReturnsEmpty)
{
    MasterScore* score = ScoreRW::readScore(u"data/s1c_seg_changes.mscx");
    ASSERT_TRUE(score);
    const NoteModel model = NoteModel::build(score);
    const auto slices = changePointSlices(model);
    ASSERT_GE(slices.size(), 3u);
    const int T = static_cast<int>(slices.size());
    const KeyModeAnalysisResult pin;   // default endpoint pin

    EXPECT_TRUE(KMSD::redecodeRange(slices, model, 0, std::nullopt, -1, T - 1, pin, pin).empty())
        << "first < 0";
    EXPECT_TRUE(KMSD::redecodeRange(slices, model, 0, std::nullopt, 0, T, pin, pin).empty())
        << "last >= T";
    EXPECT_TRUE(KMSD::redecodeRange(slices, model, 0, std::nullopt, 2, 1, pin, pin).empty())
        << "first > last";
    // A valid range is non-empty (the guard is not over-broad).
    EXPECT_FALSE(KMSD::redecodeRange(slices, model, 0, std::nullopt, 0, T - 1, pin, pin).empty());

    delete score;
}

// populateEmissionConfidence writes the EMISSION-scale C1 confidence into each
// slice's chosen.normalizedConfidence (the value the downstream 0.8 key-confidence
// gates consume) — a sigmoid in [0,1], distinct from the sequence-margin
// SliceKeyMode.confidence (which is unbounded above).
TEST(Composing_L3Coverage, Decode_EmissionConfidence_PopulatedOnC1Scale)
{
    MasterScore* score = ScoreRW::readScore(u"data/s1c_c_major.mscx");
    ASSERT_TRUE(score);
    const NoteModel model = NoteModel::build(score);
    const auto slices = changePointSlices(model);
    ASSERT_FALSE(slices.empty());

    const auto d = KMSD::decode(slices, model, /*keySigFifths=*/0);
    ASSERT_EQ(d.size(), slices.size());

    double maxEmission = 0.0;
    for (const kms::SliceKeyMode& s : d) {
        EXPECT_GE(s.chosen.normalizedConfidence, 0.0);
        EXPECT_LE(s.chosen.normalizedConfidence, 1.0)
            << "chosen.normalizedConfidence is the C1 emission sigmoid, bounded to [0,1]";
        maxEmission = std::max(maxEmission, s.chosen.normalizedConfidence);
    }
    EXPECT_GT(maxEmission, 0.0)
        << "populateEmissionConfidence actually wrote a confidence (not left at 0)";

    delete score;
}
