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
BASE_COMMIT = "1d213b19b618aa1d148a7777460c48f37fd5de68"

# The THEN-PREVIOUS batch, named by its dispatch because that is what each of its entries says of
# itself. Ruling 4's forward bound moves exactly these, in the act that writes this batch's own.
PREVIOUS_BATCH_DISPATCH = "cc_instruction_framework_arrangement_landing.md"

ACT_DATE = "2026-08-28"
DISPATCH = "cc_instruction_informed_brief_landing.md"
# TASK IS A CHOICE, DECLARED RATHER THAN IMPLIED. The executing dispatch orders the move and this
# batch's own `STATUS.md` entries in the same numbered task — its Task 1, item 1 — so both halves
# of "the same act that writes its own entries" sit inside Task 1, and Task 1 is what the archive
# header names. No sub-item is carried, because the header names an act rather than a sub-step and
# every previous aiming names a whole task.
TASK = "Task 1"
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
    {"executing_act": "cc_instruction_preparation_ninth.md, Task 5",
     "base_commit": "e36168ec3333f06b4f2752d872f9169cbbe26562",
     "the_then_previous_batch": "cc_instruction_preparation_eighth.md"},
    {"executing_act": "cc_instruction_preparation_tenth.md, Task 5",
     "base_commit": "30d44165cf12fcb462ed11225b024b4a86bd17c6",
     "the_then_previous_batch": "cc_instruction_preparation_ninth.md"},
    {"executing_act": "cc_instruction_preparation_eleventh_amended.md, Task 5",
     "base_commit": "3a37c5d06901821eaed3224865a5bcc57630c883",
     "the_then_previous_batch": "cc_instruction_preparation_tenth.md"},
    {"executing_act": "cc_instruction_preparation_twelfth.md, Task 5",
     "base_commit": "18127bab0160d21aa0ced9170a9fe3c968888673",
     "the_then_previous_batch": "cc_instruction_preparation_eleventh_amended.md"},
    {"executing_act": "cc_instruction_preparation_thirteenth.md, Task 3",
     "base_commit": "a33a933404507c855201c35e36df23b38470946f",
     "the_then_previous_batch": "cc_instruction_preparation_twelfth.md"},
    {"executing_act": "cc_instruction_preparation_fourteenth.md, Task 2",
     "base_commit": "ac6cacec9fb0c1f64128da87704e6e0d94e1323c",
     "the_then_previous_batch": "cc_instruction_preparation_thirteenth.md"},
    {"executing_act": "cc_instruction_successor_plan_landing_and_step_zero.md, Task 4",
     "base_commit": "553dd5f40589bed6eb1e9fc64233a4fde7096c06",
     "the_then_previous_batch": "cc_instruction_preparation_fourteenth.md"},
    {"executing_act": "cc_instruction_step_zero_exclusion_and_pass_continuation.md, Task 3",
     "base_commit": "311dee8d11d323c1cc126fc9e0a3f72be04d20aa",
     "the_then_previous_batch": "cc_instruction_successor_plan_landing_and_step_zero.md"},
    {"executing_act": "cc_instruction_pass_continuation_second.md, Task 2",
     "base_commit": "3e9410bfd79e0c2bf2328f9a3c35fa7f22aea87d",
     "the_then_previous_batch": "cc_instruction_step_zero_exclusion_and_pass_continuation.md"},
    {"executing_act": "cc_instruction_pilot_preparation_withheld_family.md, Task 2",
     "base_commit": "a12cc0350322dd286708dcbf19d95548b01f7d55",
     "the_then_previous_batch": "cc_instruction_pass_continuation_second.md"},
    {"executing_act": "cc_instruction_withheld_family_correction.md, Task 2",
     "base_commit": "72534e5da90e5924f889f90a01547d34194c1951",
     "the_then_previous_batch": "cc_instruction_pilot_preparation_withheld_family.md"},
    {"executing_act": "cc_instruction_second_passage_withheld.md, Task 2",
     "base_commit": "cf00b6af7b89a6599c610b31bc9f47b639ccb217",
     "the_then_previous_batch": "cc_instruction_withheld_family_correction.md"},
    {"executing_act": "cc_instruction_brief_ratification_and_readme_boundary.md, Task 2",
     "base_commit": "a3ed95077697de6f75e46ecc0a0183346e6e823e",
     "the_then_previous_batch": "cc_instruction_second_passage_withheld.md"},
    {"executing_act": "cc_instruction_blind_output_landing.md, Task 1",
     "base_commit": "95c17e6660cb230676b44da339a2c9e87653c21c",
     "the_then_previous_batch": "cc_instruction_brief_ratification_and_readme_boundary.md"},
    {"executing_act": "cc_instruction_comparison_harmony_boundary.md, Task 2",
     "base_commit": "5b994124f2d193742d4c9ca2e25f85625cd9c733",
     "the_then_previous_batch": "cc_instruction_blind_output_landing.md"},
    {"executing_act": "cc_instruction_sizing_pack_preparation.md, Task 2",
     "base_commit": "7c1119dcdbb3c5466652516a95b2eda819ce9a38",
     "the_then_previous_batch": "cc_instruction_comparison_harmony_boundary.md"},
    {"executing_act": "cc_instruction_manifest_prose_and_sizing_brief.md, Task 2",
     "base_commit": "e1946429d22265ccbc9aad8a23611a9789431c20",
     "the_then_previous_batch": "cc_instruction_sizing_pack_preparation.md"},
    {"executing_act": "cc_instruction_sizing_brief_ruled.md, Task 1",
     "base_commit": "7f6f72d85873b93a39f956e0ce3366c4f85fcc28",
     "the_then_previous_batch": "cc_instruction_manifest_prose_and_sizing_brief.md"},
    {"executing_act": "cc_instruction_sizing_output_landing.md, Task 1",
     "base_commit": "0a6ccc75b4026ea8c9b47a76698481e1800a2a6f",
     "the_then_previous_batch": "cc_instruction_sizing_brief_ruled.md"},
    # ★ BACKFILLED 2026-08-26 by `cc_instruction_amendment_landing.md` Task 7, on Ruling 5 of
    # `cowork_rulings_2026_08_26_amendment_landing_sitting.md`. This move was performed WITHOUT
    # this tool: the executing dispatch forbade every edit to a tool source by name, and re-aiming
    # this one is such an edit, so the move was taken from the committed object by hand and
    # declared at the archive block itself. The row is written here so the tool's record of
    # aimings — kept rather than replaced (#12) — no longer omits a move that happened, and the
    # extra field says what the three-field rows would otherwise imply falsely (#10).
    {"executing_act": "cc_instruction_register_reconciliation.md, Task 4",
     "base_commit": "0a2675855c5a92fc2e32cd55c05281ba4d2c24e6",
     "the_then_previous_batch": "cc_instruction_sizing_output_landing.md",
     "★_not_performed_by_this_tool":
         "Performed by hand from the committed object, byte-faithfully, because the executing "
         "dispatch forbade editing any tool source and this tool's per-batch re-aiming is such an "
         "edit. The departure was declared at the STATUS_ARCHIVE.md block the move wrote and is "
         "reported at `cc_report_register_reconciliation.md` §5.3 and §5.4. Backfilled here on "
         "Ruling 5 of `cowork_rulings_2026_08_26_amendment_landing_sitting.md`, which also names "
         "the re-aiming a carve-out from that bar so the conflict cannot recur."},
    {"executing_act": "cc_instruction_amendment_landing.md, Task 7",
     "base_commit": "2d7c3c3119e92dadb7b8fbffa76403ef5c7b6f5f",
     "the_then_previous_batch": "cc_instruction_register_reconciliation.md"},
    {"executing_act": "cc_instruction_boot_pack_regeneration.md, Task 4",
     "base_commit": "68c42b7f7743c02bdebefacdd9ed06ca9060fbbe",
     "the_then_previous_batch": "cc_instruction_amendment_landing.md"},
    {"executing_act": "cc_instruction_sizing_tests.md, Task 7",
     "base_commit": "9683a9c1fe351cde4450bfe63c86d2331a83946b",
     "the_then_previous_batch": "cc_instruction_boot_pack_regeneration.md"},
    {"executing_act": "cc_instruction_ledger_build.md, Task 5",
     "base_commit": "4bc362c57e300688a28617a764f97f98e9df836e",
     "the_then_previous_batch": "cc_instruction_sizing_tests.md"},
    {"executing_act": "cc_instruction_ledger_admissions.md, Task 5",
     "base_commit": "550ffc28cd80b52aa8d0e6f8a88925b8b3cf2de0",
     "the_then_previous_batch": "cc_instruction_ledger_build.md"},
    {"executing_act": "cc_instruction_placement_sample.md, Task 5",
     "base_commit": "9053861b9cc71d8de8dc9c12105abd553620b55a",
     "the_then_previous_batch": "cc_instruction_ledger_admissions.md"},
    {"executing_act": "cc_instruction_placement_sample_redraw.md, Task 6",
     "base_commit": "ec9034011857c223e2eb44ecbb210811908edc61",
     "the_then_previous_batch": "cc_instruction_placement_sample.md"},
    {"executing_act": "cc_instruction_unit_correction_redraw.md, Task 6",
     "base_commit": "7c32f37fb36c55e16e3504d45934fb692a39be04",
     "the_then_previous_batch": "cc_instruction_placement_sample_redraw.md"},
    {"executing_act": "cc_instruction_framework_pack_preparation.md, Task 2",
     "base_commit": "85e0b8da162a5b937f4a4be0f033f5c7d281eddf",
     "the_then_previous_batch": "cc_instruction_unit_correction_redraw.md"},
    {"executing_act": "cc_instruction_framework_arrangement_landing.md, Task 3",
     "base_commit": "722c7327a9472436cdc43a9ffc0dd4eb1533823a",
     "the_then_previous_batch": "cc_instruction_framework_pack_preparation.md"},
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
