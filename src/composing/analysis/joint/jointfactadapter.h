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

#ifndef MU_COMPOSING_ANALYSIS_JOINT_JOINTFACTADAPTER_H
#define MU_COMPOSING_ANALYSIS_JOINT_JOINTFACTADAPTER_H

#include <optional>
#include <string>
#include <vector>

#include "jointdecoder.h"   // Piece / NoteRec / EventRec

namespace mu::engraving {
class Score;
}

// ── The joint estimator's FACT ADAPTER (score -> Piece) ──────────────────────────────────────────
//
// This is the "score -> facts" build step the --joint-decode-corpus driver comment names as separate.
// It builds the decoder's inputs from the L1 PUBLISHED fact surface — the note model's notatedNotes()
// tie-UNRESOLVED atoms (Task B) — plus the score's STRUCTURAL facts (measure layout, initial key
// signature/mode, meter). It NEVER re-walks the note DOM: every note fact is read through
// notemodel::NoteModel::notatedNotes(); the only score reads are the metric layout (measures/ticks),
// the initial KeySigEvent (signature fifths + declared mode — the OI-180-listed adapter inputs), and
// the time signature. There is no L1 publication of the measure/meter/signature structure, so those
// structural facts are read from the Score directly (reported in the include-closure audit). A
// module-private RAW-NOTE walk stays forbidden (OI-180); this reads the published notated notes.
//
// It is the C++ counterpart of the music21 extraction tools/joint_estimator/gen_note_events.py, and
// the two-readers-agree "input parity" establishment (gen_input_parity.py) grades the adapter's facts
// against the committed note_events.json field by field, enumerating any divergence by class.
//
// Field derivations (matching gen_note_events.py exactly):
//   note.onset  = notatedNote.onset (segment tick, 480/quarter — == music21 round(offset*480))
//   note.dur    = notatedNote.duration (Chord::actualTicks — the NOTATED, tie-unresolved length)
//   note.pc     = pitch % 12;   note.midi = pitch (ppitch)
//   note.lof    = tpc - Tpc::TPC_C   (line-of-fifths, C=0; == music21 step_lof + 7*alter)
//   note.part   = index of the note's staff's Part among score->parts() (== music21 part index)
//   note.measure= music21 measure number (leading pickup = 0, then 1,2,3,...)
//   note.beat   = music21 native .beat (1-indexed quarter-beat; PADDED for the leading pickup)
//   note.mc     = glt._beat_class(beat, n_quarter)
//   note.ap/dp  = melodic step/leap/none vs the temporally-adjacent same-PART note (gen_note_events._melodic)
//   note.tied   = notatedNote.tieContinuation (Note::tieBack != null == music21 tie.type in stop/continue)
//   note.ferm   = notatedNote.hasFermata
// Grace notes (music21 skips dur<=0) are excluded. The event lattice + per-event facts match
// gen_note_events.extract_stem exactly (minimal Pardo-Birmingham segments over notated onsets/offsets).
//
// DORMANT (no production consumer). Spec: cowork_joint_estimator_factorization.md §1; gen_note_events.py.

namespace mu::composing::analysis::joint {

struct AdapterFacts {
    bool ok = false;
    std::string error;

    Piece piece;                          ///< notes/events populated + prepare() called.
    std::optional<int> meterBeats;        ///< first time-signature numerator (music21 _time_signature).
    std::optional<int> meterBeatType;     ///< first time-signature denominator.
    bool multiMeter = false;              ///< more than one distinct time signature.

    std::optional<int> sigFifths;         ///< initial key-signature fifths (read_xml_header init_fifths).
    std::string declaredMode;             ///< "major" | "minor" | "" (read_xml_header declared_mode).
};

/// Build the joint decoder's inputs for one score from the published note-model surface + the score's
/// structural facts. `stem` labels the returned Piece. Never re-walks the note DOM (OI-180).
AdapterFacts buildAdapterFacts(const mu::engraving::Score* score, const std::string& stem);

} // namespace mu::composing::analysis::joint

#endif // MU_COMPOSING_ANALYSIS_JOINT_JOINTFACTADAPTER_H
