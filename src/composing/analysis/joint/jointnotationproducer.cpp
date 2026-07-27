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

#include "jointnotationproducer.h"

#include "jointfactadapter.h"   // buildAdapterFacts / AdapterFacts (the score -> facts step)
#include "jointweights.h"       // selectedWeights / WeightVector (the SELECTED production vector)
// JointTables / Vocabulary / ChordCache / FittedAdapter / decodePiece come via jointnotationrecord.h
// (-> jointdecoder.h / jointadapter.h / jointtables.h). assembleNotationRecord is declared there too.

namespace mu::composing::analysis::joint {

NotationRecordResult produceNotationRecord(const Piece& piece, std::optional<int> sigFifths,
                                           const std::string& declaredMode)
{
    NotationRecordResult res;

    // The PRODUCTION fitted values (ratified Decision D1): the compiled-in EMBEDDED tables + adapter +
    // the SELECTED weight vector — byte-identical to the committed tools/joint_estimator artifacts. No
    // filesystem read, no caching: loaded fresh per call (a shared/cached loader is a later, measured
    // concern, not built speculatively — #17's funnel; this increment is dormant).
    JointTables tables = JointTables::loadEmbedded("all");
    if (!tables.loaded) {
        res.error = "embedded tables load failed: " + tables.error;
        return res;
    }
    Vocabulary vocab(tables);
    ChordCache cache;
    const WeightVector selected = selectedWeights();
    FittedAdapter adapter = FittedAdapter::loadEmbedded(selected);
    if (!adapter.loaded()) {
        res.error = "embedded adapter load failed: " + adapter.error();
        return res;
    }

    // Whole-score decode, ONCE (§5 total order, seg_cap 4); then the record assembly, which attaches the
    // §3.3 posterior slice (it re-scores the committed spans; it does NOT re-decode). Deterministic.
    const DecodeResult r = decodePiece(piece, adapter, vocab, cache, 4, sigFifths, declaredMode);
    res.record = assembleNotationRecord(piece, r, sigFifths, declaredMode, adapter, vocab, cache);
    res.ok = true;
    return res;
}

NotationRecordResult produceNotationRecord(const mu::engraving::Score* score, const std::string& stem)
{
    NotationRecordResult res;
    const AdapterFacts fx = buildAdapterFacts(score, stem);
    if (!fx.ok) {
        // The adapter could not extract the score (e.g. a null score): an unambiguous FAILURE, never a
        // partial record, never a silent fallback to anything (#13). The caller branches on `ok`.
        res.error = "adapter extraction failed: " + fx.error;
        return res;
    }
    return produceNotationRecord(fx.piece, fx.sigFifths, fx.declaredMode);
}

std::vector<int> spanViewSegments(const NotationRecord& rec, int startTick, int endTick)
{
    std::vector<int> out;
    if (startTick >= endTick) {
        return out;   // an empty (or inverted) span selects nothing
    }
    for (int i = 0; i < static_cast<int>(rec.segments.size()); ++i) {
        const RecordSegment& s = rec.segments[i];
        if (s.startTick < endTick && s.endTick > startTick) {   // overlap
            out.push_back(i);
        }
    }
    return out;
}

NoteView noteView(const NotationRecord& rec, int tick)
{
    NoteView v;
    for (int i = 0; i < static_cast<int>(rec.segments.size()); ++i) {
        const RecordSegment& s = rec.segments[i];
        if (s.startTick <= tick && tick < s.endTick) {   // containing segment; a boundary tick belongs
            v.found = true;                              // to the segment it STARTS (half-open [start,end))
            v.segmentIndex = i;
            v.segment = &s;
            v.slice = (i < static_cast<int>(rec.slices.size())) ? &rec.slices[i] : nullptr;
            return v;
        }
    }
    return v;   // `tick` is outside the analyzed span
}

} // namespace mu::composing::analysis::joint
