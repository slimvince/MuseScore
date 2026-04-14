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

#include <algorithm>
#include <cmath>

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
static const Settings::Key TUNING_MODE(module_name,                  "composing/tuningMode");
static const Settings::Key ALLOW_SPLIT_SLUR_OF_SUSTAINED_EVENTS(module_name, "composing/allowSplitSlurOfSustainedEvents");
static const Settings::Key MINIMIZE_TUNING_DEVIATION(module_name,   "composing/minimizeTuningDeviation");
static const Settings::Key ANNOTATE_TUNING_OFFSETS(module_name,     "composing/annotateTuningOffsets");
static const Settings::Key ANNOTATE_DRIFT_AT_BOUNDARIES(module_name, "composing/annotateDriftAtBoundaries");
static const Settings::Key USE_REGIONAL_ACCUMULATION(module_name,    "composing/useRegionalAccumulation");
static const Settings::Key ONSET_BOUNDARY_THRESHOLD(module_name,     "composing/onsetBoundaryThreshold");
static const Settings::Key MODE_NAME_CONFIDENCE_THRESHOLD(module_name, "composing/modeNameConfidenceThreshold");
static const Settings::Key MINIMUM_DISPLAY_DURATION_BEATS(module_name, "composing/minimumDisplayDurationBeats");
static const Settings::Key MIN_KEY_STABILITY_BEATS(module_name, "composing/minKeyStabilityBeats");
static const Settings::Key SHOW_KEY_MODE_IN_STATUS_BAR(module_name,       "composing/showKeyModeInStatusBar");
static const Settings::Key SHOW_CHORD_SYMBOLS_IN_STATUS_BAR(module_name,  "composing/showChordSymbolsInStatusBar");
static const Settings::Key SHOW_ROMAN_NUMERALS_IN_STATUS_BAR(module_name, "composing/showRomanNumeralsInStatusBar");
static const Settings::Key SHOW_NASHVILLE_NUMBERS_IN_STATUS_BAR(module_name, "composing/showNashvilleNumbersInStatusBar");
static const Settings::Key CHORD_STAFF_WRITE_CHORD_SYMBOLS(module_name,   "composing/chordStaffWriteChordSymbols");
static const Settings::Key CHORD_STAFF_FUNCTION_NOTATION(module_name,    "composing/chordStaffFunctionNotation");
static const Settings::Key CHORD_STAFF_WRITE_KEY_ANNOTATIONS(module_name, "composing/chordStaffWriteKeyAnnotations");
static const Settings::Key CHORD_STAFF_HIGHLIGHT_NON_DIATONIC(module_name, "composing/chordStaffHighlightNonDiatonic");
static const Settings::Key CHORD_STAFF_WRITE_CADENCE_MARKERS(module_name,  "composing/chordStaffWriteCadenceMarkers");
// ── Mode prior Settings::Keys ────────────────────────────────────────────────
// Diatonic
static const Settings::Key MODE_PRIOR_IONIAN(module_name,     "composing/modePriorIonian");
static const Settings::Key MODE_PRIOR_DORIAN(module_name,     "composing/modePriorDorian");
static const Settings::Key MODE_PRIOR_PHRYGIAN(module_name,   "composing/modePriorPhrygian");
static const Settings::Key MODE_PRIOR_LYDIAN(module_name,     "composing/modePriorLydian");
static const Settings::Key MODE_PRIOR_MIXOLYDIAN(module_name, "composing/modePriorMixolydian");
static const Settings::Key MODE_PRIOR_AEOLIAN(module_name,    "composing/modePriorAeolian");
static const Settings::Key MODE_PRIOR_LOCRIAN(module_name,    "composing/modePriorLocrian");
// Melodic minor family
static const Settings::Key MODE_PRIOR_MELODIC_MINOR(module_name,  "composing/modePriorMelodicMinor");
static const Settings::Key MODE_PRIOR_DORIAN_B2(module_name,      "composing/modePriorDorianB2");
static const Settings::Key MODE_PRIOR_LYDIAN_AUGMENTED(module_name, "composing/modePriorLydianAugmented");
static const Settings::Key MODE_PRIOR_LYDIAN_DOMINANT(module_name,  "composing/modePriorLydianDominant");
static const Settings::Key MODE_PRIOR_MIXOLYDIAN_B6(module_name,  "composing/modePriorMixolydianB6");
static const Settings::Key MODE_PRIOR_AEOLIAN_B5(module_name,     "composing/modePriorAeolianB5");
static const Settings::Key MODE_PRIOR_ALTERED(module_name,        "composing/modePriorAltered");
// Harmonic minor family
static const Settings::Key MODE_PRIOR_HARMONIC_MINOR(module_name, "composing/modePriorHarmonicMinor");
static const Settings::Key MODE_PRIOR_LOCRIAN_SHARP6(module_name, "composing/modePriorLocrianSharp6");
static const Settings::Key MODE_PRIOR_IONIAN_SHARP5(module_name,  "composing/modePriorIonianSharp5");
static const Settings::Key MODE_PRIOR_DORIAN_SHARP4(module_name,  "composing/modePriorDorianSharp4");
static const Settings::Key MODE_PRIOR_PHRYGIAN_DOMINANT(module_name, "composing/modePriorPhrygianDominant");
static const Settings::Key MODE_PRIOR_LYDIAN_SHARP2(module_name,  "composing/modePriorLydianSharp2");
static const Settings::Key MODE_PRIOR_ALTERED_DOM_BB7(module_name,"composing/modePriorAlteredDomBB7");

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

    settings()->setDefaultValue(TUNING_MODE,
        Val(static_cast<int>(mu::composing::intonation::TuningMode::TonicAnchored)));
    settings()->valueChanged(TUNING_MODE).onReceive(nullptr, [this](const Val&) {
        m_tuningModeChanged.notify();
    });

    settings()->setDefaultValue(ALLOW_SPLIT_SLUR_OF_SUSTAINED_EVENTS, Val(true));
    settings()->valueChanged(ALLOW_SPLIT_SLUR_OF_SUSTAINED_EVENTS).onReceive(nullptr, [this](const Val&) {
        m_allowSplitSlurOfSustainedEventsChanged.notify();
    });

    settings()->setDefaultValue(MINIMIZE_TUNING_DEVIATION, Val(false));
    settings()->valueChanged(MINIMIZE_TUNING_DEVIATION).onReceive(nullptr, [this](const Val&) {
        m_minimizeTuningDeviationChanged.notify();
    });

    settings()->setDefaultValue(ANNOTATE_TUNING_OFFSETS, Val(false));
    settings()->valueChanged(ANNOTATE_TUNING_OFFSETS).onReceive(nullptr, [this](const Val&) {
        m_annotateTuningOffsetsChanged.notify();
    });

    settings()->setDefaultValue(ANNOTATE_DRIFT_AT_BOUNDARIES, Val(false));
    settings()->valueChanged(ANNOTATE_DRIFT_AT_BOUNDARIES).onReceive(nullptr, [this](const Val&) {
        m_annotateDriftAtBoundariesChanged.notify();
    });

    settings()->setDefaultValue(USE_REGIONAL_ACCUMULATION, Val(true));
    settings()->valueChanged(USE_REGIONAL_ACCUMULATION).onReceive(nullptr, [this](const Val&) {
        m_useRegionalAccumulationChanged.notify();
    });

    settings()->setDefaultValue(ONSET_BOUNDARY_THRESHOLD, Val(0.25));
    settings()->valueChanged(ONSET_BOUNDARY_THRESHOLD).onReceive(nullptr, [this](const Val&) {
        m_onsetBoundaryThresholdChanged.notify();
    });

    settings()->setDefaultValue(MODE_NAME_CONFIDENCE_THRESHOLD, Val(0.35));
    settings()->valueChanged(MODE_NAME_CONFIDENCE_THRESHOLD).onReceive(nullptr, [this](const Val&) {
        m_modeNameConfidenceThresholdChanged.notify();
    });

    settings()->setDefaultValue(MINIMUM_DISPLAY_DURATION_BEATS, Val(0.5));
    settings()->valueChanged(MINIMUM_DISPLAY_DURATION_BEATS).onReceive(nullptr, [this](const Val&) {
        m_minimumDisplayDurationBeatsChanged.notify();
    });

    settings()->setDefaultValue(MIN_KEY_STABILITY_BEATS, Val(8.0));
    settings()->valueChanged(MIN_KEY_STABILITY_BEATS).onReceive(nullptr, [this](const Val&) {
        m_minKeyStabilityBeatsChanged.notify();
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

    // ── Mode priors — diatonic ───────────────────────────────────────────────
    settings()->setDefaultValue(MODE_PRIOR_IONIAN, Val(1.20));
    settings()->valueChanged(MODE_PRIOR_IONIAN).onReceive(nullptr, [this](const Val&) {
        m_modePriorIonianChanged.notify();
    });
    settings()->setDefaultValue(MODE_PRIOR_DORIAN, Val(-0.50));
    settings()->valueChanged(MODE_PRIOR_DORIAN).onReceive(nullptr, [this](const Val&) {
        m_modePriorDorianChanged.notify();
    });
    settings()->setDefaultValue(MODE_PRIOR_PHRYGIAN, Val(-1.50));
    settings()->valueChanged(MODE_PRIOR_PHRYGIAN).onReceive(nullptr, [this](const Val&) {
        m_modePriorPhrygianChanged.notify();
    });
    settings()->setDefaultValue(MODE_PRIOR_LYDIAN, Val(0.00));
    settings()->valueChanged(MODE_PRIOR_LYDIAN).onReceive(nullptr, [this](const Val&) {
        m_modePriorLydianChanged.notify();
    });
    settings()->setDefaultValue(MODE_PRIOR_MIXOLYDIAN, Val(-0.20));
    settings()->valueChanged(MODE_PRIOR_MIXOLYDIAN).onReceive(nullptr, [this](const Val&) {
        m_modePriorMixolydianChanged.notify();
    });
    settings()->setDefaultValue(MODE_PRIOR_AEOLIAN, Val(1.00));
    settings()->valueChanged(MODE_PRIOR_AEOLIAN).onReceive(nullptr, [this](const Val&) {
        m_modePriorAeolianChanged.notify();
    });
    settings()->setDefaultValue(MODE_PRIOR_LOCRIAN, Val(-3.50));
    settings()->valueChanged(MODE_PRIOR_LOCRIAN).onReceive(nullptr, [this](const Val&) {
        m_modePriorLocrianChanged.notify();
    });

    // ── Mode priors — melodic minor family ──────────────────────────────────
    settings()->setDefaultValue(MODE_PRIOR_MELODIC_MINOR, Val(-0.50));
    settings()->valueChanged(MODE_PRIOR_MELODIC_MINOR).onReceive(nullptr, [this](const Val&) {
        m_modePriorMelodicMinorChanged.notify();
    });
    settings()->setDefaultValue(MODE_PRIOR_DORIAN_B2, Val(-1.50));
    settings()->valueChanged(MODE_PRIOR_DORIAN_B2).onReceive(nullptr, [this](const Val&) {
        m_modePriorDorianB2Changed.notify();
    });
    settings()->setDefaultValue(MODE_PRIOR_LYDIAN_AUGMENTED, Val(-1.00));
    settings()->valueChanged(MODE_PRIOR_LYDIAN_AUGMENTED).onReceive(nullptr, [this](const Val&) {
        m_modePriorLydianAugmentedChanged.notify();
    });
    settings()->setDefaultValue(MODE_PRIOR_LYDIAN_DOMINANT, Val(-0.30));
    settings()->valueChanged(MODE_PRIOR_LYDIAN_DOMINANT).onReceive(nullptr, [this](const Val&) {
        m_modePriorLydianDominantChanged.notify();
    });
    settings()->setDefaultValue(MODE_PRIOR_MIXOLYDIAN_B6, Val(-1.00));
    settings()->valueChanged(MODE_PRIOR_MIXOLYDIAN_B6).onReceive(nullptr, [this](const Val&) {
        m_modePriorMixolydianB6Changed.notify();
    });
    settings()->setDefaultValue(MODE_PRIOR_AEOLIAN_B5, Val(-2.00));
    settings()->valueChanged(MODE_PRIOR_AEOLIAN_B5).onReceive(nullptr, [this](const Val&) {
        m_modePriorAeolianB5Changed.notify();
    });
    settings()->setDefaultValue(MODE_PRIOR_ALTERED, Val(-3.50));
    settings()->valueChanged(MODE_PRIOR_ALTERED).onReceive(nullptr, [this](const Val&) {
        m_modePriorAlteredChanged.notify();
    });

    // ── Mode priors — harmonic minor family ─────────────────────────────────
    settings()->setDefaultValue(MODE_PRIOR_HARMONIC_MINOR, Val(-0.30));
    settings()->valueChanged(MODE_PRIOR_HARMONIC_MINOR).onReceive(nullptr, [this](const Val&) {
        m_modePriorHarmonicMinorChanged.notify();
    });
    settings()->setDefaultValue(MODE_PRIOR_LOCRIAN_SHARP6, Val(-2.00));
    settings()->valueChanged(MODE_PRIOR_LOCRIAN_SHARP6).onReceive(nullptr, [this](const Val&) {
        m_modePriorLocrianSharp6Changed.notify();
    });
    settings()->setDefaultValue(MODE_PRIOR_IONIAN_SHARP5, Val(-1.50));
    settings()->valueChanged(MODE_PRIOR_IONIAN_SHARP5).onReceive(nullptr, [this](const Val&) {
        m_modePriorIonianSharp5Changed.notify();
    });
    settings()->setDefaultValue(MODE_PRIOR_DORIAN_SHARP4, Val(-1.50));
    settings()->valueChanged(MODE_PRIOR_DORIAN_SHARP4).onReceive(nullptr, [this](const Val&) {
        m_modePriorDorianSharp4Changed.notify();
    });
    settings()->setDefaultValue(MODE_PRIOR_PHRYGIAN_DOMINANT, Val(-0.80));
    settings()->valueChanged(MODE_PRIOR_PHRYGIAN_DOMINANT).onReceive(nullptr, [this](const Val&) {
        m_modePriorPhrygianDominantChanged.notify();
    });
    settings()->setDefaultValue(MODE_PRIOR_LYDIAN_SHARP2, Val(-2.00));
    settings()->valueChanged(MODE_PRIOR_LYDIAN_SHARP2).onReceive(nullptr, [this](const Val&) {
        m_modePriorLydianSharp2Changed.notify();
    });
    settings()->setDefaultValue(MODE_PRIOR_ALTERED_DOM_BB7, Val(-3.50));
    settings()->valueChanged(MODE_PRIOR_ALTERED_DOM_BB7).onReceive(nullptr, [this](const Val&) {
        m_modePriorAlteredDomBB7Changed.notify();
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

// ── tuningMode ──────────────────────────────────────────────────────────────

mu::composing::intonation::TuningMode ComposingConfiguration::tuningMode() const
{
    const int raw = settings()->value(TUNING_MODE).toInt();
    return static_cast<mu::composing::intonation::TuningMode>(raw);
}

void ComposingConfiguration::setTuningMode(mu::composing::intonation::TuningMode mode)
{
    settings()->setSharedValue(TUNING_MODE, Val(static_cast<int>(mode)));
}

muse::async::Notification ComposingConfiguration::tuningModeChanged() const
{
    return m_tuningModeChanged;
}

bool ComposingConfiguration::allowSplitSlurOfSustainedEvents() const
{
    return settings()->value(ALLOW_SPLIT_SLUR_OF_SUSTAINED_EVENTS).toBool();
}

void ComposingConfiguration::setAllowSplitSlurOfSustainedEvents(bool value)
{
    settings()->setSharedValue(ALLOW_SPLIT_SLUR_OF_SUSTAINED_EVENTS, Val(value));
}

muse::async::Notification ComposingConfiguration::allowSplitSlurOfSustainedEventsChanged() const
{
    return m_allowSplitSlurOfSustainedEventsChanged;
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

// ── annotateDriftAtBoundaries ────────────────────────────────────────────────

bool ComposingConfiguration::annotateDriftAtBoundaries() const
{
    return settings()->value(ANNOTATE_DRIFT_AT_BOUNDARIES).toBool();
}

void ComposingConfiguration::setAnnotateDriftAtBoundaries(bool value)
{
    settings()->setSharedValue(ANNOTATE_DRIFT_AT_BOUNDARIES, Val(value));
}

muse::async::Notification ComposingConfiguration::annotateDriftAtBoundariesChanged() const
{
    return m_annotateDriftAtBoundariesChanged;
}

// ── useRegionalAccumulation ──────────────────────────────────────────────────

bool ComposingConfiguration::useRegionalAccumulation() const
{
    return settings()->value(USE_REGIONAL_ACCUMULATION).toBool();
}

void ComposingConfiguration::setUseRegionalAccumulation(bool value)
{
    settings()->setSharedValue(USE_REGIONAL_ACCUMULATION, Val(value));
}

muse::async::Notification ComposingConfiguration::useRegionalAccumulationChanged() const
{
    return m_useRegionalAccumulationChanged;
}

// ── onsetBoundaryThreshold ───────────────────────────────────────────────────

double ComposingConfiguration::onsetBoundaryThreshold() const
{
    return settings()->value(ONSET_BOUNDARY_THRESHOLD).toDouble();
}

void ComposingConfiguration::setOnsetBoundaryThreshold(double value)
{
    settings()->setSharedValue(ONSET_BOUNDARY_THRESHOLD, Val(value));
}

muse::async::Notification ComposingConfiguration::onsetBoundaryThresholdChanged() const
{
    return m_onsetBoundaryThresholdChanged;
}

double ComposingConfiguration::modeNameConfidenceThreshold() const
{
    return settings()->value(MODE_NAME_CONFIDENCE_THRESHOLD).toDouble();
}

void ComposingConfiguration::setModeNameConfidenceThreshold(double value)
{
    settings()->setSharedValue(MODE_NAME_CONFIDENCE_THRESHOLD, Val(std::clamp(value, 0.0, 1.0)));
}

muse::async::Notification ComposingConfiguration::modeNameConfidenceThresholdChanged() const
{
    return m_modeNameConfidenceThresholdChanged;
}

double ComposingConfiguration::minimumDisplayDurationBeats() const
{
    return settings()->value(MINIMUM_DISPLAY_DURATION_BEATS).toDouble();
}

void ComposingConfiguration::setMinimumDisplayDurationBeats(double value)
{
    settings()->setSharedValue(MINIMUM_DISPLAY_DURATION_BEATS, Val(std::clamp(value, 0.0, 4.0)));
}

muse::async::Notification ComposingConfiguration::minimumDisplayDurationBeatsChanged() const
{
    return m_minimumDisplayDurationBeatsChanged;
}

double ComposingConfiguration::minKeyStabilityBeats() const
{
    return settings()->value(MIN_KEY_STABILITY_BEATS).toDouble();
}

void ComposingConfiguration::setMinKeyStabilityBeats(double value)
{
    settings()->setSharedValue(MIN_KEY_STABILITY_BEATS, Val(std::clamp(value, 2.0, 16.0)));
}

muse::async::Notification ComposingConfiguration::minKeyStabilityBeatsChanged() const
{
    return m_minKeyStabilityBeatsChanged;
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

// ── Mode priors — diatonic ───────────────────────────────────────────────────

double ComposingConfiguration::modePriorIonian() const { return settings()->value(MODE_PRIOR_IONIAN).toDouble(); }
void ComposingConfiguration::setModePriorIonian(double v) { settings()->setSharedValue(MODE_PRIOR_IONIAN, Val(v)); }
muse::async::Notification ComposingConfiguration::modePriorIonianChanged() const { return m_modePriorIonianChanged; }

double ComposingConfiguration::modePriorDorian() const { return settings()->value(MODE_PRIOR_DORIAN).toDouble(); }
void ComposingConfiguration::setModePriorDorian(double v) { settings()->setSharedValue(MODE_PRIOR_DORIAN, Val(v)); }
muse::async::Notification ComposingConfiguration::modePriorDorianChanged() const { return m_modePriorDorianChanged; }

double ComposingConfiguration::modePriorPhrygian() const { return settings()->value(MODE_PRIOR_PHRYGIAN).toDouble(); }
void ComposingConfiguration::setModePriorPhrygian(double v) { settings()->setSharedValue(MODE_PRIOR_PHRYGIAN, Val(v)); }
muse::async::Notification ComposingConfiguration::modePriorPhrygianChanged() const { return m_modePriorPhrygianChanged; }

double ComposingConfiguration::modePriorLydian() const { return settings()->value(MODE_PRIOR_LYDIAN).toDouble(); }
void ComposingConfiguration::setModePriorLydian(double v) { settings()->setSharedValue(MODE_PRIOR_LYDIAN, Val(v)); }
muse::async::Notification ComposingConfiguration::modePriorLydianChanged() const { return m_modePriorLydianChanged; }

double ComposingConfiguration::modePriorMixolydian() const { return settings()->value(MODE_PRIOR_MIXOLYDIAN).toDouble(); }
void ComposingConfiguration::setModePriorMixolydian(double v) { settings()->setSharedValue(MODE_PRIOR_MIXOLYDIAN, Val(v)); }
muse::async::Notification ComposingConfiguration::modePriorMixolydianChanged() const { return m_modePriorMixolydianChanged; }

double ComposingConfiguration::modePriorAeolian() const { return settings()->value(MODE_PRIOR_AEOLIAN).toDouble(); }
void ComposingConfiguration::setModePriorAeolian(double v) { settings()->setSharedValue(MODE_PRIOR_AEOLIAN, Val(v)); }
muse::async::Notification ComposingConfiguration::modePriorAeolianChanged() const { return m_modePriorAeolianChanged; }

double ComposingConfiguration::modePriorLocrian() const { return settings()->value(MODE_PRIOR_LOCRIAN).toDouble(); }
void ComposingConfiguration::setModePriorLocrian(double v) { settings()->setSharedValue(MODE_PRIOR_LOCRIAN, Val(v)); }
muse::async::Notification ComposingConfiguration::modePriorLocrianChanged() const { return m_modePriorLocrianChanged; }

// ── Mode priors — melodic minor family ──────────────────────────────────────

double ComposingConfiguration::modePriorMelodicMinor() const { return settings()->value(MODE_PRIOR_MELODIC_MINOR).toDouble(); }
void ComposingConfiguration::setModePriorMelodicMinor(double v) { settings()->setSharedValue(MODE_PRIOR_MELODIC_MINOR, Val(v)); }
muse::async::Notification ComposingConfiguration::modePriorMelodicMinorChanged() const { return m_modePriorMelodicMinorChanged; }

double ComposingConfiguration::modePriorDorianB2() const { return settings()->value(MODE_PRIOR_DORIAN_B2).toDouble(); }
void ComposingConfiguration::setModePriorDorianB2(double v) { settings()->setSharedValue(MODE_PRIOR_DORIAN_B2, Val(v)); }
muse::async::Notification ComposingConfiguration::modePriorDorianB2Changed() const { return m_modePriorDorianB2Changed; }

double ComposingConfiguration::modePriorLydianAugmented() const { return settings()->value(MODE_PRIOR_LYDIAN_AUGMENTED).toDouble(); }
void ComposingConfiguration::setModePriorLydianAugmented(double v) { settings()->setSharedValue(MODE_PRIOR_LYDIAN_AUGMENTED, Val(v)); }
muse::async::Notification ComposingConfiguration::modePriorLydianAugmentedChanged() const { return m_modePriorLydianAugmentedChanged; }

double ComposingConfiguration::modePriorLydianDominant() const { return settings()->value(MODE_PRIOR_LYDIAN_DOMINANT).toDouble(); }
void ComposingConfiguration::setModePriorLydianDominant(double v) { settings()->setSharedValue(MODE_PRIOR_LYDIAN_DOMINANT, Val(v)); }
muse::async::Notification ComposingConfiguration::modePriorLydianDominantChanged() const { return m_modePriorLydianDominantChanged; }

double ComposingConfiguration::modePriorMixolydianB6() const { return settings()->value(MODE_PRIOR_MIXOLYDIAN_B6).toDouble(); }
void ComposingConfiguration::setModePriorMixolydianB6(double v) { settings()->setSharedValue(MODE_PRIOR_MIXOLYDIAN_B6, Val(v)); }
muse::async::Notification ComposingConfiguration::modePriorMixolydianB6Changed() const { return m_modePriorMixolydianB6Changed; }

double ComposingConfiguration::modePriorAeolianB5() const { return settings()->value(MODE_PRIOR_AEOLIAN_B5).toDouble(); }
void ComposingConfiguration::setModePriorAeolianB5(double v) { settings()->setSharedValue(MODE_PRIOR_AEOLIAN_B5, Val(v)); }
muse::async::Notification ComposingConfiguration::modePriorAeolianB5Changed() const { return m_modePriorAeolianB5Changed; }

double ComposingConfiguration::modePriorAltered() const { return settings()->value(MODE_PRIOR_ALTERED).toDouble(); }
void ComposingConfiguration::setModePriorAltered(double v) { settings()->setSharedValue(MODE_PRIOR_ALTERED, Val(v)); }
muse::async::Notification ComposingConfiguration::modePriorAlteredChanged() const { return m_modePriorAlteredChanged; }

// ── Mode priors — harmonic minor family ─────────────────────────────────────

double ComposingConfiguration::modePriorHarmonicMinor() const { return settings()->value(MODE_PRIOR_HARMONIC_MINOR).toDouble(); }
void ComposingConfiguration::setModePriorHarmonicMinor(double v) { settings()->setSharedValue(MODE_PRIOR_HARMONIC_MINOR, Val(v)); }
muse::async::Notification ComposingConfiguration::modePriorHarmonicMinorChanged() const { return m_modePriorHarmonicMinorChanged; }

double ComposingConfiguration::modePriorLocrianSharp6() const { return settings()->value(MODE_PRIOR_LOCRIAN_SHARP6).toDouble(); }
void ComposingConfiguration::setModePriorLocrianSharp6(double v) { settings()->setSharedValue(MODE_PRIOR_LOCRIAN_SHARP6, Val(v)); }
muse::async::Notification ComposingConfiguration::modePriorLocrianSharp6Changed() const { return m_modePriorLocrianSharp6Changed; }

double ComposingConfiguration::modePriorIonianSharp5() const { return settings()->value(MODE_PRIOR_IONIAN_SHARP5).toDouble(); }
void ComposingConfiguration::setModePriorIonianSharp5(double v) { settings()->setSharedValue(MODE_PRIOR_IONIAN_SHARP5, Val(v)); }
muse::async::Notification ComposingConfiguration::modePriorIonianSharp5Changed() const { return m_modePriorIonianSharp5Changed; }

double ComposingConfiguration::modePriorDorianSharp4() const { return settings()->value(MODE_PRIOR_DORIAN_SHARP4).toDouble(); }
void ComposingConfiguration::setModePriorDorianSharp4(double v) { settings()->setSharedValue(MODE_PRIOR_DORIAN_SHARP4, Val(v)); }
muse::async::Notification ComposingConfiguration::modePriorDorianSharp4Changed() const { return m_modePriorDorianSharp4Changed; }

double ComposingConfiguration::modePriorPhrygianDominant() const { return settings()->value(MODE_PRIOR_PHRYGIAN_DOMINANT).toDouble(); }
void ComposingConfiguration::setModePriorPhrygianDominant(double v) { settings()->setSharedValue(MODE_PRIOR_PHRYGIAN_DOMINANT, Val(v)); }
muse::async::Notification ComposingConfiguration::modePriorPhrygianDominantChanged() const { return m_modePriorPhrygianDominantChanged; }

double ComposingConfiguration::modePriorLydianSharp2() const { return settings()->value(MODE_PRIOR_LYDIAN_SHARP2).toDouble(); }
void ComposingConfiguration::setModePriorLydianSharp2(double v) { settings()->setSharedValue(MODE_PRIOR_LYDIAN_SHARP2, Val(v)); }
muse::async::Notification ComposingConfiguration::modePriorLydianSharp2Changed() const { return m_modePriorLydianSharp2Changed; }

double ComposingConfiguration::modePriorAlteredDomBB7() const { return settings()->value(MODE_PRIOR_ALTERED_DOM_BB7).toDouble(); }
void ComposingConfiguration::setModePriorAlteredDomBB7(double v) { settings()->setSharedValue(MODE_PRIOR_ALTERED_DOM_BB7, Val(v)); }
muse::async::Notification ComposingConfiguration::modePriorAlteredDomBB7Changed() const { return m_modePriorAlteredDomBB7Changed; }

// ── Named mode prior presets ─────────────────────────────────────────────────

std::vector<ModePriorPreset> mu::composing::modePriorPresets()
{
    // All values are additive log-odds biases.  Positive = more likely,
    // negative = less likely.  Defaults reflect empirical tuning on the
    // 371-chorale validation corpus.

    ModePriorPreset standard;
    standard.name             = "Standard";
    standard.ionian           =  1.20;
    standard.dorian           = -0.50;
    standard.phrygian         = -1.50;
    standard.lydian           = -1.50;
    standard.mixolydian       = -0.50;
    standard.aeolian          =  1.00;
    standard.locrian          = -3.00;
    standard.melodicMinor     = -0.50;
    standard.dorianB2         = -1.50;
    standard.lydianAugmented  = -2.00;
    standard.lydianDominant   = -1.00;
    standard.mixolydianB6     = -1.50;
    standard.aeolianB5        = -2.50;
    standard.altered          = -3.50;
    standard.harmonicMinor    = -0.30;
    standard.locrianSharp6    = -2.50;
    standard.ionianSharp5     = -2.00;
    standard.dorianSharp4     = -2.00;
    standard.phrygianDominant = -0.80;
    standard.lydianSharp2     = -2.50;
    standard.alteredDomBB7    = -3.50;

    ModePriorPreset jazz;
    jazz.name             = "Jazz";
    jazz.ionian           =  0.50;
    jazz.dorian           =  0.80;
    jazz.phrygian         = -1.00;
    jazz.lydian           = -0.50;
    jazz.mixolydian       =  0.80;
    jazz.aeolian          =  0.50;
    jazz.locrian          = -1.50;
    jazz.melodicMinor     =  0.50;
    jazz.dorianB2         = -0.50;
    jazz.lydianAugmented  = -0.50;
    jazz.lydianDominant   =  0.80;
    jazz.mixolydianB6     = -0.50;
    jazz.aeolianB5        = -1.00;
    jazz.altered          =  0.50;
    jazz.harmonicMinor    = -0.30;
    jazz.locrianSharp6    = -1.50;
    jazz.ionianSharp5     = -1.50;
    jazz.dorianSharp4     = -0.50;
    jazz.phrygianDominant =  0.20;
    jazz.lydianSharp2     = -1.50;
    jazz.alteredDomBB7    = -1.50;

    ModePriorPreset modal;
    modal.name             = "Modal";
    modal.ionian           =  0.50;
    modal.dorian           =  0.50;
    modal.phrygian         =  0.50;
    modal.lydian           =  0.50;
    modal.mixolydian       =  0.50;
    modal.aeolian          =  0.50;
    modal.locrian          = -1.00;
    modal.melodicMinor     = -1.00;
    modal.dorianB2         = -1.50;
    modal.lydianAugmented  = -2.00;
    modal.lydianDominant   = -1.50;
    modal.mixolydianB6     = -1.50;
    modal.aeolianB5        = -2.50;
    modal.altered          = -3.50;
    modal.harmonicMinor    = -1.00;
    modal.locrianSharp6    = -2.50;
    modal.ionianSharp5     = -2.00;
    modal.dorianSharp4     = -2.00;
    modal.phrygianDominant = -1.50;
    modal.lydianSharp2     = -2.50;
    modal.alteredDomBB7    = -3.50;

    ModePriorPreset baroque;
    baroque.name             = "Baroque";
    baroque.ionian           =  1.20;
    baroque.dorian           = -0.70;
    baroque.phrygian         = -1.50;
    baroque.lydian           = -2.00;
    baroque.mixolydian       = -0.70;
    baroque.aeolian          =  1.00;
    baroque.locrian          = -3.00;
    baroque.melodicMinor     = -1.50;
    baroque.dorianB2         = -2.00;
    baroque.lydianAugmented  = -2.50;
    baroque.lydianDominant   = -2.00;
    baroque.mixolydianB6     = -2.00;
    baroque.aeolianB5        = -3.00;
    baroque.altered          = -3.50;
    baroque.harmonicMinor    =  0.50;
    baroque.locrianSharp6    = -2.00;
    baroque.ionianSharp5     = -1.50;
    baroque.dorianSharp4     = -2.50;
    baroque.phrygianDominant =  0.50;
    baroque.lydianSharp2     = -2.00;
    baroque.alteredDomBB7    = -3.50;

    ModePriorPreset contemporary;
    contemporary.name             = "Contemporary";
    contemporary.ionian           =  0.80;
    contemporary.dorian           =  0.20;
    contemporary.phrygian         = -0.50;
    contemporary.lydian           = -0.20;
    contemporary.mixolydian       =  0.20;
    contemporary.aeolian          =  0.80;
    contemporary.locrian          = -2.00;
    contemporary.melodicMinor     =  0.20;
    contemporary.dorianB2         = -0.80;
    contemporary.lydianAugmented  = -1.00;
    contemporary.lydianDominant   =  0.20;
    contemporary.mixolydianB6     = -0.50;
    contemporary.aeolianB5        = -1.50;
    contemporary.altered          = -1.50;
    contemporary.harmonicMinor    =  0.20;
    contemporary.locrianSharp6    = -1.50;
    contemporary.ionianSharp5     = -1.00;
    contemporary.dorianSharp4     = -1.00;
    contemporary.phrygianDominant =  0.00;
    contemporary.lydianSharp2     = -1.50;
    contemporary.alteredDomBB7    = -2.00;

    return { standard, jazz, modal, baroque, contemporary };
}

void ComposingConfiguration::applyModePriorPreset(const std::string& name)
{
    for (const auto& p : modePriorPresets()) {
        if (p.name != name) continue;
        setModePriorIonian(p.ionian);
        setModePriorDorian(p.dorian);
        setModePriorPhrygian(p.phrygian);
        setModePriorLydian(p.lydian);
        setModePriorMixolydian(p.mixolydian);
        setModePriorAeolian(p.aeolian);
        setModePriorLocrian(p.locrian);
        setModePriorMelodicMinor(p.melodicMinor);
        setModePriorDorianB2(p.dorianB2);
        setModePriorLydianAugmented(p.lydianAugmented);
        setModePriorLydianDominant(p.lydianDominant);
        setModePriorMixolydianB6(p.mixolydianB6);
        setModePriorAeolianB5(p.aeolianB5);
        setModePriorAltered(p.altered);
        setModePriorHarmonicMinor(p.harmonicMinor);
        setModePriorLocrianSharp6(p.locrianSharp6);
        setModePriorIonianSharp5(p.ionianSharp5);
        setModePriorDorianSharp4(p.dorianSharp4);
        setModePriorPhrygianDominant(p.phrygianDominant);
        setModePriorLydianSharp2(p.lydianSharp2);
        setModePriorAlteredDomBB7(p.alteredDomBB7);
        return;
    }
}

std::string ComposingConfiguration::currentModePriorPreset() const
{
    constexpr double eps = 1e-6;
    auto eq = [](double a, double b) { return std::abs(a - b) < 1e-6; };
    (void)eps;

    for (const auto& p : modePriorPresets()) {
        if (eq(modePriorIonian(),          p.ionian)
         && eq(modePriorDorian(),          p.dorian)
         && eq(modePriorPhrygian(),        p.phrygian)
         && eq(modePriorLydian(),          p.lydian)
         && eq(modePriorMixolydian(),      p.mixolydian)
         && eq(modePriorAeolian(),         p.aeolian)
         && eq(modePriorLocrian(),         p.locrian)
         && eq(modePriorMelodicMinor(),    p.melodicMinor)
         && eq(modePriorDorianB2(),        p.dorianB2)
         && eq(modePriorLydianAugmented(), p.lydianAugmented)
         && eq(modePriorLydianDominant(),  p.lydianDominant)
         && eq(modePriorMixolydianB6(),    p.mixolydianB6)
         && eq(modePriorAeolianB5(),       p.aeolianB5)
         && eq(modePriorAltered(),         p.altered)
         && eq(modePriorHarmonicMinor(),   p.harmonicMinor)
         && eq(modePriorLocrianSharp6(),   p.locrianSharp6)
         && eq(modePriorIonianSharp5(),    p.ionianSharp5)
         && eq(modePriorDorianSharp4(),    p.dorianSharp4)
         && eq(modePriorPhrygianDominant(), p.phrygianDominant)
         && eq(modePriorLydianSharp2(),    p.lydianSharp2)
         && eq(modePriorAlteredDomBB7(),   p.alteredDomBB7)) {
            return p.name;
        }
    }
    return {};
}
