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

// ── composing/analysis/engravingbridge — the shared spelling primitive ────────
//
// The SINGLE place that interprets a note's notated tonal pitch class (`tpc`,
// a line-of-fifths spelling carried by Layer 1) into spelling semantics. It
// lives beside the other Layer-1-derived views (soundingAt / weightedPcView /
// pitchContextOverSpan), NOT inside an analysis layer, so both Layer 3 (key)
// and Layer 4 (chord) read spelling through one interpreter — never a per-layer
// copy (the unification rule).
//
// Two read shapes of the SAME interpretation:
//   • per-note    — lineOfFifths() / sharpFlatSense(): the per-note spelling the
//                   Layer-4 symmetric-root spelling-pin consumes (G♯ ≠ A♭).
//   • over a span — spanSpelling(): the signature-agnostic line-of-fifths
//                   centroid + sharp/flat distribution (modulation-direction
//                   signal) the Layer-3 key-spelling term consumes.
//
// Capability (Phase 4): no PRODUCTION (live) path consumes this yet — its only
// consumer is the DORMANT Layer-4 spelling-pin (chordslicedecoder.cpp:553,
// engravingbridge::lineOfFifths). That pin is BUILT (commit 1e74f21ea4), not
// "the next build". FOLDING the chordanalyzer.cpp inline tpc cluster — tpcForPc /
// tpcSpellsAsSharp / tpcConsistencyBonus / countTpcMatches — into this primitive
// has NOT happened: the live legacy scorer still interprets tpc independently, so
// a second tpc reader coexists today. The fold lands when the decoder goes live
// and the legacy scorer retires (engage-with-L5). The Layer-3 key-spelling *term*
// + its weight (spanSpelling / sharpFlatSense — currently zero consumers) are
// Phase B. See cowork_tpc_capability_design.md.
//
// SCOPE — signature-agnostic by ratified design (option A): the span aggregate
// is the centroid / sharp-flat distribution only; it takes NO key signature.
// The signature-relative key-fit (line-of-fifths distance outside the
// [sf-1, sf+5] diatonic window, analysisutils::diatonicMaskFromFifths) is the
// Layer-3 key-spelling TERM and lands in Phase B — recorded here as that term's
// reuse target, deliberately NOT built into this primitive.

#include <vector>

#include "engraving/dom/pitchspelling.h"

namespace mu::composing::analysis::engravingbridge {

/// Returned by lineOfFifths() for a tpc that fails `tpcIsValid()` (absent or out
/// of the [TPC_MIN, TPC_MAX] = [-8, 40] range). Chosen as the position TPC_INVALID
/// would map to (= -23), one below the minimum valid line-of-fifths position (-22),
/// so it can never collide with a real spelling's position.
constexpr int kNoLineOfFifths
    = static_cast<int>(mu::engraving::Tpc::TPC_INVALID) - static_cast<int>(mu::engraving::Tpc::TPC_C);

/// Line-of-fifths position of a notated spelling: `tpc - TPC_C` (TPC_C = 14;
/// +1 tpc = +1 fifth). C = 0, G = +1 (sharp / dominant side), F = -1 (flat /
/// subdominant side); G♯ = +8, A♭ = -4 — so enharmonics are distinguished (the
/// per-note signal the Layer-4 spelling-pin needs).
///
/// Presence is tested with engraving `tpcIsValid()` — NOT `tpc >= 0` / `tpc != -1`.
/// The flat side of the line of fifths is NEGATIVE (TPC_F_BB = -1 down to
/// TPC_F_BBB = -8), so a `>= 0` guard would silently drop legitimate flat-side
/// spellings. Returns kNoLineOfFifths when `!tpcIsValid(tpc)`.
///
/// Note: `tpcIsValid` keeps the real range but does NOT separate "absent" from a
/// real F𝄫 (both stored as -1). Distinguishing those is the build-path
/// invariant's job (every NoteEvent on the build path is assigned a real
/// `Note::tpc()`), NOT this function's — a recorded Layer-1 matter
/// (cowork_tpc_capability_design.md §5), out of scope here.
int lineOfFifths(int tpc);

/// Sharp-side / flat-side sense of a spelling: the SIGN of its line-of-fifths
/// offset from C. +1 = sharp side, -1 = flat side, 0 = C (the line-of-fifths
/// origin). Returns 0 for an absent/invalid tpc.
int sharpFlatSense(int tpc);

/// Signature-agnostic aggregate of a span's spellings — the line-of-fifths
/// centroid (modulation-direction signal: sharp-side mass ⇒ dominant direction,
/// flat-side ⇒ subdominant) and the sharp/flat/natural distribution. Spellings
/// failing `tpcIsValid()` are skipped (not counted). With no valid spellings,
/// count == 0 and lofCentroid == 0.0. Invariant: count == sharpCount + flatCount
/// + naturalCount.
struct SpanSpelling {
    int    count        = 0;    ///< number of valid (tpcIsValid) spellings aggregated
    double lofCentroid  = 0.0;  ///< mean line-of-fifths position over the valid spellings (0.0 if count == 0)
    int    sharpCount   = 0;    ///< valid spellings on the sharp side (line-of-fifths > 0)
    int    flatCount    = 0;    ///< valid spellings on the flat side (line-of-fifths < 0)
    int    naturalCount = 0;    ///< valid spellings at C (line-of-fifths == 0)
};

/// Aggregate the line-of-fifths centroid + sharp/flat distribution over @p tpcs.
SpanSpelling spanSpelling(const std::vector<int>& tpcs);

} // namespace mu::composing::analysis::engravingbridge
