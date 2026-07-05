#!/usr/bin/env python3
"""stage5_2_2c_sweep.py — Task 4: candidate re-selection under the full-corpus hard stop.

Sweeps bassNoteRootBonus over {0.70..0.775} at (sameRootInversionBonus=0.475,
kWStepIn=0.125) [Baroque/Default carriers; Jazz pinned = byte-identical], and for
each point reports:
  - fitting-split (261) objective root% + feasibility (no new class-(b) batch case
    + class-(b) dur non-increase, per §4.2)
  - full-corpus surface (Baroque + Default; Jazz byte-identical by construction):
    batch count, new class-(b) batch cases vs the frozen 53/24/53 (the S-3 rule).

Selection rule (dispatch Task 4.2): the HIGHEST fitting-split objective whose
full-corpus check adds ZERO new class-(b) batch cases on ANY carrier.

Reuses the fit driver's regen + measure (a8 objective + batch cases). Reference
corpus read-only (all regen to scratch). Writes a committed trade-curve ledger.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT / "tools"))
import stage5_fit_driver as fd  # regen, measure, write_override

SCRATCH = Path("C:/tmp/stage5_2_2c/sweep")
A8_OUT = SCRATCH / "a8"
LEDGER = _ROOT / "tools" / "fit_ledgers" / "stage5_2_2c_sweep.jsonl"
FROZEN = _ROOT / "tools" / "corpus"
SWEEP = [0.70, 0.7125, 0.725, 0.7375, 0.75, 0.7625, 0.775]
FIXED = {"sameRootInversionBonus": 0.475, "kWStepIn": 0.125}


def fitting_scores():
    reg = json.loads((_ROOT / "tools" / "stage5_split_registry.json").read_text())
    return sorted(s for s, r in reg["scores"].items() if r["split"] == "fitting")


def write_scores(stems, path):
    Path(path).write_text("\n".join(stems) + "\n")
    return path


def new_class_b(cand_cases, base_cases):
    return sorted(c for c, cl in cand_cases.items() if cl == "b" and c not in base_cases)


def main():
    SCRATCH.mkdir(parents=True, exist_ok=True)
    A8_OUT.mkdir(parents=True, exist_ok=True)
    fit_file = write_scores(fitting_scores(), SCRATCH / "fitting.txt")

    print("== baselines (frozen corpus, all-on) ==")
    base_fit = fd.measure("Baroque", FROZEN, A8_OUT, fit_file)
    base_bar = fd.measure("Baroque", FROZEN, A8_OUT)
    base_def = fd.measure("Default", FROZEN, A8_OUT)
    print(f"  fitting(261) Baroque root={base_fit['root_pct']:.4f} batch={base_fit['batch_gate']} clsBdur={base_fit['cls_b_dur']}")
    print(f"  full Baroque root={base_bar['root_pct']:.4f} batch={base_bar['batch_gate']}")
    print(f"  full Default root={base_def['root_pct']:.4f} batch={base_def['batch_gate']}")

    LEDGER.write_text("")  # fresh
    rows = []
    for x in SWEEP:
        ov = dict(FIXED); ov["bassNoteRootBonus"] = x
        ovpath = SCRATCH / f"ov_{x}.txt"
        fd.write_override(ov, "Baroque", ovpath)
        ov_win = str(ovpath).replace("\\", "/")
        # regen full Baroque once -> measure both fitting-subset and full
        fd.regen("Baroque", ov_win, SCRATCH)
        m_fit = fd.measure("Baroque", SCRATCH, A8_OUT, fit_file)
        m_bar = fd.measure("Baroque", SCRATCH, A8_OUT)
        nb_fit = new_class_b(m_fit["cases"], base_fit["cases"])
        fit_clsb_ok = m_fit["cls_b_dur"] <= base_fit["cls_b_dur"]
        fit_feasible = (len(nb_fit) == 0) and fit_clsb_ok
        row = {
            "bassNoteRootBonus": x, "fixed": FIXED,
            "fit_root": round(m_fit["root_pct"], 4),
            "fit_gain": round(m_fit["root_pct"] - base_fit["root_pct"], 4),
            "fit_batch": m_fit["batch_gate"], "fit_new_class_b": nb_fit,
            "fit_clsb_dur_delta": m_fit["cls_b_dur"] - base_fit["cls_b_dur"],
            "fit_feasible": fit_feasible,
            "bar_full_root": round(m_bar["root_pct"], 4),
            "bar_full_batch": m_bar["batch_gate"],
            "bar_new_class_b": new_class_b(m_bar["cases"], base_bar["cases"]),
        }
        if fit_feasible:
            fd.regen("Default", ov_win, SCRATCH)
            m_def = fd.measure("Default", SCRATCH, A8_OUT)
            nb_def = new_class_b(m_def["cases"], base_def["cases"])
            row["def_full_root"] = round(m_def["root_pct"], 4)
            row["def_full_batch"] = m_def["batch_gate"]
            row["def_new_class_b"] = nb_def
            # Jazz pinned (no override for these params) -> byte-identical -> 0 new class-b
            row["jazz_new_class_b"] = []
            row["full_feasible"] = (len(row["bar_new_class_b"]) == 0
                                    and len(nb_def) == 0)
        else:
            row["full_feasible"] = None  # not evaluated (fitting-infeasible)
        rows.append(row)
        with open(LEDGER, "a", encoding="utf-8") as f:
            f.write(json.dumps(row, sort_keys=True) + "\n")
        print(f"  bnrb={x}: fitR={row['fit_root']} (+{row['fit_gain']}) fitFeas={fit_feasible} "
              f"fitNewB={nb_fit} | barFull batch={row['bar_full_batch']} newB={row['bar_new_class_b']} "
              f"| fullFeas={row['full_feasible']} defNewB={row.get('def_new_class_b')}")

    # selection: highest fitting objective with full_feasible True
    feasible = [r for r in rows if r.get("full_feasible")]
    sel = max(feasible, key=lambda r: r["fit_root"]) if feasible else None
    print("\n== TRADE CURVE ==")
    for r in rows:
        print(f"  bnrb={r['bassNoteRootBonus']}: fit +{r['fit_gain']} feas={r['fit_feasible']} "
              f"| full bar_batch={r['bar_full_batch']} bar_newB={len(r['bar_new_class_b'])} "
              f"def_newB={len(r.get('def_new_class_b',[])) if r.get('def_new_class_b') is not None else 'NA'} "
              f"fullFeas={r['full_feasible']}")
    print(f"\nSELECTED: {('bassNoteRootBonus=' + str(sel['bassNoteRootBonus'])) if sel else 'NONE PASS (family not adoptable at any swept value)'}")
    if sel:
        print(f"  fit_root={sel['fit_root']} (+{sel['fit_gain']}) bar_full_root={sel['bar_full_root']} "
              f"def_full_root={sel['def_full_root']} batch bar={sel['bar_full_batch']} def={sel['def_full_batch']}")


if __name__ == "__main__":
    main()
