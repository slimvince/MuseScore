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

// functionoutput_tests.cpp — Architectural Layer 5 (FUNCTION), Phase 5c Step 6.
//
// Oracle-asserted against the §7 output contract: a resolved unit carries the full
// Roman numeral + a function confidence (its three fixed components combined at default
// weights); an undecided unit carries the honest open mark; a region carries its local
// key (possibly modulated) + the cadence markers; the output is ADDITIVE over the
// Layer-4 result (the committed identity is carried, not replaced). The T/S/D read-out
// is correctly ABSENT (§9-D1, deferred). Spec: cowork_layer5_function_design.md §7.

#include <gtest/gtest.h>

#include "composing/analysis/function/functionoutput.h"

using namespace mu::composing::analysis;

namespace {

using Q = ChordQuality;
using R = RelationalRole;

constexpr int C = 0, D = 2, G = 7;

// One committed analysis unit: an L4 committed chord + its Step-5 numeral + the Step-3
// resolver verdict (resolved, with a confidence).
FunctionUnitAssembly committedUnit(int startTick, int endTick, int rootPc, Q quality,
                                   const std::string& label, R role, double resolverConf)
{
    FunctionUnitAssembly u;
    u.startTick = startTick;
    u.endTick = endTick;
    u.committedIdentity.rootPc = rootPc;
    u.committedIdentity.quality = quality;
    u.chord.rootPc = rootPc;
    u.chord.quality = quality;
    u.committed = true;
    u.relational.role = role;
    u.relational.label = label;
    u.openMark = false;
    u.resolverConfidence = resolverConf;
    return u;
}

// A §5.2 cadence arriving at @p arrivalTick, voting @p tonicVote for @p tonicPc.
FunctionalCadence cadence(int approachTick, int arrivalTick, int tonicPc, double tonicVote,
                          FunctionalCadenceType type = FunctionalCadenceType::PerfectAuthentic)
{
    FunctionalCadence c;
    c.type = type;
    c.approachTick = approachTick;
    c.arrivalTick = arrivalTick;
    c.tonicPc = tonicPc;
    c.tonicVote = tonicVote;
    return c;
}

} // namespace

// ── §7: a resolved unit carries the full Roman numeral + a function confidence ─────

TEST(FunctionOutput, ResolvedUnitCarriesNumeralAndConfidence)
{
    // V→I in C major: unit0 = V (G major), unit1 = I (C major). The motion G→C is a
    // descending fifth → a LICENSED progression, so unit1's licensed-fit is 1.0. A PAC
    // arrives at unit1 (tonic vote 3.0). unit1 is resolved with confidence 1.0.
    std::vector<FunctionUnitAssembly> units = {
        committedUnit(0, 960, G, Q::Major, "V", R::None, 0.5),
        committedUnit(960, 1920, C, Q::Major, "I", R::None, 1.0),
    };
    const std::vector<FunctionalCadence> cadences = { cadence(0, 960, C, 3.0) };

    const FunctionLayerOutput out =
        assembleFunctionOutput(units, cadences, /*modulations=*/{}, /*homeTonic=*/C, /*homeMinor=*/false);

    ASSERT_EQ(out.units.size(), 2u);
    const FunctionAnalysisUnit& tonic = out.units[1];
    EXPECT_EQ(tonic.romanNumeral, "I");                       // the full DCML numeral, carried
    EXPECT_FALSE(tonic.openMark);
    EXPECT_DOUBLE_EQ(tonic.confidence.cadenceVoteWeight, 3.0);       // §5.2 — the PAC arriving in its span
    EXPECT_DOUBLE_EQ(tonic.confidence.licensedProgressionFit, 1.0);  // §5.0 — V→I is licensed
    EXPECT_DOUBLE_EQ(tonic.confidence.nextBestMargin, 1.0);          // §5.5 — the resolver confidence
    EXPECT_DOUBLE_EQ(tonic.confidence.combined, 5.0);               // default weights: 3 + 1 + 1

    // The region's FIRST unit has no preceding committed harmony → fit 0 (the motion into
    // the first unit is unscored).
    EXPECT_DOUBLE_EQ(out.units[0].confidence.licensedProgressionFit, 0.0);
}

TEST(FunctionOutput, LicensedFitZeroForUnlicensedMotion)
{
    // An ascending perfect fifth C→G (delta 7) is the retrograde of the descending-fifth
    // and is NOT in §5.0's enumerated licensed set (descending fifth / descending third /
    // ascending second / applied resolution), so the Step-1 predicate returns false and
    // the assembly faithfully reports licensed-fit 0.0.
    std::vector<FunctionUnitAssembly> units = {
        committedUnit(0, 960, C, Q::Major, "I", R::None, 0.5),
        committedUnit(960, 1920, G, Q::Major, "V", R::None, 0.5),
    };
    const FunctionLayerOutput out =
        assembleFunctionOutput(units, /*cadences=*/{}, /*modulations=*/{}, C, false);
    EXPECT_DOUBLE_EQ(out.units[1].confidence.licensedProgressionFit, 0.0);  // C→G is unlicensed
}

// ── §7: an undecided unit carries the honest open mark ────────────────────────────

TEST(FunctionOutput, UndecidedUnitCarriesOpenMark)
{
    // A genuinely undecided slice: the resolver carried the open mark (a displayed-but-
    // uncertain numeral). The assembly carries openMark == true AND the numeral (§7: the
    // mark names what is unresolved; the numeral is still displayed, never a guess erased).
    std::vector<FunctionUnitAssembly> units = {
        committedUnit(0, 960, D, Q::Diminished, "viio", R::None, 0.0),
    };
    units[0].openMark = true;
    units[0].committed = false;            // an L4 abstain the resolver could not decide
    units[0].resolverConfidence = 0.0;

    const FunctionLayerOutput out =
        assembleFunctionOutput(units, /*cadences=*/{}, /*modulations=*/{}, C, false);

    ASSERT_EQ(out.units.size(), 1u);
    EXPECT_TRUE(out.units[0].openMark);
    EXPECT_EQ(out.units[0].romanNumeral, "viio");           // the numeral is still carried to display
    EXPECT_DOUBLE_EQ(out.units[0].confidence.nextBestMargin, 0.0);
}

// ── §7: a region carries its local key + cadence markers ──────────────────────────

TEST(FunctionOutput, RegionCarriesHomeKeyAndCadencesWithoutModulation)
{
    std::vector<FunctionUnitAssembly> units = {
        committedUnit(0, 960, G, Q::Major, "V", R::None, 0.5),
        committedUnit(960, 1920, C, Q::Major, "I", R::None, 1.0),
    };
    const std::vector<FunctionalCadence> cadences = { cadence(0, 960, C, 3.0) };

    const FunctionLayerOutput out =
        assembleFunctionOutput(units, cadences, /*modulations=*/{}, /*homeTonic=*/C, /*homeMinor=*/false);

    EXPECT_EQ(out.region.startTick, 0);
    EXPECT_EQ(out.region.endTick, 1920);
    EXPECT_EQ(out.region.localTonicPc, C);       // no modulation → the home key
    EXPECT_FALSE(out.region.localMinorMode);
    EXPECT_FALSE(out.region.modulated);
    ASSERT_EQ(out.region.cadences.size(), 1u);   // the §5.2 markers carried verbatim
    EXPECT_EQ(out.region.cadences[0].arrivalTick, 960);
    EXPECT_EQ(out.region.cadences[0].type, FunctionalCadenceType::PerfectAuthentic);
}

TEST(FunctionOutput, RegionLocalKeyReflectsConfirmedModulation)
{
    std::vector<FunctionUnitAssembly> units = {
        committedUnit(0, 960, D, Q::Major, "V/V", R::AppliedSecondary, 1.0),
        committedUnit(960, 1920, G, Q::Major, "I", R::None, 1.0),
    };
    // A §5.4 confirmed modulation to G major over the region.
    ModulationDecision mod;
    mod.startTick = 0;
    mod.endTick = 1920;
    mod.tonicPc = G;
    mod.minorMode = false;
    mod.isModulation = true;

    const FunctionLayerOutput out =
        assembleFunctionOutput(units, /*cadences=*/{}, { mod }, /*homeTonic=*/C, /*homeMinor=*/false);

    EXPECT_EQ(out.region.localTonicPc, G);   // the confirmed modulation changed the local key
    EXPECT_FALSE(out.region.localMinorMode);
    EXPECT_TRUE(out.region.modulated);
}

TEST(FunctionOutput, RegionNonModulationDecisionKeepsHomeKey)
{
    // A §5.3 decision that did NOT cross the hysteresis (isModulation == false — a
    // tonicization) leaves the home key unchanged: the break-even defaults to tonicization.
    std::vector<FunctionUnitAssembly> units = {
        committedUnit(0, 960, D, Q::Major, "V/V", R::AppliedSecondary, 1.0),
    };
    ModulationDecision tonicization;
    tonicization.tonicPc = G;
    tonicization.isModulation = false;       // a tonicization, not a modulation

    const FunctionLayerOutput out =
        assembleFunctionOutput(units, /*cadences=*/{}, { tonicization }, /*homeTonic=*/C, /*homeMinor=*/false);

    EXPECT_EQ(out.region.localTonicPc, C);   // still the home key
    EXPECT_FALSE(out.region.modulated);
}

// ── §7: the output is ADDITIVE over the Layer-4 result (identity not replaced) ─────

TEST(FunctionOutput, AdditiveOverLayer4CommittedIdentityPreserved)
{
    // The committed L4 identity (root + quality) is carried VERBATIM alongside the L5
    // annotation — never overwritten by the assembly.
    std::vector<FunctionUnitAssembly> units = {
        committedUnit(0, 960, D, Q::Major, "V/V", R::AppliedSecondary, 1.0),
    };
    const FunctionLayerOutput out =
        assembleFunctionOutput(units, /*cadences=*/{}, /*modulations=*/{}, C, false);

    ASSERT_EQ(out.units.size(), 1u);
    EXPECT_EQ(out.units[0].committedIdentity.rootPc, D);          // L4's chord — unchanged
    EXPECT_EQ(out.units[0].committedIdentity.quality, Q::Major);
    EXPECT_EQ(out.units[0].romanNumeral, "V/V");                  // the L5 annotation, additive
    EXPECT_EQ(out.units[0].relationalRole, R::AppliedSecondary);
}

// ── §7: the cadence-vote component is attributed by tick (spatial, deterministic) ─

TEST(FunctionOutput, CadenceVoteAttributedToArrivalUnitOnly)
{
    // Two units; the cadence arrives in unit1's span only. unit0 gets no cadence vote.
    std::vector<FunctionUnitAssembly> units = {
        committedUnit(0, 960, G, Q::Major, "V", R::None, 0.5),
        committedUnit(960, 1920, C, Q::Major, "I", R::None, 1.0),
    };
    const std::vector<FunctionalCadence> cadences = { cadence(0, 960, C, 2.5) };

    const FunctionLayerOutput out =
        assembleFunctionOutput(units, cadences, /*modulations=*/{}, C, false);

    EXPECT_DOUBLE_EQ(out.units[0].confidence.cadenceVoteWeight, 0.0);   // no arrival in [0,960)... arrival is AT 960
    EXPECT_DOUBLE_EQ(out.units[1].confidence.cadenceVoteWeight, 2.5);   // arrival 960 ∈ [960,1920)
}
