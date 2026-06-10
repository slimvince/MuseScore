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
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <memory>
#include <string>
#include <vector>

#include "analysisutils.h"
#include "../key/keymodeanalyzer.h"

// Forward declaration — avoids a circular include with harmonicfunctionlayer.h
// (which itself includes this header). Full definition of ScoringSnapshot is in
// harmonicfunctionlayer.h.
namespace mu::composing::function {
struct ScoringSnapshot;

/// Scoring phase for applyHarmonicFunction(). Selects whether the competition
/// pipeline applies the progression signals (w_seq / w_dim / step bonuses) and Gate R.
///
/// Defined HERE rather than in harmonicfunctionlayer.h on purpose: ChordAnalyzerPreferences
/// carries a ScoringPhase, and chordanalyzer.h cannot include harmonicfunctionlayer.h —
/// the include runs the other way (see the forward declaration above). A forward-declared
/// enum would not satisfy the `= ScoringPhase::Final` default member initializer either.
/// harmonicfunctionlayer.h sees the full definition through its include of this header.
enum class ScoringPhase : uint8_t {
    Segmentation, ///< Boundary exploration — progression signals suppressed and Gate R
                  ///< skipped; rootContinuityBonus stays active (segmentation depends on it).
    Final         ///< Per-region final scoring — all signals active.
};
} // namespace mu::composing::function

namespace mu::composing::analysis {

/// Number of chord templates the scorer ranks against. SINGLE SOURCE OF TRUTH for every
/// template-sized array, eliminating the silent stack-overrun class (B1, 2026-06-04):
///   - the `templates` and `kDiagTemplates` TemplateDef arrays in chordanalyzer.cpp,
///   - the three score matrices basisIndepMatrix / complexityFactorMatrix / augFactorMatrix
///     (inner extent) in chordanalyzer.cpp,
///   - the `kMasks` interval-bitmask table and its bounds check in
///     harmonicfunctionlayer.cpp (referenced there as `analysis::kTemplateCount`).
/// Placed in the `analysis` namespace because the template set is owned by the chord
/// scorer; the function layer's kMasks mirror is a dependent — matching the include
/// direction harmonicfunctionlayer.h → chordanalyzer.h. Adding a template = bump this
/// constant and add the matching entries; the compiler then enforces every array's size.
/// See docs/scoring_model.md §3 and §9.
inline constexpr std::size_t kTemplateCount = 17;

enum class ChordQuality {
    Unknown,
    Major,
    Minor,
    Diminished,
    Augmented,
    HalfDiminished,
    Suspended2,
    Suspended4,
    Power
};

struct ChordAnalysisTone {
    int pitch = 0;      // MIDI playback pitch (ppitch — honours ottavas and transpositions)
    int tpc = -1;       // MuseScore TPC (0–34, circle-of-fifths spelling). -1 = not provided.
    double weight = 1;  // Relative evidence weight (duration × metric weight, normalised to [0,1])
    bool isBass = false;

    // ── Regional accumulation fields (§4.1c) ───────────────────────────────
    // Populated by collectRegionTones(); 0 when using the legacy single-tick path.

    /// Total duration of this pitch class within the harmonic region, in ticks.
    /// Summed across all voices and all note events that fall within [startTick, endTick).
    int durationInRegion = 0;

    /// Number of distinct metric positions (beat onsets) within the region at
    /// which this pitch class appears in at least one voice.  Used by Pass 2
    /// (repetition boost) to reward pitch classes that recur at multiple beats.
    int distinctMetricPositions = 0;

    /// Maximum number of voices in which this pitch class sounds simultaneously
    /// at any single tick within the region.  Used by Pass 3 (cross-voice boost)
    /// to reward pitch classes reinforced by multiple voices at once.
    int simultaneousVoiceCount = 0;

    /// True when this tone has at least one attack at the region's startTick.
    /// Used by Iter 92 joint (bass, chord) scoring to distinguish beat-onset
    /// bass candidates from passing-tone mid-region bass candidates.
    /// Set by collectRegionTones; left at the default false on single-segment
    /// tone-collection paths (status-bar analysis).
    bool onsetAtRegionStart = false;
};

inline void normalizeMergedBassTone(std::vector<ChordAnalysisTone>& tones)
{
    if (tones.empty()) {
        return;
    }

    size_t lowestIndex = 0;
    for (size_t index = 1; index < tones.size(); ++index) {
        if (tones[index].pitch < tones[lowestIndex].pitch) {
            lowestIndex = index;
        }
    }

    for (auto& tone : tones) {
        tone.isBass = false;
    }
    tones[lowestIndex].isBass = true;
}

inline void mergeChordAnalysisTones(std::vector<ChordAnalysisTone>& existingTones,
                                    const std::vector<ChordAnalysisTone>& newTones)
{
    for (const auto& newTone : newTones) {
        ChordAnalysisTone* mergedTone = nullptr;
        for (auto& existingTone : existingTones) {
            if ((existingTone.pitch % 12) == (newTone.pitch % 12)) {
                mergedTone = &existingTone;
                break;
            }
        }

        if (!mergedTone) {
            existingTones.push_back(newTone);
            continue;
        }

        mergedTone->weight += newTone.weight;
        mergedTone->durationInRegion += newTone.durationInRegion;
        mergedTone->distinctMetricPositions += newTone.distinctMetricPositions;
        if (newTone.simultaneousVoiceCount > mergedTone->simultaneousVoiceCount) {
            mergedTone->simultaneousVoiceCount = newTone.simultaneousVoiceCount;
        }
        if (newTone.onsetAtRegionStart) {
            mergedTone->onsetAtRegionStart = true;
        }
        if (newTone.pitch < mergedTone->pitch) {
            mergedTone->pitch = newTone.pitch;
            mergedTone->tpc = newTone.tpc;
        } else if (mergedTone->tpc == -1 && newTone.tpc != -1) {
            mergedTone->tpc = newTone.tpc;
        }
    }

    normalizeMergedBassTone(existingTones);
}

inline const ChordAnalysisTone* bassToneFromTones(const std::vector<ChordAnalysisTone>& tones)
{
    const ChordAnalysisTone* bassTone = nullptr;
    for (const auto& tone : tones) {
        if (!tone.isBass) {
            continue;
        }
        if (!bassTone || tone.pitch < bassTone->pitch) {
            bassTone = &tone;
        }
    }
    return bassTone;
}

/// Returns true if two pitch classes are a diatonic step apart
/// (chromatic interval of 1 or 2 semitones, shortest path).
inline bool isDiatonicStep(int pc1, int pc2) noexcept
{
    int interval = std::abs(pc1 - pc2);
    interval = std::min(interval, 12 - interval);
    return interval == 1 || interval == 2;
}

// ── Extension bitmask ────────────────────────────────────────────────────────

/// Chord extension and alteration flags.  Stored as a bitmask in ChordIdentity.
/// Use hasExtension() / setExtension() rather than raw bit operations.
enum class Extension : uint32_t {
    MinorSeventh      = 1u << 0,   ///< b7 — minor seventh
    MajorSeventh      = 1u << 1,   ///< M7 — major seventh
    DiminishedSeventh = 1u << 2,   ///< dim7 (9 semitones) — Diminished quality only
    AddedSixth        = 1u << 3,   ///< Added sixth (no seventh)
    FlatNinth         = 1u << 4,   ///< b9
    NaturalNinth      = 1u << 5,   ///< Natural 9th (add9 / sus, or upper extension)
    SharpNinth        = 1u << 6,   ///< #9
    NaturalEleventh   = 1u << 7,   ///< 11th (sus4 or upper extension)
    SharpEleventh     = 1u << 8,   ///< #11 / Lydian dominant
    FlatThirteenth    = 1u << 9,   ///< b13
    NaturalThirteenth = 1u << 10,  ///< 13th
    SharpThirteenth   = 1u << 11,  ///< #13
    FlatFifth         = 1u << 12,  ///< b5 alteration
    SharpFifth        = 1u << 13,  ///< #5 alteration
    OmitsThird        = 1u << 14,  ///< No third present (power chord / open voicing)
    SixNine           = 1u << 15,  ///< 6/9 chord special case
};

inline bool hasExtension(uint32_t ext, Extension flag)
{
    return (ext & static_cast<uint32_t>(flag)) != 0;
}

inline bool hasAnyNinth(uint32_t ext)
{
    return hasExtension(ext, Extension::FlatNinth)
        || hasExtension(ext, Extension::NaturalNinth)
        || hasExtension(ext, Extension::SharpNinth);
}

inline bool hasAnyThirteenth(uint32_t ext)
{
    return hasExtension(ext, Extension::FlatThirteenth)
        || hasExtension(ext, Extension::NaturalThirteenth)
        || hasExtension(ext, Extension::SharpThirteenth);
}

inline void setExtension(uint32_t& ext, Extension flag)
{
    ext |= static_cast<uint32_t>(flag);
}

// ── ChordIdentity ─────────────────────────────────────────────────────────────

/// The pitch-content identity of a chord: root, quality, extensions, and bass.
/// Contains no key-function information.
struct ChordIdentity {
    double score = 0.0;                ///< Template match score (higher = better); ranking only.
    int rootPc = 0;           ///< Root pitch class (0–11)
    int rootTpc = -1;         ///< Root TPC for enharmonic-correct naming; -1 = unknown
    int bassPc = 0;           ///< Bass pitch class (0–11)
    int bassTpc = -1;         ///< Bass TPC for enharmonic-correct naming; -1 = unknown
    /// True if the perfect fifth above root is present in the input tones.
    /// Used by the augmented sixth classifier to distinguish Italian +6 (no P5)
    /// from German +6 (has P5). Both carry SharpThirteenth when TPC data is present.
    bool naturalFifthPresent = false;
    ChordQuality quality = ChordQuality::Unknown;
    int tiePriority = -1;     ///< Template index (E2c: used by applyHarmonicFunction
                              ///< to match snapshot cells back to result candidates).
    uint32_t extensions = 0;  ///< Extension/alteration bitmask (see Extension enum)

    /// True when the bass note is a structural pedal point: it is not a chord
    /// tone of the upper-voice harmony and the upper voices produce a confident
    /// independent chord (confidence ≥ pedalConfidenceThreshold).  When true,
    /// the chord label describes the upper-voice harmony, not the full sonority,
    /// and pedalBassPc identifies the sustained pedal note.
    bool isPedalPoint = false;
    int pedalBassPc = -1;  ///< Pedal bass pitch class; -1 when isPedalPoint is false
};

// ── ChordFunction ─────────────────────────────────────────────────────────────

/// The tonal function of a chord within its key and mode context.
struct ChordFunction {
    int degree = -1;           ///< 0..6 when diatonic degree is known; -1 otherwise
    bool diatonicToKey = false;

    // Key context — stored so formatRomanNumeral() can generate chromatic
    // numerals (♭VII, ♭III, etc.) even when degree == -1 (non-diatonic root).
    int keyTonicPc = 0;
    KeySigMode keyMode = KeySigMode::Ionian;

    /// Root pitch class of the immediately following chord region (-1 = unknown).
    /// Populated by the harmonic rhythm bridge after all regions are identified
    /// (two-pass). Used by formatRomanNumeral() to emit V/x and vii°/x labels.
    /// Always -1 for status-bar / single-note analysis.
    int nextRootPc = -1;
};

// ── ChordAnalysisResult ───────────────────────────────────────────────────────

/// Abstract analysis result — contains only harmonic data, no formatting.
/// An empty result vector from analyzeChord() signals insufficient data.
struct ChordAnalysisResult {
    ChordIdentity identity;
    ChordFunction function;
};

/// Raw per-cell scoring output from the joint-scoring loop, before
/// buildChordResult() and gate post-processing. Used by applyPostScoringGates()
/// fallback paths (Gates A-FM2 and G-E) that may need to promote a cell
/// not in the top-N results.
struct RawCandidate {
    double score;
    double appliedBassBonus;
    int rootPc;
    ChordQuality quality;
    int tiePriority;  // template index; lower = preferred on equal score
    double wDimDelta; // Iter 97a-v3 — w_dim bonus applied to score (for post-bonus quality guard)
};

/// Forward declaration — full definition appears after RuleBasedChordAnalyzer.
/// Needed here so analyzeChord()'s `PostScoringGateContext* gateCtxOut` param
/// is well-formed at the point the interface is declared.
struct PostScoringGateContext;

/// Tunable parameters for chord analysis.
///
/// All values are compile-time defaults.  When MuseScore's user-preferences
/// infrastructure is wired in, replace each initialiser with a lookup from the
/// settings store.  Until then, tweak the constants here.
struct ChordAnalyzerPreferences {

    // ── Scoring weights ─────────────────────────────────────────────────────

    /// Added to the score when the candidate root equals the bass note.
    double bassNoteRootBonus = 0.70;

    /// Multiplier applied to bassNoteRootBonus when the bass note is supported by a
    /// weaker but still chord-defining shell: a major/minor third without a fifth,
    /// a root-fifth shell whose third is omitted, or a bare suspended triad.
    /// Range: 0.0–1.0. Default: 0.3.
    double bassRootThirdOnlyMultiplier = 0.3;

    /// Multiplier applied to bassNoteRootBonus when the bass note has neither a
    /// major/minor third nor a perfect fifth above it in the accumulated tones.
    /// Range: 0.0–1.0. Default: 0.1.
    double bassRootAloneMultiplier = 0.1;

    /// Added to the score when the candidate root belongs to the current key scale.
    double diatonicRootBonus = 0.30;

    /// Added per chord-tone whose enharmonic spelling (TPC) matches the expected
    /// spelling for the candidate root and quality.  Only applied when TPC data
    /// is present in the input tones (ChordAnalysisTone::tpc != -1).
    double tpcConsistencyBonusPerTone = 0.20;

    /// Added to a candidate whose root matches the previous chord's root.
    /// Resolves ambiguous root choices in favour of root continuity.
    double rootContinuityBonus = 0.40;

    /// Added to a candidate when the previous chord's quality implies a typical
    /// harmonic resolution to this root.
    ///   - Diminished → Major/Minor a semitone above  (viio → I, e.g. Bdim → C)
    ///   - HalfDiminished → Major a perfect fourth above  (ii∅ → V, e.g. Bm7b5 → E)
    ///   - Augmented → Major/Minor at the same root  (I+ → I returning, e.g. C+ → C)
    double resolutionBonus = 0.35;

    // TODO (ARCHITECTURE.md §4.1c): These four score-addition signals belong in the
    // post-ranking correction layer, not in the vertical sonority scorer. They are
    // left here as pre-existing technical debt; do not add further contextual signals
    // to this section.

    // ── Contextual inversion bonuses (§4.1b) ───────────────────────────────

    /// Bonus applied to a non-bass-root candidate when the current
    /// bass note moves by diatonic step FROM the previous region's
    /// bass note.  Stepwise bass motion strongly implies inversion —
    /// root-position chords produce leaping bass lines while inverted
    /// chords enable smooth stepwise bass.
    /// Only fires when candidate.rootPc != bassPc (inverted reading).
    /// Only fires for Major or Minor quality candidates.
    /// Range: 0.0–2.0.  Default: 0.5.
    double stepwiseBassInversionBonus = 0.5;

    /// Bonus applied to a non-bass-root candidate when the current
    /// bass note also moves by diatonic step TO the next region's
    /// bass note.  Both-direction stepwise motion is the strongest
    /// linear bass signal available without full sequence analysis.
    /// Only fires when nextBassPc is known (chord staff analysis only).
    /// Only fires for Major or Minor quality candidates.
    /// Range: 0.0–2.0.  Default: 0.5.
    double stepwiseBassLookaheadBonus = 0.5;

    /// Bonus applied to an inverted triad candidate when all three chord tones
    /// are present in a 3-pitch-class texture. This helps complete first- or
    /// second-inversion triads outrank bass-root shell readings in walking-bass
    /// passages without affecting denser sonorities.
    /// Only fires for Major, Minor, or Diminished quality candidates.
    /// Range: 0.0–2.0. Default: 0.45.
    double completeTriadInversionBonus = 0.45;

    /// Bonus applied to a non-bass-root candidate when the candidate
    /// root matches the previous region's root (same harmony, different
    /// inversion).  Bass arpeggiation — I → I6 → I — is one of the
    /// most common inversion usages in tonal music.
    /// Only fires when candidate.rootPc != bassPc (inverted reading).
    /// Only fires for Major or Minor quality candidates.
    /// Range: 0.0–2.0.  Default: 0.4.
    double sameRootInversionBonus = 0.4;

    /// Maximum total context bonus that can be applied to any single inversion
    /// candidate across ALL temporal signals combined (stepwise, lookahead,
    /// sameRoot, completeTriad, nextRoot, consecutive, recentRoot, weakBeat).
    /// Prevents runaway stacking when multiple signals fire simultaneously.
    /// Default 2.0 — slightly above the old implicit ceiling of 1.85 so new
    /// signals can contribute marginally at default prefs without large risk.
    /// Baroque: 2.5 — ~0.65 headroom above old max for amplified signals.
    /// Jazz: 0.6 — inversion bonuses heavily suppressed.
    /// Range: 0.0–10.0.  Default: 2.0.
    double maxTotalInversionContextBonus = 2.0;

    // ── Inversion / bass-root bias correction ──────────────────────────────
    //
    // When the winning candidate beat the best non-bass alternative by less
    // than inversionSuspicionMargin, and a clean (triadic) non-bass alternative
    // exists and noteCount >= 3, the bass-root bonus is suspected of firing
    // incorrectly on an inverted chord.  The bonus contribution to the winner's
    // score is reduced by (1 - inversionBonusReduction) * bassNoteRootBonus,
    // then candidates are re-sorted.
    //
    // inversionSuspicionMargin = 0 disables the correction entirely.
    // inversionBonusReduction = 1.0 means no reduction (NOP).
    // inversionBonusReduction = 0.0 removes the bonus entirely for close-margin cases.
    //
    // Empirically tuned from Section 6.1 validation data (Bach chorales):
    //   - 86.1% of confirmed genuine errors have margin < 0.25
    //   - 100.0% of confirmed genuine errors have margin < 1.0
    //   - 0% of genuine errors have noteCount < 3
    // A margin threshold of 0.70 (= bassNoteRootBonus) catches all cases where
    // the bonus is the sole reason the bass-root candidate wins.

    /// Score-margin threshold below which the inversion correction activates.
    /// Must be >= 0. Set to 0 to disable the correction.
    /// Default: 0.70 (= bassNoteRootBonus — bass bonus is sole deciding factor).
    double inversionSuspicionMargin = 0.70;

    /// Multiplier applied to the bass-root bonus reduction when the correction fires.
    /// 1.0 = no reduction (NOP).  0.0 = remove the bonus contribution entirely.
    /// Default: 0.0 — fully remove the bonus so the non-bass alternative wins.
    double inversionBonusReduction = 0.0;

    /// When true, prefer a Minor reading over a bass-root Major reading when the
    /// two span identical pitch classes (the enharmonic Major-add6 / Minor7 pair:
    /// e.g. Bb6 vs Gm7/Bb, C6 vs Am7/C).  The preference is applied unconditionally
    /// — no margin check — because score-based discrimination cannot reliably
    /// resolve this pair in bass-heavy textures.
    /// Set true for Standard and Baroque presets where added-sixth chords are rare;
    /// leave false for Jazz where C6, Bb6, etc. are idiomatic labels.
    /// Default: false.
    bool preferMinorOverMajorAdd6 = false;

    // ── Harmonic boundary detection (§4.1c) ────────────────────────────────

    /// Jaccard distance threshold for the beat-window boundary detector.
    /// Jaccard distance = 1 - |A∩B| / |A∪B| where A and B are the pitch-class
    /// bitsets of two consecutive quarter-note windows.
    /// Values in [0,1]; 0 = identical harmony, 1 = no shared pitch classes.
    /// 0.6 catches strong harmonic changes while ignoring ornamental tones.
    /// Only used when useRegionalAccumulation is true.
    /// Range: 0.0–1.0.  Default: 0.6.
    double harmonicBoundaryJaccardThreshold = 0.6;

    /// Multiplier applied to the discounted sustain-pedal tail added after a
    /// note's written note-off and before the pedal release.
    /// Values in [0,1]; 0 disables pedal tails, 1 treats the tail as strongly
    /// as the written attack weight.
    double pedalTailWeightMultiplier = 0.3;

    /// Minimum weight fraction for a tone to be considered a valid bass-note candidate.
    /// A tone whose weight is less than (fraction × total_weight) is treated as a
    /// chromatic passing tone or ornament and excluded from slash-chord bass selection.
    /// Set to 0.0 to disable the filter (all tones are valid bass candidates).
    /// Range: 0.0–0.5.  Default: 0.05 (5 % of accumulated weight).
    double bassPassingToneMinWeightFraction = 0.05;

    // ── Extension detection threshold ──────────────────────────────────────
    //
    // Jazz voicings routinely place the ninth at pcWeight 0.12–0.19 (below the
    // conservative 0.20 used to suppress ornamental passing tones in counterpoint
    // textures).  Setting this to kSeventhThreshold (0.12) for the Jazz preset
    // allows lightly-voiced ninths to register without disturbing classical corpora.
    // Standard and Baroque keep the conservative 0.20 default.

    /// Minimum pcWeight for chord extensions (9th, 11th, 13th, alterations).
    /// Jazz preset should use 0.12 (= kSeventhThreshold) to detect lightly-voiced
    /// ninths.  Standard/Baroque use 0.20 to suppress Baroque passing tones.
    /// Range: 0.10–0.30.  Default: 0.20.
    double extensionThreshold = 0.20;

    /// Minimum number of distinct pitch classes (counted at pcWeight > 0.05) for
    /// analyzeChord() to return any candidates. SATB chorale regions always have
    /// 3+ distinct PCs and gate at the conservative default; thin-PC entry points
    /// in non-SATB textures (e.g. Corelli trio sonata dominant beats — G unison,
    /// G+B dyad) need the gate relaxed to be scored at all. greedyExpandSegmentation
    /// sets this to 1 so it can promote sparse anchors; all other callers keep 3.
    /// Range: 1–3.  Default: 3.
    int minDistinctPcsForCandidate = 3;

    /// Scoring phase forwarded to applyHarmonicFunction().  Set to
    /// `function::ScoringPhase::Segmentation` for boundary-exploration calls
    /// (greedyExpandSegmentation's internal analyzeChord calls): this suppresses the
    /// progression signals (w_seq / w_dim / step bonuses) and skips Gate R, which would
    /// otherwise bias sub-region bass selection and shift region boundaries before the
    /// final per-region scoring pass runs.  rootContinuityBonus stays active in both
    /// phases — segmentation depends on it.  The default
    /// `function::ScoringPhase::Final` is used by all per-region analysis calls
    /// (bridge / batch_analyze, after segmentation returns boundaries) so every signal
    /// applies.
    function::ScoringPhase scoringPhase = function::ScoringPhase::Final;

    // ── Pedal point detection (§5.12) ───────────────────────────────────────

    /// Minimum confidence for the upper-voice-only Pass 2 result to confirm a
    /// structural pedal point.  Confidence is computed inline as a sigmoid of
    /// the score gap to the best different-root competitor (midpoint=2.0,
    /// steepness=1.5).  If below this threshold, the full-sonority Pass 1 result
    /// is kept and no pedal annotation is made.
    /// Conservative default — only flag very confident pedals.
    /// Range: 0.3–0.95.  Default: 0.65.
    double pedalConfidenceThreshold = 0.65;

    // ── Score annotations (future — not yet implemented) ────────────────────
    // These are intentionally off.  When the score-annotation pipeline is ready,
    // flip them on and wire up the corresponding logic.

    /// Use an explicit chord symbol written in the score to constrain / override
    /// the analysis at that tick.
    bool useExistingChordSymbols = false;       // TODO: implement

    /// Use Roman-numeral annotations written in the score as prior context.
    bool useRomanNumeralAnnotations = false;    // TODO: implement

    /// Use Nashville-number annotations written in the score as prior context.
    bool useNashvilleAnnotations = false;       // TODO: implement

    // ── Scoring snapshot ─────────────────────────────────────────────────────
    //
    // analyzeChord() now always builds a ScoringSnapshot internally and hands it
    // to applyHarmonicFunction() (the competition pipeline). There is no external
    // capture opt-in and no progression-signal suppression flag: the oracle never
    // computes a progression signal, so there is nothing to suppress. See
    // docs/scoring_model.md section 11.

    // ── Style prior (future — not yet implemented) ───────────────────────────
    // TODO: expose as a user preference.  Affects chord-frequency priors and
    // which extensions are considered idiomatic.
    // enum class StylePrior { General, Classical, Jazz, Pop, Blues, Folk };
    // StylePrior stylePrior = StylePrior::General;

    /// Returns the valid range for every numeric scoring parameter.
    ///
    /// isManual=false parameters are safe to hand to automated optimizers
    /// (grid search, gradient descent, Bayesian optimization).
    /// isManual=true parameters are wired to user-visible preferences or have
    /// a narrow hand-tuned sweet-spot and should not be auto-adjusted.
    ///
    /// The boolean toggle fields (useExistingChordSymbols, etc.) are omitted;
    /// they are not continuous-valued and are not optimization targets.
    ParameterBoundsMap bounds() const
    {
        return {
            { "bassNoteRootBonus",           { 0.0, 2.0 } },
            { "bassRootThirdOnlyMultiplier", { 0.0, 1.0 } },
            { "bassRootAloneMultiplier",     { 0.0, 1.0 } },
            { "diatonicRootBonus",           { 0.0, 1.0 } },
            { "tpcConsistencyBonusPerTone",  { 0.0, 1.0 } },
            { "rootContinuityBonus",           { 0.0, 1.5 } },
            { "resolutionBonus",               { 0.0, 1.5 } },
            { "stepwiseBassInversionBonus",    { 0.0, 2.0 } },
            { "stepwiseBassLookaheadBonus",    { 0.0, 2.0 } },
            { "completeTriadInversionBonus",  { 0.0, 2.0 } },
            { "sameRootInversionBonus",                    { 0.0, 2.0 } },
            { "maxTotalInversionContextBonus",            { 0.0, 10.0 } },
            { "inversionSuspicionMargin",                 { 0.0, 2.0 } },
            { "inversionBonusReduction",            { 0.0, 1.0 } },
            { "harmonicBoundaryJaccardThreshold",       { 0.0, 1.0 } },
            { "pedalTailWeightMultiplier",              { 0.0, 1.0 } },
            { "bassPassingToneMinWeightFraction",       { 0.0, 0.5 } },
            { "pedalConfidenceThreshold",               { 0.3, 0.95 } },
            { "extensionThreshold",                     { 0.10, 0.30 } },
        };
    }
};

/// Global default preferences.  The analyzer uses this when no explicit
/// preferences are supplied by the caller.
inline constexpr ChordAnalyzerPreferences kDefaultChordAnalyzerPreferences{};

/// Optional temporal context passed between successive chord analyses.
/// Enables root-continuity scoring, resolution biasing, and contextual
/// inversion resolution (§4.1b).
///
/// Fields marked "populated" are set by the bridge on every call.
/// Fields marked "deferred" are always at their default values until
/// two-pass chord-staff analysis is implemented (§4.1b).
///
/// Naming note: ChordTemporalContext carries single-step look-around
/// data for vertical chord analysis.  A future TemporalContext struct
/// (planned for analysis/temporal/) will accumulate full progression
/// context (chord history, cadence state) for a ProgressionAnalyzer.
/// These are distinct structs with distinct roles.
struct ChordTemporalContext {
    /// Root pitch class of the most recently identified chord (-1 = none).
    int previousRootPc = -1;

    /// Quality of the most recently identified chord.
    ChordQuality previousQuality = ChordQuality::Unknown;

    /// Bass pitch class of the most recently identified chord.
    /// Used to detect stepwise bass motion indicating inversion.
    /// -1 if unknown.
    int previousBassPc = -1;

    /// True if the current region's bass note is one diatonic step
    /// above or below the previous region's bass note.
    /// Stepwise bass motion is a strong signal that the current
    /// chord is an inversion within a linear bass line.
    /// Computed by the bridge before passing to the analyzer.
    bool bassIsStepwiseFromPrevious = false;

    /// True if the current region's bass note is one diatonic step
    /// above or below the next region's bass note.
    bool bassIsStepwiseToNext = false;

    /// Bass pitch class of the next harmonic region (-1 if unknown).
    /// Iter 92: separated from bassIsStepwiseToNext so the joint scoring pass
    /// can compute step-out plausibility against any candidate bass, not just
    /// the bass that was committed before the analyzer ran.
    int nextBassPc = -1;

    /// Inferred root pitch class of the next harmonic region; -1 if unknown.
    /// Populated by batch_analyze via a one-region look-ahead analyzeChord call.
    int nextRootPc = -1;

    /// Number of consecutive regions (including this one) whose bass moved by
    /// diatonic step from the preceding region's bass.  0 if this region's bass
    /// is not stepwise from the previous one.  Scalar bass lines are strong
    /// evidence that non-root-bass readings are passing inversions.
    int consecutiveBassStepwiseCount = 0;

    /// Root pitch classes of the 3 most recent regions, most-recent first.
    /// -1 for slots that are not yet populated (start of piece).
    /// Used to detect harmony persistence across a short window.
    std::array<int, 3> recentRootPcs = {-1, -1, -1};

    /// Normalised metric strength of this region's onset: 1.0 = strong downbeat,
    /// lower values for weaker beats, 0.5 for subbeatoffbeats.
    /// Root-position chords cluster on strong beats; inversions on weak beats.
    double regionMetricWeight = 1.0;

    // Step 2 redesign: predecessor confidence channel — forwarded to HarmonicFunctionContext
    // All values are pre-gate (from applyHarmonicFunction competition pipeline output).

    /// Score of the preceding region's committed winner (post-competition-pipeline).
    /// 0.0 if not available (piece start, sub-region without gateCtx).
    double previousWinnerScore { 0.0 };

    /// Score gap between winner and runner-up in the winning bass group.
    /// -1.0 if only one candidate existed (no runner-up).
    double previousWinnerMargin { -1.0 };

    /// pcWeight of the preceding region's committed winner's root pitch class.
    /// 0.0 means the root was entirely absent from the sounded tones.
    double previousWinnerRootPcWeight { 0.0 };

    /// Distinct pitch-class count in the preceding region.
    /// 0 if not available.
    int previousDistinctPcs { 0 };
};

/// Per-candidate diagnostic entry from the full 12 × template scoring loop.
/// Component scores sum (approximately) to totalScore.
struct ChordCandidateDiagnostic {
    int rootPc = 0;
    int templateIdx = 0;                   ///< 0-based index into the 16-template array
    ChordQuality quality = ChordQuality::Unknown;
    double totalScore = 0.0;
    // ── Additive scoring components ────────────────────────────────────────
    double templateTonesScore = 0.0; ///< scoreTemplateTones() — template tone hits
    double extraNotesScore    = 0.0; ///< scoreExtraNotes()    — extensions (+) / contradictions (−)
    double dim7Bonus          = 0.0; ///< dim7CharacteristicBonus()
    double nonBassAdjust      = 0.0; ///< nonBassAdjustment() — ≤ 0 for non-bass Min7/HalfDim/Sus4
    double structuralPenalty  = 0.0; ///< structuralPenalties() — ≤ 0
    double tpcBonus           = 0.0; ///< tpcConsistencyBonus()
    double bassBonus          = 0.0; ///< appliedBassRootBonus() (0 when root ≠ bass)
    double diatonicBonus      = 0.0; ///< diatonicRootBonus (0 when root is non-diatonic)
    double contextBonus       = 0.0; ///< continuity + resolution + inversion bonuses
};

/// Full diagnostic output from a single chord analysis run.
struct ChordAnalysisDiagnosticResult {
    int bassPc = -1;                        ///< Bass PC chosen by the analyzer
    std::array<double, 12> pcWeights{};    ///< Per-PC accumulated weights (pre-normalization)
    int distinctPcs = 0;                    ///< Distinct PCs with weight > 0.05
    /// All 12 × 16 = 192 candidates, sorted descending by totalScore.
    std::vector<ChordCandidateDiagnostic> candidates;
};

/// Interface for chord analysis strategies.
///
/// Callers that need dependency injection (tests, bridge) should hold a
/// const reference or pointer to IChordAnalyzer rather than a concrete type.
class IChordAnalyzer
{
public:
    virtual ~IChordAnalyzer() = default;

    /// Analyse a vertical sonority from sounding notes under a key context.
    ///
    /// keySignatureFifths: -7..+7, same convention as KeyModeAnalyzer.
    /// keyMode: detected mode — determines the tonic and diatonic scale used
    ///          for degree assignment and diatonic scoring.
    /// context: optional temporal context for root-continuity scoring.
    ///
    /// Returns up to 3 candidates sorted by score descending. An empty result
    /// means fewer than 3 distinct pitch classes are sounding (insufficient data).
    virtual std::vector<ChordAnalysisResult> analyzeChord(
        const std::vector<ChordAnalysisTone>& tones,
        int keySignatureFifths,
        KeySigMode keyMode,
        const ChordTemporalContext* context = nullptr,
        const ChordAnalyzerPreferences& prefs = kDefaultChordAnalyzerPreferences,
        PostScoringGateContext* gateCtxOut = nullptr) const = 0;
};

/// Forward declaration — `inferNextRootPc` is defined further down the header,
/// after `PostScoringGateContext` and `applyPostScoringGates()` are fully
/// declared (its body references both). Declared here so callers that include
/// chordanalyzer.h before the body can still see the symbol.
inline int inferNextRootPc(
    const IChordAnalyzer* analyzer,
    const std::vector<ChordAnalysisTone>& tones,
    int keySignatureFifths,
    KeySigMode keyMode,
    const ChordAnalyzerPreferences& prefs = kDefaultChordAnalyzerPreferences);

/// Advances the temporal context and rolling state after a region has been analyzed.
/// Call once per region, after analyzeChord() has been called and the final result
/// chosen. Updates: rolling stepwise count, recent-roots window, and previous-chord
/// fields. After returning, ctx is ready for the next region's analyzeChord() call
/// (except for bassIsStepwiseFromPrevious / bassIsStepwiseToNext / nextRootPc which
/// depend on the next region's tones and must be set separately).
///
/// A third overload taking a PostScoringGateContext& is declared further down
/// (after PostScoringGateContext is fully defined); it does everything the
/// ChordIdentity overload does AND populates the predecessor-confidence fields
/// (previousWinnerScore / previousWinnerMargin / previousWinnerRootPcWeight /
/// previousDistinctPcs). It is the canonical commit helper used at every
/// chord-commit site in regionanalyzer.cpp.
inline void advanceTemporalContext(
    ChordTemporalContext& ctx,
    int& runningStepwiseCount,
    std::array<int, 3>& recentRootsBuf,
    int chosenRootPc,
    int chosenBassPc,
    ChordQuality chosenQuality) noexcept
{
    // Rolling stepwise count.
    if (ctx.bassIsStepwiseFromPrevious) {
        ++runningStepwiseCount;
    } else {
        runningStepwiseCount = 0;
    }

    // Recent-roots window (most-recent first).
    recentRootsBuf[2] = recentRootsBuf[1];
    recentRootsBuf[1] = recentRootsBuf[0];
    recentRootsBuf[0] = chosenRootPc;

    // Pre-populate rolling fields for the next call to analyzeChord.
    ctx.consecutiveBassStepwiseCount = runningStepwiseCount;
    ctx.recentRootPcs                = recentRootsBuf;

    // Advance previous-chord fields.
    ctx.previousRootPc  = chosenRootPc;
    ctx.previousBassPc  = chosenBassPc;
    ctx.previousQuality = chosenQuality;
}

inline void advanceTemporalContext(
    ChordTemporalContext& ctx,
    int& runningStepwiseCount,
    std::array<int, 3>& recentRootsBuf,
    const ChordIdentity& chosen) noexcept
{
    advanceTemporalContext(ctx, runningStepwiseCount, recentRootsBuf,
                           chosen.rootPc, chosen.bassPc, chosen.quality);
}

/// Locally-computed inputs that applyPostScoringGates() needs from
/// analyzeChord(). Populated when analyzeChord() is called with a
/// non-null pointer to this struct.
struct PostScoringGateContext {
    std::array<double, 12>    pcWeight       {};
    std::array<int, 12>       tpcForPc       {};
    std::array<int, 7>        scale          {};
    int                       keyTonicPc     { -1 };
    KeySigMode                keyMode        {};
    int                       bassPc         { -1 };
    int                       bassTpc        { -1 };
    int                       distinctPcs    { 0 };
    double                    threshold      { 0.0 };
    std::vector<RawCandidate> rawCandidates  {};

    // Extracted Iter 86/91/pedal tail (Phase 1, E2d-prereq) — captured so
    // applyIter8691Pedal() can run after applyHarmonicFunction() at the
    // production call sites.
    std::vector<ChordAnalysisTone> tones        {};   ///< Region tones (pedal Pass-2 re-analysis).
    int                            keySigFifths { 0 }; ///< keySignatureFifths (pedal Pass-2 re-analysis).
};

/// Canonical chord-commit helper. Delegates to the ChordIdentity overload above
/// (rolling stepwise count, recent-roots window, previous-chord fields) and then
/// populates the Step-2 predecessor-confidence fields from the captured
/// PostScoringGateContext. Used at every commit site in regionanalyzer.cpp so the
/// main loop, Pass 2 sub-regions and Pass 2b sub-regions all advance identically.
/// Declared here (not next to the other overloads) because its body references
/// PostScoringGateContext, which is only fully defined immediately above.
inline void advanceTemporalContext(
    ChordTemporalContext&         ctx,
    int&                          runningStepwiseCount,
    std::array<int, 3>&           recentRootsBuf,
    const ChordIdentity&          chosen,
    const PostScoringGateContext& gateCtx) noexcept
{
    // Delegate to the existing overload for rolling state + identity fields.
    advanceTemporalContext(ctx, runningStepwiseCount, recentRootsBuf, chosen);

    // Predecessor confidence fields (Step 2 redesign).
    const int winRoot = chosen.rootPc;
    ctx.previousWinnerRootPcWeight = (winRoot >= 0)
        ? gateCtx.pcWeight[static_cast<size_t>(winRoot)] : 0.0;
    ctx.previousDistinctPcs  = gateCtx.distinctPcs;
    ctx.previousWinnerScore  = gateCtx.rawCandidates.empty()
        ? 0.0 : gateCtx.rawCandidates[0].score;
    ctx.previousWinnerMargin = (gateCtx.rawCandidates.size() >= 2)
        ? gateCtx.rawCandidates[0].score - gateCtx.rawCandidates[1].score
        : -1.0;
}

/// Locally-computed inputs that buildChordResult() needs from analyzeChord().
struct BuildChordResultContext {
    const std::array<double, 12>& pcWeight;
    const std::array<int, 12>&    tpcForPc;
    int                           bassPc;
    int                           bassTpc;
    int                           keyTonicPc;
    KeySigMode                    keyMode;
    const std::array<int, 7>&     scale;
};

/// Construct a fully-normalised ChordAnalysisResult from a raw scored cell.
/// Applies augmented-root correction, Sus→Major(omitsThird), extension
/// detection, degree labelling and diatonic check.
/// Called from analyzeChord() (main result-building loop) and from
/// applyPostScoringGates() (A-FM2 and G-E fallback cell promotion).
ChordAnalysisResult buildChordResult(
    const RawCandidate&             rc,
    const BuildChordResultContext&  ctx,
    const ChordAnalyzerPreferences& prefs);

/// Apply post-scoring identity gates (A–L) to a result list.
/// Must be called after applyHarmonicFunction() and before refinements.
/// When callers need pre-gate inputs (rawCandidates, threshold, distinctPcs,
/// pcWeight, …) they obtain them by passing a non-null PostScoringGateContext*
/// to analyzeChord(); this function then operates on those captured values.
///
/// Mutates results[] in place (may swap, push, or reorder entries).
/// Caller should reassign chosenResult = results.front() afterwards.
void applyPostScoringGates(
    std::vector<ChordAnalysisResult>& results,
    const ChordAnalyzerPreferences&   prefs,
    const ChordTemporalContext*       context,
    const PostScoringGateContext&     gateCtx);

/// Apply the Iter 86 (bass-b7 promotion), Iter 91 (bass-as-root promotion) and
/// two-pass pedal-point passes that previously ran at the tail of analyzeChord().
/// Extracted (Phase 1, E2d-prereq) so they run AFTER applyHarmonicFunction() —
/// in suppression mode they must stamp the function-layer-selected winner, not the
/// suppressed-signal winner. In non-suppression mode applyHarmonicFunction() is a
/// no-op, so this is byte-identical to the old inline tail. Must be called between
/// applyHarmonicFunction() and applyPostScoringGates() at every production site.
void applyIter8691Pedal(
    std::vector<ChordAnalysisResult>& results,
    const PostScoringGateContext&     gateCtx,
    const ChordTemporalContext*       context,
    const ChordAnalyzerPreferences&   prefs);

/// Lightweight root-PC inference for a neighbouring region.
/// Calls analyzeChord with nullptr context (no temporal signals) to avoid recursion.
/// Returns -1 if tones is empty or analyzeChord returns no candidates.
/// Defined inline here so it can be called from headers; uses
/// PostScoringGateContext and applyPostScoringGates which are now declared above.
inline int inferNextRootPc(
    const IChordAnalyzer* analyzer,
    const std::vector<ChordAnalysisTone>& tones,
    int keySignatureFifths,
    KeySigMode keyMode,
    const ChordAnalyzerPreferences& prefs)
{
    if (tones.empty()) return -1;
    PostScoringGateContext igCtx;
    auto candidates = analyzer->analyzeChord(
        tones, keySignatureFifths, keyMode, nullptr, prefs, &igCtx);
    if (candidates.empty()) return -1;
    applyIter8691Pedal(candidates, igCtx, nullptr, prefs);
    applyPostScoringGates(candidates, prefs, nullptr, igCtx);
    return candidates.empty() ? -1 : candidates[0].identity.rootPc;
}

/// Default chord analyzer: template-matching rule-based approach.
class RuleBasedChordAnalyzer : public IChordAnalyzer
{
public:
    std::vector<ChordAnalysisResult> analyzeChord(
        const std::vector<ChordAnalysisTone>& tones,
        int keySignatureFifths,
        KeySigMode keyMode,
        const ChordTemporalContext* context = nullptr,
        const ChordAnalyzerPreferences& prefs = kDefaultChordAnalyzerPreferences,
        PostScoringGateContext* gateCtxOut = nullptr) const override;

    /// Run the full 12 × template scoring loop and return per-candidate breakdowns.
    /// Unlike analyzeChord(), post-scoring quality normalization is not applied, so
    /// quality reflects the raw template that produced the score.
    ChordAnalysisDiagnosticResult diagnoseChord(
        const std::vector<ChordAnalysisTone>& tones,
        int keySignatureFifths,
        KeySigMode keyMode,
        const ChordTemporalContext* context = nullptr,
        const ChordAnalyzerPreferences& prefs = kDefaultChordAnalyzerPreferences) const;
};

/// Analyzer implementation variants.
enum class ChordAnalyzerType {
    RuleBased,  ///< Template-matching rule-based analyzer (the only implemented type).
};

/// Factory for IChordAnalyzer instances.
///
/// Bridge files should obtain analyzers via this factory so callers depend only
/// on IChordAnalyzer.  Test code can bypass the factory and inject a mock directly.
class ChordAnalyzerFactory
{
public:
    static std::unique_ptr<IChordAnalyzer> create(
        ChordAnalyzerType type = ChordAnalyzerType::RuleBased);
};

/// Formatting utilities to generate display strings from analysis results.
/// Kept separate from ChordAnalyzer so the analysis layer remains display-agnostic.
namespace ChordSymbolFormatter {

/// Note spelling convention for chord symbol root and bass names.
/// Mirrors NoteSpellingType in src/engraving/types/types.h.
/// The bridge reads Sid::chordSymbolSpelling from the score style and maps it here.
/// German mapping mirrors tpc2name() GERMAN case (pitchspelling.cpp:343-356):
///   B natural → "H", Bb → "B". All other note names unchanged.
/// Solfeggio and French map to Standard (not yet supported in chord symbol output).
enum class NoteSpelling {
    Standard,    ///< English: B natural = "B", Bb = "Bb"
    German,      ///< H = B natural, B = Bb  (mirrors NoteSpellingType::GERMAN)
    GermanPure,  ///< Same B/H rules as German for chord symbols  (mirrors NoteSpellingType::GERMAN_PURE)
};

/// Display options for chord symbol and Roman numeral formatting.
/// Kept separate from ChordAnalyzerPreferences so the abstract analysis layer
/// has no knowledge of display conventions (locale, notation style, etc.).
struct Options {
    /// Note spelling convention for root/bass names.
    NoteSpelling spelling = NoteSpelling::Standard;
};

/// Global default formatting options.
inline constexpr Options kDefaultOptions{};

/// Format root, quality, and bass into a chord symbol (e.g. "C7/E", "Fm").
/// Uses flat names for negative keySignatureFifths, sharp names otherwise.
std::string formatSymbol(const ChordAnalysisResult& result, int keySignatureFifths,
                         const Options& opts = kDefaultOptions);

/// Format diatonic degree and quality into roman numeral notation (e.g. "V7", "iiø7").
/// Returns an empty string when result.function.degree < 0 (non-diatonic chord).
std::string formatRomanNumeral(const ChordAnalysisResult& result);


// Nashville Number System formatter and helpers
std::string formatNashvilleNumber(const ChordAnalysisResult& result, int keySignatureFifths);

} // namespace ChordSymbolFormatter

/// Voicing output for chord track population.  Bass note is placed separately
/// from upper-structure tones so the caller can write them to different staves.
struct ClosePositionVoicing {
    int bassPitch = -1;                  ///< Root MIDI pitch in C2–C3 range (-1 = empty)
    std::vector<int> treblePitches;      ///< Upper chord tones in C4–C5 close position
};

/// Compute a close-position keyboard reduction voicing from an analysis result.
///
/// Bass: root placed in C2–C3 (MIDI 36–48), nearest to midpoint (42).
/// Treble: remaining chord tones stacked ascending above C4 (MIDI 60),
/// each note ascending from the previous, staying within one octave.
///
/// Returns empty voicing (bassPitch == -1) if analysis has Unknown quality.
ClosePositionVoicing closePositionVoicing(const ChordAnalysisResult& result);

/// Derive the canonical set of pitch classes for a chord from its analysis result.
///
/// Returns pitch classes (0–11) ordered: root first, then remaining chord tones
/// ascending from the root.  The result reflects the chord's quality and all
/// detected extensions — it is not a transcription of what was sounding, but the
/// idealized chord content suitable for a keyboard reduction.
///
/// If omitsThird is true in the result, the third is excluded.
/// Altered fifths (b5, #5) replace the natural fifth when flagged.
std::vector<int> chordTonePitchClasses(const ChordAnalysisResult& result);

} // namespace mu::composing::analysis
