#!/usr/bin/env python3
"""WHAT THE 2026-08-08 HOME-CLASSIFICATION APPLY ACTUALLY MOVED, field by field.

WHY THIS EXISTS.  The applying run of `gen_home_classification.py` rewrites the WHOLE of
`backbone_decisions.json` — it re-serializes the file rather than patching it — and it had been
held un-run for a month (`OPEN_ITEMS.md` OI-305, OI-319, OI-350).  A claim that such a run touched
only the two fields it is supposed to touch is a claim about the register's own data, and a claim
about data stated in prose is a claim nobody can re-run.  The dispatch of 2026-08-08 declares it as
ASSUMPTION A1 — *the epoch treatment leaves every field outside its intended writes byte-stable* —
and requires it discharged by a field-diff before anything reads the result.  Movement anywhere
else is a STOP, not a remark.

WHAT THE INTENDED WRITES ARE, taken from the classifier's own docstring and not restated from
memory: `nonspec_kind` and `home_section` on every entry of the home population, and the removal of
a stale `home_section` from an entry outside it.  Everything else in every entry — the verbatim,
the home, the status, the defense, the provenance, the supersession — is outside the intended
writes and must be byte-stable.

HOW THE BEFORE SIDE IS OBTAINED, and why it is not a git object.  The edit-shape tools of the two
preceding waves fetch their BEFORE side as a git object by explicit hash, which is the form D-253
admits.  That route is not available here: the register data is already MODIFIED in the working
tree by the uncommitted document-route wave, so the last commit is not the state this apply starts
from.  The pre-apply state is therefore SNAPSHOTTED into the repository first — the O-12 pattern
gate block (A) uses for a re-baseline, and the same pattern the phase-1q record itself was frozen
under on 2026-08-04.  Both sides are then ordinary files this tool reads.

WHY IT CARRIES NO RE-DERIVATION MODE, and why that keeps it out of the guard population.  Under the
user's ruling R4 of 2026-08-04 a tool that RE-DERIVES A LIVE INVARIANT belongs in the guard list and
a tool that RECORDS A MEASUREMENT TAKEN AT A POINT IN TIME does not.  This one records what one
named run did on one day; re-deriving it later would say nothing about the tree.  It therefore
carries no re-derivation mode at all, which also keeps it out of `gen_guard_state.py`'s derived
candidate population rather than sitting there unclassified — the same construction, and the same
reason, as `gen_route_homing_edit_shape.py`.

WHAT IT DOES NOT DO.  It reads two files and writes one artifact.  It moves no entry, applies no
criterion, judges nothing about whether a class is correct, and authorizes nothing.

Run, in this order:
    python tools/audit/decisions/gen_apply_field_diff.py --snapshot   # BEFORE the applying run
    python tools/audit/decisions/gen_apply_field_diff.py              # AFTER it
"""
from __future__ import annotations

import json
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
LIVE = os.path.join(HERE, "backbone_decisions.json")
SNAPDIR = os.path.join(HERE, "snapshot_2026-08-08_pre_home_classification_apply")
SNAP = os.path.join(SNAPDIR, "backbone_decisions.json")
OUT = os.path.join(HERE, "apply_field_diff.json")

sys.path.insert(0, os.path.dirname(HERE))
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

# The classifier's intended writes, per its own docstring. A field outside this set that moves is
# the STOP this tool exists for.
INTENDED = {"nonspec_kind", "home_section"}

# AUTHORED — top-level MAP KEYS of the register data whose movement between the snapshot and the
# applying run is ACCOUNTED FOR by a declared act of this batch, with the act named. The applying
# run itself writes no top-level map key, so an unaccounted one is a defect in it; one that moved
# because a preceding edit of this batch moved it is not, and the difference must be visible
# rather than folded into a verdict. A map key that moves with no row here is the STOP.
ACCOUNTED_TOP_LEVEL: dict[str, str] = {
    "section_home_criterion": (
        "Moved by a DECLARED EDIT of this batch, made before the applying run and not by it: "
        "`docs/unified_analysis_pipeline.md`'s authored delegation-scope judgment was moved from "
        "`documents` into `documents_retired_when_their_last_entry_was_re_homed`, because the "
        "2026-08-07 owner-rulings wave re-homed its last four entries and retired three other "
        "emptied documents but not this one. Until that was completed the classifier STOPPED on "
        "it before classifying anything — the STOP is that guard working, and the same act the "
        "three earlier retirement records in that block already say. The judgment is moved whole "
        "rather than deleted (#12)."
    ),
}


class Stop(Exception):
    """A field outside the intended writes moved, or a side is unreadable. Never a warning."""


def load(path: str) -> dict:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def entries_by_id(doc: dict) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for d in doc["decisions"]:
        if d["id"] in out:
            raise Stop(f"duplicate entry identifier in the register data: {d['id']}")
        out[d["id"]] = d
    return out


def field_moves(before: dict, after: dict) -> list[dict]:
    """Per entry, every top-level field whose serialized value differs."""
    rows: list[dict] = []
    for ident in sorted(set(before) | set(after)):
        b, a = before.get(ident), after.get(ident)
        if b is None:
            rows.append({"id": ident, "what": "ENTRY ADDED", "fields": sorted(a)})
            continue
        if a is None:
            rows.append({"id": ident, "what": "ENTRY REMOVED", "fields": sorted(b)})
            continue
        moved = []
        for field in sorted(set(b) | set(a)):
            bv = json.dumps(b.get(field), sort_keys=True, ensure_ascii=False) if field in b else None
            av = json.dumps(a.get(field), sort_keys=True, ensure_ascii=False) if field in a else None
            if bv != av:
                moved.append({
                    "field": field,
                    "present_before": field in b,
                    "present_after": field in a,
                    "intended": field in INTENDED,
                })
        if moved:
            rows.append({"id": ident, "what": "FIELDS MOVED", "moved": moved})
    return rows


def top_level_moves(before: dict, after: dict) -> list[dict]:
    """Every top-level map key of the register data OTHER than `decisions`, compared whole."""
    rows = []
    for name in sorted(set(before) | set(after)):
        if name == "decisions":
            continue
        bv = json.dumps(before.get(name), sort_keys=True, ensure_ascii=False) if name in before else None
        av = json.dumps(after.get(name), sort_keys=True, ensure_ascii=False) if name in after else None
        if bv != av:
            rows.append({"map_key": name,
                         "present_before": name in before, "present_after": name in after,
                         "accounted_for": name in ACCOUNTED_TOP_LEVEL,
                         "by_what": ACCOUNTED_TOP_LEVEL.get(name)})
    return rows


def snapshot() -> int:
    if not os.path.exists(LIVE):
        raise Stop(f"the register data is missing: {os.path.relpath(LIVE, ROOT)}")
    if os.path.exists(SNAP):
        raise Stop(
            "a pre-apply snapshot already exists at "
            f"{os.path.relpath(SNAP, ROOT)} — refusing to overwrite it. A snapshot taken after "
            "the applying run has already moved the data would record the wrong BEFORE side, "
            "which is the whole failure this tool exists to detect.")
    os.makedirs(SNAPDIR, exist_ok=True)
    shutil.copyfile(LIVE, SNAP)
    print(f"wrote {os.path.relpath(SNAP, ROOT)}")
    return 0


def main(argv: list[str]) -> int:
    if "--snapshot" in argv:
        return snapshot()

    if not os.path.exists(SNAP):
        raise Stop("no pre-apply snapshot on disk — run this tool with --snapshot BEFORE the "
                   "applying run, or the comparison has no BEFORE side.")

    before_doc, after_doc = load(SNAP), load(LIVE)
    before, after = entries_by_id(before_doc), entries_by_id(after_doc)

    rows = field_moves(before, after)
    top = top_level_moves(before_doc, after_doc)

    unintended = []
    for r in rows:
        if r["what"] != "FIELDS MOVED":
            unintended.append({"id": r["id"], "why": r["what"]})
            continue
        for m in r["moved"]:
            if not m["intended"]:
                unintended.append({"id": r["id"], "why": f"field {m['field']!r} moved"})

    counted = {
        "entries_before": len(before),
        "entries_after": len(after),
        "entries_with_any_field_moved": len(rows),
        "nonspec_kind_moved": sum(
            1 for r in rows if r["what"] == "FIELDS MOVED"
            and any(m["field"] == "nonspec_kind" for m in r["moved"])),
        "home_section_moved": sum(
            1 for r in rows if r["what"] == "FIELDS MOVED"
            and any(m["field"] == "home_section" for m in r["moved"])),
        "home_section_written_for_the_first_time": sum(
            1 for r in rows if r["what"] == "FIELDS MOVED"
            and any(m["field"] == "home_section" and not m["present_before"] for m in r["moved"])),
        "home_section_removed": sum(
            1 for r in rows if r["what"] == "FIELDS MOVED"
            and any(m["field"] == "home_section" and not m["present_after"] for m in r["moved"])),
        "entries_with_a_field_outside_the_intended_writes_moved": len(unintended),
        "top_level_map_keys_moved": len(top),
        "top_level_map_keys_moved_with_no_declared_act_to_account_for_them": len(
            [t for t in top if not t["accounted_for"]]),
    }
    unaccounted = [t["map_key"] for t in top if not t["accounted_for"]]
    stale_account = [k for k in ACCOUNTED_TOP_LEVEL
                     if k not in {t["map_key"] for t in top}]
    if stale_account:
        raise Stop("a top-level map key is recorded as accounted for and did not move: "
                   f"{stale_account} — an account for a movement that did not happen is the "
                   "same defect in the other direction, and it is not carried silently.")

    art = {
        "purpose": "ASSUMPTION A1 of the 2026-08-08 away dispatch, discharged by measurement: the "
                   "home-classification applying run leaves every field outside its intended "
                   "writes byte-stable. Not a judgment about whether any class is correct, and "
                   "not an authorization for any fix, design or inference change.",
        "generated_by": "tools/audit/decisions/gen_apply_field_diff.py",
        "generated_for": "cc_instruction_away_execution.md, Task 0 (the epoch treatment ruled by "
                         "the user on 2026-08-08, Ruling 1 of "
                         "`cowork_rulings_2026_08_08_pre_away.md`)",
        "the_before_side": {
            "path": os.path.relpath(SNAP, ROOT).replace("\\", "/"),
            "what_it_is": "the register data as it stood immediately before the applying run, "
                          "snapshotted into the repository first (the O-12 pattern)",
            "why_not_a_git_object": "the register data was already modified in the working tree by "
                                    "the uncommitted document-route wave, so the last commit is "
                                    "not the state this apply starts from",
        },
        "the_intended_writes": sorted(INTENDED),
        "what_intended_means_here": (
            "The classifier's own docstring states what it writes: `nonspec_kind` and "
            "`home_section` on every entry of the home population, plus the removal of a stale "
            "`home_section` from an entry outside that population. Every other field of every "
            "entry, and every top-level map key of the register data, is outside the intended "
            "writes."
        ),
        "★_a_field_outside_the_intended_writes_is_a_STOP_not_a_remark": (
            "The applying run re-serializes the whole file rather than patching it, so a defect in "
            "it would move data nobody was looking at. That is why this is measured rather than "
            "asserted, and why a non-empty list below halts the batch."
        ),
        "★_a_top_level_map_key_that_moved_is_reported_with_the_act_that_moved_it_or_it_is_a_STOP": (
            "The applying run writes no top-level map key at all, so one that moved was moved by "
            "something else. This batch made one such edit before the run and declares it rather "
            "than letting the diff absorb it: the account is authored, the movement is derived, "
            "and each stops the run if the other is absent. A movement with no account halts the "
            "batch; an account for a movement that did not happen halts it too."
        ),
        "counted": counted,
        "fields_outside_the_intended_writes_that_moved": unintended,
        "top_level_map_keys_that_moved": top,
        "top_level_map_keys_that_moved_with_no_declared_act": unaccounted,
        "entries": rows,
        "verdict": ("A1 HOLDS" if not unintended and not unaccounted
                    else "A1 REFUTED — STOP"),
    }

    with open(OUT, "w", encoding="utf-8", newline="") as fh:
        fh.write(json.dumps(art, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {os.path.relpath(OUT, ROOT)}")
    for k, v in counted.items():
        print(f"  {k}: {v}")
    for t in top:
        print(f"  top-level map key moved: {t['map_key']}  accounted-for={t['accounted_for']}")
    print(f"  VERDICT: {art['verdict']}")
    return 0 if not unintended and not unaccounted else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except Stop as exc:
        print(f"STOP: {exc}")
        raise SystemExit(2)
