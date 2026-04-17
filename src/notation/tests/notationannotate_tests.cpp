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

// ── Unit tests for cadence and pivot detection helpers ────────────────────────
//
// Tests for detectCadences() and detectPivotChords() in
// notationcomposingbridgehelpers.h/cpp.  These functions take
// HarmonicRegion vectors; no Score object is required.

#include <gtest/gtest.h>

// Engraving headers required before notationcomposingbridgehelpers.h because
// that header declares functions taking mu::engraving types (BeatType, Score*).
#include "engraving/dom/masterscore.h"
#include "engraving/dom/sig.h"

#include "composing/analysis/chord/chordanalyzer.h"
#include "composing/analysis/key/keymodeanalyzer.h"
#include "composing/analysis/region/harmonicrhythm.h"

#include "notation/internal/notationcomposingbridgehelpers.h"

using namespace mu::composing::analysis;
using namespace mu::notation::internal;

namespace {

// Ticks per quarter note — 480 in MuseScore's encoding.
// Used to give regions plausible durations; the detection logic does not
// care about exact tick values, only their ordering.
constexpr int kQ = 480;

// ── Region construction helpers ──────────────────────────────────────────────

/// Build a ChordAnalysisResult for a diatonic chord in C major (keyFifths=0,
/// Ionian).  degree: 0=I, 1=ii, 2=iii, 3=IV, 4=V, 5=vi, 6=viio.
ChordAnalysisResult diatonicResult(int degree, ChordQuality quality)
{
    static const int kIonianIntervals[7] = { 0, 2, 4, 5, 7, 9, 11 };
    ChordAnalysisResult r;
    r.identity.rootPc = (kIonianIntervals[degree] + 0) % 12; // C major tonic = 0
    r.identity.bassPc = r.identity.rootPc;
    r.identity.quality = quality;
    r.function.degree = degree;
    r.function.diatonicToKey = true;
    r.function.keyTonicPc = 0;   // C
    r.function.keyMode = KeySigMode::Ionian;
    return r;
}

/// Build a KeyModeAnalysisResult for a given key/mode and confidence.
KeyModeAnalysisResult keyResult(int fifths, KeySigMode mode, double confidence)
{
    KeyModeAnalysisResult km;
    km.keySignatureFifths = fifths;
    km.mode = mode;
    km.normalizedConfidence = confidence;
    return km;
}

/// Build a minimal HarmonicRegion at the given tick range.
HarmonicRegion region(int startTick, int endTick,
                      const ChordAnalysisResult& chord,
                      const KeyModeAnalysisResult& km)
{
    HarmonicRegion r;
    r.startTick = startTick;
    r.endTick = endTick;
    r.chordResult = chord;
    r.keyModeResult = km;
    return r;
}

// Assertive confidence — above the 0.8 threshold.
constexpr double kHigh = 0.95;
// Low confidence — below the 0.8 threshold.
constexpr double kLow  = 0.40;

} // namespace

// ── detectCadences — PAC within selection ────────────────────────────────────

TEST(CadenceDetection, PAC_BothInSelection)
{
    // V → I in C major, both regions inside the selection.
    const auto cMajor = keyResult(0, KeySigMode::Ionian, kHigh);
    std::vector<HarmonicRegion> regions = {
        region(0,      4 * kQ, diatonicResult(4, ChordQuality::Major), cMajor),  // V
        region(4 * kQ, 8 * kQ, diatonicResult(0, ChordQuality::Major), cMajor),  // I
    };

    const auto markers = detectCadences(regions, /*selectionCount=*/2);

    ASSERT_EQ(markers.size(), 1u);
    EXPECT_EQ(markers[0].label, "PAC");
    // Resolution chord (I) is at tick 4*kQ.
    EXPECT_EQ(markers[0].tick, 4 * kQ);
}

// ── detectCadences — PAC at selection end (lookahead) ────────────────────────

TEST(CadenceDetection, PAC_ResolutionInLookahead)
{
    // V is the last in-selection region; I is a lookahead region.
    // The label must be placed at the V tick (within the selection).
    const auto cMajor = keyResult(0, KeySigMode::Ionian, kHigh);
    std::vector<HarmonicRegion> regions = {
        region(0,      4 * kQ, diatonicResult(4, ChordQuality::Major), cMajor),  // V  (in selection)
        region(4 * kQ, 8 * kQ, diatonicResult(0, ChordQuality::Major), cMajor),  // I  (lookahead)
    };

    // Only region[0] is inside the selection.
    const auto markers = detectCadences(regions, /*selectionCount=*/1);

    ASSERT_EQ(markers.size(), 1u);
    EXPECT_EQ(markers[0].label, "PAC");
    // Written at V tick (0), not at I tick (4*kQ), because I is outside selection.
    EXPECT_EQ(markers[0].tick, 0);
}

// ── detectCadences — viio → I is also PAC ────────────────────────────────────

TEST(CadenceDetection, PAC_LeadingToneDiminished)
{
    const auto cMajor = keyResult(0, KeySigMode::Ionian, kHigh);
    std::vector<HarmonicRegion> regions = {
        region(0,      4 * kQ, diatonicResult(6, ChordQuality::Diminished), cMajor),  // viio
        region(4 * kQ, 8 * kQ, diatonicResult(0, ChordQuality::Major),      cMajor),  // I
    };

    const auto markers = detectCadences(regions, 2);
    ASSERT_EQ(markers.size(), 1u);
    EXPECT_EQ(markers[0].label, "PAC");
}

// ── detectCadences — PC (plagal) ─────────────────────────────────────────────

TEST(CadenceDetection, PC_PlagalCadence)
{
    const auto cMajor = keyResult(0, KeySigMode::Ionian, kHigh);
    std::vector<HarmonicRegion> regions = {
        region(0,      4 * kQ, diatonicResult(3, ChordQuality::Major), cMajor),  // IV
        region(4 * kQ, 8 * kQ, diatonicResult(0, ChordQuality::Major), cMajor),  // I
    };

    const auto markers = detectCadences(regions, 2);
    ASSERT_EQ(markers.size(), 1u);
    EXPECT_EQ(markers[0].label, "PC");
}

// ── detectCadences — DC (deceptive) ──────────────────────────────────────────

TEST(CadenceDetection, DC_DeceptiveCadence)
{
    const auto cMajor = keyResult(0, KeySigMode::Ionian, kHigh);
    std::vector<HarmonicRegion> regions = {
        region(0,      4 * kQ, diatonicResult(4, ChordQuality::Major), cMajor),  // V
        region(4 * kQ, 8 * kQ, diatonicResult(5, ChordQuality::Minor), cMajor),  // vi
    };

    const auto markers = detectCadences(regions, 2);
    ASSERT_EQ(markers.size(), 1u);
    EXPECT_EQ(markers[0].label, "DC");
}

// ── detectCadences — HC (half cadence) ───────────────────────────────────────

TEST(CadenceDetection, HC_LastRegionIsDominant)
{
    const auto cMajor = keyResult(0, KeySigMode::Ionian, kHigh);
    std::vector<HarmonicRegion> regions = {
        region(0,      4 * kQ, diatonicResult(0, ChordQuality::Major), cMajor),  // I
        region(4 * kQ, 8 * kQ, diatonicResult(4, ChordQuality::Major), cMajor),  // V
    };

    // Two regions, both in selection; last is V.
    const auto markers = detectCadences(regions, 2);
    // No PAC (V does not precede I) — we get HC at tick 4*kQ.
    ASSERT_EQ(markers.size(), 1u);
    EXPECT_EQ(markers[0].label, "HC");
    EXPECT_EQ(markers[0].tick, 4 * kQ);
}

// ── detectCadences — no cadence across key change ────────────────────────────

TEST(CadenceDetection, NoCadence_AcrossKeyChange)
{
    // The two regions are in different keys — no cadence should be detected.
    const auto cMajor = keyResult(0, KeySigMode::Ionian, kHigh);
    const auto gMajor = keyResult(1, KeySigMode::Ionian, kHigh);
    std::vector<HarmonicRegion> regions = {
        region(0,      4 * kQ, diatonicResult(4, ChordQuality::Major), cMajor),  // V in C
        region(4 * kQ, 8 * kQ, diatonicResult(0, ChordQuality::Major), gMajor),  // I in G (different key)
    };

    const auto markers = detectCadences(regions, 2);
    // No PAC because the key changes between the two regions.
    // V in C is not the last in-selection region... wait, it IS the first,
    // and I in G is the last.  V in C as last → HC check: degree 4 in cMajor
    // but regions[1] is the last (degree 0 in G major, not 4) → no HC.
    // No markers expected.
    EXPECT_TRUE(markers.empty());
}

// ── detectCadences — low confidence regions are ignored ──────────────────────

TEST(CadenceDetection, NoCadence_LowConfidence)
{
    const auto cMajorLow  = keyResult(0, KeySigMode::Ionian, kLow);
    std::vector<HarmonicRegion> regions = {
        region(0,      4 * kQ, diatonicResult(4, ChordQuality::Major), cMajorLow),
        region(4 * kQ, 8 * kQ, diatonicResult(0, ChordQuality::Major), cMajorLow),
    };

    const auto markers = detectCadences(regions, 2);
    EXPECT_TRUE(markers.empty());
}

// ── detectPivotChords — pivot in middle of selection ─────────────────────────

TEST(PivotDetection, PivotInMiddleOfSelection)
{
    // Four regions in selection + two lookahead:
    //   [0..1] C major (I, ii),  [2..3] G major (IV→V in G = I→ii in G's scale)
    //   Pivot candidate: ii in C = pc 2 (D), which is vi in G (also diatonic).
    //
    // C major scale: 0,2,4,5,7,9,11  — degree 1 (ii) rootPc = 2 (D)
    // G major scale: 0,2,4,5,7,9,11 shifted by 7 = 7,9,11,0,2,4,6
    //   — D (pc 2) is degree 4 (V) in G major? No. G=7,A=9,B=11,C=0,D=2 → D is degree 4 in G.
    // So the pivot chord is "ii in C → V in G".

    const auto cMajor = keyResult(0, KeySigMode::Ionian, kHigh);
    const auto gMajor = keyResult(1, KeySigMode::Ionian, kHigh);

    // Build C major ii chord (rootPc = 2, degree 1)
    ChordAnalysisResult cMajorII;
    cMajorII.identity.rootPc = 2;  // D
    cMajorII.identity.quality = ChordQuality::Minor;
    cMajorII.function.degree = 1;
    cMajorII.function.diatonicToKey = true;
    cMajorII.function.keyTonicPc = 0;
    cMajorII.function.keyMode = KeySigMode::Ionian;

    // G major I chord (rootPc = 7, degree 0)
    ChordAnalysisResult gMajorI;
    gMajorI.identity.rootPc = 7;  // G
    gMajorI.identity.quality = ChordQuality::Major;
    gMajorI.function.degree = 0;
    gMajorI.function.diatonicToKey = true;
    gMajorI.function.keyTonicPc = 7;
    gMajorI.function.keyMode = KeySigMode::Ionian;

    std::vector<HarmonicRegion> regions = {
        region(0,          kQ, diatonicResult(0, ChordQuality::Major), cMajor),  // I in C
        region(kQ,      2 * kQ, cMajorII,                              cMajor),  // ii in C (= pivot candidate)
        region(2 * kQ,  3 * kQ, gMajorI,                               gMajor),  // I in G (key boundary)
        region(3 * kQ,  4 * kQ, diatonicResult(4, ChordQuality::Major), gMajor), // V in G (confirming)
    };
    // All 4 regions are in selection; no lookahead needed since confirming is in selection.

    const auto pivots = detectPivotChords(regions, /*selectionCount=*/4);

    ASSERT_EQ(pivots.size(), 1u);
    // Pivot chord is the ii in C (index 1, tick = kQ).
    EXPECT_EQ(pivots[0].tick, kQ);
    // Label: "ii" in C major → "V" in G major.
    EXPECT_NE(pivots[0].label.find("\u2192"), std::string::npos)
        << "Pivot label must contain right arrow";
    // Both sides should be non-empty (full label like "ii → V").
    EXPECT_FALSE(pivots[0].label.empty());
}

// ── detectPivotChords — pivot at selection end, confirmed by lookahead ────────

TEST(PivotDetection, PivotAtSelectionEnd_ConfirmedByLookahead)
{
    // Last in-selection region is the pivot candidate; confirming regions
    // are in the lookahead.
    const auto cMajor = keyResult(0, KeySigMode::Ionian, kHigh);
    const auto gMajor = keyResult(1, KeySigMode::Ionian, kHigh);

    // ii in C = D minor (rootPc = 2)
    ChordAnalysisResult cMajorII;
    cMajorII.identity.rootPc = 2;
    cMajorII.identity.quality = ChordQuality::Minor;
    cMajorII.function.degree = 1;
    cMajorII.function.diatonicToKey = true;
    cMajorII.function.keyTonicPc = 0;
    cMajorII.function.keyMode = KeySigMode::Ionian;

    ChordAnalysisResult gMajorI;
    gMajorI.identity.rootPc = 7;
    gMajorI.identity.quality = ChordQuality::Major;
    gMajorI.function.degree = 0;
    gMajorI.function.diatonicToKey = true;
    gMajorI.function.keyTonicPc = 7;
    gMajorI.function.keyMode = KeySigMode::Ionian;

    std::vector<HarmonicRegion> regions = {
        region(0,          kQ, diatonicResult(0, ChordQuality::Major), cMajor),  // I in C  (in selection)
        region(kQ,      2 * kQ, cMajorII,                              cMajor),  // ii in C (in selection, pivot candidate)
        region(2 * kQ,  3 * kQ, gMajorI,                               gMajor),  // I in G  (LOOKAHEAD, key boundary)
        region(3 * kQ,  4 * kQ, diatonicResult(4, ChordQuality::Major), gMajor), // V in G  (LOOKAHEAD, confirming)
    };
    // Only regions[0..1] are inside the selection.
    const auto pivots = detectPivotChords(regions, /*selectionCount=*/2);

    ASSERT_EQ(pivots.size(), 1u);
    EXPECT_EQ(pivots[0].tick, kQ);  // ii in C is at tick kQ
    EXPECT_NE(pivots[0].label.find("\u2192"), std::string::npos);
}

// ── detectPivotChords — pivot suppressed when new key unconfirmed ─────────────

TEST(PivotDetection, PivotSuppressed_NewKeyUnconfirmed)
{
    // Same setup but lookahead shows the "G major" region only once — no second
    // assertive G-major region to confirm the new key.
    const auto cMajor = keyResult(0, KeySigMode::Ionian, kHigh);
    const auto gMajor = keyResult(1, KeySigMode::Ionian, kHigh);

    ChordAnalysisResult cMajorII;
    cMajorII.identity.rootPc = 2;
    cMajorII.identity.quality = ChordQuality::Minor;
    cMajorII.function.degree = 1;
    cMajorII.function.diatonicToKey = true;
    cMajorII.function.keyTonicPc = 0;
    cMajorII.function.keyMode = KeySigMode::Ionian;

    ChordAnalysisResult gMajorI;
    gMajorI.identity.rootPc = 7;
    gMajorI.identity.quality = ChordQuality::Major;
    gMajorI.function.degree = 0;
    gMajorI.function.diatonicToKey = true;
    gMajorI.function.keyTonicPc = 7;
    gMajorI.function.keyMode = KeySigMode::Ionian;

    // Only ONE G-major region in lookahead — detection requires TWO assertive
    // G-major regions (the transition region + at least one confirming region).
    std::vector<HarmonicRegion> regions = {
        region(0,      kQ, diatonicResult(0, ChordQuality::Major), cMajor),  // I in C (in selection)
        region(kQ,  2 * kQ, cMajorII,                              cMajor),  // ii in C (in selection, pivot candidate)
        region(2 * kQ, 3 * kQ, gMajorI,                            gMajor),  // I in G (LOOKAHEAD, boundary — but no confirming region follows)
    };
    const auto pivots = detectPivotChords(regions, /*selectionCount=*/2);

    // New key is NOT confirmed (only one G-major region, no second assertive
    // G-major region within lookahead) → pivot suppressed.
    EXPECT_TRUE(pivots.empty());
}

// ── detectPivotChords — no false pivot with stable key ───────────────────────

TEST(PivotDetection, NoPivot_StableKey)
{
    // Four regions all in C major — no modulation, no pivot.
    const auto cMajor = keyResult(0, KeySigMode::Ionian, kHigh);
    std::vector<HarmonicRegion> regions = {
        region(0,          kQ, diatonicResult(0, ChordQuality::Major), cMajor),
        region(kQ,      2 * kQ, diatonicResult(4, ChordQuality::Major), cMajor),
        region(2 * kQ,  3 * kQ, diatonicResult(3, ChordQuality::Major), cMajor),
        region(3 * kQ,  4 * kQ, diatonicResult(0, ChordQuality::Major), cMajor),
    };

    const auto pivots = detectPivotChords(regions, 4);
    EXPECT_TRUE(pivots.empty());
}

// ── Pivot format — new format must not contain "pivot:" prefix ────────────────

TEST(PivotDetection, PivotLabel_NoOldFormatPrefix)
{
    // Verify that the new vi → ii format does not include the old "pivot: " prefix.
    const auto cMajor = keyResult(0, KeySigMode::Ionian, kHigh);
    const auto gMajor = keyResult(1, KeySigMode::Ionian, kHigh);

    ChordAnalysisResult cMajorII;
    cMajorII.identity.rootPc = 2;
    cMajorII.identity.quality = ChordQuality::Minor;
    cMajorII.function.degree = 1;
    cMajorII.function.diatonicToKey = true;
    cMajorII.function.keyTonicPc = 0;
    cMajorII.function.keyMode = KeySigMode::Ionian;

    ChordAnalysisResult gMajorI;
    gMajorI.identity.rootPc = 7;
    gMajorI.identity.quality = ChordQuality::Major;
    gMajorI.function.degree = 0;
    gMajorI.function.diatonicToKey = true;
    gMajorI.function.keyTonicPc = 7;
    gMajorI.function.keyMode = KeySigMode::Ionian;

    ChordAnalysisResult gMajorV;
    gMajorV.identity.rootPc = 2;  // D = V in G major (degree 4)
    gMajorV.identity.quality = ChordQuality::Major;
    gMajorV.function.degree = 4;
    gMajorV.function.diatonicToKey = true;
    gMajorV.function.keyTonicPc = 7;
    gMajorV.function.keyMode = KeySigMode::Ionian;

    std::vector<HarmonicRegion> regions = {
        region(0,          kQ, diatonicResult(0, ChordQuality::Major), cMajor),
        region(kQ,      2 * kQ, cMajorII,                              cMajor),
        region(2 * kQ,  3 * kQ, gMajorI,                               gMajor),
        region(3 * kQ,  4 * kQ, gMajorV,                               gMajor),
    };

    const auto pivots = detectPivotChords(regions, 4);
    ASSERT_EQ(pivots.size(), 1u);

    const std::string& label = pivots[0].label;
    // Must NOT start with "pivot:"
    EXPECT_FALSE(label.rfind("pivot:", 0) == 0)
        << "Old pivot prefix found: " << label;
    // Must NOT contain "in C major" or similar key-name context
    EXPECT_EQ(label.find(" in "), std::string::npos)
        << "Old key-context found in pivot label: " << label;
    // Must contain U+2192 right arrow
    EXPECT_NE(label.find("\u2192"), std::string::npos)
        << "Right arrow missing from pivot label: " << label;
}
