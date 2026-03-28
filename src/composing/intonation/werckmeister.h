// SPDX-License-Identifier: GPL-3.0-only
// MuseScore Studio — Werckmeister Well Temperament tuning system
#pragma once

#include "tuning_system.h"
#include "tuning_keys.h"
#include <array>
#include "../analysis/keymodeanalyzer.h"

namespace mu::composing::intonation {

/**
 * @brief Werckmeister III Well Temperament.
 *
 * A historically important irregular temperament (c. 1691) designed to allow
 * modulation to all keys, with each key having a unique character. Used by J.S. Bach.
 *
 * This implementation is key-dependent: the cent deviation for each note depends
 * on the tonic (key) of the piece. Mode is not used.
 *
 * The mapping below is for Werckmeister III, with C as tonic. For other tonics,
 * the mapping is rotated accordingly.
 *
 * Reference: https://en.wikipedia.org/wiki/Werckmeister_temperament
 */
class WerckmeisterTemperament : public TuningSystem {
public:
    TuningSystemId id() const override { return TuningSystemId::Werckmeister; }
    const char* key() const override { return TuningKey::Werckmeister; }
    std::string displayName() const override { return "Werckmeister III"; }

    double tuningOffset(
        const mu::composing::analysis::KeyModeAnalysisResult& keyMode,
        mu::composing::analysis::ChordQuality /*quality*/,
        int /*rootPc*/,
        int semitones
    ) const override
    {
        // Werckmeister III deviations from 12-TET in cents for C major tonic.
        // Order: C, C#, D, D#, E, F, F#, G, G#, A, A#, B
        static constexpr std::array<double, 12> dev = {
            0.0,    // C
            +3.9,   // C#
            +1.0,   // D
            +5.9,   // D#
            +3.9,   // E
            +1.0,   // F
            +5.9,   // F#
            +3.9,   // G
            +1.0,   // G#
            +5.9,   // A
            +3.9,   // A#
            +1.0    // B
        };
        // Determine tonic (0-11) from key signature and mode using canonical helper
        int tonicPc = mu::composing::analysis::ionianTonicPcForMode(
            (keyMode.keySignatureFifths * 7) % 12,
            static_cast<size_t>(keyMode.mode));
        if (tonicPc < 0) tonicPc += 12;
        int idx = (semitones + 12 - tonicPc) % 12;
        return dev[idx];
    }
};

} // namespace mu::composing::intonation
