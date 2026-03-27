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

    bool analyzeForRomanNumerals() const override;
    void setAnalyzeForRomanNumerals(bool value) override;
    muse::async::Notification analyzeForRomanNumeralsChanged() const override;

    bool inferKeyMode() const override;
    void setInferKeyMode(bool value) override;
    muse::async::Notification inferKeyModeChanged() const override;

    int analysisAlternatives() const override;
    void setAnalysisAlternatives(int count) override;
    muse::async::Notification analysisAlternativesChanged() const override;

    std::string tuningSystemKey() const override;
    void setTuningSystemKey(const std::string& key) override;
    muse::async::Notification tuningSystemKeyChanged() const override;

    bool showKeyModeInStatusBar() const override;
    void setShowKeyModeInStatusBar(bool value) override;
    muse::async::Notification showKeyModeInStatusBarChanged() const override;

    int statusBarChordSymbolCount() const override;
    void setStatusBarChordSymbolCount(int count) override;
    muse::async::Notification statusBarChordSymbolCountChanged() const override;

    int statusBarRomanNumeralCount() const override;
    void setStatusBarRomanNumeralCount(int count) override;
    muse::async::Notification statusBarRomanNumeralCountChanged() const override;

private:
    muse::async::Notification m_analyzeForChordSymbolsChanged;
    muse::async::Notification m_analyzeForRomanNumeralsChanged;
    muse::async::Notification m_inferKeyModeChanged;
    muse::async::Notification m_analysisAlternativesChanged;
    muse::async::Notification m_tuningSystemKeyChanged;
    muse::async::Notification m_showKeyModeInStatusBarChanged;
    muse::async::Notification m_statusBarChordSymbolCountChanged;
    muse::async::Notification m_statusBarRomanNumeralCountChanged;
};

} // namespace mu::composing
