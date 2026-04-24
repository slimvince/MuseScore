/*
 * SPDX-License-Identifier: GPL-3.0-only
 * MuseScore-Studio-CLA-applies
 *
 * MuseScore Studio
 * Music Composition & Notation
 *
 * Copyright (C) 2021 MuseScore Limited
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

// ── Notation ↔ Composing analysis bridge — public declarations ───────────────
//
// All bridge functions live in the mu::notation namespace.  Their
// implementations are in notation/internal/notationcomposingbridge.cpp,
// the only file where both engraving model types and composing analysis
// types are available together.
//
// Callers outside the notation module should include this header rather
// than calling composing functions directly.

#include <set>
#include <string>
#include <vector>

#include "composing/analysis/chord/chordanalyzer.h"   // ChordAnalysisResult, KeyMode, ChordAnalysisTone
#include "composing/analysis/region/harmonicrhythm.h"  // HarmonicRegion

namespace mu::engraving {
class Note;
class Rest;
class Score;
class Segment;
class Fraction;
}

namespace mu::notation {

enum class HarmonicRegionGranularity {
    Smoothed,
    PreserveAllChanges,
};

struct NoteHarmonicContext {
    std::vector<mu::composing::analysis::ChordAnalysisResult> chordResults;
    int keyFifths = 0;
    mu::composing::analysis::KeySigMode keyMode = mu::composing::analysis::KeySigMode::Ionian;
    double keyConfidence = 0.0;

    /// True when the result was produced by the regional (P3) path.  False when
    /// analyzeHarmonicContextAtTick fell back to the tick-local (P4) path because
    /// regional analysis produced no result.  Lets callers (and snapshot tests)
    /// observe Divergence A between the two paths.
    bool wasRegional = true;
};

/// Computes the harmonic annotation string appended to the status bar when a
/// note is selected.  Returns "[Key] Sym [Roman] (score) | ..." or "" if no
/// analysis is possible.
std::string harmonicAnnotation(const mu::engraving::Note* note);

/// Extract pitch context from a note and run harmonic analysis, preferring the
/// same regional accumulation path used by chord-track population when enabled.
NoteHarmonicContext analyzeNoteHarmonicContextDetails(const mu::engraving::Note* note);

/// Same as analyzeNoteHarmonicContextDetails but takes a Rest — infers the
/// prevailing harmony at the rest's tick position from surrounding note content.
NoteHarmonicContext analyzeRestHarmonicContextDetails(const mu::engraving::Rest* rest);

/// Run the same user-facing harmonic inference used by note context at an
/// arbitrary score tick. The implementation expands a bounded local window only
/// until the displayed harmonic result stabilizes.
NoteHarmonicContext analyzeHarmonicContextAtTick(const mu::engraving::Score* score,
                                                 const mu::engraving::Fraction& tick,
                                                 size_t preferredStaffIdx = 0,
                                                 const std::set<size_t>& excludeStaves = {});

/// Tick-local (P4) harmonic analysis — the fallback path used by
/// analyzeHarmonicContextAtTick when regional (P3) analysis produces no
/// result.  Exposed so the pipeline snapshot harness can pin tick-local
/// output directly (Divergence A observability).  Callers must pre-resolve
/// the anchor segment and reference staff; see analyzeHarmonicContextAtTick
/// for the canonical resolution.
NoteHarmonicContext analyzeHarmonicContextLocallyAtTick(
    const mu::engraving::Score* sc,
    const mu::engraving::Fraction& tick,
    const mu::engraving::Segment* seg,
    size_t refStaff,
    const std::set<size_t>& excludeStaves = {});

/// Extract pitch context from a note and run harmonic analysis.
/// Returns up to 3 ranked ChordAnalysisResult candidates (empty = insufficient data).
/// Populates outKeyFifths and outKeyMode for use with ChordSymbolFormatter.
std::vector<mu::composing::analysis::ChordAnalysisResult>
analyzeNoteHarmonicContext(const mu::engraving::Note* note,
                           int& outKeyFifths,
                           mu::composing::analysis::KeySigMode& outKeyMode);

/// Scan a time range across all eligible staves, detect harmonic boundaries,
/// run chord analysis at each boundary, and collapse consecutive same-chord
/// regions.  Returns the sequence of harmonic regions, or empty if no data.
std::vector<mu::composing::analysis::HarmonicRegion> analyzeHarmonicRhythm(
    const mu::engraving::Score* score,
    const mu::engraving::Fraction& startTick,
    const mu::engraving::Fraction& endTick,
    const std::set<size_t>& excludeStaves = {},
    HarmonicRegionGranularity granularity = HarmonicRegionGranularity::Smoothed);

/// Analyse the current selection range, compute harmonic regions, and write
/// Harmony elements (chord symbols / Roman numerals / Nashville numbers) as
/// an undoable command.  Applies chord-track priority: if any selected staff
/// is a chord track staff, annotations are written only to those staves.
/// Regions shorter than the minimumDisplayDurationBeats preference are skipped.
void addHarmonicAnnotationsToSelection(mu::engraving::Score* score,
                                       bool writeChordSymbols,
                                       bool writeRomanNumerals,
                                       bool writeNashvilleNumbers);

/// Formatted presentation strings for a chord analysis result.
struct FormattedChordResult {
    std::string symbol;
    std::string roman;
    std::string nashville;
};

/// Shared formatter for chord-result presentation. Used by both the region
/// annotation path (addHarmonicAnnotationsToSelection) and the per-note UI
/// path (NotationInteraction::addAnalyzedHarmonyToSelection).
/// Honors scoreNoteSpelling via the ChordSymbolFormatter.
FormattedChordResult formatChordResultForStatusBar(
    const mu::engraving::Score* sc,
    const mu::composing::analysis::ChordAnalysisResult& result,
    int keyFifths);

/// Returns the set of staff indices that are chord-track staves in sc.
/// These staves should be excluded from annotation OUTPUT on the per-note path
/// (the region path handles them via chord-track priority).
std::set<size_t> chordTrackExcludeStaves(const mu::engraving::Score* sc);

} // namespace mu::notation
