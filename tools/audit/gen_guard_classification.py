#!/usr/bin/env python3
"""CLASSIFY EVERY GUARD: does it RE-DERIVE A LIVE INVARIANT, or RECORD A POINT-IN-TIME MEASUREMENT?

THE RULING (user, 2026-08-04, READ WAVE 6, dispatch `cc_instruction_reads_6.md` §0a ruling R4;
`OPEN_ITEMS.md` OI-330).  **A tool that RE-DERIVES A LIVE INVARIANT belongs in the guard list; a
tool that RECORDS A MEASUREMENT TAKEN AT A POINT IN TIME does not.**  The ruling attaches its own
condition: the question is **CHECKED PER TOOL BEFORE ANY TOOL MOVES** — a supposed historical
recorder that turns out to assert a live invariant STAYS, failing if it fails.

WHAT THE DISTINCTION IS FOR, so a later reader does not apply it as a convenience.  A guard list
whose failures are permanent and meaningless teaches a reader to ignore it, and then a real failure
arrives in a list nobody reads.  The operational form of the ruling: can this check pass forever
while the tree moves on correctly, or must it eventually fail BECAUSE the tree moved on?  The second
kind measures the clock, not the repository.

WHAT MOVING DOES NOT MEAN.  A tool classified `records-a-point-in-time-measurement` is not repaired,
not deleted, and not excused.  Its artifact stays on disk exactly as the wave that produced it wrote
it, and is marked historical.  Nothing here discharges `OPEN_ITEMS.md` OI-309 or OI-330.

WHAT IS AUTHORED AND WHAT IS DERIVED.
  authored : VERDICTS — per tool, the classification, the EVIDENCE it was made from (a citation into
             the tool itself), and the reason.  Nothing else.
  derived  : the population, taken from `gen_guard_state.AUTHORED` so the two cannot disagree about
             which tools exist; the current pass/fail verdict of each, read off the committed
             `guard_state.json` rather than re-run here (#6 — one runner); the counts; and the
             cross-check against `gen_guard_state.HISTORICAL`.

THE THREE STOPS.
  * a tool in the guard-state population with NO authored verdict is a STOP — the ruling's own
    per-tool condition, made mechanical;
  * a verdict naming a tool the guard state does not carry is a STOP;
  * a disagreement between this file's `records-a-point-in-time-measurement` set and
    `gen_guard_state.HISTORICAL` is a STOP, in EITHER direction — the verdict and its consequence
    have one home each and neither may drift from the other (#6).

Run:  python tools/audit/gen_guard_classification.py [--check]
"""
from __future__ import annotations

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
STATE = os.path.join(HERE, "guard_state.json")
OUT = os.path.join(HERE, "guard_classification.json")

sys.path.insert(0, HERE)
from output_encoding import use_utf8_output      # noqa: E402  (path set above)
import gen_guard_state as gs                     # noqa: E402  (the population + the consequence)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

LIVE = "re-derives-a-live-invariant"
POINT = "records-a-point-in-time-measurement"
NEITHER = "neither — not a guard"


class Stop(Exception):
    """The ruling's per-tool condition is unmet, or the two homes disagree. Never a warning."""


# ── AUTHORED — the verdict per tool, with the evidence it was made from ──────────────────────
# Every citation below was READ IN THIS SESSION, in the tool it names, with the file tools.
VERDICTS: dict[str, tuple[str, str, str]] = {

    # ---- tools/audit — the record's own checks ----------------------------------------------
    "tools/audit/register_lint.py": (
        LIVE, "register_lint.py:10-13",
        "\"This lint reads OPEN_ITEMS.md, collects the ID of every register ROW … and fails if any "
        "ID appears more than once.\" The subject is the register AS IT STANDS; a collision "
        "introduced tomorrow fails tomorrow, and a clean tree passes indefinitely."),
    "tools/audit/local_patches_check.py": (
        LIVE, "local_patches_check.py:2, :17-22",
        "Its own title is a question about NOW — \"Are the local patches to MuseScore's own code "
        "still present at HEAD?\" — and the patch list is DERIVED from `CLAUDE.md` rather than "
        "frozen, so a fourth recorded patch is covered without editing the tool. The failure it "
        "exists to catch (a dependency update silently reverting one) is a future event."),
    "tools/audit/guard_armed_check.py": (
        LIVE, "guard_armed_check.py:22-25",
        "It reads the settings files a session in this directory WOULD read and reports whether a "
        "PreToolUse hook running the shell-read guard is declared, and whether hooks are globally "
        "off. A property of the current machine state, re-answered on every run."),
    "tools/audit/process_check.py": (
        LIVE, "process_check.py:28",
        "The invocation in the guard list is `--establish --check`, which RE-MEASURES the check's "
        "own detection and false-positive rates against its fixtures and compares them with the "
        "recorded ones. An establishment obligation (#19) re-derived at HEAD, not a dated reading."),
    "tools/audit/shell_read_guard.py": (
        LIVE, "shell_read_guard.py:12-14",
        "Same shape: `--establish --check` re-derives the guard's measured deny and false-deny "
        "rates. The guard itself is a live PreToolUse control, and its establishment is a standing "
        "obligation rather than a wave's finding."),
    "tools/audit/output_encoding.py": (
        LIVE, "output_encoding.py:4-9",
        "`--establish --check` re-runs four probes at HEAD — the crash reproduces without the fix, "
        "the whole output arrives with it, a deliberate non-zero exit still exits non-zero, an "
        "unrelated exception still ends the process. Each is a property of the code as it stands."),
    "tools/audit/changed_paths.py": (
        LIVE, "changed_paths.py:18-30",
        "`--establish` builds a KNOWN SET in a temporary directory on every run and measures the "
        "tool against it, including the two refusals. Nothing about it is dated: it re-measures "
        "the structural property (it cannot return file content) at the code as it stands."),
    "tools/audit/claude_md_rule_triage.py": (
        LIVE, "claude_md_rule_triage.py:15-18",
        "★ CLASSIFIED LIVE DESPITE FAILING, and the failure is the reason it is live: the "
        "population is DERIVED — \"every register entry whose home is `CLAUDE.md`\" — so it grows "
        "as rules are written, and the STOP fires on exactly that (three rules with no authored "
        "triage). The invariant it asserts is about the rule set TODAY: every rule carries a "
        "mechanisation triage. A tool whose population tracks the tree is not a dated reading of "
        "it. It stays, failing."),
    "tools/audit/corpus_arm_stamp.py": (
        LIVE, "corpus_arm_stamp.py:18-28",
        "The arm of a corpus is readable AT THE OBJECT, per file, from a field each `.ours.json` "
        "stamps; `--check` re-reads the corpus directories the block-(A) hard stop consumes. A "
        "regeneration on the wrong arm tomorrow is caught tomorrow."),
    "tools/audit/instrument_arm_declaration_effect.py": (
        LIVE, "instrument_arm_declaration_effect.py:18-22",
        "It RE-RUNS gate block (A)'s own two commands over the production corpus at HEAD and "
        "re-diffs the candidate against the committed reference. The claim — a pinned instrument's "
        "arm declaration cannot move a measured value — is about the instrument as it stands, and "
        "the tool measures rather than recalls it."),
    "tools/audit/gen_phase3_gate_partition.py": (
        LIVE, "gen_phase3_gate_partition.py:4-16",
        "★ A REGISTERED PREDICTION, and still live — the case R4's per-tool condition exists for. "
        "Its artifact carries verdicts fixed before the classified items run, but its --check "
        "LOCATES every source quote IN THE FILE IT CITES and STOPS on one that has drifted, and "
        "its per-item check column is filled in as each item runs. It is a LIVING register with a "
        "frozen prediction inside it, not a dated measurement, and the drift check is a live "
        "invariant nothing else asserts."),
    "tools/audit/gen_nongating_apparatus_rows.py": (
        LIVE, "gen_nongating_apparatus_rows.py:13-21",
        "It PARSES `OPEN_ITEMS.md` on every run for the row population and which rows are open, and "
        "STOPS if any candidate has no authored verdict or any verdict names a row the index no "
        "longer carries open. Both stops are about the register as it stands today."),
    "tools/audit/gen_phase1_completion_inventory.py": (
        LIVE, "gen_phase1_completion_inventory.py:11-26",
        "It RE-DERIVES on every run: D-231's clause is located in `CLAUDE.md` by anchor string and "
        "must still be findable or the tool STOPS; every home class, defense gap and "
        "section-criterion verdict is read off the register as it stands; the open-row population "
        "and each row's gate verdict come from `OPEN_ITEMS.md` and the apparatus declaration as "
        "they stand today, and a verdict naming a row the index no longer carries open is a STOP. "
        "Nothing in it is a measurement taken at a point in time — a later wave that homes an entry "
        "or closes a row SHOULD move its output, and the check is what makes that movement visible."),
    "tools/audit/gen_phase1_finish_line.py": (
        LIVE, "gen_phase1_finish_line.py:18-34",
        "Authored 2026-08-04 in answer to this tool's own per-tool STOP — it entered the guard "
        "population two waves ago and had never been classified. It IMPORTS both populations "
        "rather than storing them, locates D-231's clause by anchor at HEAD, and carries a STOP "
        "that is a live demand in the strongest form the population has: a population that grows "
        "WITHOUT AN ITEM TO CARRY IT stops the tool, which is what makes the list a finish line "
        "rather than a selection. It re-derives as the record moves under it, and it passes."),
    "tools/audit/decisions/gen_finish_line_item1_routes.py": (
        LIVE, "gen_finish_line_item1_routes.py:8-17",
        "Authored 2026-08-04 in answer to the same STOP. Its population is IMPORTED from the "
        "finish-line generator and never re-listed (#6), so it shrinks as entries are homed; and "
        "it REFUSES to run if any entry has no authored route or if a route names an entry the "
        "population no longer carries — in its own words, 'so the register moving under the table "
        "is a STOP rather than a silent partial answer'. That is a demand about today, not a dated "
        "reading: the AUTHORED half is the route per entry, and the tool will not let that half go "
        "stale silently. It passes at the committed tree."),
    "tools/audit/decisions/gen_r1_superseded_reach.py": (
        LIVE, "gen_r1_superseded_reach.py:22-38",
        "Authored 2026-08-04 with the tool, so R4's per-tool condition was a design input. It "
        "IMPORTS its population from the route table rather than storing one, and re-reads the "
        "register on every run for each entry's status and each successor's home CLASS — so the "
        "HOMED verdict and the disposition move the day a successor is homed, which is exactly "
        "the event the ruling makes the owed act. Its sharpest STOP is a live demand on the "
        "record rather than on the tree's history: every AUTHORED successor must still be NAMED "
        "IN THE SUPERSEDED ENTRY'S OWN TEXT, so a session cannot nominate one the register does "
        "not name, and a reworded supersession stops the tool instead of silently keeping a "
        "verdict the record no longer supports. It re-derives and it passes."),
    "tools/audit/decisions/gen_item1_rehome_blocker.py": (
        LIVE, "gen_item1_rehome_blocker.py:32-42",
        "Authored 2026-08-04 with the tool, so R4's per-tool condition was a design input. Every "
        "half of it is a demand about TODAY: the population is IMPORTED from the route table and "
        "shrinks as entries are homed; each row's blocker is re-cut from that row's own recorded "
        "reason on every run, so a reworded reason moves the verdict instead of leaving a stale one "
        "standing; and the STANDING AUTHORIZATION it compares against is located in `CLAUDE.md` BY "
        "ANCHOR and quoted at HEAD, with a STOP if it cannot be found — so a change to what a "
        "session may edit moves this artifact rather than being silently outrun by it. It stores no "
        "dated reading of anything."),
    "tools/audit/decisions/gen_outstanding_delegations.py": (
        LIVE, "gen_outstanding_delegations.py:36-46",
        "It RE-DERIVES the whole partition on every run, from the delegation grades it IMPORTS "
        "(`gen_phase1p_delegation_bar.FORMS`) and the home population it IMPORTS "
        "(`gen_home_classification.home_population`) — never from a stored figure. Three STOPs are "
        "about the record as it stands today: a write-list member with no authored state label, a "
        "label naming a non-member, and a class-C document with no authored draft. A later wave "
        "that writes a delegation or widens one SHOULD move its output, which is the point of it "
        "(D-640 / OI-335)."),
    "tools/audit/decisions/gen_true_half_reach.py": (
        LIVE, "gen_true_half_reach.py:22-30",
        "It LOCATES ruling R1 in `CLAUDE.md` by anchor string on every run and STOPS if it has "
        "moved or been reworded; it re-reads `open_items/OI-332.md` and STOPS if that row no "
        "longer carries a document it grades; and it STOPS on a verdict naming a worked example "
        "the ruling does not state. Whether the ruling's FALLBACK was reached is DERIVED from the "
        "verdicts rather than declared, so the artifact cannot claim a clean application it did "
        "not have."),
    "tools/audit/decisions/gen_true_half_reach_rows.py": (
        LIVE, "gen_true_half_reach_rows.py:30-43",
        "LIVE for the same operational reason as the first application, with one addition that is "
        "the stronger half. It imports the ruling, the three worked examples and the locator from "
        "that application (#6), so it inherits the anchor STOP; every verdict must name a worked "
        "example the ruling states and must AGREE with the thing that decides it — the example's "
        "own sign, or, where no example matched, the one authored ground the fallback turns on — "
        "so a verdict and its reason cannot point different ways. And its POPULATION is read at "
        "the completion inventory on every run and reconciled with the authored verdicts in BOTH "
        "directions: a row entering or leaving the apparatus-classed set halts it rather than "
        "being graded silently or dropped. That is a demand about the record as it stands today, "
        "not a dated reading of it."),
    "tools/audit/gen_gating_row_sizing.py": (
        LIVE, "gen_gating_row_sizing.py:30-44",
        "LIVE, and the verdict is worth stating because the artifact's CONTENT is authored "
        "judgment. What the check asserts is not that the sizes are right — a size cannot be "
        "checked — but three demands about the record as it stands TODAY. Its POPULATION is read "
        "at the completion inventory on every run and reconciled with the authored sizings in "
        "BOTH directions, so a row entering or leaving the gating set halts it rather than being "
        "sized silently or quietly dropped. Every label, owner and blocker must come from the "
        "closed vocabulary the file declares, so a later wave cannot widen the label set by "
        "writing one. And every row's quoted words must still be in the INDEX, so a sizing cannot "
        "outlive the text it was read from. None of that is a dated reading."),
    "tools/audit/decisions/gen_phase1q_snapshot_establishment.py": (
        LIVE, "gen_phase1q_snapshot_establishment.py:24-38",
        "★ THE FIRST TOOL BUILT AFTER R4 AND BUILT TO IT, so the classification was a design "
        "input rather than a later verdict — and it comes out LIVE on the ruling's own "
        "operational form: can this check pass forever while the tree moves on correctly? It can. "
        "Its ARTIFACT contains a point-in-time record (checks 1 and 2 — the snapshot matched the "
        "artifact, and that artifact was the committed one — both statements about the tree "
        "BEFORE the home-classification apply ran, and both false the moment the apply rewrites "
        "the artifact, which is the apply WORKING). Those two are therefore FROZEN and read back, "
        "never recomputed. What the CHECK re-derives is a live invariant nothing else asserts: "
        "that the snapshot still hashes to the established value and still parses and carries the "
        "fields OI-291 and D-432 cite (checks 1b and 3). A snapshot edited, truncated or lost is "
        "caught on the next run, forever. **The distinction the classification turns on is "
        "between an artifact that RECORDS a moment and a check that RE-RUNS one** — and getting "
        "it wrong in the safe-looking direction would have been the OI-301 / OI-305 shape a third "
        "time: a guard over a historical record that contradicts the record it guards."),
    "tools/audit/gen_ratification_surface_set.py": (
        LIVE, "gen_ratification_surface_set.py:13-24",
        "Classified for completeness though it is NOT RUN. Its three readings — the class, the "
        "direct namings, the reached namings — are all derived by SCANNING THE TREE, so it is a "
        "live census. Its defect is the missing verify-only mode, which is why the guard state "
        "carries it as not-run with that reason; the defect is not that it is historical."),
    "tools/audit/reaim_ratification_surface_paths.py": (
        NEITHER, "reaim_ratification_surface_paths.py:25-27",
        "An APPLIER, not a guard: it re-aims citations and reports what it changed, and its "
        "`--dry-run` classifies without returning a pass/fail verdict about the tree. R4's question "
        "does not arise — there is no invariant and no measurement, only an edit."),
    "tools/audit/decisions/gen_verbatim_subject_consistency.py": (
        NEITHER, "gen_verbatim_subject_consistency.py, the 'WHAT IT IS AND IS NOT' paragraph of its "
        "module docstring, and the `adoption_verdict` field of its own artifact",
        "An ADVISORY REPORT, not a guard, and its own artifact is what says so. It compares every "
        "register entry's quoted decision against that entry's own account of which decision it "
        "records — the one comparison that does not depend on a corrupted pair agreeing with "
        "itself — but it returns no pass/fail verdict about the tree and has no verify-only mode. "
        "R4's question is not the one to ask of it: it neither re-derives an invariant nor records "
        "a dated measurement of the tree, it RANKS entries for a reader. It would become live only "
        "on a measurement showing clean separation between its labelled known-bad corpus and the "
        "remainder, and that measurement — taken with the corpus recorded first, per the user's "
        "Ruling 24(b) — is NEGATIVE at this tree. Classified for completeness though it is NOT "
        "RUN, on the same footing as the census above."),

    # ---- AUTHORED 2026-08-09, cc_instruction_return_continuation_6.md Task 0 -----------------
    # Both tools were added by the previous continuation and reached this pass's derived
    # population without a verdict, which is this tool's own STOP working. A verdict is authored
    # for a tool the population DID reach; none is hand-added for one it did not.
    "tools/audit/gen_arm_comment_sweep.py": (
        LIVE, "gen_arm_comment_sweep.py:14-22, :24-31",
        "★ EVERY HALF OF IT IS A DEMAND ABOUT TODAY, which is what separates a live invariant from "
        "a dated reading. The two CONFIGURATION FACTS it grades against are RE-READ AT THE CODE on "
        "every run, located by anchor string rather than by line number — the flag's default value, "
        "and whether any non-test `src/` translation unit outside the joint module references a "
        "joint or record symbol — so the day either fact moves, every verdict is re-decided against "
        "the new one rather than against a stored copy. Its CANDIDATE POPULATION is derived from "
        "the tree by scanning every source and build file, so it grows as the tree grows. And its "
        "two STOPs are live demands in both directions: a candidate block with no authored verdict "
        "halts it, so a comment written tomorrow cannot enter the population unclassified; and a "
        "verdict for a block the scan no longer finds halts it too, so a verdict cannot outlive "
        "the comment it grades. It stores no dated measurement of anything. ★ WHAT IT DOES NOT "
        "ASSERT, stated so the verdict is not read wider than it is: it does not claim the "
        "authored verdicts are RIGHT — only that every candidate carries one and that the facts "
        "they rest on still hold."),
    "tools/audit/index_status_lint.py": (
        LIVE, "index_status_lint.py:4-7, :16-20, :22-24",
        "It PARSES `OPEN_ITEMS.md` on every run and asserts a property of the index AS IT STANDS: "
        "every status cell opens with one canonical token, and every row splits into the expected "
        "number of cells. A row written tomorrow with a non-canonical opening fails tomorrow, and a "
        "clean index passes indefinitely — the shape of a live invariant rather than a dated "
        "reading. It also OWNS the vocabulary, the row split and the leading-token function that "
        "the ONE index parser imports (#6), so what it checks and what every derivation reads are "
        "the same code. Its own docstring draws the boundary that keeps it live: it does not judge "
        "whether a row's recorded state is CORRECT, only that the state is STATED in a form every "
        "derivation reads the same way."),
    "tools/audit/gen_reserved_word_scanner.py": (
        LIVE, "gen_reserved_word_scanner.py:11-20, :37-39",
        "★ CLASSIFIED LIVE DESPITE BEING REGISTERED NOT RUN, and the two facts are about different "
        "things. Its POPULATION is DERIVED from the tree on every run — the project's own musical "
        "vocabulary intersected with the words its governance surfaces use — and the invariant it "
        "asserts is about that population TODAY: every derived candidate carries an authored "
        "verdict, with an unclassified candidate a STOP. That is the `claude_md_rule_triage.py` "
        "shape exactly, and it was demonstrated rather than assumed: writing new governance prose "
        "in this very task moved the derived counts, which is what register entry D-661 means by "
        "*re-derived as the tree grows*. It is NOT RUN in the guard set for a separate and recorded "
        "reason — its STOP is its headline and it fails by design until the verdicts are authored, "
        "and a guard set carrying a member that fails by design teaches a reader to ignore the set. "
        "Classified for completeness on the same footing as the ratification-surface census above."),

    # ---- tools/audit/decisions — the register's own checks -----------------------------------
    "tools/audit/decisions/gen_decisions_register.py": (
        LIVE, "gen_decisions_register.py:11-16",
        "The register is GENERATED from its data, and `--check` regenerates and diffs ALL emitted "
        "files. \"The rendered register matches its source data\" is true or false of the tree at "
        "any moment, and an edit to either side is caught at once."),
    "tools/audit/decisions/gen_cluster_dispositions.py": (
        LIVE, "gen_cluster_dispositions.py:28-41 (the Usage block), :43-56 (why producibility is "
        "separate from --check)",
        "ALL THREE invocations are live. `--verify` locates every backbone verbatim IN THE FILE IT "
        "IS CITED TO and checks the cited START LINE — the drift check every home-document edit "
        "exercises. `--check` RE-READS the emitted artifacts and proves the coverage bijection over "
        "all clusters; it is live because that bijection is a property of the artifacts as they "
        "stand. `--producible` (authored 2026-08-07 on the user's ruling, `OPEN_ITEMS.md` OI-333) "
        "compiles every register pattern and runs the whole derivation in memory, writing nothing — "
        "a demand about the register as it stands today, since a pattern entered tomorrow that does "
        "not compile fails it tomorrow. Its detection was measured before it was authored here: on "
        "the clean tree it passes, and with one OI-333-shaped pattern re-introduced it names the "
        "entry and exits non-zero. ★ THE EVIDENCE STRING FORMERLY READ, in part: *'`--check` "
        "re-derives the dispositions from the current backbone and proves the bijection over all "
        "clusters'* — which was wrong about the first half in exactly the way OI-333 records, since "
        "`--check` re-reads and never re-derives. Corrected here with the former wording preserved "
        "(#12), because a classification's own evidence may not restate the error the row it "
        "classifies is about."),
    "tools/audit/decisions/gen_home_classification.py": (
        LIVE, "gen_home_classification.py:35-49",
        "★ CLASSIFIED LIVE DESPITE FAILING. It APPLIES the criteria in force to the WHOLE current "
        "home population and writes each entry's class; `--check` re-derives both the "
        "classification and its artifact. Its STOP — home documents with no authored delegation "
        "scope — fires because the population grows as waves enter entries, which is the tool "
        "asking for the authored input it refuses to guess. That is a live demand about today's "
        "register, not a dated reading. It stays, failing."),
    "tools/audit/decisions/gen_phase1p_delegation_bar.py": (
        LIVE, "gen_phase1p_delegation_bar.py:22-27, :39-49",
        "★ THE CASE THAT REFUTES THE ASSUMPTION THIS TASK WAS GIVEN, and the clearest demonstration "
        "of why R4 required a per-tool check. `OPEN_ITEMS.md` OI-309 names it \"the clearest "
        "candidate\" for the historical reading, on its own docstring's words — \"THIS ARTIFACT IS "
        "A PRE-APPLY RECORD, AND IT STAYS ONE\". But the frozen half was ALREADY SOLVED, by reading "
        "each entry's `class_before_phase1q` rather than its current class; and the LIVE half is "
        "load-bearing — the FORMS table is imported by `gen_home_classification.py` to classify "
        "against the delegations that exist TODAY, and every anchor is LOCATED in its surface, with "
        "a moved, missing or ambiguous one stopping the tool. It asserts a live invariant, it "
        "PASSES at the committed tree, and it stays."),
    "tools/audit/decisions/gen_phase1n_reading_regime.py": (
        POINT, "gen_phase1n_reading_regime.py:4-8; reads5_repack.json → why_the_regime_artifact_is_read_and_not_regenerated",
        "The artifact is a REGISTRATION recorded before the reads it governs (#17b). Re-deriving it "
        "does not reproduce it and passing would be the defect: OI-328 MEASURED that the ordering "
        "key flips, because a candidate proxy counts namings in user-ratified surfaces and the "
        "register's own homing work increments it for documents whose yield is already known (#20). "
        "The generator now STOPS with that reason. NO LIVE COVERAGE IS LOST — the packing rule it "
        "owns is imported and exercised by `gen_reads5_repack.py`, which passes."),
    "tools/audit/decisions/gen_reads5_repack.py": (
        LIVE, "gen_reads5_repack.py:9-27, :29-60, :70-81",
        "It reads the REGISTERED regime verbatim and never regenerates it, and imports the packing "
        "rule rather than copying it, so its --check is a live assertion that the re-pack still "
        "follows from the registration. ★ THE REASON IS CORRECTED 2026-08-07 (user's ruling R3, "
        "dispatch `cc_instruction_licensed_homing_and_oi344.md`; `OPEN_ITEMS.md` OI-344), because "
        "the clause it formerly carried was the claim the row refuted. THE FORMER REASON, "
        "PRESERVED (#12): \"It reads the REGISTERED regime verbatim and never regenerates it, and "
        "imports the packing rule rather than copying it. Its inputs are frozen artifacts, so its "
        "--check is a live assertion that the re-pack still follows from the registration — and it "
        "passes and can keep passing.\" Its inputs were NOT all frozen artifacts: the contamination "
        "measurement recomputed a rank correlation against the cluster-disposition layer on every "
        "run and stored it under a key DATING it 2026-08-04, so refreshing that layer — correct "
        "work — turned the check red. The two dated fields are now written once and read back "
        "(the tool's own docstring, and `reads5_repack.json` → "
        "`★_the_dated_figures_are_FROZEN_and_read_back`). THE VERDICT DOES NOT MOVE and the tool "
        "stays in the guard list: what it asserts is a live invariant — that the re-pack still "
        "follows from the registration, and that no read document's naming count in the "
        "user-ratified surfaces has moved since registration — and it now passes and can keep "
        "passing, which is what the classification turns on."),
    "tools/audit/decisions/gen_reads1_yield.py": (
        POINT, "gen_reads1_yield.py:2-9 (its own subject line), :11-21, :23-28",
        "★ RE-CLASSIFIED 2026-08-04 (dispatch `cc_instruction_finish_line_item1b.md`, ruling R2) — "
        "THE EARLIER VERDICT PUT THIS FAMILY ON THE WRONG SIDE, and the tool's own words say so: "
        "its subject is \"READ WAVE 1's measured yield, graded against the bands registered BEFORE "
        "the reads\", a completed instalment of an out-of-sample test whose bands are frozen "
        "precisely because re-deriving them would destroy the registration (:11-21). The live half "
        "it was credited with — that every entry the wave names is still in the register AT THE "
        "HOME IT RECORDS — IS NOT A LIVE INVARIANT: phase 1's own criterion C1 OBLIGES entries to "
        "be written into their owning specification, so a check that fails when an entry's home "
        "moves must eventually fail BECAUSE the tree moved on correctly, which is this ruling's "
        "own definition of measuring the clock. It fails at HEAD for the narrower of the two "
        "reasons: both entries it names are still homed in `ARCHITECTURE.md` and only the LINE "
        "RANGE moved, drifted by the insertions the previous wave's homing act made above them. "
        "NO LIVE COVERAGE IS LOST: that every entry still exists with a resolving reference and a "
        "verbatim quote at its home is asserted by `gen_decisions_register.py --check` (the "
        "register's own rule (d) guard) and `register_lint.py`, and that no register home anchor "
        "has drifted by `reaim_home_anchors.py --check` — all three live, all three passing."),
    "tools/audit/decisions/gen_reads2_yield.py": (
        POINT, "gen_reads2_yield.py:2-8 (the same construction as wave 1's); guard_state.json → runs",
        "Same verdict and same ground as wave 1's, and the same tool by construction: an "
        "instalment of the registered out-of-sample test, with the entry homes frozen as they "
        "stood when the wave ran. It PASSES at the committed tree today — and that is a fact about "
        "WHICH entries the previous wave's ten re-homings touched, not a difference in kind. "
        "Classified with its siblings rather than left to fail at the next homing wave, because a "
        "verdict is made on the tool's own text and this tool's text is theirs."),
    "tools/audit/decisions/gen_reads3_yield.py": (
        POINT, "gen_reads3_yield.py:2-8 (the same construction as wave 1's); guard_state.json → runs",
        "Same verdict, same ground, same construction. It passes at the committed tree for the "
        "same reason wave 2's does."),
    "tools/audit/decisions/gen_reads4_yield.py": (
        POINT, "gen_reads4_yield.py:2-8 (the same construction as wave 1's); guard_state.json → runs",
        "Same verdict, same ground, same construction. It passes at the committed tree for the "
        "same reason wave 2's does."),
    "tools/audit/decisions/gen_reads5_yield.py": (
        POINT, "gen_reads5_yield.py:2-15; finish_line_item1_routes.json → executed_this_wave",
        "★ RE-CLASSIFIED with wave 1's, and this is one of the two members where the mechanism is "
        "VISIBLE rather than argued: SIX of the ten entries the previous wave re-homed into "
        "`ARCHITECTURE.md` are named by this wave, so the home strings frozen in its artifact no "
        "longer match the register — the check fails because the homing act phase 1 requires was "
        "performed. Re-deriving it would restate a historical measurement against a population "
        "that act changed, which `OPEN_ITEMS.md` OI-330 refused. NO LIVE COVERAGE IS LOST, on the "
        "same three live guards named at wave 1's verdict."),
    "tools/audit/decisions/gen_reads6_yield.py": (
        POINT, "gen_reads6_yield.py:2-25; finish_line_item1_routes.json → executed_this_wave",
        "★ RE-CLASSIFIED with wave 1's; the other member where the mechanism is visible — FOUR of "
        "the previous wave's ten re-homed entries are named here. Its one further assertion, that "
        "the owed remainder derives from the regime's partition plus every completed wave's own "
        "count, does not make it live: every input to that derivation is frozen (a registration "
        "recorded before the reads, and each wave's own authored read list), so it cannot detect "
        "a change in the tree either — it re-computes a closed sum. NO LIVE COVERAGE IS LOST, on "
        "the same three live guards named at wave 1's verdict."),
    "tools/audit/decisions/gen_phase1m_measurements.py": (
        POINT, "gen_phase1m_measurements.py:4-19, :27-33",
        "Its own docstring says the dispatch \"orders two MEASUREMENTS and forbids acting on "
        "either\", and it applies nothing. Its authored KIND table is a judgment over the home "
        "population AS IT STOOD at phase 1m; the STOP fires because that population has GROWN, so "
        "passing again would mean re-authoring a historical measurement's judgment table for "
        "documents it never measured — restating a measurement against a changed population, the "
        "OI-330 shape. NO LIVE COVERAGE IS LOST: its delegation clauses are applied live by "
        "`gen_home_classification.py`."),
    "tools/audit/decisions/gen_phase1g_triage.py": (
        POINT, "gen_phase1g_triage.py:4-15; open_items/OI-207.md (the phase-1h note's moved counts)",
        "The emitted table is the decision surface the user ACCEPTED on 2026-08-02 (the "
        "41-document exclusion list). Its counts are cluster attributions that MOVE WHENEVER A "
        "DOCUMENT IS READ — measured at the phase-1h wave, which moved one document from 23 "
        "clusters to 19 and from rank 5 to rank 11 — so the check cannot pass while reading "
        "continues, and re-deriving would restate an accepted surface against a population the "
        "acceptance did not cover. It locates no quote and checks no anchor, so nothing live is "
        "lost with it."),
    "tools/audit/decisions/gen_decision_clusters.py": (
        LIVE, "gen_decision_clusters.py:10-14",
        "`--check` proves a round-trip over the current harvest: every candidate placed in exactly "
        "one cluster, the id set identical to the input, the input unchanged by the tool, with the "
        "input's own hash reported. A structural invariant of the data as it stands."),
    "tools/audit/decisions/gen_phase1w_legacy_verification.py": (
        LIVE, "gen_phase1w_legacy_verification.py:9-22",
        "★ CLASSIFIED LIVE DESPITE FAILING, and its failure is the live invariant FIRING. It "
        "DERIVES the marked set from the backbone rather than from a recorded figure, LOCATES every "
        "recorded figure and every code anchor an entry rests on, and STOPS when a quote is not at "
        "its cited line — \"so the evidence cannot go stale silently\", in its own words. That is "
        "exactly what it reported: one anchor drifted by 23 lines. Re-aiming it is a lawful repair "
        "and is NOT done here (the freeze). It is also load-bearing live — "
        "`gen_live_prohibition_pointers.py` derives its class from this artifact. It stays, "
        "failing."),
    "tools/audit/decisions/gen_reads4_oi326_application.py": (
        POINT, "gen_reads4_oi326_application.py:2-17; open_items/OI-330.md",
        "Read wave 4's measurement of the OI-326 ruling, taken BEFORE the ruling was applied on the "
        "user's own condition. OI-330 establishes both repairs inadmissible — re-pointing the "
        "anchor edits a historical measurement's tool, re-deriving restates it against the "
        "population the delegation writes changed. Its failure is not an invariant firing: the "
        "anchor became ambiguous BECAUSE THE USER WROTE A CORRECT DELEGATION. NO LIVE COVERAGE IS "
        "LOST — that each delegation citation still resolves is asserted by "
        "`gen_phase1p_delegation_bar.py`, which locates every anchor, stops on an ambiguous one, "
        "and passes."),
    "tools/audit/decisions/reaim_home_anchors.py": (
        LIVE, "reaim_home_anchors.py:13-22",
        "`--check` reports what would move and writes nothing, reading the drift from the verifier's "
        "OWN machinery so the number is by construction the number the guard reports. \"No register "
        "home anchor has drifted\" is a property of the tree right now."),
    "tools/audit/decisions/gen_live_prohibition_pointers.py": (
        LIVE, "gen_live_prohibition_pointers.py:23-27",
        "Its class membership is DERIVED from the phase-1w verification artifact and its pointers "
        "are checked against the live specification sections they name, quoting each section's own "
        "words rather than a line number precisely so the citation survives insertions. A live "
        "assertion that every entry in the class still carries its pointer."),

    # ---- guards that live outside tools/audit -------------------------------------------------
    "tools/open_items_split_check.py": (
        LIVE, "open_items_split_check.py:9-13",
        "Its default mode is called LIVING MODE in the file's own words — \"the standing "
        "register-health check, valid on the CURRENT tree no matter how many items are added after "
        "the split\". The bijection and the no-status-in-a-detail-file rule are properties of the "
        "register today."),
    "tools/notation_seams/gen_callpath_facts.py": (
        LIVE, "gen_callpath_facts.py:9-13",
        "\"The script re-reads each cited line at the current checkout and FAILS LOUDLY (exit 2) if "
        "the line does not contain the expected token.\" A citation that no longer matches is "
        "treated as a bit-rot finding, which is the definition of a live invariant."),
}


def build() -> dict:
    with open(STATE, encoding="utf-8") as fh:
        state = json.load(fh)

    ran = {r["tool"] for r in state["runs"]}
    failing = {r["tool"] for r in state["runs"] if r["verdict"] == "FAIL"}
    not_run = {n["tool"] for n in state["not_run"]}
    hist_state = {h["tool"] for h in state.get("historical_records", {}).get("tools", [])}
    population = sorted({rel for rel, _a, _w in gs.AUTHORED})

    missing = [p for p in population if p not in VERDICTS]
    if missing:
        raise Stop(f"tool(s) in the guard-state population with no authored verdict: {missing}")
    extra = [p for p in VERDICTS if p not in population]
    if extra:
        raise Stop(f"verdict(s) naming a tool the guard state does not carry: {extra}")

    point_here = {p for p, (v, _e, _w) in VERDICTS.items() if v == POINT}
    if point_here != set(gs.HISTORICAL):
        raise Stop(
            "the verdicts and gen_guard_state.HISTORICAL disagree — "
            f"only here: {sorted(point_here - set(gs.HISTORICAL))}; "
            f"only there: {sorted(set(gs.HISTORICAL) - point_here)}")
    if point_here != hist_state:
        raise Stop("guard_state.json's historical_records does not match the verdicts; "
                   "re-run gen_guard_state.py")

    rows = []
    for tool in population:
        verdict, evidence, why = VERDICTS[tool]
        rows.append({
            "tool": tool,
            "verdict": verdict,
            "evidence": evidence,
            "why": why,
            "in_the_live_guard_list_after_this_classification": verdict == LIVE and tool not in not_run,
            "state_at_the_committed_tree": (
                "FAIL" if tool in failing else
                "PASS" if tool in ran else
                "NOT RUN" if tool in not_run else
                "HISTORICAL" if tool in hist_state else "unknown"),
        })

    stays_failing = sorted(r["tool"] for r in rows
                           if r["verdict"] == LIVE and r["state_at_the_committed_tree"] == "FAIL")
    moved = sorted(r["tool"] for r in rows if r["verdict"] == POINT)

    return {
        "header": {
            "purpose": "Every guard classified under the user's ruling R4 of 2026-08-04: does it "
                       "RE-DERIVE A LIVE INVARIANT, or RECORD A MEASUREMENT TAKEN AT A POINT IN "
                       "TIME? One verdict per tool, with the evidence it was made from.",
            "generator": "tools/audit/gen_guard_classification.py",
            "ruling": "User, 2026-08-04 (READ WAVE 6, dispatch `cc_instruction_reads_6.md` §0a "
                      "ruling R4; `OPEN_ITEMS.md` OI-330): a tool that RE-DERIVES A LIVE INVARIANT "
                      "belongs in the guard list; a tool that RECORDS A MEASUREMENT TAKEN AT A "
                      "POINT IN TIME does not — CHECKED PER TOOL before any tool moves, a supposed "
                      "historical recorder that turns out to assert a live invariant STAYS.",
            "authored_inputs": ["VERDICTS — the classification, its evidence citation and its "
                                "reason, per tool. Nothing else."],
            "derived_from": [
                "gen_guard_state.AUTHORED (the population — imported, never restated)",
                "gen_guard_state.HISTORICAL (the invocation consequence — cross-checked both ways)",
                "guard_state.json (each tool's pass/fail state at the committed tree)",
            ],
            "what_this_does_not_do":
                "It repairs nothing. A tool classified as recording a point-in-time measurement "
                "keeps its artifact exactly as written, marked historical; a tool classified live "
                "stays in the list and fails if it fails. `OPEN_ITEMS.md` OI-309 and OI-330 are "
                "CLASSIFIED here, not discharged.",
        },
        "the_operational_form_of_the_test": (
            "Can this check pass forever while the tree moves on correctly, or must it eventually "
            "fail BECAUSE the tree moved on? The second kind measures the clock, not the "
            "repository. Two corollaries the population exercised: a tool whose POPULATION is "
            "derived from the tree (the CLAUDE.md rule triage, the home classification) is live "
            "even when it fails, because its failure is a demand about today; and a tool that "
            "LOCATES its citations in the files (the phase-1w verification, the delegation bar) is "
            "live even when its artifact carries a frozen finding, because a drifted anchor is a "
            "real event."),
        "the_assumption_this_task_was_given_and_what_happened_to_it": (
            "The dispatch declared assumption A1 — that OPEN_ITEMS.md OI-309's four failing tools "
            "are ALL point-in-time wave measurements — and said in terms that it came from "
            "filenames and a session report rather than from reading the tools, which is why R4 "
            "required the per-tool check. **A1 IS REFUTED IN PART, and the refuting member is the "
            "one OI-309 itself called 'the clearest candidate' for the historical reading**: "
            "`gen_phase1p_delegation_bar.py`. Its frozen half was already solved by reading each "
            "entry's pre-apply class rather than its current one; its live half is load-bearing "
            "(the home classifier imports its grade table, and it locates every delegation anchor "
            "in its surface, stopping on a moved or ambiguous one); and it PASSES at the committed "
            "tree. It stays. The other three of OI-309's four are point-in-time and move. One tool "
            "OUTSIDE OI-309's four also moves — OI-330's — which A1 did not cover."),
        "★_the_2026_08_04_re_classification_of_the_read_wave_yield_FAMILY": {
            "ordered_by": "`cc_instruction_finish_line_item1b.md`, ruling R2 — the read-wave yield "
                          "artifacts are checked against R4's test before the re-homing continues. "
                          "Its assumption A1 held that the three FAILING members are point-in-time "
                          "measurements sitting on R4's live side.",
            "what_happened_to_that_assumption": "CONFIRMED for all three, and the check found the "
                "family is larger than the failing set. The earlier classification put all six "
                "read-wave yield tools on the LIVE side, crediting each with one assertion: that "
                "every entry its wave names is STILL IN THE REGISTER AT THE HOME IT RECORDS, on "
                "the ground that 'an entry silently vanishing or changing home is a real defect'.",
            "why_that_was_the_wrong_side": "CHANGING HOME IS NOT A DEFECT — it is the act phase 1's "
                "criterion C1 requires, performed under a dispatch and recorded in the register "
                "with its provenance (#12). So the check must eventually fail BECAUSE the tree "
                "moved on correctly, which is this ruling's own definition of a check that "
                "measures the clock. The tool cannot separate the two cases: its --check is "
                "whole-artifact equality, so a correctly re-homed entry and a vanished one are "
                "indistinguishable to it.",
            "measured_rather_than_argued": "The previous wave re-homed ten entries into "
                "`ARCHITECTURE.md` (`finish_line_item1_routes.json` → `executed_this_wave`). Six "
                "of them are named by read wave 5 and four by read wave 6, and both artifacts now "
                "fail on exactly those home strings. Read wave 1 fails on the narrower cause — its "
                "entries never left `ARCHITECTURE.md` and only the LINE RANGE drifted under the "
                "same insertions. Waves 2, 3 and 4 pass, and that is a fact about which entries "
                "the ten touched, not a difference in kind.",
            "why_the_three_that_PASS_moved_with_them": "A verdict is made on the tool's own text "
                "(#19), and their text is their siblings'. Classifying identical tools onto "
                "opposite sides would author a verdict the evidence contradicts, and would leave "
                "three known false alarms armed for the next homing wave.",
            "no_live_coverage_is_lost": "The live half the family was credited with is asserted by "
                "three live guards that pass at the committed tree: `gen_decisions_register.py "
                "--check` (the register's own rule (d) guard — drift, quote fidelity, reference "
                "resolution), `register_lint.py`, and `reaim_home_anchors.py --check` (no register "
                "home anchor has drifted).",
            "the_scaling_fact_this_classification_buys": "Item 1's remaining re-homings move more "
                "entries, and every entry moved breaks every frozen artifact that names it at its "
                "old home. Left live, this family would have produced a fresh permanent failure "
                "per wave for the rest of the item — the failure mode R4 exists to prevent, where "
                "a list whose failures are permanent and meaningless teaches a reader to ignore "
                "it. This is what makes the rest of item 1 affordable without accumulating "
                "failures.",
            "what_this_does_NOT_do": "It repairs nothing and discharges nothing. The six artifacts "
                "stay on disk exactly as their waves wrote them; the registered bands and every "
                "measured yield are preserved (#12); `OPEN_ITEMS.md` OI-309 and OI-330 stay open "
                "on their own subjects.",
        },
        "counts": {
            "tools_classified": len(rows),
            "re_derives_a_live_invariant": sum(1 for r in rows if r["verdict"] == LIVE),
            "records_a_point_in_time_measurement": len(moved),
            "neither_not_a_guard": sum(1 for r in rows if r["verdict"] == NEITHER),
            "live_tools_that_FAIL_at_the_committed_tree_and_STAY": len(stays_failing),
        },
        "tools_that_leave_the_live_guard_list": moved,
        "live_tools_that_fail_and_stay": stays_failing,
        "rows": rows,
    }


def main(argv: list[str]) -> int:
    built = build()
    text = json.dumps(built, indent=2, ensure_ascii=False) + "\n"
    if "--check" in argv:
        have = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
        if have != text:
            print("STALE: guard_classification.json does not re-derive")
            return 1
        print("the guard classification re-derives")
        return 0
    with open(OUT, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    print(f"wrote {os.path.relpath(OUT, ROOT)}")
    c = built["counts"]
    print(f"  live {c['re_derives_a_live_invariant']} · "
          f"point-in-time {c['records_a_point_in_time_measurement']} · "
          f"neither {c['neither_not_a_guard']} · "
          f"live-and-failing {c['live_tools_that_FAIL_at_the_committed_tree_and_STAY']}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except Stop as exc:
        print(f"STOP: {exc}")
        sys.exit(2)
