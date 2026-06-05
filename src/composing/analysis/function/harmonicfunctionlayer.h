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

#include <vector>

#include "composing/analysis/chord/chordanalyzer.h"

namespace mu::composing::function {

/// Context passed to the function layer for each region.
/// Extended in later phases (E4: phrase boundaries, cadence evidence).
struct HarmonicFunctionContext {
    int keyFifths { 0 };
    analysis::KeySigMode keyMode { analysis::KeySigMode::Ionian };
    int previousRootPc { -1 };   ///< Root PC of the preceding region (-1 = unknown)
    int nextRootPc { -1 };       ///< Root PC of the following region (-1 = unknown)
    int previousBassPc { -1 };   ///< Bass PC of the preceding region (-1 = unknown).
                                  ///< Required by E2d Pass B (wStepInBonus gate).
    int nextBassPc     { -1 };   ///< Bass PC of the following region (-1 = unknown).
                                  ///< Required by E2d Pass B (wStepOutBonus gate).
};

// Forward declaration — full definition further down in this header.
struct ScoringSnapshot;

/// Apply harmonic function reasoning to the winning chord candidate.
/// When \p snapshot is non-null (E2c mode), re-scores the full candidate set
/// using the snapshot and promotes the signal-inclusive winner into
/// candidates[0]; \p chosenResult is updated to match. When \p snapshot is
/// null (pre-E2c call sites), remains a no-op.
void applyHarmonicFunction(std::vector<analysis::ChordAnalysisResult>& candidates,
                           analysis::ChordAnalysisResult& chosenResult,
                           const HarmonicFunctionContext& ctx,
                           const ScoringSnapshot* snapshot,
                           const analysis::ChordAnalyzerPreferences* prefs);

// -----------------------------------------------------------------------
// Progression-signal bonus functions (E2a: called from chordanalyzer.cpp
// at their existing call sites; will become a post-analysis pass in E2c).
// -----------------------------------------------------------------------

/// Bonus magnitude constants — defined here because they are function-layer
/// properties, not scoring-model constants.
inline constexpr double kWSeq = 0.20;  ///< Sequential root-progression bonus (Iter 95)
inline constexpr double kWDim = 0.15;  ///< Dim/HalfDim leading-tone bonus (Iter 96)
inline constexpr double kWStepIn   = 0.10;  ///< Stepwise-bass step-in bonus (E2d Pass B)
inline constexpr double kWStepOut  = 0.10;  ///< Stepwise-bass step-out bonus (E2d Pass B)
inline constexpr double kStepBudget = kWStepIn + kWStepOut + 0.01;  ///< m7-family guard tolerance

/// Root-continuity bonus.
/// Returns bonusValue when candidateRootPc == previousRootPc, else 0.
/// Called from bassIndependentContextualBonuses (and diagnoseChord path).
double rootContinuityBonus(int candidateRootPc, int previousRootPc,
                           double bonusValue);

/// Sequential root-motion bonus (+kWSeq).
/// Rewards a candidate whose root sits a P4 below nextRootPc (classic V→I).
/// Callers pass nextRootPc = context->nextRootPc, or -1 if context is null.
double wSeqBonus(int candRootPc, int nextRootPc, int distinctPcs,
                 bool jointScoringEnabled, bool explorationMode);

/// Diminished/HalfDim leading-tone bonus (+kWDim).
/// Rewards a Dim/HalfDim candidate whose root sits one semitone below
/// nextRootPc (leading-tone-of-next). For the with-wDim path only.
/// Callers pass nextRootPc = context->nextRootPc, or -1 if context is null.
double wDimBonus(int candRootPc, analysis::ChordQuality quality,
                 int nextRootPc, int distinctPcs,
                 bool jointScoringEnabled, bool explorationMode);

// -----------------------------------------------------------------------
// Scoring snapshot (E2b) — captured by analyzeChord() when
// prefs.captureScoringSnapshot is non-null. Consumed by applyHarmonicFunction()
// in E2c to redo joint scoring with progression signals suppressed.
// -----------------------------------------------------------------------

/// One (bass, root, template) scoring cell, pre-step-bonus.
/// E2c uses the decomposed fields to rebuild the score with any subset of
/// {rootContinuityBonus, w_seq, w_dim} suppressed and then re-runs Pass B.
struct ScoringCell {
    // Identifiers — locate the cell in the (bass, root, template) cube.
    int                    bassPc;
    int                    bassTpc;            ///< TPC of the bass candidate; needed by E2c
                                               ///< to correct bassTpc when the re-scored winner
                                               ///< uses a different bass than the suppressed-signal pass.
    int                    rootPc;
    int                    tiePriority;        ///< Template index; needed by E2c for
                                               ///< the Pass B m7-family guard look-up.
    analysis::ChordQuality quality;
    int                    intervalCount { 0 }; ///< Number of intervals in the template
                                                ///< (templates[tiePriority].intervals.size()).
                                                ///< Used by E2d Pass B m7-family guard:
                                                ///< isMin7 ≡ quality==Minor && intervalCount==4.

    // Bass-independent pitch evidence (basisIndepMatrix[rootPc][tiePriority]).
    // INCLUDES the rootContinuityBonus contribution (if it fired for this rootPc).
    // E2c deducts:
    //   fn::rootContinuityBonus(rootPc, ctx.previousRootPc, prefs.rootContinuityBonus)
    // before re-multiplying, because that bonus is folded into basisIndep and
    // thus scaled by complexityFactor × augFactor (simple score subtraction is wrong).
    double basisIndep;

    double basisDep;            ///< Bass-dependent delta.
    double complexityFactor;    ///< complexityFactorMatrix[rootPc][tiePriority].
    double augFactor;           ///< augFactorMatrix[rootPc][tiePriority].

    // Additive terms (applied AFTER the cf × af multiplication).
    // Simple addition/subtraction by E2c is correct for all of these.
    double wCompleteBonus;      ///< 0 or kWComplete.
    double wSeqBonus;           ///< Identical across both cubes (neutral w.r.t. wDim).
    double wDimDelta;           ///< 0 in cellsWithoutWDim; >= 0 in cellsWithWDim.

    // Bass bonus, used for threshold de-inflation: threshold = (bestScore -
    // appliedBassBonus) * kScoreThresholdRatio. Must match what the scorer used.
    double appliedBassBonus;
};

/// Full per-region scoring snapshot. Populated inside analyzeChord() when
/// prefs.captureScoringSnapshot != nullptr. Contains nothing that is not
/// already computable from the analyzeChord() inputs; it exists only so E2c
/// does not have to re-run the full pitch scorer.
struct ScoringSnapshot {
    /// Scoring cubes for both the with-wDim and without-wDim variants.
    /// Layout: cells are stored in (bass, root, template) order — bass is the
    /// outer dimension (index bi), rootPc the middle (0..11), tiePriority the
    /// inner (0..N_templates-1). Total cells per cube:
    ///   bassCandidates.size() x 12 x N_templates  (typically <= 4 x 12 x 17 = 816).
    /// The two cubes share all fields except wDimDelta; they also share wSeqBonus
    /// (it is added before wDimDelta and is therefore identical in both variants).
    /// Pass B (step bonuses) is NOT reflected here — cells hold pre-step scores.
    /// E2c must re-run Pass B after re-scoring.
    std::vector<ScoringCell> cellsWithWDim;
    std::vector<ScoringCell> cellsWithoutWDim;

    /// Scorer's actual decisions (useful for E2c cross-check and debugging).
    int  chosenBassPc        { -1 };  ///< bassCandidates[winnerIdx].pc after quality guard
    bool acceptedWithWDim    { false }; ///< true iff the with-wDim variant was accepted
    int  winnerBassPcWith    { -1 };  ///< bass chosen by the with-wDim variant
    int  winnerBassPcWithout { -1 };  ///< bass chosen by the without-wDim variant

    /// Needed by E2c for w_seq / w_dim gate conditions.
    int  distinctPcs         { 0 };

    /// Mirrors analyzeChord()'s jointScoringEnabled flag; required by
    /// fn::wSeqBonus / fn::wDimBonus. Not in prefs (computed inside analyzeChord()).
    bool jointScoringEnabled { false };
};

} // namespace mu::composing::function
