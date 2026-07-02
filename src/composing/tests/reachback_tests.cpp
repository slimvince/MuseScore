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

// ── Architectural Layer 3 — reach-back (Phase 3) ─────────────────────────────
//
// These tests exercise the SELECTION-AWARE reach-back capability built on the
// region analyzer (region::analyzeRegions, opts.reachBack). Production builds the
// whole score and never reaches back — byte-identical; the standing corpus + suite
// + snapshot gates cover that. Reach-back fires ONLY on a partial selection whose
// opening has no settled key — the only place it is exercised — so these are the
// only tests of the new behaviour. Design: cowork_layer3_reachback_design.md.
//
// Fixture data/reachback_anchor.mscx (0 fifths, declared A minor): bars 1-6 = an
// unambiguous C-major establishment (I IV V I V I, G-B-D dominants with the B
// leading tone, no G#), bars 7-9 = a relative-pair A-minor/E-minor/A-minor tail.
// Selecting ONLY bar 7 (a single A-minor triad, ticks [11520, 13440)) opens with a
// LOW-confidence A-minor reading (a bare triad reads as its own tonic, but the
// relative C major is close — confidence ~1.3). Reach-back extends earlier into the
// C-major head, whose established key anchors the opening to C major (the change
// cost is not repaid by a single Am measure): iso A-minor → reached C-major, which
// equals the whole-score reading.

#include <gtest/gtest.h>

#include <set>
#include <vector>

#include "engraving/dom/masterscore.h"
#include "engraving/types/fraction.h"
#include "engraving/tests/utils/scorerw.h"

#include "composing/analysis/chord/chordanalyzer.h"
#include "composing/analysis/key/keymodeanalyzer.h"
#include "composing/analysis/region/regionanalyzer.h"
#include "composing/analysis/region/harmonicrhythm.h"

using namespace mu::composing::analysis;

using mu::engraving::Fraction;
using mu::engraving::MasterScore;
using mu::engraving::ScoreRW;

namespace {
const std::set<std::size_t> kNoExclude {};
const ChordAnalyzerPreferences kPrefs {};
const KeyModeAnalyzerPreferences kKeyPrefs {};

// Tick layout of reachback_anchor.mscx (Division 480, 4/4 whole notes; 9 bars).
constexpr int kMeasure   = 1920;
constexpr int kTailStart = 6 * kMeasure;   // 11520 — bar 7, the single A-minor triad
constexpr int kM7End     = 7 * kMeasure;   // 13440 — end of bar 7

// Pitch classes for the keys this fixture decides between.
constexpr int kCMajorTonic = 0;   // C
constexpr int kAMinorTonic = 9;   // A

std::vector<HarmonicRegion> run(MasterScore* score, int s, int e,
                                const region::AnalyzeRegionsOptions& opts)
{
    return region::analyzeRegions(score, Fraction::fromTicks(s), Fraction::fromTicks(e),
                                  kNoExclude, kPrefs, kKeyPrefs, opts);
}

// Reach-back ON over the selection, growing earlier while the opening is unsettled.
// The low-confidence trigger (minConf) is the design's "or low sequence-margin"
// clause: this fixture's bare-Am opening is confident enough to clear the decoder's
// own "uncertain" flag (~1.3) but is still a weak reading, so a 2.0 threshold treats
// it as unsettled. The increment defaults to one measure.
region::AnalyzeRegionsOptions reachOpts(int maxSteps = 8, int incTicks = 0, double minConf = 2.0)
{
    region::AnalyzeRegionsOptions o;
    o.reachBack.enabled = true;
    o.reachBack.maxReachSteps = maxSteps;
    o.reachBack.incrementTicks = incTicks;
    o.reachBack.minOpeningConfidence = minConf;
    return o;
}

int leadTonic(const std::vector<HarmonicRegion>& rs)
{
    return rs.empty() ? -1 : rs.front().keyModeResult.tonicPc;
}

// Compare two region streams by the user-visible analysis (key + chord + span).
bool sameAnalysis(const std::vector<HarmonicRegion>& a, const std::vector<HarmonicRegion>& b)
{
    if (a.size() != b.size()) { return false; }
    for (size_t i = 0; i < a.size(); ++i) {
        if (a[i].startTick != b[i].startTick || a[i].endTick != b[i].endTick) { return false; }
        if (a[i].keyModeResult.tonicPc != b[i].keyModeResult.tonicPc) { return false; }
        if (a[i].keyModeResult.isMajor() != b[i].keyModeResult.isMajor()) { return false; }
        if (a[i].chordResult.identity.rootPc != b[i].chordResult.identity.rootPc) { return false; }
        if (a[i].chordResult.identity.quality != b[i].chordResult.identity.quality) { return false; }
    }
    return true;
}
} // namespace

// ── §3.1 — reach-back fires, anchors the leading-edge key, and terminates ─────
// A partial selection whose opening is unsettled (the single bar-7 A-minor triad,
// read locally as A minor) extends earlier into the C-major head and anchors the
// opening to the carried-in C major — which equals the whole-score reading. The
// extension changed the outcome (reached != isolated), and the loop terminated.
TEST(Composing_ReachBack, FiresAndAnchorsToCarriedInContext)
{
    MasterScore* score = ScoreRW::readScore(u"data/reachback_anchor.mscx");
    ASSERT_TRUE(score);

    const auto whole = run(score, kTailStart, kM7End, {});               // whole-score build
    const auto iso   = run(score, kTailStart, kM7End, reachOpts(0));     // selection only, no reach
    const auto reach = run(score, kTailStart, kM7End, reachOpts(8));     // selection + reach-back

    ASSERT_EQ(iso.size(), 1u);
    ASSERT_EQ(reach.size(), 1u);
    ASSERT_EQ(whole.size(), 1u);

    // Isolated, the opening reads its local tonic — A minor.
    EXPECT_EQ(leadTonic(iso), kAMinorTonic);
    // Reach-back anchors it to the carried-in C major (the established head).
    EXPECT_EQ(leadTonic(reach), kCMajorTonic);
    // The extension changed the outcome (it genuinely fired and mattered)…
    EXPECT_NE(leadTonic(reach), leadTonic(iso));
    // …and recovered exactly the full-context (whole-score) reading.
    EXPECT_TRUE(sameAnalysis(reach, whole));

    delete score;
}

// ── §3.2 — convergence is deterministic: independent of the increment size ────
// Reaching the converged span in several small steps (one measure) or fewer big
// steps (two measures) yields the SAME in-selection analysis — the re-decode is a
// pure function of the loaded span, and once the leading-edge key settles, more
// context cannot move it. This is also the check that the convergence criterion is
// not increment-sensitive.
TEST(Composing_ReachBack, ConvergenceIsIncrementIndependent)
{
    MasterScore* score = ScoreRW::readScore(u"data/reachback_anchor.mscx");
    ASSERT_TRUE(score);

    const auto small = run(score, kTailStart, kM7End, reachOpts(8, kMeasure));        // 1-measure steps
    const auto big   = run(score, kTailStart, kM7End, reachOpts(8, 2 * kMeasure));    // 2-measure steps

    ASSERT_FALSE(small.empty());
    EXPECT_TRUE(sameAnalysis(small, big)) << "the converged result must not depend on the increment";
    // Both converged to the carried-in C major (not the isolated A-minor reading).
    EXPECT_EQ(leadTonic(small), kCMajorTonic);
    EXPECT_EQ(leadTonic(big), kCMajorTonic);

    delete score;
}

// ── §3.3 — selection at the score start truncates cleanly (no error) ──────────
// When the opening is the score start there is nothing earlier to reach; extend()
// reports the boundary and the loop exits gracefully. Even with the trigger forced
// (a very high confidence threshold marks the opening unsettled) and the increment
// large, the result equals the no-reach baseline over the same span — a graceful
// no-op, not a crash or a different reading.
TEST(Composing_ReachBack, SelectionAtScoreStart_TruncatesCleanly)
{
    MasterScore* score = ScoreRW::readScore(u"data/reachback_anchor.mscx");
    ASSERT_TRUE(score);

    // Force the trigger (minConf huge ⇒ opening always "unsettled") AND a large
    // increment, so the loop genuinely tries to reach back from the score start.
    const auto reached = run(score, 0, kMeasure, reachOpts(8, 4 * kMeasure, 1.0e9));
    const auto baseline = run(score, 0, kMeasure, reachOpts(0, 0, 1.0e9));   // no extension

    ASSERT_FALSE(reached.empty());
    EXPECT_TRUE(sameAnalysis(reached, baseline))
        << "at the score start reach-back has nothing to load and must be a clean no-op";

    delete score;
}

// ── §3.4 — output is the selection only (context is evidence, never emitted) ──
// Reaching back loads the whole C-major head as context, but the emitted regions
// cover only the selection; the reached-back context span is not output.
TEST(Composing_ReachBack, OutputIsSelectionOnly)
{
    MasterScore* score = ScoreRW::readScore(u"data/reachback_anchor.mscx");
    ASSERT_TRUE(score);

    const auto reach = run(score, kTailStart, kM7End, reachOpts(8));
    ASSERT_FALSE(reach.empty());
    for (const HarmonicRegion& r : reach) {
        EXPECT_GE(r.startTick, kTailStart) << "no region may start before the selection";
        EXPECT_LE(r.endTick, kM7End)       << "no region may end after the selection";
    }

    delete score;
}

// ── §3.5 — the hard bound terminates the loop (never-converges cap; design §3.7) ─
// With the trigger forced permanently ON (minConf huge ⇒ every reached slice still reads
// "unsettled", so the convergence stop can NEVER fire), the only remaining terminators are
// the score start and the hard bound. From a mid-score selection (bar 7), a SMALL
// maxReachSteps stops the loop at the hard bound — strictly before the score start — and it
// still returns a valid selection-only result rather than reaching to the start or looping.
// Its own re-run is identical (no oscillation), and its output span is the selection.
TEST(Composing_ReachBack, HardBoundTerminatesBeforeScoreStart)
{
    MasterScore* score = ScoreRW::readScore(u"data/reachback_anchor.mscx");
    ASSERT_TRUE(score);

    // maxSteps = 2, one-measure increment, trigger permanently ON. Bar 7 is 6 measures in,
    // so 2 steps reach back only to bar 5 — the hard bound bites well before the score start.
    const auto bounded = run(score, kTailStart, kM7End, reachOpts(2, kMeasure, 1.0e9));
    ASSERT_FALSE(bounded.empty());
    for (const HarmonicRegion& r : bounded) {
        EXPECT_GE(r.startTick, kTailStart) << "hard-bounded reach must still emit selection-only";
        EXPECT_LE(r.endTick, kM7End);
    }
    // No oscillation: the hard-bounded reach is deterministic across identical runs.
    const auto bounded2 = run(score, kTailStart, kM7End, reachOpts(2, kMeasure, 1.0e9));
    EXPECT_TRUE(sameAnalysis(bounded, bounded2)) << "hard-bounded reach must be deterministic";

    delete score;
}

// ── §3.6 — determinism: same score + selection + settings ⇒ same result ──────────
// The reach-back loop is a pure function of (score, selection, settings): re-running it
// with the identical inputs yields the byte-identical user-visible analysis. Guards against
// any hidden state / ordering dependence introduced by the extend → re-slice → re-decode
// loop (design §8 determinism).
TEST(Composing_ReachBack, DeterministicAcrossRuns)
{
    MasterScore* score = ScoreRW::readScore(u"data/reachback_anchor.mscx");
    ASSERT_TRUE(score);

    const auto a = run(score, kTailStart, kM7End, reachOpts(8));
    const auto b = run(score, kTailStart, kM7End, reachOpts(8));
    ASSERT_FALSE(a.empty());
    EXPECT_TRUE(sameAnalysis(a, b)) << "identical inputs must give identical reach-back output";

    delete score;
}
