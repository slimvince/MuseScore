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

#pragma once

#include <set>
#include <vector>

#include "chordanalyzer.h"
#include "keymodeanalyzer.h"

namespace mu::engraving {
class Score;
class Fraction;
}

namespace mu::composing::analysis {

/// A contiguous time region in which the harmonic content (root + quality)
/// remains constant.  Produced by analyzeHarmonicRhythm() and consumed by
/// both the chord track population and region intonation workflows.
///
/// Tick values are stored as raw integers (use Fraction::ticks() /
/// Fraction::fromTicks() to convert) so that this header stays free of the
/// engraving Fraction include — preserving composing_analysis's independence
/// from the engraving module.
struct HarmonicRegion {
    int startTick = 0;                              ///< First tick of this region (raw tick integer)
    int endTick = 0;                                ///< First tick of the next region (exclusive)
    ChordAnalysisResult chordResult;                ///< Root, quality, extensions, degree
    KeyModeAnalysisResult keyModeResult;            ///< Key and mode context for this region
    std::vector<ChordAnalysisTone> tones;           ///< The sounding tones that produced the analysis
};

/// Scan a time range across all eligible staves, detect harmonic boundaries
/// (ticks where the sounding pitch-class set changes), run chord analysis at
/// each boundary, and collapse consecutive same-chord regions.
///
/// @param score           The score to analyze.
/// @param startTick       Start of the time range (inclusive).
/// @param endTick         End of the time range (exclusive).
/// @param excludeStaves   Staff indices to skip (e.g., the chord track target).
///
/// Returns the sequence of harmonic regions, or empty if insufficient data.
///
/// Declared here in composing/; **defined in
/// src/notation/internal/notationcomposingbridge.cpp** — same bridge pattern as
/// analyzeNoteHarmonicContext().
std::vector<HarmonicRegion> analyzeHarmonicRhythm(
    const mu::engraving::Score* score,
    const mu::engraving::Fraction& startTick,
    const mu::engraving::Fraction& endTick,
    const std::set<size_t>& excludeStaves = {});

/// Populate a grand-staff instrument with a harmonic reduction of the score.
///
/// Analyzes all eligible staves (excluding the target) within the time range,
/// detects harmonic rhythm, and writes to the target grand staff:
///   - Treble staff: upper-structure chord tones in close position (C4–C5)
///   - Bass staff:   root note (C2–C3)
///   - Chord symbols (HarmonyType::STANDARD) above the treble staff
///   - Roman numerals (HarmonyType::ROMAN) below the treble staff
///
/// The target region is cleared before population.  The entire operation is
/// one undo group (caller is responsible for startEdit/apply bracketing).
///
/// @param score           The score to mutate.
/// @param startTick       Start of the time range (inclusive).
/// @param endTick         End of the time range (exclusive).
/// @param trebleStaffIdx  Staff index of the treble staff (bass = trebleStaffIdx + 1).
/// @return true if any content was written, false if analysis produced no regions.
///
/// Declared here in composing/; **defined in
/// src/notation/internal/notationcomposingbridge.cpp**.
/// When true, the chord track uses the actual sounding tones from the score
/// (deduplicated by pitch class) rather than reconstructing canonical chord
/// tones from the analysis result.  Preserves the original voicing/color.
/// When false (default), the chord track shows the idealized chord.
bool populateChordTrack(
    mu::engraving::Score* score,
    const mu::engraving::Fraction& startTick,
    const mu::engraving::Fraction& endTick,
    mu::engraving::staff_idx_t trebleStaffIdx,
    bool useCollectedTones = false);

} // namespace mu::composing::analysis
