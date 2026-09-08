#!/usr/bin/env python3
"""HOW MUCH OF THE SESSION-START READ OF `CLAUDE.md` IS EXPLICITLY-MARKED DEFENSE — a LOWER BOUND.

WHY THIS EXISTS.  The user ruled on 2026-09-08 that a rule's DEFENSE may live in a satellite
provided the rule's home carries a POINTER to it, the rule itself not moving
(`cowork_rulings_2026_09_08_defense_satellite_sitting.md`, Ruling 1, amending the defense-at-home
convention **D-195**).  The writing side then recorded a correction it owed on its own surface:
that ruling's reach is the defense material across ALL SIX session-start spans, and it is
UNMEASURED.  This tool measures it.  It is a MEASUREMENT ONLY: it moves no text, edits nothing,
proposes nothing and grades nothing.

WHAT IT MEASURES.  For each of the six SESSION-START spans of `CLAUDE.md`, the characters standing
inside explicitly-marked defense clauses.

WHERE THE SPANS COME FROM.  They are IMPORTED from `gen_session_start_read_size.py`, which parses
them out of `CLAUDE.md`'s own membership block.  Nothing here re-implements that parse, re-locates
a heading, or carries a line number for a span (**D-307**, #6): a later amendment of the membership
moves this measurement without anybody editing this tool, exactly as it moves the read-size
measurement.  The coordinates arrive through that reader's `with_coordinates` parameter, which
exists for this caller and reaches no published artifact -- see that function's own docstring.

WHAT IS AUTHORED AND WHAT IS DERIVED
------------------------------------
authored : the MARKER TABLE -- three forms of run that open a defense clause.  It is a judgment
           about how this record writes a defense, and its reach is UNMEASURED, which is why the
           published value is a LOWER BOUND and says so of itself (**D-673**).
derived  : every span, every match, every extent, every count and both denominators.  No value is
           transcribed (**D-431**).

HOW A RUN IS MATCHED.  By the `ITALIC` and `BOLD` regular expressions the read-size tool already
carries, imported rather than rewritten (#6).  Those two are what keep a bold run out of the italic
population and the other way round; a fresh pattern here would be a second home for that decision,
and the marker table shipped by an earlier issue of this arc was defective precisely because it
admitted one emphasis and one punctuation mark where the file uses two of each.

HOW FAR A MARKED CLAUSE REACHES.  From the first character of the marker through the end of the
paragraph containing it, using the imported `_paragraph_end`, bounded by the span's own `hi` -- AND
CLOSED AT THE NEXT MARKED CLAUSE where one opens before that paragraph ends.  A marked clause never
extends past its span.

★ THAT LAST CLOSING RULE IS A DECLARED DEPARTURE FROM THE DISPATCH'S LITERAL WORDING, TAKEN ON A
MEASUREMENT AND RECORDED HERE, ON THE ARTIFACT AND IN THE BATCH'S REPORT (2026-09-08).  The
dispatch that ordered this tool fixes the extent as *"from the first character of the marker through
the end of the paragraph containing it"* and, separately, makes *"no two overlap"* and *"a span's
clause characters do not exceed that span's own count"* establishment STOPs.  AT THIS TREE THOSE
CANNOT BOTH HOLD, and it is not a near thing: `CLAUDE.md` routinely writes one bullet's marked
defense immediately followed by a second one inside the SAME paragraph, so under the literal rule
both run to the same paragraph end and overlap.  Measured before anything was decided, and
published on this tool's own artifact rather than typed into this comment (#17f, D-431): the
literal rule attributes to the six spans far more characters than those six spans hold in total,
and it does so in every span that carries a clause at all.

WHY THE CLOSING RULE IS THE FAITHFUL READING RATHER THAN A CONVENIENCE.  The quantity the dispatch
NAMES is *"the characters standing inside explicitly-marked defense clauses"*, and a character
standing inside two clauses is ONE character; the two establishment STOPs above are what say so,
since both are violated only by double-counting.  And the repair preserves exactly what is
measured: for
clauses ordered by their start and ending at one paragraph end, the union of the untruncated
extents and the union of the closed ones are THE SAME CHARACTER SET.  What changes is only that a
character is counted once.  The literal sum is published below anyway, beside the count of
overlapping pairs, so the reading side can see both and rule without re-running anything (#12).

THE STOPS -- every one of them an establishment taken POSITIVELY on every run (#19), and a STOP
rather than a reported field, because a measurement that reports its own unsoundness as a field is
one a reader can skip:
  * other than SIX session-start spans is a STOP -- the membership ruled six, and a reader that
    returned five would publish a share of the wrong denominator;
  * a marker row matching NOTHING is a STOP -- a dead row is a defect in the authored table, and
    an earlier issue of this arc shipped one that matched nothing at all;
  * a measured clause not lying wholly inside the span it is attributed to is a STOP;
  * two clauses overlapping AFTER the closing rule above is a STOP -- the closing rule removes the
    overlaps the record's own paragraphs create, so anything still overlapping is a shape this tool
    does not understand, and a total that double-counts is worse than no total;
  * a clause left holding nothing by the closing rule is a STOP -- two markers at one position is a
    shape this tool does not understand either, and a zero-character clause would sit in the
    published table looking measured;
  * a span's clause characters exceeding that span's own count is a STOP, which is the same defect
    caught from the other side;
  * the six spans' re-derived total disagreeing with the reader's own is a STOP;
  * the known unemphasised miss no longer locatable, or locatable twice, is a STOP -- it is named
    on the artifact as a miss, and a named miss that has moved must not be asserted;
  * `--check` re-derives the artifact and compares rendered text.

WHAT THIS DOES NOT CLAIM.  That any marked clause is MOVABLE -- movability is Ruling 1's question
and this tool answers none of it.  That any unmarked passage is not a defense; the bound below says
the opposite.  That the value is what a satellite would remove.  And it consumes
`cowork_claude_md_live_rule_classification_2026_09_08.md` not at all -- that file is not read here.

Run:
    python tools/audit/gen_defense_share.py
    python tools/audit/gen_defense_share.py --check
"""
from __future__ import annotations

import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(HERE, "defense_share.json")

sys.path.insert(0, HERE)
from output_encoding import use_utf8_output              # noqa: E402  (path set above)
import gen_session_start_read_size as reader             # noqa: E402  (path set above)

use_utf8_output()   # OI-297 -- the findings must survive a non-console stdout

# -- AUTHORED: the three forms of run that open a defense clause. --------------------------------
#
# Each is matched against the CONTENT of a run the imported `ITALIC` or `BOLD` pattern found, so
# the emphasis half is never re-decided here.  The punctuation each row admits is DERIVED FROM THE
# FILE rather than guessed: the record writes `Why:`, `Why ` and `Why,`; `Evidence:`; and both
# `Founding instance:` and `Founding instance,`.  An earlier issue of this arc admitted a colon
# alone on two of these rows -- which made one row match nothing at all, and made the other
# silently LOWER the value by missing the comma form.  The zero-match STOP above is the check that
# catches the first of those; only reading the file catches the second, which is why the widening
# is recorded here at the table rather than left in a report.
MARKERS: tuple[tuple[str, str], ...] = (
    ("Why followed by a space, a colon or a comma", r"Why[ :,]"),
    ("Evidence followed by a colon", r"Evidence:"),
    ("Founding instance followed by a colon or a comma", r"Founding instance[:,]"),
)
MARKER_PATTERNS = tuple((label, re.compile("^" + body)) for label, body in MARKERS)

# -- AUTHORED: one defense the table deliberately does NOT admit, named as a known miss. ----------
#
# It is a PLAIN, UNEMPHASISED clause, and admitting it would mean a pattern over unemphasised prose
# -- which would match ordinary text, so the doubt default keeps the table narrow.  It is located
# on every run rather than asserted, and the locator tolerates a LINE BREAK inside the phrase
# because the phrase wraps in the file: a single-line search for the whole of it finds nothing,
# which is a mistake this arc has now made three times.
KNOWN_MISS = re.compile(r"Founding instances of the\s+gap:")
KNOWN_MISS_WHAT = ("a plain, unemphasised clause opening `Founding instances of the gap:`, in the "
                   "Conventions span, inside the bullet requiring every design decision to carry "
                   "its defense at its home. It wraps across two lines.")


class Stop(Exception):
    """A demand of the measurement is unmet. Never a warning, never a reported field."""


def line_offsets(lines: list[str]) -> list[int]:
    """The absolute character offset at which each line begins, in the file as a reader reads it."""
    out, n = [], 0
    for line in lines:
        out.append(n)
        n += len(line) + 1          # the newline that `"\n".join` puts back
    return out


def clauses_in(span: dict, lines: list[str], offset: list[int]) -> list[dict]:
    """Every marked defense clause standing inside one span, with its extent."""
    lo, hi = span["lo"], span["hi"]
    text = "\n".join(lines[lo:hi])
    found = []
    for emphasis, pattern in (("bold", reader.BOLD), ("italic", reader.ITALIC)):
        for match in pattern.finditer(text):
            run = match.group(1)
            for label, marker in MARKER_PATTERNS:
                if not marker.match(run):
                    continue
                start_line = lo + text.count("\n", 0, match.start(1))
                end_line = reader._paragraph_end(lines, start_line, hi)
                column = match.start(1) - (offset[start_line] - offset[lo])
                begins = offset[start_line] + column
                ends = offset[end_line - 1] + len(lines[end_line - 1])
                found.append({
                    "the_span_it_stands_in": span["name"],
                    "the_marker_row_it_matched": label,
                    "emphasis": emphasis,
                    "first_line": start_line + 1,
                    "the_marked_run_as_written": run.replace("\n", " ")[:120],
                    "_begins": begins,
                    "_ends": ends,
                    "_paragraph_ends": ends,
                })
                break
    found.sort(key=lambda c: c["_begins"])
    return found


def close_at_the_next_clause(found: list[dict], lines: list[str], offset: list[int]) -> int:
    """Close each clause where the next one opens inside it. Returns the number closed.

    ★ THE DECLARED DEPARTURE, IMPLEMENTED IN ONE PLACE (#6) -- see this module's docstring for the
    measurement that forced it and for the proof that it preserves the character set exactly. Its
    whole content is: a clause reaches the end of its paragraph OR the next marked clause,
    whichever comes first.
    """
    closed = 0
    for earlier, later in zip(found, found[1:]):
        if later["_begins"] < earlier["_ends"]:
            earlier["_ends"] = later["_begins"]
            earlier["_closed_at_the_next_clause"] = True
            closed += 1
    for clause in found:
        clause.setdefault("_closed_at_the_next_clause", False)
        end = clause["_ends"]
        last = next(i for i in range(len(offset) - 1, -1, -1) if offset[i] < end)
        clause["last_line"] = last + 1
        clause["characters"] = end - clause["_begins"]
        clause["it_was_closed_at_the_next_marked_clause"] = clause["_closed_at_the_next_clause"]
        clause["characters_had_it_run_to_the_paragraph_end"] = \
            clause["_paragraph_ends"] - clause["_begins"]
    return closed


def build() -> dict:
    claude_md = reader.at_tree("CLAUDE.md")
    reading = reader.claude_md_reading(claude_md, with_coordinates=True)
    whole_read = reader.measure(claude_md, reader.at_tree)["total_characters"]

    spans = [s for s in reading.get("the_session_start_spans", [])
             if s["kind"] == "session start"]
    if len(spans) != 6:
        raise Stop("the reader returned %d session-start span(s) and the ruled membership names "
                   "six -- a share taken over any other number is a share of the wrong "
                   "denominator" % len(spans))

    lines = claude_md.split("\n")
    offset = line_offsets(lines)

    per_span, clauses = [], []
    closed_total, literal_total = 0, 0
    for span in spans:
        mine = clauses_in(span, lines, offset)
        closed_total += close_at_the_next_clause(mine, lines, offset)
        literal_total += sum(c["characters_had_it_run_to_the_paragraph_end"] for c in mine)
        for c in mine:
            if c["characters"] <= 0:
                raise Stop("a marked clause at line %d is left holding nothing once closed at the "
                           "next one -- two markers at one position is a shape this tool does not "
                           "understand" % c["first_line"])
        held = sum(c["characters"] for c in mine)
        if held > span["characters"]:
            raise Stop("the clauses attributed to the span %r hold %d characters and the span "
                       "itself is %d -- the extents double-count"
                       % (span["name"], held, span["characters"]))
        span_lo = offset[span["lo"]]
        span_hi = offset[span["hi"] - 1] + len(lines[span["hi"] - 1])
        for c in mine:
            if c["_begins"] < span_lo or c["_ends"] > span_hi:
                raise Stop("a clause attributed to the span %r at lines %d-%d does not lie wholly "
                           "inside it" % (span["name"], c["first_line"], c["last_line"]))
        per_span.append({
            "name": span["name"],
            "characters": span["characters"],
            "marked_clauses": len(mine),
            "characters_those_clauses_hold": held,
            "characters_had_every_clause_run_to_its_paragraph_end":
                sum(c["characters_had_it_run_to_the_paragraph_end"] for c in mine),
            "share_of_this_span": round(100.0 * held / span["characters"], 2)
            if span["characters"] else 0.0,
        })
        clauses.extend(mine)

    clauses.sort(key=lambda c: c["_begins"])
    for earlier, later in zip(clauses, clauses[1:]):
        if later["_begins"] < earlier["_ends"]:
            raise Stop("two marked clauses overlap -- lines %d-%d and %d-%d. Overlapping extents "
                       "double-count, and a total that double-counts is worse than no total"
                       % (earlier["first_line"], earlier["last_line"],
                          later["first_line"], later["last_line"]))

    six_spans = sum(s["characters"] for s in per_span)
    if six_spans != reading["characters"]:
        raise Stop("the six spans re-derive to %d characters and the reader's own total is %d"
                   % (six_spans, reading["characters"]))

    rows = []
    for label, body in MARKERS:
        hits = [c for c in clauses if c["the_marker_row_it_matched"] == label]
        if not hits:
            raise Stop("the marker row %r matched NOTHING. A dead row is a defect in the authored "
                       "table, not an absence of defenses" % label)
        rows.append({
            "the_row": label,
            "matched_against": "the content of a run the imported ITALIC or BOLD pattern found",
            "the_opening_it_admits": body,
            "matches": len(hits),
            "in_bold": sum(1 for c in hits if c["emphasis"] == "bold"),
            "in_italics": sum(1 for c in hits if c["emphasis"] == "italic"),
        })

    misses = list(KNOWN_MISS.finditer(claude_md))
    if len(misses) != 1:
        raise Stop("the known unemphasised miss is locatable %d time(s) in `CLAUDE.md` and it must "
                   "be exactly one -- a named miss that has moved must not be asserted"
                   % len(misses))
    miss_line = claude_md.count("\n", 0, misses[0].start()) + 1
    miss_span = next((s["name"] for s in spans
                      if s["lo"] < miss_line <= s["hi"]), "outside every session-start span")

    held_total = sum(c["characters"] for c in clauses)
    return {
        "what_this_is":
            "HOW MUCH OF THE SESSION-START READ OF `CLAUDE.md` IS EXPLICITLY-MARKED DEFENSE, in "
            "characters, measured at the tree. A MEASUREMENT ONLY: it moves no text, proposes "
            "nothing and grades nothing. Every value is computed; none is transcribed (D-431).",
        "generated_by": "tools/audit/gen_defense_share.py",
        "generated_for": "cc_instruction_defense_share_sizing_third_2026_09_08.md, Task 2",
        "★_THE_PUBLISHED_VALUE_IS_A_LOWER_BOUND_AND_THIS_IS_ITS_DECLARED_BOUND": {
            "the_bound": "THE MARKER SET'S REACH IS UNMEASURED. A defense written without one of "
                         "these markers is NOT COUNTED, so every total below is a LOWER BOUND on "
                         "the defense material standing in the six session-start spans -- never an "
                         "estimate of it, and never a ceiling.",
            "why_it_is_stated_rather_than_left_implicit":
                "D-673: an enumerating pattern whose reach is unmeasured may state its bound on "
                "its own artifact. The test that clause fixes is met here -- no analysis decision "
                "consumes this enumeration; it sizes a documentation question.",
            "a_known_miss_re_located_on_every_run_rather_than_asserted": {
                "what_it_is": KNOWN_MISS_WHAT,
                "why_it_is_deliberately_not_admitted":
                    "admitting it would mean a pattern over UNEMPHASISED prose, which would match "
                    "ordinary text. The doubt default keeps the table narrow.",
                "found_at_line": miss_line,
                "the_span_it_stands_in": miss_span,
                "how_it_is_located": "by a pattern tolerating a line break inside the phrase, "
                                     "because it wraps -- a single-line search for the whole "
                                     "phrase finds nothing.",
            },
            "what_the_bound_does_NOT_say":
                "that these three forms are the only ones the record uses; that an unmarked "
                "passage is not a defense; or that the miss above is the only one.",
        },
        "how_a_marked_clause_is_bounded":
            "from the first character of the marker through the end of the paragraph containing "
            "it, using the reader's own `_paragraph_end`, bounded by the span's own end, AND "
            "closed at the next marked clause where one opens before that paragraph ends. A "
            "marked clause never extends past its span, and that is checked rather than assumed.",
        "★_THE_CLOSING_RULE_IS_A_DECLARED_DEPARTURE_FROM_THE_DISPATCH_S_LITERAL_WORDING": {
            "what_the_dispatch_says": "cc_instruction_defense_share_sizing_third_2026_09_08.md "
                                      "fixes the extent as `From the first character of the marker "
                                      "through the end of the paragraph containing it` and makes "
                                      "`no two overlap` and `a span's clause characters do not "
                                      "exceed that span's own count` establishment STOPs.",
            "why_both_cannot_hold_at_this_tree":
                "`CLAUDE.md` routinely puts two marked defenses in ONE paragraph, so under the "
                "literal rule both run to the same paragraph end and overlap. This is the common "
                "case here, not an edge.",
            "measured_before_anything_was_decided":
                "the literal rule attributes %d characters to the six spans, whose own total is "
                "%d, and it produces %d overlapping pair(s). Every value in this sentence is "
                "computed by this run; none is transcribed (D-431), and the per-span column "
                "`characters_had_every_clause_run_to_its_paragraph_end` below carries the same "
                "comparison span by span."
                % (literal_total, six_spans, closed_total),
            "why_the_closing_rule_is_the_faithful_reading":
                "the quantity the dispatch NAMES is the CHARACTERS standing inside marked defense "
                "clauses, and a character standing inside two clauses is one character -- which is "
                "what the two STOPs above say, since both are violated only by double-counting.",
            "and_it_preserves_exactly_what_is_measured":
                "for clauses ordered by their start and ending at one paragraph end, the union of "
                "the untruncated extents and the union of the closed ones are the SAME CHARACTER "
                "SET. What changes is only that a character is counted once.",
            "clauses_closed_at_the_next_one": closed_total,
            "the_literal_sum_published_so_the_reading_side_can_rule_without_re_running":
                literal_total,
            "★_what_is_owed_to_the_reading_side":
                "this is a MEASUREMENT DEFINITION and it belongs to the writing side. It is taken "
                "here because the ordered measurement is otherwise unproducible, and it is "
                "declared at the tool, on this artifact and in the batch's report rather than "
                "taken silently. Every per-clause record below carries BOTH its closed length and "
                "the length it would have had running to its paragraph end (#12), so the ruling "
                "costs no re-derivation whichever way it falls.",
        },
        "where_the_spans_come_from":
            "IMPORTED from `tools/audit/gen_session_start_read_size.py`, which parses them out of "
            "`CLAUDE.md`'s own membership block. Nothing here re-implements that parse, re-locates "
            "a heading, or carries a line number for a span (D-307, #6).",
        "the_marker_table": rows,
        "the_denominators_both_re_derived_through_the_imported_reader_at_this_tree": {
            "the_six_session_start_spans": six_spans,
            "the_whole_ordinary_session_start_read": whole_read,
            "why_two": "the first says how much of what a session reads OF `CLAUDE.md` is marked "
                       "defense; the second says how much of the WHOLE boot it is. A share quoted "
                       "against one of them is not the share against the other.",
        },
        "per_span": per_span,
        "the_totals": {
            "marked_clauses": len(clauses),
            "characters_those_clauses_hold": held_total,
            "share_of_the_six_session_start_spans":
                round(100.0 * held_total / six_spans, 2) if six_spans else 0.0,
            "share_of_the_whole_ordinary_session_start_read":
                round(100.0 * held_total / whole_read, 2) if whole_read else 0.0,
        },
        "every_clause_published_so_the_tables_reach_is_inspectable_rather_than_asserted":
            [{k: v for k, v in c.items() if not k.startswith("_")} for c in clauses],
        "★_the_establishment_taken_positively_on_every_run": {
            "how_it_runs": "each of these is a STOP and not a reported field: a reported field "
                           "would let a reader skip an unsound measurement.",
            "the_reader_returned_exactly_six_session_start_spans": True,
            "every_marker_row_matched_at_least_once": True,
            "every_clause_lies_wholly_inside_the_span_it_is_attributed_to": True,
            "no_two_clauses_overlap_after_the_closing_rule": True,
            "no_clause_is_left_holding_nothing_by_the_closing_rule": True,
            "no_span_s_clause_characters_exceed_that_span_s_own_count": True,
            "the_six_spans_re_derived_total_equals_the_reader_s_own": True,
            "the_known_unemphasised_miss_is_locatable_exactly_once": True,
            "what_it_does_NOT_establish":
                "that the marker table is COMPLETE. Every check above is about the measurement's "
                "internal soundness; none of them can see a defense the table does not admit, "
                "which is exactly why the bound above is declared.",
        },
        "what_this_does_not_claim": [
            "That any marked clause is MOVABLE. Movability is Ruling 1's question and nothing "
            "here answers any portion of it.",
            "That any unmarked passage is not a defense -- the declared bound says the opposite.",
            "That the value is what a satellite would remove.",
            "That `cowork_claude_md_live_rule_classification_2026_09_08.md` was consumed. It was "
            "NOT read by this tool.",
        ],
    }


def main(argv: list[str]) -> int:
    art = build()
    text = json.dumps(art, indent=1, ensure_ascii=False) + "\n"
    if "--check" in argv:
        have = reader.at_tree(os.path.relpath(OUT, ROOT).replace("\\", "/")) \
            if os.path.exists(OUT) else ""
        if have != text:
            print("STALE vs the measurement: defense_share.json does not re-derive")
            return 1
        print("the defense-share measurement re-derives")
    else:
        with io.open(OUT, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        print("wrote %s" % os.path.relpath(OUT, ROOT).replace("\\", "/"))

    for row in art["the_marker_table"]:
        print("  row %-52s matched %3d  (bold %d, italic %d)"
              % (row["the_row"][:52], row["matches"], row["in_bold"], row["in_italics"]))
    for span in art["per_span"]:
        print("  %-52s %7d of %7d  (%5.2f%%)  in %d clause(s)"
              % (span["name"][:52], span["characters_those_clauses_hold"], span["characters"],
                 span["share_of_this_span"], span["marked_clauses"]))
    tot = art["the_totals"]
    den = art["the_denominators_both_re_derived_through_the_imported_reader_at_this_tree"]
    print("  TOTAL %d character(s) in %d clause(s)"
          % (tot["characters_those_clauses_hold"], tot["marked_clauses"]))
    print("    of the six session-start spans (%d): %.2f%%"
          % (den["the_six_session_start_spans"], tot["share_of_the_six_session_start_spans"]))
    print("    of the whole session-start read (%d): %.2f%%"
          % (den["the_whole_ordinary_session_start_read"],
             tot["share_of_the_whole_ordinary_session_start_read"]))
    print("  THE VALUE IS A LOWER BOUND: the marker set's reach is UNMEASURED.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except Stop as exc:
        print("STOP: %s" % exc)
        sys.exit(2)
