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

// functionrelationallabel_tests.cpp — Architectural Layer 5 (FUNCTION), Phase 5c Step 5.
//
// Oracle-asserted against known music theory (§5.6): the four relational labels on
// their defining triggers, tested in the FIXED PRECEDENCE (augmented sixth →
// Neapolitan → applied/secondary → modal mixture, first match wins; modal mixture is
// the residual). An applied chord emits V/x with the correct target degree in the
// LOCAL key; a lowered-second major triad → bII6; an It/Fr/Ger is selected by the
// degree + (for Ger vs V7) the notated SPELLING (read through spellingview); a
// borrowed quality-altering degree matching none → modal mixture; an altered chord
// matching multiple triggers takes the FIRST in the precedence.
// Spec: cowork_layer5_function_design.md §5.6.

#include <gtest/gtest.h>

#include "composing/analysis/function/functionrelationallabel.h"
#include "composing/analysis/chord/chordanalyzer.h"   // ChordQuality, Extension, setExtension

using namespace mu::composing::analysis;

namespace {

using Q = ChordQuality;
using E = Extension;
using R = RelationalRole;

// ø U+00F8 (the half-diminished glyph formatRomanNumeral emits).
const std::string OE = "\xc3\xb8";

// Pitch classes (C major context).
constexpr int C = 0, Db = 1, D = 2, Eb = 3, F = 5, Fs = 6, Gb = 6, G = 7, Ab = 8, B = 11;

// MuseScore Tpc values (TPC_C = 14; ±1 tpc = ±1 fifth). The spellings the aug6 read
// distinguishes: F# (sharp side, tpc 20) vs Gb (flat side, tpc 8).
constexpr int TPC_C = 14, TPC_Eb = 11, TPC_F = 13, TPC_Ab = 10, TPC_Bb = 12,
              TPC_D = 16, TPC_Fs = 20, TPC_Gb = 8, TPC_A = 17;

// 12-bit pitch-class mask from a list of pitch classes.
uint16_t pcMask(std::initializer_list<int> pcs)
{
    uint16_t m = 0;
    for (int pc : pcs) {
        m |= static_cast<uint16_t>(1u << (((pc % 12) + 12) % 12));
    }
    return m;
}

// A relational-label input in C major (keyFifths 0, Ionian, tonic pc 0).
RelationalLabelInput cMajor()
{
    RelationalLabelInput in;
    in.keyFifths = 0;
    in.keyMode = KeySigMode::Ionian;
    in.keyTonicPc = 0;
    return in;
}

// Set the chord identity (root/bass pc + root tpc + quality + extensions).
void setChord(RelationalLabelInput& in, int rootPc, int rootTpc, int bassPc, Q quality,
              std::initializer_list<E> exts = {})
{
    in.identity.rootPc = rootPc;
    in.identity.rootTpc = rootTpc;
    in.identity.bassPc = bassPc;
    in.identity.bassTpc = -1;
    in.identity.quality = quality;
    for (E e : exts) {
        setExtension(in.identity.extensions, e);
    }
}

} // namespace

// ── §5.6 applied/secondary: V/x with the correct target degree (local key) ─────

TEST(FunctionRelationalLabel, AppliedDominantTriadTargetDegree)
{
    // D major triad resolving to G in C major = V/V (a plain-triad applied dominant,
    // which the inline formatRomanNumeral path drops but the unified emitter keeps).
    RelationalLabelInput in = cMajor();
    setChord(in, D, TPC_D, D, Q::Major);
    in.nextRootPc = G;
    in.pitchClassMask = pcMask({ D, Fs, 9 /*A*/ });  // F# = the raised LT of the dominant
    const RelationalLabel out = classifyRelationalLabel(in);
    EXPECT_EQ(out.role, R::AppliedSecondary);
    EXPECT_EQ(out.label, "V/V");
    EXPECT_EQ(out.targetDegree, 4);   // the dominant degree (0-indexed)
    EXPECT_EQ(out.targetPc, G);
}

TEST(FunctionRelationalLabel, AppliedDominantSeventhTargetDegree)
{
    // D7 resolving to G = V7/V.
    RelationalLabelInput in = cMajor();
    setChord(in, D, TPC_D, D, Q::Major, { E::MinorSeventh });
    in.nextRootPc = G;
    in.pitchClassMask = pcMask({ D, Fs, 9, C });
    const RelationalLabel out = classifyRelationalLabel(in);
    EXPECT_EQ(out.role, R::AppliedSecondary);
    EXPECT_EQ(out.label, "V7/V");
    EXPECT_EQ(out.targetDegree, 4);
}

TEST(FunctionRelationalLabel, AppliedLeadingToneSeventhTargetDegree)
{
    // F#ø7 resolving to G = viiø7/V (the secondary leading-tone chord of the dominant).
    RelationalLabelInput in = cMajor();
    setChord(in, Fs, TPC_Fs, Fs, Q::HalfDiminished, { E::MinorSeventh });
    in.nextRootPc = G;
    const RelationalLabel out = classifyRelationalLabel(in);
    EXPECT_EQ(out.role, R::AppliedSecondary);
    EXPECT_EQ(out.label, "vii" + OE + "7/V");
    EXPECT_EQ(out.targetDegree, 4);
}

TEST(FunctionRelationalLabel, AppliedRequiresChromaticLeadingToneGuard)
{
    // A plain dominant→tonic (G major → C) is NOT a tonicization: the target is the
    // tonic and its "leading tone" is diatonic. The kept chromatic-LT guard rejects it.
    RelationalLabelInput in = cMajor();
    setChord(in, G, 15 /*TPC_G*/, G, Q::Major, { E::MinorSeventh });
    in.nextRootPc = C;
    in.pitchClassMask = pcMask({ G, B, D, F });
    const RelationalLabel out = classifyRelationalLabel(in);
    EXPECT_NE(out.role, R::AppliedSecondary);  // V7 → I is not applied
}

// ── §5.6 Neapolitan: a lowered-second first-inversion major triad → bII6 ───────

TEST(FunctionRelationalLabel, NeapolitanFirstInversion)
{
    // Db major triad (b2̂) in first inversion (bass = F, the third) in C major → bII6.
    RelationalLabelInput in = cMajor();
    setChord(in, Db, 9 /*TPC_Db*/, /*bass=*/F, Q::Major);
    const RelationalLabel out = classifyRelationalLabel(in);
    EXPECT_EQ(out.role, R::Neapolitan);
    EXPECT_EQ(out.label, "bII6");
}

// ── §5.6 augmented sixth: selected by degree + (Ger vs V7) the notated spelling ─

TEST(FunctionRelationalLabel, ItalianSixthBySpelling)
{
    // Ab-C-F# (no fifth, no second) in C major = It+6.
    RelationalLabelInput in = cMajor();
    setChord(in, Ab, TPC_Ab, Ab, Q::Major);
    in.noteTpcs = { TPC_Ab, TPC_C, TPC_Fs };  // F# = the augmented-sixth spelling
    const RelationalLabel out = classifyRelationalLabel(in);
    EXPECT_EQ(out.role, R::AugmentedSixth);
    EXPECT_EQ(out.label, "It+6");
    EXPECT_TRUE(out.spellingConsulted);
    EXPECT_TRUE(out.spelledAsAugSixth);
}

TEST(FunctionRelationalLabel, FrenchSixthBySpelling)
{
    // Ab-C-D-F# in C major = Fr+6 (the second degree spelled sharp = SharpEleventh).
    RelationalLabelInput in = cMajor();
    setChord(in, Ab, TPC_Ab, Ab, Q::Major, { E::SharpEleventh });
    in.noteTpcs = { TPC_Ab, TPC_C, TPC_D, TPC_Fs };
    const RelationalLabel out = classifyRelationalLabel(in);
    EXPECT_EQ(out.role, R::AugmentedSixth);
    EXPECT_EQ(out.label, "Fr+6");
}

TEST(FunctionRelationalLabel, GermanSixthBySpelling)
{
    // Ab-C-Eb-F# in C major = Ger+6 (the perfect fifth Eb present = naturalFifthPresent).
    RelationalLabelInput in = cMajor();
    setChord(in, Ab, TPC_Ab, Ab, Q::Major);
    in.identity.naturalFifthPresent = true;
    in.noteTpcs = { TPC_Ab, TPC_C, TPC_Eb, TPC_Fs };
    const RelationalLabel out = classifyRelationalLabel(in);
    EXPECT_EQ(out.role, R::AugmentedSixth);
    EXPECT_EQ(out.label, "Ger+6");
    EXPECT_TRUE(out.spelledAsAugSixth);
}

TEST(FunctionRelationalLabel, GerVsV7SeparatedBySpelling)
{
    // The SAME pitch classes {Ab, C, Eb, F#/Gb}: spelled with Gb the top tone is a
    // MINOR SEVENTH (a dominant-seventh reading, Ab7), not an augmented sixth — the
    // aug6 label does NOT fire (§5.6 Ger6↔V7, the one spelling distinction). It falls
    // through to its base/borrowed reading (bVI7), never AugmentedSixth.
    RelationalLabelInput in = cMajor();
    setChord(in, Ab, TPC_Ab, Ab, Q::Major, { E::MinorSeventh });
    in.identity.naturalFifthPresent = true;
    in.noteTpcs = { TPC_Ab, TPC_C, TPC_Eb, TPC_Gb };  // Gb = the minor-seventh spelling
    const RelationalLabel out = classifyRelationalLabel(in);
    EXPECT_NE(out.role, R::AugmentedSixth);
    EXPECT_FALSE(out.spelledAsAugSixth);
    EXPECT_EQ(out.label, "bVI7");
}

// ── §5.6 modal mixture: the residual (a borrowed quality-altering degree) ──────

TEST(FunctionRelationalLabel, ModalMixtureBorrowedMinorSubdominant)
{
    // F minor (iv) in C major — a diatonic root (IV) with a borrowed minor quality.
    RelationalLabelInput in = cMajor();
    setChord(in, F, TPC_F, F, Q::Minor);
    const RelationalLabel out = classifyRelationalLabel(in);
    EXPECT_EQ(out.role, R::ModalMixture);
    EXPECT_EQ(out.label, "iv");
}

TEST(FunctionRelationalLabel, ModalMixtureBorrowedFlatSubmediant)
{
    // Ab major (bVI) in C major, NO augmented-sixth tone present — a chromatic root,
    // borrowed by construction. (With an aug6 tone it would be It/Ger+6 — see precedence.)
    RelationalLabelInput in = cMajor();
    setChord(in, Ab, TPC_Ab, Ab, Q::Major);
    in.noteTpcs = { TPC_Ab, TPC_C, TPC_Eb };  // a plain Ab triad — no +10 tone
    const RelationalLabel out = classifyRelationalLabel(in);
    EXPECT_EQ(out.role, R::ModalMixture);
    EXPECT_EQ(out.label, "bVI");
}

// ── §5.6 the fixed precedence (an altered chord matching several triggers) ─────

TEST(FunctionRelationalLabel, PrecedenceNeapolitanBeatsModalMixture)
{
    // A Db major triad (b2̂) matches BOTH the Neapolitan (a b2̂ major triad) and the
    // modal-mixture residual (a chromatic root) — the Neapolitan wins (it is earlier
    // in the precedence).
    RelationalLabelInput in = cMajor();
    setChord(in, Db, 9 /*TPC_Db*/, /*bass=*/F, Q::Major);
    const RelationalLabel out = classifyRelationalLabel(in);
    EXPECT_EQ(out.role, R::Neapolitan);
    EXPECT_EQ(out.label, "bII6");
}

TEST(FunctionRelationalLabel, PrecedenceAugmentedSixthBeatsModalMixture)
{
    // A Ger+6 (b6̂ major + aug6 spelling) matches BOTH the augmented sixth and the
    // modal-mixture residual (a b6̂ chromatic root) — the augmented sixth wins.
    RelationalLabelInput in = cMajor();
    setChord(in, Ab, TPC_Ab, Ab, Q::Major);
    in.identity.naturalFifthPresent = true;
    in.noteTpcs = { TPC_Ab, TPC_C, TPC_Eb, TPC_Fs };
    const RelationalLabel out = classifyRelationalLabel(in);
    EXPECT_EQ(out.role, R::AugmentedSixth);
    EXPECT_EQ(out.label, "Ger+6");
}

TEST(FunctionRelationalLabel, PrecedenceAppliedBeatsModalMixture)
{
    // A D major triad resolving to G matches BOTH the applied label (V/V) and the
    // modal-mixture residual (a major II where the diatonic ii is minor) — applied wins.
    RelationalLabelInput in = cMajor();
    setChord(in, D, TPC_D, D, Q::Major);
    in.nextRootPc = G;
    in.pitchClassMask = pcMask({ D, Fs, 9 });
    const RelationalLabel out = classifyRelationalLabel(in);
    EXPECT_EQ(out.role, R::AppliedSecondary);
    EXPECT_EQ(out.label, "V/V");
}

// ── role None: a plain diatonic chord carries the base numeral ─────────────────

TEST(FunctionRelationalLabel, PlainDiatonicChordIsNoneWithBaseNumeral)
{
    // G major (V) in C major — no relational role; the label is the plain base numeral.
    RelationalLabelInput in = cMajor();
    setChord(in, G, 15 /*TPC_G*/, G, Q::Major);
    const RelationalLabel out = classifyRelationalLabel(in);
    EXPECT_EQ(out.role, R::None);
    EXPECT_EQ(out.label, "V");
}

// ── the unified emitter (§3) is directly callable and keeps the guard ──────────

TEST(FunctionRelationalLabel, UnifiedAppliedEmitterDirectCall)
{
    // emitAppliedLabel() — the one owned applied/tonicization emitter — produces the
    // same V/V the classifier routes to, and returns None for a non-applied chord.
    RelationalLabelInput applied = cMajor();
    setChord(applied, D, TPC_D, D, Q::Major);
    applied.nextRootPc = G;
    applied.pitchClassMask = pcMask({ D, Fs, 9 });
    EXPECT_EQ(emitAppliedLabel(applied).label, "V/V");

    RelationalLabelInput notApplied = cMajor();
    setChord(notApplied, G, 15, G, Q::Major);
    notApplied.nextRootPc = -1;  // no resolution target
    EXPECT_EQ(emitAppliedLabel(notApplied).role, R::None);
}
