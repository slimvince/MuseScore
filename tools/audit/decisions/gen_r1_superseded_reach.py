#!/usr/bin/env python3
"""Apply ruling R1 — C1's reach over SUPERSEDED entries — to finish-line item 1's NO-HOME class.

THE RULING (user, 2026-08-04, dispatch `cc_instruction_c1_ruling_and_item1c.md` §0a, R1) is
RECORDED, with the clause it rests on and the basis it withdraws, at the one place the C1 criteria
live: `tools/audit/phase1_completion_inventory.json` → `the_requirement.criteria` → C1 →
`★_the_reach_of_C1_over_SUPERSEDED_entries`.  It is not restated here (#6).  THIS file APPLIES it.

WHAT R1 TURNS ON, and therefore what this tool must establish per entry: a superseded decision's
live content lives in its SUCCESSOR, and C1 is satisfied for that content only WHERE THE SUCCESSOR
IS HOMED.  So the question is not whether an entry is superseded — it is whether the record names a
successor for its live content, and whether that successor is homed.

DERIVED — the population (imported from the item-1 route table, never re-listed, #6); each entry's
          status; each named successor's home, home class and HOMED verdict, read off the register's
          own home classes; and the disposition, which is a function of those verdicts.
AUTHORED — the SUCCESSOR LIST per entry.  Which entry carries a superseded entry's live content is a
          judgment, so it is authored — but it is authored against the record rather than from it:
          every successor must be NAMED IN THE SUPERSEDED ENTRY'S OWN TEXT, and the tool STOPS if it
          is not.  A session may not nominate a successor the register does not name.

THE FOUR STOPS:
  1. a member of the derived NO-HOME class with no authored successor record — an entry cannot be
     silently left undecided by the ruling that was made for it;
  2. an authored successor record for an entry the class does not carry — the register moving under
     the table;
  3. an authored successor whose `named_as` string is NOT found in the superseded entry's own
     `superseded_by`, `rationale` or `status_source` — this session naming a successor the record
     does not;
  4. an authored successor resolved to a register id the register does not hold.

WHAT THIS FILE DOES NOT DO.  It moves no entry's home, class or status; it regenerates no register
data; it authorizes no fix, design or inference change.  It records a disposition per entry and the
counts that follow from it.

Usage:
    python tools/audit/decisions/gen_r1_superseded_reach.py           # write the artifact
    python tools/audit/decisions/gen_r1_superseded_reach.py --check   # re-derive, exit 1 on drift
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

from output_encoding import use_utf8_output                       # noqa: E402  (path set above)
from gen_finish_line_item1_routes import build as build_routes, NO_HOME   # noqa: E402  (#6)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

REGISTER = HERE / "backbone_decisions.json"
OUT = HERE / "r1_superseded_reach.json"

# ── authored: what "homed" means, READ OUT OF the C1 criterion rather than decided here ─────────
# The mapping is authored; what it is applied to — each entry's home class — is read off the
# register. Marked authored because a reader must not take it for a measured quantity (D-431).
# Taken from the C1 criterion's own words at `the_requirement.criteria`: "`process` and
# `project-convention` are declared CORRECTLY homed and are not outstanding; `contract-home` is the
# fifth home case, admitted by D-430/D-432/D-546", against "`gap` … and `unhomed` … no home at all".
HOMED_KINDS = {"process", "project-convention", "contract-home"}
NOT_HOMED_KINDS = {"gap", "unhomed"}

SUPERSEDED_STATUSES = {"superseded-by", "superseded-in-fact"}

LEAVES = "LEAVES ITEM 1 — correctly homed already (the register plus the successor's home)"
ROUTE_CHANGES = "STAYS IN ITEM 1, ROUTE CHANGED — the owed act is homing the SUCCESSOR"
NEITHER = "NEITHER — R1 does not discharge this entry"


# ── authored: the successor list per entry of the NO-HOME class ────────────────────────────────────
#
# `successors`   : each is {register_id, named_as}. `named_as` MUST occur in the superseded entry's
#                own text (STOP 3). `register_id` None means the record names a successor that is not
#                a register entry, so its home cannot be derived — the entry is NOT discharged.
# `why`        : why R1 reaches or does not reach this entry.
# `note`       : optional. Anything found while checking that a later reader would otherwise
#                re-derive — never a substitute for a successor the record does not name.
SUCCESSORS: dict[str, dict] = {

    # ---- superseded meta-findings, successors named in `superseded_by` -----------------------
    "D-282": {
        "successors": [{"register_id": "D-115", "named_as": "D-115"},
                     {"register_id": "D-191", "named_as": "D-191"}],
        "why": "The register names both successors in its own `superseded_by` field, 'D-115 and "
               "D-191', and the entry's rationale states what each carries.",
    },
    "D-283": {
        "successors": [{"register_id": "D-001", "named_as": "D-001"},
                     {"register_id": "D-096", "named_as": "D-096"}],
        "why": "`superseded_by` reads 'D-001 and D-096', and the rationale states the supersession "
               "stands on dates and explicitness — both are later, explicit and user-ratified on "
               "the same subject.",
    },
    "D-284": {
        "successors": [{"register_id": "D-036", "named_as": "D-036"},
                     {"register_id": "D-001", "named_as": "D-001"},
                     {"register_id": "D-010", "named_as": "D-010"}],
        "why": "`superseded_by` reads 'D-036 with D-001/D-010' — D-036 carries the standing "
               "doctrine, and the other two retired the mechanism the finding warned about.",
    },
    "D-285": {
        "successors": [
            {"register_id": "D-004", "named_as": "D-004"},
            {"register_id": "D-426", "named_as": "D-426"},
        ],
        "why": "`superseded_by` reads 'the ratified factorization emission design (D-004 and D-426, "
               "the OI-194 ornament-label increment)'. BOTH successors are register entries the "
               "record names, so STOP 3 is satisfied for each: D-004 is homed in a layer "
               "specification, and D-426 — named by the USER on 2026-08-07 as the recorded decision "
               "carrying the increment half — is not, so R1's condition is still not discharged for "
               "the whole of this entry's content and the owed act is homing D-426.",
        "note": "★ THE NAMING GAP THIS RECORD REPORTED IS CLOSED BY A USER RULING, AND WHAT THE "
                "RECORD FORMERLY SAID IS KEPT WHOLE (#12). The user ruled on 2026-08-07 (dispatch "
                "`cc_instruction_five_rulings.md` §0a R2) that D-426 is the recorded decision "
                "carrying 'the OI-194 increment', and the register's `superseded_by` now names it — "
                "so the successor is derivable and no session had to nominate one. Before that "
                "ruling this record read, verbatim: \"A search of the register finds ONE entry whose "
                "subject is that increment — the one recording that the ornament labels get their "
                "own increment with the tracking row created at ruling time. It is NOT named here as "
                "the successor and does NOT drive the disposition: identifying it would be this "
                "session nominating a successor the record does not name, which STOP 3 exists to "
                "prevent. Reported so the next reader does not re-derive it, and so that whoever "
                "rules can see that the gap is a NAMING gap rather than an absent successor.\" The "
                "candidate that record declined to name is the one the user has now named, which is "
                "the STOP working rather than being circumvented: the search was reported, the "
                "naming was left to the user, and the ruling supplied it. WHAT THE RULING DID NOT "
                "CHANGE: the disposition. D-426 is unhomed, so this entry still STAYS IN ITEM 1 with "
                "its route on the successor side — what moved is that the act owed first is no "
                "longer a naming but the homing of a named entry.",
    },

    # ---- ruled superseded 2026-08-07, successors named in `superseded_by` ---------------------
    "D-538": {
        "successors": [{"register_id": "D-177", "named_as": "D-177"},
                     {"register_id": "D-115", "named_as": "D-115"}],
        "why": "Ratified and ruled SUPERSEDED in the same act (user, 2026-08-07, ruling R2). The "
               "register names both successors in its own `superseded_by` field, 'D-177 and "
               "D-115', and — the reason a session had nothing to nominate — the entry's "
               "status_source had already named exactly these two in prose, BEFORE the ruling: "
               "'an early, concrete form of the discipline the project later stated generally — "
               "one revertible provenance-stamped commit per behaviour change (#14) and a "
               "measured non-increase before proceeding (the gate block (A) hard stop)'.",
        "note": "⚠ LEGACY SUBJECT, and the mark is what makes the excluded alternative matter. "
                "The user's ruling records why this entry is NOT homed beside gate block (A): "
                "that would put a second copy of in-force discipline into a live specification "
                "(#6), under a LEGACY subject a reader could misapply to the live solution. So "
                "the early concrete form stays in the register verbatim (#12) and the obligation "
                "moves to the successors under D-642 — which is this file's own construction, "
                "arrived at here by a RULING rather than by a supersession the record already "
                "carried.",
    },

    # ---- superseded-in-fact: `superseded_by` is empty by construction, and the record names the
    # ---- successor (or does not) in the status_source prose instead --------------------------------
    "D-579": {
        "successors": [{"register_id": "D-001", "named_as": "D-001"}],
        "why": "Recorded superseded-in-fact, so no ruling names a successor and `superseded_by` is "
               "empty. The register's own status_source names the successor in terms: 'The "
               "obligation was met by replacement rather than by repair: the production arm is now "
               "one joint decode over key, mode, chord and segmentation together (D-001), which is "
               "the ordering this step asked for arrived at by a different route.'",
    },
    "D-571": {
        "successors": [{"register_id": "D-528", "named_as": "D-528"},
                     {"register_id": "D-450", "named_as": "D-450"}],
        "why": "Superseded-in-fact on the legacy key path. The status_source names what carries "
               "the live content on the production arm: the joint estimator 'takes the signature "
               "and declared mode as a weak fitted soft prior with no conditional gate anywhere "
               "(D-528), and conditions the initial key state only (D-450)'.",
        "note": "One of the two successors, D-450, is ITSELF a member of finish-line item 1 — its "
                "own route is RE-HOME and its home class is `gap`. That is the case R1's second "
                "half was written for, arrived at from the other direction: the owed act is homing "
                "the successor, and here the successor is already carried by the same item.",
    },
    # ---- members of the NO-HOME class R1 does not reach: their status is LIVE ------------------
    "D-498": {"successors": [], "why": "Status LIVE. R1 governs entries whose content is superseded; "
                                     "this one records that a PRODUCT STANCE IS OWED, which is "
                                     "live and undecided rather than superseded."},
    "D-499": {"successors": [], "why": "Status LIVE. Four documentation riders, owed rather than "
                                     "superseded."},
    "D-453": {"successors": [], "why": "Status LIVE. A desk simulation's verdict — a finding about a "
                                     "stage that has run, not a superseded rule."},
    "D-535": {"successors": [], "why": "Status LIVE. The checking stage's verdict, same shape as "
                                     "D-453."},
    "D-610": {"successors": [], "why": "Status LIVE. A completed refactor's zero-churn property."},
    "D-569": {"successors": [], "why": "Status LIVE. Held by the user's ruling of 2026-08-04 that "
                                     "its document is not a delegation target; that ruling did not "
                                     "put the re-homing question and R1 does not answer it."},
    "D-570": {"successors": [], "why": "Status LIVE. Same ruling and same reason as D-569."},

    # ── THE THREE THAT ENTERED THIS CLASS ON 2026-08-11, each by its own user ruling ────────────
    #
    # They arrive here for a reason the class has not carried before, and it is worth stating once
    # rather than three times: the members above are here because their live content is SUPERSEDED
    # and carried by a successor, or because there is no decision content at all. These three are
    # here because the user ruled that their content, though live and correctly recorded, IS NOT A
    # RULE A SPECIFICATION SECTION STATES — an adoption event, a per-corpus establishment verdict,
    # and the evidence half of a split entry. R1 governs SUPERSEDED content and does not reach any
    # of them, which their dispositions below say in the tool's own derived words; what closes them
    # is the ruling recorded on each route row, not this file. They are recorded here because this
    # class's population is derived from the route table and a member with no successor record is
    # a STOP — an entry may not be left silently undecided by the ruling made for it.
    "D-516": {"successors": [], "why": "Status LIVE. Ruling 44 of 2026-08-09 (user) closed it as an "
                                     "ADOPTION EVENT for which no home is owed, its evidence "
                                     "pointed at the §8c needs table where the adoption happened. "
                                     "R1 governs entries whose content is superseded; this content "
                                     "is neither superseded nor a rule."},
    "D-475": {"successors": [], "why": "Status LIVE. Ruling 46 of 2026-08-09 (user) recorded it as a "
                                     "STATUS-CLASS entry — a per-corpus establishment verdict is "
                                     "the same kind as supersession and shelving, so the register "
                                     "itself is its home and no specification home is owed. R1 does "
                                     "not reach it: what is superseded here is nothing, and the "
                                     "verdict's own route and exhaustion rule live at OI-179."},
    "D-613": {"successors": [], "why": "Status LIVE. Ruling 47 of 2026-08-09 (user) SPLIT the entry; "
                                     "the intake-rule half is D-665 and is homed in the census, "
                                     "and THIS half — the confirmed absence — stays at the "
                                     "needs-vector row that already carries it, as evidence, so no "
                                     "home is owed. A split is not a supersession and R1 does not "
                                     "reach it."},
}


# ── RETIRED successor records — kept whole, never deleted (#12) ──────────────────────────────────
#
# An entry leaves this class when something CLOSES it, and the record of what was found while it
# was here is evidence about the ruling, not scaffolding. It is moved rather than deleted, for the
# reason the guard-classification table gives for its own retired verdicts: a reasoning deleted is
# a reasoning the next session re-derives.
RETIRED: dict[str, dict] = {
    "D-572": {
        "retired_on": "2026-08-04",
        "retired_by": "Ruling R2 / register entry D-644 (dispatch "
                      "`cc_instruction_guard_fix_and_item1d.md`, Task 2.2), which answered exactly "
                      "the shape this record found R1 silent on.",
        "what_this_record_found_PRESERVED_VERBATIM": {
            "successors": [],
            "why": "Superseded-in-fact, and the record names NO successor for its content. What the "
                   "entry records is a REMOVAL — the hard post-hoc declared-mode promotion taken out "
                   "outright rather than kept in a gated form — so there is no later decision that "
                   "states the same rule. The status_source names two other entries, and neither is a "
                   "successor: D-571 is named as landing at the same event, and D-058 as a separate "
                   "removal for which this document is a second source.",
            "note": "R1 is silent on this shape. Its condition is that the live content LIVES IN a "
                    "successor; where the record names none, the application reports that and "
                    "proposes nothing. Whether an entry recording a removal is owed a home at all is "
                    "not decided here and is not decided by R1.",
        },
        "★_the_finding_was_correct_and_is_what_produced_the_ruling": (
            "The note above says R1 is silent on this shape and proposes nothing. That was the "
            "right answer under the rulings then in force, and it is the finding the user ruled on: "
            "D-644 says that where the content is a REMOVAL the owning specification states the "
            "current behaviour and records the removal as a tried-and-closed line — precedent, not "
            "a new rule, the act having already been performed at `ARCHITECTURE.md` §5.2 for the "
            "sibling removal that landed at the same increment (D-058). The entry is now homed "
            "there and its route is RE-HOME, so it is no longer in this class."
        ),
    },
}


def register() -> dict[str, dict]:
    data = json.loads(REGISTER.read_text(encoding="utf-8"))
    return {e["id"]: e for e in data["decisions"]}


def homed_verdict(entry: dict) -> dict:
    """Is this entry homed? Derived from the register's own home classes, never authored."""
    kind = entry.get("nonspec_kind")
    if entry.get("home_is_layer_spec"):
        return {"homed": True,
                "because": "home_is_layer_spec — written into a layer specification"}
    if kind in HOMED_KINDS:
        return {"homed": True,
                "because": f"home class `{kind}` — declared correctly homed by the C1 criterion"}
    if kind in NOT_HOMED_KINDS:
        return {"homed": False,
                "because": f"home class `{kind}` — C1's own outstanding population"}
    return {"homed": False,
            "because": f"home class `{kind}` is not one the C1 criterion classifies; treated as "
                       "NOT homed, because a successor whose home cannot be established cannot "
                       "discharge C1 for the entry that points at it (#19)"}


def build() -> dict:
    routes = build_routes()
    reg = register()

    class_rows = [r for r in routes["rows"]
                  if r["route"] == NO_HOME and not r["closed_by_this_wave"]]
    pop = [r["id"] for r in class_rows]

    missing = sorted(i for i in pop if i not in SUCCESSORS)
    if missing:
        raise SystemExit(
            "STOP: members of item 1's NO-HOME class with no authored successor record: "
            + ", ".join(missing) + ". An entry cannot be left undecided by the ruling made for it.")
    stray = sorted(i for i in SUCCESSORS if i not in pop)
    if stray:
        raise SystemExit(
            "STOP: authored successor records for entries the NO-HOME class does not carry: "
            + ", ".join(stray) + " — the register has moved under the table.")
    # A RETIRED record must name an entry this class no longer carries, and must not also be live.
    # Both directions, so the retired table cannot quietly become a second live table or a
    # graveyard for entries that are still owed a disposition here.
    back = sorted(i for i in RETIRED if i in pop)
    if back:
        raise SystemExit(
            "STOP: retired successor record(s) for entries the NO-HOME class carries again: "
            + ", ".join(back) + ". An entry that returns to this class needs a live disposition, "
            "not a retirement note.")
    both = sorted(i for i in RETIRED if i in SUCCESSORS)
    if both:
        raise SystemExit(
            "STOP: entr(ies) recorded both live and retired: " + ", ".join(both) + ".")

    rows = []
    for r in class_rows:
        eid = r["id"]
        entry = reg[eid]
        authored = SUCCESSORS[eid]
        # The three fields that record what the REGISTER says about this entry's supersession.
        # `plain` is deliberately excluded: it is the register's own restatement of the decision,
        # not the record's naming of a successor, so admitting it would let the restatement
        # supply the fact the STOP exists to demand from the record.
        own_text = " ".join(str(entry.get(f) or "")
                            for f in ("superseded_by", "rationale", "status_source"))

        successors = []
        for c in authored["successors"]:
            if c["named_as"] not in own_text:
                raise SystemExit(
                    f"STOP: {eid}'s authored successor {c['named_as']!r} is not named in the entry's "
                    "own superseded_by / rationale / status_source. A session may not nominate a "
                    "successor the record does not name.")
            rid = c["register_id"]
            if rid is not None and rid not in reg:
                raise SystemExit(
                    f"STOP: {eid}'s authored successor resolves to {rid}, which the register does "
                    "not hold.")
            rec = {
                "named_as": c["named_as"],
                "register_id": rid,
                "named_in": ("superseded_by" if c["named_as"] in str(entry.get("superseded_by") or "")
                             else "the entry's own rationale / status_source prose"),
            }
            if rid is None:
                rec.update({
                    "home": None,
                    "home_class": None,
                    "homed": False,
                    "because": "named by the record, but not as a register entry — its home cannot "
                               "be derived, so it cannot discharge C1 for the entry pointing at it",
                })
            else:
                ce = reg[rid]
                rec.update({
                    "home": ce["home"],
                    "home_class": ce.get("nonspec_kind") or "homed-in-a-layer-specification",
                    "status": ce.get("status"),
                    **homed_verdict(ce),
                })
            successors.append(rec)

        status = entry.get("status")
        if status not in SUPERSEDED_STATUSES:
            disposition, ground = NEITHER, (
                f"R1 DOES NOT REACH IT: the entry's status is `{status}`, and R1 governs entries "
                "whose content is superseded.")
        elif not successors:
            disposition, ground = NEITHER, (
                "R1's CONDITION IS NOT DISCHARGEABLE: the entry is superseded, but the record "
                "names no successor carrying its live content. R1 is silent on that shape and "
                "nothing is proposed.")
        elif all(c["homed"] for c in successors):
            disposition, ground = LEAVES, (
                "Every successor the record names is homed, so C1 is satisfied for this entry's live "
                "content at the successor's home, and the supersession itself is register "
                "business — which D-231's clause assigns to the register.")
        else:
            unhomed = [c for c in successors if not c["homed"]]
            named = [c["register_id"] for c in unhomed if c["register_id"]]
            unresolved = [c["named_as"] for c in unhomed if not c["register_id"]]
            ground = ("At least one successor is NOT homed, so C1 is defeated and the owed act is on "
                      "the SUCCESSOR side rather than on this entry. ")
            if named:
                ground += "Home the successor: " + ", ".join(named) + ". "
            if unresolved:
                ground += ("What the record names — " + ", ".join(unresolved) + " — is not a "
                           "register entry, so the act owed FIRST is a naming: which recorded "
                           "decision carries it. That is not settled here, for the reason the "
                           "entry's note gives.")
            disposition, ground = ROUTE_CHANGES, ground.strip()

        row = {
            "id": eid,
            "title": entry["title"],
            "status": status,
            "home_at_HEAD": entry["home"],
            "home_class": entry.get("nonspec_kind") or "homed-in-a-layer-specification",
            "route_before_R1": r["route"],
            "superseded_by_field": entry.get("superseded_by"),
            "successors": successors,
            "disposition": disposition,
            "disposition_ground": ground,
            "why_these_successors": authored["why"],
            "authored": "the successor list and its reason. The status, every successor's home and "
                        "home class, the HOMED verdict and the disposition are derived.",
        }
        if authored.get("note"):
            row["note"] = authored["note"]
        rows.append(row)

    leaves = [r for r in rows if r["disposition"] == LEAVES]
    changed = [r for r in rows if r["disposition"] == ROUTE_CHANGES]
    neither = [r for r in rows if r["disposition"] == NEITHER]

    # Derived over the WHOLE register, so finding 1 below is a measured property of the data
    # rather than an impression taken from the fourteen entries this file dispositions.
    by_status: dict[str, dict] = {}
    for st in sorted(SUPERSEDED_STATUSES):
        members = [e for e in reg.values() if e.get("status") == st]
        by_status[st] = {
            "entries": len(members),
            "carrying_a_populated_superseded_by_field":
                len([e for e in members if e.get("superseded_by")]),
        }
    field_population = {
        "what_was_measured": "for each superseded status in the register, how many of its entries "
                             "carry a populated `superseded_by` field",
        "by_status": by_status,
        "why_it_matters": "The field is populated exactly where a RULING named the successor. "
                          "Where supersession was recorded as a matter of fact, the field is "
                          "empty and the successor — if there is one — is named only in prose.",
    }

    # Derived, so the report cannot imply that the NO-HOME class exhausts R1's reach.
    other_superseded = sorted(
        {r["id"] for r in routes["rows"]
         if not r["closed_by_this_wave"] and r["route"] != NO_HOME
         and reg[r["id"]].get("status") in SUPERSEDED_STATUSES})

    return {
        "purpose": (
            "Ruling R1 APPLIED to finish-line item 1's NO-HOME class: per entry, the successor the "
            "record names for its live content, whether that successor is homed, and what follows. "
            "NOT a completion statement, and not an authorization for any fix, design or inference "
            "change."
        ),
        "generated_by": "tools/audit/decisions/gen_r1_superseded_reach.py",
        "generated_for": "cc_instruction_c1_ruling_and_item1c.md (Task 2, ruling R1)",
        "the_ruling_is_recorded_elsewhere_and_is_not_restated_here": (
            "tools/audit/phase1_completion_inventory.json → the_requirement.criteria → C1 → "
            "★_the_reach_of_C1_over_SUPERSEDED_entries, which carries R1's text, the sentence of "
            "D-231's clause it rests on, and the WITHDRAWN OI-272 basis with the four grounds that "
            "refuted it (#6, #12)."
        ),
        "derived_at_head_from": [
            "tools/audit/decisions/gen_finish_line_item1_routes.py → build() (imported, #6)",
            "tools/audit/decisions/backbone_decisions.json — statuses, homes and home classes",
        ],
        "what_is_authored_and_what_is_derived": {
            "derived": "the population, each entry's status and home class, every successor's home "
                       "and HOMED verdict, the disposition, and every count",
            "authored": "the SUCCESSOR LIST per entry and its reason",
            "how_the_authored_half_is_bounded": (
                "Every successor must be NAMED IN THE SUPERSEDED ENTRY'S OWN TEXT — its "
                "`superseded_by`, its rationale or its status_source — and the tool STOPS on one "
                "that is not. So the judgment is which of the entries the record names is the "
                "successor, never which entry ought to be."
            ),
        },
        "★_what_discharging_the_dispatch_ASSUMPTION_found": {
            "the_assumption": (
                "A2 of `cc_instruction_c1_ruling_and_item1c.md`: 'That every member of item 1's "
                "no-home superseded class HAS a homed successor. This is not established — R1's "
                "application turns on it per entry.'"
            ),
            "verdict": "REFUTED IN PART, and the part that is refuted is the useful half.",
            "1_the_successor_field_is_not_where_the_successor_is": {
                "the_finding": (
                    "An entry recorded `superseded-in-fact` carries an EMPTY `superseded_by` — by "
                    "construction, since no ruling names a successor — and the register names the "
                    "successor in its status_source PROSE instead, or names none at all. A "
                    "derivation that had read the `superseded_by` field alone would have reported "
                    "every such entry as having no successor, which is false for most of them."
                ),
                "measured_over_the_WHOLE_register_not_this_class": field_population,
            },
            "2_a_successor_can_itself_be_unhomed_and_one_is": (
                "This is the case R1's second half was written for, and the class contains it: a "
                "successor that is itself a member of finish-line item 1, class `gap`. The owed act "
                "there is homing the successor, and the successor is already in the same item."
            ),
            "3_a_successor_can_be_named_by_something_that_is_not_a_register_entry": (
                "One entry's supersession named an INCREMENT by its open-items row rather than a "
                "decision by its identifier, so its home could not be derived at all. R1's "
                "condition turns on the successor being HOMED, and a successor that is not a "
                "register entry has no home field to read. ★ THE USER RULED IT on 2026-08-07 "
                "(dispatch `cc_instruction_five_rulings.md` §0a R2): D-426 is the recorded decision "
                "carrying that increment, and the register's `superseded_by` now names it, so the "
                "successor is derivable. The finding stands as the reason a naming was owed at all; "
                "what it reported is preserved in that entry's own note (#12). It did NOT change "
                "the disposition — the newly named successor is itself unhomed, so the entry keeps "
                "its route on the successor side."
            ),
            "4_a_superseded_entry_can_have_no_successor_because_the_content_is_not_live": (
                "One entry records a REMOVAL. Nothing later states the rule it states, because "
                "there is no rule left to state. R1 was silent on that shape and this file "
                "proposed nothing for it. ★ THE USER RULED IT on 2026-08-04 — register entry "
                "D-644: where the content is a REMOVAL the owning specification states the current "
                "behaviour and records the removal as a tried-and-closed line, which is precedent "
                "rather than a new rule. The entry left this class when that act was performed; "
                "its record here is RETIRED WHOLE rather than deleted, at `retired_records` below."
            ),
        },
        "retired_records": {
            "what_this_is": (
                "Successor records for entries this class no longer carries, kept whole (#12). An "
                "entry leaves when something CLOSES it, and what was found while it was here is "
                "evidence about the ruling rather than scaffolding — a reasoning deleted is a "
                "reasoning the next session re-derives."
            ),
            "count": len(RETIRED),
            "records": RETIRED,
        },
        "the_homed_test": {
            "homed_if": "home_is_layer_spec is true, or the home class is one of "
                        + ", ".join(f"`{k}`" for k in sorted(HOMED_KINDS)),
            "not_homed_if": "the home class is one of "
                            + ", ".join(f"`{k}`" for k in sorted(NOT_HOMED_KINDS)),
            "source": "the C1 criterion's own words at "
                      "tools/audit/phase1_completion_inventory.json → the_requirement.criteria",
            "what_is_authored_here_and_what_is_not": (
                "The MAPPING from home class to homed/not-homed is authored, read out of that "
                "criterion. Which class each entry carries is DERIVED, read off the register. No "
                "entry's class is judged or changed here."
            ),
        },
        "counted": {
            "no_home_class_population": len(rows),
            "entries_that_LEAVE_item_1": len(leaves),
            "entries_whose_ROUTE_CHANGES_to_home_the_successor": len(changed),
            "entries_that_do_NEITHER": len(neither),
            "of_which_R1_does_not_reach_because_the_status_is_live":
                len([r for r in neither if r["status"] not in SUPERSEDED_STATUSES]),
            "of_which_superseded_with_no_successor_the_record_names":
                len([r for r in neither if r["status"] in SUPERSEDED_STATUSES]),
            "ids_that_leave": [r["id"] for r in leaves],
            "ids_whose_route_changes": [r["id"] for r in changed],
        },
        "★_the_one_thing_this_application_does_NOT_move": {
            "what": (
                "The DERIVED population of finish-line item 1 at "
                "`tools/audit/phase1_finish_line.json`, which still carries every entry above."
            ),
            "why": (
                "That population is derived from the DOCUMENT-level delegation partition — "
                "entries whose home document is named in no user-ratified surface — while R1 is an "
                "ENTRY-level clause about which entries criterion C1 reaches. The two are "
                "different cuts, and subtracting R1's discharged entries from the derived item "
                "would mean changing what that generator derives."
            ),
            "what_is_therefore_reported_rather_than_done": (
                "The entries above are recorded as leaving item 1 by R1's own terms, and the count "
                "is here. Reconciling the derived item with R1 is a change to the finish line's "
                "derivation; the finish line is THE SCOPE by the user's ruling R2 of 2026-08-04, "
                "and a session does not reshape it. Nothing is hidden either way: this artifact "
                "and the item disagree in a stated direction, by a stated amount."
            ),
        },
        "superseded_entries_of_item_1_OUTSIDE_this_class": {
            "note": "Derived, so that no reader takes the NO-HOME class for the whole of R1's "
                    "reach over item 1. These are not dispositioned here — the dispatch scopes "
                    "Task 2 to the no-home class.",
            "ids": other_superseded,
            "count": len(other_superseded),
        },
        "rows": rows,
    }


def main(argv: list[str]) -> int:
    data = build()
    text = json.dumps(data, indent=1, ensure_ascii=False) + "\n"
    if "--check" in argv:
        if not OUT.exists():
            print(f"FAIL: {OUT.name} does not exist")
            return 1
        if OUT.read_text(encoding="utf-8") != text:
            print(f"FAIL: {OUT.name} differs from what the generator now produces")
            return 1
        c = data["counted"]
        print(f"PASS: {OUT.name} re-derives byte-identically "
              f"({c['no_home_class_population']} entries; {c['entries_that_LEAVE_item_1']} leave / "
              f"{c['entries_whose_ROUTE_CHANGES_to_home_the_successor']} route-changed / "
              f"{c['entries_that_do_NEITHER']} neither)")
        return 0
    OUT.write_text(text, encoding="utf-8")
    c = data["counted"]
    print(f"wrote {OUT}")
    print(f"  {c['no_home_class_population']} entries in item 1's NO-HOME class")
    print(f"  leave: {c['entries_that_LEAVE_item_1']}  "
          f"route changed: {c['entries_whose_ROUTE_CHANGES_to_home_the_successor']}  "
          f"neither: {c['entries_that_do_NEITHER']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
