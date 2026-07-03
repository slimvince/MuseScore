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
#pragma once

// ── composing/analysis/voiceleading — VL-A: the VOICE-LINEAR VIEW (axis 2) ────
//
// The SECOND analysis axis (voice leading), foundation component VL-A. Spec:
// cowork_voiceleading_axis_design.md (SIGNED 2026-07-03) §5.1, §7. This is a FACT
// layer — it decides nothing, carries no confidence (the universality rule, §2).
//
// WHAT IT OWNS (and only this): the per-voice LINEAR reorganization of the Layer-1
// note model. It reorders the SAME lossless L1 notes by (staff, voice) and onset
// into per-voice event series — the linear reading of the same notes. It REUSES the
// one L1 note model (total unification, §3): it does NOT re-walk the score and adds
// no second note model.
//
// LOSSLESS — a partition, not a detection (§5.1): every retained L1 note appears in
// EXACTLY ONE voice's series EXACTLY ONCE; nothing is dropped, merged, or inferred.
// The notated (staff, voice) fact decides line membership; tie chains are already
// resolved by L1 (a tied group is one sounding event) and the view inherits that.
// flattenToNotes(view) reproduces the L1 content of the span (the round-trip law,
// asserted in the tests).
//
// CHORDAL VOICES ARE A RECORDED FACT, not an error (§5.1): all notes of one
// (staff, voice) sharing an onset are grouped into ONE chordal event (chordal flag).
//
// REDUCTION IS DECLARED, UNIFORM, AND PER-QUERY — never silent, never per-source
// (§5.1). A consumer needing one line from a chordal event names a reduction rule;
// v1 provides exactly one — TopNote (the highest sounding pitch per event, the
// study's curated-branch rule). The rule is a parameter of the QUERY (reducedPitch),
// never a mutation of the view; the choice rides the consumer's output provenance.
//
// PROFILE ELIGIBILITY (declared): a note is eligible for a PROFILE query iff it
// passes the standard analysis-view line filter `plays && visible && staffEligible`
// (the verified filter of the per-(staff,voice) line collapse in phraseboundaryview.cpp,
// the Layer-1.5 per-voice-line precedent). The LOSSLESS view itself keeps EVERYTHING
// (grace / non-playing / invisible / staff-ineligible notes are retained + flagged);
// the filter is applied only at profile-query time (VL-B), never to the view.
//
// DORMANT: no production consumer — nothing in src/ calls buildVoiceLinearView(); it
// is exercised only by voiceleading_tests.cpp and the default-OFF diagnostic
// tools/batch_analyze --dump-vl. Byte-identical on production by construction.

#include <optional>
#include <vector>

#include "composing/analysis/notemodel/note_model.h"

namespace mu::composing::analysis::voiceleading {

/// The declared, per-query reduction of a chordal event to a single line pitch.
/// v1 provides exactly TopNote (spec §5.1); alternatives (bass-note, per-stream) are
/// deferred until a consumer needs one (§15-3).
enum class ReductionRule {
    TopNote   ///< the highest sounding profile-eligible pitch of the event
};

/// One member note of a voice event — a lossless projection of a Layer-1 NoteEvent.
/// (staff, voice) live on the owning line; onset lives on the owning event; every
/// other L1 fact needed to reconstruct the NoteEvent is carried here. Metric weight
/// is NOT copied (spec §7 as signed — it stays with the shared scoreharvest machinery
/// and is read on demand; no second store of a derived quantity).
struct VoiceNote {
    int  pitch = 0;             ///< ppitch (== NoteEvent::pitch)
    int  tpc = -1;             ///< notated spelling (== NoteEvent::tpc); -1 = not provided
    int  release = 0;          ///< tie-resolved release tick
    int  duration = 0;         ///< release - onset
    bool isGrace = false;      ///< grace note (retained + flagged; NOT profile-eligible-excluded here)
    bool plays = true;         ///< NoteEvent::plays
    bool visible = true;       ///< NoteEvent::visible
    bool staffEligible = true; ///< NoteEvent::staffEligible
};

/// One event of a voice line: all notes of one (staff, voice) sharing an onset.
/// `chordal` is a recorded fact (more than one member pitch), not an error.
struct VoiceEvent {
    int  onset = 0;
    bool chordal = false;              ///< notes.size() > 1
    std::vector<VoiceNote> notes;      ///< build order (as in the L1 model); size >= 1
};

/// One voice line: a (staff, voice) identity plus its onset-ordered events.
struct VoiceLine {
    int staff = 0;
    int voice = 0;
    std::vector<VoiceEvent> events;    ///< ascending onset
};

/// The whole voice-linear view over a note model's LOADED span.
struct VoiceLinearView {
    std::vector<VoiceLine> lines;      ///< sorted by (staff, voice)
};

/// Profile eligibility of a member note (the standard analysis-view line filter,
/// spec §5.1 as declared): `plays && visible && staffEligible`.
bool isProfileEligible(const VoiceNote& n);

/// The declared per-query reduction of an event to a single sounding pitch among its
/// PROFILE-ELIGIBLE members. std::nullopt if no member is profile-eligible. v1: the
/// highest eligible pitch (TopNote). Never mutates the view.
std::optional<int> reducedPitch(const VoiceEvent& e, ReductionRule rule = ReductionRule::TopNote);

/// Build the lossless voice-linear view from the Layer-1 note set (build order:
/// ascending onset, then staff, voice, chord-note — the NoteModel invariant). Every
/// note appears in exactly one line's events exactly once; nothing dropped/merged;
/// all L1 flags carried. The pure core — plain-data constructible, so the oracle
/// tests inject NoteEvents by hand.
VoiceLinearView buildVoiceLinearView(const std::vector<notemodel::NoteEvent>& notes);

/// Convenience overload over a built note model — reuses model.notes() (does NOT
/// re-walk the score; total unification). The view covers the model's LOADED span.
VoiceLinearView buildVoiceLinearView(const notemodel::NoteModel& model);

/// Flatten the view back to a note set (the round-trip losslessness law, §5.1). The
/// returned notes carry every field needed to compare against the source L1 notes.
std::vector<notemodel::NoteEvent> flattenToNotes(const VoiceLinearView& view);

} // namespace mu::composing::analysis::voiceleading
