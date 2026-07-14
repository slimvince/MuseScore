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

#include "chordanalyzer.h"
#include "analysisutils.h"
#include "keycollectionprobe.h"      // OI-168 measurement scaffolding (default-OFF)
#include "composing/analysis/function/harmonicfunctionlayer.h"
#include "../param/paramoverride.h"   // Stage-5 fitter: optional constant override (D-6)

#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <limits>
#include <utility>

namespace fn = mu::composing::function;
namespace kcp = mu::composing::analysis::keycollectionprobe;

namespace mu::composing::analysis {
namespace {

// Three-way classification for a note that is NOT part of the template being scored.
//
//   Extension    — neutral colour tone; adds slight evidence for the candidate.
//   Contradiction — structurally incompatible with the template quality; the note's
//                   presence is positive evidence *against* this candidate and earns
//                   a larger penalty than a merely foreign note.
//   Foreign      — neither; penalised at the standard rate.
//
// The distinction matters because a note that belongs to the defining core of a
// *different* quality (e.g. a minor 7th heard over a diminished-triad template,
// which defines half-diminished) should hurt the wrong candidate more than an
// unrelated passing tone does.
enum class ExtraNoteCategory { Extension, Contradiction, Foreign };

// A contradiction (a note that definitively excludes a template quality, e.g. a
// major third over a diminished template) is penalised more severely than a merely
// foreign note.  Theory-grounded ordering: contradiction penalty > foreign penalty.
// Absolute magnitude is empirically tuned against the regression corpus.
static double kContradictionPenalty = 0.75;

// ── Template tone scoring ────────────────────────────────────────────────────
//
// Theory basis: root identity is the strongest harmonic signal (1.8×); the second
// template tone (bass-position third or fifth) carries chord colour (1.2×); remaining
// tones are structural but less individually identifying (1.0×).  The relative ordering
// (root > second > other) is theory-grounded; the exact ratios are empirically tuned.
//
// Caps prevent any single heavily-doubled note from dominating the score.
static double kRootToneFactor          = 1.8;   // [theory-grounded ordering, empirical value]
static double kSecondToneFactor        = 1.2;   // [theory-grounded ordering, empirical value]
static double kOtherToneFactor         = 1.0;   // baseline
static double kTemplateToneWeightCap   = 3.0;   // [empirical]
static double kExtraNoteWeightCap      = 2.0;   // [empirical]

// ── Extension and foreign-note scoring ──────────────────────────────────────
//
// Theory basis: 7ths are the most common and unambiguous colour extensions, so they
// earn the highest extension reward.  b13/aug5 intervals are enharmonically ambiguous
// and can resemble inversions of other chords, so they earn less.  Other extensions
// (9ths, 11ths, #11s) fall between these extremes.  The ordering is theory-grounded;
// absolute values are empirically tuned.
//
// kForeignPenalty < kContradictionPenalty: a note that merely doesn't fit the template
// is less damaging than one that actively excludes it.  [theory-grounded ordering]
static double kExtensionFactor7th      = 0.45;  // m7/M7: common colour tone [empirical]
static double kExtensionFactorFlat13   = 0.20;  // b13/#5: inversion-ambiguous [empirical]
static double kExtensionFactorDefault  = 0.35;  // 9th, 11th, etc.  [empirical]
static double kForeignPenalty          = 0.45;  // neither extension nor contradiction [empirical]

// ── TPC-based Sus4 vs minor disambiguation ───────────────────────────────────
//
// A note 3 semitones above the root is enharmonically Eb (minor third) or D# (#9).
// Theory basis: a flat spelling (Eb) signals minor-third intent and suppresses the
// Sus4 reading; a sharp spelling (D#) signals #9 intent and is compatible with Sus4.
// The asymmetry (0.10 vs 0.45) reflects that Eb-over-Sus4 is a strong contradiction
// signal while D#-over-Sus4 is a mild confirmation.  Both values are empirical.
static double kSus4FlatThirdFactor     = 0.10;  // Eb spelling → minor intent  [empirical]
static double kSus4SharpThirdFactor    = 0.45;  // D# spelling → #9 intent     [empirical]

// ── Template-specific structural penalties and bonuses ───────────────────────
//
// Each constant keeps a template family self-consistent.  The ordering of related
// values (e.g. Sus4Variant > Sus4Maj7 because a missing 7th is a bigger ambiguity
// than a missing 5th) is theory-grounded; absolute values are empirically tuned.
static double kDim7CharacteristicBonus = 0.75;  // fully-diminished fingerprint confirmed [empirical]
static double kNonBassPenalty          = 0.35;  // Min7/Sus4/HalfDim: prefer bass-root reading [empirical]
static double kSus4VariantMissing7th   = 0.70;  // Sus4b5/Sus4#5 without defining m7 [empirical]
static double kSus4Maj7MissingP5       = 0.50;  // Sus4+Maj7 without P5 anchor [empirical]
static double kSus4MissingFourth       = 0.70;  // Sus4 without defining P4 (interval 5) [empirical]
/// Minimum pcWeight for the defining P4 to be treated as a structural suspension
/// tone.  Below this, the Sus4 template is penalised even when the P4 is
/// technically present — passing or ornamental fourths routinely clear 0.20
/// (extensionThreshold) but rarely reach 0.50.
static double kSus4StructuralFourthThreshold = 0.50;
static double kDom7FlatFiveTpcPenalty  = 0.55;  // dom7b5: enharmonic ambiguity without Gb TPC [empirical]
static double kDom7FlatFiveMissing7th  = 0.50;  // dom7b5 without minor 7th: too ambiguous [empirical]
static double kPowerChord3PcPenalty    = 0.30;  // power chord with 3+ pcs: triadic reading preferred [empirical]
static double kBassSupportPresenceThreshold = 0.05;  // matches distinct-PC presence threshold

/// Minimum pcWeight for a seventh interval (min7 = +10, maj7 = +11) to register
/// as a chord seventh extension.  Seventh notes in lightly-voiced jazz chords
/// consistently appear in the 0.12–0.19 range (below the 0.20 general threshold)
/// so a separate, lower guard is needed.
/// Must be strictly above the max(0.1, weight) floor (0.1) applied in analyzeChord.
static double kSeventhThreshold        = 0.12;

/// Minimum pcWeight for all other chord extensions (9th, 11th, 13th, alterations).
/// Conservative at 0.20 so that brief ornamental notes in non-jazz contexts
/// (passing tones, neighbor notes) do not trigger false extension labels.
static double kExtensionThreshold      = 0.20;

// kScoreThresholdRatio moved to harmonicfunctionlayer.h (fn::kScoreThresholdRatio):
// the result-admission threshold is a function of post-signal scores, so it is a
// property of the competition pipeline, not the vertical scorer.

// ── Stage-5 fitter: former analyzeChord-local scoring shaping constants ──────────
// Relocated to file scope (from lambda/loop bodies) with unchanged values so the
// Stage-5 parameter-override mechanism can register their addresses at static-init
// (a function-local static is not initialized until its function first runs — too
// late for the startup-time override loader). Byte-identical: same literals, read
// exactly as before. See cowork_stage5_fitter_design.md D-6 + the Phase-0 manifest.
static double kWComplete = 0.50;                    ///< Iter-92 root-position complete-triad bonus (was chordanalyzer.cpp local)
static double kWCompletePresenceThreshold = 0.05;   ///< wComplete triad-tone presence bar (was the lambda-local kPresenceThreshold)
static double kComplexityEvidenceFloor = 0.5;       ///< Iter-74 FixA: template-complexity discount threshold AND additive floor (one shaping constant)
static double kAugThinEvidenceFactor = 0.5;         ///< Iter-78/79: augmented thin-evidence / bare-root halving factor (both *= sites)

// ── Stage-5 fitter: register the file-level scoring constants for the optional ───
// parameter-override mechanism. The registry stores each address; the override
// loader (params::loadAndApply) is the ONLY writer, and it runs only when a
// --param-override file is passed. No override loaded ⇒ every read below sees its
// literal initializer above ⇒ byte-identical. Registration runs at static-init
// because analyzeChord() (this TU) is odr-used by every analysis caller.
static const bool s_registerChordScoringParams = [] {
    namespace P = mu::composing::params;
    P::registerDouble("kContradictionPenalty",          &kContradictionPenalty);
    P::registerDouble("kRootToneFactor",                &kRootToneFactor);
    P::registerDouble("kSecondToneFactor",              &kSecondToneFactor);
    P::registerDouble("kOtherToneFactor",               &kOtherToneFactor);
    P::registerDouble("kTemplateToneWeightCap",         &kTemplateToneWeightCap);
    P::registerDouble("kExtraNoteWeightCap",            &kExtraNoteWeightCap);
    P::registerDouble("kExtensionFactor7th",            &kExtensionFactor7th);
    P::registerDouble("kExtensionFactorFlat13",         &kExtensionFactorFlat13);
    P::registerDouble("kExtensionFactorDefault",        &kExtensionFactorDefault);
    P::registerDouble("kForeignPenalty",                &kForeignPenalty);
    P::registerDouble("kSus4FlatThirdFactor",           &kSus4FlatThirdFactor);
    P::registerDouble("kSus4SharpThirdFactor",          &kSus4SharpThirdFactor);
    P::registerDouble("kDim7CharacteristicBonus",       &kDim7CharacteristicBonus);
    P::registerDouble("kNonBassPenalty",                &kNonBassPenalty);
    P::registerDouble("kSus4VariantMissing7th",         &kSus4VariantMissing7th);
    P::registerDouble("kSus4Maj7MissingP5",             &kSus4Maj7MissingP5);
    P::registerDouble("kSus4MissingFourth",             &kSus4MissingFourth);
    P::registerDouble("kSus4StructuralFourthThreshold", &kSus4StructuralFourthThreshold);
    P::registerDouble("kDom7FlatFiveTpcPenalty",        &kDom7FlatFiveTpcPenalty);
    P::registerDouble("kDom7FlatFiveMissing7th",        &kDom7FlatFiveMissing7th);
    P::registerDouble("kPowerChord3PcPenalty",          &kPowerChord3PcPenalty);
    P::registerDouble("kBassSupportPresenceThreshold",  &kBassSupportPresenceThreshold);
    P::registerDouble("kSeventhThreshold",              &kSeventhThreshold);
    P::registerDouble("kExtensionThreshold",            &kExtensionThreshold);
    P::registerDouble("kWComplete",                     &kWComplete);
    P::registerDouble("kWCompletePresenceThreshold",    &kWCompletePresenceThreshold);
    P::registerDouble("kComplexityEvidenceFloor",       &kComplexityEvidenceFloor);
    P::registerDouble("kAugThinEvidenceFactor",         &kAugThinEvidenceFactor);
    return true;
}();

/// Classify a non-template interval relative to a chord quality.
///
/// Pure classifier: takes only the interval (already normalised, 0–11) and the
/// quality; assumes the most permissive interpretation for ambiguous cases.
/// Specifically:
///   - Major  + m3 (rel==3): defaults to Extension (assumes M3 also sounding → #9).
///     Becomes Contradiction when M3 is absent — caller must apply that override.
///   - Sus4   + m3 (rel==3): defaults to Extension (assumes P4 also sounding → #9).
///     Becomes Contradiction when P4 is absent — caller must apply that override.
///
/// All other context-sensitive corrections (TPC-based factor adjustments, etc.)
/// are likewise the caller's responsibility.
ExtraNoteCategory categorizeExtraNote(int rel, ChordQuality quality)
{
    // Quality-specific contradictions: intervals that definitively identify a
    // different quality.  Context-dependent cases (Major/m3, Sus4/m3) are handled
    // in the caller.
    switch (quality) {
    case ChordQuality::Minor:
        if (rel == 4)  return ExtraNoteCategory::Contradiction; // M3  → not minor
        break;
    case ChordQuality::Suspended4:
        if (rel == 4)  return ExtraNoteCategory::Contradiction; // M3  → not sus4
        // m3 defaults to Extension; Contradiction when P4 absent — caller checks.
        break;
    case ChordQuality::Suspended2:
        if (rel == 3)  return ExtraNoteCategory::Contradiction; // m3  → not sus2
        if (rel == 4)  return ExtraNoteCategory::Contradiction; // M3  → not sus2
        break;
    case ChordQuality::Diminished:
        if (rel == 4)  return ExtraNoteCategory::Contradiction; // M3  → not diminished
        if (rel == 7)  return ExtraNoteCategory::Contradiction; // P5  → not diminished (requires ♭5) // BUG-10
        if (rel == 10) return ExtraNoteCategory::Contradiction; // m7  → half-diminished
        if (rel == 11) return ExtraNoteCategory::Contradiction; // M7  → not diminished
        break;
    case ChordQuality::HalfDiminished:
        if (rel == 4)  return ExtraNoteCategory::Contradiction; // M3  → not half-dim
        if (rel == 9)  return ExtraNoteCategory::Contradiction; // dim7 → fully diminished
        if (rel == 11) return ExtraNoteCategory::Contradiction; // M7  → not half-dim
        break;
    default:
        break;
    }

    // Neutral colour/extension intervals: valid additions for most qualities.
    switch (rel) {
    case 1:  // b9
    case 2:  // 9
    case 3:  // #9 (dual-use with minor 3rd; context overrides handled in caller)
    case 5:  // 11
    case 6:  // #11 / b5
    case 8:  // b13 / #5
    case 9:  // 13 / 6
    case 10: // minor 7
    case 11: // major 7
        return ExtraNoteCategory::Extension;
    default:
        return ExtraNoteCategory::Foreign;
    }
}


/// Compute all extension and alteration flags from a pitch-class weight histogram,
/// given the best root pitch class and quality.
struct ExtensionFlags {
    bool hasMinorSeventh    = false;
    bool hasMajorSeventh    = false;
    bool hasDiminishedSeventh = false;
    bool hasAddedSixth      = false;
    bool hasNinth           = false;
    bool hasNinthNatural    = false;
    bool hasNinthFlat       = false;
    bool hasNinthSharp      = false;
    bool hasEleventh        = false;
    bool hasEleventhSharp   = false;
    bool hasThirteenth      = false;
    bool hasThirteenthFlat  = false;
    bool hasThirteenthSharp = false;
    bool hasSharpFifth      = false;
    bool hasFlatFifth       = false;
    bool isSixNine          = false;
};

ExtensionFlags detectExtensions(const std::array<double, 12>& pcWeight,
                                int rootPc,
                                ChordQuality quality,
                                const std::array<int, 12>& tpcForPc,
                                int rootTpc,
                                double extThreshold = kExtensionThreshold)
{
    auto w = [&](int semitones) -> double {
        return pcWeight[static_cast<size_t>((rootPc + semitones) % 12)];
    };

    ExtensionFlags f;

    const bool rawMin7  = w(10) > kSeventhThreshold;
    const bool rawMaj7  = w(11) > kSeventhThreshold;
    const bool rawDim7  = (quality == ChordQuality::Diminished) && (w(9) > extThreshold);

    // For HalfDiminished the minor 7th is structural, not an "added" extension.
    // Also suppress if pitch class 10 is spelled as A# (#13) rather than Bb (min7).
    {
        const int pc10 = static_cast<size_t>((rootPc + 10) % 12);
        const int tpc10 = tpcForPc[static_cast<size_t>(pc10)];
        const bool isSharp13Spelling = (rootTpc >= 0 && tpc10 >= 0)
                                       && (tpc10 - rootTpc == 10);
        f.hasMinorSeventh = rawMin7 && !rawMaj7
                            && quality != ChordQuality::HalfDiminished
                            && !isSharp13Spelling;
    }
    f.hasMajorSeventh     = rawMaj7;
    f.hasDiminishedSeventh = rawDim7;

    f.hasAddedSixth = w(9) > extThreshold && !rawMin7 && !rawMaj7
                      && quality != ChordQuality::Diminished;

    f.hasNinthNatural = w(2) > extThreshold;
    f.hasNinthFlat    = w(1) > extThreshold;
    // Interval 3 is the minor 3rd in minor/diminished templates — exclude it.
    // For Major quality, also require a major 3rd (interval 4) to be present:
    // without it the note at interval 3 is the minor 3rd of a minor chord, not
    // a #9 (e.g. {A,C,E} is Am, not Aadd#9).  Suspended chords have no major
    // 3rd by definition, so the requirement is skipped for them.
    f.hasNinthSharp   = w(3) > extThreshold
                        && (quality != ChordQuality::Major || w(4) > extThreshold)
                        && quality != ChordQuality::Minor
                        && quality != ChordQuality::Diminished
                        && quality != ChordQuality::HalfDiminished;
    f.hasNinth        = f.hasNinthNatural || f.hasNinthFlat || f.hasNinthSharp;

    f.hasEleventh = w(5) > extThreshold;  // P4: stays at general threshold

    const bool hasSeventh = rawMin7 || rawMaj7 || rawDim7
                            || f.hasEleventh || f.hasNinthNatural;
    f.hasThirteenth = w(9) > extThreshold && hasSeventh;
    // A# (#13) vs Bb (min7): same pitch class, distinguished by TPC.
    // TPC delta from root: min7 = -2, aug6 (#13) = +10.
    {
        const int pc10 = static_cast<size_t>((rootPc + 10) % 12);
        const int tpc10 = tpcForPc[static_cast<size_t>(pc10)];
        const bool isSharp13Spelling = (rootTpc >= 0 && tpc10 >= 0)
                                       && (tpc10 - rootTpc == 10);
        f.hasThirteenthSharp = w(10) > extThreshold && isSharp13Spelling
                               && quality != ChordQuality::Diminished;
    }

    // Natural 5th presence distinguishes #5 (no natural 5th) from b13 (natural 5th
    // also present).  For Augmented quality the #5 is structural, not an extension.
    const bool naturalFifthPresent = (quality != ChordQuality::Augmented) && (w(7) > extThreshold);

    // pc+6: distinguish b5 (flat Gb spelling, no natural 5th) from #11 (sharp F# spelling
    // or natural 5th also present).  Compute first so hasFlatFifth is available for
    // the fifthSlotFilled check on pc+8 below.
    const bool rawFlatFifth = w(6) > extThreshold
                              && quality != ChordQuality::Diminished
                              && quality != ChordQuality::HalfDiminished;
    {
        const int pc6  = (rootPc + 6) % 12;
        const int tpc6 = tpcForPc[static_cast<size_t>(pc6)];
        // Positive TPC delta from root = sharp direction (F# from C: 21-15=+6).
        // Natural 5th present → always #11.  Sharp spelling → #11.  Otherwise b5.
        const bool tpcSpellsAsSharp = (rootTpc >= 0 && tpc6 >= 0) && (tpc6 - rootTpc > 0);
        const bool preferSharp11    = rawFlatFifth && (naturalFifthPresent || tpcSpellsAsSharp);
        f.hasFlatFifth = rawFlatFifth && !preferSharp11;
    }
    // Suppress #11 flag when treating pc+6 as b5 to avoid double-counting.
    // Also suppress for HalfDiminished: the b5 is structural there (rawFlatFifth
    // is blocked above), so hasFlatFifth is always false for half-dim even though
    // the note at +6 is the chord's own diminished fifth, not an added #11.
    f.hasEleventhSharp = w(6) > 0.3 && !f.hasFlatFifth
                         && quality != ChordQuality::HalfDiminished;

    // pc+8: flat-13th when a "fifth slot" is filled (natural 5th or flat 5th present);
    // augmented-5th (#5) otherwise.  When a b5 (Gb) already occupies the fifth slot,
    // Ab functions as b13 rather than #5 — consistent with how the catalog annotates this interval.
    //
    // Special case for Minor quality: the b6 interval (pc+8 spelled as Ab, TPC < rootTpc)
    // is the natural b13 of the minor scale.  Treat it as b13 even without a natural 5th,
    // as long as the TPC spelling confirms a flat direction (Ab, not G#).
    const int pc8  = (rootPc + 8) % 12;
    const int tpc8 = tpcForPc[static_cast<size_t>(pc8)];
    const bool tpc8SpellsAsFlat = (rootTpc >= 0 && tpc8 >= 0) && (tpc8 - rootTpc < 0);
    const bool fifthSlotFilled = naturalFifthPresent || f.hasFlatFifth;
    const bool fifthSlotOrMinorFlat6 = fifthSlotFilled
                                       || (quality == ChordQuality::Minor && tpc8SpellsAsFlat);
    f.hasSharpFifth     = w(8) > extThreshold && !fifthSlotOrMinorFlat6;
    // Allow b13 without a 7th for Minor quality only when the perfect 5th is also present
    // (e.g. "Cmaddb13" = {C,Eb,G,Ab}).  Without the 5th, {root,m3,b6} is more parsimoniously
    // a first-inversion major triad (e.g. {G,Bb,Eb} = Eb/G), so we suppress the b13 label.
    f.hasThirteenthFlat = w(8) > 0.3 && fifthSlotOrMinorFlat6
                          && (hasSeventh || (quality == ChordQuality::Minor && w(7) > 0.2));

    f.isSixNine = f.hasAddedSixth && f.hasNinthNatural && !rawMin7 && !rawMaj7;

    return f;
}

/// Map detected ExtensionFlags (+ the omitsThird flag buildChordResult derives on the
/// Sus->Major upgrade) to the ChordIdentity.extensions bitmask. The single source of the
/// flag->bit mapping, shared by buildChordResult and the exposed deriveChordExtensions.
uint32_t extensionBits(const ExtensionFlags& ext, bool omitsThird)
{
    uint32_t e = 0;
    if (ext.hasMinorSeventh)      setExtension(e, Extension::MinorSeventh);
    if (ext.hasMajorSeventh)      setExtension(e, Extension::MajorSeventh);
    if (ext.hasDiminishedSeventh) setExtension(e, Extension::DiminishedSeventh);
    if (ext.hasAddedSixth)        setExtension(e, Extension::AddedSixth);
    if (ext.hasNinthNatural)      setExtension(e, Extension::NaturalNinth);
    if (ext.hasNinthFlat)         setExtension(e, Extension::FlatNinth);
    if (ext.hasNinthSharp)        setExtension(e, Extension::SharpNinth);
    if (ext.hasEleventh)          setExtension(e, Extension::NaturalEleventh);
    if (ext.hasEleventhSharp)     setExtension(e, Extension::SharpEleventh);
    if (ext.hasThirteenth)        setExtension(e, Extension::NaturalThirteenth);
    if (ext.hasThirteenthFlat)    setExtension(e, Extension::FlatThirteenth);
    if (ext.hasThirteenthSharp)   setExtension(e, Extension::SharpThirteenth);
    if (ext.hasSharpFifth)        setExtension(e, Extension::SharpFifth);
    if (ext.hasFlatFifth)         setExtension(e, Extension::FlatFifth);
    if (ext.isSixNine)            setExtension(e, Extension::SixNine);
    if (omitsThird)               setExtension(e, Extension::OmitsThird);
    return e;
}

// ── Chord template definition ──────────────────────────────────────────────

/// A chord template: quality, intervals from root (semitones), and expected
/// TPC (circle-of-fifths) deltas for each interval.
///
/// TPC deltas encode the expected circle-of-fifths distance per interval:
///   P5=+1, M3=+4, m3=−3, P4=−1, A5=+8, d5=−6, m7=−2, M2=+2, A4=+6.
/// Used to score enharmonic-spelling consistency when TPC data is available.
struct TemplateDef {
    ChordQuality quality;
    std::vector<int> intervals;
    std::vector<int> tpcDeltas;  // parallel to intervals; tpcDeltas[0] is always 0 (root)
};

/// Build a TemplateDef's runtime `intervals` vector from the canonical
/// kTemplateIntervals table (chordanalyzer.h), dropping the trailing -1 unused
/// slots. This makes kTemplateIntervals the SINGLE source of per-template interval
/// data — both the `templates` array below and Gate R's kMasks (harmonicfunctionlayer.cpp,
/// `= makeTemplateMasks()`) now consume it, so the two can no longer drift (audit Q1.3).
/// Each `templates` row keeps its `quality` and `tpcDeltas` inline (template-scoring data,
/// not the shared interval set). Row order is load-bearing: index == template index.
std::vector<int> templateIntervalsVec(std::size_t t)
{
    std::vector<int> intervals;
    intervals.reserve(kMaxTemplateTones);
    for (int interval : kTemplateIntervals[t]) {
        if (interval >= 0) {
            intervals.push_back(interval);
        }
    }
    return intervals;
}

// ── Per-candidate scoring helpers ──────────────────────────────────────────
//
// The analyzeChord scoring loop calls one function per concern.  Each helper
// returns a signed score delta and is independently readable and testable.

/// Weighted sum of the template tones' presence in the input.
/// Absent template tones contribute zero (their pcWeight is near zero).
double scoreTemplateTones(const TemplateDef& tpl, int rootPc,
                          const std::array<double, 12>& pcWeight)
{
    double score = 0.0;
    for (size_t i = 0; i < tpl.intervals.size(); ++i) {
        const int chordPc = (rootPc + tpl.intervals[i]) % 12;
        const double w    = pcWeight[static_cast<size_t>(chordPc)];
        const double factor = (i == 0) ? kRootToneFactor
                            : (i == 1) ? kSecondToneFactor
                                       : kOtherToneFactor;
        score += factor * std::min(w, kTemplateToneWeightCap);
    }
    return score;
}

/// Signed contribution of all non-template pitch classes.
/// Positive for extensions, negative for contradictions and foreign notes.
///
/// Also applies two context-sensitive classification overrides that the pure
/// categorizeExtraNote classifier cannot handle on its own:
///   - Major/m3:  Contradiction when M3 is absent (not a #9 — it's a real minor 3rd).
///   - Sus4/m3:   Contradiction when P4 is absent (no sus4 sound without the defining P4).
/// And a TPC-based sus4 vs minor soft factor adjustment for the #9/m3 ambiguity.
double scoreExtraNotes(const TemplateDef& tpl, int rootPc,
                       const std::array<double, 12>& pcWeight,
                       const std::array<int, 12>& tpcForPc)
{
    // Standard Sus4 = Sus4 with P5 present (intervals[2]==7).
    // Only standard Sus4 templates use the TPC sus4/minor disambiguation.
    // Sus4-variant templates (altered P5: Sus4b5, Sus4#5) legitimately use Eb as a
    // #9 colour tone and should not have their extension factor reduced.
    const bool sus4Standard = (tpl.quality == ChordQuality::Suspended4
                               && (tpl.intervals.size() < 3 || tpl.intervals[2] == 7));

    double score = 0.0;
    for (int pc = 0; pc < 12; ++pc) {
        const double w = pcWeight[static_cast<size_t>(pc)];
        if (w < 0.01) {
            continue;  // not sounding — contributes nothing regardless of classification
        }

        bool inTemplate = false;
        for (int interval : tpl.intervals) {
            if (((rootPc + interval) % 12) == pc) { inTemplate = true; break; }
        }
        if (inTemplate) {
            continue;
        }

        const int rel = normalizePc(pc - rootPc);
        ExtraNoteCategory cat = categorizeExtraNote(rel, tpl.quality);

        // Context-sensitive classification overrides (cannot be done in the pure classifier).
        if (tpl.quality == ChordQuality::Major && rel == 3) {
            // m3 is a #9 colour tone only when M3 is also sounding.
            if (pcWeight[static_cast<size_t>((rootPc + 4) % 12)] < 0.1) {
                cat = ExtraNoteCategory::Contradiction;
            }
        }
        if (tpl.quality == ChordQuality::Suspended4 && rel == 3) {
            // m3 is a #9 colour tone only when P4 (the defining Sus4 interval) is present.
            if (pcWeight[static_cast<size_t>(normalizePc(rootPc + 5))] < 0.1) {
                cat = ExtraNoteCategory::Contradiction;
            }
        }

        if (cat == ExtraNoteCategory::Extension) {
            double extensionFactor = (rel == 10 || rel == 11) ? kExtensionFactor7th
                                   : (rel == 8)               ? kExtensionFactorFlat13
                                                              : kExtensionFactorDefault;

            // TPC-based sus4 vs minor disambiguation for the minor-3rd / #9 position.
            // Eb spelling (TPC = rootTpc − 3) → likely a real minor third, suppress Sus4.
            // D# spelling (TPC = rootTpc + 9) → #9 intent confirmed, boost Sus4 slightly.
            if (sus4Standard && rel == 3) {
                const int rootTpc = tpcForPc[static_cast<size_t>(rootPc)];
                const int noteTpc = tpcForPc[static_cast<size_t>(pc)];
                if (rootTpc >= 0 && noteTpc >= 0) {
                    if (noteTpc == rootTpc - 3) {
                        extensionFactor = kSus4FlatThirdFactor;
                    } else if (noteTpc == rootTpc + 9) {
                        extensionFactor = kSus4SharpThirdFactor;
                    }
                }
            }

            score += extensionFactor * std::min(w, kExtraNoteWeightCap);
        } else if (cat == ExtraNoteCategory::Contradiction) {
            score -= kContradictionPenalty * std::min(w, kExtraNoteWeightCap);
        } else {
            score -= kForeignPenalty * std::min(w, kExtraNoteWeightCap);
        }
    }
    return score;
}

/// Bonus for Diminished templates when a non-diatonic dim7 interval is present.
/// The dim7 (9 semitones from root) fingerprints the true diminished root: when it is
/// non-diatonic in the current key it confirms this root over chord inversions.
///
/// "Diatonic in the current key" is a question about the key's COLLECTION, not its tonic, so
/// the term takes only \p signatureMask — the notated signature's own diatonic pitch classes
/// (`diatonicMaskFromFifths`). It takes no tonic and no mode scale, which is what makes the
/// tonic-independence structural rather than a cancellation a future mode-table edit could
/// silently break — the way OI-168 was born. See docs/scoring_model.md §4.
double dim7CharacteristicBonus(const TemplateDef& tpl, int rootPc,
                               const std::array<double, 12>& pcWeight,
                               uint16_t signatureMask,
                               double extThreshold = kExtensionThreshold)
{
    if (tpl.quality != ChordQuality::Diminished) {
        return 0.0;
    }
    const int dim7Pc = (rootPc + 9) % 12;
    if (pcWeight[static_cast<size_t>(dim7Pc)] <= extThreshold) {
        return 0.0;
    }
    // The dim7 characteristic only applies to a fully-formed diminished triad.
    // Without root, minor-third AND diminished-fifth all sounding, the root+9
    // tone is not functioning as a diminished seventh — it belongs to another
    // harmony (e.g. {C#,E,F#,A#} is F#7, not an incomplete C#°7 missing its G).
    // Requiring the complete triad leaves genuine vii°7 / chromatic °7 chords
    // (which always voice root + b3 + b5) untouched, while suppressing the
    // spurious bonus that let an incomplete °7 outscore a perfect dominant-7th.
    const int b3Pc = (rootPc + 3) % 12;
    const int b5Pc = (rootPc + 6) % 12;
    if (pcWeight[static_cast<size_t>(rootPc)] <= extThreshold
        || pcWeight[static_cast<size_t>(b3Pc)] <= extThreshold
        || pcWeight[static_cast<size_t>(b5Pc)] <= extThreshold) {
        return 0.0;
    }
    if (pcInMask(signatureMask, dim7Pc)) {
        return 0.0;  // diatonic — no bonus
    }
    return kDim7CharacteristicBonus;
}

/// TPC match counts for non-root template tones.
/// Used by nonBassAdjustment and tpcConsistencyBonus to avoid duplicating the
/// same iteration pattern.
struct TpcMatchCounts {
    int present = 0;  ///< Non-root template tones that have TPC data.
    int matched = 0;  ///< Of those, tones whose TPC equals the expected value.
};

/// Count TPC matches for non-root intervals of \p tpl rooted at \p rootPc.
/// Returns all-zero when the root has no TPC data (cannot compute expected values).
TpcMatchCounts countTpcMatches(const TemplateDef& tpl, int rootPc,
                                const std::array<int, 12>& tpcForPc)
{
    const int rootTpc = tpcForPc[static_cast<size_t>(rootPc)];
    if (rootTpc < 0) {
        return {};
    }
    TpcMatchCounts counts;
    for (size_t i = 1; i < tpl.intervals.size(); ++i) {
        const int chordPc   = (rootPc + tpl.intervals[i]) % 12;
        const int actualTpc = tpcForPc[static_cast<size_t>(chordPc)];
        if (actualTpc >= 0) {
            ++counts.present;
            if (actualTpc == rootTpc + tpl.tpcDeltas[i]) {
                ++counts.matched;
            }
        }
    }
    return counts;
}

/// Net score adjustment for templates that carry a non-bass penalty, with a
/// TPC-spelling waiver when that evidence is authoritative.
///
/// Minor7, any 4-note Sus4, and HalfDim templates are penalised when their root is
/// not the bass note: re-labelling from the bass is almost always preferable
/// (e.g. Am7 from non-bass root A is better labelled C6 or C/E).
///
/// The penalty is waived when every non-root template tone that has TPC data is
/// spelled exactly right for this root/quality — the composer's enharmonic spelling
/// then overrides the bass-root preference.
///
/// Exception: Sus4-variant templates (Sus4b5/Sus4♯5) are excluded from the waiver.
/// Their altered fifth makes TPC evidence less discriminating from non-bass roots
/// (e.g. {C,Db,F,G} should label as Csusb9, not G7susb5/C).
double nonBassAdjustment(const TemplateDef& tpl, int rootPc, int bassPc,
                         const std::array<int, 12>& tpcForPc)
{
    const bool isSus4Any = (tpl.quality == ChordQuality::Suspended4
                            && tpl.intervals.size() == 4);
    const bool isMinor4  = (tpl.quality == ChordQuality::Minor
                            && tpl.intervals.size() == 4);
    const bool isHalfDim = (tpl.quality == ChordQuality::HalfDiminished);

    if (!(isSus4Any || isMinor4 || isHalfDim) || rootPc == bassPc) {
        return 0.0;  // penalty does not apply to this template or this root
    }

    const bool isSus4Variant = (tpl.quality == ChordQuality::Suspended4
                                && tpl.intervals.size() == 4
                                && tpl.intervals[2] != 7);

    const TpcMatchCounts tpc = countTpcMatches(tpl, rootPc, tpcForPc);
    const bool waiverApplies = (!isSus4Variant
                                && tpc.present > 0
                                && tpc.matched == tpc.present);
    return waiverApplies ? 0.0 : -kNonBassPenalty;
}

/// Penalties for structural notes that are absent or enharmonically ambiguous.
///
/// Each penalty keeps a template family self-consistent: the template scores well
/// only when its own characteristic intervals are present and correctly spelled.
double structuralPenalties(const TemplateDef& tpl, int rootPc,
                           const std::array<double, 12>& pcWeight,
                           const std::array<int, 12>& tpcForPc,
                           int distinctPcs,
                           double extThreshold = kExtensionThreshold)
{
    double score = 0.0;

    // Sus4 templates (except Sus4b5): the P4 is the defining suspension tone.
    // Penalise when it is absent or too weak to sustain a suspension reading.
    // Without a detectable fourth the chord sounds augmented or altered, not suspended.
    //
    // Sus4b5 {0,5,6,10} (intervals[2]==6) is excluded: in that variant the tritone (b5)
    // is the identifying characteristic.  Sus4b5 from C legitimately wins for chords like
    // {C,F#,Bb,D} (Lydian dominant / C7♭5 spelling) where P4=F is genuinely absent.
    // Applying the penalty there pushes the root away from C toward D, which is incorrect
    // per corpus ground truth.  Sus4♯5 and standard Sus4 are still penalised.
    const bool sus4HasPerfectFourth = (tpl.quality == ChordQuality::Suspended4)
                                      && std::any_of(tpl.intervals.begin(), tpl.intervals.end(),
                                                     [](int i) { return i == 5; });
    const bool isSus4FlatFive = (tpl.quality == ChordQuality::Suspended4)
                                && tpl.intervals.size() >= 3
                                && tpl.intervals[2] == 6;
    if (sus4HasPerfectFourth && !isSus4FlatFive) {
        const int fourthPc = static_cast<int>((rootPc + 5) % 12);
        if (pcWeight[static_cast<size_t>(fourthPc)] < kSus4StructuralFourthThreshold) {
            score -= kSus4MissingFourth;
        }
    }

    // Sus4-variant (Sus4b5 / Sus4♯5): penalise when the minor-7th is absent.
    // Without it, {root, P4, b5/♯5} is ambiguous with simpler chord inversions.
    const bool isSus4Variant = (tpl.quality == ChordQuality::Suspended4
                                && tpl.intervals.size() == 4
                                && tpl.intervals[2] != 7);
    if (isSus4Variant) {
        const int seventhPc = (rootPc + tpl.intervals[3]) % 12;
        if (pcWeight[static_cast<size_t>(seventhPc)] < 0.05) {
            score -= kSus4VariantMissing7th;
        }
    }

    // Sus4+Maj7: penalise when the perfect fifth is absent.
    // Without it, {root, P4, Maj7} is ambiguous with simpler chord inversions.
    const bool isSus4Maj7 = (tpl.quality == ChordQuality::Suspended4
                              && tpl.intervals.size() == 4
                              && tpl.intervals[3] == 11);
    if (isSus4Maj7) {
        const int fifthPc = (rootPc + 7) % 12;
        if (pcWeight[static_cast<size_t>(fifthPc)] < 0.05) {
            score -= kSus4Maj7MissingP5;
        }
    }

    // Dom7b5: the tritone (interval 6) is enharmonically ambiguous between
    // dom7b5 (Gb, TPC delta −6) and Lydian-dominant / augmented (F#, TPC delta +6).
    // Penalise unless TPC data confirms the Gb (flat-5th) spelling.
    // Also penalise when the minor 7th is absent: {root, M3, b5} alone is ambiguous.
    const bool isDom7FlatFive = (tpl.quality == ChordQuality::Major
                                  && tpl.intervals.size() == 4
                                  && tpl.intervals[2] == 6);
    if (isDom7FlatFive) {
        const int tritonePc  = (rootPc + 6) % 12;
        const int rootTpcNow = tpcForPc[static_cast<size_t>(rootPc)];
        const int tritTpcNow = tpcForPc[static_cast<size_t>(tritonePc)];
        const bool flatFiveConfirmed = (rootTpcNow >= 0 && tritTpcNow >= 0
                                        && tritTpcNow - rootTpcNow == -6);
        if (!flatFiveConfirmed) {
            score -= kDom7FlatFiveTpcPenalty;
        }
        const int minorSeventhPc = (rootPc + tpl.intervals[3]) % 12;
        if (pcWeight[static_cast<size_t>(minorSeventhPc)] < 0.05) {
            score -= kDom7FlatFiveMissing7th;
        }
    }

    // Power chord: with 3+ distinct pitch classes a triadic interpretation is
    // almost always preferable.
    if (tpl.quality == ChordQuality::Power && distinctPcs >= 3) {
        score -= kPowerChord3PcPenalty;
    }

    return score;
}

/// Per-tone TPC spelling-consistency bonus.
/// For each non-root template tone whose actual TPC matches the expected TPC
/// for this root and quality, add prefs.tpcConsistencyBonusPerTone.
double tpcConsistencyBonus(const TemplateDef& tpl, int rootPc,
                           const std::array<int, 12>& tpcForPc,
                           const ChordAnalyzerPreferences& prefs)
{
    const TpcMatchCounts tpc = countTpcMatches(tpl, rootPc, tpcForPc);
    return tpc.matched * prefs.tpcConsistencyBonusPerTone;
}

double bassRootBonusMultiplier(const TemplateDef& tpl,
                               int rootPc,
                               const std::array<double, 12>& pcWeight,
                               const ChordAnalyzerPreferences& prefs)
{
    const auto hasPitchClass = [&](int pc) {
        return pcWeight[static_cast<size_t>(normalizePc(pc))] > kBassSupportPresenceThreshold;
    };

    const bool templateHasThird = std::any_of(tpl.intervals.begin(), tpl.intervals.end(),
                                              [](int interval) {
        return interval == 3 || interval == 4;
    });
    const bool hasMatchingTemplateThird = std::any_of(tpl.intervals.begin(), tpl.intervals.end(),
                                                      [&](int interval) {
        return (interval == 3 || interval == 4)
               && hasPitchClass(rootPc + interval);
    });

    const bool hasTemplateFifth = std::any_of(tpl.intervals.begin(), tpl.intervals.end(),
                                              [&](int interval) {
        return (interval == 6 || interval == 7 || interval == 8)
               && hasPitchClass(rootPc + interval);
    });
    const bool isBareSuspensionTriad = ((tpl.quality == ChordQuality::Suspended2
                                         || tpl.quality == ChordQuality::Suspended4)
                                        && tpl.intervals.size() == 3);

    if (hasTemplateFifth) {
        if (hasMatchingTemplateThird) {
            return 1.0;
        }

        if (!templateHasThird) {
            // Bare sus triads should not outrank omitted-third triads purely because
            // the suspension template receives a full bass-root bonus.
            return isBareSuspensionTriad ? prefs.bassRootThirdOnlyMultiplier : 1.0;
        }

        // Root plus fifth is materially stronger than bass alone, even when the third
        // is omitted from the local sonority.
        return prefs.bassRootThirdOnlyMultiplier;
    }

    if (hasPitchClass(rootPc + 3) || hasPitchClass(rootPc + 4)) {
        return prefs.bassRootThirdOnlyMultiplier;
    }

    return prefs.bassRootAloneMultiplier;
}

bool templateHasMatchingThird(const TemplateDef& tpl,
                              int rootPc,
                              const std::array<double, 12>& pcWeight)
{
    return std::any_of(tpl.intervals.begin(), tpl.intervals.end(),
                       [&](int interval) {
        return (interval == 3 || interval == 4)
               && pcWeight[static_cast<size_t>(normalizePc(rootPc + interval))] > 0.05;
    });
}

bool templateHasMatchingFifth(const TemplateDef& tpl,
                              int rootPc,
                              const std::array<double, 12>& pcWeight)
{
    return std::any_of(tpl.intervals.begin(), tpl.intervals.end(),
                       [&](int interval) {
        return (interval == 6 || interval == 7 || interval == 8)
               && pcWeight[static_cast<size_t>(normalizePc(rootPc + interval))] > 0.05;
    });
}

bool qualifiesForCompleteTriadInversionBonus(const TemplateDef& tpl,
                                             int rootPc,
                                             int bassPc,
                                             const std::array<double, 12>& pcWeight,
                                             int distinctPcs)
{
    if (distinctPcs != 3 || rootPc == bassPc) {
        return false;
    }

    // Extended in Iter 46 to include Augmented and HalfDiminished: these quality
    // types were systematically excluded from inversion bonuses, causing correct
    // inverted readings to fall below the results[] threshold.
    const bool supportedQuality = (tpl.quality == ChordQuality::Major
                                   || tpl.quality == ChordQuality::Minor
                                   || tpl.quality == ChordQuality::Diminished
                                   || tpl.quality == ChordQuality::Augmented
                                   || tpl.quality == ChordQuality::HalfDiminished);
    if (!supportedQuality) {
        return false;
    }

    return templateHasMatchingThird(tpl, rootPc, pcWeight)
           && templateHasMatchingFifth(tpl, rootPc, pcWeight);
}

bool supportsContextualInversionBonuses(const TemplateDef& tpl,
                                        int rootPc,
                                        int bassPc,
                                        const std::array<double, 12>& pcWeight)
{
    // Extended in Iter 46 to include Augmented and HalfDiminished: these quality
    // types were systematically excluded from inversion bonuses, causing correct
    // inverted readings (e.g. C+/E, Yø7/X) to fall below the results[] threshold.
    // They now compete on equal terms with Major/Minor inversions.
    const bool isInvertedSupportedQuality = (rootPc != bassPc)
                                  && (tpl.quality == ChordQuality::Major
                                      || tpl.quality == ChordQuality::Minor
                                      || tpl.quality == ChordQuality::Augmented
                                      || tpl.quality == ChordQuality::HalfDiminished);
    return isInvertedSupportedQuality && templateHasMatchingThird(tpl, rootPc, pcWeight);
}

double appliedBassRootBonus(const TemplateDef& tpl,
                            int rootPc,
                            int bassPc,
                            const std::array<double, 12>& pcWeight,
                            const ChordAnalyzerPreferences& prefs)
{
    if (rootPc != bassPc) {
        return 0.0;
    }

    return prefs.bassNoteRootBonus * bassRootBonusMultiplier(tpl, rootPc, pcWeight, prefs);
}


// Diatonic-root preference — the one bass-independent KEY fact the oracle folds into
// basisIndep. Genuinely vertical/key as of Stage 3.3.
//
// HISTORY — until Stage 3.3 two helpers (bassIndependentContextualBonuses /
// bassDependentContextualBonuses) folded FIVE progression signals into basisIndep /
// basisDep as documented oracle temporal debt (chordanalyzer.h TODO, audit Finding 1):
// resolutionBonus + the four §4.1b inversion bonuses (stepwise-from-prev, lookahead,
// sameRoot, completeTriad). Stage 3.3 migrated all five into the competition pipeline
// (fn::resolutionEdgeBonus + fn::inversionContextBonus, folded into basisIndep / basisDep
// there, before the cf × af multiply — same arithmetic positions). rootContinuityBonus had
// already moved in the E2d redesign. The oracle is now genuinely vertical: it adds NO
// progression signal. The vertical inversion-eligibility predicates
// (supportsContextualInversionBonuses / qualifiesForCompleteTriadInversionBonus) stay here
// (they are pitch facts) and are published as per-cell flags on the ScoringSnapshot so the
// pipeline can gate the migrated bonuses. See docs/scoring_model.md §4 / §11.
//
// KEY CONTEXT — the COLLECTION, never the tonic. "Does this root belong to the key?" is a
// question about the key signature's diatonic pitch-class set, and the term takes exactly that:
// \p signatureMask, from `diatonicMaskFromFifths` ("depends ONLY on the notated signature, never
// a resolved mode"). It takes no tonic and no mode scale — so the property cannot lapse when a
// mode is added to the table, which is precisely how OI-168 arose: the previous form tested
// membership in { (keyTonicPc + scale[i]) mod 12 }, which equals the signature's collection only
// while every mode's tonic offset matches its diatonic parent's — false for Altered and
// AlteredDomBB7, whose set is the collection transposed up a semitone.
double diatonicRootContribution(int rootPc, uint16_t signatureMask,
                                const ChordAnalyzerPreferences& prefs)
{
    if (pcInMask(signatureMask, rootPc)) {
        return prefs.diatonicRootBonus;
    }
    return 0.0;
}

} // namespace

ChordAnalysisResult buildChordResult(
    const RawCandidate&             rc,
    const BuildChordResultContext&  ctx,
    const ChordAnalyzerPreferences& prefs)
{
    int rootPc    = rc.rootPc;
    ChordQuality quality = rc.quality;

    // ── Post-scoring quality normalisation ──────────────────────────────────
    //
    // The following steps refine the reported quality AFTER ranking is complete.
    // They do NOT affect rc.score (which reflects the raw template match); they
    // ensure ChordAnalysisResult::quality carries the most accurate musical label.
    //
    // There are three cases:
    //   1. Augmented root correction  — symmetric triad; bass selects the root
    //                                   when TPC data is absent.
    //   2. Sus2 → Sus4 upgrade        — when P4 is sounding, Sus4 is more specific.
    //   3. Sus → Major (omitsThird)   — when Maj7 is present but no 3rd, the catalog
    //                                   labels the chord as Major quality.
    //
    // Note: rc.score is the winning template's raw score and may not exactly match
    // the normalised quality reported below.  Callers that need to compare scores
    // across results should be aware of this.

    // 1. Augmented root correction.
    // Augmented triads are symmetric, so pure pitch-class scoring cannot distinguish
    // roots.  TPC spelling resolves this directly when available (the scoring loop
    // already applied the bonus); the heuristic fallback uses the bass note when
    // no TPC data was supplied.
    if (quality == ChordQuality::Augmented && ctx.tpcForPc[static_cast<size_t>(rootPc)] < 0) {
        std::vector<int> pcs;
        for (int pc = 0; pc < 12; ++pc) {
            if (ctx.pcWeight[static_cast<size_t>(pc)] > 0.05) {
                pcs.push_back(pc);
            }
        }
        if (pcs.size() == 3) {
            bool isAug = false;
            for (int i = 0; i < 3 && !isAug; ++i) {
                const int a = pcs[i], b = pcs[(i + 1) % 3], c = pcs[(i + 2) % 3];
                if ((b - a + 12) % 12 == 4 && (c - b + 12) % 12 == 4 && (a - c + 12) % 12 == 4) {
                    isAug = true;
                }
            }
            if (isAug) {
                // Iter 92 — use the joint-winner bass instead of the absolute
                // lowest pitch. The two could disagree when the joint pass
                // picks an octave-up bass-register candidate as the winner.
                rootPc = ctx.bassPc;
            }
        }
    }

    const int rootTpc = ctx.tpcForPc[static_cast<size_t>(rootPc)];
    ExtensionFlags ext = detectExtensions(ctx.pcWeight, rootPc, quality, ctx.tpcForPc, rootTpc, prefs.extensionThreshold);

    // 2. Sus2 → Sus4 upgrade: Sus4 is more specific when P4 is actually sounding.
    if (quality == ChordQuality::Suspended2 && ext.hasEleventh) {
        quality = ChordQuality::Suspended4;
        ext = detectExtensions(ctx.pcWeight, rootPc, quality, ctx.tpcForPc, rootTpc, prefs.extensionThreshold);
    }

    // 3. Sus → Major (omitsThird): when Maj7 is present but no 3rd is sounding,
    // the catalog labels the chord as Major quality.  This covers both the
    // "no-fourth" case (true suspended with Maj7) and the "with-fourth" case
    // (CMaj7sus4 / CMaj9sus4).  A present P4 is retained as an extension.
    const bool hasMajThird  = ctx.pcWeight[static_cast<size_t>((rootPc + 4) % 12)] > 0.2;
    const bool hasMinThird  = ctx.pcWeight[static_cast<size_t>((rootPc + 3) % 12)] > 0.2;
    const bool hasAnyThird  = hasMajThird || hasMinThird;

    bool omitsThird = false;
    if (ext.hasMajorSeventh && !hasAnyThird
        && (quality == ChordQuality::Suspended2 || quality == ChordQuality::Suspended4)) {
        quality    = ChordQuality::Major;
        omitsThird = true;
        ext = detectExtensions(ctx.pcWeight, rootPc, quality, ctx.tpcForPc, rootTpc, prefs.extensionThreshold);
    }

    // Degree assignment.
    int degree = -1;
    for (size_t i = 0; i < ctx.scale.size(); ++i) {
        if ((ctx.keyTonicPc + ctx.scale[i]) % 12 == rootPc) {
            degree = static_cast<int>(i);
            break;
        }
    }

    // Diatonic check: every sounding pc must be in the scale.
    bool diatonic = (degree >= 0);
    if (diatonic) {
        for (int pc = 0; pc < 12; ++pc) {
            if (ctx.pcWeight[static_cast<size_t>(pc)] <= 0.2) {
                continue;
            }
            bool inScale = false;
            for (int interval : ctx.scale) {
                if ((ctx.keyTonicPc + interval) % 12 == pc) {
                    inScale = true;
                    break;
                }
            }
            if (!inScale) {
                diatonic = false;
                break;
            }
        }
    }

    ChordAnalysisResult r;
    r.identity.score                = rc.score;
    r.identity.rootPc               = rootPc;
    r.identity.rootTpc              = rootTpc;
    r.identity.bassPc               = ctx.bassPc;
    r.identity.bassTpc              = ctx.bassTpc;
    r.identity.naturalFifthPresent  = (quality != ChordQuality::Augmented)
                                      && (ctx.pcWeight[static_cast<size_t>((rootPc + 7) % 12)]
                                          > prefs.extensionThreshold);
    r.identity.quality              = quality;
    r.identity.tiePriority          = static_cast<int>(rc.tiePriority);
    r.identity.extensions           = extensionBits(ext, omitsThird);
    r.function.degree               = degree;
    r.function.diatonicToKey        = diatonic;
    r.function.keyTonicPc           = ctx.keyTonicPc;
    r.function.keyMode              = ctx.keyMode;

    return r;
}

ChordExtensionInfo deriveChordExtensions(
    const std::array<double, 12>& pcWeight,
    int rootPc, ChordQuality quality,
    const std::array<int, 12>& tpcForPc,
    int rootTpc, double extThreshold)
{
    ChordExtensionInfo info;
    if (rootPc < 0 || rootPc >= 12) {
        return info;   // no root → no colour (defensive; the caller gates on rootPc >= 0)
    }
    const ExtensionFlags ext =
        detectExtensions(pcWeight, rootPc, quality, tpcForPc, rootTpc, extThreshold);
    // Fixed-quality extraction: NO Sus->Major(omitsThird) mutation (that only fires when
    // buildChordResult CHANGES the quality; the committed quality is authoritative here).
    info.extensions = extensionBits(ext, /*omitsThird=*/false);
    info.naturalFifthPresent = (quality != ChordQuality::Augmented)
                               && (pcWeight[static_cast<size_t>((rootPc + 7) % 12)] > extThreshold);
    return info;
}


std::vector<ChordAnalysisResult> RuleBasedChordAnalyzer::analyzeChord(
    const std::vector<ChordAnalysisTone>& tones,
    int keySignatureFifths,
    KeySigMode keyMode,
    const ChordTemporalContext* context,
    const ChordAnalyzerPreferences& prefs,
    PostScoringGateContext* gateCtxOut,
    fn::ScoringSnapshot* snapshotOut) const
{
    if (tones.empty()) {
        return {};
    }

    // OI-168 (default-OFF): the population the two key-consuming terms are scored under.
    kcp::bump(kcp::counters().analyzeChordCalls);
    if (keyMode == KeySigMode::Altered) {
        kcp::bump(kcp::counters().analyzeChordCallsAltered);
    } else if (keyMode == KeySigMode::AlteredDomBB7) {
        kcp::bump(kcp::counters().analyzeChordCallsAlteredDomBB7);
    }

    // Build pitch-class weight histogram and find the bass note.
    std::array<double, 12> pcWeight {};
    int lowestPitch = std::numeric_limits<int>::max();

    double totalRawWeight = 0.0;
    for (const ChordAnalysisTone& t : tones) {
        const int pc = normalizePc(t.pitch);
        pcWeight[static_cast<size_t>(pc)] += std::max(0.1, t.weight);
        totalRawWeight += std::max(0.0, t.weight);
        if (t.pitch < lowestPitch) {
            lowestPitch = t.pitch;
        }
    }

    // Iter 92 — bass candidate enumeration (joint scoring).
    //
    // Pre-Iter 92 the analyzer committed to a single bass (the lowest qualifying
    // pitch) before the chord scorer ran.  This caused two coupled bugs:
    //   Bug 1 (bwv103.6 m3 b2): a passing eighth note that happens to be the
    //     absolute lowest pitch in the region won bass selection over a
    //     beat-onset bass a step above it.
    //   Bug 2 (bwv310 m8 b3): a slash-chord reading (Em/C) outscored the
    //     root-position triad (C major) because the bass-root bonus + complete-
    //     triad evidence on C had no way to flip the global ranking.
    //
    // Both bugs are fixed by enumerating multiple bass candidates and scoring
    // each against the full 12 × 16 template grid, then picking the global
    // best (rootPc, templateIdx, bassPc) triple.
    //
    // Joint scoring is gated on the input coming from regional accumulation —
    // any tone with onsetAtRegionStart=true OR distinctMetricPositions>0 (both
    // are populated by collectRegionTones but not by the single-tick buildTones
    // path used by status-bar analysis and unit tests).  Synthetic single-tick
    // inputs fall back to the legacy single-bass selection (the absolute lowest
    // qualifying pitch) so that scoring-rule unit tests remain valid.
    const double bassMinWeight = prefs.bassPassingToneMinWeightFraction * totalRawWeight;

    // Joint scoring is enabled when the input came from regional accumulation
    // (collectRegionTones).  buildTones / status-bar inputs default to false
    // and fall back to legacy single-bass scoring.
    bool jointScoringEnabled = false;
    for (const ChordAnalysisTone& t : tones) {
        if (t.onsetAtRegionStart || t.distinctMetricPositions > 0) {
            jointScoringEnabled = true;
            break;
        }
    }
    // jointScoringEnabled is published to the ScoringSnapshot below; the snapshot
    // is now always built internally (no external capture opt-in).

    struct BassCandidate {
        int pitch = std::numeric_limits<int>::max();
        int pc = -1;
        int tpc = -1;
        bool onsetAtRegionStart = false;
    };
    std::vector<BassCandidate> bassCandidates;
    if (jointScoringEnabled) {
        // Scan tones in the bass register (lowest pitch + one octave) for
        // multi-bass enumeration candidates.  The actual enumeration only
        // fires when there is musical evidence that the bass voice moves
        // within the region — at least one candidate with onsetAtRegionStart
        // = true AND at least one with onsetAtRegionStart = false.  This
        // distinguishes the bwv103.6 m3 b2 scenario (bass voice has G at
        // start, F# mid-region) from a static SATB / Jazz voicing where the
        // bass and upper voices all attack at the region start (one bass
        // candidate, no enumeration).
        const int bassRegisterCutoff = (lowestPitch != std::numeric_limits<int>::max())
                                       ? lowestPitch + 12
                                       : std::numeric_limits<int>::max();
        std::array<int, 12> bestPitchPerPc;
        std::array<int, 12> tpcPerPc;
        std::array<bool, 12> onsetPerPc;
        bestPitchPerPc.fill(std::numeric_limits<int>::max());
        tpcPerPc.fill(-1);
        onsetPerPc.fill(false);
        for (const ChordAnalysisTone& t : tones) {
            if (t.pitch > bassRegisterCutoff) { continue; }
            if (t.weight < bassMinWeight)      { continue; }
            const int pc = normalizePc(t.pitch);
            const size_t pcIdx = static_cast<size_t>(pc);
            if (t.pitch < bestPitchPerPc[pcIdx]) {
                bestPitchPerPc[pcIdx] = t.pitch;
                tpcPerPc[pcIdx]       = t.tpc;
            }
            if (t.onsetAtRegionStart) {
                onsetPerPc[pcIdx] = true;
            }
        }
        std::vector<BassCandidate> regionalCandidates;
        for (int pc = 0; pc < 12; ++pc) {
            const size_t pcIdx = static_cast<size_t>(pc);
            if (bestPitchPerPc[pcIdx] != std::numeric_limits<int>::max()) {
                regionalCandidates.push_back({ bestPitchPerPc[pcIdx], pc,
                                               tpcPerPc[pcIdx], onsetPerPc[pcIdx] });
            }
        }
        std::sort(regionalCandidates.begin(), regionalCandidates.end(),
                  [](const BassCandidate& a, const BassCandidate& b) { return a.pitch < b.pitch; });
        bool hasOnsetTrue  = false;
        bool hasOnsetFalse = false;
        for (const auto& rc : regionalCandidates) {
            if (rc.onsetAtRegionStart) { hasOnsetTrue = true; }
            else                       { hasOnsetFalse = true; }
        }
        // Sparse upper-register fallback: when the bass continuo rests (no
        // sounding note below middle C) and the region is reduced to two
        // upper-voice pitches, the "lowest sounding pitch" picked by the
        // legacy single-bass fallback is just the lower of two melodic notes,
        // not a structural bass. Enumerate so the root-position reading can
        // compete with the accidental inversion implied by literal-bass
        // selection. Corelli op01n08d m2 b3: G5 + B4 should score as V (G
        // root-position) per DCML, not V6/B. Gated on lowestPitch > 60 so
        // genuine bass voicings (D3, E2, …) keep their single-bass path.
        int distinctPcCount = 0;
        for (double w : pcWeight) {
            if (w > 0.05) { ++distinctPcCount; }
        }
        const bool sparseUpperRegisterAmbiguous =
            distinctPcCount <= 2
            && regionalCandidates.size() >= 2
            && lowestPitch > 60;
        if ((hasOnsetTrue && hasOnsetFalse) || sparseUpperRegisterAmbiguous) {
            bassCandidates = std::move(regionalCandidates);
            if (bassCandidates.size() > 4) {
                bassCandidates.resize(4);
            }
        }
    }
    // Legacy single-bass fallback (used when joint enumeration declines to fire
    // or when the weight filter eliminated every candidate).
    if (bassCandidates.empty() && lowestPitch != std::numeric_limits<int>::max()) {
        int lowestQualifyingPitch = std::numeric_limits<int>::max();
        for (const ChordAnalysisTone& t : tones) {
            if (t.weight >= bassMinWeight && t.pitch < lowestQualifyingPitch) {
                lowestQualifyingPitch = t.pitch;
            }
        }
        const int chosenPitch = (lowestQualifyingPitch < std::numeric_limits<int>::max())
                                ? lowestQualifyingPitch : lowestPitch;
        int chosenTpc = -1;
        bool chosenOnsetAtStart = false;
        for (const ChordAnalysisTone& t : tones) {
            if (t.pitch == chosenPitch) {
                if (t.tpc >= 0) { chosenTpc = t.tpc; }
                if (t.onsetAtRegionStart) { chosenOnsetAtStart = true; }
            }
        }
        bassCandidates.push_back({ chosenPitch, normalizePc(chosenPitch),
                                   chosenTpc, chosenOnsetAtStart });
    }

    // The working bass (winning bassPc / bassTpc) is now selected by the function
    // layer (applyHarmonicFunction) from the full multi-bass snapshot built below.

    // TPC lookup: for each pitch class, store the TPC of the first sounding tone
    // that has TPC data.  -1 means no TPC data for that pitch class.
    std::array<int, 12> tpcForPc;
    tpcForPc.fill(-1);
    for (const ChordAnalysisTone& t : tones) {
        if (t.tpc >= 0) {
            const int pc = normalizePc(t.pitch);
            if (tpcForPc[static_cast<size_t>(pc)] == -1) {
                tpcForPc[static_cast<size_t>(pc)] = t.tpc;
            }
        }
    }

    // Count distinct pitch classes; require at least prefs.minDistinctPcsForCandidate
    // (default 3) for meaningful analysis. Greedy-expand callers relax this to 1 so
    // sparse 1–2 PC entries can be scored, then apply a PC-count-adaptive threshold
    // at the comparison site.
    int distinctPcs = 0;
    for (double w : pcWeight) {
        if (w > 0.05) {
            ++distinctPcs;
        }
    }
    if (distinctPcs < prefs.minDistinctPcsForCandidate) {
        return {};
    }

    // Structural-bass heuristic: when the lowest sounding pitch sits above
    // middle C (MIDI 60) and the region is sparse (≤ 2 distinct PCs), the
    // "bass" picked from the literal lowest pitch is just the lower of two
    // upper-voice notes — there is no continuo / bass-voice support behind
    // it. Inversion contextual bonuses (stepwise / lookahead / same-root) assume
    // a structural bass; firing them on accidental upper-voice "inversions"
    // promotes spurious slash readings over root-position chords whose
    // function is implied (Corelli op01n08d m2 b3: G + B with bass continuo
    // resting should score as V root-position per DCML, not V6 / G/B).
    // distinctPcs ≥ 3 retains the bonus because denser regions carry their
    // own structural cues; dense static SATB textures with bass in tenor
    // register remain unchanged.
    const bool hasStructuralBass = (lowestPitch <= 60) || (distinctPcs >= 3);

    // Chord templates (quality, intervals-from-root, TPC-deltas-from-root).
    //
    // Template ordering encodes quality tie-breaking priority: when two candidates
    // score identically, the one whose template appears earlier in this array wins
    // (see RawCandidate::tiePriority and the sort below).
    //
    // Key ordering decisions:
    //   Sus4b5 (index 7) precedes HalfDim (index 8): both templates cover the same
    //   4 pitch classes for altered-suspension chords (e.g. {root,P4,b5,m7}); the
    //   Sus4b5 interpretation is preferred because it names the defining P4 interval.
    //
    //   Min7 (index 5) follows Minor triad (index 4) and precedes Sus4 templates:
    //   the explicit 4-note template scores {root,m3,P5,m7} as a unit and outranks
    //   inverted alternatives (e.g. a C6 inversion over E bass) that share the same
    //   pitch classes but have a weaker template-tone match from the correct root.
    //
    //   dom7b5 {root,M3,b5,m7} covers Lydian-dominant chords (C7#11 = C E F# Bb).
    //   TPC delta +6 = augmented 4th (F# from C, clockwise six steps on circle of fifths).
    //
    // analysis::kTemplateCount templates: see docs/scoring_model.md §2 for the full list.
    // When adding a template: bump analysis::kTemplateCount (chordanalyzer.h), add the
    // interval row to kTemplateIntervals (chordanalyzer.h — the single interval source, from
    // which both this array's intervals AND the kMasks bitmask are now DERIVED), then add the
    // matching entry here (quality + tpcDeltas; intervals via templateIntervalsVec(i)). Every
    // template-sized array — this TemplateDef array, the three score matrices below, and
    // kMasks — derives its extent from kTemplateCount, so adding an entry without bumping
    // the constant is now a COMPILE error (too many initializers) rather than the silent
    // stack-buffer overrun caught in the B1 attempt 2026-06-04. (The former kDiagTemplates
    // mirror was removed in Stage 2.3 — diagnoseChord no longer keeps its own template
    // array.) See docs/scoring_model.md §3 and §9.
    // The `intervals` field of every row is DERIVED from the canonical kTemplateIntervals
    // table (chordanalyzer.h) via templateIntervalsVec(i) — kTemplateIntervals is the sole
    // interval source, shared with Gate R's kMasks. The index i == the row's template index
    // (Row order is load-bearing; see kTemplateIntervals). `quality` and `tpcDeltas` stay
    // inline (template-scoring data, not the shared interval set).
    static const std::array<TemplateDef, kTemplateCount> templates = {{
        { ChordQuality::Major,          templateIntervalsVec(0),  { 0, +4, +1 }       },
        { ChordQuality::Major,          templateIntervalsVec(1),  { 0, +4, +1, +5 }   },  // maj7
        { ChordQuality::Major,          templateIntervalsVec(2),  { 0, +4, +1, -2 }   },  // dom7
        { ChordQuality::Major,          templateIntervalsVec(3),  { 0, +4, -6, -2 }   },  // dom7b5
        { ChordQuality::Minor,          templateIntervalsVec(4),  { 0, -3, +1 }       },
        { ChordQuality::Minor,          templateIntervalsVec(5),  { 0, -3, +1, -2 }   },  // min7
        { ChordQuality::Diminished,     templateIntervalsVec(6),  { 0, -3, -6 }       },
        { ChordQuality::Suspended4,     templateIntervalsVec(7),  { 0, -1, -6, -2 }   },  // sus4b5  — precedes HalfDim (tie-break)
        { ChordQuality::HalfDiminished, templateIntervalsVec(8),  { 0, -3, -6, -2 }   },
        { ChordQuality::Augmented,      templateIntervalsVec(9),  { 0, +4, +8 }       },
        { ChordQuality::Augmented,      templateIntervalsVec(10), { 0, +4, +8, -2 }   },  // aug7 (C7♯5)
        { ChordQuality::Suspended2,     templateIntervalsVec(11), { 0, +2, +1 }       },
        { ChordQuality::Suspended4,     templateIntervalsVec(12), { 0, -1, +1, -2 }   },
        { ChordQuality::Suspended4,     templateIntervalsVec(13), { 0, -1, +1, +5 }   },  // sus4+maj7
        { ChordQuality::Suspended4,     templateIntervalsVec(14), { 0, -1, +8, -2 }   },  // sus4#5
        { ChordQuality::Suspended4,     templateIntervalsVec(15), { 0, +6, +1 }       },  // sus#4 (F# not Gb)
        { ChordQuality::Power,          templateIntervalsVec(16), { 0, +1 }           }
    }};
    static_assert(templates.size() == kTemplateCount,
                  "templates array extent must equal analysis::kTemplateCount");

    // Key context — used for scale-DEGREE assignment (a degree is tonic-relative by definition)
    // and published on the snapshot for the post-scoring gates. The two key-consuming SCORING
    // terms no longer read either of these: they take the signature collection below (OI-168).
    const int ionianTonicPc = ionianTonicPcFromFifths(keySignatureFifths);
    const int keyTonicPc    = (ionianTonicPc + keyModeTonicOffset(keyMode)) % 12;

    // keyModeIndex() returns the raw enum ordinal (0–20 for all 21 KeySigMode values).
    // Non-diatonic modes are mapped to their diatonic key-signature parent for degree
    // assignment.
    //
    // OI-168 — READ THIS BEFORE REUSING `scale` FOR A COLLECTION TEST. The set
    // { (keyTonicPc + scale[i]) mod 12 } equals the key SIGNATURE's collection only while every
    // mode's tonic offset matches its parent's. That holds for 19 of the 21 KeySigMode values
    // and FAILS for Altered (offset 1, Ionian parent offset 0) and AlteredDomBB7 (offset 8,
    // Mixolydian parent offset 7): for those two the set is the signature's collection
    // transposed up a semitone (2 of 7 pitch classes shared). It is not fixable by re-parenting —
    // their tonic is not a member of any parent collection. A question of the form "is this pitch
    // class IN THE KEY?" must therefore use `signatureMask` below, never this pair.
    static constexpr std::array<size_t, 21> DIATONIC_PARENT_INDEX = {
        0, 1, 2, 3, 4, 5, 6,  // diatonic: identity mapping
        1, 2, 3, 4, 5, 6, 0,  // melodic minor family: Dorian…Ionian parents
        5, 6, 0, 1, 2, 3, 4   // harmonic minor family: Aeolian…Mixolydian parents
    };
    const size_t modeScaleIdx = DIATONIC_PARENT_INDEX[keyModeIndex(keyMode)];
    const std::array<int, 7>& scale = keyModeScaleIntervals(keyModeFromIndex(modeScaleIdx));

    // The key SIGNATURE's own diatonic collection: the pitch-class set the two key-consuming
    // scoring terms test membership in. Depends only on the notated signature — no tonic, no
    // mode — so their tonic-independence is structural (OI-168).
    const uint16_t signatureMask = diatonicMaskFromFifths(keySignatureFifths);

    // Score every root × template combination.
    //
    // Each concern is delegated to a named helper (defined in the anonymous namespace
    // above) so that each rule is independently readable and modifiable.
    //
    // RawCandidate is declared at namespace scope (chordanalyzer.h) so it can be
    // used by buildChordResult() and applyPostScoringGates().

    // Iter 92 — joint (bass, chord) scoring.
    //
    // For each (rootPc, templateIdx) compute the bass-INDEPENDENT base once.
    // For each enumerated bass candidate, add the bass-DEPENDENT delta plus
    // the JOINT terms (w_complete in Step 3a, w_onset / w_passing in 3b,
    // w_stepIn / w_stepOut in 3c), build full rawCandidates, and track the
    // global best (rootPc, templateIdx, bassPc) triple.  The winning bass
    // becomes the working bass for downstream result-building, post-ranking
    // inversion correction and pedal detection.
    // The three score matrices' column extent derives from analysis::kTemplateCount, so
    // it stays in sync with the TemplateDef arrays above by construction (no more silent
    // stack-buffer overrun on a mismatched literal).  See docs/scoring_model.md §3.
    std::array<std::array<double, kTemplateCount>, 12> basisIndepMatrix{};
    std::array<std::array<double, kTemplateCount>, 12> complexityFactorMatrix{};
    std::array<std::array<double, kTemplateCount>, 12> augFactorMatrix{};
    for (int rootPc = 0; rootPc < 12; ++rootPc) {
        for (size_t tplIdx = 0; tplIdx < templates.size(); ++tplIdx) {
            const TemplateDef& tpl = templates[tplIdx];

            // B2 guard: the 4-tone Augmented (aug7) template requires BOTH the major
            // third (rootPc+4) AND the augmented fifth (rootPc+8) to be present above
            // extensionThreshold.  The `||` (skip if EITHER is absent) means BOTH
            // must be present for the template to score.
            //
            // M3-only relaxation has been tried and reverted (2026-06-05).  Using
            // `&&` instead of `||` lets the aug7 template over-fire on complete
            // major triads containing a minor seventh: with only root+M3+m7 present,
            // the large aug5 score offset (+8) still inflates the partial-match
            // score above a complete major triad.  Schumann D-major and Corelli
            // G-major snapshots flipped to aug7 under the relaxed guard.  The dual
            // `||` is load-bearing — see docs/scoring_model.md §4.
            if (tpl.quality == ChordQuality::Augmented
                && tpl.intervals.size() == 4
                && (pcWeight[static_cast<size_t>((rootPc + 4) % 12)] <= prefs.extensionThreshold
                    || pcWeight[static_cast<size_t>((rootPc + 8) % 12)] <= prefs.extensionThreshold)) {
                continue;
            }

            // dim7CharacteristicBonus is a ROTATION-SELECTION MECHANISM — not just a
            // score offset.  All four enharmonic rotations of a dim7 chord share the
            // same PC set (C°7 = Eb°7 = Gb°7 = A°7).  The non-diatonic check on the
            // bb7 PC inside the helper asymmetrically rewards the correct enharmonic
            // root: the bb7 of the "true" rotation is non-diatonic in the current key,
            // while the bb7 of the three spurious rotations is diatonic (coincides
            // with a scale tone) and gets no bonus.
            // DO NOT suppress or bypass this bonus without replacing this rotation-
            // selection function.  Suppressing it breaks 6 Jazz catalog dim7 entries
            // (B3 attempt 2026-06-05).  See docs/scoring_model.md §4.
            basisIndepMatrix[rootPc][tplIdx] =
                scoreTemplateTones(tpl, rootPc, pcWeight)
                + scoreExtraNotes(tpl, rootPc, pcWeight, tpcForPc)
                + dim7CharacteristicBonus(tpl, rootPc, pcWeight, signatureMask,
                                          prefs.extensionThreshold)
                + structuralPenalties(tpl, rootPc, pcWeight, tpcForPc, distinctPcs, prefs.extensionThreshold)
                + tpcConsistencyBonus(tpl, rootPc, tpcForPc, prefs)
                + diatonicRootContribution(rootPc, signatureMask, prefs);

            // Iter 74 Fix A — template complexity preference (bass-independent).
            const int templateDefinedTones = static_cast<int>(tpl.intervals.size());
            const double evidenceRatio
                = (distinctPcs >= templateDefinedTones)
                ? 1.0
                : static_cast<double>(distinctPcs) / templateDefinedTones;
            complexityFactorMatrix[rootPc][tplIdx]
                = (evidenceRatio >= kComplexityEvidenceFloor)
                ? 1.0 : (kComplexityEvidenceFloor + evidenceRatio);

            // Iter 78 Fix C + Iter 79 — augmented bare-root / thin-evidence
            // penalties (both bass-independent).
            double augFactor = 1.0;
            if (tpl.quality == ChordQuality::Augmented
                && distinctPcs <= 2
                && pcWeight[static_cast<size_t>(rootPc)] <= prefs.extensionThreshold) {
                augFactor *= kAugThinEvidenceFactor;
            }
            if (tpl.quality == ChordQuality::Augmented) {
                const double thirdW = pcWeight[static_cast<size_t>((rootPc + 4) % 12)];
                const double fifthW = pcWeight[static_cast<size_t>((rootPc + 8) % 12)];
                const double min7W  = pcWeight[static_cast<size_t>((rootPc + 10) % 12)];
                const double maj7W  = pcWeight[static_cast<size_t>((rootPc + 11) % 12)];
                if (thirdW <= prefs.extensionThreshold
                    && fifthW <= prefs.extensionThreshold
                    && min7W <= prefs.extensionThreshold
                    && maj7W <= prefs.extensionThreshold) {
                    augFactor *= kAugThinEvidenceFactor;
                }
            }
            augFactorMatrix[rootPc][tplIdx] = augFactor;
        }
    }

    // Iter 92 Step 3a — w_complete.
    //
    // When the candidate root equals the bass, all three triad tones are
    // present above extensionThreshold, and the region has exactly 3 distinct
    // pitch classes, promote the root-position triad by w_complete.  This
    // unblocks the Em/C → C major flip (bwv310 m8 b3, Bug 2) without
    // promoting slash-chord candidates that are missing a triad tone (the
    // Iter 90 regression mode).  Gated on jointScoringEnabled so single-tick
    // (status-bar / unit test) inputs preserve their pre-Iter-92 scores.
    // (kWComplete relocated to file scope for the Stage-5 override mechanism.)
    auto wCompleteBonus = [&](const TemplateDef& tpl, int rootPc, int candBassPc) -> double {
        if (!jointScoringEnabled || candBassPc != rootPc || distinctPcs != 3) {
            return 0.0;
        }
        const double thr = prefs.extensionThreshold;
        int thirdInterval = -1;
        int fifthInterval = -1;
        switch (tpl.quality) {
        case ChordQuality::Major:      thirdInterval = 4; fifthInterval = 7; break;
        case ChordQuality::Minor:      thirdInterval = 3; fifthInterval = 7; break;
        case ChordQuality::Diminished: thirdInterval = 3; fifthInterval = 6; break;
        case ChordQuality::Augmented:  thirdInterval = 4; fifthInterval = 8; break;
        default:                       return 0.0;  // gate only fires for plain triads
        }
        const double rootW  = pcWeight[static_cast<size_t>(rootPc)];
        const double thirdW = pcWeight[static_cast<size_t>((rootPc + thirdInterval) % 12)];
        const double fifthW = pcWeight[static_cast<size_t>((rootPc + fifthInterval) % 12)];
        // "Present" = above the distinctPcs gate (0.05), matching how the rest
        // of the analyzer defines a sounding tone.  This avoids the floating-
        // point boundary at exactly extensionThreshold (bwv310 m8 b3 has C and
        // G with pcWeight that prints as 0.200 but rounds slightly below in
        // double).  Iter-90's regression mode (slash chord with missing fifth)
        // is still excluded — an absent tone gives pcWeight = 0.  `thr` is
        // accepted into the API for a future tightening pass.
        (void)thr;
        // (kPresenceThreshold relocated to file scope as kWCompletePresenceThreshold
        //  for the Stage-5 override mechanism — same 0.05 value.)
        const bool allTriadPresent = (rootW > kWCompletePresenceThreshold)
                                  && (thirdW > kWCompletePresenceThreshold)
                                  && (fifthW > kWCompletePresenceThreshold);
        return allTriadPresent ? kWComplete : 0.0;
    };

    // -- Build the scoring snapshot (vertical-only scores, every bass) ---------
    //
    // The oracle computes only pitch/key-dependent quantities. Progression
    // signals (rootContinuity, w_seq, w_dim, step bonuses), winner selection,
    // threshold, result cap, diff-root append and gate-context construction are
    // all owned by applyHarmonicFunction(). See docs/scoring_model.md section 11.
    fn::ScoringSnapshot snapshot;
    snapshot.distinctPcs         = distinctPcs;
    snapshot.jointScoringEnabled = jointScoringEnabled;
    snapshot.pcWeight            = pcWeight;
    snapshot.tpcForPc            = tpcForPc;
    snapshot.scale               = scale;
    snapshot.keyTonicPc          = keyTonicPc;
    snapshot.keyMode             = keyMode;
    snapshot.cells.reserve(bassCandidates.size() * 12 * templates.size());

    for (size_t bi = 0; bi < bassCandidates.size(); ++bi) {
        const int candBassPc = bassCandidates[bi].pc;
        for (int rootPc = 0; rootPc < 12; ++rootPc) {
            for (size_t tplIdx = 0; tplIdx < templates.size(); ++tplIdx) {
                const TemplateDef& tpl = templates[tplIdx];
                const double bassBonus =
                    appliedBassRootBonus(tpl, rootPc, candBassPc, pcWeight, prefs);
                // basisDep is now genuinely vertical (Stage 3.3): nonBassAdjustment +
                // appliedBassBonus. The four §4.1b inversion bonuses migrated to the
                // competition pipeline (fn::inversionContextBonus), gated by the per-cell
                // vertical-eligibility flags published below.
                const double basisDep =
                    nonBassAdjustment(tpl, rootPc, candBassPc, tpcForPc) + bassBonus;

                fn::ScoringCell cell;
                cell.bassPc           = candBassPc;
                cell.bassTpc          = bassCandidates[bi].tpc;
                cell.rootPc           = rootPc;
                cell.tiePriority      = static_cast<int>(tplIdx);
                cell.quality          = tpl.quality;
                cell.intervalCount    = static_cast<int>(tpl.intervals.size());
                cell.basisIndep       = basisIndepMatrix[rootPc][tplIdx];
                cell.basisDep         = basisDep;
                cell.complexityFactor = complexityFactorMatrix[rootPc][tplIdx];
                cell.augFactor        = augFactorMatrix[rootPc][tplIdx];
                cell.wCompleteBonus   = wCompleteBonus(tpl, rootPc, candBassPc);
                cell.appliedBassBonus = bassBonus;
                // Vertical inversion-eligibility flags (oracle pitch facts), ANDed with
                // hasStructuralBass so sparse upper-register "basses" never trigger the
                // migrated inversion bonuses (the old `if (context && hasStructuralBass)`
                // guard). The pipeline gates fn::inversionContextBonus on these.
                cell.supportsInversionBonuses =
                    hasStructuralBass
                    && supportsContextualInversionBonuses(tpl, rootPc, candBassPc, pcWeight);
                cell.qualifiesCompleteTriad =
                    hasStructuralBass
                    && qualifiesForCompleteTriadInversionBonus(tpl, rootPc, candBassPc, pcWeight, distinctPcs);
                snapshot.cells.push_back(cell);
            }
        }
    }

    // -- Run the competition pipeline (winner selection lives here) ------------
    // Key influence does NOT flow through the function context: it is already frozen
    // into cell.basisIndep here, via the oracle's dim7CharacteristicBonus and
    // diatonicRootContribution (which consume keyTonicPc/scale above), and is
    // forwarded to the post-scoring gates through snapshot.{scale,keyTonicPc,keyMode}.
    // Do NOT add key-confidence scaling on the function context (it would be a no-op —
    // scale the oracle terms instead). See cc_step3_key_investigation_report.md Part A.
    fn::HarmonicFunctionContext fnCtx;
    fnCtx.previousRootPc = context ? context->previousRootPc : -1;
    fnCtx.nextRootPc     = context ? context->nextRootPc     : -1;
    fnCtx.previousBassPc = context ? context->previousBassPc : -1;
    fnCtx.nextBassPc     = context ? context->nextBassPc     : -1;
    // Stage 3.3 — bass-stepwise edges the migrated inversion bonuses read (the old
    // bassDependentContextualBonuses' `context->bassIsStepwise*`). Null-context path keeps
    // them false, which zeroes fn::inversionContextBonus (matches the old `if (context...)`).
    fnCtx.bassIsStepwiseFromPrevious = context ? context->bassIsStepwiseFromPrevious : false;
    fnCtx.bassIsStepwiseToNext       = context ? context->bassIsStepwiseToNext       : false;
    // Step 1 redesign: free wiring — forwarded from ChordTemporalContext, no scoring logic yet
    fnCtx.previousQuality              = context ? context->previousQuality              : ChordQuality::Unknown;
    fnCtx.consecutiveBassStepwiseCount = context ? context->consecutiveBassStepwiseCount : 0;
    fnCtx.regionMetricWeight           = context ? context->regionMetricWeight           : 1.0;
    fnCtx.recentRootPcs                = context ? context->recentRootPcs : std::array<int, 3>{ -1, -1, -1 };
    // Step 2 redesign: predecessor confidence channel
    fnCtx.previousWinnerScore        = context ? context->previousWinnerScore        : 0.0;
    fnCtx.previousWinnerMargin       = context ? context->previousWinnerMargin       : -1.0;
    fnCtx.previousWinnerRootPcWeight = context ? context->previousWinnerRootPcWeight : 0.0;
    fnCtx.previousDistinctPcs        = context ? context->previousDistinctPcs        : 0;

    // Region data the gate context needs but the snapshot does not carry.
    if (gateCtxOut) {
        gateCtxOut->tones        = tones;
        gateCtxOut->keySigFifths = keySignatureFifths;
    }

    std::vector<ChordAnalysisResult> results;
    ChordAnalysisResult chosenResult;
    fn::applyHarmonicFunction(snapshot, fnCtx, prefs, results, chosenResult, gateCtxOut,
                              prefs.scoringPhase);

    // Gates A-L, the Iter 86/91 promotions and the two-pass pedal detection run
    // externally (applyIter8691Pedal + applyPostScoringGates) at every production
    // call site AFTER this function returns. Do NOT call them here.

    // Hand the internally-built snapshot to an introspecting caller (diagnoseChord).
    // Mirrors the gateCtxOut pattern: a single branch + one move when requested, and
    // byte-identical behavior (zero cost) when null. applyHarmonicFunction() consumed
    // `snapshot` by const-ref and does not mutate it, so moving it out here is safe.
    if (snapshotOut) {
        *snapshotOut = std::move(snapshot);
    }

    return results;
}





std::unique_ptr<IChordAnalyzer> ChordAnalyzerFactory::create(ChordAnalyzerType type)
{
    switch (type) {
    case ChordAnalyzerType::RuleBased:
    default:
        return std::make_unique<RuleBasedChordAnalyzer>();
    }
}

} // namespace mu::composing::analysis
