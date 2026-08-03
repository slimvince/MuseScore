#!/usr/bin/env python3
"""Re-aim drifted `home` line anchors in the backbone, from the drift report's own numbers.

WHY THIS EXISTS.  Every wave that edits a home document shifts the line anchors of every
register entry below the edit, and the standing rule is that each anchor is re-aimed **per
citation from the drift report's own line numbers, never by an assumed uniform shift** — a
uniform shift is wrong whenever two edits land in one file, or an edit lands inside a quoted
block.  Waves have re-aimed 159, 182 and 187 anchors by hand under that rule.  Doing it by hand
is where an assumed shift creeps back in, so it is done here instead: this tool takes the
verifier's OWN reported start line for each drifted entry and writes exactly that.

WHAT IT DOES, AND WHAT IT REFUSES TO DO.
  * It reads the drift from `gen_cluster_dispositions.verify_backbone`'s own machinery — the
    same `find_start_line` the guard uses — so the number written is by construction the number
    the guard reports, not a recomputation that could differ.
  * It moves ONLY the line part of `home`.  The file part is never touched: a quote that has
    MOVED FILE, or that no longer exists at its home, is a different event and is left for a
    reader.  Entries whose verbatim is not found are reported and skipped.
  * It preserves a range's WIDTH (`:395-397` -> `:408-410`).  The width is a property of the
    quoted block, not of the shift, so it is carried across unchanged; if the block itself
    changed length, the verbatim check fails first and this tool skips the entry.
  * `--check` reports what would move and writes nothing.

Establishment (#19): after a run, `gen_cluster_dispositions.py --verify` must report zero line
drift.  That is the check that makes this tool trustworthy, and it is run explicitly, never
assumed.

Run:
    python tools/audit/decisions/reaim_home_anchors.py --check
    python tools/audit/decisions/reaim_home_anchors.py
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
BACKBONE = os.path.join(HERE, "backbone_decisions.json")

sys.path.insert(0, HERE)
import gen_cluster_dispositions as gcd          # noqa: E402  (norm + find_start_line)


def drifted(backbone: dict) -> list[tuple[dict, int, int, str]]:
    """(entry, cited_start, actual_start, new_home) for every entry whose anchor has moved."""
    line_cache: dict[str, list[str]] = {}
    text_cache: dict[str, str] = {}
    out = []
    for d in backbone["decisions"]:
        home = d["home"]
        parts = home.split(":")
        fname = parts[0]
        if len(parts) < 2:
            continue
        m = re.match(r"(\d+)(?:-(\d+))?", parts[1])
        if not m:
            continue
        cited = int(m.group(1))
        end = int(m.group(2)) if m.group(2) else None

        path = os.path.join(ROOT, fname)
        if fname not in line_cache:
            if not os.path.exists(path):
                line_cache[fname] = []
                text_cache[fname] = ""
            else:
                raw = open(path, encoding="utf-8", errors="replace").read()
                text_cache[fname] = gcd.norm(raw)
                line_cache[fname] = [
                    re.sub(r"\s+", " ", re.sub(r"^\s*>+\s?", "", ln)).strip()
                    for ln in raw.splitlines()]
        needle = gcd.norm(d["verbatim"])
        if not needle or needle not in text_cache[fname]:
            continue                      # not a drift — a miss, which is a reader's problem
        found = gcd.find_start_line(line_cache[fname], needle,
                                    len(d["verbatim"].splitlines()))
        if found is None or found == cited:
            continue
        new_anchor = str(found) if end is None else f"{found}-{found + (end - cited)}"
        out.append((d, cited, found, f"{fname}:{new_anchor}"))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="report, write nothing")
    args = ap.parse_args()

    raw = open(BACKBONE, encoding="utf-8").read()
    backbone = json.loads(raw)
    roundtrip = json.dumps(json.loads(raw), indent=2, ensure_ascii=False) + "\n"
    if roundtrip != raw:
        print("REFUSED: re-serializing the untouched backbone is not byte-identical to the "
              "committed file, so writing would reformat it.")
        return 2

    moves = drifted(backbone)
    for d, cited, found, new_home in moves:
        print(f"  {d['id']}: {d['home']} -> {new_home}   (drift {found - cited:+d})")
    print(f"anchors drifted: {len(moves)}")
    if args.check or not moves:
        return 0

    for d, _c, _f, new_home in moves:
        d["home"] = new_home
    open(BACKBONE, "w", encoding="utf-8", newline="").write(
        json.dumps(backbone, indent=2, ensure_ascii=False) + "\n")
    print(f"re-aimed {len(moves)} anchor(s); run gen_cluster_dispositions.py --verify to confirm "
          "zero drift")
    return 0


if __name__ == "__main__":
    sys.exit(main())
