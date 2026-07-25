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

#include "labelclass.h"

#include <array>
#include <utility>

namespace mu::composing::analysis::joint {
// normalize._SEVENTH_QUALITIES
static const std::array<const char*, 8> kSeventhQualities = {
    "Dom7", "Maj7", "Min7", "MinMaj7", "Dim7", "HalfDim7", "Aug7", "AugMaj7"
};

// The exact three-character field separator used by LabelClass.key().
static const std::string kSep = " | ";

LabelClass::LabelClass(std::string degreeBase, std::string quality, std::string inversion,
                       std::string target, bool rawUnnormalized)
    : m_degreeBase(std::move(degreeBase)), m_quality(std::move(quality)),
    m_inversion(std::move(inversion)), m_target(std::move(target)),
    m_rawUnnormalized(rawUnnormalized)
{
}

std::string LabelClass::key() const
{
    return m_degreeBase + kSep + m_quality + kSep + m_inversion + kSep + m_target;
}

LabelClass LabelClass::inversionFree() const
{
    return LabelClass(m_degreeBase, m_quality, "", m_target, m_rawUnnormalized);
}

LabelClass LabelClass::family() const
{
    const std::string fam = isSeventhQuality(m_quality) ? "seventh" : "triad";
    return LabelClass(m_degreeBase, fam, "", m_target, m_rawUnnormalized);
}

bool LabelClass::operator==(const LabelClass& o) const
{
    return m_degreeBase == o.m_degreeBase && m_quality == o.m_quality
           && m_inversion == o.m_inversion && m_target == o.m_target
           && m_rawUnnormalized == o.m_rawUnnormalized;
}

bool isSeventhQuality(const std::string& quality)
{
    for (const char* q : kSeventhQualities) {
        if (quality == q) {
            return true;
        }
    }
    return false;
}

LabelClass classFromKey(const std::string& key)
{
    // Python: parts = key.split(" | "); while len(parts) < 4: parts.append("").
    // std::string::split on the 3-char separator, then pad to four fields.
    std::array<std::string, 4> parts = { "", "", "", "" };
    size_t field = 0;
    size_t pos = 0;
    while (field < 4) {
        const size_t next = key.find(kSep, pos);
        if (next == std::string::npos) {
            parts[field] = key.substr(pos);
            break;
        }
        parts[field] = key.substr(pos, next - pos);
        pos = next + kSep.size();
        ++field;
    }
    return LabelClass(parts[0], parts[1], parts[2], parts[3]);
}
} // namespace mu::composing::analysis::joint
