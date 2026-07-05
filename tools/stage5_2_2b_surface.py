#!/usr/bin/env python3
"""stage5_2_2b_surface.py — Task-3 decision surface for a joint-fit candidate (per config).

For a given config's best_vector (read from its jointfit ledger summary) + the config's rule
disables, measure the full decision surface (MEASUREMENT ONLY; nothing adopted):
  - held-out (65) scored ONCE + fitting (261) — the overfit check;
  - full-corpus x3 carriers: root/RN/key, batch set-diff vs the committed 53/24/53 (explained
    per case with class), class-(b)/(a) durations;
  - D-4 Default adopt-with-Baroque eligibility (measured); Jazz regression spot-check (A-3).

Reference (committed baseline) = the evidence-sweep all-on full-corpus regen dirs at
C:/tmp/s5_2b/<carrier>/baseline (352 ours each, manifest-stamped) — reused, not re-regenerated.
The frozen tools/corpus is never touched. Reuses stage5_fit_driver (regen/measure) + a8.
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT / "tools"))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import stage5_fit_driver as drv   # noqa: E402

FIT_LEDGER_DIR = _ROOT / "tools" / "fit_ledgers"
BASE_ROOT = Path("C:/tmp/s5_2b")   # the evidence-sweep all-on full-corpus dirs
CARRIERS = ["Baroque", "Jazz", "Default"]
DISABLES = {
    "I": [],
    "II": ["GateA", "GateF", "GateGB", "GateGC", "GateK"],
    "III": ["GateA", "GateF", "GateGB", "GateGC", "GateK",
            "BiasCorrection", "GateE", "GateH", "GateJ"],
}


def read_best_vector(config):
    p = FIT_LEDGER_DIR / f"stage5_jointfit_cfg{config}.jsonl"
    best = None
    for ln in p.read_text(encoding="utf-8").splitlines():
        d = json.loads(ln)
        if d.get("record") == "summary":
            best = d
    return best


def base_cases(carrier, scratch):
    """a8-measure the all-on baseline dir for `carrier` (no regen)."""
    a8 = scratch / f"a8_base_{carrier.lower()}"
    return drv.measure(carrier, BASE_ROOT / carrier / "baseline", a8)


# Adoption model (per-preset scope, §4.2 shared-scope semantics + A-3/D-4):
#   - SHARED cluster params (all but sameRootInversionBonus) apply to EVERY preset on adoption.
#   - PER-PRESET params (sameRootInversionBonus) apply only to the ADOPT targets: Baroque (fit
#     target) + Default (D-4 adopt-with-Baroque). Jazz is NOT adopting (A-3), so its per-preset
#     value stays at the Jazz default — the fitted Baroque value must NOT be forced onto Jazz.
ADOPT_TARGETS = {"Baroque", "Default"}


def carrier_vec(vec, carrier):
    """The override dict for `carrier` under the adoption model: shared params = fitted value;
    per-preset params = fitted value on the adopt targets, the carrier's own default elsewhere."""
    out = {}
    for name, v in vec.items():
        if drv.PARAMS[name].get("per_preset") is not None and carrier not in ADOPT_TARGETS:
            out[name] = round(drv.baseline_value(name, carrier), 6)   # keep the preset's own default
        else:
            out[name] = v
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True, choices=["I", "II", "III"])
    ap.add_argument("--scratch", default="C:/tmp/s5_surface")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    scratch = Path(args.scratch) / f"cfg{args.config}"
    scratch.mkdir(parents=True, exist_ok=True)
    disables = DISABLES[args.config]
    summ = read_best_vector(args.config)
    vec = {k: v for k, v in summ["best_vector"].items()}
    out = Path(args.out) if args.out else (FIT_LEDGER_DIR / f"stage5_surface_cfg{args.config}.jsonl")

    print(f"SURFACE config={args.config} disables={disables}")
    print(f"  best_vector={vec}")
    print(f"  fitting best_root={summ['best_root']} (Δvs all-on {summ['best_delta_vs_all_on']:+})")

    surface = {"record": "surface", "config": args.config, "vector": vec,
               "disables": disables, "fitting_root": summ["best_root"],
               "fitting_delta_vs_all_on": summ["best_delta_vs_all_on"], "carriers": {}}

    # ── held-out + fitting on Baroque (overfit check) ──
    fit_file = drv.split_scores_file("fitting", scratch)
    held_file = drv.split_scores_file("held_out", scratch)
    a8b = scratch / "a8_baroque"
    # regen Baroque full with candidate ONCE, measure fitting + held-out + full
    ov = scratch / "override_baroque.txt"
    drv.write_override(carrier_vec(vec, "Baroque"), "Baroque", ov, disable_rules=disables)
    drv.regen("Baroque", str(ov).replace("\\", "/"), scratch)
    m_full = drv.measure("Baroque", scratch, a8b / "full")
    m_fit = drv.measure("Baroque", scratch, a8b / "fit", fit_file)
    m_held = drv.measure("Baroque", scratch, a8b / "held", held_file)
    # baseline splits (all-on)
    b_full = base_cases("Baroque", scratch)
    b_fit = drv.measure("Baroque", BASE_ROOT / "Baroque" / "baseline", scratch / "a8_bfit", fit_file)
    b_held = drv.measure("Baroque", BASE_ROOT / "Baroque" / "baseline", scratch / "a8_bheld", held_file)
    surface["overfit"] = {
        "fitting_base": round(b_fit["root_pct"], 4), "fitting_cand": round(m_fit["root_pct"], 4),
        "fitting_delta": round(m_fit["root_pct"] - b_fit["root_pct"], 4),
        "heldout_base": round(b_held["root_pct"], 4), "heldout_cand": round(m_held["root_pct"], 4),
        "heldout_delta": round(m_held["root_pct"] - b_held["root_pct"], 4),
    }
    print(f"  OVERFIT: fitting {b_fit['root_pct']:.4f}->{m_fit['root_pct']:.4f} "
          f"({m_fit['root_pct']-b_fit['root_pct']:+.4f}) | held-out "
          f"{b_held['root_pct']:.4f}->{m_held['root_pct']:.4f} "
          f"({m_held['root_pct']-b_held['root_pct']:+.4f})", flush=True)

    # ── full-corpus x3 carriers ──
    for carrier in CARRIERS:
        if carrier == "Baroque":
            m = m_full
            b = b_full
        else:
            ovp = scratch / f"override_{carrier.lower()}.txt"
            drv.write_override(carrier_vec(vec, carrier), carrier, ovp, disable_rules=disables)
            drv.regen(carrier, str(ovp).replace("\\", "/"), scratch)
            m = drv.measure(carrier, scratch, scratch / f"a8_{carrier.lower()}")
            b = base_cases(carrier, scratch)
        added = sorted((c, m["cases"][c]) for c in m["cases"] if c not in b["cases"])
        removed = sorted((c, b["cases"][c]) for c in b["cases"] if c not in m["cases"])
        changed = sorted((c, b["cases"][c], m["cases"][c]) for c in m["cases"]
                         if c in b["cases"] and m["cases"][c] != b["cases"][c])
        new_b = [c for c, cl in added if cl == "b"]
        rec = {
            "root_base": round(b["root_pct"], 4), "root_cand": round(m["root_pct"], 4),
            "root_delta": round(m["root_pct"] - b["root_pct"], 4),
            "rn_delta": round(m["rn_pct"] - b["rn_pct"], 4),
            "key_delta": round(m["key_pct"] - b["key_pct"], 4),
            "batch_base": b["batch_gate"], "batch_cand": m["batch_gate"],
            "batch_added": added, "batch_removed": removed, "batch_changed": changed,
            "new_class_b": new_b,
            "cls_b_dur_delta": m["cls_b_dur"] - b["cls_b_dur"],
            "cls_a_dur_delta": m["cls_a_dur"] - b["cls_a_dur"],
        }
        surface["carriers"][carrier] = rec
        print(f"  [{carrier}] root {rec['root_base']:.4f}->{rec['root_cand']:.4f} "
              f"({rec['root_delta']:+.4f}) rn_d={rec['rn_delta']:+.4f} key_d={rec['key_delta']:+.4f} "
              f"batch {rec['batch_base']}->{rec['batch_cand']} "
              f"+{len(added)}/-{len(removed)}/~{len(changed)} newB={len(new_b)} "
              f"clsBd={rec['cls_b_dur_delta']:+g} clsAd={rec['cls_a_dur_delta']:+g}", flush=True)
        if added or removed or changed:
            print(f"      added={added}\n      removed={removed}\n      changed={changed}", flush=True)

    # D-4 Default eligibility + Jazz regression
    dft = surface["carriers"]["Default"]
    jaz = surface["carriers"]["Jazz"]
    surface["d4_default_eligible"] = (dft["root_delta"] > 0 and len(dft["new_class_b"]) == 0
                                      and dft["cls_b_dur_delta"] <= 0)
    surface["jazz_no_regression"] = (len(jaz["new_class_b"]) == 0 and jaz["cls_b_dur_delta"] <= 0)
    print(f"  D-4 Default eligible (root>0, no new class-b, clsB non-increase): "
          f"{surface['d4_default_eligible']}")
    print(f"  Jazz no-regression (no new class-b, clsB non-increase): {surface['jazz_no_regression']}")

    with open(out, "a", encoding="utf-8") as f:
        f.write(json.dumps(surface, sort_keys=True) + "\n")
    print(f"SURFACE DONE -> {out}", flush=True)


if __name__ == "__main__":
    main()
