# CC report — LAND the unit-question ruling record, the §9.0 decision surface, and the register-repair stop report

**Dispatch:** `cc_instruction_second_landing_2026_08_28.md`
**Date the batch ran:** 2026-08-29 — **the dispatch's file name carries 2026-08-28, the day it was
written; this batch executed the day after.** Stated here because two dated fields in the record
follow from it (§6.1) and because a reader meeting the file name would otherwise take the two dates
for one.
**Outcome:** Task 0, Task 1 and Task 2 performed. Nothing stopped. Two declared departures and one
finding the previous batch's enumeration could not have reached are below, and none was absorbed
silently.

---

## 1. What this batch was, and what it was not

It is a **backup act**. It lands three untracked root-level documents and the dispatch itself, and
closes. **It repairs nothing, designs nothing, derives nothing, binds nothing and prepends
nothing.** It moves the framework phase not at all — see §11.

**Every standing bar of the dispatch held.** No `src/` change; no test changed, moved or run; no
golden; no build; nothing under `tools/corpus/` or `tools/robust_stop/`; no measurement of the
analysis; no design; no repair; no derivation of any specification statement; **no session booted**;
no document archived or moved AS A FILE; no open-items row created, flipped or discarded; no finding
number allocated; no decisions-register entry written and no `D-NNN` allocated; no edit to any
governing document, any register entry or any register source. **No landed file's content was
edited** — every landed path is committed exactly as it stood on disk, proven blob-to-blob at §4.1.
No handoff entry rides this batch and `cowork_handoff.md` was not written to. The only tool source
touched is `tools/audit/gen_status_batch_bound.py`'s per-batch re-aiming, which the dispatch excepts
by name under Ruling 5 of `cowork_rulings_2026_08_26_amendment_landing_sitting.md`. None of the
three sealed placement-sample files was opened, in any portion; neither pack directory's contents
was opened; `ARCHITECTURE.md` was not opened; `cowork_framework_document_draft_2026_08_28.md` was
not opened. The parked register dispatch was neither run, revalidated nor edited, and the §8 move
was not performed.

**The three landed documents were not opened for content either.** They are committed as they stand,
which is what the dispatch orders; nothing in this report characterises what any of them says.

---

## 2. Method, declared

Working-tree content was read with the file tools throughout (**D-253**). Shell use was confined to
read-only git object queries by explicit hash, the writes the dispatch orders, and the sanctioned
`tools/audit/` scripts. Every shell command carried `; echo "exit:$?"`, and every command whose
output could be large was redirected to a file outside the repository and read separately with the
file tools.

**Two shell commands were denied by the armed guard and neither was routed around.** The first was a
`python -c` code string carrying a literal repository path, aimed at reading the derived gating
answer — re-taken through `Grep`/`Read`. The second was a `wc -l` on a scratchpad file whose path
came from an unexpanded shell variable, which the guard's DENY-ON-INDETERMINATE policy refused —
re-taken through the file tools rather than re-issued. **The denials are recorded rather than merely
obeyed**; both are the guard's own standing clause working as written.

**Every read of the instruction after Task 0 was taken from its git object**, extracted into the
session scratchpad outside the repository, never from the working tree.

---

## 3. Task 0 — pin, then establish

### 3.1 The pin

| what | blob |
|---|---|
| `cc_instruction_second_landing_2026_08_28.md` (the dispatch), pinned at Task 0 | `67b74738d8de1ecfa9fbf9754e545d9835696e52` |

Written with `git hash-object -w`; every later read taken from `git cat-file blob 67b74738…` into a
scratch file outside the repository, and the extracted content compared against the working-tree
read that preceded it.

**★ DECLARED DEPARTURE (1) — THE DISPATCH WAS READ FROM THE WORKING TREE BEFORE IT WAS PINNED.** The
user's opening instruction named this file and directed that it be read and followed; it did not
carry the suggested pin-first wording the dispatch's own head proposes. The dispatch provides for
exactly this: *"Where the session has instead read this file from the working tree first, that is
DECLARED, not a STOP: pin it at Task 0 and prove at Task 1 that the blob has not moved."* **Both
halves were performed.** The proof is at §4.1: the blob pinned at Task 0 and the blob pinned
immediately before staging in Task 1 are the same value, and that same value stands at the commit
object. **The instruction did not move under this batch, and the writing side's declared restraint
held.**

*For the record, on the dispatch's own finding 4:* the head's remedy — putting the pin instruction
into the user's opening message — remains the only construction under which "pin before reading" is
performable, and it was not used this time. The declared-departure route the head supplies is what
made the order dischargeable anyway, and it worked.

### 3.2 The tip, established at the object

| what | value |
|---|---|
| `HEAD` at the start | `c1b755f4037707314dbfca2b74916782a2c1dec0` |
| `master` at the start | `c1b755f4037707314dbfca2b74916782a2c1dec0` |
| `origin/master` at the start | `c1b755f4037707314dbfca2b74916782a2c1dec0` |
| its parent | `39d0b91134178f1d9c4fdfe417532868caf2b716` |

All three refs identical; the previous batch's push had landed. The object was confirmed to be of
type `commit`, and its subject read at the object is *"the report SHA table completed: the close
commit and the end-state commit named, and the fourth commit declared at the departures section"* —
**so the tip is the previous batch's own declared fourth commit, whose parent is the end-state
commit that report names.** That is exactly what the dispatch's premise ledger predicts without
stating a value, and **no git-object value was taken from the dispatch, which deliberately states
none.**

### 3.3 The full guard set, CHECK mode, before the first act

`python tools/audit/gen_guard_state.py --check`, exit **1**. Its summary line reports **75 guards
run, 4 failing, 4 not run, 16 historical records**, and its first line reads *"STALE vs the run:
guard_state.json does not re-derive"*.

The four failing:

- `tools/audit/gen_filing_convention_application.py --check`
- `tools/audit/decisions/apply_soft_discard.py --check`
- `tools/audit/decisions/apply_residue_discard.py --check`
- `tools/audit/gen_evidence_pin_membership.py --check`

**No other check failed, and a search of the whole run output for `STOP` returns none.**

**★ THE NON-ZERO EXIT IS THE DECLARED START STATE ITSELF, NOT A SECOND FINDING, and it is stated
because the previous batch's start run exited 0.** `--check` compares the live run against the
committed `tools/audit/guard_state.json`, which records three failing; the live run measures four,
because the membership check went red after that artifact was last written. **The staleness IS the
fourth red**, arriving by the mechanism A2 names. Nothing else in the run differs.

### 3.4 The tree, enumerated

`python tools/audit/changed_paths.py` — **837 records, every one of them untracked (`??`). There is
no tracked modification of any kind, and therefore no third one, no second and no first.** Producer:
that tool; the pattern that separated the classes is `^\?\?\t` over its output, read with `Grep`.

**E0 is MET:** the dispatch blob reported (§3.1); the tip and `origin/master` established at the
object (§3.2); A1 and A2 graded from measurement (§8).

---

## 4. Task 1 — the landing

### 4.1 The four paths, blob-identical before staging and at the commit object

**Every path item 1 names was confirmed PRESENT and UNTRACKED at Task 0's enumeration before it was
staged. None was absent and none was already tracked, so no STOP fired.** Each was pinned to a blob
before staging and each blob was re-established at the commit object afterwards — **the two lists
are identical, so no landed file carries an edit of its content by this batch.**

| path | blob (pinned before staging, and at the commit object) |
|---|---|
| `cowork_rulings_2026_08_28_unit_question_sitting.md` | `60aa72f3f6a813a44218924d168ed1eef4f2402d` |
| `cowork_unit_question_surface_2026_08_28.md` | `c1f26025dbe7c84f5e2374e606c74600a313eb6c` |
| `cc_report_register_baseline_repair.md` | `ddaa68be6a0f28b0c2836d3786aa7cac91d51202` |
| `cc_instruction_second_landing_2026_08_28.md` (this dispatch) | `67b74738d8de1ecfa9fbf9754e545d9835696e52` |

**The last row is the proof departure (1) owes:** `67b74738…` is the value pinned at Task 0, the
value pinned immediately before staging, and the value at the commit object. Three readings, one
value.

The staged enumeration reported exactly **four** records and nothing else
(`python tools/audit/changed_paths.py --staged`), and the same four are what the commit touched
(`--commit 9735d8e939…`), each as an addition.

### 4.2 The evidence-pin membership artifact, MEASURED before it was accepted

| what | blob |
|---|---|
| the committed object at the start tip `c1b755f403…` | `565611d4fe6276a495805e6ba1998d98b785600d` |
| the file on disk before regeneration | `565611d4fe6276a495805e6ba1998d98b785600d` |
| the file after regeneration | `568c1bf0063d75256571c8d66486a3a835332a83` |

`git diff --numstat 565611d4fe… 568c1bf006…` → **`2  1`**, and the unified difference at `-U1` is
**two hunks and no third**:

- `ruling_records_read` incremented by one;
- `cowork_rulings_2026_08_28_unit_question_sitting.md` inserted into the list of ruling records read.

**`members` did not move**, and no pin, no route, no tool and no verdict moved. **The movement is
exactly the one new ruling record entering the membership, which is what the dispatch predicts.
Nothing beyond this batch's own landed paths appears in it, and nothing was absorbed unexamined.**

**★ THE PREDICTION WAS CHECKED AT EVERY ROUTE THE DERIVATION REACHES ITS INPUTS BY, which the
standing clause requires and which finding F75 exists for.** That derivation reaches its inputs by
two routes — the population of root-level `cowork_rulings_*.md` records, and a scan of a ruling
record's whole text for a measurement tool the record names as fixed to a commit. **The predicted
route produced both hunks; the second route produced none**, and the `-U1` difference is the
evidence that there is no third hunk to attribute to it.

`python tools/audit/gen_evidence_pin_membership.py --check` — **PASS**, exit 0.

### 4.3 The commit and the push

| what | value |
|---|---|
| commit | `9735d8e9398b137a61ec0a20f34d994f9f61a0e1` |
| parent | `c1b755f4037707314dbfca2b74916782a2c1dec0` |
| `origin/master` after the push | `9735d8e9398b137a61ec0a20f34d994f9f61a0e1` |

Subject, verified at the object with `git log -1 --format='%s'`:

> `record: land the unit-question ruling and its decision surface, and the register-repair stop report`

`origin/master` was re-read after a `git fetch`, and the push output names the same movement
(`c1b755f403..9735d8e939  master -> master`).

**★ THE REGENERATED MEMBERSHIP ARTIFACT DID NOT RIDE THIS COMMIT, AND THE READING IS DECLARED
RATHER THAN ASSUMED.** E1 says in terms *"no path outside item 1 committed by Task 1"*, while item 3
of the same task orders the artifact regenerated and A3 lists it in the footprint **without
assigning it to a task**. Committing it in Task 1 would leave E1's own clause unmet; holding it to
the close leaves both satisfied — E1 literally, and A3 because the artifact is in its list whichever
commit carries it. **It therefore rides the Task 2 close commit** (§6.2). *Why this is a reading and
not a resolution in the dispatch's favour:* the reading chosen is the one that breaks no clause of
the dispatch at all, and the alternative would have broken a stated acceptance criterion in order to
satisfy an assumption that does not name a task.

**E1 is MET:** every path of item 1 committed exactly as it stood, blob-identical before staging and
at the commit object (§4.1); no path outside item 1 committed by Task 1 (§4.1, the staged and
commit enumerations); the membership check passing (§4.2); `origin/master` at the commit (above).

---

## 5. Item 2 — what was found, in full

### 5.1 The population, by pattern

At Task 0's enumeration the repository root carried **289** untracked files matching the dispatch's
three patterns. Item 1 names four of them. **The other 285 are reported and NOT landed**, and are
reported by pattern and count only, as ordered — they are not re-listed here, the previous report
having enumerated them by name.

| pattern, root-level, untracked, at Task 0 | records |
|---|---|
| `cc_instruction_*.md` | 286 |
| `cc_report_*.md` | 1 |
| `cowork_*.md` | 2 |
| **total** | **289** |

Producer: `python tools/audit/changed_paths.py`, filtered with `Grep` over its captured output by
`^\?\?\t<pattern>[^/]*\.md\r?$`. **No generated artifact exists for this quantity and the dispatch
orders the figure in the report, so each figure is published with the producer that made it rather
than by citation to an artifact** — D-431's own stated reason is met, the figures being reproducible
from the tool and pattern named beside them, and the character-figure clause's demand that a
published figure name its producer is met in the same sentence.

**The four item-1 paths account for all three patterns' non-historical members**: the two `cowork_*`
records are the ruling record and its decision surface; the one `cc_report_*` record is the previous
CC session's stop report; and one of the 286 `cc_instruction_*` records is this dispatch. **The
residue is therefore 285, all of them `cc_instruction_*.md`** — the same historical dispatch-file
population the previous report enumerated by name at its §5.4, unchanged in size. Nothing outside
the three patterns was landed by this batch at all.

`cc_report_second_landing_2026_08_28.md` did not exist at Task 0 and is committed by Task 2, which
item 2's own carve-out names and which is therefore not a breach of it.

### 5.2 ★ A CLASS OF ROOT-LEVEL UNTRACKED DOCUMENTS THE PREVIOUS ENUMERATION COULD NOT REACH

At Task 0 the repository root carried **449** untracked records in total, of which **447** are
`cc_*.md` and **2** are `cowork_*.md`. Of the 447, **287** match `cc_instruction_*` or `cc_report_*`.
**The remaining 160 root-level untracked `cc_*.md` files match NONE of the dispatch's three
patterns** — names of the shape `cc_<subject>_report.md`, `cc_<subject>_investigation.md`,
`cc_<subject>_dossier.md`, which do not begin `cc_report_`.

Producer: the same tool and the same `Grep` patterns as §5.1; the 160 is the difference of two
measured counts, 447 and 287, both stated above.

**Why this is surfaced rather than left in the enumeration.** The previous report's §5.4 states a
finding about the root's **mixed** dispatch-file population — some tracked, some never committed,
with nothing in the record saying which state is intended — and derives it from a population scoped
to three patterns. **That scope does not reach this class**, so the finding is true and its stated
extent is narrower than the tree. **This is not a correction of that report**, whose enumeration was
correct within the scope its dispatch set; it is the same finding measured at a wider boundary, and
it makes the open user question larger than it looked.

**Acted on in no way.** Not landed, not rowed, not investigated, not measured beyond the two counts
above. **The dispatch forbids creating an open-items row, and what state the root's untracked
document population should be in is a user question, not a session's.**

### 5.3 The two findings the previous report left owed — both discharged by this batch

- **`cc_report_register_baseline_repair.md`** — the previous CC session's stop report on the parked
  register dispatch, which the previous batch was ordered not to land. **Landed** (§4.1).
- **`cowork_unit_question_surface_2026_08_28.md`** — the §9.0 decision surface that appeared on disk
  mid-batch and which the previous batch reported and did not land. **Landed** (§4.1).

Both were in git nowhere and pushed nowhere until this batch. **They are now on `origin/master`.**

### 5.4 What appeared or moved while this batch ran

**Nothing.** The enumeration taken at the close differs from Task 0's only by the four paths this
batch landed and the six tracked modifications its own close acts write (§8, A3). **No third party
created a file under this batch**, which is the shape the previous batch had to grade.

---

## 6. Task 2 — the close

### 6.1 The three `STATUS.md` pointer entries

One per task, written under the OI-222 pointer convention, with no count, no identity and no
rendered value restated (**D-431**). The newest names the dispatch; the two below it say *Same
dispatch*, which is what the forward bound's own derivation reads.

**They are dated 2026-08-29**, the day the acts they record were performed, not the day the dispatch
was written. The same choice was made for the forward bound's `ACT_DATE`, whose value goes into the
archive header sentence *"RULING 4's FORWARD BOUND, <date>"* — a header carrying the dispatch's date
would state something false about when the move ran. **The date field is a fourth authored field
beside the three aiming inputs, and the change is declared at the constant itself** so a later reader
does not take it for one of the three.

### 6.2 The forward bound, applied

`python tools/audit/gen_status_batch_bound.py --apply`, exit **0**. The previous batch's **three**
entries moved verbatim to `STATUS_ARCHIVE.md`; the tool's own reconciliation reports each
**byte-present in the archive exactly once: True** and **absent from the must-read: True**.

The re-aiming moved exactly the three inputs the tool's own comment permits — the base commit
(`9735d8e9398b137a61ec0a20f34d994f9f61a0e1`, this batch's Task 1 commit, pushed before the close
began), the then-previous batch (`cc_instruction_landing_2026_08_28.md`) and the executing act
(`cc_instruction_second_landing_2026_08_28.md`) — plus the declared date field of §6.1. **The
outgoing aiming was APPENDED to `PREVIOUS_AIMINGS` rather than replacing anything (#12).** The one
declared textual adjustment fired as designed: the previous batch's newest entry carried the
`Last updated: ` prefix at the base commit, this batch's entries were written above it, and the
prefix moved to the newest of those — no second adjustment was needed, which the tool's occurrence
test would have stopped on.

### 6.3 The rest of the close

- `python tools/audit/gen_session_start_read_size.py` regenerated; no figure from it is restated
  here (**D-431**).
- `tools/audit/evidence_pin_membership.json` rides this commit, for the reason declared at §4.3.
- This report.

---

## 7. Every SHA this batch produced or resolved

| what | value |
|---|---|
| tip at the start, `HEAD` = `master` = `origin/master` | `c1b755f4037707314dbfca2b74916782a2c1dec0` |
| its parent — the previous batch's end-state commit | `39d0b91134178f1d9c4fdfe417532868caf2b716` |
| Task 1 commit — the landing | `9735d8e9398b137a61ec0a20f34d994f9f61a0e1` |
| Task 2 commit — the close | `b8dc957257788d64a2ecbc58cf05c045ddd048fb` |
| the end-state commit | `121bf4303ac23c98e245d9b31c58b3046403f7aa` |
| the §7 completion commit — **the further commit, declared at §9.3** | `b25d71e6c7202fb5461571a309d3369ade00aa02` |
| the §12 correction commit — **declared at §9.4** | `b0f1d8e25c8886870fbee6df438a2606f91ac67d` |
| the commit that completed this table — **declared at §9.4** | *its own identity cannot stand inside itself; it is the commit whose parent is `b0f1d8e25c…`, and it is the last commit of this batch* |
| dispatch blob, pinned at Task 0, unmoved before staging and at the commit object | `67b74738d8de1ecfa9fbf9754e545d9835696e52` |
| `cowork_rulings_2026_08_28_unit_question_sitting.md` | `60aa72f3f6a813a44218924d168ed1eef4f2402d` |
| `cowork_unit_question_surface_2026_08_28.md` | `c1f26025dbe7c84f5e2374e606c74600a313eb6c` |
| `cc_report_register_baseline_repair.md` | `ddaa68be6a0f28b0c2836d3786aa7cac91d51202` |
| `tools/audit/evidence_pin_membership.json` — the committed object at the start | `565611d4fe6276a495805e6ba1998d98b785600d` |
| `tools/audit/evidence_pin_membership.json` — after regeneration | `568c1bf0063d75256571c8d66486a3a835332a83` |

---

## 8. The assumptions, graded from measurement

### A1 — the working tree by shape — **HELD, with limb 1 stronger than declared**

- **Limb 1 — HELD.** A1 expects no tracked modification outside `STATUS.md` and the artifacts Task 2
  regenerates, and makes any tracked modification found at Task 0 a STOP-and-report. **Task 0's
  enumeration found NO tracked modification at all** — every one of its 837 records is untracked —
  so the STOP could not fire and the tree is cleaner than the assumption allows for. **The mechanism
  is established rather than guessed:** the previous batch landed both of the tracked modifications
  its own A1 declared, and its close commits carried everything it wrote.
- **Limb 2 — HELD.** The untracked root-level population contains the three files this batch lands,
  this dispatch, and the historical dispatch-file population the previous report enumerated (§5.1).
  **It also contains a class that population does not reach (§5.2)**, which is an addition to what
  limb 2 describes rather than a contradiction of it — limb 2's own word is *includes*.
- **Limb 3 — MET.** The enumeration was taken and reported before anything was staged.

### A2 — the guard state at the start — **HELD ON BOTH LIMBS**

- **HELD:** the three known failing checks failed, each for its own recorded cause.
- **HELD:** `gen_evidence_pin_membership.py --check` came back **RED**, by exactly the mechanism the
  dispatch names — the derivation's population is the FILE SYSTEM, this batch's own untracked input
  `cowork_rulings_2026_08_28_unit_question_sitting.md` is a root-level `cowork_rulings_*.md` record,
  and it entered that population after the artifact was last regenerated. **The verdict was measured,
  and neither the dispatch's statement nor the eightieth entry's contrary one was carried.**
- **The fifth-failing-verdict STOP did not fire.** Four failing, no fifth, zero STOPs.

*This is the declared-start-state clause working:* the dispatch stated the red its own input causes,
named the cause, and ordered it measured rather than assumed. Both halves came back as declared.

### A3 — the footprint — **HELD**

The measured working-tree movement across the whole batch is exactly the dispatch's own list:

`cowork_rulings_2026_08_28_unit_question_sitting.md` · `cowork_unit_question_surface_2026_08_28.md` ·
`cc_report_register_baseline_repair.md` · `cc_instruction_second_landing_2026_08_28.md` (the four
landed) · `tools/audit/evidence_pin_membership.json` (regenerated) · `STATUS.md` ·
`STATUS_ARCHIVE.md` · `tools/audit/status_batch_bound.json` ·
`tools/audit/gen_status_batch_bound.py` (**the named carve-out**) ·
`tools/audit/session_start_read_size.json` · this report · and `tools/audit/guard_state.json` at the
end-state commit.

The enumeration taken immediately before the close commit reported **exactly six tracked
modifications** — `STATUS.md`, `STATUS_ARCHIVE.md`, `tools/audit/evidence_pin_membership.json`,
`tools/audit/gen_status_batch_bound.py`, `tools/audit/session_start_read_size.json`,
`tools/audit/status_batch_bound.json` — **every one of them a member of A3's list, and no seventh.**
Its untracked count is Task 0's less the four paths landed, which reconciles exactly.

**No path outside A3's list moved, by this batch's orders or otherwise.** No STOP was owed.

---

## 9. Declared departures

1. **The dispatch was read from the working tree before it was pinned** — §3.1. The dispatch
   provides for this explicitly and orders it declared rather than stopped on; the exposure is
   closed by measurement, the blob being the same value at the Task 0 pin, at the pre-staging pin
   and at the commit object.
2. **The regenerated membership artifact rides the Task 2 close commit rather than the Task 1
   commit** — §4.3. Declared with its reasoning, which is that this is the only reading under which
   no clause of the dispatch goes unmet.
3. **★ A FURTHER COMMIT WAS TAKEN, AS THE DISPATCH'S TASK 2 ITEM 4 PROVIDES.** The close commit's
   identity and the end-state commit's identity cannot stand inside a report those commits carry.
   Item 4 orders exactly this remedy — *"fill them by one further commit that changes nothing else,
   as the previous batch did and declared"* — and the further commit fills those two cells of §7 and
   changes nothing else. **It re-runs no guard, moves no measured value, edits no other section and
   touches no file but this report. The end-state guard artifact is untouched and remains the
   artifact of the run that produced it** — §12's claim is about the tree the guard ran at, and this
   commit changes nothing the guard set reads.

4. **★ A FIFTH COMMIT WAS TAKEN TO CORRECT A FALSE SENTENCE THIS REPORT MADE ABOUT ITSELF** — §12's
   account of what moved at the end-state commit. Item 4 provides for ONE further commit, and this
   is a second one. *Why it was taken rather than left:* the sentence stated the enumeration's
   result as though it were the commit's contents, and the two differ because writing §12 moved the
   report after the enumeration was taken. **Leaving it would ship a statement that is false at
   HEAD, in the very file whose job is to report what this batch did**, which is the shape the
   licence-and-falsity clause names — correct it and report the widening in the same act. The
   correction touches no file but this report, changes no measured value, re-runs no guard, and
   preserves the former wording in place (**#12**). **It does not make the commit-count clause
   wider for any future batch**; the narrow-letter default is unchanged.

   **A SIXTH AND FINAL COMMIT CLOSES THE SAME DEPARTURE**, and it is named here rather than given a
   §9.5 because it corrects the consequence of the fifth rather than a new thing. The fifth commit
   left §7's stated scope — *every SHA this batch produced or resolved* — missing its own identity,
   which is a completeness claim the table did not meet. The sixth fills the fourth and fifth
   commits' cells and **closes the regress at the same place the record already closes it**: the
   last commit of a batch is described by its parent, because no commit can name itself inside a
   file it carries. **It touches no file but this report, re-runs no guard and moves no measured
   value**, and it is the last commit of this batch.

**No other departure.** In particular: no bar of the dispatch was widened, no landed file's content
was edited, no register or governing document was touched, and no open-items row was created for any
of the findings below — the dispatch forbids creating one.

---

## 10. Findings surfaced, none acted on

1. **The root's untracked document population is larger than the three patterns reach** — 160
   root-level untracked `cc_*.md` files match none of them (§5.2). The previous report's mixed-
   population finding is true and its stated extent is narrower than the tree. **A user question,
   not a session's**; nothing in the record says which state is intended.
2. **The root's dispatch-file population remains mixed** — some tracked, some never committed
   (§5.1), carried forward unchanged from the previous report.
3. **The pin order remains unperformable as written** where the user's opening instruction names
   only the dispatch file (§3.1). The dispatch's declared-departure route made it dischargeable, and
   the head's suggested opening instruction is still the only construction that would make it
   performable directly.

**None of these was rowed, investigated, measured beyond the counts stated, or fixed**, as ordered.

---

## 11. The plan lines

**★ THIS BATCH CLOSES NOTHING AND MOVES THE FRAMEWORK PHASE NOT AT ALL.** It is a backup act. The
phase's postcondition is a **RATIFIED** framework, held until the user's external research list
arrives and is dispositioned against the decomposition — **so the critical path runs through the
user and through no session.**

The state as it stands:

- **§9.0 IS RULED** — a unit is a decision the analysis makes about the music. The ruling record and
  the decision surface it was ruled on are what Task 1 lands, and **the layer-ownership question
  (Δ2) is thereby gradable and is NOT decided.**

Owed, and NOT done:

- **The placement test** — carrying the record's **twice-stated** condition that a session with a
  shell precede reliance on its results, **which is still unanswered.**
- **The phase's retrospective** — §3.9 of the phase-definition surface. It must land before the next
  phase opens **and it does not exist.**
- **Everything the eightieth entry's backlog carries**, including the **eleven quarantined audit
  questions**, which belong to the AUDIT by the user's ruling of 2026-08-15 and **must not be worked
  before it**; and the mixed root-level dispatch-file population, on which **nothing in the record
  says which state is intended — a user question, not a session's**, now measured at a wider
  boundary than the previous report could reach (§5.2).

---

## 12. The end state

*(This section was deliberately EMPTY at the close commit and is written here, at the end-state
commit. E2 requires a fresh full guard run at the tree the close leaves, and
`tools/audit/guard_state.json` committed only after the run that produced it — so that run cannot
have happened when the close commit is taken, and asserting its result there would have been a
statement the record makes about itself that is not yet true. The close commit's own §12 says
exactly that and nothing more.)*

**A fresh FULL guard run was performed at the tree the close left**, in write mode, and
`tools/audit/guard_state.json` is committed as the artifact of that run and of no other — **the run
came first and the commit second.**

`python tools/audit/gen_guard_state.py`, exit **0**. Its summary line reports **75 guards run, 3
failing, 4 not run, 16 historical records**, and the artifact's own `summary` block reads **run 75,
passing 72, failing 3**. The three failing are **the three known and no others**:

- `tools/audit/gen_filing_convention_application.py --check`
- `tools/audit/decisions/apply_soft_discard.py --check`
- `tools/audit/decisions/apply_residue_discard.py --check`

**ZERO STOPs** — a search of the whole run output for `STOP` returns none.

**★ THE FOURTH RED IS GONE, AND THAT IS THIS BATCH'S OWN ORDERED ACT RATHER THAN A DRIFT.**
`gen_evidence_pin_membership.py --check` failed at the start (§3.3) and passes at the end, because
Task 1 regenerated that artifact over the population the new ruling record had already joined (§4.2).
**No check that passed at the start failed at the end, and no new failure appeared.**

**The enumeration taken immediately after the run, and before this section was written, reported
`tools/audit/guard_state.json` as the ONE tracked modification and no second**, with the untracked
count unchanged from the close (`python tools/audit/changed_paths.py`). **This section was then
written, so the end-state commit carries two paths — that artifact and this report — and both are
members of A3's list. A3 holds through the end state.**

*★ CORRECTED IN A FIFTH COMMIT, AND THE CORRECTION IS DECLARED RATHER THAN MADE QUIETLY (§9.4).* The
sentence above first read *"The only path that moved between the close commit and this one is
`tools/audit/guard_state.json`"*. That was the enumeration's own result and it was true of the
moment it was taken; it was **not** true of the commit that then carried it, because writing this
section moved the report as well. The former wording stands here (**#12**), and what replaces it
states both the measurement and what happened after it.

**E2 is MET.**

---

## 13. Self-check over this batch's own diff

Performed by re-reading the actual working-tree movement and the commit objects, not the memory of
making them.

1. **Principles touched.** **#12** — nothing was deleted and nothing rewritten; every landed path is
   committed as it stands, the forward bound's outgoing aiming was appended rather than replaced,
   and the previous batch's `STATUS.md` entries were moved verbatim with the tool's own byte
   reconciliation rather than retyped. **#6** — each landed document has one home and this batch adds
   no second one. **#15** — every claim about a commit or a blob in this report is verified at the
   object by explicit hash, never at an assertion; the four landed paths are checked at three
   readings each. **#17f / D-431** — no figure is transcribed from the dispatch, which states none;
   the figures this report publishes that have no generated artifact are ordered by the dispatch and
   are published with the tool and the pattern that produced them, stated at each site. **#13** —
   the wider untracked class at §5.2 is surfaced as a finding rather than absorbed into the
   enumeration. **#19** — nothing is claimed established that was not measured; A2's second limb is
   reported with the mechanism that explains it, and A1's limb 1 is graded as measured rather than
   as declared. **#10** — the act date is stated as the day the batch ran rather than the day the
   dispatch was written, at both sites where a date enters the record.
2. **Conventions.** American English. No self-invented label, abbreviation or numbering scheme —
   every identifier used is one the record already carries. **No music-theory word arises in this
   batch's subject matter in a non-musical sense**: *score* does not appear in its numerical sense,
   *key* does not appear at all, *measure* appears only as the verb and as *measurement*, and *root*
   appears only in the record's own compound *root-level*, naming the repository's top directory.
3. **Figures and premises.** Every premise the dispatch stated was re-established at the object or at
   the file before it was relied on: the tip and its parent, the tree shape, the guard state, the
   present-and-untracked status of each of the four paths, and the membership artifact's committed
   blob. **No premise was carried from the dispatch's word, and the dispatch asserts no git-object
   value to carry.**
4. **File-tools rule (D-253).** Working-tree content was read with `Read` / `Grep` / `Glob`
   throughout. Shell use was read-only git object queries by explicit hash, the writes the dispatch
   orders, and the sanctioned `tools/audit/` scripts. **The guard denied two commands and neither was
   routed around** — each was re-taken through the file tools; §2 records them.
5. **Uncertainty on any comparison.** The comparisons this report asserts — the four blob identities
   and the membership artifact's difference — are byte-exact object-to-object measurements, not
   estimates, so **#24** is not engaged. The one derived quantity, the 160 at §5.2, is the exact
   difference of two exact counts and carries no sampling error. No difference between two estimated
   quantities is asserted anywhere.
