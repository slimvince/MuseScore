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

// ── analyzeHarmonicRhythm — thin notation wrapper ────────────────────────────
//
// Phase 4 of the duplication remediation (docs/duplication_audit.md §§2.14, 5.4)
// moved the per-region pipeline body into
// `composing/analysis/region/regionanalyzer.{h,cpp}`.  This file now adapts
// the notation-side configuration (IComposingAnalysisConfiguration prefs,
// thread-local HarmonicRegionDebugCapture) into a call into
// `mu::composing::analysis::region::analyzeRegions()`.

#include "notationcomposingbridge.h"
#include "notationanalysisinternal.h"
#include "notationcomposingbridgehelpers.h"

#include <set>
#include <vector>

#include "composing/analysis/chord/chordanalyzer.h"
#include "composing/analysis/region/harmonicrhythm.h"
#include "composing/analysis/region/regionanalyzer.h"
#include "composing/icomposinganalysisconfiguration.h"
#include "modularity/ioc.h"

namespace mu::notation {

namespace cra = mu::composing::analysis::region;

namespace {

thread_local internal::HarmonicRegionDebugCapture* s_harmonicRegionDebugCapture = nullptr;

}

namespace internal {

void setHarmonicRegionDebugCapture(HarmonicRegionDebugCapture* capture)
{
    s_harmonicRegionDebugCapture = capture;
}

HarmonicRegionDebugCapture* harmonicRegionDebugCapture()
{
    return s_harmonicRegionDebugCapture;
}

} // namespace internal

std::vector<mu::composing::analysis::HarmonicRegion> analyzeHarmonicRhythm(
    const mu::engraving::Score* score,
    const mu::engraving::Fraction& startTick,
    const mu::engraving::Fraction& endTick,
    const std::set<size_t>& excludeStaves,
    HarmonicRegionGranularity granularity)
{
    using namespace mu::composing::analysis;

    if (!score || endTick <= startTick) {
        return {};
    }

    // ── Read live notation-side configuration ────────────────────────────────
    static muse::GlobalInject<mu::composing::IComposingAnalysisConfiguration> composingConfig;
    const auto* cfg = composingConfig.get().get();
    const double onsetThreshold = (cfg != nullptr) ? cfg->onsetBoundaryThreshold() : 0.25;

    // Bridge uses default chord-analyzer prefs at scoring time but admits
    // sparse 1-2 PC slices in Pass 1 (Iter 75) — passed to analyzeRegions via
    // opts.pass1MinDistinctPcsForCandidate.
    KeyModeAnalyzerPreferences keyPrefs;
    if (cfg) {
        keyPrefs.modePriorIonian        = cfg->modePriorIonian();
        keyPrefs.modePriorDorian        = cfg->modePriorDorian();
        keyPrefs.modePriorPhrygian      = cfg->modePriorPhrygian();
        keyPrefs.modePriorLydian        = cfg->modePriorLydian();
        keyPrefs.modePriorMixolydian    = cfg->modePriorMixolydian();
        keyPrefs.modePriorAeolian       = cfg->modePriorAeolian();
        keyPrefs.modePriorLocrian       = cfg->modePriorLocrian();
        keyPrefs.modePriorMelodicMinor  = cfg->modePriorMelodicMinor();
        keyPrefs.modePriorDorianB2      = cfg->modePriorDorianB2();
        keyPrefs.modePriorLydianAugmented = cfg->modePriorLydianAugmented();
        keyPrefs.modePriorLydianDominant  = cfg->modePriorLydianDominant();
        keyPrefs.modePriorMixolydianB6  = cfg->modePriorMixolydianB6();
        keyPrefs.modePriorAeolianB5     = cfg->modePriorAeolianB5();
        keyPrefs.modePriorAltered       = cfg->modePriorAltered();
        keyPrefs.modePriorHarmonicMinor = cfg->modePriorHarmonicMinor();
        keyPrefs.modePriorLocrianSharp6 = cfg->modePriorLocrianSharp6();
        keyPrefs.modePriorIonianSharp5  = cfg->modePriorIonianSharp5();
        keyPrefs.modePriorDorianSharp4  = cfg->modePriorDorianSharp4();
        keyPrefs.modePriorPhrygianDominant = cfg->modePriorPhrygianDominant();
        keyPrefs.modePriorLydianSharp2  = cfg->modePriorLydianSharp2();
        keyPrefs.modePriorAlteredDomBB7 = cfg->modePriorAlteredDomBB7();
    }

    // ── Build options and forward to the shared orchestrator ────────────────
    cra::AnalyzeRegionsOptions opts;
    opts.granularity                   = granularity;
    opts.onsetBoundaryThreshold        = onsetThreshold;
    opts.excludeLookAheadOnDenseStart  = false;
    opts.pass1MinDistinctPcsForCandidate = 1;  // Iter 75 sparse-texture admission

    // Notation-specific debug-capture wiring.
    cra::RegionAnalysisHooks hooks;
    auto* debugCapture = internal::harmonicRegionDebugCapture();
    if (debugCapture) {
        hooks.preMergeRegions  = debugCapture->preMergeRegions;
        hooks.postMergeRegions = debugCapture->postMergeRegions;
        opts.hooks = &hooks;
    }

    return cra::analyzeRegions(
        score, startTick, endTick, excludeStaves,
        kDefaultChordAnalyzerPreferences, keyPrefs, opts);
}

} // namespace mu::notation
