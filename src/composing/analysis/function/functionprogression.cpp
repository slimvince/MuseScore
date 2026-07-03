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
#include "functionprogression.h"

namespace mu::composing::analysis {

namespace {

/// Pitch-class interval from `fromPc` up to `toPc`, in [0, 11]. Returns -1 when
/// either root is absent (a defensive guard — a missing root licenses nothing).
int rootMotion(int fromPc, int toPc) noexcept
{
    if (fromPc < 0 || toPc < 0) {
        return -1;
    }
    return ((toPc - fromPc) % 12 + 12) % 12;
}

} // namespace

bool isDescendingFifth(int fromRootPc, int toRootPc) noexcept
{
    // (to - from) mod 12 == 5  ⇔  the target sits a perfect fifth below `from`.
    // Mirrors wSeqBonus (harmonicfunctionlayer.cpp): delta == 5.
    return rootMotion(fromRootPc, toRootPc) == 5;
}

bool isDescendingThird(int fromRootPc, int toRootPc) noexcept
{
    // Down a major third (-4 ≡ 8) or a minor third (-3 ≡ 9).
    const int delta = rootMotion(fromRootPc, toRootPc);
    return delta == 8 || delta == 9;
}

bool isAscendingSecond(int fromRootPc, int toRootPc) noexcept
{
    // Up a minor second (1) or a major second (2). The minor-second case also
    // covers the leading-tone-into-tonic step (mirrors wDimBonus delta == 1).
    const int delta = rootMotion(fromRootPc, toRootPc);
    return delta == 1 || delta == 2;
}

bool isAscendingFifth(int fromRootPc, int toRootPc) noexcept
{
    // (to - from) mod 12 == 7  ⇔  the target sits a perfect fifth above `from`.
    // §15-12 amendment (RATIFIED 2026-07-03): tonic→dominant (I→V) and plagal (IV→I)
    // motion. No scoring-bonus analogue — a theory completion the bonus-derived set
    // omitted; unconditional on quality.
    return rootMotion(fromRootPc, toRootPc) == 7;
}

bool isDescendingSecond(int fromRootPc, int toRootPc) noexcept
{
    // Down a major second (-2 ≡ 10) or a minor second (-1 ≡ 11): the Phrygian/
    // Andalusian step (i→♭VII, ♭VII→♭VI, ♭VI→V). §15-12 amendment (2026-07-03);
    // unconditional on quality.
    const int delta = rootMotion(fromRootPc, toRootPc);
    return delta == 10 || delta == 11;
}

bool isDiatonicDiminishedFifth(const ProgressionChord& from, const ProgressionChord& to) noexcept
{
    // The IV→viiᵒ link of the full circle of fifths: the root falls a diminished fifth
    // (delta 6, the tritone) AND the arriving chord is a diminished triad. §15-12
    // amendment (2026-07-03). The quality condition IS the amendment's "diatonic"
    // qualifier made operational — a bare delta-6 license would admit generic tritone
    // root motion, which the grammar has never licensed and the amendment does not want.
    return rootMotion(from.rootPc, to.rootPc) == 6
           && to.quality == ChordQuality::Diminished;
}

bool isAppliedResolution(const ProgressionChord& from, const ProgressionChord& to) noexcept
{
    const int delta = rootMotion(from.rootPc, to.rootPc);
    if (delta < 0) {
        return false;
    }

    // Applied dominant (V/x, V7/x → x): a Major-quality dominant a perfect fifth
    // above its target (the wSeqBonus descending-fifth arithmetic).
    if (from.quality == ChordQuality::Major && delta == 5) {
        return true;
    }

    // Secondary leading-tone (viio/x → x): a Diminished chord a semitone below a
    // major/minor target (the wDimBonus / resolutionEdgeBonus dim arithmetic).
    if (from.quality == ChordQuality::Diminished
        && (to.quality == ChordQuality::Major || to.quality == ChordQuality::Minor)
        && delta == 1) {
        return true;
    }

    // Half-diminished pre-dominant resolving up a perfect fourth to a major target
    // (the resolutionEdgeBonus half-dim arithmetic: candRootPc == prevRootPc + 5).
    if (from.quality == ChordQuality::HalfDiminished
        && to.quality == ChordQuality::Major
        && delta == 5) {
        return true;
    }

    // The augmented→major/minor SAME-ROOT resolution edge (delta 0) is excluded —
    // §5.0 licenses root MOTION, and same-root is no motion (see header / report §6).
    return false;
}

bool isLicensedProgression(const ProgressionChord& from, const ProgressionChord& to) noexcept
{
    if (from.rootPc < 0 || to.rootPc < 0) {
        return false;
    }
    // The §5.0 successions, OR'd: the pre-amendment three root-motion steps + the three
    // §15-12 amendment (2026-07-03) additions (ascending fifth, descending second,
    // diatonic diminished fifth) + the applied/leading-tone clause. That clause is (by
    // theory) subsumed by the descending-fifth + ascending-second motions; it is listed
    // explicitly to mirror §5.0's enumeration and expose the quality-aware sub-predicate
    // the resolver (Step 3) reuses.
    return isDescendingFifth(from.rootPc, to.rootPc)
           || isDescendingThird(from.rootPc, to.rootPc)
           || isAscendingSecond(from.rootPc, to.rootPc)
           || isAscendingFifth(from.rootPc, to.rootPc)
           || isDescendingSecond(from.rootPc, to.rootPc)
           || isDiatonicDiminishedFifth(from, to)
           || isAppliedResolution(from, to);
}

bool isMetricallyStrong(const Progression& region, int sliceIndex) noexcept
{
    const int n = static_cast<int>(region.size());
    if (sliceIndex < 0 || sliceIndex >= n) {
        return false;
    }
    const double w = region[static_cast<size_t>(sliceIndex)].metricWeight;
    // A local maximum of the metric-weight profile. An out-of-region neighbour
    // counts as −∞, so the first/last slice can qualify. Inclusive (≥) on both
    // sides so a plateau of equal strong beats all count as strong.
    const bool geLeft = (sliceIndex == 0)
                        || w >= region[static_cast<size_t>(sliceIndex - 1)].metricWeight;
    const bool geRight = (sliceIndex == n - 1)
                         || w >= region[static_cast<size_t>(sliceIndex + 1)].metricWeight;
    return geLeft && geRight;
}

int prevailingHarmonyIndex(const Progression& region, int sliceIndex) noexcept
{
    const int n = static_cast<int>(region.size());
    if (sliceIndex < 0 || sliceIndex >= n) {
        return -1;
    }
    for (int j = sliceIndex; j >= 0; --j) {
        if (region[static_cast<size_t>(j)].committed && isMetricallyStrong(region, j)) {
            return j;
        }
    }
    return -1;
}

int establishedNextFunctionIndex(const Progression& region, int sliceIndex) noexcept
{
    const int n = static_cast<int>(region.size());
    if (sliceIndex < 0) {
        return -1;
    }
    for (int j = sliceIndex + 1; j < n; ++j) {
        if (region[static_cast<size_t>(j)].committed) {
            return j;
        }
    }
    return -1;
}

} // namespace mu::composing::analysis
