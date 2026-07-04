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

#include <optional>
#include <vector>

#include "../types/analysistypes.h"

namespace mu::composing::analysis {

// KeySigMode now lives in the leaf types header analysis/types/analysistypes.h
// (included above) — a pure relocation, name and namespace unchanged. Including the
// leaf (instead of ../chord/analysisutils.h, which is where ParameterBoundsMap used
// to come from) also kills the L3 → chord/ header back-edge. See
// cowork_types_header_design.md.

/// Total number of KeySigMode values.
inline constexpr size_t KEY_MODE_COUNT = 21;

/// Index of a KeySigMode value in the mode table (same as its enum ordinal).
inline constexpr size_t keyModeIndex(KeySigMode m) { return static_cast<size_t>(m); }

/// Convert a mode table index back to a KeySigMode enum value.
inline constexpr KeySigMode keyModeFromIndex(size_t idx) { return static_cast<KeySigMode>(idx); }

/// Returns true for modes with a major third (interval 4 from tonic).
///
/// Diatonic: Ionian, Lydian, Mixolydian.
/// Melodic minor: LydianAugmented, LydianDominant, MixolydianB6.
/// Harmonic minor: IonianSharp5, PhrygianDominant, LydianSharp2.
inline constexpr bool keyModeIsMajor(KeySigMode m) {
    switch (m) {
    case KeySigMode::Ionian:
    case KeySigMode::Lydian:
    case KeySigMode::Mixolydian:
    case KeySigMode::LydianAugmented:
    case KeySigMode::LydianDominant:
    case KeySigMode::MixolydianB6:
    case KeySigMode::IonianSharp5:
    case KeySigMode::PhrygianDominant:
    case KeySigMode::LydianSharp2:
        return true;
    default:
        return false;
    }
}

/// Semitone offset of this mode's tonic from the Ionian tonic of the associated
/// key signature.  For diatonic modes: the standard church-mode offsets.
/// For non-diatonic modes: the offset of the mode's tonic from the Ionian tonic
/// of the parent key (e.g. MelodicMinor shares Dorian's offset = 2).
inline constexpr int keyModeTonicOffset(KeySigMode m) {
    constexpr int offsets[] = {
        // Diatonic (0–6)
        0, 2, 4, 5, 7, 9, 11,
        // Melodic minor family (7–13) — parent key = Bb major for C root
        2,   ///< MelodicMinor   ~ Dorian
        4,   ///< DorianB2       ~ Phrygian
        5,   ///< LydianAugmented ~ Lydian
        7,   ///< LydianDominant  ~ Mixolydian
        9,   ///< MixolydianB6   ~ Aeolian
        11,  ///< AeolianB5      ~ Locrian
        1,   ///< Altered        ~ mode-7 of melodic minor (1 above Ionian)
        // Harmonic minor family (14–20) — parent key = C major for A root
        9,   ///< HarmonicMinor  ~ Aeolian
        11,  ///< LocrianSharp6  ~ Locrian
        0,   ///< IonianSharp5   ~ Ionian
        2,   ///< DorianSharp4   ~ Dorian
        4,   ///< PhrygianDominant ~ Phrygian
        5,   ///< LydianSharp2   ~ Lydian
        8,   ///< AlteredDomBB7  ~ aug5 above Ionian (unique — no diatonic equivalent)
    };
    return offsets[static_cast<size_t>(m)];
}

/// Result of a key/mode analysis: the most likely key and mode with a confidence score.
struct KeyModeAnalysisResult {
    int keySignatureFifths = 0;          ///< Resolved key signature (-7..+7, Ionian convention)
    KeySigMode mode = KeySigMode::Ionian;      ///< Detected mode
    int tonicPc = 0;                     ///< Pitch class of the mode's tonic (0=C, 2=D, etc.)
    double score = 0.0;                  ///< Raw confidence score; higher is better
    double normalizedConfidence = 0.0;   ///< [0,1] EMISSION SIGMOID (see §5.7). Role (confidence contract §3 / D-L3a): an INTERNAL gate input (the 0.8 KeyArea/cadence annotate gate) + diagnostic export — NOT the Layer-3 boundary confidence, which is the sequence margin (SliceKeyMode.confidence → HarmonicRegion.keyConfidence).

    /// Convenience: true when mode has a major third (Ionian, Lydian, Mixolydian).
    bool isMajor() const { return keyModeIsMajor(mode); }
};

/// Diagnostic-only per-candidate score breakdown (Stage-4 emission instrument).
///
/// Filled by analyzeKeyMode ONLY when a non-null dump pointer is supplied. Every
/// production call passes nullptr and is byte-identical (the gateCtxOut/snapshotOut
/// precedent — the dump only serializes scores already computed; the selected
/// winner is unchanged). One entry per (tonicPc, modeIndex) candidate (252 total).
///
/// The six orthogonal scoring terms (ARCHITECTURE §4.2) plus the declared-mode
/// penalty and the post-hoc pairwise disambiguation delta. By construction:
///   finalScore == scaleMembership + triadEvidence + characteristicPitch
///                 + trueLeadingTone + keySignatureProximity + modePrior
///                 - declaredPenalty + disambiguationDelta
struct KeyCandidateScore {
    int tonicPc = 0;
    std::size_t modeIndex = 0;
    double scaleMembership       = 0.0;  ///< scoreScaleMembership
    double triadEvidence         = 0.0;  ///< scoreTriadEvidence (triad + complete-triad/missing-tonic + extra-scale)
    double characteristicPitch   = 0.0;  ///< scoreCharacteristicPitch
    double trueLeadingTone       = 0.0;  ///< scoreTrueLeadingTone
    double keySignatureProximity = 0.0;  ///< scoreKeySignatureProximity
    double modePrior             = 0.0;  ///< scoreModePrior
    double declaredPenalty       = 0.0;  ///< prefs.declaredModePenalty when mode incompatible with declared, else 0 (SUBTRACTED)
    double disambiguationDelta   = 0.0;  ///< post-hoc pairwise mutation applied to this candidate (signed)
    double finalScore            = 0.0;  ///< eval.score after all adjustments (the ranking score)
    double tonalCenterScore      = 0.0;  ///< family-selection tonal-centre comparison score
    double tonicWeight           = 0.0;
    double thirdWeight           = 0.0;
    double fifthWeight           = 0.0;
    double leadingToneWeight     = 0.0;
    bool   hasCompleteTriad      = false;
};

// KeyModeAnalyzerPreferences (+ kDefaultKeyModeAnalyzerPreferences) now lives in the
// leaf types header analysis/types/analysistypes.h (included above) — a pure
// relocation, name and namespace unchanged. See cowork_types_header_design.md.

class KeyModeAnalyzer
{
public:
    /// Pitch context passed from the score/notation layer into the abstract analysis.
    /// Un-nested to the leaf types header (analysis/types/analysistypes.h) as
    /// analysis::PitchContext — a pure relocation (same body, same namespace-qualified
    /// home). This member alias keeps every existing `KeyModeAnalyzer::PitchContext`
    /// call site resolving to the identical type, unchanged. See cowork_types_header_design.md.
    using PitchContext = analysis::PitchContext;

    /// Analyse key/mode from a window of pitch contexts and the local key signature.
    /// keySignatureFifths is the fixed-accidental context at the selection point (-7..+7).
    ///
    /// Returns up to 3 candidates sorted by score descending.  An empty result means
    /// insufficient pitch data to form a reliable estimate.
    /// @param declaredMode  If set, modes outside this mode's class receive
    ///                      a penalty (prefs.declaredModePenalty).  Pass
    ///                      std::nullopt (the default) to use pure pitch
    ///                      analysis with no constraint.
    /// @param dumpOut  Diagnostic-only. When non-null, cleared and filled with one
    ///                 KeyCandidateScore per (tonicPc, modeIndex) candidate (the
    ///                 emission instrument). Pass nullptr (the default) on every
    ///                 production path — output is byte-identical either way.
    static std::vector<KeyModeAnalysisResult> analyzeKeyMode(
        const std::vector<PitchContext>& pitches,
        int keySignatureFifths,
        const KeyModeAnalyzerPreferences& prefs = kDefaultKeyModeAnalyzerPreferences,
        std::optional<KeySigMode> declaredMode = std::nullopt,
        std::vector<KeyCandidateScore>* dumpOut = nullptr);
};

/// Scale degrees (semitone offsets from tonic) for every mode defined
/// by KeySigMode. Indexed by keyModeIndex(mode). Size is always 7 even
/// for modes whose scale has fewer distinct pitch classes — the table
/// expresses the canonical diatonic mapping used for Roman-numeral
/// degree lookup.
const std::array<int, 7>& keyModeScaleIntervals(KeySigMode mode);

/// Maps a modal tonic pitch class to the equivalent Ionian tonic that shares
/// the same key signature.  Defined in keymodeanalyzer.cpp; exposed here so the
/// intonation module can convert a KeyModeAnalysisResult back to an Ionian tonic
/// without depending on the full analyzeKeyMode implementation.
int ionianTonicPcForMode(int tonicPc, size_t modeIndex);

/// Maps a binary (tonicPc, isMajor) key to its notated key-signature fifths value
/// (-7..+7), choosing the enharmonic spelling nearest @p referenceFifths (the
/// notated signature).  Major → Ionian circle position; minor → relative-major
/// fifths.  Used by the J-key-iii joint-key override, whose decision is only
/// (tonicPc, isMajor); passing the notated signature as the reference pins a home
/// (signature-pair) key back to the notated fifths automatically.
int keySignatureFifthsForKey(int tonicPc, bool isMajor, int referenceFifths);

/// Resolve a full (tonicPc, mode) — any of the 21 modes — to its notated
/// key-signature fifths (-7..+7), choosing the enharmonic spelling nearest
/// @p referenceFifths (the notated signature).  A pure additive accessor over the
/// internal resolveToFifths; used by the Layer-3 key/mode sequence decoder to
/// label each lattice state's key signature.  No production scoring path calls it.
int keyModeSignatureFifths(int tonicPc, KeySigMode mode, int referenceFifths);

/// Human-readable tonic name for a (key-signature, mode) pair.
/// E.g. keyModeTonicName(0, KeySigMode::Ionian) → "C",
///      keyModeTonicName(0, KeySigMode::Dorian) → "D",
///      keyModeTonicName(-3, KeySigMode::Aeolian) → "C".
const char* keyModeTonicName(int fifths, KeySigMode mode);

/// Human-readable mode suffix for display.
/// E.g. KeySigMode::Ionian → "major", KeySigMode::Dorian → "Dorian".
const char* keyModeSuffix(KeySigMode mode);

} // namespace mu::composing::analysis
