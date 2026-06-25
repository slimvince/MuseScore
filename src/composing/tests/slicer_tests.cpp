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

// Layer-2 CHANGE-POINT SLICER tests (audit §3 functional set + the measured
// full-branch coverage gate).
//
// The slicer is a pure, deterministic FACT over the layer-1 note model:
// boundaries at every ELIGIBLE onset AND release, tiling the domain with a
// covering, lossless partition (all-rest interior spans are explicit empty
// slices), zero interpretation, no special-casing of any note kind. Each test
// asserts the exact [start,end) slice list and, for constant-sonority cases, the
// eligible overlapping() note set. Oracle tags: C = completeness, S =
// constant-sonority, N = no-spurious/missed.

#include <gtest/gtest.h>

#include <algorithm>
#include <climits>
#include <utility>
#include <vector>

#include "engraving/dom/masterscore.h"
#include "engraving/tests/utils/scorerw.h"

#include "composing/analysis/notemodel/note_model.h"
#include "composing/analysis/slicing/slicer.h"

using mu::engraving::MasterScore;
using mu::engraving::ScoreRW;
using NEvent = mu::composing::analysis::notemodel::NoteEvent;
using mu::composing::analysis::notemodel::NoteModel;
using mu::composing::analysis::slicing::Slice;
using mu::composing::analysis::slicing::changePointSlices;

namespace {

// The exact [start,end) span list, for direct comparison against an expected literal.
std::vector<std::pair<int, int>> spans(const std::vector<Slice>& slices)
{
    std::vector<std::pair<int, int>> out;
    for (const Slice& s : slices) {
        out.push_back({ s.start, s.end });
    }
    return out;
}

// Layer-1 eligibility: a note is a tonal sounding member iff plays && visible &&
// staffEligible (the flags layer 1 set). The slicer keys boundaries off exactly
// this set; tests check constant-sonority over it.
bool eligible(const NEvent& e)
{
    return e.plays && e.visible && e.staffEligible;
}

// Sorted pitches of the ELIGIBLE notes overlapping [s,e) — the slice's identity set.
std::vector<int> eligiblePitches(const NoteModel& m, int s, int e)
{
    std::vector<int> out;
    for (const NEvent* n : m.overlapping(s, e)) {
        if (eligible(*n)) {
            out.push_back(n->pitch);
        }
    }
    std::sort(out.begin(), out.end());
    return out;
}

// Sorted pitches of ALL notes overlapping [s,e) — eligible AND the flagged
// non-eligible passengers (the pass-through set the slicer forwards untouched).
std::vector<int> allPitches(const NoteModel& m, int s, int e)
{
    std::vector<int> out;
    for (const NEvent* n : m.overlapping(s, e)) {
        out.push_back(n->pitch);
    }
    std::sort(out.begin(), out.end());
    return out;
}

// Count of eligible notes overlapping [s,e) (identity is the NOTE set, so a
// unison shrink changes the count even when the pitch-class set is constant).
int eligibleCount(const NoteModel& m, int s, int e)
{
    int n = 0;
    for (const NEvent* ev : m.overlapping(s, e)) {
        if (eligible(*ev)) {
            ++n;
        }
    }
    return n;
}

// Covering, lossless partition invariant: every slice is non-empty width and the
// slices are contiguous (no gaps, no overlaps) — slices[i].end == slices[i+1].start.
void expectCoveringPartition(const std::vector<Slice>& slices)
{
    for (size_t i = 0; i < slices.size(); ++i) {
        EXPECT_LT(slices[i].start, slices[i].end) << "slice " << i << " is zero/negative width";
        if (i + 1 < slices.size()) {
            EXPECT_EQ(slices[i].end, slices[i + 1].start)
                << "gap/overlap between slice " << i << " and " << (i + 1);
        }
    }
}

} // namespace

// ── S1 (case 1) — chord + one passing tone → 3 slices ────────────────────────
// C-E-G held the whole 3/4 bar [0,1440); a passing D sounds only [480,960). The
// passing tone opens and closes ONE slice; the chord is unchanged. C, S.
TEST(Composing_SlicerTests, S1_PassingTone_ThreeSlices)
{
    MasterScore* score = ScoreRW::readScore(u"data/nm_slice_passing.mscx");
    ASSERT_TRUE(score);
    const NoteModel model = NoteModel::build(score);

    const auto slices = changePointSlices(model);
    EXPECT_EQ(spans(slices),
              (std::vector<std::pair<int, int>>{ { 0, 480 }, { 480, 960 }, { 960, 1440 } }));
    expectCoveringPartition(slices);

    EXPECT_EQ(eligiblePitches(model, 0, 480), (std::vector<int>{ 60, 64, 67 }));
    EXPECT_EQ(eligiblePitches(model, 480, 960), (std::vector<int>{ 60, 62, 64, 67 }));   // + passing D
    EXPECT_EQ(eligiblePitches(model, 960, 1440), (std::vector<int>{ 60, 64, 67 }));

    delete score;
}

// ── S2 (case 2) — held chord under a moving melody → slice per melody onset ───
// C-E-G whole [0,1920) on staff 2; melody quarters C5 D5 E5 F5 on staff 1. Four
// slices, each = held chord + the current melody note. Also pins the coincident
// release+onset dedup (each melody release coincides with the next onset → ONE
// boundary, so exactly 4 slices, no zero-width sliver). C, S, N.
TEST(Composing_SlicerTests, S2_HeldChordUnderMelody_SlicePerOnset)
{
    MasterScore* score = ScoreRW::readScore(u"data/nm_slice_held_melody.mscx");
    ASSERT_TRUE(score);
    const NoteModel model = NoteModel::build(score);

    const auto slices = changePointSlices(model);
    EXPECT_EQ(spans(slices),
              (std::vector<std::pair<int, int>>{
                  { 0, 480 }, { 480, 960 }, { 960, 1440 }, { 1440, 1920 } }));
    expectCoveringPartition(slices);

    EXPECT_EQ(eligiblePitches(model, 0, 480), (std::vector<int>{ 60, 64, 67, 72 }));
    EXPECT_EQ(eligiblePitches(model, 480, 960), (std::vector<int>{ 60, 64, 67, 74 }));
    EXPECT_EQ(eligiblePitches(model, 960, 1440), (std::vector<int>{ 60, 64, 67, 76 }));
    EXPECT_EQ(eligiblePitches(model, 1440, 1920), (std::vector<int>{ 60, 64, 67, 77 }));

    delete score;
}

// ── S3 (case 3) — tie chain → no internal boundary ───────────────────────────
// 3 tied C4 quarters then a D4 quarter. Layer 1 merged the tie into one span
// [0,1440), so there is NO boundary at 480/960 — the tie-merge makes this clean. N.
TEST(Composing_SlicerTests, S3_TieChain_NoInternalBoundary)
{
    MasterScore* score = ScoreRW::readScore(u"data/nm_tie_chain.mscx");
    ASSERT_TRUE(score);
    const NoteModel model = NoteModel::build(score);

    const auto slices = changePointSlices(model);
    EXPECT_EQ(spans(slices),
              (std::vector<std::pair<int, int>>{ { 0, 1440 }, { 1440, 1920 } }));
    expectCoveringPartition(slices);

    EXPECT_EQ(eligiblePitches(model, 0, 1440), (std::vector<int>{ 60 }));
    EXPECT_EQ(eligiblePitches(model, 1440, 1920), (std::vector<int>{ 62 }));

    delete score;
}

// ── S4 (case 4) — chord tone releases mid-span → new slice (offset boundary) ──
// C and E sound as a dyad [0,960); G is a quarter [0,480) that RELEASES at 480.
// The boundary at 480 comes from G's RELEASE, not any onset — the offset-boundary
// core case. S, N.
TEST(Composing_SlicerTests, S4_MidSpanRelease_NewSlice)
{
    MasterScore* score = ScoreRW::readScore(u"data/nm_slice_release.mscx");
    ASSERT_TRUE(score);
    const NoteModel model = NoteModel::build(score);

    const auto slices = changePointSlices(model);
    EXPECT_EQ(spans(slices),
              (std::vector<std::pair<int, int>>{ { 0, 480 }, { 480, 960 } }));
    expectCoveringPartition(slices);

    EXPECT_EQ(eligiblePitches(model, 0, 480), (std::vector<int>{ 60, 64, 67 }));
    EXPECT_EQ(eligiblePitches(model, 480, 960), (std::vector<int>{ 60, 64 }));   // G released

    delete score;
}

// ── S4b (case 4b) — minimal release boundary (unison shrink) ─────────────────
// Two voices both sound E4: v0 a half [0,960), v1 a quarter [0,480). At 480 the
// note SET shrinks (2 → 1) though the pitch-CLASS set is unchanged (still {E}).
// Slice identity is the NOTE set, so this is a real boundary. S.
TEST(Composing_SlicerTests, S4b_UnisonShrink_NoteSetBoundary)
{
    MasterScore* score = ScoreRW::readScore(u"data/nm_unison.mscx");
    ASSERT_TRUE(score);
    const NoteModel model = NoteModel::build(score);

    const auto slices = changePointSlices(model);
    EXPECT_EQ(spans(slices),
              (std::vector<std::pair<int, int>>{ { 0, 480 }, { 480, 960 } }));
    expectCoveringPartition(slices);

    // Pitch-class set is constant ({E4}); the NOTE count is what changes.
    EXPECT_EQ(eligiblePitches(model, 0, 480), (std::vector<int>{ 64, 64 }));
    EXPECT_EQ(eligiblePitches(model, 480, 960), (std::vector<int>{ 64 }));
    EXPECT_EQ(eligibleCount(model, 0, 480), 2);
    EXPECT_EQ(eligibleCount(model, 480, 960), 1);

    delete score;
}

// ── S5 (case 5) — grace note: sliced by its layer-1 span, NO special rule ─────
// §3 verify-at-source finding: the acciaccatura is NOT zero-duration. Layer 1
// gives a grace event onset = parent chord tick and duration =
// playTicksFraction() = grace chord actualTicks() = the nominal written value
// (here durationType=eighth → 240). So the grace span is [0,240) and, under the
// zero-interpretation uniform slicer, it OPENS a boundary at 240 (the design's
// "duration-bearing grace opens a slice" branch). The slicer needs no grace code:
// the boundary falls out of the model span as a fact. The extra slice is a
// redundant candidate (necessary-but-not-sufficient contract; layer N groups it).
TEST(Composing_SlicerTests, S5_Grace_SlicedByLayer1Span_NoSpecialRule)
{
    MasterScore* score = ScoreRW::readScore(u"data/nm_grace.mscx");
    ASSERT_TRUE(score);
    const NoteModel model = NoteModel::build(score);

    // Document the verified layer-1 grace span: onset 0, release 240 (eighth).
    const NEvent* grace = nullptr;
    for (const NEvent& e : model.notes()) {
        if (e.isGrace && e.pitch == 79) {
            grace = &e;
            break;
        }
    }
    ASSERT_TRUE(grace) << "grace G5 present in the model";
    EXPECT_EQ(grace->onset, 0);
    EXPECT_EQ(grace->release, 240) << "grace is duration-bearing in layer 1 (nominal eighth)";

    const auto slices = changePointSlices(model);
    EXPECT_EQ(spans(slices),
              (std::vector<std::pair<int, int>>{ { 0, 240 }, { 240, 480 } }));
    expectCoveringPartition(slices);

    EXPECT_EQ(eligiblePitches(model, 0, 240), (std::vector<int>{ 60, 64, 67, 79 }));   // grace present
    EXPECT_EQ(eligiblePitches(model, 240, 480), (std::vector<int>{ 60, 64, 67 }));     // grace released

    delete score;
}

// ── S6 (case 6) — all-rest interior span → explicit EMPTY slice (covering) ────
// C4 [0,480), a rest [480,960), E4 [960,1440). The rest gap is NOT a hole: it is
// an explicit empty slice (eligible overlap set ∅), so the partition still tiles
// [0,1440) with no gaps. C, N.
TEST(Composing_SlicerTests, S6_AllRestInterior_EmptySlice)
{
    MasterScore* score = ScoreRW::readScore(u"data/nm_slice_rest.mscx");
    ASSERT_TRUE(score);
    const NoteModel model = NoteModel::build(score);

    const auto slices = changePointSlices(model);
    EXPECT_EQ(spans(slices),
              (std::vector<std::pair<int, int>>{ { 0, 480 }, { 480, 960 }, { 960, 1440 } }));
    expectCoveringPartition(slices);   // proves the empty middle slice is covering, not a gap

    EXPECT_EQ(eligiblePitches(model, 0, 480), (std::vector<int>{ 60 }));
    EXPECT_TRUE(eligiblePitches(model, 480, 960).empty()) << "the rest span is an EMPTY slice";
    EXPECT_EQ(eligiblePitches(model, 960, 1440), (std::vector<int>{ 64 }));

    delete score;
}

// ── S7a (edge) — empty model → no slices ─────────────────────────────────────
// No eligible notes (here: a null-sourced model) → fewer than two boundaries →
// the covering partition is empty. Exercises the size < 2 early return and the
// not-entered note loop.
TEST(Composing_SlicerTests, S7a_EmptyModel_NoSlices)
{
    const NoteModel model = NoteModel::build(nullptr);
    EXPECT_TRUE(changePointSlices(model).empty());
}

// ── S7b (edge) — single note → exactly one slice (and no horizon) ────────────
// A C4 held five whole notes [0,9600): exactly one slice spanning the full
// sustain (the slicer inherits the note model's no-horizon span). C, S.
TEST(Composing_SlicerTests, S7b_SingleNote_OneSlice)
{
    MasterScore* score = ScoreRW::readScore(u"data/nm_long_sustain.mscx");
    ASSERT_TRUE(score);
    const NoteModel model = NoteModel::build(score);

    const auto slices = changePointSlices(model);
    EXPECT_EQ(spans(slices), (std::vector<std::pair<int, int>>{ { 0, 9600 } }));
    EXPECT_EQ(eligiblePitches(model, 0, 9600), (std::vector<int>{ 60 }));

    delete score;
}

// ── S7c (edge) — back-to-back distinct onsets, each opening one boundary ──────
// All quarters: C-E-G [0,480), D [480,960), F [960,1440), A [1440,1920). Four
// contiguous slices; each successive onset (coincident with the prior release)
// opens exactly one boundary — coincident release+onset dedups to a single
// boundary (no zero-width slice). C, N.
TEST(Composing_SlicerTests, S7c_OnsetAtBoundary_NoOverlap)
{
    MasterScore* score = ScoreRW::readScore(u"data/nm_dense_start.mscx");
    ASSERT_TRUE(score);
    const NoteModel model = NoteModel::build(score);

    const auto slices = changePointSlices(model);
    EXPECT_EQ(spans(slices),
              (std::vector<std::pair<int, int>>{
                  { 0, 480 }, { 480, 960 }, { 960, 1440 }, { 1440, 1920 } }));
    expectCoveringPartition(slices);

    EXPECT_EQ(eligiblePitches(model, 0, 480), (std::vector<int>{ 60, 64, 67 }));
    EXPECT_EQ(eligiblePitches(model, 480, 960), (std::vector<int>{ 62 }));
    EXPECT_EQ(eligiblePitches(model, 960, 1440), (std::vector<int>{ 65 }));
    EXPECT_EQ(eligiblePitches(model, 1440, 1920), (std::vector<int>{ 69 }));

    delete score;
}

// ── S8a (eligibility) — invisible note MID-SLICE opens no boundary (pass-through)
// Eligible C4 whole [0,1920); an INVISIBLE G4 quarter [480,960) mid-bar. If it
// opened boundaries the bar would split at 480/960; layer 1 flagged it
// visible=false, so the slicer honors that and produces ONE slice [0,1920). The
// invisible note still rides in overlapping() (forwarded, not dropped). N.
TEST(Composing_SlicerTests, S8a_IneligibleMidSlice_NoBoundary_ButPassedThrough)
{
    MasterScore* score = ScoreRW::readScore(u"data/nm_slice_ineligible.mscx");
    ASSERT_TRUE(score);
    const NoteModel model = NoteModel::build(score);

    const auto slices = changePointSlices(model);
    EXPECT_EQ(spans(slices), (std::vector<std::pair<int, int>>{ { 0, 1920 } }))
        << "the invisible mid-slice note must NOT open a boundary";

    // Eligible identity is just C4; the invisible G4 is a passed-through passenger.
    EXPECT_EQ(eligiblePitches(model, 0, 1920), (std::vector<int>{ 60 }));
    EXPECT_EQ(allPitches(model, 0, 1920), (std::vector<int>{ 60, 67 }))
        << "the invisible G4 is still present in overlapping() (pass-through)";

    delete score;
}

// ── S8b (eligibility) — non-playing (cue) AND invisible notes open no boundary ─
// nm_flags: eligible C4+E4 [0,480); G4 invisible (visible=false) and cue B4
// (plays=false), all at [0,480). Exercises the plays=false and visible=false
// eligibility-skip arms. One slice; the non-eligible notes pass through. N.
TEST(Composing_SlicerTests, S8b_NonPlayingAndInvisible_NoBoundary)
{
    MasterScore* score = ScoreRW::readScore(u"data/nm_flags.mscx");
    ASSERT_TRUE(score);
    const NoteModel model = NoteModel::build(score);

    const auto slices = changePointSlices(model);
    EXPECT_EQ(spans(slices), (std::vector<std::pair<int, int>>{ { 0, 480 } }));

    EXPECT_EQ(eligiblePitches(model, 0, 480), (std::vector<int>{ 60, 64 }));
    EXPECT_EQ(allPitches(model, 0, 480), (std::vector<int>{ 60, 64, 67, 71 }))
        << "invisible G4 (67) and cue B4 (71) pass through but open no boundary";

    delete score;
}

// ── S8c (eligibility) — staff-ineligible (chord-track) note opens no boundary ─
// nm_staff_eligibility: eligible C4 whole on the normal staff [0,1920); E4 whole
// on a "Chord Track" staff (staffEligible=false). Exercises the staffEligible=false
// eligibility-skip arm. One slice; the chord-track note passes through. N.
TEST(Composing_SlicerTests, S8c_StaffIneligible_NoBoundary)
{
    MasterScore* score = ScoreRW::readScore(u"data/nm_staff_eligibility.mscx");
    ASSERT_TRUE(score);
    const NoteModel model = NoteModel::build(score);

    const auto slices = changePointSlices(model);
    EXPECT_EQ(spans(slices), (std::vector<std::pair<int, int>>{ { 0, 1920 } }));

    EXPECT_EQ(eligiblePitches(model, 0, 1920), (std::vector<int>{ 60 }));
    EXPECT_EQ(allPitches(model, 0, 1920), (std::vector<int>{ 60, 64 }))
        << "chord-track E4 (64) passes through but opens no boundary";

    delete score;
}

// ── Phase 2 — slicing under bounded context: clip the slicing span to the LOADED
// span, and re-slice on extend. Design: cowork_layer2_reslice_design.md (§2 clip,
// §3 seam-aware stability, §6 invariants). These assert the REAL invariants per §3
// of the impl instruction — NOT the naive "all old slices byte-identical."

namespace {

// Every nm_* fixture (whole-score build path) — the same set the note-model tests
// sweep. Each fixture is a whole-score model, so the §2 clip is INERT on all of
// them; that inertness is itself the degenerate byte-identity gate (CP1).
const char16_t* const kSlicerFixtures[] = {
    u"data/nm_tie_chain.mscx",        u"data/nm_long_sustain.mscx",
    u"data/nm_grace.mscx",            u"data/nm_unison.mscx",
    u"data/nm_flags.mscx",            u"data/nm_two_staff.mscx",
    u"data/nm_staff_eligibility.mscx", u"data/nm_solid_theory.mscx",
    u"data/nm_dense_start.mscx",      u"data/nm_slice_passing.mscx",
    u"data/nm_slice_held_melody.mscx", u"data/nm_slice_release.mscx",
    u"data/nm_slice_rest.mscx",       u"data/nm_slice_ineligible.mscx",
};

// The min eligible onset / max eligible release over a model's notes — the span
// the UNCLIPPED tiling would cover (`[firstEligibleOnset, lastEligibleRelease)`).
std::pair<int, int> eligibleSpan(const NoteModel& m)
{
    int lo = INT_MAX, hi = INT_MIN;
    for (const NEvent& e : m.notes()) {
        if (e.plays && e.visible && e.staffEligible) {
            lo = std::min(lo, e.onset);
            hi = std::max(hi, e.release);
        }
    }
    return { lo, hi };
}

// The [start,end) slice that covers `tick` (start <= tick < end), or {-1,-1}.
std::pair<int, int> sliceCovering(const std::vector<Slice>& slices, int tick)
{
    for (const Slice& s : slices) {
        if (s.start <= tick && tick < s.end) {
            return { s.start, s.end };
        }
    }
    return { -1, -1 };
}

// Whether `tick` is a slice boundary (a slice start, or the final slice end).
bool isBoundary(const std::vector<Slice>& slices, int tick)
{
    if (slices.empty()) {
        return false;
    }
    if (slices.back().end == tick) {
        return true;
    }
    for (const Slice& s : slices) {
        if (s.start == tick) {
            return true;
        }
    }
    return false;
}

} // namespace

// ── CP1 (degenerate byte-identity) — the §2 clip is INERT on every whole-score
// model. For each fixture, the slices from build(score) equal the slices from an
// explicitly-everything span build, AND the tiling still spans exactly
// [firstEligibleOnset, lastEligibleRelease) — the clip moved no endpoint inward.
// (The exact whole-score span lists are pinned by S1–S8c; this proves the clip
// itself changes nothing, i.e. loadedStart <= front and loadedEnd >= back hold.)
TEST(Composing_SlicerTests, CP1_Clip_InertOnWholeScore)
{
    for (const char16_t* path : kSlicerFixtures) {
        MasterScore* score = ScoreRW::readScore(path);
        ASSERT_TRUE(score) << "missing fixture";

        const NoteModel whole = NoteModel::build(score);
        // A span that cannot clip anything: it strictly contains every note.
        const NoteModel everything = NoteModel::build(score, INT_MIN / 2, INT_MAX / 2);

        const auto sWhole = changePointSlices(whole);
        const auto sEvery = changePointSlices(everything);
        EXPECT_EQ(spans(sWhole), spans(sEvery))
            << "clip not inert: whole-score slices differ from an everything-span build";
        ASSERT_FALSE(sWhole.empty()) << "fixture has eligible notes ⇒ ≥1 slice";

        const auto [lo, hi] = eligibleSpan(whole);
        EXPECT_EQ(sWhole.front().start, lo)
            << "clip moved the leading endpoint inward on a whole-score model";
        EXPECT_EQ(sWhole.back().end, hi)
            << "clip moved the trailing endpoint inward on a whole-score model";
        expectCoveringPartition(sWhole);

        delete score;
    }
}

// ── CP2 (clip correctness — sustained-IN) — a note onsetting BEFORE loadedStart
// but sustaining into the loaded span: the first slice starts at loadedStart, the
// note is IN it, and NO slice exists before loadedStart. (C4 [0,9600); select
// [4800, scoreEnd) so C4 sustains in.)
TEST(Composing_SlicerTests, CP2_SustainedIn_FirstSliceStartsAtLoadedStart)
{
    MasterScore* score = ScoreRW::readScore(u"data/nm_long_sustain.mscx");
    ASSERT_TRUE(score);
    const int e = NoteModel::build(score).loadedEnd();  // scoreEnd (>= 9600)

    const NoteModel model = NoteModel::build(score, 4800, e);
    ASSERT_EQ(model.loadedStart(), 4800);

    const auto slices = changePointSlices(model);
    ASSERT_FALSE(slices.empty());
    expectCoveringPartition(slices);
    EXPECT_EQ(slices.front().start, 4800)
        << "the first slice must start at loadedStart, not at the sustained-in onset (0)";
    for (const Slice& s : slices) {
        EXPECT_GE(s.start, 4800) << "no slice may exist before loadedStart";
    }
    // The sustained-in C4 is present in the first (edge) slice.
    EXPECT_EQ(eligiblePitches(model, slices.front().start, slices.front().end),
              (std::vector<int>{ 60 }));

    delete score;
}

// ── CP3 (clip correctness — sustained-OUT) — a note releasing AFTER loadedEnd:
// the last slice ENDS at loadedEnd, the note is IN it, and NO slice exists after
// loadedEnd. (C4 [0,9600); select [0,4800) so C4 sustains out past 4800.)
TEST(Composing_SlicerTests, CP3_SustainedOut_LastSliceEndsAtLoadedEnd)
{
    MasterScore* score = ScoreRW::readScore(u"data/nm_long_sustain.mscx");
    ASSERT_TRUE(score);

    const NoteModel model = NoteModel::build(score, 0, 4800);
    ASSERT_EQ(model.loadedEnd(), 4800);

    const auto slices = changePointSlices(model);
    ASSERT_FALSE(slices.empty());
    expectCoveringPartition(slices);
    EXPECT_EQ(slices.back().end, 4800)
        << "the last slice must end at loadedEnd, not at the sustained-out release (9600)";
    for (const Slice& s : slices) {
        EXPECT_LE(s.end, 4800) << "no slice may exist after loadedEnd";
    }
    EXPECT_EQ(eligiblePitches(model, slices.back().start, slices.back().end),
              (std::vector<int>{ 60 }));

    delete score;
}

// ── CP4 (clip + interior preservation) — a richer partial span. nm_slice_passing:
// C-E-G held [0,1440), passing D [480,960). Select [600,1440): D sustains in
// (onset 480 < 600). The clip drops the pre-600 boundaries (0, the D-onset 480)
// and starts the edge slice at loadedStart=600, while the INTERIOR real change-
// point at 960 (D releases) is preserved.
TEST(Composing_SlicerTests, CP4_PartialSpan_ClipsEdge_PreservesInterior)
{
    MasterScore* score = ScoreRW::readScore(u"data/nm_slice_passing.mscx");
    ASSERT_TRUE(score);

    const NoteModel model = NoteModel::build(score, 600, 1440);
    const auto slices = changePointSlices(model);
    EXPECT_EQ(spans(slices),
              (std::vector<std::pair<int, int>>{ { 600, 960 }, { 960, 1440 } }));
    expectCoveringPartition(slices);
    EXPECT_TRUE(isBoundary(slices, 960)) << "interior real change-point at 960 preserved";

    // Edge slice [600,960): C-E-G + the sustained-in D. Interior [960,1440): C-E-G.
    EXPECT_EQ(eligiblePitches(model, 600, 960), (std::vector<int>{ 60, 62, 64, 67 }));
    EXPECT_EQ(eligiblePitches(model, 960, 1440), (std::vector<int>{ 60, 64, 67 }));

    delete score;
}

// ── CP5 (seam-aware stability on extend — ARTIFICIAL seam grows) — the §3
// property. The clip boundary at loadedStart=600 is ARTIFICIAL (D sounds on both
// sides of it). Extending earlier dissolves it: the edge slice GROWS outward
// (it is NOT byte-identical — the naive "all old slices identical" assertion is
// wrong, §3), while the interior real change-point (960) and the content over the
// original span are unchanged.
TEST(Composing_SlicerTests, CP5_Extend_ArtificialSeam_EdgeSliceGrows)
{
    MasterScore* score = ScoreRW::readScore(u"data/nm_slice_passing.mscx");
    ASSERT_TRUE(score);

    NoteModel model = NoteModel::build(score, 600, 1440);
    const auto before = changePointSlices(model);
    EXPECT_EQ(spans(before),
              (std::vector<std::pair<int, int>>{ { 600, 960 }, { 960, 1440 } }));
    // Capture the content over the original span BEFORE extending.
    const auto edgeBefore   = eligiblePitches(model, 600, 960);
    const auto interiorBefore = eligiblePitches(model, 960, 1440);
    const auto coverBefore  = sliceCovering(before, 600);  // {600,960}

    // Extend earlier to the score start (loadedStart 600 -> 0) and re-slice.
    model.extend(NoteModel::Direction::Earlier, 600);
    ASSERT_EQ(model.loadedStart(), 0);
    const auto after = changePointSlices(model);
    EXPECT_EQ(spans(after),
              (std::vector<std::pair<int, int>>{ { 0, 480 }, { 480, 960 }, { 960, 1440 } }));

    // (a) The edge slice GREW: the slice covering tick 600 now starts EARLIER than
    //     it did (480 < 600) — it is NOT byte-identical (the seam-aware property).
    const auto coverAfter = sliceCovering(after, 600);  // {480,960}
    EXPECT_LT(coverAfter.first, coverBefore.first)
        << "the artificial-seam edge slice must extend outward, not stay byte-identical";
    EXPECT_EQ(coverAfter.second, coverBefore.second) << "the edge slice's far end is unchanged";

    // (b) Interior real change-point at 960 identical before/after.
    EXPECT_TRUE(isBoundary(before, 960));
    EXPECT_TRUE(isBoundary(after, 960));

    // (c) Content over the ORIGINAL span [600,1440) unchanged (re-inference sees the
    //     same notes there; extend only adds context to the leading edge).
    EXPECT_EQ(eligiblePitches(model, 600, 960), edgeBefore);
    EXPECT_EQ(eligiblePitches(model, 960, 1440), interiorBefore);

    delete score;
}

// ── CP6 (extend — REAL seam is additive) — the complementary case. nm_dense_start:
// C-E-G [0,480), D [480,960), F [960,1440), A [1440,1920). Select [960,1920): the
// clip boundary at 960 coincides with a REAL change-point (F's onset / the prior
// release), so it is NOT artificial. Extending earlier PREPENDS a new slice and
// leaves the old slices byte-identical — additive, not edge-growth. (This is the
// special case where old slices ARE preserved; CP5 is the general one where they
// are not — do not conflate them.)
TEST(Composing_SlicerTests, CP6_Extend_RealSeam_AdditivePrepend)
{
    MasterScore* score = ScoreRW::readScore(u"data/nm_dense_start.mscx");
    ASSERT_TRUE(score);

    NoteModel model = NoteModel::build(score, 960, 1920);
    const auto before = changePointSlices(model);
    EXPECT_EQ(spans(before),
              (std::vector<std::pair<int, int>>{ { 960, 1440 }, { 1440, 1920 } }));

    model.extend(NoteModel::Direction::Earlier, 480);  // loadedStart 960 -> 480
    ASSERT_EQ(model.loadedStart(), 480);
    const auto after = changePointSlices(model);
    EXPECT_EQ(spans(after),
              (std::vector<std::pair<int, int>>{ { 480, 960 }, { 960, 1440 }, { 1440, 1920 } }));

    // The two old slices survive byte-identically (real seam ⇒ additive prepend).
    EXPECT_EQ(after[1].start, before[0].start);
    EXPECT_EQ(after[1].end, before[0].end);
    EXPECT_EQ(after[2].start, before[1].start);
    EXPECT_EQ(after[2].end, before[1].end);

    delete score;
}

// ── CP7 (re-slice equivalence — the correctness-critical invariant, §3/§6.3) —
// re-slicing after an extend equals slicing a model built directly over the
// enlarged span. For each fixture, an interior selection extended to [x0,x1) gives
// the SAME slices as build(score, x0, x1). Holds by construction (the slicer is a
// pure function of (notes, loaded span), and EXT3 proves both agree on those), so
// this is a genuine regression guard on that purity, swept over every shape.
TEST(Composing_SlicerTests, CP7_ReSliceEquivalence_ExtendEqualsDirectBuild)
{
    for (const char16_t* path : kSlicerFixtures) {
        MasterScore* score = ScoreRW::readScore(path);
        ASSERT_TRUE(score) << "missing fixture";

        const NoteModel full = NoteModel::build(score);
        const int s = full.loadedStart();
        const int e = full.loadedEnd();
        const int span = e - s;
        if (span <= 8) { delete score; continue; }  // too short to nest an interior span

        const int x0 = s + span / 8;
        const int a0 = s + span * 3 / 8;
        const int a1 = e - span * 3 / 8;
        const int x1 = e - span / 8;
        ASSERT_LT(a0, a1);
        ASSERT_LT(x0, a0);
        ASSERT_LT(a1, x1);

        const NoteModel direct = NoteModel::build(score, x0, x1);

        NoteModel sel = NoteModel::build(score, a0, a1);
        sel.extend(NoteModel::Direction::Earlier, a0 - x0);
        sel.extend(NoteModel::Direction::Later, x1 - a1);
        ASSERT_EQ(sel.loadedStart(), x0);
        ASSERT_EQ(sel.loadedEnd(), x1);

        EXPECT_EQ(spans(changePointSlices(sel)), spans(changePointSlices(direct)))
            << "re-slice after extend != slice over the directly-built enlarged span: " << path;

        delete score;
    }
}
