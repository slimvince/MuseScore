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

// ── composing/analysis/chord/chordslicedecoder ──────────────────────────────
//
// LAYER 4 — the CHORD-SYMBOL per-slice path (INCREMENT A only).
//
// For each Layer-2 slice this names a chord (root + quality + bass/inversion)
// by running the EXISTING chord scorer (analyzeChord) over the slice's note
// window and reading the COMPLETE candidate cube it surfaces — exactly the way
// the Layer-3 key/mode decoder reads analyzeKeyMode's 252-candidate dump. The
// per-slice result carries the chosen chord, the ranked alternatives, a
// confidence (the margin to the best DIFFERENT chord) and an "uncertain" mark.
//
// WHAT INCREMENT A IS (signed design cowork_layer4_chordsymbol_design.md;
// pre-build audit cc_layer4_audit_dossier.md): it stands up the per-slice path
// and the grading harness so the genuinely-new parts land on a measured
// baseline. It reuses the scorer and its cube; it does NOT fork a second scorer.
//
// WHAT INCREMENT A IS NOT (deferred — STOP if you start building these here):
//   * per-note chord-tone-vs-NCT MEMBERSHIP (the two-pass, neighbour-aware
//     decision + the adaptive lazy-extend window) — Increment B. The membership
//     sets on SliceChord are STUBBED EMPTY here.
//   * the deterministic spelling-PIN for the symmetric (dim7/aug) root, the new
//     diminished-seventh / minor-major TYPES, and extensions read from
//     membership — Increment C.
// So the chosen chord here is the existing scorer's per-window winner; the
// "complete candidate list" is the surfaced cube ranked and pruned to top-K. No
// new chord type, no spelling pin, no membership — those land on this baseline.
//
// HOW IT WORKS (this increment):
//   1. Window. For each slice, build a ChordAnalysisTone window over the slice
//      span EXTENDED by `contextSlices` neighbour slices on each side, through
//      the INDEXED engravingbridge view weightedPcView (over the Layer-1 indexed
//      NoteModel::overlapping) — NEVER a region aggregate or a DOM walk. The
//      fixed ±contextSlices window is a crude stand-in for the design's adaptive
//      lazy-extend window (Increment B); it is a SETTING, not a constant.
//   2. Score + surface the cube. Run analyzeChord(window, key, …) with a
//      snapshotOut, giving the complete (bass × root × template) candidate cube
//      (fn::ScoringSnapshot::cells), each with its vertical fit score.
//   3. Rank + prune. Project every cell to a candidate, rank by vertical score,
//      keep the top-K distinct chords (∪ the prevailing chord — the previous
//      slice's chosen, kept alive as a carried alternative, the L3 incumbent
//      pattern). The chosen chord is the existing scorer's own winner
//      (analyzeChord's top result), located back in the cube by template index.
//   4. Confidence. confidence = the chosen cell's vertical score minus the best
//      vertical score over any DIFFERENT (root, quality) cell; a slice is
//      "uncertain" when that margin is below uncertaintyMargin. Membership sets
//      are left EMPTY (Increment B).
//
// KEY is a feed-forward PRIOR (design §2/§9): the slice is scored under a given
// key/mode (the notated signature in the --decode-chords diagnostic), which
// tips genuinely-close readings diatonic. Per-slice key feed-forward from the
// Layer-3 decoder is a later (wiring) refinement; this increment takes one key.
//
// ISOLATION (this increment): the decoder is BUILT, unit-tested, and GRADED
// against the held-out chord ground truth, but NOT wired into the live analysis
// pipeline. Production analysis output is byte-identical; the decoder runs only
// under the read-only batch_analyze --decode-chords diagnostic (which returns
// before analyzeScore). Re-pointing the per-region analyzeChord seam
// (regionanalyzer.cpp) onto this per-slice path is a later, separate increment.

#include <optional>
#include <set>
#include <vector>

#include "chordanalyzer.h"
#include "composing/analysis/notemodel/note_model.h"
#include "composing/analysis/slicing/slicer.h"

namespace mu::composing::analysis::chordslice {

// ── Tunable settings (effort-retrofit hygiene) ───────────────────────────────
//
// Every cost-driving choice is a SETTING here, never a hardcoded constant, so a
// future "effort" preset (quick / normal / ambitious) is a clean retrofit and
// the window / top-K / uncertainty knobs can be swept against the held-out
// metric. The defaults are sensible seeds, not tuned values.
struct ChordSliceDecoderPreferences {
    /// Number of neighbour slices included on EACH side of the focal slice when
    /// building its tone window (0 = the slice alone). A crude fixed stand-in
    /// for the design's adaptive lazy-extend window (Increment B): wide enough
    /// that an arpeggio / incomplete-chord slice can see the figure it belongs
    /// to, narrow enough that it does not pool a whole phrase. Default 1 (the
    /// slice and its immediate neighbours).
    int contextSlices = 1;

    /// Distinct chords kept per slice as ranked alternatives (∪ the prevailing
    /// chord), excluding the chosen. 0 = keep all surviving distinct chords.
    int topK = 6;

    /// A slice is marked "uncertain" when its confidence (the chosen cell's
    /// vertical score minus the best DIFFERENT (root,quality) cell's) is below
    /// this margin. A seed in vertical-score units; swept later.
    double uncertaintyMargin = 0.5;

    /// Minimum distinct pitch classes for analyzeChord to score a window. The
    /// production default is 3; the per-slice path relaxes it to 1 (the same
    /// relaxation greedyExpandSegmentation already uses for sparse anchors —
    /// audit §8-D) so thin slices are still named rather than silently dropped.
    /// Applied to a COPY of the chord prefs inside decode(); production is
    /// untouched.
    int minDistinctPcs = 1;
};

/// Global default decoder settings.
inline constexpr ChordSliceDecoderPreferences kDefaultChordSliceDecoderPreferences{};

// ── A single candidate chord (one cube cell, projected) ──────────────────────
//
// The chord-symbol fields the home BIR metric scores: root + quality + the
// bass/inversion (bassPc vs rootPc). The tpc fields name the chord
// enharmonically; tiePriority is the template index (locates the cell in the
// cube). `score` is the cell's VERTICAL fit score
// ((basisIndep + basisDep) × complexityFactor × augFactor + wCompleteBonus) —
// the value the competition pipeline ranks by on the null-context path.
struct ChordSliceCandidate {
    int rootPc = -1;
    int rootTpc = -1;
    int bassPc = -1;
    int bassTpc = -1;
    ChordQuality quality = ChordQuality::Unknown;
    int tiePriority = -1;
    double score = 0.0;

    bool bassIsRoot() const { return bassPc == rootPc; }
};

// ── Per-slice chord decision (signed design §7) ──────────────────────────────
struct SliceChord {
    int sliceIndex = 0;                            ///< index into the slice vector
    bool hasChord = false;                         ///< false = no scorable candidate (empty / sub-gate slice)
    ChordSliceCandidate chosen;                    ///< the decided chord (root + quality + bass/inversion)
    std::vector<ChordSliceCandidate> alternatives; ///< other distinct chords, ranked (∪ prevailing)
    double confidence = 0.0;                       ///< margin to the best DIFFERENT (root,quality) chord
    bool uncertain = false;                        ///< confidence < uncertaintyMargin

    // ── Membership (Increment B) — STUBBED EMPTY this increment ──────────────
    // Binary chord-tone vs non-chord-tone membership is the real lever (design
    // §11) and the per-note decision is built next. Here every sounding note is
    // implicitly a chord tone (no NCT called); these stay empty so the §10
    // membership metric reports the trivial baseline.
    std::vector<int> chordTonePcs;                 ///< empty (Increment B)
    std::vector<int> nonChordTonePcs;              ///< empty (Increment B)
};

// ── The decoder ──────────────────────────────────────────────────────────────
class ChordSliceDecoder
{
public:
    /// Name a chord for every Layer-2 slice, in order (one SliceChord per slice).
    ///
    /// @param keySignatureFifths  the key the slices are scored under (a diatonic
    ///                            PRIOR; -7..+7). One key for the whole run this
    ///                            increment (the notated signature in the
    ///                            diagnostic); per-slice Layer-3 feed-forward is a
    ///                            later refinement.
    /// @param keyMode             the mode of that key (diatonic scale for the prior).
    /// @param chordPrefs          the chord scorer's preferences — the user STYLE
    ///                            PRESET enters here, unchanged (Jazz lowers the
    ///                            extension threshold, etc.). minDistinctPcs is
    ///                            overridden from @p decoderPrefs on a local copy.
    /// @param decoderPrefs        this decoder's own tunable settings.
    /// @param excludeStaves       staves whose pitches are excluded from every
    ///                            slice's window (e.g. a chord track). Empty (the
    ///                            default) = score every staff.
    static std::vector<SliceChord> decode(
        const std::vector<slicing::Slice>& slices,
        const notemodel::NoteModel& noteModel,
        int keySignatureFifths,
        KeySigMode keyMode,
        const ChordAnalyzerPreferences& chordPrefs = kDefaultChordAnalyzerPreferences,
        const ChordSliceDecoderPreferences& decoderPrefs = kDefaultChordSliceDecoderPreferences,
        const std::set<std::size_t>& excludeStaves = {});

    /// Re-name a sub-range [first, last] (inclusive), consistent with the
    /// incremental contract of the layers below. Because the per-slice decision
    /// is context-free (the chosen chord + confidence depend only on the slice's
    /// own window, not on any prior decision), a sub-range re-decode reproduces
    /// the matching slice of a full decode EXACTLY — including the prevailing
    /// alternative of the first slice (one slice of look-back is recomputed).
    /// Returns SliceChord entries with global sliceIndex (first..last).
    static std::vector<SliceChord> redecodeRange(
        const std::vector<slicing::Slice>& slices,
        const notemodel::NoteModel& noteModel,
        int keySignatureFifths,
        KeySigMode keyMode,
        int first, int last,
        const ChordAnalyzerPreferences& chordPrefs = kDefaultChordAnalyzerPreferences,
        const ChordSliceDecoderPreferences& decoderPrefs = kDefaultChordSliceDecoderPreferences,
        const std::set<std::size_t>& excludeStaves = {});

    // ── Scorer-independent core (for behaviour/branch tests) ──────────────────
    //
    // The ranking + confidence + alternatives over a precomputed candidate list,
    // with NO dependency on the chord scorer or the note model. The synthetic
    // behaviour tests inject `candidates` (and an optional prevailing chord) by
    // hand and assert the chosen chord, the confidence margin, the ranked-and-
    // capped alternatives, and the "uncertain" mark.

    /// Decide one slice from a precomputed candidate list (one entry per cube
    /// cell, in any order — ranking is internal). The chosen chord is the
    /// highest-vertical-score candidate; confidence is its margin to the best
    /// DIFFERENT (root, quality) candidate; the prevailing chord (if given and
    /// expressible among the candidates) is kept among the alternatives.
    static SliceChord decideSlice(
        int sliceIndex,
        const std::vector<ChordSliceCandidate>& candidates,
        const std::optional<ChordSliceCandidate>& prevailing,
        const ChordSliceDecoderPreferences& decoderPrefs = kDefaultChordSliceDecoderPreferences);
};

} // namespace mu::composing::analysis::chordslice
