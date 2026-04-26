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

#include "chordanalyzer.h"
#include "analysisutils.h"

#include <algorithm>
#include <array>
#include <cmath>
#include <limits>

namespace mu::composing::analysis {
namespace {

/// Return the standard English name for a pitch class, choosing flat vs sharp
/// based on the key signature.  Applies German B/H mapping when spelling requires it.
/// German mapping mirrors tpc2name() GERMAN case (pitchspelling.cpp:343-356):
///   Rule 1: B natural → "H"
///   Rule 2: Bb → "B"
/// All other note names are unchanged.
const char* pitchClassName(int pc, int keySignatureFifths,
                           ChordSymbolFormatter::NoteSpelling spelling = ChordSymbolFormatter::NoteSpelling::Standard)
{
    static constexpr std::array<const char*, 12> SHARP_NAMES = {
        "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"
    };
    static constexpr std::array<const char*, 12> FLAT_NAMES = {
        "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"
    };
    // German/Nordic: SHARP_NAMES[11]="B" → "H", FLAT_NAMES[10]="Bb" → "B"
    static constexpr std::array<const char*, 12> SHARP_NAMES_GERMAN = {
        "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "H"
    };
    static constexpr std::array<const char*, 12> FLAT_NAMES_GERMAN = {
        "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "B", "H"
    };
    const size_t idx = static_cast<size_t>(normalizePc(pc));
    const bool isGerman = (spelling == ChordSymbolFormatter::NoteSpelling::German
                        || spelling == ChordSymbolFormatter::NoteSpelling::GermanPure);
    if (keySignatureFifths < 0) {
        return isGerman ? FLAT_NAMES_GERMAN[idx] : FLAT_NAMES[idx];
    }
    return isGerman ? SHARP_NAMES_GERMAN[idx] : SHARP_NAMES[idx];
}

/// Name a pitch class using TPC spelling rather than key-signature convention.
/// Covers cases like Eb (tpc=12), Bb (tpc=13), Ab (tpc=11) in C major (keyFifths=0).
///
/// TPC encoding note: two TPC encodings coexist in this codebase.
///   • MuseScore internal (from n->tpc()): F=13, C=14, G=15…, B=19, Bb=12, Cb=7, Fb=6.
///   • Test-file encoding (+1 offset):       F=14, C=15, G=16…, B=20, Bb=13, Cb=8, Fb=7.
/// Absolute-value checks below handle both by pairing TPC range with pitch class (pc).
///
/// TPC is consulted in four scenarios:
///   1. Explicit Cb/Fb spelling (pc 11/4 with TPC in the double-flat range): always use
///      the flat name regardless of key, since the standard name tables return B/E.
///   2. keySignatureFifths == 0 (C major / A minor): key signature gives no preference;
///      TPC in the flat range 7..13 (or 8..14 for the +1 encoding) → flat spelling.
///   3. Very flat key contexts (keyFifths ≤ −5): B natural (pc 11, high-TPC) → Cb.
///   4. Very flat key contexts (keyFifths ≤ −6): E natural (pc 4,  high-TPC) → Fb.
///
/// German mapping mirrors tpc2name() GERMAN case (pitchspelling.cpp:343-356).
const char* pitchClassNameFromTpc(int pc, int tpc, int keySignatureFifths,
                                  ChordSymbolFormatter::NoteSpelling spelling = ChordSymbolFormatter::NoteSpelling::Standard)
{
    static constexpr std::array<const char*, 12> SHARP_NAMES = {
        "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"
    };
    static constexpr std::array<const char*, 12> FLAT_NAMES = {
        "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"
    };
    static constexpr std::array<const char*, 12> SHARP_NAMES_GERMAN = {
        "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "H"
    };
    static constexpr std::array<const char*, 12> FLAT_NAMES_GERMAN = {
        "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "B", "H"
    };
    const bool isGerman = (spelling == ChordSymbolFormatter::NoteSpelling::German
                        || spelling == ChordSymbolFormatter::NoteSpelling::GermanPure);
    if (tpc >= 0) {
        // Cb (pc=11): TPC_C_B=7 in MuseScore internal, 8 in +1 test encoding.
        // Fb (pc=4):  TPC_F_B=6 in MuseScore internal, 7 in +1 test encoding.
        // Both are not representable in the standard 12-entry name tables (FLAT_NAMES
        // maps pc=11→"B" and pc=4→"E"), so return the explicit flat name here.
        // Use pc to disambiguate TPC=7 (which is Cb in MuseScore internal vs Fb in +1 encoding).
        if (pc == 11 && (tpc == 7 || tpc == 8)) return isGerman ? "Ces" : "Cb";
        if (pc == 4  && (tpc == 6 || tpc == 7)) return isGerman ? "Fes" : "Fb";

        // Sharp-spelled chromatic note in flat or mildly-sharp key contexts: normalise to
        // the conventional flat chord-symbol name used in jazz/pop.  A sharp TPC (≥20,
        // covering both MuseScore-internal and +1-offset encodings) means the score writer
        // used a sharp accidental; below the diatonic-at key threshold the flat name is the
        // canonical chord-symbol spelling.  Checked before the keySignatureFifths==0 TPC
        // block so it intercepts sharp-spelled notes even in neutral-key contexts.
        //   Eb (pc=3)  diatonic at E major (keyFifths=4) → D# in C/G/D/A major becomes Eb
        //   Ab (pc=8)  diatonic at A major (keyFifths=3) → G# in C/G/D major becomes Ab
        //   Bb (pc=10) diatonic at B major (keyFifths=5) → A# in C through 4 sharps → Bb
        if (tpc >= 20) {
            const size_t idx = static_cast<size_t>(normalizePc(pc));
            if ((pc == 3  && keySignatureFifths < 4)   // D# → Eb
             || (pc == 8  && keySignatureFifths < 3)   // G# → Ab
             || (pc == 10 && keySignatureFifths < 5))  // A# → Bb
            {
                return isGerman ? FLAT_NAMES_GERMAN[idx] : FLAT_NAMES[idx];
            }
        }

        if (keySignatureFifths == 0) {
            // Key signature gives no flat/sharp preference (C major / A minor):
            // use TPC to disambiguate.  Flat range covers both encodings: MuseScore [7,13]
            // and +1 encoding [8,14].  Union [7,14] is safe because natural notes (FLAT==SHARP).
            const bool preferFlat = (tpc >= 7 && tpc <= 14);
            const size_t idx = static_cast<size_t>(normalizePc(pc));
            if (preferFlat) {
                return isGerman ? FLAT_NAMES_GERMAN[idx] : FLAT_NAMES[idx];
            }
            return isGerman ? SHARP_NAMES_GERMAN[idx] : SHARP_NAMES[idx];
        }

        // Very flat key contexts: natural notes whose enharmonic flat spelling is
        // more appropriate than what the standard flat-key table provides.
        //
        // B natural (pc=11, TPC=19 MuseScore or 20 +1-encoding) in keys with 5+ flats → Cb.
        // E natural (pc=4,  TPC=18 MuseScore or 19 +1-encoding) in keys with 6+ flats → Fb.
        if (keySignatureFifths <= -5 && pc == 11 && (tpc == 19 || tpc == 20))
            return isGerman ? "Ces" : "Cb";
        if (keySignatureFifths <= -6 && pc == 4  && (tpc == 18 || tpc == 19))
            return isGerman ? "Fes" : "Fb";
    }
    return pitchClassName(pc, keySignatureFifths, spelling);
}

std::string qualitySuffix(ChordQuality quality, bool hasMin7, bool hasMaj7, bool hasDim7,
                           bool hasAdd6,
                           bool hasNinth, bool hasNinthNatural, bool hasEleventh, bool hasThirteenth,
                           bool hasNinthFlat, bool hasNinthSharp, bool hasEleventhSharp,
                           bool hasThirteenthFlat, bool hasThirteenthSharp,
                           bool hasSharpFifth, bool hasFlatFifth,
                           bool isSixNine)
{
    if (isSixNine) {
        switch (quality) {
        case ChordQuality::Minor:      return "m69";
        case ChordQuality::Suspended2: return "sus269";
        case ChordQuality::Suspended4: return "sus69";
        default:                       return "69";
        }
    }

    const bool hasExtended = hasThirteenth || hasEleventh || hasNinth;
    std::string suffix;

    switch (quality) {
    case ChordQuality::Major:
        if (hasMaj7 && hasThirteenth) {
            // "Maj13" implies 9th; use "Maj7add13" when 9th is absent.
            suffix = hasNinth ? "Maj13" : "Maj7add13";
            if (hasEleventhSharp) { suffix += "#11"; }
        } else if (hasMaj7 && hasEleventh) {
            suffix = hasEleventhSharp ? "Maj#11" : "Maj11";
        } else if (hasMaj7 && hasNinth) {
            if (hasNinthNatural) {
                suffix = "Maj9";
            } else {
                suffix = hasNinthFlat ? "Maj7b9" : "Maj7#9";
            }
            if (hasEleventhSharp) { suffix += "#11"; }
        } else if (hasMin7 && hasThirteenth) {
            suffix = hasThirteenthFlat ? "b13" : "13";
            if (hasEleventhSharp) { suffix += "#11"; }
            if (hasNinthFlat)  { suffix += "b9"; }
            if (hasNinthSharp) { suffix += "#9"; }
        } else if (hasMin7 && hasEleventh) {
            suffix = hasEleventhSharp ? "#11" : "11";
        } else if (hasMin7 && hasNinth) {
            if (hasNinthNatural) {
                suffix = hasNinthFlat ? "b9" : hasNinthSharp ? "#9" : "9";
            } else {
                suffix = "7";
                if (hasNinthFlat)  { suffix += "b9"; }
                if (hasNinthSharp) { suffix += "#9"; }
            }
            if (hasEleventhSharp) { suffix += "#11"; }
        } else if (hasMaj7) {
            suffix = "Maj7";
            if (hasEleventhSharp) { suffix += "#11"; }
        } else if (hasMin7) {
            suffix = "7";
            if (hasNinthFlat)   { suffix += "b9"; }
            if (hasNinthSharp)  { suffix += "#9"; }
            if (hasEleventhSharp) { suffix += "#11"; }
        } else if (hasAdd6) {
            suffix = "6";
        } else if (hasEleventh) {
            suffix = hasEleventhSharp ? "add#11" : "add11";
        } else if (hasNinth) {
            suffix = hasNinthFlat ? "addb9" : hasNinthSharp ? "add#9" : "add9";
            if (hasThirteenthSharp) { suffix += "add#13"; }
        } else if (hasThirteenthSharp) {
            // When a #11 is also present, embed it before #13.
            suffix = hasEleventhSharp ? "add#11#13" : "add#13";
        } else {
            suffix = "";  // plain major triad: "C" not "CMaj"
        }
        break;

    case ChordQuality::Minor:
        if (hasMaj7 && hasExtended) {
            if (hasThirteenth) {
                suffix = hasNinth ? "mMaj13" : "mMaj7add13";
            } else if (hasEleventh) {
                suffix = hasNinth ? "mMaj11" : "mMaj7add11";
            } else {
                suffix = hasNinthNatural ? "mMaj9" : "mMaj7";
            }
        } else if (hasMin7 && hasThirteenth) {
            suffix = hasThirteenthFlat ? "mb13" : "m13";
        } else if (hasMin7 && hasEleventh) {
            // "m11" implies 9th; use "m7add11" when 9th is absent.
            suffix = hasEleventhSharp ? "m#11" : (hasNinth ? "m11" : "m7add11");
        } else if (hasMin7 && hasNinth) {
            if (hasNinthNatural) {
                suffix = hasNinthFlat ? "mb9" : hasNinthSharp ? "m#9" : "m9";
            } else {
                suffix = "m7";
                if (hasNinthFlat)  { suffix += "b9"; }
                if (hasNinthSharp) { suffix += "#9"; }
            }
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
        suffix = hasDim7 ? "dim7" : "dim";
        break;

    case ChordQuality::HalfDiminished:
        if (hasNinthNatural && hasEleventh) {
            suffix = "m11b5";
        } else if (hasNinthNatural) {
            suffix = "m9b5";
        } else if (hasNinthFlat) {
            suffix = "m7b5b9";
        } else if (hasEleventh) {
            suffix = "m7b5add11";
        } else {
            suffix = "m7b5";
        }
        break;

    case ChordQuality::Augmented:
        // Catalog convention: "#5" suffix notation (e.g. "7#5", "9#5", "Maj7#5"),
        // not "aug" prefix.  Order: [7|9|13] [#5] [b9|#9] [#11].
        if (hasMaj7) {
            if (hasNinthNatural) {
                suffix = "Maj9#5";
            } else {
                suffix = "Maj7#5";
                if (hasNinthFlat)  { suffix += "b9"; }
                if (hasNinthSharp) { suffix += "#9"; }
            }
        } else if (hasMin7) {
            if (hasThirteenth) {
                suffix = "13#5";
                if (hasNinthFlat)  { suffix += "b9"; }
                if (hasNinthSharp) { suffix += "#9"; }
            } else if (hasNinth && hasNinthNatural) {
                suffix = "9#5";
            } else {
                suffix = "7#5";
                if (hasNinthFlat)  { suffix += "b9"; }
                if (hasNinthSharp) { suffix += "#9"; }
            }
            if (hasEleventhSharp) { suffix += "#11"; }
        } else {
            suffix = "+";
        }
        break;

    case ChordQuality::Suspended2:
        if (hasMin7) {
            suffix = hasThirteenth ? "13sus2" : hasEleventh ? "11sus2" : hasNinth ? "9sus2" : "7sus2";
        } else {
            // Natural eleventh in a bare sus2 chord = added 4th.
            suffix = hasEleventh ? "sus2(add4)" : "sus2";
        }
        break;

    case ChordQuality::Suspended4:
        if (hasMaj7 && hasNinthNatural) {
            suffix = "Maj9sus";
        } else if (hasMaj7) {
            suffix = "Maj7sus";
            if (hasNinthFlat)  { suffix += "b9"; }
            if (hasNinthSharp) { suffix += "#9"; }
        } else if (hasMin7) {
            // Base: highest implied extension.  Natural 9th only → "9sus".  Altered 9th or
            // no 9th → "7sus" (alteration appended below).  13th → "13sus".
            if (hasThirteenth) {
                suffix = "13sus";
            } else if (hasNinthNatural && !hasNinthFlat && !hasNinthSharp) {
                suffix = "sus(add9)";
            } else {
                suffix = "7sus";
            }
            // Catalog ordering: [b5|#5] [b9|#9] [#11] [b13]
            if (hasFlatFifth)       { suffix += "b5"; }
            else if (hasSharpFifth) { suffix += "#5"; }
            if (hasNinthFlat)       { suffix += "b9"; }
            else if (hasNinthSharp) { suffix += "#9"; }
            if (hasEleventhSharp)   { suffix += "#11"; }
            if (hasThirteenthFlat)  { suffix += "b13"; }
        } else {
            // MuseScore treats "sus" and "sus4" as synonymous; "sus" is the canonical
            // form that renders without doubling.  Augmented fourth uses "sus#4".
            if (hasNinthFlat || hasNinthSharp) {
                suffix = "sus";
                if (hasNinthFlat)       { suffix += "b9"; }
                else if (hasNinthSharp) { suffix += "#9"; }
            } else if (hasEleventhSharp) {
                suffix = "sus#4";
            } else if (hasNinthNatural) {
                // Natural 9th in a bare sus4 chord = added 2nd.
                suffix = "sus(add9)";
            } else {
                suffix = "sus";
            }
        }
        break;

    case ChordQuality::Power:
        suffix = "5";
        break;

    default:
        suffix = "";
        break;
    }

    // Append flat 13th when natural 5th is present alongside pc+8, and not already
    // covered by a hasThirteenth branch above (e.g. Maj7b13, bare 7b13 forms).
    // When no seventh is present (e.g. minor triad + b6), use "addb13" to match
    // notation (e.g. "Cmaddb13" = C minor add flat-13; this suffix form is used throughout the catalog).
    if (hasThirteenthFlat && !hasThirteenth && !endsWith(suffix, "b13")
            && quality != ChordQuality::Augmented) {
        const bool hasAnySeventh = hasMin7 || hasMaj7;
        suffix += hasAnySeventh ? "b13" : "addb13";
    }

    // For Suspended4, #5 is already appended inline above (before #11/b13 to match catalog
    // ordering).  Use contains-check to avoid double-appending for all other qualities.
    // b5 is suppressed when hasSharpFifth is true (mutually exclusive via detectExtensions).
    if (hasSharpFifth && quality != ChordQuality::Augmented
            && suffix.find("#5") == std::string::npos) {
        suffix += "#5";
    }
    if (hasFlatFifth && !hasSharpFifth && quality != ChordQuality::Diminished
               && quality != ChordQuality::HalfDiminished
               && suffix.find("b5") == std::string::npos) {
        // MuseScore convention: a plain major triad with flat 5 uses "5b" (e.g. "C5b"),
        // but when a seventh is already present the accidental precedes the interval ("C7b5").
        if (suffix.empty() && quality == ChordQuality::Major) {
            suffix = "5b";
        } else {
            suffix += "b5";
        }
    }

    return suffix;
}

// Returns a chromatic Roman numeral (e.g. "bVII", "bIII") for a chord whose
// root is not a diatonic scale degree in the current mode.
// semitone: (rootPc - keyTonicPc + 12) % 12 — interval from tonic to root.
// modeIdx:  0 = Ionian … 6 = Locrian.
// isMinorQuality: true → lower-case numeral (bvii, biii); false → upper-case.
// Returns "" if the root is more than 1 semitone from every scale degree
// (should not occur in standard 12-tone music).
static std::string chromaticRoman(int semitone, int modeIdx, bool isMinorQuality)
{
    static constexpr std::array<int, 7> SCALES[7] = {
        { 0, 2, 4, 5, 7, 9, 11 }, // Ionian
        { 0, 2, 3, 5, 7, 9, 10 }, // Dorian
        { 0, 1, 3, 5, 7, 8, 10 }, // Phrygian
        { 0, 2, 4, 6, 7, 9, 11 }, // Lydian
        { 0, 2, 4, 5, 7, 9, 10 }, // Mixolydian
        { 0, 2, 3, 5, 7, 8, 10 }, // Aeolian
        { 0, 1, 3, 5, 6, 8, 10 }, // Locrian
    };
    static constexpr const char* UPPER[7] = { "I","II","III","IV","V","VI","VII" };
    static constexpr const char* LOWER[7] = { "i","ii","iii","iv","v","vi","vii" };

    const std::array<int, 7>& scale = SCALES[modeIdx];

    // Prefer flat notation (one semitone below a scale degree) over sharp.
    for (int i = 0; i < 7; ++i) {
        if ((scale[i] - 1 + 12) % 12 == semitone) {
            return std::string("b") + (isMinorQuality ? LOWER[i] : UPPER[i]);
        }
    }
    // Fall back to sharp (one semitone above a scale degree).
    for (int i = 0; i < 7; ++i) {
        if ((scale[i] + 1) % 12 == semitone) {
            return std::string("#") + (isMinorQuality ? LOWER[i] : UPPER[i]);
        }
    }
    return "";
}

std::string diatonicRoman(const ChordAnalysisResult& r)
{
    if (r.function.degree < 0 || r.function.degree > 6) {
        return "";
    }

    static constexpr std::array<const char*, 7> UPPER = { "I", "II", "III", "IV", "V", "VI", "VII" };
    static constexpr std::array<const char*, 7> LOWER = { "i", "ii", "iii", "iv", "v", "vi", "vii" };

    const auto quality = r.identity.quality;
    std::string rn;

    // ── Base numeral (upper = major/aug/power/sus; lower = minor/dim/halfdim) ──
    switch (quality) {
    case ChordQuality::Major:
    case ChordQuality::Augmented:
    case ChordQuality::Power:
    case ChordQuality::Suspended2:
    case ChordQuality::Suspended4:
        rn = UPPER[static_cast<size_t>(r.function.degree)];
        break;
    case ChordQuality::Minor:
    case ChordQuality::Diminished:
    case ChordQuality::HalfDiminished:
        rn = LOWER[static_cast<size_t>(r.function.degree)];
        break;
    default:
        return "";
    }

    // ── Quality decoration ──
    if (quality == ChordQuality::Augmented) {
        rn += "+";
    } else if (quality == ChordQuality::Diminished) {
        rn += "o";
    }

    // ── Added-sixth / 6/9 (no 7th by definition) ──
    if (hasExtension(r.identity.extensions, Extension::AddedSixth) && (quality == ChordQuality::Major || quality == ChordQuality::Minor)) {
        rn += hasExtension(r.identity.extensions, Extension::NaturalNinth) ? "69" : "(add6)";
        return rn;
    }

    // ── Determine 7th presence and extension level ──
    // HalfDiminished structurally includes a minor 7th (suppressed in the flag
    // by detectExtensions), so treat it as having a 7th for level purposes.
    const bool hasAnySeventh = hasExtension(r.identity.extensions, Extension::MinorSeventh) || hasExtension(r.identity.extensions, Extension::MajorSeventh)
                               || (hasExtension(r.identity.extensions, Extension::DiminishedSeventh) && quality == ChordQuality::Diminished)
                               || quality == ChordQuality::HalfDiminished;

    // Extension level = highest natural extension when a 7th is present.
    // Natural 9th/11th/13th elevate the level number; altered forms (b9, #11, etc.)
    // are appended as suffixes without elevating it.
    int level = 0;
    if (hasAnySeventh) {
        if (hasExtension(r.identity.extensions, Extension::NaturalThirteenth))        level = 13;
        else if (hasExtension(r.identity.extensions, Extension::NaturalEleventh))     level = 11;
        else if (hasExtension(r.identity.extensions, Extension::NaturalNinth)) level = 9;
        else                        level = 7;
    }

    // ── Half-diminished: "ø" + level + alterations ──
    if (quality == ChordQuality::HalfDiminished) {
        rn += "\xc3\xb8";  // ø (U+00F8)
        rn += std::to_string(level);
        if (hasExtension(r.identity.extensions, Extension::FlatNinth))       rn += "b9";
        if (hasExtension(r.identity.extensions, Extension::SharpNinth))      rn += "#9";
        if (hasExtension(r.identity.extensions, Extension::SharpEleventh))   rn += "#11";
        if (hasExtension(r.identity.extensions, Extension::FlatThirteenth))  rn += "b13";
        return rn;
    }

    // ── Fully diminished 7th (no higher extensions in standard usage) ──
    if (quality == ChordQuality::Diminished && hasExtension(r.identity.extensions, Extension::DiminishedSeventh)) {
        rn += "7";
        return rn;
    }

    // ── Suspended chords: level + alterations + susN ──
    if (quality == ChordQuality::Suspended2 || quality == ChordQuality::Suspended4) {
        const char* susTag = (quality == ChordQuality::Suspended2) ? "sus2" : "sus4";
        if (level > 0) {
            if (hasExtension(r.identity.extensions, Extension::MajorSeventh)) rn += "M";
            rn += std::to_string(level);
            if (hasExtension(r.identity.extensions, Extension::FlatFifth))       rn += "b5";
            if (hasExtension(r.identity.extensions, Extension::SharpFifth))      rn += "#5";
            if (hasExtension(r.identity.extensions, Extension::FlatNinth))       rn += "b9";
            if (hasExtension(r.identity.extensions, Extension::SharpNinth))      rn += "#9";
            if (hasExtension(r.identity.extensions, Extension::SharpEleventh))   rn += "#11";
            if (hasExtension(r.identity.extensions, Extension::FlatThirteenth))  rn += "b13";
            rn += susTag;
        } else {
            rn += susTag;
        }
        return rn;
    }

    // ── Extension level for major/minor/augmented ──
    if (level > 0) {
        if (hasExtension(r.identity.extensions, Extension::MajorSeventh)) rn += "M";
        rn += std::to_string(level);
    }

    // ── Altered extensions as suffixes (only with a 7th present) ──
    // Suppress structural alterations: b5 is inherent to Diminished, #5 to Augmented.
    if (hasAnySeventh) {
        if (hasExtension(r.identity.extensions, Extension::FlatFifth) && quality != ChordQuality::Diminished)  rn += "b5";
        if (hasExtension(r.identity.extensions, Extension::SharpFifth) && quality != ChordQuality::Augmented)  rn += "#5";
        if (hasExtension(r.identity.extensions, Extension::FlatNinth))       rn += "b9";
        if (hasExtension(r.identity.extensions, Extension::SharpNinth))      rn += "#9";
        if (hasExtension(r.identity.extensions, Extension::SharpEleventh))   rn += "#11";
        if (hasExtension(r.identity.extensions, Extension::FlatThirteenth))  rn += "b13";
    }

    // ── "add" notation for extensions without a 7th ──
    if (!hasAnySeventh && quality != ChordQuality::Diminished) {
        if (hasExtension(r.identity.extensions, Extension::NaturalThirteenth)) {
            rn += "(add13)";
        } else if (hasExtension(r.identity.extensions, Extension::SharpEleventh)) {
            rn += "(add#11)";
        } else if (hasExtension(r.identity.extensions, Extension::NaturalEleventh)) {
            rn += "(add11)";
        } else if (hasExtension(r.identity.extensions, Extension::FlatNinth)) {
            rn += "(addb9)";
        } else if (hasExtension(r.identity.extensions, Extension::SharpNinth)) {
            rn += "(add#9)";
        } else if (hasExtension(r.identity.extensions, Extension::NaturalNinth)) {
            rn += "(add9)";
        }
    }

    return rn;
}

std::vector<int> coreIntervals(ChordQuality quality, bool hasMinorSeventh, bool hasMajorSeventh,
                                bool hasDiminishedSeventh)
{
    std::vector<int> intervals;

    switch (quality) {
    case ChordQuality::Major:
        intervals = { 0, 4, 7 };
        break;
    case ChordQuality::Minor:
        intervals = { 0, 3, 7 };
        break;
    case ChordQuality::HalfDiminished:
        intervals = { 0, 3, 6, 10 };
        return intervals;  // fixed structure — no further 7th appended
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

    if (hasDiminishedSeventh && quality == ChordQuality::Diminished) {
        intervals.push_back(9);
    } else if (hasMajorSeventh) {
        intervals.push_back(11);
    } else if (hasMinorSeventh) {
        intervals.push_back(10);
    }

    return intervals;
}

// Three-way classification for a note that is NOT part of the template being scored.
//
//   Extension    — neutral colour tone; adds slight evidence for the candidate.
//   Contradiction — structurally incompatible with the template quality; the note's
//                   presence is positive evidence *against* this candidate and earns
//                   a larger penalty than a merely foreign note.
//   Foreign      — neither; penalised at the standard rate.
//
// The distinction matters because a note that belongs to the defining core of a
// *different* quality (e.g. a minor 7th heard over a diminished-triad template,
// which defines half-diminished) should hurt the wrong candidate more than an
// unrelated passing tone does.
enum class ExtraNoteCategory { Extension, Contradiction, Foreign };

// A contradiction (a note that definitively excludes a template quality, e.g. a
// major third over a diminished template) is penalised more severely than a merely
// foreign note.  Theory-grounded ordering: contradiction penalty > foreign penalty.
// Absolute magnitude is empirically tuned against the regression corpus.
static constexpr double kContradictionPenalty = 0.75;

// ── Template tone scoring ────────────────────────────────────────────────────
//
// Theory basis: root identity is the strongest harmonic signal (1.8×); the second
// template tone (bass-position third or fifth) carries chord colour (1.2×); remaining
// tones are structural but less individually identifying (1.0×).  The relative ordering
// (root > second > other) is theory-grounded; the exact ratios are empirically tuned.
//
// Caps prevent any single heavily-doubled note from dominating the score.
static constexpr double kRootToneFactor          = 1.8;   // [theory-grounded ordering, empirical value]
static constexpr double kSecondToneFactor        = 1.2;   // [theory-grounded ordering, empirical value]
static constexpr double kOtherToneFactor         = 1.0;   // baseline
static constexpr double kTemplateToneWeightCap   = 3.0;   // [empirical]
static constexpr double kExtraNoteWeightCap      = 2.0;   // [empirical]

// ── Extension and foreign-note scoring ──────────────────────────────────────
//
// Theory basis: 7ths are the most common and unambiguous colour extensions, so they
// earn the highest extension reward.  b13/aug5 intervals are enharmonically ambiguous
// and can resemble inversions of other chords, so they earn less.  Other extensions
// (9ths, 11ths, #11s) fall between these extremes.  The ordering is theory-grounded;
// absolute values are empirically tuned.
//
// kForeignPenalty < kContradictionPenalty: a note that merely doesn't fit the template
// is less damaging than one that actively excludes it.  [theory-grounded ordering]
static constexpr double kExtensionFactor7th      = 0.45;  // m7/M7: common colour tone [empirical]
static constexpr double kExtensionFactorFlat13   = 0.20;  // b13/#5: inversion-ambiguous [empirical]
static constexpr double kExtensionFactorDefault  = 0.35;  // 9th, 11th, etc.  [empirical]
static constexpr double kForeignPenalty          = 0.45;  // neither extension nor contradiction [empirical]

// ── TPC-based Sus4 vs minor disambiguation ───────────────────────────────────
//
// A note 3 semitones above the root is enharmonically Eb (minor third) or D# (#9).
// Theory basis: a flat spelling (Eb) signals minor-third intent and suppresses the
// Sus4 reading; a sharp spelling (D#) signals #9 intent and is compatible with Sus4.
// The asymmetry (0.10 vs 0.45) reflects that Eb-over-Sus4 is a strong contradiction
// signal while D#-over-Sus4 is a mild confirmation.  Both values are empirical.
static constexpr double kSus4FlatThirdFactor     = 0.10;  // Eb spelling → minor intent  [empirical]
static constexpr double kSus4SharpThirdFactor    = 0.45;  // D# spelling → #9 intent     [empirical]

// ── Template-specific structural penalties and bonuses ───────────────────────
//
// Each constant keeps a template family self-consistent.  The ordering of related
// values (e.g. Sus4Variant > Sus4Maj7 because a missing 7th is a bigger ambiguity
// than a missing 5th) is theory-grounded; absolute values are empirically tuned.
static constexpr double kDim7CharacteristicBonus = 0.75;  // fully-diminished fingerprint confirmed [empirical]
static constexpr double kNonBassPenalty          = 0.35;  // Min7/Sus4/HalfDim: prefer bass-root reading [empirical]
static constexpr double kSus4VariantMissing7th   = 0.70;  // Sus4b5/Sus4#5 without defining m7 [empirical]
static constexpr double kSus4Maj7MissingP5       = 0.50;  // Sus4+Maj7 without P5 anchor [empirical]
static constexpr double kSus4MissingFourth       = 0.70;  // Sus4 without defining P4 (interval 5) [empirical]
static constexpr double kDom7FlatFiveTpcPenalty  = 0.55;  // dom7b5: enharmonic ambiguity without Gb TPC [empirical]
static constexpr double kDom7FlatFiveMissing7th  = 0.50;  // dom7b5 without minor 7th: too ambiguous [empirical]
static constexpr double kPowerChord3PcPenalty    = 0.30;  // power chord with 3+ pcs: triadic reading preferred [empirical]
static constexpr double kBassSupportPresenceThreshold = 0.05;  // matches distinct-PC presence threshold

/// Minimum pcWeight for a seventh interval (min7 = +10, maj7 = +11) to register
/// as a chord seventh extension.  Seventh notes in lightly-voiced jazz chords
/// consistently appear in the 0.12–0.19 range (below the 0.20 general threshold)
/// so a separate, lower guard is needed.
/// Must be strictly above the max(0.1, weight) floor (0.1) applied in analyzeChord.
static constexpr double kSeventhThreshold        = 0.12;

/// Minimum pcWeight for all other chord extensions (9th, 11th, 13th, alterations).
/// Conservative at 0.20 so that brief ornamental notes in non-jazz contexts
/// (passing tones, neighbor notes) do not trigger false extension labels.
static constexpr double kExtensionThreshold      = 0.20;

// Fraction of the best raw score below which candidates are discarded.  [empirical]
static constexpr double kScoreThresholdRatio     = 0.75;

/// Classify a non-template interval relative to a chord quality.
///
/// Pure classifier: takes only the interval (already normalised, 0–11) and the
/// quality; assumes the most permissive interpretation for ambiguous cases.
/// Specifically:
///   - Major  + m3 (rel==3): defaults to Extension (assumes M3 also sounding → #9).
///     Becomes Contradiction when M3 is absent — caller must apply that override.
///   - Sus4   + m3 (rel==3): defaults to Extension (assumes P4 also sounding → #9).
///     Becomes Contradiction when P4 is absent — caller must apply that override.
///
/// All other context-sensitive corrections (TPC-based factor adjustments, etc.)
/// are likewise the caller's responsibility.
ExtraNoteCategory categorizeExtraNote(int rel, ChordQuality quality)
{
    // Quality-specific contradictions: intervals that definitively identify a
    // different quality.  Context-dependent cases (Major/m3, Sus4/m3) are handled
    // in the caller.
    switch (quality) {
    case ChordQuality::Minor:
        if (rel == 4)  return ExtraNoteCategory::Contradiction; // M3  → not minor
        break;
    case ChordQuality::Suspended4:
        if (rel == 4)  return ExtraNoteCategory::Contradiction; // M3  → not sus4
        // m3 defaults to Extension; Contradiction when P4 absent — caller checks.
        break;
    case ChordQuality::Suspended2:
        if (rel == 3)  return ExtraNoteCategory::Contradiction; // m3  → not sus2
        if (rel == 4)  return ExtraNoteCategory::Contradiction; // M3  → not sus2
        break;
    case ChordQuality::Diminished:
        if (rel == 4)  return ExtraNoteCategory::Contradiction; // M3  → not diminished
        if (rel == 7)  return ExtraNoteCategory::Contradiction; // P5  → not diminished (requires ♭5) // BUG-10
        if (rel == 10) return ExtraNoteCategory::Contradiction; // m7  → half-diminished
        if (rel == 11) return ExtraNoteCategory::Contradiction; // M7  → not diminished
        break;
    case ChordQuality::HalfDiminished:
        if (rel == 4)  return ExtraNoteCategory::Contradiction; // M3  → not half-dim
        if (rel == 9)  return ExtraNoteCategory::Contradiction; // dim7 → fully diminished
        if (rel == 11) return ExtraNoteCategory::Contradiction; // M7  → not half-dim
        break;
    default:
        break;
    }

    // Neutral colour/extension intervals: valid additions for most qualities.
    switch (rel) {
    case 1:  // b9
    case 2:  // 9
    case 3:  // #9 (dual-use with minor 3rd; context overrides handled in caller)
    case 5:  // 11
    case 6:  // #11 / b5
    case 8:  // b13 / #5
    case 9:  // 13 / 6
    case 10: // minor 7
    case 11: // major 7
        return ExtraNoteCategory::Extension;
    default:
        return ExtraNoteCategory::Foreign;
    }
}

std::string romanWithInversion(const std::string& roman, ChordQuality quality, int rootPc, int bassPc,
                               bool hasMinorSeventh, bool hasMajorSeventh, bool hasDiminishedSeventh)
{
    if (roman.empty() || bassPc == rootPc) {
        return roman;
    }

    const int bassInterval = normalizePc(bassPc - rootPc);
    const std::vector<int> intervals = coreIntervals(quality, hasMinorSeventh, hasMajorSeventh,
                                                     hasDiminishedSeventh);

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

/// Compute all extension and alteration flags from a pitch-class weight histogram,
/// given the best root pitch class and quality.
struct ExtensionFlags {
    bool hasMinorSeventh    = false;
    bool hasMajorSeventh    = false;
    bool hasDiminishedSeventh = false;
    bool hasAddedSixth      = false;
    bool hasNinth           = false;
    bool hasNinthNatural    = false;
    bool hasNinthFlat       = false;
    bool hasNinthSharp      = false;
    bool hasEleventh        = false;
    bool hasEleventhSharp   = false;
    bool hasThirteenth      = false;
    bool hasThirteenthFlat  = false;
    bool hasThirteenthSharp = false;
    bool hasSharpFifth      = false;
    bool hasFlatFifth       = false;
    bool isSixNine          = false;
};

ExtensionFlags detectExtensions(const std::array<double, 12>& pcWeight,
                                int rootPc,
                                ChordQuality quality,
                                const std::array<int, 12>& tpcForPc,
                                int rootTpc,
                                double extThreshold = kExtensionThreshold)
{
    auto w = [&](int semitones) -> double {
        return pcWeight[static_cast<size_t>((rootPc + semitones) % 12)];
    };

    ExtensionFlags f;

    const bool rawMin7  = w(10) > kSeventhThreshold;
    const bool rawMaj7  = w(11) > kSeventhThreshold;
    const bool rawDim7  = (quality == ChordQuality::Diminished) && (w(9) > extThreshold);

    // For HalfDiminished the minor 7th is structural, not an "added" extension.
    // Also suppress if pitch class 10 is spelled as A# (#13) rather than Bb (min7).
    {
        const int pc10 = static_cast<size_t>((rootPc + 10) % 12);
        const int tpc10 = tpcForPc[static_cast<size_t>(pc10)];
        const bool isSharp13Spelling = (rootTpc >= 0 && tpc10 >= 0)
                                       && (tpc10 - rootTpc == 10);
        f.hasMinorSeventh = rawMin7 && !rawMaj7
                            && quality != ChordQuality::HalfDiminished
                            && !isSharp13Spelling;
    }
    f.hasMajorSeventh     = rawMaj7;
    f.hasDiminishedSeventh = rawDim7;

    f.hasAddedSixth = w(9) > extThreshold && !rawMin7 && !rawMaj7
                      && quality != ChordQuality::Diminished;

    f.hasNinthNatural = w(2) > extThreshold;
    f.hasNinthFlat    = w(1) > extThreshold;
    // Interval 3 is the minor 3rd in minor/diminished templates — exclude it.
    // For Major quality, also require a major 3rd (interval 4) to be present:
    // without it the note at interval 3 is the minor 3rd of a minor chord, not
    // a #9 (e.g. {A,C,E} is Am, not Aadd#9).  Suspended chords have no major
    // 3rd by definition, so the requirement is skipped for them.
    f.hasNinthSharp   = w(3) > extThreshold
                        && (quality != ChordQuality::Major || w(4) > extThreshold)
                        && quality != ChordQuality::Minor
                        && quality != ChordQuality::Diminished
                        && quality != ChordQuality::HalfDiminished;
    f.hasNinth        = f.hasNinthNatural || f.hasNinthFlat || f.hasNinthSharp;

    f.hasEleventh = w(5) > extThreshold;  // P4: stays at general threshold

    const bool hasSeventh = rawMin7 || rawMaj7 || rawDim7
                            || f.hasEleventh || f.hasNinthNatural;
    f.hasThirteenth = w(9) > extThreshold && hasSeventh;
    // A# (#13) vs Bb (min7): same pitch class, distinguished by TPC.
    // TPC delta from root: min7 = -2, aug6 (#13) = +10.
    {
        const int pc10 = static_cast<size_t>((rootPc + 10) % 12);
        const int tpc10 = tpcForPc[static_cast<size_t>(pc10)];
        const bool isSharp13Spelling = (rootTpc >= 0 && tpc10 >= 0)
                                       && (tpc10 - rootTpc == 10);
        f.hasThirteenthSharp = w(10) > extThreshold && isSharp13Spelling
                               && quality != ChordQuality::Diminished;
    }

    // Natural 5th presence distinguishes #5 (no natural 5th) from b13 (natural 5th
    // also present).  For Augmented quality the #5 is structural, not an extension.
    const bool naturalFifthPresent = (quality != ChordQuality::Augmented) && (w(7) > extThreshold);

    // pc+6: distinguish b5 (flat Gb spelling, no natural 5th) from #11 (sharp F# spelling
    // or natural 5th also present).  Compute first so hasFlatFifth is available for
    // the fifthSlotFilled check on pc+8 below.
    const bool rawFlatFifth = w(6) > extThreshold
                              && quality != ChordQuality::Diminished
                              && quality != ChordQuality::HalfDiminished;
    {
        const int pc6  = (rootPc + 6) % 12;
        const int tpc6 = tpcForPc[static_cast<size_t>(pc6)];
        // Positive TPC delta from root = sharp direction (F# from C: 21-15=+6).
        // Natural 5th present → always #11.  Sharp spelling → #11.  Otherwise b5.
        const bool tpcSpellsAsSharp = (rootTpc >= 0 && tpc6 >= 0) && (tpc6 - rootTpc > 0);
        const bool preferSharp11    = rawFlatFifth && (naturalFifthPresent || tpcSpellsAsSharp);
        f.hasFlatFifth = rawFlatFifth && !preferSharp11;
    }
    // Suppress #11 flag when treating pc+6 as b5 to avoid double-counting.
    // Also suppress for HalfDiminished: the b5 is structural there (rawFlatFifth
    // is blocked above), so hasFlatFifth is always false for half-dim even though
    // the note at +6 is the chord's own diminished fifth, not an added #11.
    f.hasEleventhSharp = w(6) > 0.3 && !f.hasFlatFifth
                         && quality != ChordQuality::HalfDiminished;

    // pc+8: flat-13th when a "fifth slot" is filled (natural 5th or flat 5th present);
    // augmented-5th (#5) otherwise.  When a b5 (Gb) already occupies the fifth slot,
    // Ab functions as b13 rather than #5 — consistent with how the catalog annotates this interval.
    //
    // Special case for Minor quality: the b6 interval (pc+8 spelled as Ab, TPC < rootTpc)
    // is the natural b13 of the minor scale.  Treat it as b13 even without a natural 5th,
    // as long as the TPC spelling confirms a flat direction (Ab, not G#).
    const int pc8  = (rootPc + 8) % 12;
    const int tpc8 = tpcForPc[static_cast<size_t>(pc8)];
    const bool tpc8SpellsAsFlat = (rootTpc >= 0 && tpc8 >= 0) && (tpc8 - rootTpc < 0);
    const bool fifthSlotFilled = naturalFifthPresent || f.hasFlatFifth;
    const bool fifthSlotOrMinorFlat6 = fifthSlotFilled
                                       || (quality == ChordQuality::Minor && tpc8SpellsAsFlat);
    f.hasSharpFifth     = w(8) > extThreshold && !fifthSlotOrMinorFlat6;
    // Allow b13 without a 7th for Minor quality only when the perfect 5th is also present
    // (e.g. "Cmaddb13" = {C,Eb,G,Ab}).  Without the 5th, {root,m3,b6} is more parsimoniously
    // a first-inversion major triad (e.g. {G,Bb,Eb} = Eb/G), so we suppress the b13 label.
    f.hasThirteenthFlat = w(8) > 0.3 && fifthSlotOrMinorFlat6
                          && (hasSeventh || (quality == ChordQuality::Minor && w(7) > 0.2));

    f.isSixNine = f.hasAddedSixth && f.hasNinthNatural && !rawMin7 && !rawMaj7;

    return f;
}

// ── Chord template definition ──────────────────────────────────────────────

/// A chord template: quality, intervals from root (semitones), and expected
/// TPC (circle-of-fifths) deltas for each interval.
///
/// TPC deltas encode the expected circle-of-fifths distance per interval:
///   P5=+1, M3=+4, m3=−3, P4=−1, A5=+8, d5=−6, m7=−2, M2=+2, A4=+6.
/// Used to score enharmonic-spelling consistency when TPC data is available.
struct TemplateDef {
    ChordQuality quality;
    std::vector<int> intervals;
    std::vector<int> tpcDeltas;  // parallel to intervals; tpcDeltas[0] is always 0 (root)
};

// ── Per-candidate scoring helpers ──────────────────────────────────────────
//
// The analyzeChord scoring loop calls one function per concern.  Each helper
// returns a signed score delta and is independently readable and testable.

/// Weighted sum of the template tones' presence in the input.
/// Absent template tones contribute zero (their pcWeight is near zero).
double scoreTemplateTones(const TemplateDef& tpl, int rootPc,
                          const std::array<double, 12>& pcWeight)
{
    double score = 0.0;
    for (size_t i = 0; i < tpl.intervals.size(); ++i) {
        const int chordPc = (rootPc + tpl.intervals[i]) % 12;
        const double w    = pcWeight[static_cast<size_t>(chordPc)];
        const double factor = (i == 0) ? kRootToneFactor
                            : (i == 1) ? kSecondToneFactor
                                       : kOtherToneFactor;
        score += factor * std::min(w, kTemplateToneWeightCap);
    }
    return score;
}

/// Signed contribution of all non-template pitch classes.
/// Positive for extensions, negative for contradictions and foreign notes.
///
/// Also applies two context-sensitive classification overrides that the pure
/// categorizeExtraNote classifier cannot handle on its own:
///   - Major/m3:  Contradiction when M3 is absent (not a #9 — it's a real minor 3rd).
///   - Sus4/m3:   Contradiction when P4 is absent (no sus4 sound without the defining P4).
/// And a TPC-based sus4 vs minor soft factor adjustment for the #9/m3 ambiguity.
double scoreExtraNotes(const TemplateDef& tpl, int rootPc,
                       const std::array<double, 12>& pcWeight,
                       const std::array<int, 12>& tpcForPc)
{
    // Standard Sus4 = Sus4 with P5 present (intervals[2]==7).
    // Only standard Sus4 templates use the TPC sus4/minor disambiguation.
    // Sus4-variant templates (altered P5: Sus4b5, Sus4#5) legitimately use Eb as a
    // #9 colour tone and should not have their extension factor reduced.
    const bool sus4Standard = (tpl.quality == ChordQuality::Suspended4
                               && (tpl.intervals.size() < 3 || tpl.intervals[2] == 7));

    double score = 0.0;
    for (int pc = 0; pc < 12; ++pc) {
        const double w = pcWeight[static_cast<size_t>(pc)];
        if (w < 0.01) {
            continue;  // not sounding — contributes nothing regardless of classification
        }

        bool inTemplate = false;
        for (int interval : tpl.intervals) {
            if (((rootPc + interval) % 12) == pc) { inTemplate = true; break; }
        }
        if (inTemplate) {
            continue;
        }

        const int rel = normalizePc(pc - rootPc);
        ExtraNoteCategory cat = categorizeExtraNote(rel, tpl.quality);

        // Context-sensitive classification overrides (cannot be done in the pure classifier).
        if (tpl.quality == ChordQuality::Major && rel == 3) {
            // m3 is a #9 colour tone only when M3 is also sounding.
            if (pcWeight[static_cast<size_t>((rootPc + 4) % 12)] < 0.1) {
                cat = ExtraNoteCategory::Contradiction;
            }
        }
        if (tpl.quality == ChordQuality::Suspended4 && rel == 3) {
            // m3 is a #9 colour tone only when P4 (the defining Sus4 interval) is present.
            if (pcWeight[static_cast<size_t>(normalizePc(rootPc + 5))] < 0.1) {
                cat = ExtraNoteCategory::Contradiction;
            }
        }

        if (cat == ExtraNoteCategory::Extension) {
            double extensionFactor = (rel == 10 || rel == 11) ? kExtensionFactor7th
                                   : (rel == 8)               ? kExtensionFactorFlat13
                                                              : kExtensionFactorDefault;

            // TPC-based sus4 vs minor disambiguation for the minor-3rd / #9 position.
            // Eb spelling (TPC = rootTpc − 3) → likely a real minor third, suppress Sus4.
            // D# spelling (TPC = rootTpc + 9) → #9 intent confirmed, boost Sus4 slightly.
            if (sus4Standard && rel == 3) {
                const int rootTpc = tpcForPc[static_cast<size_t>(rootPc)];
                const int noteTpc = tpcForPc[static_cast<size_t>(pc)];
                if (rootTpc >= 0 && noteTpc >= 0) {
                    if (noteTpc == rootTpc - 3) {
                        extensionFactor = kSus4FlatThirdFactor;
                    } else if (noteTpc == rootTpc + 9) {
                        extensionFactor = kSus4SharpThirdFactor;
                    }
                }
            }

            score += extensionFactor * std::min(w, kExtraNoteWeightCap);
        } else if (cat == ExtraNoteCategory::Contradiction) {
            score -= kContradictionPenalty * std::min(w, kExtraNoteWeightCap);
        } else {
            score -= kForeignPenalty * std::min(w, kExtraNoteWeightCap);
        }
    }
    return score;
}

/// Bonus for Diminished templates when a non-diatonic dim7 interval is present.
/// The dim7 (9 semitones from root) fingerprints the true diminished root: when it is
/// non-diatonic in the current key it confirms this root over chord inversions.
double dim7CharacteristicBonus(const TemplateDef& tpl, int rootPc,
                               const std::array<double, 12>& pcWeight,
                               int keyTonicPc,
                               const std::array<int, 7>& scale,
                               double extThreshold = kExtensionThreshold)
{
    if (tpl.quality != ChordQuality::Diminished) {
        return 0.0;
    }
    const int dim7Pc = (rootPc + 9) % 12;
    if (pcWeight[static_cast<size_t>(dim7Pc)] <= extThreshold) {
        return 0.0;
    }
    for (int interval : scale) {
        if ((keyTonicPc + interval) % 12 == dim7Pc) {
            return 0.0;  // diatonic — no bonus
        }
    }
    return kDim7CharacteristicBonus;
}

/// TPC match counts for non-root template tones.
/// Used by nonBassAdjustment and tpcConsistencyBonus to avoid duplicating the
/// same iteration pattern.
struct TpcMatchCounts {
    int present = 0;  ///< Non-root template tones that have TPC data.
    int matched = 0;  ///< Of those, tones whose TPC equals the expected value.
};

/// Count TPC matches for non-root intervals of \p tpl rooted at \p rootPc.
/// Returns all-zero when the root has no TPC data (cannot compute expected values).
TpcMatchCounts countTpcMatches(const TemplateDef& tpl, int rootPc,
                                const std::array<int, 12>& tpcForPc)
{
    const int rootTpc = tpcForPc[static_cast<size_t>(rootPc)];
    if (rootTpc < 0) {
        return {};
    }
    TpcMatchCounts counts;
    for (size_t i = 1; i < tpl.intervals.size(); ++i) {
        const int chordPc   = (rootPc + tpl.intervals[i]) % 12;
        const int actualTpc = tpcForPc[static_cast<size_t>(chordPc)];
        if (actualTpc >= 0) {
            ++counts.present;
            if (actualTpc == rootTpc + tpl.tpcDeltas[i]) {
                ++counts.matched;
            }
        }
    }
    return counts;
}

/// Net score adjustment for templates that carry a non-bass penalty, with a
/// TPC-spelling waiver when that evidence is authoritative.
///
/// Minor7, any 4-note Sus4, and HalfDim templates are penalised when their root is
/// not the bass note: re-labelling from the bass is almost always preferable
/// (e.g. Am7 from non-bass root A is better labelled C6 or C/E).
///
/// The penalty is waived when every non-root template tone that has TPC data is
/// spelled exactly right for this root/quality — the composer's enharmonic spelling
/// then overrides the bass-root preference.
///
/// Exception: Sus4-variant templates (Sus4b5/Sus4♯5) are excluded from the waiver.
/// Their altered fifth makes TPC evidence less discriminating from non-bass roots
/// (e.g. {C,Db,F,G} should label as Csusb9, not G7susb5/C).
double nonBassAdjustment(const TemplateDef& tpl, int rootPc, int bassPc,
                         const std::array<int, 12>& tpcForPc)
{
    const bool isSus4Any = (tpl.quality == ChordQuality::Suspended4
                            && tpl.intervals.size() == 4);
    const bool isMinor4  = (tpl.quality == ChordQuality::Minor
                            && tpl.intervals.size() == 4);
    const bool isHalfDim = (tpl.quality == ChordQuality::HalfDiminished);

    if (!(isSus4Any || isMinor4 || isHalfDim) || rootPc == bassPc) {
        return 0.0;  // penalty does not apply to this template or this root
    }

    const bool isSus4Variant = (tpl.quality == ChordQuality::Suspended4
                                && tpl.intervals.size() == 4
                                && tpl.intervals[2] != 7);

    const TpcMatchCounts tpc = countTpcMatches(tpl, rootPc, tpcForPc);
    const bool waiverApplies = (!isSus4Variant
                                && tpc.present > 0
                                && tpc.matched == tpc.present);
    return waiverApplies ? 0.0 : -kNonBassPenalty;
}

/// Penalties for structural notes that are absent or enharmonically ambiguous.
///
/// Each penalty keeps a template family self-consistent: the template scores well
/// only when its own characteristic intervals are present and correctly spelled.
double structuralPenalties(const TemplateDef& tpl, int rootPc,
                           const std::array<double, 12>& pcWeight,
                           const std::array<int, 12>& tpcForPc,
                           int distinctPcs,
                           double extThreshold = kExtensionThreshold)
{
    double score = 0.0;

    // Sus4 templates (except Sus4b5): the P4 is the defining suspension tone.
    // Penalise when it is absent or too weak to sustain a suspension reading.
    // Without a detectable fourth the chord sounds augmented or altered, not suspended.
    //
    // Sus4b5 {0,5,6,10} (intervals[2]==6) is excluded: in that variant the tritone (b5)
    // is the identifying characteristic.  Sus4b5 from C legitimately wins for chords like
    // {C,F#,Bb,D} (Lydian dominant / C7♭5 spelling) where P4=F is genuinely absent.
    // Applying the penalty there pushes the root away from C toward D, which is incorrect
    // per corpus ground truth.  Sus4♯5 and standard Sus4 are still penalised.
    const bool sus4HasPerfectFourth = (tpl.quality == ChordQuality::Suspended4)
                                      && std::any_of(tpl.intervals.begin(), tpl.intervals.end(),
                                                     [](int i) { return i == 5; });
    const bool isSus4FlatFive = (tpl.quality == ChordQuality::Suspended4)
                                && tpl.intervals.size() >= 3
                                && tpl.intervals[2] == 6;
    if (sus4HasPerfectFourth && !isSus4FlatFive) {
        const int fourthPc = static_cast<int>((rootPc + 5) % 12);
        if (pcWeight[static_cast<size_t>(fourthPc)] < extThreshold) {
            score -= kSus4MissingFourth;
        }
    }

    // Sus4-variant (Sus4b5 / Sus4♯5): penalise when the minor-7th is absent.
    // Without it, {root, P4, b5/♯5} is ambiguous with simpler chord inversions.
    const bool isSus4Variant = (tpl.quality == ChordQuality::Suspended4
                                && tpl.intervals.size() == 4
                                && tpl.intervals[2] != 7);
    if (isSus4Variant) {
        const int seventhPc = (rootPc + tpl.intervals[3]) % 12;
        if (pcWeight[static_cast<size_t>(seventhPc)] < 0.05) {
            score -= kSus4VariantMissing7th;
        }
    }

    // Sus4+Maj7: penalise when the perfect fifth is absent.
    // Without it, {root, P4, Maj7} is ambiguous with simpler chord inversions.
    const bool isSus4Maj7 = (tpl.quality == ChordQuality::Suspended4
                              && tpl.intervals.size() == 4
                              && tpl.intervals[3] == 11);
    if (isSus4Maj7) {
        const int fifthPc = (rootPc + 7) % 12;
        if (pcWeight[static_cast<size_t>(fifthPc)] < 0.05) {
            score -= kSus4Maj7MissingP5;
        }
    }

    // Dom7b5: the tritone (interval 6) is enharmonically ambiguous between
    // dom7b5 (Gb, TPC delta −6) and Lydian-dominant / augmented (F#, TPC delta +6).
    // Penalise unless TPC data confirms the Gb (flat-5th) spelling.
    // Also penalise when the minor 7th is absent: {root, M3, b5} alone is ambiguous.
    const bool isDom7FlatFive = (tpl.quality == ChordQuality::Major
                                  && tpl.intervals.size() == 4
                                  && tpl.intervals[2] == 6);
    if (isDom7FlatFive) {
        const int tritonePc  = (rootPc + 6) % 12;
        const int rootTpcNow = tpcForPc[static_cast<size_t>(rootPc)];
        const int tritTpcNow = tpcForPc[static_cast<size_t>(tritonePc)];
        const bool flatFiveConfirmed = (rootTpcNow >= 0 && tritTpcNow >= 0
                                        && tritTpcNow - rootTpcNow == -6);
        if (!flatFiveConfirmed) {
            score -= kDom7FlatFiveTpcPenalty;
        }
        const int minorSeventhPc = (rootPc + tpl.intervals[3]) % 12;
        if (pcWeight[static_cast<size_t>(minorSeventhPc)] < 0.05) {
            score -= kDom7FlatFiveMissing7th;
        }
    }

    // Power chord: with 3+ distinct pitch classes a triadic interpretation is
    // almost always preferable.
    if (tpl.quality == ChordQuality::Power && distinctPcs >= 3) {
        score -= kPowerChord3PcPenalty;
    }

    return score;
}

/// Per-tone TPC spelling-consistency bonus.
/// For each non-root template tone whose actual TPC matches the expected TPC
/// for this root and quality, add prefs.tpcConsistencyBonusPerTone.
double tpcConsistencyBonus(const TemplateDef& tpl, int rootPc,
                           const std::array<int, 12>& tpcForPc,
                           const ChordAnalyzerPreferences& prefs)
{
    const TpcMatchCounts tpc = countTpcMatches(tpl, rootPc, tpcForPc);
    return tpc.matched * prefs.tpcConsistencyBonusPerTone;
}

double bassRootBonusMultiplier(const TemplateDef& tpl,
                               int rootPc,
                               const std::array<double, 12>& pcWeight,
                               const ChordAnalyzerPreferences& prefs)
{
    const auto hasPitchClass = [&](int pc) {
        return pcWeight[static_cast<size_t>(normalizePc(pc))] > kBassSupportPresenceThreshold;
    };

    const bool templateHasThird = std::any_of(tpl.intervals.begin(), tpl.intervals.end(),
                                              [](int interval) {
        return interval == 3 || interval == 4;
    });
    const bool hasMatchingTemplateThird = std::any_of(tpl.intervals.begin(), tpl.intervals.end(),
                                                      [&](int interval) {
        return (interval == 3 || interval == 4)
               && hasPitchClass(rootPc + interval);
    });

    const bool hasTemplateFifth = std::any_of(tpl.intervals.begin(), tpl.intervals.end(),
                                              [&](int interval) {
        return (interval == 6 || interval == 7 || interval == 8)
               && hasPitchClass(rootPc + interval);
    });
    const bool isBareSuspensionTriad = ((tpl.quality == ChordQuality::Suspended2
                                         || tpl.quality == ChordQuality::Suspended4)
                                        && tpl.intervals.size() == 3);

    if (hasTemplateFifth) {
        if (hasMatchingTemplateThird) {
            return 1.0;
        }

        if (!templateHasThird) {
            // Bare sus triads should not outrank omitted-third triads purely because
            // the suspension template receives a full bass-root bonus.
            return isBareSuspensionTriad ? prefs.bassRootThirdOnlyMultiplier : 1.0;
        }

        // Root plus fifth is materially stronger than bass alone, even when the third
        // is omitted from the local sonority.
        return prefs.bassRootThirdOnlyMultiplier;
    }

    if (hasPitchClass(rootPc + 3) || hasPitchClass(rootPc + 4)) {
        return prefs.bassRootThirdOnlyMultiplier;
    }

    return prefs.bassRootAloneMultiplier;
}

bool templateHasMatchingThird(const TemplateDef& tpl,
                              int rootPc,
                              const std::array<double, 12>& pcWeight)
{
    return std::any_of(tpl.intervals.begin(), tpl.intervals.end(),
                       [&](int interval) {
        return (interval == 3 || interval == 4)
               && pcWeight[static_cast<size_t>(normalizePc(rootPc + interval))] > 0.05;
    });
}

bool templateHasMatchingFifth(const TemplateDef& tpl,
                              int rootPc,
                              const std::array<double, 12>& pcWeight)
{
    return std::any_of(tpl.intervals.begin(), tpl.intervals.end(),
                       [&](int interval) {
        return (interval == 6 || interval == 7 || interval == 8)
               && pcWeight[static_cast<size_t>(normalizePc(rootPc + interval))] > 0.05;
    });
}

bool qualifiesForCompleteTriadInversionBonus(const TemplateDef& tpl,
                                             int rootPc,
                                             int bassPc,
                                             const std::array<double, 12>& pcWeight,
                                             int distinctPcs)
{
    if (distinctPcs != 3 || rootPc == bassPc) {
        return false;
    }

    const bool supportedQuality = (tpl.quality == ChordQuality::Major
                                   || tpl.quality == ChordQuality::Minor
                                   || tpl.quality == ChordQuality::Diminished);
    if (!supportedQuality) {
        return false;
    }

    return templateHasMatchingThird(tpl, rootPc, pcWeight)
           && templateHasMatchingFifth(tpl, rootPc, pcWeight);
}

bool supportsContextualInversionBonuses(const TemplateDef& tpl,
                                        int rootPc,
                                        int bassPc,
                                        const std::array<double, 12>& pcWeight)
{
    const bool isInvertedMajMin = (rootPc != bassPc)
                                  && (tpl.quality == ChordQuality::Major || tpl.quality == ChordQuality::Minor);
    return isInvertedMajMin && templateHasMatchingThird(tpl, rootPc, pcWeight);
}

double appliedBassRootBonus(const TemplateDef& tpl,
                            int rootPc,
                            int bassPc,
                            const std::array<double, 12>& pcWeight,
                            const ChordAnalyzerPreferences& prefs)
{
    if (rootPc != bassPc) {
        return 0.0;
    }

    return prefs.bassNoteRootBonus * bassRootBonusMultiplier(tpl, rootPc, pcWeight, prefs);
}

/// Score bonuses derived from musical context: bass note, key membership, and temporal
/// information from the preceding chord.
double contextualBonuses(const TemplateDef& tpl, int rootPc, int bassPc,
                         double appliedBassBonus,
                         int distinctPcs,
                         const std::array<double, 12>& pcWeight,
                         int keyTonicPc, const std::array<int, 7>& scale,
                         const ChordAnalyzerPreferences& prefs,
                         const ChordTemporalContext* context)
{
    double score = 0.0;
    const bool hasStepwiseBassEvidence = context
                                         && (context->bassIsStepwiseFromPrevious
                                             || context->bassIsStepwiseToNext);

    // Only award the full bass-root bonus when the accumulated tones support root position.
    score += appliedBassBonus;

    // Only use this inversion preference when adjacent bass motion says the bass note is likely passing.
    if (hasStepwiseBassEvidence
            && qualifiesForCompleteTriadInversionBonus(tpl, rootPc, bassPc, pcWeight, distinctPcs)) {
        score += prefs.completeTriadInversionBonus;
    }

    // Prefer roots that belong to the current key scale.
    for (int interval : scale) {
        if ((keyTonicPc + interval) % 12 == rootPc) {
            score += prefs.diatonicRootBonus;
            break;
        }
    }

    if (context) {
        // Root-continuity: prefer keeping the same root across successive chords.
        if (context->previousRootPc == rootPc) {
            score += prefs.rootContinuityBonus;
        }

        // Contextual inversion bonuses — §4.1b
        // Only for inverted Major/Minor candidates (lesson from three-attempt
        // inversion fix history: never apply to Diminished/HalfDiminished/Augmented).
        const bool isInvertedMajMin = supportsContextualInversionBonuses(tpl, rootPc, bassPc, pcWeight);

        if (isInvertedMajMin) {
            if (context->bassIsStepwiseFromPrevious) {
                score += prefs.stepwiseBassInversionBonus;
            }
            if (context->bassIsStepwiseToNext) {
                score += prefs.stepwiseBassLookaheadBonus;
            }
            if (context->previousRootPc != -1
                    && context->previousRootPc == rootPc) {
                score += prefs.sameRootInversionBonus;
            }
        }

        // Quality-guided resolution bias: reward candidates at the typical
        // resolution target of the previous chord's quality.
        if (context->previousQuality != ChordQuality::Unknown
                && context->previousRootPc >= 0) {
            const int prevRoot = context->previousRootPc;
            const ChordQuality prevQ = context->previousQuality;
            const double rb = prefs.resolutionBonus;

            // viio(7) → I: diminished resolves up by a semitone.
            if (prevQ == ChordQuality::Diminished
                    && (tpl.quality == ChordQuality::Major || tpl.quality == ChordQuality::Minor)
                    && rootPc == (prevRoot + 1) % 12) {
                score += rb;
            }
            // ii∅7 → V: half-diminished resolves up by a perfect fourth.
            if (prevQ == ChordQuality::HalfDiminished
                    && tpl.quality == ChordQuality::Major
                    && rootPc == (prevRoot + 5) % 12) {
                score += rb;
            }
            // I+ → I (return): augmented resolves back to the same root.
            if (prevQ == ChordQuality::Augmented
                    && (tpl.quality == ChordQuality::Major || tpl.quality == ChordQuality::Minor)
                    && rootPc == prevRoot) {
                score += rb;
            }
        }
    }

    return score;
}

// ── Confidence normalization (§P8d) ────────────────────────────────────────────
//
// Maps the score gap between winner and runner-up through a sigmoid to produce
// a 0.0–1.0 normalizedConfidence value.  Sigmoid shape and k parameter mirror
// KeyModeAnalyzer's implementation so the two confidence values are comparable.
static double normalizeChordConfidence(double winnerScore, double runnerUpScore,
                                       const ChordAnalyzerPreferences& prefs)
{
    const double gap = winnerScore - runnerUpScore;
    return 1.0 / (1.0 + std::exp(-prefs.confidenceSigmoidSteepness
                                  * (gap - prefs.confidenceSigmoidMidpoint)));
}

/// Returns true if bassPc is a chord tone of the chord identified by (rootPc, quality,
/// extensions).  Used by the two-pass pedal detection to decide whether the bass note
/// belongs to the upper-voice chord or is a structural pedal point.
///
/// Checks: (1) quality-defined triad intervals, (2) 7th/9th extensions that are
/// explicitly detected in the extension bitmask.  This correctly handles F13/Eb
/// (Eb = m7 of F, MinorSeventh set → true → no pedal detected) and HalfDiminished
/// (m7 is implicit in that quality → true for interval 10).
static bool isBassChordTone(int bassPc, int rootPc, ChordQuality quality, uint32_t extensions)
{
    const int interval = (bassPc - rootPc + 12) % 12;
    if (interval == 0) {
        return true; // root is always a chord tone
    }

    // Quality-defined triad intervals
    switch (quality) {
    case ChordQuality::Major:
        if (interval == 4 || interval == 7) { return true; }
        break;
    case ChordQuality::Minor:
        if (interval == 3 || interval == 7) { return true; }
        break;
    case ChordQuality::Diminished:
        if (interval == 3 || interval == 6) { return true; }
        break;
    case ChordQuality::HalfDiminished:
        if (interval == 3 || interval == 6 || interval == 10) { return true; }
        break;
    case ChordQuality::Augmented:
        if (interval == 4 || interval == 8) { return true; }
        break;
    case ChordQuality::Suspended2:
        if (interval == 2 || interval == 7) { return true; }
        break;
    case ChordQuality::Suspended4:
        if (interval == 5 || interval == 7) { return true; }
        break;
    case ChordQuality::Power:
        if (interval == 7) { return true; }
        break;
    default:
        break;
    }

    // 7th/9th/11th/13th extensions explicitly detected in the bitmask.
    // A bass note that matches any detected extension is a chord tone — the chord
    // should be labelled as a slash chord (Cm7/F) rather than a pedal point.
    if (interval == 10 && hasExtension(extensions, Extension::MinorSeventh))      { return true; }
    if (interval == 11 && hasExtension(extensions, Extension::MajorSeventh))      { return true; }
    if (interval == 9  && hasExtension(extensions, Extension::DiminishedSeventh)) { return true; }
    if (interval == 1  && hasExtension(extensions, Extension::FlatNinth))         { return true; }
    if (interval == 2  && hasExtension(extensions, Extension::NaturalNinth))      { return true; }
    if (interval == 3  && hasExtension(extensions, Extension::SharpNinth))        { return true; }
    if (interval == 5  && hasExtension(extensions, Extension::NaturalEleventh))   { return true; }
    if (interval == 6  && hasExtension(extensions, Extension::SharpEleventh))     { return true; }
    if (interval == 8  && hasExtension(extensions, Extension::FlatThirteenth))    { return true; }
    if (interval == 9  && hasExtension(extensions, Extension::NaturalThirteenth)) { return true; }

    // If the chord carries any 7th, the perfect 4th above the root (interval 5,
    // natural 11th) is a valid chord tone even when it sits exactly at the
    // extension-detection threshold (detectExtensions uses strict '>').
    // This correctly handles Cm7/F where F's pcWeight equals kExtensionThreshold
    // and NaturalEleventh is therefore not formally detected, but the chord still
    // qualifies as a slash chord rather than a pedal point.
    // A bare triad (no 7th detected) still triggers pedal detection normally.
    const bool hasAnySeventh = hasExtension(extensions, Extension::MinorSeventh)
                            || hasExtension(extensions, Extension::MajorSeventh)
                            || hasExtension(extensions, Extension::DiminishedSeventh);
    if (interval == 5 && hasAnySeventh) { return true; }

    return false;
}

} // namespace

std::vector<ChordAnalysisResult> RuleBasedChordAnalyzer::analyzeChord(
    const std::vector<ChordAnalysisTone>& tones,
    int keySignatureFifths,
    KeySigMode keyMode,
    const ChordTemporalContext* context,
    const ChordAnalyzerPreferences& prefs) const
{
    if (tones.empty()) {
        return {};
    }

    // Build pitch-class weight histogram and find the bass note.
    std::array<double, 12> pcWeight {};
    int lowestPitch = std::numeric_limits<int>::max();

    double totalRawWeight = 0.0;
    for (const ChordAnalysisTone& t : tones) {
        const int pc = normalizePc(t.pitch);
        pcWeight[static_cast<size_t>(pc)] += std::max(0.1, t.weight);
        totalRawWeight += std::max(0.0, t.weight);
        if (t.pitch < lowestPitch) {
            lowestPitch = t.pitch;
        }
    }

    // Bass: lowest pitch whose weight meets the passing-tone threshold.
    // A tone with weight < (fraction × total) is treated as a chromatic passing
    // tone or ornament and excluded from slash-chord bass candidacy.
    // Falls back to the absolute lowest pitch when no tone meets the threshold
    // (e.g. when all tones have equal weight and the region is evenly distributed).
    const double bassMinWeight = prefs.bassPassingToneMinWeightFraction * totalRawWeight;
    int lowestQualifyingPitch = std::numeric_limits<int>::max();
    for (const ChordAnalysisTone& t : tones) {
        if (t.weight >= bassMinWeight && t.pitch < lowestQualifyingPitch) {
            lowestQualifyingPitch = t.pitch;
        }
    }
    const int lowestPitchForBass = (lowestQualifyingPitch < std::numeric_limits<int>::max())
                                   ? lowestQualifyingPitch : lowestPitch;
    const int bassPc  = normalizePc(lowestPitchForBass);
    int       bassTpc = -1;
    for (const ChordAnalysisTone& t : tones) {
        if (t.pitch == lowestPitchForBass && t.tpc >= 0) {
            bassTpc = t.tpc;
            break;
        }
    }

    // TPC lookup: for each pitch class, store the TPC of the first sounding tone
    // that has TPC data.  -1 means no TPC data for that pitch class.
    std::array<int, 12> tpcForPc;
    tpcForPc.fill(-1);
    for (const ChordAnalysisTone& t : tones) {
        if (t.tpc >= 0) {
            const int pc = normalizePc(t.pitch);
            if (tpcForPc[static_cast<size_t>(pc)] == -1) {
                tpcForPc[static_cast<size_t>(pc)] = t.tpc;
            }
        }
    }

    // Count distinct pitch classes; require at least 3 for meaningful analysis.
    int distinctPcs = 0;
    for (double w : pcWeight) {
        if (w > 0.05) {
            ++distinctPcs;
        }
    }
    if (distinctPcs < 3) {
        return {};
    }

    // Chord templates (quality, intervals-from-root, TPC-deltas-from-root).
    //
    // Template ordering encodes quality tie-breaking priority: when two candidates
    // score identically, the one whose template appears earlier in this array wins
    // (see RawCandidate::tiePriority and the sort below).
    //
    // Key ordering decisions:
    //   Sus4b5 (index 7) precedes HalfDim (index 8): both templates cover the same
    //   4 pitch classes for altered-suspension chords (e.g. {root,P4,b5,m7}); the
    //   Sus4b5 interpretation is preferred because it names the defining P4 interval.
    //
    //   Min7 (index 5) follows Minor triad (index 4) and precedes Sus4 templates:
    //   the explicit 4-note template scores {root,m3,P5,m7} as a unit and outranks
    //   inverted alternatives (e.g. a C6 inversion over E bass) that share the same
    //   pitch classes but have a weaker template-tone match from the correct root.
    //
    //   dom7b5 {root,M3,b5,m7} covers Lydian-dominant chords (C7#11 = C E F# Bb).
    //   TPC delta +6 = augmented 4th (F# from C, clockwise six steps on circle of fifths).
    static const std::array<TemplateDef, 16> templates = {{
        { ChordQuality::Major,          { 0, 4, 7 },        { 0, +4, +1 }       },
        { ChordQuality::Major,          { 0, 4, 7, 11 },    { 0, +4, +1, +5 }   },  // maj7
        { ChordQuality::Major,          { 0, 4, 7, 10 },    { 0, +4, +1, -2 }   },  // dom7
        { ChordQuality::Major,          { 0, 4, 6, 10 },    { 0, +4, -6, -2 }   },  // dom7b5
        { ChordQuality::Minor,          { 0, 3, 7 },        { 0, -3, +1 }       },
        { ChordQuality::Minor,          { 0, 3, 7, 10 },    { 0, -3, +1, -2 }   },  // min7
        { ChordQuality::Diminished,     { 0, 3, 6 },        { 0, -3, -6 }       },
        { ChordQuality::Suspended4,     { 0, 5, 6, 10 },    { 0, -1, -6, -2 }   },  // sus4b5  — precedes HalfDim (tie-break)
        { ChordQuality::HalfDiminished, { 0, 3, 6, 10 },    { 0, -3, -6, -2 }   },
        { ChordQuality::Augmented,      { 0, 4, 8 },        { 0, +4, +8 }       },
        { ChordQuality::Suspended2,     { 0, 2, 7 },        { 0, +2, +1 }       },
        { ChordQuality::Suspended4,     { 0, 5, 7, 10 },    { 0, -1, +1, -2 }   },
        { ChordQuality::Suspended4,     { 0, 5, 7, 11 },    { 0, -1, +1, +5 }   },  // sus4+maj7
        { ChordQuality::Suspended4,     { 0, 5, 8, 10 },    { 0, -1, +8, -2 }   },  // sus4#5
        { ChordQuality::Suspended4,     { 0, 6, 7 },        { 0, +6, +1 }       },  // sus#4 (F# not Gb)
        { ChordQuality::Power,          { 0, 7 },           { 0, +1 }           }
    }};

    // Key context — used for diatonic root bonus and degree assignment.
    // The tonic and scale are derived from the detected mode.
    const int ionianTonicPc = ionianTonicPcFromFifths(keySignatureFifths);
    const int keyTonicPc    = (ionianTonicPc + keyModeTonicOffset(keyMode)) % 12;

    // keyModeIndex() returns the raw enum ordinal (0–20 for all 21 KeySigMode values).
    // Non-diatonic modes are mapped to their diatonic key-signature parent so that
    // diatonic-root bonus and scale-membership scoring stay correct for the parent
    // tonal context.
    static constexpr std::array<size_t, 21> DIATONIC_PARENT_INDEX = {
        0, 1, 2, 3, 4, 5, 6,  // diatonic: identity mapping
        1, 2, 3, 4, 5, 6, 0,  // melodic minor family: Dorian…Ionian parents
        5, 6, 0, 1, 2, 3, 4   // harmonic minor family: Aeolian…Mixolydian parents
    };
    const size_t modeScaleIdx = DIATONIC_PARENT_INDEX[keyModeIndex(keyMode)];
    const std::array<int, 7>& scale = keyModeScaleIntervals(keyModeFromIndex(modeScaleIdx));

    // Score every root × template combination.
    //
    // Each concern is delegated to a named helper (defined in the anonymous namespace
    // above) so that each rule is independently readable and modifiable.
    struct RawCandidate {
        double score;
        double appliedBassBonus;
        int rootPc;
        ChordQuality quality;
        int tiePriority;  // template index in the array above; lower = preferred on equal score
    };

    std::vector<RawCandidate> rawCandidates;
    rawCandidates.reserve(12 * templates.size());

    for (int rootPc = 0; rootPc < 12; ++rootPc) {
        for (size_t tplIdx = 0; tplIdx < templates.size(); ++tplIdx) {
            const TemplateDef& tpl = templates[tplIdx];
            double score = 0.0;
            const double bassBonus = appliedBassRootBonus(tpl, rootPc, bassPc, pcWeight, prefs);

            score += scoreTemplateTones(tpl, rootPc, pcWeight);
            score += scoreExtraNotes(tpl, rootPc, pcWeight, tpcForPc);
            score += dim7CharacteristicBonus(tpl, rootPc, pcWeight, keyTonicPc, scale, prefs.extensionThreshold);
            score += nonBassAdjustment(tpl, rootPc, bassPc, tpcForPc);
            score += structuralPenalties(tpl, rootPc, pcWeight, tpcForPc, distinctPcs, prefs.extensionThreshold);
            score += tpcConsistencyBonus(tpl, rootPc, tpcForPc, prefs);
            score += contextualBonuses(tpl, rootPc, bassPc, bassBonus, distinctPcs, pcWeight,
                                       keyTonicPc, scale,
                                       prefs, context);

            rawCandidates.push_back({ score, bassBonus, rootPc, tpl.quality,
                                      static_cast<int>(tplIdx) });
        }
    }

    // Sort by score descending.  When scores are exactly equal, prefer the template
    // with the lower index (the ordering in the templates array above is intentional
    // — see its comments).  rootPc is the final tiebreaker for full determinism.
    std::sort(rawCandidates.begin(), rawCandidates.end(),
              [](const RawCandidate& a, const RawCandidate& b) -> bool {
                  if (a.score != b.score)             return a.score > b.score;
                  if (a.tiePriority != b.tiePriority) return a.tiePriority < b.tiePriority;
                  return a.rootPc < b.rootPc;
              });

    const double bestRawScore = rawCandidates.empty() ? 0.0 : rawCandidates.front().score;
    const double threshold = bestRawScore * kScoreThresholdRatio;

    std::vector<ChordAnalysisResult> results;
    results.reserve(3);

    for (const RawCandidate& rc : rawCandidates) {
        if (results.size() >= 3) {
            break;
        }
        if (rc.score < threshold) {
            break;
        }

        int rootPc    = rc.rootPc;
        ChordQuality quality = rc.quality;

        // ── Post-scoring quality normalisation ──────────────────────────────────
        //
        // The following steps refine the reported quality AFTER ranking is complete.
        // They do NOT affect rc.score (which reflects the raw template match); they
        // ensure ChordAnalysisResult::quality carries the most accurate musical label.
        //
        // There are three cases:
        //   1. Augmented root correction  — symmetric triad; bass selects the root
        //                                   when TPC data is absent.
        //   2. Sus2 → Sus4 upgrade        — when P4 is sounding, Sus4 is more specific.
        //   3. Sus → Major (omitsThird)   — when Maj7 is present but no 3rd, the catalog
        //                                   labels the chord as Major quality.
        //
        // Note: rc.score is the winning template's raw score and may not exactly match
        // the normalised quality reported below.  Callers that need to compare scores
        // across results should be aware of this.

        // 1. Augmented root correction.
        // Augmented triads are symmetric, so pure pitch-class scoring cannot distinguish
        // roots.  TPC spelling resolves this directly when available (the scoring loop
        // already applied the bonus); the heuristic fallback uses the bass note when
        // no TPC data was supplied.
        if (quality == ChordQuality::Augmented && tpcForPc[static_cast<size_t>(rootPc)] < 0) {
            std::vector<int> pcs;
            for (int pc = 0; pc < 12; ++pc) {
                if (pcWeight[static_cast<size_t>(pc)] > 0.05) {
                    pcs.push_back(pc);
                }
            }
            if (pcs.size() == 3) {
                bool isAug = false;
                for (int i = 0; i < 3 && !isAug; ++i) {
                    const int a = pcs[i], b = pcs[(i + 1) % 3], c = pcs[(i + 2) % 3];
                    if ((b - a + 12) % 12 == 4 && (c - b + 12) % 12 == 4 && (a - c + 12) % 12 == 4) {
                        isAug = true;
                    }
                }
                if (isAug) {
                    rootPc = normalizePc(lowestPitch);
                }
            }
        }

        const int rootTpc = tpcForPc[static_cast<size_t>(rootPc)];
        ExtensionFlags ext = detectExtensions(pcWeight, rootPc, quality, tpcForPc, rootTpc, prefs.extensionThreshold);

        // 2. Sus2 → Sus4 upgrade: Sus4 is more specific when P4 is actually sounding.
        if (quality == ChordQuality::Suspended2 && ext.hasEleventh) {
            quality = ChordQuality::Suspended4;
            ext = detectExtensions(pcWeight, rootPc, quality, tpcForPc, rootTpc, prefs.extensionThreshold);
        }

        // 3. Sus → Major (omitsThird): when Maj7 is present but no 3rd is sounding,
        // the catalog labels the chord as Major quality.  This covers both the
        // "no-fourth" case (true suspended with Maj7) and the "with-fourth" case
        // (CMaj7sus4 / CMaj9sus4).  A present P4 is retained as an extension.
        const bool hasMajThird  = pcWeight[static_cast<size_t>((rootPc + 4) % 12)] > 0.2;
        const bool hasMinThird  = pcWeight[static_cast<size_t>((rootPc + 3) % 12)] > 0.2;
        const bool hasAnyThird  = hasMajThird || hasMinThird;

        bool omitsThird = false;
        if (ext.hasMajorSeventh && !hasAnyThird
            && (quality == ChordQuality::Suspended2 || quality == ChordQuality::Suspended4)) {
            quality    = ChordQuality::Major;
            omitsThird = true;
            ext = detectExtensions(pcWeight, rootPc, quality, tpcForPc, rootTpc, prefs.extensionThreshold);
        }

        // Degree assignment.
        int degree = -1;
        for (size_t i = 0; i < scale.size(); ++i) {
            if ((keyTonicPc + scale[i]) % 12 == rootPc) {
                degree = static_cast<int>(i);
                break;
            }
        }

        // Diatonic check: every sounding pc must be in the scale.
        bool diatonic = (degree >= 0);
        if (diatonic) {
            for (int pc = 0; pc < 12; ++pc) {
                if (pcWeight[static_cast<size_t>(pc)] <= 0.2) {
                    continue;
                }
                bool inScale = false;
                for (int interval : scale) {
                    if ((keyTonicPc + interval) % 12 == pc) {
                        inScale = true;
                        break;
                    }
                }
                if (!inScale) {
                    diatonic = false;
                    break;
                }
            }
        }

        ChordAnalysisResult r;
        r.identity.score                = rc.score;
        r.identity.rootPc               = rootPc;
        r.identity.rootTpc              = rootTpc;
        r.identity.bassPc               = bassPc;
        r.identity.bassTpc              = bassTpc;
        r.identity.naturalFifthPresent  = (quality != ChordQuality::Augmented)
                                          && (pcWeight[static_cast<size_t>((rootPc + 7) % 12)]
                                              > prefs.extensionThreshold);
        r.identity.quality              = quality;
        if (ext.hasMinorSeventh)      setExtension(r.identity.extensions, Extension::MinorSeventh);
        if (ext.hasMajorSeventh)      setExtension(r.identity.extensions, Extension::MajorSeventh);
        if (ext.hasDiminishedSeventh) setExtension(r.identity.extensions, Extension::DiminishedSeventh);
        if (ext.hasAddedSixth)        setExtension(r.identity.extensions, Extension::AddedSixth);
        if (ext.hasNinthNatural)      setExtension(r.identity.extensions, Extension::NaturalNinth);
        if (ext.hasNinthFlat)         setExtension(r.identity.extensions, Extension::FlatNinth);
        if (ext.hasNinthSharp)        setExtension(r.identity.extensions, Extension::SharpNinth);
        if (ext.hasEleventh)          setExtension(r.identity.extensions, Extension::NaturalEleventh);
        if (ext.hasEleventhSharp)     setExtension(r.identity.extensions, Extension::SharpEleventh);
        if (ext.hasThirteenth)        setExtension(r.identity.extensions, Extension::NaturalThirteenth);
        if (ext.hasThirteenthFlat)    setExtension(r.identity.extensions, Extension::FlatThirteenth);
        if (ext.hasThirteenthSharp)   setExtension(r.identity.extensions, Extension::SharpThirteenth);
        if (ext.hasSharpFifth)        setExtension(r.identity.extensions, Extension::SharpFifth);
        if (ext.hasFlatFifth)         setExtension(r.identity.extensions, Extension::FlatFifth);
        if (ext.isSixNine)            setExtension(r.identity.extensions, Extension::SixNine);
        if (omitsThird)               setExtension(r.identity.extensions, Extension::OmitsThird);
        r.function.degree               = degree;
        r.function.diatonicToKey        = diatonic;
        r.function.keyTonicPc           = keyTonicPc;
        r.function.keyMode              = keyMode;

        results.push_back(r);
    }

    // ── Inversion / bass-root bias correction ────────────────────────────────
    //
    // If the winner's bass-root bonus is the sole reason it beat the best
    // non-bass alternative (margin < inversionSuspicionMargin), and a clean
    // triadic/seventh alternative exists, and the chord has ≥ 3 distinct PCs
    // (not an arpeggio artifact), remove the bonus contribution and re-sort.
    //
    // This corrects the systematic bias where inverted chords are labelled with
    // the bass note as root instead of the actual chord root.
    if (prefs.inversionSuspicionMargin > 0.0
        && prefs.inversionBonusReduction < 1.0
        && results.size() >= 2
        && distinctPcs >= 3)
    {
        const ChordAnalysisResult& winner = results[0];
        const bool winnerBassIsRoot = (winner.identity.rootPc == winner.identity.bassPc);

        // The correction only targets Major and Minor winners — the typical inversion
        // bias patterns (e.g. Bb6 labelled as root-position when it's really Gm/Bb).
        // Augmented, Diminished, HalfDiminished, Suspended, and Power chords with
        // bassIsRoot=true are far more often correct root-position identifications,
        // and the correction causes regressions when applied to them.
        const bool winnerQualityTargeted = (winner.identity.quality == ChordQuality::Major
                            || winner.identity.quality == ChordQuality::Minor);

        if (winnerBassIsRoot && winnerQualityTargeted) {
            // Find the best alternative that has clean (Major or Minor) quality.
            // Seconds-chord, augmented, diminished, etc. are excluded as described above.
            static constexpr std::array<ChordQuality, 2> kCleanQualities = {
                ChordQuality::Major,
                ChordQuality::Minor,
            };
            const ChordAnalysisResult* bestAlt = nullptr;
            for (size_t i = 1; i < results.size(); ++i) {
                const auto& alt = results[i];
                // The alternative must have a DIFFERENT root — if it agrees on the
                // root but differs only in extensions (e.g. CMaj9 vs CMaj9(no 3)),
                // there is no inversion to correct.
                if (alt.identity.rootPc == winner.identity.rootPc) {
                    continue;
                }
                const bool isClean = std::find(kCleanQualities.begin(),
                                               kCleanQualities.end(),
                                               alt.identity.quality)
                                     != kCleanQualities.end();
                if (isClean) {
                    bestAlt = &alt;
                    break;
                }
            }

            if (bestAlt != nullptr) {
                const double margin = winner.identity.score - bestAlt->identity.score;

                // Seventh-chord exemption: if the winner carries a minor or major
                // seventh extension that the best alternative lacks, the bass-root
                // bonus is not the sole structural advantage — the winner is a richer,
                // more specific reading (e.g. Am7 vs Em triad).  Do not penalise it.
                const bool winnerHasSeventh =
                    hasExtension(winner.identity.extensions, Extension::MinorSeventh)
                    || hasExtension(winner.identity.extensions, Extension::MajorSeventh);
                const bool altHasSeventh =
                    hasExtension(bestAlt->identity.extensions, Extension::MinorSeventh)
                    || hasExtension(bestAlt->identity.extensions, Extension::MajorSeventh);
                const bool seventhExempt = winnerHasSeventh && !altHasSeventh;

                if (!seventhExempt && margin < prefs.inversionSuspicionMargin) {
                    // Deduct the bass-bonus contribution from the winner and re-sort.
                    const double deduction = prefs.bassNoteRootBonus
                                            * (1.0 - prefs.inversionBonusReduction);
                    results[0].identity.score -= deduction;
                    std::stable_sort(results.begin(), results.end(),
                                     [](const ChordAnalysisResult& a,
                                        const ChordAnalysisResult& b) {
                                         return a.identity.score > b.identity.score;
                                     });
                }
            }
        }
    }

    // ── Populate normalizedConfidence for each result ─────────────────────────
    if (!results.empty()) {
        const double winnerScore = results.front().identity.score;
        const double runnerUpScore = (results.size() >= 2) ? results[1].identity.score : 0.0;
        results[0].identity.normalizedConfidence
            = normalizeChordConfidence(winnerScore, runnerUpScore, prefs);
        for (size_t i = 1; i < results.size(); ++i) {
            const double iRunnerUp = (i + 1 < results.size()) ? results[i + 1].identity.score : 0.0;
            results[i].identity.normalizedConfidence
                = normalizeChordConfidence(results[i].identity.score, iRunnerUp, prefs);
        }
    }

    // ── Two-pass pedal point detection ────────────────────────────────────────
    //
    // Definition: a structural pedal point is a sustained bass note that is NOT
    // a chord tone of the upper-voice harmony.  This two-pass check identifies
    // it when:
    //   (1) Pass 1 (all voices) produces a confident winner R1 with bassPc X.
    //   (2) X is not a chord tone of R1 (triad + detected 7th extensions).
    //   (3) Pass 2 (upper voices only, X removed) produces a chord R2 with
    //       confidence ≥ pedalConfidenceThreshold and ≥ 2 distinct pitch classes.
    //
    // When confirmed, the Pass 2 chord replaces the Pass 1 result: the label
    // describes the upper-voice harmony and isPedalPoint / pedalBassPc are set.
    //
    // Safety checks:
    //   - Bass IS a chord tone of R1 → no check (common-tone progressions, slash
    //     chords, jazz ostinati like F13/Eb where Eb is the minor 7th).
    //   - Upper voices have < 2 distinct pitch classes → insufficient evidence.
    //   - Pass 2 confidence < pedalConfidenceThreshold → ambiguous; keep R1.
    //   - bassPc < 0 → no valid bass (sparse region); skip.
    if (!results.empty() && bassPc >= 0 && prefs.pedalConfidenceThreshold > 0.0) {
        const ChordAnalysisResult& r1 = results.front();
        const bool bassIsChordTone = isBassChordTone(bassPc,
                                                     r1.identity.rootPc,
                                                     r1.identity.quality,
                                                     r1.identity.extensions);
        if (!bassIsChordTone) {
            // Remove all tones with the pedal pitch class and re-analyze.
            std::vector<ChordAnalysisTone> upperTones;
            upperTones.reserve(tones.size());
            for (const ChordAnalysisTone& t : tones) {
                if ((t.pitch % 12 + 12) % 12 != bassPc) {
                    upperTones.push_back(t);
                }
            }

            // Require at least 2 distinct pitch classes in the upper voices.
            std::set<int> upperPcs;
            for (const ChordAnalysisTone& t : upperTones) {
                upperPcs.insert((t.pitch % 12 + 12) % 12);
            }

            if (upperPcs.size() >= 2) {
                // Run Pass 2 — re-use the same key context and preferences.
                // Do not pass temporal context to Pass 2: the context bonuses
                // (rootContinuityBonus, stepwiseBass*) are anchored to the bass
                // note and would distort the upper-voice-only result.
                const auto pass2 = RuleBasedChordAnalyzer{}.analyzeChord(
                    upperTones, keySignatureFifths, keyMode, nullptr, prefs);

                if (!pass2.empty()) {
                    // Confidence is measured against the first competitor with a
                    // DIFFERENT root.  Multiple templates for the same chord quality
                    // (triad / maj7 / dom7) can score identically when their extended
                    // tones are absent, filling all three result slots with the same
                    // root — making normalizedConfidence artificially low.
                    // Comparing the winner's score against the best genuine alternative
                    // (different rootPc) gives a meaningful pedal-confirmation signal.
                    double pass2AltScore = 0.0;
                    const int p2Root = pass2.front().identity.rootPc;
                    for (size_t i = 1; i < pass2.size(); ++i) {
                        if (pass2[i].identity.rootPc != p2Root) {
                            pass2AltScore = pass2[i].identity.score;
                            break;
                        }
                    }
                    const double gap = pass2.front().identity.score - pass2AltScore;
                    const double c2  = 1.0 / (1.0 + std::exp(
                        -prefs.confidenceSigmoidSteepness
                        * (gap - prefs.confidenceSigmoidMidpoint)));
                    if (c2 >= prefs.pedalConfidenceThreshold) {
                        // Confirmed pedal — replace results with Pass 2.
                        results = pass2;
                        results.front().identity.isPedalPoint = true;
                        results.front().identity.pedalBassPc  = bassPc;
                    }
                }
            }
        }
    }

    return results;
}

ChordAnalysisDiagnosticResult RuleBasedChordAnalyzer::diagnoseChord(
    const std::vector<ChordAnalysisTone>& tones,
    int keySignatureFifths,
    KeySigMode keyMode,
    const ChordTemporalContext* context,
    const ChordAnalyzerPreferences& prefs) const
{
    ChordAnalysisDiagnosticResult diag;
    if (tones.empty()) { return diag; }

    // ── Build pcWeight histogram and find bass (mirrors analyzeChord) ────────
    std::array<double, 12> pcWeight{};
    int lowestPitch = std::numeric_limits<int>::max();
    double totalRawWeight = 0.0;
    for (const ChordAnalysisTone& t : tones) {
        const int pc = normalizePc(t.pitch);
        pcWeight[static_cast<size_t>(pc)] += std::max(0.1, t.weight);
        totalRawWeight += std::max(0.0, t.weight);
        if (t.pitch < lowestPitch) { lowestPitch = t.pitch; }
    }
    diag.pcWeights = pcWeight;

    const double bassMinWeight = prefs.bassPassingToneMinWeightFraction * totalRawWeight;
    int lowestQualifyingPitch = std::numeric_limits<int>::max();
    for (const ChordAnalysisTone& t : tones) {
        if (t.weight >= bassMinWeight && t.pitch < lowestQualifyingPitch) {
            lowestQualifyingPitch = t.pitch;
        }
    }
    const int lowestPitchForBass = (lowestQualifyingPitch < std::numeric_limits<int>::max())
                                   ? lowestQualifyingPitch : lowestPitch;
    const int bassPc = normalizePc(lowestPitchForBass);
    diag.bassPc = bassPc;

    std::array<int, 12> tpcForPc;
    tpcForPc.fill(-1);
    for (const ChordAnalysisTone& t : tones) {
        if (t.tpc >= 0) {
            const int pc = normalizePc(t.pitch);
            if (tpcForPc[static_cast<size_t>(pc)] == -1) {
                tpcForPc[static_cast<size_t>(pc)] = t.tpc;
            }
        }
    }

    int distinctPcs = 0;
    for (double w : pcWeight) { if (w > 0.05) { ++distinctPcs; } }
    diag.distinctPcs = distinctPcs;
    if (distinctPcs < 3) { return diag; }

    // ── Templates (same ordering as analyzeChord) ────────────────────────────
    static const std::array<TemplateDef, 16> kDiagTemplates = {{
        { ChordQuality::Major,          { 0, 4, 7 },        { 0, +4, +1 }       },
        { ChordQuality::Major,          { 0, 4, 7, 11 },    { 0, +4, +1, +5 }   },
        { ChordQuality::Major,          { 0, 4, 7, 10 },    { 0, +4, +1, -2 }   },
        { ChordQuality::Major,          { 0, 4, 6, 10 },    { 0, +4, -6, -2 }   },
        { ChordQuality::Minor,          { 0, 3, 7 },        { 0, -3, +1 }       },
        { ChordQuality::Minor,          { 0, 3, 7, 10 },    { 0, -3, +1, -2 }   },
        { ChordQuality::Diminished,     { 0, 3, 6 },        { 0, -3, -6 }       },
        { ChordQuality::Suspended4,     { 0, 5, 6, 10 },    { 0, -1, -6, -2 }   },
        { ChordQuality::HalfDiminished, { 0, 3, 6, 10 },    { 0, -3, -6, -2 }   },
        { ChordQuality::Augmented,      { 0, 4, 8 },        { 0, +4, +8 }       },
        { ChordQuality::Suspended2,     { 0, 2, 7 },        { 0, +2, +1 }       },
        { ChordQuality::Suspended4,     { 0, 5, 7, 10 },    { 0, -1, +1, -2 }   },
        { ChordQuality::Suspended4,     { 0, 5, 7, 11 },    { 0, -1, +1, +5 }   },
        { ChordQuality::Suspended4,     { 0, 5, 8, 10 },    { 0, -1, +8, -2 }   },
        { ChordQuality::Suspended4,     { 0, 6, 7 },        { 0, +6, +1 }       },
        { ChordQuality::Power,          { 0, 7 },           { 0, +1 }           }
    }};

    // ── Key context ──────────────────────────────────────────────────────────
    const int ionianTonicPc = ionianTonicPcFromFifths(keySignatureFifths);
    const int keyTonicPc    = (ionianTonicPc + keyModeTonicOffset(keyMode)) % 12;

    static constexpr std::array<size_t, 21> DIATONIC_PARENT_INDEX = {
        0, 1, 2, 3, 4, 5, 6,
        1, 2, 3, 4, 5, 6, 0,
        5, 6, 0, 1, 2, 3, 4
    };
    const size_t modeScaleIdx = DIATONIC_PARENT_INDEX[keyModeIndex(keyMode)];
    const std::array<int, 7>& scale = keyModeScaleIntervals(keyModeFromIndex(modeScaleIdx));

    // ── Score every root × template combination ──────────────────────────────
    diag.candidates.reserve(12 * kDiagTemplates.size());

    for (int rootPc = 0; rootPc < 12; ++rootPc) {
        for (size_t tplIdx = 0; tplIdx < kDiagTemplates.size(); ++tplIdx) {
            const TemplateDef& tpl = kDiagTemplates[tplIdx];

            const double tplScore   = scoreTemplateTones(tpl, rootPc, pcWeight);
            const double extraScore = scoreExtraNotes(tpl, rootPc, pcWeight, tpcForPc);
            const double bbonus     = appliedBassRootBonus(tpl, rootPc, bassPc, pcWeight, prefs);
            const double nonBassAdj = nonBassAdjustment(tpl, rootPc, bassPc, tpcForPc);
            const double structural = structuralPenalties(tpl, rootPc, pcWeight, tpcForPc, distinctPcs, prefs.extensionThreshold);
            const double tpcBonus   = tpcConsistencyBonus(tpl, rootPc, tpcForPc, prefs);
            const double dim7       = dim7CharacteristicBonus(tpl, rootPc, pcWeight, keyTonicPc, scale, prefs.extensionThreshold);

            double diatonicBonus = 0.0;
            for (int interval : scale) {
                if ((keyTonicPc + interval) % 12 == rootPc) {
                    diatonicBonus = prefs.diatonicRootBonus;
                    break;
                }
            }

            // contextualBonuses() includes bassBonus + diatonicBonus; subtract them
            // to isolate the remaining contextual contributions.
            const double totalContext = contextualBonuses(
                tpl, rootPc, bassPc, bbonus, distinctPcs, pcWeight,
                keyTonicPc, scale, prefs, context);
            const double contextBonus = totalContext - bbonus - diatonicBonus;

            ChordCandidateDiagnostic entry;
            entry.rootPc             = rootPc;
            entry.templateIdx        = static_cast<int>(tplIdx);
            entry.quality            = tpl.quality;
            entry.templateTonesScore = tplScore;
            entry.extraNotesScore    = extraScore;
            entry.dim7Bonus          = dim7;
            entry.nonBassAdjust      = nonBassAdj;
            entry.structuralPenalty  = structural;
            entry.tpcBonus           = tpcBonus;
            entry.bassBonus          = bbonus;
            entry.diatonicBonus      = diatonicBonus;
            entry.contextBonus       = contextBonus;
            entry.totalScore         = tplScore + extraScore + dim7 + nonBassAdj
                                       + structural + tpcBonus + bbonus + diatonicBonus + contextBonus;
            diag.candidates.push_back(entry);
        }
    }

    std::sort(diag.candidates.begin(), diag.candidates.end(),
              [](const ChordCandidateDiagnostic& a, const ChordCandidateDiagnostic& b) {
                  return a.totalScore > b.totalScore;
              });

    return diag;
}

/// Returns true if bass is a valid plain note name: 1–3 chars,
/// uppercase letter followed only by ASCII accidentals ('#' or 'b').
/// Guards against chord symbol strings accidentally appearing in the
/// bass field of slash chords (e.g. "C7b9/Bb" instead of "Bb").
static bool isValidBassNoteName(const char* bass)
{
    if (!bass || bass[0] == '\0') return false;
    if (!std::isupper(static_cast<unsigned char>(bass[0]))) return false;
    size_t len = 1;
    for (; bass[len] != '\0'; ++len) {
        if (bass[len] != '#' && bass[len] != 'b') return false;
        if (len >= 3) return false;   // max 3 chars
    }
    return true;
}

std::string ChordSymbolFormatter::formatSymbol(const ChordAnalysisResult& result,
                                               int keySignatureFifths,
                                               const Options& opts)
{
    // Sus4+Maj7 chords are requalified to Major+omitsThird internally.
    // Render them as "Maj7sus"/"Maj9sus" — the notation used for this chord type in the catalog.
    if (hasExtension(result.identity.extensions, Extension::OmitsThird) && hasExtension(result.identity.extensions, Extension::MajorSeventh)
            && hasExtension(result.identity.extensions, Extension::NaturalEleventh) && !hasExtension(result.identity.extensions, Extension::SharpEleventh)) {
        std::string symbol = std::string(pitchClassNameFromTpc(result.identity.rootPc, result.identity.rootTpc, keySignatureFifths, opts.spelling));
        symbol += hasExtension(result.identity.extensions, Extension::NaturalNinth) ? "Maj9sus" : "Maj7sus";
        if (result.identity.bassPc != result.identity.rootPc
                && result.identity.bassPc >= 0 && result.identity.bassPc < 12) {
            const char* bassName = pitchClassNameFromTpc(result.identity.bassPc, result.identity.bassTpc, keySignatureFifths, opts.spelling);
            if (isValidBassNoteName(bassName)) {
                symbol += "/";
                symbol += bassName;
            }
        }
        return symbol;
    }

    std::string symbol = std::string(pitchClassNameFromTpc(result.identity.rootPc, result.identity.rootTpc, keySignatureFifths, opts.spelling))
                        + qualitySuffix(result.identity.quality,
                                        hasExtension(result.identity.extensions, Extension::MinorSeventh),
                                        hasExtension(result.identity.extensions, Extension::MajorSeventh),
                                        hasExtension(result.identity.extensions, Extension::DiminishedSeventh),
                                        hasExtension(result.identity.extensions, Extension::AddedSixth),
                                        hasExtension(result.identity.extensions, Extension::NaturalNinth)
                                            || hasExtension(result.identity.extensions, Extension::FlatNinth)
                                            || hasExtension(result.identity.extensions, Extension::SharpNinth),
                                        hasExtension(result.identity.extensions, Extension::NaturalNinth),
                                        hasExtension(result.identity.extensions, Extension::NaturalEleventh),
                                        hasExtension(result.identity.extensions, Extension::NaturalThirteenth),
                                        hasExtension(result.identity.extensions, Extension::FlatNinth),
                                        hasExtension(result.identity.extensions, Extension::SharpNinth),
                                        hasExtension(result.identity.extensions, Extension::SharpEleventh),
                                        hasExtension(result.identity.extensions, Extension::FlatThirteenth),
                                        hasExtension(result.identity.extensions, Extension::SharpThirteenth),
                                        hasExtension(result.identity.extensions, Extension::SharpFifth),
                                        hasExtension(result.identity.extensions, Extension::FlatFifth),
                                        hasExtension(result.identity.extensions, Extension::SixNine));

    if (hasExtension(result.identity.extensions, Extension::OmitsThird)) {
        symbol += "(no 3)";
    }

    if (result.identity.bassPc != result.identity.rootPc
            && result.identity.bassPc >= 0 && result.identity.bassPc < 12) {
        const char* bassName = pitchClassNameFromTpc(result.identity.bassPc, result.identity.bassTpc, keySignatureFifths, opts.spelling);
        if (isValidBassNoteName(bassName)) {
            symbol += "/";
            symbol += bassName;
        }
    }

    return symbol;
}

// ── Tonicization helpers ──────────────────────────────────────────────────────

/// Diatonic scale intervals for the seven diatonic modes (semitones from tonic).
static constexpr std::array<int, 7> kTonicizationScales[7] = {
    { 0, 2, 4, 5, 7, 9, 11 }, // Ionian
    { 0, 2, 3, 5, 7, 9, 10 }, // Dorian
    { 0, 1, 3, 5, 7, 8, 10 }, // Phrygian
    { 0, 2, 4, 6, 7, 9, 11 }, // Lydian
    { 0, 2, 4, 5, 7, 9, 10 }, // Mixolydian
    { 0, 2, 3, 5, 7, 8, 10 }, // Aeolian
    { 0, 1, 3, 5, 6, 8, 10 }, // Locrian
};

/// Maps all 21 KeySigMode ordinals to their diatonic parent index (0..6).
static constexpr std::array<size_t, 21> kTonicizationParent = {
    0, 1, 2, 3, 4, 5, 6,   // diatonic: identity
    1, 2, 3, 4, 5, 6, 0,   // melodic minor family
    5, 6, 0, 1, 2, 3, 4    // harmonic minor family
};

/// Return the diatonic scale degree (0..6) for pitch class `pc` relative to
/// `tonicPc` in `scale`, or -1 if `pc` is not a scale member.
static int diatonicDegreeForPc(int pc, int tonicPc, const std::array<int, 7>& scale)
{
    const int interval = (pc - tonicPc + 12) % 12;
    for (int d = 0; d < 7; ++d) {
        if (scale[d] == interval) {
            return d;
        }
    }
    return -1;
}

/// Returns true if the natural triad built on scale degree `d` has a major
/// third (4 semitones), meaning the Roman numeral target label is upper-case.
static bool isDegreeMajorThird(int d, const std::array<int, 7>& scale)
{
    const int rootInterval  = scale[d];
    const int thirdInterval = scale[(d + 2) % 7];
    return (thirdInterval - rootInterval + 12) % 12 == 4;
}

std::string ChordSymbolFormatter::formatRomanNumeral(const ChordAnalysisResult& result)
{
    std::string romanNumeral;

    if (result.function.degree < 0) {
        // Non-diatonic root: generate a chromatic numeral (e.g. bVII, bIII, bVI).
        using Q = ChordQuality;
        const bool isMinorQuality = (result.identity.quality == Q::Minor
                                     || result.identity.quality == Q::Diminished
                                     || result.identity.quality == Q::HalfDiminished);
        const int semitone = (result.identity.rootPc - result.function.keyTonicPc + 12) % 12;
        // chromaticRoman() only knows the 7 diatonic modes (SCALES[0..6]).
        // Map non-diatonic modes to their diatonic parent before calling it.
        static constexpr std::array<int, 21> CHR_DIATONIC_PARENT = {
            0, 1, 2, 3, 4, 5, 6,  // diatonic: identity
            1, 2, 3, 4, 5, 6, 0,  // melodic minor family
            5, 6, 0, 1, 2, 3, 4   // harmonic minor family
        };
        const int modeIdx = CHR_DIATONIC_PARENT[static_cast<size_t>(keyModeIndex(result.function.keyMode))];
        const std::string chrBase = chromaticRoman(semitone, modeIdx, isMinorQuality);
        if (chrBase.empty()) {
            return "";  // Should not occur in standard 12-tone music
        }
        // Reuse diatonicRoman with degree = 0 to get the quality/extension suffix
        // (e.g. "o", "+", "ø7", "M7", "(add6)").  degree = 0 always yields a
        // single-character base "I"/"i" that we strip, leaving only the suffix.
        ChordAnalysisResult tmp = result;
        tmp.function.degree = 0;
        const std::string diatonized = diatonicRoman(tmp);
        const std::string suffix = diatonized.size() > 1 ? diatonized.substr(1) : "";
        romanNumeral = chrBase + suffix;
    } else {
        romanNumeral = diatonicRoman(result);
    }

    romanNumeral = romanWithInversion(romanNumeral, result.identity.quality,
                                      result.identity.rootPc, result.identity.bassPc,
                                      hasExtension(result.identity.extensions, Extension::MinorSeventh), hasExtension(result.identity.extensions, Extension::MajorSeventh),
                                      hasExtension(result.identity.extensions, Extension::DiminishedSeventh));

    // ── Augmented sixth label (It+6, Fr+6, Ger+6) — replaces chromatic Roman numeral ─
    //
    // Condition: root is ♭6̂ of the current key AND the note at interval 10 above root
    // is spelled as an augmented sixth (TPC delta +10 from root), which the analysis
    // phase encodes as SharpThirteenth (not MinorSeventh).  When TPC data is absent,
    // SharpThirteenth is not set and detection is suppressed — this correctly avoids
    // false positives on enharmonically identical dominant seventh chords (e.g. Ab7).
    //
    // Type determination (after confirming aug6 family):
    //   French (+6): SharpEleventh set — note at interval 6 above root (D above Ab in C)
    //                is spelled in the sharp direction (TPC delta +6 from root).
    //   German (+6): naturalFifthPresent — the perfect fifth above root (Eb in C) is present.
    //   Italian (+6): neither French nor German.
    //
    // The aug6 label REPLACES the diatonic/chromatic Roman numeral entirely.
    // Preset gating (Standard/Baroque only): deferred — formatRomanNumeral() has no
    // preset context; gating may be added when preset is threaded through the formatter.
    {
        using Q = ChordQuality;
        const int rootPc     = result.identity.rootPc;
        const int keyTonicPc = result.function.keyTonicPc;
        if (result.identity.quality == Q::Major
            && rootPc == (keyTonicPc + 8) % 12
            && hasExtension(result.identity.extensions, Extension::SharpThirteenth)) {
            if (hasExtension(result.identity.extensions, Extension::SharpEleventh)) {
                romanNumeral = "Fr+6";
            } else if (result.identity.naturalFifthPresent) {
                romanNumeral = "Ger+6";
            } else {
                romanNumeral = "It+6";
            }
        }
    }

    // ── Tonicization label (V7/x, vii°/x) — replaces normal Roman numeral ───
    //
    // Only fires when nextRootPc was populated by a two-pass sequential analysis
    // (chord staff population). Status-bar single-note analysis leaves
    // nextRootPc = -1 and shows the plain diatonic/chromatic label.
    //
    // When tonicization is detected the ENTIRE label is replaced, not appended.
    // "V7/ii" is standard notation; "VI7/ii" (degree-in-home-key + /target) is not.
    if (result.function.nextRootPc >= 0 && !romanNumeral.empty()) {
        using Q = ChordQuality;
        const Q quality  = result.identity.quality;
        const int rootPc = result.identity.rootPc;
        const int nextPc = result.function.nextRootPc;

        // V/x: dominant seventh quality (major triad + minor seventh).
        // rootPc must be a perfect fifth above nextPc.
        const bool isDom7 = (quality == Q::Major)
                            && hasExtension(result.identity.extensions, Extension::MinorSeventh);
        // vii°/x: diminished or half-diminished.
        // nextPc must be a semitone above rootPc.
        const bool isDim = (quality == Q::Diminished || quality == Q::HalfDiminished);

        const int upAFifth    = (rootPc - nextPc + 12) % 12; // 7 = rootPc is P5 above nextPc
        const int upASemitone = (nextPc - rootPc + 12) % 12; // 1 = nextPc is semitone above rootPc

        const bool isCandidateV    = isDom7 && (upAFifth == 7);
        const bool isCandidateViio = isDim  && (upASemitone == 1);

        if (isCandidateV || isCandidateViio) {
            const size_t modeScaleIdx = kTonicizationParent[keyModeIndex(result.function.keyMode)];
            const std::array<int, 7>& scale = kTonicizationScales[modeScaleIdx];

            const int nextDegree = diatonicDegreeForPc(nextPc, result.function.keyTonicPc, scale);

            // nextDegree > 0: exclude the tonic so plain V→I stays labeled "V7", not "V7/I".
            if (nextDegree > 0) {
                static constexpr const char* UPPER[7] = { "I","II","III","IV","V","VI","VII" };
                static constexpr const char* LOWER[7] = { "i","ii","iii","iv","v","vi","vii" };

                std::string tonicLabel;
                if (isCandidateV) {
                    // Dominant seventh: always "V7" (dom7 quality guaranteed by detection)
                    tonicLabel = "V7";
                } else {
                    // Diminished leading-tone chord
                    const bool isHalfDim = (quality == Q::HalfDiminished);
                    tonicLabel = "vii";
                    tonicLabel += isHalfDim ? "\xc3\xb8" : "o"; // ø or °
                    if (isHalfDim
                            || hasExtension(result.identity.extensions, Extension::DiminishedSeventh)
                            || hasExtension(result.identity.extensions, Extension::MinorSeventh)) {
                        tonicLabel += "7";
                    }
                }

                const bool upper = isDegreeMajorThird(nextDegree, scale);
                tonicLabel += "/";
                tonicLabel += (upper ? UPPER[nextDegree] : LOWER[nextDegree]);
                romanNumeral = tonicLabel; // replace the diatonic/chromatic label
            }
        }
    }

    return romanNumeral;
}

// ───────────── Nashville Number Formatter and Helpers ─────────────
namespace ChordSymbolFormatter {

namespace {
    std::string nashvilleDegree(int degree) {
        static const char* numbers[] = { "1", "2", "3", "4", "5", "6", "7" };
        if (degree >= 0 && degree < 7)
            return numbers[degree];
        return "?";
    }

    std::string nashvilleQualitySuffix(const ChordAnalysisResult& result) {
        using Q = ChordQuality;
        switch (result.identity.quality) {
            case Q::Major:        return "";
            case Q::Minor:        return "m";
            case Q::Diminished:   return "°";
            case Q::Augmented:    return "+";
            case Q::HalfDiminished: return "ø";
            case Q::Suspended2:   return "sus2";
            case Q::Suspended4:   return "sus4";
            case Q::Power:        return "5";
            default:              return "";
        }
    }

    std::string nashvilleExtensionSuffix(const ChordAnalysisResult& result) {
        std::string ext;
        if (hasExtension(result.identity.extensions, Extension::MajorSeventh))      ext += "maj7";
        else if (hasExtension(result.identity.extensions, Extension::MinorSeventh)) ext += "7";
        else if (hasExtension(result.identity.extensions, Extension::DiminishedSeventh)) ext += "°7";
        if (hasExtension(result.identity.extensions, Extension::AddedSixth))        ext += "6";
        if (hasExtension(result.identity.extensions, Extension::NaturalNinth))             ext += "9";
        if (hasExtension(result.identity.extensions, Extension::NaturalEleventh))          ext += "11";
        if (hasExtension(result.identity.extensions, Extension::NaturalThirteenth))        ext += "13";
        if (hasExtension(result.identity.extensions, Extension::FlatFifth))         ext += "♭5";
        if (hasExtension(result.identity.extensions, Extension::SharpFifth))        ext += "♯5";
        if (hasExtension(result.identity.extensions, Extension::FlatNinth))         ext += "♭9";
        if (hasExtension(result.identity.extensions, Extension::SharpNinth))        ext += "♯9";
        if (hasExtension(result.identity.extensions, Extension::SharpEleventh))     ext += "#11";
        if (hasExtension(result.identity.extensions, Extension::FlatThirteenth))    ext += "♭13";
        if (hasExtension(result.identity.extensions, Extension::SharpThirteenth))   ext += "♯13";
        if (hasExtension(result.identity.extensions, Extension::SixNine))            ext += "6/9";
        return ext;
    }

    std::string nashvilleBassSuffix(const ChordAnalysisResult& result) {
        if (result.identity.bassPc != result.identity.rootPc) {
            int bassDegree = (result.identity.bassPc - result.function.keyTonicPc + 12) % 12;
            // For now, just show as "/[bassDegree+1]"; refine as needed
            return "/" + std::to_string((bassDegree % 7) + 1);
        }
        return "";
    }
}

std::string formatNashvilleNumber(const ChordAnalysisResult& result, int keySignatureFifths) {
    std::string nashville;

    if (result.function.degree >= 0 && result.function.degree < 7) {
        nashville = nashvilleDegree(result.function.degree);
    } else {
        // Chromatic: add accidental prefix (♭ or ♯) based on semitone offset from diatonic degree
        // For now, just show as "?"; refine as needed
        nashville = "?";
    }

    nashville += nashvilleQualitySuffix(result);
    nashville += nashvilleExtensionSuffix(result);

    // Deduplication: if quality suffix ("°") and extension suffix ("°7") are both
    // appended for a fully diminished chord, the combined string contains "°°7".
    // Collapse any run of two or more consecutive "°" (U+00B0, 2-byte UTF-8 \xc2\xb0)
    // to a single "°" so the output is "°7" not "°°7".
    static const std::string kDegreeSymbol = "\xc2\xb0";  // UTF-8 for U+00B0 (°)
    static const std::string kDoubleDegree = "\xc2\xb0\xc2\xb0";
    while (nashville.find(kDoubleDegree) != std::string::npos) {
        nashville.replace(nashville.find(kDoubleDegree), kDoubleDegree.size(), kDegreeSymbol);
    }

    nashville += nashvilleBassSuffix(result);

    return nashville;
}

} // namespace ChordSymbolFormatter

// ── chordTonePitchClasses ─────────────────────────────────────────────────────

std::vector<int> chordTonePitchClasses(const ChordAnalysisResult& result)
{
    const int r = result.identity.rootPc;
    auto pc = [&](int semitones) { return (r + semitones) % 12; };

    // Start with the triad implied by quality.
    // Third slot:
    int thirdInterval = -1;  // -1 = no third
    switch (result.identity.quality) {
    case ChordQuality::Major:
    case ChordQuality::Augmented:
        thirdInterval = 4;
        break;
    case ChordQuality::Minor:
    case ChordQuality::Diminished:
    case ChordQuality::HalfDiminished:
        thirdInterval = 3;
        break;
    case ChordQuality::Suspended2:
        thirdInterval = 2;
        break;
    case ChordQuality::Suspended4:
        thirdInterval = 5;
        break;
    case ChordQuality::Power:
    case ChordQuality::Unknown:
        thirdInterval = -1;
        break;
    }

    // Fifth slot:
    int fifthInterval = -1;
    switch (result.identity.quality) {
    case ChordQuality::Major:
    case ChordQuality::Minor:
    case ChordQuality::Suspended2:
    case ChordQuality::Suspended4:
    case ChordQuality::Power:
        fifthInterval = 7;
        break;
    case ChordQuality::Diminished:
    case ChordQuality::HalfDiminished:
        fifthInterval = 6;
        break;
    case ChordQuality::Augmented:
        fifthInterval = 8;
        break;
    case ChordQuality::Unknown:
        fifthInterval = -1;
        break;
    }

    // Apply fifth alterations (override the quality's default).
    if (hasExtension(result.identity.extensions, Extension::FlatFifth) && fifthInterval == 7) {
        fifthInterval = 6;
    }
    if (hasExtension(result.identity.extensions, Extension::SharpFifth) && fifthInterval == 7) {
        fifthInterval = 8;
    }

    // Collect: root is always first.
    std::vector<int> pcs;
    pcs.push_back(r);

    // Third (skip if omitted).
    if (thirdInterval >= 0 && !hasExtension(result.identity.extensions, Extension::OmitsThird)) {
        pcs.push_back(pc(thirdInterval));
    }

    // Fifth.
    if (fifthInterval >= 0) {
        pcs.push_back(pc(fifthInterval));
    }

    // Seventh.
    if (hasExtension(result.identity.extensions, Extension::MajorSeventh)) {
        pcs.push_back(pc(11));
    } else if (hasExtension(result.identity.extensions, Extension::MinorSeventh)) {
        pcs.push_back(pc(10));
    } else if (hasExtension(result.identity.extensions, Extension::DiminishedSeventh)) {
        pcs.push_back(pc(9));
    }
    // HalfDiminished has a structural minor 7th not flagged as hasMinorSeventh.
    if (result.identity.quality == ChordQuality::HalfDiminished
        && !hasExtension(result.identity.extensions, Extension::MinorSeventh) && !hasExtension(result.identity.extensions, Extension::MajorSeventh)) {
        pcs.push_back(pc(10));
    }

    // Added sixth (when no seventh — otherwise it's a 13th).
    if (hasExtension(result.identity.extensions, Extension::AddedSixth) && !hasExtension(result.identity.extensions, Extension::MinorSeventh)
        && !hasExtension(result.identity.extensions, Extension::MajorSeventh) && !hasExtension(result.identity.extensions, Extension::DiminishedSeventh)) {
        pcs.push_back(pc(9));
    }

    // Upper extensions.
    if (hasExtension(result.identity.extensions, Extension::FlatNinth)) {
        pcs.push_back(pc(1));
    }
    if (hasExtension(result.identity.extensions, Extension::NaturalNinth)) {
        pcs.push_back(pc(2));
    }
    if (hasExtension(result.identity.extensions, Extension::SharpNinth)) {
        pcs.push_back(pc(3));
    }
    if (hasExtension(result.identity.extensions, Extension::NaturalEleventh)) {
        pcs.push_back(pc(5));
    }
    if (hasExtension(result.identity.extensions, Extension::SharpEleventh)) {
        pcs.push_back(pc(6));
    }
    if (hasExtension(result.identity.extensions, Extension::NaturalThirteenth)) {
        pcs.push_back(pc(9));
    }
    if (hasExtension(result.identity.extensions, Extension::FlatThirteenth)) {
        pcs.push_back(pc(8));
    }
    if (hasExtension(result.identity.extensions, Extension::SharpThirteenth)) {
        pcs.push_back(pc(10));
    }

    // Deduplicate (extensions may overlap with triad tones in pitch-class space).
    std::vector<int> unique;
    unique.push_back(pcs[0]);  // root always first
    for (size_t i = 1; i < pcs.size(); ++i) {
        bool dup = false;
        for (int u : unique) {
            if (u == pcs[i]) { dup = true; break; }
        }
        if (!dup) {
            unique.push_back(pcs[i]);
        }
    }

    // Sort upper tones (everything after root) ascending from root.
    if (unique.size() > 1) {
        std::sort(unique.begin() + 1, unique.end(), [&](int a, int b) {
            int relA = (a - r + 12) % 12;
            int relB = (b - r + 12) % 12;
            return relA < relB;
        });
    }

    return unique;
}

// ── closePositionVoicing ─────────────────────────────────────────────────────

ClosePositionVoicing closePositionVoicing(const ChordAnalysisResult& result)
{
    if (result.identity.quality == ChordQuality::Unknown) {
        return {};
    }

    const std::vector<int> pcs = chordTonePitchClasses(result);
    if (pcs.empty()) {
        return {};
    }

    ClosePositionVoicing v;

    // Bass: root in C2–C3 (MIDI 36–48), nearest to midpoint 42.
    const int rootPc = pcs[0];
    {
        constexpr int kBassLow = 36;   // C2
        constexpr int kBassMid = 42;   // F#2
        // Find the octave placement nearest to midpoint.
        int best = kBassLow + rootPc;
        if (best < kBassLow) {
            best += 12;
        }
        // Check one octave up too, pick closer to midpoint.
        if (best + 12 <= 48 && std::abs(best + 12 - kBassMid) < std::abs(best - kBassMid)) {
            best += 12;
        }
        v.bassPitch = best;
    }

    // Treble: upper tones in close position above C4 (MIDI 60).
    // Each successive tone is placed ascending from the previous, within one octave.
    if (pcs.size() > 1) {
        constexpr int kTrebleFloor = 60;  // C4
        int prev = kTrebleFloor;

        for (size_t i = 1; i < pcs.size(); ++i) {
            // Place this pc at or above prev.
            int pitch = kTrebleFloor + pcs[i];
            // Normalize into the correct octave: at or above prev.
            while (pitch < prev) {
                pitch += 12;
            }
            // If it jumped more than an octave above the floor, bring it down.
            // (Only possible for the first tone; subsequent tones just stack.)
            v.treblePitches.push_back(pitch);
            prev = pitch;
        }
    }

    return v;
}

std::unique_ptr<IChordAnalyzer> ChordAnalyzerFactory::create(ChordAnalyzerType type)
{
    switch (type) {
    case ChordAnalyzerType::RuleBased:
    default:
        return std::make_unique<RuleBasedChordAnalyzer>();
    }
}

} // namespace mu::composing::analysis
