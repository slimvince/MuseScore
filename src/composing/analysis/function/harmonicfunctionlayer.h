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
//                              scores (basisIndep — vertical evidence plus the
//                              node-local diatonicRootBonus; basisDep — nonBassAdjustment
//                              + appliedBassBonus), complexity/aug factors, w_complete,
//                              plus the vertical inversion-eligibility flags, plus region
//                              metadata. Packs them into a ScoringSnapshot and calls
//                              applyHarmonicFunction. As of Stage 3.3 the oracle is
//                              GENUINELY vertical: it selects NO winner and applies NONE
//                              of the progression signals — rootContinuity, resolution,
//                              the four inversion bonuses, w_seq / w_dim / step bonuses
//                              are ALL owned by the pipeline (the chordanalyzer.h temporal
//                              debt is cleared).
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
    // NOTE: no keyFifths/keyMode here by design. Key influence reaches the pipeline
    // frozen into ScoringCell::basisIndep (oracle) and the post-scoring gates via
    // ScoringSnapshot::{scale,keyTonicPc,keyMode} — never through the function context.
    // Do not add key fields here to build key-confidence scaling; it would be a no-op.
    // Scale the oracle's key-dependent terms instead. See cc_step3_key_investigation_report.md Part A.
    int previousRootPc { -1 };   ///< Root PC of the preceding region (-1 = unknown)
    int nextRootPc { -1 };       ///< Root PC of the following region (-1 = unknown)
    int previousBassPc { -1 };   ///< Bass PC of the preceding region (-1 = unknown).
                                  ///< Required by the Pass B step-in bonus.
    int nextBassPc     { -1 };   ///< Bass PC of the following region (-1 = unknown).
                                  ///< Required by the Pass B step-out bonus.

    // Stage 3.3 — temporal edges migrated from the oracle into the competition pipeline.
    // Forwarded verbatim from ChordTemporalContext so the pipeline can recompute the
    // bass-stepwise inversion bonuses (stepwiseBassInversion back-edge,
    // stepwiseBassLookahead forward/cold-lookahead edge) and the completeTriad edge gate
    // (OR-of-edges) that bassDependentContextualBonuses used to evaluate oracle-side.
    bool bassIsStepwiseFromPrevious { false };  ///< Bass steps from the predecessor region's bass.
    bool bassIsStepwiseToNext       { false };  ///< Bass steps to the successor region's bass (cold lookahead).

    // Step 1 redesign: free wiring — forwarded from ChordTemporalContext, no scoring logic yet
    analysis::ChordQuality previousQuality { analysis::ChordQuality::Unknown };
                                  ///< Quality of the preceding region's committed chord.
    std::array<int, 3> recentRootPcs { -1, -1, -1 };
                                  ///< Root PCs of the 3 most recent regions, most-recent first.
    int consecutiveBassStepwiseCount { 0 };
                                  ///< Consecutive regions (incl. this one) with stepwise bass.
    double regionMetricWeight { 1.0 };
                                  ///< Normalised metric strength of this region's onset.

    // Step 2 redesign: predecessor confidence channel — no scoring logic yet
    double previousWinnerScore        { 0.0 };
    double previousWinnerMargin       { -1.0 };
    double previousWinnerRootPcWeight { 0.0 };
    int    previousDistinctPcs        { 0 };
};

// -----------------------------------------------------------------------
// Function-layer constants — defined here because they are properties of the
// competition pipeline, not of the vertical pitch scorer.
// -----------------------------------------------------------------------

// Stage-5 fitter: these five progression-signal constants are mutable globals (was
// `inline constexpr`) so the optional parameter-override mechanism can register their
// addresses (paramoverride.h; registered in harmonicfunctionlayer.cpp). Byte-identical
// when no override is loaded — same literal initializers, read exactly as before; the
// override loader is the only writer. kWStepIn/kWStepOut/kWSeq/kWDim have static
// (constant) initializers, so they are initialized before kStepBudget's dynamic
// initializer reads them — no cross-TU init-order hazard. kStepBudget keeps the exact
// expression (not the literal 0.235) to preserve its last-bit IEEE value. See
// cowork_stage5_fitter_design.md D-6.
//
// kWStepIn adopted 0.10 -> 0.125 (Stage-5 Phase 2.2e, idiom-#2 fit; user-ratified 2026-07-05).
// This is the PRODUCTION/Default-carrier value (production has no preset-selection moment, so
// the global initializer IS the Default carrier — design O-11 iii). The Baroque carrier also
// ships 0.125 (batch_analyze.cpp). Jazz + Standard/Modal/Contemporary are pinned to 0.10 there;
// because kStepBudget is DERIVED from kWStepIn, those carriers re-derive it explicitly (a
// single-key applyGlobalOverride does NOT recompute — only the file loader does).
inline double kWSeq = 0.20;  ///< Sequential root-progression bonus (Iter 95)
inline double kWDim = 0.15;  ///< Dim/HalfDim leading-tone bonus (Iter 96)
inline double kWStepIn   = 0.125;  ///< Stepwise-bass step-in bonus (Pass B; 2.2e-adopted, was 0.10)
inline double kWStepOut  = 0.10;  ///< Stepwise-bass step-out bonus (Pass B)
inline double kStepBudget = kWStepIn + kWStepOut + 0.01;  ///< m7-family guard tolerance (DERIVED = 0.235; loader recomputes)

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
/// Stateless: the caller decides (via ScoringPhase) whether to apply it.
double wSeqBonus(int candRootPc, int nextRootPc, int distinctPcs,
                 bool jointScoringEnabled);

/// Diminished/HalfDim leading-tone bonus (+kWDim).
/// Rewards a Dim/HalfDim candidate whose root sits one semitone below nextRootPc.
/// Stateless: the caller decides (via ScoringPhase) whether to apply it.
double wDimBonus(int candRootPc, analysis::ChordQuality quality,
                 int nextRootPc, int distinctPcs,
                 bool jointScoringEnabled);

/// Stepwise-bass step-in bonus (+kWStepIn).
/// Root-position candidate whose bass moves by semitone/whole-tone FROM previousBassPc.
/// Stateless: the caller decides (via ScoringPhase) whether to apply it.
double wStepInBonus(int candBassPc, int rootPc,
                    bool jointScoringEnabled,
                    int previousBassPc);

/// Stepwise-bass step-out bonus (+kWStepOut).
/// Root-position candidate whose bass moves by semitone/whole-tone TO nextBassPc.
/// Stateless: the caller decides (via ScoringPhase) whether to apply it.
double wStepOutBonus(int candBassPc, int rootPc,
                     bool jointScoringEnabled,
                     int nextBassPc);

/// Resolution-bias edge (+resolutionBonus), migrated from the oracle in Stage 3.3.
/// Rewards a candidate sitting at the typical resolution target of the previous
/// chord's quality: prevDim→Maj/min a semitone up, prevHalfDim→Maj a P4 up,
/// prevAug→Maj/min at the same root. Folded into basisIndep before the cf × af multiply
/// (its historical home), so it is multiplied by complexityFactor × augFactor.
/// Returns 0 when no resolution relation holds (or the predecessor is unknown).
double resolutionEdgeBonus(int candRootPc, analysis::ChordQuality candQuality,
                           int previousRootPc, analysis::ChordQuality previousQuality,
                           double bonusValue);

// (inversionContextBonus is declared below ScoringCell — it takes a ScoringCell.)

// -----------------------------------------------------------------------
// Scoring snapshot — produced by analyzeChord() (the oracle) and consumed by
// applyHarmonicFunction() (the pipeline). It carries everything the pipeline
// needs and nothing that depends on progression context: every score field is
// purely vertical (no rootContinuity / w_seq / w_dim / step bonus folded in).
// -----------------------------------------------------------------------

/// One (bass, root, template) scoring cell, vertical-only.
/// Since Stage 3.3 the cell carries ONLY vertical/key pitch facts — every
/// progression signal (rootContinuity, resolution, the four inversion bonuses,
/// w_seq / w_dim / step bonuses) is recomposed by the pipeline. The pipeline
/// reconstructs the signal-inclusive score from the decomposed fields:
///   fullBasisIndep = basisIndep + resolutionEdgeBonus
///   fullBasisDep   = basisDep   + inversionContextBonus   (the capped 4-bonus sum)
///   score = (fullBasisIndep + rootContinuity + fullBasisDep) * complexityFactor * augFactor
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

    // Vertical pitch evidence PLUS the bass-INDEPENDENT diatonicRootBonus (a node-local
    // key fact). As of Stage 3.3 this is genuinely vertical: resolutionBonus — the one
    // progression signal it used to carry as oracle temporal debt — has migrated to the
    // pipeline (resolutionEdgeBonus), as has rootContinuityBonus before it. The pipeline
    // adds both before the cf × af multiply (matching the historical folding into basisIndep).
    double basisIndep;
    double basisDep;            ///< Bass-dependent delta: nonBassAdjustment + appliedBassBonus.
                                ///< Vertical as of Stage 3.3 — the §4.1b inversion bonuses
                                ///< have migrated to the pipeline (inversionContextBonus,
                                ///< gated by the two flags below + the temporal edges).
    double complexityFactor;    ///< complexityFactorMatrix[rootPc][tiePriority].
    double augFactor;           ///< augFactorMatrix[rootPc][tiePriority].

    double wCompleteBonus;      ///< 0 or kWComplete (joint, region-local — not a progression signal).

    /// Bass bonus, used for threshold de-inflation:
    ///   threshold = (bestScore - appliedBassBonus) * kScoreThresholdRatio.
    double appliedBassBonus;

    // Vertical inversion-eligibility flags (Stage 3.3). Pure pitch facts computed by the
    // oracle (supportsContextualInversionBonuses / qualifiesForCompleteTriadInversionBonus,
    // both ANDed with hasStructuralBass), so the pipeline can gate the migrated inversion
    // bonuses on the temporal edges. False on the single-tick / null-context path.
    bool supportsInversionBonuses { false };  ///< isInvertedMajMin: inverted Maj/Min/Aug/HalfDim, third sounding.
    bool qualifiesCompleteTriad   { false };  ///< complete inverted triad in a 3-PC texture (Maj/Min/Dim/Aug/HalfDim).
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
    /// The notated key signature (-7..+7) the region was analyzed under — the input to
    /// diatonicMaskFromFifths, i.e. to the key's own collection. Carried for the OI-170
    /// default-OFF signature-mask variant of the diatonic check; no committed path reads it.
    int                    keySigFifths { 0 };
};

/// Capped inversion-context bonus (the four §4.1b bonuses), migrated from the oracle in
/// Stage 3.3. Folded into basisDep before the cf × af multiply (its historical home).
/// Reproduces bassDependentContextualBonuses' accumulation EXACTLY — same term order
/// (completeTriad, stepwiseInversion, stepwiseLookahead, sameRoot) then the
/// maxTotalInversionContextBonus clamp — keyed on the cell's vertical eligibility flags
/// (cell.supportsInversionBonuses / cell.qualifiesCompleteTriad) and the temporal edges.
/// Returns 0 on the null-context path (all edges false, previousRootPc == -1).
double inversionContextBonus(const ScoringCell& cell,
                             int previousRootPc,
                             bool bassIsStepwiseFromPrevious,
                             bool bassIsStepwiseToNext,
                             const analysis::ChordAnalyzerPreferences& prefs);

// -----------------------------------------------------------------------
// Gate R — rcb bass-chord-tone guard. Declared here (exposed) so the decision
// branches and the (now DERIVED) template-membership masks can be unit-tested
// directly. The masks are derived at compile time from analysis::kTemplateIntervals
// (chordanalyzer.h) via makeTemplateMasks(), so kMasks is no longer a hand-sync site.
// See docs/scoring_model.md §4 "Gate R" / §9.
// -----------------------------------------------------------------------

/// Returns true iff `bassPc` is a tone of the candidate's template
/// (root / 3rd / 5th / 7th …) — i.e. `(bassPc - rootPc) mod 12` is in the template's
/// interval set. Returns false when the bass is foreign to the chord ("nonsense slash").
/// Conservative on unknown / out-of-range input: returns true (do not gate when unsure).
bool bassIsTemplateChordTone(int rootPc, int tiePriority, int bassPc) noexcept;

/// Gate R decision predicate: returns true iff `rootContinuityBonus` must be withheld
/// from this cell on STRUCTURAL grounds. The three structural conditions — all required:
///   (1) `rcb > 0`        — root continuity holds for this candidate,
///   (2) `basisDep <= 0`  — the candidate earned NO inversion credit (no inversion bonus
///                          fired, and no bass-root bonus applies),
///   (3) bass foreign to the candidate's template (bassIsTemplateChordTone == false).
///
/// Stage 3.3 redesign (reconstructed-credit, Cowork-ratified): condition (2) is the
/// "no inversion credit" discriminator. Before 3.3 it read the ORACLE's basisDep, which
/// carried the inversion bonuses (a cross-layer dependency, audit Finding 6). Now the
/// inversion bonuses are computed in the pipeline, so the pipeline passes the
/// RECONSTRUCTED full basisDep (cell.basisDep + inversionContextBonus) to the 3-arg
/// overload below — intra-layer, no oracle dependency. Byte-identical to the old proxy on
/// every quality (the discriminator was derivably `cappedInv == 0`, since the minimum
/// inversion bonus 0.40 strictly exceeds the maximum penalty 0.35; the literal
/// sounding-third pcWeight test diverged on Diminished completeTriad continuations — see
/// docs/decoder_design.md §6 amendment / docs/scoring_model.md §4 Gate R).
///
/// The 3-arg overload takes the basisDep value explicitly so the caller passes the
/// pipeline-reconstructed full basisDep. (Stage 3.4 removed the former 2-arg test-compat
/// overload that read `cell.basisDep` implicitly; tests now pass `cell.basisDep`
/// explicitly to the 3-arg form — the production entry point.)
///
/// The phase guard ("final-scoring correction only; never during segmentation") is NOT
/// part of this predicate — the rcbEdge() helper in harmonicfunctionlayer.cpp Pass A
/// gates the rcb-zeroing on ScoringPhase::Final.
bool gateRZeroesRootContinuity(const ScoringCell& cell, double basisDepValue,
                               double rcb) noexcept;

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
                           analysis::PostScoringGateContext*           gateCtx,
                           ScoringPhase                                phase = ScoringPhase::Final);

} // namespace mu::composing::function
