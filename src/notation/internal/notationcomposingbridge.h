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

#include <optional>
#include <set>
#include <string>
#include <vector>

#include "composing/analyzed_section.h"               // KeyArea
#include "composing/analysis/chord/chordanalyzer.h"   // ChordAnalysisResult, KeyMode, ChordAnalysisTone
#include "composing/analysis/region/harmonicrhythm.h"  // HarmonicRegion
#include "composing/analysis/region/regionanalyzer.h"  // HarmonicRegionGranularity (Phase 4)

namespace mu::engraving {
class Note;
class Rest;
class Score;
class Segment;
class Fraction;
}

namespace mu::notation {

/// Phase 4 (docs/duplication_audit.md §5.4): the canonical definition now
/// lives in composing/analysis/region/regionanalyzer.h.  The using-alias keeps
/// existing notation-side callers source-compatible.
using HarmonicRegionGranularity = mu::composing::analysis::HarmonicRegionGranularity;

struct NoteHarmonicContext {
    std::vector<mu::composing::analysis::ChordAnalysisResult> chordResults;
    int keyFifths = 0;
    mu::composing::analysis::KeySigMode keyMode = mu::composing::analysis::KeySigMode::Ionian;
    double keyConfidence = 0.0;

    /// Snapshot of the per-region temporal context that produced
    /// `chordResults[0]`.  Populated on the regional (P3) path; left at
    /// defaults on the tick-local (P4) fallback (which has no per-region
    /// concept).  Phase 3c surface for emitter and snapshot consumers
    /// (closes divergence D — was previously re-derived via per-tick
    /// `findTemporalContext`).
    mu::composing::analysis::ChordTemporalExtensions temporalExtensions;

    /// True when the result was produced by the regional (P3) path.  False when
    /// analyzeHarmonicContextAtTick fell back to the tick-local (P4) path because
    /// regional analysis produced no result.  Lets callers (and snapshot tests)
    /// observe Divergence A between the two paths.
    bool wasRegional = true;

    /// The key-area span enclosing this note's region.  Populated on the P3 path
    /// from the matched region's keyAreaId; left as nullopt on the P4 fallback
    /// (which has no region/section concept — graceful degradation per recon Q3).
    /// Phase 5b: status-bar and right-click menu can surface both the per-region
    /// key (keyFifths/keyMode) and the enclosing structural key area.
    std::optional<mu::composing::analysis::KeyArea> enclosingKeyArea;
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

/// Flush the bounded-window decode cache. Called by Notation::setScore() on every
/// score install to close the pointer-reuse hazard: the cache keys on a raw Score*
/// (no per-lifetime id exists in engraving), so a freed-then-reallocated score at the
/// same address could otherwise false-hit. Every score the cache is queried with is
/// installed via setScore first, so flushing there drops any stale entry before a
/// reused-address score can be queried.
void clearHarmonicDecodeCache();

// ── Stage 3.1b bounded-window cache byte-identity A/B + instrumentation ───────
//
// NOT the production status-bar path (that is analyzeHarmonicContextAtTick above,
// which now memoizes its per-window section build). These exist for the byte-identity
// A/B and the decode-cache tests.

/// The IDENTICAL expanding-window orchestrator with the window cache BYPASSED
/// (every window section rebuilt fresh) — the "uncached" reference for the
/// byte-identity A/B, which must show ZERO differing ticks vs the cached path.
NoteHarmonicContext analyzeHarmonicContextAtTickUncachedForTesting(const mu::engraving::Score* score,
                                                                   const mu::engraving::Fraction& tick,
                                                                   size_t preferredStaffIdx = 0,
                                                                   const std::set<size_t>& excludeStaves = {});

/// Drop the bounded-window decode cache (MRU of per-window sections).  Test-only.
void clearHarmonicDecodeCacheForTesting();

/// Number of cold window-section builds in the decode cache this process.
/// Test-only — lets cache tests assert hit/miss behaviour.
size_t harmonicDecodeCacheBuildCountForTesting();

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
