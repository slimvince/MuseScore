// SPDX-License-Identifier: GPL-3.0-only
// MuseScore-Studio-CLA-applies
//
// llm_triage.cpp — LLM-Triage v0 plain-text format emitter
//
// Loads one score, runs the harmonic analyzer, emits three artifacts:
//   <score>.notes_only.txt      — raw note onsets + durations, no analysis output
//   <score>.with_symbols.txt    — same + printed chord symbol annotations
//   <score>.analyzer_output.txt — our analyzer's per-region results (reference only)
//
// Usage: llm_triage <input_score_path> <output_dir>
//
// No LLM API calls are made in v0.  See docs/llm_triage_design.md.
//
// ── Format decisions (document here for v1 readers) ─────────────────────────
//
// Pitch spelling: TPC-derived names with octave (e.g. F#4, Bb2).  Spelling
//   follows the score's own TPC value so no enharmonic re-spelling occurs.
//   English convention (B = B-natural, Bb = B-flat); no German H/B mapping.
//
// Time format: mN bX.Y where N is 1-indexed measure number and X.Y is the
//   1-indexed beat within the measure in quarter-note units.
//
// Duration: w h q e s(16th) 32 64; dot appended for dotted values (q. h. etc.).
//   Tuplets are not specially labelled in v0 — the fraction renders as-is via
//   the dominant duration type.  Revisit in v1.
//
// Voice/staff: labelled by part name, not RH/LH, to handle scores with >2 staves.
//   Format: staff "<part_name>":
//
// Sustained notes: emitted ONCE at onset with their duration.  Not repeated on
//   subsequent beats — the LLM reads the duration and does its own windowing.
//
// Time-sig changes: emitted as "# Time sig: X/Y" marker at the first segment of
//   the measure where the change takes effect, before the onset line.
//
// Tempo markings: not emitted in v0 (revisit in v1 — TempoText access is
//   non-trivial and the v0 verification score may have no tempo text).
//
// hasAssertiveExposure: not present in the flat-vector AnalyzedRegion returned by
//   analyzeScore() (that field lives on the analyzed_section.h type, not the
//   batch_analyze local struct).  Confidence field is emitted without the
//   "(assertive)" qualifier.  Wire up in v1 when AnalyzedSection is consumed.

#include <algorithm>
#include <chrono>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <memory>
#include <optional>
#include <set>
#include <sstream>
#include <string>
#include <vector>

// ── Qt ─────────────────────────────────────────────────────────────────────
#include <QByteArray>
#include <QCoreApplication>
#include <QCryptographicHash>
#include <QDateTime>
#include <QDir>
#include <QFile>
#include <QFileInfo>
#include <QGuiApplication>
#include <QIODevice>
#include <QJsonArray>
#include <QJsonDocument>
#include <QJsonObject>

#ifdef _WIN32
extern "C" __declspec(dllimport) void* __stdcall GetCurrentProcess(void);
extern "C" __declspec(dllimport) int __stdcall TerminateProcess(void* hProcess, unsigned int uExitCode);
#endif

// ── Muse framework ─────────────────────────────────────────────────────────
#include "global/globalmodule.h"
#include "draw/internal/ifontsdatabase.h"
#include "global/iapplication.h"
#include "global/modularity/imodulesetup.h"
#include "global/io/path.h"
#include "global/types/string.h"
#include "global/types/ret.h"

// ── Draw ───────────────────────────────────────────────────────────────────
#include "draw/drawmodule.h"

// ── Engraving ──────────────────────────────────────────────────────────────
#include "engraving/engravingmodule.h"
#include "engraving/engravingerrors.h"
#include "engraving/dom/masterscore.h"
#include "engraving/dom/measure.h"
#include "engraving/dom/measurebase.h"
#include "engraving/dom/segment.h"
#include "engraving/dom/chord.h"
#include "engraving/dom/chordrest.h"
#include "engraving/dom/note.h"
#include "engraving/dom/staff.h"
#include "engraving/dom/part.h"
#include "engraving/dom/instrument.h"
#include "engraving/dom/keysig.h"
#include "engraving/dom/layoutbreak.h"
#include "engraving/dom/mscore.h"
#include "engraving/dom/pedal.h"
#include "engraving/dom/instrtemplate.h"
#include "engraving/dom/sig.h"
#include "engraving/dom/timesig.h"
#include "engraving/dom/harmony.h"
#include "engraving/dom/pitchspelling.h"
#include "engraving/compat/scoreaccess.h"
#include "engraving/compat/mscxcompat.h"
#include "engraving/infrastructure/localfileinfoprovider.h"
#include "engraving/types/constants.h"
#include "engraving/types/types.h"

// ── MusicXML import ────────────────────────────────────────────────────────
#include "importexport/musicxml/musicxmlmodule.h"
#include "importexport/musicxml/internal/import/importmusicxml.h"

// ── Analysis ───────────────────────────────────────────────────────────────
#include "composing/analysis/chord/chordanalyzer.h"
#include "composing/analysis/key/keymodeanalyzer.h"
#include "composing/analysis/chord/analysisutils.h"

// ── Namespace aliases ──────────────────────────────────────────────────────
using namespace mu::engraving;
namespace analysis = mu::composing::analysis;
using analysis::ChordAnalysisTone;
using analysis::ChordAnalysisResult;
using analysis::ChordQuality;
using analysis::ChordTemporalContext;
using analysis::KeyModeAnalysisResult;

// ══════════════════════════════════════════════════════════════════════════
// Local AnalyzedRegion — mirrors the flat-vector shape from batch_analyze.cpp.
// Does NOT use analyzed_section.h (AnalyzedSection consumption is v1 work).
// ══════════════════════════════════════════════════════════════════════════

struct AnalyzedRegion {
    int startTick = 0;
    int endTick = 0;
    int measureNumber = 0;
    double beat = 1.0;
    ChordAnalysisResult chord;
    bool hasAnalyzedChord = true;
    std::vector<ChordAnalysisResult> alternatives;
    KeyModeAnalysisResult key;
    std::vector<KeyModeAnalysisResult> keyRanked;
    std::vector<ChordAnalysisTone> tones;
    uint16_t pcMask = 0;
    int bassPc = -1;
};

// ══════════════════════════════════════════════════════════════════════════
// Module init — verbatim from tools/batch_analyze.cpp
// ══════════════════════════════════════════════════════════════════════════

static void initModules()
{
    using namespace muse;
    using namespace muse::modularity;

    const IApplication::RunMode mode = IApplication::RunMode::GuiApp;

    static GlobalModule globalModule;
    globalModule.registerResources();
    globalModule.registerExports();
    globalModule.registerUiTypes();

    static draw::DrawModule               drawModule;
    static mu::engraving::EngravingModule engravingModule;
    static mu::iex::musicxml::MusicXmlModule musicXmlModule;

    std::vector<IModuleSetup*> depModules = {
        &drawModule, &engravingModule, &musicXmlModule
    };

    for (auto* m : depModules) {
        m->setApplication(globalModule.application());
        m->registerResources();
    }
    for (auto* m : depModules) {
        m->registerExports();
    }

    globalModule.resolveImports();
    for (auto* m : depModules) {
        m->registerUiTypes();
        m->resolveImports();
    }

    globalModule.onPreInit(mode);
    for (auto* m : depModules) { m->onPreInit(mode); }

    MScore::testMode = true;
    MScore::noGui    = true;

    globalModule.onInit(mode);
    for (auto* m : depModules) { m->onInit(mode); }

    globalModule.onAllInited(mode);
    for (auto* m : depModules) { m->onAllInited(mode); }

    globalModule.onStartApp();
    for (auto* m : depModules) { m->onStartApp(); }

    loadInstrumentTemplates(":/engraving/instruments/instruments.xml");
}

// ══════════════════════════════════════════════════════════════════════════
// Score loading — verbatim from tools/batch_analyze.cpp
// ══════════════════════════════════════════════════════════════════════════

static MasterScore* loadScore(const muse::io::path_t& path)
{
    QString normalizedPath = path.toQString();
    normalizedPath.replace('\\', '/');
    const muse::String scorePath = muse::String::fromQString(normalizedPath);
    const muse::io::path_t ioPath(normalizedPath);

    MasterScore* score = compat::ScoreAccess::createMasterScoreWithBaseStyle(nullptr);
    score->setFileInfoProvider(std::make_shared<LocalFileInfoProvider>(ioPath));

    const std::string ext = muse::io::suffix(ioPath);
    bool ok = false;
    ScoreLoad sl;

    if (ext == "xml" || ext == "musicxml") {
        const Err rv = mu::iex::musicxml::importMusicXml(score, scorePath, true);
        ok = (rv == Err::NoError);
    } else if (ext == "mxl") {
        const Err rv = mu::iex::musicxml::importCompressedMusicXml(score, scorePath, true);
        ok = (rv == Err::NoError);
    } else {
        const muse::Ret rv = compat::loadMsczOrMscx(score, ioPath, false);
        ok = static_cast<bool>(rv);
    }

    if (!ok) {
        delete score;
        return nullptr;
    }

    score->setPlaylistDirty();
    return score;
}

// ══════════════════════════════════════════════════════════════════════════
// Staff eligibility — verbatim from tools/batch_analyze.cpp
// ══════════════════════════════════════════════════════════════════════════

static bool isChordTrackStaff(const Staff* staff)
{
    if (!staff || !staff->part()) return false;
    const std::string name = staff->part()->partName().toStdString();
    std::string lower = name;
    std::transform(lower.begin(), lower.end(), lower.begin(),
                   [](unsigned char c) { return static_cast<char>(std::tolower(c)); });
    return lower.find("chord") != std::string::npos;
}

static bool staffIsEligible(const Score* score, size_t staffIdx)
{
    const auto& staves = score->staves();
    if (staffIdx >= staves.size()) return false;
    const Staff* st = staves[staffIdx];
    if (!st || !st->visible()) return false;
    const Part* part = st->part();
    if (!part) return false;
    const Instrument* instr = part->instrument();
    if (instr && instr->useDrumset()) return false;
    return !isChordTrackStaff(st);
}

static bool staffIsEligible(const Score* score, size_t staffIdx, const Fraction&)
{
    return staffIsEligible(score, staffIdx);
}

static size_t referenceStaffForAnalysis(const Score* score,
                                        const std::set<size_t>& excludeStaves)
{
    for (size_t si = 0; si < score->nstaves(); ++si) {
        if (!excludeStaves.count(si) && staffIsEligible(score, si)) {
            return si;
        }
    }
    return 0;
}

// ══════════════════════════════════════════════════════════════════════════
// Pitch-class mask — verbatim from tools/batch_analyze.cpp
// ══════════════════════════════════════════════════════════════════════════

static uint16_t pitchClassMask(const std::vector<ChordAnalysisTone>& tones)
{
    uint16_t mask = 0;
    for (const auto& t : tones) {
        mask |= static_cast<uint16_t>(1u << (t.pitch % 12));
    }
    return mask;
}

// ══════════════════════════════════════════════════════════════════════════
// Measure lookup — verbatim from tools/batch_analyze.cpp
// ══════════════════════════════════════════════════════════════════════════

struct MeasureTickInfo {
    const Measure* measure = nullptr;
    int number = 0;
};

static MeasureTickInfo locateMeasureByTick(const Score* score, const Fraction& tick)
{
    if (!score) return {};

    int nextMeasureNumber = 0;
    const Measure* lastMeasure = nullptr;
    for (const Measure* m = score->firstMeasure(); m; m = m->nextMeasure()) {
        nextMeasureNumber += m->measureNumberOffset();
        const int displayedNumber = nextMeasureNumber + 1;
        lastMeasure = m;

        if (tick >= m->tick() && tick < m->endTick()) {
            return { m, displayedNumber };
        }
        if (!m->excludeFromNumbering()) {
            ++nextMeasureNumber;
        }
        const LayoutBreak* lb = m->sectionBreakElement();
        if (lb && lb->startWithMeasureOne()) {
            nextMeasureNumber = 0;
        }
    }
    if (lastMeasure && tick == score->endTick()) {
        return locateMeasureByTick(score, lastMeasure->tick());
    }
    return {};
}

// ══════════════════════════════════════════════════════════════════════════
// Local key inference (windowed) — verbatim from tools/batch_analyze.cpp
// ══════════════════════════════════════════════════════════════════════════

static constexpr int    LOOKBACK_BEATS   = 16;
static constexpr int    LOOKAHEAD_BEATS  = 8;
static constexpr double LOOKAHEAD_WEIGHT = 0.5;
static constexpr double DECAY_RATE       = 0.7;

static double beatTypeToWeight(BeatType bt,
                               const analysis::KeyModeAnalyzerPreferences& prefs)
{
    switch (bt) {
    case BeatType::DOWNBEAT:              return prefs.beatWeightDownbeat;
    case BeatType::COMPOUND_STRESSED:     return prefs.beatWeightCompoundStressed;
    case BeatType::SIMPLE_STRESSED:       return prefs.beatWeightSimpleStressed;
    case BeatType::COMPOUND_UNSTRESSED:   return prefs.beatWeightCompoundUnstressed;
    case BeatType::SIMPLE_UNSTRESSED:     return prefs.beatWeightSimpleUnstressed;
    case BeatType::COMPOUND_SUBBEAT:      return prefs.beatWeightCompoundSubbeat;
    case BeatType::SUBBEAT:               return prefs.beatWeightSubbeat;
    }
    return prefs.beatWeightSubbeat;
}

static BeatType safeBeatType(const Measure* measure, const Segment* segment)
{
    if (!measure || !segment) return BeatType::SUBBEAT;
    const int num = measure->timesig().numerator();
    const int den = measure->timesig().denominator();
    if (num <= 0 || den <= 0) return BeatType::SUBBEAT;
    return TimeSigFrac(num, den).rtick2beatType(segment->rtick().ticks());
}

static double timeDecay(double beatsAgo)
{
    return std::pow(DECAY_RATE, beatsAgo / 4.0);
}

static int distinctPitchClasses(const std::vector<analysis::KeyModeAnalyzer::PitchContext>& ctx)
{
    std::set<int> pcs;
    for (const auto& pc : ctx) {
        pcs.insert(analysis::normalizePc(pc.pitch));
    }
    return static_cast<int>(pcs.size());
}

static void collectPitchContext(Score* score,
                                const std::set<size_t>& excludeStaves,
                                const Fraction& tick,
                                const Fraction& windowStart,
                                const Fraction& windowEnd,
                                const analysis::KeyModeAnalyzerPreferences& prefs,
                                std::vector<analysis::KeyModeAnalyzer::PitchContext>& ctx)
{
    const int division = Constants::DIVISION;
    const Measure* startMeasure = score->tick2measure(windowStart);
    if (!startMeasure) startMeasure = score->firstMeasure();
    if (!startMeasure) return;

    for (const Segment* s = startMeasure->first(SegmentType::ChordRest);
         s && s->tick() <= windowEnd;
         s = s->next1(SegmentType::ChordRest)) {
        const Fraction segTick = s->tick();
        if (segTick < windowStart) continue;

        const Measure* m = s->measure();
        const BeatType bt = safeBeatType(m, s);
        const double bw = beatTypeToWeight(bt, prefs);
        const double beatsFromTick = std::abs((segTick - tick).ticks())
                                     / static_cast<double>(division);
        const double decay = timeDecay(beatsFromTick);
        const double lookaheadMul = (segTick > tick) ? LOOKAHEAD_WEIGHT : 1.0;

        struct NoteInfo { int ppitch; double durationQn; };
        std::vector<NoteInfo> segNotes;
        int lowestPitch = std::numeric_limits<int>::max();

        for (size_t si = 0; si < score->nstaves(); ++si) {
            if (excludeStaves.count(si)) continue;
            for (voice_idx_t v = 0; v < VOICES; ++v) {
                const EngravingItem* e = s->element(staff2track(si, v));
                if (!e || !e->isChord()) continue;
                const Chord* chord = toChord(e);
                if (chord->isGrace()) continue;
                const double durQn = static_cast<double>(chord->ticks().ticks()) / division;
                for (const Note* note : chord->notes()) {
                    segNotes.push_back({ note->ppitch(), durQn });
                    if (note->ppitch() < lowestPitch) lowestPitch = note->ppitch();
                }
            }
        }
        for (const auto& ni : segNotes) {
            analysis::KeyModeAnalyzer::PitchContext p;
            p.pitch          = ni.ppitch;
            p.durationWeight = ni.durationQn * decay * lookaheadMul;
            p.beatWeight     = bw;
            p.isBass         = (ni.ppitch == lowestPitch);
            ctx.push_back(p);
        }
    }
}

static std::vector<KeyModeAnalysisResult> inferLocalKey(
    Score* score,
    size_t keySigStaffIdx,
    const std::set<size_t>& excludeStaves,
    const Fraction& tick,
    const KeyModeAnalysisResult* prevResult = nullptr,
    const analysis::KeyModeAnalyzerPreferences& keyPrefs = analysis::KeyModeAnalyzerPreferences{})
{
    const size_t clampedIdx = std::min(keySigStaffIdx, score->nstaves() - 1);
    const KeySigEvent keySig = score->staff(clampedIdx)->keySigEvent(tick);
    const int keyFifths = static_cast<int>(keySig.concertKey());

    std::optional<analysis::KeySigMode> declaredMode;
    {
        using EMode = mu::engraving::KeyMode;
        using AMode = analysis::KeySigMode;
        switch (keySig.mode()) {
        case EMode::MAJOR:
        case EMode::IONIAN:      declaredMode = AMode::Ionian;     break;
        case EMode::MINOR:
        case EMode::AEOLIAN:     declaredMode = AMode::Aeolian;    break;
        case EMode::DORIAN:      declaredMode = AMode::Dorian;     break;
        case EMode::PHRYGIAN:    declaredMode = AMode::Phrygian;   break;
        case EMode::LYDIAN:      declaredMode = AMode::Lydian;     break;
        case EMode::MIXOLYDIAN:  declaredMode = AMode::Mixolydian; break;
        case EMode::LOCRIAN:     declaredMode = AMode::Locrian;    break;
        default:                 declaredMode = std::nullopt;      break;
        }
    }

    const Fraction lookbackDuration = Fraction(LOOKBACK_BEATS, 4);
    const Fraction windowStart = (tick > lookbackDuration)
                                 ? tick - lookbackDuration
                                 : Fraction(0, 1);

    if (prevResult == nullptr && declaredMode.has_value()
        && windowStart == Fraction(0, 1) && tick < lookbackDuration) {
        KeyModeAnalysisResult decl;
        decl.keySignatureFifths   = keyFifths;
        decl.mode                 = *declaredMode;
        decl.tonicPc              = (analysis::ionianTonicPcFromFifths(keyFifths)
                                     + analysis::keyModeTonicOffset(*declaredMode)) % 12;
        decl.score                = 0.0;
        decl.normalizedConfidence = 0.5;
        return { decl };
    }

    std::vector<analysis::KeyModeAnalyzer::PitchContext> ctx;
    std::vector<KeyModeAnalysisResult> results;

    int lookaheadBeats = LOOKAHEAD_BEATS;
    while (true) {
        ctx.clear();
        collectPitchContext(score, excludeStaves, tick,
                            windowStart, tick + Fraction(lookaheadBeats, 4),
                            keyPrefs, ctx);
        results = analysis::KeyModeAnalyzer::analyzeKeyMode(ctx, keyFifths, keyPrefs, declaredMode);
        const bool confident = !results.empty()
            && results.front().normalizedConfidence >= keyPrefs.dynamicLookaheadConfidenceThreshold;
        const bool atMax = lookaheadBeats >= keyPrefs.dynamicLookaheadMaxBeats;
        if (confident || atMax) break;
        lookaheadBeats += keyPrefs.dynamicLookaheadStepBeats;
    }

    if (results.empty() || distinctPitchClasses(ctx) < 3) {
        KeyModeAnalysisResult fallback;
        fallback.keySignatureFifths = keyFifths;
        fallback.mode = declaredMode.value_or(analysis::KeySigMode::Ionian);
        fallback.tonicPc = (analysis::ionianTonicPcFromFifths(keyFifths)
                            + analysis::keyModeTonicOffset(fallback.mode)) % 12;
        fallback.score = 0.0;
        fallback.normalizedConfidence = 0.0;
        return { fallback };
    }

    std::vector<KeyModeAnalysisResult> topN(
        results.begin(),
        results.begin() + std::min(results.size(), static_cast<size_t>(3)));

    if (!results.empty() && prevResult != nullptr
        && results.front().mode != prevResult->mode) {
        const double hysteresis = (results.front().keySignatureFifths == prevResult->keySignatureFifths)
                                  ? keyPrefs.relativeKeyHysteresisMargin
                                  : keyPrefs.hysteresisMargin;
        if (results.front().score < prevResult->score + hysteresis) {
            for (const auto& r : results) {
                if (r.mode == prevResult->mode
                    && r.keySignatureFifths == prevResult->keySignatureFifths) {
                    std::vector<KeyModeAnalysisResult> out = { r };
                    for (const auto& candidate : topN) {
                        if (out.size() >= 3) break;
                        if (candidate.mode != r.mode
                                || candidate.keySignatureFifths != r.keySignatureFifths) {
                            out.push_back(candidate);
                        }
                    }
                    return out;
                }
            }
        }
    }

    if (!topN.empty()) return topN;

    KeyModeAnalysisResult fallback;
    fallback.keySignatureFifths   = keyFifths;
    fallback.mode                 = analysis::KeySigMode::Ionian;
    fallback.tonicPc              = analysis::ionianTonicPcFromFifths(keyFifths);
    fallback.score                = 0.0;
    fallback.normalizedConfidence = 0.0;
    return { fallback };
}

// ══════════════════════════════════════════════════════════════════════════
// Tone collection + Jaccard boundary detection — verbatim from batch_analyze.cpp
// ══════════════════════════════════════════════════════════════════════════

static std::vector<ChordAnalysisTone> collectRegionTones(
    const Score* score,
    int startTickInt,
    int endTickInt,
    const std::set<size_t>& excludeStaves)
{
    const analysis::ChordAnalyzerPreferences& prefs = analysis::kDefaultChordAnalyzerPreferences;
    if (!score || endTickInt <= startTickInt) return {};

    const Fraction startTick = Fraction::fromTicks(startTickInt);
    const Fraction endTick   = Fraction::fromTicks(endTickInt);
    const int regionDuration = endTickInt - startTickInt;

    auto beatWeight = [](BeatType bt) -> double {
        switch (bt) {
        case BeatType::DOWNBEAT:            return 1.0;
        case BeatType::SIMPLE_STRESSED:
        case BeatType::COMPOUND_STRESSED:   return 0.85;
        case BeatType::SIMPLE_UNSTRESSED:
        case BeatType::COMPOUND_UNSTRESSED: return 0.75;
        default:                            return 0.5;
        }
    };

    struct PcAccum {
        double totalWeight = 0.0;
        int durationInRegion = 0;
        std::set<int> metricTicks;
        int lowestPitch = std::numeric_limits<int>::max();
        int tpc = -1;
    };
    PcAccum accum[12];
    std::map<int, int> voiceCountAtTick[12];

    struct PedalWindow { int startTick = 0; int endTick = 0; };
    struct PedalTailCandidate {
        size_t staffIdx = 0; int pc = 0; int pitch = 0; int tpc = -1;
        int writtenEndTick = 0; double attackBeatWeight = 0.0;
    };
    std::map<size_t, std::vector<PedalWindow>> pedalWindowsByStaff;
    std::vector<PedalTailCandidate> pedalTailCandidates;

    for (const auto& spannerEntry : score->spanner()) {
        const Spanner* spanner = spannerEntry.second;
        if (!spanner || spanner->type() != ElementType::PEDAL) continue;
        const Pedal* pedal = toPedal(spanner);
        if (!pedal) continue;
        const auto& beginText = pedal->beginText();
        if (beginText == u"<sym>keyboardPedalSost</sym>"
            || beginText == u"<sym>keyboardPedalS</sym>") continue;
        const int ps = pedal->tick().ticks();
        const int pe = pedal->tick2().ticks();
        if (pe <= ps || pe <= startTickInt || ps >= endTickInt) continue;
        const size_t si = static_cast<size_t>(pedal->track() / VOICES);
        if (si >= score->nstaves() || excludeStaves.count(si) || !staffIsEligible(score, si)) continue;
        pedalWindowsByStaff[si].push_back({ ps, pe });
    }
    for (auto& pe : pedalWindowsByStaff) {
        std::sort(pe.second.begin(), pe.second.end(),
            [](const PedalWindow& a, const PedalWindow& b) {
                return a.startTick != b.startTick ? a.startTick < b.startTick : a.endTick < b.endTick;
            });
    }

    auto earliestPedalRelease = [&](const PedalTailCandidate& c) -> int {
        auto it = pedalWindowsByStaff.find(c.staffIdx);
        if (it == pedalWindowsByStaff.end()) return -1;
        int rel = std::numeric_limits<int>::max();
        for (const PedalWindow& w : it->second) {
            if (w.startTick >= c.writtenEndTick) break;
            if (w.endTick <= c.writtenEndTick) continue;
            rel = std::min(rel, w.endTick);
        }
        return rel == std::numeric_limits<int>::max() ? -1 : rel;
    };

    auto recordPedalTail = [&](size_t si, int writtenEnd, double bw, const Note* n) {
        if (!n || writtenEnd >= endTickInt || pedalWindowsByStaff.empty()) return;
        if (!pedalWindowsByStaff.count(si)) return;
        pedalTailCandidates.push_back({ si, n->ppitch() % 12, n->ppitch(), n->tpc(),
                                        writtenEnd, bw });
    };

    const Fraction backLimit = startTick - Fraction(4, 1);
    const Segment* firstForward = score->tick2segment(startTick, true, SegmentType::ChordRest);
    const double bwAtStart = [&]() -> double {
        const Measure* m = score->tick2measure(startTick);
        if (!m) return 0.75;
        const Segment* s = score->tick2segment(startTick, true, SegmentType::ChordRest);
        if (!s) return 0.75;
        return beatWeight(safeBeatType(m, s));
    }();

    if (firstForward) {
        for (const Segment* s = firstForward->prev1(SegmentType::ChordRest);
             s && s->tick() >= backLimit;
             s = s->prev1(SegmentType::ChordRest)) {
            const int segTick = s->tick().ticks();
            const Measure* m = s->measure();
            const double sbw = m ? beatWeight(safeBeatType(m, s)) : bwAtStart;
            for (size_t si = 0; si < score->nstaves(); ++si) {
                if (excludeStaves.count(si) || !staffIsEligible(score, si)) continue;
                for (int v = 0; v < VOICES; ++v) {
                    const ChordRest* cr = s->cr(static_cast<track_idx_t>(si) * VOICES + v);
                    if (!cr || !cr->isChord() || cr->isGrace()) continue;
                    const int noteEnd = segTick + cr->actualTicks().ticks();
                    for (const Note* n : toChord(cr)->notes()) {
                        if (!n->play() || !n->visible()) continue;
                        recordPedalTail(si, noteEnd, sbw, n);
                        if (noteEnd <= startTickInt) continue;
                        const int clippedEnd = std::min(noteEnd, endTickInt);
                        const int dur = clippedEnd - startTickInt;
                        if (dur <= 0) continue;
                        const double w = (static_cast<double>(dur) / regionDuration) * bwAtStart;
                        const int pc = n->ppitch() % 12;
                        PcAccum& a = accum[pc];
                        a.totalWeight += w;
                        a.durationInRegion += dur;
                        a.metricTicks.insert(startTickInt);
                        voiceCountAtTick[pc][startTickInt]++;
                        if (n->ppitch() < a.lowestPitch) { a.lowestPitch = n->ppitch(); a.tpc = n->tpc(); }
                    }
                }
            }
        }
    }

    if (!firstForward) return {};

    int pcsSoundingAtStart = 0;
    for (int pc = 0; pc < 12; ++pc) { if (accum[pc].totalWeight > 0.0) ++pcsSoundingAtStart; }
    if (firstForward && firstForward->tick().ticks() == startTickInt) {
        for (size_t si = 0; si < score->nstaves(); ++si) {
            if (excludeStaves.count(si) || !staffIsEligible(score, si)) continue;
            for (int v = 0; v < VOICES; ++v) {
                const ChordRest* cr = firstForward->cr(static_cast<track_idx_t>(si) * VOICES + v);
                if (!cr || !cr->isChord() || cr->isGrace()) continue;
                for (const Note* n : toChord(cr)->notes()) {
                    if (!n->play() || !n->visible()) continue;
                    if (accum[n->ppitch() % 12].totalWeight == 0.0) ++pcsSoundingAtStart;
                }
            }
        }
    }
    const bool excludeLookAhead = (pcsSoundingAtStart >= 3);

    for (const Segment* s = firstForward; s && s->tick() < endTick;
         s = s->next1(SegmentType::ChordRest)) {
        const Measure* m = s->measure();
        if (!m) continue;
        const int segTick = s->tick().ticks();
        const BeatType bt = safeBeatType(m, s);
        const double bw = beatWeight(bt);
        for (size_t si = 0; si < score->nstaves(); ++si) {
            if (excludeStaves.count(si) || !staffIsEligible(score, si)) continue;
            for (int v = 0; v < VOICES; ++v) {
                const ChordRest* cr = s->cr(static_cast<track_idx_t>(si) * VOICES + v);
                if (!cr || !cr->isChord() || cr->isGrace()) continue;
                const int noteEnd = segTick + cr->actualTicks().ticks();
                const int clippedEnd = std::min(noteEnd, endTickInt);
                const int dur = clippedEnd - segTick;
                if (dur <= 0) continue;
                if (excludeLookAhead && segTick > startTickInt) continue;
                const double w = (static_cast<double>(dur) / regionDuration) * bw;
                for (const Note* n : toChord(cr)->notes()) {
                    if (!n->play() || !n->visible()) continue;
                    recordPedalTail(si, noteEnd, bw, n);
                    const int pc = n->ppitch() % 12;
                    PcAccum& a = accum[pc];
                    a.totalWeight += w;
                    a.durationInRegion += dur;
                    a.metricTicks.insert(segTick);
                    voiceCountAtTick[pc][segTick]++;
                    if (n->ppitch() < a.lowestPitch) { a.lowestPitch = n->ppitch(); a.tpc = n->tpc(); }
                }
            }
        }
    }

    for (int pc = 0; pc < 12; ++pc) {
        PcAccum& a = accum[pc];
        if (a.totalWeight == 0.0) continue;
        const int distinct = static_cast<int>(a.metricTicks.size());
        if (distinct > 1) a.totalWeight *= (1.0 + 0.3 * (distinct - 1));
    }
    for (int pc = 0; pc < 12; ++pc) {
        PcAccum& a = accum[pc];
        if (a.totalWeight == 0.0) continue;
        int maxV = 0;
        for (const auto& kv : voiceCountAtTick[pc]) maxV = std::max(maxV, kv.second);
        if (maxV > 1) a.totalWeight *= 1.5;
    }

    if (prefs.pedalTailWeightMultiplier > 0.0) {
        for (const PedalTailCandidate& c : pedalTailCandidates) {
            const int rel = earliestPedalRelease(c);
            if (rel < 0) continue;
            const int tailStart = std::max(c.writtenEndTick, startTickInt);
            const int tailEnd   = std::min(rel, endTickInt);
            const int tailDur   = tailEnd - tailStart;
            if (tailDur <= 0) continue;
            PcAccum& a = accum[c.pc];
            a.totalWeight += (static_cast<double>(tailDur) / regionDuration)
                             * c.attackBeatWeight * prefs.pedalTailWeightMultiplier;
            a.durationInRegion += tailDur;
            if (c.pitch < a.lowestPitch) { a.lowestPitch = c.pitch; a.tpc = c.tpc; }
        }
    }

    double totalWeight = 0.0;
    for (int pc = 0; pc < 12; ++pc) totalWeight += accum[pc].totalWeight;
    if (totalWeight == 0.0) return {};

    int bassPitch = std::numeric_limits<int>::max();
    for (int pc = 0; pc < 12; ++pc) {
        if (accum[pc].totalWeight > 0.0 && accum[pc].lowestPitch < bassPitch)
            bassPitch = accum[pc].lowestPitch;
    }
    const int bassPc = (bassPitch < std::numeric_limits<int>::max()) ? (bassPitch % 12) : -1;

    std::vector<ChordAnalysisTone> tones;
    for (int pc = 0; pc < 12; ++pc) {
        PcAccum& a = accum[pc];
        if (a.totalWeight == 0.0) continue;
        int maxV = 0;
        for (const auto& kv : voiceCountAtTick[pc]) maxV = std::max(maxV, kv.second);
        ChordAnalysisTone t;
        t.pitch = a.lowestPitch;
        t.tpc = a.tpc;
        t.weight = a.totalWeight / totalWeight;
        t.isBass = (pc == bassPc);
        t.durationInRegion = a.durationInRegion;
        t.distinctMetricPositions = static_cast<int>(a.metricTicks.size());
        t.simultaneousVoiceCount = maxV;
        tones.push_back(t);
    }
    return tones;
}

static std::vector<Fraction> detectHarmonicBoundariesJaccard(
    const Score* score,
    const Fraction& startTick,
    const Fraction& endTick,
    const std::set<size_t>& excludeStaves)
{
    if (!score || endTick <= startTick) return {};

    const analysis::ChordAnalyzerPreferences& prefs = analysis::kDefaultChordAnalyzerPreferences;
    const int startTickInt = startTick.ticks();
    const int endTickInt   = endTick.ticks();

    auto popcount16 = [](uint16_t bits) -> int {
        int n = 0; while (bits) { n += bits & 1u; bits >>= 1u; } return n;
    };

    struct PedalWindow { int startTick = 0; int endTick = 0; };
    std::map<size_t, std::vector<PedalWindow>> pedalWindowsByStaff;
    for (const auto& se : score->spanner()) {
        const Spanner* sp = se.second;
        if (!sp || sp->type() != ElementType::PEDAL) continue;
        const Pedal* pedal = toPedal(sp);
        if (!pedal) continue;
        const auto& bt = pedal->beginText();
        if (bt == u"<sym>keyboardPedalSost</sym>" || bt == u"<sym>keyboardPedalS</sym>") continue;
        const int ps = pedal->tick().ticks();
        const int pe = pedal->tick2().ticks();
        if (pe <= ps || pe <= startTickInt || ps >= endTickInt) continue;
        const size_t si = static_cast<size_t>(pedal->track() / VOICES);
        if (si >= score->nstaves() || excludeStaves.count(si) || !staffIsEligible(score, si)) continue;
        pedalWindowsByStaff[si].push_back({ ps, pe });
    }
    for (auto& pe : pedalWindowsByStaff) {
        std::sort(pe.second.begin(), pe.second.end(),
            [](const PedalWindow& a, const PedalWindow& b) {
                return a.startTick != b.startTick ? a.startTick < b.startTick : a.endTick < b.endTick;
            });
    }

    auto earliestPedalRelease = [&](size_t si, int writtenEnd) -> int {
        auto it = pedalWindowsByStaff.find(si);
        if (it == pedalWindowsByStaff.end()) return -1;
        int rel = std::numeric_limits<int>::max();
        for (const PedalWindow& w : it->second) {
            if (w.startTick >= writtenEnd) break;
            if (w.endTick <= writtenEnd) continue;
            rel = std::min(rel, w.endTick);
        }
        return rel == std::numeric_limits<int>::max() ? -1 : rel;
    };

    const int windowTicks = Constants::DIVISION;
    std::map<int, uint16_t> bitsByWindowTick;

    auto addWindowBits = [&](int spanStart, int spanEnd, int pc) {
        const int cs = std::max(spanStart, startTickInt);
        const int ce = std::min(spanEnd, endTickInt);
        if (ce <= cs) return;
        for (int wt = (cs / windowTicks) * windowTicks; wt < ce; wt += windowTicks)
            bitsByWindowTick[wt] |= static_cast<uint16_t>(1u << pc);
    };

    auto recordPedalTailSpan = [&](size_t si, int writtenEnd, const Note* n) {
        if (!n || pedalWindowsByStaff.empty()) return;
        const int rel = earliestPedalRelease(si, writtenEnd);
        if (rel <= writtenEnd) return;
        addWindowBits(writtenEnd, rel, n->ppitch() % 12);
    };

    const Segment* seg = score->tick2segment(startTick, true, SegmentType::ChordRest);
    if (!seg) return { startTick };

    const Fraction backLimit = startTick - Fraction(4, 1);
    for (const Segment* s = seg->prev1(SegmentType::ChordRest);
         s && s->tick() >= backLimit;
         s = s->prev1(SegmentType::ChordRest)) {
        for (size_t si = 0; si < score->nstaves(); ++si) {
            if (excludeStaves.count(si) || !staffIsEligible(score, si)) continue;
            for (voice_idx_t v = 0; v < VOICES; ++v) {
                const EngravingItem* e = s->element(staff2track(si, v));
                if (!e || !e->isChord()) continue;
                const Chord* ch = toChord(e);
                if (ch->isGrace()) continue;
                for (const Note* n : ch->notes()) {
                    recordPedalTailSpan(si, s->tick().ticks() + ch->actualTicks().ticks(), n);
                }
            }
        }
    }

    for (const Segment* s = seg; s && s->tick() < endTick; s = s->next1(SegmentType::ChordRest)) {
        const int st = s->tick().ticks();
        const int swt = (st / windowTicks) * windowTicks;
        for (size_t si = 0; si < score->nstaves(); ++si) {
            if (excludeStaves.count(si) || !staffIsEligible(score, si)) continue;
            for (voice_idx_t v = 0; v < VOICES; ++v) {
                const EngravingItem* e = s->element(staff2track(si, v));
                if (!e || !e->isChord()) continue;
                const Chord* ch = toChord(e);
                if (ch->isGrace()) continue;
                for (const Note* n : ch->notes()) {
                    bitsByWindowTick[swt] |= static_cast<uint16_t>(1u << (n->ppitch() % 12));
                    recordPedalTailSpan(si, st + ch->actualTicks().ticks(), n);
                }
            }
        }
    }

    struct Window { Fraction tick; uint16_t bits = 0; };
    std::vector<Window> windows;
    windows.reserve(bitsByWindowTick.size());
    for (const auto& entry : bitsByWindowTick) {
        if (entry.second) windows.push_back({ Fraction::fromTicks(entry.first), entry.second });
    }
    if (windows.empty()) return { startTick };

    std::vector<Fraction> boundaries;
    boundaries.push_back(startTick);
    uint16_t prevBits = windows[0].bits;
    for (size_t i = 1; i < windows.size(); ++i) {
        const uint16_t bits = windows[i].bits;
        const uint16_t inter = prevBits & bits;
        const uint16_t uni   = prevBits | bits;
        const int ic = popcount16(inter);
        const int uc = popcount16(uni);
        const double dist = (uc > 0) ? (1.0 - static_cast<double>(ic) / uc) : 0.0;
        if (dist >= prefs.harmonicBoundaryJaccardThreshold) {
            boundaries.push_back(windows[i].tick);
            prevBits = bits;
        } else {
            prevBits = uni;
        }
    }
    return boundaries;
}

static std::vector<Fraction> detectBassMovementSubBoundaries(
    const Score* score,
    const Fraction& startTick,
    const Fraction& endTick,
    const std::set<size_t>& excludeStaves,
    int minGapTicks = 2 * Constants::DIVISION)
{
    std::vector<Fraction> subBoundaries;
    if (!score || endTick <= startTick) return subBoundaries;
    const Segment* firstSeg = score->tick2segment(startTick, true, SegmentType::ChordRest);
    if (!firstSeg) return subBoundaries;

    struct BassOnset { Fraction tick; int bassPC = -1; };
    std::vector<BassOnset> onsets;

    for (const Segment* s = firstSeg; s && s->tick() < endTick;
         s = s->next1(SegmentType::ChordRest)) {
        const int segTick = s->tick().ticks();
        int lowestPitch = std::numeric_limits<int>::max();
        int lowestPC    = -1;
        for (size_t si = 0; si < score->nstaves(); ++si) {
            if (excludeStaves.count(si) || !staffIsEligible(score, si)) continue;
            for (voice_idx_t v = 0; v < VOICES; ++v) {
                const EngravingItem* e = s->element(staff2track(si, v));
                if (!e || !e->isChord()) continue;
                const Chord* ch = toChord(e);
                if (!ch || ch->isGrace()) continue;
                if (ch->tick().ticks() != segTick) continue;
                for (const Note* n : ch->notes()) {
                    if (!n->play() || !n->visible()) continue;
                    if (n->ppitch() < lowestPitch) { lowestPitch = n->ppitch(); lowestPC = n->ppitch() % 12; }
                }
            }
        }
        if (lowestPC >= 0) onsets.push_back({ s->tick(), lowestPC });
    }

    if (onsets.empty()) return subBoundaries;
    int lastBoundaryPC = onsets[0].bassPC;
    Fraction lastBoundaryTick = startTick;
    for (size_t i = 1; i < onsets.size(); ++i) {
        const int gapTicks = (onsets[i].tick - lastBoundaryTick).ticks();
        if (onsets[i].bassPC != lastBoundaryPC && gapTicks >= minGapTicks) {
            subBoundaries.push_back(onsets[i].tick);
            lastBoundaryTick = onsets[i].tick;
            lastBoundaryPC   = onsets[i].bassPC;
        }
    }
    return subBoundaries;
}

struct SoundingNote { int ppitch = 0; int tpc = -1; };

static void collectSoundingAt(const Score* score,
                              const Segment* anchorSegment,
                              const std::set<size_t>& excludeStaves,
                              std::vector<SoundingNote>& out)
{
    if (!score || !anchorSegment) return;
    const Fraction anchorTick = anchorSegment->tick();
    auto collect = [&](const Segment* seg, const ChordRest* cr) {
        if (!cr || !cr->isChord() || cr->isGrace()) return;
        if (seg->tick() < anchorTick) {
            if (seg->tick() + toChord(cr)->actualTicks() <= anchorTick) return;
        }
        for (const Note* n : toChord(cr)->notes()) {
            if (!n->play() || !n->visible()) continue;
            out.push_back({ n->ppitch(), n->tpc() });
        }
    };
    for (size_t si = 0; si < score->nstaves(); ++si) {
        if (excludeStaves.count(si) || !staffIsEligible(score, si, anchorTick)) continue;
        for (voice_idx_t v = 0; v < VOICES; ++v)
            collect(anchorSegment, anchorSegment->cr(static_cast<track_idx_t>(si) * VOICES + v));
    }
    const Fraction backLimit = anchorTick - Fraction(4, 1);
    for (const Segment* s = anchorSegment->prev1(SegmentType::ChordRest);
         s && s->tick() >= backLimit;
         s = s->prev1(SegmentType::ChordRest)) {
        for (size_t si = 0; si < score->nstaves(); ++si) {
            if (excludeStaves.count(si) || !staffIsEligible(score, si, anchorTick)) continue;
            for (voice_idx_t v = 0; v < VOICES; ++v)
                collect(s, s->cr(static_cast<track_idx_t>(si) * VOICES + v));
        }
    }
}

static std::vector<ChordAnalysisTone> buildTones(const std::vector<SoundingNote>& sounding)
{
    int lowestPitch = std::numeric_limits<int>::max();
    for (const auto& sn : sounding) lowestPitch = std::min(lowestPitch, sn.ppitch);
    std::vector<ChordAnalysisTone> tones;
    tones.reserve(sounding.size());
    for (const auto& sn : sounding) {
        ChordAnalysisTone t;
        t.pitch = sn.ppitch; t.tpc = sn.tpc; t.isBass = (sn.ppitch == lowestPitch);
        tones.push_back(t);
    }
    return tones;
}

static bool isDiatonicStep(int pc1, int pc2)
{
    int interval = std::abs(pc1 - pc2);
    interval = std::min(interval, 12 - interval);
    return interval == 1 || interval == 2;
}

static ChordTemporalContext findTemporalContext(
    const Score* score,
    const Segment* segment,
    const std::set<size_t>& excludeStaves,
    int keyFifths,
    analysis::KeySigMode keyMode,
    int currentBassPc)
{
    ChordTemporalContext ctx;
    if (!score || !segment) return ctx;
    const Fraction tick = segment->tick();
    const auto chordAnalyzer = analysis::ChordAnalyzerFactory::create();

    for (const Segment* prev = segment->prev1(SegmentType::ChordRest);
         prev != nullptr;
         prev = prev->prev1(SegmentType::ChordRest)) {
        bool hasAttacks = false;
        for (size_t si = 0; si < score->nstaves() && !hasAttacks; ++si) {
            if (excludeStaves.count(si) || !staffIsEligible(score, si, tick)) continue;
            for (int v = 0; v < VOICES && !hasAttacks; ++v) {
                const ChordRest* cr = prev->cr(static_cast<track_idx_t>(si) * VOICES + v);
                if (cr && cr->isChord() && !cr->isGrace()) hasAttacks = true;
            }
        }
        if (!hasAttacks) continue;
        std::vector<SoundingNote> prevSounding;
        collectSoundingAt(score, prev, excludeStaves, prevSounding);
        if (!prevSounding.empty()) {
            const auto prevTones = buildTones(prevSounding);
            const auto prevResults = chordAnalyzer->analyzeChord(prevTones, keyFifths, keyMode);
            if (!prevResults.empty()) {
                ctx.previousRootPc    = prevResults.front().identity.rootPc;
                ctx.previousQuality   = prevResults.front().identity.quality;
                ctx.previousBassPc    = prevResults.front().identity.bassPc;
            }
        }
        break;
    }
    if (currentBassPc != -1 && ctx.previousBassPc != -1)
        ctx.bassIsStepwiseFromPrevious = isDiatonicStep(ctx.previousBassPc, currentBassPc);
    return ctx;
}

static std::vector<AnalyzedRegion> analyzeScore(
    Score* score,
    const std::set<size_t>& excludeStaves,
    const analysis::KeyModeAnalyzerPreferences& keyPrefs  = analysis::KeyModeAnalyzerPreferences{},
    const analysis::ChordAnalyzerPreferences& chordPrefs  = analysis::kDefaultChordAnalyzerPreferences)
{
    const Segment* firstSegment = score->tick2segment(Fraction(0, 1), true, SegmentType::ChordRest);
    if (!firstSegment) return {};

    const Fraction startTick = firstSegment->tick();
    const Fraction endTick   = score->endTick();
    std::vector<AnalyzedRegion> result;
    auto boundaryTicks = detectHarmonicBoundariesJaccard(score, startTick, endTick, excludeStaves);

    {
        static constexpr int kPass2bMinRegionTicks = 4 * Constants::DIVISION;
        std::vector<Fraction> expandedTicks;
        expandedTicks.reserve(boundaryTicks.size() * 2);
        for (size_t bi = 0; bi < boundaryTicks.size(); ++bi) {
            expandedTicks.push_back(boundaryTicks[bi]);
            const Fraction rStart = boundaryTicks[bi];
            const Fraction rEnd = (bi + 1 < boundaryTicks.size())
                                  ? boundaryTicks[bi + 1] : endTick;
            if ((rEnd - rStart).ticks() >= kPass2bMinRegionTicks) {
                for (const Fraction& t : detectBassMovementSubBoundaries(score, rStart, rEnd, excludeStaves))
                    expandedTicks.push_back(t);
            }
        }
        boundaryTicks = std::move(expandedTicks);
    }

    result.reserve(boundaryTicks.size());
    const size_t refStaff = referenceStaffForAnalysis(score, excludeStaves);
    const auto initialKey = inferLocalKey(score, refStaff, excludeStaves, startTick, nullptr, keyPrefs)[0];
    ChordTemporalContext ctx = findTemporalContext(
        score, firstSegment, excludeStaves, initialKey.keySignatureFifths, initialKey.mode, -1);
    const auto chordAnalyzer = analysis::ChordAnalyzerFactory::create();
    std::optional<KeyModeAnalysisResult> prevKey;

    for (size_t bi = 0; bi < boundaryTicks.size(); ++bi) {
        const Fraction rStart = boundaryTicks[bi];
        const Fraction rEnd   = (bi + 1 < boundaryTicks.size()) ? boundaryTicks[bi + 1] : endTick;
        auto tones = collectRegionTones(score, rStart.ticks(), rEnd.ticks(), excludeStaves);
        if (tones.empty()) continue;

        const MeasureTickInfo rMeasure = locateMeasureByTick(score, rStart);
        const Measure* measure = rMeasure.measure;
        if (!measure) continue;

        int currentBassPc = -1;
        for (const auto& t : tones) { if (t.isBass) { currentBassPc = t.pitch % 12; break; } }
        ctx.bassIsStepwiseFromPrevious = (ctx.previousBassPc != -1 && currentBassPc != -1)
            && isDiatonicStep(ctx.previousBassPc, currentBassPc);

        int nextBassPc = -1;
        if (currentBassPc != -1 && bi + 1 < boundaryTicks.size()) {
            const Fraction nStart = boundaryTicks[bi + 1];
            const Fraction nEnd   = (bi + 2 < boundaryTicks.size()) ? boundaryTicks[bi + 2] : endTick;
            const auto nextTones = collectRegionTones(score, nStart.ticks(), nEnd.ticks(), excludeStaves);
            for (const auto& t : nextTones) { if (t.isBass) { nextBassPc = t.pitch % 12; break; } }
        }
        ctx.bassIsStepwiseToNext = (currentBassPc != -1 && nextBassPc != -1)
            && isDiatonicStep(currentBassPc, nextBassPc);

        const std::vector<KeyModeAnalysisResult> keyRanked = inferLocalKey(
            score, refStaff, excludeStaves, rStart,
            prevKey.has_value() ? &prevKey.value() : nullptr, keyPrefs);
        const KeyModeAnalysisResult& localKey = keyRanked[0];
        prevKey = localKey;

        auto candidates = chordAnalyzer->analyzeChord(
            tones, localKey.keySignatureFifths, localKey.mode, &ctx, chordPrefs);
        if (candidates.empty()) continue;

        const uint16_t pcMask = pitchClassMask(tones);
        ctx.previousRootPc   = candidates[0].identity.rootPc;
        ctx.previousQuality  = candidates[0].identity.quality;
        ctx.previousBassPc   = candidates[0].identity.bassPc;

        if (!result.empty()
            && result.back().chord.identity.rootPc  == candidates[0].identity.rootPc
            && result.back().chord.identity.quality == candidates[0].identity.quality) {
            result.back().endTick = rEnd.ticks();
            analysis::mergeChordAnalysisTones(result.back().tones, tones);
            result.back().pcMask |= pcMask;
            if (const auto* bt = analysis::bassToneFromTones(result.back().tones)) {
                result.back().bassPc = bt->pitch % 12;
                result.back().chord.identity.bassPc  = bt->pitch % 12;
                result.back().chord.identity.bassTpc = bt->tpc;
            }
            continue;
        }

        AnalyzedRegion ar;
        ar.startTick     = rStart.ticks();
        ar.endTick       = rEnd.ticks();
        ar.measureNumber = rMeasure.number;
        ar.beat          = 1.0 + static_cast<double>(rStart.ticks() - measure->tick().ticks())
                               / Constants::DIVISION;
        ar.chord         = candidates[0];
        ar.hasAnalyzedChord = true;
        ar.tones         = std::move(tones);
        ar.key           = localKey;
        ar.keyRanked     = keyRanked;
        ar.pcMask        = pcMask;
        ar.bassPc        = currentBassPc;
        for (size_t ci = 1; ci < candidates.size() && ci <= 2; ++ci)
            ar.alternatives.push_back(candidates[ci]);
        result.push_back(std::move(ar));
    }

    if (result.empty()) return {};

    const int minRegionTicks = Constants::DIVISION;
    std::vector<AnalyzedRegion> filtered;
    filtered.reserve(result.size());
    filtered.push_back(std::move(result[0]));
    for (size_t i = 1; i < result.size(); ++i) {
        const int dur = result[i].endTick - result[i].startTick;
        if (dur < minRegionTicks) {
            filtered.back().endTick = result[i].endTick;
        } else {
            filtered.push_back(std::move(result[i]));
        }
    }
    return filtered;
}

// ══════════════════════════════════════════════════════════════════════════
// Emitter utilities
// ══════════════════════════════════════════════════════════════════════════

// Format pitch from TPC + MIDI pitch.  Returns e.g. "F#4", "Bb2", "C5".
static std::string pitchName(int tpc, int pitch)
{
    // tpc2name uses muse::String; convert to std::string via toStdString().
    const muse::String name = tpc2name(tpc, NoteSpellingType::STANDARD, NoteCaseType::AUTO);
    const int octave = pitch / 12 - 1;
    return name.toStdString() + std::to_string(octave);
}

// Format a duration as "w", "h", "q", "e", "s", "32", "64" with optional dot suffix.
static std::string durationName(DurationType type, int dots)
{
    const char* base;
    switch (type) {
    case DurationType::V_WHOLE:   base = "w";  break;
    case DurationType::V_HALF:    base = "h";  break;
    case DurationType::V_QUARTER: base = "q";  break;
    case DurationType::V_EIGHTH:  base = "e";  break;
    case DurationType::V_16TH:    base = "s";  break;
    case DurationType::V_32ND:    base = "32"; break;
    case DurationType::V_64TH:    base = "64"; break;
    default:                      base = "?";  break;
    }
    std::string result = base;
    for (int d = 0; d < dots; ++d) result += '.';
    return result;
}

// Format a measure + beat stamp: "m4 b3.0"
static std::string measureBeat(int measureNum, int tickInMeasure)
{
    const double beat = 1.0 + static_cast<double>(tickInMeasure) / Constants::DIVISION;
    char buf[64];
    std::snprintf(buf, sizeof(buf), "m%d b%.4g", measureNum, beat);
    return buf;
}

// Emit the standard header block.
static void emitHeader(std::ostream& out,
                       const std::string& scoreBasename,
                       const std::string& sourcePath,
                       const char* formatLabel,
                       const Score* score)
{
    const QDateTime now = QDateTime::currentDateTime();
    const std::string ts = now.toString(Qt::ISODate).toStdString();

    // Initial key sig from staff 0 tick 0
    std::string keySigStr = "(unknown)";
    std::string timeSigStr = "?/?";
    if (score && score->firstMeasure()) {
        const Staff* st = score->staff(0);
        if (st) {
            const KeySigEvent kse = st->keySigEvent(Fraction(0, 1));
            const int fifths = static_cast<int>(kse.concertKey());
            // Map fifths to key name
            static const char* sharpNames[] = { "C", "G", "D", "A", "E", "B", "F#", "C#" };
            static const char* flatNames[]  = { "C", "F", "Bb", "Eb", "Ab", "Db", "Gb", "Cb" };
            const char* root = (fifths >= 0)
                ? sharpNames[std::min(fifths, 7)]
                : flatNames[std::min(-fifths, 7)];
            keySigStr = std::string(root) + (kse.mode() == KeyMode::MINOR ? " minor" : " major");
        }
        const Measure* m = score->firstMeasure();
        const Fraction mts = m->timesig();
        timeSigStr = std::to_string(mts.numerator()) + "/" + std::to_string(mts.denominator());
    }

    out << "# Score:        " << scoreBasename << "\n";
    out << "# Source path:  " << sourcePath    << "\n";
    out << "# Generated:    " << ts            << "\n";
    out << "# Format:       llm_triage v0 (" << formatLabel << ")\n";
    out << "# Key sig:      " << keySigStr << " (notation; not an analytical claim)\n";
    out << "# Time sig:     " << timeSigStr << " (initial; changes annotated inline)\n";
    out << "\n";
}

// ══════════════════════════════════════════════════════════════════════════
// Emitter 1 & 2: notes_only and with_symbols
//
// Single pass over the score's ChordRest segments.  Emits one line per
// distinct tick with note attacks, grouped by eligible staff.
// with_symbols additionally appends `printed: "..."` for Harmony annotations.
// ══════════════════════════════════════════════════════════════════════════

static void emitNoteLines(std::ostream& out,
                          const Score* score,
                          const std::set<size_t>& excludeStaves,
                          bool includeSymbols)
{
    if (!score) return;

    // Build per-staff display labels, disambiguating staves that share partName()
    // (e.g. piano: one Part, two Staves both named "Piano") so LLM input can
    // distinguish upper from lower without pitch-range inference.
    // Only eligible staves are counted — excluded staves (percussion, chord track)
    // are invisible in output and must not consume ordinal slots.
    std::map<std::string, int> partNameCount;
    for (size_t si = 0; si < score->nstaves(); ++si) {
        if (!staffIsEligible(score, si)) continue;
        const Staff* st = score->staff(si);
        if (st && st->part()) {
            partNameCount[st->part()->partName().toStdString()]++;
        }
    }
    std::map<std::string, int> partNameOrdinal; // running ordinal within each part name
    std::vector<std::string> staffPartName(score->nstaves(), "");
    for (size_t si = 0; si < score->nstaves(); ++si) {
        if (!staffIsEligible(score, si)) continue;
        const Staff* st = score->staff(si);
        if (!st || !st->part()) continue;
        const std::string name = st->part()->partName().toStdString();
        if (partNameCount[name] > 1) {
            const int ordinal = ++partNameOrdinal[name];
            staffPartName[si] = name + " #" + std::to_string(ordinal);
        } else {
            staffPartName[si] = name;
        }
    }

    Fraction prevTimeSig(-1, 1);

    for (const Measure* m = score->firstMeasure(); m; m = m->nextMeasure()) {
        // Detect time-sig change.
        const Fraction ts = m->timesig();
        if (ts != prevTimeSig) {
            out << "# Time sig: "
                << ts.numerator() << "/" << ts.denominator() << "\n";
            prevTimeSig = ts;
        }

        // Walk ChordRest segments in this measure.
        for (const Segment* s = m->first(SegmentType::ChordRest);
             s && s->tick() < m->endTick();
             s = s->next(SegmentType::ChordRest)) {

            const int segTick   = s->tick().ticks();
            const int tickInMsr = segTick - m->tick().ticks();
            const MeasureTickInfo mti = locateMeasureByTick(score, s->tick());

            // Collect notes per eligible staff at this tick.
            // staff → list of "pitchName(dur)"
            struct StaffOnset {
                size_t staffIdx = 0;
                std::string partName;
                std::string durLabel;
                std::vector<std::string> pitches;
            };
            std::vector<StaffOnset> onsetsThisTick;

            for (size_t si = 0; si < score->nstaves(); ++si) {
                if (excludeStaves.count(si) || !staffIsEligible(score, si)) continue;

                StaffOnset so;
                so.staffIdx  = si;
                so.partName  = staffPartName[si];
                std::string durLabel;

                for (voice_idx_t v = 0; v < VOICES; ++v) {
                    const EngravingItem* e = s->element(staff2track(si, v));
                    if (!e) continue;
                    if (!e->isChord()) continue;
                    const Chord* ch = toChord(e);
                    if (ch->isGrace()) continue;

                    if (durLabel.empty()) {
                        durLabel = durationName(ch->durationType().type(), ch->dots());
                    }

                    for (const Note* n : ch->notes()) {
                        if (!n->play() || !n->visible()) continue;
                        so.pitches.push_back(pitchName(n->tpc(), n->pitch()));
                    }
                    // Sort pitches low→high by MIDI pitch.
                    // We collected them already sorted by note order but let's be explicit.
                }

                if (!so.pitches.empty()) {
                    so.durLabel = durLabel;
                    // Sort ascending pitch (lowest first).
                    std::sort(so.pitches.begin(), so.pitches.end(),
                              [](const std::string& a, const std::string& b) {
                                  // Simple lexicographic sort is wrong for pitch names.
                                  // Re-extract octave digit from last char(s) for numeric compare.
                                  auto pitchVal = [](const std::string& s) {
                                      // last 1-2 chars are octave number (could be negative but
                                      // unlikely in practice).  Walk back past digits.
                                      int i = static_cast<int>(s.size()) - 1;
                                      while (i >= 0 && (std::isdigit(s[i]) || s[i] == '-')) --i;
                                      return std::stoi(s.substr(i + 1));
                                  };
                                  return pitchVal(a) < pitchVal(b);
                              });
                    onsetsThisTick.push_back(std::move(so));
                }
            }

            if (onsetsThisTick.empty()) continue;

            // Use duration from the first staff with notes (representative).
            const std::string& durLabel = onsetsThisTick[0].durLabel;

            // Format: "m4 b3.0 (q):  staff "Piano RH": F#4 A4 D5 ; staff "Piano LH": D2"
            out << measureBeat(mti.number, tickInMsr)
                << " (" << durLabel << "):  ";

            for (size_t oi = 0; oi < onsetsThisTick.size(); ++oi) {
                if (oi > 0) out << " ; ";
                out << "staff \"" << onsetsThisTick[oi].partName << "\": ";
                for (size_t pi = 0; pi < onsetsThisTick[oi].pitches.size(); ++pi) {
                    if (pi > 0) out << " ";
                    out << onsetsThisTick[oi].pitches[pi];
                }
            }

            // For with_symbols: check for Harmony annotations at this segment.
            if (includeSymbols) {
                for (const EngravingItem* ann : s->annotations()) {
                    if (!ann || ann->type() != ElementType::HARMONY) continue;
                    const Harmony* h = toHarmony(ann);
                    if (!h) continue;
                    // Only emit STANDARD harmony type (not ROMAN, NASHVILLE).
                    if (h->harmonyType() != HarmonyType::STANDARD) continue;
                    const std::string sym = h->harmonyName().toStdString();
                    if (!sym.empty()) {
                        out << "  printed: \"" << sym << "\"";
                        break; // only first standard harmony at this tick
                    }
                }
            }

            out << "\n";
        }
    }
}

// ══════════════════════════════════════════════════════════════════════════
// Emitter 3: analyzer_output
// ══════════════════════════════════════════════════════════════════════════

static std::string keyDisplayStr(const KeyModeAnalysisResult& key)
{
    const char* tonic = analysis::keyModeTonicName(key.keySignatureFifths, key.mode);
    // Map mode to a display name and a technical name for the "(mode: ...)" tag.
    const char* display;
    const char* technical;
    switch (key.mode) {
    case analysis::KeySigMode::Ionian:           display = "major";   technical = "Ionian";      break;
    case analysis::KeySigMode::Aeolian:          display = "minor";   technical = "Aeolian";     break;
    case analysis::KeySigMode::Dorian:           display = "Dorian";  technical = "Dorian";      break;
    case analysis::KeySigMode::Phrygian:         display = "Phrygian";technical = "Phrygian";    break;
    case analysis::KeySigMode::Lydian:           display = "Lydian";  technical = "Lydian";      break;
    case analysis::KeySigMode::Mixolydian:       display = "Mixolydian"; technical = "Mixolydian"; break;
    case analysis::KeySigMode::Locrian:          display = "Locrian"; technical = "Locrian";     break;
    default:
        display = technical = analysis::keyModeSuffix(key.mode);
        break;
    }
    return std::string(tonic) + " " + display + " (mode: " + technical + ")";
}

static void emitAnalyzerOutput(std::ostream& out,
                               const std::vector<AnalyzedRegion>& regions,
                               const Score* score)
{
    for (size_t i = 0; i < regions.size(); ++i) {
        const AnalyzedRegion& r = regions[i];
        const MeasureTickInfo startMti = locateMeasureByTick(score, Fraction::fromTicks(r.startTick));
        const MeasureTickInfo endMti   = locateMeasureByTick(score, Fraction::fromTicks(r.endTick));

        const int startTickInMsr = r.startTick - (startMti.measure ? startMti.measure->tick().ticks() : 0);
        const int endTickInMsr   = r.endTick   - (endMti.measure   ? endMti.measure->tick().ticks()   : 0);

        out << "region " << (i + 1)
            << ": ticks [" << r.startTick << ", " << r.endTick << ")"
            << "  " << measureBeat(startMti.number, startTickInMsr)
            << " -> " << measureBeat(endMti.number, endTickInMsr)
            << "\n";

        // Chord symbol via production ChordSymbolFormatter.
        const std::string chordSym = analysis::ChordSymbolFormatter::formatSymbol(
            r.chord, r.key.keySignatureFifths);

        // Pitch-class set from tones.
        std::string pcSet;
        {
            // Collect note names from tones (sorted by pitch).
            std::vector<std::pair<int,int>> pitchTpc; // (pitch, tpc)
            for (const auto& t : r.tones) pitchTpc.push_back({ t.pitch, t.tpc });
            std::sort(pitchTpc.begin(), pitchTpc.end());
            for (size_t pi = 0; pi < pitchTpc.size(); ++pi) {
                if (pi > 0) pcSet += " ";
                pcSet += pitchName(pitchTpc[pi].second, pitchTpc[pi].first);
            }
        }

        out << "  chord:        " << chordSym << " (" << pcSet << ")\n";

        // Alternatives.
        if (r.alternatives.empty()) {
            out << "  alternatives: (none)\n";
        } else {
            out << "  alternatives: [";
            for (size_t ai = 0; ai < r.alternatives.size(); ++ai) {
                if (ai > 0) out << ", ";
                const std::string altSym = analysis::ChordSymbolFormatter::formatSymbol(
                    r.alternatives[ai], r.key.keySignatureFifths);
                out << altSym;
            }
            out << "]\n";
        }

        out << "  key:          " << keyDisplayStr(r.key) << "\n";

        char confBuf[64];
        std::snprintf(confBuf, sizeof(confBuf), "%.2f", r.chord.identity.normalizedConfidence);
        out << "  confidence:   " << confBuf << "\n";

        // key_area: always n/a in v0 (flat vector, no AnalyzedSection).
        out << "  key_area:     (n/a in v0 — analyzer entry point returns flat region vector;"
               " full AnalyzedSection consumption deferred to v1)\n";
        out << "\n";
    }
}

// ══════════════════════════════════════════════════════════════════════════
// Emitter 4: analyzer_response.json
//
// Emits a JSON file whose top-level shape (metadata + tool_input) matches the
// LLM-side response files so v1.3's comparator can read all four sources
// provider-agnostically.  Analyzer-specific additions (tick_start, tick_end,
// tones_pc_set) are superset fields; the comparator must tolerate extra keys.
//
// Beat-range convention: "<startBeat>-<endBeat>" where both are 1-indexed
// integer beats within the region's start measure and endBeat is exclusive.
// "N-end" is used when the region extends to or past the measure boundary.
// ══════════════════════════════════════════════════════════════════════════

static std::string keySigModeStr(analysis::KeySigMode mode)
{
    switch (mode) {
    case analysis::KeySigMode::Ionian:     return "Ionian";
    case analysis::KeySigMode::Dorian:     return "Dorian";
    case analysis::KeySigMode::Phrygian:   return "Phrygian";
    case analysis::KeySigMode::Lydian:     return "Lydian";
    case analysis::KeySigMode::Mixolydian: return "Mixolydian";
    case analysis::KeySigMode::Aeolian:    return "Aeolian";
    case analysis::KeySigMode::Locrian:    return "Locrian";
    default:                               return "Ionian";
    }
}

static std::string keyShortStr(const KeyModeAnalysisResult& key)
{
    const char* tonic = analysis::keyModeTonicName(key.keySignatureFifths, key.mode);
    std::string display;
    switch (key.mode) {
    case analysis::KeySigMode::Ionian:  display = "major"; break;
    case analysis::KeySigMode::Aeolian: display = "minor"; break;
    default:                            display = keySigModeStr(key.mode); break;
    }
    return std::string(tonic) + " " + display;
}

// Maps normalizedConfidence (0–1 sigmoid-normalized score gap) to the LLM
// schema ordinal.  Abstain when !hasAnalyzedChord or nc < 0.05.
static std::string confidenceOrdinal(double nc, bool hasAnalyzedChord)
{
    if (!hasAnalyzedChord || nc < 0.05) return "abstain";
    if (nc >= 0.80) return "very_high";
    if (nc >= 0.60) return "high";
    if (nc >= 0.40) return "medium";
    if (nc >= 0.20) return "low";
    return "very_low";
}

static void emitAnalyzerJson(std::ostream& out,
                             const std::string& sourcePrefix,
                             const std::string& sourcePath,
                             const std::string& scoreContentHash,
                             const std::vector<AnalyzedRegion>& regions,
                             const Score* score)
{
    // Deterministic response ID: first 16 hex chars of SHA-256(hash || regionCount).
    const std::string idInput = scoreContentHash + std::to_string(regions.size());
    const QByteArray idHash = QCryptographicHash::hash(
        QByteArray::fromStdString(idInput), QCryptographicHash::Sha256);
    const std::string modelResponseId = "deterministic-"
        + idHash.toHex().left(16).toStdString();

    const QString tsUtc = QDateTime::currentDateTimeUtc().toString(Qt::ISODate);

    QJsonObject metadata;
    metadata["score_basename"]       = QString::fromStdString(sourcePrefix);
    metadata["score_path"]           = QString::fromStdString(sourcePath);
    metadata["score_content_hash"]   = QString::fromStdString(scoreContentHash);
    metadata["requested_model"]      = "chordanalyzer-v0";
    metadata["provider"]             = "musescore_analyzer";
    metadata["model"]                = "chordanalyzer-v0";
    metadata["model_response_id"]    = QString::fromStdString(modelResponseId);
    metadata["prompt_version"]       = "v1.3-pre";
    metadata["system_prompt_hash"]   = "";
    metadata["tool_definition_hash"] = "";
    metadata["timestamp_utc"]        = tsUtc;
    metadata["input_tokens"]         = 0;
    metadata["output_tokens"]        = 0;
    metadata["stop_reason"]          = "completed";

    QJsonArray judgments;
    for (size_t i = 0; i < regions.size(); ++i) {
        const AnalyzedRegion& r = regions[i];

        const MeasureTickInfo startMti = locateMeasureByTick(
            score, Fraction::fromTicks(r.startTick));
        const MeasureTickInfo endMti = locateMeasureByTick(
            score, Fraction::fromTicks(r.endTick));

        const int startTickInMsr = r.startTick
            - (startMti.measure ? startMti.measure->tick().ticks() : 0);
        const int endTickInMsr = r.endTick
            - (endMti.measure ? endMti.measure->tick().ticks() : 0);

        const int startBeatInt = 1 + startTickInMsr / Constants::DIVISION;
        std::string beatRange;
        if (!startMti.measure) {
            beatRange = "?";
        } else {
            const int msrDuration = startMti.measure->ticks().ticks();
            const int endTickInStartMsr =
                (endMti.measure && startMti.number == endMti.number)
                ? endTickInMsr : msrDuration;
            if (endTickInStartMsr >= msrDuration) {
                beatRange = std::to_string(startBeatInt) + "-end";
            } else {
                const int endBeatInt = 1 + endTickInStartMsr / Constants::DIVISION;
                beatRange = std::to_string(startBeatInt) + "-" + std::to_string(endBeatInt);
            }
        }

        const std::string chordLabel = analysis::ChordSymbolFormatter::formatSymbol(
            r.chord, r.key.keySignatureFifths);

        // Alternatives deduped against the primary and against each other.
        QJsonArray altArray;
        {
            std::set<std::string> seen;
            seen.insert(chordLabel);
            for (const auto& alt : r.alternatives) {
                const std::string altSym = analysis::ChordSymbolFormatter::formatSymbol(
                    alt, r.key.keySignatureFifths);
                if (!seen.count(altSym)) {
                    altArray.append(QString::fromStdString(altSym));
                    seen.insert(altSym);
                }
            }
        }

        // tones_pc_set: sounding pitches sorted by MIDI pitch.
        std::string pcSet;
        {
            std::vector<std::pair<int, int>> pitchTpc;
            for (const auto& t : r.tones) pitchTpc.push_back({ t.pitch, t.tpc });
            std::sort(pitchTpc.begin(), pitchTpc.end());
            for (size_t pi = 0; pi < pitchTpc.size(); ++pi) {
                if (pi > 0) pcSet += " ";
                pcSet += pitchName(pitchTpc[pi].second, pitchTpc[pi].first);
            }
        }

        const double nc = r.chord.identity.normalizedConfidence;

        QJsonObject j;
        j["measure"]                  = startMti.number;
        j["beat_range"]               = QString::fromStdString(beatRange);
        j["tick_start"]               = r.startTick;
        j["tick_end"]                 = r.endTick;
        j["chord_label"]              = QString::fromStdString(chordLabel);
        j["chord_label_alternatives"] = altArray;
        j["key"]                      = QString::fromStdString(keyShortStr(r.key));
        j["mode"]                     = QString::fromStdString(keySigModeStr(r.key.mode));
        j["confidence"]               = QString::fromStdString(confidenceOrdinal(nc, r.hasAnalyzedChord));
        j["reasoning"]                = "Analyzer call from collected pitch-class set; no free-form rationale.";
        j["tones_pc_set"]             = QString::fromStdString(pcSet);
        judgments.append(j);
    }

    QJsonObject toolInput;
    toolInput["judgments"]       = judgments;
    toolInput["key_summary"]     = "";
    toolInput["ambiguity_flags"] = QJsonArray{};
    toolInput["format_friction"] = "";

    QJsonObject root;
    root["metadata"]   = metadata;
    root["tool_input"] = toolInput;

    out << QJsonDocument(root).toJson(QJsonDocument::Indented).constData();
}

// ══════════════════════════════════════════════════════════════════════════
// main
// ══════════════════════════════════════════════════════════════════════════

int main(int argc, char* argv[])
{
    QCoreApplication::setOrganizationName("MuseScore");
    QCoreApplication::setOrganizationDomain("musescore.org");
    QCoreApplication::setApplicationName("llm_triage");
    QGuiApplication app(argc, argv);

    const QStringList args = QCoreApplication::arguments();
    if (args.size() < 3) {
        std::cerr << "Usage: llm_triage <input_score_path> <output_dir>\n";
        return 1;
    }

    const muse::io::path_t inputPath = args.at(1);
    const QString outputDirQ = args.at(2);
    const QFileInfo inputInfo(args.at(1));
    const std::string sourceBasename = inputInfo.fileName().toStdString();
    const std::string sourcePath     = inputInfo.absoluteFilePath().toStdString();

    // Derive output filename prefix (basename without extension).
    std::string prefix = inputInfo.completeBaseName().toStdString();

    initModules();

    MasterScore* score = loadScore(inputPath);
    if (!score) {
        std::cerr << "ERROR: failed to load score: " << sourcePath << "\n";
#ifdef _WIN32
        ::TerminateProcess(::GetCurrentProcess(), 1);
#endif
        std::_Exit(1);
    }
    std::cout << "loaded: " << sourcePath << "\n";

    // Build exclude-staves set.
    std::set<size_t> excludeStaves;
    for (size_t si = 0; si < score->nstaves(); ++si) {
        if (!staffIsEligible(score, si)) excludeStaves.insert(si);
    }
    const size_t eligible = score->nstaves() - excludeStaves.size();
    std::cout << "staves: " << eligible << "/" << score->nstaves() << "\n";

    // SHA-256 of the raw score file bytes (used in analyzer JSON metadata).
    std::string scoreContentHash;
    {
        QFile f(args.at(1));
        if (f.open(QIODevice::ReadOnly)) {
            scoreContentHash = QCryptographicHash::hash(
                f.readAll(), QCryptographicHash::Sha256).toHex().toStdString();
        }
    }

    // Analyze.
    const std::vector<AnalyzedRegion> regions = analyzeScore(score, excludeStaves);
    std::cout << "regions: " << regions.size() << "\n";

    // Ensure output directory exists.
    const QDir outDir(outputDirQ);
    if (!outDir.exists()) {
        if (!QDir().mkpath(outputDirQ)) {
            std::cerr << "ERROR: cannot create output directory: "
                      << outputDirQ.toStdString() << "\n";
            delete score;
#ifdef _WIN32
            ::TerminateProcess(::GetCurrentProcess(), 1);
#endif
            std::_Exit(1);
        }
    }

    auto openOut = [&](const std::string& suffix) -> std::ofstream {
        const std::string path = outputDirQ.toStdString() + "/" + prefix + "." + suffix;
        std::ofstream f(path);
        if (!f.is_open()) {
            std::cerr << "ERROR: cannot open output file: " << path << "\n";
        }
        return f;
    };

    // File 1: notes_only
    {
        std::ofstream f = openOut("notes_only.txt");
        if (f.is_open()) {
            emitHeader(f, sourceBasename, sourcePath, "notes_only", score);
            emitNoteLines(f, score, excludeStaves, /*includeSymbols=*/false);
        }
    }

    // File 2: with_symbols
    {
        std::ofstream f = openOut("with_symbols.txt");
        if (f.is_open()) {
            emitHeader(f, sourceBasename, sourcePath, "with_symbols", score);
            emitNoteLines(f, score, excludeStaves, /*includeSymbols=*/true);
        }
    }

    // File 3: analyzer_output
    {
        std::ofstream f = openOut("analyzer_output.txt");
        if (f.is_open()) {
            emitHeader(f, sourceBasename, sourcePath, "analyzer_output", score);
            emitAnalyzerOutput(f, regions, score);
        }
    }

    // File 4: analyzer_response (JSON, parallel to LLM provider responses)
    {
        std::ofstream f = openOut("analyzer_response.json");
        if (f.is_open()) {
            emitAnalyzerJson(f, prefix, sourcePath, scoreContentHash, regions, score);
        }
    }

    delete score;
    std::cout.flush();
    std::cerr.flush();
    // Skip static-module destructor sequence (crashes on Windows TLS shutdown).
    // Same workaround as tools/batch_analyze.cpp.
#ifdef _WIN32
    ::TerminateProcess(::GetCurrentProcess(), 0);
#endif
    std::_Exit(0);
}
