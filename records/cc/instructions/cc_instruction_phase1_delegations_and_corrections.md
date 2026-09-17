# CC dispatch — derive the real delegation population, and apply three rulings

> **Status: ACTIVE DISPATCH, written 2026-08-04 (Cowork).** Read IN FULL.
>
> **★ CITE THIS FILE BY ITS EXACT NAME** — `cc_instruction_phase1_delegations_and_corrections.md`.
>
> **★ NO FIGURES (D-431) AND NO STATE NOT READ (#17a).** No `src/`, no goldens, no corpus, no
> behaviour change, no fix to inference, no design. Phase 1 under D-231, gate at `CLAUDE.md` #8.
> The freeze holds except where a task names an exception.
>
> **★ PHASE 1's COMPLETION STATEMENT IS NOT WRITTEN HERE.**

## 0a. THE RULING LEDGER

- **R1 — RULED by the user, 2026-08-04.** Phase 1's TRUE half **reaches a document's account of
  itself ONLY where that account changes how the document's ANALYSIS content is read** — an
  "as-built" banner over a dormant mechanism, yes; a missing supersession note on a superseded plan,
  yes; a stale anchor or a formatting artifact, no. **With a stated fallback:** if the test needs
  judgment on the first rows it meets, it is the "stable enough to be cited" failure again and
  **option (1A) — the TRUE half reaches only the account of the analysis — is the fallback.**
- **R2 — RULED, same act.** The phase-1q record is **snapshotted and the snapshot ESTABLISHED as
  faithful BEFORE** `gen_home_classification.py`'s apply mode is run. Then it is run. This is the
  O-12 pattern gate block (A) already uses, and it is the freeze's one exception here.
- **R3 — RULED, same act.** **OI-334's three false statements are corrected**, and the hand-carried
  residual figure is made **computed** rather than authored (#17f).
- **R4 — RULED, same act.** The outstanding delegation population is **DERIVED at HEAD** from the
  delegation grades and the home data — **never taken from the write list**, which carries no state
  and therefore cannot distinguish written from unwritten.

**None of R1–R4 authorizes a fix to the analysis, a design, or an inference change.**

## 0b. THE PREMISE LEDGER (#17a)

**FACT — read at the object by Cowork this session:**

- **F1.** `tools/audit/decisions/backbone_decisions.json:644-653` — the `write_list` entries carry **no
  status field**, and the first entry still describes its pre-write state: its `current_delegation`
  is the bare *"Full spec:"* citation and its `why_the_bar_excludes_it` still asserts the exclusion.
- **F2.** Delegations exist at `ARCHITECTURE.md:53` (pre-fit gates), `:1242` (Layer-1 note model) and
  `:1500-1502` (Layer-5 function) — read at the file.
- **F3.** `tools/audit/phase1_completion_inventory.json` → `the_shape_of_what_remains.complete_half`
  reports the awaiting-a-delegation figure as **equal to the write list's membership**.
- **F4.** D-231's phase-1 clause at `CLAUDE.md:1117-1121` carries C4 (*conformance thereafter measured
  against the specifications themselves*) and C5 (*because a specification cannot be the compliance
  standard while it misdescribes the code*).

**ASSUMPTION — each checked before the act it licenses:**

- **A1.** That the inventory produced its figure by counting write-list membership. Cowork infers this
  from F1 and F3 together and **has not read the generator**. → **Task 1.1**.
- **A2.** That the other seven write-list documents are written and satisfy the bar. **Cowork verified
  three at the file (F2); the rest come from wave reports.** → **Task 1.2**, per document.

## 1. Task 1 — Derive the real population (R4)

**1.1** Check A1 at the generator and report how the figure was produced.

**1.2** Check A2 **per document**: for each write-list member, does a delegation exist at HEAD, and
does it satisfy the bar? **Written is not closed** — the voice-leading widening deliberately excluded
§15/§16 and the home-classification check still reports a write-list document holding a `gap` entry,
so a document may be partly closed. Report per document: written / partly closed / outstanding /
ruled-not-a-target, each with the evidence at the file.

**1.3** Then **derive, from the delegation grades and home data at HEAD**, which documents still lose
entries for want of a delegation. That derived set — not the write list — is what goes to the user.
Publish it as an artifact with a draft wording per member and what each closes.

**1.4 Row the stale figure.** A recorded finding that is never marked discharged produced a count of
outstanding work that measured membership instead — the OI-283 shape, inside the artifact a completion
statement would rest on. **Give the write list a state field, or retire it in favour of the derived
view** — CC's call, with the reason recorded.

## 2. Task 2 — R1: classify OI-332 under the ruled test

Apply R1's test to OI-332's three documents: does each one's self-statement **change how its analysis
content is read**? Report per document with the reason.

**If the test does not decide them cleanly, say so and STOP applying it** — R1's own fallback is that
this would be the judgment-clause failure repeating, and option (1A) then governs. **Do not stretch
the test to reach a verdict.**

Record the ruling and its fallback where the TRUE half is defined, so a later row is classifiable
without a fresh ruling.

## 3. Task 3 — R2: snapshot, establish, then apply

**3.1** Snapshot the phase-1q record that OI-305 warns the apply mode destroys.

**3.2 Establish the snapshot as faithful BEFORE the destructive run** — verify it reproduces what the
committed artifact holds. **If it does not, STOP**: running the applier would then destroy a record
whose copy is not established, which is the loss OI-305 exists to prevent.

**3.3** Run the apply mode. Report what it grades and what moves.

**3.4** Update OI-305 and OI-319 with the outcome, and record that the exception was **exercised under
R2**, not that the freeze relaxed.

## 4. Task 4 — R3: correct the register's account of itself

Correct all three statements OI-334 records as false, at their own place in `DECISIONS.md`'s scope
block, and **make the residual figure computed** rather than an authored string (#17f). Preserve the
former wording (#12). Flip OI-334.

**Do not restate any figure in prose** — cite the computed field.

## 5. Task 5 — Close

Guards at the committed tree with the list `gen_guard_state.py` derives; report what fails and **fix
none beyond Tasks 1.4 and 3 where they are licensed**. Re-aim any anchor this wave's edits drift, per
citation. Verify what is committed through `tools/audit/changed_paths.py`. Run
`tools/audit/process_check.py` over this dispatch. `STATUS.md` gains one POINTER entry.

## 6. Accepted outcomes

**Task 1.3 finding the real population EMPTY is a result** — it would mean the delegation work is done
and only the stale figure suggested otherwise. **Task 2 stopping at its fallback is a success.**
**Task 3.2 failing is a STOP**, and the applier does not run.

## 7. Self-check (D-434) — run by Cowork before release

- **Ruling ledger.** Four rulings, with R1's fallback stated in the ruling rather than left to
  judgment.
- **#17(a).** Four facts read at the objects. Two assumptions — A1 because Cowork inferred a
  derivation it did not read, A2 because Cowork verified three delegations of ten at the file and took
  the rest from reports. **Both are the exact shape that produced the stale figure**, so both are
  checked before anything rests on them.
- **Principles.** #12 — snapshot before the destructive run; former wordings preserved. #17(f) — the
  residual figure becomes computed. #19 — the snapshot is established before it is relied on. D-599 —
  no alternatives offered where the principles decide.
