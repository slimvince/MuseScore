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
#include "composingpreferencesmodel.h"

using namespace mu::preferences;

ComposingPreferencesModel::ComposingPreferencesModel(QObject* parent)
    : QObject(parent), muse::Contextable(muse::iocCtxForQmlObject(this))
{
}

void ComposingPreferencesModel::load()
{
    setupConnections();
}

void ComposingPreferencesModel::setupConnections()
{
    analysisConfig()->analyzeForChordSymbolsChanged().onNotify(this, [this]() {
        emit analyzeForChordSymbolsChanged();
    });
    analysisConfig()->analyzeForChordFunctionChanged().onNotify(this, [this]() {
        emit analyzeForChordFunctionChanged();
        emit inferKeyModeChanged(); // chord function forces key/mode on
    });
    analysisConfig()->inferKeyModeChanged().onNotify(this, [this]() {
        emit inferKeyModeChanged();
    });
    analysisConfig()->analysisAlternativesChanged().onNotify(this, [this]() {
        emit analysisAlternativesChanged();
    });
    analysisConfig()->tuningSystemKeyChanged().onNotify(this, [this]() {
        emit tuningSystemKeyChanged();
    });
    analysisConfig()->tonicAnchoredTuningChanged().onNotify(this, [this]() {
        emit tonicAnchoredTuningChanged();
    });
    analysisConfig()->tuningModeChanged().onNotify(this, [this]() {
        emit tuningModeChanged();
    });
    analysisConfig()->allowSplitSlurOfSustainedEventsChanged().onNotify(this, [this]() {
        emit allowSplitSlurOfSustainedEventsChanged();
    });
    analysisConfig()->minimizeTuningDeviationChanged().onNotify(this, [this]() {
        emit minimizeTuningDeviationChanged();
    });
    analysisConfig()->annotateTuningOffsetsChanged().onNotify(this, [this]() {
        emit annotateTuningOffsetsChanged();
    });
    analysisConfig()->annotateDriftAtBoundariesChanged().onNotify(this, [this]() {
        emit annotateDriftAtBoundariesChanged();
    });
    analysisConfig()->useRegionalAccumulationChanged().onNotify(this, [this]() {
        emit useRegionalAccumulationChanged();
    });
    analysisConfig()->showKeyModeInStatusBarChanged().onNotify(this, [this]() {
        emit showKeyModeInStatusBarChanged();
    });
    analysisConfig()->showChordSymbolsInStatusBarChanged().onNotify(this, [this]() {
        emit showChordSymbolsInStatusBarChanged();
    });
    analysisConfig()->showRomanNumeralsInStatusBarChanged().onNotify(this, [this]() {
        emit showRomanNumeralsInStatusBarChanged();
    });
    analysisConfig()->showNashvilleNumbersInStatusBarChanged().onNotify(this, [this]() {
        emit showNashvilleNumbersInStatusBarChanged();
    });
    // Mode priors — diatonic
    // Each handler emits the individual Changed signal AND currentModePriorPresetChanged
    // so that preset buttons stay in sync whenever a slider is moved.
    analysisConfig()->modePriorIonianChanged().onNotify(this, [this]()     { emit modePriorIonianChanged();     emit currentModePriorPresetChanged(); });
    analysisConfig()->modePriorDorianChanged().onNotify(this, [this]()     { emit modePriorDorianChanged();     emit currentModePriorPresetChanged(); });
    analysisConfig()->modePriorPhrygianChanged().onNotify(this, [this]()   { emit modePriorPhrygianChanged();   emit currentModePriorPresetChanged(); });
    analysisConfig()->modePriorLydianChanged().onNotify(this, [this]()     { emit modePriorLydianChanged();     emit currentModePriorPresetChanged(); });
    analysisConfig()->modePriorMixolydianChanged().onNotify(this, [this]() { emit modePriorMixolydianChanged(); emit currentModePriorPresetChanged(); });
    analysisConfig()->modePriorAeolianChanged().onNotify(this, [this]()    { emit modePriorAeolianChanged();    emit currentModePriorPresetChanged(); });
    analysisConfig()->modePriorLocrianChanged().onNotify(this, [this]()    { emit modePriorLocrianChanged();    emit currentModePriorPresetChanged(); });
    // Mode priors — melodic minor family
    analysisConfig()->modePriorMelodicMinorChanged().onNotify(this, [this]()   { emit modePriorMelodicMinorChanged();   emit currentModePriorPresetChanged(); });
    analysisConfig()->modePriorDorianB2Changed().onNotify(this, [this]()       { emit modePriorDorianB2Changed();       emit currentModePriorPresetChanged(); });
    analysisConfig()->modePriorLydianAugmentedChanged().onNotify(this, [this]() { emit modePriorLydianAugmentedChanged(); emit currentModePriorPresetChanged(); });
    analysisConfig()->modePriorLydianDominantChanged().onNotify(this, [this]()  { emit modePriorLydianDominantChanged();  emit currentModePriorPresetChanged(); });
    analysisConfig()->modePriorMixolydianB6Changed().onNotify(this, [this]()   { emit modePriorMixolydianB6Changed();   emit currentModePriorPresetChanged(); });
    analysisConfig()->modePriorAeolianB5Changed().onNotify(this, [this]()      { emit modePriorAeolianB5Changed();      emit currentModePriorPresetChanged(); });
    analysisConfig()->modePriorAlteredChanged().onNotify(this, [this]()        { emit modePriorAlteredChanged();        emit currentModePriorPresetChanged(); });
    // Mode priors — harmonic minor family
    analysisConfig()->modePriorHarmonicMinorChanged().onNotify(this, [this]()  { emit modePriorHarmonicMinorChanged();  emit currentModePriorPresetChanged(); });
    analysisConfig()->modePriorLocrianSharp6Changed().onNotify(this, [this]()  { emit modePriorLocrianSharp6Changed();  emit currentModePriorPresetChanged(); });
    analysisConfig()->modePriorIonianSharp5Changed().onNotify(this, [this]()   { emit modePriorIonianSharp5Changed();   emit currentModePriorPresetChanged(); });
    analysisConfig()->modePriorDorianSharp4Changed().onNotify(this, [this]()   { emit modePriorDorianSharp4Changed();   emit currentModePriorPresetChanged(); });
    analysisConfig()->modePriorPhrygianDominantChanged().onNotify(this, [this]() { emit modePriorPhrygianDominantChanged(); emit currentModePriorPresetChanged(); });
    analysisConfig()->modePriorLydianSharp2Changed().onNotify(this, [this]()   { emit modePriorLydianSharp2Changed();   emit currentModePriorPresetChanged(); });
    analysisConfig()->modePriorAlteredDomBB7Changed().onNotify(this, [this]()  { emit modePriorAlteredDomBB7Changed();  emit currentModePriorPresetChanged(); });
}

// ── Getters ──────────────────────────────────────────────────────────────────

bool ComposingPreferencesModel::analyzeForChordSymbols() const
{
    return analysisConfig()->analyzeForChordSymbols();
}

bool ComposingPreferencesModel::analyzeForChordFunction() const
{
    return analysisConfig()->analyzeForChordFunction();
}

bool ComposingPreferencesModel::inferKeyMode() const
{
    // inferKeyMode is forced on when chord-function analysis is active.
    if (analysisConfig()->analyzeForChordFunction()) {
        return true;
    }
    return analysisConfig()->inferKeyMode();
}

int ComposingPreferencesModel::analysisAlternatives() const
{
    return analysisConfig()->analysisAlternatives();
}

QString ComposingPreferencesModel::tuningSystemKey() const
{
    return QString::fromStdString(analysisConfig()->tuningSystemKey());
}

bool ComposingPreferencesModel::tonicAnchoredTuning() const
{
    return analysisConfig()->tonicAnchoredTuning();
}

int ComposingPreferencesModel::tuningMode() const
{
    return static_cast<int>(analysisConfig()->tuningMode());
}

bool ComposingPreferencesModel::allowSplitSlurOfSustainedEvents() const
{
    return analysisConfig()->allowSplitSlurOfSustainedEvents();
}

bool ComposingPreferencesModel::minimizeTuningDeviation() const
{
    return analysisConfig()->minimizeTuningDeviation();
}

bool ComposingPreferencesModel::annotateTuningOffsets() const
{
    return analysisConfig()->annotateTuningOffsets();
}

bool ComposingPreferencesModel::annotateDriftAtBoundaries() const
{
    return analysisConfig()->annotateDriftAtBoundaries();
}

bool ComposingPreferencesModel::useRegionalAccumulation() const
{
    return analysisConfig()->useRegionalAccumulation();
}

// ── Mode prior getters ────────────────────────────────────────────────────────

double ComposingPreferencesModel::modePriorIonian() const     { return analysisConfig()->modePriorIonian(); }
double ComposingPreferencesModel::modePriorDorian() const     { return analysisConfig()->modePriorDorian(); }
double ComposingPreferencesModel::modePriorPhrygian() const   { return analysisConfig()->modePriorPhrygian(); }
double ComposingPreferencesModel::modePriorLydian() const     { return analysisConfig()->modePriorLydian(); }
double ComposingPreferencesModel::modePriorMixolydian() const { return analysisConfig()->modePriorMixolydian(); }
double ComposingPreferencesModel::modePriorAeolian() const    { return analysisConfig()->modePriorAeolian(); }
double ComposingPreferencesModel::modePriorLocrian() const    { return analysisConfig()->modePriorLocrian(); }

double ComposingPreferencesModel::modePriorMelodicMinor() const  { return analysisConfig()->modePriorMelodicMinor(); }
double ComposingPreferencesModel::modePriorDorianB2() const      { return analysisConfig()->modePriorDorianB2(); }
double ComposingPreferencesModel::modePriorLydianAugmented() const { return analysisConfig()->modePriorLydianAugmented(); }
double ComposingPreferencesModel::modePriorLydianDominant() const  { return analysisConfig()->modePriorLydianDominant(); }
double ComposingPreferencesModel::modePriorMixolydianB6() const  { return analysisConfig()->modePriorMixolydianB6(); }
double ComposingPreferencesModel::modePriorAeolianB5() const     { return analysisConfig()->modePriorAeolianB5(); }
double ComposingPreferencesModel::modePriorAltered() const       { return analysisConfig()->modePriorAltered(); }

double ComposingPreferencesModel::modePriorHarmonicMinor() const { return analysisConfig()->modePriorHarmonicMinor(); }
double ComposingPreferencesModel::modePriorLocrianSharp6() const { return analysisConfig()->modePriorLocrianSharp6(); }
double ComposingPreferencesModel::modePriorIonianSharp5() const  { return analysisConfig()->modePriorIonianSharp5(); }
double ComposingPreferencesModel::modePriorDorianSharp4() const  { return analysisConfig()->modePriorDorianSharp4(); }
double ComposingPreferencesModel::modePriorPhrygianDominant() const { return analysisConfig()->modePriorPhrygianDominant(); }
double ComposingPreferencesModel::modePriorLydianSharp2() const  { return analysisConfig()->modePriorLydianSharp2(); }
double ComposingPreferencesModel::modePriorAlteredDomBB7() const { return analysisConfig()->modePriorAlteredDomBB7(); }

QString ComposingPreferencesModel::currentModePriorPreset() const
{
    return QString::fromStdString(analysisConfig()->currentModePriorPreset());
}

void ComposingPreferencesModel::applyModePriorPreset(const QString& name)
{
    analysisConfig()->applyModePriorPreset(name.toStdString());
}

bool ComposingPreferencesModel::showKeyModeInStatusBar() const
{
    return analysisConfig()->showKeyModeInStatusBar();
}

bool ComposingPreferencesModel::showChordSymbolsInStatusBar() const
{
    return analysisConfig()->showChordSymbolsInStatusBar();
}

bool ComposingPreferencesModel::showRomanNumeralsInStatusBar() const
{
    return analysisConfig()->showRomanNumeralsInStatusBar();
}

bool ComposingPreferencesModel::showNashvilleNumbersInStatusBar() const
{
    return analysisConfig()->showNashvilleNumbersInStatusBar();
}

// ── Setters ──────────────────────────────────────────────────────────────────

void ComposingPreferencesModel::setAnalyzeForChordSymbols(bool value)
{
    if (analyzeForChordSymbols() == value) {
        return;
    }
    analysisConfig()->setAnalyzeForChordSymbols(value);
    emit analyzeForChordSymbolsChanged();
}

void ComposingPreferencesModel::setAnalyzeForChordFunction(bool value)
{
    if (analyzeForChordFunction() == value) {
        return;
    }
    analysisConfig()->setAnalyzeForChordFunction(value);
    emit analyzeForChordFunctionChanged();
}

void ComposingPreferencesModel::setInferKeyMode(bool value)
{
    // Silently ignore if forced on by chord-function analysis.
    if (analysisConfig()->analyzeForChordFunction()) {
        return;
    }
    if (analysisConfig()->inferKeyMode() == value) {
        return;
    }
    analysisConfig()->setInferKeyMode(value);
    emit inferKeyModeChanged();
}

void ComposingPreferencesModel::setAnalysisAlternatives(int count)
{
    if (analysisAlternatives() == count) {
        return;
    }
    analysisConfig()->setAnalysisAlternatives(count);
    emit analysisAlternativesChanged();
}

void ComposingPreferencesModel::setTuningSystemKey(const QString& key)
{
    if (tuningSystemKey() == key) {
        return;
    }
    analysisConfig()->setTuningSystemKey(key.toStdString());
    emit tuningSystemKeyChanged();
}

void ComposingPreferencesModel::setTonicAnchoredTuning(bool value)
{
    if (tonicAnchoredTuning() == value) {
        return;
    }
    analysisConfig()->setTonicAnchoredTuning(value);
    emit tonicAnchoredTuningChanged();
}

void ComposingPreferencesModel::setTuningMode(int mode)
{
    const auto typedMode = static_cast<mu::composing::intonation::TuningMode>(mode);
    if (analysisConfig()->tuningMode() == typedMode) {
        return;
    }
    analysisConfig()->setTuningMode(typedMode);
    emit tuningModeChanged();
}

void ComposingPreferencesModel::setAllowSplitSlurOfSustainedEvents(bool value)
{
    if (allowSplitSlurOfSustainedEvents() == value) {
        return;
    }
    analysisConfig()->setAllowSplitSlurOfSustainedEvents(value);
    emit allowSplitSlurOfSustainedEventsChanged();
}

void ComposingPreferencesModel::setMinimizeTuningDeviation(bool value)
{
    if (minimizeTuningDeviation() == value) {
        return;
    }
    analysisConfig()->setMinimizeTuningDeviation(value);
    emit minimizeTuningDeviationChanged();
}

void ComposingPreferencesModel::setAnnotateTuningOffsets(bool value)
{
    if (annotateTuningOffsets() == value) {
        return;
    }
    analysisConfig()->setAnnotateTuningOffsets(value);
    emit annotateTuningOffsetsChanged();
}

void ComposingPreferencesModel::setAnnotateDriftAtBoundaries(bool value)
{
    if (annotateDriftAtBoundaries() == value) {
        return;
    }
    analysisConfig()->setAnnotateDriftAtBoundaries(value);
    emit annotateDriftAtBoundariesChanged();
}

void ComposingPreferencesModel::setUseRegionalAccumulation(bool value)
{
    if (useRegionalAccumulation() == value) {
        return;
    }
    analysisConfig()->setUseRegionalAccumulation(value);
    emit useRegionalAccumulationChanged();
}

// ── Mode prior setters ────────────────────────────────────────────────────────

#define SET_MODE_PRIOR(Name) \
void ComposingPreferencesModel::setModePrior##Name(double v) { \
    if (qFuzzyCompare(modePrior##Name(), v)) { return; } \
    analysisConfig()->setModePrior##Name(v); \
    emit modePrior##Name##Changed(); \
}

SET_MODE_PRIOR(Ionian)
SET_MODE_PRIOR(Dorian)
SET_MODE_PRIOR(Phrygian)
SET_MODE_PRIOR(Lydian)
SET_MODE_PRIOR(Mixolydian)
SET_MODE_PRIOR(Aeolian)
SET_MODE_PRIOR(Locrian)
SET_MODE_PRIOR(MelodicMinor)
SET_MODE_PRIOR(DorianB2)
SET_MODE_PRIOR(LydianAugmented)
SET_MODE_PRIOR(LydianDominant)
SET_MODE_PRIOR(MixolydianB6)
SET_MODE_PRIOR(AeolianB5)
SET_MODE_PRIOR(Altered)
SET_MODE_PRIOR(HarmonicMinor)
SET_MODE_PRIOR(LocrianSharp6)
SET_MODE_PRIOR(IonianSharp5)
SET_MODE_PRIOR(DorianSharp4)
SET_MODE_PRIOR(PhrygianDominant)
SET_MODE_PRIOR(LydianSharp2)
SET_MODE_PRIOR(AlteredDomBB7)

#undef SET_MODE_PRIOR

void ComposingPreferencesModel::setShowKeyModeInStatusBar(bool value)
{
    if (showKeyModeInStatusBar() == value) {
        return;
    }
    analysisConfig()->setShowKeyModeInStatusBar(value);
    emit showKeyModeInStatusBarChanged();
}

void ComposingPreferencesModel::setShowChordSymbolsInStatusBar(bool value)
{
    if (showChordSymbolsInStatusBar() == value) {
        return;
    }
    analysisConfig()->setShowChordSymbolsInStatusBar(value);
    emit showChordSymbolsInStatusBarChanged();
}

void ComposingPreferencesModel::setShowRomanNumeralsInStatusBar(bool value)
{
    if (showRomanNumeralsInStatusBar() == value) {
        return;
    }
    analysisConfig()->setShowRomanNumeralsInStatusBar(value);
    emit showRomanNumeralsInStatusBarChanged();
}

void ComposingPreferencesModel::setShowNashvilleNumbersInStatusBar(bool value)
{
    if (showNashvilleNumbersInStatusBar() == value) {
        return;
    }
    analysisConfig()->setShowNashvilleNumbersInStatusBar(value);
    emit showNashvilleNumbersInStatusBarChanged();
}
