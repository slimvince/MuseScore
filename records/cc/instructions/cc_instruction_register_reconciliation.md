# CC INSTRUCTION — the register-reconciliation and harvest-completion batch

> **Written by Cowork, 2026-08-25, the forty-eighth session.** You are a fresh Claude Code session.
> **Read this file whole before you touch anything.**
>
> **★ THIS BATCH HAS TWO OBJECTIVES.** (A) Close the gap between rulings that were given and
> registers that were never amended. (B) Complete the empirical-findings harvest's coverage over the
> two sources the previous batch proved it never reached. It changes no behaviour, touches no `src/`,
> **edits no tool source**, runs no analysis, and **reads no blind derivation output**.
>
> **★ DO NOT RUN `git status`.** This repository's guard refuses it (**D-253**). The sanctioned
> enumeration is **`python tools/audit/changed_paths.py`** (`--staged`, or `--commit <hash>`).

---

## 0. THE BARS THAT MAKE THIS BATCH SAFE — READ THEM BEFORE ANYTHING ELSE

**★ ADMISSION IS NEVER YOURS TO MAKE.** An admitted fact enters the empirical findings ledger and is
thereafter read by deriving sessions as established. **Nothing this batch writes is an admission, no
artifact this batch writes is the ledger, and no file this batch writes may be shaped so a later
reader could mistake it for the ledger.** Ruling 8 of 2026-08-21 requires every hand admission to be
re-checked at the ledger's gate; a batch that quietly admitted its own candidates would defeat that
re-check before the gate exists. Your product is **candidates with your reasoning stated so the user
can overturn it**.

**★ THE SWEEP RULE, ABSOLUTE.** A **staleness** red — an artifact that no longer re-derives — **is
regenerated**. A **decision** red — a failure demanding an authored verdict — is **never**
regenerated, because regenerating it converts an unanswered question into a silent pass. **If you
cannot tell which kind a red is, treat it as a DECISION red and STOP.**

**★ `tools/audit/gen_filing_convention_application.py --check` ([[OI-372]]) IS THE ONE STANDING
DECISION RED.** Do not regenerate it, do not run it in write mode, do not investigate it, do not
authored-verdict anything for it. If any **other** decision red appears, STOP and report.

**★ FOUR TRACKED FILES ARE MODIFIED AGAINST THE TIP AND THAT IS DELIBERATE.**
`open_items/OI-376.md`, `open_items/OI-374.md`, `tools/audit/guard_state.json`, `cowork_handoff.md`.
They are the stopped ledger-harvest batch's completed work, documented at §11 of
`cc_report_ledger_harvest.md`, whose words are *"Nothing needs redoing except the commits."*
**Do not revert any of it, do not re-apply the riders, and do not re-litigate it.**

**★ THIS BATCH EDITS THE DECISIONS REGISTER.** That is unusual and it is authorised by name, at the
two rulings quoted at §1.2 and nowhere wider. **You may write only the amendments those rulings
order.** You may not open a register row for anything else, may not correct a neighbouring entry you
believe is wrong, and may not renumber anything.

**★ THE BLAST RADIUS IS MEASURED AND IT IS NOT FREE.** Opening one register row turned three
artifacts red in a single round, and **two further artifacts moved without ever appearing in a
failing set**, because two guard-set members run in **living mode** and write on every run. Expect the
sweep at Task 8 to move more than the failing set names. Report everything that moved.

**★ THREE MEASUREMENT BARS.** (1) **A worktree hash and a blob hash do not agree for a CRLF file** —
`.gitattributes` marks these paths `text: auto` and `core.autocrlf` is **NOT** set. Always say which
side you measured, and never report a line-ending difference as a content difference. (2) **Never
write a file's own hash into that file** — it is stale on the next edit; order it MEASURED.
(3) Measure, never assert: every count, size and hash in your report carries the command that produced
it.

**★ VOCABULARY, RULED 2026-08-17 AND 2026-08-22, AND ENFORCED IN YOUR REPORT.** Write **"measurement
tool"**, never *instrument*. **"A changed passage"**, never *hunk*. **"The current commit"**, never a
bare *HEAD*. **"Untrusted source"**, never *witness*. When rating an option write **"towards the
objective" / "towards the principles"**, never *against* — *against* is reserved for the case opposing
an option. Explain any term you coin in plain words the first time you use it.

---

## 1. RULING LEDGER — quoted

### 1.1 Today's sitting — `cowork_rulings_2026_08_25_v1_sufficiency_sitting.md`

This record is on disk, untracked, and lands at your Task 0. It carries three rulings. In summary,
and **you must read the record itself rather than rely on this summary**:

- **Ruling 1** — the derivation method is ruled **USABLE for v1**, on the user's ground (a first
  version cannot be the ultimate one because the sources are not exhausted until the audit has run;
  what v1 can be is the best derivable from everything held except the code, plus added research).
  This discharges the pilot's postcondition at §3.2 of the phase-definition surface by its first limb
  and **supersedes the method's VOIDED status**.
- **Ruling 2** — independence is evidenced by the ten DIFFERS rows of
  `ratification_surfaces/cowork_comparison_harmony_boundary_reading.md` §6.
- **Ruling 3** — the **framework** and **detail-specification** phases are **no longer HELD**, and E
  (the user's judgement of the existing derivation) and C (the re-run of the held-out test) are **not
  the next act and are not owed**. **B — the empirical findings ledger — is untouched and still owed
  as a framework-phase input.** That is why this batch exists.

### 1.2 The two amendments this batch writes — `cowork_rulings_2026_08_25_regress_termination_sitting.md`

**Ruling 1 of that record, at its Limb A and Limb B (the record's lines 69–90), carries the exact
text to be added to three principles: #19 (D-182), #18 (D-181) and #24 (D-187).** Read those limbs at
the record and apply them **verbatim**. Do not apply them from this file, from `cowork_handoff.md`, or
from any summary — three of the closing session's six counted errors were characterising a text from a
gloss instead of opening it.

**Ruling 2 of that record orders the sharpened decision-surface rule entered in the decisions register
under its own identifier**, on the ground that it is presently nowhere in the register and survives
only by being re-typed into each successor handoff entry.

### 1.3 Standing — Ruling 9 of 2026-08-21

Everything you find that is not a candidate: an **analysis** finding goes to the quarantined audit
questions; an **apparatus** finding is **reported**; everything else is discarded with finding, date
and reason. **You may not fix what you find. No findings series exists and you allocate no finding
number.**

### 1.4 The ledger's ruled entry shape — FIVE fields, resolved

At `cowork_rulings_2026_08_15_method_directions.md:46–54`, direction 4 of nine, restated at
`ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md:95–99` and `:217–219`. The five
fields: **the fact** (approach-level, implementation-stripped); **provenance**; **uncertainty** (#24);
**establishment status** (#19); **and its failure diagnosis, or "cause undiagnosed"**. Two attached
rules travel with it: a measured-worse verdict rules out **the tried implementation** of an approach,
not always the approach; and **both polarities are carried** — design antipatterns into the ledger,
process antipatterns into the phase definitions' constraints and stop rules.

---

## 2. DECLARED START STATE — measure it, report it, assert nothing

Expected at your Task 1. **If any of it does not hold, report the difference and continue; if the tip
differs, STOP.**

- **Tip:** `0f18b358bc6a8da5ec6064760d675129e64d8f3b`. `refs/remotes/origin/master`:
  `f225b61343ff3de022d32d6b7514d835b87093cf` — **not the tip, ancestry not established by any side,
  and not a STOP.**
- **Tracked, modified (four):** `cowork_handoff.md`, `open_items/OI-374.md`, `open_items/OI-376.md`,
  `tools/audit/guard_state.json`.
- **Untracked, root-level writing-side and coding-side (nine):**
  `cowork_rulings_2026_08_25_next_act_sitting.md`,
  `cowork_rulings_2026_08_25_second_vector_sitting.md`,
  `cowork_rulings_2026_08_25_regress_termination_sitting.md`,
  `cowork_rulings_2026_08_25_v1_sufficiency_sitting.md`,
  `cowork_blind_session_opening_instruction_harmony_boundary.md`,
  `cc_instruction_ledger_harvest.md`, `cc_report_ledger_harvest.md`,
  `cowork_empirical_findings_candidates.md`, and **this instruction file**.
- **A pre-existing untracked population of roughly 834 paths** stands as a standing condition,
  already routed, **not to be re-litigated and not to be committed.**
- **The guard set at the previous batch's close: 75 run, 73 passing, 2 failing** — [[OI-372]] (the
  standing decision red) and `tools/audit/gen_evidence_pin_membership.py --check` (*"STALE vs the
  derivation: evidence_pin_membership.json does not re-derive"*), **a staleness red**, which
  pre-existed that batch's first edit.

---

## 3. ASSUMPTIONS — declared so you can falsify them

Falsify any of these at the object and say so in your report. The previous batch's most useful finding
came from falsifying a declared assumption.

- **A1** — Limbs A and B of the regress-termination record carry amendment text complete enough to
  apply verbatim, with no interpretation needed to site it in `decisions/group_S.md`.
- **A2** — the decisions register's own identifier-allocation convention determines a **unique**
  identifier for the decision-surface rule. **If it does not, STOP at Task 3** and report the
  candidates; allocation is not yours to guess.
- **A3** — `DEFECT_TYPES.md` and the `cc_<topic>_report.md` / `cc_<topic>_dossier.md` population are
  the **only** two harvest sources the previous batch did not reach.
- **A4** — regenerating `evidence_pin_membership.json` clears the staleness red. **Not claimed by any
  side; the previous batch explicitly did not claim it.**
- **A5** — no amendment at Tasks 2 and 3 turns a **decision** red on. If one appears, A5 is falsified
  and you STOP there.

---

## 4. TASKS

### Task 0 — land the writing-side files

`git add` and commit, as the batch's first act, **six paths**: `cowork_handoff.md` (already modified
in the tree), the four untracked 2026-08-25 ruling records
`cowork_rulings_2026_08_25_next_act_sitting.md`,
`cowork_rulings_2026_08_25_second_vector_sitting.md`,
`cowork_rulings_2026_08_25_regress_termination_sitting.md`,
`cowork_rulings_2026_08_25_v1_sufficiency_sitting.md`, plus **this instruction file**. Nothing else.
**Message:** state that it lands the handoff's sixty-fifth entry and the four 2026-08-25 ruling
records. **Do not assert the end state in this message.**

### Task 1 — measure the start state (§2)

`python tools/audit/changed_paths.py` for the tracked set. Read `.git/HEAD`,
`.git/refs/heads/master`, `.git/refs/remotes/origin/master` for the refs. Report sizes and hashes for
each of the nine untracked root-level files, **saying which side you measured**. Report the difference
against §2 and assert nothing beyond what you ran.

### Task 2 — apply the three ruled clause amendments to `decisions/group_S.md`

Read `cowork_rulings_2026_08_25_regress_termination_sitting.md` at its Limbs A and B. Apply the added
clauses to **#19 (D-182)**, **#18 (D-181)** and **#24 (D-187)** in `decisions/group_S.md`, verbatim as
that record states them.

**Validation:** `grep -n "inspectable" decisions/group_S.md` returns **zero** matches before your edit
and **at least one** after it. Report the changed passages in full.

**STOP conditions:** the record's text does not determine where in an entry the clause belongs; or
applying it would require rewording an existing sentence; or an entry's text on disk differs from the
text the record quotes for it.

### Task 3 — register the sharpened decision-surface rule in `DECISIONS.md`

Ruling 2 of the same record orders it entered under its own identifier. **Derive the identifier from
the register's own allocation convention.** Read the convention before you allocate; if it does not
determine a unique identifier, **STOP and report the candidates** (A2).

The rule's text is restated at §6 of the handoff's sixty-third entry and re-typed in successive
entries. **Reconcile those restatements before you write**: if they differ from one another, report
the difference and **STOP** — which restatement is authoritative is the user's, not yours.

**Validation:** the new identifier appears in `DECISIONS.md` exactly once, in its group's table and in
whatever per-group file that group's convention requires, with no other row moved or renumbered.

### Task 4 — update `STATUS.md`

Its latest entry still reads *"the method ruling suspended"*, which Ruling 1 of today's sitting
supersedes. Write the new entry under the file's own conventions — it is a **living document**, keeps
only the latest batch's entries, and is a **POINTER** under the OI-222 remedy: no count, no identity
and no rendered value is restated in it (**D-431**). Move the superseded entry to `STATUS_ARCHIVE.md`
verbatim, as Ruling 4 of `cowork_rulings_2026_08_17_governing_surface_split.md` requires.

**Validation:** `python tools/audit/gen_governing_surface_split.py --check --pair STATUS.md`.

### Task 5 — complete the harvest: `DEFECT_TYPES.md`

The ruled ledger seed list names three seeds and the previous dispatch's Task 3 sent the harvest to
two of them. `DEFECT_TYPES.md` is the missing one (`cc_report_ledger_harvest.md` §9.1). Mine it whole.

Expect a **high** pass rate — a defect *type* is by construction the generalization of an instance, so
it is already approach-level — and **apply the polarity rule carefully**: a catalog of problem types
is exactly where design antipatterns and process antipatterns are most likely to be mixed. Design
antipatterns are candidates for the ledger; process antipatterns are **reported for the phase
definitions' constraints and stop rules** and are not ledger candidates.

### Task 6 — complete the harvest: the coding side's measurement reports

`cc_report_ledger_harvest.md` §9.2 measured that the previous dispatch's glob `cc_report_*.md` matches
37 files and yielded nothing, **because the coding side's measurement reports are named the other way
round**: `cc_<topic>_report.md` and `cc_<topic>_dossier.md`.

Enumerate that population first and **report its count before mining it**. The artifact inventory's
ruled verdict for that class calls it *"the richest DESIGN-antipattern source in the repository"* — a
report that says an approach was tried and measured worse, with its failure diagnosis or an explicit
*cause undiagnosed*. That fifth field is the one the previous side did not have; it is now ruled and
you carry it.

**If this population is large enough that mining it whole would exceed your batch, mine it in
recorded order, stop at a stated boundary, and say exactly which files you did not reach.** A silent
cap reads as coverage. **Do not sample.**

### Task 7 — merge into the candidates file, admitting nothing

Extend `cowork_empirical_findings_candidates.md` with what Tasks 5 and 6 yielded, in the ruled
five-field entry shape (§1.4), each with a PASSES / FAILS / UNDECIDABLE proposal, the approach-level
half judged separately, and **your reasoning stated so the user can overturn it**. Keep the previous
batch's 20 candidates unchanged and distinguish the new ones by their source. **Nothing is admitted.
This file is not the ledger and must not be shaped so it could be read as one.**

Record, in the file, **the sources you mined and what each yielded, including any that yielded
nothing.**

### Task 8 — the guard set, and the sweep to a fixpoint

Run `python tools/audit/gen_guard_state.py`.

- **[[OI-372]] stays red.** Never regenerate it.
- **Every other red: classify it first — staleness or decision — and say which and why.** Regenerate
  staleness reds. **STOP on any decision red.**
- Re-run the guard set after each regeneration round, **at most three rounds**. Two guard-set members
  run in living mode and write on every run, so a naive fixpoint may not exist; if the failing set is
  unchanged after three rounds, **STOP and report the residue** rather than looping.
- Report **everything that moved**, not only what appeared in a failing set.

Writing four ruling records at the repository root turns `evidence_pin_membership.json` stale. **The
user has ruled that this class of staleness is expected on amendment and is not to be reported as a
notable consequence** — regenerate it under the sweep rule and note it in one line, no more.

### Task 9 — ONE commit

`git add` and commit together: `decisions/group_S.md`, `DECISIONS.md` and whatever per-group file Task
3 required, `STATUS.md`, `STATUS_ARCHIVE.md`, `open_items/OI-376.md`, `open_items/OI-374.md`,
`cowork_empirical_findings_candidates.md`, `cc_instruction_ledger_harvest.md`,
`cc_report_ledger_harvest.md`, `cowork_blind_session_opening_instruction_harmony_boundary.md`, and
**whatever Task 8's runs wrote** — and nothing else. **Not one path from the ~834 standing untracked
population.**

**Message:** state that it writes the three ruled clause amendments, registers the decision-surface
rule, updates the status record, applies the two riders, and extends the ledger candidates uncompared
and unadmitted. **Do not assert the end state in this message.**

### Task 10 — the final guard summary, in a SEPARATE, LATER commit

Report Task 8's summary in its ruled shape. Land, as the second commit, **your report**.
**★ THE E-ORDERING RULE: a commit cannot assert its own end state.**

---

## 5. REGISTERED EXPECTATIONS — MET or NOT MET, with the measurement beside each

- **E0** — the **six** paths of Task 0 land byte-identical to your Task-1 measurement. **State which
  side you measured.**
- **E1** — `grep -n "inspectable" decisions/group_S.md`: zero matches before Task 2, at least one
  after.
- **E2** — exactly three entries of `decisions/group_S.md` are changed, and they are D-182, D-181 and
  D-187. No other entry moved by one byte.
- **E3** — the identifier allocated at Task 3 appears in `DECISIONS.md` exactly once and no existing
  row is renumbered.
- **E4** — `OPEN_ITEMS.md` is in neither commit.
- **E5** — no path under `tools/` ending `.py` is modified by this batch.
- **E6** — the failing set at Task 8's last round is **[[OI-372]] alone**. If it is not, this is NOT
  MET and you report the residue rather than sweeping further.
- **E7** — the count of the `cc_<topic>_report.md` / `cc_<topic>_dossier.md` population is **measured
  and stated** before Task 6 mines it, and the files not reached are named.
- **E8** — no path of the ~834 standing untracked population is in either commit.

---

## 6. WHAT THIS BATCH DOES **NOT** DO

No `src/` change. No golden. **No test changed, moved or run.** No behaviour change to the analysis
and no fix to inference. **No measurement of the analysis built, designed, scoped or run.** No
derivation and no comparison. **No blind derivation output opened at all**, and no oracle document
opened. **No edit to `CLAUDE.md`, to `ARCHITECTURE.md`, to the boot-pack generator, to either pack
directory, or to the manifest.** No open-items row created, flipped or discarded. **No register row
opened beyond the two the rulings at §1.2 name.** No finding number allocated. **No admission to the
ledger, and the ledger is not built by this batch.** No document archived, moved or deleted as a file
except the `STATUS.md` entry Task 4 moves under its ruled forward bound. **No dispatch written.**

---

## 7. YOUR REPORT

Write `cc_report_register_reconciliation.md` at the repository root. It carries, in this order: the
start-state measurement against §2, with the command beside each figure and the side you measured;
each task's outcome; the changed passages of Tasks 2, 3 and 4 in full; the population count and
coverage boundary of Task 6; the candidate table of Task 7; the guard rounds of Task 8 with everything
that moved; the registered expectations E0–E8 with the measurement beside each; every assumption of §3
you falsified; and a **declared departures** section naming what you did not read and what you relayed
rather than measured.

**One thing extra, and it is a proposal, not an act.** Today's three rulings are recorded in a file
and in no register. **Propose** register entries for them — the text, a proposed identifier under the
allocation convention, and the group each belongs in — **in your report only. Write none of them.**
Whether they are entered, and under what identifiers, is the user's to rule. This is how the drift
that made this batch necessary gets closed without you allocating on your own authority.
