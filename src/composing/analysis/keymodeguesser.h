/*
 * SPDX-License-Identifier: GPL-3.0-only
 * MuseScore-Studio-CLA-applies
 */

#ifndef MU_COMPOSING_ANALYSIS_KEYMODEGUESSER_H
#define MU_COMPOSING_ANALYSIS_KEYMODEGUESSER_H

#include <vector>

namespace mu::composing::analysis {

struct KeyModeGuessResult {
    int keySignatureFifths = 0;
    bool isMajor = true;
    double score = 0.0;
    bool isValid = false;
};

class KeyModeGuesser
{
public:
    // Pitch context passed from the score/notation layer into the abstract analysis.
    // Carries duration and metric weight so longer, metrically-strong notes have more influence.
    struct PitchContext {
        int pitch = 0;               // MIDI pitch number
        int tpc = 0;                 // Tonal pitch class (reserved for future spelling-aware features)
        double durationWeight = 1.0; // Duration in quarter-note units; larger = more influence
        double beatWeight = 1.0;     // Metric position: 1.0=downbeat, ~0.2=offbeat
        bool isBass = false;         // True if lowest sounding pitch at this time instant
    };

    // Guess key/mode from a window of pitch contexts and the local key signature.
    // keySignatureFifths is the fixed-accidental context at the selection point (-7..+7).
    static KeyModeGuessResult guessKeyMode(const std::vector<PitchContext>& pitches,
                                           int keySignatureFifths);
};

} // namespace mu::composing::analysis

#endif // MU_COMPOSING_ANALYSIS_KEYMODEGUESSER_H
