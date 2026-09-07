#!/usr/bin/env python3
"""WHAT AN ORDINARY SESSION READS AT SESSION START, MEASURED — and what the last change to it cost.

WHY THIS EXISTS.  The pruning arc's whole subject is the size of the mandatory session-start read
(the user's direction of 2026-08-16: *"the mandatory reads at session start for you and CC are too
large"*).  Every act in that arc has had to state what it saved, and every one of those values has
so far been measured by hand at git objects and typed into a record.  A figure enters a report by
citation to a generated artifact and never by transcription (`CLAUDE.md` #17f, register entry
D-431), so the measurement is generated here.  Built by `cc_instruction_preparation_tenth.md`
Task 2, whose step 6 orders the effect published with each value read from the files at explicit
objects and not estimated.

WHAT IS AUTHORED AND WHAT IS DERIVED
------------------------------------
authored : the MEMBERSHIP of the ordinary session-start read — the whole documents a session must
           read — each with the clause in `CLAUDE.md` that makes it one.  Three of them, and the
           table is small because the read is.  A CONDITIONAL read (`BUILD_AND_TEST.md`,
           `docs/scoring_model.md`, the joint estimator's section) is NOT a member: it is read by
           the sessions its condition names and not by an ordinary one, which is what CONDITIONAL
           means.
derived  : the FOURTH member — the artifact and key rule (a) names — parsed from rule (a)'s own
           clause rather than listed here, so a later narrowing of that pointer moves this
           measurement without anybody editing this tool; **what an ordinary session reads OF
           `CLAUDE.md`, parsed from that file's own membership block on the same idiom**; every
           member's character count; the total; and the same total at each recorded earlier commit,
           read from the git OBJECT at an explicit hash.

★ WHAT `CLAUDE.md` CONTRIBUTES TO THE READ, AND WHY THAT STOPPED BEING THE WHOLE FILE (2026-09-07).
On 2026-09-07 the user ruled what a session reads OF `CLAUDE.md` itself: SIX spans at session start,
EIGHT read only when the session's work touches them.  Until that ruling this tool measured
`len(CLAUDE.md)` — the whole file — as an ordinary session's read, which after the ruling counts
eight CONDITIONAL spans into a read no ordinary session takes.  That is the same error the
conditional-read statement above already refuses for `BUILD_AND_TEST.md`, and `--check` could not
see it: `--check` re-derives the artifact and compares rendered text, so a fault in the DEFINITION
of what is measured re-derives identically and the check passes while the measurement overstates
(#19).  **The measured contribution is now the sum of the SIX session-start spans**, and the eight conditional
spans are measured BESIDE it and never summed in — the treatment `FURTHER_SPANS` already has, for
the reason stated there.

HOW A SPAN OF `CLAUDE.md` IS COUNTED, and how each is located.  Every span is named by its HEADING
and never by a line number (D-307), so a heading is located by its own text and must be found
EXACTLY ONCE in heading form.  A span runs from its heading through the line before the next heading
at the same or a higher level, with trailing blank lines dropped, and its size is the characters of
those lines joined by newlines — what a reader actually reads.  Two spans are not headings and are
located by the anchors the membership block itself quotes: the session-start read block, which has
no heading of its own, and the close of the *Guiding principles* span, which the membership states
as the paragraph that closes it.  **Neither the names nor the anchors are carried in this file** —
all of them are parsed out of the block, so an amendment to the membership moves this measurement
without anybody editing this tool.

★ THE TWO REGIMES, STATED RATHER THAN INFERRED.  `build()` also measures at earlier commits, whose
`CLAUDE.md` may carry no membership block at all — before 2026-09-07 the whole-file read was
PRACTICE and was mandated by no clause, as that file's own provenance sentence records.  So:

  * block ABSENT  → the reading is the whole file, recorded as `regime: "whole-file practice"`;
  * block PRESENT → the reading is the six spans, recorded as `regime: "ruled membership"`;
  * block PRESENT but a named span unresolvable → a STOP.  The fallback exists for the ABSENCE of
    the block and for nothing else.

Every movement row therefore NAMES THE REGIME ON BOTH SIDES of its comparison, because a comparison
across a regime boundary compares two different questions.

HOW A KEY'S SIZE IS COUNTED, stated because a convention nobody states is a convention nobody can
check.  The artifact is written with one-space indentation, so a key's span runs from the line that
opens it to the line that opens the next key at the SAME indentation.  The size is the number of
characters of that span — what a reader actually reads, not a re-serialisation.

★ AND TWO FURTHER SPANS OF THE SAME ARTIFACT ARE MEASURED BESIDE THE READ AND NEVER SUMMED INTO IT
(2026-08-18).  They are the two published figures Ruling 3 of
`cowork_rulings_2026_08_18_tenth_return.md` ordered corrected that this tool did not derive: the 216
gating rows' recorded grounds, and the comparison with the frozen record.  The extension is TWO KEY
CHAINS over the function this file already carries — it is DECLARED AS A JUDGMENT at `FURTHER_SPANS`
below, in the commit that made it, and in that batch's close, because the standing mechanism freeze
bars tool work that does not block the work and this work blocked a ruled act.

THE STOPS
  * rule (a)'s clause naming a path the tree does not have, or a key chain the artifact does not
    carry, is a STOP: the pointer a session is told to read must resolve, and a pointer that has
    stopped resolving is exactly the failure this measurement would otherwise hide;
  * a FURTHER SPAN's key chain that the same artifact does not carry is a STOP for the same reason —
    a silent zero is what a measurement may never publish;
  * an authored member the tree does not have is a STOP;
  * an earlier reading whose commit cannot be read is a STOP rather than a silently dropped row —
    a comparison that quietly loses its baseline reports a saving nobody can check;
  * the membership block's opening text occurring MORE THAN ONCE is a STOP — the block a session is
    told to read must be identifiable, and two of them is not a narrowing but an ambiguity;
  * a span the membership NAMES that does not resolve — a heading absent or found twice, an anchor
    absent or found twice, a closing paragraph the span does not contain — is a STOP, on the same
    clause that stops this tool when rule (a)'s pointer stops resolving.  A named span silently
    measured as zero is the failure this whole tool exists against;
  * the block's own DECLARED count of its spans disagreeing with the number parsed is a STOP: the
    block says how many it carries, so a parse that finds a different number has mis-read it;
  * THE FALSIFICATION TEST, RUN ON EVERY RUN — the six session-start spans costing at least as much
    as the whole file is a STOP.  A membership that costs the whole file has not been derived, it
    has been mis-parsed, and a mis-parse that happens to sum plausibly is exactly what a measurement
    may not publish.

WHAT THIS DOES NOT ASSERT.  That the membership is complete: it is AUTHORED, and a mandatory read
added to `CLAUDE.md` without being added here would not appear.  That is why each member carries
the clause it comes from, so the authored half is checkable by reading four clauses rather than a
file.  And it asserts nothing about whether the read is small enough — that is [[OI-370]]'s own
subject.

Run:
    python tools/audit/gen_session_start_read_size.py
    python tools/audit/gen_session_start_read_size.py --check
"""
from __future__ import annotations

import io
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(HERE, "session_start_read_size.json")

sys.path.insert(0, HERE)
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

# ── AUTHORED — the whole documents an ordinary session reads, with the clause that makes each one
# a member.  Every citation below was READ IN THIS SESSION, in `CLAUDE.md`, with the file tools.
#
# ★ `CLAUDE.md`'s ROW CARRIES A MARKER AND NOT A SENTENCE (2026-09-07).  Until this date it read
# "the project instructions themselves, which every clause below is written in" — which cited no
# clause at all, where the other two rows each quote a real one, and which was written when no
# clause existed to cite.  Since 2026-09-07 one does, and it is DERIVED rather than retyped here:
# `claude_md_reading()` quotes it out of the membership block itself, on the same idiom as
# `rule_a_pointer()` and for the same stated reason — a later amendment of that block moves this
# measurement without anybody editing this tool, and a sentence retyped here would be one more
# transcription site in a file that already carries one (OI-377, D-431).
DERIVED_CLAUSE = ("★ DERIVED, not authored — the clause is quoted out of `CLAUDE.md`'s own "
                  "membership block; see `the_reading_of_claude_md`")

MEMBERS: tuple[tuple[str, str], ...] = (
    ("CLAUDE.md", DERIVED_CLAUSE),
    ("STATUS.md",
     "`CLAUDE.md`, the build-and-test section's opening list: \"Always read these two files at the "
     "start of every session\""),
    ("DECISIONS.md",
     "the same list, and the decisions register's own rule (a) — \"read the INDEX `DECISIONS.md` "
     "at session start\" — explicitly NOT demoted to a conditional read on 2026-08-17"),
)

# The earlier readings this measurement compares against. Each is read at its git OBJECT by
# explicit hash; no value is carried in this file.
BASELINES: tuple[tuple[str, str], ...] = (
    # WHY THE COMPARISON STARTS HERE AND NOT EARLIER, stated because a bounded comparison that does
    # not say where its bound is reads as the whole story. Before the ninth batch the read regime
    # named a DIFFERENT MEMBER SET — `OPEN_ITEMS.md` whole, `BUILD_AND_TEST.md` unconditionally —
    # and rule (a) named no artifact-and-key pointer at all, so this measurement's shape does not
    # reach it and forcing it would compare two different questions. The cross-regime figures for
    # that arc are recorded in the ruling records that took them and are not re-derived here (#6).
    ("1760d9a4a87f82a6bdbc7cb17e99ccdd8ae4c433",
     "the preparation phase's NINTH batch terminus — the TENTH batch's own base, and the state "
     "rule (a)'s pointer was narrowed from"),
    # ★ THE NARROWING ACT'S OWN READING, KEPT LIVE RATHER THAN LEFT TO BE RECOVERED (#12). The
    # reading AT THE TREE moves with every later batch that touches a member, so the act's own
    # effect would otherwise survive only in this artifact's blob at the commit that took it. It is
    # carried here as a baseline instead, read at the git object like every other, so a reader sees
    # the narrowing's effect and the record's later growth as two separate movements.
    ("594074e1e1900079e449d2b79a38920d21bca6e6",
     "the commit that narrowed rule (a)'s pointer — `cc_instruction_preparation_tenth.md` Task 2, "
     "the act this measurement was built to publish"),
)

# ── AUTHORED — two FURTHER SPANS of the SAME artifact rule (a) points at, measured beside the read
# but NEVER counted into it.
#
# ★ WHY THEY ARE HERE, DECLARED AS A JUDGMENT AND NOT SLIPPED IN (2026-08-18, on the user's Ruling 4
# of `cowork_rulings_2026_08_18_eleventh_stop.md`; executed by
# `cc_instruction_preparation_eleventh_amended.md` Task 4).  Ruling 3 of
# `cowork_rulings_2026_08_18_tenth_return.md` orders FIVE published figures corrected by citation to
# this artifact, and this tool derived three of them.  The two it did not are named key spans of the
# very artifact it already reads, and this file already carries `key_span_characters`, a function
# general over a key chain that `measure` already calls twice with different chains.  **The extension
# is therefore TWO KEY CHAINS and not a new capability** — which is what the standing mechanism
# freeze turns on, the freeze barring tool work *that does not block the work*: without them the
# ruled correction cannot be made at all, because D-431 forbids a transcribed value.  The same
# admission the tenth batch declared at its own §9, where a whole new measurement tool was built for
# exactly this reason.
#
# ★ WHAT THEY ARE NOT.  They are NOT members of the session-start read and are NOT summed into
# `total_characters`: a session reads the ANSWER at boot and opens these to challenge a verdict,
# which is the whole point of the narrowing rule (a) records.  Counting them would report a read no
# ordinary session takes, which is the same error the conditional-read note above refuses.
#
# ★ AND THEY ARE ROOTED AT WHATEVER ARTIFACT RULE (a) NAMES, so a later narrowing that moved the
# pointer to a different file would make these chains fail to resolve — and that is a STOP, by the
# same clause that stops this tool when rule (a)'s own pointer stops resolving.  A silent zero is
# what a measurement may never publish.
FURTHER_SPANS: tuple[tuple[tuple[str, ...], str], ...] = (
    (("★_the_live_gating_answer", "the_gating_rows"),
     "the 216 gating rows, each carrying its recorded ground — the GROUNDS a session opens when it "
     "challenges a verdict, and the third of the five figures Ruling 3 orders corrected"),
    (("★_the_live_gating_answer", "★_the_frozen_enumeration_measured_against_this_one"),
     "the comparison with the frozen record — retrospective evidence for the phase's "
     "retrospective, and the fifth of the five figures Ruling 3 orders corrected"),
)

RULE_A = re.compile(r"Rules:\s*\(a\)(.*?);\s*\(b\)", re.S)
POINTER = re.compile(r"`([A-Za-z0-9_./-]+\.json)`((?:\s*→\s*`[^`]+`)+)")
KEY = re.compile(r"`([^`]+)`")

# ── the membership block of `CLAUDE.md`, located and parsed rather than listed ────────────────
# The opening text of the block, the two list headers, and the markup the block writes its names
# and anchors in. Nothing here is a span name, a heading or an anchor: those are all parsed.
MEMBERSHIP_ANCHOR = "★ AND THIS IS WHAT A SESSION READS OF"
SESSION_START_HEADER = "**READ AT SESSION START"
CONDITIONAL_HEADER = "**READ CONDITIONALLY"

BOLD = re.compile(r"\*\*(.+?)\*\*", re.S)
QUOTED_ANCHOR = re.compile(r'\*"([^"]+)"\*')
ITALIC = re.compile(r'(?<!\*)\*([^*"][^*]*?)\*(?!\*)')
HEADING = re.compile(r"^(#{2,6})\s+(\S.*)$")

# A written-out number is a WORD, not a transcribed value: the block states how many spans it
# carries, and that statement is used as a CHECK on the parse, never as a value to publish (D-431).
NUMBER_WORDS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
                "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
                "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18,
                "nineteen": 19, "twenty": 20}


class Stop(Exception):
    """A demand of the measurement is unmet. Never a warning."""


def git_show(rev: str, path: str) -> str:
    proc = subprocess.run(["git", "-C", ROOT, "show", f"{rev}:{path}"],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        raise Stop(f"could not read {path} at the git object {rev[:10]} — "
                   f"{proc.stderr.decode('utf-8', 'replace').strip()}")
    return proc.stdout.decode("utf-8")


def at_tree(path: str) -> str:
    full = os.path.join(ROOT, path)
    if not os.path.exists(full):
        raise Stop(f"an authored member is not in the tree: {path}")
    with io.open(full, encoding="utf-8") as fh:
        return fh.read()


def rule_a_pointer(claude_md: str) -> dict:
    """The artifact and key chain rule (a) tells a session to read, parsed from the clause itself.

    The FIRST chain rooted at a `.json` path is the read pointer. A later chain in the same clause
    — the grounds a session opens to challenge a verdict — is not what rule (a) sends it to at
    boot, and is reported separately rather than folded in.
    """
    m = RULE_A.search(claude_md)
    if not m:
        raise Stop("rule (a)'s clause could not be located in `CLAUDE.md`")
    clause = m.group(1)
    p = POINTER.search(clause)
    if not p:
        raise Stop("rule (a)'s clause names no artifact-and-key pointer")
    return {"artifact": p.group(1), "keys": KEY.findall(p.group(2)), "clause_characters": len(clause)}


def key_span_characters(text: str, keys: list[str]) -> int:
    """The characters of a key's span: its opening line to the next key at the same indentation."""
    lines = text.split("\n")
    lo, hi, indent = 0, len(lines), 0
    for depth, key in enumerate(keys, start=1):
        indent = depth
        opener = " " * indent + json.dumps(key, ensure_ascii=False) + ":"
        start = None
        for i in range(lo, hi):
            if lines[i].startswith(opener):
                start = i
                break
        if start is None:
            raise Stop(f"the key chain rule (a) names does not resolve: {keys!r} "
                       f"(stopped at {key!r})")
        end = hi
        for i in range(start + 1, hi):
            stripped = lines[i]
            if stripped.startswith(" " * indent + '"') and not stripped.startswith(" " * (indent + 1)):
                end = i
                break
        lo, hi = start, end
    return len("\n".join(lines[lo:hi]))


def span_characters(lines: list[str], lo: int, hi: int) -> int:
    """The characters of a span of `CLAUDE.md`: its lines joined by newlines, as a reader reads."""
    return len("\n".join(lines[lo:hi]))


def _declared_count(line: str, what: str) -> int:
    """The number the block itself says a list carries — a CHECK on the parse, never a published
    value. A header naming no number this map knows is a STOP: an unchecked parse is not a parse."""
    for word in re.findall(r"[A-Za-z]+", line.lower()):
        if word in NUMBER_WORDS:
            return NUMBER_WORDS[word]
    raise Stop("the membership block's %s header states no number this tool can read: %r"
               % (what, line.strip()))


def _bullet_list(lines: list[str], start: int, header: str, what: str) -> tuple[list[str], int]:
    """The bullets of the list opened by `header` after line `start`, each joined over its wraps."""
    head = None
    for i in range(start, len(lines)):
        if lines[i].lstrip().startswith(header):
            head = i
            break
    if head is None:
        raise Stop("the membership block carries no %s list (%r)" % (what, header))
    bullets: list[str] = []
    for i in range(head + 1, len(lines)):
        line = lines[i]
        if line.strip() == "":
            if bullets:
                break
            continue
        if line.startswith("- "):
            bullets.append(line[2:].strip())
        elif bullets:
            bullets[-1] += " " + line.strip()
        else:
            break
    if not bullets:
        raise Stop("the membership block's %s list carries no entries" % what)
    return bullets, _declared_count(lines[head], what)


def _table_rows(lines: list[str], start: int, header: str,
                what: str) -> tuple[list[tuple[str, str]], int, int]:
    """The rows of the table opened by `header`, as (first cell, second cell) pairs, with the line
    after the last table line — which is where the membership block ends."""
    head = None
    for i in range(start, len(lines)):
        if lines[i].lstrip().startswith(header):
            head = i
            break
    if head is None:
        raise Stop("the membership block carries no %s table (%r)" % (what, header))
    rows: list[tuple[str, str]] = []
    seen_table, end = False, len(lines)
    for i in range(head + 1, len(lines)):
        line = lines[i].strip()
        if not line.startswith("|"):
            if seen_table:
                end = i
                break
            continue
        seen_table = True
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 2 or set(cells[0]) <= set("-: "):
            continue                       # the column header and the separator rule
        if "**" not in cells[0]:
            continue
        rows.append((cells[0], cells[1]))
    if not rows:
        raise Stop("the membership block's %s table carries no rows" % what)
    return rows, _declared_count(lines[head], what), end


def _heading_span(lines: list[str], name: str) -> tuple[int, int, str]:
    """The span of the heading whose text opens with `name` — found exactly once, or a STOP."""
    hits = [(i, len(m.group(1))) for i, m in
            ((i, HEADING.match(ln)) for i, ln in enumerate(lines))
            if m and m.group(2).strip().startswith(name)]
    if len(hits) != 1:
        raise Stop("the membership names the span %r, and %d headings of `CLAUDE.md` open with it "
                   "— it must be exactly one" % (name, len(hits)))
    lo, level = hits[0]
    hi = len(lines)
    for j in range(lo + 1, len(lines)):
        m = HEADING.match(lines[j])
        if m and len(m.group(1)) <= level:
            hi = j
            break
    while hi > lo + 1 and lines[hi - 1].strip() == "":
        hi -= 1
    return lo, hi, lines[lo].strip()


def _anchor_line(lines: list[str], text: str, lo: int = 0, hi: int | None = None) -> int:
    """The one line carrying an anchor the membership quotes — found exactly once, or a STOP."""
    probe = text.strip().lstrip("…").strip()
    hits = [i for i in range(lo, len(lines) if hi is None else hi) if probe in lines[i]]
    if len(hits) != 1:
        raise Stop("the membership quotes the anchor %r, and it occurs %d times where it must "
                   "occur exactly once" % (probe, len(hits)))
    return hits[0]


def _paragraph_end(lines: list[str], at: int, hi: int) -> int:
    """The line after the last line of the paragraph containing `at`."""
    end = at + 1
    while end < hi and lines[end].strip() != "":
        end += 1
    return end


def _resolve_span(lines: list[str], outside: list[str], text: str, kind: str) -> dict:
    """One named span of `CLAUDE.md`, resolved by its heading or by the anchors the block quotes.

    The membership writes a span's NAME in bold.  Where it also quotes anchors, the span is located
    by them — that is how it names the two spans that are not headings.  Where it names a closing
    paragraph in italics instead, the span is its heading's, closed at that paragraph.

    ★ AN ANCHOR IS SOUGHT OUTSIDE THE MEMBERSHIP BLOCK, and `outside` is the file with the block's
    own lines blanked.  The block QUOTES the anchors it names spans by, so a whole-file search finds
    each of them twice — once as the naming and once as the named — and would stop on an ambiguity
    the record does not have.  The naming is not the thing named.
    """
    bold = BOLD.search(text)
    if not bold:
        raise Stop("a membership entry carries no span name in bold: %r" % text)
    name = bold.group(1).strip()
    quotes = QUOTED_ANCHOR.findall(text)

    if quotes:
        if len(quotes) != 2:
            raise Stop("the membership locates %r by %d quoted anchors; it takes exactly two, an "
                       "opening and a close" % (name, len(quotes)))
        lo = _anchor_line(outside, quotes[0])
        close = _anchor_line(outside, quotes[1])
        if close < lo:
            raise Stop("the membership's close for %r stands before its opening" % name)
        if close + 1 < len(lines) and lines[close + 1].strip() != "":
            raise Stop("the membership closes %r at a paragraph ending %r, and that text does not "
                       "end its paragraph" % (name, quotes[1].strip()))
        return {"name": name, "kind": kind, "lo": lo, "hi": close + 1,
                "located_by": "the two anchors the membership itself quotes — from “%s” "
                              "through the paragraph ending “%s”"
                              % (quotes[0].strip(), quotes[1].strip())}

    lo, hi, heading = _heading_span(lines, name)
    italic = ITALIC.findall(text)
    if italic:
        closer = italic[0].strip()
        at = _anchor_line(outside, "**" + closer, lo, hi)
        end = _paragraph_end(lines, at, hi)
        located = ("the heading “%s”, closed at the paragraph the membership names — the "
                   "one opening “%s”" % (heading, closer))
        return {"name": name, "kind": kind, "lo": lo, "hi": end, "located_by": located,
                "the_close_is_also_the_end_of_its_section": end == hi}
    return {"name": name, "kind": kind, "lo": lo, "hi": hi,
            "located_by": "the heading “%s”" % heading}


def claude_md_reading(claude_md: str) -> dict:
    """What an ordinary session reads OF `CLAUDE.md`, under whichever regime the file itself sets.

    No span name, heading or anchor is carried in this file: every one is parsed out of the
    membership block.  A file carrying no such block is the WHOLE-FILE regime — that was the
    practice before 2026-09-07 and was mandated by no clause, as the file's own provenance sentence
    records — and it is recorded as such rather than measured as a membership.
    """
    lines = claude_md.split("\n")
    hits = [i for i, ln in enumerate(lines) if MEMBERSHIP_ANCHOR in ln]
    if len(hits) > 1:
        raise Stop("the membership block's opening text occurs %d times in `CLAUDE.md`; the block a "
                   "session is told to read must be identifiable, and two of them is an ambiguity"
                   % len(hits))
    if not hits:
        return {
            "regime": "whole-file practice",
            "why_this_regime": "this `CLAUDE.md` carries no membership block, so the whole file was "
                               "the read — the practice the file's own provenance sentence records "
                               "as mandated by no clause until 2026-09-07",
            "the_clause_that_makes_it_a_member": "none — the whole-file read was PRACTICE here, not "
                                                 "a clause",
            "characters": len(claude_md),
        }

    start = hits[0]
    paragraph = " ".join(lines[start:_paragraph_end(lines, start, len(lines))])
    clause = BOLD.search(paragraph)
    if not clause:
        raise Stop("the membership block's opening clause could not be quoted")

    bullets, declared_start = _bullet_list(lines, start, SESSION_START_HEADER, "session-start")
    rows, declared_cond, block_end = _table_rows(lines, start, CONDITIONAL_HEADER, "conditional")
    if len(bullets) != declared_start:
        raise Stop("the membership block declares %d session-start spans and this parse found %d"
                   % (declared_start, len(bullets)))
    if len(rows) != declared_cond:
        raise Stop("the membership block declares %d conditional spans and this parse found %d"
                   % (declared_cond, len(rows)))

    # The block QUOTES the anchors it names spans by, so anchors are sought outside it.
    outside = ["" if start <= i < block_end else ln for i, ln in enumerate(lines)]

    session_start = [_resolve_span(lines, outside, b, "session start") for b in bullets]
    conditional = []
    for cell, condition in rows:
        span = _resolve_span(lines, outside, cell, "conditional")
        span["the_condition_that_calls_for_it"] = condition
        qualifier = BOLD.sub("", cell, count=1).strip(" —-,").strip()
        if qualifier:
            span["the_qualifier_the_membership_writes_beside_the_name"] = qualifier
        conditional.append(span)

    for span in session_start + conditional:
        span["characters"] = span_characters(lines, span["lo"], span["hi"])
        span["lines"] = span["hi"] - span["lo"]

    total = sum(s["characters"] for s in session_start)
    whole = len(claude_md)
    # THE FALSIFICATION TEST, run on every run.
    if total >= whole:
        raise Stop("the six session-start spans measure %d characters against the whole file's %d "
                   "— a membership costing at least the whole file has not been derived, it has "
                   "been mis-parsed" % (total, whole))

    # Every conditional span is measured BESIDE the read; where one overlaps a session-start span
    # the shared characters are published, so an overlap is visible rather than silently counted.
    for span in conditional:
        shared = {}
        for other in session_start:
            lo, hi = max(span["lo"], other["lo"]), min(span["hi"], other["hi"])
            if hi > lo:
                shared[other["name"]] = span_characters(lines, lo, hi)
        if shared:
            span["characters_shared_with_a_session_start_span"] = shared

    named = [BOLD.search(b).group(1).strip() for b in bullets] + \
            [BOLD.search(c).group(1).strip() for c, _ in rows]
    resolved = [s["name"] for s in session_start + conditional]
    in_neither = sorted(set(named) - set(resolved))
    in_both_only = sorted(set(resolved) - set(named))
    if in_neither or in_both_only or len(set(named)) != len(named):
        raise Stop("the reconciliation against the membership block failed — named-but-unresolved "
                   "%r, resolved-but-unnamed %r, %d names for %d spans"
                   % (in_neither, in_both_only, len(set(named)), len(named)))

    return {
        "regime": "ruled membership",
        "why_this_regime": "this `CLAUDE.md` carries the membership block, so the read is the six "
                           "spans it names at session start and nothing else of the file",
        "the_clause_that_makes_it_a_member": clause.group(1).strip(),
        "characters": total,
        "the_session_start_spans": [
            {k: v for k, v in s.items() if k not in ("lo", "hi")} for s in session_start],
        "the_conditional_spans_measured_beside_the_read_and_never_summed_into_it": [
            {k: v for k, v in s.items() if k not in ("lo", "hi")} for s in conditional],
        "why_the_conditional_spans_are_not_summed_in":
            "each is read by the sessions its own condition names and not by an ordinary one, which "
            "is what CONDITIONAL means. Counting them would report a read no ordinary session "
            "takes — the same error this tool already refuses for `BUILD_AND_TEST.md`.",
        "★_the_overstatement_this_repair_removes": {
            "what_it_is": "until 2026-09-07 this tool measured `len(CLAUDE.md)` as an ordinary "
                          "session's read of that file. Both values are measured HERE, at the same "
                          "tree, so the difference is the overstatement itself and not an estimate.",
            "the_former_measurement_the_whole_file": whole,
            "the_repaired_measurement_the_six_session_start_spans": total,
            "characters_the_former_measurement_overstated_by": whole - total,
        },
        "★_the_reconciliation_against_the_block_itself_run_on_every_run": {
            "how_it_runs": "both directions, and a mismatch in either is a STOP rather than a "
                           "reported field: none in both, none in neither.",
            "every_span_resolved_is_one_the_block_names": in_both_only == [],
            "every_span_the_block_names_was_resolved": in_neither == [],
            "no_two_spans_share_a_name": len(set(named)) == len(named),
            "spans_the_block_names": len(named),
            "spans_resolved": len(resolved),
            "what_it_does_not_establish": "that any span's BOUNDS are the ones the membership "
                                          "intends — what is established is that the two "
                                          "populations are the same and that every one resolved.",
        },
    }


def measure(claude_md: str, reader) -> dict:
    """One reading of the whole session-start read, at whatever source `reader` supplies."""
    pointer = rule_a_pointer(claude_md)
    artifact_text = reader(pointer["artifact"])
    answer = key_span_characters(artifact_text, pointer["keys"])
    section = key_span_characters(artifact_text, pointer["keys"][:1])
    reading = claude_md_reading(claude_md)

    per_member = {}
    for path, _why in MEMBERS:
        per_member[path] = reading["characters"] if path == "CLAUDE.md" else len(reader(path))
    per_member[pointer["artifact"] + " → " + " → ".join(pointer["keys"])] = answer

    further = {}
    for chain, what in FURTHER_SPANS:
        label = pointer["artifact"] + " → " + " → ".join(chain)
        further[label] = {
            "characters": key_span_characters(artifact_text, list(chain)),
            "what_it_is": what,
        }

    return {
        "the_pointer_rule_a_names": pointer,
        "the_regime_this_reading_was_taken_under": reading["regime"],
        "the_reading_of_claude_md": reading,
        "characters_per_member": per_member,
        "total_characters": sum(per_member.values()),
        "further_spans_of_the_same_artifact_NOT_counted_into_the_read": further,
        "the_section_that_carries_the_pointer": {
            "key": pointer["keys"][0],
            "characters": section,
            "what_it_is": "the whole section the artifact carries at that key — the answer TOGETHER "
                          "with the grounds that establish it. A session reads the answer at boot "
                          "and opens the rest to challenge a verdict.",
        },
        "characters_the_section_carries_beyond_the_answer": section - answer,
    }


def build() -> dict:
    now = measure(at_tree("CLAUDE.md"), at_tree)

    earlier = []
    for rev, what in BASELINES:
        reading = measure(git_show(rev, "CLAUDE.md"), lambda p, r=rev: git_show(r, p))
        earlier.append({
            "commit": rev,
            "what_that_commit_is": what,
            "the_regime_this_reading_was_taken_under": reading["the_regime_this_reading_was_taken_under"],
            "total_characters": reading["total_characters"],
            "the_pointer_rule_a_named_there": reading["the_pointer_rule_a_names"],
            "the_reading_of_claude_md_there": reading["the_reading_of_claude_md"],
            "characters_per_member": reading["characters_per_member"],
            "further_spans_of_the_same_artifact_NOT_counted_into_the_read":
                reading["further_spans_of_the_same_artifact_NOT_counted_into_the_read"],
        })

    movement = []
    for row in earlier:
        delta = now["total_characters"] - row["total_characters"]
        crossed = row["the_regime_this_reading_was_taken_under"] != \
            now["the_regime_this_reading_was_taken_under"]
        movement.append({
            "from_commit": row["commit"],
            "from_total": row["total_characters"],
            "from_regime": row["the_regime_this_reading_was_taken_under"],
            "to_total": now["total_characters"],
            "to_regime": now["the_regime_this_reading_was_taken_under"],
            "change_in_characters": delta,
            "change_percent": round(100.0 * delta / row["total_characters"], 2),
            "★_this_comparison_crosses_a_regime_boundary": crossed,
            "what_that_means_here":
                ("the two sides answer DIFFERENT questions — one side counts the whole of "
                 "`CLAUDE.md` because that was the practice there, the other counts only the spans "
                 "the ruled membership names — so the change is not a saving one act made, and "
                 "must not be read as one" if crossed else
                 "both sides are the same question, so the change is a movement of the read itself"),
        })

    return {
        "what_this_is":
            "WHAT AN ORDINARY SESSION READS AT SESSION START, in characters, measured at the tree "
            "and at each recorded earlier commit's git OBJECT. A MEASUREMENT ONLY: it edits "
            "nothing, moves no rule and grades nothing. Every value is computed; none is "
            "transcribed (D-431).",
        "generated_by": "tools/audit/gen_session_start_read_size.py",
        "generated_for": "cc_instruction_preparation_tenth.md, Task 2, step 6",
        "how_a_key_span_is_counted":
            "the artifact is written with one-space indentation, so a key's span runs from the "
            "line that opens it to the line that opens the next key at the SAME indentation, and "
            "the size is the characters of that span — what a reader reads, not a re-serialisation",
        "★_how_a_span_of_claude_md_is_counted_and_how_each_is_located":
            "every span is named by its HEADING and never by a line number (D-307), and a heading "
            "must be found EXACTLY ONCE in heading form or the run STOPs. A span runs from its "
            "heading through the line before the next heading at the same or a higher level, with "
            "trailing blank lines dropped, and its size is the characters of those lines joined by "
            "newlines — what a reader actually reads. Two spans are not headings and are located by "
            "the anchors the membership block itself quotes: the session-start read block, which "
            "has no heading of its own, and the close of the Guiding principles span. An anchor is "
            "sought OUTSIDE the membership block, because the block quotes the anchors it names "
            "spans by and the naming is not the thing named.",
        "★_what_an_ordinary_session_reads_of_claude_md_and_why_it_stopped_being_the_whole_file":
            "the user ruled on 2026-09-07 what a session reads OF `CLAUDE.md` itself: SIX spans at "
            "session start, EIGHT read only when the session's work touches them. Until this repair "
            "this tool measured the WHOLE FILE as an ordinary session's read, which after that "
            "ruling counts eight CONDITIONAL spans into a read no ordinary session takes — the same "
            "error the conditional-read statement below already refuses for `BUILD_AND_TEST.md`. "
            "`--check` could not see it: it re-derives this artifact and compares rendered text, so "
            "a fault in the DEFINITION of what is measured re-derives identically and the check "
            "passes while the measurement overstates (#19). The measured difference is published at "
            "`at_the_tree` → `the_reading_of_claude_md`.",
        "what_is_authored": "the membership of whole documents; two of the three carry the clause "
                            "in `CLAUDE.md` that makes them members, and `CLAUDE.md`'s own clause "
                            "is DERIVED from its membership block rather than retyped here",
        "what_is_derived": "the artifact-and-key pointer, parsed from rule (a)'s own clause, so a "
                           "later narrowing moves this measurement without editing this tool; what "
                           "an ordinary session reads OF `CLAUDE.md`, parsed from that file's own "
                           "membership block on the same idiom — every span name, every heading and "
                           "every anchor; every character count; the total; and each earlier "
                           "reading",
        "★_the_further_spans_and_why_they_are_here":
            "TWO FURTHER SPANS of the SAME artifact rule (a) points at are measured beside the read "
            "and are NEVER summed into it. They are the two of Ruling 3's five published figures "
            "this tool did not previously derive — the 216 gating rows' recorded grounds, and the "
            "comparison with the frozen record — and they are here because a correction ordered BY "
            "CITATION cannot be made to a figure no generator produces (D-431). A session reads the "
            "ANSWER at boot and opens these to challenge a verdict, which is why counting them "
            "would report a read no ordinary session takes.",
        "the_membership": [
            {"document": p,
             "the_clause_that_makes_it_a_member":
                 now["the_reading_of_claude_md"]["the_clause_that_makes_it_a_member"]
                 if p == "CLAUDE.md" else w,
             "how_much_of_it_an_ordinary_session_reads":
                 now["the_reading_of_claude_md"]["regime"] if p == "CLAUDE.md" else "the whole file"}
            for p, w in MEMBERS],
        "a_conditional_read_is_not_a_member":
            "`BUILD_AND_TEST.md`, `docs/scoring_model.md` and the joint estimator's section of "
            "`ARCHITECTURE.md` are read by the sessions their conditions name and not by an "
            "ordinary one, which is what CONDITIONAL means. Counting them would report a read no "
            "ordinary session takes.",
        "at_the_tree": now,
        "at_earlier_commits": earlier,
        "movement_against_each_earlier_reading": movement,
        "what_this_does_not_assert": [
            "That the membership is complete — it is AUTHORED, and a mandatory read added to "
            "`CLAUDE.md` without being added here would not appear. Each member carries the clause "
            "it comes from so the authored half is checkable by reading three clauses.",
            "That any span's BOUNDS are the ones the ruled membership intends. What is established "
            "is that the two populations are the same, that every named span resolved, and that no "
            "span was measured as a silent zero.",
            "That the read is small enough, which is [[OI-370]]'s own subject.",
            "That a session reads nothing else. A session opens the INDEX when it needs a row, the "
            "grounds when it challenges a verdict, and whatever its own dispatch orders; none of "
            "that is the session-start read.",
        ],
    }


def main(argv: list[str]) -> int:
    art = build()
    text = json.dumps(art, indent=1, ensure_ascii=False) + "\n"
    if "--check" in argv:
        have = at_tree(os.path.relpath(OUT, ROOT).replace("\\", "/")) if os.path.exists(OUT) else ""
        if have != text:
            print("STALE vs the measurement: session_start_read_size.json does not re-derive")
            return 1
        print("the session-start read measurement re-derives")
    else:
        with io.open(OUT, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        print("wrote %s" % os.path.relpath(OUT, ROOT).replace("\\", "/"))
    now = art["at_the_tree"]
    print("  rule (a) points at %s -> %s"
          % (now["the_pointer_rule_a_names"]["artifact"],
             " -> ".join(now["the_pointer_rule_a_names"]["keys"])))
    reading = now["the_reading_of_claude_md"]
    print("  CLAUDE.md is read under the regime: %s" % reading["regime"])
    for span in reading.get("the_session_start_spans", []):
        print("    [session start] %-53s %8d" % (span["name"][:53], span["characters"]))
    for span in reading.get(
            "the_conditional_spans_measured_beside_the_read_and_never_summed_into_it", []):
        print("    [conditional  ] %-53s %8d" % (span["name"][:53], span["characters"]))
    over = reading.get("★_the_overstatement_this_repair_removes")
    if over:
        print("  whole file %d, the six session-start spans %d, overstated by %d"
              % (over["the_former_measurement_the_whole_file"],
                 over["the_repaired_measurement_the_six_session_start_spans"],
                 over["characters_the_former_measurement_overstated_by"]))
    for name, n in now["characters_per_member"].items():
        print("    %-70s %8d" % (name, n))
    print("  total at the tree %d" % now["total_characters"])
    print("  further spans of the same artifact, NOT counted into the read:")
    for name, row in now["further_spans_of_the_same_artifact_NOT_counted_into_the_read"].items():
        print("    %-70s %8d" % (name, row["characters"]))
    for row in art["movement_against_each_earlier_reading"]:
        print("  vs %s: %d [%s] -> %d [%s]  (%+d, %+.2f%%)%s"
              % (row["from_commit"][:10], row["from_total"], row["from_regime"],
                 row["to_total"], row["to_regime"],
                 row["change_in_characters"], row["change_percent"],
                 "  <- CROSSES A REGIME BOUNDARY"
                 if row["★_this_comparison_crosses_a_regime_boundary"] else ""))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except Stop as exc:
        print("STOP: %s" % exc)
        sys.exit(2)
