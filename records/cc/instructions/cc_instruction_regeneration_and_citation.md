# CC INSTRUCTION — the regeneration-and-citation batch

> **Written by Cowork, 2026-08-25, the forty-fifth session's fourteenth sitting.** You are a fresh
> Claude Code session. **Read this file whole before you touch anything.**
>
> **★ THIS IS A HYGIENE BATCH.** It discharges **two owed regenerations**, corrects **one wrong
> cross-reference** in a register row that landed this morning, and lands one ruling record and one
> handoff entry. **It changes no behaviour, touches no `src/`, runs no analysis, reads no blind
> derivation output, and creates no register row.**
>
> **★ DO NOT RUN `git status`.** This repository's guard refuses it (D-253). The sanctioned
> enumeration is **`python tools/audit/changed_paths.py`** (`--staged`, or `--commit <hash>`). *The
> previous dispatch asked for `git status` in error; that is corrected here.*

---

## 1. RULING LEDGER — quoted

**From `cowork_rulings_2026_08_25_landing_return_sitting.md` (landing in this batch, §2):**

> *"One small correction dispatch runs now: **(a)** `gen_nongating_apparatus_rows.py` is
> regenerated … the artifact is **out of date, not wrong**, and regenerating it is the ordinary
> discharge. **(b)** `gen_evidence_pin_membership.py` is regenerated … **(c)** The `OI-376` citation
> is corrected in place, D-436 → D-438, with an inline note recording that it was corrected and
> when. Nothing else in the row changes."*

**And the clause that governs what you do with the derived gating answer — read it before Task 3:**

> *"the regeneration's derived answer is ACCEPTED as it falls, whatever it is, and the landing batch
> **reports** it … **If the derived answer differs from that expectation, that is a finding and is
> reported, NOT corrected by re-wording the row's subject cell** — re-wording a row to move a derived
> verdict would be gaming the cut, and is forbidden here in terms."*

---

## 2. PREMISE LEDGER — FACTs, each measured at an object this turn

**P1. The tip is `64d640317fd652d1192350f0eafe4ef83abca680`**, the method-voiding batch's second
commit, whose parent is `2dfe0ba485f438817f60385b4f6ea9fc0e6e4432`. **Re-measure it as your first
act. If it differs, STOP.**

**P2. The guard set at the tip reports three failures**, measured at
`HEAD:tools/audit/guard_state.json`: `{run 75, passing 72, failing 3, not_run 4,
historical_records 16}`, failing —

| tool | this batch's business |
|---|---|
| `tools/audit/gen_nongating_apparatus_rows.py --check` | **Task 3(a) discharges it** — the artifact is stale because `OI-376` joined the open population; it is out of date, **not wrong** |
| `tools/audit/gen_evidence_pin_membership.py --check` | **Task 3(b) discharges it** — the three 2026-08-25 ruling records are now committed, so the derivation and the artifact can agree |
| `tools/audit/gen_filing_convention_application.py --check` | **THE STANDING RED ([[OI-372]]). NOT YOURS. Do not touch it, do not regenerate for it, do not investigate it.** |

**P3. `DECISIONS.md` at the tip carries both decisions, and only one of them says what `OI-376`'s
row claims.** Measured verbatim:

> `| D-436 | A mechanism is judged on three measured conditions — automatic, detection rate, false-positive rate — and a failing one is REPORTED, not automatically removed | LIVE |`

> `| D-438 | Open-items register rows whose subject is this project's own tracking and documentation apparatus gate nothing — but an establishment obligation always gates | LIVE |`

**D-438 is the decision the row means. D-436 is a transposition.** [[OI-319]] and [[OI-336]] in the
same parenthesis are **correct and are NOT touched.**

**P4. Both generators write when invoked with no `--check`.** Read at their own source: each `main`
takes the `--check` branch only when `--check` is in `argv`, and otherwise writes its output file.

**P5. Two files sit on disk uncommitted and are FINISHED WRITING-SIDE ARTIFACTS.**

| path | state | size (bytes) | sha256 |
|---|---|---|---|
| `cowork_rulings_2026_08_25_landing_return_sitting.md` | UNTRACKED | *(measure)* | *(measure)* |
| `cowork_handoff.md` | MODIFIED | *(measure)* | *(measure)* |

**Their measured values are given in your start state, not here** — the writing side delivers them in
the same turn as this instruction, and a figure that would go stale between the two is worth less
than one you measure. **You do not edit, reflow or correct either file. If you believe one is wrong,
REPORT IT.**

**P5a. This instruction file and your report are also expected untracked paths.** They ride the
**second** commit, never the first.

**P6. The tree carries a large pre-existing untracked population** — the previous batch measured 831
paths unrelated to it. **That is a standing condition, not a defect. Do not commit any of them, and
do not re-litigate it; the previous report already routed it as a finding.**

---

## 3. ASSUMPTIONS — declared so you can falsify them

- **A1. NO COUNT OF THE HANDOFF'S ENTRIES IS ASSERTED HERE, AND NONE IS IMPLIED.** The writing side
  prepended one entry this cycle, **but the previous batch measured four where one was asserted, and
  the writing side has now got that assertion wrong three times.** **MEASURE the actual difference
  against the tip and report it. Whatever number you get is NOT a STOP.**
- **A2. The tip has not moved since P1.** Falsify by re-measuring. **If it moved, STOP.**
- **A3. Correcting the citation in cell 5 does not change either generator's derivation.** The
  correction touches the status cell's prose, not the subject cell the first cut matches on.
  **Falsify it: Task 2 orders the correction BEFORE the regenerations precisely so that if it does
  change something, the change is inside what you regenerate and is visible. Report whether the
  derived placement of `OI-376` differs from what a regeneration before the correction would have
  produced — and if you cannot tell, say you cannot tell rather than guessing.**
- **A4. The two regenerations discharge exactly two of the three reds, leaving the standing red
  alone.** Falsify at Task 5. **If a fourth red appears, or if either regeneration's `--check` still
  fails after the write, STOP AND REPORT.**
- **A5. Only the two named artifacts change on disk from the regenerations.** If a generator writes
  any other path, **report it and do not commit it without saying so explicitly.**

---

## 4. DECLARED START STATE — measure and report; assert nothing

The tip; the sanctioned changed-path enumeration (`python tools/audit/changed_paths.py`); the size
and sha256 of `cowork_rulings_2026_08_25_landing_return_sitting.md`, `cowork_handoff.md` and this
instruction file, at the working tree; the current sha256 of
`tools/audit/nongating_apparatus_rows.json` and `tools/audit/evidence_pin_membership.json`; and the
`OI-376` row's current cell-5 text where the citation stands.

---

## 5. FINDINGS ROUTING

**Analysis findings** → the quarantined audit questions; do not act. **Apparatus findings** → report
them; **open NO register row** — this batch creates none. **Everything else** → report with finding,
date and reason, and discard. **★ You may not fix what you find.**

---

## 6. TASKS

### Task 1 — measure the start state (§4)

**Do not proceed if the tip differs from P1.**

### Task 2 — correct the `OI-376` citation, and ONLY that

In `OPEN_ITEMS.md`, in the `OI-376` row's **status cell**, the parenthesis currently reads
`([[OI-319]], [[OI-336]], **D-436**)`.

**Change `D-436` to `D-438`, and append an inline correction note inside the same parenthesis or
immediately after it**, to the effect: *citation corrected 2026-08-25 — D-438 is the decision that
states the register's gating cut; D-436 (mechanism judging) was a transposition in the row as first
landed.* **Word it in the row's own register, briefly. Nothing else in the row changes** — not its
identity, not its name cell, not its description cell, not its subject/owning-area cell, **and above
all not its status token, which stays the bare canonical `OPEN`.**

**★ THE BAR: [[OI-319]] and [[OI-336]] are correct and stay. Do not add further citations, do not
re-word the finding, and do not add a gating verdict or an apparatus declaration.**

**Then run `python tools/audit/index_status_lint.py` and report its output.** It must PASS — the row
must still split into six cells and still open with a canonical token. **If it fails, STOP.**

### Task 3 — the two regenerations, in this order

**(a) `python tools/audit/gen_nongating_apparatus_rows.py`** (write mode, no `--check`).

**Then report, from the written artifact and not from reasoning:**
- **what the artifact now says about `OI-376`** — whether it appears in `gating_ids`, in the
  non-gating verdicts, in `open_rows`, or in none of them, **quoted from the file**;
- whether the artifact's counts moved, and by how much;
- **whether any OTHER row's placement changed.** If one did, **report it and STOP** — a hygiene
  regeneration must not silently move another row's verdict.

**★ THE WRITING SIDE'S EXPECTATION, GIVEN SO YOU CAN FALSIFY IT RATHER THAN CONFIRM IT:** a row
outside the tool's first cut takes the outside-the-cut ground and is placed on the **gating** side by
the ruled default. **That is a READING of the source made by the writing side, not a measurement.
The artifact is the measurement. If it says otherwise, the artifact is right and the reading is
wrong — report it and do not reconcile it by editing anything.**

**(b) `python tools/audit/gen_evidence_pin_membership.py`** (write mode, no `--check`).

**Then report:** how the artifact's record population moved — specifically whether the three
2026-08-25 ruling records now appear, and whether any previously-present record disappeared. **A
disappearance is a STOP.**

**(c) Re-run both with `--check` and report both exit codes.** Both must now pass.

### Task 4 — ONE commit

`git add` and commit together, in one commit: `cowork_rulings_2026_08_25_landing_return_sitting.md`,
`cowork_handoff.md`, `OPEN_ITEMS.md`, `tools/audit/nongating_apparatus_rows.json`,
`tools/audit/evidence_pin_membership.json` — **and nothing else.** **Message:** state that it lands
the landing-return record and the handoff's sixty-first entry, corrects `OI-376`'s D-436→D-438
citation, and discharges the two owed regenerations.

**If a generator wrote any further path (A5), name it in your report and say whether you committed
it and why.**

### Task 5 — the guard set, in a SEPARATE, LATER commit

Run it. Report the summary in its ruled shape: `{run, passing, failing, failing_tools, not_run,
historical_records}`. **Expect `failing: 1` and that one to be the standing red. If any other tool
fails, REPORT IT AND STOP — do not fix it.**

**Land, as the second commit:** whatever the run legitimately produces, **plus this instruction file
and your report**. **★ THE E-ORDERING RULE: a commit cannot assert its own end state. Task 4's commit
does not claim the guard set is clean; this run is what says so, and it lands after.**

---

## 7. REGISTERED EXPECTATIONS — MET or NOT MET, with the measurement beside each

- **E0 — the two writing-side files land byte-identical**, measured at the committed objects
  (`git cat-file blob <commit>:<path> | sha256sum`), equal to what you measured at Task 1.
- **E1 — Task 4's commit contains exactly five paths**, the five named. **Report the list.**
- **E2 — the `OI-376` row differs from its landed form in exactly the citation and its correction
  note.** Measure by diffing the row's text against `2dfe0ba485:OPEN_ITEMS.md`, and **quote the
  before and after of the row.** No other row in the file changed.
- **E3 — the guard set reports `failing: 1`, the standing red.** If not, NOT MET, reported, stopped.
- **E4 — the batch lands exactly TWO commits, in order.** **If the ordered structure yields a
  different number, reconcile it in your close and say what the actual number was — do not invent a
  commit to match this line, and do not silently absorb one.**

---

## 8. WHAT THIS BATCH DOES **NOT** DO

No `src/` change; no build; no test written, run, moved or changed; no golden refreshed; nothing
under `tools/corpus/` or `tools/robust_stop/`; no behaviour change and no design.

**And specifically:** it does **not** create, close, flip, re-scope or re-word any register row —
`OI-376`'s citation is corrected and nothing else about it moves; it does **not** add a gating
verdict or an apparatus declaration to any row; it does **not** touch the standing red
[[OI-372]] or its tool; it does **not** touch either derivation boot pack, the pack generator, the
manifest, either withheld family, either session brief, or either blind derivation output; it does
**not** read either blind output at all; it does **not** touch `CLAUDE.md`, `STATUS.md`,
`DECISIONS.md`, `ARCHITECTURE.md` or any other governing document; it does **not** regenerate any
generated artifact other than the two named plus whatever Task 5's guard run writes of its own
accord; it does **not** allocate a finding number (**Ruling 9 opens no findings series**); it does
**not** propose a remedy for `OI-376`'s hazard; and it does **not** open, boot or prepare any
derivation session.

**[[OI-179]] stays OPEN and GATES. [[OI-374]] stands as found. The three deferred apparatus items
stay deferred.**

---

## 9. THE WRITING SIDE'S SELF-CHECK

- **P2, P3 and P4 were measured at objects this turn** — the guard artifact at the tip, both
  `DECISIONS.md` rows verbatim, and both generators' `main` read at their own source.
- **P5 deliberately carries no hashes**, because the writing side published a self-referential hash
  in the last dispatch and watched it go stale on the next edit. **You measure them.**
- **§3's A1 orders a measurement and states the writing side's own error count**, because that
  assertion has now been wrong three times.
- **The `git status` prohibition at the head is a correction of the previous dispatch's own defect**,
  found by CC and routed by the writing side. **No repository act is owed for it.**
- **Task 3(a) publishes the writing side's expectation SO THAT YOU CAN FALSIFY IT.** The artifact is
  the authority; the reading is not.
- **Nothing here asks you to judge, compare, read or evaluate a blind derivation output**, and
  nothing asks you to invent a mechanism for anything.

---

## 10. YOUR REPORT

Write `cc_report_regeneration_and_citation.md` at the repository root. **It rides Task 5's commit.**
Carry: the declared start state; the before/after of the `OI-376` row; the lint output; **what the
regenerated non-gating artifact says about `OI-376`, quoted**; how the evidence-pin population moved;
both `--check` exit codes; both commit hashes and their changed-path lists; E0–E4 each MET or NOT MET
with the measurement beside it; the guard summary in its ruled shape; the measured handoff difference
(A1); and every finding routed under §5, including any you declined to act on.

**If anything STOPs you, stop there and report what you had done. A partial batch honestly reported
is worth more than a complete one that guessed.**
