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

#include "composing/analyzed_section.h"

namespace mu::engraving {
class Score;
class Fraction;
}

namespace mu::composing::analysis::joint {
struct NotationRecord;
}

namespace mu::notation {

/// Populate a grand-staff instrument with a harmonic reduction of the score.
/// Analyzes all eligible staves (excluding the target) within the time range,
/// detects harmonic rhythm, and writes notes, chord symbols, and Roman numerals.
///
/// Phase 3a wrapper: internally calls
/// `mu::composing::analysis::analyzeSection(...)` and forwards to
/// `emitImplodedChordTrack` below. Kept at this signature so existing call
/// sites stay untouched.
///
/// @return true if any content was written.
bool populateChordTrack(
    mu::engraving::Score* score,
    const mu::engraving::Fraction& startTick,
    const mu::engraving::Fraction& endTick,
    mu::engraving::staff_idx_t trebleStaffIdx,
    bool useCollectedTones = false);

/// Phase 3a chord-track emitter: writes notes and chord-symbol annotations
/// to the grand-staff pair starting at `trebleStaffIdx` based on a
/// pre-analysed `AnalyzedSection`. Same emit behaviour as `populateChordTrack`
/// — voicings, key annotations, segment placement, all unchanged.
///
/// Callers that already hold an `AnalyzedSection` (e.g. the unified pipeline
/// in Phase 4+) should call this directly instead of going through
/// `populateChordTrack`.
///
/// `record` (default null) selects the RECORD ARM (seams part 2): when non-null,
/// the section was derived from the joint notation record and this emitter takes
/// the record-arm specifics — the Roman numeral is the record's PUBLISHED
/// `romanNumeral` fact (looked up per region via `noteView`, NOT re-formatted from
/// `ChordIdentity`); a rootless chromatic class writes no chord symbol (matching
/// the batch rootless ""); the borrowed-key source-key search is restricted to the
/// C1 two modes (Ionian/Aeolian). When null the legacy arm runs byte-identically.
///
/// @return true if any content was written.
bool emitImplodedChordTrack(
    mu::engraving::Score* score,
    const mu::composing::analysis::AnalyzedSection& section,
    const mu::engraving::Fraction& startTick,
    const mu::engraving::Fraction& endTick,
    mu::engraving::staff_idx_t trebleStaffIdx,
    bool useCollectedTones = false,
    const mu::composing::analysis::joint::NotationRecord* record = nullptr);

} // namespace mu::notation
