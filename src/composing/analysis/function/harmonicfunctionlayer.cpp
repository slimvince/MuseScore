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

// harmonicfunctionlayer.cpp

#include "harmonicfunctionlayer.h"
#include "../param/paramoverride.h"   // Stage-5 fitter: optional constant override (D-6)

#include <algorithm>
#include <array>
#include <cstdint>
#include <limits>

namespace mu::composing::function {

using analysis::ChordQuality;

// ── Stage-5 fitter: register the progression-signal constants (G6) ───────────
// Byte-identical when no override file is loaded (the loader is the only writer).
// This TU is odr-used (it defines the bonus functions), so the registration runs
// at static-init. kStepBudget is registered too so the rider can pin it; the loader
// recomputes it from kWStepIn/kWStepOut when those move and kStepBudget is not pinned.
static const bool s_registerProgressionParams = [] {
    namespace P = mu::composing::params;
    P::registerDouble("kWSeq",       &kWSeq);
    P::registerDouble("kWDim",       &kWDim);
    P::registerDouble("kWStepIn",    &kWStepIn);
    P::registerDouble("kWStepOut",   &kWStepOut);
    P::registerDouble("kStepBudget", &kStepBudget);
    return true;
}();

// ── Progression-signal bonus functions ──────────────────────────────────────

double rootContinuityBonus(int candidateRootPc, int previousRootPc,
                           double bonusValue)
{
    return (candidateRootPc == previousRootPc) ? bonusValue : 0.0;
}

double wSeqBonus(int candRootPc, int nextRootPc, int distinctPcs,
                 bool jointScoringEnabled)
{
    if (!jointScoringEnabled) return 0.0;
    if (nextRootPc < 0 || distinctPcs < 4) return 0.0;
    const int delta = ((nextRootPc - candRootPc) % 12 + 12) % 12;
    return (delta == 5) ? kWSeq : 0.0;
}

double wDimBonus(int candRootPc, ChordQuality quality,
                 int nextRootPc, int distinctPcs,
                 bool jointScoringEnabled)
{
    if (!jointScoringEnabled) return 0.0;
    if (nextRootPc < 0 || distinctPcs < 4) return 0.0;
    if (quality != ChordQuality::Diminished && quality != ChordQuality::HalfDiminished) return 0.0;
    const int delta = ((nextRootPc - candRootPc) % 12 + 12) % 12;
    return (delta == 1) ? kWDim : 0.0;
}

namespace {

bool isSemitoneOrToneStep(int interval)
{
    return interval == 1 || interval == 2 || interval == 10 || interval == 11;
}

} // namespace

double wStepInBonus(int candBassPc, int rootPc,
                    bool jointScoringEnabled,
                    int previousBassPc)
{
    if (!jointScoringEnabled) return 0.0;
    if (candBassPc != rootPc) return 0.0;
    const int prev = previousBassPc;
    if (prev < 0 || prev == candBassPc) return 0.0;
    const int delta = ((candBassPc - prev) % 12 + 12) % 12;
    return isSemitoneOrToneStep(delta) ? kWStepIn : 0.0;
}

double wStepOutBonus(int candBassPc, int rootPc,
                     bool jointScoringEnabled,
                     int nextBassPc)
{
    if (!jointScoringEnabled) return 0.0;
    if (candBassPc != rootPc) return 0.0;
    const int next = nextBassPc;
    if (next < 0 || next == candBassPc) return 0.0;
    const int delta = ((next - candBassPc) % 12 + 12) % 12;
    return isSemitoneOrToneStep(delta) ? kWStepOut : 0.0;
}

// ── Migrated oracle temporal signals (Stage 3.3) ─────────────────────────────
// resolutionEdgeBonus + inversionContextBonus reproduce, term-for-term and in the same
// arithmetic, what bassIndependentContextualBonuses (resolution) and
// bassDependentContextualBonuses (the four inversion bonuses) used to compute oracle-side.
// They are folded into basisIndep / basisDep INSIDE the cf × af multiply (their historical
// homes), so they are multiplicatively scaled exactly as before — see Pass A.

double resolutionEdgeBonus(int candRootPc, ChordQuality candQuality,
                           int previousRootPc, ChordQuality previousQuality,
                           double bonusValue)
{
    if (previousQuality == ChordQuality::Unknown || previousRootPc < 0) {
        return 0.0;
    }
    // Mutually exclusive on previousQuality, so at most one branch contributes — exactly
    // the three `score += rb` cases of the old bassIndependentContextualBonuses helper.
    double score = 0.0;
    if (previousQuality == ChordQuality::Diminished
            && (candQuality == ChordQuality::Major || candQuality == ChordQuality::Minor)
            && candRootPc == (previousRootPc + 1) % 12) {
        score += bonusValue;
    }
    if (previousQuality == ChordQuality::HalfDiminished
            && candQuality == ChordQuality::Major
            && candRootPc == (previousRootPc + 5) % 12) {
        score += bonusValue;
    }
    if (previousQuality == ChordQuality::Augmented
            && (candQuality == ChordQuality::Major || candQuality == ChordQuality::Minor)
            && candRootPc == previousRootPc) {
        score += bonusValue;
    }
    return score;
}

double inversionContextBonus(const ScoringCell& cell,
                             int previousRootPc,
                             bool bassIsStepwiseFromPrevious,
                             bool bassIsStepwiseToNext,
                             const analysis::ChordAnalyzerPreferences& prefs)
{
    // The vertical eligibility (isInvertedMajMin / qualifiesCompleteTriad, both ANDed
    // with hasStructuralBass) is precomputed by the oracle into the cell flags; the
    // `context &&` guard of the old helper is reproduced by the null-context path leaving
    // every edge below false / previousRootPc == -1, which zeroes the sum.
    const bool hasStepwiseBassEvidence =
        bassIsStepwiseFromPrevious || bassIsStepwiseToNext;
    double sum = 0.0;

    if (hasStepwiseBassEvidence && cell.qualifiesCompleteTriad) {
        sum += prefs.completeTriadInversionBonus;
    }

    if (cell.supportsInversionBonuses) {
        if (bassIsStepwiseFromPrevious) {
            sum += prefs.stepwiseBassInversionBonus;
        }
        if (bassIsStepwiseToNext) {
            sum += prefs.stepwiseBassLookaheadBonus;
        }
        if (previousRootPc != -1 && previousRootPc == cell.rootPc) {
            sum += prefs.sameRootInversionBonus;
        }
    }

    return std::min(sum, prefs.maxTotalInversionContextBonus);
}

// ── Gate R — rcb bass-chord-tone guard (definitions; declared in the header) ──

/// Gate R helper: returns true if bassPc is a tone of the candidate's template
/// (root / 3rd / 5th / 7th …), false if the bass is foreign to the candidate's
/// chord (a "nonsense slash" voicing). Used to withhold rootContinuityBonus from
/// a candidate whose own bass cannot belong to it. See docs/scoring_model.md §4
/// "Gate R" and §9 (5th atomic-update site).
///
/// Conservative on unknown / out-of-range inputs (returns true — do not gate if
/// unsure).
///
/// kMasks is DERIVED at compile time from the single canonical interval source
/// analysis::kTemplateIntervals (chordanalyzer.h) via analysis::makeTemplateMasks() — the
/// SAME interval data the scorer's `templates` TemplateDef array is built from. It can no
/// longer be hand-typed wrong or drift from the templates (the audit-Q1.3 hazard: a
/// wrong/zero mask silently disables Gate R for that template, with no compile error).
/// Adding a template therefore means editing ONE interval source (kTemplateIntervals) —
/// there is no separate mask to keep in sync. Every template includes interval 0 (the root).
bool bassIsTemplateChordTone(int rootPc, int tiePriority, int bassPc) noexcept
{
    if (rootPc < 0 || bassPc < 0 || tiePriority < 0
        || static_cast<std::size_t>(tiePriority) >= analysis::kTemplateCount) {
        return true;
    }
    const int interval = ((bassPc - rootPc) % 12 + 12) % 12;

    // Bit i set ⇔ semitone interval i (from root) is a template tone — derived from
    // analysis::kTemplateIntervals (chordanalyzer.h), not hand-typed.
    static constexpr std::array<uint16_t, analysis::kTemplateCount> kMasks =
        analysis::makeTemplateMasks();
    static_assert(kMasks.size() == analysis::kTemplateCount,
                  "kMasks must mirror analysis::kTemplateCount templates");

    // Compile-time byte-identity proof against the original hand-typed Gate R masks
    // (kMasks-derive refactor §3). If an edit to kTemplateIntervals changes any mask, THIS
    // fails to compile — the derivation can never silently alter Gate R behaviour.
    static_assert(kMasks[0]  == 0x0091 && kMasks[1]  == 0x0891 && kMasks[2]  == 0x0491
               && kMasks[3]  == 0x0451 && kMasks[4]  == 0x0089 && kMasks[5]  == 0x0489
               && kMasks[6]  == 0x0049 && kMasks[7]  == 0x0461 && kMasks[8]  == 0x0449
               && kMasks[9]  == 0x0111 && kMasks[10] == 0x0511 && kMasks[11] == 0x0085
               && kMasks[12] == 0x04A1 && kMasks[13] == 0x08A1 && kMasks[14] == 0x0521
               && kMasks[15] == 0x00C1 && kMasks[16] == 0x0081,
                  "derived kMasks must be byte-identical to the original hand-typed values");

    return (kMasks[static_cast<size_t>(tiePriority)] & (1u << interval)) != 0;
}

/// Gate R decision — see the header for the three-condition structural contract and the
/// Stage 3.3 reconstructed-credit redesign. The phase guard ("final-scoring only") lives
/// at the call site, not here. Encodes the structural guard so the production call site
/// and the unit tests share one definition.
///
/// 3-arg overload: the production pipeline passes the RECONSTRUCTED full basisDep
/// (cell.basisDep + inversionContextBonus) for condition (2), so Gate R reads the cell's
/// total inversion credit without any cross-layer dependency on the oracle. Byte-identical
/// to the historical proxy (which read the oracle's then-inversion-bearing basisDep).
bool gateRZeroesRootContinuity(const ScoringCell& cell, double basisDepValue,
                               double rcb) noexcept
{
    return rcb > 0.0 && basisDepValue <= 0.0
           && !bassIsTemplateChordTone(cell.rootPc, cell.tiePriority, cell.bassPc);
}

// ── Competition pipeline ────────────────────────────────────────────────────

namespace {

/// rcb back-edge — the rootContinuity transition edge from the committed predecessor
/// to this candidate, with the Gate R structural guard absorbed (Stage 3.4). Returns
/// the rcb value that enters `basisIndep`.
///
/// Gate R withholds rcb from a BARE-ROOT continuation whose bass is foreign to the
/// candidate's own chord tones. Two conditions, both required:
///   (a) fullBasisDep <= 0 — the candidate earned NO inversion credit: no inversion
///       bonus fired (its third is not sounding, or the temporal edge is absent) and no
///       bass-root bonus applies. Given rcb>0 (root continuity), a legitimately
///       inverted/extended slash voicing has a sounding third, which fires
///       sameRootInversionBonus (cappedInv>0) → fullBasisDep>0; only a bare-root match
///       scores 0. (Stage 3.3 reconstructed-credit: fullBasisDep = cell.basisDep +
///       cappedInv, computed by Pass A; the discriminator is provably `cappedInv == 0`,
///       since the minimum inversion bonus 0.40 > maximum penalty 0.35 — intra-layer,
///       byte-identical to the historical oracle-basisDep proxy.)
///   (b) bass foreign to the template — the bass cannot belong to this chord.
/// Together these isolate the "nonsense slash" continuation (Δ=+7b cluster:
/// bwv245.28/296/320, bass = M6 of the continued root) and spare legitimate extended
/// voicings such as Cm7add11/F (third sounding, cappedInv>0). See docs/scoring_model.md
/// §4 Gate R.
///
/// Phase gate (applyProgressionSignals): rcb is NOT suppressed during segmentation
/// exploration — segmentation already depends on it, and letting Gate R perturb rcb
/// there shifts region boundaries (caught at bwv355 m15). Gate R is a final-scoring
/// correction only; the `&& applyProgressionSignals` order matches the historical call
/// site exactly (both operands are side-effect-free, so the result is invariant).
double rcbEdge(const ScoringCell& cell, double fullBasisDep, int previousRootPc,
               const analysis::ChordAnalyzerPreferences& prefs,
               bool applyProgressionSignals) noexcept
{
    double rcb = rootContinuityBonus(cell.rootPc, previousRootPc,
                                     prefs.rootContinuityBonus);
    if (gateRZeroesRootContinuity(cell, fullBasisDep, rcb) && applyProgressionSignals) {
        rcb = 0.0;
    }
    return rcb;
}

/// One per-bass working candidate: a RawCandidate plus the intervalCount the
/// Pass B m7-family guard needs (RawCandidate does not carry it).
struct WorkCand {
    double                 score;
    double                 appliedBassBonus;
    int                    rootPc;
    analysis::ChordQuality quality;
    int                    tiePriority;
    double                 wDimDelta;
    int                    intervalCount;
};

analysis::RawCandidate toRaw(const WorkCand& c)
{
    return analysis::RawCandidate{ c.score, c.appliedBassBonus, c.rootPc,
                                   c.quality, c.tiePriority, c.wDimDelta };
}

/// Pass B — step bonus with surgical first-inversion-m7-family guard.
/// Identical logic to the historical analyzeChord lambda: for each root-position
/// non-Power candidate eligible for a step bonus, suppress both step bonuses when a
/// competitor at (candBassPc-3) mod 12 of quality {HalfDiminished, Diminished,
/// Min7} scores within kStepBudget of this candidate's unbonused score.
void applyStepBonusGuard(std::vector<WorkCand>& perBass, int candBassPc,
                         const ScoringSnapshot& snapshot,
                         const HarmonicFunctionContext& ctx)
{
    const int compRootPc = ((candBassPc - 3) % 12 + 12) % 12;
    for (auto& cand : perBass) {
        if (cand.rootPc != candBassPc) {
            continue;  // step bonus is root-position-only (helpers also enforce)
        }
        if (cand.quality == ChordQuality::Power) {
            continue;
        }
        const double stepIn  = wStepInBonus(candBassPc, cand.rootPc,
                                            snapshot.jointScoringEnabled,
                                            ctx.previousBassPc);
        const double stepOut = wStepOutBonus(candBassPc, cand.rootPc,
                                             snapshot.jointScoringEnabled,
                                             ctx.nextBassPc);
        if (stepIn == 0.0 && stepOut == 0.0) {
            continue;
        }

        bool blocked = false;
        for (const auto& other : perBass) {
            if (other.rootPc != compRootPc) {
                continue;
            }
            const bool isMin7 = (other.quality == ChordQuality::Minor)
                                && (other.intervalCount == 4);
            const bool relevantQuality = (other.quality == ChordQuality::HalfDiminished)
                                         || (other.quality == ChordQuality::Diminished)
                                         || isMin7;
            if (!relevantQuality) {
                continue;
            }
            if (other.score >= cand.score - kStepBudget) {
                blocked = true;
                break;
            }
        }
        if (!blocked) {
            cand.score += stepIn + stepOut;
        }
    }
}

} // namespace

void applyHarmonicFunction(const ScoringSnapshot&                      snapshot,
                           const HarmonicFunctionContext&              ctx,
                           const analysis::ChordAnalyzerPreferences&   prefs,
                           std::vector<analysis::ChordAnalysisResult>& results,
                           analysis::ChordAnalysisResult&              chosenResult,
                           analysis::PostScoringGateContext*           gateCtx,
                           ScoringPhase                                phase)
{
    using analysis::RawCandidate;

    results.clear();

    // Single control point for the former explorationMode dual-path. In the
    // Segmentation phase the progression signals (w_seq / w_dim / step bonuses) are not
    // applied and Gate R is skipped; rootContinuityBonus stays active (segmentation
    // depends on it). In the Final phase every signal is active. The bonus functions and
    // Gate R are now stateless — the phase is consulted only here.
    const bool applyProgressionSignals = (phase == ScoringPhase::Final);

    // ── Re-score every cell with progression signals; run the competition ─────
    //
    // For each bass group, build the with-wDim and without-wDim variants (Pass A),
    // run the step bonus + surgical guard (Pass B), take each variant's local best
    // (Pass C), and track the global best per variant across all basses.
    double globalBestScoreWith    = -std::numeric_limits<double>::infinity();
    double globalBestScoreWithout = -std::numeric_limits<double>::infinity();
    std::vector<WorkCand> bestPerBassWith;
    std::vector<WorkCand> bestPerBassWithout;
    int winBassPcWith     = -1, winBassTpcWith     = -1;
    int winBassPcWithout  = -1, winBassTpcWithout  = -1;

    size_t i = 0;
    const size_t nCells = snapshot.cells.size();
    while (i < nCells) {
        const int groupBassPc  = snapshot.cells[i].bassPc;
        const int groupBassTpc = snapshot.cells[i].bassTpc;

        std::vector<WorkCand> perBassWith;
        std::vector<WorkCand> perBassWithout;

        // Pass A — vertical score + migrated temporal signals + rootContinuity
        //          + w_complete + w_seq [+ w_dim].
        while (i < nCells && snapshot.cells[i].bassPc == groupBassPc) {
            const ScoringCell& cell = snapshot.cells[i];

            // ── Migrated oracle temporal signals (Stage 3.3) ──────────────────────
            // resolution + the four inversion bonuses moved out of the oracle into the
            // pipeline. They are folded back into basisIndep / basisDep BEFORE the
            // cf × af multiply — their historical positions — so the score arithmetic is
            // unchanged. fullBasisDep is byte-identical to the oracle's pre-3.3 basisDep
            // (bb and the inversion sum are mutually exclusive, so the reassociation is
            // exact); resolution into fullBasisIndep is a ≤1-ULP reassociation confined to
            // non-tie Maj/Min cells (corpus A/B is the proof obligation; see report §1).
            const double resolution = resolutionEdgeBonus(
                cell.rootPc, cell.quality, ctx.previousRootPc, ctx.previousQuality,
                prefs.resolutionBonus);
            const double cappedInv = inversionContextBonus(
                cell, ctx.previousRootPc, ctx.bassIsStepwiseFromPrevious,
                ctx.bassIsStepwiseToNext, prefs);
            const double fullBasisIndep = cell.basisIndep + resolution;
            const double fullBasisDep   = cell.basisDep + cappedInv;

            // rcb back-edge (root continuity from the committed predecessor), with the
            // Gate R structural guard absorbed inside rcbEdge() — see its definition for
            // the reconstructed-credit rationale and the Δ=+7b discriminator. The phase
            // condition is folded in unchanged (rcb is NOT suppressed during segmentation).
            const double rcb = rcbEdge(cell, fullBasisDep, ctx.previousRootPc, prefs,
                                       applyProgressionSignals);
            const double newBasisIndep = fullBasisIndep + rcb;
            double scoreNoWDim = (newBasisIndep + fullBasisDep)
                                 * cell.complexityFactor * cell.augFactor;
            scoreNoWDim += cell.wCompleteBonus;
            scoreNoWDim += applyProgressionSignals
                ? wSeqBonus(cell.rootPc, ctx.nextRootPc, snapshot.distinctPcs,
                            snapshot.jointScoringEnabled)
                : 0.0;
            const double wDimDelta = applyProgressionSignals
                ? wDimBonus(cell.rootPc, cell.quality, ctx.nextRootPc,
                            snapshot.distinctPcs, snapshot.jointScoringEnabled)
                : 0.0;

            perBassWith.push_back({ scoreNoWDim + wDimDelta, cell.appliedBassBonus,
                                    cell.rootPc, cell.quality, cell.tiePriority,
                                    wDimDelta, cell.intervalCount });
            perBassWithout.push_back({ scoreNoWDim, cell.appliedBassBonus,
                                       cell.rootPc, cell.quality, cell.tiePriority,
                                       0.0, cell.intervalCount });
            ++i;
        }

        // Pass B — step bonus + surgical guard, independently per variant. Suppressed in
        // the Segmentation phase: this is the former explorationMode behaviour, now
        // explicit. The wStep* helpers are stateless, so the phase suppression lives here
        // rather than inside them.
        if (applyProgressionSignals) {
            applyStepBonusGuard(perBassWith, groupBassPc, snapshot, ctx);
            applyStepBonusGuard(perBassWithout, groupBassPc, snapshot, ctx);
        }

        // Pass C — local best per variant; promote the winning bass globally.
        double localBestWith = -std::numeric_limits<double>::infinity();
        for (const auto& c : perBassWith) {
            if (c.score > localBestWith) { localBestWith = c.score; }
        }
        double localBestWithout = -std::numeric_limits<double>::infinity();
        for (const auto& c : perBassWithout) {
            if (c.score > localBestWithout) { localBestWithout = c.score; }
        }
        if (localBestWith > globalBestScoreWith) {
            globalBestScoreWith = localBestWith;
            bestPerBassWith     = std::move(perBassWith);
            winBassPcWith       = groupBassPc;
            winBassTpcWith      = groupBassTpc;
        }
        if (localBestWithout > globalBestScoreWithout) {
            globalBestScoreWithout = localBestWithout;
            bestPerBassWithout     = std::move(perBassWithout);
            winBassPcWithout       = groupBassPc;
            winBassTpcWithout      = groupBassTpc;
        }
    }

    // ── Post-bonus quality guard (Iter 97a-v3) ───────────────────────────────
    // Accept the with-wDim result only if its global winner is Dim/HalfDim;
    // otherwise the bonus caused cross-bass contamination — use the without-wDim
    // result.
    ChordQuality postBonusWinnerQuality = ChordQuality::Unknown;
    double postBonusBestScore = -std::numeric_limits<double>::infinity();
    for (const auto& c : bestPerBassWith) {
        if (c.score > postBonusBestScore) {
            postBonusBestScore = c.score;
            postBonusWinnerQuality = c.quality;
        }
    }
    const bool acceptPostBonus = (postBonusWinnerQuality == ChordQuality::Diminished
                                  || postBonusWinnerQuality == ChordQuality::HalfDiminished);

    std::vector<WorkCand>& chosenPerBass = acceptPostBonus ? bestPerBassWith : bestPerBassWithout;
    const int winBassPc  = acceptPostBonus ? winBassPcWith  : winBassPcWithout;
    const int winBassTpc = acceptPostBonus ? winBassTpcWith : winBassTpcWithout;

    // ── Sort the winning bass's candidates ───────────────────────────────────
    std::sort(chosenPerBass.begin(), chosenPerBass.end(),
              [](const WorkCand& a, const WorkCand& b) -> bool {
                  if (a.score != b.score)             return a.score > b.score;
                  if (a.tiePriority != b.tiePriority) return a.tiePriority < b.tiePriority;
                  return a.rootPc < b.rootPc;
              });

    // ── Threshold ────────────────────────────────────────────────────────────
    const double bestRawScore = chosenPerBass.empty() ? 0.0 : chosenPerBass.front().score;
    const double winnerBassBonus = chosenPerBass.empty() ? 0.0
                                                         : chosenPerBass.front().appliedBassBonus;
    const double threshold = (bestRawScore - winnerBassBonus) * kScoreThresholdRatio;

    // ── Build results[] ──────────────────────────────────────────────────────
    const analysis::BuildChordResultContext buildCtx{
        snapshot.pcWeight, snapshot.tpcForPc, winBassPc, winBassTpc,
        snapshot.keyTonicPc, snapshot.keyMode, snapshot.scale };
    const auto buildResult = [&](const WorkCand& rc) -> analysis::ChordAnalysisResult {
        return analysis::buildChordResult(toRaw(rc), buildCtx, prefs);
    };

    for (const WorkCand& rc : chosenPerBass) {
        if (results.size() >= 3) {
            break;
        }
        if (rc.score < threshold) {
            break;
        }
        results.push_back(buildResult(rc));
    }

    // ── Guaranteed inversion alternative (diff-root append) ───────────────────
    if (!results.empty()
        && winBassPc >= 0
        && prefs.inversionSuspicionMargin > 0.0
        && results.front().identity.rootPc == winBassPc)
    {
        const int winnerRootPc = results.front().identity.rootPc;
        const bool hasDiffRoot = std::any_of(results.begin(), results.end(),
            [winnerRootPc](const analysis::ChordAnalysisResult& r) {
                return r.identity.rootPc != winnerRootPc;
            });
        if (!hasDiffRoot) {
            for (const WorkCand& rc : chosenPerBass) {
                if (rc.score < threshold)      { break; }
                if (rc.rootPc == winnerRootPc) { continue; }
                results.push_back(buildResult(rc));
                break;
            }
        }
    }

    if (!results.empty()) {
        chosenResult = results.front();
    }

    // ── Fill gateCtx ─────────────────────────────────────────────────────────
    // Bass-independent metadata is copied from the snapshot; bass-dependent fields
    // (bassPc, bassTpc, threshold, rawCandidates) come from the chosen winner.
    // tones / keySigFifths are set by analyzeChord (not part of the snapshot).
    if (gateCtx) {
        gateCtx->pcWeight    = snapshot.pcWeight;
        gateCtx->tpcForPc    = snapshot.tpcForPc;
        gateCtx->scale       = snapshot.scale;
        gateCtx->keyTonicPc  = snapshot.keyTonicPc;
        gateCtx->keyMode     = snapshot.keyMode;
        gateCtx->bassPc      = winBassPc;
        gateCtx->bassTpc     = winBassTpc;
        gateCtx->distinctPcs = snapshot.distinctPcs;
        gateCtx->threshold   = threshold;

        std::vector<RawCandidate> raw;
        raw.reserve(chosenPerBass.size());
        for (const WorkCand& c : chosenPerBass) {
            raw.push_back(toRaw(c));
        }
        gateCtx->rawCandidates = std::move(raw);
    }
}

} // namespace mu::composing::function
