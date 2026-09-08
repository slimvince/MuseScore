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
authored : the END ANCHOR TABLE -- one anchor per marked clause, in file order, each the last words
           of that clause's defense.  The judgment is published whole, with its reason per marker,
           in `cowork_defense_clause_ends_2026_09_08.md`, and every anchor is challengeable there.
derived  : every span, every match, every extent, every count and both denominators.  No value is
           transcribed (**D-431**).

HOW A RUN IS MATCHED.  By the `ITALIC` and `BOLD` regular expressions the read-size tool already
carries, imported rather than rewritten (#6).  Those two are what keep a bold run out of the italic
population and the other way round; a fresh pattern here would be a second home for that decision,
and the marker table shipped by an earlier issue of this arc was defective precisely because it
admitted one emphasis and one punctuation mark where the file uses two of each.

HOW FAR A MARKED CLAUSE REACHES -- AN AUTHORED END, READ AT THE FILE MARKER BY MARKER.  From the
first character of the marker through the end of that clause's AUTHORED END ANCHOR.

★ WHY THE MECHANICAL END WAS REPLACED, AND WHAT REPLACED IT (2026-09-08).  The end this tool used
before was the end of the paragraph containing the marker, taken through the imported
`_paragraph_end` -- WHICH WALKS FORWARD ONLY UNTIL A BLANK LINE.  In `CLAUDE.md` the guiding
principles are one numbered list with no blank line between items, and the sections for the
open-items register and for the decisions register are single unbroken blocks, so there is no
paragraph boundary where a reader sees one: a marked clause
ran from its marker to the next marker and swallowed every rule standing between them.  The value
published under that definition was therefore NOT a lower bound on defense material, as its own
artifact declared, and not a bound in either direction -- it counted live rule text as defense while
still missing every unmarked defense.  BOTH EARLIER READINGS ARE KEPT AND PUBLISHED BESIDE THE
AUTHORED ONE (#12), per clause and per span: the ruled closing reading, and the literal paragraph
reading.

★ THE CLOSING RULE IS RULED AND IS NO LONGER OUTSTANDING.  A marked clause reaching its paragraph's
end OR the next marked clause, whichever comes first, was ruled the definition on 2026-09-08 --
`cowork_rulings_2026_09_08_extent_rule_sitting.md`, §1.  `close_at_the_next_clause` below still
implements it and is still the ONE home of it (#6); what changed is that it runs over a COPY of the
extents and produces a comparison column instead of the measurement.  The block this docstring
formerly carried, declaring that rule an outstanding departure owed to the writing side, is replaced
by this pointer, the departure having been ruled.

HOW AN ANCHOR IS COMPILED, AND WHY IT IS NOT A PLAIN SEARCH.  Split on whitespace, `re.escape` each
word, join the words with `\\s+`.  Two reasons, both established at the file:
  * THREE OF THE ANCHORS WRAP ACROSS A LINE BREAK, so a plain single-line search for them finds
    nothing.  This arc has now made that mistake four times, and `KNOWN_MISS` below already uses
    exactly this technique -- so this reuses it rather than inventing a second one (#6).
  * Several anchors carry characters a regular expression treats as special.  Escaping is not
    optional.

THE STOPS -- every one of them an establishment taken POSITIVELY on every run (#19), and a STOP
rather than a reported field, because a measurement that reports its own unsoundness as a field is
one a reader can skip:
  * other than SIX session-start spans is a STOP -- the membership ruled six, and a reader that
    returned five would publish a share of the wrong denominator;
  * a marker row matching NOTHING is a STOP -- a dead row is a defect in the authored table, and
    an earlier issue of this arc shipped one that matched nothing at all;
  * THE ANCHOR COUNT NOT EQUALLING THE CLAUSE COUNT IS A STOP naming both counts -- a marker added
    to or removed from `CLAUDE.md` invalidates an authored table, and the table is then re-authored
    by the writing side, never patched by a batch;
  * AN ANCHOR NOT LOCATABLE EXACTLY ONCE inside its own clause's span is a STOP naming the anchor;
  * AN ANCHOR BEGINNING BEFORE ITS OWN MARKER, ENDING PAST ITS OWN PARAGRAPH END, ENDING AT OR AFTER
    THE NEXT MARKER, OR OUT OF FILE ORDER is a STOP;
  * AN ANCHOR LOCATED IN A SPAN OTHER THAN THE ONE THE TABLE NAMES FOR IT is a STOP -- the span
    column is authored context and is checked, never trusted;
  * a measured clause not lying wholly inside the span it is attributed to is a STOP;
  * two clauses overlapping is a STOP -- a total that double-counts is worse than no total;
  * a clause left holding nothing is a STOP -- it would sit in the published table looking measured;
  * a span's clause characters exceeding that span's own count is a STOP, which is the same defect
    caught from the other side;
  * the six spans' re-derived total disagreeing with the reader's own is a STOP;
  * the known unemphasised miss no longer locatable, or locatable twice, is a STOP -- it is named
    on the artifact as a miss, and a named miss that has moved must not be asserted;
  * `--check` re-derives the artifact and compares rendered text.

WHAT THIS DOES NOT CLAIM.  That any marked clause is MOVABLE -- movability is Ruling 1's question
and this tool answers none of it.  That any unmarked passage is not a defense; the bound below says
the opposite.  That the value is what a satellite would remove.  That an authored end is anything
but an authored judgment, challengeable at its anchor.  And it consumes
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

# -- AUTHORED: where each marked clause's defense ENDS. -------------------------------------------
#
# One row per marked clause, in FILE ORDER, each naming the span the clause stands in and the last
# words of that clause's defense.  The judgment is not taken here: it is the pass published whole,
# with its reason per marker and its two declared bounds, in
# `cowork_defense_clause_ends_2026_09_08.md`.  This table is that pass made consumable, and every
# anchor is challengeable at its own marker there.
#
# THE SPAN COLUMN IS AUTHORED CONTEXT AND IS CHECKED, NEVER TRUSTED: an anchor located in a span
# other than the one named here is a STOP.
END_ANCHORS: tuple[tuple[str, str], ...] = (
    ("Guiding principles",
     "which is the defect the catalog names DT-2."),
    ("Guiding principles",
     "would confound a structural verdict with a weighting one."),
    ("Guiding principles",
     "however convenient the invariant they share."),
    ("Guiding principles",
     "would go on reading as work outstanding rather than as an answer."),
    ("Guiding principles",
     "the condition under which that route is finished."),
    ("Guiding principles",
     "which is exactly what D-474 exists to prevent."),
    ("Guiding principles",
     "they bind on the reading of the literature rather than on the ledger."),
    ("The open-items register",
     "the establishment being the thing that made the narrower pointer admissible at all."),
    ("The open-items register",
     "#19 exists because a thing merely unfalsified is not established."),
    ("The open-items register",
     "the cost of the error in the other direction is bounded by the default above."),
    ("The open-items register",
     "so a false resolution propagates mechanically."),
    ("The open-items register",
     "forbidding the mark in prose, which is one symptom of three."),
    ("The open-items register",
     "and answers the objection rather than overriding it."),
    ("The decisions register",
     "it was never ruled to require every delegation to name sections."),
    ("The decisions register",
     "each of which produced the evidence locating its own error."),
    ("The decisions register",
     "and a status banner does not change that."),
    ("The decisions register",
     "The distinction is `ARCHITECTURE.md`'s own, not a preference."),
    ("The decisions register",
     "what keeps (i) a mechanical test rather than one with a case-by-case exception."),
    ("The decisions register",
     "and an ellipsis by anything at all."),
    ("The decisions register",
     "without the register standing in for the specification."),
    ("The decisions register",
     "which is what shows it is real rather than notional."),
    ("The decisions register",
     "what the mechanism's own output already carries, which is what #6 forbids."),
    ("The decisions register",
     "already carried at the table the adoption happened in."),
    ("The decisions register",
     "the rule the verdict bears on is elsewhere and is unmoved by it."),
    ("Conventions",
     "which is the general case, not the exception."),
    ("Conventions",
     "the reader who meets the term at its fiftieth use never meets the introduction site."),
    ("Conventions",
     "a single tree-wide pass would take every one of those decisions silently and at once."),
    ("Conventions",
     "already forbids citing code by line number in the first place."),
    ("Conventions",
     "and from probes, not from apparatus repair."),
    ("Conventions",
     "buys no protection and spends the time the fix plan is owed."),
    ("Conventions",
     "ratifications were re-presented and re-confirmed."),
    ("Conventions",
     "erroring loudly rather than returning silently-wrong content."),
    ("Conventions",
     "and it operationalizes principle #5 (investigate when facts may be scarce)."),
    ("Conventions",
     "the fifty-ninth performed it and counted one."),
)

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

# The bound this artifact declared before the authored ends replaced the paragraph unit. It is
# preserved verbatim rather than quietly overwritten (#12): it was FALSE of the value then
# published, and the record of when this measurement stopped bounding what it said it bounded
# belongs to the correction.
FORMER_BOUND_WORDING_PRESERVED = (
    "THE MARKER SET'S REACH IS UNMEASURED. A defense written without one of these markers is NOT "
    "COUNTED, so every total below is a LOWER BOUND on the defense material standing in the six "
    "session-start spans -- never an estimate of it, and never a ceiling.")


class Stop(Exception):
    """A demand of the measurement is unmet. Never a warning, never a reported field."""


def compile_anchor(anchor: str) -> re.Pattern:
    """An anchor as a whitespace-flexible pattern: escaped words joined by `\\s+`.

    Three of the authored anchors wrap across a line break, so a plain search for them finds
    nothing, and several carry regular-expression metacharacters. Both are why this exists; see the
    module docstring.
    """
    return re.compile(r"\s+".join(re.escape(word) for word in anchor.split()))


def line_offsets(lines: list[str]) -> list[int]:
    """The absolute character offset at which each line begins, in the file as a reader reads it."""
    out, n = [], 0
    for line in lines:
        out.append(n)
        n += len(line) + 1          # the newline that `"\n".join` puts back
    return out


def line_holding(offset: list[int], position: int) -> int:
    """The 1-based line whose text the character before `position` stands on."""
    return next(i for i in range(len(offset) - 1, -1, -1) if offset[i] < position) + 1


def clauses_in(span: dict, lines: list[str], offset: list[int]) -> list[dict]:
    """Every marked defense clause standing inside one span, with its paragraph extent.

    The extent set here is the PARAGRAPH one. It is no longer the measurement -- the authored end
    replaces it -- and it is kept because both earlier readings are published beside the authored
    one (#12) and because the two STOPs on an anchor's placement are stated against it.
    """
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

    ★ THIS IS THE READING THE 2026-09-08 RULING SETTLED, AND IT IS NO LONGER THE MEASUREMENT.  Its
    whole content is: a clause reaches the end of its paragraph OR the next marked clause, whichever
    comes first (`cowork_rulings_2026_09_08_extent_rule_sitting.md`, §1).  It is implemented in ONE
    place (#6) and is now run over a COPY of the extents, so that its result is published as a
    comparison column while the authored end is what is measured.  It is kept rather than deleted
    because nothing that was published is lost (#12).
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
        clause["last_line"] = line_holding(offset, end)
        clause["characters"] = end - clause["_begins"]
        clause["it_was_closed_at_the_next_marked_clause"] = clause["_closed_at_the_next_clause"]
        clause["characters_had_it_run_to_the_paragraph_end"] = \
            clause["_paragraph_ends"] - clause["_begins"]
    return closed


def apply_the_authored_ends(clauses: list[dict], claude_md: str, spans: list[dict],
                            lines: list[str], offset: list[int]) -> None:
    """Set each clause's measured end at its AUTHORED END ANCHOR, with every anchor STOP in force.

    The clauses arrive in file order. Anchor `i` belongs to clause `i`, which is why a mismatch
    between the two counts is a STOP rather than a silent re-pairing.
    """
    if len(clauses) != len(END_ANCHORS):
        raise Stop("the authored end-anchor table carries %d anchor(s) and this run found %d marked "
                   "clause(s). A marker added to or removed from `CLAUDE.md` invalidates an "
                   "authored table, and the table is re-authored by the writing side, never "
                   "patched here" % (len(END_ANCHORS), len(clauses)))

    by_name = {s["name"]: s for s in spans}
    previous_begins = -1
    for index, (clause, (span_named, anchor)) in enumerate(zip(clauses, END_ANCHORS)):
        if clause["the_span_it_stands_in"] != span_named:
            raise Stop("the anchor %r is authored against the span %r and the clause it belongs to "
                       "stands in %r" % (anchor, span_named, clause["the_span_it_stands_in"]))
        span = by_name[span_named]
        span_lo = offset[span["lo"]]
        span_hi = offset[span["hi"] - 1] + len(lines[span["hi"] - 1])
        hits = list(compile_anchor(anchor).finditer(claude_md[span_lo:span_hi]))
        if len(hits) != 1:
            raise Stop("the anchor %r is locatable %d time(s) inside the span %r and it must be "
                       "exactly once" % (anchor, len(hits), span_named))
        begins, ends = span_lo + hits[0].start(), span_lo + hits[0].end()

        if begins < clause["_begins"]:
            raise Stop("the anchor %r begins before the marker of the clause it ends" % anchor)
        if ends > clause["_paragraph_ends"]:
            raise Stop("the anchor %r ends past the paragraph end of the clause it ends" % anchor)
        if index + 1 < len(clauses) and ends >= clauses[index + 1]["_begins"]:
            raise Stop("the anchor %r ends at or after the next marked clause's marker" % anchor)
        if begins <= previous_begins:
            raise Stop("the anchor %r does not stand strictly after the anchor before it -- the "
                       "authored table is out of file order" % anchor)
        previous_begins = begins

        clause["_ends"] = ends
        clause["_last_line"] = line_holding(offset, ends)
        clause["the_authored_end_anchor"] = anchor
        clause["the_line_the_anchor_ends_on"] = clause["_last_line"]
        clause["characters"] = ends - clause["_begins"]
        if clause["characters"] <= 0:
            raise Stop("the anchor %r leaves its clause holding nothing" % anchor)


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

    # (1) Every clause, per span, with its paragraph extent.
    found_per_span = [(span, clauses_in(span, lines, offset)) for span in spans]

    # (2) The two comparison columns. The ruled closing rule runs over a COPY, so that it produces
    #     a column and not the measurement, and so that the ONE implementation of it stays the one
    #     the ruling settled (#6, #12).
    closed_total = 0
    for _span, mine in found_per_span:
        twins = [dict(c) for c in mine]
        closed_total += close_at_the_next_clause(twins, lines, offset)
        for clause, twin in zip(mine, twins):
            clause["characters_had_it_been_closed_at_the_next_marked_clause"] = twin["characters"]
            clause["it_would_have_been_closed_at_the_next_marked_clause"] = \
                twin["it_was_closed_at_the_next_marked_clause"]
            clause["characters_had_it_run_to_its_paragraph_end"] = \
                clause["_paragraph_ends"] - clause["_begins"]

    # (3) The measurement: the authored end, with every anchor STOP in force.
    clauses = [c for _span, mine in found_per_span for c in mine]
    clauses.sort(key=lambda c: c["_begins"])
    apply_the_authored_ends(clauses, claude_md, spans, lines, offset)

    per_span = []
    for span, mine in found_per_span:
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
                           "inside it" % (span["name"], c["first_line"], c["_last_line"]))
        per_span.append({
            "name": span["name"],
            "characters": span["characters"],
            "marked_clauses": len(mine),
            "characters_those_clauses_hold": held,
            "characters_had_every_clause_been_closed_at_the_next_marked_clause":
                sum(c["characters_had_it_been_closed_at_the_next_marked_clause"] for c in mine),
            "characters_had_every_clause_run_to_its_paragraph_end":
                sum(c["characters_had_it_run_to_its_paragraph_end"] for c in mine),
            "share_of_this_span": round(100.0 * held / span["characters"], 2)
            if span["characters"] else 0.0,
        })

    for earlier, later in zip(clauses, clauses[1:]):
        if later["_begins"] < earlier["_ends"]:
            raise Stop("two marked clauses overlap -- lines %d-%d and %d-%d. Overlapping extents "
                       "double-count, and a total that double-counts is worse than no total"
                       % (earlier["first_line"], earlier["_last_line"],
                          later["first_line"], later["_last_line"]))

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
    ruled_total = sum(c["characters_had_it_been_closed_at_the_next_marked_clause"] for c in clauses)
    literal_total = sum(c["characters_had_it_run_to_its_paragraph_end"] for c in clauses)
    shortened = sum(1 for c in clauses
                    if c["characters"] < c["characters_had_it_been_closed_at_the_next_marked_clause"])
    unchanged = len(clauses) - shortened
    return {
        "what_this_is":
            "HOW MUCH OF THE SESSION-START READ OF `CLAUDE.md` IS EXPLICITLY-MARKED DEFENSE, in "
            "characters, measured at the tree. A MEASUREMENT ONLY: it moves no text, proposes "
            "nothing and grades nothing. Every value is computed; none is transcribed (D-431).",
        "generated_by": "tools/audit/gen_defense_share.py",
        "generated_for":
            "cc_instruction_defense_share_authored_ends_2026_09_08.md, Task 1 -- the authored-end "
            "repair of the measurement definition. The tool itself was created for "
            "cc_instruction_defense_share_sizing_third_2026_09_08.md, Task 2, and that dispatch is "
            "re-bannered rather than rewritten (D-674).",
        "★_THE_PUBLISHED_VALUE_IS_A_LOWER_BOUND_ON_MARKED_DEFENSE_AND_THIS_IS_ITS_DECLARED_BOUND": {
            "the_bound": "THE MARKER SET'S REACH IS UNMEASURED. A defense written without one of "
                         "these three markers is NOT COUNTED, so every total below is a LOWER "
                         "BOUND on the defense material standing in the six session-start spans -- "
                         "never an estimate of it, and never a ceiling.",
            "why_it_is_stated_rather_than_left_implicit":
                "D-673: an enumerating pattern whose reach is unmeasured may state its bound on "
                "its own artifact. The test that clause fixes is met here -- no analysis decision "
                "consumes this enumeration; it sizes a documentation question.",
            "★_AND_IT_WAS_NOT_A_BOUND_IN_EITHER_DIRECTION_BEFORE_THIS_ACT": {
                "what_was_wrong": "until the authored ends replaced the paragraph unit, a marked "
                                  "clause was bounded at the end of the paragraph containing it, "
                                  "through a function that walks forward only until a BLANK LINE. "
                                  "`CLAUDE.md`'s guiding principles are one numbered list with no "
                                  "blank line between items, and its sections for the open-items "
                                  "register and for the decisions register are single unbroken "
                                  "blocks, so an extent ran from its marker to the next marker and "
                                  "CARRIED LIVE RULE TEXT. The value was therefore "
                                  "not a lower bound on defense material: it counted text that is "
                                  "not defense while still missing every unmarked defense, so it "
                                  "was wrong in both directions at once.",
                "the_former_wording_preserved_verbatim_rather_than_quietly_replaced_12":
                    FORMER_BOUND_WORDING_PRESERVED,
                "why_it_is_preserved": "#12. The former wording was published and consumed, and "
                                       "the record of when this measurement stopped bounding what "
                                       "it said it bounded belongs to the correction.",
                "where_the_defect_was_found": "the harvest's first step, opening the measured "
                                              "clauses at the file -- recorded in the "
                                              "hundred-and-fiftieth handoff entry and enumerated "
                                              "marker by marker in "
                                              "`cowork_defense_clause_ends_2026_09_08.md`.",
            },
            "★_THE_ENDS_ARE_AUTHORED": {
                "what_that_means": "each clause's end is a judgment about where its defense stops, "
                                   "read at the file marker by marker -- not a mechanical "
                                   "boundary. What is DERIVED is every character count over those "
                                   "ends, and every placement check on them.",
                "where_the_judgment_is_published_whole_with_its_reason_per_marker":
                    "cowork_defense_clause_ends_2026_09_08.md",
                "how_it_is_challenged": "at the anchor. Every anchor is published per clause below "
                                        "and at that pass, with the words it ends on, so a "
                                        "disagreement names one anchor rather than the total.",
                "the_two_bounds_that_pass_declares_on_itself":
                    "that every end is an authored judgment challengeable at its marker; and that "
                    "its reading (ii) -- a caveat bounding how a rule or a value is READ is "
                    "operative text and not defense -- is STATED AND NOT RULED, several ends moving "
                    "outward if it is ruled otherwise.",
            },
            "★_THE_LIVE_RULE_CLASSIFICATION_IS_STILL_NOT_CONSUMED":
                "`cowork_claude_md_live_rule_classification_2026_09_08.md` is NOT read by this "
                "tool, before this act or after it. The authored ends come from the pass named "
                "above and from nowhere else.",
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
            "from the first character of the marker through the end of that clause's AUTHORED END "
            "ANCHOR -- one anchor per marked clause, in file order, each the last words of that "
            "clause's defense. An anchor is compiled by splitting on whitespace, escaping each "
            "word and joining the words with a whitespace pattern, because three of them wrap "
            "across a line break and several carry regular-expression metacharacters. Every "
            "placement check on an anchor is a STOP and none is a reported field.",
        "★_THE_TWO_EARLIER_READINGS_ARE_KEPT_AND_PUBLISHED_BESIDE_THE_AUTHORED_ONE": {
            "why_they_are_kept": "#12. Both were published, and each answers a question the "
                                 "authored measurement does not: what the ruled closing rule "
                                 "attributes, and what the literal paragraph wording attributes.",
            "the_ruled_closing_reading": {
                "what_it_is": "a marked clause reaches its paragraph's end OR the next marked "
                              "clause, whichever comes first.",
                "its_standing": "RULED the definition on 2026-09-08 and no longer outstanding -- "
                                "`cowork_rulings_2026_09_08_extent_rule_sitting.md`, §1. It is "
                                "REPLACED here as the MEASUREMENT because it inherits the "
                                "paragraph unit, which is the defect; the ruling settled a "
                                "double-counting question between two readings and does not reach "
                                "the unit both of them are built on.",
                "it_is_still_implemented_in_one_place":
                    "`close_at_the_next_clause` below, unchanged and now run over a COPY of the "
                    "extents so that it produces this column and not the measurement (#6).",
                "characters_it_attributes_to_the_six_spans": ruled_total,
                "clauses_it_would_have_closed_at_the_next_one": closed_total,
            },
            "the_literal_paragraph_reading": {
                "what_it_is": "from the first character of the marker through the end of the "
                              "paragraph containing it, with no closing at all -- the wording of "
                              "the dispatch that created this tool.",
                "why_it_cannot_be_a_share_of_anything":
                    "it attributes more characters to the six spans than those six spans hold.",
                "characters_it_attributes_to_the_six_spans": literal_total,
            },
            "what_the_authored_ends_move": {
                "clauses_whose_measured_end_now_falls_short_of_the_ruled_closing_end": shortened,
                "clauses_whose_measured_end_is_unchanged_by_the_authored_table": unchanged,
                "how_to_read_this": "the movement is DOWNWARD by construction and that is the "
                                    "point of the act rather than a regression: the earlier value "
                                    "measured the wrong thing. Every clause carries all three "
                                    "lengths below, so the movement is inspectable per clause "
                                    "rather than asserted as a total.",
            },
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
            "characters_had_every_clause_been_closed_at_the_next_marked_clause": ruled_total,
            "characters_had_every_clause_run_to_its_paragraph_end": literal_total,
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
            "the_anchor_count_equals_the_marked_clause_count": True,
            "every_anchor_is_locatable_exactly_once_inside_its_own_clause_s_span": True,
            "every_anchor_stands_in_the_span_the_authored_table_names_for_it": True,
            "every_anchor_begins_at_or_after_its_own_marker": True,
            "every_anchor_ends_at_or_before_its_own_paragraph_end": True,
            "every_anchor_ends_strictly_before_the_next_marker": True,
            "the_anchors_stand_in_strictly_increasing_file_order": True,
            "every_clause_lies_wholly_inside_the_span_it_is_attributed_to": True,
            "no_two_clauses_overlap": True,
            "no_clause_is_left_holding_nothing": True,
            "no_span_s_clause_characters_exceed_that_span_s_own_count": True,
            "the_six_spans_re_derived_total_equals_the_reader_s_own": True,
            "the_known_unemphasised_miss_is_locatable_exactly_once": True,
            "what_it_does_NOT_establish":
                "that the marker table is COMPLETE, and that any authored end is the RIGHT one. "
                "Every check above is about the measurement's internal soundness and about each "
                "anchor's placement; none of them can see a defense the table does not admit, and "
                "none of them can judge where a defense ought to stop. That is why the bound above "
                "is declared and why every anchor is published for challenge.",
        },
        "what_this_does_not_claim": [
            "That any marked clause is MOVABLE. Movability is Ruling 1's question and nothing "
            "here answers any portion of it.",
            "That any unmarked passage is not a defense -- the declared bound says the opposite.",
            "That the value is what a satellite would remove.",
            "That an authored end is anything but an authored judgment -- see the declared bound "
            "above, which states where that judgment is published and how it is challenged.",
            "That `cowork_claude_md_live_rule_classification_2026_09_08.md` was consumed -- see "
            "the declared bound above, which states it at the place the ends are bounded.",
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
    print("  TOTAL %d character(s) in %d clause(s), at the AUTHORED ends"
          % (tot["characters_those_clauses_hold"], tot["marked_clauses"]))
    print("    the ruled closing reading would attribute %d; the literal paragraph reading %d"
          % (tot["characters_had_every_clause_been_closed_at_the_next_marked_clause"],
             tot["characters_had_every_clause_run_to_its_paragraph_end"]))
    print("    of the six session-start spans (%d): %.2f%%"
          % (den["the_six_session_start_spans"], tot["share_of_the_six_session_start_spans"]))
    print("    of the whole session-start read (%d): %.2f%%"
          % (den["the_whole_ordinary_session_start_read"],
             tot["share_of_the_whole_ordinary_session_start_read"]))
    print("  THE VALUE IS A LOWER BOUND ON MARKED DEFENSE: the marker set's reach is UNMEASURED,")
    print("  and the ends are AUTHORED (cowork_defense_clause_ends_2026_09_08.md).")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except Stop as exc:
        print("STOP: %s" % exc)
        sys.exit(2)
