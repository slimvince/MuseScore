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

// Joint estimator — the §3.4 UN-ROUNDED MODAL READING (contract §3.4 / §5.4) coverage tests for
// joint::computeModalReading. (a) a synthetic D-minor key run with HAND-COUNTED expectations +
// determinism; (b) the bwv254 hand-check — the genuinely modal desk-sim piece: the D-minor
// variable-degree cells (the B♭/B♮ degree-6 and C♯/C♮ degree-7 traffic) verified against an
// INDEPENDENT pitch-class count of the piece's notated notes. The module stays DORMANT.

#include <gtest/gtest.h>

#include <map>
#include <memory>
#include <optional>
#include <string>
#include <vector>

#include "composing/analysis/joint/jointnotationrecord.h"
#include "composing/analysis/joint/jointweights.h"

#ifndef JOINT_ARTIFACT_DIR
#define JOINT_ARTIFACT_DIR "."
#endif

namespace joint = mu::composing::analysis::joint;

namespace {
const joint::ModalDegree* findDegree(const joint::ModalKeyRun& run, int degree)
{
    for (const joint::ModalDegree& d : run.degrees) {
        if (d.degree == degree) {
            return &d;
        }
    }
    return nullptr;
}
const joint::ModalInflection* findInfl(const joint::ModalDegree& d, int pcOffset)
{
    for (const joint::ModalInflection& inf : d.inflections) {
        if (inf.pcOffset == pcOffset) {
            return &inf;
        }
    }
    return nullptr;
}
} // namespace

// ── (a) a synthetic D-minor run with hand-counted expectations + determinism ──────────────────────
TEST(JointModalTests, SyntheticRunHandCounted)
{
    // one D-minor segment spanning [0, 1920). Notes: Bb x2 (♭6), C x1 (♭7), C# x1 (leading tone).
    joint::Piece piece;
    piece.stem = "synthetic";
    auto addNote = [&](int onset, int dur, int pc, int lof) {
        joint::NoteRec n;
        n.onset = onset; n.dur = dur; n.pc = pc; n.lof = lof; n.midi = 60 + pc; n.measure = 1;
        piece.notes.push_back(n);
    };
    addNote(0, 480, 10, -2);     // Bb (♭6 of D)
    addNote(480, 480, 10, -2);   // Bb
    addNote(960, 240, 0, 0);     // C  (♭7 subtonic)
    addNote(1440, 480, 1, 7);    // C# (leading tone)

    joint::SegmentSummary s;
    s.i = 0; s.j = 1; s.startTick = 0; s.endTick = 1920; s.tonicPc = 2; s.isMajor = false;
    s.classKey = "I | Min |  | ";
    joint::DecodeResult r;
    r.segments.push_back(s);

    const std::vector<joint::ModalKeyRun> runs = joint::computeModalReading(piece, r, -1);
    ASSERT_EQ(runs.size(), 1u);
    const joint::ModalKeyRun& run = runs[0];
    EXPECT_EQ(run.tonicPc, 2);
    EXPECT_FALSE(run.isMajor);
    EXPECT_EQ(run.startTick, 0);
    EXPECT_EQ(run.endTick, 1920);

    // degree 6: only ♭6 (Bb, pcOffset 8), 2 onsets / 960 ticks
    const joint::ModalDegree* d6 = findDegree(run, 6);
    ASSERT_NE(d6, nullptr);
    ASSERT_EQ(d6->inflections.size(), 1u);
    const joint::ModalInflection* bb = findInfl(*d6, 8);
    ASSERT_NE(bb, nullptr);
    EXPECT_EQ(bb->onsetCount, 2);
    EXPECT_EQ(bb->durationTicks, 960);
    EXPECT_EQ(bb->notatedLofOffset, -4);   // Bb tonal offset from D

    // degree 7: ♭7 (C, pcOffset 10) 1/240 AND leading tone (C#, pcOffset 11) 1/480
    const joint::ModalDegree* d7 = findDegree(run, 7);
    ASSERT_NE(d7, nullptr);
    ASSERT_EQ(d7->inflections.size(), 2u);
    const joint::ModalInflection* cnat = findInfl(*d7, 10);
    const joint::ModalInflection* csharp = findInfl(*d7, 11);
    ASSERT_NE(cnat, nullptr);
    ASSERT_NE(csharp, nullptr);
    EXPECT_EQ(cnat->onsetCount, 1);
    EXPECT_EQ(cnat->durationTicks, 240);
    EXPECT_EQ(csharp->onsetCount, 1);
    EXPECT_EQ(csharp->durationTicks, 480);

    // determinism: recomputing yields the identical structure
    const std::vector<joint::ModalKeyRun> again = joint::computeModalReading(piece, r, -1);
    ASSERT_EQ(again.size(), 1u);
    ASSERT_EQ(again[0].degrees.size(), run.degrees.size());
}

// ── (b) bwv254 hand-check: the D-minor degree-6/7 traffic vs an INDEPENDENT pc count ──────────────
TEST(JointModalTests, Bwv254DorianVariableDegrees)
{
    const std::string dir = JOINT_ARTIFACT_DIR;
    joint::LoadedCorpus corpus = joint::loadPiecesFromNoteEvents(dir + "/note_events/note_events.json");
    ASSERT_TRUE(corpus.ok);
    ASSERT_TRUE(corpus.pieces.count("bwv254"));
    joint::Piece& piece = corpus.pieces.at("bwv254");

    joint::FittedAdapter adapter = joint::FittedAdapter::loadEmbedded(joint::selectedWeights());
    ASSERT_TRUE(adapter.loaded());
    joint::Vocabulary vocab(adapter.tables());
    joint::ChordCache cache;
    // decode with bwv254's OWN notated prior inputs (sig 0, declared minor) — the committed decode.
    const joint::DecodeResult r = joint::decodePiece(piece, adapter, vocab, cache, 4,
                                                     std::optional<int>(0), "minor");
    const std::vector<joint::ModalKeyRun> runs = joint::computeModalReading(piece, r, 0);

    // aggregate the D-minor runs (tonic pc 2, minor): degree 6 (B letter) + degree 7 (C letter).
    // pcOffsets in D minor: ♭6 Bb=8, ♮6 B=9, ♭7 C=10, leading-tone C#=11.
    std::map<int, std::pair<int, long long> > agg;   // pcOffset -> (onsets, ticks)
    std::vector<std::pair<int, int> > dminSpans;
    for (const joint::ModalKeyRun& run : runs) {
        if (run.tonicPc != 2 || run.isMajor) {
            continue;
        }
        dminSpans.emplace_back(run.startTick, run.endTick);
        for (int deg : { 6, 7 }) {
            const joint::ModalDegree* d = findDegree(run, deg);
            if (!d) {
                continue;
            }
            for (const joint::ModalInflection& inf : d->inflections) {
                agg[inf.pcOffset].first += inf.onsetCount;
                agg[inf.pcOffset].second += inf.durationTicks;
            }
        }
    }
    ASSERT_FALSE(dminSpans.empty()) << "no D-minor key run in the bwv254 decode";

    // INDEPENDENT count: notes (by pitch class, not by the degree logic) onsetting in a D-minor run.
    std::map<int, std::pair<int, long long> > indep;   // pcOffset -> (onsets, ticks)
    for (const joint::NoteRec& n : piece.notes) {
        if (n.measure == 0) {
            continue;
        }
        bool inRun = false;
        for (const auto& sp : dminSpans) {
            if (n.onset >= sp.first && n.onset < sp.second) { inRun = true; break; }
        }
        if (!inRun) {
            continue;
        }
        const int off = (((n.pc - 2) % 12) + 12) % 12;
        if (off == 8 || off == 9 || off == 10 || off == 11) {   // degree 6/7 pitch classes
            indep[off].first += 1;
            indep[off].second += n.dur;
        }
    }

    // the counter's degree-6/7 cells must equal the independent pc count, cell by cell.
    for (int off : { 8, 9, 10, 11 }) {
        EXPECT_EQ(agg[off].first, indep[off].first) << "pcOffset " << off << " onset count";
        EXPECT_EQ(agg[off].second, indep[off].second) << "pcOffset " << off << " duration";
    }
    // and the qualitative modal facts the desk-sim expects: degree 6 is all ♭6 (Bb), degree 7 uses
    // BOTH the subtonic (C) and the leading tone (C#).
    EXPECT_GT(agg[8].first, 0) << "no ♭6 (Bb) in D-minor runs";
    EXPECT_EQ(agg[9].first, 0) << "unexpected raised 6 (B natural) in D-minor runs";
    EXPECT_GT(agg[11].first, 0) << "no leading tone (C#) in D-minor runs";
}
