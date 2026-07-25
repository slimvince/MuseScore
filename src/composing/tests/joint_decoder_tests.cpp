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

// Joint estimator, commit 2: DECODE PARITY against the established Python probe. The C++ decoder must
// reproduce the committed probe_corpus_decode.json (the oracle) — the segment state sequence and
// boundaries EXACTLY, and the total score to the artifact's rounding — on the identity-weight
// (generative-baseline) arm. This establishes the semi-Markov Viterbi + candidate generation + factor
// scoring + the tie-break ordering as a byte-equivalent port (#19). Read-only over the committed
// artifacts under tools/joint_estimator/; the module stays dormant.

#include <gtest/gtest.h>

#include <fstream>
#include <iterator>
#include <optional>
#include <string>
#include <vector>

#include "serialization/json.h"
#include "types/bytearray.h"

#include "composing/analysis/joint/jointdecoder.h"

#ifndef JOINT_ARTIFACT_DIR
#define JOINT_ARTIFACT_DIR "."
#endif

namespace joint = mu::composing::analysis::joint;

namespace {
muse::JsonObject readObject(const std::string& path)
{
    std::ifstream f(path, std::ios::binary);
    EXPECT_TRUE(f.good()) << "cannot open " << path;
    const std::string s((std::istreambuf_iterator<char>(f)), std::istreambuf_iterator<char>());
    std::string err;
    const muse::ByteArray ba(s.data(), s.size());
    const muse::JsonObject o = muse::JsonDocument::fromJson(ba, &err).rootObject();
    EXPECT_TRUE(err.empty()) << err;
    return o;
}
} // namespace

TEST(JointDecoderTests, DecodeParityIdentityWeights)
{
    const std::string dir = JOINT_ARTIFACT_DIR;

    joint::LoadedCorpus corpus = joint::loadPiecesFromNoteEvents(dir + "/note_events/note_events.json");
    ASSERT_TRUE(corpus.ok) << corpus.error;
    ASSERT_EQ(corpus.ticksPerQuarter, 480);

    joint::FittedAdapter adapter = joint::FittedAdapter::load(dir, "all");
    ASSERT_TRUE(adapter.loaded()) << adapter.error();
    ASSERT_FALSE(adapter.anyCadenceWeight());   // identity arm: cadence factor inert

    joint::Vocabulary vocab(adapter.tables());
    joint::ChordCache cache;

    const muse::JsonObject oraclePieces = readObject(dir + "/probe_corpus_decode.json").value("pieces").toObject();

    // a mix of the smallest pieces + the desk-simulation named cases (the probe oracle covers all 326;
    // this establishment decodes a representative subset exactly)
    const std::vector<std::string> stems = {
        "bwv324", "bwv323", "bwv67.7", "bwv352", "bwv10.7", "bwv88.7", "bwv145.5"
    };

    for (const std::string& stem : stems) {
        ASSERT_TRUE(corpus.pieces.count(stem)) << stem;
        ASSERT_TRUE(oraclePieces.contains(stem)) << stem;
        const muse::JsonObject rec = oraclePieces.value(stem).toObject();

        const muse::JsonValue sigVal = rec.value("sig_fifths");
        const std::optional<int> sig = sigVal.isNumber() ? std::optional<int>(sigVal.toInt()) : std::nullopt;
        const std::string dm = rec.value("declared_mode").toStdString();

        const joint::DecodeResult r = joint::decodePiece(corpus.pieces.at(stem), adapter, vocab, cache,
                                                         /*segCap=*/4, sig, dm);
        ASSERT_TRUE(r.complete) << stem;

        // total score to the artifact's 3-decimal rounding
        EXPECT_NEAR(r.totalScore, rec.value("total_score").toDouble(), 5e-4) << stem << " total_score";

        // segment state sequence + boundaries — EXACT
        const muse::JsonArray expSegs = rec.value("segments").toArray();
        ASSERT_EQ(r.segments.size(), expSegs.size()) << stem << " segment count";
        for (size_t s = 0; s < r.segments.size(); ++s) {
            const muse::JsonObject e = expSegs.at(s).toObject();
            const joint::SegmentSummary& g = r.segments[s];
            const std::string where = stem + " seg " + std::to_string(s);
            EXPECT_EQ(g.i, e.value("i").toInt()) << where << " i";
            EXPECT_EQ(g.j, e.value("j").toInt()) << where << " j";
            EXPECT_EQ(g.startTick, e.value("start_tick").toInt()) << where << " start_tick";
            EXPECT_EQ(g.endTick, e.value("end_tick").toInt()) << where << " end_tick";
            EXPECT_EQ(g.tonicPc, e.value("tonic_pc").toInt()) << where << " tonic_pc";
            EXPECT_EQ(g.isMajor, e.value("is_major").toBool()) << where << " is_major";
            EXPECT_EQ(g.classKey, e.value("class_key").toStdString()) << where << " class_key";
            const muse::JsonValue rootVal = e.value("root_pc");
            if (rootVal.isNumber()) {
                ASSERT_TRUE(g.rootPc.has_value()) << where << " root_pc missing";
                EXPECT_EQ(*g.rootPc, rootVal.toInt()) << where << " root_pc";
            } else {
                EXPECT_FALSE(g.rootPc.has_value()) << where << " root_pc should be null";
            }
        }
    }

    // establish the per-segment content diagnostic against the pinned Python score_segment_content
    // (the three bwv352 segments the decode-parity divergence was localized with)
    joint::Piece& p352 = corpus.pieces.at("bwv352");
    EXPECT_NEAR(joint::segmentContentScore(p352, 73, 77, 9, false,
                                           joint::classFromKey("VI | Maj7 |  | "), adapter, cache),
                -45.26132, 1e-4);
    EXPECT_NEAR(joint::segmentContentScore(p352, 73, 74, 9, false,
                                           joint::classFromKey("V | Maj |  | "), adapter, cache),
                -14.551858, 1e-4);
    EXPECT_NEAR(joint::segmentContentScore(p352, 74, 77, 9, false,
                                           joint::classFromKey("I | Min |  | "), adapter, cache),
                -34.349269, 1e-4);
}
