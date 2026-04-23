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

// ── Behavior-snapshot pinning tests for NotationInteraction::addAnalyzedHarmonyToSelection ──
//
// PURPOSE
// -------
// These tests capture the CURRENT output of the addAnalyzedHarmonyToSelection path
// before iteration 9 routes it through the bridge.  They are NOT correctness assertions —
// they are behavior snapshots.  Iteration 9 will change the output intentionally
// (chord-track staves excluded from output, scoreNoteSpelling applied) and must update
// the EXPECT_EQ strings below as part of its diff.
//
// HOW THIS REPLICATES THE PRODUCTION FUNCTION
// --------------------------------------------
// NotationInteraction::addAnalyzedHarmonyToSelection (notationinteraction.cpp:8258)
// cannot be called directly in tests because it requires a fully wired NotationInteraction
// instance (Notation*, INotationUndoStackPtr, IoC context).  Instead, each test replicates
// the function's three-step computation:
//   1. Collect notes from selection, deduplicate by (staffIdx, tick) — first note wins.
//   2. Call analyzeNoteHarmonicContext(note, outKeyFifths, outKeyMode) for each.
//   3. Format the top result with ChordSymbolFormatter.
// The write step (startEdit / undoAddElement / apply) is standard plumbing and is not
// replicated; iter 9's change is entirely in steps 1–3.
//
// FIXTURE
// -------
// harmony_pinning_i_iv_v_i.mscx — 2 staves, 4/4 C major, 4 whole-note measures:
//   Staff 0 (Piano):             I  (C-E-G)  |  IV (F-A-C)  |  V (G-B-D)  |  I (C-E-G)
//   Staff 1 (Chord Track Piano): C4 root     |  whole rest  |  G4 root    |  C4 root
//
// Staff 1's name contains "Chord Track", so isChordTrackStaff() returns true for it.
// The whole rest at measure 2 of staff 1 is used by the Rest-path bonus test.
//
// PINNED PRE-ITER-9 BEHAVIORS
// ----------------------------
// 1. Chord-track staves are NOT excluded from harmony OUTPUT.  Staff 1's notes appear
//    in the deduplication map just like staff 0's notes, producing harmony annotations
//    on the chord-track staff (iter 9 will add the exclusion guard).
// 2. ChordSymbolFormatter is called WITHOUT scoreNoteSpelling Options (iter 9 will pass
//    ChordSymbolFormatter::Options{scoreNoteSpelling(sc)}).
// 3. analyzeNoteHarmonicContext excludes chord-track staves from ANALYSIS INPUT via
//    excludeStaves — so staff 1 notes are analyzed using staff 0 pitches anyway.

#include <algorithm>
#include <map>
#include <string>
#include <vector>

#include <gtest/gtest.h>

#include "modularity/ioc.h"

#include "composing/icomposinganalysisconfiguration.h"
#include "composing/analysis/chord/chordanalyzer.h"

#include "engraving/dom/chord.h"
#include "engraving/dom/chordrest.h"
#include "engraving/dom/masterscore.h"
#include "engraving/dom/note.h"
#include "engraving/dom/rest.h"
#include "engraving/dom/segment.h"
#include "engraving/dom/mscore.h"
#include "engraving/dom/staff.h"

#include "engraving/tests/utils/scorerw.h"

#include "notation/internal/notationcomposingbridge.h"

#include "test_helpers.h"

using namespace mu::engraving;
using namespace mu::composing::analysis;

namespace {

void configureAnalysis()
{
    auto cfg = analysisConfig();
    ASSERT_TRUE(cfg) << "IComposingAnalysisConfiguration not registered";
    cfg->setUseRegionalAccumulation(true);
}

// Replicates the note-collection step of addAnalyzedHarmonyToSelection.
// Iterates every segment of the score, deduplicates by (staffIdx, tick),
// keeping the first note encountered per pair — exactly as the production function does
// when sc->selection().elements() covers the whole score.
struct NoteEntry {
    int staffIdx;
    int tick;
    Note* note;
};

std::vector<NoteEntry> collectNotesByStaffTick(MasterScore* score)
{
    std::map<std::pair<int, int>, Note*> byStaffTick;
    for (Segment* seg = score->firstSegment(SegmentType::ChordRest); seg;
         seg = seg->next1(SegmentType::ChordRest)) {
        for (track_idx_t t = 0; t < score->ntracks(); ++t) {
            ChordRest* cr = seg->cr(t);
            if (!cr || !cr->isChord()) {
                continue;
            }
            const std::vector<Note*>& notes = toChord(cr)->notes();
            if (notes.empty()) {
                continue;
            }
            int staffIdx = static_cast<int>(track2staff(t));
            int tick = seg->tick().ticks();
            auto key = std::make_pair(staffIdx, tick);
            byStaffTick.emplace(key, notes.front());
        }
    }

    std::vector<NoteEntry> result;
    result.reserve(byStaffTick.size());
    for (auto& [key, note] : byStaffTick) {
        result.push_back({ key.first, key.second, note });
    }
    // std::map iterates in key order, so result is already sorted by (staffIdx, tick).
    return result;
}

} // namespace

class NotationInteractionHarmonyPinning : public ::testing::Test {};

// ── ChordSymbol (HarmonyType::STANDARD) ──────────────────────────────────────
//
// Pins what addAnalyzedHarmonyToSelection(HarmonyType::STANDARD) would write
// for each note position in the fixture.
//
// Pinned pre-iter-9:
//   - Staff 1 (chord track) entries appear because the function does not yet
//     exclude chord-track staves from output.  Iter 9 will remove them and update
//     the ASSERT_EQ size and the expectation list.
//   - No ChordSymbolFormatter::Options passed (spelling = Standard default).

TEST_F(NotationInteractionHarmonyPinning, BehaviorSnapshot_ChordSymbol)
{
    configureAnalysis();

    MasterScore* score = ScoreRW::readScore(u"harmony_pinning_i_iv_v_i.mscx");
    ASSERT_TRUE(score) << "Failed to load harmony_pinning_i_iv_v_i.mscx";

    const std::vector<NoteEntry> entries = collectNotesByStaffTick(score);

    // Collect (staffIdx, tick, symbol) for each entry.
    struct Row { int staffIdx; int tick; std::string symbol; };
    std::vector<Row> rows;
    for (const NoteEntry& e : entries) {
        int keyFifths = 0;
        KeySigMode keyMode = KeySigMode::Ionian;
        const auto results = mu::notation::analyzeNoteHarmonicContext(e.note, keyFifths, keyMode);
        if (results.empty()) {
            continue;
        }
        rows.push_back({ e.staffIdx, e.tick, ChordSymbolFormatter::formatSymbol(results[0], keyFifths) });
    }

    // Pinned pre-iter-9: 7 entries — staff 0 (4 notes) + staff 1 (3 notes; M2 is a rest).
    // Chord-track staves not excluded from output; iter 9 will reduce this to 4.
    ASSERT_EQ(rows.size(), 7u)
        << "Entry count changed — update expectations if iter 9 added the chord-track exclusion";

    // Staff 0: I-IV-V-I chord symbols.
    EXPECT_EQ(rows[0].staffIdx, 0); EXPECT_EQ(rows[0].symbol, "C");   // measure 1: I
    EXPECT_EQ(rows[1].staffIdx, 0); EXPECT_EQ(rows[1].symbol, "F");   // measure 2: IV
    EXPECT_EQ(rows[2].staffIdx, 0); EXPECT_EQ(rows[2].symbol, "G");   // measure 3: V
    EXPECT_EQ(rows[3].staffIdx, 0); EXPECT_EQ(rows[3].symbol, "C");   // measure 4: I

    // Staff 1 (Chord Track Piano): Pinned pre-iter-9 — should NOT be written after iter 9.
    // Analysis still uses staff 0 pitch data (chord-track excluded from analysis input),
    // so the symbols match staff 0's output at the same ticks.
    EXPECT_EQ(rows[4].staffIdx, 1); EXPECT_EQ(rows[4].symbol, "C");   // measure 1 (M2 is rest, so M3 tick next)
    EXPECT_EQ(rows[5].staffIdx, 1); EXPECT_EQ(rows[5].symbol, "G");   // measure 3: V
    EXPECT_EQ(rows[6].staffIdx, 1); EXPECT_EQ(rows[6].symbol, "C");   // measure 4: I

    delete score;
}

// ── RomanNumeral (HarmonyType::ROMAN) ────────────────────────────────────────
//
// Pins what addAnalyzedHarmonyToSelection(HarmonyType::ROMAN) would write.
// formatRomanNumeral returns "" for non-diatonic chords; all I-IV-V-I chords
// are diatonic in C major so all entries should be non-empty.
//
// Pinned pre-iter-9:
//   - Staff 1 entries present (chord-track not excluded from output).
//   - nextRootPc is -1 (single-note path, not two-pass), so no V/x tonicization labels.

TEST_F(NotationInteractionHarmonyPinning, BehaviorSnapshot_RomanNumeral)
{
    configureAnalysis();

    MasterScore* score = ScoreRW::readScore(u"harmony_pinning_i_iv_v_i.mscx");
    ASSERT_TRUE(score) << "Failed to load harmony_pinning_i_iv_v_i.mscx";

    const std::vector<NoteEntry> entries = collectNotesByStaffTick(score);

    struct Row { int staffIdx; int tick; std::string roman; };
    std::vector<Row> rows;
    for (const NoteEntry& e : entries) {
        int keyFifths = 0;
        KeySigMode keyMode = KeySigMode::Ionian;
        const auto results = mu::notation::analyzeNoteHarmonicContext(e.note, keyFifths, keyMode);
        if (results.empty()) {
            continue;
        }
        const std::string roman = ChordSymbolFormatter::formatRomanNumeral(results[0]);
        if (roman.empty()) {
            continue;  // non-diatonic; not written by addAnalyzedHarmonyToSelection
        }
        rows.push_back({ e.staffIdx, e.tick, roman });
    }

    // Pinned pre-iter-9: 7 entries (chord-track not excluded).
    ASSERT_EQ(rows.size(), 7u)
        << "Entry count changed — update expectations if iter 9 added the chord-track exclusion";

    // Staff 0.
    EXPECT_EQ(rows[0].staffIdx, 0); EXPECT_EQ(rows[0].roman, "I");    // measure 1
    EXPECT_EQ(rows[1].staffIdx, 0); EXPECT_EQ(rows[1].roman, "IV");   // measure 2
    EXPECT_EQ(rows[2].staffIdx, 0); EXPECT_EQ(rows[2].roman, "V");    // measure 3
    EXPECT_EQ(rows[3].staffIdx, 0); EXPECT_EQ(rows[3].roman, "I");    // measure 4

    // Staff 1 (Chord Track Piano): Pinned pre-iter-9.
    EXPECT_EQ(rows[4].staffIdx, 1); EXPECT_EQ(rows[4].roman, "I");    // measure 1
    EXPECT_EQ(rows[5].staffIdx, 1); EXPECT_EQ(rows[5].roman, "V");    // measure 3
    EXPECT_EQ(rows[6].staffIdx, 1); EXPECT_EQ(rows[6].roman, "I");    // measure 4

    delete score;
}

// ── Nashville (HarmonyType::NASHVILLE) ───────────────────────────────────────
//
// Pins what addAnalyzedHarmonyToSelection(HarmonyType::NASHVILLE) would write.
//
// Pinned pre-iter-9:
//   - Staff 1 entries present (chord-track not excluded from output).

TEST_F(NotationInteractionHarmonyPinning, BehaviorSnapshot_Nashville)
{
    configureAnalysis();

    MasterScore* score = ScoreRW::readScore(u"harmony_pinning_i_iv_v_i.mscx");
    ASSERT_TRUE(score) << "Failed to load harmony_pinning_i_iv_v_i.mscx";

    const std::vector<NoteEntry> entries = collectNotesByStaffTick(score);

    struct Row { int staffIdx; int tick; std::string nashville; };
    std::vector<Row> rows;
    for (const NoteEntry& e : entries) {
        int keyFifths = 0;
        KeySigMode keyMode = KeySigMode::Ionian;
        const auto results = mu::notation::analyzeNoteHarmonicContext(e.note, keyFifths, keyMode);
        if (results.empty()) {
            continue;
        }
        const std::string nashville = ChordSymbolFormatter::formatNashvilleNumber(results[0], keyFifths);
        if (nashville.empty()) {
            continue;
        }
        rows.push_back({ e.staffIdx, e.tick, nashville });
    }

    // Pinned pre-iter-9: 7 entries (chord-track not excluded).
    ASSERT_EQ(rows.size(), 7u)
        << "Entry count changed — update expectations if iter 9 added the chord-track exclusion";

    // Staff 0: Nashville numbers for I-IV-V-I in C major (degree+1).
    EXPECT_EQ(rows[0].staffIdx, 0); EXPECT_EQ(rows[0].nashville, "1");  // I
    EXPECT_EQ(rows[1].staffIdx, 0); EXPECT_EQ(rows[1].nashville, "4");  // IV
    EXPECT_EQ(rows[2].staffIdx, 0); EXPECT_EQ(rows[2].nashville, "5");  // V
    EXPECT_EQ(rows[3].staffIdx, 0); EXPECT_EQ(rows[3].nashville, "1");  // I

    // Staff 1 (Chord Track Piano): Pinned pre-iter-9.
    EXPECT_EQ(rows[4].staffIdx, 1); EXPECT_EQ(rows[4].nashville, "1");  // measure 1
    EXPECT_EQ(rows[5].staffIdx, 1); EXPECT_EQ(rows[5].nashville, "5");  // measure 3
    EXPECT_EQ(rows[6].staffIdx, 1); EXPECT_EQ(rows[6].nashville, "1");  // measure 4

    delete score;
}

// ── Bonus: Rest-path pinning (analyzeRestHarmonicContextDetails) ──────────────
//
// analyzeRestHarmonicContextDetails is the other zero-coverage public bridge entry
// point.  This test pins its output cheaply using the same fixture (the whole rest
// at staff 1, measure 2 of harmony_pinning_i_iv_v_i.mscx).
//
// At that tick (4*480 = 1920), staff 0 has an F major triad (F4-A4-C5).  The rest-path
// function excludes chord-track staves from analysis input (same as the note path),
// so it reads from staff 0 → should return F major as the prevailing harmony.
//
// Asserts:
//   - chordResults is non-empty
//   - keyFifths == 0 (C major inferred)
//   - chordResults[0].identity.rootPc == 5 (F, the IV chord)

TEST_F(NotationInteractionHarmonyPinning, BehaviorSnapshot_RestContext)
{
    configureAnalysis();

    MasterScore* score = ScoreRW::readScore(u"harmony_pinning_i_iv_v_i.mscx");
    ASSERT_TRUE(score) << "Failed to load harmony_pinning_i_iv_v_i.mscx";

    // Find the whole rest on staff 1 (Chord Track Piano), measure 2.
    // Measure 2 starts at tick = 4 * 480 = 1920 (one whole-note measure after the start).
    const int kTicksPerWhole = 4 * 480;
    const int measure2StartTick = kTicksPerWhole;

    Rest* targetRest = nullptr;
    for (Segment* seg = score->firstSegment(SegmentType::ChordRest); seg;
         seg = seg->next1(SegmentType::ChordRest)) {
        if (seg->tick().ticks() != measure2StartTick) {
            continue;
        }
        // Staff 1 uses track index VOICES (= 4 on standard scores).
        for (track_idx_t t = VOICES; t < 2 * VOICES; ++t) {
            ChordRest* cr = seg->cr(t);
            if (cr && cr->isRest()) {
                targetRest = toRest(cr);
                break;
            }
        }
        if (targetRest) {
            break;
        }
    }

    ASSERT_TRUE(targetRest)
        << "Could not find whole rest on staff 1 at measure 2 (tick " << measure2StartTick << ")";

    const mu::notation::NoteHarmonicContext ctx = mu::notation::analyzeRestHarmonicContextDetails(targetRest);

    // Pinned pre-iter-9: the rest path returns meaningful results even for a rest on a
    // chord-track staff, because chord-track staves are excluded from ANALYSIS INPUT and
    // the result comes from staff 0's F major triad at that tick.
    ASSERT_FALSE(ctx.chordResults.empty())
        << "analyzeRestHarmonicContextDetails returned empty results for a rest surrounded by clear harmony";

    // Key must be C major (inferred from surrounding I-IV-V-I context).
    EXPECT_EQ(ctx.keyFifths, 0)
        << "Expected C major (keyFifths=0); got keyFifths=" << ctx.keyFifths;

    // Prevailing chord at measure 2 must be F (rootPc=5 = IV of C major).
    EXPECT_EQ(ctx.chordResults[0].identity.rootPc, 5)
        << "Expected F major (rootPc=5) at rest position; got rootPc="
        << ctx.chordResults[0].identity.rootPc;

    delete score;
}
