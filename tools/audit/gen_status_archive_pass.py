#!/usr/bin/env python3
"""The 2026-08-11 STATUS.md archive pass — perform it, and re-derive that it lost nothing.

WHAT THIS IS.  `STATUS.md`'s own banner states the standing rule that a superseded entry moves
to `STATUS_ARCHIVE.md` instead of accumulating in the must-read.  The rule had not been applied
since the 2026-07-18 doc split, and the file grew past what the file tools will return — which
is `OPEN_ITEMS.md` OI-370: a mandatory session-start read that cannot be performed.  This tool
is the second application of that rule, and the mechanism A4 of the dispatch
`cc_instruction_status_touch_and_oi141_premise_repin.md` requires: *every moved entry is
byte-identical in the archive to what left the live file, verified mechanically, not by eye.*

THE SELECTION RULE IS THE DISPATCH'S AND IS NOT THIS TOOL'S TO WIDEN (assumption A2).  An entry
moves when it is a per-task or per-batch POINTER entry whose dispatch has completed and whose
close is recorded in `cowork_away_returns.md`, or when its own text already marks it superseded
or historical.  **An entry the rule does not decide STAYS WHERE IT IS.**

HOW THE MOVED SET WAS DRAWN, and what is derived versus authored:

  * DERIVED — an entry naming `cowork_away_returns.md` in its own text has its close recorded
    there by that text, which is clause (i)'s condition established at the entry itself.  Every
    such entry from the returns file's own creating batch (2026-08-08) up to the last completed
    batch is in the moved set.
  * AUTHORED, with a STOP — an entry in the moved range that does NOT name the file needs a
    stated reason or this tool refuses to run.  Exactly one does: a per-task entry of a batch
    whose CLOSE entry names the file.  Its reason is in AUTHORED_CLAUSE below.
  * NOT MOVED, and this is the precedent deciding rather than a preference (assumption A3) —
    the most recent batch's entries stay active.  `cc_instruction_doc_split.md` §2 keeps "the
    most recent one or two" and requires the active file to stay self-sufficient for a
    context-less session start; splitting one batch's entries across the boundary would defeat
    that, so the boundary is drawn at a batch edge.
  * NOT MOVED — every entry older than the returns file itself.  Their closes are recorded in
    dispatch reports and in the handoff archive, not in `cowork_away_returns.md`, so clause (i)
    does not reach them and the rule does not decide them.

WHAT `--check` PROVES (#12, and the doc-split precedent's own reconciliation):

  1. `STATUS.md` at HEAD is EXACTLY `STATUS.md` at the base commit with the moved line range
     removed — not merely similar, byte-for-byte after the removal.
  2. The moved block appears VERBATIM, as one contiguous run of lines, inside
     `STATUS_ARCHIVE.md` at HEAD.
  3. Together: nothing left the live file that is not in the archive, and nothing else left it.

Run:
    python tools/audit/gen_status_archive_pass.py --apply    # perform the move once
    python tools/audit/gen_status_archive_pass.py --check    # re-derive the reconciliation
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(HERE, "status_archive_pass_2026_08_11.json")

# The commit the pass was performed on top of — Task 1 of the dispatch, pushed to origin/master
# before the pass began.  An explicit hash, which is the only git read D-253 permits.
BASE = "f9c9ba3f8ee43dcae9a86c9bfbfa18877a0b2a11"

# The moved range, 1-based and inclusive of the trailing blank separator, at BASE.
FIRST_LINE = 14
LAST_LINE = 117

# The one entry in the range whose close is recorded in the returns file without its own text
# saying so.  A STOP fires if any other entry in the range lacks the derived signal.
AUTHORED_CLAUSE = {
    26: "clause (i), authored: a per-TASK pointer entry of the thirteenth continuation, whose "
        "own CLOSE entry (immediately above it in the same batch) names cowork_away_returns.md "
        "and whose dispatch has completed. Clause (i) asks whether the DISPATCH's close is "
        "recorded there, not whether the task entry names the file.",
}

RETURNS = "cowork_away_returns.md"
ENTRY = re.compile(r"^\*(Last updated: )?20\d\d-\d\d-\d\d")

# Where the moved block lands in the archive: immediately above the archive's newest dated entry,
# so the archive stays newest-first, which is the doc-split precedent's own ordering.
ARCHIVE_ANCHOR = "*Last updated: 2026-07-27, eleventh entry (CC"

ARCHIVE_MARKER = (
    "> **★ THE SECOND ARCHIVE PASS — 2026-08-11.** Everything from here to the 2026-07-27 entry\n"
    "> below was moved verbatim out of `STATUS.md` by\n"
    "> `cc_instruction_status_touch_and_oi141_premise_repin.md` Task 2, applying the standing rule\n"
    "> `STATUS.md`'s own banner states: a superseded entry moves here instead of accumulating in\n"
    "> the must-read. The rule had gone unapplied since the 2026-07-18 doc split and the live file\n"
    "> grew past what the file tools will return, which is `OPEN_ITEMS.md` OI-370. **Nothing was\n"
    "> edited in transit** — the reconciliation is re-derived by\n"
    "> `tools/audit/gen_status_archive_pass.py --check` against the base commit's own git object,\n"
    "> and it proves both directions: the live file is exactly what it was minus this block, and\n"
    "> this block is exactly what left it (#12).\n"
    "\n"
)


def _git_show(rev: str, path: str) -> str:
    proc = subprocess.run(["git", "-C", ROOT, "show", f"{rev}:{path}"],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=False)
    if proc.returncode != 0:
        raise SystemExit("gen_status_archive_pass: git show failed — "
                         + proc.stderr.decode("utf-8", "replace").strip())
    return proc.stdout.decode("utf-8")


def _read(path: str) -> str:
    with open(os.path.join(ROOT, path), "r", encoding="utf-8", newline="") as fh:
        return fh.read()


def _write(path: str, text: str) -> None:
    with open(os.path.join(ROOT, path), "w", encoding="utf-8", newline="") as fh:
        fh.write(text)


def _sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _split_keep(text: str) -> list[str]:
    """Lines WITH their terminators, so a join is byte-exact."""
    return text.splitlines(keepends=True)


def _moved_entries(block: list[str], first_line: int) -> list[dict]:
    """One record per dated entry in the block, with the clause that moved it."""
    out: list[dict] = []
    for i, line in enumerate(block):
        if not ENTRY.match(line):
            continue
        n = first_line + i
        if RETURNS in line:
            clause = ("clause (i), derived: a per-task or per-batch POINTER entry whose own text "
                      "names cowork_away_returns.md, where its dispatch's close is recorded, and "
                      "whose dispatch has completed.")
        elif n in AUTHORED_CLAUSE:
            clause = AUTHORED_CLAUSE[n]
        else:
            raise SystemExit(
                f"STOP: line {n} of the moved range carries neither the derived signal nor an "
                f"authored clause. The dispatch's rule says an entry it does not decide STAYS "
                f"WHERE IT IS — so either the range is wrong or a verdict is owed.")
        out.append({
            "line_at_base": n,
            "opening": line[:150].rstrip("\r\n"),
            "moved_by": clause,
        })
    return out


def build(applied: bool) -> dict:
    base_status = _git_show(BASE, "STATUS.md")
    base_lines = _split_keep(base_status)
    lo, hi = FIRST_LINE - 1, LAST_LINE          # 0-based slice
    block = base_lines[lo:hi]
    kept = base_lines[:lo] + base_lines[hi:]

    entries = _moved_entries(block, FIRST_LINE)
    block_text = "".join(block)

    head_status = _read("STATUS.md")
    head_archive = _read("STATUS_ARCHIVE.md")

    live_exact = (head_status == "".join(kept)) if applied else None
    archive_has_block = (block_text in head_archive) if applied else None

    return {
        "purpose": "The 2026-08-11 STATUS.md archive pass: which entries moved, which clause of "
                   "the dispatch's rule moved each, and the mechanical proof that nothing was "
                   "lost or altered in transit (#12). Every figure here is computed; none is "
                   "transcribed (D-431).",
        "generated_by": "tools/audit/gen_status_archive_pass.py",
        "the_rule_it_applies": {
            "source": "cc_instruction_status_touch_and_oi141_premise_repin.md, assumption A2",
            "verbatim": "an entry moves when it is a per-task or per-batch POINTER entry whose "
                        "dispatch has completed and whose close is recorded in "
                        "`cowork_away_returns.md`, or when its own text already marks it "
                        "superseded or historical. An entry the rule does not decide STAYS "
                        "WHERE IT IS.",
            "what_is_derived": "clause (i)'s condition, from each entry's own text naming the "
                               "returns file",
            "what_is_authored": "one entry's clause, listed in the tool's AUTHORED_CLAUSE, with "
                                "a STOP on any other entry lacking the derived signal",
        },
        "the_boundary_and_why_it_falls_there": {
            "newer_side_NOT_moved": "The most recent batch's entries stay active. "
                                    "cc_instruction_doc_split.md §2 keeps 'the most recent one or "
                                    "two' entries and requires the active file to stay "
                                    "self-sufficient for a context-less session start; the "
                                    "boundary is drawn at a BATCH edge so one batch's entries are "
                                    "not split across it. That is the precedent deciding, which "
                                    "is what assumption A3 asks of it.",
            "older_side_NOT_moved": "Every entry older than cowork_away_returns.md itself. Their "
                                    "closes are recorded in dispatch reports and in the handoff "
                                    "archive, not in the returns file, so clause (i) does not "
                                    "reach them and the rule does not decide them. They stay, and "
                                    "the remainder is UNTOUCHED rather than partly worked (D-672).",
        },
        "base_commit": BASE,
        "moved_range_at_base": {"first_line": FIRST_LINE, "last_line": LAST_LINE},
        "counted": {
            "dated_entries_moved": len(entries),
            "lines_moved": len(block),
            "lines_in_STATUS_md_at_base": len(base_lines),
            "lines_in_STATUS_md_after": len(kept),
        },
        "moved_block_sha256": _sha(block_text),
        "moved_entries": entries,
        "reconciliation": {
            "STATUS_md_at_head_is_exactly_the_base_minus_the_moved_range": live_exact,
            "the_moved_block_appears_verbatim_in_STATUS_ARCHIVE_md": archive_has_block,
            "what_that_proves_together": "Nothing left the live file that is not in the archive, "
                                         "and nothing else left it. Both are byte comparisons "
                                         "against the base commit's own git object, not against "
                                         "the memory of performing the move (#15).",
        },
    }


def apply_move() -> None:
    base_lines = _split_keep(_git_show(BASE, "STATUS.md"))
    lo, hi = FIRST_LINE - 1, LAST_LINE
    block = "".join(base_lines[lo:hi])
    _moved_entries(base_lines[lo:hi], FIRST_LINE)      # raises before anything is written

    live = _read("STATUS.md")
    if block not in live:
        raise SystemExit("STOP: the moved range is not present verbatim in the working-tree "
                         "STATUS.md — the file has changed under the pass and the range is stale.")
    _write("STATUS.md", live.replace(block, "", 1))

    archive = _read("STATUS_ARCHIVE.md")
    if ARCHIVE_ANCHOR not in archive:
        raise SystemExit("STOP: the archive's newest dated entry was not found, so the "
                         "newest-first insertion point cannot be located.")
    if block in archive:
        raise SystemExit("STOP: the block is already in the archive — the pass has run.")
    at = archive.index(ARCHIVE_ANCHOR)
    _write("STATUS_ARCHIVE.md", archive[:at] + ARCHIVE_MARKER + block + archive[at:])


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--apply", action="store_true", help="perform the move (once)")
    g.add_argument("--check", action="store_true", help="re-derive the reconciliation")
    args = ap.parse_args()

    if args.apply:
        apply_move()

    art = build(applied=True)
    text = json.dumps(art, indent=2, ensure_ascii=False) + "\n"

    if args.check:
        try:
            with open(OUT, "r", encoding="utf-8") as fh:
                committed = fh.read()
        except FileNotFoundError:
            print(f"FAIL: {os.path.relpath(OUT, ROOT)} does not exist")
            return 1
        if committed != text:
            print(f"FAIL: re-derivation differs from the committed artifact: "
                  f"{os.path.relpath(OUT, ROOT)}")
            return 1
    else:
        with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        print(f"wrote {os.path.relpath(OUT, ROOT)}")

    rec = art["reconciliation"]
    ok = (rec["STATUS_md_at_head_is_exactly_the_base_minus_the_moved_range"] is True
          and rec["the_moved_block_appears_verbatim_in_STATUS_ARCHIVE_md"] is True)
    print(f"  dated entries moved: {art['counted']['dated_entries_moved']}")
    print(f"  live file is exactly base-minus-range: "
          f"{rec['STATUS_md_at_head_is_exactly_the_base_minus_the_moved_range']}")
    print(f"  moved block verbatim in the archive:   "
          f"{rec['the_moved_block_appears_verbatim_in_STATUS_ARCHIVE_md']}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
