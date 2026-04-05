/*
 * SPDX-License-Identifier: GPL-3.0-only
 * MuseScore-Studio-CLA-applies
 *
 * MuseScore Studio
 * Music Composition & Notation
 *
 * Copyright (C) 2021 MuseScore Limited
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
#pragma once

// ── Implode-to-chord-staff bridge — public declaration ───────────────────────
//
// Implementation lives in notationimplodebridge.cpp.

#include "engraving/types/types.h"  // staff_idx_t

namespace mu::engraving {
class Score;
class Fraction;
}

namespace mu::notation {

/// Populate a grand-staff instrument with a harmonic reduction of the score.
/// Analyzes all eligible staves (excluding the target) within the time range,
/// detects harmonic rhythm, and writes notes, chord symbols, and Roman numerals.
/// @return true if any content was written.
bool populateChordTrack(
    mu::engraving::Score* score,
    const mu::engraving::Fraction& startTick,
    const mu::engraving::Fraction& endTick,
    mu::engraving::staff_idx_t trebleStaffIdx,
    bool useCollectedTones = false);

} // namespace mu::notation
