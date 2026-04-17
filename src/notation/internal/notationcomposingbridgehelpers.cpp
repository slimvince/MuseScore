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

// ── Shared bridge helpers ────────────────────────────────────────────────────
//
// File-local utilities shared by:
//   • notationcomposingbridge.cpp  — harmonicAnnotation, analyzeNoteHarmonicContext
//   • notationharmonicrhythmbridge.cpp — analyzeHarmonicRhythm

#include "notationcomposingbridgehelpers.h"
#include "notationanalysisinternal.h"
#include "notationcomposingbridge.h"

#include <algorithm>
#include <array>
#include <cmath>
#include <limits>
#include <map>
#include <optional>
#include <set>
#include <tuple>

#include "engraving/dom/chord.h"
#include "engraving/dom/harmony.h"
#include "engraving/dom/key.h"
#include "engraving/dom/masterscore.h"
#include "engraving/dom/measure.h"
#include "engraving/dom/note.h"
#include "engraving/dom/pedal.h"
#include "engraving/dom/segment.h"
#include "engraving/dom/sig.h"
#include "engraving/dom/staff.h"

#include "composing/analysis/chord/analysisutils.h"
#include "composing/analysis/chord/chordanalyzer.h"
#include "composing/analysis/key/keymodeanalyzer.h"
#include "composing/icomposinganalysisconfiguration.h"
#include "modularity/ioc.h"

using mu::notation::internal::isChordTrackStaff;
using mu::notation::internal::staffIsEligible;

namespace mu::notation::internal {

mu::composing::analysis::ChordSymbolFormatter::NoteSpelling scoreNoteSpelling(
    const mu::engraving::Score* score)
{
    using mu::engraving::NoteSpellingType;
    using mu::engraving::Sid;
    namespace CSF = mu::composing::analysis::ChordSymbolFormatter;

    if (!score) {
        return CSF::NoteSpelling::Standard;
    }
    const auto mStyle = score->style().styleV(Sid::chordSymbolSpelling).value<NoteSpellingType>();
    switch (mStyle) {
    case NoteSpellingType::GERMAN:      return CSF::NoteSpelling::German;
    case NoteSpellingType::GERMAN_PURE: return CSF::NoteSpelling::GermanPure;
    default:                            return CSF::NoteSpelling::Standard;
    }
}

namespace {

const std::array<int, 7>& keyModeScaleIntervals(mu::composing::analysis::KeySigMode mode)
{
    static constexpr std::array<std::array<int, 7>, 21> MODE_SCALES = {{
        { 0, 2, 4, 5, 7, 9, 11 },
        { 0, 2, 3, 5, 7, 9, 10 },
        { 0, 1, 3, 5, 7, 8, 10 },
        { 0, 2, 4, 6, 7, 9, 11 },
        { 0, 2, 4, 5, 7, 9, 10 },
        { 0, 2, 3, 5, 7, 8, 10 },
        { 0, 1, 3, 5, 6, 8, 10 },
        { 0, 2, 3, 5, 7, 9, 11 },
        { 0, 1, 3, 5, 7, 9, 10 },
        { 0, 2, 4, 6, 8, 9, 11 },
        { 0, 2, 4, 6, 7, 9, 10 },
        { 0, 2, 4, 5, 7, 8, 10 },
        { 0, 2, 3, 5, 6, 8, 10 },
        { 0, 1, 3, 4, 6, 8, 10 },
        { 0, 2, 3, 5, 7, 8, 11 },
        { 0, 1, 3, 5, 6, 9, 10 },
        { 0, 2, 4, 5, 8, 9, 11 },
        { 0, 2, 3, 6, 7, 9, 10 },
        { 0, 1, 4, 5, 7, 8, 10 },
        { 0, 3, 4, 6, 7, 9, 11 },
        { 0, 1, 3, 4, 6, 8, 9 },
    }};

    const size_t modeIdx = mu::composing::analysis::keyModeIndex(mode);
    return MODE_SCALES[modeIdx < MODE_SCALES.size() ? modeIdx : 0];
}

std::optional<std::tuple<mu::composing::analysis::ChordQuality, int, int>> diatonicTriadShapeForDegree(
    int degree,
    mu::composing::analysis::KeySigMode keyMode)
{
    using mu::composing::analysis::ChordQuality;

    if (degree < 0 || degree > 6) {
        return std::nullopt;
    }

    const auto& scale = keyModeScaleIntervals(keyMode);
    const int rootInterval = scale[static_cast<size_t>(degree)];
    const int thirdDegree = degree + 2;
    const int fifthDegree = degree + 4;
    const int thirdInterval = (scale[static_cast<size_t>(thirdDegree % 7)]
                               + (thirdDegree >= 7 ? 12 : 0)
                               - rootInterval) % 12;
    const int fifthInterval = (scale[static_cast<size_t>(fifthDegree % 7)]
                               + (fifthDegree >= 7 ? 12 : 0)
                               - rootInterval) % 12;

    if (thirdInterval == 4 && fifthInterval == 7) {
        return std::make_tuple(ChordQuality::Major, thirdInterval, fifthInterval);
    }
    if (thirdInterval == 3 && fifthInterval == 7) {
        return std::make_tuple(ChordQuality::Minor, thirdInterval, fifthInterval);
    }
    if (thirdInterval == 3 && fifthInterval == 6) {
        return std::make_tuple(ChordQuality::Diminished, thirdInterval, fifthInterval);
    }
    if (thirdInterval == 4 && fifthInterval == 8) {
        return std::make_tuple(ChordQuality::Augmented, thirdInterval, fifthInterval);
    }

    return std::nullopt;
}

int diatonicDegreeForRootPc(int rootPc, int keyFifths, mu::composing::analysis::KeySigMode keyMode)
{
    const int tonicPc = (mu::composing::analysis::ionianTonicPcFromFifths(keyFifths)
                         + keyModeTonicOffset(keyMode)) % 12;
    const auto& scale = keyModeScaleIntervals(keyMode);
    for (size_t i = 0; i < scale.size(); ++i) {
        if ((tonicPc + scale[i]) % 12 == rootPc) {
            return static_cast<int>(i);
        }
    }

    return -1;
}

bool tonesFitTriadShape(const std::vector<mu::composing::analysis::ChordAnalysisTone>& tones,
                       int rootPc,
                       int thirdInterval,
                       int fifthInterval)
{
    bool seenPitchClasses[12] = {};
    for (const auto& tone : tones) {
        const int pitchClass = tone.pitch % 12;
        if (seenPitchClasses[pitchClass]) {
            continue;
        }
        seenPitchClasses[pitchClass] = true;

        const int interval = (pitchClass - rootPc + 12) % 12;
        if (interval != 0 && interval != thirdInterval && interval != fifthInterval) {
            return false;
        }
    }

    return true;
}

int distinctPitchClassCount(const std::vector<mu::composing::analysis::ChordAnalysisTone>& tones)
{
    bool seenPitchClasses[12] = {};
    int count = 0;
    for (const auto& tone : tones) {
        const int pitchClass = tone.pitch % 12;
        if (seenPitchClasses[pitchClass]) {
            continue;
        }
        seenPitchClasses[pitchClass] = true;
        ++count;
    }
    return count;
}

} // anonymous namespace

void refineSparseChordQualityFromKeyContext(
    mu::composing::analysis::ChordAnalysisResult& result,
    const std::vector<mu::composing::analysis::ChordAnalysisTone>& tones,
    int keyFifths,
    mu::composing::analysis::KeySigMode keyMode)
{
    using namespace mu::composing::analysis;

    if (result.identity.quality != ChordQuality::Unknown) {
        return;
    }

    const int uniquePitchClasses = distinctPitchClassCount(tones);

    int degree = result.function.degree;
    if (degree < 0 || degree > 6) {
        degree = diatonicDegreeForRootPc(result.identity.rootPc, keyFifths, keyMode);
        if (degree < 0) {
            return;
        }

        result.function.degree = degree;
        result.function.keyTonicPc = (mu::composing::analysis::ionianTonicPcFromFifths(keyFifths)
                                      + keyModeTonicOffset(keyMode)) % 12;
        result.function.keyMode = keyMode;
    }

    const auto triadShape = diatonicTriadShapeForDegree(degree, keyMode);
    if (!triadShape) {
        return;
    }

    const auto [quality, thirdInterval, fifthInterval] = *triadShape;

    // In plain Aeolian, a lone tonic or dominant pitch is too ambiguous to
    // harden into a minor triad. Leave it unqualified and let richer later
    // evidence decide the quality.
    if (uniquePitchClasses == 1
        && quality == ChordQuality::Minor
        && keyMode == KeySigMode::Aeolian
        && (degree == 0 || degree == 4)) {
        return;
    }

    if (!tonesFitTriadShape(tones, result.identity.rootPc, thirdInterval, fifthInterval)) {
        return;
    }

    result.identity.quality = quality;
}

namespace {

void stabilizeHarmonicRegionsForDisplay(std::vector<mu::composing::analysis::HarmonicRegion>& regions)
{
    using namespace mu::composing::analysis;

    if (regions.empty()) {
        return;
    }

    int stableKeyFifths = regions.front().keyModeResult.keySignatureFifths;
    KeySigMode stableMode = regions.front().keyModeResult.mode;

    for (size_t i = 1; i < regions.size(); ++i) {
        const int regionKeyFifths = regions[i].keyModeResult.keySignatureFifths;
        const KeySigMode regionMode = regions[i].keyModeResult.mode;
        if (regionKeyFifths != stableKeyFifths || regionMode != stableMode) {
            bool persistent = (i + 1 >= regions.size());
            if (!persistent) {
                const int nextKeyFifths = regions[i + 1].keyModeResult.keySignatureFifths;
                const KeySigMode nextMode = regions[i + 1].keyModeResult.mode;
                persistent = (nextKeyFifths == regionKeyFifths && nextMode == regionMode);
            }
            if (persistent) {
                stableKeyFifths = regionKeyFifths;
                stableMode = regionMode;
            }
        }
        regions[i].keyModeResult.keySignatureFifths = stableKeyFifths;
        regions[i].keyModeResult.mode = stableMode;
    }

    for (auto& region : regions) {
        const int ionianPc = ionianTonicPcFromFifths(region.keyModeResult.keySignatureFifths);
        const int tonicPc = (ionianPc + keyModeTonicOffset(region.keyModeResult.mode)) % 12;
        const auto& scale = keyModeScaleIntervals(region.keyModeResult.mode);

        int degree = -1;
        for (size_t i = 0; i < scale.size(); ++i) {
            if ((tonicPc + scale[i]) % 12 == region.chordResult.identity.rootPc) {
                degree = static_cast<int>(i);
                break;
            }
        }
        region.chordResult.function.degree = degree;
        region.chordResult.function.keyTonicPc = tonicPc;
        region.chordResult.function.keyMode = region.keyModeResult.mode;

        bool diatonic = (degree >= 0);
        if (diatonic) {
            for (const auto& tone : region.tones) {
                const int pc = tone.pitch % 12;
                bool inScale = false;
                for (int interval : scale) {
                    if ((tonicPc + interval) % 12 == pc) {
                        inScale = true;
                        break;
                    }
                }
                if (!inScale) {
                    diatonic = false;
                    break;
                }
            }
        }
        region.chordResult.function.diatonicToKey = diatonic;
        refineSparseChordQualityFromKeyContext(region.chordResult,
                                               region.tones,
                                               region.keyModeResult.keySignatureFifths,
                                               region.keyModeResult.mode);
    }
}

} // namespace

void collectSoundingAt(const mu::engraving::Score* sc,
                       const mu::engraving::Segment* anchorSeg,
                       const std::set<size_t>& excludeStaves,
                       std::vector<SoundingNote>& out)
{
    using namespace mu::engraving;

    const Fraction anchorTick = anchorSeg->tick();

    auto collectCr = [&](const Segment* s, const ChordRest* cr) {
        if (!cr || !cr->isChord() || cr->isGrace()) {
            return;
        }
        if (s->tick() < anchorTick) {
            const Fraction noteEnd = s->tick() + toChord(cr)->actualTicks();
            if (noteEnd <= anchorTick) {
                return;
            }
        }
        for (const Note* n : toChord(cr)->notes()) {
            if (!n->play() || !n->visible()) {
                continue;  // skip silent notes and invisible tuning artifacts
            }
            out.push_back({ n->ppitch(), n->tpc() });
        }
    };

    for (size_t si = 0; si < sc->nstaves(); ++si) {
        if (excludeStaves.count(si) || !staffIsEligible(sc, si, anchorTick)) {
            continue;
        }
        for (int v = 0; v < VOICES; ++v) {
            collectCr(anchorSeg,
                      anchorSeg->cr(static_cast<track_idx_t>(si) * VOICES + v));
        }
    }

    const Fraction backLimit = anchorTick - Fraction(4, 1);
    for (const Segment* s = anchorSeg->prev1(SegmentType::ChordRest);
         s && s->tick() >= backLimit;
         s = s->prev1(SegmentType::ChordRest)) {
        for (size_t si = 0; si < sc->nstaves(); ++si) {
            if (excludeStaves.count(si) || !staffIsEligible(sc, si, anchorTick)) {
                continue;
            }
            for (int v = 0; v < VOICES; ++v) {
                collectCr(s, s->cr(static_cast<track_idx_t>(si) * VOICES + v));
            }
        }
    }
}

std::vector<mu::composing::analysis::ChordAnalysisTone>
buildTones(const std::vector<SoundingNote>& sounding)
{
    using mu::composing::analysis::ChordAnalysisTone;

    int lowestPpitch = std::numeric_limits<int>::max();
    for (const SoundingNote& sn : sounding) {
        if (sn.ppitch < lowestPpitch) {
            lowestPpitch = sn.ppitch;
        }
    }
    std::vector<ChordAnalysisTone> tones;
    tones.reserve(sounding.size());
    for (const SoundingNote& sn : sounding) {
        ChordAnalysisTone t;
        t.pitch  = sn.ppitch;
        t.tpc    = sn.tpc;
        t.isBass = (sn.ppitch == lowestPpitch);
        tones.push_back(t);
    }
    return tones;
}

double beatTypeToWeight(mu::engraving::BeatType bt,
                        const mu::composing::analysis::KeyModeAnalyzerPreferences& prefs)
{
    using mu::engraving::BeatType;
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

mu::engraving::BeatType safeBeatType(const mu::engraving::Measure* measure,
                                     const mu::engraving::Segment* segment)
{
    using namespace mu::engraving;

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

double timeDecay(double beatsAgo, double decayRate)
{
    return std::pow(decayRate, beatsAgo / 4.0);
}

int distinctPitchClasses(
    const std::vector<mu::composing::analysis::KeyModeAnalyzer::PitchContext>& ctx)
{
    bool seen[12] = {};
    int count = 0;
    for (const auto& p : ctx) {
        int pc = p.pitch % 12;
        if (!seen[pc]) {
            seen[pc] = true;
            ++count;
        }
    }
    return count;
}

void collectPitchContext(const mu::engraving::Score* sc,
                         const mu::engraving::Fraction& tick,
                         const mu::engraving::Fraction& windowStart,
                         const mu::engraving::Fraction& windowEnd,
                         const std::set<size_t>& excludeStaves,
                         const mu::composing::analysis::KeyModeAnalyzerPreferences& prefs,
                         std::vector<mu::composing::analysis::KeyModeAnalyzer::PitchContext>& ctx)
{
    using namespace mu::engraving;
    using namespace mu::composing::analysis;

    static constexpr double LOOKAHEAD_WEIGHT = 0.5;

    const Measure* startMeasure = sc->tick2measure(windowStart);
    if (!startMeasure) {
        startMeasure = sc->firstMeasure();
    }
    if (!startMeasure) {
        return;
    }

    for (const Segment* s = startMeasure->first(SegmentType::ChordRest);
         s && s->tick() <= windowEnd;
         s = s->next1(SegmentType::ChordRest)) {
        const Fraction segTick = s->tick();
        if (segTick < windowStart) {
            continue;
        }

        const Measure* m = s->measure();
        const BeatType bt = safeBeatType(m, s);
        const double bw = beatTypeToWeight(bt, prefs);

        const double beatsFromTick =
            std::abs((segTick - tick).ticks())
            / static_cast<double>(Constants::DIVISION);
        const double decay = timeDecay(beatsFromTick);

        const bool isLookahead = (segTick > tick);
        const double lookaheadMul = isLookahead ? LOOKAHEAD_WEIGHT : 1.0;

        struct NoteInfo { int ppitch; double durationQn; };
        std::vector<NoteInfo> segNotes;
        int lowestPitch = std::numeric_limits<int>::max();

        for (size_t si = 0; si < sc->nstaves(); ++si) {
            if (excludeStaves.count(si) || !staffIsEligible(sc, si, tick)) {
                continue;
            }
            for (int v = 0; v < VOICES; ++v) {
                const ChordRest* cr
                    = s->cr(static_cast<track_idx_t>(si) * VOICES + v);
                if (!cr || !cr->isChord() || cr->isGrace()) {
                    continue;
                }
                const double durQn = cr->actualTicks().ticks()
                                     / static_cast<double>(Constants::DIVISION);
                for (const Note* n : toChord(cr)->notes()) {
                    if (!n->play() || !n->visible()) {
                        continue;
                    }
                    const int pp = n->ppitch();
                    segNotes.push_back({ pp, durQn });
                    if (pp < lowestPitch) {
                        lowestPitch = pp;
                    }
                }
            }
        }

        for (const auto& ni : segNotes) {
            KeyModeAnalyzer::PitchContext p;
            p.pitch          = ni.ppitch;
            p.durationWeight = ni.durationQn * decay * lookaheadMul;
            p.beatWeight     = bw;
            p.isBass         = (ni.ppitch == lowestPitch);
            ctx.push_back(p);
        }
    }
}

void resolveKeyAndMode(const mu::engraving::Score* sc,
                       const mu::engraving::Fraction& tick,
                       mu::engraving::staff_idx_t staffIdx,
                       const std::set<size_t>& excludeStaves,
                       int& outKeyFifths,
                       mu::composing::analysis::KeySigMode& outMode,
                       double& outConfidence,
                       const mu::composing::analysis::KeyModeAnalysisResult* prevResult,
                       double* outScore)
{
    using namespace mu::engraving;
    using namespace mu::composing::analysis;

    const KeySigEvent keySig = sc->staff(staffIdx)->keySigEvent(tick);
    const int keyFifths = static_cast<int>(keySig.concertKey());
    outKeyFifths = keyFifths;

    // ── Analyzer preferences ──────────────────────────────────────────────
    KeyModeAnalyzerPreferences prefs;
    {
        static muse::GlobalInject<mu::composing::IComposingAnalysisConfiguration> config;
        const auto* cfg = config.get().get();
        if (cfg) {
            // Diatonic
            prefs.modePriorIonian     = cfg->modePriorIonian();
            prefs.modePriorDorian     = cfg->modePriorDorian();
            prefs.modePriorPhrygian   = cfg->modePriorPhrygian();
            prefs.modePriorLydian     = cfg->modePriorLydian();
            prefs.modePriorMixolydian = cfg->modePriorMixolydian();
            prefs.modePriorAeolian    = cfg->modePriorAeolian();
            prefs.modePriorLocrian    = cfg->modePriorLocrian();
            // Melodic minor family
            prefs.modePriorMelodicMinor  = cfg->modePriorMelodicMinor();
            prefs.modePriorDorianB2      = cfg->modePriorDorianB2();
            prefs.modePriorLydianAugmented = cfg->modePriorLydianAugmented();
            prefs.modePriorLydianDominant  = cfg->modePriorLydianDominant();
            prefs.modePriorMixolydianB6  = cfg->modePriorMixolydianB6();
            prefs.modePriorAeolianB5     = cfg->modePriorAeolianB5();
            prefs.modePriorAltered       = cfg->modePriorAltered();
            // Harmonic minor family
            prefs.modePriorHarmonicMinor = cfg->modePriorHarmonicMinor();
            prefs.modePriorLocrianSharp6 = cfg->modePriorLocrianSharp6();
            prefs.modePriorIonianSharp5  = cfg->modePriorIonianSharp5();
            prefs.modePriorDorianSharp4  = cfg->modePriorDorianSharp4();
            prefs.modePriorPhrygianDominant = cfg->modePriorPhrygianDominant();
            prefs.modePriorLydianSharp2  = cfg->modePriorLydianSharp2();
            prefs.modePriorAlteredDomBB7 = cfg->modePriorAlteredDomBB7();
        }
    }

    // ── Declared mode from key signature ─────────────────────────────────
    std::optional<mu::composing::analysis::KeySigMode> declaredMode;
    {
        using EMode = mu::engraving::KeyMode;
        using AMode = mu::composing::analysis::KeySigMode;
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

    // ── Fixed lookback window ─────────────────────────────────────────────
    static constexpr int LOOKBACK_BEATS  = 16;
    static constexpr int INITIAL_LOOKAHEAD_BEATS = 8;

    const Fraction lookbackDuration = Fraction(LOOKBACK_BEATS, 4);
    const Fraction windowStart = (tick > lookbackDuration)
                                 ? tick - lookbackDuration
                                 : Fraction(0, 1);

    // ── Piece-start shortcut ──────────────────────────────────────────────
    if (prevResult == nullptr && declaredMode.has_value()
        && windowStart == Fraction(0, 1) && tick < lookbackDuration) {
        const int ionianTonic = ionianTonicPcFromFifths(keyFifths);
        const int tonicPc = (ionianTonic + keyModeTonicOffset(*declaredMode)) % 12;
        outMode       = *declaredMode;
        outConfidence = 0.5;
        // Use the relative-key hysteresis margin as the piece-start anchor score so
        // that the first analysis window must beat this threshold to override the
        // declared key.  Returning 0.0 made the anchor too weak: any analysis
        // score above 2.0 would immediately override the declared key.
        if (outScore) *outScore = prefs.relativeKeyHysteresisMargin;
        (void)tonicPc;
        return;
    }

    // ── Dynamic lookahead loop ────────────────────────────────────────────
    std::vector<KeyModeAnalyzer::PitchContext> ctx;
    std::vector<KeyModeAnalysisResult> modeResults;

    int lookaheadBeats = INITIAL_LOOKAHEAD_BEATS;
    while (true) {
        ctx.clear();
        const Fraction windowEnd = tick + Fraction(lookaheadBeats, 4);
        collectPitchContext(sc, tick, windowStart, windowEnd,
                            excludeStaves, prefs, ctx);

        modeResults = KeyModeAnalyzer::analyzeKeyMode(ctx, keyFifths,
                                                      prefs, declaredMode);

        const bool confident = !modeResults.empty()
            && modeResults.front().normalizedConfidence
               >= prefs.dynamicLookaheadConfidenceThreshold;
        const bool atMax = lookaheadBeats >= prefs.dynamicLookaheadMaxBeats;

        if (confident || atMax) {
            break;
        }
        lookaheadBeats += prefs.dynamicLookaheadStepBeats;
    }

    // Fall back to notated key signature only when pitch data is insufficient
    if (modeResults.empty() || distinctPitchClasses(ctx) < 3) {
        const mu::engraving::KeyMode mode = keySig.mode();
        using CKeyMode = mu::composing::analysis::KeySigMode;
        switch (mode) {
        case mu::engraving::KeyMode::MINOR:
        case mu::engraving::KeyMode::AEOLIAN:    outMode = CKeyMode::Aeolian;    break;
        case mu::engraving::KeyMode::DORIAN:     outMode = CKeyMode::Dorian;     break;
        case mu::engraving::KeyMode::PHRYGIAN:   outMode = CKeyMode::Phrygian;   break;
        case mu::engraving::KeyMode::LYDIAN:     outMode = CKeyMode::Lydian;     break;
        case mu::engraving::KeyMode::MIXOLYDIAN: outMode = CKeyMode::Mixolydian; break;
        case mu::engraving::KeyMode::LOCRIAN:    outMode = CKeyMode::Locrian;    break;
        default:                                 outMode = CKeyMode::Ionian;     break;
        }
        outConfidence = 0.0;
        if (outScore) *outScore = 0.0;
        return;
    }

    // ── Hysteresis ───────────────────────────────────────────────────────
    const KeyModeAnalysisResult& top = modeResults.front();
    if (prevResult != nullptr && top.mode != prevResult->mode) {
        const double hysteresis = (top.keySignatureFifths == prevResult->keySignatureFifths)
                                  ? prefs.relativeKeyHysteresisMargin
                                  : prefs.hysteresisMargin;
        if (top.score < prevResult->score + hysteresis) {
            const KeyModeAnalysisResult* incumbent = nullptr;
            for (const auto& r : modeResults) {
                if (r.mode == prevResult->mode
                    && r.keySignatureFifths == prevResult->keySignatureFifths) {
                    incumbent = &r;
                    break;
                }
            }
            if (incumbent) {
                outKeyFifths  = incumbent->keySignatureFifths;
                outMode       = incumbent->mode;
                outConfidence = incumbent->normalizedConfidence;
                if (outScore) *outScore = incumbent->score;
                return;
            }
        }
    }

    outKeyFifths  = top.keySignatureFifths;
    outMode       = top.mode;
    outConfidence = top.normalizedConfidence;
    if (outScore) *outScore = top.score;
}

std::vector<mu::composing::analysis::ChordAnalysisTone>
collectRegionTones(const mu::engraving::Score* sc,
                   int startTickInt,
                   int endTickInt,
                   const std::set<size_t>& excludeStaves)
{
    using namespace mu::engraving;
    using namespace mu::composing::analysis;

    if (!sc || endTickInt <= startTickInt) {
        return {};
    }

    const ChordAnalyzerPreferences& prefs = kDefaultChordAnalyzerPreferences;

    const Fraction startTick = Fraction::fromTicks(startTickInt);
    const Fraction endTick   = Fraction::fromTicks(endTickInt);
    const int regionDuration = endTickInt - startTickInt;

    // ── Inline beat-weight mapping ─────────────────────────────────────────
    // Uses fixed weights — avoids dependency on KeyModeAnalyzerPreferences.
    auto beatWeight = [](BeatType bt) -> double {
        switch (bt) {
        case BeatType::DOWNBEAT:            return 1.0;
        case BeatType::SIMPLE_STRESSED:
        case BeatType::COMPOUND_STRESSED:   return 0.85;
        case BeatType::SIMPLE_UNSTRESSED:
        case BeatType::COMPOUND_UNSTRESSED: return 0.75;
        default:                            return 0.5;  // SUBBEAT / COMPOUND_SUBBEAT
        }
    };

    // ── Per-pitch-class accumulator ────────────────────────────────────────
    struct PcAccum {
        double totalWeight      = 0.0;
        int    durationInRegion = 0;
        std::set<int> metricTicks;      // distinct attack ticks (one per segment)
        int lowestPitch = std::numeric_limits<int>::max();
        int tpc = -1;
    };
    PcAccum accum[12];

    // voiceCountAtTick[pc][segTick] = number of voices playing pc at that tick
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

    for (const auto& spannerEntry : sc->spanner()) {
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
        if (staffIdx >= sc->nstaves() || excludeStaves.count(staffIdx) || !staffIsEligible(sc, staffIdx, startTick)) {
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

    // ── Walk backward to catch notes sustained into the region ────────────────
    // Notes that attacked before startTick but are still sounding at startTick
    // must be included (e.g., a bass note held across a harmonic boundary).
    // Walk back up to 4 quarter notes, mirroring collectSoundingAt behaviour.
    const Fraction backLimit = startTick - Fraction(4, 1);

    // Get beat weight at the region start (used for sustained notes from before).
    auto bwAtRegionStart = [&]() -> double {
        const Measure* m0 = sc->tick2measure(startTick);
        if (!m0) { return 0.75; }
        const Segment* s0 = sc->tick2segment(startTick, true, SegmentType::ChordRest);
        if (!s0) { return 0.75; }
        return beatWeight(safeBeatType(m0, s0));
    }();

    const Segment* firstForward = sc->tick2segment(startTick, true, SegmentType::ChordRest);
    if (firstForward) {
        // Walk backward to collect sustained notes.
        for (const Segment* s = firstForward->prev1(SegmentType::ChordRest);
             s && s->tick() >= backLimit;
             s = s->prev1(SegmentType::ChordRest)) {
            const int segTickInt = s->tick().ticks();
            const Measure* m = s->measure();
            const double sustainBeatWeight = m ? beatWeight(safeBeatType(m, s)) : bwAtRegionStart;
            for (size_t si = 0; si < sc->nstaves(); ++si) {
                if (excludeStaves.count(si) || !staffIsEligible(sc, si, startTick)) {
                    continue;
                }
                for (int v = 0; v < VOICES; ++v) {
                    const ChordRest* cr
                        = s->cr(static_cast<track_idx_t>(si) * VOICES + v);
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

                        const int clippedEnd  = std::min(noteEnd, endTickInt);
                        const int durInRegion = clippedEnd - startTickInt;
                        if (durInRegion <= 0) {
                            continue;
                        }

                        const double baseWeight
                            = (static_cast<double>(durInRegion) / regionDuration) * bwAtRegionStart;
                        const int pc = n->ppitch() % 12;
                        PcAccum& a = accum[pc];
                        a.totalWeight    += baseWeight;
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

    // ── Forward walk: collect notes attacking within [startTick, endTick) ──────
    const Segment* seg = firstForward;
    if (!seg) {
        return {};
    }

    for (const Segment* s = seg;
         s && s->tick() < endTick;
         s = s->next1(SegmentType::ChordRest)) {
        const Measure* m = s->measure();
        if (!m) {
            continue;
        }

        const int segTickInt = s->tick().ticks();
        const BeatType bt = safeBeatType(m, s);
        const double bw = beatWeight(bt);

        for (size_t si = 0; si < sc->nstaves(); ++si) {
            if (excludeStaves.count(si) || !staffIsEligible(sc, si, s->tick())) {
                continue;
            }
            for (int v = 0; v < VOICES; ++v) {
                const ChordRest* cr
                    = s->cr(static_cast<track_idx_t>(si) * VOICES + v);
                if (!cr || !cr->isChord() || cr->isGrace()) {
                    continue;
                }

                // Clip note duration to the region boundary.
                const int noteEnd      = segTickInt + cr->actualTicks().ticks();
                const int clippedEnd   = std::min(noteEnd, endTickInt);
                const int durInRegion  = clippedEnd - segTickInt;
                if (durInRegion <= 0) {
                    continue;
                }

                const double baseWeight
                    = (static_cast<double>(durInRegion) / regionDuration) * bw;

                for (const Note* n : toChord(cr)->notes()) {
                    if (!n->play() || !n->visible()) {
                        continue;
                    }

                    recordPedalTailCandidate(si, noteEnd, bw, n);

                    const int pc = n->ppitch() % 12;
                    PcAccum& a = accum[pc];
                    a.totalWeight    += baseWeight;
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

    // ── Pass 2: repetition boost ───────────────────────────────────────────
    // Reward pitch classes that recur at multiple metric positions.
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

    // ── Pass 3: cross-voice boost ──────────────────────────────────────────
    // Reward pitch classes reinforced by multiple simultaneous voices.
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

    // ── Pass 4: discounted sustain-pedal tails ───────────────────────────
    // Add a smaller continuation weight after written note-off when an
    // explicit sustain pedal is still active on the same staff.
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

    // ── Normalize ──────────────────────────────────────────────────────────
    double totalWeight = 0.0;
    for (int pc = 0; pc < 12; ++pc) {
        totalWeight += accum[pc].totalWeight;
    }
    if (totalWeight == 0.0) {
        return {};
    }

    // Bass = lowest MIDI pitch among PCs with sufficient accumulated weight.
    // A PC whose weight is below bassPassingToneMinWeightFraction × totalWeight is
    // treated as a chromatic passing tone or ornament and skipped for bass selection.
    // Falls back to the absolute lowest pitch if no PC meets the threshold.
    const double bassMinWeight = totalWeight * prefs.bassPassingToneMinWeightFraction;
    int bassPitch = std::numeric_limits<int>::max();
    for (int pc = 0; pc < 12; ++pc) {
        if (accum[pc].totalWeight >= bassMinWeight && accum[pc].lowestPitch < bassPitch) {
            bassPitch = accum[pc].lowestPitch;
        }
    }
    // Fallback: if the threshold filtered everything (e.g. very sparse chord),
    // use the absolute lowest pitch.
    if (bassPitch == std::numeric_limits<int>::max()) {
        for (int pc = 0; pc < 12; ++pc) {
            if (accum[pc].totalWeight > 0.0 && accum[pc].lowestPitch < bassPitch) {
                bassPitch = accum[pc].lowestPitch;
            }
        }
    }
    const int bassPC = (bassPitch < std::numeric_limits<int>::max())
                       ? (bassPitch % 12) : -1;

    // ── Build tones ────────────────────────────────────────────────────────
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
        t.pitch                  = a.lowestPitch;
        t.tpc                    = a.tpc;
        t.weight                 = a.totalWeight / totalWeight;
        t.isBass                 = (pc == bassPC);
        t.durationInRegion       = a.durationInRegion;
        t.distinctMetricPositions = static_cast<int>(a.metricTicks.size());
        t.simultaneousVoiceCount = maxVoices;
        tones.push_back(t);
    }

    return tones;
}

std::vector<mu::engraving::Fraction>
detectHarmonicBoundariesJaccard(const mu::engraving::Score* sc,
                                const mu::engraving::Fraction& startTick,
                                const mu::engraving::Fraction& endTick,
                                const std::set<size_t>& excludeStaves,
                                double jaccardThreshold)
{
    using namespace mu::engraving;

    // Portable 16-bit popcount (avoids MSVC vs GCC intrinsic divergence).
    auto popcount16 = [](uint16_t x) -> int {
        int n = 0;
        while (x) { n += x & 1; x >>= 1; }
        return n;
    };

    // ── Collect per-window PC bitsets ──────────────────────────────────────
    // Window size = 1 quarter note (Constants::DIVISION ticks).
    // Each window collects pitch classes that attack within it, plus any
    // explicit sustain-pedal tails that keep those pitch classes sounding
    // into later windows on the same staff.
    struct Window {
        Fraction tick;
        uint16_t bits = 0;
    };
    std::vector<Window> windows;

    const Segment* firstForward = sc->tick2segment(startTick, true, SegmentType::ChordRest);
    if (!firstForward) {
        return { startTick };
    }

    const int startTickInt = startTick.ticks();
    const int endTickInt = endTick.ticks();
    const int windowTicks = Constants::DIVISION;  // 1 quarter note

    struct PedalWindow {
        int startTick = 0;
        int endTick = 0;
    };

    std::map<size_t, std::vector<PedalWindow> > pedalWindowsByStaff;
    for (const auto& spannerEntry : sc->spanner()) {
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
        if (staffIdx >= sc->nstaves() || excludeStaves.count(staffIdx) || !staffIsEligible(sc, staffIdx, startTick)) {
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
    for (const Segment* s = firstForward->prev1(SegmentType::ChordRest);
         s && s->tick() >= backLimit;
         s = s->prev1(SegmentType::ChordRest)) {
        const int segTick = s->tick().ticks();

        for (size_t si = 0; si < sc->nstaves(); ++si) {
            if (excludeStaves.count(si) || !staffIsEligible(sc, si, s->tick())) {
                continue;
            }
            for (int v = 0; v < VOICES; ++v) {
                const ChordRest* cr
                    = s->cr(static_cast<track_idx_t>(si) * VOICES + v);
                if (!cr || !cr->isChord() || cr->isGrace()) {
                    continue;
                }
                for (const Note* n : toChord(cr)->notes()) {
                    if (!n->play() || !n->visible()) {
                        continue;
                    }
                    const int noteEndTick = segTick + cr->actualTicks().ticks();
                    recordPedalTailSpan(si, noteEndTick, n);
                }
            }
        }
    }

    for (const Segment* s = firstForward;
         s && s->tick() < endTick;
         s = s->next1(SegmentType::ChordRest)) {
        const int segTick = s->tick().ticks();
        const int segWindowTick = (segTick / windowTicks) * windowTicks;

        for (size_t si = 0; si < sc->nstaves(); ++si) {
            if (excludeStaves.count(si) || !staffIsEligible(sc, si, s->tick())) {
                continue;
            }
            for (int v = 0; v < VOICES; ++v) {
                const ChordRest* cr
                    = s->cr(static_cast<track_idx_t>(si) * VOICES + v);
                if (!cr || !cr->isChord() || cr->isGrace()) {
                    continue;
                }
                const int noteEndTick = segTick + cr->actualTicks().ticks();
                for (const Note* n : toChord(cr)->notes()) {
                    if (!n->play() || !n->visible()) {
                        continue;
                    }

                    bitsByWindowTick[segWindowTick] |= static_cast<uint16_t>(1u << (n->ppitch() % 12));
                    recordPedalTailSpan(si, noteEndTick, n);
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

    // ── Compute Jaccard between consecutive windows ────────────────────────
    std::vector<Fraction> boundaries;
    boundaries.push_back(startTick);

    uint16_t prevBits = windows[0].bits;
    for (size_t i = 1; i < windows.size(); ++i) {
        const uint16_t bits     = windows[i].bits;
        const uint16_t inter    = prevBits & bits;
        const uint16_t uni      = prevBits | bits;
        const int interCount    = popcount16(inter);
        const int uniCount      = popcount16(uni);
        const double jaccard    = (uniCount > 0)
                                  ? (1.0 - static_cast<double>(interCount) / uniCount)
                                  : 0.0;

        if (jaccard >= jaccardThreshold) {
            boundaries.push_back(windows[i].tick);
            prevBits = bits;
        } else {
            // Accumulate into the running "previous" set — non-boundary windows
            // merge so that gradual harmonic changes are compared holistically.
            prevBits = uni;
        }
    }

    return boundaries;
}

// ── detectOnsetSubBoundaries ─────────────────────────────────────────────────
// Pass 2: within a coarse Jaccard region, scan for sub-boundaries using
// onset-only pitch class sets.  An onset-only set contains only pitch classes
// whose start tick falls exactly at the current segment tick — no sustained
// notes, no arpeggiated leftovers.  Because onset sets are small and clean,
// a low threshold (default 0.25) catches genuine chord changes that sustained
// windows blur together.
std::vector<mu::engraving::Fraction>
detectOnsetSubBoundaries(const mu::engraving::Score* sc,
                         const mu::engraving::Fraction& startTick,
                         const mu::engraving::Fraction& endTick,
                         const std::set<size_t>& excludeStaves,
                         double threshold)
{
    using namespace mu::engraving;

    auto popcount16 = [](uint16_t x) -> int {
        int n = 0;
        while (x) { n += x & 1; x >>= 1; }
        return n;
    };

    std::vector<Fraction> subBoundaries;

    const Segment* firstSeg = sc->tick2segment(startTick, true, SegmentType::ChordRest);
    if (!firstSeg) {
        return subBoundaries;
    }

    // Build onset-only bitset at each ChordRest segment tick.
    struct OnsetWindow {
        Fraction tick;
        uint16_t bits = 0;
    };
    std::vector<OnsetWindow> onsets;

    for (const Segment* s = firstSeg;
         s && s->tick() < endTick;
         s = s->next1(SegmentType::ChordRest)) {

        uint16_t bits = 0;
        const int segTick = s->tick().ticks();

        for (size_t si = 0; si < sc->nstaves(); ++si) {
            if (excludeStaves.count(si) || !staffIsEligible(sc, si, s->tick())) {
                continue;
            }
            for (int v = 0; v < VOICES; ++v) {
                const ChordRest* cr = s->cr(static_cast<track_idx_t>(si) * VOICES + v);
                if (!cr || !cr->isChord() || cr->isGrace()) {
                    continue;
                }
                // Onset-only: only notes whose start tick equals this segment tick.
                if (cr->tick().ticks() != segTick) {
                    continue;
                }
                for (const Note* n : toChord(cr)->notes()) {
                    if (!n->play() || !n->visible()) {
                        continue;
                    }
                    bits |= static_cast<uint16_t>(1u << (n->ppitch() % 12));
                }
            }
        }

        if (bits != 0) {
            onsets.push_back({ s->tick(), bits });
        }
    }

    if (onsets.size() < 2) {
        return subBoundaries;
    }

    // Minimum gap between sub-boundaries: 2 quarter notes (half note).
    // This prevents threshold=0.25 from inserting boundaries at every beat in
    // arpeggiated passages.  The main loop calls resolveKeyAndMode per region,
    // so too many sub-boundaries cause quadratic slowdown on long scores.
    const int minGapTicks = 2 * Constants::DIVISION;

    // Compare each onset set to the previous boundary's onset set; insert a sub-boundary
    // when the Jaccard distance exceeds the threshold AND the gap since the last accepted
    // boundary is at least one quarter note.
    uint16_t prevBits = onsets[0].bits;
    Fraction lastBoundaryTick = startTick;

    for (size_t i = 1; i < onsets.size(); ++i) {
        const uint16_t bits     = onsets[i].bits;
        const uint16_t inter    = prevBits & bits;
        const uint16_t uni      = prevBits | bits;
        const int interCount    = popcount16(inter);
        const int uniCount      = popcount16(uni);
        const double jaccard    = (uniCount > 0)
                                  ? (1.0 - static_cast<double>(interCount) / uniCount)
                                  : 0.0;

        const int gapTicks = (onsets[i].tick - lastBoundaryTick).ticks();
        if (jaccard >= threshold && gapTicks >= minGapTicks) {
            subBoundaries.push_back(onsets[i].tick);
            lastBoundaryTick = onsets[i].tick;
            prevBits = bits;
        }
        // No accumulation for Pass 2 — each onset is a fresh snapshot.
    }

    return subBoundaries;
}

mu::composing::analysis::ChordTemporalContext
findTemporalContext(const mu::engraving::Score* sc,
                    const mu::engraving::Segment* seg,
                    const std::set<size_t>& excludeStaves,
                    int keyFifths,
                    mu::composing::analysis::KeySigMode keyMode,
                    int currentBassPc)
{
    using namespace mu::engraving;
    using namespace mu::composing::analysis;

    ChordTemporalContext temporalCtx;
    const Fraction tick = seg->tick();
    const auto chordAnalyzer = ChordAnalyzerFactory::create();

    for (const Segment* s = seg->prev1(SegmentType::ChordRest);
         s != nullptr;
         s = s->prev1(SegmentType::ChordRest)) {
        bool hasAttacks = false;
        for (size_t si = 0; si < sc->nstaves() && !hasAttacks; ++si) {
            if (excludeStaves.count(si) || !staffIsEligible(sc, si, tick)) {
                continue;
            }
            for (int v = 0; v < VOICES && !hasAttacks; ++v) {
                const ChordRest* cr
                    = s->cr(static_cast<track_idx_t>(si) * VOICES + v);
                if (cr && cr->isChord() && !cr->isGrace()) {
                    hasAttacks = true;
                }
            }
        }
        if (!hasAttacks) {
            continue;
        }

        std::vector<SoundingNote> prevSounding;
        collectSoundingAt(sc, s, excludeStaves, prevSounding);
        if (!prevSounding.empty()) {
            const auto prevTones = buildTones(prevSounding);
            const auto prevResults =
                chordAnalyzer->analyzeChord(prevTones, keyFifths, keyMode);
            if (!prevResults.empty()) {
                temporalCtx.previousRootPc  = prevResults.front().identity.rootPc;
                temporalCtx.previousQuality = prevResults.front().identity.quality;
                temporalCtx.previousBassPc  = prevResults.front().identity.bassPc;
            }
        }
        break;
    }

    // Stepwise bass motion detection (§4.1b).
    if (currentBassPc != -1 && temporalCtx.previousBassPc != -1) {
        temporalCtx.bassIsStepwiseFromPrevious =
            isDiatonicStep(temporalCtx.previousBassPc, currentBassPc);
    }

    // nextRootPc, nextBassPc, bassIsStepwiseToNext: populated in
    // two-pass chord staff analysis only. Deferred — see §4.1b.

    return temporalCtx;
}

std::vector<mu::composing::analysis::HarmonicRegion>
prepareUserFacingHarmonicRegions(const mu::engraving::Score* sc,
                                 const mu::engraving::Fraction& startTick,
                                 const mu::engraving::Fraction& endTick,
                                 const std::set<size_t>& excludeStaves)
{
    using namespace mu::engraving;
    using namespace mu::composing::analysis;

    if (!sc || endTick <= startTick) {
        return {};
    }

    auto regions = mu::notation::analyzeHarmonicRhythm(sc,
                                                       startTick,
                                                       endTick,
                                                       excludeStaves,
                                                       mu::notation::HarmonicRegionGranularity::Smoothed);
    if (regions.empty()) {
        return {};
    }

    const auto chordAnalyzer = ChordAnalyzerFactory::create();
    auto sameChordIdentity = [](const HarmonicRegion& lhs, const HarmonicRegion& rhs) {
        return lhs.chordResult.identity.rootPc == rhs.chordResult.identity.rootPc
               && lhs.chordResult.identity.quality == rhs.chordResult.identity.quality;
    };
    auto regionSupportsGapTones = [](const std::vector<ChordAnalysisTone>& gapTones,
                                     const HarmonicRegion& region) {
        if (region.chordResult.identity.quality == ChordQuality::Suspended2
            || region.chordResult.identity.quality == ChordQuality::Suspended4) {
            return false;
        }

        const std::vector<int> chordPitchClasses = chordTonePitchClasses(region.chordResult);
        if (gapTones.empty() || chordPitchClasses.empty()) {
            return false;
        }

        bool seenGapPitchClasses[12] = {};
        bool matchesRegionAnchor = false;
        for (const auto& tone : gapTones) {
            const int pitchClass = tone.pitch % 12;
            if (seenGapPitchClasses[pitchClass]) {
                continue;
            }
            seenGapPitchClasses[pitchClass] = true;

            if (pitchClass == region.chordResult.identity.rootPc
                || pitchClass == region.chordResult.identity.bassPc) {
                matchesRegionAnchor = true;
            }

            if (std::find(chordPitchClasses.begin(), chordPitchClasses.end(), pitchClass) == chordPitchClasses.end()) {
                return false;
            }
        }

        return matchesRegionAnchor;
    };
    auto applyGapKeyContext = [](ChordAnalysisResult& result,
                                 const std::vector<ChordAnalysisTone>& gapTones,
                                 int keyFifths,
                                 KeySigMode keyMode) {
        const int ionianTonicPc = ionianTonicPcFromFifths(keyFifths);
        const int tonicPc = (ionianTonicPc + keyModeTonicOffset(keyMode)) % 12;
        const auto& scale = keyModeScaleIntervals(keyMode);

        result.function.keyTonicPc = tonicPc;
        result.function.keyMode = keyMode;
        result.function.degree = -1;
        for (size_t degree = 0; degree < scale.size(); ++degree) {
            if ((tonicPc + scale[degree]) % 12 == result.identity.rootPc) {
                result.function.degree = static_cast<int>(degree);
                break;
            }
        }

        bool diatonicToKey = (result.function.degree >= 0);
        if (diatonicToKey) {
            for (const auto& tone : gapTones) {
                const int pitchClass = tone.pitch % 12;
                bool inScale = false;
                for (int interval : scale) {
                    if ((tonicPc + interval) % 12 == pitchClass) {
                        inScale = true;
                        break;
                    }
                }
                if (!inScale) {
                    diatonicToKey = false;
                    break;
                }
            }
        }

        result.function.diatonicToKey = diatonicToKey;
    };
    auto inferSparseGapChord = [&](const std::vector<ChordAnalysisTone>& gapTones,
                                   int keyFifths,
                                   KeySigMode keyMode,
                                   ChordAnalysisResult& outResult) {
        const auto* bassTone = bassToneFromTones(gapTones);
        if (!bassTone) {
            bassTone = &gapTones.front();
            for (const auto& tone : gapTones) {
                if (tone.pitch < bassTone->pitch) {
                    bassTone = &tone;
                }
            }
        }

        bool seenPitchClasses[12] = {};
        std::vector<int> pitchClasses;
        pitchClasses.reserve(gapTones.size());
        for (const auto& tone : gapTones) {
            const int pitchClass = tone.pitch % 12;
            if (!seenPitchClasses[pitchClass]) {
                seenPitchClasses[pitchClass] = true;
                pitchClasses.push_back(pitchClass);
            }
        }

        if (pitchClasses.empty()) {
            return false;
        }

        outResult = {};
        outResult.identity.score = 0.0;

        if (pitchClasses.size() == 1) {
            outResult.identity.rootPc = pitchClasses.front();
            outResult.identity.bassPc = pitchClasses.front();
            outResult.identity.bassTpc = bassTone->tpc;
            outResult.identity.quality = ChordQuality::Unknown;
            applyGapKeyContext(outResult, gapTones, keyFifths, keyMode);
            return true;
        }

        struct SparseCandidate {
            int rootPc = -1;
            ChordQuality quality = ChordQuality::Unknown;
            int priority = -1;
        };

        std::optional<SparseCandidate> bestCandidate;
        for (int candidateRootPc : pitchClasses) {
            bool hasMinorThird = false;
            bool hasMajorThird = false;
            bool hasFifth = false;
            bool hasDimFifth = false;
            bool supported = true;

            for (int tonePc : pitchClasses) {
                if (tonePc == candidateRootPc) {
                    continue;
                }

                const int interval = (tonePc - candidateRootPc + 12) % 12;
                if (interval == 3) {
                    hasMinorThird = true;
                } else if (interval == 4) {
                    hasMajorThird = true;
                } else if (interval == 6) {
                    hasDimFifth = true;
                } else if (interval == 7) {
                    hasFifth = true;
                } else {
                    supported = false;
                    break;
                }
            }

            if (!supported) {
                continue;
            }

            SparseCandidate candidate;
            candidate.rootPc = candidateRootPc;
            if (hasMajorThird) {
                candidate.quality = ChordQuality::Major;
                candidate.priority = 3;
            } else if (hasMinorThird) {
                candidate.quality = ChordQuality::Minor;
                candidate.priority = 3;
            } else if (hasDimFifth) {
                candidate.quality = ChordQuality::Diminished;
                candidate.priority = 2;
            } else if (hasFifth) {
                candidate.quality = ChordQuality::Unknown;
                candidate.priority = 1;
            } else {
                continue;
            }

            if (!bestCandidate || candidate.priority > bestCandidate->priority) {
                bestCandidate = candidate;
            }
        }

        if (bestCandidate) {
            outResult.identity.rootPc = bestCandidate->rootPc;
            outResult.identity.bassPc = bestCandidate->rootPc;
            outResult.identity.bassTpc = bassTone->tpc;
            outResult.identity.quality = bestCandidate->quality;
            applyGapKeyContext(outResult, gapTones, keyFifths, keyMode);
            return true;
        }

        return false;
    };
    auto analyzeGapWithContext = [&](const std::vector<ChordAnalysisTone>& gapTones,
                                     const HarmonicRegion& contextRegion,
                                     int gapStartTick,
                                     int gapEndTick) -> std::optional<HarmonicRegion> {
        HarmonicRegion inferredRegion;
        inferredRegion.startTick = gapStartTick;
        inferredRegion.endTick = gapEndTick;
        inferredRegion.hasAnalyzedChord = true;
        inferredRegion.keyModeResult = contextRegion.keyModeResult;
        inferredRegion.tones = gapTones;

        const auto results = chordAnalyzer->analyzeChord(gapTones,
                                                         contextRegion.keyModeResult.keySignatureFifths,
                                                         contextRegion.keyModeResult.mode);
        if (!results.empty()) {
            inferredRegion.chordResult = results.front();
            return inferredRegion;
        }

        if (inferSparseGapChord(gapTones,
                                contextRegion.keyModeResult.keySignatureFifths,
                                contextRegion.keyModeResult.mode,
                                inferredRegion.chordResult)) {
            return inferredRegion;
        }

        return std::nullopt;
    };
    auto inferGapRegion = [&](int gapStartTick,
                              int gapEndTick,
                              const HarmonicRegion* previousRegion,
                              const HarmonicRegion* nextRegion) -> std::optional<HarmonicRegion> {
        if (gapEndTick <= gapStartTick) {
            return std::nullopt;
        }

        const auto gapTones = collectRegionTones(sc,
                                                 gapStartTick,
                                                 gapEndTick,
                                                 excludeStaves);
        if (gapTones.empty()) {
            const HarmonicRegion* carriedSource = previousRegion ? previousRegion : nextRegion;
            if (!carriedSource) {
                return std::nullopt;
            }

            HarmonicRegion carriedRegion = *carriedSource;
            carriedRegion.startTick = gapStartTick;
            carriedRegion.endTick = gapEndTick;
            carriedRegion.tones.clear();
            carriedRegion.hasAnalyzedChord = true;
            return carriedRegion;
        }

        auto carryGapRegion = [&](const HarmonicRegion& sourceRegion) {
            HarmonicRegion carriedRegion = sourceRegion;
            carriedRegion.startTick = gapStartTick;
            carriedRegion.endTick = gapEndTick;
            carriedRegion.tones = gapTones;
            carriedRegion.hasAnalyzedChord = true;
            return carriedRegion;
        };

        int uniqueGapPitchClasses = 0;
        bool seenGapPitchClasses[12] = {};
        for (const auto& tone : gapTones) {
            const int pitchClass = tone.pitch % 12;
            if (seenGapPitchClasses[pitchClass]) {
                continue;
            }
            seenGapPitchClasses[pitchClass] = true;
            ++uniqueGapPitchClasses;
        }

        if (uniqueGapPitchClasses < 3) {
            if (nextRegion && regionSupportsGapTones(gapTones, *nextRegion)) {
                return carryGapRegion(*nextRegion);
            }

            if (previousRegion && regionSupportsGapTones(gapTones, *previousRegion)) {
                return carryGapRegion(*previousRegion);
            }
        }

        if (previousRegion) {
            if (auto analyzedRegion = analyzeGapWithContext(gapTones,
                                                            *previousRegion,
                                                            gapStartTick,
                                                            gapEndTick)) {
                return analyzedRegion;
            }
        }

        if (nextRegion) {
            if (auto analyzedRegion = analyzeGapWithContext(gapTones,
                                                            *nextRegion,
                                                            gapStartTick,
                                                            gapEndTick)) {
                return analyzedRegion;
            }
        }

        if (previousRegion && regionSupportsGapTones(gapTones, *previousRegion)) {
            return carryGapRegion(*previousRegion);
        }

        if (nextRegion && regionSupportsGapTones(gapTones, *nextRegion)) {
            return carryGapRegion(*nextRegion);
        }

        if (!previousRegion && nextRegion) {
            HarmonicRegion openingRegion = *nextRegion;
            openingRegion.startTick = gapStartTick;
            openingRegion.endTick = gapEndTick;
            openingRegion.tones = gapTones;
            openingRegion.hasAnalyzedChord = true;
            return openingRegion;
        }

        if (previousRegion && !nextRegion) {
            HarmonicRegion trailingRegion = *previousRegion;
            trailingRegion.startTick = gapStartTick;
            trailingRegion.endTick = gapEndTick;
            trailingRegion.tones = gapTones;
            trailingRegion.hasAnalyzedChord = true;
            return trailingRegion;
        }

        return std::nullopt;
    };
    auto nextRegionStartingAtOrAfter = [&](int tick) -> const HarmonicRegion* {
        const auto nextRegion = std::find_if(regions.begin(), regions.end(), [tick](const auto& region) {
            return region.startTick >= tick;
        });
        return nextRegion != regions.end() ? &*nextRegion : nullptr;
    };

    std::vector<HarmonicRegion> displayRegions;
    displayRegions.reserve(regions.size() * 2);
    const int analysisRangeStartTick = startTick.ticks();

    for (Measure* measure = sc->tick2measure(startTick);
         measure && measure->tick() < endTick;
         measure = measure->nextMeasure()) {
        const Fraction measureRangeStart = std::max(measure->tick(), startTick);
        const Fraction measureRangeEnd = std::min(measure->endTick(), endTick);
        const int measureStartTick = measureRangeStart.ticks();
        const int measureEndTick = measureRangeEnd.ticks();

        std::vector<size_t> overlappingRegions;
        for (size_t i = 0; i < regions.size(); ++i) {
            if (regions[i].endTick > measureStartTick && regions[i].startTick < measureEndTick) {
                overlappingRegions.push_back(i);
            }
        }

        std::vector<HarmonicRegion> measureRegions;
        auto appendMeasureRegion = [&](HarmonicRegion region) {
            if (region.startTick >= region.endTick) {
                return;
            }
            if (!measureRegions.empty()
                && measureRegions.back().endTick == region.startTick
                && sameChordIdentity(measureRegions.back(), region)) {
                measureRegions.back().endTick = region.endTick;
                mergeChordAnalysisTones(measureRegions.back().tones, region.tones);
                return;
            }
            measureRegions.push_back(std::move(region));
        };

        const auto previousRegion = std::find_if(regions.rbegin(), regions.rend(), [measureStartTick](const auto& region) {
            return region.endTick <= measureStartTick;
        });
        const HarmonicRegion* previousRegionPtr = previousRegion != regions.rend() ? &*previousRegion : nullptr;
        const HarmonicRegion* nextRegionAfterMeasurePtr = nextRegionStartingAtOrAfter(measureEndTick);

        if (overlappingRegions.empty()) {
            if (auto gapRegion = inferGapRegion(measureStartTick,
                                                measureEndTick,
                                                previousRegionPtr,
                                                nextRegionAfterMeasurePtr)) {
                appendMeasureRegion(std::move(*gapRegion));
            }

            for (auto& measureRegion : measureRegions) {
                displayRegions.push_back(std::move(measureRegion));
            }
            continue;
        }

        std::optional<HarmonicRegion> previousDisplayRegion;
        if (previousRegionPtr) {
            previousDisplayRegion = *previousRegionPtr;
        }

        int cursor = measureStartTick;

        for (size_t i = 0; i < overlappingRegions.size(); ++i) {
            const auto& sourceRegion = regions[overlappingRegions[i]];
            const int sourceStartTick = std::max(measureStartTick, sourceRegion.startTick);
            const int sourceEndTick = std::min(measureEndTick, sourceRegion.endTick);

            if (cursor < sourceStartTick) {
                if (measureRegions.empty() && cursor == analysisRangeStartTick) {
                    HarmonicRegion openingRegion = sourceRegion;
                    openingRegion.startTick = cursor;
                    openingRegion.endTick = sourceStartTick;
                    openingRegion.tones = collectRegionTones(sc,
                                                             openingRegion.startTick,
                                                             openingRegion.endTick,
                                                             excludeStaves);
                    appendMeasureRegion(std::move(openingRegion));
                } else if (auto gapRegion = inferGapRegion(cursor,
                                                           sourceStartTick,
                                                           previousDisplayRegion ? &*previousDisplayRegion : previousRegionPtr,
                                                           &sourceRegion)) {
                    appendMeasureRegion(std::move(*gapRegion));
                }

                if (!measureRegions.empty()) {
                    previousDisplayRegion = measureRegions.back();
                }
            }

            if (sourceStartTick >= sourceEndTick) {
                cursor = std::max(cursor, sourceEndTick);
                continue;
            }

            HarmonicRegion displayRegion = sourceRegion;
            displayRegion.startTick = sourceStartTick;
            displayRegion.endTick = sourceEndTick;
            displayRegion.tones = collectRegionTones(sc,
                                                     displayRegion.startTick,
                                                     displayRegion.endTick,
                                                     excludeStaves);
            appendMeasureRegion(std::move(displayRegion));
            previousDisplayRegion = measureRegions.back();
            cursor = sourceEndTick;
        }

        if (cursor < measureEndTick) {
            if (auto gapRegion = inferGapRegion(cursor,
                                                measureEndTick,
                                                previousDisplayRegion ? &*previousDisplayRegion : previousRegionPtr,
                                                nextRegionAfterMeasurePtr)) {
                appendMeasureRegion(std::move(*gapRegion));
            }
        }

        if (measureRegions.size() >= 2
            && measureRegions.front().startTick == measureStartTick
            && distinctPitchClassCount(measureRegions.front().tones) < 3
            && distinctPitchClassCount(measureRegions[1].tones) >= 3
            && measureRegions[1].startTick - measureStartTick <= Constants::DIVISION) {
            HarmonicRegion carriedMeasureOpening = measureRegions[1];
            carriedMeasureOpening.startTick = measureStartTick;
            carriedMeasureOpening.tones = collectRegionTones(sc,
                                                             carriedMeasureOpening.startTick,
                                                             carriedMeasureOpening.endTick,
                                                             excludeStaves);
            measureRegions[0] = std::move(carriedMeasureOpening);
            measureRegions.erase(measureRegions.begin() + 1);
        }

        for (auto& measureRegion : measureRegions) {
            displayRegions.push_back(std::move(measureRegion));
        }
    }

    stabilizeHarmonicRegionsForDisplay(displayRegions);
    return displayRegions;
}

// ── §4.1c Jazz mode — chord-symbol boundary helpers ─────────────────────────

static bool isStandardChordSymbol(const mu::engraving::EngravingItem* annotation)
{
    using namespace mu::engraving;
    if (!annotation || !annotation->isHarmony()) {
        return false;
    }

    const Harmony* harmony = toHarmony(annotation);
    return harmony->harmonyType() == HarmonyType::STANDARD
           && harmony->rootTpc() != Tpc::TPC_INVALID;
}

static bool annotationIsOnExcludedStaff(const mu::engraving::EngravingItem* annotation,
                                        const std::set<size_t>& excludeStaves)
{
    if (!annotation) {
        return false;
    }

    return excludeStaves.count(static_cast<size_t>(annotation->track() / mu::engraving::VOICES)) > 0;
}

bool scoreHasValidChordSymbols(const mu::engraving::Score* score,
                               const mu::engraving::Fraction& startTick,
                               const mu::engraving::Fraction& endTick,
                               const std::set<size_t>& excludeStaves)
{
    using namespace mu::engraving;
    for (const Segment* s = score->tick2segment(startTick, true, SegmentType::ChordRest);
         s && s->tick() < endTick;
         s = s->next1(SegmentType::ChordRest)) {
        for (const EngravingItem* ann : s->annotations()) {
            if (annotationIsOnExcludedStaff(ann, excludeStaves)) {
                continue;
            }
            if (isStandardChordSymbol(ann)) return true;
        }
    }
    return false;
}

std::vector<mu::engraving::Fraction>
collectChordSymbolBoundaries(const mu::engraving::Score* score,
                             const mu::engraving::Fraction& startTick,
                             const mu::engraving::Fraction& endTick,
                             const std::set<size_t>& excludeStaves)
{
    using namespace mu::engraving;
    std::vector<Fraction> ticks;
    ticks.push_back(startTick);
    for (const Segment* s = score->tick2segment(startTick, true, SegmentType::ChordRest);
         s && s->tick() < endTick;
         s = s->next1(SegmentType::ChordRest)) {
        for (const EngravingItem* ann : s->annotations()) {
            if (annotationIsOnExcludedStaff(ann, excludeStaves)) {
                continue;
            }
            if (s->tick() > startTick && isStandardChordSymbol(ann)) {
                ticks.push_back(s->tick());
                break;  // one boundary per segment tick
            }
        }
    }
    return ticks;  // already sorted (segment iteration is tick-ordered)
}

// ── Cadence and pivot detection ───────────────────────────────────────────────

bool hasAssertiveKeyConfidence(
    const mu::composing::analysis::KeyModeAnalysisResult& kmr)
{
    return kmr.normalizedConfidence >= kAnnotateKeyConfidenceThreshold;
}

std::vector<CadenceMarker> detectCadences(
    const std::vector<mu::composing::analysis::HarmonicRegion>& regions,
    size_t selectionCount)
{
    using namespace mu::composing::analysis;

    std::vector<CadenceMarker> markers;

    const size_t total = regions.size();
    if (total == 0 || selectionCount == 0) {
        return markers;
    }

    // Clamp: selectionCount may equal total (no lookahead), that is fine.
    const size_t n = std::min(selectionCount, total);

    // ── PAC / PC / DC ───────────────────────────────────────────────────────
    // Examine consecutive pairs (i, i+1) where i is inside the selection.
    for (size_t i = 0; i + 1 < total && i < n; ++i) {
        if (!hasAssertiveKeyConfidence(regions[i].keyModeResult)
            || !hasAssertiveKeyConfidence(regions[i + 1].keyModeResult)) {
            continue;
        }

        const auto& a = regions[i].chordResult;
        const auto& b = regions[i + 1].chordResult;

        // Cadence requires same key / mode context.
        if (regions[i].keyModeResult.keySignatureFifths
            != regions[i + 1].keyModeResult.keySignatureFifths
            || regions[i].keyModeResult.mode
               != regions[i + 1].keyModeResult.mode) {
            continue;  // key change — not a cadence
        }
        // And different chord roots.
        if (a.identity.rootPc == b.identity.rootPc) {
            continue;
        }

        const char* label = nullptr;

        // PAC: V → I (non-minor dominant) or viio → I (leading-tone diminished).
        if (b.function.degree == 0
            && ((a.function.degree == 4 && a.identity.quality != ChordQuality::Minor)
                || (a.function.degree == 6 && a.identity.quality == ChordQuality::Diminished))) {
            label = "PAC";
        } else if (a.function.degree == 3 && b.function.degree == 0) {
            label = "PC";   // Plagal: IV → I
        } else if (a.function.degree == 4 && b.function.degree == 5
                   && a.identity.quality != ChordQuality::Minor
                   && b.identity.quality == ChordQuality::Minor) {
            label = "DC";   // Deceptive: V → vi
        }

        if (!label) {
            continue;
        }

        // Place the label at the resolution chord tick (b / regions[i+1]).
        // If that chord is in the lookahead region (outside the selection)
        // place it at the preparatory chord instead so the annotation stays
        // within the selection boundary.
        const int writeTick = (i + 1 < n)
            ? regions[i + 1].startTick
            : regions[i].startTick;

        markers.push_back({ writeTick, std::string(label) });
    }

    // ── Half cadence ────────────────────────────────────────────────────────
    // Last in-selection region is degree 4 (dominant arrival).
    if (hasAssertiveKeyConfidence(regions[n - 1].keyModeResult)
        && regions[n - 1].chordResult.function.degree == 4) {
        const int hcTick = regions[n - 1].startTick;
        // Do not emit HC if another cadence label already occupies this tick.
        const bool alreadyLabelled = std::any_of(markers.begin(), markers.end(),
            [hcTick](const CadenceMarker& m) { return m.tick == hcTick; });
        if (!alreadyLabelled) {
            markers.push_back({ hcTick, "HC" });
        }
    }

    return markers;
}

std::vector<PivotLabel> detectPivotChords(
    const std::vector<mu::composing::analysis::HarmonicRegion>& regions,
    size_t selectionCount)
{
    using namespace mu::composing::analysis;

    std::vector<PivotLabel> labels;

    if (regions.empty() || selectionCount == 0) {
        return labels;
    }

    const size_t total = regions.size();
    const size_t n = std::min(selectionCount, total);

    // Walk all regions (including lookahead) to find assertive key transitions.
    // A transition occurs when consecutive assertive regions disagree on key/mode.
    struct KeyTransition {
        size_t boundaryIdx;  // index of first region in the new (incoming) key
        int oldFifths;
        KeySigMode oldMode;
        int newFifths;
        KeySigMode newMode;
    };

    std::vector<KeyTransition> transitions;
    int prevFifths  = std::numeric_limits<int>::min();
    KeySigMode prevMode = KeySigMode::Ionian;

    for (size_t i = 0; i < total; ++i) {
        const auto& km = regions[i].keyModeResult;
        if (!hasAssertiveKeyConfidence(km)) {
            continue;
        }
        if (prevFifths == std::numeric_limits<int>::min()) {
            // First assertive region establishes the baseline key.
            prevFifths = km.keySignatureFifths;
            prevMode   = km.mode;
            continue;
        }
        if (km.keySignatureFifths != prevFifths || km.mode != prevMode) {
            // Key has changed — record the transition.
            transitions.push_back({ i, prevFifths, prevMode,
                                     km.keySignatureFifths, km.mode });
            prevFifths = km.keySignatureFifths;
            prevMode   = km.mode;
        }
    }

    for (const auto& tr : transitions) {
        // Confirm that the new key is stable by finding at least one more
        // assertive region beyond the boundary that agrees with it.
        // Limit the search to kMaxPivotLookaheadRegions past the boundary.
        bool confirmed = false;
        const size_t searchEnd = std::min(tr.boundaryIdx + 1
                                          + static_cast<size_t>(kMaxPivotLookaheadRegions),
                                          total);
        for (size_t k = tr.boundaryIdx + 1; k < searchEnd; ++k) {
            const auto& km = regions[k].keyModeResult;
            if (hasAssertiveKeyConfidence(km)
                && km.keySignatureFifths == tr.newFifths
                && km.mode == tr.newMode) {
                confirmed = true;
                break;
            }
        }
        if (!confirmed) {
            continue;  // new key not confirmed — suppress pivot to avoid false positive
        }

        // Build the incoming key's scale pitch-class set.
        const int newIonianPc = ionianTonicPcFromFifths(tr.newFifths);
        const int newTonicPc  = (newIonianPc + keyModeTonicOffset(tr.newMode)) % 12;
        const auto& newScale  = keyModeScaleIntervals(tr.newMode);
        bool newScalePcs[12]  = {};
        for (int iv : newScale) {
            newScalePcs[(newTonicPc + iv) % 12] = true;
        }

        // Walk backward from the boundary through the in-selection regions,
        // looking for the first chord that is:
        //   (a) diatonic to the outgoing key  (function.degree >= 0), AND
        //   (b) its root pitch class is in the incoming key's scale.
        const size_t searchBack = std::min(tr.boundaryIdx, n);  // stay in selection
        for (size_t j = searchBack; j > 0; --j) {
            const size_t idx = j - 1;
            const auto& prev = regions[idx].chordResult;

            if (prev.function.degree < 0) {
                continue;  // not diatonic to outgoing key
            }
            if (!newScalePcs[prev.identity.rootPc]) {
                continue;  // root not in incoming scale
            }

            // Found the pivot chord.  Format in both keys.
            const std::string oldRoman = ChordSymbolFormatter::formatRomanNumeral(prev);

            // Compute the degree in the incoming key.
            ChordAnalysisResult pivotInNew = prev;
            const int semisFromNewTonic =
                ((prev.identity.rootPc - newTonicPc) % 12 + 12) % 12;
            pivotInNew.function.degree    = -1;
            pivotInNew.function.keyTonicPc = newTonicPc;
            pivotInNew.function.keyMode    = tr.newMode;
            for (int d = 0; d < 7; ++d) {
                if (newScale[d] == semisFromNewTonic) {
                    pivotInNew.function.degree       = d;
                    pivotInNew.function.diatonicToKey = true;
                    break;
                }
            }
            const std::string newRoman = ChordSymbolFormatter::formatRomanNumeral(pivotInNew);

            if (!oldRoman.empty() && !newRoman.empty()) {
                // U+2192 RIGHT ARROW — pivot chord separator (same encoding
                // used in the chord staff path).
                labels.push_back({ regions[idx].startTick,
                                   oldRoman + " \u2192 " + newRoman });
            }
            break;  // one pivot per key transition
        }
    }

    return labels;
}

} // namespace mu::notation::internal
