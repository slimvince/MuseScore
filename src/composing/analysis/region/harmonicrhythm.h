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

/// Snapshot of the `ChordTemporalContext` values that were active when the
/// enclosing region was analyzed.  The analyzer continues to consume
/// `ChordTemporalContext` as input; this struct is the parallel output
/// surface that downstream emitters and the tick-regional bridge read.
/// Phase 3c moved this from `notation/internal/` to here so it can be
/// shared between `HarmonicRegion` (transitional plumbing) and
/// `AnalyzedRegion` (canonical surface).
struct ChordTemporalExtensions {
    int previousRootPc = -1;
    int previousBassPc = -1;
    ChordQuality previousQuality = ChordQuality::Unknown;
    bool bassIsStepwiseFromPrevious = false;
    bool bassIsStepwiseToNext = false;
};

/// Snapshot the analyzer-input temporal context as a downstream-facing
/// extensions value.
inline ChordTemporalExtensions toExtensionsSnapshot(const ChordTemporalContext& ctx)
{
    ChordTemporalExtensions ext;
    ext.previousRootPc = ctx.previousRootPc;
    ext.previousBassPc = ctx.previousBassPc;
    ext.previousQuality = ctx.previousQuality;
    ext.bassIsStepwiseFromPrevious = ctx.bassIsStepwiseFromPrevious;
    ext.bassIsStepwiseToNext = ctx.bassIsStepwiseToNext;
    return ext;
}

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
    std::vector<ChordAnalysisResult> alternatives;  ///< Candidates [1..N-1] from the per-region analyzeChord (Phase 3c)
    bool hasAnalyzedChord = true;                   ///< False when note-based chord analysis produced no candidate for this region
    KeyModeAnalysisResult keyModeResult;            ///< Key and mode context for this region
    std::vector<ChordAnalysisTone> tones;           ///< The sounding tones that produced the analysis
    ChordTemporalExtensions temporalExtensions;     ///< Snapshot of the temporal context used to analyze this region (Phase 3c)
};

} // namespace mu::composing::analysis
