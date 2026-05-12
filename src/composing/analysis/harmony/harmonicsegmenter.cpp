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

#include "harmonicsegmenter.h"

#include <algorithm>
#include <cstdio>
#include <set>

#include "engraving/dom/score.h"
#include "engraving/dom/measure.h"
#include "engraving/dom/segment.h"
#include "engraving/dom/chord.h"
#include "engraving/dom/note.h"
#include "engraving/dom/staff.h"
#include "engraving/types/fraction.h"
#include "engraving/types/constants.h"
#include "engraving/types/types.h"

namespace mu::composing {

using mu::engraving::Score;
using mu::engraving::Segment;
using mu::engraving::Measure;
using mu::engraving::Chord;
using mu::engraving::Note;
using mu::engraving::EngravingItem;
using mu::engraving::Fraction;
using mu::engraving::SegmentType;
using mu::engraving::voice_idx_t;
using mu::engraving::VOICES;
using mu::engraving::staff2track;
using mu::engraving::toChord;
using Constants = mu::engraving::Constants;

namespace {

/// Maps a ChordQuality enum value to the same string used by batch_analyze.cpp's
/// JSON output, so PlacedRegion::quality remains comparable across both consumers.
const char* qualityToString(analysis::ChordQuality q)
{
    switch (q) {
    case analysis::ChordQuality::Major:          return "Major";
    case analysis::ChordQuality::Minor:          return "Minor";
    case analysis::ChordQuality::Diminished:     return "Diminished";
    case analysis::ChordQuality::Augmented:      return "Augmented";
    case analysis::ChordQuality::HalfDiminished: return "HalfDiminished";
    case analysis::ChordQuality::Suspended2:     return "Suspended2";
    case analysis::ChordQuality::Suspended4:     return "Suspended4";
    case analysis::ChordQuality::Power:          return "Power";
    default:                                      return "Unknown";
    }
}

/// Returns true if tick falls on a quarter-note beat boundary within its measure.
/// Uses the score's measure containing tick; quarter-note grid is used for all
/// time signatures for now (beat-synchronous refinement deferred).
bool isOnBeat(const Score* score, const Fraction& tick)
{
    if (!score) return false;
    const Measure* m = score->tick2measure(tick);
    if (!m) return false;
    const Fraction offset = tick - m->tick();
    return (offset.ticks() % Constants::DIVISION) == 0;
}

/// Returns the number of distinct chord-bearing staves that have at least one
/// non-rest, non-grace note sounding anywhere in [startTick, endTick).
/// A chord whose onset precedes startTick but sustains into the region also counts.
int countParticipatingStaves(const Score* score,
                             const Fraction& startTick,
                             const Fraction& endTick,
                             const std::set<size_t>& excludeStaves,
                             const std::function<bool(size_t)>& staffIsEligible)
{
    if (!score || endTick <= startTick) {
        return 0;
    }
    const Segment* firstSeg = score->tick2segment(startTick, true, SegmentType::ChordRest);
    if (!firstSeg) {
        return 0;
    }

    int count = 0;
    for (size_t staffIdx = 0; staffIdx < score->nstaves(); ++staffIdx) {
        if (excludeStaves.count(staffIdx) || !staffIsEligible(staffIdx)) {
            continue;
        }
        bool hasNote = false;
        for (const Segment* s = firstSeg; s && s->tick() < endTick && !hasNote;
             s = s->next1(SegmentType::ChordRest)) {
            for (voice_idx_t v = 0; v < VOICES && !hasNote; ++v) {
                const EngravingItem* e = s->element(staff2track(staffIdx, v));
                if (!e || !e->isChord()) {
                    continue;
                }
                const Chord* chord = toChord(e);
                if (chord->isGrace()) {
                    continue;
                }
                const int chordStart = s->tick().ticks();
                const int chordEnd = chordStart + chord->actualTicks().ticks();
                if (chordEnd <= startTick.ticks() || chordStart >= endTick.ticks()) {
                    continue;
                }
                for (const Note* n : chord->notes()) {
                    if (!n->play() || !n->visible()) {
                        continue;
                    }
                    hasNote = true;
                    break;
                }
            }
        }
        if (hasNote) {
            ++count;
        }
    }
    return count;
}

/// Returns all ticks within [startTick, endTick) at which any note in a
/// chord-bearing stave attacks (new onset). The result is sorted and
/// deduplicated. Always includes startTick.
std::vector<Fraction>
collectNoteChangeTicks(const Score* score,
                       const Fraction& startTick,
                       const Fraction& endTick,
                       const std::set<size_t>& excludeStaves,
                       const std::function<bool(size_t)>& staffIsEligible)
{
    std::set<int> tickSet;
    tickSet.insert(startTick.ticks());

    if (!score || endTick <= startTick) {
        return { startTick };
    }

    const Segment* firstSeg = score->tick2segment(startTick, true, SegmentType::ChordRest);
    if (!firstSeg) {
        return { startTick };
    }

    for (const Segment* s = firstSeg; s && s->tick() < endTick;
         s = s->next1(SegmentType::ChordRest)) {
        const int segTick = s->tick().ticks();
        if (segTick < startTick.ticks()) {
            continue;
        }

        for (size_t staffIdx = 0; staffIdx < score->nstaves(); ++staffIdx) {
            if (excludeStaves.count(staffIdx) || !staffIsEligible(staffIdx)) {
                continue;
            }
            for (voice_idx_t v = 0; v < VOICES; ++v) {
                const EngravingItem* e = s->element(staff2track(staffIdx, v));
                if (!e || !e->isChord()) {
                    continue;
                }
                const Chord* chord = toChord(e);
                if (chord->isGrace()) {
                    continue;
                }
                // Onset-only: only fire if at least one note actually attacks at segTick.
                bool hasOnset = false;
                for (const Note* n : chord->notes()) {
                    if (!n->play() || !n->visible()) {
                        continue;
                    }
                    if (n->tieBack()) {
                        continue;  // tied-in continuation, not a new onset
                    }
                    hasOnset = true;
                    break;
                }
                if (hasOnset) {
                    tickSet.insert(segTick);
                    break;  // one onset per staff is enough to record the tick
                }
            }
        }
    }

    std::vector<Fraction> result;
    result.reserve(tickSet.size());
    for (int t : tickSet) {
        result.push_back(Fraction::fromTicks(t));
    }
    return result;
}

/// Iter 53 Round 2: promote round=0 candidate regions within [gapStartTick, gapEndTick)
/// that are harmonically distinct from their current neighbours and score above
/// kRound2MinScore. Processes candidates in descending initial-score order; each
/// promotion updates the neighbourhood for subsequent candidates. After the
/// promotion pass, each promoted candidate is re-scored with its actual placed
/// neighbours as bilateral context.
void fillGap(std::vector<PlacedRegion>& regions,
             int gapStartTick,
             int gapEndTick,
             const PlacedRegion* leftAnchor,
             const PlacedRegion* rightAnchor,
             int targetRound,
             const Score* score,
             const std::set<size_t>& /*excludeStaves*/,
             const analysis::ChordAnalyzerPreferences& prefs,
             analysis::IChordAnalyzer* chordAnalyzer,
             int globalKeyFifths,
             analysis::KeySigMode globalKeyMode,
             const HarmonicSegmenterCallbacks& callbacks)
{
    if (!score || !chordAnalyzer || gapEndTick <= gapStartTick) {
        return;
    }

    struct Scored {
        size_t                  idx = 0;
        double                  initialScore = 0.0;
        int                     initialRootPc = -1;
        int                     initialBassPc = -1;
        analysis::ChordQuality  initialQuality = analysis::ChordQuality::Unknown;
    };
    std::vector<Scored> scored;
    scored.reserve(16);

    analysis::ChordTemporalContext initCtx;
    initCtx.previousRootPc = leftAnchor  ? leftAnchor->rootPitchClass  : -1;
    initCtx.nextRootPc     = rightAnchor ? rightAnchor->rootPitchClass : -1;

    for (size_t i = 0; i < regions.size(); ++i) {
        const PlacedRegion& r = regions[i];
        if (r.round != 0) continue;
        if (r.startTick < gapStartTick || r.startTick >= gapEndTick) continue;

        auto tones = callbacks.collectRegionTones(r.startTick, r.endTick);
        if (tones.empty()) continue;
        const auto cands = chordAnalyzer->analyzeChord(
            tones, globalKeyFifths, globalKeyMode, &initCtx, prefs);
        if (cands.empty()) continue;

        Scored s;
        s.idx            = i;
        s.initialScore   = cands[0].identity.score;
        s.initialRootPc  = cands[0].identity.rootPc;
        s.initialBassPc  = cands[0].identity.bassPc;
        s.initialQuality = cands[0].identity.quality;
        scored.push_back(s);
    }

    std::sort(scored.begin(), scored.end(),
        [](const Scored& a, const Scored& b) { return a.initialScore > b.initialScore; });

    struct Neighbour {
        int         startTick = 0;
        int         rootPc    = -1;
        std::string quality;
    };
    std::vector<Neighbour> neighbours;
    if (leftAnchor) {
        neighbours.push_back({leftAnchor->startTick,  leftAnchor->rootPitchClass,  leftAnchor->quality});
    }
    if (rightAnchor) {
        neighbours.push_back({rightAnchor->startTick, rightAnchor->rootPitchClass, rightAnchor->quality});
    }
    std::sort(neighbours.begin(), neighbours.end(),
        [](const Neighbour& a, const Neighbour& b) { return a.startTick < b.startTick; });

    std::vector<size_t> promotedIdxs;

    auto findNeighbours = [&](int tick, const Neighbour** L, const Neighbour** R) {
        *L = nullptr;
        *R = nullptr;
        for (const Neighbour& nb : neighbours) {
            if (nb.startTick < tick) {
                *L = &nb;
            } else if (nb.startTick > tick && !*R) {
                *R = &nb;
            }
        }
    };

    for (const Scored& sc : scored) {
        if (sc.initialScore < kRound2MinScore) continue;
        PlacedRegion& r = regions[sc.idx];

        const Neighbour* L = nullptr;
        const Neighbour* R = nullptr;
        findNeighbours(r.startTick, &L, &R);

        const std::string candQ = qualityToString(sc.initialQuality);
        auto distinct = [&](const Neighbour* nb) {
            if (!nb) return true;
            return nb->rootPc != sc.initialRootPc || nb->quality != candQ;
        };
        if (!distinct(L) || !distinct(R)) continue;

        r.round           = targetRound;
        r.confidence      = sc.initialScore;
        r.rootPitchClass  = sc.initialRootPc;
        r.bassPitchClass  = sc.initialBassPc;
        r.quality         = candQ;
        char buf[200];
        std::snprintf(buf, sizeof(buf),
                      "Round %d fill: distinct from L(root=%d) and R(root=%d) score=%.3f",
                      targetRound,
                      L ? L->rootPc : -1,
                      R ? R->rootPc : -1,
                      sc.initialScore);
        r.reason = buf;

        promotedIdxs.push_back(sc.idx);
        Neighbour nb{r.startTick, r.rootPitchClass, r.quality};
        auto it = std::upper_bound(neighbours.begin(), neighbours.end(), nb,
            [](const Neighbour& a, const Neighbour& b) { return a.startTick < b.startTick; });
        neighbours.insert(it, nb);
    }

    // Step 4: re-score each promoted candidate with updated bilateral context.
    for (size_t pi : promotedIdxs) {
        PlacedRegion& r = regions[pi];
        const Neighbour* L = nullptr;
        const Neighbour* R = nullptr;
        findNeighbours(r.startTick, &L, &R);

        analysis::ChordTemporalContext ctx;
        ctx.previousRootPc = L ? L->rootPc : -1;
        ctx.nextRootPc     = R ? R->rootPc : -1;

        auto tones = callbacks.collectRegionTones(r.startTick, r.endTick);
        if (tones.empty()) continue;
        const auto cands = chordAnalyzer->analyzeChord(
            tones, globalKeyFifths, globalKeyMode, &ctx, prefs);
        if (cands.empty()) continue;

        r.confidence     = cands[0].identity.score;
        r.rootPitchClass = cands[0].identity.rootPc;
        r.bassPitchClass = cands[0].identity.bassPc;
        r.quality        = qualityToString(cands[0].identity.quality);
    }
}

} // namespace

std::vector<PlacedRegion>
greedyExpandSegmentation(const Score* score,
                         const Fraction& startTick,
                         const Fraction& endTick,
                         const std::set<size_t>& excludeStaves,
                         const analysis::ChordAnalyzerPreferences& prefs,
                         analysis::IChordAnalyzer* chordAnalyzer,
                         int globalKeyFifths,
                         analysis::KeySigMode globalKeyMode,
                         const HarmonicSegmenterCallbacks& callbacks)
{
    std::vector<PlacedRegion> candidates;
    const auto changeTicks = collectNoteChangeTicks(
        score, startTick, endTick, excludeStaves, callbacks.staffIsEligible);
    if (changeTicks.empty()) {
        return candidates;
    }

    candidates.reserve(changeTicks.size());
    for (size_t i = 0; i < changeTicks.size(); ++i) {
        PlacedRegion pr;
        pr.startTick = changeTicks[i].ticks();
        pr.endTick   = (i + 1 < changeTicks.size())
                       ? changeTicks[i + 1].ticks()
                       : endTick.ticks();
        if (pr.endTick <= pr.startTick) {
            continue;
        }
        pr.round      = 0;
        pr.confidence = 0.0;
        pr.isAnchor   = false;
        pr.reason     = "candidate — unplaced";
        candidates.push_back(std::move(pr));
    }

    // Round 1: promote candidates that satisfy all of
    //   (a) onset on a quarter-note beat boundary,
    //   (b) duration ≥ 2×DIVISION (half note),
    //   (c) ≥3 chord-bearing staves participating,
    //   (d) analyzeChord winner score ≥ kAnchorMinScore.
    if (!chordAnalyzer) {
        return candidates;
    }
    for (PlacedRegion& region : candidates) {
        const Fraction regionStart = Fraction::fromTicks(region.startTick);
        const Fraction regionEnd   = Fraction::fromTicks(region.endTick);

        if (!isOnBeat(score, regionStart)) {
            continue;
        }
        if ((region.endTick - region.startTick) < kAnchorMinDurationTicks) {
            continue;
        }
        if (countParticipatingStaves(score, regionStart, regionEnd, excludeStaves,
                                     callbacks.staffIsEligible) < 3) {
            continue;
        }

        auto tones = callbacks.collectRegionTones(region.startTick, region.endTick);
        if (tones.empty()) {
            continue;
        }
        const auto chordCands = chordAnalyzer->analyzeChord(
            tones, globalKeyFifths, globalKeyMode, nullptr, prefs);
        if (chordCands.empty()) {
            continue;
        }
        const double winnerScore = chordCands[0].identity.score;
        if (winnerScore < kAnchorMinScore) {
            continue;
        }

        region.round          = 1;
        region.isAnchor       = true;
        region.confidence     = winnerScore;
        region.rootPitchClass = chordCands[0].identity.rootPc;
        region.bassPitchClass = chordCands[0].identity.bassPc;
        region.quality        = qualityToString(chordCands[0].identity.quality);

        const int beatNum = 1 + (region.startTick - score->tick2measure(regionStart)->tick().ticks())
                                / Constants::DIVISION;
        char buf[160];
        std::snprintf(buf, sizeof(buf),
                      "Round 1 anchor: beat=%d dur>=%dtk voice>=3 score=%.3f",
                      beatNum, kAnchorMinDurationTicks, winnerScore);
        region.reason = buf;
    }

    // Round 2 — fill gaps between Round 1 anchors using bilateral anchor context.
    std::vector<PlacedRegion*> placed;
    placed.reserve(candidates.size());
    for (auto& r : candidates) {
        if (r.round >= 1) placed.push_back(&r);
    }
    std::sort(placed.begin(), placed.end(),
        [](const PlacedRegion* a, const PlacedRegion* b) {
            return a->startTick < b->startTick;
        });

    if (!placed.empty() && placed.front()->startTick > startTick.ticks()) {
        fillGap(candidates, startTick.ticks(), placed.front()->startTick,
                nullptr, placed.front(), 2, score, excludeStaves, prefs,
                chordAnalyzer, globalKeyFifths, globalKeyMode, callbacks);
    }
    for (size_t i = 0; i + 1 < placed.size(); ++i) {
        if (placed[i]->endTick < placed[i + 1]->startTick) {
            fillGap(candidates, placed[i]->endTick, placed[i + 1]->startTick,
                    placed[i], placed[i + 1], 2, score, excludeStaves, prefs,
                    chordAnalyzer, globalKeyFifths, globalKeyMode, callbacks);
        }
    }
    if (!placed.empty() && placed.back()->endTick < endTick.ticks()) {
        fillGap(candidates, placed.back()->endTick, endTick.ticks(),
                placed.back(), nullptr, 2, score, excludeStaves, prefs,
                chordAnalyzer, globalKeyFifths, globalKeyMode, callbacks);
    }

    return candidates;
}

std::vector<Fraction>
placedRegionsToTicks(const std::vector<PlacedRegion>& regions)
{
    std::vector<Fraction> ticks;
    for (const auto& r : regions) {
        if (r.round >= 1) {
            ticks.push_back(Fraction::fromTicks(r.startTick));
        }
    }
    std::sort(ticks.begin(), ticks.end());
    ticks.erase(std::unique(ticks.begin(), ticks.end()), ticks.end());
    return ticks;
}

} // namespace mu::composing
