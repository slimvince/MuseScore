#!/usr/bin/env python3
"""EVERY OPEN-ITEMS INDEX ROW, DECIDED BOTH WAYS — before the parser correction and after it.

WHY THIS EXISTS.  `OPEN_ITEMS.md` OI-356: the ONE parser every derivation over the open-items
index uses decided a row's open state by asking whether the resolved mark occurs ANYWHERE IN THE
WHOLE STATUS CELL.  A cell that merely MENTIONS another row's resolved status therefore made its
own row read as resolved to every derivation — the open-row count, the true-half cuts and the
finish line's populations all move with it.  The user's Ruling 25 of 2026-08-09
(`cowork_rulings_2026_08_09_fourth_stop.md`) corrects it: the detection is anchored to the status
cell's own LEADING TOKEN, never to a mention of another row's resolution.

WHY A BOTH-WAYS TABLE RATHER THAN A DIFF OF THE RESULT.  The same ruling attaches the condition
that makes the correction safe: **every index row is decided both ways, before and after, and the
only verdicts that may move are rows the defect's shape names.**  A report derived from the
corrected parser alone could not show that — it would only say what the tree looks like now.  This
file implements BOTH rules itself, independently of the parser it is about, so the movement is
measured rather than asserted, and a row that moves for any other reason is visible.

WHAT IT IS.  A POINT-IN-TIME RECORD of one correction, in the class the 2026-08-04 ruling R4
defines: it records a measurement taken at a moment, not a live invariant, so it carries no
re-derivation mode and does not belong in the guard population.  It is written once, with the
correction it justifies, and read afterwards.

Run:
    python tools/audit/gen_oi356_parser_correction.py

Output:
    tools/audit/oi356_parser_correction.json
"""
from __future__ import annotations

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
INDEX = os.path.join(ROOT, "OPEN_ITEMS.md")
OUT = os.path.join(HERE, "oi356_parser_correction.json")

sys.path.insert(0, HERE)
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

ROW = re.compile(r"^\| OI-")
RESOLVED_MARK = "✅"


def rows() -> tuple[list[dict], list[dict]]:
    """Every index row, with its six cells — the same split the parser under correction uses.

    Returns (parsed, skipped). The parser under correction SILENTLY DROPS a row that does not
    split into exactly six cells, and a dropped row is invisible to every derivation over the
    index. That is measured here rather than assumed absent.
    """
    out, skipped = [], []
    with open(INDEX, encoding="utf-8") as fh:
        for lineno, ln in enumerate(fh.read().splitlines(), 1):
            if not ROW.match(ln):
                continue
            cells = [c.strip() for c in ln.strip().strip("|").split(" | ")]
            if len(cells) != 6:
                skipped.append({"line": lineno, "cells_found": len(cells),
                                "id": cells[0] if cells else None,
                                "row_opening": ln[:180]})
                continue
            out.append({"id": cells[0], "title": cells[1], "subject_column": cells[3],
                        "status_column": cells[4]})
    return out, skipped


def open_under_the_former_rule(status: str) -> bool:
    """The rule as it stood: the mark does not occur ANYWHERE in the status cell."""
    return RESOLVED_MARK not in status


def open_under_the_corrected_rule(status: str) -> bool:
    """The rule as ruled: the cell's own LEADING token is not the mark.

    Leading is taken after stripping surrounding whitespace only. No markup is skipped and no
    synonym is recognised: a cell that opens with bold text, or that spells its resolution in
    words, reads OPEN under both rules alike, so this correction cannot move it in either
    direction. That narrowness is deliberate — the ruling names one defect shape, and a wider
    reading would move verdicts the ruling does not reach.
    """
    return not status.lstrip().startswith(RESOLVED_MARK)


def main() -> int:
    parsed, skipped = rows()
    table = []
    for r in parsed:
        status = r["status_column"]
        before = open_under_the_former_rule(status)
        after = open_under_the_corrected_rule(status)
        mark_positions = [i for i, ch in enumerate(status) if ch == RESOLVED_MARK]
        table.append({
            "id": r["id"],
            "open_under_the_former_rule": before,
            "open_under_the_corrected_rule": after,
            "moves": before != after,
            "the_mark_occurs_in_the_status_cell": bool(mark_positions),
            "the_cell_opens_with_the_mark": status.lstrip().startswith(RESOLVED_MARK),
            "first_position_of_the_mark_in_the_cell": mark_positions[0] if mark_positions else None,
            "status_cell_opening": status[:180],
            # The text AROUND each occurrence of the mark, generated rather than transcribed, so
            # a reader can see WHOSE resolution the mark states -- this row's own, or another
            # row's. That distinction is what the ruling's condition turns on and it is not
            # visible from a position number.
            "the_text_around_each_mark": [status[max(0, i - 60): i + 120]
                                          for i in mark_positions],
        })

    movers = [t for t in table if t["moves"]]

    # ── AUTHORED, and it is the half a predicate cannot supply ────────────────────────────────
    # The ruling's condition names rows whose status cell mentions ANOTHER ROW'S resolution.
    # Whether a mark states THIS row's own resolution or another row's is a reading of the text,
    # not a property of the character, so it is authored per mover with its ground and its
    # evidence located in the generated context above. A mover with no reading here is a STOP:
    # the pass will not guess one.
    READING_PER_MOVER = {
        "OI-178": ("this row's OWN resolution",
                   "The cell reads 'PROTOCOL RATIFIED 2026-07-19; [mark] EXECUTED 2026-07-26' and "
                   "then describes what was executed. The mark states THIS row's completion; it "
                   "is not at the start only because a ratification date precedes it. The row is "
                   "RESOLVED, the former rule reads it correctly, and the corrected rule would "
                   "read it as open."),
        "OI-208": ("a DELIVERED HALF of this row's own work, inside a row that is OPEN",
                   "The cell OPENS with 'OPEN — ' and the mark appears far into it, on a "
                   "sub-result: the living surface landed. So the row is genuinely OPEN, the "
                   "former rule reads it as resolved, and the corrected rule reads it correctly. "
                   "This is the ONE mover the correction improves."),
        "OI-272": ("this row's OWN resolution, stated mid-cell",
                   "The cell opens with the ruling that settled the question and ends 'Row "
                   "CLOSED'; the mark appears mid-cell on the homing half of this row's own work. "
                   "The row is RESOLVED, the former rule reads it correctly, and the corrected "
                   "rule would read it as open."),
    }
    unread = [t["id"] for t in movers if t["id"] not in READING_PER_MOVER]
    if unread:
        raise SystemExit("STOP: a moving row has no authored reading of whose resolution its "
                         "mark states: " + ", ".join(unread))
    movers_stating_another_rows_resolution = [
        t["id"] for t in movers
        if "another row" in READING_PER_MOVER[t["id"]][0].lower()]
    movers_stating_their_own_resolution = [
        t["id"] for t in movers
        if READING_PER_MOVER[t["id"]][0].startswith("this row's OWN")]

    # The defect's own shape, stated as a predicate so a mover can be checked against it rather
    # than judged: the cell MENTIONS the mark but does not OPEN with it.
    def is_the_defect_shape(t: dict) -> bool:
        return t["the_mark_occurs_in_the_status_cell"] and not t["the_cell_opens_with_the_mark"]

    unexpected = [t for t in movers if not is_the_defect_shape(t)]

    # Rows that mention the mark and do NOT open with it are exactly the population at risk; a
    # mover must come from it, and every member of it must move (in the open direction).
    at_risk = [t for t in table if is_the_defect_shape(t)]
    at_risk_not_moving = [t["id"] for t in at_risk if not t["moves"]]

    # A row whose status is resolved but which spells it in WORDS rather than with the mark reads
    # OPEN under both rules. That is not a movement and this correction does not touch it, but it
    # is a discrepancy between what a row says and what every derivation over the index believes,
    # so it is enumerated rather than left for a reader to notice.
    spells_it_in_words = [
        {"id": t["id"], "status_cell_opening": t["status_cell_opening"]}
        for t in table
        if not t["the_mark_occurs_in_the_status_cell"]
        and re.match(r"^[*\s]*(RESOLVED|SUPERSEDED|CLOSED|DONE)\b", t["status_cell_opening"])
    ]

    artifact = {
        "what_this_is": "Every open-items index row decided BOTH WAYS — under the parser rule as "
                        "it stood, and under the rule the user's Ruling 25 of 2026-08-09 "
                        "corrects it to. A point-in-time record of one correction (the 2026-08-04 "
                        "ruling R4 class): it carries no re-derivation mode, because re-deriving "
                        "it after the correction would destroy the before half it exists to "
                        "record.",
        "generated_by": "tools/audit/gen_oi356_parser_correction.py",
        "the_row_it_answers": "OPEN_ITEMS.md OI-356",
        "the_two_rules": {
            "former": "A row is OPEN when the resolved mark does not occur ANYWHERE in its status "
                      "cell. A cell that merely mentions another row's resolved status therefore "
                      "made its own row read as resolved.",
            "corrected": "A row is OPEN when its status cell's own LEADING token is not the "
                         "resolved mark. Stripping whitespace only: no markup is skipped and no "
                         "synonym is recognised.",
            "why_the_corrected_rule_is_narrow_on_purpose":
                "The ruling names ONE defect shape. Recognising a bold-wrapped or word-spelled "
                "resolution as well would move verdicts the ruling does not reach, and the "
                "condition attached to the ruling is that only rows the defect's shape names may "
                "move. Narrowness is what makes that condition checkable.",
        },
        "the_condition_the_ruling_attaches": {
            "stated": "Every index row is decided both ways, before and after; the only verdicts "
                      "that may move are rows the defect's shape names; any other movement is a "
                      "STOP. The dispatch's assumption A3 states the shape in words: rows whose "
                      "status cell MENTIONS ANOTHER ROW'S RESOLUTION.",
            "the_coarse_predicate": "the status cell CONTAINS the resolved mark but does not OPEN "
                                    "with it. This is what a character test can decide, and it is "
                                    "NOT the ruling's condition — it admits a row that states its "
                                    "OWN resolution somewhere other than the first character.",
            "rows_that_move": [t["id"] for t in movers],
            "rows_that_move_and_fail_even_the_coarse_predicate":
                [t["id"] for t in unexpected],
            "rows_of_the_coarse_predicate_that_do_NOT_move": at_risk_not_moving,
            "whose_resolution_each_moving_row_s_mark_states": {
                t["id"]: {"reading": READING_PER_MOVER[t["id"]][0],
                          "ground": READING_PER_MOVER[t["id"]][1]}
                for t in movers},
            "movers_stating_ANOTHER_row_s_resolution": movers_stating_another_rows_resolution,
            "movers_stating_THEIR_OWN_resolution": movers_stating_their_own_resolution,
            "verdict": (
                "STOP — THE ASSUMPTION IS REFUTED. Every moving row passes the coarse character "
                "predicate, and NOT ONE of them mentions another row's resolution, which is what "
                "the condition names. Read at the rows themselves: two of the three state THEIR "
                "OWN resolution somewhere other than the first character, so the corrected rule "
                "would mark two genuinely closed rows as open; the third is genuinely open and is "
                "the only row the correction improves. The instance the row was found on no "
                "longer exists at this tree, because the working convention it adopted — name "
                "another row's resolved status IN WORDS — was applied to the cell that caused it. "
                "So the correction as worded fixes one row and breaks two, and it is NOT applied."
                if movers_stating_their_own_resolution else
                "HELD — every moving row is the shape the condition names."),
            "what_follows": "The parser is left EXACTLY as it stands. Nothing about the defect "
                            "OI-356 records is withdrawn: a cell that mentions another row's mark "
                            "still makes its own row read as resolved, and the working convention "
                            "is still the only thing preventing it. What is refuted is that "
                            "anchoring to the LEADING TOKEN is the remedy — it trades one error "
                            "class for another, and the measurement above is the evidence.",
        },
        "a_second_discrepancy_found_while_deciding_both_ways_and_NOT_corrected_here": {
            "what": "Rows whose status cell states a resolution IN WORDS, with no resolved mark "
                    "anywhere. They read OPEN under BOTH rules, so this correction neither moves "
                    "them nor is about them — but every derivation over the index believes they "
                    "are open while their own text says otherwise.",
            "why_it_is_not_corrected_here": "Recognising a word-spelled resolution is a SECOND "
                                            "rule change, and it would move verdicts the ruling "
                                            "does not name — which the ruling's own condition "
                                            "makes a STOP. It is reported so it is not "
                                            "rediscovered.",
            "rows": spells_it_in_words,
            "an_authored_reading_per_row_because_a_pattern_cannot_supply_one": {
                "OI-175": "NOT ASSERTED TO BE A DEFECT. The cell states a MIXED status — "
                          "superseded in fact on one surface, still live on the legacy notation "
                          "path and retiring with it — so which way a single open/resolved bit "
                          "should fall for this row is not settled by its own text, and this pass "
                          "does not settle it.",
                "OI-326": "A DEFECT. The cell opens 'RESOLVED 2026-08-04' and the row is closed, "
                          "yet every derivation over the index counts it as open.",
                "OI-349": "A DEFECT. The cell opens 'RESOLVED 2026-08-09' and the row is closed, "
                          "yet every derivation over the index counts it as open.",
            },
        },
        "a_third_finding_the_both_ways_pass_turned_up_and_did_NOT_correct": {
            "what": "The parser under correction SILENTLY DROPS any index row that does not split "
                    "into exactly six cells — it skips and continues, with no report. A dropped "
                    "row is invisible to EVERY derivation over the index: it is neither open nor "
                    "resolved, it is absent, and no count moves when it appears or disappears.",
            "why_it_is_not_corrected_here": "Making a malformed row a STOP, or parsing it another "
                                            "way, is a MECHANISM change and D-436 reserves that "
                                            "to the user. It is also a different defect from the "
                                            "one Ruling 25 names, and the ruling's own condition "
                                            "is that only rows the named defect's shape may move.",
            "rows_dropped_at_this_tree": skipped,
            "how_to_read_an_empty_list": "Empty means no row is being dropped AT THIS TREE. It "
                                         "does NOT mean the parser reports one when it happens — "
                                         "the silence is the defect, and it is unchanged.",
        },
        "counts": {
            "index_rows_matching_the_row_pattern": len(table) + len(skipped),
            "index_rows_the_parser_admits": len(table),
            "index_rows_the_parser_silently_drops": len(skipped),
            "open_under_the_former_rule": sum(1 for t in table if t["open_under_the_former_rule"]),
            "open_under_the_corrected_rule": sum(1 for t in table
                                                 if t["open_under_the_corrected_rule"]),
            "moving": len(movers),
        },
        "every_row": table,
    }

    open(OUT, "w", encoding="utf-8", newline="").write(
        json.dumps(artifact, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {os.path.relpath(OUT, ROOT)}")
    print(f"  index rows admitted: {len(table)}; silently dropped: {len(skipped)}")
    print(f"  moving: {len(movers)} -> {[t['id'] for t in movers]}")
    print(f"  failing even the coarse predicate: {[t['id'] for t in unexpected]}")
    print(f"  coarse-predicate rows not moving: {at_risk_not_moving}")
    print(f"  movers stating ANOTHER row's resolution: {movers_stating_another_rows_resolution}")
    print(f"  movers stating THEIR OWN resolution:    {movers_stating_their_own_resolution}")
    print(f"  resolution spelled in words, no mark: {[r['id'] for r in spells_it_in_words]}")
    if movers_stating_their_own_resolution:
        print("STOP: the correction as worded would move rows that state their OWN resolution "
              "away from the first character. It is NOT applied; see the artifact's verdict.")
        return 1
    return 1 if unexpected else 0


if __name__ == "__main__":
    sys.exit(main())
