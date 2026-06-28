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
#include "composing/analysis/engravingbridge/spellingview.h"          // lineOfFifths (the shared per-note spelling primitive, G4/C1)
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

/// Number of template tones (root/3rd/5th/7th…) a template carries — the sufficiency
/// DENOMINATOR (design §7: "a full seventh present versus a dyad"). Read off the one
/// source kTemplateIntervals (count of non-(-1) intervals): triads → 3, sevenths → 4,
/// Power → 2. -1 / out-of-range → 0.
int templateToneCount(int tiePriority)
{
    if (tiePriority < 0 || tiePriority >= static_cast<int>(kTemplateCount)) {
        return 0;
    }
    int n = 0;
    for (int interval : kTemplateIntervals[static_cast<std::size_t>(tiePriority)]) {
        if (interval >= 0) { ++n; }
    }
    return n;
}

/// G6 ambiguity cue — do the two readings explain the SAME focal pitch classes? Every
/// focal pc is a template tone of @p a OR @p b, and each of a, b covers at least a triad's
/// worth (>=3) of them. This is the same-collection / share-tone signal (Am6↔F♯ø7,
/// dim7-subset cases): the readings are two namings of one pitch set, separable only by
/// function (design §15-O1). A genuinely-different close reading shares few focal tones
/// and fails this test (→ RelativePair or CloseReading).
bool sameCollectionOverFocal(const ChordSliceCandidate& a, const ChordSliceCandidate& b,
                             const std::vector<FocalNote>& focal)
{
    bool present[12] = {};
    for (const FocalNote& f : focal) { present[f.pc()] = true; }
    int aCov = 0, bCov = 0;
    for (int pc = 0; pc < 12; ++pc) {
        if (!present[pc]) { continue; }
        const bool inA = function::bassIsTemplateChordTone(a.rootPc, a.tiePriority, pc);
        const bool inB = function::bassIsTemplateChordTone(b.rootPc, b.tiePriority, pc);
        if (!inA && !inB) { return false; }   // a focal pc neither reading explains → not one collection
        if (inA) { ++aCov; }
        if (inB) { ++bCov; }
    }
    return aCov >= 3 && bCov >= 3;
}

/// G6 ambiguity cue — are the two readings a relative major/minor pair? Roots a minor
/// third apart (Δ ∈ {3,9}) with one major-quality and one minor-quality (C↔Am, the
/// relative reading the key axis leaves open, design §15-O1). Quality is the coarse
/// ChordQuality category here (the relative relation is a triad-quality fact).
bool relativePair(const ChordSliceCandidate& a, const ChordSliceCandidate& b)
{
    const int d = (((a.rootPc - b.rootPc) % 12) + 12) % 12;
    const bool thirdApart = (d == 3 || d == 9);
    const bool majMin = (a.quality == ChordQuality::Major && b.quality == ChordQuality::Minor)
                        || (a.quality == ChordQuality::Minor && b.quality == ChordQuality::Major);
    return thirdApart && majMin;
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
        f.tpc          = ne->tpc;   // notated spelling for the G4/C1 spelling-pin
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

// ── The three-tier membership ladder (design §5 step 3) ──────────────────────
//
// Stepwise STRUCTURE is the decisive signal; metric weight enters ONLY at the third
// tier. The per-side step signals (from/to a chord tone) are computed once and the
// ladder + the plausibility check (G3) read them.

/// Per-side stepwise structure of a focal note within its window (design §5 step 3 /
/// §1): approached AND adjacent by step from a chord tone (stepIn), left by step to a
/// chord tone (stepOut), or held from the previous chord and resolving DOWN by step to
/// a chord tone (suspension). Per-voice / melodic; the neighbour chords are context only
/// (never a chord-to-chord transition cost — that is Layer 5). prevChord / nextChord may
/// be absent (boundary / two-pass-off) — then only the cues that do not need them fire.
struct StepwiseSignals {
    bool stepIn = false;      ///< approached by step from a chord tone
    bool stepOut = false;     ///< left by step to a chord tone
    bool leapIn = false;      ///< a melodic predecessor exists and is reached by leap (not a step)
    bool leapOut = false;     ///< a melodic successor exists and is left by leap (not a step)
    bool suspension = false;  ///< held from the previous chord, resolves down by step to a CT
};

StepwiseSignals stepwiseSignals(const FocalNote& note,
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

    StepwiseSignals s;
    s.stepIn  = pred && isSemitoneStep(pred->pitch, note.pitch)
                && isChordToneOfAny(prevOrThis, pred->pc());
    s.stepOut = succ && isSemitoneStep(note.pitch, succ->pitch)
                && isChordToneOfAny(thisOrNext, succ->pc());
    // A leap = a melodic neighbour exists but is NOT a step (interval ≥ a minor third).
    // "Reached/left by leap" needs a neighbour: an ISOLATED note (no neighbour) is neither
    // a step nor a leap on that side — it is open, and the ladder leaves it to metric weight.
    s.leapIn  = pred && !isSemitoneStep(pred->pitch, note.pitch);
    s.leapOut = succ && !isSemitoneStep(note.pitch, succ->pitch);

    // Suspension: belongs to the previous chord, resolves DOWN by step to a chord tone.
    const bool heldFromPrev = prevChord
                              && function::bassIsTemplateChordTone(prevChord->rootPc,
                                                                   prevChord->tiePriority, note.pc());
    const bool resolvesDown = succ && (note.pitch - succ->pitch) >= 1 && (note.pitch - succ->pitch) <= 2
                              && isChordToneOfAny({ &chord }, succ->pc());
    s.suspension = heldFromPrev && resolvesDown;
    return s;
}

/// The outcome of running ONE focal note through the three-tier ladder against a chord.
struct ToneOutcome {
    bool chordTone = false;          ///< structural — a chord-tone (extension) of the chord
    bool tier1Embellishing = false;  ///< Tier 1 (passing/neighbour/suspension) — the plausibility trigger
};

/// Classify a focal note against @p chord by the three-tier structure-first ladder
/// (design §5 step 3):
///   * Tier 1 — stepwise-embellishing (a passing/neighbour tone between chord tones, or
///     a suspension) → NON-CHORD TONE, regardless of metric weight (the accented passing
///     tone metric weight alone would misclassify).
///   * Tier 2 — no stepwise connection: reached AND left by LEAP (both melodic neighbours
///     present, both leaps) → CHORD-TONE EXTENSION, regardless of metric weight (the weak
///     leap / arpeggiated tone metric weight alone would wrongly call an embellishment).
///   * Tier 3 — stepwise on ONE side only (appoggiatura / escape / incomplete neighbour)
///     → metric weight adjudicates: a note that resolves by step into a chord tone is a
///     non-chord tone (appoggiatura); an escape tone is decided by weight.
/// So both-sides-stepwise and both-sides-leap are settled by structure alone; metric
/// weight adjudicates the one-sided case AND any note the three tiers do not cover — an
/// ISOLATED note (no melodic neighbour) or a single-sided open/leap note — which is
/// neither a clean embellishment nor a clean arpeggiation and is left to its salience.
ToneOutcome classifyTone(const FocalNote& note,
                         const std::vector<FocalNote>& window,
                         const ChordSliceCandidate& chord,
                         const ChordSliceCandidate* prevChord,
                         const ChordSliceCandidate* nextChord,
                         const ChordSliceDecoderPreferences& dp)
{
    const StepwiseSignals s = stepwiseSignals(note, window, chord, prevChord, nextChord, dp);
    ToneOutcome o;

    // Tier 1 — stepwise-embellishing → non-chord tone, regardless of metric weight.
    if (s.suspension || (s.stepIn && s.stepOut)) {
        o.chordTone = false;
        o.tier1Embellishing = true;
        return o;
    }
    // Tier 3 — stepwise on ONE side only.
    if (s.stepIn || s.stepOut) {
        // An appoggiatura resolves by step INTO a chord tone (stepOut) → non-chord tone;
        // an escape tone (stepIn only, leaps away) is decided by metric weight.
        o.chordTone = s.stepOut ? false
                                : (noteSalience(note, dp) >= dp.membershipSalienceThreshold);
        return o;
    }
    // Tier 2 — reached AND left by leap (both neighbours present, both leaps) → structural
    // chord-tone extension, regardless of metric weight (the arpeggiated weak leap).
    if (s.leapIn && s.leapOut) {
        o.chordTone = true;
        return o;
    }
    // Fallthrough — an isolated note, or a single open/leap side: not a clean embellishment
    // nor a clean arpeggiation. Metric weight is the only signal left.
    o.chordTone = noteSalience(note, dp) >= dp.membershipSalienceThreshold;
    return o;
}

/// Template-only inherit consistency (the conservative G1 base): are ALL of the slice's
/// focal notes template tones of @p chord? Covers the spec's documented inherit cases (the
/// single C♯-over-A-major thin slice whose C♯ is the chord's third; the dyad that is a subset
/// of the prevailing chord). Used as the inherit test where no second-reading next provisional
/// chord is available to confirm a CONTINUATION (the right boundary, or the membership /
/// two-pass-off path) — there the conservative base is the only safe inherit.
bool allFocalAreTemplateTonesOf(const ChordSliceCandidate& chord,
                                const std::vector<FocalNote>& focal)
{
    for (const FocalNote& f : focal) {
        if (!function::bassIsTemplateChordTone(chord.rootPc, chord.tiePriority, f.pc())) {
            return false;
        }
    }
    return true;
}

/// Ladder inherit consistency (design §5 step 4): are ALL of the slice's focal notes
/// consistent with the prevailing chord, each being a template tone of it OR a STEPWISE
/// EMBELLISHMENT (a non-chord tone) of it? A focal note that is a STRUCTURAL extension of the
/// prevailing chord (a real foreign chord tone — Tier 2, or a metrically-asserted Tier 3) is
/// NOT an embellishment: the slice is a new chord, not a continuation, so it is inconsistent.
/// This is the "... or a stepwise embellishment of it" relaxation; applied note-only it
/// OVER-inherits (a passing tone of the prevailing chord is just as often a passing tone INTO
/// the next chord), so applyCommitDecision GATES it on the next provisional chord being the
/// prevailing chord (a CONTINUATION) — it relaxes continuations only, never transitions.
/// @p window is the broader note stream the per-voice stepwise test reads (focal ⊆ window);
/// @p prevChord / @p nextChord are the provisional neighbour chords.
bool focalConsistentAsEmbellishmentsOf(const ChordSliceCandidate& prevailing,
                                       const std::vector<FocalNote>& focal,
                                       const std::vector<FocalNote>& window,
                                       const ChordSliceCandidate* prevChord,
                                       const ChordSliceCandidate* nextChord,
                                       const ChordSliceDecoderPreferences& dp)
{
    for (const FocalNote& f : focal) {
        if (function::bassIsTemplateChordTone(prevailing.rootPc, prevailing.tiePriority, f.pc())) {
            continue;   // a chord tone of the prevailing chord — consistent
        }
        const ToneOutcome o = classifyTone(f, window, prevailing, prevChord, nextChord, dp);
        if (o.chordTone) {
            return false;   // a structural foreign note → not an embellishment of prevailing
        }
        // else: a stepwise embellishment (non-chord tone) of the prevailing chord — consistent.
    }
    return true;
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

/// G6 — populate the L4→L5 forward contract on @p sc AFTER the G1 decision is settled
/// (design §7/§8): the composite confidence (every slice) and the named open question
/// (abstain only). Representational — reads the FINAL chosen chord; changes no decision
/// field. The membership cleanliness is read off the chosen chord's focal classification
/// (the same classifyMembership the §10 metric scores); on an abstain sc.chosen still
/// holds the top reading. @p sufficient / @p wasTransition carry the abstain sub-reason.
void populateForwardContract(SliceChord& sc,
                             const std::vector<FocalNote>& focal,
                             const std::vector<FocalNote>& window,
                             const std::optional<ChordSliceCandidate>& prevChord,
                             const std::optional<ChordSliceCandidate>& nextChord,
                             bool sufficient, bool wasTransition,
                             const ChordSliceDecoderPreferences& dp)
{
    int present = 0, required = 0, chordTonePcs = 0, focalPcs = 0;
    if (sc.chosen.rootPc >= 0) {
        required = templateToneCount(sc.chosen.tiePriority);
        present  = ChordSliceDecoder::templateTonePresenceCount(sc.chosen, focal);
        if (!focal.empty()) {
            const MembershipResult m = ChordSliceDecoder::classifyMembership(
                sc.chosen, focal, window, prevChord, nextChord, dp);
            chordTonePcs = static_cast<int>(m.chordTonePcs.size());
            focalPcs     = static_cast<int>(m.chordTonePcs.size() + m.nonChordTonePcs.size());
        }
    }
    sc.confidenceModel = ChordSliceDecoder::computeConfidence(
        sc.confidence, present, required, chordTonePcs, focalPcs, dp);
    sc.openQuestion = ChordSliceDecoder::nameOpenQuestion(sc, sufficient, wasTransition, focal, dp);
}

// ── G4 / C1: the symmetric-root SPELLING-PIN (design §5/§9) ───────────────────
//
// A symmetric (pitch-class-ambiguous) sonority and its rotation set, detected from the
// CHOSEN chord's quality + the focal pitch classes present. On the EXISTING catalogue
// (no four-note dim7 type — C2/G5 deferred) the two symmetric cases are:
//   * a fully-diminished SEVENTH — the chosen is a Diminished TRIAD (root r) and all four
//     of {r, r+3, r+6, r+9} sound: the four dim-triad rotations are the dim7Characteristic
//     coin-flip. step = 3 (minor thirds), root = the SHARPEST-spelled note (max LOF).
//   * an AUGMENTED triad — symmetric by construction: {r, r+4, r+8} all sound. step = 4
//     (major thirds), root = the FLATTEST-spelled note (min LOF).
// A plain dim TRIAD (no r+9 present) is NOT symmetric — it has a pitch-class-defined root —
// so the pin never touches it.
struct SymRotationSet {
    bool valid = false;
    bool dimSeventh = false;            ///< true: dim7 (root = max LOF); false: aug (root = min LOF)
    ChordQuality quality = ChordQuality::Unknown;
    int stepFifths = 0;                 ///< adjacent line-of-fifths step in the sorted stack (3 or 4)
    bool isRotationPc[12] = {};         ///< the symmetric collection's pitch classes
    std::vector<int> rotationPcs;       ///< the rotation root pcs (3 aug / 4 dim7)
};

SymRotationSet symmetricRotationSet(const ChordSliceCandidate& chosen,
                                    const std::vector<FocalNote>& focal)
{
    SymRotationSet s;
    if (chosen.rootPc < 0 || chosen.rootPc >= 12) {
        return s;
    }
    bool present[12] = {};
    for (const FocalNote& f : focal) { present[f.pc()] = true; }

    auto rot = [&](int base, int step, int n) -> bool {
        std::vector<int> pcs;
        for (int k = 0; k < n; ++k) {
            const int pc = (base + step * k) % 12;
            if (!present[pc]) { return false; }   // a collection tone is not sounding → not this sonority
            pcs.push_back(pc);
        }
        for (int pc : pcs) { s.isRotationPc[pc] = true; }
        s.rotationPcs = pcs;
        return true;
    };

    if (chosen.quality == ChordQuality::Augmented) {
        if (rot(chosen.rootPc, 4, 3)) {
            s.valid = true; s.dimSeventh = false; s.quality = ChordQuality::Augmented; s.stepFifths = 4;
        }
    } else if (chosen.quality == ChordQuality::Diminished) {
        if (rot(chosen.rootPc, 3, 4)) {   // a FULL dim7 (root+9 present), not a plain dim triad
            s.valid = true; s.dimSeventh = true; s.quality = ChordQuality::Diminished; s.stepFifths = 3;
        }
    }
    return s;
}

// The line-of-fifths position the focal notes assign to @p pc, or kNoLineOfFifths when no
// focal note of that pc carries a (valid) spelling, or kContradictedLof when two focal notes
// of the same pc are spelled differently (e.g. G♯ and A♭ both sounding) — the spelling is not
// internally consistent there, so the pin must defer.
constexpr int kContradictedLof = -1000000;
int focalLineOfFifths(int pc, const std::vector<FocalNote>& focal)
{
    int lof = engravingbridge::kNoLineOfFifths;
    for (const FocalNote& f : focal) {
        if (f.pc() != pc) { continue; }
        const int l = engravingbridge::lineOfFifths(f.tpc);
        if (l == engravingbridge::kNoLineOfFifths) { continue; }
        if (lof == engravingbridge::kNoLineOfFifths) {
            lof = l;
        } else if (lof != l) {
            return kContradictedLof;   // same pc spelled two ways → contradiction
        }
    }
    return lof;
}

// The spelling-determined root pc for a symmetric rotation set, or -1 when the spelling is
// absent (a collection tone has no tpc) or internally inconsistent (a contradiction, or the
// spellings do not form a clean stack of thirds). The stack is verified directly: sorted by
// line-of-fifths the positions must rise by exactly @p stepFifths each (3 for the minor-third
// dim7 stack, 4 for the major-third augmented stack); the root is the sharpest (dim7) or
// flattest (aug) end — the bottom of the stack of thirds.
int spellingRootOf(const SymRotationSet& sym, const std::vector<FocalNote>& focal)
{
    if (!sym.valid) { return -1; }
    std::vector<std::pair<int, int>> lofPc;   // (lineOfFifths, pc)
    for (int pc : sym.rotationPcs) {
        const int lof = focalLineOfFifths(pc, focal);
        if (lof == engravingbridge::kNoLineOfFifths || lof == kContradictedLof) {
            return -1;   // absent or contradicted spelling → defer to the scorer's choice
        }
        lofPc.emplace_back(lof, pc);
    }
    std::sort(lofPc.begin(), lofPc.end(),
              [](const std::pair<int, int>& a, const std::pair<int, int>& b) { return a.first < b.first; });
    for (std::size_t i = 1; i < lofPc.size(); ++i) {
        if (lofPc[i].first - lofPc[i - 1].first != sym.stepFifths) {
            return -1;   // not a clean stack of thirds → the spelling contradicts → defer
        }
    }
    // dim7 root = the sharpest (max LOF, back); aug root = the flattest (min LOF, front).
    return sym.dimSeventh ? lofPc.back().second : lofPc.front().second;
}

// The cube candidate that re-roots the chosen symmetric chord to @p root: same quality,
// preferring the chosen's actual bass (the bass note does not move when the rotation is
// re-named), else any voicing at that root+quality. nullptr when the rotation is not in the
// surfaced cube (defensive — every dim7 rotation is normally scored).
const ChordSliceCandidate* bestRotationCandidate(const std::vector<ChordSliceCandidate>& ranked,
                                                 int root, const ChordSliceCandidate& chosen)
{
    const ChordSliceCandidate* exact = nullptr;
    const ChordSliceCandidate* symbol = nullptr;
    for (const ChordSliceCandidate& c : ranked) {
        if (c.rootPc == root && c.quality == chosen.quality) {
            if (c.bassPc == chosen.bassPc) { exact = &c; break; }
            if (!symbol) { symbol = &c; }
        }
    }
    return exact ? exact : symbol;
}

} // namespace

int ChordSliceDecoder::spellingPinnedRoot(
    const ChordSliceCandidate& chosen,
    const std::vector<FocalNote>& focal,
    const ChordSliceDecoderPreferences& decoderPrefs)
{
    if (!decoderPrefs.enableSpellingPin) {
        return -1;
    }
    return spellingRootOf(symmetricRotationSet(chosen, focal), focal);
}

SliceChord ChordSliceDecoder::decideSlice(
    int sliceIndex,
    const std::vector<ChordSliceCandidate>& candidates,
    const std::optional<ChordSliceCandidate>& prevailing,
    const ChordSliceDecoderPreferences& decoderPrefs,
    const std::vector<FocalNote>& focal)
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

    // ── G4 / C1: the symmetric-root SPELLING-PIN (design §5/§9) ───────────────
    // For a symmetric (dim7 / augmented) sonority the scorer's chosen ROTATION came
    // from the KEY-dependent dim7CharacteristicBonus + diatonic-root term. Where the
    // notated spelling is present and internally consistent it NAMES the root
    // deterministically (G♯–B–D–F is G♯) — override the rotation to the spelled root
    // and treat the sibling rotations as the SAME, spelling-resolved reading (not
    // competing): they are dropped from the margin and the carried alternatives.
    // Where the spelling is absent / contradicted (spelledRoot < 0) the scorer's
    // choice stands and siblings count normally (the existing behaviour).
    const SymRotationSet sym = decoderPrefs.enableSpellingPin
        ? symmetricRotationSet(sc.chosen, focal) : SymRotationSet{};
    bool pinned = false;
    if (sym.valid) {
        const int spelledRoot = spellingRootOf(sym, focal);
        if (spelledRoot >= 0) {
            pinned = true;
            if (spelledRoot != sc.chosen.rootPc) {
                const ChordSliceCandidate* repl = bestRotationCandidate(ranked, spelledRoot, sc.chosen);
                if (repl) { sc.chosen = *repl; }
            }
        }
    }
    // A sibling rotation of the pinned symmetric collection: same quality and a root in
    // the collection. Spelling resolved among these, so they are not competing readings.
    const auto isResolvedSibling = [&](const ChordSliceCandidate& c) {
        return pinned && c.quality == sym.quality
               && c.rootPc >= 0 && c.rootPc < 12 && sym.isRotationPc[c.rootPc];
    };

    // Confidence = chosen vertical score − best score over any DIFFERENT (root,
    // quality) chord. An inversion of the SAME chord is not a different chord; nor is
    // a spelling-resolved sibling rotation (the spelling, not the score, settled it).
    double bestOther = NEG_INF;
    for (const ChordSliceCandidate& c : ranked) {
        if (sameChordSymbol(c, sc.chosen) || isResolvedSibling(c)) {
            continue;
        }
        bestOther = std::max(bestOther, c.score);
    }
    sc.confidence = (bestOther == NEG_INF) ? kNoCompetitorConfidence
                                           : (sc.chosen.score - bestOther);
    sc.uncertain = sc.confidence < decoderPrefs.uncertaintyMargin;

    // Ranked alternatives: the distinct chord voicings after the chosen, capped at
    // topK, then ∪ the prevailing chord (the L3 incumbent pattern — kept alive as a
    // carried alternative even when it falls below topK, so the membership two-pass
    // in Increment B always has it). A spelling-resolved sibling rotation is NOT a
    // competing reading (G4/C1) — it is not carried.
    for (const ChordSliceCandidate& c : ranked) {
        if (sameChordVoicing(c, sc.chosen) || isResolvedSibling(c)) {
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

    // Aggregate per pc: a pc is a chord tone if it is a template tone OR at least one of
    // its focal notes classifies as a structural chord-tone extension; a non-chord tone
    // only when EVERY focal note of that pc is embellishment-like (design §5 step 3).
    bool present[12] = {};
    bool anyChordTone[12] = {};

    for (const FocalNote& f : focal) {
        const int pc = f.pc();
        present[pc] = true;

        const bool isTemplate = function::bassIsTemplateChordTone(chord.rootPc, chord.tiePriority, pc);
        const ToneOutcome o = classifyTone(f, window, chord, prevC, nextC, dp);

        if (isTemplate) {
            // A required (template) tone is a chord tone of THIS chord. But it is NOT
            // exempt from the behaviour test — running it through the SAME ladder IS the
            // plausibility check (design §5 step 3, G3, the Step-2 ADDITION): a template
            // tone that behaves as a Tier-1 stepwise embellishment makes the candidate
            // IMPLAUSIBLE — it forces a passing tone to be a required chord member (the
            // spurious seventh of a triad, or the passing D heard as Cadd9's ninth). This
            // is the direction the OLD extra-note-only penalty could NOT catch (Step-0 G3).
            anyChordTone[pc] = true;
            if (o.tier1Embellishing) {
                r.implausibilityPenalty += noteSalience(f, dp);
            }
        } else if (o.chordTone) {
            // An "extra" note (pc not in the basic template) the chord can only absorb as an
            // added 6th/9th/… — the membership→selection feedback (design §4 step 2, the cue
            // Step-0 G3 noted the old penalty "catches one way"): a chord that leaves a
            // STRUCTURAL focal note outside its basic template is a worse explanation of the
            // FOCAL slice than one whose template already includes it (the richer-chord
            // direction — it gives the focal-fitting chord its selection margin). Charged.
            anyChordTone[pc] = true;
            r.implausibilityPenalty += noteSalience(f, dp);
        }
        // else: an extra, embellishment-like note — a non-chord tone, no penalty.
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

SliceConfidence ChordSliceDecoder::computeConfidence(
    double margin,
    int templateTonesPresent, int templateTonesRequired,
    int focalChordTonePcs, int focalPcs,
    const ChordSliceDecoderPreferences& dp)
{
    SliceConfidence c;
    c.margin = margin;

    // Sufficiency — present / required template tones of the chosen chord, clamped [0,1]
    // (a full seventh present → 1.0; a dyad of a triad → 0.67; a lone tone → 0.33). The
    // "how complete the committed chord is" axis (design §7).
    c.sufficiency = (templateTonesRequired > 0)
        ? std::min(1.0, std::max(0.0, static_cast<double>(templateTonesPresent)
                                      / static_cast<double>(templateTonesRequired)))
        : 0.0;

    // Membership cleanliness — the chord-tone fraction of the focal pitch classes (few
    // contested notes vs many, design §7). No focal notes → clean (1.0) by convention.
    c.membershipCleanliness = (focalPcs > 0)
        ? std::min(1.0, std::max(0.0, static_cast<double>(focalChordTonePcs)
                                      / static_cast<double>(focalPcs)))
        : 1.0;

    // Margin → certainty in [0,1], scaled by the EXISTING uncertainty threshold: at the
    // decision boundary (margin == uncertaintyMargin) → 0.5; at 2× → 1.0; the no-competitor
    // sentinel → 1.0. Reuses uncertaintyMargin — no NEW accuracy parameter (representational).
    const double ref = 2.0 * std::max(1e-9, dp.uncertaintyMargin);
    const double marginCertainty = std::min(1.0, std::max(0.0, margin / ref));

    // Composite = MIN (the "uncertain when low for EITHER reason" property, design §7): a
    // wide margin does NOT rescue an insufficient slice, nor a clean membership a low margin.
    c.composite = std::min(marginCertainty, std::min(c.sufficiency, c.membershipCleanliness));
    return c;
}

OpenQuestionLabel ChordSliceDecoder::nameOpenQuestion(
    const SliceChord& sc, bool sufficient, bool wasTransition,
    const std::vector<FocalNote>& focal,
    const ChordSliceDecoderPreferences& /*dp*/)
{
    OpenQuestionLabel q;
    if (sc.decision != SliceDecision::Abstain) {
        return q;   // Commit / Inherit → nothing open (None / None)
    }

    // An abstain with no scorable reading at all (an empty slice — decideSlice found no cell).
    if (sc.chosen.rootPc < 0) {
        q.question = OpenQuestion::Root;
        q.ambiguity = AmbiguityKind::InsufficientEvidence;
        return q;
    }

    q.readingA = sc.chosen;   // the chosen / top reading — one side of the open question

    // The best DIFFERENT (root,quality) reading carried among the alternatives (an inversion
    // of the chosen is NOT a different reading).
    const ChordSliceCandidate* other = nullptr;
    for (const ChordSliceCandidate& a : sc.alternatives) {
        if (!sameChordSymbol(a, sc.chosen)) { other = &a; break; }
    }
    if (other) {
        q.readingB = *other;
        q.hasReadingB = true;
    }

    if (!sufficient) {
        // Thin slice — too few notes to fix a chord (the phantom-root guard). The open
        // question is the ROOT; the kind is whether it is heading into a DIFFERENT next chord
        // (a transition) or simply has no consistent prevailing chord (insufficient evidence).
        q.question = OpenQuestion::Root;
        q.ambiguity = wasTransition ? AmbiguityKind::TransitionVsContinuation
                                    : AmbiguityKind::InsufficientEvidence;
        return q;
    }

    // Sufficient but low margin — two close readings. Name the axis they disagree on and the
    // kind of ambiguity from the chosen vs the best different reading.
    if (!other) {
        q.question = OpenQuestion::Quality;          // a margin abstain with only same-symbol inversions (rare)
        q.ambiguity = AmbiguityKind::CloseReading;
        return q;
    }

    if (sc.chosen.rootPc == other->rootPc) {
        // Same root, competing qualities/functions (C vs C7; passing-dim vs applied chord).
        q.question = OpenQuestion::Quality;
        q.ambiguity = sameCollectionOverFocal(sc.chosen, *other, focal)
                      ? AmbiguityKind::ShareTone : AmbiguityKind::CloseReading;
        return q;
    }

    // Different roots — the ROOT (chord identity) is the open question; L5 selects the reading.
    q.question = OpenQuestion::Root;
    if (sc.chosen.quality == ChordQuality::Augmented && other->quality == ChordQuality::Augmented) {
        q.ambiguity = AmbiguityKind::SymmetricRotation;   // augmented rotations (dim7 once G5 lands)
    } else if (sameCollectionOverFocal(sc.chosen, *other, focal)) {
        q.ambiguity = AmbiguityKind::ShareTone;           // same collection, different naming (Am6↔F♯ø7)
    } else if (relativePair(sc.chosen, *other)) {
        q.ambiguity = AmbiguityKind::RelativePair;        // relative major/minor (C↔Am)
    } else {
        q.ambiguity = AmbiguityKind::CloseReading;
    }
    return q;
}

void ChordSliceDecoder::applyCommitDecision(
    SliceChord& sc,
    const std::vector<FocalNote>& focal,
    const std::vector<FocalNote>& window,
    const std::optional<ChordSliceCandidate>& prevailing,
    const std::optional<ChordSliceCandidate>& prevChord,
    const std::optional<ChordSliceCandidate>& nextChord,
    const ChordSliceDecoderPreferences& dp)
{
    if (!dp.enableCommitDecision) {
        // Pre-G1 always-commit behaviour: leave the DECISION exactly as decideSlice left
        // it (the empty-slice abstain set in decideSlice is preserved). The G6 forward
        // contract is additive — it changes no decision field.
        populateForwardContract(sc, focal, window, prevChord, nextChord,
                                /*sufficient=*/false, /*wasTransition=*/false, dp);
        return;
    }

    // No scorable candidate → abstain (decideSlice already cleared hasChord).
    if (!sc.hasChord) {
        sc.decision = SliceDecision::Abstain;
        populateForwardContract(sc, focal, window, prevChord, nextChord,
                                /*sufficient=*/false, /*wasTransition=*/false, dp);
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
        populateForwardContract(sc, focal, window, prevChord, nextChord,
                                sufficient, /*wasTransition=*/false, dp);
        return;
    }

    // Inherit — the §4 two-reading BOTH-SIDES test (design §4 step 3 / §5 step 4). A thin
    // (insufficient) slice carries the prevailing chord forward only when it CONTINUES it,
    // not when it TRANSITIONS to a new chord. The left side is the prevailing chord by
    // construction (the carried committed/inherited chain); the right side is the next
    // provisional chord @p nextChord (the second-reading pass-1 neighbour):
    //   * next provisional == prevailing (a CONTINUATION): inherit iff the slice's notes are
    //     all consistent with the prevailing chord by the G2 ladder (each a template tone OR
    //     a stepwise embellishment of it). This is the spec's "... or a stepwise embellishment
    //     of it" relaxation, now SAFELY gated — it relaxes continuations only.
    //   * next provisional differs (a TRANSITION): do NOT inherit — the thin slice is heading
    //     into a new chord, so it abstains on its own (insufficient) evidence. THIS is the
    //     over-inherit fix: a note-only inherit cannot tell a continuation of the prevailing
    //     chord from a transition to the next; the next provisional chord is what separates
    //     them. A genuinely function-dependent residual (which the chord neighbours cannot
    //     resolve) abstains → Architectural Layer 5.
    //   * no next provisional in view (the right boundary, or the membership / two-pass-off
    //     path): fall back to the conservative TEMPLATE-ONLY inherit — no CONTINUATION can be
    //     confirmed, so the G1 base is the only safe inherit.
    // (A slice that is sufficient but merely loses on margin is NOT inherited — it abstains.)
    if (!sufficient && prevailing.has_value()) {
        bool inherit = false;
        if (nextChord.has_value()) {
            inherit = sameChordSymbol(*nextChord, *prevailing)
                      && focalConsistentAsEmbellishmentsOf(
                             *prevailing, focal, window,
                             prevChord.has_value() ? &*prevChord : nullptr, &*nextChord, dp);
        } else {
            inherit = allFocalAreTemplateTonesOf(*prevailing, focal);
        }
        if (inherit) {
            sc.chosen = *prevailing;
            sc.decision = SliceDecision::Inherit;
            sc.uncertain = false;   // an inherited prevailing chord is a committed answer
            populateForwardContract(sc, focal, window, prevChord, nextChord,
                                    sufficient, /*wasTransition=*/false, dp);
            return;
        }
    }

    // Abstain: insufficient with no consistent prevailing, or sufficient but low margin.
    // No new symbol is committed (the no-chord / open marker); the competing readings
    // (alternatives) are kept for Architectural Layer 5, NAMED by the open-question label.
    sc.decision = SliceDecision::Abstain;
    sc.hasChord = false;
    sc.uncertain = true;
    // The abstain sub-reason for the open question: a thin (insufficient) slice heading into
    // a DIFFERENT next chord is a transition; otherwise insufficient / low-margin (named inside).
    const bool wasTransition = !sufficient && prevailing.has_value() && nextChord.has_value()
                               && !sameChordSymbol(*nextChord, *prevailing);
    populateForwardContract(sc, focal, window, prevChord, nextChord,
                            sufficient, wasTransition, dp);
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
    // Provisional pass-1 chord (own notes + key prior). The focal notes carry the
    // per-note spelling so the G4/C1 pin re-roots a symmetric provisional too — the
    // pass-1 chosen feeds the pass-2 neighbour (prevC/nextC) context.
    w.pass1  = ChordSliceDecoder::decideSlice(t, w.cands, std::nullopt, dp, w.focal);
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
    SliceChord sc = ChordSliceDecoder::decideSlice(t, adj, prevailing, dp, w.focal);
    // G1 + the §4 two-reading inherit — commit / inherit / abstain (design §4 step 3, §5
    // step 4). Decided BEFORE membership so the per-note classification reflects the FINAL
    // chord (the inherited prevailing chord on Inherit; nothing on Abstain). The window +
    // both-side provisional neighbour chords (prevC/nextC) feed the continuation-gated
    // stepwise-embellishment inherit (nextC is the right-side provisional that tells a
    // CONTINUATION of the prevailing chord from a TRANSITION to the next).
    ChordSliceDecoder::applyCommitDecision(sc, w.focal, w.window, prevailing, prevC, nextC, dp);
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
            SliceChord sc = ChordSliceDecoder::decideSlice(t, w.cands, prevailing, dp, w.focal);
            // Membership/two-pass disabled → no provisional neighbour chords; the §4
            // two-reading continuation gate cannot fire, so inherit falls back to the
            // conservative template-only G1 base (no CONTINUATION can be confirmed).
            ChordSliceDecoder::applyCommitDecision(sc, w.focal, w.window, prevailing,
                                                   std::nullopt, std::nullopt, dp);   // G1
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
