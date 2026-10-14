# Rulings — the L2 outgoing-population check sitting, 2026-10-14

> **STATUS: RULING RECORD.** Cowork, 2026-10-14 (Stockholm), the sitting that booted on
> `records/cowork/handoff/cowork_handoff_entry_three_hundred_and_ninety_seven.md`. An interim carrier under the
> standing clause that a sitting record is written in the turn its ruling is given and lands in git at the next
> dispatch's Task 0. **No act of this sitting is a commit to git.** `.git/refs/heads/master` and
> `.git/refs/remotes/origin/master` both read `b6bceef7009f92e89a97c8a79465e5e462e1f49a`, read as files with the
> file tools over staged copies.

---

## 0. What was put, and in what form

Entry 397 §3 step 4(c) orders the next Claude Code dispatch to carry the two guard reds of entry 393 §1. The
first of them, `tools/audit/gen_l2_outgoing_population.py --check`, was left to the writing side by
`records/cc/reports/cc_report_l2_ratification_application_2026_10_14.md` §6 (*"Whether the population's order
should take the new position, and what becomes of the records that cite member 52, is the writing side's"*).
This sitting found it is the user's: **D-436** — a failing mechanism is REPORTED, not automatically removed —
and each earlier move of a check to historical status was a user ruling (2026-08-04, read wave 6, R4;
2026-08-16 §4; 2026-09-17, Alternative A1, recorded at entry 193 §1).

The surface was delivered as user-visible text in one turn, with four alternatives weighed towards the
objective and towards the principles, each marked as acting on the project's own governance apparatus, and a
recommendation; it carried no question. The question was put alone in the next turn, no widget. **The user's
word: "C".**

## 1. Ruling — THE L2 OUTGOING-POPULATION TOOL BECOMES A HISTORICAL RECORD

**What was decided.** `tools/audit/gen_l2_outgoing_population.py` leaves the live guard list as a HISTORICAL
RECORD under the user's ruling of 2026-08-04 (R4: *"a tool that RE-DERIVES A LIVE INVARIANT belongs in the guard
list; a tool that RECORDS A MEASUREMENT TAKEN AT A POINT IN TIME does not"*). Its committed artifact
`tools/audit/l2_outgoing_population.json` stays on disk exactly as committed; the tool is no longer re-run. **R4's
per-tool condition is met first:** the executing dispatch enumerates every reader of the artifact and of the
tool, and STOPS before moving anything if a live reader other than records exists.

**The ground, as put.** The artifact numbers the members the finished L2 comparison tabulated, and ratified
records cite members by position (*member 52*, the confidence contract). Task 3 of
`records/cc/instructions/cc_instruction_l2_ratification_application_2026_10_14.md` added three term-hit lines to
`cowork_confidence_contract.md` as ordered, so a re-derivation exchanges positions 51 and 52. Towards the
objective: neutral — no inference effect. Towards the principles: #12 (the ratified numbering keeps its meaning),
**D-646** (a generated record that must outlive its writer is kept at a fixed snapshot), R4.

**The alternatives not taken, recorded because an excluded alternative is evidence about the choice.**
A — regenerate and accept the new numbering: ratified records would silently name a different document (#12,
#10). B — leave the check red: every later dispatch re-explains it, and a guard failing by design *"teaches a
reader to ignore the set"* (`tools/audit/guard_state.json`, the not-run reserved-word entry). D — freeze the
numbering in the tool's code: the same effect as C with more apparatus.

**Documentation and algorithm.** This ruling orders work on the project's governance apparatus only. It amends
no specification and changes no algorithm.

## 2. Settled at the record, not ruled — the second red

`tools/audit/decisions/gen_retired_subject_moves.py --check` fails because the authored section-kind judgments
for `cowork_confidence_contract.md` in `tools/audit/decisions/backbone_decisions.json` (`section_home_criterion`)
still record the §2 heading as *"2. Definitions — the two admissible confidence classes"* and §4's heading at line
63; at the contract as it stands the §2 heading reads *"2. Definitions — the three admissible confidence
classes"* at line 23 and §4's heading stands at line 81 (read at the staged contract this sitting). Both are stale
references after a ratified amendment, which the user's rule of 2026-09-22 has fixed without asking. **D-267's
own title and patterns are not touched** — they are register content waiting on the route
(`cowork_register_rule_c_suspension_2026_08_28.md`).

## 2b. A correction found at the dispatch's check, the ground as put kept

The ground as put to the user said *ratified* records cite members by position. That the citing records are
ratified was **not established** by this side: the citation *member 52* is relayed from the 2026-10-14
application dispatch's premise ledger and its report §6. The ruling does not rest on the word — a re-derivation
would change what any record citing a position names. The ground above is left as it was put (#12).

## 3. What this ruling does NOT do

It moves no tool itself, edits no file but this record, writes no dispatch (D-250), and allocates **no
decisions-register identity**.

*Provenance: Cowork, 2026-10-14 (Stockholm). The user's words: "continue" (the question put); "C" (Ruling 1).*
