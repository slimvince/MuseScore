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

#include "jointdecoder.h"

#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iterator>
#include <limits>
#include <tuple>

#include "serialization/json.h"
#include "types/bytearray.h"

namespace mu::composing::analysis::joint {
namespace {
constexpr double NEG_INF = -std::numeric_limits<double>::infinity();
constexpr int kKeyPruneTopK = 6;
constexpr int kCadenceApproachTicks = 4 * 480;   // ★R1: the four-beat approach window
const std::string kStartEnc = "\x02START";

// gen_note_tables._MC_INV / _MV_INV
const std::array<std::string, 4> kMcName = { "downbeat", "mid_strong", "other_tactus", "sub_tactus" };
const std::array<std::string, 3> kMvName = { "none", "step", "leap" };
// (The pc->keyname spelling — probe_decoder._PC_KEYNAME — is the module's single primitive
// jointprimitives::pcKeyName, used by keyString below and by jointrender's chord symbol; #6.)

int popcount(PcMask m)
{
    int c = 0;
    while (m) {
        c += (m & 1u);
        m >>= 1;
    }
    return c;
}

std::string stateEnc(int tonic, bool major, const std::string& ckey)
{
    return std::to_string(tonic) + "|" + (major ? "1" : "0") + "|" + ckey;
}

std::string keyEnc(int tonic, bool major)
{
    return std::to_string(tonic) + "|" + (major ? "1" : "0");
}

std::string keyString(int tonic, bool major)
{
    return pcKeyName(tonic) + (major ? "maj" : "min");
}

std::optional<int> eventBassPc(const Piece& p, const std::vector<int>& noteIdx)
{
    if (noteIdx.empty()) {
        return std::nullopt;
    }
    int loMidi = std::numeric_limits<int>::max();
    int loPc = 0;
    for (int idx : noteIdx) {
        if (p.notes[idx].midi < loMidi) {
            loMidi = p.notes[idx].midi;
            loPc = p.notes[idx].pc;
        }
    }
    return loPc;
}
} // namespace

// ── OI-199 Task 1 fire-count instrument state (DEFAULT-OFF; reverted at close per OI-110) ──────────
namespace {
JointFireCounters g_fc;
bool g_fcOn = false;
} // namespace

void jointFireSetEnabled(bool on) { g_fcOn = on; }
bool jointFireEnabled() { return g_fcOn; }
void jointFireReset() { g_fc = JointFireCounters(); }
JointFireCounters jointFireSnapshot() { return g_fc; }

// ── Piece ───────────────────────────────────────────────────────────────────────────────────

void Piece::prepare()
{
    const size_t nEv = events.size();
    notesByEvent.assign(nEv, {});
    std::vector<int> starts(nEv);
    for (size_t e = 0; e < nEv; ++e) {
        starts[e] = events[e].start;
    }
    for (size_t ni = 0; ni < notes.size(); ++ni) {
        const NoteRec& n = notes[ni];
        if (n.measure == 0) {
            continue;                       // anacrusis notes excluded (OI-184(a))
        }
        // event whose [start,end) contains the note's onset (events partition by onset/offset)
        const auto it = std::upper_bound(starts.begin(), starts.end(), n.onset);
        const long i = (it - starts.begin()) - 1;
        if (i >= 0 && i < static_cast<long>(nEv)
            && events[i].start <= n.onset && n.onset < events[i].end) {
            notesByEvent[i].push_back(static_cast<int>(ni));
        }
    }
    evBass.assign(nEv, std::nullopt);
    evOnsetPcs.assign(nEv, 0);
    for (size_t e = 0; e < nEv; ++e) {
        evBass[e] = eventBassPc(*this, notesByEvent[e]);
        PcMask m = 0;
        for (int idx : notesByEvent[e]) {
            m |= static_cast<PcMask>(1u << notes[idx].pc);
        }
        evOnsetPcs[e] = m;
    }
    liveNotes.clear();
    for (const NoteRec& n : notes) {
        if (n.measure != 0) {
            liveNotes.push_back({ n.onset, n.onset + n.dur, n.pc });
        }
    }
    std::sort(liveNotes.begin(), liveNotes.end(),
              [](const std::array<int, 3>& a, const std::array<int, 3>& b) { return a[0] < b[0]; });

    // the boundary factor's fermata covariate per event — gen_fermata_boundary.event_ferm_ctx_flags.
    std::vector<int> fermOff, fermOn;    // ends/begins of non-anacrusis fermata notes
    for (const NoteRec& n : notes) {
        if (n.measure == 0 || n.ferm == 0) {
            continue;
        }
        fermOn.push_back(n.onset);
        fermOff.push_back(n.onset + n.dur);
    }
    std::sort(fermOff.begin(), fermOff.end());
    std::sort(fermOn.begin(), fermOn.end());
    evFermCtx.assign(nEv, 0);
    for (size_t e = 0; e < nEv; ++e) {
        const bool own = events[e].ferm != 0;
        const bool endsAtStart = std::binary_search(fermOff.begin(), fermOff.end(), events[e].start);
        const bool beginsAtEnd = std::binary_search(fermOn.begin(), fermOn.end(), events[e].end);
        evFermCtx[e] = (own || endsAtStart || beginsAtEnd) ? 1 : 0;
    }
}

PcMask Piece::overlapPcs(int i, int j) const
{
    const int start = events[i].start;
    const int end = events[j - 1].end;
    PcMask m = 0;
    for (const std::array<int, 3>& ln : liveNotes) {
        if (ln[0] >= end) {
            break;
        }
        if (ln[1] > start) {
            m |= static_cast<PcMask>(1u << ln[2]);
        }
    }
    return m;
}

PcMask Piece::approachWindowPcs(int i) const
{
    const int t0 = events[i].start;
    const int lo = std::max(0, t0 - kCadenceApproachTicks);
    PcMask m = 0;
    for (const std::array<int, 3>& ln : liveNotes) {
        if (ln[0] >= t0) {
            break;
        }
        if (ln[1] > lo) {
            m |= static_cast<PcMask>(1u << ln[2]);
        }
    }
    return m;
}

// ── chord content cache + chromatic root ────────────────────────────────────────────────────

int chromaticRootPc(const LabelClass& cls, int tonic, bool isMajor)
{
    const Framework fr = frameworkAndRoot(cls, tonic, isMajor);
    if (!fr.valid) {
        return -1;
    }
    if (fr.hasRoot) {
        return fr.root;
    }
    if (cls.quality() == "AugSixth") {
        return fr.fwTonic;
    }
    if (cls.quality() == "Neapolitan") {
        return normalizePc(fr.fwTonic + 1);
    }
    return -1;
}

const ChordInfo& ChordCache::get(const LabelClass& cls, int tonic, bool isMajor)
{
    const std::string key = stateEnc(tonic, isMajor, cls.key());
    const auto it = m_cache.find(key);
    if (it != m_cache.end()) {
        return it->second;
    }
    ChordInfo info;
    info.mem = memberPcs(cls, tonic, isMajor);
    info.fac = chordFactorPcs(cls, tonic, isMajor);
    if (info.fac.has_value()) {
        info.root = (*info.fac)[0].pc;
    } else {
        const int r = chromaticRootPc(cls, tonic, isMajor);
        info.root = (r >= 0) ? std::optional<int>(r) : std::nullopt;
    }
    return m_cache.emplace(key, std::move(info)).first->second;
}

// ── Vocabulary ──────────────────────────────────────────────────────────────────────────────

Vocabulary::Vocabulary(const JointTables& tables)
{
    // gather the source keys (from-keys + non-pooled outcomes + entry keys)
    static const std::string guillemet = "«";     // «
    std::set<std::string> keys;
    for (const KatzTable* t1 : { &tables.t1Major, &tables.t1Minor }) {
        for (const auto& rowPair : t1->rows) {
            keys.insert(rowPair.first);
            for (const auto& outcome : rowPair.second.dist) {
                if (!startsWith(outcome.first, guillemet) && outcome.first != "BASE") {
                    keys.insert(outcome.first);
                }
            }
        }
    }
    for (const auto& kv : tables.t3) {
        if (kv.first != "BASE" && !startsWith(kv.first, guillemet)) {
            keys.insert(kv.first);
        }
    }
    std::set<std::string> seen;
    for (const std::string& k : keys) {                // std::set iterates sorted == Python sorted()
        const LabelClass lc = classFromKey(k).inversionFree();
        if (lc.rawUnnormalized() || lc.quality() == "triad" || lc.quality() == "seventh") {
            continue;
        }
        const std::string ck = lc.key();
        if (seen.insert(ck).second) {
            m_index[ck] = m_ordered.size();
            m_ordered.push_back({ ck, lc });
        }
    }
    // chromatic completion: the Neapolitan (0 GT tokens, no table row) — probe_decoder.CHROMATIC_COMPLETION_KEYS
    for (const char* kkey : { "N | Neapolitan |  | " }) {
        const LabelClass lc = classFromKey(kkey).inversionFree();
        const std::string ck = lc.key();
        if (!lc.rawUnnormalized() && seen.insert(ck).second) {
            m_index[ck] = m_ordered.size();
            m_ordered.push_back({ ck, lc });
        }
    }
}

const LabelClass* Vocabulary::find(const std::string& ckey) const
{
    const auto it = m_index.find(ckey);
    return it != m_index.end() ? &m_ordered[it->second].second : nullptr;
}

// ── within-segment factor scoring ─────────────────────────────────────────────────────────────

namespace {
struct ContentFeatures {
    double emission = 0.0, spelling = 0.0, bass = 0.0, missing = 0.0, boundary = 0.0;
    bool valid = false;
};

ContentFeatures segmentFeatures(const Piece& piece, int i, int j, int tonic, bool isMajor,
                                const LabelClass& cls, const FittedAdapter& adapter, ChordCache& cache,
                                PcMask segPcs)
{
    ContentFeatures b;
    const ChordInfo& info = cache.get(cls, tonic, isMajor);
    if (!info.mem.has_value()) {
        return b;                          // invalid — unmappable class in this key
    }
    b.valid = true;
    const PcMask mem = *info.mem;
    const int nEvents = j - i;
    const int keyLof = pcToFifths(tonic);

    for (int e = i; e < j; ++e) {
        for (int idx : piece.notesByEvent[e]) {
            const NoteRec& n = piece.notes[idx];
            const std::string cat = noteCategory(n.pc, mem, tonic, isMajor);
            b.emission += adapter.emissionLogp(cat, kMcName[n.mc], kMvName[n.ap], kMvName[n.dp], n.tied != 0);
            b.spelling += adapter.spellingLogp(spellingBin(n.lof - keyLof, isMajor), isMajor);
        }
    }

    const bool seventh = info.fac.has_value() && info.fac->size() == 4;
    const std::string family = seventh ? "seventh" : "triad";
    std::unordered_map<int, std::string> facPc;
    if (info.fac.has_value()) {
        for (const ChordFactor& f : *info.fac) {
            facPc[f.pc] = f.role;
        }
    }
    for (int e = i; e < j; ++e) {
        if (!piece.evBass[e].has_value()) {
            continue;
        }
        const auto it = facPc.find(*piece.evBass[e]);
        const std::string* rolePtr = (it != facPc.end()) ? &it->second : nullptr;
        b.bass += adapter.bassLogp(rolePtr, family, cls.degreeBase(), cls.quality(), isMajor);
    }

    if (info.fac.has_value()) {
        for (const ChordFactor& f : *info.fac) {
            if (!((segPcs >> f.pc) & 1u)) {
                b.missing += nEvents * adapter.factorAbsentLogp(f.role, family);
            }
        }
    }

    for (int e = i; e < j; ++e) {
        b.boundary += adapter.boundaryLogp(kMcName[piece.events[e].mc], e == i, piece.evFermCtx[e] != 0);
    }
    return b;
}

double weightedContent(const ContentFeatures& f, const WeightVector& w)
{
    // BIT-IDENTICAL to probe_decoder.weighted_content, which sums the five weighted terms with Python's
    // builtin sum() — and CPython 3.12+ sum() uses NEUMAIER (Kahan-Babuska) compensated summation for
    // floats. A naive left-to-right sum drifts ~1 ULP vs the compensated one, which flips exact-tie-
    // adjacent boundary decisions in the semi-Markov Viterbi and breaks decode parity with the pinned
    // reference (#16 reproducibility). We mirror the compensated sum over the SAME term order
    // (CONTENT_FEATURES: emission, spelling, bass, missing_tone→emission-weight, boundary). /fp:precise
    // (the build default) preserves the compensation; verified bit-identical to the reference.
    const double terms[5] = {
        f.emission * w.get("emission"), f.spelling * w.get("spelling"), f.bass * w.get("bass"),
        f.missing * w.get("emission"), f.boundary * w.get("boundary")
    };
    return neumaierSum(terms, 5);
}

// cadence features toward (tonic,isMajor) at the boundary starting event i (approach i-1 -> arrival i).
// isMajor is part of the probe_decoder signature but the four features are mode-independent (tonic-
// relative pcs only), so it is deliberately unused here — matching probe_decoder._cadence_fired.
std::array<bool, 4> cadenceFired(const Piece& piece, int i, int tonic, [[maybe_unused]] bool isMajor)
{
    const int lt = normalizePc(tonic + 11);
    const int fourth = normalizePc(tonic + 5);
    const int fifth = normalizePc(tonic + 7);
    const int one = normalizePc(tonic);
    PcMask apPcs = 0, arPcs = 0;
    for (int idx : piece.notesByEvent[i - 1]) {
        apPcs |= static_cast<PcMask>(1u << piece.notes[idx].pc);
    }
    for (int idx : piece.notesByEvent[i]) {
        arPcs |= static_cast<PcMask>(1u << piece.notes[idx].pc);
    }
    const std::optional<int> apBass = eventBassPc(piece, piece.notesByEvent[i - 1]);
    const std::optional<int> arBass = eventBassPc(piece, piece.notesByEvent[i]);
    const PcMask win = piece.approachWindowPcs(i);

    // fermata cadence context (probe_decoder._fermata_cadence_ctx)
    bool ferm = false;
    const int nEv = static_cast<int>(piece.events.size());
    if (i > 0 && i < nEv) {
        auto fermAt = [&](int e) { return piece.events[e].ferm != 0; };
        bool at = fermAt(i) || fermAt(i - 1);
        bool displaced = false;
        if (i + 1 < nEv) {
            const bool arrStrong = piece.events[i].mc == 0 || piece.events[i].mc == 1;
            if (arrStrong && fermAt(i + 1) && (piece.events[i + 1].mc == 2 || piece.events[i + 1].mc == 3)) {
                displaced = true;
            }
        }
        ferm = at || displaced;
    }

    std::array<bool, 4> fired{};   // leading_tone, tritone_pair, dominant_tonic_bass, fermata_location
    fired[0] = ((apPcs >> lt) & 1u) && ((arPcs >> one) & 1u);
    fired[1] = ((win >> fourth) & 1u) && ((win >> lt) & 1u);
    fired[2] = apBass.has_value() && arBass.has_value() && (*apBass == fifth) && (*arBass == one);
    fired[3] = ferm;
    return fired;
}

// candidate keys: top-K by onset-pc overlap with the collection, always keep the signature key.
std::vector<std::pair<int, bool> > candidateKeys(PcMask onsetPcs, const std::optional<std::pair<int, bool> >& sigKey)
{
    struct Scored { int negOv; int tonic; int minorFlag; int tt; bool mm; };
    std::vector<Scored> scored;
    scored.reserve(24);
    for (int t = 0; t < 12; ++t) {
        for (bool m : { true, false }) {
            const int ov = popcount(onsetPcs & keyCollectionMask(t, m));
            scored.push_back({ -ov, t, m ? 0 : 1, t, m });
        }
    }
    std::sort(scored.begin(), scored.end(), [](const Scored& a, const Scored& b) {
        return std::tie(a.negOv, a.tonic, a.minorFlag) < std::tie(b.negOv, b.tonic, b.minorFlag);
    });
    std::vector<std::pair<int, bool> > keep;
    for (int k = 0; k < kKeyPruneTopK && k < static_cast<int>(scored.size()); ++k) {
        keep.push_back({ scored[k].tt, scored[k].mm });
    }
    if (sigKey.has_value()
        && std::find(keep.begin(), keep.end(), *sigKey) == keep.end()) {
        keep.push_back(*sigKey);
    }
    return keep;
}

std::vector<std::tuple<int, bool, std::string> > candidateStates(
    const Piece& piece, int i, int j, const Vocabulary& vocab, ChordCache& cache,
    const std::optional<std::pair<int, bool> >& sigKey, AdmitStats* stats = nullptr)
{
    PcMask onsetPcs = 0;
    for (int e = i; e < j; ++e) {
        onsetPcs |= piece.evOnsetPcs[e];
    }
    const std::vector<std::pair<int, bool> > keys = candidateKeys(onsetPcs, sigKey);
    const int nOnset = popcount(onsetPcs);
    const int maxNcts = std::max(1, j - i);
    // OI-199 fire-count: per-window admission breakdown (only when instrumented; byte-identical off).
    const bool count = (stats != nullptr) || g_fcOn;
    AdmitStats local;                      // scratch when no external stats requested but counting on
    AdmitStats* st = stats ? stats : (count ? &local : nullptr);
    if (st) {
        *st = AdmitStats();
        st->nOnset = nOnset;
    }
    int deepest = 0;                       // deepest gate any class reached this window
    std::vector<std::tuple<int, bool, std::string> > cand;
    for (const auto& km : keys) {
        for (const auto& cp : vocab.ordered()) {
            const ChordInfo& info = cache.get(cp.second, km.first, km.second);
            if (st) { ++st->offered; }
            if (!info.root.has_value() || !((onsetPcs >> *info.root) & 1u)) {
                if (st) { ++st->rejRoot; }
                continue;                  // (1) ROOT-PRESENT   [class level 0]
            }
            if (deepest < 1) { deepest = 1; }
            if (!info.mem.has_value()) {
                if (st) { ++st->rejMemInvalid; }
                continue;                  // [class level 1: passed gate 1, unmappable]
            }
            const int present = popcount(*info.mem & onsetPcs);
            if (present < std::min(2, popcount(*info.mem))) {
                if (st) { ++st->rejOverlap; }
                if (deepest < 2) { deepest = 2; }
                continue;                  // (2) MEMBER-OVERLAP  [class level 2: reached gate 2]
            }
            if ((nOnset - present) > maxNcts) {
                if (st) { ++st->rejFit; }
                deepest = 3;
                continue;                  // (3) FIT             [class level 3: reached gate 3]
            }
            deepest = 3;
            if (st) { ++st->admitted; }
            cand.push_back({ km.first, km.second, cp.first });
        }
    }
    if (st) { st->deepestGate = deepest; }
    if (g_fcOn) {
        ++g_fc.candWindows;
        g_fc.candOffered += st->offered;
        g_fc.rejRootPresent += st->rejRoot;
        g_fc.rejMemInvalid += st->rejMemInvalid;
        g_fc.rejMemberOverlap += st->rejOverlap;
        g_fc.rejFit += st->rejFit;
        g_fc.admitted += st->admitted;
        ++g_fc.onsetDiv[nOnset < 0 ? 0 : (nOnset > 12 ? 12 : nOnset)];
    }
    return cand;
}
} // namespace

double segmentContentScore(const Piece& piece, int i, int j, int tonic, bool isMajor,
                           const LabelClass& cls, const FittedAdapter& adapter, ChordCache& cache)
{
    const ContentFeatures feat = segmentFeatures(piece, i, j, tonic, isMajor, cls, adapter, cache,
                                                 piece.overlapPcs(i, j));
    return feat.valid ? weightedContent(feat, adapter.weights()) : NEG_INF;
}

std::vector<SegmentSlice> computePosteriorSlice(const Piece& piece,
                                                const std::vector<SegmentSummary>& segments,
                                                const FittedAdapter& adapter, const Vocabulary& vocab,
                                                ChordCache& cache)
{
    // The CHORD axis iterates the vocabulary in SORTED class-key order — probe_decoder iterates
    // vocab.keylist = sorted(classes); the reference artifact's chord_axis_labels are in this order.
    // (byte-lexicographic == Python's sorted() on these ASCII class keys.)
    std::vector<const std::pair<std::string, LabelClass>*> sortedClasses;
    sortedClasses.reserve(vocab.ordered().size());
    for (const auto& cp : vocab.ordered()) {
        sortedClasses.push_back(&cp);
    }
    std::sort(sortedClasses.begin(), sortedClasses.end(),
              [](const std::pair<std::string, LabelClass>* a, const std::pair<std::string, LabelClass>* b) {
                  return a->first < b->first;
              });

    std::vector<SegmentSlice> out;
    out.reserve(segments.size());
    for (const SegmentSummary& s : segments) {
        SegmentSlice slice;
        const LabelClass* committedCls = vocab.find(s.classKey);

        // KEY axis: the committed chord class re-scored under every scoreable candidate key, in
        // KEYS_24 order (tonic 0..11, major before minor). Filter == probe_decoder._segment_posterior:
        // root defined AND finite content score. The committed key is flagged by its list index.
        if (committedCls) {
            for (int t = 0; t < 12; ++t) {
                for (bool m : { true, false }) {
                    const ChordInfo& info = cache.get(*committedCls, t, m);
                    if (!info.root.has_value()) {
                        continue;
                    }
                    const double sc = segmentContentScore(piece, s.i, s.j, t, m, *committedCls, adapter, cache);
                    if (sc == NEG_INF) {
                        continue;
                    }
                    if (t == s.tonicPc && m == s.isMajor) {
                        slice.keyAxis.committed = static_cast<int>(slice.keyAxis.labels.size());
                    }
                    slice.keyAxis.labels.push_back(keyString(t, m));
                    slice.keyAxis.scores.push_back(sc);
                }
            }
        }

        // CHORD axis: every scoreable vocabulary class re-scored under the committed key, sorted order.
        for (const auto* cp : sortedClasses) {
            const ChordInfo& info = cache.get(cp->second, s.tonicPc, s.isMajor);
            if (!info.root.has_value()) {
                continue;
            }
            const double sc = segmentContentScore(piece, s.i, s.j, s.tonicPc, s.isMajor, cp->second,
                                                  adapter, cache);
            if (sc == NEG_INF) {
                continue;
            }
            if (cp->first == s.classKey) {
                slice.chordAxis.committed = static_cast<int>(slice.chordAxis.labels.size());
            }
            slice.chordAxis.labels.push_back(cp->first);
            slice.chordAxis.scores.push_back(sc);
        }
        out.push_back(std::move(slice));
    }
    return out;
}

// ── the exact semi-Markov Viterbi ─────────────────────────────────────────────────────────────

DecodeResult decodePiece(const Piece& piece, const FittedAdapter& adapter, const Vocabulary& vocab,
                         ChordCache& cache, int segCap, std::optional<int> sigFifths,
                         const std::string& declaredMode)
{
    DecodeResult result;
    result.stem = piece.stem;
    const int N = static_cast<int>(piece.events.size());
    result.nEvents = N;
    const WeightVector& w = adapter.weights();
    const double wPrior = w.get("prior"), wDmode = w.get("declared_mode");
    const double wEntry = w.get("entry"), wKey = w.get("key_trans"), wChord = w.get("chord_trans");
    const bool cadenceOn = adapter.anyCadenceWeight();

    // the notated-signature major key is always kept (KEYS_24 order: t=0..11, major before minor)
    std::optional<std::pair<int, bool> > sigKey;
    if (sigFifths.has_value()) {
        for (int t = 0; t < 12 && !sigKey.has_value(); ++t) {
            if (collectionFifths(t, true) == *sigFifths) {
                sigKey = std::make_pair(t, true);
            }
        }
    }

    struct StateEntry { int tonic; bool major; std::string ckey; double score; int backI; std::string backEnc; };
    struct Boundary {
        bool hasStart = false;
        double startScore = 0.0;
        std::vector<StateEntry> states;
        std::unordered_map<std::string, size_t> idx;
    };
    std::vector<Boundary> V(N + 1);
    V[0].hasStart = true;
    V[0].startScore = 0.0;

    // ── the §5 tie-break (user-ratified 2026-07-20; cowork_joint_estimator_factorization.md §5) ──
    // Exact-score ties resolve by a declared TOTAL ORDER on paths (no epsilon): fewer segments; then
    // the earliest boundary-tick sequence (lexicographic); then the canonical class-key order of the
    // state sequence. This is the C++ mirror of probe_decoder.decode_piece's §5 helpers. The fast
    // path is the raw score compare — the sig walk fires ONLY on an exact (bit-equal) tie.
    struct PathSig {
        std::vector<int> ticks;                                    // segment start ticks
        std::vector<std::tuple<int, int, std::string> > keys;       // canonical state keys (tonic, major?0:1, ckey)
    };
    auto sigLess = [](const PathSig& a, const PathSig& b) -> bool {
        if (a.keys.size() != b.keys.size()) {
            return a.keys.size() < b.keys.size();                   // fewer segments
        }
        if (a.ticks != b.ticks) {
            return a.ticks < b.ticks;                              // earliest boundary-tick sequence
        }
        return a.keys < b.keys;                                     // canonical class-key order
    };
    auto prefixSig = [&](int bi, const std::string& bstateEnc) -> PathSig {
        PathSig s;
        if (bstateEnc == kStartEnc) {
            return s;
        }
        int jj = bi;
        std::string enc = bstateEnc;
        while (enc != kStartEnc) {
            const Boundary& B = V[jj];
            const auto it = B.idx.find(enc);
            const StateEntry& e = B.states[it->second];
            s.ticks.push_back(piece.events[e.backI].start);        // e's segment starts at event backI
            s.keys.emplace_back(e.tonic, e.major ? 0 : 1, e.ckey);
            jj = e.backI;
            enc = e.backEnc;
        }
        std::reverse(s.ticks.begin(), s.ticks.end());
        std::reverse(s.keys.begin(), s.keys.end());
        return s;
    };
    auto fullSig = [&](int bi, const std::string& bstateEnc, int tonic, bool major,
                       const std::string& ckey) -> PathSig {
        PathSig s = prefixSig(bi, bstateEnc);
        s.ticks.push_back(piece.events[bi].start);
        s.keys.emplace_back(tonic, major ? 0 : 1, ckey);
        return s;
    };
    // A = (score, bi, bstateEnc, state) strictly §5-preferred over B?
    auto better = [&](double aScore, int aBi, const std::string& aEnc, int aT, bool aM, const std::string& aC,
                      double bScore, int bBi, const std::string& bEnc, int bT, bool bM, const std::string& bC) -> bool {
        if (aScore != bScore) {
            return aScore > bScore;
        }
        return sigLess(fullSig(aBi, aEnc, aT, aM, aC), fullSig(bBi, bEnc, bT, bM, bC));
    };
    // A = (val, prefix ending in state aEnc at boundary atI) strictly §5-preferred over B?
    auto betterPrefix = [&](double aVal, const std::string& aEnc, double bVal, const std::string& bEnc,
                            int atI) -> bool {
        if (aVal != bVal) {
            return aVal > bVal;
        }
        return sigLess(prefixSig(atI, aEnc), prefixSig(atI, bEnc));
    };

    // caches
    std::unordered_map<long long, PcMask> overlapCache;
    std::unordered_map<std::string, double> contentCache;
    std::unordered_map<std::string, std::vector<std::tuple<int, bool, std::string> > > candCache;
    std::unordered_map<std::string, std::array<bool, 4> > cadCache;
    auto ijKey = [](int i, int j) { return static_cast<long long>(i) * 100000 + j; };

    auto overlap = [&](int i, int j) -> PcMask {
        const long long k = ijKey(i, j);
        const auto it = overlapCache.find(k);
        if (it != overlapCache.end()) {
            return it->second;
        }
        const PcMask v = piece.overlapPcs(i, j);
        overlapCache.emplace(k, v);
        return v;
    };
    auto candidates = [&](int i, int j) -> const std::vector<std::tuple<int, bool, std::string> >& {
        const std::string k = std::to_string(i) + "," + std::to_string(j);
        const auto it = candCache.find(k);
        if (it != candCache.end()) {
            return it->second;
        }
        return candCache.emplace(k, candidateStates(piece, i, j, vocab, cache, sigKey)).first->second;
    };
    auto content = [&](int i, int j, int tonic, bool major, const std::string& ckey) -> double {
        const std::string k = std::to_string(i) + "," + std::to_string(j) + "," + stateEnc(tonic, major, ckey);
        const auto it = contentCache.find(k);
        if (it != contentCache.end()) {
            return it->second;
        }
        const ContentFeatures feat = segmentFeatures(piece, i, j, tonic, major, *vocab.find(ckey),
                                                     adapter, cache, overlap(i, j));
        const double v = feat.valid ? weightedContent(feat, w) : NEG_INF;
        contentCache.emplace(k, v);
        return v;
    };
    auto cadenceAt = [&](int i, int tonic, bool major) -> double {
        if (!cadenceOn || i <= 0) {
            return 0.0;
        }
        const std::string k = stateEnc(tonic, major, "@" + std::to_string(i));
        const auto it = cadCache.find(k);
        const std::array<bool, 4>& fired = (it != cadCache.end())
            ? it->second : cadCache.emplace(k, cadenceFired(piece, i, tonic, major)).first->second;
        static const std::array<const char*, 4> names = { "leading_tone", "tritone_pair",
                                                          "dominant_tonic_bass", "fermata_location" };
        // BIT-IDENTICAL to probe_decoder.cadence_at's sum(w[f] for fired f) — Neumaier-compensated
        // (Python sum()), over the fired features in CADENCE_FEATURES order. Naive would drift ~1 ULP
        // on the weighted arms.
        double terms[4];
        int nt = 0;
        for (int f = 0; f < 4; ++f) {
            if (fired[f]) {
                terms[nt++] = adapter.cadenceWeight(names[f]);
            }
        }
        return neumaierSum(terms, nt);
    };

    // per-boundary summary of V[i] (in insertion order — the tie-break order Python's dicts give)
    struct KeyBest { int tonic; bool major; double score; std::string arg; };
    struct Summary {
        bool ready = false;
        bool hasStart = false;
        double startScore = 0.0;
        std::vector<KeyBest> keyBest;
        std::unordered_map<std::string, size_t> keyIdx;
        std::unordered_map<std::string, std::vector<std::pair<std::string, double> > > perClass;
    };
    std::vector<Summary> summ(N + 1);
    auto summarize = [&](int i) -> const Summary& {
        Summary& s = summ[i];
        if (s.ready) {
            return s;
        }
        s.ready = true;
        s.hasStart = V[i].hasStart;
        s.startScore = V[i].startScore;
        for (const StateEntry& e : V[i].states) {
            const std::string kk = keyEnc(e.tonic, e.major);
            s.perClass[kk].push_back({ e.ckey, e.score });
            const auto kit = s.keyIdx.find(kk);
            if (kit == s.keyIdx.end()) {
                s.keyIdx[kk] = s.keyBest.size();
                s.keyBest.push_back({ e.tonic, e.major, e.score, e.ckey });
            } else {
                KeyBest& kb = s.keyBest[kit->second];
                // §5: the per-key representative class is best-scoring, exact ties by the §5 prefix order.
                if (betterPrefix(e.score, stateEnc(e.tonic, e.major, e.ckey),
                                 kb.score, stateEnc(kb.tonic, kb.major, kb.arg), i)) {
                    kb.score = e.score;
                    kb.arg = e.ckey;
                }
            }
        }
        return s;
    };

    for (int j = 1; j <= N; ++j) {
        Boundary& bh = V[j];
        for (int i = std::max(0, j - segCap); i < j; ++i) {
            if (!V[i].hasStart && V[i].states.empty()) {
                continue;
            }
            const Summary& sm = summarize(i);
            const std::vector<std::tuple<int, bool, std::string> >& cand = candidates(i, j);

            // (c) precompute the best key-CHANGE into each distinct target key
            struct Kchg { double best; bool hasArg; std::string backEnc; };
            std::unordered_map<std::string, Kchg> kchg;
            for (const auto& c : cand) {
                const int tt = std::get<0>(c);
                const bool tm = std::get<1>(c);
                const std::string tkey = keyEnc(tt, tm);
                if (kchg.find(tkey) != kchg.end()) {
                    continue;
                }
                Kchg kc{ NEG_INF, false, "" };
                for (const KeyBest& kb : sm.keyBest) {
                    if (kb.tonic == tt && kb.major == tm) {
                        continue;
                    }
                    const double val = kb.score + wKey * adapter.keyTransLogp(kb.tonic, kb.major, tt, tm);
                    const std::string candEnc = stateEnc(kb.tonic, kb.major, kb.arg);
                    // §5: on an exact val tie the change-source is the §5-preferred predecessor prefix.
                    if (!kc.hasArg || betterPrefix(val, candEnc, kc.best, kc.backEnc, i)) {
                        kc.best = val;
                        kc.hasArg = true;
                        kc.backEnc = candEnc;
                    }
                }
                kchg.emplace(tkey, kc);
            }

            for (const auto& c : cand) {
                const int tonic = std::get<0>(c);
                const bool major = std::get<1>(c);
                const std::string& ckey = std::get<2>(c);
                const double cscore = content(i, j, tonic, major, ckey);
                if (cscore == NEG_INF) {
                    if (g_fcOn) { ++g_fc.trContentNegInf; }
                    continue;
                }
                const LabelClass* cls = vocab.find(ckey);
                const double cad = cadenceAt(i, tonic, major);
                const double entryLp = wEntry * adapter.entryLogp(*cls, major);
                double bestIn = NEG_INF;
                int backI = -1;
                std::string backEnc;
                bool haveBack = false;
                int backKind = 0;   // OI-199 fire-count: which transition produced the chosen predecessor
                // (a) initial segment
                if (sm.hasStart) {
                    const auto pr = adapter.priorTerms(tonic, major, sigFifths, declaredMode);
                    const double tin = sm.startScore + wPrior * pr.first + wDmode * pr.second + entryLp;
                    if (!haveBack || better(tin, i, kStartEnc, tonic, major, ckey,
                                            bestIn, backI, backEnc, tonic, major, ckey)) {
                        bestIn = tin; backI = i; backEnc = kStartEnc; haveBack = true; backKind = 1;
                    }
                }
                // (b) same-key chord transition (+ stay key-cell)
                const std::string kk = keyEnc(tonic, major);
                const auto pcIt = sm.perClass.find(kk);
                if (pcIt != sm.perClass.end()) {
                    const double stay = wKey * adapter.keyTransLogp(tonic, major, tonic, major);
                    for (const auto& pck : pcIt->second) {
                        const double tin = pck.second
                            + wChord * adapter.chordTransLogp(*vocab.find(pck.first), *cls, major) + stay;
                        const std::string candEnc = stateEnc(tonic, major, pck.first);
                        if (!haveBack || better(tin, i, candEnc, tonic, major, ckey,
                                                bestIn, backI, backEnc, tonic, major, ckey)) {
                            bestIn = tin; backI = i; backEnc = candEnc; haveBack = true; backKind = 2;
                        }
                    }
                }
                // (c) key-change transition + entry
                const auto kcIt = kchg.find(kk);
                if (kcIt != kchg.end() && kcIt->second.hasArg) {
                    const double tin = kcIt->second.best + entryLp;
                    if (!haveBack || better(tin, i, kcIt->second.backEnc, tonic, major, ckey,
                                            bestIn, backI, backEnc, tonic, major, ckey)) {
                        bestIn = tin; backI = i; backEnc = kcIt->second.backEnc; haveBack = true; backKind = 3;
                    }
                }
                if (!haveBack) {
                    if (g_fcOn) { ++g_fc.trNoBack; }
                    continue;
                }
                if (g_fcOn) {
                    if (backKind == 1) { ++g_fc.trInitial; }
                    else if (backKind == 2) { ++g_fc.trSameKey; }
                    else if (backKind == 3) { ++g_fc.trKeyChange; }
                }
                const double score = bestIn + cscore + cad;
                const std::string st = stateEnc(tonic, major, ckey);
                const auto exist = bh.idx.find(st);
                if (exist == bh.idx.end()) {
                    if (g_fcOn) { ++g_fc.stInsert; }
                    bh.idx[st] = bh.states.size();
                    bh.states.push_back({ tonic, major, ckey, score, backI, backEnc });
                } else {
                    StateEntry& se = bh.states[exist->second];
                    if (better(score, backI, backEnc, tonic, major, ckey,
                               se.score, se.backI, se.backEnc, tonic, major, ckey)) {
                        if (g_fcOn) { ++g_fc.stImprove; }
                        se.score = score;
                        se.backI = backI;
                        se.backEnc = backEnc;
                    }
                }
            }
        }
    }

    if (V[N].states.empty()) {
        result.complete = false;
        result.totalScore = NEG_INF;
        if (g_fcOn) { ++g_fc.dpPieces; ++g_fc.dpEmpty; }   // the OI-215 empty-analysis outcome branch
        return result;
    }
    // terminal: the §5-best full-coverage state (exact-score ties by the total order on paths).
    size_t bestIdx = 0;
    for (size_t s = 1; s < V[N].states.size(); ++s) {
        const StateEntry& a = V[N].states[s];
        const StateEntry& b = V[N].states[bestIdx];
        if (better(a.score, a.backI, a.backEnc, a.tonic, a.major, a.ckey,
                   b.score, b.backI, b.backEnc, b.tonic, b.major, b.ckey)) {
            bestIdx = s;
        }
    }
    result.totalScore = V[N].states[bestIdx].score;
    result.complete = true;

    // backtrack
    std::vector<SegmentSummary> segs;
    std::string curEnc = stateEnc(V[N].states[bestIdx].tonic, V[N].states[bestIdx].major,
                                  V[N].states[bestIdx].ckey);
    int jj = N;
    while (jj > 0 && curEnc != kStartEnc) {
        const auto it = V[jj].idx.find(curEnc);
        if (it == V[jj].idx.end()) {
            break;
        }
        const StateEntry& se = V[jj].states[it->second];
        SegmentSummary s;
        s.i = se.backI;
        s.j = jj;
        s.tonicPc = se.tonic;
        s.isMajor = se.major;
        s.classKey = se.ckey;
        s.startTick = piece.events[se.backI].start;
        s.endTick = piece.events[jj - 1].end;
        const LabelClass* cls = vocab.find(se.ckey);
        const ChordInfo& info = cache.get(*cls, se.tonic, se.major);
        s.rootPc = info.root;
        s.key = keyString(se.tonic, se.major);
        s.degree = cls->degreeBase();
        s.quality = cls->quality();
        s.inversion = cls->inversion();
        s.target = cls->target();
        segs.push_back(std::move(s));
        curEnc = se.backEnc;
        jj = se.backI;
    }
    std::reverse(segs.begin(), segs.end());
    result.segments = std::move(segs);
    if (g_fcOn) { ++g_fc.dpPieces; ++g_fc.dpComplete; g_fc.dpSegments += static_cast<long long>(result.segments.size()); }
    return result;
}

// ── OI-199 Task 1 — per-event structural coverability decomposition (DEFAULT-OFF harness helper) ──
// For each event, examine every <=segCap window containing it, call the REAL candidateStates (no re-
// implementation, #6), and classify uncoverable events by the responsible admission gate — so the
// OI-215 member-overlap failure is separated from any sibling (root-present / NCT-budget). The global
// fire counters accumulate over the same window enumeration (candidateStates bumps g_fc when enabled).
CoverageScan scanCoverage(const Piece& piece, const Vocabulary& vocab, ChordCache& cache,
                          std::optional<int> sigFifths, int segCap)
{
    CoverageScan cs;
    const int N = static_cast<int>(piece.events.size());
    cs.nEvents = N;
    // sigKey exactly as decodePiece derives it (the notated-signature major key is always kept).
    std::optional<std::pair<int, bool> > sigKey;
    if (sigFifths.has_value()) {
        for (int t = 0; t < 12 && !sigKey.has_value(); ++t) {
            if (collectionFifths(t, true) == *sigFifths) {
                sigKey = std::make_pair(t, true);
            }
        }
    }
    std::vector<char> coverable(N, 0), hasRich(N, 0), richDeepest(N, 0);
    for (int j = 1; j <= N; ++j) {
        for (int i = std::max(0, j - segCap); i < j; ++i) {
            AdmitStats stw;
            const auto cand = candidateStates(piece, i, j, vocab, cache, sigKey, &stw);
            const bool admits = !cand.empty();
            const bool rich = stw.nOnset >= 2;
            for (int e = i; e < j; ++e) {
                if (admits) { coverable[e] = 1; }
                if (rich) {
                    hasRich[e] = 1;
                    if (stw.deepestGate > richDeepest[e]) { richDeepest[e] = static_cast<char>(stw.deepestGate); }
                }
            }
        }
    }
    for (int e = 0; e < N; ++e) {
        if (coverable[e]) { continue; }
        ++cs.uncoverable;
        if (!hasRich[e]) {
            ++cs.uncovMemberOverlapPure;          // every covering window had <2 onset pcs (OI-215 theorem)
        } else if (richDeepest[e] >= 3) {
            ++cs.uncovFitBlocked;                 // a rich window passed gates 1&2, failed gate 3 (SIBLING)
        } else if (richDeepest[e] == 2) {
            ++cs.uncovMemberOverlapRich;          // rich window, gate 2 rejected all (broader member-overlap)
        } else {
            ++cs.uncovRootOnly;                   // rich window never got a class past gate 1 (SIBLING)
        }
    }
    cs.complete = (cs.uncoverable == 0);
    return cs;
}

// ── note_events.json loader ───────────────────────────────────────────────────────────────────

LoadedCorpus loadPiecesFromNoteEvents(const std::string& noteEventsPath)
{
    LoadedCorpus lc;
    std::ifstream f(noteEventsPath, std::ios::binary);
    if (!f) {
        lc.error = "cannot open " + noteEventsPath;
        return lc;
    }
    const std::string s((std::istreambuf_iterator<char>(f)), std::istreambuf_iterator<char>());
    std::string jerr;
    const muse::ByteArray ba(s.data(), s.size());
    const muse::JsonObject root = muse::JsonDocument::fromJson(ba, &jerr).rootObject();
    if (!jerr.empty()) {
        lc.error = "JSON parse error in " + noteEventsPath + ": " + jerr;
        return lc;
    }
    const muse::JsonObject prov = root.value("provenance").toObject();
    lc.ticksPerQuarter = prov.value("ticks_per_quarter").toInt();

    const muse::JsonObject pieces = root.value("pieces").toObject();
    for (const std::string& stem : pieces.keys()) {
        const muse::JsonObject p = pieces.value(stem).toObject();
        Piece piece;
        piece.stem = stem;
        piece.nQuarter = p.value("n_quarter").toInt();
        const muse::JsonArray evs = p.value("events").toArray();
        for (size_t e = 0; e < evs.size(); ++e) {
            const muse::JsonArray a = evs.at(e).toArray();
            EventRec ev;
            ev.start = a.at(0).toInt();
            ev.end = a.at(1).toInt();
            ev.measure = a.at(2).toInt();
            ev.beat = a.at(3).toDouble();
            ev.mc = a.at(4).toInt();
            ev.ferm = a.size() > 5 ? a.at(5).toInt() : 0;
            piece.events.push_back(ev);
        }
        const muse::JsonArray ns = p.value("notes").toArray();
        for (size_t k = 0; k < ns.size(); ++k) {
            const muse::JsonArray a = ns.at(k).toArray();
            NoteRec n;
            n.onset = a.at(0).toInt();
            n.dur = a.at(1).toInt();
            n.pc = a.at(2).toInt();
            n.midi = a.at(3).toInt();
            n.lof = a.at(4).toInt();
            n.part = a.at(5).toInt();
            n.measure = a.at(6).toInt();
            n.beat = a.at(7).toDouble();
            n.mc = a.at(8).toInt();
            n.ap = a.at(9).toInt();
            n.dp = a.at(10).toInt();
            n.tied = a.at(11).toInt();
            n.ferm = a.size() > 12 ? a.at(12).toInt() : 0;
            piece.notes.push_back(n);
        }
        piece.prepare();
        lc.pieces.emplace(stem, std::move(piece));
    }
    lc.ok = true;
    return lc;
}
} // namespace mu::composing::analysis::joint
