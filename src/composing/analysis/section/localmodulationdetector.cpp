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

#include "composing/analysis/section/localmodulationdetector.h"

#include <algorithm>
#include <climits>

namespace mu::composing::analysis {

namespace {

// ── Provisional thresholds [empirical — Stage-5 fits] ────────────────────────
// NOT corpus-fit to any gate.  The 4d-i build MEASURES these and the user sets
// the bar (design §2, §5).
//
//  • kEstablishmentMinChords — the sustained-run length that promotes a cadence's
//    local tonic from a passing tonicization to an established local key.  The
//    scoping found 79–83% of DCML-confirmed local keys span ≥5 chords
//    (cc_modulation_keypath_scoping_dossier §3.2), so 5 is the established floor.
//  • kPitchTolerance — how many sounding pitch classes a region may carry OUTSIDE
//    the hypothesized local collection and still count as "consistent."  2 admits
//    an in-key secondary dominant (e.g. V/V's raised fourth) and the raised
//    leading tone without breaking the run, while rejecting heavily-chromatic
//    regions.
constexpr int kEstablishmentMinChords = 5;
constexpr int kPitchTolerance = 2;

// File-local helpers carry an lmd* prefix: the Unity/jumbo build concatenates
// every composing/analysis TU into one translation unit, so an unprefixed
// anonymous-namespace name (e.g. pcMod12) would ODR-clash with the same name in a
// sibling file (cadencekeyanchor.cpp).
inline int lmdPcMod12(int x) noexcept
{
    return ((x % 12) + 12) % 12;
}

/// 12-bit mask of the diatonic collection of a LOCAL key (hypothesized tonic +
/// mode) — key-agnostic: built from the tonic pc and mode alone, never a resolved
/// key.  Major: the major scale.  Minor: natural minor PLUS the raised leading
/// tone (harmonic minor), so a genuine minor V→i's raised LT does not count as a
/// chromatic intrusion.
inline uint16_t lmdCollectionMask(int tonicPc, bool minorMode) noexcept
{
    static constexpr int kMajor[]     = { 0, 2, 4, 5, 7, 9, 11 };
    static constexpr int kMinorHarm[] = { 0, 2, 3, 5, 7, 8, 10, 11 }; // natural minor + raised 7
    uint16_t m = 0;
    if (minorMode) {
        for (int d : kMinorHarm) {
            m |= static_cast<uint16_t>(1u << lmdPcMod12(tonicPc + d));
        }
    } else {
        for (int d : kMajor) {
            m |= static_cast<uint16_t>(1u << lmdPcMod12(tonicPc + d));
        }
    }
    return m;
}

/// Is `pc` a diatonic root degree of the local key?  Equal to membership in the
/// collection mask (major scale, or natural-minor + raised LT).
inline bool lmdRootIsDiatonic(int pc, int tonicPc, bool minorMode) noexcept
{
    return (lmdCollectionMask(tonicPc, minorMode) >> lmdPcMod12(pc)) & 1u;
}

/// Count of pitch classes set in `mask` that lie OUTSIDE the local collection.
inline int lmdOutOfCollectionCount(uint16_t mask, int tonicPc, bool minorMode) noexcept
{
    const uint16_t outside = static_cast<uint16_t>(mask & ~lmdCollectionMask(tonicPc, minorMode));
    int n = 0;
    for (int p = 0; p < 12; ++p) {
        if ((outside >> p) & 1u) {
            ++n;
        }
    }
    return n;
}

/// Is region r CONSISTENT with the hypothesized local key K=(tonicPc, minorMode)?
/// A region must carry a confident root that is a diatonic degree of K, and its
/// sounding pitch content must lie within K's collection up to kPitchTolerance
/// chromatic pitch classes.  Key-agnostic: reads only r's root/quality/mask.
bool lmdRegionConsistent(const CadenceRegionInput& r, int tonicPc, bool minorMode) noexcept
{
    if (r.rootPc < 0) {
        return false;   // gap / sparse region — never extends a local-key run
    }
    if (!lmdRootIsDiatonic(r.rootPc, tonicPc, minorMode)) {
        return false;
    }
    return lmdOutOfCollectionCount(r.pitchClassMask, tonicPc, minorMode) <= kPitchTolerance;
}

} // namespace

ModulationDetectionResult
detectLocalModulations(const std::vector<CadenceRegionInput>& regions,
                       int keySignatureFifths)
{
    ModulationDetectionResult result;

    // 1. CANDIDATES — the per-cadence local tonics (key-agnostic by construction).
    const std::vector<AuthenticCadence> cadences =
        detectAuthenticCadences(regions, keySignatureFifths);
    // The key-agnostic global (home) anchor — cadence-derived, NOT the resolved key.
    result.anchor = aggregateGlobalAnchor(cadences);
    if (cadences.empty() || regions.empty()) {
        return result;
    }

    const int n = static_cast<int>(regions.size());

    // 2. ESTABLISHMENT (assignment) — assign each region to the local key of the
    // NEAREST authentic cadence whose collection the region is consistent with.
    // "Nearest" = minimal tick distance to either cadence member (dominant or
    // resolution).  This partitions the timeline by the cadential structure
    // (each region belongs to exactly one local key, or none), so closely-related
    // keys do NOT engulf one another the way a maximal-consistent-run would, and a
    // spurious short cadence (e.g. an I→IV misread) cannot truncate a real key's
    // run — it merely claims a few regions that then fail the sustained-length and
    // confirmation gates.  Key-agnostic: only the cadence list + raw consistency.
    std::vector<int> assignedTonic(n, -1);
    std::vector<char> assignedMinor(n, 0);
    std::vector<char> hasAssignment(n, 0);
    for (int i = 0; i < n; ++i) {
        long long bestDist = LLONG_MAX;
        int bestTonic = -1;
        bool bestMinor = false;
        int bestTonicTick = INT_MAX;
        const int t = regions[i].startTick;
        for (const AuthenticCadence& c : cadences) {
            if (!lmdRegionConsistent(regions[i], c.tonicPc, c.minorMode)) {
                continue;
            }
            const long long dDom = std::llabs(static_cast<long long>(t) - c.dominantTick);
            const long long dTon = std::llabs(static_cast<long long>(t) - c.tonicTick);
            const long long dist = std::min(dDom, dTon);
            // Deterministic tie-break: nearer cadence, then earlier resolution,
            // then lower tonic pc, then major before minor.
            if (dist < bestDist
                || (dist == bestDist && c.tonicTick < bestTonicTick)
                || (dist == bestDist && c.tonicTick == bestTonicTick && c.tonicPc < bestTonic)
                || (dist == bestDist && c.tonicTick == bestTonicTick && c.tonicPc == bestTonic
                    && !c.minorMode && bestMinor)) {
                bestDist = dist;
                bestTonic = c.tonicPc;
                bestMinor = c.minorMode;
                bestTonicTick = c.tonicTick;
            }
        }
        if (bestTonic >= 0) {
            assignedTonic[i] = bestTonic;
            assignedMinor[i] = bestMinor ? 1 : 0;
            hasAssignment[i] = 1;
        }
    }

    // 3+4. CONFIRMATION + COMMIT — group maximal runs of consecutive regions with
    // the same assigned local key; commit a run only when it is SUSTAINED (≥
    // kEstablishmentMinChords regions) AND CONFIRMED (contains an authentic cadence
    // of that key resolving inside it).  Runs are non-overlapping by construction.
    int i = 0;
    while (i < n) {
        if (!hasAssignment[i]) {
            ++i;
            continue;
        }
        const int tonic = assignedTonic[i];
        const bool minor = assignedMinor[i] != 0;
        int j = i;
        while (j + 1 < n && hasAssignment[j + 1]
               && assignedTonic[j + 1] == tonic && (assignedMinor[j + 1] != 0) == minor) {
            ++j;
        }
        // run = regions [i, j]
        const int runChords = j - i + 1;
        const int startTick = regions[i].startTick;
        const int endTick = regions[j].endTick;

        int confirming = 0;
        int firstCadenceTick = -1;
        for (const AuthenticCadence& c : cadences) {
            if (c.tonicPc == tonic && c.minorMode == minor
                && c.tonicTick >= startTick && c.tonicTick < endTick) {
                ++confirming;
                if (firstCadenceTick < 0 || c.tonicTick < firstCadenceTick) {
                    firstCadenceTick = c.tonicTick;
                }
            }
        }

        if (runChords >= kEstablishmentMinChords && confirming >= 1) {
            LocalKeySpan span;
            span.startTick = startTick;
            span.endTick = endTick;
            span.tonicPc = tonic;
            span.minorMode = minor;
            span.establishmentChords = runChords;
            span.confirmingCadenceCount = confirming;
            span.firstCadenceTonicTick = firstCadenceTick;
            span.agreesWithAnchor = result.anchor.detected
                                    && result.anchor.tonicPc == tonic
                                    && result.anchor.minorMode == minor;
            result.spans.push_back(span);
        }
        i = j + 1;
    }

    return result;
}

} // namespace mu::composing::analysis
