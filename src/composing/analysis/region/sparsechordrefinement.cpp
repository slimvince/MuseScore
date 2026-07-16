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

#include "sparsechordrefinement.h"

#include <optional>
#include <tuple>

#include "composing/analysis/chord/analysisutils.h"
#include "composing/analysis/chord/keycollectionprobe.h"   // OI-168 counters (default-OFF)

namespace kcp = mu::composing::analysis::keycollectionprobe;

namespace mu::composing::analysis::region {

namespace {

std::optional<std::tuple<ChordQuality, int, int>> diatonicTriadShapeForDegree(
    int degree, KeySigMode keyMode)
{
    if (degree < 0 || degree > 6) {
        return std::nullopt;
    }

    const auto& scale = keyModeScaleIntervals(keyMode);
    const int rootInterval = scale[static_cast<size_t>(degree)];
    const int thirdDegree = degree + 2;
    const int fifthDegree = degree + 4;
    const int thirdInterval = (scale[static_cast<size_t>(thirdDegree % 7)]
                               + (thirdDegree >= 7 ? 12 : 0)
                               - rootInterval) % 12;
    const int fifthInterval = (scale[static_cast<size_t>(fifthDegree % 7)]
                               + (fifthDegree >= 7 ? 12 : 0)
                               - rootInterval) % 12;

    if (thirdInterval == 4 && fifthInterval == 7) {
        return std::make_tuple(ChordQuality::Major, thirdInterval, fifthInterval);
    }
    if (thirdInterval == 3 && fifthInterval == 7) {
        return std::make_tuple(ChordQuality::Minor, thirdInterval, fifthInterval);
    }
    if (thirdInterval == 3 && fifthInterval == 6) {
        return std::make_tuple(ChordQuality::Diminished, thirdInterval, fifthInterval);
    }
    if (thirdInterval == 4 && fifthInterval == 8) {
        return std::make_tuple(ChordQuality::Augmented, thirdInterval, fifthInterval);
    }

    return std::nullopt;
}

bool tonesFitTriadShape(const std::vector<ChordAnalysisTone>& tones,
                        int rootPc,
                        int thirdInterval,
                        int fifthInterval)
{
    bool seenPitchClasses[12] = {};
    for (const auto& tone : tones) {
        const int pitchClass = tone.pitch % 12;
        if (seenPitchClasses[pitchClass]) {
            continue;
        }
        seenPitchClasses[pitchClass] = true;

        const int interval = (pitchClass - rootPc + 12) % 12;
        if (interval != 0 && interval != thirdInterval && interval != fifthInterval) {
            return false;
        }
    }
    return true;
}

int distinctPitchClassCount(const std::vector<ChordAnalysisTone>& tones)
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

} // anonymous namespace

int diatonicDegreeForRootPc(int rootPc, int keyFifths, KeySigMode keyMode)
{
    const int tonicPc = (ionianTonicPcFromFifths(keyFifths)
                         + keyModeTonicOffset(keyMode)) % 12;
    const auto& scale = keyModeScaleIntervals(keyMode);
    for (size_t i = 0; i < scale.size(); ++i) {
        if ((tonicPc + scale[i]) % 12 == rootPc) {
            return static_cast<int>(i);
        }
    }
    return -1;
}

void refineSparseChordQualityFromKeyContext(
    ChordAnalysisResult& result,
    const std::vector<ChordAnalysisTone>& tones,
    int keyFifths,
    KeySigMode keyMode)
{
    if (result.identity.quality != ChordQuality::Unknown) {
        return;
    }

    // OI-168 Task A (default-OFF): does the Aeolian guard below ever actually run?
    kcp::bump(kcp::counters().sparseRefineEntries);

    const int uniquePitchClasses = distinctPitchClassCount(tones);

    int degree = result.function.degree;
    if (degree < 0 || degree > 6) {
        degree = diatonicDegreeForRootPc(result.identity.rootPc, keyFifths, keyMode);
        if (degree < 0) {
            return;
        }

        result.function.degree = degree;
        result.function.keyTonicPc = (ionianTonicPcFromFifths(keyFifths)
                                      + keyModeTonicOffset(keyMode)) % 12;
        result.function.keyMode = keyMode;
    }

    const auto triadShape = diatonicTriadShapeForDegree(degree, keyMode);
    if (!triadShape) {
        return;
    }

    const auto [quality, thirdInterval, fifthInterval] = *triadShape;

    // In plain Aeolian, a lone tonic or dominant pitch is too ambiguous to
    // harden into a minor triad. Leave it unqualified and let richer later
    // evidence decide the quality.
    //
    // OI-168 Task A (default-OFF): the guard is the one TONIC-dependent site OI-167 named
    // outside the chord scorer. Count its shape preconditions separately from the Aeolian
    // test, so a zero fire-count says WHICH conjunct is unreachable.
    const bool guardShapeMatches = (uniquePitchClasses == 1
                                    && quality == ChordQuality::Minor
                                    && (degree == 0 || degree == 4));
    if (guardShapeMatches) {
        kcp::bump(kcp::counters().sparseGuardShapeMatched);
    }
    if (guardShapeMatches && keyMode == KeySigMode::Aeolian) {
        kcp::bump(kcp::counters().sparseAeolianGuardFires);
        return;
    }

    if (!tonesFitTriadShape(tones, result.identity.rootPc, thirdInterval, fifthInterval)) {
        return;
    }

    result.identity.quality = quality;
}

void applyTonicPriorToSparseChord(
    ChordAnalysisResult& result,
    const std::vector<ChordAnalysisTone>& tones,
    int keyFifths,
    KeySigMode keyMode)
{
    const auto q = result.identity.quality;
    const bool isThin = (q == ChordQuality::Power
                      || q == ChordQuality::Suspended2
                      || q == ChordQuality::Suspended4);
    if (!isThin) {
        return;
    }

    // OI-170 (default-OFF): this runs on the region analyzer's COMMIT path and overwrites the
    // committed quality, and it reaches that quality through the tonic (diatonicDegreeForRootPc
    // → diatonicTriadShapeForDegree). Counted, not changed — it is a class-(b) genuine-degree
    // site the signature-mask primitive cannot replace, and its live fire count is the magnitude
    // the fix design has to account for.
    kcp::bump(kcp::counters().tonicPriorEntries);

    // Dense regions (3+ PCs) carry their own quality evidence; overriding
    // them with a diatonic assumption would suppress legitimate chord color.
    if (distinctPitchClassCount(tones) > 2) {
        return;
    }

    const int degree = diatonicDegreeForRootPc(
        result.identity.rootPc, keyFifths, keyMode);
    if (degree < 0) {
        return;
    }

    const auto triadShape = diatonicTriadShapeForDegree(degree, keyMode);
    if (!triadShape) {
        return;
    }
    const auto diatonicQuality = std::get<0>(*triadShape);

    kcp::bump(kcp::counters().tonicPriorApplied);
    result.identity.quality = diatonicQuality;
}

void forceChordTrackQualityFromKeyContext(
    ChordAnalysisResult& result,
    KeySigMode keyMode)
{
    if (result.identity.quality != ChordQuality::Unknown) {
        return;
    }

    const int degree = result.function.degree;
    const auto triadShape = diatonicTriadShapeForDegree(degree, keyMode);
    if (!triadShape) {
        return;
    }

    result.identity.quality = std::get<0>(*triadShape);
}

} // namespace mu::composing::analysis::region
