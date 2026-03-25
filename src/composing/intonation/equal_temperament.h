// SPDX-License-Identifier: GPL-3.0-only
// MuseScore Studio — 12-TET (Equal Temperament) tuning system
#pragma once


#include "tuning_system.h"
#include "tuning_keys.h"
#include "../analysis/keymodeanalyzer.h"
#include "../analysis/chordanalyzer.h"

namespace mu::composing::intonation {

class EqualTemperament : public TuningSystem {
public:
    const char* key() const override { return TuningKey::EqualTemperament; }
    std::string displayName() const override { return "Equal Temperament"; }
    double tuningOffset(const mu::composing::analysis::KeyModeAnalysisResult&, mu::composing::analysis::ChordQuality, int, int scaleDegree) const override {
        // Return absolute offset from root for each scale degree in 12-TET
        // 1=tonic/root (0 cents), 2=major second (100 cents), ..., 7=major seventh (600 cents or 1100 cents for full octave)
        if (scaleDegree < 1 || scaleDegree > 7)
            return 0.0;
        return 100.0 * (scaleDegree - 1);
    }
};

} // namespace mu::composing::intonation
