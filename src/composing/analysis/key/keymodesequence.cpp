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

#include "keymodesequence.h"

#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <limits>
#include <optional>
#include <set>

#include "engraving/types/constants.h"

#include "composing/analysis/engravingbridge/regiontonecollector.h"

namespace mu::composing::analysis::keymodeseq {

using State = KeyModeSequenceDecoder::State;

namespace {

constexpr double NEG_INF = -std::numeric_limits<double>::infinity();

/// Number of (tonic × mode) candidates the emission scores (12 × 21 = 252). A
/// candidate's flat index is `tonicPc * KEY_MODE_COUNT + modeIndex`.
constexpr int kCandidateCount = 12 * static_cast<int>(KEY_MODE_COUNT);

/// Confidence reported when a slice has only one surviving candidate (no
/// "different key/mode" to compare against) — effectively certain.
constexpr double kSingleStateConfidence = 1.0e3;

int candidateIndex(int tonicPc, std::size_t modeIndex)
{
    return tonicPc * static_cast<int>(KEY_MODE_COUNT) + static_cast<int>(modeIndex);
}

/// Circle-of-fifths distance (in signature steps) between two parent Ionian tonic
/// pitch classes. This is the minimal key-signature distance — exactly what the
/// emission's keySignatureProximity term penalizes — without needing an
/// enharmonic spelling: fifthsPos(pc) places each pc on the 12-step circle of
/// fifths, and the distance is the cyclic gap. (C→F# and C→Gb both = 6.)
int cofDistance(int ionianPcA, int ionianPcB)
{
    auto fifthsPos = [](int pc) {
        const int n = ((pc % 12) + 12) % 12;
        return (n * 7) % 12;            // 7 == circle-of-fifths step generator (mod 12)
    };
    const int d = std::abs(fifthsPos(ionianPcA) - fifthsPos(ionianPcB));
    return std::min(d, 12 - d);
}

/// Build the per-slice emission pitch-context window. Maps the slice [start, end)
/// to its look-around window (± seqPrefs.windowBeats) and the decoder's decay /
/// look-ahead settings, then delegates to the SHARED, INDEXED engravingbridge view
/// `pitchContextOverSpan` (over NoteModel::overlapping — NOT collectPitchContext /
/// a DOM walk). The window-building primitive lives in the proper (L1-adjacent)
/// layer beside weightedPcView / soundingAt; this is the L3 caller's thin mapping.
std::vector<KeyModeAnalyzer::PitchContext> buildSliceContext(
    const notemodel::NoteModel& model, int start, int end,
    const KeyModeSequencePreferences& seqPrefs,
    const KeyModeAnalyzerPreferences& keyPrefs)
{
    const int div = mu::engraving::Constants::DIVISION;
    const int win = static_cast<int>(std::lround(seqPrefs.windowBeats * div));
    const engravingbridge::SpanWindowWeights weights{
        seqPrefs.decayRate, seqPrefs.lookaheadWeight, seqPrefs.beatsPerDecayUnit };
    std::vector<KeyModeAnalyzer::PitchContext> ctx;
    engravingbridge::pitchContextOverSpan(model, start - win, end + win, start, end,
                                          /*excludeStaves=*/ {}, keyPrefs, weights, ctx);
    return ctx;
}

KeyModeAnalysisResult stateToResult(const State& st, double emissionScore)
{
    KeyModeAnalysisResult r;
    r.keySignatureFifths   = st.keySignatureFifths;
    r.mode                 = st.mode;
    r.tonicPc              = st.tonicPc;
    r.score                = emissionScore;
    r.normalizedConfidence = 0.0;
    return r;
}

// The lattice: the global state set + the per-slice emission over it.
struct Lattice {
    std::vector<State> states;
    std::vector<std::vector<double>> emissions;   // [slice][stateIndex]
};

State stateForCandidate(int candIdx, int keySigFifths)
{
    const int tonicPc      = candIdx / static_cast<int>(KEY_MODE_COUNT);
    const std::size_t mIdx = static_cast<std::size_t>(candIdx % static_cast<int>(KEY_MODE_COUNT));
    State st;
    st.tonicPc            = tonicPc;
    st.mode               = keyModeFromIndex(mIdx);
    st.ionianPc           = ionianTonicPcForMode(tonicPc, mIdx);
    st.keySignatureFifths = keyModeSignatureFifths(tonicPc, st.mode, keySigFifths);
    return st;
}

/// Build the lattice: score every slice's emission through the index, keep the
/// per-slice top-K candidates (∪ any forced candidates, e.g. redecode pins) as the
/// global state set, and project the emission onto that set. `forceCands` is the
/// set of candidate indices that MUST be present regardless of top-K (the pins).
Lattice buildLattice(const std::vector<slicing::Slice>& slices,
                     const notemodel::NoteModel& model,
                     int keySigFifths,
                     std::optional<KeySigMode> declaredMode,
                     const KeyModeAnalyzerPreferences& keyPrefs,
                     const KeyModeSequencePreferences& seqPrefs,
                     const std::vector<int>& forceCands)
{
    const int T = static_cast<int>(slices.size());
    std::vector<std::vector<double>> byCand(T, std::vector<double>(kCandidateCount, 0.0));
    std::set<int> globalCand(forceCands.begin(), forceCands.end());

    const int k = std::max(1, seqPrefs.topK);
    std::vector<KeyCandidateScore> dump;
    for (int t = 0; t < T; ++t) {
        const std::vector<KeyModeAnalyzer::PitchContext> ctx =
            buildSliceContext(model, slices[t].start, slices[t].end, seqPrefs, keyPrefs);
        dump.clear();
        if (!ctx.empty()) {
            KeyModeAnalyzer::analyzeKeyMode(ctx, keySigFifths, keyPrefs, declaredMode, &dump);
        }
        if (dump.empty()) {
            continue;   // empty-context slice → neutral (all-zero) emission, no top-K
        }
        for (const KeyCandidateScore& e : dump) {
            byCand[t][candidateIndex(e.tonicPc, e.modeIndex)] = e.finalScore;
        }
        // dump is sorted by finalScore descending — the first k are the top-K.
        const int kk = std::min(k, static_cast<int>(dump.size()));
        for (int i = 0; i < kk; ++i) {
            globalCand.insert(candidateIndex(dump[i].tonicPc, dump[i].modeIndex));
        }
    }

    Lattice lat;
    const std::vector<int> candList(globalCand.begin(), globalCand.end());   // sorted → deterministic
    lat.states.reserve(candList.size());
    for (int ci : candList) {
        lat.states.push_back(stateForCandidate(ci, keySigFifths));
    }
    lat.emissions.assign(T, std::vector<double>(candList.size(), 0.0));
    for (int t = 0; t < T; ++t) {
        for (std::size_t j = 0; j < candList.size(); ++j) {
            lat.emissions[t][j] = byCand[t][candList[j]];
        }
    }
    return lat;
}

int stateIndexForResult(const std::vector<State>& states, const KeyModeAnalysisResult& r)
{
    for (std::size_t i = 0; i < states.size(); ++i) {
        if (states[i].tonicPc == r.tonicPc && states[i].mode == r.mode) {
            return static_cast<int>(i);
        }
    }
    return -1;
}

} // namespace

double KeyModeSequenceDecoder::changeCost(const State& a, const State& b,
                                          const KeyModeSequencePreferences& seqPrefs)
{
    if (a.tonicPc == b.tonicPc && a.mode == b.mode) {
        return 0.0;   // stay
    }
    const int cof = cofDistance(a.ionianPc, b.ionianPc);
    const double relativeExtra = (a.ionianPc == b.ionianPc) ? seqPrefs.relativePairExtraCost : 0.0;
    return seqPrefs.changeBaseCost + seqPrefs.changePerFifthStep * cof + relativeExtra;
}

std::vector<SliceKeyMode> KeyModeSequenceDecoder::decodeLattice(
    const std::vector<State>& states,
    const std::vector<std::vector<double>>& emissions,
    const KeyModeSequencePreferences& seqPrefs,
    int pinFirstState,
    int pinLastState)
{
    const int T = static_cast<int>(emissions.size());
    const int S = static_cast<int>(states.size());
    if (T == 0 || S == 0) {
        return {};
    }

    auto allowed = [&](int t, int s) -> bool {
        if (t == 0 && pinFirstState >= 0) {
            return s == pinFirstState;
        }
        if (t == T - 1 && pinLastState >= 0) {
            return s == pinLastState;
        }
        return true;
    };

    // ── Forward pass (max-sum Viterbi) with back-pointers. ───────────────────
    std::vector<std::vector<double>> alpha(T, std::vector<double>(S, NEG_INF));
    std::vector<std::vector<int>> back(T, std::vector<int>(S, -1));
    for (int s = 0; s < S; ++s) {
        if (allowed(0, s)) {
            alpha[0][s] = emissions[0][s];
        }
    }
    for (int t = 1; t < T; ++t) {
        for (int s = 0; s < S; ++s) {
            if (!allowed(t, s)) {
                continue;
            }
            double best = NEG_INF;
            int bestPrev = -1;
            for (int sp = 0; sp < S; ++sp) {
                if (alpha[t - 1][sp] == NEG_INF) {
                    continue;
                }
                const double v = alpha[t - 1][sp] - changeCost(states[sp], states[s], seqPrefs);
                if (v > best) {
                    best = v;
                    bestPrev = sp;
                }
            }
            if (bestPrev >= 0) {
                alpha[t][s] = best + emissions[t][s];
                back[t][s] = bestPrev;
            }
        }
    }

    // ── Best end state + traceback → the connected optimal path. ─────────────
    int endState = -1;
    double endBest = NEG_INF;
    for (int s = 0; s < S; ++s) {
        if (alpha[T - 1][s] > endBest) {
            endBest = alpha[T - 1][s];
            endState = s;
        }
    }
    std::vector<int> chosen(T, -1);
    if (endState >= 0) {
        int s = endState;
        for (int t = T - 1; t >= 0; --t) {
            chosen[t] = s;
            s = (t > 0) ? back[t][s] : -1;
            if (s < 0 && t > 0) {
                // Defensive: a broken chain should not happen (every column has a
                // finite predecessor), but fall back to the column argmax.
                double b = NEG_INF;
                for (int q = 0; q < S; ++q) {
                    if (alpha[t - 1][q] > b) { b = alpha[t - 1][q]; s = q; }
                }
            }
        }
    }

    // ── Backward pass (best suffix) for the sequence-margin confidence. ──────
    std::vector<std::vector<double>> beta(T, std::vector<double>(S, NEG_INF));
    for (int s = 0; s < S; ++s) {
        if (allowed(T - 1, s)) {
            beta[T - 1][s] = 0.0;
        }
    }
    for (int t = T - 2; t >= 0; --t) {
        for (int s = 0; s < S; ++s) {
            if (!allowed(t, s)) {
                continue;
            }
            double best = NEG_INF;
            for (int s2 = 0; s2 < S; ++s2) {
                if (beta[t + 1][s2] == NEG_INF) {
                    continue;
                }
                const double v = -changeCost(states[s], states[s2], seqPrefs)
                                 + emissions[t + 1][s2] + beta[t + 1][s2];
                if (v > best) {
                    best = v;
                }
            }
            beta[t][s] = best;
        }
    }

    // ── Per-slice results: chosen, ranked alternatives, sequence-margin. ─────
    std::vector<SliceKeyMode> out;
    out.reserve(T);
    for (int t = 0; t < T; ++t) {
        SliceKeyMode sk;
        sk.sliceIndex = t;
        const int w = (chosen[t] >= 0) ? chosen[t] : 0;
        sk.chosen = stateToResult(states[w], emissions[t][w]);

        // total[s] = best whole-sequence score forced through state s at slice t.
        // The margin is total[winner] − best total through a DIFFERENT key/mode.
        double secondBest = NEG_INF;
        std::vector<std::pair<double, int>> ranked;   // (total, stateIdx), s != winner
        ranked.reserve(S);
        for (int s = 0; s < S; ++s) {
            if (alpha[t][s] == NEG_INF || beta[t][s] == NEG_INF) {
                continue;
            }
            if (s == w) {
                continue;
            }
            const double total = alpha[t][s] + beta[t][s];
            ranked.push_back({ total, s });
            if (total > secondBest) {
                secondBest = total;
            }
        }
        const double winnerTotal = (alpha[t][w] != NEG_INF && beta[t][w] != NEG_INF)
                                   ? alpha[t][w] + beta[t][w] : NEG_INF;
        sk.confidence = (secondBest == NEG_INF || winnerTotal == NEG_INF)
                        ? kSingleStateConfidence
                        : (winnerTotal - secondBest);
        sk.uncertain = sk.confidence < seqPrefs.uncertainThreshold;

        std::sort(ranked.begin(), ranked.end(),
                  [](const std::pair<double, int>& a, const std::pair<double, int>& b) {
                      return a.first > b.first;
                  });
        const int maxAlt = (seqPrefs.maxAlternatives <= 0)
                           ? static_cast<int>(ranked.size())
                           : std::min(seqPrefs.maxAlternatives, static_cast<int>(ranked.size()));
        sk.alternatives.reserve(maxAlt);
        for (int i = 0; i < maxAlt; ++i) {
            sk.alternatives.push_back(stateToResult(states[ranked[i].second], emissions[t][ranked[i].second]));
        }
        out.push_back(std::move(sk));
    }
    return out;
}

std::vector<SliceKeyMode> KeyModeSequenceDecoder::decode(
    const std::vector<slicing::Slice>& slices,
    const notemodel::NoteModel& noteModel,
    int keySigFifths,
    std::optional<KeySigMode> declaredMode,
    const KeyModeAnalyzerPreferences& keyPrefs,
    const KeyModeSequencePreferences& seqPrefs)
{
    const Lattice lat = buildLattice(slices, noteModel, keySigFifths, declaredMode,
                                     keyPrefs, seqPrefs, {});
    return decodeLattice(lat.states, lat.emissions, seqPrefs, -1, -1);
}

std::vector<SliceKeyMode> KeyModeSequenceDecoder::redecodeRange(
    const std::vector<slicing::Slice>& slices,
    const notemodel::NoteModel& noteModel,
    int keySigFifths,
    std::optional<KeySigMode> declaredMode,
    int first, int last,
    const KeyModeAnalysisResult& leftPin,
    const KeyModeAnalysisResult& rightPin,
    const KeyModeAnalyzerPreferences& keyPrefs,
    const KeyModeSequencePreferences& seqPrefs)
{
    const int T = static_cast<int>(slices.size());
    if (first < 0 || last >= T || first > last) {
        return {};
    }

    // Rebuild the FULL lattice (same state set + emissions as a full decode), with
    // the two pins forced into the state set, then re-run the Viterbi only over the
    // sub-range with the endpoints pinned. Reproduces the matching slice of a full
    // decode exactly (sub-path optimality over an identical lattice).
    const std::vector<int> forceCands = {
        candidateIndex(leftPin.tonicPc, keyModeIndex(leftPin.mode)),
        candidateIndex(rightPin.tonicPc, keyModeIndex(rightPin.mode)),
    };
    const Lattice lat = buildLattice(slices, noteModel, keySigFifths, declaredMode,
                                     keyPrefs, seqPrefs, forceCands);

    const int pinFirst = stateIndexForResult(lat.states, leftPin);
    const int pinLast  = stateIndexForResult(lat.states, rightPin);

    const std::vector<std::vector<double>> sub(lat.emissions.begin() + first,
                                               lat.emissions.begin() + last + 1);
    std::vector<SliceKeyMode> out = decodeLattice(lat.states, sub, seqPrefs, pinFirst, pinLast);
    for (SliceKeyMode& sk : out) {
        sk.sliceIndex += first;
    }
    return out;
}

} // namespace mu::composing::analysis::keymodeseq
