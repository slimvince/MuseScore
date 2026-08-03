#!/usr/bin/env python3
"""Bring the staged register entries to SECTION-level homes, and check they stay correct.

WHAT THIS IS.  The user ruled on 2026-08-03 (phase 1n) that the contract-home criterion's
unit is a **SECTION of a document**, not the document:

    A home is a SECTION of a document.  It is admitted when a user-ratified surface
    delegates a stated concern to that section by name, and that section states rules
    rather than recording findings.

That subsumes the two earlier tests rather than replacing them.  The phase-1l criterion
tested the DELEGATION'S SPECIFICITY and the phase-1m criterion tested the DOCUMENT'S KIND;
both were proxies for this, and the census case is where the proxy fails —
`ARCHITECTURE.md`:319 delegates the licence-pool constraint to `cowork_score_census.md`
**§8c**, a rule-stating block inside a findings-kind document, which the kind test excluded
along with the document around it.

WHY A TOOL RATHER THAN 46 HAND EDITS.  Principle #17(f): no hand-transcribed figures, and —
as of the same day's ruling — no hand-transcribed premises either.  Which section an entry's
home falls in is DERIVABLE from the home document's own headings and the entry's own cited
line, so it is derived here and written into the backbone, never typed.  `--check` re-derives
everything and fails on any drift, so a heading moving inside a home document cannot leave a
stale section behind it.

WHAT IS AUTHORED AND WHAT IS DERIVED.
  authored : the `section_home_criterion` block inside `backbone_decisions.json` — per staged
             document, whether clauses (a)+(b) pass (a user-ratified surface delegates to it
             by name for a stated concern), which SECTIONS the delegations name, and whether
             each named section states rules.  Each judgment carries the citation it was made
             from.  Nothing else is authored.
  derived  : every entry's enclosing section (nearest preceding heading), its label, the
             criterion's verdict per entry, and — for the one document whose clauses (a)+(b)
             the record settles — the resulting `nonspec_kind`.

SCOPE — THE STAGED APPLICATION.  The ruling is applied **only where section granularity
decides something**: the ambiguous population of the phase-1m kind test, and the
`cowork_score_census.md` entries.  Everything else keeps its document-level home and migrates
as its document is next touched.  The register's own scope note says so, so a reader knows the
home field is mixed granularity and why.

Run:
    python tools/audit/decisions/gen_section_homes.py            # derive and write
    python tools/audit/decisions/gen_section_homes.py --check    # re-derive and diff
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
BACKBONE = os.path.join(HERE, "backbone_decisions.json")

HEADING = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")


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


def stage(backbone: dict) -> tuple[list[dict], list[str]]:
    crit = backbone["section_home_criterion"]
    docs = crit["documents"]
    notes: list[str] = []
    changed: list[dict] = []

    heading_cache: dict[str, list[tuple[int, int, str]]] = {}

    for d in backbone["decisions"]:
        doc = d["home"].split(":")[0].replace("\\", "/")
        if doc not in docs:
            if "home_section" in d:
                del d["home_section"]
                changed.append({"id": d["id"], "what": "home_section REMOVED (document unstaged)"})
            continue

        spec = docs[doc]
        if doc not in heading_cache:
            heading_cache[doc] = headings_of(doc)
        line = cited_line(d["home"])
        if line is None:
            raise SystemExit(f"{d['id']}: home {d['home']!r} carries no line anchor; "
                             "a section home cannot be derived from a bare file name")
        enc = enclosing(heading_cache[doc], line)
        if enc is None:
            raise SystemExit(f"{d['id']}: home line {line} in {doc} precedes every heading")
        hline, hlevel, htext = enc

        delegated = None
        for sec in spec["delegated_sections"]:
            if sec["heading_line"] == hline:
                delegated = sec
                break

        # The criterion's verdict for this entry.  Both halves must hold, so either failing is
        # decisive; where clause (a)+(b) is unsettled for the document, nothing is decided and
        # the entry keeps whatever class it carries.
        if spec["clause_ab"] == "pass":
            if delegated is None:
                verdict = "EXCLUDE"          # no delegation reaches this section
            elif delegated["states_rules"]:
                verdict = "ADMIT"
            else:
                verdict = "EXCLUDE"          # delegated, but the section records findings
        else:
            verdict = "UNDECIDED"

        former = d.get("nonspec_kind")
        hs = {
            "heading_line": hline,
            "section": ("#" * hlevel) + " " + htext,
            "label": label_for(hlevel, htext),
            "delegated": delegated is not None,
            "delegation": (delegated["delegation"] if delegated else
                           "no delegation from a user-ratified surface names this section"),
            "verdict": verdict,
            "former_class": (d["home_section"]["former_class"]
                             if "home_section" in d and "former_class" in d["home_section"]
                             else former),
        }
        if d.get("home_section") != hs:
            changed.append({"id": d["id"], "what": "home_section", "to": hs["label"]})
        d["home_section"] = hs

        # `nonspec_kind` is written ONLY where the record settles clauses (a)+(b), which the
        # ruling's staged scope limits to one document.  Everywhere else the class is left
        # exactly as it was and the verdict is reported, not applied.
        if verdict in ("ADMIT", "EXCLUDE"):
            want = "contract-home" if verdict == "ADMIT" else "gap"
            if d.get("nonspec_kind") != want:
                changed.append({"id": d["id"], "what": "nonspec_kind",
                                "from": d.get("nonspec_kind"), "to": want})
                d["nonspec_kind"] = want

    for doc, spec in docs.items():
        hs = headings_of(doc)
        by_line = {h[0]: h for h in hs}
        for sec in spec["delegated_sections"]:
            h = by_line.get(sec["heading_line"])
            if h is None:
                raise SystemExit(f"{doc}: no heading at line {sec['heading_line']} "
                                 f"(the delegation {sec['delegation']} points at it)")
            if h[2] != sec["heading_text"]:
                raise SystemExit(f"{doc}:{sec['heading_line']}: heading is {h[2]!r}, "
                                 f"the criterion block records {sec['heading_text']!r}")
        notes.append(f"{doc}: clause (a)+(b) {spec['clause_ab']}, "
                     f"{len(spec['delegated_sections'])} delegated section(s)")
    return changed, notes


def summarise(backbone: dict) -> dict:
    rows = [d for d in backbone["decisions"] if "home_section" in d]
    per_doc: dict[str, dict] = {}
    for d in rows:
        doc = d["home"].split(":")[0].replace("\\", "/")
        rec = per_doc.setdefault(doc, {"entries": 0, "verdicts": {}, "sections": {}})
        rec["entries"] += 1
        v = d["home_section"]["verdict"]
        rec["verdicts"][v] = rec["verdicts"].get(v, 0) + 1
        lab = d["home_section"]["label"]
        rec["sections"][lab] = rec["sections"].get(lab, 0) + 1
    return {"staged_entries": len(rows), "staged_documents": len(per_doc), "by_document": per_doc}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="re-derive every staged section home and fail on any drift")
    args = ap.parse_args()

    raw = open(BACKBONE, encoding="utf-8").read()
    backbone = json.loads(raw)

    # Establishment (#19).  This tool REWRITES the whole backbone file, so its serialization
    # must be a fixed point of the committed file's own formatting — otherwise the first run
    # would bury the real change in a whole-file reformat and no reviewer could read the diff.
    # Re-serialize the untouched parse and require it byte-identical before touching anything.
    roundtrip = json.dumps(json.loads(raw), indent=2, ensure_ascii=False) + "\n"
    if roundtrip != raw:
        print("REFUSED: re-serializing the untouched backbone is not byte-identical to the "
              "committed file, so writing would reformat it. Fix the serialization here "
              "before running.")
        return 2

    changed, notes = stage(backbone)
    text = json.dumps(backbone, indent=2, ensure_ascii=False) + "\n"

    for n in notes:
        print("  " + n)
    s = summarise(backbone)
    print(f"staged: {s['staged_entries']} entries across {s['staged_documents']} documents")
    for doc, rec in sorted(s["by_document"].items()):
        v = ", ".join(f"{k} {n}" for k, n in sorted(rec["verdicts"].items()))
        print(f"  {doc}: {rec['entries']} entries — {v}")
        for lab, n in sorted(rec["sections"].items()):
            print(f"      {lab}: {n}")

    if args.check:
        if text != raw:
            print(f"STALE vs the files: {len(changed)} staged field(s) do not re-derive")
            for c in changed[:40]:
                print("   " + json.dumps(c, ensure_ascii=False))
            return 1
        print("every staged section home re-derives from its own document")
        return 0

    open(BACKBONE, "w", encoding="utf-8", newline="").write(text)
    print(f"wrote {os.path.relpath(BACKBONE, ROOT)}: {len(changed)} field change(s)")
    for c in changed:
        print("   " + json.dumps(c, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
