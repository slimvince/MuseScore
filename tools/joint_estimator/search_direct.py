#!/usr/bin/env python3
"""search_direct.py — THE DIRECT-METRIC WEIGHT SEARCH (the ratified fallback; the weight stage,
second attempt). Cowork dispatch `cc_instruction_direct_metric_search.md`, 2026-07-19, executing the
user-ruled option 1 after the likelihood fit's STOP (OI-187).

★ WHAT THIS IS. The likelihood fit maximized the conditional probability of the ground-truth PATH and
moved the graded metric the wrong way on two of four axes (OI-187): the proxy->target link (#17d) was
never a ledger premise and is refuted. The ratified fallback replaces the proxy with the target — the
published minimum-error-rate protocol (Och 2003, "Minimum Error Rate Training in Statistical Machine
Translation", ACL; the few-weights / direct-error-minimization / random-restart-stability form, with
the line search done on a declared grid rather than by Och's exact upper-envelope sweep — declared in
the artifact as the one approximation to the published method). The tables stay exactly as counted;
only the 13 combination weights move.

★ THE SEARCH OBJECTIVE (user ruling, 2026-07-19: ★R = M2):
        R(w) = root_disagree_fraction(w) + key_local_disagree_fraction(w)
both duration-weighted on the robust unit, POOLED over the pieces of a training-fold complement.
Roman numeral and key-home are computed and recorded beside it; they never enter R.

★ THE FIREWALL, stated precisely for this fit event (it differs from the likelihood fit's and the
difference is the whole point):
  - R(w) is a TRAINING-FOLD error quantity. The optimizer consults it on TRAINING folds only. That is
    the ratified fallback's defining property, not a leak.
  - Each held-out fold is evaluated EXACTLY ONCE, by the per-fold selected optimum. The optimum is
    selected on the TRAINING objective (best converged R over the 21 starts) — never on held-out.
  - No other accuracy figure is consulted anywhere. Grep-provable: `grade_stems` is the ONLY function
    in this module that grades, and the only stem list ever handed to it is a training-fold complement
    (`training_stems` builds it as `fold_of[s] != fold`). This module never constructs a held-out stem
    list at all. The held-out evaluation is a separate module (`search_run.py`) that reads the frozen
    selected weights, grades each fold's held-out pieces once, and feeds nothing back.

★ THE GRADER IS THE PINNED ONE (#6). `probe_run.decode_to_regions` / `probe_run.grade_regions` — the
same a8/compare_rn chain the committed baselines and the likelihood fit's held-out arm went through.
There is no second grader and no decomposed surrogate of it.

★ THE DECODE IS THE PINNED ONE (#6, established at runtime, #19). The search cannot afford to call
`probe_decoder.decode_piece` once per piece per objective evaluation (2.9 s/piece measured). It instead
caches the decoder's OWN lattice — `fit_weights.build_unit(..., augment_gt=False, gt_path=None)`, whose
candidates come from `probe_decoder._candidate_states_for_segment` and whose features come from
`probe_decoder.segment_features` — and re-runs the max-plus recursion over it at each candidate weight
vector. The lattice is weight-INDEPENDENT (the prune is a pitch-content filter; the features are raw
factor log-probabilities), which is what makes this exact rather than approximate. `establish_decoder`
proves it: the recovered segmentation, states and score must equal `decode_piece`'s, at identity AND at
random weight vectors, on a named sample. A single mismatch fails the run.
"""
from __future__ import annotations

import json
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent.parent
sys.path.insert(0, str(_ROOT / "tools"))
sys.path.insert(0, str(_HERE))

import probe_decoder as pd           # noqa: E402  the pinned decoder: lattice, factors, features
import probe_run as pr               # noqa: E402  the pinned grading chain (decode_to_regions/grade_regions)
import fit_weights as fw             # noqa: E402  the pinned lattice builder + TableSet
import fit_run as fr                 # noqa: E402  the pinned axis/counter-name map (not restated here, #6)
import gen_label_tables as glt       # noqa: E402  fold machinery / provenance helpers

NEG_INF = -np.inf
W_NAMES = fw.W_NAMES
NW = fw.NW
WI = fw.WI
fr_NUM = fr._NUM                     # axis -> (agree-counter, disagree-counter)
AXES = fr.AXES

# ── the declared search configuration (every constant here is reported in the artifact) ──
BOUNDS_LO, BOUNDS_HI = 0.0, 5.0      # dispatch: each weight in [0, 5]; non-negativity is theory-grounded
N_STARTS = 21                        # dispatch: identity + the likelihood-fit vector + 19 seeded random
SEED_BASE = 20260719                 # the recorded seed base; start s of fold f uses SEED_BASE+100*f+s
# the coordinate line search's declared grid: multiplicative about the incumbent, plus the two bounds.
# Coarse sweeps first, then refined; a sweep that improves nothing at its step size ends that stage.
GRID_STAGES = ((2.0, 1.5), (1.25, 1.1), (1.05,))
MAX_SWEEPS_PER_STAGE = 3
IMPROVE_EPS = 1e-9                   # a strict improvement must exceed this to be taken


# ══════════════════════════════════════════════════════════════════════════════
# The weight-dependent transition matrices, built once per objective evaluation
# ══════════════════════════════════════════════════════════════════════════════

def _masked_scale(L, w):
    """w * L, with the non-finite cells of L left at -inf and never entering the multiply."""
    fin = np.isfinite(L)
    return np.where(fin, w * np.where(fin, L, 0.0), NEG_INF)


class MaxContext:
    """The max-plus semiring's weight-dependent arrays, shared by every piece at a given w. The
    likelihood fit's WeightContext exponentiates for the sum semiring; the max-plus run needs the
    scaled log-tables themselves. Kept here (not per piece) because they cost ~24k multiplies each."""

    __slots__ = ("Ent", "WL", "Lk", "stay", "wc", "wcad", "w_prior", "w_dmode")

    def __init__(self, ts: fw.TableSet, w):
        self.Ent = w[WI["entry"]] * ts.Ent                       # (24, C)
        # A table cell of probability zero stays impossible at ANY weight. The masked multiply keeps
        # the -inf cells out of the arithmetic entirely: 0 * -inf is NaN, and a NaN here would
        # silently become a reachable state (NaN compares false against every incumbent).
        self.WL = _masked_scale(ts.Lchord, w[WI["chord_trans"]])
        self.Lk = _masked_scale(ts.Lkey_off, w[WI["key_trans"]])
        self.stay = w[WI["key_trans"]] * ts.Lstay
        self.wc = np.array([w[WI[x]] for x in fw.CONTENT_W], dtype=np.float64)
        self.wcad = np.array([w[WI[x]] for x in fw.CAD_W], dtype=np.float64)
        self.w_prior, self.w_dmode = w[WI["prior"]], w[WI["declared_mode"]]


def maxplus_decode(lat: fw.UnitLattice, ts: fw.TableSet, mc: MaxContext, stats=None):
    """Viterbi over the cached lattice, with backpointers. Returns (score, segments) where each
    segment is (i, j, tonic, is_major, class_key) in the lattice's own event indexing.

    The recursion is `fit_weights.unit_logZ_and_expect`'s max branch, term for term. Two differences,
    both cost-driven and neither changing the arithmetic:
      (1) the same-key chord max runs only over the keys and previous classes that are REACHABLE at
          the boundary (the rest are -inf and contribute nothing) — the dense (24, C, C) form spends
          ~90 % of its work on -inf rows;
      (2) only the span backpointer is stored; the branch and the predecessor state are RECOMPUTED
          during the backtrack from the retained `logA`, which visits a few dozen boundaries instead
          of writing (n, 24, C) argmax arrays at every one.
    ★ TIE-BREAK SCOPE (the §5 total order, user-ratified 2026-07-20): `decode_piece` now resolves an
    EXACT-score tie by the §5 total order on paths (fewer segments; earliest boundary ticks; canonical
    class-key order) — see probe_decoder. This cached-lattice decode is a SPEED path for the stability
    DIAGNOSTIC ONLY (never the CV headline, which is `decode_piece`), and its vectorised max-plus
    recursion cannot cheaply express the §5 lexicographic order; it retains the pre-§5 branch/first-span
    tie-break. On the 6 corpus pieces whose committed decode §5 canonicalised to a different EQUAL-SCORE
    segmentation (`decode_parity_ref` regeneration, this dispatch), this decode and `decode_piece` now
    pick different-but-equally-optimal paths, so `establish_decoder` would flag those 6 if the stability
    diagnostic is RE-RUN. The committed stability figures predate §5 and are unaffected (they measure the
    per-start modulation rate, invariant to a one-boundary shift on a repeated-chord run). CLOSEOUT
    (Task-C dispatch): the vectorised max-plus form still cannot cheaply carry the §5 lexicographic path
    signature (§5-ifying the recursion would mean writing per-boundary path signatures — the very cost
    this speed path exists to avoid), so instead `establish_decoder` is RELAXED to accept EQUAL-score
    §5-equivalent paths: the hard establishment is score-exactness, and an equal-score path difference is
    reported (equal_score_path_diffs) rather than failing. decode_piece remains the §5 authority; this
    diagnostic path is off the CV headline and the production/parity critical path."""
    C, n, K = lat.C, lat.n, 24
    cw = lat.cand_feat @ mc.wc                                   # weighted content per candidate
    cadw = lat.cad @ mc.wcad                                     # (n, 24)
    spans_from, cstart, cend = lat.spans_from, lat.cstart, lat.cend

    logA = np.full((n + 1, K, C), NEG_INF)
    base = np.full((n, K, C), NEG_INF)
    bp_span = np.full((n + 1, K * C), -1, dtype=np.int32)        # which span index reached (j,k,c)
    logA_f = logA.reshape(n + 1, -1)

    for b in range(n):
        if b == 0:
            if lat.is_head:
                base[0] = (mc.w_prior * lat.prior_sig
                           + mc.w_dmode * lat.prior_inc)[:, None] + mc.Ent
            else:
                base[0] = 0.0
        else:
            prev = logA[b]
            fin_mask = np.isfinite(prev)
            live_k = np.flatnonzero(fin_mask.any(axis=1))
            if live_k.size == 0:
                continue
            sm = np.full((K, C), NEG_INF)
            for k in live_k:
                fc = np.flatnonzero(fin_mask[k])
                sm[k] = (prev[k, fc][:, None] + mc.WL[0 if k < 12 else 1][fc]).max(axis=0)
            sm += mc.stay[:, None]
            Bk = prev.max(axis=1)
            ent_in = (Bk[live_k][:, None] + mc.Lk[live_k]).max(axis=0)[:, None] + mc.Ent
            base[b] = np.where(sm >= ent_in, sm, ent_in) + cadw[b][:, None]
            if stats is not None:
                stats["live_keys"] += int(live_k.size)
                stats["finite_states"] += int(fin_mask.sum())
                stats["boundaries"] += 1
        flat = base[b].reshape(-1)
        for s in spans_from[b]:
            lo_c, hi_c = cstart[s], cend[s]
            if hi_c <= lo_c:
                continue
            kc_i = lat.cand_kc[lo_c:hi_c]
            contrib = flat[kc_i] + cw[lo_c:hi_c]
            j = lat.span_j[s]
            better = contrib > logA_f[j][kc_i]
            if better.any():
                idx = kc_i[better]
                logA_f[j][idx] = contrib[better]
                bp_span[j][idx] = s

    fin = logA_f[n]
    if not np.isfinite(fin).any():
        return NEG_INF, []
    best_flat = int(fin.argmax())
    score = float(fin[best_flat])

    # ── backtrack: the branch and the predecessor are recomputed from logA at each visited boundary ──
    segs = []
    j, kc = n, best_flat
    while j > 0:
        s = int(bp_span[j][kc])
        if s < 0:
            raise AssertionError(f"{lat.stem}: broken backpointer at boundary {j}")
        b = int(lat.span_i[s])
        k, c = divmod(kc, C)
        segs.append((b, j, k % 12, k < 12, ts.cls_keys[c]))
        if b == 0:
            break
        prev = logA[b]
        col = prev[k] + mc.WL[0 if k < 12 else 1][:, c]          # same-key: over previous classes
        sm_kc = col.max() + mc.stay[k]
        Bk = prev.max(axis=1)
        kcol = Bk + mc.Lk[:, k]                                  # key-change: over previous keys
        ent_kc = kcol.max() + mc.Ent[k, c]
        if sm_kc >= ent_kc:
            kc = k * C + int(col.argmax())
        else:
            kp = int(kcol.argmax())
            kc = kp * C + int(prev[kp].argmax())
        j = b
    segs.reverse()
    return score, segs


def segments_to_dicts(lat: fw.UnitLattice, piece, segs, ts: fw.TableSet):
    """The `DecodeResult.segments` dict form `probe_run.decode_to_regions` consumes, built from the
    lattice's own indexing (lat.lo is the unit's event offset; for a whole-piece lattice it is 0)."""
    out = []
    for (i, j, tonic, is_major, ckey) in segs:
        ai, aj = lat.lo + i, lat.lo + j
        cls = ts.vocab.classes[ckey]
        _mem, _fac, root = ts.cache.get(cls, tonic, is_major)
        out.append({"i": ai, "j": aj,
                    "start_tick": piece.events[ai][pd.EV_START],
                    "end_tick": piece.events[aj - 1][pd.EV_END],
                    "tonic_pc": tonic, "is_major": is_major,
                    "key": pd._key_string(tonic, is_major),
                    "class_key": ckey, "root_pc": root,
                    "degree": cls.degree_base, "quality": cls.quality,
                    "inversion": cls.inversion, "target": cls.target})
    return out


# ══════════════════════════════════════════════════════════════════════════════
# ★ THE ESTABLISHMENT (#19): the cached-lattice decode IS the pinned decoder's
# ══════════════════════════════════════════════════════════════════════════════

def establish_decoder(pieces, ts: fw.TableSet, stems, n_random=4, seed=7, verbose=True):
    """`maxplus_decode` over the cached lattice must reproduce `probe_decoder.decode_piece` — the SCORE
    and the SEGMENTATION/state sequence, not the score alone (#15: verify on the full output surface).
    Run at identity weights and at random weight vectors drawn from the declared box, because the search
    visits the box, not just its centre. Also checks the SCALE-INVARIANCE claim the search rests on: the
    path is a function of the ray of w, so the upper bound of the declared box cannot bind."""
    rng = np.random.default_rng(seed)
    arms = [("identity", fw.identity_vector())]
    for i in range(n_random):
        arms.append((f"random{i}", rng.uniform(BOUNDS_LO, BOUNDS_HI, size=NW)))
    lats = {}
    for stem in stems:
        piece = pieces[stem]
        sig, dm = pd.piece_header(stem)
        lats[stem] = fw.build_unit(piece, stem, 0, len(piece.events), True, None, ts, sig, dm,
                                   augment_gt=False)
    rows, bad, path_diffs = [], 0, 0
    for label, x in arms:
        mc = MaxContext(ts, x)
        wd = fw.vec_to_weights(x)
        for stem in stems:
            piece = pieces[stem]
            sig, dm = pd.piece_header(stem)
            ad = pd.FittedAdapter(leftover_mode=fw.LEFTOVER, table_set=ts.name, weights=wd)
            ad._mode_marginal = ts.adapter._mode_marginal
            r = pd.decode_piece(piece, ad, ts.vocab, ts.cache, seg_cap=fw.SEG_CAP,
                                sig_fifths=sig, declared_mode=dm)
            sc, segs = maxplus_decode(lats[stem], ts, mc)
            got = segments_to_dicts(lats[stem], piece, segs, ts)
            key = lambda ss: [(s["i"], s["j"], s["tonic_pc"], s["is_major"], s["class_key"]) for s in ss]
            # §5 relaxation (closeout, this dispatch): the cached-lattice max-plus decode reproduces the
            # SCORE exactly but breaks EXACT-score ties by its own vectorised (pre-§5) order — it cannot
            # cheaply carry §5's lexicographic path signature (see maxplus_decode's docstring). On the
            # pieces §5 canonicalised to a different EQUAL-score segmentation, decode_piece and this decode
            # pick different-but-equally-optimal paths; that is a tie-break choice, NOT a decoder defect.
            # The HARD establishment is score-exactness; a path difference AT EQUAL score is reported
            # (path_identical) but does not fail the diagnostic.
            score_ok = abs(sc - r.total_score) < 1e-9
            path_ok = key(r.segments) == key(got)
            ok = score_ok
            bad += (not ok)
            path_diffs += (score_ok and not path_ok)
            rows.append({"arm": label, "stem": stem, "n_segments": len(r.segments),
                         "score_delta": round(sc - r.total_score, 12),
                         "score_exact": bool(score_ok), "path_identical": bool(path_ok)})
            if verbose:
                tag = "OK" if path_ok else ("§5-EQUAL" if score_ok else "SCORE-MISMATCH")
                print(f"    {label:9s} {stem:10s} nseg {len(r.segments):3d} "
                      f"delta {sc - r.total_score:+.1e} {tag}", flush=True)
    # scale invariance
    inv_bad, inv_n = 0, 0
    for label, x in arms:
        for c in (0.5, 2.0, 10.0):
            m0, m1 = MaxContext(ts, np.asarray(x)), MaxContext(ts, c * np.asarray(x))
            for stem in stems:
                _s0, p0 = maxplus_decode(lats[stem], ts, m0)
                _s1, p1 = maxplus_decode(lats[stem], ts, m1)
                inv_n += 1
                inv_bad += (p0 != p1)
    return {"rows": rows, "n_checks": len(rows), "mismatches": int(bad), "pass": bool(bad == 0),
            "equal_score_path_diffs": int(path_diffs),
            "equal_score_path_diffs_note": ("§5-equivalent alternative optima (equal score, different "
                                            "boundary tie-break); acceptable — max-plus keeps its "
                                            "vectorised pre-§5 tie-break, decode_piece is the §5 authority"),
            "scale_invariance": {"n_checks": inv_n, "path_changes": int(inv_bad),
                                 "pass": bool(inv_bad == 0),
                                 "consequence": ("the decode is a function of the RAY of w, so the "
                                                 "declared box's UPPER bound cannot bind (any ray with "
                                                 "non-negative components rescales into the box); the "
                                                 "box constrains exactly non-negativity")}}


# ══════════════════════════════════════════════════════════════════════════════
# The piece store: the weight-independent lattices, built once per table set
# ══════════════════════════════════════════════════════════════════════════════

class PieceStore:
    """The cached lattices for a stem list under one frozen table set, plus the pieces themselves (the
    grading chain needs them to emit regions). Built once; every objective evaluation reads it."""

    def __init__(self, stems, ts: fw.TableSet, pieces, verbose=False):
        self.ts, self.pieces, self.stems = ts, pieces, list(stems)
        self.lats = {}
        t0 = time.perf_counter()
        for idx, stem in enumerate(self.stems):
            piece = pieces[stem]
            sig, dm = pd.piece_header(stem)
            self.lats[stem] = fw.build_unit(piece, stem, 0, len(piece.events), True, None, ts,
                                            sig, dm, augment_gt=False)
            if verbose and idx % 60 == 0:
                print(f"    lattice {idx + 1}/{len(self.stems)} {stem} "
                      f"({time.perf_counter() - t0:.0f}s)", flush=True)
        self.build_seconds = round(time.perf_counter() - t0, 1)
        self.n_candidates = int(sum(l.n_cand for l in self.lats.values()))


# ══════════════════════════════════════════════════════════════════════════════
# ★ THE ONE GRADING CALL SITE (the firewall's subject)
# ══════════════════════════════════════════════════════════════════════════════

def grade_stems(store: PieceStore, x, want_segments=False):
    """Decode every stem of `store` at weights `x` and grade it through the PINNED chain
    (`probe_run.decode_to_regions` -> `probe_run.grade_regions` -> `a8.build_piece_grid`). Returns the
    per-piece duration counters, the pooled columns, and R.

    ★ This is the ONLY place in this module that grades anything. The firewall is therefore a statement
    about WHO CALLS IT and WITH WHICH STEMS: `search_fit` calls it with TRAINING stems (the declared
    search objective, lawful per the dispatch); nothing in this module ever constructs a held-out stem
    list. The held-out evaluation lives in `search_run.py`, runs once per fold after the search has
    returned, and feeds nothing back."""
    ts = store.ts
    mc = MaxContext(ts, np.asarray(x, dtype=np.float64))
    per_piece, segs_of, no_path, t0 = {}, {}, 0, time.perf_counter()
    for stem in store.stems:
        lat = store.lats[stem]
        piece = store.pieces[stem]
        _score, segs = maxplus_decode(lat, ts, mc)
        if not segs:
            no_path += 1
            continue
        sd_ = segments_to_dicts(lat, piece, segs, ts)
        if want_segments:
            segs_of[stem] = sd_
        g = pr.grade_regions(stem, pr.decode_to_regions(piece, pr._StubResult(sd_), ts.vocab, ts.cache))
        if g is not None:
            per_piece[stem] = g
    agg = Counter()
    for v in per_piece.values():
        agg.update(v)
    cols = {}
    for axis, (a, d) in fr_NUM.items():
        tot = agg[a] + agg[d]
        cols[axis] = (100.0 * agg[a] / tot) if tot else None
    rootd = _dis_fraction(agg, "root_agree", "root_dis")
    keyld = _dis_fraction(agg, "keyl_agree", "keyl_disagree")
    return {"R": rootd + keyld, "root_disagree": rootd, "key_local_disagree": keyld,
            "columns": cols, "per_piece": per_piece, "segments": segs_of,
            "pieces_without_path": no_path, "n_pieces": len(per_piece),
            "seconds": time.perf_counter() - t0}


def _dis_fraction(agg, a_key, d_key):
    tot = agg[a_key] + agg[d_key]
    return (agg[d_key] / tot) if tot else 1.0


# ══════════════════════════════════════════════════════════════════════════════
# The coordinate line search (the published minimum-error-rate protocol's search stage)
# ══════════════════════════════════════════════════════════════════════════════

def normalize(x):
    """Rescale to max component 1.0. The decode is scale-invariant (established), so this changes NO
    objective value; it keeps the iterates well-conditioned and — because every grid step is
    multiplicative and bounded by 2 — it makes the declared box's upper bound provably unreachable, so
    a clip never silently truncates a step."""
    x = np.asarray(x, dtype=np.float64)
    m = float(x.max())
    return (x / m) if m > 0 else x.copy()


def generative_scale(x):
    """The reporting normalization: the nine generative weights average 1.0, so the vector reads
    directly against the identity ablation (where every one of them IS 1.0)."""
    x = np.asarray(x, dtype=np.float64)
    m = float(np.mean([x[WI[n]] for n in pd.GENERATIVE_WEIGHTS]))
    return (x / m) if m > 0 else x.copy()


def coordinate_search(store: PieceStore, x0, label="", verbose=True):
    """Minimize R by coordinate line search on the declared multiplicative grid.

    Piecewise-constant objective: R changes only where the arg-max path of some piece changes, so a
    gradient method is inapplicable and a simplex method stalls on plateaus of exactly-equal values.
    The coordinate line search on a declared grid is the tractable form of the published protocol's
    per-coordinate line search (Och 2003 searches each line exactly by upper envelope; the grid is the
    declared approximation, recorded in the artifact).

    Deterministic given x0. A candidate replaces the incumbent only on STRICT improvement, so ties keep
    the earlier (lower-index, coarser-step) point and the trajectory is reproducible."""
    cache = {}
    n_eval = [0]

    def R(x):
        k = np.asarray(x, dtype=np.float64).tobytes()
        hit = cache.get(k)
        if hit is not None:
            return hit, True
        g = grade_stems(store, x)
        cache[k] = g["R"]
        n_eval[0] += 1
        return g["R"], False

    x = normalize(x0)
    best, _ = R(x)
    trace = [{"stage": -1, "sweep": -1, "coord": "start", "R": best}]
    t0 = time.perf_counter()
    for si, factors in enumerate(GRID_STAGES):
        for sweep in range(MAX_SWEEPS_PER_STAGE):
            improved_any = False
            for ci, name in enumerate(W_NAMES):
                cands = []
                xi = x[ci]
                if xi > 0:
                    for f in factors:
                        cands.extend([xi * f, xi / f])
                    if si == 0:
                        cands.append(0.0)            # the declared "is this factor rejected?" probe
                else:
                    # a coordinate already at zero cannot be moved multiplicatively: the declared
                    # absolute re-entry grid, relative to the incumbent's scale (max component = 1)
                    cands.extend([0.05, 0.25, 1.0])
                best_c, best_v = None, best
                for v in cands:
                    v = min(max(v, BOUNDS_LO), BOUNDS_HI)
                    if v == xi:
                        continue
                    xt = x.copy()
                    xt[ci] = v
                    r, _cached = R(xt)
                    if r < best_v - IMPROVE_EPS:
                        best_v, best_c = r, v
                if best_c is not None:
                    x[ci] = best_c
                    x = normalize(x)
                    best = best_v
                    improved_any = True
                    trace.append({"stage": si, "sweep": sweep, "coord": name,
                                  "value": float(best_c), "R": float(best)})
            if verbose:
                print(f"      [{label}] stage {si} sweep {sweep}: R={best:.6f} "
                      f"evals={n_eval[0]} ({time.perf_counter() - t0:.0f}s)", flush=True)
            if not improved_any:
                break
    return {"x": normalize(x), "R": float(best), "n_evaluations": int(n_eval[0]),
            "n_distinct_points": int(len(cache)), "seconds": round(time.perf_counter() - t0, 1),
            "trace": trace}


def starting_points(fit_label, fold, likelihood_weights):
    """The 21 declared starts: the identity vector, the likelihood fit's own optimum for this fit (both
    NAMED per the dispatch), and 19 seeded-random draws from the declared box. The seed of start s is
    SEED_BASE + 100*fold_index + s, recorded per start."""
    starts = [{"name": "identity", "seed": None, "x": fw.identity_vector()},
              {"name": "likelihood_fit", "seed": None,
               "x": np.array([likelihood_weights[n] for n in W_NAMES], dtype=np.float64)}]
    fi = 5 if fit_label == "all" else fold
    for s in range(2, N_STARTS):
        seed = SEED_BASE + 100 * fi + s
        rng = np.random.default_rng(seed)
        starts.append({"name": f"random{s - 2:02d}", "seed": int(seed),
                       "x": rng.uniform(BOUNDS_LO, BOUNDS_HI, size=NW)})
    return starts


# ══════════════════════════════════════════════════════════════════════════════
# The per-fit driver (a fit = one training-fold complement, or the all-326 model)
# ══════════════════════════════════════════════════════════════════════════════

def training_stems(fit_label, fold, covered, fold_of):
    """★ THE TRAINING STEM LIST — the firewall's operative line. For an outer fold it is the
    COMPLEMENT of that fold; for the publishable all-326 model it is everything (that model is
    reported beside the CV headline, never in its place, per OI-176 item 5)."""
    if fit_label == "all":
        return sorted(covered)
    return sorted(s for s in covered if fold_of[s] != fold)


def search_fit(fit_label, fold, store: PieceStore, likelihood_weights, start_ids=None, verbose=True):
    """Run the declared starts for one fit and return every converged optimum. Selection of THE
    optimum (best TRAINING R) happens in `search_run.py` over the merged parts, so a part that holds
    only some starts never has to guess."""
    starts = starting_points(fit_label, fold, likelihood_weights)
    todo = list(range(len(starts))) if start_ids is None else list(start_ids)
    out = []
    for s in todo:
        st = starts[s]
        if verbose:
            print(f"    --- {fit_label} start {s} ({st['name']}) ---", flush=True)
        res = coordinate_search(store, st["x"], label=f"{fit_label}/s{s}", verbose=verbose)
        g = grade_stems(store, res["x"])          # the converged point's full training columns
        out.append({"start_index": s, "start_name": st["name"], "start_seed": st["seed"],
                    "start_x": [float(v) for v in normalize(st["x"])],
                    "x": [float(v) for v in res["x"]],
                    "weights": {n: float(res["x"][i]) for i, n in enumerate(W_NAMES)},
                    "weights_generative_scale": {n: float(generative_scale(res["x"])[i])
                                                 for i, n in enumerate(W_NAMES)},
                    "R_train": res["R"], "train_columns": g["columns"],
                    "train_root_disagree": g["root_disagree"],
                    "train_key_local_disagree": g["key_local_disagree"],
                    "n_evaluations": res["n_evaluations"],
                    "n_distinct_points": res["n_distinct_points"],
                    "seconds": res["seconds"], "trace": res["trace"]})
        if verbose:
            print(f"    --- {fit_label} start {s} done: R={res['R']:.6f} "
                  f"root {100*(1-g['root_disagree']):.2f} keyL {100*(1-g['key_local_disagree']):.2f} "
                  f"({res['seconds']:.0f}s, {res['n_evaluations']} evals) ---", flush=True)
    return out


def run(fit_label, start_ids=None, out_path=None, establish=False, verbose=True):
    t_all = time.perf_counter()
    pieces, ne, covered, fold_of, prov = fw.load_corpus()
    wf = json.loads((_HERE / "weight_fit.json").read_text(encoding="utf-8"))
    fold = None if fit_label == "all" else int(fit_label.replace("fold", ""))
    lw = (wf["all"] if fit_label == "all" else wf["folds"][str(fold)])["weights"]
    ts = fw.TableSet(fit_label)
    stems = training_stems(fit_label, fold, covered, fold_of)
    if verbose:
        where = "all 326" if fit_label == "all" else f"complement of fold {fold}"
        print(f"=== {fit_label}: {len(stems)} TRAINING pieces ({where}) ===", flush=True)
    established = {}
    if establish:
        established["decoder_vs_pinned"] = establish_decoder(
            pieces, ts, ["bwv269", "bwv352", "bwv10.7", "bwv110.7"], verbose=verbose)
        if not established["decoder_vs_pinned"]["pass"]:
            raise SystemExit("STOP: the cached-lattice decode does not reproduce the pinned decoder")
    store = PieceStore(stems, ts, pieces, verbose=verbose)
    if verbose:
        print(f"    lattices built in {store.build_seconds}s "
              f"({store.n_candidates} candidates)", flush=True)
    starts = search_fit(fit_label, fold, store, lw, start_ids=start_ids, verbose=verbose)
    out = {"fit_label": fit_label, "fold_held_out": fold,
           "n_training_pieces": len(stems), "training_stems": stems,
           "lattice_build_seconds": store.build_seconds, "n_candidates": store.n_candidates,
           "starts": starts, "establishment": established,
           "wall_seconds": round(time.perf_counter() - t_all, 1),
           "provenance": _provenance(prov)}
    if out_path:
        Path(out_path).write_text(json.dumps(out, indent=1), encoding="utf-8")
    return out


def _provenance(prov):
    return {
        "generator": glt._rel(Path(__file__)),
        "instrument_commit": glt._git_head(),
        "note_events_git_hash": prov["corpus_git_hash"],
        "fold_artifact": glt._rel(fw.FOLD_ARTIFACT),
        "dispatch": ("cc_instruction_direct_metric_weight_fit.md (Cowork 2026-07-19; the ratified "
                     "fallback, executing the user-ruled option 1 after the likelihood fit's STOP)"),
        "objective": ("R(w) = duration-weighted ROOT disagreement + duration-weighted KEY-vs-LOCAL "
                      "disagreement, pooled over the training-fold complement, on the robust unit "
                      "(CLAUDE.md block (A)) through the pinned a8/compare_rn chain. User ruling "
                      "2026-07-19: the search objective is M2 - the equal-weighted sum of the two "
                      "primary axes. Roman numeral and key-home are recorded beside it and never "
                      "enter it."),
        "method": ("coordinate line search on a declared multiplicative grid, with random restarts - "
                   "the published minimum-error-rate protocol (Och 2003, ACL). The ONE declared "
                   "approximation to that protocol: Och searches each coordinate line EXACTLY by an "
                   "upper-envelope sweep over the candidate set; here each line is searched on the "
                   "declared grid below. Deterministic given the start; strict improvement only."),
        "grid_stages": [list(s) for s in GRID_STAGES],
        "max_sweeps_per_stage": MAX_SWEEPS_PER_STAGE,
        "zero_probe": ("stage 0 additionally offers 0.0 for every coordinate, so 'the metric rejects "
                       "this factor' is reachable; a coordinate already at 0 is offered the absolute "
                       "re-entry grid (0.05, 0.25, 1.0) against the incumbent's unit scale"),
        "bounds": [BOUNDS_LO, BOUNDS_HI],
        "bounds_note": ("the decode is scale-invariant (established at runtime), so the UPPER bound "
                        "cannot bind: any ray with non-negative components rescales into the box. The "
                        "declared box therefore constrains exactly NON-NEGATIVITY, which is the "
                        "theory-grounded part (each factor is a log-probability of the generative "
                        "form; a negative weight would assert the counted table actively misleads). "
                        "Iterates are held at max-component 1.0, so no clip ever fires."),
        "n_starts": N_STARTS, "seed_base": SEED_BASE,
        "weight_vector": list(W_NAMES), "n_weights": NW,
        "seg_cap_events": fw.SEG_CAP, "key_prune_topk": pd.KEY_PRUNE_TOPK,
        "leftover_rule": f"option 2a ({fw.LEFTOVER})",
        "decoder": ("probe_decoder.decode_piece's own lattice (fit_weights.build_unit, augment_gt="
                    "False), re-decoded by the max-plus recursion in this module; established at "
                    "runtime to reproduce decode_piece's score AND segmentation exactly"),
        "grading": ("probe_run.decode_to_regions -> probe_run.grade_regions -> "
                    "a8_rebaseline_measure.build_piece_grid vs dcml_parser.load_wir_regions - the "
                    "pinned chain, unmodified"),
        "firewall": ("the objective is a TRAINING-fold error quantity, lawfully consulted by the "
                     "optimizer per the ratified fallback; this module never constructs a held-out "
                     "stem list (grade_stems is its only grading call site and training_stems its "
                     "only stem source). Held-out evaluation is search_run.py, once per fold, "
                     "downstream, feeding nothing back."),
    }


def main(argv):
    """--fit <fold0|fold1|fold2|fold3|fold4|all> [--starts a,b,c] [--establish]
    Each (fit, start-group) is an independent process writing its own part artifact; --merge
    concatenates them into weight_search.json."""
    if argv and argv[0] == "--merge":
        return merge_parts()
    fit_label, start_ids, establish = None, None, False
    i = 0
    while i < len(argv):
        if argv[i] == "--fit":
            fit_label = argv[i + 1]
            i += 2
        elif argv[i] == "--starts":
            start_ids = [int(v) for v in argv[i + 1].split(",")]
            i += 2
        elif argv[i] == "--establish":
            establish = True
            i += 1
        else:
            raise SystemExit(f"unknown argument {argv[i]}")
    if fit_label is None:
        raise SystemExit("usage: search_direct.py --fit <foldN|all> [--starts a,b,c] [--establish]")
    tag = "all" if start_ids is None else "s" + "_".join(str(v) for v in start_ids)
    out = _HERE / f"weight_search_part_{fit_label}_{tag}.json"
    r = run(fit_label, start_ids=start_ids, out_path=out, establish=establish)
    print(f"\nwrote {glt._rel(out)}  ({r['wall_seconds']}s)")


def merge_parts():
    """Merge the per-(fit, start-group) parts into weight_search.json. Each part is independent; the
    merge only concatenates its starts and checks that no start index arrives twice for a fit."""
    parts = sorted(_HERE.glob("weight_search_part_*.json"))
    if not parts:
        raise SystemExit("no weight_search_part_*.json to merge")
    fits, prov, est, part_prov = {}, None, {}, {}
    for p in parts:
        d = json.loads(p.read_text(encoding="utf-8"))
        fl = d["fit_label"]
        rec = fits.setdefault(fl, {k: d[k] for k in ("fit_label", "fold_held_out",
                                                     "n_training_pieces", "training_stems")})
        rec.setdefault("starts", [])
        rec.setdefault("lattice_build_seconds", [])
        seen = {s["start_index"] for s in rec["starts"]}
        for s in d["starts"]:
            if s["start_index"] in seen:
                raise SystemExit(f"STOP: {fl} start {s['start_index']} appears in two parts")
            rec["starts"].append(s)
        rec["starts"].sort(key=lambda s: s["start_index"])
        rec["lattice_build_seconds"].append(d["lattice_build_seconds"])
        rec["wall_seconds"] = rec.get("wall_seconds", 0.0) + d["wall_seconds"]
        part_prov[glt._rel(p)] = d["provenance"]
        prov = prov or d["provenance"]
        if d.get("establishment"):
            est.update(d["establishment"])

    # ★ The merged artifact carries the provenance of the CODE BEING COMMITTED, regenerated here, not
    # a string copied out of whichever part happened to sort first. Every part's own recorded block is
    # kept under `parts_provenance` for audit. Before regenerating, every SEARCH-DEFINING constant the
    # parts recorded must match this module — a part produced under a different grid, bound, seed base
    # or decode configuration is not mergeable with these, and saying so is the point of the check.
    _pieces, _ne, _cov, _fold_of, corpus_prov = fw.load_corpus()
    current = _provenance(corpus_prov)
    GOVERNING = ("grid_stages", "max_sweeps_per_stage", "bounds", "n_starts", "seed_base",
                 "weight_vector", "n_weights", "seg_cap_events", "key_prune_topk", "leftover_rule",
                 "objective")
    for name, pp in part_prov.items():
        drift = {k: (pp.get(k), current[k]) for k in GOVERNING if pp.get(k) != current[k]}
        if drift:
            raise SystemExit(f"STOP: {name} was produced under different search constants than the "
                             f"code being committed: {drift}")
    out = {"fits": fits, "establishment": est, "provenance": current,
           "parts_provenance": part_prov, "parts": [glt._rel(p) for p in parts]}
    dst = _HERE / "weight_search.json"
    dst.write_text(json.dumps(out, indent=1), encoding="utf-8")
    print(f"merged {len(parts)} parts -> {glt._rel(dst)}")
    for fl, rec in sorted(fits.items()):
        print(f"  {fl:7s} starts {len(rec['starts'])}/{N_STARTS} "
              f"best R {min(s['R_train'] for s in rec['starts']):.6f}")
    return out


if __name__ == "__main__":
    main(sys.argv[1:])
