#!/usr/bin/env python3
"""Three-way .ours.json comparison for the RETIRE-5 byte-identity diagnosis.

Compares, per preset, the frozen tools/corpus/<preset> against two scratch regen
dirs (baseline = pre-retirement 3f52f088ad, retirement = current HEAD). Prints,
for each preset, |frozen vs baseline|, |frozen vs retirement|, |baseline vs retirement|.

The decisive cell is baseline-vs-retirement: 0 diffs there == the RETIRE-5 is
byte-identical vs the true baseline (any frozen diffs are pre-existing drift).
"""
from __future__ import annotations
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
CORPUS = _ROOT / "tools" / "corpus"


def load(d: Path) -> dict:
    return {p.name: p for p in d.glob("*.ours.json")}


def diffset(a: dict, b: dict) -> list:
    common = set(a) & set(b)
    out = [n for n in sorted(common) if a[n].read_bytes() != b[n].read_bytes()]
    only = sorted(set(a) ^ set(b))
    return out, only


def main():
    baseline_root = Path(sys.argv[1])   # e.g. C:/tmp/stage5_2_2c/baseline
    retire_root = Path(sys.argv[2])     # e.g. C:/tmp/stage5_2_2c/byteproof
    presets = sys.argv[3:] or ["baroque", "jazz", "default"]
    for preset in presets:
        frozen = load(CORPUS / preset)
        base_d = CORPUS / preset  # placeholder
        base_dir = baseline_root / preset
        ret_dir = retire_root / preset
        if not base_dir.exists():
            print(f"{preset}: baseline dir missing ({base_dir}) — skipping")
            continue
        baseline = load(base_dir)
        retire = load(ret_dir)
        fb, fb_only = diffset(frozen, baseline)
        fr, fr_only = diffset(frozen, retire)
        br, br_only = diffset(baseline, retire)
        print(f"=== {preset} ===")
        print(f"  frozen vs baseline(3f52f088ad):   {len(fb)} diff  ({len(fb_only)} set-mismatch)")
        print(f"  frozen vs retirement(HEAD):       {len(fr)} diff  ({len(fr_only)} set-mismatch)")
        print(f"  baseline vs retirement (DECISIVE): {len(br)} diff  ({len(br_only)} set-mismatch)")
        if br:
            for n in br[:20]:
                print(f"      BASE!=RETIRE: {n}")


if __name__ == "__main__":
    main()
