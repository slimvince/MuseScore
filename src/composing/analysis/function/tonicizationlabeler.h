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

// ── composing/analysis/function/tonicizationlabeler ──────────────────────────
//
// The functional layer's NARROW first slice (Stage 6-tonic-i;
// docs/stage6_functional_layer_design.md §3): a sequence-labeling pass that
// recognizes a chord functioning as a SECONDARY DOMINANT / APPLIED LEADING-TONE
// of a non-tonic diatonic degree and emits the `<numeral>/<degree>` tonicization
// label (e.g. a D-major chord in C major resolving to G is `V/V`, not a bare
// `II`).
//
// It is a NEW, higher labeling pass over the already-decoded chord+key path —
// distinct from harmonicfunctionlayer (the chord-COMPETITION layer: rcb/wSeq/
// wDim). Per the layer-by-layer audit method it ASSUMES its inputs correct:
//   • per-region chord root pc + quality (Stage 3 decoded output);
//   • the prevailing RESOLVED key/mode per region (Stage 4).
// Stage 6 legitimately consumes the resolved key (this is NOT circular, unlike
// the cadence detector which had to stay key-agnostic): with a known key, an
// applied chord is identified relative to that key.
//
// 6-tonic-i SCOPE: this pass is built and MEASURED only. It PRODUCES a per-region
// label; it does NOT mutate chord root/quality/key and is NOT emitted into the
// production Roman-numeral output (a read-only diagnostic in tools/batch_analyze
// invokes it). Wiring the label into the emitted RN is 6-tonic-ii, separately
// ratified, gated on this measurement (false-label rate + S1 recall).
//
// FALSE-POSITIVE GUARDS (the analogue of the cadence detector's resolution/
// chromatic discriminators — see §3 of the design): the candidate fires only
// when BOTH (a) the next region resolves TO the tonicized degree d, AND (b) the
// raised leading tone of d is CHROMATIC relative to the prevailing key signature
// (an accidental outside the diatonic collection). The chromatic guard is what
// distinguishes a genuine applied chord from ordinary diatonic motion (e.g. a
// diatonic VII->III in a minor key has NO chromatic alteration and is NOT a
// tonicization — DCML agrees).

#include <cstdint>
#include <string>
#include <vector>

#include "composing/analysis/chord/chordanalyzer.h"   // ChordQuality

namespace mu::composing::analysis {

/// Per-region input for tonicization labeling.
///
/// Carries the chord's pitch-content identity (root pc + quality + whether a
/// seventh is present) and the PREVAILING RESOLVED KEY (tonic pc, mode, notated
/// signature fifths). Unlike CadenceRegionInput (key-agnostic by construction),
/// this slice legitimately consumes the resolved key — Stage 6 runs AFTER key
/// resolution.
struct TonicizationRegionInput {
    int startTick = 0;
    int endTick = 0;

    /// Root pitch class (0–11), or -1 when the region produced no confident
    /// chord (a gap / sparse region — never a tonicization member).
    int rootPc = -1;

    /// Chord quality of the region's winning identity.
    ChordQuality quality = ChordQuality::Unknown;

    /// Seventh presence — distinguishes `V` from `V7` (minor seventh above a
    /// major triad) and `viio` from `viio7` (diminished/minor seventh above a
    /// diminished triad).
    bool hasMinorSeventh = false;
    bool hasDiminishedSeventh = false;

    /// 12-bit mask of pitch classes sounding anywhere in the region (bit p set ⇒
    /// pitch class p present). Used to confirm the dominant's leading tone is
    /// physically present, not merely implied by the Major quality label.
    uint16_t pitchClassMask = 0;

    /// The PREVAILING resolved key for this region (Stage 4 output):
    ///   • keyTonicPc — pitch class of the key's tonic (0=C);
    ///   • keyIsMajor — the mode has a major third;
    ///   • keySignatureFifths — the notated signature (-7..+7, Ionian convention),
    ///     used to build the diatonic collection for the chromatic-vs-key test
    ///     AND to name diatonic degrees. For a correctly-resolved key this is the
    ///     score's signature; for Aeolian it is the relative-major fifths, whose
    ///     Ionian collection IS the natural-minor collection.
    int keyTonicPc = 0;
    bool keyIsMajor = true;
    int keySignatureFifths = 0;
};

/// What kind of applied chord a region was recognized as.
enum class AppliedKind {
    None,
    AppliedDominant,      ///< V/d, V7/d — a (dom7 or major-triad) dominant of d
    AppliedLeadingTone,   ///< viio/d, viio7/d, viiø7/d — a leading-tone chord of d
};

/// The tonicization label produced for one region (the region indexed as the
/// candidate APPLIED chord `a`; the resolution target `b` is the next region).
struct TonicizationLabel {
    bool isApplied = false;            ///< true ⇒ this region is an applied chord of a degree d
    AppliedKind kind = AppliedKind::None;

    int targetPc = -1;        ///< pitch class of the tonicized degree d (== next region root)
    int targetDegree = -1;    ///< 1..6 scale degree of d in the prevailing key (0=tonic excluded)
    bool targetIsMajor = false; ///< the degree triad has a major third ⇒ uppercase degree token
    bool hasSeventh = false;  ///< the applied chord carries a seventh (V7 / viio7)

    int leadingTonePc = -1;   ///< raised leading tone of d ((d+11) mod 12), the chromatic marker

    /// The emitted `<numeral>/<degree>` label, e.g. "V/V", "V7/ii", "viio/V",
    /// "viiø7/vi". Empty when isApplied is false. The form MATCHES the existing
    /// ChordSymbolFormatter::formatRomanNumeral() secondary output (and hence
    /// what tools/compare_rn already credits) — it is not a re-invented vocabulary.
    std::string label;
};

/// Label every region in an ordered region stream with its tonicization (applied
/// chord) reading, or `none`.
///
/// For each consecutive pair (a = regions[i], b = regions[i+1]) in the prevailing
/// key K of region a, region a is labeled an applied chord of diatonic degree d
/// (d ≠ tonic) when:
///   • d = root(b) is a DIATONIC scale degree of K (so it can be named as a
///     Roman numeral) other than the tonic;
///   • the raised leading tone of d, lt = (pc(d) + 11) mod 12, is CHROMATIC
///     relative to K's signature collection (the false-positive guard);
///   • AND one of:
///       – APPLIED DOMINANT: a is Major quality, root(a) ≡ (pc(d) + 7) mod 12,
///         and lt (= a's major third) is present in a's pitch mask;
///       – APPLIED LEADING-TONE: a is Diminished/HalfDiminished, root(a) ≡ lt.
/// The resolution-to-d requirement (root(b) == pc(d)) is implicit: d IS root(b).
///
/// Returns a vector parallel to `regions` (label[i] describes regions[i]); a
/// region that is not an applied chord, or the final region (no successor), gets
/// an empty (isApplied=false) label.
std::vector<TonicizationLabel>
labelTonicizations(const std::vector<TonicizationRegionInput>& regions);

} // namespace mu::composing::analysis
