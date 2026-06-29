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

// ── composing/analysis/function/functionmodulation ───────────────────────────
//
// Architectural Layer 5 (FUNCTION) — TONICIZATION vs MODULATION (§5.3) + the
// CADENCE-CONFIRMED MODULATION RECOMPUTE (§5.4, the §8 case-4 channel #1). Spec:
// cowork_layer5_function_design.md (SIGNED) §5.3 + §5.4 + §8 + the §5.0 shared
// defs. Build plan: cowork_phase5c_l5_build_plan.md Step 4.
//
// §5.3 — THE DEFAULT IS TONICIZATION. The home key holds and a chord leaning toward
// a non-tonic degree is written as an APPLIED chord of that degree. The home key is
// changed to a MODULATION only when BOTH hold:
//   (a) a CADENCE in the candidate key CONFIRMS it (an authentic or half cadence
//       whose tonic is the candidate degree) — a NECESSARY GATE (no cadence ⇒ the
//       lean stays a tonicization no matter how long it lasts), and
//   (b) the music PERSISTS in the candidate key — expressed as a CHANGE-COST
//       (HYSTERESIS): the cost of committing the key change FALLS as the
//       cadence-confirmed candidate area grows in DURATION and in ACCUMULATED
//       CADENTIAL WEIGHT (the §5.2 votes inside it). At the exact BREAK-EVEN the
//       rule DEFAULTS TO TONICIZATION (the home key holds).
// The §5.3 "notated-spelling key signal" is consumed HERE, FUNCTION-GATED: a span
// whose accidentals are sustained-consistent with the candidate key's diatonic set
// adds soft support to (b); it is one input to (a)/(b), never a standalone gate.
//
// §5.4 — THE RECOMPUTE is the first concrete instance of the §8 confidence-weighted
// forward override (case 4): a cadence is LATER evidence that contradicts a
// *confident* earlier KEY inference (the key layer chose its key before any cadence
// was known). When §5.3 confirms a modulation and the cadence evidence is DECISIVE
// (its strength crosses the §8 bar SCALED to the home key's confidence), the layer
// commits the new local key and triggers a LOCALIZED, FORWARD, convergence-bounded
// re-read of the region (the chords' degrees change in the new key; uncertain slices
// re-resolve against it). REUSES forwardoverride's OnePassClosure — Step-3's
// mechanism, this is its second instance — so the key decision is CLOSED for the pass
// (no re-open, no recursion) and the recompute is a single forward sweep, NO back-edge.
//
// REUSE, NOT RE-IMPLEMENT (build §1, the heart of this step):
//   • localmodulationdetector (detectLocalModulations) — the KEY-AGNOSTIC, ESTABLISHED
//     + CADENCE-CONFIRMED local-key-span substrate (a span is committed only on a
//     sustained collection-consistent run WITH a confirming cadence). This unit reads
//     its committed candidate spans (LocalKeySpan, agreesWithAnchor tagging the home
//     key) and layers the §5.3 hysteresis on top: the detector's internal fixed
//     sustained-run gate (kEstablishmentMinChords) is the CANDIDATE floor (untouched,
//     not re-tuned); the §5.3 PERSISTENCE is the arbiter's duration+cadential-weight
//     CHANGE-COST — adapting the existing cadence-confirmed substrate to the spec's
//     hysteresis FORM (build-detail decision, declared in the Step-4 report).
//   • functioncadence (FunctionalCadence) — the §5.2 cadence stream + its weighted
//     tonic-votes supply BOTH the §5.3 cadence-confirmation gate (cond a) and the
//     accumulated cadential weight (cond b). The relative-pair centre is decided by
//     the same tonic-vote.
//   • forwardoverride (OnePassClosure / ForwardOverrideParams) — the §8 threshold +
//     one-pass closure + localized forward recompute, REUSED for §5.4 (its second
//     channel). No new mechanism is built here.
//   • At ENGAGE the recompute's re-read binds to the J-key-iii re-key path
//     (regionanalyzer applyJointKeyWiring) + jointkeydecision; dormant, the re-read is
//     an injected callback over an abstract slice range (hand-injectable in tests).
//
// PRODUCER-AGNOSTIC / HAND-INJECTABLE (the resolver precedent): this unit reads only
// the already-built producer-agnostic value types (LocalKeySpan, FunctionalCadence,
// OnePassClosure) — never a score / region / decoder engine type — so it compiles
// free of those headers and is exercised by hand-built inputs in its unit tests.
//
// CONSTANTS ARE PRECISION-PHASE (the firewall, build §4). The change-cost magnitude,
// the §5.2-weight and spelling weights, and the §8 override bar are DEFAULT seeds and
// are NOT tuned for accuracy — that is Phase B. Only the DIRECTION is fixed: more
// duration / more cadential weight / spelling support ⇒ more evidence ⇒ likelier to
// overcome the change-cost; the break-even tie-direction is fixed (at the exact bar
// the HOME key holds — tonicization is the default).
//
// DORMANT (build §6): NO production consumer — nothing in src/ calls it; exercised
// only by its unit tests. Byte-identical on production by construction; load-bearing
// when the function layer engages (Phase 5d).

#include <functional>
#include <vector>

#include "composing/analysis/section/localmodulationdetector.h"  // LocalKeySpan, ModulationDetectionResult, CadenceKeyAnchor
#include "functioncadence.h"                                      // FunctionalCadence (the §5.2 tonic votes)
#include "forwardoverride.h"                                      // the §8 mechanism (OnePassClosure)

namespace mu::composing::analysis {

// ── Precision-phase constants (the firewall, build §4) — provisional seeds ─────
//
// The §5.3 change-cost + its evidence weights, the §5.3 notated-spelling support
// weight, and the §5.4 §8 override bar. NONE tuned for accuracy. Only the DIRECTION
// is fixed (every evidence term is non-negative — more never lowers the evidence;
// the break-even defaults to tonicization via a STRICT inequality).
struct ModulationParams {
    // §5.3 condition (b) — the persistence change-cost (hysteresis).
    double baseChangeCost   = 1.0;  ///< the cost to commit a key change at zero persistence evidence
    double wDuration        = 1.0;  ///< evidence per whole-note of cadence-confirmed candidate-area duration
    double wCadentialWeight = 1.0;  ///< evidence per unit of accumulated §5.2 cadential vote inside the area
    double wSpelling        = 0.5;  ///< §5.3 notated-spelling support (function-gated), SOFT — one input to (b)

    // §5.4 — the §8 confidence-weighted override bar (REUSED from forwardoverride).
    ForwardOverrideParams override; ///< the cadence-strength-vs-key-confidence bar (firewall seeds)
};

/// Global default modulation-arbiter parameters.
inline constexpr ModulationParams kDefaultModulationParams{};

/// The fixed score-time UNIT for the §5.3 duration term: one whole note = 1920 ticks
/// (MuseScore's 480 ticks/quarter division). This is a stable time UNIT, NOT a
/// persistence threshold — duration TRADES OFF against cadential weight against the
/// single change-cost (so §5.3's "never a fixed beat count" is honoured: no standalone
/// duration gate exists). Kept local so this unit needs no engraving dependency.
inline constexpr double kTicksPerWholeNote = 1920.0;

// ── §5.3 — one candidate area's tonicization-vs-modulation decision ───────────
//
// One committed candidate local-key span (from detectLocalModulations) carried
// through the §5.3 decision. A span that AGREES with the home anchor is never a
// modulation candidate (it IS the home key); a span with no §5.2 cadence in its key
// fails the necessary gate (a) and stays a tonicization regardless of length.
struct ModulationDecision {
    int startTick = 0;
    int endTick = 0;
    int tonicPc = -1;
    bool minorMode = false;

    bool isHomeKey = false;            ///< the span agrees with the key-agnostic home anchor (never a modulation)
    bool cadenceConfirmed = false;     ///< §5.3 (a): a §5.2 cadence in the candidate key confirms it (necessary)
    int  confirmingCadenceCount = 0;   ///< §5.2 cadences (any authentic/half) to this tonic inside the span
    double cadentialWeight = 0.0;      ///< §5.3 (b): the summed §5.2 tonic-votes of those cadences
    double durationWholeNotes = 0.0;   ///< §5.3 (b): the candidate area's duration in whole notes
    bool spellingSupport = false;      ///< §5.3: the function-gated notated-spelling key signal (soft input to b)

    double persistenceEvidence = 0.0;  ///< §5.3 (b): wDuration·dur + wCadentialWeight·weight + wSpelling·spelling
    double changeCost = 0.0;           ///< §5.3 (b): the change-cost the evidence is tested against (baseChangeCost)

    bool isModulation = false;         ///< the §5.3 verdict — false ⇒ TONICIZATION (the default; break-even tonicizes)
};

/// §5.3 — decide tonicization vs modulation for every committed candidate span.
///
/// REUSE: @p detected is detectLocalModulations()'s output (the established +
/// cadence-confirmed substrate, key-agnostic); @p cadences is the §5.2
/// FunctionalCadence stream (the authoritative cadence-confirmation + vote weights).
/// A span is a MODULATION iff it is NOT the home key, has ≥1 §5.2 cadence in its key
/// (the necessary gate a), AND its persistence evidence (duration + cadential weight
/// + the optional spelling support) STRICTLY EXCEEDS the change-cost (the hysteresis
/// b) — so at break-even the home key holds (tonicization, the default).
///
/// @p spellingSupport, when non-empty, is parallel to @p detected.spans and supplies
/// the per-span function-gated notated-spelling signal (§5.3); empty ⇒ all false
/// (the neutral dormant default; wired at engage from each area's accidental/
/// signature consistency). Returns one decision per span, in span order.
std::vector<ModulationDecision>
decideTonicizationVsModulation(const ModulationDetectionResult& detected,
                               const std::vector<FunctionalCadence>& cadences,
                               const std::vector<bool>& spellingSupport = {},
                               const ModulationParams& params = kDefaultModulationParams);

/// §5.3 convenience (the concrete reuse path): run detectLocalModulations() over a
/// key-agnostic region stream, then decideTonicizationVsModulation() over its spans.
/// This is the integration entry the engage step binds; the test exercises it to
/// prove the detector substrate is actually invoked (not re-implemented).
std::vector<ModulationDecision>
detectAndDecideModulations(const std::vector<CadenceRegionInput>& regions,
                           const std::vector<FunctionalCadence>& cadences,
                           int keySignatureFifths = 0,
                           const std::vector<bool>& spellingSupport = {},
                           const ModulationParams& params = kDefaultModulationParams);

// ── §5.4 — the cadence-confirmed modulation recompute (the §8 case-4 channel #1) ─
//
// The result of firing the §8 forward override on a confirmed modulation.
struct ModulationRecomputeResult {
    bool fired = false;        ///< the §8 override fired (the modulation overturned the *confident* home key)
    int slicesReread = 0;      ///< forwardRecompute's count (0 if not fired; -1 if the sweep was refused)
    int newTonicPc = -1;       ///< the committed new local tonic (when fired)
    bool newMinorMode = false; ///< the committed new local mode (when fired)
};

/// §5.4 — on a confirmed §5.3 modulation, fire the LOCALIZED, FORWARD, convergence-
/// bounded recompute THROUGH the §8 mechanism (forwardoverride). REUSES the OnePassClosure:
///   • the override fires iff @p modulation.isModulation AND the cadence is DECISIVE —
///     its strength (the accumulated §5.2 CADENTIAL WEIGHT, the cadence-strength term of
///     §5.4) CROSSES the §8 bar SCALED to @p homeKeyConfidence (a well-founded confident
///     home key demands decisively stronger contradiction) — via
///     closure.tryOverride(@p keyDecisionId, …). §5.3 owns the persistence (duration)
///     call; §5.4's §8 bar is cadence-strength vs key-confidence;
///   • on fire, the key decision is CLOSED for the pass (no re-open), and a SINGLE
///     forward sweep over slice ids [@p firstSlice, @p lastSlice] re-reads each slice in
///     the new key via @p reread(sliceId, newTonicPc, newMinorMode). The sweep is
///     re-entrancy-guarded (no recursion); it sends NO request upstream (no back-edge).
/// @p keyDecisionId is the opaque closure id for THIS region's key decision (distinct
/// per region). Returns whether it fired + the sweep count.
ModulationRecomputeResult
modulationRecompute(const ModulationDecision& modulation,
                    double homeKeyConfidence,
                    int firstSlice, int lastSlice,
                    const std::function<void(int /*sliceId*/, int /*newTonicPc*/, bool /*newMinor*/)>& reread,
                    OnePassClosure& closure,
                    int keyDecisionId,
                    const ModulationParams& params = kDefaultModulationParams);

} // namespace mu::composing::analysis
