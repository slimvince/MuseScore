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
#pragma once

// ── composing/analysis/voiceleading — VL-B: MOTION & INTERVAL PROFILES (axis 2) ─
//
// The SECOND analysis axis (voice leading), foundation component VL-B. Spec:
// cowork_voiceleading_axis_design.md (SIGNED 2026-07-03) §5.2, §0. FACT layer —
// deterministic functions of the VL-A view; no tunable thresholds, no judgment, no
// confidence (§5.2). It reproduces EXACTLY the ratified study's two feature views
// (idiom_discovery/parsers/voiceleading.py `vl_profile` = View A / interval;
// voiceleading2.py `vl_profile_B` = View B / motion).
//
// MOTION PROFILE (View B), per the simultaneity rule (spec §0), aggregated over ALL
// concurrent voice pairs: for each pair, sample at the merged set of the two lines'
// onsets; a voice's pitch at a sample is its most recent onset at-or-before that time
// (piecewise-constant hold); classify the motion between consecutive samples, DROPPING
// samples where neither voice moves; rates length-normalized over all pairs.
//
// THE "PARALLEL" INTERVAL-PRESERVATION CONVENTION (spec §15-2 — the declaration owed
// at build): SEMITONE-EXACT. Read at source from voiceleading2.py `_motion`:
// `parallel` iff both voices move the same direction AND `(pu1 - pv1) == (pu0 - pv0)`
// — the SIGNED pitch difference in semitones is preserved exactly (NOT generic diatonic
// size). `similar` = same direction, semitone interval changes. This closes §15-2.
//
// THE PER-SAMPLE MOTION-EVENT SERIES is part of the export, not only the rates (§5.2):
// a MotionEvent carries the pair, the sample tick, the type, and the two harmonic
// intervals before/after — the facts a future part-writing checker (VL-H) needs (a
// parallel fifth/octave is parallel motion at a perfect harmonic interval at a specific
// event). Cheap to expose at build, structural to retrofit.
//
// INTERVAL PROFILE (View A), per voice + aggregable: the |interval|-in-semitones
// histogram (bins 0..11, >=12) plus repeat/step/leap rates (repeat=0, step=1..2,
// leap>=3 semitones). The AGGREGATE pools every eligible line's consecutive |intervals|
// into ONE histogram — exactly `vl_profile`'s computation (not a mean of per-voice
// rates).
//
// STUDY-PINNED FEATURE-DEFINITION MINIMUMS (NOT calibration): a profile is `defined`
// only at >= 8 events (`vl_profile` returns None at < 8 intervals; `vl_profile_B` at
// < 8 motions, min_events=8). These are part of what "the same feature" means.
//
// REDUCTION: chordal events are reduced to one line pitch by the declared VL-A rule
// (default TopNote, spec §5.2). The reduction rides the profile's provenance.
//
// DORMANT: no production consumer (see voicelinearview.h).

#include <array>
#include <utility>
#include <vector>

#include "composing/analysis/voiceleading/voicelinearview.h"

namespace mu::composing::analysis::voiceleading {

// The four standard counterpoint motion types (spec §0). Both-static samples are not
// a type — they are DROPPED (classifyMotion returns false).
enum class MotionType { Parallel, Similar, Contrary, Oblique };

// Study-pinned feature-definition minimums (voiceleading.py / voiceleading2.py).
inline constexpr int kMinIntervals = 8;      ///< vl_profile: < 8 intervals -> undefined
inline constexpr int kMinMotionEvents = 8;   ///< vl_profile_B: min_events=8 total motions

/// One classified per-sample motion event (spec §5.2 — a fact, exposed alongside the
/// rates). The pair is (lower-line u, higher-line v) in (staff, voice) order; the
/// harmonic interval is the SIGNED semitone difference pitchU - pitchV (the quantity
/// the semitone-exact parallel test compares).
struct MotionEvent {
    int staffU = 0, voiceU = 0;          ///< line u (the lower-indexed line of the pair)
    int staffV = 0, voiceV = 0;          ///< line v (the higher-indexed line)
    int sampleTick = 0;                  ///< the arrival sample tick t (of `after`)
    MotionType type = MotionType::Oblique;
    int harmonicIntervalBefore = 0;      ///< pitchU - pitchV at the previous sample
    int harmonicIntervalAfter = 0;       ///< pitchU - pitchV at this sample
};

/// The voice-pair motion-type rates of a span (View B). Length-normalized over all
/// pairs; `sampleCount` is the total classified motions; `defined` iff
/// sampleCount >= kMinMotionEvents.
struct MotionProfile {
    double parallel = 0.0;
    double similar = 0.0;
    double contrary = 0.0;
    double oblique = 0.0;
    int sampleCount = 0;                 ///< total classified motions across all pairs
    int eligibleVoiceCount = 0;          ///< # lines with >= 2 profile-eligible events (a pair needs 2)
    int voicePairCount = 0;              ///< # concurrent voice pairs aggregated
    ReductionRule reduction = ReductionRule::TopNote;
    bool defined = false;                ///< sampleCount >= kMinMotionEvents
};

/// The melodic-interval statistics of a span (View A). `hist[0..11]` = P(|iv|=k),
/// `hist[12]` = P(|iv|>=12). repeat=P(|iv|=0), step=P(1<=|iv|<=2), leap=P(|iv|>2).
/// `defined` iff intervalCount >= kMinIntervals.
struct IntervalProfile {
    std::array<double, 13> hist{};       ///< P(|iv|=0..11), then P(|iv|>=12)
    double repeat = 0.0;
    double step = 0.0;
    double leap = 0.0;
    int intervalCount = 0;
    bool defined = false;                ///< intervalCount >= kMinIntervals
};

/// One line's own interval profile (spec §5.2 "per voice").
struct VoiceIntervalProfile {
    int staff = 0;
    int voice = 0;
    IntervalProfile profile;
};

/// Classify the simultaneous motion of two voices from (pu0,pv0) to (pu1,pv1) — the
/// pure arithmetic of voiceleading2._motion (oracle by construction). Returns false
/// (and leaves @p out untouched) when NEITHER voice moves (the both-static drop);
/// otherwise sets @p out and returns true.
bool classifyMotion(int pu0, int pu1, int pv0, int pv1, MotionType& out);

/// Motion profile over all concurrent voice pairs of @p view (the simultaneity rule,
/// spec §0). If @p eventsOut is non-null, the full per-sample MotionEvent series is
/// appended to it (in pair-then-sample order). Deterministic; reduction default TopNote.
MotionProfile computeMotionProfile(const VoiceLinearView& view,
                                   std::vector<MotionEvent>* eventsOut = nullptr,
                                   ReductionRule rule = ReductionRule::TopNote);

/// Aggregate interval profile — pools every eligible line's consecutive |intervals|
/// into ONE histogram (== `vl_profile` over the reduced per-line sequences).
IntervalProfile computeIntervalProfileAggregate(const VoiceLinearView& view,
                                                ReductionRule rule = ReductionRule::TopNote);

/// Per-line interval profiles (each line's own histogram + rates).
std::vector<VoiceIntervalProfile> computeIntervalProfilesPerVoice(const VoiceLinearView& view,
                                                                  ReductionRule rule = ReductionRule::TopNote);

/// One line's reduced onset->pitch series (the View-A/B input, exposed for the
/// diagnostic dump + the study-parity harness).
struct ReducedLine {
    int staff = 0;
    int voice = 0;
    std::vector<std::pair<int, int>> onsets;   ///< (onset, top-pitch) over eligible events, ascending
};

/// The reduced per-line onset->pitch series over PROFILE-ELIGIBLE events, ascending
/// onset. Lines with fewer than two eligible events are OMITTED (the study's len>1
/// rule: `voices_onset` drops single-onset voices). Same order as the view's lines.
std::vector<ReducedLine> reducedOnsetSeries(const VoiceLinearView& view,
                                            ReductionRule rule = ReductionRule::TopNote);

} // namespace mu::composing::analysis::voiceleading
