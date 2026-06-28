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

#include "phraseboundaryview.h"

#include "engraving/dom/engravingitem.h"
#include "engraving/dom/measure.h"
#include "engraving/dom/score.h"
#include "engraving/dom/segment.h"

namespace mu::composing::analysis::engravingbridge {

// STEP A — fermata-only, byte-identical to the two retired hand-synced scans
// (regionanalyzer jkdPhraseBoundaryTicks + batch_analyze collectPhraseBoundaryTicks).
// Walk every measure -> ChordRest segment -> annotation; a segment carrying a
// fermata contributes its tick. Notation only (no key/function): the boundary is
// read off the engraved surface.
std::set<int> phraseBoundaryTicks(const mu::engraving::Score* score)
{
    using namespace mu::engraving;
    std::set<int> ticks;
    if (!score) {
        return ticks;
    }
    for (const Measure* m = score->firstMeasure(); m; m = m->nextMeasure()) {
        for (const Segment* s = m->first(SegmentType::ChordRest); s;
             s = s->next(SegmentType::ChordRest)) {
            for (const EngravingItem* e : s->annotations()) {
                if (e && e->isFermata()) {
                    ticks.insert(s->tick().ticks());
                    break;
                }
            }
        }
    }
    return ticks;
}

} // namespace mu::composing::analysis::engravingbridge
