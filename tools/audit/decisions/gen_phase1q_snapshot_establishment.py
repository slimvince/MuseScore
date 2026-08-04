#!/usr/bin/env python3
"""Establish the phase-1q snapshot as FAITHFUL, before the home-classification apply destroys it.

THE RULING (user, 2026-08-04, dispatch `cc_instruction_phase1_delegations_and_corrections.md` R2):
the phase-1q record is SNAPSHOTTED and the snapshot ESTABLISHED as faithful BEFORE
`gen_home_classification.py`'s apply mode is run.  This is the O-12 pattern gate block (A)
already uses: snapshot the outgoing reference first, and establish it before relying on it (#19).

WHAT IS ESTABLISHED, and how - three independent checks, none of which is an assertion:

  1. BYTE IDENTITY to the artifact being replaced.  The snapshot and
     `phase1q_reclassification.json` are compared byte for byte and by SHA-256.
  2. THE ARTIFACT IS THE COMMITTED ONE.  `tools/audit/changed_paths.py` is the sanctioned
     reader of the working-tree change list, and it must NOT carry the artifact - so the file
     on disk is what the repository holds at the last commit, and the snapshot therefore
     records the COMMITTED record rather than an uncommitted intermediate.
  3. THE SNAPSHOT PARSES AND CARRIES THE FINDING.  A byte-identical copy of a corrupt file is
     still faithful, so faithfulness alone is not enough to rely on: the snapshot is parsed and
     the three fields OI-291 and D-432 cite - the population, the pre-apply class totals and the
     `the_phase_1r_re_run` block - are read out of it and reported.  A snapshot that cannot be
     read is not a record.

THE STOP.  Any check failing exits non-zero and says so.  The apply must not run in that case -
running it would then destroy a record whose copy is not established, which is the loss OI-305
exists to prevent.

★ THE RECORD IS FROZEN AT THE MOMENT IT WAS MADE, AND `--check` VERIFIES ONLY WHAT MUST STILL BE
TRUE.  Checks 1 and 2 are statements about the moment BEFORE the apply ran: the snapshot matched
the artifact byte for byte, and that artifact was the committed one.  Both become false the instant
the apply rewrites the artifact - which is the apply working, not the establishment failing.  A
`--check` that re-ran them would therefore fail forever after the act it exists to license, which
is the OI-301 / OI-305 shape a third time: a historical record whose own guard contradicts it.

So the record is written ONCE and thereafter READ; the frozen verdicts are re-read from it rather
than recomputed.  What `--check` re-verifies is what must remain true for the record to be worth
anything: **the snapshot file still hashes to the value the record froze, and it still parses and
carries the fields OI-291 and D-432 cite.**  A snapshot that is edited, truncated or lost is caught;
an apply that has since run is not mistaken for one.

Usage:
  python tools/audit/decisions/gen_phase1q_snapshot_establishment.py           # write the record
  python tools/audit/decisions/gen_phase1q_snapshot_establishment.py --check   # re-verify
"""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
LIVE = os.path.join(HERE, "phase1q_reclassification.json")
SNAPDIR = os.path.join(HERE, "snapshot_2026-08-04_pre_home_classification_apply")
SNAP = os.path.join(SNAPDIR, "phase1q_reclassification.json")
OUT = os.path.join(SNAPDIR, "establishment.json")

sys.path.insert(0, os.path.dirname(HERE))
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 - the findings must survive a non-console stdout

REL_ARTIFACT = "tools/audit/decisions/phase1q_reclassification.json"


def sha256(path: str) -> str:
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def changed_paths() -> list[str]:
    """The sanctioned reader of the working-tree change list (D-253)."""
    res = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "audit", "changed_paths.py")],
                         capture_output=True, text=True, encoding="utf-8", cwd=ROOT)
    if res.returncode != 0:
        raise SystemExit("STOP: tools/audit/changed_paths.py failed:\n" + (res.stderr or ""))
    out = []
    for line in res.stdout.splitlines():
        parts = line.split("\t")
        if len(parts) == 2:
            out.append(parts[1].strip())
    return out


def frozen_record() -> dict | None:
    """The record as written, if it exists. Read back, never recomputed (see the docstring)."""
    if not os.path.exists(OUT):
        return None
    return json.loads(open(OUT, encoding="utf-8").read())


def build() -> tuple[dict, int]:
    checks = []
    rc = 0
    prior = frozen_record()
    snap_bytes = open(SNAP, "rb").read()
    snap_hash = sha256(SNAP)

    if prior is None:
        # ── first run: the two moment-in-time checks are MADE here, before the apply ──
        live_bytes = open(LIVE, "rb").read()
        identical = live_bytes == snap_bytes
        checks.append({
            "check": "1 - byte identity to the artifact being replaced",
            "when": "made once, BEFORE the apply ran; frozen thereafter",
            "what_was_compared": [REL_ARTIFACT, os.path.relpath(SNAP, ROOT).replace("\\", "/")],
            "bytes_equal": identical,
            "sha256_artifact": sha256(LIVE),
            "sha256_snapshot": snap_hash,
            "verdict": "PASS" if identical else "FAIL",
        })
        if not identical:
            rc = 1

        changed = changed_paths()
        uncommitted = REL_ARTIFACT in changed
        checks.append({
            "check": "2 - the artifact snapshotted is the COMMITTED one",
            "when": "made once, BEFORE the apply ran; frozen thereafter",
            "how": "tools/audit/changed_paths.py, the sanctioned reader of the working-tree "
                   "change list (D-253). The artifact must NOT appear in it.",
            "artifact_in_the_change_list": uncommitted,
            "changed_path_records": len(changed),
            "verdict": "PASS" if not uncommitted else "FAIL",
            "why_this_matters": (
                "If the artifact were dirty, the snapshot would freeze an uncommitted "
                "intermediate and the record OI-305 protects would still be the one at the last "
                "commit."
            ),
        })
        if uncommitted:
            rc = 1
    else:
        # ── thereafter: the two are READ BACK, and the snapshot's own integrity is re-checked ──
        by_name = {c["check"]: c for c in prior["checks"]}
        for name in ("1 - byte identity to the artifact being replaced",
                     "2 - the artifact snapshotted is the COMMITTED one"):
            frozen = dict(by_name[name])
            frozen["re_verified"] = False
            checks.append(frozen)
            if frozen["verdict"] != "PASS":
                rc = 1
        recorded = by_name["1 - byte identity to the artifact being replaced"]["sha256_snapshot"]
        intact = recorded == snap_hash
        checks.append({
            "check": "1b - the snapshot is UNCHANGED since the record was made",
            "when": "re-verified on every run - this is what `--check` actually tests",
            "why": (
                "Checks 1 and 2 are statements about the moment before the apply ran and become "
                "false the instant the apply rewrites the artifact, which is the apply working "
                "rather than the establishment failing. Re-running them would make this guard "
                "fail forever after the act it licensed - the OI-301 / OI-305 shape. What must "
                "still be true is that the SNAPSHOT is the bytes that were established."
            ),
            "sha256_recorded": recorded,
            "sha256_now": snap_hash,
            "verdict": "PASS" if intact else "FAIL",
        })
        if not intact:
            rc = 1

    readable, carried = True, {}
    try:
        art = json.loads(snap_bytes.decode("utf-8"))
        carried = {
            "population": art["population"],
            "totals_class_before": art["totals"]["class_before"],
            "totals_class_after": art["totals"]["class_after"],
            "totals_entries_moved": art["totals"]["entries_moved"],
            "the_phase_1r_re_run_entries_moved":
                art["the_phase_1r_re_run"]["entries_moved_since_phase1q"],
            "the_phase_1r_re_run_write_list_documents_that_did_not_move_in_whole":
                art["the_phase_1r_re_run"]["write_list_documents_that_did_not_move_in_whole"],
            "moved_out": len(art["moved_out"]),
            "moved_in": len(art["moved_in"]),
        }
    except Exception as exc:                                   # noqa: BLE001 - reported, not raised
        readable = False
        carried = {"error": repr(exc)}
    checks.append({
        "check": "3 - the snapshot parses and carries the finding it exists for",
        "when": "re-verified on every run",
        "why": "A byte-identical copy of a corrupt file is still faithful. Faithfulness is not "
               "enough to rely on, so the fields OI-291 and D-432 cite are read out of the "
               "snapshot itself.",
        "parses": readable,
        "the_finding_the_snapshot_carries": carried,
        "verdict": "PASS" if readable else "FAIL",
    })
    if not readable:
        rc = 1

    return {
        "purpose": (
            "Establishment record for the phase-1q snapshot taken before "
            "`gen_home_classification.py`'s apply mode was run. Ruling R2, user, 2026-08-04, "
            "dispatch `cc_instruction_phase1_delegations_and_corrections.md`."
        ),
        "generated_by": "tools/audit/decisions/gen_phase1q_snapshot_establishment.py",
        "the_pattern": (
            "O-12, the outgoing-reference snapshot gate block (A) uses for a re-baseline: "
            "snapshot the outgoing reference FIRST, and establish it before anything relies on "
            "it (#19). Applied here to a record rather than to a measurement."
        ),
        "what_is_snapshotted": REL_ARTIFACT,
        "why": (
            "OI-305 states in its own words that regenerating this artifact would 'overwrite the "
            "record of what phase 1q found - the OI-301 hazard'. OI-291 and D-432 both cite that "
            "record. The apply mode rewrites it from today's inputs, so the outgoing record is "
            "preserved before the run rather than after it."
        ),
        "how_this_record_ages": (
            "Checks 1 and 2 are FROZEN at the moment they were made and are read back on every "
            "later run, never recomputed; check 1b re-verifies that the snapshot's own bytes are "
            "still the established ones, and check 3 that it still reads. That is what keeps a "
            "guard over a historical record from contradicting the record - the failure mode "
            "OI-301 and OI-305 both describe."
        ),
        "checks": checks,
        "verdict": "ESTABLISHED" if rc == 0 else "NOT ESTABLISHED - THE APPLY MUST NOT RUN",
    }, rc


def main(argv: list[str]) -> int:
    art, rc = build()
    text = json.dumps(art, indent=2, ensure_ascii=False) + "\n"
    if "--check" in argv:
        have = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
        if have != text:
            print("STALE vs the files: the phase-1q snapshot establishment does not re-derive")
            return 1
        print("the phase-1q snapshot establishment re-derives from the files")
        return rc
    open(OUT, "w", encoding="utf-8", newline="").write(text)
    print(f"wrote {os.path.relpath(OUT, ROOT)}")
    for c in art["checks"]:
        print(f"  {c['verdict']}  {c['check']}")
    print(f"  VERDICT: {art['verdict']}")
    return rc


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
