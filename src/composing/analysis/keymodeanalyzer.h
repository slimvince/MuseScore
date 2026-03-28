
namespace mu::composing::analysis {
// Returns the tonic pitch class (0 = C, 1 = C#, ..., 11 = B) for a given tonic pitch class and mode index.
// Used for mapping key signature and mode to tonic for key-dependent intonation systems.
int ionianTonicPcForMode(int tonicPc, size_t modeIndex);
}
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

#ifndef MU_COMPOSING_ANALYSIS_KEYMODEANALYZER_H
#define MU_COMPOSING_ANALYSIS_KEYMODEANALYZER_H

#include <vector>

namespace mu::composing::analysis {

/// The mode of a key.  Currently only Ionian (major) and Aeolian (natural minor)
/// are actively evaluated; the full modal table is kept in keymodeanalyzer.cpp for
/// future re-enablement without interface changes.
///
/// Replacing the old `bool isMajor` with an explicit enum makes future modal
/// extensions (Dorian, Phrygian, etc.) non-breaking at the call site.
enum class KeyMode {
    Ionian,       ///< Major / Ionian
    Aeolian,      ///< Natural minor / Aeolian
    // Future: Dorian, Phrygian, Lydian, Mixolydian, Locrian
};

/// Result of a key/mode analysis: the most likely key and mode with a confidence score.
struct KeyModeAnalysisResult {
    int keySignatureFifths = 0;          ///< Resolved key signature (-7..+7, Ionian convention)
    KeyMode mode = KeyMode::Ionian;      ///< Detected mode
    double score = 0.0;                  ///< Raw confidence score; higher is better
};

/// Tunable scoring weights for KeyModeAnalyzer.
///
/// All values are compile-time defaults.  Replace each initialiser with a lookup
/// from the settings store once user-preferences infrastructure is available.
struct KeyModeAnalyzerPreferences {

    // ── Evidence weight caps ─────────────────────────────────────────────────

    /// Maximum combined weight contributed by a single pitch.
    /// Prevents one very long note from dominating the analysis.
    double noteWeightCap = 3.0;          // [empirical]

    /// Multiplier applied when a note is the lowest-sounding pitch (bass).
    /// The bass voice carries disproportionate harmonic information.
    double bassMultiplier = 2.0;         // [theory-grounded ordering, empirical value]

    // ── Scale membership scoring ─────────────────────────────────────────────
    //
    // Each note is classified against two scales: the candidate key scale and
    // the notated key-signature scale.  The combination produces four cases;
    // in-scale/in-signature earns the most, out-of-both earns the least.
    // Ordering is theory-grounded; values are empirical.

    double scaleScoreInBoth    =  1.00;  ///< Note is in candidate scale AND key-sig scale [theory-grounded ordering]
    double scaleScoreInCandidateOnly = 0.25;  ///< In candidate scale but not key-sig scale [empirical]
    double scaleScoreInKeySigOnly    = -0.20; ///< In key-sig scale but not candidate (chromatic neighbour) [empirical]
    double scaleScoreInNeither       = -0.05; ///< Outside both scales [empirical]

    // ── Tonal centre scoring ─────────────────────────────────────────────────
    //
    // Weights for tonic, third, fifth, and leading-tone evidence.
    // The ordering (tonic > third > fifth > leading tone) is theory-grounded.
    // Within each weight, the absolute value is empirically tuned.

    double tonicWeight       = 1.60;  ///< Tonic note present [theory-grounded ordering, empirical value]
    double thirdWeight       = 0.70;  ///< Third (M3 for major, m3 for minor) [empirical]
    double fifthWeight       = 0.50;  ///< Perfect fifth [empirical]
    double leadingToneWeight = 0.40;  ///< Leading tone (tonicPc + 11, used for both modes) [empirical]

    double completeTriadBonus  =  2.50;  ///< All three triad notes present simultaneously [empirical]
    double missingTonicPenalty = -2.50;  ///< Tonic entirely absent [empirical]

    double extraScaleFactor    = 0.10;   ///< Per-unit weight of non-triad in-scale notes [empirical]
    double extraScaleCap       = 5.0;    ///< Cap on total extra-scale weight [empirical]

    // ── Tonal-centre comparison (relative pair disambiguation) ───────────────
    //
    // When the key signature is known, the relative major/minor pair is scored
    // by a focussed tonal-centre formula.  If the difference exceeds
    // tonalCenterDeltaThreshold, that candidate wins outright; otherwise the
    // raw score is used as the tiebreaker.
    //
    // tonalCenter* weights are independent of the main triad-score weights above
    // because this path runs AFTER the post-hoc disambiguation mutations (which
    // themselves use the main weights).  Keeping them separate lets both be tuned
    // without cross-interference.

    double tonalCenterTonicWeight  = 2.20;  ///< [empirical]
    double tonalCenterThirdWeight  = 1.00;  ///< [empirical]
    double tonalCenterFifthWeight  = 0.70;  ///< [empirical]
    double tonalCenterLeadingTone  = 0.50;  ///< [empirical]
    double tonalCenterTriadBonus   = 2.00;  ///< [empirical]
    double tonalCenterDeltaThreshold = 0.25; ///< Min delta to choose winner outright [empirical]

    // ── Key-signature proximity ──────────────────────────────────────────────
    //
    // Theory basis: when the notated key signature is known, candidate keys that
    // require more accidentals relative to the signature are penalised.  The
    // penalty grows linearly with the circle-of-fifths distance.  This is
    // theory-grounded; the per-step value is empirical.

    double keySignatureDistancePenalty = 0.60;  ///< Per circle-of-fifths step of distance [empirical]

    // ── Relative major/minor post-hoc mutations ──────────────────────────────
    //
    // After the main loop, the relative major/minor pair for each key is explicitly
    // disambiguated.  When one candidate has a complete tonic triad and the other
    // has no tonic note, a large boost (+ disambiguation bonus) and a small penalty
    // (- disambiguation cost) are applied.  When only one side has a tonic, a
    // smaller tonic-presence boost is applied.  Both are empirical.

    double disambiguationTriadBonus  = 4.50;  ///< One side has complete triad + tonic [empirical]
    double disambiguationTriadCost   = 1.50;  ///< Applied to the other side [empirical]
    double disambiguationTonicBonus  = 1.00;  ///< Only-tonic-present (no complete triad) [empirical]
};

/// Global default preferences.
inline constexpr KeyModeAnalyzerPreferences kDefaultKeyModeAnalyzerPreferences{};

class KeyModeAnalyzer
{
public:
    /// Pitch context passed from the score/notation layer into the abstract analysis.
    /// Carries duration and metric weight so longer, metrically-strong notes have more influence.
    struct PitchContext {
        int pitch = 0;               ///< MIDI pitch number
        double durationWeight = 1.0; ///< Duration in quarter-note units; larger = more influence
        double beatWeight = 1.0;     ///< Metric position: 1.0=downbeat, ~0.2=offbeat
        bool isBass = false;         ///< True if lowest sounding pitch at this time instant
    };

    /// Analyse key/mode from a window of pitch contexts and the local key signature.
    /// keySignatureFifths is the fixed-accidental context at the selection point (-7..+7).
    ///
    /// Returns up to 3 candidates sorted by score descending.  An empty result means
    /// insufficient pitch data to form a reliable estimate.
    static std::vector<KeyModeAnalysisResult> analyzeKeyMode(
        const std::vector<PitchContext>& pitches,
        int keySignatureFifths,
        const KeyModeAnalyzerPreferences& prefs = kDefaultKeyModeAnalyzerPreferences);
};

} // namespace mu::composing::analysis

#endif // MU_COMPOSING_ANALYSIS_KEYMODEANALYZER_H
