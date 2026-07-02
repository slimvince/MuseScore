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

#include <memory>
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

// A candidate carrying a full committed identity — a real seventh/extension extraction
// (extensionsKnown = true) with an explicit bass/inversion — for the verbatim-carry tests.
ChordSliceCandidate candFull(int rootPc, ChordQuality q, int bassPc, uint32_t extensions)
{
    ChordSliceCandidate c = cand(rootPc, q, bassPc);
    c.extensions = extensions;
    c.extensionsKnown = true;
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
    // The committed FULL identity the resolver carries verbatim (root-position triad by
    // default; toPC(chosen) == chord). Tests needing a seventh/inversion set s.chosen after.
    s.chosen = candFull(rootPc, q, rootPc, /*extensions*/ 0u);
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

// ── Verbatim identity carry (carry-fix 2, §5.5/§7) ────────────────────────────

TEST(FunctionResolver, PassThrough_PreservesCommittedBassAndExtensions)
{
    // A committed dominant seventh in first inversion (G7/B — bass B ≠ root G, a MinorSeventh
    // extension): the resolver leaves the commit standing and must emit its identity VERBATIM,
    // NOT a bare root-position reconstruction. The committed bass and the seventh survive.
    const uint32_t b7 = static_cast<uint32_t>(Extension::MinorSeventh);
    FunctionSlice v65 = committedSlice(G, ChordQuality::Major, 480);
    v65.chosen = candFull(G, ChordQuality::Major, /*bass*/ B, b7);   // G7/B (a "65" figure)

    std::vector<FunctionSlice> region{
        committedSlice(C, ChordQuality::Major, 0),
        v65,
        committedSlice(C, ChordQuality::Major, 960),
    };
    const ResolverResult r = resolveCarriedReadings(region, {}, cMajor());
    const ResolvedReading& rr = r.readings[1];
    EXPECT_FALSE(rr.overrodeCommit);
    EXPECT_FALSE(rr.openMark);
    EXPECT_EQ(rr.reading.rootPc, G);
    EXPECT_EQ(rr.reading.bassPc, B);            // the committed inversion survives (not flattened to root)
    EXPECT_FALSE(rr.reading.bassIsRoot());
    EXPECT_TRUE(rr.reading.extensionsKnown);    // a real extraction, carried
    EXPECT_EQ(rr.reading.extensions & b7, b7);  // the seventh survives to the formatter
}

TEST(FunctionResolver, Inherit_CarriesPrevailingSeventh)
{
    // An Inherit slice whose L4 `chosen` is the prevailing dominant-seventh identity: the
    // resolver carries THAT identity forward verbatim (the seventh is not dropped on inherit).
    const uint32_t b7 = static_cast<uint32_t>(Extension::MinorSeventh);
    FunctionSlice inherited = committedSlice(G, ChordQuality::Major, 480);
    inherited.decision = SliceDecision::Inherit;
    inherited.chosen = candFull(G, ChordQuality::Major, /*bass*/ G, b7);   // inherited G7

    std::vector<FunctionSlice> region{
        committedSlice(G, ChordQuality::Major, 0),
        inherited,
        committedSlice(C, ChordQuality::Major, 960),
    };
    const ResolverResult r = resolveCarriedReadings(region, {}, cMajor());
    const ResolvedReading& rr = r.readings[1];
    EXPECT_FALSE(rr.overrodeCommit);
    EXPECT_FALSE(rr.openMark);
    EXPECT_EQ(rr.reading.rootPc, G);
    EXPECT_TRUE(rr.reading.extensionsKnown);
    EXPECT_EQ(rr.reading.extensions & b7, b7);  // the inherited seventh is carried
}

TEST(FunctionResolver, Override_HonestCarryAlternative_StaysTriadLevel)
{
    // The fine-grain override selects a carried alternative that is HONEST-CARRY
    // (extensionsKnown = false — its seventh was unobtainable at the L4→L5 boundary). The
    // selected reading is emitted VERBATIM, so it stays honestly triad-level: the resolver
    // does not fabricate an extension, and does not assert the seventh absent — it carries
    // the unknown state through.
    FunctionSlice wrongCommit = committedSlice(Gs, ChordQuality::Major, 480);  // committed Ab
    wrongCommit.alternatives = { cand(G, ChordQuality::Major, G) };            // honest-carry (extKnown=false)
    wrongCommit.confidence.composite = 0.5;

    std::vector<FunctionSlice> region{
        committedSlice(D, ChordQuality::Minor, 0),
        wrongCommit,
        committedSlice(C, ChordQuality::Major, 960),
    };
    const ResolverResult r = resolveCarriedReadings(region, {}, cMajor());
    const ResolvedReading& rr = r.readings[1];
    EXPECT_TRUE(rr.overrodeCommit);
    EXPECT_EQ(rr.reading.rootPc, G);            // the SELECTED corrected reading
    EXPECT_FALSE(rr.reading.extensionsKnown);   // honest-carry state preserved (unknown, not guessed)
    EXPECT_EQ(rr.reading.extensions, 0u);       // no fabricated extension
}

// ════════════════════════════════════════════════════════════════════════════
// Bounded context — the pinned decision-context extent + forward requester loop
// (resolveCarriedReadingsExtending; design §5; cowork_bounded_context_design.md §3/§4/§5).
// DORMANT: enableForwardExtension defaults OFF; no production consumer. The supplier is the
// L1-extend → L2 → L3/L4 forward re-run, injected by hand here.
// ════════════════════════════════════════════════════════════════════════════

namespace {

// A one-shot forward supplier: appends @p batch on the FIRST request, then reports @p after
// (ScoreBoundary by default) on every subsequent request. Deterministic (a shared counter).
ForwardExtensionProvider oneShot(std::vector<FunctionSlice> batch,
                                 ForwardSupply after = ForwardSupply::ScoreBoundary)
{
    auto calls = std::make_shared<int>(0);
    ForwardExtensionProvider p;
    p.supply = [batch, after, calls](int, std::vector<FunctionSlice>& more,
                                      std::vector<FunctionalCadence>&) -> ForwardSupply {
        if ((*calls)++ == 0) {
            more = batch;
            return ForwardSupply::Supplied;
        }
        return after;
    };
    return p;
}

// A supplier that always reports the given terminal status (never supplies).
ForwardExtensionProvider terminal(ForwardSupply status)
{
    ForwardExtensionProvider p;
    p.supply = [status](int, std::vector<FunctionSlice>&, std::vector<FunctionalCadence>&) {
        return status;
    };
    return p;
}

L5ForwardExtensionParams extOn(int k = 8)
{
    L5ForwardExtensionParams e;
    e.enableForwardExtension = true;
    e.maxForwardExtendSlices = k;
    return e;
}

// A region ending in a cut ShareTone abstain: ii(Dm) → {Am6 ↔ F#ø7}, no forward function.
std::vector<FunctionSlice> cutTailRegion()
{
    return {
        committedSlice(D, ChordQuality::Minor, 0),
        abstainSlice(AmbiguityKind::ShareTone,
                     cand(A, ChordQuality::Minor, A),             // readingA = Am6
                     cand(Fs, ChordQuality::HalfDiminished, Fs),  // readingB = F#ø7
                     /*hasB*/ true, 480),
    };
}

} // namespace

// L5EXT1 — DORMANT: enableForwardExtension OFF ⇒ byte-identical to resolveCarriedReadings, no
// provenance (cowork_bounded_context_design.md §8).
TEST(FunctionResolver, L5EXT1_DisabledEqualsBaseResolver_NoProvenance)
{
    const std::vector<FunctionSlice> region = cutTailRegion();
    const ResolverResult base = resolveCarriedReadings(region, {}, cMajor());
    const ResolverResult ext = resolveCarriedReadingsExtending(
        region, {}, cMajor(), oneShot({ committedSlice(G, ChordQuality::Major, 960) }),
        kDefaultFunctionResolverParams, /*ext*/ L5ForwardExtensionParams{});   // enable OFF

    ASSERT_EQ(ext.readings.size(), base.readings.size());
    for (size_t i = 0; i < ext.readings.size(); ++i) {
        EXPECT_EQ(ext.readings[i].resolved, base.readings[i].resolved);
        EXPECT_EQ(ext.readings[i].openMark, base.readings[i].openMark);
        EXPECT_EQ(ext.readings[i].reading.rootPc, base.readings[i].reading.rootPc);
        EXPECT_FALSE(ext.readings[i].clippedBySelectionEdge) << "OFF sets no provenance";
        EXPECT_FALSE(ext.readings[i].cueDenied);
    }
}

// L5EXT2 — must-FIRE + resolve: the edge abstain is cut (no forward function), so the base pass
// leaves it an OPEN MARK; supplying the forward V(G) establishes the next function, and the
// forward re-run RESOLVES the ShareTone by the licensed progression into G (→ F#ø7). Output is
// the selection only (the reached-forward G is evidence, not emitted); the resolved slice is no
// longer cut, so it carries NO clip.
TEST(FunctionResolver, L5EXT2_CutAbstain_RequestFiresAndResolves)
{
    const std::vector<FunctionSlice> region = cutTailRegion();

    // Base (no forward context): the edge ShareTone can't see its next function → open mark.
    const ResolverResult base = resolveCarriedReadings(region, {}, cMajor());
    ASSERT_EQ(base.readings.size(), 2u);
    EXPECT_TRUE(base.readings[1].openMark) << "with no forward context the edge abstain is open";

    // Extend: supply the forward V(G). The re-run resolves the abstain to F#ø7.
    const ResolverResult ext = resolveCarriedReadingsExtending(
        region, {}, cMajor(), oneShot({ committedSlice(G, ChordQuality::Major, 960) }),
        kDefaultFunctionResolverParams, extOn());

    ASSERT_EQ(ext.readings.size(), 2u) << "output covers the selection only (forward G is evidence)";
    EXPECT_TRUE(ext.readings[1].resolved) << "the extension resolved the previously-open abstain";
    EXPECT_EQ(ext.readings[1].reading.rootPc, Fs) << "resolved by licensed progression into V";
    EXPECT_FALSE(ext.readings[1].clippedBySelectionEdge) << "resolved ⇒ no longer cut";
    EXPECT_FALSE(ext.readings[1].cueDenied);
}

// L5EXT3 — denial provenance: the supplier REFUSES the request (a driver safety cap), so the
// edge abstain resolves on its truncated evidence (open mark) and carries BOTH clip + cueDenied.
TEST(FunctionResolver, L5EXT3_RefusedRequest_OpenMarkPlusDenialProvenance)
{
    const std::vector<FunctionSlice> region = cutTailRegion();
    const ResolverResult ext = resolveCarriedReadingsExtending(
        region, {}, cMajor(), terminal(ForwardSupply::Refused), kDefaultFunctionResolverParams, extOn());

    ASSERT_EQ(ext.readings.size(), 2u);
    EXPECT_TRUE(ext.readings[1].openMark) << "a refused request proceeds on truncated evidence";
    EXPECT_TRUE(ext.readings[1].clippedBySelectionEdge) << "the decision-context span was cut";
    EXPECT_TRUE(ext.readings[1].cueDenied) << "a refusal is a denial (item 10)";
}

// L5EXT4 — score boundary: the supplier reports the score end (nothing more exists). The edge
// abstain proceeds truncated (open mark) and carries the clip provenance but NOT cueDenied — a
// score-boundary truncation is honest, not a denial (design §3 item 3 / item 10).
TEST(FunctionResolver, L5EXT4_ScoreBoundary_ClipButNotDenied)
{
    const std::vector<FunctionSlice> region = cutTailRegion();
    const ResolverResult ext = resolveCarriedReadingsExtending(
        region, {}, cMajor(), terminal(ForwardSupply::ScoreBoundary), kDefaultFunctionResolverParams, extOn());

    ASSERT_EQ(ext.readings.size(), 2u);
    EXPECT_TRUE(ext.readings[1].openMark);
    EXPECT_TRUE(ext.readings[1].clippedBySelectionEdge) << "cut by the score boundary — truncated evidence";
    EXPECT_FALSE(ext.readings[1].cueDenied) << "a score-boundary stop is not a denial";
}

// L5EXT5 — §8 one-pass closure (NO RE-OPEN): a decision the base pass CLOSED (an interior abstain
// resolved because its forward function is already in view) keeps its reading after a forward
// extension finalizes a LATER edge-cut decision — forward data supply, never a back-edge.
TEST(FunctionResolver, L5EXT5_ForwardExtension_DoesNotReopenClosedDecision)
{
    // [ I(C) , abstain#1 (interior, resolvable → F#ø7) , V(G) , abstain#2 (edge, cut) ]
    std::vector<FunctionSlice> region{
        committedSlice(C, ChordQuality::Major, 0),
        abstainSlice(AmbiguityKind::ShareTone,
                     cand(A, ChordQuality::Minor, A), cand(Fs, ChordQuality::HalfDiminished, Fs),
                     /*hasB*/ true, 480),
        committedSlice(G, ChordQuality::Major, 960),
        abstainSlice(AmbiguityKind::ShareTone,
                     cand(A, ChordQuality::Minor, A), cand(Fs, ChordQuality::HalfDiminished, Fs),
                     /*hasB*/ true, 1440),
    };

    // Base: abstain#1 (index 1) resolves (G in view forward); abstain#2 (index 3) is cut → open.
    const ResolverResult base = resolveCarriedReadings(region, {}, cMajor());
    ASSERT_EQ(base.readings.size(), 4u);
    ASSERT_TRUE(base.readings[1].resolved);
    const int closedRoot = base.readings[1].reading.rootPc;   // the closed decision's reading
    ASSERT_TRUE(base.readings[3].openMark);

    // Extend: supply a forward V(G) so abstain#2 (F#ø7 → G is licensed) can resolve. abstain#1
    // is untouched (its forward function was already in view — a closed decision).
    const ResolverResult ext = resolveCarriedReadingsExtending(
        region, {}, cMajor(), oneShot({ committedSlice(G, ChordQuality::Major, 1920) }),
        kDefaultFunctionResolverParams, extOn());

    ASSERT_EQ(ext.readings.size(), 4u) << "output covers the original selection only";
    // The base-closed interior decision is UNCHANGED (never re-opened).
    EXPECT_TRUE(ext.readings[1].resolved);
    EXPECT_EQ(ext.readings[1].reading.rootPc, closedRoot) << "a closed decision must not be re-opened";
    EXPECT_FALSE(ext.readings[1].clippedBySelectionEdge);
    // The edge decision was finalized by the extension.
    EXPECT_TRUE(ext.readings[3].resolved) << "the forward extension finalized the open edge decision";
    EXPECT_FALSE(ext.readings[3].clippedBySelectionEdge) << "resolved ⇒ no longer cut";
}

// L5EXT6 — determinism: identical inputs ⇒ identical readings + provenance.
TEST(FunctionResolver, L5EXT6_Deterministic)
{
    const std::vector<FunctionSlice> region = cutTailRegion();
    const ResolverResult a = resolveCarriedReadingsExtending(
        region, {}, cMajor(), terminal(ForwardSupply::Refused), kDefaultFunctionResolverParams, extOn());
    const ResolverResult b = resolveCarriedReadingsExtending(
        region, {}, cMajor(), terminal(ForwardSupply::Refused), kDefaultFunctionResolverParams, extOn());
    ASSERT_EQ(a.readings.size(), b.readings.size());
    for (size_t i = 0; i < a.readings.size(); ++i) {
        EXPECT_EQ(a.readings[i].reading.rootPc, b.readings[i].reading.rootPc);
        EXPECT_EQ(a.readings[i].openMark, b.readings[i].openMark);
        EXPECT_EQ(a.readings[i].clippedBySelectionEdge, b.readings[i].clippedBySelectionEdge);
        EXPECT_EQ(a.readings[i].cueDenied, b.readings[i].cueDenied);
    }
}

// L5EXT7 — the §4 equivalence invariant: the result after the extension equals a SINGLE fresh
// resolve over the final (enlarged) region, restricted to the selection slices. Extension is
// "supply more forward data, then infer forward again" — never a different computation.
TEST(FunctionResolver, L5EXT7_ExtensionEqualsFreshRunOverFinalRegion)
{
    const std::vector<FunctionSlice> selection = cutTailRegion();          // 2 selection slices
    const std::vector<FunctionSlice> batch{ committedSlice(G, ChordQuality::Major, 960) };

    // The extended run (supply the forward G once, then converge).
    const ResolverResult ext = resolveCarriedReadingsExtending(
        selection, {}, cMajor(), oneShot(batch), kDefaultFunctionResolverParams, extOn());

    // The fresh run over the final region = selection ++ batch, restricted to the selection.
    std::vector<FunctionSlice> finalRegion = selection;
    finalRegion.insert(finalRegion.end(), batch.begin(), batch.end());
    const ResolverResult fresh = resolveCarriedReadings(finalRegion, {}, cMajor());

    ASSERT_EQ(ext.readings.size(), selection.size());
    ASSERT_GE(fresh.readings.size(), selection.size());
    for (size_t i = 0; i < selection.size(); ++i) {
        EXPECT_EQ(ext.readings[i].resolved, fresh.readings[i].resolved) << "slice " << i;
        EXPECT_EQ(ext.readings[i].openMark, fresh.readings[i].openMark) << "slice " << i;
        EXPECT_EQ(ext.readings[i].reading.rootPc, fresh.readings[i].reading.rootPc) << "slice " << i;
        EXPECT_EQ(ext.readings[i].basis, fresh.readings[i].basis) << "slice " << i;
    }
}

} // namespace
