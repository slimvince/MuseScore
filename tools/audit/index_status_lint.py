#!/usr/bin/env python3
"""THE STANDING LINT ON THE OPEN-ITEMS INDEX'S STATUS CELLS — one canonical opening token per row.

WHAT IT ENFORCES.  The user's Ruling 33 of 2026-08-09
(`cowork_rulings_2026_08_09_fifth_stop.md`): **every INDEX status cell begins with one canonical
token.**  A cell whose opening is not canonical is a STOP, and so is a row that does not split into
the expected number of cells.

WHY IT EXISTS.  Three rows recorded one defect in the ONE index parser, in three directions — a
mention of ANOTHER row's resolved mark reading as this row's own resolution (OI-356), a resolution
spelled in WORDS reading as open (OI-361), and a malformed row dropped SILENTLY, present in no
population at all (OI-362).  All three come of deciding a row's state by searching its prose.  With
a canonical opening the state is read from one token, and the two mis-readings become impossible
rather than unlikely; the silent drop becomes a STOP.

WHERE THE ONE DEFINITION LIVES (#6).  This module owns the canonical vocabulary, the row pattern,
the row split and the leading-token function.  `tools/audit/gen_nongating_apparatus_rows.py` — the
ONE index parser every derivation over the register imports — reads a row's state through
`leading_token` here rather than re-implementing it, and the one-off normalization pass
(`gen_index_status_normalization.py`) uses the same functions to decide every row both ways.

WHAT IT DOES NOT DO.  It does not judge whether a row's recorded state is CORRECT — that is what
the row's own text says and what a resolution act decides.  It checks only that the state is
STATED in a form every derivation reads the same way.

Run:  python tools/audit/index_status_lint.py [--check]
"""
from __future__ import annotations

import argparse
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
INDEX = os.path.join(ROOT, "OPEN_ITEMS.md")

sys.path.insert(0, HERE)
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

ROW = re.compile(r"^\| OI-")
CELLS_PER_ROW = 6
RESOLVED_MARK = "✅"

# ── THE CANONICAL VOCABULARY ─────────────────────────────────────────────────────────────────
# DERIVED, not invented, and deliberately SMALL. `gen_index_status_normalization.py --survey`
# reported the opening words every status cell used at HEAD before the normalization ran; the two
# things those openings actually carry are the RESOLVED MARK and a handful of open-state words,
# with everything else being a date, a decorative marker or a sentence. So the vocabulary is:
#
#   * the resolved mark AT THE HEAD OF THE CELL means RESOLVED — whatever word follows it, because
#     the index uses many (RESOLVED, RULED, CLOSED, SUPERSEDED, CERTIFIED, RATIFIED, ANSWERED,
#     ESTABLISHED, SETTLED, VERIFIED, DECIDED, COMPLETE, FIXED, TRIAGED, EXECUTED, DONE …) and
#     enumerating English past participles would be inventing a vocabulary rather than deriving
#     one;
#   * one of the OPEN-STATE WORDS below means OPEN.
#
# A cell whose opening is neither is a STOP — never a silent pass. That is the half of Ruling 33
# which keeps the vocabulary from widening by accident, and it is why a row cannot record its state
# in a form some derivation reads differently.
#
# ADDING AN OPEN-STATE WORD is a change to what the index may say and belongs to the act that needs
# it, with the row that introduces it named.
RESOLVED_AT_HEAD = RESOLVED_MARK          # the mark, at position 0 of the cell

OPEN_STATE_WORDS: dict[str, str] = {
    "OPEN": "the ordinary open state, and the overwhelming majority of the index",
    "DEFERRED": "open, and deferred by a named decision",
    "DECLARED": "open, and declared to the other side rather than acted on",
    "PROBED": "open, with a probe's finding recorded on it",
    "STANDING": "open by construction — a standing constraint that does not close",
    # The one row whose single open/resolved bit its own text does not settle (OI-361's own
    # reading: superseded in fact on one surface, still live on the legacy notation path and
    # retiring with it). MIXED reads as OPEN — the state it already held — so recording the
    # unsettledness moves nothing and hides nothing.
    "MIXED": "open, and the row's own text does not settle a single open/resolved bit for it",
}

CANONICAL: dict[str, str] = {RESOLVED_AT_HEAD: "resolved",
                             **{w: "open" for w in OPEN_STATE_WORDS}}


def split_row(line: str) -> list[str]:
    """The ONE row split (#6). A row that does not yield CELLS_PER_ROW cells is malformed."""
    return [c.strip() for c in line.strip().strip("|").split(" | ")]


def leading_token(status: str) -> str | None:
    """The canonical token a status cell opens with, or None if its opening is not canonical.

    Whitespace only is stripped. No markup is skipped and no synonym is recognised: a cell that
    opens with bold text or with a decorative marker is NOT canonical, and that narrowness is the
    point — the state must be readable from the head of the cell by every derivation alike, without
    any of them agreeing on how much prose to look through first.
    """
    head = status.lstrip()
    for tok in sorted(CANONICAL, key=len, reverse=True):
        if head.startswith(tok):
            return tok
    return None


def scan() -> tuple[list[dict], list[dict]]:
    """(offenders, malformed) over the index at HEAD."""
    offenders, malformed = [], []
    with open(INDEX, encoding="utf-8") as fh:
        for lineno, ln in enumerate(fh.read().splitlines(), 1):
            if not ROW.match(ln):
                continue
            cells = split_row(ln)
            if len(cells) != CELLS_PER_ROW:
                malformed.append({"line": lineno, "cells_found": len(cells),
                                  "id": cells[0] if cells else None, "opening": ln[:160]})
                continue
            if leading_token(cells[4]) is None:
                offenders.append({"line": lineno, "id": cells[0],
                                  "status_cell_opening": cells[4][:120]})
    return offenders, malformed


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="the standing form: exit nonzero on any offender (the default too)")
    ap.parse_args()

    offenders, malformed = scan()
    print(f"INDEX STATUS LINT: {os.path.relpath(INDEX, ROOT)}")
    if malformed:
        for m in malformed:
            print(f"  MALFORMED line {m['line']}: {m['cells_found']} cells — {m['opening']}")
    for o in offenders:
        print(f"  NON-CANONICAL {o['id']} (line {o['line']}): {o['status_cell_opening']}")
    if malformed or offenders:
        print(f"STOP: {len(malformed)} malformed row(s), {len(offenders)} non-canonical "
              f"opening(s). Every status cell must begin with one canonical token "
              f"(Ruling 33, 2026-08-09); the vocabulary is in this file.")
        return 1
    print("INDEX STATUS LINT: PASS — every status cell opens with one canonical token, and every "
          "row splits.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
