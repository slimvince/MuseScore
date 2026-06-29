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
#include "forwardoverride.h"

namespace mu::composing::analysis {

double overrideBar(double earlierConfidence, const ForwardOverrideParams& p) noexcept
{
    // The bar scales with the earlier layer's confidence: a well-founded confident
    // commit demands decisively stronger contradicting evidence than a borderline one
    // (§8 case 4). Confidence is clamped to [0,1] so the bar is well-defined.
    double c = earlierConfidence;
    if (c < 0.0) {
        c = 0.0;
    } else if (c > 1.0) {
        c = 1.0;
    }
    return p.baseBar + p.confidenceScale * c;
}

bool overrides(double earlierConfidence, double contradictionStrength,
               const ForwardOverrideParams& p) noexcept
{
    // STRICTLY greater: at the exact bar the incumbent holds (the fixed tie-direction).
    return contradictionStrength > overrideBar(earlierConfidence, p);
}

bool OnePassClosure::isClosed(int decisionId) const noexcept
{
    return m_closed.find(decisionId) != m_closed.end();
}

bool OnePassClosure::markFinal(int decisionId)
{
    // insert() reports whether the id was newly added — i.e. not already closed.
    return m_closed.insert(decisionId).second;
}

bool OnePassClosure::tryOverride(int decisionId, double earlierConfidence,
                                 double contradictionStrength, const ForwardOverrideParams& p)
{
    if (isClosed(decisionId)) {
        return false;                           // already overturned/closed — never re-target (§8)
    }
    if (!overrides(earlierConfidence, contradictionStrength, p)) {
        return false;                           // the contradiction is not decisive — incumbent holds
    }
    markFinal(decisionId);                      // overturned ⇒ closed for the rest of the pass
    return true;
}

int OnePassClosure::forwardRecompute(int firstSlice, int lastSlice,
                                     const std::function<void(int)>& reread)
{
    if (m_recomputing) {
        return -1;                              // re-entrant: refuse (one localized re-run, never a loop)
    }
    if (firstSlice > lastSlice) {
        return -1;                              // empty / inverted range
    }
    m_recomputing = true;
    int n = 0;
    // FORWARD sweep, each slice once: localized (bounded to [firstSlice,lastSlice]),
    // forward (ascending), no back-edge (only the reread callback is invoked; nothing
    // upstream). Closed decisions are still re-read (their now-final label re-derived);
    // the callback decides per slice and respects closure via tryOverride/isClosed.
    for (int sliceId = firstSlice; sliceId <= lastSlice; ++sliceId) {
        if (reread) {
            reread(sliceId);
        }
        ++n;
    }
    m_recomputing = false;
    return n;
}

void OnePassClosure::reset() noexcept
{
    m_closed.clear();
    m_recomputing = false;
}

} // namespace mu::composing::analysis
