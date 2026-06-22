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

#include "regiontonecollector.h"

#include <algorithm>
#include <cstdint>
#include <limits>
#include <map>

#include "engraving/dom/chord.h"
#include "engraving/dom/chordrest.h"
#include "engraving/dom/measure.h"
#include "engraving/dom/note.h"
#include "engraving/dom/segment.h"
#include "engraving/dom/sig.h"

#include "composing/analysis/chord/analysisutils.h"
#include "composing/analysis/scoreharvest/metricweights.h"

namespace shv = mu::composing::analysis::scoreharvest;

namespace mu::composing::analysis::engravingbridge {

using mu::composing::analysis::isDiatonicStep;

void soundingAt(const notemodel::NoteModel& noteModel,
                int tick,
                const std::set<std::size_t>& excludeStaves,
                std::vector<SoundingNote>& out)
{
    using notemodel::NoteEvent;

    auto passes = [&](const NoteEvent& e) -> bool {
        return e.staffEligible && !excludeStaves.count(static_cast<std::size_t>(e.staff))
               && e.plays && e.visible && !e.isGrace;
    };

    // Notes sounding AT `tick`: onset <= tick < release. overlapping[tick,tick+1)
    // is exactly that set, in model order (onset asc, then staff/voice/note).
    std::vector<const NoteEvent*> anchor;    // onset == tick
    std::vector<const NoteEvent*> sustained; // onset <  tick
    for (const NoteEvent* ne : noteModel.overlapping(tick, tick + 1)) {
        if (!passes(*ne)) {
            continue;
        }
        if (ne->onset == tick) {
            anchor.push_back(ne);
        } else {
            sustained.push_back(ne);
        }
    }

    // Legacy ordering fidelity: collectSoundingAt emitted the anchor-tick notes
    // first (staff/voice order), then walked backward emitting sustained notes in
    // descending onset order (staff/voice order within each prior segment). The
    // stable sort by descending onset reproduces that exactly (model order — the
    // staff/voice tiebreak — is preserved within each onset group).
    std::stable_sort(sustained.begin(), sustained.end(),
                     [](const NoteEvent* a, const NoteEvent* b) { return a->onset > b->onset; });

    out.reserve(out.size() + anchor.size() + sustained.size());
    for (const NoteEvent* ne : anchor) {
        out.push_back({ ne->pitch, ne->tpc });
    }
    for (const NoteEvent* ne : sustained) {
        out.push_back({ ne->pitch, ne->tpc });
    }
}

void collectSoundingAt(const mu::engraving::Score* sc,
                       const mu::engraving::Segment* anchorSeg,
                       const std::set<std::size_t>& excludeStaves,
                       std::vector<SoundingNote>& out)
{
    // Score-based convenience wrapper: build the note model and delegate to the
    // point-in-time view. Hot paths build the model once and call soundingAt.
    soundingAt(notemodel::NoteModel::build(sc), anchorSeg->tick().ticks(), excludeStaves, out);
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

void collectPitchContext(const mu::engraving::Score* sc,
                         const mu::engraving::Fraction& tick,
                         const mu::engraving::Fraction& windowStart,
                         const mu::engraving::Fraction& windowEnd,
                         const std::set<std::size_t>& excludeStaves,
                         const mu::composing::analysis::KeyModeAnalyzerPreferences& prefs,
                         std::vector<mu::composing::analysis::KeyModeAnalyzer::PitchContext>& ctx)
{
    using namespace mu::engraving;
    using namespace mu::composing::analysis;

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
        const BeatType bt = shv::safeBeatType(m, s);
        const double bw = shv::beatTypeToWeight(bt, prefs);

        const double beatsFromTick =
            std::abs((segTick - tick).ticks())
            / static_cast<double>(Constants::DIVISION);
        const double decay = shv::timeDecay(beatsFromTick);

        const bool isLookahead = (segTick > tick);
        const double lookaheadMul = isLookahead ? shv::LOOKAHEAD_WEIGHT : 1.0;

        struct NoteInfo { int ppitch; double durationQn; };
        std::vector<NoteInfo> segNotes;
        int lowestPitch = std::numeric_limits<int>::max();

        for (std::size_t si = 0; si < sc->nstaves(); ++si) {
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

namespace {

// Tick-based beat-type weight: reproduces scoreharvest::safeBeatType(measure,
// segment) using only an INDEXED measure lookup (Score::tick2measure) + the
// onset's rtick — no segment walk. The index-friendly form pitchContextOverSpan
// needs (distinct from the segment-taking safeBeatType, a different input domain).
double beatWeightForOnsetTick(const mu::engraving::Score* sc, int onsetTick,
                              const mu::composing::analysis::KeyModeAnalyzerPreferences& prefs)
{
    using namespace mu::engraving;
    if (!sc) {
        return shv::beatTypeToWeight(BeatType::SUBBEAT, prefs);
    }
    const Measure* m = sc->tick2measure(Fraction::fromTicks(onsetTick));
    if (!m) {
        return shv::beatTypeToWeight(BeatType::SUBBEAT, prefs);
    }
    const int num = m->timesig().numerator();
    const int den = m->timesig().denominator();
    if (num <= 0 || den <= 0) {
        return shv::beatTypeToWeight(BeatType::SUBBEAT, prefs);
    }
    const int rtick = onsetTick - m->tick().ticks();
    return shv::beatTypeToWeight(TimeSigFrac(num, den).rtick2beatType(rtick), prefs);
}

} // namespace

void pitchContextOverSpan(
    const notemodel::NoteModel& model,
    int windowStart, int windowEnd, int anchorStart, int anchorEnd,
    const std::set<std::size_t>& excludeStaves,
    const mu::composing::analysis::KeyModeAnalyzerPreferences& beatPrefs,
    const SpanWindowWeights& weights,
    std::vector<mu::composing::analysis::KeyModeAnalyzer::PitchContext>& out)
{
    using mu::composing::analysis::KeyModeAnalyzer;
    using notemodel::NoteEvent;

    const int div = mu::engraving::Constants::DIVISION;
    const std::vector<const NoteEvent*> notes = model.overlapping(windowStart, windowEnd);

    auto eligible = [&](const NoteEvent& e) -> bool {
        return e.plays && e.visible && e.staffEligible && !e.isGrace
               && !excludeStaves.count(static_cast<std::size_t>(e.staff));
    };

    // Lowest eligible pitch per onset tick (the per-onset bass).
    std::map<int, int> lowestByOnset;
    for (const NoteEvent* ne : notes) {
        if (!eligible(*ne)) {
            continue;
        }
        auto it = lowestByOnset.find(ne->onset);
        if (it == lowestByOnset.end() || ne->pitch < it->second) {
            lowestByOnset[ne->onset] = ne->pitch;
        }
    }

    const mu::engraving::Score* sc = model.score();
    out.reserve(out.size() + notes.size());
    for (const NoteEvent* ne : notes) {
        if (!eligible(*ne)) {
            continue;
        }
        const double durQn = ne->duration / static_cast<double>(div);

        // Distance (in beats) from the anchor span [anchorStart, anchorEnd): notes
        // inside it are full-weight; look-back decays; look-ahead decays + halves.
        double distBeats = 0.0;
        bool lookahead = false;
        if (ne->onset < anchorStart) {
            distBeats = (anchorStart - ne->onset) / static_cast<double>(div);
        } else if (ne->onset >= anchorEnd) {
            distBeats = (ne->onset - anchorEnd) / static_cast<double>(div);
            lookahead = true;
        }
        const double decay = shv::timeDecay(distBeats, weights.decayRate, weights.beatsPerDecayUnit);
        const double laMul = lookahead ? weights.lookaheadWeight : 1.0;

        KeyModeAnalyzer::PitchContext p;
        p.pitch          = ne->pitch;
        p.durationWeight = durQn * decay * laMul;
        p.beatWeight     = beatWeightForOnsetTick(sc, ne->onset, beatPrefs);
        p.isBass         = (ne->pitch == lowestByOnset[ne->onset]);
        out.push_back(p);
    }
}

std::vector<mu::engraving::Fraction>
detectOnsetSubBoundaries(const mu::engraving::Score* sc,
                         const mu::engraving::Fraction& startTick,
                         const mu::engraving::Fraction& endTick,
                         const std::set<std::size_t>& excludeStaves,
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

        for (std::size_t si = 0; si < sc->nstaves(); ++si) {
            if (excludeStaves.count(si) || !staffIsEligible(sc, si, s->tick())) {
                continue;
            }
            for (int v = 0; v < VOICES; ++v) {
                const ChordRest* cr = s->cr(static_cast<track_idx_t>(si) * VOICES + v);
                if (!cr || !cr->isChord() || cr->isGrace()) {
                    continue;
                }
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

    const int minGapTicks = 2 * Constants::DIVISION;

    uint16_t prevBits = onsets[0].bits;
    Fraction lastBoundaryTick = startTick;

    for (std::size_t i = 1; i < onsets.size(); ++i) {
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
    }

    return subBoundaries;
}

std::vector<mu::engraving::Fraction>
detectBassMovementSubBoundaries(const mu::engraving::Score* sc,
                                const mu::engraving::Fraction& startTick,
                                const mu::engraving::Fraction& endTick,
                                const std::set<std::size_t>& excludeStaves,
                                int minGapTicks)
{
    using namespace mu::engraving;

    std::vector<Fraction> subBoundaries;

    const Segment* firstSeg = sc->tick2segment(startTick, true, SegmentType::ChordRest);
    if (!firstSeg) {
        return subBoundaries;
    }

    struct BassOnset {
        Fraction tick;
        int bassPC = -1;
    };
    std::vector<BassOnset> onsets;

    for (const Segment* s = firstSeg;
         s && s->tick() < endTick;
         s = s->next1(SegmentType::ChordRest)) {

        const int segTick = s->tick().ticks();
        int lowestPitch = std::numeric_limits<int>::max();
        int lowestPC    = -1;

        for (std::size_t si = 0; si < sc->nstaves(); ++si) {
            if (excludeStaves.count(si) || !staffIsEligible(sc, si, s->tick())) {
                continue;
            }
            for (int v = 0; v < VOICES; ++v) {
                const ChordRest* cr = s->cr(static_cast<track_idx_t>(si) * VOICES + v);
                if (!cr || !cr->isChord() || cr->isGrace()) {
                    continue;
                }
                if (cr->tick().ticks() != segTick) {
                    continue;
                }
                for (const Note* n : toChord(cr)->notes()) {
                    if (!n->play() || !n->visible()) {
                        continue;
                    }
                    const int pitch = n->ppitch();
                    if (pitch < lowestPitch) {
                        lowestPitch = pitch;
                        lowestPC    = pitch % 12;
                    }
                }
            }
        }

        if (lowestPC >= 0) {
            onsets.push_back({ s->tick(), lowestPC });
        }
    }

    if (onsets.empty()) {
        return subBoundaries;
    }

    int  lastBoundaryBassPC  = onsets[0].bassPC;
    Fraction lastBoundaryTick = startTick;

    for (std::size_t i = 1; i < onsets.size(); ++i) {
        const int    curPC     = onsets[i].bassPC;
        const int    gapTicks  = (onsets[i].tick - lastBoundaryTick).ticks();

        if (curPC != lastBoundaryBassPC && gapTicks >= minGapTicks) {
            subBoundaries.push_back(onsets[i].tick);
            lastBoundaryTick   = onsets[i].tick;
            lastBoundaryBassPC = curPC;
        }
    }

    return subBoundaries;
}

mu::composing::analysis::ChordTemporalContext
findTemporalContext(const notemodel::NoteModel& noteModel,
                    const mu::engraving::Segment* seg,
                    const std::set<std::size_t>& excludeStaves,
                    int keyFifths,
                    mu::composing::analysis::KeySigMode keyMode,
                    int currentBassPc)
{
    using namespace mu::engraving;
    using namespace mu::composing::analysis;

    const Score* sc = noteModel.score();
    ChordTemporalContext temporalCtx;
    const Fraction tick = seg->tick();
    const auto chordAnalyzer = ChordAnalyzerFactory::create();

    // This bridge-path context builder walks BOTH directions, mirroring the batch path:
    //   - BACKWARD (seg->prev1): populates previousRootPc / previousQuality /
    //     previousBassPc / bassIsStepwiseFromPrevious.
    //   - FORWARD (seg->next1): populates nextRootPc / nextBassPc / bassIsStepwiseToNext.
    // The forward walk (added per docs/layer_architecture_audit.md Finding 3) lets
    // stepwiseBassLookaheadBonus, Gates B/G-B/H-B/E/F and Iter 91 fire on the bridge path
    // as they do on the batch path; previously these silently no-opped because nextRootPc
    // was always -1. Both neighbours are cold-analyzed (nullptr context, no temporal
    // chain) — a limitation shared with the backward walk and acceptable here: nextRootPc
    // is what the downstream gates need, and a cold nextRootPc is far better than -1.
    // Still NOT populated: the Step 1/2 progression fields (previousWinnerScore/Margin/
    // RootPcWeight, previousDistinctPcs), which require the neighbour's committed
    // competition result — unavailable without a full forward pre-pass over the score.

    for (const Segment* s = seg->prev1(SegmentType::ChordRest);
         s != nullptr;
         s = s->prev1(SegmentType::ChordRest)) {
        bool hasAttacks = false;
        for (std::size_t si = 0; si < sc->nstaves() && !hasAttacks; ++si) {
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
        soundingAt(noteModel, s->tick().ticks(), excludeStaves, prevSounding);
        if (!prevSounding.empty()) {
            const auto prevTones = buildTones(prevSounding);
            mu::composing::analysis::PostScoringGateContext prevGateCtx;
            auto prevResults =
                chordAnalyzer->analyzeChord(prevTones, keyFifths, keyMode, nullptr,
                                            mu::composing::analysis::kDefaultChordAnalyzerPreferences,
                                            &prevGateCtx);
            if (!prevResults.empty()) {
                mu::composing::analysis::applyIter8691Pedal(
                    prevResults,
                    prevGateCtx,
                    nullptr,
                    mu::composing::analysis::kDefaultChordAnalyzerPreferences);
                mu::composing::analysis::applyPostScoringGates(
                    prevResults,
                    mu::composing::analysis::kDefaultChordAnalyzerPreferences,
                    nullptr,
                    prevGateCtx);
                temporalCtx.previousRootPc  = prevResults.front().identity.rootPc;
                temporalCtx.previousQuality = prevResults.front().identity.quality;
                temporalCtx.previousBassPc  = prevResults.front().identity.bassPc;
            }
        }
        break;
    }

    if (currentBassPc != -1 && temporalCtx.previousBassPc != -1) {
        temporalCtx.bassIsStepwiseFromPrevious =
            isDiatonicStep(temporalCtx.previousBassPc, currentBassPc);
    }

    // Forward-lookahead walk — exact mirror of the backward walk above, via
    // seg->next1() instead of seg->prev1(). Crosses measure boundaries just as the
    // backward walk and the batch lookahead (collectRegionTones over the next region)
    // do — cadential bass motion across a barline is exactly what the lookahead signals
    // care about, so the next sounding chord is taken regardless of measure.
    for (const Segment* s = seg->next1(SegmentType::ChordRest);
         s != nullptr;
         s = s->next1(SegmentType::ChordRest)) {
        bool hasAttacks = false;
        for (std::size_t si = 0; si < sc->nstaves() && !hasAttacks; ++si) {
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

        std::vector<SoundingNote> nextSounding;
        soundingAt(noteModel, s->tick().ticks(), excludeStaves, nextSounding);
        if (!nextSounding.empty()) {
            const auto nextTones = buildTones(nextSounding);
            mu::composing::analysis::PostScoringGateContext nextGateCtx;
            auto nextResults =
                chordAnalyzer->analyzeChord(nextTones, keyFifths, keyMode, nullptr,
                                            mu::composing::analysis::kDefaultChordAnalyzerPreferences,
                                            &nextGateCtx);
            if (!nextResults.empty()) {
                mu::composing::analysis::applyIter8691Pedal(
                    nextResults,
                    nextGateCtx,
                    nullptr,
                    mu::composing::analysis::kDefaultChordAnalyzerPreferences);
                mu::composing::analysis::applyPostScoringGates(
                    nextResults,
                    mu::composing::analysis::kDefaultChordAnalyzerPreferences,
                    nullptr,
                    nextGateCtx);
                temporalCtx.nextRootPc = nextResults.front().identity.rootPc;
                temporalCtx.nextBassPc = nextResults.front().identity.bassPc;
            }
        }
        break;
    }

    if (currentBassPc != -1 && temporalCtx.nextBassPc != -1) {
        temporalCtx.bassIsStepwiseToNext =
            isDiatonicStep(currentBassPc, temporalCtx.nextBassPc);
    }

    return temporalCtx;
}

} // namespace mu::composing::analysis::engravingbridge
