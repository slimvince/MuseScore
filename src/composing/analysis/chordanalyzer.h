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

#ifndef MU_COMPOSING_ANALYSIS_CHORDANALYZER_H
#define MU_COMPOSING_ANALYSIS_CHORDANALYZER_H

#include <string>
#include <vector>

namespace mu::engraving {
class Note;
}

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

/// Abstract analysis result — contains only harmonic data, no formatting.
/// An empty result vector from analyzeChord() signals insufficient data.
struct ChordAnalysisResult {
    double score = 0.0;  // Raw template match score used for ranking; higher is better.
                         // Reflects the winning template before post-scoring quality
                         // normalisation: the reported quality field may differ from
                         // the template quality that produced this score.

    int rootPc = 0;      // Root pitch class (0–11)
    int bassPc = 0;      // Bass pitch class (0–11)
    int bassTpc = -1;    // Bass note TPC for enharmonic-correct naming; -1 = unknown
    ChordQuality quality = ChordQuality::Unknown;

    // 7th extensions
    bool hasMinorSeventh = false;
    bool hasMajorSeventh = false;
    bool hasDiminishedSeventh = false;  // dim7 interval (9 semitones) — Diminished quality only

    // 6th and 9th
    bool hasAddedSixth = false;
    bool hasNinth = false;
    bool hasNinthNatural = false;
    bool hasNinthFlat = false;
    bool hasNinthSharp = false;

    // 11th and 13th
    bool hasEleventh = false;
    bool hasEleventhSharp = false;
    bool hasThirteenth = false;
    bool hasThirteenthFlat = false;
    bool hasThirteenthSharp = false;

    // Alterations
    bool hasFlatFifth = false;
    bool hasSharpFifth = false;

    // 6/9 chord special case
    bool isSixNine = false;

    // Omitted degrees
    bool omitsThird = false;

    int degree = -1;          // 0..6 when diatonic degree is known; -1 otherwise
    bool diatonicToKey = false;
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
};

/// Global default preferences.  The analyzer uses this when no explicit
/// preferences are supplied by the caller.
inline constexpr ChordAnalyzerPreferences kDefaultChordAnalyzerPreferences{};

/// Optional temporal context passed between successive chord analyses.
/// Enables root-continuity scoring and resolution biasing: when the preceding
/// chord's root and quality are known, candidates are ranked accordingly.
struct ChordTemporalContext {
    int previousRootPc = -1;                              ///< Root pitch class of the preceding chord (-1 = no context).
    ChordQuality previousQuality = ChordQuality::Unknown; ///< Quality of the preceding chord (Unknown = no context).
};

class ChordAnalyzer
{
public:
    /// Analyse a vertical sonority from sounding notes under a key context.
    ///
    /// keySignatureFifths: -7..+7, same convention as KeyModeAnalyzer.
    /// keyIsMajor: true for major/Ionian, false for minor/Aeolian.
    /// context: optional temporal context for root-continuity scoring.
    ///
    /// Returns up to 3 candidates sorted by score descending. An empty result
    /// means fewer than 3 distinct pitch classes are sounding (insufficient data).
    static std::vector<ChordAnalysisResult> analyzeChord(
        const std::vector<ChordAnalysisTone>& tones,
        int keySignatureFifths,
        bool keyIsMajor,
        const ChordTemporalContext* context = nullptr,
        const ChordAnalyzerPreferences& prefs = kDefaultChordAnalyzerPreferences);
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
/// Returns an empty string when result.degree < 0 (non-diatonic chord).
std::string formatRomanNumeral(const ChordAnalysisResult& result, bool keyIsMajor);

} // namespace ChordSymbolFormatter

// Returns analysis results for the harmonic context of `note`.
// Also outputs keyFifths and isMajor (needed by the formatter).
// Returns empty vector if analysis is not possible.
std::vector<ChordAnalysisResult>
analyzeNoteHarmonicContext(const mu::engraving::Note* note,
                           int& outKeyFifths,
                           bool& outIsMajor);

} // namespace mu::composing::analysis

#endif // MU_COMPOSING_ANALYSIS_CHORDANALYZER_H
