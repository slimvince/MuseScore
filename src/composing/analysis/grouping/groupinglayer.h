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

// ── composing/analysis/grouping — Architectural Layer 6 (GROUPING) ────────────
//
// Spec: cowork_layer6_grouping_design.md (SIGNED 2026-07-02) §5.1–§5.5, §3 (the
// I/O contract), §6 (the proportionality bound), §8 (the L5-override/L6-merge
// division). Oracle baselines: cc_tsv_oracle_report.md.
//
// GROUPING IS ASSEMBLY, NOT DETECTION (§1/§6). Every signal L6 needs was already
// produced upstream — the punctuation-span boundaries (Layer 1.5 phrase-boundary
// primitive), the cadences and Roman numerals (Layer 5), the local keys (Layer 3,
// carried per unit by Layer 5). L6 ASSEMBLES these into the flat grouping
// structure the ground truth annotates: punctuation-spans, key-areas, and the
// alignment of cadences to punctuation-span endings. It detects nothing new and
// re-derives nothing; it changes NO Roman numeral, key, or cadence — it organises
// them (§7 additive, read-only over Layer 5). The §6 proportionality bound is a
// BUILD RULE: L6 is exactly its §5.1–§5.3 assembly + the §5.4/§5.5 read-through
// carries — any threshold / merge / re-decision NOT in §5.1–§5.5 is out of scope.
//
// PRODUCER-AGNOSTIC POD VIEWS (the established L5-unit pattern — functionoutput.h /
// functioncadence.h). L6 reads only the small POD views below; at engage each is
// mapped from the real producers (the L5 FunctionLayerOutput per-unit stream + the
// per-unit local-key track, the L1.5 PhraseBoundaryProfile picked set + strengths +
// provenance, the L5 FunctionalCadence stream, and the analysed-span selection
// edges), and the tests inject by hand. The module compiles free of the decoder /
// region / engraving headers.
//
// DORMANT (§10 tail): NO production consumer — nothing in src/ calls
// assembleGrouping(); it is exercised only by grouping_tests.cpp. Byte-identical on
// production by construction; the scattered live grouping paths it will retire at
// engagement (§4/§7 "Reuse, do not duplicate") are detectCadences() /
// detectPivotChords() (section/sectioncadencedetection.cpp) and the KeyArea grouping
// in analyzeSection() (analyzed_section.h / section/sectionanalyzer.cpp) — NAMED
// here, touched nowhere; their retirement is the joint engagement (deferred).
//
// CONSTANTS ARE PRECISION-PHASE (the firewall, §7). The alignment window, the
// §5.1-a codetta closeness window + strength margin, and the key-area confidence
// combiner shape are DECLARED DEFAULTS, NOT tuned for accuracy. The codetta window
// DEFAULTS TO 0 (inert): with no refinement the punctuation-span boundaries are the
// L1.5 picked set verbatim, so the §10 boundary oracle equals the L1.5 baseline by
// construction (L6 adds no detection). This file fixes the RULES and their
// DIRECTION, not the numbers.

#include <string>
#include <vector>

#include "composing/analysis/function/functioncadence.h"  // FunctionalCadence (read verbatim, §5.0)

namespace mu::composing::analysis::grouping {

// ── §3 boundary provenance (carried from the Layer-1.5 primitive, never computed) ─
//
// The cue KIND that fired a boundary and its SCOPE (global/system-wide vs per-part).
// Carrying the scope is what keeps the annotation from silently presenting a LOCAL
// boundary (one part's breath) as a GLOBAL one (a double barline) — §3. The current
// primitive does not yet expose per-tick cue/scope, so these default to Unknown and
// are carried through; populating them is an engage-time primitive enhancement.
enum class BoundaryCue { Unknown, Fermata, Breath, Barline, KeySignature, Tempo, Rest, SurfacePeak };
enum class BoundaryScope { Unknown, Global, PerPart };

// ── §3/§5.1 input: one picked phrase boundary (the Layer-1.5 picked-peak set) ──────
//
// L6 consumes the primitive's picked set AS-IS — it does not re-threshold or
// re-detect boundaries (§5.1). Tick + its texture strength (for the §5.1-a codetta
// refinement) + provenance.
struct BoundaryInput {
    int tick = 0;
    double strength = 0.0;          ///< §4.4 texture strength at the picked tick (codetta margin input)
    BoundaryCue cue = BoundaryCue::Unknown;
    BoundaryScope scope = BoundaryScope::Unknown;
};

// ── §3/§5.2/§5.4 input: one analysis unit's grouping-relevant carry ────────────────
//
// The per-unit local-key track (§5.2, sub-punctuation-span granularity — a key
// change may fall mid-span, §9-D5) + the honest Layer-5 residual (§5.4). Carried,
// never re-decided.
struct GroupingUnit {
    int startTick = 0;
    int endTick = 0;

    int localTonicPc = -1;          ///< the unit's local key tonic (Layers 3/5 carry)
    bool localMinorMode = false;

    /// The unit's DECLARED boundary key confidence ∈ [0,1] (confidence contract U2 —
    /// the one declared L3/L5 number, not the diagnostic sigmoid). The §5.2 key-area
    /// confidence combiner reads this; expected already in [0,1] (clamped defensively).
    double keyConfidence = 0.0;

    bool openMark = false;          ///< §5.4 Layer-5 honest residual — surfaced, NEVER resolved here
};

// ── §5.1-amendment input: the analysed-span selection edges ────────────────────────
//
// The domain L6 groups over, plus whether each edge is an ARTIFICIAL selection clip
// (mid-piece) or the TRUE score edge. An edge group whose opening/closing tick is a
// SELECTION edge (not a musical boundary and not the true score edge) carries the
// `clipped-by-selection-edge` provenance; the same distinction L2's artificial-clip
// boundary and the bounded-context design draw. A true score start/end is NOT clipped.
struct AnalyzedSpan {
    int startTick = 0;
    int endTick = 0;
    bool startIsSelectionEdge = false;  ///< true = artificial clip at start; false = true score start
    bool endIsSelectionEdge = false;    ///< true = artificial clip at end;   false = true score end
};

// ── The firewall constants (§7 — DECLARED DEFAULTS, NOT tuned) ─────────────────────
struct GroupingParams {
    /// §5.3 cadence-to-boundary alignment window (ticks): a cadence closes a span
    /// whose ending boundary lies at the arrival tick or within this window AFTER it
    /// (the arrival may slightly precede the notated span end). Declared default: one
    /// quarter-note beat (480t) — the notation-alignment slack, matching the oracle
    /// tolerance. NOT tuned; existence fixed by §5.3, width precision-phase.
    int alignmentWindowTicks = 480;

    /// §5.1-a codetta closeness window (ticks). Two boundaries within this window,
    /// strong-then-weak, trigger the codetta refinement. DEFAULT 0 = INERT (no two
    /// distinct ticks are within 0), so the base flat partition uses the L1.5 picked
    /// set verbatim — the boundary oracle equals the L1.5 baseline by construction.
    int codettaWindowTicks = 0;

    /// §5.1-a strength margin: the earlier peak is the structural end only when its
    /// strength exceeds the later peak's by at least this margin (strong-then-weak).
    /// Default 0 (any strict excess). Precision-phase.
    double codettaStrengthMargin = 0.0;
};

/// Global default grouping parameters.
inline constexpr GroupingParams kDefaultGroupingParams{};

// ── §3 outputs — the flat grouping structure (additive, read-only over Layer 5) ────

/// §5.1 one punctuation-span: a `[startTick, endTick)` flat span between two adjacent
/// boundaries, carrying its units, the opening/closing boundary provenance, the
/// closing cadence (if any), the §5.1-amendment edge marks, and the §5.4 residual.
struct PunctuationSpan {
    int startTick = 0;
    int endTick = 0;                ///< the span's end (its codetta, if any, extends past structuralEndTick)

    int firstUnit = -1;            ///< index range [firstUnit, lastUnit] into the units stream (-1 = none)
    int lastUnit = -1;

    // Opening/closing boundary provenance (§3), carried from the L1.5 picked set.
    BoundaryCue openCue = BoundaryCue::Unknown;
    BoundaryScope openScope = BoundaryScope::Unknown;
    double openStrength = 0.0;
    BoundaryCue closeCue = BoundaryCue::Unknown;
    BoundaryScope closeScope = BoundaryScope::Unknown;
    double closeStrength = 0.0;

    int closingCadenceIndex = -1;  ///< §5.3 index into the cadence stream, or -1 (ends without a cadence)

    // §5.1-amendment (user-ratified 2026-07-02).
    bool clippedAtStart = false;   ///< opening tick is a selection edge, not a musical boundary
    bool clippedAtEnd = false;     ///< closing tick is a selection edge, not a musical boundary
    bool extensionCue = false;     ///< reaches a selection END edge with NO closing boundary and NO cadence

    bool carriesOpenMark = false;  ///< §5.4 contains a Layer-5 open mark

    // §5.1-a codetta refinement (default-inert). structuralEndTick == endTick when no
    // refinement fired; otherwise structuralEndTick is the strong peak (the structural
    // end) and [structuralEndTick, codettaEndTick) is the span's codetta annexe.
    int structuralEndTick = -1;    ///< = endTick unless a codetta refinement fired
    int codettaEndTick = -1;       ///< the codetta's end, or -1 when there is no codetta
};

/// §5.2 one key-area: a maximal `[startTick, endTick)` run of constant local key.
/// An INDEPENDENT flat segmentation — NOT nested in punctuation-spans (§9-D5); a key
/// change may fall mid-punctuation-span.
struct KeyAreaSpan {
    int startTick = 0;
    int endTick = 0;

    int localTonicPc = -1;
    bool localMinorMode = false;

    /// §5.2 U2 boundary confidence ∈ [0,1] (confidence contract, Class-M declared):
    /// the DECLARED default combiner = duration-weighted mean of the area's units'
    /// declared boundary key confidences. NON-INCREASING in the weakest unit's
    /// confidence (direction fixed); the exact combiner is precision-phase.
    double confidence = 0.0;

    int firstUnit = -1;
    int lastUnit = -1;

    bool clippedAtStart = false;
    bool clippedAtEnd = false;
    bool carriesOpenMark = false;  ///< §5.4 contains a Layer-5 open mark
};

/// §5.3 the alignment of one Layer-5 cadence to the punctuation-span structure.
enum class CadenceAlignmentKind {
    ClosesSpan,   ///< the cadence closes a punctuation-span (its arrival aligns the span's ending boundary)
    Internal      ///< mid-span — surfaced as a tension signal, NEVER snapped or discarded (§5.3)
};
struct CadenceAlignment {
    int cadenceIndex = -1;                                  ///< index into the input cadence stream
    CadenceAlignmentKind kind = CadenceAlignmentKind::Internal;
    int punctuationSpanIndex = -1;                          ///< the span it closes (ClosesSpan), else -1
};

/// §5.5 a recognised-schema sequence-span — hosted verbatim from the recognition
/// consumer (cowork_progression_schema_design.md). EMPTY in the dormant state (no
/// consumer); the struct exists so the contract is complete and the empty case asserted.
struct SchemaSpan {
    int startTick = 0;
    int endTick = 0;
    std::string schemaName;        ///< the matched schema (consumer-supplied)
    std::string idiomTag;          ///< style/idiom tag
    double matchScore = 0.0;
};

/// §3 the L6 output — the flat grouping structure (the contract to the display layer).
struct GroupingLayerOutput {
    std::vector<PunctuationSpan> punctuationSpans;   ///< §5.1 the flat partition (tiles the analysed span)
    std::vector<KeyAreaSpan> keyAreas;               ///< §5.2 the independent key-span partition
    std::vector<CadenceAlignment> cadenceAlignments; ///< §5.3 one entry per input cadence
    std::vector<SchemaSpan> schemaSpans;             ///< §5.5 empty absent the recognition consumer
};

// ── The §5 assembly ────────────────────────────────────────────────────────────────

/// Assemble the flat Layer-6 grouping structure (§5.1–§5.5) from the upstream
/// products: the per-unit local-key/residual stream (in tick order), the Layer-1.5
/// picked boundary set, the Layer-5 cadences (read verbatim), and the analysed-span
/// selection edges. Additive and read-only — it changes NO upstream decision. With
/// the default params the punctuation-span boundaries are the L1.5 picked set
/// verbatim (the codetta refinement is inert).
GroupingLayerOutput
assembleGrouping(const std::vector<GroupingUnit>& units,
                 const std::vector<BoundaryInput>& boundaries,
                 const std::vector<FunctionalCadence>& cadences,
                 const AnalyzedSpan& span,
                 const GroupingParams& params = kDefaultGroupingParams);

} // namespace mu::composing::analysis::grouping
