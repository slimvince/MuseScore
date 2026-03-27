// SPDX-License-Identifier: GPL-3.0-only
// MuseScore Studio — Pythagorean tuning system
#pragma once

#include "tuning_system.h"
#include "tuning_keys.h"
#include <array>

namespace mu::composing::intonation {

/**
 * @brief Pythagorean tuning.
 *
 * All intervals are built from stacked pure perfect fifths (3/2 = 702.0 ¢).
 * Fifths and fourths are pure; thirds are considerably wider than just
 * (major third = 81/64 = 407.8 ¢, +7.8 ¢ vs ET).  This was the standard
 * tuning of medieval and early Renaissance polyphony, where the fifth was the
 * primary consonance and the third was treated as a dissonance.
 *
 * Notable deviations from 12-TET:
 *   minor 3rd  (32/27)   : −5.9 ¢
 *   major 3rd  (81/64)   : +7.8 ¢  (noticeably sharp)
 *   perfect 5th (3/2)    : +2.0 ¢
 *   minor 7th  (16/9)    : −3.9 ¢
 *   major 7th  (243/128) : +9.8 ¢
 *
 * Tritone disambiguation (semitone 6):
 *   augmented fourth (729/512)  : +11.7 ¢ — used for Major/Augmented chords
 *   diminished fifth (1024/729) : −11.7 ¢ — used for Diminished/HalfDiminished chords
 */
class PythagoreanTuning : public TuningSystem {
public:
    TuningSystemId id() const override { return TuningSystemId::Pythagorean; }
    const char* key() const override { return TuningKey::Pythagorean; }
    std::string displayName() const override { return "Pythagorean"; }

    double tuningOffset(
        const mu::composing::analysis::KeyModeAnalysisResult& /*keyMode*/,
        mu::composing::analysis::ChordQuality quality,
        int /*rootPc*/,
        int semitones
    ) const override
    {
        // Deviations from 12-TET in cents, indexed by semitone from chord root.
        // Ratios: 1/1, 256/243, 9/8, 32/27, 81/64, 4/3, [tritone], 3/2, 128/81, 27/16, 16/9, 243/128.
        // Semitone 6 is handled separately below due to enharmonic ambiguity.
        static constexpr std::array<double, 12> dev = {
             0.0,   //  0  unison         1/1
             -9.8,  //  1  minor 2nd      256/243
             +3.9,  //  2  major 2nd      9/8
             -5.9,  //  3  minor 3rd      32/27
             +7.8,  //  4  major 3rd      81/64
             -2.0,  //  5  perfect 4th    4/3
             0.0,   //  6  (see below)
             +2.0,  //  7  perfect 5th    3/2
             -7.8,  //  8  minor 6th      128/81
             +5.9,  //  9  major 6th      27/16
             -3.9,  // 10  minor 7th      16/9
             +9.8,  // 11  major 7th      243/128
        };

        if (semitones == 6) {
            // Augmented fourth (729/512 = 611.7 ¢) vs diminished fifth (1024/729 = 588.3 ¢)
            using Q = mu::composing::analysis::ChordQuality;
            const bool isDimFifth = (quality == Q::Diminished || quality == Q::HalfDiminished);
            return isDimFifth ? -11.7 : +11.7;
        }

        return dev[semitones < 0 || semitones > 11 ? 0 : semitones];
    }
};

} // namespace mu::composing::intonation
