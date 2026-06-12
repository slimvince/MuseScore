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

#pragma once

// chordpathdecoder.h
//
// Beam-1 chord-path decoder (Stage 3.1; docs/decoder_design.md §§2–5, §9, §12).
//
// The decoder re-expresses the greedy left-to-right commit chain that
// analyzeRegions() threads by hand. Today each region-commit site keeps three
// loop-local pieces of path state — a `ChordTemporalContext`, a rolling
// stepwise counter, and a recent-roots window — and advances them with
// `advanceTemporalContext()`. This object encapsulates exactly those three
// pieces and exposes a single `commit()` that calls the same
// `advanceTemporalContext()`. The three commit sites (Pass 1, Pass 2, Pass 2b)
// each hold one decoder and call `decoder.commit(...)` instead.
//
// BYTE-IDENTITY (the Stage-3.1 hard gate). The decoder NEVER computes a score.
// Emission (analyzeChord → ScoringSnapshot) and the per-bass / cross-bass
// competition that selects the winner (applyHarmonicFunction, called inside
// analyzeChord) are untouched and run upstream of commit(); the FP-sensitive
// score expression `(basisIndep + rcb + basisDep) × cf × af + wComplete + wSeq
// [+ wDim] [+ steps]` lives in harmonicfunctionlayer.cpp and is not touched
// here. The decoder only re-expresses how the gate-corrected committed identity
// threads forward to the next node. At beam 1 there is exactly one path, so the
// decoder's path state ≡ the single `ChordTemporalContext` the old loop threaded
// — identical by construction (design §4, §5). Wins come at Stage 3.2 (wider
// beam), not here.
//
// CACHE-READY, NOT CACHED (design §13 Q7 / roadmap 3.1b). The decoder is a
// constructible object that accumulates the decoded path over a region range and
// can be queried via path(); nothing stores it across queries yet. Decode-once /
// query-many is Stage 3.1b, after this byte-identity gate passes.

#include <array>
#include <utility>
#include <vector>

#include "composing/analysis/chord/chordanalyzer.h"

namespace mu::composing::analysis::decode {

/// One committed node on the decoded chord path. At beam 1 there is exactly one
/// path, so this is the gate-corrected winner the commit chain selected plus the
/// emitted alternatives and the winner's score/margin — the evidence Stage 6
/// functional labeling will consume (design §1 / §13 Q5, "emit the full path +
/// per-node alternatives + margins"; the committed identity is `committed` by
/// construction). At beam 1 this is inert plumbing: nothing reads path() yet.
struct ChordPathNode {
    ChordAnalysisResult              committed;              ///< gate-corrected committed identity
    std::vector<ChordAnalysisResult> alternatives;          ///< emitted alternatives (results[1..])
    double                           winnerScore  = 0.0;     ///< committed winner's competition score
    double                           winnerMargin = -1.0;    ///< score gap to runner-up; -1 if none
};

/// Beam-1 chord-path decoder. Encapsulates the path state that the greedy commit
/// chain threaded by hand and replaces `advanceTemporalContext()` at every
/// region-commit site with `commit()`. See the file header for the byte-identity
/// argument.
class ChordPathDecoder
{
public:
    /// Seed the decoder with the initial temporal context (Pass 1: the
    /// findTemporalContext() result; Pass 2/2b: a context seeded from the
    /// previous committed sub-region). The rolling stepwise counter and
    /// recent-roots window start at their defaults — exactly the loop-local
    /// initial values they replace (runningStepwiseCount = 0,
    /// recentRootsBuf = {-1,-1,-1}).
    explicit ChordPathDecoder(const ChordTemporalContext& seed,
                              DecodeQualityLevel level = DecodeQualityLevel::FastBeam1)
        : m_ctx(seed), m_level(level) {}

    /// Live access to the threaded temporal context. Callers populate the
    /// per-region INPUT fields on it that the oracle reads
    /// (bassIsStepwiseFromPrevious, nextRootPc / nextBassPc,
    /// bassIsStepwiseToNext, regionMetricWeight, …) exactly as the old loop wrote
    /// them onto the threaded ctx — these are region-derived inputs, not path
    /// state.
    ChordTemporalContext& context() noexcept { return m_ctx; }
    const ChordTemporalContext& context() const noexcept { return m_ctx; }

    /// Commit the gate-corrected winner for the current node and advance the path
    /// state. Byte-identical re-expression of
    ///   advanceTemporalContext(ctx, runningStepwiseCount, recentRootsBuf,
    ///                          chosen, gateCtx)
    /// — the rolling counter and recent-roots window are now owned here.
    ///
    /// Beam-1 only at Stage 3.1: the quality level is recorded but does not
    /// change commit behavior; levels > FastBeam1 are reserved for Stage 3.2
    /// (wider beam) and currently behave as FastBeam1 (no-op), so output is
    /// byte-identical at every level today.
    void commit(const ChordIdentity& chosen, const PostScoringGateContext& gateCtx) noexcept
    {
        advanceTemporalContext(m_ctx, m_runningStepwiseCount, m_recentRootsBuf,
                               chosen, gateCtx);
    }

    /// Record the committed node on the decoded path (cache-ready plumbing,
    /// design §13 Q7 / Q5). Inert at beam 1 — nothing reads path() yet.
    void recordNode(ChordPathNode node) { m_path.push_back(std::move(node)); }

    /// The decoded path accumulated so far (one node per committed region).
    const std::vector<ChordPathNode>& path() const noexcept { return m_path; }

    /// The quality level this decoder was constructed with.
    DecodeQualityLevel level() const noexcept { return m_level; }

private:
    ChordTemporalContext m_ctx;                       ///< threaded temporal context (path state)
    int                  m_runningStepwiseCount = 0;  ///< rolling stepwise counter (path state)
    std::array<int, 3>   m_recentRootsBuf = {-1, -1, -1}; ///< recent-roots window (path state)
    DecodeQualityLevel   m_level = DecodeQualityLevel::FastBeam1;
    std::vector<ChordPathNode> m_path;                ///< accumulated decoded path (inert at beam 1)
};

} // namespace mu::composing::analysis::decode
