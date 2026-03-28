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
    Werckmeister,
    Kirnberger,
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
    constexpr const char* Werckmeister         = "werckmeister";
    constexpr const char* Kirnberger           = "kirnberger";
}

} // namespace mu::composing::intonation
