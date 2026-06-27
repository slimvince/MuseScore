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
// LAYER 4 — the CHORD-SYMBOL per-slice path (Increment A + B + G1 + G2/G3).
//
// For each Layer-2 slice this names a chord (root + quality + bass/inversion)
// by running the EXISTING chord scorer (analyzeChord) over the slice's note
// window and reading the COMPLETE candidate cube it surfaces — exactly the way
// the Layer-3 key/mode decoder reads analyzeKeyMode's 252-candidate dump. The
// per-slice result carries the chosen chord, the ranked alternatives, a
// confidence (the margin to the best DIFFERENT chord) and an "uncertain" mark.
//
// WHAT IS BUILT (signed design cowork_layer4_chordsymbol_design.md; pre-build
// audit cc_layer4_audit_dossier.md):
//   * Increment A — the per-slice path + grading harness: reuse the one scorer
//     and its cube; do NOT fork a second scorer.
//   * Increment B — per-note chord-tone-vs-NCT MEMBERSHIP (the two-pass,
//     neighbour-aware decision) + the adaptive lazy-extend window. The membership
//     sets on SliceChord are populated (design §5).
//   * G1 — commit / inherit / abstain + the >=3-template-tone SUFFICIENCY gate
//     (design §4 step 3, §5 step 4): a new chord symbol is committed only from
//     enough notes; a thin slice consistent with the prevailing chord INHERITS it;
//     otherwise the slice ABSTAINS (no committed chord, the competing readings
//     carried). This is the phantom-root guard — see applyCommitDecision.
//   * G2/G3 — the three-tier structure-first membership LADDER + the plausibility
//     check (design §5 step 3). Membership now classifies each focal note by
//     stepwise structure in three tiers (stepwise-embellishing → NCT regardless of
//     weight; no-stepwise-connection → chord-tone extension regardless of weight;
//     one-sided → metric weight decides), and tests the candidate's REQUIRED
//     (template) tones through the SAME ladder — a template tone behaving as a
//     Tier-1 embellishment makes the candidate implausible (the spurious-seventh /
//     Cadd9 discriminator). The G1 inherit is relaxed to the ladder: a thin slice
//     whose extra notes are stepwise NCTs of the prevailing chord now INHERITS it
//     (Step-1 inherited on template tones only). See classifyMembership /
//     notesConsistentWithPrevailing.
//
// WHAT IS NOT YET BUILT (deferred — STOP if you start building these here):
//   * the deterministic spelling-PIN for the symmetric (dim7/aug) root, the new
//     diminished-seventh / minor-major TYPES, and the confidence composite +
//     open-question label (Increment C / G4 / G5 / G6).
// So the chosen chord is the existing scorer's per-window winner; the "complete
// candidate list" is the surfaced cube ranked and pruned to top-K; no new chord
// type and no spelling pin land here.
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
//      "uncertain" when that margin is below uncertaintyMargin.
//   5. Commit / inherit / abstain (G1, inherit relaxed by G2). The chosen chord is
//      committed only if >= sufficiencyChordTones of its own template tones are
//      present in the slice AND the margin clears; a thin (insufficient) slice whose
//      notes are all consistent with the prevailing chord — each a template tone of
//      it OR a stepwise embellishment (non-chord tone) of it — inherits it; any other
//      slice abstains (hasChord=false, competing readings carried).
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

    // ── Increment B: adaptive lazy-extend window (design §2/§3) ──────────────
    //
    // The window starts at the narrow base (±contextSlices) and lazy-extends one
    // slice each side at a time, stopping as soon as it holds >= minHarmonyPcs
    // distinct pitch classes (the prevailing harmony is "in view") OR reaches
    // ±maxContextSlices (bounded by one harmony's worth of figuration — never a
    // phrase; that wide context belongs to Layer 3). A dense (triad) slice already
    // meets minHarmonyPcs so it keeps the base window; only thin (arpeggio / dyad)
    // slices extend. With maxContextSlices == contextSlices the window is fixed
    // (the Increment-A behaviour).

    /// Upper bound on the window half-width (neighbour slices each side).
    int maxContextSlices = 3;

    /// Distinct-PC target that stops the lazy extension (a triad = 3).
    int minHarmonyPcs = 3;

    // ── Increment B: per-note membership (CT vs NCT) + its score feedback ────
    //
    // The lever (design §5/§11). For the chosen chord, each FOCAL sounding note is
    // classified chord-tone vs non-chord-tone from its metric salience and its
    // local stepwise treatment (passing/neighbour/suspension) — read off the
    // INDEXED Layer-1 NoteEvent stream, never the aggregated pc view. The
    // classification feeds back into candidate selection: a candidate is penalised
    // for every STRUCTURAL (non-embellishment) focal note it leaves out of its
    // chord, so the chosen chord best explains the slice as "a chord plus its
    // non-chord tones".

    /// Master switch. OFF reproduces Increment-A behaviour EXACTLY (no NCT called,
    /// no re-rank; only the adaptive window above differs, and that too collapses to
    /// the fixed window when maxContextSlices == contextSlices).
    bool enableMembership = true;

    /// Run the neighbour-aware second pass (design §4 two-pass). OFF = membership
    /// from the slice's own notes + key prior alone (no neighbour-chord context).
    bool twoPass = true;

    /// Metric-weight threshold the three-tier ladder (design §5 step 3) consults ONLY at
    /// its third tier — the one-sided (appoggiatura / escape / incomplete neighbour) case:
    /// a metrically-asserted note at/above this salience is a chord-tone extension, below
    /// it a non-chord tone. (Tiers 1 and 2 — both-sides-stepwise and no-side-stepwise —
    /// are settled by structure alone, regardless of weight.) salience = metricWeight
    /// [0.5,1] × min(1, durationQn / membershipReferenceDurationQn). Seed; swept later.
    double membershipSalienceThreshold = 0.55;

    /// Duration (quarter notes) at/above which a note is full-length for salience.
    double membershipReferenceDurationQn = 1.0;

    /// Strength of the membership feedback into candidate selection (design §5 step 3,
    /// the plausibility penalty G3): a candidate's score is reduced by membershipPenaltyWeight
    /// × salience for every REQUIRED (template) tone that behaves as a Tier-1 stepwise
    /// embellishment — an "implausible chord tone" (a passing tone forced to be a chord
    /// member: the spurious seventh / Cadd9 reading). 0 = label notes but do not re-rank
    /// (isolates the membership-metric effect from the chord-root effect). Seed.
    double membershipPenaltyWeight = 0.6;

    /// Tick tolerance for "immediately adjacent" in the stepwise test (0 = strictly
    /// contiguous onset/release).
    int stepwiseGapToleranceTicks = 0;

    // ── G1: commit / inherit / abstain + sufficiency gate (design §4 step 3, §5 step 4) ──
    //
    // The phantom-root guard (the headline Step-0 lever). After ranking + membership,
    // the top candidate is COMMITTED only when it is sufficiently evidenced (>=
    // sufficiencyChordTones of its own template tones present) AND clearly ahead (the
    // margin clears uncertaintyMargin); a thin slice that cannot fix its own chord
    // INHERITS the prevailing chord when its notes are consistent with it; otherwise
    // the slice ABSTAINS (no committed chord — the competing readings are still
    // carried). See ChordSliceDecoder::applyCommitDecision.

    /// Master switch. OFF reproduces the pre-G1 always-commit behaviour EXACTLY
    /// (every scorable slice commits its top candidate; no inherit, no abstain).
    bool enableCommitDecision = true;

    /// Sufficiency gate: the minimum number of the chosen candidate's OWN template
    /// tones (root/3rd/5th/7th) that must be PRESENT in the slice for a new chord
    /// symbol to be committed — a complete triad's worth (design §5 step 4). This
    /// count is the candidate's template-tone presence, independent of the
    /// (extra-note) membership rule. A slice with fewer either inherits or abstains.
    int sufficiencyChordTones = 3;
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

// ── The commit / inherit / abstain trichotomy (design §4 step 3, §5 step 4) ───
//
// The G1 decision over a ranked slice, distinct from the margin-only `uncertain`
// flag: Commit names a new chord symbol (sufficient + clear margin); Inherit carries
// the prevailing chord forward across a thin, consistent slice; Abstain declines to
// commit (no chord, the open question — carried readings — handed to Architectural
// Layer 5).
enum class SliceDecision {
    Commit,     ///< a new chord symbol committed from enough notes
    Inherit,    ///< thin slice consistent with the prevailing chord — carry it forward
    Abstain     ///< no commit (insufficient + no consistent prevailing, or low margin)
};

// ── Per-slice chord decision (signed design §7) ──────────────────────────────
struct SliceChord {
    int sliceIndex = 0;                            ///< index into the slice vector
    bool hasChord = false;                         ///< false = no committed chord (empty/sub-gate slice OR an abstain)
    ChordSliceCandidate chosen;                    ///< the decided chord (root + quality + bass/inversion); on Inherit = the prevailing chord
    std::vector<ChordSliceCandidate> alternatives; ///< other distinct chords, ranked (∪ prevailing)
    double confidence = 0.0;                       ///< margin to the best DIFFERENT (root,quality) chord
    bool uncertain = false;                        ///< confidence < uncertaintyMargin (the margin cue feeding the decision)
    SliceDecision decision = SliceDecision::Commit; ///< G1: commit / inherit / abstain (see applyCommitDecision)

    // ── Membership (Increment B + G2/G3) — the per-note CT vs NCT decision ────
    // Binary chord-tone vs non-chord-tone membership, the real lever (design §11),
    // over the FOCAL slice's sounding pitch classes, by the three-tier structure-first
    // ladder (design §5 step 3). A pc is a non-chord tone when ALL of its focal notes
    // classify embellishment-like (Tier 1 stepwise-embellishing, or a weak Tier-3
    // one-sided tone) and the pc is not a template tone of the chosen chord; otherwise
    // it is a chord tone (including the added 6th/9th that "falls out" as a structural
    // extension — Tier 2, or a metrically-asserted Tier 3 — design §5). Empty only when
    // the slice has no chord / no sounding notes, or membership is disabled.
    std::vector<int> chordTonePcs;                 ///< focal pcs the chosen chord explains
    std::vector<int> nonChordTonePcs;              ///< focal pcs called non-chord tones
};

// ── A focal sounding note, projected from the Layer-1 NoteEvent stream ────────
//
// The per-note view the membership decision reads (NOT the aggregated pc view): one
// entry per eligible note sounding in the focal slice, with the metric salience
// inputs (beat-weight at onset + sounding duration) and the voice/onset/release the
// stepwise (passing/neighbour/suspension) test needs. Built in decode() through the
// INDEXED NoteModel::overlapping; injected by hand in the behaviour tests.
struct FocalNote {
    int pitch = 0;             ///< ppitch
    int onset = 0;             ///< tie-resolved onset tick
    int release = 0;           ///< tie-resolved release tick
    int voice = 0;             ///< voice (the stepwise test is per-voice / melodic)
    double metricWeight = 1.0; ///< normalised beat weight at onset [0.5,1.0]
    double durationQn = 0.0;   ///< sounding duration in quarter notes

    int pc() const { return ((pitch % 12) + 12) % 12; }
};

// ── The result of classifying one slice's focal notes against a chord ─────────
struct MembershipResult {
    std::vector<int> chordTonePcs;
    std::vector<int> nonChordTonePcs;
    /// The membership feedback into candidate selection (design §4 step 2). Two additive
    /// contributions, in the two directions the chord-vs-membership decision must separate:
    ///   * a chord's REQUIRED (template) tone that behaves as a Tier-1 stepwise embellishment
    ///     — the "implausible chord tones" penalty (design §5 step 3, the Step-2 G3 addition):
    ///     the candidate forces a passing tone to be a chord member (the spurious seventh /
    ///     Cadd9 reading) → pull back the over-rich chord; AND
    ///   * an EXTRA (non-template) focal note the chord can only absorb as an added 6th/9th
    ///     — the richer-chord direction the old penalty already caught: a chord that leaves a
    ///     STRUCTURAL focal note outside its basic template is a worse explanation of the
    ///     slice → prefer the chord whose template includes it (this is what gives the
    ///     focal-fitting chord its selection margin).
    /// An extra EMBELLISHMENT note (a non-chord tone) is charged nothing (the chord explains
    /// it as a passing/neighbour tone — design §5 step 1).
    double implausibilityPenalty = 0.0;
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
    /// incremental contract of the layers below. The per-slice RANKING is context-free
    /// (the chosen candidate + confidence depend only on the slice's own window), so a
    /// sub-range re-decode reproduces the matching slice of a full decode EXACTLY when
    /// the prevailing chain across the range boundary is recovered by the one slice of
    /// look-back (true when `first <= 1`, or when slice `first-1` committed/abstained —
    /// a context-free decision). With G1, an INHERIT makes the chosen chord depend on
    /// the carried prevailing chain, so a deep `first` landing mid-inherit-run is only
    /// reproduced up to that bounded look-back (the chain can span more than one slice).
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

    /// Classify a slice's FOCAL notes as chord-tone vs non-chord-tone for @p chord,
    /// given the provisional neighbour chords (design §5 step 3). Pure — no scorer /
    /// note-model dependency — so the behaviour tests inject FocalNotes + neighbour
    /// chords by hand. @p window is the broader (adaptive-window) note stream the
    /// per-voice stepwise test reads its melodic neighbours from; it must contain the
    /// focal notes (focal ⊆ window). prevChord / nextChord absent ⇒ no neighbour
    /// context (the two-pass-off / boundary case). Returns the chord-tone and
    /// non-chord-tone pc sets plus the implausibility penalty the feedback charges.
    static MembershipResult classifyMembership(
        const ChordSliceCandidate& chord,
        const std::vector<FocalNote>& focal,
        const std::vector<FocalNote>& window,
        const std::optional<ChordSliceCandidate>& prevChord,
        const std::optional<ChordSliceCandidate>& nextChord,
        const ChordSliceDecoderPreferences& decoderPrefs = kDefaultChordSliceDecoderPreferences);

    /// Count the DISTINCT focal pitch classes that are TEMPLATE tones (root/3rd/5th/
    /// 7th…) of @p chord — the sufficiency gate's chord-tone source (design §5 step 4).
    /// Pure; reuses the one chord-tone oracle function::bassIsTemplateChordTone, so the
    /// count is the candidate's own structural presence, INDEPENDENT of the (extra-note)
    /// membership rule. A complete triad present returns 3.
    static int templateTonePresenceCount(
        const ChordSliceCandidate& chord,
        const std::vector<FocalNote>& focal);

    /// Apply the commit / inherit / abstain decision (design §4 step 3, §5 step 4) on
    /// top of a ranked slice @p sc (from decideSlice). The sufficiency gate counts the
    /// CHOSEN candidate's own template tones present in @p focal (templateTonePresenceCount
    /// — the phantom-root guard, independent of membership). Sets @p sc.decision and:
    ///   * Commit  — sufficiency AND margin both pass: @p sc is left committed (hasChord
    ///               stays true, chosen unchanged).
    ///   * Inherit — sufficiency fails but @p sc's focal notes are all consistent with
    ///               @p prevailing — each a template tone of it OR a stepwise embellishment
    ///               (non-chord tone) of it, judged by the G2 membership ladder over @p
    ///               window + @p prevChord / @p nextChord: chosen is replaced by the
    ///               prevailing chord (carried forward); hasChord stays true; uncertain
    ///               cleared.
    ///   * Abstain — any other slice (insufficient with no consistent prevailing, OR
    ///               sufficient but low margin, OR no scorable candidate): hasChord is
    ///               cleared (the no-chord / open marker) and uncertain set; the ranked
    ///               competing readings (alternatives) are kept.
    /// @p window is the broader (adaptive-window) note stream the stepwise inherit test
    /// reads (focal ⊆ window); an empty window degrades to the conservative template-only
    /// inherit. @p prevChord / @p nextChord are the provisional neighbour chords (absent on
    /// the membership-off path). Pure — no scorer / note-model dependency — so the
    /// behaviour tests inject the ranked SliceChord + focal/window notes + prevailing/
    /// neighbour chords by hand. With decoderPrefs.enableCommitDecision == false this is a
    /// no-op (decision left Commit): the pre-G1 always-commit behaviour.
    static void applyCommitDecision(
        SliceChord& sc,
        const std::vector<FocalNote>& focal,
        const std::vector<FocalNote>& window,
        const std::optional<ChordSliceCandidate>& prevailing,
        const std::optional<ChordSliceCandidate>& prevChord,
        const std::optional<ChordSliceCandidate>& nextChord,
        const ChordSliceDecoderPreferences& decoderPrefs = kDefaultChordSliceDecoderPreferences);
};

} // namespace mu::composing::analysis::chordslice
