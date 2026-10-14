# Rulings — the next-subject sitting, 2026-10-14

> **STATUS: RULING RECORD.** Cowork, 2026-10-14 (Stockholm), the sitting that booted on
> `records/cowork/handoff/cowork_handoff_entry_three_hundred_and_ninety_two.md`. An interim carrier under the
> standing clause that a sitting record is written in the turn its ruling is given and lands in git at the next
> dispatch's Task 0. **No act of this sitting is a commit.** `.git/refs/heads/master` and
> `.git/refs/remotes/origin/master` both read `b6bceef7009f92e89a97c8a79465e5e462e1f49a`, read as files with the
> file tools; `.git/logs/HEAD` names it as the end-state commit of
> `records/cc/instructions/cc_instruction_l2_ratification_application_2026_10_14.md`.

---

## 0. What was put, and in what form

Entry 392 §4 step 5: the next-subject decision — which specification the detail-specification phase derives
after L2 — established from the record first (D-599; Conventions, *How a decision surface is written*, steps 1
and 2), a question going to the user only if the record does not answer it.

The record does not rule the order after L2: Ruling 10 of
`records/cowork/rulings/cowork_rulings_2026_08_31_decision_surface_sitting.md` is *"L0+L1 first, then L2"*, and
nothing later names a subject. The writing side therefore set out the derivation as user-visible text in one
turn, stated that no real choice remained, named no decision surface, and said that because the order of
subjects had been the user's call before (Ruling 10) it would ask him to confirm in a later turn. **The user
answered in the next turn without that question being put. His word: "L3".**

## 1. Ruling — L3 IS THE NEXT SUBJECT OF THE DETAIL-SPECIFICATION PHASE

**The ruling.** After L2, the detail-specification phase derives **L3, the read-off facts**
(`FRAMEWORK.md` §5, *L3 — The read-off facts*: the cadence at each phrase end with its type; the phrase and
section grouping; the chord symbol; the figured bass; the harmonic rhythm).

**The derivation, as put** (every point read at the object this sitting):

1. **L3 is unblocked.** Its charter's question opens *"given a settled tonal reading"*, and L2's reading is
   ratified (the nine acts of 2026-10-13 and 2026-10-14, applied by the dispatch named above). The L2 → L3
   boundary contract (`FRAMEWORK.md` §5, *The boundary contracts*) fixes what crosses, and L3 *"may not consume
   anything L2 did not publish, and it may not revise L2"*.
2. **The voice-leading axis is not ready.** The candidacy criterion that chose Task B's reading
   (`reading_pass/candidacy_upgrades.md`, *The criterion*) reaches *"a detail specification of L1, L2 or L3"*;
   no slice of reading has been derived for the axis, so a preparatory derivation stands before any of its
   reading. `FRAMEWORK.md` §5 records the two axes as measured near-independent, which makes deferring the axis
   the cheapest point on the user's joint-evaluation argument (Ruling 2 of
   `records/cowork/rulings/cowork_rulings_2026_08_30_detail_phase_opening_sitting.md`).
3. **The boundary contracts join the other subjects**, and the whole-architecture coherence review that ends
   the phase (same record, Ruling 2 item 6) covers them.
4. **The gate stands:** no derivation of a subject before its slice of Task B is read (the eighty-seventh
   entry's gate, restated in Ruling 10). L3's slice in `cowork_l2_task_b_slice_derivation_2026_09_05.md` §5 is
   **one row, 36** (Ju, Margot, McKay, Dahn & Fujinaga, ISMIR 2020, automatic figured bass annotation), and no
   extract of it exists in `reading_pass/extracts/` or `reading_pass/extracts_second_pass/` (folder listing,
   2026-10-14). Rows 34 and 40 carry a noted L3 bearing and are read under L2.

**Documentation and algorithm.** This ruling orders work. It amends no document and changes no algorithm.

**UNSETTLED, carried rather than decided.** Whether L3's slice is only row 36. That slice was derived on
2026-09-05 from each row's recorded reason, not from the papers. Rows 37 and 38 (cadence detection) were read
for L1, and their reasons in `candidacy_upgrades.md` touch L3's cadence half: row 38's reads *"a different method
for the same L1/L3 split"*; row 37's reads *"the method behind DP-I's split: which cues are computable before the
harmony is the L1 charter's own content"*, naming L1 and not L3 in words. Whether either belongs in L3's slice
is checked before row 36 is read.

## 2. Carried from the dispatch's close, not decided here

Two guard reds left standing by the L2 ratification application, each caused by an ordered edit
(`records/cc/reports/cc_report_l2_ratification_application_2026_10_14.md` §2, §6; verified at the objects
this sitting): `gen_l2_outgoing_population.py --check` (the contract and `cowork_layer1_note_model_design.md`
would exchange positions 51 and 52; the committed artifact holds the note-model document at 51 with 22 hit lines
and the contract at 52 with 20), and `decisions/gen_retired_subject_moves.py --check` (the contract's former §2
heading still at three places of `tools/audit/decisions/backbone_decisions.json`). Both go to the next Claude
Code dispatch; neither is put to the user.

## 3. What this ruling does NOT do

It derives nothing, writes no dispatch (D-250), reads no paper, cuts no slice, edits no tracked document, and
allocates **no decisions-register identity** — the register cannot accept one while
`cowork_register_rule_c_suspension_2026_08_28.md` is the route.

*Provenance: Cowork, 2026-10-14 (Stockholm). The user's word: "L3".*
