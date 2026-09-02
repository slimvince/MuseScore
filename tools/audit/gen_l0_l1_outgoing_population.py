#!/usr/bin/env python3
"""DERIVE THE OUTGOING POPULATION FOR THE L0/L1 COMPARISON.

WHY THIS EXISTS.  Ruling 32 (§3am of `cowork_rulings_2026_08_31_decision_surface_sitting.md`)
fixes the set of current-text passages the L0/L1 comparison covers.  It names eleven members
directly and then defines a fourth limb by a TERM SEARCH over three classes of the ruled artifact
inventory.  A population defined partly by a search cannot live in prose: the search has to be
run, its hits recorded per line, and its reach stated -- which is what this tool does.

WHAT IT DOES, AND NOTHING ELSE.

  1. LISTS THE NAMED MEMBERS verbatim from Ruling 32 (its items 1-3).  Each carries its path and,
     for the three `ARCHITECTURE.md` sections, the HEADING TEXT that bounds it.  Sections are
     located BY HEADING TEXT, never by line number (D-307): a line number quoted in a rule goes
     stale on the next insertion above it.  A named member missing at its path is a STOP.

  2. RUNS THE TERM SEARCH over every file of the three inventory classes named by the ruling,
     reading class membership from `tools/audit/artifact_inventory.json` -> each class's
     `every_member` -- never from a directory listing, so the population is the ruled one rather
     than whatever the file system happens to hold.  Case-insensitive, two tiers:

       ADMITTING  one hit admits the file to the population.
       RECORDED   single words too common to admit a file on their own, recorded per hit so the
                  reach statement can say what they would have added.

     THE TWO TIERS AND THE RULE BETWEEN THEM ARE AUTHORED.  That is stated on the artifact
     itself, not only here.

  3. STATES ITS REACH (D-673).  The term list is authored, so a passage about L0's or L1's
     subject that uses none of these words is NOT found.  The artifact says so in
     `the_reach_stated`, and publishes the hit population as a LOWER BOUND on the outgoing text,
     never as a census -- the recognizer clause of the dispatch protocol, which applies because
     nothing else independently enumerates "passages about L0's or L1's subject".

  4. COUNTS -- files searched per class, files with hits, hits per file, hits per term -- AT THE
     ARTIFACT.  No figure is restated in the dispatch or in the report (D-431).

  5. ORDERS THE POPULATION: the eleven named members first, in the ruling's own order, then the
     hit files by descending hit count (ties broken by path, so the order is deterministic).
     That order is the comparison's batch order.

WHAT IT DOES NOT DO.  It takes no disposition, grades nothing, compares nothing, and edits no
outgoing text.  It reports a population and its reach.

Run:
    python tools/audit/gen_l0_l1_outgoing_population.py           # write the artifact
    python tools/audit/gen_l0_l1_outgoing_population.py --check   # re-derive, exit 1 on drift
"""
from __future__ import annotations

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(HERE, "l0_l1_outgoing_population.json")
INVENTORY = os.path.join(HERE, "artifact_inventory.json")

sys.path.insert(0, HERE)
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()


class Stop(Exception):
    """A named member is not at its path, or a class is not in the inventory. Never a warning."""


# --------------------------------------------------------------------------------------------
# (1) THE NAMED MEMBERS -- Ruling 32 items 1-3, in the ruling's own order.
#
# `section` is a heading-to-heading span located by TEXT.  `opens_at` is matched as the start of
# a line; `closes_before` is a regular expression matched as the start of a later line.
# --------------------------------------------------------------------------------------------
NAMED_MEMBERS = [
    {
        "ruling_item": 1,
        "path": "ARCHITECTURE.md",
        "member": "the current Layer 1 section",
        "section": {
            "opens_at": "#### Layer 1 — the lossless note model",
            "closes_before_pattern": r"^#### ",
        },
    },
    {
        "ruling_item": 1,
        "path": "ARCHITECTURE.md",
        "member": "the current Layer 2 section",
        "section": {
            "opens_at": "#### Layer 2 — the deterministic change-point slicer",
            "closes_before_pattern": r"^#### ",
        },
    },
    {
        "ruling_item": 2,
        "path": "cowork_layer1_note_model_design.md",
        "member": "a root design document the Layer 1 and Layer 2 sections delegate to or cite",
        "section": None,
    },
    {
        "ruling_item": 2,
        "path": "cowork_layer1_tone_collection_design.md",
        "member": "a root design document the Layer 1 and Layer 2 sections delegate to or cite",
        "section": None,
    },
    {
        "ruling_item": 2,
        "path": "cowork_layer1_extend_design.md",
        "member": "a root design document the Layer 1 and Layer 2 sections delegate to or cite",
        "section": None,
    },
    {
        "ruling_item": 2,
        "path": "cowork_layer2_slicing_design.md",
        "member": "a root design document the Layer 1 and Layer 2 sections delegate to or cite",
        "section": None,
    },
    {
        "ruling_item": 2,
        "path": "cowork_layer2_reslice_design.md",
        "member": "a root design document the Layer 1 and Layer 2 sections delegate to or cite",
        "section": None,
    },
    {
        "ruling_item": 3,
        "path": "ARCHITECTURE.md",
        "member": (
            "the current Layer 5 section — the cadence detector sentence and the two "
            "design-only obligations naming fermatas, rests and bar lines"
        ),
        "section": {
            "opens_at": "#### Layer 5 — the function/cadence layer",
            "closes_before_pattern": r"^#### ",
        },
    },
    {
        "ruling_item": 3,
        "path": "cowork_layer5_function_design.md",
        "member": "the contract the Layer 5 cadence-detector sentence delegates to",
        "section": None,
    },
    {
        "ruling_item": 3,
        "path": "cowork_phrase_boundary_design.md",
        "member": "the document carrying fermatas, rests and bar lines as boundary evidence",
        "section": None,
    },
    {
        "ruling_item": 3,
        "path": "cowork_joint_estimator_factorization.md",
        "member": (
            "the factor list, items 7-9 — the beat-strength class, the fermata prior and the "
            "cadence factor"
        ),
        "section": None,
    },
]

# --------------------------------------------------------------------------------------------
# (2) THE TERM SEARCH -- Ruling 32 item 4, as the dispatch fixes the two tiers.
# --------------------------------------------------------------------------------------------
ADMITTING_TERMS = [
    "change point", "change-point", "sounding set", "eligible note", "grace note",
    "tied note", "tie continuation", "metric strength", "metrical strength", "beat strength",
    "fermata", "bar line", "barline", "double bar", "repeat sign", "cadence cue",
    "leading tone", "leading-tone", "anacrusis", "time signature", "key signature",
    "voice membership", "pedal mark", "spelled pitch", "notated record", "MusicXML", ".mscx",
]

RECORDED_TERMS = ["slice", "release", "eligible", "grace", "tie", "tied", "repeat"]

SEARCH_CLASSES = [
    "writing-side-design-documents",
    "governing-documents",
    "documentation-directory-prose",
]

THE_TIERS_ARE_AUTHORED = (
    "THE TWO TIERS AND THE RULE BETWEEN THEM ARE AUTHORED.  Ruling 32's item 4 names the L1 "
    "charter's vocabulary and L0's list of given facts; it does not partition that vocabulary "
    "into a tier that admits a file and a tier that does not.  This tool's dispatch "
    "(`cc_instruction_comparison_l0_l1_2026_09_02.md`) fixes the partition, and it is authored "
    "rather than derived: an ADMITTING term is a phrase specific enough that one hit makes a "
    "file worth reading for this subject, and a RECORDED term is a single word so common in this "
    "repository's prose that admitting on it would admit nearly every file and say nothing.  "
    "RECORDED hits are counted and published so that a reader can see exactly what the other "
    "rule would have added."
)


def read_text(rel_path):
    """Read one repository file. A missing named member is a STOP, never a skip."""
    abs_path = os.path.join(ROOT, rel_path)
    if not os.path.isfile(abs_path):
        raise Stop("named member missing at its path: %s" % rel_path)
    with open(abs_path, "r", encoding="utf-8", errors="replace") as handle:
        return handle.read()


def locate_section(text, rel_path, opens_at, closes_before_pattern):
    """Locate a heading-to-heading span BY TEXT (D-307). Returns the bounding facts."""
    lines = text.split("\n")
    start = None
    for index, line in enumerate(lines):
        if line.startswith(opens_at):
            start = index
            break
    if start is None:
        raise Stop("heading not found in %s: %s" % (rel_path, opens_at))
    closer = re.compile(closes_before_pattern)
    end = len(lines)
    closing_heading = None
    for index in range(start + 1, len(lines)):
        if closer.match(lines[index]):
            end = index
            closing_heading = lines[index]
            break
    return {
        "located_by": "heading text, never a line number (D-307)",
        "opens_at": opens_at,
        "opening_heading_as_found": lines[start],
        "closes_before_pattern": closes_before_pattern,
        "closing_heading_as_found": closing_heading,
        "lines_in_the_span": end - start,
        "first_line_number_as_a_locator_only": start + 1,
    }


def load_classes():
    """Class membership from the ruled inventory -- never from a directory listing."""
    with open(INVENTORY, "r", encoding="utf-8") as handle:
        inventory = json.load(handle)
    blocks = inventory.get("classes") if isinstance(inventory, dict) else None
    if blocks is None:
        for value in (inventory.values() if isinstance(inventory, dict) else []):
            if isinstance(value, list) and value and isinstance(value[0], dict) \
                    and "class" in value[0]:
                blocks = value
                break
    if blocks is None:
        raise Stop("the artifact inventory does not carry a list of class blocks")
    by_name = {}
    for block in blocks:
        name = block.get("class")
        if name in SEARCH_CLASSES:
            members = block.get("every_member")
            if members is None:
                raise Stop("class %s carries no every_member list" % name)
            by_name[name] = [entry["path"] for entry in members]
    missing = [name for name in SEARCH_CLASSES if name not in by_name]
    if missing:
        raise Stop("class(es) not in the inventory: %s" % ", ".join(missing))
    return by_name


def search_terms(text, terms, tier):
    """Case-insensitive hits, one record per matched line per term."""
    hits = []
    lines = text.split("\n")
    lowered_terms = [(term, term.lower()) for term in terms]
    for index, line in enumerate(lines):
        low = line.lower()
        for term, low_term in lowered_terms:
            if low_term in low:
                hits.append({
                    "line_number": index + 1,
                    "term": term,
                    "tier": tier,
                    "line": line.strip(),
                })
    return hits


def derive():
    named = []
    for entry in NAMED_MEMBERS:
        text = read_text(entry["path"])          # STOPs if absent
        record = {
            "ruling_item": entry["ruling_item"],
            "path": entry["path"],
            "what_it_is": entry["member"],
            "present_at_its_path": True,
        }
        if entry["section"]:
            record["section"] = locate_section(
                text, entry["path"],
                entry["section"]["opens_at"],
                entry["section"]["closes_before_pattern"],
            )
        else:
            record["section"] = None
            record["whole_document"] = True
        named.append(record)

    classes = load_classes()
    named_paths = {entry["path"] for entry in NAMED_MEMBERS}

    per_file = {}
    per_class_counts = {}
    hits_per_term = {}
    for class_name in SEARCH_CLASSES:
        paths = classes[class_name]
        with_hits = 0
        for rel_path in paths:
            abs_path = os.path.join(ROOT, rel_path)
            if not os.path.isfile(abs_path):
                # A class member the tree no longer has is recorded, never silently dropped.
                per_file.setdefault(rel_path, {
                    "path": rel_path,
                    "inventory_class": class_name,
                    "absent_from_the_tree": True,
                    "admitting_hits": [],
                    "recorded_hits": [],
                })
                continue
            with open(abs_path, "r", encoding="utf-8", errors="replace") as handle:
                text = handle.read()
            admitting = search_terms(text, ADMITTING_TERMS, "admitting")
            recorded = search_terms(text, RECORDED_TERMS, "recorded")
            for hit in admitting + recorded:
                hits_per_term[hit["term"]] = hits_per_term.get(hit["term"], 0) + 1
            if admitting or recorded:
                per_file[rel_path] = {
                    "path": rel_path,
                    "inventory_class": class_name,
                    "is_a_named_member": rel_path in named_paths,
                    "admitting_hit_count": len(admitting),
                    "recorded_hit_count": len(recorded),
                    "admitting_hits": admitting,
                    "recorded_hits": recorded,
                }
            if admitting:
                with_hits += 1
        per_class_counts[class_name] = {
            "files_searched": len(paths),
            "files_with_at_least_one_admitting_hit": with_hits,
        }

    # The population as DOCUMENTS: every named member, plus every file with an admitting hit.
    admitted = [
        record for record in per_file.values()
        if record.get("admitting_hit_count", 0) > 0
    ]
    admitted_outside_named = [r for r in admitted if not r.get("is_a_named_member")]
    admitted_outside_named.sort(key=lambda r: (-r["admitting_hit_count"], r["path"]))

    order = []
    seen = []
    for entry in named:
        label = entry["path"] if entry["section"] is None else \
            "%s :: %s" % (entry["path"], entry["section"]["opens_at"])
        order.append({
            "position": len(order) + 1,
            "path": entry["path"],
            "section": entry["section"]["opens_at"] if entry["section"] else None,
            "why_in_the_population": "named by Ruling 32 item %d" % entry["ruling_item"],
            "admitting_hit_count": per_file.get(entry["path"], {}).get("admitting_hit_count"),
        })
        seen.append(label)
    for record in admitted_outside_named:
        order.append({
            "position": len(order) + 1,
            "path": record["path"],
            "section": None,
            "why_in_the_population": "a term-search hit under Ruling 32 item 4",
            "admitting_hit_count": record["admitting_hit_count"],
        })

    size_stop = {
        "the_threshold": 40,
        "what_it_is": (
            "A stop threshold for THIS BATCH, ruled in its dispatch so the decision is not the "
            "executing session's.  It is NOT a figure about the corpus and states nothing about "
            "how large the outgoing text is."
        ),
        "hit_files_outside_the_named_members": len(admitted_outside_named),
        "the_stop_is_reached": len(admitted_outside_named) > 40,
    }

    return {
        "★_what_this_artifact_is": (
            "The outgoing population for the L0/L1 comparison, derived under Ruling 32 of "
            "`cowork_rulings_2026_08_31_decision_surface_sitting.md`.  It fixes WHICH "
            "current-text documents the comparison covers and in WHAT ORDER they are worked.  "
            "It takes no disposition and grades nothing."
        ),
        "★_what_it_does_not_do": (
            "It does not compare, dispose, adopt, relocate, quarantine, discard or grade "
            "anything, and it edits no outgoing text.  It reports a population and its reach."
        ),
        "the_ruling": "§3am (Ruling 32) of cowork_rulings_2026_08_31_decision_surface_sitting.md",
        "the_named_members": named,
        "the_term_search": {
            "the_classes_searched": SEARCH_CLASSES,
            "class_membership_read_from": (
                "tools/audit/artifact_inventory.json -> each class's every_member — never a "
                "directory listing"
            ),
            "case_sensitivity": "case-insensitive",
            "admitting_terms": ADMITTING_TERMS,
            "recorded_terms": RECORDED_TERMS,
            "★_the_two_tiers_are_authored": THE_TIERS_ARE_AUTHORED,
            "counts": {
                "per_class": per_class_counts,
                "hits_per_term": dict(sorted(hits_per_term.items(),
                                             key=lambda kv: (-kv[1], kv[0]))),
                "files_with_at_least_one_admitting_hit": len(admitted),
                "of_those_already_named_by_the_ruling": len(admitted) - len(admitted_outside_named),
                "hit_files_outside_the_named_members": len(admitted_outside_named),
            },
            "per_file": dict(sorted(per_file.items())),
        },
        "the_reach_stated": {
            "★_this_is_a_LOWER_BOUND_and_not_a_census": (
                "The term list is AUTHORED.  A passage about L0's or L1's subject that uses none "
                "of these words is NOT found by this search, and this artifact does not know how "
                "many such passages exist.  The hit population is therefore published as a LOWER "
                "BOUND on the outgoing text, never as a census (D-673, and the recognizer clause "
                "of the dispatch protocol)."
            ),
            "is_there_an_independently_known_population_to_reconcile_against": (
                "NO.  Nothing other than this search enumerates 'passages of the current text "
                "about L0's or L1's subject', so no seed set can establish it and no both-ways "
                "reconciliation is available.  Its reach is therefore declared UNMEASURED."
            ),
            "the_reach_against_the_text_it_scans": "UNMEASURED",
            "what_bounds_the_exposure": (
                "The eleven NAMED members are in the population by name regardless of the "
                "search, and they are the territory the ruling identified by reading rather "
                "than by pattern.  The search widens that territory; it does not define it."
            ),
            "what_the_recorded_tier_would_have_added": (
                "The RECORDED terms are counted per hit at `per_file`, so the effect of "
                "admitting on them is readable from this artifact rather than argued."
            ),
        },
        "the_population_in_comparison_order": order,
        "the_size_stop": size_stop,
    }


def main():
    check = "--check" in sys.argv[1:]
    try:
        derived = derive()
    except Stop as stop:
        print("STOP: %s" % stop)
        return 2
    rendered = json.dumps(derived, indent=1, ensure_ascii=False) + "\n"
    if check:
        if not os.path.isfile(OUT):
            print("STALE vs the derivation: l0_l1_outgoing_population.json does not exist")
            return 1
        with open(OUT, "r", encoding="utf-8") as handle:
            if handle.read() != rendered:
                print("STALE vs the derivation: l0_l1_outgoing_population.json does not re-derive")
                return 1
        print("l0_l1_outgoing_population.json re-derives")
        return 0
    with open(OUT, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(rendered)
    counts = derived["the_term_search"]["counts"]
    print("named members: %d" % len(derived["the_named_members"]))
    print("files with an admitting hit: %d (outside the named members: %d)" % (
        counts["files_with_at_least_one_admitting_hit"],
        counts["hit_files_outside_the_named_members"]))
    print("population in comparison order: %d entries" % len(derived["the_population_in_comparison_order"]))
    print("size stop reached: %s (threshold %d)" % (
        derived["the_size_stop"]["the_stop_is_reached"], derived["the_size_stop"]["the_threshold"]))
    print("wrote %s" % OUT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
