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
#include "../analysis/chordanalyzer.h"
#include <engraving/dom/note.h>

namespace mu::composing::intonation {

/**
 * @brief Returns the semitone interval (0–11) from a chord root to a note,
 *        given their pitch classes.
 *
 * This is the primary way to obtain the semitones argument for tuningOffset()
 * when the caller has actual pitch data (e.g. when applying tuning from the
 * "tune as" context menu).
 *
 * Example: root = D (pitch class 2), note = F# (pitch class 6) → 4 semitones.
 */
inline int semitoneFromPitches(int notePc, int rootPc)
{
    return (notePc - rootPc + 12) % 12;
}

/**
 * @brief Converts a 1-based scale degree and chord quality to a semitone
 *        interval from the chord root (0–11).
 *
 * Use this when the caller has analysis results expressed as scale degrees
 * (e.g. from ChordAnalysisResult) rather than raw pitch classes.
 *
 *   degree 3, Major quality  → 4 (major third)
 *   degree 3, Minor quality  → 3 (minor third)
 *   degree 5, Diminished     → 6 (diminished fifth)
 *   degree 5, Augmented      → 8 (augmented fifth)
 *   degree 7, Diminished     → 9 (diminished seventh)
 *   degree 7, Major          → 11 (major seventh)
 *   degree 7, Minor/other    → 10 (minor seventh)
 */
inline int semitoneInterval(int scaleDegree, mu::composing::analysis::ChordQuality quality)
{
    using Q = mu::composing::analysis::ChordQuality;
    switch (scaleDegree) {
    case 1: return 0;
    case 2: return 2;
    case 3:
        switch (quality) {
        case Q::Minor:
        case Q::Diminished:
        case Q::HalfDiminished:
            return 3;   // minor third
        default:
            return 4;   // major third
        }
    case 4: return 5;
    case 5:
        switch (quality) {
        case Q::Diminished:
        case Q::HalfDiminished:
            return 6;   // diminished fifth
        case Q::Augmented:
            return 8;   // augmented fifth
        default:
            return 7;   // perfect fifth
        }
    case 6:
        switch (quality) {
        case Q::Minor:
        case Q::Diminished:
        case Q::HalfDiminished:
            return 8;   // minor sixth
        default:
            return 9;   // major sixth
        }
    case 7:
        switch (quality) {
        case Q::Diminished:
            return 9;   // diminished seventh
        case Q::Major:
            return 11;  // major seventh
        default:
            return 10;  // minor seventh
        }
    default:
        return 0;
    }
}

/**
 * @brief Applies a tuning system to a single note.
 *
 * Computes the deviation from 12-TET via the tuning system and writes it to
 * the note with Note::setTuning().  The semitones argument is the interval
 * from the chord root to this note (0–11); use semitoneFromPitches() or
 * semitoneInterval() to obtain it.
 */
inline void tuneNote(
    mu::engraving::Note* note,
    const TuningSystem& tuningSystem,
    const mu::composing::analysis::KeyModeAnalysisResult& keyMode,
    mu::composing::analysis::ChordQuality quality,
    int rootPc,
    int semitones
) {
    if (!note) {
        return;
    }
    const double deviation = tuningSystem.tuningOffset(keyMode, quality, rootPc, semitones);
    note->setTuning(deviation);
}

} // namespace mu::composing::intonation
