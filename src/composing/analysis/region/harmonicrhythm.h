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

#include "../chord/chordanalyzer.h"
#include "../key/keymodeanalyzer.h"

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
    bool hasAnalyzedChord = true;                   ///< False when note-based chord analysis produced no candidate for this region
    KeyModeAnalysisResult keyModeResult;            ///< Key and mode context for this region
    std::vector<ChordAnalysisTone> tones;           ///< The sounding tones that produced the analysis

    // ── §4.1c Jazz mode fields ──────────────────────────────────────────────
    /// True when this region was produced by the chord-symbol (jazz) path.
    /// False (default) when produced by Jaccard or legacy pitch-class detection.
    bool fromChordSymbol = false;
    /// Root pitch class (0–11) read directly from the written chord symbol.
    /// -1 when fromChordSymbol is false or when the chord symbol had no parseable root.
    int writtenRootPc = -1;
};

} // namespace mu::composing::analysis
