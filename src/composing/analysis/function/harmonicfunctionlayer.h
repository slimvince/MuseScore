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
//
// Competition pipeline — the SINGLE owner of winner selection.
//
// Architecture (scoring oracle vs competition pipeline; see docs/scoring_model.md
// §11):
//
//   analyzeChord()           — scoring ORACLE. Computes only what depends on the
//                              raw tones + key: per-(bass,root,template) vertical
//                              scores (basisIndep WITHOUT any progression signal,
//                              basisDep, complexity/aug factors, w_complete,
//                              appliedBassBonus) plus region metadata. Packs them
//                              into a ScoringSnapshot and calls applyHarmonicFunction.
//                              It selects NO winner and applies NO progression signal.
//
//   applyHarmonicFunction()  — competition PIPELINE. The sole place that applies
//                              progression signals (rootContinuity, w_seq, w_dim,
//                              step bonuses), runs the per-bass / cross-bass
//                              competition, selects the winner, computes the
//                              threshold + result cap + diff-root append, and fills
//                              the PostScoringGateContext. Because there is exactly
//                              one winner-selection pipeline, no replica can drift.
//
// E4 (planned): cadence detection and functional labeling layer on top of the
// already-final winner.

#pragma once

#include <array>
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
                                  ///< Required by the Pass B step-in bonus.
    int nextBassPc     { -1 };   ///< Bass PC of the following region (-1 = unknown).
                                  ///< Required by the Pass B step-out bonus.

    // Step 1 redesign: free wiring — forwarded from ChordTemporalContext, no scoring logic yet
    analysis::ChordQuality previousQuality { analysis::ChordQuality::Unknown };
                                  ///< Quality of the preceding region's committed chord.
    std::array<int, 3> recentRootPcs { -1, -1, -1 };
                                  ///< Root PCs of the 3 most recent regions, most-recent first.
    int consecutiveBassStepwiseCount { 0 };
                                  ///< Consecutive regions (incl. this one) with stepwise bass.
    double regionMetricWeight { 1.0 };
                                  ///< Normalised metric strength of this region's onset.
};

// -----------------------------------------------------------------------
// Function-layer constants — defined here because they are properties of the
// competition pipeline, not of the vertical pitch scorer.
// -----------------------------------------------------------------------

inline constexpr double kWSeq = 0.20;  ///< Sequential root-progression bonus (Iter 95)
inline constexpr double kWDim = 0.15;  ///< Dim/HalfDim leading-tone bonus (Iter 96)
inline constexpr double kWStepIn   = 0.10;  ///< Stepwise-bass step-in bonus (Pass B)
inline constexpr double kWStepOut  = 0.10;  ///< Stepwise-bass step-out bonus (Pass B)
inline constexpr double kStepBudget = kWStepIn + kWStepOut + 0.01;  ///< m7-family guard tolerance

/// Score-threshold ratio. results[] admits every candidate whose signal-inclusive
/// score is >= (winnerScore - winnerBassBonus) * kScoreThresholdRatio.
/// Moved here from chordanalyzer.cpp: the threshold is a function of the post-signal
/// scores, so it belongs to the competition pipeline.
inline constexpr double kScoreThresholdRatio = 0.75;

// -----------------------------------------------------------------------
// Progression-signal bonus functions.
// -----------------------------------------------------------------------

/// Root-continuity bonus.
/// Returns bonusValue when candidateRootPc == previousRootPc, else 0.
double rootContinuityBonus(int candidateRootPc, int previousRootPc,
                           double bonusValue);

/// Sequential root-motion bonus (+kWSeq).
/// Rewards a candidate whose root sits a P4 below nextRootPc (classic V→I).
double wSeqBonus(int candRootPc, int nextRootPc, int distinctPcs,
                 bool jointScoringEnabled, bool explorationMode);

/// Diminished/HalfDim leading-tone bonus (+kWDim).
/// Rewards a Dim/HalfDim candidate whose root sits one semitone below nextRootPc.
double wDimBonus(int candRootPc, analysis::ChordQuality quality,
                 int nextRootPc, int distinctPcs,
                 bool jointScoringEnabled, bool explorationMode);

/// Stepwise-bass step-in bonus (+kWStepIn).
/// Root-position candidate whose bass moves by semitone/whole-tone FROM previousBassPc.
double wStepInBonus(int candBassPc, int rootPc,
                    bool jointScoringEnabled, bool explorationMode,
                    int previousBassPc);

/// Stepwise-bass step-out bonus (+kWStepOut).
/// Root-position candidate whose bass moves by semitone/whole-tone TO nextBassPc.
double wStepOutBonus(int candBassPc, int rootPc,
                     bool jointScoringEnabled, bool explorationMode,
                     int nextBassPc);

// -----------------------------------------------------------------------
// Scoring snapshot — produced by analyzeChord() (the oracle) and consumed by
// applyHarmonicFunction() (the pipeline). It carries everything the pipeline
// needs and nothing that depends on progression context: every score field is
// purely vertical (no rootContinuity / w_seq / w_dim / step bonus folded in).
// -----------------------------------------------------------------------

/// One (bass, root, template) scoring cell, vertical-only.
/// The pipeline reconstructs the signal-inclusive score from the decomposed
/// fields:
///   score = (basisIndep + rootContinuity + basisDep) * complexityFactor * augFactor
///         + wCompleteBonus + w_seq [+ w_dim] [+ step bonuses (Pass B)]
struct ScoringCell {
    // Identifiers — locate the cell in the (bass, root, template) cube.
    int                    bassPc;
    int                    bassTpc;
    int                    rootPc;
    int                    tiePriority;        ///< Template index.
    analysis::ChordQuality quality;
    int                    intervalCount { 0 }; ///< templates[tiePriority].intervals.size();
                                                ///< Pass B m7-family guard: isMin7 ≡
                                                ///< quality==Minor && intervalCount==4.

    // Vertical pitch evidence — does NOT include rootContinuityBonus (the pipeline
    // adds it before the cf × af multiply, matching the historical folding into
    // basisIndep).
    double basisIndep;
    double basisDep;            ///< Bass-dependent delta (nonBass + §4.1b inversion bonuses).
    double complexityFactor;    ///< complexityFactorMatrix[rootPc][tiePriority].
    double augFactor;           ///< augFactorMatrix[rootPc][tiePriority].

    double wCompleteBonus;      ///< 0 or kWComplete (joint, region-local — not a progression signal).

    /// Bass bonus, used for threshold de-inflation:
    ///   threshold = (bestScore - appliedBassBonus) * kScoreThresholdRatio.
    double appliedBassBonus;
};

/// Full per-region scoring snapshot. Always produced internally by analyzeChord();
/// contains nothing that is not already computable from the analyzeChord() inputs.
///
/// Cells are stored in (bass, root, template) order — bass outer, rootPc middle
/// (0..11), tiePriority inner (0..N_templates-1). Each bass candidate has a
/// distinct bass PC, so a contiguous run of equal bassPc is one bass group.
struct ScoringSnapshot {
    std::vector<ScoringCell> cells;

    // Region-level facts (bass-independent).
    int  distinctPcs         { 0 };
    bool jointScoringEnabled { false };

    // gateCtx region metadata (copied verbatim into PostScoringGateContext by the
    // pipeline so applyPostScoringGates() has everything it needs).
    std::array<double, 12> pcWeight   {};
    std::array<int, 12>    tpcForPc   {};
    std::array<int, 7>     scale      {};
    int                    keyTonicPc { -1 };
    analysis::KeySigMode   keyMode    {};
};

/// Run the competition pipeline.
///
/// Inputs:  \p snapshot (full vertical-only candidate space, all basses),
///          \p ctx (neighbour roots/basses), \p prefs.
/// Outputs: \p results (filled from scratch — ranked top-3 + optional diff-root),
///          \p chosenResult (= results.front() when non-empty),
///          \p gateCtx (filled completely except tones/keySigFifths, which the
///          oracle sets directly; pass nullptr to skip).
void applyHarmonicFunction(const ScoringSnapshot&                      snapshot,
                           const HarmonicFunctionContext&              ctx,
                           const analysis::ChordAnalyzerPreferences&   prefs,
                           std::vector<analysis::ChordAnalysisResult>& results,
                           analysis::ChordAnalysisResult&              chosenResult,
                           analysis::PostScoringGateContext*           gateCtx);

} // namespace mu::composing::function
