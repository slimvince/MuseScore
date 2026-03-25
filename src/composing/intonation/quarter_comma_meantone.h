// SPDX-License-Identifier: GPL-3.0-only
// MuseScore Studio — Quarter-Comma Meantone tuning system
#pragma once


#include "tuning_system.h"
#include "tuning_keys.h"
#include "../analysis/keymodeanalyzer.h"
#include "../analysis/chordanalyzer.h"
#include <array>

namespace mu::composing::intonation {

class QuarterCommaMeantone : public TuningSystem {
public:
    const char* key() const override { return TuningKey::QuarterCommaMeantone; }
    std::string displayName() const override { return "Quarter-Comma Meantone"; }

    // Example: major scale degree offsets (C major, in cents)
    // 1=tonic, 2=major second, ..., 7=major seventh
    static constexpr std::array<double, 7> majorOffsets = { 0.0, 193.2, 386.3, 503.4, 696.6, 889.7, 1082.9 };
    static constexpr std::array<double, 7> minorOffsets = { 0.0, 193.2, 310.3, 503.4, 696.6, 813.7, 1006.8 };

    double tuningOffset(const mu::composing::analysis::KeyModeAnalysisResult& keyMode, mu::composing::analysis::ChordQuality, int, int scaleDegree) const override {
        if (scaleDegree < 1 || scaleDegree > 7)
            return 0.0;
        if (keyMode.mode == mu::composing::analysis::KeyMode::Ionian)
            return majorOffsets[scaleDegree - 1];
        else
            return minorOffsets[scaleDegree - 1];
    }
};

} // namespace mu::composing::intonation
