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

#include "composing/analysis/function/tonicizationlabeler.h"

#include <array>

namespace mu::composing::analysis {

// A NAMED detail namespace (not anonymous): the unity build concatenates this TU
// with cadencekeyanchor.cpp, which defines identically-named pc helpers in its own
// anonymous namespace — two anonymous namespaces in one unity TU are the SAME
// unnamed namespace and would collide. The named namespace keeps these distinct.
namespace tonicization_detail {

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
/// Identical to cadencekeyanchor's helper: signature `fifths` selects the seven
/// consecutive circle-of-fifths positions [fifths-1, fifths+5]; position i has
/// pitch class (7·i) mod 12. For fifths=0 this is {0,2,4,5,7,9,11} (C-major /
/// A-minor natural collection). Used both for the chromatic-vs-key test and to
/// enumerate the key's diatonic degrees.
inline uint16_t diatonicMaskFromFifths(int fifths) noexcept
{
    uint16_t m = 0;
    for (int i = fifths - 1; i <= fifths + 5; ++i) {
        m |= static_cast<uint16_t>(1u << pcMod12(7 * i));
    }
    return m;
}

/// Build the ordered diatonic scale of the prevailing key: the seven collection
/// members in ascending pitch order starting from the tonic. scale[0] == tonicPc.
/// For a major key this is the major scale; for a minor (Aeolian) key the
/// signature's collection rooted at the minor tonic IS the natural-minor scale.
/// Returns false if the collection does not contain exactly seven members
/// including the tonic (defensive — never expected for a real signature).
inline bool keyScale(int tonicPc, uint16_t collMask, std::array<int, 7>& out) noexcept
{
    if (!pcInMask(collMask, tonicPc)) {
        return false;
    }
    int idx = 0;
    for (int step = 0; step < 12 && idx < 7; ++step) {
        const int pc = pcMod12(tonicPc + step);
        if (pcInMask(collMask, pc)) {
            out[idx++] = pc;
        }
    }
    return idx == 7;
}

static constexpr const char* kUpper[7] = { "I", "II", "III", "IV", "V", "VI", "VII" };
static constexpr const char* kLower[7] = { "i", "ii", "iii", "iv", "v", "vi", "vii" };

} // namespace tonicization_detail

std::vector<TonicizationLabel>
labelTonicizations(const std::vector<TonicizationRegionInput>& regions)
{
    using namespace tonicization_detail;

    std::vector<TonicizationLabel> labels(regions.size());
    if (regions.size() < 2) {
        return labels;
    }

    for (size_t i = 0; i + 1 < regions.size(); ++i) {
        const TonicizationRegionInput& a = regions[i];      // candidate applied chord
        const TonicizationRegionInput& b = regions[i + 1];  // resolution target

        // Both members must carry a confident root.
        if (a.rootPc < 0 || b.rootPc < 0) {
            continue;
        }

        // The tonicized degree d is the resolution target's root.
        const int d = b.rootPc;

        // d must be a DIATONIC degree of the prevailing key (so it can be named
        // as a plain Roman numeral) and NOT the tonic (plain dominant→tonic is
        // not a tonicization). The collection is the signature's Ionian set —
        // for Aeolian this is the natural-minor collection rooted at the tonic.
        const uint16_t collMask = diatonicMaskFromFifths(a.keySignatureFifths);
        std::array<int, 7> scale{};
        if (!keyScale(a.keyTonicPc, collMask, scale)) {
            continue;
        }
        int degree = -1;
        for (int s = 0; s < 7; ++s) {
            if (scale[s] == d) {
                degree = s;
                break;
            }
        }
        if (degree <= 0) {
            // degree == 0 ⇒ tonic target (excluded); degree < 0 ⇒ d chromatic
            // (not a diatonic degree — a different functional class, out of slice).
            continue;
        }

        // FALSE-POSITIVE GUARD (chromatic raised leading tone): the leading tone
        // of d must be an ACCIDENTAL relative to the key signature. A diatonic
        // leading tone means ordinary diatonic motion, not a tonicization (e.g.
        // VII→III in a minor key — DCML agrees this is not applied).
        const int lt = pcMod12(d + 11);
        if (pcInMask(collMask, lt)) {
            continue;
        }

        AppliedKind kind = AppliedKind::None;
        bool hasSeventh = false;

        if (a.quality == ChordQuality::Major) {
            // APPLIED DOMINANT (V/d, V7/d): root a perfect fifth above d, with
            // the leading tone of d (= a's major third) physically present.
            if (a.rootPc == pcMod12(d + 7) && pcInMask(a.pitchClassMask, lt)) {
                kind = AppliedKind::AppliedDominant;
                hasSeventh = a.hasMinorSeventh;
            }
        } else if (a.quality == ChordQuality::Diminished
                   || a.quality == ChordQuality::HalfDiminished) {
            // APPLIED LEADING-TONE (viio/d, viio7/d, viiø7/d): root IS the
            // (chromatic) leading tone of d.
            if (a.rootPc == lt) {
                kind = AppliedKind::AppliedLeadingTone;
                hasSeventh = a.hasDiminishedSeventh || a.hasMinorSeventh;
            }
        }

        if (kind == AppliedKind::None) {
            continue;
        }

        // Degree token case: the diatonic triad on degree d has a major third ⇒
        // uppercase. third = the scale member two steps above d. Matches the
        // existing formatRomanNumeral() secondary casing (isDegreeMajorThird).
        const int thirdPc = scale[(degree + 2) % 7];
        const bool degMajorThird = (pcMod12(thirdPc - d) == 4);

        std::string label;
        if (kind == AppliedKind::AppliedDominant) {
            label = "V";
            if (hasSeventh) {
                label += "7";
            }
        } else {
            label = "vii";
            label += (a.quality == ChordQuality::HalfDiminished)
                     ? "\xc3\xb8"   // ø (half-diminished)
                     : "o";          // o (fully diminished)
            if (hasSeventh) {
                label += "7";
            }
        }
        label += "/";
        label += (degMajorThird ? kUpper[degree] : kLower[degree]);

        TonicizationLabel& tl = labels[i];
        tl.isApplied = true;
        tl.kind = kind;
        tl.targetPc = d;
        tl.targetDegree = degree;
        tl.targetIsMajor = degMajorThird;
        tl.hasSeventh = hasSeventh;
        tl.leadingTonePc = lt;
        tl.label = std::move(label);
    }

    return labels;
}

} // namespace mu::composing::analysis
