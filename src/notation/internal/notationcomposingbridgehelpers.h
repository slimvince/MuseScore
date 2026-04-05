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

// ── Shared bridge helpers — INTERNAL, do not include outside notation/internal ──
//
// Utility types and functions shared by the two bridge translation units:
//   • notationcomposingbridge.cpp  (harmonicAnnotation, analyzeNoteHarmonicContext)
//   • notationharmonicrhythmbridge.cpp (analyzeHarmonicRhythm)
//
// All symbols live in an anonymous namespace in each TU's .cpp — this header
// only declares them so they can be shared via a common .cpp compilation unit.
// See notationcomposingbridgehelpers.cpp for the definitions.

#include <set>
#include <vector>

#include "composing/analysis/chord/chordanalyzer.h"
#include "composing/analysis/key/keymodeanalyzer.h"

namespace mu::engraving {
class Score;
class Segment;
class Fraction;
using staff_idx_t = size_t;
}

namespace mu::notation::internal {

/// A raw sounding note: playback pitch + TPC spelling.
struct SoundingNote { int ppitch; int tpc; };

/// Collect all notes sounding at anchorSeg's tick across eligible staves.
/// Walks backward up to 4 quarter notes to catch sustained notes.
void collectSoundingAt(const mu::engraving::Score* sc,
                       const mu::engraving::Segment* anchorSeg,
                       const std::set<size_t>& excludeStaves,
                       std::vector<SoundingNote>& out);

/// Convert raw sounding notes to analysis tones.  Marks the lowest pitch as bass.
std::vector<mu::composing::analysis::ChordAnalysisTone>
buildTones(const std::vector<SoundingNote>& sounding);

/// Map MuseScore's BeatType enum to a weight for key/mode analysis.
double beatTypeToWeight(mu::engraving::BeatType bt,
                        const mu::composing::analysis::KeyModeAnalyzerPreferences& prefs);

/// Exponential time decay: notes further from the analysis tick carry less weight.
double timeDecay(double beatsAgo, double decayRate = 0.7);

/// Count distinct pitch classes in a PitchContext vector.
int distinctPitchClasses(
    const std::vector<mu::composing::analysis::KeyModeAnalyzer::PitchContext>& ctx);

/// Collect pitch context for the window [windowStart, windowEnd], appending to ctx.
void collectPitchContext(const mu::engraving::Score* sc,
                         const mu::engraving::Fraction& tick,
                         const mu::engraving::Fraction& windowStart,
                         const mu::engraving::Fraction& windowEnd,
                         const std::set<size_t>& excludeStaves,
                         const mu::composing::analysis::KeyModeAnalyzerPreferences& prefs,
                         std::vector<mu::composing::analysis::KeyModeAnalyzer::PitchContext>& ctx);

/// Resolve key signature and mode at a tick, with optional hysteresis.
void resolveKeyAndMode(const mu::engraving::Score* sc,
                       const mu::engraving::Fraction& tick,
                       mu::engraving::staff_idx_t staffIdx,
                       const std::set<size_t>& excludeStaves,
                       int& outKeyFifths,
                       mu::composing::analysis::KeySigMode& outMode,
                       double& outConfidence,
                       const mu::composing::analysis::KeyModeAnalysisResult* prevResult = nullptr,
                       double* outScore = nullptr);

/// Find the previous chord's temporal context by walking backward from seg.
mu::composing::analysis::ChordTemporalContext
findTemporalContext(const mu::engraving::Score* sc,
                    const mu::engraving::Segment* seg,
                    const std::set<size_t>& excludeStaves,
                    int keyFifths,
                    mu::composing::analysis::KeySigMode keyMode);

} // namespace mu::notation::internal
