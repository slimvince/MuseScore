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
//   P1 Implode        — two complementary slices:
//                         "implode" — the region list out of
//                         prepareUserFacingHarmonicRegions (the input
//                         populateChordTrack consumes).
//                         "implodedChordTrack" — the actual chord-track
//                         output (notes + chord-symbol annotations) read
//                         back after running populateChordTrack on a fresh
//                         score copy.  Added in Phase 3a to pin the
//                         emitter side before the analyzeSection +
//                         emitImplodedChordTrack split.
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
#include <chrono>
#include <cmath>
#include <cstdlib>
#include <fstream>
#include <limits>
#include <numeric>
#include <optional>
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
#include <QSysInfo>

#include "global/types/translatablestring.h"

#include "engraving/dom/barline.h"      // OI-206 cost profile: endBarLineType / BarLineType (boundary evidence)
#include "engraving/dom/chord.h"
#include "engraving/dom/factory.h"
#include "engraving/dom/keysig.h"       // OI-206 cost profile: KeySig / toKeySig / concertKey (key-sig change)
#include "engraving/dom/harmony.h"
#include "engraving/dom/instrument.h"
#include "engraving/dom/masterscore.h"
#include "engraving/dom/measure.h"
#include "engraving/dom/note.h"
#include "engraving/dom/part.h"
#include "engraving/dom/segment.h"
#include "engraving/dom/select.h"
#include "engraving/dom/staff.h"
#include "engraving/dom/stafftext.h"   // P3a record-arm pedal-suppression check
#include "engraving/types/constants.h"

#include "engraving/tests/utils/scorerw.h"

#include "modularity/ioc.h"

#include "composing/analysis/chord/chordanalyzer.h"
#include "composing/analysis/key/keymodeanalyzer.h"
#include "composing/analysis/section/sectionanalyzer.h"
#include "composing/analysis/joint/jointnotationproducer.h"   // P1 §4.1 gap measurement (record arm)
#include "composing/analysis/joint/jointfactadapter.h"        // OI-206 cost profile: buildAdapterFacts (phase 1)
#include "composing/analysis/joint/jointdecoder.h"            // OI-206 cost profile: decodePiece (phase 3), ChordCache
#include "composing/analysis/joint/jointtables.h"             // OI-206 cost profile: JointTables::loadEmbedded (phase 2)
#include "composing/analysis/joint/jointweights.h"            // OI-206 cost profile: selectedWeights (phase 2)
#include "composing/analysis/joint/jointadapter.h"            // OI-206 cost profile: FittedAdapter::loadEmbedded (phase 2)
#include "composing/analysis/joint/jointnotationrecord.h"     // OI-206 cost profile: assembleNotationRecord/computePosteriorSlice (phase 4)
#include "composing/analyzed_section.h"
#include "composing/icomposinganalysisconfiguration.h"
#include "composing/icomposingchordstaffconfiguration.h"

#include "notation/internal/notationimplodebridge.h"
#include "notation/internal/notationtuningbridge.h"        // P6 dual-arm: applyRegionTuning (tuning surface)

#include "notation/internal/notationcomposingbridge.h"
#include "notation/internal/notationcomposingbridgehelpers.h"

#include "composing/intonation/tuning_system.h"             // P6 dual-arm: TuningMode (deterministic tuning config)

// OI-206 cost profile: per-process resident/peak memory (Windows). We do NOT #include <windows.h> — it
// pollutes the global namespace with macros (SymId/KeyMode/CONST collisions in engraving/types/
// propertyvalue.h, min/max, and more that would break the rest of this large TU). Instead we forward-
// declare the minimal kernel32 psapi API. K32GetProcessMemoryInfo/GetCurrentProcess live in kernel32
// (Win7+, x64), which MSVC links by default — no <windows.h>, no psapi.lib. The struct layout mirrors
// PROCESS_MEMORY_COUNTERS exactly (DWORD=unsigned long, SIZE_T=size_t on x64).
#ifdef _WIN32
extern "C" {
struct MU_PROCESS_MEMORY_COUNTERS {
    unsigned long cb;
    unsigned long PageFaultCount;
    size_t PeakWorkingSetSize;
    size_t WorkingSetSize;
    size_t QuotaPeakPagedPoolUsage;
    size_t QuotaPagedPoolUsage;
    size_t QuotaPeakNonPagedPoolUsage;
    size_t QuotaNonPagedPoolUsage;
    size_t PagefileUsage;
    size_t PeakPagefileUsage;
};
__declspec(dllimport) void* __stdcall GetCurrentProcess(void);
__declspec(dllimport) int __stdcall K32GetProcessMemoryInfo(void* Process,
                                                            MU_PROCESS_MEMORY_COUNTERS* counters,
                                                            unsigned long cb);
}
#endif

using mu::engraving::Chord;
using mu::engraving::ChordRest;
using mu::engraving::Constants;
using mu::engraving::Factory;
using mu::engraving::Fraction;
using mu::engraving::Harmony;
using mu::engraving::HarmonyType;
using mu::engraving::Instrument;
using mu::engraving::MasterScore;
using mu::engraving::Measure;
using mu::engraving::Note;
using mu::engraving::Part;
using mu::engraving::ScoreRW;
using mu::engraving::Segment;
using mu::engraving::SegmentType;
using mu::engraving::Staff;
using mu::engraving::staff_idx_t;
using mu::engraving::toChord;
using mu::engraving::toChordRest;
using mu::engraving::toHarmony;
using mu::engraving::track_idx_t;
using mu::engraving::VOICES;
using mu::notation::NoteHarmonicContext;
using mu::composing::analysis::ChordAnalysisResult;
using mu::composing::analysis::ChordQuality;
using mu::composing::analysis::AnalyzedRegion;
using mu::composing::analysis::AnalyzedSection;
using mu::composing::analysis::KeySigMode;
using mu::composing::analysis::joint::produceNotationRecord;
using mu::composing::analysis::joint::spanViewSegments;
using mu::composing::analysis::joint::RecordSegment;
using mu::composing::analysis::joint::SegmentSlice;

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

    { "bach_chorale_137",
      "tools/dcml/bach_chorales/MS3/137 Du, o schönes Weltgebäude.mscx",
      "Bach Chorale No. 137 (BWV 301) — contains MinorAdd6 inversions at mm. 2, 4, 14; verifies gates G-B/G-C/G-D fire in the bridge path." },
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

QJsonObject regionToImplodeEntry(const AnalyzedRegion& r)
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
const AnalyzedRegion* regionContaining(const std::vector<AnalyzedRegion>& regions, int tick)
{
    const AnalyzedRegion* best = nullptr;
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
    const auto rawRegions = mu::notation::analyzeHarmonicRhythm(
        score, Fraction(0, 1), endTick, /*excludeStaves=*/{},
        mu::notation::HarmonicRegionGranularity::Smoothed);
    const auto section = mu::composing::analysis::analyzeSection(
        score, Fraction(0, 1), endTick, /*excludeStaves=*/{}, rawRegions);
    QJsonArray arr;
    for (const auto& r : section.regions) {
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
                                const std::vector<AnalyzedRegion>& regions)
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
        const AnalyzedRegion* reg = regionContaining(regions, entry.segment->tick().ticks());
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

        // Phase 3c: capture the per-region temporal-extension snapshot fed
        // to the chosen result's analyzeChord call.  Pre-refactor this is
        // sourced from the canonical per-region pipeline (just plumbed
        // through HarmonicRegion → NoteHarmonicContext); post-refactor
        // (after divergence D closes) it is read identically from
        // AnalyzedRegion::temporalExtensions, so this should be byte-
        // identical across the refactor.
        const auto& ext = ctx.temporalExtensions;
        o[QStringLiteral("bassIsStepwiseFromPrevious")] = ext.bassIsStepwiseFromPrevious;
        o[QStringLiteral("bassIsStepwiseToNext")] = ext.bassIsStepwiseToNext;
        o[QStringLiteral("previousRootPc")] = ext.previousRootPc;
        o[QStringLiteral("previousBassPc")] = ext.previousBassPc;
        o[QStringLiteral("previousQuality")] = QString::fromStdString(qualityName(ext.previousQuality));

        // Phase 3c: capture chordResults[1..N] as alternatives.  Pre-refactor
        // this comes from P3's cruft display-context analyzeChord (with
        // possible region-winner prepend at [0]); post-refactor it comes
        // from AnalyzedRegion::alternatives (per-region-evolved context).
        // The alternatives content is expected to shift on a small subset
        // of ticks across the refactor — that is the documented unification.
        QJsonArray alts;
        if (ctx.chordResults.size() > 1) {
            for (size_t i = 1; i < ctx.chordResults.size(); ++i) {
                const auto& alt = ctx.chordResults[i];
                QJsonObject ao;
                ao[QStringLiteral("root")] = QString::fromStdString(rootName(alt.identity.rootPc, ctx.keyFifths));
                ao[QStringLiteral("quality")] = QString::fromStdString(qualityName(alt.identity.quality));
                ao[QStringLiteral("score")] = std::round(alt.identity.score * 1000.0) / 1000.0;
                alts.append(ao);
            }
        }
        o[QStringLiteral("alternatives")] = alts;

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

// Forward declaration so buildImplodedChordTrackArray can use corpusPath (the
// snapshot-disk-IO helpers below all live in the same anonymous namespace).
QString corpusPath(const CorpusEntry& entry);

// ── implodedChordTrack: read back what populateChordTrack emits ──────────────
//
// The chord-track output is the *user-visible* implode result: the notes and
// chord-symbol annotations written to a dedicated grand-staff pair appended
// to the score.  This snapshot pins that output byte-exact so the Phase 3a
// emitter split (analyzeSection + emitImplodedChordTrack) can prove byte
// identity against the pre-refactor baseline.
//
// The implode pass mutates the score (adds two staves, writes notes and
// Harmony elements).  Running it on the same MasterScore that produced the
// other snapshot fields would change those fields too — adding chord-track
// staves activates `addHarmonicAnnotationsToSelection`'s chord-track-priority
// rule, for example.  So we load a separate fresh copy here.

void configureChordStaffForSnapshot()
{
    auto chordStaffCfg = muse::modularity::globalIoc()->resolve<
        mu::composing::IComposingChordStaffConfiguration>("composing");
    if (!chordStaffCfg) {
        return;
    }
    // Deterministic settings — the same set used by the implode-test suite's
    // configureChordStaffPopulate(). Keeping these explicit makes the snapshot
    // independent of any user-preference defaults that might shift.
    chordStaffCfg->setChordStaffWriteChordSymbols(true);
    chordStaffCfg->setChordStaffFunctionNotation("none");
    chordStaffCfg->setChordStaffWriteKeyAnnotations(false);
    chordStaffCfg->setChordStaffHighlightNonDiatonic(false);
    chordStaffCfg->setChordStaffWriteCadenceMarkers(false);
}

// Append a "Chord Track Treble" + "Chord Track Bass" pair, mirroring
// notationimplode_tests.cpp::appendChordTrackStaffPair so populateChordTrack
// has somewhere to write.
staff_idx_t appendChordTrackStaffPair(MasterScore* score)
{
    score->startCmd(muse::TranslatableString::untranslatable("pipeline_snapshot_tests append chord-track staves"));

    auto appendStaff = [&](const muse::String& trackName) {
        Part* part = new Part(score);
        Instrument instrument;
        instrument.setTrackName(trackName);
        part->setInstrument(instrument);
        score->appendPart(part);

        Staff* staff = Factory::createStaff(part);
        score->undoInsertStaff(staff, 0, true);
    };

    const staff_idx_t trebleStaffIdx = score->nstaves();
    appendStaff(u"Chord Track Treble");
    appendStaff(u"Chord Track Bass");

    score->endCmd();
    return trebleStaffIdx;
}

// One entry per chord-track segment that has either a Chord or a Harmony.
// Pitches are sorted ascending for stable diffs across runs.
QJsonArray buildImplodedChordTrackArray(const QString& corpusAbsPath, int cappedEndTickValue)
{
    QJsonArray arr;
    if (corpusAbsPath.isEmpty() || cappedEndTickValue <= 0) {
        return arr;
    }

    configureChordStaffForSnapshot();

    MasterScore* score = ScoreRW::readScore(muse::String::fromQString(corpusAbsPath),
                                             /*isAbsolutePath=*/true);
    if (!score) {
        return arr;
    }
    if (score->nstaves() == 0) {
        delete score;
        return arr;
    }

    const staff_idx_t trebleStaffIdx = appendChordTrackStaffPair(score);
    const track_idx_t trebleTrack = trebleStaffIdx * VOICES;

    score->startCmd(muse::TranslatableString::untranslatable("pipeline_snapshot_tests populate chord track"));
    const bool ok = mu::notation::populateChordTrack(score,
                                                      Fraction(0, 1),
                                                      Fraction::fromTicks(cappedEndTickValue),
                                                      trebleStaffIdx);
    score->endCmd();
    if (!ok) {
        delete score;
        return arr;
    }

    const Fraction cappedEnd = Fraction::fromTicks(cappedEndTickValue);

    for (Segment* seg = score->firstSegment(SegmentType::ChordRest);
         seg;
         seg = seg->next1(SegmentType::ChordRest)) {
        if (seg->tick() >= cappedEnd) {
            break;
        }

        // Pitches: only when the treble-track element is an actual Chord
        // (rests on the chord track are silent positions and do not warrant
        // a snapshot row of their own).
        std::vector<int> pitches;
        int durationTicks = 0;
        ChordRest* cr = seg->cr(trebleTrack) ? toChordRest(seg->cr(trebleTrack)) : nullptr;
        if (cr) {
            durationTicks = cr->actualTicks().ticks();
            if (cr->isChord()) {
                Chord* chord = toChord(cr);
                for (Note* n : chord->notes()) {
                    if (n) {
                        pitches.push_back(n->pitch());
                    }
                }
                std::sort(pitches.begin(), pitches.end());
            }
        }

        // Harmony text: pick the first Harmony annotation on the treble track
        // (implode writes one per region; multiple is a current-code bug, not
        // something the snapshot needs to disambiguate).
        QString harmonyText;
        for (mu::engraving::EngravingItem* ann : seg->annotations()) {
            if (!ann || !ann->isHarmony() || ann->track() != trebleTrack) {
                continue;
            }
            Harmony* h = toHarmony(ann);
            harmonyText = h->harmonyName().toQString();
            if (harmonyText.isEmpty()) {
                harmonyText = h->plainText().toQString();
            }
            break;
        }

        if (pitches.empty() && harmonyText.isEmpty()) {
            continue;
        }

        QJsonObject o;
        o[QStringLiteral("tick")] = seg->tick().ticks();
        o[QStringLiteral("durationTicks")] = durationTicks;
        QJsonArray pitchArr;
        for (int p : pitches) {
            pitchArr.append(p);
        }
        o[QStringLiteral("pitches")] = pitchArr;
        o[QStringLiteral("harmonyText")] = harmonyText;
        arr.append(o);
    }

    delete score;
    return arr;
}

// ── Snapshot assembly ────────────────────────────────────────────────────────

constexpr int kSchemaVersion = 3;  // Phase 5a: keyAreas array added

QJsonArray buildKeyAreasArray(const AnalyzedSection& section)
{
    using mu::composing::analysis::KeyArea;
    QJsonArray arr;
    for (const KeyArea& ka : section.keyAreas) {
        QJsonObject o;
        o[QStringLiteral("startTick")]  = ka.startTick;
        o[QStringLiteral("endTick")]    = ka.endTick;
        o[QStringLiteral("keyFifths")]  = ka.keyFifths;
        o[QStringLiteral("mode")]       = QString::fromStdString(modeName(ka.mode));
        o[QStringLiteral("confidence")] = std::round(ka.confidence * 1000.0) / 1000.0;
        arr.append(o);
    }
    return arr;
}

QJsonObject buildSnapshot(const CorpusEntry& entry, MasterScore* score)
{
    const Fraction cappedEnd = endTickForMeasureCap(score, kMaxAnalysisMeasures);
    const auto samples = collectSampleTicks(score, kMaxAnalysisMeasures);

    const auto rawRegions = mu::notation::analyzeHarmonicRhythm(
        score, Fraction(0, 1), cappedEnd, /*excludeStaves=*/{},
        mu::notation::HarmonicRegionGranularity::Smoothed);
    const auto section = mu::composing::analysis::analyzeSection(
        score, Fraction(0, 1), cappedEnd, /*excludeStaves=*/{}, rawRegions);

    QJsonObject snap;
    snap[QStringLiteral("score")] = QString::fromLatin1(entry.relativePath);
    snap[QStringLiteral("schemaVersion")] = kSchemaVersion;

    QJsonArray implodeArr;
    for (const auto& r : section.regions) {
        implodeArr.append(regionToImplodeEntry(r));
    }
    snap[QStringLiteral("implode")] = implodeArr;
    snap[QStringLiteral("keyAreas")] = buildKeyAreasArray(section);

    // Tick-sampled paths run before the annotation emitter writes Harmony
    // elements so annotation writes do not affect the regional context match
    // (analysis reads only notes, not symbols — but this ordering keeps the
    // snapshot deterministic even if future code drifts on that invariant).
    snap[QStringLiteral("tickRegional")] = buildTickRegionalArray(score, samples);
    snap[QStringLiteral("tickLocal")] = buildTickLocalArray(score, samples);

    // Annotation runs last because it mutates the score with Harmony elements.
    snap[QStringLiteral("annotation")] = buildAnnotationArray(score, cappedEnd, section.regions);

    // implodedChordTrack reads back what populateChordTrack writes to a
    // freshly-loaded copy of the score (chord-track staves alter the original
    // score's chord-track-priority behaviour for annotation, so isolation
    // matters — see the function's comment block).
    snap[QStringLiteral("implodedChordTrack")] = buildImplodedChordTrackArray(
        corpusPath(entry), cappedEnd.ticks());

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
           + QLatin1Char('/') + QString::fromUtf8(entry.relativePath);
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
        // The joint record IS the production notation path since the user-ratified switch
        // (2026-07-27) — the goldens below pin the record arm. Set the flag explicitly, for the
        // same determinism reason as the line above: the record-arm tests in this binary restore
        // the flag OFF when they finish, so the ambient value is not reliable across the suite.
        analysisCfg->setUseJointNotationRecord(true);
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

// ── P1 (seams-2): the §4.1 gap-scale measurement artifact ────────────────────
//
// Emits tools/notation_seams/gap_measurement.json — the input to the §4.1
// presentation-constant selection (choose_exposure_constants.py). For each
// snapshot-corpus score over the SAME 16-measure window the goldens pin, it
// records, per LEGACY region, the key-mode normalizedConfidence the exposure
// gates read today; and, per RECORD committed segment, the §3.3 key-axis
// content-score GAP (nats) that replaces it on the record path — the RAW gap,
// no [0,1] remapping (Cowork's binding P2 sharpening). The Python analysis then
// picks each gap-scale constant to preserve the legacy exposure RATE.
//
// MEASUREMENT-ONLY and OPT-IN (DISABLED_ — the DISABLED_P3PerfBaseline
// precedent): it never runs in the default sweep, so the golden comparison and
// byte-identity are untouched. It calls only public entry points the production
// notation path already uses (analyzeHarmonicRhythm + analyzeSection = legacy;
// produceNotationRecord = record). No production code is instrumented. Run with:
//
//   ./pipeline_snapshot_tests.exe \
//       --gtest_also_run_disabled_tests \
//       --gtest_filter='*SeamsGapMeasurement*'

// The §3.3 key-axis content-score gap (nats): the committed key's within-segment
// content score minus the best-scoring alternative key. SIGNED — negative when
// the decoded (committed) key is not the local content-argmax (a transition/prior
// chose it), which is exactly the low-local-confidence regime. Absent (null) when
// the axis carries no committed index or fewer than two candidates.
std::optional<double> keyAxisContentGap(const SegmentSlice& slice)
{
    const auto& ax = slice.keyAxis;
    const int n = static_cast<int>(ax.scores.size());
    if (ax.committed < 0 || ax.committed >= n || n < 2) {
        return std::nullopt;
    }
    double bestOther = -std::numeric_limits<double>::infinity();
    for (int i = 0; i < n; ++i) {
        if (i != ax.committed) {
            bestOther = std::max(bestOther, ax.scores[static_cast<size_t>(i)]);
        }
    }
    return ax.scores[static_cast<size_t>(ax.committed)] - bestOther;
}

TEST(SeamsGapMeasurement, DISABLED_EmitArtifact)
{
    auto analysisCfg = muse::modularity::globalIoc()->resolve<
        mu::composing::IComposingAnalysisConfiguration>("composing");
    if (analysisCfg) {
        analysisCfg->setUseRegionalAccumulation(true);   // production default (matches the golden path)
        analysisCfg->setUseJointNotationRecord(false);   // legacy arm; the record arm is a direct producer call
    }

    QJsonArray corpusArr;
    for (const CorpusEntry& entry : kCorpus) {
        const QString scorePath = corpusPath(entry);
        ASSERT_TRUE(QFileInfo::exists(scorePath)) << "missing: " << scorePath.toStdString();
        MasterScore* score = ScoreRW::readScore(muse::String::fromQString(scorePath),
                                                 /*isAbsolutePath=*/true);
        ASSERT_TRUE(score) << "load failed: " << scorePath.toStdString();

        const Fraction endTick = endTickForMeasureCap(score, kMaxAnalysisMeasures);

        // legacy arm — the normalizedConfidence the exposure gates read today, per region.
        const auto rawRegions = mu::notation::analyzeHarmonicRhythm(
            score, Fraction(0, 1), endTick, /*excludeStaves=*/{},
            mu::notation::HarmonicRegionGranularity::Smoothed);
        const auto section = mu::composing::analysis::analyzeSection(
            score, Fraction(0, 1), endTick, /*excludeStaves=*/{}, rawRegions);
        QJsonArray legacyArr;
        for (const AnalyzedRegion& r : section.regions) {
            QJsonObject o;
            o[QStringLiteral("startTick")] = r.startTick;
            o[QStringLiteral("endTick")] = r.endTick;
            o[QStringLiteral("normalizedConfidence")] = r.keyModeResult.normalizedConfidence;
            legacyArr.append(o);
        }

        // record arm — the §3.3 key-axis content-score gap per committed segment, over the same window.
        QJsonArray recordArr;
        QString recordError;
        const auto res = produceNotationRecord(score, std::string(entry.id));
        if (res.ok) {
            const std::vector<int> idx = spanViewSegments(res.record, 0, endTick.ticks());
            for (int i : idx) {
                const RecordSegment& s = res.record.segments[static_cast<size_t>(i)];
                QJsonObject o;
                o[QStringLiteral("startTick")] = s.startTick;
                o[QStringLiteral("endTick")] = s.endTick;
                std::optional<double> gap;
                if (i < static_cast<int>(res.record.slices.size())) {
                    gap = keyAxisContentGap(res.record.slices[static_cast<size_t>(i)]);
                }
                if (gap.has_value()) {
                    o[QStringLiteral("keyAxisGap")] = *gap;
                } else {
                    o[QStringLiteral("keyAxisGap")] = QJsonValue(QJsonValue::Null);
                }
                recordArr.append(o);
            }
        } else {
            recordError = QString::fromStdString(res.error);
        }

        QJsonObject scoreObj;
        scoreObj[QStringLiteral("id")] = QString::fromUtf8(entry.id);
        scoreObj[QStringLiteral("analysisEndTick")] = endTick.ticks();
        scoreObj[QStringLiteral("legacyRegions")] = legacyArr;
        scoreObj[QStringLiteral("recordSegments")] = recordArr;
        if (!recordError.isEmpty()) {
            scoreObj[QStringLiteral("recordError")] = recordError;
        }
        corpusArr.append(scoreObj);
    }

    QJsonObject root;
    root[QStringLiteral("window")] =
        QStringLiteral("[0, endTickForMeasureCap(kMaxAnalysisMeasures=16)) — the snapshot harness window");
    root[QStringLiteral("legacyConfidenceField")] =
        QStringLiteral("KeyModeAnalysisResult.normalizedConfidence per AnalyzedRegion (the exposure-gate input today)");
    root[QStringLiteral("recordGapField")] =
        QStringLiteral("keyAxis.scores[committed] - max(other keyAxis.scores), nats; null if <2 candidates / no committed. RAW, no [0,1] remap.");
    root[QStringLiteral("corpus")] = corpusArr;

    const QString outPath = QStringLiteral(PIPELINE_SNAPSHOT_CORPUS_ROOT)
                            + QStringLiteral("/tools/notation_seams/gap_measurement.json");
    QDir().mkpath(QFileInfo(outPath).absolutePath());
    const QByteArray bytes = serializeSnapshot(root).toUtf8();
    QFile out(outPath);
    ASSERT_TRUE(out.open(QIODevice::WriteOnly | QIODevice::Truncate)) << out.errorString().toStdString();
    ASSERT_EQ(out.write(bytes), static_cast<qint64>(bytes.size()));
    out.close();
    std::cout << "[seams gap measurement] wrote " << outPath.toStdString() << std::endl;
}

// ── Seams part 2, P3a — the annotation-emitter RECORD path ───────────────────
//
// With useJointNotationRecord ON, addHarmonicAnnotationsToSelection derives the AnalyzedSection from
// the joint estimator's notation record (analyzeSectionFromRecord) and writes the record's DERIVED
// chord-symbol / Roman strings (§5.6 formatter continuity, #6; A2 — the record IS the surface), not
// the legacy ChordSymbolFormatter output. This test proves the record path is taken and that the
// written Roman numerals equal the record segment at each write tick; that Nashville is a declared
// record-path GAP (requesting it writes nothing — the record/jointRender publish no Nashville form,
// §5.6 has no batch-render Nashville to reproduce; a FINDING to Cowork); and that the pedal "X ped."
// StaffText is SUSPENDED (the record path sets isPedalPoint = false, OI-194). Flag-OFF byte-identity
// is the existing golden suite (this test runs a SEPARATE arm and restores the flag before returning).
//
// Chord symbols: the record arm now writes the DISPLAY form (ChordSymbolFormatter::formatSymbol from
// the record's committed reading — the ratified D2 / §3.3-amendment presentation derivation), NOT the
// record's grading-form chordSymbol ("GDom7"). STANDARD Harmony re-parses on read-back, so the exact
// display string is not round-trip-asserted here (the exact form is established by the unit tests in
// section_record_adapter_tests.cpp); instead this asserts symbols ARE written and carry NO grading-
// only token ("Dom"/"HalfDim" — no chord-render style produces them), proving the DISPLAY form (not
// the grading form) reaches the score. Roman numerals (ROMAN Harmony) store their text literally, so
// they round-trip and are matched exactly.
TEST(SectionRecordAdapterAnnotation, RecordArmEmitsRecordDerivedStrings)
{
    auto cfg = muse::modularity::globalIoc()->resolve<
        mu::composing::IComposingAnalysisConfiguration>("composing");
    ASSERT_TRUE(cfg) << "IComposingAnalysisConfiguration not registered";
    cfg->setUseRegionalAccumulation(true);          // production default
    cfg->setUseJointNotationRecord(true);           // ← the record arm under test

    int checkedScores = 0;
    int checkedRomans = 0;
    int checkedSymbols = 0;

    // Two representative chorales — enough to exercise the record path (each score pays two
    // whole-score decodes: the test's own produceNotationRecord + the emitter's internal one), so
    // the subset is kept small to bound the default-sweep runtime.
    for (int ci = 0; ci < 2; ++ci) {
        const CorpusEntry& entry = kCorpus[ci];
        const QString scorePath = corpusPath(entry);
        ASSERT_TRUE(QFileInfo::exists(scorePath)) << "missing: " << scorePath.toStdString();
        MasterScore* score = ScoreRW::readScore(muse::String::fromQString(scorePath),
                                                 /*isAbsolutePath=*/true);
        ASSERT_TRUE(score) << "load failed: " << entry.id;

        const Fraction endTick = endTickForMeasureCap(score, kMaxAnalysisMeasures);
        const auto rec = mu::composing::analysis::joint::produceNotationRecord(score, std::string(entry.id));
        if (!rec.ok) {
            delete score;
            continue;
        }

        Segment* startSeg = score->firstSegment(SegmentType::ChordRest);
        if (!startSeg || score->nstaves() == 0) {
            delete score;
            continue;
        }
        const auto before = collectExistingHarmonies(score, endTick);
        std::vector<mu::engraving::Harmony*> pre;
        pre.reserve(before.size());
        for (const auto& e : before) {
            pre.push_back(e.harmony);
        }
        Segment* endSeg = segmentAtOrAfter(score, endTick);
        score->selection().setRange(startSeg, endSeg, /*staffStart=*/0, /*staffEnd=*/score->nstaves());
        ASSERT_TRUE(score->selection().isRange()) << entry.id;

        // Symbols + Roman: exercises the record's DISPLAY chord symbol (STANDARD Harmony, presentation
        // derivation) AND the record's romanNumeral (ROMAN Harmony, literal round-trip) + the key-area
        // brackets + cadence/pivot, and lets the pedal path (Roman-mode-gated) be observed.
        mu::notation::addHarmonicAnnotationsToSelection(score, /*sym=*/true, /*roman=*/true, /*nashville=*/false);

        const auto after = collectExistingHarmonies(score, endTick);
        for (const auto& e : after) {
            if (std::find(pre.begin(), pre.end(), e.harmony) != pre.end()) {
                continue;                                    // pre-existing DCML annotation
            }
            const std::string text = e.harmony->harmonyName().toQString().toStdString();
            if (e.harmony->harmonyType() == HarmonyType::ROMAN) {
                if (!text.empty() && text.front() == '[') {
                    continue;                                // "[G:]" key-area bracket marker, not a chord Roman
                }
                const int tick = e.segment->tick().ticks();
                const auto* rs = mu::composing::analysis::joint::noteView(rec.record, tick).segment;
                ASSERT_NE(rs, nullptr) << entry.id << " @ " << tick << " (a written Roman with no record segment)";
                EXPECT_EQ(text, rs->romanNumeral) << entry.id << " @ " << tick << " (record-derived Roman)";
                ++checkedRomans;
            } else if (e.harmony->harmonyType() == HarmonyType::STANDARD) {
                // The DISPLAY form, not the grading form: no grading-only quality token leaks through.
                for (const char* tok : { "Dom", "HalfDim", "AugSixth", "Neapolitan" }) {
                    EXPECT_EQ(text.find(tok), std::string::npos)
                        << entry.id << " @ " << e.segment->tick().ticks()
                        << ": a grading-form token in a display chord symbol (\"" << text << "\")";
                }
                ++checkedSymbols;
            }
        }

        // Pedal SUSPENDED on the record path: no "X ped." StaffText anywhere in the window.
        for (Segment* seg = score->firstSegment(SegmentType::ChordRest);
             seg && seg->tick() < endTick;
             seg = seg->next1(SegmentType::ChordRest)) {
            for (mu::engraving::EngravingItem* ann : seg->annotations()) {
                if (ann && ann->isStaffText()) {
                    const std::string t = mu::engraving::toStaffText(ann)->plainText().toStdString();
                    EXPECT_EQ(t.find(" ped."), std::string::npos)
                        << entry.id << ": a pedal annotation was written on the record path";
                }
            }
        }

        ++checkedScores;
        delete score;
    }

    // Nashville: the P3a record-path gap is CLOSED (P-strings Task 2) — requesting Nashville now WRITES
    // it (the shared formatNashvilleNumber, a presentation derivation from the record's committed
    // reading). The exact per-region string continuity vs the legacy formatter is established by the
    // unit test (section_record_adapter_tests.cpp NashvilleContinuityWithLegacyFormatter); here we
    // assert the arm emits Nashville end-to-end.
    {
        MasterScore* score = ScoreRW::readScore(muse::String::fromQString(corpusPath(kCorpus[0])),
                                                /*isAbsolutePath=*/true);
        ASSERT_TRUE(score);
        const Fraction endTick = endTickForMeasureCap(score, kMaxAnalysisMeasures);
        const auto before = collectExistingHarmonies(score, endTick);
        std::vector<mu::engraving::Harmony*> pre;
        pre.reserve(before.size());
        for (const auto& e : before) {
            pre.push_back(e.harmony);
        }
        Segment* startSeg = score->firstSegment(SegmentType::ChordRest);
        Segment* endSeg = segmentAtOrAfter(score, endTick);
        ASSERT_TRUE(startSeg && score->nstaves() > 0);
        score->selection().setRange(startSeg, endSeg, 0, score->nstaves());
        ASSERT_TRUE(score->selection().isRange());
        mu::notation::addHarmonicAnnotationsToSelection(score, /*sym=*/false, /*roman=*/false, /*nashville=*/true);
        int newNashville = 0;
        for (const auto& e : collectExistingHarmonies(score, endTick)) {
            if (std::find(pre.begin(), pre.end(), e.harmony) != pre.end()) {
                continue;
            }
            if (e.harmony->harmonyType() == HarmonyType::NASHVILLE) {
                ++newNashville;
            }
        }
        EXPECT_GT(newNashville, 0) << "record path must write Nashville (the P3a gap is closed)";
        delete score;
    }

    cfg->setUseJointNotationRecord(false);           // restore before the rest of the suite runs

    EXPECT_GT(checkedScores, 0) << "no corpus score produced a record";
    EXPECT_GT(checkedRomans, 0) << "the record-arm emitter wrote no record-derived Romans";
    EXPECT_GT(checkedSymbols, 0) << "the record-arm emitter wrote no display chord symbols";
}

// ── Seams part 2, P4 — the IMPLODE chord-track RECORD path ───────────────────
//
// With useJointNotationRecord ON, populateChordTrack derives the AnalyzedSection from the joint
// notation record (analyzeSectionFromRecord) and runs the SAME implode emitter with the record-arm
// specifics: the DISPLAY chord symbol on the treble track via the shared presentation formatter
// (STANDARD Harmony — no grading-form token leaks), and the Roman numeral on the bass track as the
// record's PUBLISHED romanNumeral (ROMAN Harmony, literal round-trip; equal to noteView(record,
// tick).romanNumeral — a fact, not re-formatted from ChordIdentity). Structural + golden-less (the
// P3a precedent); flag-OFF byte-identity is the existing implode goldens. Restores the flag + the
// chord-staff config before returning.
TEST(ImplodeRecordArm, RecordArmEmitsRecordDerivedChordTrack)
{
    auto cfg = muse::modularity::globalIoc()->resolve<
        mu::composing::IComposingAnalysisConfiguration>("composing");
    ASSERT_TRUE(cfg) << "IComposingAnalysisConfiguration not registered";
    auto chordStaffCfg = muse::modularity::globalIoc()->resolve<
        mu::composing::IComposingChordStaffConfiguration>("composing");
    ASSERT_TRUE(chordStaffCfg) << "IComposingChordStaffConfiguration not registered";

    cfg->setUseRegionalAccumulation(true);
    cfg->setUseJointNotationRecord(true);                 // ← the record arm under test
    chordStaffCfg->setChordStaffWriteChordSymbols(true);
    chordStaffCfg->setChordStaffFunctionNotation("roman");
    chordStaffCfg->setChordStaffWriteKeyAnnotations(false);
    chordStaffCfg->setChordStaffHighlightNonDiatonic(false);
    chordStaffCfg->setChordStaffWriteCadenceMarkers(false);

    int checkedScores = 0;
    int checkedRomans = 0;
    int checkedSymbols = 0;

    // Two representative chorales (each pays two whole-score decodes — the test's own + the emitter's
    // internal one), so the subset is kept small to bound the default-sweep runtime.
    for (int ci = 0; ci < 2; ++ci) {
        const CorpusEntry& entry = kCorpus[ci];
        const QString scorePath = corpusPath(entry);
        ASSERT_TRUE(QFileInfo::exists(scorePath)) << "missing: " << scorePath.toStdString();
        MasterScore* score = ScoreRW::readScore(muse::String::fromQString(scorePath),
                                                 /*isAbsolutePath=*/true);
        ASSERT_TRUE(score) << "load failed: " << entry.id;

        const Fraction endTick = endTickForMeasureCap(score, kMaxAnalysisMeasures);
        const auto rec = produceNotationRecord(score, std::string(entry.id));
        if (!rec.ok || score->nstaves() == 0) {
            delete score;
            continue;
        }

        const staff_idx_t trebleStaffIdx = appendChordTrackStaffPair(score);
        const track_idx_t trebleTrack = trebleStaffIdx * VOICES;
        const track_idx_t bassTrack   = (trebleStaffIdx + 1) * VOICES;

        score->startCmd(muse::TranslatableString::untranslatable("pipeline_snapshot_tests implode record arm"));
        const bool ok = mu::notation::populateChordTrack(score, Fraction(0, 1), endTick, trebleStaffIdx);
        score->endCmd();
        ASSERT_TRUE(ok) << entry.id << " (record-arm populateChordTrack wrote nothing)";

        for (Segment* seg = score->firstSegment(SegmentType::ChordRest);
             seg && seg->tick() < endTick;
             seg = seg->next1(SegmentType::ChordRest)) {
            const int tick = seg->tick().ticks();
            for (mu::engraving::EngravingItem* ann : seg->annotations()) {
                if (!ann || !ann->isHarmony()) {
                    continue;
                }
                const track_idx_t t = ann->track();
                if (t != trebleTrack && t != bassTrack) {
                    continue;                                // only the appended chord-track staves
                }
                const std::string text = toHarmony(ann)->harmonyName().toQString().toStdString();
                if (ann->isHarmony() && toHarmony(ann)->harmonyType() == HarmonyType::ROMAN) {
                    // the Roman is the record's PUBLISHED numeral at this tick
                    const RecordSegment* rs = mu::composing::analysis::joint::noteView(rec.record, tick).segment;
                    ASSERT_NE(rs, nullptr) << entry.id << " @ " << tick << " (a written Roman with no record segment)";
                    EXPECT_EQ(text, rs->romanNumeral) << entry.id << " @ " << tick << " (record-derived Roman)";
                    ++checkedRomans;
                } else if (toHarmony(ann)->harmonyType() == HarmonyType::STANDARD) {
                    // the DISPLAY form: no grading-only quality token leaks through
                    for (const char* tok : { "Dom", "HalfDim", "AugSixth", "Neapolitan" }) {
                        EXPECT_EQ(text.find(tok), std::string::npos)
                            << entry.id << " @ " << tick << ": a grading-form token in a display chord symbol (\"" << text << "\")";
                    }
                    ++checkedSymbols;
                }
            }
        }

        ++checkedScores;
        delete score;
    }

    cfg->setUseJointNotationRecord(false);               // restore before the rest of the suite runs
    configureChordStaffForSnapshot();                    // restore the deterministic snapshot config

    EXPECT_GT(checkedScores, 0) << "no corpus score produced a record";
    EXPECT_GT(checkedRomans, 0) << "the record-arm implode wrote no record-derived Romans";
    EXPECT_GT(checkedSymbols, 0) << "the record-arm implode wrote no display chord symbols";
}

// ── P3 status-bar performance baseline (Stage 2.5) ───────────────────────────
//
// Roadmap item 2.5 — capture the cost of the P3 status-bar query path
// (analyzeHarmonicContextAtTick) NOW, before Stage 3's decoder adds decode
// cost.  Purpose: an honest pre-decoder baseline + the budget envelope for the
// decoder's quality-level-0 (beam-1 must stay status-bar viable).
//
// This is a DISABLED gtest: timing is noisy and slow, so it must NOT run in the
// default CI sweep.  Re-run it (here at Stage 2.5, and again at Stage 3) with:
//
//   ./pipeline_snapshot_tests.exe \
//       --gtest_also_run_disabled_tests \
//       --gtest_filter='*P3Perf*'
//
// It loads each perf-corpus score (full, uncapped — unlike the snapshot corpus,
// which caps at kMaxAnalysisMeasures), enumerates EVERY chord-bearing
// ChordRest tick, and wall-times one analyzeHarmonicContextAtTick query per
// tick across several runs.  Output is a human-readable table on stdout plus a
// machine-readable block the docs/perf_p3_baseline.md table is lifted from.
//
// Measurement-only: it calls the same public entry points the production
// status bar and the snapshot harness use (analyzeHarmonicContextAtTick, and —
// for the coarse Pass-0-vs-analyzeSection attribution — analyzeHarmonicRhythm +
// analyzeSection).  No production code is instrumented or modified.

struct PerfScore {
    const char* id;
    const char* relativePath;   // under PIPELINE_SNAPSHOT_CORPUS_ROOT (= repo root)
    const char* sizeClass;
};

// Three size classes drawn from the snapshot corpus + one contrapuntal keyboard
// piece, smallest → largest by file size (chorale 58 kB, mazurka 202 kB, prelude
// 287 kB, sonata 638 kB).
constexpr PerfScore kPerfCorpus[] = {
    { "bach_chorale_001",
      "tools/dcml/bach_chorales/MS3/001 Aus meines Herzens Grunde.mscx",
      "small SATB chorale" },
    { "chopin_bi105_op30_1",
      "tools/dcml/chopin_mazurkas/MS3/BI105-1op30-1.mscx",
      "mid-size piano (mazurka)" },
    { "bach_bwv806_prelude",
      "tools/dcml/bach_en_fr_suites/MS3/BWV806_01_Prelude.mscx",
      "contrapuntal keyboard prelude" },
    { "mozart_k279_1",
      "tools/dcml/mozart_piano_sonatas/MS3/K279-1.mscx",
      "largest convenient (sonata mvt)" },
};

constexpr int kPerfRuns = 5;            // full sweeps per score; report median-of-runs
constexpr double kEgregiousMs = 100.0;  // attribution threshold

QString perfCorpusPath(const PerfScore& s)
{
    return QStringLiteral(PIPELINE_SNAPSHOT_CORPUS_ROOT)
           + QLatin1Char('/') + QString::fromUtf8(s.relativePath);
}

// Every distinct ChordRest tick that has at least one sounding note in any
// voice — these are the ticks a user can click to trigger a status-bar query.
std::vector<int> collectChordBearingTicks(MasterScore* score)
{
    std::vector<int> ticks;
    int lastTick = -1;
    for (Segment* seg = score->firstSegment(SegmentType::ChordRest);
         seg;
         seg = seg->next1(SegmentType::ChordRest)) {
        bool hasChord = false;
        for (track_idx_t tr = 0; tr < score->ntracks(); ++tr) {
            mu::engraving::EngravingItem* e = seg->element(tr);
            if (e && e->isChord()) {
                hasChord = true;
                break;
            }
        }
        if (!hasChord) {
            continue;
        }
        const int t = seg->tick().ticks();
        if (t != lastTick) {     // dedupe identical ticks across staves/voices
            ticks.push_back(t);
            lastTick = t;
        }
    }
    return ticks;
}

double percentileNearestRank(std::vector<double> v, double pct)
{
    if (v.empty()) {
        return 0.0;
    }
    std::sort(v.begin(), v.end());
    // Nearest-rank: ceil(pct/100 * N), 1-based → clamp into [1, N].
    int rank = static_cast<int>(std::ceil(pct / 100.0 * static_cast<double>(v.size())));
    rank = std::max(1, std::min<int>(rank, static_cast<int>(v.size())));
    return v[static_cast<size_t>(rank - 1)];
}

double medianSorted(std::vector<double> v)
{
    if (v.empty()) {
        return 0.0;
    }
    std::sort(v.begin(), v.end());
    const size_t n = v.size();
    return (n % 2 == 1) ? v[n / 2] : 0.5 * (v[n / 2 - 1] + v[n / 2]);
}

struct PerfRunStats {
    double medianMs = 0.0;
    double p95Ms = 0.0;
    double maxMs = 0.0;
    double totalMs = 0.0;
};

TEST(P3PerfBaseline, DISABLED_Sweep)
{
    auto analysisCfg = muse::modularity::globalIoc()->resolve<
        mu::composing::IComposingAnalysisConfiguration>("composing");
    if (analysisCfg) {
        analysisCfg->setUseRegionalAccumulation(true);
    }

    std::ostringstream report;
    report << "\n==== P3PERF BEGIN ====\n";
    report << "runs_per_score=" << kPerfRuns << "\n";

    for (const PerfScore& ps : kPerfCorpus) {
        const QString scorePath = perfCorpusPath(ps);
        ASSERT_TRUE(QFileInfo::exists(scorePath))
            << "Perf corpus score missing: " << scorePath.toStdString();

        MasterScore* score = ScoreRW::readScore(muse::String::fromQString(scorePath),
                                                 /*isAbsolutePath=*/true);
        ASSERT_TRUE(score) << "Failed to load perf score: " << scorePath.toStdString();

        // Count measures for the scaling table.
        int measureCount = 0;
        for (Measure* m = score->firstMeasure(); m; m = m->nextMeasure()) {
            ++measureCount;
        }

        const std::vector<int> ticks = collectChordBearingTicks(score);

        // P4-fallback frequency is deterministic across runs (no timing
        // dependence) — measure once, on a clean pass.
        int p4Fallbacks = 0;
        for (int t : ticks) {
            NoteHarmonicContext ctx =
                mu::notation::analyzeHarmonicContextAtTick(score, Fraction::fromTicks(t));
            if (!ctx.wasRegional) {
                ++p4Fallbacks;
            }
        }

        std::vector<PerfRunStats> runStats;
        runStats.reserve(kPerfRuns);
        std::vector<double> slowestLatencies;    // from the run with the largest max
        std::vector<int>    slowestTicks;
        double globalMax = -1.0;

        for (int run = 0; run < kPerfRuns; ++run) {
            std::vector<double> latencies;
            latencies.reserve(ticks.size());
            for (int t : ticks) {
                const auto t0 = std::chrono::steady_clock::now();
                NoteHarmonicContext ctx =
                    mu::notation::analyzeHarmonicContextAtTick(score, Fraction::fromTicks(t));
                const auto t1 = std::chrono::steady_clock::now();
                const double ms =
                    std::chrono::duration<double, std::milli>(t1 - t0).count();
                latencies.push_back(ms);
                (void)ctx;
            }
            PerfRunStats st;
            st.medianMs = medianSorted(latencies);
            st.p95Ms    = percentileNearestRank(latencies, 95.0);
            st.maxMs    = *std::max_element(latencies.begin(), latencies.end());
            st.totalMs  = std::accumulate(latencies.begin(), latencies.end(), 0.0);
            runStats.push_back(st);

            if (st.maxMs > globalMax) {
                globalMax = st.maxMs;
                slowestLatencies = latencies;
                slowestTicks = ticks;
            }
        }

        // Median-of-runs for each aggregate.
        std::vector<double> medianVals, p95Vals, maxVals, totalVals;
        for (const auto& st : runStats) {
            medianVals.push_back(st.medianMs);
            p95Vals.push_back(st.p95Ms);
            maxVals.push_back(st.maxMs);
            totalVals.push_back(st.totalMs);
        }

        // Top-3 slowest ticks (window-expansion outliers) from the slowest run.
        std::vector<size_t> idx(slowestLatencies.size());
        std::iota(idx.begin(), idx.end(), 0);
        std::sort(idx.begin(), idx.end(),
                  [&](size_t a, size_t b) { return slowestLatencies[a] > slowestLatencies[b]; });

        report << "score=" << ps.id
               << " sizeClass=\"" << ps.sizeClass << "\""
               << " measures=" << measureCount
               << " queries=" << ticks.size()
               << " medianMs=" << medianSorted(medianVals)
               << " p95Ms=" << medianSorted(p95Vals)
               << " maxMs=" << medianSorted(maxVals)
               << " sweepTotalMs=" << medianSorted(totalVals)
               << " p4Fallbacks=" << p4Fallbacks
               << "\n";
        report << "  outliers(top3 of slowest run):";
        for (int k = 0; k < 3 && k < static_cast<int>(idx.size()); ++k) {
            const size_t i = idx[k];
            Measure* m = score->tick2measure(Fraction::fromTicks(slowestTicks[i]));
            const int mn = m ? (m->measureNumber() + 1) : -1;
            report << " [tick=" << slowestTicks[i]
                   << " m=" << mn
                   << " " << slowestLatencies[i] << "ms]";
        }
        report << "\n";

        // Coarse attribution for the single slowest tick IF it is egregious
        // (>100 ms).  We cannot instrument inside
        // analyzeNoteHarmonicContextRegionallyInWindow without touching
        // production, so we reconstruct one expansion iteration: the cost of a
        // single (analyzeHarmonicRhythm, analyzeSection) pair over the initial
        // ±1-measure window.  The real query runs up to 9 such iterations with
        // a growing window; this gives the Pass-0-vs-analyzeSection ratio of
        // one representative iteration, not the full multiplier.
        if (!idx.empty() && slowestLatencies[idx[0]] > kEgregiousMs) {
            const int slowTick = slowestTicks[idx[0]];
            Measure* cur = score->tick2measure(Fraction::fromTicks(slowTick));
            if (cur) {
                Measure* startM = cur->prevMeasure() ? cur->prevMeasure() : cur;
                Measure* endM   = cur->nextMeasure() ? cur->nextMeasure() : cur;
                const Fraction ws = startM->tick();
                const Fraction we = endM->endTick();
                const auto a0 = std::chrono::steady_clock::now();
                const auto rawRegions = mu::notation::analyzeHarmonicRhythm(
                    score, ws, we, /*excludeStaves=*/{},
                    mu::notation::HarmonicRegionGranularity::Smoothed);
                const auto a1 = std::chrono::steady_clock::now();
                const auto section = mu::composing::analysis::analyzeSection(
                    score, ws, we, /*excludeStaves=*/{}, rawRegions);
                const auto a2 = std::chrono::steady_clock::now();
                (void)section;
                report << "  attribution(slowest tick, single ±1-measure iter): pass0Ms="
                       << std::chrono::duration<double, std::milli>(a1 - a0).count()
                       << " analyzeSectionMs="
                       << std::chrono::duration<double, std::milli>(a2 - a1).count()
                       << "\n";
            }
        } else {
            report << "  attribution: no egregious (>100ms) query — skipped\n";
        }

        delete score;
    }

    report << "==== P3PERF END ====\n";
    // Single emission to stdout (captured by the runner).  The machine-readable
    // block between the BEGIN/END markers is what docs/perf_p3_baseline.md is
    // lifted from.
    std::cout << report.str() << std::endl;
}

// ── OI-203: the record-arm note-seam interactive-latency measurement (read-only) ──────────────────
//
// THE SUBJECT. The notation switch (2026-07-27) put the joint record path on the DEFAULT in-app
// notation analysis (useJointNotationRecord ON). Its note seam (analyzeHarmonicContextAtTick, flag ON)
// runs produceNotationRecord — a WHOLE-SCORE decode — on every interactive query (the status bar fires
// per note selection), BYPASSING the legacy bounded-window decode cache (see the record-arm branch in
// analyzeHarmonicContextAtTick). OI-203 declared this latency at the note-seam build and DEFERRED the
// record-cache design to a later, measured increment (#17: measure before build). THIS is that
// measurement — measurement ONLY; the keyed-record-cache design returns to Cowork WITH these numbers.
// No production code is touched (a DISABLED test-layer instrument, the P3PerfBaseline pattern).
//
// Per perf-corpus score (the shared kPerfCorpus: small chorale -> mid piano -> contrapuntal prelude ->
// sonata movement, spanning the snapshot corpus + a corpus-scale piece), at the record arm (flag ON):
//   (a) produce_cold_ms   — one whole-score produceNotationRecord (COLD; the producer has no cache, so
//                           every call is cold). This is the cost the funnel pays PER query today.
//   (b) funnel_per_query  — analyzeHarmonicContextAtTick per chord-bearing tick (flag ON): the cost a
//                           consumer experiences TODAY = a whole-score produce + the record lookup, per query.
//   (c) memoized_per_query— the per-query cost WERE the record memoized: produce ONCE, then noteView(rec, tick)
//                           per tick. This is the measured BOUND the record-cache design will be judged against.
// Emits a human table on stdout + the generated artifact tools/notation_seams/noteseam_latency.json (#17f).
//
// DISABLED: a measurement, not a regression gate (timing is machine-dependent). Regenerate the artifact:
//   ./pipeline_snapshot_tests.exe --gtest_also_run_disabled_tests --gtest_filter='*NoteSeamLatency*'
TEST(NoteSeamLatency, DISABLED_Sweep)
{
    auto analysisCfg = muse::modularity::globalIoc()->resolve<
        mu::composing::IComposingAnalysisConfiguration>("composing");
    ASSERT_TRUE(analysisCfg) << "IComposingAnalysisConfiguration not registered";
    analysisCfg->setUseRegionalAccumulation(true);
    analysisCfg->setUseJointNotationRecord(true);   // the record arm — the DEFAULT since the switch

    // one per-query latency vector -> its per-run aggregate
    auto statsOf = [](std::vector<double> v) {
        PerfRunStats st;
        st.medianMs = medianSorted(v);
        st.p95Ms    = percentileNearestRank(v, 95.0);
        st.maxMs    = v.empty() ? 0.0 : *std::max_element(v.begin(), v.end());
        st.totalMs  = std::accumulate(v.begin(), v.end(), 0.0);
        return st;
    };
    // median-of-runs of one PerfRunStats field across the runs (the P3PerfBaseline reporting convention)
    auto medOfRuns = [](const std::vector<PerfRunStats>& runs, double PerfRunStats::* field) {
        std::vector<double> vals;
        for (const auto& r : runs) {
            vals.push_back(r.*field);
        }
        return medianSorted(vals);
    };

    std::ostringstream report;
    report << "\n==== NOTESEAM-LATENCY BEGIN ====\n";
    report << "runs_per_score=" << kPerfRuns << " record_arm=on\n";

    QJsonArray scoresArr;

    for (const PerfScore& ps : kPerfCorpus) {
        const QString scorePath = perfCorpusPath(ps);
        ASSERT_TRUE(QFileInfo::exists(scorePath))
            << "Perf corpus score missing: " << scorePath.toStdString();
        MasterScore* score = ScoreRW::readScore(muse::String::fromQString(scorePath),
                                                /*isAbsolutePath=*/true);
        ASSERT_TRUE(score) << "Failed to load perf score: " << scorePath.toStdString();

        // size facts for the scaling table
        int measureCount = 0;
        for (Measure* m = score->firstMeasure(); m; m = m->nextMeasure()) {
            ++measureCount;
        }
        int noteCount = 0;
        for (Segment* s = score->firstSegment(SegmentType::ChordRest); s;
             s = s->next1(SegmentType::ChordRest)) {
            for (track_idx_t tr = 0; tr < score->ntracks(); ++tr) {
                mu::engraving::EngravingItem* e = s->element(tr);
                if (e && e->isChord()) {
                    noteCount += static_cast<int>(toChord(e)->notes().size());
                }
            }
        }

        // the funnel excludes the same chord-track staves the note-seam consumer passes (OI-204 parity;
        // the perf corpus carries no chord track, so this is the empty set — decode the whole score).
        const std::set<size_t> exclude = mu::notation::chordTrackExcludeStaves(score);
        const std::vector<int> ticks = collectChordBearingTicks(score);
        ASSERT_FALSE(ticks.empty());

        // The funnel per query (b) IS a whole-score produce per query, so measuring it over EVERY tick
        // would be (ticks x produce) — hours on the largest score. The per-query wall time is
        // produce-dominated (~constant per tick), so we SAMPLE evenly-spaced ticks for (b); (c)'s
        // noteView is a microsecond lookup, so it sweeps every tick. The sampled count is on the artifact.
        constexpr int kFunnelRuns = 3;
        constexpr int kFunnelSampleTicks = 12;
        std::vector<int> sampledTicks;
        {
            const int n = static_cast<int>(ticks.size());
            const int want = std::min(kFunnelSampleTicks, n);
            for (int k = 0; k < want; ++k) {
                const int idx = (want == 1)
                                ? 0
                                : static_cast<int>(std::llround(static_cast<double>(k) * (n - 1) / (want - 1)));
                sampledTicks.push_back(ticks[idx]);
            }
        }

        // (a) whole-score produceNotationRecord, cold (the producer memoizes nothing — every call cold).
        std::vector<double> produceMs;
        for (int run = 0; run < kPerfRuns; ++run) {
            const auto t0 = std::chrono::steady_clock::now();
            const auto rec = produceNotationRecord(score, std::string(ps.id), exclude);
            const auto t1 = std::chrono::steady_clock::now();
            ASSERT_TRUE(rec.ok) << "produceNotationRecord failed for " << ps.id;
            produceMs.push_back(std::chrono::duration<double, std::milli>(t1 - t0).count());
        }

        // (b) the note-seam funnel per query TODAY (flag ON = a whole-score produce + record lookup per
        //     query), on the sampled ticks; (c) the per-query cost were the record memoized (produce ONCE,
        //     then noteView per tick), swept over EVERY tick (noteView is a cheap lookup).
        std::vector<PerfRunStats> funnelRuns, memoRuns;
        for (int run = 0; run < kFunnelRuns; ++run) {
            std::vector<double> funnel;
            funnel.reserve(sampledTicks.size());
            for (int t : sampledTicks) {
                const auto a0 = std::chrono::steady_clock::now();
                NoteHarmonicContext ctx = mu::notation::analyzeHarmonicContextAtTick(
                    score, Fraction::fromTicks(t), 0, exclude);
                const auto a1 = std::chrono::steady_clock::now();
                funnel.push_back(std::chrono::duration<double, std::milli>(a1 - a0).count());
                (void)ctx;
            }
            funnelRuns.push_back(statsOf(funnel));
        }
        for (int run = 0; run < kPerfRuns; ++run) {
            const auto rec = produceNotationRecord(score, std::string(ps.id), exclude);
            ASSERT_TRUE(rec.ok);
            std::vector<double> memo;
            memo.reserve(ticks.size());
            for (int t : ticks) {
                const auto a0 = std::chrono::steady_clock::now();
                const mu::composing::analysis::joint::NoteView nv =
                    mu::composing::analysis::joint::noteView(rec.record, t);
                const auto a1 = std::chrono::steady_clock::now();
                memo.push_back(std::chrono::duration<double, std::milli>(a1 - a0).count());
                (void)nv;
            }
            memoRuns.push_back(statsOf(memo));
        }

        const double produceMedian = medianSorted(produceMs);
        const double funnelMedian  = medOfRuns(funnelRuns, &PerfRunStats::medianMs);
        const double funnelP95     = medOfRuns(funnelRuns, &PerfRunStats::p95Ms);
        const double funnelMax     = medOfRuns(funnelRuns, &PerfRunStats::maxMs);
        const double memoMedian    = medOfRuns(memoRuns, &PerfRunStats::medianMs);
        const double memoP95       = medOfRuns(memoRuns, &PerfRunStats::p95Ms);
        const double memoMax       = medOfRuns(memoRuns, &PerfRunStats::maxMs);

        report << "score=" << ps.id
               << " sizeClass=\"" << ps.sizeClass << "\""
               << " measures=" << measureCount
               << " notes=" << noteCount
               << " queries=" << ticks.size()
               << " funnelSampleTicks=" << sampledTicks.size()
               << " produceColdMs=" << produceMedian
               << " funnelPerQueryMs(median/p95/max)=" << funnelMedian << "/" << funnelP95 << "/" << funnelMax
               << " memoizedPerQueryMs(median/p95/max)=" << memoMedian << "/" << memoP95 << "/" << memoMax
               << "\n";

        QJsonObject o;
        o["id"] = QString::fromUtf8(ps.id);
        o["sizeClass"] = QString::fromUtf8(ps.sizeClass);
        o["measures"] = measureCount;
        o["notes"] = noteCount;
        o["queries"] = static_cast<int>(ticks.size());
        o["funnel_sample_ticks"] = static_cast<int>(sampledTicks.size());
        o["produce_cold_ms_median"] = produceMedian;
        QJsonObject fq;
        fq["median"] = funnelMedian;
        fq["p95"] = funnelP95;
        fq["max"] = funnelMax;
        o["funnel_per_query_ms"] = fq;
        QJsonObject mq;
        mq["median"] = memoMedian;
        mq["p95"] = memoP95;
        mq["max"] = memoMax;
        o["memoized_per_query_ms"] = mq;
        scoresArr.append(o);

        delete score;
    }
    report << "==== NOTESEAM-LATENCY END ====\n";
    std::cout << report.str() << std::endl;

    QJsonObject root;
    root["instrument"] =
        QStringLiteral("src/notation/tests/pipeline_snapshot_tests/pipeline_snapshot_tests.cpp "
                       "NoteSeamLatency.DISABLED_Sweep");
    root["open_item"] = QStringLiteral("OI-203");
    root["purpose"] = QStringLiteral(
        "Record-arm note-seam interactive latency — MEASUREMENT ONLY (the keyed-record-cache design "
        "returns to Cowork with these numbers). (a) produce_cold_ms: one whole-score produceNotationRecord "
        "(cold; the funnel pays this per query today). (b) funnel_per_query_ms: analyzeHarmonicContextAtTick "
        "per query at the record arm (flag ON) = produce + record lookup. (c) memoized_per_query_ms: the "
        "per-query cost were the record memoized (produce once, then noteView per tick) — the bound the "
        "cache design is judged against.");
    root["record_arm"] = true;
    root["runs_per_score"] = kPerfRuns;
    root["unit"] = QStringLiteral(
        "milliseconds, wall (std::chrono::steady_clock); per-score aggregates are median-of-runs");
    root["machine"] =
        QSysInfo::prettyProductName() + QStringLiteral(" / ") + QSysInfo::currentCpuArchitecture();
    root["scores"] = scoresArr;

    const QString outPath = QStringLiteral(PIPELINE_SNAPSHOT_CORPUS_ROOT)
                            + QStringLiteral("/tools/notation_seams/noteseam_latency.json");
    QDir().mkpath(QFileInfo(outPath).absolutePath());
    const QByteArray bytes = serializeSnapshot(root).toUtf8();
    QFile out(outPath);
    ASSERT_TRUE(out.open(QIODevice::WriteOnly | QIODevice::Truncate)) << out.errorString().toStdString();
    ASSERT_EQ(out.write(bytes), static_cast<qint64>(bytes.size()));
    out.close();
    std::cout << "wrote " << outPath.toStdString() << std::endl;

    analysisCfg->setUseJointNotationRecord(false);   // leave the shared flag as the suite expects it
}

// ══ OI-206 / OI-203 ANALYSIS-COST PROFILE (READ-ONLY measurement) ═════════════════════════════════
//
// Dispatch cc_instruction_analysis_cost_profile.md. WHERE the analysis time goes, HOW it scales, and
// which analysis-extent candidates are viable. MEASUREMENT ONLY — a DISABLED test-layer sweep (the
// NoteSeamLatency / P3PerfBaseline pattern); NO production code is instrumented or modified.
//
// produceNotationRecord(score) is composed of FOUR separately-callable steps (jointnotationproducer.cpp):
//   phase 1  buildAdapterFacts(score)                         — score reading / L1 fact extraction
//   phase 2  JointTables::loadEmbedded + FittedAdapter        — embedded table/adapter/weight load (per call)
//   phase 3  decodePiece(...)                                 — the §5 semi-Markov Viterbi decode
//   phase 4  assembleNotationRecord(...)                      — derived facts + the §3.3 posterior slice
// This instrument times each phase separately (so the split is real, not reconstructed) and additionally
// isolates computePosteriorSlice (the §3.3 slice) inside phase 4. The content-scoring-vs-dynamic-program
// split WITHIN phase 3 is measured on the byte-identical Python reference decoder (tools/joint_estimator/
// gen_content_dp_split.py) — decodePiece is a single src/ call this read-only instrument may not carve.
//
// It runs the shared kPerfCorpus (chorale-scale, DCML-covered) + the 23 user-committed large scores
// (tools/extra scores/large/ — orchestral; a class the adapter and decoder have never seen: a surprise
// is a STOP). Two tests: LargeScoreCounts (cheap phases + counts + boundary/viewport — always safe) and
// LargeScoreDecodeProfile (adds the decode; env LARGE_PROFILE_MAX_EVENTS caps which scores are decoded,
// so the possibly-intractable largest are recorded counts-only and extrapolated, never force-run).
//
// Regenerate:
//   ./pipeline_snapshot_tests.exe --gtest_also_run_disabled_tests --gtest_filter='*LargeScoreCounts*'
//   LARGE_PROFILE_MAX_EVENTS=4000 ./pipeline_snapshot_tests.exe --gtest_also_run_disabled_tests \
//       --gtest_filter='*LargeScoreDecodeProfile*'

struct LargeScore {
    const char* id;
    const char* relPath;   // under PIPELINE_SNAPSHOT_CORPUS_ROOT (= repo root); the dir has a SPACE
};

// The 23 user-committed large scores (tools/extra scores/large/), ratified as the ground-truth-false
// large-score set (docs/score_inventory.md). Orchestral / large-ensemble — the new size regime.
constexpr LargeScore kLargeCorpus[] = {
    { "bach_brandenburg3_bwv1048",   "tools/extra scores/large/bach-brandenburg-concerto-no-3-bwv-1048.mscz" },
    { "bach_brandenburg3_short",     "tools/extra scores/large/bach-brandenburg-concerto-no-3.mscz" },
    { "bach_brandenburg4_mvt3",      "tools/extra scores/large/bach-brandenburg-concerto-no-4-bwv-1049-mvt-iii-presto.mscz" },
    { "bach_mass_bwv232_part1",      "tools/extra scores/large/bach-mass-in-b-minor-bwv-232-part-1.mscz" },
    { "bach_art_of_fugue",           "tools/extra scores/large/bach-the-art-of-the-fugue.mscz" },
    { "beethoven_sym7_i",            "tools/extra scores/large/beethoven-ludwig-van-symphony-no-7-op-92-i-poco-sostenuto.mscz" },
    { "beethoven_sym9",              "tools/extra scores/large/beethoven-symphony-no-9-op-125.mscz" },
    { "butterworth_green_willow",    "tools/extra scores/large/butterworth-the-banks-of-green-willow.mscz" },
    { "dvorak_cello_concerto_mvt3",  "tools/extra scores/large/dvorak-cello-concerto-in-b-minor-movement-iii.mscz" },
    { "dvorak_cello_concerto_mvt1",  "tools/extra scores/large/dvorak-cello-concerto-in-b-minor-mvt-1.mscz" },
    { "dvorak_cello_concerto_mvt2",  "tools/extra scores/large/dvorak-cello-concerto-in-b-minor-mvt-ii.mscz" },
    { "dvorak_sym9_i",               "tools/extra scores/large/dvorak-symphony-no-9-mvt-i.mscz" },
    { "faure_piano_quintet2",        "tools/extra scores/large/faure-piano-quintet-no-2-op-115.mscz" },
    { "gluck_iphigenie",             "tools/extra scores/large/gluck-iphigenie-en-aulide-vocal-score.mscz" },
    { "haydn_sym8_le_soir",          "tools/extra scores/large/haydn-8th-symphony-le-soir.mscz" },
    { "haydn_sym6",                  "tools/extra scores/large/haydn-symphony-no-6.mscz" },
    { "holst_mercury",               "tools/extra scores/large/holst-openscore-transcription-of-mercury.mscz" },
    { "holst_planets",               "tools/extra scores/large/holst-the-planets-op-32.mscz" },
    { "mozart_jupiter_k551",         "tools/extra scores/large/mozart-symphony-no-41-jupiter-k-551.mscz" },
    { "mozart_jupiter",              "tools/extra scores/large/mozart-symphony-no-41-jupiter.mscz" },
    { "schubert_d810_death_maiden",  "tools/extra scores/large/string-quartet-in-d-minor-d-810-death-and-the-maiden-franz-schubert.mscz" },
    { "beethoven_sym9_openscore",    "tools/extra scores/large/symphony-no9-op125-ludwig-van-beethoven-beethoven-symphony-no-9-op-125-arranged-bu-andrew-moranty-credit-to-openscore.mscz" },
    { "tchaikovsky_1812",            "tools/extra scores/large/tchaikovsky-1812-overture.mscz" },
};

#ifdef _WIN32
static size_t currentWorkingSetBytes()
{
    MU_PROCESS_MEMORY_COUNTERS pmc{};
    if (K32GetProcessMemoryInfo(GetCurrentProcess(), &pmc,
                                static_cast<unsigned long>(sizeof(pmc)))) {
        return static_cast<size_t>(pmc.WorkingSetSize);
    }
    return 0;
}
static size_t peakWorkingSetBytes()
{
    MU_PROCESS_MEMORY_COUNTERS pmc{};
    if (K32GetProcessMemoryInfo(GetCurrentProcess(), &pmc,
                                static_cast<unsigned long>(sizeof(pmc)))) {
        return static_cast<size_t>(pmc.PeakWorkingSetSize);
    }
    return 0;
}
#else
static size_t currentWorkingSetBytes() { return 0; }
static size_t peakWorkingSetBytes() { return 0; }
#endif

// ── file size (bytes) of a score on disk ──
static qint64 fileSizeBytes(const QString& absPath)
{
    QFileInfo fi(absPath);
    return fi.exists() ? fi.size() : -1;
}

// ── Task 4b: structural-boundary evidence per score, read straight from the engraving DOM (the same
// cues phraseboundaryview.cpp reads: fermatas, structural barlines, rehearsal marks, all-part rests).
// Returns the SORTED UNION of boundary ticks + a per-source count. All-part-rest spans are the maximal
// gaps in the union of every note's [onset, onset+dur) interval that are >= restThresholdTicks. ──
struct BoundaryEvidence {
    int fermatas = 0;
    int structuralBarlines = 0;   // double / final / repeat
    int rehearsalMarks = 0;
    int keySigChanges = 0;
    int restSpans = 0;            // maximal all-part-rest gaps >= threshold
    std::vector<int> boundaryTicks;   // sorted union of all of the above
};

static BoundaryEvidence collectBoundaryEvidence(MasterScore* score, int restThresholdTicks)
{
    using namespace mu::engraving;
    BoundaryEvidence ev;
    std::set<int> ticks;

    const Measure* firstMeasure = score->firstMeasure();
    if (!firstMeasure) {
        return ev;
    }

    // fermatas + rehearsal marks — segment annotations (any segment).
    for (const Segment* s = firstMeasure->first(); s; s = s->next1()) {
        for (const EngravingItem* a : s->annotations()) {
            if (!a) {
                continue;
            }
            if (a->isFermata()) {
                ++ev.fermatas;
                ticks.insert(s->tick().ticks());
            } else if (a->isRehearsalMark()) {
                ++ev.rehearsalMarks;
                ticks.insert(s->tick().ticks());
            }
        }
    }

    // structural barlines — double / final / repeat (a notational division).
    for (const Measure* m = firstMeasure; m; m = m->nextMeasure()) {
        const BarLineType bt = m->endBarLineType();
        if (bt == BarLineType::DOUBLE || bt == BarLineType::END
            || bt == BarLineType::END_REPEAT || bt == BarLineType::END_START_REPEAT) {
            ++ev.structuralBarlines;
            ticks.insert(m->endTick().ticks());
        }
        if (m->repeatStart()) {
            ++ev.structuralBarlines;
            ticks.insert(m->tick().ticks());
        }
    }

    // mid-score key-signature CHANGE (staff 0's engraved signature differs from the prevailing one).
    if (score->nstaves() > 0 && score->staff(0)) {
        int prevKey = static_cast<int>(score->staff(0)->keySigEvent(Fraction(0, 1)).concertKey());
        for (const Segment* s = firstMeasure->first(SegmentType::KeySig); s;
             s = s->next1(SegmentType::KeySig)) {
            const KeySig* ks = nullptr;
            for (const EngravingItem* e : s->elist()) {
                if (e && e->isKeySig()) { ks = toKeySig(e); break; }
            }
            if (!ks) { continue; }
            const int key = static_cast<int>(ks->concertKey());
            const int tick = s->tick().ticks();
            if (key != prevKey && tick > 0) {
                ++ev.keySigChanges;
                ticks.insert(tick);
            }
            prevKey = key;
        }
    }

    // all-part-rest spans — maximal gaps in the union of every note's sounding interval >= threshold.
    std::vector<std::pair<int, int> > iv;   // [onset, onset+dur)
    int maxEndTick = 0;
    for (const Segment* s = score->firstSegment(SegmentType::ChordRest); s;
         s = s->next1(SegmentType::ChordRest)) {
        for (track_idx_t tr = 0; tr < score->ntracks(); ++tr) {
            EngravingItem* e = s->element(tr);
            if (e && e->isChord()) {
                const int on = s->tick().ticks();
                const int du = toChord(e)->actualTicks().ticks();
                if (du > 0) {
                    iv.emplace_back(on, on + du);
                    maxEndTick = std::max(maxEndTick, on + du);
                }
            }
        }
    }
    if (!iv.empty()) {
        std::sort(iv.begin(), iv.end());
        int coveredEnd = iv.front().first;   // start of the first sound
        for (const auto& p : iv) {
            if (p.first > coveredEnd) {       // a gap [coveredEnd, p.first)
                if (p.first - coveredEnd >= restThresholdTicks) {
                    ++ev.restSpans;
                    ticks.insert(coveredEnd);
                }
            }
            coveredEnd = std::max(coveredEnd, p.second);
        }
    }

    ev.boundaryTicks.assign(ticks.begin(), ticks.end());
    return ev;
}

// median of a vector (copy), 0 on empty.
static double medOf(std::vector<double> v)
{
    return medianSorted(std::move(v));
}

// popcount for a 12-bit pc mask (uint16_t).
static int pcPopcount(uint16_t m)
{
    int n = 0;
    while (m) { m &= static_cast<uint16_t>(m - 1); ++n; }
    return n;
}

// Count events UNCOVERABLE by the decoder's >=2-member content gate: an event is uncoverable iff every
// <=segCap segment containing it has an onset-pc UNION with <2 distinct pcs (so no vocabulary class can
// have >=2 members present, and no finite-content candidate covers it -> V[N] empty -> segs=0).
static int countUncoverableEvents(const mu::composing::analysis::joint::Piece& piece, int segCap)
{
    const int n = static_cast<int>(piece.events.size());
    int uncoverable = 0;
    for (int e = 0; e < n; ++e) {
        bool coverable = false;
        // any segment [i, j) with i <= e < j <= min(n, i+segCap)
        for (int i = std::max(0, e - segCap + 1); i <= e && !coverable; ++i) {
            uint16_t onsetUnion = 0;
            const int jmax = std::min(n, i + segCap);
            for (int j = i + 1; j <= jmax; ++j) {
                onsetUnion |= piece.evOnsetPcs[static_cast<size_t>(j - 1)];
                if (j > e && pcPopcount(onsetUnion) >= 2) {   // this segment contains e and has >=2 pcs
                    coverable = true;
                    break;
                }
            }
        }
        if (!coverable) {
            ++uncoverable;
        }
    }
    return uncoverable;
}

// ── the size facts, phase-1/phase-2 timings, boundary evidence, and viewport density for one score.
// Written by BOTH tests; the decode test adds phase 3/4 on top. ──
struct ScoreProfile {
    std::string id;
    std::string sizeClass;   // "" for large corpus
    bool loaded = false;
    std::string error;
    // counts
    int staves = 0;
    int parts = 0;
    int measures = 0;
    int scoreChordNotes = 0;   // sum of chord notes read from the DOM (whole score)
    qint64 fileBytes = -1;
    // adapter (phase 1) facts
    bool adapterOk = false;
    std::string adapterError;
    int adapterNotes = 0;      // fx.piece.notes.size() — the fact adapter's note-event count
    int adapterEvents = 0;     // fx.piece.events.size() — the event lattice size
    bool multiMeter = false;
    // segs=0 diagnosis: events with no onset pcs / no sounding pcs, and the longest consecutive run.
    // The decoder's candidates use the union of evOnsetPcs over a segment (jointdecoder.cpp); a run of
    // onset-empty events longer than segCap (4) cannot be bridged by any <=segCap segment with a
    // candidate, so the semi-Markov DP cannot reach V[N] and returns complete=false with 0 segments.
    int emptyOnsetEvents = 0;
    int maxEmptyOnsetRun = 0;
    int emptyOverlapEvents = 0;
    int maxEmptyOverlapRun = 0;
    // The decoder skips a candidate class unless >=2 of its members are present in the segment's ONSET-pc
    // union (jointdecoder.cpp:444-445). So an event is UNCOVERABLE iff EVERY <=segCap segment containing
    // it has an onset-pc union with <2 distinct pcs — no class can have 2 members present, so no finite-
    // content candidate covers it, and V[N] cannot be reached (segs=0). This scan counts uncoverable
    // events directly (a proxy: <2 distinct onset pcs necessarily fails the >=2-member gate).
    int uncoverableEvents = 0;
    // timings (ms, median of runs)
    double phase1BuildFactsMs = 0.0;
    double phase2LoadTablesMs = 0.0;
    // memory (bytes)
    size_t wsAfterLoadScore = 0;
    size_t wsAfterBuildFacts = 0;
    // boundary evidence
    BoundaryEvidence boundary;
    // Task 4b: the enclosing-unit sizes between consecutive structural boundaries, exact in MEASURES
    // and in EVENTS (the tail is the failure mode — the distribution, not the mean). Includes the
    // implicit first/last boundaries at the piece ends so a boundary-free piece yields ONE whole-piece
    // unit rather than an empty list.
    std::vector<int> gapMeasures;
    std::vector<int> gapEvents;
    // viewport (events in first K measures — a "screen" proxy)
    int eventsFirst4Measures = 0;
    int eventsFirst8Measures = 0;
};

// Map each boundary tick to its measure index + event index, then the unit sizes (gaps) between
// consecutive boundaries, with the piece's own ends as implicit boundaries. Exact — no meter assumption.
static void computeBoundaryGaps(MasterScore* score,
                                const mu::composing::analysis::joint::Piece& piece,
                                const std::vector<int>& boundaryTicks,
                                std::vector<int>& gapMeasures, std::vector<int>& gapEvents)
{
    using namespace mu::engraving;
    // measure-start ticks
    std::vector<int> measureTicks;
    for (Measure* m = score->firstMeasure(); m; m = m->nextMeasure()) {
        measureTicks.push_back(m->tick().ticks());
    }
    const int nMeasures = static_cast<int>(measureTicks.size());
    const int nEvents = static_cast<int>(piece.events.size());
    // event-start ticks (sorted by construction)
    std::vector<int> eventTicks;
    eventTicks.reserve(piece.events.size());
    for (const auto& e : piece.events) {
        eventTicks.push_back(e.start);
    }
    auto measureIndexOf = [&](int tick) {
        // last measure whose start <= tick
        int idx = static_cast<int>(std::upper_bound(measureTicks.begin(), measureTicks.end(), tick)
                                   - measureTicks.begin()) - 1;
        return std::max(0, std::min(idx, nMeasures - 1));
    };
    auto eventIndexOf = [&](int tick) {
        return static_cast<int>(std::lower_bound(eventTicks.begin(), eventTicks.end(), tick)
                                - eventTicks.begin());
    };
    // boundary set with implicit piece ends
    std::vector<int> bm, be;
    bm.push_back(0);
    be.push_back(0);
    for (int t : boundaryTicks) {
        bm.push_back(measureIndexOf(t));
        be.push_back(eventIndexOf(t));
    }
    bm.push_back(nMeasures);
    be.push_back(nEvents);
    std::sort(bm.begin(), bm.end());
    std::sort(be.begin(), be.end());
    for (size_t i = 1; i < bm.size(); ++i) {
        const int gm = bm[i] - bm[i - 1];
        const int ge = be[i] - be[i - 1];
        if (gm > 0 || ge > 0) {
            gapMeasures.push_back(gm);
            gapEvents.push_back(ge);
        }
    }
}

// count events (adapter lattice) whose start tick is < the tick at measure index `k` (0-based).
static int eventsBeforeMeasure(MasterScore* score,
                               const mu::composing::analysis::joint::Piece& piece, int k)
{
    using namespace mu::engraving;
    int idx = 0, capTick = std::numeric_limits<int>::max();
    for (Measure* m = score->firstMeasure(); m; m = m->nextMeasure(), ++idx) {
        if (idx == k) { capTick = m->tick().ticks(); break; }
    }
    int n = 0;
    for (const auto& ev : piece.events) {
        if (ev.start < capTick) { ++n; }
    }
    return n;
}

// Run phases 1 (buildAdapterFacts) + 2 (embedded table/adapter/weight load) + the counts/boundary/
// viewport facts for one already-loaded score. `runs` = timing repeats (median reported).
static ScoreProfile profileCheapPhases(MasterScore* score, const std::string& id,
                                       const std::string& sizeClass, const QString& absPath, int runs)
{
    using namespace mu::composing::analysis::joint;
    ScoreProfile p;
    p.id = id;
    p.sizeClass = sizeClass;
    p.loaded = true;
    p.fileBytes = fileSizeBytes(absPath);

    for (mu::engraving::Measure* m = score->firstMeasure(); m; m = m->nextMeasure()) {
        ++p.measures;
    }
    p.staves = static_cast<int>(score->nstaves());
    p.parts = static_cast<int>(score->parts().size());
    for (mu::engraving::Segment* s = score->firstSegment(mu::engraving::SegmentType::ChordRest); s;
         s = s->next1(mu::engraving::SegmentType::ChordRest)) {
        for (mu::engraving::track_idx_t tr = 0; tr < score->ntracks(); ++tr) {
            mu::engraving::EngravingItem* e = s->element(tr);
            if (e && e->isChord()) {
                p.scoreChordNotes += static_cast<int>(mu::engraving::toChord(e)->notes().size());
            }
        }
    }

    p.wsAfterLoadScore = currentWorkingSetBytes();

    // phase 1 — buildAdapterFacts (score -> facts). Timed; the facts of the last run are kept.
    std::vector<double> p1;
    AdapterFacts fx;
    for (int r = 0; r < runs; ++r) {
        const auto t0 = std::chrono::steady_clock::now();
        fx = buildAdapterFacts(score, id, /*excludeStaves=*/{});
        const auto t1 = std::chrono::steady_clock::now();
        p1.push_back(std::chrono::duration<double, std::milli>(t1 - t0).count());
    }
    p.phase1BuildFactsMs = medOf(p1);
    p.wsAfterBuildFacts = currentWorkingSetBytes();
    p.adapterOk = fx.ok;
    if (!fx.ok) {
        p.adapterError = fx.error;
    } else {
        p.adapterNotes = static_cast<int>(fx.piece.notes.size());
        p.adapterEvents = static_cast<int>(fx.piece.events.size());
        p.multiMeter = fx.multiMeter;
        p.eventsFirst4Measures = eventsBeforeMeasure(score, fx.piece, 4);
        p.eventsFirst8Measures = eventsBeforeMeasure(score, fx.piece, 8);
        // segs=0 diagnosis: scan the event lattice for onset-empty / silent events and the longest runs.
        int runOnset = 0, runOverlap = 0;
        const int nev = static_cast<int>(fx.piece.events.size());
        for (int e = 0; e < nev; ++e) {
            const bool onsetEmpty = (fx.piece.evOnsetPcs[static_cast<size_t>(e)] == 0);
            const bool overlapEmpty = (fx.piece.overlapPcs(e, e + 1) == 0);
            if (onsetEmpty) {
                ++p.emptyOnsetEvents; ++runOnset;
                p.maxEmptyOnsetRun = std::max(p.maxEmptyOnsetRun, runOnset);
            } else {
                runOnset = 0;
            }
            if (overlapEmpty) {
                ++p.emptyOverlapEvents; ++runOverlap;
                p.maxEmptyOverlapRun = std::max(p.maxEmptyOverlapRun, runOverlap);
            } else {
                runOverlap = 0;
            }
        }
        p.uncoverableEvents = countUncoverableEvents(fx.piece, /*segCap=*/4);
    }

    // phase 2 — embedded table + adapter + weight load (per-call; score-independent, timed here).
    std::vector<double> p2;
    for (int r = 0; r < runs; ++r) {
        const auto t0 = std::chrono::steady_clock::now();
        JointTables tables = JointTables::loadEmbedded("all");
        Vocabulary vocab(tables);
        const WeightVector selected = selectedWeights();
        FittedAdapter adapter = FittedAdapter::loadEmbedded(selected);
        const auto t1 = std::chrono::steady_clock::now();
        p2.push_back(std::chrono::duration<double, std::milli>(t1 - t0).count());
        if (!tables.loaded || !adapter.loaded()) {
            p.adapterError += " [phase2 load failed]";
        }
        (void)vocab;
    }
    p.phase2LoadTablesMs = medOf(p2);

    // boundary evidence + viewport (Task 4b/4c). Threshold: one whole note (1920 ticks) = a clear rest.
    p.boundary = collectBoundaryEvidence(score, /*restThresholdTicks=*/1920);
    if (fx.ok) {
        computeBoundaryGaps(score, fx.piece, p.boundary.boundaryTicks, p.gapMeasures, p.gapEvents);
    }
    return p;
}

static QJsonObject profileToJson(const ScoreProfile& p)
{
    QJsonObject o;
    o["id"] = QString::fromStdString(p.id);
    if (!p.sizeClass.empty()) { o["sizeClass"] = QString::fromStdString(p.sizeClass); }
    o["loaded"] = p.loaded;
    if (!p.error.empty()) { o["error"] = QString::fromStdString(p.error); }
    o["staves"] = p.staves;
    o["parts"] = p.parts;
    o["measures"] = p.measures;
    o["scoreChordNotes"] = p.scoreChordNotes;
    o["fileBytes"] = static_cast<double>(p.fileBytes);
    o["adapterOk"] = p.adapterOk;
    if (!p.adapterError.empty()) { o["adapterError"] = QString::fromStdString(p.adapterError); }
    o["adapterNotes"] = p.adapterNotes;
    o["adapterEvents"] = p.adapterEvents;
    o["multiMeter"] = p.multiMeter;
    o["emptyOnsetEvents"] = p.emptyOnsetEvents;
    o["maxEmptyOnsetRun"] = p.maxEmptyOnsetRun;
    o["emptyOverlapEvents"] = p.emptyOverlapEvents;
    o["maxEmptyOverlapRun"] = p.maxEmptyOverlapRun;
    o["uncoverableEvents"] = p.uncoverableEvents;
    o["phase1_build_facts_ms"] = p.phase1BuildFactsMs;
    o["phase2_load_tables_ms"] = p.phase2LoadTablesMs;
    o["ws_after_load_score_bytes"] = static_cast<double>(p.wsAfterLoadScore);
    o["ws_after_build_facts_bytes"] = static_cast<double>(p.wsAfterBuildFacts);
    QJsonObject b;
    b["fermatas"] = p.boundary.fermatas;
    b["structuralBarlines"] = p.boundary.structuralBarlines;
    b["rehearsalMarks"] = p.boundary.rehearsalMarks;
    b["keySigChanges"] = p.boundary.keySigChanges;
    b["restSpans"] = p.boundary.restSpans;
    b["boundaryCount"] = static_cast<int>(p.boundary.boundaryTicks.size());
    // gaps between consecutive boundary ticks (in ticks) — the tail is the failure mode (report max + list)
    QJsonArray gaps;
    for (size_t i = 1; i < p.boundary.boundaryTicks.size(); ++i) {
        gaps.append(p.boundary.boundaryTicks[i] - p.boundary.boundaryTicks[i - 1]);
    }
    b["gapTicks"] = gaps;
    // Task 4b: exact enclosing-unit sizes between structural boundaries (piece ends implicit), in
    // measures and events; the tail is the failure mode, so the full distribution + the max are emitted.
    QJsonArray gm, ge;
    int maxGapMeasures = 0, maxGapEvents = 0;
    for (int v : p.gapMeasures) { gm.append(v); maxGapMeasures = std::max(maxGapMeasures, v); }
    for (int v : p.gapEvents) { ge.append(v); maxGapEvents = std::max(maxGapEvents, v); }
    b["unitSizesMeasures"] = gm;
    b["unitSizesEvents"] = ge;
    b["maxUnitMeasures"] = maxGapMeasures;
    b["maxUnitEvents"] = maxGapEvents;
    b["nUnits"] = static_cast<int>(p.gapMeasures.size());
    o["boundary"] = b;
    o["eventsFirst4Measures"] = p.eventsFirst4Measures;
    o["eventsFirst8Measures"] = p.eventsFirst8Measures;
    return o;
}

// LargeScoreCounts — the ALWAYS-SAFE sweep: counts + phase 1 (buildAdapterFacts) + phase 2 (load) +
// boundary/viewport, over kPerfCorpus + the 23 large scores. No decode; the first orchestral-adapter
// exposure. Load or adapter failure is a FINDING (recorded), never silently dropped.
TEST(LargeScoreCounts, DISABLED_Sweep)
{
    auto analysisCfg = muse::modularity::globalIoc()->resolve<
        mu::composing::IComposingAnalysisConfiguration>("composing");
    if (analysisCfg) {
        analysisCfg->setUseRegionalAccumulation(true);
        analysisCfg->setUseJointNotationRecord(true);
    }

    constexpr int kCountRuns = 3;
    QJsonArray perfArr, largeArr;

    auto runOne = [&](const std::string& id, const std::string& sizeClass, const QString& relPath,
                      QJsonArray& into) {
        const QString absPath = QStringLiteral(PIPELINE_SNAPSHOT_CORPUS_ROOT)
                                + QLatin1Char('/') + relPath;
        if (!QFileInfo::exists(absPath)) {
            ScoreProfile p; p.id = id; p.error = "score file missing: " + absPath.toStdString();
            into.append(profileToJson(p));
            std::cout << "[counts] MISSING " << id << " (" << absPath.toStdString() << ")\n";
            return;
        }
        MasterScore* score = ScoreRW::readScore(muse::String::fromQString(absPath),
                                                /*isAbsolutePath=*/true);
        if (!score) {
            ScoreProfile p; p.id = id; p.error = "ScoreRW::readScore returned null (load failed)";
            into.append(profileToJson(p));
            std::cout << "[counts] LOAD-FAIL " << id << "\n";
            return;
        }
        ScoreProfile p = profileCheapPhases(score, id, sizeClass, absPath, kCountRuns);
        into.append(profileToJson(p));
        std::cout << "[counts] " << id
                  << " staves=" << p.staves << " parts=" << p.parts << " measures=" << p.measures
                  << " scoreChordNotes=" << p.scoreChordNotes
                  << " adapterOk=" << (p.adapterOk ? 1 : 0)
                  << " adapterNotes=" << p.adapterNotes << " adapterEvents=" << p.adapterEvents
                  << " p1ms=" << p.phase1BuildFactsMs << " p2ms=" << p.phase2LoadTablesMs
                  << " boundaries=" << p.boundary.boundaryTicks.size()
                  << " ws_facts_MB=" << (p.wsAfterBuildFacts / (1024.0 * 1024.0)) << "\n";
        delete score;
    };

    for (const PerfScore& ps : kPerfCorpus) {
        runOne(ps.id, ps.sizeClass, QString::fromUtf8(ps.relativePath), perfArr);
    }
    for (const LargeScore& ls : kLargeCorpus) {
        runOne(ls.id, "", QString::fromUtf8(ls.relPath), largeArr);
    }

    QJsonObject root;
    root["instrument"] = QStringLiteral("pipeline_snapshot_tests.cpp LargeScoreCounts.DISABLED_Sweep");
    root["open_item"] = QStringLiteral("OI-206 / cc_instruction_analysis_cost_profile.md Task 0/1/4");
    root["purpose"] = QStringLiteral(
        "Per-score counts (notes as the fact adapter counts them, staves, parts, measures, file size), "
        "phase 1 (buildAdapterFacts) + phase 2 (embedded table/weight load) timings + resident memory, "
        "structural-boundary evidence (Task 4b), and viewport event density (Task 4c). No decode.");
    root["rest_threshold_ticks"] = 1920;
    root["runs_per_score"] = kCountRuns;
    root["machine"] = QSysInfo::prettyProductName() + QStringLiteral(" / ")
                      + QSysInfo::currentCpuArchitecture();
    root["ticks_per_quarter"] = 480;
    root["perfCorpus"] = perfArr;
    root["largeCorpus"] = largeArr;

    const QString outPath = QStringLiteral(PIPELINE_SNAPSHOT_CORPUS_ROOT)
                            + QStringLiteral("/tools/notation_seams/large_score_profile_counts.json");
    QDir().mkpath(QFileInfo(outPath).absolutePath());
    const QByteArray bytes = serializeSnapshot(root).toUtf8();
    QFile out(outPath);
    ASSERT_TRUE(out.open(QIODevice::WriteOnly | QIODevice::Truncate)) << out.errorString().toStdString();
    ASSERT_EQ(out.write(bytes), static_cast<qint64>(bytes.size()));
    out.close();
    std::cout << "wrote " << outPath.toStdString() << std::endl;
    if (analysisCfg) { analysisCfg->setUseJointNotationRecord(false); }
}

// LargeScoreDecodeProfile — the FULL phase profile: phases 1-4 + the isolated §3.3 posterior slice +
// peak resident memory around the decode. Env LARGE_PROFILE_MAX_EVENTS (0 = no cap) decodes only scores
// whose adapter event count <= the cap; larger scores are recorded counts-only ("decodeSkipped") so the
// possibly-intractable largest are extrapolated, never force-run (feedback_never_stop_long_running).
TEST(LargeScoreDecodeProfile, DISABLED_Sweep)
{
    using namespace mu::composing::analysis::joint;
    auto analysisCfg = muse::modularity::globalIoc()->resolve<
        mu::composing::IComposingAnalysisConfiguration>("composing");
    if (analysisCfg) {
        analysisCfg->setUseRegionalAccumulation(true);
        analysisCfg->setUseJointNotationRecord(true);
    }

    long capEvents = 0;
    if (const char* env = std::getenv("LARGE_PROFILE_MAX_EVENTS")) {
        capEvents = std::atol(env);
    }
    constexpr int kDecodeRuns = 3;

    QJsonArray scoresArr;

    auto runOne = [&](const std::string& id, const std::string& sizeClass, const QString& relPath) {
        const QString absPath = QStringLiteral(PIPELINE_SNAPSHOT_CORPUS_ROOT)
                                + QLatin1Char('/') + relPath;
        QJsonObject o;
        o["id"] = QString::fromStdString(id);
        if (!sizeClass.empty()) { o["sizeClass"] = QString::fromStdString(sizeClass); }
        if (!QFileInfo::exists(absPath)) {
            o["error"] = QStringLiteral("score file missing");
            scoresArr.append(o);
            return;
        }
        MasterScore* score = ScoreRW::readScore(muse::String::fromQString(absPath),
                                                /*isAbsolutePath=*/true);
        if (!score) {
            o["error"] = QStringLiteral("load failed");
            scoresArr.append(o);
            std::cout << "[decode] LOAD-FAIL " << id << "\n";
            return;
        }

        // phase 1 — build facts (once; needed for the decode + the event count / cap decision).
        const size_t wsBase = currentWorkingSetBytes();
        AdapterFacts fx = buildAdapterFacts(score, id, /*excludeStaves=*/{});
        o["adapterOk"] = fx.ok;
        if (!fx.ok) {
            o["adapterError"] = QString::fromStdString(fx.error);
            scoresArr.append(o);
            std::cout << "[decode] ADAPTER-FAIL " << id << " : " << fx.error << "\n";
            delete score;
            return;
        }
        const int nNotes = static_cast<int>(fx.piece.notes.size());
        const int nEvents = static_cast<int>(fx.piece.events.size());
        o["adapterNotes"] = nNotes;
        o["adapterEvents"] = nEvents;
        o["staves"] = static_cast<int>(score->nstaves());

        if (capEvents > 0 && nEvents > capEvents) {
            o["decodeSkipped"] = QStringLiteral("adapterEvents exceeds LARGE_PROFILE_MAX_EVENTS");
            scoresArr.append(o);
            std::cout << "[decode] SKIP " << id << " (events=" << nEvents << " > cap=" << capEvents << ")\n";
            delete score;
            return;
        }

        // phase 1 timing (re-timed cleanly, median of runs).
        std::vector<double> p1;
        for (int r = 0; r < kDecodeRuns; ++r) {
            const auto t0 = std::chrono::steady_clock::now();
            AdapterFacts f2 = buildAdapterFacts(score, id, {});
            const auto t1 = std::chrono::steady_clock::now();
            p1.push_back(std::chrono::duration<double, std::milli>(t1 - t0).count());
            (void)f2;
        }

        // phase 2 — embedded load (timed; also the objects the decode needs).
        std::vector<double> p2;
        JointTables tables = JointTables::loadEmbedded("all");
        WeightVector selected = selectedWeights();
        FittedAdapter adapter = FittedAdapter::loadEmbedded(selected);
        for (int r = 0; r < kDecodeRuns; ++r) {
            const auto t0 = std::chrono::steady_clock::now();
            JointTables t2 = JointTables::loadEmbedded("all");
            Vocabulary v2(t2);
            WeightVector w2 = selectedWeights();
            FittedAdapter a2 = FittedAdapter::loadEmbedded(w2);
            const auto t1 = std::chrono::steady_clock::now();
            p2.push_back(std::chrono::duration<double, std::milli>(t1 - t0).count());
            (void)v2; (void)a2;
        }
        Vocabulary vocab(tables);

        // phase 3 — decodePiece. Peak resident memory captured around it. Fewer runs on big scores is
        // not needed: we median kDecodeRuns; on a huge score even one run dominates. The cap protects us.
        std::vector<double> p3;
        const size_t wsBeforeDecode = currentWorkingSetBytes();
        DecodeResult dr;
        for (int r = 0; r < kDecodeRuns; ++r) {
            ChordCache cache;
            const auto t0 = std::chrono::steady_clock::now();
            dr = decodePiece(fx.piece, adapter, vocab, cache, 4, fx.sigFifths, fx.declaredMode);
            const auto t1 = std::chrono::steady_clock::now();
            p3.push_back(std::chrono::duration<double, std::milli>(t1 - t0).count());
        }
        const size_t wsAfterDecode = currentWorkingSetBytes();

        // phase 4 — assembleNotationRecord, and the ISOLATED §3.3 posterior slice (computePosteriorSlice).
        std::vector<double> p4, p4slice;
        for (int r = 0; r < kDecodeRuns; ++r) {
            ChordCache cache;
            const auto t0 = std::chrono::steady_clock::now();
            NotationRecord rec = assembleNotationRecord(fx.piece, dr, fx.sigFifths, fx.declaredMode,
                                                        adapter, vocab, cache);
            const auto t1 = std::chrono::steady_clock::now();
            p4.push_back(std::chrono::duration<double, std::milli>(t1 - t0).count());
            (void)rec;
        }
        for (int r = 0; r < kDecodeRuns; ++r) {
            ChordCache cache;
            const auto t0 = std::chrono::steady_clock::now();
            std::vector<SegmentSlice> slices = computePosteriorSlice(fx.piece, dr.segments, adapter,
                                                                     vocab, cache);
            const auto t1 = std::chrono::steady_clock::now();
            p4slice.push_back(std::chrono::duration<double, std::milli>(t1 - t0).count());
            (void)slices;
        }

        o["nSegments"] = static_cast<int>(dr.segments.size());
        o["decodeComplete"] = dr.complete;   // segs=0 diagnosis: false => the DP reached no full-coverage path
        o["phase1_build_facts_ms"] = medOf(p1);
        o["phase2_load_tables_ms"] = medOf(p2);
        o["phase3_decode_ms"] = medOf(p3);
        o["phase4_assemble_ms"] = medOf(p4);
        o["phase4_posterior_slice_ms"] = medOf(p4slice);
        o["ws_base_bytes"] = static_cast<double>(wsBase);
        o["ws_before_decode_bytes"] = static_cast<double>(wsBeforeDecode);
        o["ws_after_decode_bytes"] = static_cast<double>(wsAfterDecode);
        o["ws_decode_growth_bytes"] = static_cast<double>(
            wsAfterDecode > wsBeforeDecode ? wsAfterDecode - wsBeforeDecode : 0);
        o["peak_ws_bytes"] = static_cast<double>(peakWorkingSetBytes());
        scoresArr.append(o);

        std::cout << "[decode] " << id << " events=" << nEvents << " notes=" << nNotes
                  << " segs=" << dr.segments.size()
                  << " p1=" << medOf(p1) << " p2=" << medOf(p2) << " p3=" << medOf(p3)
                  << " p4=" << medOf(p4) << " slice=" << medOf(p4slice)
                  << " peakWS_MB=" << (peakWorkingSetBytes() / (1024.0 * 1024.0)) << "\n";
        delete score;
    };

    for (const PerfScore& ps : kPerfCorpus) {
        runOne(ps.id, ps.sizeClass, QString::fromUtf8(ps.relativePath));
    }
    for (const LargeScore& ls : kLargeCorpus) {
        runOne(ls.id, "", QString::fromUtf8(ls.relPath));
    }

    QJsonObject root;
    root["instrument"] = QStringLiteral("pipeline_snapshot_tests.cpp LargeScoreDecodeProfile.DISABLED_Sweep");
    root["open_item"] = QStringLiteral("OI-206 / cc_instruction_analysis_cost_profile.md Task 1/2");
    root["purpose"] = QStringLiteral(
        "The full produceNotationRecord phase profile: phase 1 buildAdapterFacts, phase 2 embedded "
        "table/weight load, phase 3 decodePiece, phase 4 assembleNotationRecord (+ the isolated §3.3 "
        "computePosteriorSlice), with peak resident memory around the decode. LARGE_PROFILE_MAX_EVENTS "
        "caps which scores are decoded (larger = counts-only, extrapolated).");
    root["cap_events"] = static_cast<double>(capEvents);
    root["runs_per_score"] = kDecodeRuns;
    root["seg_cap"] = 4;
    root["machine"] = QSysInfo::prettyProductName() + QStringLiteral(" / ")
                      + QSysInfo::currentCpuArchitecture();
    root["unit"] = QStringLiteral("milliseconds wall (std::chrono::steady_clock), median of runs; bytes for memory");
    root["scores"] = scoresArr;

    const QString outPath = QStringLiteral(PIPELINE_SNAPSHOT_CORPUS_ROOT)
                            + QStringLiteral("/tools/notation_seams/large_score_decode_profile.json");
    QDir().mkpath(QFileInfo(outPath).absolutePath());
    const QByteArray bytes = serializeSnapshot(root).toUtf8();
    QFile out(outPath);
    ASSERT_TRUE(out.open(QIODevice::WriteOnly | QIODevice::Truncate)) << out.errorString().toStdString();
    ASSERT_EQ(out.write(bytes), static_cast<qint64>(bytes.size()));
    out.close();
    std::cout << "wrote " << outPath.toStdString() << std::endl;
    if (analysisCfg) { analysisCfg->setUseJointNotationRecord(false); }
}

// ── Stage 3.1b byte-identity A/B (uncached window vs cached window) ───────────
//
// After Q1 was re-decided to the bounded-window cache (it memoizes the per-window
// section build inside the unchanged expanding-window path), this harness PROVES
// byte-identity: for every chord-bearing tick it compares
//   • UNCACHED = analyzeHarmonicContextAtTickUncachedForTesting (cache bypassed)
//   • CACHED   = analyzeHarmonicContextAtTick                   (production, memoized)
// and asserts ZERO differing ticks (root/quality/bass/key). Any diff is a hard
// failure — the memoization is not pure. (The pre-revision whole-score answer-delta
// — the large diff this used to measure — is preserved in
// docs/p3_granularity_ab_3_1b.md.)
std::string formatDouble(double v, int decimals);   // defined below (DivergenceC section)

struct DisplayedIdentity {
    bool empty = true;
    int rootPc = -1;
    int quality = -1;
    int bassPc = -1;
    int extensions = 0;
    int keyFifths = 0;
    int keyMode = -1;
    bool wasRegional = true;
};

DisplayedIdentity displayedOf(const NoteHarmonicContext& ctx)
{
    DisplayedIdentity d;
    d.keyFifths = ctx.keyFifths;
    d.keyMode = static_cast<int>(ctx.keyMode);
    d.wasRegional = ctx.wasRegional;
    if (ctx.chordResults.empty()) {
        return d;
    }
    const auto& id = ctx.chordResults.front().identity;
    d.empty = false;
    d.rootPc = id.rootPc;
    d.quality = static_cast<int>(id.quality);
    d.bassPc = id.bassPc;
    d.extensions = id.extensions;
    return d;
}

std::string symbolOf(const mu::engraving::Score* score, const NoteHarmonicContext& ctx)
{
    if (ctx.chordResults.empty()) {
        return "<none>";
    }
    return mu::notation::formatChordResultForStatusBar(score, ctx.chordResults.front(), ctx.keyFifths).symbol;
}

TEST(Stage31bAnswerDelta, DISABLED_Sweep)
{
    auto analysisCfg = muse::modularity::globalIoc()->resolve<
        mu::composing::IComposingAnalysisConfiguration>("composing");
    if (analysisCfg) {
        analysisCfg->setUseRegionalAccumulation(true);
    }

    std::ostringstream report;
    report << "\n==== ANSWERDELTA BEGIN ====\n";

    for (const PerfScore& ps : kPerfCorpus) {
        const QString scorePath = perfCorpusPath(ps);
        ASSERT_TRUE(QFileInfo::exists(scorePath))
            << "Perf corpus score missing: " << scorePath.toStdString();

        MasterScore* score = ScoreRW::readScore(muse::String::fromQString(scorePath),
                                                 /*isAbsolutePath=*/true);
        ASSERT_TRUE(score) << "Failed to load: " << scorePath.toStdString();

        const std::vector<int> ticks = collectChordBearingTicks(score);

        int rootDiff = 0, qualDiff = 0, bassDiff = 0, keyDiff = 0;
        int oldEmpty = 0, newEmpty = 0;
        int oldP4 = 0, newP4 = 0;
        std::ostringstream rows;

        mu::notation::clearHarmonicDecodeCacheForTesting();
        for (int t : ticks) {
            const Fraction frac = Fraction::fromTicks(t);
            // UNCACHED reference (cache bypassed) vs CACHED production path.
            const NoteHarmonicContext oldCtx = mu::notation::analyzeHarmonicContextAtTickUncachedForTesting(score, frac);
            const NoteHarmonicContext newCtx = mu::notation::analyzeHarmonicContextAtTick(score, frac);

            const DisplayedIdentity o = displayedOf(oldCtx);
            const DisplayedIdentity n = displayedOf(newCtx);
            if (o.empty) ++oldEmpty;
            if (n.empty) ++newEmpty;
            if (!o.wasRegional) ++oldP4;
            if (!n.wasRegional) ++newP4;

            const bool rDiff = (o.empty != n.empty) || (o.rootPc != n.rootPc);
            const bool qDiff = (o.empty != n.empty) || (o.quality != n.quality) || (o.extensions != n.extensions);
            const bool bDiff = (o.empty != n.empty) || (o.bassPc != n.bassPc);
            const bool kDiff = (o.keyFifths != n.keyFifths) || (o.keyMode != n.keyMode);
            if (rDiff) ++rootDiff;
            if (qDiff) ++qualDiff;
            if (bDiff) ++bassDiff;
            if (kDiff) ++keyDiff;

            if (rDiff) {
                Measure* m = score->tick2measure(frac);
                const int mn = m ? (m->measureNumber() + 1) : -1;
                const int beatTicks = m ? (t - m->tick().ticks()) : 0;
                const double beat = 1.0 + static_cast<double>(beatTicks) / static_cast<double>(Constants::DIVISION);
                rows << "  ROOTDIFF tick=" << t << " m=" << mn << " beat=" << formatDouble(beat, 2)
                     << " | old=\"" << symbolOf(score, oldCtx) << "\" (regional=" << (o.wasRegional ? 1 : 0) << ")"
                     << " | new=\"" << symbolOf(score, newCtx) << "\" (regional=" << (n.wasRegional ? 1 : 0) << ")"
                     << " | oldKeyF=" << o.keyFifths << " newKeyF=" << n.keyFifths
                     << "\n";
            }
        }

        report << "score=" << ps.id
               << " ticks=" << ticks.size()
               << " rootDiff=" << rootDiff
               << " qualDiff=" << qualDiff
               << " bassDiff=" << bassDiff
               << " keyDiff=" << keyDiff
               << " oldEmpty=" << oldEmpty
               << " newEmpty=" << newEmpty
               << " oldP4=" << oldP4
               << " newP4=" << newP4
               << "\n";
        report << rows.str();

        // Byte-identity gate: the memoization must change nothing.
        EXPECT_EQ(rootDiff, 0) << ps.id << " root drift (cache not pure)";
        EXPECT_EQ(qualDiff, 0) << ps.id << " quality drift";
        EXPECT_EQ(bassDiff, 0) << ps.id << " bass drift";
        EXPECT_EQ(keyDiff, 0)  << ps.id << " key drift";

        delete score;
    }

    report << "==== ANSWERDELTA END ====\n";
    std::cout << report.str() << std::endl;
}

// ── Stage 3.1b cold-vs-warm perf (bounded-window decode-once payoff) ──────────
//
// The bounded-window cache memoizes the per-window section build. Its warm win is
// LOCAL: re-clicking a tick (or clicking within an already-touched measure) hits the
// cached window sections; the cross-measure warm win of the shelved whole-score
// variant is deliberately forfeited (the cost of byte-identity). This harness
// reports, per score:
//   • COLD per-click: clear cache, time a single first query (≈ today's baseline,
//     no regression) — median over a spread of sample ticks.
//   • WARM re-click: each tick queried once to populate, then immediately re-queried
//     and timed — the realistic "click the same note again" / "click a neighbour"
//     latency, served from the cache.
TEST(Stage31bPerf, DISABLED_ColdWarm)
{
    auto analysisCfg = muse::modularity::globalIoc()->resolve<
        mu::composing::IComposingAnalysisConfiguration>("composing");
    if (analysisCfg) {
        analysisCfg->setUseRegionalAccumulation(true);
    }

    std::ostringstream report;
    report << "\n==== COLDWARM BEGIN ====\n";

    for (const PerfScore& ps : kPerfCorpus) {
        const QString scorePath = perfCorpusPath(ps);
        ASSERT_TRUE(QFileInfo::exists(scorePath));
        MasterScore* score = ScoreRW::readScore(muse::String::fromQString(scorePath),
                                                 /*isAbsolutePath=*/true);
        ASSERT_TRUE(score);

        const std::vector<int> ticks = collectChordBearingTicks(score);
        ASSERT_FALSE(ticks.empty());

        // COLD per-click: clear the cache before each sample query so every timed
        // click pays a fresh window build (≈ today's uncached cost). Sample ~30
        // ticks spread across the score.
        std::vector<double> coldLat;
        const int stride = std::max<int>(1, static_cast<int>(ticks.size()) / 30);
        for (size_t i = 0; i < ticks.size(); i += static_cast<size_t>(stride)) {
            mu::notation::clearHarmonicDecodeCacheForTesting();
            const auto c0 = std::chrono::steady_clock::now();
            mu::notation::analyzeHarmonicContextAtTick(score, Fraction::fromTicks(ticks[i]));
            const auto c1 = std::chrono::steady_clock::now();
            coldLat.push_back(std::chrono::duration<double, std::milli>(c1 - c0).count());
        }

        // WARM re-click: populate then immediately re-query the SAME tick (its
        // windows are at the MRU front → all hits).
        std::vector<double> warmLat;
        warmLat.reserve(ticks.size());
        mu::notation::clearHarmonicDecodeCacheForTesting();
        for (int t : ticks) {
            mu::notation::analyzeHarmonicContextAtTick(score, Fraction::fromTicks(t)); // populate
            const auto t0 = std::chrono::steady_clock::now();
            mu::notation::analyzeHarmonicContextAtTick(score, Fraction::fromTicks(t)); // warm re-click
            const auto t1 = std::chrono::steady_clock::now();
            warmLat.push_back(std::chrono::duration<double, std::milli>(t1 - t0).count());
        }

        report << "score=" << ps.id
               << " queries=" << ticks.size()
               << " coldMedianMs=" << formatDouble(medianSorted(coldLat), 3)
               << " coldP95Ms=" << formatDouble(percentileNearestRank(coldLat, 95.0), 3)
               << " warmMedianMs=" << formatDouble(medianSorted(warmLat), 5)
               << " warmP95Ms=" << formatDouble(percentileNearestRank(warmLat, 95.0), 5)
               << " warmMaxMs=" << formatDouble(*std::max_element(warmLat.begin(), warmLat.end()), 5)
               << "\n";

        delete score;
    }

    report << "==== COLDWARM END ====\n";
    std::cout << report.str() << std::endl;
}

// ── Divergence-C observation report (Phase 3b) ───────────────────────────────
//
// One-shot diagnostic gated by the env var PIPELINE_OBSERVE_DIVERGENCE_C=1.
// Generates docs/divergence_c_observation.md by enumerating, per corpus
// score, the regions shorter than 0.5 beats — exactly the regions the
// implode and tick-regional paths surface but addHarmonicAnnotationsToSelection
// silently drops via the minimumDisplayDurationBeats gate.
//
// Not part of the regular CI assertion set: this is a snapshot of corpus
// state at a point in time, not a regression target.  See
// docs/unified_analysis_pipeline.md §"Divergence resolution" for the
// follow-up decision the report informs.

bool shouldObserveDivergenceC()
{
    return qEnvironmentVariableIsSet("PIPELINE_OBSERVE_DIVERGENCE_C");
}

struct SubBeatRegionRow {
    int measureNumber = 0;       // 1-based.
    double beatPosition = 0.0;   // 1-based; e.g. "2.5" = halfway through beat 2.
    double durationBeats = 0.0;
    std::string symbolText;
    std::string romanText;
};

// Same logic as emitHarmonicAnnotations (notationcomposingbridge.cpp): start
// from formatChordResultForStatusBar, then refine the Roman numeral when the
// chord came back Unknown but the key context yields a usable degree.
void computeWouldBeAnnotationText(const mu::engraving::Score* score,
                                   const mu::composing::analysis::AnalyzedRegion& region,
                                   std::string& outSymbol,
                                   std::string& outRoman)
{
    using namespace mu::composing::analysis;

    const int keyFifths = region.keyModeResult.keySignatureFifths;
    const auto& result = region.chordResult;
    const auto fmt = mu::notation::formatChordResultForStatusBar(score, result, keyFifths);
    outSymbol = fmt.symbol;
    outRoman  = fmt.roman;

    if (outRoman.empty()
        && result.identity.quality == ChordQuality::Unknown
        && result.function.degree >= 0
        && result.function.degree <= 6) {
        ChordAnalysisResult refined = result;
        mu::notation::internal::forceChordTrackQualityFromKeyContext(
            refined, region.keyModeResult.mode);
        if (refined.identity.quality != ChordQuality::Unknown) {
            outRoman = ChordSymbolFormatter::formatRomanNumeral(refined);
        }
    }
}

std::vector<SubBeatRegionRow> collectSubBeatRegions(MasterScore* score,
                                                     const mu::composing::analysis::AnalyzedSection& section)
{
    std::vector<SubBeatRegionRow> rows;
    constexpr int kHalfBeatTicks = Constants::DIVISION / 2;  // 0.5 beats
    for (const auto& region : section.regions) {
        const int durationTicks = region.endTick - region.startTick;
        if (durationTicks <= 0 || durationTicks >= kHalfBeatTicks) {
            continue;
        }

        const Fraction startFrac = Fraction::fromTicks(region.startTick);
        Measure* m = score->tick2measure(startFrac);
        if (!m) {
            continue;
        }
        const int tickInMeasure = region.startTick - m->tick().ticks();

        SubBeatRegionRow row;
        row.measureNumber = m->measureNumber() + 1;  // measureNumber() is 0-based.
        row.beatPosition  = 1.0 + static_cast<double>(tickInMeasure) / static_cast<double>(Constants::DIVISION);
        row.durationBeats = static_cast<double>(durationTicks) / static_cast<double>(Constants::DIVISION);
        computeWouldBeAnnotationText(score, region, row.symbolText, row.romanText);
        rows.push_back(std::move(row));
    }
    return rows;
}

std::string formatDouble(double v, int decimals)
{
    std::ostringstream os;
    os.setf(std::ios::fixed);
    os.precision(decimals);
    os << v;
    return os.str();
}

TEST(PipelineDivergenceCObservation, GenerateReport)
{
    if (!shouldObserveDivergenceC()) {
        GTEST_SKIP() << "Set PIPELINE_OBSERVE_DIVERGENCE_C=1 to regenerate "
                        "docs/divergence_c_observation.md.";
    }

    auto analysisCfg = muse::modularity::globalIoc()->resolve<
        mu::composing::IComposingAnalysisConfiguration>("composing");
    if (analysisCfg) {
        analysisCfg->setUseRegionalAccumulation(true);
    }

    struct PerScore {
        const CorpusEntry* entry;
        int totalRegions = 0;
        std::vector<SubBeatRegionRow> rows;
    };
    std::vector<PerScore> perScore;
    perScore.reserve(std::size(kCorpus));

    for (const CorpusEntry& entry : kCorpus) {
        const QString scorePath = corpusPath(entry);
        ASSERT_TRUE(QFileInfo::exists(scorePath))
            << "Corpus score missing on disk: " << scorePath.toStdString();

        MasterScore* score = ScoreRW::readScore(muse::String::fromQString(scorePath),
                                                 /*isAbsolutePath=*/true);
        ASSERT_TRUE(score) << "Failed to load corpus score: " << scorePath.toStdString();

        const Fraction cappedEnd = endTickForMeasureCap(score, kMaxAnalysisMeasures);

        const auto rawRegions = mu::notation::analyzeHarmonicRhythm(
            score, Fraction(0, 1), cappedEnd, /*excludeStaves=*/{},
            mu::notation::HarmonicRegionGranularity::Smoothed);
        const auto section = mu::composing::analysis::analyzeSection(
            score, Fraction(0, 1), cappedEnd, /*excludeStaves=*/{}, rawRegions);

        PerScore p;
        p.entry         = &entry;
        p.totalRegions  = static_cast<int>(section.regions.size());
        p.rows          = collectSubBeatRegions(score, section);
        perScore.push_back(std::move(p));

        delete score;
    }

    // Build the markdown report.
    std::ostringstream md;
    md << "# Divergence C \xE2\x80\x94 Observation Report\n\n"
       << "Generated by `pipeline_snapshot_tests` "
          "(`PIPELINE_OBSERVE_DIVERGENCE_C=1`).\n"
       << "Per-score enumeration of sub-beat (< 0.5 beat) regions that "
          "implode and tick-regional surface but annotation silently drops via "
          "the `minimumDisplayDurationBeats` gate.\n\n"
       << "Window: first " << kMaxAnalysisMeasures
       << " measures of each corpus score (matches the snapshot harness).\n"
       << "Beat position is 1-based within the containing measure; a value "
          "of 2.5 means halfway through beat 2.\n\n"
       << "## Summary\n\n"
       << "| Score | Total regions | Sub-beat regions (delta set) |\n"
       << "|---|---:|---:|\n";

    int grandTotalDelta = 0;
    for (const auto& p : perScore) {
        md << "| " << p.entry->id
           << " | " << p.totalRegions
           << " | " << p.rows.size() << " |\n";
        grandTotalDelta += static_cast<int>(p.rows.size());
    }
    md << "\nTotal delta-set regions across the corpus: **"
       << grandTotalDelta << "**.\n\n";

    md << "## Per-score detail\n\n";
    for (const auto& p : perScore) {
        md << "### " << p.entry->id << "\n\n";
        md << "_" << p.entry->description << "_\n\n";
        if (p.rows.empty()) {
            md << "No sub-beat regions in the analysed window.\n\n";
            continue;
        }
        md << "| Measure | Beat | Duration (beats) | Would-be symbol | Would-be Roman |\n";
        md << "|---:|---:|---:|---|---|\n";
        for (const auto& row : p.rows) {
            md << "| " << row.measureNumber
               << " | " << formatDouble(row.beatPosition, 3)
               << " | " << formatDouble(row.durationBeats, 3)
               << " | " << (row.symbolText.empty() ? "_(none)_" : row.symbolText)
               << " | " << (row.romanText.empty()  ? "_(none)_" : row.romanText)
               << " |\n";
        }
        md << "\n";
    }

    const QString docsDir = QStringLiteral(PIPELINE_SNAPSHOT_DOCS_DIR);
    const QString outPath = docsDir + QStringLiteral("/divergence_c_observation.md");
    QFile file(outPath);
    ASSERT_TRUE(file.open(QIODevice::WriteOnly | QIODevice::Truncate))
        << "Failed to open " << outPath.toStdString()
        << ": " << file.errorString().toStdString();
    const QByteArray bytes = QByteArray::fromStdString(md.str());
    const qint64 written = file.write(bytes);
    file.close();
    ASSERT_EQ(written, bytes.size())
        << "Short write to " << outPath.toStdString();
}

// ── Seams part 2, P6 — the DUAL-ARM classified-comparison CAPTURE ─────────────
//
// Emits tools/notation_seams/dualarm_capture.json — the two arms' FULL notation output surface over
// the snapshot corpus, the input to the classified diff (tools/notation_seams/classify_dualarm.py) that
// is the §8.4 switch-ratification evidence. For each corpus score, over the 16-measure golden window,
// each of the FOUR audited output surfaces is captured TWICE — arm "legacy" (useJointNotationRecord OFF)
// and arm "record" (ON):
//   * annotation — the span-seam write (addHarmonicAnnotationsToSelection, sym+roman+nashville): the
//     written Harmony elements (STANDARD display symbol / ROMAN numeral / key bracket / NASHVILLE) and
//     the StaffText annotations (pedal "X ped.", any cadence label);
//   * implode    — the chord-track write (populateChordTrack): the treble display symbols, the bass
//     Roman/Nashville, the imploded voicing pitches, and the chord-staff key/cadence StaffText;
//   * tuning     — applyRegionTuning under a fixed Just-Intonation tonic-anchored config: per-note
//     tuning offsets (cents) — a downstream read of the committed rootPc+key;
//   * noteSeam   — analyzeHarmonicContextAtTick at EVERY MEASURE DOWNBEAT (the declared, deterministic
//     tick sample): the committed reading (rootPc/quality/key), its rendered symbol/roman/nashville
//     (the shared status-bar formatter), and its §3.3 ranked alternatives.
//
// MEASUREMENT-ONLY and OPT-IN (DISABLED_ — the DISABLED_SeamsGapMeasurement precedent): it never runs
// in the default sweep, so the golden comparison and byte-identity are untouched. It calls ONLY the
// public production entry points the notation path already uses; no production code is instrumented.
// The record arm re-decodes the whole score per surface (the OI-203 deferred latency; irrelevant to an
// output comparison). DETERMINISTIC: each surface array is sorted by a stable key, and both arms are
// deterministic decodes — two runs are byte-identical (proven by re-running and diffing the artifact).
// The flag is restored OFF by RAII scope after every surface. Run with:
//
//   ./pipeline_snapshot_tests.exe \
//       --gtest_also_run_disabled_tests \
//       --gtest_filter='*DualArmClassifiedCapture*'

// RAII: turn the record arm ON for one captured surface and restore it OFF on scope exit — so a throw
// or early return cannot leak the flag into the next surface (which must be captured on the arm it names).
struct ScopedJointRecordArm {
    mu::composing::IComposingAnalysisConfiguration* cfg = nullptr;
    explicit ScopedJointRecordArm(bool on)
    {
        auto shared = muse::modularity::globalIoc()->resolve<
            mu::composing::IComposingAnalysisConfiguration>("composing");
        cfg = shared.get();
        if (cfg) {
            cfg->setUseJointNotationRecord(on);
        }
    }
    ~ScopedJointRecordArm()
    {
        if (cfg) {
            cfg->setUseJointNotationRecord(false);
        }
    }
};

MasterScore* loadCorpusScore(const CorpusEntry& entry)
{
    const QString p = corpusPath(entry);
    if (!QFileInfo::exists(p)) {
        return nullptr;
    }
    return ScoreRW::readScore(muse::String::fromQString(p), /*isAbsolutePath=*/true);
}

// Deterministic tuning config for the tuning-surface capture: Just Intonation, tonic-anchored, NO
// sustained-event splitting (so both arms keep the identical note structure and the offsets align by
// (tick, staff, pitch) — a pure value comparison). Mirrors notationtuning_tests.cpp::configureTuning.
void configureTuningForCapture()
{
    auto cfg = muse::modularity::globalIoc()->resolve<
        mu::composing::IComposingAnalysisConfiguration>("composing");
    if (!cfg) {
        return;
    }
    cfg->setTuningSystemKey("just");
    cfg->setTonicAnchoredTuning(true);
    cfg->setTuningMode(mu::composing::intonation::TuningMode::TonicAnchored);
    cfg->setAllowSplitSlurOfSustainedEvents(false);
    cfg->setMinimizeTuningDeviation(false);
    cfg->setAnnotateTuningOffsets(false);
    cfg->setAnnotateDriftAtBoundaries(false);
    cfg->setUseRegionalAccumulation(true);
}

// A captured output item + its deterministic sort key. Sorting guarantees run-to-run byte-identity even
// if a segment's annotation list order ever drifts.
struct CapturedItem {
    QString key;
    QJsonObject obj;
};
QString itemKey(int tick, int staff, const QString& kind, const QString& text)
{
    return QStringLiteral("%1|%2|%3|%4")
        .arg(tick, 8, 10, QLatin1Char('0')).arg(staff, 3, 10, QLatin1Char('0')).arg(kind, text);
}
QJsonArray sortedItems(std::vector<CapturedItem>& items)
{
    std::sort(items.begin(), items.end(),
              [](const CapturedItem& a, const CapturedItem& b) { return a.key < b.key; });
    QJsonArray arr;
    for (const CapturedItem& it : items) {
        arr.append(it.obj);
    }
    return arr;
}

// Classify a written Harmony by type (+ the ROMAN key-bracket "[...]" sub-case).
QString harmonyKind(const Harmony* h, const QString& text)
{
    switch (h->harmonyType()) {
    case HarmonyType::STANDARD:  return QStringLiteral("symbol");
    case HarmonyType::ROMAN:     return (!text.isEmpty() && text.front() == QLatin1Char('['))
                                        ? QStringLiteral("keyBracket") : QStringLiteral("roman");
    case HarmonyType::NASHVILLE: return QStringLiteral("nashville");
    default:                     return QStringLiteral("harmonyOther");
    }
}
QString harmonyText(const Harmony* h)
{
    QString t = h->harmonyName().toQString();
    if (t.isEmpty()) {
        t = h->plainText().toQString();
    }
    return t;
}

std::vector<mu::engraving::EngravingItem*> collectStaffTexts(MasterScore* score, const Fraction& endTick)
{
    std::vector<mu::engraving::EngravingItem*> out;
    for (Segment* seg = score->firstSegment(SegmentType::ChordRest); seg && seg->tick() < endTick;
         seg = seg->next1(SegmentType::ChordRest)) {
        for (mu::engraving::EngravingItem* ann : seg->annotations()) {
            if (ann && ann->isStaffText()) {
                out.push_back(ann);
            }
        }
    }
    return out;
}

// ── surface 1: the span-seam annotation write ────────────────────────────────
QJsonArray captureAnnotationSurface(const CorpusEntry& entry, bool useRecord)
{
    std::vector<CapturedItem> items;
    MasterScore* score = loadCorpusScore(entry);
    if (!score) {
        return QJsonArray();
    }
    const Fraction endTick = endTickForMeasureCap(score, kMaxAnalysisMeasures);
    Segment* startSeg = score->firstSegment(SegmentType::ChordRest);
    if (!startSeg || score->nstaves() == 0) {
        delete score;
        return QJsonArray();
    }

    // pre-existing elements (the DCML source ships Roman numerals + staff texts) — captured by pointer
    // identity so only OUR writes are recorded.
    const auto beforeH = collectExistingHarmonies(score, endTick);
    std::vector<Harmony*> preH;
    for (const auto& e : beforeH) {
        preH.push_back(e.harmony);
    }
    const auto beforeT = collectStaffTexts(score, endTick);

    Segment* endSeg = segmentAtOrAfter(score, endTick);
    score->selection().setRange(startSeg, endSeg, /*staffStart=*/0, /*staffEnd=*/score->nstaves());
    if (!score->selection().isRange()) {
        delete score;
        return QJsonArray();
    }
    {
        ScopedJointRecordArm arm(useRecord);
        mu::notation::addHarmonicAnnotationsToSelection(score, /*sym=*/true, /*roman=*/true, /*nash=*/true);
    }

    for (const auto& e : collectExistingHarmonies(score, endTick)) {
        if (std::find(preH.begin(), preH.end(), e.harmony) != preH.end()) {
            continue;
        }
        const int tick = e.segment->tick().ticks();
        const int staff = static_cast<int>(mu::engraving::track2staff(e.harmony->track()));
        const QString text = harmonyText(e.harmony);
        const QString kind = harmonyKind(e.harmony, text);
        QJsonObject o;
        o[QStringLiteral("tick")] = tick;
        o[QStringLiteral("staff")] = staff;
        o[QStringLiteral("kind")] = kind;
        o[QStringLiteral("text")] = text;
        items.push_back({ itemKey(tick, staff, kind, text), o });
    }
    for (mu::engraving::EngravingItem* ann : collectStaffTexts(score, endTick)) {
        if (std::find(beforeT.begin(), beforeT.end(), ann) != beforeT.end()) {
            continue;
        }
        const int tick = ann->tick().ticks();
        const int staff = static_cast<int>(mu::engraving::track2staff(ann->track()));
        const QString text = mu::engraving::toStaffText(ann)->plainText().toQString();
        QJsonObject o;
        o[QStringLiteral("tick")] = tick;
        o[QStringLiteral("staff")] = staff;
        o[QStringLiteral("kind")] = QStringLiteral("staffText");
        o[QStringLiteral("text")] = text;
        items.push_back({ itemKey(tick, staff, QStringLiteral("staffText"), text), o });
    }
    delete score;
    return sortedItems(items);
}

// ── surface 2: the implode chord-track write ─────────────────────────────────
QJsonArray captureImplodeSurface(const CorpusEntry& entry, bool useRecord)
{
    // comprehensive chord-staff config: symbols + Roman function + key annotations + cadence markers.
    if (auto chordStaffCfg = muse::modularity::globalIoc()->resolve<
            mu::composing::IComposingChordStaffConfiguration>("composing")) {
        chordStaffCfg->setChordStaffWriteChordSymbols(true);
        chordStaffCfg->setChordStaffFunctionNotation("roman");
        chordStaffCfg->setChordStaffWriteKeyAnnotations(true);
        chordStaffCfg->setChordStaffHighlightNonDiatonic(false);
        chordStaffCfg->setChordStaffWriteCadenceMarkers(true);
    }

    std::vector<CapturedItem> items;
    MasterScore* score = loadCorpusScore(entry);
    if (!score) {
        return QJsonArray();
    }
    const Fraction endTick = endTickForMeasureCap(score, kMaxAnalysisMeasures);
    if (score->nstaves() == 0) {
        delete score;
        return QJsonArray();
    }

    const staff_idx_t trebleStaffIdx = appendChordTrackStaffPair(score);
    const track_idx_t trebleTrack = trebleStaffIdx * VOICES;
    const track_idx_t bassTrack   = (trebleStaffIdx + 1) * VOICES;

    bool ok = false;
    {
        ScopedJointRecordArm arm(useRecord);
        score->startCmd(muse::TranslatableString::untranslatable("P6 dual-arm implode capture"));
        ok = mu::notation::populateChordTrack(score, Fraction(0, 1), endTick, trebleStaffIdx);
        score->endCmd();
    }
    if (!ok) {
        delete score;
        return QJsonArray();
    }

    for (Segment* seg = score->firstSegment(SegmentType::ChordRest); seg && seg->tick() < endTick;
         seg = seg->next1(SegmentType::ChordRest)) {
        const int tick = seg->tick().ticks();
        // treble voicing pitches (the imploded chord's notes)
        if (ChordRest* cr = seg->cr(trebleTrack) ? toChordRest(seg->cr(trebleTrack)) : nullptr) {
            if (cr->isChord()) {
                std::vector<int> pitches;
                for (Note* n : toChord(cr)->notes()) {
                    if (n) {
                        pitches.push_back(n->pitch());
                    }
                }
                std::sort(pitches.begin(), pitches.end());
                if (!pitches.empty()) {
                    QJsonArray parr;
                    QString flat;
                    for (int p : pitches) {
                        parr.append(p);
                        flat += QString::number(p) + QLatin1Char(',');
                    }
                    QJsonObject o;
                    o[QStringLiteral("tick")] = tick;
                    o[QStringLiteral("kind")] = QStringLiteral("voicing");
                    o[QStringLiteral("pitches")] = parr;
                    items.push_back({ itemKey(tick, 900, QStringLiteral("voicing"), flat), o });
                }
            }
        }
        // treble + bass harmonies + staff texts
        for (mu::engraving::EngravingItem* ann : seg->annotations()) {
            const track_idx_t t = ann ? ann->track() : 0;
            if (!ann || (t != trebleTrack && t != bassTrack)) {
                continue;
            }
            const QString role = (t == trebleTrack) ? QStringLiteral("treble") : QStringLiteral("bass");
            if (ann->isHarmony()) {
                const Harmony* h = toHarmony(ann);
                const QString text = harmonyText(h);
                const QString kind = role + QLatin1Char(':') + harmonyKind(h, text);
                QJsonObject o;
                o[QStringLiteral("tick")] = tick;
                o[QStringLiteral("kind")] = kind;
                o[QStringLiteral("text")] = text;
                items.push_back({ itemKey(tick, (t == trebleTrack) ? 0 : 1, kind, text), o });
            } else if (ann->isStaffText()) {
                const QString text = mu::engraving::toStaffText(ann)->plainText().toQString();
                const QString kind = role + QStringLiteral(":staffText");
                QJsonObject o;
                o[QStringLiteral("tick")] = tick;
                o[QStringLiteral("kind")] = kind;
                o[QStringLiteral("text")] = text;
                items.push_back({ itemKey(tick, (t == trebleTrack) ? 0 : 1, kind, text), o });
            }
        }
    }
    delete score;
    return sortedItems(items);
}

// ── surface 3: per-note tuning offsets ───────────────────────────────────────
QJsonArray captureTuningSurface(const CorpusEntry& entry, bool useRecord)
{
    configureTuningForCapture();
    std::vector<CapturedItem> items;
    MasterScore* score = loadCorpusScore(entry);
    if (!score) {
        return QJsonArray();
    }
    const Fraction endTick = endTickForMeasureCap(score, kMaxAnalysisMeasures);
    {
        ScopedJointRecordArm arm(useRecord);
        score->startCmd(muse::TranslatableString::untranslatable("P6 dual-arm tuning capture"));
        mu::notation::applyRegionTuning(score, Fraction(0, 1), endTick);
        score->endCmd();
    }
    for (Segment* seg = score->firstSegment(SegmentType::ChordRest); seg && seg->tick() < endTick;
         seg = seg->next1(SegmentType::ChordRest)) {
        const int tick = seg->tick().ticks();
        for (track_idx_t t = 0; t < score->ntracks(); ++t) {
            ChordRest* cr = seg->cr(t);
            if (!cr || !cr->isChord()) {
                continue;
            }
            const int staff = static_cast<int>(mu::engraving::track2staff(t));
            for (Note* n : toChord(cr)->notes()) {
                if (!n) {
                    continue;
                }
                const double cents = std::round(n->tuning() * 1000.0) / 1000.0;
                QJsonObject o;
                o[QStringLiteral("tick")] = tick;
                o[QStringLiteral("staff")] = staff;
                o[QStringLiteral("pitch")] = n->pitch();
                o[QStringLiteral("cents")] = cents;
                items.push_back({ itemKey(tick, staff, QStringLiteral("t"), QString::number(n->pitch())), o });
            }
        }
    }
    delete score;
    return sortedItems(items);
}

// ── surface 4: the note-seam answers at every measure downbeat ───────────────
QJsonArray captureNoteSeamSurface(const CorpusEntry& entry, bool useRecord)
{
    QJsonArray arr;
    MasterScore* score = loadCorpusScore(entry);
    if (!score) {
        return arr;
    }
    const auto samples = collectSampleTicks(score, kMaxAnalysisMeasures);
    ScopedJointRecordArm arm(useRecord);   // ON for the whole read-only sweep; restored OFF on return
    for (const SampleTick& s : samples) {
        if (s.isMidMeasure) {
            continue;   // the declared sample is every measure DOWNBEAT
        }
        const Fraction t = Fraction::fromTicks(s.tickValue);
        const NoteHarmonicContext ctx = mu::notation::analyzeHarmonicContextAtTick(score, t);
        QJsonObject o;
        o[QStringLiteral("tick")] = s.tickValue;
        o[QStringLiteral("measure")] = s.measureNumber;
        if (ctx.chordResults.empty()) {
            o[QStringLiteral("rootPc")] = -1;
            o[QStringLiteral("quality")] = QStringLiteral("");
            o[QStringLiteral("symbol")] = QStringLiteral("");
            o[QStringLiteral("roman")] = QStringLiteral("");
            o[QStringLiteral("nashville")] = QStringLiteral("");
        } else {
            const ChordAnalysisResult& r = ctx.chordResults.front();
            const mu::notation::FormattedChordResult fmt =
                mu::notation::formatChordResultForStatusBar(score, r, ctx.keyFifths);
            o[QStringLiteral("rootPc")] = r.identity.rootPc;
            o[QStringLiteral("quality")] = QString::fromStdString(qualityName(r.identity.quality));
            o[QStringLiteral("symbol")] = QString::fromStdString(fmt.symbol);
            o[QStringLiteral("roman")] = QString::fromStdString(fmt.roman);
            o[QStringLiteral("nashville")] = QString::fromStdString(fmt.nashville);
            QJsonArray alts;
            for (size_t k = 1; k < ctx.chordResults.size(); ++k) {
                const ChordAnalysisResult& a = ctx.chordResults[k];
                QJsonObject ao;
                ao[QStringLiteral("rootPc")] = a.identity.rootPc;
                ao[QStringLiteral("quality")] = QString::fromStdString(qualityName(a.identity.quality));
                ao[QStringLiteral("score")] = std::round(a.identity.score * 1000.0) / 1000.0;
                alts.append(ao);
            }
            o[QStringLiteral("alternatives")] = alts;
        }
        o[QStringLiteral("keyFifths")] = ctx.keyFifths;
        o[QStringLiteral("keyMode")] = QString::fromStdString(modeName(ctx.keyMode));
        arr.append(o);
    }
    delete score;
    return arr;
}

QJsonObject captureArm(const CorpusEntry& entry, bool useRecord)
{
    QJsonObject arm;
    arm[QStringLiteral("annotation")] = captureAnnotationSurface(entry, useRecord);
    arm[QStringLiteral("implode")] = captureImplodeSurface(entry, useRecord);
    arm[QStringLiteral("tuning")] = captureTuningSurface(entry, useRecord);
    arm[QStringLiteral("noteSeam")] = captureNoteSeamSurface(entry, useRecord);
    return arm;
}

TEST(DualArmClassifiedCapture, DISABLED_EmitCapture)
{
    auto analysisCfg = muse::modularity::globalIoc()->resolve<
        mu::composing::IComposingAnalysisConfiguration>("composing");
    ASSERT_TRUE(analysisCfg) << "IComposingAnalysisConfiguration not registered";
    analysisCfg->setUseRegionalAccumulation(true);
    analysisCfg->setUseJointNotationRecord(false);

    QJsonArray corpusArr;
    for (const CorpusEntry& entry : kCorpus) {
        int endTickVal = 0;
        if (MasterScore* s = loadCorpusScore(entry)) {
            endTickVal = endTickForMeasureCap(s, kMaxAnalysisMeasures).ticks();
            delete s;
        }
        QJsonObject scoreObj;
        scoreObj[QStringLiteral("id")] = QString::fromUtf8(entry.id);
        scoreObj[QStringLiteral("analysisEndTick")] = endTickVal;
        scoreObj[QStringLiteral("legacy")] = captureArm(entry, /*useRecord=*/false);
        scoreObj[QStringLiteral("record")] = captureArm(entry, /*useRecord=*/true);
        corpusArr.append(scoreObj);
        std::cout << "[dual-arm capture] " << entry.id << " done" << std::endl;
    }

    QJsonObject root;
    root[QStringLiteral("window")] =
        QStringLiteral("[0, endTickForMeasureCap(kMaxAnalysisMeasures=16)) — the snapshot harness window");
    root[QStringLiteral("arms")] =
        QStringLiteral("legacy = useJointNotationRecord OFF; record = ON. Each surface captured on a fresh score.");
    root[QStringLiteral("surfaces")] = QStringLiteral(
        "annotation (span-seam write) | implode (chord track) | tuning (per-note cents) | noteSeam (downbeats)");
    root[QStringLiteral("corpus")] = corpusArr;

    const QString outPath = QStringLiteral(PIPELINE_SNAPSHOT_CORPUS_ROOT)
                            + QStringLiteral("/tools/notation_seams/dualarm_capture.json");
    QDir().mkpath(QFileInfo(outPath).absolutePath());
    const QByteArray bytes = serializeSnapshot(root).toUtf8();
    QFile out(outPath);
    ASSERT_TRUE(out.open(QIODevice::WriteOnly | QIODevice::Truncate)) << out.errorString().toStdString();
    ASSERT_EQ(out.write(bytes), static_cast<qint64>(bytes.size()));
    out.close();

    analysisCfg->setUseJointNotationRecord(false);   // explicit restore (the RAII already did per surface)
    std::cout << "[dual-arm capture] wrote " << outPath.toStdString() << std::endl;
}

} // namespace
