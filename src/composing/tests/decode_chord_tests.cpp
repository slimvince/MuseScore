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

// LAYER 4 — per-slice CHORD-SYMBOL decoder tests (Increment A).
//
// Two tiers, mirroring the Layer-3 decoder tests:
//   * SCORER-INDEPENDENT (decideSlice) — inject a candidate list (the projected
//     cube) by hand and assert the chosen chord, the confidence margin (to the
//     best DIFFERENT chord), the ranked-and-capped alternatives, the prevailing
//     (∪) union, and the "uncertain" mark, with no dependency on the chord scorer.
//   * NOTE-MODEL (end-to-end) — run the REAL decode() over Layer-1 note models
//     built from .mscx fixtures: a clean triad names that chord; the complete
//     candidate list is surfaced and ranked; redecodeRange reproduces a full
//     decode; determinism.

#include <gtest/gtest.h>

#include <algorithm>
#include <optional>
#include <vector>

#include "engraving/dom/masterscore.h"
#include "engraving/tests/utils/scorerw.h"

#include "composing/analysis/chord/chordslicedecoder.h"
#include "composing/analysis/notemodel/note_model.h"
#include "composing/analysis/slicing/slicer.h"

using mu::engraving::MasterScore;
using mu::engraving::ScoreRW;
using mu::composing::analysis::ChordQuality;
using mu::composing::analysis::KeySigMode;
using mu::composing::analysis::notemodel::NoteModel;
using mu::composing::analysis::slicing::changePointSlices;

namespace cs = mu::composing::analysis::chordslice;
using CSD = cs::ChordSliceDecoder;
using cs::ChordSliceCandidate;
using cs::ChordSliceDecoderPreferences;
using cs::SliceChord;

namespace {

ChordSliceCandidate cand(int rootPc, ChordQuality quality, int bassPc, double score, int tie = 0)
{
    ChordSliceCandidate c;
    c.rootPc = rootPc;
    c.quality = quality;
    c.bassPc = bassPc;
    c.rootTpc = -1;
    c.bassTpc = -1;
    c.tiePriority = tie;
    c.score = score;
    return c;
}

} // namespace

// ════════════════════════════════════════════════════════════════════════════
// Scorer-independent core (decideSlice) — selection, confidence, alternatives.
// ════════════════════════════════════════════════════════════════════════════

TEST(Composing_DecodeChord, Decide_ChosenIsHighestScore)
{
    const std::vector<ChordSliceCandidate> cands = {
        cand(0, ChordQuality::Major, 0, 3.0),
        cand(9, ChordQuality::Minor, 9, 2.0),
        cand(5, ChordQuality::Major, 5, 1.0),
    };
    const SliceChord sc = CSD::decideSlice(0, cands, std::nullopt);
    EXPECT_TRUE(sc.hasChord);
    EXPECT_EQ(sc.chosen.rootPc, 0);
    EXPECT_EQ(sc.chosen.quality, ChordQuality::Major);
    EXPECT_TRUE(sc.chosen.bassIsRoot());
}

TEST(Composing_DecodeChord, Decide_ConfidenceIsMarginToBestDifferentChord)
{
    const std::vector<ChordSliceCandidate> cands = {
        cand(0, ChordQuality::Major, 0, 3.0),
        cand(9, ChordQuality::Minor, 9, 2.0),   // best DIFFERENT chord
        cand(5, ChordQuality::Major, 5, 1.0),
    };
    const SliceChord sc = CSD::decideSlice(0, cands, std::nullopt);
    EXPECT_DOUBLE_EQ(sc.confidence, 1.0);   // 3.0 − 2.0
    EXPECT_FALSE(sc.uncertain);             // margin 1.0 > 0.5 default
}

TEST(Composing_DecodeChord, Decide_LowMarginIsUncertain)
{
    const std::vector<ChordSliceCandidate> cands = {
        cand(0, ChordQuality::Major, 0, 3.0),
        cand(4, ChordQuality::Minor, 4, 2.9),   // a near-tie DIFFERENT chord
    };
    const SliceChord sc = CSD::decideSlice(0, cands, std::nullopt);
    EXPECT_NEAR(sc.confidence, 0.1, 1e-9);
    EXPECT_TRUE(sc.uncertain) << "a near-tie between two different chords is uncertain";
}

TEST(Composing_DecodeChord, Decide_InversionOfChosenIsNotADifferentChord)
{
    // Same chord (C major) at two basses + a genuinely different chord far below.
    const std::vector<ChordSliceCandidate> cands = {
        cand(0, ChordQuality::Major, 0, 3.0),   // C (root position) — chosen
        cand(0, ChordQuality::Major, 4, 2.9),   // C/E — SAME chord, not a competitor
        cand(2, ChordQuality::Minor, 2, 0.5),   // Dm — the only DIFFERENT chord
    };
    const SliceChord sc = CSD::decideSlice(0, cands, std::nullopt);
    EXPECT_EQ(sc.chosen.rootPc, 0);
    EXPECT_DOUBLE_EQ(sc.confidence, 2.5) << "margin is to Dm (0.5), not to the C/E inversion";
    EXPECT_FALSE(sc.uncertain);
}

TEST(Composing_DecodeChord, Decide_AlternativesRankedAndCapped)
{
    const std::vector<ChordSliceCandidate> cands = {
        cand(0, ChordQuality::Major, 0, 5.0),
        cand(7, ChordQuality::Major, 7, 3.0),
        cand(5, ChordQuality::Major, 5, 2.0),
        cand(2, ChordQuality::Minor, 2, 1.0),
    };
    ChordSliceDecoderPreferences p;
    p.topK = 2;
    const SliceChord sc = CSD::decideSlice(0, cands, std::nullopt, p);
    EXPECT_EQ(sc.chosen.rootPc, 0);
    ASSERT_EQ(sc.alternatives.size(), 2u) << "capped to topK";
    EXPECT_EQ(sc.alternatives[0].rootPc, 7) << "best alternative (G) ranked first";
    EXPECT_EQ(sc.alternatives[1].rootPc, 5);
}

TEST(Composing_DecodeChord, Decide_PrevailingChordKeptAliveBelowTopK)
{
    const std::vector<ChordSliceCandidate> cands = {
        cand(0, ChordQuality::Major, 0, 5.0),
        cand(7, ChordQuality::Major, 7, 4.0),
        cand(5, ChordQuality::Major, 5, 3.0),
        cand(4, ChordQuality::Minor, 4, 1.0),   // Em — below topK, but the prevailing
    };
    ChordSliceDecoderPreferences p;
    p.topK = 2;
    const std::optional<ChordSliceCandidate> prevailing = cand(4, ChordQuality::Minor, 4, 0.0);
    const SliceChord sc = CSD::decideSlice(0, cands, prevailing, p);

    ASSERT_GE(sc.alternatives.size(), 3u) << "topK alternatives PLUS the prevailing chord";
    const bool hasEm = std::any_of(sc.alternatives.begin(), sc.alternatives.end(),
                                   [](const ChordSliceCandidate& a) {
                                       return a.rootPc == 4 && a.quality == ChordQuality::Minor;
                                   });
    EXPECT_TRUE(hasEm) << "the prevailing chord is carried even though it fell below topK";
}

TEST(Composing_DecodeChord, Decide_PrevailingNotExpressibleIsNotForced)
{
    const std::vector<ChordSliceCandidate> cands = {
        cand(0, ChordQuality::Major, 0, 5.0),
        cand(7, ChordQuality::Major, 7, 4.0),
    };
    // Bb major is not among this slice's candidates → cannot be expressed here.
    const std::optional<ChordSliceCandidate> prevailing = cand(10, ChordQuality::Major, 10, 0.0);
    const SliceChord sc = CSD::decideSlice(0, cands, prevailing);
    const bool hasBb = std::any_of(sc.alternatives.begin(), sc.alternatives.end(),
                                   [](const ChordSliceCandidate& a) { return a.rootPc == 10; });
    EXPECT_FALSE(hasBb) << "an inexpressible prevailing chord is not forced into the alternatives";
}

TEST(Composing_DecodeChord, Decide_SingleChordNoCompetitorIsConfident)
{
    // Only one chord symbol present (C major at several basses): no DIFFERENT chord.
    const std::vector<ChordSliceCandidate> cands = {
        cand(0, ChordQuality::Major, 0, 3.0),
        cand(0, ChordQuality::Major, 4, 2.8),
        cand(0, ChordQuality::Major, 7, 2.5),
    };
    const SliceChord sc = CSD::decideSlice(0, cands, std::nullopt);
    EXPECT_EQ(sc.chosen.rootPc, 0);
    EXPECT_GT(sc.confidence, 1.0) << "no different chord → high-confidence sentinel";
    EXPECT_FALSE(sc.uncertain);
}

TEST(Composing_DecodeChord, Decide_EmptyCandidatesIsNoChord)
{
    const SliceChord sc = CSD::decideSlice(3, {}, std::nullopt);
    EXPECT_FALSE(sc.hasChord);
    EXPECT_TRUE(sc.uncertain);
    EXPECT_TRUE(sc.alternatives.empty());
    EXPECT_EQ(sc.sliceIndex, 3);
}

TEST(Composing_DecodeChord, Decide_MembershipSetsAreEmptyThisIncrement)
{
    const std::vector<ChordSliceCandidate> cands = { cand(0, ChordQuality::Major, 0, 3.0) };
    const SliceChord sc = CSD::decideSlice(0, cands, std::nullopt);
    EXPECT_TRUE(sc.chordTonePcs.empty()) << "membership is Increment B";
    EXPECT_TRUE(sc.nonChordTonePcs.empty()) << "no NCT called this increment";
}

// ════════════════════════════════════════════════════════════════════════════
// NOTE-MODEL (end-to-end) — real decode() over Layer-1 models from .mscx fixtures.
// ════════════════════════════════════════════════════════════════════════════

// A clean C-major triad slice then a clean G-major triad slice each name THAT
// chord, root-position. contextSlices=0 isolates each slice (the default ±1
// window would pool the two triads — the over-read Increment B's membership
// addresses; here we test the per-slice naming in isolation).
TEST(Composing_DecodeChord, Fixture_CleanTriads_NameThatChord)
{
    MasterScore* score = ScoreRW::readScore(u"data/s1c_c_major.mscx");
    ASSERT_TRUE(score);
    const NoteModel model = NoteModel::build(score);
    const auto slices = changePointSlices(model);
    ASSERT_EQ(slices.size(), 2u) << "two whole-note triads → two constant-sonority slices";

    ChordSliceDecoderPreferences p;
    p.contextSlices = 0;   // window = the slice alone (isolate each triad)
    const auto d = CSD::decode(slices, model, /*keySigFifths=*/0, KeySigMode::Ionian,
                               mu::composing::analysis::kDefaultChordAnalyzerPreferences, p);
    ASSERT_EQ(d.size(), 2u);

    EXPECT_TRUE(d[0].hasChord);
    EXPECT_EQ(d[0].chosen.rootPc, 0) << "slice 0 is C major";
    EXPECT_EQ(d[0].chosen.quality, ChordQuality::Major);
    EXPECT_TRUE(d[0].chosen.bassIsRoot());

    EXPECT_TRUE(d[1].hasChord);
    EXPECT_EQ(d[1].chosen.rootPc, 7) << "slice 1 is G major";
    EXPECT_EQ(d[1].chosen.quality, ChordQuality::Major);
    EXPECT_TRUE(d[1].chosen.bassIsRoot());

    delete score;
}

// The complete candidate list is surfaced and ranked: every named slice carries
// alternatives, the chosen is the top-scoring candidate, and the alternatives are
// in non-increasing score order.
TEST(Composing_DecodeChord, Fixture_CompleteCandidateListSurfacedAndRanked)
{
    MasterScore* score = ScoreRW::readScore(u"data/s1c_seg_changes.mscx");
    ASSERT_TRUE(score);
    const NoteModel model = NoteModel::build(score);
    const auto slices = changePointSlices(model);
    ASSERT_GE(slices.size(), 4u);

    const auto d = CSD::decode(slices, model, /*keySigFifths=*/0, KeySigMode::Ionian);
    ASSERT_EQ(d.size(), slices.size());

    int named = 0;
    for (const SliceChord& sc : d) {
        if (!sc.hasChord) {
            continue;
        }
        ++named;
        // The chosen is at least as good as the best carried alternative (ranked).
        for (const ChordSliceCandidate& a : sc.alternatives) {
            EXPECT_LE(a.score, sc.chosen.score) << "alternatives never outrank the chosen";
        }
        // Alternatives are in non-increasing score order.
        for (size_t i = 1; i < sc.alternatives.size(); ++i) {
            EXPECT_LE(sc.alternatives[i].score, sc.alternatives[i - 1].score);
        }
    }
    EXPECT_GT(named, 0) << "the progression names at least one chord";

    delete score;
}

TEST(Composing_DecodeChord, Fixture_Determinism)
{
    MasterScore* score = ScoreRW::readScore(u"data/s1c_seg_changes.mscx");
    ASSERT_TRUE(score);
    const NoteModel model = NoteModel::build(score);
    const auto slices = changePointSlices(model);

    const auto a = CSD::decode(slices, model, 0, KeySigMode::Ionian);
    const auto b = CSD::decode(slices, model, 0, KeySigMode::Ionian);
    ASSERT_EQ(a.size(), b.size());
    for (size_t i = 0; i < a.size(); ++i) {
        EXPECT_EQ(a[i].hasChord, b[i].hasChord);
        EXPECT_EQ(a[i].chosen.rootPc, b[i].chosen.rootPc);
        EXPECT_EQ(a[i].chosen.quality, b[i].chosen.quality);
        EXPECT_EQ(a[i].chosen.bassPc, b[i].chosen.bassPc);
        EXPECT_DOUBLE_EQ(a[i].confidence, b[i].confidence);
        EXPECT_EQ(a[i].uncertain, b[i].uncertain);
    }

    delete score;
}

// A sub-range re-decode reproduces the matching slices of a full decode EXACTLY
// (the per-slice decision is context-free; one slice of look-back recovers the
// prevailing chord of the first slice).
TEST(Composing_DecodeChord, Fixture_RedecodeRange_MatchesFullDecode)
{
    MasterScore* score = ScoreRW::readScore(u"data/s1c_seg_changes.mscx");
    ASSERT_TRUE(score);
    const NoteModel model = NoteModel::build(score);
    const auto slices = changePointSlices(model);
    ASSERT_GE(slices.size(), 3u);

    const auto full = CSD::decode(slices, model, 0, KeySigMode::Ionian);
    const int first = 1;
    const int last = static_cast<int>(slices.size()) - 1;
    const auto sub = CSD::redecodeRange(slices, model, 0, KeySigMode::Ionian, first, last);

    ASSERT_EQ(sub.size(), static_cast<size_t>(last - first + 1));
    for (size_t i = 0; i < sub.size(); ++i) {
        EXPECT_EQ(sub[i].sliceIndex, first + static_cast<int>(i));
        EXPECT_EQ(sub[i].hasChord, full[first + i].hasChord);
        EXPECT_EQ(sub[i].chosen.rootPc, full[first + i].chosen.rootPc) << "slice " << (first + i);
        EXPECT_EQ(sub[i].chosen.quality, full[first + i].chosen.quality) << "slice " << (first + i);
        EXPECT_EQ(sub[i].chosen.bassPc, full[first + i].chosen.bassPc) << "slice " << (first + i);
        EXPECT_DOUBLE_EQ(sub[i].confidence, full[first + i].confidence) << "slice " << (first + i);
    }

    delete score;
}

TEST(Composing_DecodeChord, EmptyModel_NoSlices)
{
    const std::vector<mu::composing::analysis::slicing::Slice> noSlices;
    const NoteModel empty;
    EXPECT_TRUE(CSD::decode(noSlices, empty, 0, KeySigMode::Ionian).empty());
}
