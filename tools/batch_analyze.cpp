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
//                [--preset Standard|Jazz|Modal|Baroque|Contemporary|Default]
//                [--dump-regions batch|notation|notation-premerge]
//   batch_analyze --help

#include <algorithm>
#include <chrono>
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
#include "composing/analysis/key/keyresolver.h"
#include "composing/analysis/key/modepriorpresets.h"
#include "composing/analysis/chord/analysisutils.h"
#include "composing/analysis/region/regionanalyzer.h"
#include "composing/analysis/section/sectionanalyzer.h"   // Stage 2.2-i prototype: --section-level
#include "composing/analysis/section/cadencekeyanchor.h"   // Stage 4c-i: --dump-cadence-anchor
#include "composing/analysis/section/localmodulationdetector.h" // Stage 4d-i: --dump-modulation
#include "composing/analysis/section/jointkeydecision.h"    // J-key-i: --dump-joint-key
#include "composing/analysis/function/tonicizationlabeler.h"  // Stage 6-tonic-i: --dump-tonicization
#include "composing/analysis/function/functionrelationallabel.h"  // Phase 5c Step M: --dump-l5 (dormant L5 RN)
#include "composing/analysis/function/functionoutput.h"           // Phase 5c Step M: --dump-l5 (§7 assembly)
#include "composing/analysis/function/functionprogression.h"      // E0 --dump-fullspine (L5 Step-1 progression)
#include "composing/analysis/function/functioncadence.h"          // E0 --dump-fullspine (L5 Step-2 cadence)
#include "composing/analysis/function/functionresolver.h"         // E0 --dump-fullspine (L5 Step-3 resolver + §5.5 override)
#include "composing/analysis/function/functionmodulation.h"       // E0 --dump-fullspine (L5 Step-4 tonicization/modulation + recompute)
#include "composing/analysis/function/functionromannumeral.h"     // E0 --dump-fullspine (L5 Step-1 base RN)
#include "composing/analysis/scoreharvest/metricweights.h"        // E0 --dump-fullspine (per-slice metric weight)
#include "composing/analysis/grouping/groupinglayer.h"            // L6 --dump-l6 (dormant grouping assembly)
#include "composing/analysis/region/sparsechordrefinement.h"      // diatonicDegreeForRootPc (the inline-RN baseline)
#include "composing/analysis/notemodel/note_model.h"        // Layer 2 validation: --validate-slices
#include "composing/analysis/slicing/slicer.h"              // Layer 2 validation: --validate-slices
#include "composing/analysis/key/keymodesequence.h"         // Layer 3 decoder: --decode-keymode
#include "composing/analysis/chord/chordslicedecoder.h"     // Layer 4 decoder: --decode-chords
#include "composing/analysis/engravingbridge/phraseboundaryview.h"  // owned Layer-1.5 phrase-boundary primitive
#include "composing/analysis/engravingbridge/regiontonecollector.h" // weightedPcView (focal-slice sounding pcs)
#include "composing/analyzed_section.h"                    // Stage 2.2-i prototype: AnalyzedSection
#include "notation/internal/notationanalysisinternal.h"
#include "notation/internal/notationcomposingbridge.h"

// ── Namespace aliases ──────────────────────────────────────────────────────
using namespace mu::engraving;
namespace analysis = mu::composing::analysis;
using analysis::ChordAnalysisTone;
using analysis::ChordAnalysisResult;
using analysis::ChordQuality;
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
/// Valid names: "Standard", "Jazz", "Modal", "Baroque", "Contemporary", "Default".
/// ("Default" = live product out-of-box config, not a tuning preset — Stage 2.4 V4.)
static bool applyPreset(const std::string& name,
                        analysis::KeyModeAnalyzerPreferences& prefs)
{
    // "Default" (Stage 2.4 V4) is NOT a named tuning preset — it reproduces the
    // live product's out-of-box mode priors so the configuration users actually
    // run can be corpus-measured (informational; no gate). These 21 values are the
    // app's registered settings defaults in composingconfiguration.cpp (init(),
    // MODE_PRIOR_* setDefaultValue calls). They are NOT the KeyModeAnalyzerPreferences
    // struct defaults and NOT the "Standard" preset: the app defaults diverge from
    // both on 11 of 21 modes (Lydian, Mixolydian, Locrian, LydianAugmented,
    // LydianDominant, MixolydianB6, AeolianB5, LocrianSharp6, IonianSharp5,
    // DorianSharp4, LydianSharp2). KEEP IN SYNC with composingconfiguration.cpp.
    if (name == "Default") {
        prefs.modePriorIonian           =  1.20;
        prefs.modePriorDorian           = -0.50;
        prefs.modePriorPhrygian         = -1.50;
        prefs.modePriorLydian           =  0.00;
        prefs.modePriorMixolydian       = -0.20;
        prefs.modePriorAeolian          =  1.00;
        prefs.modePriorLocrian          = -3.50;
        prefs.modePriorMelodicMinor     = -0.50;
        prefs.modePriorDorianB2         = -1.50;
        prefs.modePriorLydianAugmented  = -1.00;
        prefs.modePriorLydianDominant   = -0.30;
        prefs.modePriorMixolydianB6     = -1.00;
        prefs.modePriorAeolianB5        = -2.00;
        prefs.modePriorAltered          = -3.50;
        prefs.modePriorHarmonicMinor    = -0.30;
        prefs.modePriorLocrianSharp6    = -2.00;
        prefs.modePriorIonianSharp5     = -1.50;
        prefs.modePriorDorianSharp4     = -1.50;
        prefs.modePriorPhrygianDominant = -0.80;
        prefs.modePriorLydianSharp2     = -2.00;
        prefs.modePriorAlteredDomBB7    = -3.50;
        return true;
    }
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

// ── Stage 4c-iii: phrase boundaries from fermatas (key-agnostic notation) ─────
// The fermata scan is now the single owned Layer-1.5 primitive
// (analysis::engravingbridge::phraseBoundaryTicks); the former local
// collectPhraseBoundaryTicks was retired into it (byte-identical de-dup). In a
// Bach chorale these mark phrase endings; a cadence resolving INTO a
// fermata-bearing region is a STRUCTURAL cadence (weighted above interior
// tonicizations). Notation only — no key/function.

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
// Measure location helpers
// ══════════════════════════════════════════════════════════════════════════

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

// ══════════════════════════════════════════════════════════════════════════
// Key/mode resolution
//
// Phase 3 of the duplication remediation (docs/duplication_audit.md §5.3)
// moved the shared resolver into composing/analysis/key/keyresolver.{h,cpp}.
// This translation unit no longer carries any pitch-context collection or
// windowed-resolution code; it only adapts the call into the JSON-emitting
// region pipeline below.
// ══════════════════════════════════════════════════════════════════════════

/// Infer key/mode at @p tick — thin wrapper around the shared resolver.
/// Returns ranked candidates; element [0] is the winner, [1] feeds the
/// `keyModeRunnerUp` JSON field.
static std::vector<KeyModeAnalysisResult> inferLocalKey(
    Score* score,
    size_t keySigStaffIdx,
    const std::set<size_t>& excludeStaves,
    const Fraction& tick,
    const KeyModeAnalysisResult* prevResult = nullptr,
    const analysis::KeyModeAnalyzerPreferences& keyPrefs = analysis::KeyModeAnalyzerPreferences{})
{
    return mu::composing::analysis::keyresolver::resolveKeyAndModeRanked(
        score, tick,
        static_cast<mu::engraving::staff_idx_t>(keySigStaffIdx),
        excludeStaves, keyPrefs, prevResult);
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

// ── Shared region orchestrator ────────────────────────────────────────────────
// Phase 4 of the duplication remediation (docs/duplication_audit.md §§2.14, 5.4)
// moved the per-region pipeline body into composing/analysis/region/
// regionanalyzer.{h,cpp}. analyzeScore() below is now a thin adapter that calls
// the shared orchestrator and post-processes its output into AnalyzedRegion.

/// Forward declaration — defined later in this file.
static const char* qualityToString(ChordQuality q);

static std::vector<AnalyzedRegion> analyzeScore(
    Score* score,
    const std::set<size_t>& excludeStaves,
    const analysis::KeyModeAnalyzerPreferences& keyPrefs = analysis::KeyModeAnalyzerPreferences{},
    const analysis::ChordAnalyzerPreferences& chordPrefs = analysis::kDefaultChordAnalyzerPreferences,
    bool sectionLevel = false)
{
    namespace cra = mu::composing::analysis::region;

    const Segment* firstSegment = score->tick2segment(Fraction(0, 1), true, SegmentType::ChordRest);
    if (!firstSegment) {
        return {};
    }

    const Fraction startTick = firstSegment->tick();
    const Fraction endTick = score->endTick();

    // Phase 4: delegate the regional pipeline to the shared orchestrator
    // (composing/analysis/region/regionanalyzer). This wrapper retains the
    // batch-specific tone-collection behaviour (excludeLookAheadOnDenseStart)
    // and post-processes the resulting regions into the JSON-flavored
    // AnalyzedRegion (with measureNumber/beat/pcMask/keyRanked).
    cra::AnalyzeRegionsOptions opts;
    opts.granularity                     = analysis::HarmonicRegionGranularity::Smoothed;
    // DIVERGENCE (see docs/implementation_roadmap.md 0.6): batch hard-codes 0.25, whereas
    // the user-facing bridge reads it from IComposingAnalysisConfiguration
    // (notationharmonicrhythmbridge.cpp:85, falling back to 0.25 only when cfg is null).
    // 0.25 is also the config default, so the two coincide today — but ALL batch corpus
    // numbers (BIR, rn_agree) assume 0.25. If the config default ever changes, batch will
    // no longer measure the user pipeline. Unifying the source is Stage 2 work; do not
    // change behavior here.
    opts.onsetBoundaryThreshold          = 0.25;
    opts.excludeLookAheadOnDenseStart    = true;
    // D2 unification — batch now matches the bridge's sparse Pass-1 admission
    // (Iter 75; both paths use minDistinctPcsForCandidate=1). Net error reduction
    // on both corpora. Known residual: the sparse-admission segmentation cascade at
    // bwv320 m27 b1 — an admitted 2-PC Gm slice makes previousRootPc=G for the next
    // C window, and rootContinuityBonus tips that ~0.02-margin decision to G6/E.
    // Queued for Iter 98 (gate rootContinuityBonus off a sparse/uncertain
    // predecessor); see regionanalyzer.h AnalyzeRegionsOptions docs.
    opts.pass1MinDistinctPcsForCandidate = 1;

    const auto regions = cra::analyzeRegions(
        score, startTick, endTick, excludeStaves, chordPrefs, keyPrefs, opts);

    if (regions.empty()) {
        return {};
    }

    // ── Stage 2.2-i prototype: section-level pass ───────────────────────────
    // When --section-level is on, feed the (preset-specific) analyzeRegions
    // HarmonicRegion stream into the user-facing section pipeline
    // (composing/analysis/section/analyzeSection): Pass-1 measure layout +
    // gap-tone insertion, Pass-4 key/mode stabilization + sparse-quality
    // refinement, and confidence-gated key-area grouping. The .ours.json schema
    // is unchanged; fields are populated from the post-section regions.
    // Additive annotations (cadence markers, pivot labels, key areas) are NOT
    // emitted this run (schema decision deferred to the dossier). The Pass-0
    // stream is batch's preset path AND the preset chordPrefs are now threaded
    // into section gap inference (Stage 2.4, D-GAP) — so the diagnostic measures
    // a consistent preset pipeline end-to-end rather than preset Pass-0 + default
    // gap analysis.
    if (sectionLevel) {
        const analysis::AnalyzedSection section = analysis::analyzeSection(
            score, startTick, endTick, excludeStaves, regions, chordPrefs);

        std::vector<AnalyzedRegion> sectionResult;
        sectionResult.reserve(section.regions.size());
        for (const auto& sr : section.regions) {
            const Fraction regionStart = Fraction::fromTicks(sr.startTick);
            const MeasureTickInfo regionMeasure = locateMeasureByTick(score, regionStart);
            const Measure* measure = regionMeasure.measure;

            AnalyzedRegion ar;
            ar.startTick        = sr.startTick;
            ar.endTick          = sr.endTick;
            ar.measureNumber    = measure ? regionMeasure.number : 0;
            if (measure) {
                const int tickInMeasure = sr.startTick - measure->tick().ticks();
                ar.beat = 1.0 + static_cast<double>(tickInMeasure) / Constants::DIVISION;
            } else {
                ar.beat = 1.0;
            }
            ar.chord            = sr.chordResult;
            ar.hasAnalyzedChord = sr.hasAnalyzedChord;
            ar.tones            = sr.tones;
            ar.key              = sr.keyModeResult;
            // Runner-up key is not produced by the section pass (stabilization
            // overwrites the per-region winner); emit a single-element ranking
            // so keyModeRunnerUp serializes as null. Core BIR/rn metrics read
            // root/quality/bass/ticks/key only — not the runner-up field.
            ar.keyRanked        = { sr.keyModeResult };
            ar.pcMask           = pitchClassMask(ar.tones);
            ar.bassPc           = sr.chordResult.identity.bassPc;
            if (ar.bassPc < 0) {
                if (const auto* bassTone = analysis::bassToneFromTones(ar.tones)) {
                    ar.bassPc = bassTone->pitch % 12;
                }
            }
            for (size_t altIdx = 0; altIdx < sr.alternatives.size() && altIdx < 3; ++altIdx) {
                ar.alternatives.push_back(sr.alternatives[altIdx]);
            }
            sectionResult.push_back(std::move(ar));
        }
        return sectionResult;
    }

    const size_t refStaff = referenceStaffForAnalysis(score, excludeStaves);

    std::vector<AnalyzedRegion> result;
    result.reserve(regions.size());

    // Per-region key ranking — batch's keyModeRunnerUp JSON field needs the
    // top-2 results; the shared orchestrator only stores the winner. The
    // resolver is windowed and cheap enough to call once per merged region.
    std::optional<analysis::KeyModeAnalysisResult> prevKey;
    for (const auto& hr : regions) {
        const Fraction regionStart = Fraction::fromTicks(hr.startTick);
        const MeasureTickInfo regionMeasure = locateMeasureByTick(score, regionStart);
        const Measure* measure = regionMeasure.measure;
        if (!measure) {
            continue;
        }

        const auto keyRanked = analysis::keyresolver::resolveKeyAndModeRanked(
            score, regionStart, static_cast<staff_idx_t>(refStaff),
            excludeStaves, keyPrefs,
            prevKey.has_value() ? &prevKey.value() : nullptr);
        prevKey = keyRanked.front();

        AnalyzedRegion ar;
        ar.startTick        = hr.startTick;
        ar.endTick          = hr.endTick;
        ar.measureNumber    = regionMeasure.number;
        const int tickInMeasure = hr.startTick - measure->tick().ticks();
        ar.beat             = 1.0 + static_cast<double>(tickInMeasure) / Constants::DIVISION;
        ar.chord            = hr.chordResult;
        ar.hasAnalyzedChord = hr.hasAnalyzedChord;
        ar.tones            = hr.tones;
        ar.key              = hr.keyModeResult;
        ar.keyRanked        = keyRanked;
        ar.pcMask           = pitchClassMask(ar.tones);
        ar.bassPc           = hr.chordResult.identity.bassPc;
        if (ar.bassPc < 0) {
            if (const auto* bassTone = analysis::bassToneFromTones(ar.tones)) {
                ar.bassPc = bassTone->pitch % 12;
            }
        }

        // Up to 3 alternatives (indices 1..3 from analyzeChord).
        for (size_t altIdx = 0; altIdx < hr.alternatives.size() && altIdx < 3; ++altIdx) {
            ar.alternatives.push_back(hr.alternatives[altIdx]);
        }

        result.push_back(std::move(ar));
    }

    return result;
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

// ── Stage-4 emission instrument: read-only key-candidate dump ────────────────
//
// Re-runs the per-region key resolution loop (threading prevKey exactly as
// regionanalyzer's loop does, but over the produced regions), with the resolver
// diagnostic dump enabled, and emits the per-candidate emission breakdown for
// any region whose [startTick,endTick) contains a requested tick (or whose
// startTick is requested). This is read-only: it does not touch the production
// regions vector or the standard JSON. analyzeKeyMode's emission scores are
// prevResult-independent, so the six-term breakdown is exact regardless of the
// prev chain; the resolver context records which path/promotions fired.
static void writeKeyCandidateDump(
    Score* score,
    const std::vector<AnalyzedRegion>& regions,
    size_t refStaff,
    const std::set<size_t>& excludeStaves,
    const analysis::KeyModeAnalyzerPreferences& keyPrefs,
    const std::set<int>& targetTicks,
    const std::string& sourceName,
    std::ostream& out)
{
    static const char* PCNAME[12] = { "C","Db","D","Eb","E","F","Gb","G","Ab","A","Bb","B" };

    out << "{\n";
    out << "  \"source\": \"" << sourceName << "\",\n";
    out << "  \"key_candidate_dump\": [\n";

    std::optional<analysis::KeyModeAnalysisResult> prevKey;
    bool firstEmitted = true;
    for (const AnalyzedRegion& r : regions) {
        analysis::keyresolver::KeyResolveDump dump;
        const Fraction regionStart = Fraction::fromTicks(r.startTick);
        const auto ranked = analysis::keyresolver::resolveKeyAndModeRanked(
            score, regionStart, static_cast<mu::engraving::staff_idx_t>(refStaff),
            excludeStaves, keyPrefs,
            prevKey.has_value() ? &prevKey.value() : nullptr, &dump);

        bool match = targetTicks.count(r.startTick) > 0;
        if (!match) {
            for (int t : targetTicks) {
                if (t >= r.startTick && t < r.endTick) { match = true; break; }
            }
        }

        if (match) {
            if (!firstEmitted) { out << ",\n"; }
            firstEmitted = false;
            out << "    {\n";
            out << "      \"startTick\": " << r.startTick << ",\n";
            out << "      \"endTick\": " << r.endTick << ",\n";
            out << "      \"measure\": " << r.measureNumber << ",\n";
            out << "      \"beat\": " << fmtDouble(r.beat) << ",\n";
            out << "      \"notatedFifths\": " << dump.notatedFifths << ",\n";
            out << "      \"correctedFifths\": " << dump.correctedFifths << ",\n";
            out << "      \"declaredModeOrdinal\": " << dump.declaredModeOrdinal << ",\n";
            out << "      \"path\": \"" << dump.pathTaken << "\",\n";
            out << "      \"lookaheadBeats\": " << dump.lookaheadBeatsUsed << ",\n";
            out << "      \"hysteresisPromoted\": " << (dump.hysteresisPromoted ? "true" : "false") << ",\n";
            out << "      \"strongPriorPromoted\": " << (dump.strongPriorPromoted ? "true" : "false") << ",\n";
            out << "      \"productionKey\": \"" << keyName(r.key.keySignatureFifths, r.key.mode) << "\",\n";
            out << "      \"resolvedWinner\": \"" << keyName(ranked.front().keySignatureFifths, ranked.front().mode) << "\",\n";
            out << "      \"candidates\": [\n";
            for (size_t ci = 0; ci < dump.candidates.size(); ++ci) {
                const analysis::KeyCandidateScore& c = dump.candidates[ci];
                const analysis::KeySigMode m = analysis::keyModeFromIndex(c.modeIndex);
                out << "        {"
                    << "\"tonicPc\": " << c.tonicPc
                    << ", \"label\": \"" << PCNAME[(c.tonicPc % 12 + 12) % 12] << analysis::keyModeSuffix(m) << "\""
                    << ", \"isMajor\": " << (analysis::keyModeIsMajor(m) ? "true" : "false")
                    << ", \"finalScore\": " << fmtDouble(c.finalScore)
                    << ", \"scale\": " << fmtDouble(c.scaleMembership)
                    << ", \"triad\": " << fmtDouble(c.triadEvidence)
                    << ", \"char\": " << fmtDouble(c.characteristicPitch)
                    << ", \"lt\": " << fmtDouble(c.trueLeadingTone)
                    << ", \"keySigProx\": " << fmtDouble(c.keySignatureProximity)
                    << ", \"prior\": " << fmtDouble(c.modePrior)
                    << ", \"declaredPenalty\": " << fmtDouble(c.declaredPenalty)
                    << ", \"disambig\": " << fmtDouble(c.disambiguationDelta)
                    << ", \"tonalCenter\": " << fmtDouble(c.tonalCenterScore)
                    << ", \"tonicW\": " << fmtDouble(c.tonicWeight)
                    << ", \"thirdW\": " << fmtDouble(c.thirdWeight)
                    << ", \"fifthW\": " << fmtDouble(c.fifthWeight)
                    << ", \"completeTriad\": " << (c.hasCompleteTriad ? "true" : "false")
                    << "}";
                out << (ci + 1 < dump.candidates.size() ? ",\n" : "\n");
            }
            out << "      ]\n";
            out << "    }";
        }

        prevKey = ranked.front();
    }
    out << "\n  ]\n}\n";
}

// ══════════════════════════════════════════════════════════════════════════
// JSON output
// ══════════════════════════════════════════════════════════════════════════

// ── Stage 4c-i: key-agnostic cadence anchor (read-only diagnostic) ───────────
// Invokes the new authentic-cadence detector (composing/analysis/section/
// cadencekeyanchor) on the analyzed regions and emits its global tonic anchor +
// the detected cadences as an extra top-level "cadenceAnchor" key. Default OFF
// (dumpCadenceAnchor=false) so the standard .ours.json is byte-identical; the
// detector NEVER feeds the resolver/winner — it is measured, not wired (4c-ii).
static void writeCadenceAnchorJson(const std::vector<AnalyzedRegion>& regions,
                                   const std::set<int>& phraseBoundaryTicks,
                                   int keySignatureFifths,
                                   std::ostream& out)
{
    std::vector<analysis::CadenceRegionInput> input;
    input.reserve(regions.size());
    for (size_t ri = 0; ri < regions.size(); ++ri) {
        const auto& r = regions[ri];
        analysis::CadenceRegionInput ci;
        ci.startTick = r.startTick;
        ci.endTick = r.endTick;
        ci.rootPc = r.hasAnalyzedChord ? r.chord.identity.rootPc : -1;
        ci.quality = r.chord.identity.quality;
        ci.pitchClassMask = r.pcMask;
        // Stage 4c-iii: a region ENDS A PHRASE when a fermata sounds within
        // [startTick, endTick) — a structural (phrase-final) boundary — or it is
        // the final region of the piece (the piece-final cadence target).  This
        // is notation (key-agnostic), read from the engraving Score in main().
        bool endsPhrase = (ri + 1 == regions.size());
        if (!endsPhrase) {
            auto it = phraseBoundaryTicks.lower_bound(r.startTick);
            if (it != phraseBoundaryTicks.end() && *it < r.endTick) {
                endsPhrase = true;
            }
        }
        ci.endsPhrase = endsPhrase;
        input.push_back(ci);
    }

    const std::vector<analysis::AuthenticCadence> cadences =
        analysis::detectAuthenticCadences(input, keySignatureFifths);
    const analysis::CadenceKeyAnchor anchor =
        analysis::aggregateGlobalAnchor(cadences);

    out << "  \"cadenceAnchor\": {\n";
    out << "    \"keySignatureFifths\": " << keySignatureFifths            << ",\n";
    out << "    \"detected\": "    << (anchor.detected ? "true" : "false") << ",\n";
    out << "    \"tonicPc\": "     << anchor.tonicPc                       << ",\n";
    out << "    \"minorMode\": "   << (anchor.minorMode ? "true" : "false") << ",\n";
    out << "    \"confidence\": "  << fmtDouble(anchor.confidence, 5)      << ",\n";
    out << "    \"cadenceCount\": " << anchor.cadenceCount                 << ",\n";
    out << "    \"cadences\": [";
    for (size_t i = 0; i < cadences.size(); ++i) {
        const auto& c = cadences[i];
        out << (i == 0 ? "\n" : ",\n");
        out << "      {\"dominantTick\": " << c.dominantTick
            << ", \"tonicTick\": " << c.tonicTick
            << ", \"tonicPc\": " << c.tonicPc
            << ", \"minorMode\": " << (c.minorMode ? "true" : "false")
            << ", \"endsPhrase\": " << (c.endsPhrase ? "true" : "false")
            << ", \"chromaticLeadingTone\": " << (c.chromaticLeadingTone ? "true" : "false") << "}";
    }
    out << (cadences.empty() ? "" : "\n    ") << "]\n";
    out << "  }";
}

// ── Stage 4d-i: key-agnostic local-modulation detector (read-only diagnostic) ─
// Invokes the new local-modulation detector (composing/analysis/section/
// localmodulationdetector) on the analyzed regions and emits its candidate
// local-key spans + the key-agnostic global anchor as an extra top-level
// "modulation" key.  Default OFF (dumpModulation=false) so the standard .ours.json
// is byte-identical.  The detector reads ONLY chord root/quality + pitch content +
// the per-cadence list (NEVER the resolved key / KeyArea — the no-circularity rule,
// design §3) and NEVER feeds the resolver/winner — it is measured, not wired (4d-ii).
// The CadenceRegionInput stream here is constructed IDENTICALLY to
// writeCadenceAnchorJson (same key-agnostic fields), so the detector and the
// cadence diagnostic see the same inputs.
static void writeModulationJson(const std::vector<AnalyzedRegion>& regions,
                                const std::set<int>& phraseBoundaryTicks,
                                int keySignatureFifths,
                                std::ostream& out)
{
    std::vector<analysis::CadenceRegionInput> input;
    input.reserve(regions.size());
    for (size_t ri = 0; ri < regions.size(); ++ri) {
        const auto& r = regions[ri];
        analysis::CadenceRegionInput ci;
        ci.startTick = r.startTick;
        ci.endTick = r.endTick;
        ci.rootPc = r.hasAnalyzedChord ? r.chord.identity.rootPc : -1;
        ci.quality = r.chord.identity.quality;
        ci.pitchClassMask = r.pcMask;
        bool endsPhrase = (ri + 1 == regions.size());
        if (!endsPhrase) {
            auto it = phraseBoundaryTicks.lower_bound(r.startTick);
            if (it != phraseBoundaryTicks.end() && *it < r.endTick) {
                endsPhrase = true;
            }
        }
        ci.endsPhrase = endsPhrase;
        input.push_back(ci);
    }

    const analysis::ModulationDetectionResult mod =
        analysis::detectLocalModulations(input, keySignatureFifths);

    out << "  \"modulation\": {\n";
    out << "    \"keySignatureFifths\": " << keySignatureFifths << ",\n";
    out << "    \"anchorDetected\": " << (mod.anchor.detected ? "true" : "false") << ",\n";
    out << "    \"anchorTonicPc\": " << mod.anchor.tonicPc << ",\n";
    out << "    \"anchorMinorMode\": " << (mod.anchor.minorMode ? "true" : "false") << ",\n";
    out << "    \"spanCount\": " << mod.spans.size() << ",\n";
    out << "    \"spans\": [";
    for (size_t i = 0; i < mod.spans.size(); ++i) {
        const auto& s = mod.spans[i];
        out << (i == 0 ? "\n" : ",\n");
        out << "      {\"startTick\": " << s.startTick
            << ", \"endTick\": " << s.endTick
            << ", \"tonicPc\": " << s.tonicPc
            << ", \"minorMode\": " << (s.minorMode ? "true" : "false")
            << ", \"establishmentChords\": " << s.establishmentChords
            << ", \"confirmingCadenceCount\": " << s.confirmingCadenceCount
            << ", \"firstCadenceTonicTick\": " << s.firstCadenceTonicTick
            << ", \"agreesWithAnchor\": " << (s.agreesWithAnchor ? "true" : "false") << "}";
    }
    out << (mod.spans.empty() ? "" : "\n    ") << "]\n";
    out << "  }";
}

// ── J-key-i: scoped constrained-joint KEY decision (read-only diagnostic) ──────
// Invokes the new scoped-joint key-decision producer (composing/analysis/section/
// jointkeydecision) on the analyzed regions and emits, per region, BOTH the
// soft-only (config A) and the soft+scoped-joint (config B) key decision plus the
// structural flags, as an extra top-level "jointKey" object.  Default OFF
// (dumpJointKey=false) so the standard .ours.json is byte-identical.
//
// The producer integrates ONLY key-agnostic + local-candidate evidence (the
// committed cadence anchor + modulation detector, the analyzeKeyMode local
// candidates, the notated signature, the declared-mode notation fact) and the
// chord alternatives for the scoped-joint coupling.  The PRODUCTION resolved key
// is carried through as an ECHOED reference ONLY (prodTonicPc/prodIsMajor) — the
// decision never reads it (no-circularity; design §10).  It NEVER feeds the
// production resolver/winner/RN — it is measured, not wired (wiring is J-key-iii).
// The CadenceRegionInput-equivalent fields are built IDENTICALLY to
// writeCadenceAnchorJson / writeModulationJson (same key-agnostic inputs).
//
// @p declaredModeOrdinal is the NOTATED <mode> at tick 0 read from the engraving
// KeySigEvent in main(): -1 unknown, 0 major, 1 minor (the declared-mode hint, a
// notation fact — NOT a resolved key).
static void writeJointKeyJson(const std::vector<AnalyzedRegion>& regions,
                              const std::set<int>& phraseBoundaryTicks,
                              int keySignatureFifths,
                              int declaredModeOrdinal,
                              std::ostream& out)
{
    std::vector<analysis::JointKeyRegionInput> input;
    input.reserve(regions.size());
    for (size_t ri = 0; ri < regions.size(); ++ri) {
        const auto& r = regions[ri];
        analysis::JointKeyRegionInput ji;
        ji.startTick = r.startTick;
        ji.endTick = r.endTick;
        ji.rootPc = r.hasAnalyzedChord ? r.chord.identity.rootPc : -1;
        ji.quality = r.chord.identity.quality;
        ji.pitchClassMask = r.pcMask;
        bool endsPhrase = (ri + 1 == regions.size());
        if (!endsPhrase) {
            auto it = phraseBoundaryTicks.lower_bound(r.startTick);
            if (it != phraseBoundaryTicks.end() && *it < r.endTick) {
                endsPhrase = true;
            }
        }
        ji.endsPhrase = endsPhrase;
        ji.bassPc = r.bassPc;

        // existing analyzeKeyMode local candidates (SOFT prior)
        for (const auto& kc : r.keyRanked) {
            analysis::JointKeyLocalCandidate lc;
            lc.tonicPc = kc.tonicPc;
            lc.isMajor = kc.isMajor();
            lc.confidence = kc.normalizedConfidence;
            ji.localCandidates.push_back(lc);
        }
        // chord winner + alternatives (scoped-joint coupling)
        if (r.hasAnalyzedChord) {
            ji.chordAlts.push_back({ r.chord.identity.rootPc, r.chord.identity.quality });
        }
        for (const auto& alt : r.alternatives) {
            ji.chordAlts.push_back({ alt.identity.rootPc, alt.identity.quality });
        }
        // production resolved key — ECHOED reference only (never read by the decision)
        ji.prodTonicPc = r.key.tonicPc;
        ji.prodIsMajor = r.key.isMajor();
        // declared-mode hint (notation fact)
        ji.declaredModeKnown = (declaredModeOrdinal == 0 || declaredModeOrdinal == 1);
        ji.declaredModeMinor = (declaredModeOrdinal == 1);
        input.push_back(ji);
    }

    const analysis::JointKeyResult jk =
        analysis::decideJointKey(input, keySignatureFifths);

    out << "  \"jointKey\": {\n";
    out << "    \"keySignatureFifths\": " << keySignatureFifths << ",\n";
    out << "    \"declaredModeOrdinal\": " << declaredModeOrdinal << ",\n";
    out << "    \"anchorDetected\": " << (jk.anchor.detected ? "true" : "false") << ",\n";
    out << "    \"anchorTonicPc\": " << jk.anchor.tonicPc << ",\n";
    out << "    \"anchorMinorMode\": " << (jk.anchor.minorMode ? "true" : "false") << ",\n";
    // J-key-ii-redux Step 1: the anchor's own confidence + cadence count, so the
    // separability instrument can test whether anchor STRENGTH discriminates a true
    // global tonic from an internal tonicization the anchor over-detects (the
    // ~44%-pin-wrong precision trap). Additive; production stays byte-identical.
    out << "    \"anchorConfidence\": " << fmtDouble(jk.anchor.confidence, 5) << ",\n";
    out << "    \"anchorCadenceCount\": " << jk.anchor.cadenceCount << ",\n";
    out << "    \"modulationSpanCount\": " << jk.modulationSpanCount << ",\n";
    out << "    \"coupledCount\": " << jk.coupledCount << ",\n";
    out << "    \"hardPinnedCount\": " << jk.hardPinnedCount << ",\n";
    // J-key-ii: the full scoped key lattice (note-inferred home candidates ∪ spans)
    // — lets the safety instrument test DCML-key representability (the successor to
    // the J-key-i home-fifths exclusion rate).
    out << "    \"latticeStates\": [";
    for (size_t i = 0; i < jk.latticeStates.size(); ++i) {
        const auto& st = jk.latticeStates[i];
        out << (i == 0 ? "" : ", ")
            << "{\"tonicPc\": " << st.tonicPc
            << ", \"isMajor\": " << (st.isMajor ? "true" : "false") << "}";
    }
    out << "],\n";
    out << "    \"decisions\": [";
    for (size_t i = 0; i < jk.decisions.size(); ++i) {
        const auto& d = jk.decisions[i];
        out << (i == 0 ? "\n" : ",\n");
        out << "      {\"startTick\": " << d.startTick
            << ", \"endTick\": " << d.endTick
            << ", \"softTonicPc\": " << d.softTonicPc
            << ", \"softIsMajor\": " << (d.softIsMajor ? "true" : "false")
            << ", \"jointTonicPc\": " << d.jointTonicPc
            << ", \"jointIsMajor\": " << (d.jointIsMajor ? "true" : "false")
            << ", \"prodTonicPc\": " << d.prodTonicPc
            << ", \"prodIsMajor\": " << (d.prodIsMajor ? "true" : "false")
            << ", \"keyHardPinned\": " << (d.keyHardPinned ? "true" : "false")
            << ", \"chordPinned\": " << (d.chordPinned ? "true" : "false")
            << ", \"keyAmbiguous\": " << (d.keyAmbiguous ? "true" : "false")
            << ", \"coupled\": " << (d.coupled ? "true" : "false")
            << ", \"jointChanged\": " << (d.jointChanged ? "true" : "false")
            << ", \"anchorContributed\": " << (d.anchorContributed ? "true" : "false")
            << ", \"modulationContributed\": " << (d.modulationContributed ? "true" : "false")
            << ", \"homeMajorTonicPc\": " << d.homeMajorTonicPc
            << ", \"homeMinorTonicPc\": " << d.homeMinorTonicPc << "}";
    }
    out << (jk.decisions.empty() ? "" : "\n    ") << "]\n";
    out << "  }";
}

// ── Stage 6-tonic-i: tonicization (applied-chord) labeler (read-only diagnostic) ─
// Invokes the new functional-labeling pass (composing/analysis/function/
// tonicizationlabeler) on the analyzed regions and emits, per region, the
// candidate tonicization label (V/x, V7/x, viio/x, viiø7/x) or null, as an extra
// top-level "tonicizations" array. Default OFF (dumpTonicization=false) so the
// standard .ours.json is byte-identical; the labeler NEVER feeds the resolver/
// formatter — it PRODUCES a label and is measured, not wired (wiring is 6-tonic-ii).
// The labeler legitimately consumes the RESOLVED key per region (Stage 6 runs
// after key resolution).
static void writeTonicizationJson(const std::vector<AnalyzedRegion>& regions,
                                  std::ostream& out)
{
    std::vector<analysis::TonicizationRegionInput> input;
    input.reserve(regions.size());
    for (const auto& r : regions) {
        analysis::TonicizationRegionInput ti;
        ti.startTick = r.startTick;
        ti.endTick = r.endTick;
        ti.rootPc = r.hasAnalyzedChord ? r.chord.identity.rootPc : -1;
        ti.quality = r.chord.identity.quality;
        const uint32_t ext = r.chord.identity.extensions;
        ti.hasMinorSeventh = analysis::hasExtension(ext, analysis::Extension::MinorSeventh);
        ti.hasDiminishedSeventh = analysis::hasExtension(ext, analysis::Extension::DiminishedSeventh);
        ti.pitchClassMask = r.pcMask;
        // Prevailing RESOLVED key for this region (Stage 4 output).
        ti.keyTonicPc = r.key.tonicPc;
        ti.keyIsMajor = r.key.isMajor();
        ti.keySignatureFifths = r.key.keySignatureFifths;
        input.push_back(ti);
    }

    const std::vector<analysis::TonicizationLabel> labels =
        analysis::labelTonicizations(input);

    out << "  \"tonicizations\": [";
    for (size_t i = 0; i < labels.size(); ++i) {
        const auto& l = labels[i];
        out << (i == 0 ? "\n" : ",\n");
        out << "      {\"startTick\": " << regions[i].startTick
            << ", \"isApplied\": " << (l.isApplied ? "true" : "false")
            << ", \"label\": \"" << jsonEscape(l.label) << "\""
            << ", \"targetPc\": " << l.targetPc
            << ", \"targetDegree\": " << l.targetDegree
            << ", \"hasSeventh\": " << (l.hasSeventh ? "true" : "false")
            << ", \"leadingTonePc\": " << l.leadingTonePc << "}";
    }
    out << (labels.empty() ? "" : "\n    ") << "]";
}

// ── Phase 5c Step M: the dormant Layer-5 (FUNCTION) would-be labels (read-only) ──
// Drives the dormant L5 over the analyzed regions — the SAME legacy region substrate as
// the 53/24/53 BIR gate baseline (r.chord.identity + r.key + tones + pcMask are exactly
// classifyRelationalLabel / assembleFunctionOutput's inputs) — and emits, per region, the
// would-be L5 Roman numeral (classifyRelationalLabel.label, carried verbatim through the §7
// assembleFunctionOutput) + its relational role + the open mark, ALONGSIDE the UNGUARDED
// inline formatRomanNumeral baseline (the §5.6 applied-divergence comparator). Read-only /
// measurement-only: the dormant L5 NEVER feeds a production output (default OFF ⇒ the
// standard .ours.json is byte-identical). L5 is ADDITIVE over L4 (§7) — the committed root
// (committedIdentity.rootPc, echoed for the class-(b) check) is UNCHANGED here; the
// relational label only changes the RN STRING. Spec: cowork_layer5_function_design.md
// §5.6/§7; cc_instruction Phase-5c Step M.
static const char* relationalRoleName(analysis::RelationalRole role)
{
    switch (role) {
    case analysis::RelationalRole::None:             return "None";
    case analysis::RelationalRole::AugmentedSixth:   return "AugmentedSixth";
    case analysis::RelationalRole::Neapolitan:       return "Neapolitan";
    case analysis::RelationalRole::AppliedSecondary: return "AppliedSecondary";
    case analysis::RelationalRole::ModalMixture:     return "ModalMixture";
    }
    return "None";
}

static void writeL5Json(const std::vector<AnalyzedRegion>& regions,
                        const KeyModeAnalysisResult& globalKey,
                        std::ostream& out)
{
    // The next committed root per region (the applied resolution target — §5.6).
    auto nextRootOf = [&](size_t i) -> int {
        for (size_t j = i + 1; j < regions.size(); ++j) {
            if (regions[j].hasAnalyzedChord && regions[j].chord.identity.rootPc >= 0) {
                return regions[j].chord.identity.rootPc;
            }
        }
        return -1;
    };

    std::vector<analysis::FunctionUnitAssembly> units;
    units.reserve(regions.size());
    std::vector<std::string> inlineRoman;   // the UNGUARDED inline formatRomanNumeral baseline (§5.6)
    std::vector<int> nextRoots;
    for (size_t i = 0; i < regions.size(); ++i) {
        const auto& r = regions[i];
        const int nextRoot = nextRootOf(i);
        nextRoots.push_back(nextRoot);

        // The Step-5 relational classifier input — mapped from the legacy region (§5.6).
        analysis::RelationalLabelInput in;
        in.identity = r.chord.identity;
        in.keyFifths = r.key.keySignatureFifths;
        in.keyMode = r.key.mode;
        in.keyTonicPc = r.key.tonicPc;
        in.nextRootPc = nextRoot;
        in.pitchClassMask = r.pcMask;
        for (const auto& t : r.tones) {
            if (t.tpc >= 0) { in.noteTpcs.push_back(t.tpc); }
        }
        const analysis::RelationalLabel rel = r.hasAnalyzedChord
            ? analysis::classifyRelationalLabel(in)
            : analysis::RelationalLabel{};

        analysis::FunctionUnitAssembly u;
        u.startTick = r.startTick;
        u.endTick = r.endTick;
        u.committedIdentity = r.chord.identity;
        u.chord.rootPc = r.chord.identity.rootPc;
        u.chord.quality = r.chord.identity.quality;
        u.committed = r.hasAnalyzedChord;
        u.relational = rel;
        u.openMark = false;          // the legacy region substrate carries no L4 abstain → no open mark
        u.resolverConfidence = 0.0;  // no resolver here (the override needs the L4-decoder carried contract)
        units.push_back(u);

        // The UNGUARDED inline path baseline (§5.6): what formatRomanNumeral emits given the
        // next root WITHOUT the foreign-tone guard — the comparator the §5.6 divergence names
        // (it "would write V7/III"). Built with the PUBLIC formatter on a hand-set function
        // context (the same fields the L5 module's makeResult sets), so it faithfully mirrors
        // the production inline path; not a re-implementation.
        std::string inl;
        if (r.hasAnalyzedChord) {
            ChordAnalysisResult cr;
            cr.identity = r.chord.identity;
            cr.function.degree = analysis::region::diatonicDegreeForRootPc(
                r.chord.identity.rootPc, r.key.keySignatureFifths, r.key.mode);
            cr.function.diatonicToKey = (cr.function.degree >= 0);
            cr.function.keyTonicPc = r.key.tonicPc;
            cr.function.keyMode = r.key.mode;
            cr.function.nextRootPc = nextRoot;
            inl = analysis::ChordSymbolFormatter::formatRomanNumeral(cr);
        }
        inlineRoman.push_back(inl);
    }

    // §7: invoke the dormant assembleFunctionOutput over the score's units (empty cadences /
    // modulations on this measurement substrate) — exercising the §7 assembly over real
    // scores; it carries each unit's relational.label as romanNumeral verbatim.
    const analysis::FunctionLayerOutput out5 = analysis::assembleFunctionOutput(
        units, /*cadences=*/{}, /*modulations=*/{},
        globalKey.tonicPc, /*homeMinor=*/!globalKey.isMajor());

    out << "  \"l5\": [";
    for (size_t i = 0; i < out5.units.size(); ++i) {
        const auto& u = out5.units[i];
        out << (i == 0 ? "\n" : ",\n");
        out << "      {\"startTick\": " << u.startTick
            << ", \"endTick\": " << u.endTick
            << ", \"rootPitchClass\": " << u.committedIdentity.rootPc
            << ", \"l5RomanNumeral\": \"" << jsonEscape(u.romanNumeral) << "\""
            << ", \"role\": \"" << relationalRoleName(u.relationalRole) << "\""
            << ", \"openMark\": " << (u.openMark ? "true" : "false")
            << ", \"inlineRomanNumeral\": \"" << jsonEscape(inlineRoman[i]) << "\""
            << ", \"nextRootPc\": " << nextRoots[i] << "}";
    }
    out << (out5.units.empty() ? "" : "\n    ") << "]";
}

static void writeJson(
    const std::vector<AnalyzedRegion>& regions,
    const std::string& sourceName,
    const std::string& presetName,
    const KeyModeAnalysisResult& globalKey,
    const char* analysisPath,
    std::ostream& out,
    bool dumpCadenceAnchor = false,
    const std::set<int>& phraseBoundaryTicks = {},
    int notatedSignatureFifths = 0,
    bool dumpTonicization = false,
    bool dumpModulation = false,
    bool dumpJointKey = false,
    int declaredModeOrdinal = -1,
    bool dumpL5 = false)
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

    if (dumpCadenceAnchor || dumpTonicization || dumpModulation || dumpJointKey || dumpL5) {
        out << "  ],\n";
        bool wroteExtra = false;
        if (dumpCadenceAnchor) {
            writeCadenceAnchorJson(regions, phraseBoundaryTicks, notatedSignatureFifths, out);
            wroteExtra = true;
        }
        if (dumpModulation) {
            if (wroteExtra) {
                out << ",\n";
            }
            writeModulationJson(regions, phraseBoundaryTicks, notatedSignatureFifths, out);
            wroteExtra = true;
        }
        if (dumpJointKey) {
            if (wroteExtra) {
                out << ",\n";
            }
            writeJointKeyJson(regions, phraseBoundaryTicks, notatedSignatureFifths,
                              declaredModeOrdinal, out);
            wroteExtra = true;
        }
        if (dumpTonicization) {
            if (wroteExtra) {
                out << ",\n";
            }
            writeTonicizationJson(regions, out);
            wroteExtra = true;
        }
        if (dumpL5) {
            if (wroteExtra) {
                out << ",\n";
            }
            writeL5Json(regions, globalKey, out);
            wroteExtra = true;
        }
        out << "\n}\n";
    } else {
        out << "  ]\n";
        out << "}\n";
    }
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
    // Must match the `templates` array order in RuleBasedChordAnalyzer::analyzeChord
    // (and the kMasks table in harmonicfunctionlayer.cpp) — all 17 of analysis::kTemplateCount.
    static constexpr const char* NAMES[] = {
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
        "Aug dom7 {0,4,8,10}",
        "Sus2 {0,2,7}",
        "Sus4 {0,5,7,10}",
        "Sus4+Maj7 {0,5,7,11}",
        "Sus4#5 {0,5,8,10}",
        "Sus#4 {0,6,7}",
        "Power {0,7}",
    };
    static_assert(sizeof(NAMES) / sizeof(NAMES[0]) == analysis::kTemplateCount,
                  "diagTemplateName must list all analysis::kTemplateCount templates");
    if (tplIdx < 0 || tplIdx >= static_cast<int>(analysis::kTemplateCount)) { return "Unknown"; }
    return NAMES[static_cast<size_t>(tplIdx)];
}

// Context banner for each diagnosed region (Stage 2.3 addendum). diagnoseChord() replays
// the production pipeline with whatever temporal context it is handed. The batch dump
// passes NULL (region-in-isolation — correct per the 2.3 scoping decision; threading the
// real inter-region context is roadmap 2.3b). The banner makes that explicit so an
// rcb-class investigation can never mistake an isolated dump for an in-context verdict.
// Conditional by design: a future 2.3b caller that threads a real context gets an accurate
// summary instead of a misleading NONE. Never returns empty.
static std::string diagContextBanner(const analysis::ChordTemporalContext* ctx, int keyFifths)
{
    if (!ctx) {
        return "NONE (isolated region — progression signals computed with null temporal "
               "context; inter-region effects such as rootContinuityBonus feed are NOT "
               "represented. For in-context diagnosis see roadmap 2.3b.)";
    }
    std::ostringstream os;
    os << "PRESENT (previousRootPc=" << ctx->previousRootPc;
    if (ctx->previousRootPc >= 0) {
        os << " [" << diagPcName(ctx->previousRootPc, keyFifths) << "]";
    }
    os << ", previousBassPc=" << ctx->previousBassPc
       << ", nextRootPc=" << ctx->nextRootPc
       << ", consecutiveBassStepwiseCount=" << ctx->consecutiveBassStepwiseCount
       << ", regionMetricWeight=" << fmtDouble(ctx->regionMetricWeight, 3)
       << "). Inter-region progression signals ARE represented.";
    return os.str();
}

static void writeDiagnosticJson(
    const std::vector<AnalyzedRegion>& regions,
    const std::set<int>& diagnoseMeasures,
    const std::string& sourceName,
    const analysis::ChordAnalyzerPreferences& chordPrefs,
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

        // Run the diagnostic — a VIEW into the production pipeline (Stage 2.3).
        // diagnoseChord() replays analyzeChord + applyIter8691Pedal +
        // applyPostScoringGates with the SAME preset prefs the batch run used, so
        // diag.finalWinner is the production winner for this region in isolation.
        // (No inter-region temporal context is threaded here: the dump shows the
        // region's own vertical/competition evidence, not its neighbours' signals.)
        // NULL temporal context — region-in-isolation (roadmap 2.3b threads the real
        // context). Named so the banner below reflects whatever is actually passed.
        const analysis::ChordTemporalContext* diagContext = nullptr;
        const auto diag = diagAnalyzer.diagnoseChord(
            region->tones,
            region->key.keySignatureFifths,
            region->key.mode,
            diagContext,
            chordPrefs);

        const int keyFifths = region->key.keySignatureFifths;

        if (!firstBlock) { out << ",\n"; }
        firstBlock = false;

        out << "    {\n";
        // Banner FIRST — every diagnosed region states its temporal context explicitly so
        // an isolated dump can never be mistaken for an in-context verdict (Stage 2.3).
        out << "      \"context\": \"" << jsonEscape(diagContextBanner(diagContext, keyFifths)) << "\",\n";
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

        // ── FINAL winner — the production winner BY CONSTRUCTION ────────
        // (diagnoseChord replays analyzeChord + applyIter8691Pedal +
        // applyPostScoringGates; diag.finalWinner == analyzeWithGates().front()).
        out << "      \"final_winner\": ";
        if (diag.hasWinner) {
            const auto& w = diag.finalWinner.identity;
            out << "{"
                << "\"root_pc\": " << w.rootPc << ", "
                << "\"root_name\": \"" << diagPcName(w.rootPc, keyFifths) << "\", "
                << "\"bass_pc\": " << w.bassPc << ", "
                << "\"quality\": \"" << diagQualityName(w.quality) << "\", "
                << "\"score\": " << fmtDouble(w.score, 5) << ", "
                << "\"symbol\": \"" << jsonEscape(
                       analysis::ChordSymbolFormatter::formatSymbol(diag.finalWinner, keyFifths))
                << "\"}";
        } else {
            out << "null";
        }
        out << ",\n";

        // ── ORACLE — vertical-only per-cell breakdown (≥ 75 % of top cell) ──
        // No progression signal; the values the scoring oracle handed to the
        // competition pipeline. Labeled ORACLE: these are pre-competition.
        const double oracleThreshold = diag.oracleCells.empty()
                                     ? 0.0
                                     : diag.oracleCells.front().verticalScore * 0.75;
        out << "      \"oracle_top\": [\n";
        bool firstOracle = true;
        for (const auto& c : diag.oracleCells) {
            if (c.verticalScore < oracleThreshold) { break; }
            if (!firstOracle) { out << ",\n"; }
            firstOracle = false;
            out << "        {"
                << "\"bass_pc\": " << c.bassPc << ", "
                << "\"root_pc\": " << c.rootPc << ", "
                << "\"root_name\": \"" << diagPcName(c.rootPc, keyFifths) << "\", "
                << "\"template_idx\": " << c.templateIdx << ", "
                << "\"template_name\": \"" << diagTemplateName(c.templateIdx) << "\", "
                << "\"quality\": \"" << diagQualityName(c.quality) << "\", "
                << "\"vertical_score\": " << fmtDouble(c.verticalScore, 5) << ", "
                << "\"basis_indep\": " << fmtDouble(c.basisIndep, 5) << ", "
                << "\"basis_dep\": " << fmtDouble(c.basisDep, 5) << ", "
                << "\"complexity_factor\": " << fmtDouble(c.complexityFactor, 5) << ", "
                << "\"aug_factor\": " << fmtDouble(c.augFactor, 5) << ", "
                << "\"w_complete\": " << fmtDouble(c.wCompleteBonus, 5) << ", "
                << "\"applied_bass_bonus\": " << fmtDouble(c.appliedBassBonus, 5)
                << "}";
        }
        out << "\n      ],\n";

        // ── COMPETITION — winning bass group, progression signals applied ──
        // Scores are authoritative (the pipeline's rawCandidates); rcb shows the
        // Gate R outcome. Labeled COMPETITION: these are post-oracle.
        out << "      \"competition\": [\n";
        bool firstComp = true;
        for (const auto& c : diag.competition) {
            if (!firstComp) { out << ",\n"; }
            firstComp = false;
            out << "        {"
                << "\"bass_pc\": " << c.bassPc << ", "
                << "\"root_pc\": " << c.rootPc << ", "
                << "\"root_name\": \"" << diagPcName(c.rootPc, keyFifths) << "\", "
                << "\"template_idx\": " << c.templateIdx << ", "
                << "\"quality\": \"" << diagQualityName(c.quality) << "\", "
                << "\"competition_score\": " << fmtDouble(c.competitionScore, 5) << ", "
                << "\"rcb\": " << fmtDouble(c.rootContinuityBonus, 5) << ", "
                << "\"rcb_raw\": " << fmtDouble(c.rootContinuityBonusRaw, 5) << ", "
                << "\"rcb_withheld_by_gate_r\": "
                << (c.rootContinuityWithheldByGateR ? "true" : "false") << ", "
                << "\"resolution\": " << fmtDouble(c.resolutionBonus, 5) << ", "
                << "\"inversion_ctx\": " << fmtDouble(c.inversionContextBonus, 5) << ", "
                << "\"w_seq\": " << fmtDouble(c.wSeqBonus, 5) << ", "
                << "\"w_dim\": " << fmtDouble(c.wDimBonus, 5) << ", "
                << "\"step_in\": " << fmtDouble(c.stepInBonus, 5) << ", "
                << "\"step_out\": " << fmtDouble(c.stepOutBonus, 5)
                << "}";
        }
        out << "\n      ],\n";

        // ── POST-GATES — which stage moved the winner ───────────────────
        out << "      \"post_gates\": {";
        if (diag.postGates.hasCompetitionWinner) {
            const auto& pg = diag.postGates;
            out << "\"competition_winner\": {"
                << "\"root_pc\": " << pg.competitionWinnerRootPc << ", "
                << "\"bass_pc\": " << pg.competitionWinnerBassPc << ", "
                << "\"quality\": \"" << diagQualityName(pg.competitionWinnerQuality) << "\", "
                << "\"score\": " << fmtDouble(pg.competitionWinnerScore, 5) << "}, "
                << "\"iter8691_changed_winner\": "
                << (pg.iter8691ChangedWinner ? "true" : "false") << ", "
                << "\"gates_changed_winner\": "
                << (pg.gatesChangedWinner ? "true" : "false");
        } else {
            out << "\"competition_winner\": null";
        }
        out << "},\n";

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
                           " [--preset Standard|Jazz|Modal|Baroque|Contemporary|Default]"
                           " [--dump-regions batch|notation|notation-premerge]"
                           " [--section-level]"
                           " [--validate-slices]"
                           " [--decode-keymode]"
                           " [--decode-chords]"
                           " [--ignore-declared-mode]"
                           " [--diagnose-measures N[,N...]]"
                           " [--dump-key-candidates TICK[,TICK...]]"
                           " [--dump-cadence-anchor]"
                           " [--dump-modulation]"
                           " [--dump-tonicization]\n"
        << "\n"
        << "  Loads a score, runs harmonic analysis (ChordAnalyzer + KeyModeAnalyzer)\n"
        << "  and writes JSON to output.json, or to stdout if no output file given.\n"
        << "\n"
        << "  --preset  Apply a named mode prior preset (default: Standard).\n"
        << "            Run the same corpus under different presets and diff the\n"
        << "            results to identify mode-inference improvements.\n"
        << "            'Default' is not a tuning preset: it reproduces the live\n"
        << "            product's out-of-box config (app mode-prior settings defaults\n"
        << "            + untouched chord prefs) for measurement (Stage 2.4 V4).\n"
        << "  --dump-regions <mode>\n"
        << "            Select which analysis path to serialize. 'batch' writes the\n"
        << "            tool's current batch path, 'notation' writes the live notation\n"
        << "            bridge result, 'notation-premerge' writes the notation\n"
        << "            bridge regions before same-chord merge/absorption.\n"
        << "  --section-level\n"
        << "            (Stage 2.2 prototype) Run the user-facing section pipeline\n"
        << "            (analyzeSection: measure layout, gap-tone insertion, key/mode\n"
        << "            stabilization, sparse-quality refinement) on top of the batch\n"
        << "            region stream. Default OFF. Only affects --dump-regions batch.\n"
        << "  --validate-slices\n"
        << "            (Layer-2 diagnostic) Build the layer-1 note model, run the REAL\n"
        << "            changePointSlices, and check the slice invariants (boundary-set\n"
        << "            match, covering/no-gaps, positive width, constant sonority, tie\n"
        << "            spans, determinism) against an INDEPENDENT oracle recomputed from\n"
        << "            the note model. Emits one per-stem JSON object and RETURNS before\n"
        << "            any analysis runs (the analysis pipeline is never invoked, so its\n"
        << "            output is unchanged). Exit 0 if all invariants held, 2 if any\n"
        << "            failed. Default OFF.\n"
        << "  --decode-keymode\n"
        << "            (Layer-3 diagnostic) Build the layer-1 note model, run the REAL\n"
        << "            layer-2 slicer, run the isolated layer-3 key/mode SEQUENCE decoder\n"
        << "            (keymodesequence) over the slices, and emit its chosen key/mode per\n"
        << "            slice in the same region shape the held-out GT harness reads. The\n"
        << "            decoder is NOT wired into the live analyzer; this RETURNS before any\n"
        << "            analysis runs, so production output is unchanged. Default OFF.\n"
        << "  --seq-change-base N | --seq-relative-extra N | --seq-per-fifth N |\n"
        << "  --seq-window-beats N | --seq-uncertain N | --seq-topk N | --seq-max-alts N\n"
        << "            (Layer-3 BOUNDED SWEEP) Override the decoder-private\n"
        << "            KeyModeSequencePreferences for the --decode-keymode path only\n"
        << "            (read nowhere else; production stays byte-identical). Default =\n"
        << "            the committed decoder defaults.\n"
        << "  --decode-chords\n"
        << "            (Layer-4 diagnostic) Build the layer-1 note model, run the REAL\n"
        << "            layer-2 slicer, run the isolated layer-4 per-slice CHORD decoder\n"
        << "            (chordslicedecoder) over the slices, and emit its chosen chord\n"
        << "            (root + quality + inversion + confidence + uncertain), the focal-\n"
        << "            slice sounding pitch classes, and the per-note chord-tone / non-\n"
        << "            chord-tone MEMBERSHIP split (Increment B). NOT wired into the live\n"
        << "            analyzer; this RETURNS before any analysis runs, so production\n"
        << "            output is unchanged. Default OFF.\n"
        << "  --chord-context-slices N | --chord-topk N | --chord-uncertain-margin N |\n"
        << "  --chord-min-pcs N | --chord-max-context-slices N | --chord-min-harmony-pcs N |\n"
        << "  --chord-memb-salience N | --chord-memb-penalty N | --chord-memb-ref-dur N |\n"
        << "  --chord-stepwise-tol N | --chord-no-membership | --chord-no-two-pass\n"
        << "            (Layer-4 sweep) Override the decoder-private\n"
        << "            ChordSliceDecoderPreferences for the --decode-chords path only\n"
        << "            (read nowhere else; production stays byte-identical). Default =\n"
        << "            the committed decoder defaults.\n"
        << "  --ignore-declared-mode\n"
        << "            (Stage 4b-i measurement floor) Force the key resolver to drop\n"
        << "            the score's declared key-signature mode (declaredMode = nullopt),\n"
        << "            so key inference is purely note-based: no declared-mode hint, no\n"
        << "            partial-signature correction, note-based opening. Default OFF =\n"
        << "            byte-identical to mode-present. The 'no-crutch floor' condition.\n"
        << "  --diagnose-measures N[,N,...]\n"
        << "            Per-measure diagnostic mode. For each listed measure number,\n"
        << "            emits a JSON block with collected notes, per-PC weights, and\n"
        << "            the full root × template scoring breakdown. Output replaces the\n"
        << "            standard regions JSON. Example: --diagnose-measures 1,2,3,5,7\n"
        << "  --dump-key-candidates TICK[,TICK,...]\n"
        << "            (Stage-4 emission instrument, read-only) For each region whose\n"
        << "            [startTick,endTick) contains a listed tick, emits the per-region\n"
        << "            key-resolution trace and the full per-candidate emission score\n"
        << "            breakdown (the six KeyModeAnalyzer terms + declared penalty +\n"
        << "            disambiguation). Production analysis is byte-identical; the dump\n"
        << "            only serializes scores already computed. Output replaces the\n"
        << "            standard regions JSON. Example: --dump-key-candidates 0,4800,9600\n"
        << "  --dump-cadence-anchor\n"
        << "            (Stage 4c-i, read-only) Append a top-level \"cadenceAnchor\" key\n"
        << "            to the standard regions JSON: the key-agnostic authentic-cadence\n"
        << "            detector's global (tonicPc, mode, confidence) anchor plus the\n"
        << "            detected cadences. The detector reads only chord root/quality +\n"
        << "            pitch content (never the resolved key) and NEVER feeds scoring;\n"
        << "            production analysis is byte-identical. Default OFF.\n"
        << "  --dump-tonicization\n"
        << "            (Stage 6-tonic-i, read-only) Append a top-level \"tonicizations\"\n"
        << "            array to the standard regions JSON: per region, the candidate\n"
        << "            secondary-dominant / applied-leading-tone label (V/x, V7/x,\n"
        << "            viio/x, viiø7/x) or none. The labeler consumes the resolved key\n"
        << "            but only PRODUCES a label — it NEVER feeds scoring or the emitted\n"
        << "            Roman numeral; production analysis is byte-identical. Default OFF.\n"
        << "  --dump-l5\n"
        << "            (Phase 5c Step M, read-only) Append a top-level \"l5\" array to the\n"
        << "            standard regions JSON: per region, the dormant Layer-5 (FUNCTION)\n"
        << "            would-be Roman numeral (classifyRelationalLabel, carried through the\n"
        << "            §7 assembleFunctionOutput) + role + open mark, plus the unguarded\n"
        << "            inline formatRomanNumeral baseline (the §5.6 applied-divergence\n"
        << "            comparator). The dormant L5 NEVER feeds production; the committed\n"
        << "            root is unchanged (L5 is additive over L4). Byte-identical. Default OFF.\n"
        << "  --dump-fullspine\n"
        << "            (E0, read-only DIAGNOSTIC — returns before analyzeScore) Chain the\n"
        << "            complete dormant spine L1→L2→L3(live key)→L4-decoder→L5 (all six\n"
        << "            function units incl. the §5.5 case-4 fine-grain override live on the\n"
        << "            decoder substrate) and write a per-stem JSON side file: the standard\n"
        << "            regions[] shape (graded by compare_rn/compare_analyses) enriched with\n"
        << "            the per-slice L4 decision/confidence/open-question + L5 role/open-mark/\n"
        << "            confidence + per-region cadences/modulations + wall-time. Base RNs are\n"
        << "            TRIAD-LEVEL (the L4→L5 carry drops the seventh/extensions — faithful,\n"
        << "            not synthesized). NO production consumer; byte-identical. Default OFF.\n"
        << "  --dump-l6\n"
        << "            (L6, read-only DIAGNOSTIC) Run --dump-fullspine AND append an additive\n"
        << "            \"l6\" object: the dormant Layer-6 grouping structure assembled from the\n"
        << "            spine's L1.5 boundaries + L5 cadences + per-slice local-key track —\n"
        << "            punctuation-spans, key-areas, cadence-to-span alignment (§5.1–§5.5). NO\n"
        << "            production consumer; fullspine output byte-identical without it. Default OFF.\n"
        << "  --dump-modulation\n"
        << "            (Stage 4d-i, read-only) Append a top-level \"modulation\" key to\n"
        << "            the standard regions JSON: the key-agnostic local-modulation\n"
        << "            detector's committed candidate local-key spans (each established\n"
        << "            by a sustained consistent run AND confirmed by a V->I cadence) plus\n"
        << "            the key-agnostic global anchor. The detector reads only chord\n"
        << "            root/quality + pitch content + the per-cadence list (NEVER the\n"
        << "            resolved key/KeyArea) and NEVER feeds scoring; production analysis\n"
        << "            is byte-identical. Default OFF.\n"
        << "  --dump-joint-key\n"
        << "            (J-key-i, read-only) Append a top-level \"jointKey\" object to the\n"
        << "            standard regions JSON: the scoped constrained-joint KEY decision\n"
        << "            per region, in BOTH configs (soft-only and soft+scoped-joint), plus\n"
        << "            the structural flags (hard-pinned / chord-pinned / coupled). The\n"
        << "            producer integrates only key-agnostic + local-candidate evidence\n"
        << "            (the production resolved key is an ECHOED reference, never read) and\n"
        << "            NEVER feeds the resolver/winner/RN; production analysis is\n"
        << "            byte-identical. Default OFF.\n"
        << "  --joint-key-wiring\n"
        << "            (J-key-iii, INTENTIONAL behavior change) WIRE the scoped\n"
        << "            constrained-joint KEY decision into production: analyzeRegions\n"
        << "            overrides each region's resolved key with decideJointKey's SOFT\n"
        << "            decision and re-emits the chord under it (key-changed regions).\n"
        << "            Off ⇒ byte-identical baseline. Default OFF (HELD until ratified).\n"
        << "\n"
        << "  Returns 0 on success, non-zero on failure.\n";
}

// ══════════════════════════════════════════════════════════════════════════
// Layer 2 — corpus property-validation of the REAL slicer (--validate-slices)
//
// DIAGNOSTIC ONLY. This path does NOT invoke or alter the analysis pipeline:
// main() returns immediately after this runs, so analyzeScore / analyzeRegions
// are never reached. It builds the layer-1 note model, runs the REAL C++
// changePointSlices, and checks the §2 invariants against an INDEPENDENT oracle
// recomputed from model.notes() — NOT the slicer's own internal boundary vector.
// Emits one JSON object (the per-stem result); a Python driver iterates the 353
// canonical stems and aggregates. Off by default ⇒ analysis output unchanged.
// ══════════════════════════════════════════════════════════════════════════

namespace {

using mu::composing::analysis::notemodel::NoteEvent;
using mu::composing::analysis::notemodel::NoteModel;
using mu::composing::analysis::slicing::Slice;

// A single invariant violation (the §2 stop condition payload).
struct SliceViolation {
    std::string invariant;   ///< which §2 check failed (e.g. "boundary-set-match")
    std::string detail;      ///< human-readable description
    long long   tickA = 0;   ///< the offending tick (or slice start)
    long long   tickB = 0;   ///< second tick where a pair/span is involved
};

// Run the §2 invariant suite + §3 stats for one score. Returns the per-stem
// JSON object as a string. `ok` is set false iff any invariant failed.
static std::string runSliceValidation(const Score* score, const std::string& stem, bool& ok)
{
    ok = true;
    std::vector<SliceViolation> violations;

    // ── Build the layer-1 note model (the slicer's only input). ─────────────
    const NoteModel model = NoteModel::build(score);

    // ── INDEPENDENT ORACLE: recompute the expected boundary set from
    //    model.notes(), applying the SAME eligibility predicate the slicer reads
    //    (plays && visible && staffEligible). This is built here in the harness —
    //    it does NOT touch the slicer's internal boundary vector. ──────────────
    std::set<int> bexp;                       // expected boundary ticks
    std::set<int> eligibleOnsets;
    std::set<int> eligibleReleases;
    std::vector<const NoteEvent*> eligible;   // eligible notes, for the overlap recompute
    eligible.reserve(model.notes().size());
    for (const NoteEvent& e : model.notes()) {
        if (!(e.plays && e.visible && e.staffEligible)) {
            continue;
        }
        eligible.push_back(&e);
        bexp.insert(e.onset);
        bexp.insert(e.release);
        eligibleOnsets.insert(e.onset);
        eligibleReleases.insert(e.release);
    }

    // ── Run the REAL slicer (timed for the §3 performance stat — only the
    //    slicer call, not the checks). Call twice for determinism (#6). ────────
    const auto t0 = std::chrono::steady_clock::now();
    const std::vector<Slice> slices = mu::composing::analysis::slicing::changePointSlices(model);
    const auto t1 = std::chrono::steady_clock::now();
    const std::vector<Slice> slices2 = mu::composing::analysis::slicing::changePointSlices(model);
    const double sliceMs =
        std::chrono::duration_cast<std::chrono::duration<double, std::milli>>(t1 - t0).count();

    // #6 — determinism: identical output across two calls. ────────────────────
    bool deterministic = (slices.size() == slices2.size());
    if (deterministic) {
        for (std::size_t i = 0; i < slices.size(); ++i) {
            if (slices[i].start != slices2[i].start || slices[i].end != slices2[i].end) {
                deterministic = false;
                violations.push_back({ "determinism",
                    "two changePointSlices calls disagree at index " + std::to_string(i),
                    slices[i].start, slices2[i].start });
                break;
            }
        }
    } else {
        violations.push_back({ "determinism",
            "two changePointSlices calls returned different slice counts",
            static_cast<long long>(slices.size()),
            static_cast<long long>(slices2.size()) });
    }

    // ── Empty-domain case: < 2 distinct boundaries ⇒ expect an empty slice
    //    list. (No eligible notes, or a single zero-width boundary.) ───────────
    if (bexp.size() < 2) {
        if (!slices.empty()) {
            violations.push_back({ "empty-domain",
                "expected empty slice list (< 2 distinct eligible boundaries) but got "
                + std::to_string(slices.size()) + " slices",
                static_cast<long long>(bexp.size()),
                static_cast<long long>(slices.size()) });
        }
    } else {
        // #1 — boundary-set match: the set of all slice start/end ticks equals
        //      the independent oracle's boundary set (completeness + no-spurious
        //      + no-missed, in one equality). ────────────────────────────────
        std::set<int> sliceBoundaries;
        for (const Slice& s : slices) {
            sliceBoundaries.insert(s.start);
            sliceBoundaries.insert(s.end);
        }
        if (sliceBoundaries != bexp) {
            // Report the first divergence in each direction.
            for (int b : bexp) {
                if (!sliceBoundaries.count(b)) {
                    violations.push_back({ "boundary-set-match",
                        "expected boundary missing from slicer output", b, 0 });
                    break;
                }
            }
            for (int b : sliceBoundaries) {
                if (!bexp.count(b)) {
                    violations.push_back({ "boundary-set-match",
                        "spurious boundary in slicer output (not in oracle)", b, 0 });
                    break;
                }
            }
        }

        // #2 — covering, no gaps/overlaps; endpoints anchored to the domain. ──
        if (slices.front().start != *bexp.begin()) {
            violations.push_back({ "covering-front",
                "first slice start != domain start", slices.front().start, *bexp.begin() });
        }
        if (slices.back().end != *bexp.rbegin()) {
            violations.push_back({ "covering-back",
                "last slice end != domain end", slices.back().end, *bexp.rbegin() });
        }
        for (std::size_t i = 0; i + 1 < slices.size(); ++i) {
            if (slices[i].end != slices[i + 1].start) {
                violations.push_back({ "covering-contiguous",
                    "gap/overlap between consecutive slices at index " + std::to_string(i),
                    slices[i].end, slices[i + 1].start });
                break;
            }
        }
    }

    // #3 — positive width: every emitted slice has start < end. ───────────────
    for (std::size_t i = 0; i < slices.size(); ++i) {
        if (!(slices[i].start < slices[i].end)) {
            violations.push_back({ "positive-width",
                "non-positive-width slice at index " + std::to_string(i),
                slices[i].start, slices[i].end });
            break;
        }
    }

    // #4 — constant tonal sonority (INDEPENDENT recompute): within each slice
    //      (s,e) no eligible note onset or release lies strictly inside. The
    //      eligible overlap set is therefore constant across the slice. ────────
    for (const Slice& sl : slices) {
        bool bad = false;
        for (const NoteEvent* e : eligible) {
            if (sl.start < e->onset && e->onset < sl.end) {
                violations.push_back({ "constant-sonority",
                    "eligible onset strictly inside slice [" + std::to_string(sl.start)
                    + "," + std::to_string(sl.end) + ")", sl.start, e->onset });
                bad = true;
                break;
            }
            if (sl.start < e->release && e->release < sl.end) {
                violations.push_back({ "constant-sonority",
                    "eligible release strictly inside slice [" + std::to_string(sl.start)
                    + "," + std::to_string(sl.end) + ")", sl.start, e->release });
                bad = true;
                break;
            }
        }
        if (bad) {
            break;
        }
    }

    // #5 — ties don't split (cross-layer spot check): every eligible note's
    //      tie-resolved endpoints appear as slicer boundaries, with onset<=release.
    //      Structurally subsumed by #1 if L1 is correct; asserted independently
    //      against the SLICER's output (the genuine tie verification is L1's unit
    //      tests — see report). ────────────────────────────────────────────────
    {
        std::set<int> sliceBoundaries;
        for (const Slice& s : slices) {
            sliceBoundaries.insert(s.start);
            sliceBoundaries.insert(s.end);
        }
        for (const NoteEvent* e : eligible) {
            if (e->onset > e->release) {
                violations.push_back({ "tie-span",
                    "eligible note onset > release (inverted span)", e->onset, e->release });
                break;
            }
            // A zero-width eligible note contributes a single deduped tick that
            // opens no slice (a fact) — its endpoint need not be a slice boundary
            // when it is the lone boundary; only check when the domain is sliced.
            if (slices.empty()) {
                continue;
            }
            if (!sliceBoundaries.count(e->onset) || !sliceBoundaries.count(e->release)) {
                violations.push_back({ "tie-span",
                    "eligible note endpoint absent from slicer boundaries",
                    e->onset, e->release });
                break;
            }
        }
    }

    // ── §3 STATS (computed independently; not gating). ───────────────────────
    int measures = 0;
    for (const Measure* m = score->firstMeasure(); m; m = m->nextMeasure()) {
        ++measures;
    }

    // Non-empty slices = those with >=1 eligible note overlapping (the proxy's
    // notion of a slice; it excluded all-rest spans). Recomputed independently.
    long long nonEmpty = 0;
    long long emptySlices = 0;
    long long releaseOpenedNonEmpty = 0;
    // Release-only boundaries: interior ticks that are an eligible release and
    // NOT an eligible onset.
    long long releaseOnlyBoundaries = 0;
    const int domainStart = bexp.empty() ? 0 : *bexp.begin();
    const int domainEnd   = bexp.empty() ? 0 : *bexp.rbegin();
    for (int t : bexp) {
        if (t > domainStart && t < domainEnd
            && eligibleReleases.count(t) && !eligibleOnsets.count(t)) {
            ++releaseOnlyBoundaries;
        }
    }
    for (const Slice& sl : slices) {
        bool hasEligible = false;
        for (const NoteEvent* e : eligible) {
            if (e->onset < sl.end && e->release > sl.start) {
                hasEligible = true;
                break;
            }
        }
        if (hasEligible) {
            ++nonEmpty;
            const bool releaseOpened = (sl.start > domainStart)
                && eligibleReleases.count(sl.start) && !eligibleOnsets.count(sl.start);
            if (releaseOpened) {
                ++releaseOpenedNonEmpty;
            }
        } else {
            ++emptySlices;
        }
    }

    if (!violations.empty()) {
        ok = false;
    }

    // ── Emit the per-stem JSON object. ───────────────────────────────────────
    std::ostringstream os;
    os << "{\n";
    os << "  \"stem\": \"" << jsonEscape(stem) << "\",\n";
    os << "  \"ok\": " << (ok ? "true" : "false") << ",\n";
    os << "  \"measures\": " << measures << ",\n";
    os << "  \"eligibleNotes\": " << eligible.size() << ",\n";
    os << "  \"boundaries\": " << bexp.size() << ",\n";
    os << "  \"domainStart\": " << domainStart << ",\n";
    os << "  \"domainEnd\": " << domainEnd << ",\n";
    os << "  \"slicesTotal\": " << slices.size() << ",\n";
    os << "  \"slicesNonEmpty\": " << nonEmpty << ",\n";
    os << "  \"slicesEmpty\": " << emptySlices << ",\n";
    os << "  \"releaseOnlyBoundaries\": " << releaseOnlyBoundaries << ",\n";
    os << "  \"releaseOpenedNonEmptySlices\": " << releaseOpenedNonEmpty << ",\n";
    os << "  \"deterministic\": " << (deterministic ? "true" : "false") << ",\n";
    os << "  \"sliceMs\": " << fmtDouble(sliceMs, 6) << ",\n";
    os << "  \"violations\": [";
    for (std::size_t i = 0; i < violations.size(); ++i) {
        const SliceViolation& v = violations[i];
        os << (i ? ",\n    " : "\n    ");
        os << "{ \"invariant\": \"" << jsonEscape(v.invariant) << "\""
           << ", \"detail\": \"" << jsonEscape(v.detail) << "\""
           << ", \"tickA\": " << v.tickA
           << ", \"tickB\": " << v.tickB << " }";
    }
    os << (violations.empty() ? "]\n" : "\n  ]\n");
    os << "}\n";
    return os.str();
}

// ══════════════════════════════════════════════════════════════════════════
// Layer 3 — the KEY/MODE SEQUENCE DECODER diagnostic (--decode-keymode)
//
// DIAGNOSTIC ONLY (mirrors --validate-slices). This path does NOT invoke or
// alter the analysis pipeline: main() returns immediately after this runs, so
// analyzeScore / analyzeRegions are never reached. It builds the Layer-1 note
// model, runs the REAL Layer-2 slicer, runs the isolated Layer-3 key/mode
// sequence DECODER (keymodesequence — emission through the indexed NoteModel),
// and emits the decoder's chosen key/mode per slice in the SAME region shape the
// held-out harness reads from *.ours.json (so cmp.load_analysis +
// align_dcml_regions grade it unchanged). Off by default ⇒ production output
// unchanged. The decoder is NOT wired into the live analyzer (this increment is
// isolated; wiring is the next, separately-ratified increment).
// ══════════════════════════════════════════════════════════════════════════
static std::string runKeyModeDecode(const Score* score, const std::string& stem,
                                    const analysis::KeyModeAnalyzerPreferences& keyPrefs,
                                    int keySigFifths,
                                    std::optional<analysis::KeySigMode> declaredMode,
                                    const mu::composing::analysis::keymodeseq::KeyModeSequencePreferences& seqPrefs)
{
    namespace kms = mu::composing::analysis::keymodeseq;

    const NoteModel model = NoteModel::build(score);
    const std::vector<Slice> slices = mu::composing::analysis::slicing::changePointSlices(model);
    const std::vector<kms::SliceKeyMode> decoded =
        kms::KeyModeSequenceDecoder::decode(slices, model, keySigFifths, declaredMode, keyPrefs, seqPrefs);

    long long uncertainCount = 0;
    for (const kms::SliceKeyMode& sk : decoded) {
        if (sk.uncertain) {
            ++uncertainCount;
        }
    }

    std::ostringstream os;
    os << "{\n";
    os << "  \"stem\": \"" << jsonEscape(stem) << "\",\n";
    os << "  \"keySigFifths\": " << keySigFifths << ",\n";
    os << "  \"slicesTotal\": " << slices.size() << ",\n";
    os << "  \"uncertainSlices\": " << uncertainCount << ",\n";
    os << "  \"regions\": [";
    for (size_t i = 0; i < decoded.size(); ++i) {
        const kms::SliceKeyMode& sk = decoded[i];
        const int s = slices[sk.sliceIndex].start;
        const int e = slices[sk.sliceIndex].end;
        const MeasureTickInfo mi = locateMeasureByTick(score, Fraction::fromTicks(s));
        const int measureNumber = mi.measure ? mi.number : 0;
        const double beat = mi.measure
            ? 1.0 + static_cast<double>(s - mi.measure->tick().ticks()) / Constants::DIVISION
            : 1.0;
        const double duration = static_cast<double>(e - s) / Constants::DIVISION;
        const std::string key = keyName(sk.chosen.keySignatureFifths, sk.chosen.mode);

        os << (i ? ",\n    " : "\n    ");
        os << "{ \"measureNumber\": " << measureNumber
           << ", \"beat\": " << fmtDouble(beat, 4)
           << ", \"startTick\": " << s
           << ", \"endTick\": " << e
           << ", \"duration\": " << fmtDouble(duration, 4)
           << ", \"key\": \"" << jsonEscape(key) << "\""
           << ", \"keyConfidence\": " << fmtDouble(sk.confidence, 6)
           // Additive (error-decomposition increment): the CHOSEN candidate's
           // per-slice EMISSION score (sk.chosen.score = emissions[t][winner],
           // the local-fit, NOT the sequence margin keyConfidence above). The
           // carried alternatives already serialize their emission as their
           // "confidence" (alt.score), but the winner's emission was absent —
           // it is exactly what the Q1 branch of the causal decomposition needs
           // (emission[picked] vs emission[correct], to tell a TRANSITION
           // override from an EMISSION failure). Diagnostic-only: the
           // --decode-keymode path returns before analyzeScore, so production
           // analysis output stays byte-identical.
           << ", \"keyEmission\": " << fmtDouble(sk.chosen.score, 6)
           << ", \"uncertain\": " << (sk.uncertain ? "true" : "false");
        if (!sk.alternatives.empty()) {
            const std::string ruKey =
                keyName(sk.alternatives[0].keySignatureFifths, sk.alternatives[0].mode);
            os << ", \"keyModeRunnerUp\": { \"key\": \"" << jsonEscape(ruKey)
               << "\", \"confidence\": " << fmtDouble(sk.alternatives[0].score, 6) << " }";
        } else {
            os << ", \"keyModeRunnerUp\": null";
        }
        // Additive (characterization scaffold): the FULL ranked alternatives the
        // decoder already carries in SliceKeyMode::alternatives (tonic+mode key
        // string + emission score), so the held-out harness can measure
        // alternative-recall ("the true key/mode was carried even when not picked").
        // confidence (keyConfidence) and the uncertain flag are emitted above. This
        // is diagnostic-only — the --decode-keymode path returns before analyzeScore,
        // so production analysis output stays byte-identical.
        os << ", \"alternatives\": [";
        for (size_t a = 0; a < sk.alternatives.size(); ++a) {
            const analysis::KeyModeAnalysisResult& alt = sk.alternatives[a];
            const std::string altKey = keyName(alt.keySignatureFifths, alt.mode);
            os << (a ? ", " : "") << "{ \"key\": \"" << jsonEscape(altKey)
               << "\", \"confidence\": " << fmtDouble(alt.score, 6) << " }";
        }
        os << "]";
        os << " }";
    }
    os << (decoded.empty() ? "]\n" : "\n  ]\n");
    os << "}\n";
    return os.str();
}

// ══════════════════════════════════════════════════════════════════════════
// Layer 3 REACH-BACK A/B — the flag-ON vs flag-OFF range-query measurement
// (--reachback-ab). HELD: for Cowork/user ratification of L3 reach-back ACTIVATION.
//
// DIAGNOSTIC ONLY: builds a set of P3-style interior RANGE selections (single-measure,
// skipping the opening measure so reach-back has earlier context to reach) and runs the
// SHARED region analyzer over each range twice — reachBack OFF (production) and reachBack
// ON (the gated capability) — reporting, per range, whether the emitted analysis DIFFERS
// and the wall-time of each. It never reaches analyzeScore's corpus path, so production /
// the corpus gate are byte-identical. Activation of reach-back on the live range-query path
// is a SEPARATE ratification (this only measures it). See cowork_layer3_reachback_design.md.
// ══════════════════════════════════════════════════════════════════════════
static std::string runReachBackAB(Score* score, const std::string& stem,
                                  const analysis::ChordAnalyzerPreferences& chordPrefs,
                                  const analysis::KeyModeAnalyzerPreferences& keyPrefs,
                                  const std::set<size_t>& excludeStaves)
{
    namespace cra = mu::composing::analysis::region;
    using mu::composing::analysis::HarmonicRegion;

    auto baseOpts = [&]() {
        cra::AnalyzeRegionsOptions o;
        o.granularity = analysis::HarmonicRegionGranularity::Smoothed;
        o.onsetBoundaryThreshold = 0.25;
        o.excludeLookAheadOnDenseStart = true;
        o.pass1MinDistinctPcsForCandidate = 1;
        return o;
    };

    // P3-style range set: interior single-measure selections (skip measure 1 — its opening IS
    // the score start, so reach-back has nowhere to go there). Bounded for a quick diagnostic.
    std::vector<std::pair<int, int>> ranges;
    int mIdx = 0;
    for (const Measure* m = score->firstMeasure(); m && ranges.size() < 24;
         m = m->nextMeasure(), ++mIdx) {
        if (mIdx == 0) { continue; }
        const int a = m->tick().ticks();
        const int b = a + m->ticks().ticks();
        if (b > a) { ranges.emplace_back(a, b); }
    }

    auto sameAnalysis = [](const std::vector<HarmonicRegion>& x,
                           const std::vector<HarmonicRegion>& y) {
        if (x.size() != y.size()) { return false; }
        for (size_t i = 0; i < x.size(); ++i) {
            if (x[i].startTick != y[i].startTick || x[i].endTick != y[i].endTick) { return false; }
            if (x[i].keyModeResult.tonicPc != y[i].keyModeResult.tonicPc) { return false; }
            if (x[i].keyModeResult.isMajor() != y[i].keyModeResult.isMajor()) { return false; }
            if (x[i].chordResult.identity.rootPc != y[i].chordResult.identity.rootPc) { return false; }
            if (x[i].chordResult.identity.quality != y[i].chordResult.identity.quality) { return false; }
        }
        return true;
    };

    std::ostringstream os;
    os << "{\n  \"stem\": \"" << jsonEscape(stem) << "\",\n  \"ranges\": [";
    int changed = 0, leadKeyChanged = 0;
    double offMsTotal = 0.0, onMsTotal = 0.0;
    for (size_t r = 0; r < ranges.size(); ++r) {
        const Fraction a = Fraction::fromTicks(ranges[r].first);
        const Fraction b = Fraction::fromTicks(ranges[r].second);
        cra::AnalyzeRegionsOptions off = baseOpts();
        cra::AnalyzeRegionsOptions on = baseOpts();
        on.reachBack.enabled = true;
        on.reachBack.maxReachSteps = 8;             // hard bound
        on.reachBack.incrementTicks = 0;            // one measure (L3's natural unit)
        on.reachBack.minOpeningConfidence = 0.0;    // the primary "uncertain" trigger only

        const auto t0 = std::chrono::steady_clock::now();
        const auto offR = cra::analyzeRegions(score, a, b, excludeStaves, chordPrefs, keyPrefs, off);
        const auto t1 = std::chrono::steady_clock::now();
        const auto onR = cra::analyzeRegions(score, a, b, excludeStaves, chordPrefs, keyPrefs, on);
        const auto t2 = std::chrono::steady_clock::now();

        const double offMs = std::chrono::duration<double, std::milli>(t1 - t0).count();
        const double onMs = std::chrono::duration<double, std::milli>(t2 - t1).count();
        offMsTotal += offMs;
        onMsTotal += onMs;
        const bool diff = !sameAnalysis(offR, onR);
        if (diff) { ++changed; }
        if (!offR.empty() && !onR.empty()
            && offR.front().keyModeResult.tonicPc != onR.front().keyModeResult.tonicPc) {
            ++leadKeyChanged;
        }
        if (r) { os << ","; }
        os << "\n    {\"start\": " << ranges[r].first << ", \"end\": " << ranges[r].second
           << ", \"changed\": " << (diff ? "true" : "false")
           << ", \"offMs\": " << offMs << ", \"onMs\": " << onMs << "}";
    }
    os << (ranges.empty() ? "]" : "\n  ]") << ",\n";
    os << "  \"rangeCount\": " << ranges.size() << ",\n";
    os << "  \"changedCount\": " << changed << ",\n";
    os << "  \"leadKeyChangedCount\": " << leadKeyChanged << ",\n";
    os << "  \"offMsTotal\": " << offMsTotal << ",\n";
    os << "  \"onMsTotal\": " << onMsTotal << "\n}\n";
    return os.str();
}

// ══════════════════════════════════════════════════════════════════════════
// Layer 4 (Increment A) — the per-slice CHORD-SYMBOL DECODER diagnostic
// (--decode-chords)
//
// DIAGNOSTIC ONLY (mirrors --decode-keymode / --validate-slices). This path does
// NOT invoke or alter the analysis pipeline: main() returns immediately after it
// runs, so analyzeScore / analyzeRegions are never reached. It builds the Layer-1
// note model, runs the REAL Layer-2 slicer, runs the isolated Layer-4 per-slice
// chord decoder (chordslicedecoder — windowed weightedPcView → analyzeChord → the
// surfaced candidate cube), and emits the decoder's chosen chord per slice in a
// region shape compatible with the chord-root graders (compare_analyses /
// oracle_root_metric read rootPitchClass / quality / bassIsRoot etc.), PLUS the
// focal-slice sounding pitch classes and the (empty) membership split the new
// NCT-membership metric scores. Off by default ⇒ production output unchanged. The
// decoder is NOT wired into the live analyzer; wiring is a later increment.
// ══════════════════════════════════════════════════════════════════════════
static std::string runChordDecode(const Score* score, const std::string& stem,
                                  const analysis::ChordAnalyzerPreferences& chordPrefs,
                                  int keySigFifths, analysis::KeySigMode keyMode,
                                  const mu::composing::analysis::chordslice::ChordSliceDecoderPreferences& decoderPrefs,
                                  const std::set<size_t>& excludeStaves)
{
    namespace cs = mu::composing::analysis::chordslice;
    namespace eb = mu::composing::analysis::engravingbridge;

    const NoteModel model = NoteModel::build(score);
    const std::vector<Slice> slices = mu::composing::analysis::slicing::changePointSlices(model);
    const std::vector<cs::SliceChord> decoded = cs::ChordSliceDecoder::decode(
        slices, model, keySigFifths, keyMode, chordPrefs, decoderPrefs, excludeStaves);

    long long namedCount = 0, uncertainCount = 0;
    for (const cs::SliceChord& sc : decoded) {
        if (sc.hasChord) { ++namedCount; }
        if (sc.uncertain) { ++uncertainCount; }
    }

    const std::string keyStr = keyName(keySigFifths, keyMode);

    // Build a display chord symbol from a candidate (reuses the production formatter
    // on a minimal identity — no function/extension state; this increment names the
    // basic chord only).
    auto symbolFor = [&](const cs::ChordSliceCandidate& c) -> std::string {
        analysis::ChordAnalysisResult res;
        res.identity.rootPc     = c.rootPc;
        res.identity.rootTpc    = c.rootTpc;
        res.identity.bassPc     = c.bassPc;
        res.identity.bassTpc    = c.bassTpc;
        res.identity.quality    = c.quality;
        res.identity.tiePriority = c.tiePriority;
        return analysis::ChordSymbolFormatter::formatSymbol(res, keySigFifths);
    };

    std::ostringstream os;
    os << "{\n";
    os << "  \"stem\": \"" << jsonEscape(stem) << "\",\n";
    os << "  \"keySigFifths\": " << keySigFifths << ",\n";
    os << "  \"key\": \"" << jsonEscape(keyStr) << "\",\n";
    os << "  \"slicesTotal\": " << slices.size() << ",\n";
    os << "  \"namedSlices\": " << namedCount << ",\n";
    os << "  \"uncertainSlices\": " << uncertainCount << ",\n";
    os << "  \"regions\": [";
    for (size_t i = 0; i < decoded.size(); ++i) {
        const cs::SliceChord& sc = decoded[i];
        const int s = slices[sc.sliceIndex].start;
        const int e = slices[sc.sliceIndex].end;
        const MeasureTickInfo mi = locateMeasureByTick(score, Fraction::fromTicks(s));
        const int measureNumber = mi.measure ? mi.number : 0;
        const double beat = mi.measure
            ? 1.0 + static_cast<double>(s - mi.measure->tick().ticks()) / Constants::DIVISION
            : 1.0;
        const double duration = static_cast<double>(e - s) / Constants::DIVISION;

        // Focal-slice sounding pitch classes (NOT the windowed context): the notes
        // the per-note membership metric scores. Same indexed view the decoder
        // window uses, over JUST [s, e).
        const std::vector<analysis::ChordAnalysisTone> focal =
            eb::weightedPcView(model, s, e, excludeStaves);
        std::set<int> soundingPcs;
        int pcMask = 0;
        for (const analysis::ChordAnalysisTone& t : focal) {
            const int pc = ((t.pitch % 12) + 12) % 12;
            soundingPcs.insert(pc);
            pcMask |= (1 << pc);
        }

        const int rootPc = sc.hasChord ? sc.chosen.rootPc : -1;
        const int bassPc = sc.hasChord ? sc.chosen.bassPc : -1;
        const bool bassIsRoot = sc.hasChord && sc.chosen.bassIsRoot();
        const char* quality = sc.hasChord ? qualityToString(sc.chosen.quality) : "Unknown";
        const std::string chordSym = sc.hasChord ? symbolFor(sc.chosen) : std::string();

        os << (i ? ",\n    " : "\n    ");
        os << "{ \"measureNumber\": " << measureNumber
           << ", \"beat\": " << fmtDouble(beat, 4)
           << ", \"startTick\": " << s
           << ", \"endTick\": " << e
           << ", \"duration\": " << fmtDouble(duration, 4)
           << ", \"rootPitchClass\": " << rootPc
           << ", \"bassPitchClass\": " << bassPc
           << ", \"bassIsRoot\": " << (bassIsRoot ? "true" : "false")
           << ", \"quality\": \"" << quality << "\""
           << ", \"chordSymbol\": \"" << jsonEscape(chordSym) << "\""
           << ", \"romanNumeral\": \"\""
           << ", \"key\": \"" << jsonEscape(keyStr) << "\""
           << ", \"keyConfidence\": 0"
           << ", \"chordScore\": " << fmtDouble(sc.hasChord ? sc.chosen.score : 0.0, 5)
           << ", \"chordScoreMargin\": " << fmtDouble(sc.confidence, 5)
           << ", \"confidence\": " << fmtDouble(sc.confidence, 5)
           << ", \"uncertain\": " << (sc.uncertain ? "true" : "false")
           << ", \"hasChord\": " << (sc.hasChord ? "true" : "false")
           << ", \"pitchClassSet\": " << pcMask
           << ", \"noteCount\": " << soundingPcs.size();

        os << ", \"soundingPitchClasses\": [";
        { bool f = true; for (int pc : soundingPcs) { os << (f ? "" : ", ") << pc; f = false; } }
        os << "]";

        // Membership split (Increment B): the per-note chord-tone / non-chord-tone
        // decision over the focal slice's sounding pitch classes (the §10 metric).
        os << ", \"noteClassifications\": { \"chordTones\": [";
        { bool f = true; for (int pc : sc.chordTonePcs) { os << (f ? "" : ", ") << pc; f = false; } }
        os << "], \"nonChordTones\": [";
        { bool f = true; for (int pc : sc.nonChordTonePcs) { os << (f ? "" : ", ") << pc; f = false; } }
        os << "] }";

        os << ", \"alternatives\": [";
        for (size_t a = 0; a < sc.alternatives.size(); ++a) {
            const cs::ChordSliceCandidate& alt = sc.alternatives[a];
            os << (a ? ", " : "")
               << "{ \"rootPitchClass\": " << alt.rootPc
               << ", \"bassPitchClass\": " << alt.bassPc
               << ", \"quality\": \"" << qualityToString(alt.quality) << "\""
               << ", \"bassIsRoot\": " << (alt.bassIsRoot() ? "true" : "false")
               << ", \"chordSymbol\": \"" << jsonEscape(symbolFor(alt)) << "\""
               << ", \"score\": " << fmtDouble(alt.score, 5) << " }";
        }
        os << "]";
        os << " }";
    }
    os << (decoded.empty() ? "]\n" : "\n  ]\n");
    os << "}\n";
    return os.str();
}

// ══════════════════════════════════════════════════════════════════════════
// E0 — the dormant FULL-SPINE measurement harness (--dump-fullspine)
//
// DIAGNOSTIC ONLY (mirrors --decode-chords / --dump-l5). This path chains the
// complete dormant analysis spine END-TO-END and writes a per-stem JSON side
// file; main() returns immediately after it, so analyzeScore / analyzeRegions
// are NEVER reached (default OFF ⇒ production output byte-identical). The new
// code has NO production consumer.
//
//   L1  NoteModel::build              — the lossless note model
//   L2  changePointSlices             — the constant-sonority slice grid
//   L3  inferLocalKey (LIVE, reused)  — the production key path's global/home
//                                       key (NO second decoder instantiated);
//                                       the L4 decoder takes ONE key (its own
//                                       design: per-slice key feed-forward is a
//                                       later wiring refinement). L5 owns local
//                                       key (§5.3/§5.4).
//   L4  ChordSliceDecoder::decode     — the dormant per-slice chord decoder →
//                                       the SliceChord stream (chosen + carried
//                                       alternatives + SliceConfidence +
//                                       OpenQuestionLabel + decision).
//   L5  the six dormant units, in build-plan order:
//        Step 1  functionprogression / functionromannumeral (base RN)
//        Step 2  functioncadence      (detectFunctionalCadences)
//        Step 4  functionmodulation   (detectAndDecideModulations + §5.4 §8 recompute)
//        Step 3  functionresolver     (resolveCarriedReadings — §5.5 + the §5.5
//                                       case-4 fine-grain override, LIVE on THIS
//                                       substrate — the E0 headline)
//        Step 5  functionrelationallabel (classifyRelationalLabel)
//        Step 6  functionoutput       (assembleFunctionOutput — the §7 contract)
//
// REUSE, NOT RE-IMPLEMENTATION: every producer/primitive is the existing one —
// NoteModel::overlapping + scoreharvest::regionMetricWeightForOnsetTick (the same
// the decoder builds its FocalNotes from), eb::weightedPcView / phraseBoundaryTicks,
// the L5 units verbatim, ChordSymbolFormatter for symbols. The grading is the
// existing compare_rn / compare_analyses / dcml_parser (the .ours.json emitted here
// carries the STANDARD regions[] shape so those graders read it unchanged) — no new
// comparator; the E0-specific fields are extra keys the loaders ignore.
//
// ★ CARRY-CONTRACT NOTE (E0 finding, Cowork-ratified 2026-07-02; CARRY-FIX applied
//   2026-07-02): the L4→L5 carry (SliceChord.chosen = ChordSliceCandidate) now CARRIES
//   ChordIdentity.extensions + naturalFifthPresent (chordslicedecoder.cpp — the chosen is
//   a full deriveChordExtensions extraction, extensionsKnown = true guaranteed; carried
//   alternatives match analyzeChord's result cells or honest-carry extensions = 0 with
//   extensionsKnown = false). The base-RN / relational units read the seventh / figured-
//   bass / V7-x / Ger+6 from `extensions` (chordsymbolformatter.cpp formatRomanNumeral).
//   We build the ChordIdentity from EXACTLY what SliceChord carries — real extensions on
//   the committed chord, honest 0 where unknown — so base RNs now emit the seventh (V7,
//   65/43/42) and the seventh-dependent labels (V7/x, Ger+6) can fire (report §4-A; E0′).
// ══════════════════════════════════════════════════════════════════════════
static const char* fsCadenceTypeName(analysis::FunctionalCadenceType t)
{
    switch (t) {
    case analysis::FunctionalCadenceType::None:               return "None";
    case analysis::FunctionalCadenceType::PerfectAuthentic:   return "PerfectAuthentic";
    case analysis::FunctionalCadenceType::ImperfectAuthentic: return "ImperfectAuthentic";
    case analysis::FunctionalCadenceType::Half:               return "Half";
    case analysis::FunctionalCadenceType::PhrygianHalf:       return "PhrygianHalf";
    case analysis::FunctionalCadenceType::Deceptive:          return "Deceptive";
    case analysis::FunctionalCadenceType::Plagal:             return "Plagal";
    case analysis::FunctionalCadenceType::Evaded:             return "Evaded";
    }
    return "None";
}

static const char* fsResolutionBasisName(analysis::ResolutionBasis b)
{
    switch (b) {
    case analysis::ResolutionBasis::None:             return "None";
    case analysis::ResolutionBasis::Progression:      return "Progression";
    case analysis::ResolutionBasis::CadenceVote:      return "CadenceVote";
    case analysis::ResolutionBasis::NeighbourHarmony: return "NeighbourHarmony";
    case analysis::ResolutionBasis::BassDegreePrior:  return "BassDegreePrior";
    case analysis::ResolutionBasis::FineGrainOverride:return "FineGrainOverride";
    }
    return "None";
}

static const char* fsSliceDecisionName(analysis::chordslice::SliceDecision d)
{
    switch (d) {
    case analysis::chordslice::SliceDecision::Commit:  return "Commit";
    case analysis::chordslice::SliceDecision::Inherit: return "Inherit";
    case analysis::chordslice::SliceDecision::Abstain: return "Abstain";
    }
    return "Commit";
}

static const char* fsOpenQuestionName(analysis::chordslice::OpenQuestion q)
{
    switch (q) {
    case analysis::chordslice::OpenQuestion::None:           return "None";
    case analysis::chordslice::OpenQuestion::Root:           return "Root";
    case analysis::chordslice::OpenQuestion::Quality:        return "Quality";
    case analysis::chordslice::OpenQuestion::NoteMembership: return "NoteMembership";
    }
    return "None";
}

static const char* fsAmbiguityKindName(analysis::chordslice::AmbiguityKind k)
{
    using AK = analysis::chordslice::AmbiguityKind;
    switch (k) {
    case AK::None:                     return "None";
    case AK::InsufficientEvidence:     return "InsufficientEvidence";
    case AK::TransitionVsContinuation: return "TransitionVsContinuation";
    case AK::SymmetricRotation:        return "SymmetricRotation";
    case AK::ShareTone:                return "ShareTone";
    case AK::RelativePair:             return "RelativePair";
    case AK::CloseReading:             return "CloseReading";
    }
    return "None";
}

// Ionian-convention key-signature fifths for a (tonicPc, minor) local key — the
// inverse of "tonic = (fifths·7) mod 12", with the minor key stamped at its
// RELATIVE-MAJOR signature (Aeolian convention). Used ONLY to keep the base-RN
// key triple (fifths, mode, tonic) internally consistent when the §5.4 recompute
// commits a modulation to a local tonic (diatonicDegreeForRootPc derives the tonic
// from the fifths, so a stale fifths would mis-degree a modulated slice).
static int fsFifthsForTonic(int tonicPc, bool minor)
{
    const int t = minor ? (((tonicPc + 3) % 12) + 12) % 12 : (((tonicPc % 12) + 12) % 12);
    int f = (7 * t) % 12;
    if (f > 6) { f -= 12; }
    return f;
}

// ── L6 --dump-l6 renderer: the dormant grouping structure as an additive JSON
//    "l6" object appended to the fullspine dump (byte-identical when emitL6=false). ─
static std::string fsGroupingJson(const mu::composing::analysis::grouping::GroupingLayerOutput& l6)
{
    namespace g6 = mu::composing::analysis::grouping;
    std::ostringstream os;
    os << "  \"l6\": {\n";
    os << "    \"punctuationSpans\": [";
    for (size_t i = 0; i < l6.punctuationSpans.size(); ++i) {
        const g6::PunctuationSpan& p = l6.punctuationSpans[i];
        os << (i ? ", " : "")
           << "{ \"startTick\": " << p.startTick
           << ", \"endTick\": " << p.endTick
           << ", \"structuralEndTick\": " << p.structuralEndTick
           << ", \"codettaEndTick\": " << p.codettaEndTick
           << ", \"closingCadenceIndex\": " << p.closingCadenceIndex
           << ", \"carriesOpenMark\": " << (p.carriesOpenMark ? "true" : "false")
           << ", \"clippedAtStart\": " << (p.clippedAtStart ? "true" : "false")
           << ", \"clippedAtEnd\": " << (p.clippedAtEnd ? "true" : "false")
           << ", \"extensionCue\": " << (p.extensionCue ? "true" : "false") << " }";
    }
    os << "],\n";
    os << "    \"keyAreas\": [";
    for (size_t i = 0; i < l6.keyAreas.size(); ++i) {
        const g6::KeyAreaSpan& k = l6.keyAreas[i];
        os << (i ? ", " : "")
           << "{ \"startTick\": " << k.startTick
           << ", \"endTick\": " << k.endTick
           << ", \"localTonicPc\": " << k.localTonicPc
           << ", \"localMinorMode\": " << (k.localMinorMode ? "true" : "false")
           << ", \"confidence\": " << fmtDouble(k.confidence, 4)
           << ", \"carriesOpenMark\": " << (k.carriesOpenMark ? "true" : "false") << " }";
    }
    os << "],\n";
    os << "    \"cadenceAlignments\": [";
    for (size_t i = 0; i < l6.cadenceAlignments.size(); ++i) {
        const g6::CadenceAlignment& a = l6.cadenceAlignments[i];
        os << (i ? ", " : "")
           << "{ \"cadenceIndex\": " << a.cadenceIndex
           << ", \"kind\": \"" << (a.kind == g6::CadenceAlignmentKind::ClosesSpan ? "ClosesSpan" : "Internal") << "\""
           << ", \"punctuationSpanIndex\": " << a.punctuationSpanIndex << " }";
    }
    os << "],\n";
    os << "    \"schemaSpanCount\": " << l6.schemaSpans.size() << "\n";
    os << "  }";
    return os.str();
}

static std::string runFullSpine(Score* score, const std::string& stem,
                                const std::string& presetName,
                                const analysis::KeyModeAnalyzerPreferences& keyPrefs,
                                const analysis::ChordAnalyzerPreferences& chordPrefs,
                                const analysis::chordslice::ChordSliceDecoderPreferences& decoderPrefs,
                                const std::set<size_t>& excludeStaves,
                                bool sectionLevel,
                                bool emitL6 = false)
{
    namespace cs = mu::composing::analysis::chordslice;
    namespace eb = mu::composing::analysis::engravingbridge;
    namespace sh = mu::composing::analysis::scoreharvest;
    using Clock = std::chrono::steady_clock;
    auto ms = [](Clock::time_point a, Clock::time_point b) {
        return std::chrono::duration<double, std::milli>(b - a).count();
    };

    // ── L1 + L2 + L3(live) + L4 — timed as the "engage-path proxy" (G3) ──
    // Done FIRST so the measured decode is byte-identical to standalone
    // --decode-chords (no prior analyzeScore can perturb the score model).
    const auto tDec0 = Clock::now();
    const NoteModel model = NoteModel::build(score);
    const std::vector<Slice> slices = analysis::slicing::changePointSlices(model);

    const size_t refStaff = referenceStaffForAnalysis(score, excludeStaves);
    // L3 LIVE: reuse the production key path (inferLocalKey → resolveKeyAndModeRanked),
    // NOT a second decoder, NOT the raw notated signature. The decoder + L5 home key.
    const KeyModeAnalysisResult homeKey =
        inferLocalKey(score, refStaff, excludeStaves, Fraction(0, 1), nullptr, keyPrefs)[0];
    const int   homeFifths = homeKey.keySignatureFifths;
    const auto  homeMode   = homeKey.mode;
    const int   homeTonicPc = homeKey.tonicPc;
    const bool  homeMinor  = !homeKey.isMajor();
    const double homeConf  = homeKey.normalizedConfidence;

    const std::set<int> phraseTicks = eb::phraseBoundaryTicks(score);

    // L4: the dormant per-slice decoder over the LIVE home key.
    const std::vector<cs::SliceChord> decoded = cs::ChordSliceDecoder::decode(
        slices, model, homeFifths, homeMode, chordPrefs, decoderPrefs, excludeStaves);
    const double decodeMs = ms(tDec0, Clock::now());

    const int lastTick = slices.empty() ? 0 : slices.back().end;

    // ── Per-slice context gathered ONCE from L1 (per-voice notes, tpcs, mask,
    //    metric weight, phrase flag) — the inputs L5 units need that the L4 carry
    //    does not hold (by design; the cadence detector's per-voice-note channel). ─
    struct SliceCtx {
        std::vector<analysis::CadenceVoiceNote> notes;  // per-voice sounding notes
        std::vector<int> noteTpcs;                       // notated spellings (Ger6↔V7)
        uint16_t pcMask = 0;                             // sounding pitch classes
        double metricWeight = 1.0;
        bool endsPhrase = false;
        bool isFinalBar = false;
    };
    std::vector<SliceCtx> ctx(slices.size());
    for (size_t i = 0; i < slices.size(); ++i) {
        const int s = slices[i].start, e = slices[i].end;
        SliceCtx& c = ctx[i];
        c.metricWeight = sh::regionMetricWeightForOnsetTick(score, s);
        auto pb = phraseTicks.lower_bound(s);
        c.endsPhrase = (pb != phraseTicks.end() && *pb < e);
        c.isFinalBar = (e >= lastTick && lastTick > 0);
        for (const NoteEvent* ne : model.overlapping(s, e)) {
            if (!ne->plays || !ne->visible || !ne->staffEligible) { continue; }
            if (excludeStaves.count(static_cast<size_t>(ne->staff))) { continue; }
            analysis::CadenceVoiceNote vn; vn.voice = ne->voice; vn.pitch = ne->pitch;
            c.notes.push_back(vn);
            if (ne->tpc >= 0) { c.noteTpcs.push_back(ne->tpc); }
            c.pcMask |= static_cast<uint16_t>(1u << (((ne->pitch % 12) + 12) % 12));
        }
    }

    auto candQuality = [](const cs::ChordSliceCandidate& c) { return c.quality; };
    auto isCommitted = [&](size_t i) {
        return decoded[i].hasChord
            && decoded[i].decision != cs::SliceDecision::Abstain;
    };

    // ── L5 Step 2 — the cadence stream (key-agnostic; reads the seventh from the
    //    per-voice notes, so cadence/modulation are FULLY faithful to the pitch). ─
    // The detector pairs ADJACENT events (events[i]→events[i+1]) — it expects "the
    // committed-chord stream of a region" (§5.0). On the per-slice substrate the
    // committed chords are separated by thin/abstain slices, so we feed the COMMITTED
    // subsequence (Commit/Inherit), matching the legacy region substrate's chord
    // stream; the returned cadences carry TICKS, mapped back to slices below.
    std::vector<analysis::CadenceEvent> events;
    events.reserve(slices.size());
    for (size_t i = 0; i < slices.size(); ++i) {
        if (!isCommitted(i)) { continue; }
        analysis::CadenceEvent ev;
        ev.rootPc  = decoded[i].chosen.rootPc;
        ev.quality = decoded[i].chosen.quality;
        ev.bassPc  = decoded[i].chosen.bassPc;
        ev.notes = ctx[i].notes;
        ev.metricWeight = ctx[i].metricWeight;
        ev.startTick = slices[i].start;
        ev.endTick = slices[i].end;
        ev.endsPhrase = ctx[i].endsPhrase;
        ev.isFinalBar = ctx[i].isFinalBar;
        events.push_back(ev);
    }
    const std::vector<analysis::FunctionalCadence> cadences =
        analysis::detectFunctionalCadences(events);

    // ── L5 Step 4 — tonicization vs modulation + the §5.4 §8 recompute ──
    // Build the key-agnostic region stream (one CadenceRegionInput per slice) and
    // run the established substrate; then FIRE the §5.4 confidence-weighted forward
    // recompute (the §8 mechanism) per confirmed modulation, recording the committed
    // local key per slice via the injected reread callback.
    // Committed subsequence (same rationale as the cadence stream: the local-key
    // detector grows contiguous runs of committed chords; thin/abstain slices would
    // break the runs). Spans carry ticks; the recompute maps them back to slices.
    std::vector<analysis::CadenceRegionInput> cadRegions;
    cadRegions.reserve(slices.size());
    for (size_t i = 0; i < slices.size(); ++i) {
        if (!isCommitted(i)) { continue; }
        analysis::CadenceRegionInput cr;
        cr.startTick = slices[i].start;
        cr.endTick = slices[i].end;
        cr.rootPc = decoded[i].chosen.rootPc;
        cr.quality = candQuality(decoded[i].chosen);
        cr.pitchClassMask = ctx[i].pcMask;
        cr.endsPhrase = ctx[i].endsPhrase;
        cadRegions.push_back(cr);
    }
    const std::vector<analysis::ModulationDecision> mods =
        analysis::detectAndDecideModulations(cadRegions, cadences, homeFifths);

    // Per-slice local key (default = home); the §5.4 recompute commits the confirmed
    // modulations onto the affected slice range.
    std::vector<int>  localTonic(slices.size(), homeTonicPc);
    std::vector<bool> localMinor(slices.size(), homeMinor);
    analysis::OnePassClosure closure;
    int recomputeFired = 0, recomputeSlices = 0, keyDecisionId = 1;
    for (const analysis::ModulationDecision& md : mods) {
        if (!md.isModulation) { continue; }
        int first = -1, last = -1;
        for (size_t i = 0; i < slices.size(); ++i) {
            if (slices[i].start < md.endTick && slices[i].end > md.startTick) {
                if (first < 0) { first = static_cast<int>(i); }
                last = static_cast<int>(i);
            }
        }
        if (first < 0) { continue; }
        auto reread = [&](int sliceId, int newTonic, bool newMinor) {
            if (sliceId >= 0 && sliceId < static_cast<int>(slices.size())) {
                localTonic[static_cast<size_t>(sliceId)] = newTonic;
                localMinor[static_cast<size_t>(sliceId)] = newMinor;
            }
        };
        const analysis::ModulationRecomputeResult rr = analysis::modulationRecompute(
            md, homeConf, first, last, reread, closure, keyDecisionId++);
        if (rr.fired) { ++recomputeFired; recomputeSlices += (rr.slicesReread > 0 ? rr.slicesReread : 0); }
    }

    // ── L5 Step 3 — the RESOLVER + the §5.5 case-4 fine-grain OVERRIDE (headline) ─
    std::vector<analysis::FunctionSlice> funcSlices(slices.size());
    for (size_t i = 0; i < slices.size(); ++i) {
        analysis::FunctionSlice& fs = funcSlices[i];
        fs.chord.rootPc = decoded[i].hasChord ? decoded[i].chosen.rootPc : -1;
        fs.chord.quality = decoded[i].hasChord ? decoded[i].chosen.quality : ChordQuality::Unknown;
        fs.committed = isCommitted(i);
        fs.metricWeight = ctx[i].metricWeight;
        fs.startTick = slices[i].start;
        fs.endTick = slices[i].end;
        fs.decision = decoded[i].decision;
        fs.openQuestion = decoded[i].openQuestion;
        fs.alternatives = decoded[i].alternatives;
        fs.confidence = decoded[i].confidenceModel;
        // The committed slice's FULL identity — the resolver emits this VERBATIM on the
        // pass-through path (carry-fix 2), so the committed bass/inversion + the carried
        // extensions survive to finalReadingOf/the formatter instead of a bare re-derivation.
        fs.chosen = decoded[i].chosen;
    }
    analysis::ResolverKey rkey;
    rkey.keyFifths = homeFifths; rkey.keyMode = homeMode; rkey.tonicPc = homeTonicPc;
    const analysis::ResolverResult res =
        analysis::resolveCarriedReadings(funcSlices, cadences, rkey);

    // The FINAL per-unit chord identity (post-resolver): the resolver's reading is
    // the committed chord for an unchanged commit, the corrected reading on an
    // override, or the selected reading on a resolved abstain.
    auto finalReadingOf = [&](size_t i) -> cs::ChordSliceCandidate {
        if (i < res.readings.size()) {
            const analysis::ResolvedReading& rr = res.readings[i];
            if (rr.reading.rootPc >= 0) { return rr.reading; }
        }
        return decoded[i].chosen;
    };
    auto unitHasChord = [&](size_t i) -> bool {
        // A committed/inherited slice, or an abstain the resolver resolved.
        if (isCommitted(i)) { return true; }
        if (i < res.readings.size() && res.readings[i].resolved && !res.readings[i].openMark) {
            return res.readings[i].reading.rootPc >= 0;
        }
        return false;
    };
    auto unitOpenMark = [&](size_t i) -> bool {
        return i < res.readings.size() && res.readings[i].openMark;
    };
    // The internally-consistent local-key triple for slice i (preserving the EXACT
    // home key — incl. a non-Aeolian home mode — where unmodulated).
    auto localKeyFifths = [&](size_t i) -> int {
        return (localTonic[i] == homeTonicPc && localMinor[i] == homeMinor)
             ? homeFifths : fsFifthsForTonic(localTonic[i], localMinor[i]);
    };
    auto localKeyMode = [&](size_t i) -> analysis::KeySigMode {
        return (localTonic[i] == homeTonicPc && localMinor[i] == homeMinor)
             ? homeMode
             : (localMinor[i] ? analysis::KeySigMode::Aeolian : analysis::KeySigMode::Ionian);
    };

    // The next committed/resolved root (the applied-resolution target — §5.6).
    auto nextRootOf = [&](size_t i) -> int {
        for (size_t j = i + 1; j < slices.size(); ++j) {
            if (unitHasChord(j)) { return finalReadingOf(j).rootPc; }
        }
        return -1;
    };

    // ── L5 Step 5 (relational) + Step 6 (§7 output assembly) ──
    std::vector<analysis::FunctionUnitAssembly> units(slices.size());
    std::vector<analysis::RelationalLabel> relLabels(slices.size());
    for (size_t i = 0; i < slices.size(); ++i) {
        analysis::FunctionUnitAssembly& u = units[i];
        u.startTick = slices[i].start;
        u.endTick = slices[i].end;
        u.committed = unitHasChord(i);
        u.openMark = unitOpenMark(i);
        u.resolverConfidence = (i < res.readings.size()) ? res.readings[i].functionConfidence : 0.0;

        if (unitHasChord(i)) {
            const cs::ChordSliceCandidate fr = finalReadingOf(i);
            // The FAITHFUL identity — root/quality/bass PLUS the L4→L5 carried extension
            // identity (the carry-fix): real extensions on the committed chord (fr is a
            // committed/inherited chosen → extensionsKnown), honest 0 where a resolver-
            // selected alternative was honest-carried. We carry EXACTLY what SliceChord holds.
            analysis::ChordIdentity id;
            id.rootPc = fr.rootPc; id.rootTpc = fr.rootTpc;
            id.bassPc = fr.bassPc; id.bassTpc = fr.bassTpc;
            id.quality = fr.quality; id.tiePriority = fr.tiePriority;
            id.extensions = fr.extensions; id.naturalFifthPresent = fr.naturalFifthPresent;
            u.committedIdentity = id;
            u.chord.rootPc = fr.rootPc; u.chord.quality = fr.quality;

            analysis::RelationalLabelInput in;
            in.identity = id;
            in.keyFifths = localKeyFifths(i);   // consistent with keyTonicPc/keyMode below
            in.keyMode = localKeyMode(i);
            in.keyTonicPc = localTonic[i];
            in.nextRootPc = nextRootOf(i);
            in.pitchClassMask = ctx[i].pcMask;
            in.noteTpcs = ctx[i].noteTpcs;
            relLabels[i] = analysis::classifyRelationalLabel(in);
        }
        u.relational = relLabels[i];
    }
    const analysis::FunctionLayerOutput out5 = analysis::assembleFunctionOutput(
        units, cadences, mods, homeTonicPc, homeMinor);

    // ── Wall-time B: the LEGACY production spine (the G3 envelope baseline) ──
    // Timed LAST so it cannot perturb the decode measured above.
    const auto tLeg0 = Clock::now();
    const std::vector<AnalyzedRegion> legacyRegions =
        analyzeScore(score, excludeStaves, keyPrefs, chordPrefs, sectionLevel);
    const double legacyMs = ms(tLeg0, Clock::now());
    (void)legacyRegions;   // graded from the flag-OFF corpus; timed here only

    // ── Emit the .ours.json (STANDARD regions[] shape + E0 fields) ──
    // Carry-fix telemetry (report §4-A / E0′): the chosen committed chord is ALWAYS a full
    // extraction (extensionsKnown), so committedExtUnknown should be 0; alternatives split
    // known (matched an analyzeChord result cell) vs honest-carry (not obtainable → 0/false).
    long long committedCount = 0, abstainCount = 0, openMarkCount = 0, overrodeCount = 0;
    long long committedExtKnown = 0, committedExtUnknown = 0, altExtKnown = 0, altExtUnknown = 0;
    for (size_t i = 0; i < decoded.size(); ++i) {
        if (isCommitted(i)) { ++committedCount; }
        else { ++abstainCount; }
        if (unitOpenMark(i)) { ++openMarkCount; }
        if (i < res.readings.size() && res.readings[i].overrodeCommit) { ++overrodeCount; }
        if (unitHasChord(i)) {
            if (finalReadingOf(i).extensionsKnown) { ++committedExtKnown; } else { ++committedExtUnknown; }
        }
        for (const cs::ChordSliceCandidate& alt : decoded[i].alternatives) {
            if (alt.extensionsKnown) { ++altExtKnown; } else { ++altExtUnknown; }
        }
    }

    auto symbolFor = [&](const cs::ChordSliceCandidate& c) -> std::string {
        ChordAnalysisResult r;
        r.identity.rootPc = c.rootPc; r.identity.rootTpc = c.rootTpc;
        r.identity.bassPc = c.bassPc; r.identity.bassTpc = c.bassTpc;
        r.identity.quality = c.quality; r.identity.tiePriority = c.tiePriority;
        return analysis::ChordSymbolFormatter::formatSymbol(r, homeFifths);
    };

    std::ostringstream os;
    os << "{\n";
    os << "  \"source\": \"" << jsonEscape(stem) << "\",\n";
    os << "  \"preset\": \"" << jsonEscape(presetName) << "\",\n";
    os << "  \"analysisPath\": \"fullspine\",\n";
    os << "  \"detectedKey\": \"" << jsonEscape(keyName(homeFifths, homeMode)) << "\",\n";
    os << "  \"keyConfidence\": " << fmtDouble(homeConf) << ",\n";
    os << "  \"homeTonicPc\": " << homeTonicPc << ",\n";
    os << "  \"homeMinor\": " << (homeMinor ? "true" : "false") << ",\n";
    os << "  \"slicesTotal\": " << slices.size() << ",\n";
    os << "  \"committedUnits\": " << committedCount << ",\n";
    os << "  \"abstainUnits\": " << abstainCount << ",\n";
    os << "  \"openMarkUnits\": " << openMarkCount << ",\n";
    os << "  \"overrodeCommits\": " << overrodeCount << ",\n";
    os << "  \"committedExtKnown\": " << committedExtKnown << ",\n";
    os << "  \"committedExtUnknown\": " << committedExtUnknown << ",\n";
    os << "  \"altExtKnown\": " << altExtKnown << ",\n";
    os << "  \"altExtUnknown\": " << altExtUnknown << ",\n";
    os << "  \"modulationsConfirmed\": " << recomputeFired << ",\n";
    os << "  \"modulationSlicesReread\": " << recomputeSlices << ",\n";
    os << "  \"wallTimeLegacyMs\": " << fmtDouble(legacyMs, 3) << ",\n";
    os << "  \"wallTimeDecodeMs\": " << fmtDouble(decodeMs, 3) << ",\n";

    // L6 punctuation-span oracle (metric 1): the L1.5 boundary-detector picked set
    // (eb::phraseBoundaryTicks, computed above as `phraseTicks`) exposed verbatim
    // as ticks — OUR boundary ticks for the punctuation-span-boundary P/R metric.
    // Diagnostic-only, additive to the --dump-fullspine output; the standard
    // .ours.json (writeJson) path is byte-identical, so the BIR gate is unaffected.
    os << "  \"phraseBoundaryTicks\": [";
    { bool f = true; for (int t : phraseTicks) { os << (f ? "" : ", ") << t; f = false; } }
    os << "],\n";

    os << "  \"cadences\": [";
    for (size_t i = 0; i < cadences.size(); ++i) {
        const analysis::FunctionalCadence& c = cadences[i];
        os << (i ? ", " : "")
           << "{ \"type\": \"" << fsCadenceTypeName(c.type) << "\""
           << ", \"approachTick\": " << c.approachTick
           << ", \"arrivalTick\": " << c.arrivalTick
           << ", \"tonicPc\": " << c.tonicPc
           << ", \"minorMode\": " << (c.minorMode ? "true" : "false")
           << ", \"tonicVote\": " << fmtDouble(c.tonicVote, 4) << " }";
    }
    os << "],\n";

    os << "  \"modulations\": [";
    for (size_t i = 0; i < mods.size(); ++i) {
        const analysis::ModulationDecision& m = mods[i];
        os << (i ? ", " : "")
           << "{ \"startTick\": " << m.startTick << ", \"endTick\": " << m.endTick
           << ", \"tonicPc\": " << m.tonicPc << ", \"minorMode\": " << (m.minorMode ? "true" : "false")
           << ", \"isHomeKey\": " << (m.isHomeKey ? "true" : "false")
           << ", \"cadenceConfirmed\": " << (m.cadenceConfirmed ? "true" : "false")
           << ", \"cadentialWeight\": " << fmtDouble(m.cadentialWeight, 4)   // D-FS §5.4 contradiction quantity
           << ", \"isModulation\": " << (m.isModulation ? "true" : "false") << " }";
    }
    os << "],\n";

    os << "  \"regions\": [";
    bool firstReg = true;
    for (size_t i = 0; i < decoded.size(); ++i) {
        const int s = slices[i].start, e = slices[i].end;
        const bool hasChord = unitHasChord(i);
        const cs::ChordSliceCandidate fr = finalReadingOf(i);
        const int rootPc = hasChord ? fr.rootPc : -1;
        const int bassPc = hasChord ? fr.bassPc : -1;
        const bool bassIsRoot = hasChord && fr.bassIsRoot();
        const std::string rn = (i < out5.units.size()) ? out5.units[i].romanNumeral : std::string();
        const std::string chordSym = hasChord ? symbolFor(fr) : std::string();

        const MeasureTickInfo mi = locateMeasureByTick(score, Fraction::fromTicks(s));
        const int measureNumber = mi.measure ? mi.number : 0;
        const double beat = mi.measure
            ? 1.0 + static_cast<double>(s - mi.measure->tick().ticks()) / Constants::DIVISION : 1.0;
        const double duration = static_cast<double>(e - s) / Constants::DIVISION;

        const analysis::ResolvedReading rr =
            (i < res.readings.size()) ? res.readings[i] : analysis::ResolvedReading{};
        const analysis::FunctionConfidence fc =
            (i < out5.units.size()) ? out5.units[i].confidence : analysis::FunctionConfidence{};

        os << (firstReg ? "\n    " : ",\n    ");
        firstReg = false;
        os << "{ \"measureNumber\": " << measureNumber
           << ", \"beat\": " << fmtDouble(beat, 4)
           << ", \"startTick\": " << s << ", \"endTick\": " << e
           << ", \"duration\": " << fmtDouble(duration, 4)
           << ", \"rootPitchClass\": " << rootPc
           << ", \"bassPitchClass\": " << bassPc
           << ", \"bassIsRoot\": " << (bassIsRoot ? "true" : "false")
           << ", \"quality\": \"" << (hasChord ? qualityToString(fr.quality) : "Unknown") << "\""
           << ", \"chordSymbol\": \"" << jsonEscape(chordSym) << "\""
           << ", \"romanNumeral\": \"" << jsonEscape(rn) << "\""
           << ", \"key\": \"" << jsonEscape(keyName(localKeyFifths(i), localKeyMode(i))) << "\""
           << ", \"keyConfidence\": " << fmtDouble(homeConf)
           << ", \"localTonicPc\": " << localTonic[i]
           << ", \"localMinor\": " << (localMinor[i] ? "true" : "false")
           // ── E0 fields (extra keys the standard loaders ignore) ──
           << ", \"l4Decision\": \"" << fsSliceDecisionName(decoded[i].decision) << "\""
           << ", \"l4RootPc\": " << (decoded[i].hasChord ? decoded[i].chosen.rootPc : -1)
           << ", \"l4Uncertain\": " << (decoded[i].uncertain ? "true" : "false")
           << ", \"l4Composite\": " << fmtDouble(decoded[i].confidenceModel.composite, 4)
           << ", \"l4Margin\": " << fmtDouble(decoded[i].confidenceModel.margin, 4)
           << ", \"l4Sufficiency\": " << fmtDouble(decoded[i].confidenceModel.sufficiency, 4)
           << ", \"l4Cleanliness\": " << fmtDouble(decoded[i].confidenceModel.membershipCleanliness, 4)
           << ", \"openQuestion\": \"" << fsOpenQuestionName(decoded[i].openQuestion.question) << "\""
           << ", \"ambiguityKind\": \"" << fsAmbiguityKindName(decoded[i].openQuestion.ambiguity) << "\""
           << ", \"l5Resolved\": " << (rr.resolved ? "true" : "false")
           << ", \"l5OverrodeCommit\": " << (rr.overrodeCommit ? "true" : "false")
           << ", \"l5OpenMark\": " << (rr.openMark ? "true" : "false")
           << ", \"l5Basis\": \"" << fsResolutionBasisName(rr.basis) << "\""
           << ", \"l5Role\": \"" << ((i < out5.units.size()) ? relationalRoleName(out5.units[i].relationalRole) : "None") << "\""
           << ", \"l5CadenceVoteWeight\": " << fmtDouble(fc.cadenceVoteWeight, 4)
           << ", \"l5LicensedFit\": " << fmtDouble(fc.licensedProgressionFit, 4)
           << ", \"l5NextBestMargin\": " << fmtDouble(fc.nextBestMargin, 4)
           << ", \"l5Combined\": " << fmtDouble(fc.combined, 4)
           << ", \"l5CombinedBoundary\": " << fmtDouble(fc.combinedBoundary, 6)   // D-L5a boundary form ∈ [0,1)
           // D-FS frame-scale evidence (Stage-5): the §5.5 contradiction (bestPlaus-committedPlaus),
           // carried on the resolver's functionConfidence when the fine-grain override fired.
           << ", \"l5OverrideContradiction\": " << fmtDouble((rr.overrodeCommit ? rr.functionConfidence : 0.0), 4)
           << ", \"l4ChosenExtensions\": " << (hasChord ? static_cast<long long>(fr.extensions) : 0)
           << ", \"l4ChosenExtKnown\": " << (hasChord && fr.extensionsKnown ? "true" : "false")
           << ", \"openMark\": " << (unitOpenMark(i) ? "true" : "false");

        os << ", \"alternatives\": [";
        for (size_t a = 0; a < decoded[i].alternatives.size(); ++a) {
            const cs::ChordSliceCandidate& alt = decoded[i].alternatives[a];
            os << (a ? ", " : "")
               << "{ \"rootPitchClass\": " << alt.rootPc
               << ", \"bassPitchClass\": " << alt.bassPc
               << ", \"quality\": \"" << qualityToString(alt.quality) << "\""
               << ", \"bassIsRoot\": " << (alt.bassIsRoot() ? "true" : "false")
               << ", \"extensions\": " << static_cast<long long>(alt.extensions)
               << ", \"extKnown\": " << (alt.extensionsKnown ? "true" : "false")
               << ", \"score\": " << fmtDouble(alt.score, 5) << " }";
        }
        os << "] }";
    }
    os << (decoded.empty() ? "]" : "\n  ]");

    // ── L6 GROUPING (dormant, --dump-l6) — additive block: the flat grouping
    //    structure assembled from THIS spine's L1.5 boundaries + L5 cadences +
    //    per-slice local-key track. Whole-score analysis → true score edges (no
    //    selection clip). Byte-identical fullspine output when emitL6 == false. ──
    if (emitL6) {
        namespace g6 = mu::composing::analysis::grouping;
        std::vector<g6::GroupingUnit> gunits;
        gunits.reserve(slices.size());
        for (size_t i = 0; i < slices.size(); ++i) {
            g6::GroupingUnit gu;
            gu.startTick = slices[i].start;
            gu.endTick = slices[i].end;
            gu.localTonicPc = localTonic[i];
            gu.localMinorMode = localMinor[i];
            gu.keyConfidence = homeConf;          // the declared L3/L5 home-key confidence [0,1]
            gu.openMark = unitOpenMark(i);
            gunits.push_back(gu);
        }
        std::vector<g6::BoundaryInput> gbounds;
        gbounds.reserve(phraseTicks.size());
        for (int t : phraseTicks) { g6::BoundaryInput b; b.tick = t; gbounds.push_back(b); }
        g6::AnalyzedSpan gspan;
        gspan.startTick = slices.empty() ? 0 : slices.front().start;
        gspan.endTick = lastTick;
        gspan.startIsSelectionEdge = false;
        gspan.endIsSelectionEdge = false;
        const g6::GroupingLayerOutput l6 =
            g6::assembleGrouping(gunits, gbounds, cadences, gspan);
        os << ",\n" << fsGroupingJson(l6);
    }
    os << "\n}\n";
    return os.str();
}

} // namespace

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
    std::set<int> dumpKeyTicks;  // Stage-4 emission instrument (read-only key-candidate dump)
    bool sectionLevel = false;   // Stage 2.2-i prototype (default OFF)
    bool ignoreDeclaredMode = false;  // Stage 4b-i mode-absent floor (default OFF = no-op)
    bool dumpCadenceAnchor = false;   // Stage 4c-i cadence anchor (default OFF = byte-identical)
    bool dumpTonicization = false;    // Stage 6-tonic-i tonicization labels (default OFF = byte-identical)
    bool dumpL5 = false;              // Phase 5c Step M: dormant L5 would-be labels (default OFF = byte-identical)
    bool dumpModulation = false;      // Stage 4d-i local-modulation spans (default OFF = byte-identical)
    bool dumpJointKey = false;        // J-key-i scoped-joint key decision (default OFF = byte-identical)
    bool jointKeyWiring = false;      // J-key-iii PRODUCTION wiring (default OFF = byte-identical baseline)
    bool validateSlices = false;      // Layer-2 corpus slice validation (default OFF = no analysis touched)
    bool decodeKeyMode = false;       // Layer-3 key/mode sequence decoder (default OFF = no analysis touched)
    bool decodeChords = false;        // Layer-4 per-slice chord decoder (default OFF = no analysis touched)
    bool reachBackAB = false;         // Layer-3 reach-back flag-ON/OFF range-query A/B (default OFF; HELD)
    bool dumpFullSpine = false;       // E0 full-spine measurement L1→L5 (default OFF = no analysis touched)
    bool dumpL6 = false;              // L6 grouping structure appended to the fullspine dump (default OFF)
    // Decode-only sweep overrides for the decoder-private ChordSliceDecoderPreferences.
    // Read ONLY on the --decode-chords diagnostic path (which returns before
    // analyzeScore), so production analysis stays byte-identical. Default = the
    // committed decoder defaults.
    mu::composing::analysis::chordslice::ChordSliceDecoderPreferences chordDecoderPrefs;
    // Decode-only sweep overrides for the decoder-private KeyModeSequencePreferences
    // (the BOUNDED L3 SWEEP). These are read ONLY on the --decode-keymode diagnostic
    // path (which returns before analyzeScore), so production analysis stays
    // byte-identical and the shared KeyModeAnalyzer(Preferences) is untouched. Default
    // = kDefaultKeyModeSequencePreferences (the decoder's committed defaults).
    mu::composing::analysis::keymodeseq::KeyModeSequencePreferences seqPrefs;
    // Decode-only EMISSION-WEIGHT overrides for the §3 A∩stable reweight MEASUREMENT
    // (the bounded sweep's emission-reweight spec validation). Applied to a COPY of
    // keyPrefs INSIDE the --decode-keymode block only, so the production keyPrefs used
    // by analyzeScore is untouched and production stays byte-identical. nullopt = use
    // the preset value. These let the sweep test whether sharpening the per-slice
    // scale-membership contrast recovers A∩stable WITHOUT the windowBeats modulation
    // penalty — the crux of the wiring-increment spec.
    std::optional<double> ovInNeither, ovInKeySigOnly, ovInCandidateOnly, ovInBoth, ovLeadingTone;

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
        } else if (a == "--section-level") {
            sectionLevel = true;
        } else if (a == "--validate-slices") {
            validateSlices = true;
        } else if (a == "--decode-keymode") {
            decodeKeyMode = true;
        } else if (a == "--decode-chords") {
            decodeChords = true;
        } else if (a == "--reachback-ab") {
            reachBackAB = true;
        } else if (a == "--dump-fullspine") {
            dumpFullSpine = true;
        } else if (a == "--dump-l6") {
            // L6 grouping: run the full spine and APPEND the dormant grouping structure.
            dumpFullSpine = true;
            dumpL6 = true;
        } else if (a == "--chord-no-membership") {
            // Decode-only: disable the Increment-B membership decision + feedback +
            // two-pass (reproduces the Increment-A behaviour, modulo the adaptive window).
            chordDecoderPrefs.enableMembership = false;
        } else if (a == "--chord-no-two-pass") {
            // Decode-only: membership from the slice's own notes + key prior alone.
            chordDecoderPrefs.twoPass = false;
        } else if (a == "--chord-context-slices" || a == "--chord-topk"
                   || a == "--chord-uncertain-margin" || a == "--chord-min-pcs"
                   || a == "--chord-max-context-slices" || a == "--chord-min-harmony-pcs"
                   || a == "--chord-memb-salience" || a == "--chord-memb-penalty"
                   || a == "--chord-memb-ref-dur" || a == "--chord-stepwise-tol") {
            // Decode-only ChordSliceDecoderPreferences sweep overrides (see decl above).
            if (i + 1 >= args.size()) {
                std::cerr << "ERROR: " << a.toStdString() << " requires a numeric argument\n";
                return 1;
            }
            const QString val = args.at(++i);
            bool ok = false;
            if (a == "--chord-context-slices") {
                chordDecoderPrefs.contextSlices = val.toInt(&ok);
            } else if (a == "--chord-topk") {
                chordDecoderPrefs.topK = val.toInt(&ok);
            } else if (a == "--chord-uncertain-margin") {
                chordDecoderPrefs.uncertaintyMargin = val.toDouble(&ok);
            } else if (a == "--chord-min-pcs") {
                chordDecoderPrefs.minDistinctPcs = val.toInt(&ok);
            } else if (a == "--chord-max-context-slices") {
                chordDecoderPrefs.maxContextSlices = val.toInt(&ok);
            } else if (a == "--chord-min-harmony-pcs") {
                chordDecoderPrefs.minHarmonyPcs = val.toInt(&ok);
            } else if (a == "--chord-memb-salience") {
                chordDecoderPrefs.membershipSalienceThreshold = val.toDouble(&ok);
            } else if (a == "--chord-memb-penalty") {
                chordDecoderPrefs.membershipPenaltyWeight = val.toDouble(&ok);
            } else if (a == "--chord-memb-ref-dur") {
                chordDecoderPrefs.membershipReferenceDurationQn = val.toDouble(&ok);
            } else if (a == "--chord-stepwise-tol") {
                chordDecoderPrefs.stepwiseGapToleranceTicks = val.toInt(&ok);
            }
            if (!ok) {
                std::cerr << "ERROR: invalid numeric argument for " << a.toStdString()
                          << ": '" << val.toStdString() << "'\n";
                return 1;
            }
        } else if (a == "--seq-change-base" || a == "--seq-relative-extra"
                   || a == "--seq-per-fifth" || a == "--seq-window-beats"
                   || a == "--seq-uncertain" || a == "--seq-topk"
                   || a == "--seq-max-alts") {
            // Decode-only KeyModeSequencePreferences sweep overrides (see decl above).
            if (i + 1 >= args.size()) {
                std::cerr << "ERROR: " << a.toStdString() << " requires a numeric argument\n";
                return 1;
            }
            const QString val = args.at(++i);
            bool ok = false;
            if (a == "--seq-change-base") {
                seqPrefs.changeBaseCost = val.toDouble(&ok);
            } else if (a == "--seq-relative-extra") {
                seqPrefs.relativePairExtraCost = val.toDouble(&ok);
            } else if (a == "--seq-per-fifth") {
                seqPrefs.changePerFifthStep = val.toDouble(&ok);
            } else if (a == "--seq-window-beats") {
                seqPrefs.windowBeats = val.toDouble(&ok);
            } else if (a == "--seq-uncertain") {
                seqPrefs.uncertainThreshold = val.toDouble(&ok);
            } else if (a == "--seq-topk") {
                seqPrefs.topK = val.toInt(&ok);
            } else if (a == "--seq-max-alts") {
                seqPrefs.maxAlternatives = val.toInt(&ok);
            }
            if (!ok) {
                std::cerr << "ERROR: invalid numeric argument for " << a.toStdString()
                          << ": '" << val.toStdString() << "'\n";
                return 1;
            }
        } else if (a == "--key-in-neither" || a == "--key-in-keysig-only"
                   || a == "--key-in-candidate-only" || a == "--key-in-both"
                   || a == "--key-leading-tone") {
            // Decode-only emission-weight overrides (§3 reweight measurement; see decl).
            if (i + 1 >= args.size()) {
                std::cerr << "ERROR: " << a.toStdString() << " requires a numeric argument\n";
                return 1;
            }
            const QString val = args.at(++i);
            bool ok = false;
            const double dv = val.toDouble(&ok);
            if (!ok) {
                std::cerr << "ERROR: invalid numeric argument for " << a.toStdString()
                          << ": '" << val.toStdString() << "'\n";
                return 1;
            }
            if (a == "--key-in-neither") { ovInNeither = dv; }
            else if (a == "--key-in-keysig-only") { ovInKeySigOnly = dv; }
            else if (a == "--key-in-candidate-only") { ovInCandidateOnly = dv; }
            else if (a == "--key-in-both") { ovInBoth = dv; }
            else if (a == "--key-leading-tone") { ovLeadingTone = dv; }
        } else if (a == "--ignore-declared-mode") {
            ignoreDeclaredMode = true;
        } else if (a == "--dump-cadence-anchor") {
            dumpCadenceAnchor = true;
        } else if (a == "--dump-modulation") {
            dumpModulation = true;
        } else if (a == "--dump-joint-key") {
            dumpJointKey = true;
        } else if (a == "--joint-key-wiring") {
            jointKeyWiring = true;
        } else if (a == "--dump-tonicization") {
            dumpTonicization = true;
        } else if (a == "--dump-l5") {
            dumpL5 = true;
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
        } else if (a == "--dump-key-candidates") {
            if (i + 1 >= args.size()) {
                std::cerr << "ERROR: --dump-key-candidates requires a comma-separated list of ticks\n";
                return 1;
            }
            const std::string tickList = args.at(++i).toUtf8().toStdString();
            std::istringstream iss(tickList);
            std::string token;
            while (std::getline(iss, token, ',')) {
                try {
                    dumpKeyTicks.insert(std::stoi(token));
                } catch (...) {
                    std::cerr << "ERROR: invalid tick in --dump-key-candidates: '"
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
                  << "'.  Valid names: Standard, Jazz, Modal, Baroque, Contemporary, Default\n";
        return 1;
    }
    // Stage 4b-i: mode-absent measurement floor. Forces declaredMode = nullopt
    // in the resolver (drops the declared-mode hint, partial-sig correction, and
    // declared opening influence). Default OFF = byte-identical to mode-present.
    keyPrefs.ignoreDeclaredMode = ignoreDeclaredMode;

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

    } else if (presetName == "Default") {
        // Live product out-of-box (Stage 2.4 V4): the app never mutates a single
        // ChordAnalyzerPreferences field (every live chord-scoring site uses
        // kDefaultChordAnalyzerPreferences — see ARCHITECTURE.md D-PASS0 Half A), so
        // leave chordPrefs at struct defaults. In particular preferMinorOverMajorAdd6
        // stays FALSE here — unlike Standard/Modal/Contemporary, which set it true —
        // so this measures the configuration users actually run, not even batch
        // "Standard".

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

    // ── Layer-2 slice validation (diagnostic; returns BEFORE any analysis) ──
    // This path never reaches analyzeScore/analyzeRegions, so the analysis
    // pipeline is not invoked and its output cannot change. Emits one per-stem
    // JSON object (to outputPath if given, else stdout); exit 0 if every §2
    // invariant held, 2 if any failed (the §5 stop signal for the driver).
    if (validateSlices) {
        const std::string stem =
            QFileInfo(inputPath.toQString()).completeBaseName().toUtf8().toStdString();
        bool ok = false;
        const std::string report = runSliceValidation(score, stem, ok);
        if (!outputPath.empty()) {
            std::ofstream ofs(outputPath.toQString().toStdString(), std::ios::binary);
            ofs << report;
        } else {
            std::cout << report;
        }
        delete score;
        return ok ? 0 : 2;
    }

    // ── Build exclude-staves set ───────────────────────────────────────────
    std::set<size_t> excludeStaves;
    for (size_t si = 0; si < score->nstaves(); ++si) {
        if (!staffIsEligible(score, si)) {
            excludeStaves.insert(si);
        }
    }

    // ── Layer-3 key/mode decode (diagnostic; returns BEFORE any analysis) ───
    // Like --validate-slices, this never reaches analyzeScore/analyzeRegions, so
    // the analysis pipeline is not invoked and its output cannot change. The
    // notated key signature (a weak hint to the decoder) is read at tick 0.
    if (decodeKeyMode) {
        const std::string stem =
            QFileInfo(inputPath.toQString()).completeBaseName().toUtf8().toStdString();
        const size_t refStaff = referenceStaffForAnalysis(score, excludeStaves);
        int keySigFifths = 0;
        std::optional<analysis::KeySigMode> declaredMode;   // the notated <mode>, a weak hint
        if (refStaff < score->nstaves() && score->staff(refStaff)) {
            const auto kse = score->staff(refStaff)->keySigEvent(Fraction(0, 1));
            keySigFifths = static_cast<int>(kse.concertKey());
            const mu::engraving::KeyMode km = kse.mode();
            if (km == mu::engraving::KeyMode::MAJOR || km == mu::engraving::KeyMode::IONIAN) {
                declaredMode = analysis::KeySigMode::Ionian;
            } else if (km == mu::engraving::KeyMode::MINOR || km == mu::engraving::KeyMode::AEOLIAN) {
                declaredMode = analysis::KeySigMode::Aeolian;
            }
        }
        // Decode-only emission-weight overrides (§3 reweight measurement). A LOCAL COPY
        // — the production keyPrefs above is untouched, so analyzeScore stays byte-identical.
        analysis::KeyModeAnalyzerPreferences decodeKeyPrefs = keyPrefs;
        if (ovInNeither) { decodeKeyPrefs.scaleScoreInNeither = *ovInNeither; }
        if (ovInKeySigOnly) { decodeKeyPrefs.scaleScoreInKeySigOnly = *ovInKeySigOnly; }
        if (ovInCandidateOnly) { decodeKeyPrefs.scaleScoreInCandidateOnly = *ovInCandidateOnly; }
        if (ovInBoth) { decodeKeyPrefs.scaleScoreInBoth = *ovInBoth; }
        if (ovLeadingTone) { decodeKeyPrefs.leadingToneWeight = *ovLeadingTone; }
        const std::string report = runKeyModeDecode(score, stem, decodeKeyPrefs, keySigFifths, declaredMode, seqPrefs);
        if (!outputPath.empty()) {
            std::ofstream ofs(outputPath.toQString().toStdString(), std::ios::binary);
            ofs << report;
        } else {
            std::cout << report;
        }
        delete score;
        return 0;
    }

    // ── Layer-4 chord decode (diagnostic; returns BEFORE any analysis) ──────
    // Like --decode-keymode, this never reaches analyzeScore/analyzeRegions, so
    // the analysis pipeline is not invoked and its output cannot change. The
    // notated key signature (the diatonic prior to the chord scorer) is read at
    // tick 0; per-slice Layer-3 key feed-forward is a later (wiring) refinement.
    if (decodeChords) {
        const std::string stem =
            QFileInfo(inputPath.toQString()).completeBaseName().toUtf8().toStdString();
        const size_t refStaff = referenceStaffForAnalysis(score, excludeStaves);
        int keySigFifths = 0;
        analysis::KeySigMode keyMode = analysis::KeySigMode::Ionian;   // the diatonic prior
        if (refStaff < score->nstaves() && score->staff(refStaff)) {
            const auto kse = score->staff(refStaff)->keySigEvent(Fraction(0, 1));
            keySigFifths = static_cast<int>(kse.concertKey());
            const mu::engraving::KeyMode km = kse.mode();
            if (km == mu::engraving::KeyMode::MINOR || km == mu::engraving::KeyMode::AEOLIAN) {
                keyMode = analysis::KeySigMode::Aeolian;
            }
        }
        const std::string report = runChordDecode(score, stem, chordPrefs, keySigFifths, keyMode,
                                                   chordDecoderPrefs, excludeStaves);
        if (!outputPath.empty()) {
            std::ofstream ofs(outputPath.toQString().toStdString(), std::ios::binary);
            ofs << report;
        } else {
            std::cout << report;
        }
        delete score;
        return 0;
    }

    // ── Layer-3 reach-back A/B (diagnostic; returns BEFORE the corpus path) ──
    // Runs the SHARED region analyzer over interior P3-style ranges with reach-back OFF
    // vs ON and reports per-range deltas + wall-time. HELD for activation ratification;
    // never reaches analyzeScore, so production / the corpus gate are byte-identical.
    if (reachBackAB) {
        const std::string stem =
            QFileInfo(inputPath.toQString()).completeBaseName().toUtf8().toStdString();
        const std::string report = runReachBackAB(score, stem, chordPrefs, keyPrefs, excludeStaves);
        if (!outputPath.empty()) {
            std::ofstream ofs(outputPath.toQString().toStdString(), std::ios::binary);
            ofs << report;
        } else {
            std::cout << report;
        }
        delete score;
        return 0;
    }

    // ── E0 — the dormant FULL-SPINE measurement (--dump-fullspine) ──
    // DIAGNOSTIC ONLY: chains L1→L2→L3(live)→L4-decoder→L5 and writes a per-stem
    // JSON side file, then returns — analyzeScore / analyzeRegions are never
    // reached, so production output is byte-identical (default OFF). See
    // runFullSpine(). The live L3 key is the production key path (inferLocalKey),
    // reused inside runFullSpine, NOT a second decoder.
    if (dumpFullSpine) {
        const std::string stem =
            QFileInfo(inputPath.toQString()).completeBaseName().toUtf8().toStdString();
        const std::string report = runFullSpine(score, stem, presetName, keyPrefs, chordPrefs,
                                                 chordDecoderPrefs, excludeStaves, sectionLevel, dumpL6);
        if (!outputPath.empty()) {
            std::ofstream ofs(outputPath.toQString().toStdString(), std::ios::binary);
            ofs << report;
        } else {
            std::cout << report;
        }
        delete score;
        return 0;
    }

    // J-key-iii: enable the production joint re-key wiring for this process (global,
    // default OFF ⇒ byte-identical baseline).  Set BEFORE analyzeScore → analyzeRegions.
    analysis::setJointKeyWiringEnabled(jointKeyWiring);

    // ── Analyze harmonic regions (key inferred locally per region) ────────
    std::vector<AnalyzedRegion> regions;
    if (dumpMode == RegionDumpMode::Batch) {
        regions = analyzeScore(score, excludeStaves, keyPrefs, chordPrefs, sectionLevel);
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

    // ── Stage 4c-iii: phrase boundaries + NOTATED signature (key-agnostic) ─
    // Only needed for the --dump-cadence-anchor diagnostic; read here where the
    // engraving Score is in scope.  The signature is the notated concertKey at
    // tick 0 (NOT a resolved key) — the key-agnostic input the raised-LT salience
    // requires.  When the flag is off these are unused (byte-identical output).
    std::set<int> phraseBoundaryTicks;
    int notatedSignatureFifths = 0;
    // Declared <mode> at tick 0 (J-key-i declared-mode hint): -1 unknown, 0 major,
    // 1 minor.  A notation fact read from the engraving KeySigEvent — NOT a resolved
    // key.  Only used by --dump-joint-key; off ⇒ unused (byte-identical output).
    int declaredModeOrdinal = -1;
    if (dumpCadenceAnchor || dumpModulation || dumpJointKey) {
        phraseBoundaryTicks = analysis::engravingbridge::phraseBoundaryTicks(score);
        if (refStaff < score->nstaves() && score->staff(refStaff)) {
            const auto kse = score->staff(refStaff)->keySigEvent(Fraction(0, 1));
            notatedSignatureFifths = static_cast<int>(kse.concertKey());
            const mu::engraving::KeyMode km = kse.mode();
            if (km == mu::engraving::KeyMode::MAJOR || km == mu::engraving::KeyMode::IONIAN) {
                declaredModeOrdinal = 0;
            } else if (km == mu::engraving::KeyMode::MINOR || km == mu::engraving::KeyMode::AEOLIAN) {
                declaredModeOrdinal = 1;
            }
        }
    }

    // ── Extract source basename ───────────────────────────────────────────
    const std::string sourceName = QFileInfo(inputPath.toQString()).fileName().toUtf8().toStdString();

    // ── Write JSON ────────────────────────────────────────────────────────
    if (outputPath.empty()) {
        if (!dumpKeyTicks.empty()) {
            writeKeyCandidateDump(score, regions, refStaff, excludeStaves, keyPrefs,
                                  dumpKeyTicks, sourceName, std::cout);
        } else if (!diagnoseMeasures.empty()) {
            writeDiagnosticJson(regions, diagnoseMeasures, sourceName, chordPrefs, std::cout);
        } else {
            writeJson(regions, sourceName, presetName, openingKey, regionDumpModeName(dumpMode), std::cout, dumpCadenceAnchor, phraseBoundaryTicks, notatedSignatureFifths, dumpTonicization, dumpModulation, dumpJointKey, declaredModeOrdinal, dumpL5);
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
        if (!dumpKeyTicks.empty()) {
            writeKeyCandidateDump(score, regions, refStaff, excludeStaves, keyPrefs,
                                  dumpKeyTicks, sourceName, out);
        } else if (!diagnoseMeasures.empty()) {
            writeDiagnosticJson(regions, diagnoseMeasures, sourceName, chordPrefs, out);
        } else {
            writeJson(regions, sourceName, presetName, openingKey, regionDumpModeName(dumpMode), out, dumpCadenceAnchor, phraseBoundaryTicks, notatedSignatureFifths, dumpTonicization, dumpModulation, dumpJointKey, declaredModeOrdinal, dumpL5);
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
