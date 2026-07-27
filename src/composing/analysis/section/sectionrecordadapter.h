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

// ── composing/analysis/section/sectionrecordadapter ──────────────────────────
//
// The RECORD-path variant of analyzeSection: analyzeSectionFromRecord derives the shared
// AnalyzedSection output type from the joint estimator's NOTATION OUTPUT-SURFACE RECORD
// (jointnotationrecord.h) instead of the legacy Pass-0 HarmonicRegion stream. It is the P2b step
// of the seams-part-2 consumer re-plumb: the section layer, record path (dispatch
// cc_instruction_notation_seams_2.md, partition P2).
//
// DORMANT (declared dormancy — no src/ caller yet; the named consumer is the span/implode bridge
// re-plumb, P3/P4, behind the default-OFF useJointNotationRecord flag). Byte-identical on production
// by construction: nothing calls it.
//
// It is a CONSUMER of the published record (a pure data surface) plus the score's L1 note surface
// (for the per-segment tone re-collection, composing-side — the SAME NoteModel/weightedPcView the
// legacy analyzeSection uses; #7). It NEVER re-decodes, never invokes the legacy analysis
// (analyzeRegions/analyzeChord/the legacy key layer), and computes NO inference. A's decode is
// contiguous by construction, so the legacy gap-fill / trim / measure-layout / key-stabilization
// machinery is NOT ported — one record segment maps to one AnalyzedRegion, 1:1.
//
// Spec: cowork_notation_output_contract.md §3 (the record) + §4 (the consumer mapping);
// cowork_notation_adoption_increment.md (Decision A2/C1); the P1 exposure measurement
// tools/notation_seams/exposure_constants.json (the record-path exposure-gate constant).

#include <set>
#include <vector>

#include "composing/analyzed_section.h"
#include "engraving/types/fraction.h"

namespace mu::engraving {
class Score;
}

namespace mu::composing::analysis::joint {
struct NotationRecord;
struct RecordSegment;
}

namespace mu::composing::analysis {

/// One committed record segment -> its ChordAnalysisResult (the committed reading's identity +
/// function), derived from the segment's published facts (§3.2). This is the ONE record-segment ->
/// ChordAnalysisResult converter (#6): analyzeSectionFromRecord uses it for every region, and the
/// presentation layer reads its result to render the DISPLAY chord symbol / Nashville number (the
/// ratified D2 / §3.3-amendment presentation derivations — ChordSymbolFormatter::formatSymbol /
/// formatNashvilleNumber). It carries the CLASS quality's seventh-ness into the extensions bitmask
/// (the coarse ChordQuality alone drops it), so the formatter renders "G7"/"GMaj7"/"Am7"/"Bdim7"
/// rather than the bare triad. `committedContentScore` seeds identity.score (the status-bar
/// "(%.2f)" suffix, CSV row 37); 0 when the segment's slice is absent. Pure — reads only `seg`.
ChordAnalysisResult chordResultFromRecordSegment(const mu::composing::analysis::joint::RecordSegment& seg,
                                                 double committedContentScore = 0.0);

/// The record-path analyzeSection: derive AnalyzedSection for [from, to) from the joint estimator's
/// notation record `rec` (produced by joint::produceNotationRecord). `sc`/`excludeStaves` are used
/// ONLY to re-collect each segment's sounding tones over its span from the L1 note surface (the
/// tones the record does not carry). Returns an empty section when `sc` is null or `to <= from`.
///
/// Each record segment becomes one AnalyzedRegion: the committed reading + derived facts from the
/// record's published fields (root/quality/bass/degree/diatonicToKey/spellings), key/mode as the C1
/// two-mode (Ionian/Aeolian) key with the RAW §3.3 key-axis gap (nats) in normalizedConfidence (no
/// [0,1] remap), hasAssertiveExposure from `gap >= the P1 assertive constant`, tones re-collected
/// over the span, and alternatives from the §3.3 chord-axis slice. Key areas via groupKeyAreas (the
/// shared helper). The pedal-point fact is NOT emitted (it suspends on the record path — OI-194).
AnalyzedSection analyzeSectionFromRecord(const mu::engraving::Score* sc,
                                         const mu::engraving::Fraction& from,
                                         const mu::engraving::Fraction& to,
                                         const std::set<size_t>& excludeStaves,
                                         const mu::composing::analysis::joint::NotationRecord& rec);

} // namespace mu::composing::analysis
