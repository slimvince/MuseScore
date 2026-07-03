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

#include "composing/analysis/voiceleading/voiceleadingprofiles.h"

#include <algorithm>
#include <cstdlib>

namespace mu::composing::analysis::voiceleading {

namespace {

int sign(int x)
{
    return (x > 0) - (x < 0);
}

} // namespace

bool classifyMotion(int pu0, int pu1, int pv0, int pv1, MotionType& out)
{
    // voiceleading2._motion, verbatim arithmetic:
    //   du,dv = sign of each voice's motion.
    //   both static      -> None (return false, both-static drop).
    //   exactly one moves -> oblique.
    //   opposite dirs     -> contrary.
    //   same dir          -> parallel iff (pu1-pv1)==(pu0-pv0) [semitone-exact], else similar.
    const int du = sign(pu1 - pu0);
    const int dv = sign(pv1 - pv0);
    if (du == 0 && dv == 0) {
        return false;
    }
    if (du == 0 || dv == 0) {
        out = MotionType::Oblique;
    } else if (du == -dv) {
        out = MotionType::Contrary;
    } else {
        out = ((pu1 - pv1) == (pu0 - pv0)) ? MotionType::Parallel : MotionType::Similar;
    }
    return true;
}

std::vector<ReducedLine> reducedOnsetSeries(const VoiceLinearView& view, ReductionRule rule)
{
    std::vector<ReducedLine> out;
    for (const VoiceLine& line : view.lines) {
        ReducedLine rl;
        rl.staff = line.staff;
        rl.voice = line.voice;
        for (const VoiceEvent& ev : line.events) {
            const std::optional<int> p = reducedPitch(ev, rule);
            if (p) {
                rl.onsets.emplace_back(ev.onset, *p);
            }
        }
        // The study includes a voice in View B only if it has more than one onset
        // (`if len(seqB) > 1`). Drop single-onset lines.
        if (rl.onsets.size() > 1) {
            out.push_back(std::move(rl));
        }
    }
    return out;
}

MotionProfile computeMotionProfile(const VoiceLinearView& view,
                                   std::vector<MotionEvent>* eventsOut,
                                   ReductionRule rule)
{
    const std::vector<ReducedLine> lines = reducedOnsetSeries(view, rule);

    MotionProfile prof;
    prof.reduction = rule;
    prof.eligibleVoiceCount = static_cast<int>(lines.size());

    long long parallel = 0, similar = 0, contrary = 0, oblique = 0;
    const std::size_t n = lines.size();
    for (std::size_t i = 0; i < n; ++i) {
        const ReducedLine& u = lines[i];
        for (std::size_t j = i + 1; j < n; ++j) {
            const ReducedLine& v = lines[j];
            ++prof.voicePairCount;

            // Merged sorted set of the two lines' onsets (the sample grid).
            std::vector<int> times;
            times.reserve(u.onsets.size() + v.onsets.size());
            for (const auto& o : u.onsets) { times.push_back(o.first); }
            for (const auto& o : v.onsets) { times.push_back(o.first); }
            std::sort(times.begin(), times.end());
            times.erase(std::unique(times.begin(), times.end()), times.end());

            // Piecewise-constant hold: a voice's pitch at t = its most recent onset
            // at-or-before t (bisect_right - 1). Skip samples before both voices have
            // started; classify between consecutive samples, dropping both-static.
            bool havePrev = false;
            int prevU = 0, prevV = 0;
            std::size_t iu = 0, iv = 0;   // advancing pointers (times is ascending)
            for (int t : times) {
                while (iu + 1 < u.onsets.size() && u.onsets[iu + 1].first <= t) { ++iu; }
                while (iv + 1 < v.onsets.size() && v.onsets[iv + 1].first <= t) { ++iv; }
                if (u.onsets[iu].first > t || v.onsets[iv].first > t) {
                    continue;   // before one voice's first onset (iu/iv==0 and onset>t)
                }
                const int curU = u.onsets[iu].second;
                const int curV = v.onsets[iv].second;
                if (havePrev) {
                    MotionType m;
                    if (classifyMotion(prevU, curU, prevV, curV, m)) {
                        switch (m) {
                        case MotionType::Parallel: ++parallel; break;
                        case MotionType::Similar:  ++similar;  break;
                        case MotionType::Contrary: ++contrary; break;
                        case MotionType::Oblique:  ++oblique;  break;
                        }
                        if (eventsOut) {
                            MotionEvent me;
                            me.staffU = u.staff; me.voiceU = u.voice;
                            me.staffV = v.staff; me.voiceV = v.voice;
                            me.sampleTick = t;
                            me.type = m;
                            me.harmonicIntervalBefore = prevU - prevV;
                            me.harmonicIntervalAfter = curU - curV;
                            eventsOut->push_back(me);
                        }
                    }
                }
                prevU = curU;
                prevV = curV;
                havePrev = true;
            }
        }
    }

    const long long tot = parallel + similar + contrary + oblique;
    prof.sampleCount = static_cast<int>(tot);
    if (tot > 0) {
        const double d = static_cast<double>(tot);
        prof.parallel = static_cast<double>(parallel) / d;
        prof.similar  = static_cast<double>(similar)  / d;
        prof.contrary = static_cast<double>(contrary) / d;
        prof.oblique  = static_cast<double>(oblique)  / d;
    }
    prof.defined = (tot >= kMinMotionEvents);
    return prof;
}

namespace {

// Fold a pooled list of absolute intervals into an IntervalProfile (== vl_profile).
IntervalProfile foldIntervals(const std::vector<int>& absIntervals)
{
    IntervalProfile p;
    p.intervalCount = static_cast<int>(absIntervals.size());
    if (absIntervals.empty()) {
        p.defined = false;
        return p;
    }
    long long counts[13] = {0};
    long long repeat = 0, step = 0, leap = 0;
    for (int a : absIntervals) {
        const int bin = (a >= 12) ? 12 : a;
        counts[bin] += 1;
        if (a == 0) { ++repeat; }
        else if (a <= 2) { ++step; }   // 1..2
        if (a > 2) { ++leap; }         // >2  (>=3)
    }
    const double d = static_cast<double>(absIntervals.size());
    for (int k = 0; k < 13; ++k) {
        p.hist[static_cast<std::size_t>(k)] = static_cast<double>(counts[k]) / d;
    }
    p.repeat = static_cast<double>(repeat) / d;
    p.step   = static_cast<double>(step)   / d;
    p.leap   = static_cast<double>(leap)   / d;
    p.defined = (p.intervalCount >= kMinIntervals);
    return p;
}

// One line's reduced pitch sequence (top-note per eligible event, ascending onset).
// Unlike reducedOnsetSeries this keeps single-event lines (they contribute 0 intervals,
// matching vl_profile's pooling) — but they are harmless either way.
std::vector<int> reducedPitchSeq(const VoiceLine& line, ReductionRule rule)
{
    std::vector<int> seq;
    for (const VoiceEvent& ev : line.events) {
        const std::optional<int> p = reducedPitch(ev, rule);
        if (p) { seq.push_back(*p); }
    }
    return seq;
}

} // namespace

IntervalProfile computeIntervalProfileAggregate(const VoiceLinearView& view, ReductionRule rule)
{
    // Pool every eligible line's consecutive |intervals| into ONE list, exactly as
    // vl_profile does (`ivs = [abs(s[i]-s[i-1]) for s in voices for i in 1..]`).
    std::vector<int> pooled;
    for (const VoiceLine& line : view.lines) {
        const std::vector<int> seq = reducedPitchSeq(line, rule);
        for (std::size_t i = 1; i < seq.size(); ++i) {
            pooled.push_back(std::abs(seq[i] - seq[i - 1]));
        }
    }
    return foldIntervals(pooled);
}

std::vector<VoiceIntervalProfile> computeIntervalProfilesPerVoice(const VoiceLinearView& view,
                                                                  ReductionRule rule)
{
    std::vector<VoiceIntervalProfile> out;
    for (const VoiceLine& line : view.lines) {
        const std::vector<int> seq = reducedPitchSeq(line, rule);
        std::vector<int> ivs;
        for (std::size_t i = 1; i < seq.size(); ++i) {
            ivs.push_back(std::abs(seq[i] - seq[i - 1]));
        }
        VoiceIntervalProfile vp;
        vp.staff = line.staff;
        vp.voice = line.voice;
        vp.profile = foldIntervals(ivs);
        out.push_back(std::move(vp));
    }
    return out;
}

} // namespace mu::composing::analysis::voiceleading
