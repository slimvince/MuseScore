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

// ── analyzeHarmonicRhythm ────────────────────────────────────────────────────
//
// Implements the analyzeHarmonicRhythm() free function declared in
// notationcomposingbridge.h.  Scans a time range across all eligible staves,
// detects harmonic boundaries, runs chord analysis at each boundary, and
// collapses consecutive same-chord regions.
//
// Shared engraving helpers (collectSoundingAt, resolveKeyAndMode, etc.) live
// in notationcomposingbridgehelpers.cpp.

#include "notationcomposingbridge.h"
#include "notationanalysisinternal.h"
#include "notationcomposingbridgehelpers.h"

#include <optional>
#include <set>
#include <vector>

#include "engraving/dom/chord.h"
#include "engraving/dom/masterscore.h"
#include "engraving/dom/segment.h"

#include "composing/analysis/chord/chordanalyzer.h"
#include "composing/analysis/region/harmonicrhythm.h"
#include "composing/analysis/key/keymodeanalyzer.h"
#include "composing/icomposinganalysisconfiguration.h"
#include "modularity/ioc.h"

using mu::notation::internal::staffIsEligible;
using mu::notation::internal::SoundingNote;
using mu::notation::internal::collectSoundingAt;
using mu::notation::internal::buildTones;
using mu::notation::internal::collectRegionTones;
using mu::notation::internal::detectHarmonicBoundariesJaccard;
using mu::notation::internal::detectOnsetSubBoundaries;
using mu::notation::internal::detectBassMovementSubBoundaries;
using mu::notation::internal::resolveKeyAndMode;
using mu::notation::internal::findTemporalContext;
using mu::notation::internal::isDiatonicStep;
using mu::notation::internal::distinctPitchClasses;

namespace mu::notation {

namespace {

thread_local internal::HarmonicRegionDebugCapture* s_harmonicRegionDebugCapture = nullptr;

/// Second-pass helper: populate nextRootPc in each region's ChordFunction so
/// that ChordSymbolFormatter::formatRomanNumeral() can emit V/x and vii°/x labels.
/// Called after all merge/absorb passes, before returning the final regions vector.
void backfillNextRootPc(std::vector<mu::composing::analysis::HarmonicRegion>& regions)
{
    for (size_t i = 0; i + 1 < regions.size(); ++i) {
        regions[i].chordResult.function.nextRootPc
            = regions[i + 1].chordResult.identity.rootPc;
    }
    // The last region has no successor — nextRootPc remains -1 (no tonicization label).
}

}

namespace internal {

void setHarmonicRegionDebugCapture(HarmonicRegionDebugCapture* capture)
{
    s_harmonicRegionDebugCapture = capture;
}

HarmonicRegionDebugCapture* harmonicRegionDebugCapture()
{
    return s_harmonicRegionDebugCapture;
}

} // namespace internal

std::vector<mu::composing::analysis::HarmonicRegion> analyzeHarmonicRhythm(
    const mu::engraving::Score* score,
    const mu::engraving::Fraction& startTick,
    const mu::engraving::Fraction& endTick,
    const std::set<size_t>& excludeStaves,
    HarmonicRegionGranularity granularity)
{
    using namespace mu::engraving;
    using namespace mu::composing::analysis;
    using mu::composing::analysis::KeySigMode;  // disambiguate from mu::engraving::KeyMode

    if (!score || endTick <= startTick) {
        return {};
    }

    // Find the first ChordRest segment at or after startTick.
    const Segment* seg = score->tick2segment(startTick, true, SegmentType::ChordRest);
    if (!seg) {
        return {};
    }

    // Resolve key/mode at the start of the range.  Use staff 0 as the reference
    // for the key signature (all concert-pitch staves share the same key sig).
    // If staff 0 is excluded or ineligible, find the first eligible one.
    staff_idx_t refStaff = 0;
    for (size_t si = 0; si < score->nstaves(); ++si) {
        if (!excludeStaves.count(si) && staffIsEligible(score, si, startTick)) {
            refStaff = static_cast<staff_idx_t>(si);
            break;
        }
    }

    int keyFifths = 0;
    KeySigMode keyMode = KeySigMode::Ionian;
    double keyConfidence = 0.0;
    resolveKeyAndMode(score, startTick, refStaff, excludeStaves,
                      keyFifths, keyMode, keyConfidence);

    // ── Read analysis preferences ────────────────────────────────────────────
    static muse::GlobalInject<mu::composing::IComposingAnalysisConfiguration> composingConfig;
    const auto* cfg = composingConfig.get().get();
    const bool useRegional = (cfg == nullptr) || cfg->useRegionalAccumulation();

    // Shared helpers used by both code paths.
    const auto chordAnalyzer = ChordAnalyzerFactory::create();
    static constexpr int kMinRegionTicks = Constants::DIVISION;  // 1 quarter note

    // Helper: apply Pass 3 (absorb short regions) to a region list in-place.
    auto absorbShortRegions = [](std::vector<HarmonicRegion>& regions) {
        if (regions.size() <= 1) {
            return;
        }
        std::vector<HarmonicRegion> filtered;
        filtered.push_back(std::move(regions[0]));
        for (size_t i = 1; i < regions.size(); ++i) {
            const int duration = regions[i].endTick - regions[i].startTick;
            if (duration < kMinRegionTicks) {
                filtered.back().endTick = regions[i].endTick;
            } else {
                filtered.push_back(std::move(regions[i]));
            }
        }
        regions = std::move(filtered);
    };

    auto denseBoundaryTicks = [&]() {
        std::vector<Fraction> boundaries;
        boundaries.push_back(startTick);

        uint16_t prevBits = 0;
        bool havePrevious = false;

        for (const Segment* s = seg;
             s && s->tick() < endTick;
             s = s->next1(SegmentType::ChordRest)) {
            std::vector<SoundingNote> sounding;
            collectSoundingAt(score, s, excludeStaves, sounding);
            if (sounding.empty()) {
                continue;
            }

            uint16_t bits = 0;
            for (const SoundingNote& sn : sounding) {
                bits |= static_cast<uint16_t>(1u << (sn.ppitch % 12));
            }

            if (!havePrevious) {
                prevBits = bits;
                havePrevious = true;
                continue;
            }

            if (bits == prevBits) {
                continue;
            }

            boundaries.push_back(s->tick());
            prevBits = bits;
        }

        return boundaries;
    };

    // ── §4.1c regional accumulation path ────────────────────────────────────
    if (useRegional) {
        const double jaccardThreshold = 0.6;  // TODO: read from ChordAnalyzerPreferences
        auto* debugCapture = internal::harmonicRegionDebugCapture();
        std::vector<HarmonicRegion> preMergeRegions;

        // B.4: Pass 1 — detect coarse boundaries via Jaccard on accumulated quarter-note windows.
        auto boundaryTicks = (granularity == HarmonicRegionGranularity::PreserveAllChanges)
            ? denseBoundaryTicks()
            : detectHarmonicBoundariesJaccard(
                score, startTick, endTick, excludeStaves, jaccardThreshold);

        ChordTemporalContext temporalCtx
            = findTemporalContext(score, seg, excludeStaves, keyFifths, keyMode, -1);
        std::optional<KeyModeAnalysisResult> prevKeyResult;

        std::vector<HarmonicRegion> regions;
        regions.reserve(boundaryTicks.size());

        for (size_t i = 0; i < boundaryTicks.size(); ++i) {
            const Fraction regionStart = boundaryTicks[i];
            const Fraction regionEnd   = (i + 1 < boundaryTicks.size())
                                         ? boundaryTicks[i + 1] : endTick;

            // B.3: collect accumulated pitch evidence for this region.
            auto tones = collectRegionTones(score,
                                            regionStart.ticks(),
                                            regionEnd.ticks(),
                                            excludeStaves);
            if (tones.empty()) {
                continue;
            }

            // Update temporal context with this region's bass.
            int currentBassPc = -1;
            for (const auto& t : tones) {
                if (t.isBass) { currentBassPc = t.pitch % 12; break; }
            }
            temporalCtx.bassIsStepwiseFromPrevious =
                (temporalCtx.previousBassPc != -1 && currentBassPc != -1)
                && isDiatonicStep(temporalCtx.previousBassPc, currentBassPc);

            int nextBassPc = -1;
            if (currentBassPc != -1 && i + 1 < boundaryTicks.size()) {
                const Fraction nextRegionStart = boundaryTicks[i + 1];
                const Fraction nextRegionEnd = (i + 2 < boundaryTicks.size())
                                               ? boundaryTicks[i + 2]
                                               : endTick;
                const auto nextTones = collectRegionTones(score,
                                                          nextRegionStart.ticks(),
                                                          nextRegionEnd.ticks(),
                                                          excludeStaves);
                for (const auto& nextTone : nextTones) {
                    if (nextTone.isBass) {
                        nextBassPc = nextTone.pitch % 12;
                        break;
                    }
                }
            }
            temporalCtx.bassIsStepwiseToNext =
                (currentBassPc != -1 && nextBassPc != -1)
                && isDiatonicStep(currentBassPc, nextBassPc);

            int localKeyFifths = keyFifths;
            KeySigMode localKeyMode = keyMode;
            double localKeyConfidence = 0.0;
            double localKeyScore = 0.0;
            resolveKeyAndMode(score, regionStart, refStaff, excludeStaves,
                              localKeyFifths, localKeyMode, localKeyConfidence,
                              prevKeyResult.has_value() ? &prevKeyResult.value() : nullptr,
                              &localKeyScore);

            const auto results = chordAnalyzer->analyzeChord(
                tones, localKeyFifths, localKeyMode, &temporalCtx);

            if (results.empty()) {
                continue;
            }

            ChordAnalysisResult chosenResult = results.front();
            mu::notation::internal::refineSparseChordQualityFromKeyContext(chosenResult,
                                                                           tones,
                                                                           localKeyFifths,
                                                                           localKeyMode);

            temporalCtx.previousRootPc  = chosenResult.identity.rootPc;
            temporalCtx.previousQuality = chosenResult.identity.quality;
            temporalCtx.previousBassPc  = chosenResult.identity.bassPc;

            KeyModeAnalysisResult kmResult;
            kmResult.keySignatureFifths   = localKeyFifths;
            kmResult.mode                 = localKeyMode;
            kmResult.normalizedConfidence = localKeyConfidence;
            kmResult.score                = localKeyScore;
            prevKeyResult = kmResult;

            if (debugCapture && debugCapture->preMergeRegions) {
                HarmonicRegion preMergeRegion;
                preMergeRegion.startTick = regionStart.ticks();
                preMergeRegion.endTick = regionEnd.ticks();
                preMergeRegion.chordResult = chosenResult;
                preMergeRegion.hasAnalyzedChord = true;
                preMergeRegion.keyModeResult = kmResult;
                preMergeRegion.tones = tones;
                preMergeRegions.push_back(std::move(preMergeRegion));
            }

            const bool isContiguousWithPreviousRegion = !regions.empty()
                                                    && regions.back().endTick == regionStart.ticks();

            // Collapse same-chord consecutive regions only when they are truly adjacent.
            // If an unanalyzable sparse slice sits between two matching regions, keep
            // them separate so later notation code can preserve the visible boundary.
            if (isContiguousWithPreviousRegion
                && regions.back().chordResult.identity.rootPc == chosenResult.identity.rootPc
                && regions.back().chordResult.identity.quality == chosenResult.identity.quality) {
                regions.back().endTick = regionEnd.ticks();
                mu::composing::analysis::mergeChordAnalysisTones(regions.back().tones, tones);
                if (const auto* bassTone = mu::composing::analysis::bassToneFromTones(regions.back().tones)) {
                    regions.back().chordResult.identity.bassPc = bassTone->pitch % 12;
                    regions.back().chordResult.identity.bassTpc = bassTone->tpc;
                }
            } else {
                HarmonicRegion region;
                region.startTick     = regionStart.ticks();
                region.endTick       = regionEnd.ticks();
                region.chordResult   = chosenResult;
                region.hasAnalyzedChord = true;
                region.keyModeResult = kmResult;
                region.tones         = std::move(tones);
                regions.push_back(std::move(region));
            }
        }

        // B.4b: Pass 2 post-processing — split large regions with onset-only sub-boundaries.
        // Runs AFTER the main loop so sub-regions inherit the parent key/mode result:
        // only collectRegionTones + analyzeChord are called (cheap), not resolveKeyAndMode.
        if (granularity != HarmonicRegionGranularity::PreserveAllChanges && !regions.empty()) {
            const double onsetThreshold = (cfg != nullptr) ? cfg->onsetBoundaryThreshold() : 0.25;
            // Only split regions wider than one whole note; shorter ones are already
            // fine-grained enough from Pass 1.
            static constexpr int kPass2MinRegionTicks = 4 * Constants::DIVISION;

            std::vector<HarmonicRegion> pass2Regions;
            pass2Regions.reserve(regions.size() * 2);

            for (const HarmonicRegion& parentRegion : regions) {
                const int parentDuration = parentRegion.endTick - parentRegion.startTick;
                if (parentDuration < kPass2MinRegionTicks) {
                    pass2Regions.push_back(parentRegion);
                    continue;
                }

                const Fraction parentStart = Fraction::fromTicks(parentRegion.startTick);
                const Fraction parentEnd   = Fraction::fromTicks(parentRegion.endTick);
                const auto subs = detectOnsetSubBoundaries(
                    score, parentStart, parentEnd, excludeStaves, onsetThreshold);

                if (subs.empty()) {
                    pass2Regions.push_back(parentRegion);
                    continue;
                }

                // Build boundary list: [parentStart, sub1, sub2, ..., parentEnd]
                std::vector<Fraction> subBounds;
                subBounds.reserve(subs.size() + 2);
                subBounds.push_back(parentStart);
                subBounds.insert(subBounds.end(), subs.begin(), subs.end());
                subBounds.push_back(parentEnd);

                // Inherit key/mode from parent — no resolveKeyAndMode call.
                const int subKeyFifths        = parentRegion.keyModeResult.keySignatureFifths;
                const KeySigMode subKeyMode   = parentRegion.keyModeResult.mode;

                // Seed temporal context from the region immediately before this parent.
                ChordTemporalContext subCtx;
                if (!pass2Regions.empty()
                    && pass2Regions.back().endTick == parentRegion.startTick) {
                    subCtx.previousRootPc  = pass2Regions.back().chordResult.identity.rootPc;
                    subCtx.previousQuality = pass2Regions.back().chordResult.identity.quality;
                    subCtx.previousBassPc  = pass2Regions.back().chordResult.identity.bassPc;
                }

                for (size_t si = 0; si + 1 < subBounds.size(); ++si) {
                    const Fraction subStart = subBounds[si];
                    const Fraction subEnd   = subBounds[si + 1];

                    auto subTones = collectRegionTones(
                        score, subStart.ticks(), subEnd.ticks(), excludeStaves);

                    if (subTones.empty()) {
                        // Rest gap: preserve boundary using parent's chord identity.
                        HarmonicRegion gap;
                        gap.startTick        = subStart.ticks();
                        gap.endTick          = subEnd.ticks();
                        gap.chordResult      = parentRegion.chordResult;
                        gap.hasAnalyzedChord = true;
                        gap.keyModeResult    = parentRegion.keyModeResult;
                        pass2Regions.push_back(std::move(gap));
                        continue;
                    }

                    int subBassPc = -1;
                    for (const auto& t : subTones) {
                        if (t.isBass) { subBassPc = t.pitch % 12; break; }
                    }
                    subCtx.bassIsStepwiseFromPrevious =
                        (subCtx.previousBassPc != -1 && subBassPc != -1)
                        && isDiatonicStep(subCtx.previousBassPc, subBassPc);
                    subCtx.bassIsStepwiseToNext = false;  // not computed for sub-regions

                    const auto subResults = chordAnalyzer->analyzeChord(
                        subTones, subKeyFifths, subKeyMode, &subCtx);

                    if (subResults.empty()) {
                        HarmonicRegion fallback;
                        fallback.startTick        = subStart.ticks();
                        fallback.endTick          = subEnd.ticks();
                        fallback.chordResult      = parentRegion.chordResult;
                        fallback.hasAnalyzedChord = true;
                        fallback.keyModeResult    = parentRegion.keyModeResult;
                        fallback.tones            = std::move(subTones);
                        pass2Regions.push_back(std::move(fallback));
                        continue;
                    }

                    ChordAnalysisResult chosenSub = subResults.front();
                    mu::notation::internal::refineSparseChordQualityFromKeyContext(
                        chosenSub, subTones, subKeyFifths, subKeyMode);

                    subCtx.previousRootPc  = chosenSub.identity.rootPc;
                    subCtx.previousQuality = chosenSub.identity.quality;
                    subCtx.previousBassPc  = chosenSub.identity.bassPc;

                    const bool isContiguous = !pass2Regions.empty()
                        && pass2Regions.back().endTick == subStart.ticks();
                    if (isContiguous
                        && pass2Regions.back().chordResult.identity.rootPc == chosenSub.identity.rootPc
                        && pass2Regions.back().chordResult.identity.quality == chosenSub.identity.quality) {
                        pass2Regions.back().endTick = subEnd.ticks();
                        mergeChordAnalysisTones(pass2Regions.back().tones, subTones);
                        if (const auto* bt = bassToneFromTones(pass2Regions.back().tones)) {
                            pass2Regions.back().chordResult.identity.bassPc  = bt->pitch % 12;
                            pass2Regions.back().chordResult.identity.bassTpc = bt->tpc;
                        }
                    } else {
                        HarmonicRegion subRegion;
                        subRegion.startTick        = subStart.ticks();
                        subRegion.endTick          = subEnd.ticks();
                        subRegion.chordResult      = chosenSub;
                        subRegion.hasAnalyzedChord = true;
                        subRegion.keyModeResult    = parentRegion.keyModeResult;
                        subRegion.tones            = std::move(subTones);
                        pass2Regions.push_back(std::move(subRegion));
                    }
                }
            }

            regions = std::move(pass2Regions);
        }

        // Pass 2b: bass-movement sub-boundary detection (iterative).
        // Runs after Pass 2 (onset Jaccard sub-boundaries). Splits regions that
        // still contain a bass PC change (e.g. identical pitch-class sets but
        // different bass notes), as long as the region is >= kPass2bMinRegionTicks.
        // ANY bass PC change fires; downstream bassPassingToneMinWeightFraction
        // suppresses passing tones during chord analysis.
        // Iterates until no new splits are found (up to kMaxBassMovementPasses).
        if (granularity != HarmonicRegionGranularity::PreserveAllChanges && !regions.empty()) {
            static constexpr int kPass2bMinRegionTicks = 4 * Constants::DIVISION;
            static constexpr int kMaxBassMovementPasses = 8;

            bool anyNewSplit = true;
            int passCount = 0;
            while (anyNewSplit && passCount < kMaxBassMovementPasses) {
            anyNewSplit = false;
            ++passCount;

            std::vector<HarmonicRegion> pass2bRegions;
            pass2bRegions.reserve(regions.size() * 2);

            for (const HarmonicRegion& parentRegion : regions) {
                const int parentDuration = parentRegion.endTick - parentRegion.startTick;
                if (parentDuration < kPass2bMinRegionTicks) {
                    pass2bRegions.push_back(parentRegion);
                    continue;
                }

                const Fraction parentStart = Fraction::fromTicks(parentRegion.startTick);
                const Fraction parentEnd   = Fraction::fromTicks(parentRegion.endTick);
                const auto subs = detectBassMovementSubBoundaries(
                    score, parentStart, parentEnd, excludeStaves);

                if (subs.empty()) {
                    pass2bRegions.push_back(parentRegion);
                    continue;
                }

                anyNewSplit = true;

                // Build boundary list: [parentStart, sub1, sub2, ..., parentEnd]
                std::vector<Fraction> bounds;
                bounds.push_back(parentStart);
                for (const Fraction& t : subs) {
                    bounds.push_back(t);
                }
                bounds.push_back(parentEnd);

                // Inherit key/mode from parent — no resolveKeyAndMode call.
                const int subKeyFifths      = parentRegion.keyModeResult.keySignatureFifths;
                const KeySigMode subKeyMode = parentRegion.keyModeResult.mode;

                // Seed temporal context from the region immediately before this parent.
                ChordTemporalContext subCtx;
                if (!pass2bRegions.empty()
                    && pass2bRegions.back().endTick == parentRegion.startTick) {
                    subCtx.previousRootPc  = pass2bRegions.back().chordResult.identity.rootPc;
                    subCtx.previousQuality = pass2bRegions.back().chordResult.identity.quality;
                    subCtx.previousBassPc  = pass2bRegions.back().chordResult.identity.bassPc;
                }

                for (size_t bi = 0; bi + 1 < bounds.size(); ++bi) {
                    const Fraction subStart = bounds[bi];
                    const Fraction subEnd   = bounds[bi + 1];

                    auto subTones = collectRegionTones(
                        score, subStart.ticks(), subEnd.ticks(), excludeStaves);

                    if (subTones.empty()) {
                        HarmonicRegion subRegion;
                        subRegion.startTick        = subStart.ticks();
                        subRegion.endTick          = subEnd.ticks();
                        subRegion.chordResult      = parentRegion.chordResult;
                        subRegion.hasAnalyzedChord = parentRegion.hasAnalyzedChord;
                        subRegion.keyModeResult    = parentRegion.keyModeResult;
                        pass2bRegions.push_back(std::move(subRegion));
                        continue;
                    }

                    int subBassPc = -1;
                    for (const auto& t : subTones) {
                        if (t.isBass) { subBassPc = t.pitch % 12; break; }
                    }
                    subCtx.bassIsStepwiseFromPrevious =
                        (subCtx.previousBassPc != -1 && subBassPc != -1)
                        && isDiatonicStep(subCtx.previousBassPc, subBassPc);
                    subCtx.bassIsStepwiseToNext = false;

                    const auto subResults = chordAnalyzer->analyzeChord(
                        subTones, subKeyFifths, subKeyMode, &subCtx);

                    if (subResults.empty()) {
                        HarmonicRegion subRegion;
                        subRegion.startTick        = subStart.ticks();
                        subRegion.endTick          = subEnd.ticks();
                        subRegion.chordResult      = parentRegion.chordResult;
                        subRegion.hasAnalyzedChord = parentRegion.hasAnalyzedChord;
                        subRegion.keyModeResult    = parentRegion.keyModeResult;
                        subRegion.tones            = std::move(subTones);
                        pass2bRegions.push_back(std::move(subRegion));
                        continue;
                    }

                    ChordAnalysisResult chosenSub = subResults.front();
                    mu::notation::internal::refineSparseChordQualityFromKeyContext(
                        chosenSub, subTones, subKeyFifths, subKeyMode);

                    subCtx.previousRootPc  = chosenSub.identity.rootPc;
                    subCtx.previousQuality = chosenSub.identity.quality;
                    subCtx.previousBassPc  = chosenSub.identity.bassPc;

                    HarmonicRegion subRegion;
                    subRegion.startTick        = subStart.ticks();
                    subRegion.endTick          = subEnd.ticks();
                    subRegion.chordResult      = chosenSub;
                    subRegion.hasAnalyzedChord = true;
                    subRegion.keyModeResult    = parentRegion.keyModeResult;
                    subRegion.tones            = std::move(subTones);
                    pass2bRegions.push_back(std::move(subRegion));
                }
            }

            regions = std::move(pass2bRegions);
            } // end while (anyNewSplit && passCount < kMaxBassMovementPasses)
        }

        if (regions.empty()) {
            return {};
        }

        // Pass 3: absorb regions shorter than 1 quarter note.
        if (granularity == HarmonicRegionGranularity::Smoothed) {
            absorbShortRegions(regions);
        }

        backfillNextRootPc(regions);

        if (debugCapture) {
            if (debugCapture->preMergeRegions) {
                *debugCapture->preMergeRegions = std::move(preMergeRegions);
            }
            if (debugCapture->postMergeRegions) {
                *debugCapture->postMergeRegions = regions;
            }
        }

        return regions;
    }

    // ── Legacy per-tick bitset path ──────────────────────────────────────────
    // Detect boundaries whenever the sounding pitch-class set changes.

    struct BoundaryAnalysis {
        Fraction tick;
        ChordAnalysisResult chordResult;
        KeyModeAnalysisResult keyModeResult;
        std::vector<ChordAnalysisTone> tones;
    };

    std::vector<BoundaryAnalysis> boundaries;
    auto* debugCapture = internal::harmonicRegionDebugCapture();

    auto pcBitset = [](const std::vector<ChordAnalysisTone>& tones) -> uint16_t {
        uint16_t bits = 0;
        for (const auto& t : tones) {
            bits |= static_cast<uint16_t>(1u << (t.pitch % 12));
        }
        return bits;
    };

    uint16_t prevBits = 0;
    // currentBassPc for the very first chord is unknown at this point (sounding
    // not yet collected); pass -1 so bassIsStepwiseFromPrevious stays false.
    ChordTemporalContext temporalCtx
        = findTemporalContext(score, seg, excludeStaves, keyFifths, keyMode, -1);

    std::optional<KeyModeAnalysisResult> prevKeyResult;

    for (const Segment* s = seg;
         s && s->tick() < endTick;
         s = s->next1(SegmentType::ChordRest)) {

        std::vector<SoundingNote> sounding;
        collectSoundingAt(score, s, excludeStaves, sounding);
        if (sounding.empty()) {
            continue;
        }

        auto tones = buildTones(sounding);
        const uint16_t bits = pcBitset(tones);

        if (bits == prevBits && !boundaries.empty()) {
            continue;  // same pitch-class set — same region
        }
        prevBits = bits;

        // Derive current bass pc from the lowest tone (§4.1b stepwise detection).
        int currentBassPc = -1;
        for (const auto& t : tones) {
            if (t.isBass) { currentBassPc = t.pitch % 12; break; }
        }
        temporalCtx.bassIsStepwiseFromPrevious =
            (temporalCtx.previousBassPc != -1 && currentBassPc != -1)
            && isDiatonicStep(temporalCtx.previousBassPc, currentBassPc);

        int localKeyFifths = keyFifths;
        KeySigMode localKeyMode = keyMode;
        double localKeyConfidence = 0.0;
        double localKeyScore = 0.0;
        resolveKeyAndMode(score, s->tick(), refStaff, excludeStaves,
                          localKeyFifths, localKeyMode, localKeyConfidence,
                          prevKeyResult.has_value() ? &prevKeyResult.value() : nullptr,
                          &localKeyScore);

        const auto results = chordAnalyzer->analyzeChord(
            tones, localKeyFifths, localKeyMode, &temporalCtx);

        if (results.empty()) {
            continue;
        }

        const ChordAnalysisResult& chosenResult = results.front();

        temporalCtx.previousRootPc  = chosenResult.identity.rootPc;
        temporalCtx.previousQuality = chosenResult.identity.quality;
        temporalCtx.previousBassPc  = chosenResult.identity.bassPc;
        // nextRootPc, nextBassPc, bassIsStepwiseToNext: populated in
        // two-pass chord staff analysis only. Deferred — see §4.1b.

        KeyModeAnalysisResult kmResult;
        kmResult.keySignatureFifths   = localKeyFifths;
        kmResult.mode                 = localKeyMode;
        kmResult.normalizedConfidence = localKeyConfidence;
        kmResult.score                = localKeyScore;

        prevKeyResult = kmResult;

        boundaries.push_back({ s->tick(), chosenResult, kmResult,
                               std::move(tones) });
    }

    if (boundaries.empty()) {
        return {};
    }

    std::vector<HarmonicRegion> preMergeRegions;
    if (debugCapture && debugCapture->preMergeRegions) {
        preMergeRegions.reserve(boundaries.size());
        for (size_t i = 0; i < boundaries.size(); ++i) {
            const Fraction regionEnd = (i + 1 < boundaries.size())
                                       ? boundaries[i + 1].tick
                                       : endTick;
            HarmonicRegion region;
            region.startTick = boundaries[i].tick.ticks();
            region.endTick = regionEnd.ticks();
            region.chordResult = boundaries[i].chordResult;
            region.hasAnalyzedChord = true;
            region.keyModeResult = boundaries[i].keyModeResult;
            region.tones = boundaries[i].tones;
            preMergeRegions.push_back(std::move(region));
        }
    }

    // ── Pass 2: build regions and collapse same-chord neighbors ──────────────
    std::vector<HarmonicRegion> regions;
    regions.reserve(boundaries.size());

    for (size_t i = 0; i < boundaries.size(); ++i) {
        const Fraction regionEnd = (i + 1 < boundaries.size())
                                   ? boundaries[i + 1].tick
                                   : endTick;

        if (!regions.empty()
            && regions.back().chordResult.identity.rootPc == boundaries[i].chordResult.identity.rootPc
            && regions.back().chordResult.identity.quality == boundaries[i].chordResult.identity.quality) {
            regions.back().endTick = regionEnd.ticks();
            mu::composing::analysis::mergeChordAnalysisTones(regions.back().tones, boundaries[i].tones);
            if (const auto* bassTone = mu::composing::analysis::bassToneFromTones(regions.back().tones)) {
                regions.back().chordResult.identity.bassPc = bassTone->pitch % 12;
                regions.back().chordResult.identity.bassTpc = bassTone->tpc;
            }
            continue;
        }

        HarmonicRegion region;
        region.startTick    = boundaries[i].tick.ticks();
        region.endTick      = regionEnd.ticks();
        region.chordResult  = boundaries[i].chordResult;
        region.hasAnalyzedChord = true;
        region.keyModeResult = boundaries[i].keyModeResult;
        region.tones        = std::move(boundaries[i].tones);
        regions.push_back(std::move(region));
    }

    // ── Pass 3: absorb short regions (passing tones, ornaments) ──────────────
    if (granularity == HarmonicRegionGranularity::Smoothed) {
        absorbShortRegions(regions);
    }

    backfillNextRootPc(regions);

    if (debugCapture) {
        if (debugCapture->preMergeRegions) {
            *debugCapture->preMergeRegions = std::move(preMergeRegions);
        }
        if (debugCapture->postMergeRegions) {
            *debugCapture->postMergeRegions = regions;
        }
    }

    return regions;
}

} // namespace mu::notation
