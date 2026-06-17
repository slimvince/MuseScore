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

#include "keymodeanalyzer.h"

#include <algorithm>

namespace mu::composing::analysis {

// ── Display helpers ─────────────────────────────────────────────────────────

const char* keyModeTonicName(int fifths, KeySigMode mode)
{
    // Tonic names indexed by circle-of-fifths position +7, per mode.
    // Non-diatonic modes reuse the name array of their parent diatonic mode
    // (same key signature), except Altered (offset 1) and AlteredDomBB7 (offset 8)
    // which have unique arrays.
    static constexpr const char* IONIAN_NAMES[15] = {
        "Cb", "Gb", "Db", "Ab", "Eb", "Bb", "F",
        "C", "G", "D", "A", "E", "B", "F#", "C#"
    };
    static constexpr const char* AEOLIAN_NAMES[15] = {
        "Ab", "Eb", "Bb", "F", "C", "G", "D",
        "A", "E", "B", "F#", "C#", "G#", "D#", "A#"
    };
    static constexpr const char* DORIAN_NAMES[15] = {
        "Db", "Ab", "Eb", "Bb", "F", "C", "G",
        "D", "A", "E", "B", "F#", "C#", "G#", "D#"
    };
    static constexpr const char* PHRYGIAN_NAMES[15] = {
        "Eb", "Bb", "F", "C", "G", "D", "A",
        "E", "B", "F#", "C#", "G#", "D#", "A#", "E#"
    };
    static constexpr const char* LYDIAN_NAMES[15] = {
        "Fb", "Cb", "Gb", "Db", "Ab", "Eb", "Bb",
        "F", "C", "G", "D", "A", "E", "B", "F#"
    };
    static constexpr const char* MIXOLYDIAN_NAMES[15] = {
        "Gb", "Db", "Ab", "Eb", "Bb", "F", "C",
        "G", "D", "A", "E", "B", "F#", "C#", "G#"
    };
    static constexpr const char* LOCRIAN_NAMES[15] = {
        "Bb", "F", "C", "G", "D", "A", "E",
        "B", "F#", "C#", "G#", "D#", "A#", "E#", "B#"
    };
    // Altered: tonic = one semitone above Ionian tonic (offset 1).
    // E.g. key sig 2 flats (Bb Ionian) → B Altered.
    static constexpr const char* ALTERED_NAMES[15] = {
        "C",  "G",  "D",  "A",  "E",  "B",  "F#",
        "C#", "G#", "D#", "A#", "E#", "B#", "Fx", "Cx"
    };
    // AlteredDomBB7: tonic = aug5 above Ionian (offset 8).
    // E.g. key sig 0 (C Ionian) → G# AlteredDomBB7.
    static constexpr const char* ALTERED_DOM_BB7_NAMES[15] = {
        "Ab", "Eb", "Bb", "F", "C", "G",  "D",
        "G#", "D#", "A#", "E#","B#","Fx", "Cx", "Gx"
    };

    const int idx = std::clamp(fifths + 7, 0, 14);
    switch (mode) {
    // Diatonic
    case KeySigMode::Ionian:           return IONIAN_NAMES[idx];
    case KeySigMode::Dorian:           return DORIAN_NAMES[idx];
    case KeySigMode::Phrygian:         return PHRYGIAN_NAMES[idx];
    case KeySigMode::Lydian:           return LYDIAN_NAMES[idx];
    case KeySigMode::Mixolydian:       return MIXOLYDIAN_NAMES[idx];
    case KeySigMode::Aeolian:          return AEOLIAN_NAMES[idx];
    case KeySigMode::Locrian:          return LOCRIAN_NAMES[idx];
    // Melodic minor — share parent diatonic key sig tonic names
    case KeySigMode::MelodicMinor:     return DORIAN_NAMES[idx];
    case KeySigMode::DorianB2:         return PHRYGIAN_NAMES[idx];
    case KeySigMode::LydianAugmented:  return LYDIAN_NAMES[idx];
    case KeySigMode::LydianDominant:   return MIXOLYDIAN_NAMES[idx];
    case KeySigMode::MixolydianB6:     return AEOLIAN_NAMES[idx];
    case KeySigMode::AeolianB5:        return LOCRIAN_NAMES[idx];
    case KeySigMode::Altered:          return ALTERED_NAMES[idx];
    // Harmonic minor — share parent diatonic key sig tonic names
    case KeySigMode::HarmonicMinor:    return AEOLIAN_NAMES[idx];
    case KeySigMode::LocrianSharp6:    return LOCRIAN_NAMES[idx];
    case KeySigMode::IonianSharp5:     return IONIAN_NAMES[idx];
    case KeySigMode::DorianSharp4:     return DORIAN_NAMES[idx];
    case KeySigMode::PhrygianDominant: return PHRYGIAN_NAMES[idx];
    case KeySigMode::LydianSharp2:     return LYDIAN_NAMES[idx];
    case KeySigMode::AlteredDomBB7:    return ALTERED_DOM_BB7_NAMES[idx];
    }
    return IONIAN_NAMES[idx];
}

const char* keyModeSuffix(KeySigMode mode)
{
    switch (mode) {
    // Diatonic
    case KeySigMode::Ionian:           return "maj";
    case KeySigMode::Dorian:           return "Dor";
    case KeySigMode::Phrygian:         return "Phryg";
    case KeySigMode::Lydian:           return "Lyd";
    case KeySigMode::Mixolydian:       return "Mixolyd";
    case KeySigMode::Aeolian:          return "min";
    case KeySigMode::Locrian:          return "Loc";
    // Melodic minor family
    case KeySigMode::MelodicMinor:     return "mel";
    case KeySigMode::DorianB2:         return "Dor\u266d2";
    case KeySigMode::LydianAugmented:  return "Lyd+";
    case KeySigMode::LydianDominant:   return "Lyd\u266d7";
    case KeySigMode::MixolydianB6:     return "Mix\u266d6";
    case KeySigMode::AeolianB5:        return "Loc#2";
    case KeySigMode::Altered:          return "alt";
    // Harmonic minor family
    case KeySigMode::HarmonicMinor:    return "harm";
    case KeySigMode::LocrianSharp6:    return "Loc#6";
    case KeySigMode::IonianSharp5:     return "Ion+";
    case KeySigMode::DorianSharp4:     return "Dor#4";
    case KeySigMode::PhrygianDominant: return "PhrygDom";
    case KeySigMode::LydianSharp2:     return "Lyd#2";
    case KeySigMode::AlteredDomBB7:    return "altDom";
    }
    return "";
}

} // namespace mu::composing::analysis
