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
#include "functionmodulation.h"

namespace mu::composing::analysis {

std::vector<ModulationDecision>
decideTonicizationVsModulation(const ModulationDetectionResult& detected,
                               const std::vector<FunctionalCadence>& cadences,
                               const std::vector<bool>& spellingSupport,
                               const ModulationParams& params)
{
    std::vector<ModulationDecision> out;
    out.reserve(detected.spans.size());

    for (size_t s = 0; s < detected.spans.size(); ++s) {
        const LocalKeySpan& span = detected.spans[s];

        ModulationDecision d;
        d.startTick  = span.startTick;
        d.endTick    = span.endTick;
        d.tonicPc    = span.tonicPc;
        d.minorMode  = span.minorMode;
        d.isHomeKey  = span.agreesWithAnchor;

        // §5.3 (a) — the CADENCE-CONFIRMATION gate, from the §5.2 FunctionalCadence
        // stream (the authoritative cadence + its weighted tonic-vote). A cadence
        // confirms this span iff it votes for the span's (tonic, mode) and its arrival
        // falls inside the span. (b) — the accumulated cadential weight is the summed
        // tonic-votes of those confirming cadences.
        int confirming = 0;
        double cadentialWeight = 0.0;
        for (const FunctionalCadence& c : cadences) {
            if (c.tonicPc == span.tonicPc && c.minorMode == span.minorMode
                && c.arrivalTick >= span.startTick && c.arrivalTick < span.endTick) {
                ++confirming;
                cadentialWeight += c.tonicVote;
            }
        }
        d.confirmingCadenceCount = confirming;
        d.cadenceConfirmed       = confirming >= 1;
        d.cadentialWeight        = cadentialWeight;

        // §5.3 (b) — the candidate area's DURATION (the spec's persistence quantity),
        // in the fixed whole-note time unit. Duration TRADES OFF against cadential
        // weight against the single change-cost (no standalone duration gate).
        const int durTicks = (span.endTick > span.startTick) ? (span.endTick - span.startTick) : 0;
        d.durationWholeNotes = static_cast<double>(durTicks) / kTicksPerWholeNote;

        // §5.3 — the function-gated notated-spelling key signal (soft; one input to b).
        d.spellingSupport = (s < spellingSupport.size()) ? spellingSupport[s] : false;

        // §5.3 (b) — the persistence evidence vs the change-cost (the hysteresis). The
        // direction is fixed: every term is non-negative (more never lowers the
        // evidence); the magnitudes are firewall seeds.
        d.persistenceEvidence = params.wDuration * d.durationWholeNotes
                                + params.wCadentialWeight * d.cadentialWeight
                                + params.wSpelling * (d.spellingSupport ? 1.0 : 0.0);
        d.changeCost = params.baseChangeCost;

        // The §5.3 verdict: a MODULATION iff it is NOT the home key, a cadence confirms
        // it (the necessary gate a), AND the persistence evidence STRICTLY EXCEEDS the
        // change-cost (b) — so at the exact break-even the home key holds (tonicization,
        // the default; the strict inequality fixes the tie-direction).
        d.isModulation = !d.isHomeKey
                         && d.cadenceConfirmed
                         && d.persistenceEvidence > d.changeCost;

        out.push_back(d);
    }

    return out;
}

std::vector<ModulationDecision>
detectAndDecideModulations(const std::vector<CadenceRegionInput>& regions,
                           const std::vector<FunctionalCadence>& cadences,
                           int keySignatureFifths,
                           const std::vector<bool>& spellingSupport,
                           const ModulationParams& params)
{
    // The concrete REUSE path: the established + cadence-confirmed substrate is the
    // detector's committed spans (NOT re-implemented here).
    const ModulationDetectionResult detected = detectLocalModulations(regions, keySignatureFifths);
    return decideTonicizationVsModulation(detected, cadences, spellingSupport, params);
}

ModulationRecomputeResult
modulationRecompute(const ModulationDecision& modulation,
                    double homeKeyConfidence,
                    int firstSlice, int lastSlice,
                    const std::function<void(int, int, bool)>& reread,
                    OnePassClosure& closure,
                    int keyDecisionId,
                    const ModulationParams& params)
{
    ModulationRecomputeResult result;

    // No modulation ⇒ no override fires (the home key holds — §5.3 default).
    if (!modulation.isModulation) {
        return result;
    }

    // §5.4 / §8 case 4 — the cadence is the DECISIVE later evidence: its strength (the
    // accumulated §5.2 cadential weight) must CROSS the §8 bar SCALED to the home key's
    // confidence (a well-founded confident home key demands decisively stronger
    // contradiction). tryOverride couples the threshold to the one-pass closure, so the
    // key decision is overturned AT MOST ONCE and is then CLOSED for the pass.
    //
    // ── Confidence-contract FRAME F-A (cadence-confirmed modulation recompute) ───
    // Incumbent (earlierConfidence): the L3 key-of-span confidence — `homeKeyConfidence`, a
    // Class-M value (the squashed sequence margin). Contradiction (contradictionStrength): the
    // accumulated cadential VOTE weight in the candidate key — `modulation.cadentialWeight`, a
    // Class-M evidence weight. Both are L3/L5 cadence quantities; `FunctionConfidence.combined`
    // (the L5 OUTPUT confidence, D-L5a) is NOT read here. Their common-scale conversion and the θ
    // (baseBar/confidenceScale) are Stage-5 CALIBRATION items (contract §6 C1/C2), not set here.
    const bool fired = closure.tryOverride(keyDecisionId, homeKeyConfidence,
                                           modulation.cadentialWeight, params.override);
    if (!fired) {
        return result;   // the contradiction is not decisive — the confident home key holds
    }

    result.fired        = true;
    result.newTonicPc   = modulation.tonicPc;
    result.newMinorMode = modulation.minorMode;

    // The LOCALIZED, FORWARD, convergence-bounded re-read: a SINGLE forward sweep over
    // the region's slice range, re-reading each slice in the new key. The key decision
    // is already CLOSED (tryOverride), so the recompute cannot re-open it; the sweep is
    // re-entrancy-guarded (no recursion) and sends nothing upstream (no back-edge).
    result.slicesReread = closure.forwardRecompute(
        firstSlice, lastSlice,
        [&](int sliceId) {
            if (reread) {
                reread(sliceId, modulation.tonicPc, modulation.minorMode);
            }
        });

    return result;
}

} // namespace mu::composing::analysis
