# CC dispatch — fix the guard, rule the removal shape, re-cut the finish line

> **Status: ACTIVE DISPATCH, written 2026-08-04 (Cowork).** Read IN FULL.
>
> **★ CITE THIS FILE BY ITS EXACT NAME** — `cc_instruction_guard_fix_and_item1d.md`.
>
> **★ THE FREEZE IS NOT RELAXED.** Task 1 repairs a mechanism, and it is licensed by **D-641's own
> stated exception** — an establishment obligation (#19) always gates — and by **D-436**, which makes
> changing a mechanism that fails a measured condition the user's ruling. That ruling is given at R1.
> **Everything else found this wave is rowed and left.**
>
> **★ NO FIGURES (D-431) AND NO STATE NOT READ (#17a).** No `src/`, no goldens, no corpus, no
> behaviour change to the analysis, no fix to inference, no design. Phase 1 under D-231.
>
> **★ Item 2 is not started. Phase 1's completion statement is not written, drafted, or partially
> written.**

## 0a. THE RULING LEDGER

- **R1 — RULED by the user, 2026-08-04.** **Fix the shell-read guard**, and **extend its establishment
  corpus with the shapes that defeat it BEFORE any rate is republished.** Re-establishing against the
  same corpus would repeat the error being fixed: the current `--establish --check` passes precisely
  because the corpus omits the defeating shape, so the published false-negative rate is not a bound on
  the true one.
- **R2 — RULED, same act.** Where a superseded decision's content is a **removal**, the owning
  specification **states the current behaviour and records the removal as a tried-and-closed line**;
  the register holds the status. **This is precedent, not a new rule** — it is what was done at
  `ARCHITECTURE.md` §5.2 for the piece-start shortcut (OI-315 / D-058).
- **R3 — RULED, same act.** **Re-cut the finish line at ENTRY granularity.** C1 is a statement about
  decisions, not documents; the document cut was a convenience and now misreports the work.

**None of R1–R3 authorizes a fix to the analysis, a design, or an inference change.**

## 0b. THE PREMISE LEDGER (#17a)

**FACT — established at the object by Cowork this session:**

- **F1.** The guard **admits** `grep -n "alpha|beta" src/composing/analysis/key/keyresolver.cpp` and
  **denies** the identical command without the pipe. Run by Cowork against `shell_read_guard.py`'s own
  decision path. The defeating shape is **any pipe inside a quoted argument**, not only the escaped
  alternation found earlier.
- **F2.** The precedent R2 rests on: `ARCHITECTURE.md:3510-3525` states what the opening does at HEAD
  and records the removal as a tried-and-closed line, after the specification had asserted the removed
  mechanism in the present tense.

**ASSUMPTION — each checked before the act it licenses:**

- **A1.** That the cause is `shlex` being applied at `tokenize()` while the **segment split still runs
  over raw text**, and that applying tokenization before the split fixes it. **This is CC's diagnosis
  and Cowork's inference, not a read of the code by Cowork.** → **Task 1.1**; **if the cause differs,
  report it and fix the cause found, not the cause assumed.**
- **A2.** That item 1's re-home class is blocked by **edit-surface licensing** rather than by genuine
  owner ambiguity — the reasons carry *"outside this dispatch's edit surface"*. → **Task 4.1**.

## 1. Task 1 — Fix the guard, corpus first (R1)

**1.1** Discharge A1 at the code. Report the cause found.

**1.2 Extend the establishment corpus FIRST**, with the defeating shapes: a pipe inside a quoted
pattern, the escaped alternation, and the heredoc and redirection shapes OI-300 already records.
**The corpus must contain the cases that broke it before any rate is measured** — otherwise the new
rate is as uninformative as the old one.

**1.3** Fix the cause. **1.4** Re-establish and publish **both** rates against the extended corpus.
**If the fix raises false denials materially, revert and report** — a guard that blocks correct
commands gets disarmed, which is worse than one with a known gap.

**1.5** Record on OI-343 that the previous rates were measured against a corpus omitting the shape, and
that this is why they passed. **The old figures are not withdrawn as wrong; they are recorded as not
bounding what they appeared to bound.**

## 2. Task 2 — Record and apply R2

**2.1** Record R2 where the C1 criteria live, beside R1's superseded-reach block, quoting F2's
precedent rather than paraphrasing it.

**2.2** Apply it to the one item-1 member whose content is a removal and which has no successor the
record names. Report what the owning specification would have to say — **do not write specification
text here unless the owning section is unambiguous and within this dispatch's edit surface**, in which
case write it in that section's own voice with its defense.

## 3. Task 3 — Re-cut the finish line (R3)

Re-cut at entry granularity, and report the movement against the document cut in both directions.
**The finish line's own scope rule applies: populations move when the record moves, and only adding an
item needs a ruling.** Re-cutting an existing item is not adding one — state that in the artifact so a
later reader does not mistake it for a scope change.

## 4. Task 4 — Item 1's real blocker (A2)

**4.1** Establish what the re-home class actually needs: **which files** the owning specifications sit
in, and whether the blocker is that those files were outside a dispatch's licensed edit surface or
that the owner is genuinely soft.

**4.2 Report the edit surface the class requires.** Do not widen it here — that is a scope question
and it comes back to the user with the list of files and what each would receive.

## 5. Task 5 — Close

Guards at the committed tree with the list `gen_guard_state.py` derives; report and **fix none beyond
Task 1**. Re-aim any anchor this wave's edits drift, per citation. Verify what is committed through
`tools/audit/changed_paths.py`. Run `tools/audit/process_check.py` over this dispatch. `STATUS.md`
gains one POINTER entry.

**Everything else found is rowed and left** unless it bears on the analysis, its inputs or a
measurement instrument — in which case it is **surfaced, not acted on**.

## 6. Accepted outcomes

**A1 finding a different cause is expected and is why it is checked.** **The fix raising false denials
is a revert-and-report, not a judgment call.** **Task 4 finding the blocker is genuine owner ambiguity
rather than licensing is a result** — it would mean the re-home route is narrower than the routes
artifact suggests.

## 7. Self-check (D-434) — run by Cowork before release

- **R2 applied.** F1 is Cowork's own run, not a report's claim; F2 quotes the precedent's location
  rather than a summary of it. R2 quotes the precedent in full at its home rather than the part that
  helps.
- **Ruling ledger.** Three rulings; R1 states why corpus-before-rate is not optional.
- **#17(a).** Two facts established at the objects. Two assumptions — A1 because Cowork inferred a
  cause it did not read, A2 because the blocker's nature comes from a phrase in a report.
- **Principles.** #19 — the corpus is extended before the rate is trusted. D-436 — the mechanism change
  is the user's ruling and is cited as such. D-641 — its stated exception is what licenses Task 1, and
  the header says the freeze is not otherwise relaxed. #12 — old rates recorded, not withdrawn.
