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
            { "bassNoteRootBonus",        { 0.0, 2.0 } },
            { "diatonicRootBonus",        { 0.0, 1.0 } },
            { "tpcConsistencyBonusPerTone",{ 0.0, 1.0 } },
            { "rootContinuityBonus",      { 0.0, 1.5 } },
            { "resolutionBonus",          { 0.0, 1.5 } },
        };
    }
};

/// Global default preferences.  The analyzer uses this when no explicit
/// preferences are supplied by the caller.
inline constexpr ChordAnalyzerPreferences kDefaultChordAnalyzerPreferences{};

/// Optional temporal context passed between successive chord analyses.
/// Enables root-continuity scoring and resolution biasing: when the preceding
/// chord's root and quality are known, candidates are ranked accordingly.
///
/// Naming note: ChordTemporalContext carries the previous root/quality for
/// single-chord analysis.  A future TemporalContext struct (planned for
/// analysis/temporal/) will accumulate full progression context (chord
/// history, cadence state) for use by a ProgressionAnalyzer.  These are
/// distinct structs with distinct roles.
struct ChordTemporalContext {
    int previousRootPc = -1;                              ///< Root pitch class of the preceding chord (-1 = no context).
    ChordQuality previousQuality = ChordQuality::Unknown; ///< Quality of the preceding chord (Unknown = no context).
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
