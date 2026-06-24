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

// ── composing/analysis/notemodel ─────────────────────────────────────────────
//
// LAYER 1 — the lossless, annotated NOTE MODEL: the single source of truth for
// "what sounds" in a score.
//
// This module reads the score ONCE and produces, for the whole piece, the set
// of sounding notes — every note annotated with its true (tie-resolved) sounding
// span and the facts downstream layers need, queryable by tick range.
//
// It is deliberately NARROW. It does NOT weight, aggregate to pitch classes,
// pick a bass, slice, or make any key/chord decision. Those are downstream
// layers that derive VIEWS over this model (see engravingbridge/weightedPcView
// and soundingAt). Every later layer annotates or derives over the note model;
// none replaces it.
//
// The two correctness duties that distinguish this from the old tie-blind,
// capped collectors:
//   * TIE RESOLUTION — a tied group is ONE note, onset of the first → release of
//     the last (via the DOM's firstTiedNote/lastTiedNote/playTicksFraction).
//     Exactly one onset per group (kills the old repetition-boost inflation and
//     false onset/attack flags).
//   * TRUE SPANS + OVERLAP QUERY — each note carries its real [onset, release);
//     "what sounds in [t0, t1)" is an overlap query with NO horizon (kills the
//     old 4-whole-note backward cap that dropped long sustains).
//
// COLLECT-AND-ANNOTATE, NEVER DROP: grace, non-playing, invisible, and
// staff-ineligible notes are KEPT and FLAGGED, not discarded. The keep/drop
// decision is an explicit, reversible, downstream step (the views apply the old
// analysis filter; the lossless model retains everything).

#include <cstddef>
#include <vector>

#include "engraving/types/fraction.h"

namespace mu::engraving {
class Score;
}

namespace mu::composing::analysis::notemodel {

// A single sounding note, tie-resolved, with its true span and annotations.
//
// Ticks are absolute (engraving Fraction::ticks()). The span is half-open
// [onset, release); `duration == release - onset` is the tie-resolved sounding
// length (== Note::playTicksFraction()).
//
// NOTE on a deliberately-absent field: the signed design listed an `isCue` flag,
// but cue-ness is NOT recoverable from the DOM post-import — MusicXML import
// collapses it via `note->setPlay(!cue)`, so a cue note and a user-muted note
// are byte-identical at the DOM level (both `play()==false`, no other
// distinguishing property; the only `cue` concept in the engraving DOM is
// Ornament::cueNoteChord, unrelated). The field is therefore omitted rather than
// fabricated (user decision 2026-06-21; see cc_layer1_impl_report.md). Cue notes
// still behave correctly downstream: `plays==false` already excludes them from
// every analysis view.
struct NoteEvent {
    int  pitch  = 0;     ///< ppitch — MIDI playback pitch (honours ottavas/transpositions).
    int  tpc    = -1;    ///< TPC (0-34, circle-of-fifths spelling). -1 = not provided.
    int  staff  = 0;     ///< Owning staff index (the note's actual track staff, not visual placement).
    int  voice  = 0;     ///< Voice 0..VOICES-1.
    int  onset  = 0;     ///< Tie-resolved onset tick (onset of the first tied note).
    int  release = 0;    ///< Tie-resolved release tick (release of the last tied note).
    int  duration = 0;   ///< release - onset (== Note::playTicksFraction()).
    bool isGrace = false;       ///< Grace note (kept + flagged; attaches to its parent chord's tick).
    bool plays   = true;        ///< Note::play() (false for user-muted AND imported cue notes).
    bool visible = true;        ///< Note::visible().
    bool staffEligible = true;  ///< staffIsEligible() at this note's onset (hidden/drumset/chord-track => false).
};

// Static query index over an onset-sorted note set.
//
// Built once from a NoteModel's notes (O(N log N)); answers the two range
// queries in O(log N + result) instead of the old O(N) head scan — the fix that
// turns the per-slice query path from O(N²) into O(N log N) at full-act scale.
//
//   * onsetLowerBound(t)  — first index i with onset[i] >= t (binary search over
//     the onset-sorted keys). onsetIn([t0,t1)) is the contiguous block
//     [onsetLowerBound(t0), onsetLowerBound(t1)).
//   * overlapIndices(qHi,t0) — every index i in [0, qHi) with release[i] > t0,
//     emitted in ASCENDING index order. The hard query: a note with onset < t0
//     can still overlap, so the onset bound alone is not enough. Backed by a
//     max-release segment tree over the onset-sorted array — a subtree whose
//     maximum release is <= t0 contains no overlapper and is pruned whole.
//
// The index stores only the onset keys and the release tree (ints) — it does NOT
// alias the NoteEvent storage, so it copies/moves with the model. It assumes the
// notes are onset-sorted ascending (the NoteModel build-order invariant); it does
// not re-sort.
class NoteQueryIndex
{
public:
    /// Build the index from the onset-sorted note set. O(N log N). Safe for N==0.
    void build(const std::vector<NoteEvent>& notes);

    /// First index i with onset[i] >= t (== std::lower_bound on the onset keys).
    int onsetLowerBound(int t) const;

    /// Append, in ascending index order, every i in [0, qHi) with release[i] > t0.
    /// qHi is typically onsetLowerBound(t1). Appends to `out` (does not clear it).
    void overlapIndices(int qHi, int t0, std::vector<int>& out) const;

private:
    /// Segment-tree descent: collect leaves in [0, qHi) whose release > t0.
    void collect(int node, int nodeLo, int nodeHi, int qHi, int t0,
                 std::vector<int>& out) const;

    std::vector<int> m_onsets;     ///< onset keys, ascending (parallel to the notes).
    std::vector<int> m_segMaxRel;  ///< max-release perfect-binary-tree (1-based; leaves at [m_segSize, 2*m_segSize)).
    int m_segSize = 0;             ///< leaf count (power of two), 0 iff empty.
    int m_n = 0;                   ///< number of notes.
};

// The lossless note model for a SELECTION of a score (the whole score is the
// degenerate "selection = score" case).
//
// Construct with build(): either over the whole score (the degenerate, batch
// path — byte-identical to before this API existed) or over a SELECTION span,
// which retains only the notes that sound within the loaded span. The loaded
// span can then be grown by extend() (the bounded-context supplier API — see
// cowork_bounded_context_design.md / cowork_layer1_extend_design.md).
//
// Three spans (cowork_bounded_context_design.md §2):
//   * selection span  — what was asked for; the OUTPUT span (fixed at build).
//   * loaded span      — what is currently held; starts == selection, GROWS by
//     extend() (append-only). selection ⊆ loaded ⊆ score.
//   * score            — the whole piece; the hard outer bound extend() clamps at.
//
// Notes are stored in build order: ascending onset tick, then staff, then voice,
// then chord-note order. The model retains a borrowed pointer to its source Score
// (the derived views need it for beat weights / pedal windows / measure lookups,
// and the interim extend() re-walks it); the Score must outlive the model.
//
// PHASE 1a (interim) — extend() re-walks the whole score and re-filters to the
// new loaded span, then rebuilds the static index. Correct and byte-identical to
// a fresh build over the enlarged span; a span-scoped walk + an incremental index
// are Phase 1b (deferred behind this byte-identity gate). The live analysis path
// (region analyzer, batch_analyze) uses the whole-score build(sc) only; extend()
// is the L1 capability the layers above are written against (no layer calls it
// yet — that is Phase 3 reach-back).
class NoteModel
{
public:
    /// Direction of an extend() — earlier (toward the score start) or later
    /// (toward the score end) in time.
    enum class Direction { Earlier, Later };

    /// Read the WHOLE score ONCE into the lossless note model (the degenerate
    /// selection = score). Walks every staff, voice, and segment (and grace
    /// notes), resolving tied groups into single spans and annotating each note.
    /// Nothing is dropped. Byte-identical to the pre-selection-API behaviour.
    /// Implemented as a thin delegate to the span overload over the full score
    /// span (one walk path).
    static NoteModel build(const mu::engraving::Score* sc);

    /// Build over a SELECTION span [loadedStart, loadedEnd): walks the score and
    /// retains the notes whose span OVERLAPS the loaded span
    /// (`onset < loadedEnd && release > loadedStart` — this captures notes that
    /// started before loadedStart and sustain into the span). Records the loaded
    /// span and the selection span (== the same range at build time). Ticks.
    static NoteModel build(const mu::engraving::Score* sc, int loadedStart, int loadedEnd);

    /// Grow the LOADED span by `amountTicks` in direction `dir`, clamped at the
    /// score start/end, then re-derive the retained notes (interim: re-walk +
    /// re-filter) and rebuild the index. Exactly ONE step — does not loop and
    /// never evaluates any stop/convergence condition (the caller's job).
    /// Append-only (never shrinks the loaded span or drops a retained note).
    /// A non-positive amount, or a request for an already-covered span, is a
    /// no-op. Sets boundaryReached() to whether the clamp at the score boundary
    /// was hit this step. Ticks (Architectural Layer 1 is unit-blind).
    void extend(Direction dir, int amountTicks);

    const mu::engraving::Score* score() const { return m_score; }
    const std::vector<NoteEvent>& notes() const { return m_notes; }

    int  loadedStart() const { return m_loadedStart; }
    int  loadedEnd() const { return m_loadedEnd; }
    int  selectionStart() const { return m_selectionStart; }
    int  selectionEnd() const { return m_selectionEnd; }
    /// Whether the most recent extend() clamped at the score start/end.
    bool boundaryReached() const { return m_boundaryReached; }

    /// All notes whose span overlaps the half-open range [t0, t1):
    /// `onset < t1 && release > t0`. No horizon. Result preserves build order
    /// (ascending onset, then staff/voice/note).
    std::vector<const NoteEvent*> overlapping(int t0, int t1) const;

    /// All notes whose ONSET lies in the half-open range [t0, t1).
    /// Result preserves build order.
    std::vector<const NoteEvent*> onsetIn(int t0, int t1) const;

private:
    /// Interim Phase-1a worker: (re-)walk the whole score, retain the notes whose
    /// span overlaps the current loaded span [m_loadedStart, m_loadedEnd), and
    /// (re-)build the index. Used by both build(sc,lo,hi) and extend() — one walk
    /// path, no duplication.
    void rebuildForLoadedSpan();

    const mu::engraving::Score* m_score = nullptr;
    std::vector<NoteEvent> m_notes;  ///< Sorted by onset (ascending, stable build order).
    NoteQueryIndex m_index;          ///< Onset/overlap query index over m_notes (built in build()).

    int  m_loadedStart = 0;          ///< Current loaded-span start tick (grows down via extend Earlier).
    int  m_loadedEnd = 0;            ///< Current loaded-span end tick (grows up via extend Later).
    int  m_selectionStart = 0;       ///< Selection-span start tick (the OUTPUT span; fixed at build).
    int  m_selectionEnd = 0;         ///< Selection-span end tick (fixed at build).
    int  m_scoreStart = 0;           ///< Score start tick — the hard lower clamp for extend().
    int  m_scoreEnd = 0;             ///< Score end tick — the hard upper clamp for extend().
    bool m_boundaryReached = false;  ///< Whether the most recent extend() hit a score boundary.
};

} // namespace mu::composing::analysis::notemodel
