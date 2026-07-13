#!/usr/bin/env python3
"""register_lint.py — the OPEN_ITEMS.md register ID-collision check (OI-153).

READ-ONLY. The register's standing rule is "IDs are stable; do not renumber", but
nothing mechanically enforced it: two near-concurrent sessions each took "the next
free OI number" and both filed a row as OI-150 (found by Cowork 2026-07-13; the
later row was renumbered OI-152). A duplicate row ID silently makes two different
issues indistinguishable to every reader and every cross-reference.

This lint reads OPEN_ITEMS.md, collects the ID of every register ROW (the first
cell of a table row, `| OI-N | ... |`), and fails if any ID appears more than once.
Only the row ID counts — an OI-N mentioned inside another row's prose is a
cross-reference, not a row, and is ignored.

Run standalone, or as the `register` gate of tools/audit/hardening_battery.py
(where it runs at every fold, which is the point).

Usage:
    python tools/audit/register_lint.py [--register <path>]
Exit 0 iff no ID collides.
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

_ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_REGISTER = _ROOT / "OPEN_ITEMS.md"

# A register row: the ID is the FIRST cell of a markdown table row.
_ROW_ID_RE = re.compile(r"^\|\s*(OI-\d+)\s*\|")


def collect_row_ids(register_path: Path) -> dict[str, list[int]]:
    """Return {row id: [1-based line numbers where it heads a row]}."""
    ids: dict[str, list[int]] = defaultdict(list)
    text = register_path.read_text(encoding="utf-8")
    for lineno, line in enumerate(text.splitlines(), start=1):
        m = _ROW_ID_RE.match(line)
        if m:
            ids[m.group(1)].append(lineno)
    return dict(ids)


def find_collisions(ids: dict[str, list[int]]) -> dict[str, list[int]]:
    """The IDs that head more than one row."""
    return {oi: lines for oi, lines in ids.items() if len(lines) > 1}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--register", default=str(DEFAULT_REGISTER),
                    help="path to the register (default: OPEN_ITEMS.md)")
    args = ap.parse_args()

    register = Path(args.register)
    if not register.exists():
        print(f"REGISTER LINT: FAIL — register not found: {register}")
        return 1

    ids = collect_row_ids(register)
    collisions = find_collisions(ids)

    print(f"REGISTER LINT: {register.name} — {len(ids)} row IDs")
    if collisions:
        for oi, lines in sorted(collisions.items(), key=lambda kv: int(kv[0].split("-")[1])):
            print(f"  COLLISION: {oi} heads {len(lines)} rows (lines {', '.join(map(str, lines))})")
        print(f"REGISTER LINT: FAIL — {len(collisions)} colliding ID(s)")
        return 1

    print("REGISTER LINT: PASS — every row ID is unique")
    return 0


if __name__ == "__main__":
    sys.exit(main())
