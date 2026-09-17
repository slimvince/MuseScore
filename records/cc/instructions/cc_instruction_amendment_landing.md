# CC INSTRUCTION — the amendment-landing batch

> **Written by Cowork, 2026-08-26, the forty-ninth session.** You are a fresh Claude Code session.
> **Read this file whole before you touch anything.**
>
> **★ THIS BATCH LANDS FIVE RULINGS OF `cowork_rulings_2026_08_26_amendment_landing_sitting.md`.** It
> changes no behaviour, touches no `src/`, runs no analysis, reads no blind derivation output, and
> **admits nothing to the empirical findings ledger.**
>
> **★ THIS BATCH EDITS `CLAUDE.md` AND ONE TOOL SOURCE. BOTH ARE AUTHORISED BY NAME AND BOTH ARE
> FENCED. Read §0 before either.**
>
> **★ DO NOT RUN `git status`.** The guard refuses it (**D-253**). Use
> **`python tools/audit/changed_paths.py`** (`--staged`, `--commit <hash>`).

---

## 0. THE BARS

**★ THE `CLAUDE.md` FENCE.** You may change **exactly three passages** — principles **#18**, **#19**
and **#24** — and in each you may only **add** the clause the ruling record states for it. **No other
line of `CLAUDE.md` may differ by one byte.** You may not reword the existing principle text, may not
renumber, may not reflow a paragraph you are not adding to, and may not "tidy" anything. **If the
clause cannot be added without rewording what stands, STOP.**

**★ THE TOOL-SOURCE FENCE.** You may edit **exactly one** `.py` file:
`tools/audit/gen_status_batch_bound.py`, and in it only its three authored constants
(`BASE_COMMIT`, `PREVIOUS_BATCH_DISPATCH`, `DISPATCH`) and its `PREVIOUS_AIMINGS` list. **No other
path under `tools/` ending `.py` may be modified.** This carve-out is Ruling 5 and reaches nothing
else.

**★ THE SWEEP RULE, ABSOLUTE.** A **staleness** red is regenerated. A **decision** red is **never**
regenerated. **If you cannot tell which kind a red is, treat it as a DECISION red and STOP.**

**★ [[OI-372]] — `gen_filing_convention_application.py --check` — IS THE ONE STANDING DECISION RED.**
Never regenerate it, never run it in write mode, never author a verdict for it. **Any other decision
red: STOP.**

**★ EXPECT A LARGE SWEEP AND DO NOT BE SURPRISED BY IT.** This batch changes **three** existing
register entries and adds **four** new ones. The measured blast radius is **five artifacts per
register row**, two of which move without ever appearing in a failing set because two guard-set
members run in living mode. **Amending `CLAUDE.md` also changes the session-start read**, which has
its own measurement. Report everything that moved, not only what went red.

**★ ADMISSION IS NEVER YOURS.** This batch does not touch
`cowork_empirical_findings_candidates.md` and does not build the ledger.

**★ MEASUREMENT BARS.** A worktree hash and a blob hash do not agree for a CRLF file — **always say
which side you measured**. **Never write a file's own hash into that file.** Every count, size and
hash in your report carries the command that produced it.

**★ VOCABULARY.** **"Measurement tool"**, never *instrument*. **"A changed passage"**, never *hunk*.
**"The current commit"**, never a bare *HEAD*. **"Untrusted source"**, never *witness*. Rate options
**"toward the objective"** and **"counting against the objective"**, never a bare *against*.

---

## 1. RULING LEDGER

All five rulings are in **`cowork_rulings_2026_08_26_amendment_landing_sitting.md`**, on disk at the
root, landing at your Task 0. **Read that record whole before Task 2.** In summary — and the record
governs, not this summary:

- **Ruling 1** — the three ruled clause amendments land at their **home file, `CLAUDE.md`**, at #18
  (D-181), #19 (D-182) and #24 (D-187). The clause texts are quoted at
  `cowork_rulings_2026_08_25_regress_termination_sitting.md:69–88`.
- **Ruling 2** — only the **unregistered residue** of the sharpened decision-surface rule is
  registered, as **one** entry, **cross-referencing D-424 and D-249** rather than repeating them.
- **Ruling 3** — **three register rows**: the method-usable-for-v1 verdict, the
  independence-evidenced verdict, and the phase-status change.
- **Ruling 4** — every new entry goes to **group T**.
- **Ruling 5** — `gen_status_batch_bound.py` is re-aimed, and the row missing for the 2026-08-26 hand
  move is backfilled.

---

## 2. DECLARED START STATE — measure it, report it, assert nothing

- **Tip expected:** `8c744a890d83fd7f035a9d07c19ba1f120f90098`. **If it differs, STOP.**
- **Tracked, modified: expected NONE.** The previous batch closed with zero tracked modifications.
- **Untracked root-level, expected THREE:** `cc_report_register_reconciliation.md` if it is not yet
  committed, `cowork_rulings_2026_08_26_amendment_landing_sitting.md`, and **this instruction file**.
  Report what you actually find.
- **A standing untracked population of roughly 831 paths**, already routed, **never committed.**
- **Guard set expected at 75 run / 74 passing / 1 failing**, [[OI-372]] alone. **The previous batch
  predicted this report's own family may present as a fourth unclassified candidate to that red —
  if it does, that is the STANDING red widening, not a new one. Report it and do not author a verdict.**

---

## 3. ASSUMPTIONS — declared so you can falsify them

- **A1** — register **rule (n)** exists in `CLAUDE.md` and makes the register its own home for an
  establishment verdict with its evidence pointed at a ruling record. **This side could not verify it
  and did not. See Task 2.**
- **A2** — the three clauses can be added to #18, #19 and #24 **without rewording any existing
  sentence**.
- **A3** — `backbone_decisions.json`'s `verbatim` and cited-line fields for D-181, D-182 and D-187
  are the only fields needing change when their home text grows.
- **A4** — four consecutive identifiers are free at allocation time. The previous batch measured the
  next free as **D-678**; **re-measure, do not inherit it.**
- **A5** — the sweep reaches a fixpoint within four rounds.

---

## 4. TASKS

### Task 0 — land the writing-side files

Commit `cowork_rulings_2026_08_26_amendment_landing_sitting.md` and **this instruction file**, plus
`cc_report_register_reconciliation.md` if it is still untracked. Nothing else. **Do not assert the end
state in the message.**

### Task 1 — measure the start state (§2)

`python tools/audit/changed_paths.py`; the three ref files by the file tools; sizes and blob
identities for each untracked root-level file, **stating the side**.

### Task 2 — ★ VERIFY RULE (n) FIRST, BEFORE ANY WRITE

Read the decisions register's own rules in `CLAUDE.md`. **Quote rule (n) verbatim in your report.**

- **If it makes the register a home for a verdict with evidence pointed at a record:** proceed; A1
  holds.
- **If it does not, or if there is no rule (n):** **STOP Task 6's two verdict rows only.** Report what
  the rule actually says and what home it implies. **Task 6's phase-status row does not depend on
  rule (n) and proceeds regardless** — Ruling 3 says so in terms. Tasks 3, 4, 5 and 7 are unaffected.

### Task 3 — amend `CLAUDE.md` at #18, #19 and #24

Read `cowork_rulings_2026_08_25_regress_termination_sitting.md` at Limbs A and B (`:69–88`) and add
each clause **verbatim** to its principle. **The §0 fence binds.**

**Validation:** `git diff --numstat` on `CLAUDE.md` shows changed passages at three sites and no
other. **Report all three changed passages in full.** Report the file's byte count before and after.

**STOP if:** adding a clause requires rewording an existing sentence (A2 falsified); or a principle's
text on disk differs from the text the ruling record quotes for it.

### Task 4 — re-anchor the three register entries and regenerate

Update `verbatim` and the cited line for **D-181, D-182, D-187** in
`tools/audit/decisions/backbone_decisions.json` so each matches its amended home text and start line.
Then regenerate: `python tools/audit/decisions/gen_decisions_register.py`.

**Validation:** `python tools/audit/decisions/gen_decisions_register.py --check` passes, and
`python tools/audit/gen_cluster_dispositions.py --verify` passes — the second is the establishment
check that requires each entry's quote to be found at its cited home and line. **Both must pass before
Task 5.** `grep -n "inspectable" decisions/group_S.md` returns **at least one** match after this task.

**STOP if:** either check still fails after one regeneration, or if A3 is falsified and some further
field must change.

### Task 5 — the decision-surface residue entry (Ruling 2)

**Allocate the next free identifier, MEASURED** — do not inherit D-678. Enter **one** entry in
**group T** carrying **only** these clauses: alternatives must not be reactions to the latest news
taken apart from the larger context and plan; alternatives must not self-generate work; the rating is
written *"toward the objective"* and *"counting against the objective"*, never a bare *"against"*;
one decision per turn; the user rules by letter; **and a surface that fails this is re-put in the
corrected form.**

**It must CITE and not repeat D-424** (the two-axis weighing, pros and cons with their principle) **and
D-249** (the whole surface delivered before any choice question).

**Home:** `CLAUDE.md`, alongside its sibling D-249, **unless rule (n) or the register's own home
convention determines otherwise — in which case report what it determines and follow it.**

### Task 6 — the three rows of Ruling 3

Three entries in **group T**, identifiers allocated consecutively after Task 5's, evidence pointed at
`cowork_rulings_2026_08_25_v1_sufficiency_sitting.md`:

1. **The method is ruled USABLE for v1** on the user's ground — a first specification cannot be the
   ultimate one because the sources are not exhausted until the audit has run, so the best derivable
   from everything held except the code is good enough by construction. **This SUPERSEDES the
   method's VOIDED status.**
2. **Independence of a deriving session from the shipped code is evidenced by the ten DIFFERS rows**
   of `ratification_surfaces/cowork_comparison_harmony_boundary_reading.md` §6.
3. **The framework and detail-specification phases are NO LONGER HELD**; E and C are neither the next
   act nor owed; **the empirical findings ledger is untouched and still owed as a framework-phase
   input.**

Row 3 also **supersedes as the ordering** Ruling 3 of
`cowork_rulings_2026_08_25_regress_termination_sitting.md`. Apply the register's own supersession
convention; **if that convention requires the superseded ruling to have an entry and it has none,
report it and enter neither — that is a question for the user.**

Rows 1 and 2 are gated on Task 2.

### Task 7 — re-aim the forward-bound tool (Ruling 5)

Re-aim `tools/audit/gen_status_batch_bound.py` to this batch: set `BASE_COMMIT`,
`PREVIOUS_BATCH_DISPATCH` and `DISPATCH`, and append its `PREVIOUS_AIMINGS` row. **Backfill the row
missing for the 2026-08-26 hand move** performed by `cc_instruction_register_reconciliation.md` Task 4
— `cc_report_register_reconciliation.md` §5.3 and §5.4 state what that move was.

Then perform this batch's own `STATUS.md` forward bound **with the tool**, and write this batch's
`STATUS.md` entry under the file's own conventions — living document, latest entry only, a **POINTER**
under the OI-222 remedy with no count, no identity and no rendered value restated (**D-431**).

**Validation:** `python tools/audit/gen_status_batch_bound.py --check` passes, and
`python tools/audit/gen_governing_surface_split.py --check --pair STATUS.md` passes.

### Task 8 — the guard set, and the sweep

`python tools/audit/gen_guard_state.py`. **Classify every red before regenerating anything, and say
which kind and why.** Regenerate staleness reds; **STOP on any decision red that is not [[OI-372]]**.
Re-run after each round, **at most four rounds** — this batch moves seven register entries and the
session-start read, so expect more rounds than the last one needed. **If the failing set is unchanged
after four rounds, STOP and report the residue rather than looping.**

**Report everything that moved**, including artifacts that never appeared in a failing set.

### Task 9 — ONE commit

`CLAUDE.md`, `tools/audit/decisions/backbone_decisions.json`, every regenerated register file,
`DECISIONS.md`, `STATUS.md`, `STATUS_ARCHIVE.md`, `tools/audit/gen_status_batch_bound.py`, and
whatever Task 8's runs wrote — and nothing else. **Not one path from the ~831 standing untracked
population.** **Do not assert the end state in the message.**

### Task 10 — the report, in a SEPARATE, LATER commit

`cc_report_amendment_landing.md`. **★ A commit cannot assert its own end state.**

---

## 5. REGISTERED EXPECTATIONS

- **E0** — the Task-0 paths land byte-identical to Task 1, side stated.
- **E1** — `CLAUDE.md` differs at exactly three sites, all three inside #18, #19 and #24, and **every
  change is an addition**; no existing sentence is reworded.
- **E2** — `gen_decisions_register.py --check` and `gen_cluster_dispositions.py --verify` both pass
  after Task 4.
- **E3** — `grep -n "inspectable" decisions/group_S.md`: zero before Task 3, at least one after
  Task 4.
- **E4** — exactly **four** new identifiers exist after Task 6 (or **two**, if Task 2 gated the
  verdict rows), all in group T, none renumbering an existing row.
- **E5** — exactly one `.py` path is modified: `tools/audit/gen_status_batch_bound.py`.
- **E6** — the failing set at the last sweep round is [[OI-372]] alone, or the residue is reported.
- **E7** — `OPEN_ITEMS.md` is in neither commit.
- **E8** — no path of the standing untracked population is in either commit.

---

## 6. WHAT THIS BATCH DOES **NOT** DO

No `src/` change, no golden, **no test changed, moved or run**, no behaviour change to the analysis,
no fix to inference. **No measurement of the analysis built, designed, scoped or run.** No derivation
and no comparison. **No blind derivation output opened at all**, and no oracle document opened beyond
`CLAUDE.md`, which this batch is authorised to edit at three fenced sites. **No edit to
`ARCHITECTURE.md`, to the boot-pack generator, to either pack directory, or to the manifest.** No
open-items row created, flipped or discarded. **No admission to the ledger, and the ledger is not
built.** No candidate file touched. **No dispatch written.** **No finding number allocated.**

---

## 7. YOUR REPORT

`cc_report_amendment_landing.md`, carrying in this order: the start-state measurement with the command
beside each figure and the side stated; **rule (n) quoted verbatim** and what it determined; the three
changed passages of `CLAUDE.md` in full; the register regeneration and both establishment checks; the
four new entries with their allocated identifiers and their homes; the forward-bound re-aiming and the
backfilled row; the sweep rounds with everything that moved; E0–E8 with the measurement beside each;
every assumption of §3 you falsified; and **declared departures** — what you did not read, and what
you relayed rather than measured.
