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

#include "keymodeanalyzer.h"
#include "analysisutils.h"

#include <algorithm>
#include <array>
#include <cmath>
#include <limits>

namespace mu::composing::analysis {
namespace {

// ── Mode table ──────────────────────────────────────────────────────────────

struct ModeDef {
    const char* name;
    std::array<int, 7> intervals;  ///< Semitones from tonic for each scale degree
};

/// Full modal table.  Only the modes indexed by ACTIVE_MODE_INDICES are evaluated;
/// the rest are kept here for future re-enablement without interface changes.
constexpr std::array<ModeDef, 7> MODES = {{
    { "Ionian",     { 0, 2, 4, 5, 7, 9, 11 } },
    { "Dorian",     { 0, 2, 3, 5, 7, 9, 10 } },
    { "Phrygian",   { 0, 1, 3, 5, 7, 8, 10 } },
    { "Lydian",     { 0, 2, 4, 6, 7, 9, 11 } },
    { "Mixolydian", { 0, 2, 4, 5, 7, 9, 10 } },
    { "Aeolian",    { 0, 2, 3, 5, 7, 8, 10 } },
    { "Locrian",    { 0, 1, 3, 5, 6, 8, 10 } }
}};

/// Index into MODES for each KeyMode variant.
constexpr size_t IONIAN_INDEX  = 0;
constexpr size_t AEOLIAN_INDEX = 5;

/// The modes currently evaluated.  Extend this to enable more modes; the
/// evaluations table is sized dynamically to avoid the hardcoded-[12][2] fragility.
constexpr std::array<size_t, 2> ACTIVE_MODE_INDICES = { IONIAN_INDEX, AEOLIAN_INDEX };

// ── Key-signature helpers ────────────────────────────────────────────────────

/// Maps a modal tonic pitch class to the equivalent Ionian tonic that shares
/// the same key signature.  The offsets shift each mode's tonic onto the Ionian
/// tonic of the corresponding parallel key signature.
int ionianTonicPcForMode(int tonicPc, size_t modeIndex)
{
    constexpr std::array<int, 7> IONIAN_OFFSETS = { 0, -2, -4, -5, -7, 3, 1 };
    const int pc = tonicPc + IONIAN_OFFSETS[modeIndex];
    return (pc % 12 + 12) % 12;
}

/// Returns the one or two possible key-signature fifths values for an Ionian tonic
/// pitch class.  Enharmonic equivalents (e.g. C#/Db) have two entries; unambiguous
/// tonics have the same value repeated for uniform handling in the caller.
std::array<int, 2> possibleIonianFifthsForPc(int ionianPc)
{
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
}

/// Resolve a (tonicPc, modeIndex) pair to the keySignatureFifths value closest
/// to the reference key signature.
int resolveToFifths(int tonicPc, size_t modeIndex, int referenceKeySignatureFifths)
{
    const int ionianPc = ionianTonicPcForMode(tonicPc, modeIndex);
    const std::array<int, 2> opts = possibleIonianFifthsForPc(ionianPc);
    return (std::abs(opts[0] - referenceKeySignatureFifths)
            <= std::abs(opts[1] - referenceKeySignatureFifths))
           ? opts[0] : opts[1];
}

// ── Per-candidate evaluation data ────────────────────────────────────────────

/// Raw evidence for the triad tones and leading tone of a specific tonic/mode.
struct TriadEvidence {
    double tonicWeight       = 0.0;
    double thirdWeight       = 0.0;
    double fifthWeight       = 0.0;
    double leadingToneWeight = 0.0;
    bool hasCompleteTriad    = false;
};

/// All score components for one (tonicPc, modeSlot) candidate, preserved for
/// the post-hoc disambiguation and result-building passes.
struct CandidateEvaluation {
    double score          = -std::numeric_limits<double>::infinity();
    size_t modeIndex      = 0;
    TriadEvidence evidence;
    double scaleScore     = 0.0;
    double triadScore     = 0.0;
    double extraToneScore = 0.0;
    double keySignatureScore = 0.0;
};

// ── Per-candidate scoring helpers ────────────────────────────────────────────
//
// Each function computes one orthogonal score component.  They are called in
// sequence for every (tonicPc, modeSlot) combination.

/// Returns the combined note weight for a single pitch, applying the bass
/// multiplier and the overall weight cap.
double noteWeight(const KeyModeAnalyzer::PitchContext& p,
                  const KeyModeAnalyzerPreferences& prefs)
{
    return std::min(p.durationWeight * p.beatWeight, prefs.noteWeightCap)
           * (p.isBass ? prefs.bassMultiplier : 1.0);
}

/// Scale-membership score: positive for notes inside the candidate scale,
/// negative for chromatic notes.  Notes inside both the candidate scale and
/// the notated key-signature scale score highest (they are doubly confirmed).
double scoreScaleMembership(int tonicPc, const ModeDef& mode,
                             const std::array<bool, 12>& inKeySignatureScale,
                             const std::vector<KeyModeAnalyzer::PitchContext>& pitches,
                             const KeyModeAnalyzerPreferences& prefs)
{
    std::array<bool, 12> inScale {};
    for (int interval : mode.intervals) {
        inScale[static_cast<size_t>((tonicPc + interval) % 12)] = true;
    }

    double score = 0.0;
    for (const KeyModeAnalyzer::PitchContext& p : pitches) {
        const int pc = normalizePc(p.pitch);
        const double w = noteWeight(p, prefs);
        const bool inC  = inScale[static_cast<size_t>(pc)];
        const bool inKS = inKeySignatureScale[static_cast<size_t>(pc)];

        if      (inC && inKS)   { score += w * prefs.scaleScoreInBoth; }
        else if (inC && !inKS)  { score += w * prefs.scaleScoreInCandidateOnly; }
        else if (!inC && inKS)  { score += w * prefs.scaleScoreInKeySigOnly; }
        else                    { score += w * prefs.scaleScoreInNeither; }
    }
    return score;
}

/// Tonal-centre score: weighted evidence from tonic, third, fifth, leading tone,
/// and the complete-triad bonus.  Also builds the TriadEvidence for later use.
double scoreTriadEvidence(int tonicPc, size_t modeIndex,
                          const std::vector<KeyModeAnalyzer::PitchContext>& pitches,
                          const KeyModeAnalyzerPreferences& prefs,
                          TriadEvidence& evidenceOut)
{
    const int tonic       = tonicPc;
    const int third       = (modeIndex == IONIAN_INDEX)
                            ? (tonicPc + 4) % 12    // major third
                            : (tonicPc + 3) % 12;   // minor third
    const int fifth        = (tonicPc + 7) % 12;
    const int leadingTone  = (tonicPc + 11) % 12;   // used for both modes (harmonic minor convention)

    double extraScaleWeight = 0.0;
    std::array<bool, 12> inScale {};
    for (int interval : MODES[modeIndex].intervals) {
        inScale[static_cast<size_t>((tonicPc + interval) % 12)] = true;
    }

    for (const KeyModeAnalyzer::PitchContext& p : pitches) {
        const int pc = normalizePc(p.pitch);
        const double w = noteWeight(p, prefs);
        if      (pc == tonic)       { evidenceOut.tonicWeight       += w; }
        else if (pc == third)       { evidenceOut.thirdWeight       += w; }
        else if (pc == fifth)       { evidenceOut.fifthWeight       += w; }
        else if (pc == leadingTone) { evidenceOut.leadingToneWeight += w; }
        else if (inScale[static_cast<size_t>(pc)]) { extraScaleWeight += w; }
    }

    const bool hasTonic = evidenceOut.tonicWeight > 0.1;
    const bool hasThird = evidenceOut.thirdWeight > 0.1;
    const bool hasFifth = evidenceOut.fifthWeight > 0.1;
    evidenceOut.hasCompleteTriad = hasTonic && hasThird && hasFifth;

    double score = 0.0;
    score += prefs.tonicWeight       * std::min(evidenceOut.tonicWeight,       prefs.noteWeightCap);
    score += prefs.thirdWeight       * std::min(evidenceOut.thirdWeight,        prefs.noteWeightCap);
    score += prefs.fifthWeight       * std::min(evidenceOut.fifthWeight,        prefs.noteWeightCap);
    score += prefs.leadingToneWeight * std::min(evidenceOut.leadingToneWeight,  prefs.noteWeightCap);

    if (evidenceOut.hasCompleteTriad) {
        score += prefs.completeTriadBonus;
    } else if (!hasTonic) {
        score += prefs.missingTonicPenalty;
    }

    // Contribution of non-triad scale-member notes (diminishing returns).
    score += prefs.extraScaleFactor
             * std::min(extraScaleWeight, prefs.extraScaleCap);

    return score;
}

/// Key-signature proximity penalty: penalises candidates far from the notated
/// key signature (in circle-of-fifths distance).
double scoreKeySignatureProximity(int tonicPc, size_t modeIndex,
                                  int keySignatureFifths,
                                  const KeyModeAnalyzerPreferences& prefs)
{
    const int ionianPc = ionianTonicPcForMode(tonicPc, modeIndex);
    const std::array<int, 2> opts = possibleIonianFifthsForPc(ionianPc);
    const int distance = std::min(std::abs(opts[0] - keySignatureFifths),
                                  std::abs(opts[1] - keySignatureFifths));
    return -prefs.keySignatureDistancePenalty * static_cast<double>(distance);
}

// ── Tonal-centre score for relative-pair comparison ──────────────────────────
//
// The key-signature path uses a focussed tonal-centre formula (independent of the
// main triad-score weights) to compare the relative major/minor pair.
// Having a separate formula allows the two scoring concerns — overall candidate
// scoring and the final relative-pair decision — to be tuned independently.

double tonalCenterScore(const CandidateEvaluation& eval,
                        const KeyModeAnalyzerPreferences& prefs)
{
    double s = 0.0;
    s += prefs.tonalCenterTonicWeight  * std::min(eval.evidence.tonicWeight,       prefs.noteWeightCap);
    s += prefs.tonalCenterThirdWeight  * std::min(eval.evidence.thirdWeight,        prefs.noteWeightCap);
    s += prefs.tonalCenterFifthWeight  * std::min(eval.evidence.fifthWeight,        prefs.noteWeightCap);
    s += prefs.tonalCenterLeadingTone  * std::min(eval.evidence.leadingToneWeight,  prefs.noteWeightCap);
    if (eval.evidence.hasCompleteTriad) {
        s += prefs.tonalCenterTriadBonus;
    }
    return s;
}

// ── Relative major/minor post-hoc disambiguation ─────────────────────────────
//
// After the main scoring loop, relative major/minor pairs that share a key
// signature are explicitly disambiguated using tonic-presence and complete-triad
// evidence.
//
// Four cases (applied independently for every major/minor pair):
//
//   (A) Major has complete triad + tonic, minor has no tonic
//       → major += disambiguationTriadBonus, minor -= disambiguationTriadCost
//
//   (B) Minor has complete triad + tonic, major has no tonic
//       → minor += disambiguationTriadBonus, major -= disambiguationTriadCost
//       Note: (B) is structurally unreachable in practice for the natural relative
//       pair because the minor triad's m3 IS the major tonic.  It is preserved for
//       correctness if the mode table is extended.
//
//   (C) Major has tonic, minor has no tonic (no complete triad involved)
//       → major += disambiguationTonicBonus
//
//   (D) Minor has tonic, major has no tonic
//       → minor += disambiguationTonicBonus

void applyRelativePairDisambiguation(
    CandidateEvaluation& majorEval,
    CandidateEvaluation& minorEval,
    const KeyModeAnalyzerPreferences& prefs)
{
    // Case (A): major complete triad confirmed, minor tonic absent.
    if (majorEval.evidence.hasCompleteTriad
        && majorEval.evidence.tonicWeight > 0.1
        && minorEval.evidence.tonicWeight < 0.1)
    {
        majorEval.score += prefs.disambiguationTriadBonus;
        minorEval.score -= prefs.disambiguationTriadCost;
    }

    // Case (B): minor complete triad confirmed, major tonic absent.
    if (minorEval.evidence.hasCompleteTriad
        && minorEval.evidence.tonicWeight > 0.1
        && majorEval.evidence.tonicWeight < 0.1)
    {
        minorEval.score += prefs.disambiguationTriadBonus;
        majorEval.score -= prefs.disambiguationTriadCost;
    }

    // Case (C): major tonic present, minor tonic absent.
    if (majorEval.evidence.tonicWeight > 0.1 && minorEval.evidence.tonicWeight < 0.1) {
        majorEval.score += prefs.disambiguationTonicBonus;
    }

    // Case (D): minor tonic present, major tonic absent.
    if (minorEval.evidence.tonicWeight > 0.1 && majorEval.evidence.tonicWeight < 0.1) {
        minorEval.score += prefs.disambiguationTonicBonus;
    }
}

} // anonymous namespace

// ── Public API ───────────────────────────────────────────────────────────────

std::vector<KeyModeAnalysisResult> KeyModeAnalyzer::analyzeKeyMode(
    const std::vector<PitchContext>& pitches,
    int keySignatureFifths,
    const KeyModeAnalyzerPreferences& prefs)
{
    if (pitches.empty()) {
        return {};
    }

    // Build the scale-membership bitmap for the notated key signature (Ionian).
    std::array<bool, 12> inKeySignatureScale {};
    {
        const int keySigTonicPc = ionianTonicPcFromFifths(keySignatureFifths);
        for (int interval : MODES[IONIAN_INDEX].intervals) {
            inKeySignatureScale[static_cast<size_t>((keySigTonicPc + interval) % 12)] = true;
        }
    }

    // Evaluate every (tonicPc, modeSlot) combination.
    //
    // The evaluations are stored in a flat vector rather than a [12][2] array so
    // that extending ACTIVE_MODE_INDICES to more modes does not require any
    // structural changes here.
    const size_t numModeSlots = ACTIVE_MODE_INDICES.size();
    std::vector<CandidateEvaluation> evaluations(12 * numModeSlots);

    for (int tonicPc = 0; tonicPc < 12; ++tonicPc) {
        for (size_t modeSlot = 0; modeSlot < numModeSlots; ++modeSlot) {
            const size_t modeIndex = ACTIVE_MODE_INDICES[modeSlot];
            CandidateEvaluation& eval = evaluations[static_cast<size_t>(tonicPc) * numModeSlots + modeSlot];
            eval.modeIndex = modeIndex;

            eval.scaleScore      = scoreScaleMembership(tonicPc, MODES[modeIndex],
                                                        inKeySignatureScale, pitches, prefs);
            eval.triadScore      = scoreTriadEvidence(tonicPc, modeIndex, pitches, prefs,
                                                      eval.evidence);
            eval.keySignatureScore = scoreKeySignatureProximity(tonicPc, modeIndex,
                                                                keySignatureFifths, prefs);
            eval.extraToneScore  = 0.0;  // folded into triadScore via scoreTriadEvidence
            eval.score           = eval.scaleScore + eval.triadScore + eval.keySignatureScore;
        }
    }

    // Apply relative major/minor post-hoc disambiguation for every pair.
    for (int majorTonicPc = 0; majorTonicPc < 12; ++majorTonicPc) {
        const int minorTonicPc = (majorTonicPc + 9) % 12;

        // modeSlot 0 = Ionian (major), modeSlot 1 = Aeolian (minor).
        CandidateEvaluation& majorEval = evaluations[static_cast<size_t>(majorTonicPc) * numModeSlots + 0];
        CandidateEvaluation& minorEval = evaluations[static_cast<size_t>(minorTonicPc) * numModeSlots + 1];

        applyRelativePairDisambiguation(majorEval, minorEval, prefs);
    }

    // Select the best candidate.
    //
    // When the key signature is within the valid range [-7, 7], the relative
    // major/minor pair for that key signature is first compared using the focussed
    // tonal-centre formula; the global highest-scoring candidate wins only if the
    // key signature is out of range (defensive path for invalid input).
    int bestTonicPc    = 0;
    size_t bestModeSlot = 0;
    double bestScore   = -std::numeric_limits<double>::infinity();

    if (keySignatureFifths >= -7 && keySignatureFifths <= 7) {
        const int keySigMajorTonicPc = ionianTonicPcFromFifths(keySignatureFifths);
        const int keySigMinorTonicPc = (keySigMajorTonicPc + 9) % 12;

        const CandidateEvaluation& majorEval = evaluations[static_cast<size_t>(keySigMajorTonicPc) * numModeSlots + 0];
        const CandidateEvaluation& minorEval = evaluations[static_cast<size_t>(keySigMinorTonicPc) * numModeSlots + 1];

        const double majorCenter = tonalCenterScore(majorEval, prefs);
        const double minorCenter = tonalCenterScore(minorEval, prefs);
        const double delta = majorCenter - minorCenter;

        const bool chooseMajor = (std::abs(delta) > prefs.tonalCenterDeltaThreshold)
                                 ? (delta > 0.0)
                                 : (majorEval.score >= minorEval.score);

        bestTonicPc  = chooseMajor ? keySigMajorTonicPc : keySigMinorTonicPc;
        bestModeSlot = chooseMajor ? 0 : 1;
        bestScore    = chooseMajor ? majorEval.score : minorEval.score;
    } else {
        // Out-of-range key signature: use the global highest-scoring candidate.
        for (int tonicPc = 0; tonicPc < 12; ++tonicPc) {
            for (size_t modeSlot = 0; modeSlot < numModeSlots; ++modeSlot) {
                const CandidateEvaluation& eval = evaluations[static_cast<size_t>(tonicPc) * numModeSlots + modeSlot];
                if (eval.score > bestScore) {
                    bestScore    = eval.score;
                    bestTonicPc  = tonicPc;
                    bestModeSlot = modeSlot;
                }
            }
        }
    }

    // Build the result list (up to 3), placing the key-signature winner first.
    struct RawCandidate {
        double score;
        int tonicPc;
        size_t modeSlot;
    };

    std::vector<RawCandidate> allCandidates;
    allCandidates.reserve(12 * numModeSlots);
    for (int tonicPc = 0; tonicPc < 12; ++tonicPc) {
        for (size_t modeSlot = 0; modeSlot < numModeSlots; ++modeSlot) {
            allCandidates.push_back({
                evaluations[static_cast<size_t>(tonicPc) * numModeSlots + modeSlot].score,
                tonicPc, modeSlot });
        }
    }
    std::sort(allCandidates.begin(), allCandidates.end(),
              [](const RawCandidate& a, const RawCandidate& b) { return a.score > b.score; });

    std::vector<KeyModeAnalysisResult> results;
    results.reserve(3);

    const size_t bestModeIndex = ACTIVE_MODE_INDICES[bestModeSlot];
    KeyModeAnalysisResult best;
    best.keySignatureFifths = resolveToFifths(bestTonicPc, bestModeIndex, keySignatureFifths);
    best.mode  = (bestModeIndex == IONIAN_INDEX) ? KeyMode::Ionian : KeyMode::Aeolian;
    best.score = bestScore;
    results.push_back(best);

    for (const RawCandidate& c : allCandidates) {
        if (results.size() >= 3) {
            break;
        }
        const size_t modeIndex = ACTIVE_MODE_INDICES[c.modeSlot];
        const int fifths = resolveToFifths(c.tonicPc, modeIndex, keySignatureFifths);
        const KeyMode mode = (modeIndex == IONIAN_INDEX) ? KeyMode::Ionian : KeyMode::Aeolian;
        if (fifths == best.keySignatureFifths && mode == best.mode) {
            continue;  // already added as the winner
        }
        KeyModeAnalysisResult r;
        r.keySignatureFifths = fifths;
        r.mode  = mode;
        r.score = c.score;
        results.push_back(r);
    }

    return results;
}

} // namespace mu::composing::analysis
