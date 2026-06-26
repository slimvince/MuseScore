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

// ── Test-backfill (criteria 1-4): ChordSymbolFormatter::formatNashvilleNumber ─
//
// formatNashvilleNumber was asserted by a single test (the °°7 dedup case).
// The DECIDABLE oracle is the Nashville Number System itself: scale degrees map
// 1..7, and the per-quality / per-seventh suffixes are standard chord-symbol
// conventions (m, °, +, ø, sus2/sus4, maj7/7/°7). Those assertions are oracles.
//
// TWO behaviours here are documented PLACEHOLDERS ("// just show as ...; refine as
// needed" in chordsymbolformatter.cpp), NOT theory-decidable values — they are
// pinned only as explicitly-labelled REGRESSION GUARDS:
//   (a) a non-diatonic / out-of-range degree yields "?" (NOT "" — see the
//       SURFACED FINDING below);
//   (b) the slash-bass degree uses a crude semitone%7+1 map, not the true scale
//       degree of the bass.
//
// SURFACED FINDING (rule 2 — reported, not silently pinned): the test instruction
// stated the contract as "degree < 0 -> \"\"". Production actually emits "?" for a
// negative/out-of-range degree (nashvilleDegree() returns "?" outside 0..6, and
// formatNashvilleNumber then appends the quality/extension/bass suffixes). Neither
// "" nor "?" is mandated by the Nashville system (it has no symbol for a
// non-diatonic root); "?" is the code's deliberate placeholder. This is flagged for
// Cowork, not xfail'd, because the expected "" is not itself a proven oracle.

#include <gtest/gtest.h>

#include <string>

#include "composing/analysis/chord/chordanalyzer.h"

#include "test_helpers.h"

using namespace mu::composing::analysis;

namespace {
// UTF-8 byte sequences for the non-ASCII suffix glyphs (matches the formatter).
const std::string DEG = "\xc2\xb0";   // ° U+00B0
const std::string HD  = "\xc3\xb8";   // ø U+00F8

std::string nash(const ChordAnalysisResult& r) {
    return ChordSymbolFormatter::formatNashvilleNumber(r, /*keySignatureFifths=*/0);
}
} // namespace

// ── Scale degrees 1..7, major triads, root position (criterion 1, 3 — oracle) ─

TEST(Composing_NashvilleTests, ScaleDegrees_MajorTriads_MapOneToSeven)
{
    EXPECT_EQ(nash(makeRomanResult(0, ChordQuality::Major)), "1");
    EXPECT_EQ(nash(makeRomanResult(3, ChordQuality::Major)), "4");
    EXPECT_EQ(nash(makeRomanResult(4, ChordQuality::Major)), "5");
    EXPECT_EQ(nash(makeRomanResult(6, ChordQuality::Major)), "7");
}

// ── Per-quality suffixes (criterion 3 — chord-symbol convention oracle) ──────

TEST(Composing_NashvilleTests, QualitySuffixes_PerQuality)
{
    EXPECT_EQ(nash(makeRomanResult(1, ChordQuality::Minor)), "2m");
    EXPECT_EQ(nash(makeRomanResult(6, ChordQuality::Diminished)), "7" + DEG);
    EXPECT_EQ(nash(makeRomanResult(0, ChordQuality::Augmented)), "1+");
    EXPECT_EQ(nash(makeRomanResult(6, ChordQuality::HalfDiminished)), "7" + HD);
    EXPECT_EQ(nash(makeRomanResult(0, ChordQuality::Suspended2)), "1sus2");
    EXPECT_EQ(nash(makeRomanResult(0, ChordQuality::Suspended4)), "1sus4");
    EXPECT_EQ(nash(makeRomanResult(0, ChordQuality::Power)), "15");
}

// ── Sevenths (criterion 3 — oracle) ──────────────────────────────────────────

TEST(Composing_NashvilleTests, Sevenths_DominantMajorAndFullyDiminished)
{
    // V7 = degree 5, dominant (Major + minor 7th) -> "57".
    EXPECT_EQ(nash(makeRomanResult(4, ChordQuality::Major, 0, 0, /*min7=*/true)), "57");
    // Imaj7 -> "1maj7".
    EXPECT_EQ(nash(makeRomanResult(0, ChordQuality::Major, 0, 0, false, /*maj7=*/true)), "1maj7");
    // vii°7: quality "°" + extension "°7" collapse to a single "°" -> "7°7"
    // (the dedup path; mirrors the existing real-chord test, here via a direct result).
    EXPECT_EQ(nash(makeRomanResult(6, ChordQuality::Diminished, 0, 0, false, false, /*dim7=*/true)),
              "7" + DEG + "7");
}

// ── Minor-key tonic (criterion 1 — oracle) ───────────────────────────────────

TEST(Composing_NashvilleTests, MinorKeyTonic_DegreeIsModeIndependent)
{
    // i in a minor key: degree index 0, Minor quality, Aeolian mode -> "1m".
    // nashvilleDegree maps the diatonic degree index only; the mode does not change it.
    EXPECT_EQ(nash(makeRomanResult(0, ChordQuality::Minor, 0, 0, false, false, false, false,
                                   /*keyTonicPc=*/0, KeySigMode::Aeolian)),
              "1m");
}

// ── REGRESSION GUARD: slash-bass uses a crude semitone map (not the true degree) ─

TEST(Composing_NashvilleTests, RegressionGuard_InversionSlashBass_CrudeSemitoneDegree)
{
    // C/E (root pc 0, bass pc 4 = E), key C: nashvilleBassSuffix uses
    // ((bassPc - keyTonicPc) % 7) + 1 = (4 % 7) + 1 = 5 -> "/5". Musically E is the
    // 3rd of C, so "/5" is the crude-placeholder output, pinned as a change detector.
    EXPECT_EQ(nash(makeRomanResult(0, ChordQuality::Major, /*rootPc=*/0, /*bassPc=*/4)), "1/5");
}

// ── REGRESSION GUARD: non-diatonic / out-of-range degree -> "?" (placeholder) ─

TEST(Composing_NashvilleTests, RegressionGuard_NegativeDegree_YieldsQuestionMarkNotEmpty)
{
    // SURFACED FINDING: the instruction expected "" here; production emits "?".
    // Pinned as the current placeholder behaviour (see file header).
    EXPECT_EQ(nash(makeRomanResult(-1, ChordQuality::Major)), "?");
    // A default result (degree -1, Unknown quality) is also "?", not "".
    EXPECT_EQ(nash(ChordAnalysisResult{}), "?");
}

TEST(Composing_NashvilleTests, RegressionGuard_DegreeAtOrAboveSeven_YieldsQuestionMark)
{
    // Degrees are 1..7 (index 0..6); index 7 is out of contract -> "?".
    EXPECT_EQ(nash(makeRomanResult(7, ChordQuality::Major)), "?");
}
