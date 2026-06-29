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

// functionresolver_tests.cpp — Architectural Layer 5 (FUNCTION), Phase 5c Step 3.
//
// Oracle-asserted against known music theory (NOT echoes of the analyzer): the §5.5
// resolver (selection among the L4-carried readings by ambiguity kind) + the §5.7
// bass-degree prior + the §5.5 case-4 fine-grain override (the §8 channel). The build
// obligations (§5):
//   • one resolution per kind — share-tone by the licensed progression; relative-pair
//     by the tonic-vote; symmetric-rotation by the resolution context; transition by
//     the continuation; close by functional plausibility;
//   • a genuinely-undecidable slice → the honest OPEN MARK (not a guess);
//   • the fine-grain override selects the corrected carried/neighbour reading and the
//     §8 closure holds (the overturned commit is not re-opened — no recursion).
// SELECTION, NEVER RE-DERIVATION: every selected reading is one Layer 4 carried (or a
// neighbouring committed chord). Spec: cowork_layer5_function_design.md §5.5/§5.7/§8.

#include <gtest/gtest.h>

#include <vector>

#include "composing/analysis/function/functionresolver.h"

using namespace mu::composing::analysis;

namespace {

// Pitch classes for readability.
constexpr int C = 0, D = 2, Eb = 3, E = 4, F = 5, Fs = 6, G = 7, Gs = 8, A = 9, B = 11;

ChordSliceCandidate cand(int rootPc, ChordQuality q, int bassPc)
{
    ChordSliceCandidate c;
    c.rootPc = rootPc;
    c.quality = q;
    c.bassPc = bassPc;
    return c;
}

FunctionSlice committedSlice(int rootPc, ChordQuality q, int startTick)
{
    FunctionSlice s;
    s.chord = ProgressionChord{ rootPc, q };
    s.committed = true;
    s.decision = SliceDecision::Commit;
    s.metricWeight = 1.0;
    s.startTick = startTick;
    s.endTick = startTick + 480;
    return s;
}

FunctionSlice abstainSlice(AmbiguityKind kind, const ChordSliceCandidate& A,
                           const ChordSliceCandidate& B, bool hasB, int startTick,
                           std::vector<ChordSliceCandidate> alts = {})
{
    FunctionSlice s;
    s.committed = false;
    s.decision = SliceDecision::Abstain;
    s.metricWeight = 1.0;
    s.startTick = startTick;
    s.endTick = startTick + 480;
    s.openQuestion.question = OpenQuestion::Root;
    s.openQuestion.ambiguity = kind;
    s.openQuestion.readingA = A;
    s.openQuestion.readingB = B;
    s.openQuestion.hasReadingB = hasB;
    s.alternatives = std::move(alts);
    return s;
}

FunctionalCadence cadence(int tonicPc, double vote, FunctionalCadenceType type)
{
    FunctionalCadence c;
    c.type = type;
    c.tonicPc = tonicPc;
    c.tonicVote = vote;
    return c;
}

ResolverKey cMajor() { return ResolverKey{ /*fifths*/ 0, KeySigMode::Ionian, /*tonic*/ C }; }

// ── §5.7 the soft bass-/root-scale-degree functional bias (oracle of the mapping) ─

TEST(FunctionResolver, DegreeFunctionalBiasMapping)
{
    EXPECT_EQ(degreeFunctionalBias(0), FunctionalBias::Tonic);        // 1̂
    EXPECT_EQ(degreeFunctionalBias(2), FunctionalBias::Tonic);        // 3̂
    EXPECT_EQ(degreeFunctionalBias(1), FunctionalBias::Predominant);  // 2̂
    EXPECT_EQ(degreeFunctionalBias(3), FunctionalBias::Predominant);  // 4̂
    EXPECT_EQ(degreeFunctionalBias(4), FunctionalBias::Dominant);     // 5̂
    EXPECT_EQ(degreeFunctionalBias(6), FunctionalBias::Dominant);     // 7̂
    EXPECT_EQ(degreeFunctionalBias(5), FunctionalBias::None);         // 6̂ — no lean
    EXPECT_EQ(degreeFunctionalBias(-1), FunctionalBias::None);        // chromatic
    // Through the key: G is 5̂ of C major ⇒ dominant lean; D is 2̂ ⇒ pre-dominant.
    EXPECT_EQ(bassScaleDegreeBias(G, cMajor()), FunctionalBias::Dominant);
    EXPECT_EQ(bassScaleDegreeBias(D, cMajor()), FunctionalBias::Predominant);
}

// ── One resolution per kind (§5.5) ────────────────────────────────────────────

TEST(FunctionResolver, ShareTone_ResolvedByLicensedProgressionIntoNext)
{
    // ii → {Am6 ↔ F#ø7 (same pcs)} → V. Only F#ø7 forms a licensed progression INTO V
    // (F#→G, an ascending semitone); Am6→G (a descending whole step) is not licensed.
    std::vector<FunctionSlice> region{
        committedSlice(D, ChordQuality::Minor, 0),
        abstainSlice(AmbiguityKind::ShareTone,
                     cand(A, ChordQuality::Minor, A),            // readingA = Am6
                     cand(Fs, ChordQuality::HalfDiminished, Fs), // readingB = F#ø7
                     /*hasB*/ true, 480),
        committedSlice(G, ChordQuality::Major, 960),
    };
    const ResolverResult r = resolveCarriedReadings(region, {}, cMajor());
    ASSERT_EQ(r.readings.size(), 3u);
    const ResolvedReading& rr = r.readings[1];
    EXPECT_TRUE(rr.resolved);
    EXPECT_FALSE(rr.openMark);
    EXPECT_EQ(rr.reading.rootPc, Fs);                            // the licensed reading selected
    EXPECT_EQ(rr.basis, ResolutionBasis::Progression);
}

TEST(FunctionResolver, Transition_ResolvedAsArrivingFunction)
{
    // I → {D7 (V/V, belongs to the arriving V) ↔ C (passing within I)} → V. D7 forms a
    // licensed progression into V (descending fifth); the slice "belongs to the arriving
    // function", so D7 is selected.
    std::vector<FunctionSlice> region{
        committedSlice(C, ChordQuality::Major, 0),
        abstainSlice(AmbiguityKind::TransitionVsContinuation,
                     cand(D, ChordQuality::Major, D),   // readingA = D7 (arriving)
                     cand(C, ChordQuality::Major, C),   // readingB = C (passing)
                     /*hasB*/ true, 480),
        committedSlice(G, ChordQuality::Major, 960),
    };
    const ResolverResult r = resolveCarriedReadings(region, {}, cMajor());
    const ResolvedReading& rr = r.readings[1];
    EXPECT_TRUE(rr.resolved);
    EXPECT_EQ(rr.reading.rootPc, D);
    EXPECT_EQ(rr.basis, ResolutionBasis::Progression);
}

TEST(FunctionResolver, Transition_ResolvedAsNeighbourWithinPrevailing)
{
    // I → {C (continues I) ↔ Eb (unrelated)} → bVII. Neither reading is licensed into the
    // next (C→Bb, Eb→Bb both unlicensed), so the slice reduces to a neighbour figure
    // within the prevailing harmony: the reading matching prevailing I (C) is selected.
    constexpr int Bb = 10;
    std::vector<FunctionSlice> region{
        committedSlice(C, ChordQuality::Major, 0),
        abstainSlice(AmbiguityKind::TransitionVsContinuation,
                     cand(C, ChordQuality::Major, C),    // readingA = C (continues prevailing)
                     cand(Eb, ChordQuality::Major, Eb),  // readingB = Eb (unrelated)
                     /*hasB*/ true, 480),
        committedSlice(Bb, ChordQuality::Major, 960),
    };
    const ResolverResult r = resolveCarriedReadings(region, {}, cMajor());
    const ResolvedReading& rr = r.readings[1];
    EXPECT_TRUE(rr.resolved);
    EXPECT_EQ(rr.reading.rootPc, C);
    EXPECT_EQ(rr.basis, ResolutionBasis::NeighbourHarmony);
}

TEST(FunctionResolver, RelativePair_ResolvedByCadenceTonicVote)
{
    // {C ↔ Am} (the relative pair). A cadence votes for A as the tonal centre ⇒ the
    // minor reading (Am) is selected — the cadence tonic-vote settles the key question.
    std::vector<FunctionSlice> region{
        abstainSlice(AmbiguityKind::RelativePair,
                     cand(C, ChordQuality::Major, C),   // readingA = C major
                     cand(A, ChordQuality::Minor, A),   // readingB = A minor
                     /*hasB*/ true, 0),
    };
    std::vector<FunctionalCadence> cadences{
        cadence(/*tonic*/ A, /*vote*/ 3.0, FunctionalCadenceType::PerfectAuthentic),
    };
    const ResolverResult r = resolveCarriedReadings(region, cadences, cMajor());
    const ResolvedReading& rr = r.readings[0];
    EXPECT_TRUE(rr.resolved);
    EXPECT_EQ(rr.reading.rootPc, A);
    EXPECT_EQ(rr.basis, ResolutionBasis::CadenceVote);
}

TEST(FunctionResolver, Close_ResolvedByFunctionalPlausibility)
{
    // ii → {G ↔ Ab} → I. G forms licensed progressions both OUT of ii (descending fifth)
    // and INTO I (descending fifth); Ab forms neither. Functional plausibility selects G.
    std::vector<FunctionSlice> region{
        committedSlice(D, ChordQuality::Minor, 0),
        abstainSlice(AmbiguityKind::CloseReading,
                     cand(G, ChordQuality::Major, G),     // readingA = G (plausible)
                     cand(Gs, ChordQuality::Major, Gs),   // readingB = Ab (implausible)
                     /*hasB*/ true, 480),
        committedSlice(C, ChordQuality::Major, 960),
    };
    const ResolverResult r = resolveCarriedReadings(region, {}, cMajor());
    const ResolvedReading& rr = r.readings[1];
    EXPECT_TRUE(rr.resolved);
    EXPECT_EQ(rr.reading.rootPc, G);
    EXPECT_EQ(rr.basis, ResolutionBasis::Progression);
}

TEST(FunctionResolver, Insufficient_GenuinelyUndecidable_CarriesOpenMark)
{
    // A too-thin slice with no second reading to select among → the honest open mark,
    // never a guess (§7). The top reading is carried as the displayed-but-uncertain one.
    std::vector<FunctionSlice> region{
        abstainSlice(AmbiguityKind::InsufficientEvidence,
                     cand(E, ChordQuality::Major, E),
                     ChordSliceCandidate{}, /*hasB*/ false, 0),
    };
    const ResolverResult r = resolveCarriedReadings(region, {}, cMajor());
    const ResolvedReading& rr = r.readings[0];
    EXPECT_FALSE(rr.resolved);
    EXPECT_TRUE(rr.openMark);
    EXPECT_EQ(rr.basis, ResolutionBasis::None);
    EXPECT_EQ(rr.kind, AmbiguityKind::InsufficientEvidence);
}

TEST(FunctionResolver, SymmetricRotation_ResolvedByResolutionContext)
{
    // A fully-diminished seventh {G#,B,D,F} (four rotations) → Am. Exactly one rotation —
    // G#dim7 — resolves as a leading-tone chord into the target (G#→A, a semitone), so
    // the symmetric sonority is pinned as G#dim7 (viio7 of A). The others do not resolve.
    std::vector<FunctionSlice> region{
        abstainSlice(AmbiguityKind::SymmetricRotation,
                     cand(B, ChordQuality::Diminished, B),    // readingA = Bdim7 (the scorer's pick)
                     cand(Gs, ChordQuality::Diminished, B),   // readingB = G#dim7
                     /*hasB*/ true, 0,
                     { cand(D, ChordQuality::Diminished, B),  // alternatives: the other rotations
                       cand(F, ChordQuality::Diminished, B) }),
        committedSlice(A, ChordQuality::Minor, 480),
    };
    const ResolverResult r = resolveCarriedReadings(region, {}, cMajor());
    const ResolvedReading& rr = r.readings[0];
    EXPECT_TRUE(rr.resolved);
    EXPECT_EQ(rr.reading.rootPc, Gs);                          // the resolving rotation
    EXPECT_EQ(rr.basis, ResolutionBasis::Progression);
}

TEST(FunctionResolver, SymmetricRotation_NoResolution_CarriesOpenMark)
{
    // The same diminished-seventh rotations → Em, into which NO rotation resolves as a
    // leading-tone/applied chord, and no cadence pins one. Genuinely undecidable
    // (class-(a)) → the honest open mark; no rotation is guessed.
    std::vector<FunctionSlice> region{
        abstainSlice(AmbiguityKind::SymmetricRotation,
                     cand(B, ChordQuality::Diminished, B),
                     cand(Gs, ChordQuality::Diminished, B),
                     /*hasB*/ true, 0,
                     { cand(D, ChordQuality::Diminished, B),
                       cand(F, ChordQuality::Diminished, B) }),
        committedSlice(E, ChordQuality::Minor, 480),
    };
    const ResolverResult r = resolveCarriedReadings(region, {}, cMajor());
    const ResolvedReading& rr = r.readings[0];
    EXPECT_FALSE(rr.resolved);
    EXPECT_TRUE(rr.openMark);
}

TEST(FunctionResolver, SymmetricRotation_ResolvedByCadencePin)
{
    // The same diminished-seventh rotations as the LAST slice (no committed successor, so
    // the applied-resolution path has no target). A cadence on A pins the rotation whose
    // root is a semitone BELOW A — G#dim7, the viio7 of A — as the reading. This exercises
    // the §5.5 cadence-pin branch (distinct from the applied-resolution branch above).
    std::vector<FunctionSlice> region{
        abstainSlice(AmbiguityKind::SymmetricRotation,
                     cand(B, ChordQuality::Diminished, B),    // readingA = Bdim7 (the scorer's pick)
                     cand(Gs, ChordQuality::Diminished, B),   // readingB = G#dim7
                     /*hasB*/ true, 0,
                     { cand(D, ChordQuality::Diminished, B),  // alternatives: the other rotations
                       cand(F, ChordQuality::Diminished, B) }),
    };
    const std::vector<FunctionalCadence> cadences{
        cadence(/*tonic*/ A, /*vote*/ 3.0, FunctionalCadenceType::PerfectAuthentic),
    };
    const ResolverResult r = resolveCarriedReadings(region, cadences, cMajor());
    const ResolvedReading& rr = r.readings[0];
    EXPECT_TRUE(rr.resolved);
    EXPECT_FALSE(rr.openMark);
    EXPECT_EQ(rr.reading.rootPc, Gs);                         // the cadence-pinned rotation (A's viio)
    EXPECT_EQ(rr.basis, ResolutionBasis::CadenceVote);
}

TEST(FunctionResolver, BassDegreePrior_BreaksAnOtherwiseExactTie)
{
    // A lone slice with no progression/cadence context ⇒ functional plausibility ties at
    // 0. The §5.7 prior breaks it: the bass is 5̂ (G, a dominant lean); G major's root is
    // 5̂ (dominant) — it matches; Em (first inversion, same bass) roots on 3̂ (tonic) — it
    // does not. So G is selected by the soft prior (never a gate).
    std::vector<FunctionSlice> region{
        abstainSlice(AmbiguityKind::CloseReading,
                     cand(G, ChordQuality::Major, G),   // readingA = G (root 5̂, bass G)
                     cand(E, ChordQuality::Minor, G),   // readingB = Em6/4-ish, bass G (root 3̂)
                     /*hasB*/ true, 0),
    };
    const ResolverResult r = resolveCarriedReadings(region, {}, cMajor());
    const ResolvedReading& rr = r.readings[0];
    EXPECT_TRUE(rr.resolved);
    EXPECT_EQ(rr.reading.rootPc, G);
    EXPECT_EQ(rr.basis, ResolutionBasis::BassDegreePrior);
}

// ── The fine-grain override (§5.5 case-4 / §8) ────────────────────────────────

TEST(FunctionResolver, FineGrainOverride_SelectsCorrectedCarriedReading_ClosureHolds)
{
    // ii → [Commit = Ab, contextually wrong] → I. The carried alternative G is far more
    // plausible (ii→G→I, two licensed fifths) than the committed Ab (neither licensed).
    // With a borderline confidence (composite 0.5 ⇒ §8 bar 1.5) the strength-2
    // contradiction overturns the commit; G is SELECTED (not re-derived). The §8 closure
    // then holds: the overturned slice is closed and cannot be re-targeted in the pass.
    FunctionSlice wrongCommit = committedSlice(Gs, ChordQuality::Major, 480);  // committed Ab
    wrongCommit.alternatives = { cand(G, ChordQuality::Major, G) };            // the carried correction
    wrongCommit.confidence.composite = 0.5;

    std::vector<FunctionSlice> region{
        committedSlice(D, ChordQuality::Minor, 0),
        wrongCommit,
        committedSlice(C, ChordQuality::Major, 960),
    };
    ResolverResult r = resolveCarriedReadings(region, {}, cMajor());
    const ResolvedReading& rr = r.readings[1];
    EXPECT_TRUE(rr.overrodeCommit);
    EXPECT_FALSE(rr.openMark);
    EXPECT_EQ(rr.reading.rootPc, G);                       // the SELECTED corrected reading
    EXPECT_EQ(rr.basis, ResolutionBasis::FineGrainOverride);

    // §8 closure: the overturned decision is final for the pass — a re-attempt is refused.
    EXPECT_TRUE(r.closure.isClosed(1));
    EXPECT_FALSE(r.closure.tryOverride(1, /*conf*/ 0.0, /*strength*/ 999.0));
    EXPECT_EQ(r.closure.closedCount(), 1);                 // exactly one override, no recursion
    EXPECT_FALSE(r.closure.isRecomputing());               // the recompute completed and unwound
}

TEST(FunctionResolver, FineGrainOverride_DoesNotFireOnAVeryConfidentCommit)
{
    // The SAME contradiction (strength 2) against a MAXIMALLY confident commit
    // (composite 1.0 ⇒ §8 bar 2.0) does NOT fire: a well-founded confident commit demands
    // strictly stronger contradicting evidence. The commit stands; nothing is closed.
    FunctionSlice confidentCommit = committedSlice(Gs, ChordQuality::Major, 480);
    confidentCommit.alternatives = { cand(G, ChordQuality::Major, G) };
    confidentCommit.confidence.composite = 1.0;

    std::vector<FunctionSlice> region{
        committedSlice(D, ChordQuality::Minor, 0),
        confidentCommit,
        committedSlice(C, ChordQuality::Major, 960),
    };
    const ResolverResult r = resolveCarriedReadings(region, {}, cMajor());
    const ResolvedReading& rr = r.readings[1];
    EXPECT_FALSE(rr.overrodeCommit);
    EXPECT_EQ(rr.reading.rootPc, Gs);                      // L4's commit stands, unchanged
    EXPECT_FALSE(r.closure.isClosed(1));
}

TEST(FunctionResolver, PlainCommitsCarryThroughUnchanged)
{
    // A clean I–V–I region: every slice is a confident, context-consistent commit, so the
    // resolver changes nothing — no overrides, no open marks (L5 is additive).
    std::vector<FunctionSlice> region{
        committedSlice(C, ChordQuality::Major, 0),
        committedSlice(G, ChordQuality::Major, 480),
        committedSlice(C, ChordQuality::Major, 960),
    };
    const ResolverResult r = resolveCarriedReadings(region, {}, cMajor());
    for (const ResolvedReading& rr : r.readings) {
        EXPECT_FALSE(rr.overrodeCommit);
        EXPECT_FALSE(rr.openMark);
        EXPECT_FALSE(rr.resolved);
    }
    EXPECT_EQ(r.closure.closedCount(), 0);
}

} // namespace
