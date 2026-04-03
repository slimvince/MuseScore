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
#pragma once

#include <optional>
#include <vector>

namespace mu::composing::analysis {

/// The mode of a key.  All seven diatonic modes are evaluated.
///
/// Replacing the old `bool isMajor` with an explicit enum makes modal
/// extensions non-breaking at the call site.
enum class KeyMode {
    Ionian,       ///< Major
    Dorian,
    Phrygian,
    Lydian,
    Mixolydian,
    Aeolian,      ///< Natural minor
    Locrian,
};

/// Number of entries in the KeyMode enum.
inline constexpr size_t KEY_MODE_COUNT = 7;

/// Index of a KeyMode value in the mode table (same as its enum ordinal).
inline constexpr size_t keyModeIndex(KeyMode m) { return static_cast<size_t>(m); }

/// Convert a mode table index back to a KeyMode enum value.
inline constexpr KeyMode keyModeFromIndex(size_t idx) { return static_cast<KeyMode>(idx); }

/// Returns true for modes with a major third (Ionian, Lydian, Mixolydian).
inline constexpr bool keyModeIsMajor(KeyMode m) {
    return m == KeyMode::Ionian || m == KeyMode::Lydian || m == KeyMode::Mixolydian;
}

/// Semitone offset from the Ionian tonic to this mode's tonic within the same
/// key signature.  E.g. Dorian = 2 (D Dorian shares the key signature of C Ionian).
inline constexpr int keyModeTonicOffset(KeyMode m) {
    constexpr int offsets[] = { 0, 2, 4, 5, 7, 9, 11 };
    return offsets[static_cast<size_t>(m)];
}

/// Result of a key/mode analysis: the most likely key and mode with a confidence score.
struct KeyModeAnalysisResult {
    int keySignatureFifths = 0;          ///< Resolved key signature (-7..+7, Ionian convention)
    KeyMode mode = KeyMode::Ionian;      ///< Detected mode
    int tonicPc = 0;                     ///< Pitch class of the mode's tonic (0=C, 2=D, etc.)
    double score = 0.0;                  ///< Raw confidence score; higher is better
    double normalizedConfidence = 0.0;   ///< 0.0–1.0 confidence (see §5.7)

    /// Convenience: true when mode has a major third (Ionian, Lydian, Mixolydian).
    bool isMajor() const { return keyModeIsMajor(mode); }
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

    // ── Characteristic pitch scoring ────────────────────────────────────────
    //
    // Each mode has a single pitch that most distinguishes it from its closest
    // neighbor (e.g. Dorian's raised 6th vs Aeolian).  The presence of this
    // pitch boosts the candidate; its absence penalizes it.  Both the boost
    // and penalty values are empirical.

    double characteristicPitchBoost   = 1.80;  ///< Boost when characteristic pitch is present [empirical]
    double characteristicPitchPenalty = -0.60;  ///< Penalty when characteristic pitch is absent [empirical]

    // ── True leading-tone scoring ──────────────────────────────────────────
    //
    // The note a semitone below the tonic ((tonicPc + 11) % 12) is the
    // strongest tonal indicator in Western music.  Its presence boosts the
    // candidate regardless of whether it is diatonic to the mode (chromatic
    // leading tones, as in harmonic minor, still indicate the tonic).
    // This complements the mode-specific 7th-degree evidence in triad scoring.

    double trueLeadingToneBoost = 1.20;  ///< Bonus when semitone-below-tonic is present [empirical]

    // ── Mode prior (frequency bias) ─────────────────────────────────────────
    //
    // In real-world music, Ionian and Aeolian are vastly more common than
    // the other diatonic modes.  A small additive prior prevents rare modes
    // (Lydian, Locrian, etc.) from winning when the pitch evidence is
    // ambiguous.  The ordering is theory-grounded (Ionian/Aeolian >> Dorian/
    // Mixolydian > Phrygian/Lydian > Locrian); the absolute values are
    // empirical.

    // Default values match the "Standard" preset (T1=+1.0, T2=-0.5, T3=-1.5, T4=-3.0).
    // The bridge overrides these from user preferences when available.
    double modePriorIonian     =  1.20;  ///< Tier 1 (+1.0) + 0.2 internal offset [empirical]
    double modePriorAeolian    =  1.00;  ///< Tier 1 (+1.0) [empirical]
    double modePriorDorian     = -0.50;  ///< Tier 2 (-0.5) [empirical]
    double modePriorMixolydian = -0.50;  ///< Tier 2 (-0.5) [empirical]
    double modePriorLydian     = -1.50;  ///< Tier 3 (-1.5) [empirical]
    double modePriorPhrygian   = -1.50;  ///< Tier 3 (-1.5) [empirical]
    double modePriorLocrian    = -3.00;  ///< Tier 4 (-3.0) [empirical]

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

    // ── Declared-mode penalty ────────────────────────────────────────────────
    //
    // When the caller provides a declared mode (e.g. from the score's key
    // signature), any candidate mode outside the declared mode class receives
    // this additive penalty.  The value is chosen to be decisive for common
    // relative-major/minor ambiguities (larger than disambiguationTriadBonus)
    // while still theoretically overridable by very strong opposing pitch
    // evidence.  A higher value reflecting full trust in the composer's
    // declaration is tracked as a backlog item.

    double declaredModePenalty = 7.0;  ///< Penalty for modes outside the declared class [empirical]

    // ── Beat-type weights for temporal window collection ─────────────────
    //
    // Mapping from MuseScore's BeatType enum to a weight applied during
    // pitch context collection.  The ordering (downbeat > stressed >
    // unstressed > subbeat) is theory-grounded; the specific values are
    // empirical — not derived from any measurement.

    // ── Normalized confidence mapping ──────────────────────────────────────
    //
    // The raw score gap between the top-1 and top-2 candidates is mapped to
    // a 0.0–1.0 confidence value through a sigmoid: 1 / (1 + exp(-k * (gap - midpoint))).
    // The midpoint is the gap value that maps to 0.5 confidence.
    // The steepness controls how quickly confidence rises with increasing gap.
    // Both values are empirical.

    double confidenceSigmoidMidpoint  = 2.0;   ///< Gap at which confidence = 0.5 [empirical]
    double confidenceSigmoidSteepness = 1.5;   ///< Rate of confidence rise [empirical]

    // ── Dynamic lookahead ─────────────────────────────────────────────────
    //
    // When confidence after the initial fixed lookahead is below
    // dynamicLookaheadConfidenceThreshold, the lookahead window is expanded by
    // dynamicLookaheadStepBeats per iteration up to dynamicLookaheadMaxBeats.
    // Each expansion re-collects pitch context and re-runs the analyzer.
    // Lives in the bridge / batch_analyze caller, not in analyzeKeyMode itself.
    // Theory-grounded ordering (expanding beats); values are empirical.

    double dynamicLookaheadConfidenceThreshold = 0.60; ///< Stop expanding when confidence ≥ this [empirical]
    int    dynamicLookaheadStepBeats            = 2;    ///< Beats added per expansion step [empirical]
    int    dynamicLookaheadMaxBeats             = 24;   ///< Hard cap on lookahead [empirical]

    // ── Mode-switching hysteresis ─────────────────────────────────────────
    //
    // When the inferred mode differs from the previous inference at a nearby
    // tick, the challenger must exceed the incumbent's score by this margin to
    // cause a switch.  Prevents thin transient evidence from triggering
    // spurious modulations.
    // Lives in the bridge / batch_analyze caller; not used inside analyzeKeyMode.

    double hysteresisMargin = 2.0;  ///< Score advantage required to switch modes when key sigs differ [empirical]

    /// Higher hysteresis applied when the challenger shares the same key signature
    /// as the incumbent (relative major/minor pair, e.g. D minor ↔ F major).
    /// These pairs are structurally ambiguous — all diatonic notes are shared —
    /// so a larger margin is needed to avoid spurious switches on passing chords.
    double relativeKeyHysteresisMargin = 2.0;  ///< Same-key-sig switch barrier [empirical, = hysteresisMargin by default]

    // ── Beat-type weights for temporal window collection ─────────────────
    //
    // Mapping from MuseScore's BeatType enum to a weight applied during
    // pitch context collection.  The ordering (downbeat > stressed >
    // unstressed > subbeat) is theory-grounded; the specific values are
    // empirical — not derived from any measurement.

    double beatWeightDownbeat            = 1.0;  ///< [empirical]
    double beatWeightCompoundStressed    = 0.7;  ///< [empirical]
    double beatWeightSimpleStressed      = 0.7;  ///< [empirical]
    double beatWeightCompoundUnstressed  = 0.4;  ///< [empirical]
    double beatWeightSimpleUnstressed    = 0.4;  ///< [empirical]
    double beatWeightCompoundSubbeat     = 0.2;  ///< [empirical]
    double beatWeightSubbeat             = 0.2;  ///< [empirical]
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
    /// @param declaredMode  If set, modes outside this mode's class receive
    ///                      a penalty (prefs.declaredModePenalty).  Pass
    ///                      std::nullopt (the default) to use pure pitch
    ///                      analysis with no constraint.
    static std::vector<KeyModeAnalysisResult> analyzeKeyMode(
        const std::vector<PitchContext>& pitches,
        int keySignatureFifths,
        const KeyModeAnalyzerPreferences& prefs = kDefaultKeyModeAnalyzerPreferences,
        std::optional<KeyMode> declaredMode = std::nullopt);
};

/// Maps a modal tonic pitch class to the equivalent Ionian tonic that shares
/// the same key signature.  Defined in keymodeanalyzer.cpp; exposed here so the
/// intonation module can convert a KeyModeAnalysisResult back to an Ionian tonic
/// without depending on the full analyzeKeyMode implementation.
int ionianTonicPcForMode(int tonicPc, size_t modeIndex);

/// Human-readable tonic name for a (key-signature, mode) pair.
/// E.g. keyModeTonicName(0, KeyMode::Ionian) → "C",
///      keyModeTonicName(0, KeyMode::Dorian) → "D",
///      keyModeTonicName(-3, KeyMode::Aeolian) → "C".
const char* keyModeTonicName(int fifths, KeyMode mode);

/// Human-readable mode suffix for display.
/// E.g. KeyMode::Ionian → "major", KeyMode::Dorian → "Dorian".
const char* keyModeSuffix(KeyMode mode);

} // namespace mu::composing::analysis
