#!/usr/bin/env python3
"""D-639's test applied to the OPEN DOCUMENTATION ROWS CLASSED APPARATUS — the second application.

THE RULING is the same one the first application reads, and it is read from the same place by the
same locator: `gen_true_half_reach.py` owns the anchor, the three worked examples and the fallback,
and this file IMPORTS them rather than restating them (#6).  What differs is the POPULATION.  The
first application graded the three DOCUMENTS `OPEN_ITEMS.md` OI-332 carries; this grades the open
apparatus-classed rows the phase-1 finish line names as the one item D-639's test has not decided.

WHAT THIS FILE DOES.  Per row: does the document's account of ITSELF change how its analysis content
is read?  A verdict names the worked example it matched, or names none — and a row matching none is a
row the test did not decide, where **D-639's fallback (1A) governs: the doc-sync half reaches only
the account of the ANALYSIS.**  The ruling's own words are that a session which finds itself arguing a
case applies the fallback and says so rather than stretching the test, and this file says so per row.

HOW THE FALLBACK IS MADE MECHANICAL RATHER THAN A SECOND JUDGMENT.  Applying (1A) to a row needs one
authored bit and nothing else: does the row assert that a document STATES SOMETHING FALSE ABOUT THE
SYSTEM — its behaviour, its inputs, its parameters, or what a layer produces?  The verdict is then
DERIVED from that bit, and a verdict disagreeing with it is a STOP.  So a session cannot author a
fallback verdict and a ground that point different ways.

WHAT IS AUTHORED AND WHAT IS DERIVED.
  authored : per row, the worked example it matches (or none), the one fallback bit where no example
             matched, the verdict, the reason, and a short quote from the row's own detail file.
  derived  : the POPULATION, read at the artifact that owns it; the ruling's text, located by anchor
             in `CLAUDE.md`; whether the fallback was reached, per row and in total; the agreement
             between each verdict and the thing that decides it; and every count.

THE STOPS.  The run refuses if the authored set and the derived population disagree in either
direction; if a verdict names a worked example the ruling does not state; if a verdict disagrees with
the worked example it names or with its own fallback bit; or if a row's quote is not in that row's
detail file.

WHAT IT DOES NOT DO.  It moves no gate verdict.  A non-gating verdict is DERIVED from the apparatus
cut and never hand-added, so the consequence a row put IN carries for its gate classification is
REPORTED here and left to the user, exactly as the first application reported its own.

Usage:
  python tools/audit/decisions/gen_true_half_reach_rows.py           # write the artifact
  python tools/audit/decisions/gen_true_half_reach_rows.py --check   # re-derive, exit 1 on drift
"""
from __future__ import annotations

import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
OPEN_ITEMS_DIR = os.path.join(ROOT, "open_items")
INVENTORY = os.path.join(ROOT, "tools", "audit", "phase1_completion_inventory.json")
OUT = os.path.join(HERE, "true_half_reach_rows.json")

sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))
from output_encoding import use_utf8_output          # noqa: E402  (path set above)

# #6 — the ruling, its three worked examples and the locator have ONE home, which is the first
# application. This file reads them from there and never restates them.
from gen_true_half_reach import WORKED_EXAMPLES, locate_ruling   # noqa: E402

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

FALLBACK_BIT = "the_row_asserts_a_document_states_something_false_about_the_system"

# ---------------------------------------------------------------------------
# AUTHORED — one verdict per row of the derived population. Each carries a quote from the row's own
# detail file, checked to be present, so a verdict cannot depend on a reading of a row nobody opened.
# ---------------------------------------------------------------------------
VERDICTS = [
    {
        "row": "OI-205",
        "anchor_quote": "render + human/LLM context capacity",
        "what_the_row_records": (
            "Two governing documents have grown past comfortable human and LLM working size; half "
            "(a) is executed and half (b) — the ARCHITECTURE.md restructure — is a decision surface "
            "owed after the retirement map's deletions settle."
        ),
        "matched_worked_example": None,
        FALLBACK_BIT: False,
        "verdict": "OUT — the doc-sync half does not reach it",
        "why": (
            "It matches none of the three worked examples, so the test does not decide it and the "
            "fallback governs. Its subject is a document's SIZE and shape, which is not an account "
            "of anything: the documents state nothing false about the system, and a restructure "
            "moves no statement in them. Under (1A) the half reaches only the account of the "
            "analysis, and this row makes no claim about the analysis at all."
        ),
    },
    {
        "row": "OI-229",
        "anchor_quote": "The existing tree is **NOT renamed unilaterally.**",
        "what_the_row_records": (
            "The music-theory terminology convention binds new writing; the cleanup over the "
            "existing tree is a scoped decision surface whose order the user has since ruled, and "
            "the row stays open because the cleanup is not done."
        ),
        "matched_worked_example": None,
        FALLBACK_BIT: False,
        "verdict": "OUT — the doc-sync half does not reach it",
        "why": (
            "No worked example matches, so the fallback governs. A reserved-word collision makes a "
            "sentence AMBIGUOUS; it does not make it false. The row asserts no statement about the "
            "system that is untrue at HEAD — it records a convention and an owed cleanup — so under "
            "(1A) the half does not reach it. The convention's own enforcement is the per-session "
            "self-check, which is a separate obligation and is not touched here."
        ),
    },
    {
        "row": "OI-233",
        "anchor_quote": "the rename pass is NOT done and stays owed",
        "what_the_row_records": (
            "A ratified ban on a bare word was recorded as executed through every layer "
            "specification and was not; the FALSE CLAIM was corrected at the document on "
            "2026-08-02, and what remains owed is the rename pass itself."
        ),
        "matched_worked_example": None,
        FALLBACK_BIT: False,
        "verdict": "OUT — the doc-sync half does not reach it",
        "why": (
            "Its false half is already corrected: the specification now records what the 2026-07-03 "
            "pass actually covered and says the pass over this document is not executed, which the "
            "row's own dated remark states. What is left is a terminology pass the user's standing "
            "ruling defers, and an ambiguous word is not a false statement. Had the execution claim "
            "still stood it would have belonged to the first worked example's family, and it is "
            "recorded here that it does not still stand rather than that it never did."
        ),
    },
    {
        "row": "OI-280",
        "anchor_quote": "It is a **documentation gap only**.",
        "what_the_row_records": (
            "One document uses the same private label for two unrelated rulings, so a reader "
            "looking the label up finds the wrong one; both rulings are live and correct."
        ),
        "matched_worked_example": None,
        FALLBACK_BIT: False,
        "verdict": "OUT — the doc-sync half does not reach it",
        "why": (
            "The third worked example names a stale ANCHOR, and a colliding private label is close "
            "to it without being it — which is exactly the case the ruling says a session must not "
            "stretch, so the fallback is applied and said. Under (1A): the row's own words are that "
            "both decisions' content is not in doubt, so no statement about the system is false; "
            "what is wrong is which of two correct rules a lookup lands on."
        ),
    },
    {
        "row": "OI-281",
        "anchor_quote": "a question about the fifth home case's criterion",
        "what_the_row_records": (
            "Whether a delegation pointer confers contract-home standing on a document whose own "
            "banner says draft — a question about the decisions register's home criterion, which "
            "later rulings answered by making the banner expressly not the test."
        ),
        "matched_worked_example": None,
        FALLBACK_BIT: False,
        "verdict": "OUT — the doc-sync half does not reach it",
        "why": (
            "No worked example matches. Its subject is a criterion for classifying a home, not a "
            "statement any document makes about the system; and the banner it turns on has since "
            "been ruled out of the test altogether, so even the document's account of itself no "
            "longer decides anything. Under (1A) the half does not reach it."
        ),
    },
    # OI-282's verdict moved to RETIRED_VERDICTS on 2026-08-11, when the row closed.
    {
        "row": "OI-290",
        "anchor_quote": "§8c should be SPLIT so that the rules and the",
        "what_the_row_records": (
            "A rule-stating section of the corpus census also holds a findings table, and most of "
            "the entries admitted through it are rows of that table; the remedy is to re-section "
            "the document so rules and findings are not one block."
        ),
        "matched_worked_example": None,
        FALLBACK_BIT: False,
        "verdict": "OUT — the doc-sync half does not reach it",
        "why": (
            "No worked example matches. The row's own words are that the section states three "
            "binding rules, that the delegation reaches it by name, that the eleven entries are "
            "correctly homed and that the section's content is not in doubt — so nothing in it is "
            "false. What is owed is a re-sectioning, which under (1A) the half does not reach."
        ),
    },
    {
        "row": "OI-296",
        "anchor_quote": "Sweep for ratified rules parked in tracking sections",
        "what_the_row_records": (
            "A sweep that has not run, for ratified rules recorded in tracking sections rather "
            "than where the rule belongs; its dated remarks record four instances found by other "
            "work rather than by looking for the class."
        ),
        "matched_worked_example": None,
        FALLBACK_BIT: False,
        "verdict": "OUT — the doc-sync half does not reach it",
        "why": (
            "No worked example matches: the row's subject is a search that has not been performed, "
            "not any document's account of itself. Under (1A) it asserts no statement about the "
            "system that is false — the rules it names are correctly recorded, only in weaker "
            "places than they belong. Recorded rather than smoothed over: its fourth dated remark "
            "observes that a document the canonical specification marks superseded is nonetheless "
            "the only home of measured values, and calls that a filing decision rather than a "
            "session's; that observation is the row's evidence and not its subject, and grading it "
            "would grade something the row explicitly does not carry."
        ),
    },
    # OI-298's verdict moved to RETIRED_VERDICTS on 2026-08-11, when the user's Ruling 53 corrected
    # its status cell's opening token and the row left the open population.
    {
        "row": "OI-299",
        "anchor_quote": "this is an apparatus row — its subject is",
        "what_the_row_records": (
            "The index rows restate their detail files, so a correction reached one copy and not "
            "the other for five waves; the remedy is one redesign of the index row's shape with "
            "its own establishment run."
        ),
        "matched_worked_example": None,
        FALLBACK_BIT: False,
        "verdict": "OUT — the doc-sync half does not reach it",
        "why": (
            "No worked example matches: the subject is the SHAPE of a tracking surface, which the "
            "row says of itself. Under (1A) the half does not reach it. The establishment run the "
            "redesign ends in does gate, by the non-gating declaration's own clause, and that is a "
            "statement about what a stage waits on rather than about the doc-sync half — the two "
            "tests D-639 keeps apart."
        ),
    },
    {
        "row": "OI-317",
        "anchor_quote": "the banner is an **instruction to a future session**",
        "what_the_row_records": (
            "A design document's banner says it is uncommitted and under a commit hold; it is "
            "committed at HEAD, and no ratification addendum is named."
        ),
        "matched_worked_example": None,
        FALLBACK_BIT: False,
        "verdict": "OUT — the doc-sync half does not reach it",
        "why": (
            "It is close to the first worked example and is not it: that example is a banner over a "
            "MECHANISM, and the first application's reversal of its sign stayed on that subject. "
            "This banner is false about the document's own repository standing and carries a stale "
            "standing instruction — a different subject — so the test does not decide it and the "
            "fallback is applied and said. Under (1A) the half reaches only the account of the "
            "analysis, and the record has already put that half of this document elsewhere: its "
            "substantive staleness is [[OI-315]], which gates, while this row's own text says the "
            "document's finding is corroborated three ways and yielded no register entry."
        ),
    },
    # OI-318's verdict moved to RETIRED_VERDICTS on 2026-08-11, when the row closed.
    {
        "row": "OI-338",
        "anchor_quote": "The subject is an **authored prose field inside an audit artifact**.",
        "what_the_row_records": (
            "The phase-1 completion inventory publishes as an open question one the user ruled as "
            "D-639, because its clause quote is derived and moves with HEAD while its criteria are "
            "an authored constant that did not."
        ),
        "matched_worked_example": None,
        FALLBACK_BIT: False,
        "verdict": "OUT — the doc-sync half does not reach it",
        "why": (
            "No worked example matches. The stale field IS false — it says a question is the "
            "user's to settle where the user has settled it — but it is false about a RULING's "
            "standing, not about the system, and the row's own reading records that it bears on no "
            "analysis behaviour, no analysis input and no measurement tool. Under (1A) the half "
            "does not reach it. Worth a reader's attention rather than hidden: the question that "
            "field reports as open is the very ruling this derivation applies."
        ),
    },
    {
        "row": "OI-346",
        "anchor_quote": "it changes what a reader of those constants is told about how far",
        "what_the_row_records": (
            "A ratified verifiability amendment's RULE half is written into the specification and "
            "its APPLICATION half is not: the Jazz preset constants and the idioms no ground truth "
            "calibrates carry no unvalidated mark and name no validating corpus."
        ),
        "matched_worked_example": None,
        FALLBACK_BIT: False,
        "verdict": "OUT — the doc-sync half does not reach it",
        "why": (
            "No worked example matches, so the fallback governs, and it turns on the difference "
            "between an omission and a falsity: the specification states nothing untrue about "
            "those constants, it withholds a qualification a ratified rule requires. Under (1A) "
            "the half reaches a document that STATES something false, which this does not. **The "
            "counter-reading is recorded rather than dropped (#12):** an unmarked constant can be "
            "read as an implicit claim that it is established, which is what #19 exists against — "
            "on that reading the row would be reached. It is not adopted, because reading an "
            "omission as a statement is the stretch the ruling's fallback exists to refuse, and "
            "because the row's own words are that nothing the analysis computes changes."
        ),
    },
    {
        "row": "OI-347",
        "anchor_quote": "**NOT in doubt:** the primitive itself, its behaviour, and the rule",
        "what_the_row_records": (
            "The two Layer-1.5 primitives are sited in different sections of the canonical "
            "architecture document and only one siting states its reason; the second primitive is "
            "named in three places and specified in none."
        ),
        "matched_worked_example": None,
        FALLBACK_BIT: False,
        "verdict": "OUT — the doc-sync half does not reach it",
        "why": (
            "No worked example matches. The row is a siting question plus an open question about "
            "whether one list is incomplete — an omission the row itself puts under 'in doubt' "
            "rather than establishes. Under (1A) the half reaches a false statement about the "
            "system, and the row's own words are that the primitive, its behaviour and the rule "
            "recorded about it are not in doubt and that no analysis behaviour or measurement is "
            "affected."
        ),
    },
    {
        "row": "OI-46",
        "anchor_quote": "Audit §3/§4 tables contradict §3.1 build-status",
        "what_the_row_records": (
            "Inside one audit, the queued-fix tables and the build-status section disagree about "
            "the stage two proposed structural fixes belong to."
        ),
        "matched_worked_example": None,
        FALLBACK_BIT: False,
        "verdict": "OUT — the doc-sync half does not reach it",
        "why": (
            "No worked example matches, and the row is too terse to decide mechanically: it names "
            "no document, and it does not establish which of the two sides is the stale one, so "
            "reaching a verdict through a worked example would mean adjudicating two sections — "
            "the judgment the fallback exists to refuse. Under (1A): the two items in dispute are "
            "proposed REFACTORS and what disagrees is which stage they belong to, so a reader is "
            "misled about the work plan rather than about the system's behaviour, inputs, "
            "parameters or what any layer produces."
        ),
    },
    # OI-47's verdict moved to RETIRED_VERDICTS on 2026-08-11, when the row closed.
    {
        "row": "OI-48",
        "anchor_quote": "the file EXISTS — it is a Claude Code MEMORY",
        "what_the_row_records": (
            "Two live documents reference a file that is not in the repository; it exists as a "
            "session memory, so nothing is lost, and what dangles is the repository-internal "
            "reference. The code substance rides a separate row."
        ),
        "matched_worked_example": "stale anchor or a formatting artifact",
        FALLBACK_BIT: False,
        "verdict": "OUT — the doc-sync half does not reach it",
        "why": (
            "It is the third worked example: a reference that does not resolve. The ruling's own "
            "ground fits it exactly — a coordinate that has drifted misleads nobody about the "
            "analysis — and the row establishes that in its own words: nothing is lost, and the "
            "code substance it points at is carried by another row. What is owed is a re-pointing."
        ),
    },
    {
        "row": "OI-49",
        "anchor_quote": "D-L3a \"closed\" (fitter) vs \"remains\" (roadmap G1)",
        "what_the_row_records": (
            "Two documents disagree about whether one design item is closed or still owed."
        ),
        "matched_worked_example": None,
        FALLBACK_BIT: False,
        "verdict": "OUT — the doc-sync half does not reach it",
        "why": (
            "No worked example matches, and the row does not establish which side is stale, so a "
            "verdict through an example would mean adjudicating two documents. Under (1A): what "
            "the two disagree about is the STANDING of a design item — closed or still owed — "
            "which is the account of the work rather than of the system's behaviour, inputs, "
            "parameters or what a layer produces."
        ),
    },
    {
        "row": "OI-50",
        "anchor_quote": "FQ-2 \"decided at Stage 2\" (arc plan) vs \"enumerated-not-resolved\" (L5-engage)",
        "what_the_row_records": (
            "Two documents disagree about whether one open question was decided or merely "
            "enumerated."
        ),
        "matched_worked_example": None,
        FALLBACK_BIT: False,
        "verdict": "OUT — the doc-sync half does not reach it",
        "why": (
            "The same shape as its sibling and the same treatment: no worked example matches, the "
            "row does not say which side is stale, and what is in dispute is whether a question "
            "was decided — the account of the work. Under (1A) the half does not reach it."
        ),
    },
    {
        "row": "OI-99",
        "anchor_quote": "Doc-sync only, no code effect.",
        "what_the_row_records": (
            "Two production comments cite a provenance document that does not exist in the "
            "repository; the row's own words are that it is doc-sync only with no code effect."
        ),
        "matched_worked_example": "stale anchor or a formatting artifact",
        FALLBACK_BIT: False,
        "verdict": "OUT — the doc-sync half does not reach it",
        "why": (
            "It is the third worked example, in code comments rather than in prose: a citation "
            "that does not resolve. Nothing a reader concludes about the analysis changes — the "
            "row says so in terms — and the owed act is to re-point the citation or drop it at the "
            "next touch of that file."
        ),
    },
]

# ---------------------------------------------------------------------------
# RETIRED — a verdict whose ROW has left the derived population, moved here WHOLE rather than
# deleted (#12, D-648: authored-input maintenance, not a mechanism change). It is carried into the
# artifact as history and COUNTED NOWHERE. A retired verdict naming a row the derivation reaches
# again is a STOP in the other direction: a reading made of a row as it stood is not evidence about
# a row that has since moved, so it is RE-READ rather than restored.
# ---------------------------------------------------------------------------
RETIRED_VERDICTS = [
    {
        "row": "OI-47",
        "anchor_quote": "Their figures are superseded by the governing robust-unit stop",
        "what_the_row_records": (
            "Four submission-era sections of the status document contradict the governing "
            "documents; the triage half is discharged and the banner half — marking those sections "
            "historical — remains owed."
        ),
        "matched_worked_example": None,
        FALLBACK_BIT: True,
        "verdict": "IN — the doc-sync half reaches it",
        "why": (
            "The second worked example names a superseded PLAN and these are superseded status "
            "sections, so the match is not literal and the fallback is applied and said. It "
            "reaches: the sections carry MEASURED VALUES about the analysis that the governing "
            "hard stop supersedes, so a reader of the current-state section is told the system's "
            "error counts are values no measurement now supports. That is a document stating "
            "something false about the system, which (1A) reaches. What is owed is the row's own "
            "stated act — annotate, do not rewrite history."
        ),
        "why_it_is_retired": (
            "LEFT THE POPULATION 2026-08-11 — the row RESOLVED "
            "(`cc_instruction_status_touch_and_oi141_premise_repin.md` Task 2) when the banner "
            "half was performed at the objects, all four sections carrying a dated HISTORICAL "
            "banner with nothing below any banner edited. THE VERDICT WAS CORRECT WHILE IT STOOD "
            "and is kept whole; it is retired because the row closed, never because it was wrong. "
            "★ IT IS THE DERIVATION'S ONLY IN VERDICT SO FAR AND THE ONE THE USER APPLIED: Ruling "
            "56 moved it to the gating side on this ground, and the closing act then wrote exactly "
            "what the verdict said was missing — that those acceptance numbers and hard stops are "
            "superseded in whole. ★ AND IT SURVIVED A DEPARTURE THE VERDICT DID NOT PREDICT: the "
            "four sections were not in the file the row's citations named, the 2026-07-18 doc "
            "split having moved them into the status archive, so the act was performed where they "
            "live. The verdict was written against what the sections SAY, which is why the change "
            "of file left it standing."
        ),
    },
    {
        "row": "OI-282",
        "anchor_quote": "**no annotation of any of this**",
        "what_the_row_records": (
            "A document titled as planned future work presents both halves of its subject as "
            "undelivered; one half was delivered and user-ratified the following day, and the "
            "document carries no annotation of it."
        ),
        "matched_worked_example": "missing supersession note on a superseded plan",
        FALLBACK_BIT: False,
        "verdict": "IN — the doc-sync half reaches it",
        "why": (
            "It is the ruling's second worked example word for word: the document IS a plan, half "
            "of it is superseded by a ratified delivery, and it carries no annotation saying so. "
            "The "
            "consequence is the one the example is about — a reader sent there by two live "
            "specifications is told the categories are still to be discovered when they are "
            "discovered, ratified and compiled in, so the same text is read as two different "
            "things depending on a fact the document does not carry. It would also be reached "
            "under the fallback, since that statement is false about the system at HEAD; the "
            "worked example decides it and the fallback is not needed."
        ),
        "why_it_is_retired": (
            "LEFT THE POPULATION 2026-08-11 — the row RESOLVED "
            "(`cc_instruction_return_continuation_14.md` Task 3) by the annotation being written. "
            "THE VERDICT WAS CORRECT WHILE IT STOOD and is kept whole; it is retired because the "
            "row closed, never because it was wrong. ★ IT IS THE CLEANEST CONFIRMATION THIS "
            "DERIVATION HAS: it matched a worked example word for word, needed no fallback, and "
            "the act performed was exactly the annotation the example prescribes."
        ),
    },
    {
        "row": "OI-318",
        "anchor_quote": "grouping layer segments melodic phrases, which is the one thing",
        "what_the_row_records": (
            "Two label defects in the canonical architecture document: its Layer-6 paragraph uses "
            "the bare word a ratified rename reserved for a different object, and one section "
            "number is used twice."
        ),
        "matched_worked_example": None,
        FALLBACK_BIT: True,
        "verdict": "IN — the doc-sync half reaches it",
        "why": (
            "The row is mixed and no worked example decides it, so the fallback governs — and it "
            "reaches the row through its first half. That half is not the document's account of "
            "ITSELF at all: the paragraph tells a reader what a LAYER PRODUCES, and the row's own "
            "words are that a reader of it alone is told the grouping layer segments melodic "
            "phrases, which the ratified design exists to deny. That is a specification stating "
            "something false about the system, which is the doc-sync half's own subject. The "
            "second half — one section number used twice — is a numbering artifact and would be "
            "OUT on its own; it is recorded so the row is not read as gating on both."
        ),
        "why_it_is_retired": (
            "LEFT THE POPULATION 2026-08-11 — the row RESOLVED "
            "(`cc_instruction_return_continuation_14.md` Task 3), both items corrected. THE "
            "VERDICT WAS CORRECT WHILE IT STOOD and is kept whole; it is retired because the row "
            "closed. ★ ITS SPLIT SURVIVED THE ACT INTACT, which is the useful half: the paragraph "
            "was corrected as a statement about what a layer produces, and the duplicated section "
            "number was renumbered as the numbering artifact this verdict said it was — the two "
            "halves were treated differently in the same act, which is what the verdict asked for."
        ),
    },
    {
        "row": "OI-298",
        "anchor_quote": "the two things the row said would not be done were done, in the order the user ruled",
        "what_the_row_records": (
            "A user-directed clause leaned on an unratified draft for an enumeration it requires; "
            "the user ruled the scope, the draft was corrected and ratified, and the clause now "
            "points at the ratified home."
        ),
        "matched_worked_example": None,
        FALLBACK_BIT: False,
        "verdict": "OUT — the doc-sync half does not reach it",
        "why": (
            "No worked example matches. The row's subject — a governing clause pointing at "
            "unratified content — is discharged by its own dated remark, and the clause names no "
            "subjects of its own at HEAD. Under (1A) nothing here is a false statement about the "
            "system. **Read beside [[OI-367]]:** this row's status cell opens with an open-state "
            "token while its own text records a closure with provenance, so it is counted open by "
            "every derivation over the index. That is why it is in this population at all, and the "
            "verdict is the same whichever way its state finally falls."
        ),
        "why_it_is_retired": (
            "LEFT THE POPULATION 2026-08-11. The user's Ruling 53 of "
            "`cowork_rulings_2026_08_11_eleventh_stop.md` corrected this row's status-cell opening "
            "token PER THE CELL'S OWN WORDS, so the row is now counted RESOLVED and is no longer an "
            "open apparatus-classed row. THE VERDICT WAS CORRECT WHILE IT STOOD and is kept whole: "
            "its own text had already named the reading that turned out to be right — that the row "
            "reads open only because of its opening token, and that the verdict is the same "
            "whichever way its state finally falls — so nothing here is withdrawn. It is retired "
            "because the row left the derived set, never because it was wrong."
        ),
    },
]


def read(path: str) -> str:
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def derived_population() -> list:
    """The apparatus-classed rows this derivation grades — the cut BEFORE Ruling 56 is applied.

    WHY THE *BEFORE* CUT AND NOT THE LIVE ONE, which is the whole of why this function has a
    docstring. The user's Ruling 56 (2026-08-11) applies this derivation's IN verdicts by moving
    those rows to the gating side. Read against the LIVE non-gating cut, this derivation's own
    result would remove its own graded rows from its own population — its both-ways STOP would fire,
    retiring them would empty the IN set, and the application would reverse itself on the next
    regeneration. The BEFORE cut is invariant under the application, so the population is stable and
    the fixed point is the one the ruling intends. It is still DERIVED, at the same artifact, and
    the two cuts differ by exactly the rows that artifact records as moved.
    """
    inv = json.loads(read(INVENTORY))
    try:
        return list(inv["the_gating_split"]["non_gating_before_the_ruling_56_application"]["ids"])
    except KeyError as exc:                                       # pragma: no cover - a STOP
        raise SystemExit(
            "STOP: the completion inventory does not carry "
            "`the_gating_split.non_gating_before_the_ruling_56_application.ids`, which is the "
            f"population this derivation grades ({exc}). It is NOT read from the live non-gating "
            "cut, because that cut moves when this derivation's own verdicts are applied."
        )


def build() -> dict:
    ruling = locate_ruling()
    population = derived_population()

    authored = [v["row"] for v in VERDICTS]
    if len(set(authored)) != len(authored):
        raise SystemExit("STOP: a row is graded twice.")
    retired_ids = [v["row"] for v in RETIRED_VERDICTS]
    if set(retired_ids) & set(authored):
        raise SystemExit("STOP: a row is both graded and retired: "
                         + ", ".join(sorted(set(retired_ids) & set(authored))))
    resurrected = [r for r in retired_ids if r in population]
    if resurrected:
        raise SystemExit(
            "STOP: a RETIRED verdict names a row the derivation reaches again: "
            + ", ".join(resurrected) + ". A reading made of a row as it stood is not evidence "
            "about a row that has since moved — it is RE-READ and re-authored, never restored."
        )
    missing = [r for r in population if r not in authored]
    extra = [r for r in authored if r not in population]
    if missing or extra:
        raise SystemExit(
            "STOP: the authored verdicts and the derived population disagree. "
            f"Derived but ungraded: {missing}. Graded but not in the derived population: {extra}. "
            "The population is the finish line's own and may not be authored beside it."
        )

    for v in VERDICTS:
        detail = os.path.join(OPEN_ITEMS_DIR, f"{v['row']}.md")
        if not os.path.exists(detail):
            raise SystemExit(f"STOP: {v['row']} has no detail file at {detail}.")
        if v["anchor_quote"] not in read(detail):
            raise SystemExit(
                f"STOP: {v['row']}'s quoted words are not in its own detail file — a verdict may "
                "not rest on a reading of a row nobody opened."
            )
        example = v["matched_worked_example"]
        if example is not None and example not in WORKED_EXAMPLES:
            raise SystemExit(
                f"STOP: {v['row']} names a worked example the ruling does not state: {example!r}"
            )
        if example is not None:
            if not v["verdict"].startswith(WORKED_EXAMPLES[example]):
                raise SystemExit(
                    f"STOP: {v['row']} matches the worked example {example!r}, which the ruling "
                    f"puts {WORKED_EXAMPLES[example]}, and its verdict says otherwise."
                )
        else:
            wanted = "IN" if v[FALLBACK_BIT] else "OUT"
            if not v["verdict"].startswith(wanted):
                raise SystemExit(
                    f"STOP: {v['row']}'s fallback verdict disagrees with its own ground. The "
                    f"authored bit puts it {wanted}."
                )

    undecided = [v["row"] for v in VERDICTS if v["matched_worked_example"] is None]
    inside = [v["row"] for v in VERDICTS if v["verdict"].startswith("IN")]
    outside = [v["row"] for v in VERDICTS if v["verdict"].startswith("OUT")]
    by_example = {}
    for name in WORKED_EXAMPLES:
        by_example[name] = [v["row"] for v in VERDICTS if v["matched_worked_example"] == name]

    out = []
    for v in VERDICTS:
        entry = dict(v)
        entry["detail_file"] = f"open_items/{v['row']}.md"
        entry["fallback_applied"] = v["matched_worked_example"] is None
        entry["what_decided_it"] = (
            "the worked example named above, which the ruling puts "
            f"{WORKED_EXAMPLES[v['matched_worked_example']]}"
            if v["matched_worked_example"] is not None else
            "D-639's fallback (1A), applied because no worked example matches — and the verdict is "
            f"derived from `{FALLBACK_BIT}`, not authored beside it"
        )
        out.append(entry)

    return {
        "purpose": (
            "D-639's test applied a second time — over the OPEN APPARATUS-CLASSED rows the phase-1 "
            "finish line names as the one item the test has not decided. The first application "
            "graded three documents; this grades the rows, and the ruling, its worked examples and "
            "its locator are imported from that application rather than restated (#6)."
        ),
        "generated_by": "tools/audit/decisions/gen_true_half_reach_rows.py",
        "generated_for": "cc_instruction_return_continuation_10.md, Task 0 (the user's Ruling 51 of "
                         "`cowork_rulings_2026_08_11_tenth_stop.md`, which places this derivation "
                         "first with nothing large in front of it)",
        "the_ruling": {
            "who_and_when": "User, 2026-08-04. Homed at `CLAUDE.md`, the D-231 phase-1 clause; "
                            "register entry D-639.",
            "worked_examples_that_ARE_the_test": WORKED_EXAMPLES,
            "imported_from": "tools/audit/decisions/gen_true_half_reach.py (#6 — one home for the "
                             "test's own definition)",
            **ruling,
        },
        "the_population": {
            "what_it_is": "the open rows the gating split classes apparatus, and therefore "
                          "non-gating — the finish line's own item, whose closing act is ONE "
                          "derivation over the whole set rather than a per-row judgment",
            "derived_from": "tools/audit/phase1_completion_inventory.json → "
                            "the_gating_split.non_gating.ids",
            "count": len(population),
            "ids": population,
            "how_a_disagreement_is_handled": "a STOP in either direction — a row derived but "
                                             "ungraded, or graded but not derived, halts the run",
        },
        "the_fallback": {
            "what_it_is": (
                "Option (1A) — the doc-sync half reaches only the account of the ANALYSIS — which "
                "the ruling states as the answer where the test needs judgment, together with its "
                "instruction that a session finding itself arguing a case applies the fallback and "
                "SAYS SO rather than stretching a worked example to reach a verdict."
            ),
            "was_it_reached": bool(undecided),
            "how_it_is_made_mechanical_here": (
                "One authored bit per row and nothing else: does the row assert that a document "
                "STATES SOMETHING FALSE ABOUT THE SYSTEM — its behaviour, its inputs, its "
                "parameters, or what a layer produces? The verdict is then DERIVED from that bit, "
                "and a verdict disagreeing with it is a STOP. Two consequences are deliberate: an "
                "OMISSION is not a statement, so a row recording something a document fails to say "
                "is not reached; and a document's account of the WORK — a stage, a closure, a "
                "commit standing — is not the account of the analysis."
            ),
            "rows_the_test_did_not_decide": undecided,
            "count_undecided": len(undecided),
        },
        "verdicts": out,
        "retired_verdicts": {
            "what": "Verdicts whose ROW has since left the derived population. Each is kept WHOLE "
                    "rather than deleted (#12) and is COUNTED NOWHERE — it is history, not a "
                    "grading. A retired verdict naming a row this derivation reaches again is a "
                    "STOP in the other direction: a reading made of a row as it stood is not "
                    "evidence about a row that has since moved, so it is RE-READ and re-authored "
                    "rather than restored. This is authored-input maintenance (D-648), not a "
                    "mechanism change.",
            "rows": RETIRED_VERDICTS,
            "count": len(RETIRED_VERDICTS),
        },
        "counted": {
            "rows_graded": len(VERDICTS),
            "inside_the_doc_sync_half": len(inside),
            "outside_it": len(outside),
            "decided_by_a_worked_example": len(VERDICTS) - len(undecided),
            "decided_by_the_fallback": len(undecided),
            "by_worked_example": {k: len(v) for k, v in by_example.items()},
        },
        "rows_inside_the_doc_sync_half": inside,
        "rows_outside_it": outside,
        "what_follows_for_each_verdict": {
            "OUT": "The row leaves the TRUE half and is owed nothing further ON THAT HALF. It does "
                   "not close: each remains an open item with its own recorded act, and this "
                   "derivation moves no status.",
            "IN": "The row joins the phase-1 obligation the finish line's preceding item carries. "
                  "See the gate consequence below, which is REPORTED and not applied.",
        },
        "the_gate_consequence_this_carries": {
            "what_it_is": (
                "The finish line's preceding item is the TRUE-half item whose rows GATE. A row this "
                "derivation puts IN therefore raises the question whether its non-gating "
                "classification survives, which is the same question the first application raised "
                "for OI-332 and which the user then ruled at OI-336."
            ),
            "why_it_is_reported_and_not_applied_here": (
                "A non-gating verdict is DERIVED from the apparatus cut and never hand-added — "
                "`CLAUDE.md` forbids hand-adding one for a row the first cut never reached, and "
                "`tools/audit/gen_nongating_apparatus_rows.py` is the one place a verdict is "
                "authored. Moving one is a change to that tool's authored table and to a published "
                "classification, which is the user's. The precedent is exact: the first "
                "application reported the same consequence, declined to apply it, and the user "
                "ruled it separately."
            ),
            "the_rows_it_is_raised_for": inside,
            "what_is_NOT_claimed": (
                "That any of these rows gates. D-639 says in terms that what PHASE 1 OWES and what "
                "A STAGE WAITS ON are different tests with different subjects, and neither "
                "overrides the other. This derivation answers the first and leaves the second "
                "exactly where the apparatus declaration has it."
            ),
        },
        "what_this_derivation_does_not_do": [
            "It moves no open-items status, in either direction.",
            "It moves no gate verdict and edits no authored apparatus table.",
            "It proposes no fix, no design and no inference change, and it touches nothing about "
            "the analysis, any measurement of it, any golden or anything in `tools/robust_stop/`.",
            "It writes no portion of phase 1's completion statement.",
        ],
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    art = build()
    text = json.dumps(art, indent=2, ensure_ascii=False) + "\n"
    if args.check:
        have = read(OUT) if os.path.exists(OUT) else ""
        if have != text:
            print("STALE vs the files: true_half_reach_rows.json does not re-derive")
            return 1
        print("the D-639 row application re-derives from the files")
        return 0
    with open(OUT, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    c = art["counted"]
    print(f"wrote {os.path.relpath(OUT, ROOT)}")
    print(f"  {c['rows_graded']} rows graded: {c['inside_the_doc_sync_half']} IN, "
          f"{c['outside_it']} OUT")
    print(f"  decided by a worked example: {c['decided_by_a_worked_example']}; "
          f"by the fallback: {c['decided_by_the_fallback']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
