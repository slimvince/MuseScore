# CC dispatch — commit the backlog, derive the finish line, install the surfacing rule

> **Status: ACTIVE DISPATCH, written 2026-08-04 (Cowork), on the user's ruling of the same date.**
> Read IN FULL.
>
> **★ CITE THIS FILE BY ITS EXACT NAME** — `cc_instruction_commit_and_finish_line.md`.
>
> **★ THIS DISPATCH DOES THREE THINGS AND NOTHING ELSE.** It commits, it derives one list, and it
> homes one rule. **Do not fix anything you find.** If a task tempts you to repair something, that is
> the behaviour this dispatch exists to stop.
>
> **★ NO FIGURES (D-431) AND NO STATE NOT READ (#17a).** No `src/`, no goldens, no corpus, no
> behaviour change, no fix to inference, no design. Phase 1 under D-231.
>
> **★ PHASE 1's COMPLETION STATEMENT IS NOT WRITTEN HERE.** Task 2 derives what completion would
> REQUIRE. That is a different artifact and the distinction must stay sharp.

## 0a. THE RULING LEDGER

- **R1 — RULED by the user, 2026-08-04, at OI-337.** **Commit the whole backlog as one act.** The six
  waves cannot be separated — each layers on the last — so the available acts were all or none, and
  the user has ruled all.
- **R2 — RULED, same act.** **Derive the finish line**: one statement, freshly computed, of exactly
  what phase 1 still requires. **That list is then the scope.** Nothing outside it gets a wave.
- **R3 — RULED, same act. The standing surfacing rule.** A finding whose subject **bears on the
  analysis, its inputs, or an instrument a measurement depends on** — D-438's own test — is
  **SURFACED to the user for decision, whatever its size**. A finding that does not is **rowed and
  left: no wave, no dispatch, no surface.** D-438 already says such rows gate nothing; what R3 adds is
  the duty on the other side, and the prohibition on spending a wave on the first side.

**None of R1–R3 authorizes a fix, a design, or an inference change.**

## 0b. THE PREMISE LEDGER (#17a)

**FACT — read at the object by Cowork this session:**

- **F1.** D-438's test is at `CLAUDE.md:206-215`: *"does the row's subject bear on the analysis, its
  inputs, or an instrument a measurement depends on? IF YES IT GATES"*, with apparatus rows gating
  nothing and **an establishment obligation (#19) always gating, whatever its subject.**

**ASSUMPTION — each checked before the act it licenses:**

- **A1.** That the backlog is six waves, that HEAD is still the read-wave-3 commit, and that the six
  are inseparable. Cowork has this from a session report. → **Task 1.1**.
- **A2.** That `phase1_completion_inventory.json`'s COMPLETE-half figures are now **stale** — the
  applier has since run and the census delegation has since moved six entries. **The finish line must
  be RE-DERIVED, not reused.** → **Task 2.1**.

## 1. Task 1 — Commit (R1)

**1.1 Discharge A1.** Enumerate what is uncommitted through `tools/audit/changed_paths.py` and report
it. **If the backlog is not what A1 says, report that and commit what is actually there** — the
ruling is "all of it", not "the six named".

**1.2** Commit by git plumbing as one provenance-stamped commit. **Re-run every guard at the
committed tree** with the list `gen_guard_state.py` derives, and report the state.

**1.3** OI-337 records what is uncommitted and **is not wave work** — including the untracked dumps
inside `tools/robust_stop/`, the directory gate block (A) names as the committed reference. **Report
their disposition; do not act on them.** Whether they belong in that directory is a question about a
measurement reference and therefore an R3 surfacing item, not a tidy.

## 2. Task 2 — Derive the finish line (R2)

**2.1 Re-derive, do not reuse.** Compute afresh, at HEAD:

- the **COMPLETE half** — entries not homed in an owning specification, and entries whose defense the
  record does not state;
- the **TRUE half** — open rows asserting a specification states something false at HEAD, under R1 of
  the C5 ruling already in force;
- the **gating split** across both, by F1's test;
- anything D-231's clause requires that neither half carries — **read the clause again rather than
  reusing the earlier reading of it.**

**2.2** Publish it as one artifact, and state per item: what it is, which half, whether it gates, and
**what act would close it**. An item with no closing act named is not on the finish line — it is a row.

**2.3 The list is the scope.** Record in the artifact that nothing outside it gets a wave, and that
additions to it require a user ruling. That is what makes it a finish line rather than a snapshot.

**2.4 Do NOT write phase 1's completion statement.**

## 3. Task 3 — Home the surfacing rule (R3)

Home it in `cowork_audit_protocol.md`'s dispatch-protocol section, beside D-431, D-434, D-436 and
D-640, with a register entry in the same commit.

Its text carries both halves and the reason: **the apparatus is now large enough to generate its own
defect stream indefinitely, and treating each defect as owed is what produced a six-wave backlog while
the findings that bear on the objective came from reads and probes, not from apparatus repair.**

**State the exception plainly:** an establishment obligation (#19) always gates and is therefore always
surfaced, whatever its subject — R3 does not weaken that.

## 4. Task 4 — Close

Run `tools/audit/process_check.py` over this dispatch. Re-aim any anchor this wave's edits drift, per
citation. `STATUS.md` gains one POINTER entry.

**Report — do not fix — anything found.** The three observations the previous wave left open (the
recomputed proxy correlation, the intermittent guard, the two fresh false-denial shapes) are **R3
apparatus items**: rowed, left, and not surfaced.

## 5. Accepted outcomes

**A1 coming back different is expected** — the ruling covers whatever is there. **A finish line longer
than hoped is the honest result**; the point is that it is finite and derived. **Finding an item with
no nameable closing act is a result** and it belongs in a row, not on the list.

## 6. Self-check (D-434) — run by Cowork before release

- **Ruling ledger.** Three rulings; R3's two halves and its #19 exception stated in the ruling.
- **#17(a).** One fact read at the object. Two assumptions — A1 because the backlog figure came from a
  report, A2 because the inventory predates two acts that moved its inputs, which is the stale-figure
  shape this project keeps producing.
- **Scope.** Three acts, and the header forbids a fourth. This dispatch is itself the first
  application of R3: the previous wave's three loose observations are named as rowed-and-left rather
  than turned into tasks.
- **Principles.** #4 — R3 exists to keep the objective the filter. D-438 — R3 enforces it rather than
  amending it. #19 — the exception is stated. #12 — nothing deleted.
