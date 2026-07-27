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

#ifndef MU_COMPOSING_ANALYSIS_JOINT_JOINTNOTATIONPRODUCER_H
#define MU_COMPOSING_ANALYSIS_JOINT_JOINTNOTATIONPRODUCER_H

#include <optional>
#include <string>
#include <vector>

#include "jointnotationrecord.h"   // NotationRecord / RecordSegment / SegmentSlice / Piece

namespace mu::engraving {
class Score;
}

// ── The record-producing entry + the two seam views (notation output-surface contract §1) ──────────
//
// This is the PRODUCER side of the two §1 seams: the one-call score->record entry, plus the span view
// and the note view that READ the produced record. It composes ONLY already-delivered, established
// parts (buildAdapterFacts + the embedded tables/adapter/weights + decodePiece + assembleNotationRecord,
// which itself attaches the §3.3 slice) — no inference, no new derivation. The consumer side (the
// re-plumbed notation consumers) is the SEAMS PART 2 dispatch; this increment builds the producer + the
// views and leaves them DORMANT (declared dormancy — nothing in src/ calls them yet).
//
// Spec: cowork_notation_output_contract.md §1 (the two seams) + §3 (the record); the producer chain is
// the same as tools/batch_analyze --joint-inference's decode + assembleNotationRecord.

namespace mu::composing::analysis::joint {

// The result of producing a notation record: either the full record (ok == true) or an unambiguous
// FAILURE (ok == false, `error` set) — returned when the fact adapter cannot extract the score
// (AdapterFacts.ok == false, e.g. a null score). NEVER a partial record, NEVER a silent fallback (#13):
// a consumer must branch on `ok` before reading `record`.
struct NotationRecordResult {
    bool ok = false;
    std::string error;          ///< human-readable cause, set iff !ok
    NotationRecord record;      ///< valid iff ok
};

/// The seams' one-call PRODUCER: score in -> record out. buildAdapterFacts (the L1 published-fact
/// surface) -> the compiled-in EMBEDDED tables/adapter + the SELECTED weight vector (ratified Decision
/// D1) -> decodePiece (§5 total order, seg_cap 4) -> computePosteriorSlice (inside assembleNotationRecord)
/// -> the §3.1–§3.4 record. WHOLE-SCORE decode, ONCE; deterministic (§5); NO caching in this increment
/// (a cache is a later, measured concern — #17's funnel, not built speculatively). Returns an
/// unambiguous FAILURE when the adapter cannot extract the score (never a partial record).
NotationRecordResult produceNotationRecord(const mu::engraving::Score* score, const std::string& stem);

/// The facts->record CORE of the producer (the above minus buildAdapterFacts): a prepared decode Piece
/// + its prior inputs (`sigFifths`/`declaredMode`) -> the record. Loads the embedded production
/// tables/adapter/weights, decodes ONCE, assembles. `piece.stem` labels the record. Shared by the
/// score overload; also the establishment seam (exercised on the committed note_events pieces, where the
/// score-reading half is separately established by the input-parity drivers).
NotationRecordResult produceNotationRecord(const Piece& piece, std::optional<int> sigFifths,
                                           const std::string& declaredMode);

/// §1 seam 1 — the SPAN VIEW: the record segments intersecting [startTick, endTick), in segment order.
/// A pure view (NO recompute, #6): a segment is included iff it OVERLAPS the span
/// (seg.startTick < endTick && seg.endTick > startTick). An empty span (startTick >= endTick) selects
/// nothing. Returned as indices into `rec.segments` (and, lock-step, `rec.slices`); the §3.1 piece block
/// is the record's own fields (`rec.spanStartTick`/`spanEndTick`/`sigFifths`/`declaredMode`/`provenance`).
std::vector<int> spanViewSegments(const NotationRecord& rec, int startTick, int endTick);

/// §1 seam 2 — the NOTE VIEW: the record segment CONTAINING `tick` (seg.startTick <= tick < seg.endTick
/// — a tick on a segment boundary belongs to the segment it STARTS), resolving the committed reading,
/// the derived facts (`segment`), and the §3.3 group (i) slice (`slice`) — the display-ready answer,
/// NO recompute (#6: a lookup into the record). `found` is false when `tick` is outside the analyzed
/// span; then `segment`/`slice` are null and `segmentIndex` is -1.
struct NoteView {
    bool found = false;
    int segmentIndex = -1;
    const RecordSegment* segment = nullptr;   ///< &rec.segments[segmentIndex] when found
    const SegmentSlice* slice = nullptr;      ///< &rec.slices[segmentIndex] when found (null if the
                                              ///< record carries no slice at that index)
};
NoteView noteView(const NotationRecord& rec, int tick);

} // namespace mu::composing::analysis::joint

#endif // MU_COMPOSING_ANALYSIS_JOINT_JOINTNOTATIONPRODUCER_H
