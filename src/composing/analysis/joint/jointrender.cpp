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

#include "jointrender.h"

#include <cctype>
#include <map>
#include <set>

#include "jointprimitives.h"   // pcKeyName (the module's one pc->spelling source, #6)

namespace mu::composing::analysis::joint {

// probe_run._QUAL_STR: joint chord quality -> the .ours.json quality string a8/compare_rn grades.
std::string jointOursQuality(const std::string& quality)
{
    static const std::map<std::string, std::string> kMap = {
        { "Maj", "Major" }, { "Dom7", "Major" }, { "Maj7", "Major" }, { "Min", "Minor" },
        { "Min7", "Minor" }, { "MinMaj7", "Minor" }, { "Dim", "Diminished" }, { "Dim7", "Diminished" },
        { "HalfDim", "HalfDiminished" }, { "HalfDim7", "HalfDiminished" }, { "Aug", "Augmented" },
        { "Aug7", "Augmented" }, { "AugMaj7", "Augmented" }, { "AugSixth", "Major" },
        { "Neapolitan", "Major" }
    };
    const auto it = kMap.find(quality);
    return it != kMap.end() ? it->second : std::string("Unknown");
}

// The chord-symbol string: root's canonical pc name + the class's own quality (e.g. "GMaj7"). Empty
// when the class has no defined root (a chromatic class chordFactorPcs leaves rootless).
std::string jointChordSymbol(std::optional<int> rootPc, const std::string& quality)
{
    if (!rootPc.has_value()) {
        return std::string();
    }
    return pcKeyName(*rootPc) + quality;
}

// probe_run.render_rn: a When-in-Rome-style Roman numeral from the (inversion-free) class + the
// derived bass role. `bassRole` is empty when the bass is not a chord factor (Python .get default "").
std::string jointRenderRn(const LabelClass& cls, const std::string& bassRole, bool hasSeventh)
{
    static const std::set<std::string> kMajorColor = {
        "Maj", "Dom7", "Maj7", "Aug", "Aug7", "AugMaj7", "AugSixth", "Neapolitan"
    };
    const std::string q = cls.quality();
    std::string d = cls.degreeBase();
    if (kMajorColor.find(q) == kMajorColor.end()) {
        for (char& c : d) {
            c = static_cast<char>(std::tolower(static_cast<unsigned char>(c)));
        }
    }
    std::string sig;
    if (q == "Dim" || q == "Dim7") {
        sig = "o";
    } else if (q == "HalfDim" || q == "HalfDim7") {
        sig = "\xC3\xB8";                         // U+00F8 LATIN SMALL LETTER O WITH STROKE (ø), UTF-8
    } else if (q == "Aug" || q == "Aug7" || q == "AugMaj7") {
        sig = "+";
    }
    std::string fig;                             // _FIG_SEVENTH / _FIG_TRIAD; "" when bass role unknown
    if (hasSeventh) {
        if (bassRole == "root") { fig = "7"; } else if (bassRole == "third") { fig = "6/5"; } else if (bassRole == "fifth") { fig = "4/3"; } else if (bassRole == "seventh") { fig = "4/2"; }
    } else {
        if (bassRole == "third") { fig = "6"; } else if (bassRole == "fifth") { fig = "6/4"; }
        // "root" -> "" (root-position triad); unknown -> ""
    }
    const std::string tgt = cls.target().empty() ? std::string() : ("/" + cls.target());
    return d + sig + fig + tgt;
}

} // namespace mu::composing::analysis::joint
