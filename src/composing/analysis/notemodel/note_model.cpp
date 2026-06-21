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

#include "note_model.h"

#include <algorithm>

#include "engraving/dom/chord.h"
#include "engraving/dom/chordrest.h"
#include "engraving/dom/measure.h"
#include "engraving/dom/note.h"
#include "engraving/dom/score.h"
#include "engraving/dom/segment.h"
#include "engraving/dom/staff.h"

// Reuse the existing staff-eligibility predicate (hidden / drumset / chord-track)
// as a per-note annotation — derived, not duplicated. See design §1/§4.1.
#include "composing/analysis/engravingbridge/regiontonecollector.h"

namespace mu::composing::analysis::notemodel {

namespace {

// Emit one NoteEvent for a (tie-resolved) note. Tie continuations are skipped by
// the caller (they are subsumed into the tie-start note's span).
NoteEvent makeEvent(const mu::engraving::Note* n, int onsetTick, int staff, int voice,
                    bool isGrace, bool staffEligible)
{
    using namespace mu::engraving;
    NoteEvent e;
    e.pitch         = n->ppitch();
    e.tpc           = n->tpc();
    e.staff         = staff;
    e.voice         = voice;
    e.onset         = onsetTick;
    // playTicksFraction() returns the tie-resolved sounding length (the chord's
    // own actualTicks() when untied; lastTiedNote.endTick - firstTiedNote.tick
    // across a tied group). It is the DOM's authoritative tie-aware span.
    e.duration      = n->playTicksFraction().ticks();
    e.release       = onsetTick + e.duration;
    e.isGrace       = isGrace;
    e.plays         = n->play();
    e.visible       = n->visible();
    e.staffEligible = staffEligible;
    return e;
}

} // namespace

NoteModel NoteModel::build(const mu::engraving::Score* sc)
{
    using namespace mu::engraving;
    namespace ebr = mu::composing::analysis::engravingbridge;

    NoteModel model;
    model.m_score = sc;
    if (!sc) {
        return model;
    }

    const Measure* firstMeasure = sc->firstMeasure();
    if (!firstMeasure) {
        return model;
    }

    // Walk every ChordRest segment across the whole score (next1 crosses
    // barlines). For each, walk every staff and voice. Notes are appended in
    // (ascending onset, staff, voice, chord-note) order, so m_notes is sorted by
    // onset by construction.
    for (const Segment* s = firstMeasure->first(SegmentType::ChordRest);
         s != nullptr;
         s = s->next1(SegmentType::ChordRest)) {
        const int segTick = s->tick().ticks();

        for (std::size_t si = 0; si < sc->nstaves(); ++si) {
            // staffEligible is an ANNOTATION computed once per note at its onset
            // tick (hidden/drumset/chord-track). It is NOT a drop — ineligible
            // notes are kept and flagged.
            const bool eligible = ebr::staffIsEligible(sc, si, s->tick());

            for (int v = 0; v < VOICES; ++v) {
                const ChordRest* cr
                    = s->cr(static_cast<track_idx_t>(si) * VOICES + v);
                if (!cr || !cr->isChord()) {
                    continue;  // rests and empty slots contribute no notes
                }
                const Chord* chord = toChord(cr);

                // Grace notes hang off the main chord (not their own segment
                // slot). Keep them, flagged isGrace, attached to the parent
                // chord's tick (so they group with that slice downstream).
                for (const Chord* grace : chord->graceNotes()) {
                    if (!grace) {
                        continue;
                    }
                    for (const Note* gn : grace->notes()) {
                        if (gn->tieBack()) {
                            continue;  // continuation — subsumed into its tie-start
                        }
                        model.m_notes.push_back(
                            makeEvent(gn, segTick, static_cast<int>(si), v, true, eligible));
                    }
                }

                // Main chord notes.
                for (const Note* n : chord->notes()) {
                    if (n->tieBack()) {
                        // Tie continuation: already represented by the tie-start
                        // note's resolved span. Exactly one onset per tied group.
                        continue;
                    }
                    model.m_notes.push_back(
                        makeEvent(n, segTick, static_cast<int>(si), v, false, eligible));
                }
            }
        }
    }

    return model;
}

std::vector<const NoteEvent*> NoteModel::overlapping(int t0, int t1) const
{
    std::vector<const NoteEvent*> out;
    if (t1 <= t0) {
        return out;
    }
    // m_notes is sorted by onset ascending. A note overlaps [t0, t1) iff
    // onset < t1 && release > t0. Only notes with onset < t1 can qualify, so
    // scan the onset-sorted prefix up to the first onset >= t1.
    for (const NoteEvent& e : m_notes) {
        if (e.onset >= t1) {
            break;
        }
        if (e.release > t0) {
            out.push_back(&e);
        }
    }
    return out;
}

std::vector<const NoteEvent*> NoteModel::onsetIn(int t0, int t1) const
{
    std::vector<const NoteEvent*> out;
    if (t1 <= t0) {
        return out;
    }
    for (const NoteEvent& e : m_notes) {
        if (e.onset >= t1) {
            break;
        }
        if (e.onset >= t0) {
            out.push_back(&e);
        }
    }
    return out;
}

} // namespace mu::composing::analysis::notemodel
