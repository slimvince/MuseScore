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
#include "engraving/dom/stafftext.h"   // P3a record-arm pedal-suppression check
#include "engraving/types/constants.h"

#include "engraving/tests/utils/scorerw.h"

#include "modularity/ioc.h"

#include "composing/analysis/chord/chordanalyzer.h"
#include "composing/analysis/key/keymodeanalyzer.h"
#include "composing/analysis/section/sectionanalyzer.h"
#include "composing/analysis/joint/jointnotationproducer.h"   // P1 §4.1 gap measurement (record arm)
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

} // namespace
