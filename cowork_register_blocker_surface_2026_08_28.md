# DECISION SURFACE — the decisions-register blocker

Drafted 2026-08-28 by the Cowork writing side. Untracked. Nothing here is ruled.

**REVISED the same day, at the user's condition that the choices be fact based.** The first draft
diagnosed the blocker from the two tools' docstrings and their failure output, and declared that it
had not read their check implementations. It has now read them, and the diagnosis was half wrong.
The revision is recorded below rather than over the first version's claims (#12); what changed and
why is stated at §6.

This surface is written to be read cold. Every identifier is explained where it first appears.

---

## 1. What the pieces are

**The decisions register.** The project's record of what has been decided and what its status is.
Its data lives in one file, `tools/audit/decisions/backbone_decisions.json`. The readable files —
`DECISIONS.md`, the lean index, and `decisions/group_<X>.md`, the full entries — are *generated*
from that data file and are never hand-edited. Every entry has an identifier of the form `D-NNN`.

**Register rule (c).** One of the register's lettered rules in `CLAUDE.md`, quoted from the file:
*"a new ratification, shelving or falsification gets its register entry (data + regenerated files)
IN the commit that records it"*.

**A soft discard.** An act that retires an entry from the live part of the register because no
deciding act could be named for it. Retired, not deleted, and revivable. Two were performed on the
user's rulings: the first on 2026-08-16 by `tools/audit/decisions/apply_soft_discard.py`, retiring
165 entries; the second on 2026-08-17 by `tools/audit/decisions/apply_residue_discard.py`, retiring
38. Together 203.

**The retired-entries block.** One block inside the same data file holding both retirements. It
carries a field `the_population_before_this_retirement`, and its own written stop says why:
*"live entries plus retired entries must equal `the_population_before_this_retirement` exactly — an
entry in NEITHER block is caught by that arithmetic, which is why the former population is recorded
here rather than remembered"*.

**The committed plan.** `tools/audit/soft_discard_application.json`, the first discard's planning
artifact, written before the act and never re-derived after it. Read at the file: it records
`the_live_record_before: 677`, `retired_by_this_act: 165`, `the_live_record_after: 512`.

---

## 2. What is actually wrong — read at the check code, not inferred

Three entries have been added to the register since the sittings: `D-678`, `D-679` and `D-680`,
confirmed at the data file. The live record now holds 477, the retired block 203.

**The two checks fail for two DIFFERENT reasons, and only one of them is the reason the first draft
of this surface gave.**

**`apply_residue_discard.py --check` — the first draft was right about this one.** It carries the
sitting's sums as constants and compares the record as it stands today against them. Its
`the_arithmetic` function reconciles `keep_side + retired_after` against a ruled total of 677 *and*
against the data file's own before-figure, and reconciles the live record after the act against a
ruled 474. With three entries added, the live record is 477 and neither reconciles. This check does
break on every addition, permanently, by construction.

**`apply_soft_discard.py --check` — the first draft was wrong about this one.** It does not pin the
sitting's totals at all: it reads its before-figure out of the data file. Its check was **already
narrowed once**, and the source carries the reason in a comment at lines 544–556 — the comparison
formerly read the whole retired population back into the plan's figures, which became false the
moment the second retirement appended to the same block, and it was re-aimed at something narrower
that stays true across later retirements. Its only remaining frozen comparison is against the
committed plan. It fails today for one reason: the plan says the population before the first
retirement was 677, and the data file's block field no longer agrees.

## 2a. The finding that was not visible from the docstrings

**`the_population_before_this_retirement` in the data file now reads 680.** It was 677 when
`cc_report_register_reconciliation.md` measured it at that offset, and the committed plan — read
directly at the artifact — still records 677.

That field names a historical quantity: the size of the register before the 2026-08-16 retirement.
That quantity was 677 and cannot change. It has been rewritten to 680, and the effect is exactly
what the shape predicts — the block-level arithmetic *"live + retired = the former population"*
keeps passing (477 + 203 = 680), and the plan comparison breaks instead.

So **the register's own data file currently carries a statement about its own history that is not
true**, and that false statement is the direct cause of one of the two red guards. Whoever added
`D-678`, `D-679` and `D-680` bumped the field to keep the block arithmetic alive.

**Not established, and it should be:** which act bumped it, and under what dispatch. A change to the
register's data file outside a ruled discard act is a separate question from this surface's.

---

## 3. The alternatives, restated on the established facts

### A — Re-baseline the recorded arithmetic

Restate each retirement's recorded sums against the population as it now stands.

**This is no longer viable, and the record says so in its own words.** For the first discard, the
figures to re-base are the committed plan's 677 / 165 / 512, and the check's source states the
purpose of the comparison in terms: *"A plan whose arithmetic was rewritten still fails, which is
what this check exists for."* Re-basing the plan is precisely the act that check was built to
catch. For the second discard, re-basing means changing the constants that carry the sitting's ruled
sums, which would make the tool state the sitting ruled numbers it did not rule.

A cannot be performed without writing something untrue into the record. It is listed here because it
was on the first draft and was the user's provisional choice, not because it survives.

### B — Correct the false figure and re-aim what the checks measure

Three parts, and each is small and separately checkable:

1. Restore `the_population_before_this_retirement` to **677**, the figure the committed plan and the
   earlier measurement both carry. This is a data repair to a historical field, not a decision act —
   nothing moves between the live and retired sides.
2. Re-shape the block-level assertion so it accounts for the population **as it was at the
   retirement**, with entries created afterwards outside it, instead of requiring the live count plus
   the retired count to equal a fixed historical number forever.
3. Re-shape `apply_residue_discard.py`'s `the_arithmetic` the same way, so the sitting's ruled sums
   are re-reconciled over **the sitting's own population** rather than over the live record as it
   stands today.

*Towards the objective:* permanent; register rule (c) becomes satisfiable again; no entry moves; no
sitting's ruled figures are restated; and the one untrue statement in the data file goes away. On
today's numbers all of it reconciles — keep 474 plus retired 203 is the sitting's 677, with the
three later entries outside it and the live record 477 = 474 + 3.

*Costs:* it is an edit to two guards that makes them stop failing, which is the shape the record
treats as a defect, so it must be ruled explicitly as *the checks were measuring the wrong thing* —
with the argument on the record. It needs a dispatch; CC is idle.

*What removes most of that cost:* **the same class of re-aiming has already been done to one of
these two checks**, for a closely related reason, and its justification is written into the source
at the site. B is not a new liberty; it is the second application of one already taken.

### C — Suspend rule (c) on the record, with the owed entries listed

Defer register entries until the baseline is repaired, keep a written list of what is owed — the
nine ratifications of 2026-08-28 and everything before them — and enter them in one act afterwards.
Costs nothing now; the register keeps drifting; the guards stay red with an explanation.

Worth doing alongside B, for the interval between the ruling and its landing.

### D — Continue as now

C without the writing. Where seven batches have already landed.

---

## 4. Recommendation

**B, with C alongside it for the interval.** A is withdrawn: on the established facts it cannot be
performed truthfully.

---

## 5. Declared limits of this revision

Read at the files by this side: both tools' `--check` implementations and the residue tool's
`the_arithmetic`; the retired block's header fields and its written stops; the committed plan
`tools/audit/soft_discard_application.json`; the three added entries in the data file; the two
checks' current failure output in `tools/audit/guard_state.json`; register rule (c) in `CLAUDE.md`.

**Not read, and relied on nowhere in the recommendation:** the two ruling records
`cowork_rulings_2026_08_16_preparation_return.md` and
`cowork_rulings_2026_08_17_residue_sitting.md` themselves. Every quotation of a ruling in this
surface is quoted from a tool's own source or from a committed artifact, not from the ruling record.
**Before B is dispatched, the sentence the residue tool relies on — that a non-reconciling derivation
is a stop-and-report and not an adjustment — should be read at its ruling record, because B changes
what "reconciling" means and that sentence is the closest thing to a bar on doing so.**

No git object was resolved by this side. The tip was read as a file at `.git/refs/heads/master`:
`6005daecaf9f1a6692e61521911ef8b99ed73b55`.

---

## 6. This side's error, recorded

The first draft of this surface asserted that **both** checks verify the discards by absolute totals
carried over from the sittings. That is true of one of them and false of the other, and the false
half was the ground on which the draft ranked A as a live alternative at all. The draft declared
that it had not read the check implementations — the limit was stated — but it made a
recommendation and offered a choice on top of the unread ground anyway, which is what a declared
limit does not excuse.

It is the same shape the handoff's seventy-eighth entry names as this project's recurring defect: an
assertion written into an artifact without going to the record that would have answered it. Counted
as one error of this session. It was caught by the user's condition, not by this side.
