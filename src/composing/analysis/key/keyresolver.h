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

// ── composing/analysis/key/keyresolver ───────────────────────────────────────
//
// Single source of truth for windowed key/mode resolution. Replaces the two
// parallel implementations of `inferLocalKey` (tools/batch_analyze.cpp) and
// `resolveKeyAndMode` (notationcomposingbridgehelpers.cpp). See
// docs/duplication_audit.md §2.11 and §5.3.
//
// The resolver (Stage 4b-i: note-based inference PRIMARY, declared mode demoted
// to a small droppable hint):
//   • reads the score's key signature event at the analysis tick
//   • detects a declared mode from the key signature's KeyMode enum (dropped
//     entirely when prefs.ignoreDeclaredMode — the mode-absent measurement floor)
//   • runs the dynamic-lookahead loop FROM PIECE START (the former declared-mode
//     piece-start short-circuit was removed in 4b-i — the opening is note-based),
//     growing the window until the top result clears
//     `dynamicLookaheadConfidenceThreshold` or `dynamicLookaheadMaxBeats`
//   • falls back to the notated key signature when pitch evidence is sparse
//   • applies hysteresis vs the previous region's result (note-based)
//
// The declared mode now influences the result ONLY via the small additive hint
// inside analyzeKeyMode (prefs.declaredModePenalty, 1.0). The former hard
// "strong declared-mode prior" promotion was removed in 4b-i.
//
// Returns the ranked top-N candidates with the chosen winner at index 0.
// Callers that only need the winner take [0]; batch additionally takes [1]
// for its `keyModeRunnerUp` JSON field.

#include <cstddef>
#include <set>
#include <vector>

#include "composing/analysis/key/keymodeanalyzer.h"

namespace mu::engraving {
class Score;
class Fraction;
using staff_idx_t = std::size_t;
}

namespace mu::composing::analysis::keyresolver {

/// Diagnostic-only resolver trace (Stage-4 emission instrument). Filled ONLY when
/// a non-null pointer is supplied to resolveKeyAndModeRanked; production passes
/// nullptr and is byte-identical. Records which resolver path was taken and the
/// per-candidate emission breakdown from the final analyzeKeyMode call.
struct KeyResolveDump {
    int notatedFifths   = 0;          ///< key signature fifths read at the tick (pre-correction)
    int correctedFifths = 0;          ///< after partialSignatureCorrection
    int declaredModeOrdinal = -1;     ///< KeySigMode ordinal of the declared mode, or -1 if none
    const char* pathTaken = "normal"; ///< "fallback" | "normal" ("anchor" removed in 4b-i)
    int lookaheadBeatsUsed = 0;       ///< window beats at the final analyzeKeyMode call
    bool hysteresisPromoted   = false; ///< the hysteresis block reordered the winner
    bool strongPriorPromoted  = false; ///< always false since 4b-i (strong declared-mode prior removed; field kept for dump-format stability)
    std::vector<mu::composing::analysis::KeyCandidateScore> candidates; ///< emission breakdown (empty on anchor/fallback)
};

/// Resolve key/mode at `tick` returning ranked candidates.
///
/// `staffIdx` selects which staff supplies the key signature.
/// `prevResult` is the previous region's chosen result for hysteresis, or
/// nullptr at the first region (piece-start shortcut may apply).
///
/// `dumpOut` is diagnostic-only: when non-null it is filled with the resolver
/// trace and the final analyzeKeyMode per-candidate breakdown. Pass nullptr (the
/// default) on every production path — output is byte-identical either way.
///
/// Returned vector always has size ≥ 1. The chosen winner — after note-based
/// hysteresis — is at index 0.
std::vector<mu::composing::analysis::KeyModeAnalysisResult>
resolveKeyAndModeRanked(
    const mu::engraving::Score* sc,
    const mu::engraving::Fraction& tick,
    mu::engraving::staff_idx_t staffIdx,
    const std::set<std::size_t>& excludeStaves,
    const mu::composing::analysis::KeyModeAnalyzerPreferences& prefs,
    const mu::composing::analysis::KeyModeAnalysisResult* prevResult = nullptr,
    KeyResolveDump* dumpOut = nullptr);

} // namespace mu::composing::analysis::keyresolver
