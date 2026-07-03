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

// ── composing/analysis/function/functionprogression ──────────────────────────
//
// Architectural Layer 5 (FUNCTION) — the PROGRESSION MODEL: the shared, key-/
// chord-fed surface evidence the cadence detector (Step 2) and the resolver
// (Step 3) both stand on. Spec: cowork_layer5_function_design.md (SIGNED) §5.0.
// Build plan: cowork_phase5c_l5_build_plan.md Step 1.
//
// This is PURE predicate logic over the committed-chord stream of a region — no
// cadence (Step 2), no resolution decisions (Step 3). It states, by enumerable
// rule, three §5.0 concepts:
//   • "a licensed (real) progression"  — is a root motion one of the standard
//     functional successions? (the enumerable test, no preference);
//   • "prevailing harmony"             — the committed chord of the nearest
//     metrically-strong slice at or before a slice;
//   • "the established next function"   — the next committed (non-abstained)
//     chord's function.
//
// DORMANT (build §6): this module has NO production consumer — nothing in src/
// calls it; it is exercised only by its unit tests. So adding it is byte-identical
// on production by construction (the firewall). It becomes load-bearing when the
// function layer engages (Phase 5d). The new L5 layer is DISTINCT from the
// misnamed predecessor `harmonicfunctionlayer` (the chord-identity COMPETITION
// pipeline); that rename is an engage-step structural item, not this step.
//
// REUSE, NOT DUPLICATE (build §1): the pre-amendment licensing sub-tests reuse the
// SAME root-motion arithmetic the competition pipeline already uses as scoring bonuses
// — wSeqBonus (descending-fifth, delta == 5), wDimBonus (leading-tone, delta == 1),
// resolutionEdgeBonus (dim/half-dim resolution targets) in harmonicfunctionlayer.
// Here that arithmetic is a LICENSING test (a boolean), not a score term: §5.0's
// "the licensing itself is the rule here; the numeric preference among licensed
// readings is a precision-phase weight" — so this step computes no weight.
//   (The §15-12 amendment (RATIFIED 2026-07-03) added THREE motions with NO bonus
//   analogue — the ascending fifth (delta 7), the descending second (delta 10/11),
//   and the diatonic diminished fifth (delta 6 into a diminished triad). They exist
//   precisely because the pre-amendment set descended from the bonus signals and
//   omitted them; they are pure theory completions, still licensing booleans that
//   compute no weight. See isAscendingFifth / isDescendingSecond /
//   isDiatonicDiminishedFifth below.)
//
// PRODUCER-AGNOSTIC: the predicates read only the small view types below. At
// engage they are mapped from the L4 decoder's committed chord
// (chord/chordslicedecoder.h SliceChord.chosen) or the region chord results
// (region/harmonicrhythm.h HarmonicRegion.chordResult); the predicates never read
// a producer type, so this module compiles free of the decoder / region headers.
//
// NO CONSTANTS (build §4): the progression model is an enumerable rule set; it
// introduces no weight, threshold, or margin. "Metrically strong" is realized
// parameter-free as a local metric-weight maximum (the structural-peak convention
// the sibling Layer-1.5 primitive phraseboundaryview §4.4 already uses), not a
// tuned cutoff.
//
// ── D5 DEPENDENCY MAP — the GRAMMAR owner (mirror at harmonicvocabulary.h) ─────
//
// TWO places in the system know about chord successions, and they have ONE owner
// each (the D5 one-owner ruling, cowork_progression_schema_design.md §6-D5, user-
// ratified 2026-07-02 with the make-it-explicit rider). This module — the pairwise
// LICENSING GRAMMAR (isLicensedProgression) — owns "which root motions are licensed
// at all". The Harmonic Vocabulary (vocabulary/harmonicvocabulary) owns the NAMED
// progressions and substitutions (the catalog).
//   • Changing the GRAMMAR (the licensed root motions) → change THIS module ONLY.
//     The catalog never needs an edit for a grammar change — but the consistency
//     test re-runs, and a catalog entry that now fails it is flagged.
//   • Changing the CATALOG (add/edit a named progression or substitution) → change
//     the Vocabulary ONLY. The grammar never needs an edit — but a new entry must
//     PASS the consistency test (every adjacent chord pair licensed); a failure
//     means the entry is mis-encoded OR a genuine grammar gap was found (escalate,
//     do NOT tag around it).
//   • The two are NOT derived from each other (the grammar licenses MORE than
//     convention names; the catalog is enumerative and grows from evidence). The
//     ONLY coupling is the CONSISTENCY TEST, and it runs ONE WAY (catalog → grammar):
//     tests/progressionrecognizer_tests.cpp asserts every adjacent chord pair of
//     every catalog entry passes isLicensedProgression.
//   • SCOPE of "the ONLY coupling" (grammar-completion ruling, 2026-07-03): that
//     statement governs the CATALOG↔GRAMMAR relationship. The in-layer CONSUMERS of
//     this grammar (function/functionresolver, function/functionoutput,
//     function/functioncadence) are ordinary same-layer callers, expected to MOVE WITH
//     the grammar — a grammar change may shift their behaviour and their tests (e.g. the
//     §5.5 disambiguation that no longer separates two now-both-licensed readings falls
//     to the structural tie-breaks / honest open mark; the numeric preference AMONG
//     licensed readings is the deferred Stage-5 lever, L5 §15-13).
//   • RULED KNOWN GAPS (2026-07-02) — ★ CLOSED by the §15-12 grammar completion
//     (RATIFIED 2026-07-03). The consistency test had found 6 catalog entries / 11
//     motions the pre-amendment §5.0 grammar did NOT license (plagal / ascending-fifth
//     = delta 7; descending-second = delta 10/11; the diatonic diminished-fifth =
//     delta 6 into a diminished triad) — each musically correct, so ruled GRAMMAR GAPS
//     (not mis-encodings). The ratified §15-12 amendment (L5 spec) added exactly those
//     three root-motion classes to THIS grammar (see isAscendingFifth /
//     isDescendingSecond / isDiatonicDiminishedFifth below); the consumer's consistency
//     test then EMPTIED its known-gap list and tightened to the clean invariant (every
//     adjacent catalog pair licensed). No catalog edit was needed. Historical note
//     retained.

#include <vector>

#include "composing/analysis/types/analysistypes.h"   // ChordQuality

namespace mu::composing::analysis {

// ── The unit the licensed-progression test reasons over ("two functions", §5.0) ─
//
// A committed chord read in the prevailing key. The licensing test needs only the
// root and quality; the degree-in-key (the full RN function) is derived separately
// by the base-RN module (functionromannumeral) and is not required here.
struct ProgressionChord {
    int rootPc = -1;                              ///< committed root pitch class (0–11); -1 = none
    ChordQuality quality = ChordQuality::Unknown; ///< committed chord quality
};

// ── One slice of the ordered committed-chord stream over a region (§5.0) ───────
//
// "The progression" is the std::vector<ProgressionSlice> of a single region — the
// chord stream Layer 4 committed, read in order. A slice that Layer 4 abstained on
// (or an empty/sub-gate slice) carries committed == false; its chord fields are
// not read.
struct ProgressionSlice {
    ProgressionChord chord;       ///< the committed chord (valid only when committed == true)
    bool committed = false;       ///< a committed, non-abstained chord (L4 decision Commit/Inherit)
    double metricWeight = 1.0;    ///< slice metric weight (§3); higher == metrically stronger
    int startTick = 0;            ///< slice start tick (raw integer)
    int endTick = 0;              ///< slice end tick, exclusive
};

/// The ordered committed-chord stream over ONE region (§5.0 "the progression").
using Progression = std::vector<ProgressionSlice>;

// ── §5.0 root-motion sub-tests (the wSeq/wDim/resolutionEdge arithmetic, here as
//    licensing booleans rather than score terms) ─────────────────────────────────

/// Descending-fifth (dominant) motion: the target root sits a perfect fifth below
/// `fromRootPc` — i.e. (to - from) mod 12 == 5 (the wSeqBonus arithmetic). V→I.
bool isDescendingFifth(int fromRootPc, int toRootPc) noexcept;

/// Descending-third functional step: the target root sits a major or minor third
/// below `fromRootPc` — (to - from) mod 12 ∈ {8, 9}. e.g. I→vi, vi→IV.
bool isDescendingThird(int fromRootPc, int toRootPc) noexcept;

/// Ascending-second functional step: the target root sits a minor or major second
/// above `fromRootPc` — (to - from) mod 12 ∈ {1, 2}. e.g. IV→V, vii→I.
bool isAscendingSecond(int fromRootPc, int toRootPc) noexcept;

// ── §15-12 amendment (RATIFIED 2026-07-03): the three theory-licensed motions the
//    pre-amendment (bonus-derived) set omitted. Enumerated in L5 spec §5.0. ──────────

/// Ascending-fifth (tonic→dominant / plagal) motion: the target root sits a perfect
/// fifth ABOVE `fromRootPc` — (to - from) mod 12 == 7. I→V and IV→I. Unconditional on
/// quality. Has NO scoring-bonus analogue — a §15-12 theory completion.
bool isAscendingFifth(int fromRootPc, int toRootPc) noexcept;

/// Descending-second (Phrygian/Andalusian) step: the target root sits a major or minor
/// second BELOW `fromRootPc` — (to - from) mod 12 ∈ {10, 11}. i→♭VII, ♭VII→♭VI, ♭VI→V.
/// Unconditional on quality. A §15-12 theory completion.
bool isDescendingSecond(int fromRootPc, int toRootPc) noexcept;

/// The diatonic diminished-fifth link (IV→viiᵒ of the full circle of fifths): the root
/// falls a DIMINISHED fifth — (to - from) mod 12 == 6 — AND the arriving chord is a
/// DIMINISHED triad. The quality condition operationalises §15-12's "diatonic"
/// qualifier: a bare delta-6 license would admit generic tritone root motion, which the
/// grammar has never licensed and the amendment does not intend. A §15-12 completion.
bool isDiatonicDiminishedFifth(const ProgressionChord& from, const ProgressionChord& to) noexcept;

/// The resolution of an applied or leading-tone chord to its tonicized target
/// (§5.0). Quality-aware (the one root-motion clause that needs the chord quality):
///   • applied dominant  (V/x, V7/x → x): `from` is Major-quality (a dominant
///     triad / dominant seventh) a perfect fifth above the target — the wSeqBonus
///     descending-fifth arithmetic;
///   • secondary leading-tone (viio/x → x): `from` is Diminished a semitone below
///     a major/minor target — the wDimBonus / resolutionEdgeBonus dim arithmetic;
///   • half-diminished pre-dominant resolving up a perfect fourth to a major
///     target — the resolutionEdgeBonus half-dim arithmetic.
/// NOTE — the resolutionEdgeBonus augmented→major/minor SAME-ROOT edge (delta 0)
/// is DELIBERATELY EXCLUDED: §5.0 frames licensing as root MOTION (delta 0 is no
/// motion) and an augmented triad is not an applied/leading-tone chord. Flagged to
/// Cowork (report §6).
bool isAppliedResolution(const ProgressionChord& from, const ProgressionChord& to) noexcept;

/// §5.0 "a licensed (real) progression": the root motion between two functions is
/// one of the enumerable standard functional successions — descending-fifth,
/// descending-third or ascending-second functional step, ascending fifth (I→V, IV→I),
/// descending second (the Phrygian/Andalusian step), the diatonic diminished fifth
/// (IV→viiᵒ), or an applied/leading-tone resolution to its target. A stated, closed
/// test (no preference). The last three are the §15-12 amendment (RATIFIED 2026-07-03).
///
/// The CADENTIAL-MOTION clause of §5.0 is added when the cadence detector lands
/// (Step 2); its core motion (V→I, descending fifth) is already licensed here. The
/// applied/leading-tone clause is, by music theory, subsumed by the descending-
/// fifth and ascending-second motions; it is enumerated explicitly to mirror §5.0
/// and because the resolver (Step 3) consumes isAppliedResolution() as a standalone
/// quality-aware predicate.
bool isLicensedProgression(const ProgressionChord& from, const ProgressionChord& to) noexcept;

// ── §5.0 stream queries over a region ─────────────────────────────────────────

/// Is slice `sliceIndex` metrically strong? Parameter-free realization of §5.0
/// "metrically-strong slice": a LOCAL MAXIMUM of the metric-weight profile —
/// metricWeight ≥ both immediate onset-neighbours within the region (an
/// out-of-region neighbour counts as −∞, so the region's endpoints can qualify).
/// This mirrors the structural-peak convention phraseboundaryview §4.4 uses, and
/// introduces no tuned threshold. Returns false on an out-of-range index.
///
/// Known edge behaviour of the parameter-free rule (documented, refine at engage
/// if the cadence/resolver need a beat-grid-aware test — flagged to Cowork): the ≥
/// comparison treats a plateau of equal-weight slices as all strong, and a region's
/// FINAL slice counts as strong whenever it is ≥ its one in-region neighbour (the
/// −∞ right edge). Both are rare in real metric grids and harmless while dormant.
bool isMetricallyStrong(const Progression& region, int sliceIndex) noexcept;

/// §5.0 "prevailing harmony of a slice": the index of the committed chord of the
/// nearest metrically-strong slice AT OR BEFORE `sliceIndex`, within the region —
/// the harmony a passing/neighbour figure is heard against. Returns the slice's own
/// index when it is itself a committed, metrically-strong slice; -1 when no such
/// slice exists at or before it.
int prevailingHarmonyIndex(const Progression& region, int sliceIndex) noexcept;

/// §5.0 "the established next function": the index of the next committed (non-
/// abstained) slice AFTER `sliceIndex`, within the region. Returns -1 when no
/// committed slice follows. (Where the next chord is itself open, §5.0 falls back
/// to the next CADENCE-ANCHORED function; that fallback is a Step-2 addition once
/// the cadence detector exists.)
int establishedNextFunctionIndex(const Progression& region, int sliceIndex) noexcept;

} // namespace mu::composing::analysis
