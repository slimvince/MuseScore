// SPDX-License-Identifier: GPL-3.0-only
// MuseScore Studio — Intonation utilities
#pragma once

#include "tuning_system.h"
#include <engraving/dom/note.h>

namespace mu::composing::intonation {

// Tunes a single note using the given tuning system and context
inline void tuneNote(
    mu::engraving::Note* note,
    const TuningSystem& tuningSystem,
    const KeyModeAnalysisResult& keyMode,
    ChordQuality chordQuality,
    int rootPc,
    int scaleDegree
) {
    if (!note)
        return;
    double offset = tuningSystem.tuningOffset(keyMode, chordQuality, rootPc, scaleDegree);
    note->setTuning(offset);
}

} // namespace mu::composing::intonation
