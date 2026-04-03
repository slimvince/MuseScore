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

    /// Whether to run the chord-symbol analyzer when a note is selected.
    virtual bool analyzeForChordSymbols() const = 0;
    virtual void setAnalyzeForChordSymbols(bool value) = 0;
    virtual muse::async::Notification analyzeForChordSymbolsChanged() const = 0;

    /// Whether to run the Roman-numeral analyzer when a note is selected.
    virtual bool analyzeForRomanNumerals() const = 0;
    virtual void setAnalyzeForRomanNumerals(bool value) = 0;
    virtual muse::async::Notification analyzeForRomanNumeralsChanged() const = 0;

    /// Whether to infer the key/mode when a note is selected.
    /// Forced on when either chord-symbol or Roman-numeral analysis is enabled.
    virtual bool inferKeyMode() const = 0;
    virtual void setInferKeyMode(bool value) = 0;
    virtual muse::async::Notification inferKeyModeChanged() const = 0;

    /// Number of alternative chord interpretations offered in the context menu (1–3).
    virtual int analysisAlternatives() const = 0;
    virtual void setAnalysisAlternatives(int count) = 0;
    virtual muse::async::Notification analysisAlternativesChanged() const = 0;

    /// Tuning system used for "tune as" in the note context menu.
    /// Stored as a TuningKey string (e.g. "equal", "just").
    /// Enabled in the UI only when Roman-numeral analysis is active.
    virtual std::string tuningSystemKey() const = 0;
    virtual void setTuningSystemKey(const std::string& key) = 0;
    virtual muse::async::Notification tuningSystemKeyChanged() const = 0;

    /// Whether to anchor chord root tuning to the mode tonic (tonic-anchored JI).
    /// When enabled, each chord root is placed at its just-intonation scale-degree
    /// position above the mode tonic rather than always at 0 ¢ from 12-TET.
    /// Default: true.  Has no effect when the tuning system is equal temperament.
    virtual bool tonicAnchoredTuning() const = 0;
    virtual void setTonicAnchoredTuning(bool value) = 0;
    virtual muse::async::Notification tonicAnchoredTuningChanged() const = 0;

    /// Whether to subtract the mean tuning offset from all notes in each chord,
    /// minimizing the total deviation from 12-TET while preserving pure intervals
    /// between notes.  Default: false.
    virtual bool minimizeTuningDeviation() const = 0;
    virtual void setMinimizeTuningDeviation(bool value) = 0;
    virtual muse::async::Notification minimizeTuningDeviationChanged() const = 0;

    /// Whether to add a staff text annotation below each tuned chord showing
    /// each note's deviation from 12-TET in cents (e.g. "+2 -14 +4").
    /// Useful for analysis; annotations accumulate on re-application.
    /// Default: false.
    virtual bool annotateTuningOffsets() const = 0;
    virtual void setAnnotateTuningOffsets(bool value) = 0;
    virtual muse::async::Notification annotateTuningOffsetsChanged() const = 0;

    // ── Status-bar display ───────────────────────────────────────────────────

    /// Whether to show the inferred key/mode in the status bar.
    virtual bool showKeyModeInStatusBar() const = 0;
    virtual void setShowKeyModeInStatusBar(bool value) = 0;
    virtual muse::async::Notification showKeyModeInStatusBarChanged() const = 0;

    /// Number of chord symbol suggestions to show in the status bar (0–3).
    virtual int statusBarChordSymbolCount() const = 0;
    virtual void setStatusBarChordSymbolCount(int count) = 0;
    virtual muse::async::Notification statusBarChordSymbolCountChanged() const = 0;

    /// Number of Roman numeral suggestions to show in the status bar (0–3).
    virtual int statusBarRomanNumeralCount() const = 0;
    virtual void setStatusBarRomanNumeralCount(int count) = 0;
    virtual muse::async::Notification statusBarRomanNumeralCountChanged() const = 0;

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
