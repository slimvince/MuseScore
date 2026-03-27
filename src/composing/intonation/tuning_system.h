// SPDX-License-Identifier: GPL-3.0-only
// MuseScore Studio — Intonation infrastructure
#pragma once

#include <vector>
#include <string>
#include <memory>
#include "tuning_keys.h"
#include "../analysis/keymodeanalyzer.h" // for KeyModeAnalysisResult
#include "../analysis/chordanalyzer.h"   // for ChordQuality

namespace mu::composing::intonation {

/**
 * @brief Abstract base class for all tuning systems.
 *
 * tuningOffset() returns the deviation in cents from 12-TET for a given note.
 * A positive value means the note should be tuned sharp of equal temperament;
 * negative means flat.  Pass this value directly to Note::setTuning().
 *
 * The note is identified by its semitone interval from the chord root (0–11),
 * which is unambiguous for any pitch including chromatic passing tones.
 * Use tuning_utils.h helpers to compute this from pitch or scale degree.
 *
 * chordQuality is needed to disambiguate enharmonically equivalent intervals
 * (notably: augmented fourth vs. diminished fifth at semitone 6, and to
 * choose the correct third/fifth/seventh size for a given chord type).
 */
class TuningSystem {
public:
    virtual ~TuningSystem() = default;

    /// Type-safe identifier for use in logic and dispatch.
    virtual TuningSystemId id() const = 0;

    /// Stable string key for serialization (preferences, settings files).
    virtual const char* key() const = 0;

    /// Display name shown in the UI.
    virtual std::string displayName() const = 0;

    /**
     * @brief Returns the tuning deviation in cents from 12-TET.
     *
     * @param keyMode  Inferred key and mode.  Available for systems that
     *                 need it; currently unused by the shipped implementations
     *                 because chord quality fully determines interval sizes
     *                 for all chord tones.
     * @param quality  Quality of the chord this note belongs to.  Used to
     *                 disambiguate enharmonically equivalent intervals and to
     *                 choose the correct interval size for thirds, fifths, and
     *                 sevenths.
     * @param rootPc   Root pitch class (0–11).  Available for systems that
     *                 require absolute pitch; currently unused.
     * @param semitones  Semitone interval from the chord root (0–11).
     *                   Compute via semitoneFromPitches() or
     *                   semitoneInterval() from tuning_utils.h.
     * @return Cents deviation from 12-TET.  Positive = sharper, negative = flatter.
     */
    virtual double tuningOffset(
        const mu::composing::analysis::KeyModeAnalysisResult& keyMode,
        mu::composing::analysis::ChordQuality quality,
        int rootPc,
        int semitones
    ) const = 0;
};

/**
 * @brief Registry for available tuning systems.
 */
class TuningRegistry {
public:
    /// Returns all registered tuning systems.
    static const std::vector<std::unique_ptr<TuningSystem>>& all();

    /// Primary lookup — by type-safe id.  Returns nullptr if not found.
    static const TuningSystem* byId(TuningSystemId id);

    /// Deserialization lookup — by string key.  Returns nullptr if not found.
    /// Prefer byId() in all logic code.
    static const TuningSystem* byKey(const std::string& key);

    /// UI lookup — by display name.  Returns nullptr if not found.
    /// Do not use for logic or serialization.
    static const TuningSystem* byDisplayName(const std::string& displayName);

    [[deprecated("Use byId() for logic; byKey() for deserialization; byDisplayName() for UI")]]
    static const TuningSystem* byName(const std::string& name);

    /// Returns all tuning system ids (for iteration).
    static std::vector<TuningSystemId> allIds();

    /// Returns all string keys (for serialization).
    static std::vector<std::string> allKeys();

    /// Returns all display names (for UI).
    static std::vector<std::string> allDisplayNames();
};

} // namespace mu::composing::intonation
