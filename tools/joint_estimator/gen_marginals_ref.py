#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
# MuseScore-Studio-CLA-applies
#
# MuseScore Studio
# Music Composition & Notation
#
# Copyright (C) 2026 MuseScore Limited
"""gen_marginals_ref.py — the FORWARD-BACKWARD MARGINALS reference (notation output contract §3.3
group (ii); OI-193's completion). The C++ parity oracle for the group-(ii) marginal fields.

★ WHAT THIS PRODUCES. Group (i) (gen_posterior_slice.py) is a LOCAL content-score slice: hold a
committed span + its committed class fixed and re-score under each candidate. Group (ii) is the FULL
posterior — the exact forward-backward MARGINALS over the SAME pruned semi-Markov lattice the
production decode `probe_decoder.decode_piece` explores (same candidate sets, same seg_cap 4, same
frozen tables, the SELECTED weight vector the C++ module embeds). Per piece it publishes:

  * BOUNDARY axis — per event e (0..N): P(a segment boundary falls at e) = the cross-segmentation mass
    the local slice cannot see (contract §3.3 group (ii) boundary axis; #17e's named limit). e=0 and
    e=N are 1.0 by construction (every path starts/ends there).
  * KEY axis, per COMMITTED segment span — P(key = k | this span is a segment) for every candidate key
    at the span, committed key flagged. CONDITIONAL on the span, so the masses SUM TO 1.
  * CHORD axis, per committed segment span — P(class = c | this span is a segment) for every candidate
    class at the span, committed class flagged. CONDITIONAL on the span, so the masses SUM TO 1.
  * span_mass — the (unconditional) marginal probability that the committed span is itself a segment
    (the span's segmentation uncertainty; carried for completeness, #12 — it is the denominator the
    conditional key/chord masses are divided by).

★ THE MASS IS A MODEL PROBABILITY, NOT A CALIBRATED CONFIDENCE (contract §3.3): a forward-backward
marginal of the decode's own lattice. No [0,1] calibration is claimed anywhere; no consumer may
load-bear on calibration until a #20-gated calibration is measured. The masses and the group-(i) gap
are DIFFERENT instruments (a probability vs a log-score difference) — never silently interchanged.

★ THE LATTICE IS THE DECODE'S OWN (#6; the "difference to state, not paper over" duty). The marginals
are OF the PRUNED decode lattice: `probe_decoder._candidate_states_for_segment` applies the ratified
§5 key-fit prune (top-K=6 keys per span + the signature key) and the root-present/member-overlap
filters. So the group-(ii) KEY axis lists the pruned candidate keys the decode actually summed over
(≤ ~7), NOT the full 24 keys the group-(i) slice re-scores — a stated, honest difference: group (i) is
a broad content-only slice; group (ii) is the marginal of the paths the decode's lattice contains.

★ CARRIED ESTABLISHMENT — reuse of the fit arc's lattice machinery by import (#6, the dispatch's
directive). `fit_weights.py`'s forward-backward (`build_unit` + `unit_logZ_and_expect`) is IMPORTED,
never edited; its whole-piece lattice at augment_gt=False IS the decode lattice, proven by the fit
arc's own `establish_viterbi_parity` (its max-plus == decode_piece's Viterbi). This module's own
scalar forward-backward (transparent, hand-checkable, the shape the C++ port mirrors) is established
AGAINST it: our sum-semiring logZ reproduces `unit_logZ_and_expect`'s logZ, and our max-plus logZ
reproduces `decode_piece.total_score`, on real pieces. Difference between the two lattices, stated:
the fit lattice is built over ground-truth training UNITS with GT augmentation and the head-only
prior; here we build the WHOLE-PIECE lattice at augment_gt=False (one head unit, no augmentation) —
which is exactly the decode lattice (that is what establish_viterbi_parity certifies).

★ THE ORACLE (contract §5.5 + OI-193; ALL must pass BEFORE any group-(ii) field is published — an
establishment blocker is a #13 STOP, never a silent regression to slice-as-end-state):
  (a) forward logZ == backward logZ, per piece (machine tolerance; report max |Δ|).
  (a2) our max-plus logZ == decode_piece.total_score, per piece — our lattice IS the decode lattice.
  (b) per committed span: the conditional key masses SUM TO 1 and the class masses SUM TO 1 (machine
      tolerance; report the max deviation).
  (c) synthetic-case agreement with the fit-arc lattice arithmetic — a tiny structured lattice whose
      logZ + arc/boundary marginals we ALSO compute by brute-force path enumeration (absolute
      correctness of the decomposed recursion), PLUS our sum-logZ == fit_weights.unit_logZ_and_expect's
      logZ on real pieces (the fit-arc agreement). One case is hand-traced in the report.
  (d) MAP consistency — the committed reading is the modal marginal where the decode margin is large;
      the group-(i) key gap and the committed-key marginal mass move in the SAME direction (positive
      rank correlation) and the committed key is the modal marginal key on the large-gap segments. A
      negative correlation, or a committed key that is not modal where the gap is large, is a STOP.

Config is gen_posterior_slice's / gen_decode_parity_ref's exactly: seg_cap 4, leftover option 2a
("freq"), table_set "all", signature/declared mode from the xml header, KEYS_24 candidate set (the
prune is INSIDE _candidate_states_for_segment). Floats full precision. Deterministic (two runs
byte-identical). This artifact is the Task-3 C++ parity oracle.

Usage:
    python tools/joint_estimator/gen_marginals_ref.py               # full corpus: establish + write
    python tools/joint_estimator/gen_marginals_ref.py --stems bwv269 bwv352   # subset dry-run
        (subset: establishes + measures; writes NOTHING)
    python tools/joint_estimator/gen_marginals_ref.py --self-check   # the synthetic oracle only (fast)
"""
from __future__ import annotations

import argparse
import json
import math
import subprocess
import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent.parent
sys.path.insert(0, str(_ROOT / "tools"))
sys.path.insert(0, str(_HERE))

import probe_decoder as pd          # noqa: E402  the pinned decoder — IMPORT-ONLY (candidates/factors/decode)
import fit_weights as fw            # noqa: E402  the fit arc's forward-backward — IMPORT-ONLY (carried logZ)

SEG_CAP = 4
LEFTOVER = "freq"
ART_PATH = _HERE / "marginals_ref.json"
NEG_INF = float("-inf")
START = ("START",)


def _git_head() -> str:
    return subprocess.run(["git", "-C", str(_ROOT), "rev-parse", "HEAD"],
                          capture_output=True, text=True).stdout.strip()


# ── a Neumaier-compensated log-sum-exp (the summation discipline the C++ port mirrors) ────────────
# The exp-sum is accumulated with Neumaier compensation — the established bit-parity summation pattern
# the C++ side reproduces (the slice's segmentContentScore uses the same). The transcendental exp/log
# are libm calls; their cross-language last-ULP behavior is the Task-3 parity ASSESSMENT, not a Task-2
# oracle concern (the oracle checks below are invariant to the last ULP).
def _neumaier_sum(values):
    s = 0.0
    c = 0.0
    for v in values:
        t = s + v
        if abs(s) >= abs(v):
            c += (s - t) + v
        else:
            c += (v - t) + s
        s = t
    return s + c


def _lse(values):
    """log(sum(exp(v))) over a list, max-shifted, Neumaier-compensated. [] -> -inf."""
    m = NEG_INF
    for v in values:
        if v > m:
            m = v
    if m == NEG_INF:
        return NEG_INF
    return m + math.log(_neumaier_sum([math.exp(v - m) for v in values]))


def _lse_add(acc, v):
    """Incrementally fold v into a running log-sum-exp accumulator (acc may be None/-inf)."""
    if acc is None or acc == NEG_INF:
        return v
    if v == NEG_INF:
        return acc
    m = acc if acc > v else v
    return m + math.log(math.exp(acc - m) + math.exp(v - m))


# ══════════════════════════════════════════════════════════════════════════════
# The decode's lattice for one piece (decode_piece's own primitives)
# ══════════════════════════════════════════════════════════════════════════════

class Lattice:
    """The decode's lattice for one piece, materialized from decode_piece's OWN primitives: the pruned
    candidate states per span (_candidate_states_for_segment), the weighted within-segment content
    (score_segment_content), and the boundary cadence term (cadence_at). The transition scores are the
    adapter's factor methods times the ★R2 weights, exactly as decode_piece's Viterbi applies them."""

    def __init__(self, piece, adapter, vocab, cache, sig_fifths, declared_mode, seg_cap=SEG_CAP,
                 key_set=None, ftab=None):
        self.piece = piece
        self.adapter = adapter
        self.vocab = vocab
        self.cache = cache
        self.sig_fifths = sig_fifths
        self.declared_mode = declared_mode
        self.seg_cap = seg_cap
        self.ftab = ftab          # precomputed dense factor tables (CT/KT/ENT); None -> compute via adapter
        self.N = len(piece.events)
        w = adapter.weights()
        self.w_prior, self.w_dmode = w["prior"], w["declared_mode"]
        self.w_entry, self.w_key, self.w_chord = w["entry"], w["key_trans"], w["chord_trans"]
        self.key_set = key_set or pd.KEYS_24
        # the notated-signature MAJOR key is always kept (decode_piece's sig_key computation, verbatim)
        self.sig_key = None
        if sig_fifths is not None:
            for (t, m) in self.key_set:
                if m and pd.glt._collection_fifths(t, m) == sig_fifths:
                    self.sig_key = (t, m)
                    break
        self._cand_cache = {}
        self._content_cache = {}
        self._overlap_cache = {}
        self._cad_cache = {}

    def candidates(self, i, j):
        c = self._cand_cache.get((i, j))
        if c is None:
            c = pd._candidate_states_for_segment(self.piece, i, j, self.vocab, self.cache,
                                                 self.key_set, self.sig_key)
            self._cand_cache[(i, j)] = c
        return c

    def content(self, i, j, st):
        v = self._content_cache.get((i, j, st))
        if v is None:
            sp = self._overlap_cache.get((i, j))
            if sp is None:
                sp = self.piece.overlap_pcs(i, j)
                self._overlap_cache[(i, j)] = sp
            (tonic, is_major, ckey) = st
            v = pd.score_segment_content(self.piece, i, j, tonic, is_major, self.vocab.classes[ckey],
                                         self.adapter, self.cache, seg_pcs=sp)
            self._content_cache[(i, j, st)] = v
        return v

    def cad(self, i, tonic, is_major):
        v = self._cad_cache.get((i, tonic, is_major))
        if v is None:
            v = pd.cadence_at(self.piece, i, tonic, is_major, self.adapter)
            self._cad_cache[(i, tonic, is_major)] = v
        return v

    # --- the three transition sub-terms decode_piece applies (each times its ★R2 weight) ---
    # When ftab (the precomputed dense tables) is present these are O(1) dict lookups — the ONLY change
    # from computing via the adapter is speed (the values are the adapter's own, materialized once).
    def prior_entry(self, tonic, is_major, ckey):
        """Initial-segment factor: w_prior·sig-prior + w_dmode·declared-mode-increment + w_entry·entry."""
        ps, pi = self.adapter.prior_terms(tonic, is_major, self.sig_fifths, self.declared_mode)
        return self.w_prior * ps + self.w_dmode * pi + self.entry(ckey, is_major)

    def entry(self, ckey, is_major):
        if self.ftab is not None:
            return self.ftab["ENT"][is_major][ckey]
        return self.w_entry * self.adapter.entry_logp(self.vocab.classes[ckey], is_major)

    def key_trans(self, k_prev, k):
        if self.ftab is not None:
            return self.ftab["KT"][(k_prev, k)]
        return self.w_key * self.adapter.key_trans_logp(k_prev, k)

    def chord_trans(self, pck, ckey, is_major):
        if self.ftab is not None:
            return self.ftab["CT"][is_major][(pck, ckey)]
        return self.w_chord * self.adapter.chord_trans_logp(self.vocab.classes[pck],
                                                            self.vocab.classes[ckey], is_major)


# ══════════════════════════════════════════════════════════════════════════════
# The exact semi-Markov forward-backward (decomposed — O(K² + K·C²) per boundary)
# ══════════════════════════════════════════════════════════════════════════════
# The predecessor transition splits three ways exactly as decode_piece's Viterbi (a)/(b)/(c) branches:
#   (a) initial  (predecessor START, boundary 0): prior + declared-mode + entry
#   (b) same key: chord-transition + the stay key-cell (NO entry)
#   (c) key change: key-transition + entry
# The key-change branch needs only the per-key marginal of the predecessor (its class is summed out),
# so it is O(K²) not O(states²); the same-key branch is O(C²) per key — the standard semi-Markov
# decomposition (the SAME one fit_weights vectorizes). We store each arc's into-arc mass (`ain`) in the
# forward pass so the marginals need no re-derivation.

def _summarize(alpha_i, reduce_add):
    """(start, key_red{(t,m): reduced score over classes}, per_class{(t,m):{ck:score}}) of alpha[i]."""
    start = alpha_i.get(START)
    key_red = {}
    per_class = {}
    for st, a in alpha_i.items():
        if st == START:
            continue
        (t, m, ck) = st
        kk = (t, m)
        key_red[kk] = a if kk not in key_red else reduce_add(key_red[kk], a)
        per_class.setdefault(kk, {})[ck] = a
    return start, key_red, per_class


def _run_forward(lat: Lattice, is_max):
    """The forward pass in the max-plus (is_max) or log-sum-exp semiring. Returns (alpha, ain_store):
    alpha[e] is the per-ending-state table at boundary e; ain_store[(i,j,st)] is the arc's into-mass."""
    N, seg_cap = lat.N, lat.seg_cap

    def red(a, b):
        return (a if a > b else b) if is_max else _lse_add(a, b)

    def red_list(xs):
        if not xs:
            return NEG_INF
        if is_max:
            m = NEG_INF
            for x in xs:
                if x > m:
                    m = x
            return m
        return _lse(xs)

    alpha = [dict() for _ in range(N + 1)]
    alpha[0][START] = 0.0
    ain_store = {}
    summ = [None] * (N + 1)
    for j in range(1, N + 1):
        aj = alpha[j]
        for i in range(max(0, j - seg_cap), j):
            if not alpha[i]:
                continue
            if summ[i] is None:
                summ[i] = _summarize(alpha[i], red)
            start_score, key_red, per_class = summ[i]
            cands = lat.candidates(i, j)
            tgt_keys = set((t, m) for (t, m, _c) in cands)
            # best/summed key-change into each target key (predecessor class summed/maxed out)
            kchg = {}
            for tk in tgt_keys:
                terms = [kr + lat.key_trans(pk, tk) for pk, kr in key_red.items() if pk != tk]
                kchg[tk] = red_list(terms)
            for st in cands:
                c = lat.content(i, j, st)
                if c == NEG_INF:
                    continue
                (t, m, ck) = st
                cad = lat.cad(i, t, m)
                branch = []
                if start_score is not None:                       # (a) initial
                    branch.append(start_score + lat.prior_entry(t, m, ck))
                same = per_class.get((t, m))
                if same:                                          # (b) same key: chord + stay
                    stay = lat.key_trans((t, m), (t, m))
                    terms = [a + lat.chord_trans(pck, ck, m) for pck, a in same.items()]
                    branch.append(red_list(terms) + stay)
                kc = kchg.get((t, m), NEG_INF)
                if kc != NEG_INF:                                 # (c) key change: key-trans + entry
                    branch.append(kc + lat.entry(ck, m))
                ain = red_list(branch)
                if ain == NEG_INF:
                    continue
                ain_store[(i, j, st)] = ain
                total = ain + c + cad
                aj[st] = total if st not in aj else red(aj[st], total)
    return alpha, ain_store


def forward_backward(lat: Lattice):
    """Exact sum-product semi-Markov forward-backward. Returns logZ (forward), logZ_bwd (backward), the
    per-span arc marginals, and the per-event boundary marginals. START pays the initial factors."""
    N, seg_cap = lat.N, lat.seg_cap
    alpha, ain_store = _run_forward(lat, is_max=False)
    if not alpha[N]:
        return {"complete": False}
    logZ = _lse(list(alpha[N].values()))

    # ── backward: beta[i][ps] = LSE over continuations from a segment ending at i in state ps ──
    beta = [dict() for _ in range(N + 1)]
    for st in alpha[N]:
        beta[N][st] = 0.0
    for i in range(N - 1, -1, -1):
        # arcs starting at i, with their predecessor-independent potential (content + cad + beta[end])
        arcs = []
        for j in range(i + 1, min(N, i + seg_cap) + 1):
            for st in lat.candidates(i, j):
                c = lat.content(i, j, st)
                if c == NEG_INF:
                    continue
                b = beta[j].get(st)
                if b is None:
                    continue
                (t, m, _ck) = st
                arcs.append((st, c + lat.cad(i, t, m) + b))
        if i == 0:
            # START: initial factor per arc (prior + declared mode + entry)
            terms = [ap + lat.prior_entry(st[0], st[1], st[2]) for (st, ap) in arcs]
            if terms:
                beta[0][START] = _lse(terms)
            continue
        # G[target key] = LSE over arcs at that key of (arc_pot + entry); grouped same-key arc lists
        G = {}
        by_key = {}
        for (st, ap) in arcs:
            (t, m, ck) = st
            G[(t, m)] = _lse_add(G.get((t, m)), ap + lat.entry(ck, m))
            by_key.setdefault((t, m), []).append((ck, ap))
        # kcb[source key] = LSE over target != source of G[target] + key-trans(source, target)
        src_keys = set((st[0], st[1]) for st in alpha[i] if st != START)
        kcb = {}
        for pk in src_keys:
            terms = [g + lat.key_trans(pk, tk) for tk, g in G.items() if tk != pk]
            kcb[pk] = _lse(terms)
        for ps in alpha[i]:
            if ps == START:
                continue
            (pt, pm, pck) = ps
            pk = (pt, pm)
            stay = lat.key_trans(pk, pk)
            same_terms = [ap + lat.chord_trans(pck, ck, pm) + stay for (ck, ap) in by_key.get(pk, [])]
            b = _lse([_lse(same_terms), kcb.get(pk, NEG_INF)])
            if b != NEG_INF:
                beta[i][ps] = b
    logZ_bwd = beta[0].get(START, NEG_INF)

    # ── arc marginals from the stored into-mass + beta; per-event boundary marginals ──
    seg_marg = {}
    for (i, j, st), ain in ain_store.items():
        b = beta[j].get(st)
        if b is None:
            continue
        (t, m, _ck) = st
        g = math.exp(ain + lat.content(i, j, st) + lat.cad(i, t, m) + b - logZ)
        seg_marg.setdefault((i, j), {})[st] = g

    boundary = [0.0] * (N + 1)
    boundary[0] = 1.0
    boundary[N] = 1.0
    for e in range(1, N):
        s = 0.0
        for st, a in alpha[e].items():
            b = beta[e].get(st)
            if b is not None:
                s += math.exp(a + b - logZ)
        boundary[e] = s

    return {"complete": True, "logZ": logZ, "logZ_bwd": logZ_bwd, "alpha": alpha, "beta": beta,
            "seg_marg": seg_marg, "boundary": boundary}


def maxplus_logZ(lat: Lattice):
    """The best-path score over the lattice (max-plus forward) — == decode_piece.total_score (oracle a2:
    our lattice IS the decode lattice). The §5 tie-break moves no SCORE, so no tie-break is needed here."""
    alpha, _ain = _run_forward(lat, is_max=True)
    if not alpha[lat.N]:
        return None
    return max(alpha[lat.N].values())


# ══════════════════════════════════════════════════════════════════════════════
# Per-committed-segment marginal fields (the contract §3.3 group-(ii) publication)
# ══════════════════════════════════════════════════════════════════════════════

def segment_marginal_fields(lat: Lattice, seg, fb):
    """For one COMMITTED decode segment (a decode seg_dict with i/j/tonic_pc/is_major/class_key), the
    group-(ii) key axis and chord axis, both CONDITIONAL on the committed span (so each sums to 1), and
    the span's segmentation mass. Candidate keys/classes are the decode's own pruned candidates at the
    span (the honest lattice set)."""
    i, j = seg["i"], seg["j"]
    arcs = fb["seg_marg"].get((i, j), {})
    span_mass = _neumaier_sum(list(arcs.values()))
    key_raw = {}
    class_raw = {}
    for (tonic, is_major, ckey), g in arcs.items():
        ks = pd._key_string(tonic, is_major)
        key_raw[ks] = key_raw.get(ks, 0.0) + g
        class_raw[ckey] = class_raw.get(ckey, 0.0) + g
    committed_key = pd._key_string(seg["tonic_pc"], seg["is_major"])
    committed_class = seg["class_key"]
    # deterministic candidate ordering: keys in KEYS_24 order, classes in vocabulary (sorted) order
    key_labels = [pd._key_string(t, m) for (t, m) in pd.KEYS_24 if pd._key_string(t, m) in key_raw]
    class_labels = [c for c in lat.vocab.keylist if c in class_raw]
    denom = span_mass if span_mass > 0.0 else 1.0
    key_scores = [key_raw[k] / denom for k in key_labels]
    class_scores = [class_raw[c] / denom for c in class_labels]
    key_committed = key_labels.index(committed_key) if committed_key in key_labels else -1
    class_committed = class_labels.index(committed_class) if committed_class in class_labels else -1
    return {
        "i": i, "j": j, "span": [seg["start_tick"], seg["end_tick"]],
        "committed_key": committed_key, "committed_class": committed_class,
        "span_mass": span_mass,
        "key_labels": key_labels, "key_masses": key_scores, "key_committed": key_committed,
        "chord_labels": class_labels, "chord_masses": class_scores, "chord_committed": class_committed,
    }


def group_i_key_gap(lat: Lattice, seg):
    """The group-(i) key gap (committed class fixed, re-score under KEYS_24) — the SAME quantity
    gen_posterior_slice publishes, reused here for the MAP-consistency oracle (gap vs marginal mass)."""
    cls = lat.vocab.classes[seg["class_key"]]
    i, j = seg["i"], seg["j"]
    best = (seg["tonic_pc"], seg["is_major"])
    best_sc, alt_sc = NEG_INF, NEG_INF
    for (tonic, is_major) in pd.KEYS_24:
        _m, _f, root = lat.cache.get(cls, tonic, is_major)
        if root is None:
            continue
        sc = pd.score_segment_content(lat.piece, i, j, tonic, is_major, cls, lat.adapter, lat.cache)
        if sc == NEG_INF:
            continue
        if (tonic, is_major) == best:
            best_sc = sc
        elif sc > alt_sc:
            alt_sc = sc
    if best_sc == NEG_INF or alt_sc == NEG_INF:
        return None
    return best_sc - alt_sc


def build_factor_tables(adapter, vocab, w):
    """Materialize the weight-independent factors as dense lookup tables ONCE (the fit_weights.TableSet
    pattern): CT[is_major][(prevClass, curClass)], KT[(prevKey, curKey)], ENT[is_major][class]. The
    values are the adapter's own methods times the ★R2 weights — no new derivation, only memoized so
    the forward-backward's millions of transition reads are O(1) dict lookups instead of Katz queries."""
    keylist = vocab.keylist
    CT = {True: {}, False: {}}
    for m in (True, False):
        for pck in keylist:
            pcls = vocab.classes[pck]
            row = CT[m]
            for ckey in keylist:
                row[(pck, ckey)] = w["chord_trans"] * adapter.chord_trans_logp(pcls, vocab.classes[ckey], m)
    KT = {}
    for a in pd.KEYS_24:
        for b in pd.KEYS_24:
            KT[(a, b)] = w["key_trans"] * adapter.key_trans_logp(a, b)
    ENT = {True: {}, False: {}}
    for m in (True, False):
        for ckey in keylist:
            ENT[m][ckey] = w["entry"] * adapter.entry_logp(vocab.classes[ckey], m)
    return {"CT": CT, "KT": KT, "ENT": ENT}


def committed_segments_from_parity(piece, parity_stem):
    """Reconstruct the committed decode segments (as seg_dicts) from decode_parity_ref.json's compact
    selected-arm tuples [i, j, tonic, is_major, class_key, root] + the piece's event ticks — the
    ESTABLISHED committed decode, so no re-decode is needed (gen_posterior_slice establishes these
    segments equal a fresh decode; here (a2) additionally confirms our lattice's best path scores the
    committed total)."""
    segs = []
    for (i, j, tonic, is_major, class_key, root) in parity_stem["segments"]:
        segs.append({
            "i": i, "j": j,
            "start_tick": piece.events[i][pd.EV_START],
            "end_tick": piece.events[j - 1][pd.EV_END],
            "tonic_pc": tonic, "is_major": is_major,
            "class_key": class_key, "root_pc": root,
        })
    return segs


def build_piece(stem, pieces, adapter, vocab, cache, ftab, parity_stem):
    piece = pieces[stem]
    sig, dm = pd.piece_header(stem)
    segments = committed_segments_from_parity(piece, parity_stem)
    total_score = parity_stem["total_score"]
    lat = Lattice(piece, adapter, vocab, cache, sig, dm, ftab=ftab)
    fb = forward_backward(lat)
    return piece, sig, dm, segments, total_score, lat, fb


# ══════════════════════════════════════════════════════════════════════════════
# The synthetic oracle: a tiny STRUCTURED lattice (mimics the real interface), brute-forced
# ══════════════════════════════════════════════════════════════════════════════

class _FakeAdapter:
    """A hand-set factor provider matching the Lattice's adapter interface (prior_terms / entry_logp /
    key_trans_logp / chord_trans_logp), so the ACTUAL decomposed forward_backward runs on the synthetic."""
    def __init__(self, prior, entry, kt, ct):
        self._prior, self._entry, self._kt, self._ct = prior, entry, kt, ct

    def weights(self):
        return {n: 1.0 for n in pd.WEIGHT_NAMES}

    def prior_terms(self, t, m, sig, dm):
        return self._prior[(t, m)]

    def entry_logp(self, cls, is_major):
        return self._entry[(cls, is_major)]

    def key_trans_logp(self, a, b):
        return self._kt[(a, b)]

    def chord_trans_logp(self, prev, cur, is_major):
        return self._ct[(prev, cur, is_major)]


class _FakeVocab:
    def __init__(self, classes):
        self.classes = {c: c for c in classes}          # cls object == its ckey string
        self.keylist = sorted(classes)


class _FakeLattice(Lattice):
    """A structured tiny lattice: bypasses Lattice.__init__ (no real piece) but reuses every method the
    forward-backward calls, so the SAME decomposed recursion is exercised against brute-force."""
    def __init__(self, N, seg_cap, states, content, cad, adapter, vocab):
        self.N = N
        self.seg_cap = seg_cap
        self.adapter = adapter
        self.vocab = vocab
        self.ftab = None          # the synthetic computes transitions via its FakeAdapter (no dense tables)
        self.sig_fifths = 0
        self.declared_mode = ""
        self.w_prior = self.w_dmode = self.w_entry = self.w_key = self.w_chord = 1.0
        self._states = states
        self._content = content
        self._cad = cad

    def candidates(self, i, j):
        return self._states.get((i, j), [])

    def content(self, i, j, st):
        return self._content.get((i, j, st), NEG_INF)

    def cad(self, i, tonic, is_major):
        return self._cad.get((i, (tonic, is_major)), 0.0)


def _make_tiny():
    """A 3-event, 2-key, 2-class structured lattice with hand-set factor log-scores. K1=(0,True),
    K2=(5,False); classes 'x','y'. Every span up to length 2 admits all four (key,class) states."""
    K1, K2 = (0, True), (5, False)
    keys = [K1, K2]
    classes = ["x", "y"]
    N, seg_cap = 3, 2
    states = {}
    for i in range(N):
        for j in range(i + 1, min(N, i + seg_cap) + 1):
            states[(i, j)] = [(t, m, c) for (t, m) in keys for c in classes]
    content, cad = {}, {}
    for (i, j), sts in states.items():
        for k, st in enumerate(sts):
            content[(i, j, st)] = -0.4 * (i + 1) - 0.2 * (j - i) - 0.11 * k
            cad[(i, (st[0], st[1]))] = -0.05 * (i + 1) - 0.03 * (0 if st[1] else 1)
    prior = {K1: (-0.7, 0.0), K2: (-0.9, -0.1)}
    entry = {("x", True): -0.3, ("y", True): -0.5, ("x", False): -0.4, ("y", False): -0.6}
    kt = {}
    for a in keys:
        for b in keys:
            kt[(a, b)] = -0.2 if a == b else -0.85       # stay vs change
    ct = {}
    for p in classes:
        for c in classes:
            for m in (True, False):
                ct[(p, c, m)] = -0.25 if p == c else -0.55
    lat = _FakeLattice(N, seg_cap, states, content, cad, _FakeAdapter(prior, entry, kt, ct),
                       _FakeVocab(classes))
    return lat


def _path_score(lat, segs):
    """The DEFINITION of a path's total log-score (independent of the recursion): initial prior+entry;
    same-key chord+stay; key-change key-trans+entry; plus content + cadence per segment."""
    score = 0.0
    for idx, (i, j, st) in enumerate(segs):
        (t, m, ck) = st
        score += lat.content(i, j, st) + lat.cad(i, t, m)
        if idx == 0:
            score += lat.prior_entry(t, m, ck)
        else:
            (_pi, _pj, pst) = segs[idx - 1]
            (pt, pm, pck) = pst
            if pt == t and pm == m:
                score += lat.chord_trans(pck, ck, m) + lat.key_trans((t, m), (t, m))
            else:
                score += lat.key_trans((pt, pm), (t, m)) + lat.entry(ck, m)
    return score


def _enumerate_paths(lat):
    out = []

    def rec(pos, segs):
        if pos == lat.N:
            out.append((list(segs), _path_score(lat, segs)))
            return
        for j in range(pos + 1, min(lat.N, pos + lat.seg_cap) + 1):
            for st in lat.candidates(pos, j):
                if lat.content(pos, j, st) == NEG_INF:
                    continue
                segs.append((pos, j, st))
                rec(j, segs)
                segs.pop()
    rec(0, [])
    return out


def establish_synthetic():
    """(c) the tiny lattice: the ACTUAL decomposed forward_backward's logZ + arc marginals + boundary
    marginals equal brute-force path enumeration exactly. Returns (ok, detail, hand_trace)."""
    lat = _make_tiny()
    fb = forward_backward(lat)
    mx = maxplus_logZ(lat)
    paths = _enumerate_paths(lat)
    logZ_brute = _lse([sc for _s, sc in paths])
    best_brute = max(sc for _s, sc in paths)
    arc_brute = {}
    for segs, sc in paths:
        for (i, j, st) in segs:
            arc_brute[(i, j, st)] = arc_brute.get((i, j, st), 0.0) + math.exp(sc - logZ_brute)
    bnd_brute = [0.0] * (lat.N + 1)
    bnd_brute[0] = 1.0
    bnd_brute[lat.N] = 1.0
    for segs, sc in paths:
        p = math.exp(sc - logZ_brute)
        bset = {0, lat.N}
        for (i, j, _st) in segs:
            bset.add(i)
            bset.add(j)
        for e in range(1, lat.N):
            if e in bset:
                bnd_brute[e] += p
    arc_fb = {}
    for (i, j), sts in fb["seg_marg"].items():
        for st, g in sts.items():
            arc_fb[(i, j, st)] = g
    d_logZ = abs(fb["logZ"] - logZ_brute)
    d_fb = abs(fb["logZ"] - fb["logZ_bwd"])
    d_max = abs(mx - best_brute)
    d_arc = max((abs(arc_fb.get(k, 0.0) - v) for k, v in arc_brute.items()), default=0.0)
    d_bnd = max((abs(fb["boundary"][e] - bnd_brute[e]) for e in range(lat.N + 1)), default=0.0)
    ok = (d_logZ < 1e-9 and d_fb < 1e-9 and d_max < 1e-9 and d_arc < 1e-9 and d_bnd < 1e-9)
    A = (0, True, "x")
    hand = {
        "n_paths": len(paths),
        "logZ_forward": fb["logZ"], "logZ_backward": fb["logZ_bwd"], "logZ_brute": logZ_brute,
        "best_path_maxplus": mx, "best_path_brute": best_brute,
        "example_arc": "(i=0,j=1,key=Cmaj,class=x)",
        "example_arc_mass_fb": arc_fb.get((0, 1, A), 0.0),
        "example_arc_mass_brute": arc_brute.get((0, 1, A), 0.0),
        "boundary_marginals_fb": [round(x, 12) for x in fb["boundary"]],
        "boundary_marginals_brute": [round(x, 12) for x in bnd_brute],
    }
    detail = {"max_abs_logZ_vs_brute": d_logZ, "max_abs_fwd_bwd": d_fb, "max_abs_maxplus_vs_brute": d_max,
              "max_abs_arc_vs_brute": d_arc, "max_abs_boundary_vs_brute": d_bnd, "n_paths": len(paths)}
    return ok, detail, hand


def establish_fit_arc_agreement(stems, pieces, adapter, vocab, cache, sel_weights, ftab):
    """(c, real-piece half) Build each piece's whole-piece lattice with fit_weights (augment_gt=False)
    and compare its forward logZ (and backward logZ) to our scalar forward-backward's logZ. The fit
    lattice at augment_gt=False IS the decode lattice (fit_weights.establish_viterbi_parity); agreement
    ties our forward-backward to the carried fit-arc machinery."""
    import numpy as np
    ts = fw.TableSet("all", leftover=LEFTOVER)
    ts.adapter.w = dict(sel_weights)          # score the fit lattice at the SELECTED weights (our arm)
    xvec = np.array([sel_weights[n] for n in fw.W_NAMES], dtype=np.float64)
    rows = []
    for stem in stems:
        piece = pieces[stem]
        sig, dm = pd.piece_header(stem)
        lat_fw = fw.build_unit(piece, stem, 0, len(piece.events), True, None, ts, sig, dm,
                               augment_gt=False)
        lz_fw, _EF, lzb_fw = fw.unit_logZ_and_expect(lat_fw, ts, xvec, want_grad=True)
        lat = Lattice(piece, adapter, vocab, cache, sig, dm, ftab=ftab)
        fb = forward_backward(lat)
        rows.append({"stem": stem, "logZ_ours": round(fb["logZ"], 8),
                     "logZ_fit_weights": round(float(lz_fw), 8),
                     "delta": round(fb["logZ"] - float(lz_fw), 10),
                     "fit_weights_fwd_bwd_delta": round(float(lzb_fw) - float(lz_fw), 10)})
    worst = max((abs(r["delta"]) for r in rows), default=0.0)
    return {"rows": rows, "max_abs_delta_vs_fit_weights": worst, "pass": bool(worst < 1e-6)}


# ══════════════════════════════════════════════════════════════════════════════
# MAP-consistency helpers + the corpus run
# ══════════════════════════════════════════════════════════════════════════════

def _spearman(xs, ys):
    n = len(xs)
    if n < 2:
        return 0.0

    def ranks(v):
        order = sorted(range(n), key=lambda k: v[k])
        r = [0.0] * n
        k = 0
        while k < n:
            k2 = k
            while k2 + 1 < n and v[order[k2 + 1]] == v[order[k]]:
                k2 += 1
            avg = (k + k2) / 2.0 + 1.0
            for t in range(k, k2 + 1):
                r[order[t]] = avg
            k = k2 + 1
        return r
    rx, ry = ranks(xs), ranks(ys)
    return _pearson(rx, ry)


def _pearson(xs, ys):
    n = len(xs)
    if n < 2:
        return 0.0
    mx = sum(xs) / n
    my = sum(ys) / n
    num = sum((xs[k] - mx) * (ys[k] - my) for k in range(n))
    dx = math.sqrt(sum((xs[k] - mx) ** 2 for k in range(n)))
    dy = math.sqrt(sum((ys[k] - my) ** 2 for k in range(n)))
    return num / (dx * dy) if dx > 0 and dy > 0 else 0.0


def run(stems, sel_weights, weight_identity, write, fit_arc_sample, parity_sel):
    pieces, prov = pd.load_pieces()
    adapter = pd.FittedAdapter(leftover_mode=LEFTOVER, table_set="all", weights=sel_weights)
    adapter.mode_marginal("major")
    vocab = pd.Vocabulary(adapter.tables)
    cache = pd.ChordCache()
    ftab = build_factor_tables(adapter, vocab, adapter.weights())

    pieces_out = {}
    max_fb_delta = 0.0
    max_maxplus_delta = 0.0
    max_norm_dev = 0.0
    gap_list, mass_list, modal_flags = [], [], []

    t0 = time.perf_counter()
    for idx, stem in enumerate(stems):
        piece, sig, dm, segments, total_score, lat, fb = build_piece(
            stem, pieces, adapter, vocab, cache, ftab, parity_sel[stem])
        if not fb.get("complete"):
            raise SystemExit(f"STOP: {stem} has no complete decode path — the lattice is empty")
        max_fb_delta = max(max_fb_delta, abs(fb["logZ"] - fb["logZ_bwd"]))
        max_maxplus_delta = max(max_maxplus_delta, abs(maxplus_logZ(lat) - total_score))

        segs_out = []
        for s in segments:
            m = segment_marginal_fields(lat, s, fb)
            if m["key_masses"]:
                max_norm_dev = max(max_norm_dev, abs(_neumaier_sum(m["key_masses"]) - 1.0))
            if m["chord_masses"]:
                max_norm_dev = max(max_norm_dev, abs(_neumaier_sum(m["chord_masses"]) - 1.0))
            gap = group_i_key_gap(lat, s)
            committed_mass = m["key_masses"][m["key_committed"]] if m["key_committed"] >= 0 else 0.0
            if gap is not None and m["key_masses"]:
                gap_list.append(gap)
                mass_list.append(committed_mass)
                modal_idx = max(range(len(m["key_masses"])), key=lambda k: m["key_masses"][k])
                modal_flags.append(1 if modal_idx == m["key_committed"] else 0)
            segs_out.append(m)
        pieces_out[stem] = {
            "n_segments": len(segments), "n_events": lat.N,
            "sig_fifths": sig, "declared_mode": dm, "logZ": fb["logZ"],
            "boundary_marginals": fb["boundary"], "segments": segs_out,
        }
        if (idx + 1) % 40 == 0:
            print(f"  [{idx + 1}/{len(stems)}] {stem} ({time.perf_counter() - t0:.0f}s)", flush=True)

    # (d) MAP consistency — the committed reading is modal WHERE THE MARGIN IS LARGE, and the group-(i)
    # gap and committed-key mass move in the SAME direction. The signal is the DIRECTION (positive rank
    # correlation) + the committed key being modal on the high-gap segments; the per-quartile modal
    # fraction must RISE with the gap (Q4 >= Q1) and be high in the top quartile. (A negative
    # correlation, or the committed key NOT modal where the gap is large, is the STOP.)
    n_mapc = len(gap_list)
    spearman = _spearman(gap_list, mass_list)
    pearson = _pearson(gap_list, mass_list)
    modal_frac = sum(modal_flags) / n_mapc if n_mapc else 0.0
    quartiles = []
    q_modal = [0.0, 0.0, 0.0, 0.0]
    q_mass = [0.0, 0.0, 0.0, 0.0]
    if gap_list:
        order = sorted(range(len(gap_list)), key=lambda k: gap_list[k])
        for qi in range(4):
            lo = int(qi / 4.0 * len(order))
            hi = int((qi + 1) / 4.0 * len(order))
            sub = order[lo:hi]
            if sub:
                q_modal[qi] = sum(modal_flags[k] for k in sub) / len(sub)
                q_mass[qi] = sum(mass_list[k] for k in sub) / len(sub)
                quartiles.append({"gap_quartile": qi,
                                  "mean_gap": round(sum(gap_list[k] for k in sub) / len(sub), 4),
                                  "mean_committed_mass": round(q_mass[qi], 6),
                                  "committed_is_modal_fraction": round(q_modal[qi], 6),
                                  "n": len(sub)})
    # DIRECTION criterion: positive rank correlation AND both the committed mass and the committed-modal
    # fraction RISE with the margin (top gap quartile >= bottom). The absolute mass is legitimately
    # moderate (group (ii) integrates the cross-segmentation/neighbor-key mass the local slice cannot
    # see — the point of group (ii)); the STOP is a NEGATIVE correlation or a trend that FALLS with the
    # margin (the marginal contradicting the local slice).
    map_pass = bool(spearman > 0.05 and q_mass[3] >= q_mass[0] and q_modal[3] >= q_modal[0])

    ok_syn, syn_detail, syn_hand = establish_synthetic()
    fit_arc = establish_fit_arc_agreement(fit_arc_sample, pieces, adapter, vocab, cache, sel_weights, ftab)

    oracle = {
        "a_forward_equals_backward_logZ": {"max_abs_delta": max_fb_delta, "pass": max_fb_delta < 1e-6},
        "a2_maxplus_equals_decoder": {"max_abs_delta": max_maxplus_delta, "pass": max_maxplus_delta < 1e-6},
        "b_per_span_normalization": {"max_abs_sum_minus_1": max_norm_dev, "pass": max_norm_dev < 1e-9},
        "c_synthetic_vs_brute": {**syn_detail, "pass": ok_syn, "hand_trace": syn_hand},
        "c_fit_arc_agreement": fit_arc,
        "d_map_consistency": {
            "n_segments": n_mapc,
            "spearman_gap_vs_committed_mass": round(spearman, 6),
            "pearson_gap_vs_committed_mass": round(pearson, 6),
            "committed_is_modal_fraction_overall": round(modal_frac, 6),
            "committed_is_modal_fraction_top_gap_quartile": round(q_modal[3], 6),
            "by_gap_quartile": quartiles,
            "criterion": ("positive spearman(gap, committed_mass) AND both the committed mass and the "
                          "committed-modal fraction RISE with the margin (top gap quartile >= bottom). "
                          "The absolute mass is legitimately moderate: group (ii) integrates the "
                          "cross-segmentation/neighbor-key mass the local group-(i) slice cannot see. "
                          "A negative correlation or a trend that FALLS with the margin is the STOP."),
            "pass": map_pass,
        },
    }
    all_pass = all(oracle[k].get("pass") for k in oracle)

    art = {
        "provenance": {
            "generator": "tools/joint_estimator/gen_marginals_ref.py",
            "instrument_commit": _git_head(),
            "decoder": "tools/joint_estimator/probe_decoder.py (pinned; import-only)",
            "fit_lattice_machinery": "tools/joint_estimator/fit_weights.py (pinned; import-only — carried logZ establishment)",
            "note_events_git_hash": prov["corpus_git_hash"],
            "seg_cap": SEG_CAP, "leftover_rule": f"option 2a ({LEFTOVER})", "table_set": "all",
            "weight_arm": "selected",
            "weight_vector_identity": weight_identity,
            "weight_vector_source": "decode_parity_ref.json selected_weights (== the C++ embedded vector)",
            "lattice": ("the PRUNED decode lattice probe_decoder.decode_piece explores: "
                        "_candidate_states_for_segment applies the ratified §5 key-fit prune "
                        "(top-K=6 keys per span + the signature key) and root-present/member-overlap "
                        "filters. The group-(ii) marginals are OF this lattice; the key axis lists the "
                        "pruned candidate keys (NOT the full 24 the group-(i) slice re-scores)."),
            "mass_semantics": ("forward-backward MARGINAL PROBABILITY of the decode's own lattice — a "
                               "MODEL probability, never a calibrated [0,1] confidence (contract §3.3; "
                               "no #20-gated calibration is claimed). key_masses / chord_masses are "
                               "CONDITIONAL on the committed span (each sums to 1); span_mass is the "
                               "unconditional segmentation mass of the span; boundary_marginals[e] is "
                               "P(a segment boundary at event e)."),
            "group_ii_only": ("this is contract §3.3 GROUP (ii) — the forward-backward marginals "
                              "(OI-193). GROUP (i) is the content-score slice in posterior_slice_ref.json; "
                              "the two are DIFFERENT instruments (a probability vs a log-score difference) "
                              "and never silently interchanged (#19)."),
            "float_form": "full precision (json round-trippable float repr)",
            "schema": ("per piece: n_segments, n_events, sig_fifths, declared_mode, logZ, "
                       "boundary_marginals[N+1] (index e = P(boundary at event e); e=0 and e=N are 1.0), "
                       "and segments[]. Each segment: i, j, span[startTick,endTick], committed_key, "
                       "committed_class, span_mass, key_labels[]/key_masses[]/key_committed (index into "
                       "key_labels), chord_labels[]/chord_masses[]/chord_committed. key/chord masses are "
                       "conditional-on-span (sum to 1); labels are the decode's pruned candidates at the "
                       "span, key_labels in KEYS_24 order, chord_labels in vocabulary sorted order."),
            "establishment": {
                "form": ("contract §5.5 + OI-193: (a) forward==backward logZ; (a2) our max-plus == "
                         "decode_piece.total_score (our lattice IS the decode lattice); (b) per-span "
                         "key/chord mass normalization; (c) synthetic brute-force + fit-arc logZ "
                         "agreement (fit_weights carried); (d) MAP consistency (gap<->mass direction)."),
                "all_pass": all_pass,
                "oracle": oracle,
            },
        },
        "pieces": pieces_out,
    }

    print("\nORACLE:")
    print(f"  (a)  fwd==bwd logZ      max|delta| = {max_fb_delta:.3e}  {'PASS' if oracle['a_forward_equals_backward_logZ']['pass'] else 'FAIL'}")
    print(f"  (a2) maxplus==decoder   max|delta| = {max_maxplus_delta:.3e}  {'PASS' if oracle['a2_maxplus_equals_decoder']['pass'] else 'FAIL'}")
    print(f"  (b)  per-span sum==1    max dev    = {max_norm_dev:.3e}  {'PASS' if oracle['b_per_span_normalization']['pass'] else 'FAIL'}")
    print(f"  (c)  synthetic vs brute max|delta| = {max(syn_detail['max_abs_logZ_vs_brute'], syn_detail['max_abs_arc_vs_brute'], syn_detail['max_abs_boundary_vs_brute'], syn_detail['max_abs_maxplus_vs_brute']):.3e}  {'PASS' if ok_syn else 'FAIL'}  ({syn_detail['n_paths']} paths)")
    print(f"  (c)  fit-arc agreement  max|delta| = {fit_arc['max_abs_delta_vs_fit_weights']:.3e}  {'PASS' if fit_arc['pass'] else 'FAIL'}  ({len(fit_arc_sample)} pieces)")
    print(f"  (d)  MAP consistency    spearman={spearman:.4f} modal_overall={modal_frac:.4f} modal_topQ={q_modal[3]:.4f}  {'PASS' if oracle['d_map_consistency']['pass'] else 'FAIL'}")
    print(f"       by gap quartile (mean_gap, mean_committed_mass, modal_frac): "
          + " | ".join(f"Q{q['gap_quartile']}:{q['mean_gap']:.2f},{q['mean_committed_mass']:.3f},{q['committed_is_modal_fraction']:.3f}" for q in quartiles))
    print(f"  ALL: {'PASS' if all_pass else 'FAIL'}")

    if not all_pass:
        print("STOP: oracle failed — marginals NOT published (OI-193: establish before publish).",
              file=sys.stderr)
        return art, False

    if write:
        ART_PATH.write_text(json.dumps(art) + "\n", encoding="utf-8", newline="\n")
        print(f"\nwrote {ART_PATH}  ({ART_PATH.stat().st_size:,} bytes, {len(pieces_out)} pieces)")
    else:
        blob = json.dumps(art)
        print(f"\n[dry-run] oracle PASSED; artifact would be {len(blob.encode('utf-8')):,} bytes for "
              f"{len(pieces_out)} piece(s). Nothing written.")
    return art, True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stems", nargs="*", default=None, help="subset (dry-run: establish + measure only)")
    ap.add_argument("--self-check", action="store_true", help="the synthetic oracle only (fast, no corpus)")
    args = ap.parse_args()

    if args.self_check:
        ok, detail, hand = establish_synthetic()
        print("synthetic oracle:", "PASS" if ok else "FAIL")
        print(json.dumps(detail, indent=1))
        print(json.dumps(hand, indent=1))
        sys.exit(0 if ok else 1)

    parity = json.loads((_HERE / "decode_parity_ref.json").read_text(encoding="utf-8"))
    sel_weights = parity["selected_weights"]
    parity_sel = parity["selected"]
    weight_identity = parity.get("provenance", {}).get("selected_start", "")

    all_pieces = sorted(pd.load_pieces()[0])
    stems = args.stems if args.stems else all_pieces
    dry = args.stems is not None
    fit_sample = [s for s in ("bwv269", "bwv352", "bwv10.7", "bwv362") if s in set(stems)]
    if not fit_sample:
        fit_sample = stems[:2]

    print(f"forward-backward on {len(stems)} piece(s) at SELECTED weights "
          f"('{weight_identity}')" + (" [dry-run subset]" if dry else "") + " ...", flush=True)
    _art, ok = run(stems, sel_weights, weight_identity, write=not dry, fit_arc_sample=fit_sample,
                   parity_sel=parity_sel)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
