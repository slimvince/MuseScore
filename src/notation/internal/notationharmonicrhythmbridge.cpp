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

using mu::notation::internal::staffIsEligible;
using mu::notation::internal::SoundingNote;
using mu::notation::internal::collectSoundingAt;
using mu::notation::internal::buildTones;
using mu::notation::internal::resolveKeyAndMode;
using mu::notation::internal::findTemporalContext;
using mu::notation::internal::isDiatonicStep;
using mu::notation::internal::distinctPitchClasses;

namespace mu::notation {

std::vector<mu::composing::analysis::HarmonicRegion> analyzeHarmonicRhythm(
    const mu::engraving::Score* score,
    const mu::engraving::Fraction& startTick,
    const mu::engraving::Fraction& endTick,
    const std::set<size_t>& excludeStaves)
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

    // ── Pass 1: detect boundaries and analyze ────────────────────────────────
    // At each ChordRest segment, collect the sounding pitch-class set (as a
    // 12-bit bitset).  When it differs from the previous set, we have a new
    // harmonic boundary.  Run chord analysis at each boundary.

    struct BoundaryAnalysis {
        Fraction tick;
        ChordAnalysisResult chordResult;
        KeyModeAnalysisResult keyModeResult;
        std::vector<ChordAnalysisTone> tones;
    };

    std::vector<BoundaryAnalysis> boundaries;

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
    const auto chordAnalyzer = ChordAnalyzerFactory::create();

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
            continue;  // < 3 distinct pitch classes — skip
        }

        temporalCtx.previousRootPc  = results.front().identity.rootPc;
        temporalCtx.previousQuality = results.front().identity.quality;
        temporalCtx.previousBassPc  = results.front().identity.bassPc;
        // nextRootPc, nextBassPc, bassIsStepwiseToNext: populated in
        // two-pass chord staff analysis only. Deferred — see §4.1b.

        KeyModeAnalysisResult kmResult;
        kmResult.keySignatureFifths   = localKeyFifths;
        kmResult.mode                 = localKeyMode;
        kmResult.normalizedConfidence = localKeyConfidence;
        kmResult.score                = localKeyScore;

        prevKeyResult = kmResult;

        boundaries.push_back({ s->tick(), results.front(), kmResult,
                               std::move(tones) });
    }

    if (boundaries.empty()) {
        return {};
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
            continue;
        }

        HarmonicRegion region;
        region.startTick    = boundaries[i].tick.ticks();
        region.endTick      = regionEnd.ticks();
        region.chordResult  = boundaries[i].chordResult;
        region.keyModeResult = boundaries[i].keyModeResult;
        region.tones        = std::move(boundaries[i].tones);
        regions.push_back(std::move(region));
    }

    // ── Pass 3: absorb short regions (passing tones, ornaments) ──────────────
    static constexpr int kMinRegionTicks = Constants::DIVISION;  // 1 quarter note

    if (regions.size() > 1) {
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

    return regions;
}

} // namespace mu::notation
