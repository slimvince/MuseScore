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

#include <cmath>

#include <gtest/gtest.h>

#include "global/types/translatablestring.h"
#include "composing/intonation/tuning_system.h"

#include "test_helpers.h"

#include "engraving/dom/chord.h"
#include "engraving/dom/chordrest.h"
#include "engraving/dom/masterscore.h"
#include "engraving/dom/measure.h"
#include "engraving/dom/note.h"
#include "engraving/dom/segment.h"
#include "engraving/dom/spanner.h"

#include "engraving/tests/utils/scorerw.h"

#include "notation/internal/notationtuningbridge.h"

using namespace mu::engraving;

namespace {

constexpr track_idx_t kTopTrack = 0;

void configureTuning(mu::composing::intonation::TuningMode mode,
                     bool allowSplitSlurOfSustainedEvents = true)
{
    auto config = analysisConfig();
    ASSERT_TRUE(config);

    config->setTuningSystemKey("just");
    config->setTonicAnchoredTuning(true);
    config->setTuningMode(mode);
    config->setAllowSplitSlurOfSustainedEvents(allowSplitSlurOfSustainedEvents);
    config->setMinimizeTuningDeviation(false);
    config->setAnnotateTuningOffsets(false);
    config->setAnnotateDriftAtBoundaries(false);
    config->setUseRegionalAccumulation(true);
}

Chord* chordAt(MasterScore* score, const Fraction& tick, track_idx_t track = kTopTrack)
{
    Measure* measure = score->tick2measure(tick);
    if (!measure) {
        return nullptr;
    }

    Segment* segment = measure->findSegment(SegmentType::ChordRest, tick);
    if (!segment) {
        return nullptr;
    }

    ChordRest* chordRest = segment->cr(track);
    if (!chordRest || !chordRest->isChord()) {
        return nullptr;
    }

    return toChord(chordRest);
}

Note* noteAt(MasterScore* score, const Fraction& tick, track_idx_t track = kTopTrack)
{
    Chord* chord = chordAt(score, tick, track);
    return chord ? chord->upNote() : nullptr;
}

bool chordHasAnyTie(const Chord* chord)
{
    if (!chord) {
        return false;
    }
    for (const Note* note : chord->notes()) {
        if (note->tieFor() || note->tieBack()) {
            return true;
        }
    }
    return false;
}

bool anyTuningDifference(const Chord* first, const Chord* second)
{
    if (!first || !second || first->notes().size() != second->notes().size()) {
        return false;
    }
    for (size_t index = 0; index < first->notes().size(); ++index) {
        if (std::abs(first->notes()[index]->tuning() - second->notes()[index]->tuning()) > 0.5) {
            return true;
        }
    }
    return false;
}

int countChordStarts(MasterScore* score, track_idx_t track = kTopTrack)
{
    int count = 0;
    for (Segment* segment = score->firstMeasure()->first(SegmentType::ChordRest);
         segment;
         segment = segment->next1(SegmentType::ChordRest)) {
        ChordRest* chordRest = segment->cr(track);
        if (chordRest && chordRest->isChord()) {
            ++count;
        }
    }
    return count;
}

int countSlurs(MasterScore* score)
{
    int count = 0;
    for (const auto& [tick, spanner] : score->spanner()) {
        Q_UNUSED(tick);
        if (spanner && spanner->isSlur()) {
            ++count;
        }
    }
    return count;
}

void applyRegionTuningForWholeScore(MasterScore* score)
{
    score->startCmd(TranslatableString::untranslatable("Notation tuning tests"));
    EXPECT_TRUE(mu::notation::applyRegionTuning(score, Fraction(0, 1), score->endTick()));
    score->endCmd();
}

} // namespace

class Notation_TuningTests : public ::testing::Test
{
};

TEST_F(Notation_TuningTests, TonicAnchoredSplitsNonTiedSustainedNote)
{
    configureTuning(mu::composing::intonation::TuningMode::TonicAnchored);

    MasterScore* score = ScoreRW::readScore(u"split_sustained_note.mscx");
    ASSERT_TRUE(score);
    ASSERT_EQ(countChordStarts(score), 1);
    ASSERT_EQ(countSlurs(score), 0);

    applyRegionTuningForWholeScore(score);

    EXPECT_EQ(countChordStarts(score), 2);
    EXPECT_EQ(countSlurs(score), 1);

    Note* firstNote = noteAt(score, Fraction(0, 1));
    Note* secondNote = noteAt(score, Fraction(2, 4));
    ASSERT_TRUE(firstNote);
    ASSERT_TRUE(secondNote);
    EXPECT_FALSE(firstNote->tieFor());
    EXPECT_FALSE(secondNote->tieBack());
    EXPECT_GT(std::abs(firstNote->tuning() - secondNote->tuning()), 0.5);

    delete score;
}

TEST_F(Notation_TuningTests, FreeDriftKeepsNonTiedSustainedNoteWhole)
{
    configureTuning(mu::composing::intonation::TuningMode::FreeDrift);

    MasterScore* score = ScoreRW::readScore(u"split_sustained_note.mscx");
    ASSERT_TRUE(score);
    ASSERT_EQ(countChordStarts(score), 1);

    applyRegionTuningForWholeScore(score);

    EXPECT_EQ(countChordStarts(score), 1);
    EXPECT_EQ(countSlurs(score), 0);
    EXPECT_TRUE(noteAt(score, Fraction(0, 1)));
    EXPECT_FALSE(noteAt(score, Fraction(2, 4)));

    delete score;
}

TEST_F(Notation_TuningTests, FreeDriftKeepsSimpleTieChainWholeWhenSplitPreferenceDisabled)
{
    configureTuning(mu::composing::intonation::TuningMode::FreeDrift, false);

    MasterScore* score = ScoreRW::readScore(u"preserve_tie_chain.mscx");
    ASSERT_TRUE(score);
    ASSERT_EQ(countChordStarts(score), 2);
    ASSERT_EQ(countSlurs(score), 0);

    applyRegionTuningForWholeScore(score);

    EXPECT_EQ(countChordStarts(score), 2);
    EXPECT_EQ(countSlurs(score), 0);

    Note* firstNote = noteAt(score, Fraction(0, 1));
    Note* secondNote = noteAt(score, Fraction(2, 4));
    ASSERT_TRUE(firstNote);
    ASSERT_TRUE(secondNote);
    ASSERT_TRUE(firstNote->tieFor());
    ASSERT_TRUE(secondNote->tieBack());
    EXPECT_NEAR(firstNote->tuning(), secondNote->tuning(), 0.5);

    delete score;
}

TEST_F(Notation_TuningTests, FreeDriftSplitsNonTiedSustainedChordWhenSplitPreferenceEnabled)
{
    configureTuning(mu::composing::intonation::TuningMode::FreeDrift, true);

    MasterScore* score = ScoreRW::readScore(u"freedrift_split_sustained_chord.mscx");
    ASSERT_TRUE(score);
    ASSERT_EQ(countChordStarts(score), 1);
    ASSERT_EQ(countSlurs(score), 0);

    applyRegionTuningForWholeScore(score);

    EXPECT_EQ(countChordStarts(score), 2);
    EXPECT_EQ(countSlurs(score), 1);

    Chord* firstChord = chordAt(score, Fraction(0, 1));
    Chord* secondChord = chordAt(score, Fraction(2, 4));
    ASSERT_TRUE(firstChord);
    ASSERT_TRUE(secondChord);
    EXPECT_FALSE(chordHasAnyTie(firstChord));
    EXPECT_FALSE(chordHasAnyTie(secondChord));
    EXPECT_TRUE(anyTuningDifference(firstChord, secondChord));

    delete score;
}

TEST_F(Notation_TuningTests, FreeDriftKeepsNonTiedSustainedChordWholeWhenSplitPreferenceDisabled)
{
    configureTuning(mu::composing::intonation::TuningMode::FreeDrift, false);

    MasterScore* score = ScoreRW::readScore(u"freedrift_split_sustained_chord.mscx");
    ASSERT_TRUE(score);
    ASSERT_EQ(countChordStarts(score), 1);
    ASSERT_EQ(countSlurs(score), 0);

    applyRegionTuningForWholeScore(score);

    EXPECT_EQ(countChordStarts(score), 1);
    EXPECT_EQ(countSlurs(score), 0);
    EXPECT_TRUE(chordAt(score, Fraction(0, 1)));
    EXPECT_FALSE(chordAt(score, Fraction(2, 4)));

    delete score;
}

TEST_F(Notation_TuningTests, FreeDriftSplitsTieChainAtExistingBoundaryWhenSplitPreferenceEnabled)
{
    configureTuning(mu::composing::intonation::TuningMode::FreeDrift, true);

    MasterScore* score = ScoreRW::readScore(u"freedrift_split_tie_chain.mscx");
    ASSERT_TRUE(score);
    ASSERT_EQ(countChordStarts(score), 2);
    ASSERT_EQ(countSlurs(score), 0);

    applyRegionTuningForWholeScore(score);

    EXPECT_EQ(countChordStarts(score), 2);
    EXPECT_EQ(countSlurs(score), 1);

    Chord* firstChord = chordAt(score, Fraction(0, 1));
    Chord* secondChord = chordAt(score, Fraction(2, 4));
    ASSERT_TRUE(firstChord);
    ASSERT_TRUE(secondChord);
    EXPECT_FALSE(chordHasAnyTie(firstChord));
    EXPECT_FALSE(chordHasAnyTie(secondChord));
    EXPECT_TRUE(anyTuningDifference(firstChord, secondChord));

    delete score;
}

TEST_F(Notation_TuningTests, FreeDriftKeepsTieChainWholeWhenSplitPreferenceDisabled)
{
    configureTuning(mu::composing::intonation::TuningMode::FreeDrift, false);

    MasterScore* score = ScoreRW::readScore(u"freedrift_split_tie_chain.mscx");
    ASSERT_TRUE(score);
    ASSERT_EQ(countChordStarts(score), 2);
    ASSERT_EQ(countSlurs(score), 0);

    applyRegionTuningForWholeScore(score);

    EXPECT_EQ(countChordStarts(score), 2);
    EXPECT_EQ(countSlurs(score), 0);

    Chord* firstChord = chordAt(score, Fraction(0, 1));
    Chord* secondChord = chordAt(score, Fraction(2, 4));
    ASSERT_TRUE(firstChord);
    ASSERT_TRUE(secondChord);
    EXPECT_TRUE(chordHasAnyTie(firstChord));
    EXPECT_TRUE(chordHasAnyTie(secondChord));
    EXPECT_FALSE(anyTuningDifference(firstChord, secondChord));

    delete score;
}

TEST_F(Notation_TuningTests, TonicAnchoredKeepsNonTiedSustainedNoteWholeWhenSplitPreferenceDisabled)
{
    configureTuning(mu::composing::intonation::TuningMode::TonicAnchored, false);

    MasterScore* score = ScoreRW::readScore(u"split_sustained_note.mscx");
    ASSERT_TRUE(score);
    ASSERT_EQ(countChordStarts(score), 1);
    ASSERT_EQ(countSlurs(score), 0);

    applyRegionTuningForWholeScore(score);

    EXPECT_EQ(countChordStarts(score), 1);
    EXPECT_EQ(countSlurs(score), 0);
    EXPECT_TRUE(noteAt(score, Fraction(0, 1)));
    EXPECT_FALSE(noteAt(score, Fraction(2, 4)));

    delete score;
}

TEST_F(Notation_TuningTests, TonicAnchoredKeepsAnchoredNonTiedSustainedNoteWhole)
{
    configureTuning(mu::composing::intonation::TuningMode::TonicAnchored);

    MasterScore* score = ScoreRW::readScore(u"anchored_sustained_note.mscx");
    ASSERT_TRUE(score);
    ASSERT_EQ(countChordStarts(score), 1);
    ASSERT_EQ(countSlurs(score), 0);

    applyRegionTuningForWholeScore(score);

    EXPECT_EQ(countChordStarts(score), 1);
    EXPECT_EQ(countSlurs(score), 0);

    Note* anchoredNote = noteAt(score, Fraction(0, 1));
    ASSERT_TRUE(anchoredNote);
    EXPECT_NEAR(anchoredNote->tuning(), 0.0, 0.5);
    EXPECT_FALSE(noteAt(score, Fraction(2, 4)));

    delete score;
}

TEST_F(Notation_TuningTests, TonicAnchoredRetunesTieChainAtExistingBoundaryWhenSplitPreferenceEnabled)
{
    configureTuning(mu::composing::intonation::TuningMode::TonicAnchored);

    MasterScore* score = ScoreRW::readScore(u"preserve_tie_chain.mscx");
    ASSERT_TRUE(score);
    ASSERT_EQ(countChordStarts(score), 2);
    ASSERT_EQ(countSlurs(score), 0);

    applyRegionTuningForWholeScore(score);

    EXPECT_EQ(countChordStarts(score), 2);
    EXPECT_EQ(countSlurs(score), 1);

    Note* firstNote = noteAt(score, Fraction(0, 1));
    Note* secondNote = noteAt(score, Fraction(2, 4));
    ASSERT_TRUE(firstNote);
    ASSERT_TRUE(secondNote);
    EXPECT_FALSE(firstNote->tieFor());
    EXPECT_FALSE(secondNote->tieBack());
    EXPECT_GT(std::abs(firstNote->tuning() - secondNote->tuning()), 0.5);

    delete score;
}

TEST_F(Notation_TuningTests, TonicAnchoredKeepsAnchoredTieChainWhole)
{
    configureTuning(mu::composing::intonation::TuningMode::TonicAnchored);

    MasterScore* score = ScoreRW::readScore(u"anchored_tie_chain.mscx");
    ASSERT_TRUE(score);
    ASSERT_EQ(countChordStarts(score), 2);
    ASSERT_EQ(countSlurs(score), 0);

    applyRegionTuningForWholeScore(score);

    EXPECT_EQ(countChordStarts(score), 2);
    EXPECT_EQ(countSlurs(score), 0);

    Note* firstNote = noteAt(score, Fraction(0, 1));
    Note* secondNote = noteAt(score, Fraction(2, 4));
    ASSERT_TRUE(firstNote);
    ASSERT_TRUE(secondNote);
    ASSERT_TRUE(firstNote->tieFor());
    ASSERT_TRUE(secondNote->tieBack());
    EXPECT_NEAR(firstNote->tuning(), 0.0, 0.5);
    EXPECT_NEAR(secondNote->tuning(), 0.0, 0.5);

    delete score;
}

TEST_F(Notation_TuningTests, TonicAnchoredKeepsTieChainWholeWhenSplitPreferenceDisabled)
{
    configureTuning(mu::composing::intonation::TuningMode::TonicAnchored, false);

    MasterScore* score = ScoreRW::readScore(u"preserve_tie_chain.mscx");
    ASSERT_TRUE(score);
    ASSERT_EQ(countChordStarts(score), 2);
    ASSERT_EQ(countSlurs(score), 0);

    applyRegionTuningForWholeScore(score);

    EXPECT_EQ(countChordStarts(score), 2);
    EXPECT_EQ(countSlurs(score), 0);

    Note* firstNote = noteAt(score, Fraction(0, 1));
    Note* secondNote = noteAt(score, Fraction(2, 4));
    ASSERT_TRUE(firstNote);
    ASSERT_TRUE(secondNote);
    ASSERT_TRUE(firstNote->tieFor());
    ASSERT_TRUE(secondNote->tieBack());
    EXPECT_NEAR(firstNote->tuning(), secondNote->tuning(), 0.5);

    delete score;
}

TEST_F(Notation_TuningTests, SplitSlurPreferenceRoundTrips)
{
    auto config = analysisConfig();
    ASSERT_TRUE(config);

    config->setAllowSplitSlurOfSustainedEvents(true);
    EXPECT_TRUE(config->allowSplitSlurOfSustainedEvents());

    config->setAllowSplitSlurOfSustainedEvents(false);
    EXPECT_FALSE(config->allowSplitSlurOfSustainedEvents());

    config->setAllowSplitSlurOfSustainedEvents(true);
    EXPECT_TRUE(config->allowSplitSlurOfSustainedEvents());
}