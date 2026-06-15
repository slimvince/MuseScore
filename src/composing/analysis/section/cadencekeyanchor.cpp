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

#include "composing/analysis/section/cadencekeyanchor.h"

#include <algorithm>
#include <map>
#include <utility>

namespace mu::composing::analysis {

namespace {

/// Reduce x to the [0, 12) pitch-class residue.
inline int pcMod12(int x) noexcept
{
    return ((x % 12) + 12) % 12;
}

/// True if pitch class `pc` (0–11) is set in the 12-bit mask.
inline bool pcInMask(uint16_t mask, int pc) noexcept
{
    return (mask >> pcMod12(pc)) & 1u;
}

/// 12-bit mask of the diatonic pitch classes of a key SIGNATURE (Ionian).
/// Signature `fifths` selects the seven consecutive circle-of-fifths positions
/// [fifths-1, fifths+5]; position i has pitch class (7·i) mod 12.  For fifths=0
/// this is {0,2,4,5,7,9,11} (C-major / A-minor natural collection).
/// Key-agnostic: depends ONLY on the notated signature, never a resolved mode.
inline uint16_t diatonicMaskFromFifths(int fifths) noexcept
{
    uint16_t m = 0;
    for (int i = fifths - 1; i <= fifths + 5; ++i) {
        m |= static_cast<uint16_t>(1u << pcMod12(7 * i));
    }
    return m;
}

} // namespace

std::vector<AuthenticCadence>
detectAuthenticCadences(const std::vector<CadenceRegionInput>& regions,
                        int keySignatureFifths)
{
    const uint16_t diatonicMask = diatonicMaskFromFifths(keySignatureFifths);
    std::vector<AuthenticCadence> cadences;
    if (regions.size() < 2) {
        return cadences;
    }

    for (size_t i = 0; i + 1 < regions.size(); ++i) {
        const CadenceRegionInput& a = regions[i];      // candidate dominant
        const CadenceRegionInput& b = regions[i + 1];  // candidate tonic

        // Both members must carry a confident root.
        if (a.rootPc < 0 || b.rootPc < 0) {
            continue;
        }

        // The dominant must be major quality (carries a major third = leading
        // tone).  A dominant seventh is Major quality + a MinorSeventh
        // extension, so this admits V and V7 while excluding minor v.
        if (a.quality != ChordQuality::Major) {
            continue;
        }

        // The tonic must be a stable triad — major or minor.  Diminished,
        // augmented, suspended, and power sonorities are not cadential
        // resolution targets.
        if (b.quality != ChordQuality::Major && b.quality != ChordQuality::Minor) {
            continue;
        }

        // Descending perfect fifth: root(b) ≡ (root(a) − 7) mod 12.
        if (pcMod12(a.rootPc - 7) != b.rootPc) {
            continue;
        }

        // The leading tone is the dominant's major third = (root(a) + 4) mod 12,
        // which is by construction one semitone below root(b).  Require it to be
        // physically present in the dominant's pitch content (not merely implied
        // by the Major quality label).
        const int leadingTone = pcMod12(a.rootPc + 4);
        if (!pcInMask(a.pitchClassMask, leadingTone)) {
            continue;
        }

        AuthenticCadence c;
        c.dominantTick = a.startTick;
        c.tonicTick = b.startTick;
        c.tonicPc = b.rootPc;
        c.minorMode = (b.quality == ChordQuality::Minor);
        // Stage 4c-iii salience markers (key-agnostic):
        //  • structural: the resolution region b ends a phrase (fermata/piece-end).
        //  • chromatic LT: the leading tone is outside the signature's diatonic
        //    collection — the raised-LT marker of a genuine minor V→i.
        c.endsPhrase = b.endsPhrase;
        c.chromaticLeadingTone = !((diatonicMask >> leadingTone) & 1u);
        cadences.push_back(c);
    }

    return cadences;
}

namespace {

// Stage 4c-iii salience weights (provisional [empirical — Stage-5 fits];
// NOT corpus-fit to the 326-chorale gate).  Rationale in the header:
//  • a STRUCTURAL (phrase-final) cadence defines the key — it must outweigh
//    several interior tonicizations (the diatonic V→III that swamped 4c-i);
//  • a CHROMATIC raised leading tone marks a genuine minor V→i, the discriminator
//    against a purely-diatonic relative-major tonicization;
//  • FINALITY is a mild recency tilt, not a dominant term.
// Structural is the PRIMARY lever (largest single bonus): a phrase-final cadence
// must outweigh interior tonicizations.  Chromatic (raised-LT) is the secondary
// discriminator, equal to base.  Finality is a mild recency tilt.  Swept on the
// mode-absent relative-pair floor (realized) vs the mode-present clean-stem
// contradiction; this point sits at the high-realized / low-contradiction knee
// (75.2% / 25.3%) and is robust across the neighborhood (not a sharp optimum).
constexpr double kWeightBase       = 1.0;   // every detected authentic cadence
constexpr double kWeightStructural = 2.0;   // resolution coincides with a phrase boundary
constexpr double kWeightChromatic  = 1.0;   // dominant carries a chromatic (raised) leading tone
constexpr double kWeightFinality   = 1.0;   // maximal recency bonus (scaled by position)

} // namespace

CadenceKeyAnchor
aggregateGlobalAnchor(const std::vector<AuthenticCadence>& cadences)
{
    CadenceKeyAnchor anchor;
    anchor.cadenceCount = static_cast<int>(cadences.size());
    if (cadences.empty()) {
        return anchor;
    }

    // Sort by tonicTick so the recency tilt and Picardy "final cadence" reading
    // are well defined (a piece resolves to its tonic last).
    std::vector<AuthenticCadence> sorted = cadences;
    std::sort(sorted.begin(), sorted.end(),
              [](const AuthenticCadence& x, const AuthenticCadence& y) {
                  return x.tonicTick < y.tonicTick;
              });
    const size_t n = sorted.size();

    // (tonicPc, minorMode) → accumulated salience weight.  std::map gives a
    // deterministic iteration order so ties resolve to the lowest (tonicPc, then
    // major < minor).  Also track per-tonic-pc weight by mode for the Picardy
    // correction.
    std::map<std::pair<int, bool>, double> votes;
    std::map<int, double> minorWeightByPc;   // tonicPc → total weight cast as minor
    double total = 0.0;
    for (size_t k = 0; k < n; ++k) {
        const AuthenticCadence& c = sorted[k];
        const double recency = (n > 1) ? static_cast<double>(k) / static_cast<double>(n - 1)
                                       : 1.0;
        double w = kWeightBase
                   + (c.endsPhrase ? kWeightStructural : 0.0)
                   + (c.chromaticLeadingTone ? kWeightChromatic : 0.0)
                   + kWeightFinality * recency;
        votes[{ c.tonicPc, c.minorMode }] += w;
        if (c.minorMode) {
            minorWeightByPc[c.tonicPc] += w;
        }
        total += w;
    }

    auto best = votes.begin();
    for (auto it = votes.begin(); it != votes.end(); ++it) {
        if (it->second > best->second) {
            best = it;
        }
    }

    int winnerPc = best->first.first;
    bool winnerMinor = best->first.second;

    // ── Picardy correction ────────────────────────────────────────────────────
    // A minor piece often ends on a MAJOR tonic triad (Picardy third).  If the
    // winning bucket is MAJOR but the SAME tonic pc also carries minor cadential
    // weight (the body cadenced to i), the major reading is a Picardy third — the
    // global mode is minor.  A genuinely major key has no i cadences to its tonic,
    // so this never flips a true major.
    if (!winnerMinor) {
        auto mw = minorWeightByPc.find(winnerPc);
        if (mw != minorWeightByPc.end() && mw->second > 0.0) {
            winnerMinor = true;
        }
    }

    // Confidence = the winning (tonic, resolved-mode) weight share of the total.
    double winnerWeight = 0.0;
    auto wv = votes.find({ winnerPc, winnerMinor });
    if (wv != votes.end()) {
        winnerWeight = wv->second;
    }
    if (winnerMinor) {
        // After a Picardy flip, fold the same-pc major weight into the winner so
        // confidence reflects the unified tonic.
        auto maj = votes.find({ winnerPc, false });
        if (maj != votes.end() && !best->first.second) {
            winnerWeight += maj->second;
        }
    }

    anchor.detected = true;
    anchor.tonicPc = winnerPc;
    anchor.minorMode = winnerMinor;
    anchor.confidence = (total > 0.0) ? (winnerWeight / total) : 0.0;
    return anchor;
}

} // namespace mu::composing::analysis
