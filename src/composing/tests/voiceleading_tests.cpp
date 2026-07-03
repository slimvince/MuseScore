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

// voiceleading_tests.cpp — AXIS 2 (VOICE LEADING), the dormant foundation build.
//
// Oracle-asserted against cowork_voiceleading_axis_design.md (SIGNED 2026-07-03):
//   VL-A §5.1 — partition / losslessness / round-trip / tie inheritance / chordal
//     grouping / declared top-note reduction / profile eligibility.
//   VL-B §5.2/§0 — the four motion types + both-static drop + holds + chordal
//     reduction (hand fixtures, oracle by construction) + the §15-2 SEMITONE-EXACT
//     parallel convention; interval histogram bins + repeat/step/leap rates.
//   VL-C §5.3 — buildFeature order; at-centroid / margin-floor / fit-floor / no-pair /
//     too-few abstention; ranked-list completeness + ordering + weights; squash [0,1];
//     determinism.
//   VL-C requester §8 — whole-score inertness, must-fire, must-not-fire (cue cleared),
//     hard-bound denial provenance, termination, determinism.

#include <gtest/gtest.h>

#include <algorithm>
#include <array>
#include <cmath>
#include <vector>

#include "engraving/dom/masterscore.h"
#include "engraving/types/fraction.h"
#include "engraving/tests/utils/scorerw.h"

#include "composing/analysis/notemodel/note_model.h"
#include "composing/analysis/voiceleading/voicelinearview.h"
#include "composing/analysis/voiceleading/voiceleadingprofiles.h"
#include "composing/analysis/voiceleading/textureclassifier.h"

using namespace mu::composing::analysis::voiceleading;
using mu::composing::analysis::notemodel::NoteEvent;
using mu::composing::analysis::notemodel::NoteModel;
using mu::engraving::Fraction;
using mu::engraving::MasterScore;
using mu::engraving::ScoreRW;

namespace {

// Build one Layer-1 NoteEvent (the plain-data fixture primitive).
NoteEvent ne(int pitch, int staff, int voice, int onset, int release,
             int tpc = -1, bool plays = true, bool visible = true, bool staffEligible = true,
             bool isGrace = false)
{
    NoteEvent e;
    e.pitch = pitch;
    e.tpc = tpc;
    e.staff = staff;
    e.voice = voice;
    e.onset = onset;
    e.release = release;
    e.duration = release - onset;
    e.plays = plays;
    e.visible = visible;
    e.staffEligible = staffEligible;
    e.isGrace = isGrace;
    return e;
}

bool sameNote(const NoteEvent& a, const NoteEvent& b)
{
    return a.pitch == b.pitch && a.tpc == b.tpc && a.staff == b.staff && a.voice == b.voice
           && a.onset == b.onset && a.release == b.release && a.duration == b.duration
           && a.isGrace == b.isGrace && a.plays == b.plays && a.visible == b.visible
           && a.staffEligible == b.staffEligible;
}

} // namespace

// ════════════════════════════════ VL-A ════════════════════════════════════════

// §5.1 — a partition: every note in exactly one line's events exactly once; the
// round-trip (view -> notes) reproduces the L1 content in build order.
TEST(VoiceLeadingViewA, PartitionAndRoundTrip)
{
    const std::vector<NoteEvent> notes{
        ne(60, 0, 0, 0, 480), ne(64, 0, 1, 0, 480),          // two voices, staff 0
        ne(62, 0, 0, 480, 960), ne(65, 0, 1, 480, 960),
        ne(48, 1, 0, 0, 960),                                 // staff 1
    };
    const VoiceLinearView view = buildVoiceLinearView(notes);

    // three (staff,voice) lines, sorted.
    ASSERT_EQ(view.lines.size(), 3u);
    EXPECT_EQ(view.lines[0].staff, 0); EXPECT_EQ(view.lines[0].voice, 0);
    EXPECT_EQ(view.lines[1].staff, 0); EXPECT_EQ(view.lines[1].voice, 1);
    EXPECT_EQ(view.lines[2].staff, 1); EXPECT_EQ(view.lines[2].voice, 0);

    // total member count == input count (nothing dropped/merged).
    std::size_t members = 0;
    for (const VoiceLine& l : view.lines) {
        for (const VoiceEvent& e : l.events) { members += e.notes.size(); }
    }
    EXPECT_EQ(members, notes.size());

    // round-trip: flatten reproduces the L1 CONTENT of the span (§5.1 — a partition,
    // so the multiset is preserved; the view is (staff,voice,onset)-grouped rather than
    // the model's global onset order, which is content-equivalent). Sort both by a
    // canonical key and compare element-wise.
    std::vector<NoteEvent> back = flattenToNotes(view);
    std::vector<NoteEvent> in = notes;
    ASSERT_EQ(back.size(), in.size());
    auto keyLess = [](const NoteEvent& a, const NoteEvent& b) {
        if (a.staff != b.staff) { return a.staff < b.staff; }
        if (a.voice != b.voice) { return a.voice < b.voice; }
        if (a.onset != b.onset) { return a.onset < b.onset; }
        return a.pitch < b.pitch;
    };
    std::sort(back.begin(), back.end(), keyLess);
    std::sort(in.begin(), in.end(), keyLess);
    for (std::size_t i = 0; i < in.size(); ++i) {
        EXPECT_TRUE(sameNote(back[i], in[i])) << "note " << i;
    }
}

// §5.1 — chordal voices are a recorded fact: same (staff,voice,onset) -> one chordal
// event; distinct onsets -> separate non-chordal events.
TEST(VoiceLeadingViewA, ChordalGrouping)
{
    const std::vector<NoteEvent> notes{
        ne(60, 0, 0, 0, 480), ne(64, 0, 0, 0, 480), ne(67, 0, 0, 0, 480),   // a triad chord
        ne(72, 0, 0, 480, 960),                                             // a single note
    };
    const VoiceLinearView view = buildVoiceLinearView(notes);
    ASSERT_EQ(view.lines.size(), 1u);
    ASSERT_EQ(view.lines[0].events.size(), 2u);
    EXPECT_TRUE(view.lines[0].events[0].chordal);
    EXPECT_EQ(view.lines[0].events[0].notes.size(), 3u);
    EXPECT_FALSE(view.lines[0].events[1].chordal);
    EXPECT_EQ(view.lines[0].events[1].notes.size(), 1u);
}

// §5.1 — tie inheritance: L1 resolves a tied group into ONE sounding event with the
// last note's release; the view inherits that span (one event, long release).
TEST(VoiceLeadingViewA, TieResolvedSpanInherited)
{
    const std::vector<NoteEvent> notes{ ne(60, 0, 0, 0, 1920) };   // a tie-resolved whole note
    const VoiceLinearView view = buildVoiceLinearView(notes);
    ASSERT_EQ(view.lines.size(), 1u);
    ASSERT_EQ(view.lines[0].events.size(), 1u);
    EXPECT_EQ(view.lines[0].events[0].onset, 0);
    ASSERT_EQ(view.lines[0].events[0].notes.size(), 1u);
    EXPECT_EQ(view.lines[0].events[0].notes[0].release, 1920);
}

// §5.1 — declared per-query TOP-NOTE reduction; skips non-eligible members; nullopt
// when no member is profile-eligible. The lossless view keeps every member either way.
TEST(VoiceLeadingViewA, TopNoteReductionAndEligibility)
{
    // chord {60, 64, 67} all eligible -> top 67.
    {
        VoiceEvent e; e.onset = 0;
        e.notes = { {60,-1,480,480,false,true,true,true}, {64,-1,480,480,false,true,true,true},
                    {67,-1,480,480,false,true,true,true} };
        const std::optional<int> r = reducedPitch(e);
        ASSERT_TRUE(r.has_value());
        EXPECT_EQ(*r, 67);
    }
    // the top pitch is staff-INELIGIBLE -> reduction falls to the next eligible (64).
    {
        VoiceEvent e; e.onset = 0;
        VoiceNote hi; hi.pitch = 67; hi.staffEligible = false;   // ineligible top
        e.notes = { {60,-1,480,480,false,true,true,true}, {64,-1,480,480,false,true,true,true}, hi };
        EXPECT_FALSE(isProfileEligible(hi));
        const std::optional<int> r = reducedPitch(e);
        ASSERT_TRUE(r.has_value());
        EXPECT_EQ(*r, 64);
    }
    // all members ineligible -> nullopt.
    {
        VoiceEvent e; e.onset = 0;
        VoiceNote n; n.pitch = 60; n.plays = false;
        e.notes = { n };
        EXPECT_FALSE(reducedPitch(e).has_value());
    }
}

// The lossless view retains non-playing / grace / ineligible notes (nothing dropped),
// even though they are excluded from PROFILE queries.
TEST(VoiceLeadingViewA, LosslessKeepsIneligible)
{
    const std::vector<NoteEvent> notes{
        ne(60, 0, 0, 0, 480),
        ne(61, 0, 0, 0, 480, -1, /*plays*/false),                 // muted — kept, flagged
        ne(62, 0, 0, 240, 480, -1, true, true, true, /*grace*/true), // grace — kept, flagged
    };
    const VoiceLinearView view = buildVoiceLinearView(notes);
    EXPECT_EQ(flattenToNotes(view).size(), 3u);
}

// ════════════════════════════════ VL-B ════════════════════════════════════════

// §0 — the four motion types + the both-static drop, oracle by construction.
TEST(VoiceLeadingProfilesB, ClassifyMotionAllTypes)
{
    MotionType m;
    // parallel — same direction, harmonic interval preserved (both +2; -4 -> -4).
    EXPECT_TRUE(classifyMotion(60, 62, 64, 66, m)); EXPECT_EQ(m, MotionType::Parallel);
    // similar — same direction, interval changes (u+4, v+1).
    EXPECT_TRUE(classifyMotion(60, 64, 64, 65, m)); EXPECT_EQ(m, MotionType::Similar);
    // contrary — opposite directions.
    EXPECT_TRUE(classifyMotion(60, 62, 64, 62, m)); EXPECT_EQ(m, MotionType::Contrary);
    // oblique — exactly one voice moves.
    EXPECT_TRUE(classifyMotion(60, 60, 64, 66, m)); EXPECT_EQ(m, MotionType::Oblique);
    // both static -> dropped (returns false, m untouched).
    EXPECT_FALSE(classifyMotion(60, 60, 64, 64, m));
}

// §15-2 — the "parallel" convention is SEMITONE-EXACT (voiceleading2._motion:
// (pu1-pv1)==(pu0-pv0)). A move both voices "up" that a GENERIC reading would call
// parallel (both up a scale step) is SIMILAR when the semitone interval changes.
TEST(VoiceLeadingProfilesB, ParallelIsSemitoneExactNotGeneric)
{
    MotionType m;
    // u: 60->61 (+1 semitone), v: 67->69 (+2 semitones). Same direction, but -7 -> -8:
    // the semitone interval changed -> SIMILAR (generic "both up" would be parallel).
    EXPECT_TRUE(classifyMotion(60, 61, 67, 69, m));
    EXPECT_EQ(m, MotionType::Similar);
    // u: 60->62, v: 67->69 (both +2, interval -7 preserved) -> PARALLEL.
    EXPECT_TRUE(classifyMotion(60, 62, 67, 69, m));
    EXPECT_EQ(m, MotionType::Parallel);
}

// §5.2 — motion profile over a two-voice view: rates, sample count, and the exposed
// per-sample motion-event series (with the two harmonic intervals).
TEST(VoiceLeadingProfilesB, MotionProfileAndEvents)
{
    const std::vector<NoteEvent> notes{
        ne(60, 0, 0, 0, 480),   ne(64, 0, 1, 0, 480),
        ne(62, 0, 0, 480, 960), ne(64, 0, 1, 480, 960),
        ne(64, 0, 0, 960, 1440), ne(66, 0, 1, 960, 1440),
    };
    const VoiceLinearView view = buildVoiceLinearView(notes);
    std::vector<MotionEvent> events;
    const MotionProfile p = computeMotionProfile(view, &events);

    EXPECT_EQ(p.eligibleVoiceCount, 2);
    EXPECT_EQ(p.voicePairCount, 1);
    EXPECT_EQ(p.sampleCount, 2);          // oblique @480, parallel @960
    EXPECT_FALSE(p.defined);              // 2 < 8
    EXPECT_DOUBLE_EQ(p.oblique, 0.5);
    EXPECT_DOUBLE_EQ(p.parallel, 0.5);
    EXPECT_DOUBLE_EQ(p.similar, 0.0);
    EXPECT_DOUBLE_EQ(p.contrary, 0.0);

    ASSERT_EQ(events.size(), 2u);
    EXPECT_EQ(events[0].type, MotionType::Oblique);
    EXPECT_EQ(events[0].sampleTick, 480);
    EXPECT_EQ(events[0].harmonicIntervalBefore, 60 - 64);   // -4
    EXPECT_EQ(events[0].harmonicIntervalAfter, 62 - 64);    // -2
    EXPECT_EQ(events[1].type, MotionType::Parallel);
    EXPECT_EQ(events[1].sampleTick, 960);
    EXPECT_EQ(events[1].harmonicIntervalBefore, 62 - 64);   // -2
    EXPECT_EQ(events[1].harmonicIntervalAfter, 64 - 66);    // -2
}

// §0 — piecewise-constant HOLD: a voice with sparse onsets holds its last pitch across
// the other voice's onsets (bisect: most-recent onset <= t).
TEST(VoiceLeadingProfilesB, HoldSampling)
{
    const std::vector<NoteEvent> notes{
        ne(60, 0, 0, 0, 240),   ne(67, 0, 1, 0, 480),   // B holds 67 across A's 240/480
        ne(62, 0, 0, 240, 480),
        ne(64, 0, 0, 480, 720), ne(67, 0, 1, 480, 720),
    };
    const VoiceLinearView view = buildVoiceLinearView(notes);
    const MotionProfile p = computeMotionProfile(view, nullptr);
    EXPECT_EQ(p.sampleCount, 2);          // 60->62 and 62->64 over held 67
    EXPECT_DOUBLE_EQ(p.oblique, 1.0);     // both are oblique (B static, held)
}

// §0 — a both-static sample between two moving samples is DROPPED from the count.
TEST(VoiceLeadingProfilesB, BothStaticDropped)
{
    const std::vector<NoteEvent> notes{
        ne(60, 0, 0, 0, 240),   ne(67, 0, 1, 0, 240),
        ne(60, 0, 0, 240, 480), ne(67, 0, 1, 240, 480),   // both static @240 -> dropped
        ne(64, 0, 0, 480, 720), ne(69, 0, 1, 480, 720),   // moves @480
    };
    const VoiceLinearView view = buildVoiceLinearView(notes);
    const MotionProfile p = computeMotionProfile(view, nullptr);
    EXPECT_EQ(p.sampleCount, 1);          // only the @480 motion counts
    EXPECT_DOUBLE_EQ(p.similar, 1.0);     // 60->64 (+4), 67->69 (+2): -7 -> -5 changed
}

// §5.2 — a chordal voice is reduced to its TOP note for the motion profile.
TEST(VoiceLeadingProfilesB, ChordalReducedToTopNote)
{
    const std::vector<NoteEvent> notes{
        ne(48, 0, 0, 0, 480),  ne(60, 0, 0, 0, 480),      // chord {48,60} -> top 60
        ne(64, 0, 1, 0, 480),
        ne(50, 0, 0, 480, 960), ne(62, 0, 0, 480, 960),   // chord {50,62} -> top 62
        ne(64, 0, 1, 480, 960),
    };
    const VoiceLinearView view = buildVoiceLinearView(notes);
    std::vector<MotionEvent> events;
    const MotionProfile p = computeMotionProfile(view, &events);
    ASSERT_EQ(events.size(), 1u);
    // top-note line A: 60->62 (+2); line B static -> oblique.
    EXPECT_EQ(events[0].type, MotionType::Oblique);
    EXPECT_EQ(events[0].harmonicIntervalBefore, 60 - 64);
}

// §5.2 — interval histogram bins + repeat/step/leap rates (== vl_profile arithmetic).
TEST(VoiceLeadingProfilesB, IntervalProfileBinsAndRates)
{
    // one voice: 60,60,62,65,60 -> |iv| = 0,2,3,5.
    const std::vector<NoteEvent> notes{
        ne(60, 0, 0, 0, 240), ne(60, 0, 0, 240, 480), ne(62, 0, 0, 480, 720),
        ne(65, 0, 0, 720, 960), ne(60, 0, 0, 960, 1200),
    };
    const VoiceLinearView view = buildVoiceLinearView(notes);
    const IntervalProfile ip = computeIntervalProfileAggregate(view);
    EXPECT_EQ(ip.intervalCount, 4);
    EXPECT_FALSE(ip.defined);                 // 4 < 8
    EXPECT_DOUBLE_EQ(ip.hist[0], 0.25);       // one |0|
    EXPECT_DOUBLE_EQ(ip.hist[2], 0.25);       // one |2|
    EXPECT_DOUBLE_EQ(ip.hist[3], 0.25);       // one |3|
    EXPECT_DOUBLE_EQ(ip.hist[5], 0.25);       // one |5|
    EXPECT_DOUBLE_EQ(ip.repeat, 0.25);        // |0|
    EXPECT_DOUBLE_EQ(ip.step, 0.25);          // |2| (1..2)
    EXPECT_DOUBLE_EQ(ip.leap, 0.50);          // |3|,|5| (>2)
}

// §5.2 — >= 8 intervals -> defined; all semitone steps -> step rate 1.0, hist[1]=1.0.
TEST(VoiceLeadingProfilesB, IntervalProfileDefinedThreshold)
{
    std::vector<NoteEvent> notes;
    for (int i = 0; i < 9; ++i) { notes.push_back(ne(60 + i, 0, 0, i * 240, (i + 1) * 240)); }
    const VoiceLinearView view = buildVoiceLinearView(notes);
    const IntervalProfile ip = computeIntervalProfileAggregate(view);
    EXPECT_EQ(ip.intervalCount, 8);
    EXPECT_TRUE(ip.defined);
    EXPECT_DOUBLE_EQ(ip.hist[1], 1.0);
    EXPECT_DOUBLE_EQ(ip.step, 1.0);
}

// ════════════════════════════════ VL-C ════════════════════════════════════════

namespace {

// The 20-d feature whose z-score equals class k's reference centroid (an at-centroid
// sample): feat = mean + std * centroidZ[k].
std::array<double, kVlFeatureDim> featForClass(int k)
{
    std::array<double, kVlFeatureDim> f{};
    for (std::size_t d = 0; d < kVlFeatureDim; ++d) {
        f[d] = kVlRefMean[d] + kVlRefStd[d] * kVlRefCentroidZ[static_cast<std::size_t>(k)][d];
    }
    return f;
}

// Split a raw 20-d feature into a (defined) motion + interval profile pair.
void featToProfiles(const std::array<double, kVlFeatureDim>& f, MotionProfile& m, IntervalProfile& iv,
                    int samples = 100)
{
    for (int k = 0; k < 13; ++k) { iv.hist[static_cast<std::size_t>(k)] = f[static_cast<std::size_t>(k)]; }
    iv.repeat = f[13]; iv.step = f[14]; iv.leap = f[15];
    iv.intervalCount = samples; iv.defined = true;
    m.parallel = f[16]; m.similar = f[17]; m.contrary = f[18]; m.oblique = f[19];
    m.sampleCount = samples; m.eligibleVoiceCount = 2; m.voicePairCount = 1; m.defined = true;
}

} // namespace

// §5.3 — the 20-d feature is interval(16) then motion(4), in the reference order.
TEST(VoiceLeadingClassifierC, BuildFeatureOrder)
{
    MotionProfile m; IntervalProfile iv;
    for (int k = 0; k < 13; ++k) { iv.hist[static_cast<std::size_t>(k)] = 0.1 * k; }
    iv.repeat = 1.0; iv.step = 2.0; iv.leap = 3.0;
    m.parallel = 4.0; m.similar = 5.0; m.contrary = 6.0; m.oblique = 7.0;
    const std::array<double, kVlFeatureDim> f = buildFeature(m, iv);
    EXPECT_DOUBLE_EQ(f[0], 0.0); EXPECT_DOUBLE_EQ(f[12], 1.2);
    EXPECT_DOUBLE_EQ(f[13], 1.0); EXPECT_DOUBLE_EQ(f[14], 2.0); EXPECT_DOUBLE_EQ(f[15], 3.0);
    EXPECT_DOUBLE_EQ(f[16], 4.0); EXPECT_DOUBLE_EQ(f[17], 5.0);
    EXPECT_DOUBLE_EQ(f[18], 6.0); EXPECT_DOUBLE_EQ(f[19], 7.0);
}

// §5.3 — an at-centroid feature commits to that class with a healthy margin; the full
// ranked list of ALL four classes is carried, fit-descending, weights summing to 1.
TEST(VoiceLeadingClassifierC, AtCentroidCommitsAndRanksAll)
{
    for (int k = 0; k < kVlTextureClassCount; ++k) {
        MotionProfile m; IntervalProfile iv;
        featToProfiles(featForClass(k), m, iv);
        const VoiceLeadingSpan s = classifyTexture(m, iv, 0, 1920);
        EXPECT_FALSE(s.abstained) << "class " << k;
        EXPECT_EQ(static_cast<int>(s.committed), k);
        EXPECT_EQ(s.reason, AbstentionReason::None);
        ASSERT_EQ(s.ranked.size(), 4u);
        EXPECT_EQ(static_cast<int>(s.ranked.front().cls), k);
        EXPECT_NEAR(s.ranked.front().fit, 1.0, 1e-6);           // distance ~0 -> fit ~1
        // fit-descending
        for (std::size_t i = 1; i < s.ranked.size(); ++i) {
            EXPECT_GE(s.ranked[i - 1].fit, s.ranked[i].fit);
        }
        // weights sum to 1
        double wsum = 0.0;
        for (const ClassFit& cf : s.ranked) { wsum += cf.weight; }
        EXPECT_NEAR(wsum, 1.0, 1e-9);
        // confidence in [0,1]
        EXPECT_GE(s.confidence, 0.0);
        EXPECT_LE(s.confidence, 1.0);
        EXPECT_GT(s.confidence, kVlMarginFloorDefault);
    }
}

// §5.3 — the MARGIN FLOOR: a near-tie (the midpoint of the two nearest centroids)
// abstains LowMargin while STILL carrying the full ranked list.
TEST(VoiceLeadingClassifierC, MarginFloorAbstainsNearTie)
{
    // midpoint of HomophonicClassical(1) and HomophonicPianistic(2) — the closest pair.
    std::array<double, kVlFeatureDim> f{};
    for (std::size_t d = 0; d < kVlFeatureDim; ++d) {
        const double zmid = 0.5 * (kVlRefCentroidZ[1][d] + kVlRefCentroidZ[2][d]);
        f[d] = kVlRefMean[d] + kVlRefStd[d] * zmid;
    }
    MotionProfile m; IntervalProfile iv;
    featToProfiles(f, m, iv);
    const VoiceLeadingSpan s = classifyTexture(m, iv, 0, 1920);
    EXPECT_TRUE(s.abstained);
    EXPECT_EQ(s.reason, AbstentionReason::LowMargin);
    ASSERT_EQ(s.ranked.size(), 4u);                            // zero information loss
    EXPECT_LT(s.confidence, kVlMarginFloorDefault);
    EXPECT_GE(s.ranked.front().fit, kVlFitFloorDefault);       // not a fit-floor case
}

// §5.3 — the FIT FLOOR: a feature far from ALL reference centroids abstains LowFit
// (resembles no class) rather than being forced to its nearest.
TEST(VoiceLeadingClassifierC, FitFloorAbstainsFarFromAll)
{
    std::array<double, kVlFeatureDim> f{};
    for (std::size_t d = 0; d < kVlFeatureDim; ++d) {
        f[d] = kVlRefMean[d] + kVlRefStd[d] * 100.0;           // z ~ 100 in every dim
    }
    MotionProfile m; IntervalProfile iv;
    featToProfiles(f, m, iv);
    const VoiceLeadingSpan s = classifyTexture(m, iv, 0, 1920);
    EXPECT_TRUE(s.abstained);
    EXPECT_EQ(s.reason, AbstentionReason::LowFit);
    ASSERT_EQ(s.ranked.size(), 4u);
    EXPECT_LT(s.ranked.front().fit, kVlFitFloorDefault);
}

// §5.3 — a single-voice selection has no voice pairs -> NO-PAIR abstention (never
// interval-only classification, v1). No ranked list is produced.
TEST(VoiceLeadingClassifierC, NoPairAbstains)
{
    MotionProfile m; m.eligibleVoiceCount = 1;                 // < 2 voices
    IntervalProfile iv; iv.defined = true; iv.intervalCount = 20;
    const VoiceLeadingSpan s = classifyTexture(m, iv, 0, 1920);
    EXPECT_TRUE(s.abstained);
    EXPECT_EQ(s.reason, AbstentionReason::NoPair);
    EXPECT_TRUE(s.ranked.empty());
}

// §5.3 — the EVIDENTIAL FLOOR / undefined interval profile -> TooFewSamples.
TEST(VoiceLeadingClassifierC, TooFewSamplesAbstains)
{
    {   // motion below the evidential floor
        MotionProfile m; m.eligibleVoiceCount = 2; m.sampleCount = 3; m.defined = false;
        IntervalProfile iv; iv.defined = true; iv.intervalCount = 20;
        const VoiceLeadingSpan s = classifyTexture(m, iv, 0, 1920);
        EXPECT_TRUE(s.abstained);
        EXPECT_EQ(s.reason, AbstentionReason::TooFewSamples);
    }
    {   // interval half undefined
        MotionProfile m; m.eligibleVoiceCount = 2; m.sampleCount = 100; m.defined = true;
        IntervalProfile iv; iv.defined = false; iv.intervalCount = 3;
        const VoiceLeadingSpan s = classifyTexture(m, iv, 0, 1920);
        EXPECT_TRUE(s.abstained);
        EXPECT_EQ(s.reason, AbstentionReason::TooFewSamples);
    }
}

// Determinism: identical input -> byte-identical output, twice.
TEST(VoiceLeadingClassifierC, Deterministic)
{
    MotionProfile m; IntervalProfile iv;
    featToProfiles(featForClass(0), m, iv);
    const VoiceLeadingSpan a = classifyTexture(m, iv, 0, 1920);
    const VoiceLeadingSpan b = classifyTexture(m, iv, 0, 1920);
    EXPECT_EQ(a.committed, b.committed);
    EXPECT_DOUBLE_EQ(a.confidence, b.confidence);
    ASSERT_EQ(a.ranked.size(), b.ranked.size());
    for (std::size_t i = 0; i < a.ranked.size(); ++i) {
        EXPECT_DOUBLE_EQ(a.ranked[i].fit, b.ranked[i].fit);
        EXPECT_EQ(a.ranked[i].cls, b.ranked[i].cls);
    }
}

// ═══════════════════════════ VL-C requester (§8) ══════════════════════════════

// §8 — WHOLE-SCORE INERTNESS: selection == score -> no cue can fire (loaded edges ARE
// the score bounds); the extending classify equals the direct classify, no truncation.
TEST(VoiceLeadingRequester, WholeScoreInert)
{
    MasterScore* score = ScoreRW::readScore(u"data/pb_chorale.mscx");
    ASSERT_NE(score, nullptr);
    const NoteModel whole = NoteModel::build(score);

    VlExtensionParams ext; ext.enableExtension = true;
    const VoiceLeadingSpan s = classifySelectionExtending(
        whole, whole.scoreStart(), whole.scoreEnd(), {}, ext);

    const VoiceLinearView v = buildVoiceLinearView(whole);
    const MotionProfile m = computeMotionProfile(v, nullptr);
    const IntervalProfile iv = computeIntervalProfileAggregate(v);
    const VoiceLeadingSpan direct = classifyTexture(m, iv, whole.scoreStart(), whole.scoreEnd());

    EXPECT_EQ(s.committed, direct.committed);
    EXPECT_EQ(s.abstained, direct.abstained);
    EXPECT_DOUBLE_EQ(s.confidence, direct.confidence);
    EXPECT_FALSE(s.clippedBySelectionEdge);
    EXPECT_FALSE(s.cueDenied);
    EXPECT_EQ(s.evidenceStartTick, whole.scoreStart());
    EXPECT_EQ(s.evidenceEndTick, whole.scoreEnd());
    delete score;
}

// A realistic chorale end-to-end: a 4-voice chorale classifies with >= 2 eligible
// voices and a defined motion profile (the axis runs on notated voices, §4).
TEST(VoiceLeadingRequester, ChoraleEndToEnd)
{
    MasterScore* score = ScoreRW::readScore(u"data/pb_chorale.mscx");
    ASSERT_NE(score, nullptr);
    const NoteModel whole = NoteModel::build(score);
    const VoiceLinearView v = buildVoiceLinearView(whole);
    const MotionProfile m = computeMotionProfile(v, nullptr);
    EXPECT_GE(m.eligibleVoiceCount, 2);
    EXPECT_GT(m.sampleCount, 0);
    delete score;
}

// §8 — MUST-FIRE: a short mid-piece selection forced below the evidential floor drives
// the requester to grow the loaded (evidence) span beyond the selection. Output range
// stays the SELECTION (§2 invariant).
TEST(VoiceLeadingRequester, MustFireGrowsEvidence)
{
    MasterScore* score = ScoreRW::readScore(u"data/reachback_anchor.mscx");
    ASSERT_NE(score, nullptr);
    const int selStart = 5760, selEnd = 7680;                 // bars 4-5 (Division 480, 4/4)
    const NoteModel model = NoteModel::build(score, selStart, selEnd);

    TextureClassifierParams p; p.evidentialFloor = 1000000;   // force perpetual starvation
    VlExtensionParams ext; ext.enableExtension = true; ext.maxSteps = 8;
    ext.incrementBars = 2; ext.ticksPerBar = 1920;
    const VoiceLeadingSpan s = classifySelectionExtending(model, selStart, selEnd, p, ext);

    EXPECT_TRUE(s.evidenceEndTick > selEnd || s.evidenceStartTick < selStart);   // grew
    EXPECT_EQ(s.startTick, selStart);                          // output = selection
    EXPECT_EQ(s.endTick, selEnd);
    delete score;
}

// §8 — MUST-NOT-FIRE: when the cue cannot fire (evidential floor 0), no extension
// happens — the evidence span equals the selection and nothing is denied.
TEST(VoiceLeadingRequester, MustNotFireWhenCueCleared)
{
    MasterScore* score = ScoreRW::readScore(u"data/reachback_anchor.mscx");
    ASSERT_NE(score, nullptr);
    const int selStart = 5760, selEnd = 7680;
    const NoteModel model = NoteModel::build(score, selStart, selEnd);

    TextureClassifierParams p; p.evidentialFloor = 0;         // sampleCount < 0 never -> cue clears
    VlExtensionParams ext; ext.enableExtension = true; ext.maxSteps = 8;
    const VoiceLeadingSpan s = classifySelectionExtending(model, selStart, selEnd, p, ext);

    EXPECT_EQ(s.evidenceStartTick, selStart);
    EXPECT_EQ(s.evidenceEndTick, selEnd);
    EXPECT_FALSE(s.cueDenied);
    delete score;
}

// §8 — HARD-BOUND DENIAL: perpetual starvation + a tiny step cap -> the loop stops at
// the hard bound with the cue still active and unloaded context remaining, so the
// output carries cue-denied + clipped provenance (honest truncation).
TEST(VoiceLeadingRequester, HardBoundDenialProvenance)
{
    MasterScore* score = ScoreRW::readScore(u"data/reachback_anchor.mscx");
    ASSERT_NE(score, nullptr);
    const int selStart = 5760, selEnd = 7680;
    const NoteModel model = NoteModel::build(score, selStart, selEnd);

    TextureClassifierParams p; p.evidentialFloor = 1000000;   // never satisfiable
    VlExtensionParams ext; ext.enableExtension = true; ext.maxSteps = 1;
    ext.incrementBars = 1; ext.ticksPerBar = 1920;            // one small step, far from bounds
    const VoiceLeadingSpan s = classifySelectionExtending(model, selStart, selEnd, p, ext);

    EXPECT_TRUE(s.cueDenied);
    EXPECT_TRUE(s.clippedBySelectionEdge);
    EXPECT_TRUE(s.evidenceEndTick > selEnd || s.evidenceStartTick < selStart);   // one step happened
    delete score;
}

// §8 — DORMANT default (extension OFF): the requester never calls extend(); a starved
// mid-piece selection carries clipped provenance but no growth and no denial.
TEST(VoiceLeadingRequester, ExtensionOffNoGrowth)
{
    MasterScore* score = ScoreRW::readScore(u"data/reachback_anchor.mscx");
    ASSERT_NE(score, nullptr);
    const int selStart = 5760, selEnd = 7680;
    const NoteModel model = NoteModel::build(score, selStart, selEnd);

    TextureClassifierParams p; p.evidentialFloor = 1000000;
    VlExtensionParams ext;                                     // enableExtension defaults OFF
    const VoiceLeadingSpan s = classifySelectionExtending(model, selStart, selEnd, p, ext);

    EXPECT_EQ(s.evidenceStartTick, selStart);
    EXPECT_EQ(s.evidenceEndTick, selEnd);
    EXPECT_FALSE(s.cueDenied);                                 // no request was made
    delete score;
}

// Determinism of the requester: identical inputs -> identical result (byte-same fields).
TEST(VoiceLeadingRequester, Deterministic)
{
    MasterScore* score = ScoreRW::readScore(u"data/reachback_anchor.mscx");
    ASSERT_NE(score, nullptr);
    const int selStart = 5760, selEnd = 7680;
    const NoteModel model = NoteModel::build(score, selStart, selEnd);
    TextureClassifierParams p; p.evidentialFloor = 1000000;
    VlExtensionParams ext; ext.enableExtension = true; ext.maxSteps = 3;
    const VoiceLeadingSpan a = classifySelectionExtending(model, selStart, selEnd, p, ext);
    const VoiceLeadingSpan b = classifySelectionExtending(model, selStart, selEnd, p, ext);
    EXPECT_EQ(a.committed, b.committed);
    EXPECT_EQ(a.abstained, b.abstained);
    EXPECT_EQ(a.evidenceStartTick, b.evidenceStartTick);
    EXPECT_EQ(a.evidenceEndTick, b.evidenceEndTick);
    EXPECT_EQ(a.cueDenied, b.cueDenied);
    delete score;
}
