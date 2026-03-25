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
        emit inferKeyModeChanged(); // infer key is also affected
    });
    composingConfiguration()->analyzeForRomanNumeralsChanged().onNotify(this, [this]() {
        emit analyzeForRomanNumeralsChanged();
        emit inferKeyModeChanged();
    });
    composingConfiguration()->inferKeyModeChanged().onNotify(this, [this]() {
        emit inferKeyModeChanged();
    });
    composingConfiguration()->analysisAlternativesChanged().onNotify(this, [this]() {
        emit analysisAlternativesChanged();
    });
    composingConfiguration()->showKeyModeInStatusBarChanged().onNotify(this, [this]() {
        emit showKeyModeInStatusBarChanged();
    });
    composingConfiguration()->statusBarChordSymbolCountChanged().onNotify(this, [this]() {
        emit statusBarChordSymbolCountChanged();
    });
    composingConfiguration()->statusBarRomanNumeralCountChanged().onNotify(this, [this]() {
        emit statusBarRomanNumeralCountChanged();
    });
}

// ── Getters ──────────────────────────────────────────────────────────────────

bool ComposingPreferencesModel::analyzeForChordSymbols() const
{
    return composingConfiguration()->analyzeForChordSymbols();
}

bool ComposingPreferencesModel::analyzeForRomanNumerals() const
{
    return composingConfiguration()->analyzeForRomanNumerals();
}

bool ComposingPreferencesModel::inferKeyMode() const
{
    // inferKeyMode is forced on when either analysis mode is active.
    if (composingConfiguration()->analyzeForChordSymbols()
        || composingConfiguration()->analyzeForRomanNumerals()) {
        return true;
    }
    return composingConfiguration()->inferKeyMode();
}

int ComposingPreferencesModel::analysisAlternatives() const
{
    return composingConfiguration()->analysisAlternatives();
}

bool ComposingPreferencesModel::showKeyModeInStatusBar() const
{
    return composingConfiguration()->showKeyModeInStatusBar();
}

int ComposingPreferencesModel::statusBarChordSymbolCount() const
{
    return composingConfiguration()->statusBarChordSymbolCount();
}

int ComposingPreferencesModel::statusBarRomanNumeralCount() const
{
    return composingConfiguration()->statusBarRomanNumeralCount();
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

void ComposingPreferencesModel::setAnalyzeForRomanNumerals(bool value)
{
    if (analyzeForRomanNumerals() == value) {
        return;
    }
    composingConfiguration()->setAnalyzeForRomanNumerals(value);
    emit analyzeForRomanNumeralsChanged();
}

void ComposingPreferencesModel::setInferKeyMode(bool value)
{
    // Silently ignore if forced on by active analysis.
    if (composingConfiguration()->analyzeForChordSymbols()
        || composingConfiguration()->analyzeForRomanNumerals()) {
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

void ComposingPreferencesModel::setShowKeyModeInStatusBar(bool value)
{
    if (showKeyModeInStatusBar() == value) {
        return;
    }
    composingConfiguration()->setShowKeyModeInStatusBar(value);
    emit showKeyModeInStatusBarChanged();
}

void ComposingPreferencesModel::setStatusBarChordSymbolCount(int count)
{
    if (statusBarChordSymbolCount() == count) {
        return;
    }
    composingConfiguration()->setStatusBarChordSymbolCount(count);
    emit statusBarChordSymbolCountChanged();
}

void ComposingPreferencesModel::setStatusBarRomanNumeralCount(int count)
{
    if (statusBarRomanNumeralCount() == count) {
        return;
    }
    composingConfiguration()->setStatusBarRomanNumeralCount(count);
    emit statusBarRomanNumeralCountChanged();
}
