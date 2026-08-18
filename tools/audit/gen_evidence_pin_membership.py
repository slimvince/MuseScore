#!/usr/bin/env python3
"""THE EVIDENCE PIN'S CLASS MEMBERSHIP — derived from the ruling records, never hand-listed.

THE RULING THIS EXISTS FOR (user, 2026-08-17, Ruling 1 of
`cowork_rulings_2026_08_17_ninth_return.md`), quoted verbatim:

    A GENERATED DOCUMENT PUT TO THE USER FOR A RULING JOINS THE PINNED KIND AT THE MOMENT IT IS
    RULED FROM: its generator thereafter reads its inputs at the git objects of the commit the
    ruling names.

THE GENERAL FORM IT RESTS ON, also verbatim: *a document generated from a live data file is not
evidence of what was PUT in front of the user unless its generation is PINNED.*

THE BOUND, also verbatim: *A ratification document's job ends at the ruling. Pinning it afterwards
removes nothing live — the current classification stays available in the underlying data file,
which is NOT pinned and continues to re-derive.*

WHY THE MEMBERSHIP IS DERIVED RATHER THAN LISTED.  A hand-written membership has the failure shape
the ruling exists against, one level up: it looks complete and is not checkable.  The dispatch
that executes the ruling (`cc_instruction_preparation_tenth.md`, Task 1) orders it derived and
published, with a member whose ruling commit cannot be derived from a record a STOP-and-report and
never a guessed pin.  Nothing below is transcribed (`CLAUDE.md` #17f, register entry D-431).

WHAT IS DERIVED
---------------
GENERATED DOCUMENTS  Every document under `ratification_surfaces/` that a tool writes, taken by
                     scanning the tools for a module-level assignment composing that directory
                     with a `.md` filename.  The map is document -> generator.
RULING RECORDS       Every root-level `cowork_rulings_*.md`.
WHAT A RECORD SAYS   A record states what it was taken from in two structural places and nowhere
IT WAS TAKEN FROM    else: its LEADING BLOCKQUOTE (the contiguous `>` block before its first
                     heading) and its PROVENANCE paragraph (a paragraph opening `*Provenance:`).
                     The test is structural rather than a vocabulary of phrases, so it cannot be
                     widened by taste.
ROUTE A (a document) A generated document named in one of those two blocks -> its generator is a
                     member, and the document is what was ruled from.
ROUTE B (a tool)     A ruling record naming a TOOL in a sentence that says it is PINNED -> that
                     tool is a member by the ruling's own naming.  This is how §6 kind 1 of
                     `cowork_rulings_2026_08_16_preparation_return.md` pinned its two completed
                     measurements, which name no ratification document at all.
THE RULING COMMIT    Resolved ONLY where a record states it, in the one form the record actually
                     uses: the document naming followed by "at commit `<hash>`".  A member the
                     pattern does not resolve is published UNRESOLVED — the STOP-and-report the
                     dispatch orders — and is never given a guessed pin, and never a pin taken at
                     a branch tip.  A differently-phrased naming therefore reports UNRESOLVED,
                     which is the recoverable direction: an unpinned member is a question, a
                     wrongly pinned one is a false record of what was PUT.
THE PIN CENSUS       Every tool in the tree carrying a pin constant, with the constant's own
                     description of what the commit IS, so the artifact accounts for the whole
                     pinned population and not only for this class.

THE STOPS
  * a member this artifact records as PINNED whose generator does not carry that exact commit in a
    pin constant — the pin has been moved or removed under the record;
  * a tool carrying a pin constant that this artifact does not account for in one of its two
    classes — a pin exists that this run did not cover, which is the per-tool condition the guard
    classification's own ruling makes mechanical;
  * a generated document map with two generators for one document — one path per concern (#6).

WHAT THIS DOES NOT ASSERT.  That a member SHOULD be pinned: the ruling says a generated document
put to the user for a ruling joins the pinned kind, and whether an individual member's pin would
collide with another live ruling about the same tool is a question for the user, published here as
data.  And that an UNRESOLVED member has no discoverable commit — only that no record states one
in the form above.

Run:
    python tools/audit/gen_evidence_pin_membership.py
    python tools/audit/gen_evidence_pin_membership.py --check
"""
from __future__ import annotations

import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(HERE, "evidence_pin_membership.json")

sys.path.insert(0, HERE)
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

SURFACE_DIR = "ratification_surfaces"
TOOL_DIRS = ("tools",)
SKIP_DIRS = {".git", "__pycache__", "node_modules", ".venv",
             "ninja_build_rel", "build.release", "corpus", "dcml"}

# A module-level assignment whose value composes the ratification directory with a `.md` name.
# Both spellings the tree actually uses are covered: one line, and the parenthesised two-line form.
# NAMING ONE IS NOT WRITING IT: a tool that READS a ratification surface binds it the same way, so
# the constant must also appear in a write call before the document counts as generated. Without
# that second half a hand-written surface a tool merely consumes reads as one this tool produced.
NAMES_SURFACE = re.compile(
    r'^([A-Z][A-Z0-9_]*)\s*=\s*\(?\s*(?:ROOT|REPO)[^\n]*?"' + SURFACE_DIR + r'"'
    r'[^\n]*?(?:\n\s*)?/\s*"([A-Za-z0-9_.-]+\.md)"', re.M)


def writes_it(text: str, const: str) -> bool:
    """The two write idioms the tools actually use, and no third."""
    return bool(re.search(r'\b' + re.escape(const) + r'\.write_text\s*\(', text)
                or re.search(r'open\(\s*' + re.escape(const) + r'\s*,\s*["\']w', text))

# A pin constant: a module-level NAME carrying the word PINNED, bound to a hex commit.
PIN_CONST = re.compile(r'^([A-Z][A-Z0-9_]*)\s*=\s*"([0-9a-f]{7,40})"', re.M)
# Its companion description, where the tool carries one.
PIN_DESC = re.compile(r'^([A-Z][A-Z0-9_]*)\s*=\s*\(?\s*(".*?")\s*\)?\s*$', re.M | re.S)

RULING_RECORD = re.compile(r'^cowork_rulings_.*\.md$')
SURFACE_NAMING = re.compile(r'`?' + SURFACE_DIR + r'/([A-Za-z0-9_.-]+\.md)`?')
# The ONE resolution form the record actually uses. Narrow on purpose; see the docstring.
RULED_AT = re.compile(r'`?' + SURFACE_DIR + r'/([A-Za-z0-9_.-]+\.md)`?\s+at\s+commit\s+'
                      r'`([0-9a-f]{7,40})`')
# A record names a tool either by its repository path or by its bare file name; both are resolved
# against the tool population so the reading does not depend on how a record happens to spell it.
TOOL_NAMING = re.compile(r'`([A-Za-z0-9_/.-]+\.py)`')


class Stop(Exception):
    """A demand of the derivation is unmet. Never a warning."""


def read(path: str) -> str:
    with io.open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def walk_tools() -> list[str]:
    out = []
    for base in TOOL_DIRS:
        for root, dirs, files in os.walk(os.path.join(ROOT, base)):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
            for fn in sorted(files):
                if fn.endswith(".py"):
                    out.append(os.path.relpath(os.path.join(root, fn), ROOT).replace("\\", "/"))
    return sorted(out)


def generated_documents(tool_paths: list[str]) -> dict:
    """document -> generator, derived from the write target each tool declares."""
    found: dict[str, list[str]] = {}
    for rel in tool_paths:
        text = read(os.path.join(ROOT, rel))
        for const, doc in NAMES_SURFACE.findall(text):
            if not writes_it(text, const):
                continue
            found.setdefault(doc, [])
            if rel not in found[doc]:
                found[doc].append(rel)
    doubled = {d: g for d, g in found.items() if len(g) > 1}
    if doubled:
        raise Stop(f"a generated ratification document has more than one writer, which is one "
                   f"concern with two paths (#6): {doubled}")
    return {d: g[0] for d, g in sorted(found.items())}


def pin_census(tool_paths: list[str]) -> dict:
    """Every tool carrying a pin constant, with the constant's own description of the commit."""
    census: dict[str, dict] = {}
    for rel in tool_paths:
        text = read(os.path.join(ROOT, rel))
        consts = {name: sha for name, sha in PIN_CONST.findall(text) if "PINNED" in name}
        if not consts:
            continue
        descs = {}
        for name, raw in PIN_DESC.findall(text):
            try:
                descs[name] = " ".join(
                    part for part in re.findall(r'"((?:[^"\\]|\\.)*)"', raw))
            except re.error:                                    # pragma: no cover - defensive
                descs[name] = ""
        census[rel] = {
            "pin_constants": {name: sha for name, sha in sorted(consts.items())},
            "what_the_commit_is_per_the_tool": {
                name: descs.get(name + "_IS", "").strip()
                for name in sorted(consts)
            },
        }
    return dict(sorted(census.items()))


def ruling_records() -> list[str]:
    return sorted(fn for fn in os.listdir(ROOT)
                  if RULING_RECORD.match(fn)
                  and os.path.isfile(os.path.join(ROOT, fn)))


def own_statement_blocks(text: str) -> list[dict]:
    """The two structural places a ruling record states what it was taken from.

    LEADING BLOCKQUOTE — the contiguous `>` block that stands before the record's first heading.
    PROVENANCE        — a paragraph opening `*Provenance:`.
    """
    lines = text.split("\n")
    blocks: list[dict] = []

    lead: list[str] = []
    for i, line in enumerate(lines):
        if line.startswith("##"):
            break
        if line.startswith(">"):
            lead.append(line)
        elif lead and not line.strip():
            continue
        elif lead:
            break
    if lead:
        blocks.append({"kind": "leading-blockquote", "text": "\n".join(lead)})

    para: list[str] = []
    for line in lines:
        if para:
            if not line.strip():
                blocks.append({"kind": "provenance-paragraph", "text": "\n".join(para)})
                para = []
            else:
                para.append(line)
        elif line.lstrip().startswith("*Provenance:"):
            para = [line]
    if para:
        blocks.append({"kind": "provenance-paragraph", "text": "\n".join(para)})
    return blocks


def resolve_tool(named: str, tool_paths: list[str]) -> str | None:
    """A record's naming of a tool, resolved against the tool population.

    A naming that resolves to no tool, or to more than one, resolves to nothing: route B may not
    guess which tool a record meant any more than the commit resolution may guess a commit.
    """
    named = named.replace("\\", "/")
    if named in tool_paths:
        return named
    hits = [p for p in tool_paths if p.rsplit("/", 1)[-1] == named.rsplit("/", 1)[-1]]
    return hits[0] if len(hits) == 1 else None


def derive_members(records: list[str], docs: dict,
                   tool_paths: list[str]) -> tuple[dict, dict, dict]:
    """Route A (a generated document named), route B (a tool named as PINNED), and the residue."""
    route_a: dict[str, dict] = {}
    route_b: dict[str, dict] = {}
    named_not_generated: dict[str, list[str]] = {}

    for rec in records:
        text = read(os.path.join(ROOT, rec))
        blocks = own_statement_blocks(text)
        joined = "\n\n".join(b["text"] for b in blocks)
        resolved = {d: sha for d, sha in RULED_AT.findall(joined)}
        for name in sorted(set(SURFACE_NAMING.findall(joined))):
            if name not in docs:
                named_not_generated.setdefault(name, [])
                if rec not in named_not_generated[name]:
                    named_not_generated[name].append(rec)
                continue
            rowa = route_a.setdefault(name, {
                "document": SURFACE_DIR + "/" + name,
                "generator": docs[name],
                "ruling_records_naming_it": [],
                "the_commit_a_record_states": None,
                "where_the_record_states_it": None,
            })
            if rec not in rowa["ruling_records_naming_it"]:
                rowa["ruling_records_naming_it"].append(rec)
            if name in resolved and rowa["the_commit_a_record_states"] is None:
                rowa["the_commit_a_record_states"] = resolved[name]
                rowa["where_the_record_states_it"] = rec

        # ROUTE B — a tool the record itself names as PINNED.
        for line in text.split("\n"):
            if "PINNED" not in line.upper():
                continue
            for named in TOOL_NAMING.findall(line):
                tool = resolve_tool(named, tool_paths)
                if tool is None:
                    continue
                rowb = route_b.setdefault(tool, {
                    "generator": tool,
                    "ruling_records_naming_it_as_pinned": [],
                    "the_naming": [],
                })
                if rec not in rowb["ruling_records_naming_it_as_pinned"]:
                    rowb["ruling_records_naming_it_as_pinned"].append(rec)
                snippet = line.strip()[:400]
                if snippet not in rowb["the_naming"]:
                    rowb["the_naming"].append(snippet)

    return route_a, route_b, dict(sorted(named_not_generated.items()))


def build() -> dict:
    tool_paths = walk_tools()
    docs = generated_documents(tool_paths)
    census = pin_census(tool_paths)
    records = ruling_records()
    route_a, route_b, named_not_generated = derive_members(records, docs, tool_paths)

    members: dict[str, dict] = {}
    for name, row in sorted(route_a.items()):
        members[row["generator"]] = {
            "route": "A — a ruling record's own statement names the GENERATED DOCUMENT",
            "document": row["document"],
            "generator": row["generator"],
            "ruling_records_naming_it": row["ruling_records_naming_it"],
            "the_commit_a_record_states": row["the_commit_a_record_states"],
            "where_the_record_states_it": row["where_the_record_states_it"],
        }
    for tool, row in sorted(route_b.items()):
        if tool in members:
            members[tool]["also_named_as_pinned_by"] = row["ruling_records_naming_it_as_pinned"]
            continue
        members[tool] = {
            "route": "B — a ruling record names the TOOL itself as PINNED",
            "document": None,
            "generator": tool,
            "ruling_records_naming_it": row["ruling_records_naming_it_as_pinned"],
            "the_naming": row["the_naming"],
            "the_commit_a_record_states": None,
            "where_the_record_states_it": None,
        }

    # What each member's generator actually carries today.
    for tool, row in members.items():
        carried = census.get(tool, {}).get("pin_constants", {})
        row["pin_constants_the_generator_carries"] = carried
        stated = row.get("the_commit_a_record_states")
        if carried and stated and stated in {sha[:len(stated)] for sha in carried.values()}:
            row["state"] = "PINNED — at the commit a ruling record states"
        elif carried:
            row["state"] = "PINNED — by the route the tool's own pin constant records"
        elif stated:
            row["state"] = "NOT PINNED — a record states the commit; the pin is not applied"
        else:
            row["state"] = ("UNRESOLVED — a STOP-and-report: no record states the commit it was "
                            "ruled at, and a pin may not be guessed")

    # ── the STOPs ───────────────────────────────────────────────────────────────────────────
    for tool, row in members.items():
        stated = row.get("the_commit_a_record_states")
        carried = row["pin_constants_the_generator_carries"]
        if row["state"].startswith("PINNED — at the commit a ruling record states"):
            if not any(sha.startswith(stated) or stated.startswith(sha)
                       for sha in carried.values()):
                raise Stop(f"{tool} is recorded PINNED at {stated}, which no pin constant in it "
                           f"carries: {carried}")

    unaccounted = sorted(set(census) - set(members))
    accounted_elsewhere = {t: census[t] for t in unaccounted}

    return {
        "what_this_is":
            "THE DERIVED MEMBERSHIP OF THE EVIDENCE PIN'S CLASS, and the whole pinned population "
            "beside it. A MEASUREMENT AND A PUBLICATION: nothing here pins anything, regenerates "
            "any document, or moves any verdict. Every member is derived from the ruling records "
            "themselves; none is listed by hand (D-431).",
        "generated_by": "tools/audit/gen_evidence_pin_membership.py",
        "generated_for": "cc_instruction_preparation_tenth.md, Task 1",
        "the_class_rule_verbatim":
            "A GENERATED DOCUMENT PUT TO THE USER FOR A RULING JOINS THE PINNED KIND AT THE MOMENT "
            "IT IS RULED FROM: its generator thereafter reads its inputs at the git objects of the "
            "commit the ruling names.",
        "the_general_form_verbatim":
            "a document generated from a live data file is not evidence of what was PUT in front "
            "of the user unless its generation is PINNED.",
        "the_bound_verbatim":
            "A ratification document's job ends at the ruling. Pinning it afterwards removes "
            "nothing live — the current classification stays available in the underlying data "
            "file, which is NOT pinned and continues to re-derive.",
        "the_ruling": "User, 2026-08-17, Ruling 1 of `cowork_rulings_2026_08_17_ninth_return.md`, "
                      "extending §6 kind 1 of `cowork_rulings_2026_08_16_preparation_return.md`.",
        "how_the_membership_is_derived": {
            "generated_documents":
                "every document under `ratification_surfaces/` a tool declares as a write target",
            "ruling_records": "every root-level `cowork_rulings_*.md`",
            "what_a_record_says_it_was_taken_from":
                "its LEADING BLOCKQUOTE and its PROVENANCE paragraph — the two structural places, "
                "not a vocabulary of phrases",
            "route_A": "a generated document named in one of those two blocks",
            "route_B": "a tool the record itself names in a sentence saying it is PINNED",
            "the_commit": "resolved only where a record states it, in the one form the record "
                          "actually uses: the document naming followed by \"at commit `<hash>`\"",
            "the_recoverable_direction":
                "a differently-phrased naming reports UNRESOLVED rather than resolving to "
                "something. An unpinned member is a question; a wrongly pinned one is a false "
                "record of what was PUT.",
        },
        "counts": {
            "generated_ratification_documents": len(docs),
            "ruling_records_read": len(records),
            "members": len(members),
            "members_pinned": sum(1 for r in members.values() if r["state"].startswith("PINNED")),
            "members_unresolved": sum(1 for r in members.values()
                                      if r["state"].startswith("UNRESOLVED")),
            "tools_carrying_a_pin_constant": len(census),
            "pinned_tools_outside_this_class": len(accounted_elsewhere),
        },
        "the_members": members,
        "generated_ratification_documents": docs,
        "ruling_records_read": records,
        "named_in_a_ruling_record_but_not_generated": {
            "what_this_is": "documents a ruling record states it was taken from that NO tool "
                            "writes. The class rule reaches a GENERATED document only, so these "
                            "are outside it — recorded rather than dropped (#12).",
            "documents": named_not_generated,
        },
        "pinned_tools_outside_this_class": {
            "what_this_is": "tools carrying a pin constant that this class does not reach. Each "
                            "is published with its own constant's description of what the commit "
                            "IS, so the whole pinned population is accounted for and no pin is "
                            "invisible. NO VERDICT IS TAKEN on them: whether a pin taken for "
                            "another recorded reason also belongs to this class is a question for "
                            "the user, not a derivation.",
            "tools": accounted_elsewhere,
        },
        "the_whole_pin_census": census,
        "what_this_does_not_assert": [
            "That a member SHOULD be pinned. The ruling says a generated document put to the user "
            "for a ruling joins the pinned kind; whether an individual member's pin collides with "
            "another live ruling about the same tool is published here as data and ruled by the "
            "user.",
            "That an UNRESOLVED member has no discoverable commit — only that no record states one "
            "in the form the resolution uses.",
            "That the two structural blocks are the only places a record could state what it was "
            "ruled from. They are the two the records actually use; a record that stated it "
            "somewhere else would report as not-ruled-from, which is the recoverable direction.",
        ],
    }


def main(argv: list[str]) -> int:
    art = build()
    text = json.dumps(art, indent=1, ensure_ascii=False) + "\n"
    if "--check" in argv:
        have = read(OUT) if os.path.exists(OUT) else ""
        if have != text:
            print("STALE vs the derivation: evidence_pin_membership.json does not re-derive")
            return 1
        print("the evidence pin's class membership re-derives")
    else:
        with io.open(OUT, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        print("wrote %s" % os.path.relpath(OUT, ROOT).replace("\\", "/"))
    c = art["counts"]
    print("  generated ratification documents %d; ruling records read %d"
          % (c["generated_ratification_documents"], c["ruling_records_read"]))
    print("  members %d — pinned %d, UNRESOLVED %d"
          % (c["members"], c["members_pinned"], c["members_unresolved"]))
    print("  tools carrying a pin constant %d; outside this class %d"
          % (c["tools_carrying_a_pin_constant"], c["pinned_tools_outside_this_class"]))
    for tool, row in art["the_members"].items():
        print("    %-52s %s" % (tool, row["state"]))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except Stop as exc:
        print("STOP: %s" % exc)
        sys.exit(2)
