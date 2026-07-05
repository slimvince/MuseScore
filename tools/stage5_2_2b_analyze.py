#!/usr/bin/env python3
"""stage5_2_2b_analyze.py — turn the Phase-2.2b Task-1 ledgers into the report tables.
READ-ONLY. Parses the two committed ledgers + prints:
  (Task 1.1) the 14x3 cross-carrier full-corpus disable table
  (Task 1.2) per-rule firing-site counts (+ per carrier)
  (Task 1.3) founding-case touch check
  (Task 1.4) Gate-J / BiasCorrection / GateE / GateH per-case WiR-family breakdown
"""
from __future__ import annotations
import json
import sys
from collections import defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
_ROOT = Path(__file__).resolve().parent.parent
AUDIT = _ROOT / "tools" / "fit_ledgers" / "stage5_rule_disable_fullcorpus.jsonl"
FIRING = _ROOT / "tools" / "fit_ledgers" / "stage5_rule_firing_sites.jsonl"
CARRIERS = ["Baroque", "Jazz", "Default"]
RULES = ["BiasCorrection", "FM2", "GateA", "GateE", "GateF", "GateGE", "GateGB",
         "GateGC", "GateGD", "GateH", "GateI", "GateK", "GateL", "GateJ"]
# founding cases named in scoring_model §6 / the dispatch
FOUNDING = {
    "GateK": ["bwv40.6"],
    "GateL": ["bwv144.6", "bwv245.15"],
    "GateJ": ["*{R-4,R,R+3,R+6} class*"],   # structural class, checked by V-family WiR side
}


def load(path, record):
    rows = []
    if path.exists():
        for ln in path.read_text(encoding="utf-8").splitlines():
            try:
                d = json.loads(ln)
                if d.get("record") == record:
                    rows.append(d)
            except Exception:
                pass
    return rows


def main():
    audit = load(AUDIT, "audit")
    firing = load(FIRING, "firing")

    # ── baselines per carrier ──
    base = {a["carrier"]: a for a in audit if a["rule"] == "__baseline__"}
    print("=== BASELINES (all rules on, full corpus) ===")
    for c in CARRIERS:
        b = base.get(c)
        if b:
            print(f"  {c:8} root={b['root_pct']:.4f} rn={b['rn_pct']:.4f} key={b['key_pct']:.4f} "
                  f"batch={b['batch_gate']} clsB_dur={b['cls_b_dur']} clsA_dur={b['cls_a_dur']}")

    # ── Task 1.1 the 14x3 disable table ──
    print("\n=== TASK 1.1 — cross-carrier full-corpus disable table (Δ vs all-on) ===")
    amap = {(a["carrier"], a["rule"]): a for a in audit if a["rule"] != "__baseline__"}
    hdr = f"{'rule':<15}"
    for c in CARRIERS:
        hdr += f" | {c[:3]}: droot  batch(Δ)  +/-/~   clsBd    clsAd"
    print(hdr)
    for r in RULES:
        line = f"{r:<15}"
        for c in CARRIERS:
            a = amap.get((c, r))
            if not a:
                line += f" | {'--- missing ---':<38}"
                continue
            nb, rm, ch = len(a["batch_added"]), len(a["batch_removed"]), len(a["batch_class_changed"])
            line += (f" | {a['root_delta']:+.4f} {a['batch_gate']:>3}({a['batch_delta']:+d}) "
                     f"{nb}/{rm}/{ch} {a['cls_b_dur_delta']:>+7g} {a['cls_a_dur_delta']:>+7g}")
        print(line)

    # ── batch set-diffs explained per case ──
    print("\n=== TASK 1.1 — batch set-diffs (every non-empty diff, explained) ===")
    for c in CARRIERS:
        for r in RULES:
            a = amap.get((c, r))
            if not a:
                continue
            if a["batch_added"] or a["batch_removed"] or a["batch_class_changed"]:
                print(f"  [{c}] {r}: added={a['batch_added']} removed={a['batch_removed']} "
                      f"class_changed={a['batch_class_changed']}")

    # ── Task 1.2 firing-site counts per rule per carrier ──
    print("\n=== TASK 1.2 — firing-site counts (sites / WiR-covered) ===")
    counts = defaultdict(lambda: [0, 0])
    for f in firing:
        k = (f["carrier"], f["rule"])
        counts[k][0] += 1
        if f.get("wir_covered"):
            counts[k][1] += 1
    print(f"{'rule':<15}" + "".join(f" | {c[:3]}: sites(cov)" for c in CARRIERS))
    for r in RULES:
        line = f"{r:<15}"
        for c in CARRIERS:
            s, cov = counts[(c, r)]
            line += f" | {s:>4}({cov:>4})"
        print(line)

    # ── Task 1.3 founding-case touch ──
    print("\n=== TASK 1.3 — founding-case touch (Baroque carrier) ===")
    fire_by = defaultdict(set)
    for f in firing:
        if f["carrier"] == "Baroque":
            fire_by[f["rule"]].add(f["stem"])
    for rule, cases in FOUNDING.items():
        for case in cases:
            if case.startswith("*"):
                # structural class — reported via Gate-J WiR family below
                print(f"  {rule}: founding class {case} — see Gate-J WiR-family table")
                continue
            touched = case in fire_by.get(rule, set())
            print(f"  {rule}: founding {case} still touched by rule? {'YES' if touched else 'NO'}")

    # ── Task 1.4 per-case WiR-family breakdown for the 4 disable-beneficial rules ──
    print("\n=== TASK 1.4 — Gate-J / BiasCorrection / GateE / GateH per-case WiR-family (Baroque) ===")
    for rule in ["GateJ", "BiasCorrection", "GateE", "GateH"]:
        rows = [f for f in firing if f["carrier"] == "Baroque" and f["rule"] == rule
                and f.get("wir_covered")]
        fam = defaultdict(lambda: {"n": 0, "on_wir": 0, "off_wir": 0, "dur": 0})
        for f in rows:
            fk = f.get("wir_family", "none")
            fam[fk]["n"] += 1
            fam[fk]["dur"] += f.get("dur", 0)
            if f.get("on_matches_wir"):
                fam[fk]["on_wir"] += 1
            if f.get("off_matches_wir"):
                fam[fk]["off_wir"] += 1
        tot = len(rows)
        on_w = sum(1 for f in rows if f.get("on_matches_wir"))
        off_w = sum(1 for f in rows if f.get("off_matches_wir"))
        print(f"  {rule}: {tot} WiR-covered sites | ON matches WiR at {on_w}, OFF matches WiR at {off_w}")
        for fk in sorted(fam):
            d = fam[fk]
            print(f"      {fk:<14} sites={d['n']:>4} dur={d['dur']:>7} "
                  f"ON-matches-WiR={d['on_wir']:>3} OFF-matches-WiR={d['off_wir']:>3}")


if __name__ == "__main__":
    main()
