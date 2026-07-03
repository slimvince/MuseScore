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

#include "composing/analysis/voiceleading/textureclassifier.h"

#include <algorithm>
#include <cmath>

#include "composing/analysis/voiceleading/voicelinearview.h"

namespace mu::composing::analysis::voiceleading {

namespace {

// Convergence epsilon for the extension stop condition (bounded-context §3.6): the
// classification "stops changing" when the committed class is stable AND the confidence
// margin moves less than this. Precision-phase (the firewall), NOT tuned.
constexpr double kConvergenceEps = 1e-3;

double clamp01(double x)
{
    return x < 0.0 ? 0.0 : (x > 1.0 ? 1.0 : x);
}

} // namespace

std::array<double, kVlFeatureDim> buildFeature(const MotionProfile& motion, const IntervalProfile& interval)
{
    // The reference's declared order: interval A[0..15] then motion B[16..19].
    //   A[0..11]=P(|iv|=k), A[12]=P(|iv|>=12), A[13]=repeat, A[14]=step, A[15]=leap,
    //   B[16]=parallel, B[17]=similar, B[18]=contrary, B[19]=oblique.
    std::array<double, kVlFeatureDim> f{};
    for (int k = 0; k < 13; ++k) {
        f[static_cast<std::size_t>(k)] = interval.hist[static_cast<std::size_t>(k)];
    }
    f[13] = interval.repeat;
    f[14] = interval.step;
    f[15] = interval.leap;
    f[16] = motion.parallel;
    f[17] = motion.similar;
    f[18] = motion.contrary;
    f[19] = motion.oblique;
    return f;
}

VoiceLeadingSpan classifyTexture(const MotionProfile& motion, const IntervalProfile& interval,
                                 int startTick, int endTick, const TextureClassifierParams& params)
{
    VoiceLeadingSpan span;
    span.startTick = startTick;
    span.endTick = endTick;
    span.evidenceStartTick = startTick;
    span.evidenceEndTick = endTick;
    span.reduction = motion.reduction;
    span.motionSampleCount = motion.sampleCount;

    // No voice pairs -> the motion profile is undefined by construction: a single-voice
    // selection abstains NO-PAIR (never interval-only classification, v1; spec §5.3).
    if (motion.eligibleVoiceCount < 2) {
        span.abstained = true;
        span.reason = AbstentionReason::NoPair;
        return span;
    }
    // The evidential floor: too few motion samples to support a decision, or the interval
    // half of the feature is undefined (< 8 intervals).
    if (motion.sampleCount < params.evidentialFloor || !interval.defined) {
        span.abstained = true;
        span.reason = AbstentionReason::TooFewSamples;
        return span;
    }

    // Feature -> z-space -> nearest-centroid over the shipped reference (winning space
    // ABz, textureclassifierreference.h). fit = exp(-distance/fitScale); weight = softmax.
    const std::array<double, kVlFeatureDim> feat = buildFeature(motion, interval);
    std::array<double, kVlFeatureDim> z{};
    for (std::size_t d = 0; d < kVlFeatureDim; ++d) {
        z[d] = (feat[d] - kVlRefMean[d]) / (kVlRefStd[d] + 1e-9);
    }

    const double scale = (params.fitScale > 0.0) ? params.fitScale : 1.0;
    span.ranked.reserve(static_cast<std::size_t>(kVlTextureClassCount));
    double fitSum = 0.0;
    for (int k = 0; k < kVlTextureClassCount; ++k) {
        double sq = 0.0;
        for (std::size_t d = 0; d < kVlFeatureDim; ++d) {
            const double diff = z[d] - kVlRefCentroidZ[static_cast<std::size_t>(k)][d];
            sq += diff * diff;
        }
        ClassFit cf;
        cf.cls = static_cast<TextureClass>(k);
        cf.distance = std::sqrt(sq);
        cf.fit = std::exp(-cf.distance / scale);
        fitSum += cf.fit;
        span.ranked.push_back(cf);
    }
    for (ClassFit& cf : span.ranked) {
        cf.weight = (fitSum > 0.0) ? cf.fit / fitSum : 0.0;
    }
    // Rank by fit descending (== distance ascending). Ties broken by enum order (stable).
    std::stable_sort(span.ranked.begin(), span.ranked.end(),
                     [](const ClassFit& a, const ClassFit& b) { return a.fit > b.fit; });

    span.committed = span.ranked.front().cls;
    const double bestFit = span.ranked.front().fit;
    const double secondFit = (span.ranked.size() > 1) ? span.ranked[1].fit : 0.0;
    const double margin = bestFit - secondFit;               // in [0,1)
    span.confidence = clamp01(margin);                       // Class-M, squashed (R5)

    // Abstention (contract U5): fit floor first (resembles no reference class), then
    // margin floor (a near-tie). The ranked list is CARRIED either way (zero loss).
    if (bestFit < params.fitFloor) {
        span.abstained = true;
        span.reason = AbstentionReason::LowFit;
    } else if (margin < params.marginFloor) {
        span.abstained = true;
        span.reason = AbstentionReason::LowMargin;
    }
    return span;
}

VoiceLeadingSpan classifySelectionExtending(notemodel::NoteModel model,
                                            int selectionStart, int selectionEnd,
                                            const TextureClassifierParams& params,
                                            const VlExtensionParams& ext)
{
    using Direction = notemodel::NoteModel::Direction;

    // One classification over the model's CURRENT loaded span (the profiles see the
    // loaded span = selection + any extended evidence; the labelled range stays the
    // selection). Evidence-span provenance rides the result.
    auto classifyCurrent = [&]() -> VoiceLeadingSpan {
        const VoiceLinearView view = buildVoiceLinearView(model);
        const MotionProfile motion = computeMotionProfile(view, nullptr);
        const IntervalProfile interval = computeIntervalProfileAggregate(view);
        VoiceLeadingSpan r = classifyTexture(motion, interval, selectionStart, selectionEnd, params);
        r.evidenceStartTick = model.loadedStart();
        r.evidenceEndTick = model.loadedEnd();
        return r;
    };

    VoiceLeadingSpan cur = classifyCurrent();

    // Stop reasons for honest provenance at loop exit.
    enum class Stop { CueCleared, Converged, ScoreBoundary, HardBound };
    Stop stop = Stop::CueCleared;

    if (ext.enableExtension) {
        const int incTicks = std::max(1, ext.incrementBars * ext.ticksPerBar);
        int steps = 0;
        for (;;) {
            const bool cueFires = (cur.motionSampleCount < params.evidentialFloor)
                                  && (cur.confidence < params.marginFloor);
            if (!cueFires) { stop = Stop::CueCleared; break; }
            if (steps >= ext.maxSteps) { stop = Stop::HardBound; break; }
            const bool canLater = model.loadedEnd() < model.scoreEnd();
            const bool canEarlier = model.loadedStart() > model.scoreStart();
            if (!canLater && !canEarlier) { stop = Stop::ScoreBoundary; break; }

            // Direction: later first, then earlier (spec §8) — grow later until the score
            // end, then switch to earlier. L1 extend() clamps at the score boundary.
            bool grew = false;
            if (canLater) {
                const int before = model.loadedEnd();
                model.extend(Direction::Later, incTicks);
                grew = model.loadedEnd() > before;
            } else {
                const int before = model.loadedStart();
                model.extend(Direction::Earlier, incTicks);
                grew = model.loadedStart() < before;
            }
            if (!grew) { stop = Stop::ScoreBoundary; break; }   // defensive: nothing loaded
            ++steps;

            const VoiceLeadingSpan prev = cur;
            cur = classifyCurrent();
            // Convergence (§3.6): a COMMITTED classification and its margin stopped
            // changing under further context. Guarded on !abstained on BOTH sides — two
            // starved/abstained results are trivially "unchanged", which is not
            // convergence (the profile is still below the evidential floor and must keep
            // extending toward the hard bound / score boundary), so they never count.
            if (!cur.abstained && !prev.abstained
                && cur.committed == prev.committed
                && std::abs(cur.confidence - prev.confidence) < kConvergenceEps) {
                stop = Stop::Converged;
                break;
            }
        }
    }

    // Honest marks (§7). The range stays the SELECTION; the evidence span is what the
    // final classification actually saw.
    cur.startTick = selectionStart;
    cur.endTick = selectionEnd;
    const bool hasUnloadedContext = (model.loadedStart() > model.scoreStart())
                                    || (model.loadedEnd() < model.scoreEnd());
    const bool starved = (cur.motionSampleCount < params.evidentialFloor) || cur.abstained;
    if (starved && hasUnloadedContext) {
        // The classification rests on a window truncated at a NON-score loaded edge — a
        // truncated result is never presented as complete (§3 item 10).
        cur.clippedBySelectionEdge = true;
    }
    if (ext.enableExtension && stop == Stop::HardBound && hasUnloadedContext) {
        // A decision-relevant extension request was refused because the hard bound was
        // spent (a score-boundary stop is not a denial — nothing was requestable there).
        cur.cueDenied = true;
    }
    return cur;
}

} // namespace mu::composing::analysis::voiceleading
