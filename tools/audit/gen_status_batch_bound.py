#!/usr/bin/env python3
"""RULING 4's FORWARD BOUND — `STATUS.md` keeps only the latest batch's entries.

THE RULING THIS EXISTS FOR.  User, 2026-08-17, Ruling 4 of
`cowork_rulings_2026_08_17_governing_surface_split.md`: *"An entry is SUPERSEDED the moment a later
batch's close exists. The site keeps only the latest batch's entries."*  The backlog was cleared by
the executing dispatch (`gen_governing_surface_split.py`); **this tool is the FORWARD half** the
same ruling installs: *"every future batch close, in the same act that writes its own entries,
moves the then-previous batch's entries to the archive."*  It is an instance of the continuous-
pruning rule, §5(D) of `cowork_rulings_2026_08_16_preparation_return.md`.

WHY IT IS A TOOL AND NOT A HAND EDIT.  The entries are single lines of several thousand characters
each.  Retyping one to move it is the transcription the record forbids, and a move that is not
byte-faithful is exactly what #12 exists against.  So the text is never authored here: it is read
from the git OBJECT at the commit the move is performed on top of, matched in the live file, and
moved whole.

WHAT IS AUTHORED AND WHAT IS DERIVED.
  authored : the commit the act is performed on top of, and WHICH batch is the then-previous one —
             named by its dispatch, because that is what each entry says of itself.
  derived  : which entries move, from the entries' own text at that commit.  No line number, no
             count and no entry text is authored.

THE STOPS:
  * a dispatch that names NO entry at the base commit — the batch cannot be identified, and moving
    nothing silently would leave the bound unmet without saying so;
  * a moved entry not present verbatim in the live file when the move is applied — the file has
    changed under the act;
  * an entry that is already in the archive — the move has run.

Run:
    python tools/audit/gen_status_batch_bound.py --apply    # perform the move once
    python tools/audit/gen_status_batch_bound.py --check    # re-derive the reconciliation
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
from output_encoding import use_utf8_output      # noqa: E402  (path set above)
from gen_status_archive_pass import ENTRY        # noqa: E402  the ONE dated-entry pattern (#6)
from gen_governing_surface_split import PREFIX_ADJUSTMENT   # noqa: E402  the ONE declared shift (#6)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

OUT = os.path.join(HERE, "status_batch_bound.json")

# The commit this move is performed on top of: the last task commit of the executing dispatch,
# pushed before the close began. An explicit hash, which is the only git read D-253 permits.
#
# ★ THE FORWARD BOUND IS APPLIED ONCE PER BATCH, AND EXACTLY THREE INPUTS MOVE WITH IT — the base
# commit, the then-previous batch and the executing act. Nothing else about this tool changes, and
# every previous aiming is recorded rather than overwritten (#12): a reader can see the bound being
# maintained rather than a value that keeps changing for no stated reason.
BASE_COMMIT = "e36168ec3333f06b4f2752d872f9169cbbe26562"

# The THEN-PREVIOUS batch, named by its dispatch because that is what each of its entries says of
# itself. Ruling 4's forward bound moves exactly these, in the act that writes this batch's own.
PREVIOUS_BATCH_DISPATCH = "cc_instruction_preparation_eighth.md"

ACT_DATE = "2026-08-17"
DISPATCH = "cc_instruction_preparation_ninth.md"
TASK = "Task 5"
RULINGS = "cowork_rulings_2026_08_17_governing_surface_split.md"

# Every aiming this tool has had, oldest first. Authored, and kept rather than replaced.
PREVIOUS_AIMINGS = [
    {"executing_act": "cc_instruction_preparation_sixth.md, Task 1",
     "base_commit": "1f84f5d62107bde86ddd09317282be1642feb9da",
     "the_then_previous_batch": "the backlog, cleared by gen_governing_surface_split.py"},
    {"executing_act": "cc_instruction_preparation_seventh.md, Task 2",
     "base_commit": "cfb69a7ecb21351382b25206616a0349214e44f8",
     "the_then_previous_batch": "cc_instruction_preparation_sixth.md"},
    {"executing_act": "cc_instruction_preparation_eighth.md, Task 5",
     "base_commit": "a21a55fc125fa58531b724f22918b29f0a1d0efc",
     "the_then_previous_batch": "cc_instruction_preparation_seventh.md"},
]

ARCHIVE_HEADER = (
    f"> **★ RULING 4's FORWARD BOUND, {ACT_DATE}.** The entries below are the PREVIOUS batch's "
    f"(`{PREVIOUS_BATCH_DISPATCH}`), moved verbatim out of `STATUS.md` by `{DISPATCH}` {TASK} in "
    f"the same act that wrote this batch's own entries — Ruling 4 of `{RULINGS}`: *an entry is "
    f"SUPERSEDED the moment a later batch's close exists, and the site keeps only the latest "
    f"batch's entries.* Nothing was edited in transit; the reconciliation is re-derived by "
    f"`tools/audit/gen_status_batch_bound.py --check`.\n\n"
)


class Stop(Exception):
    """A demand of the forward bound is unmet. Never a warning, never a retyped entry."""


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


# A batch writes ONE entry naming its dispatch — the close — and one per earlier task saying
# "Same dispatch" instead of repeating the name. Both halves are the entries' OWN words, so
# membership is DERIVED and nothing is listed by hand. This is the same shape
# `gen_status_archive_pass.py` had to author a clause for; here it is derived instead.
SAME_DISPATCH = "Same dispatch"


def moved_entries() -> list[dict]:
    """The then-previous batch's entries, read from the base commit's own git object.

    A batch's entries are the one naming its dispatch, plus the run of dated entries immediately
    below it whose own text says `Same dispatch` — which is what those entries mean and how the
    record writes them. The run stops at the first dated entry that says neither.
    """
    base = git_show(BASE_COMMIT, "STATUS.md")
    dated = [(n, line) for n, line in enumerate(base.splitlines(keepends=True), 1)
             if ENTRY.match(line)]
    named = [i for i, (_, line) in enumerate(dated) if PREVIOUS_BATCH_DISPATCH in line]
    if not named:
        raise Stop(f"no dated entry at {BASE_COMMIT[:10]} names {PREVIOUS_BATCH_DISPATCH} — the "
                   f"then-previous batch cannot be identified, and moving nothing silently would "
                   f"leave Ruling 4's forward bound unmet without saying so")
    members = sorted(set(named))
    i = max(named) + 1
    while i < len(dated) and SAME_DISPATCH in dated[i][1]:
        members.append(i)
        i += 1
    # ★ THE ONE DECLARED TEXTUAL ADJUSTMENT, IMPORTED RATHER THAN RESTATED (#6). The newest entry
    # of a batch carries the `Last updated: ` prefix; the NEXT batch's close writes its own entries
    # above it and the prefix moves to the newest of those, so the entry this act must find in the
    # live file differs from the base commit's by exactly that prefix and nothing else. The split
    # tool met the same shift and declared the same constant; it is imported here rather than
    # re-decided. Any entry needing a SECOND adjustment is a STOP, not a second constant: the
    # occurrence test below fires on it.
    out = []
    for i in members:
        text = dated[i][1]
        adjusted = False
        if PREFIX_ADJUSTMENT in text:
            text = text.replace(PREFIX_ADJUSTMENT, "", 1)
            adjusted = True
        out.append({"line_at_base": dated[i][0], "characters": len(text),
                    "sha256": sha(text),
                    "membership": ("names the dispatch" if PREVIOUS_BATCH_DISPATCH in dated[i][1]
                                   else "says `Same dispatch`, in the run below the entry that "
                                        "names it"),
                    "the_one_declared_adjustment_applied": adjusted,
                    "opening": text[:150].rstrip("\r\n"),
                    "_text": text})
    return out


def apply_move() -> None:
    entries = moved_entries()
    live = read("STATUS.md")
    archive = read("STATUS_ARCHIVE.md")
    for rec in entries:
        if rec["_text"] in archive:
            raise Stop(f"an entry is already in STATUS_ARCHIVE.md — the move has run "
                       f"(line {rec['line_at_base']} at the base commit)")
        if live.count(rec["_text"]) != 1:
            raise Stop(f"the entry at base line {rec['line_at_base']} occurs "
                       f"{live.count(rec['_text'])} time(s) in the live STATUS.md — the file has "
                       f"changed under the act and the move is not byte-faithful")
    block = "".join(rec["_text"] + "\n" for rec in entries)
    for rec in entries:
        # The entry and the blank line that separated it travel together, so the must-read is not
        # left with a run of blank lines where the block stood.
        live = live.replace(rec["_text"] + "\n", "", 1)
    write("STATUS.md", live)
    write("STATUS_ARCHIVE.md", archive.rstrip("\n") + "\n\n" + ARCHIVE_HEADER + block)


def build() -> dict:
    entries = moved_entries()
    live = read("STATUS.md")
    archive = read("STATUS_ARCHIVE.md")
    in_archive = all(archive.count(r["_text"]) == 1 for r in entries)
    gone_from_live = all(r["_text"] not in live for r in entries)
    return {
        "what_this_is":
            "RULING 4's FORWARD BOUND, applied at one batch close: which of the then-previous "
            "batch's STATUS.md entries moved to the archive, and the mechanical proof that nothing "
            "was lost or altered in transit (#12). Every figure here is computed; none is "
            "transcribed (D-431).",
        "generated_by": "tools/audit/gen_status_batch_bound.py",
        "dispatch": f"{DISPATCH}, {TASK}",
        "★_every_previous_aiming_of_this_tool_kept_rather_than_replaced": PREVIOUS_AIMINGS,
        "the_ruling": f"Ruling 4 of {RULINGS}: an entry is SUPERSEDED the moment a later batch's "
                      f"close exists; the site keeps only the latest batch's entries, and every "
                      f"future batch close moves the then-previous batch's entries in the same act "
                      f"that writes its own.",
        "base_commit": BASE_COMMIT,
        "the_then_previous_batch": PREVIOUS_BATCH_DISPATCH,
        "entries_moved": len(entries),
        "characters_moved": sum(r["characters"] for r in entries),
        "the_moved": [{k: v for k, v in r.items() if k != "_text"} for r in entries],
        "reconciliation": {
            "every_moved_entry_is_byte_present_in_STATUS_ARCHIVE_md_exactly_once": in_archive,
            "every_moved_entry_is_absent_from_STATUS_md": gone_from_live,
            "what_that_proves_together":
                "Nothing left the must-read that is not in the archive, and each entry was MOVED "
                "rather than copied. Both are byte comparisons against the file at HEAD and "
                "against the git object at the base commit named by explicit hash — never against "
                "the memory of performing the move (#15).",
            "★_why_the_moved_set_is_read_from_a_git_object":
                "The set is a statement about the file as it stood when the act ran. Reading it "
                "from the base commit's own object makes this check re-derive forever as later "
                "batches legitimately append their own entries — the OI-344 shape avoided by "
                "construction, on the precedent gen_status_archive_pass.py sets (D-646).",
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
            print(f"FAIL: the forward bound does not re-derive: {os.path.relpath(OUT, ROOT)}")
            return 1
    else:
        with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        print(f"wrote {os.path.relpath(OUT, ROOT)}")

    rec = art["reconciliation"]
    a = rec["every_moved_entry_is_byte_present_in_STATUS_ARCHIVE_md_exactly_once"]
    b = rec["every_moved_entry_is_absent_from_STATUS_md"]
    print(f"  entries moved: {art['entries_moved']}, {art['characters_moved']:,} characters")
    print(f"  byte-present in the archive exactly once: {a}")
    print(f"  absent from the must-read:                {b}")
    return 0 if (a and b) else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Stop as exc:
        print(f"STOP: {exc}")
        sys.exit(2)
