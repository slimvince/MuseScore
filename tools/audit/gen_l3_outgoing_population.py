#!/usr/bin/env python3
"""DERIVE AND MEASURE THE OUTGOING POPULATION FOR THE L3 COMPARISON -- NOTHING TABULATED.

WHY THIS EXISTS.  Two rulings of the user fix which existing texts the blind L3 derivation
(`cowork_blind_derivation_l3_2026_10_17.md`) is compared against -- the L3 comparison's OUTGOING
POPULATION.  Option B of 2026-10-17
(`records/cowork/rulings/cowork_rulings_2026_10_17_l3_outgoing_population_sitting.md` §2) fixes it in
four items, and Option B of 2026-10-18
(`records/cowork/rulings/cowork_rulings_2026_10_18_l3_keyword_list_sitting.md` §2) rules the 26-term
keyword list that item 3 searches for.  Three of the four items are defined by something that has
to be RUN (a pattern over six sections of one file, a term search, a read of the register's data
file), and the 2026-10-17 record says the population's size is unmeasured until the dispatch
measures it before tabulating, with a size stop.  This tool is that derivation and that
measurement, and nothing else.

WHAT IT DOES, AND NOTHING ELSE.  Every numbered item is a key of the artifact.

  1. `item_1_the_named_sections` -- LOCATES the six `ARCHITECTURE.md` places the 2026-10-17 ruling
     names, BY HEADING TEXT, never by line number (D-307), with the L0/L1 tool's own
     `locate_section`: the Layer 4, Layer 5 and Layer 6 sections; section 4.3 whole (it holds the
     "Note on figured bass"); section 4.3b; and the "Harmonic rhythm detection" passage of section
     11.5.  A heading not found is a STOP; two spans overlapping is a STOP.

  2. `item_2_the_documents_the_sections_name` -- every match of `[A-Za-z0-9_./-]+\\.md\\b` inside
     the six spans, MECHANICALLY and with no grading of form.  A name that does not resolve at the
     path as written is RECORDED, never guessed at another path and never dropped (#12).  Which of
     these documents is compared whole is a LATER question (the 2026-10-17 ruling, item 2); this
     tool takes no position on it.

  3. `item_3_the_term_search` -- the 26 terms ruled on 2026-10-18, whose ONE HOME is this file
     (`L3_KEYWORDS`, authored from the ruling record's §2 lists), searched with the L0/L1 tool's own
     `search_terms` over every file of its `SEARCH_CLASSES` as its `load_classes()` reads them.
     Hit files IN the ruled specification document set are the population; every other hit file
     is the RESIDUE, published whole under Ruling 33's shape.  Nothing is dropped.

  4. `item_4_the_decision_passages` -- the 22 decisions ruled withheld from L3's boot pack (the
     confirmed set at `tools/audit/l3_withheld_documents.json` -> `in_entries`), each read at its
     home in the register's data file through `gen_l2_withheld_documents.read_backbone()`, the
     home's lines quoted verbatim, and where each passage falls relative to items 1-3.  GENERATED,
     NEVER TYPED (D-431).

  5. `the_transfer_input` and `the_measured_size` -- the transfer lists' spans in the L0/L1 and the
     L2 comparison reading files, located by heading text and NOT parsed; and one block of computed
     sizes a reader can read without the rest.  Every figure is computed; none is authored.

  6. `the_tabulation_population` -- the population cut into the MEMBERS the comparison tabulates,
     in its order, under the named-documents derivation of the tabulation dispatch and
     THE_PASSAGE_RULE (the L2 comparison's, imported); with three further STOPs: item 2's derived
     names differing from the derivation's two lists, a specification-set member among them not
     graded WHOLE, and a hit line or an item-4 home not lying in exactly one member.

ONE PATH PER CONCERN (#6; D-623 -- a capability is a parameter, never a sibling copy).  The
section locator, the class reader, the specification-set reader, the term matcher and the text
reader are IMPORTED from `gen_l0_l1_outgoing_population`; the line splitter, the span-range
helper, the heading walker, the path normaliser, the `.md`-name pattern, the home-shape pattern
and the residue statement from `gen_l2_outgoing_population` -- a HISTORICAL RECORD in the guard
runner: importing it executes its module level (constants and function definitions) and never its
`derive()` or `main()`, so its committed artifact is not touched; the backbone reader and the
identity order from `gen_l2_withheld_documents`.  None of them is copied, and none of those tools
is edited.

THE STOPS, each ending the run with `STOP: <reason>` and exit 2 -- never a traceback, whichever
`Stop` class raised it:
  - the term list is not 26 long, carries a term twice, or carries one of the three EXCLUDED terms;
  - a heading of item 1 or of a transfer span is not found; two item-1 spans overlap; a searched
    or home document cannot be read;
  - the confirmed identity list is not 22 long; an identity is absent from the backbone; a home is
    of any shape other than `<doc>.md:<a>` or `<doc>.md:<a>-<b>`; a span is past its file's end or
    runs backwards;
  - grouping the 22 by the document part of their homes disagrees, in either direction, with the
    confirmed artifact's `documents`.

WHAT IT DOES NOT DO.  It takes no disposition, fixes no tabulation unit,
grades nothing, compares nothing, and edits no outgoing text.  It does not open the blind
derivation, its brief, or the boot pack's directory.  THE TABULATION'S ORDER IS PUBLISHED HERE; ITS
UNIT IS THE TABULATING DISPATCH'S.

Run:
    python tools/audit/gen_l3_outgoing_population.py           # write the artifact
    python tools/audit/gen_l3_outgoing_population.py --check   # re-derive, exit 1 on drift
"""
from __future__ import annotations

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(HERE, "l3_outgoing_population.json")
WITHHELD = os.path.join(HERE, "l3_withheld_documents.json")

sys.path.insert(0, HERE)
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 -- the findings must survive a non-console stdout

import gen_l0_l1_outgoing_population as l0l1     # noqa: E402  (path set above)
import gen_l2_outgoing_population as l2pop       # noqa: E402  (imported for its helpers; never run)
import gen_l2_withheld_documents as withheld     # noqa: E402  (path set above)
from gen_l0_l1_outgoing_population import (      # noqa: E402  (path set above)
    SEARCH_CLASSES,
    load_classes,
    load_specification_document_set,
    locate_section,
    read_text,
    search_terms,
)
from gen_l2_outgoing_population import (         # noqa: E402  (path set above)
    HOME_SHAPE,
    MD_NAME,
    THE_RESIDUE_STATEMENT,
    TOP_LEVEL,
    block_around,
    fence_ranges,
    file_lines,
    headings_by_line,
    merge_ranges,
    norm,
    span_range,
    subtract_spans,
)
from gen_l2_withheld_documents import entry_number, read_backbone  # noqa: E402

RULED_TERM_COUNT = 26
RULED_IDENTITY_COUNT = 22
ARCHITECTURE = "ARCHITECTURE.md"


class Stop(Exception):
    """A count moved, a heading is missing, a home cannot be read, or a reconciliation fails."""


# --------------------------------------------------------------------------------------------
# THE TWO RULINGS.
# --------------------------------------------------------------------------------------------
THE_RULING = {
    "record": "records/cowork/rulings/cowork_rulings_2026_10_17_l3_outgoing_population_sitting.md",
    "section": "§2 — Ruling — Option B",
    "executed_by": "records/cc/instructions/cc_instruction_l3_outgoing_population_2026_10_18.md, Task 1",
}

THE_KEYWORD_RULING = {
    "record": "records/cowork/rulings/cowork_rulings_2026_10_18_l3_keyword_list_sitting.md",
    "section": "§2 — Ruling — Option B",
    "what_it_rules": "L3's keyword list is these 26 terms, and no others; continuo, sentence and "
                     "bass are excluded; phrase grouping, thoroughbass and read-off are kept "
                     "although the count found no hit for them (a term that matches nothing costs "
                     "nothing).",
}

# THE ONE HOME of L3's 26 ruled terms -- AUTHORED from the 2026-10-18 record's §2 lists, in the
# record's order: the 21 core terms, then the 5 counted-in-context terms.  Nothing else in the
# repository carries this list (gen_derivation_boot_pack.SUBJECTS["l3"]["keywords"] is empty).
L3_KEYWORDS = (
    "cadence", "cadential", "plagal", "phrase end",
    "phrase boundary", "phrase grouping", "grouping layer",
    "chord symbol", "chord-symbol", "chordsymbol", "bass note", "slash chord", "root pitch class",
    "inversion",
    "figured bass", "figured-bass", "thoroughbass",
    "harmonic rhythm", "harmonic-rhythm", "harmonicrhythm",
    "read-off",
    "phrase", "grouping", "period", "contradiction", "deceptive",
)
THE_THREE_EXCLUDED = ("continuo", "sentence", "bass")
THE_THREE_KEPT_WITH_NO_HIT_AT_THE_COUNT = ("phrase grouping", "thoroughbass", "read-off")

# --------------------------------------------------------------------------------------------
# THE SIX PLACES item 1 names -- located by TEXT (D-307).  `opens_at` is matched as the start of a
# line (the first such line); `closes_before_pattern` is matched as the start of a later line.
# --------------------------------------------------------------------------------------------
NAMED_SECTIONS = [
    {"opens_at": "#### Layer 4 — the per-slice chord-symbol decoder",
     "closes_before_pattern": r"^#### "},
    {"opens_at": "#### Layer 5 — the function/cadence layer",
     "closes_before_pattern": r"^#### "},
    {"opens_at": "#### Layer 6 — the grouping layer",
     "closes_before_pattern": r"^#### "},
    {"opens_at": "### 4.3 ChordSymbolFormatter",
     "closes_before_pattern": r"^### "},
    {"opens_at": "### 4.3b HarmonicRhythm",
     "closes_before_pattern": r"^### "},
    {"opens_at": "#### Harmonic rhythm detection",
     "closes_before_pattern": r"^#{1,4} "},
]

TRANSFER_SOURCES = [
    {"path": "ratification_surfaces/cowork_comparison_l0_l1_reading.md",
     "opens_at": "## 10. The TRANSFER LIST — every RELOCATED row, by target charter",
     "closes_before_pattern": r"^## "},
    {"path": "ratification_surfaces/cowork_comparison_l2_reading.md",
     "opens_at": "## 10. The TRANSFER LIST — every RELOCATED row, by target charter",
     "closes_before_pattern": r"^## "},
]

SIZE_STOP_STATEMENT = (
    "THE TABULATION RUNS IN THE ORDER OF `the_tabulation_population`, ONE MEMBER PER COMMIT, AND "
    "MAY STOP AT ANY MEMBER BOUNDARY (D-672).  Its unit, the outgoing statement, is fixed by the "
    "dispatch that tabulates, not by this tool."
)

# --------------------------------------------------------------------------------------------
# THE NAMED-DOCUMENTS DERIVATION -- which of item 2's documents are compared WHOLE.  Not a ruling:
# the 2026-10-17 ruling (item 2) says the named documents are graded afterwards AS THE L2
# NAMED-DOCUMENTS RULING GRADED L2's, a question put to the user only where the measurement raises
# one.  The writing side applied that ruling's three classes to the twelve derived names on
# 2026-10-18 and found every name already placed by them (the tabulation dispatch records the
# derivation); the user may overrule it.  AUTHORED from that derivation; the union must equal
# item 2's derived names EXACTLY, in both directions, and every specification-set member among
# them must be WHOLE, or the run STOPs -- so a name entering or leaving the six spans halts it.
# --------------------------------------------------------------------------------------------
THE_NAMED_DOCUMENTS_DERIVATION = {
    "derived_by": "records/cc/instructions/cc_instruction_l3_comparison_tabulation_2026_10_18.md, "
                  "the section THE NAMED-DOCUMENTS DERIVATION, applying the classes of "
                  "records/cowork/rulings/cowork_rulings_2026_09_27_l2_named_documents_sitting.md §1 "
                  "under item 2 of the 2026-10-17 ruling",
    "what_it_is": "a derivation by the writing side, not a ruling; no question was raised that the "
                  "record does not answer, so none was put to the user",
    "executed_by": "records/cc/instructions/cc_instruction_l3_comparison_tabulation_2026_10_18.md, "
                   "Task 1",
}

ITEM_2_WHOLE = [
    "cowork_layer4_chordsymbol_design.md",
    "cowork_layer5_engagement_design.md",
    "cowork_layer5_function_design.md",
    "cowork_layer6_grouping_design.md",
    "cowork_engage_arc_plan.md",
    "cowork_l1l4_review_charter.md",
    "cowork_phase5b_l4_build_plan.md",
    "docs/nct_detection_design.md",
]

ITEM_2_LISTED_NOT_WHOLE = [
    "CLAUDE.md",
    "OPEN_ITEMS.md",
    "records/cc/reports/cc_tonicization_modulation_metric_dossier.md",
    "records/cowork/rulings/cowork_rulings_2026_08_09_second_stop.md",
]

THE_PASSAGE_RULE = (
    "A passage is the block of lines holding one item-3 hit line, or spanning one item-4 home: "
    "(a) a line inside a fenced code block takes the whole block, fence lines included; (b) any "
    "other line takes the maximal run of consecutive non-blank lines around it, stopping at a blank "
    "line or a fence line; (c) where that run is one heading line standing alone, it takes the "
    "heading together with the block that follows it (blank lines skipped), unless the next "
    "non-blank line is a heading or a fence.  An item-4 home spanning lines a..b takes the block "
    "around a through the block around b.  Overlapping or touching passages of one document merge.  "
    "In ARCHITECTURE.md every line inside the six item-1 spans is removed from the passages (those "
    "spans are tabulated whole), and the passages are grouped by the nearest top-level `## ` heading "
    "at or before them, the lines before the first such heading forming the opening block.  The "
    "rule and the four functions that implement it are the L2 comparison's, imported from "
    "gen_l2_outgoing_population and not copied."
)

THE_ORDER = (
    "1-6: the six item-1 places, in ARCHITECTURE.md's order.  Then the eight WHOLE item-2 "
    "documents: the specification-set members first, then the others; within each group by "
    "descending count of distinct item-3 hit lines, ties by path.  Then ARCHITECTURE.md's passages, "
    "one member per top-level `## ` section, in the file's order.  Then every other document "
    "carrying passages: the specification-set members by descending count of their distinct item-3 "
    "hit lines, ties by path; then the documents reached by item 4 alone, by path.  Last: the two "
    "transfer inputs, the L0/L1 comparison's section 10 span and then the L2 comparison's."
)


# --------------------------------------------------------------------------------------------
def derive():
    if len(L3_KEYWORDS) != RULED_TERM_COUNT:
        raise Stop("L3_KEYWORDS carries %d terms; the 2026-10-18 ruling rules %d"
                   % (len(L3_KEYWORDS), RULED_TERM_COUNT))
    if len(set(L3_KEYWORDS)) != RULED_TERM_COUNT:
        raise Stop("L3_KEYWORDS carries a term twice")
    excluded_present = [t for t in THE_THREE_EXCLUDED if t in L3_KEYWORDS]
    if excluded_present:
        raise Stop("L3_KEYWORDS carries excluded term(s): %s" % excluded_present)

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
    for i in range(len(spans)):
        for j in range(i + 1, len(spans)):
            a_first, a_last = spans[i][1], spans[i][2]
            b_first, b_last = spans[j][1], spans[j][2]
            if a_first <= b_last and b_first <= a_last:
                raise Stop("item-1 spans overlap: %r and %r" % (spans[i][0], spans[j][0]))

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
    hits_per_term = {term: 0 for term in L3_KEYWORDS}
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
            hits = search_terms(text, L3_KEYWORDS, "admitting")
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
                    record["hit_lines_distinct_inside_the_six_spans"] = len(inside)
                    record["hit_lines_distinct_outside_the_six_spans"] = len(every - inside)
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
        raise Stop("l3_withheld_documents.json -> in_entries carries %s identities; the confirmed "
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
        raise Stop("grouping the 22 by home document disagrees with l3_withheld_documents.json "
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
    transfer = []
    for source in TRANSFER_SOURCES:
        t_text = read_text(source["path"])
        t_bounds = locate_section(t_text, source["path"], source["opens_at"],
                                  source["closes_before_pattern"])
        t_first, t_last = span_range(t_bounds)
        t_lines = file_lines(t_text)[t_first - 1:t_last]
        transfer.append({
            "located_in": source["path"],
            "the_section": t_bounds,
            "lines_in_the_span_containing_the_string_L3": sum(1 for line in t_lines
                                                              if "L3" in line),
            "lines_in_the_span_beginning_a_To_L3_header": sum(
                1 for line in t_lines if line.startswith("**To ") and "L3" in line),
        })

    # ---- THE TABULATION POPULATION (the named-documents derivation; THE_PASSAGE_RULE; THE_ORDER) --
    names_derived = {d["name_as_written"] for d in distinct_names}
    graded_whole = set(ITEM_2_WHOLE)
    graded_listed = set(ITEM_2_LISTED_NOT_WHOLE)
    if (len(graded_whole) != len(ITEM_2_WHOLE)
            or len(graded_listed) != len(ITEM_2_LISTED_NOT_WHOLE)):
        raise Stop("a name is listed twice in the named-documents derivation's lists")
    if graded_whole & graded_listed:
        raise Stop("graded both WHOLE and LISTED: %s" % sorted(graded_whole & graded_listed))
    if names_derived != graded_whole | graded_listed:
        raise Stop("item 2's derived names disagree with the named-documents derivation: derived "
                   "only %s; graded only %s"
                   % (sorted(names_derived - (graded_whole | graded_listed)),
                      sorted((graded_whole | graded_listed) - names_derived)))
    for name in sorted(names_derived):
        if name in spec_paths and name not in graded_whole:
            raise Stop("%s is a specification-set member named by item 2 and is not graded WHOLE"
                       % name)
    for name in ITEM_2_WHOLE:
        if not distinct[name]["resolves_at_the_path_as_written"]:
            raise Stop("%s is graded WHOLE and does not resolve at the path as written" % name)

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
        members.append(make_member("item 1 — a named place", ARCHITECTURE,
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
    for t in transfer:
        t_first, t_last = span_range(t["the_section"])
        members.append(make_member("the transfer input — a section 10 span of an earlier "
                                   "comparison's reading file", t["located_in"],
                                   t["the_section"]["opening_heading_as_found"],
                                   [(t_first, t_last)]))
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
               "the_statement": "named inside the six item-1 spans; LISTED and not compared whole "
                                "under the named-documents derivation; the lines that name it are "
                                "tabulated inside item 1"}
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
            "of_which_ARCHITECTURE_md_inside_the_six_spans":
                arch_record.get("hit_lines_distinct_inside_the_six_spans"),
            "of_which_ARCHITECTURE_md_outside_the_six_spans":
                arch_record.get("hit_lines_distinct_outside_the_six_spans"),
            "residue_files": len(residue),
        },
        "item_4_passages_by_where_it_falls": dict(sorted(by_kind.items())),
        "item_4_passages_by_where_it_falls_exact_value": dict(sorted(by_value.items())),
        "the_transfer_spans_lines": {t["located_in"]: t["the_section"]["lines_in_the_span"]
                                     for t in transfer},
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
        "The 26 terms are RULED (2026-10-18), but the matcher is a case-insensitive SUBSTRING "
        "match (`period` matches inside *periodic*, `grouping` inside *regrouping*, `phrase` "
        "inside *paraphrase*), so the hit set OVER-REACHES in a known direction; and a passage "
        "about L3's subject that uses none of the terms is not found.  The hit set is therefore a "
        "LOWER BOUND on the relevant text, never a census (D-673).  The hit records here are "
        "LINES; the passages cut around them are at `the_tabulation_population` under "
        "`the_passage_rule`."
    )
    spec_not_searched = sorted(m for m in spec_members if m not in class_of)

    return {
        "★_what_this_artifact_is": (
            "The outgoing population for the L3 comparison, derived and MEASURED under the user's "
            "rulings of 2026-10-17 (Option B, four items) and 2026-10-18 (Option B, the 26-term "
            "keyword list).  It fixes which current-text passages the comparison covers, in the "
            "ruling's four items, and states how large each is; `the_tabulation_population` cuts "
            "it into the members the comparison tabulates, in their order.  It takes no "
            "disposition and grades nothing."
        ),
        "★_what_it_does_not_do": (
            "It does not compare, dispose, adopt, relocate, quarantine, discard or grade anything; "
            "it fixes no tabulation unit; which of item 2's documents are compared whole it "
            "carries as the writing side's derivation, not as a ruling; it edits no outgoing "
            "text; and it does not open the blind "
            "L3 derivation, its brief, or the boot pack's directory."
        ),
        "the_ruling": THE_RULING,
        "the_keyword_ruling": THE_KEYWORD_RULING,
        "generator": "tools/audit/gen_l3_outgoing_population.py",
        "one_path_per_concern": (
            "Imported by name and never copied (#6, D-623): `locate_section`, `load_classes`, "
            "`load_specification_document_set`, `search_terms`, `read_text` and `SEARCH_CLASSES` "
            "from gen_l0_l1_outgoing_population; `file_lines`, `span_range`, `headings_by_line`, "
            "`norm`, `MD_NAME`, `HOME_SHAPE`, `THE_RESIDUE_STATEMENT`, `TOP_LEVEL`, `fence_ranges`, "
            "`block_around`, `merge_ranges` and `subtract_spans` from "
            "gen_l2_outgoing_population (a historical record: imported, never run); "
            "`read_backbone` and `entry_number` from gen_l2_withheld_documents."
        ),
        "item_1_the_named_sections": {
            "located_in": ARCHITECTURE,
            "the_sections": item1,
            "★_that_section_4_3_is_taken_whole_is_a_reading": (
                "The ruling names section 4.3 (ChordSymbolFormatter, with its Note on figured "
                "bass); the Note is a subsection of 4.3, and the span here is 4.3 whole, its two "
                "subsections included -- the writing side's reading, stated on the dispatch."
            ),
        },
        "item_2_the_documents_the_sections_name": {
            "the_pattern": MD_NAME.pattern,
            "no_grading_of_form": (
                "Every match inside the six spans is recorded, whether the naming is a "
                "delegation, a citation or a passing mention.  Which documents are compared whole "
                "is graded at `the_tabulation_population` under `the_named_documents_derivation`."
            ),
            "the_occurrences": occurrences,
            "the_distinct_names": distinct_names,
            "the_reach_stated": (
                "A document named without a `.md` suffix, or referred to by description rather "
                "than by file name, is not found by this pattern; the list is a LOWER BOUND on "
                "the documents the six sections name (D-673).  A name that does not resolve at "
                "the path as written is RECORDED as not resolving, never guessed at another path "
                "and never dropped (#12)."
            ),
        },
        "item_3_the_term_search": {
            "the_terms_read_from": "L3_KEYWORDS in this file -- the one home of the 26 terms ruled "
                                   "on 2026-10-18 (§2 of the keyword-list record)",
            "the_terms": list(L3_KEYWORDS),
            "the_three_excluded_by_the_ruling_and_never_searched": list(THE_THREE_EXCLUDED),
            "one_tier": "every one of the 26 terms is ruled; one hit admits a line",
            "the_classes_searched": SEARCH_CLASSES,
            "class_membership_read_from": (
                "gen_l0_l1_outgoing_population.load_classes() -- never a directory listing"
            ),
            "the_cut": (
                "path equality, exact, against load_specification_document_set() -- the ruled "
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
                "the_three_terms_kept_with_no_hit_at_the_count_named_by_their_hits_here": {
                    term: hits_per_term.get(term)
                    for term in THE_THREE_KEPT_WITH_NO_HIT_AT_THE_COUNT
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
            "the_identities_read_from": "tools/audit/l3_withheld_documents.json -> in_entries "
                                        "(the set the user confirmed on 2026-10-15)",
            "the_homes_read_from": "gen_l2_withheld_documents.read_backbone() over "
                                   "tools/audit/decisions/backbone_decisions.json",
            "the_home_shape": HOME_SHAPE.pattern,
            "★_the_reconciliation_taken_in_both_directions": (
                "The 22 grouped by the document part of their homes equal l3_withheld_documents"
                ".json -> documents exactly, document by document and identity by identity.  A "
                "failure is a STOP, so this sentence records a check that passed."
            ),
            "where_it_falls_rule": (
                "the first that applies, in this order: `inside item 1: <opening heading>` (the "
                "home span lies wholly inside one of the six spans); `in an item-2 document that "
                "resolves: <path>` (the home's document equals, after path normalization, an "
                "item-2 name that resolves); `in a specification-set member, <n> of its lines "
                "being item-3 hit lines`; `reached by item 4 alone`"
            ),
            "the_passages": passages,
        },
        "the_transfer_input": {
            "★_what_this_is": (
                "The 2026-10-17 record's reading (its §2, 'Read by this side, not ruled') that the "
                "rows the L0/L1 and L2 comparisons RELOCATED to L3 enter as the transfer input "
                "(phase definition §3.4).  Each §10 span is located and measured; NO ROW IS PARSED."
            ),
            "the_spans": transfer,
        },
        "the_named_documents_derivation": THE_NAMED_DOCUMENTS_DERIVATION,
        "the_tabulation_population": {
            "★_what_this_is": (
                "The outgoing population cut into the MEMBERS the comparison tabulates, in the "
                "order it tabulates them, under the rulings of 2026-10-17 (Option B) and 2026-10-18 "
                "(Option B), the named-documents derivation and the passage rule below.  Every "
                "item-3 hit line of every specification-set member lies in exactly one member, and "
                "every one of the 22 item-4 homes lies wholly in exactly one member; either failing "
                "is a STOP, so this sentence records checks that passed.  It takes no disposition "
                "and grades nothing."
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
    except (Stop, l0l1.Stop, l2pop.Stop, withheld.Stop) as stop:
        print("STOP: %s" % stop)
        return 2
    rendered = json.dumps(derived, indent=1, ensure_ascii=False) + "\n"
    if check:
        if not os.path.isfile(OUT):
            print("STALE vs the derivation: l3_outgoing_population.json does not exist")
            return 1
        with open(OUT, "r", encoding="utf-8") as handle:
            if handle.read() != rendered:
                print("STALE vs the derivation: l3_outgoing_population.json does not re-derive")
                return 1
        print("l3_outgoing_population.json re-derives")
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
          "(ARCHITECTURE.md inside the six spans: %s, outside: %s); residue files: %d"
          % (i3["in_set_files_with_a_hit"], i3["total_hit_lines_distinct_over_them"],
             i3["of_which_ARCHITECTURE_md_inside_the_six_spans"],
             i3["of_which_ARCHITECTURE_md_outside_the_six_spans"], i3["residue_files"]))
    for kind, n in size["item_4_passages_by_where_it_falls"].items():
        print("item 4: %s — %d" % (kind, n))
    for path, n in size["the_transfer_spans_lines"].items():
        print("transfer span: %s — %d lines" % (path, n))
    tp = size["the_tabulation_population"]
    print("tabulation population: %d members, %d lines, %d bytes"
          % (tp["members"], tp["lines_total"], tp["bytes_total"]))
    print("wrote %s" % OUT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
