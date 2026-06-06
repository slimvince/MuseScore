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
#include <cmath>
#include <cstdio>
#include <set>

#include "../chord/analysisutils.h"
#include "engraving/dom/score.h"
#include "engraving/dom/measure.h"
#include "engraving/dom/segment.h"
#include "engraving/dom/chord.h"
#include "engraving/dom/note.h"
#include "engraving/dom/staff.h"
#include "engraving/dom/tuplet.h"
#include "engraving/types/fraction.h"
#include "engraving/types/constants.h"
#include "engraving/types/types.h"

namespace mu::composing {

using mu::engraving::Score;
using mu::engraving::Segment;
using mu::engraving::Measure;
using mu::engraving::Chord;
using mu::engraving::Note;
using mu::engraving::Tuplet;
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
/// chord-bearing stave attacks (new onset) OR releases (Iter 73 Fix A).
/// Per Pardo & Birmingham (Computer Music Journal, 2002), harmonic changes
/// may occur at note-on OR note-off; music21's chordify implements the same
/// salami-slicing principle. The result is sorted and deduplicated. Always
/// includes startTick.
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

    // Iter 73 Fix A — note-end pass.
    //
    // Per Pardo & Birmingham (CMJ 2002), harmonic boundaries occur at
    // note-on OR note-off. Collect release ticks for notes that do not
    // tie forward — sustained voices that release without a coincident
    // new onset would otherwise be invisible to the onset-only pass.
    // Deduplication is automatic (tickSet is a std::set).
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
                // True-release: at least one playing note in this chord
                // does not tie forward into the next chord. Tied-forward
                // notes continue sounding so they do not contribute a
                // release event here.
                bool anyRelease = false;
                for (const Note* n : chord->notes()) {
                    if (!n->play() || !n->visible()) {
                        continue;
                    }
                    if (n->tieFor()) {
                        continue;
                    }
                    anyRelease = true;
                    break;
                }
                if (!anyRelease) {
                    continue;
                }
                const int endTickVal = segTick + chord->actualTicks().ticks();
                if (endTickVal > startTick.ticks()
                    && endTickVal < endTick.ticks()) {
                    tickSet.insert(endTickVal);
                }
            }
        }
    }

    // Iter 71 — Fix B: tuplet alignment.
    //
    // populateChordTrack must emit chord-track entries at beat-aligned ticks;
    // a tick inside a tuplet group (not its first element) is not beat-aligned
    // on the chord-track staff and causes overlapping chord/rest insertions.
    // Snap any mid-tuplet tick to the start tick of its (outermost) enclosing
    // tuplet group, then deduplicate. The boundary at startTick is never
    // snapped below itself — the caller's range is authoritative.
    if (score) {
        std::set<int> snapped;
        const int startTickI = startTick.ticks();
        for (int t : tickSet) {
            const Fraction tickF = Fraction::fromTicks(t);
            const Segment* seg = score->tick2segment(tickF, true, SegmentType::ChordRest);
            int snapTick = t;
            if (seg) {
                for (size_t staffIdx = 0; staffIdx < score->nstaves(); ++staffIdx) {
                    if (excludeStaves.count(staffIdx) || !staffIsEligible(staffIdx)) {
                        continue;
                    }
                    for (voice_idx_t v = 0; v < VOICES; ++v) {
                        const EngravingItem* e = seg->element(staff2track(staffIdx, v));
                        if (!e || !e->isChord()) {
                            continue;
                        }
                        const Chord* chord = toChord(e);
                        if (chord->isGrace()) {
                            continue;
                        }
                        const Tuplet* top = chord->topTuplet();
                        if (!top) {
                            continue;
                        }
                        const int tupletStart = top->tick().ticks();
                        if (tupletStart < snapTick && tupletStart >= startTickI) {
                            snapTick = tupletStart;
                        }
                    }
                }
            }
            snapped.insert(snapTick);
        }
        tickSet.swap(snapped);
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
             const HarmonicSegmenterCallbacks& callbacks,
             double effectiveRound2MinScore,
             int effectiveAnchorMinDurationTicks)
{
    if (!score || !chordAnalyzer || gapEndTick <= gapStartTick) {
        return;
    }

    // Iter 94 — suppress voice-leading step bonuses for all internal greedy-expand
    // boundary-exploration analyzeChord calls.  The bonus is only applied in the
    // final per-region pass after segmentation has produced boundaries.
    analysis::ChordAnalyzerPreferences explorePrefs = prefs;
    explorePrefs.explorationMode = true;

    struct Scored {
        size_t                  idx = 0;
        double                  initialScore = 0.0;
        int                     initialRootPc = -1;
        int                     initialBassPc = -1;
        analysis::ChordQuality  initialQuality = analysis::ChordQuality::Unknown;
        // Iter 71 Fix A — true-local (no bilateral context) result.
        // Used for the distinctness comparison so that bilateral-context
        // bonuses (rootContinuityBonus, resolutionBonus) cannot mask
        // candidates whose local chord identity genuinely differs from
        // surrounding anchor identities (Pattern 2 — tonic smearing).
        double                  localScore = 0.0;
        int                     localRootPc = -1;
        int                     localBassPc = -1;
        analysis::ChordQuality  localQuality = analysis::ChordQuality::Unknown;
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
        analysis::PostScoringGateContext gateCtxInit;
        auto cands = chordAnalyzer->analyzeChord(
            tones, globalKeyFifths, globalKeyMode, &initCtx, explorePrefs, &gateCtxInit);
        if (cands.empty()) continue;
        analysis::applyIter8691Pedal(cands, gateCtxInit, &initCtx, explorePrefs);
        analysis::applyPostScoringGates(cands, explorePrefs, &initCtx, gateCtxInit);

        // Iter 71 Fix A — second analyzeChord call with no bilateral
        // context. Same tones, no anchor influence.
        analysis::PostScoringGateContext gateCtxLocal;
        auto localCands = chordAnalyzer->analyzeChord(
            tones, globalKeyFifths, globalKeyMode, nullptr, explorePrefs, &gateCtxLocal);
        if (!localCands.empty()) {
            analysis::applyIter8691Pedal(localCands, gateCtxLocal, nullptr, explorePrefs);
            analysis::applyPostScoringGates(localCands, explorePrefs, nullptr, gateCtxLocal);
        }

        Scored s;
        s.idx            = i;
        s.initialScore   = cands[0].identity.score;
        s.initialRootPc  = cands[0].identity.rootPc;
        s.initialBassPc  = cands[0].identity.bassPc;
        s.initialQuality = cands[0].identity.quality;
        if (!localCands.empty()) {
            s.localScore   = localCands[0].identity.score;
            s.localRootPc  = localCands[0].identity.rootPc;
            s.localBassPc  = localCands[0].identity.bassPc;
            s.localQuality = localCands[0].identity.quality;
        }
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
        if (sc.initialScore < effectiveRound2MinScore) continue;
        PlacedRegion& r = regions[sc.idx];

        const Neighbour* L = nullptr;
        const Neighbour* R = nullptr;
        findNeighbours(r.startTick, &L, &R);

        // Iter 71 Fix A — Pattern 2 (smearing).
        // When both anchors share a root (the smearing pattern: tonic
        // anchors on both sides of a non-tonic region), the bilateral
        // context bonuses (rootContinuity / resolution) can pull the
        // candidate's initial root toward the shared anchor root,
        // defeating the distinctness check. In that specific topology,
        // re-evaluate with a true-local analyzeChord (no bilateral
        // context). When the true-local result differs from the
        // bilateral one and clears the Round 2 score floor, prefer
        // the true-local identity for both distinctness and placement.
        // Gated on L && R && L->rootPc == R->rootPc to keep the rest
        // of the Baroque corpus untouched.
        const bool smearingTopology
            = L && R && L->rootPc == R->rootPc;
        const bool useTrueLocal
            = smearingTopology
            && sc.localRootPc >= 0
            && sc.localRootPc != sc.initialRootPc
            && sc.localScore >= effectiveRound2MinScore;

        const int       useRootPc  = useTrueLocal ? sc.localRootPc  : sc.initialRootPc;
        const int       useBassPc  = useTrueLocal ? sc.localBassPc  : sc.initialBassPc;
        const auto      useQuality = useTrueLocal ? sc.localQuality : sc.initialQuality;
        const double    useScore   = useTrueLocal ? sc.localScore   : sc.initialScore;
        const std::string candQ    = qualityToString(useQuality);

        auto distinct = [&](const Neighbour* nb) {
            if (!nb) return true;
            return nb->rootPc != useRootPc || nb->quality != candQ;
        };
        if (!distinct(L) || !distinct(R)) continue;

        r.round           = targetRound;
        r.confidence      = useScore;
        r.rootPitchClass  = useRootPc;
        r.bassPitchClass  = useBassPc;
        r.quality         = candQ;
        char buf[200];
        std::snprintf(buf, sizeof(buf),
                      "Round %d fill%s: distinct from L(root=%d) and R(root=%d) score=%.3f",
                      targetRound,
                      useTrueLocal ? " (true-local)" : "",
                      L ? L->rootPc : -1,
                      R ? R->rootPc : -1,
                      useScore);
        r.reason = buf;

        promotedIdxs.push_back(sc.idx);
        Neighbour nb{r.startTick, r.rootPitchClass, r.quality};
        auto it = std::upper_bound(neighbours.begin(), neighbours.end(), nb,
            [](const Neighbour& a, const Neighbour& b) { return a.startTick < b.startTick; });
        neighbours.insert(it, nb);
    }

    // Step 4: re-score each promoted candidate with updated bilateral context.
    //
    // Iter 70 — local-evidence preference. For long gaps (Pattern 2: tonic
    // smearing), the bilateral re-score would otherwise overwrite a clear
    // local dominant identity with the dominant root of distant anchors.
    // When the local identity differs from both anchor roots, the original
    // placement score met effectiveRound2MinScore, AND the re-score would
    // flip the chord identity, trust the local placement and keep its
    // identity instead. For very long gaps (> 4 × min-anchor-duration),
    // also drop the bilateral context entirely from the re-score itself.
    const int gapLength = gapEndTick - gapStartTick;
    const bool longGap = gapLength > 4 * effectiveAnchorMinDurationTicks;
    for (size_t pi : promotedIdxs) {
        PlacedRegion& r = regions[pi];
        const Neighbour* L = nullptr;
        const Neighbour* R = nullptr;
        findNeighbours(r.startTick, &L, &R);

        analysis::ChordTemporalContext ctx;
        if (!longGap) {
            ctx.previousRootPc = L ? L->rootPc : -1;
            ctx.nextRootPc     = R ? R->rootPc : -1;
        }

        auto tones = callbacks.collectRegionTones(r.startTick, r.endTick);
        if (tones.empty()) continue;
        analysis::PostScoringGateContext gateCtxReScore;
        auto cands = chordAnalyzer->analyzeChord(
            tones, globalKeyFifths, globalKeyMode, &ctx, explorePrefs, &gateCtxReScore);
        if (cands.empty()) continue;
        analysis::applyIter8691Pedal(cands, gateCtxReScore, &ctx, explorePrefs);
        analysis::applyPostScoringGates(cands, explorePrefs, &ctx, gateCtxReScore);

        const int newRootPc = cands[0].identity.rootPc;
        const bool reScoreFlipsIdentity = (newRootPc != r.rootPitchClass);
        const bool localDiffersFromAnchors =
            (!L || L->rootPc != r.rootPitchClass)
            && (!R || R->rootPc != r.rootPitchClass);
        if (reScoreFlipsIdentity
            && r.confidence >= effectiveRound2MinScore
            && localDiffersFromAnchors) {
            char buf[200];
            std::snprintf(buf, sizeof(buf),
                          "Round %d fill (local-preferred): rejected bilateral flip to root=%d, kept local root=%d score=%.3f gap=%d%s",
                          targetRound, newRootPc, r.rootPitchClass,
                          r.confidence, gapLength, longGap ? " long" : "");
            r.reason = buf;
            continue;
        }

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

    // Iter 69 — texture-adaptive thresholds.
    //
    // Greedy-expand was tuned against SATB chorales (dense vertical texture,
    // regular horizontal rhythm). Replace the SATB-hardcoded constants with
    // thresholds derived from two density dimensions measured per-score:
    //
    //   Vertical density   — mean concurrent eligible staves at candidate ticks
    //   Horizontal density — mean gap between note-change ticks
    //
    // SATB (~4 eligible staves, meanActiveStaves ~3.5, meanTickSpacing ~DIVISION)
    // self-calibrates to the previous constants (3-staff gate, 1.5 score, 1*DIVISION
    // duration, 1.25 Round-2 score). Sparser textures get proportionally relaxed
    // gates so genuine anchors aren't rejected for low voice count or sparse onsets.
    int nEligibleStaves = 0;
    if (score) {
        for (size_t s = 0; s < score->nstaves(); ++s) {
            if (!excludeStaves.count(s) && callbacks.staffIsEligible(s)) {
                ++nEligibleStaves;
            }
        }
    }

    double meanActiveStaves = 0.0;
    for (size_t i = 0; i < changeTicks.size(); ++i) {
        const Fraction regStart = changeTicks[i];
        const Fraction regEnd   = (i + 1 < changeTicks.size())
                                  ? changeTicks[i + 1] : endTick;
        if (regEnd <= regStart) continue;
        meanActiveStaves += countParticipatingStaves(
            score, regStart, regEnd, excludeStaves, callbacks.staffIsEligible);
    }
    if (!changeTicks.empty()) {
        meanActiveStaves /= double(changeTicks.size());
    }

    const double totalSpan = double(endTick.ticks() - startTick.ticks());
    const double meanTickSpacing = (changeTicks.size() > 1)
        ? totalSpan / double(changeTicks.size() - 1)
        : std::max(totalSpan, 1.0);

    // Staff-count gate: round(75% of MEAN ACTIVE staves), min 1 (Iter 70 — Pattern 3).
    // Previously used nEligibleStaves (total eligible) which over-counted on fixtures
    // where staves alternate rather than play simultaneously (Corelli trio, small piano).
    // SATB (meanActive ≈ 3.5):  round(2.625) = 3  ← matches prior SATB behaviour
    // Trio alternating (≈ 1.5): round(1.125) = 1
    // Piano alternating (≈ 1.0): round(0.75) = 1
    const int effectiveStaveThreshold = std::max(
        1, static_cast<int>(std::round(meanActiveStaves * 0.75)));

    // Vertical factor: 1.0 at SATB density (mean ~3.5 active staves), lower for sparse.
    // Score scaling derived from Step 2 corpus inspection: Baroque chord scores are
    // largely flat across voice count (mean ~2.85 for nc=3-4, ~2.77 for nc=5+),
    // so the relaxation slope is shallow (A = 0.75 — close to 1.0).
    // SATB:  factor=1.0 -> eff = 1.5 (unchanged)
    // 2-voice: factor~0.57 -> eff ~ 1.34
    // 1-voice: factor~0.29 -> eff ~ 1.23
    constexpr double kRefActiveStaves = 3.5;
    constexpr double kScoreFloorFraction = 0.75;
    const double verticalFactor = (kRefActiveStaves > 0.0)
        ? std::min(1.0, meanActiveStaves / kRefActiveStaves) : 1.0;
    const double scoreScale
        = kScoreFloorFraction + (1.0 - kScoreFloorFraction) * verticalFactor;
    const double effectiveAnchorMinScore = kAnchorMinScore * scoreScale;
    const double effectiveRound2MinScore = kRound2MinScore * scoreScale;

    // Horizontal factor: 1.0 at SATB pacing (~DIVISION between onsets), lower for
    // sparser/larger gaps. Sparse horizontal -> shorter minimum duration required.
    const double kRefTickSpacing = double(Constants::DIVISION);
    const double horizontalFactor = (meanTickSpacing > 0.0)
        ? std::min(1.0, kRefTickSpacing / meanTickSpacing) : 1.0;
    // Iter 70 (Pattern 1): floor scales with meanTickSpacing so short-duration
    // note-change events in sparse horizontal textures reach Round 1 eligibility.
    // SATB (meanTickSpacing ≈ DIVISION): floor = max(DIVISION/8, DIVISION*0.1)
    //   = max(60, 48) = 60; threshold = max(60, DIVISION) = DIVISION (unchanged).
    // Sparse (meanTickSpacing very small horizontalFactor): threshold = floor,
    //   which sits well below kAnchorMinDurationTicks so the short entry passes.
    const int durationFloor = std::max(
        Constants::DIVISION / 8,
        static_cast<int>(meanTickSpacing * 0.1));
    const int effectiveAnchorMinDurationTicks = std::max(
        durationFloor,
        static_cast<int>(std::round(double(kAnchorMinDurationTicks) * horizontalFactor)));

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
    //   (b) duration ≥ effectiveAnchorMinDurationTicks,
    //   (c) ≥ effectiveStaveThreshold chord-bearing staves participating,
    //   (d) analyzeChord winner score ≥ effectiveAnchorMinScore.
    // All four thresholds are texture-adaptive (Iter 69); SATB reproduces the
    // previous SATB-tuned constants.
    if (!chordAnalyzer) {
        return candidates;
    }
    // Iter 72 — relax analyzeChord's distinctPcs gate for greedy-expand only.
    //
    // The analyzer defaults to requiring ≥ 3 distinct pitch classes before it
    // returns any candidate. SATB chorale regions always satisfy this; Corelli
    // trio-sonata dominant entries do not (G unison, G+B / G+Bb dyads at
    // m1b3, m6b3, m8b1, m10b3, m11b3 — all 1-2 PC). Without scoring, those
    // beats can never become anchors. We relax the gate to 1 for our calls
    // only; every other caller in the system keeps the default behaviour.
    analysis::ChordAnalyzerPreferences sparsePrefs = prefs;
    sparsePrefs.minDistinctPcsForCandidate = 1;
    // Iter 94 — internal greedy-expand analyzeChord calls suppress voice-leading
    // step bonuses; the bonus only applies in the final per-region pass.
    sparsePrefs.explorationMode = true;

    for (PlacedRegion& region : candidates) {
        const Fraction regionStart = Fraction::fromTicks(region.startTick);
        const Fraction regionEnd   = Fraction::fromTicks(region.endTick);

        if (!isOnBeat(score, regionStart)) {
            continue;
        }
        if ((region.endTick - region.startTick) < effectiveAnchorMinDurationTicks) {
            continue;
        }
        if (countParticipatingStaves(score, regionStart, regionEnd, excludeStaves,
                                     callbacks.staffIsEligible) < effectiveStaveThreshold) {
            continue;
        }

        auto tones = callbacks.collectRegionTones(region.startTick, region.endTick);
        if (tones.empty()) {
            continue;
        }
        analysis::PostScoringGateContext gateCtxAnchor;
        auto chordCands = chordAnalyzer->analyzeChord(
            tones, globalKeyFifths, globalKeyMode, nullptr, sparsePrefs, &gateCtxAnchor);
        if (chordCands.empty()) {
            continue;
        }
        analysis::applyIter8691Pedal(chordCands, gateCtxAnchor, nullptr, sparsePrefs);
        analysis::applyPostScoringGates(chordCands, sparsePrefs, nullptr, gateCtxAnchor);
        const double winnerScore = chordCands[0].identity.score;
        if (winnerScore < effectiveAnchorMinScore) {
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
        char buf[200];
        std::snprintf(buf, sizeof(buf),
                      "Round 1 anchor: beat=%d dur>=%dtk voice>=%d score=%.3f>=%.3f",
                      beatNum, effectiveAnchorMinDurationTicks,
                      effectiveStaveThreshold, winnerScore, effectiveAnchorMinScore);
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
                nullptr, placed.front(), 2, score, excludeStaves, sparsePrefs,
                chordAnalyzer, globalKeyFifths, globalKeyMode, callbacks,
                effectiveRound2MinScore, effectiveAnchorMinDurationTicks);
    }
    for (size_t i = 0; i + 1 < placed.size(); ++i) {
        if (placed[i]->endTick < placed[i + 1]->startTick) {
            fillGap(candidates, placed[i]->endTick, placed[i + 1]->startTick,
                    placed[i], placed[i + 1], 2, score, excludeStaves, sparsePrefs,
                    chordAnalyzer, globalKeyFifths, globalKeyMode, callbacks,
                    effectiveRound2MinScore, effectiveAnchorMinDurationTicks);
        }
    }
    if (!placed.empty() && placed.back()->endTick < endTick.ticks()) {
        fillGap(candidates, placed.back()->endTick, endTick.ticks(),
                placed.back(), nullptr, 2, score, excludeStaves, sparsePrefs,
                chordAnalyzer, globalKeyFifths, globalKeyMode, callbacks,
                effectiveRound2MinScore, effectiveAnchorMinDurationTicks);
    }

    // Iter 73 Fix B — head-gap synthesis safety net.
    //
    // If Round 1 + Round 2 produced no placed region covering the start
    // of the analysis window, synthesize one covering region from the
    // tones in the uncovered head span. The analysis window was
    // requested for a reason; leaving its head uncovered is always wrong.
    int firstPlacedStart = endTick.ticks();
    for (const auto& r : candidates) {
        if (r.round >= 1) {
            firstPlacedStart = r.startTick;
            break;
        }
    }
    if (firstPlacedStart > startTick.ticks()) {
        const auto headTones = callbacks.collectRegionTones(
            startTick.ticks(), firstPlacedStart);
        if (!headTones.empty()) {
            analysis::PostScoringGateContext gateCtxHead;
            auto headCands = chordAnalyzer->analyzeChord(
                headTones, globalKeyFifths, globalKeyMode, nullptr, sparsePrefs, &gateCtxHead);
            if (!headCands.empty()) {
                analysis::applyIter8691Pedal(headCands, gateCtxHead, nullptr, sparsePrefs);
                analysis::applyPostScoringGates(headCands, sparsePrefs, nullptr, gateCtxHead);
            }
            if (!headCands.empty() && headCands[0].identity.score > 0.0) {
                PlacedRegion headRegion;
                headRegion.startTick      = startTick.ticks();
                headRegion.endTick        = firstPlacedStart;
                headRegion.round          = 2;
                headRegion.confidence     = headCands[0].identity.score;
                headRegion.isAnchor       = false;
                headRegion.rootPitchClass = headCands[0].identity.rootPc;
                headRegion.bassPitchClass = headCands[0].identity.bassPc;
                headRegion.quality        = qualityToString(headCands[0].identity.quality);
                char buf[200];
                std::snprintf(buf, sizeof(buf),
                              "head-gap-synthesized: [%d,%d) score=%.3f",
                              headRegion.startTick, headRegion.endTick,
                              headRegion.confidence);
                headRegion.reason = buf;

                // Iter 74 Fix B — key-tonic prior in head-gap synthesis.
                // In a tonal opening without a confirmed anchor, the tonic
                // is the statistically dominant harmony. Asserting a
                // non-tonic chord requires clear evidence (margin >=
                // kHeadGapTonicPreferenceMargin). When the margin is
                // thin, prefer a tonic-rooted alternative if present
                // among headCands, or fall back to the modal tonic
                // quality (Major for major keys, Minor for minor keys).
                const int ionianTonicPc
                    = analysis::ionianTonicPcFromFifths(globalKeyFifths);
                const int tonicPc
                    = (ionianTonicPc
                       + analysis::keyModeTonicOffset(globalKeyMode)) % 12;
                const bool resultIsTonic = (headRegion.rootPitchClass == tonicPc);
                const double headRunnerUp = (headCands.size() > 1)
                    ? headCands[1].identity.score : 0.0;
                const double headMargin
                    = headCands[0].identity.score - headRunnerUp;
                static constexpr double kHeadGapTonicPreferenceMargin = 0.4;

                if (!resultIsTonic && headMargin < kHeadGapTonicPreferenceMargin) {
                    int overrideIdx = -1;
                    for (size_t k = 1; k < headCands.size(); ++k) {
                        if (headCands[k].identity.rootPc == tonicPc) {
                            overrideIdx = static_cast<int>(k);
                            break;
                        }
                    }
                    if (overrideIdx >= 0) {
                        const auto& alt = headCands[static_cast<size_t>(overrideIdx)];
                        headRegion.rootPitchClass = alt.identity.rootPc;
                        headRegion.bassPitchClass = alt.identity.bassPc;
                        headRegion.quality        = qualityToString(alt.identity.quality);
                        headRegion.confidence     = alt.identity.score;
                    } else {
                        const auto modalQuality
                            = analysis::keyModeIsMajor(globalKeyMode)
                            ? analysis::ChordQuality::Major
                            : analysis::ChordQuality::Minor;
                        headRegion.rootPitchClass = tonicPc;
                        headRegion.bassPitchClass = tonicPc;
                        headRegion.quality        = qualityToString(modalQuality);
                    }
                    std::snprintf(buf, sizeof(buf),
                                  "head-gap-tonic-prior: [%d,%d) margin=%.3f<%.2f tonicPc=%d",
                                  headRegion.startTick, headRegion.endTick,
                                  headMargin, kHeadGapTonicPreferenceMargin,
                                  tonicPc);
                    headRegion.reason = buf;
                }

                candidates.insert(candidates.begin(), std::move(headRegion));
            }
        }
    }

    // Tail-gap synthesis — symmetric safety net for the end of the window.
    int lastPlacedEnd = startTick.ticks();
    for (auto it = candidates.rbegin(); it != candidates.rend(); ++it) {
        if (it->round >= 1) {
            lastPlacedEnd = it->endTick;
            break;
        }
    }
    if (lastPlacedEnd < endTick.ticks()) {
        const auto tailTones = callbacks.collectRegionTones(
            lastPlacedEnd, endTick.ticks());
        if (!tailTones.empty()) {
            analysis::PostScoringGateContext gateCtxTail;
            auto tailCands = chordAnalyzer->analyzeChord(
                tailTones, globalKeyFifths, globalKeyMode, nullptr, sparsePrefs, &gateCtxTail);
            if (!tailCands.empty()) {
                analysis::applyIter8691Pedal(tailCands, gateCtxTail, nullptr, sparsePrefs);
                analysis::applyPostScoringGates(tailCands, sparsePrefs, nullptr, gateCtxTail);
            }
            if (!tailCands.empty() && tailCands[0].identity.score > 0.0) {
                PlacedRegion tailRegion;
                tailRegion.startTick      = lastPlacedEnd;
                tailRegion.endTick        = endTick.ticks();
                tailRegion.round          = 2;
                tailRegion.confidence     = tailCands[0].identity.score;
                tailRegion.isAnchor       = false;
                tailRegion.rootPitchClass = tailCands[0].identity.rootPc;
                tailRegion.bassPitchClass = tailCands[0].identity.bassPc;
                tailRegion.quality        = qualityToString(tailCands[0].identity.quality);
                char buf[200];
                std::snprintf(buf, sizeof(buf),
                              "tail-gap-synthesized: [%d,%d) score=%.3f",
                              tailRegion.startTick, tailRegion.endTick,
                              tailRegion.confidence);
                tailRegion.reason = buf;
                candidates.push_back(std::move(tailRegion));
            }
        }
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
