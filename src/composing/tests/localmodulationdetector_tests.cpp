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

// localmodulationdetector_tests.cpp — Stage 4d-i.
//
// Pins the key-agnostic local-modulation detector (localmodulationdetector.{h,cpp}):
// the establishment (sustained consistent run ≥5 chords) + confirmation (V→I
// cadence inside the span) commit rule, the nearest-cadence region assignment, the
// chromatic-tolerance consistency test, and the home/modulation anchor tag.  Like
// the cadence tests, every input is a CadenceRegionInput built directly from root
// pc / quality / pitch mask — no key or function context — the structural proof of
// key-agnosticism.  Sequences are cadence-controlled (no accidental descending-fifth
// major→stable adjacencies) so only the intended cadences fire.

#include <gtest/gtest.h>

#include <set>
#include <vector>

#include "composing/analysis/section/localmodulationdetector.h"

using namespace mu::composing::analysis;

namespace {

uint16_t mask(std::initializer_list<int> pcs)
{
    uint16_t m = 0;
    for (int pc : pcs) {
        m |= static_cast<uint16_t>(1u << (((pc % 12) + 12) % 12));
    }
    return m;
}

CadenceRegionInput region(int startTick, int rootPc, ChordQuality q,
                          std::initializer_list<int> pcs)
{
    CadenceRegionInput r;
    r.startTick = startTick;
    r.endTick = startTick + 480;
    r.rootPc = rootPc;
    r.quality = q;
    r.pitchClassMask = mask(pcs);
    return r;
}

// Diatonic triads (480-tick regions). The constructor positions them on a 480 grid.
CadenceRegionInput Cmaj(int t) { return region(t, 0, ChordQuality::Major, { 0, 4, 7 }); }
CadenceRegionInput Gmaj(int t) { return region(t, 7, ChordQuality::Major, { 7, 11, 2 }); }
CadenceRegionInput Dmaj(int t) { return region(t, 2, ChordQuality::Major, { 2, 6, 9 }); }
CadenceRegionInput Emaj(int t) { return region(t, 4, ChordQuality::Major, { 4, 8, 11 }); }
CadenceRegionInput Fmaj(int t) { return region(t, 5, ChordQuality::Major, { 5, 9, 0 }); }
CadenceRegionInput Amin(int t) { return region(t, 9, ChordQuality::Minor, { 9, 0, 4 }); }
CadenceRegionInput Dmin(int t) { return region(t, 2, ChordQuality::Minor, { 2, 5, 9 }); }
CadenceRegionInput Emin(int t) { return region(t, 4, ChordQuality::Minor, { 4, 7, 11 }); }

} // namespace

// A single confirmed cadence (G→C) with a long surrounding consistent run is
// committed as one C-major span. Amin/Dmin are minor (never dominants) and
// F→G is not a fifth, so only the intended cadence fires.
TEST(LocalModulationDetector, SustainedConfirmedSpanCommitted)
{
    std::vector<CadenceRegionInput> regions = {
        Amin(0), Dmin(480), Fmaj(960), Gmaj(1440), Cmaj(1920),  // V(G)→I(C) at 1440→1920
    };
    const auto res = detectLocalModulations(regions, /*keySignatureFifths=*/0);
    ASSERT_EQ(res.spans.size(), 1u);
    EXPECT_EQ(res.spans[0].tonicPc, 0);
    EXPECT_FALSE(res.spans[0].minorMode);
    EXPECT_EQ(res.spans[0].establishmentChords, 5);
    EXPECT_GE(res.spans[0].confirmingCadenceCount, 1);
    EXPECT_EQ(res.spans[0].startTick, 0);
    EXPECT_EQ(res.spans[0].endTick, 1920 + 480);
}

// A confirmed cadence with too SHORT a run (< 5 chords) is NOT committed: a
// passing tonicization, not an established modulation (the conservative bar).
TEST(LocalModulationDetector, BriefRunNotCommitted)
{
    std::vector<CadenceRegionInput> regions = {
        Gmaj(0), Cmaj(480),   // a single V→I, only 2 consistent chords
    };
    const auto res = detectLocalModulations(regions, /*keySignatureFifths=*/0);
    EXPECT_TRUE(res.spans.empty());
}

// No authentic cadence ⇒ no candidate ⇒ no span (no major chord descends a fifth
// to a stable triad with its leading tone here).
TEST(LocalModulationDetector, NoCadenceNoSpan)
{
    std::vector<CadenceRegionInput> regions = {
        Dmin(0), Emin(480), Fmaj(960), Emin(1440), Dmin(1920), Amin(2400),
    };
    const auto res = detectLocalModulations(regions, /*keySignatureFifths=*/0);
    EXPECT_TRUE(res.spans.empty());
}

// A genuine modulation: a sustained C-major home with a G→C cadence, a sustained,
// cadence-confirmed G-major span (the dominant key), then a short return.  Both
// the home and the modulation commit; the key-agnostic anchor flags which is home.
TEST(LocalModulationDetector, HomeAndModulationSpansTagged)
{
    std::vector<CadenceRegionInput> regions = {
        Amin(0), Dmin(480), Gmaj(960), Cmaj(1440),                 // home C, G→I cadence
        Amin(1920), Dmaj(2400), Gmaj(2880),                        // modulate: D→G cadence
        Emin(3360), Dmaj(3840), Gmaj(4320),                        // sustain G: D→G cadence
        Dmin(4800), Gmaj(5280), Cmaj(5760),                        // return: G→C final cadence
    };
    const auto res = detectLocalModulations(regions, /*keySignatureFifths=*/0);
    ASSERT_EQ(res.spans.size(), 2u);
    EXPECT_TRUE(res.anchor.detected);

    // Two spans, one for C major (pc 0) and one for G major (pc 7); the
    // key-agnostic anchor tags exactly one of them as the home key (which one is
    // the home is a near-tie between C and G here — the robust invariant is that
    // exactly one is home and one is a modulation).
    std::set<int> tonics;
    int agree = 0, minorCount = 0;
    for (const auto& s : res.spans) {
        tonics.insert(s.tonicPc);
        if (s.agreesWithAnchor) ++agree;
        if (s.minorMode) ++minorCount;
    }
    EXPECT_EQ(tonics, (std::set<int>{ 0, 7 }));
    EXPECT_EQ(minorCount, 0);
    EXPECT_EQ(agree, 1);
}

// Minor-key modulation: a raised-leading-tone E→Am cadence with a sustained
// A-minor run is committed as a minor span (the raised LT G# is in the harmonic
// collection, so it does not count as a chromatic intrusion).
TEST(LocalModulationDetector, MinorKeyRaisedLeadingToneSpan)
{
    std::vector<CadenceRegionInput> regions = {
        Amin(0), Dmin(480), Fmaj(960), Emaj(1440), Amin(1920),   // V(E)→i(Am) at 1440→1920
    };
    const auto res = detectLocalModulations(regions, /*keySignatureFifths=*/0);
    ASSERT_EQ(res.spans.size(), 1u);
    EXPECT_EQ(res.spans[0].tonicPc, 9);
    EXPECT_TRUE(res.spans[0].minorMode);
    EXPECT_EQ(res.spans[0].establishmentChords, 5);
}

// Heavily-chromatic regions (root foreign to the key) are NOT consistent, so they
// get no assignment and break the run: the cadence's run is only the 2 cadence
// chords → not committed.
TEST(LocalModulationDetector, ChromaticRegionBreaksRun)
{
    auto Dbmaj = [](int t){ return region(t, 1, ChordQuality::Major, { 1, 5, 8 }); }; // root foreign to C
    std::vector<CadenceRegionInput> regions = {
        Dbmaj(0), Dbmaj(480), Dbmaj(960), Gmaj(1440), Cmaj(1920),
    };
    const auto res = detectLocalModulations(regions, /*keySignatureFifths=*/0);
    EXPECT_TRUE(res.spans.empty());
}

// Empty input ⇒ empty result, anchor undetected.
TEST(LocalModulationDetector, EmptyInput)
{
    const auto res = detectLocalModulations({}, 0);
    EXPECT_TRUE(res.spans.empty());
    EXPECT_FALSE(res.anchor.detected);
}
