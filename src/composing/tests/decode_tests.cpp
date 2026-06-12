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

// decode_tests.cpp
//
// Unit tests for the Stage-3.1 beam-1 chord-path decoder
// (analysis/decode/chordpathdecoder.h, docs/decoder_design.md §§4–5).
//
// The decoder re-expresses the greedy commit chain: it owns the path state the
// region loop threaded by hand (ChordTemporalContext + rolling stepwise counter +
// recent-roots window) and replaces advanceTemporalContext() with commit(). The
// load-bearing claim is that decoder.commit() is BYTE-IDENTICAL to the legacy
// advanceTemporalContext() expression. The equivalence test below pins exactly
// that, in lockstep, over a scripted commit sequence — the unit-level half of the
// Stage-3.1 byte-identity gate (the integration half is the 0/353×3 corpus A/B and
// the 11/11 pipeline snapshots). The default-level and no-op-higher-level pins
// guard the quality knob (design §9 / §13 Q6).

#include <gtest/gtest.h>

#include <array>
#include <string>
#include <vector>

#include "composing/analysis/chord/chordanalyzer.h"
#include "composing/analysis/decode/chordpathdecoder.h"

using namespace mu::composing::analysis;

namespace {

// A scripted commit: the per-region input the loop sets before committing
// (bassIsStepwiseFromPrevious, which drives the rolling stepwise count) plus the
// gate-corrected winner identity and the captured gate context.
struct ScriptStep {
    bool         stepwise;
    int          rootPc;
    int          bassPc;
    ChordQuality quality;
    // gateCtx inputs that feed the predecessor-confidence fields.
    int                    distinctPcs;
    std::array<double, 12> pcWeight;
    std::vector<double>    rawScores;   // rawCandidates[*].score (0, 1 or 2+ entries)
};

ChordIdentity makeIdentity(const ScriptStep& s)
{
    ChordIdentity id;
    id.rootPc  = s.rootPc;
    id.bassPc  = s.bassPc;
    id.quality = s.quality;
    return id;
}

PostScoringGateContext makeGateCtx(const ScriptStep& s)
{
    PostScoringGateContext g;
    g.distinctPcs = s.distinctPcs;
    g.pcWeight    = s.pcWeight;
    for (double sc : s.rawScores) {
        RawCandidate rc{};
        rc.score = sc;
        g.rawCandidates.push_back(rc);
    }
    return g;
}

// Field-by-field equality of every ChordTemporalContext member commit() can touch
// (and the input fields, which must be left untouched identically).
void expectContextsEqual(const ChordTemporalContext& a, const ChordTemporalContext& b,
                         const char* where)
{
    EXPECT_EQ(a.previousRootPc, b.previousRootPc) << where;
    EXPECT_EQ(a.previousBassPc, b.previousBassPc) << where;
    EXPECT_EQ(static_cast<int>(a.previousQuality), static_cast<int>(b.previousQuality)) << where;
    EXPECT_EQ(a.bassIsStepwiseFromPrevious, b.bassIsStepwiseFromPrevious) << where;
    EXPECT_EQ(a.bassIsStepwiseToNext, b.bassIsStepwiseToNext) << where;
    EXPECT_EQ(a.nextBassPc, b.nextBassPc) << where;
    EXPECT_EQ(a.nextRootPc, b.nextRootPc) << where;
    EXPECT_EQ(a.consecutiveBassStepwiseCount, b.consecutiveBassStepwiseCount) << where;
    EXPECT_EQ(a.recentRootPcs, b.recentRootPcs) << where;
    EXPECT_DOUBLE_EQ(a.regionMetricWeight, b.regionMetricWeight) << where;
    EXPECT_DOUBLE_EQ(a.previousWinnerScore, b.previousWinnerScore) << where;
    EXPECT_DOUBLE_EQ(a.previousWinnerMargin, b.previousWinnerMargin) << where;
    EXPECT_DOUBLE_EQ(a.previousWinnerRootPcWeight, b.previousWinnerRootPcWeight) << where;
    EXPECT_EQ(a.previousDistinctPcs, b.previousDistinctPcs) << where;
}

// A varied script exercising: stepwise on/off transitions (rolling count up/reset),
// the recent-roots window sliding past 3 entries, all rawCandidates arities (0 / 1 /
// 2+ → previousWinnerScore / Margin branches), and a winner root absent from pcWeight.
std::vector<ScriptStep> makeScript()
{
    std::array<double, 12> w0{}; // all zero
    std::array<double, 12> wMix{};
    wMix[0] = 0.9; wMix[4] = 0.5; wMix[7] = 0.3; wMix[2] = 0.15;

    return {
        // stepwise, root, bass, quality, distinctPcs, pcWeight, rawScores
        { false, 0,  0, ChordQuality::Major,          3, wMix, { 2.50, 1.90 } },
        { true,  7,  7, ChordQuality::Major,          4, wMix, { 3.10, 3.08, 1.0 } },
        { true,  2,  5, ChordQuality::Minor,          3, wMix, { 1.75 } },          // 1 cand → margin -1
        { true,  9,  9, ChordQuality::Diminished,     2, w0,   {} },                // 0 cand → score 0, margin -1
        { false, 4,  4, ChordQuality::Major,          4, wMix, { 2.00, 1.10 } },
        { false, 11, 2, ChordQuality::HalfDiminished, 4, wMix, { 2.20, 2.19 } },    // winner root 11 absent from pcWeight
        { true,  5,  7, ChordQuality::Minor,          3, wMix, { 1.40, 1.39 } },
    };
}

} // namespace

// ── Equivalence: decoder.commit() == legacy advanceTemporalContext() ───────────
//
// Drive a raw ChordTemporalContext + standalone rolling buffers (the exact legacy
// expression the loop used) and a ChordPathDecoder through the same scripted
// commits in lockstep. The context state must be byte-identical after every step.
TEST(Composing_DecodeTests, DecoderCommitMatchesAdvanceTemporalContext)
{
    const auto script = makeScript();

    // Seed both from a non-trivial starting context (mirrors a Pass-2 sub-decoder
    // seeded from a previous committed sub-region).
    ChordTemporalContext seed;
    seed.previousRootPc  = 3;
    seed.previousBassPc  = 3;
    seed.previousQuality = ChordQuality::Major;
    seed.consecutiveBassStepwiseCount = 1;
    seed.recentRootPcs = { 3, 8, -1 };

    // (a) legacy expression
    ChordTemporalContext legacyCtx = seed;
    int legacyRunning = 0;
    std::array<int, 3> legacyRecent = { -1, -1, -1 };

    // (b) decoder
    decode::ChordPathDecoder decoder(seed);

    for (size_t i = 0; i < script.size(); ++i) {
        const ScriptStep& s = script[i];
        const ChordIdentity id = makeIdentity(s);
        const PostScoringGateContext g = makeGateCtx(s);

        legacyCtx.bassIsStepwiseFromPrevious = s.stepwise;
        advanceTemporalContext(legacyCtx, legacyRunning, legacyRecent, id, g);

        decoder.context().bassIsStepwiseFromPrevious = s.stepwise;
        decoder.commit(id, g);

        expectContextsEqual(legacyCtx, decoder.context(),
                            ("step " + std::to_string(i)).c_str());
    }
}

// ── Quality knob: default is level 0 (FastBeam1) ───────────────────────────────
TEST(Composing_DecodeTests, DefaultQualityLevelIsFastBeam1)
{
    EXPECT_EQ(ChordAnalyzerPreferences{}.decodeQualityLevel, DecodeQualityLevel::FastBeam1);
    EXPECT_EQ(static_cast<int>(DecodeQualityLevel::FastBeam1), 0);

    decode::ChordPathDecoder decoder(ChordTemporalContext{});
    EXPECT_EQ(decoder.level(), DecodeQualityLevel::FastBeam1);
}

// ── Quality knob: levels > 0 are accepted but currently behave as beam 1 (no-op) ─
//
// Stage 3.1 implements only beam 1; the wider beam lands at 3.2. Until then a
// higher level must commit identically to FastBeam1, so production stays
// byte-identical regardless of the knob.
TEST(Composing_DecodeTests, HigherQualityLevelStillBehavesAsBeamOne)
{
    const auto script = makeScript();

    decode::ChordPathDecoder beam1(ChordTemporalContext{}, DecodeQualityLevel::FastBeam1);
    decode::ChordPathDecoder normal(ChordTemporalContext{}, DecodeQualityLevel::Normal);
    decode::ChordPathDecoder deep(ChordTemporalContext{}, DecodeQualityLevel::Deep);

    for (const ScriptStep& s : script) {
        const ChordIdentity id = makeIdentity(s);
        const PostScoringGateContext g = makeGateCtx(s);
        for (auto* d : { &beam1, &normal, &deep }) {
            d->context().bassIsStepwiseFromPrevious = s.stepwise;
            d->commit(id, g);
        }
        expectContextsEqual(beam1.context(), normal.context(), "Normal vs FastBeam1");
        expectContextsEqual(beam1.context(), deep.context(),   "Deep vs FastBeam1");
    }

    EXPECT_EQ(normal.level(), DecodeQualityLevel::Normal);
    EXPECT_EQ(deep.level(),   DecodeQualityLevel::Deep);
}

// ── Cache-ready plumbing: the decoder accumulates the committed path (inert) ────
//
// path() returns one node per committed region, with the gate-corrected identity as
// `committed` and the winner score/margin from the gate context (evidence-forwarding
// for Stage 6 / §13 Q5). Nothing reads this yet at beam 1.
TEST(Composing_DecodeTests, PathAccumulatesCommittedNodes)
{
    const auto script = makeScript();
    decode::ChordPathDecoder decoder(ChordTemporalContext{});

    for (const ScriptStep& s : script) {
        const ChordIdentity id = makeIdentity(s);
        const PostScoringGateContext g = makeGateCtx(s);
        decoder.context().bassIsStepwiseFromPrevious = s.stepwise;
        decoder.commit(id, g);

        decode::ChordPathNode node;
        node.committed.identity = id;
        node.winnerScore  = g.rawCandidates.empty() ? 0.0 : g.rawCandidates[0].score;
        node.winnerMargin = (g.rawCandidates.size() >= 2)
                            ? g.rawCandidates[0].score - g.rawCandidates[1].score : -1.0;
        decoder.recordNode(std::move(node));
    }

    ASSERT_EQ(decoder.path().size(), script.size());
    for (size_t i = 0; i < script.size(); ++i) {
        EXPECT_EQ(decoder.path()[i].committed.identity.rootPc, script[i].rootPc) << "node " << i;
        EXPECT_EQ(decoder.path()[i].committed.identity.bassPc, script[i].bassPc) << "node " << i;
        const double expScore = script[i].rawScores.empty() ? 0.0 : script[i].rawScores[0];
        EXPECT_DOUBLE_EQ(decoder.path()[i].winnerScore, expScore) << "node " << i;
    }
}
