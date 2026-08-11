#!/usr/bin/env python3
"""The FINISH LINE for D-231's phase 1: what is still required, and what act would close each item.

THE RULING (user, 2026-08-04, dispatch `cc_instruction_commit_and_finish_line.md`, R2): derive one
statement, FRESHLY COMPUTED, of exactly what phase 1 still requires — and that list is then THE
SCOPE.  Nothing outside it gets a wave; adding to it requires a user ruling.

HOW THIS DIFFERS FROM `gen_phase1_completion_inventory.py`, which it IMPORTS rather than repeats
(#6 — one path per concern).  That tool measures POPULATIONS: how many entries are unhomed, how
many rows assert a specification states something false.  This one turns those populations into
WORK ITEMS, each carrying THE ACT THAT WOULD CLOSE IT.  The dispatch's rule is the reason the
distinction matters: *an item with no closing act named is not on the finish line — it is a row.*

THIS DERIVES.  IT DOES NOT COMPLETE, AND IT IS NOT PHASE 1's COMPLETION STATEMENT.  The dispatch
forbids writing that statement here (Task 2.4), and no part of this file is a draft of one.  The
statement is the terminal item BELOW, named as owed work.

WHAT IS DERIVED AND WHAT IS AUTHORED — stated because the difference is the whole value:
  DERIVED  — D-231's clause, located by anchor and quoted at HEAD; every population and every
             identifier, from `gen_phase1_completion_inventory.build()` and
             `gen_outstanding_delegations.build()`; every gate verdict, from the committed
             apparatus declaration or the row's own words via the inventory's own classifier.
  AUTHORED — the grouping of those populations into items, and each item's CLOSING ACT.  A
             closing act is a judgment about what work would discharge the item; it is authored
             here and marked as authored, never presented as measured.

THE THREE STOPS, so the list cannot silently stop being a finish line:
  1. An item carrying no closing act STOPS the tool.  That is the dispatch's own rule made
     mechanical rather than remembered.
  2. The items must RECONCILE with the derived populations: every entry the register counts
     unhomed-or-gap must fall in exactly one item, and every row of the true half's wide cut must
     fall in exactly one item.  A population that grows without an item to carry it STOPS the
     tool — which is what makes the list exhaustive rather than a selection.
  3. D-231's clause must be locatable by anchor (inherited from the inventory's own STOP).

Usage:
  python tools/audit/gen_phase1_finish_line.py           # write the artifact
  python tools/audit/gen_phase1_finish_line.py --check   # re-derive, exit 1 on drift
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent / "decisions"))
from output_encoding import use_utf8_output                     # noqa: E402  (path set above)
from gen_phase1_completion_inventory import build as build_inventory      # noqa: E402  (#6)
from gen_outstanding_delegations import build as build_delegations        # noqa: E402  (#6)
from gen_nongating_apparatus_rows import parse_rows                       # noqa: E402  (#6)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

ROOT = Path(__file__).resolve().parent.parent.parent
OUT = ROOT / "tools" / "audit" / "phase1_finish_line.json"

# The committed application of the entry-level rulings, READ AS A FILE rather than imported: the
# generator that produces it imports the route table, which imports THIS module, so importing it
# back would be a cycle. Reading the committed artifact is the same pattern the completion
# inventory already uses for the apparatus declaration, and it carries the same kind of STOP.
R1_APPLICATION = ROOT / "tools" / "audit" / "decisions" / "r1_superseded_reach.json"

# D-639's test applied over THIS FILE's apparatus-row item, READ AS A FILE for the same reason:
# that generator derives its population from the completion inventory, which this module imports,
# so importing it back would be a cycle. Its own STOP is what makes reading it safe — it refuses to
# write unless its authored verdicts and the derived population agree in both directions.
REACH_OVER_ROWS = ROOT / "tools" / "audit" / "decisions" / "true_half_reach_rows.json"

# ── Ruling 65 (user, 2026-08-11): THE BEARING CUT ────────────────────────────────────────────────
#
# The finish line's own per-item gate is cut by D-438's test, and the apparatus residue does not
# gate phase 1's completion.  Everything the cut rests on is LOCATED IN `CLAUDE.md` BY ANCHOR and
# quoted on every run — never typed here — so an item's gate cannot outlive the sentence it rests
# on.  A missing anchor is a STOP: a cut that cannot find its own ground may not be published.
CLAUDE_MD = ROOT / "CLAUDE.md"
APPARATUS = ROOT / "tools" / "audit" / "nongating_apparatus_rows.json"
PHASE3 = ROOT / "tools" / "audit" / "phase3_gate_partition.json"

RULING_65_ANCHOR = ("**★ WHEN PHASE 1 IS COMPLETE — THE FINISH LINE IS CUT BY D-438'S TEST, AND "
                    "THE APPARATUS RESIDUE")
RULING_65_END = "**Phase 2 — issue-finding is EXHAUSTED"
RULING_66_ANCHOR = ("**★ AND WHAT SUCH A ROW IS OWED — IT STOPS BEING OWED, WITH A PER-ROW LAPSE "
                    "RECORD")
RULING_66_END = "**★ RULE (f) — EVERY INDEX STATUS CELL"
# D-438's own line, the half that decides every COMPLETE-half item, and the #19 carve-out clause.
D438_SPEC_COMPLETION = ("the completion of a specification, GATES, because the phase-1 rule in "
                        "Conventions makes specifications COMPLETE and TRUE the thing that "
                        "precedes everything else")
D438_EXEMPTION = "AN ESTABLISHMENT OBLIGATION (#19) ALWAYS GATES, WHATEVER ITS SUBJECT"
D231_STRICT_ORDER = "Three phases, strictly ordered."

# The token the #19 carve-out is recognised by inside a recorded gate ground.  It is the register
# identifier of the principle itself, so a ground that invokes the carve-out cannot fail to carry
# it and a ground that does not invoke it cannot accidentally match.
EXEMPTION_TOKEN = "#19"
# The subject-column vocabulary the record's own rows use for the instrument/measurement layer.
# A row carrying it is one the record's own taxonomy calls a measurement matter.
MEASUREMENT_LAYER_SUBJECT_VOCAB = ("instrument / measurement layer", "instrument/measurement layer")
# The sentence a row's own recorded reason uses when the apparatus criterion ALONE would put it
# outside the gate and only the #19 carve-out keeps it in. Matching the record's own words is what
# makes the carve-out DEMONSTRATED on a member rather than asserted in prose.
CRITERION_ALONE_MARKER = "criterion alone would put it outside the gate"


# ────────────────────────────────────────────── the ENTRY-LEVEL re-cut (user ruling R3, 2026-08-04)
#
# THE RULING: 'Re-cut the finish line at ENTRY granularity. C1 is a statement about decisions, not
# documents; the document cut was a convenience and now misreports the work.'
#
# WHAT WAS WRONG WITH THE DOCUMENT CUT. Items 1–4 take their populations from the DELEGATION
# partition, which classifies by the entry's HOME DOCUMENT — is that document named in a
# user-ratified surface, and in what form. That is the right cut for the question *does a
# delegation exist*, and the wrong one for the question criterion C1 actually asks, which is per
# DECISION. An entry whose obligation an entry-level ruling has already discharged still sits in
# the document cut, because its home document's delegation state has not moved — so the item
# over-reports the work.
#
# RE-CUTTING AN EXISTING ITEM IS NOT ADDING ONE. The scope rule reserves ADDING an item to the
# user; it says in its own words that populations move when the record moves, and it is
# regenerated rather than maintained. This changes what an existing item's population IS, on the
# user's own ruling, and adds no item.
THE_ENTRY_LEVEL_RE_CUT_RULING = (
    "User, 2026-08-04 (R3), dispatch `cc_instruction_guard_fix_and_item1d.md`: 'Re-cut the finish "
    "line at ENTRY granularity. C1 is a statement about decisions, not documents; the document cut "
    "was a convenience and now misreports the work.'"
)


def entry_level_discharges() -> dict:
    """Entries criterion C1 no longer reaches, read off the COMMITTED application of the rulings.

    Nothing is judged here. The dispositions were derived, per entry, against the register's own
    text, by the generator that owns that derivation (#6 — imported in substance, never repeated).
    """
    if not R1_APPLICATION.exists():
        raise SystemExit(
            "STOP: the entry-level re-cut needs the committed application of ruling R1 at "
            f"{R1_APPLICATION}, and it is not there. The re-cut may not fall back to a document "
            "cut silently, and it may not re-derive the dispositions here (#6).")
    app = json.loads(R1_APPLICATION.read_text(encoding="utf-8"))
    counted = app["counted"]
    rows = {r["id"]: r for r in app["rows"]}
    return {
        "ids": list(counted["ids_that_leave"]),
        "ground_per_id": {
            i: rows[i]["disposition_ground"] for i in counted["ids_that_leave"] if i in rows},
        "source": "tools/audit/decisions/r1_superseded_reach.json → counted.ids_that_leave",
        "the_ruling_that_discharges_them": (
            "D-642 (user, 2026-08-04): criterion C1 reaches every decision whose content is LIVE; a "
            "superseded entry's obligation moves to its successor and is discharged where that "
            "successor is homed. Quoted in full at its home and at "
            "`tools/audit/phase1_completion_inventory.json` → the_requirement.criteria → C1."
        ),
        "what_is_NOT_discharged_and_why": {
            "route_changed_rather_than_discharged": list(counted["ids_whose_route_changes"]),
            "why": "At least one successor is itself unhomed, so C1 is defeated and the owed act "
                   "moves to the successor. The entry stays in the population.",
        },
    }


# ─────────────────────────────────────────────────────────── authored: the re-reading of the clause
#
# The dispatch (Task 2.1, fourth bullet) instructs that D-231's clause be READ AGAIN rather than
# the earlier reading reused.  It was.  What that re-reading changed is recorded here, at the one
# place a later reader will look for it.
THE_RE_READING = {
    "instruction": (
        "Dispatch `cc_instruction_commit_and_finish_line.md`, Task 2.1: 'anything D-231's clause "
        "requires that neither half carries — read the clause again rather than reusing the "
        "earlier reading of it.'"
    ),
    "what_the_re_reading_confirms": [
        "The clause carries a THIRD requirement beside the two halves — the purposive clause "
        "'so that conformance is thereafter measured against the specifications themselves — the "
        "decisions register remains the status ledger …, never the conformance reference'. The "
        "earlier reading found it and recorded it as criterion C4; the re-reading agrees. It is "
        "NOT a separate item below, and the reason is stated at "
        "`the_requirement_that_is_a_condition_rather_than_an_item`.",
        "The clause states its own reason — 'because a specification cannot be the compliance "
        "standard while it misdescribes the code' — and that reason is what bounds the doc-sync "
        "half. The earlier reading found this too, as criterion C5.",
    ],
    "★_what_the_re_reading_finds_DIFFERENT": {
        "the_finding": (
            "The earlier reading recorded C5's consequence as an OPEN QUESTION — in its own words, "
            "'The question is REPORTED, not settled' — and the inventory still publishes it that "
            "way at `the_question_the_two_halves_do_not_settle`, whose `who_settles_it` reads 'the "
            "user. It is reported, not decided.' AT HEAD IT IS SETTLED. The user ruled it on "
            "2026-08-04 as D-639, and the ruling sits INSIDE the very span the inventory quotes: "
            "the doc-sync half reaches a document's account of itself ONLY WHERE THAT ACCOUNT "
            "CHANGES HOW THE DOCUMENT'S ANALYSIS CONTENT IS READ, with three worked examples that "
            "ARE the test and an explicit fallback."
        ),
        "why_the_inventory_did_not_move_when_the_ruling_landed": (
            "Its clause quote is DERIVED and therefore did move — `the_requirement.phase_1_verbatim` "
            "contains D-639's text at HEAD. Its criteria are an AUTHORED python constant and did "
            "not. So its `--check` passes, because the artifact matches a fresh derivation, while "
            "the authored half contradicts the derived half inside the same file. This is the "
            "shape OI-332 and OI-334 recorded elsewhere: a computed half that is current beside an "
            "authored half that is not."
        ),
        "what_this_file_does_about_it": (
            "Carries the corrected reading, which is the act the dispatch ordered. It does NOT fix "
            "the inventory — the dispatch forbids fixing anything found (header) — and the finding "
            "is rowed under ruling R3, whose test it does not meet: the subject is an authored "
            "field in an audit artifact, not the analysis, its inputs, or an instrument any "
            "measurement of the analysis depends on."
        ),
        "the_ruling_it_reads": "D-639, at CLAUDE.md's phase-1 clause; the fallback is option (1A).",
    },
    "the_clause_also_carries_a_pointer_to_a_question_that_HAS_NOW_BEEN_RULED": (
        "D-639's own closing paragraph points at `OPEN_ITEMS.md` OI-336 — whether OI-332's "
        "apparatus classification survives reading the whole of D-438's line rather than its first "
        "half — and said in terms that nothing in the clause settles it. ★ THE USER RULED IT on "
        "2026-08-07 (dispatch `cc_instruction_five_rulings.md` §0a, R5): the classification does "
        "NOT survive, OI-332 is re-classed GATING on the second half of D-438's line, and OI-336 "
        "closes. The authored verdict was corrected with its former verdict preserved, and the "
        "derived set and the populations below follow. The pointer is kept rather than deleted "
        "(#12) because D-639's clause still carries it, and a reader arriving from that clause "
        "needs to be told the question is answered. This key formerly read "
        "`the_clause_also_carries_a_pointer_to_an_UNRULED_question` and ended: 'It is the user's. "
        "It is carried below as an item because it has a nameable closing act (a ruling), and "
        "because a gate verdict it moves would move which items here gate.'"
    ),
}

THE_CONDITION_NOT_AN_ITEM = {
    "which_requirement": (
        "C4, the purposive clause: 'so that conformance is thereafter measured against the "
        "specifications themselves — the decisions register remains the status ledger "
        "(supersession, shelving, the same-commit rule), never the conformance reference'."
    ),
    "why_it_is_not_a_separate_item": (
        "It names no work of its own. It is a TEST applied to how the homing items below are "
        "discharged: a decision written where the register points at it, but which a reader of the "
        "owning specification would not find, satisfies C1's letter and defeats C4. Under the "
        "dispatch's own rule — an item with no closing act named is not on the finish line — it is "
        "therefore recorded as a CONDITION on every homing item rather than as a line of its own."
    ),
    "the_condition_it_places_on_every_homing_item": (
        "The decision must be findable FROM the owning specification, not only through the "
        "register. Rule (e) of the decisions register says the same thing from the other side: the "
        "register is 'the index and pointer, never a substitute home'."
    ),
    "and_it_is_satisfied_at_HEAD_for_one_thing_it_used_to_bound": (
        "A completion statement rests on DECISIONS.md, so the register's own published account of "
        "itself had to be true. All three of the statements the inventory checks now read TRUE AT "
        "HEAD — see `the_register_account_of_itself` below. OPEN_ITEMS.md OI-334 is closed."
    ),
}


# ───────────────────────────────────────────────────────────── authored: the items
#
# Each entry names its population by a FUNCTION over the derived data, never by a literal.  The
# `name` fields are plain descriptions rather than codes, per the standing convention forbidding
# self-invented labels and numbering schemes.
def reach_over_rows_block() -> dict:
    """The D-639 row application, read at its own artifact — never restated (D-431).

    A missing artifact is a STOP rather than an absent block: this item's closing act names the
    derivation, and a finish line that quietly omitted it would read as though the act were still
    wholly outstanding.
    """
    if not REACH_OVER_ROWS.is_file():
        raise SystemExit(
            "STOP: this item's closing act names ONE derivation over the whole set and its "
            f"artifact is absent ({REACH_OVER_ROWS}). Run "
            "`tools/audit/decisions/gen_true_half_reach_rows.py` first."
        )
    art = json.loads(REACH_OVER_ROWS.read_text(encoding="utf-8"))
    graded = art["the_population"]["ids"]
    return {
        "performed": "2026-08-11 (CC, `cc_instruction_return_continuation_10.md` Task 0), on the "
                     "user's Ruling 51 of `cowork_rulings_2026_08_11_tenth_stop.md`, which placed "
                     "it first with nothing large in front of it after seven batches of starvation.",
        "artifact": "tools/audit/decisions/true_half_reach_rows.json",
        "the_ruling_and_its_worked_examples_are_imported_not_restated":
            "tools/audit/decisions/gen_true_half_reach.py (#6)",
        "it_graded_the_whole_population_or_nothing":
            "its own STOP — the authored verdicts and the population derived from the completion "
            "inventory must agree in BOTH directions, so a derivation published over a subset "
            "cannot be written",
        "rows_graded": len(graded),
        "rows_inside_the_doc_sync_half": art["rows_inside_the_doc_sync_half"],
        "rows_outside_it": art["rows_outside_it"],
        "decided_by_a_worked_example": art["counted"]["decided_by_a_worked_example"],
        "decided_by_the_fallback": art["counted"]["decided_by_the_fallback"],
        "what_remains_and_who_it_belongs_to": (
            "The rows put OUT leave the TRUE half and are owed nothing further on it; they do not "
            "close, and each keeps its own recorded act. The rows put IN raise the question "
            "whether their non-gating classification survives — the same question the first "
            "application raised for OI-332 and the user then ruled at OI-336. It is REPORTED at "
            "the artifact and not applied here, because a non-gating verdict is derived from a cut "
            "and never hand-added."
        ),
        "no_value_is_restated_here_beyond_the_lists_the_item_already_carries": "D-431 — every "
            "verdict, its ground and its quoted evidence are at the artifact.",
    }


# ═══════════════════════════════ Ruling 65 and Ruling 66: THE BEARING CUT ════════════════════════
#
# WHAT THE CUT IS.  Every item of this finish line carries a gate.  Until the user's Ruling 65 of
# 2026-08-11 that gate was an AUTHORED ground per item; from this act it is DERIVED, by D-438's own
# test — does the item's subject bear on the analysis, on the analysis's inputs, or on a
# measurement tool something depends on — with the #19 carve-out ENCODED rather than remembered.
#
# WHAT IS DERIVED HERE AND WHAT IS STILL AUTHORED.
#   derived  : every clause the cut rests on, LOCATED in CLAUDE.md by its own words and quoted on
#              every run; each item's population kind; each item's bearing verdict; which members
#              only the #19 carve-out keeps gating; the lapse population and each row's grading;
#              the falsification test and every one of its four probes; every count.
#   authored : nothing new. The closing acts stay authored and stay marked authored, exactly as
#              they were before this act.
#
# WHY EVERY GROUND IS LOCATED RATHER THAN TYPED.  A gate whose ground is a typed quotation outlives
# the sentence it quotes — the defect this file's own header calls out one level up. A missing
# anchor is therefore a STOP: a cut that cannot find its own ground may not be published.
def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def locate_in_claude_md(anchor: str, end: str | None, what: str) -> str:
    """Quote a span of CLAUDE.md located by its own words. A missing anchor is a STOP."""
    text = _norm(CLAUDE_MD.read_text(encoding="utf-8"))
    a = _norm(anchor)
    i = text.find(a)
    if i < 0:
        raise SystemExit(
            f"STOP: {what} could not be located in CLAUDE.md by its own words. The bearing cut "
            "rests on it, and a cut that cannot find its own ground may not be published — "
            "Ruling 65's own clause is that the cut is DERIVED and never hand-classified.")
    if end is None:
        return a
    j = text.find(_norm(end), i)
    if j < 0:
        raise SystemExit(
            f"STOP: the end anchor for {what} is no longer present after it in CLAUDE.md, so the "
            "span cannot be quoted whole (D-643 — a ruling invoked as an application is quoted in "
            "full, never the branch that supports the claim).")
    return text[i:j].strip()


def population_kind(item: dict) -> str:
    """DERIVED from the item's own population shape — never assigned per item."""
    p = item["population"]
    if "row_ids" in p:
        return "open rows of the open-items register"
    if "statements" in p:
        return "the completion statement itself"
    return "register entries"


def apparatus_facts() -> dict:
    """The apparatus declaration's own verdicts — the ONE place a row's D-438 verdict is authored."""
    if not APPARATUS.is_file():
        raise SystemExit(
            f"STOP: the apparatus declaration is absent ({APPARATUS}). The bearing cut reads its "
            "per-row verdicts and may not fall back to a default silently.")
    app = json.loads(APPARATUS.read_text(encoding="utf-8"))
    by_id = {i["id"]: i for i in app["items"]}
    return {
        "by_id": by_id,
        "non_gating_ids": sorted(i for i, r in by_id.items() if r["verdict"] == "NON-GATING"),
        "gates_ids": sorted(i for i, r in by_id.items() if r["verdict"] == "GATES"),
        "kept_gating_only_by_the_19_carve_out": sorted(
            i for i, r in by_id.items()
            if r["verdict"] == "GATES" and EXEMPTION_TOKEN in (r.get("gate_ground") or "")),
        # The demonstration A4 asks for, and it is READ OFF THE ROW rather than argued: a row
        # whose own recorded reason states that the documentation criterion ALONE would put it
        # outside the gate is a row the carve-out — and nothing else — keeps inside it.
        "whose_own_reason_says_the_criterion_alone_would_put_them_outside": sorted(
            i for i, r in by_id.items()
            if CRITERION_ALONE_MARKER in (r.get("reason") or "")),
    }


def cut_one_item(item: dict, gating_ids: set, app: dict, grounds: dict) -> dict:
    """D-438's test applied to ONE finish-line item, with the #19 carve-out encoded."""
    kind = population_kind(item)
    members = list(item["population"].get("row_ids", []))
    if kind == "open rows of the open-items register":
        bearing = sorted(m for m in members if m in gating_ids)
        bears = bool(bearing)
        how = ("PER MEMBER, from the committed apparatus declaration's own verdicts — the item "
               "bears if any row in it does. No item-level judgment is made and none is available "
               "to be made: the row verdicts are where D-438's test is applied.")
        exempt = sorted(m for m in members
                        if EXEMPTION_TOKEN in (app["by_id"].get(m, {}).get("gate_ground") or ""))
    elif kind == "register entries":
        bears, bearing = True, []
        how = ("FROM D-438'S OWN LINE, located in CLAUDE.md and quoted at `the_clauses_the_cut_"
               "rests_on`: the completion of a specification GATES, because the phase-1 rule makes "
               "specifications COMPLETE and TRUE the thing that precedes everything else. Every "
               "item of the COMPLETE half is the completion of a specification, so the clause "
               "decides them all and no per-entry judgment is invented.")
        exempt = []
    else:
        bears, bearing = True, []
        how = ("FROM D-231'S OWN CLAUSE, located in CLAUDE.md and quoted at `the_clauses_the_cut_"
               "rests_on`: three phases, STRICTLY ORDERED. The completion statement is what the "
               "order turns on, so it cannot be the residue the cut removes.")
        exempt = []
    gates = bears or bool(exempt)
    return {
        "the_test": grounds["the_test"],
        "population_kind": kind,
        "bears_on_the_analysis_its_inputs_or_a_measurement_tool": bears,
        "how_that_was_derived": how,
        "members_that_bear": bearing,
        "★_the_19_carve_out": {
            "encoded_not_remembered": (
                "A member is kept gating by the carve-out when its own recorded gate ground names "
                "principle #19. The token is the principle's identifier, so a ground that invokes "
                "the carve-out cannot fail to carry it and a ground that does not cannot match by "
                "accident."
            ),
            "members_the_carve_out_keeps_gating": exempt,
            "would_this_item_move_if_the_carve_out_were_OFF": bool(exempt) and not bears,
        },
        "gates_phase_1_completion": gates,
        "owed": gates,
        "why_owed_tracks_the_gate_at_ITEM_granularity": (
            "Ruling 66 — an apparatus row stays open, stops gating and stops being owed. At item "
            "granularity the two coincide by construction and not by choice: the only class the "
            "cut places outside the gate is the apparatus residue, and Ruling 66 is what lapses "
            "it. An item kept gating by the #19 carve-out is therefore still owed, which is the "
            "carve-out doing exactly what it is for."
        ),
        "★_before_the_cut": {
            "gates": item["gate"]["gates"],
            "owed": True,
            "ground": item["gate"]["ground"],
            "derived_from": item["gate"].get("derived_from"),
            "why_it_is_kept": (
                "So the movement is visible rather than inferred (#12), and so the cut can be "
                "recomputed with itself OFF — which is what shows that nothing else moved."
            ),
        },
        "moved": (item["gate"]["gates"] != gates) or (True != gates),
    }


def falsification_test(app: dict, inv: dict, reach: dict, rows_by_id: dict) -> dict:
    """Ruling 65's own test: if the cut files as APPARATUS anything the record elsewhere calls
    inference-bearing, the cut is WRONG AND HALTS.

    Four probes, each over a place the record records a determinate verdict about the SAME row.
    None of them is this file's opinion: each reads a committed surface or the row's own words.
    """
    ng = set(app["non_gating_ids"])

    # (1) The phase-3 gate partition — an independent, user-ACCEPTED partition using the same
    #     D-438 test. Only its item identifiers that NAME a row are comparable, and they are
    #     parsed rather than listed.
    p3 = json.loads(PHASE3.read_text(encoding="utf-8"))
    p3_gating_rows = sorted({f"OI-{m.group(1)}" for i in p3["totals"]["gating_ids"]
                             for m in [re.fullmatch(r"P2-OI(\d+)", i)] if m})
    probe_1 = sorted(ng & set(p3_gating_rows))

    # (2) D-639's reach derivation — a row it puts INSIDE the doc-sync half is a row the record
    #     says states something false about the SYSTEM. This is the exact shape Ruling 56 ruled.
    reach_in = set(reach["rows_inside_the_doc_sync_half"])
    probe_2 = sorted(ng & reach_in)

    # (3) The row's OWN recorded words. A row that asserts its own gate state does so in the
    #     bolded form the index uses for it; prose about gating in lower case is not a verdict and
    #     is deliberately not matched.
    probe_3 = sorted(r for r in ng
                     if "**GATES**" in (rows_by_id.get(r, {}).get("status_column") or ""))

    # (4) The record's own subject taxonomy. A row whose subject column names the
    #     instrument/measurement layer is one the record itself calls a measurement matter.
    probe_4 = sorted(r for r in ng
                     if any(v in (app["by_id"][r]["subject_column"] or "").lower()
                            for v in MEASUREMENT_LAYER_SUBJECT_VOCAB))

    hits = {
        "1_named_GATING_by_the_phase_3_gate_partition": probe_1,
        "2_put_INSIDE_the_doc_sync_half_by_D_639s_reach_derivation": probe_2,
        "3_asserting_its_own_gate_in_the_index": probe_3,
        "4_subject_column_naming_the_instrument_or_measurement_layer": probe_4,
    }
    failing = sorted({r for v in hits.values() for r in v})
    if failing:
        raise SystemExit(
            "STOP — THE CUT IS WRONG AND HALTS (Ruling 65's falsification test). The cut places "
            "in the apparatus class row(s) the record elsewhere calls inference-bearing: "
            + ", ".join(failing) + ".\n  per probe: " + json.dumps(hits))
    return {
        "the_ruling": (
            "User, 2026-08-11, Ruling 65: 'If the cut moves into the apparatus class any item the "
            "record elsewhere calls inference-bearing, the cut is wrong and halts.' Without this a "
            "declaration cannot be told apart from wishful filing."
        ),
        "when_it_runs": "on every regeneration, before anything is written",
        "what_it_is_applied_to": {
            "rows": sorted(ng),
            "items": ["every item the cut places outside the gate — read at `THE_FINISH_LINE`"],
        },
        "the_four_probes_and_why_each_is_the_record_rather_than_an_opinion": {
            "1_named_GATING_by_the_phase_3_gate_partition": (
                "tools/audit/phase3_gate_partition.json — a separate, user-ACCEPTED partition "
                "applying the SAME D-438 test to phase 2's items. Only the item identifiers that "
                "NAME an open-items row are comparable, and they are parsed from the artifact "
                "rather than listed here."
            ),
            "2_put_INSIDE_the_doc_sync_half_by_D_639s_reach_derivation": (
                "tools/audit/decisions/true_half_reach_rows.json — a row it puts IN is one the "
                "record says states something false about the SYSTEM. This is the exact shape the "
                "user ruled at Ruling 56, so a disagreement here would be the cut re-deciding a "
                "question already ruled."
            ),
            "3_asserting_its_own_gate_in_the_index": (
                "The row's own status cell, in the bolded form the index uses to assert a gate "
                "state. Lower-case prose about gating is not a verdict and is deliberately not "
                "matched — a looser test would fire on every row that merely discusses the cut."
            ),
            "4_subject_column_naming_the_instrument_or_measurement_layer": (
                "The record's own subject taxonomy. A row filed under the instrument/measurement "
                "layer is one the record itself calls a measurement matter, which is the middle "
                "term of D-438's test."
            ),
        },
        "hits_per_probe": hits,
        "verdict": "PASS — no row the cut places in the apparatus class is called "
                   "inference-bearing anywhere the four probes read",
        "★_what_a_PASS_does_and_does_not_establish": (
            "It establishes that the cut does not CONTRADICT a determinate verdict the record "
            "already holds about the same row. It does not establish that no such row bears on "
            "the analysis — no probe can, since the whole question the criterion answers is a "
            "reading of the row. Probe 2 currently reads an EMPTY IN set and therefore passes "
            "vacuously; that is stated rather than counted as evidence."
        ),
    }


def the_lapse_population(app: dict, reach: dict, rows_by_id: dict) -> dict:
    """Ruling 66's population: which rows stop being owed, and WHAT GRADED EACH.

    THE RULE'S OWN STOP IS ARMED HERE: a row with no named grading DOES NOT LAPSE. It is a STOP
    rather than a silent exclusion, because a row that lapsed without a grading is exactly the
    thing the per-row lapse record exists to make challengeable.
    """
    graded_by_the_reach = set(reach["rows_outside_it"])
    out = []
    ungraded = []
    for rid in app["non_gating_ids"]:
        rec = app["by_id"][rid]
        if rid in graded_by_the_reach:
            grading = {
                "derivation": "tools/audit/decisions/true_half_reach_rows.json",
                "what_it_decided": "D-639's test put the row OUTSIDE the doc-sync half, so it is "
                                   "owed nothing further on phase 1's TRUE half",
                "and_also": "tools/audit/nongating_apparatus_rows.json — the apparatus cut, which "
                            "classes the row NON-GATING on D-438's criterion",
            }
        elif rid in app["by_id"]:
            grading = {
                "derivation": "tools/audit/nongating_apparatus_rows.json",
                "what_it_decided": "the apparatus cut classes the row NON-GATING on D-438's "
                                   "criterion, with its ground and its reason recorded there",
                "and_also": None,
            }
        else:                                                    # pragma: no cover — a STOP
            ungraded.append(rid)
            continue
        detail = ROOT / "open_items" / f"{rid}.md"
        out.append({
            "row": rid,
            "class_basis": rec.get("class_basis"),
            "the_derivation_that_graded_it": grading,
            "detail_file": f"open_items/{rid}.md",
            "the_lapse_record_is_written": (
                detail.is_file() and LAPSE_RECORD_ANCHOR in detail.read_text(encoding="utf-8")),
        })
    if ungraded:
        raise SystemExit(
            "STOP: row(s) would lapse with no named grading: " + ", ".join(sorted(ungraded))
            + ". Ruling 66's own clause is that a row with no named grading DOES NOT LAPSE.")
    written = sorted(r["row"] for r in out if r["the_lapse_record_is_written"])
    return {
        "the_ruling": (
            "User, 2026-08-11, Ruling 66: an apparatus row STAYS OPEN, STOPS GATING and STOPS "
            "BEING OWED, and each lapse is recorded PER ROW with the derivation that graded it. "
            "Homed at CLAUDE.md's non-gating declaration; register entry D-676."
        ),
        "what_lapsing_is_NOT": (
            "It is not a resolution. No status cell moves, no row closes, and the open-row count "
            "is unchanged — the register's rule (d) flips a row with provenance and there is none "
            "here, because nothing was done. What lapses is the OBLIGATION, not the row."
        ),
        "the_population_is_derived": (
            "the NON-GATING set of the committed apparatus declaration — the ONE place a row's "
            "D-438 verdict is authored — read on every run and never listed here"
        ),
        "the_rules_own_STOP_is_armed": (
            "A row with no named grading does not lapse: it halts this derivation rather than "
            "lapsing by default."
        ),
        "count": len(out),
        "rows": out,
        "lapse_records_written": {
            "count": len(written),
            "rows": written,
            "rows_still_owed_a_lapse_record": sorted(
                r["row"] for r in out if not r["the_lapse_record_is_written"]),
            "how_it_is_checked": (
                f"the row's own detail file is searched for the anchor {LAPSE_RECORD_ANCHOR!r}. "
                "This is REPORTED and is deliberately not a STOP: writing the records is a "
                "per-entry pass, which D-672 permits stopping at a member boundary provided the "
                "record says what was done and what was not — and this field is that record."
            ),
        },
    }


LAPSE_RECORD_ANCHOR = "★ LAPSE RECORD"


def the_clauses_the_cut_rests_on() -> dict:
    """Every clause the cut rests on, LOCATED in CLAUDE.md by its own words and quoted at HEAD."""
    return {
        "the_test": (
            "D-438's own test, as Ruling 65 applies it to this list: does the item's subject bear "
            "on the analysis, on the analysis's inputs, or on a measurement tool something depends "
            "on? If yes it gates. An establishment obligation (#19) gates whatever its subject."
        ),
        "ruling_65_quoted_IN_FULL_from_its_home": locate_in_claude_md(
            RULING_65_ANCHOR, RULING_65_END, "Ruling 65, the bearing cut"),
        "ruling_66_quoted_IN_FULL_from_its_home": locate_in_claude_md(
            RULING_66_ANCHOR, RULING_66_END, "Ruling 66, the lapse rule"),
        "d438_the_clause_that_decides_every_COMPLETE_half_item": locate_in_claude_md(
            D438_SPEC_COMPLETION, None, "D-438's specification-completion clause"),
        "d438_the_19_carve_out": locate_in_claude_md(
            D438_EXEMPTION, None, "D-438's #19 carve-out"),
        "d231_the_clause_that_decides_the_terminal_item": locate_in_claude_md(
            D231_STRICT_ORDER, None, "D-231's strict-order clause"),
        "located_by": "anchor string, never a line number (the OI-330 lesson, and D-307)",
        "a_missing_anchor_is_a_STOP": (
            "A gate whose ground is a typed quotation outlives the sentence it quotes. Every "
            "ground here is re-located on every run, so a rewording halts the derivation rather "
            "than leaving a stale account of a rule standing in a published gate."
        ),
    }


def recut(cls: dict, discharged: set[str]) -> dict:
    """A homing class's population at ENTRY granularity (user ruling R3).

    The document cut is PRESERVED beside it rather than replaced (#12): a reader comparing this
    artifact with an earlier one must be able to see which figure moved and by how much.
    """
    by_doc_all = cls["by_document"]
    by_doc: dict[str, list[str]] = {}
    dropped: dict[str, list[str]] = {}
    for doc, ids in by_doc_all.items():
        keep = [i for i in ids if i not in discharged]
        gone = [i for i in ids if i in discharged]
        if keep:
            by_doc[doc] = keep
        if gone:
            dropped[doc] = gone
    kept_entries = sum(len(v) for v in by_doc.values())
    return {
        "entries": kept_entries,
        "documents": len(by_doc),
        "entry_ids_by_document": by_doc,
        "★_this_is_the_ENTRY_level_cut": (
            "The population criterion C1 still reaches, per DECISION. Entries an entry-level "
            "ruling has already discharged are subtracted, and are listed below rather than "
            "silently absent."
        ),
        "at_document_granularity_before_the_re_cut": {
            "entries": cls["entries"],
            "documents": cls["documents"],
            "why_it_is_kept": "So the movement is visible rather than inferred (#12). It is the "
                              "figure this item published before ruling R3.",
        },
        "discharged_by_an_entry_level_ruling": dropped,
        "entries_discharged": sum(len(v) for v in dropped.values()),
    }


def recut_unhomed(cls: dict, discharged: set[str]) -> dict:
    """The `unhomed` class's population, with the SAME subtraction its four siblings apply.

    ★ THE USER'S RULING 61 of 2026-08-11 (`cowork_rulings_2026_08_11_fourteenth_stop.md`), closing
    `OPEN_ITEMS.md` OI-369.  Until this act the last homing item took its population RAW while its
    four siblings subtracted the entries an entry-level ruling had discharged — so the item asked
    for an act the user's Ruling 6 of 2026-08-09 forbids for the one entry it carried.  The ruling
    gives it the same subtraction rather than a carve-out of its own: one machinery per concern (#6),
    two subtraction behaviours across five siblings being the excluded alternative recorded there.

    The subtraction is IMPORTED, not re-implemented: `discharged` is the same set `recut` takes,
    derived by `gen_r1_superseded_reach.py`, whose population the same ruling extends to this class.
    The document cut is PRESERVED beside the result (#12), exactly as `recut` preserves it.
    """
    homes = cls["ids_and_homes"]
    keep = {i: h for i, h in homes.items() if i not in discharged}
    gone = {i: h for i, h in homes.items() if i in discharged}
    return {
        "entries": len(keep),
        "entry_ids_and_current_homes": keep,
        "★_the_same_subtraction_the_four_sibling_items_apply": (
            "The population criterion C1 still reaches, per DECISION. Entries an entry-level ruling "
            "has already discharged are subtracted, and are listed below rather than silently "
            "absent — the user's Ruling 61 of 2026-08-11."
        ),
        "before_the_subtraction": {
            "entries": cls["count"],
            "entry_ids_and_current_homes": homes,
            "why_it_is_kept": "So the movement is visible rather than inferred (#12). It is the "
                              "figure this item published before Ruling 61.",
        },
        "discharged_by_an_entry_level_ruling": gone,
        "entries_discharged": len(gone),
    }


def build_items(inv: dict, deleg: dict, discharged: set[str]) -> list[dict]:
    part = deleg["the_partition"]
    comp = inv["the_complete_half"]
    true_half = inv["the_true_half"]
    split = inv["the_gating_split"]

    gap_gate = {
        "gates": True,
        "ground": (
            "D-438's own line, quoted at CLAUDE.md: '… or the completion of a specification, "
            "GATES, because the phase-1 rule in Conventions makes specifications COMPLETE and TRUE "
            "the thing that precedes everything else.' Every item of the COMPLETE half is the "
            "completion of a specification."
        ),
        "derived_from": "D-438's text, not from a per-row verdict — these are register entries, "
                        "and the apparatus declaration classifies open-items ROWS.",
    }

    unhomed = comp["class_2_recorded_only_on_a_tracking_surface"]
    defense = comp["class_3_defense_not_recorded"]["entries_with_no_rationale_at_all"]

    wide_rows = {r["id"]: r for r in true_half["rows"]}
    gating_ids = split["gates"]["ids"]
    nongating_ids = split["non_gating"]["ids"]

    items: list[dict] = []

    # ── the COMPLETE half, criterion C1 — the homing acts ────────────────────────────────────
    items.append({
        "name": "Register entries whose home document is named in NO user-ratified surface",
        "half": "COMPLETE",
        "criterion": "C1 — every recorded decision written into its owning specification",
        "population": recut(part["A_no_delegation_exists"], discharged),
        "why_it_is_outstanding": part["A_no_delegation_exists"]["the_criterion_that_decides_it"],
        "gate": gap_gate,
        "closing_act": (
            "RE-HOMING, per entry, into the owning layer's specification section — rule (e)'s own "
            "preference ('a decision belongs, wherever possible, in the OWNING LAYER'S "
            "SPECIFICATION') and what makes criterion C4 true without the register. ★ THE FORK IS "
            "RESOLVED: the user's Ruling 38 of 2026-08-09 "
            "(`cowork_rulings_2026_08_09_sixth_stop.md`) rules re-homing the DEFAULT route for "
            "every remaining entry of this item, and NO DOCUMENT IS EXCEPTED at ruling time. A "
            "later exception — a document the user wants kept as a contract home by delegation — "
            "is A NEW USER RULING NAMING THE DOCUMENT, taken BEFORE its entries are re-homed and "
            "never after. THE FORMER CLOSING ACT, PRESERVED (#12), true until that ruling: 'Per "
            "document, ONE of two acts, and they are not equivalent: (i) the user writes a "
            "delegation naming the document — rule (g)'s guard reserves that act to the user, "
            "since only the user writes a delegation into ARCHITECTURE.md; or (ii) each entry is "
            "re-homed into the owning layer's specification section, which rule (e) prefers in "
            "terms.' THE EXCLUDED ALTERNATIVE, RECORDED AT THE RULING: delegation as the default — "
            "it grows the contract-home class, requires the user's writing per document (rule "
            "(g)), and runs against both concrete declinations already on the record."
        ),
        "who_may_perform_it": "a working session, per entry. (The user's route survives only as a "
                              "NEW RULING naming a document, taken before that document's entries "
                              "are re-homed — Ruling 38.)",
        "authored": "the closing act. The population and the criterion are derived.",
    })

    items.append({
        "name": "Register entries whose home document is named only in a form the delegation bar "
                "excludes",
        "half": "COMPLETE",
        "criterion": "C1",
        "population": recut(part["B_naming_exists_but_the_bar_excludes_its_form"], discharged),
        "why_it_is_outstanding":
            part["B_naming_exists_but_the_bar_excludes_its_form"]["the_criterion_that_decides_it"],
        "gate": gap_gate,
        "closing_act": (
            "RE-HOMING, per entry, into the owning layer's specification — the same ruled default "
            "as the item above, and by the same act: the user's Ruling 38 of 2026-08-09 covers "
            "'every remaining register entry in the finish-line items whose home document is named "
            "in NO user-ratified surface, OR ONLY IN A FORM THE DELEGATION BAR EXCLUDES', which is "
            "this item by name. NO DOCUMENT IS EXCEPTED at ruling time, and a later exception is a "
            "new user ruling naming the document, taken BEFORE its entries are re-homed. Note what "
            "is still NOT a closing act: relaxing the bar. D-432 was applied over the whole home "
            "population on the user's ruling, and its own record states that the alternative to "
            "applying it was a revision of the bar, which the user declined. THE FORMER CLOSING "
            "ACT, PRESERVED (#12): 'Per document, ONE of two acts: (i) the user rewrites the "
            "naming into a form D-432 admits — an explicit delegation clause or a named home with "
            "sections, rather than the bare appended citation the bar excludes; or (ii) each entry "
            "is re-homed into the owning layer's specification.'"
        ),
        "who_may_perform_it": "a working session, per entry. (The user's route survives only as a "
                              "NEW RULING naming a document, taken before that document's entries "
                              "are re-homed — Ruling 38.)",
        "authored": "the closing act. The population and the criterion are derived.",
    })

    items.append({
        "name": "Register entries whose admitting delegation does not reach the section they sit in",
        "half": "COMPLETE",
        "criterion": "C1",
        "population": recut(part["C_admitting_delegation_does_not_name_this_section"], discharged),
        "why_it_is_outstanding":
            part["C_admitting_delegation_does_not_name_this_section"]
            ["the_criterion_that_decides_it"],
        "gate": gap_gate,
        "the_widening_question_is_ALREADY_RULED": (
            "This is the only class a widening moves, and the user ruled BOTH its documents on "
            "2026-08-04 (rulings R2 and R3 of `cc_instruction_census_delegation_and_commit.md`): "
            "the voice-leading delegation is NOT widened, and NO delegation is drafted or written "
            "for the structural-integrity audit. Both are recorded as RULINGS, NOT DEFERRALS. The "
            "derived count of write-list members still awaiting an act by the user is "
            "`tools/audit/decisions/outstanding_delegations.json` → "
            "`counted.write_list_members_still_AWAITING_AN_ACT_BY_THE_USER`, and it is empty."
        ),
        "gate_note": (
            "The delegation question is closed; the ENTRIES are not. A ruling that no delegation "
            "will be written leaves the entries where they are, so C1 is still undischarged for "
            "them — by the record's own intent rather than by an oversight."
        ),
        "closing_act": (
            "The remedy the record itself names, which is not a delegation act: at the document, "
            "or by homing those entries where the concern is owned — the register's "
            "`not_write_list_cases` states it in those words. Since the delegation route is ruled "
            "out, the act is a re-homing, per entry."
        ),
        "who_may_perform_it": "a working session, per entry.",
        "authored": "the closing act. The population, the criterion and the ruling are derived.",
    })

    items.append({
        "name": "Register entries the delegation reaches, in a section that records findings "
                "rather than stating rules",
        "half": "COMPLETE",
        "criterion": "C1",
        "population": recut(part["E_reached_and_the_kind_half_decides"], discharged),
        "why_it_is_outstanding":
            part["E_reached_and_the_kind_half_decides"]["the_criterion_that_decides_it"],
        "gate": gap_gate,
        "closing_act": (
            "Not a delegation matter — the partition says so in its own words ('the remedy is at "
            "the document'). Per entry, ONE of two acts: (i) the rule the entry records is written "
            "into a section that STATES it, in the specification that owns the concern; or (ii) the "
            "finding-recording section is rewritten to state the rule, which changes what D-430's "
            "kind half sees. (i) is the one rule (e) prefers."
        ),
        "who_may_perform_it": "a working session, per entry.",
        "authored": "the closing act. The population and the criterion are derived.",
    })

    items.append({
        "name": "Register entries with no home at all — recorded only on a session-handoff archive "
                "or a superseded status archive",
        "half": "COMPLETE",
        "criterion": "C1",
        "population": recut_unhomed(unhomed, discharged),
        "why_it_is_outstanding": unhomed["what_it_is"],
        "gate": gap_gate,
        "closing_act": (
            "Per entry: write the decision into the specification that owns its subject, and leave "
            "the archive text in place (#12 — the archive is provenance, and nothing is deleted "
            "from it). The archives themselves are reference-only and are NOT part of the "
            "session-start read, which is precisely why an entry homed only there defeats C4. "
            "★ IT GOVERNS WHAT THIS ITEM STILL HOLDS, AND NOTHING MORE (the user's Ruling 61 of "
            "2026-08-11, closing `OPEN_ITEMS.md` OI-369): a SUPERSEDED entry whose successors are "
            "homed leaves this item by the same D-642 subtraction its four sibling items apply, and "
            "nothing is written into any specification for it — a supersession is register "
            "business, which is what the user's Ruling 6 of 2026-08-09 ruled for the entry this "
            "item used to carry. The act above therefore reaches whatever the subtraction leaves "
            "standing, never what it removes."
        ),
        "who_may_perform_it": "a working session, per entry.",
        "authored": "the closing act. The population, the homes and the subtraction are derived.",
    })

    # ── the COMPLETE half, criterion C2 — the defenses ───────────────────────────────────────
    items.append({
        "name": "Register entries whose defense the record does not state",
        "half": "COMPLETE",
        "criterion": "C2 — with its defense",
        "population": {"entries": defense["count"], "entry_ids": defense["ids"]},
        "why_it_is_outstanding": (
            "Every design decision carries its defense at its home — the research adopted, the "
            "measurement that decided it, or the constraint that forced it. These entries carry "
            "none."
        ),
        "gate": gap_gate,
        "closing_act": (
            "Per entry, ONE of two acts, and the second is not a lesser one: (i) record, at the "
            "entry's home, the defense THE RECORD HOLDS — a citation to the research, the "
            "measurement, or the constraint; or (ii) record 'derivation not recorded' where the "
            "record holds none. Writing a defense from memory is FORBIDDEN and would not close the "
            "item: the standing convention says a defense written after the fact without a source "
            "is invention, and the never-work-from-memory rule forbids it. So this item is closed "
            "by SEARCHING the record, and its outcome per entry is not predictable in advance."
        ),
        "who_may_perform_it": "a working session, per entry.",
        "authored": "the closing act. The population is derived.",
    })

    # ── the TRUE half, criterion C3 ──────────────────────────────────────────────────────────
    items.append({
        "name": "Open rows asserting a specification states something false at HEAD, which GATE",
        "half": "TRUE",
        "criterion": "C3 — the specification text corrected wherever it states something false",
        "population": {"rows": len(gating_ids), "row_ids": gating_ids},
        "why_it_is_outstanding": (
            "Each row records a statement in a document of record that is false at HEAD, or an "
            "obligation that keeps one from being checkable. Under D-438 each bears on the "
            "analysis, its inputs, or an instrument a measurement depends on — or is an "
            "establishment obligation, which always gates whatever its subject."
        ),
        "gate": {
            "gates": True,
            "ground": "per row, from the committed non-gating apparatus declaration, the row's own "
                      "recorded words, or D-438's default that an unsettled row gates",
            "derived_from": "tools/audit/phase1_completion_inventory.json → the_gating_split",
        },
        "per_row_gate_source": split["where_each_verdict_came_from"],
        "closing_act": (
            "Per row: correct the statement at the document that makes it, or discharge the "
            "obligation the row records, and flip the INDEX row with provenance (register rule "
            "(d)). Rows differ widely in size and several are user rulings rather than session "
            "work — see `the_rows_that_are_user_rulings`."
        ),
        "who_may_perform_it": "a working session per row, EXCEPT the rows listed as user rulings.",
        "authored": "the closing act. The population and every gate verdict are derived.",
    })

    items.append({
        "name": "Open documentation rows classed apparatus — D-639's test has decided them, and "
                "the user's Ruling 66 lapses what they were owed",
        "★_the_former_name_preserved": (
            "'Open documentation rows classed apparatus, whose place inside the doc-sync half "
            "D-639's test has not yet decided' (#12). It was true until 2026-08-11: the "
            "derivation ran on that date and the user's Rulings 65 and 66 then decided what "
            "follows for the rows it graded, so the clause 'has not yet decided' had become false "
            "about this item — which is exactly what phase 1's own TRUE half does not admit in a "
            "surface a commissioning reader reads."
        ),
        "half": "TRUE",
        "criterion": "C3, bounded by C5 and D-639",
        "population": {"rows": len(nongating_ids), "row_ids": nongating_ids},
        "why_it_is_outstanding": (
            "★ IT IS NO LONGER OUTSTANDING, AND THE FIELD SAYS SO RATHER THAN BEING DELETED (#12). "
            "D-438 declared these rows non-gating, so no stage waits on them; D-639 said in terms "
            "that what a STAGE waits on and what PHASE 1 OWES are different tests with different "
            "subjects, and this item existed for the second question. Both halves are now "
            "answered. **The derivation ran** over the whole set — see `the_derivation_has_run` — "
            "and **the user's Ruling 65 then cut this finish line by D-438's test**, so the "
            "apparatus residue does not gate phase 1's completion, and **Ruling 66 lapses what "
            "these rows were owed**: each stays open, gates nothing and is no longer work anybody "
            "owes. What remains is not an obligation but a RECORD — the per-row lapse record, one "
            "per row, naming the derivation that graded it."
        ),
        "the_derivation_has_run": reach_over_rows_block(),
        "gate": {
            "gates": False,
            "ground": "the committed non-gating apparatus declaration, or the row's own recorded "
                      "words that it is an apparatus row",
            "derived_from": "tools/audit/phase1_completion_inventory.json → the_gating_split",
        },
        "closing_act": (
            "★ THE PER-ROW LAPSE RECORD, and nothing else (the user's Ruling 66 of 2026-08-11): "
            "one dated record in each row's own detail file, naming the derivation that graded it, "
            "so a later reader sees why the row stopped being owed and can re-open it by "
            "challenging a recorded derivation rather than by rediscovering the issue. A row with "
            "no named grading DOES NOT LAPSE — the derivation halts instead. Which rows lapse and "
            "what graded each is at `★_the_bearing_cut.the_lapse_population`, derived and never "
            "hand-listed. THE FORMER CLOSING ACT, PRESERVED (#12), and it is DISCHARGED rather "
            "than superseded: 'ONE derivation, not a per-row judgment: apply D-639's test — does "
            "the document's account of ITSELF change how its analysis content is read? — over "
            "these rows, generated the way its first application was, so the verdicts are derived "
            "and each carries its reason. Rows the test puts OUT leave the TRUE half and are owed "
            "nothing further; rows it puts IN join the item above. D-639's fallback governs any "
            "row the test does not decide mechanically: option (1A), the half reaches only the "
            "account of the ANALYSIS — and a session that finds itself arguing a case applies the "
            "fallback and says so.' It ran on 2026-08-11 and its one IN verdict was applied by the "
            "user's Ruling 56."
        ),
        "who_may_perform_it": "a working session, per row — a per-entry pass, which D-672 permits "
                              "stopping at a member boundary provided the record says what was "
                              "done and what was not.",
        "already_decided_for_three_documents": (
            "D-639's first application, at OPEN_ITEMS.md OI-332, decided three documents — one "
            "matching each worked example — without reaching the fallback. Generated at "
            "`tools/audit/decisions/true_half_reach.json`; no verdict is restated here (D-431)."
        ),
        "authored": "the closing act. The population and every gate verdict are derived.",
    })

    # ── the terminal item ────────────────────────────────────────────────────────────────────
    items.append({
        "name": "Phase 1's completion statement",
        "half": "terminal — it is what the finish line is the finish line OF",
        "criterion": "D-231's phase 1 as a whole, read against C1, C2, C3 and C4",
        "population": {"statements": 1},
        "why_it_is_outstanding": (
            "It is not written, not drafted and not partially written. Every wave since the "
            "completion inventory has said so in its own status entry, and this file does not "
            "write it either — the dispatch forbids it at Task 2.4."
        ),
        "gate": {
            "gates": True,
            "ground": "D-231's own words: three phases, STRICTLY ORDERED. Phase 2 does not open "
                      "and phase 3 does not begin until phase 1 is complete.",
            "derived_from": "D-231's clause, quoted at `the_requirement`",
        },
        "closing_act": (
            "★ AMENDED BY THE USER'S RULING 65 OF 2026-08-11, and the amendment is the whole of "
            "what that ruling does to this item: **once every GATING item above is discharged** — "
            "the inference-bearing obligations, as the bearing cut derives them — write the "
            "statement, resting it on the specifications rather than on the register (C4), and "
            "stating what it may NOT claim. **The apparatus residue does not gate it**, so an item "
            "the cut places outside the gate is not something this statement waits on; and what "
            "such a row is then owed is Ruling 66's, which lapses it. THE FORMER CLOSING ACT, "
            "PRESERVED (#12), true until that ruling: 'Once every item above is closed: write the "
            "statement, resting it on the specifications rather than on the register (C4), and "
            "stating what it may NOT claim.' **What the amendment does NOT do:** it does not "
            "write, draft or partially write the statement; it does not discharge any gating item; "
            "and it does not weaken the #19 exception, which keeps an establishment obligation "
            "inside the gate whatever its subject."
        ),
        "★_one_bound_on_this_item_is_LIFTED_and_is_recorded_rather_than_dropped": (
            "This act formerly carried a bound, in these words: 'in particular that no CURRENT "
            "unresolved residual may be published while the cluster-disposition layer cannot be "
            "re-derived at HEAD (OPEN_ITEMS.md OI-333), which is a bound on what may be said and "
            "not a blocked derivation.' ★ IT NO LONGER APPLIES: the user ruled OI-333 on "
            "2026-08-07 (R4), the six uncompilable register patterns are escaped, and the "
            "disposition layer re-derives at the register's current backbone — so a current "
            "residual is derivable. The former wording is kept (#12) because the bound was real "
            "while it stood and a reader comparing artifacts must see why it went. What the "
            "repair's own diff did NOT settle rides with it: whether the regenerated layer "
            "supersedes the committed one is the user's, and both are on disk "
            "(`tools/audit/decisions/oi333_repair.json`)."
        ),
        "who_may_perform_it": "the user commissions it; a working session writes it.",
        "authored": "the closing act, and the record of the bound that has been lifted.",
    })

    return items


# ─────────────────────────────────────────────────────── authored: rows that are user rulings
ROWS_THAT_ARE_USER_RULINGS = {
    "what_this_is": (
        "Rows inside the gating item whose closing act is a RULING and not session work. They are "
        "named because a finish line that reads as session work end to end would mis-state who is "
        "blocked on what."
    ),
    "rows": {},
    "how_this_list_was_made": (
        "AUTHORED, from the rows' own recorded dispositions as the status entries state them. It "
        "is not a derived partition of the gating set and is not offered as one — it names the "
        "rows a reader would otherwise mistake for session work."
    ),
    "the_list_is_EMPTY_at_HEAD_and_that_is_a_result": (
        "Every row this list carried was RULED by the user on 2026-08-07, in one act (dispatch "
        "`cc_instruction_five_rulings.md` §0a), and each closed. An empty list here does not mean "
        "the gating item is now all session work in general — it means no row currently inside it "
        "is waiting on a ruling. The three that were are kept whole below."
    ),
    "★_rows_whose_ruling_has_been_MADE": {
        "what_this_is": (
            "Rows this list carried until the user ruled them. They are kept rather than deleted "
            "(#12): the list's own value is that it names who is blocked on what, and a reader "
            "comparing this artifact with an earlier one must be able to see that a row left "
            "because it was ANSWERED rather than because it was dropped. The tool STOPS if one of "
            "them is still in the derived gating set, or is also named live above."
        ),
        "rows": {
            "OI-331": {
                "what_it_was_owed_a_ruling_FOR": (
                    "Which of two register entries the record keeps, where a LIVE user-ratified "
                    "entry names a convergence proxy the build measured false and dropped. All "
                    "three candidate remedies change a user-ratified entry."
                ),
                "ruled": (
                    "2026-08-07, R3: the proxy clause and its worked example are struck from the "
                    "signed contract, which now states the current behaviour and records the "
                    "struck clause as tried and closed with D-622 superseding it; D-261's "
                    "headline rule and ratified status stand unchanged."
                ),
            },
            "OI-336": {
                "what_it_was_owed_a_ruling_FOR": (
                    "Whether OI-332's apparatus classification survives reading the whole of "
                    "D-438's line rather than its first half. A non-gating verdict is derived "
                    "from a cut and never hand-added, so it is the user's. D-639's own closing "
                    "paragraph points here."
                ),
                "ruled": (
                    "2026-08-07, R5: it does not survive. OI-332 is re-classed GATING on the "
                    "second half of D-438's line, the authored verdict corrected with the former "
                    "verdict preserved, and the derived populations follow."
                ),
            },
            "OI-333": {
                "what_it_was_owed_a_ruling_FOR": (
                    "Whether the disposition check should re-derive rather than re-read, and what "
                    "becomes of the six patterns that stop the layer regenerating. The row also "
                    "bounds what the terminal item may claim."
                ),
                "ruled": (
                    "2026-08-07, R4: one bounded repair wave — snapshot first, escape the six, "
                    "regenerate, diff and explain every moved cluster, and add a NARROW "
                    "producibility mode rather than widening the coverage check. The bound on the "
                    "terminal item is lifted: the layer re-derives at HEAD."
                ),
            },
        },
    },
}

THE_SCOPE_RULE = {
    "the_ruling": (
        "User, 2026-08-04 (R2), dispatch `cc_instruction_commit_and_finish_line.md`: 'Derive the "
        "finish line: one statement, freshly computed, of exactly what phase 1 still requires. "
        "That list is then the scope. Nothing outside it gets a wave.'"
    ),
    "what_that_means_operationally": [
        "Nothing outside the items above gets a wave. Not a dispatch, not a session, not a "
        "sub-task of one.",
        "An addition to this list requires a USER RULING. A session may not add an item to it, "
        "however well-founded the item looks — that is what makes this a finish line rather than a "
        "snapshot of one moment's opinion.",
        "A finding made while working an item is governed by ruling R3, not by this list: if its "
        "subject bears on the analysis, its inputs, or an instrument a measurement depends on, it "
        "is SURFACED to the user whatever its size; if it does not, it is rowed and left — no "
        "wave, no dispatch, no surface.",
        "An establishment obligation (#19) always gates and is therefore always surfaced, whatever "
        "its subject. R3 does not weaken that, and neither does this list.",
    ],
    "what_this_list_is_NOT": (
        "It is not phase 1's completion statement, not a draft of one, and not an authorization "
        "for any fix, design or inference change. D-231 forbids fix design before phase 1 "
        "completes, and nothing here moves that."
    ),
    "how_it_stays_honest": (
        "It is regenerated, not maintained. Every population is a function over the register and "
        "the open-items index at HEAD, so an item's size moves when the record moves, and the "
        "reconciliation STOP below fires if a population appears that no item carries."
    ),
}


# ───────────────────────────────────────────────────────────────────────────── build
def build() -> dict:
    inv = build_inventory()
    deleg = build_delegations()
    disch = entry_level_discharges()
    discharged = set(disch["ids"])
    items = build_items(inv, deleg, discharged)

    # ── Ruling 65: THE BEARING CUT, applied to every item ────────────────────────────────────
    # Order matters and is stated so it is not rearranged: each item's PRE-CUT gate is read first
    # and frozen (#12), the cut is then derived and replaces the gate, and only afterwards is the
    # falsification test run — over the result rather than over the intention.
    app = apparatus_facts()
    if not REACH_OVER_ROWS.is_file():                            # pragma: no cover — a STOP
        raise SystemExit(f"STOP: the reach derivation's artifact is absent ({REACH_OVER_ROWS}); "
                         "the bearing cut's second probe reads it and may not skip it silently.")
    reach = json.loads(REACH_OVER_ROWS.read_text(encoding="utf-8"))
    rows_by_id = {r["id"]: r for r in parse_rows()}
    grounds = the_clauses_the_cut_rests_on()
    gating_ids_set = set(inv["the_gating_split"]["gates"]["ids"])

    before_the_cut = [{"item": it["name"], "gates": it["gate"]["gates"], "owed": True,
                       "ground": it["gate"]["ground"]} for it in items]
    for it in items:
        cut = cut_one_item(it, gating_ids_set, app, grounds)
        it["★_the_bearing_cut"] = cut
        it["gate"] = {
            "gates": cut["gates_phase_1_completion"],
            "ground": ("DERIVED by the bearing cut from D-438's own test, with the #19 carve-out "
                       "encoded — the user's Ruling 65 of 2026-08-11. The clause that decides this "
                       "item is quoted at `★_the_bearing_cut.how_that_was_derived`, and the "
                       "clauses themselves are located in CLAUDE.md on every run."),
            "derived_from": "tools/audit/gen_phase1_finish_line.py → cut_one_item(), reading the "
                            "committed apparatus declaration and CLAUDE.md's own clauses",
        }
    after_the_cut = [{"item": it["name"], "gates": it["gate"]["gates"],
                      "owed": it["★_the_bearing_cut"]["owed"]} for it in items]
    falsification = falsification_test(app, inv, reach, rows_by_id)
    lapse = the_lapse_population(app, reach, rows_by_id)

    # ── STOP 1: an item with no closing act is not an item ───────────────────────────────────
    for it in items:
        if not it.get("closing_act", "").strip():
            raise SystemExit(
                "STOP: item %r carries no closing act. The dispatch's own rule is that an item "
                "with no closing act named is not on the finish line — it is a row." % it["name"])

    # ── STOP 2: the items must reconcile with the derived populations ────────────────────────
    part = deleg["the_partition"]
    comp = inv["the_complete_half"]
    split = inv["the_gating_split"]

    homing_covered = (part["A_no_delegation_exists"]["entries"]
                      + part["B_naming_exists_but_the_bar_excludes_its_form"]["entries"]
                      + part["C_admitting_delegation_does_not_name_this_section"]["entries"]
                      + part["E_reached_and_the_kind_half_decides"]["entries"])
    gap_total = comp["class_1_documentation_gap"]["count"]
    unhomed_total = comp["class_2_recorded_only_on_a_tracking_surface"]["count"]
    if homing_covered != gap_total:
        raise SystemExit(
            "STOP: the homing items cover %d register entries but the register counts %d in the "
            "documentation-gap class. A population no item carries means this list is not a finish "
            "line." % (homing_covered, gap_total))

    # ── STOP 2b: the ENTRY-level re-cut must ACCOUNT for every entry the document cut carried ──
    # Subtracting a population is only safe if every subtracted entry is named with its ground.
    # An entry that vanishes from the items without appearing among the discharged is a silent
    # narrowing of the scope, which is the one thing the scope rule reserves to the user.
    homing_items = [i for i in items if i["criterion"].startswith("C1")
                    and "entry_ids_by_document" in i["population"]]
    entry_covered = sum(i["population"]["entries"] for i in homing_items)
    entry_discharged = sum(i["population"]["entries_discharged"] for i in homing_items)
    if entry_covered + entry_discharged != gap_total:
        raise SystemExit(
            "STOP: the entry-level re-cut accounts for %d + %d entries but the documentation-gap "
            "class holds %d. Every entry the document cut carried must be either still on the "
            "finish line or named as discharged, with its ground."
            % (entry_covered, entry_discharged, gap_total))
    accounted = {i for it in homing_items
                 for ids in it["population"]["discharged_by_an_entry_level_ruling"].values()
                 for i in ids}
    unaccounted = sorted(discharged - accounted)
    if entry_discharged != len(accounted):
        raise SystemExit(
            "STOP: the discharged count and the discharged identifiers disagree — %d against %d."
            % (entry_discharged, len(accounted)))

    # ── STOP 2c: the `unhomed` item's subtraction must ACCOUNT for its whole class (Ruling 61) ──
    # The same demand STOP 2b makes of the four sibling items, made of the fifth. It is stated
    # separately because the class has its own shape — id → home rather than by document — and
    # folding it into 2b would have meant re-shaping one of the two populations to fit the check.
    unhomed_items = [i for i in items
                     if i["criterion"] == "C1" and "entry_ids_and_current_homes" in i["population"]]
    if len(unhomed_items) != 1:
        raise SystemExit(
            "STOP: expected exactly one item over the register's `unhomed` class, found %d. The "
            "subtraction's reconciliation is stated over one item and cannot silently cover two."
            % len(unhomed_items))
    unhomed_pop = unhomed_items[0]["population"]
    unhomed_kept = unhomed_pop["entries"]
    unhomed_discharged = unhomed_pop["entries_discharged"]
    if unhomed_kept + unhomed_discharged != unhomed_total:
        raise SystemExit(
            "STOP: the `unhomed` item accounts for %d + %d entries but the register's `unhomed` "
            "class holds %d. Every entry the class carried must be either still on the finish line "
            "or named as discharged, with its ground."
            % (unhomed_kept, unhomed_discharged, unhomed_total))

    rows_covered = split["gates"]["count"] + split["non_gating"]["count"]
    wide_total = inv["the_true_half"]["the_wide_cut"]["count"]
    if rows_covered != wide_total:
        raise SystemExit(
            "STOP: the true-half items cover %d rows but the wide cut holds %d."
            % (rows_covered, wide_total))

    ruling_rows = set(ROWS_THAT_ARE_USER_RULINGS["rows"])
    stray = sorted(ruling_rows - set(split["gates"]["ids"]))
    if stray:
        raise SystemExit(
            "STOP: rows named as user rulings are not in the gating set at HEAD: "
            + ", ".join(stray) + " — the authored list has drifted from the derived one.")
    # A row whose ruling HAS been made must have left the gating set, and must not also be named
    # live above. Both directions, so the ruled table can neither become a second live list nor a
    # place a still-open row is quietly filed in.
    ruled = set(ROWS_THAT_ARE_USER_RULINGS["★_rows_whose_ruling_has_been_MADE"]["rows"])
    back = sorted(ruled & set(split["gates"]["ids"]))
    if back:
        raise SystemExit(
            "STOP: row(s) recorded as RULED are still in the derived gating set: "
            + ", ".join(back) + " — a row that is still owed work needs a live entry, not a "
            "record that it was answered.")
    both = sorted(ruled & ruling_rows)
    if both:
        raise SystemExit(
            "STOP: row(s) named both as awaiting a ruling and as ruled: " + ", ".join(both) + ".")

    total_entries = entry_covered + unhomed_kept
    defense_total = comp["class_3_defense_not_recorded"][
        "entries_with_no_rationale_at_all"]["count"]

    return {
        "purpose": (
            "THE FINISH LINE for D-231's phase 1: what is still required, item by item, with the "
            "act that would close each. Derived at HEAD. This is NOT phase 1's completion "
            "statement and is not a draft of one."
        ),
        "generated_by": "tools/audit/gen_phase1_finish_line.py",
        "generated_for": "cc_instruction_commit_and_finish_line.md (Task 2, ruling R2)",
        "derived_at_head_from": [
            "tools/audit/gen_phase1_completion_inventory.py → build() (imported, not repeated, #6)",
            "tools/audit/decisions/gen_outstanding_delegations.py → build() (imported, #6)",
            "CLAUDE.md, D-231's clause, located by anchor and quoted",
        ],
        "what_is_authored_and_what_is_derived": {
            "derived": (
                "D-231's clause; every population, every entry identifier and every row "
                "identifier; every gate verdict; the delegation partition and its criteria"
            ),
            "authored": (
                "the grouping of the populations into items; each item's CLOSING ACT; the list of "
                "gating rows that are user rulings rather than session work; the re-reading note"
            ),
            "why_it_matters": (
                "A closing act is a judgment about what work would discharge an item. It is marked "
                "authored on every item so no reader takes it for a measured quantity (D-431)."
            ),
        },
        "the_requirement": inv["the_requirement"],
        "★_the_bearing_cut": {
            "the_ruling": (
                "User, 2026-08-11, Ruling 65 of `cowork_rulings_2026_08_11_fifteenth_stop.md`, "
                "homed at CLAUDE.md's D-231 phase-1 clause as register entry D-675: the finish "
                "line is cut by D-438's own test, phase 1 completes when the INFERENCE-BEARING "
                "obligations are discharged, and the apparatus residue does not gate the "
                "completion. Its sibling, Ruling 66 / D-676, says what such a row is then OWED."
            ),
            "what_it_changes_mechanically": (
                "Each item's gate was an AUTHORED ground; it is now DERIVED, by D-438's test, with "
                "the #19 carve-out encoded rather than remembered. Nothing was added to this list "
                "and nothing removed — the scope rule reserves ADDING an item to the user, and "
                "this changes how the items are CUT, exactly as ruling R3's entry-level re-cut did "
                "for their populations."
            ),
            "the_clauses_the_cut_rests_on": grounds,
            "★_the_19_carve_out_demonstrated_on_a_member": {
                "why_a_demonstration_and_not_a_sentence": (
                    "The ruling says the exception is ENCODED IN THE CUT RATHER THAN REMEMBERED, "
                    "and prose asserting that it is encoded is exactly what 'remembered' looks "
                    "like. So the carve-out's effect is shown on the members it acts on, read off "
                    "their own recorded grounds."
                ),
                "rows_the_carve_out_keeps_inside_the_gate": app["kept_gating_only_by_the_19_carve_out"],
                "how_they_are_identified": (
                    "their recorded gate ground names principle #19 — the identifier itself, so a "
                    "ground that invokes the carve-out cannot fail to carry it"
                ),
                "of_those_the_ones_the_criterion_ALONE_would_put_OUTSIDE": app[
                    "whose_own_reason_says_the_criterion_alone_would_put_them_outside"],
                "how_THOSE_are_identified": (
                    "their own recorded reason says, in the record's own words, that the "
                    "documentation criterion alone would put them outside the gate. Those are the "
                    "members that WOULD MOVE if the carve-out were off, and they are what makes "
                    "the carve-out demonstrated rather than asserted."
                ),
                "the_others_gate_on_two_independent_grounds": (
                    "A row named above but not in the second list gates on the criterion as well "
                    "as on the exemption, and its own reason says so. It is not a demonstration of "
                    "the carve-out, and it is not counted as one."
                ),
                "and_it_is_ARMED_at_the_item_level_too": (
                    "Each item carries `★_the_bearing_cut.★_the_19_carve_out."
                    "would_this_item_move_if_the_carve_out_were_OFF`, derived per item from its own "
                    "members' grounds."
                ),
            },
            "★_the_movement_BOTH_WAYS": {
                "before_the_cut": before_the_cut,
                "after_the_cut": after_the_cut,
                "items_whose_GATE_moved": [
                    b["item"] for b, a in zip(before_the_cut, after_the_cut)
                    if b["gates"] != a["gates"]],
                "items_whose_OWED_moved": [
                    b["item"] for b, a in zip(before_the_cut, after_the_cut)
                    if b["owed"] != a["owed"]],
                "recomputed_with_the_cut_OFF": {
                    "what_that_means": (
                        "`before_the_cut` IS the recomputation: it is each item's gate as the "
                        "authored grounds gave it, carried beside the derived one on every run "
                        "rather than reconstructed from memory (#12). Comparing the two lists is "
                        "the both-ways report, and it is computed here rather than described."
                    ),
                    "nothing_else_moves": (
                        [b["item"] for b, a in zip(before_the_cut, after_the_cut)
                         if b["gates"] != a["gates"]] == []),
                    "what_that_field_means": (
                        "TRUE means the cut moved no item's GATE — the derived verdict agrees with "
                        "every authored one it replaces. That is the expected result and it is the "
                        "point rather than a disappointment: D-438's line already decided the "
                        "COMPLETE half, and the TRUE half's rows already carried per-row verdicts, "
                        "so what the cut changes is WHERE the verdict comes from and what an "
                        "un-gated item is then OWED — not which items gate. A cut that moved gates "
                        "would be the falsification test's business, and it runs regardless."
                    ),
                },
                "rows": {
                    "the_cut_authors_no_row_verdict": (
                        "Every row verdict comes from the committed apparatus declaration, which "
                        "is the ONE place a row's D-438 verdict is authored (#6). This cut reads "
                        "them and never re-decides one."
                    ),
                    "rows_the_cut_places_in_the_apparatus_class": app["non_gating_ids"],
                    "rows_the_cut_keeps_inside_the_gate": app["gates_ids"],
                    "where_a_row_that_ENTERED_or_LEFT_the_population_is_recorded": (
                        "tools/audit/nongating_apparatus_rows.json → `retired_verdicts` (a row "
                        "that closed) and `superseded_verdicts` (a row a user ruling re-classed). "
                        "Both are kept whole there (#12) and neither is restated here (D-431)."
                    ),
                },
            },
            "the_falsification_test": falsification,
            "the_lapse_population": lapse,
            "what_the_cut_does_NOT_do": [
                "It adds nothing to this list and removes nothing from it — an addition is a user "
                "ruling by the scope rule's own terms.",
                "It moves no row's D-438 verdict and edits no authored apparatus table.",
                "It closes no row and moves no status cell: a lapse is not a resolution.",
                "It authorizes no fix, no design and no inference change, and it writes no portion "
                "of phase 1's completion statement.",
            ],
        },
        "★_the_entry_level_re_cut": {
            "the_ruling": THE_ENTRY_LEVEL_RE_CUT_RULING,
            "★_re_cutting_an_existing_item_is_NOT_adding_one": (
                "Stated here so a later reader does not mistake this for a scope change. The scope "
                "rule reserves ADDING an item to the user, and says in its own words that this list "
                "is regenerated rather than maintained and that 'an item's size moves when the "
                "record moves'. R3 changes what an existing item's population IS. No item is added, "
                "none is removed, and every closing act is unchanged."
            ),
            "what_was_wrong_with_the_document_cut": (
                "The four homing items took their populations from the DELEGATION partition, which "
                "classifies by the entry's HOME DOCUMENT — is that document named in a "
                "user-ratified surface, and in what form. That is the right cut for the question "
                "*does a delegation exist* and the wrong one for the question criterion C1 asks, "
                "which is per DECISION. An entry whose obligation an entry-level ruling has already "
                "discharged stayed in the count, because its home document's delegation state had "
                "not moved."
            ),
            "direction_1_entries_the_entry_cut_DROPS": {
                "count": entry_discharged,
                "ids_by_item": {
                    it["name"]: it["population"]["discharged_by_an_entry_level_ruling"]
                    for it in homing_items
                    if it["population"]["discharged_by_an_entry_level_ruling"]},
                "the_ruling_that_discharges_them": disch["the_ruling_that_discharges_them"],
                "ground_per_entry": disch["ground_per_id"],
                "read_off": disch["source"],
                "discharged_but_NOT_found_in_any_item": unaccounted,
                "what_that_field_means_if_it_is_non_empty": (
                    "The ruling discharged an entry the document cut no longer carries at all — it "
                    "left the gap class by some other act. Reported rather than stopped: it is not "
                    "a disagreement, it is the same entry leaving by two routes."
                ),
            },
            "direction_2_what_the_entry_cut_SURFACES_that_the_document_cut_cannot_carry": {
                "the_finding": (
                    "One owed act has no register entry to hang on, so no register-derived "
                    "population can carry it. R1's application records it: one supersession names "
                    "its successor as an INCREMENT by its open-items row rather than as a decision "
                    "by its identifier, so there is no home field to read and the act owed FIRST is "
                    "a NAMING — which recorded decision carries that content — before any homing "
                    "question can be put."
                ),
                "where_it_is_recorded": (
                    "tools/audit/decisions/r1_superseded_reach.json → "
                    "★_what_discharging_the_dispatch_ASSUMPTION_found → "
                    "3_a_successor_can_be_named_by_something_that_is_not_a_register_entry, and the "
                    "entry's own row note. No identifier is nominated there and none is nominated "
                    "here — the tool's own STOP forbids naming a successor the record does not."
                ),
                "★_it_is_NOT_added_as_an_item": (
                    "Adding an item to this list requires a USER RULING, by the scope rule's own "
                    "terms, and R3 authorized a re-cut rather than an addition. It is surfaced here "
                    "and left."
                ),
                "the_other_half_of_direction_2_checked_and_empty": (
                    "No entry-level ruling ADDS a register entry to the homing population: both "
                    "rulings in force (D-642, D-644) discharge or re-route, and neither creates an "
                    "obligation for an entry the gap class does not already hold. Checked rather "
                    "than assumed — the re-cut's own STOP would fire if the two cuts failed to "
                    "account for each other."
                ),
            },
            "what_the_re_cut_does_NOT_move": (
                "No entry's home, class or status; no closing act; no gate verdict; and not the "
                "TRUE half, whose population is open-items ROWS and was never cut by document."
            ),
        },
        "the_re_reading_of_the_clause": THE_RE_READING,
        "the_requirement_that_is_a_condition_rather_than_an_item": THE_CONDITION_NOT_AN_ITEM,
        "THE_FINISH_LINE": items,
        "the_rows_that_are_user_rulings": ROWS_THAT_ARE_USER_RULINGS,
        "the_scope_rule": THE_SCOPE_RULE,
        "the_register_account_of_itself": {
            "why_it_is_here": (
                "A completion statement rests on DECISIONS.md. The inventory checks three "
                "statements the register publishes about itself; all three read TRUE AT HEAD, so "
                "this is a discharged requirement rather than an item. OPEN_ITEMS.md OI-334 is "
                "closed."
            ),
            "verdicts": {
                k: v["verdict"]
                for k, v in inv["what_the_register_says_about_itself_that_is_no_longer_true"].items()
                if k.startswith("statement_")
            },
        },
        "the_reads_are_done": {
            "note": (
                "Recorded because it is the one large phase-1 obligation that IS discharged, and a "
                "finish line that listed only what remains would misrepresent the position."
            ),
            "owed_set_is_empty": inv["the_reads_are_done"]["the_owed_set_is_empty"],
            "read_in_full_after_wave_6": inv["the_reads_are_done"]["read_in_full_after_wave_6"],
            "derived_from": inv["the_reads_are_done"]["derived_here_rather_than_asserted"],
        },
        "counted": {
            "items_on_the_finish_line": len(items),
            "items_that_gate": sum(1 for i in items if i["gate"]["gates"]),
            "★_items_that_gate_is_now_the_BEARING_CUT's_figure": (
                "The user's Ruling 65 of 2026-08-11. It counts the items phase 1's completion "
                "waits on — the inference-bearing ones — and no longer the items that merely "
                "remain. The count before the cut is at "
                "`★_the_bearing_cut.★_the_movement_BOTH_WAYS.before_the_cut` (#12)."
            ),
            "items_that_are_still_OWED": sum(
                1 for i in items if i["★_the_bearing_cut"]["owed"]),
            "items_whose_obligation_has_LAPSED": sum(
                1 for i in items if not i["★_the_bearing_cut"]["owed"]),
            "open_rows_whose_obligation_has_LAPSED": lapse["count"],
            "of_those_whose_lapse_record_is_written": lapse["lapse_records_written"]["count"],
            "register_entries_owed_a_home": total_entries,
            "register_entries_owed_a_defense": defense_total,
            "open_rows_owed_on_the_true_half_that_gate": split["gates"]["count"],
            "open_rows_the_cut_places_in_the_apparatus_class": split["non_gating"]["count"],
            "★_this_field_was_renamed_2026-08-11_and_the_former_name_is_kept": (
                "It read `open_rows_owed_a_reach_verdict` (#12). That became FALSE on 2026-08-11: "
                "the reach derivation ran over the whole set, so no row is owed a reach verdict "
                "any more, and under the user's Ruling 66 these rows are owed nothing at all. The "
                "count is unchanged; only what it is called is."
            ),
            "items_with_a_closing_route_only_the_user_may_take": sum(
                1 for i in items if "the user only" in i["who_may_perform_it"]
                or i["who_may_perform_it"].startswith("the user")),
            "★_that_count_is_items_not_acts": (
                "It counts items at least ONE of whose closing routes is the user's — not items "
                "the user alone can close. Items offering a user route and a session route are in "
                "it, because a reader deciding what to commission needs to see them."
            ),
            "register_entries_owed_a_home_at_document_granularity": homing_covered + unhomed_total,
            "register_entries_discharged_by_an_entry_level_ruling": entry_discharged
                                                                    + unhomed_discharged,
            "★_which_of_those_two_figures_is_the_finish_line": (
                "The entry-level one, on ruling R3. The document-granularity figure is kept beside "
                "it so the movement is visible rather than inferred (#12), and it is the figure "
                "this artifact published before the re-cut."
            ),
            "reconciliation": {
                "homing_items_cover_the_documentation_gap_class": homing_covered == gap_total,
                "entry_cut_plus_discharged_covers_the_documentation_gap_class":
                    entry_covered + entry_discharged == gap_total,
                "unhomed_item_kept_plus_discharged_covers_the_register_unhomed_class":
                    unhomed_kept + unhomed_discharged == unhomed_total,
                "true_half_items_cover_the_wide_cut": rows_covered == wide_total,
                "every_item_carries_a_closing_act": True,
            },
        },
    }


def main(argv: list[str]) -> int:
    art = build()
    text = json.dumps(art, indent=1, ensure_ascii=False) + "\n"
    if "--check" in argv:
        if not OUT.exists():
            print("FAIL: artifact missing:", OUT)
            return 1
        if OUT.read_text(encoding="utf-8") != text:
            print("FAIL: re-derivation differs from the committed artifact:", OUT)
            return 1
        print("OK: the phase-1 finish line re-derives byte-identically.")
        return 0
    OUT.write_text(text, encoding="utf-8")
    c = art["counted"]
    print("wrote", OUT)
    print(f"  {c['items_on_the_finish_line']} item(s), {c['items_that_gate']} gating, "
          f"{c['items_whose_obligation_has_LAPSED']} lapsed")
    print(f"  register entries owed a home: {c['register_entries_owed_a_home']}; "
          f"owed a defense: {c['register_entries_owed_a_defense']}")
    print(f"  open rows owed on the true half that gate: "
          f"{c['open_rows_owed_on_the_true_half_that_gate']}; "
          f"in the apparatus class: "
          f"{c['open_rows_the_cut_places_in_the_apparatus_class']}")
    print(f"  open rows whose obligation has LAPSED: "
          f"{c['open_rows_whose_obligation_has_LAPSED']}; lapse records written: "
          f"{c['of_those_whose_lapse_record_is_written']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
