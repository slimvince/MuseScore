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

    bool minimizeTuningDeviation() const override;
    void setMinimizeTuningDeviation(bool value) override;
    muse::async::Notification minimizeTuningDeviationChanged() const override;

    bool annotateTuningOffsets() const override;
    void setAnnotateTuningOffsets(bool value) override;
    muse::async::Notification annotateTuningOffsetsChanged() const override;

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

    double modeTierWeight1() const override;
    void setModeTierWeight1(double value) override;
    muse::async::Notification modeTierWeight1Changed() const override;

    double modeTierWeight2() const override;
    void setModeTierWeight2(double value) override;
    muse::async::Notification modeTierWeight2Changed() const override;

    double modeTierWeight3() const override;
    void setModeTierWeight3(double value) override;
    muse::async::Notification modeTierWeight3Changed() const override;

    double modeTierWeight4() const override;
    void setModeTierWeight4(double value) override;
    muse::async::Notification modeTierWeight4Changed() const override;

private:
    muse::async::Notification m_analyzeForChordSymbolsChanged;
    muse::async::Notification m_analyzeForChordFunctionChanged;
    muse::async::Notification m_inferKeyModeChanged;
    muse::async::Notification m_analysisAlternativesChanged;
    muse::async::Notification m_tuningSystemKeyChanged;
    muse::async::Notification m_tonicAnchoredTuningChanged;
    muse::async::Notification m_minimizeTuningDeviationChanged;
    muse::async::Notification m_annotateTuningOffsetsChanged;
    muse::async::Notification m_showKeyModeInStatusBarChanged;
    muse::async::Notification m_showChordSymbolsInStatusBarChanged;
    muse::async::Notification m_showRomanNumeralsInStatusBarChanged;
    muse::async::Notification m_showNashvilleNumbersInStatusBarChanged;
    muse::async::Notification m_chordStaffWriteChordSymbolsChanged;
    muse::async::Notification m_chordStaffFunctionNotationChanged;
    muse::async::Notification m_chordStaffWriteKeyAnnotationsChanged;
    muse::async::Notification m_chordStaffHighlightNonDiatonicChanged;
    muse::async::Notification m_chordStaffWriteCadenceMarkersChanged;
    muse::async::Notification m_modeTierWeight1Changed;
    muse::async::Notification m_modeTierWeight2Changed;
    muse::async::Notification m_modeTierWeight3Changed;
    muse::async::Notification m_modeTierWeight4Changed;
};

} // namespace mu::composing
