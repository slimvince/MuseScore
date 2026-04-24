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

// ── Shared analysis output for the unified pipeline (Phase 2) ────────────────
//
// These are the structured types produced by the future `analyzeSection()`
// entry point and consumed by the three regional emitters (implode,
// annotation, tick-regional).  Introduced in Phase 2 with no call sites yet;
// Phase 3a/3b/3c wire each emitter over.
//
// Design contract (docs/unified_analysis_pipeline.md):
//   • Tick values are stored as raw integers — same convention as
//     `HarmonicRegion` — so this header stays free of the engraving Fraction
//     include and composing_analysis keeps its independence from engraving.
//   • No emitter-specific fields.  If a value is only read by the implode
//     chord-track writer (voicing choice), the annotation writer (text
//     format), or the status-bar formatter, it belongs on the emitter-side
//     options struct, not here.
//   • `ChordTemporalExtensions` will be added in Phase 3c when divergence D
//     is closed.  See the "ChordTemporalContext audit (Phase 2)" section of
//     docs/unified_analysis_pipeline.md for the migration candidates.

#include <vector>

#include "analysis/chord/chordanalyzer.h"
#include "analysis/key/keymodeanalyzer.h"

namespace mu::composing::analysis {

/// One harmonic region in the analysed score — the Phase 2 type that will
/// replace `HarmonicRegion` as the shared analysis-result payload across all
/// three regional paths.  Phase 2 keeps `HarmonicRegion` in place;
/// `analyzeSection()` produces `AnalyzedRegion` by one-to-one translation.
struct AnalyzedRegion {
    /// First tick of this region (raw tick integer; convert with
    /// Fraction::fromTicks()).
    int startTick = 0;

    /// First tick of the next region (exclusive).
    int endTick = 0;

    /// Root, quality, extensions, and tonal-function payload for this region.
    ChordAnalysisResult chordResult;

    /// False when the per-region note set was too sparse to produce a
    /// confident chord-analyzer candidate; the bridge may have inferred a
    /// sparse/gap-tone result instead.
    bool hasAnalyzedChord = true;

    /// Key and mode context for this region.  Informs the `KeyArea` that
    /// encloses this region and the Roman numeral / Nashville number
    /// emitters.
    KeyModeAnalysisResult keyModeResult;

    /// The sounding tones that produced `chordResult`.  Emitters that need
    /// to re-examine the pitch content (e.g. the implode voicing builder)
    /// read this directly.
    std::vector<ChordAnalysisTone> tones;

    /// True when the enclosing key context was confirmed with assertive
    /// confidence (`kAssertiveKeyExposureThreshold = 0.8`, shared with
    /// cadence / pivot detection).  Promoted from implode-internal state
    /// so annotation and tick-regional paths can gate on the same flag.
    bool hasAssertiveExposure = false;

    /// Index into `AnalyzedSection::keyAreas` identifying the key-area span
    /// that contains this region.  -1 when the region was built without a
    /// surrounding `AnalyzedSection` (e.g. unit tests that construct an
    /// `AnalyzedRegion` in isolation).
    int keyAreaId = -1;
};

/// A contiguous span of regions sharing a key signature and mode.  Adjacent
/// `KeyArea` entries with different (keyFifths, mode) mark a modulation
/// boundary — this is the first-class output that Phase 5's modulation-aware
/// Roman numeral annotation will consume.
struct KeyArea {
    /// First tick of the span (= startTick of the first region).
    int startTick = 0;

    /// First tick after the span (exclusive; = endTick of the last region).
    int endTick = 0;

    /// Key signature in the -7..+7 Ionian convention shared with
    /// `KeyModeAnalysisResult`.
    int keyFifths = 0;

    /// Detected mode (Ionian, Aeolian, Dorian, etc.).
    KeySigMode mode = KeySigMode::Ionian;

    /// Confidence score of this key-area.  Phase 2 seeds it with the
    /// maximum `normalizedConfidence` across the collapsed regions so a
    /// single low-confidence region does not mask a strongly-exposed span.
    /// Phase 5 may replace this with a dedicated area-level confidence.
    double confidence = 0.0;
};

/// The full analysis result for one call to `analyzeSection()`: the flat
/// sequence of regions covering `[startTick, endTick)`, plus the derived
/// key-area grouping.  `regions[i].keyAreaId` indexes into `keyAreas`.
struct AnalyzedSection {
    /// First tick of the analysed window (raw tick integer).
    int startTick = 0;

    /// First tick after the analysed window (exclusive).
    int endTick = 0;

    /// Regions in ascending order of `startTick`.
    std::vector<AnalyzedRegion> regions;

    /// Key-areas in ascending order of `startTick`, covering the same
    /// tick span as `regions`.  Always non-empty when `regions` is
    /// non-empty.
    std::vector<KeyArea> keyAreas;
};

} // namespace mu::composing::analysis
