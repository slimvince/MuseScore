#!/usr/bin/env python3
"""stage5_2_2b_snapshot_preview.py — Task-3 snapshot-impact preview (MEASUREMENT ONLY).
Runs batch_analyze --preset Default --dump-regions notation on the 11 pipeline_snapshot_tests
scores, candidate override vs baseline, and reports which of the 11 P1-P4 notation goldens WOULD
need refreshing at adoption. Nothing refreshed (nothing adopted)."""
from __future__ import annotations
import subprocess
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
BA = _ROOT / "ninja_build_rel" / "batch_analyze.exe"
BASH = Path("C:/Program Files/Git/usr/bin/bash.exe")
CAND = "C:/tmp/s5_cand_cfgI.txt"   # the Config I Default candidate (full vector; Default is an adopt target)
SCORES = [
    "tools/dcml/bach_chorales/MS3/001 Aus meines Herzens Grunde.mscx",
    "tools/dcml/bach_chorales/MS3/003 Ach Gott, vom Himmel sieh darein.mscx",
    "tools/dcml/bach_en_fr_suites/MS3/BWV806_01_Prelude.mscx",
    "tools/dcml/bach_en_fr_suites/MS3/BWV806_10_Gigue.mscx",
    "tools/dcml/mozart_piano_sonatas/MS3/K279-1.mscx",
    "tools/dcml/mozart_piano_sonatas/MS3/K280-1.mscx",
    "tools/dcml/chopin_mazurkas/MS3/BI105-1op30-1.mscx",
    "tools/dcml/chopin_mazurkas/MS3/BI105-2op30-2.mscx",
    "tools/dcml/corelli/MS3/op01n08a.mscx",
    "tools/dcml/schumann_kinderszenen/MS3/n01.mscx",
    "tools/dcml/bach_chorales/MS3/137 Du, o schönes Weltgebäude.mscx",
]


def winpath(p):
    return str(Path(p).resolve()).replace("\\", "/")


def run(score, out, override=None):
    cmd = (f'{winpath(BA)} "{winpath(score)}" "{out}" --preset Default '
           f'--dump-regions notation')
    if override:
        cmd += f' --param-override "{override}"'
    subprocess.run([str(BASH), "-c", cmd], stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, timeout=120)


def main():
    tmp = Path("C:/tmp/s5_snap")
    tmp.mkdir(parents=True, exist_ok=True)
    diff, same, fail = [], [], []
    for sc in SCORES:
        name = Path(sc).stem
        base = tmp / f"{name}.base.json"
        cand = tmp / f"{name}.cand.json"
        run(sc, str(base).replace("\\", "/"))
        run(sc, str(cand).replace("\\", "/"), CAND)
        if not base.exists() or not cand.exists():
            fail.append(name)
            continue
        if base.read_bytes() == cand.read_bytes():
            same.append(name)
        else:
            diff.append(name)
    print(f"SNAPSHOT PREVIEW (Config I candidate, --preset Default --dump-regions notation):")
    print(f"  DIFFERS ({len(diff)}): {diff}")
    print(f"  identical ({len(same)}): {same}")
    if fail:
        print(f"  FAILED ({len(fail)}): {fail}")
    print(f"  => at adoption, ~{len(diff)}/11 P1-P4 goldens would refresh.")


if __name__ == "__main__":
    main()
