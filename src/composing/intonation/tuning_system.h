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

#include <cctype>
#include <memory>
#include <string>
#include <string_view>
#include <vector>
#include "tuning_keys.h"
#include "../analysis/key/keymodeanalyzer.h" // for KeyModeAnalysisResult
#include "../analysis/chord/chordanalyzer.h"   // for ChordQuality

namespace mu::composing::intonation {

// ── Tuning anchor ─────────────────────────────────────────────────────────────
//
// A note carrying a MuseScore Expression element with this text is treated as
// absolutely protected: zero tuning offset, never split, excluded from
// zero-sum centering.  Keyword matching is case-insensitive with leading/
// trailing whitespace trimmed.
//
// "anchor-pitch" is a placeholder — the final user-visible name is TBD.
inline constexpr const char* kTuningAnchorKeyword = "anchor-pitch";

/// Returns true when @p text, after trimming leading/trailing whitespace and
/// lower-casing, equals kTuningAnchorKeyword.
///
/// Extracted as a pure function so it can be tested without MuseScore objects.
/// hasTuningAnchorExpression() (notation bridge) calls this after lowering and
/// trimming the Expression's plainText().
inline bool isTuningAnchorText(std::string_view text)
{
    // Trim leading whitespace.
    size_t start = text.find_first_not_of(" \t\r\n");
    if (start == std::string_view::npos) { return false; }
    // Trim trailing whitespace.
    size_t end = text.find_last_not_of(" \t\r\n");
    text = text.substr(start, end - start + 1);

    if (text.size() != std::string_view(kTuningAnchorKeyword).size()) { return false; }

    // Case-insensitive comparison.
    for (size_t i = 0; i < text.size(); ++i) {
        if (std::tolower(static_cast<unsigned char>(text[i]))
                != kTuningAnchorKeyword[i]) {
            return false;
        }
    }
    return true;
}

/// How susceptible a note is to being retuned.
/// Computed per note before applying a tuning offset.
enum class RetuningSusceptibility {
    /// Zero tuning offset.  Never split.  Excluded from zero-sum centering.
    /// Highest priority: overrides all duration-based and context-based rules.
    /// Triggered by a kTuningAnchorKeyword Expression attached to the note.
    AbsolutelyProtected,

    /// Note may be retuned but must not be split across harmonic boundaries.
    /// (Reserved for future use — long sustained notes, fermatas, etc.)
    Adjustable,

    /// Note is freely retunable and may be split.
    Free,
};

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

    /**
     * @brief Returns the tuning offset in cents of the chord root relative to
     *        the mode tonic (tonic-anchored tuning).
     *
     * For tonic-anchored tuning the chord root is not assumed to sit at 0 ¢
     * from 12-TET.  Instead it is placed at its just-intonation scale-degree
     * position above the mode tonic.  Callers add this to the per-note result
     * of tuningOffset() to obtain the absolute offset for each note.
     *
     * Default implementation returns 0.0 — correct for equal temperament and
     * any system where absolute pitch class does not affect the per-note offsets.
     */
    virtual double rootOffset(
        const mu::composing::analysis::KeyModeAnalysisResult& /*keyMode*/,
        int /*rootPc*/
    ) const { return 0.0; }
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
