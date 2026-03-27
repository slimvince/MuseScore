// SPDX-License-Identifier: GPL-3.0-only
// MuseScore Studio — Quarter-Comma Meantone tuning system
#pragma once

#include "tuning_system.h"
#include "tuning_keys.h"
#include <array>

namespace mu::composing::intonation {

/**
 * @brief Quarter-Comma Meantone tuning.
 *
 * The standard tuning of the Renaissance and early Baroque.  The perfect fifth
 * is narrowed by 1/4 syntonic comma (~5.4 ¢) so that four consecutive fifths
 * produce a pure major third (5/4 = 386.3 ¢).  This gives very pure major
 * thirds at the cost of slightly flat fifths (696.6 ¢ vs 702.0 ¢ just).
 *
 * Notable deviations from 12-TET:
 *   major 3rd  : −13.7 ¢  (= pure 5/4, same as Just Intonation)
 *   minor 3rd  : +10.3 ¢
 *   perfect 5th: −3.4 ¢
 *   major 7th  : −17.1 ¢
 *
 * Tritone disambiguation (semitone 6) — the largest difference of any system:
 *   augmented fourth : −20.5 ¢  (579.5 ¢) — used for Major/Augmented chords
 *   diminished fifth : +20.5 ¢  (620.5 ¢) — used for Diminished/HalfDiminished chords
 *
 * Meantone has a "wolf" fifth between the enharmonic pair G#/Ab that is not
 * represented here; this system assumes the key is within the well-tempered
 * range of roughly 3 flats to 3 sharps.
 */
class QuarterCommaMeantone : public TuningSystem {
public:
    TuningSystemId id() const override { return TuningSystemId::QuarterCommaMeantone; }
    const char* key() const override { return TuningKey::QuarterCommaMeantone; }
    std::string displayName() const override { return "Quarter-Comma Meantone"; }

    double tuningOffset(
        const mu::composing::analysis::KeyModeAnalysisResult& /*keyMode*/,
        mu::composing::analysis::ChordQuality quality,
        int /*rootPc*/,
        int semitones
    ) const override
    {
        // Deviations from 12-TET in cents, indexed by semitone from chord root.
        // Semitone 6 is handled separately due to enharmonic ambiguity —
        // the meantone aug4 and dim5 differ by ~41 ¢, the largest split of any system here.
        static constexpr std::array<double, 12> dev = {
             0.0,   //  0  unison              (0.0 ¢)
            +17.1,  //  1  diatonic semitone   (117.1 ¢)
             -6.8,  //  2  major 2nd           (193.2 ¢)
            +10.3,  //  3  minor 3rd           (310.3 ¢)
            -13.7,  //  4  major 3rd           (386.3 ¢ = pure 5/4)
             +3.4,  //  5  perfect 4th         (503.4 ¢)
             0.0,   //  6  (see below)
             -3.4,  //  7  perfect 5th         (696.6 ¢)
            +13.7,  //  8  minor 6th           (813.7 ¢)
            -10.3,  //  9  major 6th           (889.7 ¢)
             +6.8,  // 10  minor 7th           (1006.8 ¢)
            -17.1,  // 11  major 7th           (1082.9 ¢)
        };

        if (semitones == 6) {
            // Aug4 (579.5 ¢) vs dim5 (620.5 ¢) — a ~41 ¢ split unique to meantone.
            using Q = mu::composing::analysis::ChordQuality;
            const bool isDimFifth = (quality == Q::Diminished || quality == Q::HalfDiminished);
            return isDimFifth ? +20.5 : -20.5;
        }

        return dev[semitones < 0 || semitones > 11 ? 0 : semitones];
    }
};

} // namespace mu::composing::intonation
