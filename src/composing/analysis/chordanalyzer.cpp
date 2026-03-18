/*
 * SPDX-License-Identifier: GPL-3.0-only
 * MuseScore-Studio-CLA-applies
 */

#include "chordanalyzer.h"

#include <algorithm>
#include <array>
#include <limits>

namespace mu::composing::analysis {
namespace {

int normalizePc(int pitch)
{
    int pc = pitch % 12;
    return pc < 0 ? pc + 12 : pc;
}

int ionianTonicPcFromFifths(int fifths)
{
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
    default: return 0;
    }
}

bool endsWith(const std::string& value, const char* suffix)
{
    const size_t suffixLen = std::char_traits<char>::length(suffix);
    return value.size() >= suffixLen
           && value.compare(value.size() - suffixLen, suffixLen, suffix) == 0;
}

const char* pitchClassName(int pc, int keySignatureFifths)
{
    static constexpr std::array<const char*, 12> SHARP_NAMES = {
        "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"
    };
    static constexpr std::array<const char*, 12> FLAT_NAMES = {
        "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"
    };
    const size_t idx = static_cast<size_t>(normalizePc(pc));
    return keySignatureFifths < 0 ? FLAT_NAMES[idx] : SHARP_NAMES[idx];
}

std::string qualitySuffix(ChordQuality quality, bool hasMin7, bool hasMaj7, bool hasAdd6,
                           bool hasNinth = false, bool hasEleventh = false, bool hasThirteenth = false,
                           bool hasNinthFlat = false, bool hasNinthSharp = false, bool hasEleventhSharp = false,
                           bool hasThirteenthFlat = false, bool hasSharpFifth = false, bool hasFlatFifth = false,
                           bool isSixNine = false)
{
    if (isSixNine) {
        switch (quality) {
        case ChordQuality::Minor: return "m69";
        case ChordQuality::Suspended2: return "sus269";
        case ChordQuality::Suspended4: return "sus469";
        default: return "69";
        }
    }

    const bool hasExtended = hasThirteenth || hasEleventh || hasNinth;
    const bool hasSharpEleventhOnly = hasEleventhSharp && !hasEleventh;
    std::string suffix;

    switch (quality) {
    case ChordQuality::Major:
        if (hasMaj7 && hasThirteenth) {
            suffix = "Maj13";
            if (hasSharpEleventhOnly) {
                suffix += "#11";
            }
        } else if (hasMaj7 && hasEleventh) {
            suffix = hasEleventhSharp ? "Maj#11" : "Maj11";
        } else if (hasMaj7 && hasNinth) {
            suffix = hasNinthFlat ? "Majb9" : hasNinthSharp ? "Maj#9" : "Maj9";
            if (hasSharpEleventhOnly) {
                suffix += "#11";
            }
        } else if (hasMin7 && hasThirteenth) {
            suffix = hasThirteenthFlat ? "b13" : "13";
            if (hasSharpEleventhOnly) {
                suffix += "#11";
            }
        } else if (hasMin7 && hasEleventh) {
            suffix = hasEleventhSharp ? "#11" : "11";
        } else if (hasMin7 && hasNinth) {
            suffix = hasNinthFlat ? "b9" : hasNinthSharp ? "#9" : "9";
            if (hasSharpEleventhOnly) {
                suffix += "#11";
            }
        } else if (hasMaj7) {
            suffix = "Maj7";
        } else if (hasMin7) {
            suffix = "7";
        } else if (hasAdd6) {
            suffix = "6";
        } else if (hasEleventh) {
            suffix = hasEleventhSharp ? "add#11" : "add11";
        } else if (hasNinth) {
            suffix = hasNinthFlat ? "addb9" : hasNinthSharp ? "add#9" : "add9";
        } else {
            suffix = "Maj";
        }
        break;
    case ChordQuality::Minor:
        if (hasMaj7 && hasExtended) {
            suffix = "mMaj7";
        } else if (hasMin7 && hasThirteenth) {
            suffix = hasThirteenthFlat ? "mb13" : "m13";
        } else if (hasMin7 && hasEleventh) {
            suffix = hasEleventhSharp ? "m#11" : "m11";
        } else if (hasMin7 && hasNinth) {
            suffix = hasNinthFlat ? "mb9" : hasNinthSharp ? "m#9" : "m9";
        } else if (hasMin7) {
            suffix = "m7";
        } else if (hasMaj7) {
            suffix = "mMaj7";
        } else if (hasAdd6) {
            suffix = "m6";
        } else if (hasNinth) {
            suffix = hasNinthFlat ? "maddb9" : hasNinthSharp ? "madd#9" : "madd9";
        } else {
            suffix = "m";
        }
        break;
    case ChordQuality::Diminished:
        suffix = hasMin7 ? "m7b5" : hasMaj7 ? "dim7" : "dim";
        break;
    case ChordQuality::HalfDiminished:
        suffix = "m7b5";
        break;
    case ChordQuality::Augmented:
        if (hasMaj7) {
            suffix = "augmaj7";
        } else if (hasMin7) {
            suffix = hasThirteenth ? "aug13" : hasEleventh ? "aug11" : hasNinth ? "aug9" : "aug7";
        } else {
            suffix = "+";
        }
        break;
    case ChordQuality::Suspended2:
        if (hasMin7) {
            suffix = hasThirteenth ? "13sus2" : hasEleventh ? "11sus2" : hasNinth ? "9sus2" : "7sus2";
        } else {
            suffix = "sus2";
        }
        break;
    case ChordQuality::Suspended4:
        if (hasMaj7 && hasNinth) {
            suffix = "Maj9sus";
        } else if (hasMaj7) {
            suffix = "Maj7sus";
        } else if (hasMin7) {
            suffix = hasThirteenth ? "13sus4" : hasEleventh ? "11sus4" : hasNinth ? "9sus4" : "7sus4";
        } else {
            suffix = "sus4";
        }
        break;
    case ChordQuality::Power:
        suffix = "5";
        break;
    default:
        suffix = "";
        break;
    }

    if (hasSharpFifth && quality != ChordQuality::Augmented && !endsWith(suffix, "#5")) {
        suffix += "#5";
    } else if (hasFlatFifth && quality != ChordQuality::Diminished && quality != ChordQuality::HalfDiminished && !endsWith(suffix, "b5")) {
        suffix += "b5";
    }

    return suffix;
}

std::string diatonicRoman(int degree, ChordQuality quality, bool keyIsMajor, bool hasMinorSeventh, bool hasMajorSeventh,
                           bool hasNinth, bool hasEleventh, bool hasThirteenth)
{
    if (degree < 0 || degree > 6) {
        return "";
    }

    static constexpr std::array<const char*, 7> UPPER = { "I", "II", "III", "IV", "V", "VI", "VII" };
    static constexpr std::array<const char*, 7> LOWER = { "i", "ii", "iii", "iv", "v", "vi", "vii" };

    std::string rn;
    switch (quality) {
    case ChordQuality::Major:
    case ChordQuality::Augmented:
    case ChordQuality::Suspended2:
    case ChordQuality::Suspended4:
    case ChordQuality::Power:
        rn = UPPER[static_cast<size_t>(degree)];
        break;
    case ChordQuality::Minor:
        rn = LOWER[static_cast<size_t>(degree)];
        break;
    case ChordQuality::Diminished:
        rn = LOWER[static_cast<size_t>(degree)];
        rn += "o";
        break;
    case ChordQuality::HalfDiminished:
        rn = LOWER[static_cast<size_t>(degree)];
        rn += "o7";
        break;
    default:
        return "";
    }

    if (quality == ChordQuality::Augmented
        && !hasMajorSeventh
        && !hasMinorSeventh
        && !hasNinth
        && !hasEleventh
        && !hasThirteenth) {
        rn += "+";
    }

    if (hasMajorSeventh) {
        rn += "M7";
    } else if (hasMinorSeventh) {
        rn += "7";
    }

    if (!hasMajorSeventh && !hasMinorSeventh) {
        if (hasThirteenth) {
            rn += "13";
        } else if (hasEleventh) {
            rn += "11";
        } else if (hasNinth) {
            rn += "9";
        }
    }

    if (!keyIsMajor && degree == 6 && quality == ChordQuality::Major) {
        // In natural minor, VII is usually interpreted as subtonic major.
        return rn;
    }

    return rn;
}

std::vector<int> coreIntervals(ChordQuality quality, bool hasMinorSeventh, bool hasMajorSeventh)
{
    std::vector<int> intervals;

    switch (quality) {
    case ChordQuality::Major:
        intervals = { 0, 4, 7 };
        break;
    case ChordQuality::Minor:
    case ChordQuality::HalfDiminished:
        intervals = { 0, 3, 7 };
        break;
    case ChordQuality::Diminished:
        intervals = { 0, 3, 6 };
        break;
    case ChordQuality::Augmented:
        intervals = { 0, 4, 8 };
        break;
    case ChordQuality::Suspended2:
        intervals = { 0, 2, 7 };
        break;
    case ChordQuality::Suspended4:
        intervals = { 0, 5, 7 };
        break;
    case ChordQuality::Power:
        intervals = { 0, 7 };
        break;
    default:
        intervals = { 0, 4, 7 };
        break;
    }

    if (quality == ChordQuality::HalfDiminished) {
        intervals.push_back(10);
    } else if (hasMajorSeventh) {
        intervals.push_back(11);
    } else if (hasMinorSeventh) {
        intervals.push_back(quality == ChordQuality::Diminished ? 9 : 10);
    }

    return intervals;
}

bool isCompatibleExtensionInterval(int interval)
{
    switch (normalizePc(interval)) {
    case 2:  // 9
    case 6:  // #11 / b5 context-dependent tension
    case 5:  // 11
    case 9:  // 13 / 6
    case 10: // minor 7
    case 11: // major 7
        return true;
    default:
        return false;
    }
}

std::string romanWithInversion(const std::string& roman, ChordQuality quality, int rootPc, int bassPc,
                               bool hasMinorSeventh, bool hasMajorSeventh)
{
    if (roman.empty() || bassPc == rootPc) {
        return roman;
    }

    const int bassInterval = normalizePc(bassPc - rootPc);
    const std::vector<int> intervals = coreIntervals(quality, hasMinorSeventh, hasMajorSeventh);

    auto intervalIt = std::find(intervals.begin(), intervals.end(), bassInterval);
    if (intervalIt == intervals.end()) {
        return roman;
    }

    const int inversion = static_cast<int>(std::distance(intervals.begin(), intervalIt));
    if (inversion <= 0) {
        return roman;
    }

    if (intervals.size() <= 3) {
        if (inversion == 1) {
            return roman + "6";
        }
        if (inversion == 2) {
            return roman + "64";
        }
        return roman;
    }

    static constexpr std::array<const char*, 4> FIGURED_BASS = { "", "65", "43", "42" };
    const char* suffix = FIGURED_BASS[static_cast<size_t>(std::min(inversion, 3))];
    if (endsWith(roman, "M7")) {
        return roman.substr(0, roman.size() - 2) + suffix;
    }
    if (endsWith(roman, "7")) {
        return roman.substr(0, roman.size() - 1) + suffix;
    }

    return roman + suffix;
}

} // namespace

ChordAnalysisResult ChordAnalyzer::analyzeChord(const std::vector<ChordAnalysisTone>& tones,
                                                bool keyIsMajor)
{
    ChordAnalysisResult result;
    if (tones.empty()) {
        return result;
    }

    // Require a minimum number of sounding tones for meaningful chord analysis
    // (3+ tones gives good confidence for diatonic chord identification)
    constexpr size_t MIN_TONES_FOR_ANALYSIS = 3;
    if (tones.size() < MIN_TONES_FOR_ANALYSIS) {
        return result;
    }

    std::array<double, 12> pcWeight {};
    int bassPitch = std::numeric_limits<int>::max();
    int lowestPitch = std::numeric_limits<int>::max();

    for (const ChordAnalysisTone& t : tones) {
        const int pc = normalizePc(t.pitch);
        const double w = std::max(0.1, t.weight);
        pcWeight[static_cast<size_t>(pc)] += w;

        if (t.pitch < lowestPitch) {
            lowestPitch = t.pitch;
        }
        if (t.isBass && t.pitch < bassPitch) {
            bassPitch = t.pitch;
        }
    }

    if (bassPitch == std::numeric_limits<int>::max()) {
        bassPitch = lowestPitch;
    }
    if (bassPitch == std::numeric_limits<int>::max()) {
        return result;
    }

    const int bassPc = normalizePc(bassPitch);

    struct TemplateDef {
        ChordQuality quality;
        std::vector<int> intervals;
    };

    const std::array<TemplateDef, 8> templates = {{
        { ChordQuality::Major,      { 0, 4, 7 } },
        { ChordQuality::Major,      { 0, 4, 6 } },
        { ChordQuality::Minor,      { 0, 3, 7 } },
        { ChordQuality::Diminished, { 0, 3, 6 } },
        { ChordQuality::Augmented,  { 0, 4, 8 } },
        { ChordQuality::Suspended2, { 0, 2, 7 } },
        { ChordQuality::Suspended4, { 0, 5, 7 } },
        { ChordQuality::Power,      { 0, 7 } }
    }};

    double bestScore = -std::numeric_limits<double>::infinity();
    int bestRootPc = 0;
    ChordQuality bestQuality = ChordQuality::Unknown;

    for (int rootPc = 0; rootPc < 12; ++rootPc) {
        for (const TemplateDef& tpl : templates) {
            double score = 0.0;

            for (size_t i = 0; i < tpl.intervals.size(); ++i) {
                const int chordPc = (rootPc + tpl.intervals[i]) % 12;
                const double toneWeight = pcWeight[static_cast<size_t>(chordPc)];
                const double factor = (i == 0) ? 1.8 : ((i == 1) ? 1.2 : 1.0);
                score += factor * std::min(toneWeight, 3.0);
            }

            // Penalize chromatic clutter, but reward common chord extensions.
            for (int pc = 0; pc < 12; ++pc) {
                bool inTemplate = false;
                for (int interval : tpl.intervals) {
                    if (((rootPc + interval) % 12) == pc) {
                        inTemplate = true;
                        break;
                    }
                }
                if (inTemplate) {
                    continue;
                }

                const int rel = normalizePc(pc - rootPc);
                if (isCompatibleExtensionInterval(rel)) {
                    const double extensionFactor = (rel == 10 || rel == 11) ? 0.45 : 0.35;
                    score += extensionFactor * std::min(pcWeight[static_cast<size_t>(pc)], 2.0);
                } else {
                    score -= 0.45 * std::min(pcWeight[static_cast<size_t>(pc)], 2.0);
                }
            }

            if (rootPc == bassPc) {
                score += 0.35;
            }

            if (score > bestScore) {
                bestScore = score;
                bestRootPc = rootPc;
                bestQuality = tpl.quality;
            }
        }
    }

    const bool hasMin7 = pcWeight[static_cast<size_t>((bestRootPc + 10) % 12)] > 0.2;
    const bool hasMaj7 = pcWeight[static_cast<size_t>((bestRootPc + 11) % 12)] > 0.2;
    const bool hasAdd6 = pcWeight[static_cast<size_t>((bestRootPc + 9) % 12)] > 0.2;
    
    // Extended detection for 9th, 11th, 13th
    const bool hasNinth = pcWeight[static_cast<size_t>((bestRootPc + 2) % 12)] > 0.2;
    const bool hasNinthFlat = hasNinth && pcWeight[static_cast<size_t>((bestRootPc + 1) % 12)] > 0.3;
    const bool hasNinthSharp = hasNinth && pcWeight[static_cast<size_t>((bestRootPc + 3) % 12)] > 0.3;
    
    const bool hasEleventh = pcWeight[static_cast<size_t>((bestRootPc + 5) % 12)] > 0.2;
    // #11 can appear without a natural 11 in common chord-symbol usage.
    const bool hasEleventhSharp = pcWeight[static_cast<size_t>((bestRootPc + 6) % 12)] > 0.3;
    
    const bool hasThirteenth = pcWeight[static_cast<size_t>((bestRootPc + 9) % 12)] > 0.2 && (hasMin7 || hasMaj7 || hasEleventh || hasNinth);
    const bool hasThirteenthFlat = hasThirteenth && pcWeight[static_cast<size_t>((bestRootPc + 8) % 12)] > 0.3;
    
    // Fifth alterations
    const bool hasSharpFifth = pcWeight[static_cast<size_t>((bestRootPc + 8) % 12)] > 0.2;
    const bool hasFlatFifthRaw = pcWeight[static_cast<size_t>((bestRootPc + 6) % 12)] > 0.2
                                 && bestQuality != ChordQuality::Diminished
                                 && bestQuality != ChordQuality::HalfDiminished;
    // Prefer interpreting tritone tension as #11 only in seventh/extended contexts.
    const bool preferSharp11 = hasFlatFifthRaw
                               && (hasMin7 || hasMaj7 || hasNinth || hasEleventh || hasThirteenth);
    const bool hasFlatFifth = hasFlatFifthRaw && !preferSharp11;
    
    // 69 chord detection: has both 6 and 9
    const bool isSixNine = hasAdd6 && hasNinth && !hasMin7 && !hasMaj7;

    // Degree-presence flags used for requalification
    const bool hasMajThird     = pcWeight[static_cast<size_t>((bestRootPc + 4) % 12)] > 0.2;
    const bool hasMinThird     = pcWeight[static_cast<size_t>((bestRootPc + 3) % 12)] > 0.2;
    const bool hasAnyThird     = hasMajThird || hasMinThird;
    const bool hasPerfectFourth = pcWeight[static_cast<size_t>((bestRootPc + 5) % 12)] > 0.2;

    // Prefer sus4 over sus2 when the perfect fourth is actually sounding.
    // The two templates score identically on the shared {root, 5th} notes, so
    // sus2 wins only by array order.  If interval-5 is present, sus4 is more
    // precise (e.g. C F G B D should be sus4, not sus2).
    if (bestQuality == ChordQuality::Suspended2 && hasPerfectFourth) {
        bestQuality = ChordQuality::Suspended4;
    }

    // Requalify sus2/sus4 → Major + omitsThird when a major-7th is present but
    // neither a 3rd nor a perfect 4th is sounding.  A major-7th alongside a
    // suspension score virtually always means the chord is a tertian voicing
    // with omitted 3rd (e.g. C G B D = Maj9(no 3)), not a true suspension.
    bool omitsThird = false;
    if (hasMaj7 && !hasAnyThird && !hasPerfectFourth
        && (bestQuality == ChordQuality::Suspended2 || bestQuality == ChordQuality::Suspended4)) {
        bestQuality = ChordQuality::Major;
        omitsThird  = true;
    }

    // Default to C as tonic if key signature is not provided
    const int ionianTonicPc = 0;
    const int keyTonicPc = keyIsMajor ? ionianTonicPc : (ionianTonicPc + 9) % 12;

    constexpr std::array<int, 7> MAJOR_SCALE = { 0, 2, 4, 5, 7, 9, 11 };
    constexpr std::array<int, 7> MINOR_SCALE = { 0, 2, 3, 5, 7, 8, 10 };
    const std::array<int, 7>& scale = keyIsMajor ? MAJOR_SCALE : MINOR_SCALE;

    int degree = -1;
    bool diatonic = true;
    for (size_t i = 0; i < scale.size(); ++i) {
        if ((keyTonicPc + scale[i]) % 12 == bestRootPc) {
            degree = static_cast<int>(i);
            break;
        }
    }

    for (size_t pc = 0; pc < pcWeight.size(); ++pc) {
        if (pcWeight[pc] <= 0.2) {
            continue;
        }

        bool inScale = false;
        for (int interval : scale) {
            if ((keyTonicPc + interval) % 12 == static_cast<int>(pc)) {
                inScale = true;
                break;
            }
        }
        if (!inScale) {
            diatonic = false;
            break;
        }
    }

    // Symmetrical chord root override: for augmented triads, use the pitch class of the lowest pitch as the root
    if (tones.size() == 3) {
        std::vector<int> pcs;
        std::vector<int> pitches;
        int lowestPitch = std::numeric_limits<int>::max();
        int lowestPc = -1;
        for (const auto& t : tones) {
            int pc = normalizePc(t.pitch);
            if (std::find(pcs.begin(), pcs.end(), pc) == pcs.end()) {
                pcs.push_back(pc);
            }
            pitches.push_back(t.pitch);
            if (t.pitch < lowestPitch) {
                lowestPitch = t.pitch;
                lowestPc = pc;
            }
        }
        if (pcs.size() == 3) {
            // Check all permutations for three 4-semitone intervals (augmented triad)
            for (int i = 0; i < 3; ++i) {
                int a = pcs[i];
                int b = pcs[(i + 1) % 3];
                int c = pcs[(i + 2) % 3];
                int i1 = (b - a + 12) % 12;
                int i2 = (c - b + 12) % 12;
                int i3 = (a - c + 12) % 12;
                if (i1 == 4 && i2 == 4 && i3 == 4) {
                    // Always use the pitch class of the lowest pitch as the root
                    bestRootPc = lowestPc;
                    bestQuality = ChordQuality::Augmented;
                    break;
                }
            }
        }
    }

    result.isValid = true;
    result.rootPc = bestRootPc;
    result.bassPc = bassPc;
    result.quality = bestQuality;
    result.hasMinorSeventh = hasMin7 && !hasMaj7;
    result.hasMajorSeventh = hasMaj7;
    result.hasAddedSixth = hasAdd6 && !hasMin7 && !hasMaj7;
    result.hasNinth = hasNinth;
    result.hasNinthFlat = hasNinthFlat;
    result.hasNinthSharp = hasNinthSharp;
    result.hasEleventh = hasEleventh;
    result.hasEleventhSharp = hasEleventhSharp;
    result.hasThirteenth = hasThirteenth;
    result.hasThirteenthFlat = hasThirteenthFlat;
    result.hasSharpFifth = hasSharpFifth;
    result.hasFlatFifth = hasFlatFifth;
    result.isSixNine = isSixNine;
    result.omitsThird = omitsThird;
    result.degree = degree;
    result.diatonicToKey = diatonic && degree >= 0;

    return result;
}

std::string ChordSymbolFormatter::formatSymbol(const ChordAnalysisResult& result, int keySignatureFifths)
{
    if (!result.isValid) {
        return "";
    }

    std::string symbol = std::string(pitchClassName(result.rootPc, keySignatureFifths))
                        + qualitySuffix(result.quality, result.hasMinorSeventh, result.hasMajorSeventh, 
                                       result.hasAddedSixth, result.hasNinth, result.hasEleventh, 
                                       result.hasThirteenth, result.hasNinthFlat, result.hasNinthSharp,
                                       result.hasEleventhSharp, result.hasThirteenthFlat, result.hasSharpFifth, 
                                       result.hasFlatFifth, result.isSixNine);

    if (result.omitsThird) {
        symbol += "(no 3)";
    }

    if (result.bassPc != result.rootPc) {
        symbol += "/";
        symbol += pitchClassName(result.bassPc, keySignatureFifths);
    }

    return symbol;
}

std::string ChordSymbolFormatter::formatRomanNumeral(const ChordAnalysisResult& result, bool keyIsMajor)
{
    if (result.degree < 0) {
        return "";
    }

    std::string romanNumeral = diatonicRoman(result.degree, result.quality, keyIsMajor,
                                            result.hasMinorSeventh, result.hasMajorSeventh,
                                            result.hasNinth, result.hasEleventh, result.hasThirteenth);
    romanNumeral = romanWithInversion(romanNumeral, result.quality,
                                      result.rootPc, result.bassPc,
                                      result.hasMinorSeventh, result.hasMajorSeventh);
    return romanNumeral;
}

} // namespace mu::composing::analysis
