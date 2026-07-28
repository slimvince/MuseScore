#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
# MuseScore-Studio-CLA-applies
#
# MuseScore Studio
# Music Composition & Notation
#
# Copyright (C) 2026 MuseScore Limited
"""gen_window_study.py — OI-206 Task 2: the windowed-vs-whole-piece decode study.

★ THE QUESTION (the Stage-3.1b transfer question, UNMEASURED for the JOINT estimator). 3.1b
(docs/p3_granularity_ab_3_1b.md) A/B-measured window-vs-whole-score for the LEGACY analyzer and
found window BEATS whole on DCML accuracy (Mozart 35/65) — whole-score was SHELVED. This module
measures, for the JOINT estimator's OWN decode, how the committed reading and its DCML accuracy
depend on the analyzed SPAN, and how fast a queried reading STABILIZES as the span grows — the two
inputs the OI-206 fix decision surface needs (the accuracy cost of bounding the span; the measured
stopping criterion for the user's recorded grow-until-satisfied design).

★ WHAT IS DECODED. For every covered corpus piece and every DOWNBEAT query tick t, the SAME pinned
production decode (probe_decoder.decode_piece; seg_cap 4, KEYS_24 candidate pool with the ratified §5
prune inside, the SELECTED weight vector the C++ module embeds, leftover 2a, table_set 'all') is run
on nested spans CENTERED on t: span sizes in MEASURES {4, 8, 16, 32, 64, whole} clipped to the piece
bounds. Per span we read, at t: the committed (key, class); the §3.3 group-(i) key-axis gap of the
committed segment containing t (probe_decoder._segment_posterior's per-segment key gap — the SAME
quantity gen_posterior_slice publishes); and whether the (key, class) reading at t equals the
whole-piece decode's reading at t.

★ EXACT WINDOW CONSTRUCTION (declared, #17). m_c = the query downbeat event's measure. For span S
(measures): m_lo = m_c - S//2, m_hi = m_c + (S - 1 - S//2), clipped to [m_min, m_max] (the piece's
measure range). The window is every event whose measure is in [m_lo, m_hi]; sub_piece re-indexes
them but PRESERVES absolute ticks (so overlap membership and the ★R1 approach window are the window's
own — the honest bounded context). Nested by construction (m_lo non-increasing, m_hi non-decreasing
as S grows). span='whole' == all events == the whole-piece decode. A window that clips to the whole
piece IS the whole-piece decode (recorded as clipped_to_whole). Query points: every event at
EV_BEAT==1.0 with EV_MEAS >= the first real (non-anacrusis) measure — the declared "every downbeat"
sample.

★ ESTABLISHMENT (#19; a mismatch is a #13 STOP, never silently absorbed). Before any window figure
is trusted: the WHOLE-PIECE decode this module runs must reproduce decode_parity_ref.json's committed
'selected' segments (i, j, tonic, is_major, class_key) per stem AND its total_score — i.e. the decode
here IS the production decode. The windowed decodes reuse the identical decode_piece on sub_pieces.

★ THREE MEASURED CURVES.
  (1) STABILITY (no ground truth): per span, the fraction of queries whose (key,class) reading equals
      the whole-piece reading (count + duration-weighted), and the distribution of the SMALLEST span
      at which a query's reading becomes stable (== whole and unchanged for all larger spans) —
      including whether that stabilizing span is a genuinely BOUNDED window (< whole) or needs the
      whole piece. This is the measured "how much context a query actually needs" curve.
  (2) ACCURACY (DCML, the robust unit's cell basis; the established substrate import-only). For spans
      {8,16,32,whole}, at each query: ROOT agree = compare_analyses.roots_agree(win_root, dcml_root);
      KEY-LOCAL agree = compare_rn._our_key_ident(win_key) == compare_rn._dcml_key_tonic(dcml_local).
      The DCML spans are the WiR (When-in-Rome) GT aligned exactly as tools/a8_rebaseline_measure.py
      does (compare_analyses._dcml_time_spans over the whole-piece anchor regions) — computed once per
      piece, identical for all span sizes, so the windowed-vs-whole accuracy DELTA is convention-
      robust. Does bounding the span COST ground-truth accuracy, and where.
  (3) COST: the Python-reference decode wall time per span (decode_piece's own timer). This completes
      the SHAPE of the cost-vs-span curve (how decode cost scales with span). It is the PYTHON
      reference decoder, NOT the C++ producer — the absolute interactive latency lives in
      tools/notation_seams/noteseam_latency.json (OI-203); the two are never conflated (#19).

★ PREDICTIONS (#17b — recorded in the artifact BEFORE measuring; a band miss is a REPORTED finding,
not silently absorbed). See PREDICTIONS below.

Artifacts (#17f): window_study.json (full per-query data + aggregates) + a printed summary.
Deterministic. Read-only (imports the pinned decoder + the grading substrate; touches no production
code, no golden, no corpus, no tools/robust_stop/).

Usage:
    python tools/joint_estimator/gen_window_study.py                    # full corpus: establish + write
    python tools/joint_estimator/gen_window_study.py --stems bwv269 bwv352   # subset dry-run (no write)
    python tools/joint_estimator/gen_window_study.py --limit 20         # first 20 pieces, write
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from bisect import bisect_right
from collections import Counter, defaultdict
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent.parent
sys.path.insert(0, str(_ROOT / "tools"))
sys.path.insert(0, str(_HERE))

import probe_decoder as pd            # noqa: E402  the pinned production decoder — IMPORT-ONLY
import compare_analyses as cmp        # noqa: E402  Region, _dcml_time_spans, roots_agree (substrate)
import compare_rn as crn              # noqa: E402  _our_key_ident, _dcml_key_tonic (substrate)
import dcml_parser as dcml            # noqa: E402  load_wir_regions / find_wir_file (WiR GT)

SEG_CAP = 4
LEFTOVER = "freq"
TPB = pd.TICKS_PER_QUARTER            # 480; DCML abs_tick == quarterbeats*480 uses the same unit
SPANS = [4, 8, 16, 32, 64, "whole"]   # measure widths; 'whole' == the whole piece
ACC_SPANS = [8, 16, 32, "whole"]      # the accuracy-graded span sizes (dispatch Task 2.2)
WIR_DIR = _ROOT / "tools" / "dcml" / "when_in_rome"
ART_PATH = _HERE / "window_study.json"

# ── PREDICTIONS (#17b), recorded before measuring. A band miss is a reported finding. ──────────────
PREDICTIONS = {
    "stability_rises_monotonically_with_span": {
        "claim": "the fraction of queries whose reading equals the whole-piece reading rises "
                 "monotonically with span size and reaches ~1.0 at 'whole' by construction",
        "band": "monotone non-decreasing across {4,8,16,32,64}",
    },
    "most_queries_stable_below_whole": {
        "claim": "on this chorale-scale corpus MOST queries stabilize at a BOUNDED window well below "
                 "the whole piece (a local reading needs only local context)",
        "band": "fraction of queries whose smallest-stable span is a bounded (< whole) window >= 0.60; "
                "median smallest-stable width <= 16 measures",
    },
    "stability_fraction_at_small_spans": {
        "claim": "count stability vs whole-piece is already high at 8 measures and higher at 16",
        "band": "stability@8 >= 0.75 and stability@16 >= 0.88 (count)",
    },
    "accuracy_cost_of_bounding_is_small_but_nonzero": {
        "claim": "unlike the 3.1b legacy finding (window BEAT whole on Mozart), on the CHORALE-scale "
                 "established envelope WHOLE-piece is the measured-accurate form, so bounding the span "
                 "COSTS a little root/key-local accuracy; the cost shrinks as the span grows",
        "band": "root_agree@whole - root_agree@16 in [-0.01, +0.05] (whole >= windowed within ~5pp); "
                "key_local@whole - key_local@16 in [-0.01, +0.06]; both deltas larger at span 8",
    },
    "accuracy_sensitive_class": {
        "claim": "the worst accuracy drops at small spans are pieces with long modulation spans / "
                 "pieces whose global context revises the opening key (the desk-sim S2 retroactive-"
                 "revision shape) — key-local drops more than root",
        "band": "the worst-drop pieces show a key-local drop at span 8 materially larger than the "
                "corpus mean; key-local is the more span-sensitive axis than root",
    },
    "cost_grows_with_span": {
        "claim": "Python-reference decode wall time grows with span (roughly linear-to-superlinear in "
                 "measures), so a bounded window is far cheaper to decode COLD than the whole piece",
        "band": "mean decode seconds monotone non-decreasing in span; mean@8 < mean@whole",
    },
}


def _git_head() -> str:
    return subprocess.run(["git", "-C", str(_ROOT), "rev-parse", "HEAD"],
                          capture_output=True, text=True).stdout.strip()


# ══════════════════════════════════════════════════════════════════════════════
# Content-score memo (a correctness-preserving speedup — overlapping windows of ONE piece
# re-score the SAME absolute spans). score_segment_content is a PURE function of the segment's
# own absolute notes (onset-in-segment notes + per-event covariates, all determined by the absolute
# event range) plus the overlap pcs (seg_pcs — the only window-dependent input, captured in the key)
# plus the (key, class). So a memo keyed by (stem, abs_start, abs_end, tonic, is_major, class-tuple,
# frozenset(seg_pcs)) returns the identical value. NOT assumed — ESTABLISHED (#19) by establish_memo()
# below (memo-ON == memo-OFF decode, byte-identical segments) AND self-checked per piece by the
# whole-piece parity establishment (which runs with the memo active).
# ══════════════════════════════════════════════════════════════════════════════

_ORIG_SSC = pd.score_segment_content
_CONTENT_MEMO = {}
_MEMO_ON = [True]


# The class objects come from vocab.classes and are held for the whole run (no GC), so id(cls) is a
# stable, fast (C-builtin) key — orders of magnitude cheaper than reading class attributes in the
# hot transition loop (called ~16M times per piece). Correctness is self-established: establish_memo
# compares memo-ON (id-keyed) to memo-OFF (bypassed) and STOPs on any byte-difference.
def _memo_ssc(piece, i, j, tonic, is_major, cls, adapter, cache, seg_pcs=None):
    if not _MEMO_ON[0]:
        return _ORIG_SSC(piece, i, j, tonic, is_major, cls, adapter, cache, seg_pcs=seg_pcs)
    if seg_pcs is None:
        seg_pcs = piece.overlap_pcs(i, j)
    a = piece.events[i][pd.EV_START]
    b = piece.events[j - 1][pd.EV_END]
    k = (a, b, tonic, is_major, id(cls), frozenset(seg_pcs))   # piece-scoped (memo cleared per stem)
    v = _CONTENT_MEMO.get(k)
    if v is None:
        v = _ORIG_SSC(piece, i, j, tonic, is_major, cls, adapter, cache, seg_pcs=seg_pcs)
        _CONTENT_MEMO[k] = v
    return v


pd.score_segment_content = _memo_ssc      # intercept decode_piece's inner content() global lookup

_MISS = object()


def install_transition_memos(adapter):
    """Memoize the adapter's DP transition factors — chord_trans_logp / key_trans_logp / entry_logp.
    Each is a PURE function of (class/key args, is_major) and PIECE-INDEPENDENT, so one memo serves the
    whole corpus (the DP calls them hundreds of thousands of times per decode over a tiny domain). Gated
    by _MEMO_ON so the establish_memo() on/off check covers them too. A correctness-preserving speedup,
    established (#19), not assumed."""
    ct, kt, en = adapter.chord_trans_logp, adapter.key_trans_logp, adapter.entry_logp
    m_ct, m_kt, m_en = {}, {}, {}

    def chord_trans_logp(prev_cls, cur_cls, is_major):
        if not _MEMO_ON[0]:
            return ct(prev_cls, cur_cls, is_major)
        k = (id(prev_cls), id(cur_cls), is_major)
        v = m_ct.get(k, _MISS)
        if v is _MISS:
            v = ct(prev_cls, cur_cls, is_major); m_ct[k] = v
        return v

    def key_trans_logp(a, b):
        if not _MEMO_ON[0]:
            return kt(a, b)
        k = (a, b)
        v = m_kt.get(k, _MISS)
        if v is _MISS:
            v = kt(a, b); m_kt[k] = v
        return v

    def entry_logp(cls, is_major):
        if not _MEMO_ON[0]:
            return en(cls, is_major)
        k = (id(cls), is_major)
        v = m_en.get(k, _MISS)
        if v is _MISS:
            v = en(cls, is_major); m_en[k] = v
        return v

    adapter.chord_trans_logp = chord_trans_logp
    adapter.key_trans_logp = key_trans_logp
    adapter.entry_logp = entry_logp


# decode_piece computes a FULL per-segment 24-key posterior (report-only, AFTER the Viterbi backtrack —
# it does NOT affect the committed segments or total_score). This study needs the §3.3 key gap only for
# the QUERY segment, so we skip the full posterior and compute the gap on demand (gap_for_segment). This
# does not change the committed decode (establishment is byte-identical); it only drops report-only work.
_ORIG_POSTERIOR = pd._segment_posterior
pd._segment_posterior = lambda *a, **k: []


def gap_for_segment(sub, i, j, tonic, is_major, cls_key, adapter, vocab, cache):
    """The §3.3 group-(i) key gap for ONE segment (committed class fixed, re-scored under KEYS_24) — the
    SAME quantity decode_piece's _segment_posterior / gen_posterior_slice publish, computed for just the
    query segment. Reuses the content memo. Returns None if no alternate key scores."""
    cls = vocab.classes[cls_key]
    best = (tonic, is_major)
    best_sc, alt_sc = pd.NEG_INF, pd.NEG_INF
    for (t, m) in pd.KEYS_24:
        _mem, _fac, root = cache.get(cls, t, m)
        if root is None:
            continue
        sc = pd.score_segment_content(sub, i, j, t, m, cls, adapter, cache)
        if sc == pd.NEG_INF:
            continue
        if (t, m) == best:
            best_sc = sc
        elif sc > alt_sc:
            alt_sc = sc
    if best_sc == pd.NEG_INF or alt_sc == pd.NEG_INF:
        return None
    return best_sc - alt_sc


def establish_memo(pieces, adapter, vocab, cache, sample_stems):
    """(#19) Establish the content memo: for a sample of real windows, the memo-ON decode's committed
    segments + total_score must be BYTE-IDENTICAL to the memo-OFF decode's. A mismatch is a #13 STOP."""
    checks = []
    for stem in sample_stems:
        piece = pieces[stem]
        sig, dm = pd.piece_header(stem)
        N = len(piece.events)
        m_min, m_max = _measure_bounds(piece)
        downs = [e[pd.EV_MEAS] for e in piece.events if e[pd.EV_BEAT] == 1.0 and e[pd.EV_MEAS] >= m_min]
        centers = [downs[0], downs[len(downs) // 2], downs[-1]] if downs else []
        for m_c in centers:
            for span in (4, 8, 16):
                half = span // 2
                lo, hi = _event_range_for_measures(
                    piece, max(m_min, m_c - half), min(m_max, m_c + (span - 1 - half)))
                sub = piece if (lo == 0 and hi == N) else pd.sub_piece(piece, list(range(lo, hi)))
                _MEMO_ON[0] = True
                _CONTENT_MEMO.clear()
                a = SegLookup(pd.decode_piece(sub, adapter, vocab, cache, seg_cap=SEG_CAP,
                                              sig_fifths=sig, declared_mode=dm), sub)
                _MEMO_ON[0] = False
                b = SegLookup(pd.decode_piece(sub, adapter, vocab, cache, seg_cap=SEG_CAP,
                                              sig_fifths=sig, declared_mode=dm), sub)
                _MEMO_ON[0] = True
                ok = (a.seg_ijs == b.seg_ijs and abs(a.total_score - b.total_score) < 1e-9)
                checks.append(ok)
                if not ok:
                    return {"ok": False, "stem": stem, "m_c": m_c, "span": span,
                            "seg_match": a.seg_ijs == b.seg_ijs,
                            "score_on": a.total_score, "score_off": b.total_score}
    _CONTENT_MEMO.clear()
    return {"ok": True, "n_checks": len(checks)}


# ══════════════════════════════════════════════════════════════════════════════
# Decode + reading-at-tick
# ══════════════════════════════════════════════════════════════════════════════

class SegLookup:
    """The committed segments of one decode as a tick-indexed reading lookup. `sub` is the decoded
    (sub_)piece, kept so the §3.3 gap can be computed on demand for the query segment (local i/j)."""
    def __init__(self, result, sub=None):
        self.sub = sub
        self.starts = []
        self.rows = []          # (start_tick, end_tick, key, class_key, root_pc)
        self.seg_ijs = []       # (i, j, tonic_pc, is_major, class_key) — parity + on-demand gap
        for s in result.segments:
            self.starts.append(s["start_tick"])
            self.rows.append((s["start_tick"], s["end_tick"], s["key"], s["class_key"], s["root_pc"]))
            self.seg_ijs.append((s["i"], s["j"], s["tonic_pc"], s["is_major"], s["class_key"]))
        self.total_score = result.total_score
        self.decode_seconds = result.decode_seconds

    def at(self, tick):
        """The (key, class_key, root_pc, seg_index) reading whose committed segment contains `tick`."""
        idx = bisect_right(self.starts, tick) - 1
        if 0 <= idx < len(self.rows):
            s0, s1, key, ck, root = self.rows[idx]
            if s0 <= tick < s1:
                return (key, ck, root, idx)
        for i, (s0, s1, key, ck, root) in enumerate(self.rows):   # boundary guard
            if s0 <= tick < s1:
                return (key, ck, root, i)
        return None

    def gap_at(self, idx, adapter, vocab, cache):
        """The §3.3 group-(i) key gap of committed segment `idx` (on demand)."""
        if self.sub is None:
            return None
        i, j, tonic, is_major, ck = self.seg_ijs[idx]
        return gap_for_segment(self.sub, i, j, tonic, is_major, ck, adapter, vocab, cache)


def decode_events(piece, ev_lo, ev_hi, adapter, vocab, cache, sig, dm):
    """Decode the contiguous event range [ev_lo, ev_hi) as a sub_piece (or the whole piece if it is
    the full range). Returns a SegLookup. Absolute ticks are preserved by sub_piece."""
    if ev_lo == 0 and ev_hi == len(piece.events):
        sub = piece
    else:
        sub = pd.sub_piece(piece, list(range(ev_lo, ev_hi)))
    res = pd.decode_piece(sub, adapter, vocab, cache, seg_cap=SEG_CAP, sig_fifths=sig, declared_mode=dm)
    return SegLookup(res, sub)


# ══════════════════════════════════════════════════════════════════════════════
# Per-piece measurement
# ══════════════════════════════════════════════════════════════════════════════

def _measure_bounds(piece):
    meas = [e[pd.EV_MEAS] for e in piece.events]
    real = [m for m in meas if m >= 1]           # measure 0 is the anacrusis/pickup
    m_min = min(real) if real else min(meas)
    m_max = max(meas)
    return m_min, m_max


def _event_range_for_measures(piece, m_lo, m_hi):
    """The contiguous event index range [lo, hi) whose EV_MEAS lies in [m_lo, m_hi]."""
    lo = None
    hi = None
    for i, e in enumerate(piece.events):
        m = e[pd.EV_MEAS]
        if m_lo <= m <= m_hi:
            if lo is None:
                lo = i
            hi = i + 1
    return (lo, hi) if lo is not None else (0, len(piece.events))


def _anchor_regions(piece, whole_lookup):
    """compare_analyses.Region objects for the whole-piece committed segments (measure/beat/ticks),
    the anchor source _dcml_time_spans needs to align the WiR GT — exactly a8's alignment input."""
    regions = []
    ev = piece.events
    # map start_tick -> (measure, beat) via the event whose EV_START == the segment start
    start2mb = {}
    for e in ev:
        start2mb.setdefault(e[pd.EV_START], (e[pd.EV_MEAS], e[pd.EV_BEAT]))
    for (s0, s1, key, ck, root) in whole_lookup.rows:
        meas, beat = start2mb.get(s0, (0, 1.0))
        regions.append(cmp.Region(
            measure_number=meas, beat=float(beat), start_tick=s0, end_tick=s1,
            duration=max(1.0, (s1 - s0) / TPB), root_pc=root if root is not None else -1,
            quality="", chord_symbol="", roman_numeral="", key=key,
            key_confidence=0.0, diatonic_to_key=None))
    return regions


def measure_piece(stem, piece, adapter, vocab, cache, parity_sel):
    sig, dm = pd.piece_header(stem)
    N = len(piece.events)
    _CONTENT_MEMO.clear()          # the memo is keyed by stem; bound it to one piece at a time

    # whole-piece decode (cache anchor at (0, N)) + establishment vs the committed parity
    dcache = {}
    whole = decode_events(piece, 0, N, adapter, vocab, cache, sig, dm)
    dcache[(0, N)] = whole
    est = _establish_whole(piece, whole, parity_sel.get(stem))

    m_min, m_max = _measure_bounds(piece)

    # query points: downbeats (EV_BEAT==1.0) in real measures
    queries = []
    for e in piece.events:
        if e[pd.EV_BEAT] == 1.0 and e[pd.EV_MEAS] >= m_min:
            queries.append((e[pd.EV_START], e[pd.EV_MEAS]))
    queries.sort()
    q_ticks = [t for (t, _m) in queries]

    # per-query duration weight = interval to the next downbeat (last -> piece end)
    piece_end = max(e[pd.EV_END] for e in piece.events)
    weights = []
    for k, (t, _m) in enumerate(queries):
        nxt = q_ticks[k + 1] if k + 1 < len(q_ticks) else piece_end
        weights.append(max(1, nxt - t))

    # WiR ground-truth alignment (once per piece; identical for all spans)
    wir_regions = None
    dcml_spans = None
    try:
        if dcml.find_wir_file(str(WIR_DIR), stem):
            wir_regions = dcml.load_wir_regions(str(WIR_DIR), stem)
            if wir_regions:
                anchors = _anchor_regions(piece, whole)
                dcml_spans = cmp._dcml_time_spans(anchors, wir_regions)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"  [{stem}] WiR load failed ({type(exc).__name__}: {exc}); accuracy skipped", flush=True)

    def dcml_at(tick):
        if dcml_spans is None:
            return None
        di = crn._active_index_at(dcml_spans, tick)
        if di is None:
            return None
        return wir_regions[di]

    # decode each needed window (cached by contiguous event range)
    def lookup_for_span(span, m_c):
        if span == "whole":
            key = (0, N)
        else:
            half = span // 2
            m_lo = max(m_min, m_c - half)
            m_hi = min(m_max, m_c + (span - 1 - half))
            key = _event_range_for_measures(piece, m_lo, m_hi)
        sl = dcache.get(key)
        if sl is None:
            sl = decode_events(piece, key[0], key[1], adapter, vocab, cache, sig, dm)
            dcache[key] = sl
        return sl, key

    per_query = []
    for k, (t, m_c) in enumerate(queries):
        w_reading = whole.at(t)
        if w_reading is None:
            continue
        w_key, w_class, w_root, w_idx = w_reading
        w_gap = whole.gap_at(w_idx, adapter, vocab, cache)
        dr = dcml_at(t)
        dcml_root = dr.root_pc if dr is not None else None
        dcml_local = crn._dcml_key_tonic(getattr(dr, "local_key", None)) if dr is not None else (None, None)

        row = {"tick": t, "measure": m_c, "weight": weights[k],
               "whole_key": w_key, "whole_class": w_class, "whole_root": w_root, "whole_gap": w_gap,
               "spans": {}}
        for span in SPANS:
            sl, ekey = lookup_for_span(span, m_c)
            r = sl.at(t)
            if r is None:
                row["spans"][str(span)] = {"reading": None}
                continue
            s_key, s_class, s_root, s_idx = r
            s_gap = sl.gap_at(s_idx, adapter, vocab, cache)
            eq_whole = (s_key == w_key and s_class == w_class)
            clipped_to_whole = (ekey == (0, N))
            win_meas = (m_max - m_min + 1) if span == "whole" else min(
                m_max, m_c + (span - 1 - span // 2)) - max(m_min, m_c - span // 2) + 1
            entry = {"key": s_key, "class": s_class, "root": s_root, "gap": s_gap,
                     "eq_whole": eq_whole, "clipped_to_whole": clipped_to_whole,
                     "win_measures": win_meas}
            if span in ACC_SPANS and dcml_root is not None:
                entry["root_agree"] = bool(cmp.roots_agree(s_root, dcml_root))
                our_ident = crn._our_key_ident(s_key)
                entry["key_local_agree"] = bool(our_ident is not None and dcml_local[0] is not None
                                                and our_ident == dcml_local)
                entry["key_local_scoreable"] = bool(our_ident is not None and dcml_local[0] is not None)
            row["spans"][str(span)] = entry
        per_query.append(row)

    # per-piece cost: unique decodes by span-width class
    cost = defaultdict(list)
    # (recomputed at corpus level from dcache is not span-tagged; time is captured per SegLookup)
    return {
        "stem": stem, "n_events": N, "n_queries": len(per_query),
        "establishment": est, "has_dcml": dcml_spans is not None,
        "queries": per_query,
        "whole_decode_seconds": whole.decode_seconds,
        "n_unique_decodes": len(dcache),
    }


def _establish_whole(piece, whole, parity_stem):
    """The whole-piece decode must reproduce the committed parity (i,j,tonic,is_major,class_key) +
    total_score. Returns a dict; ok=False is a #13 STOP for the caller."""
    if parity_stem is None:
        return {"ok": None, "reason": "no parity entry (stem not in decode_parity_ref)"}
    got = list(whole.seg_ijs)
    exp = [(i, j, t, m, ck) for (i, j, t, m, ck, _root) in parity_stem["segments"]]
    seg_match = (got == exp)
    score_match = abs(whole.total_score - parity_stem["total_score"]) < 1e-6
    return {"ok": bool(seg_match and score_match), "seg_match": seg_match,
            "score_match": score_match, "n_seg_got": len(got), "n_seg_exp": len(exp),
            "score_got": whole.total_score, "score_exp": parity_stem["total_score"]}


# ══════════════════════════════════════════════════════════════════════════════
# Corpus aggregation
# ══════════════════════════════════════════════════════════════════════════════

def aggregate(piece_results):
    span_keys = [str(s) for s in SPANS]
    stab_count = {s: [0, 0] for s in span_keys}          # [equal, total]
    stab_dur = {s: [0, 0] for s in span_keys}            # [equal_w, total_w]
    smallest_stable = Counter()                          # width bucket -> count
    needs_whole = [0, 0]                                 # [needs_whole, total]
    acc = {str(s): {"root": [0, 0], "keyloc": [0, 0]} for s in ACC_SPANS}
    per_piece_acc = defaultdict(lambda: {str(s): {"root": [0, 0], "keyloc": [0, 0]} for s in ACC_SPANS})
    gap_stable = []                                       # (whole_gap, became_stable_width)

    for pr in piece_results:
        stem = pr["stem"]
        m_range = None
        for row in pr["queries"]:
            w = row["weight"]
            # stability per span
            for s in span_keys:
                e = row["spans"].get(s)
                if not e or "eq_whole" not in e:      # {"reading": None} entries have no eq_whole
                    continue
                stab_count[s][1] += 1
                stab_dur[s][1] += w
                if e["eq_whole"]:
                    stab_count[s][0] += 1
                    stab_dur[s][0] += w
            # smallest-stable span: largest span index that DIFFERS, +1
            last_diff = -1
            widths = {}
            for idx, s in enumerate(span_keys):
                e = row["spans"].get(s)
                if e and "eq_whole" in e:
                    widths[idx] = e.get("win_measures")
                    if not e["eq_whole"]:
                        last_diff = idx
            stable_idx = last_diff + 1
            if stable_idx < len(span_keys):
                width = widths.get(stable_idx)
                bucket = str(SPANS[stable_idx]) if SPANS[stable_idx] == "whole" else _width_bucket(width)
                smallest_stable[bucket] += 1
                needs_whole[1] += 1
                e_stab = row["spans"].get(span_keys[stable_idx])
                if e_stab and e_stab.get("clipped_to_whole"):
                    needs_whole[0] += 1
                if row.get("whole_gap") is not None:
                    gap_stable.append((row["whole_gap"], width if width else 0))
            # accuracy per span
            for s in [str(x) for x in ACC_SPANS]:
                e = row["spans"].get(s)
                if not e or "root_agree" not in e:
                    continue
                acc[s]["root"][1] += 1
                per_piece_acc[stem][s]["root"][1] += 1
                if e["root_agree"]:
                    acc[s]["root"][0] += 1
                    per_piece_acc[stem][s]["root"][0] += 1
                if e.get("key_local_scoreable"):
                    acc[s]["keyloc"][1] += 1
                    per_piece_acc[stem][s]["keyloc"][1] += 1
                    if e["key_local_agree"]:
                        acc[s]["keyloc"][0] += 1
                        per_piece_acc[stem][s]["keyloc"][0] += 1

    def frac(pair):
        return (pair[0] / pair[1]) if pair[1] else None

    stability = {s: {"count_fraction": frac(stab_count[s]), "n": stab_count[s][1],
                     "duration_fraction": frac(stab_dur[s]), "dur_total": stab_dur[s][1]}
                 for s in span_keys}
    accuracy = {}
    whole_root = frac(acc["whole"]["root"])
    whole_keyloc = frac(acc["whole"]["keyloc"])
    for s in [str(x) for x in ACC_SPANS]:
        r = frac(acc[s]["root"])
        kl = frac(acc[s]["keyloc"])
        accuracy[s] = {
            "root_agree": r, "n_root": acc[s]["root"][1],
            "key_local_agree": kl, "n_keyloc": acc[s]["keyloc"][1],
            "root_delta_vs_whole": (None if r is None or whole_root is None else round(whole_root - r, 5)),
            "key_local_delta_vs_whole": (None if kl is None or whole_keyloc is None else round(whole_keyloc - kl, 5)),
        }

    # worst pieces: largest key-local drop at span 8 vs whole (>= a few scored queries)
    worst = []
    for stem, d in per_piece_acc.items():
        r8 = _fr(d["8"]["root"]); rw = _fr(d["whole"]["root"])
        k8 = _fr(d["8"]["keyloc"]); kw = _fr(d["whole"]["keyloc"])
        n = d["8"]["keyloc"][1]
        if n >= 4 and k8 is not None and kw is not None:
            worst.append({"stem": stem, "n_scored": n,
                          "key_local_drop_8": round(kw - k8, 4),
                          "root_drop_8": (None if r8 is None or rw is None else round(rw - r8, 4)),
                          "key_local_8": round(k8, 4), "key_local_whole": round(kw, 4)})
    worst.sort(key=lambda x: (x["key_local_drop_8"] if x["key_local_drop_8"] is not None else 0), reverse=True)

    return {
        "stability": stability,
        "smallest_stable_span_distribution": dict(smallest_stable),
        "needs_whole_piece_fraction": frac(needs_whole), "n_smallest_stable": needs_whole[1],
        "accuracy": accuracy,
        "worst_key_local_drop_pieces_span8": worst[:15],
        "n_queries_total": sum(pr["n_queries"] for pr in piece_results),
    }


def _fr(pair):
    return (pair[0] / pair[1]) if pair[1] else None


def _width_bucket(width):
    if width is None:
        return "unknown"
    for b in (4, 8, 16, 32, 64):
        if width <= b:
            return f"<={b}"
    return ">64"


# ══════════════════════════════════════════════════════════════════════════════
# Cost curve (a small dedicated timing pass, isolated from the caching above)
# ══════════════════════════════════════════════════════════════════════════════

def cost_curve(piece_results, pieces, adapter, vocab, cache):
    """Time one COLD decode per (piece, span) at the piece's MIDDLE downbeat — a clean per-span cost
    sample uncontaminated by cross-query cache reuse. Reports mean/median decode seconds per span.
    The memo is DISABLED here: cost is the PRODUCTION decoder's cost (which has no content memo), so
    the curve is the honest cold decode cost, not the memo-accelerated one."""
    import statistics
    saved = _MEMO_ON[0]
    _MEMO_ON[0] = False
    by_span = defaultdict(list)
    for pr in piece_results:
        stem = pr["stem"]
        piece = pieces[stem]
        sig, dm = pd.piece_header(stem)
        N = len(piece.events)
        m_min, m_max = _measure_bounds(piece)
        downbeats = [e[pd.EV_MEAS] for e in piece.events if e[pd.EV_BEAT] == 1.0 and e[pd.EV_MEAS] >= m_min]
        if not downbeats:
            continue
        m_c = downbeats[len(downbeats) // 2]
        for span in SPANS:
            if span == "whole":
                lo, hi = 0, N
            else:
                half = span // 2
                m_lo = max(m_min, m_c - half)
                m_hi = min(m_max, m_c + (span - 1 - half))
                lo, hi = _event_range_for_measures(piece, m_lo, m_hi)
            sub = piece if (lo == 0 and hi == N) else pd.sub_piece(piece, list(range(lo, hi)))
            t0 = time.perf_counter()
            pd.decode_piece(sub, adapter, vocab, cache, seg_cap=SEG_CAP, sig_fifths=sig, declared_mode=dm)
            by_span[str(span)].append((time.perf_counter() - t0, hi - lo))
    _MEMO_ON[0] = saved
    out = {}
    for s in [str(x) for x in SPANS]:
        vals = [v for (v, _n) in by_span.get(s, [])]
        evs = [n for (_v, n) in by_span.get(s, [])]
        if vals:
            out[s] = {"mean_seconds": round(statistics.mean(vals), 5),
                      "median_seconds": round(statistics.median(vals), 5),
                      "max_seconds": round(max(vals), 5),
                      "mean_events": round(statistics.mean(evs), 1), "n": len(vals)}
    return out


# ══════════════════════════════════════════════════════════════════════════════
# Prediction check
# ══════════════════════════════════════════════════════════════════════════════

def check_predictions(agg, cost):
    st = agg["stability"]
    acc = agg["accuracy"]
    res = {}

    def cf(s):
        return st[str(s)]["count_fraction"]

    seq = [cf(s) for s in [4, 8, 16, 32, 64]]
    res["stability_rises_monotonically_with_span"] = {
        "measured": seq, "hit": all(a is not None and b is not None and b >= a - 1e-9
                                    for a, b in zip(seq, seq[1:]))}
    nb = agg["needs_whole_piece_fraction"]
    bounded_frac = None if nb is None else (1.0 - nb)
    res["most_queries_stable_below_whole"] = {
        "bounded_stable_fraction": bounded_frac,
        "hit": bounded_frac is not None and bounded_frac >= 0.60}
    res["stability_fraction_at_small_spans"] = {
        "stability_8": cf(8), "stability_16": cf(16),
        "hit": cf(8) is not None and cf(16) is not None and cf(8) >= 0.75 and cf(16) >= 0.88}
    rd16 = acc["16"]["root_delta_vs_whole"]
    kd16 = acc["16"]["key_local_delta_vs_whole"]
    res["accuracy_cost_of_bounding_is_small_but_nonzero"] = {
        "root_delta_16": rd16, "key_local_delta_16": kd16,
        "hit": rd16 is not None and kd16 is not None and -0.01 <= rd16 <= 0.05 and -0.01 <= kd16 <= 0.06}
    kd8 = acc["8"]["key_local_delta_vs_whole"]
    rd8 = acc["8"]["root_delta_vs_whole"]
    res["accuracy_sensitive_class"] = {
        "key_local_delta_8": kd8, "root_delta_8": rd8,
        "key_local_more_sensitive_than_root": (kd8 is not None and rd8 is not None and kd8 >= rd8),
        "hit": kd8 is not None and rd8 is not None and kd8 >= rd8 and len(agg["worst_key_local_drop_pieces_span8"]) > 0}
    means = [cost.get(str(s), {}).get("mean_seconds") for s in SPANS]
    mono = all(a is not None and b is not None and b >= a - 1e-9 for a, b in zip(means, means[1:]))
    m8 = cost.get("8", {}).get("mean_seconds")
    mw = cost.get("whole", {}).get("mean_seconds")
    res["cost_grows_with_span"] = {
        "means": means, "hit": bool(mono and m8 is not None and mw is not None and m8 < mw)}
    return res


# ══════════════════════════════════════════════════════════════════════════════
# Run
# ══════════════════════════════════════════════════════════════════════════════

def run(stems, write, coverage="unspecified"):
    parity = json.loads((_HERE / "decode_parity_ref.json").read_text(encoding="utf-8"))
    sel_weights = parity["selected_weights"]
    parity_sel = parity["selected"]
    weight_identity = parity.get("provenance", {}).get("selected_start", "")

    pieces, prov = pd.load_pieces()
    adapter = pd.FittedAdapter(leftover_mode=LEFTOVER, table_set="all", weights=sel_weights)
    adapter.mode_marginal("major")
    install_transition_memos(adapter)      # piece-independent DP factor memos (gated by _MEMO_ON)
    vocab = pd.Vocabulary(adapter.tables)
    cache = pd.ChordCache()

    # (#19) establish the content + transition memos before they are trusted (memo-ON == memo-OFF)
    memo_sample = [s for s in stems[:5]]
    memo_est = establish_memo(pieces, adapter, vocab, cache, memo_sample)
    if not memo_est.get("ok"):
        print(f"\nSTOP (#13): the content memo is NOT byte-identical to the unmemoized decode: {memo_est}",
              file=sys.stderr)
        return None, False
    print(f"content memo established ({memo_est['n_checks']} window checks, memo-ON==memo-OFF)", flush=True)

    piece_results = []
    stop_stems = []
    t0 = time.perf_counter()
    for idx, stem in enumerate(stems):
        pr = measure_piece(stem, pieces[stem], adapter, vocab, cache, parity_sel)
        est = pr["establishment"]
        if est.get("ok") is False:
            stop_stems.append((stem, est))
        piece_results.append(pr)
        if (idx + 1) % 10 == 0:
            print(f"  [{idx + 1}/{len(stems)}] {stem} ({time.perf_counter() - t0:.0f}s)", flush=True)

    if stop_stems:
        print("\nSTOP (#13): the whole-piece decode did NOT reproduce the committed parity on:",
              file=sys.stderr)
        for stem, est in stop_stems[:20]:
            print(f"  {stem}: {est}", file=sys.stderr)
        print("The window study is NOT trustworthy until the decode is the production decode.",
              file=sys.stderr)
        return None, False

    agg = aggregate(piece_results)
    cost_sample = piece_results if len(piece_results) <= 60 else piece_results[::max(1, len(piece_results) // 60)]
    print(f"\ntiming the cost curve ({len(cost_sample)} pieces x {len(SPANS)} spans, cold, memo OFF) ...",
          flush=True)
    cost = cost_curve(cost_sample, pieces, adapter, vocab, cache)
    pred = check_predictions(agg, cost)

    n_dcml = sum(1 for pr in piece_results if pr["has_dcml"])
    art = {
        "provenance": {
            "generator": "tools/joint_estimator/gen_window_study.py",
            "instrument_commit": _git_head(),
            "open_item": "OI-206 (Task 2) / transfers docs/p3_granularity_ab_3_1b.md to the joint estimator",
            "decoder": "tools/joint_estimator/probe_decoder.py (pinned; import-only)",
            "grading_substrate": "compare_analyses (_dcml_time_spans, roots_agree) + compare_rn "
                                 "(_our_key_ident, _dcml_key_tonic) + dcml_parser (load_wir_regions) — import-only",
            "note_events_git_hash": prov.get("corpus_git_hash"),
            "config": {"seg_cap": SEG_CAP, "leftover_rule": f"option 2a ({LEFTOVER})",
                       "table_set": "all", "weight_arm": "selected", "weight_identity": weight_identity,
                       "spans_measures": SPANS, "accuracy_spans": ACC_SPANS,
                       "query_sample": "every downbeat (EV_BEAT==1.0, real measures)",
                       "ticks_per_beat": TPB},
            "window_construction": ("span S measures centered on the query measure m_c: "
                                    "[m_c - S//2, m_c + (S-1-S//2)] clipped to the piece measure range; "
                                    "the window is every event in that measure range; sub_piece preserves "
                                    "absolute ticks. Nested by construction; 'whole' == all events."),
            "dcml_alignment": ("WiR (When-in-Rome) GT; ticks aligned exactly as a8_rebaseline_measure "
                               "via compare_analyses._dcml_time_spans over the whole-piece anchor regions, "
                               "computed ONCE per piece and reused for every span (so the windowed-vs-whole "
                               "accuracy DELTA is convention-robust). ROOT: compare_analyses.roots_agree; "
                               "KEY-LOCAL: compare_rn._our_key_ident vs compare_rn._dcml_key_tonic(local_key)."),
            "cost_caveat": ("cost_curve is the PYTHON reference decoder's wall time (decode_piece, with the "
                            "report-only 24-key posterior skipped as the study runs it, and the memos OFF); "
                            "it gives the SHAPE of cost-vs-span, NOT the C++ producer latency. The absolute "
                            "interactive latency is tools/notation_seams/noteseam_latency.json (OI-203); "
                            "the two are never conflated (#19)."),
            "establishment": ("the whole-piece decode reproduces decode_parity_ref.json's committed "
                              "'selected' segments (i,j,tonic,is_major,class_key) + total_score per stem "
                              "(a mismatch is a #13 STOP; the run refuses to publish). Windowed decodes "
                              "reuse the identical decode_piece on sub_pieces."),
            "content_memo": ("correctness-preserving speedups: (1) score_segment_content memoized by "
                             "(stem, abs_start, abs_end, tonic, is_major, class-tuple, frozenset(seg_pcs)) "
                             "so overlapping windows of one piece re-use identical content scores; (2) the "
                             "DP transition factors chord_trans_logp/key_trans_logp/entry_logp memoized "
                             "(pure, piece-independent). BOTH ESTABLISHED (#19) memo-ON == memo-OFF "
                             "byte-identical on sample windows; the cost_curve times with the memos OFF "
                             "(the production decoder has no such memo)."),
            "content_memo_established": memo_est,
            "cost_curve_sample": f"{len(cost_sample)} of {len(piece_results)} pieces (evenly strided; cost is the SHAPE)",
            "coverage": coverage,
            "n_pieces": len(stems), "n_pieces_with_dcml": n_dcml,
            "predictions_recorded_before_measuring": PREDICTIONS,
        },
        "aggregate": agg,
        "cost_curve": cost,
        "prediction_vs_measured": pred,
        "pieces": {pr["stem"]: {k: v for k, v in pr.items() if k != "queries"} for pr in piece_results},
    }
    if write:
        # full per-query detail is large; keep it in a sibling for drill-down, keep the headline lean
        detail = {"pieces": {pr["stem"]: pr["queries"] for pr in piece_results}}
        (_HERE / "window_study_detail.json").write_text(json.dumps(detail) + "\n",
                                                        encoding="utf-8", newline="\n")
        ART_PATH.write_text(json.dumps(art, indent=1) + "\n", encoding="utf-8", newline="\n")

    _print_summary(art, pred)
    if write:
        print(f"\nwrote {ART_PATH} + window_study_detail.json ({len(stems)} pieces, {n_dcml} with DCML)")
    else:
        print(f"\n[dry-run] nothing written ({len(stems)} pieces).")
    return art, True


def _print_summary(art, pred):
    agg = art["aggregate"]
    prov = art["provenance"]
    print(f"\n── COVERAGE ──\n  {prov['coverage']}\n  n_pieces={prov['n_pieces']} "
          f"with_dcml={prov['n_pieces_with_dcml']} n_queries={agg['n_queries_total']}")
    print("\n── STABILITY (reading == whole-piece reading) ──")
    for s in [str(x) for x in SPANS]:
        st = agg["stability"][s]
        cf = st["count_fraction"]
        du = st["duration_fraction"]
        print(f"  span {s:>5}: count {cf if cf is None else round(cf,4)}  dur {du if du is None else round(du,4)}  (n={st['n']})")
    nb = agg["needs_whole_piece_fraction"]
    print(f"  smallest-stable-span dist: {agg['smallest_stable_span_distribution']}")
    print(f"  needs-whole-piece fraction: {None if nb is None else round(nb,4)}  "
          f"(bounded-stable {None if nb is None else round(1-nb,4)})")
    print("\n── ACCURACY vs DCML (root / key-local; delta = whole - windowed) ──")
    for s in [str(x) for x in ACC_SPANS]:
        a = agg["accuracy"][s]
        print(f"  span {s:>5}: root {a['root_agree'] if a['root_agree'] is None else round(a['root_agree'],4)} "
              f"(d {a['root_delta_vs_whole']})   key-local {a['key_local_agree'] if a['key_local_agree'] is None else round(a['key_local_agree'],4)} "
              f"(d {a['key_local_delta_vs_whole']})  n={a['n_root']}")
    print("  worst key-local drop @span8 (top 5):")
    for w in agg["worst_key_local_drop_pieces_span8"][:5]:
        print(f"    {w['stem']}: drop {w['key_local_drop_8']} (8={w['key_local_8']} whole={w['key_local_whole']}, n={w['n_scored']})")
    print("\n── COST (python reference decode seconds per span, cold) ──")
    for s in [str(x) for x in SPANS]:
        c = art["cost_curve"].get(s)
        if c:
            print(f"  span {s:>5}: mean {c['mean_seconds']}s  median {c['median_seconds']}s  "
                  f"max {c['max_seconds']}s  (~{c['mean_events']} events, n={c['n']})")
    print("\n── PREDICTION vs MEASURED ──")
    for k, v in pred.items():
        print(f"  [{'HIT ' if v.get('hit') else 'MISS'}] {k}: "
              + ", ".join(f"{kk}={vv}" for kk, vv in v.items() if kk != 'hit'))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stems", nargs="*", default=None, help="subset (dry-run: measure only, no write)")
    ap.add_argument("--limit", type=int, default=None, help="first N pieces (writes)")
    ap.add_argument("--stride", type=int, default=None,
                    help="declared corpus-representative sample: every Nth name-sorted piece (writes)")
    args = ap.parse_args()

    all_stems = sorted(pd.load_pieces()[0])
    if args.stems:
        stems = [s for s in args.stems if s in set(all_stems)]
        write = False
        coverage = f"explicit subset of {len(stems)} stem(s) (dry-run)"
    elif args.stride:
        stems = all_stems[::args.stride]
        write = True
        coverage = (f"DECLARED corpus-representative sample: every {args.stride}th name-sorted piece "
                    f"= {len(stems)} of {len(all_stems)} covered pieces (the corpus is a homogeneous "
                    f"Bach-chorale set, so a name stride spans the size range evenly). Every downbeat in "
                    f"each sampled piece is queried. Chosen for tractability of the pure-Python reference "
                    f"decode (~20-30 s/piece x 326 ~ 2-3 h full); the FULL-corpus run is a mechanical "
                    f"extension of this same instrument with no --stride (no code change).")
    elif args.limit:
        stems = all_stems[:args.limit]
        write = True
        coverage = f"first {len(stems)} of {len(all_stems)} name-sorted pieces"
    else:
        stems = all_stems
        write = True
        coverage = f"FULL corpus: all {len(all_stems)} covered pieces, every downbeat"

    print(f"window study on {len(stems)} piece(s)"
          + (" [dry-run subset]" if not write else "") + " ...", flush=True)
    _art, ok = run(stems, write, coverage)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
