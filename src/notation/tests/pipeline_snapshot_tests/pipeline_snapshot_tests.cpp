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
#include "engraving/dom/factory.h"
#include "engraving/dom/harmony.h"
#include "engraving/dom/instrument.h"
#include "engraving/dom/masterscore.h"
#include "engraving/dom/measure.h"
#include "engraving/dom/note.h"
#include "engraving/dom/part.h"
#include "engraving/dom/segment.h"
#include "engraving/dom/select.h"
#include "engraving/dom/staff.h"
#include "engraving/types/constants.h"

#include "engraving/tests/utils/scorerw.h"

#include "modularity/ioc.h"

#include "composing/analysis/chord/chordanalyzer.h"
#include "composing/analysis/key/keymodeanalyzer.h"
#include "composing/analyzed_section.h"
#include "composing/icomposinganalysisconfiguration.h"
#include "composing/icomposingchordstaffconfiguration.h"

#include "notation/internal/notationimplodebridge.h"

#include "notation/internal/notationcomposingbridge.h"
#include "notation/internal/notationcomposingbridgehelpers.h"

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
    const auto section = mu::notation::internal::analyzeSection(
        score, Fraction(0, 1), endTick, /*excludeStaves=*/{});
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

    const auto section = mu::notation::internal::analyzeSection(
        score, Fraction(0, 1), cappedEnd, /*excludeStaves=*/{});

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

        const auto section = mu::notation::internal::analyzeSection(
            score, Fraction(0, 1), cappedEnd, /*excludeStaves=*/{});

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

} // namespace
