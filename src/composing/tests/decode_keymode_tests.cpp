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

// LAYER 3 — KEY/MODE SEQUENCE DECODER tests (signed design §10; decoder audit §5).
//
// Two tiers:
//   * SCORER-INDEPENDENT behaviour + change-cost + branch tests — inject the
//     lattice (states + per-slice emission) by hand and assert the decoded
//     sequence / confidence. These pin the Viterbi, the change cost, the
//     sequence-margin confidence, the endpoint pins (redecode core), and every
//     decoder branch, with no dependency on the emission scorer.
//   * NOTE-MODEL (end-to-end) fixture tests — run the REAL decode() over Layer-1
//     note models built from .mscx fixtures: single key, a chord progression that
//     must NOT spuriously modulate, the relative-major/minor pair chosen
//     consistently, the redecodeRange == full-decode property, and determinism.

#include <gtest/gtest.h>

#include <optional>
#include <set>
#include <utility>
#include <vector>

#include "engraving/dom/masterscore.h"
#include "engraving/tests/utils/scorerw.h"

#include "composing/analysis/key/keymodesequence.h"
#include "composing/analysis/notemodel/note_model.h"
#include "composing/analysis/slicing/slicer.h"

using mu::engraving::MasterScore;
using mu::engraving::ScoreRW;
using mu::composing::analysis::KeySigMode;
using mu::composing::analysis::KeyModeAnalysisResult;
using mu::composing::analysis::notemodel::NoteModel;
using mu::composing::analysis::slicing::Slice;
using mu::composing::analysis::slicing::changePointSlices;

namespace kms = mu::composing::analysis::keymodeseq;
using KMSD = kms::KeyModeSequenceDecoder;
using State = KMSD::State;
using kms::SliceKeyMode;
using kms::KeyModeSequencePreferences;

namespace {

// The four reference states used across the synthetic tests. ionianPc is the
// parent Ionian tonic pitch class (drives the change cost); keySignatureFifths is
// only the label.
const State kCIon  { 0, KeySigMode::Ionian,  0, 0 };   // C major
const State kGIon  { 7, KeySigMode::Ionian,  1, 7 };   // G major (dominant — near, cof 1)
const State kAAeol { 9, KeySigMode::Aeolian, 0, 0 };   // A minor (relative pair of C — same sig)
const State kFsIon { 6, KeySigMode::Ionian,  6, 6 };   // F# major (remote, cof 6)

// Decode a synthetic lattice and return only the chosen (tonicPc, mode) per slice.
std::vector<std::pair<int, KeySigMode>> chosenSeq(const std::vector<SliceKeyMode>& d)
{
    std::vector<std::pair<int, KeySigMode>> out;
    for (const SliceKeyMode& s : d) {
        out.push_back({ s.chosen.tonicPc, s.chosen.mode });
    }
    return out;
}

int distinctKeys(const std::vector<SliceKeyMode>& d)
{
    std::set<std::pair<int, int>> keys;
    for (const SliceKeyMode& s : d) {
        keys.insert({ s.chosen.tonicPc, static_cast<int>(s.chosen.mode) });
    }
    return static_cast<int>(keys.size());
}

} // namespace

// ════════════════════════════════════════════════════════════════════════════
// Change cost (design §5.2 / audit §2.3) — emission-score units.
// ════════════════════════════════════════════════════════════════════════════

TEST(Composing_DecodeKeyMode, ChangeCost_StayIsFree)
{
    const KeyModeSequencePreferences p;
    EXPECT_DOUBLE_EQ(KMSD::changeCost(kCIon, kCIon, p), 0.0);
    EXPECT_DOUBLE_EQ(KMSD::changeCost(kAAeol, kAAeol, p), 0.0);
}

TEST(Composing_DecodeKeyMode, ChangeCost_NearSwitchCheaperThanRemote)
{
    const KeyModeSequencePreferences p;   // base 2.0, perFifth 0.60, relative 2.0
    // C → G (one fifth): base + 0.60*1 = 2.60.
    EXPECT_DOUBLE_EQ(KMSD::changeCost(kCIon, kGIon, p), 2.60);
    // C → F# (six fifths): base + 0.60*6 = 5.60.
    EXPECT_DOUBLE_EQ(KMSD::changeCost(kCIon, kFsIon, p), 5.60);
    EXPECT_LT(KMSD::changeCost(kCIon, kGIon, p), KMSD::changeCost(kCIon, kFsIon, p));
}

TEST(Composing_DecodeKeyMode, ChangeCost_RelativePairCarriesTheExtraPenalty)
{
    const KeyModeSequencePreferences p;
    // C major ↔ A minor: same key signature (cof 0) + the relative-pair extra.
    EXPECT_DOUBLE_EQ(KMSD::changeCost(kCIon, kAAeol, p), 4.00);   // base 2.0 + 0 + 2.0
    EXPECT_GT(KMSD::changeCost(kCIon, kAAeol, p), KMSD::changeCost(kCIon, kGIon, p));
}

// ════════════════════════════════════════════════════════════════════════════
// Behaviour (synthetic emission) — the design §10 / §6 scenarios.
// ════════════════════════════════════════════════════════════════════════════

// Scenario 1 — a single-key passage stays one key with no spurious switches.
TEST(Composing_DecodeKeyMode, Behaviour_SingleKey_NoSpuriousSwitch)
{
    const std::vector<State> states = { kCIon, kGIon };
    std::vector<std::vector<double>> em(6, { 5.0, 1.0 });   // C dominates every slice
    const auto d = KMSD::decodeLattice(states, em);

    ASSERT_EQ(d.size(), 6u);
    for (const SliceKeyMode& s : d) {
        EXPECT_EQ(s.chosen.tonicPc, 0);
        EXPECT_EQ(s.chosen.mode, KeySigMode::Ionian);
        EXPECT_FALSE(s.uncertain) << "a clear single key is confident";
    }
    EXPECT_EQ(distinctKeys(d), 1);
}

// Scenario 2 — a relative-major/minor near-tie is resolved CONSISTENTLY to one
// member across the whole stretch, and the slice is marked uncertain (low
// confidence) because the whole-sequence alternative is almost as good.
TEST(Composing_DecodeKeyMode, Behaviour_RelativePair_ConsistentButUncertain)
{
    const std::vector<State> states = { kCIon, kAAeol };
    // C major very slightly preferred over its relative A minor, every slice.
    std::vector<std::vector<double>> em(6, { 3.0, 2.9 });
    const auto d = KMSD::decodeLattice(states, em);

    ASSERT_EQ(d.size(), 6u);
    for (const SliceKeyMode& s : d) {
        EXPECT_EQ(s.chosen.tonicPc, 0) << "the tilt wins consistently (C, not A)";
        EXPECT_EQ(s.chosen.mode, KeySigMode::Ionian);
        EXPECT_TRUE(s.uncertain) << "the relative pair is a near-tie → low confidence";
    }
    EXPECT_EQ(distinctKeys(d), 1) << "no flip-flopping between the relative pair";
}

// Scenario 3 — a brief tonicization (one slice scores the dominant higher) does
// NOT repay the change cost over so few slices, so the key is UNCHANGED.
TEST(Composing_DecodeKeyMode, Behaviour_BriefTonicization_KeyUnchanged)
{
    const std::vector<State> states = { kCIon, kGIon };
    std::vector<std::vector<double>> em = {
        { 4.0, 1.0 }, { 4.0, 1.0 }, { 4.0, 6.0 },   // slice 2: G locally beats C…
        { 4.0, 1.0 }, { 4.0, 1.0 }, { 4.0, 1.0 },
    };
    const auto d = KMSD::decodeLattice(states, em);

    ASSERT_EQ(d.size(), 6u);
    for (const SliceKeyMode& s : d) {
        EXPECT_EQ(s.chosen.tonicPc, 0) << "the round-trip switch cost is not repaid";
        EXPECT_EQ(s.chosen.mode, KeySigMode::Ionian);
    }
    EXPECT_EQ(distinctKeys(d), 1);
}

// Scenario 4 — a sustained modulation (the new key persists) repays the change
// cost, so the key CHANGES exactly once (no cadence detection involved).
TEST(Composing_DecodeKeyMode, Behaviour_SustainedModulation_KeyChanges)
{
    const std::vector<State> states = { kCIon, kGIon };
    std::vector<std::vector<double>> em = {
        { 4.0, 1.0 }, { 4.0, 1.0 }, { 4.0, 1.0 },   // C half
        { 1.0, 4.0 }, { 1.0, 4.0 }, { 1.0, 4.0 },   // G half
    };
    const auto d = KMSD::decodeLattice(states, em);

    ASSERT_EQ(d.size(), 6u);
    const auto seq = chosenSeq(d);
    const std::vector<std::pair<int, KeySigMode>> expected = {
        { 0, KeySigMode::Ionian }, { 0, KeySigMode::Ionian }, { 0, KeySigMode::Ionian },
        { 7, KeySigMode::Ionian }, { 7, KeySigMode::Ionian }, { 7, KeySigMode::Ionian },
    };
    EXPECT_EQ(seq, expected) << "C for the first half, G for the second — one switch";
    EXPECT_EQ(distinctKeys(d), 2);
}

// Scenario 5 — when two modulation targets have equal local evidence, the NEAR
// key (smaller circle-of-fifths distance) is preferred (cheaper switch).
TEST(Composing_DecodeKeyMode, Behaviour_NearPreferredToRemote_OnEqualEvidence)
{
    const std::vector<State> states = { kCIon, kGIon, kFsIon };   // 0:C 1:G(near) 2:F#(remote)
    std::vector<std::vector<double>> em = {
        { 5.0, 1.0, 1.0 }, { 5.0, 1.0, 1.0 },   // clearly C
        { 1.0, 4.0, 4.0 }, { 1.0, 4.0, 4.0 },   // G and F# tie locally
    };
    const auto d = KMSD::decodeLattice(states, em);

    ASSERT_EQ(d.size(), 4u);
    EXPECT_EQ(d[2].chosen.tonicPc, 7) << "switch to the NEAR key G, not remote F#";
    EXPECT_EQ(d[3].chosen.tonicPc, 7);
    EXPECT_NE(d[2].chosen.tonicPc, 6);
}

// ════════════════════════════════════════════════════════════════════════════
// Confidence, alternatives, pins, determinism, edges (branch coverage).
// ════════════════════════════════════════════════════════════════════════════

// Single-state lattice → the "no different key/mode to compare" confidence branch.
TEST(Composing_DecodeKeyMode, SingleState_ConfidenceSentinel_NotUncertain)
{
    const std::vector<State> states = { kCIon };
    std::vector<std::vector<double>> em(3, { 2.0 });
    const auto d = KMSD::decodeLattice(states, em);

    ASSERT_EQ(d.size(), 3u);
    for (const SliceKeyMode& s : d) {
        EXPECT_EQ(s.chosen.tonicPc, 0);
        EXPECT_TRUE(s.alternatives.empty());
        EXPECT_FALSE(s.uncertain);
        EXPECT_GT(s.confidence, 1.0);
    }
}

// Alternatives are ranked by whole-sequence total and capped at maxAlternatives.
TEST(Composing_DecodeKeyMode, Alternatives_RankedAndCapped)
{
    const std::vector<State> states = { kCIon, kGIon, kFsIon };
    std::vector<std::vector<double>> em(3, { 5.0, 3.0, 1.0 });   // C > G > F#
    KeyModeSequencePreferences p;
    p.maxAlternatives = 1;
    const auto d = KMSD::decodeLattice(states, em, p);

    ASSERT_EQ(d.size(), 3u);
    EXPECT_EQ(d[1].chosen.tonicPc, 0);
    ASSERT_EQ(d[1].alternatives.size(), 1u) << "capped to maxAlternatives";
    EXPECT_EQ(d[1].alternatives[0].tonicPc, 7) << "the best alternative (G) is ranked first";
}

// Endpoint pins (the redecodeRange core): force the first and last columns.
TEST(Composing_DecodeKeyMode, Pins_ForceEndpointStates)
{
    const std::vector<State> states = { kCIon, kGIon };
    // Emission alone would pick C everywhere; pin the ends to G.
    std::vector<std::vector<double>> em(4, { 5.0, 1.0 });
    const auto d = KMSD::decodeLattice(states, em, kms::kDefaultKeyModeSequencePreferences,
                                       /*pinFirstState=*/1, /*pinLastState=*/1);

    ASSERT_EQ(d.size(), 4u);
    EXPECT_EQ(d.front().chosen.tonicPc, 7) << "first column pinned to G";
    EXPECT_EQ(d.back().chosen.tonicPc, 7) << "last column pinned to G";
}

TEST(Composing_DecodeKeyMode, Determinism_Synthetic)
{
    const std::vector<State> states = { kCIon, kGIon, kAAeol };
    std::vector<std::vector<double>> em = {
        { 3.0, 2.0, 2.9 }, { 4.0, 1.0, 2.0 }, { 1.0, 4.0, 1.0 }, { 1.0, 4.0, 1.0 },
    };
    const auto a = KMSD::decodeLattice(states, em);
    const auto b = KMSD::decodeLattice(states, em);
    ASSERT_EQ(a.size(), b.size());
    for (size_t i = 0; i < a.size(); ++i) {
        EXPECT_EQ(a[i].chosen.tonicPc, b[i].chosen.tonicPc);
        EXPECT_EQ(a[i].chosen.mode, b[i].chosen.mode);
        EXPECT_DOUBLE_EQ(a[i].confidence, b[i].confidence);
    }
}

TEST(Composing_DecodeKeyMode, EmptyLattice_NoSlices)
{
    EXPECT_TRUE(KMSD::decodeLattice({}, {}).empty());
    EXPECT_TRUE(KMSD::decodeLattice({ kCIon }, {}).empty());   // states but no columns
}

// ════════════════════════════════════════════════════════════════════════════
// NOTE-MODEL (end-to-end) — real decode() over Layer-1 models from .mscx fixtures.
// ════════════════════════════════════════════════════════════════════════════

// A single-key C-major passage → C major (Ionian) on every slice, confidently.
TEST(Composing_DecodeKeyMode, Fixture_CMajor_SingleKeyThroughout)
{
    MasterScore* score = ScoreRW::readScore(u"data/s1c_c_major.mscx");
    ASSERT_TRUE(score);
    const NoteModel model = NoteModel::build(score);
    const auto slices = changePointSlices(model);
    ASSERT_FALSE(slices.empty());

    const auto d = KMSD::decode(slices, model, /*keySigFifths=*/0);
    ASSERT_EQ(d.size(), slices.size());
    for (const SliceKeyMode& s : d) {
        EXPECT_EQ(s.chosen.tonicPc, 0) << "C tonic on every slice";
        EXPECT_TRUE(s.chosen.isMajor());
    }
    EXPECT_EQ(distinctKeys(d), 1) << "no spurious key change in a single-key passage";

    delete score;
}

// A I–V–vi–IV progression sits entirely in C major: the SEQUENCE decoder must
// keep one key across all the chord changes (it must NOT modulate to the dominant
// on the V chord) — the defect the per-region argmax is prone to.
TEST(Composing_DecodeKeyMode, Fixture_Progression_NoSpuriousModulation)
{
    MasterScore* score = ScoreRW::readScore(u"data/s1c_seg_changes.mscx");
    ASSERT_TRUE(score);
    const NoteModel model = NoteModel::build(score);
    const auto slices = changePointSlices(model);
    ASSERT_GE(slices.size(), 4u);

    const auto d = KMSD::decode(slices, model, /*keySigFifths=*/0);
    ASSERT_EQ(d.size(), slices.size());
    EXPECT_EQ(distinctKeys(d), 1) << "one key across the whole progression — no modulation";
    for (const SliceKeyMode& s : d) {
        EXPECT_EQ(s.chosen.keySignatureFifths, 0) << "stays a 0-signature key";
    }

    delete score;
}

// The relative-major/minor ambiguity is resolved to ONE member consistently
// (the decoder commits to a single 0-signature reading, never flip-flops).
TEST(Composing_DecodeKeyMode, Fixture_RelativePair_ConsistentChoice)
{
    MasterScore* score = ScoreRW::readScore(u"data/s1c_a_minor_amb.mscx");
    ASSERT_TRUE(score);
    const NoteModel model = NoteModel::build(score);
    const auto slices = changePointSlices(model);
    ASSERT_FALSE(slices.empty());

    const auto d = KMSD::decode(slices, model, /*keySigFifths=*/0);
    ASSERT_EQ(d.size(), slices.size());
    EXPECT_EQ(distinctKeys(d), 1) << "one consistent reading of the relative pair";
    for (const SliceKeyMode& s : d) {
        EXPECT_EQ(s.chosen.keySignatureFifths, 0);
    }

    delete score;
}

// A NOTE-BASED sustained modulation (C major → G major, NOT in the signature):
// the decoder starts in C, ends in G — the change cost is repaid by the sustained
// second half (scenario 4 end-to-end, on a real note model).
TEST(Composing_DecodeKeyMode, Fixture_SustainedModulation_CtoG)
{
    MasterScore* score = ScoreRW::readScore(u"data/s1c_modulation_cg.mscx");
    ASSERT_TRUE(score);
    const NoteModel model = NoteModel::build(score);
    const auto slices = changePointSlices(model);
    ASSERT_GE(slices.size(), 4u);

    // Notated signature is 0 (C); the modulation to G is inferred from the notes.
    const auto d = KMSD::decode(slices, model, /*keySigFifths=*/0);
    ASSERT_EQ(d.size(), slices.size());
    EXPECT_EQ(d.front().chosen.tonicPc, 0) << "opens in C major";
    EXPECT_TRUE(d.front().chosen.isMajor());
    EXPECT_EQ(d.back().chosen.tonicPc, 7) << "ends in G major (modulated)";
    EXPECT_TRUE(d.back().chosen.isMajor());
    EXPECT_GE(distinctKeys(d), 2) << "the sustained modulation changes the key";

    delete score;
}

// The declaredMode parameter threads through to the emission and orders the
// relative-major/minor reading. The PRODUCTION default penalty (1.0) is a weak
// tiebreaker whose effect is corpus-scale (the Baroque relative-pair recovery,
// see cc_layer3_decoder_build_report.md); to exercise the threading
// deterministically in a unit test, a strong penalty makes the pull visible: a
// declared MINOR then yields strictly more minor slices than a declared MAJOR,
// and each reading stays a single 0-signature key.
TEST(Composing_DecodeKeyMode, DeclaredMode_ThreadsToEmissionAndOrdersTheRelativePair)
{
    MasterScore* score = ScoreRW::readScore(u"data/s1c_a_minor_amb.mscx");
    ASSERT_TRUE(score);
    const NoteModel model = NoteModel::build(score);
    const auto slices = changePointSlices(model);
    ASSERT_FALSE(slices.empty());

    auto minorCount = [](const std::vector<SliceKeyMode>& d) {
        int n = 0;
        for (const SliceKeyMode& s : d) {
            if (!s.chosen.isMajor()) {
                ++n;
            }
        }
        return n;
    };

    mu::composing::analysis::KeyModeAnalyzerPreferences hint;   // Standard defaults
    hint.declaredModePenalty = 8.0;   // a strong hint, to make the threading visible
    const auto dMinor = KMSD::decode(slices, model, 0, KeySigMode::Aeolian, hint);
    const auto dMajor = KMSD::decode(slices, model, 0, KeySigMode::Ionian, hint);
    ASSERT_EQ(dMinor.size(), slices.size());
    ASSERT_EQ(dMajor.size(), slices.size());

    EXPECT_GT(minorCount(dMinor), minorCount(dMajor))
        << "a strong declared minor pulls the reading minor — the param reaches the emission";
    EXPECT_NE(chosenSeq(dMinor), chosenSeq(dMajor))
        << "the declared mode changes the decoded sequence (it is threaded, not ignored)";
}

// R2 — a sub-range re-decode with both endpoints pinned to a full decode's values
// reproduces the matching slice of that full decode (design §5 property).
TEST(Composing_DecodeKeyMode, Fixture_RedecodeRange_MatchesFullDecode)
{
    MasterScore* score = ScoreRW::readScore(u"data/s1c_seg_changes.mscx");
    ASSERT_TRUE(score);
    const NoteModel model = NoteModel::build(score);
    const auto slices = changePointSlices(model);
    ASSERT_GE(slices.size(), 3u);

    const auto full = KMSD::decode(slices, model, 0);
    const int first = 1;
    const int last = static_cast<int>(slices.size()) - 1;
    const auto sub = KMSD::redecodeRange(slices, model, 0, std::nullopt, first, last,
                                         full[first].chosen, full[last].chosen);

    ASSERT_EQ(sub.size(), static_cast<size_t>(last - first + 1));
    for (size_t i = 0; i < sub.size(); ++i) {
        EXPECT_EQ(sub[i].sliceIndex, first + static_cast<int>(i));
        EXPECT_EQ(sub[i].chosen.tonicPc, full[first + i].chosen.tonicPc) << "slice " << (first + i);
        EXPECT_EQ(sub[i].chosen.mode, full[first + i].chosen.mode) << "slice " << (first + i);
    }

    delete score;
}

TEST(Composing_DecodeKeyMode, Fixture_Determinism)
{
    MasterScore* score = ScoreRW::readScore(u"data/s1c_seg_changes.mscx");
    ASSERT_TRUE(score);
    const NoteModel model = NoteModel::build(score);
    const auto slices = changePointSlices(model);

    const auto a = KMSD::decode(slices, model, 0);
    const auto b = KMSD::decode(slices, model, 0);
    ASSERT_EQ(a.size(), b.size());
    for (size_t i = 0; i < a.size(); ++i) {
        EXPECT_EQ(a[i].chosen.tonicPc, b[i].chosen.tonicPc);
        EXPECT_EQ(a[i].chosen.mode, b[i].chosen.mode);
        EXPECT_DOUBLE_EQ(a[i].confidence, b[i].confidence);
        EXPECT_EQ(a[i].uncertain, b[i].uncertain);
    }

    delete score;
}
