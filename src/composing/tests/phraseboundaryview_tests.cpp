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

// ── Phrase-boundary primitive tests (design §7) ───────────────────────────────
//
// Two tiers, mirroring the design's mechanism:
//   • ORACLE tests of the pure local-change / normalisation / peak-picking rules
//     (§4.1, §4.4) on constructed value sequences — hand-computed, no Score.
//   • FULL-PIPELINE tests of computePhraseBoundaryProfile on real .mscx fixtures —
//     a Bach chorale (fermata markers, per-voice + texture, ends-a-phrase) and a
//     rest fixture (the all-voice-rest marker). Chorale-corpus validation: the
//     fermata phrase-ends are ground truth, and a marker spike must always be
//     picked. (Broader corpus validation across many chorales is done at script
//     level via batch_analyze --dump-cadence-anchor; see the build report.)

#include <gtest/gtest.h>

#include <map>
#include <set>
#include <vector>

#include "engraving/dom/engravingitem.h"
#include "engraving/dom/masterscore.h"
#include "engraving/dom/measure.h"
#include "engraving/dom/score.h"
#include "engraving/dom/segment.h"
#include "engraving/types/fraction.h"
#include "engraving/tests/utils/scorerw.h"

#include "composing/analysis/engravingbridge/phraseboundaryview.h"

namespace ebr = mu::composing::analysis::engravingbridge;
using mu::engraving::MasterScore;
using mu::engraving::ScoreRW;

namespace {

// Ground-truth fermata ticks of a score (the chorale phrase ends), read with the
// same surface convention the retired fermata-only scan used.
std::set<int> fermataTicks(const mu::engraving::Score* score)
{
    using namespace mu::engraving;
    std::set<int> ticks;
    for (const Measure* m = score->firstMeasure(); m; m = m->nextMeasure()) {
        for (const Segment* s = m->first(SegmentType::ChordRest); s;
             s = s->next(SegmentType::ChordRest)) {
            for (const EngravingItem* e : s->annotations()) {
                if (e && e->isFermata()) {
                    ticks.insert(s->tick().ticks());
                    break;
                }
            }
        }
    }
    return ticks;
}

int scoreEndTick(const mu::engraving::Score* score)
{
    using namespace mu::engraving;
    int last = 0;
    for (const Measure* m = score->firstMeasure(); m; m = m->nextMeasure()) {
        last = m->endTick().ticks();
    }
    return last;
}

} // namespace

// ─────────────────────────── ORACLE: the local-change rule (§4.1) ─────────────

TEST(Composing_PhraseBoundaryView, ChangeRatio_basics)
{
    EXPECT_DOUBLE_EQ(ebr::changeRatio(5.0, 5.0), 0.0);   // no change
    EXPECT_DOUBLE_EQ(ebr::changeRatio(0.0, 10.0), 1.0);  // full change (one side zero)
    EXPECT_DOUBLE_EQ(ebr::changeRatio(10.0, 0.0), 1.0);
    EXPECT_DOUBLE_EQ(ebr::changeRatio(0.0, 0.0), 0.0);   // both zero -> defined 0
    EXPECT_DOUBLE_EQ(ebr::changeRatio(2.0, 6.0), 0.5);   // |2-6|/(2+6)
}

// A long note among short ones (or a large gap among small gaps) yields a peak in
// the local-change profile exactly at the large value (design §7 oracle).
TEST(Composing_PhraseBoundaryView, LocalChange_longValueYieldsPeak)
{
    const std::vector<double> values = { 2, 2, 2, 8, 2, 2 };   // a long note at index 3
    const std::vector<double> s = ebr::localChangeProfile(values);
    ASSERT_EQ(s.size(), values.size());
    // hand-computed: [0, 0, 1.2, 9.6, 1.2, 0]
    EXPECT_NEAR(s[3], 9.6, 1e-9);
    for (size_t i = 0; i < s.size(); ++i) {
        if (i != 3) {
            EXPECT_LT(s[i], s[3]) << "index " << i << " should be below the peak";
        }
    }
}

TEST(Composing_PhraseBoundaryView, LocalChange_flatSequenceIsZero)
{
    const std::vector<double> s = ebr::localChangeProfile({ 3, 3, 3, 3 });
    for (double x : s) {
        EXPECT_DOUBLE_EQ(x, 0.0);   // no local change anywhere
    }
}

TEST(Composing_PhraseBoundaryView, LocalChange_edgesAndDegenerate)
{
    EXPECT_TRUE(ebr::localChangeProfile({}).empty());
    EXPECT_EQ(ebr::localChangeProfile({ 5 }), std::vector<double>({ 0.0 }));  // single point, one-sided -> 0
    // two points [1,9]: i0 = 1*cr(1,9)=0.8 ; i1 = 9*cr(1,9)=7.2
    const std::vector<double> s = ebr::localChangeProfile({ 1, 9 });
    ASSERT_EQ(s.size(), 2u);
    EXPECT_NEAR(s[0], 0.8, 1e-9);
    EXPECT_NEAR(s[1], 7.2, 1e-9);
}

TEST(Composing_PhraseBoundaryView, MaxNormalize)
{
    std::vector<double> v = { 2, 4, 1 };
    ebr::maxNormalizeInPlace(v);
    EXPECT_DOUBLE_EQ(v[0], 0.5);
    EXPECT_DOUBLE_EQ(v[1], 1.0);
    EXPECT_DOUBLE_EQ(v[2], 0.25);

    std::vector<double> zero = { 0, 0, 0 };
    ebr::maxNormalizeInPlace(zero);                       // non-positive max -> unchanged
    EXPECT_EQ(zero, std::vector<double>({ 0, 0, 0 }));

    std::vector<double> empty;
    ebr::maxNormalizeInPlace(empty);                      // no crash
    EXPECT_TRUE(empty.empty());
}

// ─────────────────────────── ORACLE: peak-picking (§4.4) ──────────────────────

// A single low bump among real peaks does NOT clear the (peak-elevated) adaptive
// threshold, while the real peaks do — the design's "single mid-phrase leap does
// not clear the threshold alone" (scenario 5), and "a strong peak/marker clears".
TEST(Composing_PhraseBoundaryView, PickPeaks_smallBumpRejectedRealPeaksKept)
{
    const std::vector<double> texture = { 0, 0, 0.2, 0, 0, 1.5, 0, 0, 1.5, 0, 0 };
    const std::vector<int> picked = ebr::pickPeaks(texture, /*k=*/1.0);
    const std::set<int> got(picked.begin(), picked.end());
    EXPECT_TRUE(got.count(5));   // real peak kept
    EXPECT_TRUE(got.count(8));   // real peak kept
    EXPECT_FALSE(got.count(2));  // low-weighted single bump rejected
}

TEST(Composing_PhraseBoundaryView, PickPeaks_isolatedSpikeKept_flatRejected)
{
    const std::vector<int> spike = ebr::pickPeaks({ 0, 0, 0, 5, 0, 0, 0 }, 1.0);
    ASSERT_EQ(spike.size(), 1u);
    EXPECT_EQ(spike[0], 3);

    EXPECT_TRUE(ebr::pickPeaks({ 1, 1, 1, 1 }, 1.0).empty());   // flat: nothing clears mean
    EXPECT_TRUE(ebr::pickPeaks({}, 1.0).empty());
}

// ─────────────────────────── FULL PIPELINE on a Bach chorale ──────────────────

// Per-voice profiles exist, the texture aggregate exists, boundaries are picked,
// and EVERY fermata phrase-end (ground truth) is a picked boundary — a marker
// spike dominates by construction (§4.2/§4.4).
TEST(Composing_PhraseBoundaryView, Chorale_fermataPhraseEndsArePicked)
{
    MasterScore* score = ScoreRW::readScore(u"data/pb_chorale.mscx");
    ASSERT_TRUE(score);

    const ebr::PhraseBoundaryProfile profile = ebr::computePhraseBoundaryProfile(score);

    EXPECT_GE(profile.perVoice.size(), 2u) << "a chorale is polyphonic";
    EXPECT_FALSE(profile.textureStrength.empty());
    EXPECT_EQ(profile.textureTicks.size(), profile.textureStrength.size());
    EXPECT_FALSE(profile.pickedTicks.empty());

    const std::set<int> ferms = fermataTicks(score);
    ASSERT_FALSE(ferms.empty()) << "fixture precondition: the chorale has fermatas";
    for (int ft : ferms) {
        EXPECT_TRUE(profile.pickedTicks.count(ft) > 0)
            << "fermata phrase-end tick " << ft << " must be a picked boundary";
    }
}

// The structural FINAL barline at the score end is a marker spike -> a picked
// boundary (design §4.2 / §4.4; the consumers' last-region rule also covers it).
TEST(Composing_PhraseBoundaryView, Chorale_finalBarlineIsPicked)
{
    MasterScore* score = ScoreRW::readScore(u"data/pb_chorale.mscx");
    ASSERT_TRUE(score);
    const ebr::PhraseBoundaryProfile profile = ebr::computePhraseBoundaryProfile(score);
    const int endTick = scoreEndTick(score);
    EXPECT_TRUE(profile.pickedTicks.count(endTick) > 0)
        << "the final barline tick " << endTick << " must be picked";
}

// Per-voice profiles aggregate into the texture (design §4.3): every per-voice
// onset is on the texture grid, the texture strength is at least the per-voice
// surface sum there (texture = sum of per-voice strengths, plus any marker spike),
// and a homophonic chorale has coincident onsets where several voices contribute.
// (A point where many voices phrase together therefore scores higher than a single
// inner voice would — the basis for "per-voice boundary but low texture".)
TEST(Composing_PhraseBoundaryView, PerVoiceAggregatesIntoTexture)
{
    MasterScore* score = ScoreRW::readScore(u"data/pb_chorale.mscx");
    ASSERT_TRUE(score);
    const ebr::PhraseBoundaryProfile p = ebr::computePhraseBoundaryProfile(score);
    EXPECT_GE(p.perVoice.size(), 2u);

    std::map<int, double> surfaceSum;
    std::map<int, int>    voiceCount;
    for (const ebr::VoiceBoundaryProfile& v : p.perVoice) {
        ASSERT_EQ(v.onsets.size(), v.strength.size());
        for (size_t i = 0; i < v.onsets.size(); ++i) {
            surfaceSum[v.onsets[i]] += v.strength[i];
            voiceCount[v.onsets[i]] += 1;
        }
    }
    std::map<int, double> tex;
    for (size_t i = 0; i < p.textureTicks.size(); ++i) {
        tex[p.textureTicks[i]] = p.textureStrength[i];
    }
    bool sawCoincident = false;
    for (const auto& [tick, sum] : surfaceSum) {
        ASSERT_TRUE(tex.count(tick) > 0) << "per-voice onset " << tick << " absent from texture grid";
        EXPECT_GE(tex[tick] + 1e-9, sum) << "texture below the per-voice surface sum at " << tick;
        if (voiceCount[tick] >= 2) {
            sawCoincident = true;
        }
    }
    EXPECT_TRUE(sawCoincident) << "a homophonic chorale has coincident onsets";
}

// A region that contains a picked boundary "ends a phrase" — the derivation the
// (dormant/gated) consumers apply. Here exercised against the chorale's picks.
TEST(Composing_PhraseBoundaryView, Chorale_endsAPhraseDerivation)
{
    MasterScore* score = ScoreRW::readScore(u"data/pb_chorale.mscx");
    ASSERT_TRUE(score);
    const std::set<int> picks = ebr::computePhraseBoundaryProfile(score).pickedTicks;
    ASSERT_FALSE(picks.empty());

    // A half-open region [start,end) ends a phrase iff a picked tick lies in it.
    const int b = *picks.begin();
    auto regionEndsPhrase = [&](int start, int end) {
        auto it = picks.lower_bound(start);
        return it != picks.end() && *it < end;
    };
    EXPECT_TRUE(regionEndsPhrase(b, b + 1));          // the picked tick itself
    EXPECT_FALSE(regionEndsPhrase(b + 1, b + 2));     // a one-tick gap just after it (no pick)
}

// ─────────────────────────── FULL PIPELINE on a rest fixture ──────────────────

// The all-voice-rest interior span (a Layer-2 empty slice) yields a boundary
// (the all-voice-rest marker and/or the gap-profile peak) — robust smoke that the
// rest cue path runs and produces a pick (design §5 scenario 2).
TEST(Composing_PhraseBoundaryView, RestFixture_producesABoundary)
{
    MasterScore* score = ScoreRW::readScore(u"data/nm_slice_rest.mscx");
    ASSERT_TRUE(score);
    const ebr::PhraseBoundaryProfile profile = ebr::computePhraseBoundaryProfile(score);
    EXPECT_FALSE(profile.textureStrength.empty());
    EXPECT_FALSE(profile.pickedTicks.empty());
}

// The chorale's complete phrase structure is captured: the fermata phrase-ends
// plus the closing barline, and nothing spurious — a clean, proportionate pick set
// (bwv10.7: 4 fermata phrase-ends + the final barline = 5 boundaries).
TEST(Composing_PhraseBoundaryView, Chorale_pickSetIsTheClosePhraseStructure)
{
    MasterScore* score = ScoreRW::readScore(u"data/pb_chorale.mscx");
    ASSERT_TRUE(score);
    const std::set<int> picks = ebr::computePhraseBoundaryProfile(score).pickedTicks;
    const std::set<int> ferms = fermataTicks(score);
    // every fermata phrase-end + the final barline is present ...
    std::set<int> expected = ferms;
    expected.insert(scoreEndTick(score));
    for (int e : expected) {
        EXPECT_TRUE(picks.count(e) > 0) << "expected boundary " << e << " missing";
    }
    // ... and the pick set stays proportionate to the phrase structure (no flood).
    EXPECT_LE(picks.size(), ferms.size() + 4);
}

// A null score is handled (empty profile, empty ticks).
TEST(Composing_PhraseBoundaryView, NullScoreIsSafe)
{
    const ebr::PhraseBoundaryProfile profile = ebr::computePhraseBoundaryProfile(nullptr);
    EXPECT_TRUE(profile.perVoice.empty());
    EXPECT_TRUE(profile.pickedTicks.empty());
    EXPECT_TRUE(ebr::phraseBoundaryTicks(nullptr).empty());
}
