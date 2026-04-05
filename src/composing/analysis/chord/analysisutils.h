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

#include <map>
#include <string>

namespace mu::composing::analysis {

/// Describes the valid range for a single numeric scoring parameter.
///
/// Used by ChordAnalyzerPreferences::bounds() and KeyModeAnalyzerPreferences::bounds()
/// to expose all tunable parameters to automated optimizers or UI sliders.
///
/// isManual: when true, the parameter should be held fixed during automated
/// optimization (it is wired to a user-visible preference or has a narrow
/// hand-tuned sweet-spot).  When false, it is fair game for gradient-based
/// or grid search optimizers.
struct ParameterBound {
    double min;
    double max;
    bool   isManual = false;
};

/// Convenience alias for the map returned by bounds().
using ParameterBoundsMap = std::map<std::string, ParameterBound>;

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

} // namespace mu::composing::analysis

#endif // MU_COMPOSING_ANALYSIS_ANALYSISUTILS_H
