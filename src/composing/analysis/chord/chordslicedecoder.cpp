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

#include "chordslicedecoder.h"

#include <algorithm>
#include <limits>
#include <optional>

#include "function/harmonicfunctionlayer.h"            // ScoringSnapshot/ScoringCell (cube) + bassIsTemplateChordTone
#include "composing/analysis/engravingbridge/regiontonecollector.h"   // weightedPcView (indexed window)
#include "composing/analysis/scoreharvest/metricweights.h"            // regionMetricWeightForOnsetTick (indexed per-note beat weight)

namespace mu::composing::analysis::chordslice {

namespace {

constexpr double NEG_INF = -std::numeric_limits<double>::infinity();

/// Confidence reported when a slice has no DIFFERENT (root, quality) candidate to
/// compare against — effectively certain (mirrors the L3 single-state sentinel).
constexpr double kNoCompetitorConfidence = 1.0e3;

/// The cell's vertical fit score, BEFORE any progression signal — exactly the
/// value applyHarmonicFunction ranks by on the null-context path (no rootContinuity
/// / resolution / inversion / w_seq folded in, because decode() passes no context):
///   (basisIndep + basisDep) × complexityFactor × augFactor + wCompleteBonus.
/// Identical to DiagnosticOracleCell::verticalScore (chordanalyzer.h) — the one
/// score formula, not a second scorer.
double verticalScore(const function::ScoringCell& cell)
{
    return (cell.basisIndep + cell.basisDep) * cell.complexityFactor * cell.augFactor
           + cell.wCompleteBonus;
}

/// Strict weak ordering for ranking candidates: higher vertical score first;
/// ties broken by template index (lower = preferred, matching the scorer's own
/// tiePriority tie-break), then root pc, then bass pc — fully deterministic.
bool candidateBetter(const ChordSliceCandidate& a, const ChordSliceCandidate& b)
{
    if (a.score != b.score) {
        return a.score > b.score;
    }
    if (a.tiePriority != b.tiePriority) {
        return a.tiePriority < b.tiePriority;
    }
    if (a.rootPc != b.rootPc) {
        return a.rootPc < b.rootPc;
    }
    return a.bassPc < b.bassPc;
}

bool sameChordVoicing(const ChordSliceCandidate& a, const ChordSliceCandidate& b)
{
    return a.rootPc == b.rootPc && a.quality == b.quality && a.bassPc == b.bassPc;
}

bool sameChordSymbol(const ChordSliceCandidate& a, const ChordSliceCandidate& b)
{
    return a.rootPc == b.rootPc && a.quality == b.quality;   // ignores bass/inversion
}

/// Eligible sounding notes in [startTick, endTick), projected to FocalNote — the
/// INDEXED per-note view membership reads (NoteModel::overlapping, NOT the aggregated
/// pc view; design §1). Same eligibility filter as weightedPcView / soundingAt
/// (plays && visible && staffEligible && !grace, staff not excluded), so the focal pc
/// set matches the grader's soundingPitchClasses. The metric weight is the indexed,
/// prefs-free per-note beat weight (scoreharvest::regionMetricWeightForOnsetTick).
std::vector<FocalNote> eligibleNotesInSpan(const notemodel::NoteModel& model,
                                           int startTick, int endTick,
                                           const std::set<std::size_t>& excludeStaves)
{
    const mu::engraving::Score* sc = model.score();
    const double div = static_cast<double>(mu::engraving::Constants::DIVISION);
    std::vector<FocalNote> out;
    for (const notemodel::NoteEvent* ne : model.overlapping(startTick, endTick)) {
        if (!(ne->plays && ne->visible && ne->staffEligible && !ne->isGrace
              && !excludeStaves.count(static_cast<std::size_t>(ne->staff)))) {
            continue;
        }
        FocalNote f;
        f.pitch        = ne->pitch;
        f.onset        = ne->onset;
        f.release      = ne->release;
        f.voice        = ne->voice;
        f.metricWeight = scoreharvest::regionMetricWeightForOnsetTick(sc, ne->onset);
        f.durationQn   = ne->duration / div;
        out.push_back(f);
    }
    return out;
}

/// Distinct pitch classes among a focal-note set.
int distinctPcCount(const std::vector<FocalNote>& notes)
{
    bool seen[12] = {};
    int n = 0;
    for (const FocalNote& f : notes) {
        const int pc = f.pc();
        if (!seen[pc]) { seen[pc] = true; ++n; }
    }
    return n;
}

/// The adaptive lazy-extend window (design §2/§3). The window starts at the narrow
/// base (±contextSlices) and grows one slice each side at a time, stopping as soon as
/// it holds >= minHarmonyPcs distinct pitch classes (the prevailing harmony is in
/// view) OR reaches ±maxContextSlices (bounded by one harmony's worth of figuration).
/// Reuses the INDEXED NoteModel::overlapping for the distinct-pc probe — no new window
/// builder. Because the slices tile the domain contiguously, a half-width `c` window is
/// [slices[t-c].start, slices[t+c].end).
void adaptiveWindow(const std::vector<slicing::Slice>& slices,
                    const notemodel::NoteModel& model, int t,
                    const ChordSliceDecoderPreferences& dp,
                    const std::set<std::size_t>& excludeStaves,
                    int& winStart, int& winEnd)
{
    const int n = static_cast<int>(slices.size());
    const int base = std::max(0, dp.contextSlices);
    const int maxc = std::max(base, dp.maxContextSlices);

    auto spanFor = [&](int half, int& a, int& b) {
        const int lo = std::max(0, t - half);
        const int hi = std::min(n - 1, t + half);
        a = slices[static_cast<std::size_t>(lo)].start;
        b = slices[static_cast<std::size_t>(hi)].end;
    };

    int c = base;
    spanFor(c, winStart, winEnd);
    while (c < maxc
           && distinctPcCount(eligibleNotesInSpan(model, winStart, winEnd, excludeStaves))
              < std::max(1, dp.minHarmonyPcs)) {
        ++c;
        spanFor(c, winStart, winEnd);
    }
}

/// Is `pc` a template tone (root/3rd/5th/7th…) of any of the given (present) chords?
/// Reuses the one chord-tone oracle function::bassIsTemplateChordTone (the kMasks
/// table) — no second interval set.
bool isChordToneOfAny(const std::vector<const ChordSliceCandidate*>& chords, int pc)
{
    for (const ChordSliceCandidate* c : chords) {
        if (c && function::bassIsTemplateChordTone(c->rootPc, c->tiePriority, pc)) {
            return true;
        }
    }
    return false;
}

/// Inherit-consistency (design §5 step 4, the "inherit on insufficiency" fallback):
/// are ALL of the slice's focal notes consistent with the prevailing chord? For
/// Step-1 (G1) this is the conservative TEMPLATE-ONLY reading — every focal pitch
/// class is a template tone of the prevailing chord (covers the spec's documented
/// inherit cases: the single C#-over-A-major thin slice whose C# is the chord's
/// third, and the dyad that is a subset of the prevailing chord). The looser
/// "... or a stepwise embellishment of it" relaxation depends on the membership
/// stepwise machinery and is deferred to the G2 membership refinement (Step 2), so
/// G1 stays decoupled from the still-flat membership ladder.
bool notesConsistentWithPrevailing(const ChordSliceCandidate& prevailing,
                                   const std::vector<FocalNote>& focal)
{
    for (const FocalNote& f : focal) {
        if (!function::bassIsTemplateChordTone(prevailing.rootPc, prevailing.tiePriority, f.pc())) {
            return false;
        }
    }
    return true;
}

/// Metric salience of a focal note: beat-weight [0.5,1] scaled by how close it is to
/// full length. A weak / short note is embellishment-like (design §1).
double noteSalience(const FocalNote& f, const ChordSliceDecoderPreferences& dp)
{
    const double ref = std::max(1e-6, dp.membershipReferenceDurationQn);
    const double durFactor = std::min(1.0, f.durationQn / ref);
    return f.metricWeight * durFactor;
}

inline bool isSemitoneStep(int p1, int p2)
{
    const int d = std::abs(p1 - p2);
    return d == 1 || d == 2;   // chromatic step (minor/major 2nd) — melodic passing/neighbour
}

/// Local stepwise treatment of a focal note within the window (design §1): a
/// passing/neighbour tone (approached AND left by step, between chord tones) or a
/// suspension (a tone held from the previous chord that resolves DOWN by step to a
/// chord tone). Per-voice / melodic; uses the neighbour chords as context only — never
/// a chord-to-chord transition cost (that is Layer 5). prevChord / nextChord may be
/// absent (boundary / two-pass-off) — then only the cues that do not need them fire.
bool isStepwiseTreated(const FocalNote& note,
                       const std::vector<FocalNote>& window,
                       const ChordSliceCandidate& chord,
                       const ChordSliceCandidate* prevChord,
                       const ChordSliceCandidate* nextChord,
                       const ChordSliceDecoderPreferences& dp)
{
    const int tol = std::max(0, dp.stepwiseGapToleranceTicks);

    // Nearest same-voice melodic predecessor (ends at/just before this onset) and
    // successor (starts at/just after this release).
    const FocalNote* pred = nullptr;
    const FocalNote* succ = nullptr;
    for (const FocalNote& w : window) {
        if (w.voice != note.voice || (&w == &note)) {
            continue;
        }
        if (w.onset == note.onset && w.pitch == note.pitch && w.release == note.release) {
            continue;   // the same note (defensive — window contains focal)
        }
        if (w.release >= note.onset - tol && w.release <= note.onset + tol) {
            if (!pred || w.release > pred->release) { pred = &w; }   // immediate melodic predecessor
        }
        if (w.onset >= note.release - tol && w.onset <= note.release + tol) {
            if (!succ || w.onset < succ->onset) { succ = &w; }       // immediate melodic successor
        }
    }

    const std::vector<const ChordSliceCandidate*> prevOrThis = { prevChord, &chord };
    const std::vector<const ChordSliceCandidate*> thisOrNext = { &chord, nextChord };

    const bool leftToCT = succ && isSemitoneStep(note.pitch, succ->pitch)
                          && isChordToneOfAny(thisOrNext, succ->pc());
    const bool approachedFromCT = pred && isSemitoneStep(pred->pitch, note.pitch)
                                  && isChordToneOfAny(prevOrThis, pred->pc());

    // Passing / neighbour: stepwise in and stepwise out, between chord tones.
    if (approachedFromCT && leftToCT) {
        return true;
    }

    // Suspension: belongs to the previous chord, resolves DOWN by step to a chord tone.
    const bool heldFromPrev = prevChord
                              && function::bassIsTemplateChordTone(prevChord->rootPc,
                                                                   prevChord->tiePriority, note.pc());
    const bool resolvesDown = succ && (note.pitch - succ->pitch) >= 1 && (note.pitch - succ->pitch) <= 2
                              && isChordToneOfAny({ &chord }, succ->pc());
    if (heldFromPrev && resolvesDown) {
        return true;
    }
    return false;
}

/// Run the existing scorer over a slice's window and project the surfaced
/// candidate cube (fn::ScoringSnapshot::cells) to a flat candidate list — one
/// ChordSliceCandidate per (bass × root × template) cell, with its vertical score.
/// This is the generation step (design §4 "candidate generation is the lever"): no
/// second scorer, no re-derivation — analyzeChord's complete cube, surfaced the way
/// the L3 decoder surfaced analyzeKeyMode's 252-candidate dump. Returns empty when
/// the window has too few distinct pitch classes to score (analyzeChord gates).
std::vector<ChordSliceCandidate> candidatesForWindow(
    const RuleBasedChordAnalyzer& analyzer,
    const notemodel::NoteModel& model,
    int winStart, int winEnd,
    int keySignatureFifths, KeySigMode keyMode,
    const ChordAnalyzerPreferences& prefs,
    const std::set<std::size_t>& excludeStaves)
{
    const std::vector<ChordAnalysisTone> tones =
        engravingbridge::weightedPcView(model, winStart, winEnd, excludeStaves,
                                        /*parentStartTick=*/-1,
                                        /*excludeLookAheadOnDenseStart=*/false, prefs);

    function::ScoringSnapshot snapshot;
    analyzer.analyzeChord(tones, keySignatureFifths, keyMode,
                          /*context=*/nullptr, prefs, /*gateCtxOut=*/nullptr, &snapshot);

    std::vector<ChordSliceCandidate> out;
    out.reserve(snapshot.cells.size());
    for (const function::ScoringCell& cell : snapshot.cells) {
        ChordSliceCandidate c;
        c.rootPc      = cell.rootPc;
        c.rootTpc     = (cell.rootPc >= 0 && cell.rootPc < 12)
                        ? snapshot.tpcForPc[static_cast<std::size_t>(cell.rootPc)] : -1;
        c.bassPc      = cell.bassPc;
        c.bassTpc     = cell.bassTpc;
        c.quality     = cell.quality;
        c.tiePriority = cell.tiePriority;
        c.score       = verticalScore(cell);
        out.push_back(c);
    }
    return out;
}

} // namespace

SliceChord ChordSliceDecoder::decideSlice(
    int sliceIndex,
    const std::vector<ChordSliceCandidate>& candidates,
    const std::optional<ChordSliceCandidate>& prevailing,
    const ChordSliceDecoderPreferences& decoderPrefs)
{
    SliceChord sc;
    sc.sliceIndex = sliceIndex;
    if (candidates.empty()) {
        sc.hasChord = false;
        sc.uncertain = true;            // no scorable candidate → treated as uncertain
        sc.decision = SliceDecision::Abstain;   // ... and an abstain (no chord to commit)
        return sc;
    }

    // Rank the complete candidate list (the surfaced cube) deterministically.
    std::vector<ChordSliceCandidate> ranked(candidates);
    std::sort(ranked.begin(), ranked.end(), candidateBetter);

    sc.hasChord = true;
    sc.chosen = ranked.front();

    // Confidence = chosen vertical score − best score over any DIFFERENT (root,
    // quality) chord. An inversion of the SAME chord is not a different chord.
    double bestOther = NEG_INF;
    for (const ChordSliceCandidate& c : ranked) {
        if (!sameChordSymbol(c, sc.chosen)) {
            bestOther = std::max(bestOther, c.score);
        }
    }
    sc.confidence = (bestOther == NEG_INF) ? kNoCompetitorConfidence
                                           : (sc.chosen.score - bestOther);
    sc.uncertain = sc.confidence < decoderPrefs.uncertaintyMargin;

    // Ranked alternatives: the distinct chord voicings after the chosen, capped at
    // topK, then ∪ the prevailing chord (the L3 incumbent pattern — kept alive as a
    // carried alternative even when it falls below topK, so the membership two-pass
    // in Increment B always has it).
    for (const ChordSliceCandidate& c : ranked) {
        if (sameChordVoicing(c, sc.chosen)) {
            continue;
        }
        const bool dup = std::any_of(sc.alternatives.begin(), sc.alternatives.end(),
                                     [&](const ChordSliceCandidate& a) { return sameChordVoicing(a, c); });
        if (dup) {
            continue;
        }
        if (decoderPrefs.topK > 0 && static_cast<int>(sc.alternatives.size()) >= decoderPrefs.topK) {
            break;
        }
        sc.alternatives.push_back(c);
    }

    // ∪ the prevailing chord. Keep it alive if it is expressible among THIS slice's
    // candidates (its root+quality is scorable here) and is not already carried /
    // the chosen — using this slice's own cube cell (so it has this slice's score).
    if (prevailing.has_value() && !sameChordSymbol(*prevailing, sc.chosen)) {
        const bool alreadyCarried = std::any_of(
            sc.alternatives.begin(), sc.alternatives.end(),
            [&](const ChordSliceCandidate& a) { return sameChordSymbol(a, *prevailing); });
        if (!alreadyCarried) {
            // Prefer the cube cell matching root+quality+bass; fall back to root+quality.
            const ChordSliceCandidate* exact = nullptr;
            const ChordSliceCandidate* symbol = nullptr;
            for (const ChordSliceCandidate& c : ranked) {
                if (sameChordVoicing(c, *prevailing)) { exact = &c; break; }
                if (!symbol && sameChordSymbol(c, *prevailing)) { symbol = &c; }
            }
            if (exact) {
                sc.alternatives.push_back(*exact);
            } else if (symbol) {
                sc.alternatives.push_back(*symbol);
            }
            // If neither — the prevailing chord is not expressible by this slice's
            // pitches — it is genuinely not a candidate here, so it is not forced.
        }
    }

    return sc;
}

MembershipResult ChordSliceDecoder::classifyMembership(
    const ChordSliceCandidate& chord,
    const std::vector<FocalNote>& focal,
    const std::vector<FocalNote>& window,
    const std::optional<ChordSliceCandidate>& prevChord,
    const std::optional<ChordSliceCandidate>& nextChord,
    const ChordSliceDecoderPreferences& dp)
{
    MembershipResult r;
    const ChordSliceCandidate* prevC = prevChord.has_value() ? &*prevChord : nullptr;
    const ChordSliceCandidate* nextC = nextChord.has_value() ? &*nextChord : nullptr;

    // Aggregate per pc: a pc is a chord tone if it is a template tone OR at least one
    // of its focal notes is a chord-tone extension; a non-chord tone only when EVERY
    // focal note of that pc is embellishment-like.
    bool present[12] = {};
    bool anyChordTone[12] = {};

    for (const FocalNote& f : focal) {
        const int pc = f.pc();
        present[pc] = true;

        if (function::bassIsTemplateChordTone(chord.rootPc, chord.tiePriority, pc)) {
            anyChordTone[pc] = true;   // a basic template tone — always a chord tone
            continue;
        }
        // An "extra" note (pc not in the chord's basic template). Embellishment-like —
        // weak metric salience OR locally stepwise — ⇒ non-chord tone; otherwise a
        // chord-tone extension (the sustained strong 6th/9th that "falls out", design §5)
        // and the candidate is charged its salience as an implausible chord tone it needs.
        const double sal = noteSalience(f, dp);
        const bool weak = sal < dp.membershipSalienceThreshold;
        const bool stepwise = isStepwiseTreated(f, window, chord, prevC, nextC, dp);
        if (weak || stepwise) {
            // non-chord tone — no penalty (the chord explains it as an embellishment).
        } else {
            anyChordTone[pc] = true;            // chord-tone extension
            r.implausibilityPenalty += sal;     // a structural note outside the basic template
        }
    }

    for (int pc = 0; pc < 12; ++pc) {
        if (!present[pc]) {
            continue;
        }
        if (anyChordTone[pc]) {
            r.chordTonePcs.push_back(pc);
        } else {
            r.nonChordTonePcs.push_back(pc);
        }
    }
    return r;
}

int ChordSliceDecoder::templateTonePresenceCount(const ChordSliceCandidate& chord,
                                                 const std::vector<FocalNote>& focal)
{
    bool counted[12] = {};
    int n = 0;
    for (const FocalNote& f : focal) {
        const int pc = f.pc();
        if (!counted[pc] && function::bassIsTemplateChordTone(chord.rootPc, chord.tiePriority, pc)) {
            counted[pc] = true;
            ++n;
        }
    }
    return n;
}

void ChordSliceDecoder::applyCommitDecision(
    SliceChord& sc,
    const std::vector<FocalNote>& focal,
    const std::optional<ChordSliceCandidate>& prevailing,
    const ChordSliceDecoderPreferences& dp)
{
    if (!dp.enableCommitDecision) {
        // Pre-G1 always-commit behaviour: leave the slice exactly as decideSlice left
        // it (the empty-slice abstain set in decideSlice is preserved).
        return;
    }

    // No scorable candidate → abstain (decideSlice already cleared hasChord).
    if (!sc.hasChord) {
        sc.decision = SliceDecision::Abstain;
        return;
    }

    // Sufficiency — does the slice contain enough of the chosen chord's OWN template
    // tones (a complete triad's worth) to fix it? The phantom-root guard: a candidate
    // whose root/3rd/5th are not actually present cannot reach the count.
    const int present = templateTonePresenceCount(sc.chosen, focal);
    const bool sufficient = present >= std::max(1, dp.sufficiencyChordTones);
    const bool marginOk = !sc.uncertain;   // confidence >= uncertaintyMargin

    // Commit: enough independent chord tones AND a clear-enough winner.
    if (sufficient && marginOk) {
        sc.decision = SliceDecision::Commit;
        return;
    }

    // Inherit: a thin (insufficient) slice whose notes are all consistent with the
    // prevailing chord carries it forward, rather than naming a phantom. (A slice that
    // is sufficient but merely loses on margin is NOT inherited — it abstains.)
    if (!sufficient && prevailing.has_value()
        && notesConsistentWithPrevailing(*prevailing, focal)) {
        sc.chosen = *prevailing;
        sc.decision = SliceDecision::Inherit;
        sc.uncertain = false;   // an inherited prevailing chord is a committed answer
        return;
    }

    // Abstain: insufficient with no consistent prevailing, or sufficient but low margin.
    // No new symbol is committed (the no-chord / open marker); the competing readings
    // (alternatives) are kept for Architectural Layer 5.
    sc.decision = SliceDecision::Abstain;
    sc.hasChord = false;
    sc.uncertain = true;
}

namespace {

// Per-slice work cached across the two passes (the candidate cube + the focal and
// windowed per-note streams + the provisional pass-1 chord). Pass 2 re-ranks and
// classifies WITHOUT re-running the scorer (no O(N²); the analyzeChord cost is paid
// once per slice in pass 1).
struct SliceWork {
    std::vector<ChordSliceCandidate> cands;
    std::vector<FocalNote> focal;     ///< notes in [slice.start, slice.end)
    std::vector<FocalNote> window;    ///< notes in the adaptive window (focal ⊆ window)
    SliceChord pass1;                 ///< provisional chord (own notes + key prior)
    bool built = false;
};

// Build a slice's work + its provisional pass-1 chord (context-free per slice — the
// chosen chord depends only on the slice's own window, not on any decision).
SliceWork buildSliceWork(const RuleBasedChordAnalyzer& analyzer,
                         const std::vector<slicing::Slice>& slices,
                         const notemodel::NoteModel& model, int t,
                         int keyFifths, KeySigMode keyMode,
                         const ChordAnalyzerPreferences& prefs,
                         const ChordSliceDecoderPreferences& dp,
                         const std::set<std::size_t>& excludeStaves)
{
    SliceWork w;
    int ws = 0, we = 0;
    adaptiveWindow(slices, model, t, dp, excludeStaves, ws, we);
    w.cands  = candidatesForWindow(analyzer, model, ws, we, keyFifths, keyMode, prefs, excludeStaves);
    w.window = eligibleNotesInSpan(model, ws, we, excludeStaves);
    w.focal  = eligibleNotesInSpan(model, slices[static_cast<std::size_t>(t)].start,
                                   slices[static_cast<std::size_t>(t)].end, excludeStaves);
    w.pass1  = ChordSliceDecoder::decideSlice(t, w.cands, std::nullopt, dp);
    w.built  = true;
    return w;
}

// Finalize a slice (pass 2): apply the membership feedback to the candidate scores,
// re-decide, then classify the chosen chord's focal notes. prevC/nextC are the
// provisional neighbour chords (design §4 two-pass).
SliceChord finalizeSlice(int t, const SliceWork& w,
                         const std::optional<ChordSliceCandidate>& prevC,
                         const std::optional<ChordSliceCandidate>& nextC,
                         const std::optional<ChordSliceCandidate>& prevailing,
                         const ChordSliceDecoderPreferences& dp)
{
    std::vector<ChordSliceCandidate> adj = w.cands;
    if (dp.membershipPenaltyWeight != 0.0) {
        for (ChordSliceCandidate& c : adj) {
            const MembershipResult m =
                ChordSliceDecoder::classifyMembership(c, w.focal, w.window, prevC, nextC, dp);
            c.score -= dp.membershipPenaltyWeight * m.implausibilityPenalty;
        }
    }
    SliceChord sc = ChordSliceDecoder::decideSlice(t, adj, prevailing, dp);
    // G1 — commit / inherit / abstain (design §4 step 3, §5 step 4). Decided BEFORE
    // membership so the per-note classification reflects the FINAL chord (the inherited
    // prevailing chord on Inherit; nothing on Abstain).
    ChordSliceDecoder::applyCommitDecision(sc, w.focal, prevailing, dp);
    if (sc.hasChord) {
        const MembershipResult mc =
            ChordSliceDecoder::classifyMembership(sc.chosen, w.focal, w.window, prevC, nextC, dp);
        sc.chordTonePcs    = mc.chordTonePcs;
        sc.nonChordTonePcs = mc.nonChordTonePcs;
    }
    return sc;
}

// Decode (and re-decode) driver over the output range [outFirst, outLast].
//   * Pass 1 is computed over the slightly wider span the pass-2 neighbours + the
//     prevailing chain of `outFirst` need ([outFirst-2 .. outLast+1]); because pass-1
//     and pass-2 chosen chords are context-free w.r.t. the prevailing incumbent, this
//     reproduces a full decode's slices EXACTLY (the redecodeRange contract).
//   * With membership disabled the path collapses to pass 1 with the L3 incumbent
//     chain (the Increment-A behaviour, modulo the adaptive window).
std::vector<SliceChord> decodeWindowed(
    const std::vector<slicing::Slice>& slices, const notemodel::NoteModel& model,
    int keyFifths, KeySigMode keyMode, const ChordAnalyzerPreferences& chordPrefs,
    const ChordSliceDecoderPreferences& dp, const std::set<std::size_t>& excludeStaves,
    int outFirst, int outLast)
{
    const int T = static_cast<int>(slices.size());
    std::vector<SliceChord> out;
    if (T == 0 || outFirst < 0 || outLast >= T || outFirst > outLast) {
        return out;
    }
    out.reserve(static_cast<std::size_t>(outLast - outFirst + 1));

    ChordAnalyzerPreferences prefs = chordPrefs;
    prefs.minDistinctPcsForCandidate = std::max(1, dp.minDistinctPcs);
    const RuleBasedChordAnalyzer analyzer;

    if (!dp.enableMembership) {
        // Pass-1 only, with the incumbent (∪ prevailing) chain — one slice of look-back
        // recovers the prevailing chord of outFirst.
        const int lo = std::max(0, outFirst - 1);
        std::optional<ChordSliceCandidate> prevailing;
        for (int t = lo; t <= outLast; ++t) {
            const SliceWork w = buildSliceWork(analyzer, slices, model, t, keyFifths, keyMode,
                                               prefs, dp, excludeStaves);
            SliceChord sc = ChordSliceDecoder::decideSlice(t, w.cands, prevailing, dp);
            ChordSliceDecoder::applyCommitDecision(sc, w.focal, prevailing, dp);   // G1
            if (sc.hasChord) { prevailing = sc.chosen; }
            if (t >= outFirst) { out.push_back(std::move(sc)); }
        }
        return out;
    }

    // Membership two-pass. Pass 1 over the span the pass-2 neighbours + the prevailing
    // chain of outFirst need.
    const int p1lo = std::max(0, outFirst - 2);
    const int p1hi = std::min(T - 1, outLast + 1);
    std::vector<SliceWork> work(static_cast<std::size_t>(p1hi - p1lo + 1));
    for (int t = p1lo; t <= p1hi; ++t) {
        work[static_cast<std::size_t>(t - p1lo)] =
            buildSliceWork(analyzer, slices, model, t, keyFifths, keyMode, prefs, dp, excludeStaves);
    }
    auto pass1ChosenAt = [&](int t) -> std::optional<ChordSliceCandidate> {
        if (t < p1lo || t > p1hi) { return std::nullopt; }
        const SliceWork& w = work[static_cast<std::size_t>(t - p1lo)];
        if (w.built && w.pass1.hasChord) { return w.pass1.chosen; }
        return std::nullopt;
    };

    // Pass 2 from outFirst-1 (only to seed the prevailing chain of outFirst); emit
    // from outFirst.
    const int p2lo = std::max(0, outFirst - 1);
    std::optional<ChordSliceCandidate> prevailing;
    for (int t = p2lo; t <= outLast; ++t) {
        const std::optional<ChordSliceCandidate> prevC =
            dp.twoPass ? pass1ChosenAt(t - 1) : std::nullopt;
        const std::optional<ChordSliceCandidate> nextC =
            dp.twoPass ? pass1ChosenAt(t + 1) : std::nullopt;
        const SliceWork& w = work[static_cast<std::size_t>(t - p1lo)];
        SliceChord sc = finalizeSlice(t, w, prevC, nextC, prevailing, dp);
        if (sc.hasChord) { prevailing = sc.chosen; }
        if (t >= outFirst) { out.push_back(std::move(sc)); }
    }
    return out;
}

} // namespace

std::vector<SliceChord> ChordSliceDecoder::decode(
    const std::vector<slicing::Slice>& slices,
    const notemodel::NoteModel& noteModel,
    int keySignatureFifths,
    KeySigMode keyMode,
    const ChordAnalyzerPreferences& chordPrefs,
    const ChordSliceDecoderPreferences& decoderPrefs,
    const std::set<std::size_t>& excludeStaves)
{
    const int T = static_cast<int>(slices.size());
    if (T == 0) {
        return {};
    }
    return decodeWindowed(slices, noteModel, keySignatureFifths, keyMode, chordPrefs,
                          decoderPrefs, excludeStaves, 0, T - 1);
}

std::vector<SliceChord> ChordSliceDecoder::redecodeRange(
    const std::vector<slicing::Slice>& slices,
    const notemodel::NoteModel& noteModel,
    int keySignatureFifths,
    KeySigMode keyMode,
    int first, int last,
    const ChordAnalyzerPreferences& chordPrefs,
    const ChordSliceDecoderPreferences& decoderPrefs,
    const std::set<std::size_t>& excludeStaves)
{
    return decodeWindowed(slices, noteModel, keySignatureFifths, keyMode, chordPrefs,
                          decoderPrefs, excludeStaves, first, last);
}

} // namespace mu::composing::analysis::chordslice
