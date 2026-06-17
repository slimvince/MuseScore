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
#include <cctype>
#include <cstddef>
#include <cstdint>
#include <string>
#include <vector>

namespace mu::composing::analysis {
namespace {

/// Return the standard English name for a pitch class, choosing flat vs sharp
/// based on the key signature.  Applies German B/H mapping when spelling requires it.
/// German mapping mirrors tpc2name() GERMAN case (pitchspelling.cpp:343-356):
///   Rule 1: B natural → "H"
///   Rule 2: Bb → "B"
/// All other note names are unchanged.
const char* csfPitchClassName(int pc, int keySignatureFifths,
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
const char* csfPitchClassNameFromTpc(int pc, int tpc, int keySignatureFifths,
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
        // canonical chord-symbol spelling.
        //   Eb (pc=3)  diatonic at E major (keyFifths=4) → D# in C/G/D/A major becomes Eb
        //   Bb (pc=10) diatonic at B major (keyFifths=5) → A# in C through 4 sharps → Bb
        //
        // G# (pc=8): Iter 78/84/89 — the pc=8 normalisation is intentionally
        // omitted here.  G# is the leading tone of A in every minor-mode
        // regime, the third of E (V/V in flat-key Baroque writing), and the
        // raised 4th of D major (also V/V).  A corpus survey of 533 sharp-
        // authored pc=8 bass tones across Baroque + Jazz Bach chorales found
        // zero false-positive risk to honoring the composer's sharp TPC.
        // Iter 78's blanket flattening produced 155/277 wrong "E/Ab", "Bm/Ab"
        // etc. spellings in the Baroque corpus at keyFifths<0 and keyFifths==2.
        // pc=8 falls through to the explicit TPC-disambiguation block below,
        // which spells pc=8 sharp or flat per the authored TPC across all
        // key signatures.  D# (pc=3) and A# (pc=10) have no analogous
        // leading-tone status and still normalise to Eb / Bb.
        if (tpc >= 20) {
            const size_t idx = static_cast<size_t>(normalizePc(pc));
            if ((pc == 3  && keySignatureFifths < 4)                          // D# → Eb
             || (pc == 10 && keySignatureFifths < 5))                         // A# → Bb
            {
                return isGerman ? FLAT_NAMES_GERMAN[idx] : FLAT_NAMES[idx];
            }
        }

        if (keySignatureFifths == 0
            || (keySignatureFifths == 1 && pc == 8)
            || (keySignatureFifths < 0 && pc == 6)
            || (keySignatureFifths < 0 && pc == 8)
            || (keySignatureFifths == 2 && pc == 8)) {
            // Key signature gives no decisive flat/sharp preference, or the
            // composer's TPC is the only reliable signal:
            //   • fifths==0 (C major / A minor): no key preference at all.
            //   • fifths==1 && pc==8: A melodic minor mapped to its Dorian
            //     parent slot at +1 fifths; G# is the leading tone.
            //   • fifths<0 && pc==6 (Iter 88): F# is the leading tone in
            //     G minor and a frequent secondary leading tone (V/V third,
            //     tonicized V6) in flat-key Baroque writing.  csfPitchClassName()
            //     unconditionally returns "Gb" for any keyFifths<0, but a
            //     score-authored sharp TPC (e.g. F#=20/21) means the composer
            //     wrote F# explicitly and the chord symbol must honor that.
            //     Gb-authored TPCs (tpc=8/9) still fall through to "Gb" via
            //     the flat range below, so deep flat keys (Ab/Db/Gb major,
            //     where pc=6 is the diatonic Gb) are unaffected.
            //   • fifths<0 && pc==8 and fifths==2 && pc==8 (Iter 89): G# is
            //     the M3 of E (V/V in flat-key Baroque, V/V in D major),
            //     the M7 of A (leading tone), or the chromatic V/V leading
            //     tone in various flat- and mildly-sharp-key contexts.
            //     The Iter 78 sharp-TPC flattening for pc=8 mis-spelled
            //     ~155/277 sharp-authored Baroque cases and ~95/256 Jazz
            //     cases as "E/Ab", "Bm/Ab", etc. when the composer wrote
            //     G# explicitly.  Flat-authored Ab (tpc=10/11) in these
            //     keys (Fm/Ab, Bbm7/Ab, Ab root chords) still falls through
            //     to "Ab" via the flat range below.  Survey: 0 sharp-
            //     authored cases in either corpus where Ab is the correct
            //     spelling (every flat-correct case is flat-authored).
            // Flat range covers both encodings: MuseScore [7,13] and +1
            // encoding [8,14].  Union [7,14] is safe because natural notes
            // (FLAT==SHARP).
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
    return csfPitchClassName(pc, keySignatureFifths, spelling);
}

std::string csfQualitySuffix(ChordQuality quality, bool hasMin7, bool hasMaj7, bool hasDim7,
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
    // Diminished/HalfDiminished are excluded: their suffix already asserts a diminished
    // fifth ("dim", "m7b5"), so appending "#5" would yield a self-contradictory symbol
    // (e.g. "m7b5#5") — mirrors the HalfDiminished guard on the b5 block below.
    if (hasSharpFifth && quality != ChordQuality::Augmented
            && quality != ChordQuality::Diminished
            && quality != ChordQuality::HalfDiminished
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
static std::string csfChromaticRoman(int semitone, int modeIdx, bool isMinorQuality)
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

std::string csfDiatonicRoman(const ChordAnalysisResult& r)
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

std::vector<int> csfCoreIntervals(ChordQuality quality, bool hasMinorSeventh, bool hasMajorSeventh,
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

std::string csfRomanWithInversion(const std::string& roman, ChordQuality quality, int rootPc, int bassPc,
                               bool hasMinorSeventh, bool hasMajorSeventh, bool hasDiminishedSeventh)
{
    if (roman.empty() || bassPc == rootPc) {
        return roman;
    }

    const int bassInterval = normalizePc(bassPc - rootPc);
    const std::vector<int> intervals = csfCoreIntervals(quality, hasMinorSeventh, hasMajorSeventh,
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

} // namespace

/// Returns true if bass is a valid plain note name: 1–3 chars,
/// uppercase letter followed only by ASCII accidentals ('#' or 'b').
/// Guards against chord symbol strings accidentally appearing in the
/// bass field of slash chords (e.g. "C7b9/Bb" instead of "Bb").
static bool csfIsValidBassNoteName(const char* bass)
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
        std::string symbol = std::string(csfPitchClassNameFromTpc(result.identity.rootPc, result.identity.rootTpc, keySignatureFifths, opts.spelling));
        symbol += hasExtension(result.identity.extensions, Extension::NaturalNinth) ? "Maj9sus" : "Maj7sus";
        if (result.identity.bassPc != result.identity.rootPc
                && result.identity.bassPc >= 0 && result.identity.bassPc < 12) {
            const char* bassName = csfPitchClassNameFromTpc(result.identity.bassPc, result.identity.bassTpc, keySignatureFifths, opts.spelling);
            if (csfIsValidBassNoteName(bassName)) {
                symbol += "/";
                symbol += bassName;
            }
        }
        return symbol;
    }

    std::string symbol = std::string(csfPitchClassNameFromTpc(result.identity.rootPc, result.identity.rootTpc, keySignatureFifths, opts.spelling))
                        + csfQualitySuffix(result.identity.quality,
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
        const char* bassName = csfPitchClassNameFromTpc(result.identity.bassPc, result.identity.bassTpc, keySignatureFifths, opts.spelling);
        if (csfIsValidBassNoteName(bassName)) {
            symbol += "/";
            symbol += bassName;
        }
    }

    return symbol;
}

// ── Tonicization helpers ──────────────────────────────────────────────────────

/// Diatonic scale intervals for the seven diatonic modes (semitones from tonic).
static constexpr std::array<int, 7> csfTonicizationScales[7] = {
    { 0, 2, 4, 5, 7, 9, 11 }, // Ionian
    { 0, 2, 3, 5, 7, 9, 10 }, // Dorian
    { 0, 1, 3, 5, 7, 8, 10 }, // Phrygian
    { 0, 2, 4, 6, 7, 9, 11 }, // Lydian
    { 0, 2, 4, 5, 7, 9, 10 }, // Mixolydian
    { 0, 2, 3, 5, 7, 8, 10 }, // Aeolian
    { 0, 1, 3, 5, 6, 8, 10 }, // Locrian
};

/// Maps all 21 KeySigMode ordinals to their diatonic parent index (0..6).
static constexpr std::array<size_t, 21> csfTonicizationParent = {
    0, 1, 2, 3, 4, 5, 6,   // diatonic: identity
    1, 2, 3, 4, 5, 6, 0,   // melodic minor family
    5, 6, 0, 1, 2, 3, 4    // harmonic minor family
};

/// Return the diatonic scale degree (0..6) for pitch class `pc` relative to
/// `tonicPc` in `scale`, or -1 if `pc` is not a scale member.
static int csfDiatonicDegreeForPc(int pc, int tonicPc, const std::array<int, 7>& scale)
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
static bool csfIsDegreeMajorThird(int d, const std::array<int, 7>& scale)
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
        // csfChromaticRoman() only knows the 7 diatonic modes (SCALES[0..6]).
        // Map non-diatonic modes to their diatonic parent before calling it.
        static constexpr std::array<int, 21> CHR_DIATONIC_PARENT = {
            0, 1, 2, 3, 4, 5, 6,  // diatonic: identity
            1, 2, 3, 4, 5, 6, 0,  // melodic minor family
            5, 6, 0, 1, 2, 3, 4   // harmonic minor family
        };
        const int modeIdx = CHR_DIATONIC_PARENT[static_cast<size_t>(keyModeIndex(result.function.keyMode))];
        const std::string chrBase = csfChromaticRoman(semitone, modeIdx, isMinorQuality);
        if (chrBase.empty()) {
            return "";  // Should not occur in standard 12-tone music
        }
        // Reuse csfDiatonicRoman with degree = 0 to get the quality/extension suffix
        // (e.g. "o", "+", "ø7", "M7", "(add6)").  degree = 0 always yields a
        // single-character base "I"/"i" that we strip, leaving only the suffix.
        ChordAnalysisResult tmp = result;
        tmp.function.degree = 0;
        const std::string diatonized = csfDiatonicRoman(tmp);
        const std::string suffix = diatonized.size() > 1 ? diatonized.substr(1) : "";
        romanNumeral = chrBase + suffix;
    } else {
        romanNumeral = csfDiatonicRoman(result);
    }

    romanNumeral = csfRomanWithInversion(romanNumeral, result.identity.quality,
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
            const size_t modeScaleIdx = csfTonicizationParent[keyModeIndex(result.function.keyMode)];
            const std::array<int, 7>& scale = csfTonicizationScales[modeScaleIdx];

            const int nextDegree = csfDiatonicDegreeForPc(nextPc, result.function.keyTonicPc, scale);

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

                const bool upper = csfIsDegreeMajorThird(nextDegree, scale);
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

} // namespace mu::composing::analysis
