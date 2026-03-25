// SPDX-License-Identifier: GPL-3.0-only
// MuseScore Studio — Intonation infrastructure
#pragma once

#include <vector>
#include <string>
#include <memory>
#include "../analysis/keymodeanalyzer.h" // for KeyModeAnalysisResult
#include "../analysis/chordanalyzer.h"   // for ChordQuality

namespace mu::composing::intonation {

/**
 * @brief Abstract base class for all tuning systems.
 * Provides interface for cent offset calculation.
 */
class TuningSystem {
public:
    virtual ~TuningSystem() = default;


    /**
     * @brief Returns the unique key for the tuning system (for logic/lookup).
     */
    virtual const char* key() const = 0;

    /**
     * @brief Returns the (localized) display name of the tuning system.
     */
    virtual std::string displayName() const = 0;

    /**
     * @brief Returns cent offset for a note given context.
     * @param midiPitch MIDI pitch number of the note
     * @param rootPc Root pitch class of the chord
     * @param scaleDegree 1-based scale degree (1=tonic/root)
     * @return Cent offset for tuning
     */
    virtual double tuningOffset(
        const mu::composing::analysis::KeyModeAnalysisResult& keyMode,
        mu::composing::analysis::ChordQuality chordQuality,
        int rootPc,
        int scaleDegree
    ) const = 0;
};

/**
 * @brief Registry for available tuning systems.
 */
class TuningRegistry {
public:
    /**
     * @brief Returns all registered tuning systems.
     */
    static const std::vector<std::unique_ptr<TuningSystem>>& all();

    /**
     * @brief Returns a tuning system by unique key, or nullptr if not found.
     */
    static const TuningSystem* byKey(const std::string& key);

    /**
     * @brief Returns a tuning system by display name, or nullptr if not found.
     *        (For UI only; do not use for logic.)
     */
    static const TuningSystem* byDisplayName(const std::string& displayName);

    [[deprecated("Use byKey() for logic; byDisplayName() for UI")]]
    static const TuningSystem* byName(const std::string& name);
    /**
     * @brief Returns all tuning system keys (for logic/serialization).
     */
    static std::vector<std::string> allKeys();

    /**
     * @brief Returns all tuning system display names (for UI).
     */
    static std::vector<std::string> allDisplayNames();
};

} // namespace mu::composing::intonation
