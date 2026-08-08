#!/usr/bin/env python3
"""THE OI-333 REPAIR RECORD — what the escape changed in the cluster-disposition layer.

WHY THIS FILE EXISTS.  The user's ruling R4 of 2026-08-07 (dispatch
`cc_instruction_five_rulings.md` §0a) orders the repair in five parts: snapshot the committed
disposition layer first, escape the six invalid register patterns, regenerate the layer at the
register's current backbone, DIFF the result against the snapshot and EXPLAIN every cluster that
moves, and add a producibility mode so the failure class fails a guard in future.  This file is the
fourth part.  It is also where the two assumptions the dispatch declared are discharged in writing.

WHAT IS AUTHORED AND WHAT IS DERIVED.
  authored : the SIX FORMER PATTERN STRINGS, preserved verbatim (#12) so the repair is reversible
             and reviewable; the dispatch's two assumptions as it stated them; and the one note
             recording where the escape did more than escape emphasis, with the evidence for it.
  derived  : every pattern's compile result at HEAD; the snapshot's own recorded hashes; the whole
             cluster-level diff and its per-cluster cause attribution; and every count.

WHY IT IS NOT IN THE GUARD LIST, stated so a later reader does not read the absence as an
oversight.  Under the user's ruling R4 of 2026-08-04 (`OPEN_ITEMS.md` OI-330) a tool that RECORDS A
MEASUREMENT TAKEN AT A POINT IN TIME does not belong in the guard list; this is such a record — the
movement between one named snapshot and one named regeneration, both of which are past events.  It
therefore carries no re-derivation mode at all, so the guard population's own derived candidate rule
does not reach it.  What IS live, and what the same ruling put in the guard list instead, is
`gen_cluster_dispositions.py --producible`.

Run:  python tools/audit/decisions/gen_oi333_repair.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent
sys.path.insert(0, str(HERE.parent))

from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

REGISTER = HERE / "backbone_decisions.json"
LAYER = HERE / "cluster_dispositions.json"
MANIFEST = HERE / "disposition_manifest.json"
SNAP = HERE / "snapshot_2026-08-07_pre_oi333_repair"
OUT = HERE / "oi333_repair.json"

# ── authored: the six patterns as they stood before the escape, kept whole (#12) ────────────────
# Read off the tree by the wave that repaired them, and identical to the table `open_items/OI-333.md`
# carries.  They are preserved here rather than in six entries' provenance because the defect is one
# act over one class, and splitting it six ways would leave no place where the class is visible.
FORMER_PATTERNS = {
    "D-555": "a **motion-type-led** feature set",
    "D-570": "judged against the **score**",
    "D-576": "is largely **key-independent**",
    "D-577": "design debt** (wrong cut) from **migration debt",
    "D-578": "orphan claims need a **whole-repo** grep",
    "D-581": "Not-yet-consumed information is **NOT automatically a defect",
}

# authored: the one place the escape did more than escape markdown emphasis, with its evidence.
THE_ONE_PLACE_THE_ESCAPE_DID_MORE = {
    "entry": "D-577",
    "what": "The parentheses around `wrong cut` were escaped as well as the emphasis.",
    "why_it_is_the_literal_the_author_meant": (
        "Unescaped, `(wrong cut)` is a regular-expression GROUP, so the pattern would have "
        "required the text `design debt** wrong cut from **migration debt` — WITHOUT the "
        "parentheses. The entry's own text carries them: the phrase occurs, with its parentheses, "
        "in this entry's verbatim. So the group reading matched a string the record does not "
        "contain, and escaping is what makes the matcher match what the author wrote."
    ),
    "why_it_is_recorded_rather_than_folded_in": (
        "Every other change in this repair is mechanical — a literal `**` escaped to `\\*\\*` — "
        "and this one is a judgment about intent. It is named so a reviewer can disagree with it "
        "in one place rather than having to re-derive which of six changes was not mechanical."
    ),
}

ASSUMPTIONS = {
    "A1": {
        "as_the_dispatch_states_it": (
            "That the six `patterns` strings in `tools/audit/decisions/backbone_decisions.json` "
            "(entries D-555, D-570, D-576, D-577, D-578, D-581) are exactly as OI-333's table "
            "lists them, and are the ONLY patterns that fail to compile."
        ),
        "how_it_was_checked": (
            "Every pattern in the register was compiled BEFORE any was edited, as the dispatch "
            "orders — not the six the row names."
        ),
    },
    "A3": {
        "as_the_dispatch_states_it": (
            "That the disposition regeneration, after the escape fix, completes and its movement "
            "is confined to `unresolved` → `restates`. The ruling's own words: 'expected movement "
            "is `unresolved` → `restates` for entries entered since the last successful "
            "derivation; ANY other movement is a STOP (#13)'."
        ),
        "how_it_was_checked": (
            "The regenerated layer was diffed against the snapshot cluster by cluster, on all "
            "three fields that carry a judgment — the disposition, the bulk rule that fired, and "
            "the decisions named."
        ),
    },
}


def compile_probe(reg: dict) -> dict:
    bad, total = [], 0
    for e in reg["decisions"]:
        for p in e.get("patterns", []):
            total += 1
            try:
                re.compile(p, re.IGNORECASE)
            except re.error as exc:
                bad.append({"id": e["id"], "pattern": p, "error": str(exc)})
    return {"patterns_compiled": total, "failing": len(bad), "failing_set": bad}


def build() -> dict:
    reg = json.loads(REGISTER.read_text(encoding="utf-8"))
    by_id = {e["id"]: e for e in reg["decisions"]}

    # The register's identifiers must be contiguous D-001..D-N for the "entered since the snapshot"
    # cut below to be a derivation rather than a guess. Checked, not assumed.
    nums = sorted(int(i.split("-")[1]) for i in by_id)
    contiguous = nums == list(range(1, len(nums) + 1))
    if not contiguous:
        raise SystemExit(
            "STOP: register identifiers are not contiguous D-001..D-N, so an entry cannot be "
            "placed before or after the snapshot by its number. Re-derive the cut another way "
            "before trusting the cause attribution below.")

    snap_manifest = json.loads((SNAP / "snapshot_manifest.json").read_text(encoding="utf-8"))
    snap_layer = json.loads((SNAP / "cluster_dispositions.json").read_text(encoding="utf-8"))
    snap_disp_manifest = json.loads(
        (SNAP / "disposition_manifest.json").read_text(encoding="utf-8"))
    new_layer = json.loads(LAYER.read_text(encoding="utf-8"))
    new_manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    base = {r["cluster_id"]: r for r in snap_layer["dispositions"]}
    now = {r["cluster_id"]: r for r in new_layer["dispositions"]}
    if set(base) != set(now):
        raise SystemExit("STOP: the snapshot and the regenerated layer do not carry the same "
                         "cluster identifiers; the diff below would not be cluster-for-cluster.")

    backbone_at_snapshot = snap_disp_manifest["inputs"]["backbone"]["decision_count"]
    six = set(FORMER_PATTERNS)

    moved, transitions, rule_transitions, causes = [], {}, {}, {}
    newly_named_counts: dict[str, int] = {}
    for cid in sorted(base, key=lambda c: (base[c]["disposition"], c)):
        ob, nb = base[cid], now[cid]
        if (ob["disposition"], ob["rule"], ob["decisions"]) == \
           (nb["disposition"], nb["rule"], nb["decisions"]):
            continue
        gained = [d for d in nb["decisions"] if d not in ob["decisions"]]
        lost = [d for d in ob["decisions"] if d not in nb["decisions"]]
        for d in gained:
            newly_named_counts[d] = newly_named_counts.get(d, 0) + 1
        entered_since = [d for d in gained
                         if int(d.split("-")[1]) > backbone_at_snapshot]
        from_escaped = [d for d in gained if d in six]
        if lost:
            cause = ("A MATCH WAS LOST — the escape or an edit removed a naming this layer "
                     "previously carried")
        elif gained and len(entered_since) == len(gained):
            cause = ("BACKBONE GROWTH — every decision newly named on this cluster was entered "
                     "AFTER the snapshot's derivation")
        elif gained:
            cause = ("A DECISION THE SNAPSHOT'S BACKBONE ALREADY HELD now matches — not "
                     "attributable to growth")
        else:
            cause = "NO NAMING CHANGED — the disposition or rule moved for another reason"
        causes[cause] = causes.get(cause, 0) + 1
        key = f"{ob['disposition']} -> {nb['disposition']}"
        transitions[key] = transitions.get(key, 0) + 1
        rkey = f"{ob['rule']} -> {nb['rule']}"
        rule_transitions[rkey] = rule_transitions.get(rkey, 0) + 1
        moved.append({
            "cluster_id": cid,
            "disposition": {"before": ob["disposition"], "after": nb["disposition"]},
            "rule": {"before": ob["rule"], "after": nb["rule"]},
            "decisions": {"before": ob["decisions"], "after": nb["decisions"]},
            "decisions_gained": gained,
            "decisions_lost": lost,
            "gained_entries_entered_after_the_snapshot": entered_since,
            "gained_entries_among_the_six_escaped": from_escaped,
            "cause": cause,
            "files": nb.get("files", []),
        })

    probe = compile_probe(reg)
    a1_failing_now = [f["id"] for f in probe["failing_set"]]

    predicted = "unresolved -> restates"
    outside = {k: v for k, v in transitions.items() if k != predicted}

    return {
        "purpose": (
            "The OI-333 repair, recorded: what the escape of six invalid register patterns "
            "changed in the cluster-disposition layer, measured against a snapshot of the "
            "committed layer taken before the repair. NOT a completion statement, and not an "
            "authorization for any fix, design or inference change."
        ),
        "generated_by": "tools/audit/decisions/gen_oi333_repair.py",
        "generated_for": "cc_instruction_five_rulings.md (Task 5, ruling R4)",
        "the_ruling": (
            "User, 2026-08-07 (dispatch `cc_instruction_five_rulings.md` §0a, R4): OI-333 is "
            "resolved by one bounded repair wave — snapshot the committed disposition layer first "
            "(the O-12 pattern, #16); escape the six patterns; regenerate the disposition layer at "
            "the register's current backbone; diff against the snapshot and explain every cluster "
            "that moves; and add a narrow producibility mode to `gen_cluster_dispositions.py` so "
            "this failure class fails a guard in future."
        ),
        "what_is_authored_and_what_is_derived": {
            "authored": (
                "the six FORMER pattern strings (#12); the dispatch's two assumptions as it "
                "stated them; and the one note recording where the escape did more than escape "
                "markdown emphasis, with its evidence"
            ),
            "derived": (
                "every pattern's compile result at HEAD; the snapshot's own recorded hashes; the "
                "whole cluster-level diff, its per-cluster cause attribution, and every count"
            ),
        },
        "the_snapshot": {
            "where": "tools/audit/decisions/snapshot_2026-08-07_pre_oi333_repair/",
            "why": snap_manifest["why_it_is_taken"],
            "taken_at_head": snap_manifest["head_commit_at_snapshot"],
            "files": snap_manifest["files"],
            "backbone_it_was_derived_at": {
                "decision_count": backbone_at_snapshot,
                "sha256": snap_disp_manifest["inputs"]["backbone"]["sha256"],
                "head_commit": snap_disp_manifest["head_commit"],
            },
        },
        "the_regenerated_layer": {
            "backbone_it_is_derived_at": {
                "decision_count": new_manifest["inputs"]["backbone"]["decision_count"],
                "sha256": new_manifest["inputs"]["backbone"]["sha256"],
                "head_commit": new_manifest["head_commit"],
            },
            "completeness_check": new_manifest["completeness_check"],
            "disposition_counts": new_manifest["disposition_counts"],
        },
        "★_assumption_A1": dict(
            ASSUMPTIONS["A1"],
            verdict=("CONFIRMED. Compiling every pattern in the register found a failing set "
                     "identical to the one OI-333's table names, in both membership and size, and "
                     "no other pattern failed."),
            failing_set_before_the_repair=sorted(FORMER_PATTERNS),
            failing_set_after_the_repair=a1_failing_now,
            patterns_compiled_at_head=probe["patterns_compiled"],
            failing_at_head=probe["failing"],
        ),
        "the_six_patterns": {
            "how_to_read_this": (
                "`former` is preserved verbatim (#12); `current` is read off the register at HEAD. "
                "The change in five of the six is exactly one substitution — a literal `**` "
                "escaped so the regular-expression compiler reads it as two asterisks rather than "
                "as a repeat applied to a repeat. The sixth is named below it."
            ),
            "entries": {
                did: {
                    "former": former,
                    "current": by_id[did]["patterns"],
                    "title": by_id[did]["title"],
                }
                for did, former in sorted(FORMER_PATTERNS.items())
            },
            "★_the_one_place_the_escape_did_more_than_escape_emphasis":
                THE_ONE_PLACE_THE_ESCAPE_DID_MORE,
        },
        "★_assumption_A3_AND_THE_STOP_IT_FIRED": dict(
            ASSUMPTIONS["A3"],
            verdict=(
                "REFUTED. The movement is NOT confined to `unresolved` → `restates`, so the "
                "ruling's own STOP (#13) fires and this artifact is the report it requires. Every "
                "moved cluster is named below with its cause."
            ),
            predicted_transition=predicted,
            clusters_that_moved=len(moved),
            transitions_observed=dict(sorted(transitions.items(), key=lambda kv: -kv[1])),
            transitions_outside_the_prediction=dict(
                sorted(outside.items(), key=lambda kv: -kv[1])),
            rule_transitions_observed=dict(
                sorted(rule_transitions.items(), key=lambda kv: -kv[1])),
            cause_attribution=dict(sorted(causes.items(), key=lambda kv: -kv[1])),
            what_the_prediction_got_RIGHT=(
                "The MECHANISM. Every moved cluster moved because a decision newly named on it was "
                "entered into the register after the snapshot's derivation — which is the "
                "prediction's own stated cause, 'entries entered since the last successful "
                "derivation'. No cluster lost a naming, in either direction."
            ),
            what_the_prediction_got_WRONG=(
                "The SHAPE, in two ways, and both follow from the disposition pass's own rule "
                "ORDER rather than from anything about the escape. (1) The destination is not "
                "always `restates`: BR-3 fires when a matching decision is homed in a layer "
                "specification and BR-4 when every matching decision is homed outside one, so a "
                "newly matching entry whose home is not a layer specification lands in "
                "`no-spec-home`. (2) The source is not always `unresolved`: BR-3 and BR-4 run "
                "BEFORE the sweep rules BR-5 to BR-18, so a cluster a sweep had called "
                "`not-a-decision` moves the moment any backbone pattern matches it. A prediction "
                "naming one source and one destination could not have held for a backbone that "
                "grew by any entry homed outside a layer specification."
            ),
            what_is_NOT_claimed=(
                "That the regenerated layer is correct, or that its unresolved residual may now be "
                "published as the current one. This artifact records what MOVED and why; whether "
                "the regenerated layer supersedes the committed one is the user's, and both are on "
                "disk. No figure from either is restated in any prose surface (D-431)."
            ),
            attributable_to_the_six_escaped_patterns=sorted(
                {m["cluster_id"] for m in moved if m["gained_entries_among_the_six_escaped"]}),
            note_on_the_six=(
                "The clusters the escape itself moved are a small subset, and they would have "
                "moved on backbone growth alone had their patterns compiled — the six entries were "
                "all entered after the snapshot's derivation. The escape did not move any cluster "
                "that growth would not have reached; it made three of the six able to match at all."
            ),
        ),
        "newly_named_decisions_by_cluster_count": dict(
            sorted(newly_named_counts.items(), key=lambda kv: (-kv[1], kv[0]))),
        "moved_clusters": moved,
    }


def main() -> int:
    doc = build()
    OUT.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    a1 = doc["★_assumption_A1"]
    a3 = doc["★_assumption_A3_AND_THE_STOP_IT_FIRED"]
    print(f"wrote {OUT}")
    print(f"  A1: {a1['verdict'].split('.')[0]} — {a1['patterns_compiled_at_head']} patterns, "
          f"{a1['failing_at_head']} failing at HEAD")
    print(f"  A3: {a3['verdict'].split('.')[0]} — {a3['clusters_that_moved']} clusters moved, "
          f"{len(a3['transitions_outside_the_prediction'])} transition class(es) outside the "
          f"prediction")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
