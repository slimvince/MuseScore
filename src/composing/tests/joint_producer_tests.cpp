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

// Joint estimator — the RECORD-PRODUCING ENTRY + the two seam views (notation output-surface contract
// §1). Coverage for joint::produceNotationRecord (score->record and its facts->record core), and the
// span/note views. The producer composes only established parts, so the tests assert (a) internal
// consistency — the produced record equals the same decode assembled BY PARTS — plus a spot-check of the
// committed segment fields against decode_parity_ref.json's selected arm; (b) the score->record wrapper
// equals buildAdapterFacts + the core on a real .mscx; (c) the adapter-failure path returns an
// unambiguous failure; (d) the view semantics (overlap; the boundary rule; the edge duties) on a
// hand-built record. DORMANT: nothing in src/ reads the producer or the views.

#include <gtest/gtest.h>

#include <memory>
#include <optional>
#include <set>
#include <string>
#include <vector>

#include "composing/analysis/joint/jointnotationproducer.h"
#include "composing/analysis/joint/jointnotationrecord.h"
#include "composing/analysis/joint/jointfactadapter.h"
#include "composing/analysis/joint/jointweights.h"
#include "composing/analysis/joint/jointembeddedartifacts.h"

#include "engraving/dom/masterscore.h"
#include "engraving/tests/utils/scorerw.h"

#ifndef JOINT_ARTIFACT_DIR
#define JOINT_ARTIFACT_DIR "."
#endif

namespace joint = mu::composing::analysis::joint;
using mu::engraving::MasterScore;
using mu::engraving::ScoreRW;

namespace {
// The committed note_events corpus + the embedded production adapter — the "by parts" reference.
struct Fixture {
    joint::LoadedCorpus corpus;
    joint::FittedAdapter adapter;
    std::unique_ptr<joint::Vocabulary> vocab;
    joint::ChordCache cache;
    bool ok = false;
};

Fixture load()
{
    Fixture f;
    const std::string dir = JOINT_ARTIFACT_DIR;
    f.corpus = joint::loadPiecesFromNoteEvents(dir + "/note_events/note_events.json");
    if (!f.corpus.ok) {
        return f;
    }
    f.adapter = joint::FittedAdapter::loadEmbedded(joint::selectedWeights());
    if (!f.adapter.loaded()) {
        return f;
    }
    f.vocab = std::make_unique<joint::Vocabulary>(f.adapter.tables());
    f.ok = true;
    return f;
}

// Assert two records are structurally identical (the producer must equal the parts-assembled record).
void expectRecordsEqual(const joint::NotationRecord& a, const joint::NotationRecord& b,
                        const std::string& ctx)
{
    ASSERT_EQ(a.segments.size(), b.segments.size()) << ctx;
    ASSERT_EQ(a.slices.size(), b.slices.size()) << ctx;
    ASSERT_EQ(a.modalReading.size(), b.modalReading.size()) << ctx;
    EXPECT_EQ(a.spanStartTick, b.spanStartTick) << ctx;
    EXPECT_EQ(a.spanEndTick, b.spanEndTick) << ctx;
    EXPECT_EQ(a.sigFifths, b.sigFifths) << ctx;
    EXPECT_EQ(a.declaredMode, b.declaredMode) << ctx;
    for (size_t i = 0; i < a.segments.size(); ++i) {
        const joint::RecordSegment& x = a.segments[i];
        const joint::RecordSegment& y = b.segments[i];
        const std::string sc = ctx + " seg " + std::to_string(i);
        EXPECT_EQ(x.startTick, y.startTick) << sc;
        EXPECT_EQ(x.endTick, y.endTick) << sc;
        EXPECT_EQ(x.tonicPc, y.tonicPc) << sc;
        EXPECT_EQ(x.isMajor, y.isMajor) << sc;
        EXPECT_EQ(x.key, y.key) << sc;
        EXPECT_EQ(x.classKey, y.classKey) << sc;
        EXPECT_EQ(x.degree, y.degree) << sc;
        EXPECT_EQ(x.quality, y.quality) << sc;
        EXPECT_EQ(x.inversion, y.inversion) << sc;
        EXPECT_EQ(x.target, y.target) << sc;
        EXPECT_EQ(x.rootPc, y.rootPc) << sc;
        EXPECT_EQ(x.keySignatureFifths, y.keySignatureFifths) << sc;
        EXPECT_EQ(x.rootSpellingLof, y.rootSpellingLof) << sc;
        EXPECT_EQ(x.memberPcs, y.memberPcs) << sc;
        EXPECT_EQ(x.chordSymbol, y.chordSymbol) << sc;
        EXPECT_EQ(x.romanNumeral, y.romanNumeral) << sc;
        EXPECT_EQ(x.diatonicToKey, y.diatonicToKey) << sc;
        EXPECT_EQ(x.augSixthSubType, y.augSixthSubType) << sc;
        EXPECT_EQ(x.members.size(), y.members.size()) << sc;
        EXPECT_EQ(x.bassPerEvent.size(), y.bassPerEvent.size()) << sc;
    }
    for (size_t i = 0; i < a.slices.size(); ++i) {
        const std::string sc = ctx + " slice " + std::to_string(i);
        EXPECT_EQ(a.slices[i].keyAxis.committed, b.slices[i].keyAxis.committed) << sc;
        EXPECT_EQ(a.slices[i].chordAxis.committed, b.slices[i].chordAxis.committed) << sc;
        EXPECT_EQ(a.slices[i].keyAxis.labels.size(), b.slices[i].keyAxis.labels.size()) << sc;
        EXPECT_EQ(a.slices[i].chordAxis.labels.size(), b.slices[i].chordAxis.labels.size()) << sc;
    }
}

// Build a hand-made 3-segment record with known ticks for the view semantics tests. Segments are
// contiguous: [0,480), [480,960), [960,1440); one (empty) slice per segment; span [0,1440).
joint::NotationRecord threeSegmentRecord()
{
    joint::NotationRecord rec;
    rec.stem = "synthetic";
    rec.spanStartTick = 0;
    rec.spanEndTick = 1440;
    const int bounds[3][2] = { { 0, 480 }, { 480, 960 }, { 960, 1440 } };
    for (int i = 0; i < 3; ++i) {
        joint::RecordSegment s;
        s.startTick = bounds[i][0];
        s.endTick = bounds[i][1];
        s.tonicPc = 0;
        s.isMajor = true;
        s.classKey = "seg" + std::to_string(i);
        rec.segments.push_back(s);
        rec.slices.push_back(joint::SegmentSlice{});
    }
    return rec;
}

// one expected committed segment field-set from decode_parity_ref.json's selected arm.
struct ExpectSeg { int tonicPc; bool isMajor; const char* classKey; int rootPc; };
} // namespace

// ── (a) the producer core on ≥2 corpus pieces: equals the parts-assembled record + spot-check ─────────
TEST(JointProducerTests, CoreMatchesPartsAndReferenceOnCorpusPieces)
{
    Fixture f = load();
    ASSERT_TRUE(f.ok) << "corpus/adapter load failed";

    struct Case { const char* stem; int sig; const char* mode; std::vector<ExpectSeg> first2; };
    const std::vector<Case> cases = {
        // decode_parity_ref.json selected arm (the committed decode inputs + first two segments)
        { "bwv324", 1, "minor",
          { { 4, false, "I | Min |  | ", 4 }, { 4, false, "V | Maj |  | III", 2 } } },
        { "bwv362", -2, "major",
          { { 10, true, "VI | Min |  | ", 7 }, { 10, true, "VI | Min |  | ", 7 } } },
    };

    for (const Case& c : cases) {
        ASSERT_TRUE(f.corpus.pieces.count(c.stem)) << c.stem;
        joint::Piece& piece = f.corpus.pieces.at(c.stem);
        const std::optional<int> sig(c.sig);

        // by parts: the SAME decode the producer runs, assembled directly.
        const joint::DecodeResult r =
            joint::decodePiece(piece, f.adapter, *f.vocab, f.cache, 4, sig, c.mode);
        const joint::NotationRecord recParts =
            joint::assembleNotationRecord(piece, r, sig, c.mode, f.adapter, *f.vocab, f.cache);

        // the producer core (loads its OWN embedded adapter/tables internally).
        const joint::NotationRecordResult res = joint::produceNotationRecord(piece, sig, c.mode);
        ASSERT_TRUE(res.ok) << c.stem << ": " << res.error;

        expectRecordsEqual(res.record, recParts, c.stem);

        // spot-check the first two committed segments against the decode_parity_ref oracle.
        ASSERT_GE(res.record.segments.size(), c.first2.size()) << c.stem;
        for (size_t i = 0; i < c.first2.size(); ++i) {
            const joint::RecordSegment& rs = res.record.segments[i];
            EXPECT_EQ(rs.tonicPc, c.first2[i].tonicPc) << c.stem << " seg " << i;
            EXPECT_EQ(rs.isMajor, c.first2[i].isMajor) << c.stem << " seg " << i;
            EXPECT_EQ(rs.classKey, std::string(c.first2[i].classKey)) << c.stem << " seg " << i;
            EXPECT_EQ(rs.rootPc, std::optional<int>(c.first2[i].rootPc)) << c.stem << " seg " << i;
        }
        // the first segment begins the analyzed span; provenance is the embedded block.
        EXPECT_EQ(res.record.segments.front().startTick, res.record.spanStartTick) << c.stem;
        EXPECT_EQ(res.record.provenance.tableArtifacts.size(), joint::embedded::kTableArtifacts.size())
            << c.stem;
    }
}

// ── (b) the score->record wrapper equals buildAdapterFacts + the core on a real .mscx ─────────────────
TEST(JointProducerTests, ScoreWrapperEqualsFactsPlusCore)
{
    Fixture f = load();
    ASSERT_TRUE(f.ok);

    MasterScore* sc = ScoreRW::readScore(u"data/pb_chorale.mscx");
    ASSERT_TRUE(sc) << "failed to read pb_chorale.mscx";

    const joint::AdapterFacts fx = joint::buildAdapterFacts(sc, "pb_chorale");
    ASSERT_TRUE(fx.ok) << fx.error;

    const joint::NotationRecordResult res = joint::produceNotationRecord(sc, "pb_chorale");
    ASSERT_TRUE(res.ok) << res.error;
    // a well-formed record: the analyzed span is set and the D1 provenance block is present.
    EXPECT_EQ(res.record.provenance.tableArtifacts.size(), joint::embedded::kTableArtifacts.size());
    EXPECT_GT(res.record.spanEndTick, res.record.spanStartTick);
    EXPECT_FALSE(res.record.segments.empty());

    // the wrapper must equal buildAdapterFacts + the facts->record core (same piece + prior inputs).
    const joint::NotationRecordResult core =
        joint::produceNotationRecord(fx.piece, fx.sigFifths, fx.declaredMode);
    ASSERT_TRUE(core.ok) << core.error;
    expectRecordsEqual(res.record, core.record, "pb_chorale wrapper==core");

    delete sc;
}

// ── (b2, OI-204) input-scoping: excludeStaves drops the named staves' notes from the fact surface ─────
// The producer's excludeStaves parameter (forwarded to buildAdapterFacts) is the OI-204 fix: an excluded
// staff's notes never enter the L1 fact surface the decode reads (no self-feedback on a populated chord
// track). Establishment, both directions:
//   * the EXCLUSION works — nm_two_staff sounds C5 (midi 72) on staff 0 and C3 (midi 48) on staff 1 (one
//     Piano part, two staves); excluding staff 1 removes exactly the midi-48 notes from the facts while
//     keeping midi-72, and the note count drops. The default/explicit-empty set keeps both.
//   * the exclusion CHANGES the decode — pb_chorale (4-staff SATB) with the bass staff (index 3, 59
//     notes) excluded yields a record that differs from the full-score record (fewer notes decoded ->
//     different committed reading), while the empty-set produce equals the default produce (byte-identical).
TEST(JointProducerTests, ExcludeStavesScopesTheFactSurfaceAndDecode)
{
    // ── the exclusion removes exactly the named staff's notes from the fact surface ──
    MasterScore* two = ScoreRW::readScore(u"data/nm_two_staff.mscx");
    ASSERT_TRUE(two) << "failed to read nm_two_staff.mscx";

    const joint::AdapterFacts full = joint::buildAdapterFacts(two, "nm_two_staff", {});
    ASSERT_TRUE(full.ok) << full.error;
    auto hasMidi = [](const joint::Piece& p, int midi) {
        for (const joint::NoteRec& n : p.notes) { if (n.midi == midi) { return true; } }
        return false;
    };
    // fixture preconditions: staff-0 C5 (72) and staff-1 C3 (48) both sound (else the test is vacuous).
    ASSERT_TRUE(hasMidi(full.piece, 72)) << "fixture precondition: staff-0 C5 must sound";
    ASSERT_TRUE(hasMidi(full.piece, 48)) << "fixture precondition: staff-1 C3 must sound";

    const joint::AdapterFacts excl = joint::buildAdapterFacts(two, "nm_two_staff", { size_t(1) });
    ASSERT_TRUE(excl.ok) << excl.error;
    EXPECT_TRUE(hasMidi(excl.piece, 72)) << "staff-0 note must survive exclusion of staff 1";
    EXPECT_FALSE(hasMidi(excl.piece, 48)) << "the excluded staff's note leaked into the fact surface";
    EXPECT_LT(excl.piece.notes.size(), full.piece.notes.size()) << "exclusion must drop notes";

    // the default-argument call equals the explicit empty set (the empty set skips nothing).
    const joint::AdapterFacts dflt = joint::buildAdapterFacts(two, "nm_two_staff");
    ASSERT_TRUE(dflt.ok);
    EXPECT_EQ(dflt.piece.notes.size(), full.piece.notes.size());
    delete two;

    // ── the exclusion changes the produced decode (harmonically load-bearing staff removed) ──
    MasterScore* sc = ScoreRW::readScore(u"data/pb_chorale.mscx");
    ASSERT_TRUE(sc) << "failed to read pb_chorale.mscx";

    const joint::NotationRecordResult recFull = joint::produceNotationRecord(sc, "pb_chorale", {});
    const joint::NotationRecordResult recDflt = joint::produceNotationRecord(sc, "pb_chorale");
    const joint::NotationRecordResult recExcl = joint::produceNotationRecord(sc, "pb_chorale", { size_t(3) });
    ASSERT_TRUE(recFull.ok) << recFull.error;
    ASSERT_TRUE(recDflt.ok) << recDflt.error;
    ASSERT_TRUE(recExcl.ok) << recExcl.error;

    // the empty-set produce equals the default produce (byte-identical extraction + decode).
    expectRecordsEqual(recFull.record, recDflt.record, "pb_chorale empty==default");

    // excluding the bass staff changes the record: some committed reading (segment count, span, or
    // committed class) must differ — removing a chorale's bass line cannot leave the decode identical.
    bool differs = recFull.record.segments.size() != recExcl.record.segments.size();
    for (size_t i = 0; !differs && i < recFull.record.segments.size(); ++i) {
        const joint::RecordSegment& a = recFull.record.segments[i];
        const joint::RecordSegment& b = recExcl.record.segments[i];
        differs = a.startTick != b.startTick || a.endTick != b.endTick
                  || a.classKey != b.classKey || a.tonicPc != b.tonicPc;
    }
    EXPECT_TRUE(differs) << "excluding the bass staff must change the decode";
    delete sc;
}

// ── (c) the adapter-failure path: an unambiguous failure, no partial record (#13) ─────────────────────
TEST(JointProducerTests, FailurePathOnNullScore)
{
    const joint::NotationRecordResult res = joint::produceNotationRecord(nullptr, "none");
    EXPECT_FALSE(res.ok);
    EXPECT_FALSE(res.error.empty());
    EXPECT_TRUE(res.record.segments.empty());   // no partial record
    EXPECT_TRUE(res.record.slices.empty());
}

// ── (d1) the span view: overlap semantics, span-splitting, and the empty-span edge duty ───────────────
TEST(JointProducerTests, SpanViewOverlapSemantics)
{
    const joint::NotationRecord rec = threeSegmentRecord();

    EXPECT_EQ(joint::spanViewSegments(rec, 0, 1440), (std::vector<int>{ 0, 1, 2 }));   // whole span
    EXPECT_EQ(joint::spanViewSegments(rec, 0, 480), (std::vector<int>{ 0 }));          // exactly seg 0
    EXPECT_EQ(joint::spanViewSegments(rec, 200, 300), (std::vector<int>{ 0 }));        // inside seg 0 (split)
    EXPECT_EQ(joint::spanViewSegments(rec, 400, 500), (std::vector<int>{ 0, 1 }));     // crosses the 480 boundary
    EXPECT_EQ(joint::spanViewSegments(rec, 480, 960), (std::vector<int>{ 1 }));        // exactly seg 1
    EXPECT_EQ(joint::spanViewSegments(rec, 950, 970), (std::vector<int>{ 1, 2 }));     // crosses the 960 boundary
    // edge duties: empty / degenerate / out-of-range spans select nothing
    EXPECT_TRUE(joint::spanViewSegments(rec, 1440, 1440).empty());                     // empty span (== spanEnd)
    EXPECT_TRUE(joint::spanViewSegments(rec, 500, 500).empty());                       // degenerate empty span
    EXPECT_TRUE(joint::spanViewSegments(rec, 600, 300).empty());                       // inverted span
    EXPECT_TRUE(joint::spanViewSegments(rec, -100, 0).empty());                        // before the piece
    EXPECT_TRUE(joint::spanViewSegments(rec, 1440, 2000).empty());                     // after the piece
}

// ── (d2) the note view: the containing-segment boundary rule, and the out-of-span edge duty ───────────
TEST(JointProducerTests, NoteViewBoundaryRule)
{
    const joint::NotationRecord rec = threeSegmentRecord();

    auto idxAt = [&](int t) { return joint::noteView(rec, t).segmentIndex; };
    EXPECT_EQ(idxAt(0), 0);       // seg 0 starts at 0
    EXPECT_EQ(idxAt(240), 0);     // inside seg 0
    EXPECT_EQ(idxAt(479), 0);     // last tick of seg 0
    EXPECT_EQ(idxAt(480), 1);     // boundary belongs to the segment it STARTS (seg 1)
    EXPECT_EQ(idxAt(960), 2);     // next boundary -> seg 2
    EXPECT_EQ(idxAt(1439), 2);    // last tick of seg 2

    // the containing view resolves the segment + slice pointers into the record (no copy, no recompute).
    const joint::NoteView v = joint::noteView(rec, 240);
    ASSERT_TRUE(v.found);
    EXPECT_EQ(v.segmentIndex, 0);
    EXPECT_EQ(v.segment, &rec.segments[0]);
    EXPECT_EQ(v.slice, &rec.slices[0]);

    // edge duty: a tick outside the analyzed span is not found (span end is exclusive).
    EXPECT_FALSE(joint::noteView(rec, 1440).found);   // == spanEnd
    EXPECT_FALSE(joint::noteView(rec, 5000).found);    // after
    EXPECT_FALSE(joint::noteView(rec, -1).found);       // before
    const joint::NoteView miss = joint::noteView(rec, -1);
    EXPECT_EQ(miss.segmentIndex, -1);
    EXPECT_EQ(miss.segment, nullptr);
    EXPECT_EQ(miss.slice, nullptr);
}
