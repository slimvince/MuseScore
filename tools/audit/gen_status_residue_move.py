#!/usr/bin/env python3
"""THE PRE-CONVENTION `STATUS.md` RESIDUE, MOVED UNDER RULING 4's OWN LINE — read before it moves.

THE RULING THIS EXISTS FOR.  User, 2026-08-17, Ruling 3 of
`cowork_rulings_2026_08_17_sixth_return.md` (the user's word: "A."): *"The next dispatch moves the
17 dated entries to `STATUS_ARCHIVE.md` under Ruling 4's own line, each entry READ before it moves
(the A4 safeguard binding — an entry that does not read as a completed batch's dated record stays
at site and is flagged), each move byte-faithful."*

WHAT THE RESIDUE IS, so the population is a derivation rather than a list.  The executed split
(`gen_governing_surface_split.py`) moved the 131 spans of `STATUS.md` that the PINNED decomposition
places in an archive class.  Ruling 4's bound — the site keeps only the latest batch's entries —
was therefore reached over the MEASURED population and not over the file: the decomposition's
pointer recognizer matches the OI-222 remedy's own sentence, and the dated entries that predate or
paraphrase that sentence fell to `operative-rule-text` and stayed.  This tool moves exactly those.

  DERIVED   the candidate population: every span of `STATUS.md` in the pinned decomposition classed
            `operative-rule-text` and beginning AT OR AFTER the file's first dated entry — which
            cuts away the title and the banner without naming either.  Cross-checked in BOTH
            directions against the split-application artifact: no candidate is in that act's moved
            set, and the moved set plus the candidates plus the file's head account for every span
            the decomposition carries.
  DERIVED   every entry's TEXT, from the git OBJECT at the pinned commit, matched verbatim in the
            live file.  No entry is retyped: each is a single line of several thousand characters,
            and retyping one to move it is the transcription the record forbids.
  AUTHORED  the base commit this act is performed on top of, and ONE READING VERDICT PER CANDIDATE
            — assumption A3's safeguard, which is the whole reason this is not a bulk delete.

★ THE READING TEST, STATED ONCE AND APPLIED IDENTICALLY TO EVERY CANDIDATE.

    A candidate MOVES only when **(1)** it IS, read whole, a dated record of a COMPLETED batch or
    session — the dispatch it names has finished and the work it points forward to has been
    overtaken — and **(2)** it carries no rule, STOP, prohibition or live caveat whose ONLY home is
    this entry.  A rule the entry states AND names a home for is not a sole carrier: the move is
    archive-with-record, the pointer resolves, and #12 is satisfied by preservation
    elsewhere-with-record.  Anything else STAYS: the ruled doubt default, flagged.

  Clause (2)'s "sole carrier" wording is the narrow half and is meant narrowly.  Every candidate
  here PREDATES the OI-222 pointer remedy or paraphrases it, so unlike a modern entry it restates
  substance rather than pointing at it — which is exactly why the recognizer left it behind, and
  exactly why each one has to be read rather than classed.

THE STOPS — each one a way the act could go wrong silently:
  * a candidate with no authored reading verdict halts it, so no entry is moved unread;
  * an authored verdict naming a span the pinned decomposition does not carry halts it, so the
    verdicts and the measurement cannot drift apart;
  * a candidate that appears in the split-application artifact's own moved set halts it — the two
    acts would then be moving the same span twice;
  * the candidates, the split's moved set and the file's head not accounting for every span of the
    decomposition halts it;
  * a moved entry not present exactly once in the live file when the move is applied halts it;
  * an entry already present in the companion halts it — the move has run.

Run:
    python tools/audit/gen_status_residue_move.py --apply    # perform the move once
    python tools/audit/gen_status_residue_move.py --check    # re-derive the reconciliation
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
from output_encoding import use_utf8_output          # noqa: E402  (path set above)
from gen_status_archive_pass import ENTRY            # noqa: E402  the ONE dated-entry pattern (#6)
import gen_governing_surface_spans as spans          # noqa: E402  the pin and the class names (#6)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

OUT = os.path.join(HERE, "status_residue_move.json")
DECOMPOSITION = os.path.join(HERE, "governing_surface_spans.json")
SPLIT_APPLICATION = os.path.join(HERE, "governing_surface_split_application.json")

PARENT = "STATUS.md"
COMPANION = "STATUS_ARCHIVE.md"

# The pin is the span decomposition's own, imported rather than restated (#6): the population is
# that measurement's residue, so a disagreement about WHEN it was taken would make this act a
# statement about a different file.
PINNED_COMMIT = spans.PINNED_COMMIT

# The commit this move is performed on top of: Task 0 of the executing dispatch, pushed before
# Task 1 began. An explicit hash, which is the only git read D-253 permits.
BASE_COMMIT = "ec953b4cef423fba606cf84e89acbcda32fd8d6e"

ACT_DATE = "2026-08-17"
DISPATCH = "cc_instruction_preparation_seventh.md"
RULINGS = "cowork_rulings_2026_08_17_sixth_return.md"
SPLIT_RULINGS = "cowork_rulings_2026_08_17_governing_surface_split.md"

MOVE = "MOVE"
STAY = "STAYS AT SITE — flagged by the reading (A3)"

READING_TEST = (
    "A candidate MOVES only when (1) it IS, read whole, a dated record of a COMPLETED batch or "
    "session — the dispatch it names has finished and the work it points forward to has been "
    "overtaken — and (2) it carries no rule, STOP, prohibition or live caveat whose ONLY home is "
    "this entry. A rule the entry states AND names a home for is not a sole carrier: the move is "
    "archive-with-record and the pointer resolves (#12). Anything else STAYS: the ruled doubt "
    "default, flagged."
)

# ── AUTHORED — one reading verdict per candidate (Ruling 3's A4/A3 safeguard) ─────────────────
# Keyed by (first_line, last_line) AT THE PINNED COMMIT. Every one was read in this session, in
# `STATUS.md` itself, with the file tools — never from the decomposition's 160-character opening.
VERDICTS: dict[tuple[int, int], tuple[str, str]] = {
    (142, 142): (
        MOVE,
        "The phase-2 adjudication-method surface's commit entry. A dated record of a completed "
        "task that calls itself a POINTER in those words and names the method's one home; it "
        "missed the recognizer only because it does not carry the remedy's own sentence "
        "verbatim. Every rule it mentions is stated at that home and not here."),
    (144, 144): (
        MOVE,
        "The proxy-premise entry. Same shape: a completed task's dated record, saying in its own "
        "words that the premise is written in full as a dated note on `open_items/OI-179.md` and "
        "nothing is restated here. The premise's home is that row, which is OPEN and unmoved."),
    (154, 154): (
        MOVE,
        "The re-run-cut entry. A completed task's dated record pointing at three generated "
        "artifacts for every population and count; the finding it reports is rowed at [[OI-374]], "
        "which is untouched by this act."),
    (156, 156): (
        MOVE,
        "The halt-released entry. A completed task's dated record; the two rows it opened "
        "([[OI-372]], [[OI-373]]) carry their own narrative in their detail files, and the "
        "closing observation it makes about its own cuts is about work already done."),
    (222, 222): (
        MOVE,
        "The phase-1w delivery entry. A dated record of a completed wave: its result lives in the "
        "generated artifact it names, and every owed item in its closing list is a register row, "
        "which the register's own rule makes the authoritative status surface. Nothing in it is "
        "the sole carrier of a rule."),
    (650, 650): (
        MOVE,
        "A Cowork session close recording an adjudication IN FLIGHT. The dispatch it names has "
        "completed and its successor waves are themselves archived; the handover it points at is "
        "a block of `cowork_handoff.md`, which is unmoved."),
    (652, 652): (
        MOVE,
        "The OI-199 pass-2 receipt. A dated record of a completed verification. The user ruling "
        "it reports — dispositions not redone, the two arms completed, the instruments partition "
        "carrying the sealed test — is a scheduling ruling about work that has since been done, "
        "and OI-199's own row carries the state."),
    (654, 654): (
        MOVE,
        "The OI-199 pass-1 receipt. It states the standing structural remedy — withheld findings "
        "never enter a mandatory session-start read — AND names its home in the same sentence: "
        "*rowed by CC as OI-222*. That row is OPEN in `OPEN_ITEMS.md` at this tree, so the entry "
        "is not the rule's sole carrier and clause (2) is met rather than stretched."),
    (656, 656): (
        MOVE,
        "The analysis-cost receipt. The user rulings it reports are homed: correctness before "
        "performance compromise is a standing rule of `CLAUDE.md` dated to this very session, and "
        "the OI-199 pull-forward is a scheduling fact about a completed review."),
    (658, 687): (
        MOVE,
        "The OI-199 pass-1 delivery entry. A completed wave's dated record; every finding it "
        "reports was rowed in the same act ([[OI-215]]…[[OI-223]]) and the rows are the state."),
    (689, 689): (
        MOVE,
        "The OI-206 re-framing entry. Its user standing additions — very large scores must be "
        "handled; the effort control is one setting whose dials must bound temporally — are homed "
        "in `ARCHITECTURE.md`, in the decisions register and on [[OI-206]] / [[OI-209]]'s own "
        "detail files, so the entry restates them rather than carrying them."),
    (691, 727): (
        MOVE,
        "The analysis-cost profile delivery entry. A completed wave's dated record: every measured "
        "value it reports lives in the artifacts it names under `tools/notation_seams/` and "
        "`tools/joint_estimator/`, and the register rows it opened carry the consequences."),
    (729, 757): (
        MOVE,
        "The OI-206 investigation delivery entry. A completed wave's dated record, its two studies "
        "published as generated artifacts and its dated notes written onto [[OI-206]] and "
        "[[OI-203]]."),
    (759, 774): (
        MOVE,
        "A Cowork session close written mid-flight. The dispatch it calls in flight has completed, "
        "the notation switch it reports is recorded in `CLAUDE.md` gate block (A) and "
        "`ARCHITECTURE.md`, and the handover it points at is a block of `cowork_handoff.md`."),
    (776, 776): (
        MOVE,
        "The notation-switch entry. It is the fullest record of a completed, ratified act — and "
        "the act's standing consequences are homed: the staged scope's closure in `CLAUDE.md` "
        "gate block (A), the as-built record path in `ARCHITECTURE.md`, the retirement map on "
        "[[OI-180]]. What moves is the narrative of the act, not the rules it installed."),
    (778, 778): (
        MOVE,
        "The seams P7 close-out entry. A completed partition's dated record; its completeness "
        "verification is the generated artifact it names, and the post-switch agenda it lists is "
        "carried on the register rows it names."),
    (780, 780): (
        STAY,
        "★ FAILS TEST (1). It is not a dated record of anything: it is the LIVE navigational "
        "paragraph at the foot of the file, telling a reader that the older entries and every "
        "historical section are in `STATUS_ARCHIVE.md`, that the ratified robust-unit baselines, "
        "the hard stop and the gate policy live in `CLAUDE.md` gate block (A), and that the "
        "build/test commands live in `BUILD_AND_TEST.md`. A working session acts on it today. "
        "★ AND IT IS THE SEVENTEENTH MEMBER: the residue is 17 CANDIDATES, of which 16 are dated "
        "entries and this one is not — which is why the record's own count of *17 dated entries* "
        "is one too many, reported rather than quietly reconciled."),
}


class Stop(Exception):
    """A demand of the ruled move is unmet. Never a warning, never an entry moved unread."""


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


def load(path: str, what: str) -> dict:
    if not os.path.exists(path):
        raise Stop(f"{what} is missing: {os.path.relpath(path, ROOT)} — this act's population is "
                   f"derived from it and may not be listed by hand")
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def candidates() -> tuple[list[dict], dict]:
    """The residue, DERIVED, with the both-directions cross-check that bounds it."""
    decomposition = load(DECOMPOSITION, "the pinned span decomposition")
    application = load(SPLIT_APPLICATION, "the split-application artifact")

    per_file = next((f for f in decomposition["per_file"] if f["file"] == PARENT), None)
    if per_file is None:
        raise Stop(f"the pinned decomposition carries no {PARENT} — the residue cannot be derived")
    applied = next((f for f in application["per_file"] if f["file"] == PARENT), None)
    if applied is None:
        raise Stop(f"the split-application artifact carries no {PARENT}")

    pinned_lines = git_show(PINNED_COMMIT, PARENT).splitlines(keepends=True)

    # The head cut, derived: everything before the file's FIRST dated entry is its title and its
    # banner, and neither is residue. Naming them would be a hand-listed exemption.
    first_dated = next((n for n, line in enumerate(pinned_lines, 1) if ENTRY.match(line)), None)
    if first_dated is None:
        raise Stop(f"{PARENT} at the pin carries no dated entry at all — the head cut cannot be "
                   f"derived and the residue would be the whole file")

    moved_by_the_split = {(r["first_line_at_the_pin"], r["last_line_at_the_pin"])
                          for r in applied["the_moved"]}

    residue, head = [], []
    for span in per_file["the_spans"]:
        key = (span["first_line"], span["last_line"])
        if span["the_class"] != spans.OPERATIVE:
            continue
        (residue if span["first_line"] >= first_dated else head).append(span)

    for span in residue:
        key = (span["first_line"], span["last_line"])
        if key in moved_by_the_split:
            raise Stop(f"{PARENT} lines {key[0]}-{key[1]} is in the split's own moved set AND in "
                       f"this act's candidate set — the same span would move twice")

    accounted = len(moved_by_the_split) + len(residue) + len(head)
    if accounted != per_file["spans"]:
        raise Stop(f"the split's moved set ({len(moved_by_the_split)}), this act's candidates "
                   f"({len(residue)}) and the file's head ({len(head)}) account for {accounted} "
                   f"spans against a decomposition of {per_file['spans']} — the residue is not the "
                   f"complement it claims to be")

    unverdicted = [(s["first_line"], s["last_line"]) for s in residue
                   if (s["first_line"], s["last_line"]) not in VERDICTS]
    if unverdicted:
        raise Stop(f"candidate(s) with no authored reading verdict: {unverdicted} — Ruling 3 binds "
                   f"this act to READ every entry before it moves, so an unread candidate halts it")
    carried = {(s["first_line"], s["last_line"]) for s in residue}
    stray = sorted(k for k in VERDICTS if k not in carried)
    if stray:
        raise Stop(f"authored verdict(s) naming a span the residue does not carry: {stray} — the "
                   f"verdicts and the measurement have drifted apart")

    rows = []
    for span in residue:
        key = (span["first_line"], span["last_line"])
        verdict, why = VERDICTS[key]
        text = "".join(pinned_lines[key[0] - 1:key[1]])
        rows.append({
            "first_line_at_the_pin": key[0],
            "last_line_at_the_pin": key[1],
            "the_class_the_measurement_gave_it": span["the_class"],
            "characters": len(text),
            "the_verdict": verdict,
            "why": why,
            "how_the_verdict_was_made": "authored per span, read in the file itself (A3)",
            "the_opening": span["the_opening"],
            "text_sha256": sha(text),
            "_text": text,
        })
    bounds = {
        "the_first_dated_entry_at_the_pin": first_dated,
        "spans_the_decomposition_carries": per_file["spans"],
        "moved_by_the_split": len(moved_by_the_split),
        "the_files_head_before_the_first_dated_entry": len(head),
        "candidates": len(residue),
    }
    return rows, bounds


THE_POINTER = (
    f"*★ ARCHIVED {ACT_DATE}, THE SECOND ACT — the dated entries that PREDATE (or paraphrase) the "
    f"OI-222 pointer convention fell to `operative-rule-text` in the pinned measurement and stayed "
    f"when the block above was cleared. They were READ one by one and moved verbatim to "
    f"`STATUS_ARCHIVE.md` by `{DISPATCH}` Task 1, under Ruling 3 of `{RULINGS}`, which brings them "
    f"under Ruling 4's own line. **One candidate did NOT move and is flagged:** the navigational "
    f"paragraph at the foot of this file is not a completed batch's dated record but a live "
    f"pointer to the archive and to the gate policy, so the read-before-move safeguard left it at "
    f"site. The per-entry reconciliation is re-derived by "
    f"`tools/audit/gen_status_residue_move.py --check`.*\n"
)

ARCHIVE_HEADER = (
    f"> **★ THE PRE-CONVENTION RESIDUE, {ACT_DATE}.** The entries below are the dated `STATUS.md` "
    f"entries the executed split left at site — their own wording predates or paraphrases the "
    f"OI-222 pointer remedy, so the pinned measurement's recognizer did not place them and the "
    f"ruled doubt default kept them. They were moved verbatim by `{DISPATCH}` Task 1 under Ruling "
    f"3 of `{RULINGS}`, which brings them under Ruling 4 of `{SPLIT_RULINGS}`: *an entry is "
    f"SUPERSEDED the moment a later batch's close exists, and the site keeps only the latest "
    f"batch's entries.* **Each was READ before it moved**, and the one candidate that does not "
    f"read as a completed batch's dated record was left at site and flagged. They appear here in "
    f"the order they stood in the parent. Nothing was edited in transit; the reconciliation is "
    f"re-derived by `tools/audit/gen_status_residue_move.py --check`.\n\n"
)


def apply_move() -> None:
    rows, _bounds = candidates()
    moving = [r for r in rows if r["the_verdict"] == MOVE]
    if not moving:
        raise Stop("no candidate carries a MOVE verdict — moving nothing silently would leave "
                   "Ruling 3 unmet without saying so")

    live = read(PARENT)
    archive = read(COMPANION)
    for rec in moving:
        if rec["_text"] in archive:
            raise Stop(f"an entry is already in {COMPANION} — the move has run (pin lines "
                       f"{rec['first_line_at_the_pin']}-{rec['last_line_at_the_pin']})")
        if live.count(rec["_text"]) != 1:
            raise Stop(f"the entry at pin lines {rec['first_line_at_the_pin']}-"
                       f"{rec['last_line_at_the_pin']} occurs {live.count(rec['_text'])} time(s) "
                       f"in the live {PARENT} — the file has changed under the act and the move "
                       f"would not be byte-faithful")

    # The clearing pointer the split left is where this act's own pointer goes: Ruling 3's
    # "beside the existing clearing pointer", located by its own text rather than by a line.
    clearing = git_show(BASE_COMMIT, PARENT)
    marker = next((line for line in clearing.splitlines(keepends=True)
                   if line.startswith("*★ ARCHIVED ") and "Ruling 4" in line), None)
    if marker is None or live.count(marker) != 1:
        raise Stop("the split's clearing pointer is not present exactly once in the live file, so "
                   "this act's pointer has no anchored place to go")

    block = "".join(rec["_text"] + "\n" for rec in moving)
    for rec in moving:
        # The entry and the blank line that separated it travel together, so the must-read is not
        # left with a run of blank lines where the block stood.
        live = live.replace(rec["_text"] + "\n", "", 1)
    live = live.replace(marker, marker + "\n" + THE_POINTER, 1)
    write(PARENT, live)
    write(COMPANION, archive.rstrip("\n") + "\n\n" + ARCHIVE_HEADER + block)


def build() -> dict:
    rows, bounds = candidates()
    live = read(PARENT)
    archive = read(COMPANION)
    moving = [r for r in rows if r["the_verdict"] == MOVE]
    stayed = [r for r in rows if r["the_verdict"] != MOVE]
    in_archive = all(archive.count(r["_text"]) == 1 for r in moving)
    gone_from_live = all(r["_text"] not in live for r in moving)
    still_at_site = all(live.count(r["_text"]) == 1 for r in stayed)
    return {
        "what_this_is":
            "THE PRE-CONVENTION `STATUS.md` RESIDUE, MOVED UNDER RULING 4's OWN LINE: which "
            "candidate moved, which was LEFT AT SITE by the reading Ruling 3 requires, and the "
            "mechanical proof that nothing was lost or altered in transit (#12). Every figure "
            "here is computed; none is transcribed (D-431).",
        "generated_by": "tools/audit/gen_status_residue_move.py",
        "dispatch": f"{DISPATCH}, Task 1",
        "the_ruling": f"Ruling 3 of {RULINGS}: the dated entries the split left at site move to "
                      f"{COMPANION} under Ruling 4's own line, each entry READ before it moves, "
                      f"each move byte-faithful.",
        "measured_at_commit": PINNED_COMMIT,
        "base_commit": BASE_COMMIT,
        "★_why_the_population_is_the_pinned_measurement's_residue":
            "The executed split moved the spans the PINNED decomposition places in an archive "
            "class, so what it left behind is defined by that same measurement and by nothing "
            "else. Deriving the candidates as its complement — the operative-classed spans at or "
            "after the file's first dated entry — makes the two acts account for the file "
            "together, which is checked in both directions rather than asserted.",
        "the_reading_test_applied": READING_TEST,
        "★_what_this_act_does_NOT_establish":
            "That every moved entry's substance is carried elsewhere in full. What is established "
            "per entry is narrower and is what clause (2) asks: no rule, STOP, prohibition or "
            "live caveat whose ONLY home is that entry. The move is archive-with-record, so an "
            "entry's own substance remains readable at the companion whatever else is true.",
        "the_derivation_bounds": bounds,
        "candidates": len(rows),
        "entries_moved": len(moving),
        "left_at_site_by_the_reading": len(stayed),
        "characters_moved": sum(r["characters"] for r in moving),
        "characters_left_at_site_by_the_reading": sum(r["characters"] for r in stayed),
        "the_moved": [{k: v for k, v in r.items() if k != "_text"} for r in moving],
        "the_left_at_site": [{k: v for k, v in r.items() if k != "_text"} for r in stayed],
        "reconciliation": {
            f"every_moved_entry_is_byte_present_in_{COMPANION.replace('.', '_')}_exactly_once":
                in_archive,
            f"every_moved_entry_is_absent_from_{PARENT.replace('.', '_')}": gone_from_live,
            "every_entry_left_at_site_is_still_present_exactly_once": still_at_site,
            "what_that_proves_together":
                "Nothing left the must-read that is not in the archive; each entry was MOVED "
                "rather than copied; and the reading's flag was honoured rather than recorded and "
                "then overridden. All three are byte comparisons against the files at HEAD and "
                "against the git objects named by explicit hash — never against the memory of "
                "performing the move (#15).",
            "★_why_the_moved_text_is_read_from_a_git_object":
                "The entries are single lines of several thousand characters. Reading each from "
                "the pinned commit's own object and requiring exactly one occurrence in the live "
                "file makes the move byte-faithful by construction, and makes this check "
                "re-derive forever as later batches legitimately append their own entries — the "
                "OI-344 shape avoided by construction, on the precedent gen_status_archive_pass.py "
                "sets (D-646).",
        },
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--apply", action="store_true", help="perform the move (once)")
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
            print(f"FAIL: the residue move does not re-derive: {os.path.relpath(OUT, ROOT)}")
            return 1
    else:
        with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        print(f"wrote {os.path.relpath(OUT, ROOT)}")

    rec = art["reconciliation"]
    a = rec[f"every_moved_entry_is_byte_present_in_{COMPANION.replace('.', '_')}_exactly_once"]
    b = rec[f"every_moved_entry_is_absent_from_{PARENT.replace('.', '_')}"]
    c = rec["every_entry_left_at_site_is_still_present_exactly_once"]
    print(f"  candidates: {art['candidates']}, moved {art['entries_moved']}, "
          f"left at site by the reading {art['left_at_site_by_the_reading']}")
    print(f"  characters moved: {art['characters_moved']:,}")
    print(f"  byte-present in the companion exactly once: {a}")
    print(f"  absent from the must-read:                  {b}")
    print(f"  every flagged entry still at site:          {c}")
    return 0 if (a and b and c) else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Stop as exc:
        print(f"STOP: {exc}")
        sys.exit(2)
