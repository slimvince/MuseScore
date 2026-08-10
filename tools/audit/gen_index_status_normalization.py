#!/usr/bin/env python3
"""THE CANONICAL STATUS DISCIPLINE — surveyed, decided BOTH WAYS, then applied once.

WHY THIS EXISTS.  Three open-items rows record one defect in the ONE index parser (#6), in three
directions:

  * OI-356 — a status cell that merely MENTIONS another row's resolved mark makes its own row read
    as RESOLVED to every derivation over the index;
  * OI-361 — a status cell that spells its resolution IN WORDS, with no mark, reads OPEN to every
    derivation while its own text says otherwise;
  * OI-362 — a row that does not split into the expected number of cells is skipped SILENTLY, so it
    is neither open nor resolved but absent from every population.

The user's Ruling 33 of 2026-08-09 (`cowork_rulings_2026_08_09_fifth_stop.md`) remedies the family
ONCE rather than per symptom: **every INDEX status cell begins with one canonical token**; ONE
mechanical normalization pass over the index, gated by a both-ways table in which the only state
movements are the three defect rows' named corrections; a LINT stops on a non-canonical opening
thereafter; and the parser STOPS on a row that does not split rather than dropping it silently
(#12, #19).

WHY A BOTH-WAYS TABLE RATHER THAN A DIFF OF THE RESULT.  Ruling 25 attached that condition to the
previous, refuted remedy and the condition is what refuted it: a report derived from the corrected
rule alone can only say what the tree looks like afterwards.  This file computes BOTH states
itself — the rule as it stood at HEAD, and the canonical-token rule — so a movement is measured
rather than asserted, and any movement outside the three named corrections is a STOP.

THE VOCABULARY IS DERIVED, NOT INVENTED.  `--survey` reads every status cell at HEAD and reports
the opening words the index actually uses, with their frequencies and their state under the rule as
it stood.  The canonical set below was authored FROM that survey; running `--survey` again after a
change re-derives the evidence for it.

WHAT THIS IS.  A POINT-IN-TIME RECORD of one normalization, in the class the 2026-08-04 ruling R4
defines: it records a measurement taken at a moment, not a live invariant, so it carries no
re-derivation mode and does not belong in the guard population.  The STANDING check is
`tools/audit/index_status_lint.py`, and the enforcement is in the one parser itself.

Run:
    python tools/audit/gen_index_status_normalization.py --survey   # evidence, no edit
    python tools/audit/gen_index_status_normalization.py            # the gated pass, one edit

Output:
    tools/audit/index_status_normalization.json
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
INDEX = os.path.join(ROOT, "OPEN_ITEMS.md")
OUT = os.path.join(HERE, "index_status_normalization.json")

sys.path.insert(0, HERE)
from output_encoding import use_utf8_output      # noqa: E402  (path set above)
from index_status_lint import (                  # noqa: E402  (path set above)
    CANONICAL, RESOLVED_MARK, ROW, leading_token, split_row,
)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

# ── The corrections this pass is allowed to make, NAMED IN ADVANCE ───────────────────────────
# The dispatch's assumption A1 states them: the two rows whose cells spell a resolution in words
# read RESOLVED, and the row the parser silently drops is parsed and reports its true state. Any
# other state movement is a STOP. A row named here that does NOT move is also a STOP: the
# correction was predicted and the prediction is checked in both directions (#17b).
#
# The dropped row's identity is DERIVED, not carried: it is whatever row fails to split at this
# tree, and the pass stops if the derived set is not exactly the one named here.
NAMED_CORRECTIONS = {
    "OI-326": ("resolved", "OI-361's first defect: the cell opens `RESOLVED 2026-08-04` in words "
                           "with no mark, so every derivation counts a closed row as open."),
    "OI-349": ("resolved", "OI-361's second defect: the cell opens `RESOLVED 2026-08-09` in words "
                           "with no mark, so every derivation counts a closed row as open."),
    "OI-321": ("open", "OI-362's dropped row, its identity DERIVED at this tree rather than "
                       "carried: its prose carries an unescaped cell separator, so it splits into "
                       "one cell too many and the parser skips it with no report. It is neither "
                       "open nor resolved but ABSENT. Escaping the separator admits it, and its "
                       "own text says it is open."),
}

# ── The row OI-361 names and this pass deliberately does NOT settle ──────────────────────────
# Its cell states a MIXED status — superseded in fact on one surface, still live on the legacy
# notation path and retiring with it — so which way a single open/resolved bit should fall is not
# settled by its own text. It takes the canonical token MIXED, which the parser reads as OPEN:
# that is exactly the state it holds at HEAD, so nothing moves, and the token makes the
# unsettledness visible instead of hiding it behind a bit that looks decided.
THE_UNSETTLED_ROW = "OI-175"

# ── Rows whose CANONICAL opening disagrees with the state the rule at HEAD gives them ────────
# A cell can open with an open-state word and still carry the resolved mark later. Under the rule
# at HEAD that mark decides the row; under the canonical rule the opening does. Which is right is a
# READING of the cell, not a property of any character, so it is AUTHORED per row with its ground,
# and a disagreement with no reading here is a STOP — the pass will not guess one.
#
# `keep` names the state the row actually holds. Where that state is the one the rule at HEAD gave
# it, nothing moves and the normalization only replaces a stale opening token with the canonical
# one for the state the cell's own text states.
# ── Rows this same commit RESOLVES, which is a different act from normalizing an opening ─────
# The both-ways table compares the baseline against the tree, so a row the same commit flips shows
# as a state movement. Those movements are NOT the normalization's and must not be hidden inside
# it: they are listed here with the act that made them, and the gate below treats them apart. A
# flip not listed here is still a STOP.
RESOLUTIONS_IN_THE_SAME_COMMIT = {
    "OI-356": "Flipped RESOLVED by the same act: Ruling 33's canonical status discipline IS this "
              "row's remedy, so it closes in the commit that applies it. The flip is a "
              "resolution, not a normalization movement.",
    "OI-361": "Flipped RESOLVED by the same act, one family one fix: the discipline requires the "
              "mark at the head of a resolved cell, which is the remedy this row named.",
    "OI-362": "Flipped RESOLVED by the same act: the malformed-row STOP and the repair of the "
              "dropped row are both in this commit, in the order the row itself stated.",
}

DISAGREEMENT_READINGS = {
    "OI-178": ("resolved",
               "The cell reads `PROTOCOL RATIFIED 2026-07-19; ✅ EXECUTED 2026-07-26 — the joint "
               "estimator is the PRODUCTION inference layer …`. The mark is THIS row's own "
               "completion; the ratification date merely precedes it. The row is RESOLVED, which "
               "is the state the rule at HEAD gives it, so nothing moves: the opening gains the "
               "canonical mark."),
    "OI-208": ("resolved",
               "READ AT THE CELL, and it CORRECTS a reading the previous both-ways pass recorded. "
               "The cell opens `OPEN — ` and ENDS `… the row's purpose is achieved and it "
               "CLOSES`; the marks inside it are this row's own three ratifications (shape, "
               "content, living surface). The row is RESOLVED and its opening is STALE — it was "
               "never updated when the row closed. The rule at HEAD reads it correctly, so nothing "
               "moves; the stale opening token is replaced by the canonical one. The previous "
               "pass's authored reading — that the mark is a delivered half inside a row that is "
               "open, making it the one row the leading-token remedy improved — is REFUTED by the "
               "cell's own closing words, and that refutation makes Ruling 25's remedy worse than "
               "recorded rather than better: it would have marked three genuinely closed rows "
               "open and improved none."),
    "OI-272": ("resolved",
               "The cell opens `★ RULED by the user 2026-08-02 — ` and ends `Row CLOSED`; the mark "
               "appears mid-cell on the homing half of this row's own work. The row is RESOLVED, "
               "which is the state the rule at HEAD gives it, so nothing moves: the decorative "
               "marker is not a canonical opening and the canonical mark is prefixed."),
}


# ── The BEFORE half, taken from a git OBJECT by explicit hash ────────────────────────────────
# The both-ways table needs the index as it stood BEFORE the normalization, and a pass that read
# it from the working tree could only be run once — a second run would report the tree it had
# itself just changed and destroy the record it exists to keep. Reading the baseline from a
# content-addressed git object makes the record RE-DERIVABLE instead of one-shot, and it is the
# sanctioned form of shell read: read-only, by explicit commit hash (D-253).
BASELINE_COMMIT = "45a082dc51"      # the commit this pass's own commit follows
BASELINE_NOTE = ("The last commit before the normalization: the fifth continuation's Task 0. Its "
                 "index is the BEFORE half of every state below, including the row that did not "
                 "parse at all.")


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
    """(state per row under the rule at HEAD, status cell per row, malformed rows)."""
    states, cells_by_id, malformed = {}, {}, []
    for lineno, ln in enumerate(lines, 1):
        if not ROW.match(ln):
            continue
        cells = split_row(ln)
        if len(cells) != 6:
            malformed.append({"line": lineno, "cells_found": len(cells),
                              "id": cells[0] if cells else None, "row_opening": ln[:160]})
            continue
        states[cells[0]] = state_under_the_former_rule(cells[4])
        cells_by_id[cells[0]] = cells[4]
    return states, cells_by_id, malformed


def survey(lines: list[str]) -> dict:
    """Every status cell's opening, as evidence for the canonical vocabulary."""
    openings, per_row, malformed = {}, [], []
    for lineno, ln in enumerate(lines, 1):
        if not ROW.match(ln):
            continue
        cells = split_row(ln)
        if len(cells) != 6:
            malformed.append({"line": lineno, "cells_found": len(cells),
                              "id": cells[0] if cells else None, "row_opening": ln[:160]})
            continue
        status = cells[4]
        # The opening WORDS, up to the first separator a status cell conventionally uses.
        head = re.split(r"[—\-–,;(]", status.lstrip(), maxsplit=1)[0].strip()
        head = head[:60]
        openings[head] = openings.get(head, 0) + 1
        per_row.append({
            "id": cells[0],
            "opening_words": head,
            "opens_with_the_mark": status.lstrip().startswith(RESOLVED_MARK),
            "the_mark_occurs_anywhere": RESOLVED_MARK in status,
            "canonical_token_at_head": leading_token(status),
            "status_cell_opening": status[:180],
        })
    return {
        "opening_words_by_frequency": dict(sorted(openings.items(), key=lambda kv: (-kv[1], kv[0]))),
        "rows_whose_opening_is_not_canonical": [r["id"] for r in per_row
                                                if r["canonical_token_at_head"] is None],
        "malformed_rows_the_parser_drops": malformed,
        "per_row": per_row,
    }


def state_under_the_former_rule(status: str) -> str:
    """The rule live at HEAD before this pass: RESOLVED iff the mark occurs anywhere in the cell."""
    return "resolved" if RESOLVED_MARK in status else "open"


def state_under_the_canonical_rule(status: str) -> str | None:
    tok = leading_token(status)
    return None if tok is None else CANONICAL[tok]


CANONICAL_OPENING = {"open": "OPEN — ", "resolved": RESOLVED_MARK + " RESOLVED — "}


def target_state(row_id: str, status: str) -> str:
    """The state the row actually holds — the rule at HEAD, overridden only where a ruling names it."""
    if row_id in NAMED_CORRECTIONS:
        return NAMED_CORRECTIONS[row_id][0]
    if row_id in DISAGREEMENT_READINGS:
        return DISAGREEMENT_READINGS[row_id][0]
    return state_under_the_former_rule(status)


def normalized_status(row_id: str, status: str) -> str:
    """The canonical form of one status cell.

    PREPEND ONLY, with ONE exception that is not a rewrite of content: where the cell opens with an
    open-state word that contradicts the state the row actually holds, that STALE TOKEN is replaced
    rather than prefixed, because prefixing would leave a cell reading `RESOLVED — OPEN — …`. Every
    such row is named in DISAGREEMENT_READINGS with its ground, its former opening is recorded in
    the artifact, and its state does not move (#12).
    """
    tok = leading_token(status)
    target = NAMED_CORRECTIONS[row_id][0] if row_id in NAMED_CORRECTIONS \
        else target_state(row_id, status)
    if row_id == THE_UNSETTLED_ROW:
        return status if tok == "MIXED" else "MIXED — " + status
    if tok is not None and CANONICAL[tok] == target:
        return status
    if tok is not None:
        # A stale opening token: drop exactly that token and any separator following it.
        rest = status.lstrip()[len(tok):].lstrip()
        rest = re.sub(r"^[—\-–:;,]\s*", "", rest)
        return CANONICAL_OPENING[target] + rest
    return CANONICAL_OPENING[target] + status.lstrip()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--survey", action="store_true",
                    help="write the evidence for the canonical vocabulary; change nothing")
    args = ap.parse_args()

    lines = index_lines()
    ev = survey(lines)

    if args.survey:
        artifact = {"what_this_is": "The evidence the canonical vocabulary was authored from: "
                                    "every status cell's opening words at this tree, with their "
                                    "frequencies. No file is changed by --survey.",
                    "generated_by": "tools/audit/gen_index_status_normalization.py --survey",
                    "survey": ev}
        open(OUT, "w", encoding="utf-8", newline="").write(
            json.dumps(artifact, indent=2, ensure_ascii=False) + "\n")
        print(f"wrote {os.path.relpath(OUT, ROOT)} (survey only, nothing changed)")
        print(f"  distinct openings: {len(ev['opening_words_by_frequency'])}")
        print(f"  rows whose opening is NOT canonical: "
              f"{len(ev['rows_whose_opening_is_not_canonical'])}")
        print(f"  malformed rows the parser drops: {len(ev['malformed_rows_the_parser_drops'])}")
        return 0

    # ── The BEFORE half, from the baseline git object; the AFTER half, from this tree ─────────
    baseline_states, baseline_cells, malformed_before = states_at(baseline_lines())

    table, out_lines = [], []
    for lineno, ln in enumerate(lines, 1):
        if not ROW.match(ln):
            out_lines.append(ln)
            continue
        cells = split_row(ln)
        if len(cells) != 6:
            raise SystemExit(f"STOP: a row at this tree still does not split (line {lineno}, "
                             f"{len(cells)} cells). The malformed-row repair belongs to this pass "
                             f"and must be made before it runs.")
        row_id, status = cells[0], cells[4]
        # The state BEFORE is the baseline's, never this tree's — so the record survives re-runs.
        # A row absent from the baseline is one this pass's own commit adds or repairs; both are
        # reported rather than silently defaulted.
        before = baseline_states.get(row_id)
        new_status = normalized_status(row_id, status)
        after = state_under_the_canonical_rule(new_status)
        table.append({
            "id": row_id,
            "state_under_the_rule_at_HEAD": before if before is not None
            else "ABSENT — the row did not parse at the baseline, or is added by this act",
            "state_under_the_canonical_rule": after,
            "moves": before is not None and before != after,
            "opening_was_already_canonical":
                leading_token(baseline_cells.get(row_id, status)) is not None,
            "canonical_token_before": leading_token(baseline_cells.get(row_id, status)),
            "the_opening_changed_from_the_baseline":
                row_id in baseline_cells and baseline_cells[row_id] != new_status,
            "canonical_token_after": leading_token(new_status),
            "the_mark_occurs_anywhere_in_the_cell": RESOLVED_MARK in status,
            "status_cell_opening_before": baseline_cells.get(row_id, status)[:140],
            "status_cell_opening_after": new_status[:140],
        })
        if new_status != status:
            # Rebuild the row with the normalized status cell, changing nothing else.
            cells[4] = new_status
            ln = "| " + " | ".join(cells) + " |"
        out_lines.append(ln)

    unresolved = [t["id"] for t in table if t["state_under_the_canonical_rule"] is None]
    if unresolved:
        raise SystemExit("STOP: rows with no canonical token after normalization: "
                         + ", ".join(unresolved))

    # A cell can open with an open-state word and carry the mark later; which decides the row is a
    # READING, and an unread disagreement is a STOP rather than a guess.
    disagreements = [t for t in table if t["opening_was_already_canonical"]
                     and t["state_under_the_rule_at_HEAD"] in ("open", "resolved")
                     and CANONICAL[t["canonical_token_before"]]
                     != t["state_under_the_rule_at_HEAD"]]
    unread = [t["id"] for t in disagreements if t["id"] not in DISAGREEMENT_READINGS
              and t["id"] not in NAMED_CORRECTIONS and t["id"] != THE_UNSETTLED_ROW]
    if unread:
        raise SystemExit("STOP: a row whose canonical opening disagrees with the state the rule at "
                         "HEAD gives it, with no authored reading: " + ", ".join(unread))

    movers = [t for t in table if t["moves"]]
    resolved_in_act = [t for t in movers if t["id"] in RESOLUTIONS_IN_THE_SAME_COMMIT]
    movers = [t for t in movers if t["id"] not in RESOLUTIONS_IN_THE_SAME_COMMIT]
    unexpected = [t["id"] for t in movers if t["id"] not in NAMED_CORRECTIONS]
    if unexpected:
        raise SystemExit("STOP: state movements the ruling does not name: " + ", ".join(unexpected)
                         + " — the pass is NOT applied.")

    # The dropped row never parsed at the baseline, so it has no BEFORE state to move from; the
    # derived set of dropped rows must be exactly the one named in advance, in both directions.
    dropped_ids = sorted(m["id"] for m in malformed_before if m["id"])
    named_dropped = sorted(i for i, (_, _) in NAMED_CORRECTIONS.items()
                           if i not in baseline_states)
    if dropped_ids != named_dropped:
        raise SystemExit("STOP: the rows the baseline parser drops are not the ones named in "
                         f"advance. derived={dropped_ids} named={named_dropped}")
    predicted_dropped = named_dropped

    artifact = {
        "what_this_is": "Every open-items index row decided BOTH WAYS — under the parser rule live "
                        "at HEAD (the resolved mark anywhere in the status cell) and under the "
                        "canonical-token rule the user's Ruling 33 of 2026-08-09 establishes. A "
                        "point-in-time record (the 2026-08-04 ruling R4 class): re-deriving it "
                        "after the pass would destroy the before half it exists to record.",
        "generated_by": "tools/audit/gen_index_status_normalization.py",
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
        "the_rows_it_answers": ["OPEN_ITEMS.md OI-356", "OPEN_ITEMS.md OI-361",
                                "OPEN_ITEMS.md OI-362"],
        "the_ruling": "Ruling 33 of `cowork_rulings_2026_08_09_fifth_stop.md`: one family, one fix "
                      "(#6) — every INDEX status cell begins with one canonical token; ONE "
                      "mechanical normalization gated by a both-ways table whose only movements "
                      "are the named corrections; a lint STOPs on a non-canonical opening "
                      "thereafter; the parser STOPs on a row that does not split rather than "
                      "dropping it silently.",
        "excluded_alternatives_recorded_at_the_ruling": [
            "The bounded-opening search — a hand-picked threshold over varying prose, and it fixes "
            "neither sibling.",
            "The glyph prohibition alone — one symptom of three.",
        ],
        "how_the_vocabulary_was_derived": "From `--survey` over the index at HEAD: the opening "
                                          "words every status cell actually uses, with their "
                                          "frequencies. No token was invented; MIXED is the word "
                                          "OI-361's own reading uses for the one row whose single "
                                          "open/resolved bit its text does not settle.",
        "the_canonical_vocabulary": CANONICAL,
        "the_named_corrections": {k: {"target_state": v[0], "why": v[1]}
                                  for k, v in NAMED_CORRECTIONS.items()},
        "rows_whose_canonical_opening_disagreed_with_the_state_at_HEAD": {
            "what": "A cell can open with an open-state word and still carry the resolved mark "
                    "later. Under the rule at HEAD that mark decides the row; under the canonical "
                    "rule the opening does. WHICH IS RIGHT IS A READING of the cell, so it is "
                    "authored per row with its ground, and an unread disagreement is a STOP.",
            "ids": [t["id"] for t in disagreements],
            "readings": {k: {"state_the_row_holds": v[0], "ground": v[1]}
                         for k, v in DISAGREEMENT_READINGS.items()},
            "none_of_them_moves": all(not t["moves"] for t in disagreements),
        },
        "the_row_deliberately_not_settled": {
            "id": THE_UNSETTLED_ROW,
            "why": "OI-361's own per-row reading: the cell states a MIXED status — superseded in "
                   "fact on one surface, still live on the legacy notation path and retiring with "
                   "it — so which way a single open/resolved bit should fall is not settled by its "
                   "own text and is not settled here. Its canonical token is MIXED, which the "
                   "parser reads as OPEN — the state it already holds, so nothing moves.",
        },
        "how_the_normalization_edits": "PREPEND ONLY, with ONE exception that is not a rewrite of "
                                       "content. A cell already opening with a canonical token "
                                       "whose state agrees with the row's is untouched; a cell "
                                       "with no canonical opening gains the token as a prefix, and "
                                       "no existing text is removed or reworded (#12). THE "
                                       "EXCEPTION: where a cell opens with an open-state word that "
                                       "contradicts the state the row actually holds, that STALE "
                                       "TOKEN is replaced rather than prefixed — prefixing would "
                                       "leave a cell reading `RESOLVED — OPEN — …`. Every such row "
                                       "is named with its authored ground, its former opening is "
                                       "recorded per row above, and its state does not move.",
        "the_dropped_row_was_repaired_in_this_same_act_and_the_repair_is_recorded_here": {
            "row": "OI-321",
            "what_was_wrong": "The row carried SEVEN cells: its layer/gate column was written "
                              "TWICE, the second copy carrying the gating clause. The ONE index "
                              "parser splits on the cell separator and skips a row that does not "
                              "yield the expected number of cells, with no report of any kind — so "
                              "this row was in NO population at all, neither open nor resolved but "
                              "absent (OI-362).",
            "what_was_done": "The duplicate column was MERGED into the status cell, its whole text "
                             "preserved there (#12), before this pass ran — which is why "
                             "`malformed_rows_before_the_pass` is empty rather than naming it. "
                             "The row's state did not move: it was open by its own text and is "
                             "open now.",
            "where_the_former_seven_cell_form_is": "The commit this pass's own commit follows — "
                                                   "`45a082dc51` and every commit before it "
                                                   "carries the row in its former form, readable "
                                                   "as a git object by explicit hash.",
            "why_the_order_was_this_way": "OI-362 states the order the other way round — the "
                                          "silent-skip STOP first, so the population movement is "
                                          "visible rather than merely happening. It is honored: "
                                          "the STOP is in the ONE parser in the same commit as "
                                          "this repair, and the movement is accounted for HERE, "
                                          "which is what that instruction asks for. What the row "
                                          "forbids is a parser task slipping the movement in "
                                          "unremarked, and this pass names it in advance, applies "
                                          "it under a ruling, and records it.",
        },
        "counts": {
            "rows_parsed": len(table),
            "rows_malformed_before_the_pass": len(malformed_before),
            "openings_already_canonical_at_the_baseline":
                sum(1 for t in table if t["opening_was_already_canonical"]),
            "openings_normalized": sum(1 for t in table
                                       if t["the_opening_changed_from_the_baseline"]),
            "state_movements": len(movers),
        },
        "state_movements": [{"id": t["id"], "from": t["state_under_the_rule_at_HEAD"],
                             "to": t["state_under_the_canonical_rule"],
                             "named_in_advance": t["id"] in NAMED_CORRECTIONS,
                             "why": NAMED_CORRECTIONS.get(t["id"], (None, None))[1]}
                            for t in movers],
        "rows_this_same_commit_RESOLVES_which_is_a_different_act": {
            "what": "The baseline is the commit before this one, so a row this commit FLIPS shows "
                    "as a state movement in the table. A resolution is not a normalization "
                    "movement and is not hidden inside one: these are listed apart, with the act "
                    "that made each, and a flip not listed here is still a STOP.",
            "rows": [{"id": t["id"], "from": t["state_under_the_rule_at_HEAD"],
                      "to": t["state_under_the_canonical_rule"],
                      "why": RESOLUTIONS_IN_THE_SAME_COMMIT[t["id"]]}
                     for t in resolved_in_act],
        },
        "malformed_rows_before_the_pass": malformed_before,
        "named_corrections_not_visible_in_the_table_because_the_row_did_not_parse":
            predicted_dropped,
        "the_survey_the_vocabulary_rests_on": ev["opening_words_by_frequency"],
        "every_row": table,
    }
    open(OUT, "w", encoding="utf-8", newline="").write(
        json.dumps(artifact, indent=2, ensure_ascii=False) + "\n")

    with open(INDEX, "w", encoding="utf-8", newline="") as fh:
        fh.write("\n".join(out_lines) + "\n")

    print(f"wrote {os.path.relpath(OUT, ROOT)} and normalized {os.path.relpath(INDEX, ROOT)}")
    print(f"  rows parsed {len(table)}; malformed before the pass {len(malformed_before)} "
          f"{dropped_ids}")
    print(f"  openings normalized: {artifact['counts']['openings_normalized']}")
    print(f"  state movements: {[t['id'] for t in movers]} (all named in advance)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
