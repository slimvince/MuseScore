#!/usr/bin/env python3
"""stage5_2_2b_dlc_probe.py — Task 1.5 DLC generalization probe (validation-only, NC data,
shapes no value). Runs run_dlc_baseline.py on 2-3 DLC styles under three configs:
  (baseline) no override; (a) the inert-7 disabled; (b) GateJ disabled.
Reports per-style DCML root-agree deltas. Reuses run_dlc_baseline --param-override (O-8).
Writes tools/fit_ledgers/stage5_dlc_probe.jsonl (committed evidence)."""
from __future__ import annotations
import json
import shutil
import subprocess
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
RESULTS = _ROOT / "tools" / "corpus_dlc_wave1" / "results.json"
LEDGER = _ROOT / "tools" / "fit_ledgers" / "stage5_dlc_probe.jsonl"
CORPORA = "corelli,mozart_piano_sonatas,schumann_kinderszenen"
LIMIT = "12"
CONFIGS = [
    ("baseline", None),
    ("inert7_off", "C:/tmp/s5_dlc/inert7.txt"),
    ("gatej_off", "C:/tmp/s5_dlc/gatej.txt"),
]


def run_cfg(name, override):
    cmd = [sys.executable, str(_ROOT / "tools" / "run_dlc_baseline.py"),
           "--corpora", CORPORA, "--limit", LIMIT, "--timeout", "120"]
    if override:
        cmd += ["--param-override", override]
    print(f"=== config {name} (override={override}) ===", flush=True)
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(f"  FAILED rc={r.returncode}: {r.stderr[-400:]}", flush=True)
    res = {}
    if RESULTS.exists():
        try:
            res = json.loads(RESULTS.read_text(encoding="utf-8"))
        except Exception:
            res = {}
    out = {}
    for repo, rec in res.items():
        out[repo] = {"root_agree_pct": rec.get("root_agree_pct"),
                     "rn_agree_pct": rec.get("rn_agree_pct"),
                     "root_aligned": rec.get("root_aligned"),
                     "movements_run": rec.get("movements_run")}
    return out


def main():
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    if LEDGER.exists():
        LEDGER.unlink()
    all_res = {}
    for name, override in CONFIGS:
        out = run_cfg(name, override)
        all_res[name] = out
        with open(LEDGER, "a", encoding="utf-8") as f:
            f.write(json.dumps({"record": "dlc", "config": name, "override": override,
                                "per_style": out}, sort_keys=True) + "\n")
        for repo, rec in out.items():
            print(f"  {name:<12} {repo:<26} root_agree={rec['root_agree_pct']}% "
                  f"(aligned={rec['root_aligned']} n={rec['movements_run']})", flush=True)

    print("\n=== DLC PROBE — root-agree deltas vs baseline ===", flush=True)
    base = all_res.get("baseline", {})
    for name in ("inert7_off", "gatej_off"):
        cfg = all_res.get(name, {})
        for repo in base:
            b = base[repo].get("root_agree_pct")
            v = cfg.get(repo, {}).get("root_agree_pct")
            if b is not None and v is not None:
                print(f"  {name:<12} {repo:<26} {b}% -> {v}%  Δ={round(v-b,2):+}", flush=True)
    print("DLC PROBE DONE", flush=True)


if __name__ == "__main__":
    main()
