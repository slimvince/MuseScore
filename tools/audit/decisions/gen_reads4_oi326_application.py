#!/usr/bin/env python3
"""READ WAVE 4, Task 1 — the OI-326 ruling MEASURED before it is applied (the user's R5).

WHAT THIS IS.  On 2026-08-04 the user ruled `OPEN_ITEMS.md` OI-326:

    R1 — `ARCHITECTURE.md`'s doc-governance hierarchy clause DELEGATES, but only to the
         members it names EXPLICITLY.  The glob `cowork_layer*_design.md` and the trailing
         ellipsis CONFER NOTHING — a delegation with indeterminate membership could be
         extended by a session, which is the authority rule (g) reserves to the user.
    R5 — the CONDITION on R1: before it is applied, measure how many glob-matched documents
         are already `contract-home` on their own separate anchors.  If the split moves a
         LARGE population, report and STOP.

This tool is that measurement.  **It applies nothing** — it reads
`backbone_decisions.json`, `gen_phase1p_delegation_bar.FORMS` and the clause itself, and
writes only its own artifact.  No entry's `nonspec_kind`, no FORMS grade and no register
file is written here.

WHY A GENERATOR.  `CLAUDE.md` #17(f) and register entry D-431: no figure enters a dispatch,
a report, a status entry or an open-item row by transcription.  Every count below is
computed from the files.

WHAT IS AUTHORED AND WHAT IS DERIVED.
  authored : the three membership-route names and the rule that maps each to R1's verdict
             (explicit name admits on this clause; glob, prose reference and ellipsis do
             not); the "large" threshold is NOT authored — see `the_R5_verdict`.
  derived  : the clause's own span and text, read from `ARCHITECTURE.md`; the DELEGATING
             SENTENCE inside it and the parenthesised list that sentence governs; the
             explicit filenames and the glob pattern, PARSED from that list rather than
             listed here; the glob's matches on disk; the prose reference's filename
             candidates on disk and which of them the reading regime counts as design
             documents; which documents any existing grade was made ON THE DELEGATING
             SENTENCE (by locating each FORMS anchor and asking whether it lands inside it);
             every home document, its entries and their present classes; and the movement.

WHY THE MEMBERSHIP IS PARSED FROM THE DELEGATING SENTENCE AND NOT FROM THE BLOCKQUOTE.  The
blockquote holds more than the delegation: two lines below the list it DEMOTES
`cowork_target_architecture.md` — *"not a second canonical doc"* — which is the opposite act.
Parsing backticked names out of the whole block admits that document as an explicitly-named
delegatee of a sentence that says it is not one.  (Found by reading this tool's own first
output, before it was reported; the first run listed it among the explicit names.)  So the
membership comes from the parenthesised list the delegating predicate governs, and the
"graded on this clause" test uses that sentence's line span, not the block's.

THE ONE THING THIS TOOL DELIBERATELY CANNOT COMPUTE.  R1 moves a document's FORMS GRADE.
An entry's CLASS moves only when `gen_home_classification.py` applies the criteria, and that
pass stays UNRUN under `OPEN_ITEMS.md` OI-305 / OI-319 — and cannot run at all for the wave-2
and wave-3 home documents, which carry no authored `delegation_scope` and no section-kind
judgment, so D-430's kind half (R4: decisive, applied second) has no input.  The entry
figures below are therefore the population ATTACHED to each moving grade, stated as such,
never a projected class.

Run:  python tools/audit/decisions/gen_reads4_oi326_application.py [--check]
"""
from __future__ import annotations

import argparse
import collections
import glob as globmod
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
BACKBONE = os.path.join(HERE, "backbone_decisions.json")
REGIME = os.path.join(HERE, "phase1n_reading_regime.json")
OUT = os.path.join(HERE, "reads4_oi326_application.json")

sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))
from output_encoding import use_utf8_output      # noqa: E402  (path set above)
from gen_phase1p_delegation_bar import (          # noqa: E402  (path set above)
    FORMS, ADMITTING, NOT_NAMED, locate,
)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

# The clause is found by its own opening words, never by line number (a line number in a
# tool is the stale-citation failure D-432's own defense was rewritten to avoid).
CLAUSE_OPENING = "**Doc governance (2026-06-29) — the hierarchy.**"
# The delegating sentence inside it: the parenthesised list, and the predicate that governs
# it.  Both located by their own words for the same reason.
LIST_SUBJECT = "per-component design docs**"
DELEGATING_PREDICATE = "are the **authoritative detail** for their own"
SENTENCE_END = "**referenced** from here."

# AUTHORED — the four membership routes, and what R1 says each confers.  This is the whole
# of the authored judgment in this tool: R1's own words name the glob and the ellipsis as
# conferring nothing and admit "the members it names EXPLICITLY".
ROUTE_VERDICT = {
    "explicit-filename": "ADMITS ON THIS CLAUSE — R1's 'named EXPLICITLY'",
    "glob-match": "CONFERS NOTHING — R1 names the glob",
    "prose-reference": "R1 DOES NOT SETTLE IT — see `the_prose_reference`; goes to R2",
    "ellipsis": "CONFERS NOTHING — R1 names the trailing ellipsis",
}


def read_lines(rel: str) -> list[str]:
    with open(os.path.join(ROOT, rel), encoding="utf-8", errors="replace") as fh:
        return fh.read().splitlines()


def clause_span(lines: list[str]) -> tuple[int, int]:
    """The blockquote the doc-governance clause occupies, located by its opening words."""
    starts = [i for i, ln in enumerate(lines, 1) if CLAUSE_OPENING in ln]
    if len(starts) != 1:
        raise SystemExit(f"the doc-governance clause opening is not unique in ARCHITECTURE.md "
                         f"(lines {starts}); re-read it before measuring")
    first = starts[0]
    last = first
    while last < len(lines) and lines[last].startswith(">"):
        last += 1
    return first, last


def delegating_sentence(lines: list[str], first: int, last: int) -> tuple[int, int, str]:
    """The one sentence inside the block that DELEGATES, and the lines it occupies.

    Located by its own words: it opens on the line carrying the list's subject and closes on
    the line carrying `SENTENCE_END`.  The block's remaining lines state a prohibition and a
    DEMOTION, and are deliberately outside this span — see the module docstring.
    """
    subj = [i for i in range(first, last + 1) if LIST_SUBJECT in lines[i - 1]]
    end = [i for i in range(first, last + 1) if SENTENCE_END in lines[i - 1]]
    if len(subj) != 1 or len(end) != 1 or end[0] < subj[0]:
        raise SystemExit("the delegating sentence is not uniquely locatable inside the "
                         f"doc-governance block (subject {subj}, end {end}); re-read it")
    # the sentence opens mid-line on the line above the subject where the file wraps it
    start = subj[0] - 1 if subj[0] > first and "The **per-layer" in lines[subj[0] - 2] else subj[0]
    return start, end[0], "\n".join(lines[start - 1:end[0]])


def parenthesised_list(text: str) -> str:
    """The parenthesised list the delegating predicate governs, taken from the sentence."""
    i = text.find(LIST_SUBJECT)
    if i < 0:
        raise SystemExit("the delegating sentence does not carry the list's subject")
    j = text.find("(", i)
    if j < 0:
        raise SystemExit("the delegating sentence carries no parenthesised list")
    depth, k = 0, j
    while k < len(text):
        if text[k] == "(":
            depth += 1
        elif text[k] == ")":
            depth -= 1
            if depth == 0:
                break
        k += 1
    if depth != 0:
        raise SystemExit("the parenthesised list is unclosed")
    lst = text[j + 1:k]
    if DELEGATING_PREDICATE not in text[k:]:
        raise SystemExit("the delegating predicate does not follow the parenthesised list; "
                         "the sentence has been reworded and must be re-read")
    return lst


def parse_members(text: str) -> tuple[list[str], list[str], bool]:
    """The list's own naming, parsed from it: backticked names, split glob vs explicit."""
    names = re.findall(r"`([^`]+\.md)`", text)
    explicit = [n for n in names if "*" not in n and "?" not in n]
    globs = [n for n in names if "*" in n or "?" in n]
    return sorted(set(explicit)), sorted(set(globs)), ("…" in text or "..." in text)


def repo_matches(pattern: str) -> list[str]:
    """Files matching a glob pattern, relative to the repository root, in sorted order."""
    hits = globmod.glob(os.path.join(ROOT, pattern))
    return sorted(os.path.relpath(h, ROOT).replace("\\", "/") for h in hits)


def build() -> dict:
    arch = read_lines("ARCHITECTURE.md")
    first, last = clause_span(arch)
    clause_text = "\n".join(arch[first - 1:last])
    s_first, s_last, sentence_text = delegating_sentence(arch, first, last)
    the_list = parenthesised_list(sentence_text)
    explicit, globs, has_ellipsis = parse_members(the_list)

    # The design-document surface the reading regime partitions — used only to say which
    # prose-reference candidates are design documents at all, never to narrow the candidates.
    regime = json.loads(open(REGIME, encoding="utf-8").read())
    surface = {r["document"] for r in regime["read_rows"]} | {
        r["document"] for r in regime["owed_rows"]}

    # ── the register's home population, and each document's present classes ──
    backbone = json.loads(open(BACKBONE, encoding="utf-8").read())
    per_doc: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)
    ids: dict[str, list[str]] = collections.defaultdict(list)
    for d in backbone["decisions"]:
        if d.get("home_is_layer_spec"):
            continue
        if d.get("nonspec_kind") not in ("contract-home", "gap"):
            continue
        doc = d["home"].split(":")[0].replace("\\", "/")
        per_doc[doc][d["nonspec_kind"]] += 1
        ids[doc].append(d["id"])

    # ── which existing grades were made ON THIS CLAUSE (derived, not asserted) ──
    graded_on_clause: dict[str, dict] = {}
    grade_anchor: dict[str, dict] = {}
    for doc, (form, surf, anchor, _why) in FORMS.items():
        if form == NOT_NAMED:
            grade_anchor[doc] = {"form": form, "at": None, "line": None,
                                 "inside_the_clause": False}
            continue
        ln, txt = locate(surf, anchor)
        inside = (surf == "ARCHITECTURE.md" and s_first <= ln <= s_last)
        grade_anchor[doc] = {"form": form, "at": f"{surf}:{ln}",
                             "line": txt.strip(), "inside_the_clause": inside}
        if inside:
            graded_on_clause[doc] = grade_anchor[doc]

    # ── reading-A membership ────────────────────────────────────────────────
    members: dict[str, str] = {}
    for name in explicit:
        members[name] = "explicit-filename"
    glob_hits: dict[str, list[str]] = {}
    for g in globs:
        glob_hits[g] = repo_matches(g)
        for m in glob_hits[g]:
            members.setdefault(m, "glob-match")

    prose_present = "the phrase-boundary design" in clause_text
    prose_candidates = repo_matches("*phrase*boundary*.md")
    for m in prose_candidates:
        members.setdefault(m, "prose-reference")

    # What the ellipsis has been TAKEN to cover in existing grades: a document graded on this
    # clause that none of the determinate routes reaches.  Derived, so it cannot be asserted.
    ellipsis_taken = sorted(d for d in graded_on_clause if d not in members)
    for m in ellipsis_taken:
        members[m] = "ellipsis"

    rows = []
    for doc in sorted(members):
        route = members[doc]
        ga = grade_anchor.get(doc)
        is_home = doc in per_doc
        cur = per_doc.get(doc, collections.Counter())
        on_this_clause = doc in graded_on_clause
        cur_verdict = None
        if ga:
            cur_verdict = ("EXCLUDE" if ga["form"] == NOT_NAMED
                           else ("ADMIT" if ga["form"] in ADMITTING else "EXCLUDE"))
        # R1's effect on the GRADE: only a grade made on this clause can move, and it moves
        # only if the document's route is one R1 says confers nothing.
        if not on_this_clause:
            grade_moves, why = False, ("this document's grade was not made on this clause, so "
                                       "R1 cannot move it")
        elif route == "explicit-filename":
            grade_moves, why = False, ("named EXPLICITLY in the clause, which is precisely what "
                                       "R1 keeps")
        elif route == "prose-reference":
            grade_moves, why = False, ("R1 does not settle the prose reference; the grade is "
                                       "left where it stands and the document goes to the R2 "
                                       "write list")
        else:
            grade_moves, why = True, (f"graded on this clause by the {route} route, which R1 "
                                      "says confers nothing")
        rows.append({
            "document": doc,
            "membership_route": route,
            "what_R1_says_this_route_confers": ROUTE_VERDICT[route],
            "is_a_home_document_in_the_register": is_home,
            "entries": sum(cur.values()),
            "entry_ids": sorted(ids.get(doc, [])),
            "present_classes": dict(cur),
            "present_contract_home_entries": cur.get("contract-home", 0),
            "graded_in_FORMS": bool(ga),
            "grade_form": ga["form"] if ga else None,
            "grade_anchor_at": ga["at"] if ga else None,
            "grade_anchor_line": ga["line"] if ga else None,
            "grade_was_made_on_this_clause": on_this_clause,
            "grade_is_on_a_separate_anchor": bool(ga) and ga["form"] != NOT_NAMED
            and not on_this_clause,
            "present_verdict": cur_verdict,
            "grade_moves_under_R1": grade_moves,
            "why": why,
        })

    homes = [r for r in rows if r["is_a_home_document_in_the_register"]]
    already_ch = [r for r in homes if r["present_contract_home_entries"] > 0]
    sep_anchor = [r for r in homes if r["grade_is_on_a_separate_anchor"]]
    ch_on_sep = [r for r in already_ch if r["grade_is_on_a_separate_anchor"]]
    only_naming = [r for r in homes
                   if r["grade_was_made_on_this_clause"]]
    moving = [r for r in rows if r["grade_moves_under_R1"]]
    glob_homes = [r for r in homes if r["membership_route"] == "glob-match"]
    glob_ch_sep = [r for r in glob_homes if r["grade_is_on_a_separate_anchor"]
                   and r["present_contract_home_entries"] > 0]

    return {
        "header": {
            "purpose": "READ WAVE 4 Task 1 — the R5 measurement the user made a CONDITION on "
                       "applying R1 (OI-326). Nothing is applied here.",
            "generator": "tools/audit/decisions/gen_reads4_oi326_application.py",
            "dispatch": "cc_instruction_reads_4.md",
            "ruling": {
                "R1": "ARCHITECTURE.md's doc-governance hierarchy clause DELEGATES, but only "
                      "to the members it names EXPLICITLY. The glob `cowork_layer*_design.md` "
                      "and the trailing ellipsis CONFER NOTHING — a delegation with "
                      "indeterminate membership could be extended by a session, which is the "
                      "authority rule (g) reserves to the user. (User, 2026-08-04, OI-326.)",
                "R5": "Before R1 is applied, measure how many glob-matched documents are "
                      "already `contract-home` on their own separate anchors. If the split "
                      "moves a LARGE population, report and STOP. (User, 2026-08-04.)",
            },
            "what_this_tool_does_not_compute":
                "R1 moves a FORMS GRADE. An entry's CLASS moves only when "
                "`gen_home_classification.py` applies the criteria, and that pass stays UNRUN "
                "under OI-305 / OI-319 — and cannot run at all for the wave-2 and wave-3 home "
                "documents, which carry no authored `delegation_scope` and no section-kind "
                "judgment, so D-430's kind half (R4) has no input. Every entry figure below is "
                "the population ATTACHED to a grade, never a projected class.",
        },
        "the_clause": {
            "block_at": f"ARCHITECTURE.md:{first}-{last}",
            "located_by": CLAUSE_OPENING,
            "block_text": clause_text,
            "the_delegating_sentence_at": f"ARCHITECTURE.md:{s_first}-{s_last}",
            "the_delegating_sentence": sentence_text,
            "the_parenthesised_list": the_list.strip(),
            "why_the_sentence_and_not_the_block":
                "The block holds more than the delegation. Two lines below the list it DEMOTES "
                "`cowork_target_architecture.md` — 'not a second canonical doc' — which is the "
                "opposite act, and a line above the demotion states a prohibition. Parsing "
                "backticked names out of the whole block admits the demoted document as an "
                "explicitly-named delegatee of a sentence that says it is not one; this tool's "
                "own first run did exactly that, which is how the span was narrowed. Membership "
                "is therefore parsed from the parenthesised list the delegating predicate "
                "governs, and the 'graded on this clause' test uses the sentence's line span.",
        },
        "reading_A_membership": {
            "note": "Reading A is OI-326's own first reading — the clause is a delegation "
                    "clause. Its membership is parsed FROM the parenthesised list, not listed "
                    "here.",
            "explicit_filenames": explicit,
            "glob_patterns": globs,
            "glob_matches_on_disk": glob_hits,
            "the_prose_reference": {
                "present_in_the_clause": prose_present,
                "phrase": "the phrase-boundary design",
                "filename_candidates_on_disk": prose_candidates,
                "of_those_in_the_reading_regimes_design_document_surface":
                    [c for c in prose_candidates if c in surface],
                "why_R1_does_not_settle_it":
                    "R1's words name the GLOB and the TRAILING ELLIPSIS as conferring nothing, "
                    "and admit the members named EXPLICITLY. A prose description is neither: it "
                    "names no file, and the design-document candidates derived above are more "
                    "than one, so its membership is indeterminate in exactly the way R1's own "
                    "defense objects to — but R1 does not say so, and reading it in is the "
                    "extension rule (g) withholds from a session. Routed to R2 (the OI-293 "
                    "write list) rather than decided. Nothing turns on it either way: the "
                    "documents concerned are graded NOT_NAMED, which is where they stay.",
            },
            "the_ellipsis": {
                "present_in_the_clause": has_ellipsis,
                "what_it_has_been_taken_to_cover_in_existing_grades": ellipsis_taken,
                "note": "Derived: a document whose FORMS grade was made on a line inside the "
                        "delegating sentence and which none of the determinate routes reaches. "
                        "An empty list means no existing grade rests on the ellipsis.",
            },
        },
        "documents": rows,
        "the_R5_measurement": {
            "question": "How many glob-matched documents are already `contract-home` on their "
                        "own separate anchors, and how large is the population the split moves?",
            "reading_A_members_total": len(rows),
            "of_those_home_documents_in_the_register": len(homes),
            "home_documents_holding_at_least_one_contract_home_entry": len(already_ch),
            "home_documents_graded_on_a_SEPARATE_anchor_of_their_own": len(sep_anchor),
            "home_documents_contract_home_ON_a_separate_anchor": [
                {"document": r["document"], "route": r["membership_route"],
                 "contract_home_entries": r["present_contract_home_entries"],
                 "separate_anchor": r["grade_anchor_at"]} for r in ch_on_sep],
            "glob_matched_home_documents": len(glob_homes),
            "glob_matched_home_documents_already_contract_home_on_a_separate_anchor":
                len(glob_ch_sep),
            "home_documents_whose_grade_rests_on_THIS_clause": [
                {"document": r["document"], "route": r["membership_route"],
                 "entries": r["entries"], "present_classes": r["present_classes"]}
                for r in only_naming],
            "grades_that_MOVE_under_R1": [
                {"document": r["document"], "route": r["membership_route"],
                 "from": r["present_verdict"], "entries": r["entries"], "why": r["why"]}
                for r in moving],
            "grades_that_move_under_R1_count": len(moving),
            "entries_attached_to_a_moving_grade": sum(r["entries"] for r in moving),
        },
        "the_R5_verdict": {
            "verdict": ("PROCEED — no grade moves under R1" if not moving else
                        "REPORT AND STOP — R1 moves at least one grade; the population is "
                        "enumerated above and the user decides whether it is large"),
            "why_no_threshold_is_authored":
                "R5 says a LARGE moving population is a stop and does not define large. This "
                "tool therefore reports the number and does not judge it (#17f, D-431): a "
                "threshold invented here would be a session deciding the condition the user "
                "attached to their own ruling. The verdict above is mechanical — it turns on "
                "whether the count is zero, which is the one reading that needs no threshold.",
            "the_reason_the_count_is_what_it_is":
                "Derived above and stated so a reader need not reconstruct it: the register's "
                "existing grades were made on the STRONGEST naming each document has (the FORMS "
                "table's own rule), and for every glob-matched and prose-referenced member that "
                "strongest naming is a separate anchor — an explicit delegation clause for the "
                "four layer specifications, a bare appended citation for the rest, and no naming "
                "at all for the documents graded NOT_NAMED. Only the explicitly-named members "
                "were ever graded on this clause, and R1 keeps exactly those.",
        },
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="rebuild into memory and report whether the artifact matches")
    args = ap.parse_args()

    built = build()
    text = json.dumps(built, indent=2, ensure_ascii=False) + "\n"
    if args.check:
        have = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
        if have != text:
            print("STALE vs the files: reads4_oi326_application.json does not re-derive")
            return 1
        print("the OI-326 application measurement re-derives from the files")
        return 0

    open(OUT, "w", encoding="utf-8", newline="").write(text)
    m = built["the_R5_measurement"]
    print(f"wrote {os.path.relpath(OUT, ROOT)}")
    print(f"  clause block: {built['the_clause']['block_at']}   delegating sentence: "
          f"{built['the_clause']['the_delegating_sentence_at']}")
    print(f"  reading-A members: {m['reading_A_members_total']}  "
          f"(home documents: {m['of_those_home_documents_in_the_register']})")
    print(f"  glob-matched home documents: {m['glob_matched_home_documents']}  "
          f"of which already contract-home on a separate anchor: "
          f"{m['glob_matched_home_documents_already_contract_home_on_a_separate_anchor']}")
    print(f"  grades that move under R1: {m['grades_that_move_under_R1_count']}  "
          f"(entries attached: {m['entries_attached_to_a_moving_grade']})")
    print(f"  R5: {built['the_R5_verdict']['verdict']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
