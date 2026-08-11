#!/usr/bin/env python3
"""THE FOURTH IN-WORDS-CLOSURE ROW — its opening token corrected, decided BOTH WAYS first.

WHY THIS EXISTS.  `OPEN_ITEMS.md` OI-367 records a row whose status cell states its own closure in
words while opening with an open-state token, so every derivation over the index counts it OPEN
while its own text says otherwise.  It is the fourth member of the family OI-361 named, and the
pass that enumerated that family found three and missed this one — its pattern was never measured
against the openings the index actually uses.

WHAT THE USER RULED.  Ruling 53 of `cowork_rulings_2026_08_11_eleventh_stop.md`: the row's opening
token is corrected PER ITS OWN CELL'S WORDS, under the both-ways discipline — every index row
decided before and after, the named row the only permitted mover, any other movement a STOP.
OI-367 flips on it, and the enumeration gap is recorded on that row itself.

WHY A BOTH-WAYS TABLE RATHER THAN A DIFF OF THE RESULT.  Ruling 25 attached that condition to a
remedy and the condition is what refuted it: a report derived from the corrected tree alone can
only say what the tree looks like afterwards.  This file computes BOTH states itself — every row at
the baseline commit and every row at this tree — so a movement is MEASURED rather than asserted,
and any movement outside the one named correction halts the pass before it writes.

WHY THE BASELINE IS A GIT OBJECT.  A pass that took its own BEFORE half from the working tree could
be run exactly once: a second run would report the tree it had itself just changed and destroy the
record it exists to keep.  Reading the baseline from a content-addressed object makes this record
RE-DERIVABLE, and it is the sanctioned form of shell read — read-only, by explicit commit hash
(D-253).  The fifth continuation's normalization pass established that shape and this follows it
(#6).

WHAT THIS IS.  A POINT-IN-TIME RECORD of one correction, in the class the 2026-08-04 ruling R4
defines: it records a measurement taken at a moment rather than a live invariant, so it carries no
re-derivation mode and does not belong in the guard population.  The STANDING enforcement is
`tools/audit/index_status_lint.py`, whose vocabulary, row split and leading-token function this
file imports rather than restating (#6).

Run:
    python tools/audit/gen_oi367_opening_correction.py

Output:
    tools/audit/oi367_opening_correction.json
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
INDEX = os.path.join(ROOT, "OPEN_ITEMS.md")
OUT = os.path.join(HERE, "oi367_opening_correction.json")

sys.path.insert(0, HERE)
from output_encoding import use_utf8_output      # noqa: E402  (path set above)
from index_status_lint import (                  # noqa: E402  (path set above)
    CANONICAL, RESOLVED_MARK, ROW, leading_token, split_row,
)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

# ── The one correction this pass is allowed to make, NAMED IN ADVANCE ────────────────────────
# The ruling names the row by description — the fourth in-words-closure row — and fixes the target
# state by the cell's OWN WORDS rather than by any judgment of this pass. A row named here that
# does NOT move is a STOP too: the correction is a prediction and it is checked in both directions
# (#17b).
NAMED_CORRECTION = {
    "OI-298": ("resolved",
               "OI-367's subject, and the fourth member of the OI-361 family. The status cell "
               "opens `OPEN — ` and continues `★ RESOLVED 2026-08-03 (CC, phase 1v) — the user "
               "ruled …`, then records that closure in full in six numbered acts with their "
               "provenance; `CLAUDE.md`'s phase-2 clause says of the same subject that the gap it "
               "closed WAS tracked at this row. The cell's own words state a closure, so the "
               "opening token is stale and the row is RESOLVED. Nothing about the row's CONTENT "
               "is re-read here: the target state is taken from the cell's own words, which is "
               "what Ruling 53 fixes it by."),
}

# ── Rows this same commit RESOLVES, which is a different act from correcting an opening ──────
# The baseline is the commit before this one, so a row this commit FLIPS shows as a state movement
# in the table. A resolution is not an opening correction and must not be hidden inside one: it is
# listed here with the act that made it, and the gate treats it apart. A flip not listed here is
# still a STOP. (The shape is the fifth continuation's, kept identical on purpose, #6.)
RESOLUTIONS_IN_THE_SAME_COMMIT = {
    "OI-367": "Flipped RESOLVED by the same act: this row's whole subject is the correction "
              "above, so it closes in the commit that applies it. The flip is a resolution, not "
              "an opening correction.",
}

BASELINE_COMMIT = "464e6e3752"      # the commit this pass's own commit follows
BASELINE_NOTE = ("The last commit before this correction: the tenth continuation's closing "
                 "self-check catch. Its index is the BEFORE half of every state below.")

CANONICAL_OPENING = {"open": "OPEN — ", "resolved": RESOLVED_MARK + " RESOLVED — "}


def index_lines() -> list[str]:
    with open(INDEX, encoding="utf-8") as fh:
        return fh.read().splitlines()


def baseline_lines() -> list[str]:
    out = subprocess.run(["git", "show", f"{BASELINE_COMMIT}:OPEN_ITEMS.md"],
                         cwd=ROOT, capture_output=True)
    if out.returncode != 0:
        raise SystemExit(f"STOP: the baseline object {BASELINE_COMMIT}:OPEN_ITEMS.md is not "
                         f"readable — a missing object is a staleness signal, never something to "
                         f"guess around (D-253). git said: {out.stderr.decode(errors='replace')}")
    return out.stdout.decode("utf-8").splitlines()


def states_at(lines: list[str]) -> tuple[dict[str, str], dict[str, str], list[dict]]:
    """(state per row under the canonical rule, status cell per row, malformed rows)."""
    states, cells_by_id, malformed = {}, {}, []
    for lineno, ln in enumerate(lines, 1):
        if not ROW.match(ln):
            continue
        cells = split_row(ln)
        if len(cells) != 6:
            malformed.append({"line": lineno, "cells_found": len(cells),
                              "id": cells[0] if cells else None, "row_opening": ln[:160]})
            continue
        tok = leading_token(cells[4])
        states[cells[0]] = None if tok is None else CANONICAL[tok]
        cells_by_id[cells[0]] = cells[4]
    return states, cells_by_id, malformed


def corrected_status(row_id: str, status: str) -> str:
    """The corrected form of one status cell — the fifth continuation's own construction (#6).

    The stale opening token is REPLACED rather than prefixed, because prefixing would leave a cell
    reading `RESOLVED — OPEN — …`. Nothing else in the cell is touched: every word of its text
    survives, including the closure statement the correction is taken from (#12).
    """
    if row_id not in NAMED_CORRECTION:
        return status
    target = NAMED_CORRECTION[row_id][0]
    tok = leading_token(status)
    if tok is not None and CANONICAL[tok] == target:
        return status
    if tok is not None:
        rest = status.lstrip()[len(tok):].lstrip()
        rest = re.sub(r"^[—\-–:;,]\s*", "", rest)
        return CANONICAL_OPENING[target] + rest
    return CANONICAL_OPENING[target] + status.lstrip()


def main() -> int:
    lines = index_lines()
    baseline_states, baseline_cells, malformed_before = states_at(baseline_lines())

    if malformed_before:
        raise SystemExit("STOP: the baseline index carries a row that does not split — the "
                         "both-ways table would be computed over an incomplete population: "
                         f"{malformed_before}")

    table, out_lines = [], []
    for lineno, ln in enumerate(lines, 1):
        if not ROW.match(ln):
            out_lines.append(ln)
            continue
        cells = split_row(ln)
        if len(cells) != 6:
            raise SystemExit(f"STOP: a row at this tree does not split (line {lineno}, "
                             f"{len(cells)} cells). Every row is decided in this table or none "
                             f"is.")
        row_id, status = cells[0], cells[4]
        new_status = corrected_status(row_id, status)
        before = baseline_states.get(row_id)
        after_tok = leading_token(new_status)
        after = None if after_tok is None else CANONICAL[after_tok]
        table.append({
            "id": row_id,
            "state_at_the_baseline": before if before is not None
            else "ABSENT — the row is added by this act, or its baseline opening was not canonical",
            "state_at_this_tree": after,
            "moves": before is not None and before != after,
            "canonical_token_before": leading_token(baseline_cells.get(row_id, status)),
            "canonical_token_after": after_tok,
            "the_cell_changed_from_the_baseline":
                row_id in baseline_cells and baseline_cells[row_id] != new_status,
            "status_cell_opening_before": baseline_cells.get(row_id, status)[:140],
            "status_cell_opening_after": new_status[:140],
        })
        if new_status != status:
            cells[4] = new_status
            ln = "| " + " | ".join(cells) + " |"
        out_lines.append(ln)

    unresolved = [t["id"] for t in table if t["state_at_this_tree"] is None]
    if unresolved:
        raise SystemExit("STOP: rows with no canonical opening at this tree: "
                         + ", ".join(unresolved))

    movers = [t for t in table if t["moves"]]
    resolved_in_act = [t for t in movers if t["id"] in RESOLUTIONS_IN_THE_SAME_COMMIT]
    movers = [t for t in movers if t["id"] not in RESOLUTIONS_IN_THE_SAME_COMMIT]
    unexpected = [t["id"] for t in movers if t["id"] not in NAMED_CORRECTION]
    if unexpected:
        raise SystemExit("STOP: state movements the ruling does not name: " + ", ".join(unexpected)
                         + " — the pass is NOT applied.")
    predicted_but_still = [i for i in NAMED_CORRECTION
                           if i not in {t["id"] for t in movers}]
    if predicted_but_still:
        raise SystemExit("STOP: a named correction did not move: " + ", ".join(predicted_but_still)
                         + " — the prediction is checked in both directions and this is the "
                           "direction that is silent when it fails.")
    missing_resolutions = [i for i in RESOLUTIONS_IN_THE_SAME_COMMIT
                           if i not in {t["id"] for t in resolved_in_act}]
    if missing_resolutions:
        raise SystemExit("STOP: a row named as resolved by this same commit did not move: "
                         + ", ".join(missing_resolutions) + " — the flip must be applied to the "
                         "index before this pass runs, so that the movement is measured here "
                         "rather than in a later act that does not account for it.")

    artifact = {
        "what_this_is": "Every open-items index row decided BOTH WAYS — at the baseline commit and "
                        "at this tree — so that the one opening correction the user's Ruling 53 "
                        "licenses is measured rather than asserted, and any other movement halts "
                        "the pass. A point-in-time record (the 2026-08-04 ruling R4 class): "
                        "re-deriving it after the act would destroy the before half it exists to "
                        "record.",
        "generated_by": "tools/audit/gen_oi367_opening_correction.py",
        "the_ruling": "Ruling 53 of `cowork_rulings_2026_08_11_eleventh_stop.md`: the fourth "
                      "in-words-closure row's opening token is corrected per its own cell's "
                      "words, under the both-ways discipline — every index row decided before and "
                      "after, the named row the only permitted mover, any other movement a STOP. "
                      "OI-367 flips on it; the enumeration gap that missed the row is recorded on "
                      "the row itself.",
        "the_row_it_answers": "OPEN_ITEMS.md OI-367",
        "the_baseline_the_before_half_is_read_from": {
            "commit": BASELINE_COMMIT,
            "path": "OPEN_ITEMS.md",
            "note": BASELINE_NOTE,
            "why_a_git_object_rather_than_the_working_tree":
                "A pass that read its own BEFORE half from the working tree could be run exactly "
                "once: a second run would report the tree it had itself just changed and destroy "
                "the record it exists to keep. Reading the baseline from a content-addressed "
                "object makes this record RE-DERIVABLE, and it is the sanctioned form of shell "
                "read — read-only, by explicit commit hash (D-253).",
        },
        "the_rule_both_halves_are_decided_under": "The canonical status discipline (D-662): a "
                                                  "row's state is the first token of its status "
                                                  "cell and nothing else. BOTH halves are decided "
                                                  "under it, because it is the rule live at HEAD "
                                                  "and the correction does not amend it — what "
                                                  "moves is one cell, not the reading.",
        "the_named_correction": {k: {"target_state": v[0], "why": v[1]}
                                 for k, v in NAMED_CORRECTION.items()},
        "how_the_correction_edits": "The stale opening token is REPLACED rather than prefixed, "
                                    "because prefixing would leave a cell reading `RESOLVED — "
                                    "OPEN — …`. It is the fifth continuation's own construction, "
                                    "imported in shape rather than re-invented (#6). No other "
                                    "text in the cell is touched, and the closure statement the "
                                    "correction is taken FROM survives in place (#12).",
        "what_this_pass_does_not_decide": "Whether the row's recorded closure is CORRECT. Ruling "
                                          "53 fixes the target state by the cell's own words, and "
                                          "this pass reads those words rather than re-adjudicating "
                                          "the six acts the cell records. The lint's own scope "
                                          "clause says the same thing from the other side: it "
                                          "checks that a state is STATED in a form every "
                                          "derivation reads alike, never that the state is right.",
        "counts": {
            "rows_parsed": len(table),
            "rows_malformed_at_the_baseline": len(malformed_before),
            "cells_changed": sum(1 for t in table if t["the_cell_changed_from_the_baseline"]),
            "state_movements_that_are_this_correction": len(movers),
            "state_movements_that_are_resolutions_in_the_same_commit": len(resolved_in_act),
        },
        "state_movements": [{"id": t["id"], "from": t["state_at_the_baseline"],
                             "to": t["state_at_this_tree"],
                             "named_in_advance": t["id"] in NAMED_CORRECTION,
                             "why": NAMED_CORRECTION.get(t["id"], (None, None))[1]}
                            for t in movers],
        "rows_this_same_commit_RESOLVES_which_is_a_different_act": {
            "what": "The baseline is the commit before this one, so a row this commit FLIPS shows "
                    "as a state movement in the table. A resolution is not an opening correction "
                    "and is not hidden inside one: these are listed apart, with the act that made "
                    "each, and a flip not listed here is still a STOP.",
            "rows": [{"id": t["id"], "from": t["state_at_the_baseline"],
                      "to": t["state_at_this_tree"],
                      "why": RESOLUTIONS_IN_THE_SAME_COMMIT[t["id"]]}
                     for t in resolved_in_act],
        },
        "the_population_movement_this_act_accounts_for": {
            "what": "Correcting the opening moves the row from the OPEN population to the "
                    "RESOLVED one, which moves the open-row count, the TRUE-half cuts, the finish "
                    "line's populations and the apparatus declaration's candidate cut.",
            "why_it_is_named_here": "OI-367's own row states the precedent it inherits from "
                                    "OI-362: a population movement belongs to an act that "
                                    "accounts for it, not to a task that would slip it in "
                                    "unremarked. This pass is that act, and the movement is named "
                                    "in advance, applied under a ruling, and recorded here.",
            "what_is_regenerated_because_of_it": "Every derivation over the index — the apparatus "
                                                 "declaration, the completion inventory, the "
                                                 "finish line and the reach derivation that reads "
                                                 "them — is regenerated in the same commit, so no "
                                                 "surface carries the pre-correction population.",
        },
        "every_row": table,
    }
    open(OUT, "w", encoding="utf-8", newline="").write(
        json.dumps(artifact, indent=2, ensure_ascii=False) + "\n")

    with open(INDEX, "w", encoding="utf-8", newline="") as fh:
        fh.write("\n".join(out_lines) + "\n")

    print(f"wrote {os.path.relpath(OUT, ROOT)} and corrected {os.path.relpath(INDEX, ROOT)}")
    print(f"  rows parsed {len(table)}")
    print(f"  state movements (this correction): {[t['id'] for t in movers]}")
    print(f"  state movements (resolutions in this commit): "
          f"{[t['id'] for t in resolved_in_act]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
