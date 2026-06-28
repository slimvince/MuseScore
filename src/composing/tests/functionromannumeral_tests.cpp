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

// functionromannumeral_tests.cpp — Architectural Layer 5 (FUNCTION), Phase 5c Step 1.
//
// Oracle-asserted against known music theory: the §5.1 base Roman-numeral
// derivation emits the correct full numeral (degree + quality + figured-bass
// inversion + a chromatic case + an applied label) for a known chord in a known
// key, and the wrap is FAITHFUL — the wrapper reproduces a direct
// ChordSymbolFormatter::formatRomanNumeral() call exactly (not a re-derivation).
// Spec: cowork_layer5_function_design.md §5.1.

#include <gtest/gtest.h>

#include "composing/analysis/function/functionromannumeral.h"
#include "composing/analysis/chord/chordanalyzer.h"   // ChordAnalysisResult, Extension, ChordSymbolFormatter

using namespace mu::composing::analysis;

namespace {

using Q = ChordQuality;
using E = Extension;

// ø U+00F8 (half-diminished glyph the formatter emits).
const std::string OE = "\xc3\xb8";

// Build a base-RN input in C major (keyFifths 0, Ionian, tonic pc 0) for a chord
// with the given root/bass/quality/extensions and optional next root.
BaseRomanNumeralInput inCMajor(int rootPc, int bassPc, Q quality,
                               std::initializer_list<E> exts = {}, int nextRootPc = -1)
{
    BaseRomanNumeralInput in;
    in.identity.rootPc = rootPc;
    in.identity.bassPc = bassPc;
    in.identity.rootTpc = -1;
    in.identity.bassTpc = -1;
    in.identity.quality = quality;
    for (E e : exts) {
        setExtension(in.identity.extensions, e);
    }
    in.keyFifths = 0;
    in.keyMode = KeySigMode::Ionian;
    in.keyTonicPc = 0;
    in.nextRootPc = nextRootPc;
    return in;
}

constexpr int C = 0, G = 7, B = 11, Bb = 10, D = 2;

} // namespace

// ── §5.1 the correct full numeral (degree + quality + inversion + chromatic) ────

TEST(FunctionRomanNumeral, DiatonicTriadDegreeAndQuality)
{
    // G major triad in C major = V (degree computed by diatonicDegreeForRootPc).
    const BaseRomanNumeral v = deriveBaseRomanNumeral(inCMajor(G, G, Q::Major));
    EXPECT_EQ(v.label, "V");
    EXPECT_EQ(v.degree, 4);          // 0-indexed scale degree of the dominant
    EXPECT_TRUE(v.diatonicToKey);
}

TEST(FunctionRomanNumeral, SeventhAndFiguredBassInversion)
{
    // G7 root position = V7.
    EXPECT_EQ(deriveBaseRomanNumeral(inCMajor(G, G, Q::Major, {E::MinorSeventh})).label, "V7");
    // G major triad in first inversion (bass = B, the third) = V6.
    EXPECT_EQ(deriveBaseRomanNumeral(inCMajor(G, B, Q::Major)).label, "V6");
    // G7 in first inversion (bass = B) = V65.
    EXPECT_EQ(deriveBaseRomanNumeral(inCMajor(G, B, Q::Major, {E::MinorSeventh})).label, "V65");
}

TEST(FunctionRomanNumeral, ChromaticRootAlteration)
{
    // Bb major in C major is a non-diatonic root → chromatic numeral bVII, no key change.
    const BaseRomanNumeral bvii = deriveBaseRomanNumeral(inCMajor(Bb, Bb, Q::Major));
    EXPECT_EQ(bvii.label, "bVII");
    EXPECT_EQ(bvii.degree, -1);
    EXPECT_FALSE(bvii.diatonicToKey);
}

TEST(FunctionRomanNumeral, AppliedSecondaryLabelCarriedThrough)
{
    // D7 in C major resolving to G is V7/V (the existing emitter's inline applied
    // label, carried through the wrap; full §5.6 relational treatment is Step 5).
    EXPECT_EQ(deriveBaseRomanNumeral(inCMajor(D, D, Q::Major, {E::MinorSeventh}, /*next=*/G)).label,
              "V7/V");
    // F#ø7 resolving to G is the secondary leading-tone label viiø7/V.
    EXPECT_EQ(deriveBaseRomanNumeral(inCMajor(/*F#=*/6, /*F#=*/6, Q::HalfDiminished, {}, /*next=*/G)).label,
              "vii" + OE + "7/V");
}

// ── §5.1 the wrap is faithful (reproduces a direct formatter call) ─────────────

TEST(FunctionRomanNumeral, WrapReproducesDirectFormatterCall_Diatonic)
{
    // Build the result the way the formatter's own tests do: degree set by hand.
    ChordAnalysisResult direct;
    direct.identity.rootPc = G;
    direct.identity.bassPc = G;
    direct.identity.rootTpc = -1;
    direct.identity.bassTpc = -1;
    direct.identity.quality = Q::Major;
    direct.function.degree = 4;          // V, set manually
    direct.function.keyTonicPc = 0;
    direct.function.keyMode = KeySigMode::Ionian;
    const std::string fromFormatter = ChordSymbolFormatter::formatRomanNumeral(direct);

    // The wrapper computes the SAME degree via diatonicDegreeForRootPc and produces
    // the SAME string — proving it wraps the one formatter, not a re-derivation.
    const BaseRomanNumeral wrapped = deriveBaseRomanNumeral(inCMajor(G, G, Q::Major));
    EXPECT_EQ(wrapped.label, fromFormatter);
    EXPECT_EQ(wrapped.degree, direct.function.degree);
}

TEST(FunctionRomanNumeral, WrapReproducesDirectFormatterCall_Chromatic)
{
    // Chromatic path: degree -1 (non-diatonic), keyTonicPc drives the chromatic numeral.
    ChordAnalysisResult direct;
    direct.identity.rootPc = Bb;
    direct.identity.bassPc = Bb;
    direct.identity.rootTpc = -1;
    direct.identity.bassTpc = -1;
    direct.identity.quality = Q::Major;
    direct.function.degree = -1;
    direct.function.keyTonicPc = 0;
    direct.function.keyMode = KeySigMode::Ionian;
    const std::string fromFormatter = ChordSymbolFormatter::formatRomanNumeral(direct);

    const BaseRomanNumeral wrapped = deriveBaseRomanNumeral(inCMajor(Bb, Bb, Q::Major));
    EXPECT_EQ(wrapped.label, fromFormatter);
    EXPECT_EQ(wrapped.degree, -1);
}

// Degenerate input: no committed root → empty numeral (the formatter's contract),
// surfaced honestly rather than guessed.
TEST(FunctionRomanNumeral, NoRootYieldsEmptyNumeral)
{
    BaseRomanNumeralInput in = inCMajor(/*root=*/-1, /*bass=*/-1, Q::Unknown);
    const BaseRomanNumeral out = deriveBaseRomanNumeral(in);
    EXPECT_EQ(out.degree, -1);
}
