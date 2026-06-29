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

#include "composing/analysis/function/functionrelationallabel.h"

#include "composing/analysis/chord/analysisutils.h"            // normalizePc, diatonicMaskFromFifths
#include "composing/analysis/engravingbridge/spellingview.h"   // lineOfFifths (the ONE spelling read)
#include "composing/analysis/function/tonicizationlabeler.h"   // labelTonicizations (the applied path reuse)
#include "composing/analysis/region/sparsechordrefinement.h"   // diatonicDegreeForRootPc

#include <array>

namespace mu::composing::analysis {

// The relational-label helpers live in a NAMED detail namespace: the unity build
// concatenates this TU with sibling files, and a named namespace keeps these private
// symbols distinct from theirs (the tonicizationlabeler / functionromannumeral convention).
namespace relational_detail {

/// Build the ChordAnalysisResult the shared formatter consumes — the deterministic
/// reading of degree + key context, the identity passed straight through. nextRootPc
/// is -1 for the base numeral (no inline applied label) and may be set when the caller
/// wants the formatter's inline applied emission. The degree is computed by the SAME
/// region::diatonicDegreeForRootPc the base-RN module (functionromannumeral) uses.
inline ChordAnalysisResult makeResult(const RelationalLabelInput& in, int nextRootPc) noexcept
{
    ChordAnalysisResult r;
    r.identity = in.identity;
    r.function.degree = region::diatonicDegreeForRootPc(in.identity.rootPc, in.keyFifths, in.keyMode);
    r.function.diatonicToKey = (r.function.degree >= 0);
    r.function.keyTonicPc = in.keyTonicPc;
    r.function.keyMode = in.keyMode;
    r.function.nextRootPc = nextRootPc;
    return r;
}

/// The chord's plain BASE Roman numeral (no relational label) — the ONE formatter,
/// nextRootPc unset. This is what a role==None or a modal-mixture chord emits (the
/// chromatic/altered numeral the formatter already produces: bVI, iv, …).
inline std::string baseNumeral(const RelationalLabelInput& in)
{
    return ChordSymbolFormatter::formatRomanNumeral(makeResult(in, /*nextRootPc=*/-1));
}

/// Read the notated spelling of the +10-semitone tone above a ♭6̂ root through the
/// shared engravingbridge::lineOfFifths() interpreter — the ONE place this layer reads
/// spelling (§5.6 / §8): the German sixth versus the dominant seventh. The line-of-
/// fifths DISTANCE of that tone from the root distinguishes the two pitch-class-identical
/// readings: +10 ⇒ an augmented sixth (which expands outward to the dominant), −2 ⇒ a
/// minor seventh (which resolves down). Returns +1 (aug6), −1 (minor seventh / another
/// spelling of that pc), or 0 (the spelling is unavailable — the +10 tone or the root
/// has no valid tpc — so the aug6 label is held uncertain, §11).
inline int augSixthSpellingSign(const RelationalLabelInput& in) noexcept
{
    using engravingbridge::kNoLineOfFifths;
    using engravingbridge::lineOfFifths;

    const int rootLof = lineOfFifths(in.identity.rootTpc);
    if (rootLof == kNoLineOfFifths) {
        return 0;  // the root spelling is absent — cannot read the interval's spelling
    }
    const int targetPc = normalizePc(in.identity.rootPc + 10);
    for (int tpc : in.noteTpcs) {
        const int lof = lineOfFifths(tpc);
        if (lof == kNoLineOfFifths) {
            continue;
        }
        // The pitch class of a spelling is (lineOfFifths · 7) mod 12 (each fifth is 7
        // semitones); compare against the +10 tone's pitch class.
        if (normalizePc(lof * 7) != targetPc) {
            continue;
        }
        const int dist = lof - rootLof;
        if (dist == 10) {
            return 1;   // augmented sixth — the aug6 spelling
        }
        if (dist == -2) {
            return -1;  // minor seventh — the dominant-seventh spelling
        }
        return -1;      // any other spelling of that pitch class — not an augmented sixth
    }
    return 0;  // the +10 tone's spelling is not among the chord's notes — cannot confirm
}

// ── §5.6 the four relational triggers (in precedence order) ───────────────────

/// 1. AUGMENTED SIXTH (spelling-aware, the Ger6↔V7 distinction). Trigger: a Major-
/// quality chord on ♭6̂ whose +10 tone is spelled as an augmented sixth (the spelling
/// read). The It/Fr/Ger string comes from formatRomanNumeral (SharpThirteenth +
/// naturalFifthPresent[Ger] / SharpEleventh[Fr]); SharpThirteenth is ensured so the
/// emission is driven by THIS layer's spelling decision (L5 as the spelling authority).
inline RelationalLabel tryAugmentedSixth(const RelationalLabelInput& in)
{
    RelationalLabel out;
    const int root = in.identity.rootPc;
    if (root < 0 || in.identity.quality != ChordQuality::Major) {
        return out;  // an augmented sixth is a Major-quality ♭6̂-rooted sonority
    }
    if (root != normalizePc(in.keyTonicPc + 8)) {
        return out;  // not on the lowered sixth degree
    }
    const int sign = augSixthSpellingSign(in);
    out.spellingConsulted = (sign != 0);
    if (sign != 1) {
        return out;  // a dominant-seventh spelling (or spelling absent) — not an aug6
    }
    ChordAnalysisResult r = makeResult(in, /*nextRootPc=*/-1);
    setExtension(r.identity.extensions, Extension::SharpThirteenth);
    out.label = ChordSymbolFormatter::formatRomanNumeral(r);
    out.role = RelationalRole::AugmentedSixth;
    out.spelledAsAugSixth = true;
    return out;
}

/// 2. NEAPOLITAN (bII6). Trigger: a Major triad on the lowered second degree (b2̂),
/// conventionally in first inversion; a chromatic pre-dominant, the local key unchanged.
/// The string is the chromatic numeral + inversion figure formatRomanNumeral already
/// emits (bII in root position; bII6 in first inversion — the DCML-canonical form).
inline RelationalLabel tryNeapolitan(const RelationalLabelInput& in)
{
    RelationalLabel out;
    const int root = in.identity.rootPc;
    if (root < 0 || in.identity.quality != ChordQuality::Major) {
        return out;
    }
    if (root != normalizePc(in.keyTonicPc + 1)) {
        return out;  // not on the lowered second degree
    }
    out.label = baseNumeral(in);  // bII / bII6 (the inversion figure follows the bass)
    out.role = RelationalRole::Neapolitan;
    return out;
}

/// The fixed major-key diatonic triad qualities, by degree 0..6: I ii iii IV V vi viio.
/// Used only by the modal-mixture residual to detect a borrowed quality on a diatonic
/// root in a MAJOR (Ionian) key (the canonical iv-in-major case). The minor/modal
/// borrowed-quality case is NOT measured here (only the chromatic-root mixture fires
/// in non-Ionian keys) — a documented scope, declared to Cowork; the role is a best-
/// effort tag and the LABEL string is always the formatter's correct numeral.
constexpr std::array<ChordQuality, 7> kMajorKeyTriadQuality = {
    ChordQuality::Major, ChordQuality::Minor, ChordQuality::Minor, ChordQuality::Major,
    ChordQuality::Major, ChordQuality::Minor, ChordQuality::Diminished
};

/// Collapse a chord quality onto its underlying TRIAD family (the seventh/extensions are
/// ignored for the borrowed-triad test). A half-diminished triad is diminished; sus /
/// power chords are not mixture candidates (Unknown ⇒ the test is skipped).
inline ChordQuality triadFamily(ChordQuality q) noexcept
{
    switch (q) {
    case ChordQuality::Major:          return ChordQuality::Major;
    case ChordQuality::Minor:          return ChordQuality::Minor;
    case ChordQuality::Diminished:     return ChordQuality::Diminished;
    case ChordQuality::HalfDiminished: return ChordQuality::Diminished;
    case ChordQuality::Augmented:      return ChordQuality::Augmented;
    default:                           return ChordQuality::Unknown;
    }
}

/// 4. MODAL MIXTURE (the RESIDUAL, §5.6). Fires only when no earlier label matched: a
/// borrowed degree that changes the chord's quality but not the key — a chromatic root
/// (bVI, bIII, bVII…), or, in a major (Ionian) key, a diatonic root whose triad quality
/// differs from the key's diatonic triad on that degree (iv-in-major…). The string is
/// the chromatic/altered numeral formatRomanNumeral already emits; the role marks it
/// borrowed.
inline RelationalLabel tryModalMixture(const RelationalLabelInput& in)
{
    RelationalLabel out;
    const int root = in.identity.rootPc;
    if (root < 0) {
        return out;
    }
    const int degree = region::diatonicDegreeForRootPc(root, in.keyFifths, in.keyMode);
    bool borrowed = false;
    if (degree < 0) {
        borrowed = true;  // a chromatic root — borrowed by construction
    } else if (in.keyMode == KeySigMode::Ionian && degree < 7) {
        const ChordQuality cq = triadFamily(in.identity.quality);
        const ChordQuality dq = kMajorKeyTriadQuality[static_cast<size_t>(degree)];
        if (cq != ChordQuality::Unknown && cq != dq) {
            borrowed = true;  // a borrowed (quality-altering) diatonic degree
        }
    }
    if (!borrowed) {
        return out;
    }
    out.label = baseNumeral(in);
    out.role = RelationalRole::ModalMixture;
    return out;
}

} // namespace relational_detail

// ── The unified applied/tonicization emitter (§3) — ONE owned emitter ─────────

RelationalLabel emitAppliedLabel(const RelationalLabelInput& in)
{
    RelationalLabel out;
    if (in.identity.rootPc < 0 || in.nextRootPc < 0) {
        return out;  // no chord / no resolution target — the applied label cannot fire
    }

    using namespace relational_detail;

    // SUBSUME the dormant tonicizationlabeler (its chromatic-leading-tone guard kept):
    // run its per-pair classification over [this chord → the next chord's root]. This is
    // REUSE, not a re-implementation — the one owned L5 applied emitter delegates to the
    // existing guarded labeler; at Phase 5d the labeler retires INTO this emitter. It
    // handles the raised-secondary-leading-tone applied chords (V/V, V7/V, viiø7/V, …,
    // and the plain-triad V/x the inline formatRomanNumeral path drops).
    std::vector<TonicizationRegionInput> pair(2);
    TonicizationRegionInput& a = pair[0];
    a.rootPc = in.identity.rootPc;
    a.quality = in.identity.quality;
    a.hasMinorSeventh = hasExtension(in.identity.extensions, Extension::MinorSeventh);
    a.hasDiminishedSeventh = hasExtension(in.identity.extensions, Extension::DiminishedSeventh);
    a.pitchClassMask = in.pitchClassMask;
    a.keyTonicPc = in.keyTonicPc;
    a.keyIsMajor = (in.keyMode == KeySigMode::Ionian);  // unused by the labeler; set for fidelity
    a.keySignatureFifths = in.keyFifths;
    pair[1].rootPc = in.nextRootPc;  // the target d (the labeler reads only b.rootPc)

    const std::vector<TonicizationLabel> labels = labelTonicizations(pair);
    const TonicizationLabel& tl = labels[0];
    if (tl.isApplied) {
        out.role = RelationalRole::AppliedSecondary;
        out.label = tl.label;
        out.targetDegree = tl.targetDegree;
        out.targetPc = tl.targetPc;
        return out;
    }

    // BROADEN the applied trigger to the chords the labeler's raised-secondary-leading-
    // tone guard drops, by the GENERAL chromaticism test §5.6 always implied: an applied
    // dominant- OR leading-tone-function chord of a non-tonic diatonic degree that
    // contains AT LEAST ONE TONE FOREIGN to the home-key collection (§5.6 amended
    // 2026-06-29). The raised secondary LT (V/V — the labeler), the ♭7̂ (V7/IV), and the
    // secondary-diminished's foreign tone (viio/IV, viio7/ii) are all INSTANCES of the one
    // test — NOT a closed enumeration; this generalizes the prior two named ♭7̂/raised-LT
    // forms so applied cases are not discovered one at a time. REUSE the production
    // formatRomanNumeral inline applied path for the string (it already emits V7/x and
    // viio/x) — no second formatter (§3); we broaden WHICH chords reach the emitter, gated
    // by the foreign-tone test.
    const ChordIdentity& id = in.identity;

    // The chord's FUNCTION class + the relation to its target degree (§5.6):
    //   • DOMINANT-function (major triad / dominant seventh): root a perfect fifth ABOVE
    //     the target — rootPc == target + 7;
    //   • LEADING-TONE-function (diminished / half-diminished, with or without a seventh):
    //     root a semitone BELOW the target — rootPc == target + 11 (target a semitone above).
    const bool isDominantFn = (id.quality == ChordQuality::Major);
    const bool isLeadingToneFn = (id.quality == ChordQuality::Diminished
                                  || id.quality == ChordQuality::HalfDiminished);
    const bool dominantRel = isDominantFn && id.rootPc == normalizePc(in.nextRootPc + 7);
    const bool leadingToneRel = isLeadingToneFn && id.rootPc == normalizePc(in.nextRootPc + 11);
    if (!dominantRel && !leadingToneRel) {
        return out;  // role None — neither an applied dominant nor an applied leading-tone chord
    }

    // The target degree must be a non-tonic DIATONIC degree of the home key (so it can be
    // named as a plain numeral; a tonic target is V7→I / viio→I, not applied).
    const int targetDegree = region::diatonicDegreeForRootPc(in.nextRootPc, in.keyFifths, in.keyMode);
    if (targetDegree <= 0) {
        return out;  // tonic target (not applied) or a chromatic target (out of slice)
    }

    // THE GENERAL CHROMATICISM TEST (§5.6) — the trigger's necessary condition AND its
    // false-positive guard, in one: the chord must contain at least one tone foreign to the
    // home-key collection. A chord FULLY DIATONIC to the home key is never applied — so the
    // natural-minor VII7→III (its ♭7̂ diatonic) stays the diatonic numeral, NOT V7/III, and
    // the diatonic ii°→III in minor stays ii°, NOT viio/III. (This is what the prior raised-
    // leading-tone-only guard wrongly enforced, dropping the chromatic ♭7̂ V7/IV and the
    // secondary-diminished viio/IV whose own foreign tone — not the target's leading tone —
    // carries the chromaticism.)
    const uint16_t collMask = diatonicMaskFromFifths(in.keyFifths);
    const bool hasForeignTone = (in.pitchClassMask & static_cast<uint16_t>(~collMask)) != 0;
    if (!hasForeignTone) {
        return out;  // fully diatonic — a genuinely diatonic chord, not applied
    }

    ChordAnalysisResult r = makeResult(in, /*nextRootPc=*/in.nextRootPc);
    const std::string label = ChordSymbolFormatter::formatRomanNumeral(r);
    // The reused emitter produces an applied label (containing the "/<degree>" separator)
    // for a dominant SEVENTH (V7/x) or a diminished/half-diminished chord (viio/x); a plain
    // dominant TRIAD falls through to its base numeral. Confirm an applied label was
    // produced before committing the role — defensive (a non-applied label is carried as
    // role None, never re-derived here).
    if (label.find('/') == std::string::npos) {
        return out;
    }
    out.role = RelationalRole::AppliedSecondary;
    out.label = label;
    out.targetDegree = targetDegree;
    out.targetPc = in.nextRootPc;
    return out;
}

// ── The §5.6 precedence classifier ────────────────────────────────────────────

RelationalLabel classifyRelationalLabel(const RelationalLabelInput& in)
{
    using namespace relational_detail;

    // FIXED PRECEDENCE, first match wins (§5.6).
    if (RelationalLabel a6 = tryAugmentedSixth(in); a6.role != RelationalRole::None) {
        return a6;
    }
    if (RelationalLabel neap = tryNeapolitan(in); neap.role != RelationalRole::None) {
        return neap;
    }
    if (RelationalLabel app = emitAppliedLabel(in); app.role != RelationalRole::None) {
        return app;
    }
    if (RelationalLabel mix = tryModalMixture(in); mix.role != RelationalRole::None) {
        return mix;
    }

    // No relational role — a plain diatonic chord; carry the base numeral so the caller
    // always receives a complete RN (the label is additive over the base RN, §7).
    RelationalLabel out;
    out.role = RelationalRole::None;
    out.label = baseNumeral(in);
    return out;
}

} // namespace mu::composing::analysis
