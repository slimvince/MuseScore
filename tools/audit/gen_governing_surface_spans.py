#!/usr/bin/env python3
"""THE FIVE MANDATORY-READ FILES, DECOMPOSED SPAN BY SPAN AND CLASSED — the pruning measurement.

THE RULING THIS EXISTS FOR.  User, 2026-08-16, §5(A) of
`cowork_rulings_2026_08_16_preparation_return.md`, on the user's own stated ground: *"we need to
prune (at least) claude.md and open_items.md because the mandatory reads at session start for you
and CC are too large (we are already hitting quality problems - and there are also other issues
like real monetary cost and response times)."*  The ordered batch is READ-ONLY: *"a per-file
decomposition by span (operative rule text; preserved former wordings; defenses and
declined-alternatives records; self-declared historical or superseded blocks; resolved rows) and
the reader/anchor/quote inventory over all five files, delivering a ratification surface with
per-span fates."*

★ THIS TOOL MEASURES.  IT PROPOSES NOTHING AND IT MOVES NOTHING.  No governing file is edited,
and no span's fate is decided here — the fates are proposed on the ratification surface the
companion tool generates, the user rules that surface, and a LATER dispatch executes.

WHAT A SPAN IS, so the unit is mechanical rather than a matter of taste.
  * A BLOCK — a maximal run of consecutive non-blank lines.  Blank lines separate spans, which is
    the same block rule the deciding-act recovery pass already uses over this record (#6).
  * A FENCED CODE BLOCK is ONE span whatever blank lines it contains: splitting a command recipe
    at a blank line would produce spans that are not readable on their own.
  * A TABLE ROW is its own span.  Consecutive rows of a markdown table carry no blank line between
    them, so without this the whole open-items index would be one span and the ruled `resolved
    row` class could not be measured at all.
  * A BLOCK IS CUT AGAIN AT EVERY ★ MARKER LINE.  This is the record's OWN convention, not an
    invention: `CLAUDE.md` opens each amendment, each preserved former wording and each
    declined-alternatives record with a line beginning `**★`, inside a numbered principle that
    carries no blank line from end to end.  Without this cut a whole principle is ONE span, and a
    single `FORMER WORDING` marker inside it would class fourteen thousand characters of live rule
    text as archive material — an error in the direction the ruled doubt default exists to
    prevent.  MEASURED, not argued: before the cut, three spans of `CLAUDE.md` carried 26.8% of
    the file into `preserved-former-wording`.

THE CLASSES, and the order they are applied in.  Each is decided from the span's OWN TEXT, and the
evidence — the matched marker, quoted — is published beside every verdict.

  1. `resolved-row`                    a table row whose status cell opens with the resolved mark.
                                       The row split and the leading-token test are IMPORTED from
                                       the one index lint that owns them (#6), never re-implemented.
  2. `self-declared-historical-or-superseded`
                                       a span that says of ITSELF that it is historical, superseded,
                                       retired, frozen or retained for provenance.
  3. `preserved-former-wording`        a span that carries a former wording preserved under #12.
  4. `defense-and-declined-alternatives`
                                       a span recording a DECLINED alternative or an ACCEPTED COST.
                                       Deliberately NARROW: a bare *Why:* is a rule's purpose, and
                                       the ruled test keeps the purpose that bounds a rule's
                                       application AT SITE.  Only an explicit declined-alternative
                                       or accepted-cost marker is recognised here.
  5. `pointer-entry-of-a-completed-batch`
                                       a dated STATUS.md entry that is a POINTER under the OI-222
                                       remedy — it names the report and the close and restates
                                       nothing (D-431).
  6. `operative-rule-text`             everything else, and the DOUBT DEFAULT.

★ THE DOUBT DEFAULT IS THE RULING'S OWN, AND IT IS RECORDED PER SPAN.  *"A span the test cannot
place STAYS AT SITE"* — so a span the recognizers do not positively place falls to
`operative-rule-text` and carries `placed_by_the_doubt_default: true`.  A reader can therefore see
exactly how much of each file is classed by evidence and how much by the default, which is the
number that says whether the measurement is worth acting on.

WHAT IT DOES NOT ESTABLISH, stated before its first use: that a span classed `operative-rule-text`
IS operative — only that no recognizer placed it elsewhere.  The classes are recognizers over
prose, their reach is UNMEASURED, and the direction of their error is the recoverable one: a missed
marker keeps a span at site, which is the ruled default.

THE STOPS:
  * a file the ruling names that the tree does not carry STOPS it;
  * a span whose byte count cannot be taken STOPS it;
  * the per-class byte counts not summing to the file's own measured size STOPS it — no span may
    be silently dropped from the decomposition, which is the one failure that would make every
    number below meaningless.

Run:
  python tools/audit/gen_governing_surface_spans.py
  python tools/audit/gen_governing_surface_spans.py --check
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent

sys.path.insert(0, str(HERE))
from output_encoding import use_utf8_output                        # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

import index_status_lint as lint                                   # noqa: E402  (path set above)

OUT = HERE / "governing_surface_spans.json"

# The five mandatory session-start reads, in the ruling's own scope: the three CLAUDE.md names,
# plus DECISIONS.md "as the measurement warrants" and STATUS.md per ruling (C).
FILES = ("CLAUDE.md", "OPEN_ITEMS.md", "DECISIONS.md", "STATUS.md", "BUILD_AND_TEST.md")

RESOLVED_ROW = "resolved-row"
HISTORICAL = "self-declared-historical-or-superseded"
FORMER_WORDING = "preserved-former-wording"
DEFENSE = "defense-and-declined-alternatives"
POINTER = "pointer-entry-of-a-completed-batch"
OPERATIVE = "operative-rule-text"

CLASSES = (RESOLVED_ROW, HISTORICAL, FORMER_WORDING, DEFENSE, POINTER, OPERATIVE)

# ── AUTHORED — the recognizers, published beside the verdicts they produce ────────────────────
# Every pattern below was read in the five files themselves. Each is a phrase a span uses ABOUT
# ITSELF; none is a topic word, because a span that DISCUSSES supersession is not thereby
# superseded — that confusion is what would archive a live rule.
HISTORICAL_MARKERS = (
    r"\[SUPERSEDED\b",
    r"\bSUPERSEDED by\b",
    r"\bis SUPERSEDED\b",
    r"\bare SUPERSEDED\b",
    r"\bnow HISTORICAL\b",
    r"\bis now historical\b",
    r"\bHISTORICAL RECORD\b",
    r"\bhistorical reference only\b",
    r"\bretained for provenance\b",
    r"\bfrozen as history\b",
    r"\bfrozen historical\b",
    r"\bRETROSPECTIVE\b",
    r"\bhistorical, retained\b",
    r"\bSuperseded columns preserved\b",
    r"\bhistorical\)\s*$",
    r"— historical\b",
    r"\bno longer the governing structure\b",
    r"\bis now the superseded\b",
    r"\bthe superseded .{0,40}lineage\b",
    r"\bPrevious baseline\b",
    r"\bPrevious Jazz baseline\b",
    r"\bPrevious figures for reference\b",
    r"\bPrevious baselines for reference\b",
)
FORMER_WORDING_MARKERS = (
    r"FORMER WORDING",
    r"[Ff]ormer wording",
    r"THE FORMER \w+, PRESERVED",
    r"preserved in place \(#12\)",
    r"[Pp]reserved verbatim",
    r"THE FORMER VERDICT, PRESERVED",
    r"[Tt]he former text",
    r"[Tt]he clause that formerly closed",
    r"formerly read",
    r"formerly carried",
)
DEFENSE_MARKERS = (
    r"\bDECLINED\b",
    r"\bdeclined as rated on the surface\b",
    r"\bALTERNATIVES? (?:B|C|D)\b",
    r"THE COSTS THE USER ACCEPTED",
    r"an accepted cost is not a discharged one",
    r"an excluded alternative is evidence about the choice",
    r"\bTRIED AND CLOSED\b",
    r"\bwas declined\b",
    r"\bwere declined\b",
    r"\bDeclined:",
)
# A STATUS.md pointer entry under the OI-222 remedy: a dated entry that names its report and its
# close and restates nothing. The marker is the remedy's own sentence, which every such entry
# carries verbatim.
POINTER_MARKERS = (
    r"this entry is a \*\*POINTER\*\*",
    r"Per the OI-222 remedy",
)

TABLE_ROW = re.compile(r"^\s*\|")
FENCE = re.compile(r"^\s*```")
# The record's own sub-block marker: a line opening an amendment, a preserved former wording or a
# declined-alternatives record inside a principle that carries no blank line from end to end.
STAR_MARKER = re.compile(r"^\s*(\*\*)?★")


class Stop(Exception):
    """A demand of the decomposition is unmet. Never a warning, never a span dropped."""


def spans_of(text: str) -> tuple[list[dict], int]:
    """The file, cut into spans by the rule the module docstring states.

    Returns the spans and the characters of the blank lines BETWEEN them — separately, because a
    blank line INSIDE a fenced block belongs to that span and counting it twice would make the
    reconciliation below pass while a span was missing.
    """
    lines = text.splitlines(keepends=True)
    out: list[dict] = []
    skipped = 0
    i, n = 0, len(lines)
    while i < n:
        if not lines[i].strip():
            skipped += len(lines[i])
            i += 1
            continue
        start = i
        if FENCE.match(lines[i]):
            i += 1
            while i < n and not FENCE.match(lines[i]):
                i += 1
            if i < n:
                i += 1
            out.append({"first_line": start + 1, "last_line": i,
                        "text": "".join(lines[start:i]), "kind": "fenced-block"})
            continue
        if TABLE_ROW.match(lines[i]):
            out.append({"first_line": i + 1, "last_line": i + 1,
                        "text": lines[i], "kind": "table-row"})
            i += 1
            continue
        i += 1
        while i < n and lines[i].strip() and not FENCE.match(lines[i]) \
                and not TABLE_ROW.match(lines[i]) and not STAR_MARKER.match(lines[i]):
            i += 1
        kind = "star-marked sub-block" if STAR_MARKER.match(lines[start]) else "block"
        out.append({"first_line": start + 1, "last_line": i,
                    "text": "".join(lines[start:i]), "kind": kind})
    return out, skipped


def first_match(text: str, patterns) -> str | None:
    for pattern in patterns:
        found = re.search(pattern, text)
        if found:
            return found.group(0)
    return None


def classify(span: dict, filename: str) -> tuple[str, dict, bool]:
    text = span["text"]

    if filename == "OPEN_ITEMS.md" and span["kind"] == "table-row" \
            and lint.ROW.match(text.strip()):
        cells = lint.split_row(text.strip())
        if len(cells) == lint.CELLS_PER_ROW:
            token = lint.leading_token(cells[4])
            if token == lint.RESOLVED_AT_HEAD:
                return RESOLVED_ROW, {
                    "the_row": cells[0],
                    "its_status_cell_opens_with": token,
                    "read_by": "tools/audit/index_status_lint.py — the ONE index parser, imported "
                               "rather than re-implemented (#6)",
                }, False

    # The pointer test comes FIRST for STATUS.md. A dated entry recording a completed batch is
    # that batch's entry whatever else it mentions, and a former wording it happens to quote is
    # inside it rather than instead of it. Ordered the other way, an entry would be classed by a
    # phrase it merely contains — which is the same confusion the recognizers avoid elsewhere by
    # matching only what a span says about ITSELF.
    hit = first_match(text, POINTER_MARKERS)
    if hit and filename == "STATUS.md":
        return POINTER, {"the_marker_matched": hit}, False
    hit = first_match(text, FORMER_WORDING_MARKERS)
    if hit:
        return FORMER_WORDING, {"the_marker_matched": hit}, False
    hit = first_match(text, HISTORICAL_MARKERS)
    if hit:
        return HISTORICAL, {"the_marker_matched": hit}, False
    hit = first_match(text, DEFENSE_MARKERS)
    if hit:
        return DEFENSE, {"the_marker_matched": hit}, False
    return OPERATIVE, {"no_recognizer_placed_it": True}, True


def measure(filename: str) -> dict:
    path = ROOT / filename
    if not path.is_file():
        raise Stop(f"a file the ruling names for the measurement is missing: {filename}")
    text = path.read_text(encoding="utf-8")
    total_characters = len(text)

    rows, by_class, doubt_characters = [], {}, 0
    covered = 0
    all_spans, blank = spans_of(text)
    for span in all_spans:
        category, evidence, defaulted = classify(span, filename)
        size = len(span["text"])
        covered += size
        by_class.setdefault(category, {"spans": 0, "characters": 0})
        by_class[category]["spans"] += 1
        by_class[category]["characters"] += size
        if defaulted:
            doubt_characters += size
        rows.append({
            "first_line": span["first_line"], "last_line": span["last_line"],
            "kind": span["kind"], "characters": size,
            "the_class": category, "the_evidence": evidence,
            "placed_by_the_doubt_default": defaulted,
            "the_opening": " ".join(span["text"].split())[:160],
        })

    if covered + blank != total_characters:
        raise Stop(f"{filename}: the spans and the blank lines account for {covered + blank} "
                   f"characters against a file of {total_characters} — a span has been dropped "
                   f"from the decomposition, which would make every count here meaningless")

    return {
        "file": filename,
        "characters": total_characters,
        "lines": len(text.splitlines()),
        "spans": len(rows),
        "characters_in_the_blank_lines_between_spans": blank,
        "by_class": {c: by_class.get(c, {"spans": 0, "characters": 0}) for c in CLASSES},
        "characters_placed_by_the_doubt_default": doubt_characters,
        "★_what_the_doubt_default_share_means":
            "the part of this file that no recognizer placed, and which therefore falls to "
            "`operative-rule-text` because the ruled default is that a span the test cannot place "
            "STAYS AT SITE. It is not a claim that this share is operative.",
        "the_spans": rows,
    }


def build() -> dict:
    per_file = [measure(name) for name in FILES]
    return {
        "what_this_is":
            "THE FIVE MANDATORY-READ FILES, DECOMPOSED SPAN BY SPAN AND CLASSED, with byte counts "
            "per class per file. A MEASUREMENT ONLY: no governing file is edited, no fate is "
            "decided, and nothing is moved. It is the first of the two artifacts the ruled "
            "read-only pruning batch delivers.",
        "generator": "tools/audit/gen_governing_surface_spans.py",
        "dispatch": "cc_instruction_preparation_fifth.md, Task 2",
        "the_ruling_that_ordered_it": {
            "source": "cowork_rulings_2026_08_16_preparation_return.md §5(A)",
            "the_ordered_batch_quoted":
                "The next batch after the fourth is READ-ONLY: a per-file decomposition by span "
                "(operative rule text; preserved former wordings; defenses and "
                "declined-alternatives records; self-declared historical or superseded blocks; "
                "resolved rows) and the reader/anchor/quote inventory over all five files, "
                "delivering a ratification surface with per-span fates.",
            "the_doubt_default_quoted":
                "THE DOUBT DEFAULT: a span the test cannot place STAYS AT SITE — a wrongly "
                "archived operative span fails silently (a rule misapplied, nothing flags it) "
                "while wrongly kept noise fails visibly and cheaply, and staying is the "
                "recoverable direction.",
        },
        "the_span_rule": {
            "a_block": "a maximal run of consecutive non-blank lines",
            "a_fenced_code_block": "ONE span whatever blank lines it contains",
            "a_table_row": "its own span, so the ruled `resolved row` class can be measured at all",
            "a_star_marked_sub_block":
                "a block is cut again at every line opening with the record's own ★ marker, "
                "because a principle of CLAUDE.md carries no blank line from end to end and one "
                "marker inside it would otherwise class the whole live rule as archive material",
        },
        "the_recognizers_AUTHORED_and_published_here": {
            HISTORICAL: list(HISTORICAL_MARKERS),
            FORMER_WORDING: list(FORMER_WORDING_MARKERS),
            DEFENSE: list(DEFENSE_MARKERS),
            POINTER: list(POINTER_MARKERS),
            RESOLVED_ROW: "the resolved mark at the head of the status cell, read by "
                          "tools/audit/index_status_lint.py",
        },
        "★_what_this_measurement_does_NOT_establish":
            "That a span classed `operative-rule-text` IS operative — only that no recognizer "
            "placed it elsewhere. The recognizers' reach is UNMEASURED (#19), and the direction "
            "of their error is the recoverable one: a missed marker keeps a span at site, which "
            "is the ruled default.",
        "the_totals": {
            "files": len(per_file),
            "characters": sum(f["characters"] for f in per_file),
            "spans": sum(f["spans"] for f in per_file),
            "characters_by_class": {
                c: sum(f["by_class"][c]["characters"] for f in per_file) for c in CLASSES},
            "spans_by_class": {
                c: sum(f["by_class"][c]["spans"] for f in per_file) for c in CLASSES},
            "characters_placed_by_the_doubt_default":
                sum(f["characters_placed_by_the_doubt_default"] for f in per_file),
        },
        "per_file": per_file,
    }


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="re-derive the decomposition and report whether the artifact matches")
    args = ap.parse_args(argv)

    text = json.dumps(build(), indent=1, ensure_ascii=False) + "\n"
    if args.check:
        have = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if have != text:
            print("STALE: the governing-surface span decomposition does not re-derive")
            return 1
        print("the governing-surface span decomposition re-derives")
        return 0

    OUT.write_text(text, encoding="utf-8", newline="")
    data = json.loads(text)
    print("wrote", OUT.relative_to(ROOT).as_posix())
    for f in data["per_file"]:
        print(f"  {f['file']:<20} {f['characters']:>8,} characters, {f['spans']:>5} spans, "
              f"{f['characters_placed_by_the_doubt_default']:>8,} by the doubt default")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except Stop as exc:
        print(f"STOP: {exc}")
        raise SystemExit(2)
