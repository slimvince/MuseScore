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

// ── composing/analysis/types — the cross-layer value-types LEAF ──────────────
//
// A dependency-free LEAF header (STL only — no chord/, no key/, no engraving):
// it holds the value types that cross the L1.5 / L3 / L4 boundaries so the
// engravingbridge (L1.5) and key (L3) headers can compile WITHOUT including the
// chord (L4) headers. This kills the two type-only header back-edges the
// layering audit (Q2) found: regiontonecollector.h → {chordanalyzer.h,
// keymodeanalyzer.h} and keymodeanalyzer.h → chord/analysisutils.h.
//
// Every type below is a PURE RELOCATION from its former home — same name, same
// namespace, same layout, same definition; only the *defining file* changed.
// chord/chordanalyzer.h and key/keymodeanalyzer.h now #include this leaf, so all
// existing includers (and the gtest suites) get the types transitively, unchanged.
//
//   - mu::composing::function : ScoringPhase   (moved from chord/chordanalyzer.h)
//   - mu::composing::analysis : ParameterBound / ParameterBoundsMap
//                                              (moved from chord/analysisutils.h)
//                               DecodeQualityLevel, ChordQuality, ChordAnalysisTone,
//                               ChordAnalyzerPreferences (+ kDefault),
//                               ChordTemporalContext
//                                              (moved from chord/chordanalyzer.h)
//                               KeySigMode, KeyModeAnalyzerPreferences (+ kDefault),
//                               PitchContext   (moved from key/keymodeanalyzer.h;
//                                               PitchContext un-nested out of
//                                               class KeyModeAnalyzer — that class
//                                               keeps a member alias
//                                               `using PitchContext = analysis::PitchContext;`)

#include <array>
#include <cstdint>
#include <map>
#include <string>

namespace mu::composing::function {

/// Scoring phase for applyHarmonicFunction(). Selects whether the competition
/// pipeline applies the progression signals (w_seq / w_dim / step bonuses) and Gate R.
///
/// Lives in this leaf (not harmonicfunctionlayer.h) on purpose: ChordAnalyzerPreferences
/// carries a ScoringPhase with the `= ScoringPhase::Final` default member initializer,
/// which needs the complete enum, and chordanalyzer.h cannot include harmonicfunctionlayer.h
/// (the include runs the other way). harmonicfunctionlayer.h sees the full definition
/// through its include of chordanalyzer.h, which includes this header.
enum class ScoringPhase : uint8_t {
    Segmentation, ///< Boundary exploration — progression signals suppressed and Gate R
                  ///< skipped; rootContinuityBonus stays active (segmentation depends on it).
    Final         ///< Per-region final scoring — all signals active.
};

} // namespace mu::composing::function

namespace mu::composing::analysis {

// ── Parameter bounds (relocated from chord/analysisutils.h) ──────────────────

/// Describes the valid range for a single numeric scoring parameter.
///
/// Used by ChordAnalyzerPreferences::bounds() and KeyModeAnalyzerPreferences::bounds()
/// to expose all tunable parameters to automated optimizers or UI sliders.
///
/// isManual: when true, the parameter should be held fixed during automated
/// optimization (it is wired to a user-visible preference or has a narrow
/// hand-tuned sweet-spot).  When false, it is fair game for gradient-based
/// or grid search optimizers.
struct ParameterBound {
    double min;
    double max;
    bool   isManual = false;
};

/// Convenience alias for the map returned by bounds().
using ParameterBoundsMap = std::map<std::string, ParameterBound>;

// ── Chord-path decoder quality level (relocated from chord/chordanalyzer.h) ──

/// Chord-path decoder quality level (Stage 3.1; docs/decoder_design.md §9).
/// Selects the beam width of the chord-path decoder (analysis/decode/).
///
/// Lives in this leaf (fully defined, not forward-declared) for the same reason as
/// ScoringPhase above: ChordAnalyzerPreferences carries a DecodeQualityLevel with a
/// default member initializer (`= DecodeQualityLevel::FastBeam1`), which needs the
/// complete enum, and chordanalyzer.h cannot include the decode header — the include
/// runs the other way (chordpathdecoder.h → chordanalyzer.h).
///
/// Level 0 (FastBeam1) is the only level implemented at Stage 3.1 and is the
/// byte-identical default: a re-expression of the greedy left-to-right commit
/// chain. Higher levels are reserved for Stage 3.2 (wider beam, forward signals
/// promoted to decoded-successor edges) and currently behave as FastBeam1 (no-op).
enum class DecodeQualityLevel : uint8_t {
    FastBeam1 = 0,  ///< beam 1 — byte-identical greedy commit; forward signals = cold lookahead
    Normal    = 1,  ///< reserved (Stage 3.2) — small beam; NOT yet active (behaves as FastBeam1)
    Deep      = 2,  ///< reserved (Stage 3.2+) — wide / exact DP; NOT yet active (behaves as FastBeam1)
};

// ── Chord quality (relocated from chord/chordanalyzer.h) ─────────────────────

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

// ── ChordAnalysisTone (relocated from chord/chordanalyzer.h) ─────────────────

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

// ── ChordAnalyzerPreferences (relocated from chord/chordanalyzer.h) ──────────

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

    // The four score-addition signals below + resolutionBonus above used to be folded
    // into the vertical sonority scorer (basisIndep / basisDep) as documented temporal
    // debt (ARCHITECTURE.md §4.1c, audit Finding 1). Stage 3.3 MIGRATED all five into the
    // competition pipeline (fn::resolutionEdgeBonus / fn::inversionContextBonus); these
    // members are now read THERE, not in analyzeChord(). The values/conditions are
    // unchanged. Do not re-fold a progression signal into the oracle.

    // ── Contextual inversion bonuses (§4.1b — applied by the competition pipeline) ──

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
    /// candidate across the inversion temporal signals combined — the four that
    /// actually feed the sum in fn::inversionContextBonus() (the competition pipeline,
    /// since Stage 3.3): stepwise (bassIsStepwiseFromPrevious), lookahead
    /// (bassIsStepwiseToNext), sameRoot (previousRootPc == rootPc), and completeTriad.
    /// The formerly-listed
    /// nextRoot / consecutive / recentRoot / weakBeat signals were never wired
    /// into this sum.
    /// Prevents runaway stacking when multiple signals fire simultaneously.
    /// Currently INERT on every code path: the cap is never overridden (both
    /// presets inherit this 2.0 default) and the four bonuses sum to at most
    /// 1.85 (Baroque/default) or 0.75 (Jazz), so std::min() never clamps.  See
    /// docs/scoring_model.md §4 ("currently inert" paragraph) for the full story.
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

    /// Chord-path decoder quality level (Stage 3.1; docs/decoder_design.md §9).
    /// Selects the decoder beam width (analysis/decode/chordpathdecoder.h). The
    /// default FastBeam1 (level 0) is a byte-identical re-expression of the greedy
    /// left-to-right commit chain; higher levels are reserved for Stage 3.2 and
    /// currently behave identically (no-op). No preset branches on this — it is a
    /// per-query quality knob, not a style preference (design §10).
    DecodeQualityLevel decodeQualityLevel = DecodeQualityLevel::FastBeam1;

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

// ── ChordTemporalContext (relocated from chord/chordanalyzer.h) ──────────────

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

// ── KeySigMode (relocated from key/keymodeanalyzer.h) ────────────────────────

/// The mode of a key.  All 21 modes (7 diatonic + 7 melodic minor + 7 harmonic minor)
/// are evaluated.
///
/// Enum ordinal == index into the MODES interval table in keymodeanalyzer.cpp.
/// Diatonic modes (0–6) come first so existing code casting to/from size_t is unaffected.
enum class KeySigMode {
    // ── Diatonic modes ────────────────────────────────────────────────────
    Ionian,       ///< Major (0 2 4 5 7 9 11)
    Dorian,       ///<       (0 2 3 5 7 9 10)
    Phrygian,     ///<       (0 1 3 5 7 8 10)
    Lydian,       ///<       (0 2 4 6 7 9 11)
    Mixolydian,   ///<       (0 2 4 5 7 9 10)
    Aeolian,      ///< Natural minor (0 2 3 5 7 8 10)
    Locrian,      ///<       (0 1 3 5 6 8 10)

    // ── Melodic minor family ──────────────────────────────────────────────
    MelodicMinor,     ///< Ascending melodic minor / jazz minor (0 2 3 5 7 9 11)
    DorianB2,         ///< Phrygian #6 (0 1 3 5 7 9 10)
    LydianAugmented,  ///< Lydian #5 (0 2 4 6 8 9 11)
    LydianDominant,   ///< Lydian b7 (0 2 4 6 7 9 10)
    MixolydianB6,     ///< Mixolydian b6 (0 2 4 5 7 8 10)
    AeolianB5,        ///< Locrian #2 (0 2 3 5 6 8 10)
    Altered,          ///< Altered / Super Locrian (0 1 3 4 6 8 10)

    // ── Harmonic minor family ─────────────────────────────────────────────
    HarmonicMinor,     ///< Natural minor #7 (0 2 3 5 7 8 11)
    LocrianSharp6,     ///< Locrian #6 (0 1 3 5 6 9 10)
    IonianSharp5,      ///< Major #5 (0 2 4 5 8 9 11)
    DorianSharp4,      ///< Dorian #4 (0 2 3 6 7 9 10)
    PhrygianDominant,  ///< Phrygian #3 / harmonic dominant (0 1 4 5 7 8 10)
    LydianSharp2,      ///< Lydian #2 (0 3 4 6 7 9 11)
    AlteredDomBB7,     ///< Harmonic minor mode 7 (0 1 3 4 6 8 9)
};

// ── KeyModeAnalyzerPreferences (relocated from key/keymodeanalyzer.h) ────────

/// Tunable scoring weights for KeyModeAnalyzer.
///
/// All values are compile-time defaults.  Replace each initialiser with a lookup
/// from the settings store once user-preferences infrastructure is available.
struct KeyModeAnalyzerPreferences {

    // ── Evidence weight caps ─────────────────────────────────────────────────

    /// Maximum combined weight contributed by a single pitch.
    /// Prevents one very long note from dominating the analysis.
    double noteWeightCap = 3.0;          // [empirical]

    /// Multiplier applied when a note is the lowest-sounding pitch (bass).
    /// The bass voice carries disproportionate harmonic information.
    double bassMultiplier = 2.0;         // [theory-grounded ordering, empirical value]

    // ── Scale membership scoring ─────────────────────────────────────────────
    //
    // Each note is classified against two scales: the candidate key scale and
    // the notated key-signature scale.  The combination produces four cases;
    // in-scale/in-signature earns the most, out-of-both earns the least.
    // Ordering is theory-grounded; values are empirical.

    double scaleScoreInBoth    =  1.00;  ///< Note is in candidate scale AND key-sig scale [theory-grounded ordering]
    double scaleScoreInCandidateOnly = 0.25;  ///< In candidate scale but not key-sig scale [empirical]
    double scaleScoreInKeySigOnly    = -0.20; ///< In key-sig scale but not candidate (chromatic neighbour) [empirical]
    double scaleScoreInNeither       = -0.05; ///< Outside both scales [empirical]

    // ── Tonal centre scoring ─────────────────────────────────────────────────
    //
    // Weights for tonic, third, fifth, and leading-tone evidence.
    // The ordering (tonic > third > fifth > leading tone) is theory-grounded.
    // Within each weight, the absolute value is empirically tuned.

    double tonicWeight       = 1.60;  ///< Tonic note present [theory-grounded ordering, empirical value]
    double thirdWeight       = 0.70;  ///< Third (M3 for major, m3 for minor) [empirical]
    double fifthWeight       = 0.50;  ///< Perfect fifth [empirical]
    double leadingToneWeight = 0.40;  ///< Leading tone (tonicPc + 11, used for both modes) [empirical]

    double completeTriadBonus  =  2.50;  ///< All three triad notes present simultaneously [empirical]
    double missingTonicPenalty = -2.50;  ///< Tonic entirely absent [empirical]

    double extraScaleFactor    = 0.10;   ///< Per-unit weight of non-triad in-scale notes [empirical]
    double extraScaleCap       = 5.0;    ///< Cap on total extra-scale weight [empirical]

    // ── Characteristic pitch scoring ────────────────────────────────────────
    //
    // Each mode has a single pitch that most distinguishes it from its closest
    // neighbor (e.g. Dorian's raised 6th vs Aeolian).  The presence of this
    // pitch boosts the candidate; its absence penalizes it.  Both the boost
    // and penalty values are empirical.

    double characteristicPitchBoost   = 1.80;  ///< Boost when characteristic pitch is present [empirical]
    double characteristicPitchPenalty = -0.60;  ///< Penalty when characteristic pitch is absent [empirical]

    // ── True leading-tone scoring ──────────────────────────────────────────
    //
    // The note a semitone below the tonic ((tonicPc + 11) % 12) is the
    // strongest tonal indicator in Western music.  Its presence boosts the
    // candidate regardless of whether it is diatonic to the mode (chromatic
    // leading tones, as in harmonic minor, still indicate the tonic).
    // This complements the mode-specific 7th-degree evidence in triad scoring.

    double trueLeadingToneBoost = 1.20;  ///< Bonus when semitone-below-tonic is present [empirical]

    // ── Mode priors (frequency bias) ────────────────────────────────────────
    //
    // One independent prior per mode.  Additive bias applied to every (tonicPc,
    // modeSlot) candidate.  A small prior prevents rare modes winning when pitch
    // evidence is ambiguous.  Defaults reflect the "Standard (classical)" preset.
    // The bridge overrides these from user preferences (21 independent sliders /
    // named presets) when available.  The former +0.2 Ionian internal offset is
    // now absorbed into the explicit Ionian prior (1.2) vs Aeolian prior (1.0).

    // Diatonic modes
    double modePriorIonian          =  1.20;  ///< [empirical — was tier1+0.2]
    double modePriorDorian          = -0.50;  ///< [empirical]
    double modePriorPhrygian        = -1.50;  ///< [empirical]
    double modePriorLydian          = -1.50;  ///< [empirical]
    double modePriorMixolydian      = -0.50;  ///< [empirical]
    double modePriorAeolian         =  1.00;  ///< [empirical — was tier1]
    double modePriorLocrian         = -3.00;  ///< [empirical]

    // Melodic minor family
    double modePriorMelodicMinor    = -0.50;  ///< [empirical]
    double modePriorDorianB2        = -1.50;  ///< [empirical]
    double modePriorLydianAugmented  = -2.00;  ///< [empirical]
    double modePriorLydianDominant   = -1.00;  ///< [empirical]
    double modePriorMixolydianB6    = -1.50;  ///< [empirical]
    double modePriorAeolianB5       = -2.50;  ///< [empirical]
    double modePriorAltered         = -3.50;  ///< [empirical]

    // Harmonic minor family
    double modePriorHarmonicMinor   = -0.30;  ///< [empirical]
    double modePriorLocrianSharp6   = -2.50;  ///< [empirical]
    double modePriorIonianSharp5    = -2.00;  ///< [empirical]
    double modePriorDorianSharp4    = -2.00;  ///< [empirical]
    double modePriorPhrygianDominant = -0.80;  ///< [empirical]
    double modePriorLydianSharp2    = -2.50;  ///< [empirical]
    double modePriorAlteredDomBB7   = -3.50;  ///< [empirical]

    // ── Tonal-centre comparison (relative pair disambiguation) ───────────────
    //
    // When the key signature is known, the relative major/minor pair is scored
    // by a focussed tonal-centre formula.  If the difference exceeds
    // tonalCenterDeltaThreshold, that candidate wins outright; otherwise the
    // raw score is used as the tiebreaker.
    //
    // tonalCenter* weights are independent of the main triad-score weights above
    // because this path runs AFTER the post-hoc disambiguation mutations (which
    // themselves use the main weights).  Keeping them separate lets both be tuned
    // without cross-interference.

    double tonalCenterTonicWeight  = 2.20;  ///< [empirical]
    double tonalCenterThirdWeight  = 1.00;  ///< [empirical]
    double tonalCenterFifthWeight  = 0.70;  ///< [empirical]
    double tonalCenterLeadingTone  = 0.50;  ///< [empirical]
    double tonalCenterTriadBonus   = 2.00;  ///< [empirical]
    double tonalCenterDeltaThreshold = 0.25; ///< Min delta to choose winner outright [empirical]

    // ── Key-signature proximity ──────────────────────────────────────────────
    //
    // Theory basis: when the notated key signature is known, candidate keys that
    // require more accidentals relative to the signature are penalised.  The
    // penalty grows linearly with the circle-of-fifths distance.  This is
    // theory-grounded; the per-step value is empirical.

    double keySignatureDistancePenalty = 0.60;  ///< Per circle-of-fifths step of distance [empirical]

    // ── Relative major/minor post-hoc mutations ──────────────────────────────
    //
    // After the main loop, the relative major/minor pair for each key is explicitly
    // disambiguated.  When one candidate has a complete tonic triad and the other
    // has no tonic note, a large boost (+ disambiguation bonus) and a small penalty
    // (- disambiguation cost) are applied.  When only one side has a tonic, a
    // smaller tonic-presence boost is applied.  Both are empirical.

    double disambiguationTriadBonus  = 4.50;  ///< One side has complete triad + tonic [empirical]
    double disambiguationTriadCost   = 1.50;  ///< Applied to the other side [empirical]
    double disambiguationTonicBonus  = 1.00;  ///< Only-tonic-present (no complete triad) [empirical]

    // ── Declared-mode hint (Stage 4b-i: demoted from a wall to a tiebreaker) ──
    //
    // When the caller provides a declared mode (e.g. from the score's key
    // signature), any candidate mode outside the declared mode class receives
    // this small additive penalty.  Since Stage 4b-i the magnitude is *small*
    // (1.0 by default, was 7.0): the demoted role is a genuine TIEBREAKER, not a
    // wall.  It can only flip the winner when the raw note-based score gap is
    // already within ~1.0 (i.e. when the note evidence is genuinely unsure); it
    // can no longer override clear note evidence (triad 2.50, disambiguation
    // 4.50).  Note-based major/minor inference is now PRIMARY; the declared mode
    // is a low-weight, droppable hint.  Droppable by construction: not applied
    // when the caller passes no declared mode (declaredMode == nullopt, e.g. the
    // --ignore-declared-mode measurement floor).  The final magnitude is Stage 5's
    // fit; 1.0 is the provisional measurement value.

    double declaredModePenalty = 1.0;  ///< Small declared-mode hint, outside-class candidates [empirical — Stage-5 fits]

    /// Measurement-only toggle (Stage 4b-i): when true, the resolver forces
    /// declaredMode = nullopt, so NO declared-mode influence is applied (the hint
    /// above is not subtracted, the partial-signature correction is skipped, and
    /// the piece-start opening is purely note-based).  This is the "no-crutch
    /// floor" condition wired to batch_analyze --ignore-declared-mode. Default
    /// false = no-op (every production / mode-present path is byte-identical).
    bool ignoreDeclaredMode = false;  ///< Force mode-absent resolution (measurement floor)

    // ── Beat-type weights for temporal window collection ─────────────────
    //
    // Mapping from MuseScore's BeatType enum to a weight applied during
    // pitch context collection.  The ordering (downbeat > stressed >
    // unstressed > subbeat) is theory-grounded; the specific values are
    // empirical — not derived from any measurement.

    // ── Normalized confidence mapping ──────────────────────────────────────
    //
    // The raw score gap between the top-1 and top-2 candidates is mapped to
    // a 0.0–1.0 confidence value through a sigmoid: 1 / (1 + exp(-k * (gap - midpoint))).
    // The midpoint is the gap value that maps to 0.5 confidence.
    // The steepness controls how quickly confidence rises with increasing gap.
    // Both values are empirical.

    double confidenceSigmoidMidpoint  = 2.0;   ///< Gap at which confidence = 0.5 [empirical]
    double confidenceSigmoidSteepness = 1.5;   ///< Rate of confidence rise [empirical]

    // ── Dynamic lookahead ─────────────────────────────────────────────────
    //
    // When confidence after the initial fixed lookahead is below
    // dynamicLookaheadConfidenceThreshold, the lookahead window is expanded by
    // dynamicLookaheadStepBeats per iteration up to dynamicLookaheadMaxBeats.
    // Each expansion re-collects pitch context and re-runs the analyzer.
    // Lives in the bridge / batch_analyze caller, not in analyzeKeyMode itself.
    // Theory-grounded ordering (expanding beats); values are empirical.

    double dynamicLookaheadConfidenceThreshold = 0.60; ///< Stop expanding when confidence ≥ this [empirical]
    int    dynamicLookaheadStepBeats            = 2;    ///< Beats added per expansion step [empirical]
    int    dynamicLookaheadMaxBeats             = 24;   ///< Hard cap on lookahead [empirical]

    // ── Mode-switching hysteresis ─────────────────────────────────────────
    //
    // When the inferred mode differs from the previous inference at a nearby
    // tick, the challenger must exceed the incumbent's score by this margin to
    // cause a switch.  Prevents thin transient evidence from triggering
    // spurious modulations.
    // Lives in the bridge / batch_analyze caller; not used inside analyzeKeyMode.

    double hysteresisMargin = 2.0;  ///< Score advantage required to switch modes when key sigs differ [empirical]

    /// Higher hysteresis applied when the challenger shares the same key signature
    /// as the incumbent (relative major/minor pair, e.g. D minor ↔ F major).
    /// These pairs are structurally ambiguous — all diatonic notes are shared —
    /// so a larger margin is needed to avoid spurious switches on passing chords.
    double relativeKeyHysteresisMargin = 2.0;  ///< Same-key-sig switch barrier [empirical, = hysteresisMargin by default]

    // ── Beat-type weights for temporal window collection ─────────────────
    //
    // Mapping from MuseScore's BeatType enum to a weight applied during
    // pitch context collection.  The ordering (downbeat > stressed >
    // unstressed > subbeat) is theory-grounded; the specific values are
    // empirical — not derived from any measurement.

    double beatWeightDownbeat            = 1.0;  ///< [empirical]
    double beatWeightCompoundStressed    = 0.7;  ///< [empirical]
    double beatWeightSimpleStressed      = 0.7;  ///< [empirical]
    double beatWeightCompoundUnstressed  = 0.4;  ///< [empirical]
    double beatWeightSimpleUnstressed    = 0.4;  ///< [empirical]
    double beatWeightCompoundSubbeat     = 0.2;  ///< [empirical]
    double beatWeightSubbeat             = 0.2;  ///< [empirical]

    /// Returns the valid range for every numeric scoring parameter.
    ///
    /// Parameters marked isManual=true are wired to user-visible preferences or
    /// have narrow hand-tuned sweet-spots; automated optimizers should leave them
    /// fixed.  Parameters marked isManual=false are safe for gradient-based or
    /// grid-search tuning.
    ///
    /// Integer parameters (dynamicLookaheadStepBeats, dynamicLookaheadMaxBeats)
    /// are omitted; they require integer-aware optimizers and are unlikely to
    /// benefit from fine-grained tuning.
    ParameterBoundsMap bounds() const
    {
        return {
            // Evidence weight caps
            { "noteWeightCap",                     { 1.0,  6.0 } },
            { "bassMultiplier",                    { 1.0,  4.0 } },
            // Scale membership scoring
            { "scaleScoreInBoth",                  { 0.5,  2.0 } },
            { "scaleScoreInCandidateOnly",         { 0.0,  1.0 } },
            { "scaleScoreInKeySigOnly",            {-1.0,  0.0 } },
            { "scaleScoreInNeither",               {-0.5,  0.0 } },
            // Tonal centre scoring
            { "tonicWeight",                       { 0.5,  3.0 } },
            { "thirdWeight",                       { 0.0,  2.0 } },
            { "fifthWeight",                       { 0.0,  2.0 } },
            { "leadingToneWeight",                 { 0.0,  1.5 } },
            { "completeTriadBonus",                { 0.5,  5.0 } },
            { "missingTonicPenalty",               {-5.0, -0.5 } },
            { "extraScaleFactor",                  { 0.0,  0.5 } },
            { "extraScaleCap",                     { 1.0, 10.0 } },
            // Characteristic pitch scoring
            { "characteristicPitchBoost",          { 0.5,  4.0 } },
            { "characteristicPitchPenalty",        {-2.0,  0.0 } },
            // Leading tone
            { "trueLeadingToneBoost",              { 0.0,  3.0 } },
            // Mode priors — isManual because each slider maps to a user preference
            { "modePriorIonian",        { -5.0, 5.0, true } },
            { "modePriorDorian",        { -5.0, 5.0, true } },
            { "modePriorPhrygian",      { -5.0, 5.0, true } },
            { "modePriorLydian",        { -5.0, 5.0, true } },
            { "modePriorMixolydian",    { -5.0, 5.0, true } },
            { "modePriorAeolian",       { -5.0, 5.0, true } },
            { "modePriorLocrian",       { -5.0, 5.0, true } },
            { "modePriorMelodicMinor",  { -5.0, 5.0, true } },
            { "modePriorDorianB2",      { -5.0, 5.0, true } },
            { "modePriorLydianAugmented", { -5.0, 5.0, true } },
            { "modePriorLydianDominant",  { -5.0, 5.0, true } },
            { "modePriorMixolydianB6",  { -5.0, 5.0, true } },
            { "modePriorAeolianB5",     { -5.0, 5.0, true } },
            { "modePriorAltered",       { -5.0, 5.0, true } },
            { "modePriorHarmonicMinor", { -5.0, 5.0, true } },
            { "modePriorLocrianSharp6", { -5.0, 5.0, true } },
            { "modePriorIonianSharp5",  { -5.0, 5.0, true } },
            { "modePriorDorianSharp4",  { -5.0, 5.0, true } },
            { "modePriorPhrygianDominant", { -5.0, 5.0, true } },
            { "modePriorLydianSharp2",  { -5.0, 5.0, true } },
            { "modePriorAlteredDomBB7", { -5.0, 5.0, true } },
            // Tonal centre comparison
            { "tonalCenterTonicWeight",            { 0.5,  4.0 } },
            { "tonalCenterThirdWeight",            { 0.0,  2.0 } },
            { "tonalCenterFifthWeight",            { 0.0,  2.0 } },
            { "tonalCenterLeadingTone",            { 0.0,  1.5 } },
            { "tonalCenterTriadBonus",             { 0.5,  5.0 } },
            { "tonalCenterDeltaThreshold",         { 0.0,  1.0 } },
            // Key-signature proximity
            { "keySignatureDistancePenalty",       { 0.0,  2.0 } },
            // Relative pair disambiguation
            { "disambiguationTriadBonus",          { 1.0,  8.0 } },
            { "disambiguationTriadCost",           { 0.0,  4.0 } },
            { "disambiguationTonicBonus",          { 0.0,  3.0 } },
            // Declared-mode hint — isManual: user may override. Lower bound 0.0
            // (Stage 4b-i) so the demoted small-hint / fully-dropped exploration
            // is expressible (was {3.0,15.0} when it was a wall).
            { "declaredModePenalty",               { 0.0, 15.0, true } },
            // Confidence sigmoid
            { "confidenceSigmoidMidpoint",         { 0.5,  5.0 } },
            { "confidenceSigmoidSteepness",        { 0.5,  5.0 } },
            // Dynamic lookahead threshold
            { "dynamicLookaheadConfidenceThreshold",{ 0.3, 0.9 } },
            // Hysteresis margins — isManual: tightly coupled to user experience
            { "hysteresisMargin",                  { 0.5,  5.0, true } },
            { "relativeKeyHysteresisMargin",       { 0.5,  8.0, true } },
            // Beat weights
            { "beatWeightDownbeat",                { 0.5,  2.0 } },
            { "beatWeightCompoundStressed",        { 0.3,  1.5 } },
            { "beatWeightSimpleStressed",          { 0.3,  1.5 } },
            { "beatWeightCompoundUnstressed",      { 0.1,  1.0 } },
            { "beatWeightSimpleUnstressed",        { 0.1,  1.0 } },
            { "beatWeightCompoundSubbeat",         { 0.0,  0.5 } },
            { "beatWeightSubbeat",                 { 0.0,  0.5 } },
        };
    }
};

/// Global default preferences.
inline constexpr KeyModeAnalyzerPreferences kDefaultKeyModeAnalyzerPreferences{};

// ── PitchContext (relocated + un-nested from class KeyModeAnalyzer) ──────────

/// Pitch context passed from the score/notation layer into the abstract analysis.
/// Carries duration and metric weight so longer, metrically-strong notes have more influence.
///
/// Un-nested from class KeyModeAnalyzer (it depends on no KeyModeAnalyzer internals).
/// KeyModeAnalyzer keeps a member alias `using PitchContext = analysis::PitchContext;`
/// so the existing `KeyModeAnalyzer::PitchContext` call sites resolve unchanged.
/// Namespace-qualified — no clash with the unrelated muse::mpe::PitchContext.
struct PitchContext {
    int pitch = 0;               ///< MIDI pitch number
    double durationWeight = 1.0; ///< Duration in quarter-note units; larger = more influence
    double beatWeight = 1.0;     ///< Metric position: 1.0=downbeat, ~0.2=offbeat
    bool isBass = false;         ///< True if lowest sounding pitch at this time instant
};

} // namespace mu::composing::analysis
