#!/usr/bin/env python3
"""THE DISCARD RECORDS THE GATING DERIVATION MAY CONSUME — located, validated, published.

THE RULING THIS EXISTS FOR.  User, 2026-08-13, Ruling 69 of
`cowork_rulings_2026_08_13_seventeenth_stop.md`, homed at `CLAUDE.md`'s open-items register section
and entered as **D-677**: *a DISCARD verdict on an already-rowed item is an INPUT to the derivation
that decides gating — never an edit to a gating verdict.*  The gate stays DERIVED; what changes is
what the derivation reads.  This file is what it reads.

THE GUARD, WHICH IS THE RULING'S OWN AND NOT AN ADDITION.  A discard verdict is AUTHORED, so
feeding it to a derived cut lets an authored judgment move a gate.  **A discard record therefore
moves the gate only where it carries its finding, its date and its reason** — amended #10's own
requirement (**D-174**) — and a record lacking any of the three does not reach the cut.  That is
enforced here, per record, at the record's own text.

AND THE CARVE-OUT BOUNDS IT.  Amended #10 states that an establishment obligation (#19) is never
discarded, whatever its subject.  That is checked DERIVED rather than read out of the record's
prose: a row the committed apparatus declaration keeps gating on a ground naming #19 is a row no
discard record may move, and one naming such a row is a STOP.

WHAT IS AUTHORED AND WHAT IS DERIVED — the difference is the whole value.
  AUTHORED  a POINTER, per record: which row, which surface, and the QUOTE that locates each of
            the three elements.  Nothing here is a verdict.  The discard verdicts themselves were
            authored elsewhere, under the worth test, in the acts named at each entry's
            `recorded_by`; this table cites them and cannot create one.
  DERIVED   every element's presence, located in the surface at run time and required to fall
            inside the SAME record; the row's open state, from the ONE index parser (#6); the #19
            carve-out, from the committed apparatus declaration; and the conforming set the gating
            derivation consumes.

WHY A LOCATED POINTER TABLE RATHER THAN A SCANNER OVER THE RECORD.  A scanner would have to invent
a grammar for a discard record and would then carry an UNMEASURED REACH — the defect the record has
met twice already, at a family enumerated by an unmeasured pattern (`OPEN_ITEMS.md` OI-367) and at a
derived enumeration reporting its class empty while an instance stood (OI-368).  A pointer whose
every element is RE-LOCATED on each run cannot go stale silently: a reworded record STOPS this tool
rather than leaving a citation to text nobody re-read.  It is also the construction every sibling
tool here already uses — an authored table with STOPs in both directions.

THE COMPLETENESS BOUND, STATED RATHER THAN CLAIMED (#19, and D-661's rule that *complete* means
complete relative to a NAMED derivation).  A BOUNDED completeness STOP runs over the open-items
register's OWN two surfaces — the INDEX status cells and the detail files — so a discard recorded by
the route this register uses cannot be left out of the table silently.  It does NOT reach any other
surface.  A discard record written somewhere else reaches the cut only by being entered here, and
the error that leaves is in the SAFE direction: a gate is KEPT that the record may have discarded,
never removed by something nobody read.

SOUNDNESS, MEASURED AGAINST SEEDS RATHER THAN ASSERTED (#19).  The record holds two worth-test
outcomes that are NOT discards, written on the same day and by the same act as two of the discards.
They are the negative seeds: this tool must not carry them and its completeness scan must not pull
them in.  Both directions are published at `the_soundness_check`.

WHAT THIS FILE DOES NOT DO.  It authors no discard, tests no row, closes no row and moves no status
cell.  It writes no gating verdict — the gate is derived by the completion inventory, which reads
this artifact's conforming set as ONE of its inputs.  It authorizes no fix, no design and no
inference change.

Run:
  python tools/audit/gen_discard_records.py           # write the artifact
  python tools/audit/gen_discard_records.py --check   # re-derive, exit 1 on drift
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from output_encoding import use_utf8_output                       # noqa: E402  (path set above)
from gen_nongating_apparatus_rows import parse_rows               # noqa: E402  (#6 — one parser)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

ROOT = Path(__file__).resolve().parent.parent.parent
INDEX = ROOT / "OPEN_ITEMS.md"
OPEN_ITEMS_DIR = ROOT / "open_items"
APPARATUS = ROOT / "tools" / "audit" / "nongating_apparatus_rows.json"
OUT = ROOT / "tools" / "audit" / "discard_records.json"

# The token a recorded gate ground carries when the #19 carve-out — and nothing else — keeps a row
# inside the gate. It is the principle's own register identifier, so a ground that invokes the
# carve-out cannot fail to carry it and a ground that does not cannot match by accident. The same
# token, for the same reason, as the bearing cut's own carve-out test (#6 in substance).
EXEMPTION_TOKEN = "#19"

# ── the BOUNDED completeness scan's two patterns, over the register's own two surfaces ───────────
# Neither may match a NOT-DISCARDED record: the record writes those with the word `NOT` before the
# verdict, and the two negative seeds below are what checks that on every run rather than by
# inspection.
INDEX_DISCARD_MARK = "★ DISCARDED"
DETAIL_DISCARD_HEADING = "## ★ DISCARD RECORD"


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


# ═══════════════════════════════════════ AUTHORED: the pointers, one per discard record ══════════
#
# Each entry POINTS at a discard verdict authored elsewhere. `finding`, `date` and `reason` are the
# quotes that locate Ruling 69's three required elements, and every one of them must fall inside the
# span the record's own opening heading begins. `date_value` must itself appear inside the located
# date quote, so this table cannot carry a date the record does not state.
AUTHORED: list[dict] = [
    {
        "row": "OI-90",
        "surface": "cowork_away_returns.md",
        "record_opens_at": "### ★ (i) [[OI-90]] — the stale reason strings under "
                           "`tools/audit/l1l2/` — DISCARDED",
        "the_verdict": "**THE VERDICT — DISCARDED, with what amended #10 requires of a discard "
                       "record.**",
        "finding": "*Finding:* the three stale `reason` strings named above.",
        "date": "*Date:* found by the L3 pass-1 audit and rowed as OI-90; put to the worth test "
                "and discarded 2026-08-13, at this batch.",
        "date_value": "2026-08-13",
        "reason": [
            "*Reason for the discard:* it bears on neither limb.",
            "**Limb (a)** — nothing is built on a reason string; no design carries load from it.",
            "**Limb (b)** — `tools/audit/l1l2/file_table.csv` is an audit-scope table and not a "
            "specification",
        ],
        "the_records_own_19_sentence": "**THE #19 CARVE-OUT FIRST, AND IT DOES NOT REACH THIS "
                                       "ROW.**",
        "recorded_by": "CC, 2026-08-13, `cc_instruction_false_statements_pass.md` Task 3",
        "under": "the worth test at `CLAUDE.md` principle #10 (D-174), the user's Ruling 68",
        "why_the_surface_is_not_the_row": (
            "The dispatch that ordered the test forbade the status cell moving, and the detail-file "
            "half of the route its predecessors used was not written either — so the record stands "
            "in the returns file and nowhere else. That is a fact about WHERE the record is, not "
            "about whether it conforms: Ruling 69's guard is that the record carry its finding, its "
            "date and its reason, and all three are located above. It is also why this table is "
            "authored rather than scanned: no derivation over the register's own two surfaces "
            "would find this record at all."
        ),
    },
    {
        "row": "OI-372",
        "surface": "open_items/OI-372.md",
        "record_opens_at": "## ★ DISCARD RECORD — 2026-08-12 (CC, `cc_instruction_worth_test.md` "
                           "Task 2)",
        "the_verdict": "this finding is **DISCARDED** — it is not an open obligation: no gate, no "
                       "capacity.",
        "finding": "the tool still STOPs, its authored verdict still names a document its "
                   "derivation no longer carries, and it still has no retired block.",
        "date": "## ★ DISCARD RECORD — 2026-08-12 (CC, `cc_instruction_worth_test.md` Task 2)",
        "date_value": "2026-08-12",
        "reason": [
            "**Limb (a) — does leaving it unfixed risk something being built that does not serve",
            "**Limb (b) — does it risk code no longer being comparable against a correct and "
            "complete",
            "**The consumer, named rather than guessed.**",
        ],
        "the_records_own_19_sentence": "**The #19 check, taken FIRST and answered at the "
                                       "objects.**",
        "recorded_by": "CC, 2026-08-12, `cc_instruction_worth_test.md` Task 2",
        "under": "the worth test at `CLAUDE.md` principle #10 (D-174), the user's Ruling 68",
        "why_the_surface_is_not_the_row": (
            "It IS the row: this record sits in the row's own detail file, which is the route the "
            "register uses, and the INDEX status cell carries the clause beside it. The bounded "
            "completeness scan below finds it on both surfaces."
        ),
    },
    {
        "row": "OI-373",
        "surface": "open_items/OI-373.md",
        "record_opens_at": "## ★ DISCARD RECORD — 2026-08-12 (CC, `cc_instruction_worth_test.md` "
                           "Task 2)",
        "the_verdict": "this finding is **DISCARDED** — it is not an open obligation: no gate, no "
                       "capacity.",
        "finding": "no invocation was authored, nothing about the guard set was adjusted, and the "
                   "runner still cannot exit clean.",
        "date": "## ★ DISCARD RECORD — 2026-08-12 (CC, `cc_instruction_worth_test.md` Task 2)",
        "date_value": "2026-08-12",
        "reason": [
            "**Limb (a) — does leaving it unfixed risk something being built that does not serve",
            "**Limb (b) — does it risk code no longer being comparable against a correct and "
            "complete",
            "**The consumer, named rather than guessed.**",
        ],
        "the_records_own_19_sentence": "**The #19 check, taken FIRST and answered at the "
                                       "objects.**",
        "recorded_by": "CC, 2026-08-12, `cc_instruction_worth_test.md` Task 2",
        "under": "the worth test at `CLAUDE.md` principle #10 (D-174), the user's Ruling 68",
        "why_the_surface_is_not_the_row": (
            "It IS the row, on the same route as the entry above."
        ),
    },
]

# ═══════════════════════════════════ AUTHORED: the negative seeds (#19) ══════════════════════════
#
# Two worth-test outcomes the record holds that are NOT discards, written on the same day and by the
# same act as two of the records above. They are what makes the soundness of both the table and the
# completeness scan MEASURED rather than asserted: this tool must carry neither, and the scan must
# pull in neither. A seed that stops matching its own quote is a STOP — a negative control that has
# silently left the record establishes nothing.
NEGATIVE_SEEDS: list[dict] = [
    {
        "row": "OI-374",
        "surface": "open_items/OI-374.md",
        "the_quote": "## ★ WORTH-TEST RECORD — 2026-08-12 (CC, `cc_instruction_worth_test.md` "
                     "Task 2): NOT DISCARDED",
        "why_it_is_a_seed": "The worth test was applied to it in the same act as OI-372 and "
                            "OI-373 and returned NOT DISCARDED on the #19 carve-out. A tool that "
                            "cannot tell this record from theirs would discard an establishment "
                            "obligation, which amended #10 forbids outright.",
    },
    {
        "row": "OI-375",
        "surface": "open_items/OI-375.md",
        "the_quote": "## Why it is not DISCARDED under the worth test",
        "why_it_is_a_seed": "A second NOT-DISCARDED outcome, written in a DIFFERENT form from the "
                            "seed above — so the two together test the scan against both shapes "
                            "the record actually uses for a negative outcome, not one shape twice.",
    },
]


# ────────────────────────────────────────────────────────────────────── locating, at the objects
def record_span(text: str, opening: str, surface: str, row: str) -> tuple[str, int]:
    """The lines of ONE record: from its own heading to the next heading of the same depth or less.

    Line-based on purpose. The span has to be computed before whitespace is collapsed, or a heading
    boundary is indistinguishable from an inline `#`; every element quote is then matched against
    the NORMALIZED span, so a record that was re-wrapped still matches and one that was reworded
    does not.
    """
    lines = text.splitlines()
    want = norm(opening)
    hits = [i for i, ln in enumerate(lines) if ln.lstrip().startswith("#") and norm(ln) == want]
    if len(hits) != 1:
        raise SystemExit(
            f"STOP: {row}'s discard record opens at a heading this tool cannot locate exactly once "
            f"in {surface} ({len(hits)} match(es)). A pointer that cannot find its own record may "
            "not be published, and a record that has been reworded is re-read rather than assumed."
        )
    start = hits[0]
    depth = len(re.match(r"#+", lines[start].lstrip()).group(0))
    end = len(lines)
    for i in range(start + 1, len(lines)):
        m = re.match(r"(#+)\s", lines[i])
        if m and len(m.group(1)) <= depth:
            end = i
            break
    return "\n".join(lines[start:end]), depth


def carve_out_rows() -> dict:
    """Rows the committed apparatus declaration keeps gating on a ground naming #19.

    Read on every run and never listed here. A missing artifact is a STOP: treating it as an empty
    set would let a discard record move a gate the carve-out holds, which amended #10 forbids.
    """
    if not APPARATUS.is_file():
        raise SystemExit(
            f"STOP: the apparatus declaration is absent ({APPARATUS}). The #19 carve-out is read "
            "from its recorded gate grounds and may not fall back to an empty set silently.")
    app = json.loads(APPARATUS.read_text(encoding="utf-8"))
    return {i["id"]: i for i in app["items"]
            if i["verdict"] == "GATES" and EXEMPTION_TOKEN in (i.get("gate_ground") or "")}


def completeness_scan(rows_by_id: dict) -> dict:
    """The BOUNDED scan: discard records on the register's own two surfaces.

    Its reach is exactly those two surfaces and is stated as such. It exists so a discard written by
    the route the register uses cannot be left out of the authored table silently; it establishes
    nothing about any other surface.
    """
    on_the_index: list[str] = []
    for rid, r in rows_by_id.items():
        if INDEX_DISCARD_MARK in r["status_column"]:
            on_the_index.append(rid)
    in_a_detail_file: list[str] = []
    for path in sorted(OPEN_ITEMS_DIR.glob("OI-*.md")):
        if DETAIL_DISCARD_HEADING in path.read_text(encoding="utf-8"):
            in_a_detail_file.append(path.stem)
    found = sorted(set(on_the_index) | set(in_a_detail_file))
    return {
        "what_it_covers": (
            "The open-items INDEX status cells and the per-row detail files — the register's own "
            "two surfaces, and nothing else."
        ),
        "what_it_does_NOT_cover": (
            "Every other surface in the record. A discard recorded elsewhere reaches the cut only "
            "by being entered in the authored table above, so this scan is a completeness STOP over "
            "the register and is NOT a claim that the table is complete over the record. The error "
            "that leaves is in the safe direction: a gate is KEPT that a record may have discarded."
        ),
        "the_two_patterns": {"index_status_cell": INDEX_DISCARD_MARK,
                             "detail_file_heading": DETAIL_DISCARD_HEADING},
        "found_on_the_index": sorted(on_the_index),
        "found_in_a_detail_file": sorted(in_a_detail_file),
        "found": found,
    }


def build() -> dict:
    rows = parse_rows()
    rows_by_id = {r["id"]: r for r in rows}
    carve = carve_out_rows()

    seen: set[str] = set()
    conforming: list[dict] = []
    for a in AUTHORED:
        row = a["row"]
        if row in seen:
            raise SystemExit(f"STOP: {row} carries two pointers in this table. One record per row.")
        seen.add(row)

        rec = rows_by_id.get(row)
        if rec is None:
            raise SystemExit(
                f"STOP: this table points at {row}, which the open-items INDEX does not carry. A "
                "discard record for a row the register no longer holds may not reach the cut.")
        if not rec["open"]:
            raise SystemExit(
                f"STOP: {row} is RESOLVED at the INDEX and this table carries a discard record for "
                "it. A discard is not a resolution and a resolved row does not need one — the two "
                "states have come apart and are not reconciled here.")
        if row in carve:
            raise SystemExit(
                f"STOP: {row} is kept gating by the #19 carve-out and a discard record names it. "
                "Amended #10 states that an establishment obligation is NEVER discarded, whatever "
                "its subject, so this record may not reach the cut — the disagreement is surfaced "
                "rather than resolved by preferring one of the two.")

        surface = ROOT / a["surface"]
        if not surface.is_file():
            raise SystemExit(f"STOP: {row}'s discard record names a surface that is not there: "
                             f"{a['surface']}")
        span, depth = record_span(surface.read_text(encoding="utf-8"), a["record_opens_at"],
                                  a["surface"], row)
        nspan = norm(span)

        elements: dict[str, dict] = {}
        missing: list[str] = []
        wanted = [("finding", [a["finding"]]), ("date", [a["date"]]), ("reason", a["reason"])]
        for name, quotes in wanted:
            located = [q for q in quotes if norm(q) in nspan]
            elements[name] = {"quotes": quotes, "located": located,
                              "present": len(located) == len(quotes)}
            if not elements[name]["present"]:
                missing.append(name)
        for optional in ("the_verdict", "the_records_own_19_sentence"):
            q = a.get(optional)
            elements[optional] = {"quotes": [q], "located": [q] if norm(q) in nspan else [],
                                  "present": norm(q) in nspan}

        if not elements["the_verdict"]["present"]:
            raise SystemExit(
                f"STOP: {row}'s record does not carry the verdict sentence this table quotes, "
                "inside the record it names. A pointer to a discard that cannot find the discard "
                "may not be published.")
        if a["date_value"] not in norm(a["date"]):
            raise SystemExit(
                f"STOP: {row}'s pointer carries the date {a['date_value']!r}, which its own quoted "
                "date element does not state. This table may not carry a date the record does not.")
        if missing:
            # Ruling 69's guard, and the ONE thing that keeps an authored verdict from moving a
            # derived gate on nothing. It is reported rather than raised: a record that does not
            # conform simply does not reach the cut, which is the ruling's own wording.
            conforming_row = False
        else:
            conforming_row = True

        entry = {
            **{k: v for k, v in a.items() if k != "reason"},
            "reason_quotes": a["reason"],
            "the_three_elements_required_by_the_ruling": {
                k: elements[k] for k in ("finding", "date", "reason")},
            "also_located_but_not_required": {
                k: elements[k] for k in ("the_verdict", "the_records_own_19_sentence")},
            "the_19_carve_out": {
                "kept_gating_by_the_carve_out": row in carve,
                "how_that_was_derived": (
                    "the committed apparatus declaration's own recorded gate ground, read on every "
                    "run — never the record's prose about itself"),
            },
            "record_heading_depth": depth,
            "conforms": conforming_row,
            "elements_not_located": missing,
        }
        conforming.append(entry)

    scan = completeness_scan(rows_by_id)
    unentered = sorted(r for r in scan["found"] if r not in seen)
    if unentered:
        raise SystemExit(
            "STOP: the register's own surfaces carry a discard record for row(s) this table does "
            "not enter: " + ", ".join(unentered) + ". A discard on the register's own route may "
            "not be left out of the table silently — enter it with its three located elements, or "
            "say at the row why it is not one.")

    # ── the soundness check (#19): both directions, against seeds that are in the record ─────────
    seed_rows: list[dict] = []
    for s in NEGATIVE_SEEDS:
        path = ROOT / s["surface"]
        if not path.is_file():
            raise SystemExit(f"STOP: negative seed {s['row']} names a surface that is not there: "
                             f"{s['surface']}")
        text = path.read_text(encoding="utf-8")
        present = norm(s["the_quote"]) in norm(text)
        if not present:
            raise SystemExit(
                f"STOP: negative seed {s['row']}'s quoted record is no longer in {s['surface']}. A "
                "control that has silently left the record establishes nothing, so this tool "
                "refuses to publish a soundness verdict resting on it.")
        seed_rows.append({
            **s,
            "the_record_is_still_there": present,
            "in_the_authored_table": s["row"] in seen,
            "pulled_in_by_the_completeness_scan": s["row"] in scan["found"],
        })
    caught = [s for s in seed_rows if s["in_the_authored_table"]
              or s["pulled_in_by_the_completeness_scan"]]
    if caught:
        raise SystemExit(
            "STOP: a NOT-DISCARDED worth-test outcome is being treated as a discard: "
            + ", ".join(s["row"] for s in caught)
            + ". The two records are written with the word NOT before the verdict, so this is the "
            "tool reading its own patterns wrongly, not the record being ambiguous.")

    conforming_ids = sorted(e["row"] for e in conforming if e["conforms"])
    non_conforming = sorted(e["row"] for e in conforming if not e["conforms"])

    return {
        "purpose": (
            "The discard records the gating derivation may consume, each LOCATED in its own surface "
            "and checked against Ruling 69's guard — a discard record moves the gate only where it "
            "carries its finding, its date and its reason."
        ),
        "generated_by": "tools/audit/gen_discard_records.py",
        "generated_for": "cc_instruction_ruling69_discard_input.md (Task 2)",
        "the_ruling": (
            "User, 2026-08-13, Ruling 69 of `cowork_rulings_2026_08_13_seventeenth_stop.md`, homed "
            "at `CLAUDE.md`'s open-items register section, register entry D-677: a DISCARD verdict "
            "on an already-rowed item is an INPUT to the derivation that decides gating — never an "
            "edit to a gating verdict. Quoted in full at its home and not restated here (#6, D-643)."
        ),
        "what_this_file_does_NOT_do": (
            "It authors no discard, tests no row, closes no row, moves no status cell and writes no "
            "gating verdict. The gate is derived by the completion inventory, which reads the "
            "conforming set below as ONE of its inputs. It authorizes no fix, no design and no "
            "inference change."
        ),
        "what_is_authored_and_what_is_derived": {
            "authored": "a POINTER per record — the row, the surface, and the quote that locates "
                        "each of the three elements. No verdict.",
            "derived": "every element's presence inside the record's own span; the row's open "
                       "state, from the ONE index parser; the #19 carve-out, from the committed "
                       "apparatus declaration; the completeness scan; the soundness check.",
        },
        "★_the_guard": {
            "the_three_elements": ["finding", "date", "reason"],
            "what_happens_without_one": (
                "The record DOES NOT REACH THE CUT. It is reported here with the element it lacks "
                "and is not consumed — which is the ruling's own wording, and is deliberately not a "
                "STOP: a non-conforming record is a fact about the record, not a broken tool."
            ),
            "the_19_carve_out": (
                "Amended #10: an establishment obligation is NEVER discarded, whatever its subject. "
                "A discard record naming a row the apparatus declaration keeps gating on a ground "
                "invoking #19 is a STOP rather than a non-conformance — the two statements "
                "contradict each other and the disagreement is surfaced rather than settled by "
                "preferring one."
            ),
        },
        "records": conforming,
        "conforming": [e for e in conforming if e["conforms"]],
        "counted": {
            "records_entered": len(conforming),
            "conforming": len(conforming_ids),
            "conforming_ids": conforming_ids,
            "not_conforming": len(non_conforming),
            "not_conforming_ids": non_conforming,
        },
        "the_bounded_completeness_scan": scan,
        "the_soundness_check": {
            "why_it_is_here": (
                "A pattern's reach against the text it scans is exactly what this project has twice "
                "been caught not measuring, so this tool publishes what its patterns do against "
                "records the record actually holds rather than asserting they are right."
            ),
            "positive": {
                "what_it_asserts": "every entered record is located, and its three elements fall "
                                   "inside the record's own span",
                "records_located": len(conforming),
                "conforming": conforming_ids,
                "not_conforming": non_conforming,
            },
            "negative": {
                "what_it_asserts": "a NOT-DISCARDED worth-test outcome is carried by neither the "
                                   "table nor the completeness scan",
                "seeds": seed_rows,
                "verdict": "PASS — neither negative seed is treated as a discard",
            },
            "what_a_PASS_does_and_does_not_establish": (
                "It establishes that the two patterns separate the discards the record holds from "
                "the non-discards it holds beside them, on every shape of each the record currently "
                "uses. It does NOT establish that the patterns would separate a shape the record "
                "does not yet contain, and no such claim is made — which is why the authored table, "
                "and not the scan, is what reaches the cut."
            ),
        },
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true",
                    help="re-derive and exit 1 if the committed artifact does not match")
    args = ap.parse_args(argv)

    art = build()
    text = json.dumps(art, indent=2, ensure_ascii=False) + "\n"
    if args.check:
        have = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if have != text:
            print("STALE: tools/audit/discard_records.json does not re-derive from the record")
            return 1
        print("the discard records re-derive from the record")
        print(f"  entered {art['counted']['records_entered']}, "
              f"conforming {art['counted']['conforming']}, "
              f"not conforming {art['counted']['not_conforming']}")
        return 0

    OUT.write_text(text, encoding="utf-8", newline="\n")
    print(f"wrote {OUT.relative_to(ROOT)}")
    print(f"  records entered: {art['counted']['records_entered']}; "
          f"conforming: {art['counted']['conforming']}; "
          f"not conforming: {art['counted']['not_conforming']}")
    print(f"  the bounded completeness scan found: "
          f"{len(art['the_bounded_completeness_scan']['found'])} on the register's own surfaces")
    print(f"  negative seeds: {art['the_soundness_check']['negative']['verdict']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
