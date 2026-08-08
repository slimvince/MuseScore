#!/usr/bin/env python3
"""THE ONE HOME-CLASSIFICATION PASS — every ratified criterion applied at once, to every entry.

WHAT THIS IS.  The user ruled on 2026-08-03 (phase 1q, X1) that the register's home classes are
brought into line with the criteria in force in **one re-classification pass over the whole home
population**, with a WRITE LIST for the homes the record means to keep, rather than forward-only
or by revising the bar.  `OPEN_ITEMS.md` OI-291 is the row that ruling answers.

THE CRITERIA IN FORCE, in the order this tool applies them, each cited to its register entry:

  1. **Clause (a) — the fifth home case** (`OPEN_ITEMS.md` OI-268, user-ratified 2026-08-02): a
     home must be DELEGATED to by a user-ratified surface.  A document named in none of the three
     is excluded before any later clause is reached.
  2. **The delegation bar — D-432** (user, 2026-08-03): which WORDINGS delegate.  An explicit
     delegation clause or a named home with sections admits; a bare appended citation or a
     provenance attribution does not.  The per-document form grade is authored ONCE, in
     `gen_phase1p_delegation_bar.py`'s FORMS table, and imported here — it is not restated (#6).
  3. **The section-level unit — D-430** (user, 2026-08-03): the unit is a SECTION.  A section is
     admitted when a delegation reaches it AND the section STATES RULES rather than recording
     findings.  Both halves are applied here; neither was applied outside phase 1n's staged 46.

  The document-kind test and the delegation-specificity criterion are SUPERSEDED (D-430's own
  provenance says so, and phase 1n recorded them as steps toward it).  They are not applied.

HOW A WHOLE-DOCUMENT DELEGATION IS READ, stated because it is load-bearing and it is an
interpretation, not a mechanism.  A delegation that names a document and no section — *"The
ratified contract for this layer is X"* — reaches EVERY section of that document; a delegation
that names sections reaches those sections and their subsections and no others.  The ground is
the record's own precedent, not a preference: `OPEN_ITEMS.md` OI-290 states it in terms —
*"`ARCHITECTURE.md:1331` delegates 'this layer' and admits all sixteen of that document's
entries"* — recorded there as the reason the narrower reading was not adopted.  The STRICT
alternative (no section is named, so no section is admitted) is recorded in the artifact under
`the_reading_of_a_whole_document_delegation` and is NOT adopted; it would empty the class.

WHAT IS AUTHORED AND WHAT IS DERIVED.
  authored : `section_home_criterion.documents` in `backbone_decisions.json` — per home document,
             the delegation's SCOPE (document / named sections), and per section that holds an
             entry, whether that section STATES RULES, each with the reason it was so judged and
             the reading it was judged from.  The write-list cases and their draft delegation
             wordings.  Nothing else.
  derived  : the population and its present classes; each entry's enclosing section; which
             sections a delegation reaches; the criterion that decides each entry; the new class;
             the movement against the register's present state; and every count.

WHAT THIS TOOL WRITES.  `nonspec_kind` and `home_section` on every entry of the population, in
`backbone_decisions.json`, plus the LIVE artifact `home_classification.json`.  The former class
is preserved on the entry (#12) — `former_class` keeps the earliest recorded pre-classification
value, `class_before_phase1q` the value immediately before the first pass, `class_before_phase1r`
the value before the second, and `class_before_the_2026_08_08_apply` the value before the third —
so no movement is lost and a re-run cannot overwrite any of them.

★ THE PHASE-1Q ARTIFACT IS HISTORICAL AND IS NEVER WRITTEN BY THIS TOOL AGAIN (user, 2026-08-08,
Ruling 1 of `cowork_rulings_2026_08_08_pre_away.md`; the change to this tool is licensed by that
ruling, D-436).  `phase1q_reclassification.json` is the record of what the phase-1q pass found,
frozen at the snapshot established on 2026-08-04 under ruling R2 of
`cc_instruction_phase1_delegations_and_corrections.md`.  Until this ruling the applying run
rewrote it from the day's inputs, so running the apply would have destroyed the record OI-291 and
D-432 both cite — the `OPEN_ITEMS.md` OI-301 hazard, which is why OI-305 and OI-319 held the
applying run un-run for a month and OI-350 measured what that hold then cost: a delegation the
user writes lands its entries in a class that is false of them and stops six generators.  The
hazard is discharged by FREEZING the record rather than by holding the writer forever, which is
the epoch treatment this tool already applies to its own class fields, applied one level up — to
the artifact.  Two things follow and both are mechanical rather than asserted:

  * the live derived view moves to `home_classification.json`, so a run says what the tree holds
    TODAY and the phase-1q record goes on saying what phase 1q found (#12);
  * this tool never writes the phase-1q file again, and it STOPS if the snapshot that carries the
    phase-1q record no longer hashes to the value its establishment record froze — so *never
    regenerated over* is enforced by the run rather than promised by a docstring (#19).

★ AND ONE FACT MEASURED AT THE FIRST RUN UNDER THE RULING, WHICH THE RULING'S PREMISE DID NOT
CARRY (CC, 2026-08-08).  The file named for phase 1q is NOT the phase-1q record at HEAD.  The
2026-08-04 establishment froze the two as byte-identical; at HEAD they are not, the snapshot is
intact at its established hash, and what moved is the live file, whose content differs across the
recent commits as well.  So the applying run has been performed by more than one wave since the
snapshot was taken, each rewriting that file, and the rows describing the applying run as held
un-run describe the LAST wave rather than the month.  The record survives because the snapshot was
taken; the file named for it holds neither the phase-1q classification nor the present one.  The
measurement is the generated artifact `tools/audit/decisions/phase1q_record_divergence.json` and no
value from it is transcribed here (D-431).  Whether the stale file is restored from the snapshot,
renamed for what it holds, or removed is a FILING DECISION about a committed artifact and is the
user's, not this tool's — surfaced in `cowork_away_returns.md` rather than taken.

THIS TOOL REPLACES `gen_section_homes.py`, which applied D-430 alone to a staged five documents.
Two appliers of one criterion is the duplication #6 forbids, so that file is deleted rather than
left beside this one.

Run:
    python tools/audit/decisions/gen_home_classification.py            # derive, apply and write
    python tools/audit/decisions/gen_home_classification.py --check    # re-derive and diff both
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
BACKBONE = os.path.join(HERE, "backbone_decisions.json")
OUT = os.path.join(HERE, "home_classification.json")

# The frozen phase-1q record and the snapshot it is established against. Neither is written here;
# both are READ, and a difference between them stops the run (see `frozen_record_intact`).
FROZEN = os.path.join(HERE, "phase1q_reclassification.json")
SNAPSHOT = os.path.join(HERE, "snapshot_2026-08-04_pre_home_classification_apply",
                        "phase1q_reclassification.json")

sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))
from output_encoding import use_utf8_output      # noqa: E402  (path set above)
from gen_phase1p_delegation_bar import (          # noqa: E402  (path set above)
    FORMS, ADMITTING, NOT_NAMED, locate, mentions,
)

use_utf8_output()   # OI-297 — the `STALE vs the files:` block must survive a non-console stdout

HEADING = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")


# ── the document's own headings, and where a cited line sits among them ──────
def headings_of(rel: str) -> list[tuple[int, int, str]]:
    """(line, level, text) for every markdown heading in the file, in file order."""
    path = os.path.join(ROOT, rel)
    out: list[tuple[int, int, str]] = []
    with open(path, encoding="utf-8", errors="replace") as fh:
        for i, line in enumerate(fh.read().splitlines(), 1):
            m = HEADING.match(line)
            if m:
                out.append((i, len(m.group(1)), m.group(2)))
    return out


def cited_line(home: str) -> int | None:
    parts = home.split(":")
    if len(parts) < 2:
        return None
    m = re.match(r"(\d+)", parts[1])
    return int(m.group(1)) if m else None


def enclosing(headings: list[tuple[int, int, str]], line: int) -> tuple[int, int, str] | None:
    """The nearest preceding heading — the most specific section the line sits in."""
    found = None
    for h in headings:
        if h[0] < line:
            found = h
        else:
            break
    return found


def label_for(level: int, text: str) -> str:
    """A short citable label for a section.

    Rule, stated because it is a judgment made once and then applied mechanically: if the
    heading opens with a section number (`8c.`, `5.3`, `9.`), the label is that number with a
    section mark.  If it does not, the heading has no number to cite and the label is the
    heading's own text up to its first em dash or parenthesis, in quotation marks.  A level-1
    heading is the document title, and a home above the first real section sits in the
    document's opening block, which is what the label then says.
    """
    if level == 1:
        return "the opening block (above the first section heading)"
    m = re.match(r"^(\d+[0-9a-z]*(?:\.\d+)*)\.?\s", text)
    if m:
        return "§" + m.group(1)
    short = re.split(r"\s+[—(]", text)[0].strip()
    return f"“{short}”"


def descendants(headings: list[tuple[int, int, str]], head_line: int) -> set[int]:
    """A heading's own line plus every heading nested under it (level strictly deeper)."""
    idx = next((i for i, h in enumerate(headings) if h[0] == head_line), None)
    if idx is None:
        raise SystemExit(f"no heading at line {head_line}")
    level = headings[idx][1]
    out = {head_line}
    for h in headings[idx + 1:]:
        if h[1] <= level:
            break
        out.add(h[0])
    return out


# ── the pass ────────────────────────────────────────────────────────────────
def home_population(backbone: dict) -> list[dict]:
    """The entries the home-class criteria reach — the ONE definition of that population.

    `process`, `project-convention` and `unhomed` entries, and every entry homed in a layer
    specification, are outside it (the register's own `home_rule`).  Factored out so a reader
    of the population — `gen_outstanding_delegations.py` — imports it rather than restating
    the predicate (#6).
    """
    return [d for d in backbone["decisions"]
            if not d.get("home_is_layer_spec")
            and d.get("nonspec_kind") in ("contract-home", "gap")]


def classify(backbone: dict) -> tuple[list[dict], list[dict]]:
    crit = backbone["section_home_criterion"]
    authored = crit["documents"]

    population = home_population(backbone)

    docs = sorted({d["home"].split(":")[0].replace("\\", "/") for d in population})
    missing = [x for x in docs if x not in authored]
    if missing:
        raise SystemExit(f"home document(s) with no authored delegation scope: {missing}")
    stale = [x for x in authored if x not in docs]
    if stale:
        raise SystemExit(f"authored judgment for a document that is nobody's home: {stale}")

    heads: dict[str, list[tuple[int, int, str]]] = {d: headings_of(d) for d in docs}
    changed: list[dict] = []
    rows: list[dict] = []
    used_kind: dict[tuple[str, int], bool] = {}

    # Per document: the bar's verdict, and the set of heading lines a delegation reaches.
    doc_state: dict[str, dict] = {}
    for doc in docs:
        form, surface, anchor, why_form = FORMS[doc]
        spec = authored[doc]
        if form == NOT_NAMED:
            citation, line_text = None, None
        else:
            ln, line_text = locate(surface, anchor)
            citation = f"{surface}:{ln}"
        verdict = "ADMIT" if form in ADMITTING else "EXCLUDE"

        reached: set[int] | None = None
        if verdict == "ADMIT":
            if spec["delegation_scope"] == "document":
                reached = {h[0] for h in heads[doc]}
            elif spec["delegation_scope"] == "sections":
                reached = set()
                by_line = {h[0]: h for h in heads[doc]}
                for sec in spec["delegated_sections"]:
                    h = by_line.get(sec["heading_line"])
                    if h is None:
                        raise SystemExit(f"{doc}: no heading at line {sec['heading_line']} "
                                         "(a delegated section points at it)")
                    if h[2] != sec["heading_text"]:
                        raise SystemExit(f"{doc}:{sec['heading_line']}: heading is {h[2]!r}, "
                                         f"the authored block records {sec['heading_text']!r}")
                    reached |= descendants(heads[doc], sec["heading_line"])
            else:
                raise SystemExit(f"{doc}: delegation_scope {spec['delegation_scope']!r} is not "
                                 "'document' or 'sections' on an ADMITTED document")
        doc_state[doc] = {"form": form, "verdict": verdict, "citation": citation,
                          "delegation_line": (line_text.strip() if line_text else None),
                          "why_this_grade": why_form, "reached": reached,
                          "scope": spec["delegation_scope"]}

        # every authored kind judgment must sit on a real heading with the recorded text
        for k in spec.get("section_kind", []):
            h = next((x for x in heads[doc] if x[0] == k["heading_line"]), None)
            if h is None:
                raise SystemExit(f"{doc}: no heading at line {k['heading_line']} "
                                 "(a section-kind judgment points at it)")
            if h[2] != k["heading_text"]:
                raise SystemExit(f"{doc}:{k['heading_line']}: heading is {h[2]!r}, the authored "
                                 f"kind judgment records {k['heading_text']!r}")
            used_kind[(doc, k["heading_line"])] = False

    for d in population:
        doc = d["home"].split(":")[0].replace("\\", "/")
        st = doc_state[doc]
        line = cited_line(d["home"])
        if line is None:
            raise SystemExit(f"{d['id']}: home {d['home']!r} carries no line anchor; a section "
                             "home cannot be derived from a bare file name")
        enc = enclosing(heads[doc], line)
        if enc is None:
            raise SystemExit(f"{d['id']}: home line {line} in {doc} precedes every heading")
        hline, hlevel, htext = enc

        kind_row = None
        for k in authored[doc].get("section_kind", []):
            if k["heading_line"] == hline:
                kind_row = k
                break

        if st["verdict"] == "EXCLUDE":
            want = "gap"
            if st["form"] == NOT_NAMED:
                decided_by = ("clause (a), the fifth home case (OI-268) — this document is named "
                              "in none of the three user-ratified surfaces, so no delegation "
                              "exists to grade")
            else:
                decided_by = (f"D-432, the delegation bar — the strongest delegation is a "
                              f"{st['form']}, which the bar does not admit")
            delegated, states_rules = None, None
        else:
            delegated = hline in st["reached"]
            if not delegated:
                want, states_rules = "gap", None
                decided_by = ("D-430, the section-level unit — the delegation reaches named "
                              "sections only, and no delegation names this section")
            else:
                if kind_row is None:
                    raise SystemExit(
                        f"{d['id']} ({doc} {label_for(hlevel, htext)}, heading line {hline}): the "
                        "delegation reaches this section and no authored judgment says whether it "
                        "STATES RULES. Read the section and record the judgment before running.")
                used_kind[(doc, hline)] = True
                states_rules = kind_row["states_rules"]
                want = "contract-home" if states_rules else "gap"
                decided_by = ("D-430, the section-level unit — the delegation reaches this "
                              "section and it " + ("STATES RULES" if states_rules
                                                   else "RECORDS FINDINGS"))

        prior = d.get("home_section") or {}
        former = prior.get("former_class", d.get("nonspec_kind"))
        before = prior.get("class_before_phase1q", d.get("nonspec_kind"))
        # A third frozen epoch. The user WROTE delegations on 2026-08-03 (the OI-293 write
        # list), so this pass runs a second time over classes the first pass already moved.
        # Without an epoch of its own, the phase-1q RESULT — the class each entry carried
        # between the two passes — is overwritten and lost (#12). Frozen the same way the
        # others are: read back from the entry, so a re-run cannot overwrite it.
        before_1r = prior.get("class_before_phase1r", d.get("nonspec_kind"))
        # A FOURTH frozen epoch, for the same reason the third was added and by the same
        # construction. The user WROTE three more delegations on 2026-08-08 (the document-route
        # ruling, route (i)), so this pass runs a third time over classes the earlier passes had
        # already moved. Without an epoch of its own, the class each entry carried BETWEEN the
        # phase-1r pass and this one is overwritten and lost (#12) — and it can no longer be
        # recovered from the derived artifact either, because that artifact is now the frozen
        # phase-1q record and stops being rewritten at every pass. Read back from the entry, so a
        # re-run cannot overwrite it.
        before_0808 = prior.get("class_before_the_2026_08_08_apply", d.get("nonspec_kind"))
        hs = {
            "heading_line": hline,
            "section": ("#" * hlevel) + " " + htext,
            "label": label_for(hlevel, htext),
            "delegated": delegated,
            "delegation": (st["citation"] if st["citation"] else
                           "named in no user-ratified surface"),
            "states_rules": states_rules,
            "verdict": "ADMIT" if want == "contract-home" else "EXCLUDE",
            "decided_by": decided_by,
            "former_class": former,
            "class_before_phase1q": before,
            "class_before_phase1r": before_1r,
            "class_before_the_2026_08_08_apply": before_0808,
        }
        if d.get("home_section") != hs:
            changed.append({"id": d["id"], "what": "home_section", "to": hs["label"]})
        d["home_section"] = hs

        if d.get("nonspec_kind") != want:
            changed.append({"id": d["id"], "what": "nonspec_kind",
                            "from": d.get("nonspec_kind"), "to": want})
            d["nonspec_kind"] = want

        rows.append({
            "id": d["id"], "title": d["title"], "document": doc,
            "home": d["home"], "section": hs["label"], "section_heading_line": hline,
            "delegation_form": st["form"], "delegation_scope": st["scope"],
            "delegation_at": st["citation"], "delegation_line": st["delegation_line"],
            "section_delegated": delegated, "section_states_rules": states_rules,
            "class_before_phase1q": before, "class_before_phase1r": before_1r,
            "class_before_the_2026_08_08_apply": before_0808,
            "class_after": want,
            "moves": before != want, "moves_since_phase1q": before_1r != want,
            "moves_since_phase1r": before_0808 != want,
            "decided_by": decided_by,
        })

    unused = [f"{k[0]}:{k[1]}" for k, v in used_kind.items() if not v]
    if unused:
        raise SystemExit("authored section-kind judgment(s) that decide no entry — remove them or "
                         f"say why they are kept: {unused}")

    # entries outside the population must not keep a stale section block
    for d in backbone["decisions"]:
        if d in population:
            continue
        if "home_section" in d:
            del d["home_section"]
            changed.append({"id": d["id"], "what": "home_section REMOVED (outside the population)"})
    return rows, changed


def build_artifact(backbone: dict, rows: list[dict]) -> dict:
    crit = backbone["section_home_criterion"]
    per_doc: dict[str, dict] = {}
    for r in rows:
        rec = per_doc.setdefault(r["document"], {
            "entries": 0, "before": collections.Counter(), "after": collections.Counter(),
            "moves_out": 0, "moves_in": 0,
            "delegation_form": r["delegation_form"], "delegation_scope": r["delegation_scope"],
            "delegation_at": r["delegation_at"], "delegation_line": r["delegation_line"],
            "sections": {},
        })
        rec["entries"] += 1
        rec["before"][r["class_before_phase1q"]] += 1
        rec["after"][r["class_after"]] += 1
        if r["moves"] and r["class_after"] == "gap":
            rec["moves_out"] += 1
        if r["moves"] and r["class_after"] == "contract-home":
            rec["moves_in"] += 1
        if r["moves_since_phase1q"] and r["class_after"] == "gap":
            rec["moves_out_since_phase1q"] = rec.get("moves_out_since_phase1q", 0) + 1
        if r["moves_since_phase1q"] and r["class_after"] == "contract-home":
            rec["moves_in_since_phase1q"] = rec.get("moves_in_since_phase1q", 0) + 1
        s = rec["sections"].setdefault(r["section"], {
            "heading_line": r["section_heading_line"], "delegated": r["section_delegated"],
            "states_rules": r["section_states_rules"], "entries": [], "class_after": r["class_after"],
        })
        s["entries"].append(r["id"])
    for rec in per_doc.values():
        rec["before"] = dict(rec["before"])
        rec["after"] = dict(rec["after"])

    moved = [r for r in rows if r["moves"]]
    out_rows = [r for r in moved if r["class_after"] == "gap"]
    in_rows = [r for r in moved if r["class_after"] == "contract-home"]
    moved_1r = [r for r in rows if r["moves_since_phase1q"]]
    moved_0808 = [r for r in rows if r["moves_since_phase1r"]]

    return {
        "purpose": "THE LIVE HOME CLASSIFICATION — every ratified home criterion applied at once "
                   "to the whole home population, per entry, with every former class preserved "
                   "(#12). Generated: no class here is hand-assigned. The user ruled this shape "
                   "on 2026-08-03 (option A3) at `OPEN_ITEMS.md` OI-291, and ruled on 2026-08-08 "
                   "(Ruling 1, `cowork_rulings_2026_08_08_pre_away.md`) that the phase-1q record "
                   "is HISTORICAL and this live view is written beside it rather than over it.",
        "generated_by": "tools/audit/decisions/gen_home_classification.py",
        "★_this_file_is_the_LIVE_view_and_the_phase_1q_record_is_a_different_file": (
            "`tools/audit/decisions/phase1q_reclassification.json` is the record of what the "
            "phase-1q pass found, frozen at the snapshot established on 2026-08-04 and never "
            "written again. This file is what the criteria say about the tree TODAY. A reader "
            "after the pre-apply classes wants the frozen record; a reader after the present "
            "classes wants this one. Before this split there was one file doing both jobs, which "
            "is why running the applying pass would have destroyed the phase-1q record — the "
            "OI-301 hazard OI-305 and OI-319 held the run against, and the cause OI-350 measured "
            "the cost of."
        ),
        "criteria_applied": [
            "clause (a), the fifth home case — OI-268, user-ratified 2026-08-02",
            "D-432, the delegation bar — user, 2026-08-03",
            "D-430, the section-level unit, BOTH halves — user, 2026-08-03",
        ],
        "criteria_not_applied": [
            "the delegation-specificity criterion — superseded by D-430",
            "the document-kind test — superseded by D-430",
        ],
        "the_reading_of_a_whole_document_delegation": crit["whole_document_reading"],
        "population": {"entries": len(rows), "documents": len(per_doc)},
        "totals": {
            "class_before": dict(collections.Counter(r["class_before_phase1q"] for r in rows)),
            "class_after": dict(collections.Counter(r["class_after"] for r in rows)),
            "entries_moved": len(moved),
            "moved_to_gap": len(out_rows),
            "moved_to_contract_home": len(in_rows),
            "decided_by": dict(collections.Counter(
                r["decided_by"].split(" — ")[0] for r in rows)),
        },
        "by_document": per_doc,
        "entries": rows,
        "the_phase_1r_re_run": {
            "why": "The user WROTE delegations on 2026-08-03 (the OI-293 write list) for the "
                   "six documents this pass had reported losing entries. The pass therefore "
                   "runs a SECOND time, over classes it had itself moved. `class_before_"
                   "phase1q` still holds the state before the FIRST run, so `totals` and "
                   "`by_document` below are unchanged in meaning; this block is the movement "
                   "caused by the written delegations alone.",
            "entries_moved_since_phase1q": len(moved_1r),
            "moved_to_contract_home": [
                {"id": r["id"], "document": r["document"], "section": r["section"],
                 "from": r["class_before_phase1r"], "decided_by": r["decided_by"]}
                for r in moved_1r if r["class_after"] == "contract-home"],
            "moved_to_gap": [
                {"id": r["id"], "document": r["document"], "section": r["section"],
                 "from": r["class_before_phase1r"], "decided_by": r["decided_by"]}
                for r in moved_1r if r["class_after"] == "gap"],
            "write_list_documents_that_did_not_move_in_whole": sorted({
                r["document"] for r in rows
                if r["class_after"] == "gap"
                and r["document"] in {w["document"] for w in crit["write_list"]}}),
        },
        "the_2026_08_08_apply": {
            "why": "The user WROTE three more delegations on 2026-08-08 (the document-route "
                   "ruling, route (i)) and every read wave since phase 1r entered register "
                   "entries whose `home_section` had no writer while the applying run was held. "
                   "This block is the movement caused by everything since the phase-1r pass — "
                   "graded against `class_before_the_2026_08_08_apply`, the fourth frozen epoch, "
                   "which is read back from each entry and never overwritten (#12).",
            "entries_moved_since_phase1r": len(moved_0808),
            "moved_to_contract_home": [
                {"id": r["id"], "document": r["document"], "section": r["section"],
                 "from": r["class_before_the_2026_08_08_apply"], "decided_by": r["decided_by"]}
                for r in moved_0808 if r["class_after"] == "contract-home"],
            "moved_to_gap": [
                {"id": r["id"], "document": r["document"], "section": r["section"],
                 "from": r["class_before_the_2026_08_08_apply"], "decided_by": r["decided_by"]}
                for r in moved_0808 if r["class_after"] == "gap"],
        },
        "moved_out": [{"id": r["id"], "document": r["document"], "section": r["section"],
                       "decided_by": r["decided_by"]} for r in out_rows],
        "moved_in": [{"id": r["id"], "document": r["document"], "section": r["section"],
                      "decided_by": r["decided_by"]} for r in in_rows],
        "write_list": crit["write_list"],
        "not_write_list_cases": crit["not_write_list_cases"],
    }


def sha256(path: str) -> str:
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def frozen_record_intact() -> None:
    """The phase-1q record is HISTORICAL — stop if the copy that carries it has moved.

    Ruling 1 of 2026-08-08 discharges the OI-301 hazard by FREEZING the phase-1q record rather
    than by holding this tool's applying run forever.  A freeze nobody checks is a promise, and
    #19 does not admit one: what makes it a fact is that the run refuses to proceed while the
    bytes that carry the record have moved.  Checked on every run, before anything is written,
    because the failure it guards against is precisely a run that rewrote the record.

    ★ WHICH FILE CARRIES THE RECORD, MEASURED RATHER THAN ASSUMED (CC, 2026-08-08, at the first
    run under this ruling).  It is the SNAPSHOT, and not the file named for phase 1q.  The
    establishment record of 2026-08-04 froze the two as byte-identical; they are not identical at
    HEAD, and the divergence is not damage to the snapshot — the snapshot still hashes to the
    established value.  What moved is `phase1q_reclassification.json`, which later waves
    regenerated, so the applying run this tool performs has been run more than once since the
    snapshot was taken and has rewritten that file each time.  The file named for phase 1q
    therefore holds NEITHER the phase-1q classification NOR the present one, and this ruling's
    freeze is what stops it being rewritten again.  What the freeze protects is consequently the
    snapshot, which is what is checked here.  The measurement is the generated artifact
    `tools/audit/decisions/phase1q_record_divergence.json`; no value is transcribed into this
    docstring (D-431).  Whether the stale file is restored from the snapshot, renamed for what it
    holds, or removed is a FILING DECISION about an artifact already committed, and it is left to
    the user rather than taken here (surfaced in `cowork_away_returns.md`).
    """
    if not os.path.exists(SNAPSHOT):
        raise SystemExit("STOP: the established phase-1q snapshot is missing: "
                         + os.path.relpath(SNAPSHOT, ROOT))
    established = json.loads(open(
        os.path.join(os.path.dirname(SNAPSHOT), "establishment.json"), encoding="utf-8").read())
    recorded = next(c["sha256_snapshot"] for c in established["checks"]
                    if c["check"].startswith("1 -"))
    if sha256(SNAPSHOT) != recorded:
        raise SystemExit(
            "STOP: the phase-1q snapshot no longer hashes to the value its establishment record "
            "froze, so the record of what the phase-1q pass found is not the one that was "
            "established (#19). Nothing may be applied over it.")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="re-derive the classification and the artifact; fail on any drift")
    args = ap.parse_args()

    frozen_record_intact()

    raw = open(BACKBONE, encoding="utf-8").read()
    backbone = json.loads(raw)

    # Establishment (#19). This tool REWRITES the whole backbone file, so its serialization must
    # be a fixed point of the committed file's own formatting — otherwise the first run would
    # bury the real change in a whole-file reformat and no reviewer could read the diff.
    roundtrip = json.dumps(json.loads(raw), indent=2, ensure_ascii=False) + "\n"
    if roundtrip != raw:
        print("REFUSED: re-serializing the untouched backbone is not byte-identical to the "
              "committed file, so writing would reformat it.")
        return 2

    # A second establishment step, and it is the one that matters here: every delegation the
    # authored block relies on must still be locatable in its surface. `locate()` stops on a
    # moved or reworded anchor rather than emitting a stale citation.
    seen = mentions()
    for doc, (form, _s, _a, _w) in FORMS.items():
        if form == NOT_NAMED and seen.get(doc):
            raise SystemExit(f"FORMS says {doc} is named nowhere, but it is: {seen[doc]}")
        if form != NOT_NAMED and not seen.get(doc):
            raise SystemExit(f"FORMS grades a delegation for {doc}, which is named nowhere")

    rows, changed = classify(backbone)
    artifact = build_artifact(backbone, rows)

    bb_text = json.dumps(backbone, indent=2, ensure_ascii=False) + "\n"
    art_text = json.dumps(artifact, indent=2, ensure_ascii=False) + "\n"

    t = artifact["totals"]
    print(f"population: {artifact['population']['entries']} entries / "
          f"{artifact['population']['documents']} documents")
    print(f"  before: {t['class_before']}")
    print(f"  after:  {t['class_after']}")
    print(f"  moved:  {t['entries_moved']}  (to gap {t['moved_to_gap']}, "
          f"to contract-home {t['moved_to_contract_home']})")
    for doc, rec in sorted(artifact["by_document"].items()):
        if rec["moves_out"] or rec["moves_in"]:
            print(f"    {doc}: −{rec['moves_out']} / +{rec['moves_in']}")
    p1r = artifact["the_phase_1r_re_run"]
    print(f"  since phase 1q (the written delegations alone): "
          f"{p1r['entries_moved_since_phase1q']} moved "
          f"(to contract-home {len(p1r['moved_to_contract_home'])}, "
          f"to gap {len(p1r['moved_to_gap'])})")
    for doc, rec in sorted(artifact["by_document"].items()):
        o, i = rec.get("moves_out_since_phase1q", 0), rec.get("moves_in_since_phase1q", 0)
        if o or i:
            print(f"    {doc}: −{o} / +{i}")
    if p1r["write_list_documents_that_did_not_move_in_whole"]:
        print("  write-list documents still holding a `gap` entry: "
              + ", ".join(p1r["write_list_documents_that_did_not_move_in_whole"]))
    p0808 = artifact["the_2026_08_08_apply"]
    print(f"  since phase 1r (the 2026-08-08 apply): "
          f"{p0808['entries_moved_since_phase1r']} moved "
          f"(to contract-home {len(p0808['moved_to_contract_home'])}, "
          f"to gap {len(p0808['moved_to_gap'])})")

    if args.check:
        bad = 0
        if bb_text != raw:
            print(f"STALE vs the files: {len(changed)} classification field(s) do not re-derive")
            for c in changed[:40]:
                print("   " + json.dumps(c, ensure_ascii=False))
            bad = 1
        have = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
        if have != art_text:
            print("STALE vs the files: home_classification.json does not re-derive")
            bad = 1
        if bad:
            return 1
        print("the home classification and its artifact re-derive from the files")
        return 0

    open(BACKBONE, "w", encoding="utf-8", newline="").write(bb_text)
    open(OUT, "w", encoding="utf-8", newline="").write(art_text)
    print(f"wrote {os.path.relpath(BACKBONE, ROOT)}: {len(changed)} field change(s)")
    print(f"wrote {os.path.relpath(OUT, ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
