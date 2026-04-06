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

#include <memory>
#include <string>
#include <vector>

#include "analysisutils.h"
#include "../key/keymodeanalyzer.h"

namespace mu::composing::analysis {

enum class ChordQuality {
    Unknown,
    Major,
    Minor,
    Diminished,
    Augmented,
    HalfDiminished,
    Suspended2,
    Suspended4,
    Power
};

struct ChordAnalysisTone {
    int pitch = 0;      // MIDI playback pitch (ppitch — honours ottavas and transpositions)
    int tpc = -1;       // MuseScore TPC (0–34, circle-of-fifths spelling). -1 = not provided.
    double weight = 1;  // Relative evidence weight (future: populate from duration/beat)
    bool isBass = false;
};

// ── Extension bitmask ────────────────────────────────────────────────────────

/// Chord extension and alteration flags.  Stored as a bitmask in ChordIdentity.
/// Use hasExtension() / setExtension() rather than raw bit operations.
enum class Extension : uint32_t {
    MinorSeventh      = 1u << 0,   ///< b7 — minor seventh
    MajorSeventh      = 1u << 1,   ///< M7 — major seventh
    DiminishedSeventh = 1u << 2,   ///< dim7 (9 semitones) — Diminished quality only
    AddedSixth        = 1u << 3,   ///< Added sixth (no seventh)
    FlatNinth         = 1u << 4,   ///< b9
    NaturalNinth      = 1u << 5,   ///< Natural 9th (add9 / sus, or upper extension)
    SharpNinth        = 1u << 6,   ///< #9
    NaturalEleventh   = 1u << 7,   ///< 11th (sus4 or upper extension)
    SharpEleventh     = 1u << 8,   ///< #11 / Lydian dominant
    FlatThirteenth    = 1u << 9,   ///< b13
    NaturalThirteenth = 1u << 10,  ///< 13th
    SharpThirteenth   = 1u << 11,  ///< #13
    FlatFifth         = 1u << 12,  ///< b5 alteration
    SharpFifth        = 1u << 13,  ///< #5 alteration
    OmitsThird        = 1u << 14,  ///< No third present (power chord / open voicing)
    SixNine           = 1u << 15,  ///< 6/9 chord special case
};

inline bool hasExtension(uint32_t ext, Extension flag)
{
    return (ext & static_cast<uint32_t>(flag)) != 0;
}

inline bool hasAnyNinth(uint32_t ext)
{
    return hasExtension(ext, Extension::FlatNinth)
        || hasExtension(ext, Extension::NaturalNinth)
        || hasExtension(ext, Extension::SharpNinth);
}

inline bool hasAnyThirteenth(uint32_t ext)
{
    return hasExtension(ext, Extension::FlatThirteenth)
        || hasExtension(ext, Extension::NaturalThirteenth)
        || hasExtension(ext, Extension::SharpThirteenth);
}

inline void setExtension(uint32_t& ext, Extension flag)
{
    ext |= static_cast<uint32_t>(flag);
}

// ── ChordIdentity ─────────────────────────────────────────────────────────────

/// The pitch-content identity of a chord: root, quality, extensions, and bass.
/// Contains no key-function information.
struct ChordIdentity {
    double score = 0.0;       ///< Template match score (higher = better); ranking only.
    int rootPc = 0;           ///< Root pitch class (0–11)
    int bassPc = 0;           ///< Bass pitch class (0–11)
    int bassTpc = -1;         ///< Bass TPC for enharmonic-correct naming; -1 = unknown
    ChordQuality quality = ChordQuality::Unknown;
    uint32_t extensions = 0;  ///< Extension/alteration bitmask (see Extension enum)
};

// ── ChordFunction ─────────────────────────────────────────────────────────────

/// The tonal function of a chord within its key and mode context.
struct ChordFunction {
    int degree = -1;           ///< 0..6 when diatonic degree is known; -1 otherwise
    bool diatonicToKey = false;

    // Key context — stored so formatRomanNumeral() can generate chromatic
    // numerals (♭VII, ♭III, etc.) even when degree == -1 (non-diatonic root).
    int keyTonicPc = 0;
    KeySigMode keyMode = KeySigMode::Ionian;
};

// ── ChordAnalysisResult ───────────────────────────────────────────────────────

/// Abstract analysis result — contains only harmonic data, no formatting.
/// An empty result vector from analyzeChord() signals insufficient data.
struct ChordAnalysisResult {
    ChordIdentity identity;
    ChordFunction function;
};

/// Tunable parameters for chord analysis.
///
/// All values are compile-time defaults.  When MuseScore's user-preferences
/// infrastructure is wired in, replace each initialiser with a lookup from the
/// settings store.  Until then, tweak the constants here.
struct ChordAnalyzerPreferences {

    // ── Scoring weights ─────────────────────────────────────────────────────

    /// Added to the score when the candidate root equals the bass note.
    double bassNoteRootBonus = 0.65;

    /// Added to the score when the candidate root belongs to the current key scale.
    double diatonicRootBonus = 0.30;

    /// Added per chord-tone whose enharmonic spelling (TPC) matches the expected
    /// spelling for the candidate root and quality.  Only applied when TPC data
    /// is present in the input tones (ChordAnalysisTone::tpc != -1).
    double tpcConsistencyBonusPerTone = 0.20;

    /// Added to a candidate whose root matches the previous chord's root.
    /// Resolves ambiguous root choices in favour of root continuity.
    double rootContinuityBonus = 0.40;

    /// Added to a candidate when the previous chord's quality implies a typical
    /// harmonic resolution to this root.
    ///   - Diminished → Major/Minor a semitone above  (viio → I, e.g. Bdim → C)
    ///   - HalfDiminished → Major a perfect fourth above  (ii∅ → V, e.g. Bm7b5 → E)
    ///   - Augmented → Major/Minor at the same root  (I+ → I returning, e.g. C+ → C)
    double resolutionBonus = 0.35;

    // ── Contextual inversion bonuses (§4.1b) ───────────────────────────────

    /// Bonus applied to a non-bass-root candidate when the current
    /// bass note moves by diatonic step FROM the previous region's
    /// bass note.  Stepwise bass motion strongly implies inversion —
    /// root-position chords produce leaping bass lines while inverted
    /// chords enable smooth stepwise bass.
    /// Only fires when candidate.rootPc != bassPc (inverted reading).
    /// Only fires for Major or Minor quality candidates.
    /// Range: 0.0–2.0.  Default: 0.5.
    double stepwiseBassInversionBonus = 0.5;

    /// Bonus applied to a non-bass-root candidate when the current
    /// bass note also moves by diatonic step TO the next region's
    /// bass note.  Both-direction stepwise motion is the strongest
    /// linear bass signal available without full sequence analysis.
    /// Only fires when nextBassPc is known (chord staff analysis only).
    /// Only fires for Major or Minor quality candidates.
    /// Range: 0.0–2.0.  Default: 0.5.
    double stepwiseBassLookaheadBonus = 0.5;

    /// Bonus applied to a non-bass-root candidate when the candidate
    /// root matches the previous region's root (same harmony, different
    /// inversion).  Bass arpeggiation — I → I6 → I — is one of the
    /// most common inversion usages in tonal music.
    /// Only fires when candidate.rootPc != bassPc (inverted reading).
    /// Only fires for Major or Minor quality candidates.
    /// Range: 0.0–2.0.  Default: 0.4.
    double sameRootInversionBonus = 0.4;

    // ── Inversion / bass-root bias correction ──────────────────────────────
    //
    // When the winning candidate beat the best non-bass alternative by less
    // than inversionSuspicionMargin, and a clean (triadic) non-bass alternative
    // exists and noteCount >= 3, the bass-root bonus is suspected of firing
    // incorrectly on an inverted chord.  The bonus contribution to the winner's
    // score is reduced by (1 - inversionBonusReduction) * bassNoteRootBonus,
    // then candidates are re-sorted.
    //
    // inversionSuspicionMargin = 0 disables the correction entirely.
    // inversionBonusReduction = 1.0 means no reduction (NOP).
    // inversionBonusReduction = 0.0 removes the bonus entirely for close-margin cases.
    //
    // Empirically tuned from Section 6.1 validation data (Bach chorales):
    //   - 86.1% of confirmed genuine errors have margin < 0.25
    //   - 100.0% of confirmed genuine errors have margin < 1.0
    //   - 0% of genuine errors have noteCount < 3
    // A margin threshold of 0.65 (= bassNoteRootBonus) catches all cases where
    // the bonus is the sole reason the bass-root candidate wins.

    /// Score-margin threshold below which the inversion correction activates.
    /// Must be >= 0. Set to 0 to disable the correction.
    /// Default: 0.65 (= bassNoteRootBonus — bass bonus is sole deciding factor).
    double inversionSuspicionMargin = 0.65;

    /// Multiplier applied to the bass-root bonus reduction when the correction fires.
    /// 1.0 = no reduction (NOP).  0.0 = remove the bonus contribution entirely.
    /// Default: 0.0 — fully remove the bonus so the non-bass alternative wins.
    double inversionBonusReduction = 0.0;

    // ── Score annotations (future — not yet implemented) ────────────────────
    // These are intentionally off.  When the score-annotation pipeline is ready,
    // flip them on and wire up the corresponding logic.

    /// Use an explicit chord symbol written in the score to constrain / override
    /// the analysis at that tick.
    bool useExistingChordSymbols = false;       // TODO: implement

    /// Use Roman-numeral annotations written in the score as prior context.
    bool useRomanNumeralAnnotations = false;    // TODO: implement

    /// Use Nashville-number annotations written in the score as prior context.
    bool useNashvilleAnnotations = false;       // TODO: implement

    // ── Style prior (future — not yet implemented) ───────────────────────────
    // TODO: expose as a user preference.  Affects chord-frequency priors and
    // which extensions are considered idiomatic.
    // enum class StylePrior { General, Classical, Jazz, Pop, Blues, Folk };
    // StylePrior stylePrior = StylePrior::General;

    /// Returns the valid range for every numeric scoring parameter.
    ///
    /// isManual=false parameters are safe to hand to automated optimizers
    /// (grid search, gradient descent, Bayesian optimization).
    /// isManual=true parameters are wired to user-visible preferences or have
    /// a narrow hand-tuned sweet-spot and should not be auto-adjusted.
    ///
    /// The boolean toggle fields (useExistingChordSymbols, etc.) are omitted;
    /// they are not continuous-valued and are not optimization targets.
    ParameterBoundsMap bounds() const
    {
        return {
            { "bassNoteRootBonus",           { 0.0, 2.0 } },
            { "diatonicRootBonus",           { 0.0, 1.0 } },
            { "tpcConsistencyBonusPerTone",  { 0.0, 1.0 } },
            { "rootContinuityBonus",           { 0.0, 1.5 } },
            { "resolutionBonus",               { 0.0, 1.5 } },
            { "stepwiseBassInversionBonus",    { 0.0, 2.0 } },
            { "stepwiseBassLookaheadBonus",    { 0.0, 2.0 } },
            { "sameRootInversionBonus",        { 0.0, 2.0 } },
            { "inversionSuspicionMargin",      { 0.0, 2.0 } },
            { "inversionBonusReduction",       { 0.0, 1.0 } },
        };
    }
};

/// Global default preferences.  The analyzer uses this when no explicit
/// preferences are supplied by the caller.
inline constexpr ChordAnalyzerPreferences kDefaultChordAnalyzerPreferences{};

/// Optional temporal context passed between successive chord analyses.
/// Enables root-continuity scoring, resolution biasing, and contextual
/// inversion resolution (§4.1b).
///
/// Fields marked "populated" are set by the bridge on every call.
/// Fields marked "deferred" are always at their default values until
/// two-pass chord-staff analysis is implemented (§4.1b).
///
/// Naming note: ChordTemporalContext carries single-step look-around
/// data for vertical chord analysis.  A future TemporalContext struct
/// (planned for analysis/temporal/) will accumulate full progression
/// context (chord history, cadence state) for a ProgressionAnalyzer.
/// These are distinct structs with distinct roles.
struct ChordTemporalContext {
    // ── Already implemented ─────────────────────────────────────────────────

    /// Root pitch class of the most recently identified chord (-1 = none).
    int previousRootPc = -1;

    /// Quality of the most recently identified chord.
    ChordQuality previousQuality = ChordQuality::Unknown;

    /// Elapsed quarter-note time since the previous chord attacked.
    /// 0.0 when unknown.  (Not yet populated — reserved for beat-strength
    /// weighting of root-continuity bonus.)
    double previousChordAge = 0.0;

    // ── New fields (§4.1b — Contextual Inversion Resolution) ────────────────

    /// Bass pitch class of the most recently identified chord.
    /// Used to detect stepwise bass motion indicating inversion.
    /// -1 if unknown.
    int previousBassPc = -1;

    /// Root pitch class of the next identified chord.
    /// Populated by chord staff two-pass analysis only.
    /// -1 if unknown (status bar single-note analysis never has this).
    int nextRootPc = -1;

    /// Bass pitch class of the next identified chord.
    /// -1 if unknown.
    int nextBassPc = -1;

    /// True if the current region's bass note is one diatonic step
    /// above or below the previous region's bass note.
    /// Stepwise bass motion is a strong signal that the current
    /// chord is an inversion within a linear bass line.
    /// Computed by the bridge before passing to the analyzer.
    bool bassIsStepwiseFromPrevious = false;

    /// True if the current region's bass note is one diatonic step
    /// above or below the next region's bass note.
    /// False if nextBassPc is -1.
    bool bassIsStepwiseToNext = false;
};

/// Interface for chord analysis strategies.
///
/// Callers that need dependency injection (tests, bridge) should hold a
/// const reference or pointer to IChordAnalyzer rather than a concrete type.
class IChordAnalyzer
{
public:
    virtual ~IChordAnalyzer() = default;

    /// Analyse a vertical sonority from sounding notes under a key context.
    ///
    /// keySignatureFifths: -7..+7, same convention as KeyModeAnalyzer.
    /// keyMode: detected mode — determines the tonic and diatonic scale used
    ///          for degree assignment and diatonic scoring.
    /// context: optional temporal context for root-continuity scoring.
    ///
    /// Returns up to 3 candidates sorted by score descending. An empty result
    /// means fewer than 3 distinct pitch classes are sounding (insufficient data).
    virtual std::vector<ChordAnalysisResult> analyzeChord(
        const std::vector<ChordAnalysisTone>& tones,
        int keySignatureFifths,
        KeySigMode keyMode,
        const ChordTemporalContext* context = nullptr,
        const ChordAnalyzerPreferences& prefs = kDefaultChordAnalyzerPreferences) const = 0;
};

/// Default chord analyzer: template-matching rule-based approach.
class RuleBasedChordAnalyzer : public IChordAnalyzer
{
public:
    std::vector<ChordAnalysisResult> analyzeChord(
        const std::vector<ChordAnalysisTone>& tones,
        int keySignatureFifths,
        KeySigMode keyMode,
        const ChordTemporalContext* context = nullptr,
        const ChordAnalyzerPreferences& prefs = kDefaultChordAnalyzerPreferences) const override;
};

/// Analyzer implementation variants.
enum class ChordAnalyzerType {
    RuleBased,  ///< Template-matching rule-based analyzer (the only implemented type).
};

/// Factory for IChordAnalyzer instances.
///
/// Bridge files should obtain analyzers via this factory so callers depend only
/// on IChordAnalyzer.  Test code can bypass the factory and inject a mock directly.
class ChordAnalyzerFactory
{
public:
    static std::unique_ptr<IChordAnalyzer> create(
        ChordAnalyzerType type = ChordAnalyzerType::RuleBased);
};

/// Formatting utilities to generate display strings from analysis results.
/// Kept separate from ChordAnalyzer so the analysis layer remains display-agnostic.
namespace ChordSymbolFormatter {

/// Display options for chord symbol and Roman numeral formatting.
/// Kept separate from ChordAnalyzerPreferences so the abstract analysis layer
/// has no knowledge of display conventions (locale, notation style, etc.).
struct Options {
    /// When true, display B natural as "H" and Bb as "B" (German/Nordic convention).
    /// TODO: Replace with a locale-based lookup once user preferences are implemented.
    bool useGermanBHNaming = false;
};

/// Global default formatting options.
inline constexpr Options kDefaultOptions{};

/// Format root, quality, and bass into a chord symbol (e.g. "C7/E", "Fm").
/// Uses flat names for negative keySignatureFifths, sharp names otherwise.
std::string formatSymbol(const ChordAnalysisResult& result, int keySignatureFifths,
                         const Options& opts = kDefaultOptions);

/// Format diatonic degree and quality into roman numeral notation (e.g. "V7", "iiø7").
/// Returns an empty string when result.function.degree < 0 (non-diatonic chord).
std::string formatRomanNumeral(const ChordAnalysisResult& result);


// Nashville Number System formatter and helpers
std::string formatNashvilleNumber(const ChordAnalysisResult& result, int keySignatureFifths);

} // namespace ChordSymbolFormatter

/// Voicing output for chord track population.  Bass note is placed separately
/// from upper-structure tones so the caller can write them to different staves.
struct ClosePositionVoicing {
    int bassPitch = -1;                  ///< Root MIDI pitch in C2–C3 range (-1 = empty)
    std::vector<int> treblePitches;      ///< Upper chord tones in C4–C5 close position
};

/// Compute a close-position keyboard reduction voicing from an analysis result.
///
/// Bass: root placed in C2–C3 (MIDI 36–48), nearest to midpoint (42).
/// Treble: remaining chord tones stacked ascending above C4 (MIDI 60),
/// each note ascending from the previous, staying within one octave.
///
/// Returns empty voicing (bassPitch == -1) if analysis has Unknown quality.
ClosePositionVoicing closePositionVoicing(const ChordAnalysisResult& result);

/// Derive the canonical set of pitch classes for a chord from its analysis result.
///
/// Returns pitch classes (0–11) ordered: root first, then remaining chord tones
/// ascending from the root.  The result reflects the chord's quality and all
/// detected extensions — it is not a transcription of what was sounding, but the
/// idealized chord content suitable for a keyboard reduction.
///
/// If omitsThird is true in the result, the third is excluded.
/// Altered fifths (b5, #5) replace the natural fifth when flagged.
std::vector<int> chordTonePitchClasses(const ChordAnalysisResult& result);

} // namespace mu::composing::analysis
