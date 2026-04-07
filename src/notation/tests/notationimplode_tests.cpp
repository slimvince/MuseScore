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

#include <gtest/gtest.h>

#include "global/types/translatablestring.h"
#include "modularity/ioc.h"

#include "composing/icomposinganalysisconfiguration.h"
#include "composing/icomposingchordstaffconfiguration.h"

#include "engraving/dom/chordrest.h"
#include "engraving/dom/harmony.h"
#include "engraving/dom/masterscore.h"
#include "engraving/dom/measure.h"
#include "engraving/dom/segment.h"

#include "engraving/tests/utils/scorerw.h"

#include "notation/internal/notationcomposingbridge.h"
#include "notation/internal/notationimplodebridge.h"

using namespace mu::engraving;

namespace {

std::shared_ptr<mu::composing::IComposingAnalysisConfiguration> analysisConfig()
{
    return muse::modularity::globalIoc()->resolve<mu::composing::IComposingAnalysisConfiguration>("composing");
}

std::shared_ptr<mu::composing::IComposingChordStaffConfiguration> chordStaffConfig()
{
    return muse::modularity::globalIoc()->resolve<mu::composing::IComposingChordStaffConfiguration>("composing");
}

void configureChordStaffPopulate()
{
    auto analysis = analysisConfig();
    ASSERT_TRUE(analysis);
    analysis->setUseRegionalAccumulation(true);

    auto chordStaff = chordStaffConfig();
    ASSERT_TRUE(chordStaff);
    chordStaff->setChordStaffWriteChordSymbols(true);
    chordStaff->setChordStaffFunctionNotation("none");
    chordStaff->setChordStaffWriteKeyAnnotations(false);
    chordStaff->setChordStaffHighlightNonDiatonic(false);
    chordStaff->setChordStaffWriteCadenceMarkers(false);
}

int countChordStartsOnStaff(MasterScore* score, staff_idx_t staffIdx)
{
    int count = 0;
    const track_idx_t track = staffIdx * VOICES;

    for (Segment* segment = score->firstSegment(SegmentType::ChordRest);
         segment;
         segment = segment->next1(SegmentType::ChordRest)) {
        ChordRest* chordRest = segment->cr(track);
        if (chordRest && chordRest->isChord()) {
            ++count;
        }
    }

    return count;
}

int countHarmonyAnnotationsOnTrack(MasterScore* score, track_idx_t track)
{
    int count = 0;

    for (Segment* segment = score->firstSegment(SegmentType::ChordRest);
         segment;
         segment = segment->next1(SegmentType::ChordRest)) {
        for (EngravingItem* annotation : segment->annotations()) {
            if (annotation && annotation->isHarmony() && annotation->track() == track) {
                ++count;
            }
        }
    }

    return count;
}

bool hasHarmonyAt(MasterScore* score, const Fraction& tick, track_idx_t track)
{
    Segment* segment = score->tick2segment(tick, true, SegmentType::ChordRest);
    if (!segment || segment->tick() != tick) {
        return false;
    }

    for (EngravingItem* annotation : segment->annotations()) {
        if (annotation && annotation->isHarmony() && annotation->track() == track) {
            return true;
        }
    }

    return false;
}

void populateWholeScore(MasterScore* score, staff_idx_t trebleStaffIdx)
{
    score->startCmd(TranslatableString::untranslatable("Notation implode tests"));
    EXPECT_TRUE(mu::notation::populateChordTrack(
        score, Fraction(0, 1), score->endTick(), trebleStaffIdx));
    score->endCmd();
}

} // namespace

class Notation_ImplodeTests : public ::testing::Test
{
};

TEST_F(Notation_ImplodeTests, ImplodeChordTrackPreservesHalfMeasureHarmonyChanges)
{
    configureChordStaffPopulate();

    MasterScore* score = ScoreRW::readScore(u"implode_half_measure_harmony_changes.mscx");
    ASSERT_TRUE(score);

    constexpr staff_idx_t kTargetTrebleStaff = 1;
    constexpr track_idx_t kTargetTrebleTrack = kTargetTrebleStaff * VOICES;

    ASSERT_EQ(countChordStartsOnStaff(score, kTargetTrebleStaff), 0);
    ASSERT_EQ(countChordStartsOnStaff(score, kTargetTrebleStaff + 1), 0);

    populateWholeScore(score, kTargetTrebleStaff);

    EXPECT_EQ(countChordStartsOnStaff(score, kTargetTrebleStaff), 2);
    EXPECT_EQ(countChordStartsOnStaff(score, kTargetTrebleStaff + 1), 2);
    EXPECT_EQ(countHarmonyAnnotationsOnTrack(score, kTargetTrebleTrack), 2);
    EXPECT_TRUE(hasHarmonyAt(score, Fraction(0, 1), kTargetTrebleTrack));
    EXPECT_TRUE(hasHarmonyAt(score, Fraction(2, 4), kTargetTrebleTrack));

    delete score;
}

TEST_F(Notation_ImplodeTests, ImplodeChordTrackKeepsSustainedSupportAcrossBeatBoundaries)
{
    configureChordStaffPopulate();

    MasterScore* score = ScoreRW::readScore(u"implode_sustained_support_each_beat.mscx");
    ASSERT_TRUE(score);

    constexpr staff_idx_t kTargetTrebleStaff = 2;
    constexpr track_idx_t kTargetTrebleTrack = kTargetTrebleStaff * VOICES;

    const auto regions = mu::notation::analyzeHarmonicRhythm(
        score,
        Fraction(0, 1),
        score->endTick(),
        { static_cast<size_t>(kTargetTrebleStaff), static_cast<size_t>(kTargetTrebleStaff + 1) },
        mu::notation::HarmonicRegionGranularity::PreserveAllChanges);
    ASSERT_EQ(regions.size(), 4);
    EXPECT_EQ(regions[0].startTick, Fraction(0, 1).ticks());
    EXPECT_EQ(regions[1].startTick, Fraction(1, 4).ticks());
    EXPECT_EQ(regions[2].startTick, Fraction(2, 4).ticks());
    EXPECT_EQ(regions[3].startTick, Fraction(3, 4).ticks());
    EXPECT_NE(regions.back().chordResult.identity.quality,
              mu::composing::analysis::ChordQuality::Unknown);
    const auto finalVoicing = mu::composing::analysis::closePositionVoicing(regions.back().chordResult);
    EXPECT_GE(finalVoicing.bassPitch, 0);
    EXPECT_FALSE(mu::composing::analysis::ChordSymbolFormatter::formatSymbol(
        regions.back().chordResult,
        regions.back().keyModeResult.keySignatureFifths).empty());

    ASSERT_EQ(countChordStartsOnStaff(score, kTargetTrebleStaff), 0);
    ASSERT_EQ(countChordStartsOnStaff(score, kTargetTrebleStaff + 1), 0);

    populateWholeScore(score, kTargetTrebleStaff);

    EXPECT_EQ(countChordStartsOnStaff(score, kTargetTrebleStaff), 4);
    EXPECT_EQ(countChordStartsOnStaff(score, kTargetTrebleStaff + 1), 4);
    EXPECT_EQ(countHarmonyAnnotationsOnTrack(score, kTargetTrebleTrack), 4);
    EXPECT_TRUE(hasHarmonyAt(score, Fraction(0, 1), kTargetTrebleTrack));
    EXPECT_TRUE(hasHarmonyAt(score, Fraction(1, 4), kTargetTrebleTrack));
    EXPECT_TRUE(hasHarmonyAt(score, Fraction(2, 4), kTargetTrebleTrack));
    EXPECT_TRUE(hasHarmonyAt(score, Fraction(3, 4), kTargetTrebleTrack));

    delete score;
}