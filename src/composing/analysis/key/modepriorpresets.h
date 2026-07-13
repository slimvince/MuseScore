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

// ── ModePriorPreset and the five named built-in presets ──────────────────────
//
// This was previously inlined in icomposinganalysisconfiguration.h with the
// definition in composingconfiguration.cpp.  Moved into composing_analysis
// (per docs/duplication_audit.md §5.8) so tools/batch_analyze.cpp — which
// links composing_analysis but not the composing module — can call the same
// preset table the live UI/preferences path uses.

#include <string>
#include <vector>

namespace mu::composing {

/// All 21 mode priors bundled under a display name.
/// The five built-in presets are returned by modePriorPresets().
/// The "Standard" preset matches the compile-time defaults in
/// KeyModeAnalyzerPreferences.
struct ModePriorPreset {
    std::string name;               ///< Display name (e.g. "Standard", "Jazz")

    // Diatonic modes
    double ionian          =  1.20;
    double dorian          = -0.50;
    double phrygian        = -1.50;
    double lydian          = -1.50;
    double mixolydian      = -0.50;
    double aeolian         =  1.00;
    double locrian         = -3.00;

    // Melodic minor family
    double melodicMinor    = -0.50;
    double dorianB2        = -1.50;
    double lydianAugmented = -2.00;
    double lydianDominant  = -1.00;
    double mixolydianB6    = -1.50;
    double aeolianB5       = -2.50;
    double altered         = -3.50;

    // Harmonic minor family
    double harmonicMinor      = -0.30;
    double locrianSharp6      = -2.50;
    double ionianSharp5       = -2.00;
    double dorianSharp4       = -2.00;
    double phrygianDominant   = -0.80;
    double lydianSharp2       = -2.50;
    double alteredDomBB7      = -3.50;
};

/// Returns the five built-in mode prior presets in display order:
/// Standard, Jazz, Modal, Baroque, Contemporary.
std::vector<ModePriorPreset> modePriorPresets();

/// The app's out-of-box mode priors — the 21 values ComposingConfiguration::init()
/// registers as the MODE_PRIOR_* settings defaults.
///
/// This is NOT one of the five named tuning presets (it is absent from
/// modePriorPresets()) and it is NOT the ModePriorPreset struct defaults, i.e. not
/// "Standard": the app defaults diverge from Standard on 11 of the 21 modes (lydian,
/// mixolydian, locrian, lydianAugmented, lydianDominant, mixolydianB6, aeolianB5,
/// locrianSharp6, ionianSharp5, dorianSharp4, lydianSharp2).
///
/// It lives here for the same reason modePriorPresets() does (see the note above):
/// composing_analysis is the only library both the app and tools/batch_analyze link,
/// so it is the one place where the settings registration and the harness's "Default"
/// preset — which exists to corpus-measure the configuration users actually run — can
/// read ONE table instead of value-copying it between them (OI-135).
ModePriorPreset modePriorAppDefaults();

} // namespace mu::composing
