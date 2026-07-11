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

// ── composing/analysis/slicing ───────────────────────────────────────────────
//
// LAYER 2 — the deterministic CHANGE-POINT SLICER: enumerate the constant-tonal-
// sonority slices of a score as a FACT, read off the layer-1 note model.
//
// Output: an ordered, gapless, non-overlapping list of half-open `[start, end)`
// spans that TILE the domain. Within each slice the eligible (tonal, sounding)
// note set is constant; it changes only at a boundary. This is the exhaustive
// candidate grid for chord change — a chord (root + quality) can change ONLY at a
// slice boundary, so boundaries are NECESSARY but NOT SUFFICIENT for a chord
// change. Layer 3 decides which boundaries are real; layer N groups equal
// analyses for display. A real chord change can therefore never be MISSED
// (over-grab is structurally impossible), and layer 2 never ASSERTS a change.
//
// INVARIANTS (the whole module, in brief — see §2 of the impl instruction):
//   * ZERO INTERPRETATION. A purely mechanical function of the note model. No
//     thresholds, no min-gap, no merge, no snapping, no notion of "ornamental /
//     passing / structural / important". No special-casing of any note kind
//     (grace, tuplet, etc.) — their outcomes fall out of the note-model spans as
//     facts. Anything that looks like a rule about KINDS of notes is layer-3
//     judgment and does not belong here.
//   * CONSUMES LAYER-1's ELIGIBILITY — never re-decides it. A note participates
//     in boundary generation iff `plays && visible && staffEligible` (the flags
//     layer 1 already set). Layer 2 READS those flags; it does not re-filter or
//     override them. A muted / invisible / non-tonal-staff note opens NO boundary.
//   * PASSES THE WHOLE MODEL FORWARD. A Slice stores only `[start, end)` and the
//     model reference; its note set is the LAZY query `model.overlapping(start,
//     end)`, which returns ALL overlapping notes (eligible AND the flagged
//     non-eligible passengers) — nothing is dropped. Slice IDENTITY (for
//     "constant sonority") is the eligible sounding-NOTE set, not the octave-
//     folded pitch-class set, and not the non-eligible passengers.
//   * COVERING, LOSSLESS PARTITION over the LOADED SPAN. Consecutive boundary
//     ticks form the slices; they tile the domain with no gaps and no overlaps.
//     The domain is the intersection of the eligible-notes span with the model's
//     loaded span (the bounded-context clip — see changePointSlices below): a
//     sustained-in / sustained-out note is clipped to the loaded boundary, never
//     dragging slicing outside the loaded span. On a whole-score model the loaded
//     span covers the notes, so the clip is inert. An interior span where all
//     eligible voices rest is an explicit EMPTY slice (its eligible overlap set is
//     empty) — NOT omitted. Leading/trailing silence outside the domain is not
//     invented (no eligible note bounds it).
//   * DETERMINISTIC + O(n log n). Same input model -> same slices, every run.
//
// It IS wired into the live analysis pipeline: layer 3 consumes the slices
// (regionanalyzer.cpp -> KeyModeSequenceDecoder::decode, at :634 and :705). The slicer's own
// output stays byte-identical on the whole-score live path (the clip is inert
// there) — the analysis movement came from layer 3's CONSUMPTION of the slices,
// not from the slicer. See cowork_layer2_slicing_design.md + cc_layer2_audit_dossier.md.

#include <vector>

#include "composing/analysis/notemodel/note_model.h"

namespace mu::composing::analysis::slicing {

// A constant-(tonal-)sonority slice: the half-open tick span [start, end).
//
// It references the note model (it stores no notes). Its sounding content is the
// lazy query `model.overlapping(start, end)` — ALL overlapping notes, eligible
// and non-eligible alike. `start < end` always holds for an emitted slice.
struct Slice {
    int start = 0;   ///< inclusive lower bound (a note onset or release tick).
    int end   = 0;   ///< exclusive upper bound (the next boundary tick).
};

// Enumerate the constant-sonority slices of the note model — the deterministic
// change-point grid.
//
// Boundaries = the sorted-unique union of every ONSET and every RELEASE tick
// among the ELIGIBLE notes (`plays && visible && staffEligible`), CLIPPED to the
// model's loaded span. Consecutive boundaries form the slices, tiling
// `[max(loadedStart, firstEligibleOnset), min(loadedEnd, lastEligibleRelease))`
// with no gaps and no overlaps (an all-rest interior span is an explicit empty
// slice). The clip keeps slicing inside the loaded span: a sustained-in note
// (onset < loadedStart) is present from loadedStart, a sustained-out note ends at
// loadedEnd (bounded context — cowork_layer2_reslice_design.md §2). On a whole-
// score model loadedStart <= firstEligibleOnset and loadedEnd >=
// lastEligibleRelease, so the clip is inert and the tiling is exactly
// `[firstEligibleOnset, lastEligibleRelease)` — byte-identical to before the clip.
// Returns empty if there are fewer than two distinct boundaries (no eligible
// notes, or a single zero-width / single-tick span — nothing to slice).
std::vector<Slice> changePointSlices(const notemodel::NoteModel& model);

} // namespace mu::composing::analysis::slicing
