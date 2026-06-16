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

// ── Cadence and pivot detection ───────────────────────────────────────────────

bool hasAssertiveKeyConfidence(
    const mu::composing::analysis::KeyModeAnalysisResult& kmr)
{
    return kmr.normalizedConfidence >= kAnnotateKeyConfidenceThreshold;
}

std::vector<CadenceMarker> detectCadences(
    const std::vector<mu::composing::analysis::AnalyzedRegion>& regions,
    size_t selectionCount)
{
    using namespace mu::composing::analysis;

    std::vector<CadenceMarker> markers;

    const size_t total = regions.size();
    if (total == 0 || selectionCount == 0) {
        return markers;
    }

    // Clamp: selectionCount may equal total (no lookahead), that is fine.
    const size_t n = std::min(selectionCount, total);

    // ── PAC / PC / DC ───────────────────────────────────────────────────────
    // Examine consecutive pairs (i, i+1) where i is inside the selection.
    for (size_t i = 0; i + 1 < total && i < n; ++i) {
        if (!hasAssertiveKeyConfidence(regions[i].keyModeResult)
            || !hasAssertiveKeyConfidence(regions[i + 1].keyModeResult)) {
            continue;
        }

        const auto& a = regions[i].chordResult;
        const auto& b = regions[i + 1].chordResult;

        // Cadence requires same key / mode context.
        if (regions[i].keyModeResult.keySignatureFifths
            != regions[i + 1].keyModeResult.keySignatureFifths
            || regions[i].keyModeResult.mode
               != regions[i + 1].keyModeResult.mode) {
            continue;  // key change — not a cadence
        }
        // And different chord roots.
        if (a.identity.rootPc == b.identity.rootPc) {
            continue;
        }

        const char* label = nullptr;

        // PAC: V → I (non-minor dominant) or viio → I (leading-tone diminished).
        if (b.function.degree == 0
            && ((a.function.degree == 4 && a.identity.quality != ChordQuality::Minor)
                || (a.function.degree == 6 && a.identity.quality == ChordQuality::Diminished))) {
            label = "PAC";
        } else if (a.function.degree == 3 && b.function.degree == 0) {
            label = "PC";   // Plagal: IV → I
        } else if (a.function.degree == 4 && b.function.degree == 5
                   && a.identity.quality != ChordQuality::Minor
                   && b.identity.quality == ChordQuality::Minor) {
            label = "DC";   // Deceptive: V → vi
        }

        if (!label) {
            continue;
        }

        // Place the label at the resolution chord tick (b / regions[i+1]).
        // If that chord is in the lookahead region (outside the selection)
        // place it at the preparatory chord instead so the annotation stays
        // within the selection boundary.
        const int writeTick = (i + 1 < n)
            ? regions[i + 1].startTick
            : regions[i].startTick;

        markers.push_back({ writeTick, std::string(label) });
    }

    // ── Half cadence ────────────────────────────────────────────────────────
    // Last in-selection region is degree 4 (dominant arrival).
    if (hasAssertiveKeyConfidence(regions[n - 1].keyModeResult)
        && regions[n - 1].chordResult.function.degree == 4) {
        const int hcTick = regions[n - 1].startTick;
        // Do not emit HC if another cadence label already occupies this tick.
        const bool alreadyLabelled = std::any_of(markers.begin(), markers.end(),
            [hcTick](const CadenceMarker& m) { return m.tick == hcTick; });
        if (!alreadyLabelled) {
            markers.push_back({ hcTick, "HC" });
        }
    }

    return markers;
}

std::vector<PivotLabel> detectPivotChords(
    const std::vector<mu::composing::analysis::AnalyzedRegion>& regions,
    size_t selectionCount)
{
    using namespace mu::composing::analysis;

    std::vector<PivotLabel> labels;

    if (regions.empty() || selectionCount == 0) {
        return labels;
    }

    const size_t total = regions.size();
    const size_t n = std::min(selectionCount, total);

    // Walk all regions (including lookahead) to find assertive key transitions.
    // A transition occurs when consecutive assertive regions disagree on key/mode.
    struct KeyTransition {
        size_t boundaryIdx;  // index of first region in the new (incoming) key
        int oldFifths;
        KeySigMode oldMode;
        int newFifths;
        KeySigMode newMode;
    };

    std::vector<KeyTransition> transitions;
    int prevFifths  = std::numeric_limits<int>::min();
    KeySigMode prevMode = KeySigMode::Ionian;

    for (size_t i = 0; i < total; ++i) {
        const auto& km = regions[i].keyModeResult;
        if (!hasAssertiveKeyConfidence(km)) {
            continue;
        }
        if (prevFifths == std::numeric_limits<int>::min()) {
            // First assertive region establishes the baseline key.
            prevFifths = km.keySignatureFifths;
            prevMode   = km.mode;
            continue;
        }
        if (km.keySignatureFifths != prevFifths || km.mode != prevMode) {
            // Key has changed — record the transition.
            transitions.push_back({ i, prevFifths, prevMode,
                                     km.keySignatureFifths, km.mode });
            prevFifths = km.keySignatureFifths;
            prevMode   = km.mode;
        }
    }

    for (const auto& tr : transitions) {
        // Confirm that the new key is stable by finding at least one more
        // assertive region beyond the boundary that agrees with it.
        // Limit the search to kMaxPivotLookaheadRegions past the boundary.
        bool confirmed = false;
        const size_t searchEnd = std::min(tr.boundaryIdx + 1
                                          + static_cast<size_t>(kMaxPivotLookaheadRegions),
                                          total);
        for (size_t k = tr.boundaryIdx + 1; k < searchEnd; ++k) {
            const auto& km = regions[k].keyModeResult;
            if (hasAssertiveKeyConfidence(km)
                && km.keySignatureFifths == tr.newFifths
                && km.mode == tr.newMode) {
                confirmed = true;
                break;
            }
        }
        if (!confirmed) {
            continue;  // new key not confirmed — suppress pivot to avoid false positive
        }

        // Build the incoming key's tonic pitch class (still needed for keyTonicPc).
        const int newIonianPc = ionianTonicPcFromFifths(tr.newFifths);
        const int newTonicPc  = (newIonianPc + keyModeTonicOffset(tr.newMode)) % 12;

        // Walk backward from the boundary through the in-selection regions,
        // looking for the first chord that is:
        //   (a) diatonic to the outgoing key  (function.degree >= 0), AND
        //   (b) its root pitch class is in the incoming key's scale.
        const size_t searchBack = std::min(tr.boundaryIdx, n);  // stay in selection
        for (size_t j = searchBack; j > 0; --j) {
            const size_t idx = j - 1;
            const auto& prev = regions[idx].chordResult;

            if (prev.function.degree < 0) {
                continue;  // not diatonic to outgoing key
            }
            if (cra::diatonicDegreeForRootPc(prev.identity.rootPc, tr.newFifths, tr.newMode) < 0) {
                continue;  // root not in incoming scale
            }

            // Found the pivot chord.  Format in both keys.
            const std::string oldRoman = ChordSymbolFormatter::formatRomanNumeral(prev);

            // Compute the degree in the incoming key.
            ChordAnalysisResult pivotInNew = prev;
            pivotInNew.function.degree = cra::diatonicDegreeForRootPc(
                prev.identity.rootPc, tr.newFifths, tr.newMode);
            pivotInNew.function.diatonicToKey = (pivotInNew.function.degree >= 0);
            pivotInNew.function.keyTonicPc = newTonicPc;
            pivotInNew.function.keyMode    = tr.newMode;
            const std::string newRoman = ChordSymbolFormatter::formatRomanNumeral(pivotInNew);

            if (!oldRoman.empty() && !newRoman.empty()) {
                // U+2192 RIGHT ARROW — pivot chord separator (same encoding
                // used in the chord staff path).
                labels.push_back({ regions[idx].startTick,
                                   oldRoman + " \u2192 " + newRoman });
            }
            break;  // one pivot per key transition
        }
    }

    return labels;
}

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

        const auto gapTones = ebr::collectRegionTones(sc,
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
                    openingRegion.tones = ebr::collectRegionTones(sc,
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
            displayRegion.tones = ebr::collectRegionTones(sc,
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
            carriedMeasureOpening.tones = ebr::collectRegionTones(sc,
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

    // Post-stabilization: set hasAssertiveExposure on each display region.
    for (auto& r : displayRegions) {
        r.hasAssertiveExposure = hasAssertiveKeyConfidence(r.keyModeResult);
    }

    out.regions = std::move(displayRegions);

    // Key-areas: confidence-gated grouping per docs/unified_analysis_pipeline.md:149-163.
    //
    // A new KeyArea opens at the first region, then only when:
    //   (a) the region's (keyFifths, mode) differs from the enclosing area, AND
    //   (b) the region's normalizedConfidence >= kAnnotateKeyConfidenceThreshold (0.8).
    //
    // Regions that disagree with the enclosing area but fall below the threshold
    // are silently grouped into the enclosing area (keyAreaId unchanged).
    // Their own keyModeResult is preserved verbatim — status-bar display remains
    // accurate; only the keyAreaId annotation grouping is affected.
    for (size_t i = 0; i < out.regions.size(); ++i) {
        const AnalyzedRegion& region = out.regions[i];
        const int regionFifths = region.keyModeResult.keySignatureFifths;
        const KeySigMode regionMode = region.keyModeResult.mode;
        const double regionConfidence = region.keyModeResult.normalizedConfidence;

        const bool diverges = !out.keyAreas.empty()
            && (out.keyAreas.back().keyFifths != regionFifths
                || out.keyAreas.back().mode != regionMode);

        if (out.keyAreas.empty()
            || (diverges && regionConfidence >= kAnnotateKeyConfidenceThreshold)) {
            KeyArea area;
            area.startTick  = region.startTick;
            area.endTick    = region.endTick;
            area.keyFifths  = regionFifths;
            area.mode       = regionMode;
            area.confidence = regionConfidence;
            out.keyAreas.push_back(area);
        } else {
            KeyArea& back = out.keyAreas.back();
            back.endTick = region.endTick;
            if (regionConfidence > back.confidence) {
                back.confidence = regionConfidence;
            }
        }
        out.regions[i].keyAreaId = static_cast<int>(out.keyAreas.size()) - 1;
    }

    return out;
}

} // namespace mu::composing::analysis
