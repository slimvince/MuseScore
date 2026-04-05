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

#include <string>
#include <vector>
#include "modularity/imoduleinterface.h"
#include "async/notification.h"

namespace mu::composing {

// ── Mode prior preset ────────────────────────────────────────────────────────

/// All 21 mode priors bundled under a display name.
/// The five built-in presets are returned by IComposingAnalysisConfiguration::modePriorPresets().
/// The "Standard" preset matches the compile-time defaults in KeyModeAnalyzerPreferences.
struct ModePriorPreset {
    std::string name;               ///< Display name (e.g. "Standard", "Jazz")

    // Diatonic modes
    double ionian          =  1.20;
    double dorian          = -0.50;
    double phrygian        = -1.50;
    double lydian          = -1.50;
    double mixolydian      = -0.50;
    double aeolian         =  1.00;
    double locrian         = -3.00;

    // Melodic minor family
    double melodicMinor    = -0.50;
    double dorianB2        = -1.50;
    double lydianAugmented = -2.00;
    double lydianDominant  = -1.00;
    double mixolydianB6    = -1.50;
    double aeolianB5       = -2.50;
    double altered         = -3.50;

    // Harmonic minor family
    double harmonicMinor      = -0.30;
    double locrianSharp6      = -2.50;
    double ionianSharp5       = -2.00;
    double dorianSharp4       = -2.00;
    double phrygianDominant   = -0.80;
    double lydianSharp2       = -2.50;
    double alteredDomBB7      = -3.50;
};

/// Returns the five built-in mode prior presets in display order:
/// Standard, Jazz, Modal, Baroque, Contemporary.
std::vector<ModePriorPreset> modePriorPresets();

/// Settings required by the analysis bridge, context menu, and status bar.
/// Does NOT include chord-staff (implode) output settings.
/// This is the interface a clean-branch submission exposes.
class IComposingAnalysisConfiguration : MODULE_GLOBAL_INTERFACE
{
    INTERFACE_ID(IComposingAnalysisConfiguration)

public:
    virtual ~IComposingAnalysisConfiguration() = default;

    // ── Analysis behaviour ───────────────────────────────────────────────────

    virtual bool analyzeForChordSymbols() const = 0;
    virtual void setAnalyzeForChordSymbols(bool value) = 0;
    virtual muse::async::Notification analyzeForChordSymbolsChanged() const = 0;

    virtual bool analyzeForChordFunction() const = 0;
    virtual void setAnalyzeForChordFunction(bool value) = 0;
    virtual muse::async::Notification analyzeForChordFunctionChanged() const = 0;

    virtual bool inferKeyMode() const = 0;
    virtual void setInferKeyMode(bool value) = 0;
    virtual muse::async::Notification inferKeyModeChanged() const = 0;

    /// Number of alternative chord interpretations to show (1–3).
    virtual int analysisAlternatives() const = 0;
    virtual void setAnalysisAlternatives(int count) = 0;
    virtual muse::async::Notification analysisAlternativesChanged() const = 0;

    /// Tuning system key (e.g. "equal", "just").
    virtual std::string tuningSystemKey() const = 0;
    virtual void setTuningSystemKey(const std::string& key) = 0;
    virtual muse::async::Notification tuningSystemKeyChanged() const = 0;

    virtual bool tonicAnchoredTuning() const = 0;
    virtual void setTonicAnchoredTuning(bool value) = 0;
    virtual muse::async::Notification tonicAnchoredTuningChanged() const = 0;

    virtual bool minimizeTuningDeviation() const = 0;
    virtual void setMinimizeTuningDeviation(bool value) = 0;
    virtual muse::async::Notification minimizeTuningDeviationChanged() const = 0;

    virtual bool annotateTuningOffsets() const = 0;
    virtual void setAnnotateTuningOffsets(bool value) = 0;
    virtual muse::async::Notification annotateTuningOffsetsChanged() const = 0;

    // ── Status-bar display ───────────────────────────────────────────────────

    virtual bool showKeyModeInStatusBar() const = 0;
    virtual void setShowKeyModeInStatusBar(bool value) = 0;
    virtual muse::async::Notification showKeyModeInStatusBarChanged() const = 0;

    virtual bool showChordSymbolsInStatusBar() const = 0;
    virtual void setShowChordSymbolsInStatusBar(bool value) = 0;
    virtual muse::async::Notification showChordSymbolsInStatusBarChanged() const = 0;

    virtual bool showRomanNumeralsInStatusBar() const = 0;
    virtual void setShowRomanNumeralsInStatusBar(bool value) = 0;
    virtual muse::async::Notification showRomanNumeralsInStatusBarChanged() const = 0;

    virtual bool showNashvilleNumbersInStatusBar() const = 0;
    virtual void setShowNashvilleNumbersInStatusBar(bool value) = 0;
    virtual muse::async::Notification showNashvilleNumbersInStatusBarChanged() const = 0;

    // ── Mode priors (21 independent values, one per mode) ───────────────────
    // Diatonic
    virtual double modePriorIonian() const = 0;
    virtual void setModePriorIonian(double value) = 0;
    virtual muse::async::Notification modePriorIonianChanged() const = 0;

    virtual double modePriorDorian() const = 0;
    virtual void setModePriorDorian(double value) = 0;
    virtual muse::async::Notification modePriorDorianChanged() const = 0;

    virtual double modePriorPhrygian() const = 0;
    virtual void setModePriorPhrygian(double value) = 0;
    virtual muse::async::Notification modePriorPhrygianChanged() const = 0;

    virtual double modePriorLydian() const = 0;
    virtual void setModePriorLydian(double value) = 0;
    virtual muse::async::Notification modePriorLydianChanged() const = 0;

    virtual double modePriorMixolydian() const = 0;
    virtual void setModePriorMixolydian(double value) = 0;
    virtual muse::async::Notification modePriorMixolydianChanged() const = 0;

    virtual double modePriorAeolian() const = 0;
    virtual void setModePriorAeolian(double value) = 0;
    virtual muse::async::Notification modePriorAeolianChanged() const = 0;

    virtual double modePriorLocrian() const = 0;
    virtual void setModePriorLocrian(double value) = 0;
    virtual muse::async::Notification modePriorLocrianChanged() const = 0;

    // Melodic minor family
    virtual double modePriorMelodicMinor() const = 0;
    virtual void setModePriorMelodicMinor(double value) = 0;
    virtual muse::async::Notification modePriorMelodicMinorChanged() const = 0;

    virtual double modePriorDorianB2() const = 0;
    virtual void setModePriorDorianB2(double value) = 0;
    virtual muse::async::Notification modePriorDorianB2Changed() const = 0;

    virtual double modePriorLydianAugmented() const = 0;
    virtual void setModePriorLydianAugmented(double value) = 0;
    virtual muse::async::Notification modePriorLydianAugmentedChanged() const = 0;

    virtual double modePriorLydianDominant() const = 0;
    virtual void setModePriorLydianDominant(double value) = 0;
    virtual muse::async::Notification modePriorLydianDominantChanged() const = 0;

    virtual double modePriorMixolydianB6() const = 0;
    virtual void setModePriorMixolydianB6(double value) = 0;
    virtual muse::async::Notification modePriorMixolydianB6Changed() const = 0;

    virtual double modePriorAeolianB5() const = 0;
    virtual void setModePriorAeolianB5(double value) = 0;
    virtual muse::async::Notification modePriorAeolianB5Changed() const = 0;

    virtual double modePriorAltered() const = 0;
    virtual void setModePriorAltered(double value) = 0;
    virtual muse::async::Notification modePriorAlteredChanged() const = 0;

    // Harmonic minor family
    virtual double modePriorHarmonicMinor() const = 0;
    virtual void setModePriorHarmonicMinor(double value) = 0;
    virtual muse::async::Notification modePriorHarmonicMinorChanged() const = 0;

    virtual double modePriorLocrianSharp6() const = 0;
    virtual void setModePriorLocrianSharp6(double value) = 0;
    virtual muse::async::Notification modePriorLocrianSharp6Changed() const = 0;

    virtual double modePriorIonianSharp5() const = 0;
    virtual void setModePriorIonianSharp5(double value) = 0;
    virtual muse::async::Notification modePriorIonianSharp5Changed() const = 0;

    virtual double modePriorDorianSharp4() const = 0;
    virtual void setModePriorDorianSharp4(double value) = 0;
    virtual muse::async::Notification modePriorDorianSharp4Changed() const = 0;

    virtual double modePriorPhrygianDominant() const = 0;
    virtual void setModePriorPhrygianDominant(double value) = 0;
    virtual muse::async::Notification modePriorPhrygianDominantChanged() const = 0;

    virtual double modePriorLydianSharp2() const = 0;
    virtual void setModePriorLydianSharp2(double value) = 0;
    virtual muse::async::Notification modePriorLydianSharp2Changed() const = 0;

    virtual double modePriorAlteredDomBB7() const = 0;
    virtual void setModePriorAlteredDomBB7(double value) = 0;
    virtual muse::async::Notification modePriorAlteredDomBB7Changed() const = 0;

    // ── Preset helpers ───────────────────────────────────────────────────────

    /// Apply all 21 mode priors from the named preset.
    /// name must be one of the names returned by modePriorPresets(); unknown
    /// names are ignored.  Emits individual modePriorXxxChanged notifications.
    virtual void applyModePriorPreset(const std::string& name) = 0;

    /// Return the name of the currently matching preset, or empty string if
    /// the current settings do not exactly match any built-in preset.
    virtual std::string currentModePriorPreset() const = 0;
};

} // namespace mu::composing
