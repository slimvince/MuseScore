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

// ── composing/analysis/function/functionrelationallabel ──────────────────────
//
// Architectural Layer 5 (FUNCTION) — THE RELATIONAL LABELS (§5.6) + THE UNIFIED
// TONICIZATION EMITTER (§3). Spec: cowork_layer5_function_design.md (SIGNED) §5.6
// + the §5.0 shared defs. Build plan: cowork_phase5c_l5_build_plan.md Step 5.
//
// THE FOUR RELATIONAL LABELS, in the FIXED PRECEDENCE (§5.6), first match wins:
//   AUGMENTED SIXTH  →  NEAPOLITAN  →  APPLIED / SECONDARY  →  MODAL MIXTURE
// The augmented sixth and the Neapolitan are the most specific (a named chromatic-
// predominant shape); the applied label fires next (a chord manufacturing dominant
// function toward a non-tonic degree); MODAL MIXTURE is the RESIDUAL — a quality-
// altering borrowed degree that matched NONE of the earlier labels (so it is decided
// by non-match, not by a positive "is borrowed" test). An altered chord matching
// several triggers takes the FIRST in the precedence.
//
// REUSE, NOT A SECOND FORMATTER (build §1 / §2). The RN STRING is produced by the ONE
// existing emitter, ChordSymbolFormatter::formatRomanNumeral(), which already emits
// the augmented-sixth labels (It+6 / Fr+6 / Ger+6), the chromatic numerals (bII6, bVI,
// iv, …), the figured-bass inversion, and the inline applied/secondary label. This
// module adds NO second RN formatter: it CLASSIFIES the relational role in precedence
// and delegates the string to that emitter. The applied/secondary case reuses the
// dormant tonicizationlabeler (with its chromatic-leading-tone false-positive guard).
//
// SPELLING IS READ ONLY WHERE THE DISTINCTION IS A SPELLING DISTINCTION (§5.6 / §8).
// The ONE place this layer reads notated spelling is the GERMAN SIXTH vs the DOMINANT
// SEVENTH — pitch-class-identical, separable only by the notated spelling and the
// resolution it implies. It is read through the shared interpreter
// engravingbridge::lineOfFifths(): the +10-semitone tone above a ♭6̂ root spelled as an
// AUGMENTED SIXTH (line-of-fifths distance +10 from the root) is an aug6 chord (which
// expands outward to the dominant); spelled as a MINOR SEVENTH (−2) it is a dominant
// seventh (which resolves down) — so the spelling IS "which resolution it implies".
// No second spelling interpreter is introduced; where the spelling is absent the aug6
// label is held uncertain (§11) and the chord falls through to its applied/base reading.
//
// THE UNIFIED TONICIZATION EMITTER (§3, dormant). emitAppliedLabel() is the ONE owned
// applied/tonicization emitter, subsuming the two paths that label tonicization today
// — the dormant tonicizationlabeler (the chromatic-LT guard kept) and the inline
// formatRomanNumeral applied path. It is DORMANT: production stays on the existing two
// paths; the RETIREMENT of those paths and the production switch are the joint engage
// (Phase 5d), so this step is byte-identical by construction (§6). The unification keeps
// the guarded labeler for the raised-secondary-leading-tone applied chords AND broadens
// the trigger to the ♭7̂-CHROMATIC applied dominant the labeler dropped — V7/IV, whose
// chromaticism is the ♭7̂ (IV's leading tone is the diatonic third degree), emitted via
// the production formatRomanNumeral inline path (Cowork ruling, §5.6 corrected 2026-06-26:
// V7/IV IS a genuine applied dominant and production correctly emits it). The false-
// positive guard for a genuinely diatonic chord (no chromaticism at all — e.g. the
// natural-minor VII7→III) is kept: the ♭7̂ broadening fires only on a chromatic seventh.
//
// NO CONSTANTS (build §4): the relational labels are deterministic structural triggers
// — degree relations + a spelling sign — with no weight, threshold, or margin to tune.
//
// PRODUCER-AGNOSTIC: the classifier reads only the small input below (a committed
// ChordIdentity + the prevailing key + the next committed root + the chord's notated
// spellings). At engage each field maps from the L4 decoder's committed chord
// (chord/chordslicedecoder.h SliceChord.chosen) + the L3 region key + the L1 note tpcs;
// injected by hand in the tests.
//
// DORMANT (build §6): NO production consumer — nothing in src/ calls it; exercised only
// by its unit tests. Byte-identical on production by construction; load-bearing when the
// function layer engages (Phase 5d).

#include <cstdint>
#include <string>
#include <vector>

#include "composing/analysis/chord/chordanalyzer.h"   // ChordIdentity, ChordAnalysisResult, ChordSymbolFormatter, Extension, KeySigMode

namespace mu::composing::analysis {

// ── The four relational roles (§5.6), in precedence order ─────────────────────
enum class RelationalRole {
    None,              ///< no relational label — a plain diatonic chord (label = the base numeral)
    AugmentedSixth,    ///< It+6 / Fr+6 / Ger+6 — the Ger6↔V7 call read from notated spelling
    Neapolitan,        ///< bII6 — a major triad on the lowered second degree
    AppliedSecondary,  ///< V/x, V7/x, viio/x, viio7/x, viiø7/x — applied chord of a non-tonic degree
    ModalMixture       ///< a borrowed quality-altering degree (the RESIDUAL): bVI, iv-in-major, …
};

// ── Input: one committed chord read in its prevailing key (§5.1 / §5.6) ───────
//
// The key fields map directly from the Layer-3 region key (keyModeResult): keyFifths =
// keySignatureFifths, keyMode = mode, keyTonicPc = tonicPc.
struct RelationalLabelInput {
    /// The committed chord identity (root/bass pc + tpc, quality, extension bitmask,
    /// naturalFifthPresent) — Layer-4's decided sonority.
    ChordIdentity identity;

    int keyFifths = 0;                       ///< prevailing key signature fifths (-7..+7, Ionian convention)
    KeySigMode keyMode = KeySigMode::Ionian; ///< prevailing mode
    int keyTonicPc = 0;                      ///< prevailing tonic pitch class (0=C)

    /// Root pitch class of the NEXT committed chord (the applied resolution target),
    /// or -1 when there is no successor. The applied/secondary test needs the target
    /// to name the tonicized degree; without it the applied label cannot fire (matching
    /// the inline formatRomanNumeral path, which also requires a next root).
    int nextRootPc = -1;

    /// The chord's NOTATED SPELLINGS (one tpc per sounding note), read through the
    /// shared engravingbridge::lineOfFifths() interpreter for the ONE spelling
    /// distinction the layer makes — the German sixth vs the dominant seventh (§5.6).
    /// Empty ⇒ spelling unavailable ⇒ the aug6 label is held uncertain (§11).
    std::vector<int> noteTpcs;

    /// 12-bit mask of pitch classes sounding in the chord (the applied path's
    /// leading-tone-present check, reused from the tonicizationlabeler guard).
    uint16_t pitchClassMask = 0;
};

// ── Output: the relational label for one chord (additive over the base RN, §7) ─
struct RelationalLabel {
    RelationalRole role = RelationalRole::None;
    std::string label;               ///< the emitted RN string (from formatRomanNumeral / emitAppliedLabel)

    int targetDegree = -1;           ///< applied: 0..6 tonicized degree in the LOCAL key; else -1
    int targetPc = -1;               ///< applied: pitch class of the tonicized degree; else -1

    bool spellingConsulted = false;  ///< the aug6 path read the notated spelling (transparency)
    bool spelledAsAugSixth = false;  ///< the +10 tone is spelled as an augmented sixth (vs a minor seventh)
};

// ── The §5.6 precedence classifier ────────────────────────────────────────────

/// Classify one committed chord's relational label in the fixed §5.6 precedence
/// (augmented sixth → Neapolitan → applied/secondary → modal mixture, first match
/// wins; modal mixture is the residual). Reuses formatRomanNumeral for the RN string
/// and reads spellingview only for the Ger6↔V7 distinction. When no relational role
/// fires, returns role == None with `label` set to the chord's plain base numeral.
RelationalLabel classifyRelationalLabel(const RelationalLabelInput& in);

// ── The unified applied/tonicization emitter (§3) — ONE owned emitter ─────────

/// Produce the applied/tonicization label (V/x, V7/x, viio/x, viio7/x, viiø7/x) for one
/// chord resolving to in.nextRootPc, keeping the dormant tonicizationlabeler's chromatic-
/// leading-tone false-positive guard. The single OWNED emitter that subsumes the two
/// tonicization paths today (the dormant labeler + the inline formatRomanNumeral applied
/// path). DORMANT — production keeps using the existing paths until Phase 5d. Returns
/// role == None (empty label) when the chord is not an applied chord of a non-tonic degree.
RelationalLabel emitAppliedLabel(const RelationalLabelInput& in);

} // namespace mu::composing::analysis
