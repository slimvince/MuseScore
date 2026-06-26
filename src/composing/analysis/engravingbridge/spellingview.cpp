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

#include "spellingview.h"

#include "engraving/dom/pitchspelling.h"

namespace mu::composing::analysis::engravingbridge {

using mu::engraving::Tpc;
using mu::engraving::tpcIsValid;

// lineOfFifths is the SOLE place that turns a tpc into a line-of-fifths position
// and the SOLE place that applies the `tpcIsValid()` presence test. sharpFlatSense
// and spanSpelling derive from it, so the interpretation lives in exactly one
// place (the unification rule) — a kNoLineOfFifths return encodes "absent/invalid".
int lineOfFifths(int tpc)
{
    if (!tpcIsValid(tpc)) {
        return kNoLineOfFifths;
    }
    return tpc - static_cast<int>(Tpc::TPC_C);
}

int sharpFlatSense(int tpc)
{
    const int lof = lineOfFifths(tpc);
    if (lof == kNoLineOfFifths) {
        return 0;
    }
    return (lof > 0) - (lof < 0);
}

SpanSpelling spanSpelling(const std::vector<int>& tpcs)
{
    SpanSpelling agg;
    long long lofSum = 0;
    for (int tpc : tpcs) {
        const int lof = lineOfFifths(tpc);
        if (lof == kNoLineOfFifths) {
            continue; // absent/invalid spelling — skip (the tpcIsValid presence test)
        }
        ++agg.count;
        lofSum += lof;
        if (lof > 0) {
            ++agg.sharpCount;
        } else if (lof < 0) {
            ++agg.flatCount;
        } else {
            ++agg.naturalCount;
        }
    }
    if (agg.count > 0) {
        agg.lofCentroid = static_cast<double>(lofSum) / agg.count;
    }
    return agg;
}

} // namespace mu::composing::analysis::engravingbridge
