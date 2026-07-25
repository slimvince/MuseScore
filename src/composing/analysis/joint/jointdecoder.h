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
} // namespace mu::composing::analysis::joint

#endif // MU_COMPOSING_ANALYSIS_JOINT_JOINTDECODER_H
