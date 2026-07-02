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
#include "functionresolver.h"

#include <algorithm>
#include <cmath>

#include "composing/analysis/region/sparsechordrefinement.h"   // diatonicDegreeForRootPc

namespace mu::composing::analysis {

namespace {

/// Pitch class in [0,11] (the self-contained-helper precedent; no chord/ math headers).
/// Named normPc (not norm) to avoid an anonymous-namespace collision with
/// functioncadence.cpp's norm() in the Unity build.
int normPc(int pc) noexcept
{
    return ((pc % 12) + 12) % 12;
}

/// The §5.0 "function" view of a candidate (root + quality) the licensing test reasons over.
ProgressionChord toPC(const ChordSliceCandidate& c) noexcept
{
    return ProgressionChord{ c.rootPc, c.quality };
}

bool sameRootQuality(const ChordSliceCandidate& c, const ProgressionChord& p) noexcept
{
    return c.rootPc == p.rootPc && c.quality == p.quality;
}

/// Build the §5.0 progression view from the resolver's region (the committed-chord
/// stream the functionprogression queries read; abstained slices carry committed==false).
Progression buildProgression(const std::vector<FunctionSlice>& region)
{
    Progression prog;
    prog.reserve(region.size());
    for (const FunctionSlice& s : region) {
        ProgressionSlice ps;
        ps.chord = s.chord;
        ps.committed = s.committed;
        ps.metricWeight = s.metricWeight;
        ps.startTick = s.startTick;
        ps.endTick = s.endTick;
        prog.push_back(ps);
    }
    return prog;
}

/// §5.2/§5.5: the total cadence tonic-vote a candidate tonic pc receives in this region
/// (sum of the votes of cadences whose tonic is that pc). Region-scoped by construction.
double cadenceVoteFor(int tonicPc, const std::vector<FunctionalCadence>& cadences) noexcept
{
    if (tonicPc < 0) {
        return 0.0;
    }
    double v = 0.0;
    for (const FunctionalCadence& c : cadences) {
        if (c.tonicPc == tonicPc) {
            v += c.tonicVote;
        }
    }
    return v;
}

/// §5.5 "functional plausibility": the fixed-feature score breaking a low-margin tie —
/// a licensed progression OUT of the prevailing harmony + INTO the established next
/// function + a cadential fit (the reading's root receives a cadence tonic-vote). The
/// features are fixed here; the weights are firewall seeds.
double plausibility(const ProgressionChord& reading,
                    const ProgressionChord& prevChord, bool hasPrev,
                    const ProgressionChord& nextChord, bool hasNext,
                    const std::vector<FunctionalCadence>& cadences,
                    const FunctionResolverParams& params) noexcept
{
    double p = 0.0;
    if (hasPrev && isLicensedProgression(prevChord, reading)) {
        p += params.wLicensedOut;
    }
    if (hasNext && isLicensedProgression(reading, nextChord)) {
        p += params.wLicensedIn;
    }
    if (cadenceVoteFor(reading.rootPc, cadences) > 0.0) {
        p += params.wCadentialFit;
    }
    return p;
}

} // namespace

// ── §5.7 the soft bass-/root-scale-degree functional bias ─────────────────────

FunctionalBias degreeFunctionalBias(int degree) noexcept
{
    // §5.7: 1̂/3̂ → tonic; 2̂/4̂ → pre-dominant; 5̂/7̂ → dominant; 6̂ → none. Degrees are
    // 0-based (diatonicDegreeForRootPc): 0=1̂ … 6=7̂; -1 (chromatic) → none.
    switch (degree) {
    case 0: case 2: return FunctionalBias::Tonic;        // 1̂, 3̂
    case 1: case 3: return FunctionalBias::Predominant;  // 2̂, 4̂
    case 4: case 6: return FunctionalBias::Dominant;     // 5̂, 7̂
    default:        return FunctionalBias::None;          // 6̂ or chromatic
    }
}

FunctionalBias bassScaleDegreeBias(int bassPc, const ResolverKey& key)
{
    if (bassPc < 0) {
        return FunctionalBias::None;
    }
    const int degree = region::diatonicDegreeForRootPc(normPc(bassPc), key.keyFifths, key.keyMode);
    return degreeFunctionalBias(degree);
}

namespace {

/// The function-class of a reading's ROOT degree in the key (the same §5.7 mapping,
/// used to compare a tied reading against the bass-degree bias).
FunctionalBias rootFunctionalBias(int rootPc, const ResolverKey& key)
{
    if (rootPc < 0) {
        return FunctionalBias::None;
    }
    const int degree = region::diatonicDegreeForRootPc(normPc(rootPc), key.keyFifths, key.keyMode);
    return degreeFunctionalBias(degree);
}

// ── Per-abstain resolution (§5.5) ─────────────────────────────────────────────
//
// Selects among the carried readings of an L4-abstained slice by the named ambiguity
// kind, using the progression model (Step 1), the cadence tonic-vote (Step 2), and the
// §5.7 bass-degree prior — NEVER re-deriving, carrying the honest open mark where the
// evidence decides nothing. (The two contesting readings are named readA / readB — not
// single-letter locals, to dodge a Unity-build macro collision.)
ResolvedReading resolveAbstained(int i, const Progression& prog,
                                 const std::vector<FunctionSlice>& region,
                                 const std::vector<FunctionalCadence>& cadences,
                                 const ResolverKey& key,
                                 const FunctionResolverParams& params)
{
    const FunctionSlice& s = region[static_cast<size_t>(i)];
    const OpenQuestionLabel& oq = s.openQuestion;

    ResolvedReading r;
    r.sliceIndex = i;
    r.wasAbstain = true;
    r.kind = oq.ambiguity;

    // §5.0 context (read off the CURRENT progression — reflects any upstream override).
    const int nextIdx = establishedNextFunctionIndex(prog, i);
    const int prevIdx = prevailingHarmonyIndex(prog, i);
    const bool hasNext = nextIdx >= 0;
    const bool hasPrev = prevIdx >= 0;
    const ProgressionChord nextChord = hasNext ? prog[static_cast<size_t>(nextIdx)].chord : ProgressionChord{};
    const ProgressionChord prevChord = hasPrev ? prog[static_cast<size_t>(prevIdx)].chord : ProgressionChord{};

    const ChordSliceCandidate& readA = oq.readingA;
    const ChordSliceCandidate& readB = oq.readingB;
    const bool hasB = oq.hasReadingB;

    auto openMark = [&]() -> ResolvedReading {
        r.openMark = true;
        r.resolved = false;
        r.basis = ResolutionBasis::None;
        r.reading = readA;             // carry the top reading as the displayed-but-uncertain one (§7)
        r.functionConfidence = 0.0;
        return r;
    };
    auto pick = [&](const ChordSliceCandidate& c, ResolutionBasis basis, double conf) -> ResolvedReading {
        r.resolved = true;
        r.openMark = false;
        r.reading = c;
        r.basis = basis;
        r.functionConfidence = conf;
        return r;
    };
    // §5.7 soft prior tie-break between the two contesting readings (never a gate): the
    // slice's bass degree biases a function class; prefer the reading whose own root
    // function-class matches that bias. If exactly one matches → pick it; else open mark.
    auto tieBreakOrOpen = [&]() -> ResolvedReading {
        if (!hasB) {
            return openMark();
        }
        const FunctionalBias bias = bassScaleDegreeBias(readA.bassPc, key);  // bassPc is the slice bass (shared)
        if (bias == FunctionalBias::None) {
            return openMark();
        }
        const bool aMatch = rootFunctionalBias(readA.rootPc, key) == bias;
        const bool bMatch = rootFunctionalBias(readB.rootPc, key) == bias;
        if (aMatch != bMatch) {
            return pick(aMatch ? readA : readB, ResolutionBasis::BassDegreePrior, 0.25);
        }
        return openMark();
    };

    switch (oq.ambiguity) {
    case AmbiguityKind::TransitionVsContinuation: {
        if (!hasB) {
            return openMark();
        }
        // Belong to the arriving function: a licensed progression INTO the next.
        const bool aIn = hasNext && isLicensedProgression(toPC(readA), nextChord);
        const bool bIn = hasNext && isLicensedProgression(toPC(readB), nextChord);
        if (aIn != bIn) {
            return pick(aIn ? readA : readB, ResolutionBasis::Progression, 1.0);
        }
        // Else a passing/neighbour figure within the prevailing harmony: the reading
        // that continues (matches) the prevailing harmony.
        const bool aPrev = hasPrev && sameRootQuality(readA, prevChord);
        const bool bPrev = hasPrev && sameRootQuality(readB, prevChord);
        if (aPrev != bPrev) {
            return pick(aPrev ? readA : readB, ResolutionBasis::NeighbourHarmony, 0.5);
        }
        return tieBreakOrOpen();
    }

    case AmbiguityKind::ShareTone: {
        if (!hasB) {
            return openMark();
        }
        // Select the reading that participates in a licensed progression into the next.
        const bool aIn = hasNext && isLicensedProgression(toPC(readA), nextChord);
        const bool bIn = hasNext && isLicensedProgression(toPC(readB), nextChord);
        if (aIn != bIn) {
            return pick(aIn ? readA : readB, ResolutionBasis::Progression, 1.0);
        }
        return tieBreakOrOpen();
    }

    case AmbiguityKind::RelativePair: {
        if (!hasB) {
            return openMark();
        }
        // A key/tonic question: the cadence tonic-vote (which candidate tonic receives the
        // cadential arrival / phrase-final emphasis / raised leading tone — all carried in
        // the authentic-cadence vote, §5.2). The two candidate tonics are the two roots.
        const double voteA = cadenceVoteFor(readA.rootPc, cadences);
        const double voteB = cadenceVoteFor(readB.rootPc, cadences);
        if (voteA != voteB) {
            return pick(voteA > voteB ? readA : readB, ResolutionBasis::CadenceVote,
                        std::max(voteA, voteB));
        }
        // The cadence vote did not separate the two centres → the §5.7 prior, then open.
        return tieBreakOrOpen();
    }

    case AmbiguityKind::CloseReading:
    case AmbiguityKind::InsufficientEvidence: {
        if (!hasB) {
            return openMark();
        }
        // Break by functional plausibility (the §5.5 fixed-feature score); the §5.7 prior
        // is the tie-breaker, and where even that does not separate → the honest open mark.
        const double plausA = plausibility(toPC(readA), prevChord, hasPrev, nextChord, hasNext, cadences, params);
        const double plausB = plausibility(toPC(readB), prevChord, hasPrev, nextChord, hasNext, cadences, params);
        if (std::fabs(plausA - plausB) > params.decidingMargin) {
            return pick(plausA > plausB ? readA : readB, ResolutionBasis::Progression,
                        std::max(plausA, plausB));
        }
        return tieBreakOrOpen();
    }

    case AmbiguityKind::SymmetricRotation: {
        // The competing rotations of the symmetric sonority (the full carried pool, deduped
        // by root). Select the rotation that RESOLVES as a licensed leading-tone/applied
        // chord into the next function (the resolution context names which root it is acting
        // as), or that a cadence pins as its leading-tone chord; else genuinely undecidable
        // (the gate-policy class-(a)) → carry the honest open mark, never a guess.
        std::vector<ChordSliceCandidate> pool;
        auto addRotation = [&](const ChordSliceCandidate& c) {
            if (c.rootPc < 0) {
                return;
            }
            for (const ChordSliceCandidate& e : pool) {
                if (e.rootPc == c.rootPc && e.quality == c.quality) {
                    return;
                }
            }
            pool.push_back(c);
        };
        addRotation(readA);
        if (hasB) {
            addRotation(readB);
        }
        for (const ChordSliceCandidate& alt : s.alternatives) {
            addRotation(alt);
        }

        // (1) the unique rotation resolving as an applied/leading-tone chord into the next.
        int appliedHits = 0;
        ChordSliceCandidate appliedPick;
        if (hasNext) {
            for (const ChordSliceCandidate& c : pool) {
                if (isAppliedResolution(toPC(c), nextChord)) {
                    ++appliedHits;
                    appliedPick = c;
                }
            }
        }
        if (appliedHits == 1) {
            return pick(appliedPick, ResolutionBasis::Progression, 1.0);
        }
        // (2) the unique rotation a cadence pins as its leading-tone chord (a cadence whose
        // tonic sits a semitone above the rotation's root — the rotation is its viio).
        int pinHits = 0;
        ChordSliceCandidate pinPick;
        for (const ChordSliceCandidate& c : pool) {
            for (const FunctionalCadence& cad : cadences) {
                if (cad.tonicPc >= 0 && cad.tonicPc == normPc(c.rootPc + 1)) {
                    ++pinHits;
                    pinPick = c;
                    break;
                }
            }
        }
        if (pinHits == 1) {
            return pick(pinPick, ResolutionBasis::CadenceVote, 1.0);
        }
        return openMark();
    }

    case AmbiguityKind::None:
    default:
        // No named ambiguity (or NoteMembership, reserved) → nothing to select among.
        return openMark();
    }
}

/// A committed slice that L5 leaves unchanged (L4's commit stands). The emitted reading
/// IS the slice's own committed identity, carried VERBATIM (root + quality + committed
/// bass/inversion + the carried extensions) — never a reconstruction from the §5.0
/// projection. This is the §7 additive contract: L5 annotates, it does not replace the
/// chord identity Layer 4 committed. For an Inherit slice `s.chosen` is already L4's
/// inherited (prevailing) identity, so the same verbatim carry serves both Commit and
/// Inherit.
ResolvedReading carryThrough(int i, const FunctionSlice& s)
{
    ResolvedReading r;
    r.sliceIndex = i;
    r.wasAbstain = false;
    r.resolved = false;
    r.openMark = false;
    r.overrodeCommit = false;
    r.reading = s.chosen;                 // the committed identity, verbatim (§5.5/§7)
    r.kind = AmbiguityKind::None;
    r.basis = ResolutionBasis::None;
    r.functionConfidence = 0.0;
    return r;
}

// ── The fine-grain override (§5.5 case-4 / §8) ────────────────────────────────
//
// When Layer 4 CONFIDENTLY COMMITTED (decision == Commit) a fine-grain reading the
// established function/cadence contradicts, override it — by SELECTING the corrected
// reading from the carried alternatives or the neighbouring committed harmony (never
// re-deriving), firing per the §8 confidence-weighted threshold. On fire it mutates the
// working progression and triggers the localized forward recompute of the downstream
// readings (the §8 mechanism). Updates result.readings[i] (and, via the recompute,
// downstream entries). Does nothing when no contradiction is decisive.
void attemptFineGrainOverride(int i, Progression& prog,
                              const std::vector<FunctionSlice>& region,
                              const std::vector<FunctionalCadence>& cadences,
                              const ResolverKey& key,
                              const FunctionResolverParams& params,
                              ResolverResult& result)
{
    const FunctionSlice& s = region[static_cast<size_t>(i)];
    if (s.decision != SliceDecision::Commit) {
        return;                                  // §5.5 case-4 is the *committed* override only
    }
    const ProgressionChord committed = s.chord;
    if (committed.rootPc < 0) {
        return;
    }

    // The ADJACENT committed harmony (§5.5 case-4 "the neighbouring committed harmony of
    // the adjacent committed slices") — the nearest committed chord strictly before i and
    // the established next function. (Not prevailingHarmonyIndex(i), which for a committed
    // slice returns i itself — here we want the slice's NEIGHBOURS, the harmony it
    // progresses out of and into.)
    int prevIdx = -1;
    for (int j = i - 1; j >= 0; --j) {
        if (prog[static_cast<size_t>(j)].committed) {
            prevIdx = j;
            break;
        }
    }
    const int nextIdx = establishedNextFunctionIndex(prog, i);
    const bool hasNext = nextIdx >= 0;
    const bool hasPrev = prevIdx >= 0;
    const ProgressionChord nextChord = hasNext ? prog[static_cast<size_t>(nextIdx)].chord : ProgressionChord{};
    const ProgressionChord prevChord = hasPrev ? prog[static_cast<size_t>(prevIdx)].chord : ProgressionChord{};

    const double committedPlaus =
        plausibility(committed, prevChord, hasPrev, nextChord, hasNext, cadences, params);

    // The candidate pool: the carried alternatives ∪ the neighbouring committed harmony
    // (prevailing + established-next) — never the notes. The neighbour enters as its OWN
    // committed identity (region[idx].chosen, carried VERBATIM), not a bare reconstruction:
    // a neighbour SELECTED as the correction is emitted with its own bass/inversion +
    // extensions intact (the source-identity-as-is choice — see the emission note below).
    // Pick the most plausible that is NOT the committed reading.
    std::vector<ChordSliceCandidate> pool = s.alternatives;
    if (hasPrev) {
        pool.push_back(region[static_cast<size_t>(prevIdx)].chosen);
    }
    if (hasNext) {
        pool.push_back(region[static_cast<size_t>(nextIdx)].chosen);
    }

    bool haveBest = false;
    double bestPlaus = 0.0;
    ChordSliceCandidate bestAlt;
    for (const ChordSliceCandidate& c : pool) {
        if (c.rootPc < 0 || sameRootQuality(c, committed)) {
            continue;                            // skip the committed reading itself
        }
        const double p = plausibility(toPC(c), prevChord, hasPrev, nextChord, hasNext, cadences, params);
        if (!haveBest || p > bestPlaus) {
            haveBest = true;
            bestPlaus = p;
            bestAlt = c;
        }
    }
    if (!haveBest) {
        return;                                  // nothing carried to select among
    }

    const double contradictionStrength = bestPlaus - committedPlaus;
    if (contradictionStrength <= 0.0) {
        return;                                  // the context does not contradict the commit
    }

    // §8 case-4: fire iff the contradiction crosses the confidence-scaled bar AND the
    // slice is not already closed. tryOverride marks it final on fire (the closure).
    //
    // ── Confidence-contract FRAME F-B (fine-grain chord override) ────────────────
    // Incumbent (earlierConfidence): the L4 composite confidence of the Commit —
    // `s.confidence.composite`, a Class-M value ALREADY in [0,1] (SliceConfidence, the
    // decoder's own min-composite). It is VERTICAL-FIT-ONLY by construction (no progression
    // term), which the frame's θ accounts for (L5 §15-2). Contradiction (contradictionStrength):
    // the functional-plausibility MARGIN of the contradicting context, `bestPlaus - committedPlaus`
    // (licensed-progression fit + cadential fit) — a separate L5 quantity, NOT FunctionConfidence.
    // NOTE (D-L5a / D-FS): `FunctionConfidence.combined` is the OUTPUT confidence and is NOT read
    // here; the two quantities compared are the ones above. Their scale-commensurability and the
    // θ (baseBar/confidenceScale) are Stage-5 CALIBRATION items (contract §6 C1/C2), not set here.
    if (!result.closure.tryOverride(i, s.confidence.composite, contradictionStrength, params.override)) {
        return;
    }

    ResolvedReading& r = result.readings[static_cast<size_t>(i)];
    r.sliceIndex = i;
    r.wasAbstain = false;
    r.resolved = false;
    r.openMark = false;
    r.overrodeCommit = true;
    // The SELECTED corrected reading, carried VERBATIM (§5.5/§7) — not re-derived. When
    // bestAlt is a carried alternative it already holds THIS slice's own sounding bass;
    // when it is a neighbouring committed harmony it is that source's identity AS-IS
    // (its own bass/inversion). We do NOT pair a neighbour's root/quality with this slice's
    // bass: that hybrid is not itself a carried candidate, so synthesizing it is forbidden
    // (§2/D4). Source-identity-as-is is the safe verbatim choice.
    r.reading = bestAlt;
    r.kind = AmbiguityKind::None;
    r.basis = ResolutionBasis::FineGrainOverride;
    r.functionConfidence = contradictionStrength;

    // The corrected fact propagates forward; re-read the affected downstream region (§8).
    prog[static_cast<size_t>(i)].chord = toPC(bestAlt);
    result.closure.forwardRecompute(i + 1, static_cast<int>(region.size()) - 1,
                                    [&](int j) {
        if (region[static_cast<size_t>(j)].decision == SliceDecision::Abstain) {
            result.readings[static_cast<size_t>(j)] =
                resolveAbstained(j, prog, region, cadences, key, params);
        }
    });
}

} // namespace

ResolverResult
resolveCarriedReadings(const std::vector<FunctionSlice>& region,
                       const std::vector<FunctionalCadence>& cadences,
                       const ResolverKey& key,
                       const FunctionResolverParams& params)
{
    ResolverResult result;
    const int n = static_cast<int>(region.size());
    result.readings.resize(static_cast<size_t>(n));

    Progression prog = buildProgression(region);

    // Phase 1 — base resolution of every abstain against the base progression; commits
    // carry through unchanged (for now).
    for (int i = 0; i < n; ++i) {
        const FunctionSlice& s = region[static_cast<size_t>(i)];
        if (s.decision == SliceDecision::Abstain) {
            result.readings[static_cast<size_t>(i)] =
                resolveAbstained(i, prog, region, cadences, key, params);
        } else {
            result.readings[static_cast<size_t>(i)] = carryThrough(i, s);
        }
    }

    // Phase 2 — the fine-grain overrides, in FORWARD order, each firing a localized
    // forward recompute of the downstream readings (§8). The one-pass closure guarantees
    // each commit is overturned AT MOST ONCE and never re-opened.
    for (int i = 0; i < n; ++i) {
        attemptFineGrainOverride(i, prog, region, cadences, key, params, result);
    }

    return result;
}

} // namespace mu::composing::analysis
