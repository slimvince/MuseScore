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

// ── composing/analysis/key/keymodesequence ──────────────────────────────────
//
// LAYER 3 — the KEY/MODE SEQUENCE DECODER: decide the key/mode for each Layer-2
// slice as ONE consistent sequence over time, rather than per-region in
// isolation. A dedicated key-path Viterbi over (tonic × mode) states.
//
// Why a whole-sequence decision (signed design §1/§2): deciding one region at a
// time is the measured ceiling on the two largest key/mode errors — (a) relative
// major vs relative minor (same notes, a single region cannot choose), and (b)
// brief tonicization misread as real modulation. Both need the surrounding music,
// which is exactly what one best-sequence decode supplies.
//
// HOW IT WORKS (signed design §5):
//   1. Local-fit scoring (emission). For each slice, score every (tonic × mode)
//      candidate with the existing KeyModeAnalyzer over a small pitch-context
//      window (slice ± windowBeats), built through the LAYER-1 INDEXED query
//      (NoteModel::overlapping) — NOT the older direct-score-walk pitch collector
//      (collectPitchContext), which would re-introduce the O(N²) cost the indexing
//      removed. The full 252-candidate vector is read via analyzeKeyMode's dumpOut.
//   2. Change cost. stay = 0; switch = base + per-fifth-step × circle-of-fifths
//      distance + an extra penalty for the relative-major/minor (same-signature)
//      switch. The source-true starting magnitudes (2.0 / 0.60 / 2.0) are the
//      resolver's live hysteresis/key-distance margins, already in emission-score
//      units; they are SETTINGS, not constants (effort-retrofit hygiene).
//   3. Best whole sequence. A dedicated forward Viterbi + back-pointers, linear
//      in slices (ChordPathDecoder is chord-specific and not reusable).
//   4. Per-slice results. The chosen key/mode; ranked alternatives; a CONFIDENCE
//      = the sequence margin (best whole-sequence total vs the best total forced
//      through a different key/mode at that slice — a forward+backward read of the
//      Viterbi tables); and an "uncertain" mark where that margin is low.
//
// State pruning (design §5.1 "best-scoring candidates ∪ the running incumbent"):
// the lattice state set is the GLOBAL UNION of each slice's emission top-K. Every
// state in that union is scored at EVERY slice via the full 252-dump, so the
// running/incumbent key — which is top-K where it prevails, hence in the union —
// always has a state even on a transient slice that scores something else higher.
// This realizes "keep the incumbent alive" deterministically and path-
// independently (the union depends only on emissions, never on the decode), which
// is also what makes a pinned sub-range re-decode reproduce the matching slice of
// a full decode exactly (redecodeRange, R2).
//
// This layer is the FIRST to use the user's style preset (as a weak mode prior);
// that enters automatically because the emission reuses analyzeKeyMode(ctx,
// fifths, prefs, …) with the preset's KeyModeAnalyzerPreferences — no new wiring.
//
// SCOPE: key/mode only, from the notes only (no chord/function/cadence — those are
// later layers; passing-vs-real modulation is handled by the change cost). The
// genuinely ambiguous residual (relative pair, modulation seam) is flagged
// "uncertain" and left for the later, gated key-and-chord step — never forced.
//
// WIRING (as-built): this decoder IS the live key path. The region analyzer
// (regionanalyzer.cpp, analyzeRegions) runs ONE whole-score decode() over the
// Layer-2 change-point slice grid and each Pass-1 coarse region takes its
// duration-majority decoder key over the slice run it spans — replacing the old
// per-region key argmax (resolveKeyAndModeRanked) at the Pass-1 seam. The
// whole-sequence change cost supplies the smoothing the per-region hysteresis used
// to. Three fidelity ties keep it faithful to the resolver-as-graded: the same
// excluded staves, the same Baroque partial-signature-corrected fifths + declared
// mode, and the emission-scale C1 confidence the downstream 0.8 key-confidence
// gates expect. The committed BIR delta of this wiring is the ratified
// −4 / +1 / −4 (Baroque / Jazz / Default), all class-(a) symmetric-rotation churn
// (see CLAUDE.md gate section). The decoder remains pure/static; the read-only
// batch_analyze --decode-keymode diagnostic still exercises it directly.
//
// Selection-aware reach-back (cowork_layer3_reachback_design.md, Phase 3) wraps the
// SAME decode() in an extend → re-slice → re-decode loop in the orchestrator; the
// decoder itself is untouched (a pure function of the slices it is given).
//
// See cowork_layer3_keymode_design.md (signed) + cc_layer3_decoder_audit_dossier.md.

#include <cstddef>
#include <optional>
#include <set>
#include <vector>

#include "keymodeanalyzer.h"
#include "composing/analysis/notemodel/note_model.h"
#include "composing/analysis/slicing/slicer.h"

namespace mu::composing::analysis::keymodeseq {

// ── Tunable settings (effort-retrofit hygiene) ───────────────────────────────
//
// Every cost-driving choice is a SETTING here, never a hardcoded constant, so a
// future "effort" preset (quick / normal / ambitious) is a clean retrofit. The
// defaults are the source-true starting magnitudes the decoder audit read; the
// impl's held-out sweep tunes them.
struct KeyModeSequencePreferences {
    // ── State pruning ────────────────────────────────────────────────────────
    /// Per-slice emission candidates kept; the lattice state set is the union of
    /// these across all slices (∪ the running incumbent — see header). [audit §2.2]
    int topK = 8;

    // ── Change cost (emission-score units; design §5.2 / audit §2.3) ──────────
    /// Base "change penalty" for any key/mode switch (= resolver hysteresisMargin).
    double changeBaseCost = 2.0;
    /// Per circle-of-fifths step between the two key signatures
    /// (= resolver keySignatureDistancePenalty).
    double changePerFifthStep = 0.60;
    /// Extra penalty for a relative-major/minor (same-signature, different-mode)
    /// switch (= resolver relativeKeyHysteresisMargin). The "hardest pair".
    double relativePairExtraCost = 2.0;

    // ── Emission window (per slice; design §5.1 / audit §2.4) ─────────────────
    /// Symmetric look-around added to each side of the slice span, in quarter-note
    /// beats. The per-slice transition penalty (not a fat window) now carries the
    /// long-range coherence the old 16-beat look-back faked, so the window is small.
    double windowBeats = 4.0;
    /// Time decay per measure for notes away from the slice (= DECAY_RATE).
    double decayRate = 0.7;
    /// Weight multiplier for notes that onset AFTER the slice end (= LOOKAHEAD_WEIGHT).
    double lookaheadWeight = 0.5;
    /// Length-scale of the time decay, in beats per decay unit (one 4/4 measure).
    double beatsPerDecayUnit = 4.0;

    // ── Confidence (sequence margin; design §5.4 / audit §2.5) ────────────────
    /// A slice is marked "uncertain" when its sequence margin is below this.
    double uncertainThreshold = 1.0;

    /// Cap on alternatives kept per slice in SliceKeyMode (ranked, excluding the
    /// chosen). 0 = keep all surviving states.
    int maxAlternatives = 4;
};

/// Global default sequence preferences.
inline constexpr KeyModeSequencePreferences kDefaultKeyModeSequencePreferences{};

// ── Per-slice decision (signed design §3 / §7) ───────────────────────────────
struct SliceKeyMode {
    int sliceIndex = 0;                                   ///< index into the slice vector
    KeyModeAnalysisResult chosen;                         ///< the decided key/mode
    std::vector<KeyModeAnalysisResult> alternatives;      ///< other surviving candidates, ranked
    double confidence = 0.0;                              ///< sequence margin (best vs best-different-key/mode)
    bool uncertain = false;                               ///< confidence < uncertainThreshold
};

// ── The decoder ──────────────────────────────────────────────────────────────
class KeyModeSequenceDecoder
{
public:
    /// A single lattice state: a (tonic, mode) candidate. `keySignatureFifths` is
    /// the enharmonic-resolved notated signature (for labels/output); `ionianPc` is
    /// the parent Ionian tonic pitch class (the change-cost distance is computed
    /// over these, so no enharmonic resolution is needed for the cost).
    struct State {
        int tonicPc = 0;
        KeySigMode mode = KeySigMode::Ionian;
        int keySignatureFifths = 0;
        int ionianPc = 0;
    };

    /// Decide the key/mode sequence over the given slices (design §3 "decide the
    /// key/mode sequence"). One SliceKeyMode per slice, in order.
    ///
    /// @param keySigFifths  the notated key signature (a weak hint only).
    /// @param declaredMode  the notated key's mode (Ionian for major, Aeolian for
    ///                      minor), a WEAK declared-mode tiebreaker the emission
    ///                      applies via KeyModeAnalyzerPreferences.declaredModePenalty
    ///                      (1.0 — demoted from a wall to a hint). nullopt = pure
    ///                      note-based, no declared-mode influence. This is the
    ///                      design's "signature as a weak hint" use, matching the
    ///                      per-region resolver; it chiefly settles relative-pair
    ///                      (major/minor) ambiguity where the note evidence is close.
    /// @param keyPrefs      the emission scorer's preferences — the user STYLE
    ///                      PRESET enters here (weak mode prior), unchanged.
    /// @param seqPrefs      the decoder's own tunable settings.
    /// @param excludeStaves staves whose pitches are excluded from every slice's
    ///                      emission context (threaded to pitchContextOverSpan).
    ///                      Production analysis excludes staves (e.g. a chord
    ///                      track), so the decode must too — without this the
    ///                      decoded key would include excluded-staff pitches.
    ///                      Empty (the default) = score every staff (the as-graded
    ///                      held-out condition; the batch --decode-keymode path).
    ///
    /// SIDE-EFFECT (since the Layer-3 wiring): each returned SliceKeyMode's
    /// `chosen.normalizedConfidence` is the EMISSION-scale confidence for the
    /// chosen state at that slice — the analyzeKeyMode winner sigmoid
    /// (keymodeanalyzer.cpp) computed over keyPrefs, so it is the input the 0.8
    /// downstream key-confidence annotate gate consumes (C1) — an INTERNAL gate
    /// input, NOT the Layer-3 boundary confidence (D-L3a). The sequence-margin
    /// confidence — THE Layer-3 boundary confidence — remains on
    /// `SliceKeyMode.confidence`.
    static std::vector<SliceKeyMode> decode(
        const std::vector<slicing::Slice>& slices,
        const notemodel::NoteModel& noteModel,
        int keySigFifths,
        std::optional<KeySigMode> declaredMode = std::nullopt,
        const KeyModeAnalyzerPreferences& keyPrefs = kDefaultKeyModeAnalyzerPreferences,
        const KeyModeSequencePreferences& seqPrefs = kDefaultKeyModeSequencePreferences,
        const std::set<std::size_t>& excludeStaves = {});

    /// Re-decide the sub-range [first, last] (inclusive) holding the key/mode at
    /// the two ends fixed to @p leftPin / @p rightPin (design §3 "re-decide a
    /// sub-range"; R2). The full lattice (state set + emissions) is rebuilt over
    /// all slices, so a pinned sub-range re-decode reproduces the matching slice of
    /// a full decode EXACTLY (the §5 property). The incremental-emission
    /// optimization (re-score only the dirty span) is the later editor-wiring step.
    ///
    /// Returns SliceKeyMode entries with global sliceIndex (first..last).
    static std::vector<SliceKeyMode> redecodeRange(
        const std::vector<slicing::Slice>& slices,
        const notemodel::NoteModel& noteModel,
        int keySigFifths,
        std::optional<KeySigMode> declaredMode,
        int first, int last,
        const KeyModeAnalysisResult& leftPin,
        const KeyModeAnalysisResult& rightPin,
        const KeyModeAnalyzerPreferences& keyPrefs = kDefaultKeyModeAnalyzerPreferences,
        const KeyModeSequencePreferences& seqPrefs = kDefaultKeyModeSequencePreferences,
        const std::set<std::size_t>& excludeStaves = {});

    // ── Scorer-independent core (for behaviour/branch tests) ──────────────────
    //
    // The Viterbi + change-cost + confidence over a precomputed lattice, with NO
    // dependency on KeyModeAnalyzer. The synthetic behaviour tests (single-key,
    // relative-pair tilt, brief tonicization, sustained modulation, near-vs-remote)
    // inject `states` + `emissions` by hand and assert the decoded sequence.

    /// emissions[t][s] = local-fit score of state s at slice t (parallel to
    /// `states`). Optional endpoint pins (state index, or -1 for none) force the
    /// decode through a fixed state at the first / last column (redecodeRange).
    static std::vector<SliceKeyMode> decodeLattice(
        const std::vector<State>& states,
        const std::vector<std::vector<double>>& emissions,
        const KeyModeSequencePreferences& seqPrefs = kDefaultKeyModeSequencePreferences,
        int pinFirstState = -1,
        int pinLastState = -1);

    /// The change cost τ(a → b) in emission-score units (design §5.2). Exposed for
    /// the change-cost unit tests. stay = 0; switch = base + per-fifth × cof-steps
    /// + relative-pair extra.
    static double changeCost(const State& a, const State& b,
                             const KeyModeSequencePreferences& seqPrefs);
};

} // namespace mu::composing::analysis::keymodeseq
