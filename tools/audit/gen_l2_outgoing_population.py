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

  6. `the_tabulation_population` -- the population cut into the MEMBERS the comparison tabulates,
     in its order, under the named-documents ruling of 2026-09-27 (Option B) and THE_PASSAGE_RULE;
     with two further STOPs: item 2's derived names differing from the ruling's two lists, and a
     hit line or an item-4 home not lying in exactly one member.

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
boot pack's directory.  THE TABULATION'S ORDER IS PUBLISHED HERE; ITS UNIT IS THE TABULATING DISPATCH'S.

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
    "THE TABULATION RUNS IN THE ORDER OF `the_tabulation_population`, ONE MEMBER PER COMMIT, AND "
    "MAY STOP AT ANY MEMBER BOUNDARY (D-672).  Its unit, the outgoing statement, is fixed by the "
    "dispatch that tabulates, not by this tool."
)

# --------------------------------------------------------------------------------------------
# THE NAMED-DOCUMENTS RULING -- which of item 2's documents are compared WHOLE.  User, 2026-09-27,
# `records/cowork/rulings/cowork_rulings_2026_09_27_l2_named_documents_sitting.md` §1, Option B.
# AUTHORED from the ruling's own lists; the union must equal item 2's derived names EXACTLY, in both
# directions, or the run STOPs -- so a name entering or leaving the four spans halts it.
# --------------------------------------------------------------------------------------------
THE_NAMED_DOCUMENTS_RULING = {
    "record": "records/cowork/rulings/cowork_rulings_2026_09_27_l2_named_documents_sitting.md",
    "section": "§1 — Ruling — Option B",
    "executed_by": "records/cc/instructions/cc_instruction_l2_comparison_tabulation_2026_09_27.md, "
                   "Task 1",
}

ITEM_2_WHOLE = [
    "cowork_joint_estimator_factorization.md",
    "cowork_layer3_keymode_design.md",
    "cowork_layer4_chordsymbol_design.md",
    "cowork_layer5_engagement_design.md",
    "cowork_layer5_function_design.md",
    "cowork_prefit_gates.md",
    "cowork_score_census.md",
    "cowork_stage5_fitter_design.md",
    "cowork_engage_arc_plan.md",
    "cowork_l1l4_review_charter.md",
    "cowork_phase5b_l4_build_plan.md",
    "docs/nct_detection_design.md",
]

ITEM_2_LISTED_NOT_WHOLE = [
    "CLAUDE.md",
    "OPEN_ITEMS.md",
    "DEFECT_TYPES.md",
    "open_items/OI-176.md",
    "open_items/OI-177.md",
    "records/cc/reports/cc_layer3_wiring_report.md",
    "records/cc/reports/cc_tonicization_modulation_metric_dossier.md",
    "records/cowork/rulings/cowork_rulings_2026_08_11_fourteenth_stop.md",
]

TOP_LEVEL = re.compile(r"^## ")

THE_PASSAGE_RULE = (
    "A passage is the block of lines holding one item-3 hit line, or spanning one item-4 home: "
    "(a) a line inside a fenced code block takes the whole block, fence lines included; (b) any "
    "other line takes the maximal run of consecutive non-blank lines around it, stopping at a blank "
    "line or a fence line; (c) where that run is one heading line standing alone, it takes the "
    "heading together with the block that follows it (blank lines skipped), unless the next "
    "non-blank line is a heading or a fence.  An item-4 home spanning lines a..b takes the block "
    "around a through the block around b.  Overlapping or touching passages of one document merge.  "
    "In ARCHITECTURE.md every line inside the four item-1 spans is removed from the passages (those "
    "spans are tabulated whole), and the passages are grouped by the nearest top-level `## ` heading "
    "at or before them, the lines before the first such heading forming the opening block."
)

THE_ORDER = (
    "1-4: the four item-1 sections, in ARCHITECTURE.md's order.  Then the twelve WHOLE item-2 "
    "documents: the specification-set members first, then the others; within each group by "
    "descending count of distinct item-3 hit lines, ties by path.  Then ARCHITECTURE.md's passages, "
    "one member per top-level `## ` section, in the file's order.  Then every other document "
    "carrying passages: the specification-set members by descending count of their distinct item-3 "
    "hit lines, ties by path; then the documents reached by item 4 alone, by path.  Last: the L0/L1 "
    "transfer input."
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


def fence_ranges(lines):
    """1-based (first, last) of every fenced code block, fence lines included; an unclosed fence
    runs to the end of the file.  The fence test is FENCE, the one `headings_by_line` uses."""
    out = []
    start = None
    for number, line in enumerate(lines, 1):
        if FENCE.match(line):
            if start is None:
                start = number
            else:
                out.append((start, number))
                start = None
    if start is not None:
        out.append((start, len(lines)))
    return out


def block_around(lines, number, fences):
    """THE PASSAGE RULE (THE_PASSAGE_RULE, (a) to (c)) for one 1-based line."""
    for first, last in fences:
        if first <= number <= last:
            return first, last
    fenced = set()
    for first, last in fences:
        fenced.update(range(first, last + 1))

    def stops(n):
        return lines[n - 1].strip() == "" or n in fenced

    first = last = number
    while first > 1 and not stops(first - 1):
        first -= 1
    while last < len(lines) and not stops(last + 1):
        last += 1
    if first == last and HEADING.match(lines[first - 1]):
        following = last + 1
        while following <= len(lines) and lines[following - 1].strip() == "":
            following += 1
        if (following <= len(lines) and following not in fenced
                and not HEADING.match(lines[following - 1])):
            last = block_around(lines, following, fences)[1]
    return first, last


def merge_ranges(ranges):
    """The sorted union of 1-based inclusive ranges; overlapping or touching ranges merge."""
    out = []
    for first, last in sorted(ranges):
        if out and first <= out[-1][1] + 1:
            out[-1] = (out[-1][0], max(out[-1][1], last))
        else:
            out.append((first, last))
    return out


def subtract_spans(ranges, spans):
    """`ranges` with every line inside any (first, last) of `spans` removed, a range split where a
    span cuts it; the result merged."""
    out = []
    for first, last in ranges:
        pieces = [(first, last)]
        for s_first, s_last in spans:
            kept = []
            for a, b in pieces:
                if b < s_first or a > s_last:
                    kept.append((a, b))
                    continue
                if a < s_first:
                    kept.append((a, s_first - 1))
                if b > s_last:
                    kept.append((s_last + 1, b))
            pieces = kept
        out.extend(pieces)
    return merge_ranges(out)


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

    # ---- THE TABULATION POPULATION (the named-documents ruling; THE_PASSAGE_RULE; THE_ORDER) -----
    names_derived = {d["name_as_written"] for d in distinct_names}
    ruled_whole = set(ITEM_2_WHOLE)
    ruled_listed = set(ITEM_2_LISTED_NOT_WHOLE)
    if len(ruled_whole) != len(ITEM_2_WHOLE) or len(ruled_listed) != len(ITEM_2_LISTED_NOT_WHOLE):
        raise Stop("a name is listed twice in the named-documents ruling's lists")
    if ruled_whole & ruled_listed:
        raise Stop("ruled both WHOLE and LISTED: %s" % sorted(ruled_whole & ruled_listed))
    if names_derived != ruled_whole | ruled_listed:
        raise Stop("item 2's derived names disagree with the named-documents ruling: derived only "
                   "%s; ruled only %s" % (sorted(names_derived - (ruled_whole | ruled_listed)),
                                          sorted((ruled_whole | ruled_listed) - names_derived)))
    for name in ITEM_2_WHOLE:
        if not distinct[name]["resolves_at_the_path_as_written"]:
            raise Stop("%s is ruled WHOLE and does not resolve at the path as written" % name)

    cache = {ARCHITECTURE: arch_lines}

    def lines_of(path):
        if path not in cache:
            cache[path] = file_lines(read_text(path))
        return cache[path]

    def hit_lines_of(path):
        record = population.get(path) or residue.get(path)
        return {h["line_number"] for h in record["hit_records"]} if record else set()

    whole_norm = {norm(p) for p in ITEM_2_WHOLE}
    arch_spans = [(first, last) for _, first, last in spans]
    passage_ranges = {}
    passage_hit_count = {}
    for path, record in population.items():
        if norm(path) in whole_norm:
            continue
        lines = lines_of(path)
        fences = fence_ranges(lines)
        hit_set = {h["line_number"] for h in record["hit_records"]}
        if path == ARCHITECTURE:
            hit_set = {n for n in hit_set if not item1_span_of(n)}
        passage_hit_count[path] = len(hit_set)
        passage_ranges.setdefault(path, []).extend(
            block_around(lines, n, fences) for n in sorted(hit_set))
    for p in passages:
        where = p["where_it_falls"]
        if where.startswith("inside item 1"):
            continue
        if where.startswith("in an item-2 document") and norm(p["document"]) in whole_norm:
            continue
        lines = lines_of(p["document"])
        fences = fence_ranges(lines)
        first = block_around(lines, p["span"]["first_line"], fences)[0]
        last = block_around(lines, p["span"]["last_line"], fences)[1]
        passage_ranges.setdefault(p["document"], []).append((first, last))
    for path in list(passage_ranges):
        merged = merge_ranges(passage_ranges[path])
        if path == ARCHITECTURE:
            merged = subtract_spans(merged, arch_spans)
        passage_ranges[path] = merged

    def make_member(kind, document, label, ranges):
        lines = lines_of(document)
        body = [lines[n - 1] for first, last in ranges for n in range(first, last + 1)]
        return {
            "kind": kind,
            "document": document,
            "label": label,
            "ranges": [{"first_line_as_a_locator_only": first,
                        "last_line_as_a_locator_only": last,
                        "first_line_text": lines[first - 1],
                        "last_line_text": lines[last - 1]} for first, last in ranges],
            "lines": len(body),
            "bytes": len(("\n".join(body) + "\n").encode("utf-8")) if body else 0,
        }

    members = []
    for record in item1:
        first, last = span_range(record["section"])
        members.append(make_member("item 1 — a named section", ARCHITECTURE,
                                   record["section"]["opening_heading_as_found"], [(first, last)]))
    for path in sorted(ITEM_2_WHOLE, key=lambda p: (p not in spec_paths, -len(hit_lines_of(p)), p)):
        members.append(make_member(
            "item 2 — a whole document" + (" (a specification-set member)" if path in spec_paths
                                           else " (not a specification-set member)"),
            path, "the whole document", [(1, len(lines_of(path)))]))
    if ARCHITECTURE in passage_ranges:
        fences = fence_ranges(arch_lines)
        fenced = set()
        for first, last in fences:
            fenced.update(range(first, last + 1))
        heads = [n for n, line in enumerate(arch_lines, 1)
                 if n not in fenced and TOP_LEVEL.match(line)]
        groups = {}
        for first, last in passage_ranges[ARCHITECTURE]:
            x = first
            while x <= last:
                prior = [h for h in heads if h <= x]
                later = [h for h in heads if h > x]
                key = prior[-1] if prior else 0
                end = min(last, later[0] - 1) if later else last
                groups.setdefault(key, []).append((x, end))
                x = end + 1
        for key in sorted(groups):
            label = (arch_lines[key - 1] if key
                     else "the opening block, above the first `## ` heading")
            members.append(make_member("items 3 and 4 — passages of a specification-set member",
                                       ARCHITECTURE, label, merge_ranges(groups[key])))
    others = [p for p in passage_ranges if p != ARCHITECTURE]
    in_set = sorted((p for p in others if p in spec_paths),
                    key=lambda p: (-passage_hit_count.get(p, 0), p))
    alone = sorted(p for p in others if p not in spec_paths)
    for path in in_set:
        members.append(make_member("items 3 and 4 — passages of a specification-set member",
                                   path, "the passages of the document", passage_ranges[path]))
    for path in alone:
        members.append(make_member("item 4 — passages reached by item 4 alone",
                                   path, "the passages of the document", passage_ranges[path]))
    members.append(make_member("the L0/L1 transfer input", TRANSFER_SOURCE,
                               transfer_bounds["opening_heading_as_found"], [(t_first, t_last)]))
    for position, member in enumerate(members, 1):
        member["position"] = position
        member["item_3_hit_lines_inside"] = 0
        member["item_4_identities_inside"] = []

    def members_holding(document, first, last):
        return [m for m in members if norm(m["document"]) == norm(document) and any(
            r["first_line_as_a_locator_only"] <= first and last <= r["last_line_as_a_locator_only"]
            for r in m["ranges"])]

    for path, record in population.items():
        for n in sorted({h["line_number"] for h in record["hit_records"]}):
            holding = members_holding(path, n, n)
            if len(holding) != 1:
                raise Stop("item-3 hit line %s:%d lies in %d tabulation members, not one"
                           % (path, n, len(holding)))
            holding[0]["item_3_hit_lines_inside"] += 1
    for p in passages:
        holding = members_holding(p["document"], p["span"]["first_line"], p["span"]["last_line"])
        if len(holding) != 1:
            raise Stop("%s's home %s lies wholly in %d tabulation members, not one"
                       % (p["identity"], p["home_as_cited"], len(holding)))
        holding[0]["item_4_identities_inside"].append(
            {"identity": p["identity"], "home_as_cited": p["home_as_cited"]})
    listed = [{"name": name, "bytes": distinct[name]["bytes"],
               "inventory_class": distinct[name]["inventory_class"],
               "in_the_residue": name in residue,
               "the_statement": "named inside the four item-1 spans; LISTED and not compared "
                                "whole under the named-documents ruling; the lines that name it "
                                "are tabulated inside item 1"}
              for name in ITEM_2_LISTED_NOT_WHOLE]

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
        "the_tabulation_population": {
            "members": len(members),
            "members_by_kind": {k: sum(1 for m in members if m["kind"] == k)
                                for k in sorted({m["kind"] for m in members})},
            "lines_by_kind": {k: sum(m["lines"] for m in members if m["kind"] == k)
                              for k in sorted({m["kind"] for m in members})},
            "bytes_by_kind": {k: sum(m["bytes"] for m in members if m["kind"] == k)
                              for k in sorted({m["kind"] for m in members})},
            "lines_total": sum(m["lines"] for m in members),
            "bytes_total": sum(m["bytes"] for m in members),
        },
    }

    reach_item3 = (
        "The forty-two terms are RULED (Ruling 86), but the matcher is a case-insensitive "
        "SUBSTRING match (`tonic` matches inside *diatonic*, `grain` inside longer words), so the "
        "hit set OVER-REACHES in a known direction; and a passage about L2's subject that uses "
        "none of the terms is not found.  The hit set is therefore a LOWER BOUND on the relevant "
        "text, never a census (D-673).  The hit records here are LINES; the passages cut around "
        "them are at `the_tabulation_population` under `the_passage_rule`."
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
        "the_named_documents_ruling": THE_NAMED_DOCUMENTS_RULING,
        "the_tabulation_population": {
            "★_what_this_is": (
                "The outgoing population cut into the MEMBERS the comparison tabulates, in the "
                "order it tabulates them, under the ruling of 2026-09-27 (Option B), the "
                "named-documents ruling of the same date (Option B) and the passage rule below.  "
                "Every item-3 hit line of every specification-set member lies in exactly one "
                "member, and every one of the 111 item-4 homes lies wholly in exactly one member; "
                "either failing is a STOP, so this sentence records checks that passed.  It takes "
                "no disposition and grades nothing."
            ),
            "the_passage_rule": THE_PASSAGE_RULE,
            "the_order": THE_ORDER,
            "item_2_listed_not_compared_whole": listed,
            "the_members": members,
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
    tp = size["the_tabulation_population"]
    print("tabulation population: %d members, %d lines, %d bytes"
          % (tp["members"], tp["lines_total"], tp["bytes_total"]))
    print("wrote %s" % OUT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
