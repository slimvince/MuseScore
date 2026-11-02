#!/usr/bin/env python3
"""WHAT A SESSION READS BEFORE ITS WORK, MEMBER BY MEMBER — AND `CLAUDE.md`'S SIX SESSION-START SPANS,
PARTITIONED BY THE RULED CLASSES.  A MEASUREMENT ONLY: it moves no text, edits nothing, proposes
nothing, gives no span a fate and decides nothing.

WHAT IT IS.  One artifact, `per_session_reading.json`, carrying two tables.

  TABLE 1 — what a session reads before its work begins, as the two sides now read it.  The
  ordinary session-start read is IMPORTED from `gen_session_start_read_size.py` (its `measure`
  function, called at the tree) and never re-measured here; beside it stand the members that tool
  does not cover: the whole of `CLAUDE.md` as the executing sessions report it injected at boot;
  `BUILD_AND_TEST.md`; the dispatch-protocol section of `cowork_audit_protocol.md`, its marked
  standing clauses and its unmarked sections apart; every dispatch and every report of the L3
  comparison arc, derived from the file system; the blind derivation of L3; and the Cowork writing
  side's boot chain of handoff entries.  Each member carries its size in characters, which side
  reads it, how it is located, and WHAT MANDATES IT — one of four classes, the record cited.

  TABLE 2 — the six session-start spans of `CLAUDE.md`, parsed out of that file's own membership
  block by the IMPORTED reader, each cut by the IMPORTED finer cut of
  `gen_claude_md_finer_spans.py`, each sub-block classed by that tool's IMPORTED classifier under
  the ruled classes and read for the amendment-record shape by its IMPORTED `shape_of`; sizes per
  class and per shape element, per span and in total; the marked defense clauses beside them, from
  the IMPORTED defense-share measurement; and, by text hash, the sub-blocks earlier sittings
  already settled, so that nobody re-proposes them.

AND, SINCE 2026-11-02, THREE ADDITIONS (`cc_instruction_per_session_reading_extension_2026_11_02.md`,
Task 2 — step 4's second dispatch).  (1) THE INVARIANT SHARE: for each dispatch and each report of the
arc, the characters on lines it shares with its predecessor (the member before it in the population's
own order), matched line for line with line endings, order ignored, whitespace-only lines apart — the
figure the dispatch-form question waits for (handoff entry 464 §1).  (2) THE APPENDIX FILE BESIDE A
REPORT: under Ruling 4 of the 2026-11-01 record a report's raw printouts stand in `<stem>_appendix.md`
beside it; appendix files leave the populations, are sized beside their reports, and every report of
the folder with one is listed with both sizes.  (3) RULING 2's AFTER-FIGURE: the Claude Code side's
per-batch total with the six spans' file-tool read replaced by the injected copy.

WHY IT EXISTS.  The user's instruction of 2026-10-31, in his words: *"After group 5, together with
the member's feet and closing sections is a natural break: plan a pruning iteration (shrink the
context occupied every session by mandatory reading ), then continue."*  The plan the writing side
put to him and he answered *"continue"* to is at `records/cowork/handoff/
cowork_handoff_entry_four_hundred_and_sixty_one.md` §2, and its STEP 1 is to measure before
anything moves (D-277, measure before build).  Built under
`cc_instruction_per_session_reading_measurement_2026_11_01.md` Task 1, whose first write-mode run
STOPPED on an authored anchor the file does not carry, the source kept as a loose blob; recovered,
amended at three sites and completed under
`cc_instruction_per_session_reading_measurement_remainder_2026_11_01.md` Task 1.

WHAT IS AUTHORED AND WHAT IS DERIVED
------------------------------------
authored : the MEMBERSHIP of the further members — each row with the side that reads it, how it
           is located, its mandate class and the record cited for that class; the DEFINITIONS of
           the four mandate classes (`MANDATE_CLASSES`); the anchors that locate a portion (the
           protocol section's heading and its standing-clause marker, the bridge-fault heading of
           entry 118, the two openers of entry 152); the name prefixes the two arc populations and
           the handoff population are derived by; and the TWO TOTALS-BY-SIDE COMPOSITIONS, each
           naming every member it sums and every read it leaves out.
derived  : every size, every count, every population, every partition and every hash match.  The
           ordinary read, the six spans, the finer cut, the classes, the shape and the marked
           defense are each IMPORTED and called as written, never re-implemented (#6).  No value
           is transcribed (D-431).  Three choices in how these are derived, each AUTHORED by the
           remainder dispatch named under WHY IT EXISTS above:
             * THE PROTOCOL PARTITION'S ACCOUNTING.  A located portion is its lines joined by
               newlines, so the opening prose, the marked and the unmarked sections sum to the
               section LESS the newline joining each portion to the next.  Those joining newlines
               are counted explicitly, and the run STOPs unless opening + marked + unmarked +
               joining newlines = the section; the equality is exact and is published.
             * THE SETTLED-SPAN OPENING MATCH, OVER WHITESPACE-COLLAPSED TEXT.  The two settled-span
               artifacts write `the_opening` as `" ".join(span["text"].split())[:160]`, which is
               `gen_claude_md_finer_spans.build()`'s own form.  A raw comparison would fail at the
               first line break of every multi-line sub-block, so whitespace is collapsed on both
               sides before the first 120 characters are compared, as the producing tool does.
             * THE ADD-COMMIT LOOKUP, ONE `git log` PER FOLDER.  A per-path call costs about a
               second here and the handoff folder holds several hundred entries, so ONE
               `git log --no-renames --diff-filter=A --format=@@%H %ct --name-only -- <folder>`
               runs per folder, and each path takes the first (newest) commit naming it — what a
               per-path call's first line gives.  That equality was proved against the per-path
               call by that dispatch's proof P6.

WHY A SIBLING AND NOT AN EXTENSION of `gen_session_start_read_size.py`.  That tool's subject is the
ORDINARY session-start read: its own docstring states that a conditional read is not a member and
that whatever a session's dispatch orders is not the session-start read.  Its `total_characters` is
the denominator `defense_share.json` publishes and two ruling records cite, and its movement rows
warn that a comparison across a regime boundary compares two different questions — so adding
dispatches, reports and the protocol section to its membership would change the meaning of a
published value and of every comparison built on it.  `gen_defense_share.py` already imports from
it rather than extending it, and this tool follows that precedent.

HOW A SIZE IS COUNTED.  A whole file's size is `len(text)` of the file read by the imported
`at_tree` (UTF-8, universal newlines).  A located portion's size is its lines joined by newlines,
as the imported `span_characters` counts a span.  Where a section is partitioned into portions,
the newlines that join one portion to the next are counted explicitly, so the portions and those
joining newlines sum to the section exactly.  A sub-block of table 2 is counted WITH its line
endings, which is the imported finer cut's own unit, and each span's text is given to that cut as
its lines joined by newlines with one closing newline added; the per-span accounting publishes
both quantities.

HOW AN ADD-COMMIT IS FOUND.  One `git log --no-renames --diff-filter=A --name-only` per folder, run
at the repository's top folder, read newest first, the first commit naming a path being that
path's add-commit — the first line a per-path `git log --diff-filter=A` would print for it.  One
call per folder rather than one per file, because a per-path call costs about a second at this
repository and the handoff folder holds several hundred entries; the equivalence for the arc's
populations was checked by the dispatch's proofs and is not asserted here beyond that check.

THE STOPS — each raised as `Stop`, printed as `STOP: …`, exit 2:
  * an imported module failing to import, or an imported function raising its own `Stop`;
  * the imported reader returning other than the ruled-membership regime, or no session-start span;
  * a span's sub-block accounting not summing to the span text given to the finer cut;
  * the protocol heading found other than exactly once;
  * the standing-clause marker found nowhere, or no `###` section judged marked;
  * the opening prose, the marked sections, the unmarked sections and the joining newlines not
    summing to the protocol section;
  * an authored member path the tree does not have;
  * a boot-chain anchor found other than exactly once, or the closing opener standing before the
    opening one;
  * a dispatch, a report or a handoff entry of a derived population with no add-commit;
  * an appendix file of the reports folder with no report beside it;
  * the imported measurement's total disagreeing with its own committed artifact at the tree;
  * the defense-share denominator disagreeing with the reader's six-span total.

WHAT THIS DOES NOT ASSERT.  That table 1's membership is complete; that any mandate class is right;
that the injected copy of `CLAUDE.md` exists or has the size of the file; that the dispatch and
report populations are complete beyond their name prefixes; that any sub-block's class is right;
that any size is small or large enough; or that any text should move.  The artifact states each of
these at `the_bounds_this_artifact_declares_on_itself`.

Run:
    python tools/audit/gen_per_session_reading.py
    python tools/audit/gen_per_session_reading.py --check
"""
from __future__ import annotations

import hashlib
import io
import json
import os
import re
import subprocess
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(HERE, "per_session_reading.json")

sys.path.insert(0, HERE)
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout


class Stop(Exception):
    """A demand of the measurement is unmet. Never a warning."""


# The four imported tools, called as they are written. A failure to import is a STOP, raised when
# the measurement is asked for rather than at import, so that it prints as one.
_IMPORT_FAILURE: Exception | None = None
try:
    import gen_session_start_read_size as ssr          # noqa: E402
    import gen_defense_share as defense                # noqa: E402
    import gen_claude_md_finer_spans as finer          # noqa: E402
    import gen_governing_surface_spans as coarse       # noqa: E402
except ImportError as exc:                             # pragma: no cover — the STOP is the report
    _IMPORT_FAILURE = exc


def _stops() -> tuple:
    """Every Stop class this measurement may meet: its own and each imported tool's."""
    if _IMPORT_FAILURE is not None:
        return (Stop,)
    return (Stop, ssr.Stop, defense.Stop, finer.Stop, coarse.Stop)


# ── AUTHORED — the four mandate classes, defined once ───────────────────────────────────────────
MANDATE_CLASSES = {
    "a user ruling": "a ruling record, or a user-ruled clause of a governing document, names the read.",
    "a standing clause": "a `###` section of `cowork_audit_protocol.md`'s dispatch-protocol section "
                         "carrying the standing-clause marker, or a clause of that kind elsewhere, "
                         "names the read.",
    "a dispatch's choice": "the writing side's dispatch orders the read, and no ruling and no "
                           "standing clause does.",
    "unwritten practice": "the read recurs every cycle and nothing on the record orders it.",
}

# ── AUTHORED — the anchors that locate a portion, each found exactly once or a STOP ─────────────
PROTOCOL_PATH = "cowork_audit_protocol.md"
PROTOCOL_HEADING = "## The dispatch protocol these audits are commissioned and run under"
STANDING_MARKER = ("*★ STANDING CLAUSE — a dispatch's read-first block requires the clause below to "
                   "be met.*")
STANDING_RATIFIED = re.compile(r"^\*\*STANDING CLAUSE \(ratified")
SECTION_HEADING = "### "

HANDOFF_FOLDER = "records/cowork/handoff"
HANDOFF_PREFIX = "cowork_handoff_entry_"
ENTRY_118 = HANDOFF_FOLDER + "/cowork_handoff_entry_one_hundred_and_eighteen.md"
BRIDGE_HEADING = "### ★★ THE BRIDGE FAULT — READ THIS BEFORE YOU WRITE ANYTHING"
ENTRY_152 = HANDOFF_FOLDER + "/cowork_handoff_entry_one_hundred_and_fifty_two.md"
OPENER_V = "**(v)**"
OPENER_X = "**(x) ★"
ENTRY_169 = HANDOFF_FOLDER + "/cowork_handoff_entry_one_hundred_and_sixty_nine.md"
ENTRY_291 = HANDOFF_FOLDER + "/cowork_handoff_entry_two_hundred_and_ninety_one.md"

DISPATCH_FOLDER = "records/cc/instructions"
DISPATCH_PREFIX = "cc_instruction_l3_comparison_tabulation_"
REPORT_FOLDER = "records/cc/reports"
REPORT_PREFIX = "cc_report_l3_comparison_tabulation_"
APPENDIX_SUFFIX = "_appendix.md"      # Ruling 4 of the 2026-11-01 record: `<stem>_appendix.md` beside `<stem>.md`

DERIVATION_PATH = "cowork_blind_derivation_l3_2026_10_17.md"
SETTLED_SOURCES = (
    ("tools/audit/claude_md_finer_archive.json", "the_left_at_site_by_the_reading"),
    ("tools/audit/claude_md_finer_archive.json", "the_refused_by_the_ruling"),
    ("tools/audit/claude_md_prune_backlog.json", "the_left_at_site_by_the_reading"),
)
SETTLED_SENTENCE = "re-proposing it is forbidden"
OPENING_WIDTH = 120
DEFENSE_DENOMINATORS = "the_denominators_both_re_derived_through_the_imported_reader_at_this_tree"


# ── reading ─────────────────────────────────────────────────────────────────────────────────────
def read(path: str) -> str:
    """A file of the tree, read by the imported `at_tree`; an absent authored path is a STOP."""
    if not os.path.exists(os.path.join(ROOT, path)):
        raise Stop("an authored member path is not in the tree: %s" % path)
    return ssr.at_tree(path)


def joined(lines: list[str]) -> int:
    """A located portion's size: its lines joined by newlines, as the imported reader counts."""
    return len("\n".join(lines))


# ── the dispatch-protocol section ───────────────────────────────────────────────────────────────
def protocol_section(text: str) -> dict:
    """The dispatch-protocol section, partitioned into its opening prose and its `###` sections.

    A `###` section is MARKED when the nearest non-blank line above its heading, stripped, is the
    standing-clause marker. Its span opens at the marker line where it has one and at its heading
    otherwise, and runs to the line before the next section's span opens, or to the end of the
    file — so every line of the section belongs to exactly one portion.
    """
    lines = text.split("\n")
    hits = [i for i, line in enumerate(lines) if line == PROTOCOL_HEADING]
    if len(hits) != 1:
        raise Stop("the protocol heading %r is found %d time(s) and must be found exactly once"
                   % (PROTOCOL_HEADING, len(hits)))
    head, end = hits[0], len(lines)
    if not any(line.strip() == STANDING_MARKER for line in lines[head:end]):
        raise Stop("the standing-clause marker is found nowhere in the protocol section")

    sections = []
    for i in range(head + 1, end):
        if not lines[i].startswith(SECTION_HEADING):
            continue
        j = i - 1
        while j > head and lines[j].strip() == "":
            j -= 1
        marked = lines[j].strip() == STANDING_MARKER
        sections.append({"heading": lines[i][len(SECTION_HEADING):].strip(),
                         "heading_line_at_the_tree": i + 1,
                         "marked": marked, "_opens": j if marked else i})
    for k, s in enumerate(sections):
        s["_ends"] = sections[k + 1]["_opens"] if k + 1 < len(sections) else end
        s["characters"] = joined(lines[s["_opens"]:s["_ends"]])

    opening_ends = sections[0]["_opens"] if sections else end
    opening = joined(lines[head:opening_ends])
    total = joined(lines[head:end])
    marked = [s for s in sections if s["marked"]]
    unmarked = [s for s in sections if not s["marked"]]
    if not marked:
        raise Stop("no `###` section of the protocol section is judged marked")
    joins = len(sections)           # one joining newline between each consecutive pair of portions
    summed = opening + sum(s["characters"] for s in sections) + joins
    if summed != total:
        raise Stop("the opening prose, the marked and the unmarked sections and the %d joining "
                   "newlines sum to %d against the section's %d" % (joins, summed, total))

    last_lo = sections[-1]["_opens"] if sections else head
    ratified = [i for i in range(head, end) if STANDING_RATIFIED.match(lines[i])]

    def published(group: list[dict]) -> dict:
        return {"count": len(group),
                "characters": sum(s["characters"] for s in group),
                "the_sections": [{"heading": s["heading"],
                                  "heading_line_at_the_tree": s["heading_line_at_the_tree"],
                                  "characters": s["characters"]} for s in group]}

    return {
        "characters": total,
        "the_opening_prose": {"what_it_is": "from the section's heading through the line before the "
                                            "first `###` section's span opens",
                              "characters": opening},
        "the_marked_sections": published(marked),
        "the_unmarked_sections": published(unmarked),
        "newlines_joining_one_portion_to_the_next": joins,
        "the_accounting": "the opening prose + the marked sections + the unmarked sections + the "
                          "joining newlines = the section, checked on every run (a STOP otherwise)",
        "paragraphs_opening_STANDING_CLAUSE_ratified_inside_the_last_section": len(ratified),
        "all_of_those_paragraphs_lie_inside_the_last_section": all(i >= last_lo for i in ratified),
        "_sections": sections,
    }


# ── the boot-chain portions ─────────────────────────────────────────────────────────────────────
def bridge_fault_portion(text: str) -> dict:
    """Entry 118 at the `###` section headed by the bridge-fault heading, to the next `###` heading."""
    lines = text.split("\n")
    hits = [i for i, line in enumerate(lines) if line.rstrip() == BRIDGE_HEADING]
    if len(hits) != 1:
        raise Stop("the boot-chain anchor %r is found %d time(s) and must be found exactly once"
                   % (BRIDGE_HEADING, len(hits)))
    lo = hits[0]
    hi = next((j for j in range(lo + 1, len(lines)) if lines[j].startswith(SECTION_HEADING)),
              len(lines))
    return {"first_line_at_the_tree": lo + 1, "last_line_at_the_tree": hi,
            "characters": joined(lines[lo:hi])}


def roman_items_portion(text: str) -> dict:
    """Entry 152 from the line opening `**(v)**` through the end of the paragraph opening `**(x) ★`."""
    lines = text.split("\n")
    found = {}
    for opener in (OPENER_V, OPENER_X):
        hits = [i for i, line in enumerate(lines) if line.lstrip().startswith(opener)]
        if len(hits) != 1:
            raise Stop("the boot-chain anchor %r is found %d time(s) and must be found exactly once"
                       % (opener, len(hits)))
        found[opener] = hits[0]
    lo, at = found[OPENER_V], found[OPENER_X]
    if at < lo:
        raise Stop("the boot-chain anchor %r stands before %r" % (OPENER_X, OPENER_V))
    hi = ssr._paragraph_end(lines, at, len(lines))
    return {"first_line_at_the_tree": lo + 1, "last_line_at_the_tree": hi,
            "characters": joined(lines[lo:hi])}


# ── the derived populations ─────────────────────────────────────────────────────────────────────
def add_commits(folder: str) -> dict:
    """Every path under `folder` with the newest commit that ADDED it: (hash, unix time)."""
    proc = subprocess.run(["git", "log", "--no-renames", "--diff-filter=A", "--format=@@%H %ct",
                           "--name-only", "--", folder], cwd=ROOT, capture_output=True)
    if proc.returncode != 0:
        raise Stop("git log over %s failed: %s"
                   % (folder, proc.stderr.decode("utf-8", "replace").strip()))
    first: dict[str, tuple[str, int]] = {}
    current = None
    for line in proc.stdout.decode("utf-8", "replace").splitlines():
        if line.startswith("@@"):
            commit, when = line[2:].split()
            current = (commit, int(when))
        elif line.strip() and current is not None:
            first.setdefault(line.strip(), current)
    return first


def population_rows(folder: str, prefix: str, commits: dict, sized: bool = True) -> list[dict]:
    """Every file under `folder` whose name opens with `prefix`, with its add-commit; no add-commit
    is a STOP. Ordered by (time, name)."""
    rows = []
    for name in sorted(os.listdir(os.path.join(ROOT, folder))):
        if not name.startswith(prefix) or name.endswith(APPENDIX_SUFFIX):
            continue
        path = folder + "/" + name
        if path not in commits:
            raise Stop("a member of a derived population has no add-commit: %s" % path)
        commit, when = commits[path]
        row = {"name": name, "added_in_commit": commit, "added_at_unix_time": when}
        if sized:
            row["characters"] = len(read(path))
        rows.append(row)
    rows.sort(key=lambda r: (r["added_at_unix_time"], r["name"]))
    return rows


def population_summary(rows: list[dict], latest: int, latest_field: str) -> dict:
    sizes = [r["characters"] for r in rows]
    return {
        "count": len(rows),
        "characters_total": sum(sizes),
        "characters_mean": round(sum(sizes) / len(sizes)) if sizes else 0,
        "characters_min": min(sizes) if sizes else 0,
        "characters_max": max(sizes) if sizes else 0,
        latest_field: rows[-latest:],
        "the_population": rows,
    }


# ── the appendix beside a report (Ruling 4 of the 2026-11-01 record) ────────────────────────────
def pair_appendices(names: list[str]) -> dict[str, str]:
    """Every appendix file among `names`, keyed by the report it stands beside: the report of
    `<stem>_appendix.md` is `<stem>.md`. An appendix with no report beside it is a STOP."""
    present = set(names)
    pairs = {}
    for name in sorted(names):
        if not name.endswith(APPENDIX_SUFFIX):
            continue
        report = name[:-len(APPENDIX_SUFFIX)] + ".md"
        if report not in present:
            raise Stop("an appendix file has no report beside it: %s" % name)
        pairs[report] = name
    return pairs


# ── the invariant share: what a member shares line for line with its predecessor ───────────────
def shared_with_predecessor(text: str, previous: str) -> dict:
    """The characters of `text` on lines that also stand in `previous`, matched line for line with
    their line endings, each line of `previous` matched at most once, order ignored.
    Whitespace-only lines are counted apart and are not in the share."""
    available = Counter(previous.splitlines(keepends=True))
    shared = blank = 0
    for line in text.splitlines(keepends=True):
        if available[line] > 0:
            available[line] -= 1
            if line.strip():
                shared += len(line)
            else:
                blank += len(line)
    return {
        "characters": len(text),
        "characters_on_lines_shared_with_the_predecessor": shared,
        "characters_on_whitespace_only_lines_shared_and_not_counted_above": blank,
        "share_percent": round(100.0 * shared / len(text), 2) if text else 0.0,
    }


def invariant_shares(folder: str, rows: list[dict]) -> dict:
    """Each member of a derived population against the member before it in the population's own
    order (add-commit time, then name). The first member has no predecessor."""
    previous_name = previous_text = None
    shared_total = own_total = 0
    for row in rows:
        text = read(folder + "/" + row["name"])
        if previous_text is None:
            row["the_predecessor"] = None
            row["shared_with_the_predecessor"] = None
        else:
            s = shared_with_predecessor(text, previous_text)
            row["the_predecessor"] = previous_name
            row["shared_with_the_predecessor"] = s
            shared_total += s["characters_on_lines_shared_with_the_predecessor"]
            own_total += s["characters"]
        previous_name, previous_text = row["name"], text
    return {
        "members_with_a_predecessor": max(len(rows) - 1, 0),
        "their_characters": own_total,
        "their_characters_on_lines_shared_with_the_predecessor": shared_total,
        "share_percent": round(100.0 * shared_total / own_total, 2) if own_total else 0.0,
        "how_a_line_is_shared": "a line of the member, with its line ending, counts as shared when "
                                "the predecessor holds the same line not already matched; the order "
                                "of lines is ignored; whitespace-only lines are counted apart and are "
                                "not in the share. A line changed by one character counts as not "
                                "shared, and a short common line counts as shared wherever it stands.",
    }


# ── table 2: the six spans, partitioned ─────────────────────────────────────────────────────────
def normalized_opening(text: str) -> str:
    """The whitespace-collapsed opening the settled-span artifacts publish — the same normalization
    the finer tool applies when it writes `the_opening`."""
    return " ".join(text.split())[:OPENING_WIDTH]


def _add(cell: dict, size: int) -> None:
    cell["sub_blocks"] = cell.get("sub_blocks", 0) + 1
    cell["characters"] = cell.get("characters", 0) + size


def partition_the_six_spans(claude_md: str, settled: list[dict]) -> dict:
    """The six session-start spans, each cut by the imported finer cut and each sub-block classed
    by the imported classifier; the settled spans matched by hash, then by opening."""
    reading = ssr.claude_md_reading(claude_md, with_coordinates=True)
    if reading["regime"] != "ruled membership":
        raise Stop("the imported reader returned the regime %r, not the ruled membership"
                   % reading["regime"])
    spans = reading.get("the_session_start_spans", [])
    if not spans or any(s["kind"] != "session start" for s in spans):
        raise Stop("the imported reader resolved no session-start span, or a span of another kind")
    lines = claude_md.split("\n")
    archive = {coarse.FORMER_WORDING, coarse.HISTORICAL, coarse.DEFENSE}

    every = []
    per_span = []
    for span in spans:
        lo, hi = span["lo"], span["hi"]
        span_text = "\n".join(lines[lo:hi]) + "\n"
        subs, skipped = finer.spans_of(span_text)
        if sum(len(s["text"]) for s in subs) + skipped != len(span_text):
            raise Stop("the span %r: its sub-blocks and blank lines account for %d characters "
                       "against the %d given to the finer cut"
                       % (span["name"], sum(len(s["text"]) for s in subs) + skipped,
                          len(span_text)))
        rows = []
        for s in subs:
            shape = finer.shape_of(s["text"])
            cls, evidence, doubt = finer.classify(s["text"], shape)
            row = {
                "kind": s["kind"],
                "first_line_at_the_tree": lo + s["first_line"],
                "last_line_at_the_tree": lo + s["last_line"],
                "characters_with_line_endings": len(s["text"]),
                "the_class": cls,
                "the_doubt_default_decided_it": doubt,
                "the_classifiers_evidence": evidence,
                "the_amendment_record_shape": sorted(shape.keys()),
                "carries_a_ruled_date_header": "ruled_date_header" in shape,
                "text_sha256": hashlib.sha256(s["text"].encode("utf-8")).hexdigest(),
                "the_opening": s["text"][:160],
                "settled_at_an_earlier_sitting": [],
                "_normalized_opening": normalized_opening(s["text"]),
                "_span": span["name"],
            }
            rows.append(row)
            every.append(row)
        per_span.append((span, len(span_text), skipped, rows))

    # The settled spans: by hash first, by opening only where no hash matches.
    the_settled = []
    for entry in settled:
        by_hash = [r for r in every if r["text_sha256"] == entry["text_sha256"]]
        by_opening = [r for r in every
                      if r["_normalized_opening"] == normalized_opening(entry["the_opening"])]
        if by_hash:
            how, matched = "by hash — the sub-block stands unchanged", by_hash
        elif by_opening:
            how, matched = "by its opening only — the same sub-block, amended since", by_opening
        else:
            how, matched = "not found", []
        for r in matched:
            r["settled_at_an_earlier_sitting"].append({
                "artifact": entry["artifact"], "field": entry["field"], "how": how,
                "the_sentence_the_prune_backlog_carries": SETTLED_SENTENCE})
        the_settled.append({
            "artifact": entry["artifact"], "field": entry["field"],
            "text_sha256": entry["text_sha256"], "the_opening": entry["the_opening"],
            "found_at_the_tree": how,
            "the_sub_blocks_it_matched_first_line_at_the_tree":
                [r["first_line_at_the_tree"] for r in matched],
        })

    def sums(rows: list[dict]) -> dict:
        out = {"by_kind": {}, "by_class": {}, "by_shape_element": {},
               "star_marked_sub_blocks": {"sub_blocks": 0, "characters": 0},
               "sub_blocks_carrying_a_ruled_date_header": {"sub_blocks": 0, "characters": 0},
               "archive_class_characters": 0, "doubt_defaulted_characters": 0,
               "settled_sub_blocks": {"sub_blocks": 0, "characters": 0}}
        for r in rows:
            size = r["characters_with_line_endings"]
            _add(out["by_kind"].setdefault(r["kind"], {}), size)
            _add(out["by_class"].setdefault(r["the_class"], {}), size)
            for element in r["the_amendment_record_shape"]:
                _add(out["by_shape_element"].setdefault(element, {}), size)
            if r["kind"] == "star-marked sub-block":
                _add(out["star_marked_sub_blocks"], size)
            if r["carries_a_ruled_date_header"]:
                _add(out["sub_blocks_carrying_a_ruled_date_header"], size)
            if r["the_class"] in archive:
                out["archive_class_characters"] += size
            if r["the_doubt_default_decided_it"]:
                out["doubt_defaulted_characters"] += size
            if r["settled_at_an_earlier_sitting"]:
                _add(out["settled_sub_blocks"], size)
        return out

    published_spans = []
    given_total = skipped_total = 0
    for span, given, skipped, rows in per_span:
        given_total += given
        skipped_total += skipped
        entry = {"name": span["name"], "characters": span["characters"],
                 "characters_given_to_the_finer_cut": given,
                 "characters_of_the_blank_lines_between_sub_blocks": skipped,
                 "sub_block_count": len(rows)}
        entry.update(sums(rows))
        entry["sub_blocks"] = [{k: v for k, v in r.items() if not k.startswith("_")}
                               for r in rows]
        published_spans.append(entry)

    totals = {"characters_of_the_six_spans": reading["characters"],
              "characters_given_to_the_finer_cut": given_total,
              "characters_of_the_blank_lines_between_sub_blocks": skipped_total,
              "sub_block_count": len(every),
              "how_the_two_counts_relate": "each span is given to the finer cut as its lines joined "
                                           "by newlines with one closing newline added, so the "
                                           "characters given exceed the six spans' own count by "
                                           "one per span"}
    totals.update(sums(every))
    return {
        "the_spans": published_spans,
        "totals": totals,
        "the_settled_spans": {
            "found_by_hash": sum(1 for s in the_settled if s["found_at_the_tree"].startswith("by hash")),
            "found_by_opening_only": sum(1 for s in the_settled
                                         if s["found_at_the_tree"].startswith("by its opening")),
            "not_found": sum(1 for s in the_settled if s["found_at_the_tree"] == "not found"),
            "how_a_match_is_taken": "by hash when a sub-block's text_sha256 equals the entry's; else "
                                    "by opening when the first %d characters of the sub-block's text, "
                                    "whitespace collapsed as the settled-span artifacts collapse it, "
                                    "equal the first %d of the entry's opening. None of the three "
                                    "outcomes is a STOP." % (OPENING_WIDTH, OPENING_WIDTH),
            "the_entries": the_settled,
        },
        "_reading": reading,
    }


def settled_entries() -> list[dict]:
    """The settled spans the two earlier sittings' artifacts carry, with their hashes."""
    out = []
    for path, field in SETTLED_SOURCES:
        data = json.loads(read(path))
        for entry in data.get(field, []):
            out.append({"artifact": path, "field": field,
                        "text_sha256": entry["text_sha256"], "the_opening": entry["the_opening"]})
    return out


# ── the build ───────────────────────────────────────────────────────────────────────────────────
def build() -> dict:
    if _IMPORT_FAILURE is not None:
        raise Stop("an imported module failed to import: %s" % _IMPORT_FAILURE)

    claude_md = read("CLAUDE.md")

    # ── TABLE 1 ─────────────────────────────────────────────────────────────────────────────────
    ordinary = ssr.measure(claude_md, ssr.at_tree)
    committed = json.loads(read("tools/audit/session_start_read_size.json"))
    if ordinary["total_characters"] != committed["at_the_tree"]["total_characters"]:
        raise Stop("the imported ordinary read measures %d characters and its committed artifact "
                   "says %d at the same tree" % (ordinary["total_characters"],
                                                 committed["at_the_tree"]["total_characters"]))
    six = ordinary["the_reading_of_claude_md"]["characters"]

    whole = len(claude_md)
    build_and_test = len(read("BUILD_AND_TEST.md"))
    protocol = protocol_section(read(PROTOCOL_PATH))
    derivation = len(read(DERIVATION_PATH))

    further = [
        {"member": "CLAUDE.md, the whole file as the executing sessions report it injected at boot",
         "path": "CLAUDE.md",
         "the_portion_read": "the whole file",
         "how_it_is_located": "the whole file",
         "read_by": "Claude Code, per batch — DECLARED by the executing sessions in their reports, "
                    "not established by this tool (#18)",
         "the_mandate_class": "unwritten practice",
         "the_record_that_mandates_it": "no clause of `CLAUDE.md` names the injection; the "
                                        "dispatches' clause \"injected context does not stand in "
                                        "for this read\" carries no stated ground in the record "
                                        "(entry 461 §2, item (a)); the membership block's own "
                                        "provenance paragraph records that until 2026-09-07 the "
                                        "whole-file read was PRACTICE mandated by no clause",
         "characters": whole,
         "characters_the_six_spans_read_with_the_file_tool_add_on_top_of_it": six,
         "characters_of_the_file_outside_the_six_spans": whole - six},
        {"member": "BUILD_AND_TEST.md",
         "path": "BUILD_AND_TEST.md",
         "the_portion_read": "the whole file",
         "how_it_is_located": "the whole file",
         "read_by": "Claude Code, per batch that builds, tests or runs a tool whose command lives "
                    "there — every batch of the L3 arc did, each running the guard set",
         "the_mandate_class": "a user ruling",
         "the_record_that_mandates_it": "Ruling 3 of "
                                        "`records/cowork/rulings/cowork_rulings_2026_08_17_session_"
                                        "start_read_sitting.md` — a CONDITIONAL read; `CLAUDE.md`'s "
                                        "build-and-test block states the condition",
         "characters": build_and_test},
        {"member": "cowork_audit_protocol.md, the dispatch-protocol section",
         "path": PROTOCOL_PATH,
         "the_portion_read": "from the line whose text is exactly `%s` to the end of the file"
                             % PROTOCOL_HEADING,
         "how_it_is_located": "its heading, found exactly once; a `###` section is MARKED when the "
                              "nearest non-blank line above its heading is the standing-clause "
                              "marker, and its span opens at that marker",
         "read_by": "Claude Code, per batch (every dispatch of the arc orders it IN FULL); Cowork, "
                    "per sitting that writes a dispatch",
         "the_mandate_class": {"the_marked_sections": "a user ruling",
                               "the_opening_prose_and_the_unmarked_sections": "a dispatch's choice"},
         "the_record_that_mandates_it": "Ruling 3 of "
                                        "`records/cowork/rulings/cowork_rulings_2026_08_19_thirteenth_"
                                        "return.md`, as the section's own opening paragraphs state "
                                        "it: the standing clauses are the `###` sections carrying "
                                        "the marker, obtained by reading them here; the dispatches "
                                        "order the whole section",
         "characters": protocol["characters"]},
        {"member": "the blind derivation of L3, whole",
         "path": DERIVATION_PATH,
         "the_portion_read": "the whole file",
         "how_it_is_located": "the whole file",
         "read_by": "Claude Code, per batch of the L3 comparison",
         "the_mandate_class": "a user ruling",
         "the_record_that_mandates_it": "Ruling 2 of "
                                        "`records/cowork/rulings/cowork_rulings_2026_08_24_comparison_"
                                        "design_sitting.md`, as the thirtieth dispatch's ruling "
                                        "ledger quotes it; ruled for this comparison, and not a "
                                        "target of the pruning iteration (entry 461 §2)",
         "characters": derivation},
    ]
    further[2].update({k: v for k, v in protocol.items()
                       if k not in ("characters", "_sections")})

    instructions = add_commits(DISPATCH_FOLDER)
    reports = add_commits(REPORT_FOLDER)
    handoffs = add_commits(HANDOFF_FOLDER)
    dispatch_rows = population_rows(DISPATCH_FOLDER, DISPATCH_PREFIX, instructions)
    report_rows = population_rows(REPORT_FOLDER, REPORT_PREFIX, reports)
    handoff_rows = population_rows(HANDOFF_FOLDER, HANDOFF_PREFIX, handoffs, sized=False)
    latest_entries = handoff_rows[-3:]
    for r in latest_entries:
        r["characters"] = len(read(HANDOFF_FOLDER + "/" + r["name"]))

    dispatch_shares = invariant_shares(DISPATCH_FOLDER, dispatch_rows)
    report_shares = invariant_shares(REPORT_FOLDER, report_rows)
    appendix_pairs = pair_appendices(sorted(os.listdir(os.path.join(ROOT, REPORT_FOLDER))))
    for row in report_rows:
        beside = appendix_pairs.get(row["name"])
        row["the_appendix_beside_it"] = (
            {"name": beside, "characters": len(read(REPORT_FOLDER + "/" + beside))} if beside else None)
    reports_with_an_appendix = []
    for report, beside in sorted(appendix_pairs.items()):
        proper = len(read(REPORT_FOLDER + "/" + report))
        appendix = len(read(REPORT_FOLDER + "/" + beside))
        reports_with_an_appendix.append({
            "the_report": report,
            "characters_of_the_report_proper": proper,
            "the_appendix": beside, "characters_of_the_appendix": appendix,
            "the_appendix_share_of_the_two_percent":
                round(100.0 * appendix / (proper + appendix), 2) if proper + appendix else 0.0,
        })

    the_dispatches = {
        "the_folder": DISPATCH_FOLDER, "the_name_prefix": DISPATCH_PREFIX,
        "read_by": "Claude Code, per batch (its own dispatch, whole); Cowork, per sitting that "
                   "writes the next dispatch (the previous dispatch whole, for its form)",
        "the_mandate_class": {"the_executing_sides_read": "a dispatch's choice",
                              "the_writing_sides_read_of_the_previous": "unwritten practice"},
        "the_record_that_mandates_it": "the user's opening line names the dispatch and D-252 binds "
                                       "the executing side to it; its SIZE is the writing side's "
                                       "choice; no record orders the writing side's read of the "
                                       "previous dispatch",
    }
    the_dispatches.update(population_summary(dispatch_rows, 5, "the_last_five"))
    the_dispatches["the_invariant_share"] = dispatch_shares
    the_reports = {
        "the_folder": REPORT_FOLDER, "the_name_prefix": REPORT_PREFIX,
        "read_by": "Cowork, per sitting (whole); Claude Code, per batch (at the portions its "
                   "dispatch orders — not sized here)",
        "the_mandate_class": "a user ruling",
        "the_record_that_mandates_it": "the user's rule of 2026-09-03 — Claude Code's output is "
                                       "read in full — carried in the handoff entries (entry 461 §4)",
    }
    the_reports.update(population_summary(report_rows, 3, "the_last_three"))
    the_reports["the_invariant_share"] = report_shares
    the_reports["the_appendices_beside_them"] = {
        "count": sum(1 for r in report_rows if r["the_appendix_beside_it"]),
        "characters_total": sum(r["the_appendix_beside_it"]["characters"]
                                for r in report_rows if r["the_appendix_beside_it"]),
        "how_these_relate_to_the_sizes_above": "every size above is of the report proper only; an "
                                               "appendix file is sized here and in "
                                               "`the_reports_with_an_appendix_beside_them`, never "
                                               "added to the report's own size",
    }

    chain_record = ("the writing side's own boot instruction — entry 291 §4 step 3 and entry 169's "
                    "Boot block; no user ruling names these reads")
    bridge = bridge_fault_portion(read(ENTRY_118))
    roman = roman_items_portion(read(ENTRY_152))
    boot_chain = [
        dict({"member": "entry 118, the bridge-fault section", "path": ENTRY_118,
              "the_portion_read": "the `###` section headed `%s`, to the line before the next "
                                  "`###` heading" % BRIDGE_HEADING,
              "read_by": "Cowork, per sitting", "the_mandate_class": "unwritten practice",
              "the_record_that_mandates_it": chain_record}, **bridge),
        dict({"member": "entry 152, items (v) to (x)", "path": ENTRY_152,
              "the_portion_read": "from the line opening `%s` through the end of the paragraph "
                                  "whose first line opens `%s`" % (OPENER_V, OPENER_X),
              "read_by": "Cowork, per sitting", "the_mandate_class": "unwritten practice",
              "the_record_that_mandates_it": chain_record}, **roman),
        {"member": "entry 169, whole", "path": ENTRY_169, "the_portion_read": "the whole file",
         "read_by": "Cowork, per sitting", "the_mandate_class": "unwritten practice",
         "the_record_that_mandates_it": chain_record, "characters": len(read(ENTRY_169))},
        {"member": "entry 291, whole", "path": ENTRY_291, "the_portion_read": "the whole file",
         "read_by": "Cowork, per sitting", "the_mandate_class": "unwritten practice",
         "the_record_that_mandates_it": chain_record, "characters": len(read(ENTRY_291))},
        {"member": "the three handoff entry files with the latest add-commits",
         "path": HANDOFF_FOLDER, "the_portion_read": "each whole",
         "how_it_is_located": "every file of the folder whose name opens `%s`, ordered by its "
                              "add-commit; the three latest" % HANDOFF_PREFIX,
         "read_by": "both sides: the executing side reads the ones its dispatch's read-first block "
                    "names; the writing side reads the three latest",
         "the_mandate_class": {"the_executing_sides_read": "a standing clause",
                               "the_writing_sides_read": "unwritten practice"},
         "the_record_that_mandates_it": "the standing clause `Every dispatch's read-first block "
                                        "names the CURRENT HANDOVER BLOCK`, which this repository "
                                        "carries as numbered entry files; the writing side's three "
                                        "is its own practice",
         "the_population_count": len(handoff_rows),
         "the_three": latest_entries,
         "characters": sum(r["characters"] for r in latest_entries)},
    ]

    ordinary_total = ordinary["total_characters"]
    latest_dispatch = dispatch_rows[-1] if dispatch_rows else None
    latest_report = report_rows[-1] if report_rows else None
    three_entries = boot_chain[4]["characters"]
    cc_members = [
        ("the ordinary session-start read (imported)", ordinary_total),
        ("BUILD_AND_TEST.md", build_and_test),
        ("the dispatch-protocol section of cowork_audit_protocol.md, whole", protocol["characters"]),
        ("the latest dispatch of the arc: %s" % (latest_dispatch or {}).get("name"),
         (latest_dispatch or {}).get("characters", 0)),
        ("the blind derivation of L3", derivation),
        ("the three handoff entry files with the latest add-commits", three_entries),
    ]
    cc_without = sum(n for _, n in cc_members)
    cowork_members = [
        ("the ordinary session-start read (imported)", ordinary_total),
    ] + [(row["member"], row["characters"]) for row in boot_chain] + [
        ("the latest report of the arc, whole: %s" % (latest_report or {}).get("name"),
         (latest_report or {}).get("characters", 0)),
        ("the latest dispatch of the arc, whole: %s" % (latest_dispatch or {}).get("name"),
         (latest_dispatch or {}).get("characters", 0)),
    ]
    totals_by_side = {
        "Claude Code, per batch, in the thirtieth dispatch's shape": {
            "the_members_it_sums": [{"member": m, "characters": n} for m, n in cc_members],
            "without_the_injected_copy_of_CLAUDE_md": cc_without,
            "with_it": cc_without + whole,
            "the_injected_copy_added_in_with_it": "CLAUDE.md, the whole file, %d characters" % whole,
            "under_ruling_2_of_2026_11_01": cc_without + whole - six,
            "how_ruling_2_moves_it": "Ruling 2 of `records/cowork/rulings/cowork_rulings_2026_11_01_"
                                     "pruning_iteration_sitting.md`: the injected copy is the read of "
                                     "the six spans, so their file-tool read (%d characters) leaves the "
                                     "sum and the injected copy stays; the eight-line check's own reads "
                                     "are not sized here" % six,
            "left_out_and_said_so": "the previous report at the portions a dispatch orders, the "
                                    "reading file at its ordered portions, the ruling records a "
                                    "dispatch orders — varies per dispatch and is not sized here",
        },
        "Cowork, per sitting, in the shape of the sitting of entry 461": {
            "the_members_it_sums": [{"member": m, "characters": n} for m, n in cowork_members],
            "characters": sum(n for _, n in cowork_members),
            "left_out_and_said_so": "the verification reads at the objects (the reading file at its "
                                    "sections, the guard state, the ref files, the away-returns "
                                    "close) — varies per batch and is not sized here",
        },
    }

    # ── TABLE 2 ─────────────────────────────────────────────────────────────────────────────────
    partition = partition_the_six_spans(claude_md, settled_entries())
    d = defense.build()
    denominators = d[DEFENSE_DENOMINATORS]
    if denominators["the_six_session_start_spans"] != partition["totals"]["characters_of_the_six_spans"]:
        raise Stop("the defense-share denominator is %d and the reader's six-span total is %d"
                   % (denominators["the_six_session_start_spans"],
                      partition["totals"]["characters_of_the_six_spans"]))

    return {
        "what_this_is":
            "WHAT A SESSION READS BEFORE ITS WORK, MEMBER BY MEMBER, with size and mandate (table 1), "
            "and `CLAUDE.md`'s six session-start spans partitioned by the ruled classes and the "
            "amendment-record shape (table 2), measured at the tree. A MEASUREMENT ONLY: it moves no "
            "text, gives no span a fate, proposes nothing and decides nothing. Every value is "
            "computed; none is transcribed (D-431).",
        "generated_by": "tools/audit/gen_per_session_reading.py",
        "generated_for": "cc_instruction_per_session_reading_extension_2026_11_02.md, Task 2 — step 4's "
                         "second dispatch of the pruning iteration the user ordered on 2026-10-31; "
                         "first built for step 1 (cc_instruction_per_session_reading_measurement_"
                         "2026_11_01.md, Task 1)",
        "the_four_mandate_classes": MANDATE_CLASSES,
        "how_a_size_is_counted":
            "a whole file is `len(text)` of the file read by the imported `at_tree` (UTF-8, universal "
            "newlines); a located portion is its lines joined by newlines, as the imported reader "
            "counts a span; a sub-block of table 2 is counted WITH its line endings, the imported "
            "finer cut's own unit",
        "how_an_add_commit_is_found":
            "one `git log --no-renames --diff-filter=A --name-only` per folder at the repository's "
            "top folder, read newest first; the first commit naming a path is its add-commit",
        "table_1_the_per_session_reading": {
            "the_ordinary_session_start_read_imported": {
                "its_one_home": "`tools/audit/session_start_read_size.json`, written by "
                                "`tools/audit/gen_session_start_read_size.py`; what stands here is "
                                "that tool's own `measure` called at the tree, and its total is "
                                "checked against that artifact on every run",
                "characters_per_member": ordinary["characters_per_member"],
                "total_characters": ordinary_total,
                "the_reading_of_claude_md": {
                    "regime": ordinary["the_reading_of_claude_md"]["regime"],
                    "characters": six,
                },
            },
            "the_further_members": further,
            "the_arc_dispatches": the_dispatches,
            "the_arc_reports": the_reports,
            "the_reports_with_an_appendix_beside_them": {
                "the_folder": REPORT_FOLDER,
                "how_a_pair_is_found": "every file of the folder whose name ends `%s`, beside the report "
                                       "named by its stem; an appendix with no report beside it is a "
                                       "STOP" % APPENDIX_SUFFIX,
                "read_by": "Cowork: the report proper in full under the user's rule of 2026-09-03, the "
                           "appendix at need (Ruling 4 of the 2026-11-01 record)",
                "count": len(reports_with_an_appendix),
                "characters_of_the_reports_proper": sum(r["characters_of_the_report_proper"]
                                                        for r in reports_with_an_appendix),
                "characters_of_the_appendices": sum(r["characters_of_the_appendix"]
                                                    for r in reports_with_an_appendix),
                "the_pairs": reports_with_an_appendix,
            },
            "the_cowork_boot_chain": boot_chain,
            "totals_by_side": totals_by_side,
        },
        "table_2_the_six_spans_partitioned": {
            "where_the_spans_cut_and_classes_come_from":
                "the spans from `gen_session_start_read_size.claude_md_reading`; the cut, the shape "
                "and the class from `gen_claude_md_finer_spans.spans_of`, `shape_of` and `classify`; "
                "the class names from `gen_governing_surface_spans`. Nothing is re-implemented and "
                "no class or verdict is added here.",
            "the_archive_classes_summed_in_archive_class_characters":
                [coarse.FORMER_WORDING, coarse.HISTORICAL, coarse.DEFENSE],
            "the_spans": partition["the_spans"],
            "totals": partition["totals"],
            "the_settled_spans": partition["the_settled_spans"],
            "the_marked_defense_clauses_imported": {
                "from": "`tools/audit/gen_defense_share.py` → `build()`, called at the tree",
                "the_totals": d["the_totals"],
                "per_span": d["per_span"],
                "the_two_denominators": {
                    "the_six_session_start_spans": denominators["the_six_session_start_spans"],
                    "the_whole_ordinary_session_start_read":
                        denominators["the_whole_ordinary_session_start_read"],
                },
                "how_these_relate_to_the_sums_above":
                    "a marked clause lies INSIDE a sub-block, so these values overlap table 2's "
                    "sums and are never added to them",
            },
        },
        "the_bounds_this_artifact_declares_on_itself": [
            "Table 1's membership is AUTHORED, and a read nobody wrote into it does not appear.",
            "Each mandate class is the writing side's authored reading of the record, cited per row "
            "and challengeable there; the user rules on it.",
            "The injected copy of `CLAUDE.md` is DECLARED by the executing sessions; this tool "
            "measures the file, not the copy.",
            "The dispatch and report populations are complete only relative to their name prefixes.",
            "The invariant share is a LINE measure, not a judgement of copying: a line changed by one "
            "character counts as not shared, and a short common line counts as shared wherever it "
            "stands. It compares each member with its predecessor only.",
            "An appendix file is found by its name alone (`<stem>_appendix.md` beside `<stem>.md`).",
            "The imported recognizers are patterns over prose whose reach is UNMEASURED (D-673 "
            "applies: no analysis decision consumes this enumeration); the doubt default places "
            "what no recognizer places; and a sub-block cut at a ★ marker may carry a sentence that "
            "continues in the next.",
        ],
        "what_this_does_not_assert": [
            "That the membership of table 1 is complete.",
            "That any mandate class is right.",
            "That the injected copy of `CLAUDE.md` exists or has the size of the file.",
            "That the dispatch and report populations are complete beyond the name prefixes.",
            "That a line shared with the predecessor was copied from it, or that a line not shared "
            "was newly written.",
            "That any sub-block's class is right.",
            "That any size is small or large enough — that is the user's question at step 3.",
            "That any text should move — this tool proposes nothing.",
        ],
    }


def main(argv: list[str]) -> int:
    art = build()
    text = json.dumps(art, indent=1, ensure_ascii=False) + "\n"
    if "--check" in argv:
        rel = os.path.relpath(OUT, ROOT).replace("\\", "/")
        have = ssr.at_tree(rel) if os.path.exists(OUT) else ""
        if have != text:
            print("STALE vs the measurement: per_session_reading.json does not re-derive")
            return 1
        print("the per-session reading measurement re-derives")
    else:
        with io.open(OUT, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        print("wrote %s" % os.path.relpath(OUT, ROOT).replace("\\", "/"))
    t1 = art["table_1_the_per_session_reading"]
    print("  the ordinary session-start read (imported) %d"
          % t1["the_ordinary_session_start_read_imported"]["total_characters"])
    for row in t1["the_further_members"]:
        print("    %-70s %8d" % (row["member"][:70], row["characters"]))
    print("  arc dispatches %d, %d characters; arc reports %d, %d characters"
          % (t1["the_arc_dispatches"]["count"], t1["the_arc_dispatches"]["characters_total"],
             t1["the_arc_reports"]["count"], t1["the_arc_reports"]["characters_total"]))
    print("  invariant share: dispatches %.2f %%, reports %.2f %%"
          % (t1["the_arc_dispatches"]["the_invariant_share"]["share_percent"],
             t1["the_arc_reports"]["the_invariant_share"]["share_percent"]))
    ap = t1["the_reports_with_an_appendix_beside_them"]
    print("  reports with an appendix beside them %d: reports proper %d, appendices %d characters"
          % (ap["count"], ap["characters_of_the_reports_proper"], ap["characters_of_the_appendices"]))
    for name, side in t1["totals_by_side"].items():
        value = side.get("without_the_injected_copy_of_CLAUDE_md", side.get("characters"))
        print("  %s: %d" % (name, value))
    t2 = art["table_2_the_six_spans_partitioned"]["totals"]
    print("  six spans %d characters, %d sub-blocks, archive-class %d, doubt-defaulted %d"
          % (t2["characters_of_the_six_spans"], t2["sub_block_count"],
             t2["archive_class_characters"], t2["doubt_defaulted_characters"]))
    st = art["table_2_the_six_spans_partitioned"]["the_settled_spans"]
    print("  settled spans: %d by hash, %d by opening only, %d not found"
          % (st["found_by_hash"], st["found_by_opening_only"], st["not_found"]))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except _stops() as exc:
        print("STOP: %s" % exc)
        sys.exit(2)
