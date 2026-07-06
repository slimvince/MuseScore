#!/usr/bin/env python3
"""c1_gen_substrate.py — regenerate the C1 reliability substrate on the CURRENT binary.

READ-ONLY DIAGNOSTIC GENERATION. Runs batch_analyze's two default-off diagnostic dump
paths over the frozen gate-corpus source scores (tools/corpus/*.xml) for each of the
three carriers (Baroque / Jazz / Default), writing the substrate c1_reliability.py reads:

  {out_root}/fs_{preset}/{stem}.ours.json    (--dump-fullspine   : L4/L5 + D-FS + bothLicensed)
  {out_root}/km_{preset}/{stem}.keymargin.json (--dump-region-keymargin : L3 sequence margin)

The standard .ours.json corpus is NOT touched: both dump paths `return` before the
standard writeJson (batch_analyze.cpp, verified at source). music21 GT is NOT regenerated
— c1_reliability reads it from the frozen tools/corpus/{preset} dir. Launched via Git Bash
(direct Python subprocess triggers a Qt access violation — the compare_l6_oracle idiom).

Usage: python tools/c1_gen_substrate.py --out-root C:/tmp/c1 [--workers N]
"""
from __future__ import annotations

import argparse
import concurrent.futures
import multiprocessing
import platform
import subprocess
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent

# (batch_analyze --preset value, output-dir suffix)
PRESETS = [("Baroque", "baroque"), ("Jazz", "jazz"), ("Default", "default")]


def _find_batch_analyze() -> "Path | None":
    for p in (_REPO_ROOT / "ninja_build_rel" / "batch_analyze.exe",
              _REPO_ROOT / "ninja_build_rel" / "batch_analyze"):
        if p.exists():
            return p
    return None


def _find_git_bash() -> "Path | None":
    for p in (Path("C:/Program Files/Git/usr/bin/bash.exe"),
              Path("C:/Program Files (x86)/Git/usr/bin/bash.exe")):
        if p.exists():
            return p
    return None


def _to_unix(p: Path) -> str:
    s = str(p.resolve())
    if len(s) >= 2 and s[1] == ":":
        s = "/" + s[0].lower() + s[2:]
    return s.replace("\\", "/")


def _run_one(args_tuple) -> tuple:
    """(kind, preset, stem) → (kind, preset, stem, ok). kind in {'fs','km'}."""
    kind, preset, xml_path_s, out_path_s, exe_s, bash_s = args_tuple
    exe, xml_path, out_path = Path(exe_s), Path(xml_path_s), Path(out_path_s)
    bash = Path(bash_s) if bash_s else None
    stem = xml_path.stem
    try:
        if kind == "fs":
            # fullspine → stdout, redirected to out
            core = f'{_to_unix(exe)} "{_to_unix(xml_path)}" --preset {preset} --dump-fullspine'
            cmd = f'{core} > "{_to_unix(out_path)}"'
        else:
            # keymargin → positional out path
            cmd = (f'{_to_unix(exe)} "{_to_unix(xml_path)}" "{_to_unix(out_path)}" '
                   f'--preset {preset} --dump-region-keymargin')
        if platform.system() == "Windows" and bash:
            r = subprocess.run([str(bash), "-c", cmd], stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL, timeout=180)
        else:
            r = subprocess.run(["bash", "-c", cmd], stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL, timeout=180)
        ok = (r.returncode == 0 and out_path.exists() and out_path.stat().st_size > 0)
    except Exception:
        ok = False
    return (kind, preset, stem, ok)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-root", default="C:/tmp/c1")
    ap.add_argument("--corpus-dir", default=str(_REPO_ROOT / "tools" / "corpus"))
    ap.add_argument("--workers", type=int, default=0)
    ap.add_argument("--kinds", default="fs,km", help="comma list: fs,km")
    args = ap.parse_args()

    exe = _find_batch_analyze()
    if exe is None:
        print("ERROR: batch_analyze not found", file=sys.stderr); return 1
    bash = _find_git_bash()
    out_root = Path(args.out_root)
    corpus_dir = Path(args.corpus_dir)
    kinds = [k.strip() for k in args.kinds.split(",") if k.strip()]

    xml_files = sorted(f for f in corpus_dir.glob("*.xml") if not f.stem.endswith("_m21"))
    if not xml_files:
        print(f"ERROR: no .xml in {corpus_dir}", file=sys.stderr); return 1
    print(f"Using batch_analyze: {exe}")
    print(f"Source scores: {len(xml_files)} | presets: {[p[0] for p in PRESETS]} | kinds: {kinds}")

    work = []
    for preset_name, suffix in PRESETS:
        for kind in kinds:
            sub = out_root / (f"fs_{suffix}" if kind == "fs" else f"km_{suffix}")
            sub.mkdir(parents=True, exist_ok=True)
            # clean-slate this dir's dumps
            pat = "*.ours.json" if kind == "fs" else "*.keymargin.json"
            for stale in sub.glob(pat):
                stale.unlink()
            for xml_path in xml_files:
                name = f"{xml_path.stem}.ours.json" if kind == "fs" else f"{xml_path.stem}.keymargin.json"
                out_path = sub / name
                work.append((kind, preset_name, str(xml_path), str(out_path),
                             str(exe), str(bash) if bash else ""))

    workers = args.workers or min(multiprocessing.cpu_count(), 24)
    print(f"Parallelising {len(work)} runs over {workers} workers...\n")

    fail = {}
    done = 0
    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as pool:
        futs = [pool.submit(_run_one, w) for w in work]
        for fut in concurrent.futures.as_completed(futs):
            kind, preset, stem, ok = fut.result()
            done += 1
            if not ok:
                fail.setdefault((kind, preset), []).append(stem)
            if done % 200 == 0:
                print(f"  {done}/{len(work)} done...")

    print("\n=== SUMMARY ===")
    for preset_name, suffix in PRESETS:
        for kind in kinds:
            f = fail.get((kind, preset_name), [])
            n_ok = len(xml_files) - len(f)
            tag = "OK" if not f else f"FAIL={len(f)}: {f[:8]}"
            print(f"  {kind} {preset_name:<9} {n_ok}/{len(xml_files)}  {tag}")
    total_fail = sum(len(v) for v in fail.values())
    print(f"\nTOTAL FAIL: {total_fail}")
    return 1 if total_fail else 0


if __name__ == "__main__":
    sys.exit(main())
