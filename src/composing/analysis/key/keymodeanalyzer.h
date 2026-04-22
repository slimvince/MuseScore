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

#include "../chord/analysisutils.h"

namespace mu::composing::analysis {

/// The mode of a key.  All 21 modes (7 diatonic + 7 melodic minor + 7 harmonic minor)
/// are evaluated.
///
/// Enum ordinal == index into the MODES interval table in keymodeanalyzer.cpp.
/// Diatonic modes (0–6) come first so existing code casting to/from size_t is unaffected.
enum class KeySigMode {
    // ── Diatonic modes ────────────────────────────────────────────────────
    Ionian,       ///< Major (0 2 4 5 7 9 11)
    Dorian,       ///<       (0 2 3 5 7 9 10)
    Phrygian,     ///<       (0 1 3 5 7 8 10)
    Lydian,       ///<       (0 2 4 6 7 9 11)
    Mixolydian,   ///<       (0 2 4 5 7 9 10)
    Aeolian,      ///< Natural minor (0 2 3 5 7 8 10)
    Locrian,      ///<       (0 1 3 5 6 8 10)

    // ── Melodic minor family ──────────────────────────────────────────────
    MelodicMinor,     ///< Ascending melodic minor / jazz minor (0 2 3 5 7 9 11)
    DorianB2,         ///< Phrygian #6 (0 1 3 5 7 9 10)
    LydianAugmented,  ///< Lydian #5 (0 2 4 6 8 9 11)
    LydianDominant,   ///< Lydian b7 (0 2 4 6 7 9 10)
    MixolydianB6,     ///< Mixolydian b6 (0 2 4 5 7 8 10)
    AeolianB5,        ///< Locrian #2 (0 2 3 5 6 8 10)
    Altered,          ///< Altered / Super Locrian (0 1 3 4 6 8 10)

    // ── Harmonic minor family ─────────────────────────────────────────────
    HarmonicMinor,     ///< Natural minor #7 (0 2 3 5 7 8 11)
    LocrianSharp6,     ///< Locrian #6 (0 1 3 5 6 9 10)
    IonianSharp5,      ///< Major #5 (0 2 4 5 8 9 11)
    DorianSharp4,      ///< Dorian #4 (0 2 3 6 7 9 10)
    PhrygianDominant,  ///< Phrygian #3 / harmonic dominant (0 1 4 5 7 8 10)
    LydianSharp2,      ///< Lydian #2 (0 3 4 6 7 9 11)
    AlteredDomBB7,     ///< Harmonic minor mode 7 (0 1 3 4 6 8 9)
};

/// Total number of KeySigMode values.
inline constexpr size_t KEY_MODE_COUNT = 21;

/// Index of a KeySigMode value in the mode table (same as its enum ordinal).
inline constexpr size_t keyModeIndex(KeySigMode m) { return static_cast<size_t>(m); }

/// Convert a mode table index back to a KeySigMode enum value.
inline constexpr KeySigMode keyModeFromIndex(size_t idx) { return static_cast<KeySigMode>(idx); }

/// Returns true for modes with a major third (interval 4 from tonic).
///
/// Diatonic: Ionian, Lydian, Mixolydian.
/// Melodic minor: LydianAugmented, LydianDominant, MixolydianB6.
/// Harmonic minor: IonianSharp5, PhrygianDominant, LydianSharp2.
inline constexpr bool keyModeIsMajor(KeySigMode m) {
    switch (m) {
    case KeySigMode::Ionian:
    case KeySigMode::Lydian:
    case KeySigMode::Mixolydian:
    case KeySigMode::LydianAugmented:
    case KeySigMode::LydianDominant:
    case KeySigMode::MixolydianB6:
    case KeySigMode::IonianSharp5:
    case KeySigMode::PhrygianDominant:
    case KeySigMode::LydianSharp2:
        return true;
    default:
        return false;
    }
}

/// Semitone offset of this mode's tonic from the Ionian tonic of the associated
/// key signature.  For diatonic modes: the standard church-mode offsets.
/// For non-diatonic modes: the offset of the mode's tonic from the Ionian tonic
/// of the parent key (e.g. MelodicMinor shares Dorian's offset = 2).
inline constexpr int keyModeTonicOffset(KeySigMode m) {
    constexpr int offsets[] = {
        // Diatonic (0–6)
        0, 2, 4, 5, 7, 9, 11,
        // Melodic minor family (7–13) — parent key = Bb major for C root
        2,   ///< MelodicMinor   ~ Dorian
        4,   ///< DorianB2       ~ Phrygian
        5,   ///< LydianAugmented ~ Lydian
        7,   ///< LydianDominant  ~ Mixolydian
        9,   ///< MixolydianB6   ~ Aeolian
        11,  ///< AeolianB5      ~ Locrian
        1,   ///< Altered        ~ mode-7 of melodic minor (1 above Ionian)
        // Harmonic minor family (14–20) — parent key = C major for A root
        9,   ///< HarmonicMinor  ~ Aeolian
        11,  ///< LocrianSharp6  ~ Locrian
        0,   ///< IonianSharp5   ~ Ionian
        2,   ///< DorianSharp4   ~ Dorian
        4,   ///< PhrygianDominant ~ Phrygian
        5,   ///< LydianSharp2   ~ Lydian
        8,   ///< AlteredDomBB7  ~ aug5 above Ionian (unique — no diatonic equivalent)
    };
    return offsets[static_cast<size_t>(m)];
}

/// Result of a key/mode analysis: the most likely key and mode with a confidence score.
struct KeyModeAnalysisResult {
    int keySignatureFifths = 0;          ///< Resolved key signature (-7..+7, Ionian convention)
    KeySigMode mode = KeySigMode::Ionian;      ///< Detected mode
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

    // ── Mode priors (frequency bias) ────────────────────────────────────────
    //
    // One independent prior per mode.  Additive bias applied to every (tonicPc,
    // modeSlot) candidate.  A small prior prevents rare modes winning when pitch
    // evidence is ambiguous.  Defaults reflect the "Standard (classical)" preset.
    // The bridge overrides these from user preferences (21 independent sliders /
    // named presets) when available.  The former +0.2 Ionian internal offset is
    // now absorbed into the explicit Ionian prior (1.2) vs Aeolian prior (1.0).

    // Diatonic modes
    double modePriorIonian          =  1.20;  ///< [empirical — was tier1+0.2]
    double modePriorDorian          = -0.50;  ///< [empirical]
    double modePriorPhrygian        = -1.50;  ///< [empirical]
    double modePriorLydian          = -1.50;  ///< [empirical]
    double modePriorMixolydian      = -0.50;  ///< [empirical]
    double modePriorAeolian         =  1.00;  ///< [empirical — was tier1]
    double modePriorLocrian         = -3.00;  ///< [empirical]

    // Melodic minor family
    double modePriorMelodicMinor    = -0.50;  ///< [empirical]
    double modePriorDorianB2        = -1.50;  ///< [empirical]
    double modePriorLydianAugmented  = -2.00;  ///< [empirical]
    double modePriorLydianDominant   = -1.00;  ///< [empirical]
    double modePriorMixolydianB6    = -1.50;  ///< [empirical]
    double modePriorAeolianB5       = -2.50;  ///< [empirical]
    double modePriorAltered         = -3.50;  ///< [empirical]

    // Harmonic minor family
    double modePriorHarmonicMinor   = -0.30;  ///< [empirical]
    double modePriorLocrianSharp6   = -2.50;  ///< [empirical]
    double modePriorIonianSharp5    = -2.00;  ///< [empirical]
    double modePriorDorianSharp4    = -2.00;  ///< [empirical]
    double modePriorPhrygianDominant = -0.80;  ///< [empirical]
    double modePriorLydianSharp2    = -2.50;  ///< [empirical]
    double modePriorAlteredDomBB7   = -3.50;  ///< [empirical]

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

    /// Returns the valid range for every numeric scoring parameter.
    ///
    /// Parameters marked isManual=true are wired to user-visible preferences or
    /// have narrow hand-tuned sweet-spots; automated optimizers should leave them
    /// fixed.  Parameters marked isManual=false are safe for gradient-based or
    /// grid-search tuning.
    ///
    /// Integer parameters (dynamicLookaheadStepBeats, dynamicLookaheadMaxBeats)
    /// are omitted; they require integer-aware optimizers and are unlikely to
    /// benefit from fine-grained tuning.
    ParameterBoundsMap bounds() const
    {
        return {
            // Evidence weight caps
            { "noteWeightCap",                     { 1.0,  6.0 } },
            { "bassMultiplier",                    { 1.0,  4.0 } },
            // Scale membership scoring
            { "scaleScoreInBoth",                  { 0.5,  2.0 } },
            { "scaleScoreInCandidateOnly",         { 0.0,  1.0 } },
            { "scaleScoreInKeySigOnly",            {-1.0,  0.0 } },
            { "scaleScoreInNeither",               {-0.5,  0.0 } },
            // Tonal centre scoring
            { "tonicWeight",                       { 0.5,  3.0 } },
            { "thirdWeight",                       { 0.0,  2.0 } },
            { "fifthWeight",                       { 0.0,  2.0 } },
            { "leadingToneWeight",                 { 0.0,  1.5 } },
            { "completeTriadBonus",                { 0.5,  5.0 } },
            { "missingTonicPenalty",               {-5.0, -0.5 } },
            { "extraScaleFactor",                  { 0.0,  0.5 } },
            { "extraScaleCap",                     { 1.0, 10.0 } },
            // Characteristic pitch scoring
            { "characteristicPitchBoost",          { 0.5,  4.0 } },
            { "characteristicPitchPenalty",        {-2.0,  0.0 } },
            // Leading tone
            { "trueLeadingToneBoost",              { 0.0,  3.0 } },
            // Mode priors — isManual because each slider maps to a user preference
            { "modePriorIonian",        { -5.0, 5.0, true } },
            { "modePriorDorian",        { -5.0, 5.0, true } },
            { "modePriorPhrygian",      { -5.0, 5.0, true } },
            { "modePriorLydian",        { -5.0, 5.0, true } },
            { "modePriorMixolydian",    { -5.0, 5.0, true } },
            { "modePriorAeolian",       { -5.0, 5.0, true } },
            { "modePriorLocrian",       { -5.0, 5.0, true } },
            { "modePriorMelodicMinor",  { -5.0, 5.0, true } },
            { "modePriorDorianB2",      { -5.0, 5.0, true } },
            { "modePriorLydianAugmented", { -5.0, 5.0, true } },
            { "modePriorLydianDominant",  { -5.0, 5.0, true } },
            { "modePriorMixolydianB6",  { -5.0, 5.0, true } },
            { "modePriorAeolianB5",     { -5.0, 5.0, true } },
            { "modePriorAltered",       { -5.0, 5.0, true } },
            { "modePriorHarmonicMinor", { -5.0, 5.0, true } },
            { "modePriorLocrianSharp6", { -5.0, 5.0, true } },
            { "modePriorIonianSharp5",  { -5.0, 5.0, true } },
            { "modePriorDorianSharp4",  { -5.0, 5.0, true } },
            { "modePriorPhrygianDominant", { -5.0, 5.0, true } },
            { "modePriorLydianSharp2",  { -5.0, 5.0, true } },
            { "modePriorAlteredDomBB7", { -5.0, 5.0, true } },
            // Tonal centre comparison
            { "tonalCenterTonicWeight",            { 0.5,  4.0 } },
            { "tonalCenterThirdWeight",            { 0.0,  2.0 } },
            { "tonalCenterFifthWeight",            { 0.0,  2.0 } },
            { "tonalCenterLeadingTone",            { 0.0,  1.5 } },
            { "tonalCenterTriadBonus",             { 0.5,  5.0 } },
            { "tonalCenterDeltaThreshold",         { 0.0,  1.0 } },
            // Key-signature proximity
            { "keySignatureDistancePenalty",       { 0.0,  2.0 } },
            // Relative pair disambiguation
            { "disambiguationTriadBonus",          { 1.0,  8.0 } },
            { "disambiguationTriadCost",           { 0.0,  4.0 } },
            { "disambiguationTonicBonus",          { 0.0,  3.0 } },
            // Declared-mode penalty — isManual: user may override
            { "declaredModePenalty",               { 3.0, 15.0, true } },
            // Confidence sigmoid
            { "confidenceSigmoidMidpoint",         { 0.5,  5.0 } },
            { "confidenceSigmoidSteepness",        { 0.5,  5.0 } },
            // Dynamic lookahead threshold
            { "dynamicLookaheadConfidenceThreshold",{ 0.3, 0.9 } },
            // Hysteresis margins — isManual: tightly coupled to user experience
            { "hysteresisMargin",                  { 0.5,  5.0, true } },
            { "relativeKeyHysteresisMargin",       { 0.5,  8.0, true } },
            // Beat weights
            { "beatWeightDownbeat",                { 0.5,  2.0 } },
            { "beatWeightCompoundStressed",        { 0.3,  1.5 } },
            { "beatWeightSimpleStressed",          { 0.3,  1.5 } },
            { "beatWeightCompoundUnstressed",      { 0.1,  1.0 } },
            { "beatWeightSimpleUnstressed",        { 0.1,  1.0 } },
            { "beatWeightCompoundSubbeat",         { 0.0,  0.5 } },
            { "beatWeightSubbeat",                 { 0.0,  0.5 } },
        };
    }
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
        std::optional<KeySigMode> declaredMode = std::nullopt);
};

/// Scale degrees (semitone offsets from tonic) for every mode defined
/// by KeySigMode. Indexed by keyModeIndex(mode). Size is always 7 even
/// for modes whose scale has fewer distinct pitch classes — the table
/// expresses the canonical diatonic mapping used for Roman-numeral
/// degree lookup.
const std::array<int, 7>& keyModeScaleIntervals(KeySigMode mode);

/// Maps a modal tonic pitch class to the equivalent Ionian tonic that shares
/// the same key signature.  Defined in keymodeanalyzer.cpp; exposed here so the
/// intonation module can convert a KeyModeAnalysisResult back to an Ionian tonic
/// without depending on the full analyzeKeyMode implementation.
int ionianTonicPcForMode(int tonicPc, size_t modeIndex);

/// Human-readable tonic name for a (key-signature, mode) pair.
/// E.g. keyModeTonicName(0, KeySigMode::Ionian) → "C",
///      keyModeTonicName(0, KeySigMode::Dorian) → "D",
///      keyModeTonicName(-3, KeySigMode::Aeolian) → "C".
const char* keyModeTonicName(int fifths, KeySigMode mode);

/// Human-readable mode suffix for display.
/// E.g. KeySigMode::Ionian → "major", KeySigMode::Dorian → "Dorian".
const char* keyModeSuffix(KeySigMode mode);

} // namespace mu::composing::analysis
