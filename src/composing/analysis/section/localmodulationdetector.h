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

// ── composing/analysis/section/localmodulationdetector ───────────────────────
//
// A KEY-AGNOSTIC local-modulation detector (Stage 4d-i; docs/stage4d_local_
// modulation_design.md §2).  It commits a *local-key span* only when that local
// key is both ESTABLISHED (a sustained run of regions consistent with its
// diatonic collection) and CONFIRMED (a V→I authentic cadence to its tonic inside
// the span) — exactly the brief-vs-sustained signal that separates a real
// modulation from a passing tonicization.
//
// ⛔ NO-CIRCULARITY RULE (design §3 — the load-bearing soundness property).
// The detector derives the local-key hypothesis ONLY from key-agnostic signals:
//   • the committed cadence instrument (detectAuthenticCadences — key-agnostic by
//     construction: its input CadenceRegionInput carries only ticks, root pc,
//     quality, and a pitch-class mask, and it cannot read the resolved key), and
//   • raw region structure (root pitch class + sounding pitch content vs the
//     HYPOTHESIZED local key's diatonic collection).
// It MUST NOT read the resolved key, KeyModeAnalysisResult, or the current
// KeyArea (all downstream of the stay-home resolver → circular).  Its only inputs
// are the same CadenceRegionInput stream the cadence detector consumes plus the
// NOTATED signature fifths (used only to mark the cadence's chromatic leading
// tone — the signature, never a resolved key).  This is enforced structurally:
// the input type is physically incapable of carrying a key.
//
// 4d-i SCOPE: built and MEASURED only.  A read-only diagnostic in tools/
// batch_analyze (--dump-modulation) invokes it and emits the candidate spans; the
// production key resolver / KeyArea NEVER calls it, so production key/RN output is
// byte-identical.  Re-keying the production span (overriding the home-signature
// pull within a committed span) is 4d-ii, separately ratified and gated.

#include <cstdint>
#include <vector>

#include "composing/analysis/section/cadencekeyanchor.h"   // CadenceRegionInput, AuthenticCadence, CadenceKeyAnchor

namespace mu::composing::analysis {

/// One committed candidate local-key span (a contiguous run of regions the
/// detector reads as locally in (tonicPc, mode)).  Diagnostic-only at 4d-i.
struct LocalKeySpan {
    int startTick = 0;          ///< startTick of the first region in the span
    int endTick = 0;            ///< endTick of the last region in the span
    int tonicPc = -1;           ///< local tonic pitch class (0–11)
    bool minorMode = false;     ///< local mode (true = minor, false = major)

    /// Number of regions in the consistent run that established this local key
    /// (the establishment-test count; ≥ kEstablishmentMinChords by construction).
    int establishmentChords = 0;

    /// Number of authentic cadences to this local tonic resolving inside the span
    /// (≥ 1 by construction — every span has at least one confirming cadence).
    int confirmingCadenceCount = 0;

    /// tonicTick of the earliest confirming cadence (for diagnostics / spot-checks).
    int firstCadenceTonicTick = -1;

    /// True when this span's local key equals the piece's KEY-AGNOSTIC global
    /// cadence anchor (aggregateGlobalAnchor) — i.e. it is the HOME key, not a
    /// modulation.  A modulation candidate is a committed span with this FALSE.
    /// The anchor is itself cadence-derived (key-agnostic), so this tag introduces
    /// no resolved-key dependency.
    bool agreesWithAnchor = false;
};

/// The detector's output: the committed candidate spans plus the key-agnostic
/// global cadence anchor used as the home reference for the agreesWithAnchor tag.
struct ModulationDetectionResult {
    std::vector<LocalKeySpan> spans;   ///< committed candidate local-key spans (ascending startTick)
    CadenceKeyAnchor anchor;           ///< key-agnostic global (home) anchor
};

/// Detect candidate local-key spans from a key-agnostic region stream.
///
/// Mechanism (design §2):
///   1. CANDIDATES — every authentic cadence (detectAuthenticCadences) exposes a
///      candidate local key (its resolution tonic + mode).
///   2. ESTABLISHMENT — grow the maximal contiguous run of regions consistent
///      with that local key's diatonic collection (root is a diatonic degree AND
///      the sounding pitch content lies within the collection up to a small
///      chromatic tolerance) around the cadence's resolution region.  The run
///      must span ≥ kEstablishmentMinChords regions.
///   3. CONFIRMATION — the cadence itself (a V→I of the local tonic inside the
///      run) is the confirmation.
///   4. COMMIT — when establishment AND confirmation hold, commit the span.
///      Overlapping same-key spans merge; overlapping different-key spans resolve
///      to the one with the longer establishment (conservative — prefer missing a
///      borderline modulation over inventing one).
///
/// @p keySignatureFifths is the NOTATED signature (-7..+7), passed through to the
/// cadence detector for its chromatic-leading-tone marker ONLY; it is the
/// signature, never a resolved key (key-agnostic).  Defaults to 0.
ModulationDetectionResult
detectLocalModulations(const std::vector<CadenceRegionInput>& regions,
                       int keySignatureFifths = 0);

} // namespace mu::composing::analysis
