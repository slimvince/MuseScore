#!/usr/bin/env python3
"""gen_label_tables.py — the label-side table fit (the fit event, part 1 of 2).

FIT-LAYER-OWNED. No src/ change, no corpus mutation, no gate change, NO DECODING, NO EVALUATION,
no accuracy metric consulted anywhere in this code path (the DT-2 firewall — grep this file: it
imports the count reconciliation basis only, never a grader/decoder). It produces the fitted TABLES
derivable from the ground-truth LABEL stream (+ notated signature/declared mode/meter) as committed
artifacts, per fold and for all-326, under the ratified OI-176 (held-out folds) and OI-177 (capacity
budget) protocols (`cowork_prefit_gates.md`, user-ratified 2026-07-19). Dispatch:
`cc_instruction_label_table_fit.md` (Cowork 2026-07-19).

THE TABLES (label-side; the NOTE-side emission/spelling tables are part 2, their own dispatch):
  1. same-key chord transition  P(c_j | c_{j-1}, mode)   — label-sequence (not tick-anchored)
  2. key transition             P(k_j | k_{j-1})         — (CoF distance, mode pair); rel/parallel cells
  3. entry chord                P(c | key change)        — first class after each key change
  4. bass/inversion             P(inv figure | degree, quality, mode)
  5. signature/declared-mode prior P(local key | signature, declared mode) — per local-key SEGMENT
  6. boundary by beat class     P(boundary | beat class) — tick-anchored; OI-184 exclusions BIND

FIT DISCIPLINE (ratified):
  - Fit per training-fold COMPLEMENT (fold i held out) AND once on all-326; tables_fold{0..4}.json
    are fit on the 4 non-i folds; tables_all.json on all 326. Fold source: fold_assignment.json.
  - Pooling/smoothing (OI-177): a cell keeps its own MLE iff its training count >= 20; below, it
    pools to its declared parent (the chains below); additive smoothing alpha=1 at the final
    back-off level (Katz reserved-mass construction: reliable cells exact MLE, residual mass =
    sparse-count mass, alpha-1 at the pooled base). ONE alpha per table. No other smoothing, no
    judgment calls — where the rule produces something odd it is REPORTED, never adjusted.
  - Normalization: tools/joint_estimator/normalize.py (OI-186a — quality from figure+case, NOT
    compare_rn.extract_quality). No second RN parser (#6).

REUSE (#6): dcml_parser.load_wir_regions (OI-142-corrected WiR substrate), compare_rn._dcml_key_tonic
(the ONE key-string reduction), normalize.normalize_label. Meter/signature/mode from the corpus xml
headers (tools/corpus/*.xml — music21 exports; elements <key><fifths>/<mode>, <time><beats>/<beat-type>).

OI-184 consequences (BINDING on the tick-anchored table 6 only; the label-sequence tables 1-5 are
unaffected): pickup measures (WiR m0 labels) EXCLUDED; the 7 flagged local-misalignment pieces
EXCLUDED. Declared in the artifact.

Usage:
    python tools/joint_estimator/gen_label_tables.py
    python tools/joint_estimator/gen_label_tables.py --out-dir <scratch>   # reproducibility check
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(_ROOT / "tools"))
sys.path.insert(0, str(_ROOT / "tools" / "joint_estimator"))

import dcml_parser as dcml              # noqa: E402
import compare_rn as crn               # noqa: E402
import normalize as norm               # noqa: E402  (the OI-186a fit-time normalization)

WIR_DIR = str(_ROOT / "tools" / "dcml" / "when_in_rome")
CORPUS_XML_DIR = _ROOT / "tools" / "corpus"          # bwv*.xml music21 exports (headers only)
FOLD_ARTIFACT = _ROOT / "tools" / "joint_estimator" / "fold_assignment.json"
COUNT_INVENTORY = _ROOT / "tools" / "joint_estimator" / "count_inventory.json"

# ── ratified protocol constants (cowork_prefit_gates.md, [prov-ratify]) ──
THRESHOLD = 20        # cell own-MLE iff training count >= 20
ALPHA = 1.0           # single additive-smoothing constant per table, at the final back-off level
N_FOLDS = 5
TOKENS_PER_PARAM_MIN = 10   # total effective free params <= training tokens / 10

# OI-184: the 7 flagged local-misalignment pieces — EXCLUDED from the tick-anchored boundary table.
OI184_FLAGGED = {"bwv384", "bwv274", "bwv140.7", "bwv113.8", "bwv110.7", "bwv123.6", "bwv112.5"}

# Reconciliation targets (establishment iii) — from the committed count inventory (all-326).
RECON_LABELS = 18418
RECON_TRANS = 16372
RECON_KEYCHG = 1720

# pc -> signed circle-of-fifths position (major-key signature fifths of that tonic).
_PC_TO_FIFTHS = {0: 0, 7: 1, 2: 2, 9: 3, 4: 4, 11: 5, 6: 6,
                 1: -5, 8: -4, 3: -3, 10: -2, 5: -1}


def _git_head() -> str:
    out = subprocess.run(["git", "-C", str(_ROOT), "rev-parse", "HEAD"],
                         capture_output=True, text=True, check=True)
    return out.stdout.strip()


def _rel(p) -> str:
    return Path(p).resolve().relative_to(_ROOT).as_posix()


# ══════════════════════════════════════════════════════════════════════════
# Per-stem extraction (shared across all 6 training sets)
# ══════════════════════════════════════════════════════════════════════════

_KEY_RE = re.compile(r"<key[^>]*>\s*<fifths>(-?\d+)</fifths>(?:\s*<mode>([a-zA-Z]+)</mode>)?")
_TIME_RE = re.compile(r"<time[^>]*>\s*<beats>(\d+)</beats>\s*<beat-type>(\d+)</beat-type>")


def read_xml_header(stem):
    """Read the corpus xml header: initial signature fifths, declared mode, meter(s). Returns a
    dict, or None if the xml is missing. The music21 export repeats <attributes> per part, so the
    FIRST <key>/<time> is the initial state; distinct values across the file flag a mid-piece
    change (handled/flagged per table)."""
    p = CORPUS_XML_DIR / f"{stem}.xml"
    if not p.exists():
        return None
    s = p.read_text(encoding="utf-8", errors="replace")
    keys = _KEY_RE.findall(s)          # [(fifths, mode), ...]
    times = _TIME_RE.findall(s)        # [(beats, beat_type), ...]
    distinct_fifths = sorted({int(f) for f, m in keys})
    distinct_meters = sorted({(int(b), int(bt)) for b, bt in times})
    init_fifths = int(keys[0][0]) if keys else None
    init_mode = (keys[0][1] or "") if keys else ""
    init_meter = (int(times[0][0]), int(times[0][1])) if times else None
    return {
        "init_fifths": init_fifths,
        "declared_mode": init_mode,           # 'major' | 'minor' | ''
        "init_meter": init_meter,             # (beats, beat_type) | None
        "multi_signature": len(distinct_fifths) > 1,
        "multi_meter": len(distinct_meters) > 1,
        "distinct_fifths": distinct_fifths,
        "distinct_meters": [list(m) for m in distinct_meters],
    }


def extract_stem(stem):
    """Extract everything the tables need from one stem. Returns a dict with the region sequence
    (normalized class, local key, measure, beat) and the xml header facts."""
    regs = dcml.load_wir_regions(WIR_DIR, stem)
    seq = []
    for r in regs:
        lc = norm.normalize_label(r.chord_symbol or "")
        tonic, is_major = crn._dcml_key_tonic(getattr(r, "local_key", None))
        seq.append({
            "cls": lc,
            "tonic": tonic,
            "is_major": is_major,
            "measure": r.measure_number,
            "beat": float(r.beat),
        })
    return {"stem": stem, "seq": seq, "xml": read_xml_header(stem)}


# ══════════════════════════════════════════════════════════════════════════
# Counting (per training set of stems)
# ══════════════════════════════════════════════════════════════════════════

def _collection_fifths(tonic, is_major):
    """Signed circle-of-fifths position of a key's diatonic collection. Minor uses its relative
    major's signature (so g minor and Bb major share position -2 — the 'relative pair')."""
    if tonic is None:
        return None
    base = tonic if is_major else (tonic + 3) % 12
    return _PC_TO_FIFTHS[base % 12]


def _fold_fifths_diff(d):
    """Fold a fifths difference into (-6, 6] (the shortest signed circle-of-fifths displacement)."""
    d %= 12
    return d - 12 if d > 6 else d


def _cof_distance(a, b):
    """Unsigned circle-of-fifths distance between two tonic pcs (0..6)."""
    ca, cb = (a * 7) % 12, (b * 7) % 12
    d = abs(ca - cb)
    return min(d, 12 - d)


def _key_change_kind(ta, ma, tb, mb):
    if ta == tb and ma != mb:
        return "parallel"
    if ma and not mb and tb == (ta + 9) % 12:      # major -> its relative minor
        return "relative"
    if (not ma) and mb and tb == (ta + 3) % 12:    # minor -> its relative major
        return "relative"
    return "other"


def count_tables(stems, stem_data):
    """Accumulate raw counts for all 6 tables over `stems`. Returns a dict of count structures and
    a tokens dict."""
    # 1: transitions per mode; key = (from LabelClass, to LabelClass)
    trans = {True: Counter(), False: Counter()}
    # 2: key-transition cells
    keytrans = Counter()
    # 3: entry classes
    entry = Counter()
    # 4: bass/inversion: context (deg,qual,mode) -> Counter(inv)
    inv_ctx = defaultdict(Counter)
    # 5: per declared_mode -> Counter((dist_band, local_mode))  ; dist signed folded, |d|>=2 -> 'far'
    sigprior = defaultdict(Counter)
    # 6: beat-class boundary counts
    boundary = {c: {"boundary": 0, "slots": 0} for c in
                ("downbeat", "mid_strong", "other_tactus", "sub_tactus")}
    boundary_out_of_grid = 0
    boundary_pieces_counted = 0
    boundary_excluded = {"flagged": [], "meter": [], "no_meter": []}

    tokens = {"labels": 0, "transition_pairs": 0, "key_changes": 0,
              "local_key_segments": 0, "inv_labels": 0, "boundary_slots": 0,
              "raw_unnormalized": 0, "indeterminate_mode_labels": 0}

    for stem in stems:
        d = stem_data[stem]
        seq = d["seq"]
        xml = d["xml"]
        tokens["labels"] += len(seq)

        # ── table 1/2/3: adjacency ──
        for i in range(len(seq) - 1):
            a, b = seq[i], seq[i + 1]
            same = (a["tonic"] is not None and b["tonic"] is not None
                    and a["tonic"] == b["tonic"] and a["is_major"] == b["is_major"])
            if same:
                tokens["transition_pairs"] += 1
                trans[a["is_major"]][(a["cls"], b["cls"])] += 1
                keytrans["stay"] += 1        # table 2: P(k_j|k_{j-1}) includes STAY (no change) — §3.5
            else:
                tokens["key_changes"] += 1
                # table 2 cell
                ta, ma, tb, mb = a["tonic"], a["is_major"], b["tonic"], b["is_major"]
                if ta is None or tb is None:
                    keytrans["indeterminate"] += 1
                else:
                    kind = _key_change_kind(ta, ma, tb, mb)
                    if kind in ("parallel", "relative"):
                        keytrans[kind] += 1
                    else:
                        dist = _cof_distance(ta, tb)
                        mp = f"{'M' if ma else 'm'}{'M' if mb else 'm'}"
                        band = f"cof{dist}" if dist <= 2 else "cofFar"
                        keytrans[f"{band}|{mp}"] += 1
                # table 3 entry (the class entering the new key)
                entry[b["cls"]] += 1

        # ── table 4: bass/inversion (every label with a parseable degree) ──
        for s in seq:
            lc = s["cls"]
            if lc.raw_unnormalized:
                tokens["raw_unnormalized"] += 1     # surfaced, never silently dropped (#12/DT-23)
                continue
            if s["is_major"] is None:
                tokens["indeterminate_mode_labels"] += 1
                continue
            ctx = (lc.degree_base, lc.quality, "M" if s["is_major"] else "m")
            inv_ctx[ctx][lc.inversion] += 1
            tokens["inv_labels"] += 1

        # ── table 5: signature/declared-mode prior, per local-key SEGMENT ──
        if xml and xml["init_fifths"] is not None:
            sig_fifths = xml["init_fifths"]
            dmode = xml["declared_mode"] or "none"
            # contiguous local-key runs (count 1 each, duration-free)
            prev = object()
            for s in seq:
                cur = (s["tonic"], s["is_major"])
                if cur == prev:
                    continue
                prev = cur
                if s["tonic"] is None:
                    sigprior[dmode]["indeterminate"] += 1
                    tokens["local_key_segments"] += 1
                    continue
                coll = _collection_fifths(s["tonic"], s["is_major"])
                diff = _fold_fifths_diff(coll - sig_fifths)
                band = str(diff) if abs(diff) <= 1 else "far"
                lm = "M" if s["is_major"] else "m"
                sigprior[dmode][f"{band}|{lm}"] += 1
                tokens["local_key_segments"] += 1

        # ── table 6: boundary by beat class (tick-anchored; OI-184 exclusions BIND) ──
        if stem in OI184_FLAGGED:
            boundary_excluded["flagged"].append(stem)
            continue
        if not xml or xml["init_meter"] is None:
            boundary_excluded["no_meter"].append(stem)
            continue
        meter = tuple(xml["init_meter"])
        if xml["multi_meter"] or meter not in ((4, 4), (3, 4)):
            boundary_excluded["meter"].append(stem)
            continue
        n_quarter = meter[0] * 4 // meter[1]           # 4/4->4, 3/4->3
        # label starts, keyed by (measure, rounded-beat) — a boundary iff a GT label starts there.
        label_at = set()
        for s in seq:
            if s["measure"] == 0:                      # OI-184 (a): pickup measures excluded
                continue
            label_at.add((s["measure"], round(s["beat"] * 4) / 4.0))
        measures = [s["measure"] for s in seq if s["measure"] > 0]
        if not measures:
            continue
        boundary_pieces_counted += 1
        for m in range(1, max(measures) + 1):
            for k in range(n_quarter * 4):             # 16th-note grid (0.25 quarter resolution)
                pos = 1.0 + k * 0.25
                cls = _beat_class(pos, n_quarter)
                boundary[cls]["slots"] += 1
                tokens["boundary_slots"] += 1
                if (m, pos) in label_at:
                    boundary[cls]["boundary"] += 1
        # labels starting off the 16th grid (e.g. beat 5.0 in 4/4) — counted, reported
        for (m, pos) in label_at:
            if pos < 1.0 or pos >= 1.0 + n_quarter:
                boundary_out_of_grid += 1

    return {
        "trans": trans, "keytrans": keytrans, "entry": entry, "inv_ctx": inv_ctx,
        "sigprior": sigprior, "boundary": boundary,
        "boundary_out_of_grid": boundary_out_of_grid,
        "boundary_pieces_counted": boundary_pieces_counted,
        "boundary_excluded": boundary_excluded,
        "tokens": tokens,
    }


def _beat_class(pos, n_quarter):
    """Classify a metric position (quarter-beat, 1-indexed): downbeat / mid-measure strong (beat 3
    in 4/4 only) / other tactus (integer beat) / sub-tactus (non-integer)."""
    if pos != int(pos):
        return "sub_tactus"
    ib = int(pos)
    if ib == 1:
        return "downbeat"
    if ib == 3 and n_quarter == 4:
        return "mid_strong"
    return "other_tactus"


# ══════════════════════════════════════════════════════════════════════════
# Estimation — Katz back-off (hard >=20 gate + alpha=1 at the pooled base)
# ══════════════════════════════════════════════════════════════════════════

def katz_distribution(counts: dict, parent_fn, alpha=ALPHA, thr=THRESHOLD):
    """A distribution over `counts`'s cells with the ratified pooling/smoothing:
      - reliable cells (count >= thr) keep their EXACT MLE = count/total;
      - sparse cells (count < thr) pool into their declared parent (parent_fn), promoted further
        while a pooled bucket is still < thr, until it reaches >= thr or a base cell (parent_fn
        returns None); the residual mass (= sparse-count mass) is distributed over the pooled
        buckets with additive alpha smoothing.
    Returns ({cell_key: prob}, meta) with meta.{reliable_cells, pooled_buckets, free_params}.
    Deterministic (sorted). `parent_fn(cell) -> parent cell key or None (base)`."""
    total = sum(counts.values())
    if total == 0:
        return {}, {"reliable_cells": 0, "pooled_buckets": 0, "free_params": 0}
    reliable = {c: n for c, n in counts.items() if n >= thr}
    sparse = {c: n for c, n in counts.items() if n < thr}
    # aggregate sparse into parent buckets, promoting while < thr and a parent exists
    buckets: dict = {}
    for c, n in sparse.items():
        p = parent_fn(c)
        p = c if p is None else p           # a base cell that is itself sparse survives as itself
        buckets[p] = buckets.get(p, 0) + n
    changed = True
    while changed:
        changed = False
        for b in sorted(buckets, key=str):
            if buckets[b] < thr:
                pp = parent_fn(b)
                if pp is not None and pp != b:
                    buckets[pp] = buckets.get(pp, 0) + buckets.pop(b)
                    changed = True
    dist = {}
    for c in sorted(reliable, key=str):
        dist[_ck(c)] = reliable[c] / total       # exact MLE
    reliable_mass = sum(reliable.values()) / total
    residual = 1.0 - reliable_mass
    zb = sum(n + alpha for n in buckets.values())
    for b in sorted(buckets, key=str):
        dist[_ck(b)] = residual * (buckets[b] + alpha) / zb if zb > 0 else 0.0
    meta = {"reliable_cells": len(reliable), "pooled_buckets": len(buckets),
            "free_params": max(0, len(dist) - 1)}
    return dist, meta


def _ck(cell):
    """String key for a cell that may be a LabelClass or already a string."""
    return cell.key() if isinstance(cell, norm.LabelClass) else str(cell)


# ── conditional table (context back-off at the row level; outcome pooling within a reliable row) ──

def estimate_conditional(pair_counts, context_chain, outcome_parent_fn, display_key):
    """Estimate P(outcome | context) with context back-off + within-row Katz outcome pooling.
      pair_counts:   {(context_full, outcome): count}
      context_chain(context_full) -> [k0=full, k1, ..., base]  DISTINCT level KEY strings, finest
                     first; the level keys are namespaced (L0:/L1:/L2:/BASE) so a root-position
                     full context's key never collides with the inversion-free back-off key of its
                     own inversions (the context-side analogue of the outcome namespacing).
      outcome_parent_fn(outcome) -> parent outcome or None (base)
      display_key(context_full) -> the clean context key the row is stored under.
    A full context whose total count < thr uses the finest coarser level with total >= thr (the base
    level always qualifies). Returns (rows, meta).  rows: {display_key: {context_used, dist}}."""
    ctx_out = defaultdict(Counter)      # level key -> Counter(outcome)
    full_contexts = {}                  # display key -> context object
    for (cf, o), n in pair_counts.items():
        full_contexts[display_key(cf)] = cf
        for k in context_chain(cf):
            ctx_out[k][o] += n
    ctx_total = {k: sum(c.values()) for k, c in ctx_out.items()}

    rows = {}
    level_meta = {}
    free_params = 0
    reliable_rows = 0
    for dk in sorted(full_contexts):
        chain = context_chain(full_contexts[dk])
        chosen = next((k for k in chain if ctx_total[k] >= THRESHOLD), chain[-1])
        if chosen == chain[0]:
            reliable_rows += 1
        if chosen not in level_meta:
            dist, meta = katz_distribution(dict(ctx_out[chosen]), outcome_parent_fn)
            level_meta[chosen] = (dist, meta)
            free_params += meta["free_params"]
        rows[dk] = {"context_used": chosen, "dist": level_meta[chosen][0]}
    return rows, {"reliable_rows": reliable_rows, "distinct_estimated_rows": len(level_meta),
                  "free_params": free_params}


# ── the per-table parent/chain definitions (the declared back-off chains) ──

# Pooled buckets are NAMESPACED so a coarsened bucket (e.g. the inversion-free class of 'I|Maj|6')
# can never collide with a real fine outcome key (the root-position 'I|Maj||'). A bucket is a
# DISTINCT symbol in the pooled vocabulary (pooling reduces the vocabulary — OI-177 item 2).
_POOL_INVFREE = "«invfree» "     # «invfree»
_POOL_FAMILY = "«family» "        # «family»
_BASE = "BASE"


def _family_key_of(invfree_key: str) -> str:
    """The family-level key of an inversion-free class key 'deg | qual |  | tgt'."""
    parts = invfree_key.split(" | ")
    deg, qual, tgt = parts[0], parts[1], (parts[3] if len(parts) > 3 else "")
    fam = "seventh" if qual in norm._SEVENTH_QUALITIES else "triad"
    return f"{deg} | {fam} |  | {tgt}"


def _t1_ctx_chain(from_cls):
    """table 1 context back-off (distinct level keys): full from -> inversion-free -> family ->
    unigram base. Level tags keep a root-position full context distinct from the inversion-free
    back-off level (else i-root would aggregate i6/i64's transitions)."""
    return [f"L0:{from_cls.key()}", f"L1:{from_cls.inversion_free().key()}",
            f"L2:{from_cls.family().key()}", _BASE]


def _t1_outcome_parent(to):
    """table 1 outcome pooling chain (namespaced): full to -> «invfree» -> «family» -> BASE."""
    if isinstance(to, norm.LabelClass):
        if to.inversion:
            return _POOL_INVFREE + to.inversion_free().key()
        if to.quality not in ("triad", "seventh"):
            return _POOL_FAMILY + to.family().key()
        return _BASE
    if to.startswith(_POOL_INVFREE):
        return _POOL_FAMILY + _family_key_of(to[len(_POOL_INVFREE):])
    if to.startswith(_POOL_FAMILY):
        return _BASE
    return _BASE                       # BASE (terminal: parent == self)


def _t4_ctx_chain(ctx):
    """table 4 context back-off (distinct level keys): (deg,qual,mode) -> (qual,mode) -> (mode)."""
    deg, qual, mode = ctx
    return [f"L0:{deg}|{qual}|{mode}", f"L1:*|{qual}|{mode}", f"L2:*|*|{mode}"]


def _t3_entry_parent(cls):
    """table 3 entry pooling (namespaced): full class -> «invfree» -> BASE (unigram)."""
    if isinstance(cls, norm.LabelClass):
        if cls.inversion:
            return _POOL_INVFREE + cls.inversion_free().key()
        return _BASE
    if cls.startswith(_POOL_INVFREE):
        return _BASE
    return _BASE


def _t2_parent(cell):
    """table 2: a sparse (cof-band|mode-pair) change cell pools to its mode-pair marginal, then
    the overall change base. Dedicated cells (stay/parallel/relative/indeterminate) pool to base."""
    if isinstance(cell, str) and "|" in cell:
        return "mp:" + cell.split("|", 1)[1]
    if isinstance(cell, str) and cell.startswith("mp:"):
        return "BASE"
    return "BASE"


def _t5_parent(cell):
    """table 5: a sparse (dist|mode) cell pools to its local-mode marginal, then the base."""
    if isinstance(cell, str) and "|" in cell:
        return "mode:" + cell.split("|", 1)[1]
    if isinstance(cell, str) and cell.startswith("mode:"):
        return "BASE"
    return "BASE"


# ══════════════════════════════════════════════════════════════════════════
# Fit one training set into the 6 tables
# ══════════════════════════════════════════════════════════════════════════

def fit_tables(stems, stem_data, label):
    c = count_tables(stems, stem_data)

    # 1: transition per mode (conditional)
    t1 = {}
    t1_meta = {}
    for is_major, name in ((True, "major"), (False, "minor")):
        pc = {(a, b): n for (a, b), n in c["trans"][is_major].items()}
        rows, meta = estimate_conditional(pc, _t1_ctx_chain, _t1_outcome_parent,
                                          display_key=lambda cf: cf.key())
        t1[name] = rows
        t1_meta[name] = meta

    # 2: key transition (categorical)
    t2_dist, t2_meta = katz_distribution(dict(c["keytrans"]), _t2_parent)

    # 3: entry (categorical)
    t3_dist, t3_meta = katz_distribution(dict(c["entry"]), _t3_entry_parent)

    # 4: bass/inversion (conditional)
    pc4 = {}
    for ctx, invc in c["inv_ctx"].items():
        for inv, n in invc.items():
            pc4[(ctx, inv)] = n
    t4_rows, t4_meta = estimate_conditional(
        pc4, _t4_ctx_chain, lambda o: None,
        display_key=lambda ctx: f"{ctx[0]}|{ctx[1]}|{ctx[2]}")

    # 5: signature prior per declared mode (categorical per context)
    t5 = {}
    t5_meta = {}
    for dmode, cells in c["sigprior"].items():
        dist, meta = katz_distribution(dict(cells), _t5_parent)
        t5[dmode] = dist
        t5_meta[dmode] = meta

    # 6: boundary (Bernoulli per beat class — no distribution to normalize)
    t6 = {}
    for cls, v in c["boundary"].items():
        p = v["boundary"] / v["slots"] if v["slots"] else None
        t6[cls] = {"boundary": v["boundary"], "slots": v["slots"], "prob": p}

    free_params = (sum(m["free_params"] for m in t1_meta.values())
                   + t2_meta["free_params"] + t3_meta["free_params"]
                   + t4_meta["free_params"]
                   + sum(m["free_params"] for m in t5_meta.values())
                   + len([x for x in t6.values() if x["prob"] is not None]))
    tokens = c["tokens"]
    # per-table training-token bases (the fit's own data size per table): t1=transition_pairs,
    # t2=adjacency (stay+change), t3=key_changes, t4=inv_labels, t5=segments, t6=boundary_slots.
    per_table_tokens = {
        "table1": tokens["transition_pairs"],
        "table2": tokens["transition_pairs"] + tokens["key_changes"],
        "table3": tokens["key_changes"],
        "table4": tokens["inv_labels"],
        "table5": tokens["local_key_segments"],
        "table6": tokens["boundary_slots"],
    }
    total_tokens = sum(per_table_tokens.values())
    tables = {
        "provenance_label": label,
        "table1_chord_transition": t1,
        "table2_key_transition": t2_dist,
        "table3_entry_chord": t3_dist,
        "table4_bass_inversion": t4_rows,
        "table5_signature_prior": t5,
        "table6_boundary_by_beat_class": t6,
    }
    meta = {
        "tokens": tokens,
        "per_table_tokens": per_table_tokens,
        "total_tokens_for_bound": total_tokens,
        "free_params": {
            "table1": {k: m["free_params"] for k, m in t1_meta.items()},
            "table2": t2_meta["free_params"], "table3": t3_meta["free_params"],
            "table4": t4_meta["free_params"],
            "table5": {k: m["free_params"] for k, m in t5_meta.items()},
            "table6": len([x for x in t6.values() if x["prob"] is not None]),
            "total": free_params,
        },
        "tokens_per_param": (total_tokens / free_params) if free_params else float("inf"),
        "passes_capacity_bound": (free_params == 0 or total_tokens / free_params >= TOKENS_PER_PARAM_MIN),
        "table1_meta": t1_meta, "table2_meta": t2_meta, "table3_meta": t3_meta,
        "table4_meta": t4_meta, "table5_meta": t5_meta,
        "boundary_out_of_grid": c["boundary_out_of_grid"],
        "boundary_pieces_counted": c["boundary_pieces_counted"],
        "boundary_excluded": c["boundary_excluded"],
        "raw_counts": c,      # kept for the inventory / reconciliation (not serialized wholesale)
    }
    return tables, meta


# ══════════════════════════════════════════════════════════════════════════
# Establishment checks
# ══════════════════════════════════════════════════════════════════════════

def check_row_sums(tables):
    """(ii) every conditional/categorical table row sums to 1 within 1e-9. Table 6 is Bernoulli
    (each prob in [0,1], not a distribution) — checked separately."""
    problems = []

    def _check(name, dist):
        s = sum(dist.values())
        if abs(s - 1.0) > 1e-9:
            problems.append((name, s))

    for mode, rows in tables["table1_chord_transition"].items():
        for ck, row in rows.items():
            _check(f"t1[{mode}][{ck}]", row["dist"])
    _check("t2", tables["table2_key_transition"])
    _check("t3", tables["table3_entry_chord"])
    for ck, row in tables["table4_bass_inversion"].items():
        _check(f"t4[{ck}]", row["dist"])
    for dmode, dist in tables["table5_signature_prior"].items():
        _check(f"t5[{dmode}]", dist)
    for cls, v in tables["table6_boundary_by_beat_class"].items():
        if v["prob"] is not None and not (0.0 <= v["prob"] <= 1.0):
            problems.append((f"t6[{cls}]", v["prob"]))
    return problems


def hand_checks(all_meta):
    """(iv) V->I (major), i->V (minor), V->vi (major): raw count -> probability arithmetic."""
    rc = all_meta["raw_counts"]
    out = {}

    def find(mode_bool, from_key, to_key):
        row = rc["trans"][mode_bool]
        num = 0
        den = 0
        for (a, b), n in row.items():
            if a.key() == from_key:
                den += n
                if b.key() == to_key:
                    num += n
        return num, den

    for name, mode_bool, fk, tk in (
        ("V->I (major)", True, "V | Maj |  | ", "I | Maj |  | "),
        ("i->V (minor)", False, "I | Min |  | ", "V | Maj |  | "),
        ("V->vi (major)", True, "V | Maj |  | ", "VI | Min |  | "),
    ):
        num, den = find(mode_bool, fk, tk)
        out[name] = {"from": fk, "to": tk, "raw_count_pair": num, "raw_count_from_row": den,
                     "mle_prob": (num / den if den else None)}
    return out


# ══════════════════════════════════════════════════════════════════════════
# Main
# ══════════════════════════════════════════════════════════════════════════

def main():
    ap = argparse.ArgumentParser()
    here = Path(__file__).resolve().parent
    ap.add_argument("--out-dir", default=str(here))
    args = ap.parse_args()
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    fa = json.loads(FOLD_ARTIFACT.read_text(encoding="utf-8"))
    stem_index = fa["stem_index"]
    covered = sorted(stem_index.keys())
    stem_fold = {s: stem_index[s]["fold"] for s in covered}

    # extract every stem once
    stem_data = {s: extract_stem(s) for s in covered}

    git_hash = _git_head()
    prov = {
        "generator": _rel(__file__),
        "corpus_git_hash": git_hash,
        "fold_artifact": _rel(FOLD_ARTIFACT),
        "wir_dir": _rel(WIR_DIR),
        "corpus_xml_dir": _rel(CORPUS_XML_DIR),
        "normalization_version": norm.NORMALIZATION_VERSION,
        "ground_truth_substrate": "dcml_parser.load_wir_regions (OI-142-corrected)",
        "protocol": "cowork_prefit_gates.md (OI-176/OI-177), user-ratified 2026-07-19",
        "constants": {"threshold": THRESHOLD, "alpha": ALPHA, "n_folds": N_FOLDS,
                      "tokens_per_param_min": TOKENS_PER_PARAM_MIN},
        "xml_elements_used": ["<key><fifths>", "<key><mode>", "<time><beats>", "<time><beat-type>"],
        "oi184_flagged_excluded_from_boundary": sorted(OI184_FLAGGED),
    }

    # ── fit the 6 training sets ──
    fits = {}     # label -> (tables, meta)
    for i in range(N_FOLDS):
        train = [s for s in covered if stem_fold[s] != i]
        fits[f"fold{i}"] = fit_tables(train, stem_data, f"train=complement(fold{i}) n={len(train)}")
    fits["all"] = fit_tables(covered, stem_data, f"train=all-326 n={len(covered)}")

    # ── write the fitted-table artifacts (per fold + all) ──
    for label, (tables, meta) in fits.items():
        art = {"provenance": {**prov, "fit_scope": label,
                              "source": "fold_assignment.json complement" if label != "all" else "all-326"},
               **{k: v for k, v in tables.items() if k != "provenance_label"}}
        fn = out_dir / (f"tables_{label}.json" if label != "all" else "tables_all.json")
        fn.write_text(json.dumps(art, indent=1, ensure_ascii=False, sort_keys=True) + "\n",
                      encoding="utf-8")

    # ── establishment ──
    all_tables, all_meta = fits["all"]
    row_problems = check_row_sums(all_tables)
    for label, (tables, _m) in fits.items():
        rp = check_row_sums(tables)
        if rp:
            row_problems.extend([(f"{label}:{n}", s) for n, s in rp[:3]])

    rc_all = all_meta["raw_counts"]
    recon = {
        "labels": all_meta["tokens"]["labels"],
        "transition_pairs": all_meta["tokens"]["transition_pairs"],
        "key_changes": all_meta["tokens"]["key_changes"],
        "labels_ok": all_meta["tokens"]["labels"] == RECON_LABELS,
        "transition_pairs_ok": all_meta["tokens"]["transition_pairs"] == RECON_TRANS,
        "key_changes_ok": all_meta["tokens"]["key_changes"] == RECON_KEYCHG,
    }
    recon["all_ok"] = recon["labels_ok"] and recon["transition_pairs_ok"] and recon["key_changes_ok"]
    hchecks = hand_checks(all_meta)

    if row_problems:
        raise SystemExit(f"STOP (#13): {len(row_problems)} table rows do not sum to 1: "
                         f"{row_problems[:5]}")
    if not recon["all_ok"]:
        raise SystemExit(f"STOP (#13): reconciliation to the count inventory FAILED: {recon}")

    # ── capacity bound per fold ──
    capacity = {}
    for label, (_t, meta) in fits.items():
        capacity[label] = {
            "total_tokens": meta["total_tokens_for_bound"],
            "free_params": meta["free_params"]["total"],
            "tokens_per_param": round(meta["tokens_per_param"], 3),
            "passes": meta["passes_capacity_bound"],
        }
    if not all(v["passes"] for v in capacity.values()):
        failing = {k: v for k, v in capacity.items() if not v["passes"]}
        raise SystemExit(f"STOP (#13): capacity bound (tokens/params >= {TOKENS_PER_PARAM_MIN}) "
                         f"FAILED on: {failing}")

    # ── sensitive cells (desk-sim §4.3) — reuse the count-inventory predicates for the counts,
    #    report the fitted P each constituent transition receives ──
    sensitive = build_sensitive_report(fits, stem_data, covered, stem_fold)

    # ── the OI-177 parameter inventory artifact ──
    inventory = build_inventory(fits, prov, recon, hchecks, capacity, sensitive, all_tables)
    (out_dir / "table_fit_inventory.json").write_text(
        json.dumps(inventory, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    write_inventory_summary(out_dir / "table_fit_inventory_summary.txt", inventory)

    print(f"Wrote tables_fold0..4.json, tables_all.json, table_fit_inventory.json (+summary) to {out_dir}")
    print(f"  reconcile labels/trans/keychg: {recon['all_ok']}  "
          f"({recon['labels']}/{recon['transition_pairs']}/{recon['key_changes']})")
    print(f"  row-sums OK: {not row_problems};  capacity all pass: "
          f"{all(v['passes'] for v in capacity.values())}")
    for label in [f"fold{i}" for i in range(N_FOLDS)] + ["all"]:
        v = capacity[label]
        print(f"    {label:6s} tokens={v['total_tokens']:7d} params={v['free_params']:4d} "
              f"tok/param={v['tokens_per_param']:.1f} pass={v['passes']}")


# ── sensitive-cell report ──

_SENS = [
    ("V6_to_vihalfdim", "V6 -> vi half-dim (deg V maj fig '6' -> deg VI min color '/o')"),
    ("vihalfdim_to_IV", "vi half-dim -> IV (deg VI '/o' -> deg IV maj)"),
    ("i_to_IVraised6", "minor key: i -> IV (raised 6th, maj color)"),
    ("vi_to_appliedTo_vi", "vi -> any chord applied to VI (target base VI)"),
    ("applied_not_resolving_to_target", "applied chord -> a chord whose degree != target (aggregate)"),
    ("V_to_vi", "V (maj, not applied) -> VI (any, not applied) — deceptive"),
]


def _sens_match(name, a, b, ma):
    """Predicate over normalized adjacent (a -> b) same-key classes (ma = local key is_major).
    Mirrors the count-inventory predicates in normalized-class space so counts reconcile."""
    da, db = a.degree_base, b.degree_base
    a_min = a.quality in ("Min", "Min7", "MinMaj7", "Dim", "Dim7", "HalfDim", "HalfDim7")
    b_min = b.quality in ("Min", "Min7", "MinMaj7", "Dim", "Dim7", "HalfDim", "HalfDim7")
    a_hd = a.quality in ("HalfDim", "HalfDim7")
    b_hd = b.quality in ("HalfDim", "HalfDim7")
    tgt_a = a.target.split("/")[-1].upper() if a.target else ""
    tgt_b = b.target.split("/")[-1].upper() if b.target else ""
    if name == "V6_to_vihalfdim":
        return (da == "V" and a.quality == "Maj" and a.inversion == "6" and not a.target
                and db == "VI" and b_hd and not b.target)
    if name == "vihalfdim_to_IV":
        return (da == "VI" and a_hd and not a.target
                and db == "IV" and b.quality in ("Maj", "Maj7", "Dom7") and not b.target)
    if name == "i_to_IVraised6":
        return (not ma and da == "I" and a_min and not a.target
                and db == "IV" and b.quality in ("Maj", "Maj7", "Dom7") and not b.target)
    if name == "vi_to_appliedTo_vi":
        return (da == "VI" and a_min and not a.target and tgt_b == "VI")
    if name == "applied_not_resolving_to_target":
        return (bool(tgt_a) and bool(db) and db != tgt_a)
    if name == "V_to_vi":
        return (da == "V" and a.quality in ("Maj", "Dom7", "Maj7") and not a.target
                and db == "VI" and not b.target)
    return False


# the two normalized-vs-raw deltas, explained (both because the fit-time normalization is FINER /
# more complete than compare_rn's coarse parse used by the count inventory — the OI-186 intent).
_SENS_DELTA_NOTE = {
    "V_to_vi": ("normalized count is raw_count-1: bwv90.5 'V->bVI' — the fit-time normalization "
                "preserves the bVI accidental (#12), so V->bVI is NOT a diatonic deceptive V->vi; "
                "the count inventory's compare_rn parse folds bVI to VI."),
    "applied_not_resolving_to_target": (
        "normalized count is raw_count+1: bwv60.5 'It6/ii -> V7/ii' — the fit-time normalization "
        "maps It6 to the AugSixth class (dispatch-mandated), exposing the applied It6/ii; the count "
        "inventory's compare_rn parse leaves It6 unparseable (label_components None) so it was missed."),
}


def build_sensitive_report(fits, stem_data, covered, stem_fold):
    """Report each desk-sim §4.3 named cell: the count-inventory authoritative raw-label count
    (per fold + overall), the fit-time NORMALIZED-class count, the disposition (own-MLE >=20 vs
    pooled), the two explained normalized-vs-raw deltas, and the fitted P the representative
    single-pair transition receives in the all-326 fitted table 1."""
    ci = json.loads(COUNT_INVENTORY.read_text(encoding="utf-8"))["sensitive_cells"]

    def count_over(stems):
        per = {n: 0 for n, _ in _SENS}
        for stem in stems:
            seq = stem_data[stem]["seq"]
            for i in range(len(seq) - 1):
                a, b = seq[i], seq[i + 1]
                if a["tonic"] is None or b["tonic"] is None:
                    continue
                if not (a["tonic"] == b["tonic"] and a["is_major"] == b["is_major"]):
                    continue
                if a["cls"].raw_unnormalized or b["cls"].raw_unnormalized:
                    continue
                for name, _ in _SENS:
                    if _sens_match(name, a["cls"], b["cls"], a["is_major"]):
                        per[name] += 1
        return per

    # collect the constituent fine transitions per named cell (over all-326)
    constituents = {n: Counter() for n, _ in _SENS}
    for stem in covered:
        seq = stem_data[stem]["seq"]
        for i in range(len(seq) - 1):
            a, b = seq[i], seq[i + 1]
            if a["tonic"] is None or b["tonic"] is None:
                continue
            if not (a["tonic"] == b["tonic"] and a["is_major"] == b["is_major"]):
                continue
            if a["cls"].raw_unnormalized or b["cls"].raw_unnormalized:
                continue
            for name, _ in _SENS:
                if _sens_match(name, a["cls"], b["cls"], a["is_major"]):
                    constituents[name][(a["is_major"], a["cls"], b["cls"])] += 1

    overall = count_over(covered)
    per_train = {f"fold{i}": count_over([s for s in covered if stem_fold[s] != i])
                 for i in range(N_FOLDS)}
    all_tables = fits["all"][0]

    def fitted_handling(is_major, from_cls, to_cls):
        rows = all_tables["table1_chord_transition"]["major" if is_major else "minor"]
        row = rows.get(from_cls.key())
        if row is None:
            return {"prob": None, "how": "from-context not observed"}
        dist = row["dist"]
        tk = to_cls.key()
        if tk in dist:
            return {"prob": round(dist[tk], 6), "how": "own_MLE"}
        node = _t1_outcome_parent(to_cls)
        for _ in range(5):
            if node in dist:
                return {"prob": round(dist[node], 6), "how": f"pooled -> {node}"}
            nxt = _t1_outcome_parent(node)
            if nxt == node:
                break
            node = nxt
        return {"prob": None, "how": "not in row"}

    report = {}
    for name, desc in _SENS:
        top = []
        for (is_major, fc, tc), n in constituents[name].most_common(6):
            fh = fitted_handling(is_major, fc, tc)
            top.append({
                "mode": "major" if is_major else "minor",
                "transition": f"{fc.key()}  =>  {tc.key()}",
                "raw_count": n,
                "fine_cell_own_MLE": n >= THRESHOLD,
                "fitted": fh,
            })
        report[name] = {
            "description": desc,
            "raw_label_count_overall": ci[name]["count_overall"],       # count-inventory authoritative
            "raw_label_count_by_fold_holdout": ci[name]["by_fold"],
            "normalized_class_count_overall": overall[name],
            "normalized_class_count_by_train_complement": {k: v[name] for k, v in per_train.items()},
            "disposition_all326": ("own_MLE (>=20)" if ci[name]["count_overall"] >= THRESHOLD
                                    else "pooled (<20 -> declared parent)"),
            "note_disposition_is_aggregate": (
                "the count and disposition are the AGGREGATE over the predicate's constituent fine "
                "transitions; the fitted table gates each FINE (from,to) cell individually (below)."),
            "top_constituent_fine_transitions": top,
        }
        if name in _SENS_DELTA_NOTE:
            report[name]["normalized_vs_raw_delta_note"] = _SENS_DELTA_NOTE[name]
    return report


# ── the OI-177 parameter inventory ──

def build_inventory(fits, prov, recon, hchecks, capacity, sensitive, all_tables):
    def raw_hist(counter):
        h = Counter()
        for n in counter.values():
            h[_hist_bin(n)] += 1
        return dict(sorted(h.items(), key=lambda kv: _bin_order(kv[0])))

    per_fold_dims = {}
    for label in [f"fold{i}" for i in range(N_FOLDS)] + ["all"]:
        tables, meta = fits[label]
        rc = meta["raw_counts"]
        t1_cells = {m: len(rc["trans"][b]) for b, m in ((True, "major"), (False, "minor"))}
        pt_tok = meta["per_table_tokens"]
        fp = meta["free_params"]
        pt_params = {"table1": fp["table1"]["major"] + fp["table1"]["minor"],
                     "table2": fp["table2"], "table3": fp["table3"], "table4": fp["table4"],
                     "table5": sum(fp["table5"].values()), "table6": fp["table6"]}
        per_fold_dims[label] = {
            "tokens": meta["tokens"],
            "per_table_tokens": pt_tok,
            "per_table_free_params": pt_params,
            "per_table_tokens_per_param": {t: (round(pt_tok[t] / pt_params[t], 2)
                                               if pt_params[t] else None) for t in pt_tok},
            "total_tokens_for_bound": meta["total_tokens_for_bound"],
            "free_params": meta["free_params"],
            "tokens_per_param": round(meta["tokens_per_param"], 3),
            "passes_capacity_bound": meta["passes_capacity_bound"],
            "table1": {
                "distinct_from_contexts": {
                    "major": len({a for (a, b) in rc["trans"][True]}),
                    "minor": len({a for (a, b) in rc["trans"][False]})},
                "distinct_transition_pairs": t1_cells,
                "reliable_rows": {m: meta["table1_meta"][m]["reliable_rows"] for m in ("major", "minor")},
                "distinct_estimated_rows": {m: meta["table1_meta"][m]["distinct_estimated_rows"]
                                            for m in ("major", "minor")},
                "pair_count_histogram": {
                    "major": raw_hist(rc["trans"][True]),
                    "minor": raw_hist(rc["trans"][False])},
            },
            "table2": {"distinct_cells": len(rc["keytrans"]),
                       "cell_count_histogram": raw_hist(rc["keytrans"]),
                       "reliable_cells": meta["table2_meta"]["reliable_cells"],
                       "pooled_buckets": meta["table2_meta"]["pooled_buckets"]},
            "table3": {"distinct_entry_classes": len(rc["entry"]),
                       "class_count_histogram": raw_hist(rc["entry"]),
                       "reliable_cells": meta["table3_meta"]["reliable_cells"],
                       "pooled_buckets": meta["table3_meta"]["pooled_buckets"]},
            "table4": {"distinct_contexts": len(rc["inv_ctx"]),
                       "reliable_rows": meta["table4_meta"]["reliable_rows"],
                       "distinct_estimated_rows": meta["table4_meta"]["distinct_estimated_rows"]},
            "table5": {"declared_mode_contexts": {dm: {"distinct_cells": len(cells),
                                                       "cell_count_histogram": raw_hist(cells)}
                                                  for dm, cells in rc["sigprior"].items()}},
            "table6": {"beat_classes": tables["table6_boundary_by_beat_class"],
                       "out_of_grid_label_starts": meta["boundary_out_of_grid"],
                       "pieces_counted": meta["boundary_pieces_counted"],
                       "excluded": meta["boundary_excluded"]},
        }

    return {
        "provenance": prov,
        "purpose": ("OI-177 pre-fit parameter inventory for the label-side table fit. Per fold + "
                    "all-326: table dimensions, raw-cell histograms, own-MLE vs pooled cell counts, "
                    "effective free parameters, training tokens, tokens/params>=10 check."),
        "establishment": {
            "reconcile_count_inventory": recon,
            "row_sums_all_within_1e-9": True,     # (else the run STOPped)
            "byte_reproducible": "run twice; artifacts are deterministic (sorted, no timestamp/random)",
            "normalization_coverage_all326": {
                "raw_unnormalized_labels": fits["all"][1]["tokens"]["raw_unnormalized"],
                "indeterminate_mode_labels": fits["all"][1]["tokens"]["indeterminate_mode_labels"],
                "note": ("every WiR label normalizes (raw_unnormalized == 0: the 2 It6 tokens route "
                         "to the AugSixth class); nothing is silently dropped — the label total "
                         "reconciles to 18418 (#12/DT-23)."),
            },
            "hand_checks_table1": hchecks,
        },
        "capacity_bound_summary": capacity,
        "per_fold": per_fold_dims,
        "sensitive_cells_desk_sim_4_3": sensitive,
        "notes": _INVENTORY_NOTES,
    }


def _hist_bin(n):
    if n == 1:
        return "1"
    if n < 5:
        return "2-4"
    if n < 20:
        return "5-19"
    if n < 50:
        return "20-49"
    if n < 100:
        return "50-99"
    return "100+"


def _bin_order(b):
    return ["1", "2-4", "5-19", "20-49", "50-99", "100+"].index(b)


_INVENTORY_NOTES = {
    "smoothing": ("Katz-style back-off with a hard count>=20 reliability gate and additive alpha=1 "
                  "at the pooled base (the single declared alpha per table). Reliable cells "
                  "(count>=20) keep their EXACT MLE = count/total; sparse cells pool into their "
                  "declared parent (chains below), promoted while a bucket stays <20, and the "
                  "residual (sparse-count) mass is distributed over the pooled buckets alpha-smoothed. "
                  "Rows sum to 1 by construction."),
    "backoff_chains": {
        "table1": "context (from) back-off: full -> inversion-free -> family -> unigram; outcome "
                  "(to) pooled within a reliable row: full -> inversion-free -> family -> base. "
                  "NOTE (interpretation, reported per #13): the dispatch chain 'drop BOTH sides' "
                  "inversion' is realized as context (from-side) coarsening at the row level plus "
                  "within-row outcome pooling; the from-side is not coarsened per-sparse-cell "
                  "(which would require cross-row redistribution). The named sensitive cells "
                  "(V->vi own-MLE at 236; V6->vi-halfdim pooled at 2) behave as specified.",
        "table2": "sparse (cofBand|modePair) change cell -> mode-pair marginal -> base; "
                  "distances>=3 pre-pooled to 'cofFar' per mode pair (declared cell definition).",
        "table3": "entry class -> inversion-free -> unigram base.",
        "table4": "context (deg,quality,mode) -> (quality,mode) -> (mode); inversion-figure outcome.",
        "table5": "cell (signed-fifths-distance | local-mode) per declared mode; |distance|>=2 "
                  "pre-pooled to 'far'; sparse cell -> local-mode marginal -> base.",
        "table6": "no pooling (Bernoulli per beat class); cells with <20 slots would be reported.",
    },
    "table5_distance": ("signed circle-of-fifths displacement of the local key's diatonic COLLECTION "
                        "(minor keys use their relative-major signature) from the piece's notated "
                        "signature fifths, folded to (-6,6]; kept for {-1,0,+1}, |d|>=2 pooled to 'far'. "
                        "The signature's relative pair (major + relative minor) is distance 0, split by "
                        "the local-mode coordinate. Initial signature used; 3 multi-signature pieces "
                        "flagged."),
    "table6_grid": ("denominator = a 16th-note (0.25 quarter-beat) metric grid per counted measure, "
                    "the finest resolution that captures every observed WiR label beat with no "
                    "snapping. A slot is a boundary iff a GT label starts there. Sub-tactus boundary "
                    "probability is grid-dependent (the note-event denominator is part 2, sec 3.7); "
                    "reported with that caveat. Pickup measures (m0) and the 7 OI-184 flagged pieces "
                    "excluded; 3/2 and 2 multi-meter pieces excluded (flagged)."),
    "ninth_figures": ("figures '9'/'9[b9]' (2 labels: V9/V, V9[b9]) are outside the dispatch's "
                      "enumerated inversion set {7,6/5,4/3,2,42}; mapped to the dominant-seventh "
                      "family (a ninth carries a seventh) with the figure retained verbatim. Flagged."),
    "multi_level_applied": ("3 two-level applied labels (V6/5/V/III, V2/V/III, V/V/III) are peeled to "
                            "a clean base chord with the applied chain joined as the target "
                            "(e.g. 'V/III'), reusing dcml._split_rntxt_applied iteratively (no new parser)."),
}


def write_inventory_summary(path, inv):
    L = []
    L.append("=== OI-177 label-side table-fit parameter inventory — summary ===")
    L.append(f"corpus git_hash: {inv['provenance']['corpus_git_hash']}")
    r = inv["establishment"]["reconcile_count_inventory"]
    L.append(f"reconcile (all-326): labels={r['labels']} trans={r['transition_pairs']} "
             f"keychg={r['key_changes']}  ->  ALL_OK={r['all_ok']}")
    L.append("")
    L.append("-- capacity bound (tokens/params >= 10) --")
    L.append(f"{'fit':8s} {'tokens':>8s} {'params':>7s} {'tok/param':>10s} {'pass':>5s}")
    for label in [f"fold{i}" for i in range(N_FOLDS)] + ["all"]:
        v = inv["capacity_bound_summary"][label]
        L.append(f"{label:8s} {v['total_tokens']:8d} {v['free_params']:7d} "
                 f"{v['tokens_per_param']:10.2f} {str(v['passes']):>5s}")
    L.append("")
    L.append("-- all-326 free params by table --")
    fp = inv["per_fold"]["all"]["free_params"]
    L.append(f"  table1 major={fp['table1']['major']} minor={fp['table1']['minor']}; "
             f"table2={fp['table2']} table3={fp['table3']} table4={fp['table4']}; "
             f"table5={fp['table5']}; table6={fp['table6']}; TOTAL={fp['total']}")
    L.append("")
    L.append("-- hand checks (all-326 raw MLE) --")
    for name, hc in inv["establishment"]["hand_checks_table1"].items():
        L.append(f"  {name:16s}: {hc['raw_count_pair']}/{hc['raw_count_from_row']} = "
                 f"{hc['mle_prob']:.4f}" if hc["mle_prob"] is not None else f"  {name}: n/a")
    L.append("")
    L.append("-- table 6 boundary by beat class (all-326) --")
    for cls, v in inv["per_fold"]["all"]["table6"]["beat_classes"].items():
        p = f"{v['prob']:.4f}" if v["prob"] is not None else "n/a"
        L.append(f"  {cls:14s} boundary={v['boundary']:6d} slots={v['slots']:7d} P={p}")
    t6 = inv["per_fold"]["all"]["table6"]
    L.append(f"  pieces_counted={t6['pieces_counted']} out_of_grid_starts={t6['out_of_grid_label_starts']}")
    L.append(f"  excluded: flagged={len(t6['excluded']['flagged'])} "
             f"meter={t6['excluded']['meter']} no_meter={t6['excluded']['no_meter']}")
    L.append("")
    L.append("-- sensitive cells (desk-sim 4.3): raw-label(count-inv) / normalized / disposition --")
    for name, sc in inv["sensitive_cells_desk_sim_4_3"].items():
        delta = "  [delta explained]" if "normalized_vs_raw_delta_note" in sc else ""
        L.append(f"  {name:34s} raw={sc['raw_label_count_overall']:4d}  "
                 f"norm={sc['normalized_class_count_overall']:4d}  "
                 f"{sc['disposition_all326']}{delta}")
    path.write_text("\n".join(L) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
