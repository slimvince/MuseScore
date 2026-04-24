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

// ── pipeline_snapshot_tests ──────────────────────────────────────────────────
//
// Phase 1b safety net for the unified-pipeline refactor
// (docs/unified_analysis_pipeline.md).  Captures current user-facing output of
// the four analysis paths against a fixed 10-score corpus so behavior
// preservation can be verified before, during, and after the refactor.
//
// Paths captured per score:
//   P1 Implode        — regions out of prepareUserFacingHarmonicRegions (the
//                       exact input populateChordTrack consumes).  See
//                       corpus/README.md for the rationale — this phase treats
//                       the region list as the pinned observable rather than
//                       re-parsing emitted chord-track pitches.
//   P2 Annotation     — Harmony elements written by addHarmonicAnnotationsToSelection.
//   P3 Tick-regional  — analyzeHarmonicContextAtTick at one-per-measure-downbeat
//                       plus one-mid-measure ticks, with wasRegional flag.
//   P4 Tick-local     — analyzeHarmonicContextLocallyAtTick (exposed in
//                       Phase 2) at the same sample ticks as tickRegional.
//                       Divergence A (Policy #2) is observable two ways:
//                       tickRegional[].wasRegional=false marks a P3→P4
//                       fallback, and tickLocal vs. tickRegional entries at
//                       the same tick show how the two paths disagree when
//                       both produce a result.
//
// Running:
//   ./pipeline_snapshot_tests.exe --update-goldens   # write/refresh baselines
//   ./pipeline_snapshot_tests.exe                    # compare against baselines
//
// The update flag is also accepted via the PIPELINE_SNAPSHOT_UPDATE=1
// environment variable.  The flag is a developer-local tool — CI never sets it.

#include <algorithm>
#include <cmath>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

#include <gtest/gtest.h>

#include <QCoreApplication>
#include <QDir>
#include <QFile>
#include <QFileInfo>
#include <QIODevice>
#include <QJsonArray>
#include <QJsonDocument>
#include <QJsonObject>
#include <QJsonValue>
#include <QString>

#include "global/types/translatablestring.h"

#include "engraving/dom/chord.h"
#include "engraving/dom/harmony.h"
#include "engraving/dom/masterscore.h"
#include "engraving/dom/measure.h"
#include "engraving/dom/segment.h"
#include "engraving/dom/select.h"
#include "engraving/types/constants.h"

#include "engraving/tests/utils/scorerw.h"

#include "modularity/ioc.h"

#include "composing/analysis/chord/chordanalyzer.h"
#include "composing/analysis/key/keymodeanalyzer.h"
#include "composing/analysis/region/harmonicrhythm.h"
#include "composing/icomposinganalysisconfiguration.h"

#include "notation/internal/notationcomposingbridge.h"
#include "notation/internal/notationcomposingbridgehelpers.h"

using mu::engraving::Constants;
using mu::engraving::Fraction;
using mu::engraving::Harmony;
using mu::engraving::HarmonyType;
using mu::engraving::MasterScore;
using mu::engraving::Measure;
using mu::engraving::ScoreRW;
using mu::engraving::Segment;
using mu::engraving::SegmentType;
using mu::engraving::staff_idx_t;
using mu::engraving::toHarmony;
using mu::notation::NoteHarmonicContext;
using mu::composing::analysis::ChordAnalysisResult;
using mu::composing::analysis::ChordQuality;
using mu::composing::analysis::HarmonicRegion;
using mu::composing::analysis::KeySigMode;

namespace {

// ── Corpus ───────────────────────────────────────────────────────────────────

struct CorpusEntry {
    const char* id;               // Snapshot file stem.  ASCII-only, safe to use as a filename.
    const char* relativePath;     // Path under PIPELINE_SNAPSHOT_CORPUS_ROOT.
    const char* description;      // Human-readable note for READMEs and test output.
};

// Keep this list in sync with corpus/README.md.
constexpr CorpusEntry kCorpus[] = {
    { "bach_chorale_001",
      "tools/dcml/bach_chorales/MS3/001 Aus meines Herzens Grunde.mscx",
      "SATB Bach chorale — dense 4-voice functional-tonal baseline." },

    { "bach_chorale_003",
      "tools/dcml/bach_chorales/MS3/003 Ach Gott, vom Himmel sieh darein.mscx",
      "Second Bach chorale — modal colouring and cadence variety." },

    { "bach_bwv806_prelude",
      "tools/dcml/bach_en_fr_suites/MS3/BWV806_01_Prelude.mscx",
      "Bach English Suite BWV 806 Prelude — substitutes for a two-voice invention (DCML has no inventions; keyboard prelude covers contrapuntal keyboard texture)." },

    { "bach_bwv806_gigue",
      "tools/dcml/bach_en_fr_suites/MS3/BWV806_10_Gigue.mscx",
      "Bach English Suite BWV 806 Gigue — substitutes for a fugue (DCML has no 48-style fugues; gigue gives dance-form imitation)." },

    { "mozart_k279_1",
      "tools/dcml/mozart_piano_sonatas/MS3/K279-1.mscx",
      "Mozart Piano Sonata K.279 mvt. 1 — Classical-era exposition already used as a chord-analyzer fixture." },

    { "mozart_k280_1",
      "tools/dcml/mozart_piano_sonatas/MS3/K280-1.mscx",
      "Mozart Piano Sonata K.280 mvt. 1 — substitutes for the Haydn string quartet slot (DCML has no Haydn)." },

    { "chopin_bi105_op30_1",
      "tools/dcml/chopin_mazurkas/MS3/BI105-1op30-1.mscx",
      "Chopin Mazurka Op. 30 No. 1 — substitutes for the Chopin prelude slot (DCML has mazurkas but no preludes)." },

    { "chopin_bi105_op30_2",
      "tools/dcml/chopin_mazurkas/MS3/BI105-2op30-2.mscx",
      "Chopin Mazurka Op. 30 No. 2 — substitutes for the Brahms intermezzo slot (DCML has no Brahms); adds modulation and chromatic colour." },

    { "corelli_op01n08a",
      "tools/dcml/corelli/MS3/op01n08a.mscx",
      "Corelli Trio Sonata Op. 1 No. 8 movement a — cadence-heavy Baroque corpus ground already used as an implode fixture." },

    { "schumann_kinderszenen_n01",
      "tools/dcml/schumann_kinderszenen/MS3/n01.mscx",
      "Schumann Kinderszenen No. 1 — fills the sub-beat-passing-harmony slot (per the prompt, a second Chopin piece was considered; Schumann gives more rhythmic variety)." },
};

// Number of opening measures analysed per score.  Caps end-to-end runtime on
// the larger scores (Mozart K.279-1 is ~650 kB / hundreds of measures); the
// sampled portion is enough to pin current behavior for Phase 1b purposes.
constexpr int kMaxAnalysisMeasures = 16;

// ── Helpers: name / format conversions ──────────────────────────────────────

const char* qualityName(ChordQuality q)
{
    switch (q) {
    case ChordQuality::Unknown:        return "unknown";
    case ChordQuality::Major:          return "major";
    case ChordQuality::Minor:          return "minor";
    case ChordQuality::Diminished:     return "diminished";
    case ChordQuality::Augmented:      return "augmented";
    case ChordQuality::HalfDiminished: return "halfDiminished";
    case ChordQuality::Suspended2:     return "sus2";
    case ChordQuality::Suspended4:     return "sus4";
    case ChordQuality::Power:          return "power";
    }
    return "unknown";
}

// Display flats for flat keys, sharps for sharp keys — matches the analyzer's
// default spelling convention for a stable, human-readable snapshot.  TPC is
// intentionally ignored here: the snapshot records the pitch-class identity,
// and TPC-driven enharmonic disambiguation is already covered by
// composing_tests.
std::string rootName(int pc, int keyFifths)
{
    static const char* SHARP[12] = { "C","C#","D","D#","E","F","F#","G","G#","A","A#","B" };
    static const char* FLAT [12] = { "C","Db","D","Eb","E","F","Gb","G","Ab","A","Bb","B" };
    const int p = ((pc % 12) + 12) % 12;
    return (keyFifths < 0) ? FLAT[p] : SHARP[p];
}

std::string keyName(int fifths, KeySigMode mode)
{
    return mu::composing::analysis::keyModeTonicName(fifths, mode);
}

std::string modeName(KeySigMode mode)
{
    const char* suffix = mu::composing::analysis::keyModeSuffix(mode);
    return (suffix && *suffix) ? suffix : "ionian";
}

// ── Sampling: one tick per measure downbeat, plus a mid-measure tick ─────────

struct SampleTick {
    int tickValue;
    int measureNumber;
    bool isMidMeasure;
};

std::vector<SampleTick> collectSampleTicks(MasterScore* score, int maxMeasures)
{
    std::vector<SampleTick> out;
    int measureNumber = 0;
    for (Measure* m = score->firstMeasure();
         m && measureNumber < maxMeasures;
         m = m->nextMeasure()) {
        ++measureNumber;
        const int startTick = m->tick().ticks();
        const int lenTicks = m->ticks().ticks();
        if (lenTicks <= 0) {
            continue;
        }
        out.push_back({ startTick, measureNumber, /*isMidMeasure*/ false });
        const int midTick = startTick + (lenTicks / 2);
        if (midTick > startTick) {
            out.push_back({ midTick, measureNumber, /*isMidMeasure*/ true });
        }
    }
    return out;
}

Fraction endTickForMeasureCap(MasterScore* score, int maxMeasures)
{
    int measureNumber = 0;
    Measure* lastIncluded = nullptr;
    for (Measure* m = score->firstMeasure();
         m && measureNumber < maxMeasures;
         m = m->nextMeasure()) {
        ++measureNumber;
        lastIncluded = m;
    }
    if (!lastIncluded) {
        return Fraction(0, 1);
    }
    return lastIncluded->endTick();
}

// ── Snapshot builders (one JSON array per path) ──────────────────────────────

QJsonObject regionToImplodeEntry(const HarmonicRegion& r)
{
    QJsonObject o;
    o[QStringLiteral("tick")] = r.startTick;
    o[QStringLiteral("durationTicks")] = r.endTick - r.startTick;
    const int keyFifths = r.keyModeResult.keySignatureFifths;
    o[QStringLiteral("root")]    = QString::fromStdString(rootName(r.chordResult.identity.rootPc, keyFifths));
    o[QStringLiteral("quality")] = QString::fromStdString(qualityName(r.chordResult.identity.quality));
    o[QStringLiteral("key")]     = QString::fromStdString(keyName(keyFifths, r.keyModeResult.mode));
    o[QStringLiteral("mode")]    = QString::fromStdString(modeName(r.keyModeResult.mode));
    return o;
}

// Find the region containing (or most recently preceding) a tick.
const HarmonicRegion* regionContaining(const std::vector<HarmonicRegion>& regions, int tick)
{
    const HarmonicRegion* best = nullptr;
    for (const auto& r : regions) {
        if (r.startTick <= tick && tick < r.endTick) {
            return &r;
        }
        if (r.startTick <= tick) {
            best = &r;
        }
    }
    return best;
}

QJsonArray buildImplodeArray(MasterScore* score, const Fraction& endTick)
{
    const auto regions = mu::notation::internal::prepareUserFacingHarmonicRegions(
        score, Fraction(0, 1), endTick, /*excludeStaves=*/{});
    QJsonArray arr;
    for (const auto& r : regions) {
        arr.append(regionToImplodeEntry(r));
    }
    return arr;
}

// Collect (segment, Harmony*) pairs currently present inside [0, endTick).
struct HarmonyAt {
    Segment* segment = nullptr;
    Harmony* harmony = nullptr;
};

std::vector<HarmonyAt> collectExistingHarmonies(MasterScore* score, const Fraction& endTick)
{
    std::vector<HarmonyAt> out;
    for (Segment* seg = score->firstSegment(SegmentType::ChordRest);
         seg;
         seg = seg->next1(SegmentType::ChordRest)) {
        if (seg->tick() >= endTick) {
            break;
        }
        for (mu::engraving::EngravingItem* ann : seg->annotations()) {
            if (ann && ann->isHarmony()) {
                out.push_back({ seg, toHarmony(ann) });
            }
        }
    }
    return out;
}

// Return the first ChordRest segment at or after cappedEnd, or nullptr for
// "to end of score".  Used as the endSegment argument to Selection::setRange.
Segment* segmentAtOrAfter(MasterScore* score, const Fraction& cappedEnd)
{
    for (Segment* seg = score->firstSegment(SegmentType::ChordRest);
         seg;
         seg = seg->next1(SegmentType::ChordRest)) {
        if (seg->tick() >= cappedEnd) {
            return seg;
        }
    }
    return nullptr;
}

QJsonArray buildAnnotationArray(MasterScore* score,
                                const Fraction& endTick,
                                const std::vector<HarmonicRegion>& regions)
{
    // Snapshot our pipeline's written annotations specifically — not the
    // DCML-sourced Roman numerals that some corpus scores ship with.  The
    // approach:
    //   1. Record which Harmony elements are in [0, endTick) before we write
    //      (the "pre-existing" set from the DCML score file).
    //   2. Run addHarmonicAnnotationsToSelection on a range selection.
    //   3. Record all Harmony elements in [0, endTick) after writing.
    //   4. Emit only the ones that were added by us (identity-by-pointer).
    Segment* startSeg = score->firstSegment(SegmentType::ChordRest);
    QJsonArray arr;
    if (!startSeg || score->nstaves() == 0) {
        return arr;
    }

    const auto before = collectExistingHarmonies(score, endTick);
    std::vector<Harmony*> preExisting;
    preExisting.reserve(before.size());
    for (const auto& entry : before) {
        preExisting.push_back(entry.harmony);
    }

    Segment* endSeg = segmentAtOrAfter(score, endTick);  // nullptr = to end of score
    score->selection().setRange(startSeg, endSeg,
                                /*staffStart*/ 0,
                                /*staffEnd (exclusive)*/ score->nstaves());
    if (!score->selection().isRange()) {
        return arr;
    }

    mu::notation::addHarmonicAnnotationsToSelection(score,
                                                     /*writeChordSymbols=*/true,
                                                     /*writeRomanNumerals=*/true,
                                                     /*writeNashvilleNumbers=*/false);

    const auto after = collectExistingHarmonies(score, endTick);
    for (const auto& entry : after) {
        if (std::find(preExisting.begin(), preExisting.end(), entry.harmony) != preExisting.end()) {
            continue;  // pre-existing from the DCML source, not something we wrote
        }
        const HarmonyType type = entry.harmony->harmonyType();
        if (type != HarmonyType::STANDARD && type != HarmonyType::ROMAN) {
            continue;
        }
        QJsonObject o;
        o[QStringLiteral("tick")] = entry.segment->tick().ticks();
        // harmonyName() reflects the semantic chord label the analyzer built
        // before layout; plainText() is empty for unlaid-out Harmony elements.
        QString text = entry.harmony->harmonyName().toQString();
        if (text.isEmpty()) {
            text = entry.harmony->plainText().toQString();
        }
        o[QStringLiteral("text")] = text;
        const HarmonicRegion* reg = regionContaining(regions, entry.segment->tick().ticks());
        if (reg) {
            o[QStringLiteral("key")] = QString::fromStdString(
                keyName(reg->keyModeResult.keySignatureFifths, reg->keyModeResult.mode));
        } else {
            o[QStringLiteral("key")] = QStringLiteral("");
        }
        arr.append(o);
    }

    return arr;
}

QJsonArray buildTickRegionalArray(MasterScore* score,
                                  const std::vector<SampleTick>& sampleTicks)
{
    QJsonArray arr;
    for (const SampleTick& s : sampleTicks) {
        const Fraction t = Fraction::fromTicks(s.tickValue);
        NoteHarmonicContext ctx = mu::notation::analyzeHarmonicContextAtTick(score, t);
        QJsonObject o;
        o[QStringLiteral("tick")] = s.tickValue;
        if (ctx.chordResults.empty()) {
            o[QStringLiteral("root")] = QStringLiteral("");
            o[QStringLiteral("quality")] = QStringLiteral("");
        } else {
            const auto& r = ctx.chordResults.front();
            o[QStringLiteral("root")] = QString::fromStdString(rootName(r.identity.rootPc, ctx.keyFifths));
            o[QStringLiteral("quality")] = QString::fromStdString(qualityName(r.identity.quality));
        }
        o[QStringLiteral("key")] = QString::fromStdString(keyName(ctx.keyFifths, ctx.keyMode));
        o[QStringLiteral("wasRegional")] = ctx.wasRegional;
        arr.append(o);
    }
    return arr;
}

QJsonArray buildTickLocalArray(MasterScore* score,
                               const std::vector<SampleTick>& sampleTicks)
{
    // Phase 2 added a public analyzeHarmonicContextLocallyAtTick so the
    // snapshot can pin P4 output directly.  The DCML corpus scores always
    // have staff 0 eligible for analysis (no chord-track staves, no drumset);
    // passing 0 as refStaff matches what resolveAnalysisReferenceStaff in
    // notationcomposingbridge.cpp would pick anyway.
    QJsonArray arr;
    for (const SampleTick& s : sampleTicks) {
        const Fraction t = Fraction::fromTicks(s.tickValue);
        Segment* seg = score->tick2segment(t, /*first=*/true, SegmentType::ChordRest);
        QJsonObject o;
        o[QStringLiteral("tick")] = s.tickValue;
        if (!seg) {
            o[QStringLiteral("root")] = QStringLiteral("");
            o[QStringLiteral("quality")] = QStringLiteral("");
            o[QStringLiteral("key")] = QStringLiteral("");
            arr.append(o);
            continue;
        }
        NoteHarmonicContext ctx = mu::notation::analyzeHarmonicContextLocallyAtTick(
            score, t, seg, /*refStaff=*/0, /*excludeStaves=*/{});
        if (ctx.chordResults.empty()) {
            o[QStringLiteral("root")] = QStringLiteral("");
            o[QStringLiteral("quality")] = QStringLiteral("");
        } else {
            const auto& r = ctx.chordResults.front();
            o[QStringLiteral("root")] = QString::fromStdString(rootName(r.identity.rootPc, ctx.keyFifths));
            o[QStringLiteral("quality")] = QString::fromStdString(qualityName(r.identity.quality));
        }
        o[QStringLiteral("key")] = QString::fromStdString(keyName(ctx.keyFifths, ctx.keyMode));
        arr.append(o);
    }
    return arr;
}

// ── Snapshot assembly ────────────────────────────────────────────────────────

constexpr int kSchemaVersion = 1;

QJsonObject buildSnapshot(const CorpusEntry& entry, MasterScore* score)
{
    const Fraction cappedEnd = endTickForMeasureCap(score, kMaxAnalysisMeasures);
    const auto samples = collectSampleTicks(score, kMaxAnalysisMeasures);

    const auto regions = mu::notation::internal::prepareUserFacingHarmonicRegions(
        score, Fraction(0, 1), cappedEnd, /*excludeStaves=*/{});

    QJsonObject snap;
    snap[QStringLiteral("score")] = QString::fromLatin1(entry.relativePath);
    snap[QStringLiteral("schemaVersion")] = kSchemaVersion;

    QJsonArray implodeArr;
    for (const auto& r : regions) {
        implodeArr.append(regionToImplodeEntry(r));
    }
    snap[QStringLiteral("implode")] = implodeArr;

    // Tick-sampled paths run before the annotation emitter writes Harmony
    // elements so annotation writes do not affect the regional context match
    // (analysis reads only notes, not symbols — but this ordering keeps the
    // snapshot deterministic even if future code drifts on that invariant).
    snap[QStringLiteral("tickRegional")] = buildTickRegionalArray(score, samples);
    snap[QStringLiteral("tickLocal")] = buildTickLocalArray(score, samples);

    // Annotation runs last because it mutates the score with Harmony elements.
    snap[QStringLiteral("annotation")] = buildAnnotationArray(score, cappedEnd, regions);

    return snap;
}

// ── Snapshot disk I/O ────────────────────────────────────────────────────────

QString snapshotsDir()
{
    return QStringLiteral(PIPELINE_SNAPSHOT_SNAPSHOTS_DIR);
}

QString snapshotPath(const CorpusEntry& entry)
{
    return snapshotsDir() + QLatin1Char('/') + QString::fromLatin1(entry.id) + QStringLiteral(".json");
}

QString corpusPath(const CorpusEntry& entry)
{
    return QStringLiteral(PIPELINE_SNAPSHOT_CORPUS_ROOT)
           + QLatin1Char('/') + QString::fromLatin1(entry.relativePath);
}

QString serializeSnapshot(const QJsonObject& snap)
{
    return QString::fromUtf8(QJsonDocument(snap).toJson(QJsonDocument::Indented));
}

bool writeSnapshotToDisk(const QString& path, const QString& contents, QString* errorOut)
{
    QDir().mkpath(snapshotsDir());
    QFile file(path);
    if (!file.open(QIODevice::WriteOnly | QIODevice::Truncate)) {
        if (errorOut) {
            *errorOut = file.errorString();
        }
        return false;
    }
    const QByteArray utf8 = contents.toUtf8();
    const qint64 written = file.write(utf8);
    file.close();
    if (written != utf8.size()) {
        if (errorOut) {
            *errorOut = QStringLiteral("short write: %1 of %2 bytes").arg(written).arg(utf8.size());
        }
        return false;
    }
    return true;
}

bool readSnapshotFromDisk(const QString& path, QString* outContents)
{
    QFile file(path);
    if (!file.open(QIODevice::ReadOnly)) {
        return false;
    }
    const QByteArray bytes = file.readAll();
    file.close();
    if (outContents) {
        *outContents = QString::fromUtf8(bytes);
    }
    return true;
}

// ── Minimal unified-style diff for error output ──────────────────────────────

std::string simpleLineDiff(const QString& expected, const QString& actual)
{
    const QStringList expLines = expected.split(QLatin1Char('\n'));
    const QStringList actLines = actual.split(QLatin1Char('\n'));
    std::ostringstream out;
    const int maxLines = std::max(expLines.size(), actLines.size());
    int divergenceLine = -1;
    for (int i = 0; i < maxLines; ++i) {
        const QString e = (i < expLines.size()) ? expLines.at(i) : QString();
        const QString a = (i < actLines.size()) ? actLines.at(i) : QString();
        if (e != a) {
            divergenceLine = i;
            break;
        }
    }
    if (divergenceLine < 0) {
        out << "(snapshots match — diff invoked in error)";
        return out.str();
    }
    const int contextBefore = 3;
    const int contextAfter = 8;
    const int startLine = std::max(0, divergenceLine - contextBefore);
    const int endLine = std::min(maxLines - 1, divergenceLine + contextAfter);
    out << "first divergence at line " << (divergenceLine + 1) << ":\n";
    out << "--- expected\n+++ actual\n";
    for (int i = startLine; i <= endLine; ++i) {
        const QString e = (i < expLines.size()) ? expLines.at(i) : QString();
        const QString a = (i < actLines.size()) ? actLines.at(i) : QString();
        if (e == a) {
            out << "  " << (i + 1) << ": " << e.toStdString() << "\n";
        } else {
            out << "- " << (i + 1) << ": " << e.toStdString() << "\n";
            out << "+ " << (i + 1) << ": " << a.toStdString() << "\n";
        }
    }
    return out.str();
}

// ── Flag detection: --update-goldens / PIPELINE_SNAPSHOT_UPDATE=1 ────────────

bool shouldUpdateGoldens()
{
    if (qEnvironmentVariableIsSet("PIPELINE_SNAPSHOT_UPDATE")) {
        return true;
    }
    if (QCoreApplication::instance()) {
        const QStringList args = QCoreApplication::arguments();
        return args.contains(QStringLiteral("--update-goldens"));
    }
    return false;
}

// ── gtest parametrization ───────────────────────────────────────────────────

class PipelineSnapshotTests : public ::testing::TestWithParam<CorpusEntry> {};

TEST_P(PipelineSnapshotTests, MatchesGoldenSnapshot)
{
    const CorpusEntry entry = GetParam();

    // Ensure regional accumulation is on — this is the default in production
    // but some test suites flip it off; set explicitly for determinism.
    auto analysisCfg = muse::modularity::globalIoc()->resolve<
        mu::composing::IComposingAnalysisConfiguration>("composing");
    if (analysisCfg) {
        analysisCfg->setUseRegionalAccumulation(true);
    }

    const QString scorePath = corpusPath(entry);
    ASSERT_TRUE(QFileInfo::exists(scorePath))
        << "Corpus score missing on disk: " << scorePath.toStdString()
        << "\n  (expected under PIPELINE_SNAPSHOT_CORPUS_ROOT = "
        << PIPELINE_SNAPSHOT_CORPUS_ROOT << ")";

    MasterScore* score = ScoreRW::readScore(muse::String::fromQString(scorePath),
                                             /*isAbsolutePath=*/true);
    ASSERT_TRUE(score) << "Failed to load corpus score: " << scorePath.toStdString();

    const QJsonObject snap = buildSnapshot(entry, score);
    const QString produced = serializeSnapshot(snap);

    const QString goldenPath = snapshotPath(entry);

    if (shouldUpdateGoldens()) {
        QString writeErr;
        ASSERT_TRUE(writeSnapshotToDisk(goldenPath, produced, &writeErr))
            << "Failed to write golden snapshot " << goldenPath.toStdString()
            << ": " << writeErr.toStdString();
        delete score;
        return;
    }

    QString expected;
    const bool haveGolden = readSnapshotFromDisk(goldenPath, &expected);
    if (!haveGolden) {
        delete score;
        FAIL() << "Golden snapshot missing: " << goldenPath.toStdString()
               << "\n  Run `./pipeline_snapshot_tests --update-goldens` to create it.";
    }

    if (expected != produced) {
        const std::string diff = simpleLineDiff(expected, produced);
        delete score;
        FAIL() << "Snapshot drift for " << entry.id
               << "\n  expected file: " << goldenPath.toStdString()
               << "\n\n" << diff
               << "\n  If the drift is intentional, update with `--update-goldens`.";
    }

    delete score;
}

// GoogleTest displays the second arg as each test's parametrized suffix.
// Using entry.id keeps error messages readable.
std::string corpusIdForTestName(const ::testing::TestParamInfo<CorpusEntry>& info)
{
    return std::string(info.param.id);
}

INSTANTIATE_TEST_SUITE_P(Corpus,
                         PipelineSnapshotTests,
                         ::testing::ValuesIn(kCorpus),
                         corpusIdForTestName);

} // namespace
