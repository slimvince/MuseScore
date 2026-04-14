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

#include "composing/icomposinganalysisconfiguration.h"


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
    Q_PROPERTY(int  tuningMode               READ tuningMode               WRITE setTuningMode               NOTIFY tuningModeChanged)
    Q_PROPERTY(bool allowSplitSlurOfSustainedEvents READ allowSplitSlurOfSustainedEvents WRITE setAllowSplitSlurOfSustainedEvents NOTIFY allowSplitSlurOfSustainedEventsChanged)
    Q_PROPERTY(bool minimizeTuningDeviation  READ minimizeTuningDeviation  WRITE setMinimizeTuningDeviation  NOTIFY minimizeTuningDeviationChanged)
    Q_PROPERTY(bool annotateTuningOffsets      READ annotateTuningOffsets      WRITE setAnnotateTuningOffsets      NOTIFY annotateTuningOffsetsChanged)
    Q_PROPERTY(bool annotateDriftAtBoundaries  READ annotateDriftAtBoundaries  WRITE setAnnotateDriftAtBoundaries  NOTIFY annotateDriftAtBoundariesChanged)
    Q_PROPERTY(bool useRegionalAccumulation    READ useRegionalAccumulation    WRITE setUseRegionalAccumulation    NOTIFY useRegionalAccumulationChanged)

    // Mode priors — diatonic
    Q_PROPERTY(double modePriorIonian     READ modePriorIonian     WRITE setModePriorIonian     NOTIFY modePriorIonianChanged)
    Q_PROPERTY(double modePriorDorian     READ modePriorDorian     WRITE setModePriorDorian     NOTIFY modePriorDorianChanged)
    Q_PROPERTY(double modePriorPhrygian   READ modePriorPhrygian   WRITE setModePriorPhrygian   NOTIFY modePriorPhrygianChanged)
    Q_PROPERTY(double modePriorLydian     READ modePriorLydian     WRITE setModePriorLydian     NOTIFY modePriorLydianChanged)
    Q_PROPERTY(double modePriorMixolydian READ modePriorMixolydian WRITE setModePriorMixolydian NOTIFY modePriorMixolydianChanged)
    Q_PROPERTY(double modePriorAeolian    READ modePriorAeolian    WRITE setModePriorAeolian    NOTIFY modePriorAeolianChanged)
    Q_PROPERTY(double modePriorLocrian    READ modePriorLocrian    WRITE setModePriorLocrian    NOTIFY modePriorLocrianChanged)
    // Mode priors — melodic minor family
    Q_PROPERTY(double modePriorMelodicMinor  READ modePriorMelodicMinor  WRITE setModePriorMelodicMinor  NOTIFY modePriorMelodicMinorChanged)
    Q_PROPERTY(double modePriorDorianB2      READ modePriorDorianB2      WRITE setModePriorDorianB2      NOTIFY modePriorDorianB2Changed)
    Q_PROPERTY(double modePriorLydianAugmented READ modePriorLydianAugmented WRITE setModePriorLydianAugmented NOTIFY modePriorLydianAugmentedChanged)
    Q_PROPERTY(double modePriorLydianDominant  READ modePriorLydianDominant  WRITE setModePriorLydianDominant  NOTIFY modePriorLydianDominantChanged)
    Q_PROPERTY(double modePriorMixolydianB6  READ modePriorMixolydianB6  WRITE setModePriorMixolydianB6  NOTIFY modePriorMixolydianB6Changed)
    Q_PROPERTY(double modePriorAeolianB5     READ modePriorAeolianB5     WRITE setModePriorAeolianB5     NOTIFY modePriorAeolianB5Changed)
    Q_PROPERTY(double modePriorAltered       READ modePriorAltered       WRITE setModePriorAltered       NOTIFY modePriorAlteredChanged)
    // Mode priors — harmonic minor family
    Q_PROPERTY(double modePriorHarmonicMinor READ modePriorHarmonicMinor WRITE setModePriorHarmonicMinor NOTIFY modePriorHarmonicMinorChanged)
    Q_PROPERTY(double modePriorLocrianSharp6 READ modePriorLocrianSharp6 WRITE setModePriorLocrianSharp6 NOTIFY modePriorLocrianSharp6Changed)
    Q_PROPERTY(double modePriorIonianSharp5  READ modePriorIonianSharp5  WRITE setModePriorIonianSharp5  NOTIFY modePriorIonianSharp5Changed)
    Q_PROPERTY(double modePriorDorianSharp4  READ modePriorDorianSharp4  WRITE setModePriorDorianSharp4  NOTIFY modePriorDorianSharp4Changed)
    Q_PROPERTY(double modePriorPhrygianDominant READ modePriorPhrygianDominant WRITE setModePriorPhrygianDominant NOTIFY modePriorPhrygianDominantChanged)
    Q_PROPERTY(double modePriorLydianSharp2  READ modePriorLydianSharp2  WRITE setModePriorLydianSharp2  NOTIFY modePriorLydianSharp2Changed)
    Q_PROPERTY(double modePriorAlteredDomBB7 READ modePriorAlteredDomBB7 WRITE setModePriorAlteredDomBB7 NOTIFY modePriorAlteredDomBB7Changed)

    // Status-bar display
    Q_PROPERTY(bool showKeyModeInStatusBar          READ showKeyModeInStatusBar          WRITE setShowKeyModeInStatusBar          NOTIFY showKeyModeInStatusBarChanged)
    Q_PROPERTY(bool showChordSymbolsInStatusBar     READ showChordSymbolsInStatusBar     WRITE setShowChordSymbolsInStatusBar     NOTIFY showChordSymbolsInStatusBarChanged)
    Q_PROPERTY(bool showRomanNumeralsInStatusBar    READ showRomanNumeralsInStatusBar    WRITE setShowRomanNumeralsInStatusBar    NOTIFY showRomanNumeralsInStatusBarChanged)
    Q_PROPERTY(bool showNashvilleNumbersInStatusBar READ showNashvilleNumbersInStatusBar WRITE setShowNashvilleNumbersInStatusBar NOTIFY showNashvilleNumbersInStatusBarChanged)

    Q_PROPERTY(QString currentModePriorPreset READ currentModePriorPreset NOTIFY currentModePriorPresetChanged)

    muse::GlobalInject<composing::IComposingAnalysisConfiguration> analysisConfig;

public:
    explicit ComposingPreferencesModel(QObject* parent = nullptr);

    Q_INVOKABLE void load();

    bool analyzeForChordSymbols() const;
    bool analyzeForChordFunction() const;
    bool inferKeyMode() const;
    int  analysisAlternatives() const;
    QString tuningSystemKey() const;
    bool tonicAnchoredTuning() const;
    int  tuningMode() const;
    bool allowSplitSlurOfSustainedEvents() const;
    bool minimizeTuningDeviation() const;
    bool annotateTuningOffsets() const;
    bool annotateDriftAtBoundaries() const;
    bool useRegionalAccumulation() const;

    // Mode priors — diatonic
    double modePriorIonian() const;
    double modePriorDorian() const;
    double modePriorPhrygian() const;
    double modePriorLydian() const;
    double modePriorMixolydian() const;
    double modePriorAeolian() const;
    double modePriorLocrian() const;
    // Mode priors — melodic minor family
    double modePriorMelodicMinor() const;
    double modePriorDorianB2() const;
    double modePriorLydianAugmented() const;
    double modePriorLydianDominant() const;
    double modePriorMixolydianB6() const;
    double modePriorAeolianB5() const;
    double modePriorAltered() const;
    // Mode priors — harmonic minor family
    double modePriorHarmonicMinor() const;
    double modePriorLocrianSharp6() const;
    double modePriorIonianSharp5() const;
    double modePriorDorianSharp4() const;
    double modePriorPhrygianDominant() const;
    double modePriorLydianSharp2() const;
    double modePriorAlteredDomBB7() const;
    QString currentModePriorPreset() const;

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
    void setTuningMode(int mode);
    void setAllowSplitSlurOfSustainedEvents(bool value);
    void setMinimizeTuningDeviation(bool value);
    void setAnnotateTuningOffsets(bool value);
    void setAnnotateDriftAtBoundaries(bool value);
    void setUseRegionalAccumulation(bool value);

    // Mode priors — diatonic
    void setModePriorIonian(double value);
    void setModePriorDorian(double value);
    void setModePriorPhrygian(double value);
    void setModePriorLydian(double value);
    void setModePriorMixolydian(double value);
    void setModePriorAeolian(double value);
    void setModePriorLocrian(double value);
    // Mode priors — melodic minor family
    void setModePriorMelodicMinor(double value);
    void setModePriorDorianB2(double value);
    void setModePriorLydianAugmented(double value);
    void setModePriorLydianDominant(double value);
    void setModePriorMixolydianB6(double value);
    void setModePriorAeolianB5(double value);
    void setModePriorAltered(double value);
    // Mode priors — harmonic minor family
    void setModePriorHarmonicMinor(double value);
    void setModePriorLocrianSharp6(double value);
    void setModePriorIonianSharp5(double value);
    void setModePriorDorianSharp4(double value);
    void setModePriorPhrygianDominant(double value);
    void setModePriorLydianSharp2(double value);
    void setModePriorAlteredDomBB7(double value);
    void applyModePriorPreset(const QString& name);

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
    void tuningModeChanged();
    void allowSplitSlurOfSustainedEventsChanged();
    void minimizeTuningDeviationChanged();
    void annotateTuningOffsetsChanged();
    void annotateDriftAtBoundariesChanged();
    void useRegionalAccumulationChanged();

    // Mode priors — diatonic
    void modePriorIonianChanged();
    void modePriorDorianChanged();
    void modePriorPhrygianChanged();
    void modePriorLydianChanged();
    void modePriorMixolydianChanged();
    void modePriorAeolianChanged();
    void modePriorLocrianChanged();
    // Mode priors — melodic minor family
    void modePriorMelodicMinorChanged();
    void modePriorDorianB2Changed();
    void modePriorLydianAugmentedChanged();
    void modePriorLydianDominantChanged();
    void modePriorMixolydianB6Changed();
    void modePriorAeolianB5Changed();
    void modePriorAlteredChanged();
    // Mode priors — harmonic minor family
    void modePriorHarmonicMinorChanged();
    void modePriorLocrianSharp6Changed();
    void modePriorIonianSharp5Changed();
    void modePriorDorianSharp4Changed();
    void modePriorPhrygianDominantChanged();
    void modePriorLydianSharp2Changed();
    void modePriorAlteredDomBB7Changed();
    void currentModePriorPresetChanged();

    void showKeyModeInStatusBarChanged();
    void showChordSymbolsInStatusBarChanged();
    void showRomanNumeralsInStatusBarChanged();
    void showNashvilleNumbersInStatusBarChanged();

private:
    void setupConnections();
};
} // namespace mu::preferences
