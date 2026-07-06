#!/usr/bin/env python3
"""conformal_check.py — Stage-5 Phase 3 Task D: R-11 split-conformal abstention disposition.

MEASUREMENT / VERDICT MATERIAL ONLY. Nothing adopted. On the SAME substrate as Task A's
L3/L4 rows, compares two ways of choosing the ABSTENTION bar (contract U5) at declared
target-correctness (coverage) levels:

  (a) SPLIT-CONFORMAL: fitting split = calibration set, held-out = test set. Choose the
      smallest confidence threshold whose calibration retained-correctness LOWER bound
      (Hoeffding, delta=0.1 — a finite-sample-valid selective-risk threshold) >= target.
  (b) MAP-IMPLIED: abstain when the fitted Class-P map(conf) < target (confidence-below-bar,
      the map's own implied abstention).

Both are confidence thresholds (the map is monotone); the comparison is METHOD-of-choosing.
Deliverable: does conformal add value for the abstention bars (design: "a complement, not
a replacement")? — recorded for the Cowork disposition.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import calibration_fit as cf   # reuse the Task-A collectors + splits + map loader

_ROOT = Path(__file__).resolve().parent.parent
CALIB_DIR = _ROOT / "tools" / "calibration_maps"

TARGETS = [0.70, 0.75, 0.80]   # declared coverage (target retained-correctness) levels
DELTA = 0.10                    # Hoeffding confidence for the conformal lower bound


def _map_fn(path):
    art = json.loads(Path(path).read_text(encoding="utf-8"))
    xs = art["map"]["x_thresholds"]; ys = art["map"]["y_thresholds"]

    def m(c):
        if c <= xs[0]:
            return ys[0]
        if c >= xs[-1]:
            return ys[-1]
        for i in range(1, len(xs)):
            if c <= xs[i]:
                x0, x1, y0, y1 = xs[i - 1], xs[i], ys[i - 1], ys[i]
                return y1 if x1 == x0 else y0 + (y1 - y0) * (c - x0) / (x1 - x0)
        return ys[-1]
    return m


def _retained_stats(pairs, tau):
    """pairs: (conf, correct, w). Weighted retained fraction + weighted correctness among
    conf>=tau."""
    w_ret = w_cor = w_tot = 0.0
    for c, y, w in pairs:
        w_tot += w
        if c >= tau:
            w_ret += w
            w_cor += y * w
    frac = (w_ret / w_tot) if w_tot else 0.0
    corr = (w_cor / w_ret) if w_ret else None
    return frac, corr, w_ret


def _hoeffding_lb(emp, n_eff, delta):
    if n_eff <= 0:
        return 0.0
    return emp - math.sqrt(math.log(1.0 / delta) / (2.0 * n_eff))


def conformal_tau(cal_pairs, target, delta):
    """Smallest confidence tau s.t. the calibration retained-correctness Hoeffding lower
    bound >= target. n_eff = retained COUNT (unweighted, for the finite-sample bound)."""
    confs = sorted(set(round(c, 4) for c, _, _ in cal_pairs))
    best = None
    for tau in confs:
        ret = [(c, y, w) for (c, y, w) in cal_pairs if c >= tau]
        n = len(ret)
        if n == 0:
            continue
        wcor = sum(y * w for _, y, w in ret); wsum = sum(w for _, _, w in ret)
        emp = wcor / wsum if wsum else 0.0
        lb = _hoeffding_lb(emp, n, delta)
        if lb >= target:
            best = tau
            break   # confs ascending; first tau meeting the bound retains the most
    return best


def map_tau(mapper, target):
    """Smallest conf where map(conf) >= target (map monotone). Scan a fine grid."""
    for i in range(0, 1001):
        c = i / 1000.0
        if mapper(c) >= target:
            return c
    return None


def run_row(name, carrier, cells, map_path, out):
    fit = cf.split_pairs(cells, "fitting")
    hel = cf.split_pairs(cells, "held_out")
    mapper = _map_fn(map_path)
    rows = []
    for tgt in TARGETS:
        ct = conformal_tau(fit, tgt, DELTA)
        mt = map_tau(mapper, tgt)
        r = {"target": tgt}
        if ct is not None:
            f, c, _ = _retained_stats(hel, ct)
            r["conformal"] = {"tau": ct, "test_retained_frac": round(f, 4),
                              "test_correct_among_retained": (round(c, 4) if c is not None else None),
                              "meets_target_on_test": (c is not None and c >= tgt)}
        else:
            r["conformal"] = {"tau": None, "note": "no calibration threshold meets the Hoeffding bound (target unreachable)"}
        if mt is not None:
            f, c, _ = _retained_stats(hel, mt)
            r["map_implied"] = {"tau": mt, "test_retained_frac": round(f, 4),
                                "test_correct_among_retained": (round(c, 4) if c is not None else None),
                                "meets_target_on_test": (c is not None and c >= tgt)}
        else:
            r["map_implied"] = {"tau": None, "note": "map never reaches target (ceiling below target)"}
        rows.append(r)
        cs = r["conformal"]; ms = r["map_implied"]
        print(f"    target={tgt:.2f}  CONFORMAL tau={cs.get('tau')} ret={cs.get('test_retained_frac')} "
              f"corr={cs.get('test_correct_among_retained')} meets={cs.get('meets_target_on_test')}  |  "
              f"MAP tau={ms.get('tau')} ret={ms.get('test_retained_frac')} corr={ms.get('test_correct_among_retained')} "
              f"meets={ms.get('meets_target_on_test')}")
    out[f"{name}_{carrier}"] = {"rows": rows, "n_cal": len(fit), "n_test": len(hel)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--km-root", default="C:/tmp/c1")
    ap.add_argument("--fs-root", default="C:/tmp/c1")
    ap.add_argument("--out", default="")
    args = ap.parse_args()

    splits = cf._load_splits()
    out = {"targets": TARGETS, "hoeffding_delta": DELTA, "rows": {}}
    print("=" * 78)
    print("conformal_check — Task D: split-conformal vs map-implied abstention (verdict material)")
    print("=" * 78)
    for carrier in cf.CARRIERS:
        print(f"\n########## CARRIER = {carrier} ##########")
        km_dir = Path(args.km_root) / f"km_{carrier}"
        fs_dir = Path(args.fs_root) / f"fs_{carrier}"
        print("  L3 key margin:")
        l3 = cf.collect_l3(carrier, km_dir, splits)
        run_row("l3_key_margin", carrier, l3,
                CALIB_DIR / f"stage5_classP_l3_key_margin_{carrier}.json", out["rows"])
        print("  L4 chord composite:")
        l4 = cf.collect_l4(carrier, fs_dir, splits)
        run_row("l4_chord_composite", carrier, l4,
                CALIB_DIR / f"stage5_classP_l4_chord_composite_{carrier}.json", out["rows"])

    if args.out:
        Path(args.out).write_text(json.dumps(out, indent=1), encoding="utf-8")
        print(f"\n[wrote {args.out}]")


if __name__ == "__main__":
    main()
