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
#include "../types/analysistypes.h"

// Forward declaration — avoids a circular include with harmonicfunctionlayer.h
// (which itself includes this header). Full definition of ScoringSnapshot is in
// harmonicfunctionlayer.h. (function::ScoringPhase, formerly defined here, now
// lives in the leaf types header analysis/types/analysistypes.h, included above —
// a pure relocation, name and namespace unchanged. See cowork_types_header_design.md.)
namespace mu::composing::function {
struct ScoringSnapshot;
} // namespace mu::composing::function

namespace mu::composing::analysis {

/// Number of chord templates the scorer ranks against. SINGLE SOURCE OF TRUTH for every
/// template-sized array, eliminating the silent stack-overrun class (B1, 2026-06-04):
///   - the `templates` TemplateDef array in chordanalyzer.cpp (the former byte-identical
///     `kDiagTemplates` mirror was removed in Stage 2.3 — `diagnoseChord` now replays the
///     production pipeline instead of re-scoring against a second array),
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

/// Maximum number of chord tones in any single template (the 7th chords — Maj7/Dom7/… —
/// have 4; triads have 3; Power has 2).
inline constexpr std::size_t kMaxTemplateTones = 4;

/// Canonical chord-template interval sets — semitones above the root. THE SINGLE SOURCE of
/// the per-template interval data, shared by:
///   - the chord scorer's `templates` TemplateDef array (chordanalyzer.cpp), and
///   - Gate R's interval-membership masks (harmonicfunctionlayer.cpp), which are now
///     DERIVED from this table via templateIntervalMask() rather than hand-typed.
/// Deriving the masks closes the audit-Q1.3 hazard: a hand-typed mask could silently drift
/// from the templates (a wrong/zero mask disables Gate R for that template with no compile
/// error). Row order is load-bearing — index == template index == tiePriority, matching
/// `templates` and kTemplateCount. Trailing -1 = unused slot (triads/Power have fewer than
/// kMaxTemplateTones tones). Every template includes interval 0 (the root).
inline constexpr std::array<std::array<int, kMaxTemplateTones>, kTemplateCount>
kTemplateIntervals = { {
    { { 0, 4, 7, -1 } },   // 0  Major triad   {0,4,7}
    { { 0, 4, 7, 11 } },   // 1  Maj7          {0,4,7,11}
    { { 0, 4, 7, 10 } },   // 2  Dom7          {0,4,7,10}
    { { 0, 4, 6, 10 } },   // 3  Dom7b5        {0,4,6,10}
    { { 0, 3, 7, -1 } },   // 4  Minor triad   {0,3,7}
    { { 0, 3, 7, 10 } },   // 5  Minor 7th     {0,3,7,10}
    { { 0, 3, 6, -1 } },   // 6  Diminished    {0,3,6}
    { { 0, 5, 6, 10 } },   // 7  Sus4b5        {0,5,6,10}
    { { 0, 3, 6, 10 } },   // 8  HalfDim       {0,3,6,10}
    { { 0, 4, 8, -1 } },   // 9  Augmented     {0,4,8}
    { { 0, 4, 8, 10 } },   // 10 Aug dom7      {0,4,8,10}
    { { 0, 2, 7, -1 } },   // 11 Sus2          {0,2,7}
    { { 0, 5, 7, 10 } },   // 12 Sus4+m7       {0,5,7,10}
    { { 0, 5, 7, 11 } },   // 13 Sus4+Maj7     {0,5,7,11}
    { { 0, 5, 8, 10 } },   // 14 Sus4#5        {0,5,8,10}
    { { 0, 6, 7, -1 } },   // 15 Sus#4         {0,6,7}
    { { 0, 7, -1, -1 } },  // 16 Power         {0,7}
} };

/// Gate R interval-membership bitmask for template `t`: bit i set ⇔ semitone interval i
/// (from the root) is one of the template's tones. Derived purely from kTemplateIntervals,
/// so the function layer's mask table cannot drift from the scorer's templates.
constexpr std::uint16_t templateIntervalMask(std::size_t t)
{
    std::uint16_t mask = 0;
    for (int interval : kTemplateIntervals[t]) {
        if (interval >= 0) {
            mask |= static_cast<std::uint16_t>(1u << interval);
        }
    }
    return mask;
}

/// The full derived Gate R mask table — one entry per template. Replaces the former
/// hand-typed kMasks literal array in harmonicfunctionlayer.cpp (now `= makeTemplateMasks()`).
constexpr std::array<std::uint16_t, kTemplateCount> makeTemplateMasks()
{
    std::array<std::uint16_t, kTemplateCount> masks{};
    for (std::size_t t = 0; t < kTemplateCount; ++t) {
        masks[t] = templateIntervalMask(t);
    }
    return masks;
}

// ChordQuality and ChordAnalysisTone now live in the leaf types header
// analysis/types/analysistypes.h (included above) — a pure relocation, names and
// namespace unchanged. The free helpers below still operate on them. See
// cowork_types_header_design.md.

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

// ChordAnalyzerPreferences (+ kDefaultChordAnalyzerPreferences), DecodeQualityLevel,
// and ChordTemporalContext now live in the leaf types header
// analysis/types/analysistypes.h (included above) — a pure relocation, names and
// namespace unchanged. See cowork_types_header_design.md.

// ── diagnoseChord() introspection result (Stage 2.3) ──────────────────────────
//
// diagnoseChord() REPLAYS the production pipeline (analyzeChord + applyIter8691Pedal
// + applyPostScoringGates) and decorates its intermediate state. The result is split
// into three clearly-labeled layers plus the production winner:
//   ORACLE      — the vertical-only per-cell scores the scoring oracle produced,
//                 copied straight from the fn::ScoringSnapshot (no progression signal).
//   COMPETITION — the winning bass group's candidates with their progression-signal
//                 components (rcb incl. Gate R outcome, w_seq, w_dim, step bonuses);
//                 the SCORES are taken verbatim from the real pipeline
//                 (PostScoringGateContext::rawCandidates), the component values are
//                 recomputed from the snapshot cell + context via the SAME public
//                 fn:: bonus functions applyHarmonicFunction() calls.
//   POST-GATES  — which stage (Iter 86/91/pedal, gates A–L) moved the winner.
// finalWinner is the production winner BY CONSTRUCTION (== analyzeWithGates().front()).

/// ORACLE layer: one snapshot cell — the vertical-only scoring terms for a
/// (bass, root, template) candidate. Mirrors fn::ScoringCell.
struct DiagnosticOracleCell {
    int          bassPc           = -1;
    int          rootPc           = 0;
    int          templateIdx      = 0;   ///< tiePriority (index into the template array)
    ChordQuality quality          = ChordQuality::Unknown;
    double       basisIndep       = 0.0; ///< vertical pitch evidence (no progression signal; Stage 3.3)
    double       basisDep         = 0.0; ///< bass-dependent delta: nonBassAdjustment + appliedBassBonus
                                          ///< (inversion bonuses migrated to the pipeline, Stage 3.3)
    double       complexityFactor = 0.0;
    double       augFactor        = 0.0;
    double       wCompleteBonus   = 0.0;
    double       appliedBassBonus = 0.0;
    /// Vertical-only score handed to the competition pipeline, BEFORE any progression
    /// signal: (basisIndep + basisDep) * complexityFactor * augFactor + wCompleteBonus.
    double       verticalScore    = 0.0;
};

/// COMPETITION layer: one candidate of the WINNING bass group. The competitionScore is
/// authoritative (from the pipeline's rawCandidates); the component fields are a faithful
/// view of the progression signals the pipeline applied to this cell.
struct DiagnosticCompetitionCandidate {
    int          bassPc       = -1;
    int          rootPc       = 0;
    int          templateIdx  = 0;
    ChordQuality quality      = ChordQuality::Unknown;
    /// rootContinuityBonus actually in effect (0 when withheld by Gate R or no continuity).
    double       rootContinuityBonus           = 0.0;
    /// Pre-Gate-R rootContinuityBonus — the value Gate R may have withheld.
    double       rootContinuityBonusRaw        = 0.0;
    bool         rootContinuityWithheldByGateR = false;
    /// Migrated oracle temporal signals (Stage 3.3), folded into basisIndep / basisDep
    /// before the cf × af multiply. resolutionBonus = the back-edge resolution bias;
    /// inversionContextBonus = the capped sum of the four §4.1b inversion bonuses (also the
    /// "inversion credit" Gate R's reconstructed fullBasisDep reads).
    double       resolutionBonus      = 0.0;
    double       inversionContextBonus = 0.0;
    double       wSeqBonus     = 0.0;
    double       wDimBonus     = 0.0;   ///< exact value the pipeline applied (RawCandidate::wDimDelta)
    double       stepInBonus   = 0.0;   ///< potential w_stepIn (the surgical guard may suppress it)
    double       stepOutBonus  = 0.0;   ///< potential w_stepOut (the surgical guard may suppress it)
    /// Final competition score for this candidate — authoritative, from the pipeline.
    double       competitionScore = 0.0;
};

/// POST-GATES layer: the winner identity + score after each production stage, so the
/// dump shows which stage (if any) changed the winner.
struct DiagnosticPostGateTrail {
    bool         hasCompetitionWinner    = false;
    int          competitionWinnerRootPc  = -1;
    int          competitionWinnerBassPc  = -1;
    ChordQuality competitionWinnerQuality = ChordQuality::Unknown;
    double       competitionWinnerScore   = 0.0;
    bool         iter8691ChangedWinner    = false;  ///< applyIter8691Pedal moved results.front()
    bool         gatesChangedWinner       = false;  ///< applyPostScoringGates moved results.front()
};

/// Full diagnostic output — a VIEW into the production pipeline's intermediate state
/// (Stage 2.3), not a separate scorer.
struct ChordAnalysisDiagnosticResult {
    int                    bassPc      = -1;       ///< winner bass PC (production); -1 if no winner
    std::array<double, 12> pcWeights{};            ///< per-PC accumulated weights (from the snapshot)
    int                    distinctPcs = 0;        ///< distinct PCs with weight > 0.05
    int                    keyTonicPc  = -1;
    KeySigMode             keyMode{};

    std::vector<DiagnosticOracleCell>           oracleCells;  ///< ORACLE (all cells, score-sorted)
    std::vector<DiagnosticCompetitionCandidate> competition;  ///< COMPETITION (winning bass group)
    DiagnosticPostGateTrail                     postGates;     ///< POST-GATES trail
    ChordAnalysisResult                         finalWinner;   ///< production winner by construction
    bool                                        hasWinner = false;
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
    ///
    /// snapshotOut: when non-null, the internally-built fn::ScoringSnapshot (the
    /// vertical-only candidate cube the competition pipeline consumed) is copied out
    /// after applyHarmonicFunction() ran. Mirrors the gateCtxOut pattern: byte-identical
    /// behavior when null, a single branch + one copy when set. Used by diagnoseChord()
    /// to introspect the production pipeline without re-scoring.
    virtual std::vector<ChordAnalysisResult> analyzeChord(
        const std::vector<ChordAnalysisTone>& tones,
        int keySignatureFifths,
        KeySigMode keyMode,
        const ChordTemporalContext* context = nullptr,
        const ChordAnalyzerPreferences& prefs = kDefaultChordAnalyzerPreferences,
        PostScoringGateContext* gateCtxOut = nullptr,
        function::ScoringSnapshot* snapshotOut = nullptr) const = 0;
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

/// ── Read-only Layer-5 fan-out summary (Engage arc #8 measurement) ───────────
/// The TRUE untruncated above-threshold ranked-set size Layer 5 will select over,
/// BEFORE applyHarmonicFunction()'s cap-of-3 (harmonicfunctionlayer.cpp:521) and its
/// diff-root append. A pure read-only VIEW of the pipeline's own gateCtx: `total` is
/// the full winning-bass fan-out (gateCtx.rawCandidates.size(), uncapped);
/// `aboveThreshold` counts the leading candidates whose score clears gateCtx.threshold
/// (the results[] admission test, harmonicfunctionlayer.cpp:524) — the real ranked set
/// the cap truncates. distinctRoots* count genuinely-different-ROOT readings (the
/// decoder already dedups voicings, so each rawCandidate is one reading; the reading
/// count IS the distinct-voicing count). Computed by computeRawFanoutSummary(); carried
/// in-memory only and NEVER serialized into any production output (.ours.json, snapshot
/// goldens, notation annotations) — it exists solely for the read-only fan-out dump.
struct RawFanoutSummary {
    int total              = 0;  ///< all rawCandidates (uncapped winning-bass fan-out)
    int aboveThreshold     = 0;  ///< rawCandidates with score >= gateCtx.threshold (pre-cap ranked set)
    int distinctRootsTotal = 0;  ///< distinct rootPc across all rawCandidates
    int distinctRootsAbove = 0;  ///< distinct rootPc across the above-threshold set
};

/// Read-only view: derive the fan-out summary from the pipeline's own gateCtx (its
/// rawCandidates + threshold). rawCandidates is score-sorted descending, so the
/// above-threshold set is a prefix; counting every entry is equivalent and order-free.
/// No scoring, no re-decision — a faithful count of the reading set applyHarmonicFunction
/// already produced.
inline RawFanoutSummary computeRawFanoutSummary(const PostScoringGateContext& gateCtx) noexcept
{
    RawFanoutSummary s;
    s.total = static_cast<int>(gateCtx.rawCandidates.size());
    std::array<bool, 12> rootSeenAll{};
    std::array<bool, 12> rootSeenAbove{};
    for (const RawCandidate& rc : gateCtx.rawCandidates) {
        const bool above = rc.score >= gateCtx.threshold;
        if (above) { ++s.aboveThreshold; }
        if (rc.rootPc >= 0 && rc.rootPc < 12) {
            const auto r = static_cast<size_t>(rc.rootPc);
            if (!rootSeenAll[r])          { rootSeenAll[r]   = true; ++s.distinctRootsTotal; }
            if (above && !rootSeenAbove[r]) { rootSeenAbove[r] = true; ++s.distinctRootsAbove; }
        }
    }
    return s;
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
    /// The NOTATED key signature the region was analyzed under. Carried so the diatonic check
    /// can ask its collection-membership question of the signature's own collection rather than
    /// of the mode-tonic-anchored set (OI-170). Read only by the default-OFF signature-mask
    /// variant today; the committed path still uses keyTonicPc + scale.
    int                           keySignatureFifths;
};

/// Construct a fully-normalised ChordAnalysisResult from a raw scored cell.
/// Applies augmented-root correction, Sus→Major(omitsThird), extension
/// detection, degree labelling and diatonic check.
/// The single builder for the whole module: called from applyHarmonicFunction()'s
/// score-ordered build loop, and — via buildResultFromGateCtx() — from the unified
/// promoteToWinner() primitive for every post-scoring cell promotion.
ChordAnalysisResult buildChordResult(
    const RawCandidate&             rc,
    const BuildChordResultContext&  ctx,
    const ChordAnalyzerPreferences& prefs);

// ── Unified post-scoring promotion primitive (Layer 4) ────────────────────────────
//
// A single "promote a reading to the winner" primitive shared by every post-scoring
// promotion site — the enharmonic Major-add6 ↔ Minor7 flip (formerly the split Gate A +
// FM2), Gate E, the Minor-add6 ↔ HalfDim7 G-block (Gate G-E / G-D), and the Iter-91
// bass-root pull — replacing the ad-hoc swap-vs-append idioms and the three duplicated
// builder lambdas. One path per concern (⛔ total unification). See docs/scoring_model.md §6
// and cowork_gateA_unification_design.md.
//
//   Idiom A (present-first): a target reading already carried in results[] is swapped to the
//   front (reuse-in-place — no growth, no duplicate).
//   Idiom B (append-built):  otherwise the target is built ONCE (the single builder path)
//   from gateCtx.rawCandidates, appended, and swapped to the front.

/// The (rootPc, quality) reading a promotion wants as the winner. quality == Unknown matches
/// any quality (the Iter-91 bass-root pull, which does not constrain quality).
struct PromotionTarget {
    int          rootPc  = -1;
    ChordQuality quality = ChordQuality::Unknown;
};

/// promoteToWinner()'s @p presentHint sentinels. Any other value is a concrete results[]
/// index the caller already computed (the primitive swaps it iff it still matches @p target —
/// this is how the enharmonic flip / Gate E reproduce their exact bestAltIdx swap):
inline constexpr std::size_t kPromotePresentScan = static_cast<std::size_t>(-1); ///< scan results[1..] for the first match
inline constexpr std::size_t kPromoteAppendOnly  = static_cast<std::size_t>(-2); ///< skip the present branch (bass-root pull; no dedup)

/// Promote @p target to results[0], unifying the swap-existing and append-built idioms.
/// @p presentHint selects the present branch: a concrete index (swap iff it matches), or
/// kPromotePresentScan (first-match scan of results[1..]), or kPromoteAppendOnly (skip the
/// present branch). When the present branch does not fire and @p target is found in
/// gateCtx.rawCandidates, it is built once via the single builder path and appended+swapped.
/// @p stopBelowThreshold stops the raw scan at the first candidate below gateCtx.threshold
/// (the FM2 inclusion policy). Returns true iff a promotion occurred.
bool promoteToWinner(std::vector<ChordAnalysisResult>& results,
                     const PostScoringGateContext&      gateCtx,
                     const ChordAnalyzerPreferences&    prefs,
                     const PromotionTarget&             target,
                     std::size_t                        presentHint,
                     bool                               stopBelowThreshold);

/// The vertical extension/alteration identity of a chord (the ChordIdentity fields
/// that describe its colour, not its root/quality/bass).
struct ChordExtensionInfo {
    uint32_t extensions = 0;          ///< Extension/alteration bitmask (see Extension enum)
    bool     naturalFifthPresent = false;  ///< P5 above root sounding (It+6 vs Ger+6 discriminator)
};

/// Extract the vertical extension/alteration identity for a FIXED (root, quality) from
/// the weighted pc view — the SAME primitive analyzeChord()/buildChordResult() use
/// (detectExtensions + the exact flag mapping + the naturalFifthPresent rule), factored
/// out and exposed so a downstream consumer can COMPLETE a chord's identity without
/// re-running the analysis (the Layer-4 slice decoder's L4->L5 carry,
/// cowork_layer4_chordsymbol_design.md §7). Pure: reads only @p pcWeight + @p tpcForPc
/// (both already produced by analyzeChord's snapshot); performs NO scoring and NO quality
/// mutation — the committed @p quality is authoritative, so the Sus->Major(omitsThird) and
/// Sus2->Sus4 upgrades that buildChordResult applies only when it CHANGES the quality are
/// intentionally NOT applied here (a fixed-quality extraction never mutates its quality).
/// @p rootTpc names the root enharmonically for the #13-vs-b7 spelling disambiguation.
ChordExtensionInfo deriveChordExtensions(
    const std::array<double, 12>& pcWeight,
    int rootPc, ChordQuality quality,
    const std::array<int, 12>& tpcForPc,
    int rootTpc, double extThreshold);

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
        PostScoringGateContext* gateCtxOut = nullptr,
        function::ScoringSnapshot* snapshotOut = nullptr) const override;

    /// Diagnostic VIEW into the production pipeline (Stage 2.3). Replays the exact
    /// production sequence — analyzeChord() (capturing the snapshot + gate context),
    /// then applyIter8691Pedal() and applyPostScoringGates() — and decorates the result
    /// with the ORACLE per-cell breakdown, the COMPETITION progression-signal terms of
    /// the winning bass group, and the POST-GATES winner trail. finalWinner is the
    /// production winner BY CONSTRUCTION (identical to analyzeWithGates().front()).
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
