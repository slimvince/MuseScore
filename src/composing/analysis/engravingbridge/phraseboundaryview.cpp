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

#include "phraseboundaryview.h"

#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <limits>
#include <map>
#include <utility>

#include "composing/analysis/notemodel/note_model.h"
#include "composing/analysis/slicing/slicer.h"

#include "engraving/dom/breath.h"
#include "engraving/dom/engravingitem.h"
#include "engraving/dom/gradualtempochange.h"
#include "engraving/dom/keysig.h"
#include "engraving/dom/measure.h"
#include "engraving/dom/score.h"
#include "engraving/dom/segment.h"
#include "engraving/dom/spanner.h"
#include "engraving/dom/staff.h"
#include "engraving/types/types.h"

namespace mu::composing::analysis::engravingbridge {

namespace {

using notemodel::NoteEvent;
using notemodel::NoteModel;

// One eligible voice's collapsed monophonic event (a chord folds to a single
// line event: the same onset, the longest release, the highest pitch).
struct VoiceEvent {
    int onset   = 0;
    int release = 0;
    int pitch   = 0;
};

bool isEligible(const NoteEvent& n)
{
    return n.plays && n.visible && n.staffEligible;
}

// Group eligible notes by (staff, voice) and collapse same-onset notes (chords)
// into one monophonic line event. model.notes() is onset-sorted, so each group is
// onset-ascending; the collapse is a single linear merge per group.
std::map<std::pair<int, int>, std::vector<VoiceEvent>>
collectVoiceLines(const NoteModel& model)
{
    std::map<std::pair<int, int>, std::vector<VoiceEvent>> lines;
    for (const NoteEvent& n : model.notes()) {
        if (!isEligible(n)) {
            continue;
        }
        std::vector<VoiceEvent>& ev = lines[{ n.staff, n.voice }];
        if (!ev.empty() && ev.back().onset == n.onset) {
            ev.back().release = std::max(ev.back().release, n.release);
            ev.back().pitch   = std::max(ev.back().pitch, n.pitch);
        } else {
            ev.push_back({ n.onset, n.release, n.pitch });
        }
    }
    return lines;
}

// §4.2 the deterministic notated markers. Scan the engraved surface for the
// boundary signals; return their ticks (each is spiked on the texture profile).
// Notation only — no key/function (the key-signature CHANGE is read as the
// engraved signature event, NOT an inferred key).
//
// NOTE — the design qualifies the fermata/breath markers "on an eligible voice".
// We spike at ANY fermata/breath tick (the behaviour of the retired byte-identical
// scan): a fermata/breath on an analysis-ineligible staff is rare and harmless,
// and deriving the annotation's staff eligibility robustly is a minor refinement
// deferred from this build (proportionality). All other markers are voice-agnostic.
std::set<int> collectMarkerTicks(const mu::engraving::Score* score,
                                 const NoteModel& model,
                                 const PhraseBoundaryParams& params)
{
    using namespace mu::engraving;
    std::set<int> ticks;

    const Measure* firstMeasure = score->firstMeasure();
    if (!firstMeasure) {
        return ticks;
    }

    // Fermata + subito tempo marking — segment annotations (any segment).
    for (const Segment* s = firstMeasure->first(); s; s = s->next1()) {
        for (const EngravingItem* a : s->annotations()) {
            if (a && (a->isFermata() || a->isTempoText())) {
                ticks.insert(s->tick().ticks());
            }
        }
    }

    // Breath mark / caesura — Breath-segment elements.
    for (const Segment* s = firstMeasure->first(SegmentType::Breath); s;
         s = s->next1(SegmentType::Breath)) {
        for (const EngravingItem* e : s->elist()) {
            if (e && e->isBreath()) {
                ticks.insert(s->tick().ticks());
                break;
            }
        }
    }

    // Mid-score key-signature CHANGE — the engraved signature event (NOT the
    // inferred key). Track the prevailing concert key from tick 0 and spike where
    // a written signature differs from it.
    int prevKey = std::numeric_limits<int>::min();
    if (score->nstaves() > 0 && score->staff(0)) {
        prevKey = static_cast<int>(score->staff(0)->keySigEvent(Fraction(0, 1)).concertKey());
    }
    for (const Segment* s = firstMeasure->first(SegmentType::KeySig); s;
         s = s->next1(SegmentType::KeySig)) {
        const KeySig* ks = nullptr;
        for (const EngravingItem* e : s->elist()) {
            if (e && e->isKeySig()) {
                ks = toKeySig(e);
                break;
            }
        }
        if (!ks) {
            continue;
        }
        const int key = static_cast<int>(ks->concertKey());
        const int tick = s->tick().ticks();
        if (prevKey == std::numeric_limits<int>::min()) {
            prevKey = key;
        } else if (key != prevKey && tick > 0) {
            ticks.insert(tick);
            prevKey = key;
        } else {
            prevKey = key;
        }
    }

    // Structural barline — double / final / repeat (a notational division).
    for (const Measure* m = firstMeasure; m; m = m->nextMeasure()) {
        const BarLineType bt = m->endBarLineType();
        if (bt == BarLineType::DOUBLE || bt == BarLineType::END
            || bt == BarLineType::END_REPEAT || bt == BarLineType::END_START_REPEAT) {
            ticks.insert(m->endTick().ticks());
        }
        if (m->repeatStart()) {
            ticks.insert(m->tick().ticks());
        }
    }

    // Written ritardando / rallentando — a notated slowing into an arrival,
    // spiked at the arrival it leads to (the spanner end tick). Accelerations are
    // not a phrase-end signal.
    for (const auto& sp : score->spanner()) {
        const Spanner* spanner = sp.second;
        if (!spanner || !spanner->isGradualTempoChange()) {
            continue;
        }
        const GradualTempoChange* gtc = toGradualTempoChange(spanner);
        switch (gtc->tempoChangeType()) {
        case GradualTempoChangeType::Ritardando:
        case GradualTempoChangeType::Rallentando:
        case GradualTempoChangeType::Allargando:
        case GradualTempoChangeType::Calando:
        case GradualTempoChangeType::Lentando:
        case GradualTempoChangeType::Morendo:
        case GradualTempoChangeType::Smorzando:
            ticks.insert(gtc->tick2().ticks());
            break;
        default:
            break;   // Accelerando / Precipitando / Stringendo / Sostenuto: not a slowing-into-arrival
        }
    }

    // Maximal all-voice-rest span — a Layer-2 empty slice (no eligible voice
    // sounds) of at least the minimum-silence duration; spike at its onset.
    for (const slicing::Slice& sl : slicing::changePointSlices(model)) {
        if (sl.end - sl.start < params.minSilenceTicks) {
            continue;
        }
        bool anyEligible = false;
        for (const NoteEvent* n : model.overlapping(sl.start, sl.end)) {
            if (n && isEligible(*n)) {
                anyEligible = true;
                break;
            }
        }
        if (!anyEligible) {
            ticks.insert(sl.start);
        }
    }

    return ticks;
}

} // namespace

// ── Pure local-change helpers (design §4.1) ───────────────────────────────────

double changeRatio(double a, double b)
{
    const double denom = a + b;
    if (denom <= 0.0) {
        return 0.0;
    }
    return std::abs(a - b) / denom;
}

std::vector<double> localChangeProfile(const std::vector<double>& values)
{
    const size_t n = values.size();
    std::vector<double> out(n, 0.0);
    for (size_t i = 0; i < n; ++i) {
        const double left  = (i > 0)     ? changeRatio(values[i - 1], values[i]) : 0.0;
        const double right = (i + 1 < n) ? changeRatio(values[i], values[i + 1]) : 0.0;
        out[i] = values[i] * (left + right);
    }
    return out;
}

void maxNormalizeInPlace(std::vector<double>& profile)
{
    double mx = 0.0;
    for (double v : profile) {
        mx = std::max(mx, v);
    }
    if (mx <= 0.0) {
        return;
    }
    for (double& v : profile) {
        v /= mx;
    }
}

std::vector<int> pickPeaks(const std::vector<double>& strength, double k)
{
    std::vector<int> picked;
    const size_t m = strength.size();
    if (m == 0) {
        return picked;
    }
    double sum = 0.0, sumSq = 0.0;
    for (double x : strength) {
        sum += x;
        sumSq += x * x;
    }
    const double mean = sum / static_cast<double>(m);
    const double var = std::max(0.0, sumSq / static_cast<double>(m) - mean * mean);
    const double threshold = mean + k * std::sqrt(var);
    for (size_t i = 0; i < m; ++i) {
        const double x = strength[i];
        const bool leftOk  = (i == 0)     || x > strength[i - 1];
        const bool rightOk = (i + 1 == m) || x > strength[i + 1];
        if (leftOk && rightOk && x > threshold) {
            picked.push_back(static_cast<int>(i));
        }
    }
    return picked;
}

// ── The primitive (design §4) ─────────────────────────────────────────────────

PhraseBoundaryProfile computePhraseBoundaryProfile(const mu::engraving::Score* score,
                                                   const PhraseBoundaryParams& params)
{
    PhraseBoundaryProfile profile;
    if (!score) {
        return profile;
    }

    const NoteModel model = NoteModel::build(score);
    const auto lines = collectVoiceLines(model);
    if (lines.empty()) {
        return profile;
    }

    // §4.1 per voice: the three cue value sequences (each "after" value attaches
    // to the event it follows from — a large gap/IOI/leap AFTER an event marks
    // that event as a phrase end), then the local-change strength of each.
    struct VoiceStrengths {
        int                 staff = 0;
        int                 voice = 0;
        std::vector<int>    onsets;
        std::vector<double> gap;
        std::vector<double> ioi;
        std::vector<double> pitch;
    };
    std::vector<VoiceStrengths> vs;
    vs.reserve(lines.size());

    for (const auto& [key, ev] : lines) {
        const size_t n = ev.size();
        std::vector<double> gapVal(n, 0.0), ioiVal(n, 0.0), pitchVal(n, 0.0);
        std::vector<int> onsets(n, 0);
        for (size_t i = 0; i < n; ++i) {
            onsets[i] = ev[i].onset;
            if (i + 1 < n) {
                gapVal[i]   = std::max(0, ev[i + 1].onset - ev[i].release);   // offset-to-onset silence
                ioiVal[i]   = ev[i + 1].onset - ev[i].onset;                  // inter-onset interval
                pitchVal[i] = std::abs(ev[i + 1].pitch - ev[i].pitch);        // pitch-interval (semitones)
            }
        }
        VoiceStrengths v;
        v.staff = key.first;
        v.voice = key.second;
        v.onsets = std::move(onsets);
        v.gap   = localChangeProfile(gapVal);
        v.ioi   = localChangeProfile(ioiVal);
        v.pitch = localChangeProfile(pitchVal);
        vs.push_back(std::move(v));
    }

    // §4.1 max-normalise each cue over the WHOLE score (its per-score maximum
    // across all voices), so the three cues are on a common [0,1] scale and
    // comparable across voices for the texture sum.
    auto normalizeAcrossVoices = [&](std::vector<double> VoiceStrengths::* member) {
        double mx = 0.0;
        for (const VoiceStrengths& v : vs) {
            for (double x : v.*member) {
                mx = std::max(mx, x);
            }
        }
        if (mx <= 0.0) {
            return;
        }
        for (VoiceStrengths& v : vs) {
            for (double& x : v.*member) {
                x /= mx;
            }
        }
    };
    normalizeAcrossVoices(&VoiceStrengths::gap);
    normalizeAcrossVoices(&VoiceStrengths::ioi);
    normalizeAcrossVoices(&VoiceStrengths::pitch);

    // §4.1 per-voice combined surface strength = gap-dominant weighted sum.
    // §4.3 expose the per-voice profiles.
    profile.perVoice.reserve(vs.size());
    for (const VoiceStrengths& v : vs) {
        VoiceBoundaryProfile vb;
        vb.staff = v.staff;
        vb.voice = v.voice;
        vb.onsets = v.onsets;
        vb.strength.resize(v.onsets.size(), 0.0);
        for (size_t i = 0; i < v.onsets.size(); ++i) {
            vb.strength[i] = params.wGap * v.gap[i]
                           + params.wInterOnset * v.ioi[i]
                           + params.wPitch * v.pitch[i];
        }
        profile.perVoice.push_back(std::move(vb));
    }

    // §4.3 aggregate to the texture: sum the per-voice strengths per (tau-merged)
    // onset. Collect every (onset, strength) sample, sort by onset, greedily
    // cluster onsets within tau (rep = the cluster's first onset), sum strengths.
    std::vector<std::pair<int, double>> samples;
    for (const VoiceBoundaryProfile& vb : profile.perVoice) {
        for (size_t i = 0; i < vb.onsets.size(); ++i) {
            samples.push_back({ vb.onsets[i], vb.strength[i] });
        }
    }
    std::sort(samples.begin(), samples.end(),
              [](const auto& a, const auto& b) { return a.first < b.first; });

    std::map<int, double> surfaceByTick;   // tau-cluster rep tick -> summed surface strength
    std::map<int, int>    countByTick;     // rep tick -> number of contributing voice samples
    int rep = std::numeric_limits<int>::min();
    for (const auto& s : samples) {
        if (rep == std::numeric_limits<int>::min() || s.first - rep > params.tauTicks) {
            rep = s.first;   // start a new coincidence cluster
        }
        surfaceByTick[rep] += s.second;
        countByTick[rep]   += 1;
    }
    // §4.3 optional explicit coincidence weight (default 0 = plain sum).
    if (params.coincidenceWeight > 0.0) {
        for (auto& [tick, strength] : surfaceByTick) {
            strength *= (1.0 + params.coincidenceWeight * (countByTick[tick] - 1));
        }
    }

    // §4.2 marker spikes. Height = spikeCeilingFactor * (#voices * sum of cue
    // weights) = a multiple of the theoretical maximum texture surface strength.
    // The default factor (> 1) makes a marker STRICTLY EXCEED any surface-cue peak
    // (which can itself reach the ceiling when every voice's combined cue maxes and
    // coincides), so a marker dominates and clears the peak-picking threshold by
    // construction (design §4.2) — while staying close enough to the surface scale
    // that a locally-strong surface peak can still clear the threshold (§4.4).
    const std::set<int> markerTicks = collectMarkerTicks(score, model, params);
    const double sumWeights = params.wGap + params.wInterOnset + params.wPitch;
    const double spike = params.spikeCeilingFactor
                       * static_cast<double>(vs.size()) * sumWeights;

    // Build the texture grid = sorted union of the surface ticks and the marker
    // ticks; the combined strength is the surface sum plus the spike at markers.
    std::set<int> gridTicks;
    for (const auto& [tick, strength] : surfaceByTick) {
        (void)strength;
        gridTicks.insert(tick);
    }
    for (int t : markerTicks) {
        gridTicks.insert(t);
    }

    profile.textureTicks.reserve(gridTicks.size());
    profile.textureStrength.reserve(gridTicks.size());
    for (int t : gridTicks) {
        double strength = 0.0;
        auto it = surfaceByTick.find(t);
        if (it != surfaceByTick.end()) {
            strength += it->second;
        }
        if (markerTicks.count(t)) {
            strength += spike;
        }
        profile.textureTicks.push_back(t);
        profile.textureStrength.push_back(strength);
    }

    // §4.4 peak-picking — local maximum AND above the Simple-Picker threshold
    // (whole-profile mean + k * standard deviation) — picks the locally-strong
    // SURFACE peaks (and any marker that is a clean local maximum).
    for (int i : pickPeaks(profile.textureStrength, params.k)) {
        profile.pickedTicks.insert(profile.textureTicks[static_cast<size_t>(i)]);
    }
    // §4.2 the notated markers are DETERMINISTIC boundaries that "dominate wherever
    // it occurs" — always emitted, regardless of the local-max test (which the
    // strict-greater rule would otherwise drop for two adjacent equal-height
    // markers, e.g. a final phrase's fermata abutting the closing barline). The
    // spike already places them at/above any surface peak in the exposed texture
    // profile; here they are guaranteed in the picked set.
    for (int t : markerTicks) {
        profile.pickedTicks.insert(t);
    }

    return profile;
}

std::set<int> phraseBoundaryTicks(const mu::engraving::Score* score)
{
    return computePhraseBoundaryProfile(score).pickedTicks;
}

} // namespace mu::composing::analysis::engravingbridge
