// SPDX-License-Identifier: GPL-3.0-only
// MuseScore Studio — Tuning system registry implementation

#include "tuning_system.h"
#include "just_intonation.h"
#include "pythagorean.h"
#include "equal_temperament.h"
#include "quarter_comma_meantone.h"
#include <algorithm>

namespace mu::composing::intonation {

static std::vector<std::unique_ptr<TuningSystem>>& registry() {
    static std::vector<std::unique_ptr<TuningSystem>> systems;
    static bool initialized = false;
    if (!initialized) {
        systems.emplace_back(std::make_unique<JustIntonation>());
        systems.emplace_back(std::make_unique<PythagoreanTuning>());
        systems.emplace_back(std::make_unique<EqualTemperament>());
        systems.emplace_back(std::make_unique<QuarterCommaMeantone>());
        initialized = true;
    }
    return systems;
}

const std::vector<std::unique_ptr<TuningSystem>>& TuningRegistry::all() {
    return registry();
}

const TuningSystem* TuningRegistry::byKey(const std::string& key) {
    const auto& systems = registry();
    auto it = std::find_if(systems.begin(), systems.end(), [&](const std::unique_ptr<TuningSystem>& sys) {
        return sys->key() == key;
    });
    return (it != systems.end()) ? it->get() : nullptr;
}

const TuningSystem* TuningRegistry::byDisplayName(const std::string& displayName) {
    const auto& systems = registry();
    auto it = std::find_if(systems.begin(), systems.end(), [&](const std::unique_ptr<TuningSystem>& sys) {
        return sys->displayName() == displayName;
    });
    return (it != systems.end()) ? it->get() : nullptr;
}

const TuningSystem* TuningRegistry::byName(const std::string& name) {
    // Deprecated: Use byKey() for logic, byDisplayName() for UI
    return byDisplayName(name);
}

std::vector<std::string> TuningRegistry::allKeys() {
    const auto& systems = registry();
    std::vector<std::string> keys;
    for (const auto& sys : systems) {
        keys.push_back(sys->key());
    }
    return keys;
}

std::vector<std::string> TuningRegistry::allDisplayNames() {
    const auto& systems = registry();
    std::vector<std::string> names;
    for (const auto& sys : systems) {
        names.push_back(sys->displayName());
    }
    return names;
}

} // namespace mu::composing::intonation
