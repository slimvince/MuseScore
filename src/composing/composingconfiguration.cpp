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

static const Settings::Key ANALYZE_FOR_CHORD_SYMBOLS(module_name,   "composing/analyzeForChordSymbols");
static const Settings::Key ANALYZE_FOR_CHORD_FUNCTION(module_name,  "composing/analyzeForChordFunction");
static const Settings::Key INFER_KEY_MODE(module_name,              "composing/inferKeyMode");
static const Settings::Key ANALYSIS_ALTERNATIVES(module_name,       "composing/analysisAlternatives");
static const Settings::Key TUNING_SYSTEM_KEY(module_name,           "composing/tuningSystemKey");
static const Settings::Key TONIC_ANCHORED_TUNING(module_name,       "composing/tonicAnchoredTuning");
static const Settings::Key MINIMIZE_TUNING_DEVIATION(module_name,   "composing/minimizeTuningDeviation");
static const Settings::Key ANNOTATE_TUNING_OFFSETS(module_name,     "composing/annotateTuningOffsets");
static const Settings::Key SHOW_KEY_MODE_IN_STATUS_BAR(module_name,       "composing/showKeyModeInStatusBar");
static const Settings::Key SHOW_CHORD_SYMBOLS_IN_STATUS_BAR(module_name,  "composing/showChordSymbolsInStatusBar");
static const Settings::Key SHOW_ROMAN_NUMERALS_IN_STATUS_BAR(module_name, "composing/showRomanNumeralsInStatusBar");
static const Settings::Key SHOW_NASHVILLE_NUMBERS_IN_STATUS_BAR(module_name, "composing/showNashvilleNumbersInStatusBar");
static const Settings::Key CHORD_STAFF_WRITE_CHORD_SYMBOLS(module_name,   "composing/chordStaffWriteChordSymbols");
static const Settings::Key CHORD_STAFF_FUNCTION_NOTATION(module_name,    "composing/chordStaffFunctionNotation");
static const Settings::Key CHORD_STAFF_WRITE_KEY_ANNOTATIONS(module_name, "composing/chordStaffWriteKeyAnnotations");
static const Settings::Key CHORD_STAFF_HIGHLIGHT_NON_DIATONIC(module_name, "composing/chordStaffHighlightNonDiatonic");
static const Settings::Key CHORD_STAFF_WRITE_CADENCE_MARKERS(module_name,  "composing/chordStaffWriteCadenceMarkers");
static const Settings::Key MODE_TIER_WEIGHT_1(module_name, "composing/modeTierWeight1");
static const Settings::Key MODE_TIER_WEIGHT_2(module_name, "composing/modeTierWeight2");
static const Settings::Key MODE_TIER_WEIGHT_3(module_name, "composing/modeTierWeight3");
static const Settings::Key MODE_TIER_WEIGHT_4(module_name, "composing/modeTierWeight4");

void ComposingConfiguration::init()
{
    settings()->setDefaultValue(ANALYZE_FOR_CHORD_SYMBOLS, Val(true));
    settings()->valueChanged(ANALYZE_FOR_CHORD_SYMBOLS).onReceive(nullptr, [this](const Val&) {
        m_analyzeForChordSymbolsChanged.notify();
    });

    settings()->setDefaultValue(ANALYZE_FOR_CHORD_FUNCTION, Val(false));
    settings()->valueChanged(ANALYZE_FOR_CHORD_FUNCTION).onReceive(nullptr, [this](const Val&) {
        m_analyzeForChordFunctionChanged.notify();
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

    settings()->setDefaultValue(TONIC_ANCHORED_TUNING, Val(true));
    settings()->valueChanged(TONIC_ANCHORED_TUNING).onReceive(nullptr, [this](const Val&) {
        m_tonicAnchoredTuningChanged.notify();
    });

    settings()->setDefaultValue(MINIMIZE_TUNING_DEVIATION, Val(false));
    settings()->valueChanged(MINIMIZE_TUNING_DEVIATION).onReceive(nullptr, [this](const Val&) {
        m_minimizeTuningDeviationChanged.notify();
    });

    settings()->setDefaultValue(ANNOTATE_TUNING_OFFSETS, Val(false));
    settings()->valueChanged(ANNOTATE_TUNING_OFFSETS).onReceive(nullptr, [this](const Val&) {
        m_annotateTuningOffsetsChanged.notify();
    });

    settings()->setDefaultValue(SHOW_KEY_MODE_IN_STATUS_BAR, Val(true));
    settings()->valueChanged(SHOW_KEY_MODE_IN_STATUS_BAR).onReceive(nullptr, [this](const Val&) {
        m_showKeyModeInStatusBarChanged.notify();
    });

    settings()->setDefaultValue(SHOW_CHORD_SYMBOLS_IN_STATUS_BAR, Val(true));
    settings()->valueChanged(SHOW_CHORD_SYMBOLS_IN_STATUS_BAR).onReceive(nullptr, [this](const Val&) {
        m_showChordSymbolsInStatusBarChanged.notify();
    });

    settings()->setDefaultValue(SHOW_ROMAN_NUMERALS_IN_STATUS_BAR, Val(false));
    settings()->valueChanged(SHOW_ROMAN_NUMERALS_IN_STATUS_BAR).onReceive(nullptr, [this](const Val&) {
        m_showRomanNumeralsInStatusBarChanged.notify();
    });

    settings()->setDefaultValue(SHOW_NASHVILLE_NUMBERS_IN_STATUS_BAR, Val(false));
    settings()->valueChanged(SHOW_NASHVILLE_NUMBERS_IN_STATUS_BAR).onReceive(nullptr, [this](const Val&) {
        m_showNashvilleNumbersInStatusBarChanged.notify();
    });

    settings()->setDefaultValue(CHORD_STAFF_WRITE_CHORD_SYMBOLS, Val(true));
    settings()->valueChanged(CHORD_STAFF_WRITE_CHORD_SYMBOLS).onReceive(nullptr, [this](const Val&) {
        m_chordStaffWriteChordSymbolsChanged.notify();
    });

    settings()->setDefaultValue(CHORD_STAFF_FUNCTION_NOTATION, Val(std::string("roman")));
    settings()->valueChanged(CHORD_STAFF_FUNCTION_NOTATION).onReceive(nullptr, [this](const Val&) {
        m_chordStaffFunctionNotationChanged.notify();
    });

    settings()->setDefaultValue(CHORD_STAFF_WRITE_KEY_ANNOTATIONS, Val(true));
    settings()->valueChanged(CHORD_STAFF_WRITE_KEY_ANNOTATIONS).onReceive(nullptr, [this](const Val&) {
        m_chordStaffWriteKeyAnnotationsChanged.notify();
    });

    settings()->setDefaultValue(CHORD_STAFF_HIGHLIGHT_NON_DIATONIC, Val(true));
    settings()->valueChanged(CHORD_STAFF_HIGHLIGHT_NON_DIATONIC).onReceive(nullptr, [this](const Val&) {
        m_chordStaffHighlightNonDiatonicChanged.notify();
    });

    settings()->setDefaultValue(CHORD_STAFF_WRITE_CADENCE_MARKERS, Val(true));
    settings()->valueChanged(CHORD_STAFF_WRITE_CADENCE_MARKERS).onReceive(nullptr, [this](const Val&) {
        m_chordStaffWriteCadenceMarkersChanged.notify();
    });

    settings()->setDefaultValue(MODE_TIER_WEIGHT_1, Val(1.0));
    settings()->valueChanged(MODE_TIER_WEIGHT_1).onReceive(nullptr, [this](const Val&) {
        m_modeTierWeight1Changed.notify();
    });

    settings()->setDefaultValue(MODE_TIER_WEIGHT_2, Val(-0.5));
    settings()->valueChanged(MODE_TIER_WEIGHT_2).onReceive(nullptr, [this](const Val&) {
        m_modeTierWeight2Changed.notify();
    });

    settings()->setDefaultValue(MODE_TIER_WEIGHT_3, Val(-1.5));
    settings()->valueChanged(MODE_TIER_WEIGHT_3).onReceive(nullptr, [this](const Val&) {
        m_modeTierWeight3Changed.notify();
    });

    settings()->setDefaultValue(MODE_TIER_WEIGHT_4, Val(-3.0));
    settings()->valueChanged(MODE_TIER_WEIGHT_4).onReceive(nullptr, [this](const Val&) {
        m_modeTierWeight4Changed.notify();
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

// ── analyzeForChordFunction ──────────────────────────────────────────────────

bool ComposingConfiguration::analyzeForChordFunction() const
{
    return settings()->value(ANALYZE_FOR_CHORD_FUNCTION).toBool();
}

void ComposingConfiguration::setAnalyzeForChordFunction(bool value)
{
    settings()->setSharedValue(ANALYZE_FOR_CHORD_FUNCTION, Val(value));
}

muse::async::Notification ComposingConfiguration::analyzeForChordFunctionChanged() const
{
    return m_analyzeForChordFunctionChanged;
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

// ── tonicAnchoredTuning ──────────────────────────────────────────────────────

bool ComposingConfiguration::tonicAnchoredTuning() const
{
    return settings()->value(TONIC_ANCHORED_TUNING).toBool();
}

void ComposingConfiguration::setTonicAnchoredTuning(bool value)
{
    settings()->setSharedValue(TONIC_ANCHORED_TUNING, Val(value));
}

muse::async::Notification ComposingConfiguration::tonicAnchoredTuningChanged() const
{
    return m_tonicAnchoredTuningChanged;
}

// ── minimizeTuningDeviation ──────────────────────────────────────────────────

bool ComposingConfiguration::minimizeTuningDeviation() const
{
    return settings()->value(MINIMIZE_TUNING_DEVIATION).toBool();
}

void ComposingConfiguration::setMinimizeTuningDeviation(bool value)
{
    settings()->setSharedValue(MINIMIZE_TUNING_DEVIATION, Val(value));
}

muse::async::Notification ComposingConfiguration::minimizeTuningDeviationChanged() const
{
    return m_minimizeTuningDeviationChanged;
}

// ── annotateTuningOffsets ────────────────────────────────────────────────────

bool ComposingConfiguration::annotateTuningOffsets() const
{
    return settings()->value(ANNOTATE_TUNING_OFFSETS).toBool();
}

void ComposingConfiguration::setAnnotateTuningOffsets(bool value)
{
    settings()->setSharedValue(ANNOTATE_TUNING_OFFSETS, Val(value));
}

muse::async::Notification ComposingConfiguration::annotateTuningOffsetsChanged() const
{
    return m_annotateTuningOffsetsChanged;
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

// ── showChordSymbolsInStatusBar ──────────────────────────────────────────────

bool ComposingConfiguration::showChordSymbolsInStatusBar() const
{
    return settings()->value(SHOW_CHORD_SYMBOLS_IN_STATUS_BAR).toBool();
}

void ComposingConfiguration::setShowChordSymbolsInStatusBar(bool value)
{
    settings()->setSharedValue(SHOW_CHORD_SYMBOLS_IN_STATUS_BAR, Val(value));
}

muse::async::Notification ComposingConfiguration::showChordSymbolsInStatusBarChanged() const
{
    return m_showChordSymbolsInStatusBarChanged;
}

// ── showRomanNumeralsInStatusBar ─────────────────────────────────────────────

bool ComposingConfiguration::showRomanNumeralsInStatusBar() const
{
    return settings()->value(SHOW_ROMAN_NUMERALS_IN_STATUS_BAR).toBool();
}

void ComposingConfiguration::setShowRomanNumeralsInStatusBar(bool value)
{
    settings()->setSharedValue(SHOW_ROMAN_NUMERALS_IN_STATUS_BAR, Val(value));
}

muse::async::Notification ComposingConfiguration::showRomanNumeralsInStatusBarChanged() const
{
    return m_showRomanNumeralsInStatusBarChanged;
}

// ── showNashvilleNumbersInStatusBar ──────────────────────────────────────────

bool ComposingConfiguration::showNashvilleNumbersInStatusBar() const
{
    return settings()->value(SHOW_NASHVILLE_NUMBERS_IN_STATUS_BAR).toBool();
}

void ComposingConfiguration::setShowNashvilleNumbersInStatusBar(bool value)
{
    settings()->setSharedValue(SHOW_NASHVILLE_NUMBERS_IN_STATUS_BAR, Val(value));
}

muse::async::Notification ComposingConfiguration::showNashvilleNumbersInStatusBarChanged() const
{
    return m_showNashvilleNumbersInStatusBarChanged;
}

// ── chordStaffWriteChordSymbols ──────────────────────────────────────────────

bool ComposingConfiguration::chordStaffWriteChordSymbols() const
{
    return settings()->value(CHORD_STAFF_WRITE_CHORD_SYMBOLS).toBool();
}

void ComposingConfiguration::setChordStaffWriteChordSymbols(bool value)
{
    settings()->setSharedValue(CHORD_STAFF_WRITE_CHORD_SYMBOLS, Val(value));
}

muse::async::Notification ComposingConfiguration::chordStaffWriteChordSymbolsChanged() const
{
    return m_chordStaffWriteChordSymbolsChanged;
}

// ── chordStaffFunctionNotation ───────────────────────────────────────────────

std::string ComposingConfiguration::chordStaffFunctionNotation() const
{
    return settings()->value(CHORD_STAFF_FUNCTION_NOTATION).toString();
}

void ComposingConfiguration::setChordStaffFunctionNotation(const std::string& value)
{
    settings()->setSharedValue(CHORD_STAFF_FUNCTION_NOTATION, Val(value));
}

muse::async::Notification ComposingConfiguration::chordStaffFunctionNotationChanged() const
{
    return m_chordStaffFunctionNotationChanged;
}

// ── chordStaffWriteKeyAnnotations ────────────────────────────────────────────

bool ComposingConfiguration::chordStaffWriteKeyAnnotations() const
{
    return settings()->value(CHORD_STAFF_WRITE_KEY_ANNOTATIONS).toBool();
}

void ComposingConfiguration::setChordStaffWriteKeyAnnotations(bool value)
{
    settings()->setSharedValue(CHORD_STAFF_WRITE_KEY_ANNOTATIONS, Val(value));
}

muse::async::Notification ComposingConfiguration::chordStaffWriteKeyAnnotationsChanged() const
{
    return m_chordStaffWriteKeyAnnotationsChanged;
}

// ── chordStaffHighlightNonDiatonic ───────────────────────────────────────────

bool ComposingConfiguration::chordStaffHighlightNonDiatonic() const
{
    return settings()->value(CHORD_STAFF_HIGHLIGHT_NON_DIATONIC).toBool();
}

void ComposingConfiguration::setChordStaffHighlightNonDiatonic(bool value)
{
    settings()->setSharedValue(CHORD_STAFF_HIGHLIGHT_NON_DIATONIC, Val(value));
}

muse::async::Notification ComposingConfiguration::chordStaffHighlightNonDiatonicChanged() const
{
    return m_chordStaffHighlightNonDiatonicChanged;
}

// ── chordStaffWriteCadenceMarkers ────────────────────────────────────────────

bool ComposingConfiguration::chordStaffWriteCadenceMarkers() const
{
    return settings()->value(CHORD_STAFF_WRITE_CADENCE_MARKERS).toBool();
}

void ComposingConfiguration::setChordStaffWriteCadenceMarkers(bool value)
{
    settings()->setSharedValue(CHORD_STAFF_WRITE_CADENCE_MARKERS, Val(value));
}

muse::async::Notification ComposingConfiguration::chordStaffWriteCadenceMarkersChanged() const
{
    return m_chordStaffWriteCadenceMarkersChanged;
}

// ── modeTierWeight1 ─────────────────────────────────────────────────────────

double ComposingConfiguration::modeTierWeight1() const
{
    return settings()->value(MODE_TIER_WEIGHT_1).toDouble();
}

void ComposingConfiguration::setModeTierWeight1(double value)
{
    settings()->setSharedValue(MODE_TIER_WEIGHT_1, Val(value));
}

muse::async::Notification ComposingConfiguration::modeTierWeight1Changed() const
{
    return m_modeTierWeight1Changed;
}

// ── modeTierWeight2 ─────────────────────────────────────────────────────────

double ComposingConfiguration::modeTierWeight2() const
{
    return settings()->value(MODE_TIER_WEIGHT_2).toDouble();
}

void ComposingConfiguration::setModeTierWeight2(double value)
{
    settings()->setSharedValue(MODE_TIER_WEIGHT_2, Val(value));
}

muse::async::Notification ComposingConfiguration::modeTierWeight2Changed() const
{
    return m_modeTierWeight2Changed;
}

// ── modeTierWeight3 ─────────────────────────────────────────────────────────

double ComposingConfiguration::modeTierWeight3() const
{
    return settings()->value(MODE_TIER_WEIGHT_3).toDouble();
}

void ComposingConfiguration::setModeTierWeight3(double value)
{
    settings()->setSharedValue(MODE_TIER_WEIGHT_3, Val(value));
}

muse::async::Notification ComposingConfiguration::modeTierWeight3Changed() const
{
    return m_modeTierWeight3Changed;
}

// ── modeTierWeight4 ─────────────────────────────────────────────────────────

double ComposingConfiguration::modeTierWeight4() const
{
    return settings()->value(MODE_TIER_WEIGHT_4).toDouble();
}

void ComposingConfiguration::setModeTierWeight4(double value)
{
    settings()->setSharedValue(MODE_TIER_WEIGHT_4, Val(value));
}

muse::async::Notification ComposingConfiguration::modeTierWeight4Changed() const
{
    return m_modeTierWeight4Changed;
}
