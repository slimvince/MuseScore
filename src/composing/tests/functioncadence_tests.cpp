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

// functioncadence_tests.cpp — Architectural Layer 5 (FUNCTION), Phase 5c Step 2.
//
// Oracle-asserted against known music theory (NOT echoes of the analyzer): the
// §5.2 key-agnostic event-pair cadence detector. The §4 build obligations:
//   • a root-position V7→I (both root position) is a PAC; the same with an inverted
//     tonic is an IAC (by INVERSION, not the top voice);
//   • a iv6→V minor-mode pair with the semitone bass is a Phrygian half;
//   • a cadential V→vi is deceptive;
//   • the cadential-6/4 collapse reads the bass as 5̂→1̂ (and the 6/4 never registers
//     as a tonic arrival);
//   • a passing I→IV is NOT a cadence (the false positive the old leading-tone-
//     PRESENCE test hit — the corrected resolution + genuine-dominant tests reject it).
// Spec: cowork_layer5_function_design.md §5.2 + §5.0.

#include <gtest/gtest.h>

#include "composing/analysis/function/functioncadence.h"

using namespace mu::composing::analysis;

namespace {

// Pitch classes for readability.
constexpr int C = 0, Cs = 1, D = 2, Eb = 3, E = 4, F = 5, Fs = 6, G = 7, Gs = 8,
              A = 9, Bb = 10, B = 11;

// One sounding note: voice id + pitch class (placed in a fixed octave — register is
// irrelevant; only the voice id pairs a note across the boundary).
CadenceVoiceNote n(int voice, int pc)
{
    CadenceVoiceNote x;
    x.voice = voice;
    x.pitch = pc + 60;
    return x;
}

CadenceEvent ev(int rootPc, ChordQuality quality, int bassPc,
                std::vector<CadenceVoiceNote> notes, bool endsPhrase, int startTick,
                double metricWeight = 1.0)
{
    CadenceEvent e;
    e.rootPc = rootPc;
    e.quality = quality;
    e.bassPc = bassPc;
    e.notes = std::move(notes);
    e.endsPhrase = endsPhrase;
    e.startTick = startTick;
    e.metricWeight = metricWeight;
    return e;
}

// Common chords (SATB-ish; the leading tone B is placed in voice 3 so its resolution
// to C in voice 3 at the tonic is a same-voice event).
CadenceEvent iiDm(int tick)  { return ev(D, ChordQuality::Minor, D, { n(0, D), n(1, F), n(2, A) }, false, tick, 0.7); }
CadenceEvent IVF(int tick)   { return ev(F, ChordQuality::Major, F, { n(0, F), n(1, A), n(2, C) }, false, tick, 0.7); }
CadenceEvent G7(int tick, bool endsPhrase = false)
{
    // G–B–D–F: B (leading tone) in voice 3, F (minor seventh) in voice 2.
    return ev(G, ChordQuality::Major, G, { n(0, G), n(1, D), n(2, F), n(3, B) }, endsPhrase, tick, 1.0);
}
CadenceEvent CmajRoot(int tick, bool endsPhrase)
{
    // C–E–G, soprano C in voice 3 (the B→C resolution target).
    return ev(C, ChordQuality::Major, C, { n(0, C), n(1, E), n(2, G), n(3, C) }, endsPhrase, tick, 1.0);
}

} // namespace

// ── §4: PAC vs IAC by inversion ───────────────────────────────────────────────

TEST(FunctionCadence, RootPositionV7ToIIsPerfectAuthentic)
{
    // ii → V7 → I, all root position. The V7→I pair is a PAC: bass 5̂→1̂, the leading
    // tone resolves (B→C, voice 3), and the dominant is genuine (the minor seventh F).
    auto cs = detectFunctionalCadences({ iiDm(0), G7(480), CmajRoot(960, true) });
    ASSERT_EQ(cs.size(), 1u);
    EXPECT_EQ(cs[0].type, FunctionalCadenceType::PerfectAuthentic);
    EXPECT_EQ(cs[0].tonicPc, C);
    EXPECT_TRUE(cs[0].bassFiveToOne);
    EXPECT_TRUE(cs[0].leadingToneResolves);
    EXPECT_TRUE(cs[0].genuineDominant);
    EXPECT_EQ(cs[0].arrivalTick, 960);
}

TEST(FunctionCadence, InvertedTonicIsImperfectAuthenticByInversionNotTopVoice)
{
    // Same V7, but the tonic arrives in FIRST INVERSION (bass E). The top voice still
    // arrives on C (soprano C in voice 3) — yet the call is IAC, made on the bass-
    // derived inversion, never the top voice (§5.2 amendment).
    CadenceEvent iFirstInv = ev(C, ChordQuality::Major, E, { n(0, E), n(1, G), n(2, C), n(3, C) }, true, 960);
    auto cs = detectFunctionalCadences({ iiDm(0), G7(480), iFirstInv });
    ASSERT_EQ(cs.size(), 1u);
    EXPECT_EQ(cs[0].type, FunctionalCadenceType::ImperfectAuthentic);
    EXPECT_EQ(cs[0].tonicPc, C);
    EXPECT_FALSE(cs[0].bassFiveToOne);          // inverted tonic — bass does not read 5̂→1̂
    EXPECT_TRUE(cs[0].leadingToneResolves);
}

TEST(FunctionCadence, ViioSubstitutionIsImperfectAuthentic)
{
    // viio6-style leading-tone chord standing in for the dominant: Bdim → C. No V root
    // motion, so it is IAC, not PAC — admitted by the resolving tritone (B→C, F→E).
    CadenceEvent viio = ev(B, ChordQuality::Diminished, B, { n(0, B), n(1, D), n(2, F) }, false, 480);
    CadenceEvent c = ev(C, ChordQuality::Major, C, { n(0, C), n(1, G), n(2, E) }, true, 960);
    auto cs = detectFunctionalCadences({ IVF(0), viio, c });
    ASSERT_EQ(cs.size(), 1u);
    EXPECT_EQ(cs[0].type, FunctionalCadenceType::ImperfectAuthentic);
    EXPECT_EQ(cs[0].tonicPc, C);
    EXPECT_TRUE(cs[0].genuineDominant);          // the diminished tritone resolves
}

// ── §4: the cadential six-four collapse ───────────────────────────────────────

TEST(FunctionCadence, CadentialSixFourCollapsesAndBassReadsFiveToOne)
{
    // ii → I64 (C/G, bass 5̂) → V7 (G, root, same held bass) → I. The 6/4 is the
    // dominant's accented suspension; it must NOT register as a tonic arrival, and the
    // V7→I pair reads the cadential bass 5̂→1̂.
    CadenceEvent i64 = ev(C, ChordQuality::Major, G, { n(0, G), n(1, C), n(2, E) }, false, 480, 0.7);
    auto cs = detectFunctionalCadences({ iiDm(0), i64, G7(720), CmajRoot(960, true) });
    ASSERT_EQ(cs.size(), 1u);
    EXPECT_EQ(cs[0].type, FunctionalCadenceType::PerfectAuthentic);
    EXPECT_TRUE(cs[0].sixFourCollapsed);
    EXPECT_TRUE(cs[0].bassFiveToOne);
    EXPECT_EQ(cs[0].tonicPc, C);
    // The 6/4 at tick 480 is never a tonic arrival.
    for (const auto& c : cs) {
        EXPECT_NE(c.arrivalTick, 480);
    }
}

TEST(FunctionCadence, SecondInversionTonicNeverRegistersAsArrival)
{
    // A bare ii → I64 ending a phrase must NOT read as an authentic cadence — a
    // second-inversion tonic spelling never registers as a tonic arrival (§5.2).
    CadenceEvent i64 = ev(C, ChordQuality::Major, G, { n(0, G), n(1, C), n(2, E) }, true, 480);
    auto cs = detectFunctionalCadences({ G7(0), i64 });
    for (const auto& c : cs) {
        EXPECT_NE(c.type, FunctionalCadenceType::PerfectAuthentic);
        EXPECT_NE(c.type, FunctionalCadenceType::ImperfectAuthentic);
    }
}

// ── §4: Phrygian half ─────────────────────────────────────────────────────────

TEST(FunctionCadence, Iv6ToVWithSemitoneBassIsPhrygianHalf)
{
    // A minor: iv6 (Dm/F, bass b6̂ = F) → V (E major, bass 5̂ = E), the bass descending
    // a semitone F→E. A Phrygian half cadence, held in minor mode.
    CadenceEvent iv6 = ev(D, ChordQuality::Minor, F, { n(0, F), n(1, A), n(2, D) }, false, 0, 0.7);
    CadenceEvent v = ev(E, ChordQuality::Major, E, { n(0, E), n(1, Gs), n(2, B) }, true, 480);
    auto cs = detectFunctionalCadences({ iv6, v });
    ASSERT_EQ(cs.size(), 1u);
    EXPECT_EQ(cs[0].type, FunctionalCadenceType::PhrygianHalf);
    EXPECT_EQ(cs[0].tonicPc, A);
    EXPECT_TRUE(cs[0].minorMode);
}

// ── §4: deceptive ─────────────────────────────────────────────────────────────

TEST(FunctionCadence, CadentialVToViIsDeceptive)
{
    // ii → V7 → vi (Am). The dominant is set up to cadence but arrives on the
    // submediant: a deceptive cadence whose tonic vote is still for C.
    CadenceEvent vi = ev(A, ChordQuality::Minor, A, { n(0, A), n(1, E), n(2, C), n(3, C) }, true, 960);
    auto cs = detectFunctionalCadences({ iiDm(0), G7(480), vi });
    ASSERT_EQ(cs.size(), 1u);
    EXPECT_EQ(cs[0].type, FunctionalCadenceType::Deceptive);
    EXPECT_EQ(cs[0].tonicPc, C);
    EXPECT_FALSE(cs[0].minorMode);               // vi ⇒ a major key
}

// ── §4: a passing I→IV is NOT a cadence ───────────────────────────────────────

TEST(FunctionCadence, PassingIToIVIsNotACadence)
{
    // I → IV → V7 → I, a single phrase. The mid-phrase I→IV (the very motion the old
    // leading-tone-PRESENCE test false-flagged) produces no cadence; only the
    // phrase-final V7→I PAC is found.
    CadenceEvent I = ev(C, ChordQuality::Major, C, { n(0, C), n(1, E), n(2, G) }, false, 0);
    CadenceEvent IVmid = ev(F, ChordQuality::Major, F, { n(0, F), n(1, A), n(2, C) }, false, 480, 0.7);
    auto cs = detectFunctionalCadences({ I, IVmid, G7(720), CmajRoot(960, true) });
    ASSERT_EQ(cs.size(), 1u);
    EXPECT_EQ(cs[0].type, FunctionalCadenceType::PerfectAuthentic);
    EXPECT_EQ(cs[0].arrivalTick, 960);
    for (const auto& c : cs) {
        EXPECT_NE(c.arrivalTick, 480);           // the I→IV motion is not a cadence
    }
}

// ── The corrected genuine-dominant discriminator (the I→IV cure) ───────────────

TEST(FunctionCadence, GenuineDominantNeedsSeventhOrResolvingTritone)
{
    // A plain major triad (a tonic, or a bare V) is NOT a genuine dominant — no
    // seventh, no resolving tritone. This is what rejects I→IV even at a boundary.
    CadenceEvent Ctriad = ev(C, ChordQuality::Major, C, { n(0, C), n(1, E), n(2, G) }, false, 0);
    CadenceEvent Ftriad = ev(F, ChordQuality::Major, F, { n(0, F), n(1, A), n(2, C) }, true, 480);
    EXPECT_FALSE(isGenuineDominant(Ctriad, Ftriad, /*tonicPc=*/F));

    // A dominant seventh IS genuine (by the seventh).
    EXPECT_TRUE(dominantSeventhPresent(G7(0)));
    EXPECT_TRUE(isGenuineDominant(G7(0), CmajRoot(480, false), /*tonicPc=*/C));

    // A viio diminished chord whose tritone resolves IS genuine (B→C, F→E).
    CadenceEvent viio = ev(B, ChordQuality::Diminished, B, { n(0, B), n(1, D), n(2, F) }, false, 0);
    CadenceEvent c = ev(C, ChordQuality::Major, C, { n(0, C), n(1, G), n(2, E) }, true, 480);
    EXPECT_FALSE(dominantSeventhPresent(viio));   // no minor seventh on a viio triad
    EXPECT_TRUE(isGenuineDominant(viio, c, /*tonicPc=*/C));
}

// ── The corrected leading-tone RESOLUTION event (not presence) ────────────────

TEST(FunctionCadence, LeadingToneResolvesIsAnEventNotPresence)
{
    // Dominant with the leading tone B in voice 3.
    CadenceEvent dom = ev(G, ChordQuality::Major, G, { n(0, G), n(1, D), n(2, F), n(3, B) }, false, 0);

    // Resolves: B → C in the SAME voice (voice 3).
    CadenceEvent arrResolve = ev(C, ChordQuality::Major, C, { n(0, C), n(1, E), n(2, G), n(3, C) }, true, 480);
    EXPECT_TRUE(leadingToneResolves(dom, arrResolve, C));

    // Present but NOT resolving: B is sustained / leaps to D in voice 3 (no 7̂→1̂).
    CadenceEvent arrNoResolve = ev(C, ChordQuality::Major, C, { n(0, C), n(1, E), n(2, G), n(3, D) }, true, 480);
    EXPECT_FALSE(leadingToneResolves(dom, arrNoResolve, C));

    // Resolves to C but in a DIFFERENT voice (voice 0, not voice 3): not a same-voice
    // resolution, so the event does not fire.
    CadenceEvent arrWrongVoice = ev(C, ChordQuality::Major, C, { n(0, C), n(1, E), n(2, G), n(3, E) }, true, 480);
    EXPECT_FALSE(leadingToneResolves(dom, arrWrongVoice, C));
}

// ── Inversion / six-four structural predicates ────────────────────────────────

TEST(FunctionCadence, InversionPredicates)
{
    EXPECT_TRUE(isRootPosition(ev(G, ChordQuality::Major, G, {}, false, 0)));
    EXPECT_FALSE(isRootPosition(ev(C, ChordQuality::Major, E, {}, false, 0)));     // first inversion

    EXPECT_TRUE(isSecondInversionTonicTriad(ev(C, ChordQuality::Major, G, {}, false, 0)));   // C/G — bass = fifth
    EXPECT_FALSE(isSecondInversionTonicTriad(ev(C, ChordQuality::Major, E, {}, false, 0)));  // C/E — first inversion
    EXPECT_FALSE(isSecondInversionTonicTriad(ev(C, ChordQuality::Major, C, {}, false, 0)));  // root position
}

// ── Plagal at a phrase boundary (lower confidence by rule) ────────────────────

TEST(FunctionCadence, SubdominantToTonicIsPlagal)
{
    // IV → I at a phrase boundary, no intervening dominant: a plagal cadence.
    CadenceEvent c = ev(C, ChordQuality::Major, C, { n(0, C), n(1, E), n(2, G) }, true, 480);
    auto cs = detectFunctionalCadences({ IVF(0), c });
    ASSERT_EQ(cs.size(), 1u);
    EXPECT_EQ(cs[0].type, FunctionalCadenceType::Plagal);
    EXPECT_EQ(cs[0].tonicPc, C);
}

// ── The §5.2 weighted tonic vote ──────────────────────────────────────────────

TEST(FunctionCadence, TonicVoteDirectionAndPerTypeDiscount)
{
    // A PAC (full evidence + phrase salience) outvotes a half cadence at the SAME
    // salience (no evidence cues + the half lower-confidence discount). Direction
    // fixed; weights are firewall seeds.
    auto pac = detectFunctionalCadences({ iiDm(0), G7(480), CmajRoot(960, true) });
    ASSERT_EQ(pac.size(), 1u);

    // IV → V (a plain half cadence at the same phrase salience).
    CadenceEvent v = ev(G, ChordQuality::Major, G, { n(0, G), n(1, B), n(2, D) }, true, 480);
    auto half = detectFunctionalCadences({ IVF(0), v });
    ASSERT_EQ(half.size(), 1u);
    EXPECT_EQ(half[0].type, FunctionalCadenceType::Half);

    EXPECT_GT(pac[0].tonicVote, half[0].tonicVote);
    EXPECT_GT(half[0].tonicVote, 0.0);           // a half still casts a (discounted) vote

    // An admitted cadence votes for the right tonic; the half's dominant G implies C.
    EXPECT_EQ(half[0].tonicPc, C);
}
