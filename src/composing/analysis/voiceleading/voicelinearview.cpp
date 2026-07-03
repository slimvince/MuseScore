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

#include "composing/analysis/voiceleading/voicelinearview.h"

#include <map>
#include <utility>

namespace mu::composing::analysis::voiceleading {

using notemodel::NoteEvent;
using notemodel::NoteModel;

bool isProfileEligible(const VoiceNote& n)
{
    // The standard analysis-view line filter (spec §5.1) — the verified filter of the
    // per-(staff,voice) line collapse in phraseboundaryview.cpp.
    return n.plays && n.visible && n.staffEligible;
}

std::optional<int> reducedPitch(const VoiceEvent& e, ReductionRule rule)
{
    // v1 provides exactly TopNote: the highest PROFILE-ELIGIBLE pitch of the event.
    (void)rule;   // only TopNote exists in v1; the parameter fixes the query provenance.
    std::optional<int> top;
    for (const VoiceNote& n : e.notes) {
        if (!isProfileEligible(n)) {
            continue;
        }
        if (!top || n.pitch > *top) {
            top = n.pitch;
        }
    }
    return top;
}

VoiceLinearView buildVoiceLinearView(const std::vector<NoteEvent>& notes)
{
    // Bucket by (staff, voice) into lines (std::map keeps them (staff,voice)-sorted),
    // preserving the L1 build order within each line; then group runs of equal onset
    // into one chordal event. This mirrors phraseboundaryview::collectVoiceLines
    // (the L1 note set is onset-sorted, so each bucket is onset-ascending and same-
    // onset members are contiguous) — but LOSSLESS: it keeps every member note, never
    // collapsing to a single pitch.
    std::map<std::pair<int, int>, VoiceLine> byLine;
    for (const NoteEvent& n : notes) {
        VoiceLine& line = byLine[{ n.staff, n.voice }];
        line.staff = n.staff;
        line.voice = n.voice;
        VoiceNote vn;
        vn.pitch = n.pitch;
        vn.tpc = n.tpc;
        vn.release = n.release;
        vn.duration = n.duration;
        vn.isGrace = n.isGrace;
        vn.plays = n.plays;
        vn.visible = n.visible;
        vn.staffEligible = n.staffEligible;
        if (!line.events.empty() && line.events.back().onset == n.onset) {
            line.events.back().notes.push_back(vn);
            line.events.back().chordal = true;
        } else {
            VoiceEvent ev;
            ev.onset = n.onset;
            ev.chordal = false;
            ev.notes.push_back(vn);
            line.events.push_back(std::move(ev));
        }
    }
    VoiceLinearView view;
    view.lines.reserve(byLine.size());
    for (auto& kv : byLine) {
        view.lines.push_back(std::move(kv.second));
    }
    return view;
}

VoiceLinearView buildVoiceLinearView(const NoteModel& model)
{
    return buildVoiceLinearView(model.notes());
}

std::vector<NoteEvent> flattenToNotes(const VoiceLinearView& view)
{
    std::vector<NoteEvent> out;
    for (const VoiceLine& line : view.lines) {
        for (const VoiceEvent& ev : line.events) {
            for (const VoiceNote& n : ev.notes) {
                NoteEvent e;
                e.pitch = n.pitch;
                e.tpc = n.tpc;
                e.staff = line.staff;
                e.voice = line.voice;
                e.onset = ev.onset;
                e.release = n.release;
                e.duration = n.duration;
                e.isGrace = n.isGrace;
                e.plays = n.plays;
                e.visible = n.visible;
                e.staffEligible = n.staffEligible;
                out.push_back(e);
            }
        }
    }
    return out;
}

} // namespace mu::composing::analysis::voiceleading
