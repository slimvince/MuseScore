#!/usr/bin/env python3
"""The SHAPE of the 2026-08-08 document-route edits, measured against git objects.

WHY THIS EXISTS.  The wave writes three delegation clauses and twenty-eight homing blocks into
three specification files, and a claim that those edits added text without removing any is a claim
about the tree.  A claim about the tree stated in prose is a claim nobody can re-run, so it is
measured here and the report cites this file instead of transcribing the numbers (D-431).

HOW IT IS MEASURED, and why this is not a shell read of a working-tree file (D-253).  The BEFORE
side of each comparison is fetched as a GIT OBJECT by an explicit commit hash -- the form D-253
admits, because a content-addressed read errors loudly rather than returning silently-wrong content.
The AFTER side is read from disk by this tool, which is a tool reading a file and not a shell text
utility.  The comparison is a line-level opcode diff; what it reports is how many lines were
inserted, how many deleted, and how many existing lines were replaced.  ADD-ONLY means the last two
are zero.

WHY IT IS A SIBLING OF `gen_homing_edit_shape.py` RATHER THAN A PARAMETER ON IT.  That tool records
the 2026-08-07 wave's measurement against ITS named commit and must go on saying so (#12); a shared
tool with a movable commit would overwrite one wave's record with the next wave's.  Each wave's
measurement is a separate point-in-time record, which is why each gets its own file and its own
artifact.

WHY IT IS NOT IN THE GUARD LIST, and why it carries no re-derivation mode.  Under the user's ruling
R4 of 2026-08-04, a tool that RE-DERIVES A LIVE INVARIANT belongs in the guard list and a tool that
RECORDS A MEASUREMENT TAKEN AT A POINT IN TIME does not.  This one compares the working tree against
a NAMED COMMIT, so it must stop agreeing the moment that work is committed -- it measures the clock,
not the repository.  It therefore deliberately carries no re-derivation mode at all, which also
keeps it out of `gen_guard_state.py`'s derived candidate population rather than sitting there
unclassified.

WHAT IT DOES NOT DO.  It reads files and writes one artifact.  It moves no register entry, it judges
nothing about whether the inserted text is correct, and it authorizes nothing.

Run:
    python tools/audit/decisions/gen_route_homing_edit_shape.py
"""
from __future__ import annotations

import difflib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent
sys.path.insert(0, str(HERE.parent))

from output_encoding import use_utf8_output          # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

OUT = HERE / "route_homing_edit_shape.json"

# The BEFORE commit, named explicitly. It is the last commit this session's own start-of-session
# report recorded; that report's modified-path list carried no tracked file, the previous wave
# having committed and pushed its six waves as one, so the difference measured here is this wave's
# own editing and nothing else.
BEFORE_COMMIT = "03bce02e4b"

SUBJECTS = [
    ("ARCHITECTURE.md",
     "Route (i): three delegation clauses (the joint-estimator section, §11.5, §19). Route (ii): "
     "the homing blocks at §6.7, the new §6.8, the joint-estimator section, and the Layer-1, "
     "Layer-2, Layer-3, Layer-4, Layer-5 and Layer-6 sections."),
    ("docs/scoring_model.md",
     "Route (ii): the §8 homing blocks — the shelved bass-as-root pair, the tolerated "
     "quality-overwrite acceptance, the four legacy dead ends, and the voided validation basis."),
    ("OPEN_ITEMS.md",
     "Three new index rows: the D-472 conformance question, the blocked-route finding, and the "
     "admitted-`ls` observation."),
]


class Stop(Exception):
    """The BEFORE side could not be read as a git object. Never a warning."""


def before(path: str) -> list[str]:
    proc = subprocess.run(["git", "show", f"{BEFORE_COMMIT}:{path}"],
                          cwd=ROOT, capture_output=True)
    if proc.returncode != 0:
        raise Stop(f"git show {BEFORE_COMMIT}:{path} failed: "
                   f"{proc.stderr.decode('utf-8', errors='replace').strip()}")
    return proc.stdout.decode("utf-8", errors="replace").splitlines()


def shape(path: str, why: str) -> dict:
    a = before(path)
    b = (ROOT / path).read_text(encoding="utf-8").splitlines()
    ops = [o for o in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes()
           if o[0] != "equal"]
    inserted = sum(o[4] - o[3] for o in ops if o[0] == "insert")
    deleted = sum(o[2] - o[1] for o in ops if o[0] == "delete")
    replaced = sum(o[2] - o[1] for o in ops if o[0] == "replace")
    return {
        "file": path,
        "what_was_written": why,
        "lines_at_the_before_commit": len(a),
        "lines_in_the_worktree": len(b),
        "changed_regions": len(ops),
        "lines_inserted": inserted,
        "lines_deleted": deleted,
        "existing_lines_replaced": replaced,
        "add_only": deleted == 0 and replaced == 0,
        "regions": [{"operation": o[0],
                     "at_the_before_commit": [o[1] + 1, o[2]],
                     "in_the_worktree": [o[3] + 1, o[4]]} for o in ops],
    }


def main() -> int:
    rows = [shape(p, why) for p, why in SUBJECTS]
    not_add_only = [r["file"] for r in rows if not r["add_only"]]
    art = {
        "purpose": "The measured SHAPE of the 2026-08-08 document-route edits: how many lines each "
                   "file gained, and whether any existing line was deleted or replaced. NOT a "
                   "judgment about the text written, and not an authorization for any fix, design "
                   "or inference change.",
        "generated_by": "tools/audit/decisions/gen_route_homing_edit_shape.py",
        "generated_for": "cc_instruction_document_routes_and_d472.md (Tasks 1 and 2, whose ruling "
                         "record requires each clause written adds-only and each homing act to "
                         "preserve what it moves)",
        "the_before_side": {
            "commit": BEFORE_COMMIT,
            "read_as": "a git OBJECT by explicit hash — the one shell form D-253 admits, because a "
                       "content-addressed read errors loudly rather than returning silently-wrong "
                       "content",
            "why_this_commit": "It is the last commit the session's own start-of-session report "
                               "recorded, and that report listed no tracked file as modified — the "
                               "preceding wave having committed and pushed its accumulated work as "
                               "one — so what is measured is this wave's own editing and nothing "
                               "else.",
        },
        "what_add_only_means_here": "Zero lines deleted and zero existing lines replaced. A pure "
                                    "insertion: every line that was in the file before is still "
                                    "there, unchanged, in the same order.",
        "★_a_file_that_is_NOT_add_only_is_REPORTED_rather_than_excused": (
            "The three delegation clauses and every homing block are insertions, but the wave also "
            "CORRECTED two reserved-word collisions in its own new text and, at §11.5 and §19, "
            "wrote each clause beside an existing naming rather than replacing it. Where a file "
            "comes back not add-only, the `regions` list below says exactly where, and the report "
            "states it — a replaced line is not a defect on its own, but it must not be reported "
            "as an insertion."
        ),
        "★_this_is_a_POINT_IN_TIME_RECORD": (
            "It compares the worktree against a NAMED COMMIT, so it stops agreeing the moment this "
            "work is committed. Under the user's ruling R4 of 2026-08-04 that makes it a recorder "
            "rather than a guard, and it deliberately carries no re-derivation mode — which is also "
            "what keeps it out of the derived guard-candidate population instead of sitting there "
            "unclassified."
        ),
        "counted": {
            "files": len(rows),
            "files_that_are_add_only": len([r for r in rows if r["add_only"]]),
            "files_that_are_not_add_only": not_add_only,
            "total_lines_inserted": sum(r["lines_inserted"] for r in rows),
            "total_lines_deleted": sum(r["lines_deleted"] for r in rows),
            "total_existing_lines_replaced": sum(r["existing_lines_replaced"] for r in rows),
        },
        "files": rows,
    }
    OUT.write_text(json.dumps(art, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")
    for r in rows:
        print(f"  {r['file']}: +{r['lines_inserted']} / -{r['lines_deleted']} / "
              f"~{r['existing_lines_replaced']}   add-only={r['add_only']}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Stop as exc:
        print(f"STOP: {exc}")
        raise SystemExit(2)
