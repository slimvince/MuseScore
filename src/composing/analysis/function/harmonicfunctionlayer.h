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

// harmonicfunctionlayer.h
// Harmonic function layer — post-analysis pass between analyzeChord() output
// and final chord label. Called from regionanalyzer.cpp after each non-
// exploratory analyzeChord() call.
//
// E1: pass-through (no changes to ChordAnalysisResult).
// E2: progression signals migrate here (rootContinuityBonus, w_seq, w_dim).
// E3: post-scoring gates migrate here (Gate J, Gates A–D, dim7 rotation).
// E4: cadence detection and functional labeling.
//
// See docs/scoring_model.md §10 for the full migration plan.

#pragma once

#include "composing/analysis/chord/chordanalyzer.h"

namespace mu::composing::function {

/// Context passed to the function layer for each region.
/// Extended in later phases (E4: phrase boundaries, cadence evidence).
struct HarmonicFunctionContext {
    int keyFifths { 0 };
    analysis::KeySigMode keyMode { analysis::KeySigMode::Ionian };
    int previousRootPc { -1 };   ///< Root PC of the preceding region (-1 = unknown)
    int nextRootPc { -1 };       ///< Root PC of the following region (-1 = unknown)
};

/// Apply harmonic function reasoning to the winning chord candidate.
/// Modifies \p result in-place. Called after analyzeChord() + refinement,
/// gated on !prefs.explorationMode. E1: no-op.
void applyHarmonicFunction(analysis::ChordAnalysisResult& result,
                           const HarmonicFunctionContext& ctx);

} // namespace mu::composing::function
