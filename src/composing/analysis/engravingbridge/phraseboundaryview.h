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

// ── composing/analysis/engravingbridge — the owned phrase-boundary primitive ──
//
// Architectural Layer 1.5 (the notation-derived views): the SINGLE place that
// reads, from the notated surface alone, where a musical phrase ends. It lives
// beside the other Layer-1.5 views (spellingview / soundingAt / weightedPcView /
// pitchContextOverSpan), so every consumer of the per-region "ends a phrase"
// signal reads one owned primitive — never a per-site copy (the unification
// rule). Notation-only: key-, chord-, and function-agnostic by construction (the
// function layer's cadence detection CONSUMES phrase boundaries, so a boundary
// that depended on cadence would be circular).
//
// Spec: cowork_phrase_boundary_design.md (SIGNED) §4. Research/proportionality:
// cowork_phrase_boundary_methods.md + contrapunctus_findings.md addendum.
//
// THE GRADED MODEL (design §4). A surface-cue core plus deterministic
// notated-marker spikes, then peak-picking:
//   • §4.1 per eligible voice, three local-change CUE profiles — gap
//     (offset-to-onset silence), inter-onset (attack spacing), pitch-interval
//     (semitone leap) — each via the local-change rule (strength rises with both
//     the degree of local change and the size of the value), max-normalised over
//     the score, then a gap-dominant weighted sum (the per-voice surface strength).
//   • §4.3 the per-voice strengths are summed per (tau-merged) onset into the
//     TEXTURE strength — a point where many voices phrase together scores high.
//   • §4.2 deterministic marker spikes (fermata, breath/caesura, double/final/
//     repeat barline, mid-score key-signature change, subito tempo change /
//     written ritardando, all-voice-rest onset) add a fixed height >= the max
//     possible surface strength, so a marker dominates wherever it occurs.
//   • §4.4 peak-picking: a texture tick is a boundary iff it is a local maximum
//     AND above the Simple-Picker threshold (whole-profile mean + k*SD).
//
// CONSTANTS ARE PRECISION-PHASE (the firewall, design §11-1). The weights, k, the
// coincidence window tau, the minimum-silence duration, and the spike magnitude
// are left at the design's stated DEFAULTS here and are NOT tuned for accuracy —
// that is the precision phase. This file fixes the MECHANISM; the numbers move
// later. (Proportionality, user-ratified: the SOTA reference does no phrase/
// cadence detection and is still competitive, so this primitive is load-bearing
// for OUR cadence mechanism, not an accuracy requirement — build it right and stop.)
//
// CONSUMER STATUS (build §1 enumeration): every "ends a phrase" consumer is
// dormant or gated-off on the production path today — the joint-key re-key pass
// (regionanalyzer applyJointKeyWiring, gated on jointKeyWiringEnabled(), default
// OFF) and the batch_analyze --dump-cadence-anchor/--dump-modulation/
// --dump-joint-key diagnostics. So the graded definition is byte-identical on
// production; the strength becomes load-bearing only when the function layer
// (Layer 5) engages. (Step A retired the two hand-synced fermata scans into this
// owner byte-identically; Step B — this revision — replaces the fermata-only
// definition with the graded model without moving the consumer signature.)

#include <set>
#include <vector>

namespace mu::engraving {
class Score;
}

namespace mu::composing::analysis::engravingbridge {

// ── Precision-phase constants (design §11-1) — stated DEFAULTS, NOT tuned ──────
struct PhraseBoundaryParams {
    // §4.1 gap-dominant surface-cue weights. Ordering fixed by the design
    // (gap > inter-onset > pitch); the exact values are precision-phase.
    double wGap        = 0.50;
    double wInterOnset = 0.30;
    double wPitch      = 0.20;

    // §4.4 Simple-Picker threshold offset: a tick is a boundary when its texture
    // strength exceeds (whole-profile mean + k * standard deviation).
    double k = 1.0;

    // §4.3 voice-coincidence window (ticks). Onsets within tau merge into one
    // texture onset for the per-voice sum. Default 0 = exact-onset coincidence
    // (the chorale convention, where all voices reach the phrase-final note
    // together); precision-phase may raise it to absorb notational near-alignment.
    int tauTicks = 0;

    // §4.3 optional explicit coincidence weight beyond the plain per-voice sum.
    // 0 = plain sum (the coincidence already scores high because more voices add
    // more terms). A positive value boosts onsets where several voices peak at
    // once. Precision-phase; default off.
    double coincidenceWeight = 0.0;

    // §4.2 minimum duration (ticks) of an all-voice-rest span for it to spike
    // (filters tiny articulation gaps from real silences). Precision-phase.
    int minSilenceTicks = 240;   // eighth note at 480 ticks / quarter

    // §4.2 marker spike height = spikeCeilingFactor * (#voices) * (sum of
    // surface-cue weights). The factor is > 1 so a marker STRICTLY EXCEEDS the
    // theoretical maximum texture surface strength (a surface peak can reach the
    // ceiling when every voice's cue maxes and coincides), making a marker dominate
    // and clear the peak-picking threshold by construction. Precision-phase.
    double spikeCeilingFactor = 1.5;
};

// ── Outputs (design §3 "Produces") ────────────────────────────────────────────

/// One eligible voice's own phrase-boundary strength profile (design §4.3): the
/// gap-dominant weighted sum of that voice's three normalised local-change cues,
/// sampled at the voice's own onsets. `onsets[i]` carries strength `strength[i]`.
struct VoiceBoundaryProfile {
    int              staff = 0;
    int              voice = 0;
    std::vector<int>    onsets;    ///< the voice's event onsets (ascending), one per sampled point
    std::vector<double> strength;  ///< per-onset combined surface strength (parallel to onsets)
};

/// The full phrase-boundary profile of a score (design §3). Exposes BOTH the
/// per-voice strengths (each voice's own phrasing) and the texture profile (the
/// aggregate the cadence gate consumes), plus the picked boundary ticks.
struct PhraseBoundaryProfile {
    std::vector<VoiceBoundaryProfile> perVoice;   ///< §4.3 per-eligible-voice profiles
    std::vector<int>    textureTicks;             ///< §4.3/§4.4 texture grid ticks (ascending, unique)
    std::vector<double> textureStrength;          ///< texture combined strength incl. marker spikes (parallel)
    std::set<int>       pickedTicks;              ///< §4.4 peak-picked phrase-boundary ticks
};

// ── Pure local-change helpers (design §4.1; exposed for oracle tests) ──────────

/// A change-ratio in [0,1]: |a - b| / (a + b). Defined as 0 when a + b == 0
/// (no values, no change).
double changeRatio(double a, double b);

/// The per-point local-change strengths of a value sequence (design §4.1): for
/// value `v[i]` with neighbours `v[i-1]` (left) and `v[i+1]` (right),
/// `strength[i] = v[i] * (leftChangeRatio + rightChangeRatio)`. So strength rises
/// with both the degree of local change AND the size of the value. A missing
/// neighbour (the first/last point) contributes a 0 change-ratio on that side
/// (one-sided at the ends). Returns a vector the same length as `values`.
std::vector<double> localChangeProfile(const std::vector<double>& values);

/// Divide a profile by its own maximum (max-normalisation to [0,1], design §4.1).
/// A non-positive maximum (all zero / empty) leaves the profile unchanged (all 0).
void maxNormalizeInPlace(std::vector<double>& profile);

/// Simple-Picker peak-picking (design §4.4): the indices of @p strength that are
/// both a local maximum (greater than each existing immediate neighbour) AND above
/// the whole-profile threshold mean + k * standard-deviation. So a low-weighted
/// single bump among real peaks does NOT clear the (peak-elevated) threshold, while
/// a marker spike does. Returns the ascending picked indices.
std::vector<int> pickPeaks(const std::vector<double>& strength, double k);

// ── The primitive ─────────────────────────────────────────────────────────────

/// Compute the full graded phrase-boundary profile of @p score (design §4) at the
/// given precision-phase constants (defaults per §11-1). Notation only.
PhraseBoundaryProfile computePhraseBoundaryProfile(const mu::engraving::Score* score,
                                                   const PhraseBoundaryParams& params = {});

/// The picked phrase-boundary ticks of @p score — the consumer-facing API (the
/// single owned source the dormant/gated "ends a phrase" consumers read). Equals
/// `computePhraseBoundaryProfile(score).pickedTicks`. Returns an empty set for a
/// null score.
std::set<int> phraseBoundaryTicks(const mu::engraving::Score* score);

} // namespace mu::composing::analysis::engravingbridge
