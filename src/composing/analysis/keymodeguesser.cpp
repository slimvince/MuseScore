/*
 * SPDX-License-Identifier: GPL-3.0-only
 * MuseScore-Studio-CLA-applies
 */

#include "keymodeguesser.h"

#include <algorithm>
#include <array>
#include <cmath>
#include <limits>
#include <vector>

namespace mu::composing::analysis {

KeyModeGuessResult KeyModeGuesser::guessKeyMode(const std::vector<PitchContext>& pitches,
                                                int keySignatureFifths)
{
    if (pitches.empty()) {
        return {};
    }

    struct ModeDef {
        const char* name;
        std::array<int, 7> intervals;
    };

    constexpr std::array<ModeDef, 7> MODES = {{
        { "Ionian",     { 0, 2, 4, 5, 7, 9, 11 } },
        { "Dorian",     { 0, 2, 3, 5, 7, 9, 10 } },
        { "Phrygian",   { 0, 1, 3, 5, 7, 8, 10 } },
        { "Lydian",     { 0, 2, 4, 6, 7, 9, 11 } },
        { "Mixolydian", { 0, 2, 4, 5, 7, 9, 10 } },
        { "Aeolian",    { 0, 2, 3, 5, 7, 8, 10 } },
        { "Locrian",    { 0, 1, 3, 5, 6, 8, 10 } }
    }};

    // Temporary product decision: ignore church modes for now.
    // We only evaluate Ionian (major) and Aeolian (minor),
    // but keep the full mode table so it can be re-enabled later.
    constexpr std::array<size_t, 2> ACTIVE_MODE_INDICES = { 0, 5 };

    auto normalizePc = [](int pitch) -> int {
        int pc = pitch % 12;
        return pc < 0 ? pc + 12 : pc;
    };

    auto ionianTonicPcForMode = [](int tonicPc, size_t modeIndex) -> int {
        // Convert modal tonic to the equivalent Ionian tonic that shares the same key signature.
        // Ionian->0, Dorian->-2, Phrygian->-4, Lydian->-5, Mixolydian->-7, Aeolian->+3, Locrian->+1
        constexpr std::array<int, 7> IONIAN_OFFSETS = { 0, -2, -4, -5, -7, 3, 1 };
        const int pc = tonicPc + IONIAN_OFFSETS[modeIndex];
        return (pc % 12 + 12) % 12;
    };

    auto possibleIonianFifthsForPc = [](int ionianPc) -> std::array<int, 2> {
        // First value is canonical; second is enharmonic alternative when available.
        switch (ionianPc) {
        case 0:  return {  0,  0 };  // C
        case 1:  return {  7, -5 };  // C# / Db
        case 2:  return {  2,  2 };  // D
        case 3:  return { -3, -3 };  // Eb
        case 4:  return {  4,  4 };  // E
        case 5:  return { -1, -1 };  // F
        case 6:  return {  6, -6 };  // F# / Gb
        case 7:  return {  1,  1 };  // G
        case 8:  return { -4, -4 };  // Ab
        case 9:  return {  3,  3 };  // A
        case 10: return { -2, -2 };  // Bb
        case 11: return {  5, -7 };  // B / Cb
        default: return {  0,  0 };
        }
    };

    auto ionianTonicPcFromFifths = [](int fifths) -> int {
        // Fixed key-signature context mapped to its Ionian tonic pitch class.
        switch (fifths) {
        case -7: return 11; // Cb
        case -6: return 6;  // Gb
        case -5: return 1;  // Db
        case -4: return 8;  // Ab
        case -3: return 3;  // Eb
        case -2: return 10; // Bb
        case -1: return 5;  // F
        case 0:  return 0;  // C
        case 1:  return 7;  // G
        case 2:  return 2;  // D
        case 3:  return 9;  // A
        case 4:  return 4;  // E
        case 5:  return 11; // B
        case 6:  return 6;  // F#
        case 7:  return 1;  // C#
        default: return 0;  // Fall back to C if context is out of range
        }
    };

    std::array<bool, 12> inKeySignatureScale {};
    {
        const int keySigIonianTonicPc = ionianTonicPcFromFifths(keySignatureFifths);
        for (int interval : MODES[0].intervals) {
            inKeySignatureScale[(keySigIonianTonicPc + interval) % 12] = true;
        }
    }

    struct CandidateEvidence {
        // Weighted accumulated evidence (duration × beat × bass multiplier).
        double tonicWeight = 0.0;
        double thirdWeight = 0.0;
        double fifthWeight = 0.0;
        double leadingToneWeight = 0.0;  // Feature 4: semitone-below-tonic signal
        bool hasCompleteTriad = false;
    };

    struct CandidateEvaluation {
        double score = -std::numeric_limits<double>::infinity();
        size_t modeIndex = 0;
        CandidateEvidence evidence;
        double scaleScore = 0.0;
        double triadScore = 0.0;
        double extraToneScore = 0.0;
        double keySignatureScore = 0.0;
        double relativeBiasScore = 0.0;
    };

    std::array<std::array<CandidateEvaluation, 2>, 12> evaluations {};

    for (int tonicPc = 0; tonicPc < 12; ++tonicPc) {
        for (size_t modeSlot = 0; modeSlot < ACTIVE_MODE_INDICES.size(); ++modeSlot) {
            const size_t modeIndex = ACTIVE_MODE_INDICES[modeSlot];
            std::array<bool, 12> inScale {};
            for (int interval : MODES[modeIndex].intervals) {
                inScale[(tonicPc + interval) % 12] = true;
            }

            double scaleScore = 0.0;

            // Feature 1+2+3: scale membership weighted by duration × metric position × bass.
            // Tones outside fixed accidentals are down-weighted to avoid overfitting
            // local alterations when estimating the global key.
            for (const PitchContext& p : pitches) {
                const int pitch = p.pitch;
                const int pc = normalizePc(pitch);
                const bool candidateInScale = inScale[pc];
                const bool keySigInScale = inKeySignatureScale[pc];

                // Bass notes (Feature 1) get double weight; duration and beat compound the effect.
                const double w = std::min(p.durationWeight * p.beatWeight, 3.0)
                                 * (p.isBass ? 2.0 : 1.0);

                if (candidateInScale && keySigInScale) {
                    scaleScore += w * 1.0;
                } else if (candidateInScale && !keySigInScale) {
                    scaleScore += w * 0.25;
                } else if (!candidateInScale && keySigInScale) {
                    scaleScore -= w * 0.2;
                } else {
                    scaleScore -= w * 0.05;
                }
            }

            const int tonic = tonicPc;
            const int third = (modeIndex == 0) ? (tonicPc + 4) % 12 : (tonicPc + 3) % 12;
            const int fifth = (tonicPc + 7) % 12;
            // Feature 4: leading tone is a semitone below the tonic.
            const int leadingTonePc = (tonicPc + 11) % 12;

            double extraScaleWeight = 0.0;
            CandidateEvidence evidence;

            for (const PitchContext& p : pitches) {
                const int pitch = p.pitch;
                const int pc = normalizePc(pitch);
                const double w = std::min(p.durationWeight * p.beatWeight, 3.0)
                                 * (p.isBass ? 2.0 : 1.0);
                if (pc == tonic) {
                    evidence.tonicWeight += w;
                } else if (pc == third) {
                    evidence.thirdWeight += w;
                } else if (pc == fifth) {
                    evidence.fifthWeight += w;
                } else if (pc == leadingTonePc) {
                    evidence.leadingToneWeight += w;
                } else if (inScale[pc]) {
                    extraScaleWeight += w;
                }
            }

            // Presence threshold: small weights from very short offbeat notes are ignored.
            const bool hasTonic = evidence.tonicWeight > 0.1;
            const bool hasThird = evidence.thirdWeight > 0.1;
            const bool hasFifth = evidence.fifthWeight > 0.1;
            evidence.hasCompleteTriad = hasTonic && hasThird && hasFifth;

            double triadScore = 0.0;
            // Feature 2: tonic-triad evidence, saturated to avoid over-dominance.
            triadScore += 1.6 * std::min(evidence.tonicWeight, 3.0);
            triadScore += 0.7 * std::min(evidence.thirdWeight, 2.0);
            triadScore += 0.5 * std::min(evidence.fifthWeight, 2.0);
            // Feature 4: leading tone boost.
            triadScore += 0.4 * std::min(evidence.leadingToneWeight, 2.0);

            // Complete triad is a strong tonal anchor; missing tonic is strongly penalised.
            if (evidence.hasCompleteTriad) {
                triadScore += 2.5;
            } else if (!hasTonic) {
                triadScore -= 2.5;
            }

            // Additional in-scale tones provide mild support; much less than tonic-triad.
            const double extraToneScore = 0.1 * std::min(extraScaleWeight, 5.0);

            // Key-signature prior: prefer mode/tonic pairs compatible with local fixed accidentals.
            const int ionianPc = ionianTonicPcForMode(tonicPc, modeIndex);
            const std::array<int, 2> fifthOptions = possibleIonianFifthsForPc(ionianPc);
            const int fifthDistance = std::min(std::abs(fifthOptions[0] - keySignatureFifths),
                                               std::abs(fifthOptions[1] - keySignatureFifths));
            const double keySignatureScore = -0.6 * static_cast<double>(fifthDistance);

            const double score = scaleScore + triadScore + extraToneScore + keySignatureScore;

            evaluations[static_cast<size_t>(tonicPc)][modeSlot].score = score;
            evaluations[static_cast<size_t>(tonicPc)][modeSlot].modeIndex = modeIndex;
            evaluations[static_cast<size_t>(tonicPc)][modeSlot].evidence = evidence;
            evaluations[static_cast<size_t>(tonicPc)][modeSlot].scaleScore = scaleScore;
            evaluations[static_cast<size_t>(tonicPc)][modeSlot].triadScore = triadScore;
            evaluations[static_cast<size_t>(tonicPc)][modeSlot].extraToneScore = extraToneScore;
            evaluations[static_cast<size_t>(tonicPc)][modeSlot].keySignatureScore = keySignatureScore;
        }
    }

    // Explicitly disambiguate relative major/minor pairs sharing the same key signature.
    // If one side has a clear tonic center and the other side lacks its tonic entirely,
    // prefer the candidate with actual tonic-triad evidence.
    for (int majorTonicPc = 0; majorTonicPc < 12; ++majorTonicPc) {
        const int minorTonicPc = (majorTonicPc + 9) % 12;

        CandidateEvaluation& majorEval = evaluations[static_cast<size_t>(majorTonicPc)][0];
        CandidateEvaluation& minorEval = evaluations[static_cast<size_t>(minorTonicPc)][1];

        if (majorEval.evidence.hasCompleteTriad && majorEval.evidence.tonicWeight > 0.1
            && minorEval.evidence.tonicWeight < 0.1) {
            majorEval.score += 4.5;
            minorEval.score -= 1.5;
            majorEval.relativeBiasScore += 4.5;
            minorEval.relativeBiasScore -= 1.5;
        }

        if (minorEval.evidence.hasCompleteTriad && minorEval.evidence.tonicWeight > 0.1
            && majorEval.evidence.tonicWeight < 0.1) {
            minorEval.score += 4.5;
            majorEval.score -= 1.5;
            minorEval.relativeBiasScore += 4.5;
            majorEval.relativeBiasScore -= 1.5;
        }

        if (majorEval.evidence.tonicWeight > 0.1 && minorEval.evidence.tonicWeight < 0.1) {
            majorEval.score += 1.0;
            majorEval.relativeBiasScore += 1.0;
        }

        if (minorEval.evidence.tonicWeight > 0.1 && majorEval.evidence.tonicWeight < 0.1) {
            minorEval.score += 1.0;
            minorEval.relativeBiasScore += 1.0;
        }
    }

    double globalBestScore = -std::numeric_limits<double>::infinity();
    int globalBestTonicPc = 0;
    size_t globalBestModeIndex = 0;
    for (int tonicPc = 0; tonicPc < 12; ++tonicPc) {
        for (size_t modeSlot = 0; modeSlot < ACTIVE_MODE_INDICES.size(); ++modeSlot) {
            const CandidateEvaluation& evaluation = evaluations[static_cast<size_t>(tonicPc)][modeSlot];
            if (evaluation.score > globalBestScore) {
                globalBestScore = evaluation.score;
                globalBestTonicPc = tonicPc;
                globalBestModeIndex = evaluation.modeIndex;
            }
        }
    }

    double bestScore = globalBestScore;
    int bestTonicPc = globalBestTonicPc;
    size_t bestModeIndex = globalBestModeIndex;

    if (keySignatureFifths >= -7 && keySignatureFifths <= 7) {
        const int keySigMajorTonicPc = ionianTonicPcFromFifths(keySignatureFifths);
        const int keySigMinorTonicPc = (keySigMajorTonicPc + 9) % 12;

        const CandidateEvaluation& majorEval = evaluations[static_cast<size_t>(keySigMajorTonicPc)][0];
        const CandidateEvaluation& minorEval = evaluations[static_cast<size_t>(keySigMinorTonicPc)][1];

        // When local fixed accidentals are known, first decide between that signature's
        // own relative major/minor pair before falling back to a global search.
        const auto tonalCenterScore = [](const CandidateEvaluation& eval) -> double {
            double s = 0.0;
            s += 2.2 * std::min(eval.evidence.tonicWeight, 3.0);
            s += 1.0 * std::min(eval.evidence.thirdWeight, 2.0);
            s += 0.7 * std::min(eval.evidence.fifthWeight, 2.0);
            s += 0.5 * std::min(eval.evidence.leadingToneWeight, 2.0);
            if (eval.evidence.hasCompleteTriad) {
                s += 2.0;
            }
            return s;
        };

        const double majorCenter = tonalCenterScore(majorEval);
        const double minorCenter = tonalCenterScore(minorEval);
        const double centerDelta = majorCenter - minorCenter;

        bool chooseMajor = false;
        if (std::abs(centerDelta) > 0.25) {
            chooseMajor = centerDelta > 0.0;
        } else {
            // If tonal centers are nearly tied, let the full candidate score decide.
            chooseMajor = majorEval.score >= minorEval.score;
        }

        bestTonicPc = chooseMajor ? keySigMajorTonicPc : keySigMinorTonicPc;
        bestModeIndex = chooseMajor ? ACTIVE_MODE_INDICES[0] : ACTIVE_MODE_INDICES[1];
        bestScore = chooseMajor ? majorEval.score : minorEval.score;
    }

    const int bestIonianPc = ionianTonicPcForMode(bestTonicPc, bestModeIndex);
    const std::array<int, 2> bestFifthOptions = possibleIonianFifthsForPc(bestIonianPc);
    const int distance0 = std::abs(bestFifthOptions[0] - keySignatureFifths);
    const int distance1 = std::abs(bestFifthOptions[1] - keySignatureFifths);
    const int chosenFifths = (distance0 <= distance1) ? bestFifthOptions[0] : bestFifthOptions[1];

    KeyModeGuessResult result;
    result.keySignatureFifths = chosenFifths;
    result.isMajor = (bestModeIndex == 0); // Active modes are Ionian and Aeolian only.
    result.score = bestScore;
    result.isValid = true;

    return result;
}

} // namespace mu::composing::analysis
