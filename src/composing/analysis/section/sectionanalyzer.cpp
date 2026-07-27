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

// ── Unified section-level analysis ───────────────────────────────────────────
//
// analyzeSection() + key/mode stabilization + cadence / pivot detection.
// Relocated from notation/internal/notationcomposingbridgehelpers.cpp in
// Stage 2.1 (Phase 4c).  Pass 0 (boundary detection) is supplied by the caller
// as `rawRegions` — see sectionanalyzer.h.

#include "composing/analysis/section/sectionanalyzer.h"
#include "composing/analysis/param/paramoverride.h"   // Stage-5 fitter: G10 override (D-6)

#include <algorithm>
#include <array>
#include <cmath>
#include <limits>
#include <map>
#include <optional>
#include <set>
#include <tuple>

#include "engraving/dom/chord.h"
#include "engraving/dom/key.h"
#include "engraving/dom/masterscore.h"
#include "engraving/dom/measure.h"
#include "engraving/dom/note.h"
#include "engraving/dom/segment.h"
#include "engraving/dom/sig.h"
#include "engraving/dom/staff.h"
#include "engraving/types/constants.h"

#include "composing/analysis/chord/analysisutils.h"
#include "composing/analysis/chord/chordanalyzer.h"
#include "composing/analysis/engravingbridge/regiontonecollector.h"
#include "composing/analysis/key/keymodeanalyzer.h"
#include "composing/analysis/region/sparsechordrefinement.h"
#include "composing/analysis/section/jointkeydecision.h"   // J-key-iii wiring flag

namespace ebr = mu::composing::analysis::engravingbridge;
namespace cra = mu::composing::analysis::region;

namespace mu::composing::analysis {

namespace {

// Stage-5 fitter: register the G10 section-layer abstention bar (kAnnotateKeyConfidenceThreshold).
// Byte-identical when no override is loaded; this TU is odr-used (analyzeSection) so the
// registration runs at static-init.
const bool s_registerSectionParams = [] {
    mu::composing::params::registerDouble("kAnnotateKeyConfidenceThreshold",
                                          &kAnnotateKeyConfidenceThreshold);
    return true;
}();

// The legacy-arm key-exposure bucket: 0 = below tentative, 1 = tentative, 2 = assertive, from the
// per-region normalizedConfidence at the 0.5 / 0.8 thresholds. These two literals are the legacy
// exposure thresholds (formerly kTentativeKeyExposureThreshold / kAssertiveKeyExposureThreshold,
// re-thresholded inside the implode bridge's keyExposureBucket / supportsTentativeKeyExposure). Storing
// the bucket ONCE here (beside hasAssertiveExposure) gives the implode emitter one thresholding site to
// read (#6) and lets the record arm set the bucket from the P1 gap constants without any consumer
// comparing a nats gap to a [0,1] literal. Byte-identical to the former implode-local computation.
// LEGACY-ARM ONLY: these literals retire with the legacy analysis path (OI-180); the record arm's
// bucket comes from the gap constants in sectionrecordadapter.cpp.
constexpr double kLegacyTentativeKeyExposureThreshold = 0.5;
constexpr double kLegacyAssertiveKeyExposureThreshold = 0.8;

int legacyKeyExposureBucket(double confidence)
{
    if (confidence < kLegacyTentativeKeyExposureThreshold) {
        return 0;
    }
    if (confidence < kLegacyAssertiveKeyExposureThreshold) {
        return 1;
    }
    return 2;
}

int distinctPitchClassCount(const std::vector<mu::composing::analysis::ChordAnalysisTone>& tones)
{
    bool seenPitchClasses[12] = {};
    int count = 0;
    for (const auto& tone : tones) {
        const int pitchClass = tone.pitch % 12;
        if (seenPitchClasses[pitchClass]) {
            continue;
        }
        seenPitchClasses[pitchClass] = true;
        ++count;
    }
    return count;
}

void stabilizeHarmonicRegionsForDisplay(std::vector<mu::composing::analysis::AnalyzedRegion>& regions)
{
    using namespace mu::composing::analysis;

    if (regions.empty()) {
        return;
    }

    // Layer B — 1-region-island key stabilization.  J-key-iii: when the joint
    // re-key wiring is ENABLED, the per-region key is already the global key-path
    // Viterbi decision (decideJointKey IS the smoothing layer), so this island
    // stabilization is made INERT (skipped) — otherwise it would re-smooth the joint
    // keys and break the §5 invariant (wired key == measured softTonicPc/softIsMajor;
    // dossier §5, the "override after Layer B" disposition).  Default OFF ⇒ unchanged.
    if (!jointKeyWiringEnabled()) {
        int stableKeyFifths = regions.front().keyModeResult.keySignatureFifths;
        KeySigMode stableMode = regions.front().keyModeResult.mode;

        for (size_t i = 1; i < regions.size(); ++i) {
            const int regionKeyFifths = regions[i].keyModeResult.keySignatureFifths;
            const KeySigMode regionMode = regions[i].keyModeResult.mode;
            if (regionKeyFifths != stableKeyFifths || regionMode != stableMode) {
                bool persistent = (i + 1 >= regions.size());
                if (!persistent) {
                    const int nextKeyFifths = regions[i + 1].keyModeResult.keySignatureFifths;
                    const KeySigMode nextMode = regions[i + 1].keyModeResult.mode;
                    persistent = (nextKeyFifths == regionKeyFifths && nextMode == regionMode);
                }
                if (persistent) {
                    stableKeyFifths = regionKeyFifths;
                    stableMode = regionMode;
                }
            }
            regions[i].keyModeResult.keySignatureFifths = stableKeyFifths;
            regions[i].keyModeResult.mode = stableMode;
        }
    }

    for (auto& region : regions) {
        const int ionianPc = ionianTonicPcFromFifths(region.keyModeResult.keySignatureFifths);
        const int tonicPc = (ionianPc + keyModeTonicOffset(region.keyModeResult.mode)) % 12;
        const auto& scale = keyModeScaleIntervals(region.keyModeResult.mode);

        region.chordResult.function.degree = cra::diatonicDegreeForRootPc(
            region.chordResult.identity.rootPc,
            region.keyModeResult.keySignatureFifths,
            region.keyModeResult.mode);
        region.chordResult.function.keyTonicPc = tonicPc;
        region.chordResult.function.keyMode = region.keyModeResult.mode;

        bool diatonic = (region.chordResult.function.degree >= 0);
        if (diatonic) {
            for (const auto& tone : region.tones) {
                const int pc = tone.pitch % 12;
                bool inScale = false;
                for (int interval : scale) {
                    if ((tonicPc + interval) % 12 == pc) {
                        inScale = true;
                        break;
                    }
                }
                if (!inScale) {
                    diatonic = false;
                    break;
                }
            }
        }
        region.chordResult.function.diatonicToKey = diatonic;
        cra::refineSparseChordQualityFromKeyContext(region.chordResult,
                                               region.tones,
                                               region.keyModeResult.keySignatureFifths,
                                               region.keyModeResult.mode);
    }
}

} // namespace

// ── analyzeSection ───────────────────────────────────────────────────────────
//
// Canonical implementation of the unified analysis pipeline
// (docs/unified_analysis_pipeline.md).  Inlines Passes 1–4 and operates
// natively on AnalyzedRegion.  Pass 0 (boundary detection) is supplied by the
// caller as `rawRegions` (see sectionanalyzer.h).
mu::composing::analysis::AnalyzedSection
analyzeSection(const mu::engraving::Score* sc,
               const mu::engraving::Fraction& from,
               const mu::engraving::Fraction& to,
               const std::set<size_t>& excludeStaves,
               const std::vector<mu::composing::analysis::HarmonicRegion>& rawRegions,
               const mu::composing::analysis::ChordAnalyzerPreferences& chordPrefs)
{
    using namespace mu::engraving;
    using namespace mu::composing::analysis;

    AnalyzedSection out;
    out.startTick = from.ticks();
    out.endTick   = to.ticks();

    if (!sc || to <= from) {
        return out;
    }

    // LAYER 1 — build the lossless, tie-resolved note model ONCE for this
    // section's score; the weighted-PC views below derive over it.
    const mu::composing::analysis::notemodel::NoteModel noteModel
        = mu::composing::analysis::notemodel::NoteModel::build(sc);

    // Pass 0: boundary detection supplied by the caller (notation-side
    // analyzeHarmonicRhythm, Smoothed granularity) and injected as `rawRegions`
    // — keeps this module free of the notation / configuration layers (Stage 2.1).
    if (rawRegions.empty()) {
        return out;
    }

    // Boundary: convert HarmonicRegion → AnalyzedRegion.  All display passes
    // below operate on AnalyzedRegion natively.  hasAssertiveExposure is
    // recomputed per-region after Pass 4 (stabilization).
    std::vector<AnalyzedRegion> regions;
    regions.reserve(rawRegions.size());
    for (const auto& src : rawRegions) {
        AnalyzedRegion r;
        r.startTick            = src.startTick;
        r.endTick              = src.endTick;
        r.chordResult          = src.chordResult;
        r.alternatives         = src.alternatives;
        r.hasAnalyzedChord     = src.hasAnalyzedChord;
        r.keyModeResult        = src.keyModeResult;
        r.tones                = src.tones;
        r.temporalExtensions   = src.temporalExtensions;
        r.hasAssertiveExposure = false;  // recomputed after stabilization
        r.keyAreaId            = -1;
        regions.push_back(std::move(r));
    }

    // Pass 1: gap-tone region insertion and measure-level layout.
    const auto chordAnalyzer = ChordAnalyzerFactory::create();
    auto sameChordIdentity = [](const AnalyzedRegion& lhs, const AnalyzedRegion& rhs) {
        return lhs.chordResult.identity.rootPc == rhs.chordResult.identity.rootPc
               && lhs.chordResult.identity.quality == rhs.chordResult.identity.quality;
    };
    auto regionSupportsGapTones = [](const std::vector<ChordAnalysisTone>& gapTones,
                                     const AnalyzedRegion& region) {
        if (region.chordResult.identity.quality == ChordQuality::Suspended2
            || region.chordResult.identity.quality == ChordQuality::Suspended4) {
            return false;
        }

        const std::vector<int> chordPitchClasses = chordTonePitchClasses(region.chordResult);
        if (gapTones.empty() || chordPitchClasses.empty()) {
            return false;
        }

        bool seenGapPitchClasses[12] = {};
        bool matchesRegionAnchor = false;
        for (const auto& tone : gapTones) {
            const int pitchClass = tone.pitch % 12;
            if (seenGapPitchClasses[pitchClass]) {
                continue;
            }
            seenGapPitchClasses[pitchClass] = true;

            if (pitchClass == region.chordResult.identity.rootPc
                || pitchClass == region.chordResult.identity.bassPc) {
                matchesRegionAnchor = true;
            }

            if (std::find(chordPitchClasses.begin(), chordPitchClasses.end(), pitchClass) == chordPitchClasses.end()) {
                return false;
            }
        }

        return matchesRegionAnchor;
    };
    auto applyGapKeyContext = [](ChordAnalysisResult& result,
                                 const std::vector<ChordAnalysisTone>& gapTones,
                                 int keyFifths,
                                 KeySigMode keyMode) {
        const int ionianTonicPc = ionianTonicPcFromFifths(keyFifths);
        const int tonicPc = (ionianTonicPc + keyModeTonicOffset(keyMode)) % 12;
        const auto& scale = keyModeScaleIntervals(keyMode);

        result.function.keyTonicPc = tonicPc;
        result.function.keyMode = keyMode;
        result.function.degree = cra::diatonicDegreeForRootPc(result.identity.rootPc, keyFifths, keyMode);

        bool diatonicToKey = (result.function.degree >= 0);
        if (diatonicToKey) {
            for (const auto& tone : gapTones) {
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
    };
    auto inferSparseGapChord = [&](const std::vector<ChordAnalysisTone>& gapTones,
                                   int keyFifths,
                                   KeySigMode keyMode,
                                   ChordAnalysisResult& outResult) {
        const auto* bassTone = bassToneFromTones(gapTones);
        if (!bassTone) {
            bassTone = &gapTones.front();
            for (const auto& tone : gapTones) {
                if (tone.pitch < bassTone->pitch) {
                    bassTone = &tone;
                }
            }
        }

        bool seenPitchClasses[12] = {};
        std::vector<int> pitchClasses;
        pitchClasses.reserve(gapTones.size());
        for (const auto& tone : gapTones) {
            const int pitchClass = tone.pitch % 12;
            if (!seenPitchClasses[pitchClass]) {
                seenPitchClasses[pitchClass] = true;
                pitchClasses.push_back(pitchClass);
            }
        }

        if (pitchClasses.empty()) {
            return false;
        }

        outResult = {};
        outResult.identity.score = 0.0;

        if (pitchClasses.size() == 1) {
            outResult.identity.rootPc = pitchClasses.front();
            outResult.identity.bassPc = pitchClasses.front();
            outResult.identity.bassTpc = bassTone->tpc;
            outResult.identity.quality = ChordQuality::Unknown;
            applyGapKeyContext(outResult, gapTones, keyFifths, keyMode);
            return true;
        }

        struct SparseCandidate {
            int rootPc = -1;
            ChordQuality quality = ChordQuality::Unknown;
            int priority = -1;
        };

        std::optional<SparseCandidate> bestCandidate;
        for (int candidateRootPc : pitchClasses) {
            bool hasMinorThird = false;
            bool hasMajorThird = false;
            bool hasFifth = false;
            bool hasDimFifth = false;
            bool supported = true;

            for (int tonePc : pitchClasses) {
                if (tonePc == candidateRootPc) {
                    continue;
                }

                const int interval = (tonePc - candidateRootPc + 12) % 12;
                if (interval == 3) {
                    hasMinorThird = true;
                } else if (interval == 4) {
                    hasMajorThird = true;
                } else if (interval == 6) {
                    hasDimFifth = true;
                } else if (interval == 7) {
                    hasFifth = true;
                } else {
                    supported = false;
                    break;
                }
            }

            if (!supported) {
                continue;
            }

            SparseCandidate candidate;
            candidate.rootPc = candidateRootPc;
            if (hasMajorThird) {
                candidate.quality = ChordQuality::Major;
                candidate.priority = 3;
            } else if (hasMinorThird) {
                candidate.quality = ChordQuality::Minor;
                candidate.priority = 3;
            } else if (hasDimFifth) {
                candidate.quality = ChordQuality::Diminished;
                candidate.priority = 2;
            } else if (hasFifth) {
                candidate.quality = ChordQuality::Unknown;
                candidate.priority = 1;
            } else {
                continue;
            }

            if (!bestCandidate || candidate.priority > bestCandidate->priority) {
                bestCandidate = candidate;
            }
        }

        if (bestCandidate) {
            outResult.identity.rootPc = bestCandidate->rootPc;
            outResult.identity.bassPc = bestCandidate->rootPc;
            outResult.identity.bassTpc = bassTone->tpc;
            outResult.identity.quality = bestCandidate->quality;
            applyGapKeyContext(outResult, gapTones, keyFifths, keyMode);
            return true;
        }

        return false;
    };
    auto analyzeGapWithContext = [&](const std::vector<ChordAnalysisTone>& gapTones,
                                     const AnalyzedRegion& contextRegion,
                                     int gapStartTick,
                                     int gapEndTick) -> std::optional<AnalyzedRegion> {
        AnalyzedRegion inferredRegion;
        inferredRegion.startTick = gapStartTick;
        inferredRegion.endTick = gapEndTick;
        inferredRegion.hasAnalyzedChord = true;
        inferredRegion.keyModeResult = contextRegion.keyModeResult;
        inferredRegion.tones = gapTones;

        mu::composing::analysis::PostScoringGateContext gapGateCtx;
        auto results = chordAnalyzer->analyzeChord(gapTones,
                                                   contextRegion.keyModeResult.keySignatureFifths,
                                                   contextRegion.keyModeResult.mode,
                                                   nullptr,
                                                   chordPrefs,
                                                   &gapGateCtx);
        if (!results.empty()) {
            mu::composing::analysis::applyIter8691Pedal(
                results,
                gapGateCtx,
                nullptr,
                chordPrefs);
            mu::composing::analysis::applyPostScoringGates(
                results,
                chordPrefs,
                nullptr,
                gapGateCtx);
        }
        if (!results.empty()) {
            inferredRegion.chordResult = results.front();
            if (results.size() > 1) {
                inferredRegion.alternatives.assign(results.begin() + 1, results.end());
            }
            // Gap analyzer is invoked context-free; temporalExtensions stays at defaults.
            return inferredRegion;
        }

        if (inferSparseGapChord(gapTones,
                                contextRegion.keyModeResult.keySignatureFifths,
                                contextRegion.keyModeResult.mode,
                                inferredRegion.chordResult)) {
            return inferredRegion;
        }

        return std::nullopt;
    };
    auto inferGapRegion = [&](int gapStartTick,
                              int gapEndTick,
                              const AnalyzedRegion* previousRegion,
                              const AnalyzedRegion* nextRegion) -> std::optional<AnalyzedRegion> {
        if (gapEndTick <= gapStartTick) {
            return std::nullopt;
        }

        const auto gapTones = ebr::weightedPcView(noteModel,
                                                 gapStartTick,
                                                 gapEndTick,
                                                 excludeStaves);
        if (gapTones.empty()) {
            const AnalyzedRegion* carriedSource = previousRegion ? previousRegion : nextRegion;
            if (!carriedSource) {
                return std::nullopt;
            }

            AnalyzedRegion carriedRegion = *carriedSource;
            carriedRegion.startTick = gapStartTick;
            carriedRegion.endTick = gapEndTick;
            carriedRegion.tones.clear();
            carriedRegion.hasAnalyzedChord = true;
            return carriedRegion;
        }

        auto carryGapRegion = [&](const AnalyzedRegion& sourceRegion) {
            AnalyzedRegion carriedRegion = sourceRegion;
            carriedRegion.startTick = gapStartTick;
            carriedRegion.endTick = gapEndTick;
            carriedRegion.tones = gapTones;
            carriedRegion.hasAnalyzedChord = true;
            return carriedRegion;
        };

        int uniqueGapPitchClasses = 0;
        bool seenGapPitchClasses[12] = {};
        for (const auto& tone : gapTones) {
            const int pitchClass = tone.pitch % 12;
            if (seenGapPitchClasses[pitchClass]) {
                continue;
            }
            seenGapPitchClasses[pitchClass] = true;
            ++uniqueGapPitchClasses;
        }

        if (uniqueGapPitchClasses < 3) {
            // When the gap has only one pitch class, a single note that coincides
            // with the ROOT of an adjacent chord carries no quality information —
            // the diatonic shape from the key context is more reliable.  But if
            // the lone gap note is a non-root chord tone of the adjacent region
            // (e.g. the third or fifth), the carry is appropriate because that
            // interval relationship identifies the chord quality.
            auto supportsCarry = [&](const AnalyzedRegion& region) -> bool {
                if (!regionSupportsGapTones(gapTones, region)) {
                    return false;
                }
                if (uniqueGapPitchClasses == 1) {
                    const int gapPc = gapTones.front().pitch % 12;
                    if (gapPc == region.chordResult.identity.rootPc) {
                        return false;  // root alone → key context is more reliable
                    }
                }
                return true;
            };

            if (nextRegion && supportsCarry(*nextRegion)) {
                return carryGapRegion(*nextRegion);
            }

            if (previousRegion && supportsCarry(*previousRegion)) {
                return carryGapRegion(*previousRegion);
            }
        }

        if (previousRegion) {
            if (auto analyzedRegion = analyzeGapWithContext(gapTones,
                                                            *previousRegion,
                                                            gapStartTick,
                                                            gapEndTick)) {
                return analyzedRegion;
            }
        }

        if (nextRegion) {
            if (auto analyzedRegion = analyzeGapWithContext(gapTones,
                                                            *nextRegion,
                                                            gapStartTick,
                                                            gapEndTick)) {
                return analyzedRegion;
            }
        }

        if (previousRegion && regionSupportsGapTones(gapTones, *previousRegion)) {
            return carryGapRegion(*previousRegion);
        }

        if (nextRegion && regionSupportsGapTones(gapTones, *nextRegion)) {
            return carryGapRegion(*nextRegion);
        }

        if (!previousRegion && nextRegion) {
            AnalyzedRegion openingRegion = *nextRegion;
            openingRegion.startTick = gapStartTick;
            openingRegion.endTick = gapEndTick;
            openingRegion.tones = gapTones;
            openingRegion.hasAnalyzedChord = true;
            return openingRegion;
        }

        if (previousRegion && !nextRegion) {
            AnalyzedRegion trailingRegion = *previousRegion;
            trailingRegion.startTick = gapStartTick;
            trailingRegion.endTick = gapEndTick;
            trailingRegion.tones = gapTones;
            trailingRegion.hasAnalyzedChord = true;
            return trailingRegion;
        }

        // Both prev and next exist but no fitting test passed.  Rather than
        // returning nullopt (which leaves an uncovered gap in the measure and
        // produces mixed chord+rest measures on the chord track), carry the
        // previous chord forward as a last resort.
        if (previousRegion) {
            return carryGapRegion(*previousRegion);
        }

        return std::nullopt;
    };
    auto nextRegionStartingAtOrAfter = [&](int tick) -> const AnalyzedRegion* {
        const auto nextRegion = std::find_if(regions.begin(), regions.end(), [tick](const auto& region) {
            return region.startTick >= tick;
        });
        return nextRegion != regions.end() ? &*nextRegion : nullptr;
    };

    std::vector<AnalyzedRegion> displayRegions;
    displayRegions.reserve(regions.size() * 2);
    const int analysisRangeStartTick = from.ticks();

    for (Measure* measure = sc->tick2measure(from);
         measure && measure->tick() < to;
         measure = measure->nextMeasure()) {
        const Fraction measureRangeStart = std::max(measure->tick(), from);
        const Fraction measureRangeEnd = std::min(measure->endTick(), to);
        const int measureStartTick = measureRangeStart.ticks();
        const int measureEndTick = measureRangeEnd.ticks();

        std::vector<size_t> overlappingRegions;
        for (size_t i = 0; i < regions.size(); ++i) {
            if (regions[i].endTick > measureStartTick && regions[i].startTick < measureEndTick) {
                overlappingRegions.push_back(i);
            }
        }

        std::vector<AnalyzedRegion> measureRegions;
        auto appendMeasureRegion = [&](AnalyzedRegion region) {
            if (region.startTick >= region.endTick) {
                return;
            }
            if (!measureRegions.empty()
                && measureRegions.back().endTick == region.startTick
                && sameChordIdentity(measureRegions.back(), region)) {
                measureRegions.back().endTick = region.endTick;
                mergeChordAnalysisTones(measureRegions.back().tones, region.tones);
                return;
            }
            measureRegions.push_back(std::move(region));
        };

        const auto previousRegion = std::find_if(regions.rbegin(), regions.rend(), [measureStartTick](const auto& region) {
            return region.endTick <= measureStartTick;
        });
        const AnalyzedRegion* previousRegionPtr = previousRegion != regions.rend() ? &*previousRegion : nullptr;
        const AnalyzedRegion* nextRegionAfterMeasurePtr = nextRegionStartingAtOrAfter(measureEndTick);

        if (overlappingRegions.empty()) {
            if (auto gapRegion = inferGapRegion(measureStartTick,
                                                measureEndTick,
                                                previousRegionPtr,
                                                nextRegionAfterMeasurePtr)) {
                appendMeasureRegion(std::move(*gapRegion));
            }

            for (auto& measureRegion : measureRegions) {
                displayRegions.push_back(std::move(measureRegion));
            }
            continue;
        }

        std::optional<AnalyzedRegion> previousDisplayRegion;
        if (previousRegionPtr) {
            previousDisplayRegion = *previousRegionPtr;
        }

        int cursor = measureStartTick;

        for (size_t i = 0; i < overlappingRegions.size(); ++i) {
            const auto& sourceRegion = regions[overlappingRegions[i]];
            const int sourceStartTick = std::max(measureStartTick, sourceRegion.startTick);
            const int sourceEndTick = std::min(measureEndTick, sourceRegion.endTick);

            if (cursor < sourceStartTick) {
                if (measureRegions.empty() && cursor == analysisRangeStartTick) {
                    AnalyzedRegion openingRegion = sourceRegion;
                    openingRegion.startTick = cursor;
                    openingRegion.endTick = sourceStartTick;
                    openingRegion.tones = ebr::weightedPcView(noteModel,
                                                             openingRegion.startTick,
                                                             openingRegion.endTick,
                                                             excludeStaves);
                    appendMeasureRegion(std::move(openingRegion));
                } else if (auto gapRegion = inferGapRegion(cursor,
                                                           sourceStartTick,
                                                           previousDisplayRegion ? &*previousDisplayRegion : previousRegionPtr,
                                                           &sourceRegion)) {
                    appendMeasureRegion(std::move(*gapRegion));
                }

                if (!measureRegions.empty()) {
                    previousDisplayRegion = measureRegions.back();
                }
            }

            if (sourceStartTick >= sourceEndTick) {
                cursor = std::max(cursor, sourceEndTick);
                continue;
            }

            AnalyzedRegion displayRegion = sourceRegion;
            displayRegion.startTick = sourceStartTick;
            displayRegion.endTick = sourceEndTick;
            displayRegion.tones = ebr::weightedPcView(noteModel,
                                                     displayRegion.startTick,
                                                     displayRegion.endTick,
                                                     excludeStaves);
            appendMeasureRegion(std::move(displayRegion));
            previousDisplayRegion = measureRegions.back();
            cursor = sourceEndTick;
        }

        if (cursor < measureEndTick) {
            if (auto gapRegion = inferGapRegion(cursor,
                                                measureEndTick,
                                                previousDisplayRegion ? &*previousDisplayRegion : previousRegionPtr,
                                                nextRegionAfterMeasurePtr)) {
                appendMeasureRegion(std::move(*gapRegion));
            }
        }

        if (measureRegions.size() >= 2
            && measureRegions.front().startTick == measureStartTick
            && distinctPitchClassCount(measureRegions.front().tones) < 3
            && distinctPitchClassCount(measureRegions[1].tones) >= 3
            && measureRegions[1].startTick - measureStartTick <= Constants::DIVISION) {
            AnalyzedRegion carriedMeasureOpening = measureRegions[1];
            carriedMeasureOpening.startTick = measureStartTick;
            carriedMeasureOpening.tones = ebr::weightedPcView(noteModel,
                                                             carriedMeasureOpening.startTick,
                                                             carriedMeasureOpening.endTick,
                                                             excludeStaves);
            measureRegions[0] = std::move(carriedMeasureOpening);
            measureRegions.erase(measureRegions.begin() + 1);
        }

        for (auto& measureRegion : measureRegions) {
            displayRegions.push_back(std::move(measureRegion));
        }
    }

    // Pass 4: key/mode stabilization.
    stabilizeHarmonicRegionsForDisplay(displayRegions);

    // Post-stabilization: set hasAssertiveExposure + the key-exposure bucket on each display region
    // (the ONE legacy-arm set site for both — the implode emitter reads the stored results, #6).
    for (auto& r : displayRegions) {
        r.hasAssertiveExposure = hasAssertiveKeyConfidence(r.keyModeResult);
        r.keyExposureBucket = legacyKeyExposureBucket(r.keyModeResult.normalizedConfidence);
    }

    out.regions = std::move(displayRegions);

    // Key-areas: confidence-gated grouping (the shared helper — see sectionanalyzer.h). Reads the
    // stored per-region hasAssertiveExposure boolean set just above.
    groupKeyAreas(out.regions, out.keyAreas);

    return out;
}

// ── Key-area grouping (shared by the legacy and record arms) ──────────────────
//
// Lifted verbatim out of analyzeSection (byte-identical code movement) so the record-path variant
// (analyzeSectionFromRecord) shares the ONE grouping definition (#6). Documented in sectionanalyzer.h.
void groupKeyAreas(std::vector<mu::composing::analysis::AnalyzedRegion>& regions,
                   std::vector<mu::composing::analysis::KeyArea>& keyAreas)
{
    using namespace mu::composing::analysis;

    keyAreas.clear();

    // A new KeyArea opens at the first region, then only when:
    //   (a) the region's (keyFifths, mode) differs from the enclosing area, AND
    //   (b) the region is assertively exposed.
    // (b) reads the STORED per-region hasAssertiveExposure boolean rather than re-thresholding the
    // confidence field — ONE thresholding site per gate (#6). On the legacy arm this is byte-identical
    // (hasAssertiveExposure == normalizedConfidence >= 0.8); on the record arm the boolean is
    // gap >= the P1 assertive constant, and the confidence field carries a nats gap that must NOT be
    // compared to 0.8.
    //
    // Regions that disagree with the enclosing area but are not assertively exposed are silently
    // grouped into the enclosing area (keyAreaId unchanged). Their own keyModeResult is preserved
    // verbatim — status-bar display remains accurate; only the keyAreaId annotation grouping is
    // affected.
    for (size_t i = 0; i < regions.size(); ++i) {
        const AnalyzedRegion& region = regions[i];
        const int regionFifths = region.keyModeResult.keySignatureFifths;
        const KeySigMode regionMode = region.keyModeResult.mode;
        const double regionConfidence = region.keyModeResult.normalizedConfidence;

        const bool diverges = !keyAreas.empty()
            && (keyAreas.back().keyFifths != regionFifths
                || keyAreas.back().mode != regionMode);

        if (keyAreas.empty()
            || (diverges && region.hasAssertiveExposure)) {
            KeyArea area;
            area.startTick  = region.startTick;
            area.endTick    = region.endTick;
            area.keyFifths  = regionFifths;
            area.mode       = regionMode;
            area.confidence = regionConfidence;
            keyAreas.push_back(area);
        } else {
            KeyArea& back = keyAreas.back();
            back.endTick = region.endTick;
            if (regionConfidence > back.confidence) {
                back.confidence = regionConfidence;
            }
        }
        regions[i].keyAreaId = static_cast<int>(keyAreas.size()) - 1;
    }
}

} // namespace mu::composing::analysis
