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

    # ---- tools/audit/decisions — the register's own checks -----------------------------------
    "tools/audit/decisions/gen_decisions_register.py": (
        LIVE, "gen_decisions_register.py:11-16",
        "The register is GENERATED from its data, and `--check` regenerates and diffs ALL emitted "
        "files. \"The rendered register matches its source data\" is true or false of the tree at "
        "any moment, and an edit to either side is caught at once."),
    "tools/audit/decisions/gen_cluster_dispositions.py": (
        LIVE, "gen_cluster_dispositions.py:28-30",
        "Both invocations are live. `--verify` locates every backbone verbatim IN THE FILE IT IS "
        "CITED TO and checks the cited START LINE — the drift check every home-document edit "
        "exercises, this wave included. `--check` re-derives the dispositions from the current "
        "backbone and proves the bijection over all clusters."),
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
        LIVE, "gen_reads5_repack.py:9-13, :29-35",
        "It reads the REGISTERED regime verbatim and never regenerates it, and imports the packing "
        "rule rather than copying it. Its inputs are frozen artifacts, so its --check is a live "
        "assertion that the re-pack still follows from the registration — and it passes and can "
        "keep passing."),
    "tools/audit/decisions/gen_reads1_yield.py": (
        LIVE, "gen_reads1_yield.py:11-21",
        "Each wave's yield artifact records a measurement, but its --check asserts something LIVE "
        "and worth guarding: that every entry the wave names is STILL IN THE REGISTER AT THE HOME "
        "IT RECORDS. An entry silently vanishing or changing home is a real defect, and this is "
        "what would catch it. Its other inputs are frozen, so it can pass indefinitely — and does."),
    "tools/audit/decisions/gen_reads2_yield.py": (
        LIVE, "gen_reads2_yield.py (the same shape as wave 1's); guard_state.json → runs",
        "Same verdict, same ground: the entries it names must still be in the register at their "
        "recorded homes, and its running read count must still derive from the regime's partition "
        "plus the earlier waves. It passes at the committed tree."),
    "tools/audit/decisions/gen_reads3_yield.py": (
        LIVE, "gen_reads3_yield.py (the same shape as wave 1's); guard_state.json → runs",
        "Same verdict, same ground. It passes at the committed tree."),
    "tools/audit/decisions/gen_reads4_yield.py": (
        LIVE, "gen_reads4_yield.py (the same shape as wave 1's); guard_state.json → runs",
        "Same verdict, same ground. It passes at the committed tree."),
    "tools/audit/decisions/gen_reads5_yield.py": (
        LIVE, "gen_reads5_yield.py:11-15",
        "Same verdict, same ground, and it additionally reads its bands off the re-pack artifact "
        "rather than recomputing them. It passes at the committed tree."),
    "tools/audit/decisions/gen_reads6_yield.py": (
        LIVE, "gen_reads6_yield.py:14-18",
        "Same verdict and same ground as the five before it — the entries it names must still be "
        "in the register at their recorded homes — with one addition that is itself a live "
        "assertion: it DERIVES the owed remainder from the regime's partition plus every completed "
        "wave's own count, so the claim that the owed set is empty is re-checked on every run "
        "rather than recorded once."),
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
