# CC INSTRUCTION — the cascade-sweep batch

> **Written by Cowork, 2026-08-25, the forty-fifth session's fifteenth sitting.** You are a fresh
> Claude Code session. **Read this file whole before you touch anything.**
>
> **★ THIS BATCH OPENS ONE REGISTER ROW AND THEN SWEEPS THE DERIVED ARTIFACTS TO A FIXPOINT.** It
> changes no behaviour, touches no `src/`, **edits no tool source**, runs no analysis, and reads no
> blind derivation output.
>
> **★ DO NOT RUN `git status`.** This repository's guard refuses it (**D-253**). The sanctioned
> enumeration is **`python tools/audit/changed_paths.py`** (`--staged`, or `--commit <hash>`).

---

## 0. THE ONE BAR THAT MAKES THIS BATCH SAFE — READ IT BEFORE ANYTHING ELSE

**You will regenerate derived artifacts in a loop. There is exactly one kind of red you may
regenerate, and one kind you may never touch.**

- **STALENESS RED — REGENERATE.** The failure says the artifact **no longer re-derives** — *"STALE vs
  the derivation"*, *"differs from what the generator now produces"*, *"does not re-derive"*. The
  artifact is **out of date, not wrong**. Regenerating it is the ordinary discharge.
- **★ DECISION RED — NEVER REGENERATE, EVER.** The failure **STOPs demanding an authored decision** —
  e.g. *"STOP: derived candidates with no authored verdict … an unclassified candidate is a STOP,
  never a silent pass (D-661)"*. **Regenerating such a tool would convert an unanswered question into
  a silent pass. That is the single worst thing this batch could do.**

**The standing red `tools/audit/gen_filing_convention_application.py --check` ([[OI-372]]) is a
DECISION red. Do not regenerate it, do not run it in write mode, do not investigate it, do not
authored-verdict anything for it.**

**★ IF A DECISION RED APPEARS THAT IS NOT THE STANDING ONE: STOP IMMEDIATELY AND REPORT.** Do not
regenerate it, and do not continue the sweep.

**If you cannot tell which kind a red is, treat it as a DECISION red and STOP.**

---

## 1. RULING LEDGER — quoted

**From `cowork_rulings_2026_08_25_cascade_sitting.md` (landing in this batch, §2):**

> *"1. The `216` finding is ROWED at the next free identity, measured … no finding number, no
> apparatus declaration, no gating verdict, no remedy. 2. THEN the sweep runs. Run the guard set;
> regenerate every tool whose failure is a STALENESS … and ONLY those; run the guard set again;
> repeat until the failing set is the standing red alone, or a round makes no progress. 3. Commit …
> in ONE commit. Then the final guard run lands in a second."*

> *"★ THE ORDER IS THE POINT AND IS PART OF THE RULING: THE ROW IS CREATED BEFORE THE SWEEP, so the
> new row's own cascade is absorbed by the same sweep instead of starting a fourth batch."*

**From §3 — what is NOT done to the finding being rowed:**

> *"It is rowed and nothing else is done to it. No remedy is ordered, and the transcription is NOT
> updated to `217`. … updating the number would re-commit the very defect — a hand-count that goes
> stale on the next row."*

---

## 2. PREMISE LEDGER — measured at objects this turn

**P1. The tip is `9b1b0a02943fd047ab0c92ef817e8b81e52cf5a3`**, parent
`744ed4a708d3a3cf1c6764ccf2bf6ab33fa5aa2b`. **Re-measure it first. If it differs, STOP.**

**P2. The guard set at the tip reports two failures** (`HEAD:tools/audit/guard_state.json`):
`{run 75, passing 73, failing 2, not_run 4, historical_records 16}` —

| tool | kind | this batch |
|---|---|---|
| `gen_filing_convention_application.py --check` | **DECISION red** ([[OI-372]]) | **NEVER TOUCH** |
| `gen_session_start_read_size.py --check` | **STALENESS red** (*"STALE vs the measurement: session_start_read_size.json does not re-derive"*) | the sweep discharges it |

**P3. The defect to be rowed, measured at `tools/audit/gen_session_start_read_size.py` at the tip.**
It carries a **hand-transcribed count of a figure its own run derives** — the string `216` — at
**THREE sites**, and the derived value at this tree is **217**:

| line | where | published into the artifact? |
|---|---|---|
| 34 | the module docstring | no |
| 140 | `FURTHER_SPANS`, the label for the `the_gating_rows` span | **yes** |
| 298 | the `★_the_further_spans_and_why_they_are_here` block | **yes** |

**Measure all three yourself and report the line numbers you find** — this is a lead, and the file
may have moved.

**P4. The derived value is 217.** Measured at `HEAD:tools/audit/nongating_apparatus_rows.json` →
`★_the_live_gating_answer` → `gating_ids`, length **217**, and it contains `OI-376`.

**P5. A LEAD, NOT THE CLOSURE — who reads the artifact the sweep will move.** Measured at the tip:
only **two** generators read the answer key `★_the_live_gating_answer` — the producer
`gen_nongating_apparatus_rows.py` and `gen_session_start_read_size.py`. **But these further
generators read `nongating_apparatus_rows` by name**, and whether any consumes a key that moves is
**exactly what the sweep is for and what reasoning cannot settle**:

`gen_discard_records.py`, `gen_guard_classification.py`, `gen_guard_state.py`,
`gen_phase1_completion_inventory.py`, `gen_phase1_finish_line.py`,
`gen_recognizer_establishment_sort.py`, `index_status_lint.py`, `claude_md_rule_triage.py`,
`decisions/gen_true_half_reach.py`, `decisions/gen_true_half_reach_rows.py`.

**★ DO NOT PRE-EMPTIVELY REGENERATE ANY OF THESE. The sweep regenerates only what actually goes red.**

**P6. Two files sit on disk uncommitted and are FINISHED WRITING-SIDE ARTIFACTS** —
`cowork_rulings_2026_08_25_cascade_sitting.md` (untracked) and `cowork_handoff.md` (modified).
**Their sizes and hashes are NOT given here; you measure them in your start state.** **You do not
edit, reflow or correct either. If you believe one is wrong, REPORT IT.**

**P6a. This instruction file and your report** are also expected untracked paths and ride the
**second** commit.

**P7. A large pre-existing untracked population stands in the tree** (~833 paths at the last
reading). **A standing condition, already routed as a finding. Do not commit any of it and do not
re-litigate it.**

**P8. `.gitattributes` marks these paths `text: auto`** (`git check-attr text eol -- <path>`), and
`core.autocrlf` is **not set**. **Consequence you must respect in every hash comparison:** for a file
whose worktree copy has CRLF endings, a worktree sha256 and a `git cat-file blob` sha256 **will not
agree** — `tools/audit/nongating_apparatus_rows.json` is such a file (blob **173,748** bytes,
worktree **176,351**). **When you compare, say which side you measured, and never report a CRLF/LF
difference as a content difference.**

---

## 3. ASSUMPTIONS — declared so you can falsify them

- **A1. NO COUNT OF THE HANDOFF'S ENTRIES IS ASSERTED OR IMPLIED.** Measure the difference against
  the tip and report it, **with the matching pattern you used stated**, since two patterns give two
  populations. **Whatever number you get is NOT a STOP.**
- **A2. The tip has not moved since P1.** **If it moved, STOP.**
- **A3. The sweep converges.** Falsify it: **cap the sweep at FIVE rounds.** If round five does not
  reach *the standing red alone*, **STOP and report every round's failing set** — a non-converging
  sweep is a finding about the apparatus, not a reason to keep going.
- **A4. Every red the sweep meets, other than the standing one, is a STALENESS red.** **Falsify it by
  §0's test at every round.** A DECISION red that is not the standing one is an immediate STOP.
- **A5. The new row is placed on the gating side by the ruled default**, being outside the apparatus
  first cut — the same placement `OI-376` received. **This is the writing side's EXPECTATION, given
  so you can falsify it. The regenerated artifact is the measurement. If it says otherwise, the
  artifact is right — report it and reconcile nothing by editing.**

---

## 4. DECLARED START STATE — measure and report; assert nothing

The tip; `python tools/audit/changed_paths.py`; the size and sha256 of
`cowork_rulings_2026_08_25_cascade_sitting.md`, `cowork_handoff.md` and this instruction file at the
working tree; the current failing set from `HEAD:tools/audit/guard_state.json`; the three `216` sites
with their line numbers; the current length of `gating_ids`; and the highest identity in
`OPEN_ITEMS.md` and in `open_items/` **measured separately**.

---

## 5. FINDINGS ROUTING

**Analysis findings** → the quarantined audit questions; do not act. **Apparatus findings** → report
them; **open NO further register row** — this batch opens exactly one. **Everything else** → report
with finding, date and reason, and discard. **★ You may not fix what you find.**

---

## 6. TASKS

### Task 1 — measure the start state (§4)

**Do not proceed if the tip differs from P1.**

### Task 2 — ROW the `216` finding, BEFORE the sweep

**Measure the next free identity** across **both** the INDEX and `open_items/`; if the two disagree,
**report it and take the next above the higher of the two.** Call it **OI-N** and report the number
and its derivation.

**(a) `open_items/OI-N.md`** — narrative and provenance only, **never a status of its own**. It
carries:

1. **The defect.** `tools/audit/gen_session_start_read_size.py` restates by hand a figure the same
   run derives: the count of gating rows, written `216` at the sites P3 names, against a derived
   **217** at this tree. **Quote the string as it stands at each published site.**
2. **Why it is a defect and not a nit.** Two of the three sites are **published into the tool's own
   artifact**, so a reader of that artifact is told a number the same artifact contradicts. This is
   the shape **#17f** and **D-431** forbid — *a figure enters by citation to a generated artifact,
   never by transcription.*
3. **Why no remedy is ordered**, in the ruling's own words: the standing mechanism freeze bars tool
   work that does not block the work, and **updating `216` to `217` would re-commit the very defect**
   — a hand-count that goes stale at the next row. **The right repair is to remove the transcription
   and let the figure enter by citation, which is a DESIGN question with real alternatives and gets
   its own surface.** **The row records the defect; it does not pre-decide its cure.**
4. **Provenance:** found 2026-08-25 by the regeneration-and-citation batch (one site) and measured to
   three sites by Cowork at the objects; rowed on Ruling 3 of
   `cowork_rulings_2026_08_25_cascade_sitting.md` under Ruling 9 of
   `cowork_rulings_2026_08_21_successor_plan_sitting.md` and register rules (c) and (e).
5. **★ NO REMEDY, NO TASK LIST, NO PATCH.** **Do not edit
   `tools/audit/gen_session_start_read_size.py`. Do not change `216` to `217` anywhere.**

**(b) The INDEX row in `OPEN_ITEMS.md`.** **Copy the neighbouring rows' column structure exactly** —
six cells on `" | "`, status cell opening with the bare canonical `OPEN` token, the row a **pointer,
not a restatement**, with a `[detail](open_items/OI-N.md)` link.

**★ NO APPARATUS CLAIM, NO NON-GATING DECLARATION, NO GATING VERDICT** — the row takes the ruled
default, exactly as `OI-376` did. **Do not "helpfully" declare it apparatus.** If you cite a decision
for that treatment, **cite D-438** and check it at `DECISIONS.md` before you write it. *(The last
batch corrected a transposition here; do not reintroduce one.)*

**Then run `python tools/audit/index_status_lint.py`.** It must PASS. **If it fails, STOP.**

### Task 3 — THE SWEEP, to a fixpoint, at most FIVE rounds

**Each round:**

1. **Run the guard set** — `python tools/audit/gen_guard_state.py`. Record the failing set.
2. **Classify every failure by §0's test.** **Any DECISION red that is not the standing one → STOP
   AND REPORT, immediately, mid-round.**
3. **If the failing set is the standing red alone → the sweep has converged. Stop cleanly and go to
   Task 4.**
4. **Otherwise regenerate every STALENESS red's tool**, in write mode, **and nothing else.** Record,
   per tool, its output and the artifact's before/after size and sha256 **on the same side** (worktree
   vs worktree — see P8).
5. **If a round regenerates nothing new and the failing set is unchanged from the previous round →
   NO PROGRESS. Stop and report.**

**Report EVERY round**: its number, its failing set, what it classified each as, what it regenerated,
and what moved. **A round-by-round table is the deliverable here** — it is the measurement of the
blast radius that this batch exists to obtain, and it is worth more than the tidy end state.

**★ AND REPORT, FROM THE REGENERATED ARTIFACT AND NOT FROM REASONING: where OI-N landed** — in
`gating_ids`, in the non-gating verdicts, or neither — **quoted from the file**, together with
whether **any OTHER row's placement changed.** **If another row moved, report it and STOP.**

### Task 4 — ONE commit

`git add` and commit together: `cowork_rulings_2026_08_25_cascade_sitting.md`, `cowork_handoff.md`,
`OPEN_ITEMS.md`, `open_items/OI-N.md`, **and every artifact the sweep regenerated** — and nothing
else. **Message:** state that it lands the cascade record and the handoff's sixty-second entry, opens
OI-N on the hand-transcribed count, and discharges the cascade by sweep, naming how many rounds it
took. **Do not assert the end state in this message.**

### Task 5 — the final guard run, in a SEPARATE, LATER commit

Run the guard set once more at the tree Task 4's commit left. Report the summary in its ruled shape.
**Expect `failing: 1`, the standing red.** **If not, REPORT IT AND STOP — do not fix it.**

**Land, as the second commit:** whatever that run writes, **plus this instruction file and your
report**. **★ THE E-ORDERING RULE: a commit cannot assert its own end state.**

---

## 7. REGISTERED EXPECTATIONS — MET or NOT MET, with the measurement beside each

- **E0 — the two writing-side files land byte-identical**, measured at the committed objects, equal
  to your Task-1 measurement. **State which side you measured (P8).**
- **E1 — Task 4's commit contains exactly the paths named**: the record, the handoff, `OPEN_ITEMS.md`,
  `open_items/OI-N.md`, and the swept artifacts — **and nothing else. List them.**
- **E2 — `OPEN_ITEMS.md` differs from `9b1b0a02:OPEN_ITEMS.md` by exactly ONE added row.** Measure
  row-by-row: no row removed, **no existing row's text changed**, non-row lines equal.
- **E3 — the sweep converged within five rounds**, and its final failing set is the standing red
  alone. **If NOT MET, the round table is the report and the batch stops.**
- **E4 — no tool source file was modified.** Measure: no path under `tools/` ending `.py` appears in
  either commit.
- **E5 — the batch lands exactly TWO commits, in order.** **If the ordered structure yields a
  different number, reconcile it in your close — do not invent a commit, and do not silently absorb
  one.**

---

## 8. WHAT THIS BATCH DOES **NOT** DO

No `src/` change; no build; no test written, run, moved or changed; no golden refreshed; nothing
under `tools/corpus/` or `tools/robust_stop/`; no behaviour change and no design.

**And specifically:** it **edits no tool source** — the `216` above all, which is **not** changed to
`217` anywhere; it does **not** touch [[OI-372]] or its tool, and **never regenerates a DECISION
red**; it does **not** re-open, re-word or add a verdict to `OI-376`; it does **not** create more
than one register row; it does **not** touch either derivation boot pack, the pack generator, the
manifest, either withheld family, either session brief, or either blind derivation output; it does
**not** read either blind output at all; it does **not** touch `CLAUDE.md`, `STATUS.md`,
`DECISIONS.md` (which may be READ), `ARCHITECTURE.md` or any other governing document; it does
**not** allocate a finding number (**Ruling 9 opens no findings series**); it does **not** propose a
remedy for anything it rows; and it does **not** open, boot or prepare any derivation session.

**[[OI-179]] stays OPEN and GATES. [[OI-374]] stands as found. The three deferred apparatus items
stay deferred.**

---

## 9. THE WRITING SIDE'S SELF-CHECK

- **P2, P3, P4, P5 and P8 were measured at objects this turn** — the guard artifact, the tool's three
  `216` sites, the `gating_ids` length and membership, the consumer list by `git grep` at the tip,
  and the attribute state at `git check-attr` with `core.autocrlf` confirmed unset.
- **P5 is published as a LEAD and is explicitly NOT the closure**, because the last three batches
  each proved that reasoning about this graph loses to running it.
- **A5 publishes the writing side's expectation SO THAT YOU CAN FALSIFY IT.** The artifact is the
  authority.
- **P6 carries no hashes deliberately** — a figure that goes stale between writing and delivery is
  worth less than one you measure.
- **§0's DECISION/STALENESS distinction is the load-bearing safety rule of this batch**, and it is
  stated before the tasks rather than inside them for that reason.
- **The last dispatch's `git status` defect is not repeated**, and the `D-436`/`D-438` transposition
  is flagged at Task 2(b) so it is not reintroduced.

---

## 10. YOUR REPORT

Write `cc_report_cascade_sweep.md` at the repository root. **It rides Task 5's commit.** Carry: the
declared start state; the identity N and its derivation; the row's text; the lint output; **the
round-by-round sweep table — the deliverable of this batch**; where OI-N landed, quoted from the
artifact; whether any other row moved; both commit hashes and their path lists; E0–E5 each MET or NOT
MET with the measurement beside it; the final guard summary in its ruled shape; the measured handoff
difference with its pattern (A1); and every finding routed under §5, including any you declined to
act on.

**If anything STOPs you, stop there and report what you had done. A partial batch honestly reported
is worth more than a complete one that guessed** — and in this batch a STOP on a DECISION red is a
success, not a failure.
