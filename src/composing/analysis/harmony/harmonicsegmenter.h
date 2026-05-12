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

#include <functional>
#include <set>
#include <string>
#include <vector>

#include "engraving/types/constants.h"
#include "../chord/chordanalyzer.h"
#include "../key/keymodeanalyzer.h"

namespace mu::engraving {
class Score;
class Fraction;
}

namespace mu::composing {

/// Minimum analyzeChord winner score for a region to qualify as a Round 1 anchor.
/// Tuned against the Baroque corpus (Iter 52); initial value 2.0 produced
/// mean anchor/jaccard=0.08 (too sparse). Relaxed to 1.5 per Step 5 protocol.
inline constexpr double kAnchorMinScore = 1.5;

/// Minimum region duration (in ticks) for Round 1 anchor eligibility.
/// Initial value 2*DIVISION (half note); relaxed to 1*DIVISION per Step 5 protocol.
inline constexpr int kAnchorMinDurationTicks = 1 * mu::engraving::Constants::DIVISION;

/// Minimum analyzeChord winner score for a candidate to be promoted in Round 2 gap-fill.
/// Initial 1.0 produced mean placed/jaccard=1.63 on the Baroque corpus (over-placing);
/// raised to 1.25 per Iter 53 Step 5 protocol.
inline constexpr double kRound2MinScore = 1.25;

/// Working type for the greedy-expand segmentation algorithm.
/// Produced by greedyExpandSegmentation(); consumed by analyzeScore() (batch path)
/// and (Iter 68+) by the notation bridge.
struct PlacedRegion {
    int startTick = 0;
    int endTick   = 0;

    // Greedy-expand metadata
    int    round      = 0;      ///< 0 = candidate (not yet placed), 1+ = placed in that round
    double confidence = 0.0;    ///< chord-score confidence at placement time
    bool   isAnchor   = false;  ///< true if placed in round 1 (structural anchor)
    std::string reason;         ///< human-readable placement rationale

    // Chord identity determined at placement time (from analyzeChord on tones)
    int    rootPitchClass = -1;
    int    bassPitchClass = -1;
    // quality stored as string for now — replace with ChordQuality enum if convenient
    std::string quality;
};

/// Host-supplied helpers needed by greedyExpandSegmentation().
///
/// The segmenter is a pure algorithm over a Score; it does not own the policy
/// for what counts as an eligible staff or how a region's tones are collected.
/// Both call sites (batch_analyze and the notation bridge) supply their own
/// implementations — they share the algorithm, not the helpers.
struct HarmonicSegmenterCallbacks {
    /// Returns true if the given staff index should participate in chord analysis.
    /// Caller is responsible for excludeStaves filtering before this is reached.
    std::function<bool(size_t staffIdx)> staffIsEligible;

    /// Returns the aggregated, weighted tones for the half-open region
    /// [startTick, endTick).  Empty result means insufficient data — the
    /// segmenter will skip the region.
    std::function<std::vector<analysis::ChordAnalysisTone>(int startTick, int endTick)>
        collectRegionTones;
};

/// Entry point for the replacement greedy-expand segmentation algorithm.
/// Returns all note-change-event regions as round=0 candidates, then promotes
/// those satisfying beat/duration/voice/score criteria to round=1 anchors and
/// fills gaps using bilateral context (round=2).
std::vector<PlacedRegion>
greedyExpandSegmentation(const mu::engraving::Score* score,
                         const mu::engraving::Fraction& startTick,
                         const mu::engraving::Fraction& endTick,
                         const std::set<size_t>& excludeStaves,
                         const analysis::ChordAnalyzerPreferences& prefs,
                         analysis::IChordAnalyzer* chordAnalyzer,
                         int globalKeyFifths,
                         analysis::KeySigMode globalKeyMode,
                         const HarmonicSegmenterCallbacks& callbacks);

/// Extracts the start ticks of all placed regions (round >= 1) as a sorted,
/// deduplicated vector of Fractions — drop-in replacement for the
/// detectHarmonicBoundariesJaccard output in analyzeScore().
std::vector<mu::engraving::Fraction>
placedRegionsToTicks(const std::vector<PlacedRegion>& regions);

} // namespace mu::composing
