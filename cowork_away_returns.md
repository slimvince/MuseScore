# The away-batch RETURNS file — what needs the user, what was held, what each task did

> **STATUS: LIVE RETURNS FILE, created 2026-08-08 (CC, Task 0 of
> `cc_instruction_away_execution.md`).** This is the user's first read on return and Cowork's
> verification index. It is appended to per task and never rewritten.
>
> **★ HOW TO READ IT.** §1 is what needs a ruling. §2 is what was SURFACED — findings bearing on
> the analysis, its inputs, or a measurement tool a measurement depends on (D-641, #13), and
> establishment obligations (#19). §3 is the per-task log. §4 is the start state the batch began
> from, recorded before any act.
>
> **★ COWORK MAY APPEND HERE BETWEEN CC SESSIONS.** An appended entry whose heading carries
> **STOP** halts the batch at that point; the remaining tasks are not started, and the halt is
> recorded here and in `STATUS.md`. An entry without STOP is context, not instruction. CC reads
> this file in full before each task.
>
> **Nothing in this file authorizes a fix to the analysis, a design, or an inference change.**

---

## 1. What needs the user

### 1.1 The file named `phase1q_reclassification.json` holds neither phase 1q nor the present — what should happen to it? (Task 0)

**The fact, measured rather than assumed.** The establishment record of 2026-08-04 froze
`tools/audit/decisions/phase1q_reclassification.json` and its snapshot as byte-identical. **They
are not identical at HEAD**, and it is not the snapshot that moved — the snapshot still hashes to
its established value, and the classifier's own guard now re-checks that on every run. What moved
is the live file, which carries a different content at each of several recent commits: the applying
run has been performed by more than one wave since the snapshot was taken, rewriting that file each
time. **The measurement is the generated artifact
`tools/audit/decisions/phase1q_record_divergence.json`** — taken at named commits, from git objects
by explicit hash — and **no value from it is transcribed here** (**D-431**).

**What this means, stated plainly.** The record of what the phase-1q pass found survives **only
because the snapshot was taken**. The [[OI-301]] hazard `OPEN_ITEMS.md` OI-305 warned about was
realized and absorbed by the snapshot rather than avoided — and the rows that describe the applying
run as *held un-run* describe the LAST wave rather than the month.

**What was done.** Ruling 1 is applied as ruled: the live derived view moves to
`home_classification.json`, the classifier never writes the phase-1q file again, and the freeze is
enforced by a STOP on the snapshot's hash rather than promised in prose.

**What is left, and why it is the user's.** The file's NAME now says phase 1q and its CONTENT is a
later regeneration. Restoring it from the snapshot, renaming it for what it holds, or removing it
are three defensible acts and all three overwrite or delete a committed generated artifact. That is
a filing decision, which `CLAUDE.md`'s own non-gating line calls apparatus and which the record
reserves to the user. **Nothing depends on it:** the phase-1q record is at the snapshot, the live
view is at the new file, and both are guarded.

### 1.2 Should `OPEN_ITEMS.md` OI-319 be flipped? (Task 0)

The dispatch orders OI-319's remaining scope REPORTED, not its status moved, and that is what was
done. Reported for the user's decision: **the mechanism that row describes is discharged** — the
applying run has run, every `home_section` field is written, and no later wave can widen the stale
report by that cause. What remains attached to the row is a different subject its own 2026-08-04
entry records rather than rows (`gen_guard_classification.py` has a re-derivation mode no guard
list runs). Leaving the row open with its subject discharged is the OI-283 shape — a finding never
marked discharged — which is why it is put here rather than left silent.

### 1.3 `CLAUDE.md` now understates what the shell-read guard watches — a doc-sync correction owed at a surface this batch may not edit (Task 1)

`CLAUDE.md`'s D-253 conventions carry a 2026-08-08 clause stating, of the PowerShell reading family
and of a `python -c "open(...)"` in the Cowork sandbox, that **"No guard watches either surface"**.
Half of that was already made false by the 2026-08-07/08 dialect widening; **the other half is made
false by Task 1**, which brings interpreter code — `python -c`, `perl -e`, and heredoc bodies fed to
an interpreter — inside the guard, to the stated ceiling.

**What is still true and must survive any correction**, because it is the clause's actual point: a
guard armed as a hook in THIS project directory says nothing about the Cowork sandbox, and its
silence on an unwatched execution surface is not compliance (#19). The correction is therefore not
"a guard now watches it" but a narrowing — the surfaces are watched *where the hook runs*, and the
sandbox is not that place.

**HELD** because `CLAUDE.md` is in this batch's edit authority for **homing acts** only (D-645), and
a doc-sync correction is not a homing act. Stated here so it is one edit for whoever is authorized,
and so the staleness is on the record rather than merely inherited.

---

## 2. Surfaced findings (D-641, #13, #19)

### 2.1 `gen_home_classification.py` has not reached its own finding since 2026-08-07 — so two rows' quoted counts, and one row's corroborating run, describe an older tree (Task 0)

**What was observed.** The first attempt to run the applying pass stopped with *"authored judgment
for a document that is nobody's home: ['docs/unified_analysis_pipeline.md']"* — a STOP that fires
**before any entry is classified**. The committed `tools/audit/guard_state.json` records that same
STOP as this check's entire captured output, so it has been firing since the 2026-08-07
owner-rulings wave re-homed that document's last four entries and retired three other emptied
documents but not this one.

**What follows.** (a) The stale-field counts quoted in OI-305 and OI-319 describe runs older than
2026-08-07. (b) **OI-350's statement that the same check re-derives the three route-(i) documents'
eleven entries as `contract-home`, by document and by identity, cannot have come from a clean run
at the committed tree.** The mechanism OI-350 identifies is right and the applying run has now
confirmed the movement it predicted — what is withdrawn is the claim that a clean check had already
shown it. Both rows carry the correction.

**What was done about it.** The retirement was completed — the authored judgment moved whole into
the register data's own retired block, the same act with the same reason as the three retirement
records already there (#12) — and the finding is recorded rather than smoothed over.

### 2.2 A guard failed once at the batch's start and does not reproduce — recorded, not explained (Task 0)

`tools/audit/shell_read_guard.py --establish --check` returned non-zero inside the batch's opening
full guard run, at a position reached in the first seconds, **before this session had edited any
file**. The committed `guard_state.json` does not carry it among its failing tools. Re-run in
isolation it has passed on **every** attempt since, and an independent in-memory re-derivation of
the same artifact produced **no** difference against the committed one. The tool reads one file and
calls no subprocess, uses no clock and no randomness, so a content-dependent cause is not visible.

**Why it is surfaced rather than filed as noise.** It is the audit's own guard apparatus, it is
Task 1's subject, and a published deny rate that cannot be reproduced on demand is not established
(#19). **It is not asserted to be a defect** — a single non-reproducing exit against a run of clean
ones establishes nothing except that it happened. **It passed in this task's own closing full guard
run**, and it is re-tested at every later one, with the result recorded here.

### 2.3 The batch's opening guard run overlapped this session's own edits, and one row of it is therefore not evidence (Task 0)

The opening full guard run was launched before any edit and completed after five. Its rows up to
and including the slowest guard predate every edit; **`gen_home_classification.py --check`'s row
does not**, and it is discarded as evidence rather than reported as a reading. The start state of
record in §4 is therefore taken from the COMMITTED `guard_state.json`, not from that run. Recorded
because a contaminated baseline reported as a clean one is the failure this project's own
establishment rules exist against.

---

## 3. Per-task log

### Task 0 — COMPLETE. OI-305 and OI-350 resolved; OI-319's remaining scope reported

**What was done, in order.**

1. The batch's start state was taken (§4).
2. The ruled mechanism change (D-436, Ruling 1) was written into
   `tools/audit/decisions/gen_home_classification.py`: the phase-1q artifact is declared HISTORICAL
   and never written again; the live derived view moves to `home_classification.json`; a fourth
   frozen class epoch is added on the same construction as the third, so no entry's class between
   the phase-1r pass and this one is overwritten (#12); and the freeze is enforced by a STOP on the
   established snapshot's hash (#19).
3. The pre-apply register data was snapshotted into the repository (the O-12 pattern), and the
   field-diff tool `gen_apply_field_diff.py` was written to discharge **A1**. A second measurement
   tool, `gen_phase1q_record_divergence.py`, was written when the freeze's target turned out not to
   be the file the ruling's premise named (§1.1) — so the finding enters the record as a generated
   artifact rather than as prose (D-431). Neither carries a re-derivation path, both being
   point-in-time records under the 2026-08-04 ruling R4, which is also what keeps them out of the
   derived guard-candidate population instead of sitting there unclassified.
4. A missed retirement blocking the run was completed (§2.1).
5. The applying run ran. **A1 HOLDS** — no field outside the classifier's two intended writes
   moved, and the single top-level movement is the declared retirement of step 4, authored with its
   account so an unaccounted movement would still halt the batch.
6. **A2 HOLDS** — `--check` is green, and all six blocked generators run. Three of them first
   STOPPED on **D-472**'s authored route, which the same 2026-08-08 wave had homed out of item 1;
   the act was recorded in a fourth ruling table rather than the route being deleted, with the
   superseded hold preserved (#12).
7. The register and everything downstream of it were regenerated, to a fixed point.
8. OI-305 and OI-350 flipped with provenance; OI-319's remaining scope reported on its row; dated
   entries appended to all three detail files.

**Assumptions:** A1 discharged by measurement (`tools/audit/decisions/apply_field_diff.json`); A2
discharged by running the six.

**Guards at the task boundary.** The full set was re-run and the classification re-run after it,
which is the order its own STOP requires. **Cleared by this task:** the home classification, the
outstanding-delegation view, the item-1 route table, the re-home blocker, the supersession
application, the completion inventory, the finish line, the non-gating apparatus rows, the
decisions register — and the shell-read guard's establishment, which passed (§2.2). **Still
failing, and each is a standing failure this task did not touch:** the `CLAUDE.md` rule triage, the
delegation bar, the legacy-mark verification, and the live-prohibition pointers. Every verdict is
at `tools/audit/guard_state.json` → `summary` and none is restated here (**D-431**). **★ THE
DELEGATION BAR'S FAILURE IS THE SAME SHAPE AS THE ONE THIS TASK FIXED, one construct out:** it
STOPS on a list of documents that are nobody's home any more, accumulated by every re-homing wave.
It is not repaired here — its table is generator source rather than register data, and pruning it
is not among Task 0's acts.

**Holds:** the filing decision at §1.1; OI-319's status at §1.2; and two more, both outside this
batch's edit authority and both stated so they are one edit for whoever is authorized.

1. **A pointer this task made false, and did not correct.** `gen_phase1p_delegation_bar.py`'s
   artifact prose says *"the register's PRESENT classes are the post-apply ones and are at
   `tools/audit/decisions/phase1q_reclassification.json`"*, and names the same file again for its
   `by_document` and `entries` blocks. After the epoch treatment the present classes are at
   `home_classification.json`. The correction is to re-aim both namings at that file. It is HELD
   because that generator is neither the register data nor the guard tooling nor the classifier —
   the three surfaces the dispatch's edit-authority list admits — and its list ends *"Anything
   else: hold."*
2. **Two untracked files were deliberately NOT staged**, being Cowork's rather than this batch's:
   `cowork_instruction_return_session.md` and `cowork_scratch_2026_08_08/`. They remain untracked;
   naming them here is so their absence from the commit is a choice on the record rather than an
   oversight.

**Committed and pushed** as `82ebfd68d9` to `origin` (the user's fork `slimvince/MuseScore`);
`upstream` was not touched and remains push-disabled. The commit also carries the accumulated,
uncommitted document-routes wave — the two cannot be split, because the applying run re-serialized
register data that wave had already changed — and the commit message says so.

**No value is restated here (D-431)** — every quantity lives in the generated artifacts named
above.

**Freeze respected:** no `src/` change, no golden, no corpus, no `tools/robust_stop/` movement, no
behaviour change to the analysis, no fix to inference, no design.

### Task 1 — COMPLETE. The guard family built corpus-first; OI-300, OI-348 and OI-351 all resolve

**What was done, in order, and the order is the ruling's.**

1. **The corpus went in first**, before one line of the mechanism moved: OI-351's observed command
   and its path-form variants, the POSIX and `pwsh` wrapper spellings, the interpreter forms
   including the heredoc one, the hashless `git diff` forms, and — on the other side — the same
   spellings aimed OUTSIDE the tree as controls, the wrapper controls including
   `BUILD_AND_TEST.md`'s own mandated `Start-Process` invocation, and the hash-bearing git forms.
2. **The blindness was measured at the unwidened guard**, with the corpus already in place. It has
   the same shape as the dialect widening's: almost every new forbidden row admitted, not one new
   sanctioned row denied. The guard was not wrong about this family — it could not see it.
3. **The five clauses were built**, and only then were both rates re-measured on the same extended
   corpus. **The revert condition is not met — false denials FALL**, and every one that remains is
   accepted by the ruling's own clause 4.
4. **Assumption A5 discharged by measurement.** Every row the corpus carried before this act was
   decided both ways; every verdict that moved is named in the artifact, and every one is a shape
   the design names — false denials removed on the heredoc and redirection shapes, misses caught on
   the wrapper and interpreter shapes. No verdict moved anywhere else.

**★ OI-351'S CAUSE IS ESTABLISHED, AND IT IS WIDER THAN THE ROW SUPPOSED.** The row named two
candidates and asserted neither. **The first is confirmed, in a form it did not suppose: the DRIVE
LETTER'S CASE.** The guard compared a path against the repository root with a case-sensitive string
comparison on a platform whose paths are case-insensitive, so **every** repository path written with
a lowercase drive letter read as outside the tree — in every utility and both dialects, not only in
`ls`. The corpus now carries `cat` and `grep` in that spelling and both were admitted before the
fix. **The second candidate — a gap between the live hook and the decision function — is refuted by
observation**: the two agree on both live decisions the record holds, and **no new forbidden command
was issued to test it**, because performing the violation in order to measure the guard is not a
measurement anyone may take.

**★ THE NEW GUARD DENIED THIS SESSION'S OWN COMMAND WITHIN MINUTES OF BEING BUILT, AND THAT IS
REPORTED AS A DETECTION RATHER THAN AN INCONVENIENCE.** A `python - <<'PY'` heredoc was reached for
to do a bulk rename inside the guard's own source; the interpreter-heredoc clause denied it, naming
the repository path in the code. It is precisely OI-348's second shape and precisely the founding
instance's own form. **It was not worked around** — the rename was redone through the file tools.

**Two of this session's own new reserved-word collisions were caught by the standing self-check and
corrected before the commit**: the bare non-musical *part*, throughout the new text and in an
artifact field name, and the bare *rest* as a parameter name — **the same collision the previous
wave's self-check caught in its own new selection function**, reintroduced by matching the adjacent
code's idiom. That it recurred one wave later is worth the user's attention: matching the
surrounding style is exactly how this rule gets broken.

**One authored input was maintained rather than left to rot**, the same class of act as Task 0's
missed retirement and caught the same way. Closing OI-300 stopped six generators — the non-gating
apparatus declaration held a live verdict for a row the index no longer carries open, which is that
tool's own STOP working. The verdict was moved WHOLE into its retired table with the reason it
closed (#12), never deleted; and its own ground held to the end, since what discharged the row was
the establishment run it named.

**Holds:** §1.3, the `CLAUDE.md` doc-sync correction, which is outside this batch's edit authority.
**Surfacings:** none new bearing on the analysis — this task's whole subject is the audit's own
apparatus.

**Freeze respected:** no `src/` change, no golden, no corpus of scores, no `tools/robust_stop/`
movement, no behaviour change to the analysis, no fix to inference, no design. The one mechanism
change is the ruled one.

**No value is restated here (D-431)** — every rate, count and identity lives in
`tools/audit/shell_read_guard_establishment.json`.

---

## 4. The batch's start state, recorded before any act

**HEAD** is `03bce02e4b` (*"docs(cowork): the standing self-check's own two findings, corrected
rather than shipped"*). The working tree carries the uncommitted document-routes wave.

**The guard set at the start**, taken by IDENTITY from the COMMITTED `tools/audit/guard_state.json`
and not from this session's own run (§2.3). The failing tools were the `CLAUDE.md` rule triage, the
phase-1 completion inventory, the phase-1 finish line, the outstanding-delegation view, the home
classification, the delegation bar, the legacy-mark verification, the item-1 route table, the
re-home blocker, the supersession application, and the live-prohibition pointers. **No count is
given** — every count lives in that artifact's own `summary` (**D-431**); the identities are listed
because they are what lets a later reader tell a new failure from a standing one, and an identity
is not a quantity.

**The two registers:** the decisions register was current — its own check passed, every verbatim
resolved at its cited home, and the disposition verifier reported zero line drift. The open-items
index and its detail files were a bijection.

**What was already known to be owed** and is this batch's queue: the guard family (OI-300, OI-348,
OI-351), the archive-unhomed eleven and D-601, the defense gaps, the reach-verdict derivation, the
section-unreached and findings-not-rules entries, the session-executable gating rows, the OI-349
conformance probe, and OI-346's marks.

**Phase 1's completion statement is not written, not drafted and not partially written by this
batch — even if every item closes, the user commissions it.**
