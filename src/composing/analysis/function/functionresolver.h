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

// ── composing/analysis/function/functionresolver ─────────────────────────────
//
// Architectural Layer 5 (FUNCTION) — THE RESOLVER (§5.5) + THE FINE-GRAIN OVERRIDE
// (§5.5 case-4 / §10, the §8 channel #2). Spec: cowork_layer5_function_design.md
// (SIGNED) §5.5 + §5.7 + §8 + the §5.0 shared defs. Build plan:
// cowork_phase5c_l5_build_plan.md Step 3.
//
// TWO DUTIES, ONE SELECTION MACHINERY (§5.5):
//   • RESOLVE (§8 case 2): for each slice Layer 4 ABSTAINED on, SELECT among the
//     carried readings by the NAMED ambiguity kind, using the progression model
//     (Step 1), the cadence tonic-vote (Step 2), and the soft bass-scale-degree prior
//     (§5.7) — never re-deriving from notes, carrying the honest OPEN MARK (§7) where
//     the evidence decides nothing.
//   • OVERRIDE (§8 case 4): when Layer 4 CONFIDENTLY COMMITTED a fine-grain reading the
//     established function/cadence contradicts (the class-(b) override duty, §10),
//     OVERRIDE it — but by the SAME constraint: SELECT the corrected reading from the
//     carried alternatives or the neighbouring committed harmony (§5.0) of the adjacent
//     committed slices, never re-deriving — firing per the confidence-weighted threshold
//     of §8 (the reusable forwardoverride mechanism, built at this step).
//
// SELECTION, NOT RE-DERIVATION (§2 constraint / D4). The candidate set is CLOSED by
// Layer 4 (the carried readings + the neighbouring committed chords); this layer never
// re-scores from the notes nor introduces a chord Layer 4 did not carry. That is the
// structural content of resolving "uncertain" by selection.
//
// REUSE, NOT DUPLICATE (build §1). The resolver REUSES:
//   • functionprogression — isLicensedProgression / prevailingHarmonyIndex /
//     establishedNextFunctionIndex (the §5.0 evidence);
//   • functioncadence     — the detected FunctionalCadence stream + its tonic votes;
//   • forwardoverride     — the §8 confidence-weighted threshold + one-pass closure +
//     localized forward recompute (the fine-grain override fires through it);
//   • region::diatonicDegreeForRootPc — the §5.7 bass-/root-scale-degree (in the .cpp).
// It introduces only the per-kind selection rules and the §5.7 prior helper.
//
// THE CARRIED-READING CONTRACT IS CONSUMED DIRECTLY (build-detail decision, declared in
// cc_phase5c_step3_report.md). The resolver reads the L4→L5 forward-carry value types —
// AmbiguityKind, OpenQuestion, OpenQuestionLabel, SliceConfidence, ChordSliceCandidate,
// SliceDecision (chord/chordslicedecoder.h) — DIRECTLY rather than re-wrapping them in
// parallel view types. These ARE the representational contract Layer 4 built FOR Layer 5
// ("the L4→L5 abstain contract … so L5 selects among them"); §5.5 fixes that this layer
// "adds no new ambiguity kind", so duplicating the enum/structs would only create a
// drift hazard. This mirrors the functionromannumeral precedent (it includes
// chordanalyzer.h for ChordIdentity). The resolver still does NOT consume the decoder
// ENGINE, the region assembler, or any score/engraving type — it reads the value structs
// and the already-built producer-agnostic view types (Progression, FunctionalCadence),
// so it stays hand-injectable in tests.
//
// CONSTANTS ARE PRECISION-PHASE (the firewall, build §4). The functional-plausibility
// weights, the deciding margin, and the §8 override threshold are DEFAULT seeds and are
// NOT tuned for accuracy — that is Phase B. Only the DIRECTIONS are fixed (more licensed
// fit / cadential support ⇒ more plausible; a more-confident commit ⇒ harder to
// overturn; ties resolve toward the incumbent / the honest open mark).
//
// DORMANT (build §6): NO production consumer — nothing in src/ calls it; exercised only
// by its unit tests. Byte-identical on production by construction; load-bearing when the
// function layer engages (Phase 5d).

#include <functional>
#include <vector>

#include "composing/analysis/chord/chordslicedecoder.h"  // the L4→L5 carried-reading contract
#include "composing/analysis/types/analysistypes.h"      // ChordQuality, KeySigMode
#include "functioncadence.h"                              // FunctionalCadence (the tonic votes)
#include "functionprogression.h"                          // Progression / the §5.0 queries
#include "forwardoverride.h"                              // the §8 mechanism

namespace mu::composing::analysis {

// The L4→L5 carried-reading contract is declared in the nested `chordslice` namespace
// (chord/chordslicedecoder.h). Bring the value types this layer consumes into scope so
// the rules below read cleanly — and so a consumer that `using namespace`s this analysis
// namespace sees the contract types it must build the FunctionSlice from.
using chordslice::AmbiguityKind;
using chordslice::ChordSliceCandidate;
using chordslice::OpenQuestion;
using chordslice::OpenQuestionLabel;
using chordslice::SliceConfidence;
using chordslice::SliceDecision;

// ── The prevailing key of the region (§5.1 / §5.7) ────────────────────────────
//
// Maps directly from the Layer-3 region key (HarmonicRegion::keyModeResult):
//   keyFifths = keySignatureFifths, keyMode = mode, tonicPc = tonicPc.
struct ResolverKey {
    int keyFifths = 0;
    KeySigMode keyMode = KeySigMode::Ionian;
    int tonicPc = 0;
};

// ── One slice of the region the resolver iterates (the §5.0 progression view
//    UNIONED with the L4→L5 carried-reading contract) ──────────────────────────
//
// The progression fields (chord/committed/metricWeight/ticks) are the §5.0 view the
// functionprogression queries read; the contract fields (decision/openQuestion/
// alternatives/confidence) are the L4 forward-carry the selection reads. One vector
// per region, in slice order. At engage each entry is mapped from a SliceChord +
// its metric weight; injected by hand in the tests.
struct FunctionSlice {
    // — §5.0 progression view (→ ProgressionSlice) —
    ProgressionChord chord;        ///< the committed chord (valid when committed == true)
    bool committed = false;        ///< an L4 Commit/Inherit (non-abstained) chord
    double metricWeight = 1.0;     ///< slice metric weight (§3); higher == metrically stronger
    int startTick = 0;
    int endTick = 0;

    // — the L4→L5 carried-reading contract (chord/chordslicedecoder.h) —
    SliceDecision decision = SliceDecision::Commit;  ///< G1 Commit / Inherit / Abstain
    OpenQuestionLabel openQuestion;                  ///< named question + readingA / readingB (on abstain)
    std::vector<ChordSliceCandidate> alternatives;   ///< the ranked carried alternatives
    SliceConfidence confidence;                      ///< composite confidence (the §8 earlier-layer confidence)

    // — the committed chord's FULL identity (the §5.5/§7 verbatim-carry source) —
    //
    // The L4-decoded `SliceChord.chosen` for this slice: root + quality + committed
    // bass/inversion + the L4→L5 carried extension identity (extensions/naturalFifthPresent/
    // extensionsKnown). `chord` above is its §5.0 progression PROJECTION (root+quality only)
    // — the licensing queries read that; the resolver EMITS `chosen` VERBATIM on the
    // pass-through path (§7 "does not replace the chord identity Layer 4 committed") so the
    // committed bass and seventh survive to the formatter, never a re-derived bare reading.
    // For an Inherit slice this is L4's inherited (prevailing) identity; for an Abstain slice
    // it is not read (the abstain path selects among openQuestion/alternatives instead).
    // Valid ⇔ committed; `toPC(chosen)` equals `chord`. Populated at engage from the decoder;
    // injected by hand in the tests.
    ChordSliceCandidate chosen;
};

// ── Why a slice resolved the way it did (transparency; oracle-tested) ──────────
enum class ResolutionBasis {
    None,              ///< not resolved — the honest open mark (§7), or an unchanged commit
    Progression,       ///< a licensed-progression fit (§5.0) decided it
    CadenceVote,       ///< the cadence tonic-vote (§5.2) decided it
    NeighbourHarmony,  ///< the prevailing / neighbouring committed harmony decided it
    BassDegreePrior,   ///< the §5.7 soft bass-scale-degree prior broke the tie
    FineGrainOverride  ///< the §8 case-4 fine-grain override corrected a confident commit
};

// ── The resolver's per-slice output (additive over the Layer-4 result, §7) ─────
//
// For an ABSTAIN: resolved == true with a selected `reading`, OR openMark == true
// (genuinely undecidable). For a COMMIT: overrodeCommit == true with a corrected
// `reading`, OR all flags false and `reading` == the committed chord (L4's commit
// stands, L5 made no change). It annotates; it does not replace the chord identity.
struct ResolvedReading {
    int sliceIndex = -1;
    bool wasAbstain = false;       ///< the slice was an L4 abstain (case 2) vs a commit (case 4)
    bool resolved = false;         ///< an abstain was resolved (a reading selected)
    bool openMark = false;         ///< the honest open mark — genuinely undecidable (§7)
    bool overrodeCommit = false;   ///< the §8 case-4 fine-grain override fired on a commit

    ChordSliceCandidate reading;   ///< the selected/corrected reading (else the committed chord)
    AmbiguityKind kind = AmbiguityKind::None;    ///< the L4 kind, echoed for transparency
    ResolutionBasis basis = ResolutionBasis::None;
    double functionConfidence = 0.0;             ///< §7 confidence from the deciding evidence (seed; firewall)

    // ── Bounded-context denial/truncation provenance (design §3 item 10 / §5) ─────
    // Set only by resolveCarriedReadingsExtending() on the selection slices whose
    // decision-context span was cut by the selection edge; resolveCarriedReadings()
    // never touches them (they stay false — the base resolver is byte-identical).
    bool clippedBySelectionEdge = false;   ///< the decision-context span was cut by the selection edge
    bool cueDenied = false;                ///< a forward-extension request was REFUSED (proceeds on truncated evidence)
};

// ── The resolver result (the readings + the §8 closure, for transparency/tests) ─
struct ResolverResult {
    std::vector<ResolvedReading> readings;   ///< one per region slice, in order
    OnePassClosure closure;                  ///< the one-pass closure ledger after the pass (§8)
};

// ── Precision-phase constants (the firewall, build §4) — provisional seeds ─────
//
// The functional-plausibility feature weights + the deciding margin (§5.5 close), and
// the §8 override threshold. NOT tuned for accuracy; only the directions are fixed.
struct FunctionResolverParams {
    double wLicensedOut   = 1.0;   ///< §5.5: a licensed progression OUT of the prevailing harmony
    double wLicensedIn    = 1.0;   ///< §5.5: a licensed progression INTO the established next function
    double wCadentialFit  = 1.0;   ///< §5.5: the reading's root receives a cadence tonic-vote
    double decidingMargin = 0.5;   ///< §5.5: min plausibility margin to decide (below ⇒ tie ⇒ prior/open)
    ForwardOverrideParams override;///< §8: the fine-grain override threshold (firewall seeds)
};

/// Global default resolver parameters.
inline constexpr FunctionResolverParams kDefaultFunctionResolverParams{};

// ── §5.7 the soft bass-/root-scale-degree functional bias ─────────────────────
enum class FunctionalBias {
    None,        ///< the submediant (6̂) or a chromatic degree — no lean (a soft prior, never a gate)
    Tonic,       ///< degrees 1̂, 3̂
    Predominant, ///< degrees 2̂, 4̂
    Dominant     ///< degrees 5̂, 7̂
};

/// §5.7: the weak functional bias a scale-DEGREE (0..6, as from diatonicDegreeForRootPc)
/// carries — 1̂/3̂ lean tonic, 2̂/4̂ lean pre-dominant, 5̂/7̂ lean dominant, 6̂ none. Used
/// ONLY as a soft prior / tie-breaker (§5.2, §5.5), never as a gate. Chromatic (-1) ⇒ None.
FunctionalBias degreeFunctionalBias(int degree) noexcept;

/// §5.7: the bias of a pitch class read as a bass scale-degree in @p key (wraps
/// degreeFunctionalBias ∘ diatonicDegreeForRootPc). The soft prior of §5.5's tie-break.
FunctionalBias bassScaleDegreeBias(int bassPc, const ResolverKey& key);

// ── The resolver (§5.5) + the fine-grain override (§5.5 case-4 / §8) ───────────

/// Resolve a region's carried uncertain readings AND override its contradicted
/// confident commits, in ONE forward pass (§5.5 + §8). For every L4-abstained slice it
/// selects among the carried readings by the named ambiguity kind (or carries the open
/// mark); for every confident commit the established function/cadence contradicts it
/// fires the §8 fine-grain override (selecting the corrected carried/neighbour reading)
/// and a localized forward recompute of the region's downstream readings. Never
/// re-derives a chord from notes. Returns the per-slice readings + the one-pass closure.
ResolverResult
resolveCarriedReadings(const std::vector<FunctionSlice>& region,
                       const std::vector<FunctionalCadence>& cadences,
                       const ResolverKey& key,
                       const FunctionResolverParams& params = kDefaultFunctionResolverParams);

// ── Bounded context: the pinned decision-context extent + the forward requester loop
//    (design §5 / L5 §5.0; cowork_bounded_context_design.md §3/§4/§5). DORMANT ────────
//
// A slice's DECISION-CONTEXT SPAN extends forward until the FIRST of: (i) a cadence-anchored
// function, (ii) a punctuation boundary, (iii) a hard bound of K slices / B beats (the §3.7
// safety cap). A §5.5 resolution whose span is CUT by the selection edge before any of (i)–(iii)
// holds REQUESTS a forward extension (the L1 extend → L2 re-slice → L3/L4 re-decode forward
// re-run — abstracted here as a supplier so the dormant resolver stays hand-injectable). The
// extension re-runs obey the §8 one-pass closure: appending forward slices may FINALIZE an open
// (edge-cut) decision, but never re-opens a decision the base pass already closed — forward data
// supply, not a back-edge. Denied (score boundary / driver refusal) ⇒ the decision resolves on
// what it saw (its honest open mark) + the item-10 provenance. DORMANT: default OFF ⇒
// resolveCarriedReadingsExtending == resolveCarriedReadings (no request, no provenance); no
// production consumer.

/// The forward-extension bound (§5 (iii)) + the dormant master switch (firewall — the exact K/B
/// are precision-phase settings, only the existence of a cap is fixed).
struct L5ForwardExtensionParams {
    bool enableForwardExtension = false;   ///< OFF ⇒ no request, byte-identical to resolveCarriedReadings
    int  maxForwardExtendSlices = 8;       ///< K — the decision-context span's hard bound in slices
    int  maxForwardExtendBeats  = 0;       ///< B — the bound in beats (0 ⇒ slice bound only)
};

/// The outcome of one forward-extension request to the supplier.
enum class ForwardSupply {
    Supplied,       ///< more forward slices (+ cadences) were appended — re-run forward
    ScoreBoundary,  ///< the score end was reached — nothing more exists (proceed truncated, NOT a denial)
    Refused         ///< a driver-level safety cap refused the request (proceed truncated, a DENIAL)
};

/// The forward supplier (the L1-extend → L2 → L3/L4 forward re-run, abstracted). At engage this
/// is wired to actually extend Layer 1 and re-decode; in tests it is injected by hand. Given the
/// current forward edge tick, it appends the next batch of FunctionSlices (+ their cadences) and
/// returns Supplied, or reports the score boundary / a refusal.
struct ForwardExtensionProvider {
    std::function<ForwardSupply(int fromTick,
                                std::vector<FunctionSlice>& moreSlices,
                                std::vector<FunctionalCadence>& moreCadences)> supply;
};

/// Resolve a SELECTION region's carried readings WITH the forward requester loop (§5). Identical
/// to resolveCarriedReadings when @p ext.enableForwardExtension is OFF (or no supplier) — same
/// readings, no provenance. When ON, a selection slice whose decision-context span is cut by the
/// selection edge before (i)–(iii) drives a forward extension via @p provider; the region grows
/// (append-only) and the resolution re-runs forward until a stop condition holds, the K/B bound is
/// reached, or the supplier reports the score boundary / refuses. Output covers the ORIGINAL
/// selection slices only (the extended context is evidence, never emitted); the edge-cut slices
/// carry the item-10 provenance (clippedBySelectionEdge / cueDenied). @p region and @p cadences
/// are taken BY VALUE so the loop appends to private copies.
ResolverResult
resolveCarriedReadingsExtending(std::vector<FunctionSlice> region,
                                std::vector<FunctionalCadence> cadences,
                                const ResolverKey& key,
                                const ForwardExtensionProvider& provider,
                                const FunctionResolverParams& params = kDefaultFunctionResolverParams,
                                const L5ForwardExtensionParams& ext = {});

} // namespace mu::composing::analysis
