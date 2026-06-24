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

// Layer-1 NOTE MODEL — score-level tests (T1–T8 of the audit §6 spec).
//
// These assert the CORRECT note model vs the score: tied groups merged into one
// span (no double-onset / repetition inflation), sustains of any length found by
// overlap (no horizon), and grace / cross-staff / multi-voice-unison /
// invisible-non-playing / staff-ineligible notes KEPT and FLAGGED (never
// dropped). North star: faithful to the score.

#include <gtest/gtest.h>

#include <chrono>
#include <climits>
#include <cstdint>
#include <functional>
#include <random>
#include <vector>

#include "engraving/dom/chord.h"
#include "engraving/dom/chordrest.h"
#include "engraving/dom/masterscore.h"
#include "engraving/dom/measure.h"
#include "engraving/dom/note.h"
#include "engraving/dom/score.h"
#include "engraving/dom/segment.h"
#include "engraving/types/constants.h"
#include "engraving/tests/utils/scorerw.h"

#include "composing/analysis/notemodel/note_model.h"
#include "composing/analysis/engravingbridge/regiontonecollector.h"

using mu::engraving::MasterScore;
using mu::engraving::ScoreRW;
// Alias to avoid the name clash with mu::engraving::NoteEvent (a playback event,
// pulled in via the DOM headers) inside `using namespace mu::engraving` scopes.
using NEvent = mu::composing::analysis::notemodel::NoteEvent;
using mu::composing::analysis::notemodel::NoteModel;
using mu::composing::analysis::notemodel::NoteQueryIndex;
namespace ebr = mu::composing::analysis::engravingbridge;

namespace {

int countNotes(const NoteModel& m, const std::function<bool(const NEvent&)>& pred)
{
    int n = 0;
    for (const NEvent& e : m.notes()) {
        if (pred(e)) {
            ++n;
        }
    }
    return n;
}

const NEvent* findNote(const NoteModel& m, const std::function<bool(const NEvent&)>& pred)
{
    for (const NEvent& e : m.notes()) {
        if (pred(e)) {
            return &e;
        }
    }
    return nullptr;
}

} // namespace

// ── T1 — Tie across a barline (the critical case) ────────────────────────────
// Real fixture: solid theory.musicxml, voice 2, A4 (ppitch 69), a half note tied
// across the barline into the next half note. The model must produce ONE merged
// A4 span (firstTiedNote.onset -> lastTiedNote.release), no false intermediate
// onset, no repetition inflation. We derive the expected span from the DOM's own
// tie API (robust to any pickup/measure numbering), then assert the model agrees.
TEST(Composing_NoteModelTests, T1_TieAcrossBarline_OneMergedSpan)
{
    using namespace mu::engraving;
    MasterScore* score = ScoreRW::readScore(u"data/nm_solid_theory.mscx");
    ASSERT_TRUE(score);

    // Locate a voice-2 (track voice 1) A4 tie-START note in the DOM.
    const Note* tieStart = nullptr;
    for (const Measure* m = score->firstMeasure(); m && !tieStart; m = m->nextMeasure()) {
        for (const Segment* s = m->first(SegmentType::ChordRest); s && !tieStart;
             s = s->next(SegmentType::ChordRest)) {
            for (size_t si = 0; si < score->nstaves() && !tieStart; ++si) {
                const ChordRest* cr = s->cr(static_cast<track_idx_t>(si) * VOICES + 1);
                if (!cr || !cr->isChord()) {
                    continue;
                }
                for (const Note* n : toChord(cr)->notes()) {
                    if (n->ppitch() == 69 && n->tieFor() && !n->tieBack()) {
                        tieStart = n;
                        break;
                    }
                }
            }
        }
    }
    ASSERT_TRUE(tieStart) << "expected a voice-2 A4 tie-start note in solid theory.musicxml";

    const int domOnset   = tieStart->chord()->tick().ticks();
    const int domRelease = domOnset + tieStart->playTicksFraction().ticks();
    EXPECT_GT(domRelease - domOnset, tieStart->chord()->actualTicks().ticks())
        << "the tied span must exceed the first note's own length";

    const NoteModel model = NoteModel::build(score);

    // Exactly one merged A4/voice-2 event, spanning the full tied length.
    EXPECT_EQ(countNotes(model, [&](const NEvent& e) {
        return e.pitch == 69 && e.voice == 1 && e.onset == domOnset
               && e.release == domRelease && e.duration == domRelease - domOnset;
    }), 1);

    // No false onset strictly inside the merged span (the de-inflation).
    EXPECT_EQ(countNotes(model, [&](const NEvent& e) {
        return e.pitch == 69 && e.voice == 1 && e.onset > domOnset && e.onset < domRelease;
    }), 0) << "tie continuation must NOT produce a second onset inside the span";

    delete score;
}

// ── T2 — Tie chain of ≥3 ─────────────────────────────────────────────────────
// Three tied C4 quarters then a D4 quarter -> ONE C4 span [0,1440) and one D4
// span [1440,1920); exactly two notes, two onsets.
TEST(Composing_NoteModelTests, T2_TieChainOfThree_OneSpan)
{
    MasterScore* score = ScoreRW::readScore(u"data/nm_tie_chain.mscx");
    ASSERT_TRUE(score);

    const NoteModel model = NoteModel::build(score);

    // Exactly one C4 span and one D4 span (no grace, no extras).
    EXPECT_EQ(countNotes(model, [](const NEvent& e) {
        return e.pitch == 60 && e.onset == 0 && e.release == 1440 && e.duration == 1440;
    }), 1);
    EXPECT_EQ(countNotes(model, [](const NEvent& e) {
        return e.pitch == 62 && e.onset == 1440 && e.release == 1920;
    }), 1);
    // No false onsets inside the C4 chain (ticks 480, 960).
    EXPECT_EQ(countNotes(model, [](const NEvent& e) {
        return e.pitch == 60 && e.onset > 0 && e.onset < 1440;
    }), 0);
    // The whole non-grace model is exactly two notes.
    EXPECT_EQ(countNotes(model, [](const NEvent& e) { return !e.isGrace; }), 2);

    // A region query over [0,1440) sees C4 as a single held note.
    EXPECT_EQ(static_cast<int>(model.overlapping(0, 1440).size()), 1);

    delete score;
}

// ── T3 — Sustain longer than the 4-whole-note cap ────────────────────────────
// A C4 held 5 wholes (onset 0, release 9600). A query region [7680,9600), which
// begins >4 wholes after onset, must STILL find the note (overlap, no horizon).
TEST(Composing_NoteModelTests, T3_SustainBeyondCap_FoundByOverlap)
{
    MasterScore* score = ScoreRW::readScore(u"data/nm_long_sustain.mscx");
    ASSERT_TRUE(score);

    const NoteModel model = NoteModel::build(score);

    // Exactly one merged C4 spanning the full five wholes.
    EXPECT_EQ(countNotes(model, [](const NEvent& e) {
        return e.pitch == 60 && e.onset == 0 && e.release == 9600 && e.duration == 9600;
    }), 1);

    // The overlap query past the old 7680-tick cap returns the sustained note.
    const auto ov = model.overlapping(7680, 9600);
    ASSERT_EQ(static_cast<int>(ov.size()), 1);
    EXPECT_EQ(ov.front()->pitch, 60);
    EXPECT_EQ(ov.front()->onset, 0);
    EXPECT_EQ(ov.front()->release, 9600);

    delete score;
}

// ── T4 — Grace note ──────────────────────────────────────────────────────────
// An acciaccatura G5 before a C4-E4-G4 chord. The grace is KEPT, flagged
// isGrace=true, attached to the main chord's tick (onset 0); main notes normal.
TEST(Composing_NoteModelTests, T4_GraceKeptAndFlagged)
{
    MasterScore* score = ScoreRW::readScore(u"data/nm_grace.mscx");
    ASSERT_TRUE(score);

    const NoteModel model = NoteModel::build(score);

    const NEvent* grace = findNote(model, [](const NEvent& e) {
        return e.pitch == 79 && e.isGrace;  // G5
    });
    ASSERT_TRUE(grace) << "grace G5 must be collected and flagged isGrace";
    EXPECT_EQ(grace->onset, 0) << "grace attaches to its main chord's tick";

    // Main chord notes present, not grace, onset 0.
    for (int p : { 60, 64, 67 }) {  // C4, E4, G4
        EXPECT_EQ(countNotes(model, [&](const NEvent& e) {
            return e.pitch == p && !e.isGrace && e.onset == 0;
        }), 1) << "main chord pitch " << p << " missing";
    }

    delete score;
}

// ── T5 — Cross-staff (owning-staff keying) ───────────────────────────────────
// 2-staff piano: C5 on staff 1, C3 on staff 2. The model keys each on its
// owning staff index (0 / 1), not visual placement.
TEST(Composing_NoteModelTests, T5_CrossStaff_KeysOnOwningStaff)
{
    MasterScore* score = ScoreRW::readScore(u"data/nm_two_staff.mscx");
    ASSERT_TRUE(score);

    const NoteModel model = NoteModel::build(score);

    EXPECT_EQ(countNotes(model, [](const NEvent& e) {
        return e.pitch == 72 && e.staff == 0;  // C5 on staff 1
    }), 1);
    EXPECT_EQ(countNotes(model, [](const NEvent& e) {
        return e.pitch == 48 && e.staff == 1;  // C3 on staff 2
    }), 1);

    delete score;
}

// ── T6 — Multi-voice unison ──────────────────────────────────────────────────
// Voice 1 and voice 2 both sound E4 at tick 0 (half + quarter). The model keeps
// BOTH, with voice identity and their own releases (voice count is derived, not
// a loss).
TEST(Composing_NoteModelTests, T6_MultiVoiceUnison_BothRetained)
{
    MasterScore* score = ScoreRW::readScore(u"data/nm_unison.mscx");
    ASSERT_TRUE(score);

    const NoteModel model = NoteModel::build(score);

    EXPECT_EQ(countNotes(model, [](const NEvent& e) {
        return e.pitch == 64 && e.voice == 0 && e.onset == 0 && e.release == 960;  // half
    }), 1);
    EXPECT_EQ(countNotes(model, [](const NEvent& e) {
        return e.pitch == 64 && e.voice == 1 && e.onset == 0 && e.release == 480;  // quarter
    }), 1);
    // Two distinct E4 notes, not one collapsed accumulator.
    EXPECT_EQ(countNotes(model, [](const NEvent& e) { return e.pitch == 64; }), 2);

    delete score;
}

// ── T7 — Invisible / non-playing notes ───────────────────────────────────────
// Chord C4 + E4 + G4(invisible) and a cue B4 (imported plays=false). All KEPT;
// G4 flagged visible=false, B4 flagged plays=false; the rest true.
TEST(Composing_NoteModelTests, T7_InvisibleAndNonPlaying_KeptAndFlagged)
{
    MasterScore* score = ScoreRW::readScore(u"data/nm_flags.mscx");
    ASSERT_TRUE(score);

    const NoteModel model = NoteModel::build(score);

    const NEvent* c4 = findNote(model, [](const NEvent& e) { return e.pitch == 60; });
    const NEvent* e4 = findNote(model, [](const NEvent& e) { return e.pitch == 64; });
    const NEvent* g4 = findNote(model, [](const NEvent& e) { return e.pitch == 67; });
    const NEvent* b4 = findNote(model, [](const NEvent& e) { return e.pitch == 71; });

    ASSERT_TRUE(c4) << "normal note C4 kept";
    ASSERT_TRUE(e4) << "normal note E4 kept";
    ASSERT_TRUE(g4) << "invisible note G4 kept (not dropped)";
    ASSERT_TRUE(b4) << "non-playing cue note B4 kept (not dropped)";

    EXPECT_TRUE(c4->visible);
    EXPECT_TRUE(c4->plays);
    EXPECT_TRUE(e4->visible);
    EXPECT_FALSE(g4->visible) << "G4 (print-object=no) must be flagged visible=false";
    EXPECT_FALSE(b4->plays) << "cue B4 must be flagged plays=false";

    delete score;
}

// ── T8 — Staff eligibility (chord-track) ─────────────────────────────────────
// A normal staff and a "Chord Track" staff. Both staves' notes are COLLECTED;
// the chord-track notes are flagged staffEligible=false, the normal ones true.
// (Hidden [!show()] and percussion [useDrumset()] staves traverse the identical
// staffIsEligible predicate — verified at source.)
TEST(Composing_NoteModelTests, T8_StaffIneligible_KeptAndFlagged)
{
    MasterScore* score = ScoreRW::readScore(u"data/nm_staff_eligibility.mscx");
    ASSERT_TRUE(score);

    const NoteModel model = NoteModel::build(score);

    const NEvent* normal = findNote(model, [](const NEvent& e) { return e.pitch == 60; });
    const NEvent* chordTrack = findNote(model, [](const NEvent& e) { return e.pitch == 64; });

    ASSERT_TRUE(normal) << "normal-staff note kept";
    ASSERT_TRUE(chordTrack) << "chord-track-staff note kept (not silently omitted)";

    EXPECT_TRUE(normal->staffEligible) << "normal staff is eligible";
    EXPECT_FALSE(chordTrack->staffEligible) << "Chord Track staff must be flagged ineligible";

    delete score;
}

// ── View branch-coverage tests (T9–T12) ──────────────────────────────────────
// Cover the derived-view branches not reached by T1–T8 (which only build the
// model). Test-only; no production change.

// T9 — weightedPcView empty/invalid region: end <= start returns {} (the early
// guard). Also exercises onsetIn=[) edge implicitly.
TEST(Composing_NoteModelTests, T9_WeightedPcView_EmptyRegionReturnsEmpty)
{
    MasterScore* score = ScoreRW::readScore(u"data/nm_tie_chain.mscx");
    ASSERT_TRUE(score);
    const NoteModel model = NoteModel::build(score);

    EXPECT_TRUE(ebr::weightedPcView(model, 480, 480, {}).empty());   // end == start
    EXPECT_TRUE(ebr::weightedPcView(model, 960, 480, {}).empty());   // end <  start

    delete score;
}

// T10 — weightedPcView dense-start look-ahead branch: with
// excludeLookAheadOnDenseStart=true and >=3 PCs sounding at the region start, the
// post-start onsets are dropped; with it false they are included.
TEST(Composing_NoteModelTests, T10_WeightedPcView_DenseStartLookAheadExclusion)
{
    MasterScore* score = ScoreRW::readScore(u"data/nm_dense_start.mscx");
    ASSERT_TRUE(score);
    const NoteModel model = NoteModel::build(score);

    // Region [0,1920): C-E-G chord at 0 (3 PCs), then D(480) F(960) A(1440).
    const auto full = ebr::weightedPcView(model, 0, 1920, {}, -1, /*excludeLookAhead=*/false);
    const auto dense = ebr::weightedPcView(model, 0, 1920, {}, -1, /*excludeLookAhead=*/true);

    // Without exclusion: all six pitch classes (C E G D F A).
    EXPECT_EQ(static_cast<int>(full.size()), 6);
    // With exclusion (>=3 PCs at start): only the start chord's C, E, G.
    EXPECT_EQ(static_cast<int>(dense.size()), 3);
    for (const auto& t : dense) {
        const int pc = t.pitch % 12;
        EXPECT_TRUE(pc == 0 || pc == 4 || pc == 7) << "unexpected pc " << pc << " survived exclusion";
    }

    delete score;
}

// T11 — the Score-based collectSoundingAt convenience wrapper (builds a model and
// delegates to soundingAt).
TEST(Composing_NoteModelTests, T11_CollectSoundingAt_ScoreWrapper)
{
    using namespace mu::engraving;
    MasterScore* score = ScoreRW::readScore(u"data/nm_dense_start.mscx");
    ASSERT_TRUE(score);

    const Segment* seg = score->firstMeasure()->first(SegmentType::ChordRest);
    ASSERT_TRUE(seg);

    std::vector<ebr::SoundingNote> out;
    ebr::collectSoundingAt(score, seg, {}, out);

    // The start chord C-E-G sounds at the first segment.
    ASSERT_EQ(static_cast<int>(out.size()), 3);
    EXPECT_EQ(out.front().ppitch, 60) << "lowest collected note is C4 (anchor order)";

    delete score;
}

// T12 — soundingAt at a tick INSIDE a long sustain: the note (onset < tick) is
// returned via the sustained partition (exercises the descending-onset ordering
// path), with no horizon.
TEST(Composing_NoteModelTests, T12_SoundingAt_SustainedNoteMidSpan)
{
    MasterScore* score = ScoreRW::readScore(u"data/nm_long_sustain.mscx");
    ASSERT_TRUE(score);
    const NoteModel model = NoteModel::build(score);

    std::vector<ebr::SoundingNote> out;
    ebr::soundingAt(model, 4800, {}, out);   // mid the [0,9600) C4 sustain

    ASSERT_EQ(static_cast<int>(out.size()), 1);
    EXPECT_EQ(out.front().ppitch, 60);

    delete score;
}

// T13 — dense-start look-ahead, SUSTAIN-into-start path: a region whose start has
// a note sustaining in (onset < start). Exercises the first (sustain-counting)
// loop body of the excludeLookAhead block. (Here only one PC sustains, so the
// >=3 decision is false — but the loop body still runs.)
TEST(Composing_NoteModelTests, T13_WeightedPcView_DenseStartSustainCount)
{
    MasterScore* score = ScoreRW::readScore(u"data/nm_long_sustain.mscx");
    ASSERT_TRUE(score);
    const NoteModel model = NoteModel::build(score);

    // Region begins mid the [0,9600) C4 sustain, with look-ahead exclusion on.
    const auto tones = ebr::weightedPcView(model, 1920, 3840, {}, -1, /*excludeLookAhead=*/true);
    ASSERT_EQ(static_cast<int>(tones.size()), 1);
    EXPECT_EQ(tones.front().pitch % 12, 0);   // C4 sustained into the region

    delete score;
}

// T14 — bass-floor fallback: when no pitch class reaches
// bassPassingToneMinWeightFraction of the total (here forced via a high fraction
// so every PC is below it), the bass falls back to the lowest pitch among any
// weighted PC. Reachable only with prefs whose fraction exceeds 1/(#distinct PCs)
// — the production default (0.05) never triggers it; covered with a test pref.
TEST(Composing_NoteModelTests, T14_WeightedPcView_BassFloorFallback)
{
    using mu::composing::analysis::ChordAnalyzerPreferences;
    using mu::composing::analysis::kDefaultChordAnalyzerPreferences;
    MasterScore* score = ScoreRW::readScore(u"data/nm_dense_start.mscx");
    ASSERT_TRUE(score);
    const NoteModel model = NoteModel::build(score);

    ChordAnalyzerPreferences prefs = kDefaultChordAnalyzerPreferences;
    prefs.bassPassingToneMinWeightFraction = 0.9;  // no single PC reaches 90% of total

    const auto tones = ebr::weightedPcView(model, 0, 1920, {}, -1, /*excludeLookAhead=*/false, prefs);
    ASSERT_FALSE(tones.empty());
    int bassCount = 0, bassPitch = 1 << 30;
    for (const auto& t : tones) {
        if (t.isBass) { ++bassCount; bassPitch = t.pitch; }
    }
    EXPECT_EQ(bassCount, 1) << "fallback still designates exactly one bass";
    // Fallback picks the lowest pitch among weighted PCs (C4 = 60 here).
    EXPECT_EQ(bassPitch, 60);

    delete score;
}

// ── Layer-3/A — indexed query == linear scan (the load-bearing correctness proof)
//
// Increment A replaced the O(N) head-scan implementation of overlapping()/onsetIn()
// with an indexed O(log N + result) one. These tests assert the indexed result is
// element-for-element IDENTICAL (including order) to the original linear scan, on
// every nm_* fixture, over a battery of random and edge ranges. The reference
// oracles below are byte-copies of the pre-A linear implementations.

namespace {

// The pre-A overlapping(): linear head scan, onset-sorted, break at onset >= t1.
std::vector<const NEvent*> linearOverlapping(const NoteModel& m, int t0, int t1)
{
    std::vector<const NEvent*> out;
    if (t1 <= t0) {
        return out;
    }
    for (const NEvent& e : m.notes()) {
        if (e.onset >= t1) {
            break;
        }
        if (e.release > t0) {
            out.push_back(&e);
        }
    }
    return out;
}

// The pre-A onsetIn(): linear head scan, onset-sorted, break at onset >= t1.
std::vector<const NEvent*> linearOnsetIn(const NoteModel& m, int t0, int t1)
{
    std::vector<const NEvent*> out;
    if (t1 <= t0) {
        return out;
    }
    for (const NEvent& e : m.notes()) {
        if (e.onset >= t1) {
            break;
        }
        if (e.onset >= t0) {
            out.push_back(&e);
        }
    }
    return out;
}

// Assert indexed == linear (identical pointers, identical order) for one range.
void expectQueriesMatch(const NoteModel& m, int t0, int t1)
{
    EXPECT_EQ(m.overlapping(t0, t1), linearOverlapping(m, t0, t1))
        << "overlapping(" << t0 << "," << t1 << ") diverged from the linear oracle";
    EXPECT_EQ(m.onsetIn(t0, t1), linearOnsetIn(m, t0, t1))
        << "onsetIn(" << t0 << "," << t1 << ") diverged from the linear oracle";
}

// Every nm_* fixture (build-from-Score path). Each exercises a distinct shape:
// ties, long sustains, grace, multi-staff/voice, flags, eligibility, dense onsets.
const char16_t* const kAllNmFixtures[] = {
    u"data/nm_tie_chain.mscx",        u"data/nm_long_sustain.mscx",
    u"data/nm_grace.mscx",            u"data/nm_unison.mscx",
    u"data/nm_flags.mscx",            u"data/nm_two_staff.mscx",
    u"data/nm_staff_eligibility.mscx", u"data/nm_solid_theory.mscx",
    u"data/nm_dense_start.mscx",      u"data/nm_slice_passing.mscx",
    u"data/nm_slice_held_melody.mscx", u"data/nm_slice_release.mscx",
    u"data/nm_slice_rest.mscx",       u"data/nm_slice_ineligible.mscx",
};

} // namespace

// IDX1 — random + edge ranges on every fixture: indexed == linear, order-exact.
TEST(Composing_NoteModelTests, IDX1_IndexedEqualsLinear_AllFixtures)
{
    std::mt19937 rng(0xC0FFEEu);  // fixed seed ⇒ deterministic

    for (const char16_t* path : kAllNmFixtures) {
        MasterScore* score = ScoreRW::readScore(path);
        ASSERT_TRUE(score) << "missing fixture";
        const NoteModel model = NoteModel::build(score);

        // Tick domain: from before the first onset to past the last release.
        int minOnset = INT_MAX, maxRelease = INT_MIN;
        std::vector<int> boundaries;
        for (const NEvent& e : model.notes()) {
            minOnset = std::min(minOnset, e.onset);
            maxRelease = std::max(maxRelease, e.release);
            boundaries.push_back(e.onset);
            boundaries.push_back(e.release);
        }
        ASSERT_FALSE(model.notes().empty()) << "fixture has no notes";
        const int lo = minOnset - 480;
        const int hi = maxRelease + 480;

        // (a) Exhaustive boundary pairs (exact onsets/releases — the edge ticks).
        for (int a : boundaries) {
            for (int b : boundaries) {
                expectQueriesMatch(model, a, b);          // includes a>=b (empty) cases
            }
        }
        // (b) Targeted edges: empty, full span, before-first, after-last, zero-width.
        expectQueriesMatch(model, 100, 100);              // t1 == t0  (empty)
        expectQueriesMatch(model, 200, 100);              // t1 <  t0  (empty)
        expectQueriesMatch(model, lo, hi);                // full span
        expectQueriesMatch(model, lo, minOnset);          // entirely before first onset
        expectQueriesMatch(model, maxRelease, hi);        // entirely after last release
        expectQueriesMatch(model, minOnset, minOnset + 1);// just the first tick

        // (c) Many random ranges across the domain (incl. mid-note boundaries).
        std::uniform_int_distribution<int> dist(lo, hi);
        for (int k = 0; k < 400; ++k) {
            int a = dist(rng), b = dist(rng);
            expectQueriesMatch(model, a, b);              // both orders of a,b
            expectQueriesMatch(model, b, a);
        }

        delete score;
    }
}

// IDX2 — NoteQueryIndex direct unit tests (covers the index in isolation,
// including the N==0 build path the NoteModel guards never reach).
TEST(Composing_NoteModelTests, IDX2_NoteQueryIndex_EmptyAndSingleton)
{
    // Empty: build({}) — onsetLowerBound clamps to 0, overlapIndices yields nothing.
    {
        NoteQueryIndex idx;
        idx.build({});
        EXPECT_EQ(idx.onsetLowerBound(0), 0);
        EXPECT_EQ(idx.onsetLowerBound(100), 0);
        std::vector<int> out;
        idx.overlapIndices(/*qHi=*/0, /*t0=*/0, out);     // qHi<=0 guard
        EXPECT_TRUE(out.empty());
        idx.overlapIndices(/*qHi=*/5, /*t0=*/0, out);     // m_segSize==0 guard
        EXPECT_TRUE(out.empty());
    }
    // Singleton: one note [onset=10, release=20]. segSize==1 ⇒ root is a leaf.
    {
        std::vector<NEvent> notes(1);
        notes[0].onset = 10;
        notes[0].release = 20;
        NoteQueryIndex idx;
        idx.build(notes);
        EXPECT_EQ(idx.onsetLowerBound(10), 0);
        EXPECT_EQ(idx.onsetLowerBound(11), 1);
        std::vector<int> out;
        idx.overlapIndices(idx.onsetLowerBound(100), /*t0=*/15, out);  // release 20 > 15
        ASSERT_EQ(out.size(), 1u);
        EXPECT_EQ(out[0], 0);
        out.clear();
        idx.overlapIndices(idx.onsetLowerBound(100), /*t0=*/20, out);  // release 20 !> 20: pruned
        EXPECT_TRUE(out.empty());
    }
}

// IDX3 — NoteQueryIndex on a synthetic multi-level tree: exercises the internal-node
// recursion, the max-release subtree prune, and the prefix (qHi) prune, with the
// result checked against a brute-force oracle over random ranges.
TEST(Composing_NoteModelTests, IDX3_NoteQueryIndex_SyntheticOverlapMatchesBruteForce)
{
    // 13 notes (non-power-of-two ⇒ padded leaves exist). Onsets ascending; mixed
    // short and long (sustaining) releases so overlap pruning genuinely fires.
    std::vector<NEvent> notes;
    const int onsets[]   = { 0, 0, 100, 200, 200, 300, 400, 500, 600, 700, 800, 900, 1000 };
    const int releases[] = { 9600, 150, 250, 250, 2000, 350, 1500, 550, 650, 720, 850, 950, 1100 };
    for (int i = 0; i < 13; ++i) {
        NEvent e;
        e.onset = onsets[i];
        e.release = releases[i];
        notes.push_back(e);
    }
    NoteQueryIndex idx;
    idx.build(notes);

    auto brute = [&](int t0, int t1) {
        std::vector<int> out;
        if (t1 <= t0) {
            return out;
        }
        for (int i = 0; i < static_cast<int>(notes.size()); ++i) {
            if (notes[i].onset >= t1) {
                break;
            }
            if (notes[i].release > t0) {
                out.push_back(i);
            }
        }
        return out;
    };

    std::mt19937 rng(0x1234u);
    std::uniform_int_distribution<int> dist(-200, 9800);
    for (int k = 0; k < 5000; ++k) {
        const int a = dist(rng), b = dist(rng);
        const int t0 = std::min(a, b), t1 = std::max(a, b);
        std::vector<int> got;
        if (t1 > t0) {
            idx.overlapIndices(idx.onsetLowerBound(t1), t0, got);
        }
        EXPECT_EQ(got, brute(t0, t1)) << "[" << t0 << "," << t1 << ")";
    }
}

// IDX4 — empty NoteModel: the m_notes.empty() guard in both queries. build(nullptr)
// yields a model with no notes (and a default, unbuilt index); the queries must
// short-circuit to {} rather than touch the index.
TEST(Composing_NoteModelTests, IDX4_EmptyModel_QueriesReturnEmpty)
{
    const NoteModel model = NoteModel::build(nullptr);
    ASSERT_TRUE(model.notes().empty());
    EXPECT_TRUE(model.overlapping(0, 100).empty());   // t1 > t0, but m_notes empty
    EXPECT_TRUE(model.onsetIn(0, 100).empty());
    EXPECT_TRUE(model.overlapping(100, 0).empty());   // t1 <= t0
    EXPECT_TRUE(model.onsetIn(100, 0).empty());
}

// ── Layer-1 / Phase 1a — build-over-a-selection + extend (the bounded-context
// supplier API). Designs: cowork_layer1_extend_design.md /
// cowork_bounded_context_design.md. These guard the §3 invariants: degenerate
// byte-identity, build-then-extend equivalence, append-only, onset-sort,
// idempotent extend, boundary clamp + report, sustained-in capture, index≡scan.

namespace {

bool eventsEqual(const NEvent& a, const NEvent& b)
{
    return a.pitch == b.pitch && a.tpc == b.tpc && a.staff == b.staff
           && a.voice == b.voice && a.onset == b.onset && a.release == b.release
           && a.duration == b.duration && a.isGrace == b.isGrace
           && a.plays == b.plays && a.visible == b.visible
           && a.staffEligible == b.staffEligible;
}

// Two models hold the SAME notes (count, order, every field). Selection span is
// deliberately NOT compared — by design it is fixed at build and differs between
// "build(X)" and "build(A) then extend to X" (§2 selection ⊆ loaded).
void expectSameNotes(const NoteModel& a, const NoteModel& b)
{
    ASSERT_EQ(a.notes().size(), b.notes().size()) << "note count differs";
    for (std::size_t i = 0; i < a.notes().size(); ++i) {
        EXPECT_TRUE(eventsEqual(a.notes()[i], b.notes()[i])) << "note " << i << " differs";
    }
}

// Query answers identical (by value — pointers are model-local) on one range.
void expectSameQueries(const NoteModel& a, const NoteModel& b, int t0, int t1)
{
    const auto oa = a.overlapping(t0, t1);
    const auto ob = b.overlapping(t0, t1);
    ASSERT_EQ(oa.size(), ob.size()) << "overlapping(" << t0 << "," << t1 << ") size differs";
    for (std::size_t i = 0; i < oa.size(); ++i) {
        EXPECT_TRUE(eventsEqual(*oa[i], *ob[i])) << "overlapping[" << i << "] differs";
    }
    const auto na = a.onsetIn(t0, t1);
    const auto nb = b.onsetIn(t0, t1);
    ASSERT_EQ(na.size(), nb.size()) << "onsetIn(" << t0 << "," << t1 << ") size differs";
    for (std::size_t i = 0; i < na.size(); ++i) {
        EXPECT_TRUE(eventsEqual(*na[i], *nb[i])) << "onsetIn[" << i << "] differs";
    }
}

// Onset-sorted ascending (the build-order invariant; must survive every extend).
bool onsetSorted(const NoteModel& m)
{
    for (std::size_t i = 1; i < m.notes().size(); ++i) {
        if (m.notes()[i].onset < m.notes()[i - 1].onset) {
            return false;
        }
    }
    return true;
}

} // namespace

// EXT1 — degenerate byte-identity (in-process half of the corpus gate). For every
// fixture, build(sc) (full-score span) retains EXACTLY the notes a truly-unbounded
// span retains — i.e. the [scoreStart, scoreEnd) filter drops nothing — and the
// loaded span equals the score span. (The whole-corpus .ours.json byte diff is the
// other half of the gate, run outside the test binary.)
TEST(Composing_NoteModelTests, EXT1_DegenerateBuild_RetainsAllNotes)
{
    std::mt19937 rng(0xE17A1u);
    for (const char16_t* path : kAllNmFixtures) {
        MasterScore* score = ScoreRW::readScore(path);
        ASSERT_TRUE(score) << "missing fixture";

        const NoteModel full = NoteModel::build(score);
        // An explicitly-everything span: nothing can fall outside it.
        const NoteModel everything = NoteModel::build(score, INT_MIN / 2, INT_MAX / 2);

        expectSameNotes(full, everything);
        EXPECT_FALSE(full.notes().empty()) << "fixture has no notes";
        EXPECT_TRUE(onsetSorted(full));
        // Loaded span == selection span == the structural score span.
        EXPECT_EQ(full.loadedStart(), full.selectionStart());
        EXPECT_EQ(full.loadedEnd(), full.selectionEnd());
        EXPECT_LE(full.loadedStart(), full.notes().front().onset);
        EXPECT_GT(full.loadedEnd(), full.notes().back().onset);

        // Query answers identical between the two whole-score builds.
        int maxRelease = INT_MIN;
        for (const NEvent& e : full.notes()) {
            maxRelease = std::max(maxRelease, e.release);
        }
        std::uniform_int_distribution<int> dist(full.loadedStart() - 480, maxRelease + 480);
        for (int k = 0; k < 100; ++k) {
            const int a = dist(rng), b = dist(rng);
            expectSameQueries(full, everything, std::min(a, b), std::max(a, b));
        }
        delete score;
    }
}

// EXT2 — build-then-extend equivalence to the whole score + determinism in the
// step granularity. A sub-selection extended (both directions) until it reaches
// the score boundary yields a model IDENTICAL (notes, order, loaded span, query
// answers) to the whole-score build — and reaching it in one big step or many
// small steps gives the same model (§3 invariant 2; §8 determinism).
TEST(Composing_NoteModelTests, EXT2_BuildThenExtendToFull_EqualsWholeScore)
{
    std::mt19937 rng(0xB10C5u);
    for (const char16_t* path : kAllNmFixtures) {
        MasterScore* score = ScoreRW::readScore(path);
        ASSERT_TRUE(score) << "missing fixture";

        const NoteModel full = NoteModel::build(score);
        const int s = full.loadedStart();
        const int e = full.loadedEnd();
        const int span = e - s;
        ASSERT_GT(span, 0);
        if (span < 8) { delete score; continue; }  // too short to sub-select; not seen in practice
        // An interior sub-selection (well inside the score).
        const int a0 = s + span / 4;
        const int a1 = e - span / 4;
        ASSERT_LT(a0, a1) << "fixture too short to sub-select";

        // (a) one big step each direction → clamps at both boundaries.
        {
            NoteModel sel = NoteModel::build(score, a0, a1);
            sel.extend(NoteModel::Direction::Earlier, span * 4);
            EXPECT_TRUE(sel.boundaryReached());
            sel.extend(NoteModel::Direction::Later, span * 4);
            EXPECT_TRUE(sel.boundaryReached());
            EXPECT_EQ(sel.loadedStart(), s);
            EXPECT_EQ(sel.loadedEnd(), e);
            EXPECT_TRUE(onsetSorted(sel));
            expectSameNotes(sel, full);
            // selection span is the original (a0,a1) — evidence vs output (§2).
            EXPECT_EQ(sel.selectionStart(), a0);
            EXPECT_EQ(sel.selectionEnd(), a1);

            int maxRel = INT_MIN;
            for (const NEvent& ev : full.notes()) {
                maxRel = std::max(maxRel, ev.release);
            }
            std::uniform_int_distribution<int> dist(s - 480, maxRel + 480);
            for (int k = 0; k < 100; ++k) {
                const int x = dist(rng), y = dist(rng);
                expectSameQueries(sel, full, std::min(x, y), std::max(x, y));
            }
        }
        // (b) many small steps each direction → identical final model.
        {
            NoteModel sel = NoteModel::build(score, a0, a1);
            const int step = std::max(1, span / 7);
            std::size_t prevCount = sel.notes().size();
            for (int guard = 0; guard < 10000 && !sel.boundaryReached(); ++guard) {
                sel.extend(NoteModel::Direction::Earlier, step);
                EXPECT_GE(sel.notes().size(), prevCount) << "append-only violated (earlier)";
                prevCount = sel.notes().size();
            }
            for (int guard = 0; guard < 10000; ++guard) {
                const bool wasAtEnd = (sel.loadedEnd() == e);
                sel.extend(NoteModel::Direction::Later, step);
                EXPECT_GE(sel.notes().size(), prevCount) << "append-only violated (later)";
                prevCount = sel.notes().size();
                if (wasAtEnd || sel.loadedEnd() == e) {
                    break;
                }
            }
            EXPECT_EQ(sel.loadedStart(), s);
            EXPECT_EQ(sel.loadedEnd(), e);
            EXPECT_TRUE(onsetSorted(sel));
            expectSameNotes(sel, full);
        }
        delete score;
    }
}

// EXT3 — interior build-then-extend equivalence. build(A0,A1) extended to an
// INTERIOR span [X0,X1) (X0<A0, X1>A1, both inside the score) equals build(X0,X1)
// directly — notes, order, loaded span, query answers. (Selection span differs by
// design and is not compared.)
TEST(Composing_NoteModelTests, EXT3_BuildThenExtendInterior_EqualsDirectBuild)
{
    std::mt19937 rng(0x1273A7u);
    for (const char16_t* path : kAllNmFixtures) {
        MasterScore* score = ScoreRW::readScore(path);
        ASSERT_TRUE(score) << "missing fixture";

        const NoteModel full = NoteModel::build(score);
        const int s = full.loadedStart();
        const int e = full.loadedEnd();
        const int span = e - s;
        ASSERT_GT(span, 0);
        if (span <= 8) { delete score; continue; }  // too short for interior nesting; not seen in practice

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
        EXPECT_FALSE(sel.boundaryReached()) << "interior earlier target must not clamp";
        sel.extend(NoteModel::Direction::Later, x1 - a1);
        EXPECT_FALSE(sel.boundaryReached()) << "interior later target must not clamp";

        EXPECT_EQ(sel.loadedStart(), x0);
        EXPECT_EQ(sel.loadedEnd(), x1);
        EXPECT_TRUE(onsetSorted(sel));
        expectSameNotes(sel, direct);

        std::uniform_int_distribution<int> dist(s - 480, e + 480);
        for (int k = 0; k < 200; ++k) {
            const int p = dist(rng), q = dist(rng);
            expectSameQueries(sel, direct, std::min(p, q), std::max(p, q));
        }
        delete score;
    }
}

// EXT4 — extend unit semantics: append-only, idempotent re-request, boundary
// clamp + boundaryReached, on a fixture with a known long span.
TEST(Composing_NoteModelTests, EXT4_Extend_AppendOnlyIdempotentClamp)
{
    MasterScore* score = ScoreRW::readScore(u"data/nm_long_sustain.mscx");  // C4 [0,9600)
    ASSERT_TRUE(score);
    const NoteModel full = NoteModel::build(score);
    const int scoreStart = full.loadedStart();   // 0
    const int scoreEnd   = full.loadedEnd();      // == score endTick

    NoteModel m = NoteModel::build(score, 4000, 5000);
    EXPECT_EQ(m.loadedStart(), 4000);
    EXPECT_EQ(m.loadedEnd(), 5000);
    EXPECT_EQ(m.selectionStart(), 4000);
    EXPECT_EQ(m.selectionEnd(), 5000);
    EXPECT_FALSE(m.boundaryReached());

    // Non-positive amount is a pure no-op (state untouched).
    const int beforeStart = m.loadedStart();
    m.extend(NoteModel::Direction::Earlier, 0);
    EXPECT_EQ(m.loadedStart(), beforeStart);
    m.extend(NoteModel::Direction::Earlier, -100);
    EXPECT_EQ(m.loadedStart(), beforeStart);

    // Earlier within bounds: grows down, no clamp.
    m.extend(NoteModel::Direction::Earlier, 1000);
    EXPECT_EQ(m.loadedStart(), 3000);
    EXPECT_FALSE(m.boundaryReached());

    // Earlier past the start: clamps to scoreStart, boundaryReached.
    m.extend(NoteModel::Direction::Earlier, 100000);
    EXPECT_EQ(m.loadedStart(), scoreStart);
    EXPECT_TRUE(m.boundaryReached());
    const std::size_t countAtStart = m.notes().size();

    // Re-request at the boundary: idempotent no-op, still flagged boundaryReached.
    m.extend(NoteModel::Direction::Earlier, 5000);
    EXPECT_EQ(m.loadedStart(), scoreStart);
    EXPECT_TRUE(m.boundaryReached());
    EXPECT_EQ(m.notes().size(), countAtStart) << "no-op extend must not change notes";

    // Later past the end: clamps to scoreEnd, boundaryReached; append-only.
    m.extend(NoteModel::Direction::Later, 100000);
    EXPECT_EQ(m.loadedEnd(), scoreEnd);
    EXPECT_TRUE(m.boundaryReached());
    EXPECT_GE(m.notes().size(), countAtStart) << "append-only (later) violated";

    // Now fully spans the score → identical notes to the whole-score build.
    EXPECT_EQ(m.loadedStart(), scoreStart);
    EXPECT_EQ(m.loadedEnd(), scoreEnd);
    expectSameNotes(m, full);

    delete score;
}

// EXT5 — sustained-in capture: a note that ONSETS before the loaded span but
// SUSTAINS into it is retained (it really sounds during the selection). The C4
// [0,9600) sustain, selected at [4800,5000), must be present with onset 0.
TEST(Composing_NoteModelTests, EXT5_SustainedInNoteRetained)
{
    MasterScore* score = ScoreRW::readScore(u"data/nm_long_sustain.mscx");
    ASSERT_TRUE(score);

    const NoteModel m = NoteModel::build(score, 4800, 5000);
    const NEvent* c4 = findNote(m, [](const NEvent& e) {
        return e.pitch == 60 && e.onset == 0 && e.release == 9600;
    });
    ASSERT_TRUE(c4) << "C4 sustaining into [4800,5000) must be retained (onset < loadedStart)";
    // It is found by an overlap query inside the selection too.
    const auto ov = m.overlapping(4800, 5000);
    ASSERT_EQ(static_cast<int>(ov.size()), 1);
    EXPECT_EQ(ov.front()->pitch, 60);

    delete score;
}

// EXT6 — index ≡ linear scan over a post-EXTENSION model: the existing IDX linear
// oracle must still match after the loaded span has grown (the index is rebuilt
// on each extend). Extends the IDX1 property to the extended model.
TEST(Composing_NoteModelTests, EXT6_IndexedEqualsLinear_AfterExtend)
{
    std::mt19937 rng(0xF00D5u);
    for (const char16_t* path : kAllNmFixtures) {
        MasterScore* score = ScoreRW::readScore(path);
        ASSERT_TRUE(score) << "missing fixture";

        const NoteModel full = NoteModel::build(score);
        const int s = full.loadedStart();
        const int e = full.loadedEnd();
        const int span = e - s;
        ASSERT_GT(span, 0);

        NoteModel m = NoteModel::build(score, s + span / 3, e - span / 3);
        m.extend(NoteModel::Direction::Earlier, span / 6);
        m.extend(NoteModel::Direction::Later, span / 6);

        int maxRelease = INT_MIN, minOnset = INT_MAX;
        for (const NEvent& ev : m.notes()) {
            maxRelease = std::max(maxRelease, ev.release);
            minOnset = std::min(minOnset, ev.onset);
        }
        if (m.notes().empty()) {
            delete score;
            continue;
        }
        std::uniform_int_distribution<int> dist(minOnset - 480, maxRelease + 480);
        for (int k = 0; k < 300; ++k) {
            const int a = dist(rng), b = dist(rng);
            expectQueriesMatch(m, a, b);
            expectQueriesMatch(m, b, a);
        }
        delete score;
    }
}

// EXT7 — extend on a no-score / empty model is a safe no-op (the scoreSpan guard).
TEST(Composing_NoteModelTests, EXT7_ExtendOnEmptyModelIsNoOp)
{
    NoteModel m = NoteModel::build(nullptr);
    ASSERT_TRUE(m.notes().empty());
    m.extend(NoteModel::Direction::Earlier, 1000);  // scoreStart==scoreEnd==0 → clamp no-op
    m.extend(NoteModel::Direction::Later, 1000);
    EXPECT_TRUE(m.notes().empty());
    EXPECT_TRUE(m.overlapping(0, 100).empty());
}

// IDX_PERF — DISABLED by default (run with --gtest_also_run_disabled_tests). Times
// the REAL indexed query vs the linear reference across a per-slice workload at
// growing N, demonstrating the O(N²)→O(N log N) transition. Diagnostic only.
TEST(Composing_NoteModelTests, DISABLED_IDX_PERF_ScalingIndexedVsLinear)
{
    auto makeNotes = [](int n) {
        std::vector<NEvent> v;
        v.reserve(n);
        std::mt19937 rng(42u);
        std::uniform_int_distribution<int> durDist(240, 1920);
        // A few long sustains so the overlap prefix is genuinely populated.
        std::uniform_int_distribution<int> longDist(0, 49);
        int t = 0;
        for (int i = 0; i < n; ++i) {
            NEvent e;
            e.onset = t;
            int dur = durDist(rng);
            if (longDist(rng) == 0) {
                dur *= 20;  // long sustain spanning many later slices
            }
            e.release = t + dur;
            v.push_back(e);
            t += 60;  // dense onset grid
        }
        return v;
    };

    // The linear pre-A overlapping over a raw notes vector (the O(N) per-query cost).
    auto linearCount = [](const std::vector<NEvent>& v, int t0, int t1) {
        int c = 0;
        for (const NEvent& e : v) {
            if (e.onset >= t1) {
                break;
            }
            if (e.release > t0) {
                ++c;
            }
        }
        return c;
    };

    printf("\n  N      linear(ms)   indexed(ms)   ratio   (per-slice overlapping workload)\n");
    for (int n : { 1000, 4000, 16000, 64000 }) {
        const std::vector<NEvent> notes = makeNotes(n);
        NoteQueryIndex idx;
        idx.build(notes);

        // Workload: one overlapping query per "slice" = each [onset_i, onset_{i+1}).
        long long linSum = 0, idxSum = 0;

        auto tl0 = std::chrono::steady_clock::now();
        for (int i = 0; i + 1 < n; ++i) {
            linSum += linearCount(notes, notes[i].onset, notes[i + 1].onset);
        }
        auto tl1 = std::chrono::steady_clock::now();

        std::vector<int> out;
        auto ti0 = std::chrono::steady_clock::now();
        for (int i = 0; i + 1 < n; ++i) {
            out.clear();
            idx.overlapIndices(idx.onsetLowerBound(notes[i + 1].onset), notes[i].onset, out);
            idxSum += static_cast<long long>(out.size());
        }
        auto ti1 = std::chrono::steady_clock::now();

        const double linMs = std::chrono::duration_cast<std::chrono::duration<double, std::milli>>(tl1 - tl0).count();
        const double idxMs = std::chrono::duration_cast<std::chrono::duration<double, std::milli>>(ti1 - ti0).count();
        ASSERT_EQ(linSum, idxSum) << "indexed and linear disagree on total hits at N=" << n;
        printf("  %-6d %10.2f   %10.2f   %6.1f\n", n, linMs, idxMs, idxMs > 0 ? linMs / idxMs : 0.0);
    }
    printf("\n");
}
