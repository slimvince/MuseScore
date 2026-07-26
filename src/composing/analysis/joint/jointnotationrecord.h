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

#ifndef MU_COMPOSING_ANALYSIS_JOINT_JOINTNOTATIONRECORD_H
#define MU_COMPOSING_ANALYSIS_JOINT_JOINTNOTATIONRECORD_H

#include <optional>
#include <string>
#include <vector>

#include "jointadapter.h"
#include "jointdecoder.h"
#include "jointprimitives.h"

// ── The NOTATION OUTPUT-SURFACE RECORD (the A-native record; notation output-surface contract §3) ──
//
// The data the joint estimator publishes per analyzed score span — the ONE output surface the
// in-app notation path will read (ratified Decision A2). This module type and its ONE assembly
// function realize the ratified contract cowork_notation_output_contract.md §3.1–§3.4:
//   §3.1  the piece block (analyzed span, the signature/declared-mode INPUT ECHO, the §2 provenance)
//   §3.2  per committed segment: the native decode facts verbatim + the derived chord facts
//   §3.3  per segment: the ESTABLISHED posterior slice (group (i); attached from computePosteriorSlice)
//   §3.4  per key run: the un-rounded modal reading  (ADDED by the modal-counter commit; a field here)
//   §3.5  ornament fields RESERVED-absent (OI-194's own increment; no field exists yet)
//   §3.6  the deliberately-excluded fields are simply ABSENT (no confidence sigmoid, Class-M margin,
//         21-value mode, temporalExtensions, hasAnalyzedChord, keyAlternatives, fanout, pedal-identity)
//
// DORMANT (declared dormancy, fact-publication corollary): the NAMED consumer is the seams dispatch
// (the span/note seams that read this record). Nothing in src/ reads it yet. The record is a pure
// function of the decode outputs (Piece + DecodeResult) plus the decode's prior inputs (sigFifths/
// declaredMode) and the compiled-in provenance — it NEVER re-decodes and never reads the score.
//
// Spec: cowork_notation_output_contract.md §3; cowork_notation_adoption_increment.md (Decision A2).

namespace mu::composing::analysis::joint {

// §2 provenance block — the D1 compiled-in embedded-artifact constants (discharges their declared
// dormancy: the record is their named consumer). Answers "which fitted values produced this analysis".
struct RecordProvenance {
    std::vector<std::pair<std::string, std::string> > tableArtifacts;   ///< (artifact name, sha256) ×5
    std::string weightVectorIdentity;                                   ///< the SELECTED weight identity
    std::string decoderVersion;                                         ///< the joint decoder's version
    std::string corpusGitHash;                                          ///< the fitting corpus (tables provenance)
};

// One event's bass fact within a segment (§3.2 "the bass chord-factor role per event"): the event's
// bass pitch class and its factor role among the chord members ("root"/"third"/"fifth"/"seventh"), or
// an empty role when the bass pc is not a chord member.
struct EventBassFact {
    int eventIndex = 0;                 ///< event index in the Piece's event lattice
    std::optional<int> bassPc;          ///< the event's lowest-sounding pc (none if the event is empty)
    std::string role;                   ///< the bass pc's factor role, or "" when it is not a member
    std::optional<int> spellingLof;     ///< the bass factor's tonal spelling (line-of-fifths, C=0), when
                                        ///< it is a chord factor (§3.2 bass spelling); none otherwise
};

// §3.2 — one committed segment: the native decode facts (verbatim from SegmentSummary) plus the
// ratified derived-published-fact family, each computed ONCE here (consumers read, never re-derive).
struct RecordSegment {
    // committed reading (verbatim from SegmentSummary) ────────────────────────────────────────────
    int startTick = 0, endTick = 0;
    int tonicPc = 0;
    bool isMajor = true;
    std::string key;                    ///< the decoder key string ("Cmaj"/"Amin")
    std::string classKey;               ///< the vocabulary class identity
    std::string degree, quality, inversion, target;
    std::optional<int> rootPc;

    // derived chord facts ─────────────────────────────────────────────────────────────────────────
    int keySignatureFifths = 0;                  ///< (tonic, mode) -> notated key-signature fifths
    std::optional<int> rootSpellingLof;          ///< the root's tonal spelling (line-of-fifths, C=0);
                                                 ///< none for an unmappable class (§3.2 root spelling)
    std::vector<ChordFactor> members;            ///< member pcs with factor roles (EMPTY for a chromatic
                                                 ///< class — AugSixth/Neapolitan carry no standard factors)
    std::optional<PcMask> memberPcs;             ///< the raw member pc set (carries chromatic-class members
                                                 ///< even when `members` is empty)
    std::string chordSymbol;                     ///< jointChordSymbol(rootPc, quality)
    std::string romanNumeral;                    ///< jointRenderRn (first-event bass role; batch-render form)
    bool diatonicToKey = false;                  ///< the class-native diatonic-vs-chromatic/applied answer
    std::vector<EventBassFact> bassPerEvent;     ///< the per-event bass factor role over [i, j)
    std::string augSixthSubType;                 ///< "Italian"/"German"/"French" for an AugSixth class; else ""

    // §3.5 ornament labels: RESERVED-absent — delivered by OI-194's own increment, no field exists yet.
    // §3.6 excluded fields (confidence sigmoid, Class-M margin, 21-value mode, temporalExtensions,
    //      hasAnalyzedChord, keyAlternatives, fanout, pedal-identity): deliberately NOT declared here.
};

// ── §3.4 the un-rounded modal reading (C1; per key run) ───────────────────────────────────────────
// One observed chromatic inflection of a scale degree within a key run, identified by pitch-class
// offset (contract §3.4: "inflection identity by pitch-class offset, with the notated tpc recorded
// beside"). Un-rounded counts only — no label, no threshold, no rounding.
struct ModalInflection {
    int pcOffset = 0;                ///< (note pc - tonic pc) mod 12 — the inflection identity
    int notatedLofOffset = 0;        ///< the note's tonal spelling relative to the tonic (note lof - key
                                     ///< tonic lof) — the tpc "recorded beside" (well-defined per cell)
    long long durationTicks = 0;     ///< summed notated duration of notes ONSETTING in the run at this cell
    int onsetCount = 0;              ///< number of such note onsets
};
// One scale degree (1..7) of the run's key with every observed inflection (sorted by pcOffset).
struct ModalDegree {
    int degree = 0;                  ///< 1..7 (the letter-based scale degree of the key)
    std::vector<ModalInflection> inflections;
};
// A maximal run of consecutive committed segments sharing one key, with its modal reading (degrees
// that have any observed note, in ascending degree order).
struct ModalKeyRun {
    int startTick = 0, endTick = 0;
    int tonicPc = 0;
    bool isMajor = true;
    std::vector<ModalDegree> degrees;
};

// The full record for one analyzed piece/span.
struct NotationRecord {
    std::string stem;

    // §3.1 piece block ────────────────────────────────────────────────────────────────────────────
    int spanStartTick = 0, spanEndTick = 0;      ///< the analyzed span (ticks)
    std::optional<int> sigFifths;                ///< notated initial signature fifths, INPUT ECHO
    std::string declaredMode;                    ///< notated declared mode ("major"/"minor"/""), INPUT ECHO
    // NOTE: the fact adapter (AdapterFacts) exposes only the INITIAL signature/mode; it publishes no
    // mid-piece notated signature-change re-anchor points, so §3.1's OI-94(a) re-anchor list is empty
    // here (recorded, not invented — adding a score read would breach the L1-only isolation, OI-180).
    RecordProvenance provenance;

    // §3.2 committed segments (same order as the decode) ──────────────────────────────────────────
    std::vector<RecordSegment> segments;

    // §3.3 group (i) — the established posterior slice, one per segment (same order as `segments`).
    std::vector<SegmentSlice> slices;

    // §3.4 the un-rounded modal reading, one entry per key run (C1; ratified decision 1).
    std::vector<ModalKeyRun> modalReading;
};

/// Assemble the notation record for a decoded piece (contract §3.1–§3.3). Score-decode-INDEPENDENT:
/// it consumes the already-computed `piece`/`result` and the decode's prior inputs (`sigFifths`/
/// `declaredMode`, the §3.1 input echo), and re-scores the committed spans for the §3.3 slice — it
/// NEVER re-decodes and never reads the score. `adapter`/`vocab`/`cache` are the decode's own; the
/// §2 provenance is read from the compiled-in embedded constants (Decision D1).
NotationRecord assembleNotationRecord(const Piece& piece, const DecodeResult& result,
                                      std::optional<int> sigFifths, const std::string& declaredMode,
                                      const FittedAdapter& adapter, const Vocabulary& vocab,
                                      ChordCache& cache);

/// The §3.4 un-rounded modal reading over the decode's KEY RUNS (maximal consecutive same-key
/// segments). For each key run and each scale degree 1..7 of its key, the sounding duration and onset
/// count of EVERY chromatic inflection of that degree observed in the run — counted from the Piece's
/// notated notes (degree from the notated spelling, inflection keyed by pitch-class offset). No label,
/// no threshold, no rounding (C1's publication; the presentation layer formats later). `referenceFifths`
/// is the notated signature (the enharmonic reference for each run's key tonic spelling).
std::vector<ModalKeyRun> computeModalReading(const Piece& piece, const DecodeResult& result,
                                             int referenceFifths);

/// The class-native `diatonicToKey` answer (§3.2): TRUE iff the class is a plain diatonic-degree chord
/// of the key's mode — an unaltered scale degree (no ♭/♯ in the degree base), no applied target, and
/// not a chromatic predefined family (AugSixth/Neapolitan). A purely structural read of the class (no
/// pitch-collection recomputation — OI-173's lesson). Rule documented at the definition.
bool recordDiatonicToKey(const LabelClass& cls);

/// The augmented-sixth display sub-type ("Italian"/"German"/"French") derived from the pitch classes
/// SOUNDING over the segment [i, j) relative to `tonicPc` (contract §3.2's corrected derivation — the
/// vocabulary class collapsed the family to Italian content, so the sub-type is read from the sounding
/// content, not the class). Empty for a non-AugSixth class. Rule documented at the definition.
std::string recordAugSixthSubType(const Piece& piece, int i, int j, int tonicPc);

} // namespace mu::composing::analysis::joint

#endif // MU_COMPOSING_ANALYSIS_JOINT_JOINTNOTATIONRECORD_H
