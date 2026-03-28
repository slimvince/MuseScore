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

#include "tuning_system.h"
#include "just_intonation.h"
#include "pythagorean.h"
#include "equal_temperament.h"
#include "quarter_comma_meantone.h"
#include "werckmeister.h"
#include "kirnberger.h"
#include <algorithm>

namespace mu::composing::intonation {

static std::vector<std::unique_ptr<TuningSystem>>& registry()
{
    static std::vector<std::unique_ptr<TuningSystem>> systems = []() {
        std::vector<std::unique_ptr<TuningSystem>> s;
        s.emplace_back(std::make_unique<EqualTemperament>());
        s.emplace_back(std::make_unique<JustIntonation>());
        s.emplace_back(std::make_unique<PythagoreanTuning>());
        s.emplace_back(std::make_unique<QuarterCommaMeantone>());
        s.emplace_back(std::make_unique<WerckmeisterTemperament>());
        s.emplace_back(std::make_unique<KirnbergerTemperament>());
        return s;
    }();
    return systems;
}

const std::vector<std::unique_ptr<TuningSystem>>& TuningRegistry::all()
{
    return registry();
}

const TuningSystem* TuningRegistry::byId(TuningSystemId id)
{
    for (const auto& sys : registry()) {
        if (sys->id() == id) {
            return sys.get();
        }
    }
    return nullptr;
}

const TuningSystem* TuningRegistry::byKey(const std::string& key)
{
    for (const auto& sys : registry()) {
        if (sys->key() == key) {
            return sys.get();
        }
    }
    return nullptr;
}

const TuningSystem* TuningRegistry::byDisplayName(const std::string& displayName)
{
    for (const auto& sys : registry()) {
        if (sys->displayName() == displayName) {
            return sys.get();
        }
    }
    return nullptr;
}

const TuningSystem* TuningRegistry::byName(const std::string& name)
{
    return byDisplayName(name);
}

std::vector<TuningSystemId> TuningRegistry::allIds()
{
    std::vector<TuningSystemId> ids;
    for (const auto& sys : registry()) {
        ids.push_back(sys->id());
    }
    return ids;
}

std::vector<std::string> TuningRegistry::allKeys()
{
    std::vector<std::string> keys;
    for (const auto& sys : registry()) {
        keys.push_back(sys->key());
    }
    return keys;
}

std::vector<std::string> TuningRegistry::allDisplayNames()
{
    std::vector<std::string> names;
    for (const auto& sys : registry()) {
        names.push_back(sys->displayName());
    }
    return names;
}

} // namespace mu::composing::intonation
