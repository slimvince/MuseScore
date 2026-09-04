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
#
# ★ RE-AIMED 2026-09-02 by `cc_instruction_comparison_l0_l1_second_2026_09_02.md` Task 3, the
# per-batch re-aiming this tool's own carve-out provides for. The PREVIOUS aiming is recorded rather
# than overwritten (#12): base commit `ae2adfc6270aee98f18c0e1d553abb796523397a`, then-previous batch
# `cc_instruction_reading_pass_landing_second_2026_08_31.md`, act date 2026-09-02 — that move RAN,
# and this tool's own already-in-the-archive STOP is what established that it had before this
# re-aiming was made.
#
# ★★ AND THE PREVIOUS RE-AIMING WAS INCOMPLETE, WHICH IS RECORDED HERE RATHER THAN LEFT TO BE
# REDISCOVERED. Four fields are authored, and the 2026-09-02 re-aiming moved only TWO of them:
# `BASE_COMMIT` and `PREVIOUS_BATCH_DISPATCH` were re-aimed, while `DISPATCH` and `TASK` were left
# naming the THEN-PREVIOUS batch. So the archive header that move wrote states that the entries were
# moved "by `cc_instruction_reading_pass_landing_second_2026_08_31.md` Task 5" when the act was in
# fact `cc_instruction_comparison_l0_l1_2026_09_02.md` Task 3 — a header that misattributes its own
# act. **The block already written into `STATUS_ARCHIVE.md` is NOT edited by this batch**: it is a
# previous batch's record, this dispatch bars moving or rewriting an archived document, and a
# correction there would rewrite what another act did rather than record it. What this batch does is
# name the defect here, re-aim all FOUR fields, and report it. The comment at `ACT_DATE` below is
# corrected in the same act, its former reasoning having been written for a batch whose dispatch date
# and run date agreed.
#
# ★★★ RE-AIMED 2026-09-03 by `cc_instruction_comparison_l0_l1_fourth_2026_09_03.md` Task 2, and ALL
# FIVE authored inputs moved together — the fifth being `PREVIOUS_AIMINGS`, which is appended to
# rather than replaced (#12). **The aiming this replaces is the one the THIRD writing could not use.**
# That batch re-aimed these fields as its own dispatch ordered, ran the tool, and it STOPped: the
# then-previous batch's two `STATUS.md` entries name no dispatch at all, so `moved_entries()` cannot
# identify them by the key it derives from. That batch then REVERTED the re-aiming and re-ran the tool
# to prove it green, so no guard red was introduced and the constants below stood at the second
# writing's aiming until this act. Both facts are rowed in `PREVIOUS_AIMINGS` below — the second
# writing's aiming as superseded, and the third writing's non-move with the tool's own STOP message
# quoted — so the record of aimings does not silently omit a batch (#10, #12).
#
# ★★★★ RE-AIMED AGAIN 2026-09-03 by `cc_instruction_comparison_l0_l1_fifth_2026_09_03.md` Task 4 — the
# application act's close — and again ALL FIVE authored inputs moved together, `PREVIOUS_AIMINGS` being
# appended to rather than replaced (#12). The aiming this replaces is the FOURTH writing's, which RAN
# and moved the third writing's two entries exactly as its own dispatch predicted. `BASE_COMMIT` is
# this batch's LAST TASK COMMIT — Task 3, the reading file's re-marking — per this tool's docstring;
# the then-previous batch is the fourth comparison dispatch, whose close entry names it and whose
# second entry says `Same dispatch`. **The second writing's two nameless entries remain in `STATUS.md`
# and no aiming of this tool can identify them**, as the row for the third writing below records; that
# is a declared state and not a STOP.
#
# ★★★★★ RE-AIMED AGAIN 2026-09-03 by `cc_instruction_comparison_l0_l1_sixth_2026_09_03.md` Task 2 —
# the ratification act's close — and again ALL FIVE authored inputs moved together, `PREVIOUS_AIMINGS`
# being appended to rather than replaced (#12). The aiming this replaces is the FIFTH writing's, which
# RAN and moved the fourth writing's two entries exactly as its own dispatch predicted. `BASE_COMMIT`
# is this batch's LAST TASK COMMIT — Task 1, the corrections to the derived specification — per this
# tool's docstring; the then-previous batch is the fifth comparison dispatch, whose close entry names
# it and whose four entries below it say `Same dispatch`, so FIVE entries are expected to move. **The
# second writing's two nameless entries remain in `STATUS.md` and no aiming of this tool can identify
# them**, as the row for the third writing below records; that is a declared state and not a STOP.
#
# ★★★★★★ RE-AIMED AGAIN 2026-09-03 by `cc_instruction_comparison_l0_l1_seventh_2026_09_03.md` Task 3
# — the family-placements close — and again ALL FIVE authored inputs moved together,
# `PREVIOUS_AIMINGS` being appended to rather than replaced (#12). The aiming this replaces is the
# SIXTH writing's, which RAN and moved the fifth writing's five entries exactly as its own dispatch
# predicted. `BASE_COMMIT` is this batch's LAST TASK COMMIT — Task 2, S-48's anchor named as Ruling 42
# orders — per this tool's docstring; the then-previous batch is the sixth comparison dispatch, whose
# close entry names it and whose two entries below it say `Same dispatch`, so THREE entries are
# expected to move. **The second writing's two nameless entries remain in `STATUS.md` and no aiming of
# this tool can identify them**, as the row for the third writing below records; that is a declared
# state and not a STOP.
#
# ★★★★★★★ RE-AIMED AGAIN 2026-09-04 by `cc_instruction_comparison_l0_l1_eighth_2026_09_04.md` Task 2
# — the Row 4.3 placement's close — and again ALL FIVE authored inputs moved together,
# `PREVIOUS_AIMINGS` being appended to rather than replaced (#12). The aiming this replaces is the
# SEVENTH writing's, which RAN and moved the sixth writing's three entries exactly as its own dispatch
# predicted. `BASE_COMMIT` is this batch's LAST TASK COMMIT — Task 1, Row 4.3 placed QUARANTINED under
# Ruling 78 — per this tool's docstring; the then-previous batch is the seventh comparison dispatch,
# whose close entry names it and whose three entries below it say `Same dispatch`, so FOUR entries are
# expected to move. **The second writing's two nameless entries remain in `STATUS.md` and no aiming of
# this tool can identify them**, as the row for the third writing below records; that is a declared
# state and not a STOP.
#
# ★★★★★★★★ RE-AIMED AGAIN 2026-09-04 by `cc_instruction_comparison_l0_l1_ninth_2026_09_04.md` Task 2
# — the additive repair of §11 and §12's close — and again ALL FIVE authored inputs moved together,
# `PREVIOUS_AIMINGS` being appended to rather than replaced (#12). The aiming this replaces is the
# EIGHTH writing's, which RAN and moved the seventh writing's four entries exactly as its own dispatch
# predicted. `BASE_COMMIT` is this batch's LAST TASK COMMIT — Task 1, the two added subsections and the
# two corrected opening claims — per this tool's docstring; the then-previous batch is the eighth
# comparison dispatch, whose close entry names it and whose two entries below it say `Same dispatch`,
# so THREE entries are expected to move. **The second writing's two nameless entries remain in
# `STATUS.md` and no aiming of this tool can identify them**, as the row for the third writing below
# records; that is a declared state and not a STOP.
#
# ★★★★★★★★★ RE-AIMED AGAIN 2026-09-04 by `cc_instruction_comparison_l0_l1_tenth_2026_09_04.md` Task 2
# — the close of the act that gave the four quarantined rows of the per-note field list their audit
# questions under Ruling 80 — and again ALL FIVE authored inputs moved together, `PREVIOUS_AIMINGS`
# being appended to rather than replaced (#12). The aiming this replaces is the NINTH writing's, which
# RAN and moved the eighth writing's three entries exactly as its own dispatch predicted. `BASE_COMMIT`
# is this batch's LAST TASK COMMIT — Task 1, the five sentence replacements inside §11's added
# subsection — per this tool's docstring; the then-previous batch is the ninth comparison dispatch,
# whose close entry names it and whose two entries below it say `Same dispatch`, so THREE entries are
# expected to move. **The second writing's two nameless entries remain in `STATUS.md` and no aiming of
# this tool can identify them**, as the row for the third writing below records; that is a declared
# state and not a STOP.
BASE_COMMIT = "c810f5ad74648a882d0da231abad4a92066e3ad2"

# The THEN-PREVIOUS batch, named by its dispatch because that is what each of its entries says of
# itself. Ruling 4's forward bound moves exactly these, in the act that writes this batch's own.
PREVIOUS_BATCH_DISPATCH = "cc_instruction_comparison_l0_l1_ninth_2026_09_04.md"

# ★ THE ACT DATE IS THE DAY THE MOVE RAN, NOT THE DAY THE DISPATCH WAS WRITTEN. This executing
# dispatch is dated 2026-09-04 and this batch ran on 2026-09-04, so the two agree; the field is kept
# authored rather than inferred because the archive header states when the ACT happened, and a header
# carrying a dispatch's date would say something false about the record (#10) on any batch where the
# two differ.
ACT_DATE = "2026-09-04"
DISPATCH = "cc_instruction_comparison_l0_l1_tenth_2026_09_04.md"
# TASK IS A CHOICE, DECLARED RATHER THAN IMPLIED. The executing dispatch orders the move and this
# batch's own `STATUS.md` entries in the same numbered task — for the tenth comparison dispatch that
# is its Task 2, whose item 1 orders the pointer entries and the forward bound together — so both halves
# of "the same act that writes its own entries" sit inside Task 2, and Task 2 is what the archive header
# names. No sub-item is carried, because the header names an act rather than a sub-step and every
# previous aiming names a whole task. *(This comment named Task 3 while the seventh comparison dispatch
# was the executing act, and Task 2 while the eighth and the ninth were, each correct then; the
# numbered task differs per dispatch and is re-stated with each re-aiming rather than left to be
# inferred.)*
TASK = "Task 2"
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
    {"executing_act": "cc_instruction_informed_brief_landing.md, Task 1",
     "base_commit": "1d213b19b618aa1d148a7777460c48f37fd5de68",
     "the_then_previous_batch": "cc_instruction_framework_arrangement_landing.md"},
    {"executing_act": "cc_instruction_arm_and_site_fillin.md, Task 3",
     "base_commit": "836ad8ba57ab22c89cdcd6a6d85b8fa2a70a2d0d",
     "the_then_previous_batch": "cc_instruction_informed_brief_landing.md"},
    {"executing_act": "cc_instruction_landing_2026_08_28.md, Task 2",
     "base_commit": "0e927c2db2f8241660e5c2711288e61fdd921d53",
     "the_then_previous_batch": "cc_instruction_arm_and_site_fillin.md"},
    {"executing_act": "cc_instruction_second_landing_2026_08_28.md, Task 2",
     "base_commit": "9735d8e9398b137a61ec0a20f34d994f9f61a0e1",
     "the_then_previous_batch": "cc_instruction_landing_2026_08_28.md"},
    {"executing_act": "cc_instruction_third_landing_2026_08_28.md, Task 2",
     "base_commit": "0396bb6a70a6ad983ee14c84d85e9201c8f7ef16",
     "the_then_previous_batch": "cc_instruction_second_landing_2026_08_28.md"},
    {"executing_act": "cc_instruction_phase_close_second_2026_08_30.md, Task 2",
     "base_commit": "3e75ef85bce5805eefee0f5015da59d88cc0582a",
     "the_then_previous_batch": "cc_instruction_third_landing_2026_08_28.md"},
    {"executing_act": "cc_instruction_reading_pass_landing_second_2026_08_31.md, Task 5",
     "base_commit": "b8e738448ea061a2212d82de454e46a55ecf6f8f",
     "the_then_previous_batch": "cc_instruction_phase_close_second_2026_08_30.md"},
    {"executing_act": "cc_instruction_comparison_l0_l1_2026_09_02.md, Task 3",
     "base_commit": "ae2adfc6270aee98f18c0e1d553abb796523397a",
     "the_then_previous_batch": "cc_instruction_reading_pass_landing_second_2026_08_31.md",
     "★_the_re_aiming_was_incomplete":
         "Only TWO of the four authored fields were moved — `BASE_COMMIT` and "
         "`PREVIOUS_BATCH_DISPATCH`. `DISPATCH` and `TASK` were left naming the THEN-PREVIOUS batch "
         "(`cc_instruction_reading_pass_landing_second_2026_08_31.md`, Task 5), so the archive "
         "header that move wrote into `STATUS_ARCHIVE.md` states that the entries were moved by the "
         "batch whose entries were being moved. The header's DATE is right and its ATTRIBUTION is "
         "wrong. Found and recorded 2026-09-02 by "
         "`cc_instruction_comparison_l0_l1_second_2026_09_02.md` Task 3, which re-aimed all four "
         "fields; the already-written archive block was deliberately NOT edited — it is a previous "
         "batch's record, the executing dispatch bars rewriting an archived document, and recording "
         "the defect is what a later reader needs rather than a silently corrected header."},
    {"executing_act": "cc_instruction_comparison_l0_l1_second_2026_09_02.md, Task 3",
     "base_commit": "2acef005a99b829cb1c9ea173031fb6c3a4a1051",
     "the_then_previous_batch": "cc_instruction_comparison_l0_l1_2026_09_02.md"},
    # ★ RECORDED 2026-09-03 by `cc_instruction_comparison_l0_l1_fourth_2026_09_03.md` Task 2. This
    # row is written in the shape the backfilled 2026-08-26 row above uses, and for the same reason:
    # the three-field rows would otherwise imply falsely (#10) that every batch between two aimings
    # performed a move. THE THIRD WRITING PERFORMED NO MOVE. It re-aimed the fields as its own
    # dispatch ordered, ran the tool, measured the STOP, and then REVERTED the re-aiming and re-ran
    # the tool to prove it green — so no guard red was introduced and this file was byte-unchanged by
    # that batch. Rowed here so the record of aimings does not silently omit a batch (#12).
    {"executing_act": "cc_instruction_comparison_l0_l1_third_2026_09_02.md, Task 2",
     "base_commit": "e56e1153c0e08702e9e7ea51ff6ccf167aec0172",
     "the_then_previous_batch": "cc_instruction_comparison_l0_l1_second_2026_09_02.md",
     "★_no_move_was_performed":
         "The re-aiming this dispatch ordered was made and the tool run; it STOPped, in its own "
         "words, quoted from that batch's close in `cowork_away_returns.md`: `STOP: no dated entry "
         "at e56e1153c0 names cc_instruction_comparison_l0_l1_second_2026_09_02.md — the "
         "then-previous batch cannot be identified, and moving nothing silently would leave "
         "Ruling 4's forward bound unmet without saying so.` The cause, established at this file's "
         "source and at STATUS.md: membership is DERIVED from the dispatch name each entry carries, "
         "and the second writing's two entries name no dispatch at all, so no aiming of this tool "
         "can identify them. That batch reverted the re-aiming, re-ran the tool to prove it green, "
         "and declined to move the entries by hand or to edit another batch's entry text — both of "
         "which would have traded this tool's byte-proof for a hand copy or rewritten another act's "
         "record. It wrote its OWN two entries naming its dispatch, which is what makes THIS "
         "aiming's move possible. THE CONSEQUENCE, DECLARED AND STILL STANDING: the second "
         "writing's two entries have no mechanism that can retire them, and they remain in "
         "STATUS.md after this move as they did before it."},
    # ★ RECORDED 2026-09-03 by `cc_instruction_comparison_l0_l1_fifth_2026_09_03.md` Task 4. This is
    # the FOURTH writing's aiming, now superseded. Unlike the row immediately above it, that move RAN:
    # the tool was re-aimed at all five authored inputs, `--apply` moved the THIRD writing's two
    # entries to STATUS_ARCHIVE.md, and its own reconciliation came back green in both limbs — every
    # moved entry byte-present in the archive exactly once and absent from the must-read.
    {"executing_act": "cc_instruction_comparison_l0_l1_fourth_2026_09_03.md, Task 2",
     "base_commit": "b460ea2983818c4f8a077f29c901644b97bcf6e3",
     "the_then_previous_batch": "cc_instruction_comparison_l0_l1_third_2026_09_02.md"},
    # ★ RECORDED 2026-09-03 by `cc_instruction_comparison_l0_l1_sixth_2026_09_03.md` Task 2. This is
    # the FIFTH writing's aiming, now superseded. That move RAN: the tool was re-aimed at all five
    # authored inputs, `--apply` moved the FOURTH writing's two entries to STATUS_ARCHIVE.md, and its
    # own reconciliation came back green in both limbs — every moved entry byte-present in the archive
    # exactly once and absent from the must-read.
    {"executing_act": "cc_instruction_comparison_l0_l1_fifth_2026_09_03.md, Task 4",
     "base_commit": "cd62b001686d0f2793ad1d85df84057eaec57e38",
     "the_then_previous_batch": "cc_instruction_comparison_l0_l1_fourth_2026_09_03.md"},
    # ★ RECORDED 2026-09-03 by `cc_instruction_comparison_l0_l1_seventh_2026_09_03.md` Task 3. This is
    # the SIXTH writing's aiming, now superseded. That move RAN: the tool was re-aimed at all five
    # authored inputs, `--apply` moved the FIFTH writing's five entries to STATUS_ARCHIVE.md, and its
    # own reconciliation came back green in both limbs — every moved entry byte-present in the archive
    # exactly once and absent from the must-read.
    {"executing_act": "cc_instruction_comparison_l0_l1_sixth_2026_09_03.md, Task 2",
     "base_commit": "31a951bb2b206a89f150992fa4181e705115ef6c",
     "the_then_previous_batch": "cc_instruction_comparison_l0_l1_fifth_2026_09_03.md"},
    # ★ RECORDED 2026-09-04 by `cc_instruction_comparison_l0_l1_eighth_2026_09_04.md` Task 2. This is
    # the SEVENTH writing's aiming, now superseded. That move RAN: the tool was re-aimed at all five
    # authored inputs, `--apply` moved the SIXTH writing's three entries to STATUS_ARCHIVE.md, and its
    # own reconciliation came back green in both limbs — every moved entry byte-present in the archive
    # exactly once and absent from the must-read.
    {"executing_act": "cc_instruction_comparison_l0_l1_seventh_2026_09_03.md, Task 3",
     "base_commit": "cbb059bc1924f6fa04afcda959938e4ae610df0e",
     "the_then_previous_batch": "cc_instruction_comparison_l0_l1_sixth_2026_09_03.md"},
    # ★ RECORDED 2026-09-04 by `cc_instruction_comparison_l0_l1_ninth_2026_09_04.md` Task 2. This is
    # the EIGHTH writing's aiming, now superseded. That move RAN: the tool was re-aimed at all five
    # authored inputs, `--apply` moved the SEVENTH writing's four entries to STATUS_ARCHIVE.md, and its
    # own reconciliation came back green in both limbs — every moved entry byte-present in the archive
    # exactly once and absent from the must-read.
    {"executing_act": "cc_instruction_comparison_l0_l1_eighth_2026_09_04.md, Task 2",
     "base_commit": "0e6649fd95665d76f3b3702ceaed886bd7b1e7e3",
     "the_then_previous_batch": "cc_instruction_comparison_l0_l1_seventh_2026_09_03.md"},
    # ★ RECORDED 2026-09-04 by `cc_instruction_comparison_l0_l1_tenth_2026_09_04.md` Task 2. This is
    # the NINTH writing's aiming, now superseded. That move RAN: the tool was re-aimed at all five
    # authored inputs, `--apply` moved the EIGHTH writing's three entries to STATUS_ARCHIVE.md, and its
    # own reconciliation came back green in both limbs — every moved entry byte-present in the archive
    # exactly once and absent from the must-read.
    {"executing_act": "cc_instruction_comparison_l0_l1_ninth_2026_09_04.md, Task 2",
     "base_commit": "778e70c6dd9f74853fcaeaf77643809ecd07e9e6",
     "the_then_previous_batch": "cc_instruction_comparison_l0_l1_eighth_2026_09_04.md"},
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
