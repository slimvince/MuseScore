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

// ── Phase-5 branch backfill (round 2, cluster 1) — engravingbridge ────────────
//
// Oracle-asserted tests for the unhit-but-reachable branch directions in the
// L1.5 engraving bridge (regiontonecollector.{h,cpp}, regiontoneprimitives.cpp)
// and scoreharvest/metricweights.cpp, taken from the UNION branch-coverage
// baseline (cc_union_branch_coverage_report.md §5).
//
// COVERAGE IS THE GAP-FINDER, NOT THE GOAL. Each test asserts the *contract /
// music-theory correct* value, re-derived at source — never an echo of the
// implementation's current output. The fixtures are minimal hand-authored
// scores (data/eb_*.{musicxml,mscx}) plus the existing nm_* note-model fixtures.
//
// Several branch directions the upstream triage tagged ADD-TEST are in fact
// UNREACHABLE defensive guards, re-confirmed at source and therefore NOT tested
// here (the formal exclusion is the Phase-6 coverage seal):
//   * cr->isGrace() arms in detectOnsetSubBoundaries / detectBassMovement-
//     SubBoundaries / findTemporalContext — a grace note is stored in its parent
//     Chord's graceNotesBefore()/After() and is NEVER a Segment ChordRest, so
//     Segment::cr(track)->isGrace() is always false (graces surface only as
//     NoteModel events, filtered at the NoteEvent level in soundingAt /
//     weightedPcView, which IS tested below).
//   * cr->tick() != segTick in the two sub-boundary detectors — a ChordRest's
//     tick equals its own segment's tick by construction, so the "onset-only"
//     guard never fires.
//   * tailDuration <= 0 in weightedPcView Pass 4 — a candidate is only recorded
//     when writtenEnd < endTick, and every indexed pedal window ends after
//     startTick and after writtenEnd, so the clipped tail is always positive.
//   * bassPitch == max() after the bass-floor fallback in weightedPcView — once
//     totalWeight > 0 the fallback loop always sets bassPitch.
// See cc_backfill_engravingbridge_report.md for the full per-branch ledger.

#include <gtest/gtest.h>

#include <algorithm>
#include <functional>
#include <set>
#include <vector>

#include "engraving/dom/chord.h"
#include "engraving/dom/chordrest.h"
#include "engraving/dom/instrument.h"
#include "engraving/dom/masterscore.h"
#include "engraving/dom/measure.h"
#include "engraving/dom/note.h"
#include "engraving/dom/part.h"
#include "engraving/dom/pedal.h"
#include "engraving/dom/score.h"
#include "engraving/dom/segment.h"
#include "engraving/dom/sig.h"
#include "engraving/dom/spanner.h"
#include "engraving/dom/staff.h"
#include "engraving/types/constants.h"
#include "engraving/types/fraction.h"
#include "engraving/types/types.h"
#include "engraving/tests/utils/scorerw.h"

#include "composing/analysis/chord/chordanalyzer.h"   // isDiatonicStep oracle
#include "composing/analysis/notemodel/note_model.h"
#include "composing/analysis/engravingbridge/regiontonecollector.h"
#include "composing/analysis/scoreharvest/metricweights.h"

using mu::engraving::BeatType;
using mu::engraving::ElementType;
using mu::engraving::Fraction;
using mu::engraving::MasterScore;
using mu::engraving::Pedal;
using mu::engraving::Score;
using mu::engraving::ScoreRW;
using mu::engraving::Segment;
using mu::engraving::SegmentType;
using mu::engraving::TimeSigFrac;

using mu::composing::analysis::ChordAnalysisTone;
using mu::composing::analysis::ChordAnalyzerPreferences;
using mu::composing::analysis::ChordTemporalContext;
using mu::composing::analysis::isDiatonicStep;
using mu::composing::analysis::KeySigMode;
using mu::composing::analysis::KeyModeAnalyzerPreferences;
using mu::composing::analysis::kDefaultChordAnalyzerPreferences;
using mu::composing::analysis::kDefaultKeyModeAnalyzerPreferences;
using mu::composing::analysis::PitchContext;
using mu::composing::analysis::notemodel::NoteModel;
using NEvent = mu::composing::analysis::notemodel::NoteEvent;

namespace ebr = mu::composing::analysis::engravingbridge;
namespace shv = mu::composing::analysis::scoreharvest;

namespace {

const std::set<std::size_t> kNoExclude {};

// A staff-eligibility predicate that admits every staff (so buildPedalWindowIndex
// tests can drive the excludeStaves / predicate arms independently of the score).
const shv::StaffEligibilityPredicate kAllEligible
    = [](std::size_t) { return true; };

int pcOf(int pitch) { return ((pitch % 12) + 12) % 12; }

const ChordAnalysisTone* findTonePc(const std::vector<ChordAnalysisTone>& tones, int pc)
{
    for (const ChordAnalysisTone& t : tones) {
        if (pcOf(t.pitch) == pc) {
            return &t;
        }
    }
    return nullptr;
}

bool hasTonePc(const std::vector<ChordAnalysisTone>& tones, int pc)
{
    return findTonePc(tones, pc) != nullptr;
}

bool hasPitchContextPitch(const std::vector<PitchContext>& ctx, int pitch)
{
    for (const PitchContext& p : ctx) {
        if (p.pitch == pitch) {
            return true;
        }
    }
    return false;
}

// All Pedal spanners in the score, ascending by start tick.
std::vector<Pedal*> sortedPedals(Score* sc)
{
    std::vector<Pedal*> pedals;
    for (const auto& entry : sc->spanner()) {
        if (entry.second && entry.second->type() == ElementType::PEDAL) {
            pedals.push_back(mu::engraving::toPedal(entry.second));
        }
    }
    std::sort(pedals.begin(), pedals.end(),
              [](Pedal* a, Pedal* b) { return a->tick() < b->tick(); });
    return pedals;
}

const Segment* chordRestSegAt(Score* sc, int tick)
{
    return sc->tick2segment(Fraction::fromTicks(tick), true, SegmentType::ChordRest);
}

// staffEligible flag of the first note on a staff, as computed by the instrumented
// production path NoteModel::build (which calls ebr::staffIsEligible). -1 = no note.
int builtStaffEligible(const NoteModel& model, int staff)
{
    for (const NEvent& e : model.notes()) {
        if (e.staff == staff) {
            return e.staffEligible ? 1 : 0;
        }
    }
    return -1;
}

} // namespace

// ─────────────────────────────────────────────────────────────────────────────
// regiontonecollector.h — staffIsEligible / isChordTrackStaff predicates
// ─────────────────────────────────────────────────────────────────────────────

// Oracle: a staff is INELIGIBLE for harmonic analysis when it is a chord-track
// staff (marked via either the part/instrument long name OR the track name), a
// hidden staff, or a percussion (drumset) staff; an ordinary visible pitched staff
// is eligible. Each case is asserted both directly (the predicate unit) AND through
// the production path NoteModel::build, which calls the same staffIsEligible and
// flags every NoteEvent — the path the live pipeline actually uses.
TEST(Composing_EngravingBridgeBranchTests, EB_StaffPredicates_OrdinaryHiddenDrumsetChordTrack)
{
    const Fraction t0 = Fraction(0, 1);

    // (a) Ordinary pitched staff: not chord-track, eligible (positive control).
    {
        MasterScore* sc = ScoreRW::readScore(u"data/nm_two_staff.mscx");
        ASSERT_TRUE(sc);
        EXPECT_FALSE(ebr::isChordTrackStaff(sc, 0)) << "ordinary Piano staff is not a chord track";
        EXPECT_TRUE(ebr::staffIsEligible(sc, 0, t0)) << "ordinary visible pitched staff is eligible";
        EXPECT_EQ(builtStaffEligible(NoteModel::build(sc), 0), 1) << "ordinary staff flagged eligible";
        delete sc;
    }

    // (b) Hidden staff: Part::show() == false -> Staff::show() == false -> ineligible.
    {
        MasterScore* sc = ScoreRW::readScore(u"data/nm_two_staff.mscx");
        ASSERT_TRUE(sc);
        ASSERT_TRUE(ebr::staffIsEligible(sc, 0, t0));
        sc->staff(0)->part()->setShow(false);
        EXPECT_FALSE(ebr::staffIsEligible(sc, 0, t0)) << "a hidden staff must be ineligible";
        EXPECT_EQ(builtStaffEligible(NoteModel::build(sc), 0), 0) << "hidden staff flagged ineligible";
        delete sc;
    }

    // (c) Drumset (percussion) staff: useDrumset() == true -> ineligible.
    {
        MasterScore* sc = ScoreRW::readScore(u"data/nm_two_staff.mscx");
        ASSERT_TRUE(sc);
        ASSERT_TRUE(ebr::staffIsEligible(sc, 0, t0));
        sc->staff(0)->part()->instrument(t0)->setUseDrumset(true);
        EXPECT_FALSE(ebr::staffIsEligible(sc, 0, t0)) << "a drumset staff must be ineligible";
        EXPECT_EQ(builtStaffEligible(NoteModel::build(sc), 0), 0) << "drumset staff flagged ineligible";
        delete sc;
    }

    // (d) Chord-track staff marked via the TRACK name (nm_staff_eligibility):
    //     ineligible; the ordinary staff in the same score stays eligible.
    {
        MasterScore* sc = ScoreRW::readScore(u"data/nm_staff_eligibility.mscx");
        ASSERT_TRUE(sc);
        EXPECT_FALSE(ebr::isChordTrackStaff(sc, 0)) << "staff 0 (Piano) is not a chord track";
        EXPECT_TRUE(ebr::staffIsEligible(sc, 0, t0));
        EXPECT_TRUE(ebr::isChordTrackStaff(sc, 1)) << "staff 1 is a chord track";
        EXPECT_FALSE(ebr::staffIsEligible(sc, 1, t0)) << "a chord-track staff must be ineligible";
        const NoteModel m = NoteModel::build(sc);
        EXPECT_EQ(builtStaffEligible(m, 0), 1);
        EXPECT_EQ(builtStaffEligible(m, 1), 0) << "chord-track staff flagged ineligible";
        delete sc;
    }

    // (e) Chord-track staff marked via the part/instrument LONG name (eb_steps,
    //     staff 0 long name "Chord Track") -> the partName() arm of isChordTrackStaff.
    {
        MasterScore* sc = ScoreRW::readScore(u"data/eb_steps.mscx");
        ASSERT_TRUE(sc);
        EXPECT_TRUE(ebr::isChordTrackStaff(sc, 0)) << "staff 0 long name marks it a chord track";
        EXPECT_FALSE(ebr::staffIsEligible(sc, 0, t0));
        EXPECT_EQ(builtStaffEligible(NoteModel::build(sc), 0), 0)
            << "long-name chord-track staff flagged ineligible";
        delete sc;
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// regiontonecollector.cpp — weightedPcView
// ─────────────────────────────────────────────────────────────────────────────

// Oracle: a note on an EXCLUDED staff contributes nothing to the pitch-class view.
// nm_two_staff sounds C5 (staff 0) and C3 (staff 1), both pitch-class 0; with both
// staves the pc-0 tone's lowest pitch is C3 (48), but with staff 1 excluded it
// becomes C5 (72) — i.e. the staff-1 evidence was dropped.
TEST(Composing_EngravingBridgeBranchTests, EB_WeightedPcView_ExcludedStaffDropped)
{
    MasterScore* sc = ScoreRW::readScore(u"data/nm_two_staff.mscx");
    ASSERT_TRUE(sc);
    const NoteModel model = NoteModel::build(sc);

    const auto both = ebr::weightedPcView(model, 0, 1920, kNoExclude);
    const ChordAnalysisTone* pc0both = findTonePc(both, 0);
    ASSERT_TRUE(pc0both);
    EXPECT_EQ(pc0both->pitch, 48) << "with both staves the lowest pc-0 pitch is C3";

    const auto excl1 = ebr::weightedPcView(model, 0, 1920, { 1 });
    const ChordAnalysisTone* pc0excl = findTonePc(excl1, 0);
    ASSERT_TRUE(pc0excl);
    EXPECT_EQ(pc0excl->pitch, 72) << "with staff 1 excluded only C5 remains for pc 0";

    delete sc;
}

// Oracle: non-playing and invisible notes are dropped from the pitch-class view.
// nm_flags sounds C4 + E4 (kept), G4 (invisible) and a cue B4 (plays=false) — the
// last two must not appear as evidence.
TEST(Composing_EngravingBridgeBranchTests, EB_WeightedPcView_NonPlayingAndInvisibleDropped)
{
    MasterScore* sc = ScoreRW::readScore(u"data/nm_flags.mscx");
    ASSERT_TRUE(sc);
    const NoteModel model = NoteModel::build(sc);

    const auto tones = ebr::weightedPcView(model, 0, 1920, kNoExclude);
    EXPECT_TRUE(hasTonePc(tones, 0)) << "visible playing C4 kept";
    EXPECT_TRUE(hasTonePc(tones, 4)) << "visible playing E4 kept";
    EXPECT_FALSE(hasTonePc(tones, 7)) << "invisible G4 must be dropped";
    EXPECT_FALSE(hasTonePc(tones, 11)) << "non-playing cue B4 must be dropped";

    delete sc;
}

// Oracle: a note onsetting on the third beat of a 12/8 (compound quadruple) bar
// falls on a COMPOUND_STRESSED beat, weighted 0.85 vs the down-beat's 1.0. The
// fixture sounds equal-length dotted halves C4 (down-beat) and F4 (beat 3); with
// all else equal the weight ratio C:F equals exactly 1.0 : 0.85.
TEST(Composing_EngravingBridgeBranchTests, EB_WeightedPcView_CompoundStressedBeatWeight)
{
    // Pin the music-theory oracle (and guard the fixture): rtick 1440 in 12/8 is
    // COMPOUND_STRESSED (6/8 has only two beats so its second beat is unstressed).
    ASSERT_EQ(TimeSigFrac(12, 8).rtick2beatType(1440), BeatType::COMPOUND_STRESSED);

    MasterScore* sc = ScoreRW::readScore(u"data/eb_compound.mscx");
    ASSERT_TRUE(sc);
    const NoteModel model = NoteModel::build(sc);

    const auto tones = ebr::weightedPcView(model, 0, 2880, kNoExclude);
    const ChordAnalysisTone* c = findTonePc(tones, 0);   // C4 — down-beat (1.0)
    const ChordAnalysisTone* f = findTonePc(tones, 5);   // F4 — beat 3   (0.85)
    ASSERT_TRUE(c);
    ASSERT_TRUE(f);

    // Each note: duration 1440 of a 2880-tick region; only the beat weight differs.
    const double total = 0.5 + 0.5 * 0.85;   // = 0.925
    EXPECT_NEAR(c->weight, 0.5 / total, 1e-9);
    EXPECT_NEAR(f->weight, (0.5 * 0.85) / total, 1e-9);
    EXPECT_NEAR(c->weight / f->weight, 1.0 / 0.85, 1e-9)
        << "the beat-3 note must carry the COMPOUND_STRESSED 0.85 weight";

    delete sc;
}

// Oracle: dense-start look-ahead exclusion. At the region start (tick 480) three
// distinct passing pitch classes sound (C and E sustaining in, G newly attacking),
// so notes onsetting strictly after the start are dropped. The tally must:
//   - count a sustaining-in pitch class ONCE even if doubled (C5 and C6, pc 0),
//   - not re-count an at-start onset whose pc already sustains (C4, pc 0),
//   - skip invisible notes in both the sustain-in and the at-start tallies.
// Result: surviving pcs = {0,4,7}; the post-start A5 (pc 9) is excluded. With the
// exclusion off, A5 reappears.
TEST(Composing_EngravingBridgeBranchTests, EB_WeightedPcView_DenseStartTallyAndDedup)
{
    MasterScore* sc = ScoreRW::readScore(u"data/eb_dense.mscx");
    ASSERT_TRUE(sc);
    const NoteModel model = NoteModel::build(sc);

    const auto dense = ebr::weightedPcView(model, 480, 1920, kNoExclude,
                                           /*parentStartTick=*/-1, /*excludeLookAhead=*/true);
    EXPECT_TRUE(hasTonePc(dense, 0)) << "C sustaining into the dense start kept";
    EXPECT_TRUE(hasTonePc(dense, 4)) << "E sustaining into the dense start kept";
    EXPECT_TRUE(hasTonePc(dense, 7)) << "G attacking at the dense start kept";
    EXPECT_FALSE(hasTonePc(dense, 9)) << "post-start A5 (pc 9) excluded on dense start";
    EXPECT_FALSE(hasTonePc(dense, 3)) << "invisible Eb4 (pc 3) never contributes";

    const auto open = ebr::weightedPcView(model, 480, 1920, kNoExclude,
                                          /*parentStartTick=*/-1, /*excludeLookAhead=*/false);
    EXPECT_TRUE(hasTonePc(open, 9)) << "without the dense-start exclusion A5 is included";

    delete sc;
}

// Oracle: the sustain-pedal tail extends a note's evidence to the pedal release,
// and the tail is suppressed entirely when pedalTailWeightMultiplier is 0. In
// eb_pedal the {C,E,G} chord releases at tick 480 but the pedal holds to 1920, so
// C's in-region duration is 480 (written) + 1440 (tail) = 1920 with the default
// multiplier, and just 480 with the multiplier zeroed.
TEST(Composing_EngravingBridgeBranchTests, EB_WeightedPcView_PedalTailContributesAndMultiplierZeroNoOp)
{
    MasterScore* sc = ScoreRW::readScore(u"data/eb_pedal.mscx");
    ASSERT_TRUE(sc);
    const NoteModel model = NoteModel::build(sc);

    const auto withTail = ebr::weightedPcView(model, 0, 1920, kNoExclude);  // default mult 0.3
    const ChordAnalysisTone* cTail = findTonePc(withTail, 0);
    ASSERT_TRUE(cTail);
    EXPECT_EQ(cTail->durationInRegion, 1920)
        << "C's evidence runs to the pedal release (480 written + 1440 tail)";

    ChordAnalyzerPreferences noTail = kDefaultChordAnalyzerPreferences;
    noTail.pedalTailWeightMultiplier = 0.0;
    const auto withoutTail = ebr::weightedPcView(model, 0, 1920, kNoExclude,
                                                 /*parentStartTick=*/-1,
                                                 /*excludeLookAhead=*/false, noTail);
    const ChordAnalysisTone* cNo = findTonePc(withoutTail, 0);
    ASSERT_TRUE(cNo);
    EXPECT_EQ(cNo->durationInRegion, 480)
        << "with the pedal-tail multiplier zeroed only the written duration counts";

    delete sc;
}

// Oracle: the pedal pass honours the dense-start look-ahead exclusion. In eb_pedal
// the region start sounds three pcs (C,E,G) so the exclusion fires; the strictly-
// post-start D4 onset is dropped from the pedal pass too, while the at-start chord
// still receives its pedal tail.
TEST(Composing_EngravingBridgeBranchTests, EB_WeightedPcView_PedalPassDenseStartLookAhead)
{
    MasterScore* sc = ScoreRW::readScore(u"data/eb_pedal.mscx");
    ASSERT_TRUE(sc);
    const NoteModel model = NoteModel::build(sc);

    const auto dense = ebr::weightedPcView(model, 0, 1920, kNoExclude,
                                           /*parentStartTick=*/-1, /*excludeLookAhead=*/true);
    EXPECT_TRUE(hasTonePc(dense, 0)) << "the at-start C is kept";
    EXPECT_TRUE(hasTonePc(dense, 4)) << "the at-start E is kept";
    EXPECT_TRUE(hasTonePc(dense, 7)) << "the at-start G is kept";
    EXPECT_FALSE(hasTonePc(dense, 2)) << "the post-start D4 (pc 2) is excluded on dense start";

    // The at-start chord still receives its pedal tail under the exclusion.
    const ChordAnalysisTone* c = findTonePc(dense, 0);
    ASSERT_TRUE(c);
    EXPECT_EQ(c->durationInRegion, 1920) << "the at-start C still runs to the pedal release";

    delete sc;
}

// ─────────────────────────────────────────────────────────────────────────────
// scoreharvest/metricweights.cpp
// ─────────────────────────────────────────────────────────────────────────────

// Oracle: the compound-stressed beat maps to the compound-stressed preference
// weight (beatTypeToWeight) and to the canonical 0.85 normalised metric weight
// (regionMetricWeightForBeatType, shared with the simple-stressed beat).
TEST(Composing_EngravingBridgeBranchTests, EB_MetricWeights_CompoundStressedDirect)
{
    const KeyModeAnalyzerPreferences prefs = kDefaultKeyModeAnalyzerPreferences;
    EXPECT_DOUBLE_EQ(shv::beatTypeToWeight(BeatType::COMPOUND_STRESSED, prefs),
                     prefs.beatWeightCompoundStressed);

    EXPECT_DOUBLE_EQ(shv::regionMetricWeightForBeatType(BeatType::COMPOUND_STRESSED), 0.85);
    EXPECT_DOUBLE_EQ(shv::regionMetricWeightForBeatType(BeatType::SIMPLE_STRESSED), 0.85);
}

// Oracle: buildPedalWindowIndex indexes ordinary damper pedals grouped by staff,
// and drops pedals on an excluded staff (excludeStaves) or an ineligible staff
// (predicate). eb_pedal has two damper pedals on staff 0: [0,1920) and [1920,3840).
TEST(Composing_EngravingBridgeBranchTests, EB_BuildPedalWindowIndex_NormalExcludedIneligible)
{
    MasterScore* sc = ScoreRW::readScore(u"data/eb_pedal.mscx");
    ASSERT_TRUE(sc);

    auto idx = shv::buildPedalWindowIndex(sc, 0, 5760, kNoExclude, kAllEligible);
    ASSERT_EQ(idx.size(), 1u) << "both pedals are on staff 0";
    ASSERT_EQ(idx.count(0), 1u);
    ASSERT_EQ(idx.at(0).size(), 2u) << "two ordinary damper pedals indexed";
    EXPECT_EQ(idx.at(0)[0].startTick, 0);
    EXPECT_EQ(idx.at(0)[0].endTick, 1920);
    EXPECT_EQ(idx.at(0)[1].startTick, 1920);
    EXPECT_EQ(idx.at(0)[1].endTick, 3840);

    // Excluded staff: staff 0 in excludeStaves -> nothing indexed.
    auto excluded = shv::buildPedalWindowIndex(sc, 0, 5760, { 0 }, kAllEligible);
    EXPECT_TRUE(excluded.empty()) << "pedals on an excluded staff are dropped";

    // Ineligible staff: the predicate rejects staff 0 -> nothing indexed.
    const shv::StaffEligibilityPredicate none = [](std::size_t) { return false; };
    auto ineligible = shv::buildPedalWindowIndex(sc, 0, 5760, kNoExclude, none);
    EXPECT_TRUE(ineligible.empty()) << "pedals on an ineligible staff are dropped";

    delete sc;
}

// Oracle: sostenuto and soft (una-corda) pedals are NOT sustain windows, and a
// degenerate (zero/negative-length) pedal is skipped. Synthesised by mutating the
// first damper pedal's begin-text / length; the second pedal stays indexed.
TEST(Composing_EngravingBridgeBranchTests, EB_BuildPedalWindowIndex_SostenutoSoftDegenerate)
{
    MasterScore* sc = ScoreRW::readScore(u"data/eb_pedal.mscx");
    ASSERT_TRUE(sc);
    std::vector<Pedal*> pedals = sortedPedals(sc);
    ASSERT_EQ(pedals.size(), 2u);
    Pedal* p0 = pedals[0];   // [0,1920)

    // Sostenuto: begin-text marks it as keyboardPedalSost -> excluded.
    p0->setBeginText(muse::String(u"<sym>keyboardPedalSost</sym>"));
    {
        auto idx = shv::buildPedalWindowIndex(sc, 0, 5760, kNoExclude, kAllEligible);
        ASSERT_EQ(idx.count(0), 1u);
        ASSERT_EQ(idx.at(0).size(), 1u) << "the sostenuto pedal is not a sustain window";
        EXPECT_EQ(idx.at(0)[0].startTick, 1920) << "only the second (damper) pedal remains";
    }

    // Soft (una corda): begin-text keyboardPedalS -> excluded.
    p0->setBeginText(muse::String(u"<sym>keyboardPedalS</sym>"));
    {
        auto idx = shv::buildPedalWindowIndex(sc, 0, 5760, kNoExclude, kAllEligible);
        ASSERT_EQ(idx.count(0), 1u);
        ASSERT_EQ(idx.at(0).size(), 1u) << "the soft pedal is not a sustain window";
        EXPECT_EQ(idx.at(0)[0].startTick, 1920);
    }

    // Degenerate: a damper pedal of zero length (tick2 == tick) is skipped.
    p0->setBeginText(muse::String());           // ordinary again ...
    p0->setTicks(Fraction(0, 1));                // ... but zero-length
    {
        auto idx = shv::buildPedalWindowIndex(sc, 0, 5760, kNoExclude, kAllEligible);
        ASSERT_EQ(idx.count(0), 1u);
        ASSERT_EQ(idx.at(0).size(), 1u) << "a zero-length pedal is skipped";
        EXPECT_EQ(idx.at(0)[0].startTick, 1920);
    }

    delete sc;
}

// Oracle: pedals sharing a start tick on one staff are ordered by end tick. The
// two damper pedals are forced to the same start (tick 0) with different lengths
// (960 and 1920); the shorter must sort first.
TEST(Composing_EngravingBridgeBranchTests, EB_BuildPedalWindowIndex_SameStartSortedByEnd)
{
    MasterScore* sc = ScoreRW::readScore(u"data/eb_pedal.mscx");
    ASSERT_TRUE(sc);
    std::vector<Pedal*> pedals = sortedPedals(sc);
    ASSERT_EQ(pedals.size(), 2u);

    // Force both pedals onto the same start tick, different ends: [0,1920), [0,960).
    pedals[1]->setTick(pedals[0]->tick());        // -> tick 0
    pedals[1]->setTicks(Fraction(1, 2));          // -> half-note length = 960 ticks

    auto idx = shv::buildPedalWindowIndex(sc, 0, 5760, kNoExclude, kAllEligible);
    ASSERT_EQ(idx.count(0), 1u);
    ASSERT_EQ(idx.at(0).size(), 2u);
    EXPECT_EQ(idx.at(0)[0].startTick, 0);
    EXPECT_EQ(idx.at(0)[1].startTick, 0);
    EXPECT_LT(idx.at(0)[0].endTick, idx.at(0)[1].endTick)
        << "equal-start pedals are ordered by end tick (shorter first)";
    EXPECT_EQ(idx.at(0)[0].endTick, 960);
    EXPECT_EQ(idx.at(0)[1].endTick, 1920);

    delete sc;
}

// ─────────────────────────────────────────────────────────────────────────────
// regiontoneprimitives.cpp — soundingAt / pitchContextOverSpan
// ─────────────────────────────────────────────────────────────────────────────

// Oracle: soundingAt drops notes on an excluded staff, non-playing notes,
// invisible notes, and grace notes.
TEST(Composing_EngravingBridgeBranchTests, EB_SoundingAt_ExcludedNonPlayingInvisibleGraceDropped)
{
    // Excluded staff.
    {
        MasterScore* sc = ScoreRW::readScore(u"data/nm_two_staff.mscx");
        ASSERT_TRUE(sc);
        const NoteModel model = NoteModel::build(sc);

        std::vector<ebr::SoundingNote> all;
        ebr::soundingAt(model, 0, kNoExclude, all);
        EXPECT_EQ(all.size(), 2u) << "both staves sound C5 and C3";

        std::vector<ebr::SoundingNote> excl;
        ebr::soundingAt(model, 0, { 1 }, excl);
        ASSERT_EQ(excl.size(), 1u) << "staff 1 excluded -> only C5";
        EXPECT_EQ(excl.front().ppitch, 72);
        delete sc;
    }

    // Non-playing + invisible.
    {
        MasterScore* sc = ScoreRW::readScore(u"data/nm_flags.mscx");
        ASSERT_TRUE(sc);
        const NoteModel model = NoteModel::build(sc);

        std::vector<ebr::SoundingNote> out;
        ebr::soundingAt(model, 0, kNoExclude, out);
        std::set<int> pitches;
        for (const auto& sn : out) {
            pitches.insert(sn.ppitch);
        }
        EXPECT_TRUE(pitches.count(60)) << "C4 kept";
        EXPECT_TRUE(pitches.count(64)) << "E4 kept";
        EXPECT_FALSE(pitches.count(67)) << "invisible G4 dropped";
        EXPECT_FALSE(pitches.count(71)) << "non-playing cue B4 dropped";
        delete sc;
    }

    // Grace note (a NoteModel grace event, flagged isGrace).
    {
        MasterScore* sc = ScoreRW::readScore(u"data/nm_grace.mscx");
        ASSERT_TRUE(sc);
        const NoteModel model = NoteModel::build(sc);

        std::vector<ebr::SoundingNote> out;
        ebr::soundingAt(model, 0, kNoExclude, out);
        std::set<int> pitches;
        for (const auto& sn : out) {
            pitches.insert(sn.ppitch);
        }
        EXPECT_FALSE(pitches.count(79)) << "grace G5 dropped from the sounding view";
        EXPECT_TRUE(pitches.count(60) && pitches.count(64) && pitches.count(67))
            << "the main chord C4-E4-G4 is kept";
        delete sc;
    }
}

// Oracle: pitchContextOverSpan drops invisible notes and notes on an excluded staff.
TEST(Composing_EngravingBridgeBranchTests, EB_PitchContextOverSpan_InvisibleAndExcludedDropped)
{
    // Invisible note dropped (nm_flags: G4 invisible, B4 non-playing).
    {
        MasterScore* sc = ScoreRW::readScore(u"data/nm_flags.mscx");
        ASSERT_TRUE(sc);
        const NoteModel model = NoteModel::build(sc);

        std::vector<PitchContext> out;
        ebr::pitchContextOverSpan(model, 0, 1920, 0, 480, kNoExclude,
                                  kDefaultKeyModeAnalyzerPreferences, ebr::SpanWindowWeights{}, out);
        EXPECT_TRUE(hasPitchContextPitch(out, 60)) << "C4 kept";
        EXPECT_TRUE(hasPitchContextPitch(out, 64)) << "E4 kept";
        EXPECT_FALSE(hasPitchContextPitch(out, 67)) << "invisible G4 dropped";
        EXPECT_FALSE(hasPitchContextPitch(out, 71)) << "non-playing B4 dropped";
        delete sc;
    }

    // Excluded staff dropped (nm_two_staff: C5 staff 0, C3 staff 1).
    {
        MasterScore* sc = ScoreRW::readScore(u"data/nm_two_staff.mscx");
        ASSERT_TRUE(sc);
        const NoteModel model = NoteModel::build(sc);

        std::vector<PitchContext> out;
        ebr::pitchContextOverSpan(model, 0, 1920, 0, 1920, { 1 },
                                  kDefaultKeyModeAnalyzerPreferences, ebr::SpanWindowWeights{}, out);
        EXPECT_TRUE(hasPitchContextPitch(out, 72)) << "staff-0 C5 kept";
        EXPECT_FALSE(hasPitchContextPitch(out, 48)) << "staff-1 C3 dropped (excluded)";
        delete sc;
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// regiontoneprimitives.cpp — sub-boundary detectors
// ─────────────────────────────────────────────────────────────────────────────

// Oracle: an ineligible (chord-track) staff contributes nothing to onset-set
// detection, so the detector's output is identical whether that staff is reached
// via the !staffIsEligible guard (excludeStaves empty) or excluded explicitly.
// eb_steps: staff 0 = "Chord Track", staff 1 = four stepwise triads whose chord
// changes produce a single sub-boundary at tick 960.
TEST(Composing_EngravingBridgeBranchTests, EB_DetectOnsetSubBoundaries_IneligibleStaffExcluded)
{
    MasterScore* sc = ScoreRW::readScore(u"data/eb_steps.mscx");
    ASSERT_TRUE(sc);

    const auto viaIneligible =
        ebr::detectOnsetSubBoundaries(sc, Fraction::fromTicks(0), Fraction::fromTicks(1920), kNoExclude);
    const auto viaExclude =
        ebr::detectOnsetSubBoundaries(sc, Fraction::fromTicks(0), Fraction::fromTicks(1920), { 0 });

    ASSERT_EQ(viaIneligible.size(), 1u) << "one Jaccard sub-boundary from staff-1 chord changes";
    EXPECT_EQ(viaIneligible.front(), Fraction::fromTicks(960));
    EXPECT_EQ(viaIneligible, viaExclude)
        << "the chord-track staff is excluded by ineligibility, matching explicit exclusion";

    delete sc;
}

// Oracle: non-playing and invisible notes are excluded from the onset pitch-class
// set. nm_flags has a single onset whose only eligible notes are C4 + E4 (G4
// invisible, B4 non-playing), which is a single onset window -> no sub-boundary.
TEST(Composing_EngravingBridgeBranchTests, EB_DetectOnsetSubBoundaries_NonPlayingInvisibleFiltered)
{
    MasterScore* sc = ScoreRW::readScore(u"data/nm_flags.mscx");
    ASSERT_TRUE(sc);

    const auto boundaries =
        ebr::detectOnsetSubBoundaries(sc, Fraction::fromTicks(0), Fraction::fromTicks(1920), kNoExclude);
    EXPECT_TRUE(boundaries.empty())
        << "after filtering the non-playing/invisible notes only one onset remains";

    delete sc;
}

// Oracle: an ineligible (chord-track) staff contributes nothing to bass-movement
// detection. eb_steps staff-1 basses move C->D->E->F; the single accepted bass
// change (past the 2-beat minimum gap) lands at tick 960.
TEST(Composing_EngravingBridgeBranchTests, EB_DetectBassMovementSubBoundaries_IneligibleStaffExcluded)
{
    MasterScore* sc = ScoreRW::readScore(u"data/eb_steps.mscx");
    ASSERT_TRUE(sc);

    const auto viaIneligible =
        ebr::detectBassMovementSubBoundaries(sc, Fraction::fromTicks(0), Fraction::fromTicks(1920), kNoExclude);
    const auto viaExclude =
        ebr::detectBassMovementSubBoundaries(sc, Fraction::fromTicks(0), Fraction::fromTicks(1920), { 0 });

    ASSERT_EQ(viaIneligible.size(), 1u) << "one bass-movement sub-boundary from staff-1";
    EXPECT_EQ(viaIneligible.front(), Fraction::fromTicks(960));
    EXPECT_EQ(viaIneligible, viaExclude)
        << "the chord-track staff is excluded by ineligibility, matching explicit exclusion";

    delete sc;
}

// Oracle: non-playing and invisible notes are excluded when picking the bass.
// nm_flags: the lowest eligible note is C4 (G4 invisible, B4 non-playing); one
// onset -> no bass-movement sub-boundary.
TEST(Composing_EngravingBridgeBranchTests, EB_DetectBassMovementSubBoundaries_NonPlayingInvisibleFiltered)
{
    MasterScore* sc = ScoreRW::readScore(u"data/nm_flags.mscx");
    ASSERT_TRUE(sc);

    const auto boundaries =
        ebr::detectBassMovementSubBoundaries(sc, Fraction::fromTicks(0), Fraction::fromTicks(1920), kNoExclude);
    EXPECT_TRUE(boundaries.empty())
        << "after filtering the non-playing/invisible notes only one onset remains";

    delete sc;
}

// ─────────────────────────────────────────────────────────────────────────────
// regiontoneprimitives.cpp — findTemporalContext
// ─────────────────────────────────────────────────────────────────────────────

// Oracle: at an interior segment the bridge temporal context is built from both
// neighbours, with bassIsStepwiseFromPrevious / ToNext set from the diatonic-step
// relation of the neighbour basses to the current bass. eb_steps staff 1 moves
// C(0)->D(2)->E(4)->F(5); the chord-track staff 0 is scanned (and skipped) by the
// hasAttacks loop on both the backward and forward walks.
TEST(Composing_EngravingBridgeBranchTests, EB_FindTemporalContext_StepwiseBassBothDirections)
{
    MasterScore* sc = ScoreRW::readScore(u"data/eb_steps.mscx");
    ASSERT_TRUE(sc);
    const NoteModel model = NoteModel::build(sc);

    const Segment* seg = chordRestSegAt(sc, 480);   // the D-triad
    ASSERT_TRUE(seg);

    const int currentBassPc = 2;   // D
    const ChordTemporalContext ctx =
        ebr::findTemporalContext(model, seg, kNoExclude, /*keyFifths=*/0, KeySigMode::Ionian, currentBassPc);

    ASSERT_NE(ctx.previousBassPc, -1) << "the C-triad backward neighbour was analysed";
    ASSERT_NE(ctx.nextBassPc, -1) << "the E-triad forward neighbour was analysed";
    EXPECT_EQ(ctx.previousBassPc, 0) << "the previous bass is C";
    EXPECT_EQ(ctx.nextBassPc, 4) << "the next bass is E";
    // The flag logic IS the branch under test: it must equal the diatonic-step oracle.
    EXPECT_EQ(ctx.bassIsStepwiseFromPrevious, isDiatonicStep(ctx.previousBassPc, currentBassPc));
    EXPECT_EQ(ctx.bassIsStepwiseToNext, isDiatonicStep(currentBassPc, ctx.nextBassPc));
    EXPECT_TRUE(ctx.bassIsStepwiseFromPrevious) << "C->D is a diatonic step";
    EXPECT_TRUE(ctx.bassIsStepwiseToNext) << "D->E is a diatonic step";

    delete sc;
}

// Oracle: at the first segment there is no backward neighbour, so previousBassPc
// stays -1 and bassIsStepwiseFromPrevious is false (the currentBassPc-known guard
// short-circuits on the absent previous bass).
TEST(Composing_EngravingBridgeBranchTests, EB_FindTemporalContext_NoPreviousContext)
{
    MasterScore* sc = ScoreRW::readScore(u"data/eb_steps.mscx");
    ASSERT_TRUE(sc);
    const NoteModel model = NoteModel::build(sc);

    const Segment* seg = chordRestSegAt(sc, 0);   // the first (C) triad
    ASSERT_TRUE(seg);

    const ChordTemporalContext ctx =
        ebr::findTemporalContext(model, seg, kNoExclude, /*keyFifths=*/0, KeySigMode::Ionian, /*currentBassPc=*/0);

    EXPECT_EQ(ctx.previousBassPc, -1) << "no backward ChordRest at the piece start";
    EXPECT_FALSE(ctx.bassIsStepwiseFromPrevious) << "no previous bass -> flag stays false";
    EXPECT_NE(ctx.nextBassPc, -1) << "the forward neighbour (D) is still found";

    delete sc;
}

// Oracle: at the last segment there is no forward neighbour (end of score), so
// nextBassPc stays -1 and bassIsStepwiseToNext is false.
TEST(Composing_EngravingBridgeBranchTests, EB_FindTemporalContext_EndOfScoreNoForwardContext)
{
    MasterScore* sc = ScoreRW::readScore(u"data/eb_steps.mscx");
    ASSERT_TRUE(sc);
    const NoteModel model = NoteModel::build(sc);

    const Segment* seg = chordRestSegAt(sc, 1440);   // the last (F) triad
    ASSERT_TRUE(seg);

    const ChordTemporalContext ctx =
        ebr::findTemporalContext(model, seg, kNoExclude, /*keyFifths=*/0, KeySigMode::Ionian, /*currentBassPc=*/5);

    EXPECT_EQ(ctx.nextBassPc, -1) << "no forward ChordRest at the end of the score";
    EXPECT_FALSE(ctx.bassIsStepwiseToNext) << "no next bass -> flag stays false";
    EXPECT_NE(ctx.previousBassPc, -1) << "the backward neighbour (E) is still found";

    delete sc;
}
