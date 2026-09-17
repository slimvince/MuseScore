# CC report — the second ignore rule removed, the [[OI-373]] clearing act, and the guard-staleness fix

> **Dispatch:** `cc_instruction_batch_return_rulings.md` (Cowork, 2026-08-15), executing
> `cowork_rulings_2026_08_15_batch_return.md` §3 (the ignore rule), §2 (the clearing act) and §4
> (the staleness fix). Its §1 orders no act of the coding side and none was taken. **Performed
> 2026-08-15 (CC).**
>
> **This report is the whole of what the coding side says back.** Every count it names is at the
> artifact or the object it cites, and no population, member list or verdict is restated from one
> (**D-431**).
>
> **★ NOTHING IN THIS BATCH STOP-REPORTS, AND THAT IS THE HEADLINE.** Every ordered act was
> performed; all four registered expectations are MET; both declared assumptions were checked before
> the acts that rest on them and both CONFIRMED; the third was answered by measurement. **The
> condition two batches reported and the last one diagnosed is fixed and the fix is demonstrated by
> running it, not inferred.** §4 is the one thing a reader should not skip: it is a consequence of
> the act rather than a defect, and it is declared here because a mechanism's guarantee is only as
> good as the next reader's knowledge of it.
>
> **This is the first report to land as an ordinary tracked file** — Task 1 removed the rule that
> would have ignored it.

---

## 1. The second ignore rule is removed, and what became visible is measured rather than estimated

§3 orders the line `/cc_instruction_*.md` removed from `.gitignore` and **no other line moved**. Done
exactly: the object-level numstat on the one path is **0 insertions, 1 deletion**.

**The rule's absence is demonstrated at a hypothetical name, not at any file on disk** —
`git check-ignore -q cc_instruction_hypothetical_future.md` exits non-matching — so what is tested is
the rule rather than the tree, which is what registered expectation **E1** asks for.

**The declared consequence, measured (Task 1 step 3).** The sanctioned changed-path enumeration went
from **548** records to **831**, and **284** of those are `cc_instruction_*.md` files that now show
untracked. The arithmetic closes without residue: 548 − 1 (the batch-return ruling record, which Task
0 tracked) + 284 = 831. **`cc_e2d_*.md`: ZERO newly visible**, that rule being untouched as ruled.

**NOT ONE of the 284 is landed by this batch.** They ride their classes' verdicts and the
caller-check sequence exactly as the remaining ignored files do, which is what §3 states.

---

## 2. ★ THE [[OI-373]] CLEARING ACT — performed whole, and the retired block it needed is now a mechanism rather than a hole

§2 permits the coherent one-act version under **D-436**, for that act alone. It is performed.

**A1's check, at the tool read IN FULL and before anything was written.**
`tools/audit/gen_discard_records.py`'s authored table carried three pointers, of which **exactly ONE
names [[OI-373]]**; neither of its two negative seeds touches that row. **A1 CONFIRMED**; the
STOP-and-report the dispatch attaches to a different count was not owed.

**The act.** The pointer moved **WHOLE** into a **RETIRED block added to the tool**, which carried
none — the shape two sibling tools already use for the same case. It carries the reason it left, the
date, and this dispatch's name. **Nothing is destroyed (#12):** every field of the pointer is
preserved, including a record that it conformed while it stood, and **the 2026-08-12 discard record
in the detail file is untouched — not one word of it is withdrawn or rewritten.** The INDEX row was
flipped RESOLVED with provenance in the same act; the detail file gained a dated remark and **never a
status**. **No other row was touched.**

**The discard verdict is SUPERSEDED, not withdrawn**, and the record says so in those words. It was
correct while it stood: the finding was judged not worth fixing under the worth test, and was then
fixed anyway as the extension of a different ruling. What retires the pointer is the row closing,
never the verdict being wrong.

### ★ 2.a THE ONE THING IN THIS BATCH A READER MUST KNOW ABOUT — the retired block is a new authored surface in a tool the gating derivation reads

A retired block with no guard is a route by which a discard record silently stops reaching a derived
gate. That is the same shape as the unregistered-guard condition [[OI-373]] itself recorded, so it
was closed in the act that created the block rather than left for a later pass:

- **A retired pointer naming a row that is OPEN at the INDEX halts the tool.** This is the one case
  the block must never be used for — while a row is open its discard record belongs in the live
  table, and retiring it there would take it out of the cut with nothing saying so.
- **A row carrying a pointer in BOTH tables halts it.** One record per row, in exactly one table.
- **Each NOT-DISCARDED negative seed is now tested against the retired block as well as the live
  table.** Retiring a pointer for a negative outcome is the only way this block could satisfy the
  completeness STOP with a record that was never a discard, and that route is now closed.

**The refusal that caught the incoherence is not otherwise changed** — a pointer left in the live
table for a row RESOLVED at the INDEX still halts the tool, exactly as before.

**The completeness scan still FINDS the row on BOTH register surfaces** — the preserved former status
carries the discard mark and the detail file keeps its heading — and it is the retired pointer that
accounts for it. That was verified at the regenerated artifact rather than assumed, and it is the
behaviour the scan's own STOP wording already provided for (*"or say at the row why it is not one"*).

### 2.b Two derived artifacts moved, and the movement is proven at the objects to be one line each

Taking a member out of the open-row population stopped
`tools/audit/nongating_apparatus_rows.json` and `tools/audit/phase1_completion_inventory.json`
re-deriving. **Both were re-derived by their own generators and neither was edited by hand**, and each
re-derives on an immediate second run.

**Rather than regenerate and move on, the movement was established at the objects:** the pre-edit
blobs were fetched at an explicit hash before the regeneration, and `git diff -U0` between the Task 1
and Task 2 commits reports **exactly ONE changed line in each file** — the open-row count, 243 → 242 —
**and nothing else.** No verdict, no cut, no gating population and no authored table moved:
[[OI-373]] carried a verdict in neither file. This matters because a row flip that quietly shifted a
gate population would look identical to one that did not.

**Registered expectation E2 — MET on both limbs:** `gen_discard_records.py --check` passes; the full
guard set reports one FAIL ([[OI-372]]) and zero STOPs; and [[OI-373]]'s INDEX status cell now opens
with the canonical resolved mark, which the standing status lint confirms on every run.

---

## 3. The guard-staleness fix, at the printing side — and it is demonstrated, not argued

**A2's check, at the runner and before the edit.** `tools/audit/gen_guard_state.py` carries, verbatim:

> `HEAD_SHA = re.compile(r"\bHEAD [0-9a-f]{7,40}\b")`

and the comment standing beside it states the very failure this line reproduced:

> *"A guard that stamps the current HEAD into its own output makes this artifact unreproducible BY
> CONSTRUCTION: committing it changes HEAD, so the next --check reports drift that is not drift. …
> The sha is normalized in the CAPTURED output only — narrowly, by pattern, so nothing else is
> touched, and the reported pass/fail is untouched either way."*

**A2 CONFIRMED**, and the printed shape was matched to the pattern AS READ rather than to the
assumption about it.

**The edit is one word plus the reason for it.** `tools/audit/gen_artifact_inventory.py`'s live half
now prints the current head as `HEAD <sha>`, the shape that existing normalization reaches. **The
runner is NOT edited and its normalization is NOT widened** — the ruling's own smaller act. Nothing
else about the tool's behaviour changes: no classification, no signature, no STOP and no artifact
field moves, and the write path is untouched.

**The OTHER hash on the same line is deliberately left bare, and the code says why.** It comes from
the committed artifact rather than from the tree, so it does not move when anything is committed, and
normalizing it would hide a real change — the artifact being re-derived at a different commit is
exactly what a reader of the guard state must still be able to see. A comment also records why the
word `HEAD` is load-bearing, so a later session does not tidy away a token that looks like a wording
choice.

### ★ 3.a Registered expectation E3, graded by running it

**The hard limb — MET.** After this batch's final content commit (`7bd59e14a2`), a fresh
`gen_guard_state.py --check` was run and read. It prints, in its own opening words, **"the guard state
re-derives"**, and its summary line reports 48 guards run with one failing and no STOP. **The
commit-hash line is no longer a difference.** The property was also demonstrated one commit earlier:
the artifact regenerated at the pre-Task-3 tree re-derived at the Task-3 commit, which is a genuine
commit boundary rather than a same-tree re-run.

**The report limb — NO staleness remains at that tree, on any line.** The runner reports no drift at
all, so **assumption A3 is CONFIRMED at this tree**: the commit-hash line was the only cross-commit
staleness cause. The second candidate A3 names, the untracked-appendix line, does vary with the
working tree but is currently stable at *"has moved"*, and it did not move across any commit in this
batch. **What is NOT claimed:** that the appendix line can never flip — it reports a comparison
against a working tree, so a tree that made it agree again would change the captured text. That is a
bounded and visible condition, not a defect this batch found, and **no loop of regeneration was run
to make any check pass.**

`guard_classification.json` is byte-unchanged throughout, which is the expected outcome when only
captured text moves and never a verdict; it re-derives at the final tree too.

---

## 4. The guard set, both states

**AT THE START** (run before the first edit): **48 guards run, 47 passing, ONE failing** —
`gen_filing_convention_application.py --check`, which is [[OI-372]], rowed and discarded — 4 not run,
10 historical records, and **NO STOP of any kind**. The classification re-derives. The runner reported
the committed `guard_state.json` **STALE** against its own run. **This is exactly the state the
dispatch declares as expected**, the STALE included and for the diagnosed reason, so no
STOP-and-report was owed.

**The working tree carried NO tracked modification at all** — 548 records, every one untracked — so
`cowork_handoff.md` was UNMODIFIED on disk and Task 0's STOP did not fire.

**AT THE END** (run after the final content commit): **48 guards run, 47 passing, ONE failing — the
same one, [[OI-372]] — and NO STOP of any kind.** The classification re-derives beside it. **And the
STALE is gone.** The only red this batch leaves is the one it found, untouched.

---

## 5. The per-task record, with every commit verified at the object

**Every commit is pushed to `origin` and verified at the object by explicit hash through
`git diff-tree --no-commit-id --name-only -r`.**

| Task | Commit | Paths | What it did |
| --- | --- | --- | --- |
| 0 | `06cc33427d` | 2 | the ruling record and this dispatch enter git |
| 1 | `e1a313925e` | 1 | `/cc_instruction_*.md` removed from `.gitignore` |
| 2 | `83312c18b6` | 6 | the pointer retired whole, the row flipped, two derived artifacts re-derived |
| 3 | `0895883778` | 2 | the printing-side fix, and the guard state regenerated |
| 4 | `7bd59e14a2` | 2 | four `STATUS.md` pointer entries and the full close |

**Task 0 — E0 MET.** Exactly the two paths the dispatch names and no third, verified at the index
through the sanctioned enumeration before the commit and at the object after it. The dispatch itself
was staged with an explicit override for the last time.

**Task 1 — E1 MET on all three limbs.** Path count 1; one line deleted and none added; the rule's
absence demonstrated at a hypothetical name. See §1.

**Task 2 — E2 MET on both limbs.** See §2.

**Task 3 — E3 MET on both limbs.** See §3.a.

**Task 4 is TWO commits, and the reason is E3 itself.** Its hard limb asks for a run made **after this
batch's final commit**, demonstrated by running it and reading what it prints. A report written
before that run would have had to predict its result. So the `STATUS.md` entries and the close landed
first as the final content commit, the run was made at that tree, and this report — which carries the
observed result — lands second. Each commit names its own act.

---

## 6. What this batch did NOT do

- **No `src/` edit, no golden, no test changed, moved or run**; nothing under `tools/corpus/` or
  `tools/robust_stop/`; **no measurement of the analysis built, designed, scoped or run; no design,
  no repair, no fix to inference.**
- **No open-items row created, flipped or discarded except the one Task 2 orders.** [[OI-372]] stays
  exactly as found — open, undischarged, and the one standing red. [[OI-374]] is untouched.
- **No decisions-register entry written** (the filtering ruling stands).
- **No file archived, retired, renamed or deleted** — beyond the one authored pointer's move into its
  retired block, which destroys nothing. **The 284 newly visible instruction files are NOT landed**,
  the remaining ignored files are NOT landed, and **the caller-check is NOT started.**
- **No mining, no findings ledger, no register filter, no phase drafting, no pilot, and no write-back
  of ruled verdicts onto the inventory's generated surface** — the ruling records remain the carrier.
- **No edit to `gen_guard_state.py`**, and **no verdict or change authored for any tool this batch did
  not read in full.**
- **[[OI-179]] stays OPEN and GATES. D-231 and #8 stand.**

---

## 7. The standing self-check (D-434) over this batch's own work

Run against the diff on disk rather than against the memory of writing it.

1. **★ THE ACT'S DERIVED CONSEQUENCES WERE PROVEN, NOT ASSERTED** — §2.b. Two committed artifacts
   moved when the row flipped. The easy path was to regenerate and report that they re-derive; instead
   the pre-edit blobs were fetched at an explicit hash and the committed movement diffed at the
   objects, which is what establishes that a gate population did not shift behind a row flip.
2. **★ THE RETIRED BLOCK WAS GIVEN ITS OWN STOPS IN THE ACT THAT CREATED IT** — §2.a. The dispatch
   ordered a retired block and did not order guards on it; a block without them is a silent route out
   of a derived gate, which is the shape the row being closed was itself about.
3. **THE SUPERSESSION IS NAMED AS ONE.** A retirement that read as a withdrawal would have destroyed
   the record that the worth test was applied and answered (#12), so the wording says in terms that
   the verdict was correct while it stood.
4. **THE ONE WORD WAS GIVEN ITS REASON IN THE CODE** — §3. A load-bearing token that looks like a
   wording choice is a token a later tidy-up removes.
5. **ON D-253 IN EVERY DIALECT.** Every read of repository content went through Read / Grep / Glob.
   The shell was used for the guard runs and the tools' own runs, `git add` / `git commit -F` /
   `git push`, the sanctioned changed-path enumeration, and `git show` / `git diff` between commits
   named by explicit hash; line counts were taken only on scratchpad files OUTSIDE the repository.
   **One attempt was refused by the guard and the refusal was correct**: a `tail` reaching a scratchpad
   file through a relative path after a `cd`, which the guard could not tell from a repository path —
   the file was read with the file tools instead.
6. **ON THE FIGURES RULE (D-431).** Every value above names the artifact or the object it was read
   from, and no population, member list or verdict is restated from one.
7. **ON THE RESERVED-WORD CONVENTION.** Bare *score*, *key*, *measure*, *note*, *mode*, *register*,
   *root*, *part*, *rest*, *figure*, *interval*, *scale*, *beat*, *tie*, *stem*, *flat* and
   *instrument* appear in no non-musical sense in this batch's new prose: *measurement* carries the
   gauging sense, *value* the numeric one, *remark* the annotation sense, *the open-items register*
   and *register entry* are always compound, *`--check` mode* is always qualified, and *tool* is used
   where *instrument* would have collided. **Two inherited terms are carried knowingly**: a row's
   *resolution*, the open-items register's own word for the act rule (d) names, and *contract*, the
   record's own name for a ratified specification document.
8. **NOTHING WAS REGENERATED IN A LOOP TO MAKE A CHECK PASS.** Each regeneration was a single act with
   its cause named, and each was followed by an independent re-run that had to agree.
9. **WHAT THE SELF-CHECK DID NOT RESOLVE**, stated rather than left implicit: [[OI-372]] is untouched,
   as ordered, and its defect is undischarged; [[OI-374]], the guard set's own encoding exposure, is
   untouched as it was found; the 284 newly visible instruction files are unlanded and unclassified by
   this batch; the class-1 recognizers' reach from the previous batch remains unmeasured, its artifact
   saying so of itself; and the ruled verdicts are still not written back onto the inventory's
   generated surface.
