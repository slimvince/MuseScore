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

// ── Single-note bridge: harmonicAnnotation + analyzeNoteHarmonicContext ──────
//
// Implements the two single-note bridge functions declared in
// notationcomposingbridge.h.  Shared engraving helpers live in
// notationcomposingbridgehelpers.cpp; the bulk time-range scanner lives in
// notationharmonicrhythmbridge.cpp.

#include "notationcomposingbridge.h"
#include "notationanalysisinternal.h"
#include "notationcomposingbridgehelpers.h"

#include <algorithm>
#include <array>
#include <iterator>
#include <optional>
#include <set>
#include <string>
#include <vector>

#include "engraving/dom/factory.h"
#include "engraving/dom/harmony.h"
#include "engraving/dom/measure.h"
#include "engraving/dom/note.h"
#include "engraving/dom/rest.h"
#include "engraving/dom/score.h"
#include "engraving/dom/segment.h"
#include "engraving/dom/staff.h"
#include "engraving/dom/stafftext.h"
#include "engraving/types/constants.h"

#include "composing/analysis/chord/chordanalyzer.h"
#include "composing/analysis/key/keymodeanalyzer.h"
#include "composing/icomposinganalysisconfiguration.h"
#include "modularity/ioc.h"

using namespace mu::engraving;
using mu::notation::internal::isChordTrackStaff;
using mu::notation::internal::staffIsEligible;
using mu::notation::internal::SoundingNote;
using mu::notation::internal::collectSoundingAt;
using mu::notation::internal::buildTones;
using mu::notation::internal::resolveKeyAndMode;
using mu::notation::internal::findTemporalContext;
using mu::notation::internal::scoreNoteSpelling;
using mu::notation::internal::detectCadences;
using mu::notation::internal::detectPivotChords;

namespace {

static constexpr int kInitialRegionalLookBehindMeasures = 1;
static constexpr int kInitialRegionalLookAheadMeasures = 1;
static constexpr int kMaxRegionalExpansionSteps = 8;

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

void applySparseChordKeyContext(mu::composing::analysis::ChordAnalysisResult& result,
                                const std::vector<mu::composing::analysis::ChordAnalysisTone>& tones,
                                int keyFifths,
                                mu::composing::analysis::KeySigMode keyMode)
{
    using namespace mu::composing::analysis;

    const int ionianTonicPc = ionianTonicPcFromFifths(keyFifths);
    const int tonicPc = (ionianTonicPc + keyModeTonicOffset(keyMode)) % 12;
    const auto& scale = keyModeScaleIntervals(keyMode);

    result.function.keyTonicPc = tonicPc;
    result.function.keyMode = keyMode;
    result.function.degree = -1;
    for (size_t degree = 0; degree < scale.size(); ++degree) {
        if ((tonicPc + scale[degree]) % 12 == result.identity.rootPc) {
            result.function.degree = static_cast<int>(degree);
            break;
        }
    }

    bool diatonicToKey = (result.function.degree >= 0);
    if (diatonicToKey) {
        for (const auto& tone : tones) {
            const int pitchClass = tone.pitch % 12;
            bool inScale = false;
            for (int interval : scale) {
                if ((tonicPc + interval) % 12 == pitchClass) {
                    inScale = true;
                    break;
                }
            }
            if (!inScale) {
                diatonicToKey = false;
                break;
            }
        }
    }

    result.function.diatonicToKey = diatonicToKey;
}

std::optional<mu::composing::analysis::ChordAnalysisResult> inferSparseChordResult(
    const std::vector<mu::composing::analysis::ChordAnalysisTone>& tones,
    int keyFifths,
    mu::composing::analysis::KeySigMode keyMode)
{
    using namespace mu::composing::analysis;

    if (tones.empty()) {
        return std::nullopt;
    }

    const ChordAnalysisTone* bassTone = bassToneFromTones(tones);
    if (!bassTone) {
        bassTone = &tones.front();
        for (const auto& tone : tones) {
            if (tone.pitch < bassTone->pitch) {
                bassTone = &tone;
            }
        }
    }

    bool seenPitchClasses[12] = {};
    std::vector<int> pitchClasses;
    pitchClasses.reserve(tones.size());
    for (const auto& tone : tones) {
        const int pitchClass = tone.pitch % 12;
        if (!seenPitchClasses[pitchClass]) {
            seenPitchClasses[pitchClass] = true;
            pitchClasses.push_back(pitchClass);
        }
    }

    if (pitchClasses.empty()) {
        return std::nullopt;
    }

    ChordAnalysisResult inferred;
    inferred.identity.rootPc = bassTone->pitch % 12;
    inferred.identity.bassPc = bassTone->pitch % 12;
    inferred.identity.bassTpc = bassTone->tpc;
    inferred.identity.score = 0.0;

    if (pitchClasses.size() == 1) {
        inferred.identity.quality = ChordQuality::Unknown;
        applySparseChordKeyContext(inferred, tones, keyFifths, keyMode);
        return inferred;
    }

    const int bassPitchClass = bassTone->pitch % 12;
    for (int pitchClass : pitchClasses) {
        if (pitchClass == bassPitchClass) {
            continue;
        }

        const int intervalAboveBass = (pitchClass - bassPitchClass + 12) % 12;
        if (intervalAboveBass == 3 || intervalAboveBass == 4) {
            inferred.identity.quality = (intervalAboveBass == 3) ? ChordQuality::Minor : ChordQuality::Major;
            applySparseChordKeyContext(inferred, tones, keyFifths, keyMode);
            return inferred;
        }
    }

    for (int pitchClass : pitchClasses) {
        if (pitchClass == bassPitchClass) {
            continue;
        }

        if ((pitchClass - bassPitchClass + 12) % 12 != 7) {
            continue;
        }

        inferred.identity.quality = ChordQuality::Unknown;
        applySparseChordKeyContext(inferred, tones, keyFifths, keyMode);
        return inferred;
    }

    return std::nullopt;
}

mu::engraving::staff_idx_t resolveAnalysisReferenceStaff(const mu::engraving::Score* sc,
                                                         const mu::engraving::Fraction& tick,
                                                         size_t preferredStaffIdx,
                                                         const std::set<size_t>& excludeStaves)
{
    using namespace mu::engraving;

    staff_idx_t refStaff = static_cast<staff_idx_t>(preferredStaffIdx);
    if (preferredStaffIdx >= sc->nstaves()
        || excludeStaves.count(preferredStaffIdx)
        || !staffIsEligible(sc, preferredStaffIdx, tick)) {
        refStaff = 0;
        for (size_t si = 0; si < sc->nstaves(); ++si) {
            if (!excludeStaves.count(si) && staffIsEligible(sc, si, tick)) {
                refStaff = static_cast<staff_idx_t>(si);
                break;
            }
        }
    }

    return refStaff;
}

mu::notation::NoteHarmonicContext analyzeHarmonicContextLocallyAtTick(
    const mu::engraving::Score* sc,
    const mu::engraving::Fraction& tick,
    const mu::engraving::Segment* seg,
    mu::engraving::staff_idx_t refStaff,
    const std::set<size_t>& excludeStaves)
{
    using namespace mu::engraving;

    mu::notation::NoteHarmonicContext context;

    std::vector<SoundingNote> sounding;
    collectSoundingAt(sc, seg, excludeStaves, sounding);
    if (sounding.empty()) {
        return context;
    }

    resolveKeyAndMode(sc, tick, refStaff, excludeStaves,
                      context.keyFifths, context.keyMode, context.keyConfidence);

    int currentBassPc = -1;
    int lowestPitch = std::numeric_limits<int>::max();
    for (const SoundingNote& soundingNote : sounding) {
        lowestPitch = std::min(lowestPitch, soundingNote.ppitch);
    }
    if (lowestPitch != std::numeric_limits<int>::max()) {
        currentBassPc = lowestPitch % 12;
    }

    mu::composing::analysis::ChordTemporalContext temporalCtx
        = findTemporalContext(sc, seg, excludeStaves, context.keyFifths, context.keyMode, currentBassPc);

    const auto analysisTones = buildTones(sounding);
    context.chordResults = mu::composing::analysis::ChordAnalyzerFactory::create()->analyzeChord(analysisTones,
                                                                                                  context.keyFifths,
                                                                                                  context.keyMode,
                                                                                                  &temporalCtx);
    if (context.chordResults.empty()) {
        if (auto sparseResult = inferSparseChordResult(analysisTones,
                                                       context.keyFifths,
                                                       context.keyMode)) {
            context.chordResults.push_back(*sparseResult);
        }
    }
    for (auto& result : context.chordResults) {
        mu::notation::internal::refineSparseChordQualityFromKeyContext(result,
                                                                       analysisTones,
                                                                       context.keyFifths,
                                                                       context.keyMode);
    }
    return context;
}

struct RegionalContextSnapshot {
    mu::notation::NoteHarmonicContext context;
    std::string symbol;
    std::string roman;
    std::string nashville;
    bool valid = false;
};

RegionalContextSnapshot analyzeNoteHarmonicContextRegionallyInWindow(
    const mu::engraving::Score* sc,
    const mu::engraving::Fraction& tick,
    const mu::engraving::Segment* seg,
    const std::set<size_t>& excludeStaves,
    const mu::engraving::Fraction& windowStartTick,
    const mu::engraving::Fraction& windowEndTick)
{
    using namespace mu::engraving;

    RegionalContextSnapshot snapshot;

    const auto regions = mu::notation::internal::prepareUserFacingHarmonicRegions(sc,
                                                                                  windowStartTick,
                                                                                  windowEndTick,
                                                                                  excludeStaves);
    if (regions.empty()) {
        return snapshot;
    }

    const int noteTick = tick.ticks();
    auto it = std::find_if(regions.begin(), regions.end(), [noteTick](const auto& region) {
        return region.startTick <= noteTick && noteTick < region.endTick;
    });
    if (it == regions.end()) {
        const auto nextRegion = std::find_if(regions.begin(), regions.end(), [noteTick](const auto& region) {
            return noteTick < region.startTick;
        });

        if (nextRegion == regions.begin()) {
            it = nextRegion;
        } else if (nextRegion == regions.end()) {
            it = std::prev(regions.end());
        } else {
            // When the tick sits exactly at the end of the preceding region it
            // belongs to the next harmonic period — prefer the forward region.
            auto prev = std::prev(nextRegion);
            it = (prev->endTick == noteTick) ? nextRegion : prev;
        }
    }
    if (it == regions.end()) {
        return snapshot;
    }

    snapshot.context.keyFifths = it->keyModeResult.keySignatureFifths;
    snapshot.context.keyMode = it->keyModeResult.mode;
    snapshot.context.keyConfidence = it->keyModeResult.normalizedConfidence;

    auto displayTones = mu::notation::internal::collectRegionTones(sc,
                                                                   it->startTick,
                                                                   it->endTick,
                                                                   excludeStaves);
    const int currentBassPc = it->chordResult.identity.bassPc;
    const mu::composing::analysis::ChordTemporalContext* temporalCtxPtr = nullptr;
    mu::composing::analysis::ChordTemporalContext temporalCtx;
    if (seg) {
        temporalCtx = findTemporalContext(sc, seg, excludeStaves,
                                          snapshot.context.keyFifths, snapshot.context.keyMode, currentBassPc);
        temporalCtxPtr = &temporalCtx;
    }

    const int ionianPc = mu::composing::analysis::ionianTonicPcFromFifths(snapshot.context.keyFifths);
    const int tonicPc = (ionianPc + mu::composing::analysis::keyModeTonicOffset(snapshot.context.keyMode)) % 12;
    auto applyRegionalKeyContext = [tonicPc, &snapshot](mu::composing::analysis::ChordAnalysisResult& result) {
        result.function.keyTonicPc = tonicPc;
        result.function.keyMode = snapshot.context.keyMode;
    };

    mu::composing::analysis::ChordAnalysisResult preferredResult = it->chordResult;
    applyRegionalKeyContext(preferredResult);

    if (!displayTones.empty()) {
        snapshot.context.chordResults = mu::composing::analysis::ChordAnalyzerFactory::create()->analyzeChord(displayTones,
                                                                                                               snapshot.context.keyFifths,
                                                                                                               snapshot.context.keyMode,
                                                                                                               temporalCtxPtr);
    }
    for (auto& result : snapshot.context.chordResults) {
        applyRegionalKeyContext(result);
    }

    if (snapshot.context.chordResults.empty()) {
        snapshot.context.chordResults.push_back(preferredResult);
    } else {
        auto sameDisplayResult = [keyFifths = snapshot.context.keyFifths](const auto& lhs, const auto& rhs) {
            return mu::composing::analysis::ChordSymbolFormatter::formatSymbol(lhs, keyFifths)
                   == mu::composing::analysis::ChordSymbolFormatter::formatSymbol(rhs, keyFifths)
                   && mu::composing::analysis::ChordSymbolFormatter::formatRomanNumeral(lhs)
                   == mu::composing::analysis::ChordSymbolFormatter::formatRomanNumeral(rhs)
                   && mu::composing::analysis::ChordSymbolFormatter::formatNashvilleNumber(lhs, keyFifths)
                   == mu::composing::analysis::ChordSymbolFormatter::formatNashvilleNumber(rhs, keyFifths);
        };
        if (!sameDisplayResult(snapshot.context.chordResults.front(), preferredResult)) {
            // Keep the harmonic-region winner first so note context mirrors chord-track output.
            snapshot.context.chordResults.insert(snapshot.context.chordResults.begin(), preferredResult);
        }
    }

    snapshot.symbol = mu::composing::analysis::ChordSymbolFormatter::formatSymbol(snapshot.context.chordResults.front(),
                                                                                  snapshot.context.keyFifths);
    snapshot.roman = mu::composing::analysis::ChordSymbolFormatter::formatRomanNumeral(snapshot.context.chordResults.front());
    snapshot.nashville = mu::composing::analysis::ChordSymbolFormatter::formatNashvilleNumber(snapshot.context.chordResults.front(),
                                                                                              snapshot.context.keyFifths);
    snapshot.valid = true;
    return snapshot;
}

bool regionalSnapshotsMatch(const RegionalContextSnapshot& lhs,
                            const RegionalContextSnapshot& rhs)
{
    if (!lhs.valid || !rhs.valid) {
        return false;
    }

    return lhs.context.keyFifths == rhs.context.keyFifths
           && lhs.context.keyMode == rhs.context.keyMode
           && lhs.symbol == rhs.symbol
           && lhs.roman == rhs.roman
           && lhs.nashville == rhs.nashville;
}

mu::notation::NoteHarmonicContext analyzeHarmonicContextRegionallyAtTick(
    const mu::engraving::Score* sc,
    const mu::engraving::Fraction& tick,
    const mu::engraving::Segment* seg,
    const std::set<size_t>& excludeStaves)
{
    using namespace mu::engraving;

    const Measure* currentMeasure = sc->tick2measure(tick);
    if (!currentMeasure) {
        return {};
    }

    const Measure* windowStartMeasure = currentMeasure;
    for (int i = 0; i < kInitialRegionalLookBehindMeasures; ++i) {
        if (const Measure* previousMeasure = windowStartMeasure->prevMeasure()) {
            windowStartMeasure = previousMeasure;
        }
    }

    const Measure* windowEndMeasure = currentMeasure;
    for (int i = 0; i < kInitialRegionalLookAheadMeasures; ++i) {
        if (const Measure* nextMeasure = windowEndMeasure->nextMeasure()) {
            windowEndMeasure = nextMeasure;
        }
    }

    RegionalContextSnapshot previousSnapshot;
    RegionalContextSnapshot currentSnapshot;

    for (int expansionStep = 0; expansionStep <= kMaxRegionalExpansionSteps; ++expansionStep) {
        currentSnapshot = analyzeNoteHarmonicContextRegionallyInWindow(sc,
                                                                       tick,
                                                                       seg,
                                                                       excludeStaves,
                                                                       windowStartMeasure->tick(),
                                                                       windowEndMeasure->endTick());
        if (currentSnapshot.valid && regionalSnapshotsMatch(previousSnapshot, currentSnapshot)) {
            return currentSnapshot.context;
        }
        previousSnapshot = currentSnapshot;

        const Measure* nextStartMeasure = windowStartMeasure->prevMeasure();
        const Measure* nextEndMeasure = windowEndMeasure->nextMeasure();
        if (!nextStartMeasure && !nextEndMeasure) {
            break;
        }
        if (nextStartMeasure) {
            windowStartMeasure = nextStartMeasure;
        }
        if (nextEndMeasure) {
            windowEndMeasure = nextEndMeasure;
        }
    }

    return previousSnapshot.context;
}

}

// ── harmonicAnnotation ──────────────────────────────────────────────────────

namespace mu::notation {

NoteHarmonicContext analyzeHarmonicContextAtTick(const mu::engraving::Score* score,
                                                 const mu::engraving::Fraction& tick,
                                                 size_t preferredStaffIdx,
                                                 const std::set<size_t>& excludeStaves)
{
    using namespace mu::engraving;

    if (!score) {
        return {};
    }

    const Segment* seg = score->tick2segment(tick, true, SegmentType::ChordRest);
    if (!seg) {
        return {};
    }

    const staff_idx_t refStaff = resolveAnalysisReferenceStaff(score, tick, preferredStaffIdx, excludeStaves);

    NoteHarmonicContext regional = analyzeHarmonicContextRegionallyAtTick(score, tick, seg, excludeStaves);
    if (!regional.chordResults.empty()) {
        return regional;
    }

    return analyzeHarmonicContextLocallyAtTick(score, tick, seg, refStaff, excludeStaves);
}

std::string harmonicAnnotation(const Note* note)
{
    static muse::GlobalInject<mu::composing::IComposingAnalysisConfiguration> config;
    const auto* prefs = config.get().get();
    if (!prefs) {
        return "";
    }

    const NoteHarmonicContext context = analyzeNoteHarmonicContextDetails(note);
    const int keyFifths = context.keyFifths;
    const auto keyMode = context.keyMode;
    const auto& chordResults = context.chordResults;

    // Key/mode string (optional)
    std::string keyStr;
    if (prefs->showKeyModeInStatusBar()) {
        using mu::composing::analysis::keyModeTonicName;
        using mu::composing::analysis::keyModeSuffix;
        keyStr = std::string(keyModeTonicName(keyFifths, keyMode)) + " " + keyModeSuffix(keyMode);
    }

    // If no chord-level analysis is requested, show only key/mode (no "in" prefix)
    if (!prefs->analyzeForChordSymbols() && !prefs->analyzeForChordFunction()) {
        return keyStr.empty() ? "" : "key: " + keyStr;
    }

    if (chordResults.empty()) {
        return keyStr.empty() ? "" : "key: " + keyStr;
    }

    // Sort alternatives by descending normalizedConfidence, keeping position 0 (region winner)
    // fixed so the top-level annotation is always the region-level result.
    auto sortedResults = chordResults;
    if (sortedResults.size() > 1) {
        std::sort(sortedResults.begin() + 1, sortedResults.end(),
                  [](const mu::composing::analysis::ChordAnalysisResult& a,
                     const mu::composing::analysis::ChordAnalysisResult& b) {
                      return a.identity.normalizedConfidence > b.identity.normalizedConfidence;
                  });
    }

    // Determine which display formats are active
    const bool wantSym = prefs->analyzeForChordSymbols() && prefs->showChordSymbolsInStatusBar();
    // Keep function labels paired with the shown chord analysis even when the key guess is tentative.
    const bool wantRoman = prefs->analyzeForChordFunction() && prefs->showRomanNumeralsInStatusBar();
    const bool wantNashville = prefs->analyzeForChordFunction() && prefs->showNashvilleNumbersInStatusBar();

    int shown = 0;
    const int maxShown = prefs->analysisAlternatives();
    std::string candidates;
    std::set<std::string> seenKeys;

    for (const auto& result : sortedResults) {
        if (shown >= maxShown) {
            break;
        }

        std::string sym, roman, nashville;
        if (wantSym) {
            sym = mu::composing::analysis::ChordSymbolFormatter::formatSymbol(result, keyFifths);
        }
        if (wantRoman) {
            roman = mu::composing::analysis::ChordSymbolFormatter::formatRomanNumeral(result);
        }
        if (wantNashville) {
            nashville = mu::composing::analysis::ChordSymbolFormatter::formatNashvilleNumber(result, keyFifths);
        }

        if (sym.empty() && roman.empty() && nashville.empty()) {
            continue;
        }
        std::string key = sym + "|" + roman + "|" + nashville;
        if (!seenKeys.insert(key).second) {
            continue;
        }

        std::string entry;
        for (const std::string& part : { sym, roman, nashville }) {
            if (part.empty()) {
                continue;
            }
            if (!entry.empty()) {
                entry += " / ";
            }
            entry += part;
        }

        if (!entry.empty()) {
            char scoreBuf[16];
            std::snprintf(scoreBuf, sizeof(scoreBuf), " (%.2f)", result.identity.score);
            entry += scoreBuf;

            if (!candidates.empty()) {
                candidates += " | ";
            }
            candidates += entry;
            ++shown;
        }
    }

    if (candidates.empty()) {
        return keyStr.empty() ? "" : "key: " + keyStr;
    }

    const std::string headed = "Chord: " + candidates;
    if (!keyStr.empty()) {
        return headed + " in key: " + keyStr;
    }
    return headed;
}

} // namespace mu::notation

// ── analyzeNoteHarmonicContext ────────────────────────────────────────────────

namespace mu::notation {

NoteHarmonicContext analyzeNoteHarmonicContextDetails(const mu::engraving::Note* note)
{
    using namespace mu::engraving;

    NoteHarmonicContext emptyContext;

    if (!note) {
        return emptyContext;
    }

    const Score* sc = note->score();
    const Fraction tick = note->tick();

    std::set<size_t> excludeStaves;
    for (size_t si = 0; si < sc->nstaves(); ++si) {
        if (isChordTrackStaff(sc, si)) {
            excludeStaves.insert(si);
        }
    }

    return analyzeHarmonicContextAtTick(sc, tick, static_cast<size_t>(note->staffIdx()), excludeStaves);
}

NoteHarmonicContext analyzeRestHarmonicContextDetails(const mu::engraving::Rest* rest)
{
    if (!rest) {
        return {};
    }

    const Score* sc = rest->score();
    if (!sc) {
        return {};
    }

    std::set<size_t> excludeStaves;
    for (size_t si = 0; si < sc->nstaves(); ++si) {
        if (isChordTrackStaff(sc, si)) {
            excludeStaves.insert(si);
        }
    }

    return analyzeHarmonicContextAtTick(sc, rest->tick(), static_cast<size_t>(rest->staffIdx()), excludeStaves);
}

std::vector<mu::composing::analysis::ChordAnalysisResult>
analyzeNoteHarmonicContext(const mu::engraving::Note* note,
                           int& outKeyFifths,
                           mu::composing::analysis::KeySigMode& outKeyMode)
{
    const NoteHarmonicContext context = analyzeNoteHarmonicContextDetails(note);
    outKeyFifths = context.keyFifths;
    outKeyMode = context.keyMode;
    return context.chordResults;
}

} // namespace mu::notation

// ── addHarmonicAnnotationsToSelection ────────────────────────────────────────

namespace mu::notation {

void addHarmonicAnnotationsToSelection(mu::engraving::Score* score,
                                       bool writeChordSymbols,
                                       bool writeRomanNumerals,
                                       bool writeNashvilleNumbers)
{
    using namespace mu::engraving;

    if (!score) {
        return;
    }

    const Selection& sel = score->selection();
    if (!sel.isRange()) {
        return;
    }

    if (!writeChordSymbols && !writeRomanNumerals && !writeNashvilleNumbers) {
        return;
    }

    const Fraction startTick = sel.tickStart();
    const Fraction endTick   = sel.tickEnd();
    const staff_idx_t staffFirst = sel.staffStart();
    const staff_idx_t staffLast  = sel.staffEnd(); // exclusive

    // Build analysis exclude set: chord track staves contribute symbols, not notes.
    std::set<size_t> excludeStaves;
    for (size_t si = 0; si < score->nstaves(); ++si) {
        if (isChordTrackStaff(score, si)) {
            excludeStaves.insert(si);
        }
    }

    // Chord-track priority rule: if any selected staff is a chord track staff,
    // write only to those; otherwise write to all selected staves.
    bool hasChordTrackInSelection = false;
    for (staff_idx_t si = staffFirst; si < staffLast; ++si) {
        if (isChordTrackStaff(score, si)) {
            hasChordTrackInSelection = true;
            break;
        }
    }

    std::vector<staff_idx_t> writeStaves;
    for (staff_idx_t si = staffFirst; si < staffLast; ++si) {
        if (!hasChordTrackInSelection || isChordTrackStaff(score, si)) {
            writeStaves.push_back(si);
        }
    }

    if (writeStaves.empty()) {
        return;
    }

    // Minimum duration preference (beats) for filtering short regions.
    static muse::GlobalInject<mu::composing::IComposingAnalysisConfiguration> config;
    const auto* prefs = config.get().get();
    const double minimumDisplayDurationBeats = prefs ? prefs->minimumDisplayDurationBeats() : 0.5;

    // Run harmonic analysis over an extended tick range when Roman numerals
    // are requested.  The lookahead regions are read-only: used for cadence
    // and pivot detection but never annotated.
    //
    //   selectionEndTick: the first tick that is outside the user's selection.
    //   lookaheadEndTick: extends the analysis to include up to
    //       kMaxPivotLookaheadRegions extra regions for key confirmation.
    const Fraction selectionEndTick = endTick;
    const Fraction lookaheadEndTick = writeRomanNumerals
        ? Fraction::fromTicks(endTick.ticks()
            + mu::notation::internal::kMaxPivotLookaheadRegions
              * 4 * Constants::DIVISION)  // ~8 measures of lookahead
        : endTick;

    // forceClassicalPath=true: prevent chord symbols previously written by this
    // annotator from triggering the Jazz boundary-detection path in a subsequent
    // annotation call (order-of-annotation violation fix; see §analyzeHarmonicRhythm).
    const auto allRegions = mu::notation::internal::prepareUserFacingHarmonicRegions(
        score, startTick, lookaheadEndTick, excludeStaves, /*forceClassicalPath=*/true);

    if (allRegions.empty()) {
        return;
    }

    // Split into in-selection vs. lookahead.
    const size_t selectionCount = static_cast<size_t>(
        std::count_if(allRegions.begin(), allRegions.end(),
            [&selectionEndTick](const mu::composing::analysis::HarmonicRegion& r) {
                return Fraction::fromTicks(r.startTick) < selectionEndTick;
            }));

    // The main annotation loop operates only on in-selection regions.
    const auto regions = std::vector<mu::composing::analysis::HarmonicRegion>(
        allRegions.begin(),
        allRegions.begin() + static_cast<std::ptrdiff_t>(selectionCount));

    // Create a fresh analyzer for annotation writes.  The analyzeHarmonicRhythm
    // pass carries sequential ChordTemporalContext (previousRootPc, etc.) which
    // adds rootContinuityBonus across regions.  When that bonus tips a lower-
    // scoring candidate to the top (e.g. a region-level F over Cm7/F because
    // the preceding region was also F), the annotation diverges from what the
    // display path would show.
    //
    // The display path (analyzeNoteHarmonicContextRegionallyInWindow) fixes this
    // by calling analyzeChord() fresh with a segment-derived ChordTemporalContext
    // via findTemporalContext() — which populates bassIsStepwiseFromPrevious and
    // bassIsStepwiseToNext from the actual score context, enabling the
    // stepwiseBassInversionBonus for inverted slash chords (e.g. Cm7/F over F).
    // We replicate that approach here so annotation and display stay in sync.
    const auto chordAnalyzerAnnotation = mu::composing::analysis::ChordAnalyzerFactory::create();

    score->startCmd(TranslatableString("undoableAction", "Add harmonic annotations to selection"));

    for (const auto& region : regions) {
        // Minimum duration filter.
        const double regionDurationBeats = static_cast<double>(region.endTick - region.startTick)
                                           / static_cast<double>(Constants::DIVISION);
        if (regionDurationBeats < minimumDisplayDurationBeats) {
            continue;
        }

        const Fraction rStart = Fraction::fromTicks(region.startTick);
        Segment* seg = score->tick2segment(rStart, true, SegmentType::ChordRest);
        if (!seg || seg->tick() >= Fraction::fromTicks(region.endTick)) {
            continue;
        }

        const int keyFifths = region.keyModeResult.keySignatureFifths;
        const auto keyMode   = region.keyModeResult.mode;

        // Fresh chord analysis using a display-style temporal context (matching
        // what analyzeNoteHarmonicContextRegionallyInWindow does), not the
        // cumulative sequential context carried by analyzeHarmonicRhythm.
        // Fall back to region.chordResult when tones are absent (carried gaps).
        mu::composing::analysis::ChordAnalysisResult annotationResult = region.chordResult;
        if (!region.tones.empty()) {
            const int currentBassPc = region.chordResult.identity.bassPc;
            const auto displayCtx = findTemporalContext(
                score, seg, excludeStaves, keyFifths, keyMode, currentBassPc);
            const auto fresh = chordAnalyzerAnnotation->analyzeChord(
                region.tones, keyFifths, keyMode, &displayCtx);
            if (!fresh.empty()) {
                annotationResult.identity = fresh.front().identity;
                // Recompute tonal-function fields for the fresh root so Roman
                // numerals and Nashville numbers remain consistent.
                const int ionianPc = mu::composing::analysis::ionianTonicPcFromFifths(keyFifths);
                const int tonicPc  = (ionianPc
                    + mu::composing::analysis::keyModeTonicOffset(keyMode)) % 12;
                annotationResult.function.keyTonicPc   = tonicPc;
                annotationResult.function.keyMode      = keyMode;
                annotationResult.function.degree       = -1;
                const auto& scale = keyModeScaleIntervals(keyMode);
                for (size_t i = 0; i < scale.size(); ++i) {
                    if ((tonicPc + scale[i]) % 12
                            == annotationResult.identity.rootPc) {
                        annotationResult.function.degree = static_cast<int>(i);
                        break;
                    }
                }
                annotationResult.function.diatonicToKey = (annotationResult.function.degree >= 0);
            }
        }

        const mu::composing::analysis::ChordSymbolFormatter::Options fmtOpts{ scoreNoteSpelling(score) };
        const std::string symText = writeChordSymbols
            ? mu::composing::analysis::ChordSymbolFormatter::formatSymbol(annotationResult, keyFifths, fmtOpts)
            : "";
        std::string romanText;
        if (writeRomanNumerals) {
            romanText = mu::composing::analysis::ChordSymbolFormatter::formatRomanNumeral(annotationResult);
            if (romanText.empty()
                    && annotationResult.identity.quality == mu::composing::analysis::ChordQuality::Unknown
                    && annotationResult.function.degree >= 0
                    && annotationResult.function.degree <= 6) {
                auto refinedForRoman = annotationResult;
                mu::notation::internal::forceChordTrackQualityFromKeyContext(refinedForRoman, keyMode);
                if (refinedForRoman.identity.quality != mu::composing::analysis::ChordQuality::Unknown) {
                    romanText = mu::composing::analysis::ChordSymbolFormatter::formatRomanNumeral(refinedForRoman);
                }
            }
        }
        const std::string nashvilleText = writeNashvilleNumbers
            ? mu::composing::analysis::ChordSymbolFormatter::formatNashvilleNumber(annotationResult, keyFifths)
            : "";

        for (staff_idx_t si : writeStaves) {
            const track_idx_t track = si * VOICES;

            if (!symText.empty()) {
                Harmony* h = Factory::createHarmony(seg);
                h->setTrack(track);
                h->setParent(seg);
                h->setHarmonyType(HarmonyType::STANDARD);
                h->setHarmony(muse::String::fromStdString(symText));
                score->undoAddElement(h);
            }

            if (!romanText.empty()) {
                Harmony* h = Factory::createHarmony(seg);
                h->setTrack(track);
                h->setParent(seg);
                h->setHarmonyType(HarmonyType::ROMAN);
                h->setHarmony(muse::String::fromStdString(romanText));
                score->undoAddElement(h);
            }

            if (!nashvilleText.empty()) {
                Harmony* h = Factory::createHarmony(seg);
                h->setTrack(track);
                h->setParent(seg);
                h->setHarmonyType(HarmonyType::NASHVILLE);
                h->setHarmony(muse::String::fromStdString(nashvilleText));
                score->undoAddElement(h);
            }
        }

        // ── Pedal bass annotation ─────────────────────────────────────────────
        // When the chord analyzer identified a structural pedal point, write a
        // StaffText "X ped." (e.g. "G ped.", "Eb ped.") on the first write staff,
        // in the Roman numeral layer (alongside cadence markers and pivot labels).
        // Only written when Roman numeral mode is active.
        if (writeRomanNumerals
                && !writeStaves.empty()
                && annotationResult.identity.isPedalPoint
                && annotationResult.identity.pedalBassPc >= 0) {
            // Build a bare root-name result for the pedal bass PC.
            mu::composing::analysis::ChordAnalysisResult pedalRoot = annotationResult;
            pedalRoot.identity.rootPc  = annotationResult.identity.pedalBassPc;
            pedalRoot.identity.bassPc  = annotationResult.identity.pedalBassPc;
            pedalRoot.identity.quality = mu::composing::analysis::ChordQuality::Major;
            pedalRoot.identity.extensions = 0;
            const std::string baseName = mu::composing::analysis::ChordSymbolFormatter::formatSymbol(
                pedalRoot, keyFifths, fmtOpts);
            if (!baseName.empty()) {
                const std::string pedalText = baseName + " ped.";
                const track_idx_t pedTrack = writeStaves.front() * VOICES;
                StaffText* pt = Factory::createStaffText(seg);
                pt->setTrack(pedTrack);
                pt->setParent(seg);
                pt->setPlainText(muse::String::fromStdString(pedalText));
                score->undoAddElement(pt);
            }
        }
    }

    // ── Cadence markers and pivot labels (Roman numeral mode only) ──────────
    //
    // Cadence markers ("PAC", "HC", etc.) and pivot labels ("vi → ii") are
    // analytically meaningful annotations associated with the Roman numeral
    // layer.  They are suppressed in chord-symbol-only and Nashville modes.
    //
    // Both use the full allRegions vector (selection + lookahead) for
    // detection; writing is restricted to in-selection ticks only.
    if (writeRomanNumerals && !writeStaves.empty()) {
        const track_idx_t annotateTrack = writeStaves.front() * VOICES;

        const auto cadences = detectCadences(allRegions, selectionCount);
        for (const auto& marker : cadences) {
            const Fraction mTick = Fraction::fromTicks(marker.tick);
            Segment* mSeg = score->tick2segment(mTick, true, SegmentType::ChordRest);
            if (!mSeg) {
                continue;
            }
            StaffText* st = Factory::createStaffText(mSeg);
            st->setTrack(annotateTrack);
            st->setParent(mSeg);
            st->setPlainText(muse::String::fromStdString(marker.label));
            score->undoAddElement(st);
        }

        const auto pivots = detectPivotChords(allRegions, selectionCount);
        for (const auto& pv : pivots) {
            const Fraction pTick = Fraction::fromTicks(pv.tick);
            Segment* pSeg = score->tick2segment(pTick, true, SegmentType::ChordRest);
            if (!pSeg) {
                continue;
            }
            StaffText* pt = Factory::createStaffText(pSeg);
            pt->setTrack(annotateTrack);
            pt->setParent(pSeg);
            pt->setPlainText(muse::String::fromStdString(pv.label));
            score->undoAddElement(pt);
        }
    }

    score->endCmd();
}

} // namespace mu::notation
