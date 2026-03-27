// SPDX-License-Identifier: GPL-3.0-only
// MuseScore Studio — Tuning system identifiers
#pragma once

namespace mu::composing::intonation {

/**
 * @brief Type-safe identifier for a tuning system.
 *
 * Use this enum in all logic and dispatch code.  Convert to/from the
 * corresponding serialization key string (below) only at persistence
 * boundaries (preferences load/save, settings UI).
 */
enum class TuningSystemId {
    EqualTemperament,
    Just,
    Pythagorean,
    QuarterCommaMeantone,
};

/**
 * @brief Stable string keys for serialization (preferences, settings files).
 *
 * These strings must never be renamed after preferences are shipped, as they
 * are stored in user settings.  Add new systems by adding a new constant and
 * a new TuningSystemId enumerator — never change existing values.
 */
namespace TuningKey {
    constexpr const char* EqualTemperament     = "equal";
    constexpr const char* Just                 = "just";
    constexpr const char* Pythagorean          = "pythagorean";
    constexpr const char* QuarterCommaMeantone = "quarter_comma_meantone";
}

} // namespace mu::composing::intonation
