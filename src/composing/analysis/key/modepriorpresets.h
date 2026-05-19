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

} // namespace mu::composing
