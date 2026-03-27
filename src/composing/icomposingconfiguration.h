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

    /// Number of alternative chord interpretations offered in the context menu (1–5).
    virtual int analysisAlternatives() const = 0;
    virtual void setAnalysisAlternatives(int count) = 0;
    virtual muse::async::Notification analysisAlternativesChanged() const = 0;

    /// Tuning system used for "tune as" in the note context menu.
    /// Stored as a TuningKey string (e.g. "equal", "just").
    /// Enabled in the UI only when Roman-numeral analysis is active.
    virtual std::string tuningSystemKey() const = 0;
    virtual void setTuningSystemKey(const std::string& key) = 0;
    virtual muse::async::Notification tuningSystemKeyChanged() const = 0;

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
};

} // namespace mu::composing
