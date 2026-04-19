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
class Score;
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
};

/// Computes the harmonic annotation string appended to the status bar when a
/// note is selected.  Returns "[Key] Sym [Roman] (score) | ..." or "" if no
/// analysis is possible.
std::string harmonicAnnotation(const mu::engraving::Note* note);

/// Extract pitch context from a note and run harmonic analysis, preferring the
/// same regional accumulation path used by chord-track population when enabled.
NoteHarmonicContext analyzeNoteHarmonicContextDetails(const mu::engraving::Note* note);

/// Run the same user-facing harmonic inference used by note context at an
/// arbitrary score tick. The implementation expands a bounded local window only
/// until the displayed harmonic result stabilizes.
NoteHarmonicContext analyzeHarmonicContextAtTick(const mu::engraving::Score* score,
                                                 const mu::engraving::Fraction& tick,
                                                 size_t preferredStaffIdx = 0,
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
///
/// When forceClassicalPath is true, the Jazz chord-symbol detection gate is
/// skipped even if the score contains STANDARD Harmony elements.  This prevents
/// the annotation write path from having its boundary detection influenced by
/// previously-written chord symbol annotations (order-of-annotation violation).
std::vector<mu::composing::analysis::HarmonicRegion> analyzeHarmonicRhythm(
    const mu::engraving::Score* score,
    const mu::engraving::Fraction& startTick,
    const mu::engraving::Fraction& endTick,
    const std::set<size_t>& excludeStaves = {},
    HarmonicRegionGranularity granularity = HarmonicRegionGranularity::Smoothed,
    bool forceClassicalPath = false);

/// Analyse the current selection range, compute harmonic regions, and write
/// Harmony elements (chord symbols / Roman numerals / Nashville numbers) as
/// an undoable command.  Applies chord-track priority: if any selected staff
/// is a chord track staff, annotations are written only to those staves.
/// Regions shorter than the minimumDisplayDurationBeats preference are skipped.
void addHarmonicAnnotationsToSelection(mu::engraving::Score* score,
                                       bool writeChordSymbols,
                                       bool writeRomanNumerals,
                                       bool writeNashvilleNumbers);

} // namespace mu::notation
