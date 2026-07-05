#!/usr/bin/env python3
"""stage5_2_2d_sweep.py — Phase 2.2d: the (sameRootInversionBonus, kWStepIn) 2-D
sub-sweep BELOW the family-2 blocking bump.

Premise (O-11 ii / cc_stage5_phase2_2c_report.md Task 4): the coupled family-2
candidate is blocked at every swept bassNoteRootBonus, and BOTH blockers are driven
by the FIXED `sameRootInversionBonus 0.475 + kWStepIn 0.125` bump — `bwv379@11520`
at the fitting split, `bwv392@17520` at the full corpus. This driver asks the one
remaining cheap question: is there a SMALLER (srib, kw) bump that keeps a real
fitting gain and blocks NOTHING?

Grid (18 points; bassNoteRootBonus fixed 0.70 everywhere):
  sameRootInversionBonus in {0.40, 0.4125, 0.425, 0.4375, 0.45, 0.4625}   (Baroque anchor 0.40)
  kWStepIn               in {0.10, 0.1125, 0.125}                         (anchor 0.10)
  (0.40, 0.10) corner = the CURRENT values = the baseline anchor (must reproduce baseline, gain 0).

Per point (design §4.2 objective + constraints; the S-3 selection loop):
  1. fitting-split (261) objective root% + feasibility (no new class-(b) batch case
     vs the frozen 53/24/53 fitting subset + class-(b) root-disagree DURATION
     non-increase). TRACK `bwv379@11520` explicitly.
  2. For every fitting-feasible point WITH gain>0: full-corpus Baroque + Default
     (zero new class-(b) vs the frozen 53/24/53; TRACK `bwv392@17520` explicitly;
     Jazz byte-identical by construction — no Jazz override written).

Selection (Task 2): HIGHEST fitting-split gain whose full-corpus checks add ZERO new
class-(b) cases on ANY carrier. If none passes, the family-2 arc closes fully.

Reuses stage5_fit_driver (regen/measure/write_override), the frozen reference corpus
(read-only; all regen -> scratch), the a8 variant-(b) objective. Writes a committed
trade-curve ledger tools/fit_ledgers/stage5_2_2d_sweep.jsonl.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT / "tools"))
import stage5_fit_driver as fd  # regen, measure, write_override

SCRATCH = Path("C:/tmp/stage5_2_2d/sweep")
A8_OUT = SCRATCH / "a8"
LEDGER = _ROOT / "tools" / "fit_ledgers" / "stage5_2_2d_sweep.jsonl"
FROZEN = _ROOT / "tools" / "corpus"

SRIB = [0.40, 0.4125, 0.425, 0.4375, 0.45, 0.4625]
KW = [0.10, 0.1125, 0.125]
BNRB = 0.70  # fixed everywhere (family-2-closed; NOT swept)

TRACK_FIT = "bwv379@11520"   # the fitting-split blocker (2.2c)
TRACK_FULL = "bwv392@17520"  # the full-corpus blocker (2.2c Task 3, score-verified class-(b))


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

    print("== baselines (frozen corpus, all-on; NO regen) ==")
    base_fit = fd.measure("Baroque", FROZEN, A8_OUT, fit_file)
    base_bar = fd.measure("Baroque", FROZEN, A8_OUT)
    base_def = fd.measure("Default", FROZEN, A8_OUT)
    print(f"  fitting(261) Baroque root={base_fit['root_pct']:.4f} batch={base_fit['batch_gate']} clsBdur={base_fit['cls_b_dur']}")
    print(f"  full Baroque root={base_bar['root_pct']:.4f} batch={base_bar['batch_gate']}")
    print(f"  full Default root={base_def['root_pct']:.4f} batch={base_def['batch_gate']}")

    LEDGER.write_text("")  # fresh committed trade-curve ledger
    rows = []
    for srib in SRIB:
        for kw in KW:
            ov = {"sameRootInversionBonus": srib, "kWStepIn": kw, "bassNoteRootBonus": BNRB}
            ovpath = SCRATCH / f"ov_s{srib}_k{kw}.txt"
            fd.write_override(ov, "Baroque", ovpath)
            ov_win = str(ovpath).replace("\\", "/")
            # regen full Baroque once -> measure both fitting-subset and full
            fd.regen("Baroque", ov_win, SCRATCH)
            m_fit = fd.measure("Baroque", SCRATCH, A8_OUT, fit_file)
            m_bar = fd.measure("Baroque", SCRATCH, A8_OUT)
            nb_fit = new_class_b(m_fit["cases"], base_fit["cases"])
            fit_gain = round(m_fit["root_pct"] - base_fit["root_pct"], 4)
            fit_clsb_ok = m_fit["cls_b_dur"] <= base_fit["cls_b_dur"]
            fit_feasible = (len(nb_fit) == 0) and fit_clsb_ok
            nb_bar = new_class_b(m_bar["cases"], base_bar["cases"])
            row = {
                "sameRootInversionBonus": srib, "kWStepIn": kw, "bassNoteRootBonus": BNRB,
                "fit_root": round(m_fit["root_pct"], 4), "fit_gain": fit_gain,
                "fit_batch": m_fit["batch_gate"], "fit_new_class_b": nb_fit,
                "fit_clsb_dur_delta": m_fit["cls_b_dur"] - base_fit["cls_b_dur"],
                "fit_clsb_nonincrease_ok": fit_clsb_ok,
                "fit_feasible": fit_feasible,
                "track_bwv379_in_fit": TRACK_FIT in nb_fit,
                "bar_full_root": round(m_bar["root_pct"], 4),
                "bar_full_batch": m_bar["batch_gate"],
                "bar_new_class_b": nb_bar,
                "track_bwv392_in_bar": TRACK_FULL in nb_bar,
                "rn_pct": round(m_fit["rn_pct"], 4), "key_pct": round(m_fit["key_pct"], 4),
            }
            # full-corpus surface only for fitting-feasible points with a real gain (Task 1.2)
            if fit_feasible and fit_gain > 1e-9:
                fd.regen("Default", ov_win, SCRATCH)
                m_def = fd.measure("Default", SCRATCH, A8_OUT)
                nb_def = new_class_b(m_def["cases"], base_def["cases"])
                row["def_full_root"] = round(m_def["root_pct"], 4)
                row["def_full_batch"] = m_def["batch_gate"]
                row["def_new_class_b"] = nb_def
                row["track_bwv392_in_def"] = TRACK_FULL in nb_def
                # Jazz pinned (no override for these params) -> byte-identical -> 0 new class-b
                row["jazz_new_class_b"] = []
                row["full_feasible"] = (len(nb_bar) == 0 and len(nb_def) == 0)
            else:
                row["full_feasible"] = None  # not evaluated (fitting-infeasible or zero gain)
            rows.append(row)
            with open(LEDGER, "a", encoding="utf-8") as f:
                f.write(json.dumps(row, sort_keys=True) + "\n")
            print(f"  srib={srib} kw={kw}: fitR={row['fit_root']} (+{fit_gain}) "
                  f"fitFeas={fit_feasible} fitNewB={nb_fit} | barBatch={row['bar_full_batch']} "
                  f"barNewB={nb_bar} | fullFeas={row['full_feasible']} "
                  f"defNewB={row.get('def_new_class_b')}")

    # ── selection: highest fitting gain whose full-corpus adds ZERO new class-(b) anywhere ──
    feasible = [r for r in rows if r.get("full_feasible")]
    sel = max(feasible, key=lambda r: r["fit_gain"]) if feasible else None

    print("\n== 18-POINT TRADE SURFACE (fit_gain / fit_feas / bar_newB / def_newB / full_feas) ==")
    for r in rows:
        print(f"  srib={r['sameRootInversionBonus']:<7} kw={r['kWStepIn']:<7} "
              f"fit+{r['fit_gain']:<8} fitFeas={str(r['fit_feasible']):<5} "
              f"barNewB={len(r['bar_new_class_b'])} "
              f"defNewB={(len(r['def_new_class_b']) if r.get('def_new_class_b') is not None else 'NA')} "
              f"fullFeas={r['full_feasible']}")

    print("\n== TRACKED-CASE APPEARANCE MAP ==")
    print(f"  {TRACK_FIT} (fitting blocker) appears at:")
    for r in rows:
        if r["track_bwv379_in_fit"]:
            print(f"    srib={r['sameRootInversionBonus']} kw={r['kWStepIn']}")
    print(f"  {TRACK_FULL} (full-corpus blocker) appears at (Baroque full):")
    for r in rows:
        if r["track_bwv392_in_bar"]:
            print(f"    srib={r['sameRootInversionBonus']} kw={r['kWStepIn']}")

    print(f"\nSELECTED: {('srib=' + str(sel['sameRootInversionBonus']) + ' kw=' + str(sel['kWStepIn'])) if sel else 'NONE PASS (no feasible slice of the coupled gain at this grid resolution)'}")
    if sel:
        print(f"  fit_root={sel['fit_root']} (+{sel['fit_gain']}) bar_full_root={sel['bar_full_root']} "
              f"def_full_root={sel.get('def_full_root')} batch bar={sel['bar_full_batch']} def={sel.get('def_full_batch')}")


if __name__ == "__main__":
    main()
