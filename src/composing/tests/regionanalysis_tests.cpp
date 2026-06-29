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

// ── Stage 1c — pin segmentation passes, harmonicsegmenter, keyresolver ────────
//
// These suites pin the CURRENT behaviour of the three Score-consuming
// subsystems that Stages 3 and 4 will rebaseline:
//   • keyresolver::resolveKeyAndModeRanked          (Stage 4 key-HMM anchor)
//   • harmonicsegmenter::greedyExpandSegmentation   (Stage 3 segmentation)
//   • region::analyzeRegions  (Pass 1/2/2b + Pass-3 absorb/coalesce merge passes)
//
// Unlike the pure-tone suites (chordanalyzer / gates / function layer / keymode),
// these need a real mu::engraving::Score, so the composing test binary loads
// minimal hand-authored .mscx fixtures via the engraving ScoreRW utility (see
// CMakeLists.txt + environment.cpp, which mirror engraving_tests). Fixtures live
// in data/s1c_*.mscx.
//
// All assertions PIN CURRENT BEHAVIOR (Stage 1 philosophy); questionable
// behaviour is documented in cc_stage1c_report.md §Findings, not "fixed".
// Differential baseline for implementation_roadmap.md items 1.3 and 1.4.

#include <gtest/gtest.h>

#include <cmath>
#include <set>
#include <vector>

#include "engraving/dom/masterscore.h"
#include "engraving/dom/measure.h"
#include "engraving/dom/score.h"
#include "engraving/types/fraction.h"
#include "engraving/tests/utils/scorerw.h"

#include "composing/analysis/key/keyresolver.h"
#include "composing/analysis/key/keymodeanalyzer.h"
#include "composing/analysis/key/keymodesequence.h"
#include "composing/analysis/chord/chordanalyzer.h"
#include "composing/analysis/harmony/harmonicsegmenter.h"
#include "composing/analysis/region/regionanalyzer.h"
#include "composing/analysis/region/harmonicrhythm.h"
#include "composing/analysis/engravingbridge/regiontonecollector.h"

using namespace mu::composing::analysis;
namespace kr = mu::composing::analysis::keyresolver;
namespace ebr = mu::composing::analysis::engravingbridge;

using mu::engraving::Fraction;
using mu::engraving::MasterScore;
using mu::engraving::ScoreRW;

namespace {
const std::set<std::size_t> kNoExclude {};
const KeyModeAnalyzerPreferences kKeyPrefs {};

// kMinRegionTicks (scoreharvest) = 1 quarter note = 480 ticks: the Pass-3
// absorbShortRegions duration threshold pinned below.
constexpr int kMinRegionTicks = 480;

// A previous-region result that is deliberately unbeatable: used to skip the
// piece-start shortcut AND guarantee any mode-switch challenger fails the
// hysteresis margin, forcing promoteWinnerInPlace to fire.
KeyModeAnalysisResult dominantPrev(KeySigMode mode, int fifths, int tonicPc)
{
    KeyModeAnalysisResult r;
    r.mode = mode;
    r.keySignatureFifths = fifths;
    r.tonicPc = tonicPc;
    r.score = 1.0e6;
    r.normalizedConfidence = 1.0;
    return r;
}

// Collect the round>=1 (placed) regions from a greedy-expand result, in tick order.
std::vector<mu::composing::PlacedRegion>
placedAnchors(const std::vector<mu::composing::PlacedRegion>& all)
{
    std::vector<mu::composing::PlacedRegion> out;
    for (const auto& p : all) {
        if (p.round >= 1) {
            out.push_back(p);
        }
    }
    std::sort(out.begin(), out.end(),
              [](const auto& a, const auto& b) { return a.startTick < b.startTick; });
    return out;
}
} // namespace

// ═════════════════════════════════════════════════════════════════════════════
//  Task 4 — keyresolver (resolveKeyAndModeRanked)
//  Pins the RESOLVER layer only; analyzeKeyMode scoring internals are already
//  covered by keymodeanalyzer_tests.cpp (985 lines, PitchContext-driven).
// ═════════════════════════════════════════════════════════════════════════════

// 4.4 — Piece-start opening is NOTE-BASED (Stage 4b-i re-pin). The former
// declared-mode piece-start short-circuit (which returned a single-element
// declared anchor at confidence 0.5, score = relativeKeyHysteresisMargin) was
// REMOVED in 4b-i; the normal dynamic-lookahead path now runs from piece start.
// For this C-minor fixture (declared MINOR, −3 effective signature) the
// note-based path still resolves C minor (Aeolian) at rank 0 — the demotion of
// the declared wall to a small hint preserves the correct opening here — but now
// returns the full ranked candidate list (size 3) rather than the size-1 anchor.
TEST(Composing_KeyresolverTests, PieceStartOpening_NoteBased_DeclaredMinor)
{
    MasterScore* score = ScoreRW::readScore(u"data/s1c_c_minor.mscx");
    ASSERT_TRUE(score);

    const auto ranked = kr::resolveKeyAndModeRanked(
        score, Fraction(0, 1), 0, kNoExclude, kKeyPrefs, nullptr);

    // Note-based path: full ranked list, not the removed size-1 declared anchor.
    EXPECT_EQ(ranked.size(), 3u);
    ASSERT_FALSE(ranked.empty());
    EXPECT_EQ(ranked.front().mode, KeySigMode::Aeolian);  // note-based still C minor
    EXPECT_EQ(ranked.front().tonicPc, 0);                 // C
    EXPECT_EQ(ranked.front().keySignatureFifths, -3);
    // No anchor confidence/score pin: those were anchor-specific (removed in 4b-i).

    delete score;
}

// 4.4 — Piece-start opening, declared MAJOR (Stage 4b-i re-pin). Note-based path
// runs from piece start; the C-major fixture still resolves C major (Ionian) at
// rank 0, now with the full ranked list (size 3) instead of the removed anchor.
TEST(Composing_KeyresolverTests, PieceStartOpening_NoteBased_DeclaredMajor)
{
    MasterScore* score = ScoreRW::readScore(u"data/s1c_c_major.mscx");
    ASSERT_TRUE(score);

    const auto ranked = kr::resolveKeyAndModeRanked(
        score, Fraction(0, 1), 0, kNoExclude, kKeyPrefs, nullptr);

    EXPECT_EQ(ranked.size(), 3u);
    ASSERT_FALSE(ranked.empty());
    EXPECT_EQ(ranked.front().mode, KeySigMode::Ionian);
    EXPECT_EQ(ranked.front().tonicPc, 0);                 // C
    EXPECT_EQ(ranked.front().keySignatureFifths, 0);

    delete score;
}

// 4.4 — Insufficient-data fallback: a window with < 3 distinct pitch classes
// (unison C, no key signature so the piece-start shortcut does not apply) →
// fallbackResult at confidence 0.0, single element.
TEST(Composing_KeyresolverTests, InsufficientPitchClasses_FallbackConfidenceZero)
{
    MasterScore* score = ScoreRW::readScore(u"data/s1c_unison_c.mscx");
    ASSERT_TRUE(score);

    const auto ranked = kr::resolveKeyAndModeRanked(
        score, Fraction(0, 1), 0, kNoExclude, kKeyPrefs, nullptr);

    ASSERT_EQ(ranked.size(), 1u);
    EXPECT_DOUBLE_EQ(ranked.front().normalizedConfidence, 0.0);
    EXPECT_DOUBLE_EQ(ranked.front().score, 0.0);
    EXPECT_EQ(ranked.front().keySignatureFifths, 0);

    delete score;
}

// 4.1 — Ranked output contract: size ≥ 1, rank-0 is what .front() consumers get,
// list is score-ordered when no promotion fires (declared mode matches winner).
TEST(Composing_KeyresolverTests, RankedOutput_FrontIsRankZeroAndScoreOrdered)
{
    MasterScore* score = ScoreRW::readScore(u"data/s1c_c_major.mscx");
    ASSERT_TRUE(score);

    // Non-null prevResult (same Ionian mode as the natural winner) skips the
    // piece-start shortcut without triggering any promotion.
    const KeyModeAnalysisResult prev = dominantPrev(KeySigMode::Ionian, 0, 0);
    const auto ranked = kr::resolveKeyAndModeRanked(
        score, Fraction(0, 1), 0, kNoExclude, kKeyPrefs, &prev);

    ASSERT_GE(ranked.size(), 1u);
    // .front() == [0].
    EXPECT_EQ(ranked.front().mode, ranked[0].mode);
    EXPECT_EQ(ranked.front().score, ranked[0].score);
    // Score-ordered (no promotion fired: prev mode == natural winner mode).
    for (size_t i = 0; i + 1 < ranked.size(); ++i) {
        EXPECT_GE(ranked[i].score, ranked[i + 1].score) << "rank " << i;
    }

    delete score;
}

// 4.3 — Partial-signature fix (81978321e3): C-minor music under a 2-flat
// (Dorian) signature with pervasive A-flat is reinterpreted -2 → -3, so the
// note-based path resolves C minor (tonic 0) instead of G minor (tonic 7).
// (Stage 4b-i: the partial-sig correction is unchanged and still declared-gated;
// the former piece-start anchor is gone, but the corrected −3 / C-Aeolian winner
// is preserved by the note-based path here.)
TEST(Composing_KeyresolverTests, PartialSignature_CMinorUnderTwoFlats_Corrected)
{
    MasterScore* score = ScoreRW::readScore(u"data/s1c_partial_cm.mscx");
    ASSERT_TRUE(score);

    const auto ranked = kr::resolveKeyAndModeRanked(
        score, Fraction(0, 1), 0, kNoExclude, kKeyPrefs, nullptr);

    ASSERT_FALSE(ranked.empty());
    EXPECT_EQ(ranked.front().keySignatureFifths, -3);     // corrected from -2
    EXPECT_EQ(ranked.front().tonicPc, 0);                 // C, not G(7)
    EXPECT_EQ(ranked.front().mode, KeySigMode::Aeolian);

    delete score;
}

// 4.3 — Counter-case: a genuinely G-minor piece under the same 2-flat signature
// (no pervasive A-flat) must NOT be corrected — signature proximity dominates
// and the resolver stays at -2 / G minor. This test GUARDS the partial-signature
// non-correction (the −2 / tonic-G outcome), which is unaffected by Stage 4b-i.
// Stage 4b-i re-pin: with the declared-mode wall demoted to a small hint, the
// note-based winner for this fixture is now G HARMONIC minor (raised 7th present)
// rather than G Aeolian — a different minor *flavor* on the same tonic. The pin
// therefore asserts a minor mode on G at −2 (the load-bearing claim), not the
// specific church-mode label.
TEST(Composing_KeyresolverTests, PartialSignature_GMinorUnderTwoFlats_NotCorrected)
{
    MasterScore* score = ScoreRW::readScore(u"data/s1c_g_minor.mscx");
    ASSERT_TRUE(score);

    const auto ranked = kr::resolveKeyAndModeRanked(
        score, Fraction(0, 1), 0, kNoExclude, kKeyPrefs, nullptr);

    ASSERT_FALSE(ranked.empty());
    EXPECT_EQ(ranked.front().keySignatureFifths, -2);     // NOT corrected
    EXPECT_EQ(ranked.front().tonicPc, 7);                 // G
    EXPECT_FALSE(keyModeIsMajor(ranked.front().mode));    // a minor mode (now HarmonicMinor)
    EXPECT_EQ(ranked.front().mode, KeySigMode::HarmonicMinor);  // note-based flavor (was Aeolian under the removed wall)

    delete score;
}

// 4.2 — promoteWinnerInPlace hysteresis + the documented wart: when an
// unbeatable previous-region result forces a mode-switch challenger to lose the
// hysteresis margin, the previous-mode candidate is rotated to rank 0 WITHOUT
// recomputing its normalizedConfidence. The promoted winner therefore carries
// the local-gap confidence it held as a runner-up (the 0.025–1.00 spread the
// Step-3 redesign note flagged), NOT a recomputed top-rank confidence.
// This pin is the Stage-4 rebaseline anchor.
TEST(Composing_KeyresolverTests, PromoteWinnerInPlace_HysteresisDoesNotRecomputeConfidence)
{
    MasterScore* score = ScoreRW::readScore(u"data/s1c_a_minor_amb.mscx");
    ASSERT_TRUE(score);

    // Natural ranking (no prior, no declared mode → no shortcut, no promotion):
    // the C-major / A-minor relative pair with C major (Ionian) at rank 0 and a
    // minor mode at rank 1 carrying a much lower local-gap confidence.
    const auto natural = kr::resolveKeyAndModeRanked(
        score, Fraction(0, 1), 0, kNoExclude, kKeyPrefs, nullptr);
    ASSERT_GE(natural.size(), 2u);
    ASSERT_NE(natural[0].mode, natural[1].mode);
    const KeyModeAnalysisResult target = natural[1];   // the promotion target
    // The wart is only visible if the runner-up's carried confidence genuinely
    // differs from rank-0's confidence.
    ASSERT_NE(target.normalizedConfidence, natural[0].normalizedConfidence);

    // Resolve with an unbeatable prior in the rank-1 candidate's mode → the
    // mode-switch challenger (rank-0) loses the hysteresis margin, so
    // promoteWinnerInPlace rotates the rank-1 candidate to rank 0.
    const KeyModeAnalysisResult prev =
        dominantPrev(target.mode, target.keySignatureFifths, target.tonicPc);
    const auto promoted = kr::resolveKeyAndModeRanked(
        score, Fraction(0, 1), 0, kNoExclude, kKeyPrefs, &prev);
    ASSERT_FALSE(promoted.empty());

    // Promotion happened: rank 0 is now the formerly-rank-1 candidate.
    EXPECT_EQ(promoted.front().mode, target.mode);
    EXPECT_EQ(promoted.front().keySignatureFifths, target.keySignatureFifths);
    EXPECT_EQ(promoted.front().tonicPc, target.tonicPc);
    // The WART: normalizedConfidence is the carried-over runner-up value, NOT
    // recomputed for the new rank-0, so a correctly-keyed winner can carry an
    // arbitrarily low confidence.
    EXPECT_DOUBLE_EQ(promoted.front().normalizedConfidence, target.normalizedConfidence);
    EXPECT_NE(promoted.front().normalizedConfidence, natural.front().normalizedConfidence);

    delete score;
}

// ═════════════════════════════════════════════════════════════════════════════
//  Task 3 — harmonicsegmenter (greedyExpandSegmentation)
// ═════════════════════════════════════════════════════════════════════════════

// 1.4a — Round-1 anchor placement: four half-note chord changes on quarter-note
// beats each clear the texture-adaptive thresholds and become round-1 anchors,
// producing boundaries at 0/960/1920/2880 with the analyzed root + quality.
TEST(Composing_HarmonicSegmenterTests, GreedyExpand_PlacesRound1AnchorsAtChordChanges)
{
    MasterScore* score = ScoreRW::readScore(u"data/s1c_seg_changes.mscx");
    ASSERT_TRUE(score);
    const Fraction startTick(0, 1);
    const Fraction endTick = score->lastMeasure()->endTick();

    const auto analyzer = ChordAnalyzerFactory::create();
    mu::composing::HarmonicSegmenterCallbacks cb;
    cb.staffIsEligible = [&](size_t s) { return ebr::staffIsEligible(score, s, startTick); };
    cb.collectRegionTones = [&](int s, int e) {
        return ebr::collectRegionTones(score, s, e, kNoExclude, -1, false);
    };

    const auto placed = mu::composing::greedyExpandSegmentation(
        score, startTick, endTick, kNoExclude, kDefaultChordAnalyzerPreferences,
        analyzer.get(), 0, KeySigMode::Ionian, cb);

    const auto anchors = placedAnchors(placed);
    ASSERT_EQ(anchors.size(), 4u);

    EXPECT_EQ(anchors[0].startTick, 0);     EXPECT_EQ(anchors[0].endTick, 960);
    EXPECT_EQ(anchors[1].startTick, 960);   EXPECT_EQ(anchors[1].endTick, 1920);
    EXPECT_EQ(anchors[2].startTick, 1920);  EXPECT_EQ(anchors[2].endTick, 2880);
    EXPECT_EQ(anchors[3].startTick, 2880);  EXPECT_EQ(anchors[3].endTick, 3840);

    // Each anchor carries its analyzed chord identity (C / G / Am / F).
    EXPECT_EQ(anchors[0].rootPitchClass, 0);  EXPECT_EQ(anchors[0].quality, "Major");
    EXPECT_EQ(anchors[1].rootPitchClass, 7);  EXPECT_EQ(anchors[1].quality, "Major");
    EXPECT_EQ(anchors[2].rootPitchClass, 9);  EXPECT_EQ(anchors[2].quality, "Minor");
    EXPECT_EQ(anchors[3].rootPitchClass, 5);  EXPECT_EQ(anchors[3].quality, "Major");

    for (const auto& a : anchors) {
        EXPECT_EQ(a.round, 1) << "anchor at " << a.startTick;
    }

    // placedRegionsToTicks exposes the same boundaries, deduplicated + sorted.
    const auto ticks = mu::composing::placedRegionsToTicks(placed);
    ASSERT_EQ(ticks.size(), 4u);
    EXPECT_EQ(ticks[0].ticks(), 0);
    EXPECT_EQ(ticks[1].ticks(), 960);
    EXPECT_EQ(ticks[2].ticks(), 1920);
    EXPECT_EQ(ticks[3].ticks(), 2880);

    delete score;
}

// ═════════════════════════════════════════════════════════════════════════════
//  Task 2 — region::analyzeRegions Pass-3 merge passes
// ═════════════════════════════════════════════════════════════════════════════

// 1.3(1) — absorbShortRegions is ROOT-AGNOSTIC: every region shorter than
// kMinRegionTicks is absorbed into its predecessor regardless of root. The
// fixture's Pass-1 stream (preMergeRegions) holds two short (<480-tick)
// regions whose roots DIFFER from the long C-major predecessor (D minor root 2,
// E minor root 4); the returned stream shows both absorbed into the predecessor
// (its endTick extended over their span). The first region has no predecessor
// and is never absorbed.
TEST(Composing_RegionAnalysisTests, AbsorbShortRegions_RootAgnostic)
{
    MasterScore* score = ScoreRW::readScore(u"data/s1c_seg_absorb.mscx");
    ASSERT_TRUE(score);
    const Fraction endTick = score->lastMeasure()->endTick();

    std::vector<HarmonicRegion> preMerge;
    region::RegionAnalysisHooks hooks;
    hooks.preMergeRegions = &preMerge;
    region::AnalyzeRegionsOptions opts;
    opts.hooks = &hooks;

    const auto regions = region::analyzeRegions(
        score, Fraction(0, 1), endTick, kNoExclude,
        kDefaultChordAnalyzerPreferences, kDefaultKeyModeAnalyzerPreferences, opts);

    // Precondition: the Pass-1 stream genuinely contains short different-rooted
    // regions for the two eighth-note blips, so "absorbed regardless of root"
    // is a meaningful claim and not a no-op.
    int shortDifferentRooted = 0;
    for (const auto& r : preMerge) {
        const int dur = r.endTick - r.startTick;
        if (dur < kMinRegionTicks && r.chordResult.identity.rootPc != 0) {
            ++shortDifferentRooted;
        }
    }
    ASSERT_GE(shortDifferentRooted, 2)
        << "fixture precondition: Pass-1 must emit >=2 short different-rooted regions";

    // Result: the two short different-rooted blips are gone — absorbed into the
    // long C-major predecessor, whose endTick is extended over their span.
    ASSERT_EQ(regions.size(), 2u);
    EXPECT_EQ(regions[0].startTick, 0);
    EXPECT_EQ(regions[0].endTick, 1920);                 // extended from 1440
    EXPECT_EQ(regions[0].chordResult.identity.rootPc, 0);   // C predecessor wins
    EXPECT_EQ(regions[1].startTick, 1920);
    EXPECT_EQ(regions[1].endTick, 3840);
    EXPECT_EQ(regions[1].chordResult.identity.rootPc, 7);   // G

    delete score;
}

// 1.3(3) — Inline same-root merge (Pass 1 main loop): contiguous regions with
// the same root AND same quality collapse into one (here three consecutive
// C-major half notes, including across the barline, merge into [0,2880)); a
// same-root region with a DIFFERENT quality (C minor) does NOT merge and stays
// a separate region.
TEST(Composing_RegionAnalysisTests, InlineSameRootMerge_FiresOnSameQuality_BlocksOnQualityDiff)
{
    MasterScore* score = ScoreRW::readScore(u"data/s1c_seg_merge.mscx");
    ASSERT_TRUE(score);
    const Fraction endTick = score->lastMeasure()->endTick();

    const auto regions = region::analyzeRegions(
        score, Fraction(0, 1), endTick, kNoExclude,
        kDefaultChordAnalyzerPreferences, kDefaultKeyModeAnalyzerPreferences, {});

    ASSERT_EQ(regions.size(), 2u);
    // Three contiguous C-major halves merged into one region.
    EXPECT_EQ(regions[0].startTick, 0);
    EXPECT_EQ(regions[0].endTick, 2880);
    EXPECT_EQ(regions[0].chordResult.identity.rootPc, 0);
    EXPECT_EQ(regions[0].chordResult.identity.quality, ChordQuality::Major);
    // Same-root C minor (quality differs) did NOT merge.
    EXPECT_EQ(regions[1].startTick, 2880);
    EXPECT_EQ(regions[1].endTick, 3840);
    EXPECT_EQ(regions[1].chordResult.identity.rootPc, 0);
    EXPECT_EQ(regions[1].chordResult.identity.quality, ChordQuality::Minor);

    delete score;
}

// 1.3 — Clean distinct chord changes survive unchanged: four half-note regions
// each clear kMinRegionTicks, so neither absorbShortRegions nor
// coalesceShortSameRootRuns fires and the pre-/post-merge streams are identical.
TEST(Composing_RegionAnalysisTests, CleanChordChanges_NoSpuriousMerge)
{
    MasterScore* score = ScoreRW::readScore(u"data/s1c_seg_changes.mscx");
    ASSERT_TRUE(score);
    const Fraction endTick = score->lastMeasure()->endTick();

    std::vector<HarmonicRegion> preMerge, postMerge;
    region::RegionAnalysisHooks hooks;
    hooks.preMergeRegions = &preMerge;
    hooks.postMergeRegions = &postMerge;
    region::AnalyzeRegionsOptions opts;
    opts.hooks = &hooks;

    const auto regions = region::analyzeRegions(
        score, Fraction(0, 1), endTick, kNoExclude,
        kDefaultChordAnalyzerPreferences, kDefaultKeyModeAnalyzerPreferences, opts);

    ASSERT_EQ(regions.size(), 4u);
    const int expectedStarts[4] = { 0, 960, 1920, 2880 };
    const int expectedRoots[4]  = { 0, 7, 9, 5 };
    for (int i = 0; i < 4; ++i) {
        EXPECT_EQ(regions[i].startTick, expectedStarts[i]) << "region " << i;
        EXPECT_EQ(regions[i].endTick, expectedStarts[i] + 960) << "region " << i;
        EXPECT_EQ(regions[i].chordResult.identity.rootPc, expectedRoots[i]) << "region " << i;
    }
    // No merge pass altered the stream.
    EXPECT_EQ(preMerge.size(), postMerge.size());

    delete score;
}

// ═════════════════════════════════════════════════════════════════════════════
//  §3 OVERRIDE-READINESS LOCK-IN — the Layer-3 → region key forward-carry.
// ═════════════════════════════════════════════════════════════════════════════

// The Layer-3 slice decoder computes a ranked key menu + a sequence-margin confidence
// per slice; the slice→region reduction (regionanalyzer localKeyForRegion) carries the
// chosen key's confidence PLUS the PINNED region-level candidate-key menu onto the
// region so the Layer-5 confidence-weighted forward override can SELECT among the keys
// the key layer carried forward — never re-derive (cowork_layer5_function_design.md §8 /
// §9-D7). This pins that forward-carry so a future change cannot silently drop it again
// at the reduction.
//
// ★ Phase-5c Step-4 (§15-3): the carried alternatives are now the PINNED region-level
// reduction — every OTHER (tonic,mode) some slice of the region committed to, ranked by
// accumulated duration (the keys the modulation recompute chooses between) — NOT the v1
// representative-slice placeholder. A CONFIDENT region (carried confidence at/above the
// decoder's uncertainThreshold — NOT an uncertain seam) must carry a NON-EMPTY ranked
// keyAlternatives list AND a key confidence; each carried alternative is a DISTINCT key
// OTHER than the chosen (the region-level bucket property). Asserts the CONTRACT
// (presence + region-level shape), not analyzer-echoed key values.
TEST(Composing_RegionAnalysisTests, OverrideReadiness_ConfidentRegionCarriesKeyAltsAndConfidence)
{
    MasterScore* score = ScoreRW::readScore(u"data/s1c_seg_changes.mscx");   // C major I–V–vi–IV
    ASSERT_TRUE(score);
    const Fraction endTick = score->lastMeasure()->endTick();

    const auto regions = region::analyzeRegions(
        score, Fraction(0, 1), endTick, kNoExclude,
        kDefaultChordAnalyzerPreferences, kDefaultKeyModeAnalyzerPreferences, {});
    ASSERT_FALSE(regions.empty());

    // "Confident" = the carried sequence-margin confidence is at/above the decoder's
    // uncertainThreshold (the same boundary SliceKeyMode.uncertain uses). The `!empty`
    // guard skips the (vanishingly rare) single-lattice-state sentinel, which is
    // confident-by-construction but has no other key to list.
    const double kUncertainThreshold =
        mu::composing::analysis::keymodeseq::kDefaultKeyModeSequencePreferences.uncertainThreshold;

    bool foundConfidentCarry = false;
    for (const auto& r : regions) {
        if (r.keyAlternatives.empty() || r.keyConfidence < kUncertainThreshold) {
            continue;
        }
        foundConfidentCarry = true;
        EXPECT_GT(r.keyConfidence, 0.0) << "a confident region carries a positive key confidence";
        // Shape: every carried alternative is a key OTHER than the chosen, AND the carried
        // menu has no duplicate (tonic,mode) — the PINNED region-level reduction is a menu
        // of distinct candidate keys (one entry per region-level vote bucket).
        for (size_t a = 0; a < r.keyAlternatives.size(); ++a) {
            const auto& alt = r.keyAlternatives[a];
            const bool differsFromChosen = alt.tonicPc != r.keyModeResult.tonicPc
                                           || alt.mode != r.keyModeResult.mode;
            EXPECT_TRUE(differsFromChosen)
                << "keyAlternatives are keys OTHER than the chosen keyModeResult";
            for (size_t b = a + 1; b < r.keyAlternatives.size(); ++b) {
                const auto& other = r.keyAlternatives[b];
                const bool distinct = alt.tonicPc != other.tonicPc || alt.mode != other.mode;
                EXPECT_TRUE(distinct)
                    << "the pinned region-level menu carries DISTINCT candidate keys (no duplicate (tonic,mode))";
            }
        }
    }
    ASSERT_TRUE(foundConfidentCarry)
        << "the forward-carry was dropped: no confident region carried its ranked alternative keys";

    delete score;
}
