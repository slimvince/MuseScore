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
weightedPcView(const notemodel::NoteModel& noteModel,
               int startTickInt,
               int endTickInt,
               const std::set<std::size_t>& excludeStaves,
               int parentStartTickInt,
               bool excludeLookAheadOnDenseStart,
               const ChordAnalyzerPreferences& prefs)
{
    using namespace mu::engraving;
    using namespace mu::composing::analysis;
    using notemodel::NoteEvent;

    const Score* sc = noteModel.score();
    if (!sc || endTickInt <= startTickInt) {
        return {};
    }

    // Iter 93: onsetAtRegionStart is computed against parentStartTickInt so
    // that sub-region calls (Pass 2 / Pass 2b) see the parent-scope onset
    // truth. Default to startTickInt for parent-scope / unsplit callers.
    if (parentStartTickInt < 0) {
        parentStartTickInt = startTickInt;
    }

    const Fraction startTick = Fraction::fromTicks(startTickInt);
    const int regionDuration = endTickInt - startTickInt;

    // Beat-type → normalised metric weight is single-owned by
    // scoreharvest::regionMetricWeightForBeatType (metricweights.h, already
    // included). Formerly this TU inlined the identical {1.0,0.85,0.75,0.5} map;
    // FQ-5/S5 unifies to the one source.

    // The view filter — reproduces the legacy analysis drop set exactly: a note
    // contributes only if its staff is eligible and not excluded, and the note
    // plays, is visible, and is not a grace note. The lossless model keeps the
    // rest (flagged); this is where the keep/drop decision is applied.
    auto passes = [&](const NoteEvent& e) -> bool {
        return e.staffEligible && !excludeStaves.count(static_cast<std::size_t>(e.staff))
               && e.plays && e.visible && !e.isGrace;
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
                                        double attackBeatWeight, int pitch, int tpc) {
        if (writtenEndTick >= endTickInt || pedalWindowsByStaff.empty()) {
            return;
        }
        if (pedalWindowsByStaff.find(staffIdx) == pedalWindowsByStaff.end()) {
            return;
        }
        pedalTailCandidates.push_back({
            staffIdx,
            pitch % 12,
            pitch,
            tpc,
            writtenEndTick,
            attackBeatWeight,
        });
    };

    const int backLimitInt = (startTick - Fraction(4, 1)).ticks();

    const double bwAtRegionStart = [&]() -> double {
        const Measure* m0 = sc->tick2measure(startTick);
        if (!m0) { return 0.75; }
        const Segment* s0 = sc->tick2segment(startTick, true, SegmentType::ChordRest);
        if (!s0) { return 0.75; }
        return shv::regionMetricWeightForBeatType(shv::safeBeatType(m0, s0));
    }();

    // Beat weight at a note's onset segment (the legacy per-note metric weight).
    auto beatWeightAtOnset = [&](int onsetTick) -> double {
        const Fraction t = Fraction::fromTicks(onsetTick);
        const Measure* m = sc->tick2measure(t);
        if (!m) { return bwAtRegionStart; }
        const Segment* s = sc->tick2segment(t, true, SegmentType::ChordRest);
        if (!s) { return bwAtRegionStart; }
        return shv::regionMetricWeightForBeatType(shv::safeBeatType(m, s));
    };

    // Dense-start look-ahead exclusion: when ≥3 distinct pitch classes already
    // sound at the region start, drop notes that onset strictly after start.
    // The "sounding at start" set is exactly the notes overlapping [start,start+1)
    // (sustains reaching in + onsets exactly at start) — the model-native form of
    // the legacy post-backward-walk accum count.
    bool excludeLookAhead = false;
    if (excludeLookAheadOnDenseStart) {
        const auto soundingAtStart = noteModel.overlapping(startTickInt, startTickInt + 1);
        // (1) DISTINCT pitch classes sustaining INTO the region (the legacy
        //     post-backward-walk accum>0 count).
        bool backwardPc[12] = { false };
        int pcsSoundingAtStart = 0;
        for (const NoteEvent* ne : soundingAtStart) {
            if (!passes(*ne) || ne->onset >= startTickInt) {
                continue;
            }
            const int pc = ne->pitch % 12;
            if (!backwardPc[pc]) {
                backwardPc[pc] = true;
                ++pcsSoundingAtStart;
            }
        }
        // (2) Pitch classes newly attacking AT the region start. The legacy code
        //     counts each such NOTE whose pc is not already sustaining — with NO
        //     dedup among the start-onset notes, so an octave doubling at the
        //     downbeat counts twice. Reproduced exactly (changing it would alter
        //     un-fixed cases — not a tie/cap fix).
        for (const NoteEvent* ne : soundingAtStart) {
            if (!passes(*ne) || ne->onset != startTickInt) {
                continue;
            }
            if (!backwardPc[ne->pitch % 12]) {
                ++pcsSoundingAtStart;
            }
        }
        excludeLookAhead = (pcsSoundingAtStart >= 3);
    }

    // ── Weighting pass — true-span overlap (no horizon; the cap fix). Each
    // overlapping note contributes ONCE (the tie fix: one onset per tied group).
    for (const NoteEvent* ne : noteModel.overlapping(startTickInt, endTickInt)) {
        if (!passes(*ne)) {
            continue;
        }
        const int pc = ne->pitch % 12;
        PcAccum& a = accum[pc];

        if (ne->onset >= startTickInt) {
            // Onsets within the region (the legacy forward walk).
            if (excludeLookAhead && ne->onset > startTickInt) {
                continue;
            }
            const Fraction t = Fraction::fromTicks(ne->onset);
            const Measure* m = sc->tick2measure(t);
            if (!m) {
                continue;  // legacy forward walk skips measure-less segments
            }
            const Segment* fs = sc->tick2segment(t, true, SegmentType::ChordRest);
            const double bw = fs ? shv::regionMetricWeightForBeatType(shv::safeBeatType(m, fs)) : bwAtRegionStart;

            const int clippedEnd  = std::min(ne->release, endTickInt);
            const int durInRegion = clippedEnd - ne->onset;
            if (durInRegion <= 0) {
                continue;
            }
            const double baseWeight
                = (static_cast<double>(durInRegion) / regionDuration) * bw;
            a.totalWeight      += baseWeight;
            a.durationInRegion += durInRegion;
            a.metricTicks.insert(ne->onset);
            voiceCountAtTick[pc][ne->onset]++;
            if (ne->onset == parentStartTickInt) {
                a.trueAttackAtStart = true;
            }
            if (ne->pitch < a.lowestPitch) {
                a.lowestPitch = ne->pitch;
                a.tpc = ne->tpc;
            }
        } else {
            // Onsets before the region but sustaining into it (the legacy
            // backward walk). overlap guarantees release > startTick.
            const int clippedEnd  = std::min(ne->release, endTickInt);
            const int durInRegion = clippedEnd - startTickInt;
            if (durInRegion <= 0) {
                continue;
            }
            const double baseWeight
                = (static_cast<double>(durInRegion) / regionDuration) * bwAtRegionStart;
            a.totalWeight      += baseWeight;
            a.durationInRegion += durInRegion;
            a.metricTicks.insert(startTickInt);
            voiceCountAtTick[pc][startTickInt]++;
            if (ne->pitch < a.lowestPitch) {
                a.lowestPitch = ne->pitch;
                a.tpc = ne->tpc;
            }
        }
    }

    // ── Pedal-tail candidate pass — gathers candidates over the legacy onset
    // window [start - 4 wholes, end), matching the old backward+forward pedal
    // coverage. (Order is irrelevant: Pass 4 sums them.) Only when a pedal index
    // exists. The look-ahead exclusion suppresses post-start onsets here too, as
    // the legacy segment-level skip did.
    if (!pedalWindowsByStaff.empty()) {
        for (const NoteEvent* ne : noteModel.onsetIn(backLimitInt, endTickInt)) {
            if (!passes(*ne)) {
                continue;
            }
            if (excludeLookAhead && ne->onset > startTickInt) {
                continue;
            }
            const double bw = beatWeightAtOnset(ne->onset);
            recordPedalTailCandidate(static_cast<std::size_t>(ne->staff), ne->release,
                                     bw, ne->pitch, ne->tpc);
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

std::vector<mu::composing::analysis::ChordAnalysisTone>
collectRegionTones(const mu::engraving::Score* sc,
                   int startTickInt,
                   int endTickInt,
                   const std::set<std::size_t>& excludeStaves,
                   int parentStartTickInt,
                   bool excludeLookAheadOnDenseStart)
{
    // Score-based convenience wrapper: build the note model and derive the
    // weighted-PC view. Hot paths build the model once and call weightedPcView
    // directly; this one-shot form serves cold/test callers.
    return weightedPcView(notemodel::NoteModel::build(sc), startTickInt, endTickInt,
                          excludeStaves, parentStartTickInt, excludeLookAheadOnDenseStart);
}

} // namespace mu::composing::analysis::engravingbridge
