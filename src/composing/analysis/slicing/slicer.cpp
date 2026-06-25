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

#include "slicer.h"

#include <algorithm>

namespace mu::composing::analysis::slicing {

std::vector<Slice> changePointSlices(const notemodel::NoteModel& model)
{
    // Boundary ticks = every onset AND every release of an ELIGIBLE note. A note
    // is eligible iff layer 1 flagged it tonal-sounding (plays && visible &&
    // staffEligible). We READ those flags; we never re-decide eligibility. A
    // non-eligible note (muted / invisible / non-tonal-staff) opens NO boundary,
    // yet still rides along in each slice's overlapping() set (pass-through) — so
    // nothing is dropped, the slicer just does not split on it.
    std::vector<int> boundaries;
    boundaries.reserve(model.notes().size() * 2);
    for (const notemodel::NoteEvent& e : model.notes()) {
        if (!(e.plays && e.visible && e.staffEligible)) {
            continue;   // non-eligible: a passenger, not a change-point
        }
        // No special-casing of any note kind: a grace / tuplet / zero-width note
        // contributes its onset and release exactly as the model represents them.
        // A zero-width note (onset == release) contributes a single tick that
        // dedups away below and opens no slice — a fact, not a rule.
        boundaries.push_back(e.onset);
        boundaries.push_back(e.release);
    }

    // Sorted-unique: a tick that is simultaneously a release and an onset is ONE
    // boundary (set dedup), not two. O(n log n) — the only non-linear step.
    std::sort(boundaries.begin(), boundaries.end());
    boundaries.erase(std::unique(boundaries.begin(), boundaries.end()), boundaries.end());

    // Fewer than two distinct boundaries => no span to slice (no eligible notes,
    // or a single zero-width boundary). The covering partition is empty.
    std::vector<Slice> slices;
    if (boundaries.size() < 2) {
        return slices;
    }

    // CLIP TO THE LOADED SPAN (bounded context — cowork_layer2_reslice_design.md §2).
    // Layer 1 retains notes that OVERLAP the loaded span, so a sustained-in note
    // contributes an onset boundary < loadedStart, and a sustained-out note a
    // release boundary > loadedEnd. Tiling those would slice music OUTSIDE the
    // loaded span — a scope leak under bounded context. So slice the INTERSECTION
    // [max(loadedStart, front), min(loadedEnd, back)): clip the whole multiset, not
    // just the ends — drop every boundary out of [clipStart, clipEnd], then inject
    // the two clip endpoints and re-establish sorted-unique. (Retention guarantees
    // the only out-of-range boundaries are sustained-in onsets < clipStart and
    // sustained-out releases > clipEnd, so clipStart <= clipEnd always holds.)
    //
    // INERT ON WHOLE-SCORE (the degenerate live path): loadedStart == scoreStart
    // <= front and loadedEnd == scoreEnd >= back, so clipStart == front and
    // clipEnd == back; nothing is out of range and the injected endpoints are
    // already present — the clipped set is IDENTICAL to the unclipped one. Every
    // production/tooling caller builds a whole-score model, so this is byte-for-byte
    // unchanged on the live path; partial spans (Phase 1a build(sc,start,end)) are
    // the only callers the clip changes.
    const int clipStart = std::max(model.loadedStart(), boundaries.front());
    const int clipEnd   = std::min(model.loadedEnd(),   boundaries.back());
    boundaries.erase(
        std::remove_if(boundaries.begin(), boundaries.end(),
                       [clipStart, clipEnd](int b) { return b < clipStart || b > clipEnd; }),
        boundaries.end());
    boundaries.push_back(clipStart);
    boundaries.push_back(clipEnd);
    std::sort(boundaries.begin(), boundaries.end());
    boundaries.erase(std::unique(boundaries.begin(), boundaries.end()), boundaries.end());

    // A degenerate single-tick loaded span can collapse the clipped set to one
    // boundary (clipStart == clipEnd): the tiling loop then runs zero times and
    // returns the empty partition — no span to slice. (Cannot happen on whole-score.)
    if (boundaries.size() < 2) {
        return slices;
    }

    // Consecutive boundaries tile the domain [boundaries.front(), boundaries.back())
    // with no gaps and no overlaps. An interior pair with no overlapping eligible
    // note is an explicit EMPTY slice (all eligible voices rest) — kept, not omitted.
    slices.reserve(boundaries.size() - 1);
    for (std::size_t i = 0; i + 1 < boundaries.size(); ++i) {
        slices.push_back(Slice{ boundaries[i], boundaries[i + 1] });
    }
    return slices;
}

} // namespace mu::composing::analysis::slicing
