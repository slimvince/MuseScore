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

using mu::composing::analysis::isDiatonicStep;

void collectSoundingAt(const mu::engraving::Score* sc,
                       const mu::engraving::Segment* anchorSeg,
                       const std::set<std::size_t>& excludeStaves,
                       std::vector<SoundingNote>& out)
{
    using namespace mu::engraving;

    const Fraction anchorTick = anchorSeg->tick();

    auto collectCr = [&](const Segment* s, const ChordRest* cr) {
        if (!cr || !cr->isChord() || cr->isGrace()) {
            return;
        }
        if (s->tick() < anchorTick) {
            const Fraction noteEnd = s->tick() + toChord(cr)->actualTicks();
            if (noteEnd <= anchorTick) {
                return;
            }
        }
        for (const Note* n : toChord(cr)->notes()) {
            if (!n->play() || !n->visible()) {
                continue;  // skip silent notes and invisible tuning artifacts
            }
            out.push_back({ n->ppitch(), n->tpc() });
        }
    };

    for (std::size_t si = 0; si < sc->nstaves(); ++si) {
        if (excludeStaves.count(si) || !staffIsEligible(sc, si, anchorTick)) {
            continue;
        }
        for (int v = 0; v < VOICES; ++v) {
            collectCr(anchorSeg,
                      anchorSeg->cr(static_cast<track_idx_t>(si) * VOICES + v));
        }
    }

    const Fraction backLimit = anchorTick - Fraction(4, 1);
    for (const Segment* s = anchorSeg->prev1(SegmentType::ChordRest);
         s && s->tick() >= backLimit;
         s = s->prev1(SegmentType::ChordRest)) {
        for (std::size_t si = 0; si < sc->nstaves(); ++si) {
            if (excludeStaves.count(si) || !staffIsEligible(sc, si, anchorTick)) {
                continue;
            }
            for (int v = 0; v < VOICES; ++v) {
                collectCr(s, s->cr(static_cast<track_idx_t>(si) * VOICES + v));
            }
        }
    }
}

std::vector<mu::composing::analysis::ChordAnalysisTone>
buildTones(const std::vector<SoundingNote>& sounding)
{
    using mu::composing::analysis::ChordAnalysisTone;

    int lowestPpitch = std::numeric_limits<int>::max();
    for (const SoundingNote& sn : sounding) {
        if (sn.ppitch < lowestPpitch) {
            lowestPpitch = sn.ppitch;
        }
    }
    std::vector<ChordAnalysisTone> tones;
    tones.reserve(sounding.size());
    for (const SoundingNote& sn : sounding) {
        ChordAnalysisTone t;
        t.pitch  = sn.ppitch;
        t.tpc    = sn.tpc;
        t.isBass = (sn.ppitch == lowestPpitch);
        tones.push_back(t);
    }
    return tones;
}

void collectPitchContext(const mu::engraving::Score* sc,
                         const mu::engraving::Fraction& tick,
                         const mu::engraving::Fraction& windowStart,
                         const mu::engraving::Fraction& windowEnd,
                         const std::set<std::size_t>& excludeStaves,
                         const mu::composing::analysis::KeyModeAnalyzerPreferences& prefs,
                         std::vector<mu::composing::analysis::KeyModeAnalyzer::PitchContext>& ctx)
{
    using namespace mu::engraving;
    using namespace mu::composing::analysis;

    const Measure* startMeasure = sc->tick2measure(windowStart);
    if (!startMeasure) {
        startMeasure = sc->firstMeasure();
    }
    if (!startMeasure) {
        return;
    }

    for (const Segment* s = startMeasure->first(SegmentType::ChordRest);
         s && s->tick() <= windowEnd;
         s = s->next1(SegmentType::ChordRest)) {
        const Fraction segTick = s->tick();
        if (segTick < windowStart) {
            continue;
        }

        const Measure* m = s->measure();
        const BeatType bt = shv::safeBeatType(m, s);
        const double bw = shv::beatTypeToWeight(bt, prefs);

        const double beatsFromTick =
            std::abs((segTick - tick).ticks())
            / static_cast<double>(Constants::DIVISION);
        const double decay = shv::timeDecay(beatsFromTick);

        const bool isLookahead = (segTick > tick);
        const double lookaheadMul = isLookahead ? shv::LOOKAHEAD_WEIGHT : 1.0;

        struct NoteInfo { int ppitch; double durationQn; };
        std::vector<NoteInfo> segNotes;
        int lowestPitch = std::numeric_limits<int>::max();

        for (std::size_t si = 0; si < sc->nstaves(); ++si) {
            if (excludeStaves.count(si) || !staffIsEligible(sc, si, tick)) {
                continue;
            }
            for (int v = 0; v < VOICES; ++v) {
                const ChordRest* cr
                    = s->cr(static_cast<track_idx_t>(si) * VOICES + v);
                if (!cr || !cr->isChord() || cr->isGrace()) {
                    continue;
                }
                const double durQn = cr->actualTicks().ticks()
                                     / static_cast<double>(Constants::DIVISION);
                for (const Note* n : toChord(cr)->notes()) {
                    if (!n->play() || !n->visible()) {
                        continue;
                    }
                    const int pp = n->ppitch();
                    segNotes.push_back({ pp, durQn });
                    if (pp < lowestPitch) {
                        lowestPitch = pp;
                    }
                }
            }
        }

        for (const auto& ni : segNotes) {
            KeyModeAnalyzer::PitchContext p;
            p.pitch          = ni.ppitch;
            p.durationWeight = ni.durationQn * decay * lookaheadMul;
            p.beatWeight     = bw;
            p.isBass         = (ni.ppitch == lowestPitch);
            ctx.push_back(p);
        }
    }
}

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

std::vector<mu::engraving::Fraction>
detectOnsetSubBoundaries(const mu::engraving::Score* sc,
                         const mu::engraving::Fraction& startTick,
                         const mu::engraving::Fraction& endTick,
                         const std::set<std::size_t>& excludeStaves,
                         double threshold)
{
    using namespace mu::engraving;

    auto popcount16 = [](uint16_t x) -> int {
        int n = 0;
        while (x) { n += x & 1; x >>= 1; }
        return n;
    };

    std::vector<Fraction> subBoundaries;

    const Segment* firstSeg = sc->tick2segment(startTick, true, SegmentType::ChordRest);
    if (!firstSeg) {
        return subBoundaries;
    }

    struct OnsetWindow {
        Fraction tick;
        uint16_t bits = 0;
    };
    std::vector<OnsetWindow> onsets;

    for (const Segment* s = firstSeg;
         s && s->tick() < endTick;
         s = s->next1(SegmentType::ChordRest)) {

        uint16_t bits = 0;
        const int segTick = s->tick().ticks();

        for (std::size_t si = 0; si < sc->nstaves(); ++si) {
            if (excludeStaves.count(si) || !staffIsEligible(sc, si, s->tick())) {
                continue;
            }
            for (int v = 0; v < VOICES; ++v) {
                const ChordRest* cr = s->cr(static_cast<track_idx_t>(si) * VOICES + v);
                if (!cr || !cr->isChord() || cr->isGrace()) {
                    continue;
                }
                if (cr->tick().ticks() != segTick) {
                    continue;
                }
                for (const Note* n : toChord(cr)->notes()) {
                    if (!n->play() || !n->visible()) {
                        continue;
                    }
                    bits |= static_cast<uint16_t>(1u << (n->ppitch() % 12));
                }
            }
        }

        if (bits != 0) {
            onsets.push_back({ s->tick(), bits });
        }
    }

    if (onsets.size() < 2) {
        return subBoundaries;
    }

    const int minGapTicks = 2 * Constants::DIVISION;

    uint16_t prevBits = onsets[0].bits;
    Fraction lastBoundaryTick = startTick;

    for (std::size_t i = 1; i < onsets.size(); ++i) {
        const uint16_t bits     = onsets[i].bits;
        const uint16_t inter    = prevBits & bits;
        const uint16_t uni      = prevBits | bits;
        const int interCount    = popcount16(inter);
        const int uniCount      = popcount16(uni);
        const double jaccard    = (uniCount > 0)
                                  ? (1.0 - static_cast<double>(interCount) / uniCount)
                                  : 0.0;

        const int gapTicks = (onsets[i].tick - lastBoundaryTick).ticks();
        if (jaccard >= threshold && gapTicks >= minGapTicks) {
            subBoundaries.push_back(onsets[i].tick);
            lastBoundaryTick = onsets[i].tick;
            prevBits = bits;
        }
    }

    return subBoundaries;
}

std::vector<mu::engraving::Fraction>
detectBassMovementSubBoundaries(const mu::engraving::Score* sc,
                                const mu::engraving::Fraction& startTick,
                                const mu::engraving::Fraction& endTick,
                                const std::set<std::size_t>& excludeStaves,
                                int minGapTicks)
{
    using namespace mu::engraving;

    std::vector<Fraction> subBoundaries;

    const Segment* firstSeg = sc->tick2segment(startTick, true, SegmentType::ChordRest);
    if (!firstSeg) {
        return subBoundaries;
    }

    struct BassOnset {
        Fraction tick;
        int bassPC = -1;
    };
    std::vector<BassOnset> onsets;

    for (const Segment* s = firstSeg;
         s && s->tick() < endTick;
         s = s->next1(SegmentType::ChordRest)) {

        const int segTick = s->tick().ticks();
        int lowestPitch = std::numeric_limits<int>::max();
        int lowestPC    = -1;

        for (std::size_t si = 0; si < sc->nstaves(); ++si) {
            if (excludeStaves.count(si) || !staffIsEligible(sc, si, s->tick())) {
                continue;
            }
            for (int v = 0; v < VOICES; ++v) {
                const ChordRest* cr = s->cr(static_cast<track_idx_t>(si) * VOICES + v);
                if (!cr || !cr->isChord() || cr->isGrace()) {
                    continue;
                }
                if (cr->tick().ticks() != segTick) {
                    continue;
                }
                for (const Note* n : toChord(cr)->notes()) {
                    if (!n->play() || !n->visible()) {
                        continue;
                    }
                    const int pitch = n->ppitch();
                    if (pitch < lowestPitch) {
                        lowestPitch = pitch;
                        lowestPC    = pitch % 12;
                    }
                }
            }
        }

        if (lowestPC >= 0) {
            onsets.push_back({ s->tick(), lowestPC });
        }
    }

    if (onsets.empty()) {
        return subBoundaries;
    }

    int  lastBoundaryBassPC  = onsets[0].bassPC;
    Fraction lastBoundaryTick = startTick;

    for (std::size_t i = 1; i < onsets.size(); ++i) {
        const int    curPC     = onsets[i].bassPC;
        const int    gapTicks  = (onsets[i].tick - lastBoundaryTick).ticks();

        if (curPC != lastBoundaryBassPC && gapTicks >= minGapTicks) {
            subBoundaries.push_back(onsets[i].tick);
            lastBoundaryTick   = onsets[i].tick;
            lastBoundaryBassPC = curPC;
        }
    }

    return subBoundaries;
}

mu::composing::analysis::ChordTemporalContext
findTemporalContext(const mu::engraving::Score* sc,
                    const mu::engraving::Segment* seg,
                    const std::set<std::size_t>& excludeStaves,
                    int keyFifths,
                    mu::composing::analysis::KeySigMode keyMode,
                    int currentBassPc)
{
    using namespace mu::engraving;
    using namespace mu::composing::analysis;

    ChordTemporalContext temporalCtx;
    const Fraction tick = seg->tick();
    const auto chordAnalyzer = ChordAnalyzerFactory::create();

    // IMPLEMENTATION GAP (not a design constraint): this bridge-path context builder
    // looks BACKWARD only — via seg->prev1() it populates previousRootPc /
    // previousQuality / previousBassPc / bassIsStepwiseFromPrevious. It does NOT set the
    // forward-lookahead fields (nextRootPc, nextBassPc, bassIsStepwiseToNext) or the
    // Step 1/2 progression fields (previousWinnerScore/Margin/RootPcWeight,
    // previousDistinctPcs). Consequently stepwiseBassLookaheadBonus and wSeqBonus never
    // fire on the bridge path, unlike the batch path which supplies nextRootPc. This is
    // a gap, not a limitation: seg->next1(SegmentType::ChordRest) is available and used
    // elsewhere in this file; a forward walk mirroring the backward one below would close
    // it. Tracked in docs/layer_architecture_audit.md Finding 3.

    for (const Segment* s = seg->prev1(SegmentType::ChordRest);
         s != nullptr;
         s = s->prev1(SegmentType::ChordRest)) {
        bool hasAttacks = false;
        for (std::size_t si = 0; si < sc->nstaves() && !hasAttacks; ++si) {
            if (excludeStaves.count(si) || !staffIsEligible(sc, si, tick)) {
                continue;
            }
            for (int v = 0; v < VOICES && !hasAttacks; ++v) {
                const ChordRest* cr
                    = s->cr(static_cast<track_idx_t>(si) * VOICES + v);
                if (cr && cr->isChord() && !cr->isGrace()) {
                    hasAttacks = true;
                }
            }
        }
        if (!hasAttacks) {
            continue;
        }

        std::vector<SoundingNote> prevSounding;
        collectSoundingAt(sc, s, excludeStaves, prevSounding);
        if (!prevSounding.empty()) {
            const auto prevTones = buildTones(prevSounding);
            mu::composing::analysis::PostScoringGateContext prevGateCtx;
            auto prevResults =
                chordAnalyzer->analyzeChord(prevTones, keyFifths, keyMode, nullptr,
                                            mu::composing::analysis::kDefaultChordAnalyzerPreferences,
                                            &prevGateCtx);
            if (!prevResults.empty()) {
                mu::composing::analysis::applyIter8691Pedal(
                    prevResults,
                    prevGateCtx,
                    nullptr,
                    mu::composing::analysis::kDefaultChordAnalyzerPreferences);
                mu::composing::analysis::applyPostScoringGates(
                    prevResults,
                    mu::composing::analysis::kDefaultChordAnalyzerPreferences,
                    nullptr,
                    prevGateCtx);
                temporalCtx.previousRootPc  = prevResults.front().identity.rootPc;
                temporalCtx.previousQuality = prevResults.front().identity.quality;
                temporalCtx.previousBassPc  = prevResults.front().identity.bassPc;
            }
        }
        break;
    }

    if (currentBassPc != -1 && temporalCtx.previousBassPc != -1) {
        temporalCtx.bassIsStepwiseFromPrevious =
            isDiatonicStep(temporalCtx.previousBassPc, currentBassPc);
    }

    return temporalCtx;
}

} // namespace mu::composing::analysis::engravingbridge
