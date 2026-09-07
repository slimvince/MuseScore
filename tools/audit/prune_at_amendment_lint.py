#!/usr/bin/env python3
"""THE PRUNE-AT-AMENDMENT RULE, GIVEN SOMETHING THAT WATCHES IT.

THE ORDER THIS EXISTS FOR.  The user, 2026-09-07, in his own words: *"1. tidy the mess that was
caused by this rule not being followed. 2. make sure this rule is being followed from now on."*
This file is half two.  The rule is §5(D) of `cowork_rulings_2026_08_16_preparation_return.md`,
quoted to its own sentence ends (D-643):

    "From this ruling, any edit to a governing document that supersedes, amends or closes some
     part of it MOVES the newly superseded text, in the SAME act, to its archive home — verbatim,
     with the move recorded, on the established archive pattern. The site keeps a compact, dated
     supersession pointer naming where the former text now lives, so the supersession stays
     visible where it happened."

    "This SUPERSEDES the preserve-in-place default for governing-document amendments (the pattern
     principles #8's and #10's own amendments used, and which the D-231 rephrasing was ruled
     under — 'the former wording preserved in place')."

WHAT IT FAILS ON, AND WHAT IT PASSES.  It FAILS when a governing document carries a span saying
that its OWN former wording is preserved IN PLACE — the one pattern the rule explicitly supersedes
— and it PASSES when a supersession is recorded as a POINTER naming where the former text now
lives, which is what the rule asks for instead.  Both classes are published, so a reader sees what
it catches and what it treats as compliant rather than only a verdict.

★ THE ONE CUT IT MAKES, AND WHY IT IS DERIVED FROM THE RULE'S OWN DATE RATHER THAN AUTHORED.  Rule
(D) was ruled on a date.  A preserve-in-place statement dated AT OR BEFORE that date was the
lawful pattern when it was written — it is PRE-RULE BACKLOG, reported and not failed.  One dated
AFTER it, or carrying no date at all, is a BREACH and fails.  The cut is the rule's own effective
date read from the record, not a judgment about which spans deserve an exception; and it is what
makes this a check on the rule being followed FROM NOW ON rather than a check that is red forever
because of text written before the rule existed.

★ THE RECOGNIZER IS IMPORTED, NOT COPIED (#6).  Its one home is
`gen_claude_md_prune_backlog.py`, the act that derived the phrasings from what the five governing
files actually say.  A phrasing added there is watched here on the same day, and the two cannot
drift apart.  The standing archive-pointer constraint rides with it: a marker inside an archive
pointer line never places a span, because a pointer QUOTES the opening of what it points at.

★ ITS ENROLLED SCOPE IS `CLAUDE.md` ALONE, and that is a scope decision rather than a measurement.
The user's order of 2026-09-07 names `CLAUDE.md`; the other four governing documents are outside
it.  So the exit code is decided by the scope file, and every hit in the other four is REPORTED as
a finding for the user to rule on.  Widening the scope is the user's.

★ WHAT IT DOES NOT DO.  It asserts no cause and proposes no remedy.  It does not say a flagged
span should move — an archiving act reads a span whole before anything moves, and that reading is
a different question from whether the pattern is present.  It edits no document.

WHAT IS DERIVED AND WHAT IS AUTHORED.
  DERIVED   the span population of each governing file at the tree as it stands; every hit, every
            near miss and every compliant record; each hit's own date; every count.
  AUTHORED  the compliant-record phrasings, derived by searching the five files for how the record
            actually writes a pointer, and published on this file's face.

THE STOPS:
  * a governing file the ruling names that the tree does not carry halts it;
  * a hit the date rule cannot place — no date anywhere in the span — is a BREACH rather than a
    skip, so a statement cannot escape the check by carrying no date.

Run:
    python tools/audit/prune_at_amendment_lint.py            # report, and write the artifact
    python tools/audit/prune_at_amendment_lint.py --check     # report, writing nothing
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

sys.path.insert(0, HERE)
from output_encoding import use_utf8_output              # noqa: E402  (path set above)
import gen_governing_surface_spans as coarse             # noqa: E402  the files and the cut
import gen_claude_md_finer_spans as finer                # noqa: E402  CLAUDE.md's own cut
import gen_claude_md_prune_backlog as backlog            # noqa: E402  THE recognizer (#6)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

OUT = os.path.join(HERE, "prune_at_amendment_lint.json")

# The scope the user's order of 2026-09-07 names. A hit outside it is reported, never acted on.
ENROLLED_SCOPE = "CLAUDE.md"

BACKLOG_VERDICT = "PRE-RULE BACKLOG — reported, not failed"
BREACH_VERDICT = "BREACH — the preserve-in-place pattern used after rule (D) was ruled"
UNDATED_VERDICT = "BREACH — the span carries no date, so it cannot be placed before the rule"

# ── AUTHORED — how the record writes a COMPLIANT supersession, derived from the five files ─────
# Each phrasing below was taken by searching the five governing files for a supersession recorded
# as a pointer. They are what the record uses; none was added on the strength of what a document
# might say. The archive-pointer LINE itself is imported rather than restated (#6).
COMPLIANT_MARKERS = (
    r"(?i)moved verbatim to `[A-Z_]+\.md`",
    r"(?i)→ ARCHIVED \d{4}-\d{2}-\d{2}: the full row is in `[A-Z_]+\.md`",
    r"(?i)is preserved in D-\d+'s provenance",
)


class Stop(Exception):
    """A demand of the check is unmet. Never a warning."""


def read(path: str) -> str:
    full = os.path.join(ROOT, path)
    if not os.path.exists(full):
        raise Stop(f"a governing file the ruling names is not in the tree: {path}")
    with open(full, "r", encoding="utf-8", newline="") as fh:
        return fh.read()


def spans_of(name: str, text: str) -> list[dict]:
    """The file's spans, at the unit that file's own record uses.

    `CLAUDE.md` has a finer unit, commissioned by Ruling 4 of
    `cowork_rulings_2026_08_17_sixth_return.md` after the coarse one was MEASURED wrong for it
    (finding F33). Using the coarse unit here would reproduce that over-grab inside this check's
    own report, so each file is cut at the unit its own record settled on.
    """
    mod = finer if name == "CLAUDE.md" else coarse
    spans, _blank = mod.spans_of(text)
    return spans


def scan(name: str) -> dict:
    text = read(name)
    hits, near_misses, compliant = [], [], []
    for span in spans_of(name, text):
        body = span["text"]
        found = backlog.preserve_in_place_hits(body)
        regions = finer.archive_pointer_regions(body)
        record = {
            "file": name,
            "first_line": span["first_line"],
            "last_line": span["last_line"],
            "characters": len(body),
            "the_opening": " ".join(body.split())[:160],
        }
        if found:
            date = backlog.statement_date(body)
            if date is None:
                verdict = UNDATED_VERDICT
            elif date <= backlog.RULE_D_RULED_ON:
                verdict = BACKLOG_VERDICT
            else:
                verdict = BREACH_VERDICT
            hits.append(dict(record,
                             the_marker_matched=found[0].group(0),
                             markers_in_the_span=len(found),
                             the_date_the_span_carries=date,
                             the_verdict=verdict))
            continue
        # A NEAR MISS: the span carries a former-wording marker of the family this recognizer sits
        # beside, and this recognizer does not place it. Published so a reader sees what the check
        # lets through rather than only what it catches.
        for pattern in coarse.FORMER_WORDING_MARKERS:
            m = re.search(pattern, body)
            if m and not finer.inside_a_pointer(m.start(), regions):
                near_misses.append(dict(record, the_marker_it_carries=m.group(0)))
                break
        for pattern in COMPLIANT_MARKERS:
            m = re.search(pattern, body)
            if m:
                compliant.append(dict(record, the_pointer_form=m.group(0)))
                break
        else:
            if any(finer.ARCHIVE_POINTER.match(line) for line in body.splitlines(keepends=True)):
                compliant.append(dict(record, the_pointer_form="an archive pointer line"))
    return {"hits": hits, "near_misses": near_misses, "compliant": compliant}


def build(scope: str) -> dict:
    per_file = {name: scan(name) for name in coarse.FILES}
    breaches = {name: [h for h in f["hits"] if h["the_verdict"] != BACKLOG_VERDICT]
                for name, f in per_file.items()}
    return {
        "what_this_is":
            "THE PRUNE-AT-AMENDMENT CHECK: every span of a governing document saying that its OWN "
            "former wording is preserved IN PLACE — the pattern rule (D) supersedes — with each "
            "one placed before or after the date that rule was ruled, beside every near miss and "
            "every supersession the record writes as a POINTER instead. It asserts no cause and "
            "proposes no remedy; it reports. Every figure here is computed (D-431).",
        "generated_by": "tools/audit/prune_at_amendment_lint.py",
        "dispatch": f"{backlog.DISPATCH}, Task 3",
        "the_order_it_serves":
            "the user, 2026-09-07: \"make sure this rule is being followed from now on.\"",
        "the_rule": {
            "where_it_lives": backlog.RULE_D,
            "ruled_on": backlog.RULE_D_RULED_ON,
            "what_it_requires": "an edit to a governing document that supersedes part of it MOVES "
                                "the newly superseded text, in the SAME act, to its archive home, "
                                "and the site keeps a compact dated pointer naming where the "
                                "former text now lives.",
            "what_it_supersedes": "the preserve-in-place default for governing-document "
                                  "amendments — \"the former wording preserved in place\".",
        },
        "★_the_recognizer_and_where_it_lives": {
            "its_one_home": "tools/audit/gen_claude_md_prune_backlog.py — IMPORTED here, never "
                            "copied (#6), so a phrasing added there is watched here the same day",
            "the_phrasings": list(backlog.PRESERVE_IN_PLACE_MARKERS),
            "the_standing_pointer_constraint_rides_with_it": finer.POINTER_CONSTRAINT,
        },
        "★_the_date_cut": {
            "the_rule": f"a preserve-in-place statement dated at or before {backlog.RULE_D_RULED_ON} "
                        f"was the lawful pattern when it was written and is PRE-RULE BACKLOG; one "
                        f"dated after it is a BREACH; one carrying no date at all is a BREACH, so "
                        f"a statement cannot escape the check by carrying none.",
            "why_it_is_derived_rather_than_authored":
                "it is the rule's own effective date read from the record, not a judgment about "
                "which spans deserve an exception. Without it this check would be red forever on "
                "text written before the rule existed, and a check that is red at every tree "
                "teaches a reader to ignore it — which is the failure the guard set exists against.",
        },
        "★_the_enrolled_scope_and_why_it_is_one_file": {
            "the_scope": scope,
            "the_ground": "the user's order of 2026-09-07 names `CLAUDE.md`. The other four "
                          "governing documents are outside it, so a hit in them is REPORTED as a "
                          "finding and not acted on; widening the scope is the user's.",
        },
        "the_reach_measured_in_both_directions": {
            "what_this_is": "what the check CATCHES and what it would LET THROUGH, over all five "
                            "governing documents, measured before it was enrolled — because a "
                            "check that fires on four files nobody asked to change is a different "
                            "act from the one that was ordered.",
            "★_what_a_near_miss_is": "a span carrying a former-wording marker of the family this "
                                     "recognizer sits beside, which this recognizer does not "
                                     "place. It is what the check lets through, published so the "
                                     "bound is readable rather than assumed (#19).",
            "per_file": {
                name: {
                    "hits": len(f["hits"]),
                    "of_which_pre_rule_backlog":
                        len([h for h in f["hits"] if h["the_verdict"] == BACKLOG_VERDICT]),
                    "of_which_breaches": len(breaches[name]),
                    "near_misses": len(f["near_misses"]),
                    "supersessions_recorded_as_a_pointer": len(f["compliant"]),
                } for name, f in per_file.items()},
        },
        "the_verdict": {
            "scope": scope,
            "breaches_in_the_enrolled_scope": len(breaches[scope]),
            "passes": not breaches[scope],
            "★_what_a_pass_says_and_what_it_does_not":
                "SAYS: no span of the scope file uses the superseded preserve-in-place pattern "
                "with a date after the rule was ruled. DOES NOT SAY: that the pre-rule backlog is "
                "cleared — it is reported above and stays; nor that a flagged span should move, "
                "which an archiving act decides by reading the span whole.",
            "breaches_in_the_other_governing_documents":
                {name: len(b) for name, b in breaches.items() if name != scope and b},
        },
        "the_findings": {
            name: {
                "hits": f["hits"],
                "near_misses": f["near_misses"],
                "supersessions_recorded_as_a_pointer": f["compliant"],
            } for name, f in per_file.items()},
        "★_the_compliant_phrasings_and_where_they_come_from": {
            "the_phrasings": list(COMPLIANT_MARKERS),
            "plus": "any span carrying an archive-pointer line, imported from the finer pass",
            "where_they_come_from": "a search of the five governing files for how the record "
                                    "actually writes a supersession as a pointer.",
        },
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="report, writing nothing")
    ap.add_argument("--scope", default=ENROLLED_SCOPE, choices=sorted(coarse.FILES),
                    help="the file whose breaches decide the exit code")
    args = ap.parse_args()

    art = build(args.scope)
    if not args.check:
        with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(json.dumps(art, indent=1, ensure_ascii=False) + "\n")
        print("wrote", os.path.relpath(OUT, ROOT))

    reach = art["the_reach_measured_in_both_directions"]["per_file"]
    for name, cell in reach.items():
        mark = "  <= enrolled scope" if name == args.scope else ""
        print(f"  {name:<20} hits {cell['hits']:>2} "
              f"(backlog {cell['of_which_pre_rule_backlog']}, breach {cell['of_which_breaches']}), "
              f"near misses {cell['near_misses']:>2}, "
              f"pointers {cell['supersessions_recorded_as_a_pointer']:>3}{mark}")
    v = art["the_verdict"]
    if v["breaches_in_the_other_governing_documents"]:
        print(f"  REPORTED, not acted on — breaches outside the enrolled scope: "
              f"{v['breaches_in_the_other_governing_documents']}")
    print(f"  {args.scope}: {'PASS' if v['passes'] else 'FAIL'} — "
          f"{v['breaches_in_the_enrolled_scope']} breach(es) in the enrolled scope")
    return 0 if v["passes"] else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Stop as exc:
        print("STOP:", exc)
        raise SystemExit(2)
