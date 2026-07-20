#!/usr/bin/env python3
"""fit_run.py — the weight fit's MEASUREMENT side (algorithm-completion step 2, Task 3).

This is the downstream half of the fit event's firewall. `fit_weights.py` fits the weights and imports
no grading module at all; THIS module grades — each held-out fold exactly once, at the end — and feeds
NOTHING back. Nothing here adjusts a weight, a table, a threshold or a prune; every number it produces
is a report.

WHAT IT MEASURES (the dispatch's Task 3):
  1. the pooled 5-fold CROSS-VALIDATED decode on the robust unit — each piece decoded once, by the
     model fitted on the complement of ITS fold (tables and weights alike), with piece-level bootstrap
     95 % confidence intervals (#24);
  2. the IDENTITY-weight arm through the same folds — the mandated generative-baseline ablation —
     paired with the fitted arm on every bootstrap resample so the difference gets its own interval;
  3. the publishable all-326 model, reported BESIDE the CV headline, never in its place;
  4. the committed current-system baselines (CLAUDE.md block (A)) for reference;
  5. the three desk-simulation sensitive cases re-decoded under the fitted weights;
  6. the declared prune's cost re-measured at the fitted weights (weights change what pruning loses);
  7. decode timings and the cadence-feature fire counts under the ★R1 four-beat approach window.

REUSE (#6): the decode is `probe_decoder.decode_piece` (the pinned decoder, now weight-aware), the
region emission and the grading call are `probe_run.decode_to_regions` / `probe_run.grade_regions` —
the same pinned a8/compare_rn chain the committed baselines are measured with. No second grader.
"""
from __future__ import annotations

import json
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent.parent
sys.path.insert(0, str(_ROOT / "tools"))
sys.path.insert(0, str(_HERE))

import probe_decoder as pd           # noqa: E402
import probe_run as pr               # noqa: E402  decode_to_regions / grade_regions / BASELINES
import fit_weights as fw             # noqa: E402
import gen_label_tables as glt       # noqa: E402
import dcml_parser as dcml           # noqa: E402  (grading substrate, via probe_run's chain)
import a8_rebaseline_measure as a8   # noqa: E402  (pinned grading, read-only)

WEIGHT_FIT = _HERE / "weight_fit.json"
OUT_JSON = _HERE / "fit_grading.json"
OUT_SUMMARY = _HERE / "fit_grading_summary.txt"
BOOTSTRAP_B = 2000
BOOTSTRAP_SEED = 20260719

# the committed step-1 identity-weight probe columns (before the ★R1 window and the fermata-crossed
# boundary cells) — the reference the dispatch's prediction bands are stated against.
STEP1_IDENTITY = {"key_local_agree_pct": 74.43, "key_home_agree_pct": 53.67,
                  "root_agree_pct": 72.97, "rn_agree_pct": 59.50}
# the dispatch's written predictions for the FITTED arm (Cowork, #17b — recorded before measuring)
PREDICTION_BANDS = {"key_local_agree_pct": (77.0, 85.0), "key_home_agree_pct": (62.0, 75.0),
                    "root_agree_pct": (72.0, 78.0), "rn_agree_pct": (60.0, 68.0)}
AXES = ("key_local_agree_pct", "key_home_agree_pct", "root_agree_pct", "rn_agree_pct")
_NUM = {"key_local_agree_pct": ("keyl_agree", "keyl_disagree"),
        "key_home_agree_pct": ("key_agree", "key_disagree"),
        "root_agree_pct": ("root_agree", "root_dis"),
        "rn_agree_pct": ("rn_agree", "rn_dis")}
SENSITIVE_CASES = ("bwv352", "bwv10.7", "bwv88.7")
# the step-1 commit whose committed decode path the R1 window comparison is counted over (the dispatch's
# tritone count of 589). Read from the commit so the comparison stays reproducible after the working
# artifacts are regenerated under step-2 code.
STEP1_DECODE_REF = "c6ae08bd45"
# the named pieces of the band-miss diagnosis: the ten largest key-local LOSSES and the four largest
# GAINS between the two arms, read off fit_grading.json's per-piece counters (declared selection rule).
MECHANISM_STEMS = ("bwv331", "bwv342", "bwv88.7", "bwv434", "bwv391", "bwv9.7", "bwv244.62",
                   "bwv424", "bwv33.6", "bwv77.6", "bwv387", "bwv48.3", "bwv326", "bwv57.8")


def _adapter(table_set, weights):
    a = pd.FittedAdapter(leftover_mode=fw.LEFTOVER, table_set=table_set, weights=weights)
    a.mode_marginal("major")
    return a


def decode_and_grade(stems, adapter, pieces, vocab, cache, label, verbose=True):
    """Decode each stem with `adapter` and grade it on the robust unit. Returns per-piece duration
    counters (the bootstrap resamples pieces, so the per-piece grain is what must be kept)."""
    per_piece, timings, cad = {}, [], Counter()
    segs_of = {}
    for idx, stem in enumerate(stems):
        piece = pieces[stem]
        sig, dm = pd.piece_header(stem)
        r = pd.decode_piece(piece, adapter, vocab, cache, seg_cap=fw.SEG_CAP,
                            sig_fifths=sig, declared_mode=dm)
        timings.append(r.decode_seconds)
        if r.cadence_fires:
            cad.update(r.cadence_fires)
        segs_of[stem] = r.segments
        g = pr.grade_regions(stem, pr.decode_to_regions(piece, r, vocab, cache))
        if g is not None:
            per_piece[stem] = g
        if verbose and idx % 50 == 0:
            print(f"    [{label}] {idx + 1}/{len(stems)} {stem} {r.decode_seconds:.1f}s", flush=True)
    return {"per_piece": per_piece, "timings": timings, "cadence": dict(cad), "segments": segs_of}


def pooled(per_piece):
    g = Counter()
    for v in per_piece.values():
        g.update(v)
    out = {}
    for axis, (a, d) in _NUM.items():
        tot = g[a] + g[d]
        out[axis] = round(100.0 * g[a] / tot, 2) if tot else None
    out["_totals"] = {k: g[k] for k in sorted(g)}
    return out


def bootstrap(arms, b=BOOTSTRAP_B, seed=BOOTSTRAP_SEED):
    """Piece-level bootstrap 95 % intervals for each arm and for the PAIRED difference between the
    fitted and the identity arm (the same resampled pieces enter both, so the difference interval is
    the honest one). #24: a difference within its interval is not a finding."""
    stems = sorted(set.intersection(*[set(a["per_piece"]) for a in arms.values()]))
    rng = np.random.default_rng(seed)
    mats = {}
    for name, arm in arms.items():
        m = {}
        for axis, (a, d) in _NUM.items():
            m[axis] = np.array([[arm["per_piece"][s][a], arm["per_piece"][s][d]] for s in stems],
                               dtype=np.float64)
        mats[name] = m
    idx = rng.integers(0, len(stems), size=(b, len(stems)))
    out = {"n_pieces": len(stems), "B": b, "seed": seed, "arms": {}, "paired_delta": {}}
    draws = {}
    for name, m in mats.items():
        draws[name] = {}
        out["arms"][name] = {}
        for axis in AXES:
            num = m[axis][:, 0][idx].sum(axis=1)
            den = (m[axis][:, 0] + m[axis][:, 1])[idx].sum(axis=1)
            v = 100.0 * num / np.maximum(1.0, den)
            draws[name][axis] = v
            out["arms"][name][axis] = {"lo": round(float(np.percentile(v, 2.5)), 2),
                                       "hi": round(float(np.percentile(v, 97.5)), 2)}
    if "fitted_cv" in draws and "identity_cv" in draws:
        for axis in AXES:
            d = draws["fitted_cv"][axis] - draws["identity_cv"][axis]
            out["paired_delta"][axis] = {
                "mean": round(float(d.mean()), 2),
                "lo": round(float(np.percentile(d, 2.5)), 2),
                "hi": round(float(np.percentile(d, 97.5)), 2),
                "excludes_zero": bool(np.percentile(d, 2.5) > 0 or np.percentile(d, 97.5) < 0)}
    return out


def prune_cost(pieces, table_set, weights, vocab, cache, sample=pr.PRUNE_LOSS_SAMPLE):
    """The declared candidate prune's cost at the FITTED weights (the dispatch's re-measurement): the
    fixed sample decoded at the committed TIGHT prune and at a LOOSER one, graded identically."""
    ad = _adapter(table_set, weights)
    out = {}
    for name, (cap, topk) in (("tight", (4, 6)), ("loose", (6, 12))):
        old = pd.KEY_PRUNE_TOPK
        pd.KEY_PRUNE_TOPK = topk
        g = Counter()
        t0 = time.perf_counter()
        for stem in sample:
            p = pieces[stem]
            sig, dm = pd.piece_header(stem)
            r = pd.decode_piece(p, ad, vocab, cache, seg_cap=cap, sig_fifths=sig, declared_mode=dm)
            gg = pr.grade_regions(stem, pr.decode_to_regions(p, r, vocab, cache))
            if gg:
                g.update(gg)
        pd.KEY_PRUNE_TOPK = old
        cols = {}
        for axis, (a, d) in _NUM.items():
            tot = g[a] + g[d]
            cols[axis] = round(100.0 * g[a] / tot, 2) if tot else None
        out[name] = {"seg_cap": cap, "key_top_k": topk, "seconds": round(time.perf_counter() - t0, 1),
                     **cols}
    out["loss_pp"] = {axis: round(out["loose"][axis] - out["tight"][axis], 2) for axis in AXES}
    out["sample"] = list(sample)
    return out


def sensitive_cases(pieces, table_set, weights, vocab, cache, stems=SENSITIVE_CASES):
    """The named desk-simulation cases re-decoded under the fitted weights, reported as the committed
    reading over each case's span (§4.3 of the desk simulation; the dispatch's Task-3 item)."""
    ad = _adapter(table_set, weights)
    ad_id = _adapter(table_set, pd.identity_weights())
    rows = {}
    for stem in stems:
        p = pieces[stem]
        sig, dm = pd.piece_header(stem)
        r_f = pd.decode_piece(p, ad, vocab, cache, seg_cap=fw.SEG_CAP, sig_fifths=sig, declared_mode=dm)
        r_i = pd.decode_piece(p, ad_id, vocab, cache, seg_cap=fw.SEG_CAP, sig_fifths=sig,
                              declared_mode=dm)

        def reading(res, tick):
            for s in res.segments:
                if s["start_tick"] <= tick < s["end_tick"]:
                    return {"span": [s["start_tick"], s["end_tick"]], "key": s["key"],
                            "class": s["class_key"], "root_pc": s["root_pc"]}
            return None
        gf = pr.grade_regions(stem, pr.decode_to_regions(p, r_f, vocab, cache))
        gi = pr.grade_regions(stem, pr.decode_to_regions(p, r_i, vocab, cache))

        def cols(g):
            return {axis: (round(100.0 * g[a] / (g[a] + g[d]), 1) if (g[a] + g[d]) else None)
                    for axis, (a, d) in _NUM.items()} if g else None
        rows[stem] = {
            "n_segments_fitted": len(r_f.segments), "n_segments_identity": len(r_i.segments),
            "columns_fitted": cols(gf), "columns_identity": cols(gi),
            "reading_at_probe_tick": {
                "tick": {"bwv352": 1440, "bwv10.7": 36000, "bwv88.7": 0}.get(stem, 0),
                "fitted": reading(r_f, {"bwv352": 1440, "bwv10.7": 36000, "bwv88.7": 0}.get(stem, 0)),
                "identity": reading(r_i, {"bwv352": 1440, "bwv10.7": 36000, "bwv88.7": 0}.get(stem, 0)),
            },
        }
    return rows


def cadence_window_report(write=True, verbose=True):
    """★R1's isolated effect. Over the SAME committed decode path (probe_corpus_decode.json — the
    step-1 identity-weight decode, whose boundaries do not move because the cadence weights were zero
    there), recount every cadence feature under the SUPERSEDED single-event approach window and under
    the ruled four-beat window. Same boundaries, same keys, one definition changed — so the difference
    is the ruling's effect and nothing else. The old tritone count is the dispatch's 589."""
    pieces, _prov = pd.load_pieces()
    # read the step-1 decode path from the COMMIT, not from the working tree: the working copy is
    # regenerated under step-2 code, and this report must stay reproducible against the exact path the
    # dispatch's "589" was counted over.
    blob = subprocess.run(["git", "-C", str(_ROOT), "show",
                           f"{STEP1_DECODE_REF}:tools/joint_estimator/probe_corpus_decode.json"],
                          capture_output=True, text=True, encoding="utf-8")
    if blob.returncode != 0:
        raise SystemExit(f"STOP: cannot read the step-1 decode path from {STEP1_DECODE_REF}: "
                         f"{blob.stderr[:300]}")
    dec = json.loads(blob.stdout)
    old, new = Counter(), Counter()
    per_piece = {}
    for stem, rec in dec["pieces"].items():
        piece = pieces[stem]
        o, n = Counter(), Counter()
        for si, s in enumerate(rec["segments"]):
            if si == 0:
                continue
            i, tonic, is_major = s["i"], s["tonic_pc"], s["is_major"]
            ap = piece.notes_by_event[i - 1]
            ar = piece.notes_by_event[i]
            ap_pcs = {x[pd.N_PC] for x in ap}
            ar_pcs = {x[pd.N_PC] for x in ar}
            fc = pd._fermata_cadence_ctx(piece, i)
            f_old = pd.cadence_features(ap_pcs, pd.event_bass_pc(ap), ar_pcs, pd.event_bass_pc(ar),
                                        tonic, is_major, fc, window_pcs=None)
            f_new = pd.cadence_features(ap_pcs, pd.event_bass_pc(ap), ar_pcs, pd.event_bass_pc(ar),
                                        tonic, is_major, fc,
                                        window_pcs=piece.approach_window_pcs(i))
            o["boundaries"] += 1
            n["boundaries"] += 1
            for f in pd.CADENCE_FEATURES:
                o[f] += int(f_old[f])
                n[f] += int(f_new[f])
            o["any_fire"] += int(any(f_old.values()))
            n["any_fire"] += int(any(f_new.values()))
        old.update(o)
        new.update(n)
        per_piece[stem] = {"old": dict(o), "new": dict(n)}
    out = {"provenance": {
        "generator": glt._rel(Path(__file__)) + ":cadence_window_report",
        "instrument_commit": glt._git_head(),
        "path": (f"the step-1 identity-weight decode path committed at {STEP1_DECODE_REF} "
                 "(probe_corpus_decode.json, read from that commit); the "
                 "boundaries are identical under both windows because the step-1 cadence weights "
                 "were all zero, so this isolates the feature-definition change"),
        "ruling": ("R1 = W1 (user, 2026-07-19): the tritone-pair approach window is the four beats "
                   "strictly before the boundary event, within the piece, voice-agnostic, both "
                   f"degrees sounding anywhere in the window. Four beats = "
                   f"{pd.CADENCE_APPROACH_TICKS} ticks at {pd.TICKS_PER_QUARTER} ticks/quarter-beat "
                   "(the corpus-wide beat convention of these instruments)."),
        "superseded": "single-event approach (the step-1 declared under-specification)"},
        "single_event_window": dict(old), "four_beat_window": dict(new),
        "delta": {k: new[k] - old[k] for k in sorted(set(old) | set(new))},
        "fire_rate_per_boundary": {
            "single_event": {f: round(old[f] / max(1, old["boundaries"]), 4)
                             for f in pd.CADENCE_FEATURES},
            "four_beat": {f: round(new[f] / max(1, new["boundaries"]), 4)
                          for f in pd.CADENCE_FEATURES}},
        "per_piece": per_piece}
    if write:
        (_HERE / "cadence_window_report.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
    if verbose:
        print(f"cadence window (R1): over {new['boundaries']} committed boundaries")
        for f in pd.CADENCE_FEATURES:
            print(f"  {f:22s} single-event {old[f]:6d}  ->  four-beat {new[f]:6d}  "
                  f"({new[f] - old[f]:+d})")
    return out


def deceptive_cadence_check(weights, verbose=True):
    """The third sensitive case the dispatch names — the DECEPTIVE cadence (the desk simulation's S5
    trace, whose verdict 'the deceptive resolution stays in the key' rested on the cadence credit).
    Re-run S5 through the desk simulation's own ratified arithmetic with ONE thing swapped: the injected
    provisional cadence weights (+0.9 / +0.7 / +0.7) replaced by the FITTED ones. Everything else — the
    injected tables, the hypotheses, the inclusion rules — is the ratified desk-sim setup, so the
    reported margin change is the fit's effect on that verdict and nothing else."""
    import probe_desksim as ds

    class _FittedCadence(ds.ProvisionalAdapter):
        def cadence_weights(self):
            return {f: float(weights[pd.CADENCE_WEIGHT_OF[f]]) for f in pd.CADENCE_FEATURES}

    cache = pd.ChordCache()
    case = {c.name: c for c in ds.build_cases()}["S5"]
    out = {"case": "S5 (deceptive cadence V7 -> vi in C major)", "notes": case.notes,
           "desk_sim_expected": case.expected, "arms": {}}
    for label, ad in (("desk_sim_provisional_weights", ds.ProvisionalAdapter()),
                      ("fitted_weights", _FittedCadence())):
        vals = {}
        for hyp_label, hyp in case.hyps.items():
            bd = pd.score_hypothesis(case.piece, hyp, ad, cache, case.sig_fifths, case.declared_mode)
            vals[hyp_label] = round(ds._sum_included(bd, case.include, case.key_trans_stays,
                                                     case.drop_prefix), 4)
        order = sorted(vals.items(), key=lambda kv: -kv[1])
        out["arms"][label] = {"scores": vals, "winner": order[0][0],
                              "margin": round(order[0][1] - order[1][1], 4),
                              "cadence_weights": ad.cadence_weights()}
    out["verdict_preserved"] = (out["arms"]["fitted_weights"]["winner"]
                                == out["arms"]["desk_sim_provisional_weights"]["winner"])
    if verbose:
        for k, v in out["arms"].items():
            print(f"  S5 [{k}] winner {v['winner']} margin {v['margin']:+.2f}")
    return out


def mechanism_report(write=True, verbose=True, stems=None):
    """THE BAND-MISS DIAGNOSIS (dispatch Task 3: 'a prominently-reported finding with named-piece
    diagnosis'). Read-only; it adjusts nothing.

    Only the RELATIVE weights decide a decode — scaling every weight by a constant is a temperature
    change that leaves the arg-max path untouched. Reported against the emission weight, the fit
    up-weights the key-transition and boundary factors and down-weights bass and chord-transition. The
    key-transition table's stay cell is the overwhelmingly probable one, so up-weighting it makes
    staying cheaper relative to the per-tone evidence that argues for a modulation. This measures the
    consequence directly: committed segments, key CHANGES, distinct keys, and the duration fraction in
    the single most-committed key, identity vs fitted, on the named largest-movement pieces."""
    wf = json.loads(WEIGHT_FIT.read_text(encoding="utf-8"))
    W = wf["all"]["weights"]
    pieces, _prov = pd.load_pieces()
    stems = list(stems or MECHANISM_STEMS)
    rel = {k: (W[k] / W["emission"]) for k in pd.GENERATIVE_WEIGHTS}
    rows = {}
    tot = {"identity": 0, "fitted": 0}
    for stem in stems:
        p = pieces[stem]
        sig, dm = pd.piece_header(stem)
        rec = {}
        for name, wts in (("identity", pd.identity_weights()), ("fitted", W)):
            ad = _adapter("all", wts)
            voc = pd.Vocabulary(ad.tables)
            r = pd.decode_piece(p, ad, voc, pd.ChordCache(), seg_cap=fw.SEG_CAP,
                                sig_fifths=sig, declared_mode=dm)
            keys = [(s["tonic_pc"], s["is_major"]) for s in r.segments]
            durs = [s["end_tick"] - s["start_tick"] for s in r.segments]
            by_key = Counter()
            for k, d in zip(keys, durs):
                by_key[k] += d
            chg = sum(1 for a, b in zip(keys, keys[1:]) if a != b)
            rec[name] = {"segments": len(r.segments), "key_changes": chg,
                         "distinct_keys": len(set(keys)),
                         "largest_key_duration_fraction": round(max(by_key.values())
                                                                / max(1, sum(by_key.values())), 3)}
            tot[name] += chg
        rows[stem] = rec
        if verbose:
            i, f = rec["identity"], rec["fitted"]
            print(f"  {stem:11s} identity segs {i['segments']:3d} keychg {i['key_changes']:2d} "
                  f"keys {i['distinct_keys']:2d} homefrac {i['largest_key_duration_fraction']:.2f}"
                  f"   ->  fitted segs {f['segments']:3d} keychg {f['key_changes']:2d} "
                  f"keys {f['distinct_keys']:2d} homefrac {f['largest_key_duration_fraction']:.2f}")
    out = {
        "provenance": {
            "generator": glt._rel(Path(__file__)) + ":mechanism_report",
            "instrument_commit": glt._git_head(),
            "purpose": ("the named-piece diagnosis of the fitted arm's key-axis band miss; read-only, "
                        "adjusts nothing"),
            "sample": ("the largest key-local movers between the two arms, taken from "
                       "fit_grading.json's per-piece counters — declared, not cherry-picked"),
            "tables": "all-326 (the publishable model), both arms, so only the weights differ",
        },
        "relative_weights_vs_emission": {k: round(v, 3) for k, v in rel.items()},
        "per_piece": rows,
        "total_key_changes": {**tot,
                              "relative_change_pct": round(100.0 * (tot["fitted"] - tot["identity"])
                                                           / max(1, tot["identity"]), 1)},
    }
    if write:
        (_HERE / "fit_mechanism_report.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
    if verbose:
        print(f"  total key changes: identity {tot['identity']} -> fitted {tot['fitted']} "
              f"({out['total_key_changes']['relative_change_pct']:+.0f}%)")
    return out


def main(argv):
    verbose = True
    if argv and argv[0] == "window":
        return cadence_window_report()
    if argv and argv[0] == "mechanism":
        return mechanism_report()
    wf = json.loads(WEIGHT_FIT.read_text(encoding="utf-8"))
    pieces, ne, covered, fold_of, prov = fw.load_corpus()
    t_all = time.perf_counter()

    arms = {"fitted_cv": {"per_piece": {}, "timings": [], "cadence": Counter(), "segments": {}},
            "identity_cv": {"per_piece": {}, "timings": [], "cadence": Counter(), "segments": {}}}
    for fold in range(fw.N_FOLDS):
        rec = wf["folds"][str(fold)]
        stems = [s for s in covered if fold_of[s] == fold]
        ts_name = f"fold{fold}"
        vocab_cache = pd.ChordCache()
        for arm, wts in (("fitted_cv", rec["weights"]), ("identity_cv", pd.identity_weights())):
            ad = _adapter(ts_name, wts)
            voc = pd.Vocabulary(ad.tables)
            res = decode_and_grade(stems, ad, pieces, voc, vocab_cache, f"{arm} f{fold}", verbose)
            arms[arm]["per_piece"].update(res["per_piece"])
            arms[arm]["timings"].extend(res["timings"])
            arms[arm]["cadence"].update(res["cadence"])
            arms[arm]["segments"].update(res["segments"])

    # the publishable all-326 model — reported BESIDE the CV headline, never in its place
    ad_all = _adapter("all", wf["all"]["weights"])
    voc_all = pd.Vocabulary(ad_all.tables)
    cache_all = pd.ChordCache()
    all_arm = decode_and_grade(sorted(covered), ad_all, pieces, voc_all, cache_all, "all326", verbose)

    cols = {name: pooled(a["per_piece"]) for name, a in arms.items()}
    cols["all326_publishable"] = pooled(all_arm["per_piece"])
    ci = bootstrap({k: arms[k] for k in ("fitted_cv", "identity_cv")})

    verdicts = {}
    for axis, (lo, hi) in PREDICTION_BANDS.items():
        v = cols["fitted_cv"][axis]
        verdicts[axis] = {"band": [lo, hi], "measured": v,
                          "holds": bool(v is not None and lo <= v <= hi),
                          "vs_step1_identity_pp": (round(v - STEP1_IDENTITY[axis], 2)
                                                   if v is not None else None)}

    out = {
        "provenance": {
            "generator": glt._rel(Path(__file__)),
            "instrument_commit": glt._git_head(),
            "weight_fit_artifact": glt._rel(WEIGHT_FIT),
            "note_events_git_hash": prov["corpus_git_hash"],
            "decoder": "probe_decoder.decode_piece (weight-aware; the ratified factorization)",
            "grading": ("a8_rebaseline_measure.build_piece_grid (pinned, read-only) vs "
                        "dcml_parser.load_wir_regions (the OI-142-corrected substrate) — the same "
                        "chain the committed baselines are measured with"),
            "held_out_discipline": ("each piece is decoded exactly once, by the model (tables AND "
                                    "weights) fitted on the complement of ITS fold; the fold of every "
                                    "piece is recorded below"),
            "identity_weights_note": ("the ablation arm: every generative weight 1.0, every cadence "
                                      "weight 0.0 — a cadence feature is an indicator, not a "
                                      "log-probability, so the generative product gives it no weight"),
            "cadence_window": (f"tritone-pair approach window = {pd.CADENCE_APPROACH_BEATS} beats "
                               f"({pd.CADENCE_APPROACH_TICKS} ticks) — user ruling R1 (W1)"),
            "bootstrap": {"B": BOOTSTRAP_B, "seed": BOOTSTRAP_SEED, "level": "95%",
                          "unit": "piece (resampled with replacement); paired across arms"},
        },
        "fold_of_piece": {s: fold_of[s] for s in sorted(covered)},
        "columns": cols,
        "confidence_intervals": ci,
        "committed_baselines": pr.BASELINES,
        "step1_identity_columns": STEP1_IDENTITY,
        "prediction_verdicts": verdicts,
        "weights": {"per_fold": {k: v["weights"] for k, v in wf["folds"].items()},
                    "all326": wf["all"]["weights"],
                    "lambda_selected": {k: v["lambda_selected"] for k, v in wf["folds"].items()}},
        "cadence_fires": {"fitted_cv": dict(arms["fitted_cv"]["cadence"]),
                          "identity_cv": dict(arms["identity_cv"]["cadence"])},
        "timing": {name: {"mean_s": round(float(np.mean(a["timings"])), 3),
                          "max_s": round(float(np.max(a["timings"])), 3),
                          "total_s": round(float(np.sum(a["timings"])), 1)}
                   for name, a in list(arms.items()) + [("all326", all_arm)]},
        "sensitive_cases": sensitive_cases(pieces, "all", wf["all"]["weights"], voc_all, cache_all),
        "deceptive_cadence_case": deceptive_cadence_check(wf["all"]["weights"]),
        "prune_cost_at_fitted_weights": prune_cost(pieces, "all", wf["all"]["weights"], voc_all,
                                                   cache_all),
        "per_piece": {name: {s: {k: int(v) for k, v in g.items()}
                             for s, g in a["per_piece"].items()} for name, a in arms.items()},
        "wall_seconds": round(time.perf_counter() - t_all, 1),
    }
    OUT_JSON.write_text(json.dumps(out, indent=1), encoding="utf-8")
    write_summary(out, wf)
    print(f"\nwrote {glt._rel(OUT_JSON)} and {glt._rel(OUT_SUMMARY)}")
    return out


def write_summary(g, wf):
    c, ci = g["columns"], g["confidence_intervals"]
    L = ["=== the weight fit — held-out measurement (algorithm-completion step 2) ===",
         f"instrument_commit {g['provenance']['instrument_commit']}",
         f"weight fit {g['provenance']['weight_fit_artifact']}   "
         f"note_events {g['provenance']['note_events_git_hash']}",
         f"cadence window: {g['provenance']['cadence_window']}",
         f"bootstrap: {g['provenance']['bootstrap']}",
         "",
         "THE HEADLINE — pooled 5-fold cross-validated decode (each piece decoded once, by the model",
         "fitted on the complement of its own fold), with piece-level bootstrap 95% intervals.",
         "",
         f"{'axis':16s} {'FITTED (CV)':22s} {'IDENTITY (CV)':22s} {'paired delta':22s} {'step1':7s} {'current B/J/D'}",
         "-" * 118]
    bl = {"key_local_agree_pct": "key_local", "key_home_agree_pct": "key_home",
          "root_agree_pct": "root", "rn_agree_pct": "rn"}
    nm = {"key_local_agree_pct": "key vs LOCAL", "key_home_agree_pct": "key vs HOME",
          "root_agree_pct": "chord root", "rn_agree_pct": "Roman numeral"}
    for axis in AXES:
        f_i = ci["arms"]["fitted_cv"][axis]
        i_i = ci["arms"]["identity_cv"][axis]
        d = ci["paired_delta"][axis]
        b = g["committed_baselines"][bl[axis]]
        L.append(f"{nm[axis]:16s} "
                 f"{c['fitted_cv'][axis]!s:6s} [{f_i['lo']:.2f},{f_i['hi']:.2f}]  "
                 f"{c['identity_cv'][axis]!s:6s} [{i_i['lo']:.2f},{i_i['hi']:.2f}]  "
                 f"{d['mean']:+6.2f} [{d['lo']:+.2f},{d['hi']:+.2f}]  "
                 f"{g['step1_identity_columns'][axis]:6.2f}  "
                 f"{b['Baroque']}/{b['Jazz']}/{b['Default']}")
    L += ["", "prediction verdicts (Cowork's bands, written before measuring):"]
    for axis in AXES:
        v = g["prediction_verdicts"][axis]
        L.append(f"  {nm[axis]:16s} band {v['band'][0]}-{v['band'][1]}  measured {v['measured']}  "
                 f"{'HOLDS' if v['holds'] else '*** OUTSIDE BAND ***'}  "
                 f"(vs step-1 identity {v['vs_step1_identity_pp']:+.2f}pp)")
    L += ["", f"publishable all-326 model (BESIDE the headline, not in its place): "
              + "  ".join(f"{nm[a]} {c['all326_publishable'][a]}" for a in AXES)]
    L += ["", "THE FITTED WEIGHTS (per fold, and the all-326 publishable model):", ""]
    L.append(f"{'weight':26s} " + " ".join(f"{'f' + k:>8s}" for k in sorted(g["weights"]["per_fold"]))
             + f" {'all326':>9s}")
    L.append("-" * 96)
    for n in fw.W_NAMES:
        row = " ".join(f"{g['weights']['per_fold'][k][n]:8.3f}"
                       for k in sorted(g["weights"]["per_fold"]))
        L.append(f"{n:26s} {row} {g['weights']['all326'][n]:9.3f}")
    L.append(f"{'lambda (inner-validated)':26s} "
             + " ".join(f"{g['weights']['lambda_selected'][k]:8.4g}"
                        for k in sorted(g["weights"]["per_fold"])))
    cf = g["cadence_fires"]
    L += ["", f"cadence fires on the committed path — fitted: {cf['fitted_cv']}",
          f"                                     identity: {cf['identity_cv']}"]
    L += ["", "timings (decode seconds per piece): "
          + "  ".join(f"{k}: mean {v['mean_s']} max {v['max_s']}" for k, v in g["timing"].items())]
    pc = g["prune_cost_at_fitted_weights"]
    L += ["", f"-- the declared prune's cost AT THE FITTED WEIGHTS ({len(pc['sample'])}-piece sample) --",
          f"  tight(seg_cap {pc['tight']['seg_cap']}, topK {pc['tight']['key_top_k']}): "
          + "  ".join(f"{nm[a]} {pc['tight'][a]}" for a in AXES),
          f"  loose(seg_cap {pc['loose']['seg_cap']}, topK {pc['loose']['key_top_k']}): "
          + "  ".join(f"{nm[a]} {pc['loose'][a]}" for a in AXES),
          "  LOSS: " + "  ".join(f"{nm[a]} {pc['loss_pp'][a]:+.2f}pp" for a in AXES)]
    dc = g.get("deceptive_cadence_case")
    if dc:
        L += ["", f"-- the deceptive-cadence case ({dc['case']}) --",
              f"  desk-sim provisional cadence weights: winner "
              f"{dc['arms']['desk_sim_provisional_weights']['winner']} margin "
              f"{dc['arms']['desk_sim_provisional_weights']['margin']:+.2f}",
              f"  FITTED cadence weights:               winner "
              f"{dc['arms']['fitted_weights']['winner']} margin "
              f"{dc['arms']['fitted_weights']['margin']:+.2f}",
              f"  verdict preserved: {dc['verdict_preserved']}"]
    L += ["", "-- the desk-simulation sensitive cases under the fitted weights --"]
    for stem, r in g["sensitive_cases"].items():
        L.append(f"  {stem}: segments {r['n_segments_identity']} (identity) -> "
                 f"{r['n_segments_fitted']} (fitted)")
        L.append(f"     columns fitted   {r['columns_fitted']}")
        L.append(f"     columns identity {r['columns_identity']}")
        rd = r["reading_at_probe_tick"]
        L.append(f"     at tick {rd['tick']}: fitted {rd['fitted']}")
        L.append(f"                    identity {rd['identity']}")
    L += ["", "-- the fit's own record (from weight_fit.json) --"]
    est = wf.get("establishment", {})
    if est:
        L.append(f"  lattice max-plus == decoder Viterbi: max|delta| "
                 f"{est.get('viterbi_parity', {}).get('max_abs_delta')}  "
                 f"({'PASS' if est.get('viterbi_parity', {}).get('pass') else 'FAIL'})")
        L.append(f"  forward logZ == backward logZ: max|delta| "
                 f"{est.get('forward_backward', {}).get('max_abs_fb_delta')}; "
                 f"ground-truth path inside Z: {est.get('forward_backward', {}).get('gt_within_Z')}")
        L.append(f"  analytic gradient vs finite differences: max|diff| "
                 f"{est.get('gradient', {}).get('max_abs_diff')}  "
                 f"({'PASS' if est.get('gradient', {}).get('pass') else 'FAIL'})")
    for k in sorted(wf["folds"]):
        r = wf["folds"][k]
        ff = r["final_fit"]
        L.append(f"  fold{k}: lambda {r['lambda_selected']:g}  objective "
                 f"{ff['objective_start']:.5f} -> {ff['objective_end']:.5f}  |grad| "
                 f"{ff['grad_norm_end']:.2e}  evals {ff['n_objective_evals']}  "
                 f"monotone {ff['monotone_decrease']}  {ff['status'][:40]}")
    con = wf["all"]["construction"]
    L += ["", "-- ground-truth path construction (all-326 build) --",
          f"  stems used {con.get('stems_used')} (flagged excluded {con.get('stems_excluded_flagged')}); "
          f"units {con.get('units')} of which resuming {con.get('resuming_units')}",
          f"  labeled events {con.get('labeled')}; anacrusis {con.get('anacrusis')}; "
          f"misaligned-span left-out {con.get('misaligned_span_left_out')}; "
          f"no-GT-span {con.get('no_gt_span')}; class outside vocabulary "
          f"{con.get('class_outside_vocabulary', 0)}",
          f"  ground-truth segments {con.get('gt_segments')} "
          f"(of which {con.get('gt_segments_from_cap_split')} produced by the segment-cap split)",
          f"  lattice augmentation: key widened on {con.get('aug_key_widened_spans')} spans, "
          f"state force-added on {con.get('aug_state_forced_spans')} spans, of "
          f"{con.get('candidates')} candidates",
          f"  ground-truth transitions through leftover mass: chord "
          f"{con.get('gtprov_chord_leftover', 0)} of "
          f"{con.get('gtprov_chord_leftover', 0) + con.get('gtprov_chord_cell', 0)}; entry "
          f"{con.get('gtprov_entry_leftover', 0)} of "
          f"{con.get('gtprov_entry_leftover', 0) + con.get('gtprov_entry_cell', 0)}"]
    OUT_SUMMARY.write_text("\n".join(L) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1:])
