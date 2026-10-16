# Rulings — the L3 withheld-documents confirmation sitting, 2026-10-15

> **STATUS: RULING RECORD.** Cowork, 2026-10-15 (Stockholm), the sitting that booted on
> `records/cowork/handoff/cowork_handoff_entry_four_hundred_and_nine.md`. An interim carrier under the standing clause
> that a sitting record is written in the turn its ruling is given and lands in git at the next dispatch's Task 0.
> **No act of this sitting is a commit to git.** `.git/refs/heads/master` and `.git/refs/remotes/origin/master` both
> read `a01e9402fbaf034fe0d357214b67c06a8294309c`, read as files with the file tools over staged copies.

## 0. What was put, and in what form

The confirmation Ruling 5 of `records/cowork/rulings/cowork_rulings_2026_10_15_l3_boot_list_sitting.md` reserves to
the user. Ruling 5, quoted whole (D-643): *"As Ruling 6 of `cowork_rulings_2026_09_05_l2_boot_list_sitting.md` did for
L2: the pack-build dispatch derives, from the register's data file (`tools/audit/decisions/backbone_decisions.json`)
and the ruled `VERDICTS["l3"]`, the set of home documents of the 22 IN entries; prints it; and **STOPs for the user's
confirmation before the set is authored into `WITHHELD["l3"]["withheld_documents"]`**, each document with its finding,
date and reason."*

The set is the one printed by `python tools/audit/gen_l2_withheld_documents.py --subject l3` under
`records/cc/instructions/cc_instruction_l3_pack_build_first_half_2026_10_15.md` Task 3, recorded at
`tools/audit/l3_withheld_documents.json` (committed at `0ad45e7f09c054fa082f7540a855ac1b31fd35ae`). **Checked by this
sitting at the objects:** the artifact's 22 IN identities equal the 22 `VERDICT_IN` entries of `VERDICTS["l3"]` in
`tools/audit/gen_derivation_boot_pack.py`; each document's identities agree with the home column of `DECISIONS.md`
and with Ruling 5's stated expectation.

The surface was delivered as text in its own turn, stating that the alternatives had collapsed — removing a document
would let an L3 answer reach the session (against #19), adding one by hand is Ruling 5's declined alternative (C) —
with a recommendation on the three grounds; the question was put alone in a later turn, no widget.

## 1. Ruling 1 — THE DERIVED SET IS CONFIRMED, ALL FIVE DOCUMENTS

**The user's word: "yes".**

**What was decided.** The withheld documents of L3's boot pack are exactly the five the tool derived:

| Document | IN identities homed there |
|---|---|
| `ARCHITECTURE.md` | D-022, D-472, D-495, D-584, D-605 |
| `cowork_joint_estimator_architecture.md` | D-526 |
| `cowork_layer5_function_design.md` | D-336 |
| `cowork_layer6_grouping_design.md` | D-454, D-455, D-456, D-457, D-459, D-460, D-461, D-462 |
| `cowork_phrase_boundary_design.md` | D-476, D-477, D-478, D-479, D-480, D-481, D-485 |

They are authored into `WITHHELD["l3"]["withheld_documents"]` by the second half of the pack build, each with its
finding, date and reason; the finding cites this record and the artifact.

**The ground, as put.** Towards the objective: a blind derivation that agrees with these documents is evidence the
answers are right. Towards the principles: #19 (a derived, confirmed set), #6 (one rule for both subjects). Meta level:
one step from the analysis — what a session reads. Strongest argument against, as Ruling 5 states it: each name becomes
a leak string, and `cross_reference_additions` will pull into the withheld set every design-intent entry whose own text
names one, possibly entries ruled admitted; their number is unmeasured until the build runs, and under Ruling 84 any
that would withhold an admitted entry comes to the user as its own list.

**Documentation and algorithm.** This decides what a future session is not shown. It amends no specification and
changes no algorithm. The currently decided method for L3 is `FRAMEWORK.md` §5's L3 block with DP-I (*"split — cues at
L1, type at L3"*), as the boot-list record states it (not re-read at `FRAMEWORK.md` this sitting).

## 2. Put to the user, not ruled

- **Task 1's STOP (L2 not frozen).** `build_subject` keys two scopings on `FROZEN` membership (`XREF_FIELDS_FROZEN`,
  and `extras_leaks` being `None` for a frozen subject), written for packs rendered before the 2026-09-21 and 2026-09-27
  rulings; L2's pack was rendered under them, so freezing it as the generator stands would move L2's manifest record
  (report §5). Checked at the generator's code by this sitting. Whether the record already settles the fix — for
  instance under the user's rule of 2026-09-22 — was NOT checked. UNSETTLED.
- **The search's one hit** — `docs/research_papers/BIBLIOGRAPHY.md` at line 2234 of the L2 input-contract copy,
  checked at the copy. This side proposed leaving it (not a withheld document; the line states an L2 point). Not ruled.

## What this record does NOT do

It authors nothing into the generator, renders no pack, writes no dispatch, and allocates **no decisions-register
identity** — the register cannot accept one while `cowork_register_rule_c_suspension_2026_08_28.md` is the route.

*Provenance: Cowork, 2026-10-15 (Stockholm), the sitting booted on entry 409. The user's words: the opening
instruction; "continue" (the question); "yes" (Ruling 1).*
