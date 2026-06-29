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

// forwardoverride_tests.cpp — Architectural Layer 5 (FUNCTION), Phase 5c Step 3.
//
// Oracle-asserted against the §8 specification (NOT echoes of the implementation): the
// confidence-weighted forward-override MECHANISM — the threshold (the bar scales with
// the earlier layer's confidence), the one-pass closure (a decision is overturned at
// most once and never re-opened), and the localized forward recompute (a single forward
// sweep, never a back-edge, never a loop). This is the reusable mechanism Step-4's
// modulation recompute also instantiates, so its closure-safety is pinned here.
// Spec: cowork_layer5_function_design.md §8 + §5.4.

#include <gtest/gtest.h>

#include <vector>

#include "composing/analysis/function/forwardoverride.h"

using namespace mu::composing::analysis;

namespace {

// ── §8 case-4 threshold: the bar scales with the earlier layer's confidence ───

TEST(ForwardOverride, BarIsMonotoneInConfidence)
{
    // baseBar 1.0 + confidenceScale 1.0 · c  ⇒  bar(0)=1.0, bar(0.5)=1.5, bar(1)=2.0.
    EXPECT_DOUBLE_EQ(overrideBar(0.0), 1.0);
    EXPECT_DOUBLE_EQ(overrideBar(0.5), 1.5);
    EXPECT_DOUBLE_EQ(overrideBar(1.0), 2.0);
    // Monotone non-decreasing (the fixed direction).
    EXPECT_GE(overrideBar(0.7), overrideBar(0.3));
    // Confidence is clamped to [0,1] so the bar is well-defined off-range.
    EXPECT_DOUBLE_EQ(overrideBar(-1.0), 1.0);
    EXPECT_DOUBLE_EQ(overrideBar(2.0), 2.0);
}

TEST(ForwardOverride, OverturnsBorderlineButNotConfidentOnTheSameContradiction)
{
    // THE confidence-scaling property: the same contradiction strength (1.5) overturns a
    // borderline inference (conf 0.0, bar 1.0) but NOT a confident one (conf 1.0, bar 2.0).
    const double strength = 1.5;
    EXPECT_TRUE(overrides(/*conf*/ 0.0, strength));   // 1.5 > 1.0
    EXPECT_FALSE(overrides(/*conf*/ 1.0, strength));  // 1.5 < 2.0 — a confident commit demands more
}

TEST(ForwardOverride, TieDirectionFavoursTheIncumbent)
{
    // At the EXACT bar the incumbent holds (strictly-greater rule).
    EXPECT_FALSE(overrides(/*conf*/ 0.0, /*strength*/ 1.0));   // == bar(0) = 1.0
    EXPECT_TRUE(overrides(/*conf*/ 0.0, /*strength*/ 1.0001)); // just above
    EXPECT_FALSE(overrides(/*conf*/ 1.0, /*strength*/ 2.0));   // == bar(1) = 2.0
}

// ── The one-pass closure ledger ───────────────────────────────────────────────

TEST(ForwardOverride, MarkFinalIsIdempotentPerPass)
{
    OnePassClosure closure;
    EXPECT_FALSE(closure.isClosed(7));
    EXPECT_TRUE(closure.markFinal(7));    // first close
    EXPECT_TRUE(closure.isClosed(7));
    EXPECT_FALSE(closure.markFinal(7));   // already closed — re-close refused
    EXPECT_EQ(closure.closedCount(), 1);
}

TEST(ForwardOverride, TryOverrideFiresThenClosesSoItNeverReTargets)
{
    OnePassClosure closure;
    // Fires: not closed AND the contradiction crosses the bar (conf 0.5 ⇒ bar 1.5).
    EXPECT_TRUE(closure.tryOverride(3, /*conf*/ 0.5, /*strength*/ 2.0));
    EXPECT_TRUE(closure.isClosed(3));
    // A SECOND override on the SAME decision in the SAME pass is REFUSED (the §8 closure):
    // even an overwhelming contradiction cannot re-target an already-overturned decision.
    EXPECT_FALSE(closure.tryOverride(3, /*conf*/ 0.5, /*strength*/ 999.0));
    EXPECT_EQ(closure.closedCount(), 1);
}

TEST(ForwardOverride, TryOverrideDoesNotFireOrCloseBelowTheBar)
{
    OnePassClosure closure;
    // conf 0.5 ⇒ bar 1.5; strength 1.0 does not cross it.
    EXPECT_FALSE(closure.tryOverride(4, /*conf*/ 0.5, /*strength*/ 1.0));
    EXPECT_FALSE(closure.isClosed(4));    // a non-firing attempt leaves the decision open
}

// ── The localized forward recompute ───────────────────────────────────────────

TEST(ForwardOverride, ForwardRecomputeSweepsTheRangeOnceInForwardOrder)
{
    OnePassClosure closure;
    std::vector<int> visited;
    const int n = closure.forwardRecompute(2, 5, [&](int j) { visited.push_back(j); });
    EXPECT_EQ(n, 4);
    ASSERT_EQ(visited.size(), 4u);
    EXPECT_EQ(visited[0], 2);             // forward (ascending) order
    EXPECT_EQ(visited[1], 3);
    EXPECT_EQ(visited[2], 4);
    EXPECT_EQ(visited[3], 5);
}

TEST(ForwardOverride, ForwardRecomputeRejectsEmptyOrInvertedRange)
{
    OnePassClosure closure;
    int calls = 0;
    EXPECT_EQ(closure.forwardRecompute(5, 2, [&](int) { ++calls; }), -1);  // inverted
    EXPECT_EQ(calls, 0);
}

TEST(ForwardOverride, NestedRecomputeIsRefused_NeverALoop)
{
    // The re-entrancy guard makes "one localized forward re-run, never a loop" structural:
    // a forwardRecompute invoked from WITHIN a reread is refused (-1); the outer sweep
    // still completes its single forward pass.
    OnePassClosure closure;
    int nestedResult = 0;
    int outerVisits = 0;
    const int n = closure.forwardRecompute(0, 2, [&](int) {
        ++outerVisits;
        // Attempt to recurse — must be refused while the outer sweep is active.
        nestedResult = closure.forwardRecompute(10, 12, [](int) {});
    });
    EXPECT_EQ(n, 3);
    EXPECT_EQ(outerVisits, 3);
    EXPECT_EQ(nestedResult, -1);          // every nested attempt refused
    EXPECT_FALSE(closure.isRecomputing()); // the guard is cleared after the outer sweep
}

TEST(ForwardOverride, RecomputeCannotReTargetAClosedDecision)
{
    // The recompute re-reads the region but cannot re-open the triggering (closed)
    // decision: a tryOverride against it from inside the reread is refused.
    OnePassClosure closure;
    ASSERT_TRUE(closure.markFinal(0));    // the trigger is closed before the recompute
    bool reTargetRefused = false;
    closure.forwardRecompute(0, 2, [&](int j) {
        if (j == 0) {
            reTargetRefused = !closure.tryOverride(0, /*conf*/ 0.0, /*strength*/ 999.0);
        }
    });
    EXPECT_TRUE(reTargetRefused);
}

TEST(ForwardOverride, ResetStartsAFreshPass)
{
    OnePassClosure closure;
    closure.markFinal(1);
    closure.markFinal(2);
    EXPECT_EQ(closure.closedCount(), 2);
    closure.reset();
    EXPECT_EQ(closure.closedCount(), 0);
    EXPECT_FALSE(closure.isClosed(1));
}

} // namespace
