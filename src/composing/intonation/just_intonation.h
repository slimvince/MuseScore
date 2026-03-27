// SPDX-License-Identifier: GPL-3.0-only
// MuseScore Studio — Just Intonation tuning system
#pragma once

#include "tuning_system.h"
#include "tuning_keys.h"
#include <array>

namespace mu::composing::intonation {

/**
 * @brief 5-limit Just Intonation.
 *
 * All intervals are expressed as deviations from 12-TET, derived from
 * small-integer frequency ratios (5-limit lattice: primes 2, 3, and 5).
 *
 * Notable deviations:
 *   major third  (5/4)  : −13.7 ¢  (the most perceptible — flatter than ET)
 *   minor third  (6/5)  : +15.6 ¢  (sharper than ET)
 *   perfect 5th  (3/2)  :  +2.0 ¢  (nearly identical to ET)
 *   minor 7th    (9/5)  : +17.6 ¢
 *   major 7th    (15/8) : −11.7 ¢
 *
 * Tritone disambiguation (semitone 6):
 *   augmented fourth (45/32) : −9.8 ¢  — used for Major/Augmented chords
 *   diminished fifth (64/45) : +9.8 ¢  — used for Diminished/HalfDiminished chords
 */
class JustIntonation : public TuningSystem {
public:
    TuningSystemId id() const override { return TuningSystemId::Just; }
    const char* key() const override { return TuningKey::Just; }
    std::string displayName() const override { return "Just Intonation"; }

    double tuningOffset(
        const mu::composing::analysis::KeyModeAnalysisResult& /*keyMode*/,
        mu::composing::analysis::ChordQuality quality,
        int /*rootPc*/,
        int semitones
    ) const override
    {
        // Deviations from 12-TET in cents, indexed by semitone from chord root.
        // Ratios: 1/1, 16/15, 9/8, 6/5, 5/4, 4/3, [tritone], 3/2, 8/5, 5/3, 9/5, 15/8.
        // Semitone 6 is handled separately below due to enharmonic ambiguity.
        static constexpr std::array<double, 12> dev = {
             0.0,   //  0  unison        1/1
            +11.7,  //  1  minor 2nd     16/15
             +3.9,  //  2  major 2nd     9/8
            +15.6,  //  3  minor 3rd     6/5
            -13.7,  //  4  major 3rd     5/4
             -2.0,  //  5  perfect 4th   4/3
             0.0,   //  6  (see below)
             +2.0,  //  7  perfect 5th   3/2
            +13.7,  //  8  minor 6th     8/5
            -15.6,  //  9  major 6th     5/3
            +17.6,  // 10  minor 7th     9/5
            -11.7,  // 11  major 7th     15/8
        };

        if (semitones == 6) {
            // Augmented fourth (45/32 = 590.2 ¢) vs diminished fifth (64/45 = 609.8 ¢)
            using Q = mu::composing::analysis::ChordQuality;
            const bool isDimFifth = (quality == Q::Diminished || quality == Q::HalfDiminished);
            return isDimFifth ? +9.8 : -9.8;
        }

        return dev[semitones < 0 || semitones > 11 ? 0 : semitones];
    }
};

} // namespace mu::composing::intonation
