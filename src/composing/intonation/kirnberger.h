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
 * @brief Kirnberger III Well Temperament (Johann Philipp Kirnberger, c. 1779).
 *
 * An irregular temperament designed for full modulation with expressive key
 * character.  Its defining feature is a pure major third C–E (5/4 ratio =
 * 386.3 ¢), making C major and closely related keys especially consonant.
 *
 * Construction: four consecutive fifths in the circle are narrow — C–G, G–D,
 * D–A each by 1/4 syntonic comma (≈ 5.377 ¢), and A–E by the same amount so
 * that C–E is exactly pure.  The remaining eight fifths are pure except for
 * F–C, which is narrow by the schisma (≈ 1.954 ¢) to close the circle.
 *
 * The deviations are absolute — they depend on the note's pitch class, not on
 * the key being played.  Like Werckmeister III, the temperament creates distinct
 * key characters; Kirnberger III concentrates its purity around C major, making
 * keys with many sharps or flats the most colourful.
 *
 * Deviations from 12-TET (cents), indexed by absolute pitch class C=0:
 *   C=0.0, C#=−7.8, D=−6.8, Eb=−3.9, E=−13.7, F=0.0, F#=−9.8,
 *   G=−3.4, Ab=−5.9, A=−10.3, Bb=−2.0, B=−11.7
 *
 * Reference: Johann Philipp Kirnberger, "Die Kunst des reinen Satzes" (1771–79).
 */
class KirnbergerTemperament : public TuningSystem {
public:
    TuningSystemId id() const override { return TuningSystemId::Kirnberger; }
    const char* key() const override { return TuningKey::Kirnberger; }
    std::string displayName() const override { return "Kirnberger III"; }

    double tuningOffset(
        const mu::composing::analysis::KeyModeAnalysisResult& /*keyMode*/,
        mu::composing::analysis::ChordQuality /*quality*/,
        int rootPc,
        int semitones
    ) const override
    {
        // Deviations from 12-TET in cents, indexed by absolute pitch class (C=0).
        // Derived from four 1/4-syntonic-comma narrow fifths (C–G, G–D, D–A, A–E)
        // plus a schisma-narrow F–C to close the circle.
        // E = 386.3 ¢ = pure major third above C (5/4).
        static constexpr std::array<double, 12> dev = {
             0.0,   //  C    (  0.0 ¢ vs ET   0)
            -7.8,   //  C#   ( 92.2 ¢ vs ET 100)
            -6.8,   //  D    (193.2 ¢ vs ET 200)
            -3.9,   //  Eb   (296.1 ¢ vs ET 300)
           -13.7,   //  E    (386.3 ¢ vs ET 400 — pure major third from C)
             0.0,   //  F    (500.0 ¢ vs ET 500)
            -9.8,   //  F#   (590.2 ¢ vs ET 600)
            -3.4,   //  G    (696.6 ¢ vs ET 700)
            -5.9,   //  Ab   (794.1 ¢ vs ET 800)
           -10.3,   //  A    (889.7 ¢ vs ET 900)
            -2.0,   //  Bb   (998.0 ¢ vs ET 1000)
           -11.7,   //  B    (1088.3 ¢ vs ET 1100)
        };
        // Convert the semitone-from-root interval to an absolute pitch class, then
        // look up the fixed deviation for that pitch class.
        const int notePc = (rootPc + semitones + 12) % 12;
        return dev[notePc];
    }
};

} // namespace mu::composing::intonation
