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

// functionmodulation_tests.cpp — Architectural Layer 5 (FUNCTION), Phase 5c Step 4.
//
// Oracle tests for the §5.3 tonicization-vs-modulation arbiter + the §5.4 cadence-
// confirmed modulation recompute (the §8 case-4 channel #1). Every input is built
// by hand from the producer-agnostic value types (LocalKeySpan, FunctionalCadence,
// OnePassClosure) — the unit reads no score/region/decoder type — asserting the
// SIGNED contract cowork_layer5_function_design.md §5.3 + §5.4 + §8:
//   • a cadence-LESS lean stays HOME (tonicization is the default);
//   • a cadence-confirmed + persistent candidate MODULATES and the recompute re-reads
//     the region in the new key;
//   • the BREAK-EVEN defaults to tonicization (the strict-inequality tie-direction);
//   • the RELATIVE PAIR is decided by the cadence tonic-vote;
//   • the §8 CLOSURE holds on the recompute (no re-open, no recursion);
//   • the convenience path REUSES detectLocalModulations (the substrate is invoked,
//     not re-implemented).
// Constants are firewall DEFAULTS (no tuning); the cases assert DIRECTION + structure.

#include <gtest/gtest.h>

#include <vector>

#include "composing/analysis/function/functionmodulation.h"

using namespace mu::composing::analysis;

namespace {

constexpr double kWhole = kTicksPerWholeNote;   // 1920 ticks

// One committed candidate local-key span (as detectLocalModulations would emit). The
// establishment/confirmation counts are the detector's candidate floor (untouched by
// the arbiter); agreesAnchor tags the home key.
LocalKeySpan span(int startTick, int endTick, int tonicPc, bool minor, bool agreesAnchor)
{
    LocalKeySpan s;
    s.startTick = startTick;
    s.endTick = endTick;
    s.tonicPc = tonicPc;
    s.minorMode = minor;
    s.agreesWithAnchor = agreesAnchor;
    s.establishmentChords = 5;
    s.confirmingCadenceCount = 1;
    return s;
}

ModulationDetectionResult detected(std::vector<LocalKeySpan> spans)
{
    ModulationDetectionResult r;
    r.spans = std::move(spans);
    return r;
}

// One §5.2 cadence voting for (tonicPc, minor) at the given arrival, with the given vote.
FunctionalCadence cad(int arrivalTick, int tonicPc, bool minor, double vote)
{
    FunctionalCadence c;
    c.type = FunctionalCadenceType::PerfectAuthentic;
    c.arrivalTick = arrivalTick;
    c.tonicPc = tonicPc;
    c.minorMode = minor;
    c.tonicVote = vote;
    return c;
}

// A no-op re-read sink.
const std::function<void(int, int, bool)> kNoopReread = [](int, int, bool) {};

} // namespace

// ── §5.3 — a cadence-LESS lean stays HOME (tonicization is the default) ─────────
TEST(FunctionModulation, CadencelessLeanStaysTonicization)
{
    // An away candidate span (3 whole notes long) but NO cadence confirms its key.
    const auto det = detected({ span(0, static_cast<int>(3 * kWhole), 7, /*minor=*/false, /*home=*/false) });
    const std::vector<FunctionalCadence> noCadence;

    const auto d = decideTonicizationVsModulation(det, noCadence);
    ASSERT_EQ(d.size(), 1u);
    EXPECT_FALSE(d[0].cadenceConfirmed) << "no cadence in the candidate key — the necessary gate (a) fails";
    EXPECT_FALSE(d[0].isModulation) << "a lean with no confirming cadence stays a tonicization (the home key holds)";

    // The §5.4 recompute does not fire and does not close the key decision.
    OnePassClosure closure;
    int reads = 0;
    const auto rr = modulationRecompute(d[0], /*homeKeyConfidence=*/0.5, /*first=*/0, /*last=*/4,
                                        [&](int, int, bool) { ++reads; }, closure, /*keyId=*/100);
    EXPECT_FALSE(rr.fired);
    EXPECT_EQ(reads, 0);
    EXPECT_FALSE(closure.isClosed(100));
}

// ── §5.3 + §5.4 — a cadence-confirmed + persistent candidate MODULATES, and the
//    recompute re-reads the region in the new key ─────────────────────────────────
TEST(FunctionModulation, ConfirmedPersistentModulatesAndRecomputes)
{
    const auto det = detected({ span(0, static_cast<int>(3 * kWhole), 7, /*minor=*/false, /*home=*/false) });
    const std::vector<FunctionalCadence> cads = { cad(/*arrival=*/static_cast<int>(1.5 * kWhole), 7, false, 2.0) };

    const auto d = decideTonicizationVsModulation(det, cads);
    ASSERT_EQ(d.size(), 1u);
    EXPECT_TRUE(d[0].cadenceConfirmed);
    EXPECT_EQ(d[0].confirmingCadenceCount, 1);
    EXPECT_DOUBLE_EQ(d[0].cadentialWeight, 2.0);
    EXPECT_DOUBLE_EQ(d[0].durationWholeNotes, 3.0);
    EXPECT_TRUE(d[0].isModulation) << "cadence-confirmed + persistent ⇒ a modulation";

    // The §5.4 recompute fires (cadence strength 2.0 > bar 1.5 at home-confidence 0.5)
    // and re-reads the region's slice range ONCE each in forward order, in the new key.
    OnePassClosure closure;
    std::vector<int> sweep;
    int seenTonic = -1;
    bool seenMinor = true;
    const auto rr = modulationRecompute(
        d[0], /*homeKeyConfidence=*/0.5, /*first=*/3, /*last=*/7,
        [&](int sliceId, int newTonic, bool newMinor) { sweep.push_back(sliceId); seenTonic = newTonic; seenMinor = newMinor; },
        closure, /*keyId=*/7);

    EXPECT_TRUE(rr.fired);
    EXPECT_EQ(rr.newTonicPc, 7);
    EXPECT_FALSE(rr.newMinorMode);
    EXPECT_EQ(rr.slicesReread, 5);
    EXPECT_EQ(sweep, (std::vector<int>{ 3, 4, 5, 6, 7 })) << "a single forward sweep, each slice once";
    EXPECT_EQ(seenTonic, 7) << "each slice re-read in the new local key";
    EXPECT_FALSE(seenMinor);
    EXPECT_TRUE(closure.isClosed(7)) << "the key decision is closed for the pass (§8)";
}

// ── §5.3 — the BREAK-EVEN defaults to tonicization (the strict-inequality tie) ───
TEST(FunctionModulation, BreakEvenDefaultsToTonicization)
{
    // Evidence == change-cost EXACTLY: 0.5 whole-note duration + 0.5 cadential weight
    // = 1.0 == baseChangeCost. The strict `>` ⇒ the home key holds.
    const auto det = detected({ span(0, static_cast<int>(0.5 * kWhole), 7, false, false) });
    const std::vector<FunctionalCadence> atBar = { cad(static_cast<int>(0.25 * kWhole), 7, false, 0.5) };

    const auto d = decideTonicizationVsModulation(det, atBar);
    ASSERT_EQ(d.size(), 1u);
    EXPECT_TRUE(d[0].cadenceConfirmed);
    EXPECT_DOUBLE_EQ(d[0].persistenceEvidence, 1.0);
    EXPECT_DOUBLE_EQ(d[0].changeCost, 1.0);
    EXPECT_FALSE(d[0].isModulation) << "at the exact break-even the rule defaults to tonicization";

    // Just ABOVE the bar (cadential weight 0.6 ⇒ evidence 1.1 > 1.0) ⇒ a modulation.
    const auto det2 = detected({ span(0, static_cast<int>(0.5 * kWhole), 7, false, false) });
    const std::vector<FunctionalCadence> overBar = { cad(static_cast<int>(0.25 * kWhole), 7, false, 0.6) };
    const auto d2 = decideTonicizationVsModulation(det2, overBar);
    ASSERT_EQ(d2.size(), 1u);
    EXPECT_GT(d2[0].persistenceEvidence, d2[0].changeCost);
    EXPECT_TRUE(d2[0].isModulation) << "crossing the change-cost ⇒ the key change commits";
}

// ── §5.5/§5.3 — the RELATIVE PAIR is decided by the cadence tonic-vote ───────────
TEST(FunctionModulation, RelativePairDecidedByTonicVote)
{
    // Two away candidates a third apart — the relative pair C major / A minor — both
    // sustained equally. Only A minor receives a cadence: the tonic-vote alone decides
    // which centre becomes the key (the note evidence is identical between them).
    const auto det = detected({
        span(0, static_cast<int>(3 * kWhole), 0, /*minor=*/false, /*home=*/false),   // C major (relative major)
        span(0, static_cast<int>(3 * kWhole), 9, /*minor=*/true,  /*home=*/false),   // A minor (relative minor)
    });
    const std::vector<FunctionalCadence> cads = { cad(static_cast<int>(1.5 * kWhole), 9, /*minor=*/true, 2.0) };

    const auto d = decideTonicizationVsModulation(det, cads);
    ASSERT_EQ(d.size(), 2u);

    // C major: no cadence in its key ⇒ stays a tonicization.
    EXPECT_FALSE(d[0].cadenceConfirmed);
    EXPECT_FALSE(d[0].isModulation);
    // A minor: the cadence tonic-vote selects it as the centre ⇒ the modulation.
    EXPECT_TRUE(d[1].cadenceConfirmed);
    EXPECT_TRUE(d[1].isModulation);
}

// ── §8 — the closure holds on the recompute: no re-open, no recursion ───────────
TEST(FunctionModulation, RecomputeClosureNoReopenNoRecursion)
{
    const auto det = detected({ span(0, static_cast<int>(3 * kWhole), 7, false, false) });
    const std::vector<FunctionalCadence> cads = { cad(static_cast<int>(1.5 * kWhole), 7, false, 2.0) };
    const auto d = decideTonicizationVsModulation(det, cads);
    ASSERT_EQ(d.size(), 1u);
    ASSERT_TRUE(d[0].isModulation);

    // (1) NO RE-OPEN — fire once, then a second override on the same key id is refused.
    OnePassClosure closure;
    const auto rr1 = modulationRecompute(d[0], 0.5, 0, 3, kNoopReread, closure, /*keyId=*/7);
    EXPECT_TRUE(rr1.fired);
    EXPECT_TRUE(closure.isClosed(7));
    const auto rr2 = modulationRecompute(d[0], 0.5, 0, 3, kNoopReread, closure, /*keyId=*/7);
    EXPECT_FALSE(rr2.fired) << "the closed key decision is not re-targeted (§8 no re-open)";
    EXPECT_EQ(rr2.slicesReread, 0);
    EXPECT_EQ(closure.closedCount(), 1) << "exactly one decision closed this pass";

    // (2) NO RECURSION — a nested recompute invoked from WITHIN the active sweep has its
    // localized forward re-run REFUSED (the re-entrancy guard), even though its override
    // logic runs. "one localized forward re-run, never a loop."
    OnePassClosure closure2;
    bool nestedFired = false;
    int nestedReads = -999;
    // A SINGLE-slice outer sweep [0,0] so the nested attempt is made exactly once
    // (a multi-slice sweep would re-attempt key 99, now closed, and overwrite the capture).
    const auto rr3 = modulationRecompute(
        d[0], 0.5, 0, 0,
        [&](int, int, bool) {
            const auto inner = modulationRecompute(d[0], 0.5, 5, 6, kNoopReread, closure2, /*keyId=*/99);
            nestedFired = inner.fired;
            nestedReads = inner.slicesReread;
        },
        closure2, /*keyId=*/7);
    EXPECT_TRUE(rr3.fired);
    EXPECT_TRUE(nestedFired) << "the nested override's threshold still evaluates";
    EXPECT_EQ(nestedReads, -1) << "but its localized forward sweep is refused during the active sweep (no loop)";
}

// ── REUSE — the convenience path actually invokes detectLocalModulations ─────────
TEST(FunctionModulation, DetectAndDecideReusesTheDetectorSubstrate)
{
    // A key-agnostic region stream (the localmodulationdetector test corpus): a
    // sustained C-major home + a sustained, cadence-confirmed G-major span. The
    // detector commits TWO spans (tonics {0, 7}, one tagged home); the arbiter then
    // applies §5.3 — the home span stays, the away span (given a confirming cadence)
    // modulates. This proves detectLocalModulations is REUSED end-to-end.
    auto region = [](int startTick, int rootPc, ChordQuality q, std::initializer_list<int> pcs) {
        CadenceRegionInput r;
        r.startTick = startTick;
        r.endTick = startTick + 480;
        r.rootPc = rootPc;
        r.quality = q;
        uint16_t m = 0;
        for (int pc : pcs) {
            m |= static_cast<uint16_t>(1u << (((pc % 12) + 12) % 12));
        }
        r.pitchClassMask = m;
        return r;
    };
    auto Cmaj = [&](int t) { return region(t, 0, ChordQuality::Major, { 0, 4, 7 }); };
    auto Gmaj = [&](int t) { return region(t, 7, ChordQuality::Major, { 7, 11, 2 }); };
    auto Dmaj = [&](int t) { return region(t, 2, ChordQuality::Major, { 2, 6, 9 }); };
    auto Emin = [&](int t) { return region(t, 4, ChordQuality::Minor, { 4, 7, 11 }); };
    auto Amin = [&](int t) { return region(t, 9, ChordQuality::Minor, { 9, 0, 4 }); };
    auto Dmin = [&](int t) { return region(t, 2, ChordQuality::Minor, { 2, 5, 9 }); };

    const std::vector<CadenceRegionInput> regions = {
        Amin(0), Dmin(480), Gmaj(960), Cmaj(1440),       // home C, G→C cadence
        Amin(1920), Dmaj(2400), Gmaj(2880),              // modulate: D→G
        Emin(3360), Dmaj(3840), Gmaj(4320),              // sustain G: D→G
        Dmin(4800), Gmaj(5280), Cmaj(5760),              // return: G→C
    };

    // Cadences voting for both home-pair tonics across the timeline, so whichever span
    // is the away one carries a confirming cadence inside it.
    std::vector<FunctionalCadence> cads;
    for (int arr : { 1440, 1920, 2880, 4320, 5760 }) {
        cads.push_back(cad(arr, 0, false, 1.0));   // C major
        cads.push_back(cad(arr, 7, false, 1.0));   // G major
    }

    const auto decisions = detectAndDecideModulations(regions, cads, /*keySignatureFifths=*/0);
    ASSERT_EQ(decisions.size(), 2u) << "the detector committed two spans (it was actually invoked)";

    int homeCount = 0, modCount = 0;
    for (const auto& dec : decisions) {
        if (dec.isHomeKey) {
            ++homeCount;
            EXPECT_FALSE(dec.isModulation) << "the home key is never a modulation";
        } else {
            ++modCount;
            EXPECT_TRUE(dec.isModulation) << "the away, cadence-confirmed, sustained span modulates";
        }
    }
    EXPECT_EQ(homeCount, 1);
    EXPECT_EQ(modCount, 1);
}
