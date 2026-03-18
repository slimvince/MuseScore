/*
 * SPDX-License-Identifier: GPL-3.0-only
 * MuseScore-Studio-CLA-applies
 */

#ifndef MU_COMPOSING_ANALYSIS_CHORDANALYZER_H
#define MU_COMPOSING_ANALYSIS_CHORDANALYZER_H

#include <string>
#include <vector>

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
    int pitch = 0;      // MIDI pitch number
    int tpc = 0;        // Reserved for future spelling-aware improvements
    double weight = 1;  // Relative evidence weight
    bool isBass = false;
};

// Abstract analysis result containing only harmonic data, no formatting
struct ChordAnalysisResult {
    bool isValid = false;
    int rootPc = 0;     // Root pitch class (0-11)
    int bassPc = 0;     // Bass pitch class (0-11)
    ChordQuality quality = ChordQuality::Unknown;
    
    // 7th extensions
    bool hasMinorSeventh = false;
    bool hasMajorSeventh = false;
    
    // 6th and 9th
    bool hasAddedSixth = false;
    bool hasNinth = false;          // 9, b9, #9 present
    bool hasNinthFlat = false;      // b9 (minor 9th)
    bool hasNinthSharp = false;     // #9 (augmented 9th)
    
    // 11th and 13th
    bool hasEleventh = false;       // 11 present
    bool hasEleventhSharp = false;  // #11 (augmented 11th)
    bool hasThirteenth = false;     // 13 present
    bool hasThirteenthFlat = false; // b13 (minor 13th)
    bool hasThirteenthSharp = false; // #13 (augmented 13th) - rare
    
    // Alterations
    bool hasFlatFifth = false;      // b5
    bool hasSharpFifth = false;     // #5 (same as C aug but sometimes #5 on maj/dom)
    
    // 69 chord special case
    bool isSixNine = false;         // 6/9 chord

    // Omitted degrees (trigger "(no 3)" / "(no 5)" in the formatted symbol)
    bool omitsThird = false;        // 3rd absent — sus2/sus4+maj7 requalified as tertian

    int degree = -1;                 // 0..6 when diatonic degree is known
    bool diatonicToKey = false;
};

class ChordAnalyzer
{
public:
    // Analyze a vertical sonority from sounding notes under a key context.
    // keySignatureFifths uses the same -7..+7 convention as KeyModeGuesser.
    // Result contains only abstract analysis data (pitch classes, quality flags, degree).
    // For display, use ChordSymbolFormatter::formatSymbol() or ChordSymbolFormatter::formatRomanNumeral().
    static ChordAnalysisResult analyzeChord(const std::vector<ChordAnalysisTone>& tones,
                                            bool keyIsMajor);
};

// Formatting utilities to generate display strings from analysis results.
// These are separate from the analyzer to keep analysis abstract and reusable.
namespace ChordSymbolFormatter {
    // Format root, quality, and bass into a chord symbol (e.g., "Cmaj7/G").
    // Follows MuseScore conventions: "Maj" not "maj", "m7" not "min7", etc.
    std::string formatSymbol(const ChordAnalysisResult& result, int keySignatureFifths);

    // Format diatonic degree and chord quality into roman numerals (e.g., "V7", "vi64").
    // Returns empty string if result.degree < 0 (non-diatonic chords).
    std::string formatRomanNumeral(const ChordAnalysisResult& result, bool keyIsMajor);
}

} // namespace mu::composing::analysis

#endif // MU_COMPOSING_ANALYSIS_CHORDANALYZER_H
