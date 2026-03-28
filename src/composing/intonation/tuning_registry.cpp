// SPDX-License-Identifier: GPL-3.0-only
// MuseScore Studio — Tuning system registry implementation

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
    static std::vector<std::unique_ptr<TuningSystem>> systems;
    static bool initialized = false;
    if (!initialized) {
        systems.emplace_back(std::make_unique<EqualTemperament>());
        systems.emplace_back(std::make_unique<JustIntonation>());
        systems.emplace_back(std::make_unique<PythagoreanTuning>());
        systems.emplace_back(std::make_unique<QuarterCommaMeantone>());
        systems.emplace_back(std::make_unique<WerckmeisterTemperament>());
        systems.emplace_back(std::make_unique<KirnbergerTemperament>());
        initialized = true;
    }
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
