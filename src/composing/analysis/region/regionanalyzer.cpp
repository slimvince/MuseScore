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

#include "regionanalyzer.h"

#include <algorithm>
#include <array>
#include <optional>
#include <utility>

#include "engraving/dom/chord.h"
#include "engraving/dom/masterscore.h"
#include "engraving/dom/measure.h"
#include "engraving/dom/segment.h"
#include "engraving/dom/staff.h"
#include "engraving/types/constants.h"

#include "composing/analysis/chord/analysisutils.h"
#include "composing/analysis/chord/chordanalyzer.h"
#include "composing/analysis/engravingbridge/regiontonecollector.h"
#include "composing/analysis/harmony/harmonicsegmenter.h"
#include "composing/analysis/key/keyresolver.h"
#include "composing/analysis/region/sparsechordrefinement.h"
#include "composing/analysis/scoreharvest/metricweights.h"

namespace ebr = mu::composing::analysis::engravingbridge;
namespace kr  = mu::composing::analysis::keyresolver;
namespace shv = mu::composing::analysis::scoreharvest;

namespace mu::composing::analysis::region {

namespace {

constexpr int kPass2MinRegionTicks    = 4 * mu::engraving::Constants::DIVISION;
constexpr int kMaxBassMovementPasses  = 8;

/// Pass 3 — absorb every region shorter than kMinRegionTicks into the previous
/// region, regardless of root. Greedy-expand routinely emits sub-beat slices on
/// passing tones and embellishments; analyzed in isolation they produce exotic
/// low-confidence readings (sus / add11 / non-root-bass dim) that are not real
/// harmonic changes. Merging them back into the host chord keeps the region
/// stream at chord-rhythm granularity (the granularity DCML/music21 annotate
/// at). A long genuine intervening harmony survives because it clears the
/// duration threshold; a short different-rooted slice does not.
void absorbShortRegions(std::vector<HarmonicRegion>& regions)
{
    if (regions.size() <= 1) {
        return;
    }
    constexpr int kMinRegionTicks = shv::kMinRegionTicks;
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
}

/// Populate nextRootPc in each region's ChordFunction so that
/// ChordSymbolFormatter::formatRomanNumeral() can emit V/x and vii°/x labels.
/// Called after all merge/absorb passes, before returning the regions vector.
void backfillNextRootPc(std::vector<HarmonicRegion>& regions)
{
    for (size_t i = 0; i + 1 < regions.size(); ++i) {
        regions[i].chordResult.function.nextRootPc
            = regions[i + 1].chordResult.identity.rootPc;
    }
    // The last region has no successor — nextRootPc remains -1.
}

/// Iter 87 — post-merge bass-b7 promotion. The same-root same-quality merge in
/// the main loop keeps the earlier sub-region's chord identity but updates
/// bassPc/bassTpc. When a late-entering b7 in the bass promotes a later
/// sub-region to MinorSeventh (Iter 86 stamp inside analyzeChord), the merge
/// discards that candidate identity in favour of the earlier sub-region's
/// plain triad reading. Re-apply the b7 promotion on the merged region using
/// the merged tones and final bass so the chord symbol (Am7/G, Em7/D)
/// reflects the slash bass that the analyzer already emits via formatSymbol.
///
/// This used to live in tools/batch_analyze.cpp only (the bridge relied on
/// Iter 86's intra-call stamp surviving the merge). Phase 4 moves it inside
/// the shared orchestrator so both paths get the same post-merge guarantee.
void restampBassMinorSeventhAfterMerge(
    std::vector<HarmonicRegion>& regions,
    const ChordAnalyzerPreferences& prefs)
{
    for (HarmonicRegion& r : regions) {
        if (!r.hasAnalyzedChord) { continue; }
        const int rPc = r.chordResult.identity.rootPc;
        const int bPc = r.chordResult.identity.bassPc;
        if (bPc < 0 || bPc == rPc) { continue; }
        if (((bPc - rPc + 12) % 12) != 10) { continue; }
        const ChordQuality q = r.chordResult.identity.quality;
        if (q != ChordQuality::Major && q != ChordQuality::Minor) { continue; }
        if (hasExtension(r.chordResult.identity.extensions, Extension::MinorSeventh)) { continue; }
        if (hasExtension(r.chordResult.identity.extensions, Extension::MajorSeventh)) { continue; }

        double bassPcWeight = 0.0;
        for (const auto& t : r.tones) {
            const int tonePc = ((t.pitch % 12) + 12) % 12;
            if (tonePc == bPc) {
                bassPcWeight += std::max(0.1, t.weight);
            }
        }
        if (bassPcWeight > prefs.extensionThreshold) {
            setExtension(r.chordResult.identity.extensions, Extension::MinorSeventh);
        }
    }
}

/// Dense-boundary detector for PreserveAllChanges granularity. Emits a
/// boundary every time the pitch-class set changes between adjacent ChordRest
/// segments.
std::vector<mu::engraving::Fraction> denseBoundaryTicks(
    const mu::engraving::Score* score,
    const mu::engraving::Segment* firstSeg,
    const mu::engraving::Fraction& startTick,
    const mu::engraving::Fraction& endTick,
    const std::set<size_t>& excludeStaves)
{
    using namespace mu::engraving;
    std::vector<Fraction> boundaries;
    boundaries.push_back(startTick);

    uint16_t prevBits = 0;
    bool havePrevious = false;

    for (const Segment* s = firstSeg; s && s->tick() < endTick;
         s = s->next1(SegmentType::ChordRest)) {
        std::vector<ebr::SoundingNote> sounding;
        ebr::collectSoundingAt(score, s, excludeStaves, sounding);
        if (sounding.empty()) {
            continue;
        }
        uint16_t bits = 0;
        for (const ebr::SoundingNote& sn : sounding) {
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
}

} // anonymous namespace

std::vector<HarmonicRegion>
analyzeRegions(const mu::engraving::Score* score,
               const mu::engraving::Fraction& startTick,
               const mu::engraving::Fraction& endTick,
               const std::set<size_t>& excludeStaves,
               const ChordAnalyzerPreferences& prefs,
               const KeyModeAnalyzerPreferences& keyPrefs,
               const AnalyzeRegionsOptions& opts)
{
    using namespace mu::engraving;

    if (!score || endTick <= startTick) {
        return {};
    }

    // Find the first ChordRest segment at or after startTick.
    const Segment* seg = score->tick2segment(startTick, true, SegmentType::ChordRest);
    if (!seg) {
        return {};
    }

    // Resolve key/mode at the start of the range. Use staff 0 as the reference
    // for the key signature (all concert-pitch staves share the same key sig).
    // If staff 0 is excluded or ineligible, find the first eligible one.
    staff_idx_t refStaff = 0;
    for (size_t si = 0; si < score->nstaves(); ++si) {
        if (!excludeStaves.count(si) && ebr::staffIsEligible(score, si, startTick)) {
            refStaff = static_cast<staff_idx_t>(si);
            break;
        }
    }

    const auto initialRanked = kr::resolveKeyAndModeRanked(
        score, startTick, refStaff, excludeStaves, keyPrefs, nullptr);
    int keyFifths = initialRanked.front().keySignatureFifths;
    KeySigMode keyMode = initialRanked.front().mode;

    // Pass 1 chord-analyzer preferences. Bridge supplies pass1MinDistinctPcsForCandidate=1
    // (Iter 75 sparse-texture admission); batch leaves it at -1 (use the
    // caller's prefs.minDistinctPcsForCandidate unchanged).
    ChordAnalyzerPreferences pass1Prefs = prefs;
    if (opts.pass1MinDistinctPcsForCandidate >= 0) {
        pass1Prefs.minDistinctPcsForCandidate = opts.pass1MinDistinctPcsForCandidate;
    }

    const auto chordAnalyzer = ChordAnalyzerFactory::create();

    std::vector<HarmonicRegion> preMergeRegions;

    // ── Pass 1 — coarse boundary detection ───────────────────────────────────
    std::vector<Fraction> boundaryTicks;
    if (opts.granularity == HarmonicRegionGranularity::PreserveAllChanges) {
        boundaryTicks = denseBoundaryTicks(score, seg, startTick, endTick, excludeStaves);
    } else {
        mu::composing::HarmonicSegmenterCallbacks segCallbacks;
        segCallbacks.staffIsEligible = [&](size_t s) {
            return ebr::staffIsEligible(score, s, startTick);
        };
        const bool excludeLookAhead = opts.excludeLookAheadOnDenseStart;
        segCallbacks.collectRegionTones = [score, &excludeStaves, excludeLookAhead](int s, int e) {
            return ebr::collectRegionTones(score, s, e, excludeStaves, -1, excludeLookAhead);
        };
        const auto placedRegions = mu::composing::greedyExpandSegmentation(
            score, startTick, endTick, excludeStaves,
            mu::composing::analysis::kDefaultChordAnalyzerPreferences,
            chordAnalyzer.get(), keyFifths, keyMode, segCallbacks);

        // Iter 77 Fix B — emit both START and END ticks of placed regions so
        // a confident anchor followed by an unplaced gap keeps its own region.
        std::set<int> boundaryTickSet;
        for (const auto& pr : placedRegions) {
            if (pr.round >= 1) {
                boundaryTickSet.insert(pr.startTick);
                boundaryTickSet.insert(pr.endTick);
            }
        }
        for (int t : boundaryTickSet) {
            if (t >= startTick.ticks() && t < endTick.ticks()) {
                boundaryTicks.push_back(Fraction::fromTicks(t));
            }
        }
        if (boundaryTicks.empty()) {
            boundaryTicks.push_back(startTick);
        }
    }

    ChordTemporalContext temporalCtx = ebr::findTemporalContext(
        score, seg, excludeStaves, keyFifths, keyMode, -1);
    std::optional<KeyModeAnalysisResult> prevKeyResult;

    int runningStepwiseCount = 0;
    std::array<int, 3> recentRootsBuf = { -1, -1, -1 };

    std::vector<HarmonicRegion> regions;
    regions.reserve(boundaryTicks.size());

    for (size_t i = 0; i < boundaryTicks.size(); ++i) {
        const Fraction regionStart = boundaryTicks[i];
        const Fraction regionEnd   = (i + 1 < boundaryTicks.size())
                                     ? boundaryTicks[i + 1] : endTick;

        auto tones = ebr::collectRegionTones(
            score, regionStart.ticks(), regionEnd.ticks(), excludeStaves, -1,
            opts.excludeLookAheadOnDenseStart);
        if (tones.empty()) {
            continue;
        }

        int currentBassPc = -1;
        for (const auto& t : tones) {
            if (t.isBass) { currentBassPc = t.pitch % 12; break; }
        }
        temporalCtx.bassIsStepwiseFromPrevious =
            (temporalCtx.previousBassPc != -1 && currentBassPc != -1)
            && isDiatonicStep(temporalCtx.previousBassPc, currentBassPc);

        // Per-region key resolution with hysteresis.
        const auto ranked = kr::resolveKeyAndModeRanked(
            score, regionStart, refStaff, excludeStaves, keyPrefs,
            prevKeyResult.has_value() ? &prevKeyResult.value() : nullptr);
        const KeyModeAnalysisResult localKey = ranked.front();
        const int localKeyFifths = localKey.keySignatureFifths;
        const KeySigMode localKeyMode = localKey.mode;

        // Next-region lookahead (bass + root) for joint scoring.
        int nextBassPc = -1;
        temporalCtx.nextRootPc = -1;
        if (currentBassPc != -1 && i + 1 < boundaryTicks.size()) {
            const Fraction nextRegionStart = boundaryTicks[i + 1];
            const Fraction nextRegionEnd = (i + 2 < boundaryTicks.size())
                                           ? boundaryTicks[i + 2] : endTick;
            const auto nextTones = ebr::collectRegionTones(
                score, nextRegionStart.ticks(), nextRegionEnd.ticks(), excludeStaves, -1,
                opts.excludeLookAheadOnDenseStart);
            for (const auto& nextTone : nextTones) {
                if (nextTone.isBass) { nextBassPc = nextTone.pitch % 12; break; }
            }
            temporalCtx.nextRootPc = inferNextRootPc(
                chordAnalyzer.get(), nextTones, localKeyFifths, localKeyMode);
        }
        temporalCtx.bassIsStepwiseToNext =
            (currentBassPc != -1 && nextBassPc != -1)
            && isDiatonicStep(currentBassPc, nextBassPc);
        temporalCtx.nextBassPc = nextBassPc;

        const Segment* regionStartSeg = score->tick2segment(
            regionStart, false, SegmentType::ChordRest);
        const Measure* currentMeasure = regionStartSeg ? regionStartSeg->measure() : nullptr;
        temporalCtx.regionMetricWeight = shv::regionMetricWeightForBeatType(
            shv::safeBeatType(currentMeasure, regionStartSeg));

        const auto results = chordAnalyzer->analyzeChord(
            tones, localKeyFifths, localKeyMode, &temporalCtx, pass1Prefs);

        if (results.empty()) {
            continue;
        }

        ChordAnalysisResult chosenResult = results.front();
        refineSparseChordQualityFromKeyContext(
            chosenResult, tones, localKeyFifths, localKeyMode);
        applyTonicPriorToSparseChord(
            chosenResult, tones, localKeyFifths, localKeyMode);

        const ChordTemporalExtensions extensionsSnapshot = toExtensionsSnapshot(temporalCtx);
        std::vector<ChordAnalysisResult> alternativesSnapshot;
        if (results.size() > 1) {
            alternativesSnapshot.assign(results.begin() + 1, results.end());
        }

        advanceTemporalContext(temporalCtx, runningStepwiseCount, recentRootsBuf,
                               chosenResult.identity);
        temporalCtx.nextRootPc = -1;
        temporalCtx.nextBassPc = -1;

        prevKeyResult = localKey;

        if (opts.hooks && opts.hooks->preMergeRegions) {
            HarmonicRegion preMergeRegion;
            preMergeRegion.startTick = regionStart.ticks();
            preMergeRegion.endTick = regionEnd.ticks();
            preMergeRegion.chordResult = chosenResult;
            preMergeRegion.alternatives = alternativesSnapshot;
            preMergeRegion.hasAnalyzedChord = true;
            preMergeRegion.keyModeResult = localKey;
            preMergeRegion.tones = tones;
            preMergeRegion.temporalExtensions = extensionsSnapshot;
            preMergeRegions.push_back(std::move(preMergeRegion));
        }

        const bool isContiguousWithPreviousRegion = !regions.empty()
                                                && regions.back().endTick == regionStart.ticks();

        // Collapse same-chord consecutive regions only when truly adjacent.
        if (isContiguousWithPreviousRegion
            && regions.back().chordResult.identity.rootPc == chosenResult.identity.rootPc
            && regions.back().chordResult.identity.quality == chosenResult.identity.quality) {
            regions.back().endTick = regionEnd.ticks();
            mergeChordAnalysisTones(regions.back().tones, tones);
            if (const auto* bassTone = bassToneFromTones(regions.back().tones)) {
                regions.back().chordResult.identity.bassPc = bassTone->pitch % 12;
                regions.back().chordResult.identity.bassTpc = bassTone->tpc;
            }
        } else {
            HarmonicRegion region;
            region.startTick     = regionStart.ticks();
            region.endTick       = regionEnd.ticks();
            region.chordResult   = chosenResult;
            region.alternatives  = std::move(alternativesSnapshot);
            region.hasAnalyzedChord = true;
            region.keyModeResult = localKey;
            region.tones         = std::move(tones);
            region.temporalExtensions = extensionsSnapshot;
            regions.push_back(std::move(region));
        }
    }

    // ── Pass 2 — onset-Jaccard sub-boundary detection ────────────────────────
    if (opts.granularity != HarmonicRegionGranularity::PreserveAllChanges && !regions.empty()) {
        std::vector<HarmonicRegion> pass2Regions;
        pass2Regions.reserve(regions.size() * 2);

        for (size_t parentIdx = 0; parentIdx < regions.size(); ++parentIdx) {
            const HarmonicRegion& parentRegion = regions[parentIdx];
            const int parentDuration = parentRegion.endTick - parentRegion.startTick;
            if (parentDuration < kPass2MinRegionTicks) {
                pass2Regions.push_back(parentRegion);
                continue;
            }

            const Fraction parentStart = Fraction::fromTicks(parentRegion.startTick);
            const Fraction parentEnd   = Fraction::fromTicks(parentRegion.endTick);
            const auto subs = ebr::detectOnsetSubBoundaries(
                score, parentStart, parentEnd, excludeStaves, opts.onsetBoundaryThreshold);

            if (subs.empty()) {
                pass2Regions.push_back(parentRegion);
                continue;
            }

            std::vector<Fraction> subBounds;
            subBounds.reserve(subs.size() + 2);
            subBounds.push_back(parentStart);
            subBounds.insert(subBounds.end(), subs.begin(), subs.end());
            subBounds.push_back(parentEnd);

            const int subKeyFifths      = parentRegion.keyModeResult.keySignatureFifths;
            const KeySigMode subKeyMode = parentRegion.keyModeResult.mode;

            // Iter 94 — parent-scope previousBassPc / nextBassPc.
            const int parentPredBassPc = (parentIdx > 0)
                ? regions[parentIdx - 1].chordResult.identity.bassPc : -1;
            const int parentSuccBassPc = (parentIdx + 1 < regions.size())
                ? regions[parentIdx + 1].chordResult.identity.bassPc : -1;

            ChordTemporalContext subCtx;
            if (!pass2Regions.empty()
                && pass2Regions.back().endTick == parentRegion.startTick) {
                subCtx.previousRootPc  = pass2Regions.back().chordResult.identity.rootPc;
                subCtx.previousQuality = pass2Regions.back().chordResult.identity.quality;
                subCtx.previousBassPc  = pass2Regions.back().chordResult.identity.bassPc;
            }
            subCtx.consecutiveBassStepwiseCount
                = parentRegion.temporalExtensions.consecutiveBassStepwiseCount;
            subCtx.recentRootPcs = parentRegion.temporalExtensions.recentRootPcs;

            for (size_t si = 0; si + 1 < subBounds.size(); ++si) {
                const Fraction subStart = subBounds[si];
                const Fraction subEnd   = subBounds[si + 1];

                // Iter 93 — pass parent.startTick so onsetAtRegionStart is
                // computed at full-region scope.
                auto subTones = ebr::collectRegionTones(
                    score, subStart.ticks(), subEnd.ticks(), excludeStaves,
                    parentRegion.startTick, opts.excludeLookAheadOnDenseStart);

                if (subTones.empty()) {
                    HarmonicRegion gap;
                    gap.startTick        = subStart.ticks();
                    gap.endTick          = subEnd.ticks();
                    gap.chordResult      = parentRegion.chordResult;
                    gap.alternatives     = parentRegion.alternatives;
                    gap.hasAnalyzedChord = true;
                    gap.keyModeResult    = parentRegion.keyModeResult;
                    gap.temporalExtensions = parentRegion.temporalExtensions;
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
                subCtx.bassIsStepwiseToNext = false;
                {
                    const Segment* subSeg = score->tick2segment(
                        subStart, false, SegmentType::ChordRest);
                    subCtx.regionMetricWeight = shv::regionMetricWeightForBeatType(
                        shv::safeBeatType(subSeg ? subSeg->measure() : nullptr, subSeg));
                }

                // Iter 94 — parent-scope override (after stepwise booleans, before analyzeChord).
                subCtx.previousBassPc = parentPredBassPc;
                subCtx.nextBassPc     = parentSuccBassPc;

                // Iter 95 Step 2 (fine-grained) — nextRootPc from the next
                // sub-region's tones within this parent's subBounds; for the
                // last sub of the parent, fall back to the next parent's
                // whole span. Matches the old batch's per-sub lookahead that
                // w_seq / w_dim were tuned against (coarse parent-identity
                // lookup blunted the signal — see Phase 4 prompt).
                {
                    int nextStartT = -1;
                    int nextEndT   = -1;
                    if (si + 2 < subBounds.size()) {
                        nextStartT = subBounds[si + 1].ticks();
                        nextEndT   = subBounds[si + 2].ticks();
                    } else if (parentIdx + 1 < regions.size()) {
                        nextStartT = regions[parentIdx + 1].startTick;
                        nextEndT   = regions[parentIdx + 1].endTick;
                    }
                    int subNextRootPc = -1;
                    if (nextStartT >= 0 && nextEndT > nextStartT) {
                        const auto nextTones = ebr::collectRegionTones(
                            score, nextStartT, nextEndT, excludeStaves, -1,
                            opts.excludeLookAheadOnDenseStart);
                        subNextRootPc = inferNextRootPc(
                            chordAnalyzer.get(), nextTones, subKeyFifths, subKeyMode);
                    }
                    subCtx.nextRootPc = subNextRootPc;
                }

                const auto subResults = chordAnalyzer->analyzeChord(
                    subTones, subKeyFifths, subKeyMode, &subCtx, prefs);

                if (subResults.empty()) {
                    HarmonicRegion fallback;
                    fallback.startTick        = subStart.ticks();
                    fallback.endTick          = subEnd.ticks();
                    fallback.chordResult      = parentRegion.chordResult;
                    fallback.hasAnalyzedChord = true;
                    fallback.keyModeResult    = parentRegion.keyModeResult;
                    fallback.tones            = std::move(subTones);
                    fallback.temporalExtensions = toExtensionsSnapshot(subCtx);
                    pass2Regions.push_back(std::move(fallback));
                    continue;
                }

                ChordAnalysisResult chosenSub = subResults.front();
                refineSparseChordQualityFromKeyContext(
                    chosenSub, subTones, subKeyFifths, subKeyMode);

                const ChordTemporalExtensions subExtSnap = toExtensionsSnapshot(subCtx);
                std::vector<ChordAnalysisResult> subAltsSnap;
                if (subResults.size() > 1) {
                    subAltsSnap.assign(subResults.begin() + 1, subResults.end());
                }

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
                    subRegion.alternatives     = std::move(subAltsSnap);
                    subRegion.hasAnalyzedChord = true;
                    subRegion.keyModeResult    = parentRegion.keyModeResult;
                    subRegion.tones            = std::move(subTones);
                    subRegion.temporalExtensions = subExtSnap;
                    pass2Regions.push_back(std::move(subRegion));
                }
            }
        }

        regions = std::move(pass2Regions);
    }

    // ── Pass 2b — iterative bass-movement sub-boundaries ────────────────────
    if (opts.granularity != HarmonicRegionGranularity::PreserveAllChanges && !regions.empty()) {
        constexpr int kPass2bMinRegionTicks = shv::kPass2bMinRegionTicks;

        bool anyNewSplit = true;
        int passCount = 0;
        while (anyNewSplit && passCount < kMaxBassMovementPasses) {
            anyNewSplit = false;
            ++passCount;

            std::vector<HarmonicRegion> pass2bRegions;
            pass2bRegions.reserve(regions.size() * 2);

            for (size_t parentIdx = 0; parentIdx < regions.size(); ++parentIdx) {
                const HarmonicRegion& parentRegion = regions[parentIdx];
                const int parentDuration = parentRegion.endTick - parentRegion.startTick;
                if (parentDuration < kPass2bMinRegionTicks) {
                    pass2bRegions.push_back(parentRegion);
                    continue;
                }

                const Fraction parentStart = Fraction::fromTicks(parentRegion.startTick);
                const Fraction parentEnd   = Fraction::fromTicks(parentRegion.endTick);
                const auto subs = ebr::detectBassMovementSubBoundaries(
                    score, parentStart, parentEnd, excludeStaves);

                if (subs.empty()) {
                    pass2bRegions.push_back(parentRegion);
                    continue;
                }

                anyNewSplit = true;

                std::vector<Fraction> bounds;
                bounds.push_back(parentStart);
                for (const Fraction& t : subs) {
                    bounds.push_back(t);
                }
                bounds.push_back(parentEnd);

                const int subKeyFifths      = parentRegion.keyModeResult.keySignatureFifths;
                const KeySigMode subKeyMode = parentRegion.keyModeResult.mode;

                const int parentPredBassPc = (parentIdx > 0)
                    ? regions[parentIdx - 1].chordResult.identity.bassPc : -1;
                const int parentSuccBassPc = (parentIdx + 1 < regions.size())
                    ? regions[parentIdx + 1].chordResult.identity.bassPc : -1;

                ChordTemporalContext subCtx;
                if (!pass2bRegions.empty()
                    && pass2bRegions.back().endTick == parentRegion.startTick) {
                    subCtx.previousRootPc  = pass2bRegions.back().chordResult.identity.rootPc;
                    subCtx.previousQuality = pass2bRegions.back().chordResult.identity.quality;
                    subCtx.previousBassPc  = pass2bRegions.back().chordResult.identity.bassPc;
                }
                subCtx.consecutiveBassStepwiseCount
                    = parentRegion.temporalExtensions.consecutiveBassStepwiseCount;
                subCtx.recentRootPcs = parentRegion.temporalExtensions.recentRootPcs;

                for (size_t bi = 0; bi + 1 < bounds.size(); ++bi) {
                    const Fraction subStart = bounds[bi];
                    const Fraction subEnd   = bounds[bi + 1];

                    auto subTones = ebr::collectRegionTones(
                        score, subStart.ticks(), subEnd.ticks(), excludeStaves,
                        parentRegion.startTick, opts.excludeLookAheadOnDenseStart);

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
                    {
                        const Segment* subSeg = score->tick2segment(
                            subStart, false, SegmentType::ChordRest);
                        subCtx.regionMetricWeight = shv::regionMetricWeightForBeatType(
                            shv::safeBeatType(subSeg ? subSeg->measure() : nullptr, subSeg));
                    }

                    subCtx.previousBassPc = parentPredBassPc;
                    subCtx.nextBassPc     = parentSuccBassPc;

                    // Iter 95 Step 2 (fine-grained) — see Pass 2 comment above.
                    {
                        int nextStartT = -1;
                        int nextEndT   = -1;
                        if (bi + 2 < bounds.size()) {
                            nextStartT = bounds[bi + 1].ticks();
                            nextEndT   = bounds[bi + 2].ticks();
                        } else if (parentIdx + 1 < regions.size()) {
                            nextStartT = regions[parentIdx + 1].startTick;
                            nextEndT   = regions[parentIdx + 1].endTick;
                        }
                        int subNextRootPc = -1;
                        if (nextStartT >= 0 && nextEndT > nextStartT) {
                            const auto nextTones = ebr::collectRegionTones(
                                score, nextStartT, nextEndT, excludeStaves, -1,
                                opts.excludeLookAheadOnDenseStart);
                            subNextRootPc = inferNextRootPc(
                                chordAnalyzer.get(), nextTones, subKeyFifths, subKeyMode);
                        }
                        subCtx.nextRootPc = subNextRootPc;
                    }

                    const auto subResults = chordAnalyzer->analyzeChord(
                        subTones, subKeyFifths, subKeyMode, &subCtx, prefs);

                    if (subResults.empty()) {
                        HarmonicRegion subRegion;
                        subRegion.startTick        = subStart.ticks();
                        subRegion.endTick          = subEnd.ticks();
                        subRegion.chordResult      = parentRegion.chordResult;
                        subRegion.alternatives     = parentRegion.alternatives;
                        subRegion.hasAnalyzedChord = parentRegion.hasAnalyzedChord;
                        subRegion.keyModeResult    = parentRegion.keyModeResult;
                        subRegion.tones            = std::move(subTones);
                        subRegion.temporalExtensions = toExtensionsSnapshot(subCtx);
                        pass2bRegions.push_back(std::move(subRegion));
                        continue;
                    }

                    ChordAnalysisResult chosenSub = subResults.front();
                    refineSparseChordQualityFromKeyContext(
                        chosenSub, subTones, subKeyFifths, subKeyMode);

                    const ChordTemporalExtensions subExtSnap = toExtensionsSnapshot(subCtx);
                    std::vector<ChordAnalysisResult> subAltsSnap;
                    if (subResults.size() > 1) {
                        subAltsSnap.assign(subResults.begin() + 1, subResults.end());
                    }

                    subCtx.previousRootPc  = chosenSub.identity.rootPc;
                    subCtx.previousQuality = chosenSub.identity.quality;
                    subCtx.previousBassPc  = chosenSub.identity.bassPc;

                    HarmonicRegion subRegion;
                    subRegion.startTick        = subStart.ticks();
                    subRegion.endTick          = subEnd.ticks();
                    subRegion.chordResult      = chosenSub;
                    subRegion.alternatives     = std::move(subAltsSnap);
                    subRegion.hasAnalyzedChord = true;
                    subRegion.keyModeResult    = parentRegion.keyModeResult;
                    subRegion.tones            = std::move(subTones);
                    subRegion.temporalExtensions = subExtSnap;
                    pass2bRegions.push_back(std::move(subRegion));
                }
            }

            regions = std::move(pass2bRegions);
        } // end while
    }

    if (regions.empty()) {
        return {};
    }

    // ── Pass 3 — absorb short regions ────────────────────────────────────────
    if (opts.granularity == HarmonicRegionGranularity::Smoothed) {
        absorbShortRegions(regions);
    }

    // Iter 87 post-merge MinorSeventh re-stamp (now on both paths).
    restampBassMinorSeventhAfterMerge(regions, prefs);

    // V/x and vii°/x tonicization labels.
    backfillNextRootPc(regions);

    if (opts.hooks) {
        if (opts.hooks->preMergeRegions) {
            *opts.hooks->preMergeRegions = std::move(preMergeRegions);
        }
        if (opts.hooks->postMergeRegions) {
            *opts.hooks->postMergeRegions = regions;
        }
    }

    return regions;
}

} // namespace mu::composing::analysis::region
