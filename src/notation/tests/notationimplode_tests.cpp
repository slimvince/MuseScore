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

#include <sstream>

#include "global/types/translatablestring.h"
#include "modularity/ioc.h"

#include "composing/icomposinganalysisconfiguration.h"
#include "composing/icomposingchordstaffconfiguration.h"

#include "engraving/dom/chord.h"
#include "engraving/dom/chordrest.h"
#include "engraving/dom/factory.h"
#include "engraving/dom/harmony.h"
#include "engraving/dom/key.h"
#include "engraving/dom/masterscore.h"
#include "engraving/dom/measure.h"
#include "engraving/dom/note.h"
#include "engraving/dom/part.h"
#include "engraving/dom/rest.h"
#include "engraving/dom/segment.h"
#include "engraving/dom/staff.h"
#include "engraving/dom/stafftext.h"

#include "engraving/editing/undo.h"
#include "engraving/tests/utils/scorerw.h"

#include "notation/internal/notationcomposingbridge.h"
#include "notation/internal/notationanalysisinternal.h"
#include "notation/internal/notationcomposingbridgehelpers.h"
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

void configureChordStaffConfidenceExposureTest()
{
    auto analysis = analysisConfig();
    ASSERT_TRUE(analysis);
    analysis->setUseRegionalAccumulation(true);

    auto chordStaff = chordStaffConfig();
    ASSERT_TRUE(chordStaff);
    chordStaff->setChordStaffWriteChordSymbols(false);
    chordStaff->setChordStaffFunctionNotation("roman");
    chordStaff->setChordStaffWriteKeyAnnotations(true);
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

std::vector<int> emptyInferenceTicks(MasterScore* score,
                                     staff_idx_t targetTrebleStaff,
                                     const Fraction& startTick,
                                     const Fraction& endTick)
{
    std::vector<int> ticks;
    const std::set<size_t> excludeStaves = {
        static_cast<size_t>(targetTrebleStaff),
        static_cast<size_t>(targetTrebleStaff + 1),
    };
    std::set<int> seenTicks;

    for (Segment* segment = score->tick2segment(startTick, true, SegmentType::ChordRest);
         segment && segment->tick() < endTick;
         segment = segment->next1(SegmentType::ChordRest)) {
        bool hasSourceChord = false;
        for (size_t staffIdx = 0; staffIdx < score->nstaves() && !hasSourceChord; ++staffIdx) {
            if (excludeStaves.count(staffIdx)
                || !mu::notation::internal::staffIsEligible(score, staffIdx, segment->tick())) {
                continue;
            }

            for (int voice = 0; voice < VOICES && !hasSourceChord; ++voice) {
                const ChordRest* chordRest = segment->cr(static_cast<track_idx_t>(staffIdx) * VOICES + voice);
                hasSourceChord = chordRest && chordRest->isChord() && !chordRest->isGrace();
            }
        }

        if (!hasSourceChord || !seenTicks.insert(segment->tick().ticks()).second) {
            continue;
        }

        const auto context = mu::notation::analyzeHarmonicContextAtTick(score,
                                                                        segment->tick(),
                                                                        0,
                                                                        excludeStaves);
        if (context.chordResults.empty()) {
            ticks.push_back(segment->tick().ticks());
        }
    }

    return ticks;
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

std::vector<std::string> harmonyTextsAt(MasterScore* score, const Fraction& tick, track_idx_t track)
{
    std::vector<std::string> texts;

    Segment* segment = score->tick2segment(tick, true, SegmentType::ChordRest);
    if (!segment || segment->tick() != tick) {
        return texts;
    }

    for (EngravingItem* annotation : segment->annotations()) {
        if (!annotation || !annotation->isHarmony() || annotation->track() != track) {
            continue;
        }
        texts.push_back(toHarmony(annotation)->plainText().toStdString());
    }

    return texts;
}

std::vector<std::string> staffTextsAt(MasterScore* score, const Fraction& tick, track_idx_t track)
{
    std::vector<std::string> texts;

    Segment* segment = score->tick2segment(tick, true, SegmentType::ChordRest);
    if (!segment || segment->tick() != tick) {
        return texts;
    }

    for (EngravingItem* annotation : segment->annotations()) {
        if (!annotation || !annotation->isStaffText() || annotation->track() != track) {
            continue;
        }
        texts.push_back(toStaffText(annotation)->plainText().toStdString());
    }

    return texts;
}

bool hasOverlappingChordAndRestOnTrack(MasterScore* score, track_idx_t track)
{
    struct Span {
        Fraction start;
        Fraction end;
        bool isChord;
    };

    std::vector<Span> spans;
    for (Segment* segment = score->firstSegment(SegmentType::ChordRest);
         segment;
         segment = segment->next1(SegmentType::ChordRest)) {
        ChordRest* chordRest = segment->cr(track);
        if (!chordRest) {
            continue;
        }

        spans.push_back({
            chordRest->tick(),
            chordRest->tick() + chordRest->actualTicks(),
            chordRest->isChord(),
        });
    }

    for (size_t i = 0; i < spans.size(); ++i) {
        for (size_t j = i + 1; j < spans.size(); ++j) {
            if (spans[i].isChord == spans[j].isChord) {
                continue;
            }
            if (spans[i].start < spans[j].end && spans[j].start < spans[i].end) {
                return true;
            }
        }
    }

    return false;
}

std::vector<int> mixedChordRestMeasuresOnTrack(MasterScore* score, track_idx_t track)
{
    std::vector<int> measures;
    int measureNumber = 0;

    for (Measure* measure = score->firstMeasure(); measure; measure = measure->nextMeasure()) {
        ++measureNumber;
        bool hasChord = false;
        bool hasRest = false;

        for (Segment* segment = measure->first(SegmentType::ChordRest);
             segment;
             segment = segment->next(SegmentType::ChordRest)) {
            ChordRest* chordRest = segment->cr(track);
            if (!chordRest) {
                continue;
            }
            hasChord = hasChord || chordRest->isChord();
            hasRest = hasRest || chordRest->isRest();
        }

        if (hasChord && hasRest) {
            measures.push_back(measureNumber);
        }
    }

    return measures;
}

Note* firstNoteInMeasureOnStaff(MasterScore* score, int targetMeasureNumber, staff_idx_t staffIdx)
{
    int measureNumber = 0;
    const track_idx_t track = staffIdx * VOICES;

    for (Measure* measure = score->firstMeasure(); measure; measure = measure->nextMeasure()) {
        ++measureNumber;
        if (measureNumber != targetMeasureNumber) {
            continue;
        }

        for (Segment* segment = measure->first(SegmentType::ChordRest);
             segment;
             segment = segment->next(SegmentType::ChordRest)) {
            ChordRest* chordRest = segment->cr(track);
            if (!chordRest || !chordRest->isChord()) {
                continue;
            }

            Chord* chord = toChord(chordRest);
            if (chord && !chord->notes().empty()) {
                return chord->notes().front();
            }
        }

        break;
    }

    return nullptr;
}

Note* firstSourceNoteInRange(MasterScore* score, const Fraction& startTick, const Fraction& endTick)
{
    Segment* segment = score->tick2segment(startTick, true, SegmentType::ChordRest);
    for (; segment && segment->tick() < endTick; segment = segment->next1(SegmentType::ChordRest)) {
        for (staff_idx_t staffIdx = 0; staffIdx < score->nstaves(); ++staffIdx) {
            const Part* part = score->staff(staffIdx)->part();
            const std::string trackName = part ? part->partName().toStdString() : std::string();
            if (trackName.find("Chord Track") != std::string::npos) {
                continue;
            }

            ChordRest* chordRest = segment->cr(staffIdx * VOICES);
            if (!chordRest || !chordRest->isChord()) {
                continue;
            }

            Chord* chord = toChord(chordRest);
            if (chord && !chord->notes().empty()) {
                return chord->notes().front();
            }
        }
    }

    return nullptr;
}

staff_idx_t appendChordTrackStaffPair(MasterScore* score)
{
    score->startCmd(TranslatableString::untranslatable("Append chord-track staves"));

    auto appendStaff = [&](const muse::String& trackName) {
        Part* part = new Part(score);
        Instrument instrument;
        instrument.setTrackName(trackName);
        part->setInstrument(instrument);
        score->appendPart(part);

        Staff* staff = Factory::createStaff(part);
        score->undoInsertStaff(staff, 0, true);
    };

    const staff_idx_t trebleStaffIdx = score->nstaves();
    appendStaff(u"Chord Track Treble");
    appendStaff(u"Chord Track Bass");

    score->endCmd();
    return trebleStaffIdx;
}

void normalizePopulatedRegionStarts(MasterScore* score,
                                    std::vector<mu::composing::analysis::HarmonicRegion>& regions,
                                    const Fraction& startTick,
                                    const Fraction& endTick)
{
    std::vector<mu::composing::analysis::HarmonicRegion> normalizedRegions;
    normalizedRegions.reserve(regions.size() * 2);
    const int analysisRangeStartTick = startTick.ticks();

    for (Measure* measure = score->tick2measure(startTick);
         measure && measure->tick() < endTick;
         measure = measure->nextMeasure()) {
        const Fraction measureRangeStart = std::max(measure->tick(), startTick);
        const Fraction measureRangeEnd = std::min(measure->endTick(), endTick);
        const int measureStartTick = measureRangeStart.ticks();
        const int measureEndTick = measureRangeEnd.ticks();

        std::vector<size_t> overlappingRegions;
        for (size_t i = 0; i < regions.size(); ++i) {
            if (regions[i].endTick > measureStartTick && regions[i].startTick < measureEndTick) {
                overlappingRegions.push_back(i);
            }
        }

        if (overlappingRegions.empty()) {
            continue;
        }

        const bool carriesIntoMeasure = regions[overlappingRegions.front()].startTick < measureStartTick;
        int populatedStartTick = (carriesIntoMeasure || measureStartTick == analysisRangeStartTick)
                                 ? measureStartTick
                                 : std::max(measureStartTick, regions[overlappingRegions.front()].startTick);

        for (size_t i = 0; i < overlappingRegions.size(); ++i) {
            auto normalizedRegion = regions[overlappingRegions[i]];
            const int nextBoundaryTick = (i + 1 < overlappingRegions.size())
                                         ? regions[overlappingRegions[i + 1]].startTick
                                         : measureEndTick;
            normalizedRegion.startTick = populatedStartTick;
            normalizedRegion.endTick = std::min(measureEndTick, nextBoundaryTick);
            if (normalizedRegion.startTick < normalizedRegion.endTick) {
                normalizedRegions.push_back(std::move(normalizedRegion));
            }
            populatedStartTick = std::min(measureEndTick, nextBoundaryTick);
        }
    }

    regions = std::move(normalizedRegions);
}

const mu::composing::analysis::ChordAnalysisTone* findToneByPc(
    const std::vector<mu::composing::analysis::ChordAnalysisTone>& tones,
    int pitchClass)
{
    for (const auto& tone : tones) {
        if (tone.pitch % 12 == pitchClass) {
            return &tone;
        }
    }

    return nullptr;
}

std::string summarizeRegions(const std::vector<mu::composing::analysis::HarmonicRegion>& regions)
{
    std::ostringstream out;

    for (const auto& region : regions) {
        if (!out.str().empty()) {
            out << "; ";
        }

        out << region.startTick << "-" << region.endTick << ":"
            << mu::composing::analysis::ChordSymbolFormatter::formatSymbol(
            region.chordResult,
            region.keyModeResult.keySignatureFifths);
    }

    return out.str();
}

void populateWholeScore(MasterScore* score, staff_idx_t trebleStaffIdx)
{
    score->startCmd(TranslatableString::untranslatable("Notation implode tests"));
    EXPECT_TRUE(mu::notation::populateChordTrack(
        score, Fraction(0, 1), score->endTick(), trebleStaffIdx));
    score->endCmd();
}

void populateWholeScore(MasterScore* score, staff_idx_t trebleStaffIdx, bool useCollectedTones)
{
    score->startCmd(TranslatableString::untranslatable("Notation implode tests"));
    EXPECT_TRUE(mu::notation::populateChordTrack(
        score, Fraction(0, 1), score->endTick(), trebleStaffIdx, useCollectedTones));
    score->endCmd();
}

void setOpeningKeySignature(MasterScore* score, int fifths, KeyMode mode)
{
    KeySigEvent keySigEvent;
    keySigEvent.setConcertKey(Key(fifths));
    keySigEvent.setKey(Key(fifths));
    keySigEvent.setMode(mode);

    for (staff_idx_t staffIdx = 0; staffIdx < score->nstaves(); ++staffIdx) {
        score->staff(staffIdx)->setKey(Fraction(0, 1), keySigEvent);
    }
}

Fraction tickInMeasure(MasterScore* score, int measureNumber, int offsetTicks)
{
    int currentMeasureNumber = 0;
    for (Measure* measure = score->firstMeasure(); measure; measure = measure->nextMeasure()) {
        ++currentMeasureNumber;
        if (currentMeasureNumber == measureNumber) {
            return measure->tick() + Fraction::fromTicks(offsetTicks);
        }
    }

    return Fraction::fromTicks(-1);
}

std::vector<int> chordPitchesAt(MasterScore* score, const Fraction& tick, track_idx_t track)
{
    std::vector<int> pitches;

    Segment* segment = score->tick2segment(tick, true, SegmentType::ChordRest);
    if (!segment || segment->tick() != tick) {
        return pitches;
    }

    ChordRest* chordRest = segment->cr(track);
    if (!chordRest || !chordRest->isChord()) {
        return pitches;
    }

    Chord* chord = toChord(chordRest);
    if (!chord) {
        return pitches;
    }

    for (Note* note : chord->notes()) {
        if (note) {
            pitches.push_back(note->pitch());
        }
    }

    return pitches;
}

std::string summarizePitches(const std::vector<int>& pitches)
{
    std::ostringstream out;
    for (size_t i = 0; i < pitches.size(); ++i) {
        if (i > 0) {
            out << ",";
        }
        out << pitches[i];
    }
    return out.str();
}

std::string summarizeMeasureHarmonyTexts(MasterScore* score, int measureNumber, track_idx_t track)
{
    std::ostringstream out;
    int currentMeasureNumber = 0;

    for (Measure* measure = score->firstMeasure(); measure; measure = measure->nextMeasure()) {
        ++currentMeasureNumber;
        if (currentMeasureNumber != measureNumber) {
            continue;
        }

        for (Segment* segment = measure->first(SegmentType::ChordRest);
             segment;
             segment = segment->next(SegmentType::ChordRest)) {
            const auto texts = harmonyTextsAt(score, segment->tick(), track);
            if (texts.empty()) {
                continue;
            }

            out << "[" << (segment->tick() - measure->tick()).ticks() << ":";
            for (size_t i = 0; i < texts.size(); ++i) {
                if (i > 0) {
                    out << ",";
                }
                out << texts[i];
            }
            out << "]";
        }

        break;
    }

    return out.str();
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
    EXPECT_FALSE(hasOverlappingChordAndRestOnTrack(score, kTargetTrebleTrack));
    EXPECT_FALSE(hasOverlappingChordAndRestOnTrack(score, (kTargetTrebleStaff + 1) * VOICES));
    EXPECT_TRUE(hasHarmonyAt(score, Fraction(0, 1), kTargetTrebleTrack));
    EXPECT_TRUE(hasHarmonyAt(score, Fraction(2, 4), kTargetTrebleTrack));

    delete score;
}

TEST_F(Notation_ImplodeTests, CollectRegionTonesAddsPedalTailOnlyInsidePedaledRegion)
{
    MasterScore* score = ScoreRW::readScore(u"implode_pedal_tail_support.mscx");
    ASSERT_TRUE(score);

    const auto pedaledRegion = mu::notation::internal::collectRegionTones(
        score,
        Fraction(1, 4).ticks(),
        Fraction(2, 4).ticks(),
        {});
    const auto unpedaledRegion = mu::notation::internal::collectRegionTones(
        score,
        Fraction(5, 4).ticks(),
        Fraction(6, 4).ticks(),
        {});

    const auto* pedaledBassTone = findToneByPc(pedaledRegion, 0);
    ASSERT_NE(pedaledBassTone, nullptr);
    EXPECT_GT(pedaledBassTone->weight, 0.0);
    EXPECT_GT(pedaledBassTone->durationInRegion, 0);

    const auto* unpedaledBassTone = findToneByPc(unpedaledRegion, 2);
    EXPECT_EQ(unpedaledBassTone, nullptr);

    const auto* pedaledUpperTone = findToneByPc(pedaledRegion, 4);
    const auto* unpedaledUpperTone = findToneByPc(unpedaledRegion, 5);
    ASSERT_NE(pedaledUpperTone, nullptr);
    ASSERT_NE(unpedaledUpperTone, nullptr);

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
    ASSERT_EQ(regions.size(), 3);
    EXPECT_EQ(regions[0].startTick, Fraction(0, 1).ticks());
    EXPECT_EQ(regions[1].startTick, Fraction(1, 4).ticks());
    EXPECT_EQ(regions[2].startTick, Fraction(2, 4).ticks());
    EXPECT_NE(regions.back().chordResult.identity.quality,
              mu::composing::analysis::ChordQuality::Unknown);
    const auto finalVoicing = mu::composing::analysis::closePositionVoicing(regions.back().chordResult);
    EXPECT_GE(finalVoicing.bassPitch, 0);
    EXPECT_FALSE(mu::composing::analysis::ChordSymbolFormatter::formatSymbol(
        regions.back().chordResult,
        regions.back().keyModeResult.keySignatureFifths).empty());
    EXPECT_EQ(regions.back().endTick, Fraction(4, 4).ticks());

    ASSERT_EQ(countChordStartsOnStaff(score, kTargetTrebleStaff), 0);
    ASSERT_EQ(countChordStartsOnStaff(score, kTargetTrebleStaff + 1), 0);

    populateWholeScore(score, kTargetTrebleStaff);

    EXPECT_EQ(countChordStartsOnStaff(score, kTargetTrebleStaff), 3);
    EXPECT_EQ(countChordStartsOnStaff(score, kTargetTrebleStaff + 1), 3);
    EXPECT_EQ(countHarmonyAnnotationsOnTrack(score, kTargetTrebleTrack), 3);
    EXPECT_FALSE(hasOverlappingChordAndRestOnTrack(score, kTargetTrebleTrack));
    EXPECT_FALSE(hasOverlappingChordAndRestOnTrack(score, (kTargetTrebleStaff + 1) * VOICES));
    EXPECT_TRUE(hasHarmonyAt(score, Fraction(0, 1), kTargetTrebleTrack));
    EXPECT_TRUE(hasHarmonyAt(score, Fraction(1, 4), kTargetTrebleTrack));
    EXPECT_TRUE(hasHarmonyAt(score, Fraction(2, 4), kTargetTrebleTrack));
    EXPECT_FALSE(hasHarmonyAt(score, Fraction(3, 4), kTargetTrebleTrack));

    delete score;
}

TEST_F(Notation_ImplodeTests, JaccardBoundaryDetectionCarriesPedalTailsIntoLaterBeatWindows)
{
    MasterScore* score = ScoreRW::readScore(u"jaccard_pedal_support_same_harmony.mscx");
    ASSERT_TRUE(score);

    const auto boundaries = mu::notation::internal::detectHarmonicBoundariesJaccard(
        score,
        Fraction(0, 1),
        Fraction(4, 4),
        {},
        0.6);

    ASSERT_EQ(boundaries.size(), 1u);
    EXPECT_EQ(boundaries.front(), Fraction(0, 1));

    delete score;
}

TEST_F(Notation_ImplodeTests, ChopinBI16OpeningCollapsesRepeatedTonicRegions)
{
    MasterScore* score = ScoreRW::readScore(
        u"../../../../tools/dcml/chopin_mazurkas/MS3/BI16-1.mscx");
    ASSERT_TRUE(score);

    const auto regions = mu::notation::analyzeHarmonicRhythm(
        score,
        Fraction(1, 8),
        Fraction(7, 8),
        {},
        mu::notation::HarmonicRegionGranularity::PreserveAllChanges);

    ASSERT_EQ(regions.size(), 1);
    EXPECT_EQ(regions.front().chordResult.identity.rootPc, 7);
    EXPECT_EQ(regions.front().chordResult.identity.quality,
              mu::composing::analysis::ChordQuality::Major);

    delete score;
}

TEST_F(Notation_ImplodeTests, ScoreHasValidChordSymbolsIgnoresRomanHarmonyImports)
{
    MasterScore* score = ScoreRW::readScore(
        u"../../../../tools/dcml/mozart_piano_sonatas/MS3/K279-1.mscx");
    ASSERT_TRUE(score);

    EXPECT_FALSE(mu::notation::internal::scoreHasValidChordSymbols(
        score,
        Fraction(0, 1),
        score->endTick()));

    delete score;
}

TEST_F(Notation_ImplodeTests, ScoreHasValidChordSymbolsDetectsStandardHarmonyAnnotations)
{
    MasterScore* score = ScoreRW::readScore(u"implode_half_measure_harmony_changes.mscx");
    ASSERT_TRUE(score);

    Segment* segment = score->firstSegment(SegmentType::ChordRest);
    ASSERT_TRUE(segment);
    ChordRest* chordRest = segment->cr(0);
    ASSERT_TRUE(chordRest);

    score->startCmd(TranslatableString::untranslatable("Add standard harmony test annotation"));
    Harmony* harmony = Factory::createHarmony(segment);
    harmony->setHarmonyType(HarmonyType::STANDARD);
    harmony->setHarmony(u"C");
    harmony->setTrack(chordRest->track());
    harmony->setParent(segment);
    score->undoAddElement(harmony);
    score->endCmd();
    score->doLayout();

    EXPECT_TRUE(mu::notation::internal::scoreHasValidChordSymbols(
        score,
        Fraction(0, 1),
        score->endTick()));

    delete score;
}

TEST_F(Notation_ImplodeTests, MozartK279OpeningPrefersCMajorOverFLydian)
{
    MasterScore* score = ScoreRW::readScore(
        u"../../../../tools/dcml/mozart_piano_sonatas/MS3/K279-1.mscx");
    ASSERT_TRUE(score);

    const auto regions = mu::notation::analyzeHarmonicRhythm(
        score,
        Fraction(0, 1),
        Fraction(4, 4),
        {},
        mu::notation::HarmonicRegionGranularity::PreserveAllChanges);

    ASSERT_FALSE(regions.empty());
    EXPECT_EQ(regions.front().startTick, Fraction(0, 1).ticks());
    EXPECT_EQ(regions.front().keyModeResult.keySignatureFifths, 0);
    EXPECT_EQ(regions.front().keyModeResult.mode, mu::composing::analysis::KeySigMode::Ionian);

    delete score;
}

TEST_F(Notation_ImplodeTests, CorelliOp01n08dKeepsLaterDominantEntriesSeparateAcrossSparseGap)
{
    auto analysis = analysisConfig();
    ASSERT_TRUE(analysis);
    analysis->setUseRegionalAccumulation(true);

    MasterScore* score = ScoreRW::readScore(
        u"../../../../tools/dcml/corelli/MS3/op01n08d.mscx");
    ASSERT_TRUE(score);

    const auto regions = mu::notation::analyzeHarmonicRhythm(
        score,
        Fraction(0, 1),
        Fraction::fromTicks(5760),
        {},
        mu::notation::HarmonicRegionGranularity::PreserveAllChanges);

    const auto dominantAtMeasureThreeBeatThree = std::find_if(regions.begin(), regions.end(), [](const auto& region) {
        return region.startTick == 3840;
    });
    ASSERT_NE(dominantAtMeasureThreeBeatThree, regions.end());
    EXPECT_EQ(dominantAtMeasureThreeBeatThree->chordResult.identity.rootPc, 7);
    EXPECT_EQ(dominantAtMeasureThreeBeatThree->chordResult.identity.quality,
              mu::composing::analysis::ChordQuality::Major);
    EXPECT_EQ(dominantAtMeasureThreeBeatThree->endTick, 4320);

    const auto dominantAtMeasureFourBeatThree = std::find_if(regions.begin(), regions.end(), [](const auto& region) {
        return region.startTick == 5280;
    });
    ASSERT_NE(dominantAtMeasureFourBeatThree, regions.end());
    EXPECT_EQ(dominantAtMeasureFourBeatThree->chordResult.identity.rootPc, 7);
    EXPECT_EQ(dominantAtMeasureFourBeatThree->chordResult.identity.quality,
              mu::composing::analysis::ChordQuality::Major);

    delete score;
}

TEST_F(Notation_ImplodeTests, NoteContextMatchesRegionalChordOnSustainedSupportFixture)
{
    auto analysis = analysisConfig();
    ASSERT_TRUE(analysis);
    analysis->setUseRegionalAccumulation(true);

    MasterScore* score = ScoreRW::readScore(u"implode_sustained_support_each_beat.mscx");
    ASSERT_TRUE(score);

    constexpr staff_idx_t kTargetTrebleStaff = 2;
    const auto regions = mu::notation::analyzeHarmonicRhythm(
        score,
        Fraction(0, 1),
        score->endTick(),
        { static_cast<size_t>(kTargetTrebleStaff), static_cast<size_t>(kTargetTrebleStaff + 1) },
        mu::notation::HarmonicRegionGranularity::PreserveAllChanges);
    ASSERT_GE(regions.size(), 3u);

    const auto& targetRegion = regions.back();
    const std::string expectedSymbol = mu::composing::analysis::ChordSymbolFormatter::formatSymbol(
        targetRegion.chordResult,
        targetRegion.keyModeResult.keySignatureFifths);
    ASSERT_FALSE(expectedSymbol.empty());

    bool foundAnalyzableNote = false;
    Segment* segment = score->tick2segment(Fraction::fromTicks(targetRegion.startTick), true, SegmentType::ChordRest);
    for (; segment && segment->tick() < Fraction::fromTicks(targetRegion.endTick);
         segment = segment->next1(SegmentType::ChordRest)) {
        for (staff_idx_t staffIdx = 0; staffIdx < kTargetTrebleStaff; ++staffIdx) {
            ChordRest* chordRest = segment->cr(staffIdx * VOICES);
            if (!chordRest || !chordRest->isChord()) {
                continue;
            }

            Chord* chord = toChord(chordRest);
            if (!chord || chord->notes().empty()) {
                continue;
            }

            const auto context = mu::notation::analyzeNoteHarmonicContextDetails(chord->notes().front());
            if (context.chordResults.empty()) {
                continue;
            }

            foundAnalyzableNote = true;
            EXPECT_EQ(context.keyFifths, targetRegion.keyModeResult.keySignatureFifths);
            EXPECT_EQ(context.keyMode, targetRegion.keyModeResult.mode);
            EXPECT_EQ(mu::composing::analysis::ChordSymbolFormatter::formatSymbol(context.chordResults.front(),
                                                                                  context.keyFifths),
                      expectedSymbol);
            break;
        }

        if (foundAnalyzableNote) {
            break;
        }
    }

    EXPECT_TRUE(foundAnalyzableNote);

    delete score;
}

TEST_F(Notation_ImplodeTests, CorelliOp01n08dMeasureThreeOpeningNoteGetsRegionalChordContext)
{
    auto analysis = analysisConfig();
    ASSERT_TRUE(analysis);
    analysis->setUseRegionalAccumulation(true);
    analysis->setAnalyzeForChordSymbols(true);
    analysis->setAnalyzeForChordFunction(true);
    analysis->setShowChordSymbolsInStatusBar(true);
    analysis->setShowRomanNumeralsInStatusBar(true);
    analysis->setAnalysisAlternatives(1);

    MasterScore* score = ScoreRW::readScore(
        u"../../../../tools/dcml/corelli/MS3/op01n08d.mscx");
    ASSERT_TRUE(score);

    Note* note = firstNoteInMeasureOnStaff(score, 3, 0);
    ASSERT_TRUE(note);
    EXPECT_EQ(note->tick(), Fraction::fromTicks(2880));

    const auto regions = mu::notation::analyzeHarmonicRhythm(
        score,
        Fraction(0, 1),
        Fraction::fromTicks(5760),
        {},
        mu::notation::HarmonicRegionGranularity::Smoothed);
    const auto containingRegion = std::find_if(regions.begin(), regions.end(), [](const auto& region) {
        return region.startTick <= 2880 && 2880 < region.endTick;
    });
    ASSERT_NE(containingRegion, regions.end()) << summarizeRegions(regions);
    EXPECT_EQ(containingRegion->chordResult.identity.rootPc, 0);
    EXPECT_EQ(containingRegion->chordResult.identity.quality,
              mu::composing::analysis::ChordQuality::Minor);

    const auto context = mu::notation::analyzeNoteHarmonicContextDetails(note);
    ASSERT_FALSE(context.chordResults.empty());
    EXPECT_EQ(context.chordResults.front().identity.rootPc, 0);
    EXPECT_EQ(context.chordResults.front().identity.quality,
              mu::composing::analysis::ChordQuality::Minor);
    EXPECT_FALSE(mu::notation::harmonicAnnotation(note).empty());

    delete score;
}

TEST_F(Notation_ImplodeTests, CorelliOp01n08dOpeningNoteContextMatchesPopulateInCMinor)
{
    auto analysis = analysisConfig();
    ASSERT_TRUE(analysis);
    analysis->setUseRegionalAccumulation(true);
    analysis->setAnalyzeForChordSymbols(true);
    analysis->setAnalyzeForChordFunction(true);
    analysis->setShowChordSymbolsInStatusBar(true);
    analysis->setShowRomanNumeralsInStatusBar(true);
    analysis->setShowNashvilleNumbersInStatusBar(false);
    analysis->setShowKeyModeInStatusBar(false);
    analysis->setAnalysisAlternatives(1);

    auto chordStaff = chordStaffConfig();
    ASSERT_TRUE(chordStaff);
    chordStaff->setChordStaffWriteChordSymbols(true);
    chordStaff->setChordStaffFunctionNotation("roman");
    chordStaff->setChordStaffWriteKeyAnnotations(false);
    chordStaff->setChordStaffHighlightNonDiatonic(false);
    chordStaff->setChordStaffWriteCadenceMarkers(false);

    MasterScore* score = ScoreRW::readScore(
        u"../../../../tools/dcml/corelli/MS3/op01n08d.mscx");
    ASSERT_TRUE(score);

    setOpeningKeySignature(score, -3, KeyMode::MINOR);

    Note* note = firstNoteInMeasureOnStaff(score, 1, 0);
    ASSERT_TRUE(note);
    EXPECT_EQ(note->tick(), Fraction(0, 1));

    const auto context = mu::notation::analyzeNoteHarmonicContextDetails(note);
    ASSERT_FALSE(context.chordResults.empty());
    EXPECT_GE(context.keyConfidence, 0.5);
    EXPECT_EQ(mu::composing::analysis::ChordSymbolFormatter::formatSymbol(context.chordResults.front(),
                                                                          context.keyFifths),
              "Cm");
    EXPECT_EQ(mu::composing::analysis::ChordSymbolFormatter::formatRomanNumeral(context.chordResults.front()),
              "i");

    const std::string annotation = mu::notation::harmonicAnnotation(note);
    EXPECT_NE(annotation.find("Cm"), std::string::npos);
    EXPECT_NE(annotation.find("i"), std::string::npos);

    const staff_idx_t targetTrebleStaff = appendChordTrackStaffPair(score);
    const track_idx_t targetTrebleTrack = targetTrebleStaff * VOICES;
    const track_idx_t targetBassTrack = (targetTrebleStaff + 1) * VOICES;

    populateWholeScore(score, targetTrebleStaff);

    EXPECT_EQ(harmonyTextsAt(score, Fraction(0, 1), targetTrebleTrack),
              (std::vector<std::string> { "Cm" }));
    EXPECT_EQ(harmonyTextsAt(score, Fraction(0, 1), targetBassTrack),
              (std::vector<std::string> { "i" }));

    delete score;
}

TEST_F(Notation_ImplodeTests, CorelliOp01n08dOpeningBarsStatusContextMatchPopulateWithoutForcedKeySignature)
{
    auto analysis = analysisConfig();
    ASSERT_TRUE(analysis);
    analysis->setUseRegionalAccumulation(true);
    analysis->setAnalyzeForChordSymbols(true);
    analysis->setAnalyzeForChordFunction(true);
    analysis->setShowChordSymbolsInStatusBar(true);
    analysis->setShowRomanNumeralsInStatusBar(true);
    analysis->setShowNashvilleNumbersInStatusBar(false);
    analysis->setShowKeyModeInStatusBar(false);
    analysis->setAnalysisAlternatives(1);

    auto chordStaff = chordStaffConfig();
    ASSERT_TRUE(chordStaff);
    chordStaff->setChordStaffWriteChordSymbols(true);
    chordStaff->setChordStaffFunctionNotation("roman");
    chordStaff->setChordStaffWriteKeyAnnotations(false);
    chordStaff->setChordStaffHighlightNonDiatonic(false);
    chordStaff->setChordStaffWriteCadenceMarkers(false);

    MasterScore* score = ScoreRW::readScore(
        u"../../../../tools/dcml/corelli/MS3/op01n08d.mscx");
    ASSERT_TRUE(score);

    const staff_idx_t targetTrebleStaff = appendChordTrackStaffPair(score);
    const track_idx_t targetTrebleTrack = targetTrebleStaff * VOICES;
    const track_idx_t targetBassTrack = (targetTrebleStaff + 1) * VOICES;

    populateWholeScore(score, targetTrebleStaff);

    const std::set<size_t> excludeStaves = {
        static_cast<size_t>(targetTrebleStaff),
        static_cast<size_t>(targetTrebleStaff + 1),
    };

    auto expectTickMatchesPopulate = [&](int expectedTick) {
        Note* note = firstSourceNoteInRange(score,
                                            Fraction::fromTicks(expectedTick),
                                            Fraction::fromTicks(expectedTick + 480));
        ASSERT_TRUE(note) << expectedTick;

        const auto expectedContext = mu::notation::analyzeHarmonicContextAtTick(score,
                                                                                Fraction::fromTicks(expectedTick),
                                                                                0,
                                                                                excludeStaves);
        ASSERT_FALSE(expectedContext.chordResults.empty()) << expectedTick;

        const std::string expectedSymbol = mu::composing::analysis::ChordSymbolFormatter::formatSymbol(
            expectedContext.chordResults.front(),
            expectedContext.keyFifths);
        const std::string expectedRoman = mu::composing::analysis::ChordSymbolFormatter::formatRomanNumeral(
            expectedContext.chordResults.front());

        ASSERT_FALSE(expectedSymbol.empty()) << expectedTick;
        EXPECT_FALSE(expectedRoman.empty()) << expectedTick;

        const auto trebleTexts = harmonyTextsAt(score, Fraction::fromTicks(expectedTick), targetTrebleTrack);
        ASSERT_FALSE(trebleTexts.empty()) << expectedTick;
        EXPECT_EQ(trebleTexts.front(), expectedSymbol) << expectedTick;

        const auto bassTexts = harmonyTextsAt(score, Fraction::fromTicks(expectedTick), targetBassTrack);
        ASSERT_FALSE(bassTexts.empty()) << expectedTick;
        EXPECT_EQ(bassTexts.front(), expectedRoman) << expectedTick;

        const auto context = mu::notation::analyzeNoteHarmonicContextDetails(note);
        ASSERT_FALSE(context.chordResults.empty()) << expectedTick;
        EXPECT_EQ(context.keyFifths, expectedContext.keyFifths) << expectedTick;
        EXPECT_EQ(context.keyMode, expectedContext.keyMode) << expectedTick;
        EXPECT_DOUBLE_EQ(context.keyConfidence, expectedContext.keyConfidence) << expectedTick;
        EXPECT_EQ(mu::composing::analysis::ChordSymbolFormatter::formatSymbol(context.chordResults.front(),
                                                                              context.keyFifths),
                  expectedSymbol) << expectedTick;
        EXPECT_EQ(mu::composing::analysis::ChordSymbolFormatter::formatRomanNumeral(context.chordResults.front()),
                  expectedRoman) << expectedTick;

        const std::string annotation = mu::notation::harmonicAnnotation(note);
        EXPECT_NE(annotation.find(expectedSymbol), std::string::npos) << expectedTick << ": " << annotation;
        EXPECT_NE(annotation.find(expectedRoman), std::string::npos) << expectedTick << ": " << annotation;
    };

    expectTickMatchesPopulate(0);
    expectTickMatchesPopulate(1440);
    expectTickMatchesPopulate(2880);

    delete score;
}

TEST_F(Notation_ImplodeTests, PopulateChordTrackDoesNotLeaveMixedChordRestMeasuresOnBI16)
{
    configureChordStaffPopulate();

    MasterScore* score = ScoreRW::readScore(
        u"../../../../tools/dcml/chopin_mazurkas/MS3/BI16-1.mscx");
    ASSERT_TRUE(score);

    const staff_idx_t kTargetTrebleStaff = appendChordTrackStaffPair(score);
    const track_idx_t kTargetTrebleTrack = kTargetTrebleStaff * VOICES;
    const track_idx_t kTargetBassTrack = (kTargetTrebleStaff + 1) * VOICES;

    const auto missingInferenceTicks = emptyInferenceTicks(score,
                                                           kTargetTrebleStaff,
                                                           Fraction(0, 1),
                                                           score->endTick());
    EXPECT_TRUE(missingInferenceTicks.empty()) << ::testing::PrintToString(missingInferenceTicks);

    populateWholeScore(score, kTargetTrebleStaff);

    const auto trebleMixed = mixedChordRestMeasuresOnTrack(score, kTargetTrebleTrack);
    const auto bassMixed = mixedChordRestMeasuresOnTrack(score, kTargetBassTrack);

    EXPECT_TRUE(trebleMixed.empty()) << ::testing::PrintToString(trebleMixed);
    EXPECT_TRUE(bassMixed.empty()) << ::testing::PrintToString(bassMixed);

    delete score;
}

TEST_F(Notation_ImplodeTests, PopulateChordTrackPreservesCorelliOp01n08dCarryInAndLateDominant)
{
    configureChordStaffPopulate();

    MasterScore* score = ScoreRW::readScore(
        u"../../../../tools/dcml/corelli/MS3/op01n08d.mscx");
    ASSERT_TRUE(score);

    const staff_idx_t targetTrebleStaff = appendChordTrackStaffPair(score);
    const track_idx_t targetTrebleTrack = targetTrebleStaff * VOICES;

    populateWholeScore(score, targetTrebleStaff);

    EXPECT_EQ(harmonyTextsAt(score, Fraction(0, 1), targetTrebleTrack),
              (std::vector<std::string> { "Cm" }));
    EXPECT_EQ(harmonyTextsAt(score, Fraction::fromTicks(1440), targetTrebleTrack),
              (std::vector<std::string> { "Cm" }));
    EXPECT_EQ(harmonyTextsAt(score, Fraction::fromTicks(2880), targetTrebleTrack),
              (std::vector<std::string> { "Cm" }));
    EXPECT_EQ(harmonyTextsAt(score, Fraction::fromTicks(3840), targetTrebleTrack),
              (std::vector<std::string> { "G" }));
    EXPECT_TRUE(hasHarmonyAt(score, Fraction::fromTicks(5280), targetTrebleTrack));

    delete score;
}

TEST_F(Notation_ImplodeTests, CorelliOp01n08dOpeningAndSparseLateBeatsDoNotSmearPreviousChord)
{
    auto analysis = analysisConfig();
    ASSERT_TRUE(analysis);
    analysis->setUseRegionalAccumulation(true);
    analysis->setAnalyzeForChordSymbols(true);
    analysis->setAnalyzeForChordFunction(true);
    analysis->setShowChordSymbolsInStatusBar(true);
    analysis->setShowRomanNumeralsInStatusBar(true);
    analysis->setShowNashvilleNumbersInStatusBar(false);
    analysis->setShowKeyModeInStatusBar(false);
    analysis->setAnalysisAlternatives(1);

    auto chordStaff = chordStaffConfig();
    ASSERT_TRUE(chordStaff);
    chordStaff->setChordStaffWriteChordSymbols(true);
    chordStaff->setChordStaffFunctionNotation("roman");
    chordStaff->setChordStaffWriteKeyAnnotations(false);
    chordStaff->setChordStaffHighlightNonDiatonic(false);
    chordStaff->setChordStaffWriteCadenceMarkers(false);

    MasterScore* score = ScoreRW::readScore(
        u"../../../../tools/dcml/corelli/MS3/op01n08d.mscx");
    ASSERT_TRUE(score);

    const staff_idx_t targetTrebleStaff = appendChordTrackStaffPair(score);
    const track_idx_t targetTrebleTrack = targetTrebleStaff * VOICES;

    populateWholeScore(score, targetTrebleStaff);

    const std::set<size_t> excludeStaves = {
        static_cast<size_t>(targetTrebleStaff),
        static_cast<size_t>(targetTrebleStaff + 1),
    };

    struct ExpectedBeat {
        int measureNumber;
        int offsetTicks;
        std::string expectedSymbol;
        std::string unexpectedSymbol;
        bool requireChordTrackSymbol = true;
    };

    const std::vector<ExpectedBeat> expectedBeats = {
        { 1, 960, "G", "Cm", true },
        { 6, 960, "G", "Fm", true },
        { 8, 0, "G", "Ddim/Ab", true },
        { 10, 960, "G", "D", false },
        { 11, 960, "Gm", "D/A", true },
    };

    for (const auto& expectedBeat : expectedBeats) {
        const Fraction tick = tickInMeasure(score, expectedBeat.measureNumber, expectedBeat.offsetTicks);
        ASSERT_GE(tick.ticks(), 0) << expectedBeat.measureNumber;

        const auto expectedContext = mu::notation::analyzeHarmonicContextAtTick(score,
                                                                                tick,
                                                                                0,
                                                                                excludeStaves);
        ASSERT_FALSE(expectedContext.chordResults.empty()) << expectedBeat.measureNumber << ":" << expectedBeat.offsetTicks;

        const std::string actualSymbol = mu::composing::analysis::ChordSymbolFormatter::formatSymbol(
            expectedContext.chordResults.front(),
            expectedContext.keyFifths);
        EXPECT_EQ(actualSymbol, expectedBeat.expectedSymbol) << expectedBeat.measureNumber << ":" << expectedBeat.offsetTicks;

        const auto trebleTexts = harmonyTextsAt(score, tick, targetTrebleTrack);
        if (expectedBeat.requireChordTrackSymbol) {
            ASSERT_FALSE(trebleTexts.empty()) << expectedBeat.measureNumber << ":" << expectedBeat.offsetTicks;
            EXPECT_EQ(trebleTexts.front(), expectedBeat.expectedSymbol) << expectedBeat.measureNumber << ":" << expectedBeat.offsetTicks;
        } else {
            EXPECT_TRUE(trebleTexts.empty() || trebleTexts.front() == expectedBeat.expectedSymbol)
                << expectedBeat.measureNumber << ":" << expectedBeat.offsetTicks;
        }

        if (!trebleTexts.empty() && !expectedBeat.unexpectedSymbol.empty()) {
            EXPECT_NE(trebleTexts.front(), expectedBeat.unexpectedSymbol)
                << expectedBeat.measureNumber << ":" << expectedBeat.offsetTicks;
        }

        Note* note = firstSourceNoteInRange(score, tick, tick + Fraction::fromTicks(1));
        ASSERT_TRUE(note) << expectedBeat.measureNumber << ":" << expectedBeat.offsetTicks;

        const std::string annotation = mu::notation::harmonicAnnotation(note);
        EXPECT_NE(annotation.find(expectedBeat.expectedSymbol), std::string::npos)
            << expectedBeat.measureNumber << ":" << expectedBeat.offsetTicks << ": " << annotation;
        if (!expectedBeat.unexpectedSymbol.empty()) {
            EXPECT_EQ(annotation.find(expectedBeat.unexpectedSymbol), std::string::npos)
                << expectedBeat.measureNumber << ":" << expectedBeat.offsetTicks << ": " << annotation;
        }
    }

    delete score;
}

TEST_F(Notation_ImplodeTests, PopulateChordTrackHandlesTupletedDvorakOp08n06)
{
    configureChordStaffPopulate();

    MasterScore* score = ScoreRW::readScore(
        u"../../../../tools/dcml/dvorak_silhouettes/MS3/op08n06.mscx");
    ASSERT_TRUE(score);

    const staff_idx_t kTargetTrebleStaff = appendChordTrackStaffPair(score);
    const track_idx_t kTargetTrebleTrack = kTargetTrebleStaff * VOICES;
    const track_idx_t kTargetBassTrack = (kTargetTrebleStaff + 1) * VOICES;

    const auto missingInferenceTicks = emptyInferenceTicks(score,
                                                           kTargetTrebleStaff,
                                                           Fraction(0, 1),
                                                           score->endTick());
    EXPECT_TRUE(missingInferenceTicks.empty()) << ::testing::PrintToString(missingInferenceTicks);

    populateWholeScore(score, kTargetTrebleStaff);

    const auto trebleMixed = mixedChordRestMeasuresOnTrack(score, kTargetTrebleTrack);
    const auto bassMixed = mixedChordRestMeasuresOnTrack(score, kTargetBassTrack);

    EXPECT_FALSE(hasOverlappingChordAndRestOnTrack(score, kTargetTrebleTrack));
    EXPECT_FALSE(hasOverlappingChordAndRestOnTrack(score, kTargetBassTrack));
    EXPECT_TRUE(trebleMixed.empty()) << ::testing::PrintToString(trebleMixed);
    EXPECT_TRUE(bassMixed.empty()) << ::testing::PrintToString(bassMixed);
    EXPECT_GT(countChordStartsOnStaff(score, kTargetTrebleStaff), 0);
    EXPECT_GT(countChordStartsOnStaff(score, kTargetTrebleStaff + 1), 0);

    delete score;
}

TEST_F(Notation_ImplodeTests, PopulateChordTrackKeepsRomanAtLowConfidenceButSuppressesKeyAnnotationsOnDvorakOp08n06)
{
    configureChordStaffConfidenceExposureTest();

    MasterScore* score = ScoreRW::readScore(
        u"../../../../tools/dcml/dvorak_silhouettes/MS3/op08n06.mscx");
    ASSERT_TRUE(score);

    struct ExpectedExposure {
        Fraction tick;
        std::string roman;
        bool found = false;
    };

    auto findExpectedExposure = [&](auto confidencePredicate) {
        ExpectedExposure exposure;

        for (Segment* segment = score->firstSegment(SegmentType::ChordRest);
             segment;
             segment = segment->next1(SegmentType::ChordRest)) {
            for (staff_idx_t staffIdx = 0; staffIdx < score->nstaves(); ++staffIdx) {
                const Part* part = score->staff(staffIdx)->part();
                const std::string partName = part ? part->partName().toStdString() : std::string();
                if (partName.find("Chord Track") != std::string::npos) {
                    continue;
                }

                ChordRest* chordRest = segment->cr(staffIdx * VOICES);
                if (!chordRest || !chordRest->isChord()) {
                    continue;
                }

                Chord* chord = toChord(chordRest);
                if (!chord || chord->notes().empty()) {
                    continue;
                }

                const auto context = mu::notation::analyzeNoteHarmonicContextDetails(chord->notes().front());
                if (context.chordResults.empty() || !confidencePredicate(context.keyConfidence)) {
                    continue;
                }

                const std::string roman = mu::composing::analysis::ChordSymbolFormatter::formatRomanNumeral(
                    context.chordResults.front());
                if (roman.empty()) {
                    continue;
                }

                exposure.tick = segment->tick();
                exposure.roman = roman;
                exposure.found = true;
                return exposure;
            }
        }

        return exposure;
    };

    const ExpectedExposure highConfidenceExposure = findExpectedExposure([](double confidence) {
        return confidence >= 0.8;
    });
    const ExpectedExposure lowConfidenceExposure = findExpectedExposure([](double confidence) {
        return confidence < 0.5;
    });
    ASSERT_TRUE(highConfidenceExposure.found);
    ASSERT_TRUE(lowConfidenceExposure.found);

    const staff_idx_t targetTrebleStaff = appendChordTrackStaffPair(score);
    const track_idx_t targetTrebleTrack = targetTrebleStaff * VOICES;
    const track_idx_t targetBassTrack = (targetTrebleStaff + 1) * VOICES;

    populateWholeScore(score, targetTrebleStaff);

    EXPECT_FALSE(staffTextsAt(score, highConfidenceExposure.tick, targetTrebleTrack).empty());
    EXPECT_TRUE(staffTextsAt(score, lowConfidenceExposure.tick, targetTrebleTrack).empty());
    EXPECT_EQ(harmonyTextsAt(score, highConfidenceExposure.tick, targetBassTrack),
              (std::vector<std::string> { highConfidenceExposure.roman }));
    EXPECT_EQ(harmonyTextsAt(score, lowConfidenceExposure.tick, targetBassTrack),
              (std::vector<std::string> { lowConfidenceExposure.roman }));

    delete score;
}

TEST_F(Notation_ImplodeTests, HarmonicAnnotationKeepsRomanAtLowConfidenceNoteContext)
{
    auto analysis = analysisConfig();
    ASSERT_TRUE(analysis);
    analysis->setUseRegionalAccumulation(true);
    analysis->setAnalyzeForChordSymbols(true);
    analysis->setAnalyzeForChordFunction(true);
    analysis->setShowChordSymbolsInStatusBar(true);
    analysis->setShowRomanNumeralsInStatusBar(true);
    analysis->setShowNashvilleNumbersInStatusBar(false);
    analysis->setShowKeyModeInStatusBar(false);
    analysis->setAnalysisAlternatives(1);

    MasterScore* score = ScoreRW::readScore(
        u"../../../../tools/dcml/dvorak_silhouettes/MS3/op08n06.mscx");
    ASSERT_TRUE(score);

    const auto regions = mu::notation::analyzeHarmonicRhythm(
        score,
        Fraction(0, 1),
        score->endTick(),
        {},
        mu::notation::HarmonicRegionGranularity::PreserveAllChanges);
    const auto lowConfidenceRegion = std::find_if(regions.begin(), regions.end(), [](const auto& region) {
        return region.keyModeResult.normalizedConfidence < 0.5;
    });
    ASSERT_NE(lowConfidenceRegion, regions.end());

    Note* note = firstSourceNoteInRange(score,
                                        Fraction::fromTicks(lowConfidenceRegion->startTick),
                                        Fraction::fromTicks(lowConfidenceRegion->endTick));
    ASSERT_TRUE(note);

    const auto context = mu::notation::analyzeNoteHarmonicContextDetails(note);
    EXPECT_LT(context.keyConfidence, 0.5);
    ASSERT_FALSE(context.chordResults.empty());

    const std::string expectedSymbol = mu::composing::analysis::ChordSymbolFormatter::formatSymbol(
        context.chordResults.front(),
        context.keyFifths);
    const std::string expectedRoman = mu::composing::analysis::ChordSymbolFormatter::formatRomanNumeral(
        context.chordResults.front());
    ASSERT_FALSE(expectedSymbol.empty());
    ASSERT_FALSE(expectedRoman.empty());

    const std::string annotation = mu::notation::harmonicAnnotation(note);
    EXPECT_FALSE(annotation.empty());
    EXPECT_NE(annotation.find(expectedSymbol), std::string::npos);
    EXPECT_NE(annotation.find(expectedRoman), std::string::npos);
    EXPECT_NE(annotation.find(" / "), std::string::npos);

    delete score;
}

TEST_F(Notation_ImplodeTests, CorelliOp01n08dUserReportedChordTrackAudit)
{
    auto analysis = analysisConfig();
    ASSERT_TRUE(analysis);
    analysis->setUseRegionalAccumulation(true);

    auto chordStaff = chordStaffConfig();
    ASSERT_TRUE(chordStaff);
    chordStaff->setChordStaffWriteChordSymbols(true);
    chordStaff->setChordStaffFunctionNotation("roman");
    chordStaff->setChordStaffWriteKeyAnnotations(false);
    chordStaff->setChordStaffHighlightNonDiatonic(false);
    chordStaff->setChordStaffWriteCadenceMarkers(false);

    MasterScore* score = ScoreRW::readScore(
        u"../../../../tools/dcml/corelli/MS3/op01n08d.mscx");
    ASSERT_TRUE(score);

    const staff_idx_t targetTrebleStaff = appendChordTrackStaffPair(score);
    const track_idx_t targetTrebleTrack = targetTrebleStaff * VOICES;
    const track_idx_t targetBassTrack = (targetTrebleStaff + 1) * VOICES;

    populateWholeScore(score, targetTrebleStaff, true);

    struct ExpectedBeat {
        int measureNumber;
        int offsetTicks;
        std::string expectedSymbol;
        bool requireRoman;
    };

    const std::vector<ExpectedBeat> expectedBeats = {
        { 2, 960, "G", true },
        { 10, 960, "", true },
        { 13, 960, "Gm", true },
        { 14, 960, "Cm", true },
        { 21, 0, "", true },
        { 24, 0, "Fm", true },
        { 24, 960, "Fm", true },
        { 26, 960, "Cm", true },
    };

    for (const auto& expectedBeat : expectedBeats) {
        const Fraction tick = tickInMeasure(score, expectedBeat.measureNumber, expectedBeat.offsetTicks);
        ASSERT_GE(tick.ticks(), 0) << expectedBeat.measureNumber << ":" << expectedBeat.offsetTicks;

        const auto trebleTexts = harmonyTextsAt(score, tick, targetTrebleTrack);
        const auto bassTexts = harmonyTextsAt(score, tick, targetBassTrack);

        if (!expectedBeat.expectedSymbol.empty()) {
            EXPECT_FALSE(trebleTexts.empty())
                << expectedBeat.measureNumber << ":" << expectedBeat.offsetTicks
                << " treble=" << summarizeMeasureHarmonyTexts(score, expectedBeat.measureNumber, targetTrebleTrack);
            if (!trebleTexts.empty()) {
                EXPECT_EQ(trebleTexts.front(), expectedBeat.expectedSymbol)
                    << expectedBeat.measureNumber << ":" << expectedBeat.offsetTicks
                    << " treble=" << summarizeMeasureHarmonyTexts(score, expectedBeat.measureNumber, targetTrebleTrack);
            }
        }

        if (expectedBeat.requireRoman) {
            EXPECT_FALSE(bassTexts.empty())
                << expectedBeat.measureNumber << ":" << expectedBeat.offsetTicks
                << " bass=" << summarizeMeasureHarmonyTexts(score, expectedBeat.measureNumber, targetBassTrack);
            if (!bassTexts.empty()) {
                EXPECT_FALSE(bassTexts.front().empty())
                    << expectedBeat.measureNumber << ":" << expectedBeat.offsetTicks
                    << " bass=" << summarizeMeasureHarmonyTexts(score, expectedBeat.measureNumber, targetBassTrack);
            }
        }
    }

    const Fraction measure18Beat1 = tickInMeasure(score, 18, 0);
    const Fraction measure18Beat3 = tickInMeasure(score, 18, 960);
    EXPECT_GE(measure18Beat1.ticks(), 0);
    EXPECT_GE(measure18Beat3.ticks(), 0);
    const auto measure18Beat1Symbols = harmonyTextsAt(score, measure18Beat1, targetTrebleTrack);
    const auto measure18Beat3Symbols = harmonyTextsAt(score, measure18Beat3, targetTrebleTrack);
    EXPECT_FALSE(measure18Beat1Symbols.empty())
        << summarizeMeasureHarmonyTexts(score, 18, targetTrebleTrack);
    EXPECT_FALSE(measure18Beat3Symbols.empty())
        << summarizeMeasureHarmonyTexts(score, 18, targetTrebleTrack);
    if (!measure18Beat1Symbols.empty() && !measure18Beat3Symbols.empty()) {
        EXPECT_NE(measure18Beat1Symbols.front(), measure18Beat3Symbols.front());
    }

    const Fraction measure23Beat1 = tickInMeasure(score, 23, 0);
    EXPECT_GE(measure23Beat1.ticks(), 0);
    const auto measure23Beat1Symbols = harmonyTextsAt(score, measure23Beat1, targetTrebleTrack);
    EXPECT_FALSE(measure23Beat1Symbols.empty());
    if (!measure23Beat1Symbols.empty()) {
        EXPECT_EQ(measure23Beat1Symbols.front().find("sususu"), std::string::npos);
    }

    const Fraction measure9Beat3 = tickInMeasure(score, 9, 960);
    EXPECT_GE(measure9Beat3.ticks(), 0);
    const auto measure9TreblePitches = chordPitchesAt(score, measure9Beat3, targetTrebleTrack);
    const auto measure9BassPitches = chordPitchesAt(score, measure9Beat3, targetBassTrack);
    EXPECT_LE(measure9TreblePitches.size(), 1u) << summarizePitches(measure9TreblePitches);
    EXPECT_LE(measure9BassPitches.size(), 1u) << summarizePitches(measure9BassPitches);

    delete score;
}

// ── addHarmonicAnnotationsToSelection regression tests ───────────────────────

class Notation_ComposingBridgeTests : public ::testing::Test
{
};

TEST_F(Notation_ComposingBridgeTests, AddHarmonicAnnotationsToSelectionWritesAndUndoes)
{
    // This fixture has analyzable notes on staff 0 and no pre-existing chord track
    // staves, so the chord-track priority rule does not apply and annotations are
    // written to staff 0 (track 0).
    auto analysis = analysisConfig();
    ASSERT_TRUE(analysis);
    analysis->setUseRegionalAccumulation(true);

    MasterScore* score = ScoreRW::readScore(u"implode_sustained_support_each_beat.mscx");
    ASSERT_TRUE(score);
    ASSERT_GE(score->nstaves(), 1u);

    // This fixture has 4 staves: 0=Pedal, 1=Upper Motion, 2=Chord Track Treble,
    // 3=Chord Track Bass.  Select only staves 0–1 so the chord-track priority
    // rule does NOT apply and annotations land on the source staves.
    ASSERT_GE(score->nstaves(), 2u);
    Segment* startSeg = score->firstSegment(SegmentType::ChordRest);
    ASSERT_TRUE(startSeg);
    score->selection().setRange(startSeg, nullptr, 0, 2);
    ASSERT_TRUE(score->selection().isRange());

    // Baseline: no harmony on staff 0 before calling the function.
    const track_idx_t track0 = 0;
    const int annotationsBefore = countHarmonyAnnotationsOnTrack(score, track0);

    // Write chord symbols to the selection.
    mu::notation::addHarmonicAnnotationsToSelection(score, /*writeChordSymbols=*/true,
                                                    /*writeRomanNumerals=*/false,
                                                    /*writeNashvilleNumbers=*/false);

    // At least one STANDARD harmony annotation must have been written.
    const int annotationsAfter = countHarmonyAnnotationsOnTrack(score, track0);
    EXPECT_GT(annotationsAfter, annotationsBefore)
        << "addHarmonicAnnotationsToSelection wrote no STANDARD annotations to track 0";

    // Verify they are STANDARD type.
    bool hasStandard = false;
    for (Segment* seg = score->firstSegment(SegmentType::ChordRest); seg;
         seg = seg->next1(SegmentType::ChordRest)) {
        for (EngravingItem* ann : seg->annotations()) {
            if (ann && ann->isHarmony() && ann->track() == track0
                && toHarmony(ann)->harmonyType() == HarmonyType::STANDARD) {
                hasStandard = true;
                break;
            }
        }
        if (hasStandard) {
            break;
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

// ── Jazz Mode boundary-detection fix tests (§4.1c) ──────────────────────────
//
// Prior to the fix, analyzeHarmonicRhythmJazz() substituted written chord
// symbol identity directly into HarmonicRegion::chordResult (score sentinel=1.0,
// quality from xmlKind).  The tests below confirm that after the fix:
//   1. Chord symbol positions are still used as region boundaries (boundary
//      detection preserved).
//   2. chordResult.identity comes from analyzeChord() on the sounding notes,
//      not from the written symbol.
//   3. identity.score is a real note-based value, not the old 1.0 sentinel.

/// Helper: add a standard STANDARD Harmony annotation at the given segment.
static Harmony* addHarmonyAtSegment(MasterScore* score, Segment* segment, const QString& text)
{
    ChordRest* cr = segment->cr(0);
    if (!cr) {
        return nullptr;
    }
    score->startCmd(TranslatableString::untranslatable("Add test harmony"));
    Harmony* h = mu::engraving::Factory::createHarmony(segment);
    h->setHarmonyType(HarmonyType::STANDARD);
    h->setHarmony(text);
    h->setTrack(cr->track());
    h->setParent(segment);
    score->undoAddElement(h);
    score->endCmd();
    return h;
}

TEST_F(Notation_ImplodeTests, JazzModeUsesChordSymbolPositionsAsBoundaries)
{
    // Adding a chord symbol at tick 0 and another at tick 960 (second half-note chord)
    // must produce exactly 2 regions in the Jazz path, with boundaries at those ticks.
    MasterScore* score = ScoreRW::readScore(u"implode_half_measure_harmony_changes.mscx");
    ASSERT_TRUE(score);

    Segment* seg0 = score->firstSegment(SegmentType::ChordRest);
    ASSERT_TRUE(seg0);
    Segment* seg1 = score->tick2segment(Fraction(1, 2), true, SegmentType::ChordRest);
    ASSERT_TRUE(seg1) << "expected second ChordRest segment at tick Fraction(1,2)";

    addHarmonyAtSegment(score, seg0, "C");
    addHarmonyAtSegment(score, seg1, "G");
    score->doLayout();

    const auto regions = mu::notation::analyzeHarmonicRhythm(
        score,
        Fraction(0, 1),
        score->endTick(),
        {},
        mu::notation::HarmonicRegionGranularity::Smoothed);

    ASSERT_EQ(regions.size(), 2u) << "expected one region per chord symbol";
    EXPECT_EQ(regions[0].startTick, Fraction(0, 1).ticks());
    EXPECT_EQ(regions[1].startTick, Fraction(1, 2).ticks());
    EXPECT_TRUE(regions[0].fromChordSymbol);
    EXPECT_TRUE(regions[1].fromChordSymbol);

    delete score;
}

TEST_F(Notation_ImplodeTests, JazzModeChordIdentityComesFromNotesNotWrittenSymbol)
{
    // Load a score where:
    //   tick 0–960:  C4+E4+G4 (C major triad) — written symbol "Dm" (D minor, wrong)
    //   tick 960–end: G4+B4+D5 (G major triad) — written symbol "Em" (E minor, wrong)
    //
    // After the fix, analyzeChord() runs on the sounding notes.  The inferred root
    // and quality must come from the notes, not the written symbols.
    //
    // Metadata checks:
    //   regions[0].writtenRootPc == 2  (D = written root of "Dm")
    //   regions[1].writtenRootPc == 4  (E = written root of "Em")
    //
    // Inferred identity checks (note-based):
    //   regions[0] → C major: rootPc=0, quality=Major
    //   regions[1] → G major: rootPc=7, quality=Major
    MasterScore* score = ScoreRW::readScore(u"implode_half_measure_harmony_changes.mscx");
    ASSERT_TRUE(score);

    Segment* seg0 = score->firstSegment(SegmentType::ChordRest);
    ASSERT_TRUE(seg0);
    Segment* seg1 = score->tick2segment(Fraction(1, 2), true, SegmentType::ChordRest);
    ASSERT_TRUE(seg1) << "expected second ChordRest segment at tick Fraction(1,2)";

    addHarmonyAtSegment(score, seg0, "Dm");   // written D minor — notes say C major
    addHarmonyAtSegment(score, seg1, "Em");   // written E minor — notes say G major
    score->doLayout();

    const auto regions = mu::notation::analyzeHarmonicRhythm(
        score,
        Fraction(0, 1),
        score->endTick(),
        {},
        mu::notation::HarmonicRegionGranularity::Smoothed);

    ASSERT_EQ(regions.size(), 2u);

    // ── Region 0: C4+E4+G4 (C major) vs written "Dm" ──
    const auto& r0 = regions[0];
    EXPECT_TRUE(r0.fromChordSymbol);
    EXPECT_EQ(r0.writtenRootPc, 2) << "written root of 'Dm' should be stored as metadata (D=pc2)";
    // Note analysis: C major (root=C, quality=Major)
    EXPECT_EQ(r0.chordResult.identity.rootPc, 0)
        << "note-based analysis of C4+E4+G4 should give root C (pc=0), not D (pc=2) from written symbol";
    EXPECT_EQ(r0.chordResult.identity.quality, mu::composing::analysis::ChordQuality::Major)
        << "note-based analysis of C4+E4+G4 should give Major quality, not Minor from written symbol";
    EXPECT_NE(r0.chordResult.identity.score, 1.0)
        << "identity.score must be a real note-based score, not the old 1.0 sentinel";
    EXPECT_GT(r0.chordResult.identity.score, 0.0);

    // ── Region 1: G4+B4+D5 (G major) vs written "Em" ──
    const auto& r1 = regions[1];
    EXPECT_TRUE(r1.fromChordSymbol);
    EXPECT_EQ(r1.writtenRootPc, 4) << "written root of 'Em' should be stored as metadata (E=pc4)";
    // Note analysis: G major (root=G, quality=Major)
    EXPECT_EQ(r1.chordResult.identity.rootPc, 7)
        << "note-based analysis of G4+B4+D5 should give root G (pc=7), not E (pc=4) from written symbol";
    EXPECT_EQ(r1.chordResult.identity.quality, mu::composing::analysis::ChordQuality::Major)
        << "note-based analysis of G4+B4+D5 should give Major quality, not Minor from written symbol";
    EXPECT_NE(r1.chordResult.identity.score, 1.0)
        << "identity.score must be a real note-based score, not the old 1.0 sentinel";

    delete score;
}

// ── Order-of-annotation consistency test (§5.13 forceClassicalPath) ──────────
//
// Regression guard: writing chord symbols first must not alter the region
// boundaries produced by a subsequent Roman numeral annotation pass.
// This protects the forceClassicalPath=true invariant in
// addHarmonicAnnotationsToSelection.

/// Collect tick positions of all ROMAN-type Harmony elements on track 0.
static std::vector<int> collectRomanHarmonyTicks(MasterScore* score)
{
    std::vector<int> ticks;
    for (Segment* seg = score->firstSegment(SegmentType::ChordRest); seg;
         seg = seg->next1(SegmentType::ChordRest)) {
        for (EngravingItem* ann : seg->annotations()) {
            if (ann && ann->isHarmony() && ann->track() == 0
                    && toHarmony(ann)->harmonyType() == HarmonyType::ROMAN) {
                ticks.push_back(seg->tick().ticks());
            }
        }
    }
    return ticks;
}

TEST_F(Notation_ComposingBridgeTests, AnnotationOrderDoesNotAffectRomanNumeralOutput)
{
    // forceClassicalPath=true must ensure that pre-existing STANDARD chord symbols
    // written by a prior annotation call do not trigger the Jazz boundary-detection
    // path and alter the Roman numeral region boundaries.
    auto analysis = analysisConfig();
    ASSERT_TRUE(analysis);
    analysis->setUseRegionalAccumulation(true);

    MasterScore* score = ScoreRW::readScore(u"implode_sustained_support_each_beat.mscx");
    ASSERT_TRUE(score);
    ASSERT_GE(score->nstaves(), 2u);

    // Select staves 0-1 so chord-track priority does not apply.
    Segment* startSeg = score->firstSegment(SegmentType::ChordRest);
    ASSERT_TRUE(startSeg);
    score->selection().setRange(startSeg, nullptr, 0, 2);
    ASSERT_TRUE(score->selection().isRange());

    // ── Pass A: Roman numerals only (no pre-existing chord symbols) ──
    mu::notation::addHarmonicAnnotationsToSelection(score, /*writeChordSymbols=*/false,
                                                    /*writeRomanNumerals=*/true,
                                                    /*writeNashvilleNumbers=*/false);
    const std::vector<int> romanTicksA = collectRomanHarmonyTicks(score);
    ASSERT_FALSE(romanTicksA.empty()) << "Pass A: no Roman numeral annotations written";

    // Undo Pass A so the score is clean again.
    score->undoStack()->undo(nullptr);
    ASSERT_EQ(collectRomanHarmonyTicks(score).size(), 0u) << "undo did not remove Pass A annotations";

    // ── Pass B: chord symbols first, then Roman numerals ──
    // Restore same selection.
    score->selection().setRange(startSeg, nullptr, 0, 2);
    mu::notation::addHarmonicAnnotationsToSelection(score, /*writeChordSymbols=*/true,
                                                    /*writeRomanNumerals=*/false,
                                                    /*writeNashvilleNumbers=*/false);

    // Now the score has STANDARD harmonies.  A second annotation pass must ignore
    // them (forceClassicalPath=true) and produce the same Roman numeral positions.
    score->selection().setRange(startSeg, nullptr, 0, 2);
    mu::notation::addHarmonicAnnotationsToSelection(score, /*writeChordSymbols=*/false,
                                                    /*writeRomanNumerals=*/true,
                                                    /*writeNashvilleNumbers=*/false);
    const std::vector<int> romanTicksB = collectRomanHarmonyTicks(score);

    EXPECT_EQ(romanTicksA.size(), romanTicksB.size())
        << "Roman numeral annotation count differs depending on whether chord symbols were written first";
    EXPECT_EQ(romanTicksA, romanTicksB)
        << "Roman numeral annotation positions differ depending on whether chord symbols were written first";

    delete score;
}
