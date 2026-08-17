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
        POINT, "gen_phase1_completion_inventory.py:11-26; "
               "cowork_rulings_2026_08_16_preparation_return.md §4",
        "★ RE-CLASSIFIED 2026-08-16, ON THE USER'S RULING AND NOT ON THIS TOOL'S JUDGMENT. Its "
        "SUBJECT — D-231's three-phase structure and what its phase 1 still required — was "
        "SUPERSEDED on 2026-08-15 when the user ruled the six-phase structure. What re-derives is "
        "not the question: a check can re-derive perfectly and still grade a program that no "
        "longer governs, and the ruling's own words are that the superseded phase-1 apparatus "
        "follows its phase into historical status. The ruled soft-discard then made it STOP rather "
        "than drift — the delegation grading it imports refuses to run for a document the "
        "retirement empties. ★ IT ASSERTS NOTHING ABOUT WHETHER PHASE 1'S OBLIGATIONS WERE "
        "DISCHARGED, and no completion claim rides the reclassification. ★ THE FORMER VERDICT, "
        "PRESERVED (#12): LIVE — \"It RE-DERIVES on every run: D-231's clause is located in "
        "`CLAUDE.md` by anchor string and must still be findable or the tool STOPS; every home "
        "class, defense gap and section-criterion verdict is read off the register as it stands; "
        "the open-row population and each row's gate verdict come from `OPEN_ITEMS.md` and the "
        "apparatus declaration as they stand today, and a verdict naming a row the index no longer "
        "carries open is a STOP. Nothing in it is a measurement taken at a point in time — a later "
        "wave that homes an entry or closes a row SHOULD move its output, and the check is what "
        "makes that movement visible.\" It was true of the tool and remains true of it; what "
        "changed is that the PROGRAM it grades was superseded, which the former verdict could not "
        "have anticipated."),
    "tools/audit/gen_phase1_finish_line.py": (
        POINT, "gen_phase1_finish_line.py:18-34; "
               "cowork_rulings_2026_08_16_preparation_return.md §4",
        "★ RE-CLASSIFIED 2026-08-16, ON THE USER'S RULING. Same ground as the completion inventory "
        "it imports: its subject is the SUPERSEDED phase 1's finish line, and the program it "
        "measures no longer governs. It STOPS for the same cause. Its last derivable state stands "
        "frozen on disk as the record of that program, and nothing in this reclassification says "
        "the program finished. ★ THE FORMER VERDICT, PRESERVED (#12): LIVE — \"Authored 2026-08-04 "
        "in answer to this tool's own per-tool STOP — it entered the guard population two waves ago "
        "and had never been classified. It IMPORTS both populations rather than storing them, "
        "locates D-231's clause by anchor at HEAD, and carries a STOP that is a live demand in the "
        "strongest form the population has: a population that grows WITHOUT AN ITEM TO CARRY IT "
        "stops the tool, which is what makes the list a finish line rather than a selection. It "
        "re-derives as the record moves under it, and it passes.\""),
    "tools/audit/decisions/gen_finish_line_item1_routes.py": (
        POINT, "gen_finish_line_item1_routes.py:8-17; "
               "cowork_rulings_2026_08_16_preparation_return.md §4",
        "★ RE-CLASSIFIED 2026-08-16, ON THE USER'S RULING. A view of the superseded phase-1 gate — "
        "it imports the finish line transitively — so its subject went with its phase, and its "
        "inputs STOP. ★ THE FORMER VERDICT, PRESERVED (#12): LIVE — "
        "\"Authored 2026-08-04 in answer to the same STOP. Its population is IMPORTED from the "
        "finish-line generator and never re-listed (#6), so it shrinks as entries are homed; and "
        "it REFUSES to run if any entry has no authored route or if a route names an entry the "
        "population no longer carries — in its own words, 'so the register moving under the table "
        "is a STOP rather than a silent partial answer'. That is a demand about today, not a dated "
        "reading: the AUTHORED half is the route per entry, and the tool will not let that half go "
        "stale silently. It passes at the committed tree.\""),
    "tools/audit/decisions/gen_r1_superseded_reach.py": (
        POINT, "gen_r1_superseded_reach.py:22-38; "
               "cowork_rulings_2026_08_16_preparation_return.md §4",
        "★ RE-CLASSIFIED 2026-08-16, ON THE USER'S RULING. Same family and same import chain: it "
        "applies a ruling to the superseded finish line's item-1 NO-HOME class, so its subject "
        "went with its phase and its inputs STOP. NO LIVE COVERAGE IS LOST — that every register "
        "cross-reference still resolves is asserted live by `gen_cluster_dispositions.py --verify`, "
        "which stays in the list and now consults the retired-entries block beside the live "
        "entries. ★ THE FORMER VERDICT, PRESERVED (#12): LIVE — "
        "\"Authored 2026-08-04 with the tool, so R4's per-tool condition was a design input. It "
        "IMPORTS its population from the route table rather than storing one, and re-reads the "
        "register on every run for each entry's status and each successor's home CLASS — so the "
        "HOMED verdict and the disposition move the day a successor is homed, which is exactly "
        "the event the ruling makes the owed act. Its sharpest STOP is a live demand on the "
        "record rather than on the tree's history: every AUTHORED successor must still be NAMED "
        "IN THE SUPERSEDED ENTRY'S OWN TEXT, so a session cannot nominate one the register does "
        "not name, and a reworded supersession stops the tool instead of silently keeping a "
        "verdict the record no longer supports. It re-derives and it passes.\""),
    "tools/audit/decisions/gen_item1_rehome_blocker.py": (
        POINT, "gen_item1_rehome_blocker.py:32-42; "
               "cowork_rulings_2026_08_16_preparation_return.md §4",
        "★ RE-CLASSIFIED 2026-08-16, ON THE USER'S RULING. Same family, same import, same STOP: "
        "what it measures is what blocked the SUPERSEDED finish line's item-1 re-home class. Its "
        "one live-looking assertion — that the standing autonomous-operation authorization is "
        "still locatable in `CLAUDE.md` by its anchor — is not lost: `CLAUDE.md`'s own anchors are "
        "asserted live by `claude_md_rule_triage.py` and by the register's home-anchor checks, all "
        "of which stay in the list. ★ THE FORMER VERDICT, PRESERVED (#12): LIVE — "
        "\"Authored 2026-08-04 with the tool, so R4's per-tool condition was a design input. Every "
        "half of it is a demand about TODAY: the population is IMPORTED from the route table and "
        "shrinks as entries are homed; each row's blocker is re-cut from that row's own recorded "
        "reason on every run, so a reworded reason moves the verdict instead of leaving a stale one "
        "standing; and the STANDING AUTHORIZATION it compares against is located in `CLAUDE.md` BY "
        "ANCHOR and quoted at HEAD, with a STOP if it cannot be found — so a change to what a "
        "session may edit moves this artifact rather than being silently outrun by it. It stores no "
        "dated reading of anything.\""),
    "tools/audit/decisions/gen_outstanding_delegations.py": (
        POINT, "gen_outstanding_delegations.py:36-46; "
               "cowork_rulings_2026_08_16_preparation_return.md §4; "
               "tools/audit/discard_reach_split.json",
        "★ RE-CLASSIFIED 2026-08-16, ON THE USER'S RULING. It is the FEEDER whose only importers "
        "are the two superseded gate derivations and nothing else, which is the limb of the "
        "derived split that placed it here rather than among the standing checks. It is also the "
        "tool that STOPS FIRST: the authored draft it needs is for a document the retirement "
        "empties. NO LIVE COVERAGE IS LOST — the home rules it served are asserted live by "
        "`gen_home_classification.py` and `gen_phase1p_delegation_bar.py`, both of which stay in "
        "the list. ★ THE FORMER VERDICT, PRESERVED (#12): LIVE — "
        "\"It RE-DERIVES the whole partition on every run, from the delegation grades it IMPORTS "
        "(`gen_phase1p_delegation_bar.FORMS`) and the home population it IMPORTS "
        "(`gen_home_classification.home_population`) — never from a stored figure. Three STOPs are "
        "about the record as it stands today: a write-list member with no authored state label, a "
        "label naming a non-member, and a class-C document with no authored draft. A later wave "
        "that writes a delegation or widens one SHOULD move its output, which is the point of it "
        "(D-640 / OI-335).\""),
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
    "tools/audit/gen_filing_convention_application.py": (
        LIVE, "gen_filing_convention_application.py:14-40",
        "LIVE, and for the same reason its sibling sizing pass is: the artifact's CONTENT is "
        "authored judgment about documents, so what the check asserts is not that the verdicts are "
        "right — a verdict about a document cannot be checked by a tool — but three demands about "
        "the record as it stands TODAY. Its POPULATION is re-derived over the named surface set on "
        "every run and reconciled with the authored verdicts in BOTH directions, so a document "
        "entering or leaving the candidate set halts it rather than being verdicted silently or "
        "quietly dropped. And its SOUNDNESS against the seeds is re-computed on every run and "
        "published, so a signature that stops finding what the record already holds is reported "
        "rather than trusted. ★ ONE THING IS STATED PLAINLY BECAUSE THE ARTIFACT SAYS IT OF "
        "ITSELF: the derivation's REACH is unmeasured and is BOUNDED on the artifact rather than "
        "measured, under D-673 — so a green check here means the enumeration re-derives and its "
        "verdicts reconcile, never that the population is complete."),
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

    # ---- AUTHORED 2026-08-15, cc_instruction_period_checks.md Task 3 -------------------------
    # Both tools were added by this dispatch's own Tasks 1 and 2 and are classified in the same act
    # that registers them, so R4's per-tool condition is met before either enters the run rather
    # than after a later pass's STOP finds them.
    "tools/audit/gen_period_stratum_split.py": (
        LIVE, "gen_period_stratum_split.py:14-22 (what is derived), :37-47 (the five STOPs)",
        "LIVE on the ruling's own operational form — can this check pass forever while the tree "
        "moves on correctly? It can: its inputs are two committed artifacts and its output is a "
        "derived view of them, so it passes indefinitely and fails exactly when an input moves "
        "without the view being regenerated. Nothing in it is dated: every count is recomputed from "
        "the artifacts on every run, and the AUTHORED half is three citations — the ruled start "
        "commit, the two specification-bearing roles, and a registered expectation that is graded "
        "and never used as an input. Its STOPs are demands about the artifacts as they stand, and "
        "the sharpest is the reconciliation: the totals it derives must equal the totals the input "
        "artifact publishes of itself, so a hand edit to either file halts it rather than moving "
        "the split silently. ★ WHAT IT DOES NOT ASSERT: the enumeration underneath its inputs is "
        "UNESTABLISHED (#19) and the artifact says so in its own words — a green check here means "
        "the split follows from those artifacts, never that they are complete or correct."),
    "tools/audit/gen_july_screen.py": (
        LIVE, "gen_july_screen.py:22-30 (what is derived), :59-69 (the five STOPs), and its "
        "`retrieve()` function (the per-run git-object retrieval)",
        "LIVE, and the verdict is worth stating because the artifact's CONTENT is authored "
        "judgment about documentation changes — which a tool cannot check. What the check asserts "
        "is two demands about the record as it stands TODAY. Its POPULATION is IMPORTED from the "
        "split artifact on every run and reconciled with the authored verdicts in BOTH directions, "
        "so a hunk entering or leaving the screened population halts it rather than being graded "
        "silently or quietly dropped. And every screened hunk's TEXT is RE-RETRIEVED from the git "
        "object by explicit hash on every run, its recorded header located and its line counts "
        "cross-checked against the population's own record — so a coordinate that stops "
        "identifying the change it was read at is reported rather than trusted. Neither is a dated "
        "reading. Its other STOPs ride with it: the four-class vocabulary and the shape vocabulary "
        "are closed, a RATIFIED-ACT verdict must name the act AND where its ratification is "
        "recorded, and a verdict with no ground halts it."),

    # ---- AUTHORED 2026-08-15, cc_instruction_artifact_inventory.md ---------------------------
    # Classified in the act that registers it, so R4's per-tool condition is met before it enters
    # the run rather than after a later pass's STOP finds it.
    "tools/audit/gen_artifact_inventory.py": (
        LIVE, "gen_artifact_inventory.py:36-46 (the four STOPs), and its `--check` branch",
        "LIVE, and the verdict turns on a design choice made to earn it. An inventory of a tree is "
        "a dated thing by nature: re-derive it at the CURRENT commit and it fails the moment "
        "anyone commits anything, which is the OI-301/OI-305 shape exactly. So `--check` "
        "re-derives at the commit the committed artifact RECORDS -- that half passes indefinitely "
        "and fails only if the artifact or the table was edited by hand -- and then runs the "
        "classification AGAIN over the tree as it stands. That second run asserts a property of "
        "the repository TODAY: every file it carries is named by some rule. It is the "
        "`claude_md_rule_triage.py` shape -- a DERIVED population that grows as the tree grows, "
        "with an unclassified member a STOP. The last rule in the table is deliberately bounded "
        "rather than a catch-all so that STOP can fire, and the artifact carries probes that "
        "establish both halves: that a path in an unnamed top-level directory comes back "
        "unclassified, and that the tool then raises. ★ WHAT IT DOES NOT ASSERT: that any file is "
        "in the RIGHT class. The table is authored and only its coverage is checked, which the "
        "artifact states of itself."),
    "tools/audit/gen_artifact_inventory_surface.py": (
        LIVE, "gen_artifact_inventory_surface.py:40-49 (the four STOPs), and its `build()` "
        "two-way reconciliation against the inventory's class list",
        "LIVE, and for the same reason `gen_july_screen.py` is: what it re-derives is not the "
        "verdicts, which are authored judgments about how artifacts should be used, but that the "
        "surface and the inventory still describe the same population. Its POPULATION is IMPORTED "
        "from the inventory artifact on every run and reconciled with the authored proposals in "
        "BOTH directions, so a class entering or leaving the inventory halts it rather than being "
        "left unproposed or proposed for nothing. Its citation split is RE-SCANNED at the "
        "governing record on every run, so a document that stops being cited moves side rather "
        "than staying where a dated reading put it. Neither is a point-in-time reading. Its "
        "vocabulary STOPs ride with it: a role or mining verdict outside the closed set the "
        "user's direction names halts it, and so does a proposal with no reason."),

    # ---- AUTHORED 2026-08-15, cc_instruction_ruled_inventory_landing.md Task 2 ---------------
    # Three tools, on the user's Ruling of 2026-08-15 (`cowork_rulings_2026_08_15_inventory_
    # sitting.md` §5) ordering the third standing red cleared WITH its extension. The first had
    # reached the derived population with no verdict and is this tool's own STOP working; the other
    # two gain their invocation in the same act, so a verdict is authored for each here rather than
    # left for a later pass to STOP on. Every citation below was READ IN FULL in this session, in
    # the tool it names, with the file tools.
    "tools/audit/gen_discard_records.py": (
        LIVE, "gen_discard_records.py:31-37 (why a located pointer table and not a scanner), "
              ":221-246 (`record_span` — the per-run location), :299-394 (the five STOPs), "
              ":396-423 (the soundness check against its two negative seeds)",
        "★ THE ENTRANT THIS PASS'S STOP HAD BEEN NAMING, entered 2026-08-13 by the act that "
        "created it under the user's Ruling 69 (D-677) and reaching this table unclassified — the "
        "same shape `gen_phase1_finish_line.py`'s entry records for an earlier entrant, and R4's "
        "per-tool condition made mechanical. LIVE on the ruling's own operational form: can it "
        "pass forever while the tree moves on correctly? It can, and it does at the committed "
        "tree. NOTHING IN IT IS STORED. Each of the three elements Ruling 69 requires of a discard "
        "record is RE-LOCATED on every run, inside the span that record's own heading opens, so a "
        "reworded record STOPS it rather than leaving a citation to text nobody re-read; each "
        "row's OPEN state comes from the ONE index parser it imports rather than from a copy (#6); "
        "and the #19 carve-out is derived from the committed apparatus declaration's own recorded "
        "gate grounds, never listed here, with a missing artifact a STOP rather than a silent "
        "empty set. Its STOPs are demands about the record as it stands TODAY and they run in both "
        "directions: a pointer at a row the INDEX no longer carries, a row that has RESOLVED, a "
        "row the carve-out keeps gating, a discard on the open-items register's own two surfaces "
        "that the table does not enter, and a NOT-DISCARDED worth-test outcome being read as a "
        "discard. ★ WHAT IT DOES NOT ASSERT, stated so the verdict is not read wider than it is: "
        "that any discard VERDICT is right — a worth-test judgment cannot be checked by a tool — "
        "only that every entered record carries its three elements and that the table and the "
        "open-items register's own surfaces agree. Its completeness is BOUNDED to those two "
        "surfaces, which the artifact states of itself."),
    "tools/audit/gen_status_archive_pass.py": (
        LIVE, "gen_status_archive_pass.py:35-52 (what `--check` proves, and why the first claim is "
              "stamped to a commit), :150-173 (the moved-set STOP), :189-191 (the three "
              "reconciliation reads)",
        "★ CLASSIFIED IN THE ACT THAT FINALLY REGISTERS IT — it joined the derived candidate "
        "population on 2026-08-11 carrying a `--check` mode with no authored invocation, which is "
        "the condition `OPEN_ITEMS.md` OI-373 records. LIVE, and the verdict turns on a design "
        "choice the tool made to earn it. An archive pass is a completed act, so the naive check — "
        "compare the live file against a fixed base — must fail on the first legitimate append, "
        "which is the OI-344 shape the tool names of itself. So the ONE claim that is about a "
        "single moment is checked at THAT MOMENT'S OWN GIT OBJECT by explicit hash and cannot "
        "decay, while the two claims that are durable are re-read at HEAD on every run: the moved "
        "block is still verbatim in `STATUS_ARCHIVE.md`, and it is still absent from `STATUS.md`. "
        "Those two are a live invariant nothing else asserts — an edit that truncates the archive, "
        "or a later act that re-introduces the block into the must-read, is caught on the next "
        "run, forever. Its moved-set STOP is a demand of the same kind, requiring every entry in "
        "the moved range to carry either the derived signal or an authored clause. ★ WHAT IT DOES "
        "NOT ASSERT: that `STATUS.md` is readable again — it is not, and OI-370 stands — only "
        "that nothing left the live file which is not in the archive, and that nothing else left "
        "it."),
    "tools/audit/gen_doc_change_candidates.py": (
        LIVE, "gen_doc_change_candidates.py:15-24 (what is derived and what is authored), :62-70 "
              "(the five STOPs), :1006-1010 (`--check` reads the range's END back from the "
              "committed artifact)",
        "★ CLASSIFIED IN THE SAME ACT, and for the reason `gen_july_screen.py` and "
        "`gen_period_stratum_split.py` are LIVE: what it re-derives is not a judgment but the "
        "enumeration itself. Every commit, every hunk, every verdict and every count is recomputed "
        "from GIT OBJECTS on each run — the population from `rev-list`, each hunk from `show -U0 "
        "-M -C` — and the range's END is read back from the committed artifact rather than taken "
        "as HEAD, so a later commit does not turn it red, which is the OI-301/OI-305 shape "
        "avoided by construction rather than tolerated. What it asserts is therefore a live "
        "invariant: the committed candidate list still follows from the history it was drawn from, "
        "and a hand edit to either artifact halts it instead of moving that list silently. Its "
        "STOPs ride with it — a hunk carrying no verdict, a PURE verdict with no clause, a "
        "boundary commit that is not an ancestor of the range end, and two reconciliations that "
        "must balance. ★ WHAT IT DOES NOT ASSERT: that a FLAG is a defect or a PURE harmless — its "
        "own words are that neither verdict is a view on whether a change should have happened — "
        "and the recoverability of the generated-artifact class it does not enumerate per hunk is "
        "published as UNESTABLISHED rather than assumed."),
    "tools/audit/gen_test_construction_evidence.py": (
        LIVE, "gen_test_construction_evidence.py, the `★ WHY EVERY READ IS PINNED` paragraph of "
              "its module docstring and its `THE STOPS` list; `build()`'s two-way reconciliation "
              "against the inventory's class membership",
        "★ TASK 3's OWN TOOL, CLASSIFIED IN THE ACT THAT CREATES IT — the practice the two entries "
        "above exist because two earlier acts did not follow. LIVE on the same ground "
        "`gen_period_stratum_split.py` is: its input is a committed artifact and its output a "
        "derived view of that artifact, so it passes indefinitely and fails exactly when the input "
        "moves without the view being regenerated. Every reading of a test — the file's own text, "
        "its commit subjects, the specification-document name set — is taken from GIT OBJECTS at "
        "the commit the committed inventory RECORDS, so editing a test does not turn it red, which "
        "is the OI-301/OI-305 shape avoided by construction. What is LIVE is the POPULATION: it is "
        "re-read from that inventory on every run and reconciled with the graded set in BOTH "
        "directions, so a member entering or leaving the class halts it rather than being graded "
        "silently or quietly dropped. Its other STOPs are demands of the same kind — a member with "
        "no verdict, a verdict outside the closed two-value vocabulary the user's ruling fixes, a "
        "SPEC-DERIVED-EVIDENCE verdict resting on no located statement, and a distribution that "
        "does not reconcile. ★ WHAT IT DOES NOT ASSERT, and its own artifact says so: that the "
        "recognizers are complete. Their reach is UNMEASURED, and what bounds the error is the "
        "ruling's own default — an unestablished construction is treated as code-built, so a "
        "missed statement errs toward exclusion, which the ruling records as the recoverable "
        "direction."),

    # ---- AUTHORED 2026-08-15, cc_instruction_preparation_opening.md Task 2 -------------------
    # Task 2's own tool, classified in the act that creates it — the practice the entries above
    # exist because two earlier acts did not follow, and which this dispatch makes a standing rule.
    "tools/audit/gen_decisions_filter.py": (
        LIVE, "gen_decisions_filter.py, the `THE STOPS` list of its module docstring and its "
              "`build()` two-way reconciliation of the population against the rendered INDEX",
        "LIVE, and the verdict is worth stating because the artifact's CONTENT is a PROPOSAL "
        "awaiting the user — a reading of whether each entry's record names a deciding act — which "
        "no tool can check. What the check asserts is three demands about the decisions register "
        "AS IT STANDS. Its POPULATION is the register's whole data file, re-read on every run and "
        "reconciled with the rendered INDEX's entry identities in BOTH directions, so an entry "
        "entering or leaving either surface halts it rather than being classified silently or "
        "quietly dropped — which is D-671 made mechanical. Every entry must carry the fields the "
        "classification reads, so one it cannot classify at all stops it instead of being skipped. "
        "And the distribution must account for the population exactly. None of the three is a "
        "dated reading: each is re-answered against the register as it stands, and an entry added "
        "tomorrow is classified tomorrow. Its other STOPs ride with it — a duplicate entry "
        "identity, and a status outside the vocabulary the data file's own header declares. "
        "★ WHAT IT DOES NOT ASSERT: that any entry is in the right class. The recognizers are "
        "authored and only their application is checked, and the observation-shape limb of the "
        "ruling it serves has UNMEASURED reach, which the artifact states of itself (#19)."),

    # ---- AUTHORED 2026-08-15, cc_instruction_preparation_opening.md Task 3 -------------------
    "tools/audit/gen_retirement_caller_check.py": (
        LIVE, "gen_retirement_caller_check.py, the `WHY THE READING IS PINNED TO A COMMIT` "
              "paragraph of its module docstring and its `THE STOPS` list; `candidacies()`'s "
              "two-way reconciliation of the derived flags against the authored conditions",
        "LIVE, on the same ground `gen_test_construction_evidence.py` is. The REFERENCE reading is "
        "a statement about one tree and is taken at the commit the committed artifact RECORDS, so "
        "it re-derives forever instead of going red the first time anybody writes a file that "
        "names a flagged one — the OI-301/OI-305 shape avoided by construction rather than "
        "tolerated. What is LIVE is the POPULATION, and it is live twice over: the retirement "
        "flags are re-imported from `gen_artifact_inventory_surface.py`'s own authored table on "
        "every run, so this check and the ruling surface cannot disagree about what is flagged "
        "(#6); and the citation split that decides which members of a mixed class are flagged is "
        "RE-SCANNED at the governing record, so a document that starts or stops being cited moves "
        "side here exactly as it does there. Its STOPs are demands of the same kind — a flagged "
        "class the inventory does not carry, a mixed class it publishes no members for, a derived "
        "member count disagreeing with the count the inventory publishes, the authored conditions "
        "and the derived candidacies disagreeing in either direction, a condition whose quoted "
        "sentence is no longer in the ruling record, a verdict outside the closed vocabulary, and "
        "a tally that does not account for the candidacies. ★ WHAT IT DOES NOT ASSERT, and its "
        "own artifact says so: that NONE FOUND means nothing depends on a file. A reference built "
        "at run time carries no literal to find and a binary blob is not searched, so the reading "
        "is generous in the safe direction and its limits are published above its first use."),

    # ---- AUTHORED 2026-08-16, cc_instruction_preparation_second.md Task 2 --------------------
    "tools/audit/gen_deciding_act_recovery.py": (
        LIVE, "gen_deciding_act_recovery.py, the `THE STOPS` list of its module docstring; "
              "`reconcile()`, which is called on the imported population in both directions; "
              "`locate_ruling()`, which locates every sentence of the ruling in its record",
        "LIVE. Everything it asserts is a demand about the record AS IT STANDS, and each becomes "
        "false the moment the record moves under it: the non-keep population imported from the "
        "committed filter artifact and the decisions register's data file must carry the same "
        "entries in BOTH directions, so an entry entering or leaving that population halts it "
        "rather than being recovered silently or quietly dropped; every entry must carry the "
        "fields the pass reads; every result must be one of the closed three values and the "
        "distribution must account for the population; and every sentence of the ruling that "
        "ordered the pass must still be in its ruling record, which is the same shape the "
        "retirement caller-check's conditions carry — a pass may not outlive the words that "
        "ordered it. It is NOT a dated reading: it re-follows every citation and re-searches every "
        "document on each run, so a user act written into a cited document tomorrow is recovered "
        "tomorrow, and a citation that stops resolving is reported tomorrow. ★ WHAT IT DOES NOT "
        "ASSERT, and its own artifact says so: that an ACT-FOUND is a verdict, or that a "
        "NOTHING-FOUND means no act exists. The first is evidence for the user to read; the second "
        "is a statement about the documents one entry's OWN citations reach, at one level, and the "
        "one-level bound is published above the first result."),

    # ---- AUTHORED 2026-08-16, cc_instruction_preparation_second.md Task 3 --------------------
    "tools/audit/gen_rulings_sort.py": (
        LIVE, "gen_rulings_sort.py, the `THE STOPS` list of its module docstring; "
              "`require_known_nonspec()`, which refuses a value the pass has not ruled on; "
              "`locate_definitions()`, which locates every quoted header definition",
        "LIVE. Its subject is the decisions register AS IT STANDS, and every demand it makes "
        "becomes false the moment that record moves: the confirmed population imported from the "
        "committed filter artifact and the register's data file must carry the same entries in "
        "BOTH directions, so an entry entering or leaving the confirmed side halts it rather than "
        "being sorted silently or quietly dropped; a `nonspec_kind` value the pass neither maps "
        "nor deliberately leaves to the recognizers halts it, so a value entered tomorrow is ruled "
        "on tomorrow instead of being classified by silence; and every definition the mapping "
        "quotes must still be in the data file's own header, which is the same shape the "
        "retirement caller-check's conditions and the recovery pass's ruling sentences carry — a "
        "mapping may not rest on words the record has dropped. ★ WHAT IT DOES NOT ASSERT: that "
        "any entry is in the right class. The word recognizers are authored, they decide only what "
        "the register's own home classification leaves undecided, and neither their reach nor "
        "their error rate is measured (#19) — which is why the entries they cannot place return to "
        "the user rather than being placed."),

    # ---- AUTHORED 2026-08-16, cc_instruction_preparation_third.md Task 1 ---------------------
    "tools/audit/gen_sole_carrier_subclass.py": (
        LIVE, "gen_sole_carrier_subclass.py, the `THE STOPS` list of its module docstring; "
              "`locate_ruling()`, which locates every sentence of the ruling in its record on "
              "every run; `signal_probes()`, which requires each signal to fire and to stay quiet; "
              "`json_at()`, whose own comment states which half is frozen and why",
        "LIVE, and the live half is narrower than most here, so it is named rather than implied. "
        "What re-derives against the record AS IT STANDS is the ruling itself: every sentence that "
        "DEFINES the sole-carrier subclass is located in `cowork_rulings_2026_08_16_"
        "preparation_return.md` on each run, and a ruling record edited to drop the guard's "
        "definition turns this red — the same shape the retirement caller-check's conditions and "
        "the recovery pass's ruling sentences carry, and it matters more here than in either, "
        "because this artifact is what WITHHOLDS entries from a discard. Live too are the five "
        "signal establishments: each of the three signals must be shown both to fire on a case "
        "that should fire it and to stay quiet on one that should not, so a signal returning empty "
        "over the whole population cannot be mistaken for one that cannot fire at all (#19) — "
        "which is exactly the state two of the three are in. ★ WHAT IT DELIBERATELY DOES NOT "
        "ASSERT, stated because the omission is a design decision and not an oversight: that the "
        "subclass re-derives against the CURRENT decisions register. Its three inputs are read "
        "from the git objects at the commit the artifact records, because the discard this guard "
        "stands in front of MOVES those very inputs — an input read live would be changed by the "
        "act this artifact authorizes, and the published record of which entries were withheld "
        "would be destroyed by the act it guarded (#12; the OI-301 hazard). It also asserts "
        "nothing about whether any entry's verdict is right, and nothing about worth: a "
        "sole-carrier verdict is a statement about WHERE THE CONTENT LIVES and about nothing "
        "else."),

    # ---- AUTHORED 2026-08-16, cc_instruction_preparation_third.md Task 2 ---------------------
    "tools/audit/gen_ratified_document_check.py": (
        LIVE, "gen_ratified_document_check.py, the `THE STOPS` list of its module docstring; "
              "`b1_keeps()`, which PARSES the ten keeps from the ruling record and halts on any "
              "other number; `locate_ruling()`, which locates every ordering sentence; "
              "`passage_of()`, which re-reads each recorded coordinate and cross-checks it",
        "LIVE, and its live half is the strongest of the three passes this preparation phase has "
        "added. Its POPULATION is parsed from the ruling record on every run: the ten entries the "
        "(B1) limb kept are read out of the ruling's own bullet, and a bullet naming any number "
        "other than ten, or naming an entry the recovery pass did not return ACT-FOUND for, halts "
        "it rather than being corrected — so the population cannot drift away from the words that "
        "fixed it, and the derivation cannot outlive them. Live too is the coordinate "
        "cross-check: every act the recovery pass recorded as a document, a line and a span is "
        "re-read and compared with the quote that pass published, so a document that has moved "
        "under a line is reported rather than graded as though it had not. ★ WHAT IT DELIBERATELY "
        "DOES NOT ASSERT: that its evidence re-derives against the CURRENT decisions register. "
        "Its inputs are read from the git objects at the commit the artifact records, on the same "
        "ground its sibling guard states — the soft-discard this evidence is gathered for moves "
        "those very inputs (#12; the OI-301 hazard). It asserts nothing about whether any entry's "
        "result is right: the ratification recognizer is authored, its reach is unmeasured (#19), "
        "and every result is published with the passage quoted at its line so the reading is the "
        "user's and not this tool's."),

    # ---- AUTHORED 2026-08-16, cc_instruction_preparation_third.md Task 3 ---------------------
    "tools/audit/decisions/apply_soft_discard.py": (
        LIVE, "apply_soft_discard.py, the `THE STOPS` list of its module docstring; "
              "`population()`, which derives the discard set and halts on a sole-carrier inside it "
              "or on an entry the data file does not carry live; `check_applied()`, whose "
              "docstring states which half is live in which of the two states this act can be in",
        "LIVE in BOTH of the states this tool can be in, which is why it is a guard rather than a "
        "record of an act. BEFORE the act — the state at this commit, the act having been planned, "
        "measured and reverted — what re-derives is the PLAN: the ruling's sentences must still be "
        "in its ruling record, the population must still be derivable from the committed recovery "
        "and sole-carrier artifacts in both directions against the decisions register's data file "
        "(D-671), and the committed plan must still match that derivation, so an artifact moving "
        "under the plan turns this red instead of leaving a stale plan to be executed later. AFTER "
        "the act the plan is un-derivable by construction, and the live assertion becomes the "
        "applied state's own arithmetic: live plus retired accounting for the recorded former "
        "population, no entry in both blocks and none in neither, and every retired record "
        "carrying the four things the ruling requires. ★ WHAT IT DOES NOT ASSERT: that the act "
        "SHOULD be performed. It was not: the dispatch's assumption A3 was falsified by the "
        "measurement, and what is committed is the plan and the tool, never a mutation."),

    # ---- AUTHORED 2026-08-16, cc_instruction_preparation_fourth.md Task 1 --------------------
    # Task 1's own two tools, classified in the act that creates them — the standing practice.
    # Every citation below was READ IN THIS SESSION, in the tool it names, with the file tools.
    "tools/audit/gen_phase1_gate_readers.py": (
        LIVE, "gen_phase1_gate_readers.py, the `★ WHY THE ENUMERATION IS PINNED TO A COMMIT` "
              "paragraph of its module docstring and its `THE STOPS` list; `build()`, which "
              "derives each generator's own output artifact from that generator's source and "
              "halts if it cannot; `locate_ruling()`, which locates every ordering sentence",
        "LIVE, on the same ground `gen_test_construction_evidence.py` is, and the live half is "
        "named rather than implied. The ENUMERATION is a statement about one tree and is taken "
        "from the git objects at the commit the artifact RECORDS, so it re-derives forever instead "
        "of going red the first time anybody writes a file naming one of these artifacts — the "
        "OI-301 / OI-305 shape avoided by construction rather than tolerated. What is LIVE is the "
        "APPARATUS and the words that ordered the pass: every sentence of the ruling must still be "
        "in `cowork_rulings_2026_08_16_preparation_return.md`, and every generator the ruling "
        "names must still exist and must still name its own output artifact — a generator that has "
        "gone, or one whose artifact can no longer be derived from its source, halts this check "
        "rather than shrinking the population silently. Its LIVE-consumer STOP is a demand of the "
        "same kind and is the ruling's own. ★ WHAT IT DOES NOT ASSERT, and its own artifact says "
        "so: that a file naming none of these artifacts depends on none of them. A path built at "
        "run time carries no literal to find and a binary blob is not searched, which is the same "
        "bound the retirement caller-check publishes of itself. It also asserts nothing about "
        "whether a verdict is RIGHT — the ground of each and the naming line are published beside "
        "it, so the reading is the user's."),
    "tools/audit/gen_governing_surface_spans.py": (
        LIVE, "gen_governing_surface_spans.py, the WHAT A SPAN IS and THE CLASSES paragraphs of "
              "its module docstring and its THE STOPS list; `measure()`, whose reconciliation "
              "compares the decomposition against the file's own measured size",
        "LIVE. It re-reads all five governing files AS THEY STAND on every run and re-cuts and "
        "re-classes every span from their current text, so an edit to any of them moves its "
        "output the day the edit lands — which is the point of it, because the pruning act it "
        "measures for has not happened and the files keep moving under it. Its load-bearing STOP "
        "is a demand about the tree rather than a dated reading: the per-class byte counts must "
        "account for the file EXACTLY. ★ WHAT IT DOES NOT ASSERT, and its own artifact says so: "
        "that a span classed `operative-rule-text` IS operative. The classes are recognizers over "
        "prose, their reach is UNMEASURED (#19), and the direction of their error is the "
        "recoverable one — a missed marker keeps a span at site, which is the ruled doubt default."),
    "tools/audit/gen_governing_surface_readers.py": (
        LIVE, "gen_governing_surface_readers.py, the WHAT IS DERIVED and WHAT IT DOES NOT "
              "ESTABLISH paragraphs of its module docstring; `measure()`, which scans the tracked "
              "tree; `render_surface()`, which builds the ruling surface from both artifacts",
        "LIVE. Every naming, anchor, parser and register home it publishes is re-scanned at the "
        "tracked tree on every run, so a file that starts naming `CLAUDE.md` tomorrow appears "
        "tomorrow. That is not the OI-301 shape it would be if the artifact were a completed "
        "measurement someone had ruled on: nothing has been ruled from it, the pruning act it "
        "measures for has not happened, and a reach that has changed since the measurement is "
        "exactly what a session about to move a span needs to be told. ★ WHAT IT DOES NOT ASSERT: "
        "that a naming is a DEPENDENCY, or that a file naming none of the five depends on none of "
        "them — the scan sees tracked files only and a path composed at run time carries no "
        "literal to find, the same bound the retirement caller-check publishes of itself."),
    "tools/audit/gen_status_batch_bound.py": (
        LIVE, "gen_status_batch_bound.py, THE STOPS of its module docstring; `build()`, which "
              "re-reads both live files on every run; `moved_entries()`, which derives membership "
              "from the entries' own words at the base commit's git object",
        "LIVE. Both of its claims are re-answered against the tree AS IT STANDS on every run — the "
        "moved entries still byte-present in `STATUS_ARCHIVE.md` exactly once, and still absent "
        "from `STATUS.md` — so an entry put back into the must-read, or quietly dropped from the "
        "archive, fails on the day it happens. ★ ONE HALF IS DELIBERATELY FIXED AND IT IS NOT A "
        "DATED READING EITHER: WHICH entries moved is a statement about the file as it stood when "
        "the act ran, so it is derived from that commit's own git object rather than from a file "
        "that legitimately grows by every later batch's entries — the OI-344 shape avoided by "
        "construction, on the precedent `gen_status_archive_pass.py` sets. ★ WHAT IT DOES NOT "
        "ASSERT: that the must-read is small enough to read, which is [[OI-370]]'s own subject, or "
        "that every superseded entry has moved — it proves only that what left is in the archive "
        "and that nothing else left."),
    "tools/audit/gen_claude_md_finer_spans.py": (
        LIVE, "gen_claude_md_finer_spans.py, THE STOPS of its module docstring; `build()`, which "
              "re-cuts and re-classes the file on every run and STOPs unless the per-class byte "
              "counts account for it to the character",
        "LIVE, on exactly the ground the coarse decomposition is live on. Its subject is a PINNED "
        "reading, but the demand it asserts is about the tree rather than a dated finding: the "
        "decomposition must re-derive and the per-class byte counts must account for the file "
        "EXACTLY, so a change to the cut rules or the recognizers that dropped a span would fail "
        "on the day it was made. The pin is what stops it going red at every later commit, the "
        "artifact being evidence for a ruling the user has not yet given. ★ WHAT IT DOES NOT "
        "ASSERT: that a span classed `operative-rule-text` IS operative, and that a span cut "
        "inside a block is readable on its own — which is why every fate it computes is a "
        "PROPOSAL rather than an act."),
    "tools/audit/gen_claude_md_finer_surface.py": (
        LIVE, "gen_claude_md_finer_surface.py, WHAT IT DOES of its module docstring; "
              "`build_readers()`, which re-scans the tracked tree through the imported measure; "
              "`render()`, which rebuilds the surface from both artifacts on every run",
        "LIVE. Its second claim is a live invariant nothing else asserts: the ruling surface the "
        "user reads still re-derives BYTE-IDENTICALLY from the two committed artifacts, so a "
        "hand-edited proposal cannot reach a ruling unnoticed. The reach half is re-scanned "
        "against the tracked tree at the pinned commit on every run. ★ WHAT IT DOES NOT ASSERT: "
        "that a naming is a dependency, or that the parser list is complete — the bound is the "
        "imported scan's own and is published on the surface itself."),
    "tools/audit/gen_claude_md_finer_archive.py": (
        LIVE, "gen_claude_md_finer_archive.py, THE STOPS of its module docstring; `build()`, which "
              "re-reads both live files on every run; `ruled_population()`, which re-derives the "
              "ruled archive and refused sets from the pinned artifact's own conflict evidence",
        "LIVE. Every one of its claims is re-answered against the tree AS IT STANDS on every run — "
        "each moved span byte-present in `CLAUDE_ARCHIVE.md` exactly once and absent from "
        "`CLAUDE.md`, each span the reading flagged and each span the ruling REFUSED still present "
        "at site exactly once and in the companion not at all. At this tree the safeguard returned "
        "STAY on both archive candidates, so nothing moved, and the flagged and refused directions "
        "are what the check is actually holding: a later act that archived a refused span would "
        "fail on the day it happened, which is the direction the ruled doubt default exists to "
        "protect. The population is DERIVED on every run rather than listed, and its own STOPs "
        "fire against the tree — an unverdicted archive candidate, a verdict naming a span the "
        "derivation does not carry, or a derived shape that disagrees with Ruling 1's own words. "
        "★ ONE HALF IS DELIBERATELY FIXED AND IT IS NOT A DATED READING EITHER: WHICH spans the "
        "ruling is about is a statement about the measurement the user ruled on, so it is read "
        "from that artifact's pinned commit rather than from a file later acts may legitimately "
        "edit. ★ WHAT IT DOES NOT ASSERT: that either flagged span is unarchivable, or that "
        "`CLAUDE.md` is small enough to read — the first is a later ruling's, the second is "
        "[[OI-370]]'s own subject."),
    "tools/audit/gen_retirement_census_movement.py": (
        LIVE, "gen_retirement_census_movement.py, THE THREE CLASSES paragraph of its module "
              "docstring; `movements()`, which re-derives every difference on every run; "
              "`Classifier.place()`, which tests each relation against the two trees",
        "LIVE. It asserts an invariant about the tree rather than reporting a dated reading: "
        "EVERY difference between the two censuses places in one of the three ruled classes, and "
        "a movement that places in none halts it. The population is re-derived on every run from "
        "the two readings and the two trees, so a relation that stops holding — a companion "
        "edited, a retired entry revived — fails on the day it happens. ★ ONE HALF IS "
        "DELIBERATELY FIXED AND IS NOT A DATED READING EITHER: WHICH two readings are compared is "
        "the subject of the comparison, so both are read from git objects at the commits they "
        "were measured at, and the check re-derives forever instead of going red the next time "
        "anything is written. ★ WHAT IT DOES NOT ASSERT: that a class is a movement's cause, or "
        "that a movement moves any verdict — a census crossing confers CANDIDACY only, which the "
        "artifact states of itself."),
    "tools/audit/gen_status_residue_move.py": (
        LIVE, "gen_status_residue_move.py, THE STOPS of its module docstring; `build()`, which "
              "re-reads both live files on every run; `candidates()`, which re-derives the "
              "population from the pinned decomposition and cross-checks it in both directions "
              "against the split-application artifact",
        "LIVE. All three of its claims are re-answered against the tree AS IT STANDS on every run "
        "— every moved entry still byte-present in `STATUS_ARCHIVE.md` exactly once, still absent "
        "from `STATUS.md`, and the ONE candidate the reading flagged still present at site. The "
        "third is what makes it more than a move record: a later act that archived the flagged "
        "span too would fail on the day it happened, which is the direction the ruled doubt "
        "default exists to protect. Its population is DERIVED on every run rather than listed, and "
        "the derivation's own STOPs fire against the tree: an unverdicted candidate, a verdict "
        "naming a span the decomposition does not carry, or the two acts failing to account for "
        "the file together. ★ ONE HALF IS DELIBERATELY FIXED AND IT IS NOT A DATED READING "
        "EITHER: WHICH spans are the residue, and their text, are statements about the file as the "
        "pinned measurement found it, so both are read from git objects rather than from a file "
        "that legitimately grows by every later batch's entries — the same epoch pattern "
        "`gen_status_batch_bound.py` and `gen_status_archive_pass.py` use. ★ WHAT IT DOES NOT "
        "ASSERT: that every moved entry's substance is carried elsewhere in full. What it "
        "establishes per entry is narrower and is what its reading test asks — no rule, STOP, "
        "prohibition or live caveat whose ONLY home is that entry."),
    "tools/audit/gen_governing_surface_split.py": (
        LIVE, "gen_governing_surface_split.py, THE STOPS of its module docstring; `plan_for()`, "
              "which re-locates every moved span in the pre-act blob and re-checks the arithmetic; "
              "`build()`, which re-reads both live files on every run",
        "LIVE. Two of its three claims are re-answered against the tree AS IT STANDS on every run "
        "— every archived span still byte-present in its companion exactly once, and still absent "
        "from its parent — so a later edit that put an archived span back into a must-read, or that "
        "quietly dropped one from an archive, fails on the day it happens. Its STOPs are live "
        "demands too: they re-derive the population from the pinned decomposition and halt if a "
        "span reaches an archive class with no authored reading verdict, or if a verdict names a "
        "span the decomposition no longer carries. ★ ONE HALF IS DELIBERATELY FIXED AND IT IS NOT "
        "A DATED READING EITHER: the pre-act blob and the register's home anchors are read from "
        "the git objects at the commit the act was performed on top of, because moved-plus-kept "
        "accounting for that blob is a fact about ONE MOMENT — checked at that moment's own object "
        "(D-646, the epoch pattern) rather than against a file that legitimately grows, which is "
        "the OI-344 shape avoided by construction and the precedent "
        "`gen_status_archive_pass.py` already sets. ★ WHAT IT DOES NOT ASSERT: that a span left at "
        "site is operative, or that a span moved is noise — the reading verdicts are authored "
        "judgments made by reading each span, published beside the spans they moved."),
    "tools/audit/gen_census_movement_classification.py": (
        LIVE, "gen_census_movement_classification.py, the THREE CATEGORIES and THE STOPS of its "
              "module docstring; `build()`, which re-runs the citation scan at both states and "
              "classes every difference",
        "LIVE. Both sides of its comparison are re-computed on every run: the earlier state from "
        "the git objects at a named commit, the later one from the governing record AS IT STANDS. "
        "So an edit that removes a document's last naming from `CLAUDE.md` tomorrow moves its "
        "output tomorrow, and the classification either places that movement in one of the three "
        "ruled categories or STOPS. That is a demand about today's record, not a dated reading of "
        "it. ★ ONE HALF IS DELIBERATELY FIXED AND IT IS NOT A DATED READING EITHER: the BEFORE "
        "commit is the state the movement is measured against, and a comparison whose baseline "
        "moved would measure nothing. It is named in the tool rather than resolved from a branch "
        "tip, because a branch read is not trusted for what is current (D-253). ★ WHAT IT DOES "
        "NOT ASSERT: that a moved document is worth retiring, or that nothing depends on it — the "
        "citation scan sees the governing record only, which is the bound the census publishes of "
        "itself and this tool repeats rather than quietly drops."),
    "tools/audit/gen_discard_reach_split.py": (
        LIVE, "gen_discard_reach_split.py, the `★ WHERE THE POPULATION COMES FROM` and `THE "
              "VERDICT RULE` paragraphs of its module docstring and its `THE STOPS` list; "
              "`measured_population()`, which parses the population out of the committed report's "
              "own captured run; `explain()`, which places each red against the committed plan",
        "LIVE. Its POPULATION is a measurement and is imported rather than re-taken — parsed on "
        "every run out of the `[FAIL]` lines of the committed report that recorded it, read at the "
        "commit the artifact records — but everything it asserts ABOUT that population is "
        "re-derived at HEAD and becomes false the moment the record moves: every verdict comes "
        "from the import graph among the checks as they stand, every stated purpose is quoted from "
        "the check's own module docstring and from the guard set's own authored invocation table "
        "(imported, never restated, #6), and every red's explanation is derived from the committed "
        "discard plan together with the decisions register's home data. Its STOPs are demands of "
        "the same kind: the ruling's sentences must still be in its ruling record; a `[FAIL]` "
        "block that is missing, empty, or names a check the tree no longer carries halts it rather "
        "than letting the population shrink to what still parses; a member the verdict rule cannot "
        "place halts it; and a STANDING member whose red the enumerated-movement bound cannot "
        "explain halts it, which is the ruling's own STOP and the one that fired for real on this "
        "tool's first run. ★ WHAT IT DOES NOT ASSERT, and its own artifact says so: that a "
        "SUPERSEDED verdict says anything about whether the superseded phase 1's obligations were "
        "discharged — the ruling states in terms that historical status asserts nothing of the "
        "kind — and that the population has been re-confirmed at the applied tree, which is owed "
        "at the act and not before it."),

    # ---- tools/audit/decisions — the register's own checks -----------------------------------
    "tools/audit/decisions/gen_retired_subject_moves.py": (
        LIVE, "gen_retired_subject_moves.py, the two MEMBERSHIP RULES and THE STOPS of its module "
              "docstring; `partition()`, which applies both directions; `section_kind()`, which "
              "imports the home classifier's own move derivation",
        "LIVE. Every value it publishes is re-derived at HEAD from the decisions register's data "
        "file as it stands and from the five authored tables as they stand: which judgment watches "
        "a live subject, which has followed its subject into the retired-entries block, and which "
        "entries emptied each moved document or section. Nothing in it is dated. A later act that "
        "retires an entry, revives one, or writes a new authored judgment SHOULD move its output, "
        "and the check is what makes that movement visible — which is the R4 test in the form the "
        "ruling states it. ★ WHAT IT DOES NOT ASSERT, and its own artifact says so: that a moved "
        "judgment is RIGHT. A retired subject is a provenance outcome, and the judgment is carried "
        "whole, unread and unre-graded (#12). ★ ONE LIMIT DECLARED RATHER THAN GLOSSED: a "
        "judgment already on a retired side for an EARLIER act's reason — the re-homing waves — is "
        "left where that act's own record put it and is not re-derived here, because this tool is "
        "not the authority for retirements it did not perform. What it does still ask of every one "
        "of them is the direction that must never go unnoticed: that the subject has not become "
        "live again."),
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
