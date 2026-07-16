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

// chord_branch_tests.cpp — Phase-5 branch backfill (round 2), cluster 2: the L4
// scoring-oracle leaf helpers (analysisutils.h, chordanalyzer.h inline merge/bass/
// temporal helpers, chordvoicing.cpp, chordanalyzer.cpp buildChordResult/analyzeChord
// edge paths) + the function layer's empty-candidate / resolution-edge sentinels.
//
// Every assertion is the THEORY/CONTRACT-correct value re-derived at source (the
// circle-of-fifths tonic table, the close-position voicing pc set, the documented
// merge/dedup contract), never an echo of current output. The gate (post-scoring A–L)
// branches live in postscoringgates_tests.cpp where the gateCtx harness already exists.
//
// Coverage is the gap-finder, not the goal: these target specific unhit branch
// directions from cc_union_branch_coverage_report.md (re-measured fresh at HEAD), but
// each test stands on its own as a contract pin.

#include <gtest/gtest.h>

#include <algorithm>
#include <array>
#include <vector>

#include "test_helpers.h"

#include "composing/analysis/chord/analysisutils.h"
#include "composing/analysis/chord/chordanalyzer.h"
#include "composing/analysis/function/harmonicfunctionlayer.h"

using namespace mu::composing::analysis;
namespace fn = mu::composing::function;

namespace {

// pcs sorted ascending-from-root, as chordTonePitchClasses returns them.
bool containsPc(const std::vector<int>& pcs, int pc)
{
    return std::find(pcs.begin(), pcs.end(), pc) != pcs.end();
}

int countPc(const std::vector<int>& pcs, int pc)
{
    return static_cast<int>(std::count(pcs.begin(), pcs.end(), pc));
}

ChordAnalysisResult qualityResult(int rootPc, ChordQuality quality,
                                  std::initializer_list<Extension> exts = {})
{
    ChordAnalysisResult r;
    r.identity.rootPc  = rootPc;
    r.identity.bassPc  = rootPc;
    r.identity.quality = quality;
    for (Extension e : exts) {
        setExtension(r.identity.extensions, e);
    }
    return r;
}

} // namespace

// ═════════════════════════════════════════════════════════════════════════════
// analysisutils.h — ionianTonicPcFromFifths: the major-key tonic pitch class for
// each notated key signature. Oracle = the circle of fifths: tonic pc = (7·fifths)
// mod 12. Pins the WHOLE table −7..+7 (the unhit arms were Cb=−7→11, A=+3→9,
// F#=+6→6) plus the out-of-range default.
// ═════════════════════════════════════════════════════════════════════════════

TEST(Composing_ChordBranchTests, IonianTonicPcFromFifths_FullTable)
{
    struct Case { int fifths; int expectedPc; };
    // (7·fifths) mod 12, the Ionian tonic for each signature.
    const Case cases[] = {
        { -7, 11 }, // Cb
        { -6,  6 }, // Gb
        { -5,  1 }, // Db
        { -4,  8 }, // Ab
        { -3,  3 }, // Eb
        { -2, 10 }, // Bb
        { -1,  5 }, // F
        {  0,  0 }, // C
        {  1,  7 }, // G
        {  2,  2 }, // D
        {  3,  9 }, // A
        {  4,  4 }, // E
        {  5, 11 }, // B
        {  6,  6 }, // F#
        {  7,  1 }, // C#
    };
    for (const Case& c : cases) {
        EXPECT_EQ(ionianTonicPcFromFifths(c.fifths), c.expectedPc)
            << "fifths=" << c.fifths;
        // Cross-check against the closed-form circle-of-fifths identity.
        EXPECT_EQ(c.expectedPc, ((7 * c.fifths) % 12 + 12) % 12) << "fifths=" << c.fifths;
    }
    // Out-of-range signatures fall back to C (pc 0).
    EXPECT_EQ(ionianTonicPcFromFifths(8), 0);
    EXPECT_EQ(ionianTonicPcFromFifths(-8), 0);
}

// ═════════════════════════════════════════════════════════════════════════════
// chordanalyzer.h — normalizeMergedBassTone / mergeChordAnalysisTones /
// bassToneFromTones (inline merge helpers).
// ═════════════════════════════════════════════════════════════════════════════

// Empty input is a no-op (the early-return guard): nothing to normalise.
TEST(Composing_ChordBranchTests, NormalizeMergedBassTone_EmptyIsNoOp)
{
    std::vector<ChordAnalysisTone> empty;
    normalizeMergedBassTone(empty);
    EXPECT_TRUE(empty.empty());
}

// Same-pc merge backfills a missing TPC from the new tone (contract: keep the
// lower pitch but inherit a real spelling when the existing one is unknown).
TEST(Composing_ChordBranchTests, MergeChordAnalysisTones_BackfillsMissingTpcAtEqualPitch)
{
    std::vector<ChordAnalysisTone> existing(1);
    existing[0].pitch  = 60;   // C4
    existing[0].tpc    = -1;   // unknown spelling
    existing[0].weight = 1.0;
    existing[0].isBass = true;

    std::vector<ChordAnalysisTone> incoming(1);
    incoming[0].pitch  = 60;   // same pc, same pitch (so the lower-pitch branch is NOT taken)
    incoming[0].tpc    = 14;   // C (natural)
    incoming[0].weight = 1.0;

    mergeChordAnalysisTones(existing, incoming);
    ASSERT_EQ(existing.size(), 1u);
    EXPECT_EQ(existing[0].pitch, 60);
    EXPECT_EQ(existing[0].tpc, 14);    // backfilled
}

// Same-pc merge where BOTH spellings are unknown leaves the TPC unknown (no
// spurious backfill from a -1 source).
TEST(Composing_ChordBranchTests, MergeChordAnalysisTones_NoBackfillWhenNewTpcAlsoUnknown)
{
    std::vector<ChordAnalysisTone> existing(1);
    existing[0].pitch  = 60;
    existing[0].tpc    = -1;
    existing[0].weight = 1.0;
    existing[0].isBass = true;

    std::vector<ChordAnalysisTone> incoming(1);
    incoming[0].pitch  = 60;
    incoming[0].tpc    = -1;
    incoming[0].weight = 1.0;

    mergeChordAnalysisTones(existing, incoming);
    ASSERT_EQ(existing.size(), 1u);
    EXPECT_EQ(existing[0].tpc, -1);    // still unknown
}

// With several tones flagged isBass, the lowest-pitch one is the structural bass.
TEST(Composing_ChordBranchTests, BassToneFromTones_MultipleBassFlagsPicksLowestPitch)
{
    std::vector<ChordAnalysisTone> tones(3);
    tones[0].pitch = 64; tones[0].isBass = true;   // E4 (first, sets bassTone)
    tones[1].pitch = 60; tones[1].isBass = true;   // C4 (lower -> becomes bass)
    tones[2].pitch = 62; tones[2].isBass = true;   // D4 (higher -> kept)

    const ChordAnalysisTone* bass = bassToneFromTones(tones);
    ASSERT_NE(bass, nullptr);
    EXPECT_EQ(bass->pitch, 60);   // the lowest of the three flagged bass tones
}

// A non-bass tone is skipped even when it is the lowest pitch overall.
TEST(Composing_ChordBranchTests, BassToneFromTones_IgnoresNonBassEvenIfLower)
{
    std::vector<ChordAnalysisTone> tones(2);
    tones[0].pitch = 48; tones[0].isBass = false;  // lower, but NOT flagged bass
    tones[1].pitch = 60; tones[1].isBass = true;   // the only bass

    const ChordAnalysisTone* bass = bassToneFromTones(tones);
    ASSERT_NE(bass, nullptr);
    EXPECT_EQ(bass->pitch, 60);
}

// ═════════════════════════════════════════════════════════════════════════════
// chordanalyzer.h — advanceTemporalContext (5-arg, gateCtx overload) sentinels.
// When the chosen root is unknown (<0) the predecessor root-weight is 0; when
// rawCandidates is empty the predecessor score is 0; with fewer than 2 raw
// candidates the predecessor margin is the −1 sentinel.
// ═════════════════════════════════════════════════════════════════════════════

TEST(Composing_ChordBranchTests, AdvanceTemporalContext_UnknownRootAndEmptyRawCandidates)
{
    ChordTemporalContext ctx;
    int runningStepwise = 0;
    std::array<int, 3> recentRoots = { -1, -1, -1 };

    ChordIdentity chosen;
    chosen.rootPc  = -1;                     // unknown root
    chosen.bassPc  = 4;
    chosen.quality = ChordQuality::Major;

    PostScoringGateContext gateCtx;          // rawCandidates empty by default
    gateCtx.distinctPcs = 5;

    advanceTemporalContext(ctx, runningStepwise, recentRoots, chosen, gateCtx);

    EXPECT_DOUBLE_EQ(ctx.previousWinnerRootPcWeight, 0.0);   // winRoot < 0 -> 0.0
    EXPECT_DOUBLE_EQ(ctx.previousWinnerScore, 0.0);          // empty rawCandidates -> 0.0
    EXPECT_DOUBLE_EQ(ctx.previousWinnerMargin, -1.0);        // < 2 candidates -> -1 sentinel
    EXPECT_EQ(ctx.previousDistinctPcs, 5);
    EXPECT_EQ(ctx.previousRootPc, -1);                       // delegated identity field
}

// Contrast: a known root with >= 2 raw candidates yields a real weight, score and
// margin (pins the non-sentinel side so the sentinel test is not vacuous).
TEST(Composing_ChordBranchTests, AdvanceTemporalContext_KnownRootWithCandidatesUsesRealValues)
{
    ChordTemporalContext ctx;
    int runningStepwise = 0;
    std::array<int, 3> recentRoots = { -1, -1, -1 };

    ChordIdentity chosen;
    chosen.rootPc  = 7;
    chosen.bassPc  = 7;
    chosen.quality = ChordQuality::Major;

    PostScoringGateContext gateCtx;
    gateCtx.distinctPcs = 4;
    gateCtx.pcWeight[7] = 0.9;
    gateCtx.rawCandidates = {
        RawCandidate{ 2.5, 0.0, 7, ChordQuality::Major, 0, 0.0 },
        RawCandidate{ 2.1, 0.0, 2, ChordQuality::Minor, 4, 0.0 },
    };

    advanceTemporalContext(ctx, runningStepwise, recentRoots, chosen, gateCtx);

    EXPECT_DOUBLE_EQ(ctx.previousWinnerRootPcWeight, 0.9);
    EXPECT_DOUBLE_EQ(ctx.previousWinnerScore, 2.5);
    EXPECT_NEAR(ctx.previousWinnerMargin, 0.4, 1e-9);
}

// ═════════════════════════════════════════════════════════════════════════════
// chordvoicing.cpp — chordTonePitchClasses pitch-class set construction.
// Oracle = the literal chord-tone collection per quality + extension contract.
// ═════════════════════════════════════════════════════════════════════════════

// Every quality yields root + (third unless omitted) + (fifth unless Unknown).
TEST(Composing_ChordBranchTests, ChordTonePitchClasses_TriadShapesPerQuality)
{
    auto pcs = [](ChordQuality q) {
        return chordTonePitchClasses(qualityResult(0, q));
    };
    EXPECT_EQ(pcs(ChordQuality::Major),          (std::vector<int>{ 0, 4, 7 }));
    EXPECT_EQ(pcs(ChordQuality::Minor),          (std::vector<int>{ 0, 3, 7 }));
    EXPECT_EQ(pcs(ChordQuality::Diminished),     (std::vector<int>{ 0, 3, 6 }));
    EXPECT_EQ(pcs(ChordQuality::Augmented),      (std::vector<int>{ 0, 4, 8 }));
    // HalfDiminished carries a structural minor 7th not flagged as an extension.
    EXPECT_EQ(pcs(ChordQuality::HalfDiminished), (std::vector<int>{ 0, 3, 6, 10 }));
    EXPECT_EQ(pcs(ChordQuality::Suspended2),     (std::vector<int>{ 0, 2, 7 }));
    EXPECT_EQ(pcs(ChordQuality::Suspended4),     (std::vector<int>{ 0, 5, 7 }));
    EXPECT_EQ(pcs(ChordQuality::Power),          (std::vector<int>{ 0, 7 }));
    // Unknown has neither a defined third nor fifth — just the root.
    EXPECT_EQ(pcs(ChordQuality::Unknown),        (std::vector<int>{ 0 }));
}

// A b5 alteration flag on a quality whose fifth is NOT a perfect 5th (Diminished,
// fifth = 6) is a no-op: the fifth stays the structural d5, no double-fifth.
TEST(Composing_ChordBranchTests, ChordTonePitchClasses_FlatFifthFlagInertOnDiminished)
{
    const auto pcs = chordTonePitchClasses(
        qualityResult(0, ChordQuality::Diminished, { Extension::FlatFifth }));
    EXPECT_EQ(pcs, (std::vector<int>{ 0, 3, 6 }));
    EXPECT_EQ(countPc(pcs, 6), 1);    // single diminished fifth, not doubled
}

// A #5 alteration flag on Augmented (fifth already = 8) is likewise inert.
TEST(Composing_ChordBranchTests, ChordTonePitchClasses_SharpFifthFlagInertOnAugmented)
{
    const auto pcs = chordTonePitchClasses(
        qualityResult(0, ChordQuality::Augmented, { Extension::SharpFifth }));
    EXPECT_EQ(pcs, (std::vector<int>{ 0, 4, 8 }));
    EXPECT_EQ(countPc(pcs, 8), 1);
}

// HalfDiminished + an explicit MajorSeventh: the explicit M7 (pc 11) is used and the
// structural m7 (pc 10) is NOT added (the dup-avoidance guard).
TEST(Composing_ChordBranchTests, ChordTonePitchClasses_HalfDimWithMajorSeventhSkipsStructuralM7)
{
    const auto pcs = chordTonePitchClasses(
        qualityResult(0, ChordQuality::HalfDiminished, { Extension::MajorSeventh }));
    EXPECT_TRUE(containsPc(pcs, 11));   // explicit major seventh
    EXPECT_FALSE(containsPc(pcs, 10));  // structural minor seventh suppressed
}

// AddedSixth is suppressed when a seventh is present (it becomes a 13th, not a 6th):
// with a MajorSeventh the pc 9 must not appear.
TEST(Composing_ChordBranchTests, ChordTonePitchClasses_AddedSixthSkippedWithMajorSeventh)
{
    const auto pcs = chordTonePitchClasses(
        qualityResult(0, ChordQuality::Major,
                      { Extension::AddedSixth, Extension::MajorSeventh }));
    EXPECT_TRUE(containsPc(pcs, 11));   // major seventh present
    EXPECT_FALSE(containsPc(pcs, 9));   // added sixth suppressed (would be a 13th)
}

// AddedSixth suppressed when a DiminishedSeventh is present: pc 9 comes only from the
// dim7 (single copy), never doubled by the added-sixth path.
TEST(Composing_ChordBranchTests, ChordTonePitchClasses_AddedSixthSkippedWithDiminishedSeventh)
{
    const auto pcs = chordTonePitchClasses(
        qualityResult(0, ChordQuality::Major,
                      { Extension::AddedSixth, Extension::DiminishedSeventh }));
    EXPECT_EQ(countPc(pcs, 9), 1);      // dim7 pc only, added sixth did not double it
}

// closePositionVoicing: Unknown quality is rejected up front; a real triad produces a
// bass in C2..C3 and ascending close-position treble tones.
TEST(Composing_ChordBranchTests, ClosePositionVoicing_UnknownEmpty_TriadVoiced)
{
    const ClosePositionVoicing none = closePositionVoicing(qualityResult(0, ChordQuality::Unknown));
    EXPECT_TRUE(none.treblePitches.empty());
    EXPECT_EQ(none.bassPitch, -1);   // documented "empty voicing" sentinel

    const ClosePositionVoicing cmaj = closePositionVoicing(qualityResult(0, ChordQuality::Major));
    EXPECT_GE(cmaj.bassPitch, 36);  // C2..C3 register
    EXPECT_LE(cmaj.bassPitch, 48);
    EXPECT_FALSE(cmaj.treblePitches.empty());
    // Treble tones are non-decreasing (close position stacks upward).
    for (size_t i = 1; i < cmaj.treblePitches.size(); ++i) {
        EXPECT_GE(cmaj.treblePitches[i], cmaj.treblePitches[i - 1]);
    }
}

// ═════════════════════════════════════════════════════════════════════════════
// chordanalyzer.cpp — buildChordResult / detectExtensions disambiguation edges.
// buildChordResult is the public entry; driving it with a hand-built pcWeight /
// tpcForPc exercises detectExtensions deterministically (oracle = the documented
// add#9-vs-m3 and #13-on-diminished rules).
// ═════════════════════════════════════════════════════════════════════════════

namespace {
BuildChordResultContext makeBuildCtx(const std::array<double, 12>& pcWeight,
                                     const std::array<int, 12>& tpcForPc,
                                     int bassPc, int bassTpc = -1,
                                     int keyTonicPc = 0,
                                     int keySignatureFifths = 0)
{
    static const std::array<int, 7> kIonian = { 0, 2, 4, 5, 7, 9, 11 };
    // keySignatureFifths defaults to 0 (C), the signature whose collection is exactly the
    // (keyTonicPc = 0, Ionian) pair above — so the two key contexts the builder carries agree.
    return BuildChordResultContext{ pcWeight, tpcForPc, bassPc, bassTpc,
                                    keyTonicPc, KeySigMode::Ionian, kIonian,
                                    keySignatureFifths };
}
} // namespace

// A Major reading whose minor-third (pc 3) is present but whose MAJOR third (pc 4) is
// absent does NOT label the pc-3 note as a #9 — it is the m3 of a minor chord, not an
// add#9 colour tone ("{A,C,E} is Am, not Aadd#9", source comment).
TEST(Composing_ChordBranchTests, BuildChordResult_MajorWithoutMajorThird_NoSharpNinth)
{
    std::array<double, 12> w{};
    w[0] = 1.0;   // C (root)
    w[3] = 0.6;   // Eb / D# (pc 3) present
    w[7] = 1.0;   // G (fifth)
    // w[4] (E, the major third) deliberately absent.
    std::array<int, 12> tpc{};
    tpc.fill(-1);

    const ChordAnalysisResult r =
        buildChordResult(RawCandidate{ 2.0, 0.0, 0, ChordQuality::Major, 0, 0.0 },
                         makeBuildCtx(w, tpc, /*bassPc*/ 0), kDefaultChordAnalyzerPreferences);
    EXPECT_FALSE(hasExtension(r.identity.extensions, Extension::SharpNinth));
}

// Contrast: with the major third (pc 4) ALSO present, the pc-3 note IS a genuine #9.
TEST(Composing_ChordBranchTests, BuildChordResult_MajorWithBothThirds_SharpNinthDetected)
{
    std::array<double, 12> w{};
    w[0] = 1.0;   // C
    w[3] = 0.6;   // D# (#9)
    w[4] = 1.0;   // E (major third present)
    w[7] = 1.0;   // G
    std::array<int, 12> tpc{};
    tpc.fill(-1);

    const ChordAnalysisResult r =
        buildChordResult(RawCandidate{ 2.0, 0.0, 0, ChordQuality::Major, 0, 0.0 },
                         makeBuildCtx(w, tpc, /*bassPc*/ 0), kDefaultChordAnalyzerPreferences);
    EXPECT_TRUE(hasExtension(r.identity.extensions, Extension::SharpNinth));
}

// A #13 (augmented-sixth-spelled pc+10) is suppressed on a DIMINISHED reading: the
// quality guard blocks the sharp-thirteenth flag even when the TPC spelling confirms it.
TEST(Composing_ChordBranchTests, BuildChordResult_DiminishedSuppressesSharpThirteenth)
{
    std::array<double, 12> w{};
    w[0]  = 1.0;   // C (root)
    w[3]  = 1.0;   // Eb (m3)
    w[6]  = 1.0;   // Gb (d5)
    w[10] = 0.6;   // A# (pc 10), spelled as an augmented sixth below
    std::array<int, 12> tpc{};
    tpc.fill(-1);
    tpc[0]  = 14;  // C
    tpc[10] = 24;  // A#  (tpc delta from C = +10 -> aug-6 / #13 spelling)

    const ChordAnalysisResult r =
        buildChordResult(RawCandidate{ 2.0, 0.0, 0, ChordQuality::Diminished, 6, 0.0 },
                         makeBuildCtx(w, tpc, /*bassPc*/ 0), kDefaultChordAnalyzerPreferences);
    EXPECT_FALSE(hasExtension(r.identity.extensions, Extension::SharpThirteenth));
}

// ═════════════════════════════════════════════════════════════════════════════
// chordanalyzer.cpp — bass-selection edges through analyzeChord.
// ═════════════════════════════════════════════════════════════════════════════

namespace {
// Tones carrying onset data (so joint bass enumeration is enabled), bass first.
std::vector<ChordAnalysisTone> onsetBassTones(
    std::initializer_list<std::pair<int, bool>> pitchOnset)
{
    std::vector<ChordAnalysisTone> out;
    bool first = true;
    for (const auto& po : pitchOnset) {
        ChordAnalysisTone t;
        t.pitch              = po.first;
        t.weight             = 1.0;
        t.isBass             = first;
        t.onsetAtRegionStart = po.second;
        out.push_back(t);
        first = false;
    }
    return out;
}

const RuleBasedChordAnalyzer kBranchAnalyzer;
} // namespace

// Two bass-register tones of the SAME pitch class (C2 + C3): the dedup keeps the
// lower octave as the bass candidate. The reading is C major in root position.
TEST(Composing_ChordBranchTests, AnalyzeChord_SamePcBassRegisterDedup)
{
    // C2(36) + C3(48) both onset, with E4 + G4 above -> C major, bass C.
    const auto results = analyzeWithGates(
        kBranchAnalyzer,
        onsetBassTones({ { 36, true }, { 48, true }, { 64, true }, { 67, true } }),
        /*fifths*/ 0, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.rootPc, 0);
    EXPECT_EQ(results.front().identity.bassPc, 0);
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Major);
}

// When NO tone clears the bass weight floor (bassMinWeight = 0.05·totalRawWeight),
// the bass falls back to the absolute lowest pitch. A dense 21-tone equal-weight
// C-major spread (7 octaves × {C,E,G}) makes every tone < 5% of the total.
TEST(Composing_ChordBranchTests, AnalyzeChord_AllBelowBassMinWeight_LowestPitchFallback)
{
    std::vector<ChordAnalysisTone> tones;
    bool first = true;
    for (int oct = 0; oct < 7; ++oct) {
        for (int semis : { 0, 4, 7 }) {            // C, E, G
            ChordAnalysisTone t;
            t.pitch  = 36 + 12 * oct + semis;      // from C2 upward
            t.weight = 1.0;                        // equal weight -> each is 1/21 < 0.05
            t.isBass = first;
            tones.push_back(t);
            first = false;
        }
    }
    ASSERT_EQ(tones.size(), 21u);
    const auto results = analyzeWithGates(kBranchAnalyzer, tones, 0, KeySigMode::Ionian);
    ASSERT_FALSE(results.empty());
    EXPECT_EQ(results.front().identity.quality, ChordQuality::Major);
    EXPECT_EQ(results.front().identity.rootPc, 0);
    EXPECT_EQ(results.front().identity.bassPc, 0);   // fell back to the lowest pitch (C2)
}

// ═════════════════════════════════════════════════════════════════════════════
// harmonicfunctionlayer.cpp — resolutionEdgeBonus sentinel + applyHarmonicFunction
// empty-candidate path.
// ═════════════════════════════════════════════════════════════════════════════

// A known predecessor quality but an unknown predecessor root (<0) yields no
// resolution bonus (the second sentinel arm of the early-return guard).
TEST(Composing_ChordBranchTests, ResolutionEdgeBonus_KnownQualityUnknownPrevRoot_Zero)
{
    // Diminished -> Major a semitone up would normally pay the bonus, but prevRoot < 0.
    EXPECT_DOUBLE_EQ(
        fn::resolutionEdgeBonus(1, ChordQuality::Major, /*prevRoot*/ -1,
                                ChordQuality::Diminished, /*bonus*/ 0.35),
        0.0);
    // Sanity: with a valid prevRoot the same shape DOES pay the bonus.
    EXPECT_DOUBLE_EQ(
        fn::resolutionEdgeBonus(1, ChordQuality::Major, /*prevRoot*/ 0,
                                ChordQuality::Diminished, 0.35),
        0.35);
}

// An empty scoring snapshot produces no results and leaves chosenResult untouched
// (the no-above-threshold-candidates path: empty winning-bass list -> 0 score, no
// build, no diff-root append, chosenResult unchanged).
TEST(Composing_ChordBranchTests, ApplyHarmonicFunction_EmptySnapshot_NoResultsChosenUnchanged)
{
    fn::ScoringSnapshot snapshot;            // no cells
    snapshot.distinctPcs         = 3;
    snapshot.jointScoringEnabled = false;
    snapshot.tpcForPc.fill(-1);

    fn::HarmonicFunctionContext fctx;
    const ChordAnalyzerPreferences prefs;
    std::vector<ChordAnalysisResult> results;

    ChordAnalysisResult sentinel;
    sentinel.identity.rootPc  = 9;
    sentinel.identity.quality = ChordQuality::Minor;
    ChordAnalysisResult chosen = sentinel;

    fn::applyHarmonicFunction(snapshot, fctx, prefs, results, chosen, nullptr,
                              fn::ScoringPhase::Final);

    EXPECT_TRUE(results.empty());
    // chosenResult is only overwritten when results is non-empty.
    EXPECT_EQ(chosen.identity.rootPc, 9);
    EXPECT_EQ(chosen.identity.quality, ChordQuality::Minor);
}
