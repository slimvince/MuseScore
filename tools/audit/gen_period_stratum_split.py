#!/usr/bin/env python3
"""THE PERIOD SPLIT, RE-DERIVED BY A CHECKED TOOL — and the screen population published whole.

Dispatch: `cc_instruction_period_checks.md`, Task 1 (Cowork, 2026-08-15), executing the second
ruling of `cowork_rulings_2026_08_15_period_start.md`.

WHY IT EXISTS.  The restructuring period was ruled to open EXCLUSIVE at one commit.  The
per-stratum split the ruling was taken against was derived by an ad-hoc script over staged
snapshots — declared on the decision surface as assumption A1, with the check it owes stated in the
same sentence: *re-derivation by a checked tool before any act rests on the split*.  This is that
tool.  Its output SUPERSEDES the ad-hoc values wherever the two differ; the ad-hoc ones carry no
authority and are graded here as a registered expectation, never reconciled towards.

WHAT IS DERIVED AND WHAT IS AUTHORED, stated because the difference is the whole value:

  DERIVED  — every count, every population and the whole screen enumeration, from the two candidate
             artifacts alone: the hunk file's per-hunk `role`, `v` and commit index, and the main
             artifact's `commits` table with the stratum it assigns each commit.  Nothing is read
             from git here, and nothing is read from any account of what the split was.
  AUTHORED — the ruled start commit (taken at the ruling record, cited beside it); which document
             roles count as SPECIFICATION-BEARING (taken at the decision surface and at the
             dispatch, cited beside it); and the registered expectation this tool grades.

THE CUT, and why it is not the stratum field alone.  The ruling opens the period EXCLUSIVE at
`b006dc15b5`, so that commit is OUTSIDE the period it opens.  The candidate artifact's stratum
field puts that commit INSIDE its own stratum S4, because a stratum boundary is inclusive of the
act that opens it.  The two are not the same population, and the difference is not empty: the
boundary commit's own hunks are out-of-period under the ruling while carrying the S4 label.  So the
cut is published BOTH ways — the ruled one, which governs, and the stratum one, which the artifact
speaks in — and the difference between them is enumerated rather than left for a reader to notice.

THE SCREEN POPULATION is the OUT-OF-PERIOD specification-bearing flagged hunks: the pre-S4 strata
PLUS whatever the boundary commit itself contributes.  The dispatch names the pre-S4 slice; taking
the ruled cut instead can only ADD members, never drop one, and under-screening is the direction
that costs the objective.  Both slices are published, and which hunks the wider one adds is named.

THE STOPS, so this cannot silently stop being a derivation:
  1. the ruled start commit must be present in the `commits` table — absent, it STOPS;
  2. every hunk record must carry every field the derivation needs — one missing STOPS the tool,
     and no record is ever skipped (assumption A1's own check);
  3. every commit index and file index must resolve into its table — one that does not STOPS it;
  4. the two definitions of the cut must agree everywhere except at the boundary commit itself —
     they are independent readings of the same artifact and a disagreement STOPS the tool;
  5. the derived flagged totals must reconcile with the input artifact's OWN published totals,
     by stratum and by document role — a disagreement means one of the two files has been edited
     by hand since the other was written, and it STOPS the tool.

WHAT THIS DOES NOT DO.  It restores nothing, reverts nothing, corrects nothing and resolves
nothing.  It makes no comparison against the code in either direction.  It expresses no view on
whether any change should have happened, and no view on the period question itself: it re-derives
the split the ruling was taken against and publishes the population the screen must read.

Usage:
  python tools/audit/gen_period_stratum_split.py            # write the artifact
  python tools/audit/gen_period_stratum_split.py --check    # re-derive, exit 1 on drift
"""
from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from output_encoding import use_utf8_output                        # noqa: E402  (path set above)

use_utf8_output()

ROOT = Path(__file__).resolve().parent.parent.parent
IN_MAIN = ROOT / "tools" / "audit" / "doc_change_candidates.json"
IN_HUNKS = ROOT / "tools" / "audit" / "doc_change_candidates_hunks.jsonl"
OUT = ROOT / "tools" / "audit" / "period_stratum_split.json"


class Stop(Exception):
    """A demand of the derivation is unmet. Never a warning, never a skipped record."""


# ── AUTHORED — the ruled start, taken at the ruling record ───────────────────────────────────────
RULED_START = "b006dc15b5f696f2fc86ad72b97fae58d2119cd7"
RULED_START_SOURCE = (
    "`cowork_rulings_2026_08_15_period_start.md`, the first ruling: \"The restructuring period "
    "opens EXCLUSIVE at commit b006dc15b5f696f2fc86ad72b97fae58d2119cd7\" — taken by the user on "
    "2026-08-15 on the surface "
    "`ratification_surfaces/cowork_restructuring_period_start_decision_surface.md` (Alternative B).")

# ── AUTHORED — which document roles are SPECIFICATION-BEARING ────────────────────────────────────
# Taken from the decision surface's F2, which states the slice as `governing` + `specification-or-
# docs`, and from the dispatch's own §0c, which names the same two roles.  The role vocabulary
# itself is the candidate generator's, not this tool's.
SPEC_BEARING_ROLES = ("governing", "specification-or-docs")
SPEC_BEARING_SOURCE = (
    "The decision surface's F2 — \"the specification-bearing slice is 314 (governing 239 + "
    "specification-or-docs 75)\" — and `cc_instruction_period_checks.md` §0a, which names the same "
    "two roles. The roles themselves are assigned by `tools/audit/gen_doc_change_candidates.py`; "
    "this tool selects among them and defines none.")

# ── AUTHORED — the registered expectation, graded and never reconciled towards ───────────────────
# `cc_instruction_period_checks.md` §0a, prediction P1.  These are the ad-hoc values the decision
# surface declared as assumption A1.  They are recorded here ONLY so the grading is mechanical;
# the dispatch states in terms that they "are registered expectations, not values, and carry no
# authority", and that a difference is a FINDING reported with its per-cell diff — never resolved
# in their favour.
P1_FLAGGED_BY_STRATUM = {
    "S1-open-items-register": 705,
    "S2-status-handoff-doc-split": 378,
    "S3-open-items-register-split": 1279,
    "S4-D231-phase-1": 19836,
}
P1_SPEC_BEARING_BY_STRATUM = {
    "S1-open-items-register": 22,
    "S2-status-handoff-doc-split": 17,
    "S3-open-items-register-split": 28,
    "S4-D231-phase-1": 247,
}
P1_SOURCE = ("`cc_instruction_period_checks.md` §0a, prediction P1, which records the values "
             "assumption A1 of the decision surface declared. Registered expectation, moderate "
             "confidence, no authority.")

# ── AUTHORED — the caveat this tool INHERITS and may not drop ────────────────────────────────────
INHERITED_CAVEAT = (
    "#19, INHERITED AND NOT DISCHARGED HERE. Every count below is a re-derivation over the two "
    "candidate artifacts, and the generator that produced those artifacts "
    "(`tools/audit/gen_doc_change_candidates.py`) has itself never been positively established — "
    "it was written in one batch, and its own artifact marks assumption A3 UNESTABLISHED for every "
    "generator family. What THIS tool establishes is that the split follows from those artifacts "
    "and reconciles with the totals they publish of themselves. It establishes nothing about "
    "whether the enumeration underneath them is complete or correct, and a reader may not take a "
    "clean re-derivation here as evidence that it is. What would settle the inherited half is an "
    "establishment pass over that generator — an act named here and not started.")

# ── AUTHORED — the widening's own inputs ─────────────────────────────────────────────────────────
# Added 2026-08-21 by `cc_instruction_successor_plan_landing_and_step_zero.md` Task 2, executing
# Ruling 7.  It publishes a SECOND population BESIDE the one above; every field above is untouched.
IN_DOCSET = ROOT / "tools" / "audit" / "specification_document_set.json"

WIDENING_RULING = (
    "Ruling 7 (Alternative A) of `cowork_rulings_2026_08_21_successor_plan_sitting.md`: \"A "
    "preparation-phase act and the one mechanism this plan runs, declared so guardrail 3 is not "
    "breached silently. Its per-document distribution feeds the reading depth (Ruling 12) and the "
    "ordering of units. Failure signal, ruled with it: if most passages land UNDETERMINED the "
    "premise is not measurable, and that is a STOP to the user, not a licence to proceed.\"")

WIDENING_SELECTION = (
    "By MEMBERSHIP of `tools/audit/specification_document_set.json` and by nothing else, across "
    "EVERY stratum, in-period and out-of-period alike. The document ROLE is REPORTED per hunk and "
    "EXCLUDES NOTHING — the candidate generator's own ruling 4, inherited here rather than "
    "re-decided: its role map is 'reported and NOT used to exclude anything'. Selection HAS to be "
    "by membership rather than by role, and that is the whole of what 'widened over the document "
    "set' means mechanically: the candidate enumeration gives every `cowork_*.md` document the "
    "role `cowork-planning-or-ruling`, so a document-set member carrying that name sits OUTSIDE "
    "the existing screen population BY ROLE ALONE, however plainly it specifies the analysis.")

NEEDED_HUNK_FIELDS = ("c", "f", "i", "h", "v", "role")


def sha256_of(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_inputs():
    if not IN_MAIN.exists() or not IN_HUNKS.exists():
        raise Stop(f"an input artifact is missing: {IN_MAIN}, {IN_HUNKS}")
    main = json.loads(IN_MAIN.read_text(encoding="utf-8"))
    hunks = []
    for lineno, line in enumerate(IN_HUNKS.read_text(encoding="utf-8").split("\n"), start=1):
        if not line.strip():
            continue
        rec = json.loads(line)
        missing = [k for k in NEEDED_HUNK_FIELDS if k not in rec]
        if missing:
            raise Stop(f"hunk record at line {lineno} is missing {missing} — a record is never "
                       f"skipped (assumption A1's check)")
        hunks.append(rec)
    return main, hunks


def build() -> dict:
    main, hunks = load_inputs()

    commits = main["commits"]
    files = main["files"]

    start_pos = None
    for c in commits:
        if c["sha"] == RULED_START:
            start_pos = c["i"]
            break
    if start_pos is None:
        raise Stop(f"the ruled start commit {RULED_START} is not in the candidate artifact's "
                   f"commits table — the cut cannot be taken")
    start_commit = commits[start_pos]
    if start_commit["sha"] != RULED_START:
        raise Stop("the commits table is not indexed by its own `i` field")

    for h in hunks:
        if not 0 <= h["c"] < len(commits):
            raise Stop(f"hunk commit index {h['c']} does not resolve into the commits table")
        if not 0 <= h["f"] < len(files):
            raise Stop(f"hunk file index {h['f']} does not resolve into the files table")

    # ── the cut, taken two independent ways over the same artifact ───────────────────────────────
    # (a) THE RULED ONE, which governs: a commit strictly after the ruled start, in the commits
    #     table's own ancestry order, is IN-PERIOD.
    # (b) THE STRATUM ONE, which is the vocabulary the artifact speaks in: stratum S4, which is
    #     inclusive of the boundary commit.
    # They must agree everywhere except at the boundary commit itself.
    s4 = main["range"]["bounds"][-1]["id"]
    if main["range"]["bounds"][-1]["commit"] != RULED_START:
        raise Stop("the candidate artifact's last stratum boundary is not the ruled start commit — "
                   "the two readings of the cut are not comparable")

    def in_period(ci: int) -> bool:
        return ci > start_pos

    def in_s4(ci: int) -> bool:
        return commits[ci]["stratum"] == s4

    disagree = [c["sha"] for c in commits
                if in_period(c["i"]) != in_s4(c["i"]) and c["sha"] != RULED_START]
    if disagree:
        raise Stop(f"the position cut and the stratum cut disagree away from the boundary commit: "
                   f"{disagree[:5]}")

    # ── the split ────────────────────────────────────────────────────────────────────────────────
    flagged = [h for h in hunks if h["v"] == "FLAG"]

    all_by_stratum = Counter(commits[h["c"]]["stratum"] for h in hunks)
    flagged_by_stratum = Counter(commits[h["c"]]["stratum"] for h in flagged)
    flagged_by_role = Counter(h["role"] for h in flagged)

    matrix: dict[str, Counter] = defaultdict(Counter)
    for h in flagged:
        matrix[commits[h["c"]]["stratum"]][h["role"]] += 1

    spec = [h for h in flagged if h["role"] in SPEC_BEARING_ROLES]
    spec_by_stratum = Counter(commits[h["c"]]["stratum"] for h in spec)
    spec_by_role = Counter(h["role"] for h in spec)

    # ── the period cut, applied ──────────────────────────────────────────────────────────────────
    in_flagged = [h for h in flagged if in_period(h["c"])]
    out_flagged = [h for h in flagged if not in_period(h["c"])]
    in_spec = [h for h in spec if in_period(h["c"])]
    out_spec = [h for h in spec if not in_period(h["c"])]

    boundary_hunks = [h for h in hunks if commits[h["c"]]["sha"] == RULED_START]
    boundary_flagged = [h for h in boundary_hunks if h["v"] == "FLAG"]
    boundary_spec = [h for h in boundary_flagged if h["role"] in SPEC_BEARING_ROLES]

    pre_s4_spec = [h for h in spec if commits[h["c"]]["stratum"] != s4]

    def hunk_record(h: dict) -> dict:
        c = commits[h["c"]]
        path = files[h["f"]]
        return {
            "commit": c["sha"],
            "date": c["date"],
            "stratum": c["stratum"],
            "commit_subject": c["subject"],
            "file": path,
            "hunk_header": h["h"],
            "hunk_ordinal_in_the_commit": h["i"],
            "role": h["role"],
            "surface_class": h.get("cls"),
            "file_status_in_the_commit": h.get("st"),
            "change_shape": h.get("k"),
            "lines_removed_added": h.get("d"),
            "carry_vector": h.get("m"),
            "look_alike_signals": h.get("sig", []),
            "authoring_side": h.get("as"),
            "in_a_preserved_former_wording_context": bool(h.get("pres")),
            "added_by_the_ruled_cut": commits[h["c"]]["sha"] == RULED_START,
            "retrieve": f"git show {c['sha']} --no-color -U0 -- {path}",
        }

    screen = [hunk_record(h) for h in out_spec]
    screen.sort(key=lambda r: (r["date"], r["commit"], r["file"], r["hunk_ordinal_in_the_commit"]))

    # ── reconciliation against the input artifact's own published totals ─────────────────────────
    published_stratum = main["counted"]["flags_by_stratum"]
    published_role = main["counted"]["flags_by_document_role"]
    stratum_diff = {k: [published_stratum.get(k), flagged_by_stratum.get(k, 0)]
                    for k in set(published_stratum) | set(flagged_by_stratum)
                    if published_stratum.get(k) != flagged_by_stratum.get(k, 0)}
    role_diff = {k: [published_role.get(k), flagged_by_role.get(k, 0)]
                 for k in set(published_role) | set(flagged_by_role)
                 if published_role.get(k) != flagged_by_role.get(k, 0)}
    if stratum_diff or role_diff:
        raise Stop("the derived flagged totals do not reconcile with the input artifact's own "
                   f"published totals — by stratum {stratum_diff}, by role {role_diff}. One of the "
                   "two files has been edited by hand since the other was written.")

    # ── P1, graded ───────────────────────────────────────────────────────────────────────────────
    def grade(predicted: dict, derived: Counter) -> dict:
        cells = {}
        for k in sorted(set(predicted) | set(derived)):
            p, d = predicted.get(k), derived.get(k, 0)
            cells[k] = {"registered_expectation": p, "derived": d, "agrees": p == d,
                        "difference_derived_minus_expectation": (None if p is None else d - p)}
        return {"per_cell": cells,
                "every_cell_agrees": all(v["agrees"] for v in cells.values())}

    p1_flagged = grade(P1_FLAGGED_BY_STRATUM, flagged_by_stratum)
    p1_spec = grade(P1_SPEC_BEARING_BY_STRATUM, spec_by_stratum)

    # ── THE WIDENED SCREEN POPULATION (Task 2, Ruling 7) ─────────────────────────────────────────
    # A SECOND population, published beside the one above and leaving every field above untouched.
    if not IN_DOCSET.exists():
        raise Stop(f"the document set the widening selects by is missing: {IN_DOCSET}")
    docset = json.loads(IN_DOCSET.read_text(encoding="utf-8"))
    member_of = {m["member"]: m for m in docset["the_document_set"]}
    if not member_of:
        raise Stop("the document set carries no members — the widening would select nothing")

    def ident(rec: dict) -> tuple:
        return (rec["commit"], rec["file"], rec["hunk_header"])

    widened = []
    for h in flagged:
        m = member_of.get(files[h["f"]])
        if m is None:
            continue
        rec = hunk_record(h)
        rec["member_limb"] = m["limb"]
        rec["member_delegation_scope"] = m["delegation_scope"]
        rec["member_delegated_sections"] = m["delegated_sections"]
        rec["in_period_under_the_ruling"] = in_period(h["c"])
        widened.append(rec)
    widened.sort(key=lambda r: (r["file"], r["date"], r["commit"],
                                r["hunk_ordinal_in_the_commit"]))

    member_paths = set(member_of)
    screen_ids = {ident(r) for r in screen}
    widened_ids = {ident(r) for r in widened}

    # the relation to the existing population, taken BOTH WAYS
    should_be_widened = {i for i in screen_ids if i[1] in member_paths}
    unreconciled = sorted(should_be_widened - widened_ids)
    if unreconciled:
        raise Stop("hunk(s) the two readings cannot reconcile — already screened, their file IS a "
                   f"document-set member, and yet absent from the widened population: "
                   f"{unreconciled[:5]}")
    already_ids = widened_ids & screen_ids
    new_ids = widened_ids - screen_ids
    if (already_ids | new_ids) != widened_ids or (already_ids & new_ids):
        raise Stop("the widened population does not partition into already-screened and NEW — "
                   "none may be in both and none in neither")
    outside_ids = {i for i in screen_ids if i[1] not in member_paths}
    if len(already_ids) + len(outside_ids) != len(screen_ids) or (already_ids & outside_ids):
        raise Stop("the existing screen population does not partition against document-set "
                   "membership — none may be in both and none in neither")
    for r in widened:
        r["already_screened"] = ident(r) in screen_ids
        r["is_NEW"] = not r["already_screened"]

    new_rows = [r for r in widened if r["is_NEW"]]

    # the COVERAGE GAP — every member with no FLAG hunk in the candidate enumeration
    by_path: dict[str, list] = defaultdict(list)
    for h in hunks:
        by_path[files[h["f"]]].append(h)
    files_enumerated = set(files)
    rng = main["range"]
    gap = []
    for path in sorted(member_paths):
        mine = by_path.get(path, [])
        fl = [h for h in mine if h["v"] == "FLAG"]
        if mine and fl:
            continue
        if not mine:
            reason = (
                "NO hunk of this file is in the candidate enumeration. The enumeration's own "
                "commit population is the restructuring period — opening EXCLUSIVE at "
                f"{rng['start_commit_EXCLUSIVE']}, ending at {rng['end_commit']}, "
                f"{rng['commits_in_the_population']} commits — so a file no commit of that "
                "population touched has nothing to enumerate."
                + ("" if path in files_enumerated else
                   " The file does not appear in the enumeration's `files` table at all."))
        else:
            reason = (
                "the file IS enumerated and every hunk of it classifies PURE, so it contributes "
                "no FLAG hunk. The enumeration's own default is FLAG ON DOUBT, with PURE emitted "
                "only where a mechanical recognizer fires — so this is the enumeration reporting "
                "that every change it saw to this file in the period was a recognised pure "
                "restructuring, not that the file went unexamined.")
        gap.append({
            "member": path,
            "member_limb": member_of[path]["limb"],
            "hunks_in_the_candidate_enumeration": len(mine),
            "flagged_hunks": len(fl),
            "in_the_enumerations_files_table": path in files_enumerated,
            "the_reason_the_enumeration_gives_for_itself": reason,
        })

    widened_block = {
        "what_it_is": (
            "THE WIDENED SCREEN POPULATION: every FLAG hunk of the candidate enumeration whose "
            "file is a member of the specification document set, across EVERY stratum, in-period "
            "and out-of-period alike. It is published BESIDE the population above and replaces "
            "nothing: the existing screen population, its counts and its enumeration are "
            "untouched."),
        "ruling": WIDENING_RULING,
        "dispatch": "cc_instruction_successor_plan_landing_and_step_zero.md",
        "★_the_selection_is_by_MEMBERSHIP_and_the_role_excludes_nothing": WIDENING_SELECTION,
        "★_the_inherited_establishment_caveat": INHERITED_CAVEAT,
        "the_document_set": {
            "artifact": "tools/audit/specification_document_set.json",
            "sha256": sha256_of(IN_DOCSET),
            "members": sorted(member_paths),
            "members_counted": len(member_paths),
        },
        "size": len(widened),
        "already_screened": len(already_ids),
        "NEW": len(new_ids),
        "by_document": dict(sorted(Counter(r["file"] for r in widened).items())),
        "by_document_NEW_only": dict(sorted(Counter(r["file"] for r in new_rows).items())),
        "by_stratum": dict(sorted(Counter(r["stratum"] for r in widened).items())),
        "by_stratum_NEW_only": dict(sorted(Counter(r["stratum"] for r in new_rows).items())),
        "by_role": dict(sorted(Counter(r["role"] for r in widened).items())),
        "by_period": {
            "IN_PERIOD": sum(1 for r in widened if r["in_period_under_the_ruling"]),
            "OUT_OF_PERIOD": sum(1 for r in widened if not r["in_period_under_the_ruling"]),
        },
        "distinct_commits": len({r["commit"] for r in widened}),
        "the_relation_to_the_existing_screen_population": {
            "★_taken_BOTH_WAYS": (
                "Every hunk of the existing screen population whose file is a document-set member "
                "must appear in the widened population, and the widened population must partition "
                "exactly into already-screened and NEW. A hunk the two readings cannot reconcile "
                "STOPS the tool rather than being reported as a difference."),
            "existing_screen_population_size": len(screen_ids),
            "of_those_ALREADY_in_the_widened_population": len(already_ids),
            "of_those_NOT_document_set_members": len(outside_ids),
            "the_existing_screened_members_that_are_NOT_document_set_members": {
                "by_document": dict(sorted(Counter(i[1] for i in outside_ids).items())),
                "★_what_they_are": (
                    "Out-of-period specification-bearing hunks whose file the ruled document set "
                    "does not carry — `CLAUDE.md` and the `docs/` documents `ARCHITECTURE.md` "
                    "does not delegate to. They stay screened and their sixty-eight verdicts stay "
                    "exactly as they are; they are named here so that no reader takes the widened "
                    "population for a superset of the old one."),
            },
            "none_in_both_and_none_in_neither": True,
        },
        "the_coverage_gap": {
            "★_what_this_is": (
                "Every document-set member with NO FLAG hunk in the candidate enumeration, with "
                "the reason the enumeration gives for ITSELF rather than a reason invented here. "
                "This is the plan's own finding about the premise's measurability: a member with "
                "no flagged hunk contributes nothing to the pollution distribution, and the "
                "distribution must be read knowing which members are silent and why."),
            "members_with_no_flagged_hunk": len(gap),
            "of_the_members": len(member_paths),
            "members": gap,
        },
        "★_the_size_the_next_task_reads": {
            "NEW_hunks_to_be_authored_a_verdict": len(new_ids),
            "★_read_it_here_rather_than_from_prose": (
                "The sizing the next task reports is this field. It is published so that the "
                "report can state a DIRECTION with its artifact named rather than transcribe a "
                "value (D-663, D-431)."),
        },
        "hunks": widened,
    }

    art = {
        "what_this_is": (
            "THE PERIOD SPLIT, re-derived by a checked tool from the candidate artifacts alone, "
            "with the screen population for the July screen enumerated whole. It supersedes the "
            "ad-hoc per-stratum values the decision surface declared as assumption A1. It restores "
            "nothing, corrects nothing, and makes no comparison against the code."),
        "dispatch": "cc_instruction_period_checks.md",
        "generator": "tools/audit/gen_period_stratum_split.py",
        "reproduce": ("python tools/audit/gen_period_stratum_split.py --check   # re-derives from "
                      "the inputs and exits 1 on any drift"),
        "inputs": [
            {"path": "tools/audit/doc_change_candidates.json",
             "sha256": sha256_of(IN_MAIN), "bytes": IN_MAIN.stat().st_size},
            {"path": "tools/audit/doc_change_candidates_hunks.jsonl",
             "sha256": sha256_of(IN_HUNKS), "bytes": IN_HUNKS.stat().st_size},
        ],
        "★_the_inherited_establishment_caveat": INHERITED_CAVEAT,
        "what_is_AUTHORED_here": {
            "the_ruled_start_commit": {"commit": RULED_START, "taken_at": RULED_START_SOURCE},
            "the_specification_bearing_roles": {"roles": list(SPEC_BEARING_ROLES),
                                                "taken_at": SPEC_BEARING_SOURCE},
            "the_registered_expectation_graded_below": {"taken_at": P1_SOURCE},
        },
        "what_is_DERIVED": [
            "every count and every population below, from the two candidate artifacts alone",
            "the screen population, enumerated whole by hunk identity",
            "the reconciliation against the input artifact's own published totals",
        ],
        "the_ruled_period": {
            "opens_EXCLUSIVE_at": RULED_START,
            "the_boundary_commit": {
                "sha": start_commit["sha"], "date": start_commit["date"],
                "stratum_label_it_carries": start_commit["stratum"],
                "subject": start_commit["subject"],
                "position_in_the_commits_table": start_pos,
            },
            "★_the_boundary_commit_is_OUTSIDE_the_period_it_opens": (
                "EXCLUSIVE is the ruling's own word. The candidate artifact nonetheless labels this "
                "commit with stratum S4, because a stratum boundary is inclusive of the act that "
                "opens it. So the stratum label and the ruled period are NOT the same population, "
                "and the difference is exactly this commit's own hunks — enumerated below rather "
                "than left for a reader to discover."),
            "commits_in_the_candidate_population": len(commits),
            "commits_IN_PERIOD_under_the_ruling": sum(1 for c in commits if in_period(c["i"])),
            "commits_OUT_OF_PERIOD_under_the_ruling": sum(1 for c in commits
                                                          if not in_period(c["i"])),
            "the_two_readings_of_the_cut_agree_away_from_the_boundary_commit": True,
        },
        "the_split": {
            "hunks_by_stratum_all_verdicts": dict(sorted(all_by_stratum.items())),
            "flagged_hunks_by_stratum": dict(sorted(flagged_by_stratum.items())),
            "flagged_hunks_by_stratum_and_document_role": {
                s: dict(sorted(matrix[s].items())) for s in sorted(matrix)},
            "flagged_hunks_by_document_role": dict(sorted(flagged_by_role.items())),
            "specification_bearing_roles": list(SPEC_BEARING_ROLES),
            "specification_bearing_flagged_by_stratum": dict(sorted(spec_by_stratum.items())),
            "specification_bearing_flagged_by_role": dict(sorted(spec_by_role.items())),
            "specification_bearing_flagged_total": len(spec),
        },
        "the_period_cut_applied": {
            "flagged_hunks_IN_PERIOD": len(in_flagged),
            "flagged_hunks_OUT_OF_PERIOD": len(out_flagged),
            "specification_bearing_flagged_IN_PERIOD": len(in_spec),
            "specification_bearing_flagged_OUT_OF_PERIOD": len(out_spec),
            "the_boundary_commits_own_hunks": {
                "hunks_enumerated": len(boundary_hunks),
                "flagged": len(boundary_flagged),
                "specification_bearing_flagged": len(boundary_spec),
                "★_why_they_are_counted_OUT_OF_PERIOD": (
                    "The ruling opens the period exclusive at this commit, so its own changes are "
                    "outside the period and inside the class the screen exists to check."),
            },
        },
        "the_screen_population_for_task_2": {
            "what_it_is": (
                "Every OUT-OF-PERIOD specification-bearing flagged hunk: the pre-S4 strata plus "
                "whatever the boundary commit itself contributes. This is the population the July "
                "screen reads, one hunk at a time."),
            "★_why_the_ruled_cut_rather_than_the_pre_S4_strata_alone": (
                "The dispatch names the pre-S4 slice, which is the stratum reading. Under the "
                "ruled cut the boundary commit is out of period too, so its specification-bearing "
                "flagged hunks sit in exactly the class the screen exists to check. Taking the "
                "ruled cut can only ADD members and never drop one, and under-screening is the "
                "direction that costs the objective. Both slices are published; the members the "
                "wider one adds are marked `added_by_the_ruled_cut` in the enumeration."),
            "size": len(screen),
            "the_pre_S4_strata_slice_size": len(pre_s4_spec),
            "members_the_ruled_cut_adds": len(screen) - len(pre_s4_spec),
            "by_stratum": dict(sorted(Counter(r["stratum"] for r in screen).items())),
            "by_role": dict(sorted(Counter(r["role"] for r in screen).items())),
            "by_file": dict(sorted(Counter(r["file"] for r in screen).items())),
            "distinct_commits": len({r["commit"] for r in screen}),
            "hunks": screen,
        },
        "reconciliation_against_the_input_artifacts_own_totals": {
            "flags_by_stratum": "reconciles exactly",
            "flags_by_document_role": "reconciles exactly",
            "★_what_a_disagreement_would_have_meant": (
                "The two inputs come from one generator in one act. A difference between what this "
                "tool counts and what that artifact publishes of itself would mean one of the two "
                "files had been edited by hand since the other was written, which is why it is a "
                "STOP here rather than a reported difference."),
        },
        "P1_the_registered_expectation_graded": {
            "★_what_this_grading_is_and_is_not": (
                "The expectation is the ad-hoc split the decision surface declared as assumption "
                "A1. It carries no authority. Where a cell differs, the derived value governs and "
                "the difference is a FINDING published per cell — it is never reconciled towards "
                "the expectation, and nothing here is adjusted to make a cell agree."),
            "flagged_hunks_by_stratum": p1_flagged,
            "specification_bearing_flagged_by_stratum": p1_spec,
        },
        "what_this_does_NOT_do": (
            "It restores nothing, reverts nothing, corrects nothing and resolves nothing. It makes "
            "no comparison against the code in either direction. It takes no view on the period "
            "question, on whether any enumerated change should have happened, or on what the "
            "screen will find. It closes no open-items row and writes no decisions-register "
            "entry."),
        "★_the_widened_screen_population": widened_block,
    }
    return art


def render(art: dict) -> str:
    return json.dumps(art, indent=1, ensure_ascii=False) + "\n"


def main(argv: list[str]) -> int:
    art = build()
    text = render(art)
    if "--check" in argv:
        if not OUT.exists():
            print("FAIL: artifact missing:", OUT)
            return 1
        if OUT.read_text(encoding="utf-8") != text:
            print("FAIL: re-derivation differs from the committed artifact:", OUT)
            return 1
        print("OK: the period split re-derives byte-identically.")
        return 0
    OUT.write_text(text, encoding="utf-8", newline="")
    print("wrote", OUT)
    s = art["the_split"]
    p = art["the_period_cut_applied"]
    print(f"  flagged by stratum: {s['flagged_hunks_by_stratum']}")
    print(f"  specification-bearing by stratum: "
          f"{s['specification_bearing_flagged_by_stratum']}")
    print(f"  flagged in period {p['flagged_hunks_IN_PERIOD']}, "
          f"out of period {p['flagged_hunks_OUT_OF_PERIOD']}")
    sc = art["the_screen_population_for_task_2"]
    print(f"  THE SCREEN POPULATION: {sc['size']} hunks "
          f"({sc['the_pre_S4_strata_slice_size']} in the pre-S4 strata, "
          f"{sc['members_the_ruled_cut_adds']} added by the ruled cut) "
          f"across {sc['distinct_commits']} commits")
    g = art["P1_the_registered_expectation_graded"]
    print(f"  P1 flagged-by-stratum every cell agrees: "
          f"{g['flagged_hunks_by_stratum']['every_cell_agrees']}")
    print(f"  P1 specification-bearing every cell agrees: "
          f"{g['specification_bearing_flagged_by_stratum']['every_cell_agrees']}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except Stop as exc:
        print(f"STOP: {exc}")
        raise SystemExit(2)
