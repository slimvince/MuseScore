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

// Seams part 2, partition P2b — the record-path variant of analyzeSection. Coverage for
// analyzeSectionFromRecord: it derives the shared AnalyzedSection from a joint::NotationRecord (built
// via produceNotationRecord on a real .mscx) faithfully to the record's published fields, applies the
// C1 two-mode key axis + the raw §3.3 gap in normalizedConfidence + the P1 gap-based assertive gate,
// re-collects per-segment tones from the L1 surface, ranks the chord-axis alternatives by content
// score, groups key areas via the shared helper, suspends the pedal fact, and honours the [from, to)
// overlap window + the null/degenerate guards. DORMANT: nothing in src/ calls the adapter.

#include <gtest/gtest.h>

#include <algorithm>
#include <limits>
#include <optional>
#include <string>
#include <vector>

#include "composing/analysis/section/sectionrecordadapter.h"
#include "composing/analysis/joint/jointnotationproducer.h"
#include "composing/analysis/joint/jointnotationrecord.h"
#include "composing/analysis/joint/jointrender.h"
#include "composing/analyzed_section.h"

#include "engraving/dom/masterscore.h"
#include "engraving/dom/pitchspelling.h"   // Tpc::TPC_C
#include "engraving/types/fraction.h"
#include "engraving/tests/utils/scorerw.h"

namespace an = mu::composing::analysis;
namespace joint = mu::composing::analysis::joint;
using mu::engraving::Fraction;
using mu::engraving::MasterScore;
using mu::engraving::ScoreRW;

namespace {
constexpr int kTpcC = static_cast<int>(mu::engraving::Tpc::TPC_C);
constexpr double kAssertiveGap = 1.055757;   // exposure_constants.json 0.8-gate chosen_gap_nats

// Independent mirror of the adapter's coarse-quality -> enum map (drives the seg.quality expectation
// through the PUBLIC jointOursQuality — an independent check of the pipeline, not a copy of the impl).
an::ChordQuality expectQuality(const std::string& fineQuality)
{
    const std::string q = joint::jointOursQuality(fineQuality);
    if (q == "Major") { return an::ChordQuality::Major; }
    if (q == "Minor") { return an::ChordQuality::Minor; }
    if (q == "Diminished") { return an::ChordQuality::Diminished; }
    if (q == "HalfDiminished") { return an::ChordQuality::HalfDiminished; }
    if (q == "Augmented") { return an::ChordQuality::Augmented; }
    return an::ChordQuality::Unknown;
}

// The expected degree index (0 = I .. 6 = VII) for a record segment: an unaltered diatonic Roman with
// no applied target, else -1. Mirrors recordFunctionDegree from the record's OWN degree/target fields.
int expectDegree(const joint::RecordSegment& seg)
{
    if (!seg.target.empty()) { return -1; }
    static const char* kRoman[7] = { "I", "II", "III", "IV", "V", "VI", "VII" };
    for (int i = 0; i < 7; ++i) {
        if (seg.degree == kRoman[i]) { return i; }
    }
    return -1;
}

// The expected §3.3 key-axis gap for a segment's slice: scores[committed] - max(others); nullopt when
// <2 scoreable candidates or no committed reading.
std::optional<double> expectGap(const joint::SegmentSlice& slice)
{
    const joint::PosteriorAxis& ax = slice.keyAxis;
    if (ax.committed < 0 || ax.committed >= static_cast<int>(ax.scores.size()) || ax.scores.size() < 2) {
        return std::nullopt;
    }
    double best = -std::numeric_limits<double>::infinity();
    for (size_t k = 0; k < ax.scores.size(); ++k) {
        if (static_cast<int>(k) == ax.committed) { continue; }
        best = std::max(best, ax.scores[k]);
    }
    return ax.scores[static_cast<size_t>(ax.committed)] - best;
}
} // namespace

// ── (1) the whole-span map: every record segment -> one faithful AnalyzedRegion ───────────────────────
TEST(SectionRecordAdapterTests, MapsRecordFieldsFaithfullyOverTheWholeSpan)
{
    MasterScore* sc = ScoreRW::readScore(u"data/pb_chorale.mscx");
    ASSERT_TRUE(sc) << "failed to read pb_chorale.mscx";

    const joint::NotationRecordResult rec = joint::produceNotationRecord(sc, "pb_chorale");
    ASSERT_TRUE(rec.ok) << rec.error;
    ASSERT_FALSE(rec.record.segments.empty());
    ASSERT_EQ(rec.record.slices.size(), rec.record.segments.size());

    const an::AnalyzedSection sec = an::analyzeSectionFromRecord(
        sc, Fraction::fromTicks(rec.record.spanStartTick),
        Fraction::fromTicks(rec.record.spanEndTick), {}, rec.record);

    // whole span -> 1:1 with the record's segments, in order.
    ASSERT_EQ(sec.regions.size(), rec.record.segments.size());

    bool anyTones = false;
    for (size_t i = 0; i < sec.regions.size(); ++i) {
        const an::AnalyzedRegion& r = sec.regions[i];
        const joint::RecordSegment& seg = rec.record.segments[i];
        const joint::SegmentSlice& slice = rec.record.slices[i];
        const std::string ctx = "seg " + std::to_string(i);

        EXPECT_EQ(r.startTick, seg.startTick) << ctx;
        EXPECT_EQ(r.endTick, seg.endTick) << ctx;
        EXPECT_TRUE(r.hasAnalyzedChord) << ctx;

        // committed identity, from the record's published facts
        EXPECT_EQ(r.chordResult.identity.rootPc, seg.rootPc.value_or(-1)) << ctx;
        const int expectRootTpc = seg.rootSpellingLof.has_value() ? *seg.rootSpellingLof + kTpcC : -1;
        EXPECT_EQ(r.chordResult.identity.rootTpc, expectRootTpc) << ctx;
        EXPECT_EQ(r.chordResult.identity.quality, expectQuality(seg.quality)) << ctx;
        EXPECT_FALSE(r.chordResult.identity.isPedalPoint) << ctx << " (pedal suspends on the record path)";

        // committed function
        EXPECT_EQ(r.chordResult.function.degree, expectDegree(seg)) << ctx;
        // invariant: A's degree is known iff the class is a plain diatonic degree (== diatonicToKey)
        EXPECT_EQ(r.chordResult.function.degree >= 0, seg.diatonicToKey) << ctx;
        EXPECT_EQ(r.chordResult.function.diatonicToKey, seg.diatonicToKey) << ctx;
        EXPECT_EQ(r.chordResult.function.keyTonicPc, seg.tonicPc) << ctx;

        // key/mode context — the C1 two-mode key
        EXPECT_EQ(r.keyModeResult.keySignatureFifths, seg.keySignatureFifths) << ctx;
        EXPECT_EQ(r.keyModeResult.tonicPc, seg.tonicPc) << ctx;
        const an::KeySigMode expectMode = seg.isMajor ? an::KeySigMode::Ionian : an::KeySigMode::Aeolian;
        EXPECT_EQ(r.keyModeResult.mode, expectMode) << ctx;
        EXPECT_EQ(r.chordResult.function.keyMode, expectMode) << ctx;
        // C1: never an exotic mode
        EXPECT_TRUE(r.keyModeResult.mode == an::KeySigMode::Ionian
                    || r.keyModeResult.mode == an::KeySigMode::Aeolian) << ctx;

        // the RAW §3.3 gap in normalizedConfidence (nats), and the P1 gap-based assertive gate
        const std::optional<double> gap = expectGap(slice);
        EXPECT_DOUBLE_EQ(r.keyModeResult.normalizedConfidence, gap.value_or(0.0)) << ctx;
        EXPECT_EQ(r.hasAssertiveExposure, gap.has_value() && *gap >= kAssertiveGap) << ctx;

        // alternatives: the chord-axis slice minus the committed reading, content-score descending
        const size_t committedDrop = (slice.chordAxis.committed >= 0
                                      && slice.chordAxis.committed < static_cast<int>(slice.chordAxis.labels.size()))
                                         ? 1u : 0u;
        EXPECT_EQ(r.alternatives.size(), slice.chordAxis.labels.size() - committedDrop) << ctx;
        for (size_t a = 1; a < r.alternatives.size(); ++a) {
            EXPECT_GE(r.alternatives[a - 1].identity.score, r.alternatives[a].identity.score) << ctx;
        }

        anyTones = anyTones || !r.tones.empty();
    }
    EXPECT_TRUE(anyTones) << "the score has notes — some region must carry re-collected tones";

    // key areas: cover the region span, ascending, every region assigned, adjacent areas distinct
    ASSERT_FALSE(sec.keyAreas.empty());
    EXPECT_EQ(sec.keyAreas.front().startTick, sec.regions.front().startTick);
    EXPECT_EQ(sec.keyAreas.back().endTick, sec.regions.back().endTick);
    for (size_t k = 1; k < sec.keyAreas.size(); ++k) {
        EXPECT_LE(sec.keyAreas[k - 1].endTick, sec.keyAreas[k].startTick);
        EXPECT_TRUE(sec.keyAreas[k].keyFifths != sec.keyAreas[k - 1].keyFifths
                    || sec.keyAreas[k].mode != sec.keyAreas[k - 1].mode)
            << "adjacent key areas must differ in (fifths, mode)";
    }
    for (const an::AnalyzedRegion& r : sec.regions) {
        EXPECT_GE(r.keyAreaId, 0);
        EXPECT_LT(r.keyAreaId, static_cast<int>(sec.keyAreas.size()));
    }

    delete sc;
}

// ── (2) the [from, to) window includes exactly the overlapping segments (unclipped) ───────────────────
TEST(SectionRecordAdapterTests, WindowSelectsOverlappingSegmentsUnclipped)
{
    MasterScore* sc = ScoreRW::readScore(u"data/pb_chorale.mscx");
    ASSERT_TRUE(sc);
    const joint::NotationRecordResult rec = joint::produceNotationRecord(sc, "pb_chorale");
    ASSERT_TRUE(rec.ok) << rec.error;
    ASSERT_GE(rec.record.segments.size(), 3u);

    // a window strictly inside the piece: from the 2nd segment's start to the 3rd segment's end.
    const int fromTick = rec.record.segments[1].startTick;
    const int toTick   = rec.record.segments[2].endTick;

    size_t expectCount = 0;
    for (const joint::RecordSegment& s : rec.record.segments) {
        if (s.endTick > fromTick && s.startTick < toTick) { ++expectCount; }
    }

    const an::AnalyzedSection sec = an::analyzeSectionFromRecord(
        sc, Fraction::fromTicks(fromTick), Fraction::fromTicks(toTick), {}, rec.record);

    EXPECT_EQ(sec.regions.size(), expectCount);
    for (const an::AnalyzedRegion& r : sec.regions) {
        // every mapped region overlaps the window and is NOT clipped to it
        EXPECT_GT(r.endTick, fromTick);
        EXPECT_LT(r.startTick, toTick);
    }
    // window bounds recorded on the section
    EXPECT_EQ(sec.startTick, fromTick);
    EXPECT_EQ(sec.endTick, toTick);

    delete sc;
}

// ── (3) the guards: a null score or a degenerate window returns an empty section ──────────────────────
TEST(SectionRecordAdapterTests, NullScoreAndDegenerateWindowReturnEmpty)
{
    // null score — returns immediately, never touches the record (a default-constructed record is fine)
    const an::AnalyzedSection nullSec = an::analyzeSectionFromRecord(
        nullptr, Fraction::fromTicks(0), Fraction::fromTicks(1920), {}, joint::NotationRecord{});
    EXPECT_TRUE(nullSec.regions.empty());
    EXPECT_TRUE(nullSec.keyAreas.empty());

    // to <= from — empty, even with a valid score
    MasterScore* sc = ScoreRW::readScore(u"data/pb_chorale.mscx");
    ASSERT_TRUE(sc);
    const joint::NotationRecordResult rec = joint::produceNotationRecord(sc, "pb_chorale");
    ASSERT_TRUE(rec.ok) << rec.error;

    const an::AnalyzedSection degen = an::analyzeSectionFromRecord(
        sc, Fraction::fromTicks(960), Fraction::fromTicks(960), {}, rec.record);
    EXPECT_TRUE(degen.regions.empty());
    EXPECT_TRUE(degen.keyAreas.empty());

    delete sc;
}
