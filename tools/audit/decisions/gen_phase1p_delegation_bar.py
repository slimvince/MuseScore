#!/usr/bin/env python3
"""Generate `tools/audit/decisions/phase1p_delegation_bar.json` — the phase-1p measurements.

WHAT THIS IS.  The user ruled on 2026-08-03 (phase 1p, W2) what a DELEGATION is — the
clause (b) question three waves had left open.  The bar:

    ADMITTED — an explicit delegation clause ("The ratified contract for this layer is X",
               "The ONE detailed cross-layer spec for this contract is X", "formalised as
               an independent knowledge-base component with its own spec (X)"); or a named
               home with sections ("Criterion + build home: X §0/§5.3").
    NOT ADMITTED — a bare appended citation ("Full spec: X."); or a provenance attribution
               (a naming inside a list of citations, or a parenthetical recording where
               something was ratified).

The dispatch orders a CHECK BEFORE APPLYING: does the bar change the verdict for any
document the register currently classifies `contract-home`?  It predicts not, on the ground
that "the admitted set was reached on explicit delegation clauses", and names a different
answer a #13 STOP.  This tool runs that check.  **It applies nothing** — it only reads
`backbone_decisions.json`; no entry's `nonspec_kind` is written here.

WHY A GENERATOR.  `CLAUDE.md` #17(f), and the 2026-08-03 figures rule (register entry
D-431): no figure enters a dispatch or a report by transcription.  Every count in the
phase-1p report and in the dated notes is computed here.  Only the FORMS table below is a
judgment, and each row carries an ANCHOR — a distinctive substring of the delegating line —
which this tool LOCATES in the surface file itself, so the line number and the quoted text
come from the file and not from the author.  An anchor that has moved, gone or become
ambiguous stops the tool rather than emitting a stale citation.

WHAT IS AUTHORED AND WHAT IS DERIVED.
  authored : FORMS — per home document, the STRONGEST delegation found in the three
             user-ratified surfaces, graded into one of the bar's four forms, with the
             anchor it was graded from and a note saying why that grade.
  derived  : the home population and its current classification; each anchor's current
             line number and text; the bar's verdict per document; the movement against
             the register's present state; the pre-apply check and its verdict; the
             section-level consequence for the five documents already at section
             granularity; and the `cowork_score_census.md` §8c table-row count.

THIS ARTIFACT IS A PRE-APPLY RECORD, AND IT STAYS ONE (amended 2026-08-03, phase 1q).  The
user ruled the bar APPLIED, in one pass over the whole population
(`tools/audit/decisions/gen_home_classification.py`), so the register's present classes are the
POST-apply ones.  Recomputing this artifact from them would report "PROCEED — the prediction
holds" and quietly destroy the finding `OPEN_ITEMS.md` OI-291 and **D-432** both cite (#12).  It
therefore reads each entry's class from `home_section.class_before_phase1q` — the value the pass
recorded and never overwrites — so the pre-apply check keeps reporting what it found, while the
delegation citations stay live against the files.  The one block that WAS superseded, the
section-level consequence, is not recomputed here: the phase-1q pass covers every entry rather
than the five documents then at section granularity, and two computations of one thing is the
duplication #6 forbids.

THE SAME PROBLEM REACHED THE GRADES (amended 2026-08-03, phase 1r).  On 2026-08-03 the user WROTE
delegations for four documents (the OI-293 write list), which moves their FORMS grade — and FORMS
must move, because `gen_home_classification.py` imports it to classify against the delegations
that exist TODAY, and a second grade table would be the duplication #6 forbids.  Recomputing the
pre-apply check from the moved grades would drop two of its three documents and shrink
`entries_affected_by_the_bar`, destroying the finding exactly as recomputing the classes would
have.  So the grades are frozen the same way the classes are: FORMS is LIVE, `GRADE_AT_PHASE_1P`
records what the four carried when the check ran, and the check reads the frozen values while
every row also reports its live grade beside them.  A document enters that block only once its
delegation has actually changed, so it cannot shadow a grade that never moved.

Run:  python tools/audit/decisions/gen_phase1p_delegation_bar.py [--check]
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
OUT = os.path.join(HERE, "phase1p_delegation_bar.json")

sys.path.insert(0, os.path.dirname(HERE))
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

# The three surfaces whose USER ratification is not in question — the same three phases 1l
# and 1m searched, and the only places a delegation can come from under the criterion.
RATIFIED_SURFACES = ["ARCHITECTURE.md", "CLAUDE.md", "cowork_engage_arc_plan.md"]

# The bar's four forms.  The first two admit; the last two do not.  NOT_NAMED is not one of
# the bar's forms — it is clause (a) failing before the bar is reached, and is kept separate
# so the report can say which documents the bar itself decides and which it never touches.
CLAUSE = "explicit-delegation-clause"
NAMED_SECTIONS = "named-home-with-sections"
BARE_CITATION = "bare-appended-citation"
PROVENANCE = "provenance-attribution"
NOT_NAMED = "not-named-in-any-ratified-surface"

ADMITTING = {CLAUSE, NAMED_SECTIONS}

# ---------------------------------------------------------------------------
# AUTHORED — the STRONGEST delegation per home document, graded against the bar.
#   document -> (form, surface, anchor, why)
# The anchor is located in the surface below; the emitted citation is the file's own line.
# Every grade was made by reading the located line in place in the phase-1p session.
# ---------------------------------------------------------------------------
FORMS: dict[str, tuple[str, str, str, str]] = {
    "cowork_layer3_keymode_design.md": (
        CLAUSE, "ARCHITECTURE.md",
        "The ratified contract for this layer is `cowork_layer3_keymode_design.md`",
        "The bar's first named form, word for word."),
    "cowork_layer4_chordsymbol_design.md": (
        CLAUSE, "ARCHITECTURE.md",
        "The ratified contract for this layer is `cowork_layer4_chordsymbol_design.md`",
        "The bar's first named form, word for word."),
    "cowork_layer5_engagement_design.md": (
        CLAUSE, "ARCHITECTURE.md",
        "The ratified contract for how this layer ENGAGES",
        "The bar's first named form, and it names its target's sections as well "
        "(Part 1 §1–§5, Part 2 §6–§10). Independently carried by the arc plan's three "
        "by-name delegations, which is what kept this precedent honest at phase 1l."),
    "cowork_bounded_context_design.md": (
        CLAUSE, "ARCHITECTURE.md",
        "detailed cross-layer spec for this contract is",
        "The bar's second named form, word for word."),
    "cowork_confidence_contract.md": (
        CLAUSE, "ARCHITECTURE.md",
        "are stated in full in `cowork_confidence_contract.md`",
        "An instruction to read the document instead of the section — the delegation "
        "clause's shape, in different words."),
    "cowork_stage5_fitter_design.md": (
        CLAUSE, "ARCHITECTURE.md",
        "the fitting event's own design contract is",
        "A delegation clause of the 'the X for this Y is Z' shape."),
    "docs/scoring_model.md": (
        CLAUSE, "CLAUDE.md",
        "Read `docs/scoring_model.md` at the start of any session",
        "A whole standing section that makes the document a mandatory read, calls it the "
        "authoritative reference for the scoring pipeline, and binds a same-commit sync "
        "rule to it. Stronger than any single clause in the bar's examples."),
    "cowork_progression_schema_dictionary.md": (
        CLAUSE, "ARCHITECTURE.md",
        "formalised as an **independent knowledge-base component** with its own spec",
        "The bar's third named form, word for word."),
    "cowork_notation_output_contract.md": (
        NAMED_SECTIONS, "ARCHITECTURE.md",
        "DORMANT; contract `cowork_notation_output_contract.md`",
        "A JUDGMENT, recorded as one: the naming sits inside a parenthesis, which the bar "
        "associates with the excluded provenance form — but it names the document's ROLE "
        "('contract') and the SECTIONS it delegates (§3.1–§3.4), and it records no "
        "ratification event. The excluded parenthetical form is the one that records WHERE "
        "SOMETHING WAS RATIFIED; this one names a home."),
    "cowork_score_census.md": (
        NAMED_SECTIONS, "ARCHITECTURE.md",
        "with the per-licence-class pool table, is `cowork_score_census.md` §8c",
        "A named home with a section — the case the section-level ruling (D-430) was made "
        "on, inside a passage the section marks user-ratified."),
    "cowork_voiceleading_axis_design.md": (
        NAMED_SECTIONS, "ARCHITECTURE.md",
        "Criterion + build home:",
        "The bar's second named form, word for word — it is the bar's own worked example."),
    "cowork_structural_integrity_audit.md": (
        NAMED_SECTIONS, "cowork_engage_arc_plan.md",
        "those live in `cowork_structural_integrity_audit.md`",
        "A named home with sections (§3 fix-queue, §4 sequencing), from a user-ratified "
        "surface. The bar admits the DELEGATION; whether the named sections state rules is "
        "the second half of D-430 and is not decided here."),

    "cowork_layer5_function_design.md": (
        CLAUSE, "ARCHITECTURE.md",
        "The ratified contract for this layer's function, cadence and tonicization decisions is",
        "The bar's first named form, word for word. WRITTEN 2026-08-03 on the user's "
        "direction (the OI-293 write list); until then the strongest naming was the bare "
        "appended citation on the line above it, which is why this document sat on the "
        "write list. The 'Full spec:' line is retained beside it and is still the ruling's "
        "own worked example of the excluded form."),
    "docs/redesign_plan.md": (
        BARE_CITATION, "ARCHITECTURE.md",
        "Design reference: `docs/redesign_plan.md`",
        "A bare appended citation. (Two of its three namings additionally sit inside "
        "blocks `ARCHITECTURE.md` itself banners SUPERSEDED — the phase-1l ground, which "
        "the bar does not need.)"),
    "cowork_prefit_gates.md": (
        CLAUSE, "ARCHITECTURE.md",
        "ratified contract for the PRE-FIT PROTOCOLS",
        "The bar's first named form. WRITTEN 2026-08-03 on the user's direction (the "
        "OI-293 write list); until then the strongest naming was a provenance attribution "
        "— the document inside a list of citations, and a parenthetical recording where "
        "the protocols were ratified. Both of those namings are retained."),
    "cowork_notation_adoption_increment.md": (
        PROVENANCE, "ARCHITECTURE.md",
        "pedal-point ruling of the notation-adoption increment",
        "A parenthetical recording where a ruling was made. Its `CLAUDE.md` naming "
        "('analysis in `…` §2') is the same form."),
    "cowork_engage_arc_plan.md": (
        CLAUSE, "CLAUDE.md",
        "The ratified contract for the ORDER OF WORK from here to the precision phase",
        "The bar's first named form. WRITTEN 2026-08-03 on the user's direction (the "
        "OI-293 write list), in `CLAUDE.md` beside the citation list it supplements. Until "
        "then the strongest naming was that list — a provenance attribution — which is the "
        "W4 collision **D-435** settled in the bar's favour. Note that this document is "
        "ALSO one of the three surfaces delegations are read FROM; D-435 is the ruling that "
        "the two roles are independent, so being a delegation TARGET here is a separate "
        "fact from being a delegating SURFACE."),
    "cowork_joint_key_chord_design.md": (
        CLAUSE, "cowork_engage_arc_plan.md",
        "The ratified contract for the coupled key↔chord decision",
        "The bar's first named form. WRITTEN 2026-08-03 on the user's direction (the "
        "OI-293 write list), into the arc-#10 bullet, which is the shape arcs #9 and #11 "
        "two bullets away already used. Until then the naming was a parenthetical inside a "
        "bulleted list of arcs, naming no section — a provenance attribution."),

    "cowork_architecture_reassessment.md": (
        NOT_NAMED, "", "", "Named in none of the three surfaces; verified mechanically here."),
    # ------------------------------------------------------------------
    # (the four regraded rows above are the ONLY ones whose grade has moved since phase 1p;
    #  GRADE_AT_PHASE_1P below records what they were, and is what the pre-apply check reads)
    # ------------------------------------------------------------------
    "docs/decoder_design.md": (
        NOT_NAMED, "", "", "Named in none of the three surfaces; verified mechanically here."),
    "docs/implementation_roadmap.md": (
        NOT_NAMED, "", "", "Named in none of the three surfaces; verified mechanically here."),
    "docs/iteration_path1_summary.md": (
        NOT_NAMED, "", "", "Named in none of the three surfaces; verified mechanically here."),
}


# ---------------------------------------------------------------------------
# FROZEN — the grade each regraded document carried WHEN THE PRE-APPLY CHECK WAS RUN.
#
# WHY THIS EXISTS.  FORMS above is the LIVE grade, and it must be: `gen_home_classification.py`
# imports it to classify against the delegations that exist TODAY, and two grade tables would be
# the duplication #6 forbids.  But the pre-apply check is a HISTORICAL finding — the phase-1p
# prediction was REFUTED, and `OPEN_ITEMS.md` OI-291 and **D-432** both cite it.  On 2026-08-03
# the user WROTE delegations for four of these documents (the OI-293 write list), which moves
# their live grade; recomputing the check from the moved grades would drop two of its three
# documents and shrink `entries_affected_by_the_bar`, quietly destroying the finding (#12).
#
# This is the same pattern the class figures already use: the classes are read frozen from
# `home_section.class_before_phase1q`, and the grades are read frozen from here.  A document
# appears below ONLY once its delegation has actually changed; every other document's check row
# comes from the live FORMS grade, so this block cannot silently shadow a grade that never moved.
#
#   document -> (form, citation as recorded at phase 1p, what the naming was)
GRADE_AT_PHASE_1P: dict[str, tuple[str, str, str]] = {
    "cowork_layer5_function_design.md": (
        BARE_CITATION, "ARCHITECTURE.md:1482",
        "\"…it does not read a resolved key). Full spec:\" — the bar's first excluded form, "
        "word for word, and the line the ruling's own defense cites."),
    "cowork_prefit_gates.md": (
        PROVENANCE, "ARCHITECTURE.md:49",
        "\"…`cowork_prefit_gates.md`; adoption record…\" — a naming inside a list of "
        "citations; its other naming recorded where the protocols were ratified."),
    "cowork_engage_arc_plan.md": (
        PROVENANCE, "CLAUDE.md:129",
        "\"Companion standing rules elsewhere: … the MEASURE-BEFORE-BUILD gate "
        "(`cowork_engage_arc_plan.md`, …)\" — a naming inside a list of citations."),
    "cowork_joint_key_chord_design.md": (
        PROVENANCE, "cowork_engage_arc_plan.md:44",
        "\"**arc #10 — the joint key-and-chord step**\" — a parenthetical naming inside a "
        "bulleted list of arcs, naming no section."),
}


def read_lines(rel: str) -> list[str]:
    with open(os.path.join(ROOT, rel), encoding="utf-8", errors="replace") as fh:
        return fh.read().splitlines()


def locate(surface: str, anchor: str) -> tuple[int, str]:
    """The one line of `surface` carrying `anchor`.  Ambiguity or absence is a stop."""
    hits = [(i, ln) for i, ln in enumerate(read_lines(surface), 1) if anchor in ln]
    if not hits:
        raise SystemExit(f"anchor not found in {surface}: {anchor!r} — the delegation has "
                         "moved or been reworded; re-read it and re-grade, never re-aim blind")
    if len(hits) > 1:
        raise SystemExit(f"anchor is ambiguous in {surface} (lines "
                         f"{[h[0] for h in hits]}): {anchor!r}")
    return hits[0]


def mentions() -> dict[str, list[str]]:
    """Every by-name mention of every home document in the three ratified surfaces."""
    text = {s: read_lines(s) for s in RATIFIED_SURFACES}
    out: dict[str, list[str]] = collections.defaultdict(list)
    for name in FORMS:
        base = name.split("/")[-1]
        for s, lines in text.items():
            for i, line in enumerate(lines, 1):
                if base in line:
                    out[name].append(f"{s}:{i}")
    return dict(out)


def census_table_rows() -> dict:
    """The `cowork_score_census.md` needs-vector table's extent, derived from the file.

    Task 1 asks how many of the entries admitted into §8c are rows of the findings table
    inside it.  The extent is derived — the maximal run of lines opening `| N<digit>` — so
    the count is not eyeballed off a rendered table.
    """
    lines = read_lines("cowork_score_census.md")
    rows = [i for i, ln in enumerate(lines, 1) if ln.startswith("| N") and ln[3:4].isdigit()
            or (ln.startswith("| N") and ln[2:3].isdigit())]
    return {"first_row_line": min(rows), "last_row_line": max(rows), "row_count": len(rows)}


def pre_apply_kind(d: dict) -> str | None:
    """The entry's home class BEFORE the phase-1q pass applied the bar.

    The pass records it once, on the entry, and never overwrites it; reading it here is what
    keeps this artifact a record of the state the check was run against rather than a
    recomputation over the state the check caused.
    """
    hs = d.get("home_section")
    if hs and "class_before_phase1q" in hs:
        return hs["class_before_phase1q"]
    return d.get("nonspec_kind")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="regenerate into memory and report whether the artifact matches")
    args = ap.parse_args()

    backbone = json.loads(open(BACKBONE, encoding="utf-8").read())
    decisions = backbone["decisions"]

    population = [d for d in decisions
                  if not d.get("home_is_layer_spec")
                  and pre_apply_kind(d) in ("contract-home", "gap")]
    per_doc: dict[str, dict] = {}
    for d in population:
        doc = d["home"].split(":")[0].replace("\\", "/")
        rec = per_doc.setdefault(doc, {"entries": [], "current": collections.Counter()})
        rec["entries"].append(d["id"])
        rec["current"][pre_apply_kind(d)] += 1

    unknown = sorted(set(per_doc) - set(FORMS))
    if unknown:
        raise SystemExit(f"home document(s) with no authored FORM judgment: {unknown}")
    unused = sorted(set(FORMS) - set(per_doc))
    if unused:
        raise SystemExit(f"FORM judgment for a document that is nobody's home: {unused}")

    seen = mentions()
    for doc, (form, _s, _a, _w) in FORMS.items():
        if form == NOT_NAMED and seen.get(doc):
            raise SystemExit(f"FORMS says {doc} is named nowhere, but it is: {seen[doc]}")
        if form != NOT_NAMED and not seen.get(doc):
            raise SystemExit(f"FORMS grades a delegation for {doc}, which is named nowhere")

    rows, tally = [], collections.Counter()
    for doc in sorted(per_doc, key=lambda k: (-len(per_doc[k]["entries"]), k)):
        rec = per_doc[doc]
        form, surface, anchor, why = FORMS[doc]
        if form == NOT_NAMED:
            line, text, verdict = None, None, "EXCLUDE"
        else:
            line, text = locate(surface, anchor)
            verdict = "ADMIT" if form in ADMITTING else "EXCLUDE"

        # The grade the pre-apply check was RUN AGAINST. Identical to the live grade unless
        # the delegation has since been written, in which case it is read frozen from above.
        frozen = GRADE_AT_PHASE_1P.get(doc)
        form_1p = frozen[0] if frozen else form
        cite_1p = frozen[1] if frozen else (f"{surface}:{line}" if line else None)
        verdict_1p = ("EXCLUDE" if form_1p == NOT_NAMED
                      else ("ADMIT" if form_1p in ADMITTING else "EXCLUDE"))

        cur_ch = rec["current"]["contract-home"]
        cur_gap = rec["current"]["gap"]
        movement = "none"
        if verdict_1p == "ADMIT" and cur_gap:
            movement = "WOULD MOVE IN"
        elif verdict_1p == "EXCLUDE" and cur_ch:
            movement = "WOULD MOVE OUT"
        tally[verdict_1p] += len(rec["entries"])
        rows.append({
            "document": doc,
            "entries": len(rec["entries"]),
            "entry_ids": rec["entries"],
            "current_contract_home": cur_ch,
            "current_gap": cur_gap,
            "form": form_1p,
            "delegation_citation": cite_1p,
            "form_now": form,
            "delegation_citation_now": (f"{surface}:{line}" if line else None),
            "delegation_line_now": (text.strip() if text else None),
            "delegation_written_since_the_check": bool(frozen),
            "what_the_naming_was_at_the_check": (frozen[2] if frozen else None),
            "why_this_grade_now": why,
            "verdict": verdict_1p,
            "verdict_now": verdict,
            "movement": movement,
            "decided_by_the_bar": form_1p != NOT_NAMED,
            "mentions_in_ratified_surfaces": seen.get(doc, []),
        })

    # ── the check the dispatch orders BEFORE applying ────────────────────────
    changed = [r for r in rows if r["movement"] == "WOULD MOVE OUT" and r["decided_by_the_bar"]]
    untouched_stale = [r for r in rows
                       if r["movement"] == "WOULD MOVE OUT" and not r["decided_by_the_bar"]]
    check = {
        "question": "Does this bar change the verdict for any document the register "
                    "currently classifies contract-home?",
        "prediction_in_the_dispatch": "It should not — the admitted set was reached on "
                                      "explicit delegation clauses.",
        "documents_currently_admitted_that_the_BAR_excludes":
            [{"document": r["document"], "entries": r["current_contract_home"],
              "form": r["form"], "at": r["delegation_citation"]} for r in changed],
        "entries_affected_by_the_bar": sum(r["current_contract_home"] for r in changed),
        "documents_currently_admitted_that_FAIL_CLAUSE_(a)_ANYWAY":
            [{"document": r["document"], "entries": r["current_contract_home"]}
             for r in untouched_stale],
        "entries_affected_without_the_bar": sum(r["current_contract_home"]
                                                for r in untouched_stale),
        "verdict": ("STOP — the prediction is REFUTED" if changed
                    else "PROCEED — the prediction holds"),
    }

    # ── Task 1's figure: how many §8c-admitted entries are rows of the findings table ──
    tbl = census_table_rows()
    admitted_8c = [d for d in decisions
                   if d["home"].split(":")[0].replace("\\", "/") == "cowork_score_census.md"
                   and d.get("home_section") and d["home_section"]["label"] == "§8c"
                   and d["home_section"]["verdict"] == "ADMIT"]

    def first_line(home: str) -> int:
        return int(home.split(":")[1].split("-")[0])

    in_table = [d["id"] for d in admitted_8c
                if tbl["first_row_line"] <= first_line(d["home"]) <= tbl["last_row_line"]]
    out_table = [d["id"] for d in admitted_8c if d["id"] not in in_table]

    artifact = {
        "purpose": "phase 1p — the delegation bar (W2) measured over the whole home "
                   "population, the pre-apply check the dispatch orders, and the §8c "
                   "mixed-section figure Task 1 rows. NOTHING IS APPLIED HERE.",
        "the_grades_below_are_the_ones_the_check_was_run_against":
            "`form`, `delegation_citation`, `verdict`, `movement` and `verdict_totals` are AS "
            "OF THE CHECK. Where the user has since WRITTEN a delegation (the OI-293 write "
            "list, 2026-08-03), the row additionally carries `form_now`, "
            "`delegation_citation_now` and `verdict_now`, and "
            "`delegation_written_since_the_check` is true. The live grade lives once, in this "
            "tool's FORMS table, which `gen_home_classification.py` imports (#6); the frozen "
            "grade lives once, in GRADE_AT_PHASE_1P, and exists because recomputing the check "
            "from the moved grades would drop two of its three documents and destroy the "
            "finding OI-291 and D-432 both cite (#12).",
        "this_is_a_pre_apply_record":
            "The class figures below are the ones the check was RUN AGAINST, read from each "
            "entry's `home_section.class_before_phase1q` — the value the phase-1q pass records "
            "once and never overwrites. The user ruled the bar APPLIED on 2026-08-03, so the "
            "register's PRESENT classes are the post-apply ones and are at "
            "`tools/audit/decisions/phase1q_reclassification.json`. Recomputing this artifact "
            "from the present classes would report that the prediction holds and destroy the "
            "finding OI-291 and D-432 both cite (#12).",
        "section_level_consequence_moved":
            "The block that stood here reported what the section-level criterion would do to "
            "the five documents then at section granularity. It is SUPERSEDED, not deleted: the "
            "phase-1q pass computes it for every entry of the population, at "
            "`tools/audit/decisions/phase1q_reclassification.json` → `by_document` and "
            "`entries`. Two computations of one thing is the duplication #6 forbids.",
        "the_bar": {
            "admitted_forms": [CLAUSE, NAMED_SECTIONS],
            "not_admitted_forms": [BARE_CITATION, PROVENANCE],
            "clause_a_failure": NOT_NAMED,
            "ruling": "User, 2026-08-03 (phase 1p, W2 — option 4B, 'grade the forms and "
                      "set the bar'). It settles clause (b) of the contract-home criterion, "
                      "which D-430 (the section-level unit) deliberately did not touch.",
            "defense": "ARCHITECTURE.md's 'Full spec:' line sits immediately above a line "
                       "that is an explicit delegation clause; the canonical document "
                       "distinguishes the two acts in adjacent lines. Both are located and "
                       "quoted in `the_defense` below, from the file.",
        },
        "the_defense": {
            "bare_appended_citation": None,     # filled below, from the file
            "explicit_delegation_clause": None,
        },
        "population": {
            "entries": len(population),
            "documents": len(per_doc),
            "note": "the register's `contract-home` + `gap` entries — the classes the "
                    "criterion reaches. `process`, `project-convention` and `unhomed` are "
                    "outside it.",
        },
        "verdict_totals": dict(tally),
        "documents": rows,
        "pre_apply_check": check,
        "census_8c_mixed_section": {
            "needs_vector_table": tbl,
            "admitted_in_8c": [d["id"] for d in admitted_8c],
            "of_those_rows_of_the_findings_table": in_table,
            "of_those_not_rows_of_the_table": out_table,
            "note": "Task 1's figure. The phase-1n note on `open_items/OI-281.md` (§4) and "
                    "the phase-1n `STATUS.md` entry both say NINE of the eleven are rows of "
                    "the table; derived from the file the count is what "
                    "`of_those_rows_of_the_findings_table` holds.",
        },
    }
    dl, dtext = locate("ARCHITECTURE.md", "it does not read a resolved key). Full spec:")
    artifact["the_defense"]["bare_appended_citation"] = {
        "at": f"ARCHITECTURE.md:{dl}", "line": dtext.strip()}
    cl, ctext = locate("ARCHITECTURE.md", "The ratified contract for how this layer ENGAGES")
    artifact["the_defense"]["explicit_delegation_clause"] = {
        "at": f"ARCHITECTURE.md:{cl}", "line": ctext.strip()}

    text = json.dumps(artifact, indent=2, ensure_ascii=False) + "\n"
    if args.check:
        have = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
        if have != text:
            print("STALE vs the files: phase1p_delegation_bar.json does not re-derive")
            return 1
        print("the phase-1p delegation-bar artifact re-derives from the files")
        return 0

    open(OUT, "w", encoding="utf-8", newline="").write(text)
    print(f"wrote {os.path.relpath(OUT, ROOT)}")
    print(f"  population: {len(population)} entries / {len(per_doc)} documents")
    print(f"  under the bar: " + ", ".join(f"{k} {v}" for k, v in sorted(tally.items())))
    print(f"  PRE-APPLY CHECK: {check['verdict']}")
    for r in check["documents_currently_admitted_that_the_BAR_excludes"]:
        print(f"      the bar excludes a currently-admitted document: "
              f"{r['document']} ({r['entries']} entries, {r['form']}, {r['at']})")
    for r in check["documents_currently_admitted_that_FAIL_CLAUSE_(a)_ANYWAY"]:
        print(f"      currently admitted but named in no ratified surface: "
              f"{r['document']} ({r['entries']} entries)")
    print(f"  §8c: {len(admitted_8c)} admitted, {len(in_table)} of them rows of the "
          f"findings table")
    return 0


if __name__ == "__main__":
    sys.exit(main())
