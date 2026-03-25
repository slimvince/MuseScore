// SPDX-License-Identifier: GPL-3.0-only
// MuseScore Studio — Just Intonation tuning system
#pragma once


#include "tuning_system.h"
#include "tuning_keys.h"
#include "../analysis/keymodeanalyzer.h"
#include "../analysis/chordanalyzer.h"
#include <array>

namespace mu::composing::intonation {

class JustIntonation : public TuningSystem {
public:
    const char* key() const override { return TuningKey::Just; }
    std::string displayName() const override { return "Just Intonation"; }

    // Example: major scale degree offsets (C major, in cents)
    // 1=tonic, 2=major second, ..., 7=major seventh
    static constexpr std::array<double, 7> majorOffsets = { 0.0, 203.9, 386.3, 498.0, 701.9, 884.4, 1088.3 };
    static constexpr std::array<double, 7> minorOffsets = { 0.0, 203.9, 315.6, 498.0, 701.9, 813.7, 1017.6 };

    double tuningOffset(const mu::composing::analysis::KeyModeAnalysisResult& keyMode, mu::composing::analysis::ChordQuality, int, int scaleDegree) const override {
        // Use Ionian (major) or Aeolian (minor) mode for now
        if (scaleDegree < 1 || scaleDegree > 7)
            return 0.0;
        if (keyMode.mode == mu::composing::analysis::KeyMode::Ionian)
            return majorOffsets[scaleDegree - 1];
        else
            return minorOffsets[scaleDegree - 1];
    }
};

} // namespace mu::composing::intonation
