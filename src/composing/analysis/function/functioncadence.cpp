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
#include "functioncadence.h"

#include "functionprogression.h"   // isLicensedProgression — the §5.0 pre-dominant→dominant reuse

namespace mu::composing::analysis {

namespace {

/// Pitch class of any integer pitch/interval in [0, 11] (the functionprogression
/// self-contained-helper precedent; keeps this module free of chord/ headers).
int norm(int pitch) noexcept
{
    return ((pitch % 12) + 12) % 12;
}

/// True when pitch class @p pc sounds anywhere in @p e's notes.
bool eventHasPc(const CadenceEvent& e, int pc) noexcept
{
    const int target = norm(pc);
    for (const CadenceVoiceNote& n : e.notes) {
        if (n.pc() == target) {
            return true;
        }
    }
    return false;
}

/// True when some voice sounds pc @p fromPc at @p dom and the SAME voice sounds pc
/// @p toPc at @p arr — a same-voice melodic motion across the boundary (the basis of
/// the leading-tone-resolution and tritone-resolution events, §5.0).
bool voiceMovesFromTo(const CadenceEvent& dom, const CadenceEvent& arr,
                      int fromPc, int toPc) noexcept
{
    const int from = norm(fromPc);
    const int to = norm(toPc);
    for (const CadenceVoiceNote& nd : dom.notes) {
        if (nd.pc() != from) {
            continue;
        }
        for (const CadenceVoiceNote& na : arr.notes) {
            if (na.voice == nd.voice && na.pc() == to) {
                return true;
            }
        }
    }
    return false;
}

/// The dominant carries its TRITONE (the leading tone 7̂ and the fourth degree 4̂,
/// relative to @p tonicPc) in its pitch content — present, not necessarily resolving.
bool dominantTritonePresent(const CadenceEvent& dom, int tonicPc) noexcept
{
    return eventHasPc(dom, tonicPc + 11) && eventHasPc(dom, tonicPc + 5);
}

/// A pre-dominant before the dominant (the §5.2 sequence pre-dominant→dominant→
/// tonic), relative to the candidate @p tonicPc. A subdominant-family root (IV/iv +5,
/// ii/ii° +2, bII/Neapolitan +1, bVI +8) OR a Step-1 licensed progression INTO the
/// dominant (IV→V ascending second, ii→V descending fifth — the functionprogression
/// reuse), excluding the tonic and the dominant root themselves.
bool isPredominant(const CadenceEvent& pred, const CadenceEvent& dom, int tonicPc) noexcept
{
    if (pred.rootPc < 0) {
        return false;
    }
    const int r = norm(pred.rootPc - tonicPc);
    if (r == 5 || r == 2 || r == 1 || r == 8) {
        return true;
    }
    if (pred.rootPc != tonicPc && pred.rootPc != dom.rootPc) {
        return isLicensedProgression({ pred.rootPc, pred.quality },
                                     { dom.rootPc, dom.quality });
    }
    return false;
}

} // namespace

bool isRootPosition(const CadenceEvent& e) noexcept
{
    return e.rootPc >= 0 && e.bassPc == e.rootPc;
}

bool isSecondInversionTonicTriad(const CadenceEvent& e) noexcept
{
    if (e.quality != ChordQuality::Major && e.quality != ChordQuality::Minor) {
        return false;
    }
    if (e.rootPc < 0 || e.bassPc < 0) {
        return false;
    }
    // The bass is the chord's own fifth (a 6/4 voicing).
    return e.bassPc == norm(e.rootPc + 7);
}

bool leadingToneResolves(const CadenceEvent& dom, const CadenceEvent& arr, int tonicPc) noexcept
{
    // The leading tone (tonicPc - 1 = 7̂) in a voice of the dominant moves, in THAT
    // SAME voice, to the tonic (tonicPc = 1̂) at the arrival. Resolution as a detected
    // event, never the mere presence of the leading tone (the I→IV false-positive trap
    // the prior presence test fell into).
    return voiceMovesFromTo(dom, arr, tonicPc + 11, tonicPc);
}

bool dominantSeventhPresent(const CadenceEvent& dom) noexcept
{
    if (dom.rootPc < 0) {
        return false;
    }
    // A minor seventh above the dominant's own root — the dominant-seventh signature.
    // Read from the pitch content (the seventh is not on the L4 quality projection; §1).
    return eventHasPc(dom, dom.rootPc + 10);
}

bool isGenuineDominant(const CadenceEvent& dom, const CadenceEvent& arr, int tonicPc) noexcept
{
    // §5.2: "a seventh OR its tritone resolving."
    // (a) a seventh — the V7's minor seventh present.
    if (dominantSeventhPresent(dom)) {
        return true;
    }
    // (b) the tritone resolving — the dominant carries 7̂ and 4̂, and across the
    // boundary 7̂→1̂ and 4̂→3̂ resolve by same-voice step to the tonic's root and third
    // (the third's mode read off the arrival triad). Admits a viio leading-tone chord
    // (its root-to-b5 tritone resolves); a plain V or I triad carries no 4̂, so no
    // tritone, and fails — the I→IV discriminator.
    if (dominantTritonePresent(dom, tonicPc)) {
        const int thirdPc = (arr.quality == ChordQuality::Minor) ? norm(tonicPc + 3)
                                                                 : norm(tonicPc + 4);
        if (leadingToneResolves(dom, arr, tonicPc)
            && voiceMovesFromTo(dom, arr, tonicPc + 5, thirdPc)) {
            return true;
        }
    }
    return false;
}

double cadenceTonicVote(const FunctionalCadence& c, const CadenceEvent& arrival,
                        const FunctionCadenceParams& params) noexcept
{
    // §5.2: a monotone-increasing weighted sum of the evidence cues + the salience
    // cues, minus the per-type lower-confidence discount. Direction fixed; weights
    // firewall seeds. Clamped at 0.
    double v = params.wBase;
    if (c.bassFiveToOne) {
        v += params.wBassFiveToOne;
    }
    if (c.leadingToneResolves) {
        v += params.wLeadingTone;
    }
    if (c.genuineDominant) {
        v += params.wSeventh;
    }
    v += params.wMetric * arrival.metricWeight;
    if (arrival.endsPhrase) {
        v += params.wPhraseBoundary;
    }
    if (arrival.isFinalBar) {
        v += params.wFinalBar;
    }
    switch (c.type) {
    case FunctionalCadenceType::Half:
    case FunctionalCadenceType::PhrygianHalf:
        v -= params.discountHalf;
        break;
    case FunctionalCadenceType::Plagal:
        v -= params.discountPlagal;
        break;
    case FunctionalCadenceType::Evaded:
        v -= params.discountEvaded;
        break;
    default:
        break;
    }
    return v < 0.0 ? 0.0 : v;
}

namespace {

// ── Per-pair classification (§5.2) ────────────────────────────────────────────
//
// Tries the typology in priority order on the pair (events[i] = approach,
// events[i+1] = arrival), returning the first match (the types are near-disjoint by
// the arrival's relation to the implied tonic). Returns type None when no cadence is
// found. The chorale phrase gate (the arrival ends a phrase) is applied per type.

FunctionalCadence makeNone() noexcept
{
    return FunctionalCadence{};
}

/// AUTHENTIC (PAC / IAC). Pair (dom = events[i], tonic = events[i+1]).
FunctionalCadence tryAuthentic(const std::vector<CadenceEvent>& events, size_t i,
                               const FunctionCadenceParams& params) noexcept
{
    const CadenceEvent& dom = events[i];
    const CadenceEvent& arr = events[i + 1];

    if (!arr.endsPhrase) {                         // phrase gate — §5.2 candidate admission:
        return makeNone();                          // the common passing I→IV is mid-phrase, rejected here
    }
    if (isSecondInversionTonicTriad(arr)) {        // a 6/4 never registers as a tonic arrival
        return makeNone();
    }
    if (arr.quality != ChordQuality::Major && arr.quality != ChordQuality::Minor) {
        return makeNone();                          // the tonic is a stable triad
    }
    const int tonicPc = arr.rootPc;
    if (tonicPc < 0) {
        return makeNone();
    }

    // Dominant form: a V (Major on 5̂) or a viio leading-tone chord (Diminished on 7̂).
    const bool formV = (dom.quality == ChordQuality::Major)
                       && (dom.rootPc == norm(tonicPc + 7));
    const bool formViio = (dom.quality == ChordQuality::Diminished)
                          && (dom.rootPc == norm(tonicPc + 11));
    if (!formV && !formViio) {
        return makeNone();
    }
    // The leading tone RESOLVES (event) — the authentic-family gate (§5.2 amendment,
    // 2026-06-26). A *plain* triad V→I with the leading-tone resolution IS authentic
    // (Caplin's V(7)→I — the seventh is parenthetical), and it is the common Bach-
    // chorale phrase-end; the genuine dominant (seventh / resolving tritone) is now a
    // vote STRENGTHENER (the +wSeventh term, below), NOT an admission requirement.
    const bool ltResolves = leadingToneResolves(dom, arr, tonicPc);
    if (!ltResolves) {
        return makeNone();
    }
    const bool genuineDom = isGenuineDominant(dom, arr, tonicPc);

    // Sequence: a pre-dominant before the dominant (collapsing a cadential 6/4).
    bool sixFour = false;
    int predIdx = static_cast<int>(i) - 1;
    if (predIdx >= 0
        && isSecondInversionTonicTriad(events[static_cast<size_t>(predIdx)])
        && events[static_cast<size_t>(predIdx)].rootPc == tonicPc
        && isRootPosition(dom)
        && events[static_cast<size_t>(predIdx)].bassPc == dom.bassPc) {
        sixFour = true;            // the 6/4 is the dominant's accented suspension
        predIdx -= 1;              // the real pre-dominant sits before the 6/4
    }
    if (predIdx < 0
        || !isPredominant(events[static_cast<size_t>(predIdx)], dom, tonicPc)) {
        return makeNone();          // §5.2 requires the pre-dominant→dominant→tonic sequence
    }

    // Perfect ⟺ a V with BOTH chords root position (the cadential bass reads 5̂→1̂);
    // imperfect is the complement (inverted dominant/tonic, or the viio substitution).
    const bool bassFiveToOne = formV && isRootPosition(dom) && isRootPosition(arr);

    FunctionalCadence c = makeNone();
    c.type = bassFiveToOne ? FunctionalCadenceType::PerfectAuthentic
                           : FunctionalCadenceType::ImperfectAuthentic;
    c.approachTick = dom.startTick;
    c.arrivalTick = arr.startTick;
    c.tonicPc = tonicPc;
    c.minorMode = (arr.quality == ChordQuality::Minor);
    c.bassFiveToOne = bassFiveToOne;
    c.leadingToneResolves = true;
    c.genuineDominant = genuineDom;     // the strengthener flag (V7 outvotes a plain V), not a gate
    c.sixFourCollapsed = sixFour;
    c.tonicVote = cadenceTonicVote(c, arr, params);
    return c;
}

/// DECEPTIVE. Pair (dom = events[i], submediant = events[i+1]).
FunctionalCadence tryDeceptive(const std::vector<CadenceEvent>& events, size_t i,
                               const FunctionCadenceParams& params) noexcept
{
    const CadenceEvent& dom = events[i];
    const CadenceEvent& arr = events[i + 1];

    if (!arr.endsPhrase) {
        return makeNone();
    }
    if (dom.quality != ChordQuality::Major || dom.rootPc < 0 || arr.rootPc < 0) {
        return makeNone();                          // a V dominant set up to cadence
    }
    const int tonicPc = norm(dom.rootPc - 7);

    // Arrival is the submediant: vi (minor, 6̂ = tonic+9) in a major key, or bVI
    // (major, b6̂ = tonic+8) in a minor key.
    const bool viMajorKey = (arr.rootPc == norm(tonicPc + 9))
                            && (arr.quality == ChordQuality::Minor);
    const bool bVIminorKey = (arr.rootPc == norm(tonicPc + 8))
                             && (arr.quality == ChordQuality::Major);
    if (!viMajorKey && !bVIminorKey) {
        return makeNone();
    }

    // The dominant is set up to cadence: its leading tone sounds, and it is a genuine
    // dominant (a seventh present, or the tritone present — it resolves deceptively,
    // so presence, not resolution-to-tonic, is the test here).
    const int ltPc = norm(tonicPc + 11);
    if (!eventHasPc(dom, ltPc)) {
        return makeNone();
    }
    if (!dominantSeventhPresent(dom) && !dominantTritonePresent(dom, tonicPc)) {
        return makeNone();
    }

    // Sequence: a pre-dominant before the dominant.
    const int predIdx = static_cast<int>(i) - 1;
    if (predIdx < 0
        || !isPredominant(events[static_cast<size_t>(predIdx)], dom, tonicPc)) {
        return makeNone();
    }

    FunctionalCadence c = makeNone();
    c.type = FunctionalCadenceType::Deceptive;
    c.approachTick = dom.startTick;
    c.arrivalTick = arr.startTick;
    c.tonicPc = tonicPc;
    c.minorMode = bVIminorKey;                      // bVI ⇒ minor key; vi ⇒ major key
    c.bassFiveToOne = false;
    c.leadingToneResolves = leadingToneResolves(dom, arr, tonicPc); // LT → tonic (= 3rd of vi)
    c.genuineDominant = true;
    c.sixFourCollapsed = false;
    c.tonicVote = cadenceTonicVote(c, arr, params);
    return c;
}

/// HALF (incl. PHRYGIAN). Pair (pre-dominant = events[i], dominant arrival = events[i+1]).
FunctionalCadence tryHalf(const std::vector<CadenceEvent>& events, size_t i,
                          const FunctionCadenceParams& params) noexcept
{
    const CadenceEvent& pred = events[i];
    const CadenceEvent& arr = events[i + 1];        // the phrase-final dominant

    if (!arr.endsPhrase) {
        return makeNone();
    }
    if (arr.quality != ChordQuality::Major || arr.rootPc < 0) {
        return makeNone();                          // the arrival is a dominant
    }
    const int tonicPc = norm(arr.rootPc - 7);

    if (!isPredominant(pred, arr, tonicPc)) {
        return makeNone();                          // the sequence pre-dominant→dominant
    }

    // Phrygian: a first-inversion pre-dominant (iv6) whose bass is b6̂ moving to the
    // root-position dominant whose bass is 5̂, a DESCENDING SEMITONE in the bass.
    bool phrygian = false;
    if (pred.bassPc >= 0 && arr.bassPc >= 0
        && pred.bassPc == norm(tonicPc + 8)
        && arr.bassPc == norm(tonicPc + 7)
        && norm(arr.bassPc - pred.bassPc) == 11) {
        phrygian = true;
    }

    FunctionalCadence c = makeNone();
    c.type = phrygian ? FunctionalCadenceType::PhrygianHalf : FunctionalCadenceType::Half;
    c.approachTick = pred.startTick;
    c.arrivalTick = arr.startTick;
    c.tonicPc = tonicPc;
    // Best-effort mode: Phrygian is minor by construction; otherwise a minor
    // subdominant (iv) or a diminished supertonic (ii°) implies minor.
    const int predDegree = (pred.rootPc >= 0) ? norm(pred.rootPc - tonicPc) : -1;
    c.minorMode = phrygian
                  || (predDegree == 5 && pred.quality == ChordQuality::Minor)
                  || (predDegree == 2 && pred.quality == ChordQuality::Diminished);
    c.bassFiveToOne = false;
    c.leadingToneResolves = false;                  // a half cadence does not resolve
    c.genuineDominant = false;                      // a seventh WEAKENS a half (not credited)
    c.sixFourCollapsed = false;
    c.tonicVote = cadenceTonicVote(c, arr, params);
    return c;
}

/// PLAGAL. Pair (subdominant-family = events[i], tonic = events[i+1]), no dominant.
FunctionalCadence tryPlagal(const std::vector<CadenceEvent>& events, size_t i,
                            const FunctionCadenceParams& params) noexcept
{
    const CadenceEvent& sd = events[i];
    const CadenceEvent& arr = events[i + 1];

    if (!arr.endsPhrase) {
        return makeNone();
    }
    if (isSecondInversionTonicTriad(arr)) {
        return makeNone();
    }
    if (arr.quality != ChordQuality::Major && arr.quality != ChordQuality::Minor) {
        return makeNone();                          // the tonic is a stable triad
    }
    const int tonicPc = arr.rootPc;
    if (tonicPc < 0 || sd.rootPc < 0) {
        return makeNone();
    }
    // The approach is a subdominant-family chord (IV/iv +5, ii +2, bVI +8) — NOT a
    // dominant — moving directly to the tonic (the pair carries no intervening chord).
    const int r = norm(sd.rootPc - tonicPc);
    if (r != 5 && r != 2 && r != 8) {
        return makeNone();
    }

    FunctionalCadence c = makeNone();
    c.type = FunctionalCadenceType::Plagal;
    c.approachTick = sd.startTick;
    c.arrivalTick = arr.startTick;
    c.tonicPc = tonicPc;
    c.minorMode = (arr.quality == ChordQuality::Minor);
    c.bassFiveToOne = false;
    c.leadingToneResolves = false;
    c.genuineDominant = false;
    c.sixFourCollapsed = false;
    c.tonicVote = cadenceTonicVote(c, arr, params);
    return c;
}

/// EVADED. Pair (dom set up to cadence = events[i], abandoned arrival = events[i+1]).
/// The loosest, lowest-confidence type: a genuine dominant set up to cadence whose
/// phrase-final successor is NEITHER the tonic (authentic) NOR the submediant
/// (deceptive) NOR a dominant (half) — the expected tonic arrival is replaced.
FunctionalCadence tryEvaded(const std::vector<CadenceEvent>& events, size_t i,
                            const FunctionCadenceParams& params) noexcept
{
    const CadenceEvent& dom = events[i];
    const CadenceEvent& arr = events[i + 1];

    if (!arr.endsPhrase) {
        return makeNone();
    }
    if (dom.quality != ChordQuality::Major || dom.rootPc < 0 || arr.rootPc < 0) {
        return makeNone();
    }
    const int tonicPc = norm(dom.rootPc - 7);

    // Set up to cadence: the LT sounds and the dominant is genuine (present).
    if (!eventHasPc(dom, norm(tonicPc + 11))) {
        return makeNone();
    }
    if (!dominantSeventhPresent(dom) && !dominantTritonePresent(dom, tonicPc)) {
        return makeNone();
    }
    // Sequence.
    const int predIdx = static_cast<int>(i) - 1;
    if (predIdx < 0
        || !isPredominant(events[static_cast<size_t>(predIdx)], dom, tonicPc)) {
        return makeNone();
    }

    // The arrival is none of tonic / submediant / dominant.
    const bool isTonic = (arr.rootPc == tonicPc)
                         && (arr.quality == ChordQuality::Major
                             || arr.quality == ChordQuality::Minor);
    const bool isSubmediant = (arr.rootPc == norm(tonicPc + 9))
                              || (arr.rootPc == norm(tonicPc + 8));
    const bool isDominant = (arr.quality == ChordQuality::Major)
                            && (arr.rootPc == norm(tonicPc + 7));
    if (isTonic || isSubmediant || isDominant) {
        return makeNone();
    }

    FunctionalCadence c = makeNone();
    c.type = FunctionalCadenceType::Evaded;
    c.approachTick = dom.startTick;
    c.arrivalTick = arr.startTick;
    c.tonicPc = tonicPc;
    c.minorMode = false;
    c.bassFiveToOne = false;
    c.leadingToneResolves = false;
    c.genuineDominant = true;
    c.sixFourCollapsed = false;
    c.tonicVote = cadenceTonicVote(c, arr, params);
    return c;
}

} // namespace

std::vector<FunctionalCadence>
detectFunctionalCadences(const std::vector<CadenceEvent>& events,
                         const FunctionCadenceParams& params)
{
    std::vector<FunctionalCadence> cadences;
    if (events.size() < 2) {
        return cadences;
    }

    for (size_t i = 0; i + 1 < events.size(); ++i) {
        // Priority order (the types are near-disjoint by the arrival's relation to the
        // implied tonic; order resolves the tonic-arrival overlap authentic-before-
        // plagal and is otherwise inert): authentic → deceptive → half → plagal →
        // evaded. The first match wins.
        FunctionalCadence c = tryAuthentic(events, i, params);
        if (c.type == FunctionalCadenceType::None) {
            c = tryDeceptive(events, i, params);
        }
        if (c.type == FunctionalCadenceType::None) {
            c = tryHalf(events, i, params);
        }
        if (c.type == FunctionalCadenceType::None) {
            c = tryPlagal(events, i, params);
        }
        if (c.type == FunctionalCadenceType::None) {
            c = tryEvaded(events, i, params);
        }
        if (c.type != FunctionalCadenceType::None) {
            cadences.push_back(c);
        }
    }

    return cadences;
}

} // namespace mu::composing::analysis
