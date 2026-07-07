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

#include "modepriorpresets.h"

namespace mu::composing {

std::vector<ModePriorPreset> modePriorPresets()
{
    // All values are additive log-odds biases.  Positive = more likely,
    // negative = less likely.  Defaults reflect empirical tuning on the
    // 371-chorale validation corpus.

    // "Standard" == the ModePriorPreset struct default member initializers
    // (modepriorpresets.h), which in turn match the KeyModeAnalyzerPreferences
    // compile-time defaults. FQ-5/S7 removed the explicit `standard.*=` restatement
    // (a third literal copy the sync test had to guard); a default-constructed
    // ModePriorPreset already carries exactly these magnitudes.
    ModePriorPreset standard;
    standard.name             = "Standard";

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

} // namespace mu::composing
