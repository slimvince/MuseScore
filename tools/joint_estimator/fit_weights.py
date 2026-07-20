#!/usr/bin/env python3
"""fit_weights.py — THE WEIGHT FIT (algorithm-completion step 2 of 2; Cowork dispatch 2026-07-19).

The ratified staged fitting's SECOND stage: the frozen generative tables stay exactly as counted, and
the small vector of COMBINATION WEIGHTS of the ratified log-linear score form
(`cowork_joint_estimator_factorization.md` §2) is fit by convex conditional likelihood under the
pre-fit gates (`cowork_prefit_gates.md`: OI-176 held-out protocol, OI-177 capacity budget).

★ THE FIREWALL, as the dispatch states it for a fit event. The TRAINING OBJECTIVE below (the
conditional log-likelihood of the ground-truth path) is lawfully consulted by the optimizer on TRAINING
folds. The GRADING metric is computed exactly once per held-out fold, downstream, in fit_run.py, and
feeds NOTHING back. THIS MODULE IMPORTS NO GRADING MODULE — no compare_rn, no compare_analyses, no
a8_rebaseline_measure, no dcml_parser region grading. Grep-provable: the import block below is the
whole of it. No value here is adjusted in response to any accuracy figure.

★ WHAT IS FIT — the 13-element weight vector `probe_decoder.WEIGHT_NAMES` (★R2, user ruling C1
2026-07-19, which amended the capacity cap ≤12 → ≤14):
    prior, declared_mode, emission, spelling, bass, boundary, chord_trans, key_trans, entry,
    cad_leading_tone, cad_tritone_pair, cad_dominant_tonic_bass, cad_fermata_location
Nine generative-factor weights over FROZEN table log-probabilities + the four cadence-evidence feature
weights the ratified §3.9 gives their own fitted strengths. Nothing else moves: no table cell, no
threshold, no smoothing constant is touched by this module.

★ THE OBJECTIVE (convex). For each training unit u (below), with F(y) the 13-vector of feature sums
along a path y,
        NLL(w) = Σ_u [ logZ_u(w) − w·F(y*_u) ] / T   +   λ · ‖w − w_identity‖²
where y*_u is the ground-truth path, Z_u the partition function over the SAME lattice the decoder
searches, T the training token count (events) and w_identity the ratified generative baseline
(every generative weight 1, every cadence weight 0). The numerator is LINEAR in w and logZ is convex,
so NLL is convex — which is what makes the optimizer's convergence checkable (the dispatch's point).
The L2 anchor is the generative baseline rather than zero, so λ→∞ recovers the mandated ablation arm
exactly rather than recovering "no model".

★ THE TRAINING UNIT — a maximal contiguous run of GROUND-TRUTH-LABELED events inside a piece. This is
how the dispatch's three exclusions are implemented, without distorting anything:
  - the 7 OI-184-flagged pieces are excluded entirely;
  - anacrusis (measure-0) events carry no WiR label and fall outside every unit;
  - the OI-184 interim measured-misaligned (zero-factor) spans are left out — their events are unlabeled,
    so they simply end one unit and begin the next.
The FIRST unit of a piece pays the signature/declared-mode prior and the entry chord at its first
segment (the true piece start). A unit that RESUMES after an unlabeled gap pays neither: the model has
no information about how the gap was traversed, so its first segment starts free. Declared, counted,
and reported on the artifact.

★ THE LATTICE is the decoder's own: candidates come from `probe_decoder._candidate_states_for_segment`
and content features from `probe_decoder.segment_features` — the SAME calls the Viterbi makes (#6; no
shadow scorer). For a TRAINING unit the lattice is augmented so the ground-truth path is representable
(otherwise its likelihood is zero and the objective is −∞): where the ground-truth KEY was dropped by
the decoder's key-fit prune, that key is added and the ordinary state filters are then applied to it
unchanged (a symmetric widening — the ground-truth chord gets no privilege over its competitors in that
key); where the ground-truth STATE itself was dropped by a state filter it is force-added. Both counts
are reported: they measure how much of the ground truth the decode-time prune cannot reach. The
augmentation is TRAINING-ONLY — `augment_gt` is passed by nothing but this module's training path, and
held-out decoding in fit_run.py goes through `probe_decoder.decode_piece` on the plain lattice.
"""
from __future__ import annotations

import json
import math
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np
from scipy.optimize import minimize

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent.parent
sys.path.insert(0, str(_ROOT / "tools"))
sys.path.insert(0, str(_HERE))

import probe_decoder as pd          # noqa: E402  the decoder: lattice, factors, features (reused)
import gen_note_tables as gnt       # noqa: E402  GT segments + the OI-184 exclusion rules (reused)
import gen_label_tables as glt      # noqa: E402  fold machinery / constants (reused)
# FIREWALL: the four imports above are the whole import surface. No grading module is imported here.

FOLD_ARTIFACT = _HERE / "fold_assignment.json"
NOTE_EVENTS = _HERE / "note_events" / "note_events.json"
SEG_CAP = 4                          # the committed decode configuration (probe_run.SEG_CAP)
LEFTOVER = "freq"                    # the ratified §5 below-threshold rule (option 2a)

W_NAMES = list(pd.WEIGHT_NAMES)
NW = len(W_NAMES)
WI = {n: i for i, n in enumerate(W_NAMES)}
# the four content features, in the order their weights appear in the vector
CONTENT_W = ("emission", "spelling", "bass", "boundary")
CAD_W = tuple("cad_" + f for f in pd.CADENCE_FEATURES)

NEG_INF = -np.inf


def identity_vector():
    w = pd.identity_weights()
    return np.array([w[n] for n in W_NAMES], dtype=np.float64)


def vec_to_weights(x):
    return {n: float(x[i]) for i, n in enumerate(W_NAMES)}


# ══════════════════════════════════════════════════════════════════════════════
# The frozen transition tables, materialized once per table set
# ══════════════════════════════════════════════════════════════════════════════

class TableSet:
    """Every factor that does NOT depend on the notes, materialized as dense log-probability arrays:
    the chord-transition matrix per mode, the entry vector per mode, and the key-transition matrix.
    Read through the adapter's own methods, so these ARE the decoder's values (#6)."""

    def __init__(self, table_set="all", leftover=LEFTOVER):
        self.name = table_set
        self.adapter = pd.FittedAdapter(leftover_mode=leftover, table_set=table_set)
        self.adapter.mode_marginal("major")            # warm the class marginal once
        self.vocab = pd.Vocabulary(self.adapter.tables)
        self.cls_keys = list(self.vocab.keylist)
        self.C = len(self.cls_keys)
        self.cidx = {k: i for i, k in enumerate(self.cls_keys)}
        C = self.C
        # chord transition: L[mode][prev, next]; mode 0 = major, 1 = minor
        self.Lchord = np.empty((2, C, C), dtype=np.float64)
        for mi, is_major in ((0, True), (1, False)):
            for a, ak in enumerate(self.cls_keys):
                pa = self.vocab.classes[ak]
                row = self.Lchord[mi, a]
                for b, bk in enumerate(self.cls_keys):
                    row[b] = self.adapter.chord_trans_logp(pa, self.vocab.classes[bk], is_major)
        # entry chord per mode
        self.Lentry = np.empty((2, C), dtype=np.float64)
        for mi, is_major in ((0, True), (1, False)):
            for a, ak in enumerate(self.cls_keys):
                self.Lentry[mi, a] = self.adapter.entry_logp(self.vocab.classes[ak], is_major)
        # key transition (kidx = tonic for major, tonic+12 for minor)
        self.Lkey = np.empty((24, 24), dtype=np.float64)
        for ka in range(24):
            for kb in range(24):
                self.Lkey[ka, kb] = self.adapter.key_trans_logp(kkey(ka), kkey(kb))
        self.Lstay = np.array([self.Lkey[k, k] for k in range(24)], dtype=np.float64)
        self.Lkey_off = self.Lkey.copy()
        np.fill_diagonal(self.Lkey_off, NEG_INF)
        # per-key mode index, and the (24, C) entry array
        self.kmode = np.array([0] * 12 + [1] * 12, dtype=np.int64)
        self.Ent = self.Lentry[self.kmode]              # (24, C)
        self.cache = pd.ChordCache()


def kkey(kidx):
    """(tonic, is_major) of a key index: 0-11 major, 12-23 minor."""
    return (kidx % 12, kidx < 12)


def kidx_of(tonic, is_major):
    return (tonic % 12) if is_major else (tonic % 12) + 12


# ══════════════════════════════════════════════════════════════════════════════
# Ground truth on the event lattice
# ══════════════════════════════════════════════════════════════════════════════

def gt_event_labels(stem, piece, piece_dict, ts: TableSet):
    """Per event of `piece`: (kidx, cidx) of the ground-truth label, or None where the event carries no
    usable label. Uses the established GT→tick resolver and the OI-184 exclusions, all from
    gen_note_tables (#6): anacrusis events, events in a measured-misaligned (left-out) span, events in
    no GT span, indeterminate-key labels, and labels whose class is outside the decoder vocabulary are
    all None. Returns (labels, diagnostics)."""
    segs = gnt.gt_segments(stem)
    starts = [s["start"] for s in segs]
    excluded = {sp["idx"] for sp in gnt.excluded_zero_factor_segments(segs, piece_dict)}
    diag = Counter()
    labels = []
    for ev in piece.events:
        if ev[pd.EV_MEAS] == 0:
            labels.append(None)
            diag["anacrusis"] += 1
            continue
        si = gnt._seg_idx_for_tick(segs, starts, ev[pd.EV_START])
        if si < 0:
            labels.append(None)
            diag["no_gt_span"] += 1
            continue
        if si in excluded:
            labels.append(None)
            diag["misaligned_span_left_out"] += 1
            continue
        s = segs[si]
        if s["tonic"] is None or s["is_major"] is None:
            labels.append(None)
            diag["indeterminate_key"] += 1
            continue
        ck = s["cls"].inversion_free().key()
        ci = ts.cidx.get(ck)
        if ci is None:
            labels.append(None)
            diag["class_outside_vocabulary"] += 1
            diag["unmapped_" + ck] += 1
            continue
        labels.append((kidx_of(s["tonic"], s["is_major"]), ci, si))
        diag["labeled"] += 1
    return labels, diag


def gt_units(labels):
    """Maximal contiguous runs of labeled events → [(ev_lo, ev_hi)] (half-open, absolute event idx)."""
    units = []
    i = 0
    n = len(labels)
    while i < n:
        if labels[i] is None:
            i += 1
            continue
        j = i
        while j + 1 < n and labels[j + 1] is not None:
            j += 1
        units.append((i, j + 1))
        i = j + 1
    return units


def gt_path_for_unit(labels, lo, hi, seg_cap=SEG_CAP):
    """The ground-truth path over a unit: maximal runs of one GT SEGMENT (so two adjacent GT labels of
    identical (key, class) stay two segments — the ground truth says a chord change occurred), each run
    split into consecutive chunks of at most `seg_cap` events. Returns [(i, j, kidx, cidx)] in unit-
    relative event indices, plus the number of chunks that a cap split created."""
    path, splits = [], 0
    i = lo
    while i < hi:
        si = labels[i][2]
        j = i
        while j + 1 < hi and labels[j + 1][2] == si:
            j += 1
        k, c = labels[i][0], labels[i][1]
        a = i
        first = True
        while a <= j:
            b = min(a + seg_cap - 1, j)
            path.append((a - lo, b + 1 - lo, k, c))
            if not first:
                splits += 1
            first = False
            a = b + 1
        i = j + 1
    return path, splits


# ══════════════════════════════════════════════════════════════════════════════
# The lattice of one training / evaluation unit
# ══════════════════════════════════════════════════════════════════════════════

class UnitLattice:
    """One training unit's lattice as flat arrays. `is_head` marks the unit that starts the piece (only
    that one pays the prior + entry initial factors)."""

    __slots__ = ("stem", "lo", "hi", "n", "C", "is_head", "n_cand", "cand_span", "cand_kc",
                 "cand_feat", "span_i", "span_j", "cad", "prior_sig", "prior_inc", "F_gt",
                 "gt_ok", "n_events", "aug_key", "aug_state", "n_gt_seg", "gt_splits", "gt_prov",
                 "spans_from", "cstart", "cend")

    def __init__(self, stem, lo, hi, is_head):
        self.stem, self.lo, self.hi, self.is_head = stem, lo, hi, is_head
        self.n = hi - lo
        self.n_events = hi - lo


def build_unit(piece, stem, lo, hi, is_head, gt_path, ts: TableSet, sig_fifths, declared_mode,
               augment_gt=True, seg_cap=SEG_CAP):
    """Build the lattice arrays for one unit. `gt_path` may be None (an evaluation unit): then no
    augmentation happens and no ground-truth feature vector is computed."""
    ad, vocab, cache, C = ts.adapter, ts.vocab, ts.cache, ts.C
    lat = UnitLattice(stem, lo, hi, is_head)
    n = lat.n
    sig_key = None
    if sig_fifths is not None:
        for (t, m) in pd.KEYS_24:
            if m and glt._collection_fifths(t, m) == sig_fifths:
                sig_key = (t, m)
                break

    # ground-truth state per unit-relative event (for the augmentation + the consistency check)
    gt_state = [None] * n
    if gt_path is not None:
        for (a, b, k, c) in gt_path:
            for e in range(a, b):
                gt_state[e] = (k, c)

    span_i, span_j = [], []
    cand_span, cand_kc, cand_feat = [], [], []
    aug_key = aug_state = 0
    for i in range(n):
        for j in range(i + 1, min(n, i + seg_cap) + 1):
            ai, aj = lo + i, lo + j
            extra = None
            want = None
            if gt_path is not None and augment_gt:
                st = gt_state[i]
                if st is not None and all(gt_state[e] == st for e in range(i, j)):
                    want = st
                    extra = [kkey(st[0])]
            cands = pd._candidate_states_for_segment(piece, ai, aj, vocab, cache, pd.KEYS_24,
                                                     sig_key, extra_keys=extra)
            cset = set(cands)
            if want is not None:
                wt, wm = kkey(want[0])
                wtriple = (wt, wm, ts.cls_keys[want[1]])
                if wtriple not in cset:
                    # the ordinary state filters reject the ground truth here: force it in, counted.
                    cands = cands + [wtriple]
                    aug_state += 1
                elif extra is not None:
                    base = pd._candidate_states_for_segment(piece, ai, aj, vocab, cache, pd.KEYS_24,
                                                            sig_key)
                    if wtriple not in set(base):
                        aug_key += 1
            if not cands:
                continue
            s = len(span_i)
            span_i.append(i)
            span_j.append(j)
            seg_pcs = piece.overlap_pcs(ai, aj)
            for (tonic, is_major, ckey) in cands:
                feat = pd.segment_features(piece, ai, aj, tonic, is_major, vocab.classes[ckey],
                                           ad, cache, seg_pcs=seg_pcs)
                if feat is None:
                    continue
                cand_span.append(s)
                cand_kc.append(kidx_of(tonic, is_major) * C + ts.cidx[ckey])
                cand_feat.append((feat["emission"] + feat["missing_tone"], feat["spelling"],
                                  feat["bass"], feat["boundary"]))

    lat.C = C
    lat.span_i = np.asarray(span_i, dtype=np.int64)
    lat.span_j = np.asarray(span_j, dtype=np.int64)
    lat.cand_span = np.asarray(cand_span, dtype=np.int64)
    lat.cand_kc = np.asarray(cand_kc, dtype=np.int64)
    lat.cand_feat = np.asarray(cand_feat, dtype=np.float64).reshape(-1, 4)
    lat.n_cand = lat.cand_kc.size
    lat.aug_key, lat.aug_state = aug_key, aug_state
    # weight-independent index structures, built once (they are per-evaluation overhead otherwise)
    lat.spans_from = [[] for _ in range(n)]
    for s in range(lat.span_i.size):
        lat.spans_from[lat.span_i[s]].append(s)
    lat.cstart = np.searchsorted(lat.cand_span, np.arange(lat.span_i.size))
    lat.cend = np.searchsorted(lat.cand_span, np.arange(lat.span_i.size), side="right")

    # cadence features per unit-relative boundary event (1..n-1) toward each key
    cad = np.zeros((n, 24, 4), dtype=np.float64)
    for i in range(1, n):
        for k in range(24):
            t, m = kkey(k)
            fired = pd.cadence_site_features(piece, lo + i, t, m)
            for fi, f in enumerate(pd.CADENCE_FEATURES):
                if fired[f]:
                    cad[i, k, fi] = 1.0
    lat.cad = cad

    # the initial-state prior (head unit only)
    ps = np.zeros(24, dtype=np.float64)
    pinc = np.zeros(24, dtype=np.float64)
    if is_head:
        for k in range(24):
            t, m = kkey(k)
            a, b = ad.prior_terms(t, m, sig_fifths, declared_mode)
            ps[k], pinc[k] = a, b
    lat.prior_sig, lat.prior_inc = ps, pinc

    if gt_path is not None:
        lat.F_gt, lat.gt_prov = gt_features(piece, lo, gt_path, ts, sig_fifths, declared_mode, is_head)
        lat.n_gt_seg = len(gt_path)
    else:
        lat.F_gt, lat.gt_prov, lat.n_gt_seg = None, None, 0
    return lat


def gt_features(piece, lo, gt_path, ts: TableSet, sig_fifths, declared_mode, is_head):
    """The 13-feature vector of the ground-truth path, by the SAME rules the lattice recursion uses:
    prior + entry at a head unit's first segment; key transition at every boundary (the stay cell when
    the key does not change); chord transition at a same-key boundary; entry at a key change; cadence
    features at every boundary. Also returns the below-threshold (leftover) provenance counts of the
    ground truth's own transitions — the dispatch's Task-1 establishment item."""
    ad, vocab, cache = ts.adapter, ts.vocab, ts.cache
    F = np.zeros(NW, dtype=np.float64)
    prov = Counter()
    for si, (a, b, k, c) in enumerate(gt_path):
        tonic, is_major = kkey(k)
        cls = vocab.classes[ts.cls_keys[c]]
        feat = pd.segment_features(piece, lo + a, lo + b, tonic, is_major, cls, ad, cache)
        if feat is None:
            return None, prov
        F[WI["emission"]] += feat["emission"] + feat["missing_tone"]
        F[WI["spelling"]] += feat["spelling"]
        F[WI["bass"]] += feat["bass"]
        F[WI["boundary"]] += feat["boundary"]
        if si == 0:
            if is_head:
                psig, pinc = ad.prior_terms(tonic, is_major, sig_fifths, declared_mode)
                F[WI["prior"]] += psig
                F[WI["declared_mode"]] += pinc
                F[WI["entry"]] += ad.entry_logp(cls, is_major)
                prov["entry_" + ad.entry_prov(cls, is_major).split(":")[0]] += 1
            continue
        pa, pb, pk, pc = gt_path[si - 1]
        pcls = vocab.classes[ts.cls_keys[pc]]
        F[WI["key_trans"]] += ad.key_trans_logp(kkey(pk), (tonic, is_major))
        if pk == k:
            F[WI["chord_trans"]] += ad.chord_trans_logp(pcls, cls, is_major)
            prov["chord_" + ad.chord_trans_prov(pcls, cls, is_major).split(":")[0]] += 1
        else:
            F[WI["entry"]] += ad.entry_logp(cls, is_major)
            prov["entry_" + ad.entry_prov(cls, is_major).split(":")[0]] += 1
        fired = pd.cadence_site_features(piece, lo + a, tonic, is_major)
        for fi, f in enumerate(pd.CADENCE_FEATURES):
            if fired[f]:
                F[WI[CAD_W[fi]]] += 1.0
    return F, prov


# ══════════════════════════════════════════════════════════════════════════════
# The forward-backward over a unit lattice (log-domain, scaled matmuls)
# ══════════════════════════════════════════════════════════════════════════════

def _logsumexp_rows(A):
    m = A.max(axis=1)
    out = np.full(m.shape, NEG_INF)
    ok = np.isfinite(m)
    if ok.any():
        out[ok] = m[ok] + np.log(np.exp(A[ok] - m[ok][:, None]).sum(axis=1))
    return out


class WeightContext:
    """The weight-dependent transition matrices, built ONCE per objective evaluation and shared by
    every unit (each costs ~2·C² exponentials; rebuilding them per unit dominated the objective)."""

    __slots__ = ("Ent", "Tc", "Lk", "stay", "TcL", "eLk", "eLkL")

    def __init__(self, ts, w):
        self.Ent = w[WI["entry"]] * ts.Ent
        self.Tc = np.exp(w[WI["chord_trans"]] * ts.Lchord)
        self.TcL = self.Tc * ts.Lchord
        # the key-change matrix keeps its -inf diagonal at ANY weight (0·-inf would be a NaN)
        self.Lk = np.where(np.isfinite(ts.Lkey_off), w[WI["key_trans"]] * ts.Lkey_off, NEG_INF)
        self.eLk = np.exp(self.Lk)
        fin = np.isfinite(ts.Lkey_off)
        self.eLkL = np.zeros_like(self.eLk)
        np.multiply(self.eLk, ts.Lkey_off, out=self.eLkL, where=fin)
        self.stay = w[WI["key_trans"]] * ts.Lstay


def unit_logZ_and_expect(lat: UnitLattice, ts: TableSet, w, want_grad=True, semiring="sum",
                         wctx=None):
    """logZ (or the best-path score when semiring='max') over the unit's lattice, and — when
    want_grad — the model's expected feature vector E_w[F]. One recursion, two semirings: the max-plus
    run is the establishment cross-check against the pinned decoder's Viterbi, the log-sum-exp run is
    the fit's partition function."""
    C, n = lat.C, lat.n
    K, KC = 24, 24 * lat.C
    wc = np.array([w[WI[x]] for x in CONTENT_W], dtype=np.float64)
    w_prior, w_dmode = w[WI["prior"]], w[WI["declared_mode"]]
    w_entry, w_key, w_chord = w[WI["entry"]], w[WI["key_trans"]], w[WI["chord_trans"]]
    wcad = np.array([w[WI[x]] for x in CAD_W], dtype=np.float64)
    is_max = (semiring == "max")

    cw = lat.cand_feat @ wc                                     # weighted content per candidate
    # the weight-dependent transition matrices are shared by every unit at a given w — built once per
    # objective evaluation by WeightContext and passed in (they cost ~22k exponentials each).
    if wctx is None:
        wctx = WeightContext(ts, w)
    Ent, Tc, Lk, stay, TcL, eLk = (wctx.Ent, wctx.Tc, wctx.Lk, wctx.stay, wctx.TcL, wctx.eLk)
    cadw = lat.cad @ wcad                                       # (n, 24)

    spans_from, cstart, cend = lat.spans_from, lat.cstart, lat.cend

    start_in = np.empty((K, C))
    if lat.is_head:
        start_in[:] = (w_prior * lat.prior_sig + w_dmode * lat.prior_inc)[:, None] + Ent
    else:
        start_in[:] = 0.0                       # a resuming unit starts free (no initial factor)

    def trans_in(prev):
        """The transition-in score (24, C) at a boundary whose incoming states are `prev` (24, C)."""
        m = prev.max(axis=1)
        fin = np.isfinite(m)
        sm = np.full((K, C), NEG_INF)
        R = np.zeros((K, C))
        E = np.zeros((K, C))
        if fin.any():
            mm = np.where(fin, m, 0.0)
            E = np.exp(prev - mm[:, None])
            E[~fin] = 0.0
            if is_max:
                for mi, sl in ((0, slice(0, 12)), (1, slice(12, 24))):
                    sm[sl] = (prev[sl][:, :, None] + w_chord * ts.Lchord[mi][None]).max(axis=1)
            else:
                for mi, sl in ((0, slice(0, 12)), (1, slice(12, 24))):
                    R[sl] = E[sl] @ Tc[mi]
                with np.errstate(divide="ignore"):
                    sm = np.log(R) + mm[:, None]
                sm[~fin] = NEG_INF
            sm = sm + stay[:, None]
        # key-change branch
        Bk = prev.max(axis=1) if is_max else _logsumexp_rows(prev)
        if is_max:
            kc = (Bk[:, None] + Lk).max(axis=0)
        else:
            mb = Bk.max()
            if np.isfinite(mb):
                with np.errstate(divide="ignore"):
                    kc = np.log(np.exp(Bk - mb) @ eLk) + mb
            else:
                kc = np.full(K, NEG_INF)
        ent_in = kc[:, None] + Ent
        if is_max:
            ins = np.maximum(sm, ent_in)
        else:
            ins = np.logaddexp(sm, ent_in)
        return ins, sm, ent_in, E, R, Bk

    logA = np.full((n + 1, K, C), NEG_INF)
    base = np.full((n, K, C), NEG_INF)
    keep = [None] * n
    for b in range(n):
        if b == 0:
            ins = start_in.copy()
            keep[b] = None
        else:
            if not np.isfinite(logA[b]).any():
                continue
            ins, sm, ent_in, E, R, Bk = trans_in(logA[b])
            keep[b] = (sm, ent_in, E, R, Bk)
        base[b] = (ins + cadw[b][:, None]) if b > 0 else ins
        flat = base[b].reshape(-1)
        for s in spans_from[b]:
            lo_c, hi_c = cstart[s], cend[s]
            if hi_c <= lo_c:
                continue
            kc_i = lat.cand_kc[lo_c:hi_c]
            contrib = flat[kc_i] + cw[lo_c:hi_c]
            j = lat.span_j[s]
            tgt = logA[j].reshape(-1)
            cur = tgt[kc_i]
            tgt[kc_i] = np.maximum(cur, contrib) if is_max else np.logaddexp(cur, contrib)
    fin = logA[n].reshape(-1)
    if not np.isfinite(fin).any():
        return NEG_INF, None, NEG_INF
    if is_max:
        return float(fin.max()), None, None
    mx = fin.max()
    logZ = float(mx + math.log(np.exp(fin - mx).sum()))
    if not want_grad:
        return logZ, None, None
    del fin, mx

    # ── backward: M[b][k,c] = LSE over spans starting at b of (content + logB at the span end) ──
    logB = np.full((n + 1, K, C), NEG_INF)
    logB[n] = 0.0
    M = np.full((n, K, C), NEG_INF)
    Mc = np.full((n, K, C), NEG_INF)
    for b in range(n - 1, -1, -1):
        mflat = M[b].reshape(-1)
        for s in spans_from[b]:
            lo_c, hi_c = cstart[s], cend[s]
            if hi_c <= lo_c:
                continue
            kc_i = lat.cand_kc[lo_c:hi_c]
            j = lat.span_j[s]
            contrib = cw[lo_c:hi_c] + logB[j].reshape(-1)[kc_i]
            mflat[kc_i] = np.logaddexp(mflat[kc_i], contrib)
        Mc[b] = M[b] + (cadw[b][:, None] if b > 0 else 0.0)
        if b == 0:
            break
        # logB[b][k,c]: same-key (chord transition out) + key-change (entry into any other key)
        mm = Mc[b].max(axis=1)
        finm = np.isfinite(mm)
        same = np.full((K, C), NEG_INF)
        if finm.any():
            mmm = np.where(finm, mm, 0.0)
            EM = np.exp(Mc[b] - mmm[:, None])
            EM[~finm] = 0.0
            for mi, sl in ((0, slice(0, 12)), (1, slice(12, 24))):
                with np.errstate(divide="ignore"):
                    same[sl] = np.log(EM[sl] @ Tc[mi].T) + mmm[sl, None]
            same[~finm] = NEG_INF
        same = same + stay[:, None]
        G = _logsumexp_rows(Ent + Mc[b])                        # (24,)
        mg = G.max()
        if np.isfinite(mg):
            with np.errstate(divide="ignore"):
                kcb = np.log(eLk @ np.exp(G - mg)) + mg
        else:
            kcb = np.full(K, NEG_INF)
        logB[b] = np.logaddexp(same, kcb[:, None])

    # ── expectations ──
    EF = np.zeros(NW, dtype=np.float64)
    bi = lat.span_i[lat.cand_span]
    bj = lat.span_j[lat.cand_span]
    g = np.exp(base.reshape(n, -1)[bi, lat.cand_kc] + cw
               + logB.reshape(n + 1, -1)[bj, lat.cand_kc] - logZ)
    EF[[WI[x] for x in CONTENT_W]] = g @ lat.cand_feat
    # segment posterior mass per (boundary, key, class)
    mu = np.bincount(bi * (K * C) + lat.cand_kc, weights=g, minlength=n * K * C).reshape(n, K, C)
    # cadence (the features attach to the boundary that starts the segment)
    EF[[WI[x] for x in CAD_W]] = np.einsum("bk,bkf->f", mu.sum(axis=2), lat.cad)
    # the initial segment: prior + declared mode + entry (head units only)
    m0 = mu[0]
    if lat.is_head:
        EF[WI["prior"]] += float((m0.sum(axis=1) * lat.prior_sig).sum())
        EF[WI["declared_mode"]] += float((m0.sum(axis=1) * lat.prior_inc).sum())
        EF[WI["entry"]] += float((m0 * ts.Ent).sum())
    for b in range(1, n):
        if keep[b] is None or not np.isfinite(mu[b]).any() or mu[b].sum() <= 0.0:
            continue
        sm, ent_in, E, R, Bk = keep[b]
        ins = base[b] - cadw[b][:, None]
        d = np.full((K, C), NEG_INF)
        np.subtract(sm, ins, out=d, where=np.isfinite(ins))
        sh_same = np.exp(d)                       # the two branch shares are complements: they sum to 1
        m_same = mu[b] * sh_same
        m_ent = mu[b] - m_same
        # entry (at a key change) and the key-transition change cells
        EF[WI["entry"]] += float((m_ent * ts.Ent).sum())
        EF[WI["key_trans"]] += float((m_same.sum(axis=1) * ts.Lstay).sum())
        mb = Bk.max()
        if np.isfinite(mb):
            eb = np.exp(Bk - mb)
            den = eb @ eLk                                    # eLk is 0 on the diagonal (exp(-inf))
            num = eb @ wctx.eLkL
            with np.errstate(divide="ignore", invalid="ignore"):
                ratio = np.where(den > 0, num / den, 0.0)
            EF[WI["key_trans"]] += float((m_ent.sum(axis=1) * ratio).sum())
        # chord transition: E[L] under the same-key branch
        for mi, sl in ((0, slice(0, 12)), (1, slice(12, 24))):
            AL = E[sl] @ TcL[mi]
            with np.errstate(divide="ignore", invalid="ignore"):
                r = np.where(R[sl] > 0, AL / R[sl], 0.0)
            EF[WI["chord_trans"]] += float((m_same[sl] * r).sum())
    # the backward pass's own logZ — an internal establishment of the two recursions against each other
    z0 = (start_in + Mc[0]).reshape(-1)
    mz = z0.max()
    logZ_bwd = float(mz + math.log(np.exp(z0 - mz).sum())) if np.isfinite(mz) else NEG_INF
    return logZ, EF, logZ_bwd


# ══════════════════════════════════════════════════════════════════════════════
# The convex objective over a training set
# ══════════════════════════════════════════════════════════════════════════════

class TrainingSet:
    """The built lattices of a set of training units + their ground-truth feature vectors."""

    def __init__(self, units, ts: TableSet, label=""):
        self.units = units
        self.ts = ts
        self.label = label
        self.F_gt = np.stack([u.F_gt for u in units]) if units else np.zeros((0, NW))
        self.tokens = int(sum(u.n_events for u in units))
        self.n_cand = int(sum(u.n_cand for u in units))
        self.skipped = 0                 # units with no complete path at the last evaluation

    def nll_and_grad(self, x, lam):
        """NLL(w)/tokens + λ‖w − w_identity‖² and its gradient. Convex (linear numerator + convex logZ
        + a convex quadratic)."""
        tot = 0.0
        gsum = np.zeros(NW)
        wctx = WeightContext(self.ts, x)
        self.skipped = 0
        for u in self.units:
            logZ, EF, _zb = unit_logZ_and_expect(u, self.ts, x, wctx=wctx)
            if EF is None:
                # a unit with no complete path through its lattice contributes nothing; never silent
                self.skipped += 1
                continue
            tot += logZ - float(u.F_gt @ x)
            gsum += EF - u.F_gt
        T = max(1, self.tokens)
        d = x - identity_vector()
        return tot / T + lam * float(d @ d), gsum / T + 2.0 * lam * d


def fit(training: TrainingSet, lam, x0=None, maxiter=200, verbose=False):
    """L-BFGS-B on the convex objective. Returns (x, record) with the convergence evidence the dispatch
    asks for: the objective trace (monotone decrease), the final gradient norm, and the optimizer's own
    termination status."""
    x0 = identity_vector() if x0 is None else np.array(x0, dtype=np.float64)
    evals = []            # every objective evaluation (line-search points included)
    iters = []            # the objective at each ACCEPTED iterate — this is the monotone trace
    last = {}

    def fun(x):
        f, g = training.nll_and_grad(x, lam)
        evals.append(float(f))
        last["f"] = float(f)
        return f, g

    def cb(xk):
        iters.append(last.get("f"))

    t0 = time.perf_counter()
    res = minimize(fun, x0, jac=True, method="L-BFGS-B", callback=cb,
                   options={"maxiter": maxiter, "ftol": 1e-11, "gtol": 1e-6})
    trace = [v for v in iters if v is not None] or evals
    f_end, g_end = training.nll_and_grad(res.x, lam)
    rec = {
        "lambda": lam, "n_units": len(training.units), "tokens": training.tokens,
        "objective_start": evals[0] if evals else None, "objective_end": float(f_end),
        "grad_norm_end": float(np.linalg.norm(g_end)),
        "n_objective_evals": len(evals), "iterations": int(res.nit),
        "status": str(res.message), "success": bool(res.success),
        # convexity evidence: the ACCEPTED-iterate objective sequence must decrease monotonically
        # (line-search evaluations legitimately over-shoot and are not part of this check)
        "monotone_decrease": bool(all(trace[i + 1] <= trace[i] + 1e-12 for i in range(len(trace) - 1))),
        "n_iterate_points": len(trace),
        "objective_trace_head": [round(v, 6) for v in trace[:5]],
        "objective_trace_tail": [round(v, 6) for v in trace[-5:]],
        "seconds": round(time.perf_counter() - t0, 1),
        "units_skipped_no_complete_path": int(getattr(training, "skipped", 0)),
        "weights": vec_to_weights(res.x),
    }
    if verbose:
        print(f"    lam={lam:<8g} obj {rec['objective_start']:.5f} -> {rec['objective_end']:.5f}  "
              f"|g|={rec['grad_norm_end']:.2e}  {rec['n_objective_evals']} evals  {rec['seconds']}s",
              flush=True)
    return res.x, rec


def heldout_nll(units, ts: TableSet, x):
    """Mean per-token NLL of a set of units under weights x — the INNER-validation criterion. It is a
    likelihood, never an accuracy metric: the firewall is intact (no grading module is reachable here)."""
    tot, tok = 0.0, 0
    wctx = WeightContext(ts, x)
    for u in units:
        logZ, _EF, _zb = unit_logZ_and_expect(u, ts, x, want_grad=False, wctx=wctx)
        if not np.isfinite(logZ):
            continue
        tot += logZ - float(u.F_gt @ x)
        tok += u.n_events
    return tot / max(1, tok)


# ══════════════════════════════════════════════════════════════════════════════
# Corpus loading and unit construction
# ══════════════════════════════════════════════════════════════════════════════

def load_corpus():
    pieces, prov = pd.load_pieces()
    ne = json.loads(NOTE_EVENTS.read_text(encoding="utf-8"))
    fa = json.loads(FOLD_ARTIFACT.read_text(encoding="utf-8"))
    covered = sorted(fa["stem_index"])
    fold_of = {s: fa["stem_index"][s]["fold"] for s in covered}
    return pieces, ne, covered, fold_of, prov


def build_units(stems, ts: TableSet, pieces, ne, augment_gt=True, verbose=False, want_gt=True):
    """All training units of a stem list under one frozen table set, plus the construction diagnostics
    the dispatch's Task-1 establishment asks for."""
    units = []
    diag = Counter()
    per_stem = {}
    t0 = time.perf_counter()
    for idx, stem in enumerate(stems):
        if stem in gnt.FLAGGED:
            diag["stems_excluded_flagged"] += 1
            continue
        piece = pieces[stem]
        sig, dm = pd.piece_header(stem)
        labels, ldiag = gt_event_labels(stem, piece, ne["pieces"][stem], ts)
        for k, v in ldiag.items():
            diag[k] += v
        us = gt_units(labels)
        if not us:
            diag["stems_without_any_label"] += 1
            continue
        diag["stems_used"] += 1
        diag["units"] += len(us)
        if len(us) > 1:
            diag["stems_with_resuming_units"] += 1
            diag["resuming_units"] += len(us) - 1
        stem_units = []
        for ui, (lo, hi) in enumerate(us):
            gp, splits = gt_path_for_unit(labels, lo, hi) if want_gt else (None, 0)
            diag["gt_segments"] += len(gp or [])
            diag["gt_segments_from_cap_split"] += splits
            lat = build_unit(piece, stem, lo, hi, ui == 0, gp, ts, sig, dm, augment_gt=augment_gt)
            if want_gt and lat.F_gt is None:
                diag["units_dropped_unscorable_gt"] += 1
                continue
            diag["aug_key_widened_spans"] += lat.aug_key
            diag["aug_state_forced_spans"] += lat.aug_state
            diag["candidates"] += lat.n_cand
            if lat.gt_prov:
                for k, v in lat.gt_prov.items():
                    diag["gtprov_" + k] += v
            units.append(lat)
            stem_units.append(lat)
        per_stem[stem] = stem_units
        if verbose and idx % 40 == 0:
            print(f"    [{idx + 1}/{len(stems)}] {stem} units={len(us)} "
                  f"({time.perf_counter() - t0:.0f}s)", flush=True)
    diag["build_seconds"] = round(time.perf_counter() - t0, 1)
    return units, diag, per_stem


# ══════════════════════════════════════════════════════════════════════════════
# Establishment (#19): the recursion against the pinned decoder; the gradient against finite differences
# ══════════════════════════════════════════════════════════════════════════════

def establish_viterbi_parity(pieces, ts: TableSet, stems, weights=None, verbose=True):
    """The fit's lattice recursion, run in the MAX-PLUS semiring over a whole piece, must reproduce
    `probe_decoder.decode_piece`'s best-path score exactly. This establishes that the partition function
    is taken over the SAME lattice the decoder searches — the thing that makes the fitted weights mean
    what they claim at decode time."""
    x = identity_vector() if weights is None else np.asarray(weights, dtype=np.float64)
    wdict = vec_to_weights(x)
    rows = []
    for stem in stems:
        piece = pieces[stem]
        sig, dm = pd.piece_header(stem)
        ad = pd.FittedAdapter(leftover_mode=LEFTOVER, table_set=ts.name, weights=wdict)
        ad._mode_marginal = ts.adapter._mode_marginal
        r = pd.decode_piece(piece, ad, ts.vocab, ts.cache, seg_cap=SEG_CAP,
                            sig_fifths=sig, declared_mode=dm)
        lat = build_unit(piece, stem, 0, len(piece.events), True, None, ts, sig, dm, augment_gt=False)
        best, _e, _z = unit_logZ_and_expect(lat, ts, x, want_grad=False, semiring="max")
        rows.append({"stem": stem, "decoder_score": round(r.total_score, 6),
                     "lattice_maxplus": round(best, 6),
                     "delta": round(best - r.total_score, 9)})
        if verbose:
            print(f"    {stem:10s} decoder {r.total_score:12.5f}  lattice(max) {best:12.5f}  "
                  f"delta {best - r.total_score:+.2e}")
    worst = max(abs(x["delta"]) for x in rows) if rows else 0.0
    return {"rows": rows, "max_abs_delta": worst, "pass": bool(worst < 1e-6)}


def establish_gradient(training: TrainingSet, x=None, lam=0.0, eps=1e-5, verbose=True):
    """The analytic gradient (forward-backward expectations) against central finite differences of the
    objective — the check that the expectation arithmetic is what it claims to be."""
    x = identity_vector() if x is None else np.asarray(x, dtype=np.float64)
    f0, g = training.nll_and_grad(x, lam)
    num = np.zeros(NW)
    for i in range(NW):
        xp, xm = x.copy(), x.copy()
        xp[i] += eps
        xm[i] -= eps
        fp, _ = training.nll_and_grad(xp, lam)
        fm, _ = training.nll_and_grad(xm, lam)
        num[i] = (fp - fm) / (2 * eps)
    rel = np.abs(g - num) / np.maximum(1e-9, np.abs(num))
    out = {"objective": float(f0),
           "analytic": {W_NAMES[i]: float(g[i]) for i in range(NW)},
           "numeric": {W_NAMES[i]: float(num[i]) for i in range(NW)},
           "max_abs_diff": float(np.max(np.abs(g - num))),
           "max_rel_diff": float(np.max(rel)),
           "pass": bool(np.max(np.abs(g - num)) < 1e-6)}
    if verbose:
        print(f"    gradient check: max|analytic-numeric| = {out['max_abs_diff']:.3e} "
              f"(max rel {out['max_rel_diff']:.3e})  {'PASS' if out['pass'] else 'FAIL'}")
    return out


def establish_forward_backward(units, ts: TableSet, x=None, k=6):
    """The forward and backward recursions must agree on logZ (they are independent computations of the
    same quantity), and Z must contain the ground-truth path (logZ >= w·F_gt)."""
    x = identity_vector() if x is None else np.asarray(x, dtype=np.float64)
    rows = []
    for u in units[:k]:
        lz, _EF, lzb = unit_logZ_and_expect(u, ts, x)
        rows.append({"stem": u.stem, "span": [u.lo, u.hi], "logZ_forward": round(lz, 8),
                     "logZ_backward": round(lzb, 8), "delta": round(lzb - lz, 10),
                     "gt_path_score": round(float(u.F_gt @ x), 6),
                     "logZ_minus_gt": round(lz - float(u.F_gt @ x), 6)})
    return {"rows": rows,
            "max_abs_fb_delta": max(abs(r["delta"]) for r in rows) if rows else 0.0,
            "gt_within_Z": bool(all(r["logZ_minus_gt"] >= -1e-6 for r in rows))}


# ══════════════════════════════════════════════════════════════════════════════
# The fold driver (OI-176: 5-fold grouped CV; model selection inside the training folds only)
# ══════════════════════════════════════════════════════════════════════════════

# The L2 strength is chosen by INNER validation WITHIN the training folds (OI-176 item 3). The inner
# split is a held-out TRAINING fold — for outer fold i, the inner validation set is training fold
# (i+1) mod 5, and the inner fit uses the other three. Declared; it never touches the outer held-out
# fold. The grid is walked from strong to weak regularization with a warm start (a regularization path),
# which is why each step converges in few evaluations.
LAMBDA_GRID = (1e-2, 3e-3, 1e-3, 3e-4)
N_FOLDS = glt.N_FOLDS


def fit_one(label, ts, units, fold_of, inner_val_fold, verbose=True):
    """The λ path on the inner split, then the final fit on ALL the label's training units."""
    inner_val = [u for u in units if fold_of[u.stem] == inner_val_fold]
    inner_tr = [u for u in units if fold_of[u.stem] != inner_val_fold]
    tr_inner = TrainingSet(inner_tr, ts, label + "/inner")
    path = []
    x = identity_vector()
    xs = {}
    for lam in LAMBDA_GRID:
        x, rec = fit(tr_inner, lam, x0=x, verbose=verbose)
        rec["inner_val_nll_per_token"] = float(heldout_nll(inner_val, ts, x))
        rec["inner_val_units"] = len(inner_val)
        path.append(rec)
        xs[lam] = x.copy()
        if verbose:
            print(f"      inner-validation NLL/token {rec['inner_val_nll_per_token']:.6f}",
                  flush=True)
    best = min(path, key=lambda r: r["inner_val_nll_per_token"])
    tr_all = TrainingSet(units, ts, label)
    xf, recf = fit(tr_all, best["lambda"], x0=xs[best["lambda"]], verbose=verbose)
    return xf, {"label": label, "inner_validation_fold": inner_val_fold,
                "lambda_path": path, "lambda_selected": best["lambda"], "final_fit": recf}


def run_fit(out_path=None, verbose=True, folds=None):
    t_all = time.perf_counter()
    pieces, ne, covered, fold_of, prov = load_corpus()
    result = {"folds": {}, "all": None}
    established = {}
    todo = list(range(N_FOLDS)) if folds is None else list(folds)
    do_all = folds is None or folds == []

    for fold in todo:
        if verbose:
            print(f"\n=== outer fold {fold} (held out) — tables fit on its complement ===", flush=True)
        ts = TableSet(f"fold{fold}")
        stems = [s for s in covered if fold_of[s] != fold]
        units, diag, _per = build_units(stems, ts, pieces, ne, verbose=verbose)
        if fold == todo[0] and "gradient" not in established:
            established["viterbi_parity"] = establish_viterbi_parity(
                pieces, ts, ["bwv269", "bwv352", "bwv10.7"], verbose=verbose)
            established["forward_backward"] = establish_forward_backward(units, ts)
            established["gradient"] = establish_gradient(
                TrainingSet(units[:8], ts, "gradcheck"), verbose=verbose)
        x, rec = fit_one(f"fold{fold}", ts, units, fold_of, (fold + 1) % N_FOLDS, verbose=verbose)
        rec["construction"] = {k: v for k, v in sorted(diag.items())}
        rec["weights"] = vec_to_weights(x)
        result["folds"][str(fold)] = rec
        del ts, units

    if do_all:
        if verbose:
            print("\n=== the publishable all-326 fit (reported BESIDE the CV headline) ===", flush=True)
        ts = TableSet("all")
        units, diag, _per = build_units(sorted(covered), ts, pieces, ne, verbose=verbose)
        x, rec = fit_one("all", ts, units, fold_of, 0, verbose=verbose)
        rec["construction"] = {k: v for k, v in sorted(diag.items())}
        rec["weights"] = vec_to_weights(x)
        result["all"] = rec

    result["provenance"] = {
        "generator": glt._rel(Path(__file__)),
        "instrument_commit": glt._git_head(),
        "note_events_git_hash": prov["corpus_git_hash"],
        "fold_artifact": glt._rel(FOLD_ARTIFACT),
        "protocol": ("cowork_prefit_gates.md — OI-176 (5-fold grouped held-out; every fitted object "
                     "train-fold-only; model selection by inner validation inside the training folds) "
                     "and OI-177 (capacity budget; the weight-vector cap amended <=12 -> <=14 by user "
                     "ratification 2026-07-19, ruling C1)"),
        "weight_vector": W_NAMES,
        "n_weights": NW,
        "identity_weights": vec_to_weights(identity_vector()),
        "objective": ("semi-Markov conditional log-likelihood of the ground-truth path: "
                      "NLL(w) = sum_u [ logZ_u(w) - w.F(y*_u) ] / tokens + lambda*||w - w_identity||^2. "
                      "Convex (linear numerator, convex logZ, convex quadratic). The L2 anchor is the "
                      "ratified generative baseline, so lambda -> infinity recovers the identity-weight "
                      "ablation arm exactly."),
        "lambda_grid": list(LAMBDA_GRID),
        "seg_cap_events": SEG_CAP, "key_prune_topk": pd.KEY_PRUNE_TOPK,
        "leftover_rule": f"option 2a ({LEFTOVER})",
        "cadence_approach_window": (f"{pd.CADENCE_APPROACH_BEATS} beats "
                                    f"({pd.CADENCE_APPROACH_TICKS} ticks) — user ruling R1 (W1)"),
        "firewall": ("this generator imports no grading module; the grading of the fitted weights is "
                     "downstream in fit_run.py and feeds no value back"),
    }
    result["establishment"] = established
    result["wall_seconds"] = round(time.perf_counter() - t_all, 1)
    if out_path:
        Path(out_path).write_text(json.dumps(result, indent=1), encoding="utf-8")
    return result


def main(argv):
    """--folds i   fit outer fold i alone (the folds are independent — one process each)
       --all       fit only the publishable all-326 model
       no argument everything in one process (writes weight_fit.json directly)
    The per-part artifacts are merged by `merge_parts`."""
    out = _HERE / "weight_fit.json"
    folds = None
    if argv and argv[0] == "--folds":
        folds = [int(x) for x in argv[1].split(",")]
        out = _HERE / f"weight_fit_part_folds{argv[1].replace(',', '_')}.json"
    elif argv and argv[0] == "--all":
        folds = []
        out = _HERE / "weight_fit_part_all.json"
    elif argv and argv[0] == "--merge":
        merge_parts()
        return
    r = run_fit(out_path=out, verbose=True, folds=folds)
    print(f"\nwrote {out}  ({r['wall_seconds']}s)")


def merge_parts():
    """Merge the per-part artifacts written by the parallel fold processes into weight_fit.json. Each
    part is an independent, self-provenanced fit of its own fold; merging only concatenates them."""
    parts = sorted(_HERE.glob("weight_fit_part_*.json"))
    if not parts:
        raise SystemExit("STOP: no weight_fit_part_*.json to merge")
    merged = {"folds": {}, "all": None, "establishment": {}, "parts": []}
    wall = 0.0
    for p in parts:
        d = json.loads(p.read_text(encoding="utf-8"))
        merged["folds"].update(d.get("folds") or {})
        if d.get("all"):
            merged["all"] = d["all"]
        for k, v in (d.get("establishment") or {}).items():
            merged["establishment"].setdefault(k, v)
        merged["provenance"] = d["provenance"]
        merged["parts"].append({"file": glt._rel(p), "wall_seconds": d.get("wall_seconds")})
        wall = max(wall, d.get("wall_seconds") or 0.0)
    missing = [str(i) for i in range(N_FOLDS) if str(i) not in merged["folds"]]
    if missing or merged["all"] is None:
        raise SystemExit(f"STOP: incomplete merge — missing folds {missing}, "
                         f"all-326 {'missing' if merged['all'] is None else 'present'}")
    merged["wall_seconds"] = round(wall, 1)
    merged["provenance"]["assembly"] = ("fitted as independent parallel processes, one per outer fold "
                                        "plus the all-326 model, then merged; each part carries its own "
                                        "provenance and its own convergence record")
    (_HERE / "weight_fit.json").write_text(json.dumps(merged, indent=1), encoding="utf-8")
    print(f"merged {len(parts)} parts -> weight_fit.json")


if __name__ == "__main__":
    main(sys.argv[1:])
