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

// LAYER 4 — per-slice CHORD-SYMBOL decoder tests (Increment A).
//
// Two tiers, mirroring the Layer-3 decoder tests:
//   * SCORER-INDEPENDENT (decideSlice) — inject a candidate list (the projected
//     cube) by hand and assert the chosen chord, the confidence margin (to the
//     best DIFFERENT chord), the ranked-and-capped alternatives, the prevailing
//     (∪) union, and the "uncertain" mark, with no dependency on the chord scorer.
//   * NOTE-MODEL (end-to-end) — run the REAL decode() over Layer-1 note models
//     built from .mscx fixtures: a clean triad names that chord; the complete
//     candidate list is surfaced and ranked; redecodeRange reproduces a full
//     decode; determinism.

#include <gtest/gtest.h>

#include <algorithm>
#include <optional>
#include <vector>

#include "engraving/dom/masterscore.h"
#include "engraving/tests/utils/scorerw.h"

#include "composing/analysis/chord/chordslicedecoder.h"
#include "composing/analysis/notemodel/note_model.h"
#include "composing/analysis/slicing/slicer.h"

using mu::engraving::MasterScore;
using mu::engraving::ScoreRW;
using mu::composing::analysis::ChordQuality;
using mu::composing::analysis::KeySigMode;
using mu::composing::analysis::notemodel::NoteModel;
using mu::composing::analysis::slicing::changePointSlices;

namespace cs = mu::composing::analysis::chordslice;
using CSD = cs::ChordSliceDecoder;
using cs::ChordSliceCandidate;
using cs::ChordSliceDecoderPreferences;
using cs::SliceChord;
using cs::FocalNote;
using cs::MembershipResult;

namespace {

ChordSliceCandidate cand(int rootPc, ChordQuality quality, int bassPc, double score, int tie = 0)
{
    ChordSliceCandidate c;
    c.rootPc = rootPc;
    c.quality = quality;
    c.bassPc = bassPc;
    c.rootTpc = -1;
    c.bassTpc = -1;
    c.tiePriority = tie;
    c.score = score;
    return c;
}

// kMasks template indices used by the membership tests (mirrors harmonicfunctionlayer
// kMasks / chordanalyzer kTemplateIntervals): 0 = major triad {0,4,7}, 1 = Maj7
// {0,4,7,11}, 4 = minor triad {0,3,7}, 2 = dom7 {0,4,7,10}.
constexpr int kTieMajor = 0;
constexpr int kTieMaj7  = 1;
constexpr int kTieMinor = 4;

ChordSliceCandidate triad(int rootPc, ChordQuality q, int tie)
{
    return cand(rootPc, q, rootPc, 0.0, tie);
}

// A focal note: pitch + onset/release (ticks) + voice + the salience inputs.
FocalNote note(int pitch, int onset, int release, int voice, double metricWeight, double durationQn)
{
    FocalNote f;
    f.pitch = pitch;
    f.onset = onset;
    f.release = release;
    f.voice = voice;
    f.metricWeight = metricWeight;
    f.durationQn = durationQn;
    return f;
}

bool hasPc(const std::vector<int>& v, int pc)
{
    return std::find(v.begin(), v.end(), pc) != v.end();
}

} // namespace

// ════════════════════════════════════════════════════════════════════════════
// Scorer-independent core (decideSlice) — selection, confidence, alternatives.
// ════════════════════════════════════════════════════════════════════════════

TEST(Composing_DecodeChord, Decide_ChosenIsHighestScore)
{
    const std::vector<ChordSliceCandidate> cands = {
        cand(0, ChordQuality::Major, 0, 3.0),
        cand(9, ChordQuality::Minor, 9, 2.0),
        cand(5, ChordQuality::Major, 5, 1.0),
    };
    const SliceChord sc = CSD::decideSlice(0, cands, std::nullopt);
    EXPECT_TRUE(sc.hasChord);
    EXPECT_EQ(sc.chosen.rootPc, 0);
    EXPECT_EQ(sc.chosen.quality, ChordQuality::Major);
    EXPECT_TRUE(sc.chosen.bassIsRoot());
}

TEST(Composing_DecodeChord, Decide_ConfidenceIsMarginToBestDifferentChord)
{
    const std::vector<ChordSliceCandidate> cands = {
        cand(0, ChordQuality::Major, 0, 3.0),
        cand(9, ChordQuality::Minor, 9, 2.0),   // best DIFFERENT chord
        cand(5, ChordQuality::Major, 5, 1.0),
    };
    const SliceChord sc = CSD::decideSlice(0, cands, std::nullopt);
    EXPECT_DOUBLE_EQ(sc.confidence, 1.0);   // 3.0 − 2.0
    EXPECT_FALSE(sc.uncertain);             // margin 1.0 > 0.5 default
}

TEST(Composing_DecodeChord, Decide_LowMarginIsUncertain)
{
    const std::vector<ChordSliceCandidate> cands = {
        cand(0, ChordQuality::Major, 0, 3.0),
        cand(4, ChordQuality::Minor, 4, 2.9),   // a near-tie DIFFERENT chord
    };
    const SliceChord sc = CSD::decideSlice(0, cands, std::nullopt);
    EXPECT_NEAR(sc.confidence, 0.1, 1e-9);
    EXPECT_TRUE(sc.uncertain) << "a near-tie between two different chords is uncertain";
}

TEST(Composing_DecodeChord, Decide_InversionOfChosenIsNotADifferentChord)
{
    // Same chord (C major) at two basses + a genuinely different chord far below.
    const std::vector<ChordSliceCandidate> cands = {
        cand(0, ChordQuality::Major, 0, 3.0),   // C (root position) — chosen
        cand(0, ChordQuality::Major, 4, 2.9),   // C/E — SAME chord, not a competitor
        cand(2, ChordQuality::Minor, 2, 0.5),   // Dm — the only DIFFERENT chord
    };
    const SliceChord sc = CSD::decideSlice(0, cands, std::nullopt);
    EXPECT_EQ(sc.chosen.rootPc, 0);
    EXPECT_DOUBLE_EQ(sc.confidence, 2.5) << "margin is to Dm (0.5), not to the C/E inversion";
    EXPECT_FALSE(sc.uncertain);
}

TEST(Composing_DecodeChord, Decide_AlternativesRankedAndCapped)
{
    const std::vector<ChordSliceCandidate> cands = {
        cand(0, ChordQuality::Major, 0, 5.0),
        cand(7, ChordQuality::Major, 7, 3.0),
        cand(5, ChordQuality::Major, 5, 2.0),
        cand(2, ChordQuality::Minor, 2, 1.0),
    };
    ChordSliceDecoderPreferences p;
    p.topK = 2;
    const SliceChord sc = CSD::decideSlice(0, cands, std::nullopt, p);
    EXPECT_EQ(sc.chosen.rootPc, 0);
    ASSERT_EQ(sc.alternatives.size(), 2u) << "capped to topK";
    EXPECT_EQ(sc.alternatives[0].rootPc, 7) << "best alternative (G) ranked first";
    EXPECT_EQ(sc.alternatives[1].rootPc, 5);
}

TEST(Composing_DecodeChord, Decide_PrevailingChordKeptAliveBelowTopK)
{
    const std::vector<ChordSliceCandidate> cands = {
        cand(0, ChordQuality::Major, 0, 5.0),
        cand(7, ChordQuality::Major, 7, 4.0),
        cand(5, ChordQuality::Major, 5, 3.0),
        cand(4, ChordQuality::Minor, 4, 1.0),   // Em — below topK, but the prevailing
    };
    ChordSliceDecoderPreferences p;
    p.topK = 2;
    const std::optional<ChordSliceCandidate> prevailing = cand(4, ChordQuality::Minor, 4, 0.0);
    const SliceChord sc = CSD::decideSlice(0, cands, prevailing, p);

    ASSERT_GE(sc.alternatives.size(), 3u) << "topK alternatives PLUS the prevailing chord";
    const bool hasEm = std::any_of(sc.alternatives.begin(), sc.alternatives.end(),
                                   [](const ChordSliceCandidate& a) {
                                       return a.rootPc == 4 && a.quality == ChordQuality::Minor;
                                   });
    EXPECT_TRUE(hasEm) << "the prevailing chord is carried even though it fell below topK";
}

TEST(Composing_DecodeChord, Decide_PrevailingNotExpressibleIsNotForced)
{
    const std::vector<ChordSliceCandidate> cands = {
        cand(0, ChordQuality::Major, 0, 5.0),
        cand(7, ChordQuality::Major, 7, 4.0),
    };
    // Bb major is not among this slice's candidates → cannot be expressed here.
    const std::optional<ChordSliceCandidate> prevailing = cand(10, ChordQuality::Major, 10, 0.0);
    const SliceChord sc = CSD::decideSlice(0, cands, prevailing);
    const bool hasBb = std::any_of(sc.alternatives.begin(), sc.alternatives.end(),
                                   [](const ChordSliceCandidate& a) { return a.rootPc == 10; });
    EXPECT_FALSE(hasBb) << "an inexpressible prevailing chord is not forced into the alternatives";
}

TEST(Composing_DecodeChord, Decide_SingleChordNoCompetitorIsConfident)
{
    // Only one chord symbol present (C major at several basses): no DIFFERENT chord.
    const std::vector<ChordSliceCandidate> cands = {
        cand(0, ChordQuality::Major, 0, 3.0),
        cand(0, ChordQuality::Major, 4, 2.8),
        cand(0, ChordQuality::Major, 7, 2.5),
    };
    const SliceChord sc = CSD::decideSlice(0, cands, std::nullopt);
    EXPECT_EQ(sc.chosen.rootPc, 0);
    EXPECT_GT(sc.confidence, 1.0) << "no different chord → high-confidence sentinel";
    EXPECT_FALSE(sc.uncertain);
}

TEST(Composing_DecodeChord, Decide_EmptyCandidatesIsNoChord)
{
    const SliceChord sc = CSD::decideSlice(3, {}, std::nullopt);
    EXPECT_FALSE(sc.hasChord);
    EXPECT_TRUE(sc.uncertain);
    EXPECT_TRUE(sc.alternatives.empty());
    EXPECT_EQ(sc.sliceIndex, 3);
}

TEST(Composing_DecodeChord, Decide_DoesNotClassifyMembershipItself)
{
    // decideSlice is the scorer-independent SELECTION core; membership is a separate
    // step (classifyMembership, applied in decode's pass 2). decideSlice leaves the
    // sets empty — the membership tests below exercise classifyMembership directly.
    const std::vector<ChordSliceCandidate> cands = { cand(0, ChordQuality::Major, 0, 3.0) };
    const SliceChord sc = CSD::decideSlice(0, cands, std::nullopt);
    EXPECT_TRUE(sc.chordTonePcs.empty());
    EXPECT_TRUE(sc.nonChordTonePcs.empty());
}

// ════════════════════════════════════════════════════════════════════════════
// Membership (Increment B) — per-note chord-tone vs non-chord-tone, scorer-free.
// classifyMembership(chord, focal, window, prevChord, nextChord) injected by hand.
// ════════════════════════════════════════════════════════════════════════════

// A clean triad: every focal note is a template tone → all chord tones, no NCT.
TEST(Composing_DecodeChord, Memb_CleanTriadAllChordTones)
{
    const ChordSliceCandidate c = triad(0, ChordQuality::Major, kTieMajor);   // C major {0,4,7}
    const std::vector<FocalNote> focal = {
        note(60, 0, 1920, 3, 1.0, 4.0),   // C
        note(64, 0, 1920, 2, 1.0, 4.0),   // E
        note(67, 0, 1920, 1, 1.0, 4.0),   // G
    };
    const MembershipResult m = CSD::classifyMembership(c, focal, focal, std::nullopt, std::nullopt);
    EXPECT_TRUE(hasPc(m.chordTonePcs, 0));
    EXPECT_TRUE(hasPc(m.chordTonePcs, 4));
    EXPECT_TRUE(hasPc(m.chordTonePcs, 7));
    EXPECT_TRUE(m.nonChordTonePcs.empty());
    EXPECT_DOUBLE_EQ(m.implausibilityPenalty, 0.0);
}

// A weak, short, off-beat extra note (the D in {C,E,G,D}) is a non-chord tone —
// the over-read the membership decision recovers; the chord stays C major.
TEST(Composing_DecodeChord, Memb_WeakExtraIsNonChordTone)
{
    const ChordSliceCandidate c = triad(0, ChordQuality::Major, kTieMajor);   // C major
    const std::vector<FocalNote> focal = {
        note(60, 0, 1920, 3, 1.0, 4.0),   // C  (chord tone)
        note(64, 0, 1920, 2, 1.0, 4.0),   // E
        note(67, 0, 1920, 1, 1.0, 4.0),   // G
        note(62, 960, 1200, 0, 0.5, 0.25),// D — weak (subbeat) + short → embellishment
    };
    const MembershipResult m = CSD::classifyMembership(c, focal, focal, std::nullopt, std::nullopt);
    EXPECT_TRUE(hasPc(m.nonChordTonePcs, 2)) << "the weak short D is a non-chord tone";
    EXPECT_FALSE(hasPc(m.chordTonePcs, 2));
    EXPECT_DOUBLE_EQ(m.implausibilityPenalty, 0.0) << "an embellishment costs the chord nothing";
}

// A sustained, strong extra note (a 6th) is a chord-tone extension — it "falls out" of
// membership (design §5) and the basic triad is charged for absorbing it (the richer-chord
// selection feedback: a chord whose template already had it would not need to).
TEST(Composing_DecodeChord, Memb_StrongSustainedExtraIsChordToneExtension)
{
    const ChordSliceCandidate c = triad(0, ChordQuality::Major, kTieMajor);   // C major
    const std::vector<FocalNote> focal = {
        note(60, 0, 1920, 3, 1.0, 4.0),   // C
        note(64, 0, 1920, 2, 1.0, 4.0),   // E
        note(67, 0, 1920, 1, 1.0, 4.0),   // G
        note(69, 0, 1920, 0, 1.0, 4.0),   // A — strong + full length, no step → the 6th (Tier 2)
    };
    const MembershipResult m = CSD::classifyMembership(c, focal, focal, std::nullopt, std::nullopt);
    EXPECT_TRUE(hasPc(m.chordTonePcs, 9)) << "a sustained strong 6th is a chord tone (C6)";
    EXPECT_FALSE(hasPc(m.nonChordTonePcs, 9));
    EXPECT_GT(m.implausibilityPenalty, 0.0) << "the basic triad is charged for the strong extra it absorbs";
}

// A suspension: a tone held from the previous chord that resolves DOWN by step to a
// chord tone is a non-chord tone, even on a strong beat (design §6).
TEST(Composing_DecodeChord, Memb_SuspensionIsNonChordTone)
{
    const ChordSliceCandidate cMaj = triad(0, ChordQuality::Major, kTieMajor);   // C major {0,4,7}
    const ChordSliceCandidate dMin = triad(2, ChordQuality::Minor, kTieMinor);   // Dm {2,5,9}
    // Focal slice [0,480): C/E/G + a suspended D (pc 2, held from Dm), strong beat.
    const std::vector<FocalNote> focal = {
        note(60, 0, 480, 3, 1.0, 1.0),    // C
        note(64, 0, 480, 2, 1.0, 1.0),    // E
        note(67, 0, 480, 1, 1.0, 1.0),    // G
        note(62, 0, 480, 0, 1.0, 1.0),    // D — strong, but suspends from Dm
    };
    // Window adds the resolution note: D (62) → C (60), a whole step down, in voice 0.
    std::vector<FocalNote> window = focal;
    window.push_back(note(60, 480, 960, 0, 1.0, 1.0));   // C — the resolution (next slice)

    const MembershipResult m = CSD::classifyMembership(cMaj, focal, window,
                                                       std::optional<ChordSliceCandidate>(dMin),
                                                       std::nullopt);
    EXPECT_TRUE(hasPc(m.nonChordTonePcs, 2)) << "the suspended D resolving down to C is a non-chord tone";
    EXPECT_FALSE(hasPc(m.chordTonePcs, 2));
}

// A passing tone: stepwise in from a chord tone and stepwise out to a chord tone is a
// non-chord tone purely on its stepwise treatment (even if not metrically weak).
TEST(Composing_DecodeChord, Memb_PassingToneByStepwiseTreatment)
{
    const ChordSliceCandidate cMaj = triad(0, ChordQuality::Major, kTieMajor);   // C major
    // Voice 0 line C(60) → D(62) → E(64); the D is the focal passing tone, strong beat.
    const std::vector<FocalNote> focal = {
        note(62, 480, 960, 0, 1.0, 1.0),  // D — focal, between C and E by step
        note(67, 480, 960, 1, 1.0, 1.0),  // G — chord tone sounding with it
    };
    std::vector<FocalNote> window = focal;
    window.push_back(note(60, 0, 480, 0, 1.0, 1.0));     // C before (chord tone)
    window.push_back(note(64, 960, 1440, 0, 1.0, 1.0));  // E after (chord tone)

    const MembershipResult m = CSD::classifyMembership(cMaj, focal, window, std::nullopt, std::nullopt);
    EXPECT_TRUE(hasPc(m.nonChordTonePcs, 2)) << "D approached and left by step between chord tones is passing";
}

// Determinism: classifyMembership is a pure function of its inputs.
TEST(Composing_DecodeChord, Memb_Deterministic)
{
    const ChordSliceCandidate c = triad(0, ChordQuality::Major, kTieMajor);
    const std::vector<FocalNote> focal = {
        note(60, 0, 1920, 3, 1.0, 4.0),
        note(64, 0, 1920, 2, 1.0, 4.0),
        note(67, 0, 1920, 1, 1.0, 4.0),
        note(62, 960, 1200, 0, 0.5, 0.25),
    };
    const MembershipResult a = CSD::classifyMembership(c, focal, focal, std::nullopt, std::nullopt);
    const MembershipResult b = CSD::classifyMembership(c, focal, focal, std::nullopt, std::nullopt);
    EXPECT_EQ(a.chordTonePcs, b.chordTonePcs);
    EXPECT_EQ(a.nonChordTonePcs, b.nonChordTonePcs);
    EXPECT_DOUBLE_EQ(a.implausibilityPenalty, b.implausibilityPenalty);
}

// ════════════════════════════════════════════════════════════════════════════
// G1 — commit / inherit / abstain + sufficiency gate (design §4 step 3, §5 step 4).
// Scorer-free: a ranked SliceChord (from decideSlice) + injected focal notes +
// prevailing chord by hand, asserting the trichotomy. applyCommitDecision + the
// templateTonePresenceCount sufficiency source.
// ════════════════════════════════════════════════════════════════════════════

// The sufficiency source: count the chord's OWN template tones present, ignoring
// extras and duplicates — independent of the (extra-note) membership rule.
TEST(Composing_DecodeChord, G1_TemplateTonePresenceCount)
{
    const ChordSliceCandidate c = triad(0, ChordQuality::Major, kTieMajor);   // C major {0,4,7}
    const std::vector<FocalNote> full = {
        note(60, 0, 480, 0, 1.0, 1.0), note(64, 0, 480, 1, 1.0, 1.0), note(67, 0, 480, 2, 1.0, 1.0),
    };
    EXPECT_EQ(CSD::templateTonePresenceCount(c, full), 3) << "a complete triad present → 3";

    // C, E (template tones) + D (pc 2, an extra) → only 2 template tones count.
    const std::vector<FocalNote> dyadPlusExtra = {
        note(60, 0, 480, 0, 1.0, 1.0), note(64, 0, 480, 1, 1.0, 1.0), note(62, 0, 480, 2, 1.0, 1.0),
    };
    EXPECT_EQ(CSD::templateTonePresenceCount(c, dyadPlusExtra), 2)
        << "an extra (non-template) note does not count toward sufficiency";

    // C and its octave C → one distinct template pc.
    const std::vector<FocalNote> dupes = {
        note(60, 0, 480, 0, 1.0, 1.0), note(72, 0, 480, 1, 1.0, 1.0),
    };
    EXPECT_EQ(CSD::templateTonePresenceCount(c, dupes), 1) << "duplicate pcs counted once";
}

// A clear triad with a clear margin → COMMIT.
TEST(Composing_DecodeChord, G1_CleanTriadCommits)
{
    std::vector<ChordSliceCandidate> cands = {
        cand(0, ChordQuality::Major, 0, 3.0, kTieMajor),   // C major — chosen
        cand(9, ChordQuality::Minor, 9, 1.0, kTieMinor),   // a clearly-worse different chord
    };
    SliceChord sc = CSD::decideSlice(0, cands, std::nullopt);   // chosen C, margin 2.0, not uncertain
    const std::vector<FocalNote> focal = {
        note(60, 0, 1920, 3, 1.0, 4.0),   // C
        note(64, 0, 1920, 2, 1.0, 4.0),   // E
        note(67, 0, 1920, 1, 1.0, 4.0),   // G
    };
    CSD::applyCommitDecision(sc, focal, focal, std::nullopt, std::nullopt, std::nullopt);
    EXPECT_EQ(sc.decision, cs::SliceDecision::Commit);
    EXPECT_TRUE(sc.hasChord);
    EXPECT_EQ(sc.chosen.rootPc, 0);
}

// A phantom-root slice (the chosen chord has < 3 of its template tones present) with
// no consistent prevailing chord → ABSTAIN (no committed symbol).
TEST(Composing_DecodeChord, G1_PhantomRootAbstains)
{
    // Chosen F major {5,9,0}, but the slice sounds only C (pc 0 — F major's fifth):
    // a single template tone present, far short of a triad.
    std::vector<ChordSliceCandidate> cands = {
        cand(5, ChordQuality::Major, 5, 3.0, kTieMajor),   // F major — chosen
        cand(2, ChordQuality::Minor, 2, 0.5, kTieMinor),   // a far-below different reading
    };
    SliceChord sc = CSD::decideSlice(0, cands, std::nullopt);   // margin 2.5, not uncertain
    const std::vector<FocalNote> focal = { note(60, 0, 480, 0, 1.0, 1.0) };   // C only
    CSD::applyCommitDecision(sc, focal, focal, std::nullopt, std::nullopt, std::nullopt);
    EXPECT_EQ(sc.decision, cs::SliceDecision::Abstain)
        << "a new symbol is never committed from too few notes (the phantom-root rule)";
    EXPECT_FALSE(sc.hasChord);
    EXPECT_TRUE(sc.uncertain);
    EXPECT_FALSE(sc.alternatives.empty()) << "the competing readings are still carried";
}

// A thin slice that cannot fix its own chord, but whose notes are all template tones
// of the prevailing chord → INHERIT it (NOT a phantom new symbol).
TEST(Composing_DecodeChord, G1_ThinSliceInheritsPrevailing)
{
    // Prevailing A major {9,1,4}; the slice sounds a lone C# (pc 1) — A major's third
    // (the spec's phantom-root scenario). Its own top reading (some F#m) is insufficient.
    const std::optional<ChordSliceCandidate> prevailing =
        cand(9, ChordQuality::Major, 9, 0.0, kTieMajor);
    std::vector<ChordSliceCandidate> cands = {
        cand(6, ChordQuality::Minor, 6, 3.0, kTieMinor),   // an F#m reading on the thin slice
    };
    SliceChord sc = CSD::decideSlice(0, cands, prevailing);
    const std::vector<FocalNote> focal = { note(61, 0, 480, 0, 1.0, 1.0) };   // C# only (pc 1)
    CSD::applyCommitDecision(sc, focal, focal, prevailing, std::nullopt, std::nullopt);
    EXPECT_EQ(sc.decision, cs::SliceDecision::Inherit);
    EXPECT_TRUE(sc.hasChord);
    EXPECT_EQ(sc.chosen.rootPc, 9) << "inherits the prevailing A major";
    EXPECT_EQ(sc.chosen.quality, ChordQuality::Major);
    EXPECT_FALSE(sc.uncertain);
}

// A thin slice with a note FOREIGN to the prevailing chord cannot inherit → ABSTAIN.
TEST(Composing_DecodeChord, G1_ThinSliceForeignToPrevailingAbstains)
{
    // Prevailing A major {9,1,4}; the slice sounds a lone F (pc 5), foreign to A major.
    const std::optional<ChordSliceCandidate> prevailing =
        cand(9, ChordQuality::Major, 9, 0.0, kTieMajor);
    std::vector<ChordSliceCandidate> cands = {
        cand(5, ChordQuality::Major, 5, 3.0, kTieMajor),   // some F reading
    };
    SliceChord sc = CSD::decideSlice(0, cands, prevailing);
    const std::vector<FocalNote> focal = { note(65, 0, 480, 0, 1.0, 1.0) };   // F only (pc 5)
    CSD::applyCommitDecision(sc, focal, focal, prevailing, std::nullopt, std::nullopt);
    EXPECT_EQ(sc.decision, cs::SliceDecision::Abstain)
        << "a note foreign to the prevailing chord is not a consistent inherit";
    EXPECT_FALSE(sc.hasChord);
}

// A sufficient slice that nonetheless loses on margin → ABSTAIN (not commit, not inherit).
TEST(Composing_DecodeChord, G1_SufficientButLowMarginAbstains)
{
    std::vector<ChordSliceCandidate> cands = {
        cand(0, ChordQuality::Major, 0, 3.0, kTieMajor),
        cand(9, ChordQuality::Minor, 9, 2.9, kTieMinor),   // a near-tie different chord
    };
    SliceChord sc = CSD::decideSlice(0, cands, std::nullopt);   // margin 0.1 → uncertain
    ASSERT_TRUE(sc.uncertain);
    const std::vector<FocalNote> focal = {
        note(60, 0, 1920, 3, 1.0, 4.0),   // C
        note(64, 0, 1920, 2, 1.0, 4.0),   // E
        note(67, 0, 1920, 1, 1.0, 4.0),   // G  (a full triad → sufficient)
    };
    CSD::applyCommitDecision(sc, focal, focal, std::nullopt, std::nullopt, std::nullopt);
    EXPECT_EQ(sc.decision, cs::SliceDecision::Abstain)
        << "passing sufficiency but failing margin → abstain, never a forced commit";
    EXPECT_FALSE(sc.hasChord);
}

// The master switch OFF reproduces the pre-G1 always-commit behaviour exactly.
TEST(Composing_DecodeChord, G1_DisabledReproducesAlwaysCommit)
{
    ChordSliceDecoderPreferences p;
    p.enableCommitDecision = false;
    // A slice that WOULD abstain under G1 (F major chosen, only its fifth C present).
    std::vector<ChordSliceCandidate> cands = { cand(5, ChordQuality::Major, 5, 3.0, kTieMajor) };
    SliceChord sc = CSD::decideSlice(0, cands, std::nullopt, p);
    const std::vector<FocalNote> focal = { note(60, 0, 480, 0, 1.0, 1.0) };   // C only
    CSD::applyCommitDecision(sc, focal, focal, std::nullopt, std::nullopt, std::nullopt, p);
    EXPECT_EQ(sc.decision, cs::SliceDecision::Commit) << "G1 off → always commit the top candidate";
    EXPECT_TRUE(sc.hasChord);
    EXPECT_EQ(sc.chosen.rootPc, 5);
}

// ════════════════════════════════════════════════════════════════════════════
// G2/G3 — the three-tier structure-first membership ladder + the plausibility check
// (design §5 step 3). Scorer-free: classifyMembership injected by hand, asserting each
// tier, the C-vs-Cadd9 / spurious-seventh discriminator, and the inherit-via-stepwise-NCT
// relaxation that G1 (template-only) abstained on.
// ════════════════════════════════════════════════════════════════════════════

// Tier 1 — an ACCENTED passing tone (stepwise in AND out, between chord tones, on a
// STRONG full beat) is a non-chord tone REGARDLESS of metric weight (metric weight alone
// would wrongly call the accented note a chord tone).
TEST(Composing_DecodeChord, Memb_Tier1_AccentedPassingToneIsNonChordTone)
{
    const ChordSliceCandidate cMaj = triad(0, ChordQuality::Major, kTieMajor);   // C major {0,4,7}
    const std::vector<FocalNote> focal = {
        note(62, 480, 960, 0, 1.0, 1.0),   // D — focal, STRONG + full length
        note(67, 480, 960, 1, 1.0, 1.0),   // G — chord tone sounding under it
    };
    std::vector<FocalNote> window = focal;
    window.push_back(note(60, 0, 480, 0, 1.0, 1.0));     // C before (step in, chord tone)
    window.push_back(note(64, 960, 1440, 0, 1.0, 1.0));  // E after  (step out, chord tone)
    const MembershipResult m = CSD::classifyMembership(cMaj, focal, window, std::nullopt, std::nullopt);
    EXPECT_TRUE(hasPc(m.nonChordTonePcs, 2)) << "an accented passing tone is a non-chord tone (Tier 1)";
    EXPECT_FALSE(hasPc(m.chordTonePcs, 2));
}

// Tier 2 — a WEAK leap (reached AND left by leap: an arpeggiated tone) is a chord-tone
// extension REGARDLESS of metric weight (metric weight alone would wrongly call the weak
// note an embellishment). This is the headline Tier-2 fix vs the old flat weak-OR-stepwise
// rule, which classified this weak note as a non-chord tone.
TEST(Composing_DecodeChord, Memb_Tier2_WeakLeapIsChordToneExtension)
{
    const ChordSliceCandidate cMaj = triad(0, ChordQuality::Major, kTieMajor);   // C major {0,4,7}
    const std::vector<FocalNote> focal = {
        note(69, 480, 720, 0, 0.5, 0.25),   // A — focal (the 6th), WEAK + short
        note(60, 480, 720, 1, 0.5, 0.25),   // C — chord tone under it
    };
    std::vector<FocalNote> window = focal;
    window.push_back(note(64, 0, 480, 0, 1.0, 1.0));     // E before (leap up to A — a fourth)
    window.push_back(note(72, 720, 1200, 0, 1.0, 1.0));  // C after  (leap down from A — a third)
    const MembershipResult m = CSD::classifyMembership(cMaj, focal, window, std::nullopt, std::nullopt);
    EXPECT_TRUE(hasPc(m.chordTonePcs, 9)) << "a weak arpeggiated leap is a chord-tone extension (Tier 2)";
    EXPECT_FALSE(hasPc(m.nonChordTonePcs, 9));
    EXPECT_GT(m.implausibilityPenalty, 0.0)
        << "the triad is charged for absorbing the leap as an extension (richer-chord feedback)";
}

// Tier 3 — a STRONG appoggiatura (leapt to, resolved by step into a chord tone) is a
// non-chord tone even on a strong beat (the stepwise resolution overrides the weight).
TEST(Composing_DecodeChord, Memb_Tier3_StrongAppoggiaturaIsNonChordTone)
{
    const ChordSliceCandidate cMaj = triad(0, ChordQuality::Major, kTieMajor);   // C major {0,4,7}
    const std::vector<FocalNote> focal = {
        note(65, 480, 960, 0, 1.0, 1.0),   // F — focal appoggiatura (pc 5), STRONG
        note(60, 480, 960, 1, 1.0, 1.0),   // C — chord tone under it
    };
    std::vector<FocalNote> window = focal;
    window.push_back(note(60, 0, 480, 0, 1.0, 1.0));     // C before (leap up to F — a fourth)
    window.push_back(note(64, 960, 1440, 0, 1.0, 1.0));  // E after  (step down — the resolution)
    const MembershipResult m = CSD::classifyMembership(cMaj, focal, window, std::nullopt, std::nullopt);
    EXPECT_TRUE(hasPc(m.nonChordTonePcs, 5)) << "a strong appoggiatura resolving by step is a non-chord tone (Tier 3)";
    EXPECT_FALSE(hasPc(m.chordTonePcs, 5));
}

// Tier 3 — an ESCAPE tone (approached by step from a chord tone, left by leap) is the
// genuinely-ambiguous one-sided case: metric weight adjudicates. Weak → non-chord tone;
// metrically asserted → chord-tone extension.
TEST(Composing_DecodeChord, Memb_Tier3_EscapeToneDecidedByWeight)
{
    const ChordSliceCandidate cMaj = triad(0, ChordQuality::Major, kTieMajor);   // C major {0,4,7}

    // weak escape → non-chord tone
    {
        const std::vector<FocalNote> focal = {
            note(62, 480, 960, 0, 0.5, 0.25),   // D — focal, WEAK + short
            note(67, 480, 960, 1, 1.0, 1.0),    // G — chord tone under it
        };
        std::vector<FocalNote> window = focal;
        window.push_back(note(60, 0, 480, 0, 1.0, 1.0));     // C before (step in, chord tone)
        window.push_back(note(69, 960, 1440, 0, 1.0, 1.0));  // A after  (leap out)
        const MembershipResult m = CSD::classifyMembership(cMaj, focal, window, std::nullopt, std::nullopt);
        EXPECT_TRUE(hasPc(m.nonChordTonePcs, 2)) << "a weak escape tone is a non-chord tone (Tier 3, by weight)";
    }
    // metrically asserted escape → chord-tone extension
    {
        const std::vector<FocalNote> focal = {
            note(62, 480, 960, 0, 1.0, 1.0),    // D — focal, STRONG + full length
            note(67, 480, 960, 1, 1.0, 1.0),    // G — chord tone under it
        };
        std::vector<FocalNote> window = focal;
        window.push_back(note(60, 0, 480, 0, 1.0, 1.0));     // C before (step in, chord tone)
        window.push_back(note(69, 960, 1440, 0, 1.0, 1.0));  // A after  (leap out)
        const MembershipResult m = CSD::classifyMembership(cMaj, focal, window, std::nullopt, std::nullopt);
        EXPECT_TRUE(hasPc(m.chordTonePcs, 2)) << "a metrically asserted escape tone is a chord-tone extension (Tier 3, by weight)";
    }
}

// G3 plausibility — the REQUIRED (template) tones are run through the SAME ladder. A
// required 7th that behaves as a Tier-1 embellishment (a lower NEIGHBOUR of the root)
// makes the candidate IMPLAUSIBLE — a spurious seventh — so the candidate is charged. A
// genuine sustained 7th is not. (This is what the old penalty, which tested EXTRA notes,
// could not catch — Step-0 G3 "tests the wrong tones".)
TEST(Composing_DecodeChord, Memb_G3_PlausibilityChargesImplausibleRequiredTone)
{
    // Cmaj7 {0,4,7,11} — quality is the coarse Major category; tie kTieMaj7 carries the
    // four-note template (membership keys off rootPc + tiePriority, not the quality field).
    const ChordSliceCandidate cMaj7 = cand(0, ChordQuality::Major, 0, 0.0, kTieMaj7);

    // (a) the required B (pc 11) is a lower NEIGHBOUR of the root: C(72) → B(71) → C(72).
    const std::vector<FocalNote> nbrFocal = {
        note(71, 480, 960, 0, 1.0, 1.0),   // B — focal (the would-be 7th), strong
        note(60, 480, 960, 1, 1.0, 1.0),   // C — root under it
        note(67, 480, 960, 2, 1.0, 1.0),   // G — fifth
    };
    std::vector<FocalNote> nbrWindow = nbrFocal;
    nbrWindow.push_back(note(72, 0, 480, 0, 1.0, 1.0));     // C before (step down to B)
    nbrWindow.push_back(note(72, 960, 1440, 0, 1.0, 1.0));  // C after  (step up — neighbour return)
    const MembershipResult mn = CSD::classifyMembership(cMaj7, nbrFocal, nbrWindow, std::nullopt, std::nullopt);
    EXPECT_GT(mn.implausibilityPenalty, 0.0)
        << "a required 7th behaving as a neighbour tone makes the candidate implausible (G3)";
    EXPECT_TRUE(hasPc(mn.chordTonePcs, 11)) << "the required tone is still a chord tone of the chosen chord";

    // (b) a genuine sustained 7th (no stepwise embellishment) is plausible — not charged.
    const std::vector<FocalNote> genuine = {
        note(71, 0, 1920, 0, 1.0, 4.0),   // B — sustained, isolated
        note(60, 0, 1920, 1, 1.0, 4.0),   // C
        note(67, 0, 1920, 2, 1.0, 4.0),   // G
    };
    const MembershipResult mg = CSD::classifyMembership(cMaj7, genuine, genuine, std::nullopt, std::nullopt);
    EXPECT_DOUBLE_EQ(mg.implausibilityPenalty, 0.0) << "a genuine (non-embellishing) 7th is plausible — no charge";
}

// G2 discriminator — C vs Cadd9: whether the extra D of {C,E,G,D} is a chord tone (Cadd9)
// or a passing tone (plain C) is the membership decision. A passing D → non-chord tone; a
// sustained structural D → chord-tone extension (the added 9th).
TEST(Composing_DecodeChord, Memb_G2_CVsCadd9Discriminator)
{
    const ChordSliceCandidate cMaj = triad(0, ChordQuality::Major, kTieMajor);   // C major {0,4,7}

    // passing D → non-chord tone (plain C)
    const std::vector<FocalNote> passFocal = {
        note(62, 480, 960, 0, 1.0, 1.0),   // D — focal, between C and E by step
        note(67, 480, 960, 1, 1.0, 1.0),   // G
    };
    std::vector<FocalNote> passWindow = passFocal;
    passWindow.push_back(note(60, 0, 480, 0, 1.0, 1.0));     // C before
    passWindow.push_back(note(64, 960, 1440, 0, 1.0, 1.0));  // E after
    const MembershipResult mp = CSD::classifyMembership(cMaj, passFocal, passWindow, std::nullopt, std::nullopt);
    EXPECT_TRUE(hasPc(mp.nonChordTonePcs, 2)) << "a passing D is a non-chord tone → plain C";
    EXPECT_FALSE(hasPc(mp.chordTonePcs, 2));

    // structural D (sustained, no step) → chord-tone extension (Cadd9)
    const std::vector<FocalNote> structFocal = {
        note(60, 0, 1920, 3, 1.0, 4.0),   // C
        note(64, 0, 1920, 2, 1.0, 4.0),   // E
        note(67, 0, 1920, 1, 1.0, 4.0),   // G
        note(62, 0, 1920, 0, 1.0, 4.0),   // D — strong, sustained, no step → the added 9th
    };
    const MembershipResult ms = CSD::classifyMembership(cMaj, structFocal, structFocal, std::nullopt, std::nullopt);
    EXPECT_TRUE(hasPc(ms.chordTonePcs, 2)) << "a sustained structural D is a chord-tone extension → Cadd9";
    EXPECT_FALSE(hasPc(ms.nonChordTonePcs, 2));
}

// Inherit-via-stepwise-NCT (the G2 relaxation of the G1 inherit). A thin slice whose extra
// note is a stepwise embellishment (non-chord tone) of the prevailing chord now INHERITS it
// — where G1's template-only consistency ABSTAINED. Demonstrated by the same slice inheriting
// with the window (G2 ladder) but abstaining with an empty window (the old template-only read).
TEST(Composing_DecodeChord, G2_InheritsThroughStepwiseNct)
{
    const std::optional<ChordSliceCandidate> prevailing =
        cand(0, ChordQuality::Major, 0, 0.0, kTieMajor);   // prevailing C major {0,4,7}
    // The slice's own best reading is insufficient (F major — only its root F present).
    std::vector<ChordSliceCandidate> cands = { cand(5, ChordQuality::Major, 5, 3.0, kTieMajor) };
    SliceChord ranked = CSD::decideSlice(0, cands, prevailing);

    // Slice = E (a chord tone of C) + a passing F (voice-0 E→F→G, stepwise between the C
    // chord tones E and G). F is NOT a template tone of C, so G1 (template-only) abstained.
    const std::vector<FocalNote> focal = {
        note(65, 480, 960, 0, 1.0, 1.0),   // F — focal passing tone (pc 5)
        note(64, 480, 960, 1, 1.0, 1.0),   // E — chord tone of C (pc 4)
    };
    std::vector<FocalNote> window = focal;
    window.push_back(note(64, 0, 480, 0, 1.0, 1.0));     // E before (step to F)
    window.push_back(note(67, 960, 1440, 0, 1.0, 1.0));  // G after  (step from F)

    // With the window (the G2 ladder): F is a passing NCT of C → all notes consistent → INHERIT.
    SliceChord scInherit = ranked;
    CSD::applyCommitDecision(scInherit, focal, window, prevailing, std::nullopt, std::nullopt);
    EXPECT_EQ(scInherit.decision, cs::SliceDecision::Inherit)
        << "a thin slice + a stepwise NCT of the prevailing chord inherits it (G2 relaxation)";
    EXPECT_EQ(scInherit.chosen.rootPc, 0);
    EXPECT_EQ(scInherit.chosen.quality, ChordQuality::Major);

    // Empty window (the Step-1 template-only reading): F has no melodic neighbours → it
    // classifies structural → inconsistent → ABSTAIN (the G1 behaviour the relaxation supersedes).
    SliceChord scAbstain = ranked;
    CSD::applyCommitDecision(scAbstain, focal, {}, prevailing, std::nullopt, std::nullopt);
    EXPECT_EQ(scAbstain.decision, cs::SliceDecision::Abstain)
        << "without the window, F reads structural → abstain (the superseded template-only G1 inherit)";
}

// ════════════════════════════════════════════════════════════════════════════
// NOTE-MODEL (end-to-end) — real decode() over Layer-1 models from .mscx fixtures.
// ════════════════════════════════════════════════════════════════════════════

// A clean C-major triad slice then a clean G-major triad slice each name THAT
// chord, root-position. contextSlices=0 isolates each slice (the default ±1
// window would pool the two triads — the over-read Increment B's membership
// addresses; here we test the per-slice naming in isolation).
TEST(Composing_DecodeChord, Fixture_CleanTriads_NameThatChord)
{
    MasterScore* score = ScoreRW::readScore(u"data/s1c_c_major.mscx");
    ASSERT_TRUE(score);
    const NoteModel model = NoteModel::build(score);
    const auto slices = changePointSlices(model);
    ASSERT_EQ(slices.size(), 2u) << "two whole-note triads → two constant-sonority slices";

    ChordSliceDecoderPreferences p;
    p.contextSlices = 0;   // window = the slice alone (isolate each triad)
    const auto d = CSD::decode(slices, model, /*keySigFifths=*/0, KeySigMode::Ionian,
                               mu::composing::analysis::kDefaultChordAnalyzerPreferences, p);
    ASSERT_EQ(d.size(), 2u);

    EXPECT_TRUE(d[0].hasChord);
    EXPECT_EQ(d[0].chosen.rootPc, 0) << "slice 0 is C major";
    EXPECT_EQ(d[0].chosen.quality, ChordQuality::Major);
    EXPECT_TRUE(d[0].chosen.bassIsRoot());

    EXPECT_TRUE(d[1].hasChord);
    EXPECT_EQ(d[1].chosen.rootPc, 7) << "slice 1 is G major";
    EXPECT_EQ(d[1].chosen.quality, ChordQuality::Major);
    EXPECT_TRUE(d[1].chosen.bassIsRoot());

    delete score;
}

// The complete candidate list is surfaced and ranked: every named slice carries
// alternatives, the chosen is the top-scoring candidate, and the alternatives are
// in non-increasing score order.
TEST(Composing_DecodeChord, Fixture_CompleteCandidateListSurfacedAndRanked)
{
    MasterScore* score = ScoreRW::readScore(u"data/s1c_seg_changes.mscx");
    ASSERT_TRUE(score);
    const NoteModel model = NoteModel::build(score);
    const auto slices = changePointSlices(model);
    ASSERT_GE(slices.size(), 4u);

    const auto d = CSD::decode(slices, model, /*keySigFifths=*/0, KeySigMode::Ionian);
    ASSERT_EQ(d.size(), slices.size());

    int named = 0;
    for (const SliceChord& sc : d) {
        if (!sc.hasChord) {
            continue;
        }
        ++named;
        // The chosen is at least as good as the best carried alternative (ranked) —
        // but only for a COMMITTED slice: an Inherit replaces the chosen with the
        // prevailing chord, which may score below a carried alternative here.
        if (sc.decision == cs::SliceDecision::Commit) {
            for (const ChordSliceCandidate& a : sc.alternatives) {
                EXPECT_LE(a.score, sc.chosen.score) << "alternatives never outrank a committed chosen";
            }
        }
        // Alternatives are in non-increasing score order (the ranking, independent of G1).
        for (size_t i = 1; i < sc.alternatives.size(); ++i) {
            EXPECT_LE(sc.alternatives[i].score, sc.alternatives[i - 1].score);
        }
    }
    EXPECT_GT(named, 0) << "the progression names at least one chord";

    delete score;
}

TEST(Composing_DecodeChord, Fixture_Determinism)
{
    MasterScore* score = ScoreRW::readScore(u"data/s1c_seg_changes.mscx");
    ASSERT_TRUE(score);
    const NoteModel model = NoteModel::build(score);
    const auto slices = changePointSlices(model);

    const auto a = CSD::decode(slices, model, 0, KeySigMode::Ionian);
    const auto b = CSD::decode(slices, model, 0, KeySigMode::Ionian);
    ASSERT_EQ(a.size(), b.size());
    for (size_t i = 0; i < a.size(); ++i) {
        EXPECT_EQ(a[i].hasChord, b[i].hasChord);
        EXPECT_EQ(a[i].chosen.rootPc, b[i].chosen.rootPc);
        EXPECT_EQ(a[i].chosen.quality, b[i].chosen.quality);
        EXPECT_EQ(a[i].chosen.bassPc, b[i].chosen.bassPc);
        EXPECT_DOUBLE_EQ(a[i].confidence, b[i].confidence);
        EXPECT_EQ(a[i].uncertain, b[i].uncertain);
    }

    delete score;
}

// A sub-range re-decode reproduces the matching slices of a full decode EXACTLY
// (the per-slice decision is context-free; one slice of look-back recovers the
// prevailing chord of the first slice).
TEST(Composing_DecodeChord, Fixture_RedecodeRange_MatchesFullDecode)
{
    MasterScore* score = ScoreRW::readScore(u"data/s1c_seg_changes.mscx");
    ASSERT_TRUE(score);
    const NoteModel model = NoteModel::build(score);
    const auto slices = changePointSlices(model);
    ASSERT_GE(slices.size(), 3u);

    const auto full = CSD::decode(slices, model, 0, KeySigMode::Ionian);
    const int first = 1;
    const int last = static_cast<int>(slices.size()) - 1;
    const auto sub = CSD::redecodeRange(slices, model, 0, KeySigMode::Ionian, first, last);

    ASSERT_EQ(sub.size(), static_cast<size_t>(last - first + 1));
    for (size_t i = 0; i < sub.size(); ++i) {
        EXPECT_EQ(sub[i].sliceIndex, first + static_cast<int>(i));
        EXPECT_EQ(sub[i].hasChord, full[first + i].hasChord);
        EXPECT_EQ(sub[i].chosen.rootPc, full[first + i].chosen.rootPc) << "slice " << (first + i);
        EXPECT_EQ(sub[i].chosen.quality, full[first + i].chosen.quality) << "slice " << (first + i);
        EXPECT_EQ(sub[i].chosen.bassPc, full[first + i].chosen.bassPc) << "slice " << (first + i);
        EXPECT_DOUBLE_EQ(sub[i].confidence, full[first + i].confidence) << "slice " << (first + i);
    }

    delete score;
}

// End-to-end G1 invariant: in a real decode (G1 on by default), every slice's
// commit/inherit/abstain decision is consistent with hasChord — Abstain ⟺ no
// committed chord; Commit/Inherit ⟺ a committed chord.
TEST(Composing_DecodeChord, G1_DecodeDecisionConsistentWithHasChord)
{
    MasterScore* score = ScoreRW::readScore(u"data/s1c_seg_changes.mscx");
    ASSERT_TRUE(score);
    const NoteModel model = NoteModel::build(score);
    const auto slices = changePointSlices(model);
    const auto d = CSD::decode(slices, model, 0, KeySigMode::Ionian);   // default prefs: G1 on
    ASSERT_EQ(d.size(), slices.size());
    for (const SliceChord& sc : d) {
        if (sc.decision == cs::SliceDecision::Abstain) {
            EXPECT_FALSE(sc.hasChord) << "an abstain commits no chord (slice " << sc.sliceIndex << ")";
        } else {
            EXPECT_TRUE(sc.hasChord) << "a commit/inherit carries a chord (slice " << sc.sliceIndex << ")";
        }
    }
    delete score;
}

TEST(Composing_DecodeChord, EmptyModel_NoSlices)
{
    const std::vector<mu::composing::analysis::slicing::Slice> noSlices;
    const NoteModel empty;
    EXPECT_TRUE(CSD::decode(noSlices, empty, 0, KeySigMode::Ionian).empty());
}
