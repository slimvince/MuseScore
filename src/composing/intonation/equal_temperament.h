// SPDX-License-Identifier: GPL-3.0-only
// MuseScore Studio — 12-TET (Equal Temperament) tuning system
#pragma once

#include "tuning_system.h"
#include "tuning_keys.h"

namespace mu::composing::intonation {

/**
 * @brief 12-tone Equal Temperament.
 *
 * By definition every interval is already at its equal-tempered value, so the
 * deviation from 12-TET is always zero.  Selecting this system results in no
 * pitch adjustment being applied to any note.
 */
class EqualTemperament : public TuningSystem {
public:
    TuningSystemId id() const override { return TuningSystemId::EqualTemperament; }
    const char* key() const override { return TuningKey::EqualTemperament; }
    std::string displayName() const override { return "Equal Temperament"; }

    double tuningOffset(
        const mu::composing::analysis::KeyModeAnalysisResult& /*keyMode*/,
        mu::composing::analysis::ChordQuality /*quality*/,
        int /*rootPc*/,
        int /*semitones*/
    ) const override
    {
        return 0.0;
    }
};

} // namespace mu::composing::intonation
