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
#include "composing/analysis/function/harmonicfunctionlayer.h"

#include <algorithm>
#include <array>
#include <cmath>
#include <limits>

namespace fn = mu::composing::function;

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
            //     tonicized V6) in flat-key Baroque writing.  pitchClassName()
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
/// Minimum pcWeight for the defining P4 to be treated as a structural suspension
/// tone.  Below this, the Sus4 template is penalised even when the P4 is
/// technically present — passing or ornamental fourths routinely clear 0.20
/// (extensionThreshold) but rarely reach 0.50.
static constexpr double kSus4StructuralFourthThreshold = 0.50;
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
    // The dim7 characteristic only applies to a fully-formed diminished triad.
    // Without root, minor-third AND diminished-fifth all sounding, the root+9
    // tone is not functioning as a diminished seventh — it belongs to another
    // harmony (e.g. {C#,E,F#,A#} is F#7, not an incomplete C#°7 missing its G).
    // Requiring the complete triad leaves genuine vii°7 / chromatic °7 chords
    // (which always voice root + b3 + b5) untouched, while suppressing the
    // spurious bonus that let an incomplete °7 outscore a perfect dominant-7th.
    const int b3Pc = (rootPc + 3) % 12;
    const int b5Pc = (rootPc + 6) % 12;
    if (pcWeight[static_cast<size_t>(rootPc)] <= extThreshold
        || pcWeight[static_cast<size_t>(b3Pc)] <= extThreshold
        || pcWeight[static_cast<size_t>(b5Pc)] <= extThreshold) {
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
        if (pcWeight[static_cast<size_t>(fourthPc)] < kSus4StructuralFourthThreshold) {
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

    // Extended in Iter 46 to include Augmented and HalfDiminished: these quality
    // types were systematically excluded from inversion bonuses, causing correct
    // inverted readings to fall below the results[] threshold.
    const bool supportedQuality = (tpl.quality == ChordQuality::Major
                                   || tpl.quality == ChordQuality::Minor
                                   || tpl.quality == ChordQuality::Diminished
                                   || tpl.quality == ChordQuality::Augmented
                                   || tpl.quality == ChordQuality::HalfDiminished);
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
    // Extended in Iter 46 to include Augmented and HalfDiminished: these quality
    // types were systematically excluded from inversion bonuses, causing correct
    // inverted readings (e.g. C+/E, Yø7/X) to fall below the results[] threshold.
    // They now compete on equal terms with Major/Minor inversions.
    const bool isInvertedSupportedQuality = (rootPc != bassPc)
                                  && (tpl.quality == ChordQuality::Major
                                      || tpl.quality == ChordQuality::Minor
                                      || tpl.quality == ChordQuality::Augmented
                                      || tpl.quality == ChordQuality::HalfDiminished);
    return isInvertedSupportedQuality && templateHasMatchingThird(tpl, rootPc, pcWeight);
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

    // Prefer roots that belong to the current key scale.
    for (int interval : scale) {
        if ((keyTonicPc + interval) % 12 == rootPc) {
            score += prefs.diatonicRootBonus;
            break;
        }
    }

    if (context) {
        // Root-continuity: prefer keeping the same root across successive chords.
        if (!prefs.suppressProgressionSignals) {
            score += fn::rootContinuityBonus(rootPc, context->previousRootPc,
                                             prefs.rootContinuityBonus);
        }

        // Contextual inversion bonuses — §4.1b
        // Accumulated into a local variable so the total can be capped before
        // application (prevents runaway stacking when multiple signals fire).
        // Only for inverted Major/Minor candidates (lesson from three-attempt
        // inversion fix history: never apply to Diminished/HalfDiminished/Augmented).
        const bool isInvertedMajMin = supportsContextualInversionBonuses(tpl, rootPc, bassPc, pcWeight);
        double inversionContextBonus = 0.0;

        // completeTriadInversionBonus gates on stepwise evidence (checked here
        // rather than in the isInvertedMajMin block because it guards a structural
        // condition independent of Major/Minor quality).
        if (hasStepwiseBassEvidence
                && qualifiesForCompleteTriadInversionBonus(tpl, rootPc, bassPc, pcWeight, distinctPcs)) {
            inversionContextBonus += prefs.completeTriadInversionBonus;
        }

        if (isInvertedMajMin) {
            if (context->bassIsStepwiseFromPrevious) {
                inversionContextBonus += prefs.stepwiseBassInversionBonus;
            }
            if (context->bassIsStepwiseToNext) {
                inversionContextBonus += prefs.stepwiseBassLookaheadBonus;
            }
            if (context->previousRootPc != -1
                    && context->previousRootPc == rootPc) {
                inversionContextBonus += prefs.sameRootInversionBonus;
            }
        }

        // Apply the cap — prevents multi-signal stacking from overwhelming the
        // bass-root bonus on genuinely root-position chords.
        score += std::min(inversionContextBonus, prefs.maxTotalInversionContextBonus);

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

// Iter 92 — bass-split contextual bonuses.
//
// contextualBonuses() above is a monolithic helper.  The two helpers below
// split its body so that the (rootPc, templateIdx) scoring loop can compute
// the bass-INDEPENDENT contribution exactly once per cell and then evaluate
// each bass-candidate by adding the bass-DEPENDENT delta only.
//
// Invariant:
//   bassIndependentContextualBonuses(tpl, rootPc, ..., context)
//   + bassDependentContextualBonuses(tpl, rootPc, bassPc, appliedBassBonus, ...)
//   == contextualBonuses(tpl, rootPc, bassPc, appliedBassBonus, ..., context)
//
// for every (tpl, rootPc, bassPc, context).  This is asserted by Step 2's
// byte-identical verification.
double bassIndependentContextualBonuses(const TemplateDef& tpl, int rootPc,
                                        int keyTonicPc, const std::array<int, 7>& scale,
                                        const ChordAnalyzerPreferences& prefs,
                                        const ChordTemporalContext* context)
{
    double score = 0.0;

    // Prefer roots that belong to the current key scale.
    for (int interval : scale) {
        if ((keyTonicPc + interval) % 12 == rootPc) {
            score += prefs.diatonicRootBonus;
            break;
        }
    }

    if (context) {
        // Root-continuity: prefer keeping the same root across successive chords.
        //
        // KNOWN DEAD END (Iter 98, 2026-05-23): suppressing this bonus when the
        // predecessor region has distinctPcs <= 2 was tried in two variants and
        // both regressed mozart_k280-1 IV→V65 in Alberti-bass contexts.  The
        // signal is load-bearing for legitimate sparse continuity (broken-chord
        // bass with held upper voices).  Do not attempt a density-based or
        // inversion-aware gate here without first reading the Iter 98 dead-end
        // section in COWORK_HANDOFF.md.  See docs/scoring_model.md §4.
        if (!prefs.suppressProgressionSignals) {
            score += fn::rootContinuityBonus(rootPc, context->previousRootPc,
                                             prefs.rootContinuityBonus);
        }

        // Quality-guided resolution bias: reward candidates at the typical
        // resolution target of the previous chord's quality.
        if (context->previousQuality != ChordQuality::Unknown
                && context->previousRootPc >= 0) {
            const int prevRoot = context->previousRootPc;
            const ChordQuality prevQ = context->previousQuality;
            const double rb = prefs.resolutionBonus;

            if (prevQ == ChordQuality::Diminished
                    && (tpl.quality == ChordQuality::Major || tpl.quality == ChordQuality::Minor)
                    && rootPc == (prevRoot + 1) % 12) {
                score += rb;
            }
            if (prevQ == ChordQuality::HalfDiminished
                    && tpl.quality == ChordQuality::Major
                    && rootPc == (prevRoot + 5) % 12) {
                score += rb;
            }
            if (prevQ == ChordQuality::Augmented
                    && (tpl.quality == ChordQuality::Major || tpl.quality == ChordQuality::Minor)
                    && rootPc == prevRoot) {
                score += rb;
            }
        }
    }

    return score;
}

double bassDependentContextualBonuses(const TemplateDef& tpl, int rootPc, int bassPc,
                                      double appliedBassBonus,
                                      int distinctPcs,
                                      const std::array<double, 12>& pcWeight,
                                      const ChordAnalyzerPreferences& prefs,
                                      const ChordTemporalContext* context,
                                      bool hasStructuralBass = true)
{
    double score = appliedBassBonus;

    if (context && hasStructuralBass) {
        const bool hasStepwiseBassEvidence =
            context->bassIsStepwiseFromPrevious || context->bassIsStepwiseToNext;
        const bool isInvertedMajMin =
            supportsContextualInversionBonuses(tpl, rootPc, bassPc, pcWeight);
        double inversionContextBonus = 0.0;

        if (hasStepwiseBassEvidence
                && qualifiesForCompleteTriadInversionBonus(tpl, rootPc, bassPc, pcWeight, distinctPcs)) {
            inversionContextBonus += prefs.completeTriadInversionBonus;
        }

        if (isInvertedMajMin) {
            if (context->bassIsStepwiseFromPrevious) {
                inversionContextBonus += prefs.stepwiseBassInversionBonus;
            }
            if (context->bassIsStepwiseToNext) {
                inversionContextBonus += prefs.stepwiseBassLookaheadBonus;
            }
            if (context->previousRootPc != -1
                    && context->previousRootPc == rootPc) {
                inversionContextBonus += prefs.sameRootInversionBonus;
            }
        }

        score += std::min(inversionContextBonus, prefs.maxTotalInversionContextBonus);
    }

    return score;
}

} // namespace

ChordAnalysisResult buildChordResult(
    const RawCandidate&             rc,
    const BuildChordResultContext&  ctx,
    const ChordAnalyzerPreferences& prefs)
{
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
    if (quality == ChordQuality::Augmented && ctx.tpcForPc[static_cast<size_t>(rootPc)] < 0) {
        std::vector<int> pcs;
        for (int pc = 0; pc < 12; ++pc) {
            if (ctx.pcWeight[static_cast<size_t>(pc)] > 0.05) {
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
                // Iter 92 — use the joint-winner bass instead of the absolute
                // lowest pitch. The two could disagree when the joint pass
                // picks an octave-up bass-register candidate as the winner.
                rootPc = ctx.bassPc;
            }
        }
    }

    const int rootTpc = ctx.tpcForPc[static_cast<size_t>(rootPc)];
    ExtensionFlags ext = detectExtensions(ctx.pcWeight, rootPc, quality, ctx.tpcForPc, rootTpc, prefs.extensionThreshold);

    // 2. Sus2 → Sus4 upgrade: Sus4 is more specific when P4 is actually sounding.
    if (quality == ChordQuality::Suspended2 && ext.hasEleventh) {
        quality = ChordQuality::Suspended4;
        ext = detectExtensions(ctx.pcWeight, rootPc, quality, ctx.tpcForPc, rootTpc, prefs.extensionThreshold);
    }

    // 3. Sus → Major (omitsThird): when Maj7 is present but no 3rd is sounding,
    // the catalog labels the chord as Major quality.  This covers both the
    // "no-fourth" case (true suspended with Maj7) and the "with-fourth" case
    // (CMaj7sus4 / CMaj9sus4).  A present P4 is retained as an extension.
    const bool hasMajThird  = ctx.pcWeight[static_cast<size_t>((rootPc + 4) % 12)] > 0.2;
    const bool hasMinThird  = ctx.pcWeight[static_cast<size_t>((rootPc + 3) % 12)] > 0.2;
    const bool hasAnyThird  = hasMajThird || hasMinThird;

    bool omitsThird = false;
    if (ext.hasMajorSeventh && !hasAnyThird
        && (quality == ChordQuality::Suspended2 || quality == ChordQuality::Suspended4)) {
        quality    = ChordQuality::Major;
        omitsThird = true;
        ext = detectExtensions(ctx.pcWeight, rootPc, quality, ctx.tpcForPc, rootTpc, prefs.extensionThreshold);
    }

    // Degree assignment.
    int degree = -1;
    for (size_t i = 0; i < ctx.scale.size(); ++i) {
        if ((ctx.keyTonicPc + ctx.scale[i]) % 12 == rootPc) {
            degree = static_cast<int>(i);
            break;
        }
    }

    // Diatonic check: every sounding pc must be in the scale.
    bool diatonic = (degree >= 0);
    if (diatonic) {
        for (int pc = 0; pc < 12; ++pc) {
            if (ctx.pcWeight[static_cast<size_t>(pc)] <= 0.2) {
                continue;
            }
            bool inScale = false;
            for (int interval : ctx.scale) {
                if ((ctx.keyTonicPc + interval) % 12 == pc) {
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
    r.identity.bassPc               = ctx.bassPc;
    r.identity.bassTpc              = ctx.bassTpc;
    r.identity.naturalFifthPresent  = (quality != ChordQuality::Augmented)
                                      && (ctx.pcWeight[static_cast<size_t>((rootPc + 7) % 12)]
                                          > prefs.extensionThreshold);
    r.identity.quality              = quality;
    r.identity.tiePriority          = static_cast<int>(rc.tiePriority);
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
    r.function.keyTonicPc           = ctx.keyTonicPc;
    r.function.keyMode              = ctx.keyMode;

    return r;
}

void applyPostScoringGates(
    std::vector<ChordAnalysisResult>& results,
    const ChordAnalyzerPreferences&   prefs,
    const ChordTemporalContext*       context,
    const PostScoringGateContext&     gateCtx)
{
    // Local convenience: build a ChordAnalysisResult from a RawCandidate using
    // the captured gate context. Mirrors the buildResult lambda the gate block
    // used to call when it lived inside analyzeChord().
    const auto buildResult = [&](const RawCandidate& rc) -> ChordAnalysisResult {
        return buildChordResult(rc,
            BuildChordResultContext{ gateCtx.pcWeight, gateCtx.tpcForPc,
                                     gateCtx.bassPc, gateCtx.bassTpc,
                                     gateCtx.keyTonicPc, gateCtx.keyMode,
                                     gateCtx.scale },
            prefs);
    };

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
        && gateCtx.distinctPcs >= 3)
    {
        // CAPTURE BEFORE stable_sort — Sub-9a bug (fixed in Gate G-E by commit
        // f3e0f5f72c).  winner is a live reference to results[0].  The
        // stable_sort below may promote Am7b5/C (rootPc=9) to results[0], making
        // winner.identity.rootPc=9.  Gate G-E uses originalWinnerRootPc to
        // compute gExpectedAltRoot — if it read winner.identity.rootPc after the
        // sort it would compute the wrong leading tone (e.g. (9+9)%12=6 instead
        // of (0+9)%12=9) and pull in a spurious candidate (the dormant F#m7b5
        // case).  Capture all three originalWinner* fields here for any gate
        // that needs the pre-correction winner.  See docs/scoring_model.md §7.
        //
        // Live reference — winner tracks results[0] through any swap or re-sort.
        // Use originalWinnerQuality, originalWinnerRootPc, and
        // originalWinnerHasAddedSixth (captured below) when you need the
        // pre-swap state in gates that run after A–F.
        const ChordAnalysisResult& winner = results[0];
        const ChordQuality originalWinnerQuality = winner.identity.quality;
        const int originalWinnerRootPc = winner.identity.rootPc;
        const bool originalWinnerHasAddedSixth =
            hasExtension(winner.identity.extensions, Extension::AddedSixth);
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
            size_t bestAltIdx = results.size();
            bool bestAltIsHalfDimInversion = false;
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
                // HalfDiminished first/second/third-inversion exception:
                // accept a HalfDim alt only when all four chord tones (root, m3,
                // b5, m7) are present in the region and the winner's bass pitch
                // class (= winner root, since this block requires bassIsRoot=true)
                // is the alt's m3, b5, or m7. Targets bwv187.7-style cases where
                // the bass-root bonus on a clean Minor reading is blocking the
                // correct inverted half-diminished seventh.
                bool isHalfDimInversion = false;
                if (!isClean && alt.identity.quality == ChordQuality::HalfDiminished) {
                    const int aR = alt.identity.rootPc;
                    const int thirdPc   = (aR + 3) % 12;
                    const int fifthPc   = (aR + 6) % 12;
                    const int seventhPc = (aR + 10) % 12;
                    const double thr = prefs.extensionThreshold;
                    const int wb = winner.identity.bassPc;
                    // The bass pc is by definition sounding — exempt it from the
                    // weight threshold so a briefly-sounded inversion bass (e.g.
                    // bwv187.7 m=14 G at 0.14 vs thr 0.20) does not block the
                    // inversion reading.  Targets Minor-add6 winners where the
                    // bass=m3 of the HalfDim root has short metric duration.
                    auto tonePresent = [&](int pc) {
                        return pc == wb || gateCtx.pcWeight[static_cast<size_t>(pc)] > thr;
                    };
                    const bool allTonesPresent =
                        tonePresent(aR)
                        && tonePresent(thirdPc)
                        && tonePresent(fifthPc)
                        && tonePresent(seventhPc);
                    const bool bassIsInversion =
                        (wb == thirdPc || wb == fifthPc || wb == seventhPc);
                    isHalfDimInversion = allTonesPresent && bassIsInversion;
                }
                if (isClean || isHalfDimInversion) {
                    bestAltIdx = i;
                    bestAltIsHalfDimInversion = isHalfDimInversion;
                    break;
                }
            }

            if (bestAltIdx < results.size()) {
                // ── Enharmonic equivalence fast path ─────────────────────────
                //
                // Major-add6 and Minor7 chords span identical pitch classes when
                // the Minor7 root is a minor third below the Major root:
                //   altRootPc == (winnerRootPc + 9) % 12
                // In bass-heavy textures the scorer systematically favours the
                // bass-root Major reading; margin comparison cannot reliably
                // distinguish the two.  When preferMinorOverMajorAdd6 is set
                // (Standard/Baroque), prefer the Minor alternative directly.
                bool didEnharmonicFlip = false;
                if (prefs.preferMinorOverMajorAdd6) {
                    const bool winnerIsMajor =
                        (winner.identity.quality == ChordQuality::Major);
                    // The added-sixth guard restricts the fast path to sonorities
                    // where the sixth (e.g. G in Bb-D-F-G) is present with enough
                    // structural weight that the analyzer already labeled it as an
                    // added-sixth chord.  Without this guard the fast path fires on
                    // plain C major triads (C-E-G) just because Am is a candidate,
                    // producing a flood of Am7/C regressions on root-position chords.
                    const bool winnerHasAddedSixth =
                        hasExtension(winner.identity.extensions, Extension::AddedSixth);
                    const bool altIsMinor =
                        (results[bestAltIdx].identity.quality == ChordQuality::Minor);
                    const int expectedAltRoot = (winner.identity.rootPc + 9) % 12;
                    if (winnerIsMajor && winnerHasAddedSixth && altIsMinor
                        && results[bestAltIdx].identity.rootPc == expectedAltRoot) {
                        std::swap(results[0], results[bestAltIdx]);
                        didEnharmonicFlip = true;
                    }
                    // FM2 fallback: a higher-scoring different-root alt (e.g. Em/C) may have
                    // blocked the enharmonic partner from entering results[] via the append path.
                    // Scan rawCandidates above threshold for the Minor alt at expectedAltRoot.
                    if (!didEnharmonicFlip && winnerIsMajor && winnerHasAddedSixth) {
                        for (const RawCandidate& rc : gateCtx.rawCandidates) {
                            if (rc.score < gateCtx.threshold) { break; }
                            if (rc.rootPc == expectedAltRoot
                                && rc.quality == ChordQuality::Minor) {
                                results.push_back(buildResult(rc));
                                std::swap(results[0], results.back());
                                didEnharmonicFlip = true;
                                break;
                            }
                        }
                    }
                    // Gate B: the next region's inferred root matches the alternative (Minor) root.
                    // Strong forward evidence that this harmony persists — the bass is passing through
                    // a chord tone, not establishing a new root.
                    if (!didEnharmonicFlip
                        && context != nullptr
                        && winnerIsMajor && winnerHasAddedSixth && altIsMinor
                        && results[bestAltIdx].identity.rootPc == expectedAltRoot
                        && context->nextRootPc != -1
                        && context->nextRootPc == results[bestAltIdx].identity.rootPc
                        && context->bassIsStepwiseToNext) {
                        std::swap(results[0], results[bestAltIdx]);
                        didEnharmonicFlip = true;
                    }
                    // Gate C: the alternative root appears in the 3-region window AND the bass is
                    // moving stepwise from the previous region.  The root has been recently active
                    // and the bass is passing through it — strong evidence of an inversion.
                    if (!didEnharmonicFlip
                        && context != nullptr
                        && winnerIsMajor && winnerHasAddedSixth && altIsMinor
                        && results[bestAltIdx].identity.rootPc == expectedAltRoot
                        && context->bassIsStepwiseFromPrevious) {
                        const auto& rpc = context->recentRootPcs;
                        const bool altRootIsRecent = (rpc[0] == results[bestAltIdx].identity.rootPc
                                                      || rpc[1] == results[bestAltIdx].identity.rootPc
                                                      || rpc[2] == results[bestAltIdx].identity.rootPc);
                        if (altRootIsRecent) {
                            std::swap(results[0], results[bestAltIdx]);
                            didEnharmonicFlip = true;
                        }
                    }
                    // Gate D: two or more consecutive stepwise bass moves ending here.
                    // A scalar bass line is strong evidence of a passing inversion, not a new root.
                    if (!didEnharmonicFlip
                        && context != nullptr
                        && winnerIsMajor && winnerHasAddedSixth && altIsMinor
                        && results[bestAltIdx].identity.rootPc == expectedAltRoot
                        && context->consecutiveBassStepwiseCount >= 2) {
                        std::swap(results[0], results[bestAltIdx]);
                        didEnharmonicFlip = true;
                    }

                }

                // ── Gate E: first-inversion detection ─────────────────────────────────────
                //
                // When the winner is Minor with bassIsRoot=true and the best Major alternative
                // has its root a minor-6th above the winner root (= winner root is the major
                // 3rd of the alt), the scorer has likely identified the bass note (= 3rd of
                // the actual chord) as the root.  E.g., F#m wins when D/F# is correct.
                //
                // Relationship: altRootPc == (winnerRootPc + 8) % 12
                // Gated by preferMinorOverMajorAdd6 (classical presets only) and a stepwise
                // bass signal (temporal context required).
                if (!didEnharmonicFlip
                    && prefs.preferMinorOverMajorAdd6
                    && context != nullptr
                    && winner.identity.quality == ChordQuality::Minor
                    && results[bestAltIdx].identity.quality == ChordQuality::Major
                    && results[bestAltIdx].identity.rootPc == (winner.identity.rootPc + 8) % 12
                    && gateCtx.pcWeight[static_cast<size_t>(results[bestAltIdx].identity.rootPc)] > prefs.extensionThreshold
                    && (context->bassIsStepwiseFromPrevious || context->bassIsStepwiseToNext)) {
                    std::swap(results[0], results[bestAltIdx]);
                    didEnharmonicFlip = true;
                }

                // ── Gate F: second-inversion detection ────────────────────────────────────
                //
                // When the best Major alternative has its root a perfect-4th above the winner
                // root (= winner root is the 5th of the alt), the scorer has likely identified
                // the bass note (= 5th of the actual chord) as the root.
                // E.g., B or BAug wins when E/B is correct.
                //
                // Relationship: altRootPc == (winnerRootPc + 5) % 12
                // Gated by preferMinorOverMajorAdd6 (classical presets only) and a stepwise
                // bass signal (temporal context required).
                if (!didEnharmonicFlip
                    && prefs.preferMinorOverMajorAdd6
                    && context != nullptr
                    && results[bestAltIdx].identity.quality == ChordQuality::Major
                    && results[bestAltIdx].identity.rootPc == (winner.identity.rootPc + 5) % 12
                    && (context->bassIsStepwiseFromPrevious || context->bassIsStepwiseToNext)) {
                    std::swap(results[0], results[bestAltIdx]);
                    didEnharmonicFlip = true;
                }

                if (!didEnharmonicFlip) {
                    const double margin = winner.identity.score - results[bestAltIdx].identity.score;

                    // Seventh-chord exemption: if the winner carries a minor or major
                    // seventh extension that the best alternative lacks, the bass-root
                    // bonus is not the sole structural advantage — the winner is a richer,
                    // more specific reading (e.g. Am7 vs Em triad).  Do not penalise it.
                    const bool winnerHasSeventh =
                        hasExtension(winner.identity.extensions, Extension::MinorSeventh)
                        || hasExtension(winner.identity.extensions, Extension::MajorSeventh);
                    const bool altHasSeventh =
                        hasExtension(results[bestAltIdx].identity.extensions, Extension::MinorSeventh)
                        || hasExtension(results[bestAltIdx].identity.extensions, Extension::MajorSeventh);
                    const bool seventhExempt = winnerHasSeventh && !altHasSeventh;

                    if (!seventhExempt && margin < prefs.inversionSuspicionMargin) {
                        // Deduct the bass-bonus contribution from the winner and re-sort.
                        const double deduction = prefs.bassNoteRootBonus
                                                * (1.0 - prefs.inversionBonusReduction);
                        results[0].identity.score -= deduction;
                        // Confirmed first-inversion HalfDim bonus: when the bestAlt
                        // is a HalfDim with all four chord tones present and the
                        // winner's bass is one of those tones (m3/b5/m7), the
                        // deduction alone is not enough to flip — the bass-root
                        // Minor/Major reading carries residual scoring advantages
                        // (e.g. AddedSixth extension fit) that keep it ahead.
                        // Gated by preferMinorOverMajorAdd6 (same gate as the
                        // existing Minor-add6 ↔ HalfDim7 path, Gate G-E below):
                        // Jazz prefs disable this preference because the
                        // genuine Cm6/Cm69 chord vocabulary is idiomatic and
                        // must outrank the enharmonic Aø7/C inversion reading.
                        if (bestAltIsHalfDimInversion && prefs.preferMinorOverMajorAdd6) {
                            constexpr double kHalfDimFirstInversionBonus = 0.55;
                            results[bestAltIdx].identity.score += kHalfDimFirstInversionBonus;
                        }
                        std::stable_sort(results.begin(), results.end(),
                                         [](const ChordAnalysisResult& a,
                                            const ChordAnalysisResult& b) {
                                             return a.identity.score > b.identity.score;
                                         });
                    }
                }
            }
        // ── Gates G-E / G-B / G-C / G-D: Minor-add6 ↔ HalfDim7 ─────────────────────
        //
        // MinorAdd6 and HalfDim7 share identical pitch classes.
        // kCleanQualities excludes HalfDiminished, so this block runs independently
        // of the bestAlt path above.
        //
        // Gate G-E (key-context): fires when the HalfDim7 alt is a functional chord
        // of the current key — either the leading-tone seventh (viiø7, alt root at
        // tonicPc+11) or the supertonic seventh (iiø7, alt root at tonicPc+2).
        // No temporal signals required.
        //
        // Gates G-B/C/D: temporal fallbacks for the remaining cases.
        if (prefs.preferMinorOverMajorAdd6
            && originalWinnerQuality == ChordQuality::Minor
            && originalWinnerHasAddedSixth) {
            const int gExpectedAltRoot = (originalWinnerRootPc + 9) % 12;
            // Find the HalfDim7 alt in results[].
            size_t halfDimAltIdx = results.size();
            for (size_t i = 1; i < results.size(); ++i) {
                if (results[i].identity.quality == ChordQuality::HalfDiminished
                    && results[i].identity.rootPc == gExpectedAltRoot) {
                    halfDimAltIdx = i;
                    break;
                }
            }
            // Gate G-E: if HalfDim not in results[], look in rawCandidates (temporal
            // context may have suppressed it via rootContinuityBonus)
            if (halfDimAltIdx >= results.size()) {
                for (const auto& rc : gateCtx.rawCandidates) {
                    if (rc.quality == ChordQuality::HalfDiminished
                        && rc.rootPc == gExpectedAltRoot) {
                        results.push_back(buildResult(rc));
                        halfDimAltIdx = results.size() - 1;
                        break;
                    }
                }
            }
            if (halfDimAltIdx != results.size()) {
                bool didGFlip = false;
                // Gate G-E: leading-tone key-context gate.
                // The half-diminished seventh is the standard functional reading when
                // it is rooted on the leading tone (viiø7) or supertonic (iiø7) of
                // the current key.  No temporal signals required.
                const int gLeadingTonePc  = (gateCtx.keyTonicPc + 11) % 12;  // viiø7
                const int gSupertonicPc   = (gateCtx.keyTonicPc + 2) % 12;   // iiø7
                const int gMediantPc      = (gateCtx.keyTonicPc + 4) % 12;   // iiiø7 / mediant
                if (!didGFlip
                    && (results[halfDimAltIdx].identity.rootPc == gLeadingTonePc
                        || results[halfDimAltIdx].identity.rootPc == gSupertonicPc
                        || results[halfDimAltIdx].identity.rootPc == gMediantPc)) {
                    std::swap(results[0], results[halfDimAltIdx]);
                    didGFlip = true;
                }
                // Gate G-B: next region's inferred root matches the HalfDim root.
                // Strong forward evidence the harmony continues on that root.
                if (!didGFlip
                    && context != nullptr
                    && context->nextRootPc != -1
                    && context->nextRootPc == gExpectedAltRoot
                    && context->bassIsStepwiseToNext) {
                    std::swap(results[0], results[halfDimAltIdx]);
                    didGFlip = true;
                }
                // Gate G-C: HalfDim root appears in the 3-region window AND bass
                // is moving stepwise from the previous region.
                if (!didGFlip
                    && context != nullptr
                    && context->bassIsStepwiseFromPrevious) {
                    const auto& rpc = context->recentRootPcs;
                    if (rpc[0] == gExpectedAltRoot
                        || rpc[1] == gExpectedAltRoot
                        || rpc[2] == gExpectedAltRoot) {
                        std::swap(results[0], results[halfDimAltIdx]);
                        didGFlip = true;
                    }
                }
                // Gate G-D: two or more consecutive stepwise bass moves ending here.
                if (!didGFlip
                    && context != nullptr
                    && context->consecutiveBassStepwiseCount >= 2) {
                    std::swap(results[0], results[halfDimAltIdx]);
                    didGFlip = true;
                }
            }
        }
        }

        // ── Gate H: Augmented triad root-symmetry resolution ──────────────────────────
        //
        // An augmented triad has three enharmonic roots (±4 semitones mod 12): D+, F#+,
        // and Bb+ are the same chord.  When the analyzer picks root R but the correct
        // root is (R+4)%12 or (R+8)%12, the two candidates represent the same sonority
        // with different root labels.  Temporal evidence resolves the ambiguity.
        //
        // Unlike the main correction block, this gate handles Augmented winners
        // (excluded from winnerQualityTargeted = Major/Minor).  It fires only with
        // temporal context and is gated by preferMinorOverMajorAdd6 (classical presets).
        if (winnerBassIsRoot
            && winner.identity.quality == ChordQuality::Augmented
            && prefs.preferMinorOverMajorAdd6
            && context != nullptr) {
            bool didAugmentedFlip = false;
            for (const int semitones : {4, 8}) {
                if (didAugmentedFlip) break;
                const int altRoot = (winner.identity.rootPc + semitones) % 12;
                // Find an Augmented candidate at this root.
                size_t augAltIdx = results.size();
                for (size_t i = 1; i < results.size(); ++i) {
                    if (results[i].identity.quality == ChordQuality::Augmented
                        && results[i].identity.rootPc == altRoot) {
                        augAltIdx = i;
                        break;
                    }
                }
                if (augAltIdx == results.size()) continue;
                // Gate H-B: next region's inferred root matches the alt augmented root.
                if (!didAugmentedFlip
                    && context->nextRootPc != -1
                    && context->nextRootPc == altRoot
                    && context->bassIsStepwiseToNext) {
                    std::swap(results[0], results[augAltIdx]);
                    didAugmentedFlip = true;
                }
                // Gate H-C: alt root appears in the 3-region window AND bass is stepwise.
                if (!didAugmentedFlip && context->bassIsStepwiseFromPrevious) {
                    const auto& rpc = context->recentRootPcs;
                    if (rpc[0] == altRoot || rpc[1] == altRoot || rpc[2] == altRoot) {
                        std::swap(results[0], results[augAltIdx]);
                        didAugmentedFlip = true;
                    }
                }
                // Gate H-D: two or more consecutive stepwise bass moves.
                if (!didAugmentedFlip
                    && context->consecutiveBassStepwiseCount >= 2) {
                    std::swap(results[0], results[augAltIdx]);
                    didAugmentedFlip = true;
                }
            }
        }

        // ── Gate I: prefer diatonic first-inversion major over root-position minor ──────
        //
        // When the winner is a Minor chord with bassIsRoot=true and a runner-up shares
        // the same bass note but is a first-inversion chord whose root lies a major third
        // below the bass (I4 interval), and that root is diatonic to the current key,
        // prefer the first-inversion reading.  E.g., Em → C/E when C is diatonic.
        //
        // Score margin guard (≤ 0.45) ensures the gate only fires when the two readings
        // are genuinely competitive — not when the Minor winner is strongly confirmed.
        if (winnerBassIsRoot
            && originalWinnerQuality == ChordQuality::Minor
            && results.size() >= 2
            && gateCtx.keyTonicPc >= 0) {
            for (size_t iIdx = 1; iIdx < results.size(); ++iIdx) {
                const ChordAnalysisResult& inv = results[iIdx];
                const int invBassPc = inv.identity.bassPc;
                const int invRootPc = inv.identity.rootPc;
                if (invBassPc != winner.identity.bassPc)                   continue;  // different bass
                if (invBassPc == invRootPc)                                continue;  // root position
                if ((winner.identity.bassPc - invRootPc + 12) % 12 != 4)  continue;  // not I4 interval
                const int invInterval = (invRootPc - gateCtx.keyTonicPc + 12) % 12;
                bool invRootIsDiatonic = false;
                for (int d = 0; d < 7; ++d) {
                    if (gateCtx.scale[d] == invInterval) { invRootIsDiatonic = true; break; }
                }
                if (!invRootIsDiatonic)                                    continue;  // not diatonic
                if (gateCtx.pcWeight[static_cast<size_t>(invRootPc)] <= prefs.extensionThreshold) {
                    continue;  // promoted root absent from the score — do not invent a rootless inversion
                }
                if (winner.identity.score - inv.identity.score > 0.45f)   continue;  // margin too wide
                std::swap(results[0], results[iIdx]);
                break;
            }
        }

        // ── Gate K: prefer first-inversion augmented over root-position augmented ──────────
        //
        // When the winner is an Augmented chord with bassIsRoot=true and a runner-up shares
        // the same bass note but is NOT root-position, with its root a major third below
        // the bass (I4 interval), prefer the first-inversion reading.  E.g., D+ → Bb#5/D.
        //
        // Quality condition covers both encoding variants of an augmented-collection chord:
        // Augmented quality directly, or Major with SharpFifth extension.
        //
        // Margin guard (≤ 0.20) keeps the gate narrow; all reachable targets have margin ≤ 0.12.
        if (winnerBassIsRoot
            && originalWinnerQuality == ChordQuality::Augmented
            && results.size() >= 2
            && gateCtx.keyTonicPc >= 0) {
            for (size_t iIdx = 1; iIdx < results.size(); ++iIdx) {
                const ChordAnalysisResult& inv = results[iIdx];
                if (inv.identity.bassPc != winner.identity.bassPc)                   continue;  // different bass
                if (inv.identity.bassPc == inv.identity.rootPc)                      continue;  // root position
                if ((winner.identity.bassPc - inv.identity.rootPc + 12) % 12 != 4)  continue;  // not I4 interval
                const bool isAugmentedCollection =
                    inv.identity.quality == ChordQuality::Augmented
                    || (inv.identity.quality == ChordQuality::Major
                        && hasExtension(inv.identity.extensions, Extension::SharpFifth));
                if (!isAugmentedCollection)                                          continue;  // not augmented quality
                const int invInterval = (inv.identity.rootPc - gateCtx.keyTonicPc + 12) % 12;
                bool invRootIsDiatonic = false;
                for (int d = 0; d < 7; ++d) {
                    if (gateCtx.scale[d] == invInterval) { invRootIsDiatonic = true; break; }
                }
                if (!invRootIsDiatonic)                                              continue;  // not diatonic
                if (winner.identity.score - inv.identity.score > 0.20f)             continue;  // margin too wide
                std::swap(results[0], results[iIdx]);
                break;
            }
        }

        // ── Gate L: prefer same-root Major over root-position Augmented (TYPE-A quality fix) ──
        //
        // When the winner is a plain Augmented triad (no 7th extension) at root position
        // and a runner-up shares the exact same root AND same bass (also root-position),
        // has Major quality, and that root is diatonic to the current key, prefer Major.
        // E.g., B+ → B (Bmin), E+ → E (Cmaj), F+ → F (FDor).
        //
        // Seventh exclusion: augmented +7 chords (e.g. C+7 jazz dominant) are intentionally
        // augmented and must not be demoted to plain Major.
        // Margin guard (≤ 0.35) keeps the gate narrow; all corpus targets have margin ≤ 0.30.
        // Diatonic check prevents spurious fires on chromatic passing augmented chords.
        if (originalWinnerQuality == ChordQuality::Augmented
            && winnerBassIsRoot
            && results.size() >= 2
            && gateCtx.keyTonicPc >= 0
            && !hasExtension(winner.identity.extensions, Extension::MinorSeventh)
            && !hasExtension(winner.identity.extensions, Extension::MajorSeventh)) {
            for (size_t iIdx = 1; iIdx < results.size(); ++iIdx) {
                const ChordAnalysisResult& inv = results[iIdx];
                if (inv.identity.quality != ChordQuality::Major)                        continue;  // not Major
                if (inv.identity.rootPc != winner.identity.rootPc)                      continue;  // different root
                if (inv.identity.bassPc != winner.identity.bassPc)                      continue;  // not root-position
                const int invInterval = (inv.identity.rootPc - gateCtx.keyTonicPc + 12) % 12;
                bool invRootIsDiatonic = false;
                for (int d = 0; d < 7; ++d) {
                    if (gateCtx.scale[d] == invInterval) { invRootIsDiatonic = true; break; }
                }
                if (!invRootIsDiatonic)                                                 continue;  // not diatonic
                if (winner.identity.score - inv.identity.score > 0.35f)                continue;  // margin too wide
                std::swap(results[0], results[iIdx]);
                break;
            }
        }

        // ── Gate J: prefer inverted dominant-7th over root-position diminished triad ──────
        //
        // A root-position diminished TRIAD whose would-be dominant root (a major third
        // below the dim root) is also sounding is, by construction, the 3rd/5th/7th of
        // that dominant seventh — i.e. an inverted V7, not a root-position vii°.  The
        // four pcs {R-4, R, R+3, R+6} are exactly a dominant seventh rooted at R-4
        // (root, M3, P5, m7).  Promote the dominant reading.
        //   E.g. {C#,E,F#,A#} bass A#:  A#° (vii° of Bm) → F#7/A# (V6/5).
        // A genuine standalone vii° / vii°7 never voices the dominant root, so the
        // present-root guard means this cannot misfire on real leading-tone chords.
        // No diatonic guard — a secondary dominant (V7/x) is just as validly completed.
        if (originalWinnerQuality == ChordQuality::Diminished
            && results.size() >= 2) {
            const ChordAnalysisResult& dimWinner = results[0];
            if (dimWinner.identity.quality == ChordQuality::Diminished
                && dimWinner.identity.rootPc == dimWinner.identity.bassPc            // root position
                && !hasExtension(dimWinner.identity.extensions, Extension::DiminishedSeventh)) {
                const int domRootPc = (dimWinner.identity.rootPc - 4 + 12) % 12;     // major 3rd below
                if (gateCtx.pcWeight[static_cast<size_t>(domRootPc)] > prefs.extensionThreshold) {
                    for (size_t iIdx = 1; iIdx < results.size(); ++iIdx) {
                        const ChordAnalysisResult& dom = results[iIdx];
                        if (dom.identity.rootPc != domRootPc)                          continue;  // not the V7 root
                        if (dom.identity.quality != ChordQuality::Major)              continue;  // dom7 is Major+m7
                        if (!hasExtension(dom.identity.extensions, Extension::MinorSeventh)) {
                            continue;  // must carry the dominant seventh
                        }
                        std::swap(results[0], results[iIdx]);
                        break;
                    }
                }
            }
        }

    }
}

std::vector<ChordAnalysisResult> RuleBasedChordAnalyzer::analyzeChord(
    const std::vector<ChordAnalysisTone>& tones,
    int keySignatureFifths,
    KeySigMode keyMode,
    const ChordTemporalContext* context,
    const ChordAnalyzerPreferences& prefs,
    PostScoringGateContext* gateCtxOut) const
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

    // Iter 92 — bass candidate enumeration (joint scoring).
    //
    // Pre-Iter 92 the analyzer committed to a single bass (the lowest qualifying
    // pitch) before the chord scorer ran.  This caused two coupled bugs:
    //   Bug 1 (bwv103.6 m3 b2): a passing eighth note that happens to be the
    //     absolute lowest pitch in the region won bass selection over a
    //     beat-onset bass a step above it.
    //   Bug 2 (bwv310 m8 b3): a slash-chord reading (Em/C) outscored the
    //     root-position triad (C major) because the bass-root bonus + complete-
    //     triad evidence on C had no way to flip the global ranking.
    //
    // Both bugs are fixed by enumerating multiple bass candidates and scoring
    // each against the full 12 × 16 template grid, then picking the global
    // best (rootPc, templateIdx, bassPc) triple.
    //
    // Joint scoring is gated on the input coming from regional accumulation —
    // any tone with onsetAtRegionStart=true OR distinctMetricPositions>0 (both
    // are populated by collectRegionTones but not by the single-tick buildTones
    // path used by status-bar analysis and unit tests).  Synthetic single-tick
    // inputs fall back to the legacy single-bass selection (the absolute lowest
    // qualifying pitch) so that scoring-rule unit tests remain valid.
    const double bassMinWeight = prefs.bassPassingToneMinWeightFraction * totalRawWeight;

    // Joint scoring is enabled when the input came from regional accumulation
    // (collectRegionTones).  buildTones / status-bar inputs default to false
    // and fall back to legacy single-bass scoring.
    bool jointScoringEnabled = false;
    for (const ChordAnalysisTone& t : tones) {
        if (t.onsetAtRegionStart || t.distinctMetricPositions > 0) {
            jointScoringEnabled = true;
            break;
        }
    }
    if (prefs.captureScoringSnapshot) {
        prefs.captureScoringSnapshot->jointScoringEnabled = jointScoringEnabled;
    }

    struct BassCandidate {
        int pitch = std::numeric_limits<int>::max();
        int pc = -1;
        int tpc = -1;
        bool onsetAtRegionStart = false;
    };
    std::vector<BassCandidate> bassCandidates;
    if (jointScoringEnabled) {
        // Scan tones in the bass register (lowest pitch + one octave) for
        // multi-bass enumeration candidates.  The actual enumeration only
        // fires when there is musical evidence that the bass voice moves
        // within the region — at least one candidate with onsetAtRegionStart
        // = true AND at least one with onsetAtRegionStart = false.  This
        // distinguishes the bwv103.6 m3 b2 scenario (bass voice has G at
        // start, F# mid-region) from a static SATB / Jazz voicing where the
        // bass and upper voices all attack at the region start (one bass
        // candidate, no enumeration).
        const int bassRegisterCutoff = (lowestPitch != std::numeric_limits<int>::max())
                                       ? lowestPitch + 12
                                       : std::numeric_limits<int>::max();
        std::array<int, 12> bestPitchPerPc;
        std::array<int, 12> tpcPerPc;
        std::array<bool, 12> onsetPerPc;
        bestPitchPerPc.fill(std::numeric_limits<int>::max());
        tpcPerPc.fill(-1);
        onsetPerPc.fill(false);
        for (const ChordAnalysisTone& t : tones) {
            if (t.pitch > bassRegisterCutoff) { continue; }
            if (t.weight < bassMinWeight)      { continue; }
            const int pc = normalizePc(t.pitch);
            const size_t pcIdx = static_cast<size_t>(pc);
            if (t.pitch < bestPitchPerPc[pcIdx]) {
                bestPitchPerPc[pcIdx] = t.pitch;
                tpcPerPc[pcIdx]       = t.tpc;
            }
            if (t.onsetAtRegionStart) {
                onsetPerPc[pcIdx] = true;
            }
        }
        std::vector<BassCandidate> regionalCandidates;
        for (int pc = 0; pc < 12; ++pc) {
            const size_t pcIdx = static_cast<size_t>(pc);
            if (bestPitchPerPc[pcIdx] != std::numeric_limits<int>::max()) {
                regionalCandidates.push_back({ bestPitchPerPc[pcIdx], pc,
                                               tpcPerPc[pcIdx], onsetPerPc[pcIdx] });
            }
        }
        std::sort(regionalCandidates.begin(), regionalCandidates.end(),
                  [](const BassCandidate& a, const BassCandidate& b) { return a.pitch < b.pitch; });
        bool hasOnsetTrue  = false;
        bool hasOnsetFalse = false;
        for (const auto& rc : regionalCandidates) {
            if (rc.onsetAtRegionStart) { hasOnsetTrue = true; }
            else                       { hasOnsetFalse = true; }
        }
        // Sparse upper-register fallback: when the bass continuo rests (no
        // sounding note below middle C) and the region is reduced to two
        // upper-voice pitches, the "lowest sounding pitch" picked by the
        // legacy single-bass fallback is just the lower of two melodic notes,
        // not a structural bass. Enumerate so the root-position reading can
        // compete with the accidental inversion implied by literal-bass
        // selection. Corelli op01n08d m2 b3: G5 + B4 should score as V (G
        // root-position) per DCML, not V6/B. Gated on lowestPitch > 60 so
        // genuine bass voicings (D3, E2, …) keep their single-bass path.
        int distinctPcCount = 0;
        for (double w : pcWeight) {
            if (w > 0.05) { ++distinctPcCount; }
        }
        const bool sparseUpperRegisterAmbiguous =
            distinctPcCount <= 2
            && regionalCandidates.size() >= 2
            && lowestPitch > 60;
        if ((hasOnsetTrue && hasOnsetFalse) || sparseUpperRegisterAmbiguous) {
            bassCandidates = std::move(regionalCandidates);
            if (bassCandidates.size() > 4) {
                bassCandidates.resize(4);
            }
        }
    }
    // Legacy single-bass fallback (used when joint enumeration declines to fire
    // or when the weight filter eliminated every candidate).
    if (bassCandidates.empty() && lowestPitch != std::numeric_limits<int>::max()) {
        int lowestQualifyingPitch = std::numeric_limits<int>::max();
        for (const ChordAnalysisTone& t : tones) {
            if (t.weight >= bassMinWeight && t.pitch < lowestQualifyingPitch) {
                lowestQualifyingPitch = t.pitch;
            }
        }
        const int chosenPitch = (lowestQualifyingPitch < std::numeric_limits<int>::max())
                                ? lowestQualifyingPitch : lowestPitch;
        int chosenTpc = -1;
        bool chosenOnsetAtStart = false;
        for (const ChordAnalysisTone& t : tones) {
            if (t.pitch == chosenPitch) {
                if (t.tpc >= 0) { chosenTpc = t.tpc; }
                if (t.onsetAtRegionStart) { chosenOnsetAtStart = true; }
            }
        }
        bassCandidates.push_back({ chosenPitch, normalizePc(chosenPitch),
                                   chosenTpc, chosenOnsetAtStart });
    }

    // Working bass: defaults to the lowest candidate.  Re-assigned to the winning
    // bass after joint enumeration runs (see scoring loop below).  Downstream
    // result-building, post-ranking inversion correction and pedal detection all
    // consume these as the chosen bass.
    int bassPc  = bassCandidates.empty() ? 0  : bassCandidates.front().pc;
    int bassTpc = bassCandidates.empty() ? -1 : bassCandidates.front().tpc;

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

    // Count distinct pitch classes; require at least prefs.minDistinctPcsForCandidate
    // (default 3) for meaningful analysis. Greedy-expand callers relax this to 1 so
    // sparse 1–2 PC entries can be scored, then apply a PC-count-adaptive threshold
    // at the comparison site.
    int distinctPcs = 0;
    for (double w : pcWeight) {
        if (w > 0.05) {
            ++distinctPcs;
        }
    }
    if (distinctPcs < prefs.minDistinctPcsForCandidate) {
        return {};
    }

    // Structural-bass heuristic: when the lowest sounding pitch sits above
    // middle C (MIDI 60) and the region is sparse (≤ 2 distinct PCs), the
    // "bass" picked from the literal lowest pitch is just the lower of two
    // upper-voice notes — there is no continuo / bass-voice support behind
    // it. Inversion contextual bonuses (stepwise / lookahead / same-root) assume
    // a structural bass; firing them on accidental upper-voice "inversions"
    // promotes spurious slash readings over root-position chords whose
    // function is implied (Corelli op01n08d m2 b3: G + B with bass continuo
    // resting should score as V root-position per DCML, not V6 / G/B).
    // distinctPcs ≥ 3 retains the bonus because denser regions carry their
    // own structural cues; dense static SATB textures with bass in tenor
    // register remain unchanged.
    const bool hasStructuralBass = (lowestPitch <= 60) || (distinctPcs >= 3);

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
    //
    // 17 templates: see docs/scoring_model.md §2 for the full list.
    // When adding a template: update BOTH TemplateDef arrays (this one AND
    // kDiagTemplates in diagnoseChord ~L3381) AND all three score matrices
    // (basisIndepMatrix, complexityFactorMatrix, augFactorMatrix — ~L2014–L2016)
    // atomically.  Missing the score matrices causes a silent stack-buffer
    // overrun (caught in B1 attempt 2026-06-04 — no compile error, just garbage
    // cells).
    static const std::array<TemplateDef, 17> templates = {{
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
        { ChordQuality::Augmented,      { 0, 4, 8, 10 },    { 0, +4, +8, -2 }   },  // aug7 (C7♯5)
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
    //
    // RawCandidate is declared at namespace scope (chordanalyzer.h) so it can be
    // used by buildChordResult() and applyPostScoringGates().

    // Iter 92 — joint (bass, chord) scoring.
    //
    // For each (rootPc, templateIdx) compute the bass-INDEPENDENT base once.
    // For each enumerated bass candidate, add the bass-DEPENDENT delta plus
    // the JOINT terms (w_complete in Step 3a, w_onset / w_passing in 3b,
    // w_stepIn / w_stepOut in 3c), build full rawCandidates, and track the
    // global best (rootPc, templateIdx, bassPc) triple.  The winning bass
    // becomes the working bass for downstream result-building, post-ranking
    // inversion correction and pedal detection.
    // The three score matrices below must stay in sync with the TemplateDef
    // arrays above (same column count, currently 17).  Stack-buffer overrun
    // if mismatched — silent at compile time.  See docs/scoring_model.md §3.
    std::array<std::array<double, 17>, 12> basisIndepMatrix{};
    std::array<std::array<double, 17>, 12> complexityFactorMatrix{};
    std::array<std::array<double, 17>, 12> augFactorMatrix{};
    for (int rootPc = 0; rootPc < 12; ++rootPc) {
        for (size_t tplIdx = 0; tplIdx < templates.size(); ++tplIdx) {
            const TemplateDef& tpl = templates[tplIdx];

            // B2 guard: the 4-tone Augmented (aug7) template requires BOTH the major
            // third (rootPc+4) AND the augmented fifth (rootPc+8) to be present above
            // extensionThreshold.  The `||` (skip if EITHER is absent) means BOTH
            // must be present for the template to score.
            //
            // M3-only relaxation has been tried and reverted (2026-06-05).  Using
            // `&&` instead of `||` lets the aug7 template over-fire on complete
            // major triads containing a minor seventh: with only root+M3+m7 present,
            // the large aug5 score offset (+8) still inflates the partial-match
            // score above a complete major triad.  Schumann D-major and Corelli
            // G-major snapshots flipped to aug7 under the relaxed guard.  The dual
            // `||` is load-bearing — see docs/scoring_model.md §4.
            if (tpl.quality == ChordQuality::Augmented
                && tpl.intervals.size() == 4
                && (pcWeight[static_cast<size_t>((rootPc + 4) % 12)] <= prefs.extensionThreshold
                    || pcWeight[static_cast<size_t>((rootPc + 8) % 12)] <= prefs.extensionThreshold)) {
                continue;
            }

            // dim7CharacteristicBonus is a ROTATION-SELECTION MECHANISM — not just a
            // score offset.  All four enharmonic rotations of a dim7 chord share the
            // same PC set (C°7 = Eb°7 = Gb°7 = A°7).  The non-diatonic check on the
            // bb7 PC inside the helper asymmetrically rewards the correct enharmonic
            // root: the bb7 of the "true" rotation is non-diatonic in the current key,
            // while the bb7 of the three spurious rotations is diatonic (coincides
            // with a scale tone) and gets no bonus.
            // DO NOT suppress or bypass this bonus without replacing this rotation-
            // selection function.  Suppressing it breaks 6 Jazz catalog dim7 entries
            // (B3 attempt 2026-06-05).  See docs/scoring_model.md §4.
            basisIndepMatrix[rootPc][tplIdx] =
                scoreTemplateTones(tpl, rootPc, pcWeight)
                + scoreExtraNotes(tpl, rootPc, pcWeight, tpcForPc)
                + dim7CharacteristicBonus(tpl, rootPc, pcWeight, keyTonicPc, scale, prefs.extensionThreshold)
                + structuralPenalties(tpl, rootPc, pcWeight, tpcForPc, distinctPcs, prefs.extensionThreshold)
                + tpcConsistencyBonus(tpl, rootPc, tpcForPc, prefs)
                + bassIndependentContextualBonuses(tpl, rootPc, keyTonicPc, scale, prefs, context);

            // Iter 74 Fix A — template complexity preference (bass-independent).
            const int templateDefinedTones = static_cast<int>(tpl.intervals.size());
            const double evidenceRatio
                = (distinctPcs >= templateDefinedTones)
                ? 1.0
                : static_cast<double>(distinctPcs) / templateDefinedTones;
            complexityFactorMatrix[rootPc][tplIdx]
                = (evidenceRatio >= 0.5) ? 1.0 : (0.5 + evidenceRatio);

            // Iter 78 Fix C + Iter 79 — augmented bare-root / thin-evidence
            // penalties (both bass-independent).
            double augFactor = 1.0;
            if (tpl.quality == ChordQuality::Augmented
                && distinctPcs <= 2
                && pcWeight[static_cast<size_t>(rootPc)] <= prefs.extensionThreshold) {
                augFactor *= 0.5;
            }
            if (tpl.quality == ChordQuality::Augmented) {
                const double thirdW = pcWeight[static_cast<size_t>((rootPc + 4) % 12)];
                const double fifthW = pcWeight[static_cast<size_t>((rootPc + 8) % 12)];
                const double min7W  = pcWeight[static_cast<size_t>((rootPc + 10) % 12)];
                const double maj7W  = pcWeight[static_cast<size_t>((rootPc + 11) % 12)];
                if (thirdW <= prefs.extensionThreshold
                    && fifthW <= prefs.extensionThreshold
                    && min7W <= prefs.extensionThreshold
                    && maj7W <= prefs.extensionThreshold) {
                    augFactor *= 0.5;
                }
            }
            augFactorMatrix[rootPc][tplIdx] = augFactor;
        }
    }

    // Iter 92 Step 3a — w_complete.
    //
    // When the candidate root equals the bass, all three triad tones are
    // present above extensionThreshold, and the region has exactly 3 distinct
    // pitch classes, promote the root-position triad by w_complete.  This
    // unblocks the Em/C → C major flip (bwv310 m8 b3, Bug 2) without
    // promoting slash-chord candidates that are missing a triad tone (the
    // Iter 90 regression mode).  Gated on jointScoringEnabled so single-tick
    // (status-bar / unit test) inputs preserve their pre-Iter-92 scores.
    static constexpr double kWComplete = 0.50;
    auto wCompleteBonus = [&](const TemplateDef& tpl, int rootPc, int candBassPc) -> double {
        if (!jointScoringEnabled || candBassPc != rootPc || distinctPcs != 3) {
            return 0.0;
        }
        const double thr = prefs.extensionThreshold;
        int thirdInterval = -1;
        int fifthInterval = -1;
        switch (tpl.quality) {
        case ChordQuality::Major:      thirdInterval = 4; fifthInterval = 7; break;
        case ChordQuality::Minor:      thirdInterval = 3; fifthInterval = 7; break;
        case ChordQuality::Diminished: thirdInterval = 3; fifthInterval = 6; break;
        case ChordQuality::Augmented:  thirdInterval = 4; fifthInterval = 8; break;
        default:                       return 0.0;  // gate only fires for plain triads
        }
        const double rootW  = pcWeight[static_cast<size_t>(rootPc)];
        const double thirdW = pcWeight[static_cast<size_t>((rootPc + thirdInterval) % 12)];
        const double fifthW = pcWeight[static_cast<size_t>((rootPc + fifthInterval) % 12)];
        // "Present" = above the distinctPcs gate (0.05), matching how the rest
        // of the analyzer defines a sounding tone.  This avoids the floating-
        // point boundary at exactly extensionThreshold (bwv310 m8 b3 has C and
        // G with pcWeight that prints as 0.200 but rounds slightly below in
        // double).  Iter-90's regression mode (slash chord with missing fifth)
        // is still excluded — an absent tone gives pcWeight = 0.  `thr` is
        // accepted into the API for a future tightening pass.
        (void)thr;
        constexpr double kPresenceThreshold = 0.05;
        const bool allTriadPresent = (rootW > kPresenceThreshold)
                                  && (thirdW > kPresenceThreshold)
                                  && (fifthW > kPresenceThreshold);
        return allTriadPresent ? kWComplete : 0.0;
    };

    // Iter 92 Step 3b — w_onset / w_passing (NOT enabled in this iteration).
    //
    // Design: bias bass-candidate selection toward tones that attack at the
    // region's startTick (beat-onset bass: +0.15) and away from tones that
    // attack mid-region (passing-tone bass: -0.10).  Closes Bug 1 conceptually.
    //
    // Disabled because applying the bonus at SUB-region scope (which is the
    // only granularity batch_analyze currently calls analyzeChord at) produces
    // BIR=false regressions in both Baroque (+6) and Jazz (+3): sub-regions
    // boundaries align with note onsets, so every tone tends to be
    // "onsetAtRegionStart=true" at some sub-region.  The post-merge
    // analyzeChord re-invocation needed to apply this signal at full-region
    // scope is out of scope for Iter 92 and is queued as Iter 93.

    // Iter 94 — w_stepIn / w_stepOut.
    //
    // Reward bass candidates that participate in semitone / whole-tone motion
    // from the previous region's bass (stepIn) and/or to the next region's
    // bass (stepOut).  The previous/next bass PCs are supplied by the bridge
    // and batch_analyze callers at FULL-REGION scope — for sub-region
    // analyzeChord calls these are overridden to the parent's predecessor /
    // successor bass PCs so the bonus reflects structural voice-leading rather
    // than within-parent micromotion (which caused the Iter 92 Step 3c +5
    // Baroque BIR=false regression).  Gated on jointScoringEnabled so the
    // single-tick (status-bar / unit test) path is untouched, and on
    // !prefs.explorationMode so greedyExpandSegmentation's internal boundary-
    // search analyzeChord calls do not let the step bonus redirect segmentation
    // before the final per-region scoring pass runs.
    //
    // Additionally restricted to root-position candidates (candBassPc ==
    // rootPc): the bonus is meant to reward "this chord's root moves smoothly
    // in the bass line," not "this slash-chord's bass happens to step
    // smoothly."  Without this guard, a slash-chord bass (e.g. F# in G#m7/F#)
    // that steps to a neighbouring bass gets credit even though its root (G#)
    // is not the moving voice — caused the Iter 94 Jazz bwv430 regression
    // (BIR=false 14→15).
    static constexpr double kWStepIn  = 0.10;
    static constexpr double kWStepOut = 0.10;
    auto isSemitoneOrToneStep = [](int interval) {
        return interval == 1 || interval == 2 || interval == 10 || interval == 11;
    };
    // explorationMode is set true by greedyExpandSegmentation for internal
    // boundary-exploration calls (Round 1 head/tail synthesis + Round 2 region
    // scoring in harmonicsegmenter.cpp::fillGap).  Bonuses that depend on
    // neighbouring context (step motion, sequence, leading-tone dim7) must be
    // suppressed in these calls — otherwise they bias sub-region bass selection
    // DURING segmentation, before the final per-region scoring pass runs.
    // Iter 94 caught this as a regression while developing the step bonuses.
    // The lambdas below (wStepInBonus, wStepOutBonus, wSeqBonus, wDimBonus)
    // all share this gate.  See docs/scoring_model.md §4 — "explorationMode".
    auto wStepInBonus = [&](int candBassPc, int rootPc) -> double {
        if (!jointScoringEnabled || prefs.explorationMode || context == nullptr) return 0.0;
        if (candBassPc != rootPc) return 0.0;
        const int prev = context->previousBassPc;
        if (prev < 0 || prev == candBassPc) return 0.0;
        const int delta = ((candBassPc - prev) % 12 + 12) % 12;
        return isSemitoneOrToneStep(delta) ? kWStepIn : 0.0;
    };
    auto wStepOutBonus = [&](int candBassPc, int rootPc) -> double {
        if (!jointScoringEnabled || prefs.explorationMode || context == nullptr) return 0.0;
        if (candBassPc != rootPc) return 0.0;
        const int next = context->nextBassPc;
        if (next < 0 || next == candBassPc) return 0.0;
        const int delta = ((next - candBassPc) % 12 + 12) % 12;
        return isSemitoneOrToneStep(delta) ? kWStepOut : 0.0;
    };

    // Iter 95 Step 1 — w_seq.
    //
    // Reward a candidate whose root is a perfect fourth below the next region's
    // root (equivalently: descending-fifth root motion into the successor —
    // ((nextRootPc - candRootPc) mod 12) == 5 means the successor sits a P4
    // above us, i.e. classic V→I).  Unlike w_stepIn / w_stepOut this is a
    // CHORD-LEVEL signal: any inversion of the candidate qualifies (the bonus
    // does NOT require candBassPc == candRootPc), and it is NOT subject to the
    // first-inversion-m7-family surgical guard — sequential root motion is
    // about the root identity, not the bass.
    //
    // Same gating as the step bonuses: jointScoringEnabled and
    // !prefs.explorationMode keep the single-tick / segmentation-internal
    // paths untouched.  Requires context->nextRootPc >= 0 (populated by the
    // bridge / batch_analyze look-ahead).
    auto wSeqBonus = [&](int candRootPc) -> double {
        if (prefs.suppressProgressionSignals) return 0.0;
        return fn::wSeqBonus(candRootPc,
                             context ? context->nextRootPc : -1,
                             distinctPcs,
                             jointScoringEnabled,
                             prefs.explorationMode);
    };

    // Iter 96 — w_dim: diminished/half-dim leading-tone resolution tiebreaker.
    // When a Diminished or HalfDiminished candidate's root sits one semitone
    // below the next region's root (i.e. it IS the leading tone of the next
    // chord, e.g. vii°7 → I), apply a small bonus.  Diminished sevenths are
    // fully symmetric — all four rotations produce identical pc-sets — so
    // without a context tiebreaker the analyzer's choice of rotation is
    // essentially arbitrary; the leading-tone-of-next-root resolution is the
    // canonical Western tonal signal that selects the correct spelling.
    // Same gating as w_seq.  Reuses context->nextRootPc plumbing (Iter 95
    // Steps 1 & 2 — populated on both batch and bridge paths).
    auto wDimBonus = [&](int candRootPc, ChordQuality quality) -> double {
        if (prefs.suppressProgressionSignals) return 0.0;
        return fn::wDimBonus(candRootPc, quality,
                             context ? context->nextRootPc : -1,
                             distinctPcs,
                             jointScoringEnabled,
                             prefs.explorationMode);
    };

    // Build per-bass-candidate rawCandidates; pick the global winner.
    //
    // Two-pass per candBassPc:
    //   Pass A — compute the unbonused score (template + bass-dependent deltas
    //            + w_complete) for every (rootPc, tplIdx); push into perBass.
    //   Pass B — for each root-position candidate eligible for w_stepIn/w_stepOut,
    //            apply the SURGICAL GUARD: suppress both step bonuses if any
    //            competitor in perBass with quality in {HalfDiminished,
    //            Diminished, Minor7} sits a minor third below our bass
    //            (competitor.rootPc == (candBassPc - 3) mod 12) AND scores
    //            within (kWStepIn + kWStepOut + 0.01) of the candidate's
    //            unbonused score.  The canonical case is Dm6 vs Bø7/D:
    //            candBassPc=2 (D), competitor.rootPc=11 (B) — competitor's
    //            root sits a minor third below our bass candidate, not at
    //            our bass.  Otherwise the step bonus would tip a fragile
    //            m6 root-position reading over an equally viable
    //            first-inversion m7-family reading on identical pitch evidence.

    // E2b — pre-allocate snapshot cubes to avoid repeated reallocations.
    if (prefs.captureScoringSnapshot) {
        const int nCells = static_cast<int>(bassCandidates.size()) * 12 * static_cast<int>(templates.size());
        prefs.captureScoringSnapshot->cellsWithWDim.clear();
        prefs.captureScoringSnapshot->cellsWithoutWDim.clear();
        prefs.captureScoringSnapshot->cellsWithWDim.reserve(nCells);
        prefs.captureScoringSnapshot->cellsWithoutWDim.reserve(nCells);
    }

    std::vector<RawCandidate> rawCandidates;
    rawCandidates.reserve(12 * templates.size());
    {
        // Iter 97a-v3 — post-bonus quality guard for w_dim.
        //
        // Invariant: wDimBonus should only change which Dim chord wins, never
        // change what quality the winner is.  If after applying the bonus the
        // global winner is not Dim/HalfDim, the bonus has caused cross-bass
        // contamination (a Dim triple under bass B1 boosted enough that B1
        // wins the global bass, but B1's own best candidate is Minor) and must
        // be suppressed.  Prior alpha attempts that guarded on the pre-bonus
        // global leader missed this case because the contamination is observable
        // only at the post-bonus winner level.
        //
        // Implementation: maintain TWO parallel global trackings across the bass
        // loop — one with wDim included in cand.score, one without.  After the
        // loop, inspect the with-wDim global winner's quality.  If it is Dim or
        // HalfDim, accept the with-wDim result; otherwise fall back to the
        // without-wDim result.  Pass B (step bonus + surgical m7-family guard)
        // is applied independently to both score variants — wDim can lift a
        // Dim/HalfDim competitor into the kStepBudget blocking band, so the
        // without-wDim variant must run Pass B over its own scores to be a true
        // reflection of "what we'd get if wDim never fired".
        double globalBestScoreWith = -std::numeric_limits<double>::infinity();
        double globalBestScoreWithout = -std::numeric_limits<double>::infinity();
        std::vector<RawCandidate> bestPerBassWith;
        std::vector<RawCandidate> bestPerBassWithout;
        size_t winnerIdxWith = 0;
        size_t winnerIdxWithout = 0;
        constexpr double kStepBudget = kWStepIn + kWStepOut + 0.01;

        // Pass B factored as a lambda so it can run independently against the
        // with-wDim and without-wDim per-bass arrays.
        auto applyStepBonusGuard = [&](std::vector<RawCandidate>& perBass, int candBassPc) {
            const int compRootPc = ((candBassPc - 3) % 12 + 12) % 12;
            for (auto& cand : perBass) {
                if (cand.rootPc != candBassPc) {
                    continue;  // step bonus is root-position-only (lambda also enforces)
                }
                if (cand.quality == ChordQuality::Power) {
                    continue;
                }
                const double stepIn  = wStepInBonus(candBassPc, cand.rootPc);
                const double stepOut = wStepOutBonus(candBassPc, cand.rootPc);
                if (stepIn == 0.0 && stepOut == 0.0) {
                    continue;
                }

                bool blocked = false;
                for (const auto& other : perBass) {
                    if (other.rootPc != compRootPc) {
                        continue;
                    }
                    const TemplateDef& otherTpl = templates[static_cast<size_t>(other.tiePriority)];
                    const bool isMin7 = (other.quality == ChordQuality::Minor)
                                        && (otherTpl.intervals.size() == 4);
                    const bool relevantQuality = (other.quality == ChordQuality::HalfDiminished)
                                                 || (other.quality == ChordQuality::Diminished)
                                                 || isMin7;
                    if (!relevantQuality) {
                        continue;
                    }
                    if (other.score >= cand.score - kStepBudget) {
                        blocked = true;
                        break;
                    }
                }
                if (!blocked) {
                    cand.score += stepIn + stepOut;
                }
            }
        };

        for (size_t bi = 0; bi < bassCandidates.size(); ++bi) {
            const int candBassPc = bassCandidates[bi].pc;
            std::vector<RawCandidate> perBassWith;
            std::vector<RawCandidate> perBassWithout;
            perBassWith.reserve(12 * templates.size());
            perBassWithout.reserve(12 * templates.size());

            // Pass A — build two parallel score variants. The with-wDim variant
            // is the iteration's candidate post-bonus reading; the without-wDim
            // variant is the pre-bonus fallback the post-bonus quality guard
            // restores to when the bonus's post-bonus winner is not Dim/HalfDim.
            for (int rootPc = 0; rootPc < 12; ++rootPc) {
                for (size_t tplIdx = 0; tplIdx < templates.size(); ++tplIdx) {
                    const TemplateDef& tpl = templates[tplIdx];
                    const double bassBonus = appliedBassRootBonus(tpl, rootPc, candBassPc, pcWeight, prefs);
                    const double basisDep =
                        nonBassAdjustment(tpl, rootPc, candBassPc, tpcForPc)
                        + bassDependentContextualBonuses(tpl, rootPc, candBassPc, bassBonus,
                                                         distinctPcs, pcWeight, prefs, context,
                                                         hasStructuralBass);
                    double scoreNoWDim = basisIndepMatrix[rootPc][tplIdx] + basisDep;
                    scoreNoWDim *= complexityFactorMatrix[rootPc][tplIdx];
                    scoreNoWDim *= augFactorMatrix[rootPc][tplIdx];
                    const double wCompleteBonusVal = wCompleteBonus(tpl, rootPc, candBassPc);
                    const double wSeqBonusVal      = wSeqBonus(rootPc);
                    scoreNoWDim += wCompleteBonusVal;
                    scoreNoWDim += wSeqBonusVal;

                    const double wDimDelta = wDimBonus(rootPc, tpl.quality);
                    const double scoreWith = scoreNoWDim + wDimDelta;

                    if (prefs.captureScoringSnapshot) {
                        fn::ScoringCell cell;
                        cell.bassPc           = candBassPc;
                        cell.bassTpc          = bassCandidates[bi].tpc;
                        cell.rootPc           = rootPc;
                        cell.tiePriority      = static_cast<int>(tplIdx);
                        cell.quality          = tpl.quality;
                        cell.intervalCount    = static_cast<int>(tpl.intervals.size());
                        cell.basisIndep       = basisIndepMatrix[rootPc][tplIdx];
                        cell.basisDep         = basisDep;
                        cell.complexityFactor = complexityFactorMatrix[rootPc][tplIdx];
                        cell.augFactor        = augFactorMatrix[rootPc][tplIdx];
                        cell.wCompleteBonus   = wCompleteBonusVal;
                        cell.wSeqBonus        = wSeqBonusVal;
                        cell.appliedBassBonus = bassBonus;

                        // Without-wDim cell: wDimDelta is always 0.
                        cell.wDimDelta = 0.0;
                        prefs.captureScoringSnapshot->cellsWithoutWDim.push_back(cell);

                        // With-wDim cell: same except wDimDelta.
                        cell.wDimDelta = wDimDelta;
                        prefs.captureScoringSnapshot->cellsWithWDim.push_back(cell);
                    }

                    perBassWith.push_back({ scoreWith, bassBonus, rootPc, tpl.quality,
                                            static_cast<int>(tplIdx), wDimDelta });
                    perBassWithout.push_back({ scoreNoWDim, bassBonus, rootPc, tpl.quality,
                                               static_cast<int>(tplIdx), 0.0 });
                }
            }

            // Pass B — step bonus with surgical first-inversion-m7-family guard.
            // Power-quality candidates are excluded outright: a root+fifth-only
            // template gaining +0.20 from stepwise bass motion will tip past a
            // viable triad reading in sparse Jazz tonic-on-strong-beat contexts
            // (5 of the 6 corrected-guard Jazz BIR=true regressions were
            // `[Tonic]5` Power reads vs WiR `I`/`i` triads — bwv20.7 m16b1,
            // bwv227.1 m11b3, bwv245.40 m27b3, bwv384 m4b3, bwv422 m14b1).
            applyStepBonusGuard(perBassWith, candBassPc);
            applyStepBonusGuard(perBassWithout, candBassPc);

            // Pass C — compute localBest from final scores for each variant.
            double localBestWith = -std::numeric_limits<double>::infinity();
            for (const auto& c : perBassWith) {
                if (c.score > localBestWith) {
                    localBestWith = c.score;
                }
            }
            double localBestWithout = -std::numeric_limits<double>::infinity();
            for (const auto& c : perBassWithout) {
                if (c.score > localBestWithout) {
                    localBestWithout = c.score;
                }
            }
            if (localBestWith > globalBestScoreWith) {
                globalBestScoreWith = localBestWith;
                bestPerBassWith = std::move(perBassWith);
                winnerIdxWith = bi;
            }
            if (localBestWithout > globalBestScoreWithout) {
                globalBestScoreWithout = localBestWithout;
                bestPerBassWithout = std::move(perBassWithout);
                winnerIdxWithout = bi;
            }
        }

        // Post-bonus quality guard: inspect the with-wDim global winner.  If it
        // is Diminished or HalfDiminished, the bonus did its intended job
        // (chose the correct rotation/spelling of a diminished chord); accept
        // the with-wDim result.  Otherwise the bonus caused cross-bass
        // contamination — discard the with-wDim result and fall back to the
        // without-wDim result.
        ChordQuality postBonusWinnerQuality = ChordQuality::Unknown;
        double postBonusBestScore = -std::numeric_limits<double>::infinity();
        for (const auto& c : bestPerBassWith) {
            if (c.score > postBonusBestScore) {
                postBonusBestScore = c.score;
                postBonusWinnerQuality = c.quality;
            }
        }
        const bool acceptPostBonus = (postBonusWinnerQuality == ChordQuality::Diminished
                                      || postBonusWinnerQuality == ChordQuality::HalfDiminished);

        const size_t winnerIdx = acceptPostBonus ? winnerIdxWith : winnerIdxWithout;
        rawCandidates = acceptPostBonus
                        ? std::move(bestPerBassWith)
                        : std::move(bestPerBassWithout);
        if (!bassCandidates.empty()) {
            bassPc  = bassCandidates[winnerIdx].pc;
            bassTpc = bassCandidates[winnerIdx].tpc;
        }

        if (prefs.captureScoringSnapshot) {
            prefs.captureScoringSnapshot->distinctPcs        = distinctPcs;
            prefs.captureScoringSnapshot->acceptedWithWDim   = acceptPostBonus;
            prefs.captureScoringSnapshot->chosenBassPc
                = bassCandidates.empty() ? -1 : bassCandidates[winnerIdx].pc;
            prefs.captureScoringSnapshot->winnerBassPcWith
                = bassCandidates.empty() ? -1 : bassCandidates[winnerIdxWith].pc;
            prefs.captureScoringSnapshot->winnerBassPcWithout
                = bassCandidates.empty() ? -1 : bassCandidates[winnerIdxWithout].pc;
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

    // De-inflate the threshold when the best-scoring candidate's lead comes from a
    // bass-root bonus.  A bass-inflated winner sets an artificially high bar that
    // can exclude its enharmonic non-bass alternative (e.g. Gm7 when Bb6 wins, or
    // the correct non-sus chord when a sus template wins from the bass note).
    // Using the de-bonused score as the threshold base ensures those alternatives
    // survive into results[] where the post-ranking inversion correction can
    // evaluate and flip them.
    // When the winner carries no bass bonus (winnerBassBonus == 0) this is
    // identical to the original formula.
    const double winnerBassBonus = rawCandidates.empty()
                                   ? 0.0
                                   : rawCandidates.front().appliedBassBonus;
    const double threshold = (bestRawScore - winnerBassBonus) * kScoreThresholdRatio;

    // ── Result builder ───────────────────────────────────────────────────────
    //
    // Wraps buildChordResult() (defined above at namespace scope) so call sites
    // inside analyzeChord can pass just the RawCandidate. The free function is
    // also used from applyPostScoringGates() for FM2 and G-E fallback paths.
    const auto buildResult = [&](const RawCandidate& rc) -> ChordAnalysisResult {
        return buildChordResult(rc,
            BuildChordResultContext{ pcWeight, tpcForPc, bassPc, bassTpc,
                                     keyTonicPc, keyMode, scale },
            prefs);
    };

    std::vector<ChordAnalysisResult> results;
    results.reserve(3);

    for (const RawCandidate& rc : rawCandidates) {
        if (!prefs.suppressProgressionSignals) {
            if (results.size() >= 3) {
                break;
            }
            if (rc.score < threshold) {
                break;
            }
        }
        results.push_back(buildResult(rc));
    }

    // ── Guaranteed inversion alternative ─────────────────────────────────────
    //
    // When the winner is a bass-root candidate (rootPc == bassPc), the results[]
    // cap of 3 is routinely exhausted by same-rootPc extensions/variants (e.g.
    // Bb, Bb7, BbMaj7) before the correct enharmonic alternative (e.g. Gm7) can
    // enter.  The post-ranking inversion correction requires a different-rootPc
    // Major/Minor candidate in results[] to function.
    //
    // If every entry in results[] shares the winner's rootPc, scan rawCandidates
    // for the highest-scoring different-rootPc candidate that clears the threshold
    // and append it.  The correction then has a target to evaluate and potentially
    // promote.
    //
    // This append only fires when:
    //   (a) the winner is a bass-root candidate (rootPc == bassPc), AND
    //   (b) no different-rootPc candidate already made it into results[].
    // It is a no-op for all other cases.
    if (!prefs.suppressProgressionSignals
        && !results.empty()
        && bassPc >= 0
        && prefs.inversionSuspicionMargin > 0.0
        && results.front().identity.rootPc == static_cast<int>(bassPc))
    {
        const int winnerRootPc = results.front().identity.rootPc;
        const bool hasDiffRoot = std::any_of(results.begin(), results.end(),
            [winnerRootPc](const ChordAnalysisResult& r) {
                return r.identity.rootPc != winnerRootPc;
            });

        if (!hasDiffRoot) {
            for (const RawCandidate& rc : rawCandidates) {
                if (rc.score < threshold)        { break; }
                if (rc.rootPc == winnerRootPc)   { continue; }

                results.push_back(buildResult(rc));
                break;
            }
        }
    }

    // Publish pre-gate state to the caller-supplied PostScoringGateContext, so
    // applyPostScoringGates() can run externally (in regionanalyzer.cpp and
    // bridge callers) after applyHarmonicFunction() has had a chance to alter
    // the winner.
    if (gateCtxOut) {
        gateCtxOut->pcWeight      = pcWeight;
        gateCtxOut->tpcForPc      = tpcForPc;
        gateCtxOut->scale         = scale;
        gateCtxOut->keyTonicPc    = keyTonicPc;
        gateCtxOut->keyMode       = keyMode;
        gateCtxOut->bassPc        = bassPc;
        gateCtxOut->bassTpc       = bassTpc;
        gateCtxOut->distinctPcs   = distinctPcs;
        gateCtxOut->threshold     = threshold;
        gateCtxOut->rawCandidates = rawCandidates;  // copy
        gateCtxOut->tones         = tones;          // for extracted pedal Pass-2
        gateCtxOut->keySigFifths  = keySignatureFifths;
    }

    // Gates A–L now run externally via applyPostScoringGates().
    // Production call sites (regionanalyzer.cpp, harmonicsegmenter.cpp, bridge
    // callers) invoke it after applyHarmonicFunction(); inferNextRootPc() and
    // the test helper analyzeWithGates() call it directly. Do NOT call it here —
    // that would revert the E3 extraction.

    // ── Iter 86 / Iter 91 / pedal tail — EXTRACTED (Phase 1, E2d-prereq) ──────
    //
    // The bass-b7 promotion (Iter 86), bass-as-root promotion (Iter 91) and
    // two-pass pedal-point detection used to run here, on results.front().  They
    // are now in the free function applyIter8691Pedal() (defined just below) and
    // run AFTER applyHarmonicFunction() at every production call site.  This lets
    // them stamp the function-layer-selected winner in suppression mode rather
    // than the suppressed-signal winner (the "Mode C reversion" E3 fixed for the
    // gates).  In non-suppression mode applyHarmonicFunction() is a no-op, so the
    // relocation is byte-identical to the old inline tail.

    return results;
}

// ── Iter 86 / Iter 91 / pedal-point tail (extracted from analyzeChord) ──────
//
// See the declaration in chordanalyzer.h for the rationale.  All inputs come from
// the PostScoringGateContext captured by analyzeChord(); the temporal context (for
// Iter 91's nextRootPc) is passed separately.  The pedal Pass-2 sub-analysis
// re-invokes analyzeChord() and then re-applies this same tail to its result —
// replicating the recursive behaviour the inline version had (the nested
// analyzeChord() previously ran its own Iter 86/91/pedal tail).
void applyIter8691Pedal(
    std::vector<ChordAnalysisResult>&  results,
    const PostScoringGateContext&      gateCtx,
    const ChordTemporalContext*        context,
    const ChordAnalyzerPreferences&    prefs)
{
    const int bassPc = gateCtx.bassPc;

    // Build a ChordAnalysisResult from a RawCandidate using the captured context
    // (mirrors the buildResult lambda in applyPostScoringGates / analyzeChord).
    const auto buildResult = [&](const RawCandidate& rc) -> ChordAnalysisResult {
        return buildChordResult(rc,
            BuildChordResultContext{ gateCtx.pcWeight, gateCtx.tpcForPc,
                                     gateCtx.bassPc, gateCtx.bassTpc,
                                     gateCtx.keyTonicPc, gateCtx.keyMode,
                                     gateCtx.scale },
            prefs);
    };

    // ── Iter 86 — bass-b7 promotion ──────────────────────────────────────────
    // If the winner is a Major or Minor triad whose bass is the b7 of the
    // root (interval 10) and that b7 is genuinely present in the score, stamp
    // the MinorSeventh extension so the chord symbol (Am7/G) and Roman numeral
    // (i65 / V42) match the literal slash-bass that the symbol formatter
    // already emits.  Also suppresses spurious pedal-point classification on
    // these cases — once MinorSeventh is stamped, isBassChordTone() treats
    // interval 10 as a chord tone and the pedal check below is skipped.
    if (!results.empty() && bassPc >= 0) {
        ChordAnalysisResult& winner = results.front();
        const ChordQuality q = winner.identity.quality;
        const int rPc        = winner.identity.rootPc;
        const bool bassIsB7  = (bassPc != rPc)
                               && ((bassPc - rPc + 12) % 12) == 10;
        const bool isPlainTriad = (q == ChordQuality::Major || q == ChordQuality::Minor)
                                  && !hasExtension(winner.identity.extensions, Extension::MinorSeventh)
                                  && !hasExtension(winner.identity.extensions, Extension::MajorSeventh);
        if (bassIsB7
            && isPlainTriad
            && gateCtx.pcWeight[static_cast<size_t>(bassPc)] > prefs.extensionThreshold) {
            setExtension(winner.identity.extensions, Extension::MinorSeventh);
        }
    }

    // ── Iter 91 — bass-as-root promotion (forward-context gated) ─────────────
    // When the winner is a Major/Minor plain-triad slash chord and the bass
    // sits a third (m3 or M3) above the root — Patterns A and B from the
    // iii/III ambiguity study (docs/iter90_bass_as_root_promotion_shelved.md):
    //   Pattern A: bassPc - rootPc ≡ 8 (mod 12), winner Minor — e.g. Em/C → C
    //   Pattern B: bassPc - rootPc ≡ 9 (mod 12), winner Major — e.g. C/A  → Am
    // promote the bass-rooted reading IF the following region's inferred
    // root equals the current bass (context->nextRootPc == bassPc).  That
    // forward resolution is the structural signal that the current bass is
    // the chord root, not the third of an iii/III triad.  previousRootPc was
    // deliberately omitted — it fired too broadly on genuine I → I6
    // progressions where the previous chord shares the iii/III root.
    if (!results.empty()
        && bassPc >= 0
        && context != nullptr
        && context->nextRootPc != -1
        && context->nextRootPc == bassPc) {
        ChordAnalysisResult& winner = results.front();
        const ChordQuality q = winner.identity.quality;
        const int rPc        = winner.identity.rootPc;
        const int delta      = (bassPc - rPc + 12) % 12;
        const bool patternA  = (delta == 8) && (q == ChordQuality::Minor);
        const bool patternB  = (delta == 9) && (q == ChordQuality::Major);
        const bool isPlainTriad = !hasExtension(winner.identity.extensions, Extension::MinorSeventh)
                                  && !hasExtension(winner.identity.extensions, Extension::MajorSeventh);
        if ((patternA || patternB) && (bassPc != rPc) && isPlainTriad) {
            // Find the bass-rooted candidate in rawCandidates (the top-3 results[]
            // cap is routinely exhausted by same-rootPc variants of the iii/III
            // reading; the bass-rooted target often lives only in rawCandidates).
            for (const RawCandidate& rc : gateCtx.rawCandidates) {
                if (rc.rootPc != bassPc) continue;
                // Append a built result for the bass-rooted candidate and swap
                // it into the winner slot (same swap pattern as the FM2 fallback
                // at the start of the inversion-correction block, line ~2189).
                results.push_back(buildResult(rc));
                std::swap(results[0], results.back());
                break;
            }
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
            upperTones.reserve(gateCtx.tones.size());
            for (const ChordAnalysisTone& t : gateCtx.tones) {
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
                // Disable the inversion correction and guaranteed-alt append for
                // Pass 2: in the upper-voice-only analysis there is no sustained
                // bass to correct against, and those blocks distort the confidence
                // gap used to confirm the pedal.
                ChordAnalyzerPreferences pass2Prefs = prefs;
                pass2Prefs.inversionSuspicionMargin = 0.0;
                // Capture a gate context for Pass 2 and re-apply this tail to it,
                // matching the inline version where the nested analyzeChord() ran
                // its own Iter 86/91/pedal tail (context = nullptr ⇒ Iter 91 skips).
                PostScoringGateContext pass2GateCtx;
                auto pass2 = RuleBasedChordAnalyzer{}.analyzeChord(
                    upperTones, gateCtx.keySigFifths, gateCtx.keyMode, nullptr,
                    pass2Prefs, &pass2GateCtx);
                applyIter8691Pedal(pass2, pass2GateCtx, nullptr, pass2Prefs);

                if (!pass2.empty()) {
                    // Confidence is measured against the first competitor with a
                    // DIFFERENT root.  Multiple templates for the same chord quality
                    // (triad / maj7 / dom7) can score identically when their extended
                    // tones are absent, filling all three result slots with the same
                    // root — making a gap-to-next-in-list metric artificially low.
                    // Comparing the winner's score against the best genuine alternative
                    // (different rootPc) gives a meaningful pedal-confirmation signal.
                    // Sigmoid constants (midpoint=2.0, steepness=1.5) are the empirical
                    // defaults from ChordAnalyzerPreferences, inlined here after the
                    // chord-level normalizedConfidence field was removed as dead code.
                    double pass2AltScore = 0.0;
                    const int p2Root = pass2.front().identity.rootPc;
                    for (size_t i = 1; i < pass2.size(); ++i) {
                        if (pass2[i].identity.rootPc != p2Root) {
                            pass2AltScore = pass2[i].identity.score;
                            break;
                        }
                    }
                    const double gap = pass2.front().identity.score - pass2AltScore;
                    const double c2  = 1.0 / (1.0 + std::exp(-1.5 * (gap - 2.0)));
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
    //
    // 17 templates: must remain byte-identical to the analyzeChord array (~L1955).
    // diagnoseChord intentionally omits the production guards (B2 aug7 dual
    // guard, etc.) so every cell appears in the diagnostic breakdown — guards
    // are production-only.  See docs/scoring_model.md §2.
    // When adding a template: update both this array AND the analyzeChord
    // array AND all three score matrices in analyzeChord atomically.
    static const std::array<TemplateDef, 17> kDiagTemplates = {{
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
        { ChordQuality::Augmented,      { 0, 4, 8, 10 },    { 0, +4, +8, -2 }   },  // aug7 (C7♯5)
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
            // dim7CharacteristicBonus is a ROTATION-SELECTION MECHANISM — see the
            // matching annotation at the analyzeChord call site (~L2036) and
            // docs/scoring_model.md §4.  Mirrored here so diagnostic output reflects
            // the same scoring component.
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
