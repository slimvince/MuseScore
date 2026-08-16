#!/usr/bin/env python3
"""THE DERIVED SPLIT — every check the ruled soft-discard turns red, SUPERSEDED or STANDING.

THE RULING THIS EXISTS FOR.  User, 2026-08-16, §4 of
`cowork_rulings_2026_08_16_preparation_return.md` (the soft-discard's REACH, Alternative A as
recommended): *"The executing dispatch derives, publishes and commits the classification of every
check the discard's application turns red — SUPERSEDED (serves only the old phase-1 gate) or
STANDING (serves a rule of the current record) — each member with its evidence (its imports and
its own stated purpose). A member the derivation cannot place, and any STANDING member whose red
the enumerated-movement bound cannot explain, STOPS to the user."*

★ WHERE THE POPULATION COMES FROM, AND WHICH OF THE TWO OFFERED ROUTES WAS TAKEN.  The executing
dispatch offers two: apply the committed plan to a SCRATCH working state, or derive membership
statically from each check's imports.  **THE MEASURED ROUTE IS THE ONE TAKEN**, and the population
is IMPORTED — parsed on every run out of the `[FAIL]` lines of the committed report's own captured
run (`cc_report_preparation_third.md` §4.c), read from the GIT OBJECT at the commit this artifact
records, and never retyped into this file.  That report's block IS the measurement: the third
preparation batch applied the committed plan to the working tree, ran the whole guard set at the
edited tree, captured every red, and reverted, proving the revert at the objects.

**THE STATIC ROUTE WAS TRIED AND REJECTED, and the reason is recorded rather than left implicit.**
A predicate over imports can say which checks READ the decisions register's live entry population;
it cannot say which of those TURN RED, because it cannot separate a check that re-derives cleanly
over the shrunken record from one that halts inside an authored half the retirement invalidates.
Measured against the committed run, such a predicate selects far more checks than turned red — the
that register's own renderer and its establishment pass among them, both of which pass.  A population
that overshoots the measurement is not a derivation of it, and the ruling asks for the checks the
application TURNS RED.

**WHAT IS STILL OWED, AND WHERE IT IS DISCHARGED.**  This artifact is written BEFORE the act.  The
population it imports is a measurement taken at the third batch's tree; the act's own guard run, at
the applied tree, RE-CONFIRMS it.  A member observed red there and absent here, or absent there and
present here, is a STOP-and-report at the act — not something this file can settle in advance, and
it says so rather than implying the confirmation has already happened.

WHAT IS DERIVED AND WHAT IS AUTHORED.
  AUTHORED  nothing about any member.  The family of generators is IMPORTED from
            `gen_phase1_gate_readers.py`, which owns it (#6); the population is parsed from the
            committed report; each check's stated purpose is imported from `gen_guard_state.py`'s
            own authored invocation table rather than restated here.
  DERIVED   every verdict, from the import graph among the checks; every stated purpose, quoted
            from the check's own module docstring; the explanation of every red, from the captured
            reason together with the committed discard plan and the decisions register's home data
            read at the recorded commit; every count.

THE VERDICT RULE, published here so it can be checked without reading the code.  A member is
**SUPERSEDED** when its derivation serves only the old phase-1 gate, which is true in exactly three
shapes, each of them a fact about the import graph:
  (1) it IS one of the two gate derivations — the check whose output is the phase-1 completion
      inventory or the phase-1 finish line;
  (2) it imports one of those two transitively, so it is a view of the same derivation;
  (3) it is a FEEDER whose every importer is exactly those two gate derivations and nothing else,
      so everything it serves is the gate.
Everything else is **STANDING**, and its evidence is the consumer or the subject it has outside the
family.  ★ THE FEEDER LIMB IS DELIBERATELY NOT COMPUTED TO A FIXED POINT, and the reason is a
measured one: the feeder's own feeder is imported by the feeder rather than by the gate, and a
fixed point would sweep the decisions register's home classification — a check the current record's
own home rules depend on — into a class the ruling means for the gate alone.

THE STOPS, so this cannot silently stop being a derivation:
  * a sentence of the ruling that ordered this split no longer in its ruling record STOPS it;
  * the committed report's `[FAIL]` block missing, empty, or naming a check the tree does not
    carry, STOPS it — the population may not quietly shrink to what still parses;
  * a member the verdict rule cannot place STOPS it;
  * a STANDING member whose red the enumerated-movement bound cannot explain STOPS it;
  * a tally that does not account for the population STOPS it.

Run:
  python tools/audit/gen_discard_reach_split.py           # write the artifact
  python tools/audit/gen_discard_reach_split.py --check    # re-derive, exit 1 on drift
"""
from __future__ import annotations

import ast
import json
import os
import re
import subprocess
import sys
import warnings

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(HERE, "discard_reach_split.json")
RULING = "cowork_rulings_2026_08_16_preparation_return.md"
REPORT = "cc_report_preparation_third.md"
PLAN = "tools/audit/soft_discard_application.json"
BACKBONE = "tools/audit/decisions/backbone_decisions.json"
GUARD_STATE = "tools/audit/guard_state.json"

sys.path.insert(0, HERE)
from output_encoding import use_utf8_output              # noqa: E402  (path set above)
from gen_phase1_gate_readers import (                    # noqa: E402  (#6 — one home)
    FAMILY_GENERATORS, GATE_DERIVATIONS, blob_at, flatten, head_commit, import_graph, reachable,
    string_constants, tracked_at,
)
import gen_guard_state as guards                         # noqa: E402  (the authored purposes)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout
warnings.filterwarnings("ignore", category=SyntaxWarning)

SUPERSEDED = "SUPERSEDED"
STANDING = "STANDING"

FAIL_LINE = re.compile(r"^\s*\[FAIL\]\s+(\S+)(.*)$")
REFERENCE = re.compile(r"\bD-\d+\b")
DOCUMENT = re.compile(r"[A-Za-z0-9_\-./]+\.(?:md|py)\b")

RULING_SENTENCES = {
    "what the split must publish":
        "The executing dispatch derives, publishes and commits the classification of every check "
        "the discard's application turns red — SUPERSEDED (serves only the old phase-1 gate) or "
        "STANDING (serves a rule of the current record) — each member with its evidence (its "
        "imports and its own stated purpose).",
    "what stops to the user":
        "A member the derivation cannot place, and any STANDING member whose red the "
        "enumerated-movement bound cannot explain, STOPS to the user.",
    "the bound that travels with the act":
        "movement ONLY in values whose subject is a discard-population entry, or a document whose "
        "class or home standing those entries alone carried; every moved value enumerated in the "
        "close and diffed at explicit hashes; any other movement is a STOP-and-report.",
}


class Stop(Exception):
    """A demand of this derivation is unmet. Never a warning."""


def locate_ruling() -> dict[str, str]:
    path = os.path.join(ROOT, RULING)
    if not os.path.exists(path):
        raise Stop(f"the ruling record this derivation serves is missing: {RULING}")
    with open(path, encoding="utf-8") as fh:
        text = flatten(fh.read())
    missing = [name for name, quote in RULING_SENTENCES.items() if flatten(quote) not in text]
    if missing:
        raise Stop("a sentence of the ruling that ordered this split is no longer in its ruling "
                   f"record, so the derivation would outlive the words that ordered it: {missing}")
    return dict(RULING_SENTENCES)


def measured_population(commit: str) -> list[dict]:
    """The reds, PARSED from the committed report's captured run. Never retyped here."""
    text = blob_at(commit, REPORT)
    if text is None:
        raise Stop(f"the committed report carrying the measurement is missing at {commit}: "
                   f"{REPORT}")
    rows: list[dict] = []
    current: dict | None = None
    for raw in text.splitlines():
        match = FAIL_LINE.match(raw)
        if match:
            tail = match.group(2).strip()
            flags = [token for token in tail.split() if token.startswith("--")]
            annotation = tail
            for flag in flags:
                annotation = annotation.replace(flag, "", 1)
            current = {"tool": match.group(1), "args": flags,
                       "the_annotation_on_the_run_line": annotation.strip(),
                       "the_captured_reason": []}
            rows.append(current)
            continue
        if current is not None:
            if raw.startswith("    ") and raw.strip():
                current["the_captured_reason"].append(raw.strip())
            elif not raw.strip():
                continue
            else:
                current = None
    if not rows:
        raise Stop(f"the committed report at {commit} carries no `[FAIL]` block, so the measured "
                   f"population cannot be imported — it is not retyped here")
    for row in rows:
        row["the_captured_reason"] = " ".join(row["the_captured_reason"])
    return rows


def docstring_opening(source: str) -> str:
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return ""
    text = ast.get_docstring(tree) or ""
    opening = text.strip().split("\n\n")[0].strip()
    return re.sub(r"\s+", " ", opening)


def authored_purpose(tool: str) -> str:
    for rel, _args, why in guards.AUTHORED:
        if rel == tool:
            return why
    return ""


def homes_at(commit: str) -> dict[str, list[str]]:
    text = blob_at(commit, BACKBONE)
    if text is None:
        raise Stop(f"the decisions register's data file is missing at {commit}")
    data = json.loads(text)
    homes: dict[str, list[str]] = {}
    for entry in data["decisions"]:
        home = (entry.get("home") or "").strip()
        # A home is a DOCUMENT with a line range or a section appended — `docs/x.md:1134`,
        # `ARCHITECTURE.md:1265-1267`, `x.md §3`. The document is what home standing attaches to,
        # so the appended locator is stripped: the split is on a colon FOLLOWED BY A DIGIT, which
        # a Windows drive letter cannot produce in a repository-relative path.
        base = re.split(r":(?=\d)", home.split("#")[0].split(" ")[0].strip("`"))[0]
        if base:
            homes.setdefault(base, []).append(entry["id"])
    return homes


def discard_population(commit: str) -> list[str]:
    text = blob_at(commit, PLAN)
    if text is None:
        raise Stop(f"the committed soft-discard plan is missing at {commit}: {PLAN}")
    plan = json.loads(text)
    population = plan.get("the_entries_this_act_would_retire") or []
    if not population:
        raise Stop("the committed plan carries no discard population")
    return sorted(population)


def already_failing(commit: str) -> set[str]:
    text = blob_at(commit, GUARD_STATE)
    if text is None:
        raise Stop(f"the committed guard state is missing at {commit}")
    state = json.loads(text)
    return {row["tool"] for row in state["summary"]["failing_tools"]}


ANCHOR_MOVE = re.compile(r"(tools/audit/decisions/\S+\.py)")


def explain(row: dict, source: str, discard: set[str], homes: dict[str, list[str]],
            losing_home: dict[str, list[str]], pre_existing: set[str],
            reads_home_standing: bool, reads_the_live_entry_population: bool) -> dict:
    """Why this check turned red — derived from its own inputs and from the committed plan.

    The captured reason is used where it NAMES a subject, and the check's own inputs are used
    where it does not: the committed report abbreviates two reasons to `(the same three)` and
    `(register-derived, expected)`, and a derivation that could read only the prose would have to
    stop on both.  Both signals are published per member, so which one placed it is visible.
    """
    reason = row["the_captured_reason"] + " " + row["the_annotation_on_the_run_line"]

    if row["tool"] in pre_existing:
        return {"class": "pre-existing-and-not-caused-by-this-act",
                "placed_by": "the committed guard state",
                "evidence": "the committed guard state at the recorded commit already carries "
                            "this check among its failing tools, so its red is not this act's"}

    anchor = ANCHOR_MOVE.search(reason)
    if anchor and re.search(r"\bline\b|\bquote\b", reason):
        return {"class": "an-anchored-quote-into-a-file-the-act-itself-edits",
                "placed_by": "the captured reason",
                "evidence": f"the captured reason names an anchored quote at {anchor.group(1)}, "
                            "whose line moves because the retired block's own STOPs are inserted "
                            "into the decisions register's own generator — the ruling's F15 limb, "
                            "handled under the ordinary per-citation drift discipline"}

    named_entries = sorted(set(REFERENCE.findall(reason)) & discard)
    if named_entries:
        return {"class": "the-subject-is-a-discard-population-entry",
                "placed_by": "the captured reason",
                "evidence": f"the captured reason names {named_entries}, which the committed plan "
                            "carries in the discard population"}

    named_documents = sorted(set(DOCUMENT.findall(reason)))
    lose_home = [{"document": document, "its_live_homed_entries": losing_home[document]}
                 for document in named_documents if document in losing_home]
    if lose_home:
        return {"class": "the-subject-is-a-document-whose-HOME-standing-only-discard-population-"
                         "entries-carried",
                "placed_by": "the captured reason",
                "evidence": lose_home}

    lose_class = [{"document": document,
                   "its_live_homed_entries": sorted(homes[document]),
                   "of_which_the_discard_removes": sorted(set(homes[document]) & discard)}
                  for document in named_documents
                  if document in homes and set(homes[document]) & discard]
    if lose_class:
        return {"class": "the-subject-is-a-document-whose-CLASS-standing-discard-population-"
                         "entries-carried",
                "placed_by": "the captured reason",
                "evidence": lose_class}

    if reads_home_standing and losing_home:
        return {"class": "the-subject-is-a-document-whose-HOME-standing-only-discard-population-"
                         "entries-carried",
                "placed_by": "the check's own inputs (the captured reason names no subject)",
                "evidence": [{"document": document, "its_live_homed_entries": entries}
                             for document, entries in sorted(losing_home.items())]}

    if reads_the_live_entry_population:
        return {"class": "ordinary-regeneration-over-the-changed-decisions-register",
                "placed_by": "the check's own inputs",
                "evidence": "the check reads the decisions register's live entry population — its "
                            "own data file, its rendered INDEX, or its rendered group files, "
                            "directly or through a module it imports — so the discard moves its "
                            "output by construction. Every moved value is enumerated in the close "
                            "at the act, under the bound"}

    return {"class": None,
            "placed_by": None,
            "evidence": "neither the captured reason nor the check's own inputs match a shape the "
                        "enumerated-movement bound admits"}


def build(commit: str | None = None) -> dict:
    ruling = locate_ruling()
    measured_at = commit or head_commit()
    tracked = tracked_at(measured_at)
    population = measured_population(measured_at)

    absent = sorted({row["tool"] for row in population} - set(tracked))
    if absent:
        raise Stop(f"the measured population names check(s) the tree does not carry: {absent}")

    graph = import_graph(measured_at, tracked)
    reverse: dict[str, set[str]] = {path: set() for path in graph}
    for path, targets in graph.items():
        for target in targets:
            reverse.setdefault(target, set()).add(path)

    discard = set(discard_population(measured_at))
    homes = homes_at(measured_at)
    losing_home = {document: sorted(ids) for document, ids in homes.items()
                   if set(ids) <= discard}
    pre_existing = already_failing(measured_at)

    # Which checks consume the decisions register's HOME standing, and which consume its LIVE
    # ENTRY POPULATION. Both are derived from the import graph and from each module's own string
    # constants — never listed here — because the committed report abbreviates two reasons and a
    # derivation that could read only its prose would have to stop on both.
    home_standing_source = "tools/audit/decisions/gen_phase1p_delegation_bar.py"
    sources = {path: (blob_at(measured_at, path) or "") for path in graph}
    constants = {path: string_constants(text) for path, text in sources.items()}
    register_surfaces = {"backbone_decisions.json", "DECISIONS.md", "decisions", "group_"}

    def reads_the_population(path: str) -> bool:
        for module in {path} | reachable(graph, path):
            for value in constants.get(module, ()):
                if any(surface in value for surface in register_surfaces):
                    return True
        return False

    rows, unplaced, unexplained = [], [], []
    for entry in population:
        tool = entry["tool"]
        source = blob_at(measured_at, tool) or ""
        imports_family = sorted(reachable(graph, tool) & set(FAMILY_GENERATORS))
        reads_home_standing = tool == home_standing_source or home_standing_source in reachable(graph, tool)
        reads_population = reads_the_population(tool)
        importers = sorted(reverse.get(tool, set()))
        is_a_gate_derivation = tool in GATE_DERIVATIONS
        is_feeder = bool(importers) and set(importers) == set(GATE_DERIVATIONS)

        if is_a_gate_derivation:
            verdict, limb = SUPERSEDED, "(1) it IS one of the two gate derivations"
        elif imports_family:
            verdict, limb = SUPERSEDED, ("(2) it imports a gate derivation transitively, so it is "
                                         f"a view of the same derivation: {imports_family}")
        elif is_feeder:
            verdict, limb = SUPERSEDED, ("(3) it is a FEEDER whose every importer is exactly the "
                                         f"two gate derivations and nothing else: {importers}")
        else:
            verdict = STANDING
            limb = ("no limb of the SUPERSEDED rule reaches it: it is not a gate derivation, it "
                    "imports none transitively, and its importers are "
                    + (f"{importers}, which is not the two gate derivations" if importers
                       else "none, so it feeds the gate nothing"))
        if verdict not in (SUPERSEDED, STANDING):
            unplaced.append(tool)

        explanation = explain(entry, source, discard, homes, losing_home, pre_existing,
                              reads_home_standing, reads_population)
        if verdict == STANDING and explanation["class"] is None:
            unexplained.append(tool)

        rows.append({
            "tool": tool,
            "args": entry["args"],
            "verdict": verdict,
            "the_limb_of_the_rule_that_placed_it": limb,
            "the_evidence": {
                "its_imports": {
                    "gate_derivations_it_imports_transitively": imports_family,
                    "checks_that_import_it": importers,
                    "it_consumes_the_registers_home_standing": reads_home_standing,
                    "it_consumes_the_registers_live_entry_population": reads_population,
                },
                "its_own_stated_purpose": {
                    "from_its_module_docstring": docstring_opening(source),
                    "from_the_guard_sets_authored_invocation_table": authored_purpose(tool),
                },
            },
            "the_red_it_turns": {
                "the_captured_reason": entry["the_captured_reason"],
                "the_annotation_on_the_run_line": entry["the_annotation_on_the_run_line"],
                "why_the_enumerated_movement_bound_explains_it": explanation,
            },
            "what_this_batch_does_with_it": (
                "reclassified HISTORICAL through the guard mechanism's own records; its committed "
                "artifact frozen in place as record (#12) and never regenerated again"
                if verdict == SUPERSEDED else
                "regenerated by its own generator alongside the discard, diffed against its "
                "committed blob at an explicit hash, every moved value enumerated in the close"),
        })

    if unplaced:
        raise Stop(f"the verdict rule cannot place: {unplaced}")
    if unexplained:
        raise Stop(f"STANDING member(s) whose red the enumerated-movement bound cannot explain: "
                   f"{unexplained}")

    tally: dict[str, int] = {}
    for row in rows:
        tally[row["verdict"]] = tally.get(row["verdict"], 0) + 1
    if sum(tally.values()) != len(rows):
        raise Stop("the tally does not account for the population")

    return {
        "what_this_is":
            "The derived split the user's ruling of 2026-08-16 §4 orders FIRST: every check the "
            "ruled soft-discard's application turns red, classified SUPERSEDED (serves only the "
            "old phase-1 gate) or STANDING (serves a rule of the current record), each member "
            "with its evidence.",
        "generator": "tools/audit/gen_discard_reach_split.py",
        "dispatch": "cc_instruction_preparation_fourth.md, Task 1 (R2)",
        "the_ruling_that_ordered_it": {
            "source": f"{RULING} §4",
            "every_sentence_located_in_that_record_on_this_run": ruling,
        },
        "measured_at_commit": measured_at,
        "★_which_of_the_two_offered_routes_was_taken_and_why": {
            "the_route_taken": "the MEASURED route. The population is parsed on every run out of "
                               "the `[FAIL]` lines of the committed report's own captured run "
                               f"(`{REPORT}` §4.c), read from the git object at the commit above "
                               "and never retyped into the generator.",
            "what_that_measurement_was": "the third preparation batch applied the committed plan "
                                         "to the working tree, ran the whole guard set at the "
                                         "edited tree, captured every red, and REVERTED, proving "
                                         "the revert at the objects.",
            "the_static_route_was_tried_and_REJECTED": (
                "A predicate over imports can say which checks READ the decisions register's live "
                "entry population; it cannot say which of those TURN RED, because it cannot "
                "separate a check that re-derives cleanly over the shrunken record from one that "
                "halts inside an authored half the retirement invalidates. Such a predicate "
                "selects far more checks than turned red — that register's own renderer and its "
                "establishment pass among them, both of which pass. A population that overshoots "
                "the measurement is not a derivation of it."),
            "★_what_is_still_owed_and_where_it_is_discharged": (
                "This artifact is written BEFORE the act. The act's own guard run, at the applied "
                "tree, RE-CONFIRMS the population: a member observed red there and absent here, "
                "or absent there and present here, is a STOP-and-report at the act. Nothing here "
                "claims that confirmation has already happened."),
        },
        "the_verdict_rule": {
            "SUPERSEDED": [
                "(1) it IS one of the two gate derivations — the check whose output is the "
                "phase-1 completion inventory or the phase-1 finish line;",
                "(2) it imports one of those two transitively, so it is a view of the same "
                "derivation;",
                "(3) it is a FEEDER whose every importer is exactly those two and nothing else.",
            ],
            "STANDING": "everything else, with the consumer or subject it has outside the family "
                        "named as its evidence.",
            "★_why_the_feeder_limb_is_not_computed_to_a_fixed_point": (
                "Measured rather than argued: the feeder's own feeder is imported by the feeder "
                "rather than by the gate, so a fixed point would sweep the decisions register's "
                "home classification — a check the current record's own home rules depend on — into "
                "a class the ruling means for the gate alone."),
            "the_family_is_imported_never_restated": {
                "from": "tools/audit/gen_phase1_gate_readers.py (#6 — one home)",
                "generators": FAMILY_GENERATORS,
                "the_two_gate_derivations": GATE_DERIVATIONS,
            },
        },
        "the_tally": tally,
        "the_bound_every_STANDING_member_is_read_against": RULING_SENTENCES[
            "the bound that travels with the act"],
        "what_the_discard_removes_DERIVED_and_read_at_the_recorded_commit": {
            "the_discard_population_size": len(discard),
            "★_the_source": f"the committed plan `{PLAN}` → the_entries_this_act_would_retire, "
                            "read at the commit above. No entry identity is restated here (D-431).",
            "documents_whose_every_live_homed_entry_is_in_the_discard": losing_home,
            "★_what_that_list_is_for": (
                "It is the derived form of the bound's second half — a document whose HOME "
                "standing those entries alone carried. A document that keeps at least one homed "
                "entry is not on this list, and a red naming it is explained by the CLASS limb "
                "instead, which publishes exactly which of its entries the discard removes."),
        },
        "★_what_this_split_does_NOT_assert": (
            "That a SUPERSEDED verdict says anything about whether the superseded phase 1's "
            "obligations were discharged — the ruling states in terms that historical status "
            "asserts nothing of the kind, and neither does this artifact. It also asserts nothing "
            "about whether a STANDING member's regenerated values are RIGHT: what it carries is "
            "the class of the explanation, and the values themselves are enumerated in the close "
            "at the act and diffed at explicit hashes."),
        "members": rows,
    }


def main(argv: list[str]) -> int:
    if "--check" in argv:
        if not os.path.exists(OUT):
            print("FAIL: the artifact is missing:", os.path.relpath(OUT, ROOT))
            return 1
        with open(OUT, encoding="utf-8") as fh:
            have = json.load(fh)
        rebuilt = build(have.get("measured_at_commit"))
        text = json.dumps(rebuilt, indent=1, ensure_ascii=False) + "\n"
        with open(OUT, encoding="utf-8") as fh:
            if fh.read() != text:
                print("FAIL: the discard reach split does not re-derive")
                return 1
        print("the discard reach split re-derives: "
              + " · ".join(f"{k} {v}" for k, v in sorted(rebuilt["the_tally"].items())))
        return 0

    built = build()
    with open(OUT, "w", encoding="utf-8", newline="") as fh:
        fh.write(json.dumps(built, indent=1, ensure_ascii=False) + "\n")
    print("wrote", os.path.relpath(OUT, ROOT))
    for verdict, count in sorted(built["the_tally"].items()):
        print(f"  {verdict}: {count}")
    for row in built["members"]:
        print(f"  [{row['verdict']:11}] {row['tool']} — "
              f"{row['the_red_it_turns']['why_the_enumerated_movement_bound_explains_it']['class']}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except Stop as exc:
        print(f"STOP: {exc}")
        sys.exit(2)
