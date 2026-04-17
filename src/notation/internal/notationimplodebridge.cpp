/*
 * SPDX-License-Identifier: GPL-3.0-only
 * MuseScore-Studio-CLA-applies
 *
 * MuseScore Studio
 * Music Composition & Notation
 *
 * Copyright (C) 2021 MuseScore Limited
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

// ── Implode-to-chord-staff bridge ────────────────────────────────────────────
//
// Implements populateChordTrack() (declared in composing/analysis/region/harmonicrhythm.h).
//
// This file is intentionally separate from notationcomposingbridge.cpp so that
// a clean-branch submission of the chord-symbol annotation feature does not need
// to carry the chord-staff implode machinery.

#include <limits>
#include <set>
#include <string>

#include "engraving/dom/chord.h"
#include "engraving/dom/durationtype.h"
#include "engraving/dom/factory.h"
#include "engraving/dom/harmony.h"
#include "engraving/dom/key.h"
#include "engraving/dom/keysig.h"
#include "engraving/dom/masterscore.h"
#include "engraving/dom/measure.h"
#include "engraving/dom/note.h"
#include "engraving/dom/part.h"
#include "engraving/dom/rest.h"
#include "engraving/dom/pitchspelling.h"
#include "engraving/dom/property.h"
#include "engraving/dom/segment.h"
#include "engraving/dom/sig.h"
#include "engraving/dom/staff.h"
#include "engraving/dom/stafftext.h"
#include "engraving/dom/tie.h"
#include "engraving/dom/tuplet.h"
#include "engraving/editing/editkeysig.h"
#include "engraving/types/constants.h"

#include "composing/analysis/chord/analysisutils.h"
#include "composing/analysis/chord/chordanalyzer.h"
#include "composing/analysis/region/harmonicrhythm.h"
#include "composing/analysis/key/keymodeanalyzer.h"
#include "composing/icomposingchordstaffconfiguration.h"
#include "modularity/ioc.h"

#include "notationanalysisinternal.h"
#include "notationcomposingbridge.h"
#include "notationcomposingbridgehelpers.h"
#include "notationimplodebridge.h"

using namespace mu::engraving;
using mu::notation::internal::scoreNoteSpelling;

namespace {

constexpr double kTentativeKeyExposureThreshold = 0.5;
constexpr double kAssertiveKeyExposureThreshold = 0.8;

bool supportsTentativeKeyExposure(const mu::composing::analysis::KeyModeAnalysisResult& keyModeResult)
{
    return keyModeResult.normalizedConfidence >= kTentativeKeyExposureThreshold;
}

bool supportsAssertiveKeyExposure(const mu::composing::analysis::KeyModeAnalysisResult& keyModeResult)
{
    return keyModeResult.normalizedConfidence >= kAssertiveKeyExposureThreshold;
}

int keyExposureBucket(double confidence)
{
    if (confidence < kTentativeKeyExposureThreshold) {
        return 0;
    }
    if (confidence < kAssertiveKeyExposureThreshold) {
        return 1;
    }
    return 2;
}

double ticksToQuarterNoteBeats(int ticks)
{
    return static_cast<double>(ticks) / static_cast<double>(mu::engraving::Constants::DIVISION);
}

const char* fallbackModeSuffix(mu::composing::analysis::KeySigMode mode)
{
    return mu::composing::analysis::keyModeIsMajor(mode)
           ? mu::composing::analysis::keyModeSuffix(mu::composing::analysis::KeySigMode::Ionian)
           : mu::composing::analysis::keyModeSuffix(mu::composing::analysis::KeySigMode::Aeolian);
}

std::string keyAnnotationBaseLabel(int keyFifths,
                                   mu::composing::analysis::KeySigMode mode,
                                   double confidence,
                                   double modeNameConfidenceThreshold)
{
    const char* suffix = confidence >= modeNameConfidenceThreshold
                         ? mu::composing::analysis::keyModeSuffix(mode)
                         : fallbackModeSuffix(mode);

    return std::string(mu::composing::analysis::keyModeTonicName(keyFifths, mode))
           + " " + suffix;
}

std::string sanitizeChordTrackSymbolForHarmonyRenderer(const std::string& symbol)
{
    if (symbol.find("sus#5") == std::string::npos) {
        return symbol;
    }

    std::string sanitized = symbol;
    size_t pos = 0;
    while ((pos = sanitized.find("sus#5", pos)) != std::string::npos) {
        sanitized.replace(pos, 5, "sus(add#5)");
        pos += std::string("sus(add#5)").size();
    }

    return sanitized;
}

struct KeyAnnotationCandidate {
    size_t regionIdx = 0;
    size_t representativeRegionIdx = 0;
    int keySignatureFifths = 0;
    mu::composing::analysis::KeySigMode representativeMode = mu::composing::analysis::KeySigMode::Ionian;
    std::string baseLabel;
    bool hasAssertiveExposure = false;
    bool addQuestionMark = false;
    bool isOpeningRun = false;
};

std::vector<KeyAnnotationCandidate> collectStableKeyAnnotationCandidates(
    const std::vector<mu::composing::analysis::HarmonicRegion>& regions,
    double modeNameConfidenceThreshold,
    double minKeyStabilityBeats)
{
    using mu::composing::analysis::HarmonicRegion;

    struct PendingRun {
        bool active = false;
        size_t firstRegionIdx = 0;
        size_t representativeRegionIdx = 0;
        int startTick = 0;
        int endTick = 0;
        int keySignatureFifths = 0;
        mu::composing::analysis::KeySigMode representativeMode = mu::composing::analysis::KeySigMode::Ionian;
        std::string baseLabel;
        bool hasTentativeExposure = false;
        bool hasAssertiveExposure = false;
    };

    std::vector<KeyAnnotationCandidate> candidates;
    if (regions.empty()) {
        return candidates;
    }

    int lastWrittenKeyFifths = std::numeric_limits<int>::min();
    std::string lastWrittenLabel;
    PendingRun run;

    auto startRun = [&](size_t regionIdx, const HarmonicRegion& region) {
        run.active = true;
        run.firstRegionIdx = regionIdx;
        run.representativeRegionIdx = regionIdx;
        run.startTick = region.startTick;
        run.endTick = region.endTick;
        run.keySignatureFifths = region.keyModeResult.keySignatureFifths;
        run.representativeMode = region.keyModeResult.mode;
        run.baseLabel = keyAnnotationBaseLabel(region.keyModeResult.keySignatureFifths,
                                               region.keyModeResult.mode,
                                               region.keyModeResult.normalizedConfidence,
                                               modeNameConfidenceThreshold);
        run.hasTentativeExposure = supportsTentativeKeyExposure(region.keyModeResult);
        run.hasAssertiveExposure = supportsAssertiveKeyExposure(region.keyModeResult);
    };

    auto finishRun = [&]() {
        if (!run.active) {
            return;
        }

        const double durationBeats = ticksToQuarterNoteBeats(run.endTick - run.startTick);
        const bool isOpeningRun = (run.firstRegionIdx == 0);
        if (!run.hasTentativeExposure || (!isOpeningRun && durationBeats < minKeyStabilityBeats)) {
            run = PendingRun{};
            return;
        }

        if (run.keySignatureFifths == lastWrittenKeyFifths && run.baseLabel == lastWrittenLabel) {
            run = PendingRun{};
            return;
        }

        KeyAnnotationCandidate candidate;
        candidate.regionIdx = run.firstRegionIdx;
        candidate.representativeRegionIdx = run.representativeRegionIdx;
        candidate.keySignatureFifths = run.keySignatureFifths;
        candidate.representativeMode = run.representativeMode;
        candidate.baseLabel = run.baseLabel;
        candidate.hasAssertiveExposure = run.hasAssertiveExposure;
        candidate.addQuestionMark = !run.hasAssertiveExposure;
        candidate.isOpeningRun = (run.firstRegionIdx == 0);
        candidates.push_back(std::move(candidate));

        lastWrittenKeyFifths = run.keySignatureFifths;
        lastWrittenLabel = run.baseLabel;
        run = PendingRun{};
    };

    for (size_t regionIdx = 0; regionIdx < regions.size(); ++regionIdx) {
        const auto& region = regions[regionIdx];
        const std::string regionBaseLabel = keyAnnotationBaseLabel(region.keyModeResult.keySignatureFifths,
                                                                   region.keyModeResult.mode,
                                                                   region.keyModeResult.normalizedConfidence,
                                                                   modeNameConfidenceThreshold);

        if (!run.active) {
            startRun(regionIdx, region);
            continue;
        }

        const bool sameDisplayedKey = run.keySignatureFifths == region.keyModeResult.keySignatureFifths
                                      && run.baseLabel == regionBaseLabel;
        if (!sameDisplayedKey) {
            finishRun();
            startRun(regionIdx, region);
            continue;
        }

        run.endTick = region.endTick;
        run.hasTentativeExposure = run.hasTentativeExposure || supportsTentativeKeyExposure(region.keyModeResult);
        if (!run.hasAssertiveExposure && supportsAssertiveKeyExposure(region.keyModeResult)) {
            run.hasAssertiveExposure = true;
            run.representativeRegionIdx = regionIdx;
            run.representativeMode = region.keyModeResult.mode;
        }
    }

    finishRun();
    return candidates;
}

std::vector<mu::engraving::Fraction> collectSourceInferenceTicks(
    const mu::engraving::Score* score,
    const mu::engraving::Fraction& startTick,
    const mu::engraving::Fraction& endTick,
    const std::set<size_t>& excludeStaves)
{
    using namespace mu::engraving;

    std::vector<Fraction> ticks;
    std::set<int> seenTicks;
    ticks.push_back(startTick);
    seenTicks.insert(startTick.ticks());

    for (const Segment* seg = score->tick2segment(startTick, true, SegmentType::ChordRest);
         seg && seg->tick() < endTick;
         seg = seg->next1(SegmentType::ChordRest)) {
        bool hasSourceChord = false;
        for (size_t si = 0; si < score->nstaves() && !hasSourceChord; ++si) {
            if (excludeStaves.count(si) || !mu::notation::internal::staffIsEligible(score, si, seg->tick())) {
                continue;
            }

            for (int voice = 0; voice < VOICES && !hasSourceChord; ++voice) {
                const ChordRest* chordRest = seg->cr(static_cast<track_idx_t>(si) * VOICES + voice);
                hasSourceChord = chordRest && chordRest->isChord() && !chordRest->isGrace();
            }
        }

        if (hasSourceChord && seenTicks.insert(seg->tick().ticks()).second) {
            ticks.push_back(seg->tick());
        }
    }

    return ticks;
}

bool sameUserFacingInference(const mu::composing::analysis::HarmonicRegion& lhs,
                             const mu::composing::analysis::HarmonicRegion& rhs)
{
    return lhs.chordResult.identity.rootPc == rhs.chordResult.identity.rootPc
           && lhs.chordResult.identity.quality == rhs.chordResult.identity.quality
           && lhs.keyModeResult.keySignatureFifths == rhs.keyModeResult.keySignatureFifths
           && lhs.keyModeResult.mode == rhs.keyModeResult.mode
           && keyExposureBucket(lhs.keyModeResult.normalizedConfidence)
              == keyExposureBucket(rhs.keyModeResult.normalizedConfidence);
}


// Returns the tuplet on the specified track at this segment, or nullptr if none.
mu::engraving::Tuplet* findTupletOnTrack(
    mu::engraving::Segment* seg,
    mu::engraving::track_idx_t track)
{
    using namespace mu::engraving;
    if (!seg) {
        return nullptr;
    }
    EngravingItem* el = seg->element(track);
    if (!el || !el->isChordRest()) {
        return nullptr;
    }
    return toChordRest(el)->tuplet();
}

mu::engraving::Chord* addChordChainFromPitches(
    mu::engraving::Score* sc,
    const mu::engraving::Fraction& startTick,
    const mu::engraving::Fraction& endTick,
    mu::engraving::track_idx_t track,
    const std::vector<int>& midiPitches,
    int keySignatureFifths)
{
    using namespace mu::engraving;

    if (endTick <= startTick || midiPitches.empty()) {
        return nullptr;
    }

    Measure* startMeasure = sc->tick2measure(startTick);
    if (!startMeasure) {
        return nullptr;
    }

    Segment* seg = startMeasure->undoGetSegment(SegmentType::ChordRest, startTick);
    if (!seg) {
        return nullptr;
    }

    const Key key = Key(keySignatureFifths);
    const Fraction totalDur = endTick - startTick;

    Tuplet* srcTuplet = findTupletOnTrack(seg, track);
    if (srcTuplet) {
        const Fraction elemDur = srcTuplet->baseLen().fraction()
                                 * srcTuplet->ratio().denominator()
                                 / srcTuplet->ratio().numerator();
        if (totalDur == elemDur) {
            Measure* m = sc->tick2measure(startTick);
            if (!m) {
                return nullptr;
            }


            // Remove any stale ChordRest elements on the target track within the tuplet span, regardless of their tuplet association.
            const Fraction tupFrom = srcTuplet->tick();
            const Fraction tupTo   = tupFrom + srcTuplet->ticks();
            for (Segment* clearSeg = sc->tick2segment(tupFrom, true, SegmentType::ChordRest);
                 clearSeg && clearSeg->tick() < tupTo;
                 clearSeg = clearSeg->next1(SegmentType::ChordRest)) {
                ChordRest* stale = toChordRest(clearSeg->element(track));
                if (stale) {
                    sc->undoRemoveElement(stale);
                }
            }
            // Now make the gap for the tuplet.
            Segment* tupSeg = sc->tick2segment(srcTuplet->tick(), true, SegmentType::ChordRest);
            if (tupSeg) {
                sc->makeGap(tupSeg, track, srcTuplet->ticks(), nullptr);
            }

            Tuplet* dstTuplet = Factory::createTuplet(m);
            dstTuplet->setRatio(srcTuplet->ratio());
            dstTuplet->setBaseLen(srcTuplet->baseLen());
            dstTuplet->setTicks(srcTuplet->ticks());
            dstTuplet->setTrack(track);
            dstTuplet->setTick(srcTuplet->tick());
            dstTuplet->setParent(m);

            Fraction slotTick = srcTuplet->tick();
            const int nSlots = srcTuplet->ratio().numerator();
            for (int i = 0; i < nSlots; ++i) {
                Rest* r = Factory::createRest(sc->dummy()->segment());
                r->setTrack(track);
                r->setDurationType(dstTuplet->baseLen());
                r->setTicks(dstTuplet->baseLen().fraction());
                r->setTuplet(dstTuplet);
                sc->undoAddCR(r, m, slotTick);
                slotTick += elemDur;
            }

            seg = m->undoGetSegment(SegmentType::ChordRest, startTick);

            // Remove any rest in the tuplet slot where the chord will be added
            if (seg) {
                ChordRest* crInSlot = toChordRest(seg->element(track));
                if (crInSlot && crInSlot->tuplet() == dstTuplet && crInSlot->isRest()) {
                    sc->undoRemoveElement(crInSlot);
                }
            }

            Chord* chord = Factory::createChord(sc->dummy()->segment());
            chord->setTrack(track);
            chord->setDurationType(dstTuplet->baseLen());
            chord->setTicks(dstTuplet->baseLen().fraction());
            chord->setTuplet(dstTuplet);

            for (int pitch : midiPitches) {
                Note* note = Factory::createNote(chord);
                note->setPitch(pitch);
                const int tpc = pitch2tpc(pitch, key, Prefer::NEAREST);
                note->setTpc1(tpc);
                note->setTpc2(tpc);
                chord->add(note);
            }

            sc->undoAddCR(chord, m, startTick);
            return chord;
        }
    }

    Fraction remaining = totalDur;
    Fraction tick = startTick;
    Chord* firstChord = nullptr;
    Note* prevNote0 = nullptr;

    while (remaining > Fraction(0, 1)) {
        if (track % VOICES != 0) {
            sc->expandVoice(seg, track);
        }

        const Fraction segCapacity = seg->measure()->endTick() - tick;
        const Fraction chunkDur = std::min(remaining, segCapacity);
        const Fraction gapped = sc->makeGap(seg, track, chunkDur, nullptr);
        if (gapped.isZero()) {
            break;
        }

        const std::vector<TDuration> durations = toDurationList(gapped, true);
        Fraction chunkTick = tick;
        Note* prevNoteLocal = prevNote0;

        for (const TDuration& d : durations) {
            Measure* measure = sc->tick2measure(chunkTick);
            if (!measure) {
                break;
            }

            Chord* chord = Factory::createChord(sc->dummy()->segment());
            chord->setTrack(track);
            chord->setDurationType(d);
            chord->setTicks(d.fraction());

            for (int pitch : midiPitches) {
                Note* note = Factory::createNote(chord);
                note->setPitch(pitch);
                const int tpc = pitch2tpc(pitch, key, Prefer::NEAREST);
                note->setTpc1(tpc);
                note->setTpc2(tpc);
                chord->add(note);
            }

            sc->undoAddCR(chord, measure, chunkTick);

            if (!firstChord) {
                firstChord = chord;
            }

            if (prevNoteLocal) {
                const Chord* prevChord = prevNoteLocal->chord();
                for (size_t i = 0; i < std::min(prevChord->notes().size(), chord->notes().size()); ++i) {
                    Note* n1 = prevChord->notes()[i];
                    Note* n2 = chord->notes()[i];
                    Tie* tie = Factory::createTie(sc->dummy());
                    tie->setStartNote(n1);
                    tie->setEndNote(n2);
                    tie->setTick(n1->tick());
                    tie->setTick2(n2->tick());
                    tie->setTrack(track);
                    n1->setTieFor(tie);
                    n2->setTieBack(tie);
                    sc->undoAddElement(tie);
                }
            }

            prevNoteLocal = chord->notes().empty() ? nullptr : chord->notes().front();
            chunkTick += d.fraction();
        }

        prevNote0 = prevNoteLocal;
        remaining -= gapped;
        tick = chunkTick;

        if (remaining > Fraction(0, 1)) {
            Measure* nextMeasure = sc->tick2measure(tick);
            seg = nextMeasure ? nextMeasure->undoGetSegment(SegmentType::ChordRest, tick) : nullptr;
            if (!seg) {
                break;
            }
        }
    }

    return firstChord;
}

void setExplicitRestRange(mu::engraving::Score* sc,
                          const mu::engraving::Fraction& startTick,
                          mu::engraving::track_idx_t track,
                          const mu::engraving::Fraction& duration,
                          mu::engraving::Tuplet* tuplet = nullptr)
{
    if (!sc || duration <= mu::engraving::Fraction(0, 1)) {
        return;
    }

    sc->setRest(startTick, track, duration, false, tuplet, false);
}

const std::array<int, 7>& keyModeScaleIntervals(mu::composing::analysis::KeySigMode mode)
{
    static constexpr std::array<std::array<int, 7>, 21> MODE_SCALES = {{
        { 0, 2, 4, 5, 7, 9, 11 },
        { 0, 2, 3, 5, 7, 9, 10 },
        { 0, 1, 3, 5, 7, 8, 10 },
        { 0, 2, 4, 6, 7, 9, 11 },
        { 0, 2, 4, 5, 7, 9, 10 },
        { 0, 2, 3, 5, 7, 8, 10 },
        { 0, 1, 3, 5, 6, 8, 10 },
        { 0, 2, 3, 5, 7, 9, 11 },
        { 0, 1, 3, 5, 7, 9, 10 },
        { 0, 2, 4, 6, 8, 9, 11 },
        { 0, 2, 4, 6, 7, 9, 10 },
        { 0, 2, 4, 5, 7, 8, 10 },
        { 0, 2, 3, 5, 6, 8, 10 },
        { 0, 1, 3, 4, 6, 8, 10 },
        { 0, 2, 3, 5, 7, 8, 11 },
        { 0, 1, 3, 5, 6, 9, 10 },
        { 0, 2, 4, 5, 8, 9, 11 },
        { 0, 2, 3, 6, 7, 9, 10 },
        { 0, 1, 4, 5, 7, 8, 10 },
        { 0, 3, 4, 6, 7, 9, 11 },
        { 0, 1, 3, 4, 6, 8, 9 },
    }};

    const size_t modeIdx = mu::composing::analysis::keyModeIndex(mode);
    return MODE_SCALES[modeIdx < MODE_SCALES.size() ? modeIdx : 0];
}

} // anonymous namespace

namespace mu::notation {

bool populateChordTrack(
    mu::engraving::Score* score,
    const mu::engraving::Fraction& startTick,
    const mu::engraving::Fraction& endTick,
    mu::engraving::staff_idx_t trebleStaffIdx,
    bool useCollectedTones)
{
    using namespace mu::engraving;
    using namespace mu::composing::analysis;
    using mu::composing::analysis::KeySigMode;  // disambiguate from mu::engraving::KeyMode

    if (!score || endTick <= startTick) {
        return false;
    }

    static muse::GlobalInject<mu::composing::IComposingChordStaffConfiguration> chordStaffConfig;
    const mu::composing::IComposingChordStaffConfiguration* prefs = chordStaffConfig.get().get();
    static muse::GlobalInject<mu::composing::IComposingAnalysisConfiguration> analysisConfig;
    const mu::composing::IComposingAnalysisConfiguration* analysisPrefs = analysisConfig.get().get();

    const staff_idx_t bassStaffIdx = trebleStaffIdx + 1;
    if (bassStaffIdx >= score->nstaves()) {
        return false;
    }

    // The target staves are excluded from the analysis input.
    const std::set<size_t> excludeStaves = {
        static_cast<size_t>(trebleStaffIdx),
        static_cast<size_t>(bassStaffIdx)
    };

    // ── Analyze ──────────────────────────────────────────────────────────────
    const auto displayRegions = mu::notation::internal::prepareUserFacingHarmonicRegions(score,
                                                                                          startTick,
                                                                                          endTick,
                                                                                          excludeStaves);
    std::vector<HarmonicRegion> regions;
    const auto inferenceTicks = collectSourceInferenceTicks(score, startTick, endTick, excludeStaves);

    auto selectDisplayRegionForTick = [&](const Fraction& tick) -> const HarmonicRegion* {
        const int tickValue = tick.ticks();
        const auto containingRegion = std::find_if(displayRegions.begin(), displayRegions.end(), [tickValue](const auto& region) {
            return region.startTick <= tickValue && tickValue < region.endTick;
        });
        if (containingRegion != displayRegions.end()) {
            return &*containingRegion;
        }

        const Measure* measure = score->tick2measure(tick);
        const auto nextRegion = std::find_if(displayRegions.begin(), displayRegions.end(), [tickValue](const auto& region) {
            return region.startTick >= tickValue;
        });
        if (measure && nextRegion != displayRegions.end()) {
            const Measure* nextMeasure = score->tick2measure(Fraction::fromTicks(nextRegion->startTick));
            if (nextMeasure == measure) {
                return &*nextRegion;
            }
        }

        const auto previousRegion = std::find_if(displayRegions.rbegin(), displayRegions.rend(), [tickValue](const auto& region) {
            return region.endTick <= tickValue;
        });
        if (measure && previousRegion != displayRegions.rend()) {
            const Measure* previousMeasure = score->tick2measure(Fraction::fromTicks(previousRegion->startTick));
            if (previousMeasure == measure) {
                return &*previousRegion;
            }
        }

        if (nextRegion != displayRegions.end()) {
            return &*nextRegion;
        }
        if (previousRegion != displayRegions.rend()) {
            return &*previousRegion;
        }

        return nullptr;
    };

    regions.reserve(inferenceTicks.size());
    for (size_t tickIndex = 0; tickIndex < inferenceTicks.size(); ++tickIndex) {
        const Fraction regionStart = inferenceTicks[tickIndex];
        const Fraction regionEnd = (tickIndex + 1 < inferenceTicks.size())
                                   ? inferenceTicks[tickIndex + 1]
                                   : endTick;
        if (regionEnd <= regionStart) {
            continue;
        }

        const HarmonicRegion* displayRegion = selectDisplayRegionForTick(regionStart);
        if (!displayRegion) {
            continue;
        }

        HarmonicRegion region = *displayRegion;
        region.startTick = regionStart.ticks();
        region.endTick = regionEnd.ticks();

        auto localTones = collectRegionTones(score, region.startTick, region.endTick, excludeStaves);
        if (!localTones.empty()) {
            region.tones = std::move(localTones);
        }

        regions.push_back(std::move(region));
    }

    if (regions.empty()) {
        return false;
    }

    // ── Clear target region ──────────────────────────────────────────────────
    // Remove all existing content (notes, rests, annotations) from both staves
    // in voice 0 within the time range.  Measure rests that extend beyond the
    // target range are split: portions outside the range become proper rests.
    const track_idx_t trebleTrack = trebleStaffIdx * VOICES;
    const track_idx_t bassTrack   = bassStaffIdx * VOICES;
    for (track_idx_t track : { trebleTrack, bassTrack }) {
        // Walk each measure overlapping the target range.
        for (Measure* m = score->tick2measure(startTick);
             m && m->tick() < endTick;
             m = m->nextMeasure()) {
            const Fraction mStart = m->tick();
            const Fraction mEnd   = m->endTick();
            const Fraction clearFrom = std::max(mStart, startTick);
            const Fraction clearTo   = std::min(mEnd, endTick);

            // ── Tuplet-aware clearing ───────────────────────────────────
            // If source tracks have a tuplet at this position, we must
            // clear the full tuplet span (not just the single-element
            // range) and avoid calling setRest for the tuplet zone — the
            // tuplet path in addChordChainFromPitches handles it.
            Segment* chkSeg = score->tick2segment(clearFrom, true,
                                                   SegmentType::ChordRest);
            Tuplet* srcTup = chkSeg ? findTupletOnTrack(chkSeg, track)
                                    : nullptr;
            if (srcTup) {
                const Fraction tupFrom = srcTup->tick();
                const Fraction tupTo   = tupFrom + srcTup->ticks();

                // Remove non-tuplet ChordRests that overlap the full
                // tuplet span.  Split them outside the tuplet range.
                std::vector<ChordRest*> toRemove;
                for (Segment* seg = m->first(SegmentType::ChordRest);
                     seg; seg = seg->next(SegmentType::ChordRest)) {
                    ChordRest* cr = toChordRest(seg->element(track));
                    if (!cr || cr->tuplet()) {
                        continue;
                    }
                    const Fraction crStart = cr->tick();
                    const Fraction crEnd   = crStart + cr->actualTicks();
                    if (crStart < tupTo && crEnd > tupFrom) {
                        toRemove.push_back(cr);
                    }
                }

                for (ChordRest* cr : toRemove) {
                    const Fraction crStart = cr->tick();
                    const Fraction crEnd   = crStart + cr->actualTicks();

                    // Extract pitches before removal (for chord cloning).
                    std::vector<int> pitches;
                    int crKeyFifths = 0;
                    if (cr->isChord()) {
                        for (const Note* n : toChord(cr)->notes()) {
                            pitches.push_back(n->pitch());
                        }
                        // Get key context for TPC derivation.
                        crKeyFifths = static_cast<int>(
                            cr->staff()->keySigEvent(crStart).key());
                    }

                    score->undoRemoveElement(cr);

                    // Recreate content outside the tuplet range.
                    // If it was a chord, clone as tied notes; if rest,
                    // create rests.
                    if (crStart < tupFrom) {
                        if (!pitches.empty()) {
                            addChordChainFromPitches(
                                score, crStart, tupFrom, track,
                                pitches, crKeyFifths);
                        } else {
                            setExplicitRestRange(score, crStart, track,
                                                 tupFrom - crStart);
                        }
                    }
                    if (crEnd > tupTo) {
                        if (!pitches.empty()) {
                            addChordChainFromPitches(
                                score, tupTo, crEnd, track,
                                pitches, crKeyFifths);
                        } else {
                            setExplicitRestRange(score, tupTo, track,
                                                 crEnd - tupTo);
                        }
                    }
                }
                // No setRest inside the tuplet range — tuplet path will
                // call makeGap + create tuplet + fill with rests/notes.
                continue;
            }

            // ── Normal (non-tuplet) clearing ────────────────────────────
            std::vector<ChordRest*> toRemove;
            for (Segment* seg = m->first(SegmentType::ChordRest);
                 seg; seg = seg->next(SegmentType::ChordRest)) {
                ChordRest* cr = toChordRest(seg->element(track));
                if (!cr) {
                    continue;
                }
                const Fraction crStart = cr->tick();
                const Fraction crEnd   = crStart + cr->actualTicks();
                if (crStart < clearTo && crEnd > clearFrom) {
                    toRemove.push_back(cr);
                }
            }

            for (ChordRest* cr : toRemove) {
                const Fraction crStart = cr->tick();
                const Fraction crEnd   = crStart + cr->actualTicks();

                score->undoRemoveElement(cr);

                // Re-fill portions outside [clearFrom, clearTo) with rests.
                if (crStart < clearFrom) {
                    setExplicitRestRange(score, crStart, track,
                                         clearFrom - crStart);
                }
                if (crEnd > clearTo) {
                    setExplicitRestRange(score, clearTo, track,
                                         crEnd - clearTo);
                }
            }

            // Fill the cleared range with rests (overwritten by notes later).
            if (!toRemove.empty()) {
                setExplicitRestRange(score, clearFrom, track,
                                     clearTo - clearFrom);
            }
        }
    }

    // Remove existing annotations (Harmony + StaffText) on the target staves.
    for (Segment* s = score->tick2segment(startTick, true, SegmentType::ChordRest);
         s && s->tick() < endTick;
         s = s->next1(SegmentType::ChordRest)) {
        std::vector<EngravingItem*> toRemove;
        for (EngravingItem* ann : s->annotations()) {
            if (!ann->isHarmony() && !ann->isStaffText()) {
                continue;
            }
            const track_idx_t t = ann->track();
            if (t / VOICES == trebleStaffIdx || t / VOICES == bassStaffIdx) {
                toRemove.push_back(ann);
            }
        }
        for (EngravingItem* ann : toRemove) {
            score->undoRemoveElement(ann);
        }
    }

    // Note: KeySig clearing is not needed here — undoChangeKeySig() in the
    // populate loop handles creating or updating key sigs at each boundary.

    const double modeNameConfidenceThreshold = analysisPrefs
                                               ? analysisPrefs->modeNameConfidenceThreshold()
                                               : 0.35;
    const double minimumDisplayDurationBeats = analysisPrefs
                                               ? analysisPrefs->minimumDisplayDurationBeats()
                                               : 0.5;
    const double minKeyStabilityBeats = analysisPrefs
                                        ? analysisPrefs->minKeyStabilityBeats()
                                        : 8.0;
    const auto keyAnnotationCandidates = collectStableKeyAnnotationCandidates(regions,
                                                                              modeNameConfidenceThreshold,
                                                                              minKeyStabilityBeats);

    // ── Populate ─────────────────────────────────────────────────────────────
    bool anyWritten = false;
    size_t nextKeyAnnotationIdx = 0;
    int prevAssertiveKeyFifths = std::numeric_limits<int>::min();
    KeySigMode prevAssertiveMode = static_cast<KeySigMode>(-1);
    size_t prevAssertiveRegionIdx = 0;

    for (size_t regionIdx = 0; regionIdx < regions.size(); ++regionIdx) {
        const auto& region = regions[regionIdx];
        const Fraction rStart = Fraction::fromTicks(region.startTick);
        const Fraction rEnd   = Fraction::fromTicks(region.endTick);
        const double regionDurationBeats = ticksToQuarterNoteBeats(region.endTick - region.startTick);
        const bool passesMinimumDisplayDuration = regionDurationBeats >= minimumDisplayDurationBeats;

        const auto& chord = region.chordResult;
        const int localKeyFifths = region.keyModeResult.keySignatureFifths;
        const KeySigMode localMode  = region.keyModeResult.mode;
        const bool allowAssertiveKeyExposure = supportsAssertiveKeyExposure(region.keyModeResult);

        // ── Key signature + mode annotation at key/mode boundaries ───────
        const bool writeKeyAnnotations = !prefs || prefs->chordStaffWriteKeyAnnotations();
        if (writeKeyAnnotations
            && nextKeyAnnotationIdx < keyAnnotationCandidates.size()
            && keyAnnotationCandidates[nextKeyAnnotationIdx].regionIdx == regionIdx) {
            const KeyAnnotationCandidate& keyCandidate = keyAnnotationCandidates[nextKeyAnnotationIdx];
            // Insert a key signature only when the inferred key differs from
            // what is already notated on the chord track staves at this tick.
            // This avoids redundant key sigs while still annotating mode changes
            // (which key signatures alone cannot express).
            const int notatedFifths = static_cast<int>(
                score->staff(trebleStaffIdx)->keySigEvent(rStart).concertKey());
            const int sourceNotatedFifths = static_cast<int>(score->staff(0)->keySigEvent(rStart).concertKey());
            const bool allowKeySignatureExposure = keyCandidate.hasAssertiveExposure
                                                   || (keyCandidate.isOpeningRun
                                                       && keyCandidate.keySignatureFifths == sourceNotatedFifths);

            if (allowKeySignatureExposure && keyCandidate.keySignatureFifths != notatedFifths) {
                Measure* m = score->tick2measure(rStart);
                if (m) {
                    KeySigEvent kse;
                    kse.setConcertKey(Key(keyCandidate.keySignatureFifths));
                    kse.setKey(Key(keyCandidate.keySignatureFifths));

                    // Staff-local key sig: create the element on each chord
                    // staff individually, without propagating to other staves.
                    for (staff_idx_t si : { trebleStaffIdx, bassStaffIdx }) {
                        Segment* ksSeg = m->undoGetSegment(
                            SegmentType::KeySig, rStart);
                        if (!ksSeg) {
                            continue;
                        }
                        const track_idx_t track = si * VOICES;
                        KeySig* existing = toKeySig(ksSeg->element(track));
                        if (existing) {
                            existing->undoChangeProperty(
                                Pid::GENERATED, false);
                            score->undo(new ChangeKeySig(
                                existing, kse, existing->showCourtesy()));
                        } else {
                            KeySig* ks = Factory::createKeySig(ksSeg);
                            ks->setParent(ksSeg);
                            ks->setTrack(track);
                            ks->setKeySigEvent(kse);
                            score->undoAddElement(ks);
                        }
                        score->staff(si)->setKey(rStart, kse);
                    }
                }
            }

            // Mode staff text above treble (e.g. "C major", "D Dorian").
            // Always written at key/mode boundaries — key sigs can't express
            // mode (keySig=0 could be C major, D Dorian, E Phrygian, …).
            Segment* textSeg = score->tick2segment(rStart, true,
                                                    SegmentType::ChordRest);
            if (textSeg) {
                using mu::composing::analysis::keyModeTonicOffset;
                using mu::composing::analysis::keyModeIsMajor;

                std::string modeLabel = keyCandidate.baseLabel;
                if (keyCandidate.addQuestionMark) {
                    modeLabel += "?";
                }

                // Key relationship annotation (skip for the first region).
                // Written separately below the first stave.
                std::string relationLabel;
                if (keyCandidate.hasAssertiveExposure
                    && prevAssertiveKeyFifths != std::numeric_limits<int>::min()) {
                    auto tonicPcFromKey = [](int fifths, KeySigMode mode) -> int {
                        const int ionianPc = ((fifths * 7) % 12 + 12) % 12;
                        return (ionianPc + keyModeTonicOffset(mode)) % 12;
                    };

                    const int prevTonicPc  = tonicPcFromKey(prevAssertiveKeyFifths, prevAssertiveMode);
                    const int localTonicPc = tonicPcFromKey(keyCandidate.keySignatureFifths,
                                                            keyCandidate.representativeMode);
                    const bool prevMajor   = keyModeIsMajor(prevAssertiveMode);
                    const bool localMajor  = keyModeIsMajor(keyCandidate.representativeMode);
                    const int fifthsDelta  = keyCandidate.keySignatureFifths - prevAssertiveKeyFifths;

                    if (prevAssertiveKeyFifths == keyCandidate.keySignatureFifths
                        && prevMajor != localMajor) {
                        relationLabel = localMajor
                            ? "(\u2192 relative maj)"
                            : "(\u2192 relative min)";
                    } else if (prevTonicPc == localTonicPc
                               && prevMajor != localMajor) {
                        relationLabel = localMajor
                            ? "(\u2192 parallel maj)"
                            : "(\u2192 parallel min)";
                    } else if (fifthsDelta == 1) {
                        relationLabel = "(\u2192 dominant key)";
                    } else if (fifthsDelta == -1) {
                        relationLabel = "(\u2192 subdominant key)";
                    } else if (fifthsDelta != 0) {
                        relationLabel = "(\u2192 "
                            + std::to_string(std::abs(fifthsDelta))
                            + (fifthsDelta > 0 ? "\u266f" : "\u266d")
                            + ")";
                    }
                }

                // Key/mode label above first stave.
                StaffText* st = Factory::createStaffText(textSeg);
                st->setTrack(trebleTrack);
                st->setParent(textSeg);
                st->setPlainText(muse::String::fromStdString(modeLabel));
                score->undoAddElement(st);

                // Key relationship annotation below first stave.
                if (!relationLabel.empty()) {
                    StaffText* rt = Factory::createStaffText(textSeg);
                    rt->setTrack(trebleTrack);
                    rt->setParent(textSeg);
                    rt->setPlacement(mu::engraving::PlacementV::BELOW);
                    rt->setPlainText(muse::String::fromStdString(relationLabel));
                    score->undoAddElement(rt);
                }

                // Modulation path: find the pivot chord (diatonic to both
                // old and new keys) by walking backward from the boundary.
                if (keyCandidate.hasAssertiveExposure
                    && prevAssertiveKeyFifths != std::numeric_limits<int>::min()
                    && (keyCandidate.keySignatureFifths != prevAssertiveKeyFifths
                        || keyCandidate.representativeMode != prevAssertiveMode)) {
                    // Build the new key's scale pitch class set.
                    const int newIonianPc = ((keyCandidate.keySignatureFifths * 7) % 12 + 12) % 12;
                    const int newTonicOffset = keyModeTonicOffset(keyCandidate.representativeMode);
                    const auto& newScale = keyModeScaleIntervals(keyCandidate.representativeMode);
                    bool newScalePcs[12] = {};
                    const int newTonicPc = (newIonianPc + newTonicOffset) % 12;
                    for (int iv : newScale) {
                        newScalePcs[(newTonicPc + iv) % 12] = true;
                    }

                    // Walk backward from the boundary looking for a chord
                    // that is diatonic to the OLD key (degree >= 0) AND whose
                    // root falls in the NEW key's scale.
                    std::string pivotText;
                    for (size_t j = keyCandidate.regionIdx; j > prevAssertiveRegionIdx; --j) {
                        const auto& prev = regions[j - 1].chordResult;
                        if (prev.function.degree < 0) {
                            continue;  // non-diatonic in old key
                        }
                        if (!newScalePcs[prev.identity.rootPc]) {
                            continue;  // not in new scale
                        }
                        // Found the pivot — format in both keys.
                        const std::string oldRoman =
                            ChordSymbolFormatter::formatRomanNumeral(prev);

                        // Re-derive degree in the new key for the roman
                        // numeral label.  Copy the chord result and override
                        // only the degree field.
                        ChordAnalysisResult pivotInNew = prev;
                        const int semisFromNewTonic =
                            ((prev.identity.rootPc - newTonicPc) % 12 + 12) % 12;
                        pivotInNew.function.degree = -1;
                        for (int d = 0; d < 7; ++d) {
                            if (newScale[d] == semisFromNewTonic) {
                                pivotInNew.function.degree = d;
                                break;
                            }
                        }
                        const std::string newRoman =
                            ChordSymbolFormatter::formatRomanNumeral(pivotInNew);

                        if (!oldRoman.empty() && !newRoman.empty()) {
                            // New format: "vi → ii"  (U+2192 RIGHT ARROW).
                            // Left side = Roman numeral in the outgoing key;
                            // right side = Roman numeral in the incoming key.
                            pivotText = oldRoman + " \u2192 " + newRoman;
                        }
                        break;
                    }

                    if (pivotText.empty()) {
                        pivotText = "direct modulation";
                    }

                    StaffText* pt = Factory::createStaffText(textSeg);
                    pt->setTrack(bassTrack);
                    pt->setParent(textSeg);
                    pt->setPlainText(
                        muse::String::fromStdString(pivotText));
                    score->undoAddElement(pt);
                }
            }

            if (keyCandidate.hasAssertiveExposure) {
                prevAssertiveKeyFifths = keyCandidate.keySignatureFifths;
                prevAssertiveMode = keyCandidate.representativeMode;
                prevAssertiveRegionIdx = keyCandidate.representativeRegionIdx;
            }

            ++nextKeyAnnotationIdx;
        }

        // ── Voicing ──────────────────────────────────────────────────────
        int bassPitch = -1;
        std::vector<int> treblePitches;

        auto assignCollectedTonesVoicing = [&]() {
            // Use the actual sounding tones from the score at their original
            // pitches, deduplicated by exact MIDI pitch.  The lowest pitch
            // goes to the bass staff; the rest go to treble.
            std::set<int> seen;
            std::vector<int> uniquePitches;
            for (const auto& tone : region.tones) {
                if (seen.insert(tone.pitch).second) {
                    uniquePitches.push_back(tone.pitch);
                }
            }

            std::sort(uniquePitches.begin(), uniquePitches.end());

            if (uniquePitches.empty()) {
                return false;
            }

            bassPitch = uniquePitches.front();
            if (uniquePitches.size() == 1) {
                treblePitches = { bassPitch + 12 };
                return true;
            }

            treblePitches.assign(uniquePitches.begin() + 1, uniquePitches.end());
            return true;
        };

        if (useCollectedTones && !region.tones.empty()) {
            assignCollectedTonesVoicing();
        } else {
            // Canonical close-position voicing from the analysis result.
            const ClosePositionVoicing voicing = closePositionVoicing(chord);
            bassPitch = voicing.bassPitch;
            treblePitches = voicing.treblePitches;

            // Sparse shell and monophonic regions can produce a useful chord
            // identity without a canonical close-position voicing. Reuse the
            // actual source tones instead of dropping the region entirely.
            if (bassPitch < 0 && !region.tones.empty()) {
                assignCollectedTonesVoicing();
            }
        }

        if (bassPitch < 0) {
            continue;
        }

        // ── Notes ────────────────────────────────────────────────────────
        // Bass: root only.
        addChordChainFromPitches(score, rStart, rEnd, bassTrack,
                                 { bassPitch }, localKeyFifths);

        // Treble: upper-structure chord tones.
        if (!treblePitches.empty()) {
            addChordChainFromPitches(score, rStart, rEnd, trebleTrack,
                                     treblePitches, localKeyFifths);
        }

        // Chord-staff notes are annotation-only — silence them so they don't
        // double the playback of the source staff.
        for (Segment* ps = score->tick2segment(rStart, true, SegmentType::ChordRest);
             ps && ps->tick() < rEnd;
             ps = ps->next1(SegmentType::ChordRest)) {
            for (track_idx_t tr : { trebleTrack, bassTrack }) {
                ChordRest* cr = ps->cr(tr);
                if (!cr || !cr->isChord()) {
                    continue;
                }
                for (Note* n : toChord(cr)->notes()) {
                    n->undoChangeProperty(Pid::PLAY, false);
                }
            }
        }

        // ── Harmony elements ─────────────────────────────────────────────
        Measure* regionMeasure = score->tick2measure(rStart);
        Segment* seg = regionMeasure ? regionMeasure->undoGetSegment(SegmentType::ChordRest, rStart) : nullptr;
        if (!seg) {
            continue;
        }

        // Chord symbol above treble.
        const bool writeChordSymbols = !prefs || prefs->chordStaffWriteChordSymbols();
        const ChordSymbolFormatter::Options fmtOpts{ scoreNoteSpelling(score) };
        const std::string symText = (writeChordSymbols && passesMinimumDisplayDuration)
            ? sanitizeChordTrackSymbolForHarmonyRenderer(
                ChordSymbolFormatter::formatSymbol(chord, localKeyFifths, fmtOpts))
            : "";
        if (!symText.empty()) {
            Harmony* h = Factory::createHarmony(seg);
            h->setTrack(trebleTrack);
            h->setParent(seg);
            h->setHarmonyType(HarmonyType::STANDARD);
            h->setHarmony(muse::String::fromStdString(symText));
            h->afterRead();
            score->undoAddElement(h);
        }

        // Chord function notation stays paired with the visible chord result;
        // confidence gating still applies only to key-dependent key annotations.
        const std::string fnKey = prefs ? prefs->chordStaffFunctionNotation() : "roman";
        if (fnKey != "none" && passesMinimumDisplayDuration) {
            const bool useNashville = (fnKey == "nashville");
            const std::string fnText = useNashville
                ? ChordSymbolFormatter::formatNashvilleNumber(chord, localKeyFifths)
                : ChordSymbolFormatter::formatRomanNumeral(chord);
            if (!fnText.empty()) {
                Harmony* h = Factory::createHarmony(seg);
                h->setTrack(bassTrack);
                h->setParent(seg);
                h->setHarmonyType(useNashville ? HarmonyType::NASHVILLE : HarmonyType::ROMAN);
                h->setHarmony(muse::String::fromStdString(fnText));
                h->afterRead();
                score->undoAddElement(h);
            }
        }

        // Non-diatonic chord marker (borrowed chord / secondary dominant).
        // Only annotate when we can identify the source key; purely chromatic
        // chords that fit no diatonic scale are left without a marker.
        const bool highlightNonDiatonic = !prefs || prefs->chordStaffHighlightNonDiatonic();
        if (highlightNonDiatonic
            && passesMinimumDisplayDuration
            && allowAssertiveKeyExposure
            && !chord.function.diatonicToKey) {
            // Borrowed chord source key: find the nearest key (by circle-of-
            // fifths distance) in which all of this chord's quality tones are
            // diatonic.  Check all supported modes across all 15 key signatures.
            using mu::composing::analysis::keyModeTonicName;
            using mu::composing::analysis::keyModeSuffix;
            using mu::composing::analysis::keyModeTonicOffset;
            using mu::composing::analysis::KEY_MODE_COUNT;
            using mu::composing::analysis::keyModeFromIndex;

            bool chordPcs[12] = {};
            for (int pc : mu::composing::analysis::chordTonePitchClasses(chord)) {
                chordPcs[pc % 12] = true;
            }

            int bestFifths = localKeyFifths;
            KeySigMode bestMode = localMode;
            int bestDist = std::numeric_limits<int>::max();

            for (int candidateFifths = -7; candidateFifths <= 7; ++candidateFifths) {
                if (candidateFifths == localKeyFifths) {
                    continue;
                }
                const int dist = std::abs(candidateFifths - localKeyFifths);
                if (dist >= bestDist) {
                    continue;
                }
                const int ionianPc = ((candidateFifths * 7) % 12 + 12) % 12;
                for (size_t mi = 0; mi < KEY_MODE_COUNT; ++mi) {
                    const KeySigMode candidateMode = keyModeFromIndex(mi);
                    const int tonicPc = (ionianPc + keyModeTonicOffset(candidateMode)) % 12;
                    const auto& candidateScale = keyModeScaleIntervals(candidateMode);
                    bool scalePcs[12] = {};
                    for (int iv : candidateScale) {
                        scalePcs[(tonicPc + iv) % 12] = true;
                    }
                    bool allIn = true;
                    for (int pc = 0; pc < 12; ++pc) {
                        if (chordPcs[pc] && !scalePcs[pc]) { allIn = false; break; }
                    }
                    if (!allIn) {
                        continue;
                    }
                    if (dist < bestDist
                        || (dist == bestDist && (mi == 0 || mi == 5))) {
                        bestDist = dist;
                        bestFifths = candidateFifths;
                        bestMode = keyModeFromIndex(mi);
                    }
                }
            }

            // Only write the marker when a source key was found.
            if (bestDist < std::numeric_limits<int>::max()) {
                // Star above second stave.
                StaffText* ndt = Factory::createStaffText(seg);
                ndt->setTrack(bassTrack);
                ndt->setParent(seg);
                ndt->setPlainText(muse::String(u"\u2605"));  // ★
                score->undoAddElement(ndt);

                // Source key label above second stave (no "from" prefix).
                std::string borrowLabel =
                    std::string(keyModeTonicName(bestFifths, bestMode))
                    + " " + keyModeSuffix(bestMode);
                StaffText* bt = Factory::createStaffText(seg);
                bt->setTrack(bassTrack);
                bt->setParent(seg);
                bt->setPlainText(muse::String::fromStdString(borrowLabel));
                score->undoAddElement(bt);
            }
        }

        anyWritten = true;
    }

    // ── Cadence markers ─────────────────────────────────────────────────────
    // Detect standard cadence patterns from consecutive region pairs and
    // annotate the resolution chord with a staff text label on the bass staff.
    //   Authentic  (PAC): V → I
    //   Plagal     (PC):  IV → I
    //   Deceptive  (DC):  V → vi
    //   Half       (HC):  → V  (last region, or followed by key change)
    const bool writeCadenceMarkers = !prefs || prefs->chordStaffWriteCadenceMarkers();
    if (writeCadenceMarkers)
    for (size_t i = 0; i + 1 < regions.size(); ++i) {
        if (!supportsAssertiveKeyExposure(regions[i].keyModeResult)
            || !supportsAssertiveKeyExposure(regions[i + 1].keyModeResult)) {
            continue;
        }

        const auto& a = regions[i].chordResult;
        const auto& b = regions[i + 1].chordResult;

        // Cadences require same key context and different chord roots.
        if (regions[i].keyModeResult.keySignatureFifths
            != regions[i + 1].keyModeResult.keySignatureFifths
            || regions[i].keyModeResult.mode
               != regions[i + 1].keyModeResult.mode) {
            continue;  // key change — not a cadence
        }
        if (a.identity.rootPc == b.identity.rootPc) {
            continue;  // same root (e.g. F#m → F#7) — not a cadence
        }

        const char* label = nullptr;

        // PAC: V → I (major dominant) or viio → I (leading-tone diminished).
        if (b.function.degree == 0
            && ((a.function.degree == 4 && a.identity.quality != ChordQuality::Minor)
                || (a.function.degree == 6 && a.identity.quality == ChordQuality::Diminished))) {
            label = "PAC";        // Authentic: V → I  or  viio → I
        } else if (a.function.degree == 3 && b.function.degree == 0) {
            label = "PC";         // Plagal: IV → I
        } else if (a.function.degree == 4 && b.function.degree == 5
                   && a.identity.quality != ChordQuality::Minor
                   && b.identity.quality == ChordQuality::Minor) {
            label = "DC";         // Deceptive: V → vi
        }

        if (label) {
            const Fraction bStart = Fraction::fromTicks(regions[i + 1].startTick);
            Segment* cSeg = score->tick2segment(bStart, true,
                                                 SegmentType::ChordRest);
            if (cSeg) {
                StaffText* ct = Factory::createStaffText(cSeg);
                ct->setTrack(bassTrack);
                ct->setParent(cSeg);
                ct->setPlainText(muse::String::fromStdString(label));
                score->undoAddElement(ct);
            }
        }
    }

    // Half cadence: last region is V (dominant arrival at end of range).
    if (writeCadenceMarkers
        && !regions.empty()
        && supportsAssertiveKeyExposure(regions.back().keyModeResult)
        && regions.back().chordResult.function.degree == 4) {
        const Fraction hStart = Fraction::fromTicks(regions.back().startTick);
        Segment* hSeg = score->tick2segment(hStart, true,
                                             SegmentType::ChordRest);
        if (hSeg) {
            StaffText* hc = Factory::createStaffText(hSeg);
            hc->setTrack(bassTrack);
            hc->setParent(hSeg);
            hc->setPlainText(muse::String(u"HC"));
            score->undoAddElement(hc);
        }
    }

    return anyWritten;
}

} // namespace mu::notation
