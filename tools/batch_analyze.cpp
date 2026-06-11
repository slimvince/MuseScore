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
    // stream remains batch's preset path so the A/B isolates the section-pass
    // delta (NOT the notation-bridge default-chordPrefs divergence).
    if (sectionLevel) {
        const analysis::AnalyzedSection section = analysis::analyzeSection(
            score, startTick, endTick, excludeStaves, regions);

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
                           " [--preset Standard|Jazz|Modal|Baroque|Contemporary]"
                           " [--dump-regions batch|notation|notation-premerge]"
                           " [--section-level]"
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
        << "  --section-level\n"
        << "            (Stage 2.2 prototype) Run the user-facing section pipeline\n"
        << "            (analyzeSection: measure layout, gap-tone insertion, key/mode\n"
        << "            stabilization, sparse-quality refinement) on top of the batch\n"
        << "            region stream. Default OFF. Only affects --dump-regions batch.\n"
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
    bool sectionLevel = false;   // Stage 2.2-i prototype (default OFF)

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

    // ── Extract source basename ───────────────────────────────────────────
    const std::string sourceName = QFileInfo(inputPath.toQString()).fileName().toUtf8().toStdString();

    // ── Write JSON ────────────────────────────────────────────────────────
    if (outputPath.empty()) {
        if (!diagnoseMeasures.empty()) {
            writeDiagnosticJson(regions, diagnoseMeasures, sourceName, chordPrefs, std::cout);
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
            writeDiagnosticJson(regions, diagnoseMeasures, sourceName, chordPrefs, out);
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
