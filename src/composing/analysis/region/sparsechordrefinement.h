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

// ── composing/analysis/region/sparsechordrefinement ──────────────────────────
//
// Diatonic-quality refinement passes applied to a per-region ChordAnalysisResult
// before it is committed to the region list.  Phase 4 of the duplication
// remediation (docs/duplication_audit.md §5.4) moved these out of
// notation/internal so the shared `analyzeRegions` orchestrator can call them
// directly.  notation::internal exposes pass-through entry points for callers
// that still need them outside the regional pipeline.

#include <vector>

#include "composing/analysis/chord/chordanalyzer.h"
#include "composing/analysis/key/keymodeanalyzer.h"

namespace mu::composing::analysis::region {

/// Returns the diatonic scale degree [0..6] of @p rootPc under (keyFifths, keyMode),
/// or -1 if rootPc is not in the scale.
int diatonicDegreeForRootPc(int rootPc, int keyFifths, KeySigMode keyMode);

/// Upgrade user-facing sparse results from Unknown to the diatonic triad quality
/// implied by the resolved key/mode when the sounding tones are compatible.
void refineSparseChordQualityFromKeyContext(
    ChordAnalysisResult& result,
    const std::vector<ChordAnalysisTone>& tones,
    int keyFifths,
    KeySigMode keyMode);

/// Iter 75/76 — diatonic-quality prior for thin-evidence sparse-texture regions.
///
/// When the bridge's analyzeChord call (with sparse prefs) returns a
/// Power/Suspended2/Suspended4 candidate on a region with ≤ 2 distinct pitch
/// classes, and the candidate's root is a diatonic scale degree of the current
/// key/mode, promote the quality to that degree's diatonic triad quality if the
/// present tones are consistent with that shape.  Dense regions (3+ PCs) are
/// unaffected — their winner quality is taken at face value.
void applyTonicPriorToSparseChord(
    ChordAnalysisResult& result,
    const std::vector<ChordAnalysisTone>& tones,
    int keyFifths,
    KeySigMode keyMode);

/// Force-assign the diatonic triad quality for a chord-track region that still
/// has quality=Unknown after the standard refinement.  Unlike
/// refineSparseChordQualityFromKeyContext, this does NOT apply the Aeolian
/// lone-tonic/dominant exclusion — appropriate for chord-track annotation where
/// annotating even sparse/monophonic regions is desirable.
void forceChordTrackQualityFromKeyContext(
    ChordAnalysisResult& result,
    KeySigMode keyMode);

} // namespace mu::composing::analysis::region
