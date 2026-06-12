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

// ── Bounded-window decode cache tests (Stage 3.1b) ───────────────────────────
//
// The Stage-3.1b cache MEMOIZES the per-window section build inside the unchanged
// expanding-window P3 path, so the cache is BYTE-IDENTITY-preserving. Pins:
//   • cached == uncached at every tick across a warm sweep (incl. MRU eviction) —
//     the byte-identity guarantee, the whole point of the bounded-window design.
//   • a re-click on the same tick adds no window builds (warm hit).
//   • an undoable edit advances the change token and flushes the cache.
//   • distinct scores do not share the cache (pointer/token-guarded flush).

#include <gtest/gtest.h>

#include <set>
#include <vector>

#include "global/types/translatablestring.h"

#include "engraving/dom/masterscore.h"
#include "engraving/dom/measure.h"
#include "engraving/dom/segment.h"
#include "engraving/dom/chord.h"
#include "engraving/dom/note.h"
#include "engraving/dom/property.h"
#include "engraving/editing/undo.h"

#include "notation/internal/notationcomposingbridge.h"

#include "engraving/tests/utils/scorerw.h"
#include "test_helpers.h"

using namespace mu::engraving;
using namespace mu::notation;
using mu::engraving::ScoreRW;

namespace {

const muse::String kTestScore =
    u"../../../../tools/dcml/corelli/MS3/op01n08d.mscx";

std::vector<int> chordBearingTicks(MasterScore* score)
{
    std::vector<int> ticks;
    int lastTick = -1;
    for (Segment* s = score->firstMeasure()->first(SegmentType::ChordRest);
         s;
         s = s->next1(SegmentType::ChordRest)) {
        bool anyChord = false;
        for (size_t track = 0; track < score->ntracks(); ++track) {
            const EngravingItem* el = s->element(static_cast<track_idx_t>(track));
            if (el && el->isChord()) { anyChord = true; break; }
        }
        if (anyChord) {
            const int t = s->tick().ticks();
            if (t != lastTick) { ticks.push_back(t); lastTick = t; }
        }
    }
    return ticks;
}

::testing::AssertionResult contextsEqual(const NoteHarmonicContext& a,
                                         const NoteHarmonicContext& b)
{
    if (a.keyFifths != b.keyFifths)   return ::testing::AssertionFailure() << "keyFifths";
    if (a.keyMode != b.keyMode)       return ::testing::AssertionFailure() << "keyMode";
    if (a.keyConfidence != b.keyConfidence) return ::testing::AssertionFailure() << "keyConfidence";
    if (a.wasRegional != b.wasRegional) return ::testing::AssertionFailure() << "wasRegional";
    if (a.chordResults.size() != b.chordResults.size())
        return ::testing::AssertionFailure() << "chordResults size";
    for (size_t i = 0; i < a.chordResults.size(); ++i) {
        const auto& ra = a.chordResults[i].identity;
        const auto& rb = b.chordResults[i].identity;
        if (ra.rootPc != rb.rootPc || ra.bassPc != rb.bassPc
            || ra.quality != rb.quality || ra.extensions != rb.extensions
            || ra.score != rb.score)
            return ::testing::AssertionFailure() << "chordResults[" << i << "] identity";
    }
    return ::testing::AssertionSuccess();
}

} // namespace

class Notation_DecodeCacheTests : public ::testing::Test {};

// ── byte-identity: cached == uncached at every tick across a warm sweep ───────
// A single warm sweep (no per-tick clear) drives the MRU through eviction on a
// score with more windows than kMaxWindowEntries; every tick must still equal the
// cache-bypassed reference.
TEST_F(Notation_DecodeCacheTests, CachedEqualsUncachedAcrossWarmSweep)
{
    MasterScore* score = ScoreRW::readScore(kTestScore);
    ASSERT_TRUE(score);

    const std::vector<int> ticks = chordBearingTicks(score);
    ASSERT_FALSE(ticks.empty());

    clearHarmonicDecodeCacheForTesting();
    for (int tk : ticks) {
        const Fraction t = Fraction::fromTicks(tk);
        NoteHarmonicContext cached   = analyzeHarmonicContextAtTick(score, t);                 // warm path
        NoteHarmonicContext uncached = analyzeHarmonicContextAtTickUncachedForTesting(score, t); // bypass
        EXPECT_TRUE(contextsEqual(cached, uncached)) << "byte-identity mismatch at tick " << tk;
    }

    delete score;
}

// ── warm re-click adds no window builds ──────────────────────────────────────
TEST_F(Notation_DecodeCacheTests, ReclickAddsNoBuilds)
{
    MasterScore* score = ScoreRW::readScore(kTestScore);
    ASSERT_TRUE(score);

    const std::vector<int> ticks = chordBearingTicks(score);
    ASSERT_GT(ticks.size(), 3u);
    const Fraction t = Fraction::fromTicks(ticks[ticks.size() / 2]);

    clearHarmonicDecodeCacheForTesting();
    const size_t b0 = harmonicDecodeCacheBuildCountForTesting();

    NoteHarmonicContext first = analyzeHarmonicContextAtTick(score, t);
    const size_t b1 = harmonicDecodeCacheBuildCountForTesting();
    EXPECT_GT(b1, b0) << "first query must build at least one window section";

    NoteHarmonicContext second = analyzeHarmonicContextAtTick(score, t);
    EXPECT_EQ(harmonicDecodeCacheBuildCountForTesting(), b1)
        << "re-click on the same tick must hit every window (no rebuild)";
    EXPECT_TRUE(contextsEqual(first, second));
    EXPECT_FALSE(first.chordResults.empty());

    delete score;
}

// ── invalidation on edit ─────────────────────────────────────────────────────
TEST_F(Notation_DecodeCacheTests, InvalidationOnEdit)
{
    MasterScore* score = ScoreRW::readScore(kTestScore);
    ASSERT_TRUE(score);

    const std::vector<int> ticks = chordBearingTicks(score);
    ASSERT_GT(ticks.size(), 2u);
    const Fraction t = Fraction::fromTicks(ticks[1]);

    clearHarmonicDecodeCacheForTesting();
    analyzeHarmonicContextAtTick(score, t);
    const size_t bAfterWarm = harmonicDecodeCacheBuildCountForTesting();
    analyzeHarmonicContextAtTick(score, t);
    EXPECT_EQ(harmonicDecodeCacheBuildCountForTesting(), bAfterWarm) << "still warm";

    // Undoable edit → undo-stack change token advances.
    Note* firstNote = nullptr;
    for (Segment* s = score->firstMeasure()->first(SegmentType::ChordRest);
         s && !firstNote; s = s->next1(SegmentType::ChordRest)) {
        for (size_t track = 0; track < score->ntracks(); ++track) {
            EngravingItem* el = s->element(static_cast<track_idx_t>(track));
            if (el && el->isChord()) { firstNote = toChord(el)->upNote(); break; }
        }
    }
    ASSERT_TRUE(firstNote);

    const size_t tokenBefore = score->undoStack()->currentIndex();
    score->startCmd(TranslatableString::untranslatable("Decode cache test edit"));
    firstNote->undoChangeProperty(Pid::TUNING, 7.0);
    score->endCmd();
    ASSERT_NE(score->undoStack()->currentIndex(), tokenBefore) << "edit must advance the token";

    analyzeHarmonicContextAtTick(score, t);
    EXPECT_GT(harmonicDecodeCacheBuildCountForTesting(), bAfterWarm)
        << "an edit that advances the change token must flush the cache (rebuild)";

    delete score;
}

// ── lifecycle flush closes the pointer-reuse hazard ──────────────────────────
// clearHarmonicDecodeCache() is what Notation::setScore() calls on every score
// install. This pins that it actually drops the cache (so a reused-address score
// installed later cannot false-hit). The address-reuse case itself is not
// deterministically forceable in the ScoreRW test env (no Notation; the allocator
// may or may not reuse a freed address) — the production guarantee is that every
// queried score is installed via setScore first, and that install flushes. Here we
// pin the flush primitive directly.
TEST_F(Notation_DecodeCacheTests, LifecycleFlushDropsCache)
{
    MasterScore* score = ScoreRW::readScore(kTestScore);
    ASSERT_TRUE(score);

    const std::vector<int> ticks = chordBearingTicks(score);
    ASSERT_GT(ticks.size(), 2u);
    const Fraction t = Fraction::fromTicks(ticks[ticks.size() / 2]);

    clearHarmonicDecodeCacheForTesting();
    analyzeHarmonicContextAtTick(score, t);
    const size_t bWarm = harmonicDecodeCacheBuildCountForTesting();
    analyzeHarmonicContextAtTick(score, t);
    ASSERT_EQ(harmonicDecodeCacheBuildCountForTesting(), bWarm) << "warm before flush";

    // The production lifecycle flush (Notation::setScore calls this on score install).
    clearHarmonicDecodeCache();

    analyzeHarmonicContextAtTick(score, t);
    EXPECT_GT(harmonicDecodeCacheBuildCountForTesting(), bWarm)
        << "lifecycle flush must drop the cache so the next query rebuilds";

    delete score;
}

// ── distinct scores do not share the cache ───────────────────────────────────
TEST_F(Notation_DecodeCacheTests, DistinctScoresDoNotShareCache)
{
    MasterScore* a = ScoreRW::readScore(kTestScore);
    MasterScore* b = ScoreRW::readScore(kTestScore);
    ASSERT_TRUE(a);
    ASSERT_TRUE(b);

    const std::vector<int> ticksA = chordBearingTicks(a);
    ASSERT_FALSE(ticksA.empty());
    const Fraction t = Fraction::fromTicks(ticksA[ticksA.size() / 2]);

    clearHarmonicDecodeCacheForTesting();
    NoteHarmonicContext a1 = analyzeHarmonicContextAtTick(a, t);
    const size_t afterA1 = harmonicDecodeCacheBuildCountForTesting();

    analyzeHarmonicContextAtTick(b, t);                       // different pointer → flush + rebuild
    EXPECT_GT(harmonicDecodeCacheBuildCountForTesting(), afterA1);
    const size_t afterB = harmonicDecodeCacheBuildCountForTesting();

    NoteHarmonicContext a2 = analyzeHarmonicContextAtTick(a, t);   // back to a → flush + rebuild
    EXPECT_GT(harmonicDecodeCacheBuildCountForTesting(), afterB);
    EXPECT_TRUE(contextsEqual(a1, a2)) << "score a's answer is stable across cache flushes";

    delete a;
    delete b;
}
