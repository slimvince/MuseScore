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

// grouping_tests.cpp — Architectural Layer 6 (GROUPING), dormant build.
//
// Oracle-asserted against §5.1–§5.5 of cowork_layer6_grouping_design.md (SIGNED):
// the flat punctuation-span partition (totality/flatness/interlock + the §5.1-a
// codetta refinement + the edge-provenance/extension-cue amendment), the independent
// key-area partition (D5 mid-span key change), the U2 key-area confidence (monotone,
// [0,1]), the §5.3 cadence-to-span alignment (window in/out + the internal tag), the
// §5.4 residual pass-through, and the §5.5 empty-schema case. Assembly, not detection.

#include <gtest/gtest.h>

#include "composing/analysis/grouping/groupinglayer.h"

using namespace mu::composing::analysis;
using namespace mu::composing::analysis::grouping;

namespace {

GroupingUnit unit(int startTick, int endTick, int tonicPc, bool minor = false,
                  double keyConf = 0.5, bool openMark = false)
{
    GroupingUnit u;
    u.startTick = startTick;
    u.endTick = endTick;
    u.localTonicPc = tonicPc;
    u.localMinorMode = minor;
    u.keyConfidence = keyConf;
    u.openMark = openMark;
    return u;
}

BoundaryInput bnd(int tick, double strength = 1.0)
{
    BoundaryInput b;
    b.tick = tick;
    b.strength = strength;
    return b;
}

FunctionalCadence cad(int arrivalTick, double tonicVote = 1.0,
                      FunctionalCadenceType type = FunctionalCadenceType::PerfectAuthentic)
{
    FunctionalCadence c;
    c.type = type;
    c.approachTick = arrivalTick - 240;
    c.arrivalTick = arrivalTick;
    c.tonicVote = tonicVote;
    return c;
}

// A whole-score analysed span (true score edges — NOT selection clips).
AnalyzedSpan scoreSpan(int startTick, int endTick)
{
    AnalyzedSpan s;
    s.startTick = startTick;
    s.endTick = endTick;
    s.startIsSelectionEdge = false;
    s.endIsSelectionEdge = false;
    return s;
}

// ── §5.1 the flat partition: totality + flatness ──────────────────────────────

TEST(GroupingLayer, PartitionIsTotalAndFlat)
{
    std::vector<GroupingUnit> units{ unit(0, 4000, 0) };
    std::vector<BoundaryInput> bs{ bnd(1000), bnd(2000), bnd(3000) };
    const GroupingLayerOutput g = assembleGrouping(units, bs, {}, scoreSpan(0, 4000));

    ASSERT_EQ(g.punctuationSpans.size(), 4u);
    // tiles [0,4000) with no gap / no overlap: each start == the previous end.
    EXPECT_EQ(g.punctuationSpans.front().startTick, 0);
    EXPECT_EQ(g.punctuationSpans.back().endTick, 4000);
    for (size_t i = 0; i < g.punctuationSpans.size(); ++i) {
        EXPECT_LT(g.punctuationSpans[i].startTick, g.punctuationSpans[i].endTick);
        if (i > 0) {
            EXPECT_EQ(g.punctuationSpans[i].startTick, g.punctuationSpans[i - 1].endTick);
        }
    }
    const int expectedEnds[] = { 1000, 2000, 3000, 4000 };
    for (size_t i = 0; i < 4; ++i) {
        EXPECT_EQ(g.punctuationSpans[i].endTick, expectedEnds[i]);
    }
}

// A boundary AT the analysed-span start/end is an edge marker, not an interior cut
// (no empty leading/trailing span).
TEST(GroupingLayer, BoundaryAtEdgeMakesNoEmptySpan)
{
    std::vector<GroupingUnit> units{ unit(0, 2000, 0) };
    std::vector<BoundaryInput> bs{ bnd(0), bnd(1000), bnd(2000) };
    const GroupingLayerOutput g = assembleGrouping(units, bs, {}, scoreSpan(0, 2000));
    ASSERT_EQ(g.punctuationSpans.size(), 2u);
    EXPECT_EQ(g.punctuationSpans[0].startTick, 0);
    EXPECT_EQ(g.punctuationSpans[0].endTick, 1000);
    EXPECT_EQ(g.punctuationSpans[1].endTick, 2000);
}

// ── §5.1 span interlock (`}{`): one boundary serves end-and-start, no gap ──────

TEST(GroupingLayer, SpanInterlockNoGap)
{
    std::vector<GroupingUnit> units{ unit(0, 4000, 0) };
    std::vector<BoundaryInput> bs{ bnd(2000) };
    const GroupingLayerOutput g = assembleGrouping(units, bs, {}, scoreSpan(0, 4000));
    ASSERT_EQ(g.punctuationSpans.size(), 2u);
    EXPECT_EQ(g.punctuationSpans[0].endTick, 2000);
    EXPECT_EQ(g.punctuationSpans[1].startTick, 2000);   // shared tick, no gap
}

// ── §5.1-a codetta refinement: strong-then-weak → weak peak absorbed ──────────

TEST(GroupingLayer, CodettaDefaultInertKeepsBothPeaks)
{
    std::vector<GroupingUnit> units{ unit(0, 4000, 0) };
    std::vector<BoundaryInput> bs{ bnd(1000, 1.0), bnd(1100, 0.2), bnd(3000, 1.0) };
    // default params: codettaWindowTicks == 0 → INERT, both peaks are cuts.
    const GroupingLayerOutput g = assembleGrouping(units, bs, {}, scoreSpan(0, 4000));
    ASSERT_EQ(g.punctuationSpans.size(), 4u);   // [0,1000)[1000,1100)[1100,3000)[3000,4000)
    EXPECT_EQ(g.punctuationSpans[1].startTick, 1000);
    EXPECT_EQ(g.punctuationSpans[1].endTick, 1100);
    for (const auto& ps : g.punctuationSpans) {
        EXPECT_EQ(ps.codettaEndTick, -1);
    }
}

TEST(GroupingLayer, CodettaRefinementAbsorbsWeakPeak)
{
    std::vector<GroupingUnit> units{ unit(0, 4000, 0) };
    std::vector<BoundaryInput> bs{ bnd(1000, 1.0), bnd(1100, 0.2), bnd(3000, 1.0) };
    GroupingParams p;
    p.codettaWindowTicks = 200;   // 1100-1000 = 100 <= 200, strong(1.0) > weak(0.2)
    const GroupingLayerOutput g = assembleGrouping(units, bs, {}, scoreSpan(0, 4000), p);

    // The weak peak 1100 is suppressed: [0,1000)[1000,3000)[3000,4000).
    ASSERT_EQ(g.punctuationSpans.size(), 3u);
    EXPECT_EQ(g.punctuationSpans[0].endTick, 1000);
    EXPECT_EQ(g.punctuationSpans[0].structuralEndTick, 1000);
    EXPECT_EQ(g.punctuationSpans[0].codettaEndTick, 1100);   // codetta [1000,1100)
    EXPECT_EQ(g.punctuationSpans[1].startTick, 1000);
    EXPECT_EQ(g.punctuationSpans[1].endTick, 3000);
}

// A weak-then-strong pair (wrong order) does NOT fire the refinement.
TEST(GroupingLayer, CodettaDoesNotFireWeakThenStrong)
{
    std::vector<GroupingUnit> units{ unit(0, 4000, 0) };
    std::vector<BoundaryInput> bs{ bnd(1000, 0.2), bnd(1100, 1.0) };
    GroupingParams p;
    p.codettaWindowTicks = 200;
    const GroupingLayerOutput g = assembleGrouping(units, bs, {}, scoreSpan(0, 4000), p);
    ASSERT_EQ(g.punctuationSpans.size(), 3u);   // both kept
    EXPECT_EQ(g.punctuationSpans[0].codettaEndTick, -1);
}

// ── §5.1-amendment: edge provenance + extension cue ───────────────────────────

TEST(GroupingLayer, ClippedSelectionEdgeAndExtensionCue)
{
    std::vector<GroupingUnit> units{ unit(500, 3500, 0) };
    std::vector<BoundaryInput> bs{ bnd(2000) };
    AnalyzedSpan s;
    s.startTick = 500; s.endTick = 3500;
    s.startIsSelectionEdge = true;    // artificial clips at BOTH edges
    s.endIsSelectionEdge = true;
    const GroupingLayerOutput g = assembleGrouping(units, bs, {}, s);

    ASSERT_EQ(g.punctuationSpans.size(), 2u);
    EXPECT_TRUE(g.punctuationSpans.front().clippedAtStart);
    EXPECT_FALSE(g.punctuationSpans.front().clippedAtEnd);
    EXPECT_TRUE(g.punctuationSpans.back().clippedAtEnd);
    // extension cue: last span reaches the selection END edge, no closing boundary, no cadence.
    EXPECT_TRUE(g.punctuationSpans.back().extensionCue);
}

TEST(GroupingLayer, ScoreBoundaryIsNotClippedNoExtensionCue)
{
    std::vector<GroupingUnit> units{ unit(0, 4000, 0) };
    std::vector<BoundaryInput> bs{ bnd(2000) };
    const GroupingLayerOutput g = assembleGrouping(units, bs, {}, scoreSpan(0, 4000));
    for (const auto& ps : g.punctuationSpans) {
        EXPECT_FALSE(ps.clippedAtStart);
        EXPECT_FALSE(ps.clippedAtEnd);
        EXPECT_FALSE(ps.extensionCue);   // a true score edge is never clipped/extension-cued
    }
}

// An extension cue must NOT fire when the clipped edge span closes WITH a cadence.
TEST(GroupingLayer, NoExtensionCueWhenClippedEdgeHasCadence)
{
    std::vector<GroupingUnit> units{ unit(0, 2000, 0) };
    std::vector<BoundaryInput> bs{};   // no interior boundary → one span [0,2000)
    AnalyzedSpan s = scoreSpan(0, 2000);
    s.endIsSelectionEdge = true;
    std::vector<FunctionalCadence> cs{ cad(2000) };   // arrival at the selection end
    const GroupingLayerOutput g = assembleGrouping(units, bs, cs, s);
    ASSERT_EQ(g.punctuationSpans.size(), 1u);
    EXPECT_TRUE(g.punctuationSpans[0].clippedAtEnd);
    EXPECT_GE(g.punctuationSpans[0].closingCadenceIndex, 0);
    EXPECT_FALSE(g.punctuationSpans[0].extensionCue);   // closed by a cadence → not incomplete
}

// ── §5.2 key-areas: independent, mid-punctuation-span key change (D5) ──────────

TEST(GroupingLayer, KeyAreaBoundaryFallsMidPunctuationSpan)
{
    // ONE punctuation-span [0,4000) (no boundaries), but the local key changes at 2000.
    std::vector<GroupingUnit> units{
        unit(0, 1000, 0), unit(1000, 2000, 0),      // C major
        unit(2000, 3000, 7), unit(3000, 4000, 7),   // G major
    };
    const GroupingLayerOutput g = assembleGrouping(units, {}, {}, scoreSpan(0, 4000));

    ASSERT_EQ(g.punctuationSpans.size(), 1u);        // one flat span
    ASSERT_EQ(g.keyAreas.size(), 2u);                // two independent key-areas
    EXPECT_EQ(g.keyAreas[0].startTick, 0);
    EXPECT_EQ(g.keyAreas[0].endTick, 2000);
    EXPECT_EQ(g.keyAreas[0].localTonicPc, 0);
    EXPECT_EQ(g.keyAreas[1].startTick, 2000);        // key-area boundary mid-span
    EXPECT_EQ(g.keyAreas[1].endTick, 4000);
    EXPECT_EQ(g.keyAreas[1].localTonicPc, 7);
    // the key-area boundary (2000) is NOT a punctuation-span boundary (independence).
    EXPECT_NE(g.keyAreas[1].startTick, g.punctuationSpans[0].endTick);
}

TEST(GroupingLayer, KeyAreaSplitsOnModeChangeSameTonic)
{
    std::vector<GroupingUnit> units{
        unit(0, 1000, 0, /*minor*/ false), unit(1000, 2000, 0, /*minor*/ true),
    };
    const GroupingLayerOutput g = assembleGrouping(units, {}, {}, scoreSpan(0, 2000));
    ASSERT_EQ(g.keyAreas.size(), 2u);
    EXPECT_FALSE(g.keyAreas[0].localMinorMode);
    EXPECT_TRUE(g.keyAreas[1].localMinorMode);
}

// ── §5.2 U2 confidence: bounded [0,1] and monotone-non-decreasing ─────────────

TEST(GroupingLayer, KeyAreaConfidenceBoundedAndMonotone)
{
    std::vector<GroupingUnit> lo{ unit(0, 1000, 0, false, 0.2), unit(1000, 2000, 0, false, 0.4) };
    std::vector<GroupingUnit> hi{ unit(0, 1000, 0, false, 0.9), unit(1000, 2000, 0, false, 0.4) };
    const double clo = assembleGrouping(lo, {}, {}, scoreSpan(0, 2000)).keyAreas[0].confidence;
    const double chi = assembleGrouping(hi, {}, {}, scoreSpan(0, 2000)).keyAreas[0].confidence;
    EXPECT_GE(clo, 0.0); EXPECT_LE(clo, 1.0);
    EXPECT_GE(chi, 0.0); EXPECT_LE(chi, 1.0);
    EXPECT_GE(chi, clo);   // raising one unit's confidence never lowers the area confidence
    // out-of-range inputs are clamped, not propagated.
    std::vector<GroupingUnit> over{ unit(0, 1000, 0, false, 5.0) };
    EXPECT_LE(assembleGrouping(over, {}, {}, scoreSpan(0, 1000)).keyAreas[0].confidence, 1.0);
}

// ── §5.3 cadence alignment: window in / out + the internal tag ─────────────────

TEST(GroupingLayer, CadenceWithinWindowClosesSpan)
{
    std::vector<GroupingUnit> units{ unit(0, 4000, 0) };
    std::vector<BoundaryInput> bs{ bnd(2000) };
    std::vector<FunctionalCadence> cs{ cad(1900) };   // arrival 1900, boundary 2000, gap 100 <= 480
    const GroupingLayerOutput g = assembleGrouping(units, bs, cs, scoreSpan(0, 4000));
    ASSERT_EQ(g.cadenceAlignments.size(), 1u);
    EXPECT_EQ(g.cadenceAlignments[0].kind, CadenceAlignmentKind::ClosesSpan);
    EXPECT_EQ(g.cadenceAlignments[0].punctuationSpanIndex, 0);
    EXPECT_EQ(g.punctuationSpans[0].closingCadenceIndex, 0);
    EXPECT_EQ(g.punctuationSpans[1].closingCadenceIndex, -1);   // ends without a cadence — valid
}

TEST(GroupingLayer, CadenceOutsideWindowIsInternal)
{
    std::vector<GroupingUnit> units{ unit(0, 4000, 0) };
    std::vector<BoundaryInput> bs{ bnd(2000) };
    std::vector<FunctionalCadence> cs{ cad(1000) };   // nearest boundary 2000, gap 1000 > 480
    const GroupingLayerOutput g = assembleGrouping(units, bs, cs, scoreSpan(0, 4000));
    ASSERT_EQ(g.cadenceAlignments.size(), 1u);
    EXPECT_EQ(g.cadenceAlignments[0].kind, CadenceAlignmentKind::Internal);   // surfaced, not snapped
    EXPECT_EQ(g.cadenceAlignments[0].punctuationSpanIndex, -1);
    EXPECT_EQ(g.punctuationSpans[0].closingCadenceIndex, -1);
    EXPECT_EQ(g.punctuationSpans[1].closingCadenceIndex, -1);
}

// exact window edge (gap == window) is IN; gap == window+1 is OUT.
TEST(GroupingLayer, CadenceWindowEdgeInclusive)
{
    std::vector<GroupingUnit> units{ unit(0, 2000, 0) };
    std::vector<BoundaryInput> bs{};
    {
        std::vector<FunctionalCadence> cs{ cad(2000 - 480) };   // gap exactly 480
        const auto g = assembleGrouping(units, bs, cs, scoreSpan(0, 2000));
        EXPECT_EQ(g.cadenceAlignments[0].kind, CadenceAlignmentKind::ClosesSpan);
    }
    {
        std::vector<FunctionalCadence> cs{ cad(2000 - 481) };   // gap 481
        const auto g = assembleGrouping(units, bs, cs, scoreSpan(0, 2000));
        EXPECT_EQ(g.cadenceAlignments[0].kind, CadenceAlignmentKind::Internal);
    }
}

// ── §5.4 residual pass-through: an open mark surfaces on its containing groups ──

TEST(GroupingLayer, OpenMarkSurfacesOnContainingGroups)
{
    std::vector<GroupingUnit> units{
        unit(0, 1000, 0, false, 0.5, /*openMark*/ false),
        unit(1000, 2000, 0, false, 0.5, /*openMark*/ true),
        unit(2000, 3000, 0, false, 0.5, /*openMark*/ false),
    };
    std::vector<BoundaryInput> bs{ bnd(2000) };   // spans [0,2000) [2000,3000)
    const GroupingLayerOutput g = assembleGrouping(units, bs, {}, scoreSpan(0, 3000));
    ASSERT_EQ(g.punctuationSpans.size(), 2u);
    EXPECT_TRUE(g.punctuationSpans[0].carriesOpenMark);    // contains the open-marked unit
    EXPECT_FALSE(g.punctuationSpans[1].carriesOpenMark);   // all confident
    ASSERT_EQ(g.keyAreas.size(), 1u);
    EXPECT_TRUE(g.keyAreas[0].carriesOpenMark);
}

// ── §5.5 recognised-schema hosting: empty absent the consumer ──────────────────

TEST(GroupingLayer, SchemaSpansEmptyAbsentConsumer)
{
    std::vector<GroupingUnit> units{ unit(0, 2000, 0) };
    const GroupingLayerOutput g = assembleGrouping(units, {}, {}, scoreSpan(0, 2000));
    EXPECT_TRUE(g.schemaSpans.empty());
}

// A degenerate span yields empty grouping (no crash).
TEST(GroupingLayer, DegenerateSpanIsEmpty)
{
    const GroupingLayerOutput g = assembleGrouping({}, {}, {}, scoreSpan(1000, 1000));
    EXPECT_TRUE(g.punctuationSpans.empty());
    EXPECT_TRUE(g.keyAreas.empty());
}

} // namespace
