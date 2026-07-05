#!/usr/bin/env python3
"""stage5_2_2e_liveness.py — O-10 retained-rule LIVENESS re-measurement at the 2.2e adoption.

Design O-10 (2026-07-05): the four RETAINED §6 rules (GateI, FM2, GateJ, GateL) carry ongoing
firing-site evidence so a rule whose founding cases silently get absorbed upstream surfaces as a
FINDING (the Gate-K/Gate-L failure mode) instead of by archaeology. This is the FIRST application:
re-measure their firing sites on the NEW (2.2e-adopted) corpus, using the 2.2b regen-diff method,
and append to the liveness ledger with the 2.2b prior counts beside each (a collapse to zero => a
finding to report).

Method (reused verbatim from stage5_2_2b_evidence.firing_sites): the ADOPTED tools/corpus/<preset>
.ours.json is the baseline (rule ON — byte-identical to a no-override regen of the adopted binary);
regen each rule OFF (disable_rule) to scratch; a union-of-region-boundaries cell whose chosen
root_pc OR chord_symbol differs is an effective firing site (merged into runs).

READ-ONLY w.r.t. the frozen corpus (baseline is read, never written; all regen -> scratch).
Writes committed tools/fit_ledgers/stage5_2_2e_liveness.jsonl.
"""
from __future__ import annotations
import json
import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT / "tools"))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import stage5_fit_driver as drv          # regen / write_override
import stage5_2_2b_evidence as ev        # firing_sites / load_regions / wir_context

CORPUS = _ROOT / "tools" / "corpus"       # the ADOPTED baseline (rule ON)
LEDGER = _ROOT / "tools" / "fit_ledgers" / "stage5_2_2e_liveness.jsonl"
SCRATCH = Path("C:/tmp/stage5_2_2e/liveness")

# The four RETAINED rules and the carriers on which each fired in the 2.2b measurement.
RETAINED = {
    "FM2":   ["Baroque"],
    "GateI": ["Baroque", "Jazz", "Default"],
    "GateJ": ["Baroque", "Jazz", "Default"],
    "GateL": ["Jazz"],
}
# 2.2b prior firing-site counts (tools/fit_ledgers/stage5_rule_firing_sites.jsonl).
PRIOR_2_2B = {
    ("FM2", "Baroque"): 16,
    ("GateI", "Baroque"): 28, ("GateI", "Jazz"): 186, ("GateI", "Default"): 30,
    ("GateJ", "Baroque"): 133, ("GateJ", "Jazz"): 248, ("GateJ", "Default"): 139,
    ("GateL", "Jazz"): 18,
}


def baseline_regions(carrier):
    """Load the ADOPTED tools/corpus/<preset> region maps (rule ON), keyed by stem."""
    plower = carrier.lower()
    cache = {}
    for bp in sorted((CORPUS / plower).glob("*.ours.json")):
        stem = bp.stem.replace(".ours", "")
        cache[stem] = ev.load_regions(bp)
    return cache


def main():
    SCRATCH.mkdir(parents=True, exist_ok=True)
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    LEDGER.write_text("")   # fresh compact per-run ledger

    base_cache = {}   # carrier -> {stem: regions}
    findings = []
    print(f"O-10 LIVENESS re-measurement (2.2e adopted corpus baseline = {CORPUS})", flush=True)
    for rule, carriers in RETAINED.items():
        for carrier in carriers:
            t = time.time()
            plower = carrier.lower()
            if carrier not in base_cache:
                base_cache[carrier] = baseline_regions(carrier)
            base = base_cache[carrier]

            off_root = SCRATCH / rule / carrier
            ov = off_root / f"override_{plower}.txt"
            off_root.mkdir(parents=True, exist_ok=True)
            drv.write_override({}, carrier, ov, disable_rules=[rule])
            drv.regen(carrier, str(ov).replace("\\", "/"), off_root)

            n_sites = n_cov = 0
            for op in sorted((off_root / plower).glob("*.ours.json")):
                stem = op.stem.replace(".ours", "")
                base_regions = base.get(stem)
                if base_regions is None:
                    continue
                off_regions = ev.load_regions(op)
                wir, spans = ev.wir_context(stem, base_regions)
                for s in ev.firing_sites(base_regions, off_regions, wir, spans):
                    n_sites += 1
                    if s["wir_covered"]:
                        n_cov += 1
            prior = PRIOR_2_2B.get((rule, carrier))
            live = n_sites > 0
            rec = {"record": "liveness", "phase": "2.2e", "rule": rule, "carrier": carrier,
                   "sites": n_sites, "wir_covered_sites": n_cov,
                   "prior_2_2b_sites": prior,
                   "delta_vs_2_2b": (n_sites - prior) if prior is not None else None,
                   "live": live,
                   "collapsed_to_zero": (not live)}
            if not live:
                findings.append((rule, carrier, prior))
            with open(LEDGER, "a", encoding="utf-8") as f:
                f.write(json.dumps(rec, sort_keys=True) + "\n")
            print(f"  {rule:<7} {carrier:<8} sites={n_sites:<4} (cov={n_cov}) "
                  f"prior_2.2b={prior} delta={rec['delta_vs_2_2b']:+d} "
                  f"live={'YES' if live else '*** ZERO (FINDING) ***'} ({time.time()-t:.0f}s)", flush=True)

    print("\nO-10 LIVENESS SUMMARY:", flush=True)
    if findings:
        print("  *** COLLAPSE-TO-ZERO FINDINGS (report to Cowork): ***", flush=True)
        for rule, carrier, prior in findings:
            print(f"    {rule}/{carrier}: 0 firing sites (was {prior} at 2.2b)", flush=True)
    else:
        print("  all four retained rules LIVE on every measured carrier (no collapse).", flush=True)
    print(f"LIVENESS DONE -> {LEDGER}", flush=True)


if __name__ == "__main__":
    main()
