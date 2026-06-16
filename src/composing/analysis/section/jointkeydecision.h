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

// ── composing/analysis/section/jointkeydecision ──────────────────────────────
//
// The SCOPED CONSTRAINED-JOINT *key* decision (J-key-i / J-key-ii;
// docs/scoped_joint_design.md §6 — the key-axis-first build).  A DIAGNOSTIC
// producer that decides, per analysis region, a key/mode by the constrained-joint
// procedure:
//
//   1. CANDIDATE hypotheses (J-key-i: the SIGNATURE HOME PAIR backbone) — the
//      notated-signature relative pair (major tonic + relative minor) is the HARD
//      home backbone, the ONLY non-modulation-span key states.  The lattice is then
//      the home pair ∪ committed modulation spans (the few keys the piece actually
//      visits — NOT all 24).  The committed cadence anchor (aggregateGlobalAnchor)
//      contributes as a SOFT emission bonus (reinforcing the home + breaking the
//      relative-pair mode tie), NOT as a standalone lattice state — its
//      V→IV/subdominant over-detection (J-key-i §10.5) would otherwise inject a
//      phantom subdominant key.
//   2. THE HARD HOME-PAIR PRUNE (J-key-i strong-signature-backbone).  The home pair
//      is hard-pruned from the notated signature: any region not covered by a
//      committed modulation span resolves to one of the two home states.  Its safety
//      ceiling — partial/Dorian signatures whose fifths ≠ the DCML key (~17 %/56
//      stems, bwv254/265) — is structurally excluded and is the documented, ratified
//      residual that MATCHES production (which is itself locked to the notated
//      signature), NOT recovered here (J-key-i §6a/§7).  The J-key-ii global-soften
//      (note-inferred candidates ∪ a 0.30 signature prior) that demoted this pin is
//      SUPERSEDED: it shrank the soft win and regressed Default/Baroque S2; the strong
//      backbone is what reproduces the ratified +3.80/+3.50/+12.24 pp profile.  The
//      candidate "pinned-chord ⊆ key" was measured unsafe → never used.
//   3. SOFT scores rank survivors — scale/collection prior, the cadence anchor
//      (SOFT), the local-modulation hypotheses (SOFT), bass-is-root (SOFT), the
//      declared-mode hint (1.0, SOFT), and the GLOBAL KEY-PATH transition cost (a
//      modulation penalty across regions, decoded by a Viterbi path over the
//      key-state lattice).  NONE of these is a veto — they only re-rank the
//      candidates (the −7-wall-in-reverse safety property; §3/§7).
//   4. SCOPED JOINT (config B) — on the COUPLED CORE only (regions where the chord
//      is structurally ambiguous AND the key is modulation-ambiguous — the measured
//      ~13.5%), the key emission is augmented by the best chord candidate's
//      key-fit, so chord and key are decided jointly.  Everywhere else the forward
//      soft-rank (Viterbi path) suffices (design §3.4, §5).
//
// ATTRIBUTION TOGGLE (design §3, mirrors 4b-i's dual-condition measurement): the
// producer emits BOTH a config-A (soft-only: steps 1-3, joint disabled) and a
// config-B (soft + scoped-joint: steps 1-4) decision per region, so the Python
// instrument can isolate the joint core's incremental value from the soft baseline.
//
// ⛔ NO-CIRCULARITY / NO-PRODUCTION-LEAK (design §10; J-key-i §2, §5).
//   • The decision reads ONLY key-agnostic + local-candidate evidence.  The
//     PRODUCTION resolved key (prodTonicPc/prodIsMajor) is carried through ONLY as
//     the dump's comparison reference — it is NEVER read by decideJointKey (the
//     resolver cannot measure itself).
//   • This module is invoked ONLY from a diagnostic/tools path
//     (tools/batch_analyze.cpp --dump-joint-key).  The production key resolver /
//     winner / rendered RNs never call it → production output is byte-identical.
//   Wiring the decision into production is J-key-iii, separately ratified.
//
// J-key-i/ii SCOPE: built and MEASURED only.  Weights are provisional
// [empirical — Stage-5 fits]; not corpus-fit to any gate.

#include <cstdint>
#include <vector>

#include "composing/analysis/section/localmodulationdetector.h" // CadenceRegionInput, LocalKeySpan, CadenceKeyAnchor
#include "composing/analysis/chord/chordanalyzer.h"             // ChordQuality

namespace mu::composing::analysis {

/// One chord candidate (winner or alternative) for the scoped-joint chord×key
/// coupling.  chordAlts[0] is the production chord winner; the rest are ranked
/// alternatives.  Only the root pitch class is used by the coupling (its
/// diatonic-ness under a key hypothesis); quality is carried for completeness.
struct JointKeyChordAlt {
    int rootPc = -1;
    ChordQuality quality = ChordQuality::Unknown;
};

/// One existing analyzeKeyMode local key candidate — used ONLY as a SOFT prior
/// hypothesis seed (design §3.1 "the existing local key candidates").
struct JointKeyLocalCandidate {
    int tonicPc = -1;
    bool isMajor = true;
    double confidence = 0.0;   ///< normalizedConfidence of the local candidate (0..1)
};

/// Per-region input to the scoped-joint key decision.  Carries the same
/// key-agnostic fields the committed cadence/modulation instruments consume, plus
/// the local key candidates (SOFT prior), the chord alternatives (scoped-joint
/// coupling), and the production key (ECHOED reference ONLY — never read by the
/// decision).
struct JointKeyRegionInput {
    // ── key-agnostic cadence-instrument fields (identical to CadenceRegionInput) ──
    int startTick = 0;
    int endTick = 0;
    int rootPc = -1;                                ///< -1 ⇒ gap / sparse region
    ChordQuality quality = ChordQuality::Unknown;
    uint16_t pitchClassMask = 0;
    bool endsPhrase = false;

    int bassPc = -1;                                ///< lowest sounding pc, or -1

    /// Existing analyzeKeyMode local candidates (SOFT prior; design §3.1).
    std::vector<JointKeyLocalCandidate> localCandidates;

    /// Chord winner + alternatives for the scoped-joint coupling (config B).
    std::vector<JointKeyChordAlt> chordAlts;

    /// PRODUCTION resolved key — the dump's comparison REFERENCE only.  NEVER read
    /// by decideJointKey (no-circularity: the resolver cannot measure itself).
    int prodTonicPc = -1;
    bool prodIsMajor = true;

    /// Declared-mode hint (the shipped 1.0 tiebreaker) — SOFT, home-pair only.
    bool declaredModeKnown = false;
    bool declaredModeMinor = false;
};

/// Provisional soft-scoring weights [empirical — Stage-5 fits].  NONE is a hard
/// veto — every term is an additive re-rank of the hard survivors (asserted by the
/// additive structure of decideJointKey; design §3/§4/§7).
struct JointKeyWeights {
    double scalePrior        = 1.0;   ///< per-region collection-fit fraction
    double localPrior        = 0.5;   ///< matches an analyzeKeyMode local candidate (× its confidence)
    double cadenceAnchor     = 0.8;   ///< SOFT: matches the key-agnostic global anchor
    double modulation        = 1.0;   ///< SOFT: matches a committed modulation span covering the region
    double bassIsRootTonic   = 0.15;  ///< SOFT: region bass pc == hypothesis tonic
    double declaredHint      = 1.0;   ///< SOFT: signature-pair mode matches the declared mode (shipped 1.0)
    double transitionPenalty = 1.2;   ///< global key-path: cost of switching key vs the previous region
    double couplingBonus     = 0.6;   ///< config B only: best chord candidate is diatonic to the key
};

/// One key/mode state in the producer's scoped lattice (the signature home pair ∪
/// committed modulation spans).  Echoed in the dump so the safety instrument can
/// test whether the DCML key is REPRESENTABLE — under the J-key-i strong backbone a
/// partial/Dorian signature's true key is hard-excluded (the documented ~17% ceiling).
struct JointKeyLatticeState {
    int  tonicPc = -1;
    bool isMajor = true;
};

/// One region's two-config key decision plus the structural flags the Python
/// instrument buckets on.
struct JointKeyDecision {
    int startTick = 0;
    int endTick = 0;

    int  softTonicPc  = -1;           ///< config A (soft-only) tonic pc
    bool softIsMajor  = true;         ///< config A mode
    int  jointTonicPc = -1;           ///< config B (soft + scoped-joint) tonic pc
    bool jointIsMajor = true;         ///< config B mode
    int  prodTonicPc  = -1;           ///< ECHOED production reference
    bool prodIsMajor  = true;

    bool keyHardPinned = false;       ///< home-key region (no committed modulation span covers it) —
                                      ///< under the J-key-i strong-signature backbone such a region IS
                                      ///< hard-pinned to one of the two signature home-pair states.
    bool chordPinned   = false;       ///< complete-clear-vertical-chord (residual-probe PINNED class)
    bool keyAmbiguous  = false;       ///< covered by / adjacent to a committed modulation span
    bool coupled       = false;       ///< chord-ambiguous AND key-ambiguous ⇒ scoped joint applies here
    bool jointChanged  = false;       ///< config B decision differs from config A

    bool anchorContributed     = false;  ///< the config-A winner drew a nonzero cadence-anchor bonus
    bool modulationContributed = false;  ///< the config-A winner drew a nonzero modulation bonus

    int homeMajorTonicPc = -1;        ///< notated-signature relative pair = the HARD home backbone
    int homeMinorTonicPc = -1;        ///< (J-key-i strong-signature-backbone)
};

/// The producer's output: the per-region two-config decisions plus the key-agnostic
/// anchor and a few span/scope tallies (for the dossier cross-checks).
struct JointKeyResult {
    std::vector<JointKeyDecision> decisions;
    CadenceKeyAnchor anchor;
    int modulationSpanCount = 0;
    int coupledCount = 0;
    int hardPinnedCount = 0;

    /// The full scoped key-state lattice (the signature home pair ∪ committed
    /// modulation spans) the Viterbi decoded over — piece-global.  Lets the safety
    /// instrument test DCML-key REPRESENTABILITY (the home-fifths exclusion rate).
    /// Index 0/1 are the signature home pair.
    std::vector<JointKeyLatticeState> latticeStates;
};

/// ── J-key-iii PRODUCTION WIRING FLAG ─────────────────────────────────────────
/// When ENABLED, region::analyzeRegions runs the joint re-key 2-pass (override the
/// per-region key with decideJointKey's SOFT decision + re-emit the chord under it),
/// and section::analyzeSection's island-stabilization (Layer B) becomes inert on the
/// joint keys (so the Viterbi key path is authoritative — dossier §5).  Default
/// DISABLED ⇒ production is byte-identical to the committed baseline.  Set ONCE before
/// analysis (per process: the corpus regen / snapshot harness sets it via a CLI flag);
/// read by analyzeRegions + analyzeSection.  This is the FIRST intentional production
/// behavior change on the key axis (J-key-iii) — HELD off until ratified.
void setJointKeyWiringEnabled(bool enabled);
bool jointKeyWiringEnabled();

/// Decide the scoped constrained-joint key per region (both configs).
///
/// @p keySignatureFifths is the NOTATED signature (-7..+7, Ionian convention).
/// J-key-ii: it is NO LONGER a hard pin — it seeds the signature relative pair as
/// soft candidates and feeds the soft signature prior.  It is the signature, never
/// a resolved key (key-agnostic).
JointKeyResult
decideJointKey(const std::vector<JointKeyRegionInput>& regions,
               int keySignatureFifths,
               const JointKeyWeights& weights = {});

} // namespace mu::composing::analysis
