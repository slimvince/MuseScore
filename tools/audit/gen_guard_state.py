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

# Two files are not subjects of this run, for one reason: each would make it recurse.
#   * this file — running it from inside itself is the obvious case;
#   * the classification (added 2026-08-04, READ WAVE 6) — it READS the artifact this file WRITES,
#     so running it here would classify the previous run's state, and capturing its output would
#     change the artifact it just read, and so on without a fixed point. It is run separately,
#     after this one, which is also the order its own STOP requires: it refuses to re-derive while
#     its verdicts and this file's HISTORICAL table disagree.
SELF = "tools/audit/gen_guard_state.py"
NOT_A_SUBJECT = {SELF, "tools/audit/gen_guard_classification.py"}


class Stop(Exception):
    """An authored entry names something the tree does not have. Never a warning."""


# ── authored: how each guard is invoked, and why any is not run ──────────────────────────────
# `args` None means the tool is NOT RUN; `why` then says why, and it is a reason about the tool,
# never about the result.
AUTHORED = [
    # tools/audit — the record's own checks
    ("tools/audit/register_lint.py", [], "the open-items row-ID uniqueness lint"),
    ("tools/audit/index_status_lint.py", ["--check"],
     "every open-items status cell opens with one canonical token, and every row splits — the "
     "standing half of the user's Ruling 33 of 2026-08-09, whose enforcement half is in the ONE "
     "index parser itself and whose vocabulary this tool owns (#6)"),
    ("tools/audit/gen_arm_comment_sweep.py", ["--check"],
     "Ruling 16's enumerated family re-derives — every `src/` comment block claiming an arm, a "
     "flag default or a build state, graded against the two configuration facts the tool re-reads "
     "at the code on every run. Its two STOPs are what make it a guard rather than a record: a "
     "candidate block with NO authored verdict halts it, so a sibling added by a later commit "
     "cannot enter the population unclassified; and a verdict for a block the scan no longer finds "
     "halts it too, so a verdict cannot outlive the comment it grades"),
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
    ("tools/audit/gen_phase1_completion_inventory.py", ["--check"],
     "the phase-1 completion inventory re-derives -- D-231's clause still locatable by its "
     "anchors, and every home class, defense gap, open-row cut and gate verdict unchanged"),
    ("tools/audit/gen_phase1_finish_line.py", ["--check"],
     "the phase-1 FINISH LINE re-derives -- the scope ruling R2 of 2026-08-04 fixed. Its three "
     "STOPs ride with it and are the reason it is a guard rather than a report: an item carrying "
     "no closing act stops it, a row named as a user ruling that is no longer in the derived "
     "gating set stops it, and -- the one that matters -- a population NO ITEM CARRIES stops it, "
     "so the list cannot quietly stop being exhaustive as the register and the open-items index "
     "move under it"),
    ("tools/audit/decisions/gen_outstanding_delegations.py", ["--check"],
     "the outstanding-delegation population still derives at HEAD from the delegation grades and "
     "the home data (D-640/OI-335). Its own STOPs ride with it: a write-list member with no "
     "authored state label, a label for a non-member, and a class-C document with no authored "
     "draft each stop it, so the derived view cannot drift away from the write list in either "
     "direction"),
    ("tools/audit/decisions/gen_true_half_reach.py", ["--check"],
     "ruling R1's application re-derives -- the ruling still locatable in CLAUDE.md by its anchor, "
     "OI-332 still carrying the three documents graded, and every verdict still naming one of the "
     "ruling's own worked examples (D-639)"),
    ("tools/audit/decisions/gen_true_half_reach_rows.py", ["--check"],
     "D-639's SECOND application re-derives -- the same ruling, over the open apparatus-classed "
     "rows the finish line names. Its guard value is in its four STOPs rather than in the artifact: "
     "the authored verdicts and the population derived from the completion inventory must agree in "
     "BOTH directions, so a row entering or leaving that population halts it rather than being "
     "graded silently or quietly dropped; every verdict must name a worked example the ruling "
     "states; every verdict must agree with the thing that decides it, the worked example's own "
     "sign or the row's fallback ground; and every row's quoted words must still be in that row's "
     "own detail file"),
    ("tools/audit/gen_gating_row_sizing.py", ["--check"],
     "the per-row sizing over the gating set re-derives. What it guards is not the sizes, which are "
     "authored judgments, but the pass's own completeness: the authored sizings and the population "
     "derived from the completion inventory must agree in BOTH directions, so a row entering or "
     "leaving the gating set halts it rather than being sized silently or quietly dropped -- which "
     "is the silent cap three continuations declined to risk. Its other STOPs ride with it: every "
     "label, owner and blocker must come from the closed vocabulary the pass declares, a "
     "NEEDS-RULING label and a whose-act field must agree, and every row's quoted words must still "
     "be in the INDEX"),
    ("tools/audit/gen_filing_convention_application.py", ["--check"],
     "the filing convention's candidate set re-derives. What it guards is not the verdicts, which "
     "are authored judgments about documents, but three demands on the record as it stands: every "
     "derived candidate carries an authored verdict, so an unclassified candidate halts the run "
     "rather than passing silently; no verdict names a document the derivation no longer carries, "
     "so the tree moving under the table halts it too; and the derivation's SOUNDNESS against its "
     "seeds is re-computed on every run and published, so a signature that stops finding what the "
     "record already holds is reported rather than quietly trusted"),
    ("tools/audit/decisions/gen_phase1q_snapshot_establishment.py", ["--check"],
     "the phase-1q snapshot's establishment record re-verifies. Its two moment-in-time checks "
     "are FROZEN and read back -- they are statements about the tree before the apply ran, and "
     "re-running them would make this guard fail forever after the act it licensed, which is the "
     "OI-301/OI-305 shape. What it re-verifies is that the snapshot's own bytes still hash to the "
     "established value and that it still parses and carries the fields OI-291 and D-432 cite "
     "(#19)"),
    ("tools/audit/gen_ratification_surface_set.py", None,
     "NOT RUN: it has no verify-only mode, so running it OVERWRITES a committed artifact. Its "
     "census counts files in the tree, so any wave that adds a file changes it by construction "
     "-- running it here would silently fold this session's new files into the previous wave's "
     "uncommitted record. That is the OPEN_ITEMS.md OI-301 hazard, and the missing --check is "
     "the defect to fix, not the run to force."),
    ("tools/audit/reaim_ratification_surface_paths.py", None,
     "NOT RUN: an applier, not a guard -- it re-aims citations and reports what it changed. Its "
     "--dry-run classifies but returns no pass/fail verdict about the tree."),
    ("tools/audit/decisions/gen_verbatim_subject_consistency.py", None,
     "NOT RUN: an ADVISORY REPORT that has no verify-only mode and is not a guard. It reaches "
     "this derived population only because its own prose names the mode it does not have. Built "
     "2026-08-09 on the user's Ruling 24(b), CORPUS FIRST, and adopted as a guard ONLY on measured "
     "clean separation -- which its own artifact MEASURES, and the measurement is negative: "
     "legitimate entries sit at or below the worst labelled known-bad value, so any threshold "
     "would deny legitimate work, which is D-436's third condition and D-473's ground. It is "
     "therefore carried here as not-run WITH that reason, rather than added to the run and "
     "silently reporting nothing. Adding it to the run is a decision that follows a measurement "
     "showing separation, not a session's."),

    # tools/audit/decisions — the decisions register's own checks
    ("tools/audit/decisions/gen_decisions_register.py", ["--check"],
     "the rendered register matches its source data across every emitted file"),
    ("tools/audit/decisions/gen_cluster_dispositions.py", ["--verify"],
     "every register entry's verbatim quote and cited line is found at its home"),
    ("tools/audit/decisions/gen_cluster_dispositions.py", ["--check"],
     "the committed cluster-disposition artifacts cover every cluster exactly once -- a re-READ of "
     "what was emitted, which is all this mode has ever proved"),
    ("tools/audit/decisions/gen_cluster_dispositions.py", ["--producible"],
     "the disposition layer can still be PRODUCED at all -- every register pattern compiles and "
     "the whole derivation runs to completion in memory, writing nothing. Authored 2026-08-07 on "
     "the user's ruling (OI-333): --check re-reads the emitted artifacts while the write path "
     "re-derives them, so no failure of the derivation could ever make --check fail, and six "
     "uncompilable patterns went unreported at every tree while it passed"),
    ("tools/audit/decisions/gen_home_classification.py", ["--check"],
     "every home-section field re-derives from the documents' own headings"),
    ("tools/audit/decisions/gen_phase1p_delegation_bar.py", ["--check"],
     "the delegation-bar pre-apply record re-derives"),
    ("tools/audit/decisions/gen_phase1n_reading_regime.py", ["--check"],
     "the reading regime re-derives"),
    ("tools/audit/decisions/gen_reads5_repack.py", ["--check"],
     "the re-packed reading schedule and its re-registered bands re-derive from the "
     "REGISTERED regime, which it reads and never regenerates"),
    ("tools/audit/decisions/gen_reads5_yield.py", ["--check"],
     "read wave 5's yield re-derives against the bands re-registered before it read"),
    ("tools/audit/decisions/gen_reads6_yield.py", ["--check"],
     "read wave 6's yield — the LAST owed wave — re-derives against the bands re-registered "
     "before it read, every entry it names is still in the register at the home it records, and "
     "the owed remainder it reports still derives from the regime's partition plus waves 1-5"),
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
    ("tools/audit/decisions/gen_reads2_yield.py", ["--check"],
     "READ WAVE 2's measured yield still matches the bands registered before the reads, every "
     "entry it names is still in the register at the home it records, and its running read "
     "count still derives from the regime's own partition plus wave 1's count"),
    ("tools/audit/decisions/gen_reads3_yield.py", ["--check"],
     "READ WAVE 3's measured yield still matches the bands registered before the reads, every "
     "entry it names is still in the register at the home it records, and its running read "
     "count still derives from the regime's own partition plus waves 1 and 2"),
    ("tools/audit/decisions/gen_reads4_yield.py", ["--check"],
     "READ WAVE 4's measured yield still matches the bands registered before the reads, every "
     "entry it names is still in the register at the home it records, and its running read "
     "count still derives from the regime's own partition plus waves 1, 2 and 3"),
    ("tools/audit/decisions/gen_finish_line_item1_routes.py", ["--check"],
     "every entry of finish-line item 1 still carries an authored closing route, no route names "
     "an entry the item no longer carries other than the ones this wave re-homed, and the route "
     "population still re-derives from the finish line rather than from a stored list"),
    ("tools/audit/decisions/gen_item1_rehome_blocker.py", ["--check"],
     "what actually blocks finish-line item 1's re-home class still re-derives — the standing "
     "autonomous-operation authorization still locatable in CLAUDE.md by its anchor, every open "
     "re-home row's owning specification still naming at least one file, and every row's blocker "
     "still cut from that row's own recorded reason rather than from a stored verdict"),
    ("tools/audit/decisions/gen_r1_superseded_reach.py", ["--check"],
     "ruling R1's application re-derives — every member of item 1's NO-HOME class still carries an "
     "authored successor record, no successor record names an entry the class no longer carries, "
     "every authored successor is still NAMED IN THE SUPERSEDED ENTRY'S OWN TEXT, and every one "
     "that resolves to a register identifier still resolves to an entry the register holds"),
    ("tools/audit/decisions/gen_reads4_oi326_application.py", ["--check"],
     "the OI-326 ruling's R5 measurement still re-derives — the doc-governance clause's own "
     "delegating sentence is still locatable and still says what the measurement parsed, the "
     "glob still matches the same files on disk, and no home document's grade has moved onto "
     "that clause since the ruling was applied"),
    ("tools/audit/decisions/reaim_home_anchors.py", ["--check"],
     "no register home anchor has drifted"),
    ("tools/audit/decisions/gen_live_prohibition_pointers.py", ["--check"],
     "every entry the phase-1w verification puts in the live-prohibition class carries its "
     "pointer to the specification section that restates it as binding"),

    ("tools/audit/gen_reserved_word_scanner.py", None,
     "NOT RUN, and the reason is about the tool rather than about its result: it is the ADVISORY "
     "reserved-word inventory the user's Ruling 31 of 2026-08-09 licensed, and its STOP — a derived "
     "candidate with no authored verdict — is its HEADLINE rather than a failure, so it exits "
     "nonzero by design until the per-word verdicts are authored. A guard set carrying a member "
     "that fails by design teaches a reader to ignore the set. Its STOP is reported in its own "
     "artifact `tools/audit/reserved_word_scanner.json` and on OPEN_ITEMS.md OI-229; it is not "
     "adopted as a diff-time check, because Ruling 31 permits that only on measured clean "
     "separation and the measurement is negative"),

    # guards that live outside tools/audit
    ("tools/open_items_split_check.py", [],
     "the open-items index/detail bijection, and the original items still byte-verbatim"),
    ("tools/notation_seams/gen_callpath_facts.py", ["--check"],
     "the notation-seam call-path anchors are still where the artifact says"),
]


# ── THE R4 CLASSIFICATION — tools whose artifact RECORDS A POINT-IN-TIME MEASUREMENT ─────────
#
# THE RULING (user, 2026-08-04, READ WAVE 6, dispatch `cc_instruction_reads_6.md` §0a ruling R4;
# `OPEN_ITEMS.md` OI-330): **a tool that RE-DERIVES A LIVE INVARIANT belongs in the guard list; a
# tool that RECORDS A MEASUREMENT TAKEN AT A POINT IN TIME does not.**  Checked PER TOOL before any
# tool moved — a supposed historical recorder that turns out to assert a live invariant STAYS.
#
# WHY THIS IS NOT A WAY OF HIDING FAILURES.  A tool here is not repaired, not deleted, and not
# excused: its artifact stays on disk exactly as the wave that produced it wrote it, and this table
# records why re-deriving it is the wrong act rather than a pending one.  The distinction the ruling
# draws is between a check that CAN pass forever while the tree moves on, and one that must
# eventually fail BECAUSE the tree moved on — the second measures the clock, not the repository.
#
# WHY THE VERDICTS ARE NOT AUTHORED HERE.  They are authored ONCE, with their per-tool evidence, in
# `tools/audit/gen_guard_classification.py`, which imports this table and STOPS if the two disagree
# in either direction (#6).  What lives here is the INVOCATION consequence — that the tool is not
# run — because this file owns the invocation table.
HISTORICAL: dict[str, str] = {
    "tools/audit/decisions/gen_phase1n_reading_regime.py":
        "HISTORICAL RECORD: the reading regime is a REGISTRATION — an ordering, a predicted band "
        "per owed document and a wave schedule, all recorded BEFORE the reads they govern (#17b). "
        "Its --check cannot pass again and passing would be the defect: OI-328 measured that "
        "re-deriving it flips the ordering key outright, because one of the four candidate proxies "
        "counts how often a document is named in a user-ratified surface and the register's own "
        "homing work increments that count for documents whose yield is already known (#20). The "
        "generator itself now STOPS with that reason rather than re-deriving. NO LIVE COVERAGE IS "
        "LOST: the packing RULE it owns is imported and exercised live by gen_reads5_repack.py, "
        "whose --check passes. (The second half of this reason formerly added 'and each wave's "
        "yield artifact re-derives against the registered bands read off this one'. That was "
        "already false at HEAD when the six yield artifacts were re-classified on 2026-08-04 — "
        "three of them did not re-derive — and it is false by construction now that all six are "
        "historical records themselves. Struck rather than rewritten around: a reason string that "
        "names a check nothing performs is the same defect this table exists to prevent.)",
    "tools/audit/decisions/gen_phase1m_measurements.py":
        "HISTORICAL RECORD: the phase-1m measurements, whose own dispatch ordered two MEASUREMENTS "
        "and forbade acting on either. Its authored KIND table is a judgment made over the home "
        "population AS IT STOOD at phase 1m, and its STOP fires because that population has since "
        "GROWN — so passing it again would mean re-authoring a historical measurement's judgment "
        "table for documents it never measured, which is restating a measurement against a changed "
        "population (the OI-330 shape). NO LIVE COVERAGE IS LOST: its delegation clauses (a)+(b) "
        "are applied live by gen_home_classification.py, which stays in the list.",
    "tools/audit/decisions/gen_phase1g_triage.py":
        "HISTORICAL RECORD: the phase-1g triage table is the decision surface the user ACCEPTED on "
        "2026-08-02 (the 41-document exclusion list), and its counts are cluster attributions that "
        "MOVE WHENEVER A DOCUMENT IS READ — the phase-1h note measured exactly that, one document "
        "moving from 23 clusters to 19 and from rank 5 to rank 11. So its --check cannot pass while "
        "reading continues, and re-deriving it would restate an accepted surface against a "
        "population the acceptance did not cover. NO LIVE COVERAGE IS LOST: it asserts nothing "
        "about the tree beyond those counts — it locates no quote and checks no anchor.",
    "tools/audit/decisions/gen_reads4_oi326_application.py":
        "HISTORICAL RECORD: read wave 4's measurement of the OI-326 ruling, taken BEFORE the ruling "
        "was applied on the user's own condition. OI-330 states both available repairs are "
        "inadmissible — re-pointing the anchor edits a historical measurement's tool, re-deriving "
        "restates that measurement against the population the delegation writes changed. Its "
        "failure is not a live invariant firing: the anchor became ambiguous because the USER WROTE "
        "A CORRECT DELEGATION. NO LIVE COVERAGE IS LOST: the live half it also touches — that each "
        "delegation citation still resolves in its surface — is asserted by "
        "gen_phase1p_delegation_bar.py, which locates every FORMS anchor and stops on a moved or "
        "ambiguous one, and which passes.",

    # ── THE READ-WAVE YIELD FAMILY — six tools, re-classified together 2026-08-04 ──────────────
    # Dispatch `cc_instruction_finish_line_item1b.md`, ruling R2. The earlier classification put
    # this family on the LIVE side, crediting each with the assertion that every entry its wave
    # names is still in the register AT THE HOME IT RECORDS. That is not a live invariant: phase
    # 1's criterion C1 OBLIGES entries to be written into their owning specification, so the check
    # must eventually fail because the tree moved on correctly — the ruling's own definition of a
    # check that measures the clock. Measured, not argued: the previous wave re-homed ten entries
    # and six of the family's members name them. The per-tool evidence is in the classification.
    "tools/audit/decisions/gen_reads1_yield.py":
        "HISTORICAL RECORD: read wave 1's measured yield, graded against bands registered BEFORE "
        "the reads (#17b) — a completed instalment of an out-of-sample test, not a statement about "
        "today. It fails at HEAD on the narrower of the family's two causes: both entries it names "
        "are still homed in ARCHITECTURE.md and only the LINE RANGE moved, drifted by the "
        "insertions the previous wave's homing act made above them. NO LIVE COVERAGE IS LOST: that "
        "every entry still exists with a resolving reference and a verbatim quote at its home is "
        "asserted by gen_decisions_register.py --check and register_lint.py, and that no register "
        "home anchor has drifted by reaim_home_anchors.py --check — all three live and passing.",
    "tools/audit/decisions/gen_reads2_yield.py":
        "HISTORICAL RECORD: read wave 2's measured yield, the same construction as wave 1's. It "
        "PASSES at the committed tree, and that is a fact about which entries the previous wave's "
        "ten re-homings touched rather than a difference in kind — so it is retired with its "
        "siblings instead of being left to fail at the next homing wave. NO LIVE COVERAGE IS LOST, "
        "on the same three live guards named at wave 1's entry.",
    "tools/audit/decisions/gen_reads3_yield.py":
        "HISTORICAL RECORD: read wave 3's measured yield, the same construction and the same "
        "ground as wave 2's. NO LIVE COVERAGE IS LOST, on the same three live guards.",
    "tools/audit/decisions/gen_reads4_yield.py":
        "HISTORICAL RECORD: read wave 4's measured yield, the same construction and the same "
        "ground as wave 2's. NO LIVE COVERAGE IS LOST, on the same three live guards.",
    "tools/audit/decisions/gen_reads5_yield.py":
        "HISTORICAL RECORD: read wave 5's measured yield — one of the two members where the "
        "mechanism is visible rather than argued: SIX of the ten entries the previous wave re-homed "
        "into ARCHITECTURE.md are named by this wave, so the home strings frozen in its artifact no "
        "longer match the register. The check fails because the homing act phase 1 requires was "
        "performed, and re-deriving it would restate a historical measurement against the "
        "population that act changed — the OI-330 refusal. NO LIVE COVERAGE IS LOST, on the same "
        "three live guards named at wave 1's entry.",
    "tools/audit/decisions/gen_reads6_yield.py":
        "HISTORICAL RECORD: read wave 6's measured yield — the other visible member, FOUR of the "
        "previous wave's ten re-homed entries being named here. Its further assertion, that the "
        "owed remainder derives from the regime's partition plus every completed wave's own count, "
        "does not keep it live: every input to that derivation is frozen (a registration recorded "
        "before the reads, and each wave's authored read list), so it re-computes a closed sum and "
        "cannot detect a change in the tree. NO LIVE COVERAGE IS LOST, on the same three live "
        "guards named at wave 1's entry.",
}


def candidates() -> list[str]:
    """Every *.py under tools/audit/ that carries a --check / --verify / --establish mode."""
    found = []
    for dirpath, _dirs, files in os.walk(HERE):
        for fn in sorted(files):
            if not fn.endswith(".py"):
                continue
            path = os.path.join(dirpath, fn)
            rel = os.path.relpath(path, ROOT).replace("\\", "/")
            if rel in NOT_A_SUBJECT:
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

    stray = sorted(p for p in HISTORICAL if p not in authored_paths)
    if stray:
        raise Stop(f"HISTORICAL names a tool with no authored invocation: {stray}")

    runs, not_run, historical = [], [], []
    for rel, args, why in AUTHORED:
        if rel in HISTORICAL:
            historical.append({"tool": rel, "retired_invocation": args,
                               "why": HISTORICAL[rel], "what_it_checked": why})
            continue
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
            "not_a_subject_of_this_run": sorted(NOT_A_SUBJECT),
            "not_a_subject_why": "Each would make this run recurse: this file cannot run itself, "
                                 "and the classification READS the artifact this file WRITES, so "
                                 "running it here would classify the previous run and then change "
                                 "the artifact it just read, without a fixed point. The "
                                 "classification is run separately, AFTER this one — the order its "
                                 "own STOP requires anyway.",
            "outside_tools_audit_authored_by_name": sorted(
                p for p in authored_paths if not p.startswith("tools/audit/")),
        },
        "not_run": not_run,
        "historical_records": {
            "ruling": "User, 2026-08-04 (READ WAVE 6, dispatch `cc_instruction_reads_6.md` §0a "
                      "ruling R4): a tool that RE-DERIVES A LIVE INVARIANT belongs in the guard "
                      "list; a tool that RECORDS A MEASUREMENT TAKEN AT A POINT IN TIME does not. "
                      "Checked PER TOOL before any tool moved — a supposed historical recorder "
                      "that turns out to assert a live invariant STAYS.",
            "what_leaving_the_list_means_and_does_not_mean":
                "The artifact is PRESERVED exactly as the wave that produced it wrote it, and is "
                "marked historical. The tool is not repaired, not deleted and not excused; it is "
                "simply no longer asked to re-derive, because re-deriving it would destroy the "
                "measurement it records. Nothing here fixes OPEN_ITEMS.md OI-309 or OI-330 — those "
                "rows stay open on their own subjects.",
            "the_per_tool_evidence_lives_at":
                "tools/audit/guard_classification.json (gen_guard_classification.py), which "
                "authors the verdict and its evidence for EVERY tool in this list and STOPS if its "
                "verdict set and the table here disagree in either direction (#6).",
            "tools": historical,
        },
        "runs": runs,
        "summary": {
            "run": len(runs),
            "passing": len(runs) - len(failing),
            "failing": len(failing),
            "failing_tools": [{"tool": r["tool"], "args": r["args"]} for r in failing],
            "not_run": len(not_run),
            "historical_records": len(historical),
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
    for h in historical:
        print(f"  [HISTORICAL] {h['tool']}")
    if unclassified:
        print(f"STOP: derived candidate(s) with no authored invocation: {unclassified}")
        return 1
    print(f"{len(runs)} guard(s) run, {len(failing)} failing, {len(not_run)} not run, "
          f"{len(historical)} historical record(s)")
    return drift


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except Stop as exc:
        print(f"STOP: {exc}")
        sys.exit(2)
