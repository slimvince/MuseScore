#!/usr/bin/env python3
"""THE PRUNE-AT-AMENDMENT BACKLOG IN `CLAUDE.md` — every candidate read before it moves.

THE ORDER THIS EXISTS FOR.  The user, 2026-09-07, in his own words: *"1. tidy the mess that was
caused by this rule not being followed. 2. make sure this rule is being followed from now on."*
The rule is §5(D) of `cowork_rulings_2026_08_16_preparation_return.md`, the CONTINUOUS-PRUNING
rule, quoted to its own sentence ends (D-643):

    "From this ruling, any edit to a governing document that supersedes, amends or closes some
     part of it MOVES the newly superseded text, in the SAME act, to its archive home — verbatim,
     with the move recorded, on the established archive pattern. The site keeps a compact, dated
     supersession pointer naming where the former text now lives, so the supersession stays
     visible where it happened."

    "This SUPERSEDES the preserve-in-place default for governing-document amendments (the pattern
     principles #8's and #10's own amendments used, and which the D-231 rephrasing was ruled
     under — 'the former wording preserved in place')."

This file is half one of that order.  Half two is `tools/audit/prune_at_amendment_lint.py`, which
IMPORTS this file's recognizer rather than carrying a second copy of it (#6).

★ WHY A FOURTH TOOL RATHER THAN A RE-AIMING OF A THIRD.  Three archiving acts over these files are
already on the record — the executed split, the pre-convention residue move, and the post-split
pass — and each is PINNED at its own commit with its reading verdicts keyed to that pin.  A
re-aiming would leave each act's `--check` proving something about a file it was not performed on,
and two archive pointers in `STATUS.md` cite such a check BY NAME.  So a later wave is a new tool
on the established construction, which is the shape `gen_status_residue_move.py` and
`gen_post_split_archive.py` already set.

WHAT IS DERIVED AND WHAT IS AUTHORED.

  DERIVED   the span population at this act's pin, cut and classed IN PROCESS — the cut and the
            classifier imported from `gen_claude_md_finer_spans`, the pointer constraint with
            them; the spans this file's own PRESERVE-IN-PLACE recognizer adds; the six spans the
            seventh- and eighth-return sittings settled, taken from the committed record of those
            acts; every span's text, from the git OBJECT at the pin; every count.
  AUTHORED  the two commits this act reads and writes at, the recognizer's phrasings — derived
            from what the five governing files actually say and published on this file's face —
            and ONE READING VERDICT PER CANDIDATE, which is the read-before-move safeguard and the
            whole reason this is not a bulk move.

★ WHY THE FINER CUT AND NOT THE COARSE ONE.  The coarse cut is the unit the first wave measured
`CLAUDE.md` at, and the record then MEASURED it wrong for this file: finding F33, where 15,395
characters of live governing rule text were placed in an archive class by two sentences that
merely point at former wordings held elsewhere.  Ruling 4 of `cowork_rulings_2026_08_17_sixth_return.md`
commissioned the finer cut as the answer, and it is `CLAUDE.md`'s own ruled unit.  This act uses
it.  The coarse decomposition is re-taken at this act's pin as well, published at
`governing_surface_spans_2026_09_07.json`, and every one of its `CLAUDE.md` archive-class spans is
accounted for below — so the two units are reconciled rather than one being quietly preferred.

THE READING TEST, IMPORTED FROM THE EXECUTED SPLIT RATHER THAN RESTATED (#6):

  (1) CLASS FIDELITY — the span, read whole, IS a record of the kind its class names.  A span that
      merely POINTS AT such material preserved elsewhere fails this half.
  (2) NO LIVE REMAINDER — no part of the span states a rule, a STOP condition, a live caveat or a
      prohibition that a working session acts on today.

Anything else stays: the ruled DOUBT DEFAULT (§5(E)), whose recorded ground is the asymmetry — a
wrongly archived operative span fails SILENTLY while wrongly kept noise fails visibly and cheaply,
and staying is the recoverable direction.

THE STOPS — each one a way this act could go wrong silently:
  * a candidate with no authored reading verdict halts it, so no span moves unread;
  * an authored verdict naming a span the derivation does not carry halts it;
  * a MOVE span not byte-present exactly once in the base blob halts it;
  * a MOVE span already present in the companion halts it — the move has run;
  * the subject file differing between the measurement pin and the base commit halts it, so the
    reading and the act cannot be about two different files;
  * a coarse archive-class span this act's reconciliation cannot account for halts it, so the two
    units cannot quietly disagree about what the file holds.

Run:
    python tools/audit/gen_claude_md_prune_backlog.py --apply   # perform the ruled moves once
    python tools/audit/gen_claude_md_prune_backlog.py --check   # re-derive the reconciliation
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

sys.path.insert(0, HERE)
from output_encoding import use_utf8_output              # noqa: E402  (path set above)
import gen_governing_surface_spans as coarse             # noqa: E402  the classes (#6)
import gen_claude_md_finer_spans as finer                # noqa: E402  the cut and the classifier
import gen_claude_md_finer_archive as ruled_spans        # noqa: E402  the six settled spans
from gen_governing_surface_split import pointer_text     # noqa: E402  the ONE pointer shape (#6)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

OUT = os.path.join(HERE, "claude_md_prune_backlog.json")
FRESH_COARSE = os.path.join(HERE, "governing_surface_spans_2026_09_07.json")

PARENT = "CLAUDE.md"
COMPANION = "CLAUDE_ARCHIVE.md"

# The commit this act READS the subject file at: Task 0 of the executing dispatch. It is also the
# commit the fresh coarse decomposition beside this act was measured at, so the two units describe
# one file rather than two.
PIN = "d125281a43192f23a65711199b3ccc27f7f07356"
PIN_IS = ("Task 0 of `cc_instruction_claude_md_prune_at_amendment_2026_09_07.md`, pushed before "
          "any of this batch's reading began")

# The commit this act's moves are performed ON TOP OF: Task 1 of the same dispatch, pushed before
# this task began. Task 1 does not touch the subject file, and that is CHECKED rather than assumed.
BASE_COMMIT = "87b830889d5471ea067be395de72a2ec28b5dad3"

ACT_DATE = "2026-09-07"
DISPATCH = "cc_instruction_claude_md_prune_at_amendment_2026_09_07.md"
RULE_D = "cowork_rulings_2026_08_16_preparation_return.md §5(D)"

MOVE = "MOVE"
STAY = "STAYS AT SITE — flagged by the reading (A3)"

# ── AUTHORED — the PRESERVE-IN-PLACE recognizer, and where its phrasings come from ─────────────
# ★ DERIVED FROM WHAT THE RECORD ACTUALLY SAYS, NEVER INVENTED. Every pattern below was taken by
# searching the five governing files at this act's pin for the shape rule (D) supersedes — a span
# saying that ITS OWN former wording is kept where it stands rather than moved to an archive with a
# pointer left behind. The phrasings the search returned are the ones the record uses; nothing was
# added on the strength of what a document might say.
#
# ★ WHAT THIS RECOGNIZER IS FOR, AND WHAT IT IS NOT FOR. Rule (D) does not forbid recording a
# supersession; it fixes HOW one is recorded — the text moves, a compact dated pointer stays. So
# this recognizer looks for the SUPERSEDED PATTERN and not for supersession itself. A span that
# says where a former wording NOW LIVES is rule (D) working, and is not matched here.
PRESERVE_IN_PLACE_MARKERS = (
    r"(?i)\bpreserved in place\b",
    r"(?i)\bstands? in place\b",
    r"(?i)\bpreserved under #12\b",
    r"(?i)\bformer text, preserved\b",
)

# The date a preserve-in-place statement carries, used by the lint that imports this module to tell
# a pre-rule backlog entry from a breach of a rule that was already in force. Any ISO date in the
# span; the EARLIEST is taken, because an amendment record states its own date first and a later
# date inside it belongs to something the record mentions.
A_DATE = re.compile(r"\b(20\d\d)-(\d\d)-(\d\d)\b")

# The date rule (D) was ruled. A preserve-in-place statement dated at or before it was lawful when
# it was written; one dated after it is not. The date is the ruling record's own.
RULE_D_RULED_ON = "2026-08-16"

READING_TEST = (
    "A span MOVES only when (1) it IS, read whole, a record of the kind its class names — a span "
    "that merely POINTS AT such material preserved elsewhere fails this half — and (2) no part of "
    "it states a rule, a STOP condition, a live caveat or a prohibition that a working session "
    "acts on today. Anything else stays: the ruled doubt default (§5(E) of "
    "`cowork_rulings_2026_08_16_preparation_return.md`), whose recorded ground is that a wrongly "
    "archived operative span fails silently while wrongly kept noise fails visibly and cheaply. "
    "The test is IMPORTED from the executed split, which is the discipline every archiving act on "
    "these files has run under."
)


class Stop(Exception):
    """A demand of the ordered act is unmet. Never a warning, never a span moved unread."""


def git_show(rev: str, path: str) -> str:
    proc = subprocess.run(["git", "-C", ROOT, "show", f"{rev}:{path}"],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        raise Stop(f"git show {rev[:10]}:{path} failed — "
                   f"{proc.stderr.decode('utf-8', 'replace').strip()}")
    return proc.stdout.decode("utf-8")


def read(path: str) -> str:
    with open(os.path.join(ROOT, path), "r", encoding="utf-8", newline="") as fh:
        return fh.read()


def write(path: str, text: str) -> None:
    with open(os.path.join(ROOT, path), "w", encoding="utf-8", newline="") as fh:
        fh.write(text)


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def line_form(live: str, text: str) -> str:
    """`text`, as the git object gives it (LF), in the LIVE file's own line-ending form.

    The caveat this answers was MEASURED by the post-split pass and is imported as a practice
    rather than rediscovered: these files are stored with carriage-return line endings where their
    committed blobs have none, so a byte comparison between a span from the git object and the same
    span in the working tree reports ABSENT for a span that is present.
    """
    return text.replace("\n", "\r\n") if "\r\n" in live else text


def preserve_in_place_hits(text: str) -> list[re.Match]:
    """Every preserve-in-place marker in a span that is NOT inside an archive pointer line.

    The pointer exclusion is the STANDING CONSTRAINT ruled at Ruling 1 of
    `cowork_rulings_2026_08_17_eighth_return.md` — a span whose archive classification derives from
    text inside an archive pointer is NOT archivable, wherever in the span the pointer sits. A
    pointer QUOTES the opening of what it points at, so without this a pointer to an archived
    preserved wording would place the span that carries the pointer.
    """
    regions = finer.archive_pointer_regions(text)
    out = []
    for pattern in PRESERVE_IN_PLACE_MARKERS:
        for found in re.finditer(pattern, text):
            if not finer.inside_a_pointer(found.start(), regions):
                out.append(found)
    return sorted(out, key=lambda m: m.start())


def statement_date(text: str) -> str | None:
    """The earliest ISO date the span carries, or None."""
    dates = sorted(m.group(0) for m in A_DATE.finditer(text))
    return dates[0] if dates else None


# ── AUTHORED — one reading verdict per candidate (the read-before-move safeguard) ──────────────
# Keyed by (first_line, last_line) AT THIS ACT'S PIN. Every one was read in `CLAUDE.md` itself with
# the file tools, whole, never from the artifact's 160-character opening — which is the whole
# reason the safeguard exists.
VERDICTS: dict[tuple[int, int], tuple[str, str]] = {
    (1603, 1631): (
        STAY,
        "★ FAILS TEST (1) AND TEST (2), AND TEST (2) COMPREHENSIVELY. Read whole, the span is two "
        "things and the first of them is live. Lines 1603-1624 are the SUPERSESSION STATEMENT "
        "itself: they state the governing structure — six phases, preparation through the audit, "
        "with the fix plan after it unchanged — they state the rule that replaced the truth half, "
        "in words that say of themselves that it \"must bind even a session that reads nothing "
        "else\", they impose the per-phase recorded retrospective, they fix the standing of every "
        "embedded sub-ruling one by one, and they fix how the abbreviation HEAD is read in the "
        "text below. A working session acts on all five. Lines 1625-1631 are the opening of the "
        "preserved former three-phase text, which IS archive material. ★ SO THE SPAN IS A LIVE "
        "STATEMENT THAT CARRIES THE OPENING OF A PRESERVED ONE, which fails test (1) — it is not "
        "a record of the kind its class names — and archiving it would delete the governing "
        "structure from the file. ★ WHAT WOULD BE NEEDED TO REACH THE PRESERVED HALF, stated "
        "rather than attempted: a cut that separates a preserved wording from the live statement "
        "announcing it. This act does not take it. The record's two span units were each "
        "commissioned by a ruling with measured evidence behind it, and inventing a third to "
        "reach one span is the stretched judgment the ruled doubt default exists to prevent."),
    (1720, 1749): (
        STAY,
        "★ FAILS TEST (1) AND TEST (2), on the same shape as the span above and with a smaller "
        "live half. Read whole, lines 1720-1733 are the LIVE ratification note — `cowork_oi200_"
        "perspective_inventory.md` §4 named as the ONE home for the enumerated discovery "
        "channels, and which of its channels the phase-2 clause reaches — and its second half is "
        "the operative one: **what the ratification did NOT do**. That the inventory's §6 program "
        "is not adopted, that [[OI-200]] is not pulled forward, that the document's §9 request "
        "stays open and untaken, that no probe, fix, design or inference change is authorized, "
        "and that phase 1 is not complete. A session reading this clause acts on every one of "
        "those. Lines 1734-1749 are the preserved former text of the same note, marked as such in "
        "its own opening words, and they ARE archive material under §5(E)'s own naming. ★ THE "
        "SPAN IS THEREFORE MIXED, fails test (1) as a whole, and stays — the same conclusion and "
        "the same missing cut as the span above. ★ WHAT IS NOT CLAIMED: that the preserved half "
        "is unarchivable. What is claimed is what test (1) asks — read WHOLE, this span is not a "
        "preserved former wording."),
}


def candidates() -> tuple[list[dict], dict]:
    """Every span the ruled test places, after the ruled exclusions. DERIVED, never listed."""
    if git_show(PIN, PARENT) != git_show(BASE_COMMIT, PARENT):
        raise Stop(f"{PARENT} differs between the measurement pin {PIN[:10]} and the base commit "
                   f"{BASE_COMMIT[:10]} — the reading and the act would be about two different "
                   f"files")

    text = git_show(PIN, PARENT)
    lines = text.splitlines(keepends=True)
    spans, _blank = finer.spans_of(text)

    settled = [s["_text"] for s in
               ruled_spans.with_text(sum(ruled_spans.ruled_population(), []))]

    rows, excluded = [], {"settled_at_the_two_return_sittings": 0,
                          "an_archive_pointer_left_by_a_previous_act": 0}
    for span in spans:
        body = span["text"]
        shape = finer.shape_of(body)
        category, evidence, defaulted = finer.classify(body, shape)
        in_place = preserve_in_place_hits(body)

        placed_by = None
        if category != coarse.OPERATIVE:
            placed_by = "the ruled archive classes, at the finer pass's own classifier"
        elif in_place:
            placed_by = ("this act's PRESERVE-IN-PLACE recognizer — the pattern rule (D) "
                         "supersedes, which no earlier recognizer looks for")
            category = coarse.FORMER_WORDING
            evidence = {"the_marker_matched": in_place[0].group(0),
                        "markers_found_outside_every_archive_pointer": len(in_place)}
        if placed_by is None:
            continue

        if finer.ARCHIVE_POINTER.match(body):
            excluded["an_archive_pointer_left_by_a_previous_act"] += 1
            continue
        # Containment BOTH WAYS: the settled spans were cut at a different pin, so a settled span
        # can sit inside a span of this act's cut, and proposing the container IS re-proposing it.
        if any(s in body or body in s for s in settled):
            excluded["settled_at_the_two_return_sittings"] += 1
            continue

        recomputed = "".join(lines[span["first_line"] - 1:span["last_line"]])
        if recomputed != body:
            raise Stop(f"{PARENT} lines {span['first_line']}-{span['last_line']}: the span's "
                       f"coordinates do not reproduce its own text")
        rows.append({
            "first_line_at_the_pin": span["first_line"],
            "last_line_at_the_pin": span["last_line"],
            "kind": span["kind"],
            "characters": len(body),
            "the_class": category,
            "how_it_was_placed": placed_by,
            "the_evidence": evidence,
            "the_date_the_span_carries": statement_date(body),
            "the_opening": " ".join(body.split())[:160],
            "_text": body,
        })

    keys = {(r["first_line_at_the_pin"], r["last_line_at_the_pin"]) for r in rows}
    unverdicted = sorted(k for k in keys if k not in VERDICTS)
    if unverdicted:
        detail = "\n".join(
            f"    {r['first_line_at_the_pin']}-{r['last_line_at_the_pin']} [{r['the_class']}] "
            f"{r['how_it_was_placed']}\n      {r['the_opening']}"
            for r in rows
            if (r["first_line_at_the_pin"], r["last_line_at_the_pin"]) in unverdicted)
        raise Stop("candidate(s) with no authored reading verdict — this act is bound to the "
                   "read-before-move safeguard, so an unread candidate halts it:\n" + detail)
    stray = sorted(k for k in VERDICTS if k not in keys)
    if stray:
        raise Stop(f"authored verdict(s) naming a span the derivation does not carry: {stray} — "
                   f"the verdicts and the measurement have drifted apart")

    for rec in rows:
        verdict, why = VERDICTS[(rec["first_line_at_the_pin"], rec["last_line_at_the_pin"])]
        rec["the_verdict"] = verdict
        rec["why"] = why
        rec["how_the_verdict_was_made"] = "authored per span, read in the file itself"
        rec["text_sha256"] = sha(rec["_text"])
    return rows, excluded


def coarse_reconciliation(rows: list[dict]) -> dict:
    """Every `CLAUDE.md` archive-class span of the FRESH COARSE decomposition, accounted for.

    The two units cut differently, so this does not compare coordinates: each coarse span is placed
    against this act's own population by TEXT containment, and one that lands nowhere STOPS the
    run. Without it the finer unit could quietly drop something the coarse unit sees.
    """
    if not os.path.exists(FRESH_COARSE):
        raise Stop(f"the fresh coarse decomposition is missing: "
                   f"{os.path.relpath(FRESH_COARSE, ROOT)} — the two units cannot be reconciled")
    with open(FRESH_COARSE, encoding="utf-8") as fh:
        data = json.load(fh)
    if data.get("measured_at_commit") != PIN:
        raise Stop(f"the fresh coarse decomposition is measured at "
                   f"{data.get('measured_at_commit')} where this act reads at {PIN} — the two "
                   f"units would describe different files")
    per_file = next(f for f in data["per_file"] if f["file"] == PARENT)
    text = git_show(PIN, PARENT)
    lines = text.splitlines(keepends=True)
    settled = [s["_text"] for s in
               ruled_spans.with_text(sum(ruled_spans.ruled_population(), []))]

    placed = []
    for span in per_file["the_spans"]:
        if span["the_class"] == coarse.OPERATIVE:
            continue
        body = "".join(lines[span["first_line"] - 1:span["last_line"]])
        where = None
        if finer.ARCHIVE_POINTER.match(body):
            where = ("an archive pointer left by a previous act — the standing pointer constraint "
                     "keeps it at site, and the finer classifier places it there positively")
        elif any(s in body or body in s for s in settled):
            where = "settled at the seventh- or eighth-return sitting; re-proposing it is forbidden"
        elif any(r["_text"] in body or body in r["_text"] for r in rows):
            where = "carried by this act's own population, at the finer cut"
        else:
            regions = finer.archive_pointer_regions(body)
            marker = (span.get("the_evidence") or {}).get("the_marker_matched")
            at = body.find(marker) if marker else -1
            if at >= 0 and finer.inside_a_pointer(at, regions):
                where = ("classified by text INSIDE an archive pointer — the standing constraint "
                         "of 2026-08-17 refuses the placement")
            else:
                shape = finer.shape_of(body)
                cls, _ev, _d = finer.classify(body, shape)
                if cls != coarse.OPERATIVE:
                    where = None
                elif finer.BARE_HEADING.match(body) and len(body.strip().splitlines()) == 1:
                    where = ("a BARE SECTION HEADING, which the finer classifier places "
                             "positively at site: archiving it would move the heading while its "
                             "section body stayed")
                else:
                    where = ("the finer classifier does not place it in an archive class — at the "
                             "finer cut the span carries no admissible marker, which is finding "
                             "F33's answer working")
        if where is None:
            raise Stop(f"{PARENT} coarse lines {span['first_line']}-{span['last_line']} is in an "
                       f"archive class at the coarse cut and this act's reconciliation cannot "
                       f"account for it — the two units disagree about what the file holds")
        placed.append({
            "coarse_first_line": span["first_line"],
            "coarse_last_line": span["last_line"],
            "the_coarse_class": span["the_class"],
            "characters": span["characters"],
            "how_this_act_accounts_for_it": where,
            "the_opening": span["the_opening"],
        })
    return {
        "what_this_is":
            "every span the FRESH COARSE decomposition places in an archive class for this file, "
            "and how this act accounts for it. A span it cannot account for STOPS the run, so the "
            "two units cannot quietly disagree about what the file holds.",
        "coarse_archive_class_spans": len(placed),
        "the_spans": placed,
    }


def plan() -> dict:
    rows, excluded = candidates()
    moved = [r for r in rows if r["the_verdict"] == MOVE]
    stayed = [r for r in rows if r["the_verdict"] != MOVE]

    base = git_show(BASE_COMMIT, PARENT)
    for rec in moved:
        if base.count(rec["_text"]) != 1:
            raise Stop(f"{PARENT} pin lines {rec['first_line_at_the_pin']}-"
                       f"{rec['last_line_at_the_pin']}: the span's text occurs "
                       f"{base.count(rec['_text'])} time(s) in the base blob — a move needs "
                       f"exactly one occurrence")
    order = sorted(moved, key=lambda r: base.index(r["_text"]))

    pointers, by_span, new_parent = [], {}, base
    for rec in order:
        ptr = pointer_text(PARENT, {"first_line": rec["first_line_at_the_pin"],
                                    "last_line": rec["last_line_at_the_pin"],
                                    "the_class": rec["the_class"]}, rec["_text"])
        new_parent = new_parent.replace(rec["_text"], ptr, 1)
        pointers.append(ptr)
        by_span[(rec["first_line_at_the_pin"], rec["last_line_at_the_pin"])] = ptr

    body = ""
    for rec in order:
        body += (f"> **From `{PARENT}` lines {rec['first_line_at_the_pin']}–"
                 f"{rec['last_line_at_the_pin']} at `{PIN[:10]}`, class `{rec['the_class']}`, "
                 f"{rec['characters']} characters.** Moved {ACT_DATE} by `{DISPATCH}` Task 2, "
                 f"under the CONTINUOUS-PRUNING rule ({RULE_D}); "
                 f"{rec['how_the_verdict_was_made']}.\n\n")
        body += rec["_text"]
        if not body.endswith("\n"):
            body += "\n"
        body += "\n"

    moved_characters = sum(r["characters"] for r in order)
    return {
        "rows": rows, "moved": order, "stayed": stayed, "excluded": excluded,
        "pointers": pointers, "pointer_by_span": by_span,
        "new_parent": new_parent, "companion_body": body,
        "base_characters": len(base),
        "characters_moved": moved_characters,
        "characters_kept": len(base) - moved_characters,
    }


def apply_move() -> None:
    p = plan()                       # raises before anything is written
    if not p["moved"]:
        raise Stop("every candidate carries a STAY verdict from the reading, so there is nothing "
                   "to apply. The ruled doubt default makes that outcome lawful, and it is "
                   "REPORTED rather than forced. Run --check to record the reading and prove "
                   "every candidate is still at site.")
    live, archive = read(PARENT), read(COMPANION)
    new_live = live
    for rec in p["moved"]:
        here = line_form(live, rec["_text"])
        if line_form(archive, rec["_text"]) in archive:
            raise Stop(f"a span is already in {COMPANION} — the move has run (pin lines "
                       f"{rec['first_line_at_the_pin']}-{rec['last_line_at_the_pin']})")
        if live.count(here) != 1:
            raise Stop(f"pin lines {rec['first_line_at_the_pin']}-{rec['last_line_at_the_pin']}: "
                       f"the span occurs {live.count(here)} time(s) in the live file — it has "
                       f"changed under the act and the move would not be byte-faithful")
        new_live = new_live.replace(here, line_form(live, p["pointer_by_span"][
            (rec["first_line_at_the_pin"], rec["last_line_at_the_pin"])]), 1)
    # The parent is edited IN ITS OWN LINE-ENDING FORM rather than rewritten from the pinned blob:
    # rewriting would silently re-line-end every line of a governing surface to move one span.
    write(PARENT, new_live)
    write(COMPANION, archive.rstrip("\r\n") + line_form(archive, "\n\n" + p["companion_body"]))


def build() -> dict:
    p = plan()
    live = read(PARENT)
    archive = read(COMPANION) if os.path.exists(os.path.join(ROOT, COMPANION)) else ""
    moved, stayed = p["moved"], p["stayed"]
    return {
        "what_this_is":
            "THE PRUNE-AT-AMENDMENT BACKLOG IN `CLAUDE.md`: every span the ruled archivability "
            "test places at this act's pin — including, for the first time, the spans that say "
            "their OWN former wording is preserved IN PLACE, which is the pattern rule (D) "
            "supersedes and which no earlier recognizer looks for — READ WHOLE before anything "
            "moves, with the mechanical proof of where each one stands. Every figure here is "
            "computed; none is transcribed (D-431).",
        "generated_by": "tools/audit/gen_claude_md_prune_backlog.py",
        "dispatch": f"{DISPATCH}, Task 2",
        "the_order_it_executes":
            "the user, 2026-09-07: \"1. tidy the mess that was caused by this rule not being "
            "followed. 2. make sure this rule is being followed from now on.\" The rule is the "
            f"CONTINUOUS-PRUNING rule, {RULE_D}.",
        "measured_at_commit": PIN,
        "performed_on_top_of_commit": BASE_COMMIT,
        "★_why_the_reading_is_pinned": {
            "what_that_commit_is": PIN_IS,
            "the_reason": "the file is read at a git OBJECT so this act's own writes cannot move "
                          "the measurement under it, and the subject file is proven byte-identical "
                          "between the pin and the base commit rather than assumed to be.",
        },
        "the_reading_test_applied": READING_TEST,
        "★_the_recognizer_this_act_adds": {
            "what_it_looks_for": "a span saying that ITS OWN former wording is kept where it "
                                 "stands — the preserve-in-place pattern rule (D) supersedes.",
            "the_phrasings": list(PRESERVE_IN_PLACE_MARKERS),
            "where_they_come_from": "a search of the five governing files at this act's pin for "
                                    "the shape rule (D) supersedes. They are the phrasings the "
                                    "record uses; none was added on the strength of what a "
                                    "document might say.",
            "★_what_it_deliberately_does_NOT_match":
                "a span recording a supersession as a POINTER to where the former text now lives. "
                "That is rule (D) working, not a breach of it — the rule fixes HOW a supersession "
                "is recorded, and does not forbid recording one.",
            "the_standing_pointer_constraint_applies_to_it": finer.POINTER_CONSTRAINT,
            "the_date_rule_D_was_ruled": RULE_D_RULED_ON,
        },
        "★_what_is_imported_rather_than_re_decided_(#6)": {
            "the_span_cut_the_classifier_and_the_pointer_constraint":
                "gen_claude_md_finer_spans.py — `CLAUDE.md`'s own ruled unit",
            "the_ruled_classes": "gen_governing_surface_spans.py",
            "the_compact_dated_pointer_shape": "gen_governing_surface_split.py",
            "the_six_settled_spans": "gen_claude_md_finer_archive.py, its own ruled population "
                                     "read at its own pin",
        },
        "the_exclusions_taken_before_any_reading": p["excluded"],
        "the_totals": {
            "candidates": len(p["rows"]),
            "spans_moved": len(moved),
            "spans_left_at_site_by_the_reading": len(stayed),
            "characters_moved": p["characters_moved"],
            "characters_left_at_site_by_the_reading": sum(r["characters"] for r in stayed),
            "base_characters": p["base_characters"],
            "moved_plus_kept_accounts_for_the_base_blob_to_the_character":
                p["characters_moved"] + p["characters_kept"] == p["base_characters"],
        },
        "the_moved": [{k: v for k, v in r.items() if k != "_text"} for r in moved],
        "the_left_at_site_by_the_reading":
            [{k: v for k, v in r.items() if k != "_text"} for r in stayed],
        "reconciliation": {
            "every_moved_span_is_byte_present_in_the_companion_exactly_once":
                all(archive.count(line_form(archive, r["_text"])) == 1 for r in moved),
            "every_moved_span_is_absent_from_the_parent":
                all(line_form(live, r["_text"]) not in live for r in moved),
            "every_span_the_reading_flagged_is_still_present_at_site_exactly_once":
                all(live.count(line_form(live, r["_text"])) == 1 for r in stayed),
            "no_span_the_reading_flagged_is_in_the_companion":
                all(line_form(archive, r["_text"]) not in archive for r in stayed),
            "the_base_blob_sha256": sha(git_show(BASE_COMMIT, PARENT)),
            "★_which_direction_carries_the_weight_here":
                "the third and fourth. Where the reading keeps most or all of its candidates, a "
                "check that only proved the moves would be green at a tree where a refusal had "
                "been overridden — so what is asserted hardest is that every flagged span is "
                "still exactly where the reading left it.",
            "★_the_line_ending_form_was_normalised_before_any_of_these_decided": True,
        },
        "the_coarse_unit_reconciled": coarse_reconciliation(p["rows"]),
        "★_what_this_act_does_NOT_do": [
            "It changes no rule `CLAUDE.md` states: a span that states a live rule, its bounding "
            "purpose, a live caveat or a STOP stays at site, and doubt keeps a span at site.",
            "It does not touch the pinned first-wave decomposition or the first wave's tool, so "
            "the two archive pointers citing that tool's --check go on proving what they say.",
            "It prunes no governing document other than `CLAUDE.md`.",
            "It creates, flips or discards NO open-items row.",
            "It re-proposes none of the six spans the two return sittings settled.",
        ],
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--apply", action="store_true", help="perform the ruled moves (once)")
    g.add_argument("--check", action="store_true", help="re-derive the reconciliation")
    args = ap.parse_args()

    if args.apply:
        apply_move()

    art = build()
    text = json.dumps(art, indent=1, ensure_ascii=False) + "\n"

    if args.check:
        try:
            with open(OUT, "r", encoding="utf-8") as fh:
                committed = fh.read()
        except FileNotFoundError:
            print(f"FAIL: {os.path.relpath(OUT, ROOT)} does not exist")
            return 1
        if committed != text:
            print(f"FAIL: the prune-at-amendment backlog record does not re-derive: "
                  f"{os.path.relpath(OUT, ROOT)}")
            return 1
    else:
        with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        print("wrote", os.path.relpath(OUT, ROOT))

    t = art["the_totals"]
    print(f"  candidates {t['candidates']}, moved {t['spans_moved']}, "
          f"left at site by the reading {t['spans_left_at_site_by_the_reading']}")
    print(f"  characters moved: {t['characters_moved']:,}")
    r = art["reconciliation"]
    print(f"  all four directions: {all(v for v in r.values() if isinstance(v, bool))}")
    print(f"  coarse archive-class spans accounted for: "
          f"{art['the_coarse_unit_reconciled']['coarse_archive_class_spans']}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Stop as exc:
        print("STOP:", exc)
        raise SystemExit(2)
