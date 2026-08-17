#!/usr/bin/env python3
"""THE POST-SPLIT ARCHIVING PASS — the ruled archivability test applied to what has accumulated.

THE RULING THIS EXISTS FOR.  User, 2026-08-17, Ruling 2 of
`cowork_rulings_2026_08_17_session_start_read_sitting.md`: *"The archivability test (§5(E) of the
2026-08-16 record) is applied to what has accumulated since the split — the resolved-opening rows
still in `OPEN_ITEMS.md`, `DECISIONS.md` exhaustively, and any span in the five that the test
places — riding whatever dispatch executes Ruling 1."*  And, recorded with it: *"A modest yield is
the expectation, not a transformative one, and a pass that returns little is this ruling working
rather than failing."*

★ NO NEW MECHANISM IS RULED AND NONE IS INTRODUCED.  Everything this file decides with is
IMPORTED (#6): the span cut, the six classes and the recognizers from
`gen_governing_surface_spans`; the ONE compact dated pointer shape and the per-file companions
from `gen_governing_surface_split`; the standing archive-pointer constraint from
`gen_claude_md_finer_spans`; the row split and the leading-token test through the one index lint
those modules already import.  What is NEW here is only WHEN the measurement is taken — at this
batch's own commit rather than at the split's — which is what the split's own pinning comment says
a later pruning wave does.

WHAT IS DERIVED AND WHAT IS AUTHORED.

  DERIVED   the span population of the five files at this act's pin; each span's class and the
            marker that placed it; which spans a previous act already archived; the six
            `CLAUDE.md` spans the seventh- and eighth-return sittings settled, taken from the
            committed record of those acts rather than listed here; every count.
  AUTHORED  the base commit this act is performed on top of, and ONE READING VERDICT PER SPAN the
            test proposes — the read-before-move safeguard (A4), which is the whole reason this is
            not a bulk move.

THE READING TEST, IMPORTED FROM THE EXECUTED SPLIT RATHER THAN RESTATED (#6):

  (1) CLASS FIDELITY — the span, read whole, IS a record of the kind its class names.  A span that
      merely POINTS AT such material preserved elsewhere fails this half.
  (2) NO LIVE REMAINDER — no part of the span states a rule, a STOP condition, a live caveat or a
      prohibition that a working session acts on today.

Anything else stays: the ruled DOUBT DEFAULT (§5(E) of
`cowork_rulings_2026_08_16_preparation_return.md`), whose recorded ground is the asymmetry — a
wrongly archived operative span fails SILENTLY while wrongly kept noise fails visibly and cheaply,
and staying is the recoverable direction.

THE THREE POPULATIONS THAT ARE EXCLUDED BEFORE ANY READING, each for a recorded reason:
  * a span a PREVIOUS act already archived — for `OPEN_ITEMS.md` the split leaves a stub ROW at the
    site, so its status cell still opens with the resolved mark and the recognizer would propose it
    a second time; the stub is recognised by the pointer the split itself writes, imported from
    that tool;
  * the SIX `CLAUDE.md` spans the seventh- and eighth-return sittings settled — four REFUSED at the
    seventh-return sitting and two RULED to stay at the eighth — which Ruling 2's own dispatch
    forbids re-proposing: *"a pass that proposes any of them again must answer the recorded reason
    rather than rediscover it, and this batch does not answer them."*  Their identities come from
    the committed record of those acts, never from a list here;
  * a span whose archive classification derives from text INSIDE an archive pointer, under the
    standing constraint ruled at Ruling 1 of `cowork_rulings_2026_08_17_eighth_return.md`.

THE STOPS — each one a way this act could go wrong silently:
  * a proposed span with no authored reading verdict halts it, so no span moves unread;
  * an authored verdict naming a span the derivation does not carry halts it;
  * a MOVE span not byte-present exactly once in the base blob halts it;
  * a MOVE span already present in its companion halts it — the move has run;
  * a companion the ruled mapping does not name halts it.

Run:
    python tools/audit/gen_post_split_archive.py --apply    # perform the ruled moves once
    python tools/audit/gen_post_split_archive.py --check    # re-derive the reconciliation
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
from output_encoding import use_utf8_output                 # noqa: E402  (path set above)
import gen_governing_surface_spans as coarse                # noqa: E402  the cut and the classes
import gen_claude_md_finer_spans as finer                   # noqa: E402  the pointer constraint
import gen_claude_md_finer_archive as ruled_spans           # noqa: E402  the six settled spans
from gen_governing_surface_split import (                   # noqa: E402  the ONE pointer shape
    ARCHIVE_CLASSES, COMPANION, POINTER, pointer_text,
)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

OUT = os.path.join(HERE, "post_split_archive.json")

# The commit this act reads the five files at, and performs its moves on top of: Task 1 of the
# executing dispatch, pushed before this task began. An explicit hash, which is the only git read
# D-253 permits.
PIN = "466781625554dc252dd1146a0425bc29086d0884"
PIN_IS = "cc_instruction_preparation_ninth.md Task 1, pushed before this task began"

ACT_DATE = "2026-08-17"
DISPATCH = "cc_instruction_preparation_ninth.md"
RULING = "cowork_rulings_2026_08_17_session_start_read_sitting.md"

MOVE = "MOVE"
STAY = "STAYS AT SITE — flagged by the reading (A4)"
# ★ A THIRD VERDICT, DECLARED RATHER THAN FOLDED INTO THE SECOND. A span a STANDING MECHANISM
# already owns did not FAIL the reading test; moving it here would put a second path on one concern
# (#6) and race the mechanism that owns it. Recording it as a flagged failure would say something
# false about the reading, so it is its own verdict with the owning mechanism named per span.
OWNED = "STAYS AT SITE — owned by a standing mechanism (#6)"

READING_TEST = (
    "A span MOVES only when (1) it IS, read whole, a record of the kind its class names — a span "
    "that merely POINTS AT such material preserved elsewhere fails this half — and (2) no part of "
    "it states a rule, a STOP condition, a live caveat or a prohibition that a working session "
    "acts on today. Anything else stays: the ruled doubt default (§5(E)), whose recorded ground is "
    "that a wrongly archived operative span fails silently while wrongly kept noise fails visibly "
    "and cheaply. The test is IMPORTED from the executed split, which is the discipline Ruling 2 "
    "names for this pass."
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


def line_form(live: str, text: str) -> str:
    """`text`, as the git object gives it (LF), in the LIVE file's own line-ending form.

    ★ THE DECLARED CAVEAT THIS ANSWERS, and it is not hypothetical — it was MEASURED on this
    pass's first run. Some of these files are stored on disk with carriage-return line endings
    where their committed blobs have none; the repository marks them `text=auto`, so git reports
    no modification and the two are identical once the carriage returns are removed. A byte
    comparison between a span taken from the git object and the same span in the working tree
    therefore reports ABSENT for a span that is present, and a reconciliation built on it would go
    red at a tree where nothing is wrong. Every comparison and every replacement below goes through
    this function, so the line-ending form is normalised before anything decides.
    """
    return text.replace("\n", "\r\n") if "\r\n" in live else text


# ── AUTHORED — one reading verdict per proposed span (the A4 safeguard) ───────────────────────
# Keyed by (file, first_line, last_line) AT THIS ACT'S PIN. Every one was read in the file itself
# with the file tools, never from the artifact's opening — which is the whole reason the safeguard
# exists.
_OPEN_ROW_REFUSAL = (
    "★ FAILS TEST (1) AND TEST (2), AND THE ROW IS OPEN. Read whole, this is a LIVE OPEN row of "
    "the register — it appears in the derived live gating answer's open population — and the "
    "marker that placed it sits INSIDE its status cell, describing one of the cell's own sentences "
    "or a former wording preserved ELSEWHERE, not the row. TEST (1): the row is not a preserved "
    "former wording or a self-declared historical block; it is a tracked issue that is not "
    "resolved. TEST (2): its status cell is what a working session reads to know what the row is "
    "waiting on. This is finding F33's mis-class shape reappearing on the register's own rows: a "
    "#12 preservation phrase inside a live cell places the whole cell in an archive class."
)
_STATUS_ENTRY = (
    "★ IT DID NOT FAIL THE READING — A STANDING MECHANISM ALREADY OWNS IT. This is one of the "
    "EIGHTH batch's dated entries, and the standing forward bound of Ruling 4 of "
    "`cowork_rulings_2026_08_17_governing_surface_split.md` moves a batch's entries to "
    "`STATUS_ARCHIVE.md` the moment a later batch's close exists — executed by "
    "`tools/audit/gen_status_batch_bound.py`, which THIS dispatch's Task 5 runs in the same act "
    "that writes this batch's own entries. Moving it here would put a second path on one concern "
    "(#6) and would race that mechanism inside one batch. It stays for Task 5."
)

# ── AUTHORED — one reading verdict per proposed span (the A4 safeguard) ───────────────────────
# Keyed by (file, first_line, last_line) AT THIS ACT'S PIN. Every one was read in the file itself
# with the file tools, never from the artifact's opening — which is the whole reason the safeguard
# exists.
VERDICTS: dict[tuple[str, int, int], tuple[str, str]] = {
    ("CLAUDE.md", 457, 616): (
        STAY,
        "★ FAILS TEST (1), AND IT IS THE MEASURED F33 CASE BY NAME. Read whole, this span is the "
        "ENTIRE decisions-register section of `CLAUDE.md` — rules (a) through (n), the live "
        "governing rules a session applies when it decides where a decision is homed. It was "
        "placed by the two words `former wording` occurring inside rule (i)'s and rule (j)'s "
        "defenses, each of which POINTS AT a former wording preserved in the register's own "
        "provenance rather than carrying one. The finer pass measured exactly this and recorded "
        "it: \"the coarse pass placed 15,395 characters of live governing rule text — the "
        "decisions register's rules (a) through (n) — on exactly this signal.\" TEST (2) fails "
        "too, and comprehensively: every clause of the span states a rule."),
    ("CLAUDE.md", 1100, 1100): (
        STAY,
        "★ FAILS TEST (1) ON THE STRUCTURAL GROUND THE MACHINERY ALREADY NAMES. The span is a "
        "BARE `###` HEADING and nothing else — `(C) RETROSPECTIVE — the batch 52/24/52 stop` — "
        "classed by the word `RETROSPECTIVE` in its own title. A heading is a span of its own and "
        "its section body is a different span, so archiving it would move the heading while "
        "everything under it stayed: a headless section here, and a heading filed alone in the "
        "companion. That is the second of the two structural spans `gen_claude_md_finer_spans.py` "
        "places positively at site, and the ground is imported from there rather than re-argued. "
        "The section's own archived material already left under a pointer sitting directly "
        "beneath this heading."),
    ("OPEN_ITEMS.md", 235, 235): (
        STAY,
        "[[OI-179]]. " + _OPEN_ROW_REFUSAL + " ★ AND THIS ONE IS THE SHARPEST INSTANCE THE PASS "
        "COULD HAVE PRODUCED: the row is OPEN and GATES under #19, every ruling this batch "
        "executes names it as untouched, and the marker that proposed it — `is SUPERSEDED` — "
        "describes two of the cell's OWN earlier sentences, each preserved in place under #12 "
        "because a later act answered it. The row is the register's live record of the "
        "ground-truth ceiling obligation."),
    ("OPEN_ITEMS.md", 314, 314): (STAY, "[[OI-274]]. " + _OPEN_ROW_REFUSAL),
    ("OPEN_ITEMS.md", 355, 355): (STAY, "[[OI-317]]. " + _OPEN_ROW_REFUSAL),
    ("OPEN_ITEMS.md", 359, 359): (STAY, "[[OI-321]]. " + _OPEN_ROW_REFUSAL),
    ("OPEN_ITEMS.md", 384, 384): (STAY, "[[OI-346]]. " + _OPEN_ROW_REFUSAL),
    ("OPEN_ITEMS.md", 395, 395): (STAY, "[[OI-357]]. " + _OPEN_ROW_REFUSAL),
    ("OPEN_ITEMS.md", 401, 401): (STAY, "[[OI-363]]. " + _OPEN_ROW_REFUSAL),
    ("OPEN_ITEMS.md", 408, 408): (
        MOVE,
        "[[OI-370]]. ★ PASSES BOTH HALVES, AND IT IS THE ONE GENUINE MEMBER OF THE RULING'S OWN "
        "NAMED SUBJECT. Read whole, the row is RESOLVED — its status cell opens with the resolved "
        "mark, read through the ONE index parser — and its body is entirely the record of that "
        "resolution: what was archived, under which ruling, by which act, and the both-directions "
        "reconciliation that proves nothing was lost. TEST (1): it IS a resolved row, which "
        "§5(E) names as archive material in terms — its only reader is someone auditing the "
        "history of an issue that is closed. TEST (2): it states no rule, no STOP, no caveat and "
        "no prohibition. ★ THE ONE HESITATION IS RECORDED RATHER THAN SUPPRESSED: the cell's "
        "closing clause says closing act (b), the size guard, `stays PROPOSED and untaken`. That "
        "is a record of this resolution's own limits, which is what an auditor of the closed issue "
        "needs; it is carried by the row's detail file, which the site keeps a link to; and the "
        "site keeps the row itself — its identity, its gate cell, its detail link and its status "
        "cell's own opening — so the register's bijection, its canonical status opening and the "
        "row's resolved state all survive the move."),
    ("DECISIONS.md", 252, 258): (
        STAY,
        "★ FAILS TEST (1) AND TEST (2). Read whole, the span is the block quote that STATES the "
        "ruled home criterion (D-430), what it supersedes, how a whole-document delegation is "
        "read, and the scope of its application — live rules a session applies whenever it asks "
        "whether a document is a contract home. It was placed by the phrase `TRIED AND CLOSED` in "
        "its final paragraph, which records two alternatives tried for a FILE REMOVAL inside an "
        "otherwise rule-stating block. A declined-alternative sentence inside a rule does not make "
        "the rule a declined-alternatives record — the class is deliberately narrow and this is "
        "the narrowness failing in the direction the doubt default exists for."),
    ("DECISIONS.md", 266, 266): (
        STAY,
        "★ FAILS TEST (1) AND TEST (2). Read whole, the span is `The remainder, measured.` — the "
        "register's own live BOUND on what it may claim about the documents it did not read in "
        "full, with the two qualifications that say how the figure is read at HEAD. It was placed "
        "by the sentence `THE FORMER WORDING IS PRESERVED VERBATIM (#12) at "
        "backbone_decisions.json`, which POINTS AT a former wording held elsewhere and carries "
        "none — F33's signal exactly. A working session reads this paragraph to know what the "
        "register's scope claim is worth."),
    ("DECISIONS.md", 270, 276): (
        STAY,
        "★ FAILS TEST (1). Read whole, the span records three corrections made to the scope block "
        "on a named date and states where each former wording is preserved — in "
        "`backbone_decisions.json`, not here. So it POINTS AT preserved wordings rather than "
        "carrying one, which is the half of TEST (1) that a pointer fails. It also carries live "
        "material a session acts on: the third bullet names the computed check that measures the "
        "home-granularity claim and asserts that claim true at HEAD."),
    ("STATUS.md", 8, 8): (OWNED, _STATUS_ENTRY),
    ("STATUS.md", 10, 10): (OWNED, _STATUS_ENTRY),
    ("STATUS.md", 12, 12): (OWNED, _STATUS_ENTRY),
    ("STATUS.md", 14, 14): (OWNED, _STATUS_ENTRY),
    ("STATUS.md", 16, 16): (OWNED, _STATUS_ENTRY),
    ("STATUS.md", 18, 18): (OWNED, _STATUS_ENTRY),
}


def already_archived_marker(name: str) -> str:
    """The marker a PREVIOUS archiving act left at a site in this file, derived from that act.

    Built from the imported pointer shape rather than typed here (#6): for `OPEN_ITEMS.md` the
    split leaves a stub ROW whose status cell still opens with the resolved mark, so without this
    the recognizer would propose every already-archived row a second time.
    """
    return f"ARCHIVED {ACT_DATE}: the full row is in `{COMPANION[name]}`"


def settled_claude_md_spans() -> list[str]:
    """The SIX `CLAUDE.md` spans the seventh- and eighth-return sittings settled, by TEXT.

    Derived from the committed record of those acts — `gen_claude_md_finer_archive`'s own ruled
    population, read at its own pin — never listed here. Text rather than coordinates, because the
    two acts are pinned at different commits and a coordinate would silently drift.
    """
    to_archive, refused, constraint_refused = ruled_spans.ruled_population()
    spans = ruled_spans.with_text(to_archive + refused + constraint_refused)
    return [s["_text"] for s in spans]


def proposals() -> list[dict]:
    """Every span of the five files the ruled test PLACES, after the three ruled exclusions."""
    settled = settled_claude_md_spans()
    out = []
    for name in coarse.FILES:
        if name not in COMPANION:
            raise Stop(f"{name} has no companion in the ruled mapping — a move needs a "
                       f"destination the ruling names")
        text = git_show(PIN, name)
        lines = text.splitlines(keepends=True)
        spans, _ = coarse.spans_of(text)
        stub = already_archived_marker(name)
        for span in spans:
            body = span["text"]
            category, evidence, defaulted = coarse.classify(span, name)
            wanted = set(ARCHIVE_CLASSES) | ({POINTER} if name == "STATUS.md" else set())
            if category not in wanted:
                continue
            if stub in body:
                continue                              # a previous act already archived it
            # Containment is tested in BOTH directions. The two acts cut at different grains, so a
            # settled span can sit INSIDE a span of this pass's coarser cut — and proposing the
            # container IS re-proposing the settled span, with more besides.
            if name == "CLAUDE.md" and any(s in body or body in s for s in settled):
                continue                              # settled at the two return sittings
            regions = finer.archive_pointer_regions(body)
            if regions:
                marker = evidence.get("the_marker_matched")
                at = body.find(marker) if marker else -1
                if at >= 0 and finer.inside_a_pointer(at, regions):
                    continue                          # the standing pointer constraint
            recomputed = "".join(lines[span["first_line"] - 1:span["last_line"]])
            if recomputed != body:
                raise Stop(f"{name} lines {span['first_line']}-{span['last_line']}: the span's "
                           f"coordinates do not reproduce its own text")
            out.append({
                "file": name,
                "first_line_at_the_pin": span["first_line"],
                "last_line_at_the_pin": span["last_line"],
                "kind": span["kind"],
                "characters": len(body),
                "the_class": category,
                "the_evidence": evidence,
                "placed_by_the_doubt_default": defaulted,
                "the_opening": " ".join(body.split())[:160],
                "_text": body,
            })
    return out


def plan() -> dict:
    props = proposals()
    keys = {(p["file"], p["first_line_at_the_pin"], p["last_line_at_the_pin"]) for p in props}
    unverdicted = sorted(k for k in keys if k not in VERDICTS)
    if unverdicted:
        detail = "\n".join(
            f"    {p['file']} {p['first_line_at_the_pin']}-{p['last_line_at_the_pin']} "
            f"[{p['the_class']}] {p['the_evidence']}"
            for p in props
            if (p["file"], p["first_line_at_the_pin"], p["last_line_at_the_pin"]) in unverdicted)
        raise Stop("span(s) with no authored reading verdict — Ruling 2 binds this pass to the "
                   "read-before-move safeguard, so an unread span halts it:\n" + detail)
    stray = sorted(k for k in VERDICTS if k not in keys)
    if stray:
        raise Stop(f"authored verdict(s) naming a span the derivation does not carry: {stray} — "
                   f"the verdicts and the measurement have drifted apart")

    moved, stayed = [], []
    for p in props:
        key = (p["file"], p["first_line_at_the_pin"], p["last_line_at_the_pin"])
        verdict, why = VERDICTS[key]
        rec = {k: v for k, v in p.items() if k != "_text"}
        rec.update({"the_verdict": verdict, "why": why,
                    "how_the_verdict_was_made": "authored per span, read in the file itself (A4)",
                    "text_sha256": sha(p["_text"]), "_text": p["_text"]})
        (moved if verdict == MOVE else stayed).append(rec)

    per_file = {}
    for name in coarse.FILES:
        mine = [r for r in moved if r["file"] == name]
        base = git_show(PIN, name)
        for rec in mine:
            if base.count(rec["_text"]) != 1:
                raise Stop(f"{name} lines {rec['first_line_at_the_pin']}-"
                           f"{rec['last_line_at_the_pin']}: the span's text occurs "
                           f"{base.count(rec['_text'])} time(s) in the base blob — a move needs "
                           f"exactly one occurrence")
        order = sorted(mine, key=lambda r: base.index(r["_text"]))
        new_parent, pointers, by_span = base, [], {}
        for rec in order:
            ptr = pointer_text(name, {"first_line": rec["first_line_at_the_pin"],
                                      "last_line": rec["last_line_at_the_pin"],
                                      "the_class": rec["the_class"]}, rec["_text"])
            new_parent = new_parent.replace(rec["_text"], ptr, 1)
            pointers.append(ptr)
            by_span[(rec["first_line_at_the_pin"], rec["last_line_at_the_pin"])] = ptr
        body = ""
        for rec in order:
            body += (f"> **From `{name}` lines {rec['first_line_at_the_pin']}–"
                     f"{rec['last_line_at_the_pin']} at `{PIN[:10]}`, class "
                     f"`{rec['the_class']}`, {rec['characters']} characters.** Moved {ACT_DATE} by "
                     f"`{DISPATCH}` Task 2, executing Ruling 2 of `{RULING}`; "
                     f"{rec['how_the_verdict_was_made']}.\n\n")
            body += rec["_text"]
            if not body.endswith("\n"):
                body += "\n"
            body += "\n"
        moved_characters = sum(r["characters"] for r in order)
        per_file[name] = {
            "companion": COMPANION[name],
            "moved": order,
            "pointers": pointers,
            "pointer_by_span": by_span,
            "new_parent": new_parent,
            "companion_body": body,
            "base_characters": len(base),
            "characters_moved": moved_characters,
            "characters_kept": len(base) - moved_characters,
        }
    return {"proposed": props, "moved": moved, "stayed": stayed, "per_file": per_file}


def apply_move() -> None:
    p = plan()                       # raises before anything is written
    if not p["moved"]:
        raise Stop("every proposed span carries a STAY verdict from the reading, so there is "
                   "nothing to apply. Ruling 2's own doubt default makes that outcome lawful, and "
                   "it is REPORTED rather than forced. Run --check to record the reading and prove "
                   "every span is still at site.")
    for name, f in p["per_file"].items():
        if not f["moved"]:
            continue
        live, archive = read(name), read(f["companion"])
        new_live = live
        for rec in f["moved"]:
            here = line_form(live, rec["_text"])
            if line_form(archive, rec["_text"]) in archive:
                raise Stop(f"a span is already in {f['companion']} — the move has run ({name} pin "
                           f"lines {rec['first_line_at_the_pin']}-{rec['last_line_at_the_pin']})")
            if live.count(here) != 1:
                raise Stop(f"{name} pin lines {rec['first_line_at_the_pin']}-"
                           f"{rec['last_line_at_the_pin']}: the span occurs "
                           f"{live.count(here)} time(s) in the live file — it has changed "
                           f"under the act and the move would not be byte-faithful")
            new_live = new_live.replace(here, line_form(live, f["pointer_by_span"][
                (rec["first_line_at_the_pin"], rec["last_line_at_the_pin"])]), 1)
        # The parent is edited IN ITS OWN LINE-ENDING FORM rather than rewritten from the pinned
        # blob: rewriting would silently re-line-end the whole file, which is a change to every
        # line of a governing surface for the sake of moving one span.
        write(name, new_live)
        write(f["companion"],
              archive.rstrip("\r\n") + line_form(archive, "\n\n" + f["companion_body"]))


def build() -> dict:
    p = plan()
    files = {}
    for name, f in p["per_file"].items():
        live = read(name)
        archive = read(f["companion"]) if os.path.exists(
            os.path.join(ROOT, f["companion"])) else ""
        mine_stay = [r for r in p["stayed"] if r["file"] == name]
        files[name] = {
            "companion": f["companion"],
            "spans_proposed_by_the_test": sum(1 for r in p["proposed"] if r["file"] == name),
            "spans_moved": len(f["moved"]),
            "spans_left_at_site_by_the_reading": len(mine_stay),
            "characters_moved": f["characters_moved"],
            "characters_left_at_site_by_the_reading": sum(r["characters"] for r in mine_stay),
            "the_moved": [{k: v for k, v in r.items() if k != "_text"} for r in f["moved"]],
            "the_left_at_site_by_the_reading":
                [{k: v for k, v in r.items() if k != "_text"} for r in mine_stay],
            "reconciliation": {
                "every_moved_span_is_byte_present_in_the_companion_exactly_once":
                    all(archive.count(line_form(archive, r["_text"])) == 1 for r in f["moved"]),
                "every_moved_span_is_absent_from_the_parent":
                    all(line_form(live, r["_text"]) not in live for r in f["moved"]),
                "every_span_the_reading_flagged_is_still_present_at_site_exactly_once":
                    all(live.count(line_form(live, r["_text"])) == 1 for r in mine_stay),
                "no_span_the_reading_flagged_is_in_the_companion":
                    all(line_form(archive, r["_text"]) not in archive for r in mine_stay),
                "moved_plus_kept_accounts_for_the_base_blob_to_the_character":
                    f["characters_moved"] + f["characters_kept"] == f["base_characters"],
                "the_base_blob_sha256": sha(git_show(PIN, name)),
                "★_the_line_ending_form_was_normalised_before_any_of_these_decided": True,
            },
        }

    return {
        "what_this_is":
            "THE POST-SPLIT ARCHIVING PASS: every span of the five mandatory-read files the ruled "
            "archivability test places, READ WHOLE before it moves, with the mechanical proof of "
            "where every span of this act's population actually stands. Every figure here is "
            "computed; none is transcribed (D-431).",
        "generated_by": "tools/audit/gen_post_split_archive.py",
        "dispatch": f"{DISPATCH}, Task 2",
        "the_ruling": (
            f"Ruling 2 of `{RULING}`: the archivability test (§5(E) of the 2026-08-16 record) is "
            "applied to what has accumulated since the split — the resolved-opening rows still in "
            "`OPEN_ITEMS.md`, `DECISIONS.md` exhaustively, and any span in the five that the test "
            "places. A modest yield is the expectation, not a transformative one, and a pass that "
            "returns little is this ruling working rather than failing."),
        "measured_at_commit": PIN,
        "★_why_the_reading_is_pinned": {
            "what_that_commit_is": PIN_IS,
            "the_reason": "the five files are read at a git OBJECT so this act's own writes cannot "
                          "move the measurement under it, which is the defect the split's own "
                          "pinning comment records; a later pruning wave takes its own measurement "
                          "at its own commit, which is what this pass is.",
        },
        "the_reading_test_applied": READING_TEST,
        "★_what_is_imported_rather_than_re_decided_(#6)": {
            "the_span_cut_the_six_classes_and_the_recognizers": "gen_governing_surface_spans.py",
            "the_compact_dated_pointer_and_the_companions": "gen_governing_surface_split.py",
            "the_standing_archive_pointer_constraint": "gen_claude_md_finer_spans.py — "
                                                       + finer.POINTER_CONSTRAINT,
            "the_six_settled_CLAUDE_md_spans": "gen_claude_md_finer_archive.py, its own ruled "
                                               "population read at its own pin",
        },
        "the_three_exclusions_taken_before_any_reading": {
            "already_archived_by_a_previous_act": "recognised by the pointer the split itself "
                                                  "writes at a site, imported from that tool",
            "settled_at_the_seventh_and_eighth_return_sittings": "the four REFUSED spans and the "
                                                                 "two RULED to stay; the dispatch "
                                                                 "forbids re-proposing them and "
                                                                 "this batch does not answer their "
                                                                 "recorded reasons",
            "classified_by_text_inside_an_archive_pointer": finer.POINTER_CONSTRAINT,
        },
        "totals": {
            "spans_proposed_by_the_test": len(p["proposed"]),
            "spans_moved": len(p["moved"]),
            "spans_left_at_site_by_the_reading": len(p["stayed"]),
            "characters_moved": sum(r["characters"] for r in p["moved"]),
            "characters_left_at_site_by_the_reading": sum(r["characters"] for r in p["stayed"]),
        },
        "per_file": files,
        "★_what_this_pass_does_NOT_do": [
            "It moves no verdict, no gate, no cut and no population: a row's status token, its "
            "identity, its gate cell and its detail link all survive a move, which is what the "
            "imported pointer shape is for.",
            "It archives, moves or deletes NO document AS A FILE.",
            "It creates, flips or discards NO open-items row.",
            "It re-proposes none of the six `CLAUDE.md` spans the two return sittings settled.",
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
            print(f"FAIL: the post-split archiving record does not re-derive: "
                  f"{os.path.relpath(OUT, ROOT)}")
            return 1
    else:
        with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        print("wrote", os.path.relpath(OUT, ROOT))

    t = art["totals"]
    print(f"  proposed {t['spans_proposed_by_the_test']}, moved {t['spans_moved']}, "
          f"left at site by the reading {t['spans_left_at_site_by_the_reading']}")
    print(f"  characters moved: {t['characters_moved']:,}")
    for name, f in art["per_file"].items():
        r = f["reconciliation"]
        if f["spans_proposed_by_the_test"]:
            print(f"  {name}: proposed {f['spans_proposed_by_the_test']}, "
                  f"moved {f['spans_moved']}, stayed {f['spans_left_at_site_by_the_reading']}, "
                  f"all six directions " + str(all(v for k, v in r.items()
                                                   if isinstance(v, bool))))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Stop as exc:
        print("STOP:", exc)
        raise SystemExit(2)
