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

#ifndef MU_COMPOSING_ANALYSIS_ANALYSISUTILS_H
#define MU_COMPOSING_ANALYSIS_ANALYSISUTILS_H

#include <cstdint>
#include <map>
#include <string>

namespace mu::composing::analysis {

// ParameterBound / ParameterBoundsMap (the bounds() return types) were relocated to
// the leaf types header analysis/types/analysistypes.h (Phase-5 audit-Q2 refactor) so
// the key layer can obtain them without back-edging into chord/. This header keeps the
// pitch/key free functions below. Pure relocation. See cowork_types_header_design.md.

/// Returns true when \p value ends with the string literal \p suffix.
inline bool endsWith(const std::string& value, const char* suffix)
{
    const size_t suffixLen = std::char_traits<char>::length(suffix);
    return value.size() >= suffixLen
           && value.compare(value.size() - suffixLen, suffixLen, suffix) == 0;
}

/// Maps a key signature (in fifths, -7..+7) to the pitch class of its Ionian (major) tonic.
inline int ionianTonicPcFromFifths(int fifths)
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

/// Normalises any integer pitch or interval to a pitch class in [0, 11].
inline int normalizePc(int pitch)
{
    int pc = pitch % 12;
    return pc < 0 ? pc + 12 : pc;
}

/// True if pitch class \p pc is set in the 12-bit pitch-class \p mask.
/// \p pc is normalised first, so negative or out-of-range inputs are accepted.
inline bool pcInMask(uint16_t mask, int pc) noexcept
{
    return (mask >> normalizePc(pc)) & 1u;
}

/// 12-bit mask of the diatonic pitch classes of a key SIGNATURE (Ionian).
/// Signature `fifths` selects the seven consecutive circle-of-fifths positions
/// [fifths-1, fifths+5]; position i has pitch class (7·i) mod 12.  For fifths=0
/// this is {0,2,4,5,7,9,11} (C-major / A-minor natural collection).
/// Key-agnostic: depends ONLY on the notated signature, never a resolved mode.
inline uint16_t diatonicMaskFromFifths(int fifths) noexcept
{
    uint16_t m = 0;
    for (int i = fifths - 1; i <= fifths + 5; ++i) {
        m |= static_cast<uint16_t>(1u << normalizePc(7 * i));
    }
    return m;
}

/// 12-bit diatonic-collection mask of a LOCAL key given its tonic pitch class and
/// mode.  Major (\p isMajor true): the major scale {0,2,4,5,7,9,11}.  Minor
/// (\p isMajor false): natural minor PLUS the raised leading tone (harmonic minor,
/// {0,2,3,5,7,8,10,11}), so a genuine minor V→i's raised LT is in-collection.
/// Key-agnostic: built from (tonic, mode) alone, never a resolved key.
/// CONVENTION: the boolean is `isMajor`; a call site holding `minorMode` passes
/// `!minorMode`.
inline uint16_t collectionMask(int tonicPc, bool isMajor) noexcept
{
    static constexpr int kMajor[]     = { 0, 2, 4, 5, 7, 9, 11 };
    static constexpr int kMinorHarm[] = { 0, 2, 3, 5, 7, 8, 10, 11 }; // natural minor + raised 7
    uint16_t m = 0;
    if (isMajor) {
        for (int d : kMajor) {
            m |= static_cast<uint16_t>(1u << normalizePc(tonicPc + d));
        }
    } else {
        for (int d : kMinorHarm) {
            m |= static_cast<uint16_t>(1u << normalizePc(tonicPc + d));
        }
    }
    return m;
}

} // namespace mu::composing::analysis

#endif // MU_COMPOSING_ANALYSIS_ANALYSISUTILS_H
