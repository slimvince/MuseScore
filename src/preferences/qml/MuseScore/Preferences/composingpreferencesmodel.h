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

#include <qqmlintegration.h>
#include <QObject>

#include "modularity/ioc.h"
#include "async/asyncable.h"

#include "composing/icomposingconfiguration.h"

namespace mu::preferences {
class ComposingPreferencesModel : public QObject, public muse::Contextable, public muse::async::Asyncable
{
    Q_OBJECT
    QML_ELEMENT;

    // Analysis behaviour
    Q_PROPERTY(bool analyzeForChordSymbols   READ analyzeForChordSymbols   WRITE setAnalyzeForChordSymbols   NOTIFY analyzeForChordSymbolsChanged)
    Q_PROPERTY(bool analyzeForRomanNumerals  READ analyzeForRomanNumerals  WRITE setAnalyzeForRomanNumerals  NOTIFY analyzeForRomanNumeralsChanged)
    Q_PROPERTY(bool inferKeyMode             READ inferKeyMode             WRITE setInferKeyMode             NOTIFY inferKeyModeChanged)
    Q_PROPERTY(int  analysisAlternatives     READ analysisAlternatives     WRITE setAnalysisAlternatives     NOTIFY analysisAlternativesChanged)

    // Status-bar display
    Q_PROPERTY(bool showKeyModeInStatusBar      READ showKeyModeInStatusBar      WRITE setShowKeyModeInStatusBar      NOTIFY showKeyModeInStatusBarChanged)
    Q_PROPERTY(int  statusBarChordSymbolCount   READ statusBarChordSymbolCount   WRITE setStatusBarChordSymbolCount   NOTIFY statusBarChordSymbolCountChanged)
    Q_PROPERTY(int  statusBarRomanNumeralCount  READ statusBarRomanNumeralCount  WRITE setStatusBarRomanNumeralCount  NOTIFY statusBarRomanNumeralCountChanged)

    muse::GlobalInject<composing::IComposingConfiguration> composingConfiguration;

public:
    explicit ComposingPreferencesModel(QObject* parent = nullptr);

    Q_INVOKABLE void load();

    bool analyzeForChordSymbols() const;
    bool analyzeForRomanNumerals() const;
    bool inferKeyMode() const;
    int  analysisAlternatives() const;

    bool showKeyModeInStatusBar() const;
    int  statusBarChordSymbolCount() const;
    int  statusBarRomanNumeralCount() const;

public slots:
    void setAnalyzeForChordSymbols(bool value);
    void setAnalyzeForRomanNumerals(bool value);
    void setInferKeyMode(bool value);
    void setAnalysisAlternatives(int count);

    void setShowKeyModeInStatusBar(bool value);
    void setStatusBarChordSymbolCount(int count);
    void setStatusBarRomanNumeralCount(int count);

signals:
    void analyzeForChordSymbolsChanged();
    void analyzeForRomanNumeralsChanged();
    void inferKeyModeChanged();
    void analysisAlternativesChanged();

    void showKeyModeInStatusBarChanged();
    void statusBarChordSymbolCountChanged();
    void statusBarRomanNumeralCountChanged();

private:
    void setupConnections();
};
} // namespace mu::preferences
