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
#include <optional>

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
constexpr size_t IONIAN_INDEX     = 0;
constexpr size_t DORIAN_INDEX     = 1;
constexpr size_t PHRYGIAN_INDEX   = 2;
constexpr size_t LYDIAN_INDEX     = 3;
constexpr size_t MIXOLYDIAN_INDEX = 4;
constexpr size_t AEOLIAN_INDEX    = 5;
constexpr size_t LOCRIAN_INDEX    = 6;

/// All seven diatonic modes are evaluated.
constexpr std::array<size_t, 7> ACTIVE_MODE_INDICES = {
    IONIAN_INDEX, DORIAN_INDEX, PHRYGIAN_INDEX, LYDIAN_INDEX,
    MIXOLYDIAN_INDEX, AEOLIAN_INDEX, LOCRIAN_INDEX
};

/// Characteristic pitch for each mode — the one scale degree that most
/// distinguishes it from its closest neighbor.  Index is the mode's position
/// in ACTIVE_MODE_INDICES (same as MODES index).  Value is the semitone
/// interval from the tonic.
///
/// These are theory-grounded (each mode's signature pitch); the scoring
/// weight applied to them is empirical.
constexpr std::array<int, 7> CHARACTERISTIC_INTERVAL = {
    11,   // Ionian:     major 7th — distinguishes from Mixolydian
     9,   // Dorian:     major 6th — distinguishes from Aeolian
     1,   // Phrygian:   minor 2nd — distinguishes from Aeolian
     6,   // Lydian:     augmented 4th — distinguishes from Ionian
    10,   // Mixolydian: minor 7th — distinguishes from Ionian
     8,   // Aeolian:    minor 6th — distinguishes from Dorian
     6,   // Locrian:    diminished 5th — distinguishes from Phrygian
};

} // anonymous namespace

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

namespace {

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
    const int third       = (tonicPc + MODES[modeIndex].intervals[2]) % 12;  // 3rd degree from mode table
    const int fifth       = (tonicPc + MODES[modeIndex].intervals[4]) % 12;  // 5th degree from mode table
    const int leadingTone = (tonicPc + MODES[modeIndex].intervals[6]) % 12;  // 7th degree from mode table

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

/// Characteristic pitch score: boost when the mode's distinguishing pitch is
/// present, penalty when it is absent.
double scoreCharacteristicPitch(int tonicPc, size_t modeIndex,
                                const std::vector<KeyModeAnalyzer::PitchContext>& pitches,
                                const KeyModeAnalyzerPreferences& prefs)
{
    const int charPc = (tonicPc + CHARACTERISTIC_INTERVAL[modeIndex]) % 12;
    double charWeight = 0.0;
    for (const KeyModeAnalyzer::PitchContext& p : pitches) {
        if (normalizePc(p.pitch) == charPc) {
            charWeight += noteWeight(p, prefs);
        }
    }
    return (charWeight > 0.1) ? prefs.characteristicPitchBoost
                              : prefs.characteristicPitchPenalty;
}

/// True leading-tone score: the presence of a note a semitone below the
/// candidate's tonic is the strongest tonal gravity signal in Western music.
/// Unlike the mode-specific 7th degree (which is a whole step for Dorian,
/// Phrygian, Mixolydian, Aeolian), this always checks (tonicPc + 11) % 12.
/// A chromatic leading tone (e.g. G# in A natural minor) still indicates
/// that pitch class as tonic — it's the harmonic minor raised 7th.
double scoreTrueLeadingTone(int tonicPc,
                            const std::vector<KeyModeAnalyzer::PitchContext>& pitches,
                            const KeyModeAnalyzerPreferences& prefs)
{
    const int ltPc = (tonicPc + 11) % 12;
    double ltWeight = 0.0;
    for (const KeyModeAnalyzer::PitchContext& p : pitches) {
        if (normalizePc(p.pitch) == ltPc) {
            ltWeight += noteWeight(p, prefs);
        }
    }
    return (ltWeight > 0.1) ? prefs.trueLeadingToneBoost : 0.0;
}

/// Mode prior: additive bias reflecting real-world mode frequency.
/// Ionian and Aeolian are overwhelmingly more common than Lydian or Locrian,
/// so when pitch evidence is ambiguous, the prior tips the balance toward
/// the more likely mode.
double scoreModePrior(size_t modeIndex, const KeyModeAnalyzerPreferences& prefs)
{
    constexpr size_t IONIAN     = 0;
    constexpr size_t DORIAN     = 1;
    constexpr size_t PHRYGIAN   = 2;
    constexpr size_t LYDIAN     = 3;
    constexpr size_t MIXOLYDIAN = 4;
    constexpr size_t AEOLIAN    = 5;
    constexpr size_t LOCRIAN    = 6;

    switch (modeIndex) {
    case IONIAN:     return prefs.modePriorIonian;
    case DORIAN:     return prefs.modePriorDorian;
    case PHRYGIAN:   return prefs.modePriorPhrygian;
    case LYDIAN:     return prefs.modePriorLydian;
    case MIXOLYDIAN: return prefs.modePriorMixolydian;
    case AEOLIAN:    return prefs.modePriorAeolian;
    case LOCRIAN:    return prefs.modePriorLocrian;
    default:         return 0.0;
    }
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

// ── Pairwise post-hoc disambiguation ─────────────────────────────────────────
//
// After the main scoring loop, pairs of modes sharing a key signature are
// explicitly disambiguated using tonic-presence and complete-triad evidence.
// This generalizes the former relative-major/minor disambiguation to all 7 modes.
//
// For each ordered pair (A, B) of modes sharing a key signature:
//   - If A has a complete triad + tonic and B has no tonic:
//     A gets a boost, B gets a penalty.
//   - If A has tonic presence and B does not (no complete triad):
//     A gets a smaller boost.

void applyPairwiseDisambiguation(
    CandidateEvaluation& evalA,
    CandidateEvaluation& evalB,
    const KeyModeAnalyzerPreferences& prefs)
{
    const bool aHasTonic = evalA.evidence.tonicWeight > 0.1;
    const bool bHasTonic = evalB.evidence.tonicWeight > 0.1;

    if (evalA.evidence.hasCompleteTriad && aHasTonic && !bHasTonic) {
        evalA.score += prefs.disambiguationTriadBonus;
        evalB.score -= prefs.disambiguationTriadCost;
    }
    if (evalB.evidence.hasCompleteTriad && bHasTonic && !aHasTonic) {
        evalB.score += prefs.disambiguationTriadBonus;
        evalA.score -= prefs.disambiguationTriadCost;
    }
    if (aHasTonic && !bHasTonic) {
        evalA.score += prefs.disambiguationTonicBonus;
    }
    if (bHasTonic && !aHasTonic) {
        evalB.score += prefs.disambiguationTonicBonus;
    }
}

/// Returns true if @p candidate is compatible with @p declared.
///
/// The engraving KeyMode has two levels of specificity:
///   - Ionian / Aeolian used as class-level declarations ("major" / "minor"):
///     any mode in the same class is compatible.
///   - Any other specific mode: only an exact match is compatible.
///
/// Rationale: key signatures in common practice are declared as "major" or
/// "minor", which constrains the class but leaves the specific mode (Dorian,
/// Phrygian, Aeolian, …) to pitch analysis.  Explicit modal declarations
/// (e.g. Dorian) mean exactly that mode.
bool modeIsCompatibleWithDeclared(KeyMode candidate, KeyMode declared)
{
    if (declared == KeyMode::Ionian) {
        // Class-level "major" declaration: accept any major-class mode
        return keyModeIsMajor(candidate);
    }
    if (declared == KeyMode::Aeolian) {
        // Class-level "minor" declaration: accept any minor-class mode
        return !keyModeIsMajor(candidate);
    }
    // Specific mode declared: require exact match
    return candidate == declared;
}

} // anonymous namespace

// ── Public API ───────────────────────────────────────────────────────────────

std::vector<KeyModeAnalysisResult> KeyModeAnalyzer::analyzeKeyMode(
    const std::vector<PitchContext>& pitches,
    int keySignatureFifths,
    const KeyModeAnalyzerPreferences& prefs,
    std::optional<KeyMode> declaredMode)
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
        // Tonic-level scores (independent of mode — compute once per tonic).
        const double ltScore     = scoreTrueLeadingTone(tonicPc, pitches, prefs);

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
            const double charScore  = scoreCharacteristicPitch(tonicPc, modeIndex, pitches, prefs);
            const double priorScore = scoreModePrior(modeIndex, prefs);
            eval.score           = eval.scaleScore + eval.triadScore + eval.keySignatureScore
                                 + charScore + ltScore + priorScore;

            // Declared-mode penalty: modes outside the declared class are penalised.
            if (declaredMode.has_value()) {
                const KeyMode candidate = keyModeFromIndex(modeIndex);
                if (!modeIsCompatibleWithDeclared(candidate, *declaredMode)) {
                    eval.score -= prefs.declaredModePenalty;
                }
            }
        }
    }

    // Apply post-hoc disambiguation to the top-2 scoring modes sharing the
    // key signature.  Extending disambiguation to all 21 pairs inflates absolute
    // scores disproportionately (every additional tonic-bearing mode reduces the
    // winner's accumulated bonus, making scores unstable).  Restricting to the
    // top-2 keeps the disambiguation focused on the decision boundary that
    // actually matters.
    if (keySignatureFifths >= -7 && keySignatureFifths <= 7) {
        const int matchingIonianPc = ionianTonicPcFromFifths(keySignatureFifths);

        // Find top-2 modes by raw score (before disambiguation).
        struct ModeEntry { int tonicPc; size_t modeSlot; double score; };
        std::array<ModeEntry, 7> entries;
        for (size_t slot = 0; slot < numModeSlots; ++slot) {
            const size_t mIdx = ACTIVE_MODE_INDICES[slot];
            const int tpc = (matchingIonianPc + keyModeTonicOffset(keyModeFromIndex(mIdx))) % 12;
            const double s = evaluations[static_cast<size_t>(tpc) * numModeSlots + slot].score;
            entries[slot] = { tpc, slot, s };
        }
        std::sort(entries.begin(), entries.end(),
                  [](const ModeEntry& a, const ModeEntry& b) { return a.score > b.score; });

        CandidateEvaluation& evalA = evaluations[
            static_cast<size_t>(entries[0].tonicPc) * numModeSlots + entries[0].modeSlot];
        CandidateEvaluation& evalB = evaluations[
            static_cast<size_t>(entries[1].tonicPc) * numModeSlots + entries[1].modeSlot];
        applyPairwiseDisambiguation(evalA, evalB, prefs);
    }

    // Select the best candidate.
    //
    // When the key signature is within the valid range [-7, 7], compare all modes
    // that share that key signature using the focussed tonal-centre formula, then
    // pick the one with the best combined score.  Out-of-range key signatures fall
    // back to the global highest-scoring candidate.
    int bestTonicPc    = 0;
    size_t bestModeSlot = 0;
    double bestScore   = -std::numeric_limits<double>::infinity();

    if (keySignatureFifths >= -7 && keySignatureFifths <= 7) {
        const int keySigIonianTonicPc = ionianTonicPcFromFifths(keySignatureFifths);

        // Compare all modes sharing this key signature via tonal-centre score.
        double bestCenterScore = -std::numeric_limits<double>::infinity();
        for (size_t modeSlot = 0; modeSlot < numModeSlots; ++modeSlot) {
            const size_t modeIndex = ACTIVE_MODE_INDICES[modeSlot];
            const int tonicPc = (keySigIonianTonicPc + keyModeTonicOffset(keyModeFromIndex(modeIndex))) % 12;
            const CandidateEvaluation& eval = evaluations[static_cast<size_t>(tonicPc) * numModeSlots + modeSlot];
            const double center = tonalCenterScore(eval, prefs);
            // Use tonal-centre score as primary, raw score as tiebreaker.
            if (center > bestCenterScore + prefs.tonalCenterDeltaThreshold
                || (std::abs(center - bestCenterScore) <= prefs.tonalCenterDeltaThreshold
                    && eval.score > bestScore))
            {
                bestCenterScore = center;
                bestScore    = eval.score;
                bestTonicPc  = tonicPc;
                bestModeSlot = modeSlot;
            }
        }
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
    best.mode    = keyModeFromIndex(bestModeIndex);
    best.tonicPc = bestTonicPc;
    best.score   = bestScore;
    results.push_back(best);

    for (const RawCandidate& c : allCandidates) {
        if (results.size() >= 3) {
            break;
        }
        const size_t modeIndex = ACTIVE_MODE_INDICES[c.modeSlot];
        const int fifths = resolveToFifths(c.tonicPc, modeIndex, keySignatureFifths);
        const KeyMode mode = keyModeFromIndex(modeIndex);
        if (fifths == best.keySignatureFifths && mode == best.mode) {
            continue;  // already added as the winner
        }
        KeyModeAnalysisResult r;
        r.keySignatureFifths = fifths;
        r.mode    = mode;
        r.tonicPc = c.tonicPc;
        r.score   = c.score;
        results.push_back(r);
    }

    // ── Compute normalized confidence ────────────────────────────────────
    //
    // Maps the score gap between top-1 and top-2 through a sigmoid to produce
    // a 0.0–1.0 value.  A large gap means the winner is clearly dominant; a
    // small gap means the result is ambiguous.  When only one candidate exists,
    // confidence is based on the winner's score vs. zero.
    if (!results.empty()) {
        const double winnerScore = results.front().score;
        const double runnerUpScore = (results.size() >= 2) ? results[1].score : 0.0;
        const double gap = winnerScore - runnerUpScore;
        const double confidence = 1.0 / (1.0 + std::exp(-prefs.confidenceSigmoidSteepness
                                                          * (gap - prefs.confidenceSigmoidMidpoint)));
        for (size_t i = 0; i < results.size(); ++i) {
            // Winner gets the computed confidence; runners-up get proportionally less
            if (i == 0) {
                results[i].normalizedConfidence = confidence;
            } else {
                const double iGap = results[i].score - ((i + 1 < results.size()) ? results[i + 1].score : 0.0);
                results[i].normalizedConfidence = 1.0 / (1.0 + std::exp(-prefs.confidenceSigmoidSteepness
                                                                         * (iGap - prefs.confidenceSigmoidMidpoint)));
            }
        }
    }

    return results;
}

// ── Display helpers ─────────────────────────────────────────────────────────

const char* keyModeTonicName(int fifths, KeyMode mode)
{
    // Tonic names indexed by circle-of-fifths position +7, per mode.
    static constexpr const char* IONIAN_NAMES[15] = {
        "Cb", "Gb", "Db", "Ab", "Eb", "Bb", "F",
        "C", "G", "D", "A", "E", "B", "F#", "C#"
    };
    static constexpr const char* AEOLIAN_NAMES[15] = {
        "Ab", "Eb", "Bb", "F", "C", "G", "D",
        "A", "E", "B", "F#", "C#", "G#", "D#", "A#"
    };
    // Dorian tonic = Ionian tonic + 2 fifths on the circle of fifths.
    static constexpr const char* DORIAN_NAMES[15] = {
        "Db", "Ab", "Eb", "Bb", "F", "C", "G",
        "D", "A", "E", "B", "F#", "C#", "G#", "D#"
    };
    // Phrygian tonic = Ionian tonic + 4 fifths on the circle of fifths.
    static constexpr const char* PHRYGIAN_NAMES[15] = {
        "Eb", "Bb", "F", "C", "G", "D", "A",
        "E", "B", "F#", "C#", "G#", "D#", "A#", "E#"
    };
    static constexpr const char* LYDIAN_NAMES[15] = {
        "Fb", "Cb", "Gb", "Db", "Ab", "Eb", "Bb",
        "F", "C", "G", "D", "A", "E", "B", "F#"
    };
    static constexpr const char* MIXOLYDIAN_NAMES[15] = {
        "Gb", "Db", "Ab", "Eb", "Bb", "F", "C",
        "G", "D", "A", "E", "B", "F#", "C#", "G#"
    };
    // Locrian tonic = Ionian tonic + 5 fifths on the circle of fifths.
    static constexpr const char* LOCRIAN_NAMES[15] = {
        "Bb", "F", "C", "G", "D", "A", "E",
        "B", "F#", "C#", "G#", "D#", "A#", "E#", "B#"
    };

    const int idx = std::clamp(fifths + 7, 0, 14);
    switch (mode) {
    case KeyMode::Ionian:     return IONIAN_NAMES[idx];
    case KeyMode::Dorian:     return DORIAN_NAMES[idx];
    case KeyMode::Phrygian:   return PHRYGIAN_NAMES[idx];
    case KeyMode::Lydian:     return LYDIAN_NAMES[idx];
    case KeyMode::Mixolydian: return MIXOLYDIAN_NAMES[idx];
    case KeyMode::Aeolian:    return AEOLIAN_NAMES[idx];
    case KeyMode::Locrian:    return LOCRIAN_NAMES[idx];
    }
    return IONIAN_NAMES[idx];
}

const char* keyModeSuffix(KeyMode mode)
{
    switch (mode) {
    case KeyMode::Ionian:     return "maj";
    case KeyMode::Dorian:     return "Dor";
    case KeyMode::Phrygian:   return "Phryg";
    case KeyMode::Lydian:     return "Lyd";
    case KeyMode::Mixolydian: return "Mixolyd";
    case KeyMode::Aeolian:    return "min";
    case KeyMode::Locrian:    return "Loc";
    }
    return "";
}

} // namespace mu::composing::analysis
