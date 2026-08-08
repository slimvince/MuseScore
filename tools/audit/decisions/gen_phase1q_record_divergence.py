#!/usr/bin/env python3
"""WHICH FILE STILL CARRIES THE PHASE-1Q RECORD — measured against git objects, not assumed.

WHY THIS EXISTS.  The establishment record of 2026-08-04
(`snapshot_2026-08-04_pre_home_classification_apply/establishment.json`) froze
`phase1q_reclassification.json` and its snapshot as byte-identical, and several open-items rows
describe the applying run of `gen_home_classification.py` as HELD UN-RUN since that date.  Applying
the user's Ruling 1 of 2026-08-08 required knowing whether that is still true, because the ruling
declares the phase-1q record HISTORICAL and a freeze aimed at the wrong file protects nothing.  The
answer is a claim about the repository, and a claim about the repository stated in prose is a claim
nobody can re-run — so it is measured here and every reader of it cites this file rather than
transcribing a value (D-431).

WHAT IS MEASURED, per named commit: the size, the SHA-256 and the recorded population of BOTH the
live artifact and the snapshot, and whether either matches the hash the establishment record froze.
The verdict follows from those and is not authored.

HOW THE SIDES ARE OBTAINED, and why it is not a shell read of a working-tree file (D-253).  Every
historical side is fetched as a GIT OBJECT by an explicit commit hash — the one shell form D-253
admits, because a content-addressed read errors loudly rather than returning silently-wrong content
— through a subprocess whose output is hashed here.  The working-tree sides are read by this tool,
which is a tool reading a file and not a shell text utility.

WHY IT CARRIES NO RE-DERIVATION MODE, and why that keeps it out of the guard population.  Under the
user's ruling R4 of 2026-08-04 a tool that RE-DERIVES A LIVE INVARIANT belongs in the guard list and
a tool that RECORDS A MEASUREMENT TAKEN AT A POINT IN TIME does not.  This one reads NAMED COMMITS,
so it measures the clock rather than the repository — the same construction, and the same reason, as
`gen_route_homing_edit_shape.py`.  The LIVE invariant that matters is asserted elsewhere and stays
asserted: `gen_home_classification.py` STOPS on every run if the snapshot no longer hashes to its
established value.

WHAT IT DOES NOT DO.  It reads files and writes one artifact.  It restores nothing, renames nothing,
deletes nothing, and decides nothing about what should happen to the file it reports on — that is a
filing decision about a committed artifact and it is the user's.

Run:
    python tools/audit/decisions/gen_phase1q_record_divergence.py
"""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
OUT = os.path.join(HERE, "phase1q_record_divergence.json")

sys.path.insert(0, os.path.dirname(HERE))
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

REL_LIVE = "tools/audit/decisions/phase1q_reclassification.json"
REL_SNAP = ("tools/audit/decisions/snapshot_2026-08-04_pre_home_classification_apply/"
            "phase1q_reclassification.json")
REL_EST = ("tools/audit/decisions/snapshot_2026-08-04_pre_home_classification_apply/"
           "establishment.json")

# The commits are the five this session's own start-of-session report recorded, newest first. They
# are named explicitly because a branch tip is never trusted for what is current (D-253).
COMMITS = ["03bce02e4b", "d1891db158", "bd3a608fec", "4a9c0d4827", "e10479a09f"]


class Stop(Exception):
    """A side could not be read. Never a warning."""


def git_object(sha: str, path: str) -> bytes | None:
    proc = subprocess.run(["git", "show", f"{sha}:{path}"], cwd=ROOT, capture_output=True)
    if proc.returncode != 0:
        return None
    return proc.stdout


def describe(data: bytes | None) -> dict:
    if data is None:
        return {"present": False}
    rec: dict = {"present": True, "bytes": len(data), "lines": data.count(b"\n"),
                 "sha256": hashlib.sha256(data).hexdigest()}
    try:
        rec["population"] = json.loads(data.decode("utf-8"))["population"]
    except Exception as exc:                                   # noqa: BLE001 — reported, not raised
        rec["population"] = None
        rec["unparsed"] = repr(exc)
    return rec


def main() -> int:
    est_path = os.path.join(ROOT, REL_EST)
    if not os.path.exists(est_path):
        raise Stop(f"the establishment record is missing: {REL_EST}")
    est = json.loads(open(est_path, encoding="utf-8").read())
    frozen = next(c for c in est["checks"] if c["check"].startswith("1 -"))
    established_hash = frozen["sha256_snapshot"]

    worktree = {
        "live_artifact": describe(open(os.path.join(ROOT, REL_LIVE), "rb").read()
                                  if os.path.exists(os.path.join(ROOT, REL_LIVE)) else None),
        "snapshot": describe(open(os.path.join(ROOT, REL_SNAP), "rb").read()
                             if os.path.exists(os.path.join(ROOT, REL_SNAP)) else None),
    }
    for side in worktree.values():
        side["matches_the_established_hash"] = side.get("sha256") == established_hash

    history = []
    for sha in COMMITS:
        row = {"commit": sha,
               "live_artifact": describe(git_object(sha, REL_LIVE)),
               "snapshot": describe(git_object(sha, REL_SNAP))}
        for side in ("live_artifact", "snapshot"):
            row[side]["matches_the_established_hash"] = (
                row[side].get("sha256") == established_hash)
        history.append(row)

    snapshot_intact = worktree["snapshot"]["matches_the_established_hash"]
    live_is_the_record = worktree["live_artifact"]["matches_the_established_hash"]
    live_moved_in_history = len({r["live_artifact"].get("sha256") for r in history
                                 if r["live_artifact"]["present"]}) > 1

    art = {
        "purpose": "Which file still carries the record of what the phase-1q classification pass "
                   "found, measured at named commits and in the working tree. Not a judgment about "
                   "what should happen to any file, and not an authorization for any fix, design "
                   "or inference change.",
        "generated_by": "tools/audit/decisions/gen_phase1q_record_divergence.py",
        "generated_for": "cc_instruction_away_execution.md, Task 0 — applying the user's Ruling 1 "
                         "of 2026-08-08 (`cowork_rulings_2026_08_08_pre_away.md`), which declares "
                         "the phase-1q record HISTORICAL and frozen at its established snapshot",
        "the_established_hash": {
            "value": established_hash,
            "read_from": REL_EST,
            "what_it_is": "the SHA-256 the 2026-08-04 establishment record froze for the snapshot, "
                          "which check 1 of that record also reports for the live artifact — the "
                          "two were byte-identical when the record was made",
        },
        "how_the_historical_sides_were_read": (
            "as git OBJECTS by explicit commit hash — the one shell form D-253 admits, because a "
            "content-addressed read errors loudly rather than returning silently-wrong content"
        ),
        "in_the_working_tree": worktree,
        "at_the_named_commits_newest_first": history,
        "★_what_this_measures": {
            "the_snapshot_still_carries_the_established_bytes": snapshot_intact,
            "the_file_named_for_phase_1q_still_carries_them": live_is_the_record,
            "the_file_named_for_phase_1q_has_more_than_one_content_across_these_commits":
                live_moved_in_history,
        },
        "★_what_follows_and_what_does_not": (
            "IF the snapshot is intact and the live file is not, then the record of what the "
            "phase-1q pass found survives at the SNAPSHOT and the file named for it does not carry "
            "it — so a freeze aimed at that file would protect nothing, and the freeze belongs on "
            "the snapshot, which is where `gen_home_classification.py` now puts it. IF the live "
            "file also has more than one content across these commits, then the applying run has "
            "been performed by more than one wave since the snapshot was taken, and the rows "
            "describing it as held un-run describe the LAST wave rather than the month. WHAT DOES "
            "NOT FOLLOW: any verdict about what should happen to the stale file. Restoring it from "
            "the snapshot, renaming it for what it holds and removing it are three defensible acts "
            "over a committed generated artifact, which is a filing decision and the user's."
        ),
        "★_nothing_here_is_lost": (
            "Every content this file reports is reachable: the phase-1q record at the snapshot, "
            "each intermediate at the commit named beside it, and the present classification at "
            "`home_classification.json`. Each entry additionally carries its own frozen class "
            "epochs, `class_before_the_2026_08_08_apply` among them (#12)."
        ),
    }

    with open(OUT, "w", encoding="utf-8", newline="") as fh:
        fh.write(json.dumps(art, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {os.path.relpath(OUT, ROOT)}")
    for k, v in art["★_what_this_measures"].items():
        print(f"  {k}: {v}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Stop as exc:
        print(f"STOP: {exc}")
        raise SystemExit(2)
