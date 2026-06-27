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

// ── Phase-5 round-2 cluster 3: chord/chordsymbolformatter.cpp branch backfill ──
//
// Oracle-asserted tests for previously-unhit branch directions in the three public
// formatters (formatSymbol / formatRomanNumeral / formatNashvilleNumber).  Each
// EXPECT asserts the EXACT rendered string the chord-symbol / Roman-numeral /
// Nashville convention requires, re-derived at source from music theory and the
// project's own ground-truth catalog (tests/data/chordanalyzer_catalog_jazz.musicxml,
// e.g. CMaj7#5 / C13#5 / CMaj9#5 / Cm9b5 / Cm11b5 / C7#5b9) — never an echo.
//
// Coverage was only the GAP-FINDER for which conventions were untested; the assertion
// is the convention, not the code's current output.  Branches reachable only by
// provably-impossible / defensive / synthetic inputs are documented in
// cc_backfill_formatter_report.md and intentionally NOT asserted here.
//
// SURFACED FINDING (rule 2 — reported, pinned as a labelled regression guard, also
// captured as a DISABLED_ correct-oracle below): German note spelling produces
// multi-letter bass names ("Ces" = Cb, "Fes" = Fb).  csfIsValidBassNoteName() only
// accepts a leading uppercase letter followed by '#'/'b', so it REJECTS "Ces"/"Fes"
// and the slash is dropped (e.g. German "C/Ces" renders as "C").  Flagged for Cowork.

#include <gtest/gtest.h>

#include <string>

#include "composing/analysis/chord/chordanalyzer.h"

#include "test_helpers.h"

using namespace mu::composing::analysis;

namespace {

using E  = Extension;
using Q  = ChordQuality;
using Sp = ChordSymbolFormatter::NoteSpelling;

// UTF-8 byte sequences for the non-ASCII glyphs the formatters emit.
const std::string OE  = "\xc3\xb8";       // ø  U+00F8  (half-diminished)
const std::string FL  = "\xe2\x99\xad";   // ♭  U+266D  (Nashville flat)
const std::string SH  = "\xe2\x99\xaf";   // ♯  U+266F  (Nashville sharp)

// Build a result with a quality + extension flags.  Root/bass default to C (pc 0),
// TPCs unknown — so the rendered root is "C" and (bass == root) suppresses any slash.
ChordAnalysisResult mk(Q quality, std::initializer_list<E> exts = {})
{
    ChordAnalysisResult r;
    r.identity.quality = quality;
    r.identity.rootPc  = 0;
    r.identity.bassPc  = 0;
    r.identity.rootTpc = -1;
    r.identity.bassTpc = -1;
    for (E e : exts) {
        setExtension(r.identity.extensions, e);
    }
    return r;
}

std::string sym(const ChordAnalysisResult& r, int keyFifths = 0, Sp spelling = Sp::Standard)
{
    ChordSymbolFormatter::Options opts;
    opts.spelling = spelling;
    return ChordSymbolFormatter::formatSymbol(r, keyFifths, opts);
}

std::string rn(const ChordAnalysisResult& r)
{
    return ChordSymbolFormatter::formatRomanNumeral(r);
}

std::string nash(const ChordAnalysisResult& r, int keyFifths = 0)
{
    return ChordSymbolFormatter::formatNashvilleNumber(r, keyFifths);
}

// A root-only result for spelling tests: bass mirrors root (no slash), quality Major,
// no extensions (empty suffix), so the rendered symbol is exactly the root name.
ChordAnalysisResult root(int rootPc, int rootTpc)
{
    ChordAnalysisResult r = mk(Q::Major, {});
    r.identity.rootPc  = rootPc;
    r.identity.rootTpc = rootTpc;
    r.identity.bassPc  = rootPc;
    r.identity.bassTpc = rootTpc;
    return r;
}

} // namespace

// ═════════════════════════════════════════════════════════════════════════════
//  csfPitchClassNameFromTpc — enharmonic root spelling (formatSymbol root name)
// ═════════════════════════════════════════════════════════════════════════════

// Cb spelling: pc 11 authored with a double-flat-range TPC is rendered "Cb" (German
// "Ces"), since the standard 12-name tables map pc 11 → "B".  TPC 7 = MuseScore
// internal Cb, TPC 8 = +1 test encoding.  (L108)
TEST(Composing_ChordSymbolFormatterBranch, RootName_Cb_BothTpcEncodings_AndGerman)
{
    EXPECT_EQ(sym(root(/*pc=*/11, /*tpc=*/7)), "Cb");   // internal encoding
    EXPECT_EQ(sym(root(/*pc=*/11, /*tpc=*/8)), "Cb");   // +1 test encoding
    EXPECT_EQ(sym(root(11, 7), 0, Sp::German), "Ces");  // German flat spelling
}

// Fb spelling: pc 4 authored with a double-flat-range TPC renders "Fb" (German
// "Fes"); the standard tables map pc 4 → "E".  TPC 6 internal, 7 = +1 encoding.  (L109)
TEST(Composing_ChordSymbolFormatterBranch, RootName_Fb_PlusOneEncoding_AndGerman)
{
    EXPECT_EQ(sym(root(/*pc=*/4, /*tpc=*/7)), "Fb");    // +1 encoding (tpc==7 arm)
    EXPECT_EQ(sym(root(4, 6), 0, Sp::German), "Fes");   // German flat spelling
}

// A# normalization: a sharp-authored pc 10 (A#, TPC 24) below 5 sharps is the jazz/pop
// chord-symbol "Bb"; at 5+ sharps (B major) the composer's A# is honored.  German maps
// Bb → "B".  (L134/L136)
TEST(Composing_ChordSymbolFormatterBranch, RootName_ASharp_NormalizesToBb_UnlessFiveSharps)
{
    EXPECT_EQ(sym(root(/*pc=*/10, /*tpc=*/24), /*keyFifths=*/0), "Bb");  // <5 sharps → Bb
    EXPECT_EQ(sym(root(10, 24), /*keyFifths=*/5), "A#");                 // ≥5 sharps → A#
    EXPECT_EQ(sym(root(10, 24), 0, Sp::German), "B");                   // German Bb → "B"
}

// G# is never flattened: a sharp-authored pc 8 (G#, TPC 22) is honored as the leading
// tone / V-of-V third in the key-signature-ambiguous slots G major (+1) and D major
// (+2).  (L141 / L144)
TEST(Composing_ChordSymbolFormatterBranch, RootName_GSharp_HonoredAtPlusOneAndPlusTwoSharps)
{
    EXPECT_EQ(sym(root(/*pc=*/8, /*tpc=*/22), /*keyFifths=*/1), "G#");  // A-melodic-minor slot
    EXPECT_EQ(sym(root(8, 22), /*keyFifths=*/2), "G#");                 // D major V/V slot
}

// Very-flat keys: B natural (pc 11, internal TPC 19) in 5+ flats renders Cb (German
// "Ces"); E natural (pc 4, internal TPC 18) in 6+ flats renders Fb (German "Fes").
// (L187/L188 and L189/L190)
TEST(Composing_ChordSymbolFormatterBranch, RootName_CbFb_VeryFlatKeys_InternalTpc_AndGerman)
{
    EXPECT_EQ(sym(root(/*pc=*/11, /*tpc=*/19), /*keyFifths=*/-5), "Cb");   // B♮ → Cb (5♭)
    EXPECT_EQ(sym(root(11, 19), -5, Sp::German), "Ces");
    EXPECT_EQ(sym(root(/*pc=*/4,  /*tpc=*/18), /*keyFifths=*/-6), "Fb");   // E♮ → Fb (6♭)
    EXPECT_EQ(sym(root(4, 18), -6, Sp::German), "Fes");
    // A non-E/non-B root in a 6-flat key falls through the very-flat guards to the
    // ordinary flat-key name (G, TPC 15).  (L189 pc!=4 false-arm)
    EXPECT_EQ(sym(root(/*pc=*/7, /*tpc=*/15), /*keyFifths=*/-6), "G");
}

// ═════════════════════════════════════════════════════════════════════════════
//  csfQualitySuffix — quality + extension chord-symbol suffixes
// ═════════════════════════════════════════════════════════════════════════════

// 6/9 chords on suspended triads: a sus2 with added 6th + 9th is "sus269"; a sus4 is
// "sus69" (the catalog 6/9 convention extended over the suspended qualities).  (L206/L207)
TEST(Composing_ChordSymbolFormatterBranch, Suffix_SixNine_SuspendedQualities)
{
    EXPECT_EQ(sym(mk(Q::Suspended2, {E::SixNine})), "Csus269");
    EXPECT_EQ(sym(mk(Q::Suspended4, {E::SixNine})), "Csus69");
}

// Maj7♭9: a major-seventh chord whose only ninth is a flat ninth renders "Maj7b9".  (L227)
TEST(Composing_ChordSymbolFormatterBranch, Suffix_Maj7FlatNine)
{
    EXPECT_EQ(sym(mk(Q::Major, {E::MajorSeventh, E::FlatNinth})), "CMaj7b9");
}

// add(♭9)/add(♯9): a major triad (no 7th) with a single altered ninth uses "add"
// notation — "addb9" / "add#9".  (L259)
TEST(Composing_ChordSymbolFormatterBranch, Suffix_MajorAddAlteredNinth)
{
    EXPECT_EQ(sym(mk(Q::Major, {E::FlatNinth})),  "Caddb9");
    EXPECT_EQ(sym(mk(Q::Major, {E::SharpNinth})), "Cadd#9");
}

// mMaj7add13: a minor-major-seventh carrying a 13th but no 9th names the added 13th
// explicitly ("Maj13" implies a 9th).  (L272 false-arm)
TEST(Composing_ChordSymbolFormatterBranch, Suffix_MinorMaj7Add13)
{
    EXPECT_EQ(sym(mk(Q::Minor, {E::MajorSeventh, E::NaturalThirteenth})), "CmMaj7add13");
}

// m7♯9: a minor-seventh with a (single) sharp ninth renders "m7#9".  (L288 false /
// L289 true — the b9-absent, #9-present arms.)
TEST(Composing_ChordSymbolFormatterBranch, Suffix_MinorSeventhSharpNine)
{
    EXPECT_EQ(sym(mk(Q::Minor, {E::MinorSeventh, E::SharpNinth})), "Cm7#9");
}

// madd(♯9): a minor triad (no 7th) with a single sharp ninth renders "madd#9".  (L298)
TEST(Composing_ChordSymbolFormatterBranch, Suffix_MinorAddSharpNine)
{
    EXPECT_EQ(sym(mk(Q::Minor, {E::SharpNinth})), "Cmadd#9");
}

// Maj7♯5♭9: an augmented major-seventh with a flat ninth renders "Maj7#5b9"
// (catalog "#5" convention; cf. CMaj9#5 / C13#5b9).  (L330)
TEST(Composing_ChordSymbolFormatterBranch, Suffix_AugmentedMaj7FlatNine)
{
    EXPECT_EQ(sym(mk(Q::Augmented, {E::MajorSeventh, E::FlatNinth})), "CMaj7#5b9");
}

// The sus2 dominant ladder: a sus2 with a minor 7th names the highest natural
// extension present — 7sus2 / 9sus2 / 11sus2 / 13sus2.  (L352 + the L353 ternary chain.)
TEST(Composing_ChordSymbolFormatterBranch, Suffix_Sus2DominantLadder)
{
    EXPECT_EQ(sym(mk(Q::Suspended2, {E::MinorSeventh})),                       "C7sus2");
    EXPECT_EQ(sym(mk(Q::Suspended2, {E::MinorSeventh, E::NaturalNinth})),      "C9sus2");
    EXPECT_EQ(sym(mk(Q::Suspended2, {E::MinorSeventh, E::NaturalEleventh})),   "C11sus2");
    EXPECT_EQ(sym(mk(Q::Suspended2, {E::MinorSeventh, E::NaturalThirteenth})), "C13sus2");
}

// Maj7sus via the suspended-quality path: a Suspended4 + major-seventh (not the
// OmitsThird requalification path) renders "Maj7sus".  (L366 false-arm.)
TEST(Composing_ChordSymbolFormatterBranch, Suffix_Sus4Maj7)
{
    EXPECT_EQ(sym(mk(Q::Suspended4, {E::MajorSeventh})), "CMaj7sus");
}

// sus#9: a bare sus4 carrying a sharp ninth renders "sus#9" (the #9 counterpart of the
// already-covered susb9 alteration).  (L387 sharp-arm / L389 false / L390 true.)
TEST(Composing_ChordSymbolFormatterBranch, Suffix_Sus4SharpNine)
{
    EXPECT_EQ(sym(mk(Q::Suspended4, {E::SharpNinth})), "Csus#9");
}

// ♭5 suppression: the structural diminished fifth is never re-appended.  A diminished
// chord keeps "dim"; a half-diminished keeps "m7b5" — appending "b5" would be
// self-contradictory.  (L433 quality==Diminished false-arm / L434 quality==HalfDiminished.)
TEST(Composing_ChordSymbolFormatterBranch, Suffix_FlatFifthSuppressedOnDimAndHalfDim)
{
    EXPECT_EQ(sym(mk(Q::Diminished,     {E::FlatFifth})), "Cdim");
    EXPECT_EQ(sym(mk(Q::HalfDiminished, {E::FlatFifth})), "Cm7b5");
}

// ═════════════════════════════════════════════════════════════════════════════
//  formatSymbol — requalification, "(no 3)", and slash-bass tail
// ═════════════════════════════════════════════════════════════════════════════

// OmitsThird without a major-seventh does NOT enter the Sus4+Maj7 requalification;
// it takes the normal path and appends "(no 3)".  (L733 hasMaj7 false-arm.)
TEST(Composing_ChordSymbolFormatterBranch, FormatSymbol_OmitsThirdNoMaj7_NoRequalify)
{
    EXPECT_EQ(sym(mk(Q::Major, {E::OmitsThird})), "C(no 3)");
}

// The Sus4+Maj7 requalification is suppressed when a #11 is present (Maj7sus implies a
// natural 11).  With both 11 and #11 the chord renders via the normal Major path.
// (L734 !SharpEleventh false-arm; incidentally exercises the L222 "Maj#11" figure.)
TEST(Composing_ChordSymbolFormatterBranch, FormatSymbol_Maj7SusRequalifySuppressedBySharp11)
{
    EXPECT_EQ(sym(mk(Q::Major, {E::OmitsThird, E::MajorSeventh,
                                E::NaturalEleventh, E::SharpEleventh})),
              "CMaj#11(no 3)");
}

// Slash-bass guard (requalified Maj7sus path): an out-of-range bass pitch class
// (-1 or 12) omits the slash.  (L738 bassPc>=0 false / bassPc<12 false.)
TEST(Composing_ChordSymbolFormatterBranch, FormatSymbol_Maj7Sus_OutOfRangeBass_OmitsSlash)
{
    ChordAnalysisResult lo = mk(Q::Major, {E::OmitsThird, E::MajorSeventh, E::NaturalEleventh});
    lo.identity.bassPc = -1;
    EXPECT_EQ(sym(lo), "CMaj7sus");

    ChordAnalysisResult hi = mk(Q::Major, {E::OmitsThird, E::MajorSeventh, E::NaturalEleventh});
    hi.identity.bassPc = 12;
    EXPECT_EQ(sym(hi), "CMaj7sus");
}

// Slash-bass guard (normal path): an out-of-range bass pitch class (12) omits the
// slash.  (L774 bassPc<12 false-arm.)
TEST(Composing_ChordSymbolFormatterBranch, FormatSymbol_Normal_OutOfRangeBass_OmitsSlash)
{
    ChordAnalysisResult r = mk(Q::Major, {});
    r.identity.bassPc = 12;
    EXPECT_EQ(sym(r), "C");
}

// SURFACED FINDING (regression guard, enabled): a German-spelled flat bass name
// ("Ces"/"Fes") is rejected by csfIsValidBassNoteName (the 'e' is not '#'/'b'), so the
// slash is dropped.  Pins current behaviour and exercises L740/L776 (validator false)
// + L721 (bad-accidental reject).  The musically-correct "/Ces" is asserted by the
// DISABLED_ test below.
TEST(Composing_ChordSymbolFormatterBranch, RegressionGuard_GermanFlatBass_SlashDropped)
{
    // Normal path: C major over a Cb bass, German spelling.
    ChordAnalysisResult n = mk(Q::Major, {});
    n.identity.bassPc  = 11;
    n.identity.bassTpc = 7;
    EXPECT_EQ(sym(n, 0, Sp::German), "C");  // slash to "Ces" dropped

    // Maj7sus path: same Cb bass.
    ChordAnalysisResult m = mk(Q::Major, {E::OmitsThird, E::MajorSeventh, E::NaturalEleventh});
    m.identity.bassPc  = 11;
    m.identity.bassTpc = 7;
    EXPECT_EQ(sym(m, 0, Sp::German), "CMaj7sus");  // slash to "Ces" dropped
}

// SURFACED DEFECT (correct oracle — currently FAILS, see file header). A German Cb bass
// SHOULD render "/Ces".  Disabled until the bass-name validator accepts German note
// names; flagged for Cowork.
TEST(Composing_ChordSymbolFormatterBranch, DISABLED_GermanFlatBass_ShouldKeepSlash)
{
    ChordAnalysisResult n = mk(Q::Major, {});
    n.identity.bassPc  = 11;
    n.identity.bassTpc = 7;
    EXPECT_EQ(sym(n, 0, Sp::German), "C/Ces");
}

// ═════════════════════════════════════════════════════════════════════════════
//  csfDiatonicRoman — Roman-numeral base + decorations
// ═════════════════════════════════════════════════════════════════════════════

// Out-of-range degree → empty Roman numeral (degrees are 0..6).  (L488 degree>6 true;
// also drives csfRomanWithInversion's empty-roman early return, L669.)
TEST(Composing_ChordSymbolFormatterBranch, Roman_OutOfRangeDegree_Empty)
{
    ChordAnalysisResult r = mk(Q::Major, {});
    r.function.degree = 7;
    EXPECT_EQ(rn(r), "");
}

// Added-sixth applies only to major/minor: an augmented chord with an AddedSixth flag
// does NOT pick up "(add6)"/"69".  (L524 quality==Minor false-arm.)
TEST(Composing_ChordSymbolFormatterBranch, Roman_AddedSixthIgnoredOnAugmented)
{
    ChordAnalysisResult r = mk(Q::Augmented, {E::AddedSixth});
    r.function.degree = 0;
    EXPECT_EQ(rn(r), "I+");
}

// Half-diminished alterations: ø7 + the altered tone (b9 / #9 / #11 / b13).  Altered
// tones append without elevating the level (which stays 7).  (L551-L554.)
TEST(Composing_ChordSymbolFormatterBranch, Roman_HalfDiminishedAlterations)
{
    auto hd = [](E alt) {
        ChordAnalysisResult r = mk(Q::HalfDiminished, {alt});
        r.function.degree = 1;   // ii
        return rn(r);
    };
    EXPECT_EQ(hd(E::FlatNinth),      "ii" + OE + "7b9");
    EXPECT_EQ(hd(E::SharpNinth),     "ii" + OE + "7#9");
    EXPECT_EQ(hd(E::SharpEleventh),  "ii" + OE + "7#11");
    EXPECT_EQ(hd(E::FlatThirteenth), "ii" + OE + "7b13");
}

// Suspended chord with a major seventh: the level number is preceded by "M".  (L568.)
TEST(Composing_ChordSymbolFormatterBranch, Roman_SuspendedMajorSeventh_MInsert)
{
    ChordAnalysisResult r = mk(Q::Suspended4, {E::MajorSeventh});
    r.function.degree = 0;
    EXPECT_EQ(rn(r), "IM7sus4");
}

// "(add13)" / "(add#9)": extensions on a triad with no seventh use add-notation.
// (L602 NaturalThirteenth / L610 SharpNinth.)
TEST(Composing_ChordSymbolFormatterBranch, Roman_AddNotation_NoSeventh)
{
    ChordAnalysisResult a = mk(Q::Major, {E::NaturalThirteenth});
    a.function.degree = 0;
    EXPECT_EQ(rn(a), "I(add13)");

    ChordAnalysisResult b = mk(Q::Major, {E::SharpNinth});
    b.function.degree = 0;
    EXPECT_EQ(rn(b), "I(add#9)");
}

// ═════════════════════════════════════════════════════════════════════════════
//  csfCoreIntervals via csfRomanWithInversion — sus2/sus4/power inversion figures
// ═════════════════════════════════════════════════════════════════════════════

// The core-interval tables for sus2 {0,2,7}, sus4 {0,5,7}, power {0,7} drive inversion
// figuring: a first-inversion (bass = a non-root chord tone) triad takes "6".  (L641/L644/L647.)
TEST(Composing_ChordSymbolFormatterBranch, Roman_CoreIntervals_SuspendedAndPowerInversions)
{
    // sus2, bass = the 2nd (interval 2) → first inversion.
    ChordAnalysisResult s2 = mk(Q::Suspended2, {});
    s2.function.degree = 0;
    s2.identity.bassPc = 2;
    EXPECT_EQ(rn(s2), "Isus26");

    // sus4, bass = the 4th (interval 5) → first inversion.
    ChordAnalysisResult s4 = mk(Q::Suspended4, {});
    s4.function.degree = 0;
    s4.identity.bassPc = 5;
    EXPECT_EQ(rn(s4), "Isus46");

    // power chord, bass = the 5th (interval 7) → first inversion ("I6").
    ChordAnalysisResult p = mk(Q::Power, {});
    p.function.degree = 0;
    p.identity.bassPc = 7;
    EXPECT_EQ(rn(p), "I6");
}

// ═════════════════════════════════════════════════════════════════════════════
//  formatRomanNumeral — chromatic numeral, aug6/tonicization tail
// ═════════════════════════════════════════════════════════════════════════════

// Chromatic diminished root: a non-diatonic diminished chord takes a lower-case
// chromatic numeral (isMinorQuality via the Diminished arm).  Db° in C → "biio".  (L836.)
TEST(Composing_ChordSymbolFormatterBranch, Roman_ChromaticDiminished_LowerCase)
{
    ChordAnalysisResult r = mk(Q::Diminished, {});
    r.identity.rootPc = 1;        // Db
    r.function.degree = -1;       // non-diatonic
    r.function.keyTonicPc = 0;    // C
    r.function.keyMode = KeySigMode::Ionian;
    EXPECT_EQ(rn(r), "biio");
}

// Tonicization suppressed when the target is not in the key scale: a Db7 in C whose
// next root (Gb, pc 6) is chromatic keeps its chromatic label "bII7".  (L810 next-degree
// lookup returns -1.)
TEST(Composing_ChordSymbolFormatterBranch, Roman_Tonicization_NonScaleTarget_Suppressed)
{
    ChordAnalysisResult r = mk(Q::Major, {E::MinorSeventh});
    r.identity.rootPc = 1;        // Db7
    r.identity.bassPc = 1;        // root position
    r.function.degree = -1;
    r.function.keyTonicPc = 0;    // C major
    r.function.keyMode = KeySigMode::Ionian;
    r.function.nextRootPc = 6;    // Gb — not in C major
    EXPECT_EQ(rn(r), "bII7");
}

// Tonicization skipped when the base Roman numeral is empty (out-of-range degree) even
// though a next root is present.  (L909 !empty false-arm.)
TEST(Composing_ChordSymbolFormatterBranch, Roman_Tonicization_EmptyBase_Skipped)
{
    ChordAnalysisResult r = mk(Q::Major, {});
    r.function.degree = 7;        // → empty Roman numeral
    r.function.nextRootPc = 5;
    EXPECT_EQ(rn(r), "");
}

// vii°/x and viiø/x tonicization labels.  A half-diminished leading-tone chord a
// semitone below its target renders "viiø7/x"; a diminished triad carrying a minor
// seventh renders "viio7/x".  (L948 ø-glyph / L949 isHalfDim true / L951 MinorSeventh true.)
TEST(Composing_ChordSymbolFormatterBranch, Roman_Tonicization_LeadingToneLabels)
{
    // F# half-diminished resolving up a semitone to G (degree 5 = V) in C major.
    ChordAnalysisResult hd = mk(Q::HalfDiminished, {});
    hd.identity.rootPc = 6;       // F#
    hd.identity.bassPc = 6;
    hd.function.degree = -1;
    hd.function.keyTonicPc = 0;
    hd.function.keyMode = KeySigMode::Ionian;
    hd.function.nextRootPc = 7;   // G
    EXPECT_EQ(rn(hd), "vii" + OE + "7/V");

    // F# diminished triad + minor seventh resolving to G.
    ChordAnalysisResult dm = mk(Q::Diminished, {E::MinorSeventh});
    dm.identity.rootPc = 6;
    dm.identity.bassPc = 6;
    dm.function.degree = -1;
    dm.function.keyTonicPc = 0;
    dm.function.keyMode = KeySigMode::Ionian;
    dm.function.nextRootPc = 7;
    EXPECT_EQ(rn(dm), "viio7/V");
}

// ═════════════════════════════════════════════════════════════════════════════
//  formatNashvilleNumber — accidental extension appends
// ═════════════════════════════════════════════════════════════════════════════

// The Nashville accidental appends (♭5 / ♯5 / ♭9 / ♯9 / #11 / ♭13 / ♯13) and the 6/9
// tag are emitted per the present extension flag.  (L1002-L1009.)
TEST(Composing_ChordSymbolFormatterBranch, Nashville_AccidentalExtensionAppends)
{
    auto n = [](E e) {
        ChordAnalysisResult r = mk(Q::Major, {e});
        r.function.degree = 0;   // scale degree 1
        return nash(r);
    };
    EXPECT_EQ(n(E::FlatFifth),       "1" + FL + "5");
    EXPECT_EQ(n(E::SharpFifth),      "1" + SH + "5");
    EXPECT_EQ(n(E::FlatNinth),       "1" + FL + "9");
    EXPECT_EQ(n(E::SharpNinth),      "1" + SH + "9");
    EXPECT_EQ(n(E::FlatThirteenth),  "1" + FL + "13");
    EXPECT_EQ(n(E::SharpThirteenth), "1" + SH + "13");
    EXPECT_EQ(n(E::SixNine),         "16/9");
}
