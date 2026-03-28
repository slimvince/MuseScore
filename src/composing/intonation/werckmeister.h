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

#include "tuning_system.h"
#include "tuning_keys.h"
#include <array>

namespace mu::composing::intonation {

/**
 * @brief Werckmeister III Well Temperament (Andreas Werckmeister, 1691).
 *
 * A historically important irregular temperament designed to allow modulation
 * to all keys, each key having a distinct character.  Used by J.S. Bach.
 *
 * Construction: four fifths narrow by exactly 1/4 Pythagorean comma (≈ 5.865 ¢
 * each); the remaining eight fifths are pure (701.955 ¢).  The narrow fifths are
 * C–G, G–D, D–A, and B–F#.
 *
 * The deviations are absolute — they depend on the note's pitch class, not on
 * the key being played.  This is what gives well temperament its key-specific
 * character: keys near C major are more consonant (thirds closer to pure) while
 * remote keys sound more colourful.
 *
 * Deviations from 12-TET (cents), indexed by absolute pitch class C=0:
 *   C=0.0, C#=−9.8, D=−7.8, Eb=−5.9, E=−9.8, F=−2.0, F#=−11.7,
 *   G=−3.9, Ab=−7.8, A=−11.7, Bb=−3.9, B=−7.8
 *
 * Reference: Andreas Werckmeister, "Musicalische Temperatur" (1691).
 */
class WerckmeisterTemperament : public TuningSystem {
public:
    TuningSystemId id() const override { return TuningSystemId::Werckmeister; }
    const char* key() const override { return TuningKey::Werckmeister; }
    std::string displayName() const override { return "Werckmeister III"; }

    double tuningOffset(
        const mu::composing::analysis::KeyModeAnalysisResult& /*keyMode*/,
        mu::composing::analysis::ChordQuality /*quality*/,
        int rootPc,
        int semitones
    ) const override
    {
        // Deviations from 12-TET in cents, indexed by absolute pitch class (C=0).
        // Derived from four 1/4-Pythagorean-comma narrow fifths: C–G, G–D, D–A, B–F#.
        // All values are negative (the scale is flat of ET) except the reference C=0.
        static constexpr std::array<double, 12> dev = {
             0.0,   //  C
            -9.8,   //  C#   (90.2 ¢ vs ET 100)
            -7.8,   //  D    (192.2 ¢ vs ET 200)
            -5.9,   //  Eb   (294.1 ¢ vs ET 300)
            -9.8,   //  E    (390.2 ¢ vs ET 400)
            -2.0,   //  F    (498.0 ¢ vs ET 500)
           -11.7,   //  F#   (588.3 ¢ vs ET 600)
            -3.9,   //  G    (696.1 ¢ vs ET 700)
            -7.8,   //  Ab   (792.2 ¢ vs ET 800)
           -11.7,   //  A    (888.3 ¢ vs ET 900)
            -3.9,   //  Bb   (996.1 ¢ vs ET 1000)
            -7.8,   //  B    (1092.2 ¢ vs ET 1100)
        };
        // Convert the semitone-from-root interval to an absolute pitch class, then
        // look up the fixed deviation for that pitch class.
        const int notePc = (rootPc + semitones + 12) % 12;
        return dev[notePc];
    }
};

} // namespace mu::composing::intonation
