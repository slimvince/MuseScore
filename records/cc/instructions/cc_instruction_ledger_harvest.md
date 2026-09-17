# CC INSTRUCTION — the ledger-harvest batch

> **Written by Cowork, 2026-08-25, the forty-sixth session's first sitting.** You are a fresh Claude
> Code session. **Read this file whole before you touch anything.**
>
> **★ THIS BATCH HARVESTS CANDIDATES FOR THE EMPIRICAL FINDINGS LEDGER. IT DOES NOT BUILD THE
> LEDGER.** It changes no behaviour, touches no `src/`, **edits no tool source**, runs no analysis,
> opens no register row, and reads no blind derivation output.
>
> **★ DO NOT RUN `git status`.** This repository's guard refuses it (**D-253**). The sanctioned
> enumeration is **`python tools/audit/changed_paths.py`** (`--staged`, or `--commit <hash>`).

---

## 0. THE ONE BAR THAT MAKES THIS BATCH SAFE — READ IT BEFORE ANYTHING ELSE

**You will apply an admission test to a population of candidate facts. You will not admit any of
them.**

- **CANDIDATE — this batch's product.** A fact you have found, with its provenance measured, and
  your reading of whether it passes the admission test, **with your reasoning stated so the user can
  overturn it.** This is a proposal to the user.
- **★ ADMISSION — NEVER YOURS TO MAKE.** An admitted fact enters the ledger and is thereafter read
  by deriving sessions as established. **Nothing this batch writes is an admission**, no artifact
  this batch writes is the ledger, and **no file this batch writes may be shaped so that a later
  reader could mistake it for the ledger.** Ruling 8 of 2026-08-21 requires that every hand
  admission be re-checked at the ledger's gate; a batch that quietly admitted its own candidates
  would defeat that re-check before the gate exists.

**Ruling 9 of 2026-08-21 governs everything you find that is not a candidate: an analysis finding
goes to the quarantined audit questions, an apparatus finding is reported, everything else is
discarded with finding, date and reason. ★ You may not fix what you find, and this batch opens no
register row.**

**The standing red `tools/audit/gen_filing_convention_application.py --check` ([[OI-372]]) is a
DECISION red. Do not regenerate it, do not run it in write mode, do not investigate it, do not
authored-verdict anything for it.** If any other DECISION red appears — a failure that STOPs
demanding an authored verdict rather than reporting an artifact that no longer re-derives — **STOP
and report.** If you cannot tell which kind a red is, treat it as a DECISION red and STOP.

---

## 1. RULING LEDGER — quoted

**From `cowork_rulings_2026_08_21_successor_plan_sitting.md`, Ruling 8:**

> *"The ledger (a ruled preparation output) is not built before the pilot. The admission test — does
> the fact survive the implementation being thrown away? — is applied by hand; each admitted fact is
> recorded in the ledger's ruled entry shape; those entries seed the ledger when it is built, and
> every hand admission is re-checked at the ledger's gate then. The hole is declared in the pilot's
> source declaration, not hidden."*

**From `cowork_specification_reconstruction_plan_successor_2026_08_21.md` §2:**

> *"**The fact-gate and the empirical findings ledger** — the ruled admission mechanism for our OWN
> experimental findings. The test: does the fact survive the implementation being thrown away? A
> fact that passes enters the ledger, approach-level and implementation-stripped, with its
> provenance, uncertainty and establishment status. The ledger is a ruled preparation output and has
> not been built."*

**From the same plan, §6.4:**

> *"A recorded dead end may withdraw a derived statement **only if** it passes the fact-gate's ruled
> test — does the fact survive the implementation being thrown away? — and is approach-level. A
> prohibition on re-attempting a specific mechanism of the dormant scorer does not; a fact about the
> music or the corpus ('an absent root does not mean a wrong reading, corpus-wide';
> `docs/scoring_model.md:1396`) does."*

**From the same plan, §5, on what may be mined:**

> *"`OPEN_ITEMS.md`, the handover records, dispatches and coding-side reports are process record and
> enter only as mining inputs behind the fact-gate."*

**From `cowork_curated_boot_list_draft_2026_08_19.md` §4:**

> *"**The EMPIRICAL FINDINGS LEDGER (preparation output (c)) is NOT BUILT** — no artifact of that
> kind exists anywhere in the tree at `891bacc5d2`. Its ruled place is a member of this list: it is
> the fact-gated home of the empirical findings that survive the implementation being thrown away,
> and a deriving session is meant to read admitted facts from it and from nowhere else."*

---

## 2. PREMISE LEDGER — measured this turn, or declared as a LEAD

**P1. The tip is `0f18b358bc6a8da5ec6064760d675129e64d8f3b`**, parent
`428b44143db6e3eeb6f052ad2216cfd63bd01e9a`. Measured by the writing side at `.git/HEAD` and
`.git/refs/heads/master` with file tools, not by a shell command. **Re-measure it first. If it
differs, STOP.**

**P2. `refs/remotes/origin/master` reads `f225b61343ff3de022d32d6b7514d835b87093cf`** — **not** the
local tip. The writing side measured this and **draws no conclusion from it**; it did not establish
whether the two are related by ancestry. **Report what it is at your tree and whether it is an
ancestor of the tip. Whatever you find is NOT a STOP** — the writing side never pushes, and this
premise exists so the divergence is measured rather than assumed away.

**P3. The guard set at the tip reports one failure** — `{run 75, passing 74, failing 1, not_run 4,
historical_records 16}`, the standing red ([[OI-372]]) alone. **Measure it at
`HEAD:tools/audit/guard_state.json` and report what you find.**

**P4. ★ THE BATCH'S MOST IMPORTANT PREMISE, AND IT IS A LEAD, NOT A CLOSURE — THE LEDGER'S RULED
ENTRY SHAPE.** Ruling 8, plan §6.4 and plan §2 each refer to *"the ledger's ruled entry shape"* as
something already ruled. **The writing side searched the plan, the 2026-08-21 ruling record and the
boot-list draft and did NOT find where that shape is ruled, or what its fields are, beyond §2's four
properties** — the fact stated approach-level and implementation-stripped, its **provenance**, its
**uncertainty**, and its **establishment status**.

**Find it or establish that it does not exist.** Search the ruling records, the ratification
surfaces, `ARCHITECTURE.md`, `DECISIONS.md` and the phase-definition surface. **Quote it whole where
you find it, with its file and line numbers.** **If it does not exist, say so in terms — that is a
first-class finding of this batch and worth more than the harvest itself**, because three ruled
documents rest on a shape that may never have been written down.

**P5. The ledger does not exist.** True at `891bacc5d2` per §4 of the boot-list draft. **Re-measure
it at this tip** — search the tree for any artifact of that kind under any name. **A lead, not the
closure.**

**P6. Four files sit on disk uncommitted and are FINISHED WRITING-SIDE ARTIFACTS**:

| path | state |
|---|---|
| `cowork_handoff.md` | modified against the tip (its sixty-third entry) |
| `cowork_rulings_2026_08_25_next_act_sitting.md` | untracked |
| `cowork_blind_session_opening_instruction_harmony_boundary.md` | untracked |
| this instruction file | untracked |

**Their sizes and hashes are NOT given here; you measure them in your start state.** **You do not
edit, reflow or correct any of them. If you believe one is wrong, REPORT IT.** Your report is a
fifth expected untracked path and rides the second commit.

**P7. A large pre-existing untracked population stands in the tree** (~834 paths at the last
reading). **A standing condition, already routed as a finding. Do not commit any of it and do not
re-litigate it.**

**P8. `.gitattributes` marks these paths `text: auto`** and `core.autocrlf` is **not set**.
**Consequence you must respect in every hash comparison:** for a file whose worktree copy has CRLF
endings, a worktree sha256 and a `git cat-file blob` sha256 **will not agree**. **When you compare,
say which side you measured, and never report a CRLF/LF difference as a content difference.**

**P9. The riders of Task 0 are LEADS.** The writing side did **not** open `open_items/OI-376.md` or
`open_items/OI-374.md` this turn. Line numbers below come from the next-act record. **Measure them
yourself; the files may have moved.**

---

## 3. ASSUMPTIONS — declared so you can falsify them

- **A1. NO COUNT OF THE HANDOFF'S ENTRIES IS ASSERTED OR IMPLIED.** Measure the difference against
  the tip and report it, **with the matching pattern you used stated**, since two patterns give two
  populations. **Whatever number you get is NOT a STOP.**
- **A2. The tip has not moved since P1.** **If it moved, STOP.**
- **A3. The ledger's ruled entry shape exists somewhere in the tree (P4).** **Falsify it.** If you
  cannot find it, the batch still completes: carry every candidate in the **provisional** four-field
  shape of plan §2, **labelled PROVISIONAL on every entry and in the file's banner**, and report the
  absence as this batch's leading finding.
- **A4. The mining inputs of Task 3 are the whole population.** **Falsify it.** If you meet a source
  of empirical findings that Task 3 does not name, report it and say what it would add — **do not
  mine it**, and do not silently widen your own scope.
- **A5. Every candidate can be judged on the admission test by reading alone.** **Falsify it.** A
  candidate whose admission turns on a measurement you cannot make is reported **UNDECIDABLE with
  the measurement it would need named** — never guessed, and never admitted on plausibility.
- **A6. The two riders of Task 0 are line-edits that cascade nothing**, because neither touches the
  INDEX. **Falsify it at the guard set in Task 6.** If anything goes red that was not red before,
  **STOP and report** — do not sweep, and do not regenerate.

---

## 4. DECLARED START STATE — measure and report; assert nothing

The tip and `refs/remotes/origin/master`; `python tools/audit/changed_paths.py`; the size and sha256
of each of the four files of P6 **and of this instruction file**, at the working tree, **stating
that side (P8)**; the current failing set from `HEAD:tools/audit/guard_state.json`; the length of
`gating_ids` and the count of `non_gating_rows`; and the line of `open_items/OI-376.md` carrying the
`D-436` citation, quoted with its line number.

---

## 5. FINDINGS ROUTING

Per Ruling 9 of 2026-08-21. **Analysis findings** → the quarantined audit questions; do not act.
**Apparatus findings** → report them; **open NO register row** — this batch opens none. **Everything
else** → report with finding, date and reason, and discard. **★ You may not fix what you find.**

---

## 6. TASKS

### Task 0 — land the writing-side files and apply the TWO RIDERS

The riders are a **registered expectation** carried by whichever dispatch came first, per the
sixty-third handoff entry. This is that dispatch.

**(a) `open_items/OI-376.md`.** Locate the sentence citing **`D-436`** — the next-act record reports
it at line 99, reading *"([[OI-319]], [[OI-336]], **D-436**)"*; **measure the line yourself and quote
what you find.** **Correct the citation in place to `D-438`, with an inline correction note, exactly
as the INDEX row was corrected at `744ed4a708`** — read that commit's diff and copy the note's form
rather than inventing one. **Check `D-438` at `DECISIONS.md` before you write it.** **Change nothing
else in the file**: no status, no verdict, no re-wording.

**(b) `open_items/OI-374.md`.** Add the cascade-sweep batch's observation: **the variable is not only
the interpreter's output encoding but the LAUNCHING SHELL**, and it can move a guard artifact's
committed bytes **between two commits of the same batch**. Record with it that **no verdict moved**
— both runs reported `OVERALL PASS`, and encoding touches captured text and never an exit code.
**★ The row's status is NOT flipped, no verdict is added, and no new row is opened** — [[OI-374]]
already owns this subject.

**Neither rider touches `OPEN_ITEMS.md`.** If you believe one must, **STOP and report** — that would
be a cascade this batch is not built to absorb.

**Then run `python tools/audit/index_status_lint.py`. It must PASS. If it fails, STOP.**

### Task 1 — measure the start state (§4)

**Do not proceed if the tip differs from P1.**

### Task 2 — find the ledger's ruled entry shape (P4)

Search, quote whole with file and line numbers, or **establish and report that it does not exist**.
**Do not author a shape**, and do not treat plain §2's four properties as the ruled shape — they are
this batch's fallback under A3 and are labelled PROVISIONAL when used.

### Task 3 — harvest the candidates

Mine, and **only** these, each read at the objects:

1. **`docs/scoring_model.md`** — its §8 entries above all, which plan §6.1 names as passing through
   the admission test.
2. **`OPEN_ITEMS.md` and `open_items/`** — the register's own recorded empirical findings.
3. **`cowork_away_returns.md` and the `cc_report_*.md` population** at the repository root — the
   coding side's reported measurements.
4. **The handover records** — `cowork_handoff.md`, at its entries' measured findings only.

**For every candidate record:** the fact **stated approach-level and implementation-stripped** (if
you cannot state it without naming a mechanism of this implementation, that is itself the answer to
the admission test — say so); its **provenance**, measured at the object, with file and line; its
**uncertainty**, in the terms the source itself gives, never sharpened; and its **establishment
status** as the source declares it, never upgraded.

**★ Do not paraphrase a source into a stronger claim than it makes.** Where a source hedges, the
candidate hedges in the same words.

### Task 4 — apply the admission test, and admit nothing

For each candidate, report **PASSES / FAILS / UNDECIDABLE** against *does the fact survive the
implementation being thrown away?*, **with the reasoning in one or two sentences**, and with the
approach-level requirement judged separately and reported separately.

**Use plan §6.4's own two worked cases as your calibration** and say, for each candidate, which of
the two it resembles: a prohibition on re-attempting a specific mechanism of the dormant scorer
**fails**; a fact about the music or the corpus **passes**.

**★ Every verdict here is a proposal. Nothing is admitted.**

### Task 5 — write the reading file

Write **`cowork_empirical_findings_candidates.md`** at the repository root, for the user, with the
banner *DRAFT — CANDIDATES ONLY, NOT ADMITTED, NOT THE LEDGER*.

*(The name carries no date because the file is a working list superseded by the ledger itself; the
ground is stated here so the departure from the dated convention is not claimed by silence.)*

It carries: the entry shape you found (or the PROVISIONAL fallback, banner-labelled); every
candidate in that shape with its Task-4 verdict and reasoning; the candidates you judged
UNDECIDABLE with the measurement each would need; and **the sources you mined with what each
yielded, including any that yielded nothing.**

### Task 6 — the guard set, ONCE, read-only

Run `python tools/audit/gen_guard_state.py` **once**. **Expect `failing: 1`, the standing red
alone.** **If anything else is red, REPORT IT AND STOP — do not regenerate, do not sweep, do not
fix.** A6 is falsified at this task and nowhere else.

### Task 7 — ONE commit

`git add` and commit together: the four files of P6 that are the writing side's
(`cowork_handoff.md`, `cowork_rulings_2026_08_25_next_act_sitting.md`,
`cowork_blind_session_opening_instruction_harmony_boundary.md`), the two rider files
(`open_items/OI-376.md`, `open_items/OI-374.md`), `cowork_empirical_findings_candidates.md`, and
**whatever Task 6's run wrote** — and nothing else. **Message:** state that it lands the handoff's
sixty-third entry, the next-act record and the blind session's opening instruction, applies the two
riders, and lands the ledger candidates uncompared and unadmitted. **Do not assert the end state in
this message.**

### Task 8 — the final guard summary, in a SEPARATE, LATER commit

Report Task 6's summary in its ruled shape. **Land, as the second commit: this instruction file and
your report.** **★ THE E-ORDERING RULE: a commit cannot assert its own end state.**

---

## 7. REGISTERED EXPECTATIONS — MET or NOT MET, with the measurement beside each

- **E0 — the three writing-side files land byte-identical**, measured at the committed objects,
  equal to your Task-1 measurement. **State which side you measured (P8).**
- **E1 — Task 7's commit contains exactly the paths named, and nothing else. List them.**
- **E2 — `OPEN_ITEMS.md` is NOT in either commit.** Neither rider touches it.
- **E3 — `open_items/OI-376.md` differs from `0f18b358:open_items/OI-376.md` by the citation
  correction and its inline note alone.** No status changed, no other sentence moved.
- **E4 — `open_items/OI-374.md` differs by the added observation alone**, with its status cell
  unchanged.
- **E5 — no tool source file was modified.** Measure: no path under `tools/` ending `.py` appears in
  either commit.
- **E6 — the failing set at Task 6 is the standing red alone.** If NOT MET, the batch stops there
  and that is its report.
- **E7 — no artifact this batch wrote is named, banner-marked or structured as the ledger.**
- **E8 — the batch lands exactly TWO commits, in order.** If the ordered structure yields a
  different number, **reconcile it in your close — do not invent a commit, and do not silently
  absorb one.**

---

## 8. WHAT THIS BATCH DOES **NOT** DO

No `src/` change; no build; no test written, run, moved or changed; no golden refreshed; nothing
under `tools/corpus/` or `tools/robust_stop/`; no behaviour change and no design.

**And specifically:** it **builds no ledger** and **admits no fact**; it **authors no entry shape**;
it **edits no tool source**; it does **not** touch [[OI-372]] or its tool and **never regenerates a
DECISION red**; it does **not** sweep — Task 6 is read-only; it does **not** create, flip, close or
re-word any register row, and the two riders change **no** status; it does **not** touch either
derivation boot pack, the pack generator, the manifest, either withheld family, either session
brief, or either blind derivation output; it does **not** read either blind output at all; it does
**not** open, boot, configure or prepare any derivation session, and it does **not** touch
`cowork_blind_session_opening_instruction_harmony_boundary.md` except to commit it unread-into; it
does **not** touch `CLAUDE.md`, `STATUS.md`, `DECISIONS.md` (which may be READ), `ARCHITECTURE.md`
or any other governing document; it does **not** allocate a finding number (**Ruling 9 opens no
findings series**); and it does **not** propose a remedy for anything it finds.

**[[OI-179]] stays OPEN and GATES. [[OI-374]], [[OI-376]] and [[OI-377]] stand as found apart from
the two ruled riders. The three deferred apparatus items stay deferred. The five quarantined
questions stand.**

---

## 9. THE WRITING SIDE'S SELF-CHECK

- **P1 and P2 were measured this turn** by reading `.git/HEAD`, `.git/refs/heads/master` and
  `.git/refs/remotes/origin/master` with file tools on the user's machine. **No shell command was
  run there**, so `git status` was never at risk.
- **P3, and the `gating_ids` and `non_gating_rows` figures, are RELAYED from
  `cowork_rulings_2026_08_25_next_act_sitting.md` §0**, where the previous session states it
  verified them at the objects. **This side did not re-measure them**, and they are ordered measured
  at §4 for that reason.
- **★ P4 IS PUBLISHED AS A LEAD AND AS AN ADMISSION OF WHAT THIS SIDE COULD NOT FIND**, rather than
  filled with an invented shape. Three ruled documents cite an entry shape this side could not
  locate; naming that gap is worth more than a plausible reconstruction of it.
- **P6 carries no hashes deliberately** — a figure that goes stale between writing and delivery is
  worth less than one you measure. **No file's own hash is written into it (the standing bar).**
- **P9 declares that the rider files were not opened**, so their line numbers are leads and are
  ordered measured.
- **§0's candidate/admission distinction is the load-bearing safety rule of this batch**, and it is
  stated before the tasks rather than inside them for that reason.
- **The `git status` defect is not repeated**, and the `D-436`/`D-438` transposition is flagged at
  Task 0(a) with an order to check `DECISIONS.md` before writing.
- **This dispatch copies `cc_instruction_cascade_sweep.md`'s structure clause for clause.** The
  clauses it changes: §0 carries the candidate/admission bar in place of the staleness/decision bar,
  which is restated in §0's closing paragraph rather than dropped; Task 0 is new and carries the
  riders; Task 6 is read-only where the cascade batch's sweep was a loop; E2–E4 and E7 are new. A
  reader counts this for themselves.
- **Declared departures of the writing side:** the ordinary session-start read NOT taken, so this
  side is **not oracle-aware**; `cowork_rulings_2026_08_25_method_voiding_sitting.md` NOT opened,
  deliberately, since it may quote the oracle; `cowork_audit_protocol.md`'s dispatch-protocol section
  NOT re-read before writing this dispatch; `BUILD_AND_TEST.md` NOT read; the handoff read at its
  sixty-third entry and at targeted searches, **not whole**.

---

## 10. YOUR REPORT

Write `cc_report_ledger_harvest.md` at the repository root. **It rides Task 8's commit.** Carry: the
declared start state; the `origin/master` reading and its ancestry (P2); **the entry shape you found,
quoted, or the statement that it does not exist (P4) — the leading finding of this batch**; the two
riders' before-and-after lines quoted; the lint output; the candidate table with every Task-4 verdict
and its reasoning; the sources mined and what each yielded; both commit hashes and their path lists;
E0–E8 each MET or NOT MET with the measurement beside it; the guard summary in its ruled shape; the
measured handoff difference with its pattern (A1); and every finding routed under §5, including any
you declined to act on.

**If anything STOPs you, stop there and report what you had done. A partial batch honestly reported
is worth more than a complete one that guessed.**
