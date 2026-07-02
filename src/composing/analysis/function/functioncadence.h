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
#pragma once

// ── composing/analysis/function/functioncadence ──────────────────────────────
//
// Architectural Layer 5 (FUNCTION) — the CADENCE DETECTOR: a KEY-AGNOSTIC,
// EVENT-PAIR, feature-scored detector. Spec: cowork_layer5_function_design.md
// (SIGNED) §5.2 + the §5.0 shared definitions. Build plan:
// cowork_phase5c_l5_build_plan.md Step 2.
//
// A cadence is tested on an EVENT PAIR — the approach chord and the arrival chord
// — never on a single chord's interval content (§5.2). The detector reads NO
// resolved key: the cadence CONFIRMS the tonic, it never reads an already-resolved
// one (the cure for the production detector's circularity).
//
// REUSE vs BUILD (build §1, declared in cc_phase5c_step2_report.md §1):
//   • REUSE the dormant cadencekeyanchor's KEY-AGNOSTIC FRAME — V→I read purely
//     from root pc + quality (root(dominant) = root(tonic)+7), the endsPhrase /
//     salience inputs, and the salience-weighted tonic-vote shape — plus the shared
//     pitch-class primitives (analysisutils.h normalizePc) and the Step-1
//     progression predicates (functionprogression isLicensedProgression for the
//     pre-dominant→dominant sequence).
//   • BUILD the CORRECTED detection that REPLACES the broken test. cadencekeyanchor's
//     genuine-cadence gate is a leading-tone-PRESENCE test
//     (pcInMask(a.pitchClassMask, leadingTone)) — the major third is present in
//     EVERY major triad, so it false-positives on I→IV / I→V. This unit does NOT
//     reuse that logic; it builds the leading-tone RESOLUTION event (the 7̂→1̂
//     same-voice motion ACROSS the boundary — a detected event, never mere presence)
//     as the authentic-family gate, plus the genuine-dominant (seventh / resolving
//     tritone) test, now a vote STRENGTHENER (§5.2 amendment 2026-06-26: a plain
//     triad V→I with the leading-tone resolution IS authentic — the common chorale
//     phrase-end — so the seventh is not an admission requirement).
//
//   ★★ THE KEY-AGNOSTIC LIMIT — BY DESIGN, RESOLVED DOWNSTREAM (§5.2 "the key-agnostic
//     limit"; resolution ratified cc_phase5c_step2_amendment.md §7). Dropping the
//     seventh GATE removes the only event-pair separator between a plain V→I and a plain
//     I→IV: the two are EXACT TRANSPOSITIONS (Major triad → triad, root up a fourth, the
//     third of the approach resolving up a semitone to the arrival root); the key-agnostic
//     detector hypothesizes the ARRIVAL is the tonic, so for the I→IV pair the third of I
//     IS the "leading tone" and the smooth common-tone voicing (E→F in C→F) FIRES
//     leadingToneResolves. This is NOT a defect to gate here — a key-agnostic event-pair
//     test CANNOT separate the two (that needs the key, which this detector is INFORMING,
//     not reading). The disambiguation is resolved DOWNSTREAM, not in this unit:
//       (i)   the seventh / resolving tritone, when present, is a position-independent
//             dominant signature (the +wSeventh strengthener) that admits a genuine
//             dominant robustly;
//       (ii)  the PHRASE GATE (arr.endsPhrase, applied at candidate admission in every
//             cadence type) removes the COMMON false positive — a passing I→IV is
//             mid-phrase, never admitted as a candidate;
//       (iii) the rare I→IV that falls AT a phrase boundary casts only a weak SOFT
//             tonic-vote the key-layer aggregation absorbs against the home-signature
//             pull and the genuine cadences.
//     The detector casts soft evidence; it is NOT a key-aware classifier. The seventh
//     gate is NOT re-added.
//   • The circular production detector (section/sectioncadencedetection.cpp
//     detectCadences(), key-dependent on the resolved function.degree) is NOT
//     touched here — its retirement is Phase 5d.
//
// PRODUCER-AGNOSTIC (the functionprogression precedent): the detector reads only
// the small CadenceEvent view below. At engage each event is mapped from the L4
// decoder's committed chord (chord/chordslicedecoder.h SliceChord.chosen — root,
// quality, bass) PLUS its per-voice sounding notes (the L1-projected FocalNote
// stream — voice + pitch, what the resolution event and the seventh/tritone read),
// and the endsPhrase flag from the Layer-1.5 phrase-boundary primitive
// (engravingbridge/phraseboundaryview.h phraseBoundaryTicks). The detector never
// reads a producer type, so this module compiles free of the decoder / region /
// engraving headers.
//
//   ★ Why per-voice notes, not the chord-identity projection (declared §1): §5.2's
//   genuine dominant ("a seventh or its tritone resolving") and its leading-tone
//   RESOLUTION are pitch-content / VOICE-MOTION events by definition (a seventh
//   RESOLVING is a melodic fact, not a vertical identity), so this unit reads them
//   from the per-voice notes — the faithful route, no structural change required.
//   (Note: since the L4->L5 carry-fix the ChordSliceCandidate DOES carry
//   ChordIdentity.extensions — the vertical seventh is now on the projection — but
//   that names the chord's colour, not the voice-leading resolution this detector
//   needs; the per-voice channel is intrinsic here, not a carry workaround.)
//
// DORMANT (build §5): this module has NO production consumer — nothing in src/
// calls it; it is exercised only by its unit tests. So adding it is byte-identical
// on production by construction (the firewall). It becomes load-bearing when the
// function layer engages (Phase 5d), consumed by the Step-3 resolver and the
// Step-4 modulation arbiter (the cadence is its own sub-unit, §15-4).
//
// CONSTANTS ARE PRECISION-PHASE (the firewall, build §3). The tonic-vote weights
// and the per-type lower-confidence discounts are left at provisional DEFAULT
// seeds here and are NOT tuned for accuracy — that is Phase B. Only the DIRECTION
// is fixed (more evidence + more salience never lowers the vote; half / plagal /
// evaded carry a lower-confidence discount). The half cadence is the literature's
// weakest link — held at the modest default, not chased.

#include <vector>

#include "composing/analysis/types/analysistypes.h"   // ChordQuality

namespace mu::composing::analysis {

// ── One sounding note of a cadence event, projected per voice (§5.2) ───────────
//
// The leading-tone RESOLUTION (7̂→1̂) is a per-VOICE motion across the boundary, so
// the detector needs the pitch of each voice at the approach and at the arrival.
// Mapped at engage from the L1 FocalNote stream (voice + pitch); injected by hand
// in the tests.
struct CadenceVoiceNote {
    int voice = 0;   ///< voice id (the resolution is tested per voice / melodically)
    int pitch = 0;   ///< MIDI pitch (ppitch)

    int pc() const { return ((pitch % 12) + 12) % 12; }
};

// ── One event of the approach→arrival pair (§5.0 / §5.2) ──────────────────────
//
// A committed chord (root + quality + bass/inversion, from Layer 4) plus the
// per-voice sounding notes the resolution / seventh / tritone events read, plus the
// salience cues (the §3 metric weight; the phrase-boundary / final-bar markers).
struct CadenceEvent {
    int rootPc = -1;                              ///< committed root pitch class (0–11); -1 = none
    ChordQuality quality = ChordQuality::Unknown; ///< committed chord quality
    int bassPc = -1;                              ///< committed bass pitch class (0–11); -1 = none

    std::vector<CadenceVoiceNote> notes;          ///< the event's sounding notes, per voice

    double metricWeight = 1.0;   ///< §3 metric weight of the event's onset [0.5,1.0]; higher = stronger
    int startTick = 0;           ///< event start tick (raw integer)
    int endTick = 0;             ///< event end tick, exclusive

    /// True when this event coincides with a PHRASE BOUNDARY (the chorale gate):
    /// a fermata / section end / final bar — read from the Layer-1.5 phrase-boundary
    /// primitive (phraseBoundaryTicks). A cadence is admitted only at such a point
    /// (§5.2); also the structural salience cue (fermata / section end).
    bool endsPhrase = false;
    /// True when this event is the FINAL bar of the piece/section — the extra
    /// salience cue §5.2 names beyond the phrase boundary. Optional; default false.
    bool isFinalBar = false;
};

// ── The §5.2 typology ─────────────────────────────────────────────────────────
enum class FunctionalCadenceType {
    None,
    PerfectAuthentic,    ///< PAC: V(7)→I, BOTH root position, LT resolves, genuine dominant
    ImperfectAuthentic,  ///< IAC: authentic but inverted dominant/tonic, OR a viio leading-tone substitution
    Half,                ///< terminal (phrase-final) dominant — root-position triad strongest
    PhrygianHalf,        ///< minor-mode iv6→V with the bass descending a semitone (b6̂→5̂)
    Deceptive,           ///< a dominant set up to cadence arriving on the submediant (V→vi / V→bVI)
    Plagal,              ///< subdominant-family → tonic at a phrase boundary, no intervening dominant
    Evaded               ///< a dominant set up to cadence whose tonic arrival is abandoned / re-launched
};

// ── One detected cadence (the unit's output) ──────────────────────────────────
struct FunctionalCadence {
    FunctionalCadenceType type = FunctionalCadenceType::None;
    int approachTick = -1;       ///< startTick of the approach (dominant / pre-dominant) event
    int arrivalTick = -1;        ///< startTick of the arrival event

    int tonicPc = -1;            ///< the TONIC this cadence votes for (key-agnostic — derived, not read)
    bool minorMode = false;      ///< the cadential tonic's mode (best-effort from the arrival/pre-dominant)

    double tonicVote = 0.0;      ///< the §5.2 weighted tonic vote (firewall seeds; direction fixed)

    // Evidence flags (transparency + the vote inputs; oracle-tested).
    bool bassFiveToOne = false;       ///< the bass moves scale-degree 5̂→1̂ (root-position cadential bass)
    bool leadingToneResolves = false; ///< the 7̂→1̂ same-voice resolution event fired across the boundary
    bool genuineDominant = false;     ///< the dominant carries a seventh or a resolving tritone
    bool sixFourCollapsed = false;    ///< a cadential six-four was collapsed into this dominant approach
};

// ── Precision-phase constants (the firewall, build §3) — provisional seeds ─────
//
// The tonic-vote weights and per-type discounts are NOT tuned for accuracy (Phase
// B fits them). Only the DIRECTION is fixed here: every evidence / salience cue is
// non-negative (more never lowers the vote); half / plagal / evaded carry a
// lower-confidence discount. Seeds mirror the cadencekeyanchor convention
// (wBase 1.0, the structural/phrase term the largest single bonus).
struct FunctionCadenceParams {
    double wBase            = 1.0;   ///< every admitted cadence
    double wBassFiveToOne   = 1.0;   ///< evidence: bass 5̂→1̂
    double wLeadingTone     = 1.0;   ///< evidence: leading-tone resolution
    double wSeventh         = 1.0;   ///< evidence: genuine dominant (seventh / resolving tritone)
    double wMetric          = 1.0;   ///< salience: multiplied by the event metric weight [0.5,1.0]
    double wPhraseBoundary  = 2.0;   ///< salience: fermata / section end (the structural primary)
    double wFinalBar        = 1.0;   ///< salience: the final bar

    double discountHalf     = 0.5;   ///< half is the weakest reading — held lower by rule
    double discountPlagal   = 0.5;   ///< plagal is a possible post-cadential prolongation — lower by rule
    double discountEvaded   = 0.5;   ///< evaded — lower by rule
};

/// Global default cadence-detector parameters.
inline constexpr FunctionCadenceParams kDefaultFunctionCadenceParams{};

// ── Pure event-pair predicates (exposed for the oracle tests) ─────────────────

/// True when @p e is a root-position chord (bass == root, both present).
bool isRootPosition(const CadenceEvent& e) noexcept;

/// True when @p e is a SECOND-INVERSION TONIC-SPELLED triad — a Major/Minor triad
/// whose bass is its own fifth (bassPc == (rootPc + 7) mod 12). §5.2: such a
/// sonority NEVER registers as a tonic arrival (it is the cadential six-four, the
/// dominant's accented suspension), so the authentic test rejects it as an arrival.
bool isSecondInversionTonicTriad(const CadenceEvent& e) noexcept;

/// The leading-tone RESOLUTION event (§5.0 / §5.2): some voice sounding the leading
/// tone ((tonicPc - 1) mod 12) at @p dom moves, IN THAT SAME VOICE, to the tonic
/// (tonicPc) at @p arr across the boundary. This is the CORRECTED test that replaces
/// cadencekeyanchor's leading-tone-PRESENCE check (the I→IV false-positive trap):
/// resolution as a detected voice motion, never mere presence.
bool leadingToneResolves(const CadenceEvent& dom, const CadenceEvent& arr, int tonicPc) noexcept;

/// True when @p dom carries a minor seventh above its own root (the dominant-seventh
/// signature, V7) — read from the pitch content (the seventh is not on the L4
/// quality projection; §1). One half of the §5.2 "a seventh OR its tritone
/// resolving" genuine-dominant test.
bool dominantSeventhPresent(const CadenceEvent& dom) noexcept;

/// §5.2 genuine dominant: a SEVENTH present (dominantSeventhPresent), OR the
/// dominant's TRITONE RESOLVING — the dominant carries both the leading tone
/// (tonicPc-1 = 7̂) and the fourth degree (tonicPc+5 = 4̂), and across the boundary
/// 7̂→1̂ and 4̂→3̂ resolve by same-voice step to the tonic's root and third (its mode
/// from @p arr). This admits V7 (by the seventh) and a viio leading-tone chord (by
/// the resolving tritone), while a plain V / I triad — no seventh, no resolving
/// tritone — fails (the I→IV discriminator).
bool isGenuineDominant(const CadenceEvent& dom, const CadenceEvent& arr, int tonicPc) noexcept;

/// The §5.2 weighted tonic vote of one detected cadence: a monotone-increasing
/// weighted sum of the evidence cues (bass 5̂→1̂, leading-tone resolution, genuine
/// seventh) and the salience cues (metric weight, phrase boundary, final bar), minus
/// the per-type lower-confidence discount for half / plagal / evaded. Clamped at 0.
/// Direction fixed; weights are firewall seeds. Exposed for the oracle tests.
double cadenceTonicVote(const FunctionalCadence& c, const CadenceEvent& arrival,
                        const FunctionCadenceParams& params = kDefaultFunctionCadenceParams) noexcept;

// ── The detector ──────────────────────────────────────────────────────────────

/// Detect every cadence in an ordered event stream of ONE region (key-agnostic),
/// per §5.2. Applies the cadential-six-four collapse first, then the authentic /
/// deceptive / half / plagal / evaded typology on each approach→arrival pair, gated
/// by the chorale phrase boundary (events[i].endsPhrase on the arrival). Each
/// admitted cadence carries its §5.2 weighted tonic vote. Returns the detected
/// cadences in event order.
std::vector<FunctionalCadence>
detectFunctionalCadences(const std::vector<CadenceEvent>& events,
                         const FunctionCadenceParams& params = kDefaultFunctionCadenceParams);

} // namespace mu::composing::analysis
