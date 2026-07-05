#!/usr/bin/env python3
"""Winner-only diff between two corpus regen dirs.

For each score and each region, compares ONLY the top-level (winner) analysis
fields — rootPitchClass, chordSymbol, quality, romanNumeral, bassPitchClass,
bassIsRoot, chordScore — IGNORING the per-region 'alternatives' array. Reports,
per preset, how many scores differ in their WINNERS vs how many differ at all.

This isolates whether a change alters the chosen chord (winner) or only the
alternatives-list content/ordering.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

WINNER_KEYS = ("startTick", "rootPitchClass", "chordSymbol", "quality",
               "romanNumeral", "bassPitchClass", "bassIsRoot", "chordScore",
               "key")


def winners(path: Path):
    d = json.loads(path.read_text(encoding="utf-8"))
    regs = d.get("regions", d if isinstance(d, list) else [])
    out = []
    for r in regs:
        out.append(tuple(r.get(k) for k in WINNER_KEYS))
    return out


def main():
    a_root = Path(sys.argv[1])
    b_root = Path(sys.argv[2])
    a_files = {p.name: p for p in a_root.glob("*.ours.json")}
    b_files = {p.name: p for p in b_root.glob("*.ours.json")}
    common = sorted(set(a_files) & set(b_files))
    winner_diff = []
    byte_diff = []
    for name in common:
        ab, bb = a_files[name].read_bytes(), b_files[name].read_bytes()
        if ab != bb:
            byte_diff.append(name)
            if winners(a_files[name]) != winners(b_files[name]):
                winner_diff.append(name)
    print(f"scores compared: {len(common)}")
    print(f"byte-differing scores:   {len(byte_diff)}")
    print(f"WINNER-differing scores: {len(winner_diff)}")
    if winner_diff:
        for n in winner_diff[:40]:
            print(f"    WINNER-DIFF: {n}")
    else:
        print("  => every byte-diff is ALTERNATIVES-ONLY; winners byte-identical.")


if __name__ == "__main__":
    main()
