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
//                [--inject-written-root]
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
#include "engraving/dom/harmony.h"
#include "engraving/dom/keysig.h"
#include "engraving/dom/layoutbreak.h"
#include "engraving/dom/mscore.h"
#include "engraving/dom/pedal.h"
#include "engraving/dom/pitchspelling.h"
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
#include "composing/analysis/chord/analysisutils.h"
#include "notation/internal/notationanalysisinternal.h"
#include "notation/internal/notationcomposingbridge.h"

// ── Namespace aliases ──────────────────────────────────────────────────────
using namespace mu::engraving;
namespace analysis = mu::composing::analysis;
using analysis::ChordAnalysisTone;
using analysis::ChordAnalysisResult;
using analysis::ChordQuality;
using analysis::ChordTemporalContext;
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
// Mirrors modePriorPresets() in composingconfiguration.cpp.
// batch_analyze links against composing_analysis (not the composing module),
// so preset values are inlined here.  Keep in sync with composingconfiguration.cpp.
// ══════════════════════════════════════════════════════════════════════════

/// Apply a named mode prior preset to @p prefs.
/// Returns true on success; false if @p name is not a known preset.
/// Valid names: "Standard", "Jazz", "Modal", "Baroque", "Contemporary".
static bool applyPreset(const std::string& name,
                        analysis::KeyModeAnalyzerPreferences& prefs)
{
    struct PresetValues {
        const char* name;
        // Diatonic
        double ionian, dorian, phrygian, lydian, mixolydian, aeolian, locrian;
        // Melodic minor
        double melodicMinor, dorianB2, lydianAugmented, lydianDominant,
               mixolydianB6, aeolianB5, altered;
        // Harmonic minor
        double harmonicMinor, locrianSharp6, ionianSharp5, dorianSharp4,
               phrygianDominant, lydianSharp2, alteredDomBB7;
    };

    // clang-format off
    static constexpr PresetValues PRESETS[] = {
        //                   Ion    Dor    Phr    Lyd    Mix    Aeo    Loc
        //                   MelMin DorB2  LydAug LydDom MixB6  AeoB5  Alt
        //                   HarMin LcrS6  IonS5  DorS4  PhrDom LydS2  AltBB7
        { "Standard",        1.20, -0.50, -1.50, -1.50, -0.50,  1.00, -3.00,
                            -0.50, -1.50, -2.00, -1.00, -1.50, -2.50, -3.50,
                            -0.30, -2.50, -2.00, -2.00, -0.80, -2.50, -3.50 },
        { "Jazz",            0.50,  0.80, -1.00, -0.50,  0.80,  0.50, -1.50,
                             0.50, -0.50, -0.50,  0.80, -0.50, -1.00,  0.50,
                            -0.30, -1.50, -1.50, -0.50,  0.20, -1.50, -1.50 },
        { "Modal",           0.50,  0.50,  0.50,  0.50,  0.50,  0.50, -1.00,
                            -1.00, -1.50, -2.00, -1.50, -1.50, -2.50, -3.50,
                            -1.00, -2.50, -2.00, -2.00, -1.50, -2.50, -3.50 },
        { "Baroque",         1.20, -0.70, -1.50, -2.00, -0.70,  1.00, -3.00,
                            -1.50, -2.00, -2.50, -2.00, -2.00, -3.00, -3.50,
                             0.50, -2.00, -1.50, -2.50,  0.50, -2.00, -3.50 },
        { "Contemporary",    0.80,  0.20, -0.50, -0.20,  0.20,  0.80, -2.00,
                             0.20, -0.80, -1.00,  0.20, -0.50, -1.50, -1.50,
                             0.20, -1.50, -1.00, -1.00,  0.00, -1.50, -2.00 },
    };
    // clang-format on

    for (const auto& p : PRESETS) {
        if (std::string(p.name) != name) continue;
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

    // Follows the initialization sequence from src/framework/testing/environment.cpp
    // (Environment::setup).  GlobalModule must come first; dependency modules
    // receive setApplication() before registerResources().
    // loadInstrumentTemplates() runs last (post-onStartApp), matching the
    // engraving test environment's postInit callback pattern.
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

static bool staffIsEligible(const Score* score, size_t staffIdx, const Fraction&)
{
    return staffIsEligible(score, staffIdx);
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

static constexpr int    LOOKBACK_BEATS   = 16;
static constexpr int    LOOKAHEAD_BEATS  = 8;
static constexpr double LOOKAHEAD_WEIGHT = 0.5;
static constexpr double DECAY_RATE       = 0.7;  // multiplier per measure (4 quarter notes)

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
    if (!measure || !segment) {
        return BeatType::SUBBEAT;
    }

    const int numerator = measure->timesig().numerator();
    const int denominator = measure->timesig().denominator();
    if (numerator <= 0 || denominator <= 0) {
        return BeatType::SUBBEAT;
    }

    return TimeSigFrac(numerator, denominator).rtick2beatType(segment->rtick().ticks());
}

static double timeDecay(double beatsAgo)
{
    return std::pow(DECAY_RATE, beatsAgo / 4.0);
}

static int distinctPitchClasses(const std::vector<analysis::KeyModeAnalyzer::PitchContext>& ctx)
{
    std::set<int> pcs;
    for (const auto& pitchContext : ctx) {
        pcs.insert(analysis::normalizePc(pitchContext.pitch));
    }
    return static_cast<int>(pcs.size());
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
    // §4.1c Jazz mode
    bool fromChordSymbol = false;  // true when root/quality came from a written chord symbol
    int writtenRootPc = -1;        // root PC from the chord symbol (-1 when not jazz path)
    ChordQuality writtenQuality = ChordQuality::Unknown;
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
    case RegionDumpMode::Batch:            return "batch";
    case RegionDumpMode::Notation:         return "notation";
    case RegionDumpMode::NotationPreMerge: return "notation-premerge";
    }
    return "batch";
}

// ── §4.1c Jazz mode helpers ──────────────────────────────────────────────────

static ChordQuality xmlKindToQuality(const muse::String& xmlKind)
{
    if (xmlKind == u"major" || xmlKind.startsWith(u"major-")) return ChordQuality::Major;
    if (xmlKind == u"minor" || xmlKind.startsWith(u"minor-")) return ChordQuality::Minor;
    if (xmlKind == u"dominant" || xmlKind.startsWith(u"dominant-")) return ChordQuality::Major;
    if (xmlKind == u"diminished" || xmlKind.startsWith(u"diminished-")) return ChordQuality::Diminished;
    if (xmlKind == u"augmented" || xmlKind.startsWith(u"augmented-")) return ChordQuality::Augmented;
    if (xmlKind == u"half-diminished") return ChordQuality::HalfDiminished;
    if (xmlKind == u"suspended-second") return ChordQuality::Suspended2;
    if (xmlKind == u"suspended-fourth") return ChordQuality::Suspended4;
    if (xmlKind == u"power") return ChordQuality::Power;
    return ChordQuality::Unknown;
}

static bool isStandardChordSymbol(const EngravingItem* annotation)
{
    if (!annotation || !annotation->isHarmony()) {
        return false;
    }

    const Harmony* harmony = toHarmony(annotation);
    return harmony->harmonyType() == HarmonyType::STANDARD
           && harmony->rootTpc() != Tpc::TPC_INVALID;
}

static bool scoreHasValidChordSymbols(Score* score)
{
    for (const MeasureBase* mb = score->measures()->first(); mb; mb = mb->next()) {
        if (!mb->isMeasure()) continue;
        const Measure* m = toMeasure(mb);
        for (const Segment* seg = m->first(SegmentType::ChordRest); seg;
             seg = seg->next1(SegmentType::ChordRest)) {
            if (seg->measure() != m) break;
            for (const EngravingItem* ann : seg->annotations()) {
                if (isStandardChordSymbol(ann)) return true;
            }
        }
    }
    return false;
}

static std::vector<ChordAnalysisTone> collectRegionTones(
    const Score* score,
    int startTickInt,
    int endTickInt,
    const std::set<size_t>& excludeStaves)
{
    const analysis::ChordAnalyzerPreferences& prefs = analysis::kDefaultChordAnalyzerPreferences;

    if (!score || endTickInt <= startTickInt) {
        return {};
    }

    const Fraction startTick = Fraction::fromTicks(startTickInt);
    const Fraction endTick = Fraction::fromTicks(endTickInt);
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

    struct PedalWindow {
        int startTick = 0;
        int endTick = 0;
    };

    struct PedalTailCandidate {
        size_t staffIdx = 0;
        int pc = 0;
        int pitch = 0;
        int tpc = -1;
        int writtenEndTick = 0;
        double attackBeatWeight = 0.0;
    };

    std::map<size_t, std::vector<PedalWindow> > pedalWindowsByStaff;
    std::vector<PedalTailCandidate> pedalTailCandidates;

    for (const auto& spannerEntry : score->spanner()) {
        const Spanner* spanner = spannerEntry.second;
        if (!spanner || spanner->type() != ElementType::PEDAL) {
            continue;
        }

        const Pedal* pedal = toPedal(spanner);
        if (!pedal) {
            continue;
        }

        const auto& beginText = pedal->beginText();
        if (beginText == u"<sym>keyboardPedalSost</sym>" || beginText == u"<sym>keyboardPedalS</sym>") {
            continue;
        }

        const int pedalStartTick = pedal->tick().ticks();
        const int pedalEndTick = pedal->tick2().ticks();
        if (pedalEndTick <= pedalStartTick || pedalEndTick <= startTickInt || pedalStartTick >= endTickInt) {
            continue;
        }

        const size_t staffIdx = static_cast<size_t>(pedal->track() / VOICES);
        if (staffIdx >= score->nstaves() || excludeStaves.count(staffIdx) || !staffIsEligible(score, staffIdx)) {
            continue;
        }

        pedalWindowsByStaff[staffIdx].push_back({ pedalStartTick, pedalEndTick });
    }

    for (auto& pedalEntry : pedalWindowsByStaff) {
        auto& windows = pedalEntry.second;
        std::sort(windows.begin(), windows.end(), [](const PedalWindow& lhs, const PedalWindow& rhs) {
            if (lhs.startTick != rhs.startTick) {
                return lhs.startTick < rhs.startTick;
            }
            return lhs.endTick < rhs.endTick;
        });
    }

    auto earliestPedalReleaseTick = [&](const PedalTailCandidate& candidate) -> int {
        const auto it = pedalWindowsByStaff.find(candidate.staffIdx);
        if (it == pedalWindowsByStaff.end()) {
            return -1;
        }

        int pedalReleaseTick = std::numeric_limits<int>::max();
        for (const PedalWindow& window : it->second) {
            if (window.startTick >= candidate.writtenEndTick) {
                break;
            }
            if (window.endTick <= candidate.writtenEndTick) {
                continue;
            }
            pedalReleaseTick = std::min(pedalReleaseTick, window.endTick);
        }

        return pedalReleaseTick == std::numeric_limits<int>::max() ? -1 : pedalReleaseTick;
    };

    auto recordPedalTailCandidate = [&](size_t staffIdx, int writtenEndTick, double attackBeatWeight, const Note* note) {
        if (!note || writtenEndTick >= endTickInt || pedalWindowsByStaff.empty()) {
            return;
        }

        if (pedalWindowsByStaff.find(staffIdx) == pedalWindowsByStaff.end()) {
            return;
        }

        pedalTailCandidates.push_back({
            staffIdx,
            note->ppitch() % 12,
            note->ppitch(),
            note->tpc(),
            writtenEndTick,
            attackBeatWeight,
        });
    };

    const Fraction backLimit = startTick - Fraction(4, 1);
    const Segment* firstForward = score->tick2segment(startTick, true, SegmentType::ChordRest);
    const double bwAtRegionStart = [&]() -> double {
        const Measure* measure = score->tick2measure(startTick);
        if (!measure) {
            return 0.75;
        }
        const Segment* seg = score->tick2segment(startTick, true, SegmentType::ChordRest);
        if (!seg) {
            return 0.75;
        }
        return beatWeight(safeBeatType(measure, seg));
    }();

    if (firstForward) {
        for (const Segment* s = firstForward->prev1(SegmentType::ChordRest);
             s && s->tick() >= backLimit;
             s = s->prev1(SegmentType::ChordRest)) {
            const int segTickInt = s->tick().ticks();
            const Measure* measure = s->measure();
            const double sustainBeatWeight = measure ? beatWeight(safeBeatType(measure, s)) : bwAtRegionStart;
            for (size_t si = 0; si < score->nstaves(); ++si) {
                if (excludeStaves.count(si) || !staffIsEligible(score, si)) {
                    continue;
                }
                for (int v = 0; v < VOICES; ++v) {
                    const ChordRest* cr = s->cr(static_cast<track_idx_t>(si) * VOICES + v);
                    if (!cr || !cr->isChord() || cr->isGrace()) {
                        continue;
                    }
                    const int noteEnd = segTickInt + cr->actualTicks().ticks();
                    for (const Note* n : toChord(cr)->notes()) {
                        if (!n->play() || !n->visible()) {
                            continue;
                        }

                        recordPedalTailCandidate(si, noteEnd, sustainBeatWeight, n);

                        if (noteEnd <= startTickInt) {
                            continue;
                        }

                        const int clippedEnd = std::min(noteEnd, endTickInt);
                        const int durInRegion = clippedEnd - startTickInt;
                        if (durInRegion <= 0) {
                            continue;
                        }

                        const double baseWeight =
                            (static_cast<double>(durInRegion) / regionDuration) * bwAtRegionStart;
                        const int pc = n->ppitch() % 12;
                        PcAccum& a = accum[pc];
                        a.totalWeight += baseWeight;
                        a.durationInRegion += durInRegion;
                        a.metricTicks.insert(startTickInt);
                        voiceCountAtTick[pc][startTickInt]++;
                        if (n->ppitch() < a.lowestPitch) {
                            a.lowestPitch = n->ppitch();
                            a.tpc = n->tpc();
                        }
                    }
                }
            }
        }
    }

    if (!firstForward) {
        return {};
    }

    for (const Segment* s = firstForward;
         s && s->tick() < endTick;
         s = s->next1(SegmentType::ChordRest)) {
        const Measure* measure = s->measure();
        if (!measure) {
            continue;
        }

        const int segTickInt = s->tick().ticks();
        const BeatType bt = safeBeatType(measure, s);
        const double bw = beatWeight(bt);

        for (size_t si = 0; si < score->nstaves(); ++si) {
            if (excludeStaves.count(si) || !staffIsEligible(score, si)) {
                continue;
            }
            for (int v = 0; v < VOICES; ++v) {
                const ChordRest* cr = s->cr(static_cast<track_idx_t>(si) * VOICES + v);
                if (!cr || !cr->isChord() || cr->isGrace()) {
                    continue;
                }
                const int noteEnd = segTickInt + cr->actualTicks().ticks();
                const int clippedEnd = std::min(noteEnd, endTickInt);
                const int durInRegion = clippedEnd - segTickInt;
                if (durInRegion <= 0) {
                    continue;
                }

                const double baseWeight =
                    (static_cast<double>(durInRegion) / regionDuration) * bw;

                for (const Note* n : toChord(cr)->notes()) {
                    if (!n->play() || !n->visible()) {
                        continue;
                    }

                    recordPedalTailCandidate(si, noteEnd, bw, n);

                    const int pc = n->ppitch() % 12;
                    PcAccum& a = accum[pc];
                    a.totalWeight += baseWeight;
                    a.durationInRegion += durInRegion;
                    a.metricTicks.insert(segTickInt);
                    voiceCountAtTick[pc][segTickInt]++;

                    if (n->ppitch() < a.lowestPitch) {
                        a.lowestPitch = n->ppitch();
                        a.tpc = n->tpc();
                    }
                }
            }
        }
    }

    for (int pc = 0; pc < 12; ++pc) {
        PcAccum& a = accum[pc];
        if (a.totalWeight == 0.0) {
            continue;
        }
        const int distinct = static_cast<int>(a.metricTicks.size());
        if (distinct > 1) {
            a.totalWeight *= (1.0 + 0.3 * (distinct - 1));
        }
    }

    for (int pc = 0; pc < 12; ++pc) {
        PcAccum& a = accum[pc];
        if (a.totalWeight == 0.0) {
            continue;
        }
        int maxVoices = 0;
        for (const auto& kv : voiceCountAtTick[pc]) {
            maxVoices = std::max(maxVoices, kv.second);
        }
        if (maxVoices > 1) {
            a.totalWeight *= 1.5;
        }
    }

    // Pass 4: add a discounted sustain-pedal tail after written note-off when an
    // explicit sustain pedal remains active on the same staff.
    if (prefs.pedalTailWeightMultiplier > 0.0) {
        for (const PedalTailCandidate& candidate : pedalTailCandidates) {
            const int pedalReleaseTick = earliestPedalReleaseTick(candidate);
            if (pedalReleaseTick < 0) {
                continue;
            }

            const int tailStartTick = std::max(candidate.writtenEndTick, startTickInt);
            const int tailEndTick = std::min(pedalReleaseTick, endTickInt);
            const int tailDuration = tailEndTick - tailStartTick;
            if (tailDuration <= 0) {
                continue;
            }

            PcAccum& a = accum[candidate.pc];
            a.totalWeight += (static_cast<double>(tailDuration) / regionDuration)
                             * candidate.attackBeatWeight
                             * prefs.pedalTailWeightMultiplier;
            a.durationInRegion += tailDuration;
            if (candidate.pitch < a.lowestPitch) {
                a.lowestPitch = candidate.pitch;
                a.tpc = candidate.tpc;
            }
        }
    }

    double totalWeight = 0.0;
    for (int pc = 0; pc < 12; ++pc) {
        totalWeight += accum[pc].totalWeight;
    }
    if (totalWeight == 0.0) {
        return {};
    }

    int bassPitch = std::numeric_limits<int>::max();
    for (int pc = 0; pc < 12; ++pc) {
        if (accum[pc].totalWeight > 0.0 && accum[pc].lowestPitch < bassPitch) {
            bassPitch = accum[pc].lowestPitch;
        }
    }
    const int bassPc = (bassPitch < std::numeric_limits<int>::max()) ? (bassPitch % 12) : -1;

    std::vector<ChordAnalysisTone> tones;
    for (int pc = 0; pc < 12; ++pc) {
        PcAccum& a = accum[pc];
        if (a.totalWeight == 0.0) {
            continue;
        }

        int maxVoices = 0;
        for (const auto& kv : voiceCountAtTick[pc]) {
            maxVoices = std::max(maxVoices, kv.second);
        }

        ChordAnalysisTone t;
        t.pitch = a.lowestPitch;
        t.tpc = a.tpc;
        t.weight = a.totalWeight / totalWeight;
        t.isBass = (pc == bassPc);
        t.durationInRegion = a.durationInRegion;
        t.distinctMetricPositions = static_cast<int>(a.metricTicks.size());
        t.simultaneousVoiceCount = maxVoices;
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
    if (!score || endTick <= startTick) {
        return {};
    }

    const analysis::ChordAnalyzerPreferences& prefs = analysis::kDefaultChordAnalyzerPreferences;
    const int startTickInt = startTick.ticks();
    const int endTickInt = endTick.ticks();

    auto popcount16 = [](uint16_t bits) -> int {
        int count = 0;
        while (bits) {
            count += bits & 1u;
            bits >>= 1u;
        }
        return count;
    };

    struct Window {
        Fraction tick;
        uint16_t bits = 0;
    };
    std::vector<Window> windows;

    const Segment* seg = score->tick2segment(startTick, true, SegmentType::ChordRest);
    if (!seg) {
        return { startTick };
    }

    const int windowTicks = Constants::DIVISION;

    struct PedalWindow {
        int startTick = 0;
        int endTick = 0;
    };

    std::map<size_t, std::vector<PedalWindow> > pedalWindowsByStaff;
    for (const auto& spannerEntry : score->spanner()) {
        const Spanner* spanner = spannerEntry.second;
        if (!spanner || spanner->type() != ElementType::PEDAL) {
            continue;
        }

        const Pedal* pedal = toPedal(spanner);
        if (!pedal) {
            continue;
        }

        const auto& beginText = pedal->beginText();
        if (beginText == u"<sym>keyboardPedalSost</sym>" || beginText == u"<sym>keyboardPedalS</sym>") {
            continue;
        }

        const int pedalStartTick = pedal->tick().ticks();
        const int pedalEndTick = pedal->tick2().ticks();
        if (pedalEndTick <= pedalStartTick || pedalEndTick <= startTickInt || pedalStartTick >= endTickInt) {
            continue;
        }

        const size_t staffIdx = static_cast<size_t>(pedal->track() / VOICES);
        if (staffIdx >= score->nstaves() || excludeStaves.count(staffIdx) || !staffIsEligible(score, staffIdx)) {
            continue;
        }

        pedalWindowsByStaff[staffIdx].push_back({ pedalStartTick, pedalEndTick });
    }

    for (auto& pedalEntry : pedalWindowsByStaff) {
        auto& pedalWindows = pedalEntry.second;
        std::sort(pedalWindows.begin(), pedalWindows.end(), [](const PedalWindow& lhs, const PedalWindow& rhs) {
            if (lhs.startTick != rhs.startTick) {
                return lhs.startTick < rhs.startTick;
            }
            return lhs.endTick < rhs.endTick;
        });
    }

    auto earliestPedalReleaseTick = [&](size_t staffIdx, int writtenEndTick) -> int {
        const auto it = pedalWindowsByStaff.find(staffIdx);
        if (it == pedalWindowsByStaff.end()) {
            return -1;
        }

        int pedalReleaseTick = std::numeric_limits<int>::max();
        for (const PedalWindow& window : it->second) {
            if (window.startTick >= writtenEndTick) {
                break;
            }
            if (window.endTick <= writtenEndTick) {
                continue;
            }
            pedalReleaseTick = std::min(pedalReleaseTick, window.endTick);
        }

        return pedalReleaseTick == std::numeric_limits<int>::max() ? -1 : pedalReleaseTick;
    };

    std::map<int, uint16_t> bitsByWindowTick;

    auto addWindowBitsForSpan = [&](int spanStartTick, int spanEndTick, int pitchClass) {
        const int clippedStartTick = std::max(spanStartTick, startTickInt);
        const int clippedEndTick = std::min(spanEndTick, endTickInt);
        if (clippedEndTick <= clippedStartTick) {
            return;
        }

        for (int windowTick = (clippedStartTick / windowTicks) * windowTicks;
             windowTick < clippedEndTick;
             windowTick += windowTicks) {
            bitsByWindowTick[windowTick] |= static_cast<uint16_t>(1u << pitchClass);
        }
    };

    auto recordPedalTailSpan = [&](size_t staffIdx, int writtenEndTick, const Note* note) {
        if (!note || pedalWindowsByStaff.empty()) {
            return;
        }

        const int pedalReleaseTick = earliestPedalReleaseTick(staffIdx, writtenEndTick);
        if (pedalReleaseTick <= writtenEndTick) {
            return;
        }

        addWindowBitsForSpan(writtenEndTick, pedalReleaseTick, note->ppitch() % 12);
    };

    const Fraction backLimit = startTick - Fraction(4, 1);
    for (const Segment* s = seg->prev1(SegmentType::ChordRest);
         s && s->tick() >= backLimit;
         s = s->prev1(SegmentType::ChordRest)) {
        const int segTick = s->tick().ticks();

        for (size_t si = 0; si < score->nstaves(); ++si) {
            if (excludeStaves.count(si) || !staffIsEligible(score, si)) {
                continue;
            }
            for (voice_idx_t v = 0; v < VOICES; ++v) {
                const EngravingItem* e = s->element(staff2track(si, v));
                if (!e || !e->isChord()) {
                    continue;
                }

                const Chord* chord = toChord(e);
                if (chord->isGrace()) {
                    continue;
                }

                for (const Note* note : chord->notes()) {
                    const int noteEndTick = segTick + chord->actualTicks().ticks();
                    recordPedalTailSpan(si, noteEndTick, note);
                }
            }
        }
    }

    for (const Segment* s = seg; s && s->tick() < endTick; s = s->next1(SegmentType::ChordRest)) {
        const int segTick = s->tick().ticks();
        const int segWindowTick = (segTick / windowTicks) * windowTicks;

        for (size_t si = 0; si < score->nstaves(); ++si) {
            if (excludeStaves.count(si) || !staffIsEligible(score, si)) {
                continue;
            }
            for (voice_idx_t v = 0; v < VOICES; ++v) {
                const EngravingItem* e = s->element(staff2track(si, v));
                if (!e || !e->isChord()) {
                    continue;
                }

                const Chord* chord = toChord(e);
                if (chord->isGrace()) {
                    continue;
                }

                const int noteEndTick = segTick + chord->actualTicks().ticks();
                for (const Note* note : chord->notes()) {
                    bitsByWindowTick[segWindowTick] |= static_cast<uint16_t>(1u << (note->ppitch() % 12));
                    recordPedalTailSpan(si, noteEndTick, note);
                }
            }
        }
    }

    windows.reserve(bitsByWindowTick.size());
    for (const auto& entry : bitsByWindowTick) {
        if (entry.second == 0) {
            continue;
        }
        windows.push_back({ Fraction::fromTicks(entry.first), entry.second });
    }

    if (windows.empty()) {
        return { startTick };
    }

    std::vector<Fraction> boundaries;
    boundaries.push_back(startTick);

    uint16_t previousBits = windows[0].bits;
    for (size_t i = 1; i < windows.size(); ++i) {
        const uint16_t bits = windows[i].bits;
        const uint16_t intersection = previousBits & bits;
        const uint16_t unionBits = previousBits | bits;
        const int intersectionCount = popcount16(intersection);
        const int unionCount = popcount16(unionBits);
        const double distance = (unionCount > 0)
            ? (1.0 - static_cast<double>(intersectionCount) / unionCount)
            : 0.0;

        if (distance >= prefs.harmonicBoundaryJaccardThreshold) {
            boundaries.push_back(windows[i].tick);
            previousBits = bits;
        } else {
            previousBits = unionBits;
        }
    }

    return boundaries;
}

struct SoundingNote {
    int ppitch = 0;
    int tpc = -1;
};

static void collectSoundingAt(const Score* score,
                              const Segment* anchorSegment,
                              const std::set<size_t>& excludeStaves,
                              std::vector<SoundingNote>& out)
{
    if (!score || !anchorSegment) {
        return;
    }

    const Fraction anchorTick = anchorSegment->tick();

    auto collectChordRest = [&](const Segment* segment, const ChordRest* chordRest) {
        if (!chordRest || !chordRest->isChord() || chordRest->isGrace()) {
            return;
        }
        if (segment->tick() < anchorTick) {
            const Fraction noteEnd = segment->tick() + toChord(chordRest)->actualTicks();
            if (noteEnd <= anchorTick) {
                return;
            }
        }
        for (const Note* note : toChord(chordRest)->notes()) {
            if (!note->play() || !note->visible()) {
                continue;
            }
            out.push_back({ note->ppitch(), note->tpc() });
        }
    };

    for (size_t staffIndex = 0; staffIndex < score->nstaves(); ++staffIndex) {
        if (excludeStaves.count(staffIndex) || !staffIsEligible(score, staffIndex, anchorTick)) {
            continue;
        }
        for (voice_idx_t voice = 0; voice < VOICES; ++voice) {
            collectChordRest(anchorSegment,
                             anchorSegment->cr(static_cast<track_idx_t>(staffIndex) * VOICES + voice));
        }
    }

    const Fraction backLimit = anchorTick - Fraction(4, 1);
    for (const Segment* segment = anchorSegment->prev1(SegmentType::ChordRest);
         segment && segment->tick() >= backLimit;
         segment = segment->prev1(SegmentType::ChordRest)) {
        for (size_t staffIndex = 0; staffIndex < score->nstaves(); ++staffIndex) {
            if (excludeStaves.count(staffIndex) || !staffIsEligible(score, staffIndex, anchorTick)) {
                continue;
            }
            for (voice_idx_t voice = 0; voice < VOICES; ++voice) {
                collectChordRest(segment,
                                 segment->cr(static_cast<track_idx_t>(staffIndex) * VOICES + voice));
            }
        }
    }
}

static std::vector<ChordAnalysisTone> buildTones(const std::vector<SoundingNote>& sounding)
{
    int lowestPitch = std::numeric_limits<int>::max();
    for (const auto& soundingNote : sounding) {
        lowestPitch = std::min(lowestPitch, soundingNote.ppitch);
    }

    std::vector<ChordAnalysisTone> tones;
    tones.reserve(sounding.size());
    for (const auto& soundingNote : sounding) {
        ChordAnalysisTone tone;
        tone.pitch = soundingNote.ppitch;
        tone.tpc = soundingNote.tpc;
        tone.isBass = (soundingNote.ppitch == lowestPitch);
        tones.push_back(tone);
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
    ChordTemporalContext temporalContext;
    if (!score || !segment) {
        return temporalContext;
    }

    const Fraction tick = segment->tick();
    const auto chordAnalyzer = analysis::ChordAnalyzerFactory::create();

    for (const Segment* previousSegment = segment->prev1(SegmentType::ChordRest);
         previousSegment != nullptr;
         previousSegment = previousSegment->prev1(SegmentType::ChordRest)) {
        bool hasAttacks = false;
        for (size_t staffIndex = 0; staffIndex < score->nstaves() && !hasAttacks; ++staffIndex) {
            if (excludeStaves.count(staffIndex) || !staffIsEligible(score, staffIndex, tick)) {
                continue;
            }
            for (int voice = 0; voice < VOICES && !hasAttacks; ++voice) {
                const ChordRest* chordRest = previousSegment->cr(
                    static_cast<track_idx_t>(staffIndex) * VOICES + voice);
                if (chordRest && chordRest->isChord() && !chordRest->isGrace()) {
                    hasAttacks = true;
                }
            }
        }
        if (!hasAttacks) {
            continue;
        }

        std::vector<SoundingNote> previousSounding;
        collectSoundingAt(score, previousSegment, excludeStaves, previousSounding);
        if (!previousSounding.empty()) {
            const auto previousTones = buildTones(previousSounding);
            const auto previousResults = chordAnalyzer->analyzeChord(previousTones, keyFifths, keyMode);
            if (!previousResults.empty()) {
                temporalContext.previousRootPc = previousResults.front().identity.rootPc;
                temporalContext.previousQuality = previousResults.front().identity.quality;
                temporalContext.previousBassPc = previousResults.front().identity.bassPc;
            }
        }
        break;
    }

    if (currentBassPc != -1 && temporalContext.previousBassPc != -1) {
        temporalContext.bassIsStepwiseFromPrevious = isDiatonicStep(
            temporalContext.previousBassPc, currentBassPc);
    }

    return temporalContext;
}

static void injectWrittenRootTone(
    std::vector<ChordAnalysisTone>& tones,
    int writtenRootPc,
    int regionDurationTicks)
{
    if (writtenRootPc < 0) {
        return;
    }

    for (auto& tone : tones) {
        tone.isBass = false;
    }

    ChordAnalysisTone syntheticBass;
    syntheticBass.pitch = analysis::normalizePc(writtenRootPc) + 36;
    syntheticBass.tpc = -1;
    syntheticBass.weight = 2.0;
    syntheticBass.isBass = true;
    syntheticBass.durationInRegion = regionDurationTicks;
    syntheticBass.distinctMetricPositions = 4;
    syntheticBass.simultaneousVoiceCount = 1;
    tones.insert(tones.begin(), syntheticBass);
}

/// Jazz path: build AnalyzedRegion list from written chord symbols.
/// Written chord symbols define the region boundaries and provide comparison
/// metadata only. Chord identity still comes from note-based analysis.
static std::vector<AnalyzedRegion> analyzeScoreJazz(
    Score* score,
    const std::set<size_t>& excludeStaves,
    const analysis::KeyModeAnalyzerPreferences& keyPrefs,
    bool injectWrittenRoot,
    const analysis::ChordAnalyzerPreferences& chordPrefs = analysis::kDefaultChordAnalyzerPreferences)
{
    // Collect all (tick, Harmony*) pairs in score order.
    struct ChordSymbolEvent {
        Fraction tick;
        const Harmony* harmony;
        int measureNumber;
        double beat;
    };
    std::vector<ChordSymbolEvent> events;

    const int division = Constants::DIVISION;
    int nextMeasureNumber = 0;
    for (const MeasureBase* mb = score->measures()->first(); mb; mb = mb->next()) {
        if (!mb->isMeasure()) continue;
        const Measure* m = toMeasure(mb);
        nextMeasureNumber += m->measureNumberOffset();
        const int displayedMeasureNumber = nextMeasureNumber + 1;
        for (const Segment* seg = m->first(SegmentType::ChordRest); seg;
             seg = seg->next1(SegmentType::ChordRest)) {
            if (seg->measure() != m) break;
            for (const EngravingItem* ann : seg->annotations()) {
                if (!isStandardChordSymbol(ann)) continue;
                const Harmony* h = toHarmony(ann);
                // Deduplicate: skip if we already have a chord symbol at this tick.
                if (!events.empty() && events.back().tick == seg->tick()) break;
                const int tickInMeasure = seg->tick().ticks() - m->tick().ticks();
                ChordSymbolEvent ev;
                ev.tick          = seg->tick();
                ev.harmony       = h;
                ev.measureNumber = displayedMeasureNumber;
                ev.beat          = 1.0 + static_cast<double>(tickInMeasure) / division;
                events.push_back(ev);
                break;  // first Harmony at this tick wins
            }
        }

        if (!m->excludeFromNumbering()) {
            ++nextMeasureNumber;
        }

        const LayoutBreak* layoutBreak = m->sectionBreakElement();
        if (layoutBreak && layoutBreak->startWithMeasureOne()) {
            nextMeasureNumber = 0;
        }
    }

    if (events.empty()) return {};

    const Fraction endTick = score->endTick();
    std::vector<AnalyzedRegion> result;
    result.reserve(events.size());
    const size_t refStaff = referenceStaffForAnalysis(score, excludeStaves);

    ChordTemporalContext ctx;
    ctx.previousRootPc = -1;
    ctx.previousQuality = ChordQuality::Unknown;
    ctx.jazzMode = true;

    std::optional<KeyModeAnalysisResult> prevKey;

    for (size_t i = 0; i < events.size(); ++i) {
        const auto& ev = events[i];
        const Fraction regionEnd = (i + 1 < events.size()) ? events[i + 1].tick : endTick;

        const int writtenRootPc = tpc2pitch(ev.harmony->rootTpc()) % 12;
        ChordQuality writtenQuality = ChordQuality::Unknown;
        if (const ParsedChord* parsedChord = ev.harmony->parsedForm()) {
            writtenQuality = xmlKindToQuality(parsedChord->xmlKind());
        }

        auto regionTones = collectRegionTones(score,
                                              ev.tick.ticks(),
                                              regionEnd.ticks(),
                                              excludeStaves);
        if (injectWrittenRoot) {
            injectWrittenRootTone(regionTones, writtenRootPc, regionEnd.ticks() - ev.tick.ticks());
        }

        const std::vector<KeyModeAnalysisResult> keyRanked = inferLocalKey(
            score, refStaff, excludeStaves, ev.tick,
            prevKey.has_value() ? &prevKey.value() : nullptr, keyPrefs);
        const KeyModeAnalysisResult& localKey = keyRanked[0];
        prevKey = localKey;

        ChordAnalysisResult chord;
        bool hasAnalyzedChord = false;
        auto candidates = analysis::RuleBasedChordAnalyzer{}.analyzeChord(
            regionTones, localKey.keySignatureFifths, localKey.mode, &ctx, chordPrefs);
        if (!candidates.empty()) {
            chord = candidates[0];
            hasAnalyzedChord = true;
            ctx.previousRootPc = candidates[0].identity.rootPc;
            ctx.previousQuality = candidates[0].identity.quality;
            ctx.previousBassPc = candidates[0].identity.bassPc;
        }

        const uint16_t pcMask = pitchClassMask(regionTones);
        int bassPc = -1;
        for (const auto& t : regionTones) {
            if (t.isBass) { bassPc = t.pitch % 12; break; }
        }

        AnalyzedRegion ar;
        ar.startTick      = ev.tick.ticks();
        ar.endTick        = regionEnd.ticks();
        ar.measureNumber  = ev.measureNumber;
        ar.beat           = ev.beat;
        ar.chord          = chord;
        ar.hasAnalyzedChord = hasAnalyzedChord;
        ar.key            = localKey;
        ar.keyRanked      = keyRanked;
        ar.tones          = std::move(regionTones);
        ar.pcMask         = pcMask;
        ar.bassPc         = bassPc;
        ar.fromChordSymbol = true;
        ar.writtenRootPc   = writtenRootPc;
        ar.writtenQuality  = writtenQuality;

        for (size_t candidateIndex = 1; candidateIndex < candidates.size() && candidateIndex <= 2; ++candidateIndex) {
            ar.alternatives.push_back(candidates[candidateIndex]);
        }

        result.push_back(std::move(ar));
    }

    return result;
}

static std::vector<AnalyzedRegion> analyzeScore(
    Score* score,
    const std::set<size_t>& excludeStaves,
    const analysis::KeyModeAnalyzerPreferences& keyPrefs = analysis::KeyModeAnalyzerPreferences{},
    bool injectWrittenRoot = false,
    const analysis::ChordAnalyzerPreferences& chordPrefs = analysis::kDefaultChordAnalyzerPreferences)
{
    // §4.1c Jazz detection gate: when the score contains written chord symbols,
    // use chord-symbol-driven boundaries but still analyze note content within
    // those regions.
    if (scoreHasValidChordSymbols(score)) {
        return analyzeScoreJazz(score, excludeStaves, keyPrefs, injectWrittenRoot, chordPrefs);
    }

    const Segment* firstSegment = score->tick2segment(Fraction(0, 1), true, SegmentType::ChordRest);
    if (!firstSegment) {
        return {};
    }

    const Fraction startTick = firstSegment->tick();
    const Fraction endTick = score->endTick();
    std::vector<AnalyzedRegion> result;
    const auto boundaryTicks = detectHarmonicBoundariesJaccard(score, startTick, endTick, excludeStaves);
    result.reserve(boundaryTicks.size());
    const size_t refStaff = referenceStaffForAnalysis(score, excludeStaves);

    const auto initialKey = inferLocalKey(score, refStaff, excludeStaves, startTick, nullptr, keyPrefs)[0];
    ChordTemporalContext ctx = findTemporalContext(
        score, firstSegment, excludeStaves, initialKey.keySignatureFifths, initialKey.mode, -1);

    const auto chordAnalyzer = analysis::ChordAnalyzerFactory::create();

    // Hysteresis: track the previous key result across regions.
    std::optional<KeyModeAnalysisResult> prevKey;

    for (size_t boundaryIndex = 0; boundaryIndex < boundaryTicks.size(); ++boundaryIndex) {
        const Fraction regionStart = boundaryTicks[boundaryIndex];
        const Fraction regionEnd = (boundaryIndex + 1 < boundaryTicks.size()) ? boundaryTicks[boundaryIndex + 1] : endTick;
        auto tones = collectRegionTones(score,
                                        regionStart.ticks(),
                                        regionEnd.ticks(),
                                        excludeStaves);
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

        int nextBassPc = -1;
        if (currentBassPc != -1 && boundaryIndex + 1 < boundaryTicks.size()) {
            const Fraction nextRegionStart = boundaryTicks[boundaryIndex + 1];
            const Fraction nextRegionEnd = (boundaryIndex + 2 < boundaryTicks.size())
                                           ? boundaryTicks[boundaryIndex + 2]
                                           : endTick;
            const auto nextTones = collectRegionTones(score,
                                                      nextRegionStart.ticks(),
                                                      nextRegionEnd.ticks(),
                                                      excludeStaves);
            for (const auto& tone : nextTones) {
                if (tone.isBass) {
                    nextBassPc = tone.pitch % 12;
                    break;
                }
            }
        }
        ctx.bassIsStepwiseToNext = (currentBassPc != -1 && nextBassPc != -1)
            && isDiatonicStep(currentBassPc, nextBassPc);

        // Infer key using the same windowed approach as the bridge.
        // Pass the previous result for hysteresis (nullptr on the first region).
        const std::vector<KeyModeAnalysisResult> keyRanked = inferLocalKey(
            score, refStaff, excludeStaves, regionStart,
            prevKey.has_value() ? &prevKey.value() : nullptr,
            keyPrefs);
        const KeyModeAnalysisResult& localKey = keyRanked[0];
        prevKey = localKey;

        auto candidates = chordAnalyzer->analyzeChord(
            tones, localKey.keySignatureFifths, localKey.mode, &ctx, chordPrefs);

        if (candidates.empty()) {
            continue;
        }

        // Compute pitch-class metadata from tones.
        const uint16_t pcMask = pitchClassMask(tones);
        const int bassPc = currentBassPc;

        ctx.previousRootPc = candidates[0].identity.rootPc;
        ctx.previousQuality = candidates[0].identity.quality;
        ctx.previousBassPc = candidates[0].identity.bassPc;

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

        // Up to 2 alternatives (indices 1 and 2 from analyzeChord)
        for (size_t candidateIndex = 1; candidateIndex < candidates.size() && candidateIndex <= 2; ++candidateIndex) {
            ar.alternatives.push_back(candidates[candidateIndex]);
        }

        result.push_back(std::move(ar));
    }

    if (result.empty()) {
        return {};
    }

    const int minRegionTicks = Constants::DIVISION;
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
    converted.fromChordSymbol = region.fromChordSymbol;
    converted.writtenRootPc = region.writtenRootPc;

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
        out << "      \"fromChordSymbol\": " << (r.fromChordSymbol ? "true" : "false")             << ",\n";
        out << "      \"writtenRootPc\": "   << r.writtenRootPc                                     << ",\n";
        out << "      \"writtenQuality\": \"" << qualityToString(r.writtenQuality)                  << "\",\n";
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

            out << "        {"
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
        << "  --inject-written-root\n"
        << "            Diagnostic batch-only option for chord-symbol-driven jazz\n"
        << "            regions: inject the written root as a synthetic bass tone\n"
        << "            before chord analysis. Does not affect any bridge path.\n"
        << "  --dump-regions <mode>\n"
        << "            Select which analysis path to serialize. 'batch' writes the\n"
        << "            tool's current batch path, 'notation' writes the live notation\n"
        << "            bridge result, and 'notation-premerge' writes the notation\n"
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
    // Syntax: <input> [output] [--preset <name>] [--inject-written-root]
    //         [--dump-regions <batch|notation|notation-premerge>]
    //         [--diagnose-measures N[,N,...]]
    // Options may appear anywhere after the input path.
    muse::io::path_t inputPath;
    muse::io::path_t outputPath;
    std::string presetName = "Standard";
    bool injectWrittenRoot = false;
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
        } else if (a == "--inject-written-root") {
            injectWrittenRoot = true;
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
    // Jazz preset uses the lower seventh threshold (0.12) for extension detection
    // so that lightly-voiced ninths (pcWeight 0.12–0.19) register as extensions.
    // Standard and Baroque keep the conservative 0.20 threshold to suppress
    // ornamental passing tones common in counterpoint textures.
    analysis::ChordAnalyzerPreferences chordPrefs;
    if (presetName == "Jazz") {
        chordPrefs.extensionThreshold = 0.12;  // kSeventhThreshold — matches seventh detection
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
        regions = analyzeScore(score, excludeStaves, keyPrefs, injectWrittenRoot, chordPrefs);
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
