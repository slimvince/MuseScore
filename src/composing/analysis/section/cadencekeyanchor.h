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

// ── composing/analysis/section/cadencekeyanchor ──────────────────────────────
//
// A KEY-AGNOSTIC authentic-cadence detector that derives a global tonic+mode
// anchor purely from chord-identity (root pitch class + quality) and per-region
// sounding pitch content.  It is the Stage-4c-i build (docs/stage4c_cadence_key_
// design.md §2): a note-derived replacement for the lost declared-mode global
// anchor, intended to break the relative-major/minor key tie at section/piece
// scope WITHOUT re-entering the §4 window-local coupling.
//
// It deliberately does NOT consume `ChordFunction::degree` or any resolved
// `KeyModeAnalysisResult`.  The existing detectCadences() (sectionanalyzer.cpp)
// is unusable for key inference because it decides PAC/PC/DC/HC from
// `chordResult.function.degree`, which is computed FROM the already-resolved key
// (circular), and is gated on assertive key confidence (silent exactly on the
// floor near-ties).  This detector closes that circularity STRUCTURALLY: its
// input type carries only root pc, quality, and a pitch-class mask — it is
// physically incapable of reading the key.  (cc_cadence_key_investigation_
// dossier.md §1.)
//
// 4c-i SCOPE: this header is built and MEASURED only (a read-only diagnostic in
// tools/batch_analyze invokes it; the production key resolver/winner never
// calls it).  Wiring the anchor into key scoring is 4c-ii, separately ratified.

#include <cstdint>
#include <vector>

#include "composing/analysis/chord/chordanalyzer.h"   // ChordQuality

namespace mu::composing::analysis {

/// Key-agnostic per-region input for authentic-cadence detection.
///
/// Carries ONLY the chord's pitch-content identity (root pc + quality) and the
/// region's sounding pitch classes.  It intentionally omits keyModeResult and
/// function.degree so the detector cannot read the resolved key — the
/// circularity that makes detectCadences() unusable for key inference.
struct CadenceRegionInput {
    int startTick = 0;
    int endTick = 0;

    /// Root pitch class (0–11), or -1 when the region produced no confident
    /// chord (a gap / sparse region — never a cadence member).
    int rootPc = -1;

    /// Chord quality of the region's winning identity.
    ChordQuality quality = ChordQuality::Unknown;

    /// 12-bit mask of pitch classes sounding anywhere in the region
    /// (bit p set ⇒ pitch class p present).  Used to confirm the dominant's
    /// leading tone is physically present, not merely implied by quality.
    uint16_t pitchClassMask = 0;

    /// True when this region coincides with a PHRASE BOUNDARY: a fermata sounds
    /// within it, or it is the final region of the piece.  Read from the
    /// engraving Score in tools/batch_analyze (notation, NOT a resolved key —
    /// key-agnostic).  Stage 4c-iii: a cadence resolving INTO such a region is a
    /// STRUCTURAL cadence and is weighted far above an interior tonicization.
    bool endsPhrase = false;
};

/// One detected authentic cadence: a descending-perfect-fifth dominant→tonic
/// motion whose dominant carries the leading tone (its major third) in its
/// pitch content, resolving to a stable (major/minor) triad.
struct AuthenticCadence {
    int dominantTick = -1;   ///< startTick of the dominant region (a)
    int tonicTick = -1;      ///< startTick of the resolution region (b)
    int tonicPc = -1;        ///< root pc of b — the cadential tonic
    bool minorMode = false;  ///< b's quality: true = minor triad, false = major triad

    /// Stage 4c-iii salience markers (computed in detectAuthenticCadences):
    ///
    /// endsPhrase: the resolution region b coincides with a phrase boundary
    /// (a STRUCTURAL cadence — phrase-final/piece-final).  Interior tonicizations
    /// (the abundant diatonic V→III that swamped the 4c-i vote) carry this false.
    bool endsPhrase = false;
    /// chromaticLeadingTone: the dominant's leading tone ((root(a)+4) mod 12) is
    /// CHROMATIC relative to the key SIGNATURE — i.e. it requires an accidental
    /// outside the notated diatonic collection.  This is the key-agnostic marker
    /// of a genuine raised-leading-tone V→i (e.g. E→Am needs G♯ in a 0-sharp
    /// signature), distinguishing it from a purely-diatonic V→III tonicization
    /// (G→C uses the in-collection B).  Derived from signature fifths + pitch
    /// content ONLY — never the resolved key/mode.
    bool chromaticLeadingTone = false;
};

/// The aggregated global tonic anchor for a piece (or section span).
struct CadenceKeyAnchor {
    bool detected = false;   ///< false when no authentic cadence was found in the span
    int tonicPc = -1;        ///< winning cadential tonic pitch class (0–11)
    bool minorMode = false;  ///< winning mode (true = minor, false = major)
    double confidence = 0.0; ///< finality-weighted vote share of the winning (tonic, mode) ∈ [0,1]
    int cadenceCount = 0;    ///< number of authentic cadences detected in the span
};

/// Detect every authentic cadence in an ordered region stream (key-agnostic).
///
/// For each consecutive pair (a = regions[i], b = regions[i+1]):
///   • both must carry a confident root (rootPc ≥ 0);
///   • a must be major quality (so it carries a major third = a leading tone);
///   • b must be a stable triad (major or minor quality);
///   • root(b) ≡ (root(a) − 7) mod 12 — a is the descending-fifth dominant of b;
///   • the leading tone (root(a) + 4) mod 12 must be PRESENT in a's pitch mask.
/// Then b is a cadential tonic and b's quality gives the mode.
///
/// @p keySignatureFifths is the NOTATED key signature (-7..+7, Ionian/concert
/// convention) used ONLY to mark each cadence's chromaticLeadingTone (whether the
/// dominant's leading tone lies outside the signature's diatonic collection).  It
/// is the signature, NOT a resolved key — passing it keeps the detector
/// key-agnostic (Stage 4c-iii raised-LT salience).  Defaults to 0 (the 0-sharp
/// collection) for callers that supply no signature.
std::vector<AuthenticCadence>
detectAuthenticCadences(const std::vector<CadenceRegionInput>& regions,
                        int keySignatureFifths = 0);

/// Aggregate detected cadences into a single global (tonicPc, mode, confidence)
/// anchor by a SALIENCE-WEIGHTED vote (Stage 4c-iii — replaces the 4c-i naive
/// finality count that reproduced the relative-major error).  Each cadence k
/// (0-based, ascending tonicTick) contributes
///
///     w = wBase
///       + (endsPhrase            ? wStructural : 0)   // phrase-final cadence
///       + (chromaticLeadingTone  ? wChromatic  : 0)   // raised-LT V→i marker
///       + wFinality * k/(n-1)                          // mild recency tilt
///
/// to its (tonicPc, mode) bucket.  The structural and chromatic terms let the
/// rare genuine V→i outweigh the abundant interior diatonic V→III tonicizations
/// that swamped the count vote.  The winner is the heaviest bucket; confidence is
/// its weight share.  A PICARDY correction then runs: a winning MAJOR bucket whose
/// tonic pc also carries MINOR-mode cadential weight is re-read as minor (a minor
/// piece ending on a major tonic triad must not flip the global mode).
/// Weights are provisional [empirical — Stage-5 fits]; not corpus-fit to the gate.
CadenceKeyAnchor
aggregateGlobalAnchor(const std::vector<AuthenticCadence>& cadences);

} // namespace mu::composing::analysis
