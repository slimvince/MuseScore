/*
 * SPDX-License-Identifier: GPL-3.0-only
 * MuseScore-Studio-CLA-applies
 *
 * MuseScore Studio
 * Music Composition & Notation
 *
 * Copyright (C) 2021 MuseScore Limited
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

// ── Notation composing bridge regression tests ───────────────────────────────
//
// Tests for:
//   addHarmonicAnnotationsToSelection  — writes and undoes STANDARD annotations
//   analyzeHarmonicContextAtTick       — returns valid key context at tick 0
//   prepareUserFacingHarmonicRegions   — returns ≥1 region with a valid root
//
// All tests use the tracked fixture:
//   notationcomposing_data/implode_sustained_support_each_beat.mscx

#include <gtest/gtest.h>

#include "modularity/ioc.h"

#include "composing/icomposinganalysisconfiguration.h"

#include "engraving/dom/harmony.h"
#include "engraving/dom/masterscore.h"
#include "engraving/dom/segment.h"

#include "engraving/editing/undo.h"
#include "engraving/tests/utils/scorerw.h"

#include "notation/internal/notationcomposingbridge.h"
#include "notation/internal/notationcomposingbridgehelpers.h"

using namespace mu::engraving;
using namespace mu::composing::analysis;

namespace {

std::shared_ptr<mu::composing::IComposingAnalysisConfiguration> analysisConfig()
{
    return muse::modularity::globalIoc()->resolve<mu::composing::IComposingAnalysisConfiguration>("composing");
}

int countHarmonyAnnotationsOnTrack(MasterScore* score, track_idx_t track)
{
    int count = 0;
    for (Segment* seg = score->firstSegment(SegmentType::ChordRest); seg;
         seg = seg->next1(SegmentType::ChordRest)) {
        for (EngravingItem* ann : seg->annotations()) {
            if (ann && ann->isHarmony() && ann->track() == track) {
                ++count;
            }
        }
    }
    return count;
}

} // namespace

class Notation_ComposingBridgeTests : public ::testing::Test
{
};

// ── Test 1: addHarmonicAnnotationsToSelection ─────────────────────────────────

TEST_F(Notation_ComposingBridgeTests, AddHarmonicAnnotationsToSelectionWritesAndUndoes)
{
    auto analysis = analysisConfig();
    ASSERT_TRUE(analysis);
    analysis->setUseRegionalAccumulation(true);

    MasterScore* score = ScoreRW::readScore(u"implode_sustained_support_each_beat.mscx");
    ASSERT_TRUE(score);
    ASSERT_GE(score->nstaves(), 1u);

    // Select staves 0–1 so the chord-track priority rule does NOT apply and
    // annotations land on the source staves.
    Segment* startSeg = score->firstSegment(SegmentType::ChordRest);
    ASSERT_TRUE(startSeg);
    const size_t selectionStaves = std::min(score->nstaves(), static_cast<size_t>(2));
    score->selection().setRange(startSeg, nullptr, 0, static_cast<int>(selectionStaves));
    ASSERT_TRUE(score->selection().isRange());

    const track_idx_t track0 = 0;
    const int annotationsBefore = countHarmonyAnnotationsOnTrack(score, track0);

    mu::notation::addHarmonicAnnotationsToSelection(score, /*writeChordSymbols=*/true,
                                                    /*writeRomanNumerals=*/false,
                                                    /*writeNashvilleNumbers=*/false);

    const int annotationsAfter = countHarmonyAnnotationsOnTrack(score, track0);
    EXPECT_GT(annotationsAfter, annotationsBefore)
        << "addHarmonicAnnotationsToSelection wrote no annotations to track 0";

    // At least one annotation must be STANDARD type.
    bool hasStandard = false;
    for (Segment* seg = score->firstSegment(SegmentType::ChordRest); seg && !hasStandard;
         seg = seg->next1(SegmentType::ChordRest)) {
        for (EngravingItem* ann : seg->annotations()) {
            if (ann && ann->isHarmony() && ann->track() == track0
                && toHarmony(ann)->harmonyType() == HarmonyType::STANDARD) {
                hasStandard = true;
            }
        }
    }
    EXPECT_TRUE(hasStandard) << "no STANDARD-type harmony found on track 0 after annotation";

    // Undo: all written annotations must be removed.
    score->undoStack()->undo(nullptr);
    const int annotationsAfterUndo = countHarmonyAnnotationsOnTrack(score, track0);
    EXPECT_EQ(annotationsAfterUndo, annotationsBefore)
        << "undo did not fully remove annotations: before=" << annotationsBefore
        << " afterUndo=" << annotationsAfterUndo;

    delete score;
}

// ── Test 2: analyzeHarmonicContextAtTick ─────────────────────────────────────

TEST_F(Notation_ComposingBridgeTests, AnalyzeHarmonicContextAtTickReturnValidContext)
{
    auto analysis = analysisConfig();
    ASSERT_TRUE(analysis);
    analysis->setUseRegionalAccumulation(true);

    MasterScore* score = ScoreRW::readScore(u"implode_sustained_support_each_beat.mscx");
    ASSERT_TRUE(score);

    const Fraction tick0 = Fraction(0, 1);
    const mu::notation::NoteHarmonicContext ctx
        = mu::notation::analyzeHarmonicContextAtTick(score, tick0, /*preferredStaffIdx=*/0);

    // The result must contain at least one chord analysis candidate.
    EXPECT_FALSE(ctx.chordResults.empty())
        << "analyzeHarmonicContextAtTick returned no chord results at tick 0";

    // keyConfidence must be in [0, 1].
    EXPECT_GE(ctx.keyConfidence, 0.0);
    EXPECT_LE(ctx.keyConfidence, 1.0);

    // keyFifths must be in the range [-7, 7] (valid key signature).
    EXPECT_GE(ctx.keyFifths, -7);
    EXPECT_LE(ctx.keyFifths, 7);

    // The top chord candidate must have a valid root pitch class (0–11).
    if (!ctx.chordResults.empty()) {
        EXPECT_GE(ctx.chordResults.front().identity.rootPc, 0);
        EXPECT_LE(ctx.chordResults.front().identity.rootPc, 11);
    }

    delete score;
}

// ── Test 3: prepareUserFacingHarmonicRegions ──────────────────────────────────

TEST_F(Notation_ComposingBridgeTests, PrepareUserFacingHarmonicRegionsReturnsRegions)
{
    auto analysis = analysisConfig();
    ASSERT_TRUE(analysis);
    analysis->setUseRegionalAccumulation(true);

    MasterScore* score = ScoreRW::readScore(u"implode_sustained_support_each_beat.mscx");
    ASSERT_TRUE(score);

    const Fraction startTick = Fraction(0, 1);
    const Fraction endTick   = score->lastMeasure()
                               ? score->lastMeasure()->endTick()
                               : Fraction(16, 4);   // fallback: 4 measures of 4/4

    const std::vector<mu::composing::analysis::HarmonicRegion> regions
        = mu::notation::internal::prepareUserFacingHarmonicRegions(
            score, startTick, endTick, /*excludeStaves=*/{});

    EXPECT_GE(regions.size(), 1u)
        << "prepareUserFacingHarmonicRegions returned no regions";

    for (const auto& region : regions) {
        // Every region must carry a valid root pitch class (0–11).
        EXPECT_GE(region.chordResult.identity.rootPc, 0)
            << "region has rootPc < 0";
        EXPECT_LE(region.chordResult.identity.rootPc, 11)
            << "region has rootPc > 11";

        // Region boundaries must be non-negative and ordered.
        // HarmonicRegion stores raw integer ticks (not Fraction).
        EXPECT_GE(region.startTick, 0);
        EXPECT_GT(region.endTick, region.startTick);
    }

    delete score;
}
