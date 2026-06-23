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

#include "chordslicedecoder.h"

#include <algorithm>
#include <limits>
#include <optional>

#include "function/harmonicfunctionlayer.h"            // fn::ScoringSnapshot / ScoringCell (the cube)
#include "composing/analysis/engravingbridge/regiontonecollector.h"   // weightedPcView (indexed window)

namespace mu::composing::analysis::chordslice {

namespace {

constexpr double NEG_INF = -std::numeric_limits<double>::infinity();

/// Confidence reported when a slice has no DIFFERENT (root, quality) candidate to
/// compare against — effectively certain (mirrors the L3 single-state sentinel).
constexpr double kNoCompetitorConfidence = 1.0e3;

/// The cell's vertical fit score, BEFORE any progression signal — exactly the
/// value applyHarmonicFunction ranks by on the null-context path (no rootContinuity
/// / resolution / inversion / w_seq folded in, because decode() passes no context):
///   (basisIndep + basisDep) × complexityFactor × augFactor + wCompleteBonus.
/// Identical to DiagnosticOracleCell::verticalScore (chordanalyzer.h) — the one
/// score formula, not a second scorer.
double verticalScore(const function::ScoringCell& cell)
{
    return (cell.basisIndep + cell.basisDep) * cell.complexityFactor * cell.augFactor
           + cell.wCompleteBonus;
}

/// Strict weak ordering for ranking candidates: higher vertical score first;
/// ties broken by template index (lower = preferred, matching the scorer's own
/// tiePriority tie-break), then root pc, then bass pc — fully deterministic.
bool candidateBetter(const ChordSliceCandidate& a, const ChordSliceCandidate& b)
{
    if (a.score != b.score) {
        return a.score > b.score;
    }
    if (a.tiePriority != b.tiePriority) {
        return a.tiePriority < b.tiePriority;
    }
    if (a.rootPc != b.rootPc) {
        return a.rootPc < b.rootPc;
    }
    return a.bassPc < b.bassPc;
}

bool sameChordVoicing(const ChordSliceCandidate& a, const ChordSliceCandidate& b)
{
    return a.rootPc == b.rootPc && a.quality == b.quality && a.bassPc == b.bassPc;
}

bool sameChordSymbol(const ChordSliceCandidate& a, const ChordSliceCandidate& b)
{
    return a.rootPc == b.rootPc && a.quality == b.quality;   // ignores bass/inversion
}

/// The Increment-A window: the focal slice [t] expanded by `contextSlices`
/// neighbour slices on each side. Because the slices tile the domain contiguously,
/// the window is simply [slices[lo].start, slices[hi].end). Clamped to the slice
/// vector. A crude fixed stand-in for the design's adaptive lazy-extend window.
void sliceWindow(const std::vector<slicing::Slice>& slices, int t, int contextSlices,
                 int& winStart, int& winEnd)
{
    const int n = static_cast<int>(slices.size());
    const int c = std::max(0, contextSlices);
    const int lo = std::max(0, t - c);
    const int hi = std::min(n - 1, t + c);
    winStart = slices[static_cast<std::size_t>(lo)].start;
    winEnd   = slices[static_cast<std::size_t>(hi)].end;
}

/// Run the existing scorer over a slice's window and project the surfaced
/// candidate cube (fn::ScoringSnapshot::cells) to a flat candidate list — one
/// ChordSliceCandidate per (bass × root × template) cell, with its vertical score.
/// This is the generation step (design §4 "candidate generation is the lever"): no
/// second scorer, no re-derivation — analyzeChord's complete cube, surfaced the way
/// the L3 decoder surfaced analyzeKeyMode's 252-candidate dump. Returns empty when
/// the window has too few distinct pitch classes to score (analyzeChord gates).
std::vector<ChordSliceCandidate> candidatesForSlice(
    const RuleBasedChordAnalyzer& analyzer,
    const notemodel::NoteModel& model,
    const std::vector<slicing::Slice>& slices, int t,
    int keySignatureFifths, KeySigMode keyMode,
    const ChordAnalyzerPreferences& prefs,
    const ChordSliceDecoderPreferences& decoderPrefs,
    const std::set<std::size_t>& excludeStaves)
{
    int winStart = 0, winEnd = 0;
    sliceWindow(slices, t, decoderPrefs.contextSlices, winStart, winEnd);

    const std::vector<ChordAnalysisTone> tones =
        engravingbridge::weightedPcView(model, winStart, winEnd, excludeStaves,
                                        /*parentStartTick=*/-1,
                                        /*excludeLookAheadOnDenseStart=*/false, prefs);

    function::ScoringSnapshot snapshot;
    analyzer.analyzeChord(tones, keySignatureFifths, keyMode,
                          /*context=*/nullptr, prefs, /*gateCtxOut=*/nullptr, &snapshot);

    std::vector<ChordSliceCandidate> out;
    out.reserve(snapshot.cells.size());
    for (const function::ScoringCell& cell : snapshot.cells) {
        ChordSliceCandidate c;
        c.rootPc      = cell.rootPc;
        c.rootTpc     = (cell.rootPc >= 0 && cell.rootPc < 12)
                        ? snapshot.tpcForPc[static_cast<std::size_t>(cell.rootPc)] : -1;
        c.bassPc      = cell.bassPc;
        c.bassTpc     = cell.bassTpc;
        c.quality     = cell.quality;
        c.tiePriority = cell.tiePriority;
        c.score       = verticalScore(cell);
        out.push_back(c);
    }
    return out;
}

} // namespace

SliceChord ChordSliceDecoder::decideSlice(
    int sliceIndex,
    const std::vector<ChordSliceCandidate>& candidates,
    const std::optional<ChordSliceCandidate>& prevailing,
    const ChordSliceDecoderPreferences& decoderPrefs)
{
    SliceChord sc;
    sc.sliceIndex = sliceIndex;
    if (candidates.empty()) {
        sc.hasChord = false;
        sc.uncertain = true;   // no scorable candidate → treated as uncertain
        return sc;
    }

    // Rank the complete candidate list (the surfaced cube) deterministically.
    std::vector<ChordSliceCandidate> ranked(candidates);
    std::sort(ranked.begin(), ranked.end(), candidateBetter);

    sc.hasChord = true;
    sc.chosen = ranked.front();

    // Confidence = chosen vertical score − best score over any DIFFERENT (root,
    // quality) chord. An inversion of the SAME chord is not a different chord.
    double bestOther = NEG_INF;
    for (const ChordSliceCandidate& c : ranked) {
        if (!sameChordSymbol(c, sc.chosen)) {
            bestOther = std::max(bestOther, c.score);
        }
    }
    sc.confidence = (bestOther == NEG_INF) ? kNoCompetitorConfidence
                                           : (sc.chosen.score - bestOther);
    sc.uncertain = sc.confidence < decoderPrefs.uncertaintyMargin;

    // Ranked alternatives: the distinct chord voicings after the chosen, capped at
    // topK, then ∪ the prevailing chord (the L3 incumbent pattern — kept alive as a
    // carried alternative even when it falls below topK, so the membership two-pass
    // in Increment B always has it).
    for (const ChordSliceCandidate& c : ranked) {
        if (sameChordVoicing(c, sc.chosen)) {
            continue;
        }
        const bool dup = std::any_of(sc.alternatives.begin(), sc.alternatives.end(),
                                     [&](const ChordSliceCandidate& a) { return sameChordVoicing(a, c); });
        if (dup) {
            continue;
        }
        if (decoderPrefs.topK > 0 && static_cast<int>(sc.alternatives.size()) >= decoderPrefs.topK) {
            break;
        }
        sc.alternatives.push_back(c);
    }

    // ∪ the prevailing chord. Keep it alive if it is expressible among THIS slice's
    // candidates (its root+quality is scorable here) and is not already carried /
    // the chosen — using this slice's own cube cell (so it has this slice's score).
    if (prevailing.has_value() && !sameChordSymbol(*prevailing, sc.chosen)) {
        const bool alreadyCarried = std::any_of(
            sc.alternatives.begin(), sc.alternatives.end(),
            [&](const ChordSliceCandidate& a) { return sameChordSymbol(a, *prevailing); });
        if (!alreadyCarried) {
            // Prefer the cube cell matching root+quality+bass; fall back to root+quality.
            const ChordSliceCandidate* exact = nullptr;
            const ChordSliceCandidate* symbol = nullptr;
            for (const ChordSliceCandidate& c : ranked) {
                if (sameChordVoicing(c, *prevailing)) { exact = &c; break; }
                if (!symbol && sameChordSymbol(c, *prevailing)) { symbol = &c; }
            }
            if (exact) {
                sc.alternatives.push_back(*exact);
            } else if (symbol) {
                sc.alternatives.push_back(*symbol);
            }
            // If neither — the prevailing chord is not expressible by this slice's
            // pitches — it is genuinely not a candidate here, so it is not forced.
        }
    }

    return sc;
}

std::vector<SliceChord> ChordSliceDecoder::decode(
    const std::vector<slicing::Slice>& slices,
    const notemodel::NoteModel& noteModel,
    int keySignatureFifths,
    KeySigMode keyMode,
    const ChordAnalyzerPreferences& chordPrefs,
    const ChordSliceDecoderPreferences& decoderPrefs,
    const std::set<std::size_t>& excludeStaves)
{
    const int T = static_cast<int>(slices.size());
    std::vector<SliceChord> out;
    out.reserve(static_cast<std::size_t>(std::max(0, T)));
    if (T == 0) {
        return out;
    }

    // Decode-only relaxation: score thin (1–2 PC) slices instead of dropping them
    // (the greedy-expand sparse-anchor relaxation; audit §8-D). A local copy —
    // production's prefs are untouched.
    ChordAnalyzerPreferences prefs = chordPrefs;
    prefs.minDistinctPcsForCandidate = std::max(1, decoderPrefs.minDistinctPcs);

    const RuleBasedChordAnalyzer analyzer;
    std::optional<ChordSliceCandidate> prevailing;
    for (int t = 0; t < T; ++t) {
        const std::vector<ChordSliceCandidate> cands =
            candidatesForSlice(analyzer, noteModel, slices, t, keySignatureFifths, keyMode,
                               prefs, decoderPrefs, excludeStaves);
        SliceChord sc = decideSlice(t, cands, prevailing, decoderPrefs);
        if (sc.hasChord) {
            prevailing = sc.chosen;   // the incumbent for the next slice
        }
        out.push_back(std::move(sc));
    }
    return out;
}

std::vector<SliceChord> ChordSliceDecoder::redecodeRange(
    const std::vector<slicing::Slice>& slices,
    const notemodel::NoteModel& noteModel,
    int keySignatureFifths,
    KeySigMode keyMode,
    int first, int last,
    const ChordAnalyzerPreferences& chordPrefs,
    const ChordSliceDecoderPreferences& decoderPrefs,
    const std::set<std::size_t>& excludeStaves)
{
    const int T = static_cast<int>(slices.size());
    std::vector<SliceChord> out;
    if (first < 0 || last >= T || first > last) {
        return out;
    }

    ChordAnalyzerPreferences prefs = chordPrefs;
    prefs.minDistinctPcsForCandidate = std::max(1, decoderPrefs.minDistinctPcs);

    const RuleBasedChordAnalyzer analyzer;

    // The per-slice decision is context-free, so reproducing a full decode's
    // [first..last] exactly needs only ONE slice of look-back (to recover the
    // prevailing chord of `first`). Re-run that prefix to build the incumbent.
    const int lo = std::max(0, first - 1);
    std::optional<ChordSliceCandidate> prevailing;
    out.reserve(static_cast<std::size_t>(last - first + 1));
    for (int t = lo; t <= last; ++t) {
        const std::vector<ChordSliceCandidate> cands =
            candidatesForSlice(analyzer, noteModel, slices, t, keySignatureFifths, keyMode,
                               prefs, decoderPrefs, excludeStaves);
        SliceChord sc = decideSlice(t, cands, prevailing, decoderPrefs);
        if (sc.hasChord) {
            prevailing = sc.chosen;
        }
        if (t >= first) {
            out.push_back(std::move(sc));
        }
    }
    return out;
}

} // namespace mu::composing::analysis::chordslice
