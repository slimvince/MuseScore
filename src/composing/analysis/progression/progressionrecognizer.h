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

// ── composing/analysis/progression/progressionrecognizer ─────────────────────
//
// THE PROGRESSION-RECOGNITION CONSUMER — the Layer-5/6 consumer of the Harmonic
// Vocabulary. Spec (the contract, FULLY RATIFIED 2026-07-02): the consumer design
// cowork_progression_schema_design.md §3/§4 (§0 terms; §4.1 recognition; §4.2
// substitutions; §4.3 the evidence contribution; §4.4 the annotation; §4.5 the
// idiom-mixture weighting; §4.6 harmonic sequences). Component it consumes:
// cowork_progression_schema_dictionary.md (the Vocabulary). Placement/naming are a
// DECLARED build decision (report §"declared decisions"): a dedicated progression/
// sub-namespace beside the L5 function/ units — it is the CONSUMER that bridges the
// Vocabulary (the catalog) and Layer 5's committed progression, producing the L6
// annotation. NOT the grammar owner (that is function/functionprogression, Layer 5)
// and NOT the catalog owner (that is vocabulary/harmonicvocabulary) — see the D5
// dependency-map cross-comments at both of those headers.
//
// WHAT IT DOES (design §1). It recognises NAMED progressions — including
// substitutions within them — in the committed progression, reading no notes and
// detecting nothing new. A recognition is used two ways: as EVIDENCE where Layer 4
// abstained (§4.3, a §5.5 functional-plausibility feature) or committed (§4.3, the
// §8/frame-F-B override contribution), and as a NAME in the output (§4.4, a
// progression-schema-span for Layer 6). It also ALWAYS emits the recognised
// harmonic sequences (§4.6) as typed key-evidence output.
//
// DORMANT (design §7): NO production consumer — nothing in src/ calls
// recognizeProgressions(); it is reachable only from its own module, its unit tests
// (progressionrecognizer_tests.cpp), and the read-only diagnostic dump
// (tools/batch_analyze --dump-progressions, default OFF). So adding it is
// byte-identical on production by construction (the L5/L6-step firewall precedent —
// harmonicvocabulary / groupinglayer). Engagement (the §5.5 feature + §8 override
// wiring + the L6 SchemaSpan host) is a LATER step; the §5.3 key-channel CONSUMPTION
// (§4.6 roles) is gated on declaring frame F-C in the confidence contract and is NOT
// wired here — the sequence OUTPUT existing is this build's whole obligation.
//
// REUSE, NOT A PARALLEL ENCODING (the firewall discipline the Vocabulary followed):
//   • THE RECOGNISE QUERY — reuses HarmonicVocabulary::recognise over the committed
//     progression; this module owns NO second matcher. The per-position recognise
//     input is the Vocabulary's own SpanChord (embedded in CommittedChord below), so
//     there is one chord-span type, not two.
//   • CHORD QUALITY / EXTENSION — the existing analysis::ChordQuality + Extension
//     bitmask; no second quality vocabulary.
//   • THE GRAMMAR — the pairwise licensing test is functionprogression's; this
//     consumer never re-implements it (the D5 one-owner rule).
//
// EVERY NUMERIC VALUE IS A DECLARED DEFAULT (design §4.5/§4.6 firewall — "no θ, no
// tuning"): the §4.5 blend rate, admission threshold, mode-cue factor and
// chords-only factor are RecognitionParams defaults, precision-phase, NOT tuned. The
// DIRECTION of each is fixed by §4.5 (the mode-cue and chords-only factors are < 1;
// the admission threshold is a floor; the blend moves seed → histogram as evidence
// accumulates); the VALUE is Stage-5. This file fixes the RULES and their DIRECTION.

#include <array>
#include <cstddef>
#include <string>
#include <vector>

#include "composing/analysis/vocabulary/harmonicvocabulary.h"  // HarmonicVocabulary, SpanChord, Entry,
                                                               // SubstitutionType, Idiom(Set), ChordQuality

namespace mu::composing::analysis::progression {

// ── §0 the idiom weight vector — one weight per idiom (§4.5) ───────────────────
//
// A fixed-size vector over the ratified five idioms, indexed in the enum's own
// order: 0 = DiatonicFunctional, 1 = ChromaticFunctional, 2 = SeventhFunctional,
// 3 = TriadicModal, 4 = ChromaticColoristic. kIdiomCount mirrors the five Idiom
// bits; idiomIndex() maps an Idiom bit to its index.
inline constexpr std::size_t kIdiomCount = 5;
using IdiomWeights = std::array<double, kIdiomCount>;
/// The score's idiom-evidence histogram (§4.5 phase 2): match-score mass per idiom.
using IdiomEvidenceHistogram = std::array<double, kIdiomCount>;

/// The all-equal seed (§4.5): the mixture's starting value when NO preset is given.
/// Sums to 1 — a uniform prior over the five idioms.
inline constexpr IdiomWeights kEqualSeed = { 0.2, 0.2, 0.2, 0.2, 0.2 };

/// The index [0,4] of an Idiom bit in the weight vector (its bit position). Returns
/// kIdiomCount for a non-single-bit / unknown value (defensive; skipped by callers).
std::size_t idiomIndex(Idiom idiom);

/// max over an IdiomSet of the weight vector (§4.5: prior uses the MAX, never the
/// sum — an entry tagged with several idioms is not thereby advantaged). Returns 0
/// for the empty set.
double maxWeightOverIdioms(const IdiomWeights& w, IdiomSet idioms);

// ── The firewall constants (design §4.5/§4.6 — DECLARED DEFAULTS, NOT tuned) ────
struct RecognitionParams {
    /// §4.5 phase-2 blend rate. The mixture is `w = (1-α)·seed + α·histogram` with
    /// α = E / (E + blendRate), where E = the total idiom-evidence mass. E = 0 (no
    /// recognised evidence) ⇒ α = 0 ⇒ w = seed; E → ∞ (abundant evidence) ⇒ α → 1 ⇒
    /// the histogram dominates — the §4.5 direction. Declared default 1.0 (NOT
    /// tuned); the direction is fixed, the value precision-phase.
    double blendRate = 1.0;

    /// §4.5 admission threshold: a recognition is ADMITTED when its prior strength
    /// is STRICTLY ABOVE this floor. Declared default 0.0 (inert — admits any
    /// positive prior); the direction (a floor) is fixed, the value precision-phase.
    double admissionThreshold = 0.0;

    /// §4.5 mode-cue factor (< 1, never 0 — "modes mix"): the prior strength is
    /// multiplied by this when the entry's Mode tag contradicts the local key's mode
    /// at the recognised span. Declared default 0.5 (NOT tuned); the direction (< 1)
    /// is fixed by §4.5, the value precision-phase.
    double modeCueFactor = 0.5;

    /// §4.5 chords-only factor (< 1): the prior strength is multiplied by this for a
    /// voiceLeadingDefined entry (D7 — recognisable by its chord skeleton alone, so
    /// under-identified by its chords). Declared default 0.5 (NOT tuned); the
    /// direction (< 1) is fixed by §4.5, the value precision-phase.
    double chordsOnlyFactor = 0.5;
};

/// Global default recognition parameters.
inline constexpr RecognitionParams kDefaultRecognitionParams{};

// ── §3 input: the committed progression (producer-agnostic POD views) ─────────
//
// "The committed progression" (§0) = Layer 5's §7 output for a region: the ordered
// chords the layers COMMITTED, each with its local key. This module reads only the
// small POD views below (the established L5-unit pattern — functionoutput.h /
// groupinglayer.h); at engage each is mapped from the real FunctionLayerOutput per
// unit, and the tests inject by hand.

/// One ranked candidate reading published where Layer 4 ABSTAINED (Layer 4 §7 — the
/// possible chords, ranked, that Layer 5 §5.5 selects among). Carried only for the
/// §4.3 abstained-feature path.
struct CandidateReading {
    int rootPc = -1;
    ChordQuality quality = ChordQuality::Unknown;
    uint32_t extensions = 0;
    double functionalPlausibility = 0.0;  ///< the §5.5 "close"-rule score for this reading
};

/// One position of the committed progression (one L5 §7 unit's grouping-relevant
/// carry). `chord` is the reading used for the recognise query — the COMMITTED
/// reading where Layer 4 committed, or (by the caller's convention) the TOP-ranked
/// candidate reading where Layer 4 abstained (the best available reading; there is
/// no committed chord at an abstained position). `rankedCandidates` is the full
/// ranked list, read ONLY by the §4.3 abstained-feature path.
struct CommittedChord {
    SpanChord chord;                          ///< the recognise-query chord (REUSED Vocabulary type)
    int startTick = 0;
    int endTick = 0;

    bool committed = true;                    ///< an L4 Commit/Inherit (vs an abstain) — §0/§4.3
    double compositeConfidence = 1.0;         ///< L4's [0,1] composite confidence — the §8 threshold-scaling input

    std::vector<CandidateReading> rankedCandidates;  ///< §4.3 abstained: the readings to select among
};
using CommittedProgression = std::vector<CommittedChord>;

// ── §4.2/§4.4 output: the progression-schema-span (D6) ─────────────────────────

/// §4.2 a substituted-member read-out carried on a recognised span: what the surface
/// chord stands in for. The literal Roman numeral is UNCHANGED (design §4.2, D4); the
/// substitution is recorded only here.
struct SchemaSubstitution {
    int position = -1;                                    ///< committed-progression index
    SubstitutionType substitution = SubstitutionType::TritoneSub;
    std::string readOut;                                  ///< e.g. "♭II7 = subV7/I (tritone substitution)"
};

/// §4.4 (D6) one PROGRESSION-SCHEMA-SPAN per ADMITTED recognition — the annotation
/// for Layer 6. Read-only, additive, cross-cutting punctuation-spans. At engage this
/// maps onto the L6 grouping::SchemaSpan host (D6; the L6 struct's stale "sequence-
/// span" wording is a separate Cowork doc-pass rename item — NOT wired here).
struct ProgressionSchemaSpan {
    std::string name;                         ///< the recognised entry's conventional name
    IdiomSet idioms = 0;                      ///< the entry's idiom set (multi-valued)
    int startIndex = 0;                       ///< covered position range [startIndex, endIndex)
    int endIndex = 0;
    int startTick = 0;                        ///< covered tick range (for the L6 host)
    int endTick = 0;
    double matchScore = 0.0;                  ///< the Vocabulary's match score (v1: 1.0, an exact realisation)
    double priorStrength = 0.0;               ///< §4.5 prior strength (this span passed admission)
    bool chordsOnly = false;                  ///< D7 — a voiceLeadingDefined entry, recognised by chords alone
    std::vector<SchemaSubstitution> substitutedMembers;   ///< §4.2 the substituted-member read-outs (may be empty)
};

// ── §4.3 output: the evidence contribution (both conditions, SELECTION-only) ───

/// §4.3 (abstained) one §5.5 functional-plausibility FEATURE contribution. At an
/// abstained position covered by an admitted recognition, "this ranked candidate
/// reading fills the recognised member position" enters as one §5.5 feature, weighted
/// by the recognition's prior strength. SELECTION-only: it names an EXISTING ranked
/// candidate (selectedCandidateIndex), never a reading built from the notes. The §5.5
/// selection rule is otherwise unchanged — this module produces the feature; Layer 5
/// consumes it (NOT wired here).
struct AbstainedFeature {
    int position = -1;                        ///< committed-progression index (Layer 4 abstained here)
    int memberRootPc = -1;                    ///< the reading that fills the member (the surface realisation)
    ChordQuality memberQuality = ChordQuality::Unknown;
    double weight = 0.0;                      ///< = the recognition's prior strength (the feature weight)
    int selectedCandidateIndex = -1;          ///< the ranked candidate that fills the member, or -1 if none
    std::string schemaName;                   ///< the recognition supplying this feature
};

/// §4.3 (committed) one frame-F-B OVERRIDE contribution. Where an admitted
/// recognition's member position demands a DIFFERENT root or quality than the
/// committed reading, the recognition's prior strength enters the SAME contradiction
/// quantity frame F-B already compares. SELECTION-only: the replacement it would
/// select is the member's realisation (an existing reading), never a reading built
/// from the notes. This module produces the contribution; the §8 threshold test /
/// firing (threshold scaled to compositeConfidence, tie-holds-incumbent, once-per-
/// pass) is Layer 5's — NOT run here (no new comparison frame is introduced).
///
/// NB (design §8, report): under the exact-match v1 recogniser this contribution is
/// STRUCTURALLY INERT — a literal member matches the committed reading by construction
/// (no contradiction), and a substituted member is §4.2-excluded from override. The
/// path is built (and unit-tested directly via overrideContributionFor / the
/// contradiction predicate) so it is ready for the Stage-5 partial/variant matcher,
/// where a recognition can match with a member NOT realised by the committed reading.
struct CommittedOverrideContribution {
    int position = -1;
    int committedRootPc = -1;                 ///< the L4 committed reading (differs from the member)
    ChordQuality committedQuality = ChordQuality::Unknown;
    int memberRootPc = -1;                    ///< the recognised member's demanded realisation (the selection)
    ChordQuality memberQuality = ChordQuality::Unknown;
    double priorStrength = 0.0;               ///< enters the F-B contradiction quantity
    double compositeConfidence = 0.0;         ///< the committed reading's confidence (the §8 threshold-scaling input)
    std::string schemaName;
};

// ── §4.6 output: harmonic sequences as evidence of the local key ──────────────

/// §4.6 one recognised HARMONIC SEQUENCE — the same progression repeated at
/// successive transpositions (a Monte/Fonte/descending-fifths chain). ALWAYS emitted
/// (evidence is never discarded — the no-information-loss principle). The §5.3
/// CONSUMPTION (role (i) corroboration / role (ii) the substitute confirming channel)
/// is Layer 5's and is gated on frame F-C — NOT wired here.
struct HarmonicSequence {
    std::string name;                         ///< the repeated progression entry's name
    int transpositionStep = 0;                ///< the constant nonzero semitone shift between repetitions [1,11]
    int startIndex = 0;                       ///< covered position range [startIndex, endIndex)
    int endIndex = 0;
    int startTick = 0;
    int endTick = 0;
    int repetitions = 0;                      ///< number of transposed repetitions (≥ 2 by construction)
    double priorStrength = 0.0;               ///< the max prior strength among the repeated recognitions
};

// ── §3 the module output ───────────────────────────────────────────────────────
struct ProgressionRecognitionOutput {
    IdiomWeights weights = kEqualSeed;                       ///< §4.5 phase-2 mixture w (exposed — the future auto-detect)
    std::vector<ProgressionSchemaSpan> schemaSpans;          ///< §4.4 the annotation (ordered: longer, then more specific)
    std::vector<AbstainedFeature> abstainedFeatures;         ///< §4.3 abstained-position §5.5 features
    std::vector<CommittedOverrideContribution> overrides;    ///< §4.3 committed-position F-B contributions
    std::vector<HarmonicSequence> sequences;                 ///< §4.6 always-emitted key-evidence output
};

// ── §4.5 the exposed pure rules (unit-tested in isolation) ─────────────────────

/// §4.5 phase 2 — the discovered mixture. `w = (1-α)·seedNorm + α·histogramNorm`,
/// α = E / (E + blendRate), E = Σ histogram. seedNorm/histogramNorm are the inputs
/// normalised to sum 1 (a zero histogram ⇒ α = 0 ⇒ w = seedNorm; a zero seed ⇒ the
/// equal seed). Forward-only: the histogram is phase-1 output, never phase-3's.
IdiomWeights blendIdiomWeights(const IdiomWeights& seed,
                               const IdiomEvidenceHistogram& histogram,
                               double blendRate);

/// §4.5 phase 3 — the prior strength of one recognition:
///   `match score × max(w over the entry's IdiomSet)` (the MAX, not the sum),
///   × modeCueFactor if `modeContradicts`, × chordsOnlyFactor if `chordsOnly`.
double recognitionPriorStrength(double matchScore, const IdiomWeights& w, IdiomSet idioms,
                                bool modeContradicts, bool chordsOnly,
                                const RecognitionParams& params = kDefaultRecognitionParams);

/// §4.3 the F-B contradiction predicate: does the recognised member (root, quality)
/// demand a DIFFERENT root or quality than the committed reading? (The trigger of the
/// committed-override path; excludes substituted members at the call site per §4.2.)
bool memberContradictsCommittedReading(int memberRootPc, ChordQuality memberQuality,
                                       int committedRootPc, ChordQuality committedQuality);

/// §4.3 build the F-B override contribution for a contradicting committed position —
/// SELECTION-only (the member's realisation is the selected replacement). A pure
/// assembler exposed for the direct unit test of the F-B semantics; the §8 firing is
/// Layer 5's and is not decided here.
CommittedOverrideContribution
overrideContributionFor(int position, int committedRootPc, ChordQuality committedQuality,
                        int memberRootPc, ChordQuality memberQuality,
                        double priorStrength, double compositeConfidence,
                        const std::string& schemaName);

/// §4.3 select the ranked candidate reading that fills a member (root + quality) —
/// returns the first matching candidate's index, or -1 when none fills it. The
/// abstained-feature SELECTION (never a reading built from the notes).
int selectCandidateFillingMember(const std::vector<CandidateReading>& candidates,
                                 int memberRootPc, ChordQuality memberQuality);

// ── The §4 recognition (the module entry point) ────────────────────────────────

/// Recognise named progressions in `progression` (design §4). Runs the three-phase
/// §4.5 mixture (weight-free recognise → estimate w from the idiom-evidence histogram
/// → weight and emit), then produces: the §4.4 progression-schema-spans (one per
/// admitted recognition, ordered longer-then-more-specific, carrying substituted-
/// member read-outs and the D7 chords-only mark), the §4.3 evidence contributions
/// (the abstained-position §5.5 features and the committed-position F-B contributions,
/// both SELECTION-only), and the §4.6 harmonic sequences (always emitted). Additive
/// and read-only over Layer 5; it changes NO Roman numeral (D4). Nothing is produced
/// where nothing is recognised (design §3).
ProgressionRecognitionOutput
recognizeProgressions(const CommittedProgression& progression,
                      const HarmonicVocabulary& vocabulary,
                      const IdiomWeights& seed = kEqualSeed,
                      IdiomSet idiomSubset = kAllIdioms,
                      const RecognitionParams& params = kDefaultRecognitionParams);

} // namespace mu::composing::analysis::progression
