// SPDX-License-Identifier: GPL-3.0-only
// MuseScore-Studio-CLA-applies
//
// batch_analyze.cpp — Headless harmonic analysis tool
//
// Loads a MusicXML (or MSCZ/MSCX) file, runs our harmonic analysis pipeline
// (HarmonicRhythm / ChordAnalyzer / KeyModeAnalyzer) without any UI context,
// and writes JSON results to stdout or a file.
//
// Initialization follows the same pattern as src/engraving/tests/environment.cpp
// and src/importexport/musicxml/tests/environment.cpp.
//
// Usage:
//   batch_analyze <input.[xml|musicxml|mxl|mscz|mscx]> [output.json]
//                [--preset Standard|Jazz|Modal|Baroque|Contemporary]
//                [--dump-regions batch|notation|notation-premerge]
//   batch_analyze --help

#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <optional>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <limits>
#include <map>
#include <memory>
#include <set>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

// ── Qt ─────────────────────────────────────────────────────────────────────
#include <QGuiApplication>
#include <QFile>
#include <QFileInfo>
#include <QIODevice>

#ifdef _WIN32
extern "C" __declspec(dllimport) void* __stdcall GetCurrentProcess(void);
extern "C" __declspec(dllimport) int __stdcall TerminateProcess(void* hProcess, unsigned int uExitCode);
#endif

// ── Muse framework ─────────────────────────────────────────────────────────
#include "global/globalmodule.h"
#include "draw/internal/ifontsdatabase.h"
#include "global/iapplication.h"
#include "global/modularity/ioc.h"
#include "global/modularity/imodulesetup.h"
#include "global/io/path.h"
#include "global/types/string.h"
#include "global/types/ret.h"
#include "global/tests/mocks/applicationstub.h"

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
#include "engraving/compat/scoreaccess.h"
#include "engraving/compat/mscxcompat.h"
#include "engraving/infrastructure/localfileinfoprovider.h"
#include "engraving/types/constants.h"

// ── MusicXML import ────────────────────────────────────────────────────────
#include "importexport/musicxml/musicxmlmodule.h"
#include "importexport/musicxml/internal/import/importmusicxml.h"

// ── Analysis ───────────────────────────────────────────────────────────────
#include "composing/analysis/chord/chordanalyzer.h"
#include "composing/analysis/key/keymodeanalyzer.h"
#include "composing/analysis/key/modepriorpresets.h"
#include "composing/analysis/chord/analysisutils.h"
#include "composing/analysis/harmony/harmonicsegmenter.h"
#include "composing/analysis/scoreharvest/metricweights.h"
#include "notation/internal/notationanalysisinternal.h"
#include "notation/internal/notationcomposingbridge.h"
#include "notation/internal/notationcomposingbridgehelpers.h"

// ── Namespace aliases ──────────────────────────────────────────────────────
using namespace mu::engraving;
namespace analysis = mu::composing::analysis;
namespace shv = mu::composing::analysis::scoreharvest;
using analysis::ChordAnalysisTone;
using analysis::ChordAnalysisResult;
using analysis::ChordQuality;
using analysis::ChordTemporalContext;
using analysis::isDiatonicStep;
using analysis::inferNextRootPc;
using analysis::advanceTemporalContext;
using analysis::KeyModeAnalysisResult;
// Note: analysis::KeySigMode and mu::engraving::KeyMode are both in scope;
//       always qualify as analysis::KeySigMode to avoid ambiguity.

// ══════════════════════════════════════════════════════════════════════════
// JSON helpers
// ══════════════════════════════════════════════════════════════════════════

static std::string jsonEscape(const std::string& s)
{
    std::string r;
    r.reserve(s.size() + 8);
    for (unsigned char c : s) {
        switch (c) {
        case '"':  r += "\\\""; break;
        case '\\': r += "\\\\"; break;
        case '\n': r += "\\n";  break;
        case '\r': r += "\\r";  break;
        case '\t': r += "\\t";  break;
        default:
            if (c < 0x20) {
                char buf[8];
                std::snprintf(buf, sizeof(buf), "\\u%04x", c);
                r += buf;
            } else {
                r += static_cast<char>(c);
            }
        }
    }
    return r;
}

static std::string fmtDouble(double v, int precision = 6)
{
    // Print with up to `precision` significant digits, strip trailing zeros
    char buf[64];
    std::snprintf(buf, sizeof(buf), "%.*g", precision, v);
    return buf;
}

// ══════════════════════════════════════════════════════════════════════════
// Mode prior preset application
//
// Preset values are owned by mu::composing::modePriorPresets() in
// composing_analysis (see composing/analysis/key/modepriorpresets.cpp).
// This used to inline the same 5x21 table — see docs/duplication_audit.md §5.8.
// ══════════════════════════════════════════════════════════════════════════

/// Apply a named mode prior preset to @p prefs.
/// Returns true on success; false if @p name is not a known preset.
/// Valid names: "Standard", "Jazz", "Modal", "Baroque", "Contemporary".
static bool applyPreset(const std::string& name,
                        analysis::KeyModeAnalyzerPreferences& prefs)
{
    for (const auto& p : mu::composing::modePriorPresets()) {
        if (p.name != name) continue;
        prefs.modePriorIonian           = p.ionian;
        prefs.modePriorDorian           = p.dorian;
        prefs.modePriorPhrygian         = p.phrygian;
        prefs.modePriorLydian           = p.lydian;
        prefs.modePriorMixolydian       = p.mixolydian;
        prefs.modePriorAeolian          = p.aeolian;
        prefs.modePriorLocrian          = p.locrian;
        prefs.modePriorMelodicMinor     = p.melodicMinor;
        prefs.modePriorDorianB2         = p.dorianB2;
        prefs.modePriorLydianAugmented  = p.lydianAugmented;
        prefs.modePriorLydianDominant   = p.lydianDominant;
        prefs.modePriorMixolydianB6     = p.mixolydianB6;
        prefs.modePriorAeolianB5        = p.aeolianB5;
        prefs.modePriorAltered          = p.altered;
        prefs.modePriorHarmonicMinor    = p.harmonicMinor;
        prefs.modePriorLocrianSharp6    = p.locrianSharp6;
        prefs.modePriorIonianSharp5     = p.ionianSharp5;
        prefs.modePriorDorianSharp4     = p.dorianSharp4;
        prefs.modePriorPhrygianDominant = p.phrygianDominant;
        prefs.modePriorLydianSharp2     = p.lydianSharp2;
        prefs.modePriorAlteredDomBB7    = p.alteredDomBB7;
        return true;
    }
    return false;
}

// ══════════════════════════════════════════════════════════════════════════
// Module initialization
// Replicates the sequence performed by muse::testing::SuiteEnvironment:
//   registerResources → registerExports → resolveImports →
//   onPreInit → onInit → onAllInited → onStartApp
// (with loadInstrumentTemplates inserted after onInit as in environment.cpp)
// ══════════════════════════════════════════════════════════════════════════

static void initModules()
{
    using namespace muse;
    using namespace muse::modularity;

    // Follows the initialization sequence from muse/framework/testing/environment.cpp
    // (Environment::setup).  An IApplication implementation must be registered
    // with globalIoc() before any module init — modules resolve it via inject<>.
    // (setApplication() was removed upstream in muse_framework commit 9c9cd29255.)
    // loadInstrumentTemplates() runs last (post-onStartApp), matching the
    // engraving test environment's postInit callback pattern.
    const IApplication::RunMode mode = IApplication::RunMode::GuiApp;

    muse::modularity::globalIoc()->registerExport<IApplication>("batch_analyze",
        new muse::ApplicationStub());

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

    // Must run after onStartApp() — instrument templates depend on fully-initialized engraving.
    loadInstrumentTemplates(":/engraving/instruments/instruments.xml");
}

// ══════════════════════════════════════════════════════════════════════════
// Score loading
// ══════════════════════════════════════════════════════════════════════════

/// Loads a score file (.xml / .musicxml / .mxl / .mscz / .mscx).
/// Returns a heap-allocated MasterScore on success; caller owns the pointer.
/// Returns nullptr on failure.
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
        const Err rv = mu::iex::musicxml::importMusicXml(
            score, scorePath, /*forceMode=*/true);
        ok = (rv == Err::NoError);
    } else if (ext == "mxl") {
        const Err rv = mu::iex::musicxml::importCompressedMusicXml(
            score, scorePath, /*forceMode=*/true);
        ok = (rv == Err::NoError);
    } else {
        // MSCZ or MSCX
        const muse::Ret rv = compat::loadMsczOrMscx(
            score, ioPath, /*ignoreVersionError=*/false);
        ok = static_cast<bool>(rv);
    }

    if (!ok) {
        delete score;
        return nullptr;
    }

    // Headless harmonic analysis uses logical score structure only. Forcing a
    // full layout here can overflow caches on some legacy native MSCX imports
    // even though no downstream batch-analysis step needs rendered geometry.
    score->setPlaylistDirty();
    return score;
}

// ══════════════════════════════════════════════════════════════════════════
// Staff eligibility
// Matches staffIsEligible() in src/notation/internal/notationcomposingbridge.cpp
// ══════════════════════════════════════════════════════════════════════════

/// Returns true if the part name contains "chord" (case-insensitive),
/// indicating this is our synthetic chord staff.
static bool isChordTrackStaff(const Staff* staff)
{
    if (!staff || !staff->part()) return false;
    const std::string name = staff->part()->partName().toStdString();
    std::string lower = name;
    std::transform(lower.begin(), lower.end(), lower.begin(),
                   [](unsigned char c) { return static_cast<char>(std::tolower(c)); });
    return lower.find("chord") != std::string::npos;
}

/// Returns true if the staff should be included in harmonic analysis:
/// visible, not percussion, not a chord track.
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

static size_t referenceStaffForAnalysis(const Score* score,
                                        const std::set<size_t>& excludeStaves)
{
    for (size_t staffIndex = 0; staffIndex < score->nstaves(); ++staffIndex) {
        if (!excludeStaves.count(staffIndex) && staffIsEligible(score, staffIndex)) {
            return staffIndex;
        }
    }
    return 0;
}

// ══════════════════════════════════════════════════════════════════════════
// Tone extraction
// ══════════════════════════════════════════════════════════════════════════

/// Computes a 12-bit pitch-class bitmask from the given tones.
static uint16_t pitchClassMask(const std::vector<ChordAnalysisTone>& tones)
{
    uint16_t mask = 0;
    for (const auto& t : tones) {
        mask |= static_cast<uint16_t>(1u << (t.pitch % 12));
    }
    return mask;
}

// ══════════════════════════════════════════════════════════════════════════
// Per-region local key inference
//
// TODO(Rule 10): The batch-side helpers below mirror live bridge logic in
// notationcomposingbridgehelpers.cpp. Move shared note collection, boundary

struct MeasureTickInfo {
    const Measure* measure = nullptr;
    int number = 0;
};

static MeasureTickInfo locateMeasureByTick(const Score* score, const Fraction& tick)
{
    if (!score) {
        return {};
    }

    int nextMeasureNumber = 0;
    const Measure* lastMeasure = nullptr;
    for (const Measure* measure = score->firstMeasure(); measure; measure = measure->nextMeasure()) {
        nextMeasureNumber += measure->measureNumberOffset();
        const int displayedMeasureNumber = nextMeasureNumber + 1;
        lastMeasure = measure;

        if (tick >= measure->tick() && tick < measure->endTick()) {
            return { measure, displayedMeasureNumber };
        }

        if (!measure->excludeFromNumbering()) {
            ++nextMeasureNumber;
        }

        const LayoutBreak* layoutBreak = measure->sectionBreakElement();
        if (layoutBreak && layoutBreak->startWithMeasureOne()) {
            nextMeasureNumber = 0;
        }
    }

    if (lastMeasure && tick == score->endTick()) {
        return locateMeasureByTick(score, lastMeasure->tick());
    }

    return {};
}
// detection, key resolution, and temporal-context code into src/composing/
// so the bridge and batch_analyze call one implementation. See
// ARCHITECTURE.md §2.10 and §4.1c.
//
// Mirrors the windowed pitch collection in notationcomposingbridge.cpp:
//   - 16 beats lookback, 8 beats lookahead
//   - Exponential time decay (0.7× per measure) for lookback notes
//   - Lookahead notes at 0.5× weight
//   - Beat-type weights from TimeSigFrac::rtick2beatType
//   - Two-pass per segment (lowest pitch first, then isBass assignment)
//   - Key signature fifths read from staff 0 at the analysis tick
// ══════════════════════════════════════════════════════════════════════════

// Constants and trivial helpers moved to composing/analysis/scoreharvest/metricweights.h.
// See docs/duplication_audit.md §5.8.  These thin file-scope aliases keep the existing
// call sites below readable without re-typing the namespace at every reference.

using shv::LOOKBACK_BEATS;
using shv::LOOKAHEAD_BEATS;
using shv::LOOKAHEAD_WEIGHT;
using shv::DECAY_RATE;
using shv::beatTypeToWeight;
using shv::safeBeatType;
using shv::regionMetricWeightForBeatType;
using shv::distinctPitchClasses;

// timeDecay defaults to DECAY_RATE in the shared header.
static inline double timeDecay(double beatsAgo)
{
    return shv::timeDecay(beatsAgo);
}

/// Collect pitch context for [windowStart, windowEnd] around @p tick.
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
         s = s->next1(SegmentType::ChordRest))
    {
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

/// Infer key/mode at @p tick using the same windowed approach as the bridge.
/// The selected reference staff supplies the key signature at @p tick.
/// @param prevResult  Previous inference for hysteresis.  Pass nullptr at the
///                    first region (no incumbent mode yet).
/// @param keyPrefs    KeyModeAnalyzerPreferences to use (e.g. a specific preset).
///
/// Returns up to 3 ranked key/mode candidates.  [0] is the winner (after
/// applying hysteresis); [1] and [2] are the next-best alternatives from
/// analyzeKeyMode(), useful for diagnosing near-ties and confidence levels.
static std::vector<KeyModeAnalysisResult> inferLocalKey(
    Score* score,
    size_t keySigStaffIdx,
    const std::set<size_t>& excludeStaves,
    const Fraction& tick,
    const KeyModeAnalysisResult* prevResult = nullptr,
    const analysis::KeyModeAnalyzerPreferences& keyPrefs = analysis::KeyModeAnalyzerPreferences{})
{
    const size_t clampedStaffIdx = std::min(keySigStaffIdx, score->nstaves() - 1);
    const KeySigEvent keySig = score->staff(clampedStaffIdx)->keySigEvent(tick);
    const int keyFifths = static_cast<int>(keySig.concertKey());

    // Declared mode from key signature.
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

    // Fixed lookback; lookahead expands dynamically until confident.
    const Fraction lookbackDuration = Fraction(LOOKBACK_BEATS, 4);
    const Fraction windowStart = (tick > lookbackDuration)
                                 ? tick - lookbackDuration
                                 : Fraction(0, 1);

    // Piece-start shortcut: no lookback + no previous result + declared mode
    // → trust the key signature declaration rather than thin lookahead evidence.
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

        results = analysis::KeyModeAnalyzer::analyzeKeyMode(
            ctx, keyFifths, keyPrefs, declaredMode);

        const bool confident = !results.empty()
            && results.front().normalizedConfidence
               >= keyPrefs.dynamicLookaheadConfidenceThreshold;
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

    // Build top-3 list from raw results (before hysteresis adjustment).
    std::vector<KeyModeAnalysisResult> topN(
        results.begin(),
        results.begin() + std::min(results.size(), static_cast<size_t>(3)));

    // Hysteresis: require a score margin to switch away from the previous mode.
    // Same-key-signature switches (relative major/minor) use a higher margin
    // because the shared diatonic pool makes them structurally ambiguous.
    if (!results.empty() && prevResult != nullptr
        && results.front().mode != prevResult->mode) {
        const double hysteresis = (results.front().keySignatureFifths == prevResult->keySignatureFifths)
                                  ? keyPrefs.relativeKeyHysteresisMargin
                                  : keyPrefs.hysteresisMargin;
        if (results.front().score < prevResult->score + hysteresis) {
            for (const auto& r : results) {
                if (r.mode == prevResult->mode
                    && r.keySignatureFifths == prevResult->keySignatureFifths) {
                    // Incumbent wins via hysteresis.  Return [incumbent, original top-N sans incumbent].
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
            // Incumbent not in candidate list — fall through.
        }
    }

    if (!topN.empty()) {
        return topN;
    }

    // Fallback: key signature fifths, Ionian
    KeyModeAnalysisResult fallback;
    fallback.keySignatureFifths   = keyFifths;
    fallback.mode                 = analysis::KeySigMode::Ionian;
    fallback.tonicPc              = analysis::ionianTonicPcFromFifths(keyFifths);
    fallback.score                = 0.0;
    fallback.normalizedConfidence = 0.0;
    return { fallback };
}

// ══════════════════════════════════════════════════════════════════════════
// Harmonic region detection and analysis
// Implements the same algorithm as analyzeHarmonicRhythm() in
// src/notation/internal/notationcomposingbridge.cpp, without depending on
// the notation module.  This simplified version omits the backward-lookback
// for sustained notes (adequate for chorales, where most pitches attack
// simultaneously) but keeps the short-region absorption pass.
// ══════════════════════════════════════════════════════════════════════════

struct AnalyzedRegion {
    int startTick;
    int endTick;
    int measureNumber;
    double beat;             // 1-indexed beat within measure, in quarter-note units
    ChordAnalysisResult chord;
    bool hasAnalyzedChord = true;
    std::vector<ChordAnalysisResult> alternatives;  // up to 2 additional candidates
    KeyModeAnalysisResult key;                      // winning key/mode (== keyRanked[0])
    std::vector<KeyModeAnalysisResult> keyRanked;   // top 3 key/mode candidates from analyzeKeyMode()
    std::vector<ChordAnalysisTone> tones;
    uint16_t pcMask = 0;   // 12-bit pitch-class bitmask of sounding notes
    int bassPc = -1;       // pitch class of the lowest-sounding note
};

enum class RegionDumpMode {
    Batch,
    Notation,
    NotationPreMerge,
};

struct RegionDumpBundle {
    std::vector<AnalyzedRegion> finalRegions;
    std::vector<AnalyzedRegion> preMergeRegions;
    std::vector<AnalyzedRegion> postMergeRegions;
};

static const char* regionDumpModeName(RegionDumpMode mode)
{
    switch (mode) {
    case RegionDumpMode::Batch:               return "batch";
    case RegionDumpMode::Notation:            return "notation";
    case RegionDumpMode::NotationPreMerge:    return "notation-premerge";
    }
    return "batch";
}

// ── Shared tone-collection functions ──────────────────────────────────────────
// The five functions below (collectRegionTones, detectBassMovementSubBoundaries,
// SoundingNote, collectSoundingAt, buildTones, findTemporalContext) have been
// consolidated into the canonical implementations in:
//   src/notation/internal/notationcomposingbridgehelpers.{h,cpp}
//
// batch_analyze links against 'notation' and includes the header above, so
// these are now thin aliases/using declarations into that namespace.
// See docs/duplication_audit.md §5.8 (Step 3).

using mu::notation::internal::SoundingNote;
using mu::notation::internal::collectSoundingAt;
using mu::notation::internal::buildTones;
using mu::notation::internal::collectRegionTones;
using mu::notation::internal::detectBassMovementSubBoundaries;
using mu::notation::internal::findTemporalContext;


using mu::composing::PlacedRegion;
using mu::composing::HarmonicSegmenterCallbacks;
using mu::composing::greedyExpandSegmentation;
using mu::composing::placedRegionsToTicks;

/// Forward declaration — defined later in this file.
static const char* qualityToString(ChordQuality q);

static std::vector<AnalyzedRegion> analyzeScore(
    Score* score,
    const std::set<size_t>& excludeStaves,
    const analysis::KeyModeAnalyzerPreferences& keyPrefs = analysis::KeyModeAnalyzerPreferences{},
    const analysis::ChordAnalyzerPreferences& chordPrefs = analysis::kDefaultChordAnalyzerPreferences)
{
    const Segment* firstSegment = score->tick2segment(Fraction(0, 1), true, SegmentType::ChordRest);
    if (!firstSegment) {
        return {};
    }

    const Fraction startTick = firstSegment->tick();
    const Fraction endTick = score->endTick();
    std::vector<AnalyzedRegion> result;

    const size_t refStaff = referenceStaffForAnalysis(score, excludeStaves);
    const auto initialKey = inferLocalKey(score, refStaff, excludeStaves, startTick, nullptr, keyPrefs)[0];
    const auto chordAnalyzer = analysis::ChordAnalyzerFactory::create();

    // Iter 54: greedy-expand segmentation (Task #62).
    HarmonicSegmenterCallbacks segCallbacks;
    segCallbacks.staffIsEligible = [score](size_t staffIdx) {
        return staffIsEligible(score, staffIdx);
    };
    segCallbacks.collectRegionTones = [score, &excludeStaves](int s, int e) {
        return collectRegionTones(score, s, e, excludeStaves, -1, true);
    };
    auto greedyRegions = greedyExpandSegmentation(
        score, startTick, endTick, excludeStaves, chordPrefs,
        chordAnalyzer.get(), initialKey.keySignatureFifths, initialKey.mode,
        segCallbacks);
    // Iter 83: port Iter 77 Fix B from notationharmonicrhythmbridge.cpp.
    // placedRegionsToTicks() returns only START ticks; emitting each placed
    // region's END tick as well keeps confident Round 1 anchors intact when
    // followed by an unplaced gap (otherwise the bridge/batch builds one wide
    // region spanning [anchorStart, gapEnd) and re-analysis can flip the
    // reading).
    std::vector<Fraction> boundaryTicks;
    {
        std::set<int> boundaryTickSet;
        for (const auto& pr : greedyRegions) {
            if (pr.round >= 1) {
                boundaryTickSet.insert(pr.startTick);
                boundaryTickSet.insert(pr.endTick);
            }
        }
        for (int t : boundaryTickSet) {
            if (t >= startTick.ticks() && t < endTick.ticks()) {
                boundaryTicks.push_back(Fraction::fromTicks(t));
            }
        }
        if (boundaryTicks.empty()) {
            boundaryTicks.push_back(startTick);
        }
    }

    // Iter 93: preserve pre-Pass-2b parent boundaries so the main analyzeChord
    // loop can compute onsetAtRegionStart at full-region scope (against the
    // parent's startTick, not the sub-region's). Indexed by tick value; the
    // parent for a given sub-region is the largest entry ≤ sub-region start.
    std::set<int> parentBoundaryTicks;
    for (const Fraction& t : boundaryTicks) {
        parentBoundaryTicks.insert(t.ticks());
    }

    // Iter 94 — pre-compute each parent region's bass PC (lowest qualifying
    // tone over the whole parent span) so the main loop can supply parent-
    // scope previousBassPc / nextBassPc to analyzeChord for w_stepIn /
    // w_stepOut.  Without this override, sub-region calls would see adjacent
    // sub-region neighbors' bass values — the scope mismatch behind the Iter
    // 92 Step 3c +5 Baroque BIR=false regression.
    std::unordered_map<int, int> parentBassPcMap;
    {
        std::vector<int> sortedParentTicks(parentBoundaryTicks.begin(),
                                           parentBoundaryTicks.end());
        for (size_t pi = 0; pi < sortedParentTicks.size(); ++pi) {
            const int pStart = sortedParentTicks[pi];
            const int pEnd = (pi + 1 < sortedParentTicks.size())
                             ? sortedParentTicks[pi + 1] : endTick.ticks();
            const auto pTones = collectRegionTones(
                score, pStart, pEnd, excludeStaves, pStart, true);
            int pBassPc = -1;
            for (const auto& t : pTones) {
                if (t.isBass) { pBassPc = ((t.pitch % 12) + 12) % 12; break; }
            }
            parentBassPcMap[pStart] = pBassPc;
        }
    }

    // Pass 2b: expand coarse regions with bass-movement sub-boundaries.
    // Detects regions where the pitch-class set is identical across the region but
    // the bass note changes (e.g. Eye of the Hurricane m.1: F-bass → Bb-bass with
    // the same {C,D,F,G,Bb} pitch-class set).  ANY bass PC change fires; downstream
    // chord analysis (bassPassingToneMinWeightFraction) handles passing tones.
    {
        constexpr int kPass2bMinRegionTicks = shv::kPass2bMinRegionTicks;
        std::vector<Fraction> expandedTicks;
        expandedTicks.reserve(boundaryTicks.size() * 2);
        for (size_t bi = 0; bi < boundaryTicks.size(); ++bi) {
            expandedTicks.push_back(boundaryTicks[bi]);
            const Fraction regionStart = boundaryTicks[bi];
            const Fraction regionEnd = (bi + 1 < boundaryTicks.size())
                                       ? boundaryTicks[bi + 1] : endTick;
            if ((regionEnd - regionStart).ticks() >= kPass2bMinRegionTicks) {
                const auto subs = detectBassMovementSubBoundaries(
                    score, regionStart, regionEnd, excludeStaves);
                for (const Fraction& t : subs) {
                    expandedTicks.push_back(t);
                }
            }
        }
        boundaryTicks = std::move(expandedTicks);
    }

    result.reserve(boundaryTicks.size());

    ChordTemporalContext ctx = findTemporalContext(
        score, firstSegment, excludeStaves, initialKey.keySignatureFifths, initialKey.mode, -1);

    // Temporal context accumulation state — carried across iterations.
    int runningStepwiseCount = 0;                            // consecutive stepwise bass count
    std::array<int, 3> recentRootsBuf = {-1, -1, -1};       // rolling 3-region root window

    // Hysteresis: track the previous key result across regions.
    std::optional<KeyModeAnalysisResult> prevKey;

    for (size_t boundaryIndex = 0; boundaryIndex < boundaryTicks.size(); ++boundaryIndex) {
        const Fraction regionStart = boundaryTicks[boundaryIndex];
        const Fraction regionEnd = (boundaryIndex + 1 < boundaryTicks.size()) ? boundaryTicks[boundaryIndex + 1] : endTick;
        // Iter 93: resolve parent-region startTick for onsetAtRegionStart.
        // Largest pre-Pass-2b boundary ≤ regionStart.
        int parentStartTick = regionStart.ticks();
        {
            auto it = parentBoundaryTicks.upper_bound(regionStart.ticks());
            if (it != parentBoundaryTicks.begin()) {
                --it;
                parentStartTick = *it;
            }
        }
        auto tones = collectRegionTones(score,
                                        regionStart.ticks(),
                                        regionEnd.ticks(),
                                        excludeStaves,
                                        parentStartTick,
                                        true);
        if (tones.empty()) {
            continue;
        }

        const MeasureTickInfo regionMeasure = locateMeasureByTick(score, regionStart);
        const Measure* measure = regionMeasure.measure;
        if (!measure) {
            continue;
        }

        int currentBassPc = -1;
        for (const auto& tone : tones) {
            if (tone.isBass) {
                currentBassPc = tone.pitch % 12;
                break;
            }
        }
        ctx.bassIsStepwiseFromPrevious = (ctx.previousBassPc != -1 && currentBassPc != -1)
            && isDiatonicStep(ctx.previousBassPc, currentBassPc);

        // Infer key using the same windowed approach as the bridge.
        // Pass the previous result for hysteresis (nullptr on the first region).
        const std::vector<KeyModeAnalysisResult> keyRanked = inferLocalKey(
            score, refStaff, excludeStaves, regionStart,
            prevKey.has_value() ? &prevKey.value() : nullptr,
            keyPrefs);
        const KeyModeAnalysisResult& localKey = keyRanked[0];
        prevKey = localKey;

        // Look-ahead: collect next region's tones for nextBassPc and nextRootPc.
        // nextRootPc uses the current region's key as a lightweight approximation.
        int nextBassPc = -1;
        ctx.nextRootPc = -1;
        ctx.nextBassPc = -1;
        if (boundaryIndex + 1 < boundaryTicks.size()) {
            const Fraction nextRegionStart = boundaryTicks[boundaryIndex + 1];
            const Fraction nextRegionEnd = (boundaryIndex + 2 < boundaryTicks.size())
                                           ? boundaryTicks[boundaryIndex + 2]
                                           : endTick;
            int nextParentStartTick = nextRegionStart.ticks();
            {
                auto it = parentBoundaryTicks.upper_bound(nextRegionStart.ticks());
                if (it != parentBoundaryTicks.begin()) {
                    --it;
                    nextParentStartTick = *it;
                }
            }
            const auto nextTones = collectRegionTones(score,
                                                      nextRegionStart.ticks(),
                                                      nextRegionEnd.ticks(),
                                                      excludeStaves,
                                                      nextParentStartTick,
                                                      true);
            for (const auto& tone : nextTones) {
                if (tone.isBass) {
                    nextBassPc = tone.pitch % 12;
                    break;
                }
            }
            ctx.nextRootPc = inferNextRootPc(
                chordAnalyzer.get(), nextTones,
                localKey.keySignatureFifths, localKey.mode, chordPrefs);
        }
        ctx.bassIsStepwiseToNext = (currentBassPc != -1 && nextBassPc != -1)
            && isDiatonicStep(currentBassPc, nextBassPc);
        ctx.nextBassPc = nextBassPc;

        // Iter 94 — override previousBassPc / nextBassPc to parent scope for
        // w_stepIn / w_stepOut.  Computed AFTER the stepwise booleans (which
        // intentionally use sub-region scope: passing-tone / inversion
        // signals are local) and BEFORE analyzeChord.  The next iteration's
        // ctx.previousBassPc is restored by advanceTemporalContext below.
        int parentPredBassPc = -1;
        int parentSuccBassPc = -1;
        {
            auto pIt = parentBoundaryTicks.lower_bound(parentStartTick);
            if (pIt != parentBoundaryTicks.begin()) {
                auto prevIt = pIt;
                --prevIt;
                auto m = parentBassPcMap.find(*prevIt);
                if (m != parentBassPcMap.end()) parentPredBassPc = m->second;
            }
            auto nIt = parentBoundaryTicks.upper_bound(parentStartTick);
            if (nIt != parentBoundaryTicks.end()) {
                auto m = parentBassPcMap.find(*nIt);
                if (m != parentBassPcMap.end()) parentSuccBassPc = m->second;
            }
        }
        const int savedPrevBassPc = ctx.previousBassPc;
        ctx.previousBassPc = parentPredBassPc;
        ctx.nextBassPc     = parentSuccBassPc;

        auto candidates = chordAnalyzer->analyzeChord(
            tones, localKey.keySignatureFifths, localKey.mode, &ctx, chordPrefs);

        // Restore sub-region-scope previousBassPc; advanceTemporalContext will
        // overwrite it shortly anyway, but keep the invariant clean.
        ctx.previousBassPc = savedPrevBassPc;

        if (candidates.empty()) {
            continue;
        }

        // Compute pitch-class metadata from tones.
        const uint16_t pcMask = pitchClassMask(tones);
        const int bassPc = currentBassPc;

        advanceTemporalContext(ctx, runningStepwiseCount, recentRootsBuf,
                               candidates[0].identity);

        if (!result.empty()
            && result.back().chord.identity.rootPc == candidates[0].identity.rootPc
            && result.back().chord.identity.quality == candidates[0].identity.quality) {
            result.back().endTick = regionEnd.ticks();
            analysis::mergeChordAnalysisTones(result.back().tones, tones);
            result.back().pcMask |= pcMask;
            if (const auto* bassTone = analysis::bassToneFromTones(result.back().tones)) {
                result.back().bassPc = bassTone->pitch % 12;
                result.back().chord.identity.bassPc = bassTone->pitch % 12;
                result.back().chord.identity.bassTpc = bassTone->tpc;
            }
            continue;
        }

        AnalyzedRegion ar;
        ar.startTick     = regionStart.ticks();
        ar.endTick       = regionEnd.ticks();
        ar.measureNumber = regionMeasure.number;
        const int tickInMeasure = regionStart.ticks() - measure->tick().ticks();
        ar.beat          = 1.0 + static_cast<double>(tickInMeasure) / Constants::DIVISION;
        ar.chord         = candidates[0];
        ar.hasAnalyzedChord = true;
        ar.tones         = std::move(tones);
        ar.key           = localKey;
        ar.keyRanked     = keyRanked;
        ar.pcMask        = pcMask;
        ar.bassPc        = bassPc;

        // Up to 3 alternatives (indices 1, 2, 3 from analyzeChord)
        for (size_t candidateIndex = 1; candidateIndex < candidates.size() && candidateIndex <= 3; ++candidateIndex) {
            ar.alternatives.push_back(candidates[candidateIndex]);
        }

        result.push_back(std::move(ar));
    }

    if (result.empty()) {
        return {};
    }

    constexpr int minRegionTicks = shv::kMinRegionTicks;
    std::vector<AnalyzedRegion> filtered;
    filtered.reserve(result.size());
    filtered.push_back(std::move(result[0]));
    for (size_t regionIndex = 1; regionIndex < result.size(); ++regionIndex) {
        const int duration = result[regionIndex].endTick - result[regionIndex].startTick;
        if (duration < minRegionTicks) {
            filtered.back().endTick = result[regionIndex].endTick;
        } else {
            filtered.push_back(std::move(result[regionIndex]));
        }
    }

    // ── Iter 87 — post-merge bass-b7 promotion ───────────────────────────────
    // The same-root same-quality merge above keeps result.back()'s chord
    // identity but updates bassPc/bassTpc.  When a late-entering b7 in the bass
    // promotes a later sub-region to MinorSeventh (Iter 86 stamp inside
    // analyzeChord), the merge discards that candidate identity in favour of
    // the earlier sub-region's plain triad reading.  Re-apply the b7 promotion
    // on the merged region using the merged tones and final bass so the chord
    // symbol (Am7/G, Em7/D) reflects the slash bass that the analyzer already
    // emits via formatSymbol.
    for (AnalyzedRegion& r : filtered) {
        if (!r.hasAnalyzedChord) { continue; }
        const int rPc = r.chord.identity.rootPc;
        const int bPc = r.bassPc;
        if (bPc < 0 || bPc == rPc) { continue; }
        if (((bPc - rPc + 12) % 12) != 10) { continue; }
        const ChordQuality q = r.chord.identity.quality;
        if (q != ChordQuality::Major && q != ChordQuality::Minor) { continue; }
        if (analysis::hasExtension(r.chord.identity.extensions,
                                   analysis::Extension::MinorSeventh)) { continue; }
        if (analysis::hasExtension(r.chord.identity.extensions,
                                   analysis::Extension::MajorSeventh)) { continue; }

        double bassPcWeight = 0.0;
        for (const auto& t : r.tones) {
            const int tonePc = ((t.pitch % 12) + 12) % 12;
            if (tonePc == bPc) {
                bassPcWeight += std::max(0.1, t.weight);
            }
        }
        if (bassPcWeight > chordPrefs.extensionThreshold) {
            analysis::setExtension(r.chord.identity.extensions,
                                   analysis::Extension::MinorSeventh);
        }
    }

    return filtered;
}

static AnalyzedRegion convertNotationRegion(
    const analysis::HarmonicRegion& region,
    const Score* score)
{
    AnalyzedRegion converted;
    converted.startTick = region.startTick;
    converted.endTick = region.endTick;
    converted.chord = region.chordResult;
    converted.hasAnalyzedChord = region.hasAnalyzedChord;
    converted.key = region.keyModeResult;
    converted.tones = region.tones;
    converted.pcMask = pitchClassMask(converted.tones);
    converted.bassPc = region.chordResult.identity.bassPc;

    if (converted.bassPc < 0) {
        if (const auto* bassTone = analysis::bassToneFromTones(converted.tones)) {
            converted.bassPc = bassTone->pitch % 12;
        }
    }

    const MeasureTickInfo regionMeasure = score
        ? locateMeasureByTick(score, Fraction::fromTicks(region.startTick))
        : MeasureTickInfo{};
    const Measure* measure = regionMeasure.measure;
    if (measure) {
        converted.measureNumber = regionMeasure.number;
        const int tickInMeasure = region.startTick - measure->tick().ticks();
        converted.beat = 1.0 + static_cast<double>(tickInMeasure) / Constants::DIVISION;
    } else {
        converted.measureNumber = 0;
        converted.beat = 1.0;
    }

    return converted;
}

static std::vector<AnalyzedRegion> convertNotationRegions(
    const std::vector<analysis::HarmonicRegion>& regions,
    const Score* score)
{
    std::vector<AnalyzedRegion> converted;
    converted.reserve(regions.size());
    for (const auto& region : regions) {
        converted.push_back(convertNotationRegion(region, score));
    }
    return converted;
}

static RegionDumpBundle analyzeScoreNotation(
    Score* score,
    const std::set<size_t>& excludeStaves)
{
    RegionDumpBundle dump;

    const Segment* firstSegment = score->tick2segment(Fraction(0, 1), true, SegmentType::ChordRest);
    if (!firstSegment) {
        return dump;
    }

    const Fraction startTick = firstSegment->tick();
    const Fraction endTick = score->endTick();

    std::vector<analysis::HarmonicRegion> finalRegions;
    std::vector<analysis::HarmonicRegion> preMergeRegions;
    std::vector<analysis::HarmonicRegion> postMergeRegions;
    {
        mu::notation::internal::HarmonicRegionDebugCapture capture {
            &preMergeRegions,
            &postMergeRegions,
        };
        mu::notation::internal::ScopedHarmonicRegionDebugCapture scopedCapture(&capture);
        finalRegions = mu::notation::analyzeHarmonicRhythm(
            score,
            startTick,
            endTick,
            excludeStaves,
            mu::notation::HarmonicRegionGranularity::Smoothed);
    }

    dump.finalRegions = convertNotationRegions(finalRegions, score);
    dump.preMergeRegions = convertNotationRegions(preMergeRegions, score);
    dump.postMergeRegions = postMergeRegions.empty()
        ? dump.finalRegions
        : convertNotationRegions(postMergeRegions, score);
    return dump;
}

// ══════════════════════════════════════════════════════════════════════════
// Formatting helpers
// ══════════════════════════════════════════════════════════════════════════

static const char* qualityToString(ChordQuality q)
{
    switch (q) {
    case ChordQuality::Major:          return "Major";
    case ChordQuality::Minor:          return "Minor";
    case ChordQuality::Diminished:     return "Diminished";
    case ChordQuality::Augmented:      return "Augmented";
    case ChordQuality::HalfDiminished: return "HalfDiminished";
    case ChordQuality::Suspended2:     return "Suspended2";
    case ChordQuality::Suspended4:     return "Suspended4";
    case ChordQuality::Power:          return "Power";
    default:                           return "Unknown";
    }
}

static std::string keyName(int fifths, analysis::KeySigMode mode)
{
    return std::string(analysis::keyModeTonicName(fifths, mode))
         + analysis::keyModeSuffix(mode);
}

// ══════════════════════════════════════════════════════════════════════════
// JSON output
// ══════════════════════════════════════════════════════════════════════════

static void writeJson(
    const std::vector<AnalyzedRegion>& regions,
    const std::string& sourceName,
    const std::string& presetName,
    const KeyModeAnalysisResult& globalKey,
    const char* analysisPath,
    std::ostream& out)
{
    out << "{\n";
    out << "  \"source\": \""      << jsonEscape(sourceName)                                            << "\",\n";
    out << "  \"preset\": \""      << jsonEscape(presetName)                                            << "\",\n";
    out << "  \"analysisPath\": \"" << jsonEscape(analysisPath)                                          << "\",\n";
    out << "  \"detectedKey\": \"" << jsonEscape(keyName(globalKey.keySignatureFifths, globalKey.mode)) << "\",\n";
    out << "  \"keyConfidence\": " << fmtDouble(globalKey.normalizedConfidence)                         << ",\n";
    out << "  \"regions\": [\n";

    for (size_t i = 0; i < regions.size(); ++i) {
        const auto& r = regions[i];
        const bool isLast = (i + 1 == regions.size());

        const int rootPitchClass = r.hasAnalyzedChord ? r.chord.identity.rootPc : -1;
        const std::string chordSym = r.hasAnalyzedChord
            ? analysis::ChordSymbolFormatter::formatSymbol(r.chord, r.key.keySignatureFifths)
            : std::string();
        const std::string romanNum = r.hasAnalyzedChord
            ? analysis::ChordSymbolFormatter::formatRomanNumeral(r.chord)
            : std::string();
        const std::string regionKeyName = keyName(r.key.keySignatureFifths, r.key.mode);
        const double durationQn = static_cast<double>(r.endTick - r.startTick) / Constants::DIVISION;

        // Chord score and margin (winner score − best alternative score).
        const double chordScore  = r.chord.identity.score;
        const double chordMargin = r.alternatives.empty()
                                   ? 0.0
                                   : (chordScore - r.alternatives[0].identity.score);

        // Distinct pitch-class count from bitmask.
        int noteCount = 0;
        for (int bit = 0; bit < 12; ++bit) {
            if (r.pcMask & (static_cast<uint16_t>(1u) << bit)) ++noteCount;
        }

        const bool bassIsRoot = (r.hasAnalyzedChord && r.bassPc >= 0 && r.bassPc == r.chord.identity.rootPc);

        out << "    {\n";
        out << "      \"measureNumber\": "   << r.measureNumber                                      << ",\n";
        out << "      \"beat\": "            << fmtDouble(r.beat, 4)                                 << ",\n";
        out << "      \"startTick\": "       << r.startTick                                          << ",\n";
        out << "      \"endTick\": "         << r.endTick                                            << ",\n";
        out << "      \"duration\": "        << fmtDouble(durationQn, 6)                             << ",\n";
        out << "      \"rootPitchClass\": "  << rootPitchClass                                      << ",\n";
        out << "      \"quality\": \""       << qualityToString(r.chord.identity.quality)            << "\",\n";
        out << "      \"chordSymbol\": \""   << jsonEscape(chordSym)                                 << "\",\n";
        out << "      \"romanNumeral\": \""  << jsonEscape(romanNum)                                 << "\",\n";
        out << "      \"chordScore\": "      << fmtDouble(chordScore, 5)                             << ",\n";
        out << "      \"chordScoreMargin\": "<< fmtDouble(chordMargin, 5)                            << ",\n";
        out << "      \"key\": \""           << jsonEscape(regionKeyName)                            << "\",\n";
        out << "      \"keyConfidence\": "   << fmtDouble(r.key.normalizedConfidence)                << ",\n";

        // Key/mode runner-up: second-best candidate from analyzeKeyMode().
        if (r.keyRanked.size() >= 2) {
            const auto& ru = r.keyRanked[1];
            out << "      \"keyModeRunnerUp\": {"
                << "\"key\": \""      << jsonEscape(keyName(ru.keySignatureFifths, ru.mode)) << "\", "
                << "\"confidence\": " << fmtDouble(ru.normalizedConfidence)
                << "},\n";
        } else {
            out << "      \"keyModeRunnerUp\": null,\n";
        }

        out << "      \"pitchClassSet\": "   << r.pcMask                                             << ",\n";
        out << "      \"bassPitchClass\": "  << r.bassPc                                             << ",\n";
        out << "      \"bassIsRoot\": "      << (bassIsRoot ? "true" : "false")                      << ",\n";
        out << "      \"noteCount\": "       << noteCount                                            << ",\n";
        out << "      \"diatonicToKey\": "    << (r.chord.function.diatonicToKey ? "true" : "false") << ",\n";
        out << "      \"hasAnalyzedChord\": " << (r.hasAnalyzedChord ? "true" : "false")           << ",\n";
        out << "      \"tones\": [\n";

        for (size_t ti = 0; ti < r.tones.size(); ++ti) {
            const auto& tone = r.tones[ti];
            const bool isLastTone = (ti + 1 == r.tones.size());
            out << "        {"
                << "\"pitch\": " << tone.pitch << ", "
                << "\"tpc\": " << tone.tpc << ", "
                << "\"weight\": " << fmtDouble(tone.weight, 6) << ", "
                << "\"isBass\": " << (tone.isBass ? "true" : "false") << ", "
                << "\"durationInRegion\": " << tone.durationInRegion << ", "
                << "\"distinctMetricPositions\": " << tone.distinctMetricPositions << ", "
                << "\"simultaneousVoiceCount\": " << tone.simultaneousVoiceCount
                << "}" << (isLastTone ? "" : ",") << "\n";
        }

        out << "      ],\n";
        out << "      \"alternatives\": [\n";

        for (size_t ai = 0; ai < r.alternatives.size(); ++ai) {
            const auto& alt = r.alternatives[ai];
            const bool isLastAlt = (ai + 1 == r.alternatives.size());
            const std::string altSym = analysis::ChordSymbolFormatter::formatSymbol(
                alt, r.key.keySignatureFifths);
            const std::string altRn = analysis::ChordSymbolFormatter::formatRomanNumeral(alt);

            const bool altBassIsRoot = (alt.identity.bassPc == alt.identity.rootPc);
            out << "        {"
                << "\"rootPitchClass\": " << alt.identity.rootPc << ", "
                << "\"bassPitchClass\": " << alt.identity.bassPc << ", "
                << "\"quality\": \""      << qualityToString(alt.identity.quality) << "\", "
                << "\"bassIsRoot\": "     << (altBassIsRoot ? "true" : "false") << ", "
                << "\"chordSymbol\": \""  << jsonEscape(altSym) << "\", "
                << "\"romanNumeral\": \"" << jsonEscape(altRn)  << "\", "
                << "\"score\": "          << fmtDouble(alt.identity.score, 5)
                << "}";
            if (!isLastAlt) out << ",";
            out << "\n";
        }

        out << "      ]\n";
        out << "    }";
        if (!isLast) out << ",";
        out << "\n";
    }

    out << "  ]\n";
    out << "}\n";
}

// ══════════════════════════════════════════════════════════════════════════
// Diagnostic output (--diagnose-measures)
// ══════════════════════════════════════════════════════════════════════════

static const char* diagPcName(int pc, int keyFifths)
{
    static constexpr const char* SHARP[12] = {
        "C","C#","D","D#","E","F","F#","G","G#","A","A#","B"
    };
    static constexpr const char* FLAT[12] = {
        "C","Db","D","Eb","E","F","Gb","G","Ab","A","Bb","B"
    };
    pc = ((pc % 12) + 12) % 12;
    return keyFifths < 0 ? FLAT[pc] : SHARP[pc];
}

static const char* diagQualityName(ChordQuality q)
{
    switch (q) {
    case ChordQuality::Major:          return "Major";
    case ChordQuality::Minor:          return "Minor";
    case ChordQuality::Diminished:     return "Diminished";
    case ChordQuality::Augmented:      return "Augmented";
    case ChordQuality::HalfDiminished: return "HalfDiminished";
    case ChordQuality::Suspended2:     return "Suspended2";
    case ChordQuality::Suspended4:     return "Suspended4";
    case ChordQuality::Power:          return "Power";
    default:                           return "Unknown";
    }
}

static const char* diagTemplateName(int tplIdx)
{
    // Must match the kDiagTemplates array order in RuleBasedChordAnalyzer::diagnoseChord.
    static constexpr const char* NAMES[16] = {
        "Major triad {0,4,7}",
        "Maj7 {0,4,7,11}",
        "Dom7 {0,4,7,10}",
        "Dom7b5 {0,4,6,10}",
        "Minor triad {0,3,7}",
        "Min7 {0,3,7,10}",
        "Diminished {0,3,6}",
        "Sus4b5 {0,5,6,10}",
        "HalfDim {0,3,6,10}",
        "Augmented {0,4,8}",
        "Sus2 {0,2,7}",
        "Sus4 {0,5,7,10}",
        "Sus4+Maj7 {0,5,7,11}",
        "Sus4#5 {0,5,8,10}",
        "Sus#4 {0,6,7}",
        "Power {0,7}",
    };
    if (tplIdx < 0 || tplIdx >= 16) { return "Unknown"; }
    return NAMES[static_cast<size_t>(tplIdx)];
}

static void writeDiagnosticJson(
    const std::vector<AnalyzedRegion>& regions,
    const std::set<int>& diagnoseMeasures,
    const std::string& sourceName,
    std::ostream& out)
{
    const analysis::RuleBasedChordAnalyzer diagAnalyzer;

    out << "{\n";
    out << "  \"source\": \"" << jsonEscape(sourceName) << "\",\n";
    out << "  \"diagnose_measures\": [\n";

    bool firstBlock = true;
    for (int targetMeasure : diagnoseMeasures) {
        // Find the first region at beat ~1 of this measure.
        const AnalyzedRegion* region = nullptr;
        for (const auto& r : regions) {
            if (r.measureNumber == targetMeasure) {
                // Take the first region in this measure (beat 1 or earliest beat).
                if (!region || r.beat < region->beat) {
                    region = &r;
                }
            }
        }
        if (!region) {
            // Measure not found — emit a stub.
            if (!firstBlock) { out << ",\n"; }
            firstBlock = false;
            out << "    {\"measure\": " << targetMeasure << ", \"error\": \"measure not found\"}\n";
            continue;
        }

        // Run diagnostic on this region's tones.
        const auto diag = diagAnalyzer.diagnoseChord(
            region->tones,
            region->key.keySignatureFifths,
            region->key.mode);

        const int keyFifths = region->key.keySignatureFifths;

        if (!firstBlock) { out << ",\n"; }
        firstBlock = false;

        out << "    {\n";
        out << "      \"measure\": " << region->measureNumber << ",\n";
        out << "      \"beat\": " << fmtDouble(region->beat, 4) << ",\n";
        out << "      \"key\": \"" << jsonEscape(keyName(region->key.keySignatureFifths, region->key.mode)) << "\",\n";
        out << "      \"output_symbol\": \"" << jsonEscape(
            region->hasAnalyzedChord
                ? analysis::ChordSymbolFormatter::formatSymbol(region->chord, keyFifths)
                : std::string("?")) << "\",\n";

        // ── Collected notes ─────────────────────────────────────────────
        out << "      \"collected_notes\": [\n";
        for (size_t ti = 0; ti < region->tones.size(); ++ti) {
            const auto& t = region->tones[ti];
            const int pc = t.pitch % 12;
            out << "        {"
                << "\"pitch_class\": " << pc << ", "
                << "\"pc_name\": \"" << diagPcName(pc, keyFifths) << "\", "
                << "\"midi\": " << t.pitch << ", "
                << "\"weight\": " << fmtDouble(t.weight, 6) << ", "
                << "\"duration_ticks\": " << t.durationInRegion << ", "
                << "\"is_bass\": " << (t.isBass ? "true" : "false")
                << "}";
            if (ti + 1 < region->tones.size()) { out << ","; }
            out << "\n";
        }
        out << "      ],\n";
        out << "      \"bass_pc\": " << diag.bassPc << ",\n";
        out << "      \"bass_pc_name\": \"" << diagPcName(diag.bassPc, keyFifths) << "\",\n";
        out << "      \"distinct_pcs\": " << diag.distinctPcs << ",\n";

        // ── Per-PC weight histogram ─────────────────────────────────────
        out << "      \"pc_weights\": {";
        bool firstPc = true;
        for (int pc = 0; pc < 12; ++pc) {
            if (diag.pcWeights[static_cast<size_t>(pc)] < 0.001) { continue; }
            if (!firstPc) { out << ", "; }
            firstPc = false;
            out << "\"" << diagPcName(pc, keyFifths) << "(" << pc << ")\": "
                << fmtDouble(diag.pcWeights[static_cast<size_t>(pc)], 5);
        }
        out << "},\n";

        // ── Top candidates (above 75 % of winner's score) ───────────────
        const double threshold = diag.candidates.empty()
                                 ? 0.0
                                 : diag.candidates.front().totalScore * 0.75;
        out << "      \"top_candidates\": [\n";
        bool firstCand = true;
        int rank = 0;
        for (const auto& c : diag.candidates) {
            if (c.totalScore < threshold) { break; }
            if (!firstCand) { out << ",\n"; }
            firstCand = false;
            ++rank;
            out << "        {\n";
            out << "          \"rank\": " << rank << ",\n";
            out << "          \"root_pc\": " << c.rootPc << ",\n";
            out << "          \"root_name\": \"" << diagPcName(c.rootPc, keyFifths) << "\",\n";
            out << "          \"template_idx\": " << c.templateIdx << ",\n";
            out << "          \"template_name\": \"" << diagTemplateName(c.templateIdx) << "\",\n";
            out << "          \"quality\": \"" << diagQualityName(c.quality) << "\",\n";
            out << "          \"total_score\": " << fmtDouble(c.totalScore, 5) << ",\n";
            out << "          \"template_tones\": " << fmtDouble(c.templateTonesScore, 5) << ",\n";
            out << "          \"extra_notes\": " << fmtDouble(c.extraNotesScore, 5) << ",\n";
            out << "          \"bass_bonus\": " << fmtDouble(c.bassBonus, 5) << ",\n";
            out << "          \"diatonic_bonus\": " << fmtDouble(c.diatonicBonus, 5) << ",\n";
            out << "          \"non_bass_adj\": " << fmtDouble(c.nonBassAdjust, 5) << ",\n";
            out << "          \"structural_penalty\": " << fmtDouble(c.structuralPenalty, 5) << ",\n";
            out << "          \"tpc_bonus\": " << fmtDouble(c.tpcBonus, 5) << ",\n";
            out << "          \"context_bonus\": " << fmtDouble(c.contextBonus, 5) << ",\n";
            out << "          \"dim7_bonus\": " << fmtDouble(c.dim7Bonus, 5) << "\n";
            out << "        }";
        }
        out << "\n      ],\n";

        // ── Extension flags of the winning result ───────────────────────
        out << "      \"extension_flags\": {\n";
        if (region->hasAnalyzedChord) {
            const uint32_t ext = region->chord.identity.extensions;
            out << "        \"hasMinorSeventh\": "      << (analysis::hasExtension(ext, analysis::Extension::MinorSeventh)      ? "true" : "false") << ",\n";
            out << "        \"hasMajorSeventh\": "      << (analysis::hasExtension(ext, analysis::Extension::MajorSeventh)      ? "true" : "false") << ",\n";
            out << "        \"hasDimSeventh\": "        << (analysis::hasExtension(ext, analysis::Extension::DiminishedSeventh) ? "true" : "false") << ",\n";
            out << "        \"hasAddedSixth\": "        << (analysis::hasExtension(ext, analysis::Extension::AddedSixth)        ? "true" : "false") << ",\n";
            out << "        \"hasNaturalNinth\": "      << (analysis::hasExtension(ext, analysis::Extension::NaturalNinth)      ? "true" : "false") << ",\n";
            out << "        \"hasFlatNinth\": "         << (analysis::hasExtension(ext, analysis::Extension::FlatNinth)         ? "true" : "false") << ",\n";
            out << "        \"hasSharpNinth\": "        << (analysis::hasExtension(ext, analysis::Extension::SharpNinth)        ? "true" : "false") << ",\n";
            out << "        \"hasNaturalEleventh\": "   << (analysis::hasExtension(ext, analysis::Extension::NaturalEleventh)   ? "true" : "false") << ",\n";
            out << "        \"hasSharpEleventh\": "     << (analysis::hasExtension(ext, analysis::Extension::SharpEleventh)     ? "true" : "false") << ",\n";
            out << "        \"hasNaturalThirteenth\": " << (analysis::hasExtension(ext, analysis::Extension::NaturalThirteenth) ? "true" : "false") << ",\n";
            out << "        \"hasFlatThirteenth\": "    << (analysis::hasExtension(ext, analysis::Extension::FlatThirteenth)    ? "true" : "false") << ",\n";
            out << "        \"hasSharpThirteenth\": "   << (analysis::hasExtension(ext, analysis::Extension::SharpThirteenth)   ? "true" : "false") << ",\n";
            out << "        \"hasFlatFifth\": "         << (analysis::hasExtension(ext, analysis::Extension::FlatFifth)         ? "true" : "false") << ",\n";
            out << "        \"hasSharpFifth\": "        << (analysis::hasExtension(ext, analysis::Extension::SharpFifth)        ? "true" : "false") << ",\n";
            out << "        \"omitsThird\": "           << (analysis::hasExtension(ext, analysis::Extension::OmitsThird)        ? "true" : "false") << ",\n";
            out << "        \"isSixNine\": "            << (analysis::hasExtension(ext, analysis::Extension::SixNine)           ? "true" : "false") << "\n";
        } else {
            out << "        \"error\": \"no analyzed chord\"\n";
        }
        out << "      }\n";
        out << "    }";
    }

    out << "\n  ]\n";
    out << "}\n";
}

// ══════════════════════════════════════════════════════════════════════════
// Entry point
// ══════════════════════════════════════════════════════════════════════════

static void printHelp(const std::string& prog)
{
    std::cerr
        << "Usage:\n"
        << "  " << prog << " <input.[xml|musicxml|mxl|mscz|mscx]> [output.json]"
                           " [--preset Standard|Jazz|Modal|Baroque|Contemporary]"
                           " [--dump-regions batch|notation|notation-premerge]"
                           " [--diagnose-measures N[,N...]]\n"
        << "\n"
        << "  Loads a score, runs harmonic analysis (ChordAnalyzer + KeyModeAnalyzer)\n"
        << "  and writes JSON to output.json, or to stdout if no output file given.\n"
        << "\n"
        << "  --preset  Apply a named mode prior preset (default: Standard).\n"
        << "            Run the same corpus under different presets and diff the\n"
        << "            results to identify mode-inference improvements.\n"
        << "  --dump-regions <mode>\n"
        << "            Select which analysis path to serialize. 'batch' writes the\n"
        << "            tool's current batch path, 'notation' writes the live notation\n"
        << "            bridge result, 'notation-premerge' writes the notation\n"
        << "            bridge regions before same-chord merge/absorption.\n"
        << "  --diagnose-measures N[,N,...]\n"
        << "            Per-measure diagnostic mode. For each listed measure number,\n"
        << "            emits a JSON block with collected notes, per-PC weights, and\n"
        << "            the full root × template scoring breakdown. Output replaces the\n"
        << "            standard regions JSON. Example: --diagnose-measures 1,2,3,5,7\n"
        << "\n"
        << "  Returns 0 on success, non-zero on failure.\n";
}

int main(int argc, char* argv[])
{
    QCoreApplication::setOrganizationName("MuseScore");
    QCoreApplication::setOrganizationDomain("musescore.org");
    QCoreApplication::setApplicationName("batch_analyze");
    QGuiApplication app(argc, argv);

    const QStringList args = QCoreApplication::arguments();
    const std::string programName = QFileInfo(args.value(0)).fileName().toUtf8().toStdString();

    if (args.size() < 2) {
        printHelp(programName);
        return 1;
    }

    const QString arg1 = args.at(1);
    if (arg1 == "--help" || arg1 == "-h") {
        printHelp(programName);
        return 0;
    }

    // ── Parse arguments ────────────────────────────────────────────────────
    // Syntax: <input> [output] [--preset <name>]
    //         [--dump-regions <batch|notation|notation-premerge>]
    //         [--diagnose-measures N[,N,...]]
    // Options may appear anywhere after the input path.
    muse::io::path_t inputPath;
    muse::io::path_t outputPath;
    std::string presetName = "Standard";
    RegionDumpMode dumpMode = RegionDumpMode::Batch;
    std::set<int> diagnoseMeasures;

    for (int i = 1; i < args.size(); ++i) {
        const QString a = args.at(i);
        if (a == "--preset" || a == "-p") {
            if (i + 1 < args.size()) {
                presetName = args.at(++i).toUtf8().toStdString();
            } else {
                std::cerr << "ERROR: --preset requires a name argument\n";
                return 1;
            }
        } else if (a == "--dump-regions") {
            if (i + 1 >= args.size()) {
                std::cerr << "ERROR: --dump-regions requires a mode argument\n";
                return 1;
            }

            const std::string mode = args.at(++i).toUtf8().toStdString();
            if (mode == "batch") {
                dumpMode = RegionDumpMode::Batch;
            } else if (mode == "notation") {
                dumpMode = RegionDumpMode::Notation;
            } else if (mode == "notation-premerge") {
                dumpMode = RegionDumpMode::NotationPreMerge;
            } else {
                std::cerr << "ERROR: unknown --dump-regions mode '" << mode
                          << "'. Valid values: batch, notation, notation-premerge\n";
                return 1;
            }
        } else if (a == "--diagnose-measures") {
            if (i + 1 >= args.size()) {
                std::cerr << "ERROR: --diagnose-measures requires a comma-separated list of measure numbers\n";
                return 1;
            }
            const std::string measureList = args.at(++i).toUtf8().toStdString();
            std::istringstream iss(measureList);
            std::string token;
            while (std::getline(iss, token, ',')) {
                try {
                    diagnoseMeasures.insert(std::stoi(token));
                } catch (...) {
                    std::cerr << "ERROR: invalid measure number in --diagnose-measures: '"
                              << token << "'\n";
                    return 1;
                }
            }
        } else if (inputPath.empty()) {
            inputPath = a;
        } else if (outputPath.empty()) {
            outputPath = a;
        }
    }

    if (inputPath.empty()) {
        printHelp(programName);
        return 1;
    }

    // ── Build key mode preferences from preset ─────────────────────────────
    analysis::KeyModeAnalyzerPreferences keyPrefs;
    if (!applyPreset(presetName, keyPrefs)) {
        std::cerr << "ERROR: unknown preset '" << presetName
                  << "'.  Valid names: Standard, Jazz, Modal, Baroque, Contemporary\n";
        return 1;
    }

    // ── Build chord analyzer preferences from preset ────────────────────────
    // Preset-specific chord analysis tuning.
    //
    // Jazz: lower extension threshold (0.12) so lightly-voiced ninths register;
    //       inversion bonuses are reduced because bass-root 6th chords (C6, Bb6)
    //       are idiomatic labels and should not be de-emphasised.
    //
    // Baroque preset: only preferMinorOverMajorAdd6 differs from Standard.
    // Inversion bonuses use struct defaults (stepwiseBassInversionBonus=0.50,
    // stepwiseBassLookaheadBonus=0.50, sameRootInversionBonus=0.40,
    // completeTriadInversionBonus=0.45). Tuning of these values is tracked
    // in docs/prompts/iteration_plan_inversion_redesign.md Iteration 4.
    //
    // Standard, Modal, Contemporary: defaults + preferMinorOverMajorAdd6 (added-sixth
    //          chords are rare in tonal and modal writing; Minor7 inversions are the
    //          correct reading for the Bb6/Gm7 enharmonic pair).
    analysis::ChordAnalyzerPreferences chordPrefs;

    if (presetName == "Jazz") {
        chordPrefs.extensionThreshold                    = 0.12;
        chordPrefs.preferMinorOverMajorAdd6              = false;
        // Contextual inversion bonuses reduced — bass-root 6th chords are idiomatic
        chordPrefs.stepwiseBassInversionBonus            = 0.20;
        chordPrefs.stepwiseBassLookaheadBonus            = 0.20;
        chordPrefs.sameRootInversionBonus                = 0.15;
        chordPrefs.completeTriadInversionBonus           = 0.20;

    } else if (presetName == "Baroque") {
        chordPrefs.preferMinorOverMajorAdd6              = true;

    } else {
        // Standard, Modal, Contemporary: defaults + prefer Minor over Major add6
        chordPrefs.preferMinorOverMajorAdd6              = true;
        // maxTotalInversionContextBonus stays at default (2.0)
    }

    // ── Initialize MuseScore headless ──────────────────────────────────────
    initModules();

    // ── Load score ─────────────────────────────────────────────────────────
    MasterScore* score = loadScore(inputPath);
    if (!score) {
        std::cerr << "ERROR: failed to load score: "
                  << inputPath.toQString().toUtf8().toStdString() << "\n";
        return 1;
    }

    // ── Build exclude-staves set ───────────────────────────────────────────
    std::set<size_t> excludeStaves;
    for (size_t si = 0; si < score->nstaves(); ++si) {
        if (!staffIsEligible(score, si)) {
            excludeStaves.insert(si);
        }
    }

    // ── Analyze harmonic regions (key inferred locally per region) ────────
    std::vector<AnalyzedRegion> regions;
    if (dumpMode == RegionDumpMode::Batch) {
        regions = analyzeScore(score, excludeStaves, keyPrefs, chordPrefs);
    } else {
        RegionDumpBundle notationDump = analyzeScoreNotation(score, excludeStaves);
        if (dumpMode == RegionDumpMode::NotationPreMerge) {
            regions = std::move(notationDump.preMergeRegions);
        } else if (!notationDump.postMergeRegions.empty()) {
            regions = std::move(notationDump.postMergeRegions);
        } else {
            regions = std::move(notationDump.finalRegions);
        }
    }

    // ── Opening key: inferred at tick 0 (for the top-level JSON field) ────
    const size_t refStaff = referenceStaffForAnalysis(score, excludeStaves);
    const KeyModeAnalysisResult openingKey = inferLocalKey(
        score, refStaff, excludeStaves, Fraction(0, 1), nullptr, keyPrefs)[0];

    // ── Extract source basename ───────────────────────────────────────────
    const std::string sourceName = QFileInfo(inputPath.toQString()).fileName().toUtf8().toStdString();

    // ── Write JSON ────────────────────────────────────────────────────────
    if (outputPath.empty()) {
        if (!diagnoseMeasures.empty()) {
            writeDiagnosticJson(regions, diagnoseMeasures, sourceName, std::cout);
        } else {
            writeJson(regions, sourceName, presetName, openingKey, regionDumpModeName(dumpMode), std::cout);
        }
        std::cout.flush();
        std::fflush(stdout);
    } else {
        QFile outFile(outputPath.toQString());
        if (!outFile.open(QIODevice::WriteOnly | QIODevice::Truncate | QIODevice::Text)) {
            std::cerr << "ERROR: cannot open output file: "
                      << outputPath.toQString().toUtf8().toStdString() << "\n";
            delete score;
            return 1;
        }
        std::ostringstream out;
        if (!diagnoseMeasures.empty()) {
            writeDiagnosticJson(regions, diagnoseMeasures, sourceName, out);
        } else {
            writeJson(regions, sourceName, presetName, openingKey, regionDumpModeName(dumpMode), out);
        }
        const std::string json = out.str();
        outFile.write(json.data(), static_cast<qint64>(json.size()));
        outFile.flush();
        outFile.close();
    }

    delete score;
    // Skip static-module destructor sequence (crashes due to ordering constraints).
    // On Windows, some runs hang in Qt TLS shutdown during ExitProcess after the
    // JSON is already fully written. TerminateProcess bypasses that teardown.
#ifdef _WIN32
    ::TerminateProcess(::GetCurrentProcess(), 0);
#endif
    std::_Exit(0);
}
