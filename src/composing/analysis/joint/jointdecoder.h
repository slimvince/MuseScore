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

#ifndef MU_COMPOSING_ANALYSIS_JOINT_JOINTDECODER_H
#define MU_COMPOSING_ANALYSIS_JOINT_JOINTDECODER_H

#include <array>
#include <map>
#include <optional>
#include <string>
#include <unordered_map>
#include <vector>

#include "jointadapter.h"
#include "jointprimitives.h"
#include "jointtables.h"

// The joint estimator's DECODER — the C++ port of the exact block-factorized semi-Markov Viterbi in
// probe_decoder.decode_piece, plus the candidate generation, the chord vocabulary, the within-segment
// factor scoring, and the cadence factor. Byte-for-byte parity with the Python probe is the goal
// (probe_corpus_decode.json is the oracle). The decode is a deterministic function of the note-event
// facts, the loaded tables/marginal, and the weight vector; ties are broken by the SAME
// dict-insertion order the Python uses, which this port reproduces with insertion-ordered containers.
// DORMANT (no production consumer). Spec: cowork_joint_estimator_factorization.md §5.

namespace mu::composing::analysis::joint {
// A note record (note_events.json note fields; `beat` is not used by the decode arithmetic).
struct NoteRec {
    int onset = 0, dur = 0, pc = 0, midi = 0, lof = 0, part = 0, measure = 0, mc = 0, ap = 0, dp = 0,
        tied = 0, ferm = 0;
    double beat = 0.0;
};

// An event record (note_events.json event fields).
struct EventRec {
    int start = 0, end = 0, measure = 0, mc = 0, ferm = 0;
    double beat = 0.0;
};

// A prepared piece: the event lattice + notes + the derived per-event facts the decoder reads.
struct Piece {
    std::string stem;
    std::vector<EventRec> events;
    std::vector<NoteRec> notes;
    int nQuarter = 0;

    // populated by prepare()
    std::vector<std::vector<int> > notesByEvent;    // note indices whose ONSET is in event e (non-anacrusis)
    std::vector<std::optional<int> > evBass;         // per event: lowest-midi note's pc, or none
    std::vector<PcMask> evOnsetPcs;                  // per event: onset pcs
    std::vector<char> evFermCtx;                     // per event: gfb fermata-context flag
    std::vector<std::array<int, 3> > liveNotes;       // (onset, offset, pc) for non-anacrusis notes, by onset

    void prepare();
    PcMask overlapPcs(int i, int j) const;           // pcs sounding in [start_i, end_{j-1})
    PcMask approachWindowPcs(int i) const;           // pcs sounding in the 4 beats before event i (★R1)
};

// Per-(tonic,mode,class) chord content: member pcs, ordered factors, and the (possibly chromatic) root.
struct ChordInfo {
    std::optional<PcMask> mem;
    std::optional<std::vector<ChordFactor> > fac;
    std::optional<int> root;
};

class ChordCache
{
public:
    const ChordInfo& get(const LabelClass& cls, int tonic, bool isMajor);
private:
    std::unordered_map<std::string, ChordInfo> m_cache;
};

/// The gradeable root of a chromatic class (AugSixth/Neapolitan) that chordFactorPcs leaves rootless,
/// or -1 for none (probe_decoder.chromatic_root_pc).
int chromaticRootPc(const LabelClass& cls, int tonic, bool isMajor);

// The chord-class vocabulary (inversion-free classes) — probe_decoder.Vocabulary, in Python insertion
// order (first appearance over the sorted table keys, then the chromatic completions).
class Vocabulary
{
public:
    explicit Vocabulary(const JointTables& tables);
    const std::vector<std::pair<std::string, LabelClass> >& ordered() const { return m_ordered; }
    const LabelClass* find(const std::string& ckey) const;
private:
    std::vector<std::pair<std::string, LabelClass> > m_ordered;
    std::unordered_map<std::string, size_t> m_index;
};

// One decoded segment, published as the grade-ready summary the probe artifact stores.
struct SegmentSummary {
    int i = 0, j = 0, startTick = 0, endTick = 0, tonicPc = 0;
    bool isMajor = true;
    std::string key, classKey;
    std::optional<int> rootPc;
    std::string degree, quality, inversion, target;
};

struct DecodeResult {
    std::string stem;
    std::vector<SegmentSummary> segments;
    double totalScore = 0.0;
    int nEvents = 0;
    bool complete = false;
};

// ── The posterior slice (notation output-surface contract §3.3 GROUP (i); the established
// content-score uncertainty surface). Additive: computed POST-decode by re-scoring the committed
// span under alternative readings; the decode itself is unchanged. GROUP (ii) forward-backward
// marginals are OI-193's later step and are NOT produced here. ──────────────────────────────────

// One axis of a segment's slice: a FULL candidate list (no truncation) as parallel arrays — `labels`
// and `scores` in lock-step, `committed` the index of the committed reading. The KEY axis holds the
// committed chord class re-scored under every scoreable candidate key (KEYS_24 order: tonic 0..11,
// major before minor); the CHORD axis holds every scoreable vocabulary class re-scored under the
// committed key (vocabulary class-key SORTED order). A candidate is "scoreable" iff its root is
// defined AND its within-segment content score is finite (mirrors probe_decoder._segment_posterior).
struct PosteriorAxis {
    std::vector<std::string> labels;   // key strings (key axis) or class keys (chord axis)
    std::vector<double> scores;        // weighted within-segment content score, lock-step with labels
    int committed = -1;                // index of the committed reading in labels/scores
};
struct SegmentSlice {
    PosteriorAxis keyAxis;
    PosteriorAxis chordAxis;
};

/// The per-segment posterior slice (contract §3.3 group (i)) for a decode's committed segments — the
/// C++ mirror of probe_decoder's key-axis/chord-axis re-scoring, built on segmentContentScore (so it
/// inherits the established Neumaier bit-parity). One SegmentSlice per input segment, same order.
std::vector<SegmentSlice> computePosteriorSlice(const Piece& piece,
                                                const std::vector<SegmentSummary>& segments,
                                                const FittedAdapter& adapter, const Vocabulary& vocab,
                                                ChordCache& cache);

/// Diagnostic: the weighted within-segment content score of one candidate — the value the Viterbi
/// caches as `content` (score_segment_content). Used to localize decode-parity divergences.
double segmentContentScore(const Piece& piece, int i, int j, int tonic, bool isMajor,
                           const LabelClass& cls, const FittedAdapter& adapter, ChordCache& cache);

/// The exact semi-Markov Viterbi. `segCap` = the segment-length cap in events; `sigFifths` /
/// `declaredMode` are the initial-state prior inputs. Uses the full 24-key set with the ratified
/// top-K key prune (K=6, as committed).
DecodeResult decodePiece(const Piece& piece, const FittedAdapter& adapter, const Vocabulary& vocab,
                         ChordCache& cache, int segCap, std::optional<int> sigFifths,
                         const std::string& declaredMode);

// The committed note_events.json, parsed into prepared pieces.
struct LoadedCorpus {
    bool ok = false;
    std::string error;
    int ticksPerQuarter = 0;
    std::map<std::string, Piece> pieces;
};
LoadedCorpus loadPiecesFromNoteEvents(const std::string& noteEventsPath);

// ─────────────────────────────────────────────────────────────────────────────────────────────
// OI-199 Task 1 — DEFAULT-OFF fire-count instrument (OI-110 disposition). Zero work + byte-identical
// decode output when disabled (every counting site is guarded; the returned candidate/segment data is
// untouched); an explicit jointFireSetEnabled(true) is the ONLY way to turn it on, so no production
// path ever counts. Reverted in its own commit at the dispatch close (hash recorded for a one-cherry-
// pick re-add), exactly as OI-110's L4 oracle counter was. It characterizes the joint decode to the
// L4 standard: per-filter admission rejections (candidateStates gates 1/2/3) + per-branch DP fires.

// Per-window admission breakdown, filled by candidateStates when a non-null pointer is passed (so the
// per-event coverage decomposition and the aggregate counters both read the ONE real gate logic, #6).
struct AdmitStats {
    int offered = 0;         // (key,class) pairs examined for the window
    int rejRoot = 0;         // gate (1) ROOT-PRESENT rejections
    int rejMemInvalid = 0;   // unmappable class in this key (info.mem absent)
    int rejOverlap = 0;      // gate (2) MEMBER-OVERLAP rejections (the OI-215 gate)
    int rejFit = 0;          // gate (3) FIT / non-chord-tone-budget rejections
    int admitted = 0;        // candidates admitted (returned)
    int nOnset = 0;          // distinct onset pcs in the window (the quantity gate (2) tests)
    int deepestGate = 0;     // deepest gate any class reached: 0 none, 1 root, 2 member-overlap test, 3 fit test/admit
};

struct JointFireCounters {
    // candidate admission (candidateStates) — aggregate over every examined window
    long long candWindows = 0;        // candidateStates invocations (windows examined)
    long long candOffered = 0;        // (key,class) pairs examined across all windows
    long long rejRootPresent = 0;     // gate (1) ROOT-PRESENT rejections
    long long rejMemInvalid = 0;      // unmappable class in this key
    long long rejMemberOverlap = 0;   // gate (2) MEMBER-OVERLAP rejections (the OI-215 gate)
    long long rejFit = 0;             // gate (3) FIT / NCT-budget rejections
    long long admitted = 0;           // candidates admitted
    long long onsetDiv[13] = { 0 };   // per window: histogram of distinct onset pcs (0..12, clamped)
    // decode DP (decodePiece)
    long long dpPieces = 0;
    long long dpComplete = 0;
    long long dpEmpty = 0;            // V[N] empty -> complete=false (the OI-215 OUTCOME branch)
    long long dpSegments = 0;         // committed segments across pieces
    long long trInitial = 0;         // (a) initial-segment transition was the chosen predecessor
    long long trSameKey = 0;         // (b) same-key chord transition was the chosen predecessor
    long long trKeyChange = 0;       // (c) key-change transition was the chosen predecessor
    long long trContentNegInf = 0;   // candidate skipped: content == -inf
    long long trNoBack = 0;          // candidate skipped: no admissible predecessor
    long long stInsert = 0;          // new DP state inserted at a boundary
    long long stImprove = 0;         // existing DP state improved by a §5-better path
};

void jointFireSetEnabled(bool on);
bool jointFireEnabled();
void jointFireReset();
JointFireCounters jointFireSnapshot();

// Per-event structural coverability decomposition — answers "why is an event uncoverable" per the
// three admission gates, so the OI-215 member-overlap failure is separated from any SIBLING (a
// root-present or NCT-budget failure). An event is coverable iff some <=segCap window containing it
// admits >=1 candidate. Uses the REAL candidateStates (no re-implementation, #6).
struct CoverageScan {
    int nEvents = 0;
    int uncoverable = 0;
    // uncoverable decomposition (mutually exclusive):
    int uncovMemberOverlapPure = 0;  // every covering window had <2 distinct onset pcs (the OI-215 theorem case)
    int uncovMemberOverlapRich = 0;  // some covering window had >=2 onset pcs but gate (2) still rejected all classes
    int uncovFitBlocked = 0;         // a rich covering window had a class pass gates 1&2 but fail gate (3): a SIBLING
    int uncovRootOnly = 0;           // rich covering windows never got a class past gate (1): a SIBLING
    bool complete = false;           // did a full-coverage decode exist (no uncoverable event)
};
CoverageScan scanCoverage(const Piece& piece, const Vocabulary& vocab, ChordCache& cache,
                          std::optional<int> sigFifths, int segCap);
} // namespace mu::composing::analysis::joint

#endif // MU_COMPOSING_ANALYSIS_JOINT_JOINTDECODER_H
