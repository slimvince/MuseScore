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

// ── composing/analysis/function/forwardoverride ──────────────────────────────
//
// Architectural Layer 5 (FUNCTION) — THE CONFIDENCE-WEIGHTED FORWARD OVERRIDE: the
// ONE reusable mechanism §8 (and §9-D7) specifies, by which a later layer's
// independent evidence reconciles with an earlier layer's inference. Spec:
// cowork_layer5_function_design.md (SIGNED) §8 + §5.4. Build plan:
// cowork_phase5c_l5_build_plan.md Step 3.
//
// §8's four-case model:
//   1. later evidence agrees with a confident earlier inference  → reinforce;
//   2. earlier layer was uncertain and said so                   → select (§5.5);
//   3. earlier layer was uncertain, later evidence still cannot   → carry honestly;
//   4. later evidence CONTRADICTS a *confident* earlier inference → OVERRIDE iff the
//      contradiction is DECISIVE — its strength crosses a threshold that SCALES with
//      the earlier layer's confidence (a well-founded confident commit demands
//      decisively stronger contradicting evidence than a borderline one).
//
// Cases 2 and 4, WHEN THEY FIRE, are realized by ONE mechanism: a LOCALIZED, FORWARD,
// convergence-bounded recompute — the dependent reading is re-run over the AFFECTED
// REGION ONLY with the corrected fact, and the overturned decision is CLOSED for that
// pass (a one-pass closure flag), so the recompute it triggers — and any later
// override in the same pass — cannot re-target it. The recompute therefore terminates
// after one localized forward re-run; it is NEVER a backward request and NEVER a loop.
//
// THIS UNIT IS THAT MECHANISM, built ONCE here so its two function-layer instances
// reuse it: the FINE-GRAIN CHORD OVERRIDE (§5.5 case-4 / §10, built in functionresolver
// at this step) and the CADENCE-CONFIRMED MODULATION RECOMPUTE (§5.4, Step 4). Further
// channels (future layers) are added as further instances of the same mechanism.
//
// WHAT THIS IS NOT (§8): a backward re-derivation or a full joint cross-layer search —
// that was measured inert. The architecture spends its effort on good FORWARD evidence
// (calibrated confidence + ranked alternatives), not on cycling. So this mechanism is
// forward-only by construction: the recompute sweeps a bounded slice range in forward
// order, never revisits a slice, and never calls upstream.
//
// CONSTANTS ARE PRECISION-PHASE (the firewall, build §4). The override threshold's
// base bar and confidence-scaling are DEFAULT seeds here and are NOT tuned for
// accuracy — that is Phase B. Only the DIRECTION is fixed: the bar to overturn rises
// monotonically with the earlier layer's confidence (more-confident ⇒ harder to
// overturn); the tie-direction is fixed (at the exact bar the incumbent holds).
//
// DORMANT (build §6): this module has NO production consumer — nothing in src/ calls
// it; it is exercised only by its unit tests (here and via functionresolver). So
// adding it is byte-identical on production by construction. It becomes load-bearing
// when the function layer engages (Phase 5d).

#include <functional>
#include <set>

namespace mu::composing::analysis {

// ── §8 case-4 threshold parameters (the firewall, build §4) — provisional seeds ──
//
// The bar a contradiction must cross to overturn an earlier inference of confidence
// c is:  baseBar + confidenceScale · c   (c in [0,1]). Both seeds DEFAULT; only the
// direction is fixed (the bar is non-decreasing in c). NOT tuned for accuracy.
struct ForwardOverrideParams {
    double baseBar         = 1.0;  ///< contradiction strength required at zero earlier-confidence
    double confidenceScale = 1.0;  ///< extra bar per unit of earlier-layer confidence [0,1]
};

/// Global default forward-override parameters.
inline constexpr ForwardOverrideParams kDefaultForwardOverrideParams{};

/// §8 case-4: the bar a contradiction must CROSS to overturn an inference of the
/// given confidence — baseBar + confidenceScale · earlierConfidence. Monotone
/// non-decreasing in @p earlierConfidence (the fixed direction).
double overrideBar(double earlierConfidence,
                   const ForwardOverrideParams& p = kDefaultForwardOverrideParams) noexcept;

/// §8 case-4: does the later contradiction OVERTURN the earlier inference? True iff
/// @p contradictionStrength is STRICTLY GREATER than overrideBar(@p earlierConfidence)
/// — at the exact bar the incumbent holds (tie-direction fixed). This is the pure
/// threshold test; the one-pass closure that makes it fire AT MOST ONCE per decision
/// lives in OnePassClosure below.
bool overrides(double earlierConfidence, double contradictionStrength,
               const ForwardOverrideParams& p = kDefaultForwardOverrideParams) noexcept;

// ── The one-pass closure ledger + the localized forward recompute (§8) ─────────
//
// The state that makes the override convergence-bounded within a single analysis
// pass. A decision (keyed by an opaque integer id — a slice index for the fine-grain
// override; a region/key id for the modulation recompute) that is overturned, or
// otherwise closed, is FINAL for the rest of the pass: neither the recompute it
// triggers nor any later override in the same pass can re-target it. The ledger only
// ever GROWS within a pass (no back-edge); reset() starts a fresh pass.
class OnePassClosure {
public:
    /// Has @p decisionId already been closed (overturned / marked final) this pass?
    bool isClosed(int decisionId) const noexcept;

    /// Mark @p decisionId final for the remainder of this pass. Returns false if it
    /// was ALREADY closed (the caller must not re-target a closed decision — the
    /// convergence guarantee); true on the first close.
    bool markFinal(int decisionId);

    /// §8 case-4, guarded: fire the override iff @p decisionId is NOT already closed
    /// AND overrides(@p earlierConfidence, @p contradictionStrength) holds. On fire it
    /// marks the decision final and returns true; otherwise it leaves the ledger
    /// unchanged and returns false. This is the single entry point that couples the
    /// threshold to the closure, so a decision is overturned AT MOST ONCE per pass.
    bool tryOverride(int decisionId, double earlierConfidence, double contradictionStrength,
                     const ForwardOverrideParams& p = kDefaultForwardOverrideParams);

    /// §8 / §5.4: the LOCALIZED, FORWARD, convergence-bounded recompute. Sweeps the
    /// slice range [@p firstSlice, @p lastSlice] in FORWARD order, calling @p reread
    /// exactly once per slice id (the dependent reading re-run against the corrected
    /// fact). The triggering decision must already be CLOSED (via tryOverride /
    /// markFinal) before this is called, so the recompute cannot re-open it. The sweep
    /// is RE-ENTRANCY-GUARDED: a nested forwardRecompute invoked from within @p reread
    /// is REFUSED (returns -1) — this is what makes "one localized forward re-run,
    /// never a loop" structural. @p reread may itself close downstream decisions (via
    /// tryOverride, closure-respecting) but must not launch another recompute. Returns
    /// the number of slices re-read, or -1 if refused (re-entrant) or the range is
    /// empty/inverted.
    int forwardRecompute(int firstSlice, int lastSlice,
                         const std::function<void(int /*sliceId*/)>& reread);

    /// True while a forwardRecompute sweep is in progress (the re-entrancy guard).
    bool isRecomputing() const noexcept { return m_recomputing; }

    /// Number of decisions closed this pass (transparency / tests).
    int closedCount() const noexcept { return static_cast<int>(m_closed.size()); }

    /// Start a fresh analysis pass: forget all closures and clear the recompute guard.
    void reset() noexcept;

private:
    std::set<int> m_closed;        ///< the closed-decision ids (grows-only within a pass)
    bool m_recomputing = false;    ///< true during an active forwardRecompute sweep (no nesting)
};

} // namespace mu::composing::analysis
