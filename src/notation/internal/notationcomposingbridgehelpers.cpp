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

#include <cmath>
#include <limits>
#include <optional>

#include "engraving/dom/chord.h"
#include "engraving/dom/key.h"
#include "engraving/dom/measure.h"
#include "engraving/dom/note.h"
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
        const TimeSigFrac tsig(m->timesig().numerator(),
                               m->timesig().denominator());
        const BeatType bt = tsig.rtick2beatType(s->rtick().ticks());
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
        if (outScore) *outScore = 0.0;
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

} // namespace mu::notation::internal
