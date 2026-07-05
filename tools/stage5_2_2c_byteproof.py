#!/usr/bin/env python3
"""stage5_2_2c_byteproof.py — corpus byte-identity proof for a src change.

Regenerates each preset to a scratch dir with NO param-override (default values)
using the current binary, then diffs every *.ours.json against the FROZEN
tools/corpus/<preset> reference. Zero diffs == the change is corpus-byte-identical.

Used for Task 1f (RETIRE-5 proof) and Task 2 (per-carrier-scoping proof).
Reference corpus is read-only (all output to scratch). Prints a per-preset diff
count and a final PASS/FAIL. Nothing is written under tools/corpus/.

Usage:
    python tools/stage5_2_2c_byteproof.py --scratch C:/tmp/stage5_2_2c/byteproof [--label <tag>]
"""
from __future__ import annotations
import argparse
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
_ROOT = Path(__file__).resolve().parent.parent
CORPUS = _ROOT / "tools" / "corpus"
BATCH = _ROOT / "ninja_build_rel" / "batch_analyze.exe"
PRESETS = ["Baroque", "Jazz", "Default"]


def regen(preset: str, scratch_root: Path) -> Path:
    out = scratch_root / preset.lower()
    cmd = [sys.executable, str(_ROOT / "tools" / "run_bach_preset.py"),
           "--preset", preset,
           "--batch-analyze", str(BATCH),
           "--corpus-dir", str(CORPUS),
           "--output-dir", str(out)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"regen failed ({preset}):\n{r.stderr[-800:]}")
    return out


def diff_preset(preset: str, scratch_out: Path) -> dict:
    frozen = CORPUS / preset.lower()
    frozen_files = {p.name: p for p in frozen.glob("*.ours.json")}
    scratch_files = {p.name: p for p in scratch_out.glob("*.ours.json")}
    only_frozen = sorted(set(frozen_files) - set(scratch_files))
    only_scratch = sorted(set(scratch_files) - set(frozen_files))
    differing = []
    for name in sorted(set(frozen_files) & set(scratch_files)):
        if frozen_files[name].read_bytes() != scratch_files[name].read_bytes():
            differing.append(name)
    return {
        "preset": preset,
        "frozen_count": len(frozen_files),
        "scratch_count": len(scratch_files),
        "only_frozen": only_frozen,
        "only_scratch": only_scratch,
        "differing": differing,
        "identical": (not only_frozen and not only_scratch and not differing),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--scratch", required=True)
    ap.add_argument("--label", default="")
    args = ap.parse_args()
    scratch_root = Path(args.scratch)
    scratch_root.mkdir(parents=True, exist_ok=True)

    print(f"byteproof {args.label} :: binary={BATCH}")
    all_ok = True
    for preset in PRESETS:
        out = regen(preset, scratch_root)
        d = diff_preset(preset, out)
        status = "IDENTICAL" if d["identical"] else "DIFFERS"
        print(f"  {preset:8s} frozen={d['frozen_count']} scratch={d['scratch_count']} "
              f"differing={len(d['differing'])} only_frozen={len(d['only_frozen'])} "
              f"only_scratch={len(d['only_scratch'])} -> {status}")
        if not d["identical"]:
            all_ok = False
            for n in d["differing"][:20]:
                print(f"      DIFF: {n}")
            for n in d["only_frozen"][:20]:
                print(f"      ONLY_FROZEN: {n}")
            for n in d["only_scratch"][:20]:
                print(f"      ONLY_SCRATCH: {n}")
    print(f"RESULT: {'PASS (corpus-byte-identical x3)' if all_ok else 'FAIL (non-byte-identical)'}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
