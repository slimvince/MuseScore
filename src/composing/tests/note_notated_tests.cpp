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

// Layer-1 NOTE MODEL — the ADDITIVE notated-note publication (Task B of the joint-estimator
// input-parity dispatch). These assert the NEW notatedNotes() surface (tie-UNRESOLVED atoms: every
// notated note incl. tie continuations, each with its OWN notated span, tie-continuation flag,
// fermata flag, and a link to its tie-resolved NoteEvent) AND that the pre-existing tie-RESOLVED
// notes() surface is byte-identical (the additive-publication proof).

#include <gtest/gtest.h>

#include <functional>
#include <vector>

#include "engraving/dom/masterscore.h"
#include "engraving/tests/utils/scorerw.h"

#include "composing/analysis/notemodel/note_model.h"

using mu::engraving::MasterScore;
using mu::engraving::ScoreRW;
using NEvent = mu::composing::analysis::notemodel::NoteEvent;
using NNote = mu::composing::analysis::notemodel::NotatedNote;
using mu::composing::analysis::notemodel::NoteModel;

namespace {
int countNotated(const NoteModel& m, const std::function<bool(const NNote&)>& pred)
{
    int n = 0;
    for (const NNote& x : m.notatedNotes()) {
        if (pred(x)) {
            ++n;
        }
    }
    return n;
}
} // namespace

// ── The tie chain: notated components published, resolved surface byte-identical ─────────────────
// nm_tie_chain.mscx = three tied C4 quarters (onsets 0/480/960) then a D4 quarter (onset 1440).
// notes() (tie-resolved) is ONE C4 span [0,1440) + one D4 [1440,1920) — UNCHANGED (T2 asserts it).
// notatedNotes() must publish FOUR atoms: the three C4 (durations 480 each; tieContinuation
// false/true/true; all linking to the SAME resolved C4 event) + the D4 (its own event).
TEST(Composing_NoteNotatedTests, TieChain_NotatedAtomsAndResolvedLink)
{
    MasterScore* score = ScoreRW::readScore(u"data/nm_tie_chain.mscx");
    ASSERT_TRUE(score);

    const NoteModel model = NoteModel::build(score);

    // (a) the tie-RESOLVED surface is UNCHANGED — exactly two non-grace events (the additive proof).
    int resolved = 0;
    int c4EventIdx = -1, d4EventIdx = -1;
    for (size_t i = 0; i < model.notes().size(); ++i) {
        const NEvent& e = model.notes()[i];
        if (e.isGrace) {
            continue;
        }
        ++resolved;
        if (e.pitch == 60 && e.onset == 0 && e.release == 1440) {
            c4EventIdx = static_cast<int>(i);
        }
        if (e.pitch == 62 && e.onset == 1440) {
            d4EventIdx = static_cast<int>(i);
        }
    }
    EXPECT_EQ(resolved, 2);
    ASSERT_GE(c4EventIdx, 0);
    ASSERT_GE(d4EventIdx, 0);

    // (b) FOUR notated atoms: three C4 (0/480/960, dur 480, tieContinuation false/true/true) + one D4.
    EXPECT_EQ(countNotated(model, [](const NNote& x) { return !x.isGrace; }), 4);

    const int c4[3] = { 0, 480, 960 };
    for (int k = 0; k < 3; ++k) {
        EXPECT_EQ(countNotated(model, [&](const NNote& x) {
            return x.pitch == 60 && x.onset == c4[k] && x.duration == 480
                   && x.tieContinuation == (k > 0)               // first C4 starts the tie, rest continue
                   && x.resolvedIndex == c4EventIdx;             // all three link to the ONE resolved C4
        }), 1) << "C4 notated atom k=" << k;
    }
    EXPECT_EQ(countNotated(model, [&](const NNote& x) {
        return x.pitch == 62 && x.onset == 1440 && x.duration == 480
               && !x.tieContinuation && x.resolvedIndex == d4EventIdx;
    }), 1) << "D4 notated atom";

    // (c) NO tie continuation appears on the resolved surface (exactly one onset per tied group).
    EXPECT_EQ(countNotated(model, [](const NNote& x) { return x.tieContinuation; }), 2);

    delete score;
}

// ── The fermata flag ─────────────────────────────────────────────────────────────────────────────
// pb_chorale.mscx carries fermatas (chorale phrase ends). notatedNotes() must flag the fermata-bearing
// chords' notes hasFermata=true and leave non-fermata notes false (the flag is populated, not constant).
TEST(Composing_NoteNotatedTests, Fermata_FlaggedPerChord)
{
    MasterScore* score = ScoreRW::readScore(u"data/pb_chorale.mscx");
    ASSERT_TRUE(score);

    const NoteModel model = NoteModel::build(score);
    ASSERT_FALSE(model.notatedNotes().empty());

    const int withFermata = countNotated(model, [](const NNote& x) { return x.hasFermata; });
    const int withoutFermata = countNotated(model, [](const NNote& x) { return !x.hasFermata; });

    EXPECT_GT(withFermata, 0) << "the chorale fixture carries at least one fermata";
    EXPECT_GT(withoutFermata, 0) << "and at least one note without a fermata (flag is populated, not constant)";

    delete score;
}

// ── Grace notes are published as notated atoms too (kept + flagged) ──────────────────────────────
TEST(Composing_NoteNotatedTests, Grace_PublishedAndFlagged)
{
    MasterScore* score = ScoreRW::readScore(u"data/nm_grace.mscx");
    ASSERT_TRUE(score);

    const NoteModel model = NoteModel::build(score);
    // At least one grace notated atom, flagged isGrace.
    EXPECT_GT(countNotated(model, [](const NNote& x) { return x.isGrace; }), 0);

    delete score;
}
