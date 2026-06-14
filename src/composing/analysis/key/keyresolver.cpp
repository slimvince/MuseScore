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
#include <array>
#include <optional>

#include "engraving/dom/chord.h"
#include "engraving/dom/chordrest.h"
#include "engraving/dom/key.h"
#include "engraving/dom/keysig.h"
#include "engraving/dom/measure.h"
#include "engraving/dom/note.h"
#include "engraving/dom/score.h"
#include "engraving/dom/segment.h"
#include "engraving/dom/staff.h"
#include "engraving/types/constants.h"
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

/// Ionian (major-scale) pitch-class membership set for a key-signature value.
std::array<bool, 12> ionianScaleSet(int fifths)
{
    std::array<bool, 12> s{};
    const int tonic = ionianTonicPcFromFifths(fifths);
    for (int interval : { 0, 2, 4, 5, 7, 9, 11 }) {
        s[static_cast<size_t>((tonic + interval) % 12)] = true;
    }
    return s;
}

/// Baroque "partial-signature" (one-accidental-short) detector.
///
/// Late-17th/early-18th-century scores routinely notate a key with one fewer
/// accidental than the modern convention — minor keys with a Dorian signature
/// (the b6 supplied as an accidental) and major keys with a Mixolydian signature
/// (the leading tone supplied as an accidental). See
/// docs/key_detection_baroque_partial_signature.md. The resolver is otherwise
/// locked to the notated signature, so the true tonic — a fifth/fourth away — is
/// unreachable (e.g. Corelli op01n08d, C minor notated with 2 flats, resolves to
/// G minor).
///
/// When the convention is detected this returns the corrected signature, one
/// step toward the declared mode's missing accidental (major → +1 sharp;
/// minor → -1 flat); otherwise it returns @p notatedFifths unchanged.
///
/// Only common-practice major (Ionian) / minor (Aeolian) class declarations are
/// eligible — explicit modal declarations (Dorian, Mixolydian, …) are taken at
/// face value. Moving the signature one step flips exactly one scale degree from
/// natural to accidental ("flipsIn", e.g. A♮→A♭ = the true b6 of C minor) and
/// one the other way ("flipsOut"). The convention is confirmed only when, across
/// the span sharing this signature, the accidental form is genuinely pervasive
/// AND clearly dominates its natural counterpart. Both guards matter: the floor
/// rejects incidental chromaticism; the dominance ratio rejects correctly-notated
/// keys, where the natural degree is guaranteed common (it is the 5th of the
/// dominant / part of the subdominant) and the accidental is the rare Neapolitan
/// or secondary leading tone.
int partialSignatureCorrection(const mu::engraving::Score* sc,
                               std::size_t clampedStaffIdx,
                               const std::set<std::size_t>& excludeStaves,
                               int notatedFifths,
                               KeySigMode declaredClass)
{
    using namespace mu::engraving;

    const bool isMajor = (declaredClass == KeySigMode::Ionian);
    const bool isMinor = (declaredClass == KeySigMode::Aeolian);
    if (!isMajor && !isMinor) {
        return notatedFifths;
    }

    const int neighborFifths = isMajor ? notatedFifths + 1 : notatedFifths - 1;
    if (neighborFifths < -7 || neighborFifths > 7) {
        return notatedFifths;
    }

    const std::array<bool, 12> scaleS = ionianScaleSet(notatedFifths);
    const std::array<bool, 12> scaleN = ionianScaleSet(neighborFifths);
    int flipsIn  = -1;  // in neighbor scale, not notated scale (the accidental)
    int flipsOut = -1;  // in notated scale, not neighbor scale (the natural)
    for (int pc = 0; pc < 12; ++pc) {
        if (scaleN[static_cast<size_t>(pc)] && !scaleS[static_cast<size_t>(pc)]) { flipsIn = pc; }
        if (scaleS[static_cast<size_t>(pc)] && !scaleN[static_cast<size_t>(pc)]) { flipsOut = pc; }
    }
    if (flipsIn < 0 || flipsOut < 0) {
        return notatedFifths;  // neighbors should differ by exactly one pc
    }

    // Duration-weighted pitch-class histogram over every ChordRest segment whose
    // notated signature equals `notatedFifths` (so a modulating score's other-key
    // spans do not pollute the evidence). No metric/decay bias — pervasiveness is
    // a global property of the notation, not a local window feature.
    const Measure* firstMeasure = sc->firstMeasure();
    if (!firstMeasure) {
        return notatedFifths;
    }

    std::array<double, 12> hist{};
    double total = 0.0;
    for (const Segment* s = firstMeasure->first(SegmentType::ChordRest);
         s; s = s->next1(SegmentType::ChordRest)) {
        const Fraction segTick = s->tick();
        if (static_cast<int>(sc->staff(clampedStaffIdx)->keySigEvent(segTick).concertKey()) != notatedFifths) {
            continue;
        }
        for (std::size_t si = 0; si < sc->nstaves(); ++si) {
            if (excludeStaves.count(si) || !ebr::staffIsEligible(sc, si, segTick)) {
                continue;
            }
            for (int v = 0; v < VOICES; ++v) {
                const ChordRest* cr = s->cr(static_cast<track_idx_t>(si) * VOICES + v);
                if (!cr || !cr->isChord() || cr->isGrace()) {
                    continue;
                }
                const double durQn = cr->actualTicks().ticks()
                                     / static_cast<double>(Constants::DIVISION);
                for (const Note* n : toChord(cr)->notes()) {
                    if (!n->play() || !n->visible()) {
                        continue;
                    }
                    const int pc = normalizePc(n->ppitch());
                    hist[static_cast<size_t>(pc)] += durQn;
                    total += durQn;
                }
            }
        }
    }

    if (total <= 0.0) {
        return notatedFifths;
    }

    constexpr double kPervasiveFraction = 0.03;  // accidental ≥ 3% of sounding weight
    constexpr double kDominanceRatio    = 2.0;   // accidental ≥ 2× its natural form
    const double wIn  = hist[static_cast<size_t>(flipsIn)];
    const double wOut = hist[static_cast<size_t>(flipsOut)];
    if (wIn > kPervasiveFraction * total && wIn >= kDominanceRatio * wOut) {
        return neighborFifths;
    }
    return notatedFifths;
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
    const KeyModeAnalysisResult* prevResult,
    KeyResolveDump* dumpOut)
{
    using namespace mu::engraving;

    const std::size_t clampedStaffIdx = std::min<std::size_t>(staffIdx, sc->nstaves() - 1);
    const KeySigEvent keySig = sc->staff(clampedStaffIdx)->keySigEvent(tick);
    int keyFifths = static_cast<int>(keySig.concertKey());
    const int notatedFifths = keyFifths;

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

    // ── Mode-absent measurement floor (Stage 4b-i) ───────────────────────
    //
    // When the caller sets prefs.ignoreDeclaredMode (batch_analyze
    // --ignore-declared-mode), drop the declared mode entirely. This disables
    // every remaining declared-mode influence at once — the small hint in
    // analyzeKeyMode, the partial-signature correction below (declared-gated),
    // and the piece-start opening — so key resolution is purely note-based. It
    // is the "no-crutch floor" condition; default false = no-op (byte-identical).
    if (prefs.ignoreDeclaredMode) {
        declaredMode = std::nullopt;
    }

    // ── Baroque partial-signature correction ─────────────────────────────
    //
    // Reinterpret the notated signature one step toward the declared mode's
    // missing accidental when the "one accidental short" convention is detected
    // (e.g. C minor notated with 2 flats → -3). All downstream steps (piece-start
    // anchor, analyzeKeyMode, fallback) use the corrected value, which lets the
    // proven machinery reach the true tonic without touching the signature lock.
    if (declaredMode.has_value()) {
        keyFifths = partialSignatureCorrection(sc, clampedStaffIdx, excludeStaves,
                                               keyFifths, *declaredMode);
    }

    if (dumpOut) {
        dumpOut->notatedFifths   = notatedFifths;
        dumpOut->correctedFifths = keyFifths;
        dumpOut->declaredModeOrdinal = declaredMode.has_value()
            ? static_cast<int>(keyModeIndex(*declaredMode)) : -1;
        dumpOut->pathTaken = "normal";
        dumpOut->candidates.clear();
    }

    // ── Fixed lookback window ─────────────────────────────────────────────
    const Fraction lookbackDuration = Fraction(shv::LOOKBACK_BEATS, 4);
    const Fraction windowStart = (tick > lookbackDuration)
                                 ? tick - lookbackDuration
                                 : Fraction(0, 1);

    // ── Piece-start opening: note-based (Stage 4b-i) ──────────────────────
    //
    // The former declared-mode piece-start short-circuit was removed in 4b-i:
    // it returned a declared anchor at piece start regardless of the opening
    // note evidence (a wall). The normal dynamic-lookahead path below already
    // handles the opening window (windowStart clamps to 0 when tick is inside
    // the lookback span), and gracefully handles prevResult == nullptr — the
    // hysteresis block guards on `prevResult != nullptr`. The opening is now
    // note-based; the only residual declared influence is the small hint inside
    // analyzeKeyMode. The insufficient-PCs fallback below still covers a
    // degenerate opening with < 3 distinct pitch classes.

    // ── Dynamic lookahead loop ────────────────────────────────────────────
    std::vector<KeyModeAnalyzer::PitchContext> ctx;
    std::vector<KeyModeAnalysisResult> results;

    int lookaheadBeats = shv::LOOKAHEAD_BEATS;
    while (true) {
        ctx.clear();
        const Fraction windowEnd = tick + Fraction(lookaheadBeats, 4);
        ebr::collectPitchContext(sc, tick, windowStart, windowEnd,
                                 excludeStaves, prefs, ctx);

        results = KeyModeAnalyzer::analyzeKeyMode(ctx, keyFifths, prefs, declaredMode,
                                                  dumpOut ? &dumpOut->candidates : nullptr);
        if (dumpOut) { dumpOut->lookaheadBeatsUsed = lookaheadBeats; }

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
        if (dumpOut) { dumpOut->pathTaken = "fallback"; }
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
            const KeySigMode beforeMode = results.front().mode;
            const int beforeFifths = results.front().keySignatureFifths;
            promoteWinnerInPlace(results, [&](const KeyModeAnalysisResult& r) {
                return r.mode == prevResult->mode
                    && r.keySignatureFifths == prevResult->keySignatureFifths;
            });
            if (dumpOut && (results.front().mode != beforeMode
                            || results.front().keySignatureFifths != beforeFifths)) {
                dumpOut->hysteresisPromoted = true;
            }
        }
    }

    // ── Strong declared-mode prior — REMOVED (Stage 4b-i) ─────────────────
    //
    // The former "Strong declared-mode prior" block promoted the highest-ranked
    // declared-compatible result to the front REGARDLESS of score gap — a hard
    // veto ("composer's intent overrides note-content inference"). It was removed
    // in 4b-i because it is incompatible with note-based-primary inference:
    // leaving it would make the §1 hint demotion a no-op wherever note inference
    // already out-scored the declared mode but got vetoed here. The residual
    // declared influence is now only the small hint inside analyzeKeyMode. The
    // note-based hysteresis block above (prevResult-mode) is unrelated and stays.

    return results;
}

} // namespace mu::composing::analysis::keyresolver
