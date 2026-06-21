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
