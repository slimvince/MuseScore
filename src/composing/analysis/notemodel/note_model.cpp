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
#include <climits>

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

    model.m_index.build(model.m_notes);
    return model;
}

// ── NoteQueryIndex ───────────────────────────────────────────────────────────

void NoteQueryIndex::build(const std::vector<NoteEvent>& notes)
{
    m_n = static_cast<int>(notes.size());
    m_onsets.clear();
    m_onsets.reserve(notes.size());
    for (const NoteEvent& e : notes) {
        m_onsets.push_back(e.onset);  // notes are onset-sorted ⇒ m_onsets ascending.
    }

    if (m_n == 0) {
        m_segSize = 0;
        m_segMaxRel.clear();
        return;
    }

    // Perfect binary tree over the smallest power-of-two leaf count >= N. Real
    // leaves carry the note's release; padded leaves carry INT_MIN so they are
    // always pruned (no release > t0 for any t0). Internal node = max of children.
    m_segSize = 1;
    while (m_segSize < m_n) {
        m_segSize <<= 1;
    }
    m_segMaxRel.assign(static_cast<std::size_t>(2) * m_segSize, INT_MIN);
    for (int i = 0; i < m_n; ++i) {
        m_segMaxRel[m_segSize + i] = notes[i].release;
    }
    for (int v = m_segSize - 1; v >= 1; --v) {
        m_segMaxRel[v] = std::max(m_segMaxRel[2 * v], m_segMaxRel[2 * v + 1]);
    }
}

int NoteQueryIndex::onsetLowerBound(int t) const
{
    return static_cast<int>(
        std::lower_bound(m_onsets.begin(), m_onsets.end(), t) - m_onsets.begin());
}

void NoteQueryIndex::overlapIndices(int qHi, int t0, std::vector<int>& out) const
{
    if (qHi <= 0 || m_segSize == 0) {
        return;
    }
    collect(1, 0, m_segSize, qHi, t0, out);
}

void NoteQueryIndex::collect(int node, int nodeLo, int nodeHi, int qHi, int t0,
                             std::vector<int>& out) const
{
    if (nodeLo >= qHi) {
        return;  // node's whole range is beyond the onset prefix [0, qHi).
    }
    if (m_segMaxRel[node] <= t0) {
        return;  // no leaf in this subtree has release > t0 ⇒ none overlaps.
    }
    if (nodeHi - nodeLo == 1) {
        // Reaching a leaf means nodeLo < qHi (first guard) AND its release > t0
        // (second guard) — so it qualifies unconditionally. Padded leaves carry
        // INT_MIN and are pruned above, so nodeLo is always a real index here.
        out.push_back(nodeLo);
        return;
    }
    const int mid = (nodeLo + nodeHi) / 2;
    collect(2 * node, nodeLo, mid, qHi, t0, out);          // left first ⇒ ascending order.
    collect(2 * node + 1, mid, nodeHi, qHi, t0, out);
}

std::vector<const NoteEvent*> NoteModel::overlapping(int t0, int t1) const
{
    std::vector<const NoteEvent*> out;
    if (t1 <= t0 || m_notes.empty()) {
        return out;
    }
    // A note overlaps [t0, t1) iff onset < t1 && release > t0. The onset bound is
    // the prefix [0, qHi) (qHi = first onset >= t1); within it the release filter
    // is answered by the max-release segment tree. Indices come back ascending,
    // so the result preserves build order — byte-identical to the old head scan.
    const int qHi = m_index.onsetLowerBound(t1);
    std::vector<int> idx;
    m_index.overlapIndices(qHi, t0, idx);
    out.reserve(idx.size());
    for (int i : idx) {
        out.push_back(&m_notes[i]);
    }
    return out;
}

std::vector<const NoteEvent*> NoteModel::onsetIn(int t0, int t1) const
{
    std::vector<const NoteEvent*> out;
    if (t1 <= t0 || m_notes.empty()) {
        return out;
    }
    // Onsets are sorted ascending: the notes whose onset lies in [t0, t1) form the
    // contiguous block [lower_bound(t0), lower_bound(t1)) — preserving build order.
    const int lo = m_index.onsetLowerBound(t0);
    const int hi = m_index.onsetLowerBound(t1);
    out.reserve(static_cast<std::size_t>(hi - lo));
    for (int i = lo; i < hi; ++i) {
        out.push_back(&m_notes[i]);
    }
    return out;
}

} // namespace mu::composing::analysis::notemodel
