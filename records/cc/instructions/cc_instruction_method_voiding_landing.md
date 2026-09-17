# CC INSTRUCTION — the method-voiding landing batch

> **Written by Cowork, 2026-08-25, the forty-fifth session's thirteenth sitting.** You are a fresh
> Claude Code session. **Read this file whole before you touch anything.** Everything you need is
> in it or is measured by you; nothing is carried from a conversation you were not in.
>
> **★ THIS IS A RECORD-KEEPING BATCH.** It lands four writing-side files and creates ONE
> open-items-register row. **It changes no behaviour, touches no `src/`, runs no analysis, and
> reads no blind derivation output.**

---

## 0. THE ONE THING TO DO FIRST — a stale lock the writing side left behind

**`.git/index.lock` exists in the repository and is a ZERO-BYTE STALE LOCK. It was created by the
writing side's own read-only `git status` through a bridge that cannot delete files. No git process
is running.** **Delete it before anything else** — `git add` and `git commit` will fail while it
stands.

**Verify before you delete, and report both:** its size (expect **0**) and that no git process is
running. **If it is NOT zero bytes, STOP and report** — that would mean something else is going on
and this instruction's premise is wrong.

---

## 1. RULING LEDGER — the rulings this batch executes, quoted

**From `cowork_rulings_2026_08_25_method_voiding_sitting.md` (landing in this batch, §5):**

> *"One ordinary CC dispatch is owed and is written next. It lands, at its Task 0, the four files
> now on disk uncommitted … and it creates the register row and its detail file, in that same
> commit, under Ruling 3 above, at an identity it MEASURES."*

**From the same record, §4 — the routing, and the correction the writing side made to its own
citation:**

> *"It is rowed in the open-items register under rules (c) and (e) … **No finding number is
> allocated. The identity is the next free one and is MEASURED by the landing batch across both the
> INDEX and `open_items/`, never asserted by this side.**"*

> *"The landing batch therefore creates the row WITHOUT a non-gating declaration, so it takes the
> ruled DEFAULT and GATES … The verdict is put to the user on its own surface."*

**From `cowork_rulings_2026_08_21_successor_plan_sitting.md` §9 (Ruling 9) — the governing routing,
quoted because this batch's Task 2 exists only because of it:**

> *"A finding that bears on the analysis goes to the quarantined audit questions; a finding about
> the apparatus is rowed under the open-items register's rules (c) and (e) and lapses under the
> ruled lapse rule (D-676) … **No findings series is opened.**"*

**From `CLAUDE.md`'s open-items-register section — rules (c) and (e), verbatim:**

> *"(c) every newly discovered issue gets an **index row AND its detail file** **in the same
> commit** that records the discovery; … (e) tracking an owed/deferred/TODO item in prose only,
> without a register row, is a doc-sync violation (#10)."*

**★ NOTE THE CONSEQUENCE FOR YOUR COMMIT SHAPE: rule (c) makes the row and the record that discovers
it ONE COMMIT. Do not split them.**

---

## 2. PREMISE LEDGER — FACTs, each measured at an object, each re-measurable by you

**P1. The tip is `f225b61343ff3de022d32d6b7514d835b87093cf`, both refs at it, unmoved.** Measured
by the writing side this turn. **Re-measure it as your first act after §0 (A2 below). If it differs,
STOP.**

**P2. Exactly four paths differ from the tip, and no others are expected to.** Measured:

| path | state vs tip | size (bytes) | sha256 |
|---|---|---|---|
| `cowork_handoff.md` | MODIFIED | 688028 | `cf5f2a49479945809f9ecf65343fc16a499d122209c49e1d355463576996dad9` |
| `cowork_rulings_2026_08_25_determination_route_sitting.md` | UNTRACKED | 7635 | `e3791743a73899d9c7027d67f55d2fa6a5fd0e171dd3e5ea651ed649999153e5` |
| `cowork_rulings_2026_08_25_forward_fact_sitting.md` | UNTRACKED | 8859 | `cd60697990c167c771e2800308775636ba11a1add6a8491312f4d01b6f47197d` |
| `cowork_rulings_2026_08_25_method_voiding_sitting.md` | UNTRACKED | 19961 | `0c27e6f88d941deed1b239876d6da61b21c2c717b1013152137fa54d49cbd6a4` |

**These four files are FINISHED WRITING-SIDE ARTIFACTS. You do not edit them, reflow them, fix their
typography or correct their prose. If you believe one is wrong, REPORT IT — do not fix it.**

**★ P2a — TWO FURTHER UNTRACKED PATHS ARE EXPECTED AND ARE **NOT** PART OF TASK 2's COMMIT:** this
instruction file, `cc_instruction_method_voiding_landing.md`, and the report you will write. **Both
ride TASK 3's commit, not Task 2's** — Task 2's commit is exactly the six paths of E1. **Do not edit
this instruction file; MEASURE its size and sha256 in your start state and report them**, so a later
reader can tell which instruction was executed. *(No expected value is given for it: a file cannot
state its own hash, and a figure that would be false the moment it was written is worse than none.
The writing side wrote one here, saw it go stale on the next edit, and removed it.)*

**P3. The open-items register is an INDEX plus one detail file per item.** `OPEN_ITEMS.md` is the
INDEX and the authoritative status surface; `open_items/OI-<n>.md` carries narrative and provenance
only and **never a status of its own**.

**P4. The register's highest existing detail-file identity at the tip is OI-375.** Measured by the
writing side from the tree listing of `open_items/`. **★ THIS IS A LEAD, NOT YOUR ANSWER. You
measure the next free identity yourself, across BOTH the INDEX and the `open_items/` directory, and
you report the number you used and how you derived it.** If the two disagree — an index row with no
detail file, or a detail file with no index row — **report the disagreement and take the next
identity above the higher of the two.**

---

## 3. ASSUMPTIONS — declared so you can falsify them

- **A1. NO COUNT OF THE HANDOFF'S ENTRIES IS ASSERTED HERE.** The writing side states only that it
  prepended ONE new entry (the sixtieth) and appended a superseded-marker to the fifty-ninth
  heading. **You MEASURE the actual difference `cowork_handoff.md` carries against the tip and
  report it. If the tree carries MORE inserted entries than one, that is expected-possible and is
  NOT a STOP — report the number you measured.** *(This assumption is written this way because the
  writing side got it wrong twice by asserting it.)*
- **A2. The tip has not moved since P1 was measured.** Falsify by re-measuring. **If it moved,
  STOP.**
- **A3. Nothing is running.** No other session holds this repository. Falsified by §0 finding a
  non-zero lock or a live git process — **STOP.**
- **A4. The four files in P2, plus the two of P2a, are the complete set of paths this batch expects
  to differ from the tip.** If your `git status` shows **any other** modified or untracked path,
  **report it and do NOT commit it** — land only what P2 and P2a name, in the commits they name.
- **A5. Creating one register row and one detail file changes no generated artifact's validity
  except the non-gating apparatus set, and that set is unaffected here** because the new row makes
  **no apparatus claim** and so is not one of its candidates. **Falsify it: run the guard set at
  Task 3 and report what it says.** If `gen_nongating_apparatus_rows.py` STOPs or its output
  changes, **report it — do not fix it, and do not add a verdict to the row to make it pass.**

---

## 4. DECLARED START STATE — assert nothing; measure and report

Report, before any write: the tip; the output of `git status --porcelain -uall`; the size and
sha256 of each of the four P2 paths **as they sit in the working tree**; the highest identity in
`OPEN_ITEMS.md` and the highest in `open_items/`; and the result of §0.

---

## 5. FINDINGS ROUTING — for anything you notice that is not in this instruction

**A finding that bears on the analysis** → the quarantined audit questions; do not act on it.
**A finding about the apparatus** → report it; **do NOT open a second register row for it in this
batch** — this batch opens exactly one, and a second would be self-generated work. **Everything
else** → report with finding, date and reason, and discard.

**★ AND THE STANDING BAR: you may not fix what you find.** Report it and stop there.

---

## 6. TASKS

### Task 0 — remove the stale lock (§0)

Verify zero bytes, verify no git process, delete, report.

### Task 1 — measure the start state (§4)

Report it whole. **Do not proceed to Task 2 if the tip differs from P1.**

### Task 2 — create the register row AND its detail file, and commit them TOGETHER WITH the four files

**Measure the next free identity first** (P4). Call it **OI-N** in your report, naming the actual
number.

**(a) The detail file `open_items/OI-N.md`.** It carries narrative and provenance only and **never a
status of its own** (P3). Its content is the finding as the ruling record states it — write it from
`cowork_rulings_2026_08_25_method_voiding_sitting.md` §4, which you have in the tree, and **quote
rather than paraphrase where it states the finding**. It must carry, at minimum:

1. **The finding.** `CLAUDE.md` is the single point of failure for its own discoverability: the
   instructions to read `STATUS.md` and `DECISIONS.md`, and the gating rows that tell a session what
   it may not do, live only inside the file that may not arrive.
2. **The mechanism, attributed as a relayed account and NOT as a measurement by this project.** A
   throwaway Cowork session opened by the user on 2026-08-25 reported that `CLAUDE.md`, and only
   `CLAUDE.md`, arrives at boot — whole, as a `# claudeMd` system-reminder inside the first user
   turn, from a per-connected-folder mirror — and that the connected-folder set is what drives it.
   **One variable it could not observe about itself: whether the mechanism reads only each connected
   root or also walks up toward an ancestor. Record that as INFERRED, NOT OBSERVED.**
3. **The four configurations it named in which no repository file arrives:** no folder connected at
   all; only a subfolder that itself carries no `CLAUDE.md`; no desktop bridge; the file renamed or
   moved. **Relayed, not endorsed.**
4. **The consequence, which is the part that bites:** in those configurations a session starts with
   no repository text, no knowledge that standing instructions exist, and **no signal that anything
   is missing** — it does not fail loudly; it proceeds ungoverned and unaware. **A ruling is not
   binding mechanically; it binds only a session that met it.**
5. **The irony, which is why the row is not trivially closable:** the configuration that gives a
   deriving session its correct blindness is the same one that leaves an ordinary session silently
   ungoverned.
6. **Provenance:** discovered 2026-08-25; relayed by the user from a throwaway session; rowed on
   Ruling 3 of `cowork_rulings_2026_08_25_method_voiding_sitting.md` under Ruling 9 of
   `cowork_rulings_2026_08_21_successor_plan_sitting.md` and register rules (c) and (e).
7. **★ NO REMEDY.** Do not propose one, do not sketch one, and do not write a task list. **This row
   is a finding, not a task with a foregone answer.** In particular: **do not edit, split, move,
   rename, copy or duplicate `CLAUDE.md`, and do not add any tripwire, check, marker or fallback
   file.**

**(b) The INDEX row in `OPEN_ITEMS.md`.** **Match the file's existing row shape exactly** — read
neighbouring rows and copy their column structure; the ONE index parser STOPs on a row that does not
split into six cells, and `tools/audit/index_status_lint.py` STOPs on a non-canonical opening token
in the status cell. **The status cell opens with the canonical OPEN token used by its neighbours.**
The row is a **pointer, not a restatement** — a short name and description, the owning area, and a
`[detail](open_items/OI-N.md)` link.

**★ THE ROW MAKES NO APPARATUS CLAIM AND CARRIES NO NON-GATING DECLARATION.** Under the register's
ruled default it therefore GATES. **This is deliberate and ruled; do not "helpfully" declare it
apparatus to keep the gate clear.**

**(c) ONE COMMIT.** `git add` the two new register files **and the four P2 paths**, and commit them
together — rule (c) requires the row in the same commit that records the discovery. **Message:**
state that it lands the three 2026-08-25 ruling records and the handoff's sixtieth entry, and opens
OI-N on the `CLAUDE.md` discoverability hazard. **No other path enters this commit.**

### Task 3 — the guard set, in a SEPARATE, LATER commit

**Run the guard set** (the 75 tools; the standing red is `gen_filing_convention_application.py
--check`, [[OI-372]]). Report the summary in its ruled shape: `{run, passing, failing,
failing_tools, not_run, historical_records}`.

**Land, as its own second commit:** whatever the run legitimately produces, **plus this instruction
file and your report** (P2a). **★ THE E-ORDERING RULE:
a commit cannot assert its own end state. Task 2's commit does not claim the guard set passes; this
run is what says so, and it lands after.**

**If a guard fails that is not the standing red: REPORT IT AND STOP. Do not fix it.**

---

## 7. REGISTERED EXPECTATIONS — state each as MET or NOT MET, with the measurement beside it

- **E0 — the four files land byte-identical.** After Task 2's commit, the sha256 of each of the four
  P2 paths **as committed** equals the value in P2's table. **Measure at the committed objects
  (`git show <commit>:<path> | sha256sum`), not at the working tree.**
- **E1 — the row and its detail file exist, at a measured identity, in the SAME commit as the four
  files.** Measure: the commit's changed-path list contains exactly six paths — the four of P2,
  `OPEN_ITEMS.md`, and `open_items/OI-N.md`. **Report the identity N and how you derived it.**
- **E2 — the batch lands exactly TWO commits, in order.** Task 2's, then Task 3's. **If the ordered
  structure yields a different number, reconcile it in your close and say what the actual number was
  and why — do not invent a commit to match this line, and do not silently absorb one.**

---

## 8. WHAT THIS BATCH DOES **NOT** DO

No `src/` change; no build; no test written, run, moved or changed; no golden refreshed; nothing
under `tools/corpus/` or `tools/robust_stop/`; **no behaviour change to the analysis and no design**.

**And specifically:** it does **not** touch either derivation boot pack, the pack generator, the
manifest, either withheld family, either session brief, or either blind derivation output; it does
**not** read either blind output at all — not even a bounded receipt; it does **not** open, close,
flip, re-word or annotate any register row other than the one it creates; it does **not** amend,
reflow or correct any of the four landing files; it does **not** touch `CLAUDE.md`, `STATUS.md`,
`DECISIONS.md`, `ARCHITECTURE.md` or any other governing document; it does **not** regenerate any
generated artifact except as Task 3's guard run does so of its own accord; it does **not** allocate
any finding number; it does **not** propose or implement any remedy for the hazard it rows; and it
does **not** open, boot or prepare any derivation session.

**[[OI-179]] stays OPEN and GATES. [[OI-372]] and [[OI-374]] stand as found. The three deferred
apparatus items stay deferred — do not pick any of them up.**

---

## 9. THE WRITING SIDE'S SELF-CHECK — what it declares about this instruction

- **Every hash, size and identity in §2 was measured at an object or at the working tree this turn,
  not recalled.** P4 is explicitly marked a lead you must re-measure.
- **The stale lock in §0 was created by the writing side's own read.** It is declared rather than
  left for you to trip over.
- **The routing in §1 is quoted from two objects** — Ruling 9 of the successor-plan sitting and
  `CLAUDE.md`'s register section — **because the writing side had cited it wrongly from memory, put
  the wrong citation to the user, and corrected it at the object before this instruction was
  written.** That correction is recorded in §4 of the record you are landing. **If you find the
  quotes above do not match the objects, STOP AND REPORT — that would mean the correction is itself
  wrong.**
- **A1 orders a measurement rather than asserting a count**, because the writing side got that
  assertion wrong twice.
- **Nothing in this instruction asks you to judge, compare, read or evaluate a blind derivation
  output**, and nothing asks you to invent a mechanism for anything.

---

## 10. YOUR REPORT

Write `cc_report_method_voiding_landing.md` at the repository root. **It rides TASK 3's commit, never
Task 2's** (P2a). Carry: §0's result; §4's
declared start state; the identity N and its derivation; both commit hashes and their changed-path
lists; E0/E1/E2 each MET or NOT MET with the measurement beside it; the guard-set summary in its
ruled shape; the measured handoff-entry difference (A1); and **every finding you routed under §5,
including any you declined to act on.**

**If anything STOPs you, stop there and report what you had done up to that point. A partial batch
honestly reported is worth more than a complete one that guessed.**
