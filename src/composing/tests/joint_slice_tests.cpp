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

// Joint estimator — the POSTERIOR SLICE (notation output-surface contract §3.3 group (i)) coverage
// tests for joint::computePosteriorSlice. The bit-identical parity against the Python reference is the
// batch driver's job (--joint-posterior-slice); THESE tests exercise the module-surface paths: the
// candidate-set structure (KEYS_24-order key axis / sorted chord axis), the committed-flag invariants,
// that every published score is bit-exactly segmentContentScore of that candidate (so the slice rests
// on the established Neumaier primitive), the scoreability filter, and the empty/degenerate guard.
// Read-only over the committed tools/joint_estimator/ artifacts; the module stays dormant.

#include <gtest/gtest.h>

#include <algorithm>
#include <memory>
#include <optional>
#include <string>
#include <vector>

#include "composing/analysis/joint/jointdecoder.h"

#ifndef JOINT_ARTIFACT_DIR
#define JOINT_ARTIFACT_DIR "."
#endif

namespace joint = mu::composing::analysis::joint;

namespace {
// probe_decoder._PC_KEYNAME (an INDEPENDENT test oracle for the key label, not the code-under-test's
// jointprimitives::pcKeyName — kept deliberately separate so the test checks the derived label).
const char* const kPcKeyName[12] = { "C", "Db", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B" };
std::string keyLabel(int tonic, bool major)
{
    return std::string(kPcKeyName[((tonic % 12) + 12) % 12]) + (major ? "maj" : "min");
}

struct Fixture {
    joint::LoadedCorpus corpus;
    joint::FittedAdapter adapter;     // identity arm (the slice mechanism is weight-agnostic)
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
    f.adapter = joint::FittedAdapter::load(dir, "all");
    if (!f.adapter.loaded()) {
        return f;
    }
    f.vocab = std::make_unique<joint::Vocabulary>(f.adapter.tables());
    f.ok = true;
    return f;
}
} // namespace

TEST(JointSliceTests, StructureCommittedFlagsAndPrimitiveConsistency)
{
    Fixture f = load();
    ASSERT_TRUE(f.ok) << "corpus/adapter load failed";
    ASSERT_TRUE(f.corpus.pieces.count("bwv324"));
    joint::Piece& piece = f.corpus.pieces.at("bwv324");

    const joint::DecodeResult r = joint::decodePiece(piece, f.adapter, *f.vocab, f.cache, 4,
                                                     std::optional<int>(0), "");
    ASSERT_TRUE(r.complete);
    ASSERT_FALSE(r.segments.empty());

    const std::vector<joint::SegmentSlice> slice =
        joint::computePosteriorSlice(piece, r.segments, f.adapter, *f.vocab, f.cache);
    ASSERT_EQ(slice.size(), r.segments.size());

    for (size_t si = 0; si < slice.size(); ++si) {
        const joint::SegmentSummary& seg = r.segments[si];
        const joint::SegmentSlice& sl = slice[si];
        const joint::LabelClass cls = joint::classFromKey(seg.classKey);

        // ── KEY axis ────────────────────────────────────────────────────────────────
        ASSERT_EQ(sl.keyAxis.labels.size(), sl.keyAxis.scores.size()) << "seg " << si;
        ASSERT_FALSE(sl.keyAxis.labels.empty());
        // a triad/seventh's root is defined in every key, so all 24 keys are scoreable here.
        EXPECT_EQ(sl.keyAxis.labels.size(), 24u) << "seg " << si;
        // committed flag: index valid, label == the decoded key, and (all-24 case) == KEYS_24 position.
        ASSERT_GE(sl.keyAxis.committed, 0);
        ASSERT_LT(sl.keyAxis.committed, static_cast<int>(sl.keyAxis.labels.size()));
        EXPECT_EQ(sl.keyAxis.labels[sl.keyAxis.committed], seg.key) << "seg " << si;
        if (sl.keyAxis.labels.size() == 24u) {
            EXPECT_EQ(sl.keyAxis.committed, 2 * seg.tonicPc + (seg.isMajor ? 0 : 1)) << "seg " << si;
            // KEYS_24 order (tonic 0..11, major before minor) + bit-exact vs the primitive.
            for (int t = 0; t < 12; ++t) {
                for (int mi = 0; mi < 2; ++mi) {
                    const bool m = (mi == 0);
                    const int k = 2 * t + mi;
                    EXPECT_EQ(sl.keyAxis.labels[k], keyLabel(t, m)) << "seg " << si << " key " << k;
                    EXPECT_EQ(sl.keyAxis.scores[k],
                              joint::segmentContentScore(piece, seg.i, seg.j, t, m, cls, f.adapter, f.cache))
                        << "seg " << si << " key " << k << " not bit-exact vs segmentContentScore";
                }
            }
        }

        // ── CHORD axis ──────────────────────────────────────────────────────────────
        ASSERT_EQ(sl.chordAxis.labels.size(), sl.chordAxis.scores.size()) << "seg " << si;
        ASSERT_FALSE(sl.chordAxis.labels.empty());
        // committed flag points at the decoded class.
        ASSERT_GE(sl.chordAxis.committed, 0);
        ASSERT_LT(sl.chordAxis.committed, static_cast<int>(sl.chordAxis.labels.size()));
        EXPECT_EQ(sl.chordAxis.labels[sl.chordAxis.committed], seg.classKey) << "seg " << si;
        // sorted (strictly ascending — class keys are unique).
        EXPECT_TRUE(std::is_sorted(sl.chordAxis.labels.begin(), sl.chordAxis.labels.end()));
        EXPECT_EQ(std::adjacent_find(sl.chordAxis.labels.begin(), sl.chordAxis.labels.end()),
                  sl.chordAxis.labels.end()) << "seg " << si << " chord labels not unique";
        // every published chord score is bit-exactly the primitive of that class under the committed key.
        for (size_t c = 0; c < sl.chordAxis.labels.size(); ++c) {
            const joint::LabelClass cc = joint::classFromKey(sl.chordAxis.labels[c]);
            EXPECT_EQ(sl.chordAxis.scores[c],
                      joint::segmentContentScore(piece, seg.i, seg.j, seg.tonicPc, seg.isMajor, cc,
                                                 f.adapter, f.cache))
                << "seg " << si << " chord " << c << " not bit-exact vs segmentContentScore";
        }
    }
}

TEST(JointSliceTests, ScoreabilityFilterExcludesUnscoreableClasses)
{
    Fixture f = load();
    ASSERT_TRUE(f.ok);
    joint::Piece& piece = f.corpus.pieces.at("bwv324");
    const joint::DecodeResult r = joint::decodePiece(piece, f.adapter, *f.vocab, f.cache, 4,
                                                     std::optional<int>(0), "");
    const std::vector<joint::SegmentSlice> slice =
        joint::computePosteriorSlice(piece, r.segments, f.adapter, *f.vocab, f.cache);
    ASSERT_FALSE(slice.empty());

    // The chord axis is a FILTERED subset of the vocabulary: some classes are rootless (AugSixth/
    // Neapolitan leave chordFactorPcs null) or otherwise unscoreable under the committed key, so the
    // axis is strictly smaller than the full vocabulary — the filter is not a no-op.
    EXPECT_LT(slice[0].chordAxis.labels.size(), f.vocab->ordered().size());
    // and every class the axis DID keep has a defined root under the committed key (the filter's rule).
    const joint::SegmentSummary& seg = r.segments[0];
    for (const std::string& ck : slice[0].chordAxis.labels) {
        const joint::ChordInfo& info = f.cache.get(joint::classFromKey(ck), seg.tonicPc, seg.isMajor);
        EXPECT_TRUE(info.root.has_value()) << ck << " kept but rootless";
    }
}

TEST(JointSliceTests, EmptyAndDegenerateSegments)
{
    Fixture f = load();
    ASSERT_TRUE(f.ok);
    joint::Piece& piece = f.corpus.pieces.at("bwv324");

    // empty segment list -> empty slice (the degenerate guard).
    const std::vector<joint::SegmentSlice> none =
        joint::computePosteriorSlice(piece, {}, f.adapter, *f.vocab, f.cache);
    EXPECT_TRUE(none.empty());

    // a single hand-made one-event segment is sliced without crashing and carries both axes.
    joint::SegmentSummary s;
    s.i = 0;
    s.j = 1;
    s.startTick = piece.events.front().start;
    s.endTick = piece.events.front().end;
    s.tonicPc = 0;
    s.isMajor = true;
    s.classKey = "I | Maj |  | ";
    const std::vector<joint::SegmentSlice> one =
        joint::computePosteriorSlice(piece, { s }, f.adapter, *f.vocab, f.cache);
    ASSERT_EQ(one.size(), 1u);
    EXPECT_FALSE(one[0].keyAxis.labels.empty());
    EXPECT_FALSE(one[0].chordAxis.labels.empty());
    // the committed class "I | Maj |  | " is scoreable under C major, so it is flagged.
    ASSERT_GE(one[0].chordAxis.committed, 0);
    EXPECT_EQ(one[0].chordAxis.labels[one[0].chordAxis.committed], std::string("I | Maj |  | "));
}
