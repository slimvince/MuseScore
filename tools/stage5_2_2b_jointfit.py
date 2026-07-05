#!/usr/bin/env python3
"""stage5_2_2b_jointfit.py — Stage-5 Phase-2.2b Task-2 JOINT FIT (candidate only).

Coordinate-ascent over the coupled continuous cluster (design §4.2 objective/constraints,
P1-ratified staging step 2), under ONE declared rule configuration per invocation:
  Config I   — all rules enabled (no --disable-rule)
  Config II  — the 2.2a inert-7 disabled (GateA/F/GB/GC/GD/K/L)
  Config III — Config II + the 4 disable-beneficial (BiasCorrection/GateE/GateH/GateJ)

MEASUREMENT / CANDIDATE ONLY. No committed constant changes; every evaluation regens to a
manifest-stamped scratch root; the frozen tools/corpus is never touched. Nothing adopted.

Objective (design §4.2): variant-(b) duration-weighted root agreement on the ratified
FITTING SPLIT (261). Per-evaluation HARD constraints, referenced against the COMMITTED
all-rules-ON fitting-split baseline (the 53/24/53 successor semantics):
  (1) no NEW class-(b) batch-stop case among fitting-split scores;
  (2) class-(b) root-disagree DURATION non-increase;
  (3) Gate-R invariant search bound: sameRootInversionBonus > kNonBassPenalty (0.35).
RN + key are tracked beside, never collapsed in.

Search: per row, a 5-point local ladder [v-2s, v-s, v, v+s, v+2s] at the 1b step
(value in [0,1] -> s=0.05; value >1 -> s=10%), coordinate ascent, max --rounds full rounds,
then a halved-step refinement pass on the rows that moved. Deterministic (fixed row order,
tie-break toward the current value); cached (a vector is evaluated at most once); resumable
(the cache is persisted and warm-starts a re-run). Budget: --budget-hours wall cap; STOP and
report partials beyond it.

Reuses verbatim: stage5_fit_driver (PARAMS / baseline_value / evaluate / split_scores_file).
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT / "tools"))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import stage5_fit_driver as drv   # noqa: E402

FIT_LEDGER_DIR = _ROOT / "tools" / "fit_ledgers"
K_NON_BASS_PENALTY = drv.PARAMS["kNonBassPenalty"]["val"]   # 0.35 (the Gate-R bound floor)

# The ratified cluster (design §4.4 family 1 continuous + O-7 re-entry). kWStepOut is added
# to the sweep only if kWStepIn shows it is coupled (handled by including it in --params).
DEFAULT_CLUSTER = [
    "kRootToneFactor", "kSecondToneFactor", "sameRootInversionBonus", "bassNoteRootBonus",
    "tpcConsistencyBonusPerTone", "rootContinuityBonus", "kWStepIn", "kPowerChord3PcPenalty",
]

# Config II = the CROSS-CARRIER-FULLY-INERT set (Task 1.1 refinement of the 2.2a fitting-split
# inert-7): GateGD (live on Baroque full corpus, 1 site) and GateL (live on Jazz, 18 sites,
# clsB+960) DROP OUT per the dispatch's "a rule live elsewhere drops out of the disabled set".
CONFIG_DISABLES = {
    "I": [],
    "II": ["GateA", "GateF", "GateGB", "GateGC", "GateK"],
    "III": ["GateA", "GateF", "GateGB", "GateGC", "GateK",
            "BiasCorrection", "GateE", "GateH", "GateJ"],
}


def step_for(name, carrier):
    base = drv.baseline_value(name, carrier)
    return round(0.10 * base, 6) if base > 1.0 else 0.05


def ladder(v, s):
    pts = [round(v - 2 * s, 6), round(v - s, 6), round(v, 6),
           round(v + s, 6), round(v + 2 * s, 6)]
    seen, out = set(), []
    for p in pts:
        p = max(0.0, p)
        if p not in seen:
            seen.add(p)
            out.append(p)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True, choices=["I", "II", "III"])
    ap.add_argument("--carrier", default="Baroque")
    ap.add_argument("--params", default=",".join(DEFAULT_CLUSTER))
    ap.add_argument("--rounds", type=int, default=2)
    ap.add_argument("--budget-hours", type=float, default=6.0)
    ap.add_argument("--refine", action="store_true", default=True)
    ap.add_argument("--scratch", default="C:/tmp/s5_jf")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    carrier = args.carrier
    cluster = [p for p in args.params.split(",") if p]
    disables = CONFIG_DISABLES[args.config]
    scratch = Path(args.scratch) / f"cfg{args.config}"
    scratch.mkdir(parents=True, exist_ok=True)
    a8_out = scratch / "a8"
    out = Path(args.out) if args.out else (FIT_LEDGER_DIR / f"stage5_jointfit_cfg{args.config}.jsonl")
    out.parent.mkdir(parents=True, exist_ok=True)
    cache_path = scratch / "cache.json"
    scores_file = drv.split_scores_file("fitting", scratch)

    t_start = time.time()
    budget_s = args.budget_hours * 3600

    # committed all-rules-ON fitting-split reference (the §4.2 constraint baseline)
    _, base_ref = drv.evaluate({}, carrier, scratch, a8_out, scores_file=scores_file,
                               disable_rules=[])
    base_ref_root = round(base_ref["root_pct"], 4)

    cache = {}
    if cache_path.exists():
        try:
            cache = json.loads(cache_path.read_text())
        except Exception:
            cache = {}

    def flush_cache():
        cache_path.write_text(json.dumps(cache), encoding="utf-8")

    n_evals = [0]

    def vec_key(vec):
        return "|".join(f"{k}={vec[k]:.6g}" for k in sorted(vec))

    def eval_vec(vec):
        key = vec_key(vec)
        if key in cache:
            return cache[key]
        # Gate-R invariant search bound
        srib = vec.get("sameRootInversionBonus")
        if srib is not None and srib <= K_NON_BASS_PENALTY:
            rec = {"root": None, "feasible": False, "bound_violation": "gateR", "key": key}
            cache[key] = rec
            return rec
        row, m = drv.evaluate(dict(vec), carrier, scratch, a8_out, baseline=base_ref,
                              scores_file=scores_file, disable_rules=disables)
        c = row["constraints"]
        feasible = c["no_new_class_b_ok"] and c["class_b_nonincrease_ok"]
        rec = {"root": row["objective_root_pct"], "root_delta": row["objective_delta"],
               "rn": row["tracked"]["rn_pct"], "key": row["tracked"]["key_pct"],
               "batch": row["batch_gate"], "feasible": feasible,
               "new_class_b": c["new_class_b_batch_cases"],
               "class_b_dur_delta": c["class_b_dur_delta"],
               "no_new_class_b_ok": c["no_new_class_b_ok"],
               "class_b_nonincrease_ok": c["class_b_nonincrease_ok"], "key_str": key}
        cache[key] = rec
        n_evals[0] += 1
        with open(out, "a", encoding="utf-8") as f:
            f.write(json.dumps({"record": "eval", "config": args.config, "carrier": carrier,
                                "vector": vec, "disables": disables, **rec},
                               sort_keys=True) + "\n")
        flush_cache()
        print(f"  [{n_evals[0]:3d}] {vec_key(vec)[:120]}  root={rec['root']} "
              f"d={rec['root_delta']:+.4f} batch={rec['batch']} "
              f"newB={len(rec['new_class_b'])} clsBd={rec['class_b_dur_delta']:+g} "
              f"feas={feasible}", flush=True)
        return rec

    current = {p: round(drv.baseline_value(p, carrier), 6) for p in cluster}
    # config baseline: the cluster at defaults, WITH the config disables
    cfg_base = eval_vec(dict(current))
    cur_root = cfg_base["root"] if cfg_base["feasible"] else base_ref_root
    print(f"JOINTFIT config={args.config} carrier={carrier} disables={disables}")
    print(f"  all-on fitting baseline root={base_ref_root:.4f}; "
          f"config baseline root={cfg_base['root']} feasible={cfg_base['feasible']}", flush=True)

    moved_rows = set()
    stopped = False
    for rnd in range(args.rounds):
        any_move = False
        for row in cluster:
            if time.time() - t_start > budget_s:
                stopped = True
                break
            base_v = current[row]
            s = step_for(row, carrier)
            best_v, best_rec = base_v, eval_vec(dict(current))
            best_root = best_rec["root"] if best_rec["feasible"] else -1
            for v in ladder(base_v, s):
                if v == base_v:
                    continue
                if time.time() - t_start > budget_s:
                    stopped = True
                    break
                trial = dict(current)
                trial[row] = v
                rec = eval_vec(trial)
                if rec["feasible"] and rec["root"] is not None:
                    if (rec["root"], -abs(v - base_v)) > (best_root, -abs(best_v - base_v)):
                        best_root, best_v, best_rec = rec["root"], v, rec
            if best_v != base_v and best_root > cur_root + 1e-9:
                current[row] = best_v
                cur_root = best_root
                moved_rows.add(row)
                any_move = True
                print(f"  round {rnd+1}: {row} {base_v} -> {best_v}  root->{cur_root:.4f}", flush=True)
            if stopped:
                break
        if stopped or not any_move:
            break

    # halved-step refinement on movers
    if args.refine and not stopped:
        for row in sorted(moved_rows):
            if time.time() - t_start > budget_s:
                stopped = True
                break
            base_v = current[row]
            s = step_for(row, carrier) / 2
            for v in (round(base_v - s, 6), round(base_v + s, 6)):
                if v < 0 or v == base_v:
                    continue
                trial = dict(current)
                trial[row] = v
                rec = eval_vec(trial)
                if rec["feasible"] and rec["root"] is not None and rec["root"] > cur_root + 1e-9:
                    current[row] = v
                    cur_root = rec["root"]
                    print(f"  refine: {row} {base_v} -> {v}  root->{cur_root:.4f}", flush=True)

    best_rec = eval_vec(dict(current))
    summary = {"record": "summary", "config": args.config, "carrier": carrier,
               "disables": disables, "cluster": cluster,
               "all_on_baseline_root": base_ref_root,
               "config_baseline_root": cfg_base["root"],
               "best_vector": current, "best_root": cur_root,
               "best_delta_vs_all_on": round(cur_root - base_ref_root, 4),
               "best_rec": best_rec, "moved_rows": sorted(moved_rows),
               "n_evals": n_evals[0], "budget_stopped": stopped,
               "elapsed_min": round((time.time() - t_start) / 60, 1)}
    with open(out, "a", encoding="utf-8") as f:
        f.write(json.dumps(summary, sort_keys=True) + "\n")
    print("\nJOINTFIT SUMMARY", json.dumps(summary, indent=1), flush=True)


if __name__ == "__main__":
    main()
