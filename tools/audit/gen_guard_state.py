#!/usr/bin/env python3
"""RUN EVERY GUARD AND RECORD WHAT EACH ONE SAID.

WHY THIS EXISTS.  Two failures in the record, one after the other.  A dispatch named a guard that
had been deleted two waves earlier and nobody noticed (phase 1r).  A guard nobody had been running
was found reporting STALE at the committed tree, and the reason it surfaced then rather than
earlier is that it "is not in the guard list any recent wave reported running"
(`OPEN_ITEMS.md` OI-305).  Both are the same defect: the guard list lived in prose, one wave at a
time, and prose does not notice an addition or a deletion.

HOW THE LIST IS DERIVED, AND WHERE IT IS AUTHORED.  Neither half alone is safe, so both are here
and they check each other:

  derived : every `*.py` under `tools/audit/` whose source carries a `--check`, `--verify` or
            `--establish` mode.  This is the CANDIDATE POPULATION, recomputed on every run.
  authored: the invocation for each guard -- which flags to run it with, and, for a tool that
            cannot be run without writing, the reason it is not run.  A flag is a judgment
            (`--establish` re-measures where `--establish --check` only verifies), so it is
            authored rather than guessed.

  THE TWO STOPS THAT MAKE THAT SAFE:
    * a DERIVED candidate with no authored invocation is UNCLASSIFIED -- a new guard cannot be
      silently left unrun;
    * an AUTHORED entry naming a file that does not exist is a STOP -- a deleted guard cannot be
      silently carried, which is the phase-1r failure exactly.

  Guards outside `tools/audit/` are authored by name (the open-items living check, the
  notation-seams anchor check); the existence STOP covers them the same way.

WHAT IT DOES NOT DO.  It runs guards and records their exit codes and their complete output.  It
makes no judgment about whether a failure is expected, pre-existing, or new -- that is a reading
of the findings, and it belongs in the report and the rows, not in a tool.

Run:
    python tools/audit/gen_guard_state.py           # run every guard, write the artifact
    python tools/audit/gen_guard_state.py --check   # run every guard, exit 1 on any drift
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(HERE, "guard_state.json")

sys.path.insert(0, HERE)
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

MODE_TOKEN = re.compile(r"--(check|verify|establish)\b")

# The tool that records the guard state is not a subject of it: running this file from inside
# itself would recurse.
SELF = "tools/audit/gen_guard_state.py"


class Stop(Exception):
    """An authored entry names something the tree does not have. Never a warning."""


# ── authored: how each guard is invoked, and why any is not run ──────────────────────────────
# `args` None means the tool is NOT RUN; `why` then says why, and it is a reason about the tool,
# never about the result.
AUTHORED = [
    # tools/audit — the record's own checks
    ("tools/audit/register_lint.py", [], "the open-items row-ID uniqueness lint"),
    ("tools/audit/local_patches_check.py", [],
     "the three recorded local patches are still present at HEAD"),
    ("tools/audit/local_patches_check.py", ["--establish", "--check"],
     "that same check's own establishment, verified rather than re-measured"),
    ("tools/audit/guard_armed_check.py", [],
     "the shell-read guard is declared as a PreToolUse hook"),
    ("tools/audit/process_check.py", ["--establish", "--check"],
     "the process check's measured detection and false-positive rates re-derive"),
    ("tools/audit/shell_read_guard.py", ["--establish", "--check"],
     "the shell guard's measured deny and false-deny rates re-derive"),
    ("tools/audit/output_encoding.py", ["--establish", "--check"],
     "the output-encoding fix's own establishment re-derives"),
    ("tools/audit/changed_paths.py", ["--establish"],
     "the changed-path enumeration tool, measured against a known set; it has no verify-only "
     "mode, and writes its establishment artifact on every run"),
    ("tools/audit/claude_md_rule_triage.py", ["--check"],
     "every CLAUDE.md rule carries an authored mechanisation triage"),
    ("tools/audit/corpus_arm_stamp.py", ["--check"],
     "every corpus directory the block-(A) hard stop reads carries an established inference "
     "arm, and it is the joint arm the baselines were measured on"),
    ("tools/audit/corpus_arm_stamp.py", ["--establish", "--check"],
     "the corpus arm stamp's own establishment re-derives -- a wrong-arm corpus is detected, a "
     "right-arm one is not refused, and nothing that used to be refused now passes"),
    ("tools/audit/instrument_arm_declaration_effect.py", ["--check"],
     "the block-(A) instrument's arm declaration still moves no measured value -- it re-runs "
     "that block's own two commands over the production corpus and re-diffs against the "
     "committed reference. The slowest guard here by a wide margin, and authored with --check "
     "rather than dropped because the claim it carries is about a PINNED instrument: a value "
     "moving without anyone noticing is exactly what the block's provenance now says cannot "
     "happen. With no corpus on disk it reports CORPUS-ABSENT and passes"),
    ("tools/audit/gen_phase3_gate_partition.py", ["--check"],
     "the registered phase-3 gate partition re-derives"),
    ("tools/audit/gen_nongating_apparatus_rows.py", ["--check"],
     "the non-gating apparatus-row declaration re-derives from the INDEX"),
    ("tools/audit/gen_ratification_surface_set.py", None,
     "NOT RUN: it has no verify-only mode, so running it OVERWRITES a committed artifact. Its "
     "census counts files in the tree, so any wave that adds a file changes it by construction "
     "-- running it here would silently fold this session's new files into the previous wave's "
     "uncommitted record. That is the OPEN_ITEMS.md OI-301 hazard, and the missing --check is "
     "the defect to fix, not the run to force."),
    ("tools/audit/reaim_ratification_surface_paths.py", None,
     "NOT RUN: an applier, not a guard -- it re-aims citations and reports what it changed. Its "
     "--dry-run classifies but returns no pass/fail verdict about the tree."),

    # tools/audit/decisions — the decisions register's own checks
    ("tools/audit/decisions/gen_decisions_register.py", ["--check"],
     "the rendered register matches its source data across every emitted file"),
    ("tools/audit/decisions/gen_cluster_dispositions.py", ["--verify"],
     "every register entry's verbatim quote and cited line is found at its home"),
    ("tools/audit/decisions/gen_cluster_dispositions.py", ["--check"],
     "the cluster dispositions re-derive"),
    ("tools/audit/decisions/gen_home_classification.py", ["--check"],
     "every home-section field re-derives from the documents' own headings"),
    ("tools/audit/decisions/gen_phase1p_delegation_bar.py", ["--check"],
     "the delegation-bar pre-apply record re-derives"),
    ("tools/audit/decisions/gen_phase1n_reading_regime.py", ["--check"],
     "the reading regime re-derives"),
    ("tools/audit/decisions/gen_phase1m_measurements.py", ["--check"],
     "the phase-1m measurements re-derive"),
    ("tools/audit/decisions/gen_phase1g_triage.py", ["--check"],
     "the phase-1g triage re-derives"),
    ("tools/audit/decisions/gen_decision_clusters.py", ["--check"],
     "the decision clusters re-derive"),
    ("tools/audit/decisions/gen_phase1w_legacy_verification.py", ["--check"],
     "the legacy-mark verification re-derives, and its declared premises still hold"),
    ("tools/audit/decisions/gen_reads1_yield.py", ["--check"],
     "READ WAVE 1's measured yield still matches the bands registered before the reads, and "
     "every entry it names is still in the register at the home it records"),
    ("tools/audit/decisions/reaim_home_anchors.py", ["--check"],
     "no register home anchor has drifted"),
    ("tools/audit/decisions/gen_live_prohibition_pointers.py", ["--check"],
     "every entry the phase-1w verification puts in the live-prohibition class carries its "
     "pointer to the specification section that restates it as binding"),

    # guards that live outside tools/audit
    ("tools/open_items_split_check.py", [],
     "the open-items index/detail bijection, and the original items still byte-verbatim"),
    ("tools/notation_seams/gen_callpath_facts.py", ["--check"],
     "the notation-seam call-path anchors are still where the artifact says"),
]


def candidates() -> list[str]:
    """Every *.py under tools/audit/ that carries a --check / --verify / --establish mode."""
    found = []
    for dirpath, _dirs, files in os.walk(HERE):
        for fn in sorted(files):
            if not fn.endswith(".py"):
                continue
            path = os.path.join(dirpath, fn)
            rel = os.path.relpath(path, ROOT).replace("\\", "/")
            if rel == SELF:
                continue
            with open(path, encoding="utf-8", errors="replace") as fh:
                if MODE_TOKEN.search(fh.read()):
                    found.append(rel)
    return sorted(found)


# A guard that stamps the current HEAD into its own output makes this artifact unreproducible BY
# CONSTRUCTION: committing it changes HEAD, so the next --check reports drift that is not drift.
# Caught by running --check at the tree this artifact was committed to, on the first commit that
# carried it (`gen_callpath_facts.py`, which prints "verified at HEAD <sha>"). The sha is
# normalized in the CAPTURED output only — narrowly, by pattern, so nothing else is touched, and
# the reported pass/fail is untouched either way.
HEAD_SHA = re.compile(r"\bHEAD [0-9a-f]{7,40}\b")


def run_one(rel: str, args: list[str]) -> dict:
    proc = subprocess.run(
        [sys.executable, os.path.join(ROOT, rel), *args],
        capture_output=True, cwd=ROOT,
    )
    out = HEAD_SHA.sub("HEAD <sha>", proc.stdout.decode("utf-8", errors="replace"))
    err = HEAD_SHA.sub("HEAD <sha>", proc.stderr.decode("utf-8", errors="replace"))
    return {
        "tool": rel,
        "args": args,
        "exit_code": proc.returncode,
        "verdict": "PASS" if proc.returncode == 0 else "FAIL",
        "stdout": out.splitlines(),
        "stderr": err.splitlines(),
    }


def main(argv: list[str]) -> int:
    derived = candidates()
    authored_paths = {rel for rel, _a, _w in AUTHORED}

    missing = sorted(p for p in authored_paths if not os.path.exists(os.path.join(ROOT, p)))
    if missing:
        raise Stop(f"authored entry names a file the tree does not have: {missing}")

    unclassified = sorted(p for p in derived if p not in authored_paths)

    runs, not_run = [], []
    for rel, args, why in AUTHORED:
        if args is None:
            not_run.append({"tool": rel, "why": why})
            continue
        rec = run_one(rel, args)
        rec["what_it_checks"] = why
        runs.append(rec)

    failing = [r for r in runs if r["verdict"] == "FAIL"]

    artifact = {
        "purpose": "Every guard in the record, run and recorded: which passed, which failed, and "
                   "for each failure the complete output it produced. The list is derived and "
                   "authored against each other so neither an addition nor a deletion is silent.",
        "generated_by": SELF,
        "generated_for": "cc_instruction_phase1x_guard_visibility_and_commit.md, Task 2",
        "one_normalization_and_why": "A commit sha in a guard's own output is replaced by "
                                     "'HEAD <sha>' in the captured text. Without it this artifact "
                                     "is unreproducible by construction — committing it changes "
                                     "HEAD, so the next --check reports drift that is not drift. "
                                     "Narrow and by pattern; no verdict is affected.",
        "why_this_run_can_be_trusted_where_earlier_ones_could_not":
            "Every guard here routes its printing through tools/audit/output_encoding.py, so a "
            "findings list can no longer be truncated by a character the console cannot encode. "
            "Before that fix, a check could exit non-zero having printed a clean-looking summary "
            "and none of what it found -- which is how OPEN_ITEMS.md OI-305 went unreported.",
        "the_population": {
            "derived": derived,
            "derived_rule": "every *.py under tools/audit/ carrying a --check, --verify or "
                            "--establish mode",
            "authored_entries": len(AUTHORED),
            "unclassified_candidates": unclassified,
            "unclassified_means": "a derived candidate with no authored invocation. NON-EMPTY IS "
                                  "A STOP: a guard exists that this run did not cover.",
            "outside_tools_audit_authored_by_name": sorted(
                p for p in authored_paths if not p.startswith("tools/audit/")),
        },
        "not_run": not_run,
        "runs": runs,
        "summary": {
            "run": len(runs),
            "passing": len(runs) - len(failing),
            "failing": len(failing),
            "failing_tools": [{"tool": r["tool"], "args": r["args"]} for r in failing],
            "not_run": len(not_run),
        },
    }

    text = json.dumps(artifact, indent=2, ensure_ascii=False) + "\n"

    if "--check" in argv:
        have = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
        if have != text:
            print("STALE vs the run: guard_state.json does not re-derive")
            drift = 1
        else:
            print("the guard state re-derives")
            drift = 0
    else:
        open(OUT, "w", encoding="utf-8", newline="").write(text)
        print(f"wrote {os.path.relpath(OUT, ROOT)}")
        drift = 0

    for r in runs:
        print(f"  [{r['verdict']}] {r['tool']} {' '.join(r['args'])}")
    for n in not_run:
        print(f"  [NOT RUN] {n['tool']}")
    if unclassified:
        print(f"STOP: derived candidate(s) with no authored invocation: {unclassified}")
        return 1
    print(f"{len(runs)} guard(s) run, {len(failing)} failing, {len(not_run)} not run")
    return drift


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except Stop as exc:
        print(f"STOP: {exc}")
        sys.exit(2)
