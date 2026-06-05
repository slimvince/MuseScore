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

// harmonicfunctionlayer.cpp

#include "harmonicfunctionlayer.h"

namespace mu::composing::function {

void applyHarmonicFunction(analysis::ChordAnalysisResult& result,
                           const HarmonicFunctionContext& ctx)
{
    // E1: pass-through.
    // Logic is added incrementally:
    //   E2 — rootContinuityBonus, w_seq, w_dim migrate here
    //   E3 — Gate J, Gates A–D, dim7 rotation selection migrate here
    //   E4 — cadence detection, functional label completeness
    (void)result;
    (void)ctx;
}

} // namespace mu::composing::function
