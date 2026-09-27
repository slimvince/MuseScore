#!/usr/bin/env python3
"""DERIVE AND MEASURE THE OUTGOING POPULATION FOR THE L2 COMPARISON — NOTHING TABULATED.

WHY THIS EXISTS.  The user's ruling of 2026-09-27, Option B
(`records/cowork/rulings/cowork_rulings_2026_09_27_l2_outgoing_population_sitting.md` §2), fixes
which existing texts the blind L2 derivation is compared against -- the L2 comparison's OUTGOING
POPULATION -- in four items.  Three of the four are defined by something that has to be RUN
(a pattern over four sections, a term search, a read of the register's data file), and the same
§2 records that the size of the term search's yield is UNMEASURED and is to be measured before
anything is tabulated.  This tool is that derivation and that measurement, and nothing else.

WHAT IT DOES, AND NOTHING ELSE.  Every numbered item is a key of the artifact.

  1. `item_1_the_named_sections` -- LOCATES the four `ARCHITECTURE.md` sections the ruling names,
     BY HEADING TEXT, never by line number (D-307), with the L0/L1 tool's own `locate_section`.
     A heading not found is a STOP (raised inside the imported function).

  2. `item_2_the_documents_the_sections_name` -- every match of `[A-Za-z0-9_./-]+\\.md\\b` inside
     the four spans, MECHANICALLY and with no grading of form.  A name that does not resolve at the
     path as written is RECORDED, never guessed at another path and never dropped (#12).

  3. `item_3_the_term_search` -- the forty-two terms of Ruling 86, READ FROM THEIR ONE HOME
     (`gen_derivation_boot_pack.L2_KEYWORDS`, never retyped), searched with the L0/L1 tool's own
     `search_terms` over every file of its `SEARCH_CLASSES` as its `load_classes()` reads them.
     Hit files IN the ruled specification document set are the population; every other hit file
     is the RESIDUE, published whole under Ruling 33's shape.  Nothing is dropped.

  4. `item_4_the_decision_passages` -- the 111 decisions ruled L2's own (the confirmed set at
     `tools/audit/l2_withheld_documents.json` -> `in_entries`), each read at its home in the
     register's data file through `gen_l2_withheld_documents.read_backbone()`, the home's lines
     quoted verbatim, and where each passage falls relative to items 1-3.  GENERATED, NEVER TYPED
     (D-431).

  5. `the_l0_l1_transfer_input` and `the_measured_size` -- the transfer list's span in the L0/L1
     reading file, located by heading text and NOT parsed; and one block of computed sizes a reader
     can read without the rest.  Every figure is computed; none is authored.

ONE PATH PER CONCERN (#6; D-623 -- a capability is a parameter, never a sibling copy).  The
section locator, the class reader, the specification-set reader, the term matcher and the text
reader are IMPORTED from `gen_l0_l1_outgoing_population`; the forty-two terms from
`gen_derivation_boot_pack`; the backbone reader and the identity order from
`gen_l2_withheld_documents`.  None of them is copied, and none of those tools is edited.

THE STOPS, each ending the run with `STOP: <reason>` and exit 2 -- never a traceback, whichever of
the three `Stop` classes raised it (this tool's own, the L0/L1 tool's, the withheld-document
tool's):
  - the term list is not forty-two long;
  - a heading of item 1 or of the transfer span is not found; a searched or home document cannot
    be read;
  - the confirmed identity list is not 111 long; an identity is absent from the backbone; a home is
    of any shape other than `<doc>.md:<a>` or `<doc>.md:<a>-<b>`; a span is past its file's end or
    runs backwards;
  - grouping the 111 by the document part of their homes disagrees, in either direction, with the
    confirmed artifact's `documents`.

WHAT IT DOES NOT DO.  It takes no disposition, orders no tabulation, grades nothing, compares
nothing, and edits no outgoing text.  It does not open the blind derivation, its brief, or the
boot pack's directory.  THE TABULATION'S UNIT, ORDER AND BATCHING ARE THE NEXT DISPATCH'S.

Run:
    python tools/audit/gen_l2_outgoing_population.py           # write the artifact
    python tools/audit/gen_l2_outgoing_population.py --check   # re-derive, exit 1 on drift
"""
from __future__ import annotations

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(HERE, "l2_outgoing_population.json")
WITHHELD = os.path.join(HERE, "l2_withheld_documents.json")

sys.path.insert(0, HERE)
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

import gen_l0_l1_outgoing_population as l0l1     # noqa: E402  (path set above)
import gen_l2_withheld_documents as withheld     # noqa: E402  (path set above)
from gen_derivation_boot_pack import L2_KEYWORDS  # noqa: E402  (path set above)
from gen_l0_l1_outgoing_population import (      # noqa: E402  (path set above)
    SEARCH_CLASSES,
    load_classes,
    load_specification_document_set,
    locate_section,
    read_text,
    search_terms,
)
from gen_l2_withheld_documents import entry_number, read_backbone  # noqa: E402

RULED_TERM_COUNT = 42
RULED_IDENTITY_COUNT = 111
ARCHITECTURE = "ARCHITECTURE.md"


class Stop(Exception):
    """A count moved, a home cannot be read, or a reconciliation fails. Never a warning."""


# --------------------------------------------------------------------------------------------
# THE RULING, and the four sections its item 1 names -- located by TEXT (D-307).
# --------------------------------------------------------------------------------------------
THE_RULING = {
    "record": "records/cowork/rulings/cowork_rulings_2026_09_27_l2_outgoing_population_sitting.md",
    "section": "§2 — Ruling — Option B",
    "executed_by": "records/cc/instructions/cc_instruction_l2_outgoing_population_2026_09_27.md, Task 1",
}

NAMED_SECTIONS = [
    {"opens_at": "## The joint estimator — the standing rules of the production inference layer",
     "closes_before_pattern": r"^## "},
    {"opens_at": "#### Layer 3 — key/mode is the sequence decoder",
     "closes_before_pattern": r"^#### "},
    {"opens_at": "#### Layer 4 — the per-slice chord-symbol decoder",
     "closes_before_pattern": r"^#### "},
    {"opens_at": "#### Layer 5 — the function/cadence layer",
     "closes_before_pattern": r"^#### "},
]

TRANSFER_SOURCE = "ratification_surfaces/cowork_comparison_l0_l1_reading.md"
TRANSFER_SECTION = {
    "opens_at": "## 10. The TRANSFER LIST — every RELOCATED row, by target charter",
    "closes_before_pattern": r"^## ",
}

MD_NAME = re.compile(r"[A-Za-z0-9_./-]+\.md\b")
HOME_SHAPE = re.compile(r"^(?P<doc>[^\s:]+\.md):(?P<a>\d+)(?:-(?P<b>\d+))?$")
HEADING = re.compile(r"^#{1,6}\s")
FENCE = re.compile(r"^ {0,3}(```|~~~)")

THE_SIX_RULING_86_RECORDS_AS_MATCHING_NOTHING = [
    "change-point", "harmonic rhythm", "evidence ranking", "chord-tone assignment",
    "elaboration relation", "figured bass",
]

THE_RESIDUE_STATEMENT = (
    "hit, outside the specification document set, not dispositioned by this comparison; "
    "reachable by the mining map"
)

SIZE_STOP_STATEMENT = (
    "THIS BATCH TABULATES NOTHING. The size stop is that the batch ends here; the tabulation's "
    "unit, order and batching are written by the next dispatch after the writing side has read "
    "this block."
)


def file_lines(text):
    """The file's lines, without the empty element a final newline leaves after `split`."""
    lines = text.split("\n")
    if lines and lines[-1] == "":
        lines = lines[:-1]
    return lines


def span_range(bounds):
    """1-based first and last line of a span `locate_section` returned."""
    first = bounds["first_line_number_as_a_locator_only"]
    return first, first + bounds["lines_in_the_span"] - 1


def headings_by_line(lines):
    """For each 1-based line: the nearest heading STRICTLY before it, outside fenced code blocks,
    and whether the line itself sits inside a fenced code block or is itself a heading."""
    out = {}
    nearest = None
    in_fence = False
    for index, line in enumerate(lines):
        number = index + 1
        is_fence = bool(FENCE.match(line))
        out[number] = {
            "nearest": nearest,
            "inside_fence": in_fence and not is_fence,
            "is_heading": (not in_fence) and (not is_fence) and bool(HEADING.match(line)),
        }
        if is_fence:
            in_fence = not in_fence
            continue
        if not in_fence and HEADING.match(line):
            nearest = (number, line)
    return out


def norm(path):
    return os.path.normpath(path).replace("\\", "/")


# --------------------------------------------------------------------------------------------
def derive():
    if len(L2_KEYWORDS) != RULED_TERM_COUNT:
        raise Stop("gen_derivation_boot_pack.L2_KEYWORDS carries %d terms; Ruling 86 rules %d"
                   % (len(L2_KEYWORDS), RULED_TERM_COUNT))

    classes = load_classes()                               # l0l1.Stop if unreadable
    spec_members = load_specification_document_set()       # l0l1.Stop if unreadable
    spec_paths = set(spec_members)
    class_of = {}
    classes_of = {}
    for class_name in SEARCH_CLASSES:
        for path in classes[class_name]:
            class_of.setdefault(path, class_name)
            classes_of.setdefault(path, []).append(class_name)

    # ---- ITEM 1 -----------------------------------------------------------------------------
    arch_text = read_text(ARCHITECTURE)
    arch_lines = file_lines(arch_text)
    item1 = []
    for spec in NAMED_SECTIONS:
        bounds = locate_section(arch_text, ARCHITECTURE, spec["opens_at"],
                                spec["closes_before_pattern"])
        item1.append({"path": ARCHITECTURE, "section": bounds})
    spans = [(r["section"]["opens_at"],) + span_range(r["section"]) for r in item1]

    def item1_span_of(line_number):
        inside = [opens for opens, first, last in spans if first <= line_number <= last]
        return inside[0] if len(inside) == 1 else (inside or None)

    # ---- ITEM 2 -----------------------------------------------------------------------------
    occurrences = []
    for opens, first, last in spans:
        for number in range(first, last + 1):
            for match in MD_NAME.finditer(arch_lines[number - 1]):
                name = match.group(0)
                resolved = os.path.isfile(os.path.join(ROOT, name))
                occurrences.append({
                    "name_as_written": name,
                    "section": opens,
                    "line_number_as_a_locator_only": number,
                    "resolves_at_the_path_as_written": resolved,
                    "in_the_specification_document_set": name in spec_paths,
                    "inventory_class": class_of.get(name),
                    "bytes": os.path.getsize(os.path.join(ROOT, name)) if resolved else None,
                })
    distinct = {}
    for occ in occurrences:
        rec = distinct.setdefault(occ["name_as_written"], {
            "name_as_written": occ["name_as_written"],
            "resolves_at_the_path_as_written": occ["resolves_at_the_path_as_written"],
            "in_the_specification_document_set": occ["in_the_specification_document_set"],
            "inventory_class": occ["inventory_class"],
            "bytes": occ["bytes"],
            "named_in_sections": [],
            "occurrences": 0,
        })
        rec["occurrences"] += 1
        if occ["section"] not in rec["named_in_sections"]:
            rec["named_in_sections"].append(occ["section"])
    distinct_names = [distinct[k] for k in sorted(distinct)]
    item2_resolved = {norm(d["name_as_written"]) for d in distinct_names
                      if d["resolves_at_the_path_as_written"]}

    # ---- ITEM 3 -----------------------------------------------------------------------------
    hits_per_term = {term: 0 for term in L2_KEYWORDS}
    per_class_counts = {}
    population = {}
    residue = {}
    absent = []
    searched = []
    for class_name in SEARCH_CLASSES:
        with_hit = 0
        for rel_path in classes[class_name]:
            abs_path = os.path.join(ROOT, rel_path)
            if not os.path.isfile(abs_path):
                absent.append({"path": rel_path, "inventory_class": class_name,
                               "absent_from_the_tree": True,
                               "in_the_specification_document_set": rel_path in spec_paths})
                continue
            if rel_path in population or rel_path in residue:
                with_hit += 1
                continue
            if rel_path in searched:
                continue
            searched.append(rel_path)
            text = read_text(rel_path)
            hits = search_terms(text, L2_KEYWORDS, "admitting")
            if not hits:
                continue
            with_hit += 1
            for hit in hits:
                hits_per_term[hit["term"]] += 1
            record = {
                "path": rel_path,
                "inventory_class": class_name,
                "inventory_classes_all": classes_of[rel_path],
                "in_the_specification_document_set": rel_path in spec_paths,
                "hit_lines_distinct": len({h["line_number"] for h in hits}),
                "hits": len(hits),
            }
            if rel_path in spec_paths:
                info = headings_by_line(file_lines(text))
                enriched = []
                for hit in hits:
                    here = info.get(hit["line_number"], {})
                    nearest = here.get("nearest")
                    row = dict(hit)
                    row["nearest_preceding_heading"] = nearest[1] if nearest else None
                    row["nearest_preceding_heading_line_number_as_a_locator_only"] = (
                        nearest[0] if nearest else None)
                    row["the_hit_line_is_itself_a_heading"] = here.get("is_heading", False)
                    row["the_hit_line_is_inside_a_fenced_code_block"] = here.get(
                        "inside_fence", False)
                    if rel_path == ARCHITECTURE:
                        row["inside_item_1_span"] = item1_span_of(hit["line_number"])
                    enriched.append(row)
                per_heading = {}
                for row in enriched:
                    key = (row["nearest_preceding_heading_line_number_as_a_locator_only"] or 0,
                           row["nearest_preceding_heading"])
                    per_heading.setdefault(key, set()).add(row["line_number"])
                record["hit_lines_distinct_per_heading"] = [
                    {"heading": heading, "heading_line_number_as_a_locator_only": number or None,
                     "hit_lines_distinct": len(lines)}
                    for (number, heading), lines in sorted(per_heading.items(),
                                                           key=lambda kv: kv[0][0])
                ]
                if rel_path == ARCHITECTURE:
                    inside = {r["line_number"] for r in enriched if r["inside_item_1_span"]}
                    every = {r["line_number"] for r in enriched}
                    record["hit_lines_distinct_inside_the_four_spans"] = len(inside)
                    record["hit_lines_distinct_outside_the_four_spans"] = len(every - inside)
                record["hit_records"] = enriched
                population[rel_path] = record
            else:
                record["the_statement"] = THE_RESIDUE_STATEMENT
                record["hit_records"] = hits
                residue[rel_path] = record
        per_class_counts[class_name] = {
            "files_in_the_class": len(classes[class_name]),
            "files_with_at_least_one_hit": with_hit,
        }

    hit_lines_by_member = {
        path: {h["line_number"] for h in rec["hit_records"]} for path, rec in population.items()
    }

    # ---- ITEM 4 -----------------------------------------------------------------------------
    with open(WITHHELD, "r", encoding="utf-8") as handle:
        confirmed = json.load(handle)
    identities = confirmed.get("in_entries")
    if not isinstance(identities, list) or len(identities) != RULED_IDENTITY_COUNT:
        raise Stop("l2_withheld_documents.json -> in_entries carries %s identities; the confirmed "
                   "set is %d" % (len(identities) if isinstance(identities, list) else identities,
                                  RULED_IDENTITY_COUNT))
    backbone = read_backbone()
    missing = [i for i in identities if i not in backbone]
    if missing:
        raise Stop("identity/identities absent from the register's data file: %s" % missing)

    parsed = {}
    for identity in identities:
        home = backbone[identity].get("home")
        match = HOME_SHAPE.match(home) if isinstance(home, str) else None
        if not match:
            raise Stop("%s: its home is not of the shape <doc>.md:<a>[-<b>] (home=%r)"
                       % (identity, home))
        parsed[identity] = (home, match.group("doc"), int(match.group("a")),
                            int(match.group("b")) if match.group("b") else None)

    grouped = {}
    for identity, (_, doc, _, _) in parsed.items():
        grouped.setdefault(doc, set()).add(identity)
    confirmed_grouping = {d["document"]: set(d["in_entries_homed_here"])
                          for d in confirmed.get("documents", [])}
    if grouped != confirmed_grouping:
        only_here = sorted(set(grouped) - set(confirmed_grouping))
        only_there = sorted(set(confirmed_grouping) - set(grouped))
        differing = sorted(d for d in set(grouped) & set(confirmed_grouping)
                           if grouped[d] != confirmed_grouping[d])
        raise Stop("grouping the 111 by home document disagrees with l2_withheld_documents.json "
                   "-> documents: documents only in the homes %s; only in the artifact %s; "
                   "differing membership %s" % (only_here, only_there, differing))

    texts = {}
    passages = []
    for identity in sorted(identities, key=entry_number):
        home, doc, a, b = parsed[identity]
        if doc not in texts:
            texts[doc] = file_lines(read_text(doc))
        lines = texts[doc]
        last = b if b is not None else a
        if a < 1 or last < a:
            raise Stop("%s: its home span runs backwards or starts before line 1 (home=%r)"
                       % (identity, home))
        if last > len(lines):
            raise Stop("%s: its home span ends past the end of %s, which has %d lines (home=%r)"
                       % (identity, doc, len(lines), home))
        span_lines = list(range(a, last + 1))
        if doc == ARCHITECTURE and any(first <= a and last <= end for _, first, end in spans):
            opening = [o for o, first, end in spans if first <= a and last <= end][0]
            where = "inside item 1: %s" % opening
        elif norm(doc) in item2_resolved:
            where = "in an item-2 document that resolves: %s" % doc
        elif doc in spec_paths:
            n = len(hit_lines_by_member.get(doc, set()) & set(span_lines))
            where = "in a specification-set member, %d of its lines being item-3 hit lines" % n
        else:
            where = "reached by item 4 alone"
        passages.append({
            "identity": identity,
            "home_as_cited": home,
            "document": doc,
            "span": {"first_line": a, "last_line": last},
            "the_span_verbatim": [lines[n - 1] for n in span_lines],
            "where_it_falls": where,
        })

    # ---- THE TRANSFER INPUT ------------------------------------------------------------------
    transfer_text = read_text(TRANSFER_SOURCE)
    transfer_bounds = locate_section(transfer_text, TRANSFER_SOURCE,
                                     TRANSFER_SECTION["opens_at"],
                                     TRANSFER_SECTION["closes_before_pattern"])
    t_first, t_last = span_range(transfer_bounds)
    transfer_lines = file_lines(transfer_text)[t_first - 1:t_last]

    # ---- THE MEASURED SIZE -------------------------------------------------------------------
    def falls_kind(where):
        return where.split(":")[0] if ":" in where else where.split(",")[0]

    by_kind = {}
    by_value = {}
    for p in passages:
        by_kind[falls_kind(p["where_it_falls"])] = by_kind.get(
            falls_kind(p["where_it_falls"]), 0) + 1
        by_value[p["where_it_falls"]] = by_value.get(p["where_it_falls"], 0) + 1
    arch_record = population.get(ARCHITECTURE, {})
    measured = {
        "★_the_size_stop": SIZE_STOP_STATEMENT,
        "item_1_lines_per_span": {r["section"]["opens_at"]: r["section"]["lines_in_the_span"]
                                  for r in item1},
        "item_2": {
            "distinct_names": len(distinct_names),
            "distinct_names_that_resolve": sum(1 for d in distinct_names
                                               if d["resolves_at_the_path_as_written"]),
            "summed_bytes_of_the_distinct_names_that_resolve": sum(
                d["bytes"] for d in distinct_names if d["resolves_at_the_path_as_written"]),
            "distinct_names_that_are_specification_set_members": sum(
                1 for d in distinct_names if d["in_the_specification_document_set"]),
        },
        "item_3": {
            "in_set_files_with_a_hit": len(population),
            "total_hit_lines_distinct_over_them": sum(r["hit_lines_distinct"]
                                                      for r in population.values()),
            "of_which_ARCHITECTURE_md_inside_the_four_spans":
                arch_record.get("hit_lines_distinct_inside_the_four_spans"),
            "of_which_ARCHITECTURE_md_outside_the_four_spans":
                arch_record.get("hit_lines_distinct_outside_the_four_spans"),
            "residue_files": len(residue),
        },
        "item_4_passages_by_where_it_falls": dict(sorted(by_kind.items())),
        "item_4_passages_by_where_it_falls_exact_value": dict(sorted(by_value.items())),
        "the_transfer_span_lines": transfer_bounds["lines_in_the_span"],
    }

    reach_item3 = (
        "The forty-two terms are RULED (Ruling 86), but the matcher is a case-insensitive "
        "SUBSTRING match (`tonic` matches inside *diatonic*, `grain` inside longer words), so the "
        "hit set OVER-REACHES in a known direction; and a passage about L2's subject that uses "
        "none of the terms is not found.  The hit set is therefore a LOWER BOUND on the relevant "
        "text, never a census (D-673).  THE UNIT \"PASSAGE\" IS RECORDED HERE AS THE HIT LINE; the "
        "tabulation's unit is fixed by the next dispatch, not by this tool."
    )
    spec_not_searched = sorted(m for m in spec_members if m not in class_of)

    return {
        "★_what_this_artifact_is": (
            "The outgoing population for the L2 comparison, derived and MEASURED under the user's "
            "ruling of 2026-09-27, Option B.  It fixes which current-text passages the "
            "comparison covers, in the ruling's four items, and states how large each is.  It "
            "takes no disposition, orders no tabulation and grades nothing."
        ),
        "★_what_it_does_not_do": (
            "It does not compare, dispose, adopt, relocate, quarantine, discard or grade anything; "
            "it orders no tabulation and fixes no tabulation unit; it edits no outgoing text; and "
            "it does not open the blind L2 derivation, its brief, or the boot pack's directory."
        ),
        "the_ruling": THE_RULING,
        "generator": "tools/audit/gen_l2_outgoing_population.py",
        "one_path_per_concern": (
            "Imported by name and never copied (#6, D-623): `locate_section`, `load_classes`, "
            "`load_specification_document_set`, `search_terms`, `read_text` and `SEARCH_CLASSES` "
            "from gen_l0_l1_outgoing_population; `L2_KEYWORDS` from gen_derivation_boot_pack "
            "(the one home of Ruling 86's forty-two terms); `read_backbone` and `entry_number` "
            "from gen_l2_withheld_documents."
        ),
        "item_1_the_named_sections": {
            "located_in": ARCHITECTURE,
            "the_sections": item1,
            "★_that_these_four_are_L2s_old_ground_is_a_reading_not_a_ruling":
                "The ruling's own words at §2 item 1.",
        },
        "item_2_the_documents_the_sections_name": {
            "the_pattern": MD_NAME.pattern,
            "no_grading_of_form": (
                "Every match inside the four spans is recorded, whether the naming is a "
                "delegation, a citation or a passing mention."
            ),
            "the_occurrences": occurrences,
            "the_distinct_names": distinct_names,
            "the_reach_stated": (
                "A document named without a `.md` suffix, or referred to by description rather "
                "than by file name, is not found by this pattern; the list is a LOWER BOUND on "
                "the documents the four sections name (D-673).  A name that does not resolve at "
                "the path as written is RECORDED as not resolving, never guessed at another path "
                "and never dropped (#12)."
            ),
        },
        "item_3_the_term_search": {
            "the_terms_read_from": "gen_derivation_boot_pack.L2_KEYWORDS — Ruling 86, §3co of "
                                   "cowork_rulings_2026_08_31_decision_surface_sitting.md",
            "the_terms": list(L2_KEYWORDS),
            "one_tier": "every one of the forty-two terms is ruled; one hit admits a line",
            "the_classes_searched": SEARCH_CLASSES,
            "class_membership_read_from": (
                "gen_l0_l1_outgoing_population.load_classes() — never a directory listing"
            ),
            "the_cut": (
                "path equality, exact, against load_specification_document_set() — the ruled "
                "specification document set"
            ),
            "the_heading_rule": (
                "for each hit line in a set member: the nearest heading line (`#` to `######` "
                "then whitespace) STRICTLY BEFORE it, outside fenced code blocks (``` or ~~~); "
                "whether the hit line is itself a heading and whether it lies inside a fenced "
                "code block are recorded beside it"
            ),
            "counts": {
                "per_class": per_class_counts,
                "files_with_a_hit": len(population) + len(residue),
                "in_set_files_with_a_hit": len(population),
                "residue_files": len(residue),
                "paths_in_more_than_one_searched_class": sorted(
                    p for p, cs in classes_of.items() if len(cs) > 1),
                "hits_per_term": dict(sorted(hits_per_term.items(),
                                             key=lambda kv: (-kv[1], kv[0]))),
                "the_six_terms_Ruling_86_records_as_matching_nothing_in_its_own_population": {
                    term: hits_per_term.get(term)
                    for term in THE_SIX_RULING_86_RECORDS_AS_MATCHING_NOTHING
                },
            },
            "the_population": dict(sorted(population.items())),
            "the_residue_for_the_mining_map": {
                "★_what_this_is": (
                    "Every file the term search HIT that is NOT a member of the ruled "
                    "specification document set, published as a listed residue under Ruling "
                    "33's shape, its hit records kept whole (#12).  Nothing here is "
                    "dispositioned by this comparison."
                ),
                "the_statement_that_applies_to_every_entry": THE_RESIDUE_STATEMENT,
                "files": dict(sorted(residue.items())),
            },
            "class_members_absent_from_the_tree": absent,
            "the_reach_stated": reach_item3,
            "specification_set_members_not_in_the_searched_classes": spec_not_searched,
        },
        "item_4_the_decision_passages": {
            "the_identities_read_from": "tools/audit/l2_withheld_documents.json -> in_entries "
                                        "(the set the user confirmed on 2026-09-21)",
            "the_homes_read_from": "gen_l2_withheld_documents.read_backbone() over "
                                   "tools/audit/decisions/backbone_decisions.json",
            "the_home_shape": HOME_SHAPE.pattern,
            "★_the_reconciliation_taken_in_both_directions": (
                "The 111 grouped by the document part of their homes equal l2_withheld_documents"
                ".json -> documents exactly, document by document and identity by identity.  A "
                "failure is a STOP, so this sentence records a check that passed."
            ),
            "where_it_falls_rule": (
                "the first that applies, in this order: `inside item 1: <opening heading>` (the "
                "home span lies wholly inside one of the four spans); `in an item-2 document that "
                "resolves: <path>` (the home's document equals, after path normalization, an "
                "item-2 name that resolves); `in a specification-set member, <n> of its lines "
                "being item-3 hit lines`; `reached by item 4 alone`"
            ),
            "the_passages": passages,
        },
        "the_l0_l1_transfer_input": {
            "★_what_this_is": (
                "The ruling's bound that passages the L0/L1 comparison relocated to L2 enter as "
                "the transfer list (phase definition §3.4).  The span is located and measured; "
                "NO ROW IS PARSED."
            ),
            "located_in": TRANSFER_SOURCE,
            "the_section": transfer_bounds,
            "lines_in_the_span_containing_the_string_L2": sum(1 for line in transfer_lines
                                                              if "L2" in line),
        },
        "the_measured_size": measured,
    }


def main():
    check = "--check" in sys.argv[1:]
    try:
        derived = derive()
    except (Stop, l0l1.Stop, withheld.Stop) as stop:
        print("STOP: %s" % stop)
        return 2
    rendered = json.dumps(derived, indent=1, ensure_ascii=False) + "\n"
    if check:
        if not os.path.isfile(OUT):
            print("STALE vs the derivation: l2_outgoing_population.json does not exist")
            return 1
        with open(OUT, "r", encoding="utf-8") as handle:
            if handle.read() != rendered:
                print("STALE vs the derivation: l2_outgoing_population.json does not re-derive")
                return 1
        print("l2_outgoing_population.json re-derives")
        return 0
    with open(OUT, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(rendered)
    size = derived["the_measured_size"]
    for opens, lines in size["item_1_lines_per_span"].items():
        print("item 1: %s — %d lines" % (opens, lines))
    print("item 2: %(distinct_names)d distinct names, %(distinct_names_that_resolve)d resolve "
          "(%(summed_bytes_of_the_distinct_names_that_resolve)d bytes), "
          "%(distinct_names_that_are_specification_set_members)d in the specification set"
          % size["item_2"])
    i3 = size["item_3"]
    print("item 3: %d in-set files with a hit, %d distinct hit lines over them "
          "(ARCHITECTURE.md inside the four spans: %s, outside: %s); residue files: %d"
          % (i3["in_set_files_with_a_hit"], i3["total_hit_lines_distinct_over_them"],
             i3["of_which_ARCHITECTURE_md_inside_the_four_spans"],
             i3["of_which_ARCHITECTURE_md_outside_the_four_spans"], i3["residue_files"]))
    for kind, n in size["item_4_passages_by_where_it_falls"].items():
        print("item 4: %s — %d" % (kind, n))
    print("transfer span: %d lines" % size["the_transfer_span_lines"])
    print("THIS BATCH TABULATES NOTHING.")
    print("wrote %s" % OUT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
