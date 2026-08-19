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
    ("tools/audit/gen_discard_records.py", ["--check"],
     "the DISCARD records the gating derivation consumes re-derive AT THE RECORD -- the user's "
     "Ruling 69 of 2026-08-13 (D-677) makes an authored discard verdict an input to a derived "
     "gate, so this is the guard that keeps the authored half honest. Its STOPs are what make it "
     "one rather than a report: a record whose quoted element is no longer in its surface, a "
     "record naming a row the INDEX does not carry open, a record naming a row the #19 carve-out "
     "keeps gating, a discard on the register's own two surfaces that the table does not enter, "
     "and a NOT-DISCARDED negative seed being read as a discard -- each halts it rather than "
     "letting an authored judgment move a gate on text nobody re-read"),
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
    # ---- AUTHORED 2026-08-15, cc_instruction_period_checks.md Task 3 -------------------------
    # Both tools are added by this dispatch's own Tasks 1 and 2, so each is registered in the act
    # that creates it rather than reaching a later pass's derived population unclassified — which
    # is the condition `OPEN_ITEMS.md` OI-373 already carries for two other tools.
    ("tools/audit/gen_period_stratum_split.py", ["--check"],
     "the ruled period's split re-derives from the two candidate artifacts, and the screen "
     "population still follows from them. Its five STOPs are what make it a guard rather than a "
     "record: the ruled start commit must be in the commits table, every hunk record must carry "
     "every field the derivation needs and is never skipped, every commit and file index must "
     "resolve, the position cut and the stratum cut must agree away from the boundary commit, and "
     "the derived flagged totals must reconcile with the input artifact's own published totals — "
     "so an input edited by hand halts it instead of moving the split silently"),
    ("tools/audit/gen_july_screen.py", ["--check"],
     "the July screen re-derives — its population still imported whole from the split artifact and "
     "reconciled with the authored verdicts in BOTH directions, and every screened hunk's text "
     "still retrievable at its recorded coordinates from the git object by explicit hash, with the "
     "retrieved line counts cross-checked against the population's own record. What it guards is "
     "not the verdicts, which are authored judgments about documentation changes, but that no hunk "
     "enters or leaves the screened population ungraded and that no coordinate stops identifying "
     "the change it was read at"),
    # ---- AUTHORED 2026-08-15, cc_instruction_artifact_inventory.md ---------------------------
    # Registered in the act that creates it, for the reason stated three entries above.
    ("tools/audit/gen_artifact_inventory.py", ["--check"],
     "the artifact inventory re-derives at the commit its own artifact RECORDS -- so it passes "
     "indefinitely rather than going red at the next commit -- and, separately, its signature "
     "table still covers the tree AS IT STANDS with nothing unclassified. The second half is the "
     "live one and the reason this is a guard at all: a file added by a later commit in a "
     "top-level directory no rule names halts this tool instead of reaching a later pass ungraded. "
     "Its last rule is bounded on purpose so that STOP can fire, and the artifact carries the "
     "probes that establish it does (#19). The untracked appendix is a reading of the working "
     "tree and is excluded from the byte comparison, so writing a scratch file does not turn this "
     "guard red"),
    ("tools/audit/gen_artifact_inventory_surface.py", ["--check"],
     "the artifact inventory's ruling surface re-derives from the inventory artifact. Its four "
     "STOPs are what make it a guard: a class in the inventory with no authored proposal halts it, "
     "so a class cannot be ruled on by omission; a proposal naming a class the inventory does not "
     "carry halts it, so the two files cannot drift apart in either direction; a role or mining "
     "verdict outside the closed vocabulary the direction names halts it; and a proposal with no "
     "reason halts it. What it does NOT guard is the verdicts themselves, which are authored "
     "judgments awaiting the user"),

    # ---- AUTHORED 2026-08-15, cc_instruction_ruled_inventory_landing.md Task 2 ---------------
    # THE TWO TOOLS THIS RUN'S OWN STOP HAS BEEN NAMING. Each joined the derived candidate
    # population in the act that created it, carrying a `--check` mode, and neither invocation was
    # authored with it — which is the condition `OPEN_ITEMS.md` OI-373 records and the reason this
    # runner could not exit on its guards' verdicts alone. Authored on the user's ruling of
    # 2026-08-15 (`cowork_rulings_2026_08_15_inventory_sitting.md` §5, the extension riding with
    # the third red's clearing), each after reading its tool IN FULL, and each classified in the
    # same act at `gen_guard_classification.py` — which STOPs if the two tables disagree (#6).
    # BOTH TAKE `--check` AND NOT THE BARE INVOCATION, for a reason about the tools: run with no
    # flag each REWRITES its committed artifact, so a bare run would fold whatever the tree
    # currently says into the record of a completed act, which is the OI-301 hazard exactly.
    ("tools/audit/gen_status_archive_pass.py", ["--check"],
     "the 2026-08-11 STATUS.md archive pass still reconciles in both directions -- the moved block "
     "still verbatim in STATUS_ARCHIVE.md at HEAD and still absent from STATUS.md at HEAD, with "
     "the one claim about a single moment checked at that moment's own git object by explicit hash "
     "so it cannot decay as the live file legitimately grows. What it guards is that nothing left "
     "the must-read which is not in the archive and that nothing else left it (#12); it says "
     "nothing about whether STATUS.md is readable again, which is OI-370's own subject"),
    ("tools/audit/gen_doc_change_candidates.py", ["--check"],
     "the candidate pass -- every documentation change of the restructuring period, enumerated and "
     "classified per hunk -- still re-derives byte-identically FROM THE GIT OBJECTS, with the "
     "range's END read back from the committed artifact rather than taken as HEAD so a later "
     "commit does not turn it red. Its STOPs are what make it a guard rather than a record: a hunk "
     "carrying no verdict, a PURE verdict citing no clause, a boundary commit that is not an "
     "ancestor of the range end, and two reconciliations that must balance -- so the enumeration "
     "cannot quietly stop being one"),
    # Task 3's own tool, registered in the act that creates it -- the practice the two entries above
    # exist because two earlier acts did not follow.
    ("tools/audit/gen_test_construction_evidence.py", ["--check"],
     "the class-1 construction-evidence check re-derives. Its evidence is read at the commit the "
     "committed artifact inventory RECORDS, so it passes indefinitely rather than going red the "
     "first time anybody edits a test; what is LIVE is the two-way reconciliation of its graded "
     "set against that inventory's own class membership, so a member entering or leaving the class "
     "halts it instead of being graded silently or quietly dropped. Its other STOPs ride with it: "
     "a member with no verdict, a verdict outside the closed two-value vocabulary the user's "
     "ruling fixes, a SPEC-DERIVED-EVIDENCE verdict resting on no located statement, and a "
     "distribution that does not reconcile with the population"),

    # ---- AUTHORED 2026-08-15, cc_instruction_preparation_opening.md Task 2 -------------------
    # Added by this dispatch's own Task 2 and registered in the act that creates it, rather than
    # reaching a later pass's derived population unclassified — the condition `OPEN_ITEMS.md`
    # OI-373 recorded for two other tools, made a standing rule by this dispatch. It takes
    # `--check` and not the bare invocation, for a reason about the tool: run with no flag it
    # REWRITES its committed outputs, so a bare run would fold whatever the tree currently says
    # into the record of a completed act, which is the OI-301 hazard exactly.
    ("tools/audit/gen_decisions_filter.py", ["--check"],
     "the decisions-register filter re-derives — every entry of the register's data file walked, "
     "its deciding-act evidence quoted from its own recorded text, and one proposed class per "
     "entry. What it guards is not the proposals, which are a reading awaiting the user, but "
     "three demands on the record as it stands: the population and the rendered INDEX must carry "
     "the same entries in BOTH directions, so a derivation over a derived population cannot be "
     "published in part (D-671); every entry must carry the fields the classification reads, so "
     "one it cannot classify at all halts it rather than being skipped; and the distribution must "
     "account for the population exactly. Its other STOPs ride with it — a duplicate entry "
     "identity, and a status outside the vocabulary the data file's own header declares"),
    # ---- AUTHORED 2026-08-15, cc_instruction_preparation_opening.md Task 3 -------------------
    # Task 3's own tool, on the same practice as the entry above.
    ("tools/audit/gen_retirement_caller_check.py", ["--check"],
     "the caller-check over every ruled retirement candidacy re-derives — SINCE 2026-08-16 under "
     "the ruled reading of `cowork_rulings_2026_08_16_preparation_return.md` §1, so what it "
     "re-derives now includes the DERIVED caller-kind classification: which callers are tree "
     "enumerations whose namings hold nothing, and which are not. Its reference readings "
     "are taken at the commit its own artifact RECORDS, so it passes indefinitely rather than "
     "going red the first time anybody writes a file naming a flagged one — the OI-301/OI-305 "
     "shape avoided by construction. What is LIVE is the population: the flags are re-imported "
     "from the ruling surface's generator on every run and the citation split is re-scanned at "
     "the governing record, so a candidacy entering or leaving the ruled set, or a member "
     "changing side, halts it instead of being graded silently. Its STOPs ride with it: a flagged "
     "class the inventory does not carry, a mixed class the inventory publishes no members for, a "
     "member list whose derived count disagrees with the count the inventory publishes, an "
     "authored condition and a derived candidacy disagreeing in either direction, a condition "
     "whose quoted sentence is no longer in the ruling record, A SENTENCE OF THE RULED READING NO "
     "LONGER IN ITS OWN RULING RECORD — so a reading cannot outlive the words that imposed it, the "
     "same shape the conditions already carry — a caller kind outside the closed four-value "
     "vocabulary, a kind tally that does not account for the callers found, a verdict outside the "
     "closed three-value vocabulary, and a tally that does not account for the candidacies"),

    # ---- AUTHORED 2026-08-16, cc_instruction_preparation_second.md Task 2 -------------------
    # Added by this dispatch's own Task 2 and registered in the act that creates it, rather than
    # reaching a later pass's derived population unclassified — the standing new-tool rule. It
    # takes `--check` and not the bare invocation, for a reason about the tool: run with no flag it
    # REWRITES its committed outputs, so a bare run would fold whatever the record currently says
    # into a completed pass, which is the OI-301 hazard exactly.
    ("tools/audit/gen_deciding_act_recovery.py", ["--check"],
     "the deciding-act recovery pass re-derives — for every entry the decisions-register filter "
     "could not name a deciding act for, the entry's OWN cited sources followed through the record "
     "and searched for a user act naming that entry's subject. What it guards is not the results, "
     "which are evidence awaiting the user, but four demands on the record as it stands: the "
     "non-keep population imported from the committed filter artifact and the register's data file "
     "must carry the same entries in BOTH directions, so a derivation over a derived population "
     "cannot be published in part (D-671); every entry must carry the fields the pass reads, so one "
     "it cannot read halts it rather than being skipped; every result must be one of the closed "
     "three values and the distribution must account for the population; and every sentence of the "
     "ruling that ordered the pass must still be in its ruling record, so the pass cannot outlive "
     "the words that ordered it"),

    # ---- AUTHORED 2026-08-16, cc_instruction_preparation_second.md Task 3 -------------------
    # Task 3's own tool, registered in the act that creates it, on the same practice and for the
    # same reason as the entry above: run with no flag it REWRITES its committed outputs.
    ("tools/audit/gen_rulings_sort.py", ["--check"],
     "the rulings sort re-derives — every entry on the confirmed side of the decisions-register "
     "filter carrying one PROPOSED class, design intent or management of the implementation, or "
     "NEEDS-THE-USER where the rule reaches no verdict. What it guards is not the proposals, which "
     "await the user, but five demands on the record as it stands: the confirmed population "
     "imported from the committed filter artifact and the decisions register's data file must "
     "carry the same entries in BOTH directions; every entry must carry the fields the rule reads; "
     "a `nonspec_kind` value the pass neither maps nor deliberately leaves to the recognizers halts "
     "it, so a new value cannot be classified by silence; every definition the mapping quotes must "
     "still be in the data file's own header, so the mapping cannot rest on words the record has "
     "dropped; and every class must be one of the ruled three with a distribution that accounts "
     "for the population"),

    # ---- AUTHORED 2026-08-16, cc_instruction_preparation_third.md Task 1 --------------------
    # Added by this dispatch's own Task 1 and registered in the act that creates it, rather than
    # reaching a later pass's derived population unclassified — the standing new-tool rule. It
    # takes `--check` and not the bare invocation, for a reason about the tool: run with no flag it
    # REWRITES its committed artifact, and that artifact is the GUARD the ruled soft-discard runs
    # behind, so a bare run would fold whatever the record currently says into the record of which
    # entries the guard withheld — the OI-301 hazard at its most damaging.
    ("tools/audit/gen_sole_carrier_subclass.py", ["--check"],
     "the sole-carrier subclass re-derives — the guard the user's Ruling of 2026-08-16 §3(A) put "
     "in front of the soft-discard, derived over the whole non-keep population of the decisions "
     "register at the commit the artifact RECORDS. What it guards is not the verdicts, which are "
     "a derivation the user reads, but five demands on the record: the population imported from "
     "the committed filter artifact must reconcile with the committed recovery artifact and with "
     "the decisions register's data file in BOTH directions (D-671); every entry must carry the "
     "fields the pass reads, so one it cannot read halts it rather than being skipped; every "
     "verdict must be one of the closed two values with a distribution that accounts for the "
     "population; every sentence of the ruling that DEFINES the subclass must still be in its "
     "ruling record AS IT STANDS, so the guard cannot outlive the words that imposed it; and each "
     "of the three signals must be shown BOTH to fire and to stay quiet, so a signal that came "
     "back empty over the population cannot be mistaken for one that cannot fire at all (#19)"),

    # ---- AUTHORED 2026-08-16, cc_instruction_preparation_third.md Task 2 --------------------
    # Task 2's own tool, registered in the act that creates it, on the same practice and for the
    # same reason as the entry above: run with no flag it REWRITES its committed outputs.
    ("tools/audit/gen_ratified_document_check.py", ["--check"],
     "the ratified-document subject check re-derives, and with it the residue surface both this "
     "batch's returns are carried on. For the 62 entries the user's Ruling of 2026-08-16 §3(B2) "
     "did NOT rule, each recovered act is established as a document ratification or not, and where "
     "it is, the ratified document is searched for that entry's OWN subject recognizers — the "
     "decisions register's `patterns`, which is what the ruling asks for in its own words. What it "
     "guards is not the results, which are evidence awaiting the user, but six demands on the "
     "record: the population must be derivable at all, which means the ten (B1) keeps must still "
     "be PARSED from the ruling record's own bullet — a bullet naming any number other than ten, "
     "or naming an entry the recovery pass did not return ACT-FOUND for, halts it rather than "
     "being corrected; every entry must carry the fields the pass reads; every result must be one "
     "of the closed three values with a distribution that accounts for the population; every "
     "sentence of the ruling that ordered the derivation must still be in its ruling record AS IT "
     "STANDS; and every recorded act coordinate is re-read at the measured commit and "
     "cross-checked against the quote the recovery pass published, so a document that has moved "
     "under a line cannot be graded silently as though it had not"),

    # ---- AUTHORED 2026-08-16, cc_instruction_preparation_third.md Task 3 --------------------
    # Task 3's own tool, registered in the act that creates it. THE ACT IT PERFORMS WAS NOT
    # PERFORMED: it was planned, applied to the working tree, measured against the whole guard set,
    # and REVERTED, because the dispatch's assumption A3 was falsified by that run. What is
    # committed is the PLAN and the tool, and this invocation checks the plan rather than an act.
    # It takes `--check` and never the bare invocation for the ordinary reason — the bare
    # invocation rewrites the committed plan — and never `--apply`, which is the act itself.
    ("tools/audit/decisions/apply_soft_discard.py", ["--check"],
     "the ruled soft-discard's PLAN re-derives, and no retirement has been applied. Before the act "
     "this is what is live: every sentence of the ruling that ordered the discard must still be in "
     "its ruling record; the population must still be DERIVABLE from the committed recovery and "
     "sole-carrier artifacts — the entries the recovery pass returned NOTHING-FOUND for minus the "
     "members the guard withheld, with a member that is BOTH halting it and a member the decisions "
     "register's data file does not carry live halting it too (D-671); and the committed plan must "
     "still re-derive from those inputs. AFTER the act, the plan cannot be re-derived by "
     "construction, and what this checks instead is the applied state: live plus retired accounting "
     "for the whole former population BY ARITHMETIC, no entry in both blocks and none in neither, "
     "and every retired record carrying its finding, its date, its retiring authority and the ruled "
     "clause verbatim — the four the ruling requires of every record"),

    # ---- AUTHORED 2026-08-17, cc_instruction_preparation_eighth.md Task 2 -------------------
    # THE RESIDUE SITTING'S DISCARDS, CARRIES AND KEEPS, registered in the act that creates the
    # tool — the standing new-tool rule. Both take `--check` and never the bare invocation, for the
    # ordinary reason: run with no flag each REWRITES its committed artifact; and the first never
    # takes `--apply`, which is the act itself.
    ("tools/audit/decisions/apply_residue_discard.py", ["--check"],
     "the residue sitting's applied state re-checks: the two retirements accounting for the whole "
     "former population BY ARITHMETIC, no entry in both blocks and none in neither, every record "
     "THIS act retired carrying its finding, its date, its retiring authority, the ruling that "
     "retired it and the ruled clause verbatim, and every one of the fifty-three ruled KEEPS still "
     "carrying the deciding act recorded for it — re-quoted on every run from the artifact it was "
     "taken from, so a stamp removed or rewritten fails on the day it happens. THE SITTING'S OWN "
     "ARITHMETIC IS RE-RECONCILED against the record as it stands, and the ruling makes that a "
     "STOP rather than an adjustment in its own words. Every population is DERIVED on every run "
     "and never listed: the 29 from the sole-carrier guard crossed with the recovery pass, the 9, "
     "the 47 and the 6 from the ratified-document check's own per-entry result, and the one "
     "candidate carried from the nine as the sole-carrier member among them — any other number "
     "halting it"),
    ("tools/audit/gen_framework_untrusted_candidates.py", ["--check"],
     "the framework phase's untrusted-candidate carry still re-derives — the 29 the sole-carrier "
     "guard withheld plus the one member carried from the nine, each with the title, restatement, "
     "recorded home and status the decisions register gives it, read from that register whether "
     "the entry is live or retired. A hand edit to the published list fails on the next run, which "
     "is what makes the carry a derivation rather than a transcription. ★ WHAT IT DOES NOT ASSERT: "
     "that any member is a decision, is authority, or is sound — the retirement that produced the "
     "list is a PROVENANCE verdict, which the artifact states of itself"),

    # ---- AUTHORED 2026-08-16, cc_instruction_preparation_fourth.md Task 1 -------------------
    # Both tools are added by this dispatch's own Task 1 and registered in the act that creates
    # them, rather than reaching a later pass's derived population unclassified — the standing
    # new-tool rule. Each takes `--check` and never the bare invocation, for a reason about the
    # tools: run with no flag each REWRITES its committed artifact, and both artifacts are read
    # BEFORE an irreversible act rather than after it, which is the OI-301 hazard at its sharpest.
    ("tools/audit/gen_phase1_gate_readers.py", ["--check"],
     "the R1 reader enumeration re-derives — every tracked file naming any of the old phase-1 gate "
     "artifacts or their derivation family's outputs, classified the superseded program's own "
     "apparatus, a historical record, or a LIVE consumer. What it guards is not the verdicts, "
     "which carry their ground and their quoted naming line beside them, but four demands on the "
     "record as it stands: every sentence of the ruling that ordered the enumeration must still be "
     "in its ruling record, so the pass cannot outlive the words that ordered it; every generator "
     "the ruling names must still exist AND must still name its own output artifact, so a "
     "generator that has gone halts it instead of shrinking the population silently; every naming "
     "must be placeable; and a NON-EMPTY live-consumer class halts it, which is the ruling's own "
     "instruction. Its readings are taken from the git objects at the commit its artifact RECORDS, "
     "so writing a file that names one of these artifacts does not turn it red — the OI-301 / "
     "OI-305 shape avoided by construction"),
    ("tools/audit/gen_discard_reach_split.py", ["--check"],
     "the R2 derived split re-derives — every check the ruled soft-discard's application turns "
     "red, classified SUPERSEDED (serves only the old phase-1 gate) or STANDING (serves a rule of "
     "the current record), each with its imports, its own stated purpose, and the derived "
     "explanation of its red. What it guards is not the verdicts but five demands: the ruling's "
     "sentences must still be in its ruling record; the population must still be IMPORTABLE from "
     "the `[FAIL]` block of the committed report that measured it, and a block that is missing, "
     "empty, or names a check the tree no longer carries halts it rather than letting the "
     "population shrink to what still parses; every member must be placeable by the verdict rule; "
     "a STANDING member whose red the enumerated-movement bound cannot explain halts it, which is "
     "the ruling's own STOP; and the tally must account for the population"),

    # ---- AUTHORED 2026-08-16, cc_instruction_preparation_fifth.md Task 1 --------------------
    # The tool is added by that task and registered in the act that creates it — the standing
    # new-tool rule. It takes `--check` and never the bare invocation, for the ordinary reason:
    # run with no flag it REWRITES its committed artifact.
    ("tools/audit/decisions/gen_retired_subject_moves.py", ["--check"],
     "the ruled kind-2 move list re-derives, and every one of the five authored judgment tables "
     "agrees with it in BOTH directions. What it guards is which AUTHORED judgment watches a live "
     "subject and which has followed its subject into the decisions register's retired-entries "
     "block: a judgment in both sections halts it; a judgment whose subject the discard retired "
     "and which is still in a live table halts it; a retired judgment whose subject is LIVE again "
     "halts it, so a judgment cannot be resurrected without being re-read; a live judgment whose "
     "subject is neither live nor retired by this act halts it, because its membership cannot be "
     "derived and the ruling's instruction is a STOP to the user rather than a guess; a retired "
     "section-kind judgment carrying no subject reference halts it; and every sentence of the "
     "ruling that ordered the treatment must still be in its ruling record. The section-grain "
     "derivation is IMPORTED from the home classifier that owns it rather than restated (#6), so "
     "the move list and that tool's own STOP cannot disagree about which judgments move"),

    ("tools/audit/gen_census_movement_classification.py", ["--check"],
     "every value the ruled soft-discard moved in the two derived censuses re-derives, and every "
     "one of them is inside the ruled bound. The comparison is the CITATION SCAN itself, re-run "
     "over the governing record at both states — the earlier one from the git objects at the "
     "commit before the act — rather than two rendered surfaces being diffed, and the scan and the "
     "governing-record definition are IMPORTED from the census that owns them (#6). Its STOPs are "
     "the ruling's own: a moved value none of the three categories reaches halts it, because the "
     "ruling's instruction on any other movement is a STOP-and-report and this tool may not widen "
     "the bound on its own authority; a name ENTERING the citation scan halts it, since the "
     "discard only ever removes an entry's text from the rendered register; and a census whose "
     "scan cannot be read at either state halts it. What it does NOT assert is that a moved "
     "document is worth retiring: a crossing confers CANDIDACY only, and every ruled condition on "
     "a candidacy stands untouched"),

    # ---- AUTHORED 2026-08-16, cc_instruction_preparation_fifth.md Task 2 --------------------
    # The ruled READ-ONLY pruning measurement's two tools, registered in the act that creates them.
    # Each takes `--check` and never the bare invocation: run with no flag each REWRITES its
    # committed artifact, and the second rewrites a ruling surface awaiting the user as well.
    ("tools/audit/gen_governing_surface_spans.py", ["--check"],
     "the five mandatory-read files still decompose span by span into the same classes with the "
     "same byte counts. What it guards is the DECOMPOSITION rather than the classes' verdicts, "
     "which are recognizers over prose and say so of themselves: a file the ruling names that the "
     "tree no longer carries halts it, and — the one that matters — the per-class byte counts must "
     "account for the file EXACTLY, so a span cannot be silently dropped from the decomposition, "
     "which is the single failure that would make every number in it meaningless. That STOP fired "
     "for real on the tool's first run. The row split and the resolved-mark test are IMPORTED from "
     "the one index lint that owns them (#6)"),
    ("tools/audit/gen_governing_surface_readers.py", ["--check"],
     "who reads, anchors into, quotes or parses each of the five mandatory-read files still "
     "re-derives at the tree, and the ruling surface generated from it and from the span "
     "decomposition still re-derives with it. It is the F13 lesson applied prospectively: a "
     "mutation's reach is MEASURED before the act, so the anchored namings, the tools that read "
     "each file by path and the register entries homed in it are all published before any span "
     "moves. Its STOPs: a named file the tree does not carry halts it; a span decomposition that "
     "is missing or covers a different file set halts it, because the surface is generated from "
     "BOTH artifacts and may not be built from half of them; and a per-file naming tally that "
     "stops accounting for the scan halts it. What it does NOT assert is that a naming is a "
     "dependency — the scan sees tracked files only and a computed path carries no literal to "
     "find, which it publishes of itself"),

    # ---- AUTHORED 2026-08-17, cc_instruction_preparation_sixth.md Task 1 --------------------
    # THE PERMANENT RECONCILIATION CHECK ON THE RULED GOVERNING-SURFACE SPLIT, registered in the
    # act that creates it — the standing new-tool rule. Clause 7 of the dispatch orders ONE CHECK
    # PER PARENT/COMPANION PAIR; there are five pairs and one concern (reconcile a parent against
    # its companion), so the check has ONE home (#6) and is INVOKED once per pair, which is the
    # shape `local_patches_check.py` and `corpus_arm_stamp.py` already use here. It takes `--check`
    # and never the bare invocation, for the ordinary reason: run with no flag it REWRITES its
    # committed artifact.
    *[("tools/audit/gen_governing_surface_split.py", ["--check", "--pair", pair],
       f"the ruled split of `{pair}` against its archive companion still reconciles in BOTH "
       f"directions: every archived span byte-present in the companion exactly once, every "
       f"archived span absent from the parent, and moved + kept accounting for the parent's "
       f"pre-act committed blob TO THE CHARACTER. The pre-act blob and the register's home anchors "
       f"are read from the GIT OBJECTS at the commit the act was performed on top of, so the claim "
       f"re-derives forever rather than decaying as the parent legitimately grows (D-646, the "
       f"epoch pattern). Its STOPs are what make it a guard rather than a record: an archive-class "
       f"span with no authored reading verdict halts it, so a span cannot be archived unread "
       f"(Ruling 1's own safeguard); a verdict naming a span the pinned decomposition does not "
       f"carry halts it, so the two cannot drift apart; a moved span whose text is not present "
       f"exactly once in the pre-act blob halts it; the arithmetic not accounting for that blob to "
       f"the character halts it; and a register HOME anchor falling inside a moved span halts it, "
       f"which is clause 4's own condition that no operative span may have moved")
      for pair in ("CLAUDE.md", "OPEN_ITEMS.md", "DECISIONS.md", "STATUS.md",
                   "BUILD_AND_TEST.md")],

    # ---- AUTHORED 2026-08-17, cc_instruction_preparation_sixth.md Task 2 --------------------
    # Ruling 4's FORWARD BOUND, applied for the first time at this batch's close and registered in
    # the act that creates it — the standing new-tool rule. It takes `--check` and never the bare
    # invocation, for the ordinary reason: run with no flag it REWRITES its committed artifact.
    ("tools/audit/gen_status_batch_bound.py", ["--check"],
     "the then-previous batch's `STATUS.md` entries are still byte-present in `STATUS_ARCHIVE.md` "
     "exactly once and still absent from the must-read — Ruling 4's forward bound, proven in both "
     "directions rather than asserted. The moved set is read from the git OBJECT at the commit the "
     "move was performed on top of, so the claim re-derives forever as later batches legitimately "
     "append their own entries (D-646, the epoch pattern). Its STOPs are what make it a guard "
     "rather than a record: a dispatch naming NO entry at that commit halts it, because moving "
     "nothing silently would leave the bound unmet without saying so; an entry not present exactly "
     "once in the live file when the move is applied halts it; and an entry already in the archive "
     "halts it. Membership is DERIVED from the entries' own words — the one naming the dispatch, "
     "plus the run below it saying `Same dispatch` — so no entry is listed by hand, and the dated "
     "entry pattern is IMPORTED from the archive pass that owns it (#6)"),

    # ---- AUTHORED 2026-08-17, cc_instruction_preparation_seventh.md Task 1 ------------------
    # THE PRE-CONVENTION RESIDUE MOVE, registered in the act that creates it — the standing
    # new-tool rule. It takes `--check` and never the bare invocation, for the ordinary reason:
    # run with no flag it REWRITES its committed artifact.
    ("tools/audit/gen_status_residue_move.py", ["--check"],
     "the dated `STATUS.md` entries the executed split left at site — those whose own wording "
     "predates or paraphrases the OI-222 pointer remedy, so the pinned measurement did not place "
     "them — are still byte-present in `STATUS_ARCHIVE.md` exactly once, still absent from the "
     "must-read, and the ONE candidate the reading flagged is still at site. All three directions "
     "are proven rather than asserted, and the third is the one that matters most: a check that "
     "only proved the move would stay green if a later act quietly archived the flagged span too. "
     "The population is DERIVED as the pinned decomposition's own residue — the operative-classed "
     "spans at or after the file's first dated entry — and cross-checked in BOTH directions "
     "against the split-application artifact, so this act and the split account for the file "
     "together. Every entry's text is read from the git OBJECT at the pinned commit, so the claim "
     "re-derives forever as later batches legitimately append their own entries (D-646, the epoch "
     "pattern). Its STOPs are what make it a guard rather than a record: a candidate with no "
     "authored reading verdict halts it, so no entry is moved unread (Ruling 3's own safeguard); "
     "a verdict naming a span the decomposition does not carry halts it; a candidate already in "
     "the split's moved set halts it; the two acts not accounting for every span of the "
     "decomposition halts it; and an entry not present exactly once in the live file when the "
     "move is applied halts it"),

    # ---- AUTHORED 2026-08-17, cc_instruction_preparation_seventh.md Task 2 ------------------
    # THE RE-PINNED CENSUS'S MOVEMENT, registered in the act that creates it — the standing
    # new-tool rule. It takes `--check` and never the bare invocation, for the ordinary reason:
    # run with no flag it REWRITES its committed artifact.
    ("tools/audit/gen_retirement_census_movement.py", ["--check"],
     "every difference between the retirement census's outgoing reading and its re-pinned one "
     "still places in one of the three classes Ruling 2 names — the split's effect, the discard's "
     "residue, and the tree's ordinary growth — at four units of identity, with ZERO fitting none "
     "of them. Its STOP is the guard: a movement the derivation cannot place halts it and prints "
     "the unplaced records WHOLE, so a fourth class or a too-narrow relation is reported rather "
     "than absorbed. Both readings and both trees are read from git OBJECTS at the commits the "
     "readings were MEASURED at — never at the working tree and never at the commit that happens "
     "to carry an artifact — so the comparison re-derives forever (D-646, the epoch pattern). "
     "★ WHAT IT DOES NOT ASSERT, and its own artifact says so: that a class is a movement's "
     "CAUSE. Each class is a derived RELATION between the movement and the two trees, tested in a "
     "fixed order with the first that holds recorded WITH its evidence"),

    # ---- AUTHORED 2026-08-17, cc_instruction_preparation_seventh.md Task 3 ------------------
    # THE FINER `CLAUDE.md` MEASUREMENT AND ITS RULING SURFACE, registered in the act that creates
    # them — the standing new-tool rule. Both take `--check` and never the bare invocation, for
    # the ordinary reason: run with no flag each REWRITES its committed artifact.
    ("tools/audit/gen_claude_md_finer_spans.py", ["--check"],
     "the finer decomposition of `CLAUDE.md` still re-derives at its pinned commit, with every "
     "span classed from its own text, its placing evidence published beside it, and the per-class "
     "byte counts accounting for the file TO THE CHARACTER — the STOP that makes the measurement "
     "worth anything, since a silently dropped span would make every count in it meaningless. "
     "The reading is pinned because the artifact is EVIDENCE FOR A RULING and may not move under "
     "the ruling it supports. ★ WHAT IT DOES NOT ASSERT, and its own artifact says so: that a "
     "span classed `operative-rule-text` IS operative — only that no recognizer placed it "
     "elsewhere; the recognizers are patterns over prose and their reach is UNMEASURED (#19), "
     "with the direction of their error the recoverable one"),
    ("tools/audit/gen_claude_md_finer_surface.py", ["--check"],
     "the refreshed reach for `CLAUDE.md` — who names it, who anchors into it at a LINE, which "
     "tools parse it, which register entries are homed in it — still re-derives at the finer "
     "pass's own commit, and the ruling surface generated from it and the span artifact still "
     "re-derives BYTE-IDENTICALLY. The second half is the load-bearing one: the surface is what "
     "the user rules, so a surface that has drifted from the artifacts it claims to be generated "
     "from would put a hand-edited proposal in front of a ruling. The scan itself is IMPORTED "
     "from `gen_governing_surface_readers.measure` rather than re-implemented (#6). ★ WHAT IT "
     "DOES NOT ASSERT: that a naming is a DEPENDENCY, or that the parser list is complete — a "
     "tool reaches it only when the line naming the file also carries a read signal"),

    # ---- AUTHORED 2026-08-17, cc_instruction_preparation_eighth.md Task 1 -------------------
    # THE TWO RULED `CLAUDE.md` SPANS AND THEIR READING, registered in the act that creates the
    # tool — the standing new-tool rule. It takes `--check` and never the bare invocation, for the
    # ordinary reason: run with no flag it REWRITES its committed artifact.
    ("tools/audit/gen_claude_md_finer_archive.py", ["--check"],
     "where every span of Ruling 1's own population actually stands: the spans the ruling places "
     "in the archive, the spans it REFUSED, and — at this tree, where the read-before-move "
     "safeguard returned STAY on both archive candidates — that every flagged and every refused "
     "span is still byte-present at site exactly once and in the companion not at all. Those last "
     "two directions are the load-bearing ones here, because a check that only proved a move would "
     "be green at a tree where the refusals had been overridden. The population is DERIVED on "
     "every run from the pinned finer decomposition and that artifact's own published conflict "
     "evidence, and the derivation reproducing Ruling 1's stated shape — two archive, four refused "
     "— is a STOP rather than an assumption. ★ WHAT IT DOES NOT ASSERT: that either flagged span "
     "is unarchivable; only what the imported reading test asks of each"),

    # ---- AUTHORED 2026-08-17, cc_instruction_preparation_ninth.md Task 2 --------------------
    # THE POST-SPLIT ARCHIVING PASS, registered in the act that creates the tool — the standing
    # new-tool rule. `--check` and never the bare invocation, for the ordinary reason: run with no
    # flag it REWRITES its committed artifact; run with `--apply` it MOVES text.
    ("tools/audit/gen_post_split_archive.py", ["--check"],
     "where every span of Ruling 2's own population actually stands: the spans the ruled "
     "archivability test PLACES across the five mandatory-read files at this act's pin, the "
     "reading verdict authored for each, and — per file, in both directions — that every moved "
     "span is byte-present in its companion exactly once and absent from its parent, and that "
     "every span the reading LEFT AT SITE is still byte-present at site exactly once and in the "
     "companion not at all. The second direction is the load-bearing one here, because eighteen of "
     "the nineteen proposals stayed: a check that only proved the one move would be green at a tree "
     "where a refusal had been overridden. The population is DERIVED on every run from the imported "
     "span cut and recognizers, with three ruled exclusions each derived rather than listed — a "
     "span a previous act already archived, the six `CLAUDE.md` spans the two return sittings "
     "settled, and a span classified by text inside an archive pointer. A proposed span with no "
     "authored reading verdict, and an authored verdict naming a span the derivation does not "
     "carry, each STOP it. ★ WHAT IT DOES NOT ASSERT: that any span left at site is unarchivable; "
     "only what the imported reading test asks of each"),

    # ---- AUTHORED 2026-08-18, cc_instruction_preparation_tenth.md Task 1 ---------------------
    # THE EVIDENCE PIN'S CLASS MEMBERSHIP, registered in the act that creates the tool — the
    # standing new-tool rule. `--check` and never the bare invocation, for the ordinary reason: run
    # with no flag it REWRITES its committed artifact.
    ("tools/audit/gen_evidence_pin_membership.py", ["--check"],
     "who belongs to the evidence pin's ruled class, derived on every run from the ruling records "
     "themselves rather than listed: every ratification document a tool WRITES, every root-level "
     "ruling record, and what each record says in its own two structural blocks — its leading "
     "blockquote and its provenance paragraph — that it was taken from. Its live half is that the "
     "membership tracks the record: a ruling taken tomorrow from a generated document appears "
     "tomorrow, and a member the record stops naming leaves. Its STOPs are demands about the tree "
     "AS IT STANDS — a member this artifact records as PINNED whose generator no longer carries "
     "that commit in a pin constant, a tool carrying a pin constant the run does not account for "
     "in one of its two classes, and a generated ratification document with two writers (#6). "
     "★ WHAT IT DOES NOT ASSERT: that a member SHOULD be pinned, or that an UNRESOLVED member has "
     "no discoverable commit — only that no record states one in the form the resolution uses, "
     "which is why an unresolved member is published to the user as data and never given a "
     "guessed pin"),

    # ---- AUTHORED 2026-08-18, cc_instruction_preparation_tenth.md Task 2 ---------------------
    # THE SESSION-START READ'S OWN SIZE, registered in the act that creates the tool — the standing
    # new-tool rule. `--check` and never the bare invocation, for the ordinary reason: run with no
    # flag it REWRITES its committed artifact.
    ("tools/audit/gen_session_start_read_size.py", ["--check"],
     "what an ordinary session reads at session start, in characters, measured at the tree and at "
     "the recorded earlier commit's git object. It is the arc's own subject made checkable: the "
     "pruning direction of 2026-08-16 is about this number, and every act in the arc has had to "
     "state what it saved. Its load-bearing STOP is a demand about the tree AS IT STANDS — rule "
     "(a)'s artifact-and-key pointer is PARSED FROM THE CLAUSE ITSELF and must RESOLVE in the "
     "artifact it names, so a pointer that has stopped resolving fails on the day it stops rather "
     "than being hidden inside a number. It goes red when a governing surface changes, which is "
     "the point: the session-start read moved and the record does not yet say so. ★ WHAT IT DOES "
     "NOT ASSERT: that the membership is complete — it is AUTHORED, and each member carries the "
     "clause that makes it one so the authored half is checkable by reading three clauses; and "
     "nothing about whether the read is small enough, which is [[OI-370]]'s own subject"),

    # ---- AUTHORED 2026-08-19, cc_instruction_preparation_twelfth.md Task 3 -------------------
    # THE EPOCH-PINNED PASSES AND WHAT THEIR WRITE PATHS RESOLVE, registered in the act that
    # creates the tool — the standing new-tool rule. `--check` and never the bare invocation, for
    # the ordinary reason: run with no flag it REWRITES its committed artifact.
    ("tools/audit/gen_epoch_write_path.py", ["--check"],
     "which passes are EPOCH-PINNED — their `--check` re-deriving at the commit their own "
     "committed artifact RECORDS rather than at the tree — and, per member, whether the WRITE path "
     "reads that same recorded commit back or carries the literal HEAD instead. The population is "
     "DERIVED on every run from the tools' own syntax trees and never listed, so a pass that gains "
     "or loses the epoch shape moves the artifact on the day it happens. What it guards is not the "
     "verdicts, which are a reading returned to the user, but three demands on the tree AS IT "
     "STANDS: the two establishment seeds — one member per verdict, each established at the code — "
     "must still derive to the side the record establishes for them, so a recognizer that has "
     "stopped recognizing the shape it was built for HALTS rather than publishing a smaller "
     "population; and the members the recognizers CANNOT place must reconcile with the authored "
     "reasons in BOTH directions, so a new unrecognised shape cannot enter silently and an "
     "authored reason cannot outlive its subject. ★ WHAT IT DOES NOT ASSERT: that an ASYMMETRIC "
     "member is broken, that a SYMMETRIC one needs nothing, or that the population is complete — "
     "it is complete relative to recognizers whose reach beyond the two seeds is UNMEASURED and "
     "stated as such. ★ AND IT AUTHORIZES NOTHING: the ruling it exists for says each pass is "
     "corrected only when a ruled act needs its write path"),

    # ---- AUTHORED 2026-08-19, cc_instruction_preparation_thirteenth.md Task 2 ----------------
    # THE RECOGNIZERS THE RECORD LEANS ON, SORTED BY WHETHER AN INDEPENDENTLY-KNOWN POPULATION
    # EXISTS, registered in the act that creates the tool — the standing new-tool rule. `--check`
    # and never the bare invocation, for the ordinary reason: run with no flag it REWRITES its
    # committed artifact.
    ("tools/audit/gen_recognizer_establishment_sort.py", ["--check"],
     "which tools are RECOGNIZERS OVER A POPULATION, and for each whether an INDEPENDENTLY-KNOWN "
     "population exists to reconcile against — the test the user ruled as a class on 2026-08-19. "
     "The population is DERIVED on every run from the tools' own syntax trees and never listed, so "
     "a tool that becomes or stops being a recognizer over a population moves the artifact on the "
     "day it happens. What it guards is not the verdicts, which are a reading returned to the "
     "user, but three demands on the tree AS IT STANDS: the three establishment seeds — one member "
     "per verdict, each read at its own tool and its own artifact — must still derive to the side "
     "the record establishes for them, so a recognizer that has stopped recognizing the shape it "
     "was built for HALTS rather than publishing a smaller population; the members it CANNOT place "
     "must reconcile with the authored reasons in BOTH directions, so a new unrecognised shape "
     "cannot enter silently and an authored reason cannot outlive its subject; and — the one "
     "peculiar to this tool — IT IS A MEMBER OF ITS OWN POPULATION, so the status it declares "
     "about itself must AGREE with the verdict its own test derives for it. All three were shown "
     "both to FIRE and to stay QUIET when it was built (#19). ★ WHAT IT DOES NOT ASSERT: that a "
     "member on the no-external-population side is wrong, that an ESTABLISHED member's individual "
     "verdicts are right, or that the member list is complete — the membership recognizer's reach "
     "beyond the three seeds is UNMEASURED, which is why the artifact publishes a LOWER BOUND and "
     "declares that of itself. ★ AND IT AUTHORIZES NOTHING: the ruling it exists for says in its "
     "own words that the result authorizes NOTHING."),

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
    # ── THE SUPERSEDED PHASE-1 GATE FAMILY ────────────────────────────────────────────────────
    # RECLASSIFIED 2026-08-16 by `cc_instruction_preparation_fifth.md` Task 1, on the user's
    # ruling of 2026-08-16 §4 ("the superseded phase-1 apparatus follows its phase into HISTORICAL
    # status") executed under §6.  On 2026-08-15 the user ruled the SIX-PHASE structure and D-231's
    # three phases were superseded; these six tools exist only to derive the OLD phase 1's gate.
    # The ruled soft-discard then retired every entry homed in `cowork_structural_integrity_audit.md`,
    # so that document stops being class C and the delegation grading they all import REFUSES to
    # run: they do not go stale, they STOP.
    #
    # ★ WHAT HISTORICAL STATUS ASSERTS HERE, IN THE RULING'S OWN TERMS: that these checks graded a
    # SUPERSEDED PROGRAM.  It asserts NOTHING about whether that program's obligations were
    # discharged, and no completion claim of any kind rides it.  Each artifact stays on disk
    # exactly as the wave that produced it wrote it, frozen as record (#12); the pre-discard
    # derivation state stands at the git objects; and reviving a retired entry revives its
    # consumers' inputs with it.
    #
    # ★ THE READER ENUMERATION RAN BEFORE ANYTHING FROZE, and is the reason this is not a guess:
    # every tracked file naming any of the six artifacts was enumerated at the recorded commit and
    # the LIVE-consumer class came back EMPTY (`tools/audit/phase1_gate_readers.json`).  The one
    # downstream consequence is published rather than left to be found (F22): the phase-1 completion
    # inventory feeds `gen_true_half_reach_rows.py`, whose artifact `gen_nongating_apparatus_rows.py`
    # reads to derive D-438's live declaration.  Nothing halts; what stops is future MOVEMENT of
    # that frozen population, and the user ACCEPTED that as a named cost.
    "tools/audit/gen_phase1_completion_inventory.py":
        "HISTORICAL RECORD: what the SUPERSEDED phase 1 of D-231's three-phase structure still "
        "required. The six-phase structure the user ruled on 2026-08-15 replaced that program, and "
        "the ruled soft-discard of 2026-08-16 makes this derivation STOP rather than drift — the "
        "document its delegation grading needs is no longer class C, because every entry homed in "
        "it was retired. Re-deriving it would mean re-authoring drafts for a superseded program, "
        "which is the capacity sink the apparatus-lapse ruling closed. It asserts NOTHING about "
        "whether phase 1's obligations were discharged. NO LIVE COVERAGE IS LOST: no reader of its "
        "artifact outside the superseded program exists, measured at the objects before it froze.",
    "tools/audit/gen_phase1_finish_line.py":
        "HISTORICAL RECORD: the FINISH LINE for the SUPERSEDED phase 1 — what was still required "
        "and what act would close each item. Same ground as the completion inventory it imports, "
        "and it STOPS for the same reason. Its last derivable state stands frozen on disk as the "
        "record of that program; nothing here says the program finished. NO LIVE COVERAGE IS LOST.",
    "tools/audit/decisions/gen_outstanding_delegations.py":
        "HISTORICAL RECORD: the outstanding-delegation population of the SUPERSEDED phase 1, and "
        "the FEEDER whose only importers are the two gate derivations above — which is what places "
        "it here rather than among the standing checks (the derived split, "
        "`tools/audit/discard_reach_split.json`). It is the tool that STOPS first: the authored "
        "draft it needs is for a document the retirement empties. NO LIVE COVERAGE IS LOST — the "
        "home rules it served are asserted live by gen_home_classification.py and "
        "gen_phase1p_delegation_bar.py, both of which stay in the list.",
    "tools/audit/decisions/gen_finish_line_item1_routes.py":
        "HISTORICAL RECORD: the closing ROUTE for every entry of the superseded finish line's item "
        "1 — a view of the same derivation, which it imports transitively. Its subject is a "
        "program that no longer governs, and its inputs STOP. NO LIVE COVERAGE IS LOST.",
    "tools/audit/decisions/gen_item1_rehome_blocker.py":
        "HISTORICAL RECORD: what blocked the superseded finish line's item-1 re-home class. Same "
        "family, same import, same STOP. Its one live-looking assertion — that the standing "
        "autonomous-operation authorization is still locatable in CLAUDE.md by its anchor — is not "
        "lost: CLAUDE.md's own anchors are asserted live by claude_md_rule_triage.py and by the "
        "register's home-anchor checks, all of which stay in the list.",
    "tools/audit/decisions/gen_r1_superseded_reach.py":
        "HISTORICAL RECORD: ruling R1's application to the superseded finish line's item-1 "
        "NO-HOME class. Same family, same import, same STOP. NO LIVE COVERAGE IS LOST: that every "
        "register cross-reference still resolves is asserted live by "
        "gen_cluster_dispositions.py --verify, which stays in the list and which now consults the "
        "retired-entries block beside the live entries.",
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
