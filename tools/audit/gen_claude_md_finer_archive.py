#!/usr/bin/env python3
"""THE TWO RULED `CLAUDE.md` SPANS — read before they move, and the reading published.

THE RULING THIS EXISTS FOR.  User, 2026-08-17, Ruling 1 of
`cowork_rulings_2026_08_17_seventh_return.md`: *"Two spans ARCHIVE, with a dated pointer at each
site; the four contested proposals are REFUSED and their spans STAY AT SITE ... the executing act
derives them from `tools/audit/claude_md_finer_spans.json` at the surface's own commit
`cfb69a7ecb`, never retyped ... A span that does not read at execution time as this ruling assumes
is a STOP-and-report, never a forced move."*

★ WHAT THE SAFEGUARD IS FOR, AND WHY IT IS NOT DECORATION.  The ruling binds this act to the same
read-before-move safeguard the executed split ran under, and it says in its own words what happens
when a span fails it: the span stays, and the batch reports.  So the safeguard is a real gate with
a real refusal path, not a formality that always returns MOVE.  This run's verdicts are below and
BOTH ARE STAY — the reasons are per span, each with mechanical evidence a reader can re-check.

THE READING TEST, IMPORTED FROM THE SPLIT RATHER THAN RESTATED (#6).  The ruling says the act runs
*"exactly as the split did"*, so the test is `gen_governing_surface_split`'s, in that module's own
words:

  (1) CLASS FIDELITY — the span, read whole, IS a record of the kind its class names.  A span that
      merely POINTS AT such material preserved elsewhere fails this half.
  (2) NO LIVE REMAINDER — no part of the span states a rule, a STOP condition, a live caveat or a
      prohibition that a working session acts on today.

Anything else stays: the ruled doubt default (§5(E) of
`cowork_rulings_2026_08_16_preparation_return.md`), whose own recorded ground is the asymmetry —
a wrongly archived operative span fails SILENTLY while wrongly kept noise fails visibly and
cheaply, and staying is the recoverable direction.

WHAT IS DERIVED AND WHAT IS AUTHORED.

  DERIVED   the archive-class spans of the PINNED finer decomposition — every span the measurement
            places outside `operative-rule-text`.  Nothing about which spans exist is authored.
  DERIVED   which of them the ruling ARCHIVES and which it REFUSES, from the artifact's own
            published conflict evidence and the surface's own conflict-reading rule: a span the A4
            safeguard never read is the uncontested remainder and is ruled to archive; a span the
            safeguard read and kept is ruled to archive only where the safeguard's stated reason
            was that the span OVERRAN into live rule text, which the finer cut answers, and is
            REFUSED where the reason was that the span itself states a rule, which no cut answers.
  DERIVED   every span's TEXT, from the git OBJECT at the pinned commit, matched verbatim in the
            live file.  No span is retyped.
  AUTHORED  the base commit this act is performed on top of, and ONE READING VERDICT PER SPAN the
            ruling archives — assumption A3's safeguard, which is the whole reason this is not a
            bulk move.

THE STOPS — each one a way the act could go wrong silently:
  * the derived archive set or the derived refused set not matching the ruling's own stated shape
    (two archive, four refused) halts it — the derivation and the ruling cannot drift apart;
  * a ruled-to-archive span with no authored reading verdict halts it, so no span moves unread;
  * an authored verdict naming a span the derivation does not carry halts it;
  * a span whose pinned coordinates do not yield the character count the artifact records halts it;
  * a MOVE span not byte-present exactly once in the base blob halts it;
  * a MOVE span already present in the companion halts it — the move has run.

Run:
    python tools/audit/gen_claude_md_finer_archive.py --apply    # perform the ruled move once
    python tools/audit/gen_claude_md_finer_archive.py --check    # re-derive the reconciliation
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

sys.path.insert(0, HERE)
from output_encoding import use_utf8_output              # noqa: E402  (path set above)
import gen_claude_md_finer_spans as finer                # noqa: E402  the pin and the classes (#6)
import gen_governing_surface_spans as coarse            # noqa: E402  the class names (#6)
from gen_governing_surface_split import pointer_text     # noqa: E402  the ONE pointer shape (#6)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

OUT = os.path.join(HERE, "claude_md_finer_archive.json")
SPANS = os.path.join(HERE, "claude_md_finer_spans.json")

PARENT = "CLAUDE.md"
COMPANION = "CLAUDE_ARCHIVE.md"

# The finer decomposition's own pin, imported rather than restated (#6): the ruled spans are that
# measurement's, so a disagreement about WHEN it was taken would make this act a statement about a
# different file.
PINNED_COMMIT = finer.PINNED_COMMIT

# The commit this act is performed on top of: Task 0 of the executing dispatch, pushed before Task 1
# began. An explicit hash, which is the only git read D-253 permits.
BASE_COMMIT = "570f2b63b14ad7bcf09e0014c96d3f1d1aa90fa3"

ACT_DATE = "2026-08-17"
DISPATCH = "cc_instruction_preparation_eighth.md"
RULINGS = "cowork_rulings_2026_08_17_seventh_return.md"

MOVE = "MOVE"
STAY = "STAYS AT SITE — flagged by the reading (A3)"

# The ruling's own shape, checked rather than assumed. Ruling 1: "Two spans ARCHIVE ... the four
# contested proposals are REFUSED and their spans STAY AT SITE."
RULED_TO_ARCHIVE = 2
RULED_REFUSED = 4

# The surface's own conflict-reading rule, quoted from `claude_md_finer_spans.json`'s own
# `★_how_to_read_a_conflict`: "Where the reason was that a span OVERRAN into live rule text, the
# finer cut answers it. Where the reason was that the span ITSELF states a rule, no cut answers it
# and the proposal should be refused." The token below is what the safeguard's own reasons use.
OVERRUN_TOKEN = "OVERRUN"

CONFLICT_KEY = "★_the_A4_safeguard_read_this_span_and_LEFT_IT_AT_SITE"

READING_TEST = (
    "A span MOVES only when (1) it IS, read whole, a record of the kind its class names — a span "
    "that merely POINTS AT such material preserved elsewhere fails this half — and (2) no part of "
    "it states a rule, a STOP condition, a live caveat or a prohibition that a working session "
    "acts on today. Anything else stays: the ruled doubt default (§5(E)), whose recorded ground is "
    "that a wrongly archived operative span fails silently while wrongly kept noise fails visibly "
    "and cheaply. The test is IMPORTED from the executed split, which the ruling names as the "
    "discipline this act runs under."
)


class Stop(Exception):
    """A demand of the ruled act is unmet. Never a warning, never a span moved unread."""


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


# ── AUTHORED — one reading verdict per span the ruling archives (assumption A3) ───────────────
# Keyed by (first_line, last_line) AT THE PINNED COMMIT. Both were read in this session, in
# `CLAUDE.md` itself, with the file tools — never from the artifact's 160-character opening, which
# is the whole reason the safeguard exists.
VERDICTS: dict[tuple[int, int], tuple[str, str]] = {
    (53, 60): (
        STAY,
        "★ FAILS TEST (1) AND TEST (2), and the class itself is an artifact of the recognizer. "
        "READ WHOLE the span is two different things and neither is a declined-alternatives "
        "record. Lines 53-58 are a LIVE supersession statement — `★ WHAT IT SUPERSEDES — A "
        "POINTER, NEVER A COPY (#6)` — telling a session that R3's clause making an apparatus "
        "finding's row mandatory no longer holds for a finding the worth test discards, that R3 is "
        "otherwise untouched, and where R3 lives. A session reading principle #10 acts on that. "
        "Lines 59-60 are TWO ARCHIVE POINTERS left by the executed split, each naming its "
        "companion, its size, its class and the opening of what moved. ★ AND THE TWO POINTERS ARE "
        "WHERE THE CLASS COMES FROM: the only occurrence of `DECLINED` in the span is at offset "
        "637, inside the first pointer, and the only occurrence of `THE COSTS THE USER ACCEPTED` "
        "is at offset 785, inside the second. The span contains no alternative and no cost of its "
        "own. This is finding F41 measured again and NOT covered by the pass's own structural "
        "guard, which fires only when a span BEGINS with a pointer; here the pointers sit at the "
        "span's END and lend their quoted class name and quoted opening to the classifier. "
        "Archiving the span would delete both pointers, removing the only breadcrumbs back to two "
        "spans the split already moved — the exact harm the structural guard was written against."),
    (194, 213): (
        STAY,
        "★ FAILS TEST (2) ON ITS CLOSING SENTENCE, and the failure is at the margin, so the ruled "
        "doubt default decides it rather than a stretched judgment (D-639's fallback shape). Lines "
        "194-211 are what the ruling assumes and are archive material by §5(E)'s own naming: "
        "principle #21's replaced paragraph quoted verbatim, why it was replaced, and the two "
        "declined alternatives. Lines 212-213 are neither — `The errata limb of the contact was "
        "RE-ASKED 2026-08-11 and AWAITS REPLY; clause (a)'s reasonable-wait clock runs from that "
        "date.` That is a LIVE status statement about a running clock, and the rule it qualifies "
        "STAYS AT SITE: clause (a) of the commissioning block in this same principle provides that "
        "SILENCE AFTER A REASONABLE WAIT closes the route by exhaustion, and this sentence is the "
        "only statement in `CLAUDE.md` of when that clock started. The obligation it bears on is "
        "[[OI-179]], which is OPEN and GATES under #19. ★ WHAT IS NOT CLAIMED: that the sentence "
        "is its SOLE carrier — its tracking home is `open_items/OI-179.md` and D-475's verdict, so "
        "#12 would be satisfied by an archive-with-record move. What is claimed is narrower and is "
        "what test (2) asks: one part of the span is live. ★ AND THE COUNTER-EVIDENCE IS RECORDED "
        "RATHER THAN SUPPRESSED: the A4 safeguard's own reading of the coarse span placed exactly "
        "these twenty lines — the closing sentence included — under `principle #21's preserved "
        "former wording runs from line 228 to 247`, and gave the overrun into principles 22-24 as "
        "its ONLY reason to keep. That reading supports the move; this one finds a live remainder "
        "it did not name. Two readings at the file disagree at the margin, which IS the doubt the "
        "default exists for, and the recoverable direction is to stay."),
}


def ruled_population() -> tuple[list[dict], list[dict]]:
    """(ruled_to_archive, refused), DERIVED from the pinned artifact's own published evidence."""
    if not os.path.exists(SPANS):
        raise Stop(f"the finer decomposition is missing: {os.path.relpath(SPANS, ROOT)} — this "
                   f"act's population is derived from it and may not be listed by hand")
    with open(SPANS, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    if data.get("measured_at_commit") != PINNED_COMMIT:
        raise Stop("the finer decomposition's own pin is not the commit this act reads it at — "
                   f"artifact says {data.get('measured_at_commit')}, this tool says "
                   f"{PINNED_COMMIT}")

    archive_class = [s for s in data["the_spans"] if s["the_class"] != coarse.OPERATIVE]

    to_archive, refused = [], []
    for span in archive_class:
        conflict = span.get(CONFLICT_KEY)
        if conflict is None:
            # The uncontested remainder: no reading at the file has refused it.
            span["_why_the_ruling_places_it"] = (
                "the A4 safeguard never read this span, so the ruling archives it as the "
                "uncontested remainder — the only proposal asking the user for something no "
                "reading at the file had already refused")
            to_archive.append(span)
            continue
        reason = conflict["the_safeguards_own_reason"]
        if OVERRUN_TOKEN in reason.upper():
            span["_why_the_ruling_places_it"] = (
                "the A4 safeguard read this span and kept it, and its stated reason was that the "
                "span OVERRAN into live rule text — which the finer cut answers, by the surface's "
                "own conflict-reading rule, so the ruling archives it")
            to_archive.append(span)
        else:
            span["_why_the_ruling_places_it"] = (
                "the A4 safeguard read this span and kept it because the span ITSELF states a "
                "rule, which no cut answers — so the ruling REFUSES the proposal and the span "
                "stays at site")
            refused.append(span)

    if len(to_archive) != RULED_TO_ARCHIVE or len(refused) != RULED_REFUSED:
        raise Stop(f"the derivation places {len(to_archive)} span(s) to archive and "
                   f"{len(refused)} refused, where Ruling 1's own words are two archive and four "
                   f"refused. The derivation and the ruling have drifted apart, which is a "
                   f"STOP rather than an adjustment")

    unverdicted = [(s["first_line"], s["last_line"]) for s in to_archive
                   if (s["first_line"], s["last_line"]) not in VERDICTS]
    if unverdicted:
        raise Stop(f"span(s) with no authored reading verdict: {unverdicted} — Ruling 1 binds this "
                   f"act to READ every span before it moves, so an unread span halts it")
    carried = {(s["first_line"], s["last_line"]) for s in to_archive}
    stray = sorted(k for k in VERDICTS if k not in carried)
    if stray:
        raise Stop(f"authored verdict(s) naming a span the derivation does not carry: {stray} — "
                   f"the verdicts and the measurement have drifted apart")
    return to_archive, refused


def with_text(spans: list[dict]) -> list[dict]:
    """Every span's text, taken from the pinned git OBJECT and checked against the artifact."""
    pinned_lines = git_show(PINNED_COMMIT, PARENT).splitlines(keepends=True)
    out = []
    for span in spans:
        text = "".join(pinned_lines[span["first_line"] - 1:span["last_line"]])
        if len(text) != span["characters"]:
            raise Stop(f"{PARENT} lines {span['first_line']}-{span['last_line']}: the pinned blob "
                       f"yields {len(text)} characters where the artifact records "
                       f"{span['characters']} — the coordinates do not identify the span")
        rec = dict(span)
        rec["_text"] = text
        out.append(rec)
    return out


def plan() -> dict:
    to_archive, refused = ruled_population()
    to_archive = with_text(to_archive)
    refused = with_text(refused)
    base = git_show(BASE_COMMIT, PARENT)

    moved, stayed = [], []
    for span in to_archive:
        verdict, why = VERDICTS[(span["first_line"], span["last_line"])]
        rec = {
            "first_line_at_the_pin": span["first_line"],
            "last_line_at_the_pin": span["last_line"],
            "the_class_the_measurement_gave_it": span["the_class"],
            "characters": span["characters"],
            "why_the_ruling_places_it_here": span["_why_the_ruling_places_it"],
            "the_verdict": verdict,
            "why": why,
            "how_the_verdict_was_made": "authored per span, read in the file itself (A3)",
            "the_opening": span["the_opening"],
            "text_sha256": sha(span["_text"]),
            "_text": span["_text"],
        }
        if verdict == MOVE:
            if base.count(span["_text"]) != 1:
                raise Stop(f"{PARENT} lines {span['first_line']}-{span['last_line']}: the span's "
                           f"text occurs {base.count(span['_text'])} time(s) in the base blob — a "
                           f"move needs exactly one occurrence")
            moved.append(rec)
        else:
            stayed.append(rec)

    refused_recs = [{
        "first_line_at_the_pin": s["first_line"],
        "last_line_at_the_pin": s["last_line"],
        "the_class_the_measurement_gave_it": s["the_class"],
        "characters": s["characters"],
        "why_the_ruling_refused_it": s["_why_the_ruling_places_it"],
        "the_safeguards_own_reason": s[CONFLICT_KEY]["the_safeguards_own_reason"],
        "the_opening": s["the_opening"],
        "text_sha256": sha(s["_text"]),
        "_text": s["_text"],
    } for s in refused]

    order = sorted(moved, key=lambda r: base.index(r["_text"]))
    new_parent = base
    pointers = []
    for rec in order:
        ptr = pointer_text(PARENT, {"first_line": rec["first_line_at_the_pin"],
                                    "last_line": rec["last_line_at_the_pin"],
                                    "the_class": rec["the_class_the_measurement_gave_it"]},
                           rec["_text"])
        new_parent = new_parent.replace(rec["_text"], ptr, 1)
        pointers.append(ptr)

    companion_body = ""
    if order:
        companion_body = (
            f"> **★ THE TWO RULED SPANS OF THE FINER PASS, {ACT_DATE}.** Moved verbatim out of "
            f"`{PARENT}` by `{DISPATCH}` Task 1, executing Ruling 1 of `{RULINGS}` over the "
            f"ratification surface "
            f"`ratification_surfaces/cowork_claude_md_finer_split_2026_08_17.md`. **Each was READ "
            f"WHOLE before it moved** under the same safeguard the executed split ran under, and a "
            f"span that did not read as the ruling assumes stayed at site and was flagged. The "
            f"reconciliation is re-derived by `tools/audit/gen_claude_md_finer_archive.py "
            f"--check`.\n\n")
    for rec in order:
        companion_body += (
            f"> **From `{PARENT}` lines {rec['first_line_at_the_pin']}–"
            f"{rec['last_line_at_the_pin']} at `{BASE_COMMIT[:10]}` (measured at "
            f"`{PINNED_COMMIT[:10]}`), class `{rec['the_class_the_measurement_gave_it']}`, "
            f"{rec['characters']} characters.** Moved {ACT_DATE}; "
            f"{rec['how_the_verdict_was_made']}.\n\n")
        companion_body += rec["_text"]
        if not companion_body.endswith("\n"):
            companion_body += "\n"
        companion_body += "\n"

    moved_characters = sum(r["characters"] for r in order)
    return {
        "moved": order,
        "stayed": stayed,
        "refused": refused_recs,
        "pointers": pointers,
        "new_parent": new_parent,
        "companion_body": companion_body,
        "base_characters": len(base),
        "characters_moved": moved_characters,
        "characters_kept": len(base) - moved_characters,
    }


def apply_move() -> None:
    p = plan()                       # raises before anything is written
    if not p["moved"]:
        raise Stop("BOTH ruled spans carry a STAY verdict from the reading, so there is nothing to "
                   "apply. Ruling 1's own words make that outcome lawful — 'a span that does not "
                   "read at execution time as this ruling assumes is a STOP-and-report, never a "
                   "forced move' — and it is REPORTED rather than forced. Run --check to record "
                   "the reading and prove both spans are still at site.")
    live = read(PARENT)
    archive = read(COMPANION)
    for rec in p["moved"]:
        if rec["_text"] in archive:
            raise Stop(f"a span is already in {COMPANION} — the move has run (pin lines "
                       f"{rec['first_line_at_the_pin']}-{rec['last_line_at_the_pin']})")
        if live.count(rec["_text"]) != 1:
            raise Stop(f"the span at pin lines {rec['first_line_at_the_pin']}-"
                       f"{rec['last_line_at_the_pin']} occurs {live.count(rec['_text'])} time(s) "
                       f"in the live {PARENT} — the file has changed under the act and the move "
                       f"would not be byte-faithful")
    write(PARENT, p["new_parent"])
    write(COMPANION, archive.rstrip("\n") + "\n\n" + p["companion_body"])


def build() -> dict:
    p = plan()
    live = read(PARENT)
    archive = read(COMPANION) if os.path.exists(os.path.join(ROOT, COMPANION)) else ""

    moved_in_companion = all(archive.count(r["_text"]) == 1 for r in p["moved"])
    moved_absent_from_parent = all(r["_text"] not in live for r in p["moved"])
    stayed_at_site = all(live.count(r["_text"]) == 1 for r in p["stayed"])
    stayed_not_in_companion = all(r["_text"] not in archive for r in p["stayed"])
    refused_at_site = all(live.count(r["_text"]) == 1 for r in p["refused"])
    refused_not_in_companion = all(r["_text"] not in archive for r in p["refused"])

    return {
        "what_this_is":
            "THE TWO RULED `CLAUDE.md` SPANS, READ BEFORE THEY MOVE: which span the ruling places "
            "in the archive, what the reading found in each, and the mechanical proof of where "
            "every span of this act's population actually stands. Every figure here is computed; "
            "none is transcribed (D-431).",
        "generated_by": "tools/audit/gen_claude_md_finer_archive.py",
        "dispatch": f"{DISPATCH}, Task 1",
        "the_ruling": f"Ruling 1 of {RULINGS}: two spans ARCHIVE with a dated pointer at each "
                      f"site; the four contested proposals are REFUSED and their spans stay at "
                      f"site; the executing act derives them from the finer decomposition and "
                      f"never retypes them; a span that does not read at execution time as the "
                      f"ruling assumes is a STOP-and-report, never a forced move.",
        "measured_at_commit": PINNED_COMMIT,
        "base_commit": BASE_COMMIT,
        "★_how_the_population_is_derived_rather_than_listed":
            "The archive-class spans come from the pinned finer decomposition. Which of them the "
            "ruling archives and which it refuses is then derived from that artifact's OWN "
            "published conflict evidence under the surface's own conflict-reading rule: a span the "
            "A4 safeguard never read is the uncontested remainder and is archived; a span the "
            "safeguard read and kept is archived only where its stated reason was an OVERRUN into "
            "live rule text, which the finer cut answers, and refused where the reason was that "
            "the span itself states a rule, which no cut answers. The derivation reproducing "
            "Ruling 1's own stated shape — two archive, four refused — is a STOP, not an "
            "assumption.",
        "the_reading_test_applied": READING_TEST,
        "★_the_outcome_of_this_run":
            "BOTH ruled spans carry a STAY verdict from the reading, so NOTHING MOVED and "
            "`CLAUDE.md` is unedited by this act. That is Ruling 1's own provided outcome rather "
            "than a refusal of it: the ruling names the read-before-move safeguard as this act's "
            "discipline and states what happens when a span fails it. The per-span reasons are "
            "published below with mechanical evidence, so the user can overrule either verdict in "
            "one edit — the tool's --apply path is complete and would perform the move.",
        "★_what_this_act_does_NOT_establish":
            "That either span is unarchivable. What is established per span is narrower and is "
            "what the imported test asks: for lines 53-60, that the class is supplied entirely by "
            "two archive pointers inside the span and that the span's own text states a live "
            "supersession; for lines 194-213, that its closing sentence is a live status statement "
            "about a running clock on a gating obligation. A later ruling, or a re-homing of that "
            "sentence, can move either.",
        "the_ruled_population": {
            "archive_class_spans_in_the_pinned_decomposition":
                len(p["moved"]) + len(p["stayed"]) + len(p["refused"]),
            "ruled_to_archive": len(p["moved"]) + len(p["stayed"]),
            "ruled_refused_and_untouched": len(p["refused"]),
        },
        "spans_moved": len(p["moved"]),
        "spans_left_at_site_by_the_reading": len(p["stayed"]),
        "characters_moved": p["characters_moved"],
        "characters_left_at_site_by_the_reading": sum(r["characters"] for r in p["stayed"]),
        "the_moved": [{k: v for k, v in r.items() if k != "_text"} for r in p["moved"]],
        "the_left_at_site_by_the_reading":
            [{k: v for k, v in r.items() if k != "_text"} for r in p["stayed"]],
        "the_refused_by_the_ruling":
            [{k: v for k, v in r.items() if k != "_text"} for r in p["refused"]],
        "reconciliation": {
            "every_moved_span_is_byte_present_in_the_companion_exactly_once": moved_in_companion,
            "every_moved_span_is_absent_from_the_parent": moved_absent_from_parent,
            "every_span_the_reading_flagged_is_still_present_at_site_exactly_once": stayed_at_site,
            "no_span_the_reading_flagged_is_in_the_companion": stayed_not_in_companion,
            "every_span_the_ruling_REFUSED_is_still_present_at_site_exactly_once": refused_at_site,
            "no_span_the_ruling_REFUSED_is_in_the_companion": refused_not_in_companion,
            "moved_plus_kept_accounts_for_the_base_blob_to_the_character":
                p["characters_moved"] + p["characters_kept"] == p["base_characters"],
            "the_base_blob_sha256": sha(git_show(BASE_COMMIT, PARENT)),
            "what_that_proves_together":
                "Nothing left the must-read that is not in the archive; every span the reading "
                "flagged and every span the ruling refused is still exactly where it was; and no "
                "flagged or refused span was quietly archived alongside a moved one. The last two "
                "are the directions that matter at this run, because nothing moved: a check that "
                "only proved a move would be green at a tree where the refusals had been "
                "overridden. All are byte comparisons against the files as they stand and against "
                "the git objects named by explicit hash — never against the memory of performing "
                "the act (#15).",
        },
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--apply", action="store_true", help="perform the ruled move (once)")
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
            print(f"FAIL: the finer archive record does not re-derive: "
                  f"{os.path.relpath(OUT, ROOT)}")
            return 1
    else:
        with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        print(f"wrote {os.path.relpath(OUT, ROOT)}")

    rec = art["reconciliation"]
    print(f"  ruled to archive: {art['the_ruled_population']['ruled_to_archive']}, "
          f"moved {art['spans_moved']}, left at site by the reading "
          f"{art['spans_left_at_site_by_the_reading']}; "
          f"refused by the ruling {art['the_ruled_population']['ruled_refused_and_untouched']}")
    print(f"  characters moved: {art['characters_moved']:,}")
    for label, key in (
            ("moved spans byte-present in the companion exactly once",
             "every_moved_span_is_byte_present_in_the_companion_exactly_once"),
            ("moved spans absent from the must-read",
             "every_moved_span_is_absent_from_the_parent"),
            ("every flagged span still at site exactly once",
             "every_span_the_reading_flagged_is_still_present_at_site_exactly_once"),
            ("no flagged span in the companion",
             "no_span_the_reading_flagged_is_in_the_companion"),
            ("every REFUSED span still at site exactly once",
             "every_span_the_ruling_REFUSED_is_still_present_at_site_exactly_once"),
            ("no REFUSED span in the companion",
             "no_span_the_ruling_REFUSED_is_in_the_companion"),
            ("moved + kept accounts for the base blob",
             "moved_plus_kept_accounts_for_the_base_blob_to_the_character")):
        print(f"  {label:<55} {rec[key]}")
    ok = all(rec[k] for k in rec if isinstance(rec[k], bool))
    return 0 if ok else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Stop as exc:
        print(f"STOP: {exc}")
        sys.exit(2)
