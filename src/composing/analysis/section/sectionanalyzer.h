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

// ── composing/analysis/section/sectionanalyzer ───────────────────────────────
//
// Unified section-level analysis: the canonical analyzeSection() entry point
// plus key/mode stabilization and cadence / pivot detection.  Moved here from
// notation/internal/notationcomposingbridgehelpers.cpp in Stage 2.1 (Phase 4c)
// so the analysis layer lives in the composing module rather than the notation
// bridge (Dependency Rule §3.3; docs/implementation_roadmap.md Stage 2.1).
//
// Pass 0 (boundary detection) is NOT performed here.  The caller supplies the
// raw HarmonicRegion stream — produced by the notation-side analyzeHarmonicRhythm
// wrapper, which reads IComposingAnalysisConfiguration and wires the debug
// capture hook — and injects it as `rawRegions`.  This keeps composing_analysis
// independent of the notation module and of the configuration / IoC layer:
// analyzeSection consumes the regions and performs Passes 1–4 + key-area
// grouping.

#include <set>
#include <string>
#include <vector>

#include "composing/analysis/chord/chordanalyzer.h"
#include "composing/analysis/key/keymodeanalyzer.h"
#include "composing/analysis/region/harmonicrhythm.h"
#include "composing/analyzed_section.h"
#include "engraving/types/fraction.h"

namespace mu::engraving {
class Score;
}

namespace mu::composing::analysis {

/// Canonical entry point for the unified analysis pipeline.  Runs the
/// smoothed region analysis, fills leading sparse gaps conservatively, and
/// stabilizes key/mode so Roman numerals remain consistent across display
/// paths, producing the shared-output types
/// (`AnalyzedRegion` / `KeyArea` / `AnalyzedSection`).
///
/// `rawRegions` is the Pass-0 boundary stream for [from, to) — the caller
/// obtains it from notation::analyzeHarmonicRhythm (Smoothed granularity) and
/// injects it here so this module stays free of the notation / configuration
/// layers.
///
/// `chordPrefs` is the chord-analyzer preference set applied to gap-region
/// inference (Pass 1).  The notation/implode/snapshot callers leave it at the
/// default, matching the Pass-0 prefs the live bridge already uses
/// (kDefaultChordAnalyzerPreferences) — so threading it is byte-identical on
/// every live path.  Only the batch `--section-level` diagnostic supplies a
/// preset here, so its gap analysis matches its (preset) Pass-0 stream instead
/// of silently falling back to defaults (Stage 2.4, D-GAP).
AnalyzedSection
analyzeSection(const mu::engraving::Score* sc,
               const mu::engraving::Fraction& from,
               const mu::engraving::Fraction& to,
               const std::set<size_t>& excludeStaves,
               const std::vector<HarmonicRegion>& rawRegions,
               const ChordAnalyzerPreferences& chordPrefs = kDefaultChordAnalyzerPreferences);

// ── Cadence and pivot detection ───────────────────────────────────────────────

/// Minimum normalized key confidence required for cadence or pivot detection.
/// Matches kAssertiveKeyExposureThreshold used by populateChordTrack.
inline constexpr double kAnnotateKeyConfidenceThreshold = 0.8;

/// Maximum number of lookahead regions (past the selection boundary) examined
/// when trying to confirm that a candidate pivot chord's new key is stable.
inline constexpr int kMaxPivotLookaheadRegions = 8;

/// A cadence label ("PAC", "PC", "DC", "HC") at a score tick.
struct CadenceMarker {
    int tick;
    std::string label;
};

/// A pivot chord label ("vi → ii" etc.) at a score tick.
struct PivotLabel {
    int tick;
    std::string label;
};

/// Returns true if the key mode result meets the assertive confidence threshold
/// used for cadence and pivot detection.
bool hasAssertiveKeyConfidence(
    const mu::composing::analysis::KeyModeAnalysisResult& kmr);

/// Detect cadence markers from an ordered sequence of analyzed regions.
///
/// @param regions        All regions, including any read-only lookahead regions
///                       past the selection boundary.
/// @param selectionCount First N elements of regions[] are inside the user's
///                       selection; elements at index N and above are lookahead.
///
/// PAC/PC/DC labels are placed at the resolution chord's tick. When the
/// resolution chord is in the lookahead (outside the selection), the label is
/// placed at the preparatory chord (last in-selection region) instead, so that
/// every returned tick falls inside the selection.
///
/// HC is emitted when the last in-selection region is a dominant (degree 4).
std::vector<CadenceMarker> detectCadences(
    const std::vector<mu::composing::analysis::AnalyzedRegion>& regions,
    size_t selectionCount);

/// Detect pivot chord labels from an ordered sequence of analyzed regions.
///
/// The pivot is the most recent in-selection chord that is diatonic to the
/// outgoing key AND whose root also belongs to the incoming key's scale.
/// Its label has the form "vi → ii" (outgoing Roman → incoming Roman).
///
/// @param regions        All regions including lookahead.
/// @param selectionCount Index of first lookahead region (0 = no in-selection
///                       regions; equal to regions.size() = no lookahead).
///
/// If the incoming key cannot be confirmed by an assertive region within
/// kMaxPivotLookaheadRegions past the boundary, the pivot label is suppressed
/// to avoid false positives.
std::vector<PivotLabel> detectPivotChords(
    const std::vector<mu::composing::analysis::AnalyzedRegion>& regions,
    size_t selectionCount);

} // namespace mu::composing::analysis
