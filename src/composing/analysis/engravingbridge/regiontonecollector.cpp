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

#include "regiontonecollector.h"

#include <algorithm>
#include <cstdint>
#include <limits>
#include <map>

#include "engraving/dom/chord.h"
#include "engraving/dom/chordrest.h"
#include "engraving/dom/measure.h"
#include "engraving/dom/note.h"
#include "engraving/dom/segment.h"
#include "engraving/dom/sig.h"

#include "composing/analysis/chord/analysisutils.h"
#include "composing/analysis/scoreharvest/metricweights.h"

namespace shv = mu::composing::analysis::scoreharvest;

namespace mu::composing::analysis::engravingbridge {

std::vector<mu::composing::analysis::ChordAnalysisTone>
collectRegionTones(const mu::engraving::Score* sc,
                   int startTickInt,
                   int endTickInt,
                   const std::set<std::size_t>& excludeStaves,
                   int parentStartTickInt,
                   bool excludeLookAheadOnDenseStart)
{
    using namespace mu::engraving;
    using namespace mu::composing::analysis;

    if (!sc || endTickInt <= startTickInt) {
        return {};
    }

    // Iter 93: onsetAtRegionStart is computed against parentStartTickInt so
    // that sub-region calls (Pass 2 / Pass 2b) see the parent-scope onset
    // truth. Default to startTickInt for parent-scope / unsplit callers.
    if (parentStartTickInt < 0) {
        parentStartTickInt = startTickInt;
    }

    const ChordAnalyzerPreferences& prefs = kDefaultChordAnalyzerPreferences;

    const Fraction startTick = Fraction::fromTicks(startTickInt);
    const Fraction endTick   = Fraction::fromTicks(endTickInt);
    const int regionDuration = endTickInt - startTickInt;

    auto beatWeight = [](BeatType bt) -> double {
        switch (bt) {
        case BeatType::DOWNBEAT:            return 1.0;
        case BeatType::SIMPLE_STRESSED:
        case BeatType::COMPOUND_STRESSED:   return 0.85;
        case BeatType::SIMPLE_UNSTRESSED:
        case BeatType::COMPOUND_UNSTRESSED: return 0.75;
        default:                            return 0.5;  // SUBBEAT / COMPOUND_SUBBEAT
        }
    };

    struct PcAccum {
        double totalWeight      = 0.0;
        int    durationInRegion = 0;
        std::set<int> metricTicks;
        int lowestPitch = std::numeric_limits<int>::max();
        int tpc = -1;
        bool trueAttackAtStart = false;
    };
    PcAccum accum[12];

    std::map<int, int> voiceCountAtTick[12];

    struct PedalTailCandidate {
        std::size_t staffIdx = 0;
        int pc = 0;
        int pitch = 0;
        int tpc = -1;
        int writtenEndTick = 0;
        double attackBeatWeight = 0.0;
    };

    std::map<std::size_t, std::vector<shv::PedalWindow>> pedalWindowsByStaff
        = shv::buildPedalWindowIndex(
            sc, startTickInt, endTickInt, excludeStaves,
            [&](std::size_t si) { return staffIsEligible(sc, si, startTick); });
    std::vector<PedalTailCandidate> pedalTailCandidates;

    auto earliestPedalReleaseTick = [&](const PedalTailCandidate& candidate) -> int {
        const auto it = pedalWindowsByStaff.find(candidate.staffIdx);
        if (it == pedalWindowsByStaff.end()) {
            return -1;
        }

        int pedalReleaseTick = std::numeric_limits<int>::max();
        for (const shv::PedalWindow& window : it->second) {
            if (window.startTick >= candidate.writtenEndTick) {
                break;
            }
            if (window.endTick <= candidate.writtenEndTick) {
                continue;
            }
            pedalReleaseTick = std::min(pedalReleaseTick, window.endTick);
        }

        return pedalReleaseTick == std::numeric_limits<int>::max() ? -1 : pedalReleaseTick;
    };

    auto recordPedalTailCandidate = [&](std::size_t staffIdx, int writtenEndTick,
                                        double attackBeatWeight, const Note* note) {
        if (!note || writtenEndTick >= endTickInt || pedalWindowsByStaff.empty()) {
            return;
        }
        if (pedalWindowsByStaff.find(staffIdx) == pedalWindowsByStaff.end()) {
            return;
        }
        pedalTailCandidates.push_back({
            staffIdx,
            note->ppitch() % 12,
            note->ppitch(),
            note->tpc(),
            writtenEndTick,
            attackBeatWeight,
        });
    };

    const Fraction backLimit = startTick - Fraction(4, 1);

    auto bwAtRegionStart = [&]() -> double {
        const Measure* m0 = sc->tick2measure(startTick);
        if (!m0) { return 0.75; }
        const Segment* s0 = sc->tick2segment(startTick, true, SegmentType::ChordRest);
        if (!s0) { return 0.75; }
        return beatWeight(shv::safeBeatType(m0, s0));
    }();

    const Segment* firstForward = sc->tick2segment(startTick, true, SegmentType::ChordRest);
    if (firstForward) {
        for (const Segment* s = firstForward->prev1(SegmentType::ChordRest);
             s && s->tick() >= backLimit;
             s = s->prev1(SegmentType::ChordRest)) {
            const int segTickInt = s->tick().ticks();
            const Measure* m = s->measure();
            const double sustainBeatWeight = m ? beatWeight(shv::safeBeatType(m, s)) : bwAtRegionStart;
            for (std::size_t si = 0; si < sc->nstaves(); ++si) {
                if (excludeStaves.count(si) || !staffIsEligible(sc, si, startTick)) {
                    continue;
                }
                for (int v = 0; v < VOICES; ++v) {
                    const ChordRest* cr
                        = s->cr(static_cast<track_idx_t>(si) * VOICES + v);
                    if (!cr || !cr->isChord() || cr->isGrace()) {
                        continue;
                    }
                    const int noteEnd = segTickInt + cr->actualTicks().ticks();
                    for (const Note* n : toChord(cr)->notes()) {
                        if (!n->play() || !n->visible()) {
                            continue;
                        }

                        recordPedalTailCandidate(si, noteEnd, sustainBeatWeight, n);

                        if (noteEnd <= startTickInt) {
                            continue;
                        }

                        const int clippedEnd  = std::min(noteEnd, endTickInt);
                        const int durInRegion = clippedEnd - startTickInt;
                        if (durInRegion <= 0) {
                            continue;
                        }

                        const double baseWeight
                            = (static_cast<double>(durInRegion) / regionDuration) * bwAtRegionStart;
                        const int pc = n->ppitch() % 12;
                        PcAccum& a = accum[pc];
                        a.totalWeight    += baseWeight;
                        a.durationInRegion += durInRegion;
                        a.metricTicks.insert(startTickInt);
                        voiceCountAtTick[pc][startTickInt]++;
                        if (n->ppitch() < a.lowestPitch) {
                            a.lowestPitch = n->ppitch();
                            a.tpc = n->tpc();
                        }
                    }
                }
            }
        }
    }

    const Segment* seg = firstForward;
    if (!seg) {
        return {};
    }

    bool excludeLookAhead = false;
    if (excludeLookAheadOnDenseStart) {
        int pcsSoundingAtStart = 0;
        for (int pc = 0; pc < 12; ++pc) {
            if (accum[pc].totalWeight > 0.0) {
                ++pcsSoundingAtStart;
            }
        }
        if (seg->tick().ticks() == startTickInt) {
            for (std::size_t si = 0; si < sc->nstaves(); ++si) {
                if (excludeStaves.count(si) || !staffIsEligible(sc, si, startTick)) {
                    continue;
                }
                for (int v = 0; v < VOICES; ++v) {
                    const ChordRest* cr
                        = seg->cr(static_cast<track_idx_t>(si) * VOICES + v);
                    if (!cr || !cr->isChord() || cr->isGrace()) {
                        continue;
                    }
                    for (const Note* n : toChord(cr)->notes()) {
                        if (!n->play() || !n->visible()) {
                            continue;
                        }
                        const int pc = n->ppitch() % 12;
                        if (accum[pc].totalWeight == 0.0) {
                            ++pcsSoundingAtStart;
                        }
                    }
                }
            }
        }
        excludeLookAhead = (pcsSoundingAtStart >= 3);
    }

    for (const Segment* s = seg;
         s && s->tick() < endTick;
         s = s->next1(SegmentType::ChordRest)) {
        const Measure* m = s->measure();
        if (!m) {
            continue;
        }

        const int segTickInt = s->tick().ticks();
        const BeatType bt = shv::safeBeatType(m, s);
        const double bw = beatWeight(bt);

        if (excludeLookAhead && segTickInt > startTickInt) {
            continue;
        }

        for (std::size_t si = 0; si < sc->nstaves(); ++si) {
            if (excludeStaves.count(si) || !staffIsEligible(sc, si, s->tick())) {
                continue;
            }
            for (int v = 0; v < VOICES; ++v) {
                const ChordRest* cr
                    = s->cr(static_cast<track_idx_t>(si) * VOICES + v);
                if (!cr || !cr->isChord() || cr->isGrace()) {
                    continue;
                }

                const int noteEnd      = segTickInt + cr->actualTicks().ticks();
                const int clippedEnd   = std::min(noteEnd, endTickInt);
                const int durInRegion  = clippedEnd - segTickInt;
                if (durInRegion <= 0) {
                    continue;
                }

                const double baseWeight
                    = (static_cast<double>(durInRegion) / regionDuration) * bw;

                for (const Note* n : toChord(cr)->notes()) {
                    if (!n->play() || !n->visible()) {
                        continue;
                    }

                    recordPedalTailCandidate(si, noteEnd, bw, n);

                    const int pc = n->ppitch() % 12;
                    PcAccum& a = accum[pc];
                    a.totalWeight    += baseWeight;
                    a.durationInRegion += durInRegion;
                    a.metricTicks.insert(segTickInt);
                    voiceCountAtTick[pc][segTickInt]++;
                    if (segTickInt == parentStartTickInt) {
                        a.trueAttackAtStart = true;
                    }

                    if (n->ppitch() < a.lowestPitch) {
                        a.lowestPitch = n->ppitch();
                        a.tpc = n->tpc();
                    }
                }
            }
        }
    }

    // Pass 2: repetition boost
    for (int pc = 0; pc < 12; ++pc) {
        PcAccum& a = accum[pc];
        if (a.totalWeight == 0.0) {
            continue;
        }
        const int distinct = static_cast<int>(a.metricTicks.size());
        if (distinct > 1) {
            a.totalWeight *= (1.0 + 0.3 * (distinct - 1));
        }
    }

    // Pass 3: cross-voice boost
    for (int pc = 0; pc < 12; ++pc) {
        PcAccum& a = accum[pc];
        if (a.totalWeight == 0.0) {
            continue;
        }
        int maxVoices = 0;
        for (const auto& kv : voiceCountAtTick[pc]) {
            maxVoices = std::max(maxVoices, kv.second);
        }
        if (maxVoices > 1) {
            a.totalWeight *= 1.5;
        }
    }

    // Pass 4: discounted sustain-pedal tails
    if (prefs.pedalTailWeightMultiplier > 0.0) {
        for (const PedalTailCandidate& candidate : pedalTailCandidates) {
            const int pedalReleaseTick = earliestPedalReleaseTick(candidate);
            if (pedalReleaseTick < 0) {
                continue;
            }

            const int tailStartTick = std::max(candidate.writtenEndTick, startTickInt);
            const int tailEndTick = std::min(pedalReleaseTick, endTickInt);
            const int tailDuration = tailEndTick - tailStartTick;
            if (tailDuration <= 0) {
                continue;
            }

            PcAccum& a = accum[candidate.pc];
            a.totalWeight += (static_cast<double>(tailDuration) / regionDuration)
                             * candidate.attackBeatWeight
                             * prefs.pedalTailWeightMultiplier;
            a.durationInRegion += tailDuration;
            if (candidate.pitch < a.lowestPitch) {
                a.lowestPitch = candidate.pitch;
                a.tpc = candidate.tpc;
            }
        }
    }

    // Normalize
    double totalWeight = 0.0;
    for (int pc = 0; pc < 12; ++pc) {
        totalWeight += accum[pc].totalWeight;
    }
    if (totalWeight == 0.0) {
        return {};
    }

    const double bassMinWeight = totalWeight * prefs.bassPassingToneMinWeightFraction;
    int bassPitch = std::numeric_limits<int>::max();
    for (int pc = 0; pc < 12; ++pc) {
        if (accum[pc].totalWeight >= bassMinWeight && accum[pc].lowestPitch < bassPitch) {
            bassPitch = accum[pc].lowestPitch;
        }
    }
    if (bassPitch == std::numeric_limits<int>::max()) {
        for (int pc = 0; pc < 12; ++pc) {
            if (accum[pc].totalWeight > 0.0 && accum[pc].lowestPitch < bassPitch) {
                bassPitch = accum[pc].lowestPitch;
            }
        }
    }
    const int bassPC = (bassPitch < std::numeric_limits<int>::max())
                       ? (bassPitch % 12) : -1;

    std::vector<ChordAnalysisTone> tones;
    for (int pc = 0; pc < 12; ++pc) {
        PcAccum& a = accum[pc];
        if (a.totalWeight == 0.0) {
            continue;
        }

        int maxVoices = 0;
        for (const auto& kv : voiceCountAtTick[pc]) {
            maxVoices = std::max(maxVoices, kv.second);
        }

        ChordAnalysisTone t;
        t.pitch                  = a.lowestPitch;
        t.tpc                    = a.tpc;
        t.weight                 = a.totalWeight / totalWeight;
        t.isBass                 = (pc == bassPC);
        t.durationInRegion       = a.durationInRegion;
        t.distinctMetricPositions = static_cast<int>(a.metricTicks.size());
        t.simultaneousVoiceCount = maxVoices;
        t.onsetAtRegionStart     = a.trueAttackAtStart;
        tones.push_back(t);
    }

    return tones;
}

} // namespace mu::composing::analysis::engravingbridge
