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

#include "icomposingconfiguration.h"

namespace mu::composing {

class ComposingConfiguration : public IComposingConfiguration
{
public:
    void init();

    bool analyzeForChordSymbols() const override;
    void setAnalyzeForChordSymbols(bool value) override;
    muse::async::Notification analyzeForChordSymbolsChanged() const override;

    bool analyzeForChordFunction() const override;
    void setAnalyzeForChordFunction(bool value) override;
    muse::async::Notification analyzeForChordFunctionChanged() const override;

    bool inferKeyMode() const override;
    void setInferKeyMode(bool value) override;
    muse::async::Notification inferKeyModeChanged() const override;

    int analysisAlternatives() const override;
    void setAnalysisAlternatives(int count) override;
    muse::async::Notification analysisAlternativesChanged() const override;

    std::string tuningSystemKey() const override;
    void setTuningSystemKey(const std::string& key) override;
    muse::async::Notification tuningSystemKeyChanged() const override;

    bool tonicAnchoredTuning() const override;
    void setTonicAnchoredTuning(bool value) override;
    muse::async::Notification tonicAnchoredTuningChanged() const override;

    mu::composing::intonation::TuningMode tuningMode() const override;
    void setTuningMode(mu::composing::intonation::TuningMode mode) override;
    muse::async::Notification tuningModeChanged() const override;

    bool allowSplitSlurOfSustainedEvents() const override;
    void setAllowSplitSlurOfSustainedEvents(bool value) override;
    muse::async::Notification allowSplitSlurOfSustainedEventsChanged() const override;

    bool minimizeTuningDeviation() const override;
    void setMinimizeTuningDeviation(bool value) override;
    muse::async::Notification minimizeTuningDeviationChanged() const override;

    bool annotateTuningOffsets() const override;
    void setAnnotateTuningOffsets(bool value) override;
    muse::async::Notification annotateTuningOffsetsChanged() const override;

    bool annotateDriftAtBoundaries() const override;
    void setAnnotateDriftAtBoundaries(bool value) override;
    muse::async::Notification annotateDriftAtBoundariesChanged() const override;

    bool useRegionalAccumulation() const override;
    void setUseRegionalAccumulation(bool value) override;
    muse::async::Notification useRegionalAccumulationChanged() const override;

    bool showKeyModeInStatusBar() const override;
    void setShowKeyModeInStatusBar(bool value) override;
    muse::async::Notification showKeyModeInStatusBarChanged() const override;

    bool showChordSymbolsInStatusBar() const override;
    void setShowChordSymbolsInStatusBar(bool value) override;
    muse::async::Notification showChordSymbolsInStatusBarChanged() const override;

    bool showRomanNumeralsInStatusBar() const override;
    void setShowRomanNumeralsInStatusBar(bool value) override;
    muse::async::Notification showRomanNumeralsInStatusBarChanged() const override;

    bool showNashvilleNumbersInStatusBar() const override;
    void setShowNashvilleNumbersInStatusBar(bool value) override;
    muse::async::Notification showNashvilleNumbersInStatusBarChanged() const override;

    bool chordStaffWriteChordSymbols() const override;
    void setChordStaffWriteChordSymbols(bool value) override;
    muse::async::Notification chordStaffWriteChordSymbolsChanged() const override;

    std::string chordStaffFunctionNotation() const override;
    void setChordStaffFunctionNotation(const std::string& value) override;
    muse::async::Notification chordStaffFunctionNotationChanged() const override;

    bool chordStaffWriteKeyAnnotations() const override;
    void setChordStaffWriteKeyAnnotations(bool value) override;
    muse::async::Notification chordStaffWriteKeyAnnotationsChanged() const override;

    bool chordStaffHighlightNonDiatonic() const override;
    void setChordStaffHighlightNonDiatonic(bool value) override;
    muse::async::Notification chordStaffHighlightNonDiatonicChanged() const override;

    bool chordStaffWriteCadenceMarkers() const override;
    void setChordStaffWriteCadenceMarkers(bool value) override;
    muse::async::Notification chordStaffWriteCadenceMarkersChanged() const override;

    // ── Mode priors (21 independent values) ─────────────────────────────────
    // Diatonic
    double modePriorIonian() const override;
    void setModePriorIonian(double value) override;
    muse::async::Notification modePriorIonianChanged() const override;

    double modePriorDorian() const override;
    void setModePriorDorian(double value) override;
    muse::async::Notification modePriorDorianChanged() const override;

    double modePriorPhrygian() const override;
    void setModePriorPhrygian(double value) override;
    muse::async::Notification modePriorPhrygianChanged() const override;

    double modePriorLydian() const override;
    void setModePriorLydian(double value) override;
    muse::async::Notification modePriorLydianChanged() const override;

    double modePriorMixolydian() const override;
    void setModePriorMixolydian(double value) override;
    muse::async::Notification modePriorMixolydianChanged() const override;

    double modePriorAeolian() const override;
    void setModePriorAeolian(double value) override;
    muse::async::Notification modePriorAeolianChanged() const override;

    double modePriorLocrian() const override;
    void setModePriorLocrian(double value) override;
    muse::async::Notification modePriorLocrianChanged() const override;

    // Melodic minor family
    double modePriorMelodicMinor() const override;
    void setModePriorMelodicMinor(double value) override;
    muse::async::Notification modePriorMelodicMinorChanged() const override;

    double modePriorDorianB2() const override;
    void setModePriorDorianB2(double value) override;
    muse::async::Notification modePriorDorianB2Changed() const override;

    double modePriorLydianAugmented() const override;
    void setModePriorLydianAugmented(double value) override;
    muse::async::Notification modePriorLydianAugmentedChanged() const override;

    double modePriorLydianDominant() const override;
    void setModePriorLydianDominant(double value) override;
    muse::async::Notification modePriorLydianDominantChanged() const override;

    double modePriorMixolydianB6() const override;
    void setModePriorMixolydianB6(double value) override;
    muse::async::Notification modePriorMixolydianB6Changed() const override;

    double modePriorAeolianB5() const override;
    void setModePriorAeolianB5(double value) override;
    muse::async::Notification modePriorAeolianB5Changed() const override;

    double modePriorAltered() const override;
    void setModePriorAltered(double value) override;
    muse::async::Notification modePriorAlteredChanged() const override;

    // Harmonic minor family
    double modePriorHarmonicMinor() const override;
    void setModePriorHarmonicMinor(double value) override;
    muse::async::Notification modePriorHarmonicMinorChanged() const override;

    double modePriorLocrianSharp6() const override;
    void setModePriorLocrianSharp6(double value) override;
    muse::async::Notification modePriorLocrianSharp6Changed() const override;

    double modePriorIonianSharp5() const override;
    void setModePriorIonianSharp5(double value) override;
    muse::async::Notification modePriorIonianSharp5Changed() const override;

    double modePriorDorianSharp4() const override;
    void setModePriorDorianSharp4(double value) override;
    muse::async::Notification modePriorDorianSharp4Changed() const override;

    double modePriorPhrygianDominant() const override;
    void setModePriorPhrygianDominant(double value) override;
    muse::async::Notification modePriorPhrygianDominantChanged() const override;

    double modePriorLydianSharp2() const override;
    void setModePriorLydianSharp2(double value) override;
    muse::async::Notification modePriorLydianSharp2Changed() const override;

    double modePriorAlteredDomBB7() const override;
    void setModePriorAlteredDomBB7(double value) override;
    muse::async::Notification modePriorAlteredDomBB7Changed() const override;

    void applyModePriorPreset(const std::string& name) override;
    std::string currentModePriorPreset() const override;

private:
    muse::async::Notification m_analyzeForChordSymbolsChanged;
    muse::async::Notification m_analyzeForChordFunctionChanged;
    muse::async::Notification m_inferKeyModeChanged;
    muse::async::Notification m_analysisAlternativesChanged;
    muse::async::Notification m_tuningSystemKeyChanged;
    muse::async::Notification m_tonicAnchoredTuningChanged;
    muse::async::Notification m_tuningModeChanged;
    muse::async::Notification m_allowSplitSlurOfSustainedEventsChanged;
    muse::async::Notification m_minimizeTuningDeviationChanged;
    muse::async::Notification m_annotateTuningOffsetsChanged;
    muse::async::Notification m_annotateDriftAtBoundariesChanged;
    muse::async::Notification m_useRegionalAccumulationChanged;
    muse::async::Notification m_showKeyModeInStatusBarChanged;
    muse::async::Notification m_showChordSymbolsInStatusBarChanged;
    muse::async::Notification m_showRomanNumeralsInStatusBarChanged;
    muse::async::Notification m_showNashvilleNumbersInStatusBarChanged;
    muse::async::Notification m_chordStaffWriteChordSymbolsChanged;
    muse::async::Notification m_chordStaffFunctionNotationChanged;
    muse::async::Notification m_chordStaffWriteKeyAnnotationsChanged;
    muse::async::Notification m_chordStaffHighlightNonDiatonicChanged;
    muse::async::Notification m_chordStaffWriteCadenceMarkersChanged;
    // Diatonic mode priors
    muse::async::Notification m_modePriorIonianChanged;
    muse::async::Notification m_modePriorDorianChanged;
    muse::async::Notification m_modePriorPhrygianChanged;
    muse::async::Notification m_modePriorLydianChanged;
    muse::async::Notification m_modePriorMixolydianChanged;
    muse::async::Notification m_modePriorAeolianChanged;
    muse::async::Notification m_modePriorLocrianChanged;
    // Melodic minor family mode priors
    muse::async::Notification m_modePriorMelodicMinorChanged;
    muse::async::Notification m_modePriorDorianB2Changed;
    muse::async::Notification m_modePriorLydianAugmentedChanged;
    muse::async::Notification m_modePriorLydianDominantChanged;
    muse::async::Notification m_modePriorMixolydianB6Changed;
    muse::async::Notification m_modePriorAeolianB5Changed;
    muse::async::Notification m_modePriorAlteredChanged;
    // Harmonic minor family mode priors
    muse::async::Notification m_modePriorHarmonicMinorChanged;
    muse::async::Notification m_modePriorLocrianSharp6Changed;
    muse::async::Notification m_modePriorIonianSharp5Changed;
    muse::async::Notification m_modePriorDorianSharp4Changed;
    muse::async::Notification m_modePriorPhrygianDominantChanged;
    muse::async::Notification m_modePriorLydianSharp2Changed;
    muse::async::Notification m_modePriorAlteredDomBB7Changed;
};

} // namespace mu::composing
