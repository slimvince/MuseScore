#!/usr/bin/env python3
"""
analyze_diag20.py — Classify failure modes for the 24 Cat 2 Minor→HalfDim cases.

Reads:
  tools/diag20_raw.txt  — stderr captured from run_bach_preset with DIAG20 instrumentation
  (case list hardcoded from Part A Step A2 output)

Usage:
    cd C:\s\MS && python tools/analyze_diag20.py
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

_ROOT = Path(__file__).resolve().parent.parent
_DIAG = _ROOT / "tools" / "diag20_raw.txt"

# ── Cat 2 MHD cases from Part A Step A2 ──────────────────────────────────────
# Format: (file_stem, measure, beat, winner_symbol, alt_symbol, margin, key)
CAT2_MHD_CASES = [
    ("bwv11.6",  11,  1.0, "Am6",   "F#m7b5/A",  "+0.11", "Dmaj"),
    ("bwv254",   11,  1.0, "Gm6",   "Em7b5/G",   "+0.20", "Cmaj"),
    ("bwv26.6",   4,  1.0, "Dm6",   "Bm7b5/D",   "+0.20", "Cmaj"),
    ("bwv26.6",   6,  1.0, "Gm6",   "Em7b5/G",   "+0.11", "Cmaj"),
    ("bwv268",    8,  1.0, "Am6",   "F#m7b5/A",  "+0.20", "Gmaj"),
    ("bwv291",   10,  3.0, "Gm6",   "Em7b5/G",   "+0.11", "Dmin"),
    ("bwv295",   15,  2.0, "Gm6",   "Em7b5/G",   "+0.20", "Dmin"),
    ("bwv301",    4,  3.0, "Gm6",   "Em7b5/G",   "+0.20", "Dmin"),
    ("bwv301",   14,  1.0, "Gm6",   "Em7b5/G",   "+0.11", "Dmin"),
    ("bwv327",   11,  2.0, "Em6",   "C#m7b5/E",  "+0.20", "Dmaj"),
    ("bwv334",    1,  1.0, "Cm6",   "Am7b5/C",   "+0.20", "Gmin"),
    ("bwv334",   10,  3.0, "Cm6",   "Am7b5/C",   "+0.11", "Gmin"),
    ("bwv350",    3,  1.0, "Cm6",   "Am7b5/C",   "+0.20", "Gmin"),
    ("bwv381",    6,  1.0, "Am6",   "F#m7b5/A",  "+0.20", "Emin"),
    ("bwv391",   14,  1.0, "Dm6",   "Bm7b5/D",   "+0.20", "Gmaj"),
    ("bwv397",   10,  3.0, "Cm6",   "Am7b5/C",   "+0.20", "Fmaj"),
    ("bwv40.3",   6,  1.0, "Cm6",   "Am7b5/C",   "+0.20", "Dmin"),
    ("bwv40.8",  10,  1.0, "Ebm6",  "Cm7b5/Eb",  "+0.11", "Cmin"),
    ("bwv407",    7,  4.0, "Dm6",   "Bm7b5/D",   "+0.08", "Dmaj"),
    ("bwv424",    2,  3.0, "Dm6",   "Bm7b5/D",   "+0.20", "Amin"),
    ("bwv425",    3,  1.0, "Dm6",   "Bm7b5/D",   "+0.11", "Cmaj"),
    ("bwv46.6",  15,  1.0, "Cm6",   "Am7b5/C",   "+0.20", "Fmaj"),
    ("bwv48.7",   1,  1.0, "Cm6",   "Am7b5/C",   "+0.20", "Gmin"),
    ("bwv64.8",   2,  1.0, "Am6",   "F#m7b5/A",  "+0.20", "Emin"),
]


def _stem_from_filename(path_str: str) -> str:
    """Extract chorale stem from a path like '.../bwv11.6.ours.json'."""
    name = Path(path_str).name
    # Remove known suffixes
    for suf in (".ours.json", ".music21.json", ".json"):
        if name.endswith(suf):
            name = name[: -len(suf)]
    return name


def load_diag(path: Path) -> dict[str, list[str]]:
    """
    Read diag20_raw.txt, grouping [DIAG20-*] lines by chorale stem.

    The chorale stem is inferred from [PROCESSING] lines that appear before
    each block of diagnostic output.  Falls back to grouping by appearance
    order if no PROCESSING lines are present.
    """
    if not path.exists():
        print(f"ERROR: {path} not found.  Run Step B3 first.", file=sys.stderr)
        sys.exit(1)

    by_stem: dict[str, list[str]] = defaultdict(list)
    current_stem = "__unknown__"
    diag_re = re.compile(r'\[DIAG20-')

    with path.open(encoding='utf-8', errors='replace') as fh:
        for raw in fh:
            line = raw.rstrip()
            # Detect chorale label lines: batch_analyze emits lines like
            #   [PROCESSING] bwv11.6  or  Processing: bwv11.6  etc.
            m = re.search(
                r'(?:PROCESSING|Processing|processing)[^\w]+(bwv[\w.]+)',
                line)
            if m:
                current_stem = m.group(1)
                continue
            if diag_re.search(line):
                by_stem[current_stem].append(line)

    return dict(by_stem)


def classify_case(stem: str, measure: int, beat: float, winner: str,
                  alt: str, key: str,
                  diag_by_stem: dict[str, list[str]]) -> tuple[str, list[str]]:
    """Return (failure_mode_code, matching_lines)."""
    lines = diag_by_stem.get(stem, [])
    if not lines:
        return "NO-ENTRY", []

    entry_lines  = [l for l in lines if "[DIAG20-ENTRY]" in l]
    hdx_lines    = [l for l in lines if "[DIAG20-HDX]"   in l]
    fire_lines   = [l for l in lines if "[DIAG20-FIRE]"  in l]

    if not entry_lines:
        return "NO-ENTRY", lines

    # Check if any ENTRY line shows didGFlip=1
    already_flipped = any(re.search(r'didGFlip=1', l) for l in entry_lines)
    if already_flipped:
        return "ALREADY-FLIPPED", lines

    if not hdx_lines:
        # Shouldn't normally happen (HDX always follows ENTRY)
        return "NO-HDX", lines

    not_found_lines = [l for l in hdx_lines if "not-found" in l]
    found_lines     = [l for l in hdx_lines if "found hdIdx=" in l]

    if not_found_lines and not found_lines:
        return "NO-HDX", lines

    if fire_lines:
        # Gate fired — but still a mismatch (unexpected)
        return "FIRED", lines

    if found_lines:
        # HDX found something but FIRE didn't trigger → WRONG-PC
        if len(entry_lines) > 1 or len(hdx_lines) > 1:
            return "AMBIGUOUS", lines
        return "WRONG-PC", lines

    return "AMBIGUOUS", lines


def main():
    diag_by_stem = load_diag(_DIAG)

    print(f"Loaded diagnostic data for {len(diag_by_stem)} chorales.")
    print(f"Total [DIAG20-*] lines: "
          f"{sum(len(v) for v in diag_by_stem.values())}")
    print()

    mode_counts: dict[str, int] = defaultdict(int)
    results = []

    for (stem, measure, beat, winner, alt, margin, key) in CAT2_MHD_CASES:
        mode, lines = classify_case(stem, measure, beat, winner, alt, key,
                                    diag_by_stem)
        mode_counts[mode] += 1
        results.append((stem, measure, beat, winner, alt, margin, key, mode, lines))

    # ── Summary table ──────────────────────────────────────────────────────
    print("FAILURE MODE BREAKDOWN (24 Cat 2 Minor→HalfDim cases)")
    print("=" * 60)
    for mode, count in sorted(mode_counts.items(), key=lambda x: -x[1]):
        print(f"  {mode:<18s}  {count:2d}")
    print()

    # ── Per-case detail ────────────────────────────────────────────────────
    print("PER-CASE DETAIL")
    print("=" * 60)
    for (stem, measure, beat, winner, alt, margin, key, mode, lines) in results:
        print(f"\n[{mode}] {stem}  m={measure}  beat={beat}"
              f"  winner={winner}  alt={alt}  key={key}")
        if lines:
            for l in lines:
                print(f"    {l}")
        else:
            print(f"    (no diagnostic lines for this chorale)")


if __name__ == "__main__":
    main()
