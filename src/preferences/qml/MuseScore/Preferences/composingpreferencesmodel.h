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
    Q_PROPERTY(bool analyzeForChordFunction  READ analyzeForChordFunction  WRITE setAnalyzeForChordFunction  NOTIFY analyzeForChordFunctionChanged)
    Q_PROPERTY(bool inferKeyMode             READ inferKeyMode             WRITE setInferKeyMode             NOTIFY inferKeyModeChanged)
    Q_PROPERTY(int  analysisAlternatives     READ analysisAlternatives     WRITE setAnalysisAlternatives     NOTIFY analysisAlternativesChanged)
    Q_PROPERTY(QString tuningSystemKey       READ tuningSystemKey          WRITE setTuningSystemKey          NOTIFY tuningSystemKeyChanged)
    Q_PROPERTY(bool tonicAnchoredTuning      READ tonicAnchoredTuning      WRITE setTonicAnchoredTuning      NOTIFY tonicAnchoredTuningChanged)
    Q_PROPERTY(bool minimizeTuningDeviation  READ minimizeTuningDeviation  WRITE setMinimizeTuningDeviation  NOTIFY minimizeTuningDeviationChanged)
    Q_PROPERTY(bool annotateTuningOffsets    READ annotateTuningOffsets    WRITE setAnnotateTuningOffsets    NOTIFY annotateTuningOffsetsChanged)

    // Chord staff output
    Q_PROPERTY(bool    chordStaffWriteChordSymbols   READ chordStaffWriteChordSymbols   WRITE setChordStaffWriteChordSymbols   NOTIFY chordStaffWriteChordSymbolsChanged)
    Q_PROPERTY(QString chordStaffFunctionNotation    READ chordStaffFunctionNotation    WRITE setChordStaffFunctionNotation    NOTIFY chordStaffFunctionNotationChanged)
    Q_PROPERTY(bool    chordStaffWriteKeyAnnotations READ chordStaffWriteKeyAnnotations WRITE setChordStaffWriteKeyAnnotations NOTIFY chordStaffWriteKeyAnnotationsChanged)
    Q_PROPERTY(bool    chordStaffHighlightNonDiatonic READ chordStaffHighlightNonDiatonic WRITE setChordStaffHighlightNonDiatonic NOTIFY chordStaffHighlightNonDiatonicChanged)
    Q_PROPERTY(bool    chordStaffWriteCadenceMarkers READ chordStaffWriteCadenceMarkers WRITE setChordStaffWriteCadenceMarkers NOTIFY chordStaffWriteCadenceMarkersChanged)

    // Mode detection weights
    Q_PROPERTY(double modeTierWeight1  READ modeTierWeight1  WRITE setModeTierWeight1  NOTIFY modeTierWeight1Changed)
    Q_PROPERTY(double modeTierWeight2  READ modeTierWeight2  WRITE setModeTierWeight2  NOTIFY modeTierWeight2Changed)
    Q_PROPERTY(double modeTierWeight3  READ modeTierWeight3  WRITE setModeTierWeight3  NOTIFY modeTierWeight3Changed)
    Q_PROPERTY(double modeTierWeight4  READ modeTierWeight4  WRITE setModeTierWeight4  NOTIFY modeTierWeight4Changed)

    // Status-bar display
    Q_PROPERTY(bool showKeyModeInStatusBar          READ showKeyModeInStatusBar          WRITE setShowKeyModeInStatusBar          NOTIFY showKeyModeInStatusBarChanged)
    Q_PROPERTY(bool showChordSymbolsInStatusBar     READ showChordSymbolsInStatusBar     WRITE setShowChordSymbolsInStatusBar     NOTIFY showChordSymbolsInStatusBarChanged)
    Q_PROPERTY(bool showRomanNumeralsInStatusBar    READ showRomanNumeralsInStatusBar    WRITE setShowRomanNumeralsInStatusBar    NOTIFY showRomanNumeralsInStatusBarChanged)
    Q_PROPERTY(bool showNashvilleNumbersInStatusBar READ showNashvilleNumbersInStatusBar WRITE setShowNashvilleNumbersInStatusBar NOTIFY showNashvilleNumbersInStatusBarChanged)

    muse::GlobalInject<composing::IComposingConfiguration> composingConfiguration;

public:
    explicit ComposingPreferencesModel(QObject* parent = nullptr);

    Q_INVOKABLE void load();

    bool analyzeForChordSymbols() const;
    bool analyzeForChordFunction() const;
    bool inferKeyMode() const;
    int  analysisAlternatives() const;
    QString tuningSystemKey() const;
    bool tonicAnchoredTuning() const;
    bool minimizeTuningDeviation() const;
    bool annotateTuningOffsets() const;

    double modeTierWeight1() const;
    double modeTierWeight2() const;
    double modeTierWeight3() const;
    double modeTierWeight4() const;

    bool    chordStaffWriteChordSymbols() const;
    QString chordStaffFunctionNotation() const;
    bool    chordStaffWriteKeyAnnotations() const;
    bool    chordStaffHighlightNonDiatonic() const;
    bool    chordStaffWriteCadenceMarkers() const;

    bool showKeyModeInStatusBar() const;
    bool showChordSymbolsInStatusBar() const;
    bool showRomanNumeralsInStatusBar() const;
    bool showNashvilleNumbersInStatusBar() const;

public slots:
    void setAnalyzeForChordSymbols(bool value);
    void setAnalyzeForChordFunction(bool value);
    void setInferKeyMode(bool value);
    void setAnalysisAlternatives(int count);
    void setTuningSystemKey(const QString& key);
    void setTonicAnchoredTuning(bool value);
    void setMinimizeTuningDeviation(bool value);
    void setAnnotateTuningOffsets(bool value);

    void setModeTierWeight1(double value);
    void setModeTierWeight2(double value);
    void setModeTierWeight3(double value);
    void setModeTierWeight4(double value);

    void setChordStaffWriteChordSymbols(bool value);
    void setChordStaffFunctionNotation(const QString& value);
    void setChordStaffWriteKeyAnnotations(bool value);
    void setChordStaffHighlightNonDiatonic(bool value);
    void setChordStaffWriteCadenceMarkers(bool value);

    void setShowKeyModeInStatusBar(bool value);
    void setShowChordSymbolsInStatusBar(bool value);
    void setShowRomanNumeralsInStatusBar(bool value);
    void setShowNashvilleNumbersInStatusBar(bool value);

signals:
    void analyzeForChordSymbolsChanged();
    void analyzeForChordFunctionChanged();
    void inferKeyModeChanged();
    void analysisAlternativesChanged();
    void tuningSystemKeyChanged();
    void tonicAnchoredTuningChanged();
    void minimizeTuningDeviationChanged();
    void annotateTuningOffsetsChanged();

    void modeTierWeight1Changed();
    void modeTierWeight2Changed();
    void modeTierWeight3Changed();
    void modeTierWeight4Changed();

    void chordStaffWriteChordSymbolsChanged();
    void chordStaffFunctionNotationChanged();
    void chordStaffWriteKeyAnnotationsChanged();
    void chordStaffHighlightNonDiatonicChanged();
    void chordStaffWriteCadenceMarkersChanged();

    void showKeyModeInStatusBarChanged();
    void showChordSymbolsInStatusBarChanged();
    void showRomanNumeralsInStatusBarChanged();
    void showNashvilleNumbersInStatusBarChanged();

private:
    void setupConnections();
};
} // namespace mu::preferences
