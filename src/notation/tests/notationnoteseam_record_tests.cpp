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

// ── Golden-less structural pins: the note-seam RECORD ARM (seams-2 note-seam, dispatch Task 3) ───
//
// With useJointNotationRecord ON, the single-note surface (analyzeNoteHarmonicContext[Details], and
// through it the status bar / harmony write / right-click menu) is a VIEW into the joint notation
// record (contract §1 seam 2): produceNotationRecord -> noteView(rec, tick) -> the ONE builder. These
// tests do NOT hardcode expected symbols (that would pin the inference, which is the switch's own
// evidence at P6) — they pin that each consumer's output EQUALS the record's OWN published facts, on
// two fixtures. The flag-OFF legacy path is byte-identical (every other test in the suite exercises it).
//
// The three note-seam consumers all route through analyzeNoteHarmonicContext[Details], so the ONE
// record-arm branch carries all three; each renders via the SAME shared formatters. The pins here:
//   1. the carriage == the record's committed reading at each note's tick;
//   2. the ordering rule (committed first, then descending §3.3 content score);
//   3. the status bar renders the carriage's committed symbol;
//   4. the harmony write uses the carriage;
//   5. the context menu's score suffix is the §3.3 committed content score;
//   6. the edges: an out-of-span tick and a produce failure yield NOTHING (no partial output, #13).

#include <cmath>
#include <set>
#include <string>
#include <utility>
#include <vector>

#include <gtest/gtest.h>

#include "modularity/ioc.h"

#include "composing/icomposinganalysisconfiguration.h"
#include "composing/analysis/chord/chordanalyzer.h"                 // ChordAnalysisResult / ChordSymbolFormatter / KeySigMode
#include "composing/analysis/section/sectionrecordadapter.h"        // chordResultFromRecordSegment (the ONE converter)
#include "composing/analysis/joint/jointnotationproducer.h"         // produceNotationRecord / noteView
#include "composing/analysis/joint/jointnotationrecord.h"           // NotationRecord / RecordSegment
#include "composing/analysis/joint/jointdecoder.h"                  // SegmentSlice (the §3.3 committed content score)

#include "engraving/dom/chord.h"
#include "engraving/dom/chordrest.h"
#include "engraving/dom/masterscore.h"
#include "engraving/dom/note.h"
#include "engraving/dom/segment.h"
#include "engraving/dom/staff.h"

#include "engraving/tests/utils/scorerw.h"

#include "notation/internal/notationcomposingbridge.h"

#include "test_helpers.h"

using namespace mu::engraving;

namespace an = mu::composing::analysis;
namespace joint = mu::composing::analysis::joint;

namespace {

// The two fixtures the record arm is pinned on (both decode to a non-empty record — the same fixtures
// the tuning/implode record-arm tests use). Named per the dispatch's "≥2 corpus scores".
const std::vector<String> kFixtures = {
    u"harmony_pinning_i_iv_v_i.mscx",
    u"implode_half_measure_harmony_changes.mscx",
};

// RAII: turn the record arm ON for a test and restore OFF on scope exit — so a failed ASSERT cannot
// leak the flag into the rest of the suite (which must stay byte-identical on the legacy arm).
struct RecordArmFlag {
    std::shared_ptr<mu::composing::IComposingAnalysisConfiguration> cfg{ analysisConfig() };
    RecordArmFlag()
    {
        if (cfg) {
            cfg->setUseRegionalAccumulation(true);
            cfg->setUseJointNotationRecord(true);
        }
    }
    ~RecordArmFlag()
    {
        if (cfg) {
            cfg->setUseJointNotationRecord(false);
        }
    }
};

// Every ChordRest note in the score, in (staffIdx, tick) order (first note per position).
struct NoteAt { int tick; Note* note; };
std::vector<NoteAt> collectNotes(MasterScore* score)
{
    std::vector<NoteAt> out;
    std::set<std::pair<int, int> > seen;
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
            const int staffIdx = static_cast<int>(track2staff(t));
            const int tick = seg->tick().ticks();
            if (seen.emplace(staffIdx, tick).second) {
                out.push_back({ tick, notes.front() });
            }
        }
    }
    return out;
}

// The §3.3 committed content score of a slice (the value the "(%.2f)" suffix shows), or 0 when absent.
double committedContentScore(const joint::SegmentSlice* slice)
{
    if (!slice) {
        return 0.0;
    }
    const joint::PosteriorAxis& ax = slice->chordAxis;
    if (ax.committed < 0 || ax.committed >= static_cast<int>(ax.scores.size())) {
        return 0.0;
    }
    return ax.scores[static_cast<size_t>(ax.committed)];
}

// The record the note-seam funnel ACTUALLY produces: a whole-score decode with the fixture's chord-track
// staves EXCLUDED from the analysis input (OI-204 — analyzeNoteHarmonicContext[Details] threads
// chordTrackExcludeStaves into produceNotationRecord; the reference here must use the SAME exclusion for
// arm-for-arm input parity). Both fixtures carry a populated chord track ("Chord Track Piano" /
// "Chord Track Treble+Bass"), so an empty-exclusion reference would re-analyze the chord track's own
// notes and its committed content scores would diverge from the funnel's — hence the shared helper (#6).
joint::NotationRecordResult produceFunnelRecord(MasterScore* score)
{
    return joint::produceNotationRecord(score, "noteseam", mu::notation::chordTrackExcludeStaves(score));
}

} // namespace

class NotationNoteSeamRecordArm : public ::testing::Test {};

// ── Pin 1: the carriage IS the record's committed reading at each note's tick ────────────────────
//
// For every note, the record-arm carriage (chordResults[0] + key) must equal the record's OWN
// committed segment containing that note's tick — the note seam is a VIEW into the record (#6),
// carrying the record's published facts, not the legacy analysis.
TEST_F(NotationNoteSeamRecordArm, CarriageEqualsRecordCommittedFacts)
{
    RecordArmFlag arm;
    ASSERT_TRUE(arm.cfg) << "IComposingAnalysisConfiguration not registered";

    for (const String& fixture : kFixtures) {
        MasterScore* score = ScoreRW::readScore(fixture);
        ASSERT_TRUE(score) << "failed to read fixture";

        const joint::NotationRecordResult rec = produceFunnelRecord(score);
        ASSERT_TRUE(rec.ok) << "produceNotationRecord failed";
        ASSERT_FALSE(rec.record.segments.empty()) << "record has no segments";

        const std::vector<NoteAt> notes = collectNotes(score);
        ASSERT_FALSE(notes.empty());

        int checked = 0;
        for (const NoteAt& na : notes) {
            const joint::NoteView nv = joint::noteView(rec.record, na.tick);
            ASSERT_TRUE(nv.found && nv.segment) << "no record segment at a note tick (whole-score span)";

            const mu::notation::NoteHarmonicContext ctx = mu::notation::analyzeNoteHarmonicContextDetails(na.note);
            ASSERT_FALSE(ctx.chordResults.empty()) << "record arm produced no chordResults at a note";

            const an::ChordAnalysisResult& top = ctx.chordResults.front();
            // committed identity + key equal the record segment's published facts.
            EXPECT_EQ(top.identity.rootPc, nv.segment->rootPc.value_or(-1));
            EXPECT_EQ(top.function.keyTonicPc, nv.segment->tonicPc);
            EXPECT_EQ(ctx.keyFifths, nv.segment->keySignatureFifths);
            const an::KeySigMode expectMode =
                nv.segment->isMajor ? an::KeySigMode::Ionian : an::KeySigMode::Aeolian;
            EXPECT_EQ(ctx.keyMode, expectMode);
            // keyConfidence is the RAW §3.3 gap (nats) — a model-internal quantity, never a [0,1]
            // probability (it may be any finite value, incl. negative); we only pin it is finite.
            EXPECT_TRUE(std::isfinite(ctx.keyConfidence));
            // committed identity.score is the §3.3 committed content score (the "(%.2f)" suffix).
            EXPECT_DOUBLE_EQ(top.identity.score, committedContentScore(nv.slice));
            ++checked;
        }
        EXPECT_GT(checked, 0);
        delete score;
    }
}

// ── Pin 2: the view ordering — committed first, then descending §3.3 content score ───────────────
TEST_F(NotationNoteSeamRecordArm, CarriageOrderingCommittedThenDescendingScore)
{
    RecordArmFlag arm;
    ASSERT_TRUE(arm.cfg);

    for (const String& fixture : kFixtures) {
        MasterScore* score = ScoreRW::readScore(fixture);
        ASSERT_TRUE(score);

        const joint::NotationRecordResult rec = produceFunnelRecord(score);
        ASSERT_TRUE(rec.ok);

        for (const NoteAt& na : collectNotes(score)) {
            const joint::NoteView nv = joint::noteView(rec.record, na.tick);
            ASSERT_TRUE(nv.found && nv.segment);

            const mu::notation::NoteHarmonicContext ctx = mu::notation::analyzeNoteHarmonicContextDetails(na.note);
            ASSERT_FALSE(ctx.chordResults.empty());

            // chordResults[0] is the committed reading (== the record segment's root).
            EXPECT_EQ(ctx.chordResults.front().identity.rootPc, nv.segment->rootPc.value_or(-1));
            // chordResults[1..] are the §3.3 alternatives, non-increasing in content score.
            for (size_t k = 2; k < ctx.chordResults.size(); ++k) {
                EXPECT_GE(ctx.chordResults[k - 1].identity.score, ctx.chordResults[k].identity.score)
                    << "alternatives not sorted by descending §3.3 content score";
            }
        }
        delete score;
    }
}

// ── Pin 3: the STATUS BAR renders the carriage's committed symbol ────────────────────────────────
TEST_F(NotationNoteSeamRecordArm, StatusBarRendersRecordCommittedSymbol)
{
    RecordArmFlag arm;
    ASSERT_TRUE(arm.cfg);
    arm.cfg->setAnalyzeForChordSymbols(true);
    arm.cfg->setAnalyzeForChordFunction(true);
    arm.cfg->setShowChordSymbolsInStatusBar(true);
    arm.cfg->setShowKeyModeInStatusBar(true);
    arm.cfg->setAnalysisAlternatives(3);

    MasterScore* score = ScoreRW::readScore(kFixtures.front());
    ASSERT_TRUE(score);

    int rendered = 0;
    for (const NoteAt& na : collectNotes(score)) {
        const mu::notation::NoteHarmonicContext ctx = mu::notation::analyzeNoteHarmonicContextDetails(na.note);
        if (ctx.chordResults.empty()) {
            continue;
        }
        const mu::notation::FormattedChordResult fmt =
            mu::notation::formatChordResultForStatusBar(score, ctx.chordResults.front(), ctx.keyFifths);
        if (fmt.symbol.empty()) {
            continue;   // a rootless chromatic committed class renders no symbol — nothing to find
        }
        const std::string annotation = mu::notation::harmonicAnnotation(na.note);
        EXPECT_NE(annotation.find(fmt.symbol), std::string::npos)
            << "status bar did not render the record-committed symbol '" << fmt.symbol << "'";
        ++rendered;
    }
    EXPECT_GT(rendered, 0) << "no note rendered a status-bar symbol";
    delete score;
}

// ── Pin 4: the HARMONY WRITE (notationinteraction path) uses the carriage ────────────────────────
//
// Replicates addAnalyzedHarmonyToSelection's steps 2–3 (analyzeNoteHarmonicContext -> format), the
// same replication the harmony-pinning suite uses. The written text is the record carriage's top
// reading formatted — equal to the record's committed segment.
TEST_F(NotationNoteSeamRecordArm, HarmonyWriteUsesRecordCarriage)
{
    RecordArmFlag arm;
    ASSERT_TRUE(arm.cfg);

    MasterScore* score = ScoreRW::readScore(kFixtures.front());
    ASSERT_TRUE(score);

    const joint::NotationRecordResult rec = produceFunnelRecord(score);
    ASSERT_TRUE(rec.ok);

    int checked = 0;
    for (const NoteAt& na : collectNotes(score)) {
        int keyFifths = 0;
        an::KeySigMode keyMode = an::KeySigMode::Ionian;
        const auto results = mu::notation::analyzeNoteHarmonicContext(na.note, keyFifths, keyMode);
        if (results.empty()) {
            continue;
        }
        const joint::NoteView nv = joint::noteView(rec.record, na.tick);
        ASSERT_TRUE(nv.found && nv.segment);
        // the write consumes results[0] — the record's committed reading.
        EXPECT_EQ(results.front().identity.rootPc, nv.segment->rootPc.value_or(-1));
        // the rendered STANDARD symbol equals the record-committed segment's own rendered symbol.
        const std::string written =
            mu::notation::formatChordResultForStatusBar(score, results.front(), keyFifths).symbol;
        const std::string fromRecord =
            mu::notation::formatChordResultForStatusBar(
                score, an::chordResultFromRecordSegment(*nv.segment, committedContentScore(nv.slice)),
                nv.segment->keySignatureFifths).symbol;
        EXPECT_EQ(written, fromRecord);
        ++checked;
    }
    EXPECT_GT(checked, 0);
    delete score;
}

// ── Pin 5: the CONTEXT MENU score suffix is the §3.3 committed content score ─────────────────────
//
// Replicates appendAnalysisItemsForContext's per-result formatting: the menu formats each carriage
// entry and appends " (score)" from identity.score. The pin: the committed entry's score is the
// record's §3.3 committed content score (the audited score-suffix disposition).
TEST_F(NotationNoteSeamRecordArm, ContextMenuScoreSuffixIsRecordContentScore)
{
    RecordArmFlag arm;
    ASSERT_TRUE(arm.cfg);

    MasterScore* score = ScoreRW::readScore(kFixtures.front());
    ASSERT_TRUE(score);

    const joint::NotationRecordResult rec = produceFunnelRecord(score);
    ASSERT_TRUE(rec.ok);

    int checked = 0;
    for (const NoteAt& na : collectNotes(score)) {
        const mu::notation::NoteHarmonicContext ctx = mu::notation::analyzeNoteHarmonicContextDetails(na.note);
        if (ctx.chordResults.empty()) {
            continue;
        }
        const joint::NoteView nv = joint::noteView(rec.record, na.tick);
        ASSERT_TRUE(nv.found && nv.segment);
        // the menu builds its leaves + the "(%.2f)" suffix from ctx.chordResults; the committed
        // entry's score is the record's §3.3 committed content score.
        EXPECT_DOUBLE_EQ(ctx.chordResults.front().identity.score, committedContentScore(nv.slice));
        // and the menu formats the committed symbol from the carriage (same formatter as the menu).
        const std::string sym = an::ChordSymbolFormatter::formatSymbol(ctx.chordResults.front(), ctx.keyFifths);
        const std::string fromRecord = an::ChordSymbolFormatter::formatSymbol(
            an::chordResultFromRecordSegment(*nv.segment, committedContentScore(nv.slice)),
            nv.segment->keySignatureFifths);
        EXPECT_EQ(sym, fromRecord);
        ++checked;
    }
    EXPECT_GT(checked, 0);
    delete score;
}

// ── Pin 6: the edges — nothing written on an out-of-span tick or a produce failure (#13) ─────────
TEST_F(NotationNoteSeamRecordArm, EdgesYieldNothingNoPartial)
{
    RecordArmFlag arm;
    ASSERT_TRUE(arm.cfg);

    MasterScore* score = ScoreRW::readScore(kFixtures.front());
    ASSERT_TRUE(score);

    const joint::NotationRecordResult rec = produceFunnelRecord(score);
    ASSERT_TRUE(rec.ok);
    ASSERT_FALSE(rec.record.segments.empty());

    // (a) OUT-OF-SPAN at the record level: a tick at/after the analyzed span end is in no segment
    //     (noteView uses startTick <= tick < endTick), so the record arm has no reading.
    const int spanEnd = rec.record.spanEndTick;
    EXPECT_FALSE(joint::noteView(rec.record, spanEnd).found);
    EXPECT_FALSE(joint::noteView(rec.record, spanEnd + 1920).found);

    // (b) NOTHING WRITTEN for an out-of-range query tick (well past the score): the note seam returns
    //     an empty context — no chordResults, no partial output.
    const mu::notation::NoteHarmonicContext beyond =
        mu::notation::analyzeHarmonicContextAtTick(score, Fraction::fromTicks(spanEnd + 100000), 0, {});
    EXPECT_TRUE(beyond.chordResults.empty()) << "out-of-range tick produced a partial reading";

    // (c) PRODUCE FAILURE: the producer returns an unambiguous failure (ok == false) for an
    //     unextractable score (a null score); the record-arm branch consumes that as return-empty
    //     (no partial, no legacy fallback — the record IS the surface, A2/#13). The note seam's own
    //     null-score guard also returns empty, so a produce failure never yields partial output.
    EXPECT_FALSE(joint::produceNotationRecord(nullptr, "noteseam").ok);
    const mu::notation::NoteHarmonicContext nullCtx =
        mu::notation::analyzeHarmonicContextAtTick(nullptr, Fraction(0, 1), 0, {});
    EXPECT_TRUE(nullCtx.chordResults.empty());

    delete score;
}
