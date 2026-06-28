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

// ── composing/analysis/function/functionromannumeral ─────────────────────────
//
// Architectural Layer 5 (FUNCTION) — the BASE ROMAN-NUMERAL derivation.
// Spec: cowork_layer5_function_design.md (SIGNED) §5.1. Build plan:
// cowork_phase5c_l5_build_plan.md Step 1.
//
// §5.1: "For each analysis unit with a committed root, quality, inversion, and a
// prevailing key: the degree is the root's position relative to the tonic … the
// quality and inversion come from the chord. This step is a deterministic reading;
// it introduces no judgment beyond the key and chord it is given."
//
// A FAITHFUL WRAP, NOT A RE-IMPLEMENTATION (build §1 / §3). It reuses the ONE
// existing emitter:
//   • diatonicDegreeForRootPc()  (region/sparsechordrefinement.h) — the scale
//     degree of the committed root in the prevailing key;
//   • ChordSymbolFormatter::formatRomanNumeral()  (chord/chordanalyzer.h) — the
//     full numeral at DCML completeness: degree case-marking, chromatic alteration
//     (bII, #iv, bVII…), the precise quality incl. seventh type, the figured-bass
//     inversion (6, 64; 7, 65, 43, 42), the augmented-sixth nationality (It/Fr/Ger),
//     and the inline applied/secondary label (V7/x, viio/x) when nextRootPc is set.
// There is exactly one formatter; this module adds no second one (the §5.6
// precedence / Neapolitan-as-bII6 / modal-mixture-as-residual refinements are
// Step 5 work BUILT ON TOP of this emission, not duplicates of it).
//
// DORMANT (build §6): no production consumer (nothing in src/ calls it) — exercised
// only by its unit tests, so byte-identical on production by construction.

#include <string>

#include "composing/analysis/chord/chordanalyzer.h"   // ChordIdentity, KeySigMode

namespace mu::composing::analysis {

// ── Input: a committed chord read in the prevailing key (§5.1) ────────────────
//
// The key fields map directly from the Layer-3 region key
// (region/harmonicrhythm.h HarmonicRegion::keyModeResult, a KeyModeAnalysisResult):
//   keyFifths  = keyModeResult.keySignatureFifths
//   keyMode    = keyModeResult.mode
//   keyTonicPc = keyModeResult.tonicPc
struct BaseRomanNumeralInput {
    /// The committed chord identity (root pc/tpc, bass pc/tpc, quality, extension
    /// bitmask, naturalFifthPresent) — Layer-4's decided sonority.
    ChordIdentity identity;

    int keyFifths = 0;                       ///< prevailing key signature fifths (-7..+7, Ionian convention)
    KeySigMode keyMode = KeySigMode::Ionian; ///< prevailing mode
    int keyTonicPc = 0;                      ///< prevailing tonic pitch class (0=C)

    /// Root pitch class of the next committed chord, or -1. When set, the wrapped
    /// formatter may emit the inline applied/secondary label (V7/x, viio/x). The
    /// FULL §5.6 relational-label treatment is Step 5; this carries the existing
    /// emitter's behaviour through faithfully.
    int nextRootPc = -1;
};

// ── Output: the base Roman numeral ────────────────────────────────────────────
struct BaseRomanNumeral {
    std::string label;        ///< the full numeral (formatRomanNumeral output); empty when undecidable
    int degree = -1;          ///< 0..6 diatonic degree of the root in the key; -1 when chromatic
    bool diatonicToKey = false;
};

/// Derive the base Roman numeral for one committed chord in its prevailing key, by
/// wrapping diatonicDegreeForRootPc() + ChordSymbolFormatter::formatRomanNumeral().
/// Deterministic; introduces no judgment beyond the key+chord it is given (§5.1).
BaseRomanNumeral deriveBaseRomanNumeral(const BaseRomanNumeralInput& in);

} // namespace mu::composing::analysis
