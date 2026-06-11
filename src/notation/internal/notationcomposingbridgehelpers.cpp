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

// ── Shared bridge helpers ────────────────────────────────────────────────────
//
// File-local utilities shared by:
//   • notationcomposingbridge.cpp  — harmonicAnnotation, analyzeNoteHarmonicContext
//   • notationharmonicrhythmbridge.cpp — analyzeHarmonicRhythm
//
// Stage 2.1 (Phase 4c) moved the section-level ANALYSIS layer out of this file
// and into the composing module — analyzeSection(), key/mode stabilization, and
// cadence / pivot detection now live in
// composing/analysis/section/sectionanalyzer.{h,cpp} (see
// docs/implementation_roadmap.md Stage 2.1).  What remains here is the
// notation-side adapter surface: scoreNoteSpelling plus the thin pass-throughs
// to the composing engravingbridge / scoreharvest / region / keyresolver layers.

#include "notationcomposingbridgehelpers.h"
#include "notationanalysisinternal.h"
#include "notationcomposingbridge.h"

#include <algorithm>
#include <array>
#include <cmath>
#include <limits>
#include <map>
#include <optional>
#include <set>
#include <tuple>

#include "engraving/dom/chord.h"
#include "engraving/dom/key.h"
#include "engraving/dom/masterscore.h"
#include "engraving/dom/measure.h"
#include "engraving/dom/note.h"
#include "engraving/dom/pedal.h"
#include "engraving/dom/segment.h"
#include "engraving/dom/sig.h"
#include "engraving/dom/staff.h"

#include "composing/analysis/chord/analysisutils.h"
#include "composing/analysis/chord/chordanalyzer.h"
#include "composing/analysis/engravingbridge/regiontonecollector.h"
#include "composing/analysis/key/keymodeanalyzer.h"
#include "composing/analysis/key/keyresolver.h"
#include "composing/analysis/region/sparsechordrefinement.h"
#include "composing/icomposinganalysisconfiguration.h"
#include "modularity/ioc.h"

using mu::composing::analysis::isDiatonicStep;

namespace ebr = mu::composing::analysis::engravingbridge;
namespace kr  = mu::composing::analysis::keyresolver;
namespace cra = mu::composing::analysis::region;

namespace mu::notation::internal {

mu::composing::analysis::ChordSymbolFormatter::NoteSpelling scoreNoteSpelling(
    const mu::engraving::Score* score)
{
    using mu::engraving::NoteSpellingType;
    using mu::engraving::Sid;
    namespace CSF = mu::composing::analysis::ChordSymbolFormatter;

    if (!score) {
        return CSF::NoteSpelling::Standard;
    }
    const auto mStyle = score->style().styleV(Sid::chordSymbolSpelling).value<NoteSpellingType>();
    switch (mStyle) {
    case NoteSpellingType::GERMAN:      return CSF::NoteSpelling::German;
    case NoteSpellingType::GERMAN_PURE: return CSF::NoteSpelling::GermanPure;
    default:                            return CSF::NoteSpelling::Standard;
    }
}

// diatonicDegreeForRootPc, refineSparseChordQualityFromKeyContext,
// applyTonicPriorToSparseChord, and forceChordTrackQualityFromKeyContext
// are thin pass-throughs to the shared composing/analysis/region/sparsechordrefinement
// implementation (Phase 4 — docs/duplication_audit.md §5.4).

int diatonicDegreeForRootPc(int rootPc, int keyFifths, mu::composing::analysis::KeySigMode keyMode)
{
    return cra::diatonicDegreeForRootPc(rootPc, keyFifths, keyMode);
}

void refineSparseChordQualityFromKeyContext(
    mu::composing::analysis::ChordAnalysisResult& result,
    const std::vector<mu::composing::analysis::ChordAnalysisTone>& tones,
    int keyFifths,
    mu::composing::analysis::KeySigMode keyMode)
{
    cra::refineSparseChordQualityFromKeyContext(result, tones, keyFifths, keyMode);
}

void applyTonicPriorToSparseChord(
    mu::composing::analysis::ChordAnalysisResult& result,
    const std::vector<mu::composing::analysis::ChordAnalysisTone>& tones,
    int keyFifths,
    mu::composing::analysis::KeySigMode keyMode)
{
    cra::applyTonicPriorToSparseChord(result, tones, keyFifths, keyMode);
}

void forceChordTrackQualityFromKeyContext(
    mu::composing::analysis::ChordAnalysisResult& result,
    mu::composing::analysis::KeySigMode keyMode)
{
    cra::forceChordTrackQualityFromKeyContext(result, keyMode);
}

// collectSoundingAt and buildTones are exposed via using-declarations in
// notationcomposingbridgehelpers.h — the engravingbridge implementations are
// the only definitions, so there is no separate notation::internal overload
// to confuse argument-dependent lookup.
//
// collectRegionTones, detectOnsetSubBoundaries, detectBassMovementSubBoundaries,
// and findTemporalContext have separate notation::internal entry points so
// existing notation TUs keep their using-declarations; each is a thin
// pass-through to engravingbridge.  See docs/duplication_audit.md §§2.1-2.13.

void resolveKeyAndMode(const mu::engraving::Score* sc,
                       const mu::engraving::Fraction& tick,
                       mu::engraving::staff_idx_t staffIdx,
                       const std::set<size_t>& excludeStaves,
                       int& outKeyFifths,
                       mu::composing::analysis::KeySigMode& outMode,
                       double& outConfidence,
                       const mu::composing::analysis::KeyModeAnalysisResult* prevResult,
                       double* outScore)
{
    using namespace mu::composing::analysis;

    // ── Load analyzer preferences from the bridge config ─────────────────
    // The CLI tool (batch_analyze) configures prefs via --preset; the bridge
    // loads them from IComposingAnalysisConfiguration so the live UI honours
    // the user's mode-prior settings. After loading, resolution itself is
    // identical: delegate to the shared keyresolver.
    KeyModeAnalyzerPreferences prefs;
    {
        static muse::GlobalInject<mu::composing::IComposingAnalysisConfiguration> config;
        const auto* cfg = config.get().get();
        if (cfg) {
            prefs.modePriorIonian     = cfg->modePriorIonian();
            prefs.modePriorDorian     = cfg->modePriorDorian();
            prefs.modePriorPhrygian   = cfg->modePriorPhrygian();
            prefs.modePriorLydian     = cfg->modePriorLydian();
            prefs.modePriorMixolydian = cfg->modePriorMixolydian();
            prefs.modePriorAeolian    = cfg->modePriorAeolian();
            prefs.modePriorLocrian    = cfg->modePriorLocrian();
            prefs.modePriorMelodicMinor  = cfg->modePriorMelodicMinor();
            prefs.modePriorDorianB2      = cfg->modePriorDorianB2();
            prefs.modePriorLydianAugmented = cfg->modePriorLydianAugmented();
            prefs.modePriorLydianDominant  = cfg->modePriorLydianDominant();
            prefs.modePriorMixolydianB6  = cfg->modePriorMixolydianB6();
            prefs.modePriorAeolianB5     = cfg->modePriorAeolianB5();
            prefs.modePriorAltered       = cfg->modePriorAltered();
            prefs.modePriorHarmonicMinor = cfg->modePriorHarmonicMinor();
            prefs.modePriorLocrianSharp6 = cfg->modePriorLocrianSharp6();
            prefs.modePriorIonianSharp5  = cfg->modePriorIonianSharp5();
            prefs.modePriorDorianSharp4  = cfg->modePriorDorianSharp4();
            prefs.modePriorPhrygianDominant = cfg->modePriorPhrygianDominant();
            prefs.modePriorLydianSharp2  = cfg->modePriorLydianSharp2();
            prefs.modePriorAlteredDomBB7 = cfg->modePriorAlteredDomBB7();
        }
    }

    const auto ranked = kr::resolveKeyAndModeRanked(sc, tick, staffIdx,
                                                    excludeStaves, prefs, prevResult);
    // Resolver always returns ≥ 1 result.
    const auto& chosen = ranked.front();
    outKeyFifths  = chosen.keySignatureFifths;
    outMode       = chosen.mode;
    outConfidence = chosen.normalizedConfidence;
    if (outScore) {
        *outScore = chosen.score;
    }
}

std::vector<mu::composing::analysis::ChordAnalysisTone>
collectRegionTones(const mu::engraving::Score* sc,
                   int startTickInt,
                   int endTickInt,
                   const std::set<size_t>& excludeStaves,
                   int parentStartTickInt,
                   bool excludeLookAheadOnDenseStart)
{
    return ebr::collectRegionTones(sc, startTickInt, endTickInt, excludeStaves,
                                   parentStartTickInt, excludeLookAheadOnDenseStart);
}

std::vector<mu::engraving::Fraction>
detectOnsetSubBoundaries(const mu::engraving::Score* sc,
                         const mu::engraving::Fraction& startTick,
                         const mu::engraving::Fraction& endTick,
                         const std::set<size_t>& excludeStaves,
                         double threshold)
{
    return ebr::detectOnsetSubBoundaries(sc, startTick, endTick, excludeStaves, threshold);
}

std::vector<mu::engraving::Fraction>
detectBassMovementSubBoundaries(const mu::engraving::Score* sc,
                                const mu::engraving::Fraction& startTick,
                                const mu::engraving::Fraction& endTick,
                                const std::set<size_t>& excludeStaves,
                                int minGapTicks)
{
    return ebr::detectBassMovementSubBoundaries(sc, startTick, endTick, excludeStaves, minGapTicks);
}

mu::composing::analysis::ChordTemporalContext
findTemporalContext(const mu::engraving::Score* sc,
                    const mu::engraving::Segment* seg,
                    const std::set<size_t>& excludeStaves,
                    int keyFifths,
                    mu::composing::analysis::KeySigMode keyMode,
                    int currentBassPc)
{
    return ebr::findTemporalContext(sc, seg, excludeStaves, keyFifths, keyMode, currentBassPc);
}

} // namespace mu::notation::internal
