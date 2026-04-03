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

#include <string>
#include "modularity/imoduleinterface.h"
#include "async/notification.h"

namespace mu::composing {

class IComposingConfiguration : MODULE_GLOBAL_INTERFACE
{
    INTERFACE_ID(IComposingConfiguration)

public:
    virtual ~IComposingConfiguration() = default;

    // ── Analysis behaviour ───────────────────────────────────────────────────

    /// Whether to run chord-symbol analysis (pitch structure only; no key/mode needed).
    virtual bool analyzeForChordSymbols() const = 0;
    virtual void setAnalyzeForChordSymbols(bool value) = 0;
    virtual muse::async::Notification analyzeForChordSymbolsChanged() const = 0;

    /// Whether to run chord-function analysis (key/mode inference + degree assignment).
    /// This is the single toggle that feeds both Roman-numeral and Nashville-number
    /// display; it implies inferKeyMode being active.
    virtual bool analyzeForChordFunction() const = 0;
    virtual void setAnalyzeForChordFunction(bool value) = 0;
    virtual muse::async::Notification analyzeForChordFunctionChanged() const = 0;

    /// Whether to infer the key/mode when a note is selected.
    /// Forced on when chord-function analysis is enabled.
    virtual bool inferKeyMode() const = 0;
    virtual void setInferKeyMode(bool value) = 0;
    virtual muse::async::Notification inferKeyModeChanged() const = 0;

    /// Number of alternative chord interpretations to show — used universally
    /// for both the status bar and the context menu (1–3).
    virtual int analysisAlternatives() const = 0;
    virtual void setAnalysisAlternatives(int count) = 0;
    virtual muse::async::Notification analysisAlternativesChanged() const = 0;

    /// Tuning system used for "tune as" in the note context menu.
    /// Stored as a TuningKey string (e.g. "equal", "just").
    virtual std::string tuningSystemKey() const = 0;
    virtual void setTuningSystemKey(const std::string& key) = 0;
    virtual muse::async::Notification tuningSystemKeyChanged() const = 0;

    /// Whether to anchor chord root tuning to the mode tonic (tonic-anchored JI).
    /// Has no effect when the tuning system is equal temperament.
    /// Default: true.
    virtual bool tonicAnchoredTuning() const = 0;
    virtual void setTonicAnchoredTuning(bool value) = 0;
    virtual muse::async::Notification tonicAnchoredTuningChanged() const = 0;

    /// Whether to subtract the mean tuning offset from all notes in each chord.
    /// Default: false.
    virtual bool minimizeTuningDeviation() const = 0;
    virtual void setMinimizeTuningDeviation(bool value) = 0;
    virtual muse::async::Notification minimizeTuningDeviationChanged() const = 0;

    /// Whether to add a staff text annotation below each tuned chord showing
    /// each note's deviation from 12-TET in cents.  Default: false.
    virtual bool annotateTuningOffsets() const = 0;
    virtual void setAnnotateTuningOffsets(bool value) = 0;
    virtual muse::async::Notification annotateTuningOffsetsChanged() const = 0;

    // ── Status-bar display ───────────────────────────────────────────────────

    /// Whether to show the inferred key/mode in the status bar.
    virtual bool showKeyModeInStatusBar() const = 0;
    virtual void setShowKeyModeInStatusBar(bool value) = 0;
    virtual muse::async::Notification showKeyModeInStatusBarChanged() const = 0;

    /// Whether to show chord symbols in the status bar.
    /// Requires analyzeForChordSymbols.
    virtual bool showChordSymbolsInStatusBar() const = 0;
    virtual void setShowChordSymbolsInStatusBar(bool value) = 0;
    virtual muse::async::Notification showChordSymbolsInStatusBarChanged() const = 0;

    /// Whether to show Roman numerals in the status bar.
    /// Requires analyzeForChordFunction.
    virtual bool showRomanNumeralsInStatusBar() const = 0;
    virtual void setShowRomanNumeralsInStatusBar(bool value) = 0;
    virtual muse::async::Notification showRomanNumeralsInStatusBarChanged() const = 0;

    /// Whether to show Nashville numbers in the status bar.
    /// Requires analyzeForChordFunction.
    virtual bool showNashvilleNumbersInStatusBar() const = 0;
    virtual void setShowNashvilleNumbersInStatusBar(bool value) = 0;
    virtual muse::async::Notification showNashvilleNumbersInStatusBarChanged() const = 0;

    // ── Chord staff ("Implode") output ──────────────────────────────────────

    /// Whether to write chord symbol annotations (HarmonyType::STANDARD) to the
    /// chord staff when imploding.  Requires analyzeForChordSymbols.
    virtual bool chordStaffWriteChordSymbols() const = 0;
    virtual void setChordStaffWriteChordSymbols(bool value) = 0;
    virtual muse::async::Notification chordStaffWriteChordSymbolsChanged() const = 0;

    /// Which chord-function notation to write below the treble staff when imploding.
    /// "none" — nothing; "roman" — HarmonyType::ROMAN; "nashville" — HarmonyType::NASHVILLE.
    /// Roman and Nashville are mutually exclusive (same data, different format).
    /// Requires analyzeForChordFunction.
    virtual std::string chordStaffFunctionNotation() const = 0;
    virtual void setChordStaffFunctionNotation(const std::string& value) = 0;
    virtual muse::async::Notification chordStaffFunctionNotationChanged() const = 0;

    /// Whether to write key/mode staff-text annotations at region boundaries
    /// when imploding.  Requires inferKeyMode.
    virtual bool chordStaffWriteKeyAnnotations() const = 0;
    virtual void setChordStaffWriteKeyAnnotations(bool value) = 0;
    virtual muse::async::Notification chordStaffWriteKeyAnnotationsChanged() const = 0;

    /// Whether to write the non-diatonic chord marker (★ + source key) when
    /// imploding.  Requires analyzeForChordFunction.
    virtual bool chordStaffHighlightNonDiatonic() const = 0;
    virtual void setChordStaffHighlightNonDiatonic(bool value) = 0;
    virtual muse::async::Notification chordStaffHighlightNonDiatonicChanged() const = 0;

    /// Whether to write cadence markers (PAC, PC, DC, HC) when imploding.
    /// Requires analyzeForChordFunction.
    virtual bool chordStaffWriteCadenceMarkers() const = 0;
    virtual void setChordStaffWriteCadenceMarkers(bool value) = 0;
    virtual muse::async::Notification chordStaffWriteCadenceMarkersChanged() const = 0;

    // ── Mode tier weights ───────────────────────────────────────────────────
    //
    // Additive scoring bias for four tiers of diatonic modes, controlling how
    // strongly the key/mode analyzer favors common modes over rare ones.
    // Range: -5.0 (effectively blocked) to +3.0 (strongly favored).

    /// Tier 1: Major / Minor (Ionian, Aeolian).  Default: +1.0.
    virtual double modeTierWeight1() const = 0;
    virtual void setModeTierWeight1(double value) = 0;
    virtual muse::async::Notification modeTierWeight1Changed() const = 0;

    /// Tier 2: Dorian / Mixolydian.  Default: -0.5.
    virtual double modeTierWeight2() const = 0;
    virtual void setModeTierWeight2(double value) = 0;
    virtual muse::async::Notification modeTierWeight2Changed() const = 0;

    /// Tier 3: Lydian / Phrygian.  Default: -1.5.
    virtual double modeTierWeight3() const = 0;
    virtual void setModeTierWeight3(double value) = 0;
    virtual muse::async::Notification modeTierWeight3Changed() const = 0;

    /// Tier 4: Locrian.  Default: -3.0.
    virtual double modeTierWeight4() const = 0;
    virtual void setModeTierWeight4(double value) = 0;
    virtual muse::async::Notification modeTierWeight4Changed() const = 0;
};

} // namespace mu::composing
