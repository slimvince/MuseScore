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

// ── Intonation/tuning bridge — public declarations ───────────────────────────
//
// Implementation lives in notationtuningbridge.cpp.

#include "composing/intonation/tuning_system.h"  // TuningSystem

namespace mu::engraving {
class Note;
class Score;
class Fraction;
}

namespace mu::notation {

/// Returns true if @p note has an Expression annotation whose trimmed,
/// case-insensitive text equals kTuningAnchorKeyword ("anchor-pitch").
/// The Expression must be attached to the same segment as the note.
bool hasTuningAnchorExpression(const mu::engraving::Note* note);

/// Compute the RetuningSusceptibility for a note.
///
/// AbsolutelyProtected: note carries a kTuningAnchorKeyword Expression.
/// Free:                all other notes (duration-based classification is a
///                      future addition — see backlog).
mu::composing::intonation::RetuningSusceptibility computeSusceptibility(
    const mu::engraving::Note* note);

/// Apply a tuning system to all notes sounding at the selected note's tick,
/// splitting sustained notes as needed to create a clean onset boundary.
/// Returns true if tuning was applied.
bool applyTuningAtNote(const mu::engraving::Note* selectedNote,
                       const mu::composing::intonation::TuningSystem& system);

/// Apply tuning to all notes within a time range using harmonic region analysis.
/// Returns true if any tuning was applied.
bool applyRegionTuning(mu::engraving::Score* score,
                       const mu::engraving::Fraction& startTick,
                       const mu::engraving::Fraction& endTick);

} // namespace mu::notation
