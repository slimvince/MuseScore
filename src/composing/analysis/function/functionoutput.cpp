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

#include "composing/analysis/function/functionoutput.h"

namespace mu::composing::analysis {

namespace output_detail {

/// §5.2 cadence-vote attribution: the tonic-vote of the cadence ANCHORING this unit —
/// the cadence whose tonic ARRIVAL falls within the unit's span [startTick, endTick).
/// When several arrive in the span the strongest (max vote) anchors it; none ⇒ 0.0.
/// A deterministic spatial attribution (declared build-detail decision) — no judgment.
inline double cadenceVoteForUnit(const FunctionUnitAssembly& unit,
                                 const std::vector<FunctionalCadence>& cadences) noexcept
{
    double best = 0.0;
    for (const FunctionalCadence& c : cadences) {
        if (c.arrivalTick >= unit.startTick && c.arrivalTick < unit.endTick) {
            if (c.tonicVote > best) {
                best = c.tonicVote;
            }
        }
    }
    return best;
}

/// §5.0 licensed-progression fit of the motion INTO unit @p i: 1.0 when the root motion
/// from the nearest preceding COMMITTED unit's chord to this unit's chord is a licensed
/// progression (Step-1 isLicensedProgression — a boolean fit, NOT a new score), else 0.0.
/// No preceding committed chord (the region's first committed unit) ⇒ 0.0.
inline double licensedFitForUnit(const std::vector<FunctionUnitAssembly>& units, size_t i) noexcept
{
    if (units[i].chord.rootPc < 0) {
        return 0.0;
    }
    for (size_t j = i; j-- > 0;) {
        if (units[j].committed && units[j].chord.rootPc >= 0) {
            return isLicensedProgression(units[j].chord, units[i].chord) ? 1.0 : 0.0;
        }
    }
    return 0.0;  // no preceding committed harmony — the motion into the first unit is unscored
}

} // namespace output_detail

FunctionLayerOutput
assembleFunctionOutput(const std::vector<FunctionUnitAssembly>& units,
                       const std::vector<FunctionalCadence>& cadences,
                       const std::vector<ModulationDecision>& modulations,
                       int homeTonicPc, bool homeMinorMode,
                       const FunctionOutputParams& params)
{
    using namespace output_detail;

    FunctionLayerOutput out;

    // ── Per-region markers (§7): the cadence stream + the local key ──────────────
    out.region.cadences = cadences;
    if (!units.empty()) {
        out.region.startTick = units.front().startTick;
        out.region.endTick = units.back().endTick;
    }

    // The local key is the FIRST confirmed §5.4 modulation's key (a region carries one
    // local key — the unit between modulations); absent any confirmed modulation it is
    // the home key (declared build-detail decision). §5.3's break-even defaults to
    // tonicization, so a non-modulation decision never changes the key here.
    out.region.localTonicPc = homeTonicPc;
    out.region.localMinorMode = homeMinorMode;
    out.region.modulated = false;
    for (const ModulationDecision& m : modulations) {
        if (m.isModulation) {
            out.region.localTonicPc = m.tonicPc;
            out.region.localMinorMode = m.minorMode;
            out.region.modulated = true;
            break;
        }
    }

    // ── Per analysis unit (§7): the Roman numeral + confidence + open mark ────────
    out.units.reserve(units.size());
    for (size_t i = 0; i < units.size(); ++i) {
        const FunctionUnitAssembly& in = units[i];

        FunctionAnalysisUnit u;
        u.sliceIndex = static_cast<int>(i);
        u.startTick = in.startTick;
        u.endTick = in.endTick;

        // The full DCML numeral (base RN + relational label already combined upstream by
        // classifyRelationalLabel) — no simplification (§3 Produces).
        u.romanNumeral = in.relational.label;
        u.relationalRole = in.relational.role;

        u.openMark = in.openMark;

        // ADDITIVE over Layer 4: carry the committed identity verbatim — NOT replaced.
        u.committedIdentity = in.committedIdentity;

        // §7 function confidence — the three FIXED components, combined at default weights.
        u.confidence.cadenceVoteWeight = cadenceVoteForUnit(in, cadences);
        u.confidence.licensedProgressionFit = licensedFitForUnit(units, i);
        u.confidence.nextBestMargin = in.resolverConfidence;
        u.confidence.combined =
            params.wCadenceVote * u.confidence.cadenceVoteWeight
            + params.wLicensedFit * u.confidence.licensedProgressionFit
            + params.wNextBestMargin * u.confidence.nextBestMargin;
        // D-L5a: publish the boundary (squashed) form of `combined` — the confidence
        // contract's U2 layer-boundary requirement. combined >= 0 (all components
        // non-negative), so combined/(combined + k) ∈ [0,1) and is monotone in combined.
        u.confidence.combinedBoundary =
            u.confidence.combined / (u.confidence.combined + params.kBoundary);

        out.units.push_back(std::move(u));
    }

    return out;
}

} // namespace mu::composing::analysis
