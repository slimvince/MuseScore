#!/usr/bin/env python3
"""How far phase 1's doc-sync half reaches into a document's account of ITSELF — ruling R1 applied.

THE RULING (user, 2026-08-04, dispatch `cc_instruction_phase1_delegations_and_corrections.md` R1;
`CLAUDE.md`, the D-231 phase-1 clause; register D-639): the doc-sync half reaches a document's
account of itself ONLY WHERE THAT ACCOUNT CHANGES HOW THE DOCUMENT'S ANALYSIS CONTENT IS READ, with
three worked examples that ARE the test — an as-built banner over a dormant mechanism IN, a missing
supersession note on a superseded plan IN, a stale anchor or a formatting artifact OUT — and with a
stated FALLBACK: if the test needs judgment on the first rows it meets, option (1A) governs and the
half reaches only the account of the ANALYSIS.

WHAT THIS FILE DOES.  It applies the test to the three documents `OPEN_ITEMS.md` OI-332 carries, one
per document, and records the verdict WITH the worked example it matched.  **Whether the fallback
was reached is DERIVED, not declared:** a document that matches no worked example is a document the
test did not decide, and the artifact says so and names the fallback rather than arguing the case.

WHAT IS AUTHORED AND WHAT IS DERIVED.
  authored : per document, which worked example it matches and why - the reading, made at the object
             this session, with the document's own words quoted from `open_items/OI-332.md`.
  derived  : the ruling's own text, located in `CLAUDE.md` BY ANCHOR STRING and quoted (never by
             line number - the OI-330 lesson); whether any document failed to match a worked
             example, and therefore whether the fallback governs; and every count.

THE STOPS.  The tool refuses to run if the ruling cannot be located by its anchor, if OI-332's
detail file does not carry all three documents it grades, or if a verdict names a worked example the
ruling does not state.

Usage:
  python tools/audit/decisions/gen_true_half_reach.py           # write the artifact
  python tools/audit/decisions/gen_true_half_reach.py --check   # re-derive, exit 1 on drift
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
CLAUDE_MD = os.path.join(ROOT, "CLAUDE.md")
OI332 = os.path.join(ROOT, "open_items", "OI-332.md")
OUT = os.path.join(HERE, "true_half_reach.json")

sys.path.insert(0, os.path.dirname(HERE))
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

RULING_ANCHOR = "**★ HOW FAR THE DOC-SYNC HALF REACHES INTO A DOCUMENT'S ACCOUNT OF ITSELF"
RULING_END = "**★ AND IT BEARS ON A GATE VERDICT"

# The three worked examples, as the ruling states them. A verdict may name only one of these.
WORKED_EXAMPLES = {
    "as-built banner over a dormant mechanism": "IN",
    "missing supersession note on a superseded plan": "IN",
    "stale anchor or a formatting artifact": "OUT",
}

# ---------------------------------------------------------------------------
# AUTHORED — one verdict per document OI-332 carries, each naming the worked example it matches.
# ---------------------------------------------------------------------------
VERDICTS = [
    {
        "document": "cowork_layer1_extend_design.md",
        "what_the_document_says_about_itself": (
            "Its line 2 banner reads \"Status: DRAFT for sign-off. Read-only design — no code.\""
        ),
        "what_is_true_at_head": (
            "Both operations it designs are built — `NoteModel::build` and `NoteModel::extend` are "
            "declared in `note_model.h`, with the overlap-retention contract the design's §4 "
            "specifies stated in the header's own comment, as OI-332 records at the object."
        ),
        "matched_worked_example": "as-built banner over a dormant mechanism",
        "verdict": "IN — the doc-sync half reaches it",
        "why": (
            "It is the ruling's first worked example with the sign reversed, and the reversal makes "
            "it a stronger case rather than a different one: a banner that says BUILT over dormant "
            "code and a banner that says NO CODE over built code both make a reader believe "
            "something false about the system. And the belief changes how every mechanism in the "
            "document is read — as a proposal still open to change, or as a description of what "
            "runs at HEAD. That is the account of the document changing how its analysis content "
            "is read, which is the test in its own words."
        ),
    },
    {
        "document": "cowork_layer3_reachback_design.md",
        "what_the_document_says_about_itself": (
            "Its status header cites the loop at `regionanalyzer.cpp:585–666` and its §0 cites the "
            "orchestrator at `:506` and the conditional build at `:536–538`."
        ),
        "what_is_true_at_head": (
            "The same constructs sit at `:561`, `:591` and `:660`, as OI-332 records at the object. "
            "The row's own words: \"The document's substance is accurate; only its coordinates are "
            "wrong.\""
        ),
        "matched_worked_example": "stale anchor or a formatting artifact",
        "verdict": "OUT — the doc-sync half does not reach it",
        "why": (
            "It is the ruling's third worked example word for word: a stale code anchor. Nothing a "
            "reader concludes about the analysis changes — the mechanism the document specifies "
            "and the code that implements it are both exactly as described, and only the "
            "coordinates a reader would use to find the code have moved. D-307 already forbids "
            "citing code by line number at all, so what is owed here is the D-307 fix, which the "
            "doc-sync half is not the instrument for."
        ),
    },
    {
        "document": "docs/stage4c_cadence_key_design.md",
        "what_the_document_says_about_itself": (
            "It is banner-marked \"DRAFT — ratification-gated\" and carries one inline supersession "
            "note, on the gate figures in its §4c-ii — so it has been touched since it was written."
        ),
        "what_is_true_at_head": (
            "The key-agnostic local cadence detector the document builds toward was FALSIFIED at "
            "its precision ceiling on 2026-06-15, one day after the document was written (D-290), "
            "and the document carries no note of it."
        ),
        "matched_worked_example": "missing supersession note on a superseded plan",
        "verdict": "IN — the doc-sync half reaches it",
        "why": (
            "It is the ruling's second worked example word for word. Without the note a reader "
            "takes the detector as a live design to be built; with it, the detector is a closed "
            "approach and what survives is the §3 scope constraint and the §1 grading discipline, "
            "which OI-332 already separates out (D-616, D-617). The same text is read as two "
            "different things depending on a fact the document does not carry — which is exactly "
            "what the test asks."
        ),
    },
]


def read(path: str) -> str:
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def locate_ruling() -> dict:
    text = read(CLAUDE_MD)
    i = text.find(RULING_ANCHOR)
    if i < 0:
        raise SystemExit("STOP: the R1 ruling's anchor is not in CLAUDE.md — this derivation "
                         "cannot rest on a ruling it did not locate.")
    j = text.find(RULING_END, i)
    if j < 0:
        raise SystemExit("STOP: the R1 ruling's closing anchor is not in CLAUDE.md.")
    return {
        "located_by": "anchor string, never a line number (the OI-330 lesson)",
        "verbatim": re.sub(r"\s+", " ", text[i:j]).strip(),
    }


def build() -> dict:
    ruling = locate_ruling()
    oi332 = read(OI332)

    for v in VERDICTS:
        if v["document"] not in oi332:
            raise SystemExit(f"STOP: OI-332 does not carry {v['document']}; the population this "
                             "tool grades is the row's own and may not be authored beside it.")
        if v["matched_worked_example"] is not None and \
                v["matched_worked_example"] not in WORKED_EXAMPLES:
            raise SystemExit(f"STOP: {v['document']} names a worked example the ruling does not "
                             f"state: {v['matched_worked_example']!r}")

    undecided = [v["document"] for v in VERDICTS if v["matched_worked_example"] is None]
    inside = [v["document"] for v in VERDICTS if v["verdict"].startswith("IN")]
    outside = [v["document"] for v in VERDICTS if v["verdict"].startswith("OUT")]

    return {
        "purpose": (
            "Ruling R1 applied: how far phase 1's doc-sync half reaches into a document's account "
            "of itself, tested on the three documents `OPEN_ITEMS.md` OI-332 carries."
        ),
        "generated_by": "tools/audit/decisions/gen_true_half_reach.py",
        "generated_for": "cc_instruction_phase1_delegations_and_corrections.md",
        "the_ruling": {
            "who_and_when": "User, 2026-08-04. Homed at `CLAUDE.md`, the D-231 phase-1 clause; "
                            "register entry D-639.",
            "worked_examples_that_ARE_the_test": WORKED_EXAMPLES,
            **ruling,
        },
        "the_fallback": {
            "what_it_is": (
                "Option (1A) — the doc-sync half reaches only the account of the ANALYSIS — which "
                "the ruling states as the answer if the test needs judgment on the first rows it "
                "meets, that being the \"stable enough to be cited\" failure repeating."
            ),
            "was_it_reached": bool(undecided),
            "how_that_is_decided_here": (
                "DERIVED, not declared: a document matching none of the three worked examples is "
                "one the test did not decide. Each verdict below names the example it matched, so "
                "an unmatched document cannot be argued into a verdict silently."
            ),
            "documents_the_test_did_not_decide": undecided,
        },
        "verdicts": VERDICTS,
        "counted": {
            "documents_graded": len(VERDICTS),
            "inside_the_doc_sync_half": len(inside),
            "outside_it": len(outside),
            "undecided_and_therefore_governed_by_the_fallback": len(undecided),
        },
        "the_gate_consequence_this_ruling_carries": {
            "what_moves": (
                "OI-332's own classification. The row classes itself APPARATUS under D-438, on the "
                "ground that \"Two of the three are pointers and a banner — the line the "
                "non-gating declaration draws explicitly names a pointer, an anchor, a label, a "
                "banner as apparatus.\" That reads one half of D-438's line. The same sentence "
                "continues: \"a correction to a statement about the analysis OR ITS BUILD STATE, "
                "or the completion of a specification, GATES.\" A banner that says a design has no "
                "code when both its operations are built is a statement about the build state."
            ),
            "why_it_is_reported_and_not_applied_here": (
                "The verdict set is DERIVED, never hand-listed — `CLAUDE.md` forbids hand-adding a "
                "verdict for a row the first cut never reached, and "
                "`tools/audit/gen_nongating_apparatus_rows.py` is the one place a verdict is "
                "authored. Moving this one is a change to that tool's authored table and to a "
                "published classification, which is the user's to rule on. It is stated here so it "
                "cannot be missed, and rowed."
            ),
            "which_of_the_three_carries_it": [
                {"document": "cowork_layer1_extend_design.md",
                 "why": "a banner asserting NO CODE over two built operations — a statement about "
                        "the build state"},
                {"document": "docs/stage4c_cadence_key_design.md",
                 "why": "a design whose approach the record falsified, with no note saying so — a "
                        "statement about the analysis"},
            ],
            "which_does_not": [
                {"document": "cowork_layer3_reachback_design.md",
                 "why": "a stale code anchor, which D-438's own line names as apparatus and which "
                        "R1 places outside the doc-sync half"},
            ],
        },
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    art = build()
    text = json.dumps(art, indent=2, ensure_ascii=False) + "\n"
    if args.check:
        have = read(OUT) if os.path.exists(OUT) else ""
        if have != text:
            print("STALE vs the files: true_half_reach.json does not re-derive")
            return 1
        print("the R1 application re-derives from the files")
        return 0
    with open(OUT, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    c = art["counted"]
    print(f"wrote {os.path.relpath(OUT, ROOT)}")
    print(f"  {c['documents_graded']} documents graded: {c['inside_the_doc_sync_half']} IN, "
          f"{c['outside_it']} OUT, {c['undecided_and_therefore_governed_by_the_fallback']} "
          f"undecided")
    print(f"  fallback reached: {art['the_fallback']['was_it_reached']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
