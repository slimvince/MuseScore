#!/usr/bin/env python3
"""search_run.py — THE DIRECT-METRIC SEARCH'S MEASUREMENT SIDE (Task 2 of the ratified fallback's
dispatch, `cc_instruction_direct_metric_search.md`).

★ THE FIREWALL'S DOWNSTREAM HALF. `search_direct.py` runs the search and consults R only on TRAINING
folds; it never builds a held-out stem list. THIS module reads the FROZEN per-start optima from
`weight_search.json`, SELECTS each fold's optimum by best TRAINING R (never by anything measured
here), evaluates each held-out fold exactly once with it, and feeds nothing back. Nothing in this
module adjusts a weight, a table, a threshold or a prune.

WHAT IT MEASURES (the dispatch's Task 2):
  1. the pooled 5-fold CROSS-VALIDATED decode of the direct-search arm on the robust unit, each piece
     decoded once by the model (tables AND weights) fitted on the complement of ITS fold, with
     piece-level bootstrap 95 % intervals (#24), paired against the identity and likelihood arms;
  2. the identity-weight generative baseline and the likelihood-fit arm through the SAME folds —
     recomputed here through this module's own path and REQUIRED to reproduce the committed
     `fit_grading.json` per-piece counters exactly (that reproduction is what establishes this
     harness, #19/#16 — an unreproduced arm is a STOP);
  3. the publishable all-326 model, reported BESIDE the CV headline, never in its place;
  4. the verdicts against the dispatch's written prediction bands (#17b);
  5. the STABILITY record: the spread of the 21 converged optima's training objectives per fold, and —
     as a clearly-labelled diagnostic that entered NO selection — their held-out results;
  6. the weight reading, the cadence-feature question (the OI-190 watch), the three sensitive cases,
     the modulation-rate check (the OI-187 mechanism must not reappear), the prune cost at the
     selected weights (OI-188), and timings.

REUSE (#6): the decode is `probe_decoder.decode_piece` (pinned) for every graded arm; the grading is
`probe_run.decode_to_regions` / `probe_run.grade_regions`; the confidence intervals, the sensitive
cases, the deceptive-cadence check and the prune cost are `fit_run`'s own functions. The fast
cached-lattice decode of `search_direct` is used ONLY for the per-start stability diagnostic (6 825
decodes), and only after it is re-established against `decode_piece` at the actual selected weights.
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

import probe_decoder as pd            # noqa: E402
import probe_run as pr                # noqa: E402
import fit_weights as fw              # noqa: E402
import fit_run as fr                  # noqa: E402  pooled / bootstrap / sensitive_cases / prune_cost
import search_direct as sd            # noqa: E402
import gen_label_tables as glt        # noqa: E402
import dcml_parser as dcml            # noqa: E402  (the ground-truth substrate, for the modulation rate)

SEARCH_ARTIFACT = _HERE / "weight_search.json"
FIT_GRADING = _HERE / "fit_grading.json"
OUT_JSON = _HERE / "search_grading.json"
OUT_SUMMARY = _HERE / "search_grading_summary.txt"

# the dispatch's written predictions for the DIRECT-SEARCH arm (Cowork, #17b — recorded before measuring)
PREDICTION_BANDS = {"key_local_agree_pct": (74.0, 82.0), "key_home_agree_pct": (57.0, 68.0),
                    "root_agree_pct": (72.0, 77.0), "rn_agree_pct": (59.0, 66.0)}
AXES = fr.AXES
_NUM = fr._NUM


def select_optimum(starts):
    """★ THE SELECTION RULE — best TRAINING objective, ties broken by the lower start index. Nothing
    measured in this module is consulted. Stated as one function so the rule is grep-visible."""
    return min(starts, key=lambda s: (s["R_train"], s["start_index"]))


def decode_and_grade(stems, weights, table_set, pieces, label, verbose=True):
    """One graded arm: the PINNED decode, the PINNED grading, per-piece duration counters."""
    ad = fr._adapter(table_set, weights)
    voc = pd.Vocabulary(ad.tables)
    cache = pd.ChordCache()
    per_piece, timings, cad, segs_of = {}, [], Counter(), {}
    for idx, stem in enumerate(stems):
        piece = pieces[stem]
        sig, dm = pd.piece_header(stem)
        r = pd.decode_piece(piece, ad, voc, cache, seg_cap=fw.SEG_CAP,
                            sig_fifths=sig, declared_mode=dm)
        timings.append(r.decode_seconds)
        if r.cadence_fires:
            cad.update(r.cadence_fires)
        segs_of[stem] = r.segments
        g = pr.grade_regions(stem, pr.decode_to_regions(piece, r, voc, cache))
        if g is not None:
            per_piece[stem] = g
        if verbose and idx % 40 == 0:
            print(f"    [{label}] {idx + 1}/{len(stems)} {stem} {r.decode_seconds:.1f}s", flush=True)
    return {"per_piece": per_piece, "timings": timings, "cadence": dict(cad), "segments": segs_of}


def reproduce_check(name, arm, committed):
    """An arm recomputed here must reproduce the committed fit_grading.json counters EXACTLY. This is
    what establishes the harness (#19) and the reproducibility of the committed figures (#16)."""
    ours = {s: {k: int(v) for k, v in g.items()} for s, g in arm["per_piece"].items()}
    theirs = {s: {k: int(v) for k, v in g.items()} for s, g in committed.items()}
    same_stems = set(ours) == set(theirs)
    diffs = [s for s in sorted(set(ours) & set(theirs)) if ours[s] != theirs[s]]
    return {"arm": name, "stems_identical": bool(same_stems), "n_pieces": len(ours),
            "pieces_differing": diffs[:20], "n_pieces_differing": len(diffs),
            "pass": bool(same_stems and not diffs)}


def gt_modulation_rate(stems):
    """The ground truth's own local-key change count per piece, from the SAME substrate the grading
    uses (`dcml_parser.load_wir_regions`, the OI-142-corrected one). The OI-187 mechanism was a decode
    that stopped modulating; this is the quantity that detects its return."""
    out = {}
    for stem in stems:
        regs = dcml.load_wir_regions(pr.WIR_DIR, stem)
        if not regs:
            continue
        keys = [getattr(r, "local_key", None) for r in regs]
        out[stem] = int(sum(1 for a, b in zip(keys, keys[1:]) if a != b and b is not None))
    return out


def decode_modulation_rate(segments_of):
    out = {}
    for stem, segs in segments_of.items():
        ks = [(s["tonic_pc"], s["is_major"]) for s in segs]
        out[stem] = int(sum(1 for a, b in zip(ks, ks[1:]) if a != b))
    return out


def stability_heldout(search, pieces, covered, fold_of, verbose=True):
    """★ A DIAGNOSTIC, NOT A SELECTION INPUT. The dispatch asks for the converged optima's held-out
    results beside their training objectives, as the published protocol's substitute for a convexity
    proof. It is computed AFTER the headline selection is fixed by `select_optimum` on the training
    objective, and no number here can move that selection. Run through the cached-lattice decode
    (established identical to the pinned decoder), because 21 x 5 optima x 65 held-out pieces is 6 825
    decodes — 2 minutes this way, 5.5 hours through `decode_piece`."""
    rows = {}
    for fold in range(fw.N_FOLDS):
        fl = f"fold{fold}"
        if fl not in search["fits"]:
            continue
        ts = fw.TableSet(fl)
        held = sorted(s for s in covered if fold_of[s] == fold)
        store = sd.PieceStore(held, ts, pieces)
        per_start = []
        for st in sorted(search["fits"][fl]["starts"], key=lambda s: s["start_index"]):
            g = sd.grade_stems(store, np.array(st["x"], dtype=np.float64))
            per_start.append({"start_index": st["start_index"], "start_name": st["start_name"],
                              "R_train": st["R_train"],
                              "heldout_columns": {k: (round(v, 2) if v is not None else None)
                                                  for k, v in g["columns"].items()},
                              "heldout_R": round(g["R"], 6)})
        rows[fl] = {"n_heldout_pieces": len(held), "per_start": per_start}
        if verbose:
            rs = [p["R_train"] for p in per_start]
            print(f"    [stability] {fl}: {len(per_start)} starts, R_train "
                  f"min {min(rs):.6f} max {max(rs):.6f} spread {max(rs) - min(rs):.6f}", flush=True)
        del ts, store
    return rows


def establish_at_selected(pieces, search, covered, fold_of, verbose=True):
    """Before the stability diagnostic is allowed to use the cached-lattice decode, re-establish it at
    the ACTUAL operating point: the per-fold SELECTED weights, on a named sample of that fold's
    held-out pieces. Establishment at identity and at random draws was done in the search; this is the
    check at the point the report will stand on."""
    rows, bad = [], 0
    for fold in range(fw.N_FOLDS):
        fl = f"fold{fold}"
        if fl not in search["fits"]:
            continue
        ts = fw.TableSet(fl)
        sel = select_optimum(search["fits"][fl]["starts"])
        x = np.array(sel["x"], dtype=np.float64)
        wd = fw.vec_to_weights(x)
        mc = sd.MaxContext(ts, x)
        held = sorted(s for s in covered if fold_of[s] == fold)[:4]
        for stem in held:
            piece = pieces[stem]
            sig, dm = pd.piece_header(stem)
            ad = pd.FittedAdapter(leftover_mode=fw.LEFTOVER, table_set=fl, weights=wd)
            ad._mode_marginal = ts.adapter._mode_marginal
            r = pd.decode_piece(piece, ad, ts.vocab, ts.cache, seg_cap=fw.SEG_CAP,
                                sig_fifths=sig, declared_mode=dm)
            lat = fw.build_unit(piece, stem, 0, len(piece.events), True, None, ts, sig, dm,
                                augment_gt=False)
            sc, segs = sd.maxplus_decode(lat, ts, mc)
            got = sd.segments_to_dicts(lat, piece, segs, ts)
            k = lambda ss: [(s["i"], s["j"], s["tonic_pc"], s["is_major"], s["class_key"]) for s in ss]
            ok = abs(sc - r.total_score) < 1e-9 and k(r.segments) == k(got)
            bad += (not ok)
            rows.append({"fold": fold, "stem": stem, "score_delta": round(sc - r.total_score, 12),
                         "path_identical": bool(ok)})
        del ts
    if verbose:
        print(f"    [establish@selected] {len(rows)} checks, {bad} mismatches", flush=True)
    return {"rows": rows, "n_checks": len(rows), "mismatches": int(bad), "pass": bool(bad == 0)}


def main(argv):
    verbose = True
    t_all = time.perf_counter()
    search = json.loads(SEARCH_ARTIFACT.read_text(encoding="utf-8"))
    committed = json.loads(FIT_GRADING.read_text(encoding="utf-8"))
    wf = json.loads((_HERE / "weight_fit.json").read_text(encoding="utf-8"))
    pieces, ne, covered, fold_of, prov = fw.load_corpus()

    counts = {fl: len(rec["starts"]) for fl, rec in search["fits"].items()}
    missing = {fl: n for fl, n in counts.items() if n != sd.N_STARTS}
    if missing:
        raise SystemExit(f"STOP: incomplete search artifact, starts per fit {missing} "
                         f"(expected {sd.N_STARTS} each) — a part is missing or a process died")

    # ── the per-fold selection, on the TRAINING objective alone ──
    selected = {}
    for fold in range(fw.N_FOLDS):
        fl = f"fold{fold}"
        sel = select_optimum(search["fits"][fl]["starts"])
        selected[fl] = sel
        if verbose:
            print(f"  {fl}: selected start {sel['start_index']} ({sel['start_name']}) "
                  f"R_train={sel['R_train']:.6f}", flush=True)
    sel_all = select_optimum(search["fits"]["all"]["starts"])

    # ── the three graded CV arms, all through the pinned decode ──
    arms = {k: {"per_piece": {}, "timings": [], "cadence": Counter(), "segments": {}}
            for k in ("direct_cv", "identity_cv", "likelihood_cv")}
    for fold in range(fw.N_FOLDS):
        fl = f"fold{fold}"
        stems = sorted(s for s in covered if fold_of[s] == fold)
        for arm, wts in (("direct_cv", selected[fl]["weights"]),
                         ("identity_cv", pd.identity_weights()),
                         ("likelihood_cv", wf["folds"][str(fold)]["weights"])):
            res = decode_and_grade(stems, wts, fl, pieces, f"{arm} f{fold}", verbose)
            for k in ("per_piece", "cadence", "segments"):
                arms[arm][k].update(res[k])
            arms[arm]["timings"].extend(res["timings"])

    # ── the establishment: the two committed arms must reproduce EXACTLY ──
    repro = [reproduce_check("identity_cv", arms["identity_cv"], committed["per_piece"]["identity_cv"]),
             reproduce_check("likelihood_cv", arms["likelihood_cv"], committed["per_piece"]["fitted_cv"])]
    for r in repro:
        if not r["pass"]:
            raise SystemExit(f"STOP: the recomputed {r['arm']} arm does not reproduce the committed "
                             f"fit_grading.json ({r['n_pieces_differing']} pieces differ) — the "
                             f"harness is not established (#19)")
    if verbose:
        print("  establishment: both committed arms reproduced exactly", flush=True)

    # ── the publishable all-326 model, beside the headline ──
    all_arm = decode_and_grade(sorted(covered), sel_all["weights"], "all", pieces, "all326", verbose)

    cols = {name: fr.pooled(a["per_piece"]) for name, a in arms.items()}
    cols["all326_publishable"] = fr.pooled(all_arm["per_piece"])
    ci = fr.bootstrap({k: arms[k] for k in ("direct_cv", "identity_cv", "likelihood_cv")})
    # fr.bootstrap only pairs fitted_cv vs identity_cv by name; pair the arms this event needs
    ci["paired_delta"] = _paired(arms)

    verdicts = {}
    for axis, (lo, hi) in PREDICTION_BANDS.items():
        v = cols["direct_cv"][axis]
        verdicts[axis] = {"band": [lo, hi], "measured": v,
                          "holds": bool(v is not None and lo <= v <= hi),
                          "vs_identity_pp": (round(v - cols["identity_cv"][axis], 2)
                                             if v is not None else None),
                          "vs_likelihood_pp": (round(v - cols["likelihood_cv"][axis], 2)
                                               if v is not None else None)}

    # ── the modulation-rate check (the OI-187 mechanism must not reappear) ──
    gt_mod = gt_modulation_rate(sorted(covered))
    mod = {}
    for name, a in list(arms.items()) + [("all326_publishable", all_arm)]:
        d = decode_modulation_rate(a["segments"])
        shared = sorted(set(d) & set(gt_mod))
        mod[name] = {"mean_key_changes_per_piece": round(float(np.mean([d[s] for s in shared])), 2),
                     "total_key_changes": int(sum(d[s] for s in shared)),
                     "pieces_with_zero_key_change": int(sum(1 for s in shared if d[s] == 0)),
                     "n_pieces": len(shared)}
    shared = sorted(set(gt_mod) & set(arms["direct_cv"]["segments"]))
    mod["ground_truth"] = {
        "mean_key_changes_per_piece": round(float(np.mean([gt_mod[s] for s in shared])), 2),
        "total_key_changes": int(sum(gt_mod[s] for s in shared)),
        "pieces_with_zero_key_change": int(sum(1 for s in shared if gt_mod[s] == 0)),
        "n_pieces": len(shared)}

    # ── the stability record (training spread + the labelled held-out diagnostic) ──
    est_sel = establish_at_selected(pieces, search, covered, fold_of, verbose)
    if not est_sel["pass"]:
        raise SystemExit("STOP: the cached-lattice decode does not reproduce the pinned decoder at "
                         "the selected weights — the stability diagnostic may not use it")
    stab = stability_heldout(search, pieces, covered, fold_of, verbose)
    stability = {}
    for fl, rec in stab.items():
        rs = [p["R_train"] for p in rec["per_start"]]
        hs = [p["heldout_columns"]["key_local_agree_pct"] for p in rec["per_start"]]
        rts = [p["heldout_columns"]["root_agree_pct"] for p in rec["per_start"]]
        stability[fl] = {
            "n_starts": len(rs),
            "R_train": {"min": round(min(rs), 6), "max": round(max(rs), 6),
                        "spread": round(max(rs) - min(rs), 6),
                        "median": round(float(np.median(rs)), 6),
                        "n_within_1e-3_of_best": int(sum(1 for r in rs if r <= min(rs) + 1e-3))},
            "heldout_key_local_pct": {"min": min(hs), "max": max(hs),
                                      "spread": round(max(hs) - min(hs), 2)},
            "heldout_root_pct": {"min": min(rts), "max": max(rts),
                                 "spread": round(max(rts) - min(rts), 2)},
            "selected_start_index": selected[fl]["start_index"],
            "selected_start_name": selected[fl]["start_name"],
            # ★ Does the search find a genuinely better region, or does it find the IDENTITY basin?
            # If the named starts (identity / the likelihood optimum) keep winning, the 19 random
            # starts are landing in worse local optima and the "optimum" is the neighbourhood we
            # began in — which changes how the whole result reads. Recorded per fold, summarized
            # below, so it cannot be lost behind the selected optimum's own figure.
            "R_train_by_start_class": {
                "identity": [p["R_train"] for p in rec["per_start"] if p["start_index"] == 0],
                "likelihood_fit": [p["R_train"] for p in rec["per_start"] if p["start_index"] == 1],
                "random": [p["R_train"] for p in rec["per_start"] if p["start_index"] >= 2]},
            "rank_of_identity_start": int(sorted(rs).index(
                [p["R_train"] for p in rec["per_start"] if p["start_index"] == 0][0]) + 1),
            "per_start": rec["per_start"]}

    # ── the weight reading ──
    wsel = {fl: selected[fl]["weights"] for fl in selected}
    wsel["all326"] = sel_all["weights"]
    gen = {fl: selected[fl]["weights_generative_scale"] for fl in selected}
    gen["all326"] = sel_all["weights_generative_scale"]
    per_fold_vals = {n: [selected[f"fold{f}"]["weights_generative_scale"][n]
                         for f in range(fw.N_FOLDS)] for n in sd.W_NAMES}
    weight_stats = {n: {"mean": round(float(np.mean(v)), 4), "sd": round(float(np.std(v)), 4),
                        "min": round(float(min(v)), 4), "max": round(float(max(v)), 4),
                        "n_folds_at_zero": int(sum(1 for x in v if x == 0.0))}
                    for n, v in per_fold_vals.items()}

    out = {
        "provenance": {
            "generator": glt._rel(Path(__file__)),
            "instrument_commit": glt._git_head(),
            "search_artifact": glt._rel(SEARCH_ARTIFACT),
            "note_events_git_hash": prov["corpus_git_hash"],
            "selection_rule": ("per fold, the converged optimum with the best TRAINING objective R "
                               "(ties by lower start index) — `select_optimum`. Nothing measured in "
                               "this module enters the selection."),
            "held_out_discipline": ("each piece is decoded once per arm by the model (tables AND "
                                    "weights) fitted on the complement of ITS fold; the per-start "
                                    "held-out figures under `stability` are a DIAGNOSTIC computed "
                                    "after selection and entered no decision"),
            "decoder": "probe_decoder.decode_piece (pinned) for every graded arm",
            "grading": ("probe_run.grade_regions -> a8_rebaseline_measure.build_piece_grid vs "
                        "dcml_parser.load_wir_regions — the pinned chain the committed baselines use"),
            "bootstrap": {"B": fr.BOOTSTRAP_B, "seed": fr.BOOTSTRAP_SEED, "level": "95%",
                          "unit": "piece (resampled with replacement); paired across arms"},
        },
        "search_provenance": search["provenance"],
        "search_establishment": search.get("establishment", {}),
        "establishment": {"committed_arms_reproduced": repro,
                          "cached_lattice_at_selected_weights": est_sel},
        "fold_of_piece": {s: fold_of[s] for s in sorted(covered)},
        "columns": cols,
        "confidence_intervals": ci,
        "prediction_verdicts": verdicts,
        "committed_baselines": pr.BASELINES,
        "selected": {fl: {"start_index": selected[fl]["start_index"],
                          "start_name": selected[fl]["start_name"],
                          "start_seed": selected[fl]["start_seed"],
                          "R_train": selected[fl]["R_train"],
                          "train_columns": selected[fl]["train_columns"],
                          "n_evaluations": selected[fl]["n_evaluations"]} for fl in selected},
        "selected_all326": {"start_index": sel_all["start_index"], "start_name": sel_all["start_name"],
                            "R_train": sel_all["R_train"], "train_columns": sel_all["train_columns"]},
        "weights": {"per_fold_normalized": wsel, "per_fold_generative_scale": gen,
                    "across_fold_statistics_generative_scale": weight_stats},
        "stability": stability,
        "modulation_rate": mod,
        "cadence_fires": {k: a["cadence"] for k, a in arms.items()},
        "timing": {name: {"mean_s": round(float(np.mean(a["timings"])), 3),
                          "max_s": round(float(np.max(a["timings"])), 3),
                          "total_s": round(float(np.sum(a["timings"])), 1)}
                   for name, a in list(arms.items()) + [("all326", all_arm)]},
        "sensitive_cases": fr.sensitive_cases(pieces, "all", sel_all["weights"],
                                              pd.Vocabulary(fr._adapter("all", sel_all["weights"]).tables),
                                              pd.ChordCache()),
        "deceptive_cadence_case": fr.deceptive_cadence_check(sel_all["weights"]),
        "prune_cost_at_selected_weights": fr.prune_cost(
            pieces, "all", sel_all["weights"],
            pd.Vocabulary(fr._adapter("all", sel_all["weights"]).tables), pd.ChordCache()),
        "per_piece": {name: {s: {k: int(v) for k, v in g.items()}
                             for s, g in a["per_piece"].items()} for name, a in arms.items()},
        "wall_seconds": round(time.perf_counter() - t_all, 1),
    }
    OUT_JSON.write_text(json.dumps(out, indent=1), encoding="utf-8")
    write_summary(out)
    print(f"\nwrote {glt._rel(OUT_JSON)} and {glt._rel(OUT_SUMMARY)}")
    return out


def _paired(arms):
    """Piece-level paired bootstrap deltas for the two comparisons this event needs: the direct-search
    arm against the identity generative baseline, and against the likelihood fit."""
    stems = sorted(set.intersection(*[set(a["per_piece"]) for a in arms.values()]))
    rng = np.random.default_rng(fr.BOOTSTRAP_SEED)
    idx = rng.integers(0, len(stems), size=(fr.BOOTSTRAP_B, len(stems)))
    draws = {}
    for name, arm in arms.items():
        draws[name] = {}
        for axis, (a, d) in _NUM.items():
            m = np.array([[arm["per_piece"][s][a], arm["per_piece"][s][d]] for s in stems],
                         dtype=np.float64)
            num = m[:, 0][idx].sum(axis=1)
            den = (m[:, 0] + m[:, 1])[idx].sum(axis=1)
            draws[name][axis] = 100.0 * num / np.maximum(1.0, den)
    out = {}
    for other in ("identity_cv", "likelihood_cv"):
        out[f"direct_cv_minus_{other}"] = {}
        for axis in AXES:
            dd = draws["direct_cv"][axis] - draws[other][axis]
            lo, hi = float(np.percentile(dd, 2.5)), float(np.percentile(dd, 97.5))
            out[f"direct_cv_minus_{other}"][axis] = {
                "mean": round(float(dd.mean()), 2), "lo": round(lo, 2), "hi": round(hi, 2),
                "excludes_zero": bool(lo > 0 or hi < 0)}
    return out


def write_summary(g):
    L = []
    A = ("key_local_agree_pct", "key_home_agree_pct", "root_agree_pct", "rn_agree_pct")
    L.append("THE DIRECT-METRIC WEIGHT SEARCH — the ratified fallback (Task 2 measurement)")
    L.append(f"instrument {g['provenance']['instrument_commit']}   "
             f"corpus {g['provenance']['note_events_git_hash']}")
    L.append("")
    L.append("HEADLINE — pooled 5-fold CV (each piece decoded once by its fold's complement model)")
    L.append(f"{'arm':26s} {'key-LOCAL':>12s} {'key-HOME':>12s} {'root':>12s} {'RN':>12s}")
    for name in ("direct_cv", "identity_cv", "likelihood_cv", "all326_publishable"):
        c = g["columns"][name]
        L.append(f"{name:26s} " + " ".join(f"{c[a]:12.2f}" for a in A))
    L.append("")
    L.append("95 % piece-bootstrap intervals (direct-search arm) and PAIRED deltas")
    for a in A:
        ci = g["confidence_intervals"]["arms"]["direct_cv"][a]
        d1 = g["confidence_intervals"]["paired_delta"]["direct_cv_minus_identity_cv"][a]
        d2 = g["confidence_intervals"]["paired_delta"]["direct_cv_minus_likelihood_cv"][a]
        L.append(f"  {a:22s} [{ci['lo']:6.2f},{ci['hi']:6.2f}]   "
                 f"vs identity {d1['mean']:+6.2f} [{d1['lo']:+6.2f},{d1['hi']:+6.2f}]"
                 f"{' *' if d1['excludes_zero'] else '  '}   "
                 f"vs likelihood {d2['mean']:+6.2f} [{d2['lo']:+6.2f},{d2['hi']:+6.2f}]"
                 f"{' *' if d2['excludes_zero'] else ''}")
    L.append("  (* = the interval excludes zero; a difference inside its interval is not a finding, #24)")
    L.append("")
    L.append("PREDICTION VERDICTS (bands written by Cowork before measuring, #17b)")
    for a in A:
        v = g["prediction_verdicts"][a]
        L.append(f"  {a:22s} band {v['band'][0]:5.1f}-{v['band'][1]:5.1f}  measured {v['measured']:6.2f}"
                 f"   {'HOLDS' if v['holds'] else '*** MISSED ***'}")
    L.append("")
    L.append("STABILITY — the converged optima per fold (the protocol's substitute for a convexity proof)")
    L.append(f"{'fold':8s} {'starts':>7s} {'R_train min':>12s} {'max':>10s} {'spread':>9s} "
             f"{'near-best':>10s} {'selected start':>16s} {'id.rank':>8s}  heldout keyL spread")
    for fl, s in sorted(g["stability"].items()):
        L.append(f"{fl:8s} {s['n_starts']:7d} {s['R_train']['min']:12.6f} {s['R_train']['max']:10.6f} "
                 f"{s['R_train']['spread']:9.6f} {s['R_train']['n_within_1e-3_of_best']:10d} "
                 f"{s['selected_start_name']:>16s} {s['rank_of_identity_start']:8d}  "
                 f"{s['heldout_key_local_pct']['spread']:.2f} pp")
    won = [s["selected_start_name"] for s in g["stability"].values()]
    n_named = sum(1 for w in won if w in ("identity", "likelihood_fit"))
    L.append(f"  the selected optimum came from a NAMED start (identity / likelihood) in "
             f"{n_named} of {len(won)} folds, from a seeded-random start in {len(won) - n_named}.")
    L.append("  'id.rank' = the identity start's rank among the 21 converged optima (1 = best). If the")
    L.append("  identity start keeps ranking first, the search is finding the basin it STARTED in and")
    L.append("  the 19 random starts are landing in worse local optima — read the headline accordingly.")
    L.append("")
    L.append("THE SELECTED WEIGHTS (generative scale: the nine generative weights average 1.0, so the")
    L.append("vector reads directly against the identity ablation where each of them IS 1.0)")
    ws = g["weights"]["across_fold_statistics_generative_scale"]
    L.append(f"{'weight':24s} {'mean':>8s} {'sd':>8s} {'min':>8s} {'max':>8s} {'folds@0':>8s}")
    for n in sd.W_NAMES:
        s = ws[n]
        L.append(f"{n:24s} {s['mean']:8.3f} {s['sd']:8.3f} {s['min']:8.3f} {s['max']:8.3f} "
                 f"{s['n_folds_at_zero']:8d}")
    L.append("")
    L.append("MODULATION RATE (the OI-187 mechanism was a decode that stopped modulating)")
    L.append(f"{'arm':26s} {'mean key changes/piece':>24s} {'total':>8s} {'pieces with 0':>15s}")
    for name in ("ground_truth", "identity_cv", "likelihood_cv", "direct_cv", "all326_publishable"):
        m = g["modulation_rate"][name]
        L.append(f"{name:26s} {m['mean_key_changes_per_piece']:24.2f} {m['total_key_changes']:8d} "
                 f"{m['pieces_with_zero_key_change']:15d}")
    L.append("")
    L.append("ESTABLISHMENT")
    for r in g["establishment"]["committed_arms_reproduced"]:
        L.append(f"  {r['arm']:16s} reproduces committed fit_grading.json on {r['n_pieces']} pieces: "
                 f"{'PASS' if r['pass'] else 'FAIL'}")
    e = g["establishment"]["cached_lattice_at_selected_weights"]
    L.append(f"  cached-lattice decode == pinned decode_piece at the SELECTED weights: "
             f"{e['n_checks']} checks, {e['mismatches']} mismatches "
             f"({'PASS' if e['pass'] else 'FAIL'})")
    se = g.get("search_establishment", {}).get("decoder_vs_pinned")
    if se:
        L.append(f"  cached-lattice decode == pinned decode_piece at identity + random weights: "
                 f"{se['n_checks']} checks, {se['mismatches']} mismatches "
                 f"({'PASS' if se['pass'] else 'FAIL'})")
        si = se.get("scale_invariance")
        if si:
            L.append(f"  scale invariance (the decode is a function of the RAY of w): "
                     f"{si['n_checks']} checks, {si['path_changes']} path changes "
                     f"({'PASS' if si['pass'] else 'FAIL'})")
    L.append("")
    L.append(f"PRUNE COST at the selected weights (OI-188): "
             + ", ".join(f"{a} {g['prune_cost_at_selected_weights']['loss_pp'][a]:+.2f} pp" for a in A))
    L.append(f"TIMING: " + ", ".join(f"{k} mean {v['mean_s']:.2f}s" for k, v in g["timing"].items()))
    L.append(f"wall {g['wall_seconds']:.0f}s")
    OUT_SUMMARY.write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L))


if __name__ == "__main__":
    main(sys.argv[1:])
