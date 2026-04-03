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
    composingConfiguration()->analyzeForChordSymbolsChanged().onNotify(this, [this]() {
        emit analyzeForChordSymbolsChanged();
    });
    composingConfiguration()->analyzeForChordFunctionChanged().onNotify(this, [this]() {
        emit analyzeForChordFunctionChanged();
        emit inferKeyModeChanged(); // chord function forces key/mode on
    });
    composingConfiguration()->inferKeyModeChanged().onNotify(this, [this]() {
        emit inferKeyModeChanged();
    });
    composingConfiguration()->analysisAlternativesChanged().onNotify(this, [this]() {
        emit analysisAlternativesChanged();
    });
    composingConfiguration()->tuningSystemKeyChanged().onNotify(this, [this]() {
        emit tuningSystemKeyChanged();
    });
    composingConfiguration()->tonicAnchoredTuningChanged().onNotify(this, [this]() {
        emit tonicAnchoredTuningChanged();
    });
    composingConfiguration()->minimizeTuningDeviationChanged().onNotify(this, [this]() {
        emit minimizeTuningDeviationChanged();
    });
    composingConfiguration()->annotateTuningOffsetsChanged().onNotify(this, [this]() {
        emit annotateTuningOffsetsChanged();
    });
    composingConfiguration()->chordStaffWriteChordSymbolsChanged().onNotify(this, [this]() {
        emit chordStaffWriteChordSymbolsChanged();
    });
    composingConfiguration()->chordStaffFunctionNotationChanged().onNotify(this, [this]() {
        emit chordStaffFunctionNotationChanged();
    });
    composingConfiguration()->chordStaffWriteKeyAnnotationsChanged().onNotify(this, [this]() {
        emit chordStaffWriteKeyAnnotationsChanged();
    });
    composingConfiguration()->chordStaffHighlightNonDiatonicChanged().onNotify(this, [this]() {
        emit chordStaffHighlightNonDiatonicChanged();
    });
    composingConfiguration()->chordStaffWriteCadenceMarkersChanged().onNotify(this, [this]() {
        emit chordStaffWriteCadenceMarkersChanged();
    });
    composingConfiguration()->showKeyModeInStatusBarChanged().onNotify(this, [this]() {
        emit showKeyModeInStatusBarChanged();
    });
    composingConfiguration()->showChordSymbolsInStatusBarChanged().onNotify(this, [this]() {
        emit showChordSymbolsInStatusBarChanged();
    });
    composingConfiguration()->showRomanNumeralsInStatusBarChanged().onNotify(this, [this]() {
        emit showRomanNumeralsInStatusBarChanged();
    });
    composingConfiguration()->showNashvilleNumbersInStatusBarChanged().onNotify(this, [this]() {
        emit showNashvilleNumbersInStatusBarChanged();
    });
    composingConfiguration()->modeTierWeight1Changed().onNotify(this, [this]() {
        emit modeTierWeight1Changed();
    });
    composingConfiguration()->modeTierWeight2Changed().onNotify(this, [this]() {
        emit modeTierWeight2Changed();
    });
    composingConfiguration()->modeTierWeight3Changed().onNotify(this, [this]() {
        emit modeTierWeight3Changed();
    });
    composingConfiguration()->modeTierWeight4Changed().onNotify(this, [this]() {
        emit modeTierWeight4Changed();
    });
}

// ── Getters ──────────────────────────────────────────────────────────────────

bool ComposingPreferencesModel::analyzeForChordSymbols() const
{
    return composingConfiguration()->analyzeForChordSymbols();
}

bool ComposingPreferencesModel::analyzeForChordFunction() const
{
    return composingConfiguration()->analyzeForChordFunction();
}

bool ComposingPreferencesModel::inferKeyMode() const
{
    // inferKeyMode is forced on when chord-function analysis is active.
    if (composingConfiguration()->analyzeForChordFunction()) {
        return true;
    }
    return composingConfiguration()->inferKeyMode();
}

int ComposingPreferencesModel::analysisAlternatives() const
{
    return composingConfiguration()->analysisAlternatives();
}

QString ComposingPreferencesModel::tuningSystemKey() const
{
    return QString::fromStdString(composingConfiguration()->tuningSystemKey());
}

bool ComposingPreferencesModel::tonicAnchoredTuning() const
{
    return composingConfiguration()->tonicAnchoredTuning();
}

bool ComposingPreferencesModel::minimizeTuningDeviation() const
{
    return composingConfiguration()->minimizeTuningDeviation();
}

bool ComposingPreferencesModel::annotateTuningOffsets() const
{
    return composingConfiguration()->annotateTuningOffsets();
}

double ComposingPreferencesModel::modeTierWeight1() const
{
    return composingConfiguration()->modeTierWeight1();
}

double ComposingPreferencesModel::modeTierWeight2() const
{
    return composingConfiguration()->modeTierWeight2();
}

double ComposingPreferencesModel::modeTierWeight3() const
{
    return composingConfiguration()->modeTierWeight3();
}

double ComposingPreferencesModel::modeTierWeight4() const
{
    return composingConfiguration()->modeTierWeight4();
}

bool ComposingPreferencesModel::chordStaffWriteChordSymbols() const
{
    return composingConfiguration()->chordStaffWriteChordSymbols();
}

QString ComposingPreferencesModel::chordStaffFunctionNotation() const
{
    return QString::fromStdString(composingConfiguration()->chordStaffFunctionNotation());
}

bool ComposingPreferencesModel::chordStaffWriteKeyAnnotations() const
{
    return composingConfiguration()->chordStaffWriteKeyAnnotations();
}

bool ComposingPreferencesModel::chordStaffHighlightNonDiatonic() const
{
    return composingConfiguration()->chordStaffHighlightNonDiatonic();
}

bool ComposingPreferencesModel::chordStaffWriteCadenceMarkers() const
{
    return composingConfiguration()->chordStaffWriteCadenceMarkers();
}

bool ComposingPreferencesModel::showKeyModeInStatusBar() const
{
    return composingConfiguration()->showKeyModeInStatusBar();
}

bool ComposingPreferencesModel::showChordSymbolsInStatusBar() const
{
    return composingConfiguration()->showChordSymbolsInStatusBar();
}

bool ComposingPreferencesModel::showRomanNumeralsInStatusBar() const
{
    return composingConfiguration()->showRomanNumeralsInStatusBar();
}

bool ComposingPreferencesModel::showNashvilleNumbersInStatusBar() const
{
    return composingConfiguration()->showNashvilleNumbersInStatusBar();
}

// ── Setters ──────────────────────────────────────────────────────────────────

void ComposingPreferencesModel::setAnalyzeForChordSymbols(bool value)
{
    if (analyzeForChordSymbols() == value) {
        return;
    }
    composingConfiguration()->setAnalyzeForChordSymbols(value);
    emit analyzeForChordSymbolsChanged();
}

void ComposingPreferencesModel::setAnalyzeForChordFunction(bool value)
{
    if (analyzeForChordFunction() == value) {
        return;
    }
    composingConfiguration()->setAnalyzeForChordFunction(value);
    emit analyzeForChordFunctionChanged();
}

void ComposingPreferencesModel::setInferKeyMode(bool value)
{
    // Silently ignore if forced on by chord-function analysis.
    if (composingConfiguration()->analyzeForChordFunction()) {
        return;
    }
    if (composingConfiguration()->inferKeyMode() == value) {
        return;
    }
    composingConfiguration()->setInferKeyMode(value);
    emit inferKeyModeChanged();
}

void ComposingPreferencesModel::setAnalysisAlternatives(int count)
{
    if (analysisAlternatives() == count) {
        return;
    }
    composingConfiguration()->setAnalysisAlternatives(count);
    emit analysisAlternativesChanged();
}

void ComposingPreferencesModel::setTuningSystemKey(const QString& key)
{
    if (tuningSystemKey() == key) {
        return;
    }
    composingConfiguration()->setTuningSystemKey(key.toStdString());
    emit tuningSystemKeyChanged();
}

void ComposingPreferencesModel::setTonicAnchoredTuning(bool value)
{
    if (tonicAnchoredTuning() == value) {
        return;
    }
    composingConfiguration()->setTonicAnchoredTuning(value);
    emit tonicAnchoredTuningChanged();
}

void ComposingPreferencesModel::setMinimizeTuningDeviation(bool value)
{
    if (minimizeTuningDeviation() == value) {
        return;
    }
    composingConfiguration()->setMinimizeTuningDeviation(value);
    emit minimizeTuningDeviationChanged();
}

void ComposingPreferencesModel::setAnnotateTuningOffsets(bool value)
{
    if (annotateTuningOffsets() == value) {
        return;
    }
    composingConfiguration()->setAnnotateTuningOffsets(value);
    emit annotateTuningOffsetsChanged();
}

void ComposingPreferencesModel::setModeTierWeight1(double value)
{
    if (qFuzzyCompare(modeTierWeight1(), value)) {
        return;
    }
    composingConfiguration()->setModeTierWeight1(value);
    emit modeTierWeight1Changed();
}

void ComposingPreferencesModel::setModeTierWeight2(double value)
{
    if (qFuzzyCompare(modeTierWeight2(), value)) {
        return;
    }
    composingConfiguration()->setModeTierWeight2(value);
    emit modeTierWeight2Changed();
}

void ComposingPreferencesModel::setModeTierWeight3(double value)
{
    if (qFuzzyCompare(modeTierWeight3(), value)) {
        return;
    }
    composingConfiguration()->setModeTierWeight3(value);
    emit modeTierWeight3Changed();
}

void ComposingPreferencesModel::setModeTierWeight4(double value)
{
    if (qFuzzyCompare(modeTierWeight4(), value)) {
        return;
    }
    composingConfiguration()->setModeTierWeight4(value);
    emit modeTierWeight4Changed();
}

void ComposingPreferencesModel::setChordStaffWriteChordSymbols(bool value)
{
    if (chordStaffWriteChordSymbols() == value) { return; }
    composingConfiguration()->setChordStaffWriteChordSymbols(value);
    emit chordStaffWriteChordSymbolsChanged();
}

void ComposingPreferencesModel::setChordStaffFunctionNotation(const QString& value)
{
    if (chordStaffFunctionNotation() == value) { return; }
    composingConfiguration()->setChordStaffFunctionNotation(value.toStdString());
    emit chordStaffFunctionNotationChanged();
}

void ComposingPreferencesModel::setChordStaffWriteKeyAnnotations(bool value)
{
    if (chordStaffWriteKeyAnnotations() == value) { return; }
    composingConfiguration()->setChordStaffWriteKeyAnnotations(value);
    emit chordStaffWriteKeyAnnotationsChanged();
}

void ComposingPreferencesModel::setChordStaffHighlightNonDiatonic(bool value)
{
    if (chordStaffHighlightNonDiatonic() == value) { return; }
    composingConfiguration()->setChordStaffHighlightNonDiatonic(value);
    emit chordStaffHighlightNonDiatonicChanged();
}

void ComposingPreferencesModel::setChordStaffWriteCadenceMarkers(bool value)
{
    if (chordStaffWriteCadenceMarkers() == value) { return; }
    composingConfiguration()->setChordStaffWriteCadenceMarkers(value);
    emit chordStaffWriteCadenceMarkersChanged();
}

void ComposingPreferencesModel::setShowKeyModeInStatusBar(bool value)
{
    if (showKeyModeInStatusBar() == value) {
        return;
    }
    composingConfiguration()->setShowKeyModeInStatusBar(value);
    emit showKeyModeInStatusBarChanged();
}

void ComposingPreferencesModel::setShowChordSymbolsInStatusBar(bool value)
{
    if (showChordSymbolsInStatusBar() == value) {
        return;
    }
    composingConfiguration()->setShowChordSymbolsInStatusBar(value);
    emit showChordSymbolsInStatusBarChanged();
}

void ComposingPreferencesModel::setShowRomanNumeralsInStatusBar(bool value)
{
    if (showRomanNumeralsInStatusBar() == value) {
        return;
    }
    composingConfiguration()->setShowRomanNumeralsInStatusBar(value);
    emit showRomanNumeralsInStatusBarChanged();
}

void ComposingPreferencesModel::setShowNashvilleNumbersInStatusBar(bool value)
{
    if (showNashvilleNumbersInStatusBar() == value) {
        return;
    }
    composingConfiguration()->setShowNashvilleNumbersInStatusBar(value);
    emit showNashvilleNumbersInStatusBarChanged();
}
