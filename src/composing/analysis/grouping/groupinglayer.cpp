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

#include "composing/analysis/grouping/groupinglayer.h"

#include <algorithm>
#include <map>

namespace mu::composing::analysis::grouping {

namespace {

// A surviving punctuation-span cut: the interior boundary tick that opens/closes a
// span, its provenance, and (if a §5.1-a codetta fired at it) the codetta annexe end.
struct Cut {
    int tick = 0;
    double strength = 0.0;
    BoundaryCue cue = BoundaryCue::Unknown;
    BoundaryScope scope = BoundaryScope::Unknown;
    int codettaEndTick = -1;   ///< §5.1-a: the span ending HERE has a codetta [tick, codettaEndTick), else -1
};

// §5.1 build the ordered, dedup'd interior boundary set, then apply the §5.1-a codetta
// refinement (default-inert: params.codettaWindowTicks == 0 → never fires, so the cut
// set is the L1.5 picked set restricted to the analysed span's interior, verbatim).
std::vector<Cut> buildCuts(const std::vector<BoundaryInput>& boundaries,
                           const AnalyzedSpan& span,
                           const GroupingParams& params)
{
    // Dedup by tick keeping the max strength (deterministic); keep only interior ticks
    // (a boundary AT span.start/end is an edge marker, not an interior cut).
    std::map<int, Cut> byTick;
    for (const BoundaryInput& b : boundaries) {
        if (b.tick <= span.startTick || b.tick >= span.endTick) {
            continue;
        }
        auto it = byTick.find(b.tick);
        if (it == byTick.end() || b.strength > it->second.strength) {
            byTick[b.tick] = Cut{ b.tick, b.strength, b.cue, b.scope, -1 };
        }
    }
    std::vector<Cut> ordered;
    ordered.reserve(byTick.size());
    for (const auto& [tick, c] : byTick) {
        ordered.push_back(c);
    }

    // §5.1-a codetta refinement. Two boundaries close together, strong-then-weak: the
    // STRONGER peak is the punctuation-span's structural end; the WEAKER peak does not
    // open a new span (it is suppressed as a cut); [stronger, weaker) is the codetta of
    // the span ending at the stronger peak. (Interpretation declared: the flat partition
    // keeps the strong-peak cut and drops the weak-peak cut, recording the codetta annexe —
    // both literal statements of §5.1-a hold and tiling is preserved.) DEFAULT INERT.
    std::vector<Cut> refined;
    refined.reserve(ordered.size());
    for (size_t i = 0; i < ordered.size();) {
        if (i + 1 < ordered.size()
            && params.codettaWindowTicks > 0
            && (ordered[i + 1].tick - ordered[i].tick) <= params.codettaWindowTicks
            && ordered[i].strength > ordered[i + 1].strength + params.codettaStrengthMargin) {
            Cut c = ordered[i];
            c.codettaEndTick = ordered[i + 1].tick;   // the suppressed weak peak = codetta end
            refined.push_back(c);
            i += 2;                                    // drop the weak peak (does not open a new span)
        } else {
            refined.push_back(ordered[i]);
            i += 1;
        }
    }
    return refined;
}

// §5.2 duration-weighted mean of the units' declared boundary key confidences over
// [first,last] (the declared default combiner; NON-INCREASING in the weakest unit —
// direction fixed). Clamped to [0,1] (the U2 boundary form). Empty range ⇒ 0.
double keyAreaConfidence(const std::vector<GroupingUnit>& units, size_t first, size_t last)
{
    double num = 0.0;
    long long den = 0;
    for (size_t i = first; i <= last && i < units.size(); ++i) {
        const long long dur = std::max<long long>(1, units[i].endTick - units[i].startTick);
        const double conf = std::clamp(units[i].keyConfidence, 0.0, 1.0);
        num += conf * static_cast<double>(dur);
        den += dur;
    }
    if (den <= 0) {
        return 0.0;
    }
    return std::clamp(num / static_cast<double>(den), 0.0, 1.0);
}

} // namespace

GroupingLayerOutput
assembleGrouping(const std::vector<GroupingUnit>& units,
                 const std::vector<BoundaryInput>& boundaries,
                 const std::vector<FunctionalCadence>& cadences,
                 const AnalyzedSpan& span,
                 const GroupingParams& params)
{
    GroupingLayerOutput out;
    if (span.endTick <= span.startTick) {
        return out;   // degenerate span → empty grouping
    }

    // A boundary marker sitting EXACTLY at the analysed-span start / end (an edge
    // marker, not an interior cut): its presence means the edge is a musical boundary,
    // so the edge group is NOT clipped even at a selection edge.
    bool boundaryAtStart = false, boundaryAtEnd = false;
    for (const BoundaryInput& b : boundaries) {
        if (b.tick == span.startTick) { boundaryAtStart = true; }
        if (b.tick == span.endTick)   { boundaryAtEnd = true; }
    }

    // ── §5.1 punctuation-span partition (+ §5.1-a codetta, default-inert) ──
    const std::vector<Cut> cuts = buildCuts(boundaries, span, params);

    // Edge ticks: [span.start, cut0, cut1, …, span.end]. Spans tile [edge[k], edge[k+1]).
    std::vector<int> edges;
    edges.reserve(cuts.size() + 2);
    edges.push_back(span.startTick);
    for (const Cut& c : cuts) { edges.push_back(c.tick); }
    edges.push_back(span.endTick);

    for (size_t k = 0; k + 1 < edges.size(); ++k) {
        PunctuationSpan ps;
        ps.startTick = edges[k];
        ps.endTick = edges[k + 1];
        ps.structuralEndTick = ps.endTick;

        // Opening provenance: an interior cut (k>0) supplies it; the first span opens at
        // span.start — a musical boundary iff one sits there, else clipped iff the start
        // is a selection edge (a true score start is neither a cut nor clipped).
        if (k > 0) {
            const Cut& oc = cuts[k - 1];
            ps.openCue = oc.cue; ps.openScope = oc.scope; ps.openStrength = oc.strength;
        } else if (!boundaryAtStart && span.startIsSelectionEdge) {
            ps.clippedAtStart = true;
        }

        // Closing provenance + the §5.1-a codetta annexe. An interior close (edges[k+1]
        // is cuts[k]) supplies provenance; the last span (k == cuts.size()) closes at
        // span.end — a musical boundary iff one sits there, else clipped iff a selection edge.
        if (k < cuts.size()) {
            const Cut& cc = cuts[k];
            ps.closeCue = cc.cue; ps.closeScope = cc.scope; ps.closeStrength = cc.strength;
            ps.codettaEndTick = cc.codettaEndTick;
        } else if (!boundaryAtEnd && span.endIsSelectionEdge) {
            ps.clippedAtEnd = true;
        }
        out.punctuationSpans.push_back(ps);
    }

    // ── Assign units to punctuation-spans (by unit start tick) + §5.4 residual carry ──
    for (size_t ui = 0; ui < units.size(); ++ui) {
        const GroupingUnit& u = units[ui];
        for (PunctuationSpan& ps : out.punctuationSpans) {
            if (u.startTick >= ps.startTick && u.startTick < ps.endTick) {
                if (ps.firstUnit < 0) { ps.firstUnit = static_cast<int>(ui); }
                ps.lastUnit = static_cast<int>(ui);
                if (u.openMark) { ps.carriesOpenMark = true; }
                break;
            }
        }
    }

    // ── §5.3 cadence-to-punctuation-span alignment ──
    // A cadence closes the span whose ending boundary lies at its arrival tick, or
    // within the window AFTER it (arrival may slightly precede the notated span end).
    // Among candidates the NEAREST boundary wins; ties → stronger tonic vote (declared).
    out.cadenceAlignments.reserve(cadences.size());
    for (size_t ci = 0; ci < cadences.size(); ++ci) {
        const FunctionalCadence& cad = cadences[ci];
        int bestSpan = -1;
        int bestGap = 0;
        for (size_t si = 0; si < out.punctuationSpans.size(); ++si) {
            const int end = out.punctuationSpans[si].endTick;
            const int gap = end - cad.arrivalTick;
            if (gap >= 0 && gap <= params.alignmentWindowTicks) {
                if (bestSpan < 0 || gap < bestGap) {
                    bestSpan = static_cast<int>(si);
                    bestGap = gap;
                }
            }
        }
        CadenceAlignment al;
        al.cadenceIndex = static_cast<int>(ci);
        if (bestSpan >= 0) {
            al.kind = CadenceAlignmentKind::ClosesSpan;
            al.punctuationSpanIndex = bestSpan;
            PunctuationSpan& ps = out.punctuationSpans[static_cast<size_t>(bestSpan)];
            // Keep the closing cadence whose arrival is nearest the boundary; tie → the
            // stronger tonic vote. (§5.3 "the closing cadence" is singular.)
            if (ps.closingCadenceIndex < 0) {
                ps.closingCadenceIndex = static_cast<int>(ci);
            } else {
                const FunctionalCadence& cur = cadences[static_cast<size_t>(ps.closingCadenceIndex)];
                const int curGap = ps.endTick - cur.arrivalTick;
                if (bestGap < curGap
                    || (bestGap == curGap && cad.tonicVote > cur.tonicVote)) {
                    ps.closingCadenceIndex = static_cast<int>(ci);
                }
            }
        } else {
            al.kind = CadenceAlignmentKind::Internal;   // surfaced, never snapped/discarded
        }
        out.cadenceAlignments.push_back(al);
    }

    // §5.1-amendment extension cue: a span reaching a selection END edge with NO closing
    // boundary AND no closing cadence — the signal that widening the selection completes it.
    if (!out.punctuationSpans.empty()) {
        PunctuationSpan& last = out.punctuationSpans.back();
        if (last.clippedAtEnd && last.closingCadenceIndex < 0) {
            last.extensionCue = true;
        }
    }

    // ── §5.2 key-area grouping (independent flat partition; NOT nested — §9-D5) ──
    for (size_t ui = 0; ui < units.size();) {
        const int tonic = units[ui].localTonicPc;
        const bool minor = units[ui].localMinorMode;
        size_t uj = ui;
        while (uj + 1 < units.size()
               && units[uj + 1].localTonicPc == tonic
               && units[uj + 1].localMinorMode == minor) {
            ++uj;
        }
        KeyAreaSpan ka;
        ka.startTick = units[ui].startTick;
        ka.endTick = units[uj].endTick;
        ka.localTonicPc = tonic;
        ka.localMinorMode = minor;
        ka.confidence = keyAreaConfidence(units, ui, uj);
        ka.firstUnit = static_cast<int>(ui);
        ka.lastUnit = static_cast<int>(uj);
        for (size_t k = ui; k <= uj; ++k) {
            if (units[k].openMark) { ka.carriesOpenMark = true; break; }
        }
        // Edge clip (§5.2 "the same mark applies to an edge key-area"): the first/last
        // area at a SELECTION edge with no musical boundary there is clipped.
        if (ka.startTick == span.startTick && !boundaryAtStart && span.startIsSelectionEdge) {
            ka.clippedAtStart = true;
        }
        if (ka.endTick == span.endTick && !boundaryAtEnd && span.endIsSelectionEdge) {
            ka.clippedAtEnd = true;
        }
        out.keyAreas.push_back(ka);
        ui = uj + 1;
    }

    // ── §5.5 recognised-schema hosting: EMPTY absent the recognition consumer ──
    // (Nothing to host in the dormant state; the four core rules stand alone.)

    return out;
}

} // namespace mu::composing::analysis::grouping
