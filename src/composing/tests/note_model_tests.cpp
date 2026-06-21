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

#include <functional>
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
