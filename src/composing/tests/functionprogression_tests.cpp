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

// functionprogression_tests.cpp — Architectural Layer 5 (FUNCTION), Phase 5c Step 1.
//
// Oracle-asserted against known music theory (NOT echoes of the analyzer): the
// §5.0 licensed-progression predicate (a descending-fifth is licensed; an applied
// resolution is licensed; an arbitrary non-functional tritone leap is NOT), and the
// stream queries "prevailing harmony" + "established next function" on small
// fixtures. Spec: cowork_layer5_function_design.md §5.0.

#include <gtest/gtest.h>

#include "composing/analysis/function/functionprogression.h"

using namespace mu::composing::analysis;

namespace {

ProgressionChord chord(int rootPc, ChordQuality quality)
{
    ProgressionChord c;
    c.rootPc = rootPc;
    c.quality = quality;
    return c;
}

ProgressionSlice committedSlice(int rootPc, ChordQuality quality, double metricWeight)
{
    ProgressionSlice s;
    s.chord = chord(rootPc, quality);
    s.committed = true;
    s.metricWeight = metricWeight;
    return s;
}

ProgressionSlice abstainedSlice(double metricWeight)
{
    ProgressionSlice s;
    s.committed = false;
    s.metricWeight = metricWeight;
    return s;
}

// Pitch classes for readability.
constexpr int C = 0, D = 2, E = 4, F = 5, Fs = 6, G = 7, A = 9, Bb = 10, B = 11;

} // namespace

// ── §5.0 licensed-progression predicate ───────────────────────────────────────

TEST(FunctionProgression, DescendingFifthIsLicensed)
{
    // V→I in C major: G→C is a descending-fifth (dominant) motion.
    EXPECT_TRUE(isDescendingFifth(G, C));
    EXPECT_TRUE(isLicensedProgression(chord(G, ChordQuality::Major),
                                      chord(C, ChordQuality::Major)));
}

TEST(FunctionProgression, AppliedChordResolutionIsLicensed)
{
    // Applied dominant V/V→V: D major dominant resolving down a fifth to G.
    EXPECT_TRUE(isAppliedResolution(chord(D, ChordQuality::Major),
                                    chord(G, ChordQuality::Major)));
    EXPECT_TRUE(isLicensedProgression(chord(D, ChordQuality::Major),
                                      chord(G, ChordQuality::Major)));

    // Secondary leading-tone viio/V→V: F#-diminished resolving up a semitone to G.
    EXPECT_TRUE(isAppliedResolution(chord(Fs, ChordQuality::Diminished),
                                    chord(G, ChordQuality::Major)));
    EXPECT_TRUE(isLicensedProgression(chord(Fs, ChordQuality::Diminished),
                                      chord(G, ChordQuality::Major)));

    // Half-diminished pre-dominant up a P4 to a major target (resolutionEdge): Dø7→G.
    EXPECT_TRUE(isAppliedResolution(chord(D, ChordQuality::HalfDiminished),
                                    chord(G, ChordQuality::Major)));
}

TEST(FunctionProgression, NonFunctionalTritoneLeapIsNotLicensed)
{
    // C→F# (a tritone leap) is none of the licensed successions and not a resolution.
    EXPECT_FALSE(isDescendingFifth(C, Fs));
    EXPECT_FALSE(isDescendingThird(C, Fs));
    EXPECT_FALSE(isAscendingSecond(C, Fs));
    EXPECT_FALSE(isAppliedResolution(chord(C, ChordQuality::Major),
                                     chord(Fs, ChordQuality::Major)));
    EXPECT_FALSE(isLicensedProgression(chord(C, ChordQuality::Major),
                                       chord(Fs, ChordQuality::Major)));
}

TEST(FunctionProgression, DescendingThirdAndAscendingSecondAreLicensed)
{
    // I→vi (descending minor third): C→A.
    EXPECT_TRUE(isDescendingThird(C, A));
    EXPECT_TRUE(isLicensedProgression(chord(C, ChordQuality::Major),
                                      chord(A, ChordQuality::Minor)));
    // vi→IV (descending major third): A→F.
    EXPECT_TRUE(isDescendingThird(A, F));
    // IV→V (ascending major second): F→G.
    EXPECT_TRUE(isAscendingSecond(F, G));
    EXPECT_TRUE(isLicensedProgression(chord(F, ChordQuality::Major),
                                      chord(G, ChordQuality::Major)));
    // vii→I (ascending minor second): B→C.
    EXPECT_TRUE(isAscendingSecond(B, C));
}

TEST(FunctionProgression, SameRootIsNotALicensedProgression)
{
    // Root continuity (delta 0) is no root MOTION → not a §5.0 progression. This
    // also pins the deliberate exclusion of the augmented→same-root resolution edge.
    EXPECT_FALSE(isLicensedProgression(chord(C, ChordQuality::Major),
                                       chord(C, ChordQuality::Major)));
    EXPECT_FALSE(isAppliedResolution(chord(C, ChordQuality::Augmented),
                                     chord(C, ChordQuality::Major)));
    EXPECT_FALSE(isLicensedProgression(chord(C, ChordQuality::Augmented),
                                       chord(C, ChordQuality::Major)));
}

TEST(FunctionProgression, MissingRootLicensesNothing)
{
    EXPECT_FALSE(isLicensedProgression(chord(-1, ChordQuality::Major),
                                       chord(G, ChordQuality::Major)));
    EXPECT_FALSE(isLicensedProgression(chord(G, ChordQuality::Major),
                                       chord(-1, ChordQuality::Major)));
}

// ── §5.0 prevailing harmony ───────────────────────────────────────────────────

TEST(FunctionProgression, PrevailingHarmonyIsNearestStrongAtOrBefore)
{
    // [0] C downbeat (strong), [1] D subbeat (passing), [2] E subbeat (passing),
    // [3] F beat (strong). A weak passing slice's prevailing harmony is the nearest
    // metrically-strong committed chord at or before it.
    Progression region = {
        committedSlice(C, ChordQuality::Major, 1.0),
        committedSlice(D, ChordQuality::Minor, 0.5),
        committedSlice(E, ChordQuality::Minor, 0.5),
        committedSlice(F, ChordQuality::Major, 0.85),
    };

    EXPECT_TRUE(isMetricallyStrong(region, 0));
    EXPECT_FALSE(isMetricallyStrong(region, 1));
    EXPECT_FALSE(isMetricallyStrong(region, 2));
    EXPECT_TRUE(isMetricallyStrong(region, 3));

    EXPECT_EQ(prevailingHarmonyIndex(region, 0), 0);  // a strong committed slice is its own prevailing harmony
    EXPECT_EQ(prevailingHarmonyIndex(region, 1), 0);  // passing D heard against C
    EXPECT_EQ(prevailingHarmonyIndex(region, 2), 0);  // passing E still heard against C
    EXPECT_EQ(prevailingHarmonyIndex(region, 3), 3);  // F is itself strong
}

TEST(FunctionProgression, PrevailingHarmonySkipsAbstainedSlices)
{
    // [0] C strong committed downbeat, [1] a STRONG but ABSTAINED slice (no committed
    // chord), [2] D weak committed passing, [3] G strong committed downbeat (so D is
    // interior-weak). The abstained slice is metrically strong yet must be skipped —
    // prevailing harmony is a COMMITTED chord (§5.0), so it falls back to C.
    Progression region = {
        committedSlice(C, ChordQuality::Major, 1.0),
        abstainedSlice(1.0),
        committedSlice(D, ChordQuality::Minor, 0.5),
        committedSlice(G, ChordQuality::Major, 1.0),
    };
    EXPECT_TRUE(isMetricallyStrong(region, 1));  // strong by metric position …
    EXPECT_FALSE(region[1].committed);           // … but not committed, so skipped below.

    EXPECT_EQ(prevailingHarmonyIndex(region, 1), 0);  // abstained strong slice skipped → committed C
    EXPECT_EQ(prevailingHarmonyIndex(region, 2), 0);  // weak D heard against C
}

TEST(FunctionProgression, PrevailingHarmonyOutOfRangeIsMinusOne)
{
    Progression region = { committedSlice(C, ChordQuality::Major, 1.0) };
    EXPECT_EQ(prevailingHarmonyIndex(region, -1), -1);
    EXPECT_EQ(prevailingHarmonyIndex(region, 5), -1);
}

// ── §5.0 established next function ─────────────────────────────────────────────

TEST(FunctionProgression, EstablishedNextFunctionSkipsAbstains)
{
    // [0] C committed, [1] abstain, [2] G committed.
    Progression region = {
        committedSlice(C, ChordQuality::Major, 1.0),
        abstainedSlice(0.5),
        committedSlice(G, ChordQuality::Major, 0.85),
    };
    EXPECT_EQ(establishedNextFunctionIndex(region, 0), 2);  // skips the abstained slice
    EXPECT_EQ(establishedNextFunctionIndex(region, 1), 2);
    EXPECT_EQ(establishedNextFunctionIndex(region, 2), -1); // nothing committed follows
}
