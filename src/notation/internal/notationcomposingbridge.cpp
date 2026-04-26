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
using mu::notation::internal::chordTrackExcludeStaves;
using mu::notation::internal::SoundingNote;
using mu::notation::internal::collectSoundingAt;
using mu::notation::internal::buildTones;
using mu::notation::internal::resolveKeyAndMode;
using mu::notation::internal::findTemporalContext;
using mu::notation::internal::scoreNoteSpelling;
using mu::notation::internal::detectCadences;
using mu::notation::internal::detectPivotChords;

namespace {

using mu::composing::analysis::keyModeScaleIntervals;
using mu::notation::internal::diatonicDegreeForRootPc;

static constexpr int kInitialRegionalLookBehindMeasures = 1;
static constexpr int kInitialRegionalLookAheadMeasures = 1;
static constexpr int kMaxRegionalExpansionSteps = 8;

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
    result.function.degree = diatonicDegreeForRootPc(result.identity.rootPc, keyFifths, keyMode);

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
    const mu::engraving::Segment* /*seg — unused after Phase 3c*/,
    const std::set<size_t>& excludeStaves,
    const mu::engraving::Fraction& windowStartTick,
    const mu::engraving::Fraction& windowEndTick)
{
    using namespace mu::engraving;

    RegionalContextSnapshot snapshot;

    // Phase 3c: consume AnalyzedSection.  The cruft path (display-context
    // collectRegionTones + findTemporalContext + second analyzeChord +
    // tie-break prepend) is gone — see docs/divergence_d_recon.md for the
    // archaeology.  chordResults[0] now comes from the per-region winner,
    // chordResults[1..] from the canonical alternatives the per-region
    // analyzeChord produced (and previously discarded).
    const auto section = mu::notation::internal::analyzeSection(sc,
                                                                windowStartTick,
                                                                windowEndTick,
                                                                excludeStaves);
    if (section.regions.empty()) {
        return snapshot;
    }

    const int noteTick = tick.ticks();
    const auto& regions = section.regions;
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
    snapshot.context.temporalExtensions = it->temporalExtensions;

    // Populate enclosingKeyArea from the matched region's keyAreaId.
    // P4 fallback leaves this nullopt — graceful degradation per recon Q3.
    const int kaId = it->keyAreaId;
    if (kaId >= 0 && kaId < static_cast<int>(section.keyAreas.size())) {
        snapshot.context.enclosingKeyArea = section.keyAreas[kaId];
    }

    const int ionianPc = mu::composing::analysis::ionianTonicPcFromFifths(snapshot.context.keyFifths);
    const int tonicPc = (ionianPc + mu::composing::analysis::keyModeTonicOffset(snapshot.context.keyMode)) % 12;
    auto applyRegionalKeyContext = [tonicPc, &snapshot](mu::composing::analysis::ChordAnalysisResult& result) {
        result.function.keyTonicPc = tonicPc;
        result.function.keyMode = snapshot.context.keyMode;
    };

    snapshot.context.chordResults.reserve(1 + it->alternatives.size());
    snapshot.context.chordResults.push_back(it->chordResult);
    for (const auto& alt : it->alternatives) {
        snapshot.context.chordResults.push_back(alt);
    }
    for (auto& result : snapshot.context.chordResults) {
        applyRegionalKeyContext(result);
    }

    const mu::composing::analysis::ChordSymbolFormatter::Options fmtOpts{ scoreNoteSpelling(sc) };
    snapshot.symbol = mu::composing::analysis::ChordSymbolFormatter::formatSymbol(snapshot.context.chordResults.front(),
                                                                                  snapshot.context.keyFifths, fmtOpts);
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

// ── Tick-local (P4) path ─────────────────────────────────────────────────────

namespace mu::notation {

NoteHarmonicContext analyzeHarmonicContextLocallyAtTick(
    const mu::engraving::Score* sc,
    const mu::engraving::Fraction& tick,
    const mu::engraving::Segment* seg,
    size_t refStaff,
    const std::set<size_t>& excludeStaves)
{
    using namespace mu::engraving;

    NoteHarmonicContext context;

    std::vector<SoundingNote> sounding;
    collectSoundingAt(sc, seg, excludeStaves, sounding);
    if (sounding.empty()) {
        return context;
    }

    resolveKeyAndMode(sc, tick, static_cast<staff_idx_t>(refStaff), excludeStaves,
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

} // namespace mu::notation

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
        regional.wasRegional = true;
        return regional;
    }

    NoteHarmonicContext local = analyzeHarmonicContextLocallyAtTick(score, tick, seg, refStaff, excludeStaves);
    local.wasRegional = false;
    return local;
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

    // chordResults is sorted by analyzeChord's internal score descending;
    // [0] is the top-ranked candidate.  Trust the analyzer's ranking.
    // (Phase 3c-impl deleted the legacy prepend pattern; see docs/divergence_d_recon.md.)

    // Determine which display formats are active
    const bool wantSym = prefs->analyzeForChordSymbols() && prefs->showChordSymbolsInStatusBar();
    // Keep function labels paired with the shown chord analysis even when the key guess is tentative.
    const bool wantRoman = prefs->analyzeForChordFunction() && prefs->showRomanNumeralsInStatusBar();
    const bool wantNashville = prefs->analyzeForChordFunction() && prefs->showNashvilleNumbersInStatusBar();

    const mu::composing::analysis::ChordSymbolFormatter::Options fmtOpts{ scoreNoteSpelling(note->score()) };
    int shown = 0;
    const int maxShown = prefs->analysisAlternatives();
    std::string candidates;
    std::set<std::string> seenKeys;

    for (const auto& result : chordResults) {
        if (shown >= maxShown) {
            break;
        }

        std::string sym, roman, nashville;
        if (wantSym) {
            sym = mu::composing::analysis::ChordSymbolFormatter::formatSymbol(result, keyFifths, fmtOpts);
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

    // When the enclosing KeyArea differs from the per-region key, surface both:
    // the per-region analysis (what the analyzer saw locally) and the enclosing
    // structural area (what the gate determined for the broader context).
    std::string areaStr;
    if (context.enclosingKeyArea.has_value()) {
        const auto& ka = *context.enclosingKeyArea;
        if (ka.keyFifths != keyFifths || ka.mode != keyMode) {
            using mu::composing::analysis::keyModeTonicName;
            using mu::composing::analysis::keyModeSuffix;
            areaStr = std::string(keyModeTonicName(ka.keyFifths, ka.mode))
                      + " " + keyModeSuffix(ka.mode);
        }
    }

    if (!keyStr.empty() && !areaStr.empty()) {
        return headed + " in key: " + keyStr + " (in area: " + areaStr + ")";
    }
    if (!keyStr.empty()) {
        return headed + " in key: " + keyStr;
    }
    if (!areaStr.empty()) {
        return headed + " (in area: " + areaStr + ")";
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

    std::set<size_t> excludeStaves = chordTrackExcludeStaves(sc);

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

    std::set<size_t> excludeStaves = chordTrackExcludeStaves(sc);

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

// ── formatChordResultForStatusBar / chordTrackExcludeStaves ──────────────────

namespace mu::notation {

FormattedChordResult formatChordResultForStatusBar(
    const mu::engraving::Score* sc,
    const mu::composing::analysis::ChordAnalysisResult& result,
    int keyFifths)
{
    const mu::composing::analysis::ChordSymbolFormatter::Options fmtOpts{ scoreNoteSpelling(sc) };
    return FormattedChordResult{
        mu::composing::analysis::ChordSymbolFormatter::formatSymbol(result, keyFifths, fmtOpts),
        mu::composing::analysis::ChordSymbolFormatter::formatRomanNumeral(result),
        mu::composing::analysis::ChordSymbolFormatter::formatNashvilleNumber(result, keyFifths)
    };
}

std::set<size_t> chordTrackExcludeStaves(const mu::engraving::Score* sc)
{
    return mu::notation::internal::chordTrackExcludeStaves(sc);
}

} // namespace mu::notation

// ── addHarmonicAnnotationsToSelection ────────────────────────────────────────

namespace mu::notation {

namespace {

// Phase 3b: emitter-side options for emitHarmonicAnnotations.  Defaults
// reproduce the pre-refactor addHarmonicAnnotationsToSelection behaviour
// — most importantly the 0.5-beat divergence-C duration gate.
//
// Kept anonymous-namespace-internal: the only caller today is the wrapper
// addHarmonicAnnotationsToSelection below.  Phase 4+ may promote to the
// public bridge header if a second caller appears.
struct EmitAnnotationOptions {
    /// Regions shorter than this are silently dropped (divergence C).
    /// Default Fraction(1, 2) = 0.5 beats matches the pre-Phase-3b default
    /// preference and the snapshot baseline.  Phase 3b ships an observation
    /// report (docs/divergence_c_observation.md) summarising the corpus
    /// regions affected by this gate; resolution is a follow-up decision.
    mu::engraving::Fraction minimumDisplayDurationBeats = mu::engraving::Fraction(1, 2);

    /// Selection upper bound in ticks (exclusive).  Regions whose startTick
    /// is below this are emitted; later regions are read-only lookahead used
    /// only by cadence / pivot detection.
    int selectionEndTick = 0;

    /// Output staves resolved by the wrapper using the chord-track-priority
    /// rule.  Empty = nothing to emit.
    std::vector<mu::engraving::staff_idx_t> writeStaves;

    bool writeChordSymbols = false;
    bool writeRomanNumerals = false;
    bool writeNashvilleNumbers = false;
};

void emitHarmonicAnnotations(mu::engraving::Score* score,
                             const mu::composing::analysis::AnalyzedSection& section,
                             const EmitAnnotationOptions& options)
{
    using namespace mu::engraving;
    using mu::composing::analysis::AnalyzedRegion;
    using mu::composing::analysis::KeyArea;
    using mu::composing::analysis::KeySigMode;
    using mu::composing::analysis::ChordQuality;
    using mu::composing::analysis::ionianTonicPcFromFifths;
    using mu::composing::analysis::keyModeTonicOffset;
    using mu::composing::analysis::keyModeTonicName;
    using mu::composing::analysis::keyModeSuffix;
    using mu::notation::internal::PivotLabel;

    if (!score || section.regions.empty() || options.writeStaves.empty()) {
        return;
    }
    if (!options.writeChordSymbols
        && !options.writeRomanNumerals
        && !options.writeNashvilleNumbers) {
        return;
    }

    const auto& allRegions = section.regions;
    const auto& keyAreas   = section.keyAreas;

    // Split into in-selection vs. lookahead based on options.selectionEndTick.
    const size_t selectionCount = static_cast<size_t>(
        std::count_if(allRegions.begin(), allRegions.end(),
            [&options](const AnalyzedRegion& r) {
                return r.startTick < options.selectionEndTick;
            }));

    // Convert the Fraction-of-beats gate to an integer tick threshold once.
    // The pre-Phase-3b gate compared `(endTick - startTick) / DIVISION` against
    // the preference value as doubles; the integer form is exact for any
    // Fraction-typed option (including the default Fraction(1, 2) → 240 ticks).
    const int minDurationTicks =
        static_cast<int>(static_cast<int64_t>(options.minimumDisplayDurationBeats.numerator())
                         * Constants::DIVISION
                         / options.minimumDisplayDurationBeats.denominator());

    // Pre-compute pivot labels: needed before the main loop (to suppress duplicate
    // boundary markers at pivot transitions) and reused for final emission.
    // detectPivotChords is called once here instead of twice.
    std::vector<PivotLabel> allPivots;
    if (options.writeRomanNumerals && !options.writeStaves.empty()) {
        allPivots = detectPivotChords(allRegions, selectionCount);
    }

    // Bracket marker format: "[G:]" major, "[g:]" minor, "[D Dor:]" Dorian, etc.
    // Aldwell/Laitz: major-like modes uppercase tonic, minor-like modes lowercase.
    auto makeBracketMarker = [](const KeyArea& ka) -> std::string {
        const char* tonicRaw = keyModeTonicName(ka.keyFifths, ka.mode);
        std::string tonic(tonicRaw);
        const bool isMajorLike = (ka.mode == KeySigMode::Ionian
                                  || ka.mode == KeySigMode::Lydian
                                  || ka.mode == KeySigMode::Mixolydian);
        if (!isMajorLike && !tonic.empty() && tonic[0] >= 'A' && tonic[0] <= 'Z') {
            tonic[0] = static_cast<char>(tonic[0] + ('a' - 'A'));
        }
        if (ka.mode == KeySigMode::Ionian
            || ka.mode == KeySigMode::Aeolian
            || ka.mode == KeySigMode::HarmonicMinor
            || ka.mode == KeySigMode::MelodicMinor) {
            return "[" + tonic + ":]";
        }
        return "[" + tonic + " " + keyModeSuffix(ka.mode) + ":]";
    };

    score->startCmd(TranslatableString("undoableAction", "Add harmonic annotations to selection"));

    // Tracks the enclosing KeyArea as we iterate regions.  -1 = not yet entered.
    int activeKeyAreaId = -1;

    for (size_t i = 0; i < selectionCount; ++i) {
        const AnalyzedRegion& region = allRegions[i];

        // Divergence-C minimum duration gate.
        if (minDurationTicks > 0
            && (region.endTick - region.startTick) < minDurationTicks) {
            continue;
        }

        // ── KeyArea transition (Phase 5b) ─────────────────────────────────────
        // When the region's enclosing KeyArea changes, write a bracketed key-
        // prefix marker ("[G:]") at the new area's first tick — unless
        // detectPivotChords already placed a pivot label in the outgoing area
        // (the pivot communicates the transition; the bracket would be redundant).
        const int regionKeyAreaId = region.keyAreaId;
        if (options.writeRomanNumerals
            && regionKeyAreaId >= 0
            && regionKeyAreaId != activeKeyAreaId
            && activeKeyAreaId >= 0
            && regionKeyAreaId < static_cast<int>(keyAreas.size())) {
            const int prevAreaStart = keyAreas[activeKeyAreaId].startTick;
            const int newAreaStart  = keyAreas[regionKeyAreaId].startTick;
            const bool hasPivot = std::any_of(allPivots.begin(), allPivots.end(),
                [prevAreaStart, newAreaStart](const PivotLabel& pv) {
                    return pv.tick >= prevAreaStart && pv.tick < newAreaStart;
                });
            if (!hasPivot && newAreaStart < options.selectionEndTick) {
                const Fraction mTick = Fraction::fromTicks(newAreaStart);
                Segment* mSeg = score->tick2segment(mTick, true, SegmentType::ChordRest);
                if (mSeg) {
                    Harmony* bh = Factory::createHarmony(mSeg);
                    bh->setTrack(options.writeStaves.front() * VOICES);
                    bh->setParent(mSeg);
                    bh->setHarmonyType(HarmonyType::ROMAN);
                    bh->setHarmony(muse::String::fromStdString(
                        makeBracketMarker(keyAreas[regionKeyAreaId])));
                    score->undoAddElement(bh);
                }
            }
        }
        if (regionKeyAreaId >= 0) {
            activeKeyAreaId = regionKeyAreaId;
        }

        const Fraction rStart = Fraction::fromTicks(region.startTick);
        Segment* seg = score->tick2segment(rStart, true, SegmentType::ChordRest);
        if (!seg || seg->tick() >= Fraction::fromTicks(region.endTick)) {
            continue;
        }

        // Per-region key (accurate for status bar and chord symbol spelling).
        const int perRegionFifths = region.keyModeResult.keySignatureFifths;
        const auto perRegionMode  = region.keyModeResult.mode;

        // Effective key for Roman numerals: enclosing KeyArea when available,
        // per-region key as fallback.  This is the Phase 5b behavior change:
        // regions absorbed into an enclosing area get Romans in the area's key,
        // not the transient local key the confidence gate suppressed.
        int romanKeyFifths = perRegionFifths;
        KeySigMode romanKeyMode = perRegionMode;
        if (options.writeRomanNumerals
            && activeKeyAreaId >= 0
            && activeKeyAreaId < static_cast<int>(keyAreas.size())) {
            romanKeyFifths = keyAreas[activeKeyAreaId].keyFifths;
            romanKeyMode   = keyAreas[activeKeyAreaId].mode;
        }

        // Re-contextualize the chord result when the roman key differs from the
        // per-region key: recompute degree and tonal function for the area key.
        mu::composing::analysis::ChordAnalysisResult annotationResult = region.chordResult;
        if (options.writeRomanNumerals
            && (romanKeyFifths != perRegionFifths || romanKeyMode != perRegionMode)) {
            const int ionianPc = ionianTonicPcFromFifths(romanKeyFifths);
            const int tonicPc  = (ionianPc + keyModeTonicOffset(romanKeyMode)) % 12;
            annotationResult.function.degree
                = diatonicDegreeForRootPc(annotationResult.identity.rootPc,
                                          romanKeyFifths, romanKeyMode);
            annotationResult.function.diatonicToKey = (annotationResult.function.degree >= 0);
            annotationResult.function.keyTonicPc    = tonicPc;
            annotationResult.function.keyMode       = romanKeyMode;
        }

        const FormattedChordResult fmt = formatChordResultForStatusBar(score, annotationResult, perRegionFifths);
        const std::string symText = options.writeChordSymbols ? fmt.symbol : "";
        std::string romanText = options.writeRomanNumerals ? fmt.roman : "";
        if (options.writeRomanNumerals && romanText.empty()
                && annotationResult.identity.quality == ChordQuality::Unknown
                && annotationResult.function.degree >= 0
                && annotationResult.function.degree <= 6) {
            auto refinedForRoman = annotationResult;
            mu::notation::internal::forceChordTrackQualityFromKeyContext(refinedForRoman, romanKeyMode);
            if (refinedForRoman.identity.quality != ChordQuality::Unknown) {
                romanText = mu::composing::analysis::ChordSymbolFormatter::formatRomanNumeral(refinedForRoman);
            }
        }
        const std::string nashvilleText = options.writeNashvilleNumbers ? fmt.nashville : "";

        for (staff_idx_t si : options.writeStaves) {
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
        if (options.writeRomanNumerals
                && !options.writeStaves.empty()
                && annotationResult.identity.isPedalPoint
                && annotationResult.identity.pedalBassPc >= 0) {
            // Build a bare root-name result for the pedal bass PC.
            mu::composing::analysis::ChordAnalysisResult pedalRoot = annotationResult;
            pedalRoot.identity.rootPc  = annotationResult.identity.pedalBassPc;
            pedalRoot.identity.bassPc  = annotationResult.identity.pedalBassPc;
            pedalRoot.identity.quality = ChordQuality::Major;
            pedalRoot.identity.extensions = 0;
            const std::string baseName = formatChordResultForStatusBar(score, pedalRoot, perRegionFifths).symbol;
            if (!baseName.empty()) {
                const std::string pedalText = baseName + " ped.";
                const track_idx_t pedTrack = options.writeStaves.front() * VOICES;
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
    if (options.writeRomanNumerals && !options.writeStaves.empty()) {
        const track_idx_t annotateTrack = options.writeStaves.front() * VOICES;

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

        // allPivots pre-computed above; reuse here to avoid a second detectPivotChords call.
        for (const auto& pv : allPivots) {
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

} // namespace

// Phase 3b: thin wrapper over the unified analyzeSection() + emitter split.
// Builds the EmitAnnotationOptions that reproduce the pre-refactor behaviour
// (lookahead range for Roman numerals, chord-track-priority output staves,
// 0.5-beat default duration gate from the user preference) and forwards.
// Kept at this signature so existing call sites stay untouched.
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
    std::set<size_t> excludeStaves = chordTrackExcludeStaves(score);

    // Chord-track priority rule: if any selected staff is a chord track staff,
    // write only to those; otherwise write to all selected staves.
    bool hasChordTrackInSelection = false;
    for (staff_idx_t si = staffFirst; si < staffLast; ++si) {
        if (isChordTrackStaff(score, si)) {
            hasChordTrackInSelection = true;
            break;
        }
    }

    EmitAnnotationOptions options;
    options.selectionEndTick = endTick.ticks();
    options.writeChordSymbols    = writeChordSymbols;
    options.writeRomanNumerals   = writeRomanNumerals;
    options.writeNashvilleNumbers = writeNashvilleNumbers;
    for (staff_idx_t si = staffFirst; si < staffLast; ++si) {
        if (!hasChordTrackInSelection || isChordTrackStaff(score, si)) {
            options.writeStaves.push_back(si);
        }
    }

    if (options.writeStaves.empty()) {
        return;
    }

    // Translate the user-pref double into the Fraction-typed option.  The
    // default 0.5 maps to Fraction(1, 2) → 240 ticks at DIVISION = 480, which
    // is exactly the pre-refactor gate.  A denominator of 1024 keeps any
    // non-default user preference within sub-tick precision so the integer
    // tick threshold matches the original double comparison.
    static muse::GlobalInject<mu::composing::IComposingAnalysisConfiguration> config;
    const auto* prefs = config.get().get();
    const double prefBeats = prefs ? prefs->minimumDisplayDurationBeats() : 0.5;
    constexpr int kFractionDenom = 1024;
    options.minimumDisplayDurationBeats =
        Fraction(static_cast<int>(prefBeats * kFractionDenom + 0.5), kFractionDenom);

    // Run harmonic analysis over an extended tick range when Roman numerals
    // are requested.  The lookahead regions are read-only: used for cadence
    // and pivot detection but never annotated.
    const Fraction lookaheadEndTick = writeRomanNumerals
        ? Fraction::fromTicks(endTick.ticks()
            + mu::notation::internal::kMaxPivotLookaheadRegions
              * 4 * Constants::DIVISION)  // ~8 measures of lookahead
        : endTick;

    const auto section = mu::notation::internal::analyzeSection(
        score, startTick, lookaheadEndTick, excludeStaves);

    if (section.regions.empty()) {
        return;
    }

    emitHarmonicAnnotations(score, section, options);
}

} // namespace mu::notation
