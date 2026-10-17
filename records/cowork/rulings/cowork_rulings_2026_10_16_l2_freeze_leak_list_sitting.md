# Rulings — the L2 freeze leak-list sitting, 2026-10-16

> **STATUS: RULING RECORD.** Cowork, 2026-10-16 (Stockholm), the sitting that booted on
> `records/cowork/handoff/cowork_handoff_entry_four_hundred_and_thirteen.md`. An interim carrier under the standing
> clause that a sitting record is written in the turn its ruling is given and lands in git at the next dispatch's
> Task 0. **No act of this sitting is a commit to git.** `.git/refs/heads/master` and
> `.git/refs/remotes/origin/master` both read `5324b94388bdda6c242ff937ace781cbe62d9c2d`, read as files with the file
> tools over staged copies.

## 0. What was put, and in what form

Task 1 of `records/cc/instructions/cc_instruction_l3_pack_build_second_half_2026_10_16.md` STOPPED at its (g)
(`records/cc/reports/cc_report_l3_pack_build_second_half_2026_10_16.md`, head section): with `FROZEN["l2"]` added, the
D-657 comparison against the committed manifest at `a01e9402fbaf034fe0d357214b67c06a8294309c` moved `l2`'s
`LEAKS_IN_THE_EXTRAS` by exactly two inserted entries (61 → 63), both in member (7), the charter. Checked at the objects
by this sitting: the two lines stand at `FRAMEWORK.md:450–451`, in the 2026-10-14 amendment to L2's block of §5 (the
elaboration-relations list), naming D-527 and D-207; neither line occurs in
`tools/audit/derivation_boot_pack/l2/07_the_charter_the_layers_and_the_decisions.md` (a search for *appoggiatura* and
both lines' phrases matches nothing). This is the risk §2 of
`records/cowork/rulings/cowork_rulings_2026_10_15_l2_freeze_derivation_sitting.md` named in advance.

Put on a self-contained surface in a turn of its own, five alternatives weighed towards the objective, towards the
principles and by meta level, the surface stating that the alternatives collapse to one and recommending it; the
choice question in the next turn. **The user's words, verbatim: "yes".**

## 1. Ruling 1 — a frozen subject's extras leak list is the one its session was given

**Ruled.** The freeze derivation of 2026-10-15 is confirmed and extended: when `l2` is frozen, its
`LEAKS_IN_THE_EXTRAS` (and the count `counted/extras_lines_with_a_leak_hit` with it) is taken from the pack files on
disk — the files its session was given, proved equal to their committed blobs by the hash STOP — and not from a
re-render of today's sources. The record of what L2's session was given therefore does not move.

**The evidence it owes, unchanged from the derivation (D-657).** The next dispatch re-runs the before-and-after
comparison against the committed manifest at an explicit hash: the three subjects already frozen do not move at all;
`l2` moves only by its `★_FROZEN` block and the re-pointing `frozen_from_disk` performs, its leak list equal to the
committed 61 entries. Any other movement is a STOP with nothing committed.

**Bound.** This sitting did not read the generator's `frozen_block`, `frozen_from_disk`, `build_subject` or its
extras leak scan; the code form of the repair is the next dispatch writer's, after reading them. That a scan over the
on-disk files returns exactly the committed 61 is a prediction, measured by the comparison above.

**Declined:** freezing with 63 lines (a record stating lines never given; D-646, #12); freezing with no leak list (the
ruled list discarded); re-rendering L2's pack (the `FROZEN["l2"]` reason: back-dating a later text into a completed
derivation's record); building L3 with L2 unfrozen (Ruling 1 of `cowork_rulings_2026_10_15_l3_boot_list_sitting.md`,
noted: the two packs share the charter member).

## 2. Documentation or algorithm

**Documentation and apparatus only.** It concerns what the manifest records of a spent pack. It amends no
specification and changes no algorithm of the analysis. The currently decided method for L3 is `FRAMEWORK.md` §5,
"L3 — The read-off facts" (lines 474–498), read this sitting, unchanged.

## 3. What this record does NOT do

It edits no tool, renders no pack, writes no dispatch, creates, flips or discards no open-items row, and allocates
**no decisions-register identity** (`cowork_register_rule_c_suspension_2026_08_28.md` is the route, not taken).

*Provenance: Cowork, 2026-10-16 (Stockholm), the sitting booted on entry 413. The user's words: the opening
instruction; "continue"; "yes".*
