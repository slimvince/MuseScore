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

// ── composing/analysis/function/functionoutput ───────────────────────────────
//
// Architectural Layer 5 (FUNCTION) — THE OUTPUT ASSEMBLY (§7). Spec:
// cowork_layer5_function_design.md (SIGNED) §7 + §3 ("Produces") + §9-D1. Build plan:
// cowork_phase5c_l5_build_plan.md Step 6.
//
// §7 assembles the per-unit and per-region products of Steps 1–5 into the L5→L6
// (grouping/display) CONTRACT. Per analysis unit it carries:
//   • the ROMAN NUMERAL at full DCML/RomanText completeness, NO simplification (§3
//     Produces) — the base numeral (Step 1) with its relational label (Step 5)
//     already combined upstream (classifyRelationalLabel's `.label` IS that numeral:
//     the base numeral when no relational role fires, the relational label otherwise);
//   • a FUNCTION CONFIDENCE — its three FIXED components (the §5.2 cadence-vote weight
//     where a cadence anchored it, the §5.0 licensed-progression fit where the
//     progression decided it, and the margin to the next-best reading), combined at
//     DEFAULT weights (the combination weights are precision-phase — the firewall);
//   • an OPEN MARK where a slice stayed genuinely undecided (Step 3 resolver) — carried
//     to display, never a guess.
// Per region it carries the LOCAL KEY (possibly changed by a confirmed §5.4 modulation)
// and the CADENCE MARKERS (type, location, salience — Step 2).
//
// ADDITIVE OVER THE LAYER-4 RESULT (§7). It ANNOTATES and RESOLVES; it does NOT replace
// the chord identity Layer 4 committed — each unit carries that committed identity
// verbatim alongside the L5 numeral / confidence / open mark, so the contract to L6
// preserves L4's decision rather than overwriting it.
//
// THE T/S/D DERIVED READ-OUT IS NOT BUILT (§9-D1, deferred). The output is the Roman
// numeral; the three-role tonic/subdominant/dominant summary is a derived read-out only
// (deterministically derivable, lossy to store as a primary output) and is built — if at
// all — for an accessibility/teaching display at a later step, not here.
//
// PURE ASSEMBLY — NO RE-DERIVATION (§2 / §3). This unit shuffles the already-produced
// Step-1..5 outputs into the §7 contract and combines the confidence components at
// default weights. The ONE reuse it performs is the §5.0 licensed-progression FIT, read
// through the Step-1 predicate isLicensedProgression() over the committed-chord chain
// (a boolean fit, not a new score); it derives no chord, key, or cadence of its own.
//
// CONSTANTS ARE PRECISION-PHASE (the firewall, build §3). The confidence-COMBINATION
// weights are DEFAULT seeds and are NOT tuned for accuracy — that is Phase B. The
// confidence COMPONENTS are fixed by §7. Only the direction is fixed (each component is
// non-negative; more evidence never lowers the combined confidence).
//
// DORMANT (build §6): NO production consumer — nothing in src/ calls it; exercised only
// by its unit tests. Byte-identical on production by construction; load-bearing when the
// function layer engages (Phase 5d).

#include <string>
#include <vector>

#include "composing/analysis/chord/chordanalyzer.h"   // ChordIdentity
#include "functioncadence.h"                           // FunctionalCadence (the §5.2 markers)
#include "functionmodulation.h"                        // ModulationDecision (the §5.4 local key)
#include "functionprogression.h"                       // ProgressionChord / isLicensedProgression (§5.0 fit)
#include "functionrelationallabel.h"                   // RelationalLabel / RelationalRole (the full RN)

namespace mu::composing::analysis {

// ── §7 the function confidence: three FIXED components + the default combination ──
//
// The components are fixed by §7; the COMBINATION weights are precision-phase (the
// firewall). Each component is non-negative — more evidence never lowers `combined`.
struct FunctionConfidence {
    double cadenceVoteWeight = 0.0;       ///< §5.2: the tonic-vote of the cadence anchoring this unit (0 if none)
    double licensedProgressionFit = 0.0;  ///< §5.0: 1.0 when the motion INTO this unit is a licensed progression
    double nextBestMargin = 0.0;          ///< §5.5: the resolver's margin-to-next-best (its functionConfidence)
    double combined = 0.0;                ///< the default-weighted combination (firewall — weights precision-phase)
    // ── D-L5a: the boundary (published) form of `combined` (confidence contract §5 R5 / §7) ──
    // `combined` is an UNBOUNDED additive (contract §3 row L5; observed to ~25 on the E0 spine).
    // The confidence contract's U2 requires a layer-boundary confidence to be [0,1], class-declared.
    // combinedBoundary is that squash — a fixed MONOTONE rational map combined/(combined + k),
    // k a precision-phase constant (default 1.0, NOT tuned) — so a downstream consumer that reads
    // an L5 confidence as a *comparison input* reads a commensurable [0,1) quantity. `combined`
    // itself is kept UNCHANGED for internal use (the additive is the internal working value; only
    // the boundary form is squashed). This is representational: it changes NO decision.
    double combinedBoundary = 0.0;        ///< combined / (combined + kBoundary) ∈ [0,1) — the U2 boundary form
};

// ── §7 combination weights (the firewall — default seeds, NOT tuned) ──────────────
struct FunctionOutputParams {
    double wCadenceVote    = 1.0;   ///< weight of the §5.2 cadence-vote component
    double wLicensedFit    = 1.0;   ///< weight of the §5.0 licensed-progression-fit component
    double wNextBestMargin = 1.0;   ///< weight of the §5.5 margin component
    // D-L5a boundary-squash constant: combinedBoundary = combined / (combined + kBoundary). The
    // MAP is structural (contract §5 R5); k is a precision-phase seed — default 1.0, NOT tuned.
    double kBoundary       = 1.0;
};

/// Global default output-assembly parameters.
inline constexpr FunctionOutputParams kDefaultFunctionOutputParams{};

// ── §7 one assembled analysis unit (ADDITIVE over the Layer-4 committed chord) ────
struct FunctionAnalysisUnit {
    int sliceIndex = -1;
    int startTick = 0;
    int endTick = 0;

    std::string romanNumeral;             ///< the FULL DCML numeral (base RN + relational label), no simplification
    RelationalRole relationalRole = RelationalRole::None;

    FunctionConfidence confidence;        ///< §7 function confidence
    bool openMark = false;                ///< §7 honest open mark (genuinely undecided — carried, not a guess)

    ChordIdentity committedIdentity;      ///< the L4 committed chord — carried, NOT replaced (additive §7)
};

// ── §7 the per-region cadence + key markers ──────────────────────────────────────
struct FunctionRegionMarkers {
    int startTick = 0;
    int endTick = 0;

    int localTonicPc = -1;                ///< the region's local key tonic (possibly changed by a confirmed modulation)
    bool localMinorMode = false;
    bool modulated = false;               ///< §5.4: a confirmed modulation changed the key from the home key

    std::vector<FunctionalCadence> cadences;  ///< §5.2 cadence markers (type, location, salience)
};

// ── §7 the L5 output for ONE region — the L5→L6 (grouping/display) contract ───────
struct FunctionLayerOutput {
    std::vector<FunctionAnalysisUnit> units;   ///< the per-unit Roman numerals + confidence + open marks, in order
    FunctionRegionMarkers region;              ///< the region's local key + cadence markers
};

// ── The per-unit assembly input (§7) — the Step-1..5 products for one unit ────────
//
// The engage step maps each field from the unit's L4 committed chord + its Step-1 base
// RN / Step-5 relational label / Step-3 resolver verdict; the tests inject by hand.
// `relational.label` carries the full Roman numeral (base numeral when no relational role
// fires, the relational label otherwise — the base RN + relational label already combined
// by classifyRelationalLabel), so this unit does NOT re-format the numeral.
struct FunctionUnitAssembly {
    int startTick = 0;
    int endTick = 0;

    ChordIdentity committedIdentity;      ///< L4's committed chord (carried, NOT replaced — additive §7)
    ProgressionChord chord;               ///< root + quality, for the §5.0 licensed-fit query
    bool committed = true;                ///< an L4 commit/inherit (vs an abstain) — drives the licensed-fit chain

    RelationalLabel relational;           ///< Step-5 relational label (its `.label` IS the full RN; `.role` the role)

    // — the Step-3 resolver verdict for this unit (§5.5) —
    bool openMark = false;                ///< the honest open mark (§7)
    double resolverConfidence = 0.0;      ///< the resolver's functionConfidence (the §7 margin-to-next-best component)
};

// ── The §7 output assembly ────────────────────────────────────────────────────────

/// Assemble ONE region's L5 output (§7) from the per-unit Step-1..5 products + the
/// region's §5.2 cadences and §5.4 modulation decisions. Per unit: carries the full
/// Roman numeral (relational.label), the open mark, and the function confidence — its
/// three fixed components (the cadence-vote weight attributed to the unit whose span
/// contains a cadence ARRIVAL; the §5.0 licensed-progression fit of the motion INTO the
/// unit, via isLicensedProgression over the committed-chord chain; the resolver's
/// margin) combined at the default weights. Per region: the local key (the first
/// confirmed §5.4 modulation's key, else the home key) + the cadence markers. The output
/// is ADDITIVE over Layer 4 (each unit carries its L4 committed identity unchanged).
FunctionLayerOutput
assembleFunctionOutput(const std::vector<FunctionUnitAssembly>& units,
                       const std::vector<FunctionalCadence>& cadences,
                       const std::vector<ModulationDecision>& modulations,
                       int homeTonicPc, bool homeMinorMode,
                       const FunctionOutputParams& params = kDefaultFunctionOutputParams);

} // namespace mu::composing::analysis
