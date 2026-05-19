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

#include "keyresolver.h"

#include <algorithm>
#include <optional>

#include "engraving/dom/key.h"
#include "engraving/dom/keysig.h"
#include "engraving/dom/score.h"
#include "engraving/dom/staff.h"
#include "engraving/types/fraction.h"

#include "composing/analysis/chord/analysisutils.h"
#include "composing/analysis/engravingbridge/regiontonecollector.h"
#include "composing/analysis/scoreharvest/metricweights.h"

namespace ebr = mu::composing::analysis::engravingbridge;
namespace shv = mu::composing::analysis::scoreharvest;

namespace mu::composing::analysis::keyresolver {

namespace {

/// Build a single-result vector for the fallback paths. Always returns a
/// vector of size 1 with the canonical "notated key signature, Ionian" or
/// declared-mode reading.
std::vector<KeyModeAnalysisResult> fallbackResult(int keyFifths,
                                                  std::optional<KeySigMode> declaredMode,
                                                  double confidence,
                                                  double score)
{
    KeyModeAnalysisResult fallback;
    fallback.keySignatureFifths   = keyFifths;
    fallback.mode                 = declaredMode.value_or(KeySigMode::Ionian);
    fallback.tonicPc              = (ionianTonicPcFromFifths(keyFifths)
                                     + keyModeTonicOffset(fallback.mode)) % 12;
    fallback.score                = score;
    fallback.normalizedConfidence = confidence;
    return { fallback };
}

/// Reorder `results` so the candidate matching the `chosen` selector is at
/// index 0; preserves the relative order of the remaining candidates.
template<typename Pred>
void promoteWinnerInPlace(std::vector<KeyModeAnalysisResult>& results, Pred chosenPredicate)
{
    auto it = std::find_if(results.begin(), results.end(), chosenPredicate);
    if (it != results.end() && it != results.begin()) {
        // Rotate `it` to the front, keeping the original order of the rest.
        std::rotate(results.begin(), it, it + 1);
    }
}

} // namespace

std::vector<KeyModeAnalysisResult>
resolveKeyAndModeRanked(
    const mu::engraving::Score* sc,
    const mu::engraving::Fraction& tick,
    mu::engraving::staff_idx_t staffIdx,
    const std::set<std::size_t>& excludeStaves,
    const KeyModeAnalyzerPreferences& prefs,
    const KeyModeAnalysisResult* prevResult)
{
    using namespace mu::engraving;

    const std::size_t clampedStaffIdx = std::min<std::size_t>(staffIdx, sc->nstaves() - 1);
    const KeySigEvent keySig = sc->staff(clampedStaffIdx)->keySigEvent(tick);
    const int keyFifths = static_cast<int>(keySig.concertKey());

    // ── Declared mode from key signature ─────────────────────────────────
    std::optional<KeySigMode> declaredMode;
    {
        using EMode = mu::engraving::KeyMode;
        switch (keySig.mode()) {
        case EMode::MAJOR:
        case EMode::IONIAN:      declaredMode = KeySigMode::Ionian;     break;
        case EMode::MINOR:
        case EMode::AEOLIAN:     declaredMode = KeySigMode::Aeolian;    break;
        case EMode::DORIAN:      declaredMode = KeySigMode::Dorian;     break;
        case EMode::PHRYGIAN:    declaredMode = KeySigMode::Phrygian;   break;
        case EMode::LYDIAN:      declaredMode = KeySigMode::Lydian;     break;
        case EMode::MIXOLYDIAN:  declaredMode = KeySigMode::Mixolydian; break;
        case EMode::LOCRIAN:     declaredMode = KeySigMode::Locrian;    break;
        default:                 declaredMode = std::nullopt;           break;
        }
    }

    // ── Fixed lookback window ─────────────────────────────────────────────
    const Fraction lookbackDuration = Fraction(shv::LOOKBACK_BEATS, 4);
    const Fraction windowStart = (tick > lookbackDuration)
                                 ? tick - lookbackDuration
                                 : Fraction(0, 1);

    // ── Piece-start shortcut ──────────────────────────────────────────────
    //
    // No previous region + declared mode + we're inside the lookback window
    // means we have insufficient pitch history to override the composer's
    // declaration. Return a low-confidence anchor so the next region must
    // beat `relativeKeyHysteresisMargin` to switch away from the declared key.
    if (prevResult == nullptr && declaredMode.has_value()
        && windowStart == Fraction(0, 1) && tick < lookbackDuration) {
        KeyModeAnalysisResult decl;
        decl.keySignatureFifths   = keyFifths;
        decl.mode                 = *declaredMode;
        decl.tonicPc              = (ionianTonicPcFromFifths(keyFifths)
                                     + keyModeTonicOffset(*declaredMode)) % 12;
        // The relative-key hysteresis margin is the piece-start anchor score:
        // any analysis window must beat it to override the declared key.
        decl.score                = prefs.relativeKeyHysteresisMargin;
        decl.normalizedConfidence = 0.5;
        return { decl };
    }

    // ── Dynamic lookahead loop ────────────────────────────────────────────
    std::vector<KeyModeAnalyzer::PitchContext> ctx;
    std::vector<KeyModeAnalysisResult> results;

    int lookaheadBeats = shv::LOOKAHEAD_BEATS;
    while (true) {
        ctx.clear();
        const Fraction windowEnd = tick + Fraction(lookaheadBeats, 4);
        ebr::collectPitchContext(sc, tick, windowStart, windowEnd,
                                 excludeStaves, prefs, ctx);

        results = KeyModeAnalyzer::analyzeKeyMode(ctx, keyFifths, prefs, declaredMode);

        const bool confident = !results.empty()
            && results.front().normalizedConfidence
               >= prefs.dynamicLookaheadConfidenceThreshold;
        const bool atMax = lookaheadBeats >= prefs.dynamicLookaheadMaxBeats;
        if (confident || atMax) {
            break;
        }
        lookaheadBeats += prefs.dynamicLookaheadStepBeats;
    }

    // ── Empty / insufficient PCs fallback ─────────────────────────────────
    if (results.empty() || shv::distinctPitchClasses(ctx) < 3) {
        return fallbackResult(keyFifths, declaredMode, 0.0, 0.0);
    }

    // ── Hysteresis ───────────────────────────────────────────────────────
    //
    // If the top result switches mode away from the previous region, require
    // a score margin to commit. Same-key-signature switches (relative major /
    // minor) use a larger margin because the shared diatonic pool makes them
    // structurally ambiguous.
    if (prevResult != nullptr && results.front().mode != prevResult->mode) {
        const double hysteresis = (results.front().keySignatureFifths == prevResult->keySignatureFifths)
                                  ? prefs.relativeKeyHysteresisMargin
                                  : prefs.hysteresisMargin;
        if (results.front().score < prevResult->score + hysteresis) {
            promoteWinnerInPlace(results, [&](const KeyModeAnalysisResult& r) {
                return r.mode == prevResult->mode
                    && r.keySignatureFifths == prevResult->keySignatureFifths;
            });
        }
    }

    // ── Strong declared-mode prior ────────────────────────────────────────
    //
    // When the key signature carries an explicit Mode property, the composer's
    // intent overrides note-content inference. If the chosen winner is
    // incompatible with the declared class (e.g. G# Dorian vs declared
    // F# Major), promote the highest-ranked compatible result.
    if (declaredMode.has_value()) {
        const KeyModeAnalysisResult& top = results.front();
        const bool topIsCompatible = (*declaredMode == KeySigMode::Ionian)
            ? keyModeIsMajor(top.mode)
            : (*declaredMode == KeySigMode::Aeolian)
              ? !keyModeIsMajor(top.mode)
              : (top.mode == *declaredMode);
        if (!topIsCompatible) {
            promoteWinnerInPlace(results, [&](const KeyModeAnalysisResult& r) {
                return (*declaredMode == KeySigMode::Ionian)
                    ? keyModeIsMajor(r.mode)
                    : (*declaredMode == KeySigMode::Aeolian)
                      ? !keyModeIsMajor(r.mode)
                      : (r.mode == *declaredMode);
            });
        }
    }

    return results;
}

} // namespace mu::composing::analysis::keyresolver
