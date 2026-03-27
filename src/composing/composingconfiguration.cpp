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
#include "composingconfiguration.h"

#include "settings.h"

using namespace mu::composing;
using namespace muse;

static const std::string module_name("composing");

static const Settings::Key ANALYZE_FOR_CHORD_SYMBOLS(module_name,  "composing/analyzeForChordSymbols");
static const Settings::Key ANALYZE_FOR_ROMAN_NUMERALS(module_name, "composing/analyzeForRomanNumerals");
static const Settings::Key INFER_KEY_MODE(module_name,             "composing/inferKeyMode");
static const Settings::Key ANALYSIS_ALTERNATIVES(module_name,      "composing/analysisAlternatives");
static const Settings::Key TUNING_SYSTEM_KEY(module_name,          "composing/tuningSystemKey");
static const Settings::Key SHOW_KEY_MODE_IN_STATUS_BAR(module_name,    "composing/showKeyModeInStatusBar");
static const Settings::Key STATUS_BAR_CHORD_SYMBOL_COUNT(module_name,  "composing/statusBarChordSymbolCount");
static const Settings::Key STATUS_BAR_ROMAN_NUMERAL_COUNT(module_name, "composing/statusBarRomanNumeralCount");

void ComposingConfiguration::init()
{
    settings()->setDefaultValue(ANALYZE_FOR_CHORD_SYMBOLS,  Val(true));
    settings()->valueChanged(ANALYZE_FOR_CHORD_SYMBOLS).onReceive(nullptr, [this](const Val&) {
        m_analyzeForChordSymbolsChanged.notify();
    });

    settings()->setDefaultValue(ANALYZE_FOR_ROMAN_NUMERALS, Val(false));
    settings()->valueChanged(ANALYZE_FOR_ROMAN_NUMERALS).onReceive(nullptr, [this](const Val&) {
        m_analyzeForRomanNumeralsChanged.notify();
    });

    settings()->setDefaultValue(INFER_KEY_MODE, Val(true));
    settings()->valueChanged(INFER_KEY_MODE).onReceive(nullptr, [this](const Val&) {
        m_inferKeyModeChanged.notify();
    });

    settings()->setDefaultValue(ANALYSIS_ALTERNATIVES, Val(3));
    settings()->valueChanged(ANALYSIS_ALTERNATIVES).onReceive(nullptr, [this](const Val&) {
        m_analysisAlternativesChanged.notify();
    });

    settings()->setDefaultValue(TUNING_SYSTEM_KEY, Val(std::string("equal")));
    settings()->valueChanged(TUNING_SYSTEM_KEY).onReceive(nullptr, [this](const Val&) {
        m_tuningSystemKeyChanged.notify();
    });

    settings()->setDefaultValue(SHOW_KEY_MODE_IN_STATUS_BAR, Val(true));
    settings()->valueChanged(SHOW_KEY_MODE_IN_STATUS_BAR).onReceive(nullptr, [this](const Val&) {
        m_showKeyModeInStatusBarChanged.notify();
    });

    settings()->setDefaultValue(STATUS_BAR_CHORD_SYMBOL_COUNT, Val(1));
    settings()->valueChanged(STATUS_BAR_CHORD_SYMBOL_COUNT).onReceive(nullptr, [this](const Val&) {
        m_statusBarChordSymbolCountChanged.notify();
    });

    settings()->setDefaultValue(STATUS_BAR_ROMAN_NUMERAL_COUNT, Val(0));
    settings()->valueChanged(STATUS_BAR_ROMAN_NUMERAL_COUNT).onReceive(nullptr, [this](const Val&) {
        m_statusBarRomanNumeralCountChanged.notify();
    });
}

// ── analyzeForChordSymbols ───────────────────────────────────────────────────

bool ComposingConfiguration::analyzeForChordSymbols() const
{
    return settings()->value(ANALYZE_FOR_CHORD_SYMBOLS).toBool();
}

void ComposingConfiguration::setAnalyzeForChordSymbols(bool value)
{
    settings()->setSharedValue(ANALYZE_FOR_CHORD_SYMBOLS, Val(value));
}

muse::async::Notification ComposingConfiguration::analyzeForChordSymbolsChanged() const
{
    return m_analyzeForChordSymbolsChanged;
}

// ── analyzeForRomanNumerals ──────────────────────────────────────────────────

bool ComposingConfiguration::analyzeForRomanNumerals() const
{
    return settings()->value(ANALYZE_FOR_ROMAN_NUMERALS).toBool();
}

void ComposingConfiguration::setAnalyzeForRomanNumerals(bool value)
{
    settings()->setSharedValue(ANALYZE_FOR_ROMAN_NUMERALS, Val(value));
}

muse::async::Notification ComposingConfiguration::analyzeForRomanNumeralsChanged() const
{
    return m_analyzeForRomanNumeralsChanged;
}

// ── inferKeyMode ─────────────────────────────────────────────────────────────

bool ComposingConfiguration::inferKeyMode() const
{
    return settings()->value(INFER_KEY_MODE).toBool();
}

void ComposingConfiguration::setInferKeyMode(bool value)
{
    settings()->setSharedValue(INFER_KEY_MODE, Val(value));
}

muse::async::Notification ComposingConfiguration::inferKeyModeChanged() const
{
    return m_inferKeyModeChanged;
}

// ── analysisAlternatives ─────────────────────────────────────────────────────

int ComposingConfiguration::analysisAlternatives() const
{
    return settings()->value(ANALYSIS_ALTERNATIVES).toInt();
}

void ComposingConfiguration::setAnalysisAlternatives(int count)
{
    settings()->setSharedValue(ANALYSIS_ALTERNATIVES, Val(count));
}

muse::async::Notification ComposingConfiguration::analysisAlternativesChanged() const
{
    return m_analysisAlternativesChanged;
}

// ── tuningSystemKey ──────────────────────────────────────────────────────────

std::string ComposingConfiguration::tuningSystemKey() const
{
    return settings()->value(TUNING_SYSTEM_KEY).toString();
}

void ComposingConfiguration::setTuningSystemKey(const std::string& key)
{
    settings()->setSharedValue(TUNING_SYSTEM_KEY, Val(key));
}

muse::async::Notification ComposingConfiguration::tuningSystemKeyChanged() const
{
    return m_tuningSystemKeyChanged;
}

// ── showKeyModeInStatusBar ───────────────────────────────────────────────────

bool ComposingConfiguration::showKeyModeInStatusBar() const
{
    return settings()->value(SHOW_KEY_MODE_IN_STATUS_BAR).toBool();
}

void ComposingConfiguration::setShowKeyModeInStatusBar(bool value)
{
    settings()->setSharedValue(SHOW_KEY_MODE_IN_STATUS_BAR, Val(value));
}

muse::async::Notification ComposingConfiguration::showKeyModeInStatusBarChanged() const
{
    return m_showKeyModeInStatusBarChanged;
}

// ── statusBarChordSymbolCount ────────────────────────────────────────────────

int ComposingConfiguration::statusBarChordSymbolCount() const
{
    return settings()->value(STATUS_BAR_CHORD_SYMBOL_COUNT).toInt();
}

void ComposingConfiguration::setStatusBarChordSymbolCount(int count)
{
    settings()->setSharedValue(STATUS_BAR_CHORD_SYMBOL_COUNT, Val(count));
}

muse::async::Notification ComposingConfiguration::statusBarChordSymbolCountChanged() const
{
    return m_statusBarChordSymbolCountChanged;
}

// ── statusBarRomanNumeralCount ───────────────────────────────────────────────

int ComposingConfiguration::statusBarRomanNumeralCount() const
{
    return settings()->value(STATUS_BAR_ROMAN_NUMERAL_COUNT).toInt();
}

void ComposingConfiguration::setStatusBarRomanNumeralCount(int count)
{
    settings()->setSharedValue(STATUS_BAR_ROMAN_NUMERAL_COUNT, Val(count));
}

muse::async::Notification ComposingConfiguration::statusBarRomanNumeralCountChanged() const
{
    return m_statusBarRomanNumeralCountChanged;
}
