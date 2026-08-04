#!/usr/bin/env python3
"""THE OUTSTANDING DELEGATION POPULATION, DERIVED AT HEAD — never taken from the write list.

THE RULING (user, 2026-08-04, dispatch `cc_instruction_phase1_delegations_and_corrections.md` R4):
the outstanding delegation population is DERIVED AT HEAD from the delegation grades and the home
data — **never taken from the write list, which carries no state and therefore cannot distinguish
written from unwritten.**

WHY THE RULING WAS NEEDED, measured rather than asserted.  `tools/audit/gen_phase1_completion_
inventory.py` reported the figure `documents_awaiting_a_delegation_only_the_user_may_write` as
`len(write_list)` — the LIST'S MEMBERSHIP.  A member the user has since satisfied stays in the list
(the list is the record of what was asked for, and #12 keeps it), so the figure counted asks ever
made rather than asks outstanding.  That is the OI-283 shape — a recorded finding never marked
discharged — inside the artifact a phase-1 completion statement would rest on.

WHAT THIS DERIVES, and the partition it derives.  For every entry of the home population, the
reason its class is what it is, taken from the criteria in force:

  A — NO DELEGATION EXISTS.  Clause (a) (the fifth home case, OI-268) fails: the document is named
      in none of the three user-ratified surfaces, so there is nothing to grade.
  B — A NAMING EXISTS AND THE BAR EXCLUDES ITS FORM.  D-432: a bare appended citation or a
      provenance attribution.
  C — AN ADMITTING DELEGATION NAMES SECTIONS AND THE ENTRY SITS OUTSIDE THEM.  D-430's delegation
      half.  This is the only class where a delegation the user may WIDEN would move the entry.
  D — CLOSED.  The delegation reaches the entry's section and that section states rules.
  E — REACHED, AND THE KIND HALF DECIDES.  D-430's second half: the delegation reaches the section
      and the section RECORDS FINDINGS.  **Not a delegation matter** — the remedy is at the
      document, which is what the register's own `not_write_list_cases` says for this shape.

Only A, B and C are entries lost FOR WANT OF A DELEGATION, and only C is one a widening closes.

WHAT IS AUTHORED.  The per-write-list-member state label and its reason; the draft wording offered
for each class-C document and what each would close; the reading of what each un-named section IS,
taken from its own heading and its own opening lines; and, for a document that has LEFT class C
because the user ordered a delegation and it was written, the ruling that ordered it and the draft
it superseded, preserved verbatim (#12).  Nothing else — every count, every identity, every
delegation citation and every state is derived.

THE RULINGS THIS FILE CARRIES (user, 2026-08-04, dispatch `cc_instruction_census_delegation_and_
commit.md`).  R1 — the census pointer is WIDENED, and `cowork_score_census.md` therefore appears
under `settled_by_a_written_delegation` rather than in the outstanding set.  R2 — the voice-leading
delegation is NOT widened and its three entries stay `gap`; R3 — no delegation is drafted for the
structural-integrity audit.  **R2 and R3 are RULINGS, not deferrals**: neither document is awaiting
an act, and a later wave owes nothing on either.  Both are recorded in terms, at the row each
belongs to, so that the absence of a draft is never re-read as an oversight.

THE STOPS.  The tool refuses to run if a home document carries no authored delegation grade (it
imports FORMS, whose own STOP covers that), if a write-list member is not a home document any more,
if a class-C document's authored draft names a section the document does not have, or if a document
recorded as settled by a written delegation is STILL losing entries to the delegation half — which
is exactly what a widening that failed to take would look like.

Usage:
  python tools/audit/decisions/gen_outstanding_delegations.py           # write the artifact
  python tools/audit/decisions/gen_outstanding_delegations.py --check   # re-derive, exit 1 on drift
"""
from __future__ import annotations

import argparse
import collections
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
BACKBONE = os.path.join(HERE, "backbone_decisions.json")
OUT = os.path.join(HERE, "outstanding_delegations.json")

sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))
from output_encoding import use_utf8_output          # noqa: E402  (path set above)
from gen_phase1p_delegation_bar import (              # noqa: E402  — the ONE home of the grades
    FORMS, ADMITTING, NOT_NAMED, locate,
)
from gen_home_classification import (                 # noqa: E402  — the ONE home of the population
    home_population, headings_of,
)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

# ---------------------------------------------------------------------------
# AUTHORED — the state of each write-list member at HEAD, and the reason for that label.
# The label is a reading of the derived facts beside it; the derived facts are recomputed here
# every run, so a label that stops matching them is visible rather than silent.
# ---------------------------------------------------------------------------
WRITE_LIST_STATE: dict[str, tuple[str, str]] = {
    "cowork_layer5_function_design.md": (
        "WRITTEN — CLOSED",
        "The user wrote an explicit delegation clause on 2026-08-03 and every entry of the "
        "document is `contract-home`. Nothing is outstanding."),
    "cowork_prefit_gates.md": (
        "WRITTEN — CLOSED",
        "The user wrote an explicit delegation clause on 2026-08-03 and every entry is "
        "`contract-home`."),
    "cowork_engage_arc_plan.md": (
        "WRITTEN — CLOSED",
        "The user wrote an explicit delegation clause into `CLAUDE.md` on 2026-08-03 and all "
        "three entries of the home population are `contract-home`. The document's fourth entry "
        "is `process`, which the home-class criteria do not reach at all."),
    "cowork_joint_key_chord_design.md": (
        "WRITTEN — CLOSED",
        "The user wrote an explicit delegation clause into `cowork_engage_arc_plan.md`'s arc-#10 "
        "bullet on 2026-08-03 and every entry is `contract-home`."),
    "cowork_notation_output_contract.md": (
        "WRITTEN — CLOSED",
        "The named sections were widened to include §2, which is where D-275 sits, and both "
        "entries are `contract-home`."),
    "cowork_layer2_slicing_design.md": (
        "WRITTEN — CLOSED",
        "The user wrote an explicit delegation clause on 2026-08-04 (READ WAVE 5). Both entries "
        "are `contract-home` as of this wave's classification run."),
    "cowork_layer1_note_model_design.md": (
        "WRITTEN — CLOSED ON THE DELEGATION QUESTION",
        "The user wrote an explicit delegation clause on 2026-08-04 (READ WAVE 5) and it reaches "
        "every section. Three of the four entries are `contract-home`; the fourth (D-518) stays "
        "`gap` on the KIND half — its home section is §13, whose own heading ends '(NOT needed to "
        "understand the layer)'. That is not a delegation matter and no delegation would move it."),
    "cowork_layer6_grouping_design.md": (
        "WRITTEN — CLOSED ON THE DELEGATION QUESTION",
        "The user wrote an explicit delegation clause on 2026-08-04 (READ WAVE 6, ruling R5). "
        "Eight of the nine entries are `contract-home`; the ninth (D-458) stays `gap` on the KIND "
        "half — it is homed in the document's STATUS BANNER. Not a delegation matter."),
    "cowork_phrase_boundary_design.md": (
        "WRITTEN — CLOSED ON THE DELEGATION QUESTION",
        "The user wrote an explicit delegation clause on 2026-08-04 (READ WAVE 5, ruling R4). "
        "Eight of the ten entries are `contract-home`; two (D-484, D-485) stay `gap` on the KIND "
        "half — the document's opening block and its §11 'Open items'. Not a delegation matter."),
    "cowork_layer1_tone_collection_design.md": (
        "RULED NOT A DELEGATION TARGET",
        "The user ruled on 2026-08-04 (READ WAVE 6, ruling R6) that this document is NOT a "
        "delegation target, because the concern it designs was absorbed by the note model and a "
        "delegation would create a second home for a concern that already has one (#6). Its two "
        "entries stay `gap` as the ruling intends. It is not awaiting anything."),
    "cowork_voiceleading_axis_design.md": (
        "RULED NOT WIDENED — SETTLED BY RULING, NOT DEFERRED",
        "The delegation was widened on 2026-08-03 from §0/§5.3 to §0/§5.1/§5.3/§8/§9, which moved "
        "seven entries in. Three remain outside the named sections: D-398 in §15 and D-397/D-400 "
        "in §16, and the 2026-08-03 widening excluded those two sections deliberately. ★ THE USER "
        "RULED ON 2026-08-04 (ruling R2, dispatch `cc_instruction_census_delegation_and_commit."
        "md`) THAT THE DELEGATION IS NOT WIDENED TO REACH THEM. D-397 and D-400 ARE §16's "
        "ratification asks A7 and A5 — asks put TO the user — and D-398 sits in §15, a tracking "
        "list; an ask is not a rule, and forcing either a contract home would misdescribe what it "
        "is. The three entries stay `gap` as the ruling intends, and the kind half would exclude "
        "both sections at the next run in any case, so a widening would be a wording change that "
        "closes nothing. THIS IS A RULING AND NOT A DEFERRAL: the document is not awaiting an act "
        "and no later wave owes one here."),
}

# ---------------------------------------------------------------------------
# AUTHORED — for each class-C document, what the un-named sections ARE (read at the object,
# from the section's own heading and opening lines), the draft wording, and what it would close.
# ---------------------------------------------------------------------------
CLASS_C_DRAFT: dict[str, dict] = {
    "cowork_voiceleading_axis_design.md": {
        "current_delegation_names": "§0, §5.1, §5.3, §8, §9",
        "what_the_un_named_sections_are": (
            "§15 is 'Open items & deferred refinements' — a numbered tracking list of what is "
            "owed, deferred or since closed. §16 is 'Ratification asks' — eight lettered asks "
            "(A1…A8) put TO the user; D-400 is ask A5 and D-397 is ask A7."),
        "draft_delegation_for_the_user_to_write_or_reject": (
            "Widen the named sections at `ARCHITECTURE.md`'s existing line — \"Criterion + build "
            "home: `cowork_voiceleading_axis_design.md` §0/§5.1/§5.3/§8/§9/§15/§16 (AS-BUILT)\" — "
            "OR leave it as it stands and home those three decisions where their concerns are "
            "owned instead."),
        "what_it_would_close": (
            "The DELEGATION half only, for D-397, D-398 and D-400. It would NOT by itself make "
            "them `contract-home`: D-430's kind half is then judged per section, and it is not "
            "pre-judged here. ★ THE RECOMMENDATION IS THE SECOND OPTION, and the reason is that "
            "the two sections are the two shapes the record has already declined elsewhere — a "
            "tracking list (the OI-240 shape, and the same reading this wave made of "
            "`cowork_phrase_boundary_design.md` §11) and a list of asks put to the user. A "
            "widening that reaches them would most likely be excluded on the kind half at the "
            "next run, which is a wording change that closes nothing."),
    },
    "cowork_structural_integrity_audit.md": {
        "current_delegation_names": "§3 (the prioritized fix-queue) and §4 (the sequencing call)",
        "what_the_un_named_sections_are": (
            "§1.2 'The cap→append chain — dissolution hypothesis TESTED at code (CONFIRMED)' — a "
            "section reporting the result of a test run against the code."),
        "draft_delegation_for_the_user_to_write_or_reject": (
            "NONE IS OFFERED, AND THAT IS NOW A RULING RATHER THAN THIS TOOL'S READING. ★ THE "
            "USER RULED ON 2026-08-04 (ruling R3, dispatch `cc_instruction_census_delegation_and_"
            "commit.md`) THAT NO DELEGATION IS DRAFTED OR WRITTEN FOR THIS DOCUMENT. The ground "
            "is the register's own `not_write_list_cases`, which already rules on this document's "
            "other lost entries: 'A delegation cannot repair that; the remedy is the same as "
            "OI-290's — at the document, or by homing those verdicts where the concern is owned.' "
            "D-402 sits in a section of the same kind, and the same remedy follows. THE REMEDY IS "
            "AT THE DOCUMENT, and it is not a delegation act."),
        "what_it_would_close": (
            "Nothing that should be closed by a delegation. Recorded so the class is complete, "
            "not because a widening is proposed — and it stays recorded after ruling R3, because "
            "a ruling that nothing is owed is itself a thing the record must carry (#12)."),
    },
}

# ---------------------------------------------------------------------------
# AUTHORED — documents that HAVE LEFT class C because a delegation the user ordered was written.
# The draft that was offered is preserved verbatim (#12): a delegation the record acted on is
# evidence of why it was acted on, and nothing re-derives that reasoning once the class moves.
# The STATE is derived, never recorded here (D-640) — `build()` STOPS if a document listed as
# settled is still losing entries to the delegation half, which is what a widening that failed
# to take would look like.
# ---------------------------------------------------------------------------
SETTLED_BY_A_WRITTEN_DELEGATION: dict[str, dict] = {
    "cowork_score_census.md": {
        "the_ruling": (
            "★ RULING R1, user, 2026-08-04, dispatch `cc_instruction_census_delegation_and_"
            "commit.md`: widen the existing `ARCHITECTURE.md` §8c pointer so it names the "
            "sections the six entries sit in. Explicitly NOT a document-level delegation — the "
            "census is a findings document with a few rule-stating blocks, and naming the "
            "sections says exactly that, while a document-level delegation would assert the whole "
            "census is the authoritative detail for its scope, which is a stronger claim than the "
            "record makes."),
        "what_was_written": (
            "A widening paragraph at the end of `ARCHITECTURE.md`'s clause (e), sited so the "
            "existing §8c pointer line — which is the anchor `gen_phase1p_delegation_bar.py`'s "
            "FORMS table grades this document from — stays byte-identical. It names the contract "
            "as `cowork_score_census.md` §1/§3/§4/§8/§8b/§8c, states that it settles the "
            "DELEGATION half alone, and states that the kind half is judged per section at the "
            "classification pass and is not pre-judged by the naming."),
        "the_assumption_that_was_checked_first": (
            "The dispatch declared as an ASSUMPTION that the six entries sit only in the sections "
            "Cowork had read — §1 and §3 — because that reading came from a TRUNCATED block. "
            "Discharged against this artifact's own derived `the_sections_they_sit_in` before the "
            "widening named anything: the real set is FIVE sections, §1/§3/§4/§8/§8b, with §8 "
            "holding two of the six. Had the widening been written to the assumed set, three of "
            "the six entries would have stayed lost and the act would have read as complete."),
        "the_draft_that_was_offered_preserved_verbatim": (
            "Widen the named sections at `ARCHITECTURE.md`'s existing §8c pointer, or add a "
            "document-level delegation pointer beside it in the form the Layer-3/4/5 sections "
            "use: **Delegation pointer (the fifth home case, user-ratified 2026-08-02).** The "
            "ratified contract for the corpus census and its admission rules is "
            "`cowork_score_census.md` — D-… — which this section points at and does not restate."),
        "what_it_closed": (
            "The delegation half for six entries — the largest outstanding delegation gap at "
            "HEAD, and on a document the write list never carried. The kind half was then judged "
            "per section by reading each of the five in place, and all five state rules, so all "
            "six entries moved. Two of the five are NOT homogeneous — §1 carries a container "
            "table and §8 a mitigation plan — and that is recorded at each judgment rather than "
            "smoothed over, the `OPEN_ITEMS.md` OI-290 shape."),
    },
}


def read_backbone() -> dict:
    return json.loads(open(BACKBONE, encoding="utf-8").read())


def classify_entry(d: dict) -> tuple[str, str]:
    doc = d["home"].split(":")[0].replace("\\", "/")
    hs = d.get("home_section") or {}
    form = FORMS[doc][0]
    if d.get("nonspec_kind") == "contract-home":
        return "D_closed", "the delegation reaches this section and the section states rules"
    if form == NOT_NAMED:
        return "A_no_delegation_exists", (
            "clause (a), the fifth home case (OI-268) — the document is named in none of the "
            "three user-ratified surfaces, so there is no delegation to grade")
    if form not in ADMITTING:
        return "B_naming_exists_but_the_bar_excludes_its_form", (
            f"D-432, the delegation bar — the strongest naming is a {form}, which the bar does "
            "not admit")
    if not hs.get("delegated"):
        return "C_admitting_delegation_does_not_name_this_section", (
            "D-430's delegation half — the delegation names sections and this entry's section is "
            "not among them")
    return "E_reached_and_the_kind_half_decides", (
        "D-430's kind half — the delegation reaches this section and the section records "
        "findings; not a delegation matter")


def build() -> dict:
    bb = read_backbone()
    crit = bb["section_home_criterion"]
    pop = home_population(bb)

    per_doc_entries: dict[str, list[dict]] = collections.defaultdict(list)
    for d in pop:
        per_doc_entries[d["home"].split(":")[0].replace("\\", "/")].append(d)

    # ---- the partition -----------------------------------------------------------------
    classes: dict[str, dict[str, list[str]]] = collections.defaultdict(
        lambda: collections.defaultdict(list))
    reasons: dict[str, str] = {}
    for d in pop:
        k, why = classify_entry(d)
        reasons[k] = why
        classes[k][d["home"].split(":")[0].replace("\\", "/")].append(d["id"])

    def block(k: str, note: str) -> dict:
        by_doc = {doc: sorted(ids) for doc, ids in sorted(classes[k].items())}
        return {
            "what_it_is": note,
            "the_criterion_that_decides_it": reasons.get(k),
            "entries": sum(len(v) for v in by_doc.values()),
            "documents": len(by_doc),
            "by_document": by_doc,
        }

    # ---- the write list, graded at HEAD ------------------------------------------------
    wl = [w["document"] for w in crit["write_list"]]
    unknown = [d for d in wl if d not in WRITE_LIST_STATE]
    if unknown:
        raise SystemExit(f"STOP: write-list member(s) with no authored state label: {unknown}")
    stray = [d for d in WRITE_LIST_STATE if d not in wl]
    if stray:
        raise SystemExit(f"STOP: authored state label for a non-member: {stray}")

    wl_rows = []
    for doc in wl:
        label, why = WRITE_LIST_STATE[doc]
        form, surface, anchor, _w = FORMS[doc]
        citation = None
        if form != NOT_NAMED:
            ln, _txt = locate(surface, anchor)
            citation = f"{surface}:{ln}"
        ents = per_doc_entries.get(doc, [])
        kinds = collections.Counter(e.get("nonspec_kind") for e in ents)
        still = sorted(e["id"] for e in ents
                       if classify_entry(e)[0].startswith(("A_", "B_", "C_")))
        wl_rows.append({
            "document": doc,
            "state_at_head": label,
            "why": why,
            "delegation_at_head": citation or "named in no user-ratified surface",
            "delegation_form_at_head": form,
            "entries_in_the_home_population": len(ents),
            "by_class": dict(kinds),
            "entries_still_lost_to_the_delegation_half": still,
        })

    # ---- the class-C drafts -------------------------------------------------------------
    c_docs = sorted(classes["C_admitting_delegation_does_not_name_this_section"])
    missing = [d for d in c_docs if d not in CLASS_C_DRAFT]
    if missing:
        raise SystemExit(f"STOP: class-C document(s) with no authored draft: {missing}")
    extra = [d for d in CLASS_C_DRAFT if d not in c_docs]
    if extra:
        raise SystemExit(f"STOP: authored draft for a document that is not class C: {extra}")

    # ---- the settled cases: the reason is authored, the STATE is derived (D-640) ---------
    still_c = [d for d in SETTLED_BY_A_WRITTEN_DELEGATION if d in c_docs]
    if still_c:
        raise SystemExit(
            "STOP: document(s) recorded as settled by a written delegation are still losing "
            f"entries to the delegation half — the widening did not take: {still_c}")
    settled = []
    for doc in sorted(SETTLED_BY_A_WRITTEN_DELEGATION):
        ents = per_doc_entries.get(doc, [])
        if not ents:
            raise SystemExit(f"STOP: a settled document is nobody's home any more: {doc}")
        _f, surface, anchor, _w = FORMS[doc]
        ln, txt = locate(surface, anchor)
        settled.append({
            "document": doc,
            "on_the_write_list": doc in wl,
            "class_at_head_DERIVED": dict(collections.Counter(
                e.get("nonspec_kind") for e in ents)),
            "entries_still_lost_to_the_delegation_half_DERIVED": sorted(
                e["id"] for e in ents
                if classify_entry(e)[0].startswith(("A_", "B_", "C_"))),
            "sections_the_delegation_now_reaches_DERIVED": sorted(
                {e["home_section"]["label"] for e in ents
                 if (e.get("home_section") or {}).get("delegated")}),
            "the_delegation_this_document_is_graded_from": {
                "at": f"{surface}:{ln}", "line": txt.strip()},
            **SETTLED_BY_A_WRITTEN_DELEGATION[doc],
        })

    outstanding = []
    for doc in c_docs:
        ids = sorted(classes["C_admitting_delegation_does_not_name_this_section"][doc])
        sections = {}
        for d in per_doc_entries[doc]:
            if d["id"] in ids:
                hs = d["home_section"]
                sections.setdefault(hs["label"], {"heading": hs["section"],
                                                  "heading_line": hs["heading_line"],
                                                  "entries": []})["entries"].append(d["id"])
        _f, surface, anchor, _w = FORMS[doc]
        ln, txt = locate(surface, anchor)
        outstanding.append({
            "document": doc,
            "on_the_write_list": doc in wl,
            "entries_lost_to_the_delegation_half": ids,
            "the_sections_they_sit_in": sections,
            "the_delegation_that_exists": {"at": f"{surface}:{ln}", "line": txt.strip()},
            **CLASS_C_DRAFT[doc],
        })

    a = block("A_no_delegation_exists",
              "Entries whose home document is named in NONE of the three user-ratified surfaces.")
    b = block("B_naming_exists_but_the_bar_excludes_its_form",
              "Entries whose home document IS named, in a form D-432 does not admit.")
    c = block("C_admitting_delegation_does_not_name_this_section",
              "Entries whose home document HAS an admitting delegation that names sections, and "
              "which sit outside the named ones. The only class a widening moves.")
    d_ = block("D_closed", "Entries the criteria admit: delegated section, states rules.")
    e = block("E_reached_and_the_kind_half_decides",
              "Entries the delegation REACHES, excluded on the kind half. NOT a delegation "
              "matter — the remedy is at the document.")

    return {
        "purpose": (
            "The outstanding delegation population at HEAD, derived from the delegation grades "
            "and the home data — never from the write list. Ruling R4, user, 2026-08-04, dispatch "
            "`cc_instruction_phase1_delegations_and_corrections.md`."
        ),
        "generated_by": "tools/audit/decisions/gen_outstanding_delegations.py",
        "what_this_file_does_not_do": (
            "It writes no delegation, moves no entry's class, and authorizes nothing. Only the "
            "user writes a delegation into a user-ratified surface (rule (g))."
        ),
        "why_the_write_list_cannot_answer_this": (
            "The write list's entries carry no status field, and #12 keeps a satisfied ask in the "
            "list rather than deleting it — so its MEMBERSHIP counts asks ever made, not asks "
            "outstanding. `tools/audit/gen_phase1_completion_inventory.py` reported "
            "`documents_awaiting_a_delegation_only_the_user_may_write` as that membership, which "
            "is why the figure was wrong in a known direction: too large, by every ask the user "
            "has since satisfied. The remedy is this derivation; the list keeps its own role as "
            "the record of what was asked for."
        ),
        "the_partition": {
            "note": (
                "Every entry of the home population falls in exactly one class. A, B and C are "
                "entries lost FOR WANT OF A DELEGATION; only C is one a widening closes, because "
                "in A there is nothing to widen and in B the remedy is a re-wording the record "
                "may not want at all."
            ),
            "A_no_delegation_exists": a,
            "B_naming_exists_but_the_bar_excludes_its_form": b,
            "C_admitting_delegation_does_not_name_this_section": c,
            "D_closed": d_,
            "E_reached_and_the_kind_half_decides": e,
        },
        "THE_OUTSTANDING_SET": {
            "what_this_is": (
                "The answer to the ruling's question, and what goes to the user: the documents "
                "that still lose entries to the DELEGATION HALF where an admitting delegation "
                "already exists — so the record has already said it means to keep the home, and "
                "what falls short is which sections the delegation names."
            ),
            "documents": len(outstanding),
            "entries": c["entries"],
            "members": outstanding,
        },
        "settled_by_a_written_delegation": {
            "what_this_is": (
                "Documents that WERE in the outstanding set and have left it because the user "
                "ordered a delegation and it was written. The reason each left is authored; the "
                "state is derived every run, and a document listed here that is still losing "
                "entries to the delegation half STOPS this tool — which is what a widening that "
                "failed to take would look like. Kept rather than deleted (#12): the draft that "
                "was offered and the reasoning that produced it are evidence nothing re-derives "
                "once the class has moved."
            ),
            "documents": len(settled),
            "members": settled,
        },
        "what_is_NOT_proposed_as_a_delegation_and_why": {
            "class_A": {
                "entries": a["entries"], "documents": a["documents"],
                "why_no_draft_is_offered": (
                    "The register's own `not_write_list_cases` rules on exactly this shape: 'A "
                    "delegation drafted for them would be a new decision about where a concern is "
                    "owned, not the repair of a wording — so the remedy is the OI-272 per-kind "
                    "homing act into the specification that owns each decision, which is already "
                    "the standing scheme.' Drafting delegations for this class would be proposing "
                    "that many new decisions."
                ),
            },
            "class_B": {
                "entries": b["entries"], "documents": b["documents"],
                "why_no_draft_is_offered": (
                    "A naming exists but in an excluded form, and upgrading it asserts that the "
                    "record MEANS the document to be a contract home. The register already "
                    "declines that inference for the members it examined — for "
                    "`docs/redesign_plan.md`: 'Drafting a delegation would assert that the record "
                    "means to keep a superseded plan as a contract home, which the record does "
                    "not say.' The same reasoning covers the class."
                ),
            },
            "class_E": {
                "entries": e["entries"], "documents": e["documents"],
                "why_it_is_not_a_delegation_matter": (
                    "The delegation already reaches these sections. What excludes them is D-430's "
                    "kind half — the section records findings — and the register's own remedy for "
                    "that shape is at the DOCUMENT: 'move the rule it states into a rule-stating "
                    "section'. No delegation moves them."
                ),
            },
        },
        "the_write_list_at_head": {
            "what_this_is": (
                "Every write-list member, with the delegation that exists at HEAD and the state "
                "the derived facts put it in. Answers the ruling's per-document question."
            ),
            "members": wl_rows,
            "summary": dict(collections.Counter(r["state_at_head"].split(" — ")[0]
                                                for r in wl_rows)),
        },
        "counted": {
            "home_population_entries": len(pop),
            "home_population_documents": len(per_doc_entries),
            "lost_for_want_of_a_delegation": a["entries"] + b["entries"] + c["entries"],
            "of_which_a_widening_would_move": c["entries"],
            "outstanding_set_documents": len(outstanding),
            "write_list_members": len(wl),
            "write_list_members_still_losing_entries_to_the_delegation_half": sum(
                1 for r in wl_rows if r["entries_still_lost_to_the_delegation_half"]),
            "write_list_members_still_AWAITING_AN_ACT_BY_THE_USER": sorted(
                r["document"] for r in wl_rows
                if r["entries_still_lost_to_the_delegation_half"]
                and not r["state_at_head"].startswith(("WRITTEN", "RULED"))),
            "why_those_two_counts_differ": (
                "`cowork_layer1_tone_collection_design.md` still loses both its entries to the "
                "delegation half and is NOT awaiting an act: the user ruled on 2026-08-04 (READ "
                "WAVE 6, R6) that it is not a delegation target, so `gap` is the class the ruling "
                "intends. Counting it as outstanding would re-open a settled question."
            ),
        },
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    art = build()
    text = json.dumps(art, indent=2, ensure_ascii=False) + "\n"
    if args.check:
        have = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
        if have != text:
            print("STALE vs the files: outstanding_delegations.json does not re-derive")
            return 1
        print("the outstanding-delegation derivation re-derives from the files")
        return 0
    open(OUT, "w", encoding="utf-8", newline="").write(text)
    c = art["counted"]
    print(f"wrote {os.path.relpath(OUT, ROOT)}")
    print(f"  home population: {c['home_population_entries']} entries / "
          f"{c['home_population_documents']} documents")
    print(f"  lost for want of a delegation: {c['lost_for_want_of_a_delegation']}  "
          f"(a widening would move {c['of_which_a_widening_would_move']})")
    print(f"  THE OUTSTANDING SET: {c['outstanding_set_documents']} document(s)")
    for m in art["THE_OUTSTANDING_SET"]["members"]:
        print(f"      {m['document']}  {len(m['entries_lost_to_the_delegation_half'])} entr(y/ies)"
              f"  write-list={m['on_the_write_list']}")
    print(f"  write list: {c['write_list_members']} members, "
          f"{c['write_list_members_still_losing_entries_to_the_delegation_half']} still losing "
          f"entries to the delegation half")
    return 0


if __name__ == "__main__":
    sys.exit(main())
