/*
 * SPDX-License-Identifier: GPL-3.0-only
 * MuseScore-Studio-CLA-applies
 *
 * MuseScore Studio
 * Music Composition & Notation
 *
 * Copyright (C) 2021 MuseScore Limited
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

/// Internal helpers shared between the analysis bridge and the tuning bridge.
///
/// Scope policy — include ONLY from these translation units:
///   • notationcomposingbridgehelpers.cpp  (shared bridge helpers)
///   • notationcomposingbridge.cpp         (single-note analysis path)
///   • notationharmonicrhythmbridge.cpp    (time-range analysis path)
///   • notationimplodebridge.cpp           (chord-staff population)
///   • notationtuningbridge.cpp            (per-note tuning)
///
/// Do NOT include from public headers or outside the notation/internal/ directory.
/// These helpers depend on engraving types and must not leak into composing/ code.

#pragma once

#include <cstddef>
#include <set>
#include <vector>

#include "composing/analysis/region/harmonicrhythm.h"
#include "engraving/dom/score.h"
#include "engraving/dom/staff.h"
#include "engraving/dom/part.h"

namespace mu::notation::internal {

/// Temporary name-based chord staff detection.
/// TODO: replace with a proper Part-level flag (see backlog).
inline bool isChordTrackStaff(const mu::engraving::Score* sc, size_t si)
{
    static const muse::String CHORD_TRACK_MARKER = u"Chord Track";
    if (si >= sc->nstaves()) {
        return false;
    }
    const mu::engraving::Part* part = sc->staff(si)->part();
    if (!part) {
        return false;
    }

    if (part->partName().contains(CHORD_TRACK_MARKER)) {
        return true;
    }

    const mu::engraving::Instrument* instrument = part->instrument();
    return instrument && instrument->trackName().contains(CHORD_TRACK_MARKER);
}

/// Is this staff eligible for harmonic analysis at the given tick?
/// Excludes hidden staves, percussion instruments, and chord staff staves.
inline bool staffIsEligible(const mu::engraving::Score* sc, size_t si,
                             const mu::engraving::Fraction& tick)
{
    const mu::engraving::Staff* st = sc->staff(si);
    if (!st->show()) {
        return false;
    }
    if (st->part()->instrument(tick)->useDrumset()) {
        return false;
    }
    if (isChordTrackStaff(sc, si)) {
        return false;
    }
    return true;
}

/// Returns the set of staff indices that are chord-track staves in sc.
/// These should be excluded from harmonic analysis input but may receive
/// annotation output (see chord-track priority rule).
inline std::set<size_t> chordTrackExcludeStaves(const mu::engraving::Score* sc)
{
    std::set<size_t> out;
    for (size_t si = 0; si < sc->nstaves(); ++si) {
        if (isChordTrackStaff(sc, si)) {
            out.insert(si);
        }
    }
    return out;
}

struct HarmonicRegionDebugCapture {
    std::vector<mu::composing::analysis::HarmonicRegion>* preMergeRegions = nullptr;
    std::vector<mu::composing::analysis::HarmonicRegion>* postMergeRegions = nullptr;
};

void setHarmonicRegionDebugCapture(HarmonicRegionDebugCapture* capture);
HarmonicRegionDebugCapture* harmonicRegionDebugCapture();

class ScopedHarmonicRegionDebugCapture {
public:
    explicit ScopedHarmonicRegionDebugCapture(HarmonicRegionDebugCapture* capture)
        : m_previous(harmonicRegionDebugCapture())
    {
        setHarmonicRegionDebugCapture(capture);
    }

    ~ScopedHarmonicRegionDebugCapture()
    {
        setHarmonicRegionDebugCapture(m_previous);
    }

    ScopedHarmonicRegionDebugCapture(const ScopedHarmonicRegionDebugCapture&) = delete;
    ScopedHarmonicRegionDebugCapture& operator=(const ScopedHarmonicRegionDebugCapture&) = delete;

private:
    HarmonicRegionDebugCapture* m_previous = nullptr;
};

} // namespace mu::notation::internal
