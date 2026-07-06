#!/usr/bin/env python3
"""theta_fit.py — Stage-5 Phase 3 Task C: declare the frame contradiction scales +
fit override θ CANDIDATES (RECORDED, NOTHING WIRED).

MEASUREMENT + LEDGER ONLY. No behaviour change; the override θ (forwardoverride.h
baseBar/confidenceScale) is NOT exposed to --param-override, so this fits candidates
POST-HOC from the dumped fired sites — it does not re-run or recompile anything. The
frames are dormant-chain sites; adoption rides the engage arc (design §4.5.2 / O-13).

Deliverables (design §4.5.2 / contract §7 D-FS):
  1. Re-confirm the F-A (cadentialWeight) and F-B (bestPlaus-committedPlaus) contradiction
     ranges on the CURRENT corpus; declare a monotone [0,1] squash per R5.
  2. Fit θ candidates that maximize corrections-minus-harm on the fitting split; validate
     on held-out. Acceptance reference: not worse than the current constants' corrections/
     fires ratio (the E0 968-fires/45-corrections net-harm measure).

The one-sided limitation (RECORDED): the dump emits S_contra ONLY at sites that fired at
the CURRENT bar (S > 1.0 + 1.0*C). So candidates can be explored only in the STRICTER-bar
direction (raising the bar drops current fires — measurable); a LOOSER bar would create
unseen fires (not measurable without exposing θ to --param-override + a re-run, an additive
engage-arc step, deferred). Since the current override is net-harmful, the useful direction
IS the measurable one.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import compare_analyses as cmp
import compare_rn as C
import dcml_parser as dcml
import a8_rebaseline_measure as a8

_ROOT = Path(__file__).resolve().parent.parent
WIR_BASE = a8.WIR_DIR   # tools/dcml/when_in_rome (the WiR corpus root find_wir_file expects)
SPLIT_REGISTRY = _ROOT / "tools" / "stage5_split_registry.json"
CALIB_DIR = _ROOT / "tools" / "calibration_maps"

_SYM_QUALITIES = {"Diminished", "Augmented", "HalfDiminished"}
_SYM_AMBIG = {"SymmetricRotation", "ShareTone", "RelativePair"}

# Declared squash constants (R5; precision-phase). s(x)=x/(x+k), monotone [0,inf)->[0,1).
SQUASH_K_FB = 2.0   # F-B bestPlaus-committedPlaus: median 2.0 (the minimal contradiction unit)
SQUASH_K_FA = 3.5   # F-A cadentialWeight: ~ single-authentic-cadence unit (matches C1 cadence k)

# Current override bar (forwardoverride.h defaults): S > baseBar + confidenceScale*C
CUR_BASE = 1.0
CUR_CONF = 1.0


def _load_splits():
    reg = json.loads(SPLIT_REGISTRY.read_text(encoding="utf-8"))
    return {stem: v["split"] for stem, v in reg["scores"].items()}


def _load_l4_map(carrier):
    p = CALIB_DIR / f"stage5_classP_l4_chord_composite_{carrier}.json"
    if not p.exists():
        return None
    art = json.loads(p.read_text(encoding="utf-8"))
    if art.get("map_type") != "isotonic":
        return None
    xs = art["map"]["x_thresholds"]; ys = art["map"]["y_thresholds"]

    def m(c):
        # piecewise-linear interpolation with clip (matches sklearn isotonic predict)
        if c <= xs[0]:
            return ys[0]
        if c >= xs[-1]:
            return ys[-1]
        for i in range(1, len(xs)):
            if c <= xs[i]:
                x0, x1, y0, y1 = xs[i - 1], xs[i], ys[i - 1], ys[i]
                if x1 == x0:
                    return y1
                return y0 + (y1 - y0) * (c - x0) / (x1 - x0)
        return ys[-1]
    return m


def collect_fb_fires(carrier, fs_dir, splits):
    """Per FIRED F-B site: dict(split, C, S, outcome). outcome in
    {correction, harm, neutral}."""
    out = []
    for p in sorted(Path(fs_dir).glob("*.ours.json")):
        stem = p.name.replace(".ours.json", "")
        if stem == "corpus_manifest":
            continue
        split = splits.get(stem)
        if split is None:
            continue
        try:
            data, chain_regions = cmp.load_analysis(p)
        except Exception:
            continue
        wir_path = dcml.find_wir_file(str(WIR_BASE), stem)
        if not wir_path:
            continue
        try:
            wir_regions = dcml.parse_rntxt_file(wir_path)
        except Exception:
            continue
        if not chain_regions or not wir_regions:
            continue
        matches = cmp.align_dcml_regions(chain_regions, wir_regions, mode=cmp.DEFAULT_DCML_MATCH_MODE)
        raw_by_tick = {int(r.get("startTick", -1)): r for r in data.get("regions", [])}
        for cr, dr in zip(chain_regions, matches):
            if dr is None or dr.root_pc is None:
                continue
            raw = raw_by_tick.get(cr.start_tick, {})
            if not bool(raw.get("l5OverrodeCommit", False)):
                continue
            l4root = int(raw.get("l4RootPc", -1))
            l4dec = raw.get("l4Decision", "Commit")
            Cc = float(raw.get("l4Composite", 0.0))
            S = float(raw.get("l5OverrideContradiction", 0.0))
            final = cr.root_pc
            qual = raw.get("quality", "Unknown")
            ambig = raw.get("ambiguityKind", "None")
            symmetric = (qual in _SYM_QUALITIES) or (ambig in _SYM_AMBIG)
            outcome = "neutral"
            if l4dec in ("Commit", "Inherit") and l4root >= 0 and l4root != dr.root_pc and not symmetric:
                outcome = "correction" if final == dr.root_pc else "neutral"
            elif l4dec in ("Commit", "Inherit") and l4root >= 0 and l4root == dr.root_pc:
                outcome = "harm" if final != dr.root_pc else "neutral"
            out.append({"split": split, "C": Cc, "S": S, "outcome": outcome})
    return out


def collect_fa_mods(carrier, fs_dir, splits):
    """Per confirmed modulation (F-A fire): dict(split, S=cadentialWeight, correct).
    'correct' = our modulation tonic agrees with the DCML key tonic over the span."""
    out = []
    for p in sorted(Path(fs_dir).glob("*.ours.json")):
        stem = p.name.replace(".ours.json", "")
        if stem == "corpus_manifest":
            continue
        split = splits.get(stem)
        if split is None:
            continue
        try:
            data, ours_regions = cmp.load_analysis(p)
        except Exception:
            continue
        wir_path = dcml.find_wir_file(str(WIR_BASE), stem)
        if not wir_path:
            continue
        try:
            wir_regions = dcml.parse_rntxt_file(wir_path)
        except Exception:
            continue
        if not wir_regions:
            continue
        try:
            spans = cmp._dcml_time_spans(ours_regions, wir_regions)   # (start,end) per WiR region
        except Exception:
            continue
        for m in data.get("modulations", []):
            if not (m.get("isModulation") and m.get("cadenceConfirmed")):
                continue
            S = float(m.get("cadentialWeight", 0.0))
            our_tonic = int(m.get("tonicPc", -1))
            st = int(m.get("startTick", -1)); et = int(m.get("endTick", st))
            mid = (st + et) // 2
            dcml_tonic = _dcml_key_tonic_at(spans, wir_regions, mid)
            correct = (dcml_tonic is not None and our_tonic == dcml_tonic)
            out.append({"split": split, "S": S, "correct": bool(correct),
                        "our_tonic": our_tonic, "dcml_tonic": dcml_tonic})
    return out


def _dcml_key_tonic_at(spans, wir_regions, tick):
    """Local-key tonic pc of the WiR region whose (start,end) span contains `tick`."""
    try:
        idx = C._active_index_at(spans, tick)
        if idx is None:
            return None
        pc_major = C._dcml_key_tonic(wir_regions[idx].local_key)
        if pc_major is None:
            return None
        return pc_major[0]   # (tonic_pc, is_major)
    except Exception:
        return None


def bar(bb, cs, Cc):
    return bb + cs * max(0.0, min(1.0, Cc))


def score_fb(fires, bb, cs, split=None):
    """Count fires/corrections/harm KEPT under bar (bb,cs). A site is kept iff S > bar."""
    f = c = h = 0
    for s in fires:
        if split is not None and s["split"] != split:
            continue
        if s["S"] > bar(bb, cs, s["C"]):
            f += 1
            if s["outcome"] == "correction":
                c += 1
            elif s["outcome"] == "harm":
                h += 1
    return f, c, h


def dominates_current(bb, cs, fires):
    """A candidate is MEASURABLE iff its bar >= current bar over the observed C range
    (so it can only remove current fires; it introduces no unseen fires)."""
    for s in fires:
        if bar(bb, cs, s["C"]) < bar(CUR_BASE, CUR_CONF, s["C"]) - 1e-9:
            return False
    return True


def fit_fb(fires, l4map):
    fit = [s for s in fires if s["split"] == "fitting"]
    hel = [s for s in fires if s["split"] == "held_out"]
    # current
    cur = {"bb": CUR_BASE, "cs": CUR_CONF}
    cur["fit"] = score_fb(fit, CUR_BASE, CUR_CONF)
    cur["hel"] = score_fb(hel, CUR_BASE, CUR_CONF)
    # grid search over measurable (stricter-or-equal) bars
    best = None
    bbs = [round(1.0 + 0.25 * i, 3) for i in range(0, 13)]   # 1.0 .. 4.0
    css = [round(0.0 + 0.25 * i, 3) for i in range(0, 17)]   # 0.0 .. 4.0
    for bb in bbs:
        for cs in css:
            if not dominates_current(bb, cs, fires):
                continue
            f, c, h = score_fb(fit, bb, cs)
            obj = c - h
            key = (obj, -f)  # maximize corr-harm, tie-break fewer fires (less churn)
            if best is None or key > best["key"]:
                best = {"bb": bb, "cs": cs, "key": key, "fit": (f, c, h)}
    if best:
        best["hel"] = score_fb(hel, best["bb"], best["cs"])
        # odds-ratio re-expression at the chosen bar: theta s.t. squash(S) = theta*map(C)
        # report the implied theta band on kept corrections vs dropped harms
        best["squash_note"] = f"squash_FB s(x)=x/(x+{SQUASH_K_FB}); map_L4 applied to C"
    return {"current": cur, "best": best,
            "n_fit": len(fit), "n_hel": len(hel), "n_total": len(fires)}


def fit_fa(mods):
    """Reduced F-A candidate: threshold tau on cadentialWeight (confidenceScale term
    unavailable — the per-modulation L3 incumbent confidence is not in the modulations[]
    dump; the full form is deferred to the engage arc). Maximize corr-harm on fitting."""
    fit = [m for m in mods if m["split"] == "fitting"]
    hel = [m for m in mods if m["split"] == "held_out"]

    def score(ms, tau):
        f = c = h = 0
        for m in ms:
            if m["S"] > tau:
                f += 1
                if m["correct"]:
                    c += 1
                else:
                    h += 1
        return f, c, h
    cur = {"tau": CUR_BASE, "fit": score(fit, CUR_BASE), "hel": score(hel, CUR_BASE)}
    best = None
    for i in range(0, 41):
        tau = round(1.0 + 0.25 * i, 3)   # 1.0 .. 11.0 (covers [3.25,9.35])
        f, c, h = score(fit, tau)
        obj = c - h
        key = (obj, -f)
        if best is None or key > best["key"]:
            best = {"tau": tau, "key": key, "fit": (f, c, h)}
    if best:
        best["hel"] = score(hel, best["tau"])
    return {"current": cur, "best": best, "n_fit": len(fit), "n_hel": len(hel),
            "n_total": len(mods)}


def _range(xs):
    if not xs:
        return None
    xs = sorted(xs)
    n = len(xs)
    med = xs[n // 2] if n % 2 else (xs[n // 2 - 1] + xs[n // 2]) / 2
    return {"n": n, "min": xs[0], "med": med, "max": xs[-1]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fs-root", default="C:/tmp/c1")
    ap.add_argument("--carriers", default="baroque,default")
    ap.add_argument("--out", default="")
    args = ap.parse_args()

    splits = _load_splits()
    report = {"squash": {"F_A_cadentialWeight_k": SQUASH_K_FA, "F_B_plausDiff_k": SQUASH_K_FB,
                         "form": "s(x)=x/(x+k), monotone [0,inf)->[0,1); constants precision-phase (R5)"},
              "current_bar": {"baseBar": CUR_BASE, "confidenceScale": CUR_CONF,
                              "rule": "S_contra > baseBar + confidenceScale*C_incumbent"},
              "carriers": {}}
    for carrier in args.carriers.split(","):
        carrier = carrier.strip()
        fs_dir = Path(args.fs_root) / f"fs_{carrier}"
        l4map = _load_l4_map(carrier)
        fb = collect_fb_fires(carrier, fs_dir, splits)
        fa = collect_fa_mods(carrier, fs_dir, splits)
        fb_fit = fit_fb(fb, l4map)
        fa_fit = fit_fa(fa)
        rep = {
            "F_B": {
                "range_S_bestPlaus_minus_committedPlaus": _range([s["S"] for s in fb]),
                "range_C_l4Composite": _range([round(s["C"], 4) for s in fb]),
                "n_fires_total": len(fb),
                "outcome_counts": dict((k, sum(1 for s in fb if s["outcome"] == k))
                                       for k in ("correction", "harm", "neutral")),
                "fit": fb_fit,
            },
            "F_A": {
                "range_S_cadentialWeight": _range([m["S"] for m in fa]),
                "n_confirmed_modulations": len(fa),
                "correct_counts": {"correct": sum(1 for m in fa if m["correct"]),
                                   "wrong": sum(1 for m in fa if not m["correct"])},
                "fit_reduced_tau": fa_fit,
                "note": ("full θ form deferred: per-modulation L3 incumbent key confidence "
                         "is not in the modulations[] dump; fitted here as a reduced "
                         "cadentialWeight threshold (confidenceScale term omitted)."),
            },
        }
        report["carriers"][carrier] = rep

        print(f"\n########## CARRIER = {carrier} ##########")
        fbb = fb_fit["best"]; fbc = fb_fit["current"]
        print(f"  F-B fires={len(fb)}  outcome={rep['F_B']['outcome_counts']}  "
              f"S range={rep['F_B']['range_S_bestPlaus_minus_committedPlaus']}")
        print(f"    current bar (1.0,1.0): fit(f/c/h)={fbc['fit']}  hel={fbc['hel']}")
        if fbb:
            print(f"    best candidate bar (baseBar={fbb['bb']}, confidenceScale={fbb['cs']}): "
                  f"fit(f/c/h)={fbb['fit']}  hel(f/c/h)={fbb['hel']}  corr-harm(fit)={fbb['key'][0]}")
        faa = fa_fit["best"]; fac = fa_fit["current"]
        print(f"  F-A confirmed modulations={len(fa)}  correct/wrong={rep['F_A']['correct_counts']}  "
              f"S range={rep['F_A']['range_S_cadentialWeight']}")
        print(f"    current(τ=1.0): fit={fac['fit']} hel={fac['hel']}")
        if faa:
            print(f"    best reduced τ={faa['tau']}: fit(f/c/h)={faa['fit']} hel={faa['hel']} corr-harm(fit)={faa['key'][0]}")

    if args.out:
        Path(args.out).write_text(json.dumps(report, indent=1), encoding="utf-8")
        print(f"\n[wrote {args.out}]")


if __name__ == "__main__":
    main()
