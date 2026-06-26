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

// Phase 4 — the shared spelling primitive (engravingbridge::spellingview).
// Pure-function unit tests of the SINGLE tpc → line-of-fifths / sharp-flat
// interpreter: enharmonic distinction (G♯ ≠ A♭), sharp/flat sense, flat-side
// validity (the regression a `>= 0` guard would cause), and the signature-agnostic
// span aggregate (centroid + distribution). No score / environment needed — the
// primitive is pure. See cowork_tpc_capability_design.md.

#include <gtest/gtest.h>

#include <vector>

#include "engraving/dom/pitchspelling.h"

#include "composing/analysis/engravingbridge/spellingview.h"

namespace ebr = mu::composing::analysis::engravingbridge;

using mu::engraving::Tpc;

// ── Per-note: enharmonic distinction (the whole point) ────────────────────────

TEST(SpellingViewTests, GSharpAndAFlatGetDifferentLineOfFifths)
{
    // G♯ and A♭ are the same pitch class but different spellings; line-of-fifths
    // distinguishes them. G♯ = tpc 22 → +8 (sharp side); A♭ = tpc 10 → -4 (flat side).
    EXPECT_EQ(ebr::lineOfFifths(Tpc::TPC_G_S), 8);
    EXPECT_EQ(ebr::lineOfFifths(Tpc::TPC_A_B), -4);
    EXPECT_NE(ebr::lineOfFifths(Tpc::TPC_G_S), ebr::lineOfFifths(Tpc::TPC_A_B));
}

TEST(SpellingViewTests, LineOfFifthsIsTpcMinusTpcC)
{
    EXPECT_EQ(ebr::lineOfFifths(Tpc::TPC_C),  0);   // origin
    EXPECT_EQ(ebr::lineOfFifths(Tpc::TPC_G), +1);   // one fifth sharp (dominant side)
    EXPECT_EQ(ebr::lineOfFifths(Tpc::TPC_D), +2);
    EXPECT_EQ(ebr::lineOfFifths(Tpc::TPC_F), -1);   // one fifth flat (subdominant side)
    // Boundaries of the valid line-of-fifths range.
    EXPECT_EQ(ebr::lineOfFifths(Tpc::TPC_MIN), -22); // TPC_F_BBB = -8
    EXPECT_EQ(ebr::lineOfFifths(Tpc::TPC_MAX), +26); // TPC_B_SSS = 40
}

// ── Per-note: sharp / flat / natural sense (sign of the line-of-fifths offset) ──

TEST(SpellingViewTests, SharpFlatSenseIsSignOfLineOfFifths)
{
    EXPECT_GT(ebr::sharpFlatSense(Tpc::TPC_G_S), 0);   // sharp-side spelling reads sharp
    EXPECT_LT(ebr::sharpFlatSense(Tpc::TPC_A_B), 0);   // flat-side spelling reads flat
    EXPECT_EQ(ebr::sharpFlatSense(Tpc::TPC_C),  0);    // a natural at the origin reads 0

    // The sense is exactly the sign: ±1 / 0.
    EXPECT_EQ(ebr::sharpFlatSense(Tpc::TPC_G_S), +1);
    EXPECT_EQ(ebr::sharpFlatSense(Tpc::TPC_A_B), -1);

    // By design the sense is the line-of-fifths SIDE (modulation direction), not
    // the accidental: a natural away from C is non-zero (G is on the sharp /
    // dominant side, F on the flat / subdominant side).
    EXPECT_EQ(ebr::sharpFlatSense(Tpc::TPC_G), +1);
    EXPECT_EQ(ebr::sharpFlatSense(Tpc::TPC_F), -1);
}

// ── Per-note: flat-side validity — the `>= 0` guard regression ────────────────

TEST(SpellingViewTests, FlatSideSpellingIsKeptByTpcIsValidNotDroppedByGteZero)
{
    // F𝄫 (TPC_F_BB) is a LEGITIMATE flat-side spelling whose tpc is negative (-1).
    // A `>= 0` presence guard would silently drop it; tpcIsValid() keeps it.
    ASSERT_LT(static_cast<int>(Tpc::TPC_F_BB), 0);                 // a `>= 0` guard would reject it
    EXPECT_TRUE(mu::engraving::tpcIsValid(Tpc::TPC_F_BB));         // but tpcIsValid keeps it
    EXPECT_EQ(ebr::lineOfFifths(Tpc::TPC_F_BB), -15);             // interpreted at its real position, not the sentinel
    EXPECT_NE(ebr::lineOfFifths(Tpc::TPC_F_BB), ebr::kNoLineOfFifths);
    EXPECT_EQ(ebr::sharpFlatSense(Tpc::TPC_F_BB), -1);            // and reads flat
}

TEST(SpellingViewTests, InvalidTpcReturnsTheAbsenceSentinel)
{
    // TPC_INVALID (-9) and any out-of-range value fail tpcIsValid → absence sentinel
    // / neutral sense. (This is the genuinely-absent case, distinct from the real
    // F𝄫 = -1 above, which IS valid.)
    EXPECT_FALSE(mu::engraving::tpcIsValid(Tpc::TPC_INVALID));
    EXPECT_EQ(ebr::lineOfFifths(Tpc::TPC_INVALID), ebr::kNoLineOfFifths);
    EXPECT_EQ(ebr::lineOfFifths(100), ebr::kNoLineOfFifths);
    EXPECT_EQ(ebr::sharpFlatSense(Tpc::TPC_INVALID), 0);
    // The sentinel can never collide with a real spelling's position.
    EXPECT_LT(ebr::kNoLineOfFifths, ebr::lineOfFifths(Tpc::TPC_MIN));
}

// ── Span aggregate: centroid + distribution (signature-agnostic) ──────────────

TEST(SpellingViewTests, SpanAggregateMatchesHandComputedCentroidAndDistribution)
{
    // Fixture spellings and their line-of-fifths positions:
    //   C  →  0 (natural)
    //   G  → +1 (sharp)
    //   D  → +2 (sharp)
    //   F  → -1 (flat)
    //   A♭ → -4 (flat)
    //   TPC_INVALID → skipped (not counted)
    // Hand-computed over the 5 valid spellings: sum = 0+1+2-1-4 = -2,
    // centroid = -2/5 = -0.4; sharp = 2, flat = 2, natural = 1, count = 5.
    const std::vector<int> tpcs = {
        Tpc::TPC_C, Tpc::TPC_G, Tpc::TPC_D, Tpc::TPC_F, Tpc::TPC_A_B, Tpc::TPC_INVALID
    };

    const ebr::SpanSpelling agg = ebr::spanSpelling(tpcs);

    EXPECT_EQ(agg.count, 5);                       // the invalid spelling was skipped
    EXPECT_DOUBLE_EQ(agg.lofCentroid, -0.4);
    EXPECT_EQ(agg.sharpCount, 2);
    EXPECT_EQ(agg.flatCount, 2);
    EXPECT_EQ(agg.naturalCount, 1);
    EXPECT_EQ(agg.sharpCount + agg.flatCount + agg.naturalCount, agg.count); // partition invariant
}

TEST(SpellingViewTests, SpanAggregateOfEmptyOrAllInvalidIsZero)
{
    const ebr::SpanSpelling empty = ebr::spanSpelling({});
    EXPECT_EQ(empty.count, 0);
    EXPECT_DOUBLE_EQ(empty.lofCentroid, 0.0);

    const ebr::SpanSpelling allInvalid = ebr::spanSpelling({ Tpc::TPC_INVALID, 100, -100 });
    EXPECT_EQ(allInvalid.count, 0);
    EXPECT_DOUBLE_EQ(allInvalid.lofCentroid, 0.0);
    EXPECT_EQ(allInvalid.sharpCount, 0);
    EXPECT_EQ(allInvalid.flatCount, 0);
    EXPECT_EQ(allInvalid.naturalCount, 0);
}

// ── One interpreter: the derived shapes stay consistent with lineOfFifths ─────

TEST(SpellingViewTests, DerivedShapesAreConsistentAcrossTheValidRange)
{
    // sharpFlatSense and spanSpelling both derive from lineOfFifths, so over the
    // whole valid range the sense is the sign of the position and the span counts
    // partition by that same sign — proof the interpretation lives in one place.
    int sharp = 0, flat = 0, natural = 0;
    std::vector<int> all;
    for (int tpc = Tpc::TPC_MIN; tpc <= Tpc::TPC_MAX; ++tpc) {
        const int lof = ebr::lineOfFifths(tpc);
        ASSERT_NE(lof, ebr::kNoLineOfFifths) << "tpc " << tpc << " is in range and must be valid";
        const int expectedSense = (lof > 0) - (lof < 0);
        EXPECT_EQ(ebr::sharpFlatSense(tpc), expectedSense) << "tpc " << tpc;
        if (lof > 0) {
            ++sharp;
        } else if (lof < 0) {
            ++flat;
        } else {
            ++natural;
        }
        all.push_back(tpc);
    }

    const ebr::SpanSpelling agg = ebr::spanSpelling(all);
    EXPECT_EQ(agg.count, static_cast<int>(all.size()));
    EXPECT_EQ(agg.sharpCount, sharp);
    EXPECT_EQ(agg.flatCount, flat);
    EXPECT_EQ(agg.naturalCount, natural);
    // C (line-of-fifths 0) is the only natural across the full tpc range.
    EXPECT_EQ(natural, 1);
}
