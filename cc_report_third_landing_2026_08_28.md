# CC report — LAND the external research workbook

**Dispatch:** `cc_instruction_third_landing_2026_08_28.md`
**Date the batch ran:** 2026-08-30 — **the dispatch's file name carries 2026-08-28, the day it was
written; this batch executed two days after.** Stated here because two dated fields in the record
follow from it (§6.1) and because a reader meeting the file name would otherwise take the two dates
for one.
**Outcome:** Task 0, Task 1 and Task 2 performed; the landing is committed and pushed. **E2 IS NOT
MET, and this report is a STOP-AND-REPORT: the end-state guard run turned up a FIFTH failing verdict
— a genuine STOP — caused by this batch's own ordered landing, whose remedy is a mechanism change
reserved to the user (§12.1).** One contradiction inside the dispatch is also SURFACED and not
resolved in the dispatch's favour (§9.2). Four declared departures and four findings are below, and
none was absorbed silently.

---

## 1. What this batch was, and what it was not

It is a **backup and custody act**. It lands one binary file — the external research workbook the
user prepared, which the framework document's §1.4 ratification hold waits on — and the dispatch
itself, and closes. **It reads nothing of the workbook, repairs nothing, designs nothing, derives
nothing, binds nothing and prepends nothing.** It moves the framework phase not at all — see §11.

**Every standing bar of the dispatch held.** No `src/` change; no test changed, moved or run; no
golden; no build; nothing under `tools/corpus/` or `tools/robust_stop/`; no measurement of the
analysis; no design; no repair; no derivation of any specification statement; **no session booted**;
no document archived or moved AS A FILE; no open-items row created, flipped or discarded; no finding
number allocated; no decisions-register entry written and no `D-NNN` allocated; no edit to any
governing document, any register entry or any register source. **No landed file's content was
edited** — both landed paths are committed exactly as they stood on disk, proven blob-to-blob at
§4.1. No handoff entry rides this batch and `cowork_handoff.md` was not written to. The only tool
source touched is `tools/audit/gen_status_batch_bound.py`'s per-batch re-aiming, which the dispatch
excepts by name under Ruling 5 of `cowork_rulings_2026_08_26_amendment_landing_sitting.md`. No
sealed placement-sample file was opened, in any portion; `ARCHITECTURE.md` was not opened;
`cowork_framework_document_draft_2026_08_28.md` was not opened. The parked register dispatch was
neither run, revalidated nor edited, and the §8 move was not performed.

**★ THE WORKBOOK WAS NOT OPENED, IN ANY PORTION.** It was staged and hashed, which the dispatch
states in terms is not opening it. Its content was not read, converted, extracted or characterised;
nothing in this report says what it contains; and **the containing folder was not renamed** — its
spelling is the user's and stands as it is. Every one of those is an ordered bar and each held.

---

## 2. Method, declared

Working-tree content was read with the file tools throughout (**D-253**). Shell use was confined to
read-only git object queries by explicit hash, the writes the dispatch orders, and the sanctioned
`tools/audit/` scripts. Every shell command carried `; echo "exit:$?"`, and every command whose
output could be large was redirected to a file outside the repository and read separately with the
file tools.

**One shell command was denied by the armed guard and it was not routed around.** A `grep` over a
scratchpad file carried, as its pattern, a token that reads as a repository path; the guard's
DENY-ON-INDETERMINATE policy refused it. It was re-taken through `Grep` against the same scratchpad
file rather than re-issued in another spelling. **The denial is recorded rather than merely obeyed**,
and it is the guard's own standing clause working as written.

**Every read of the instruction after Task 0 was taken from its git object**, extracted into the
session scratchpad outside the repository, never from the working tree.

---

## 3. Task 0 — pin, then establish

### 3.1 The two pins

| what | blob |
|---|---|
| `cc_instruction_third_landing_2026_08_28.md` (the dispatch), pinned at Task 0 | `bd5a053d6481eac90b67accd0d6171baed95e7c8` |
| `external resarch summary/external research.xlsx` (the workbook), pinned at Task 0 | `9bf55eadb4dbf13fbea30b89077f89646dc10542` |

Both written with `git hash-object -w`. Every later read of the instruction was taken from
`git cat-file -p bd5a053d64…` into a scratch file outside the repository, and the extracted content
was compared against the working-tree read that preceded it and found the same document. **The
workbook's object was created and never read back** — hashing is not opening.

**★ DECLARED DEPARTURE (1) — THE DISPATCH WAS READ FROM THE WORKING TREE BEFORE IT WAS PINNED.** The
user's opening instruction named this file and directed that it be read and followed; it did not
carry the pin-first wording the dispatch's own head suggests. The dispatch provides for exactly
this: *"Where the session read this file from the working tree first, declare it, pin at Task 0, and
prove at Task 1 that the blob has not moved."* **Both halves were performed.** The proof is at §4.1:
the blob pinned at Task 0 is the blob staged in Task 1 and the blob at the commit object. **The
instruction did not move under this batch, and the writing side's declared restraint held.**

### 3.2 The tip, established at the object

| what | value |
|---|---|
| `master` at the start | `6bdf4f3d2024e7257d910f5286d87ae3e4eeb823` |
| `origin/master` at the start | `6bdf4f3d2024e7257d910f5286d87ae3e4eeb823` |

Both refs identical; the previous batch's push had landed. The refs were read as files with the file
tool and the value then confirmed to be of type `commit` at the object; its subject read at the
object is *"the report SHA table completed: the fourth and fifth commits named, and the regress
closed at the last commit as the record closes it"* — **so the tip is the previous batch's own last
commit, the sixth one its report declares.** That is what the dispatch's premise ledger predicts
without stating a value, and **no git-object value was taken from the dispatch, which deliberately
states none.**

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

**★ THE NON-ZERO EXIT IS THE DECLARED START STATE ITSELF AND NOT A SECOND FINDING.** `--check`
compares the live run against the committed `tools/audit/guard_state.json`, which records three
failing; the live run measures four, because the membership check went red after that artifact was
last written. **The staleness IS the fourth red.** Nothing else in the run differs.

### 3.4 ★ THE FOURTH RED, ESTABLISHED AT ITS MECHANISM RATHER THAN CARRIED

`python tools/audit/gen_evidence_pin_membership.py --check`, run on its own, prints *"STALE vs the
derivation: evidence_pin_membership.json does not re-derive"*.

**The cause is established, not named-and-left.** That derivation's population is the FILE SYSTEM —
every root-level `cowork_rulings_*.md`, as the tool's own docstring states. The committed artifact
was regenerated by the previous batch at its own Task 1 and its `stdout` recorded in
`tools/audit/guard_state.json` states how many ruling records it then read. **The root now carries
one more than that**: `cowork_rulings_2026_08_29_ratification_sitting.md`, dated 2026-08-29, present
and **untracked** at Task 0's enumeration and therefore written after the previous batch's last
commit. Producer of the comparison: the committed `guard_state.json` field named above, read with
`Grep`, against `Glob` over the repository root for `cowork_rulings_*.md` and `Grep` over the Task 0
enumeration for the untracked members of that set — **exactly one, the file named above.**

**This is the F67 shape the declared-start-state clause exists for**, arriving from a file **no order
of this batch creates, lands or touches**. A2 names the mechanism in advance and orders the state
measured; it is measured, and the measurement agrees with the mechanism.

**★ AND THE ARTIFACT WAS DELIBERATELY NOT REGENERATED.** The previous batch cleared the same red
because its own dispatch ordered the regeneration and listed the artifact in its footprint. **This
dispatch orders no such act and A3 does not name that path**, so regenerating it would be movement
at a path outside the declared footprint — which A3 makes a STOP-and-report — and would additionally
absorb into this batch a movement another side's file caused, which A3 forbids in terms: *"a movement
no order of this batch caused is reported and graded, never absorbed."* The consequence for E2 is at
§9.2 and §12, stated rather than worked around.

### 3.5 The tree, enumerated

`python tools/audit/changed_paths.py` — **837 records, every one of them untracked (`??`). There is
no tracked modification of any kind, and therefore no third one, no second and no first.** Producer:
that tool; the classes were separated with `Grep` over its captured output, `^\?\?` for the untracked
class and `^ ?[MADRCU]` for the tracked one.

**Both paths Task 1 lands were confirmed present and untracked in that enumeration before anything
was staged** — `cc_instruction_third_landing_2026_08_28.md` as a file, and the workbook as its
containing directory `external resarch summary/`, which is how git reports a wholly-untracked
directory. Neither was absent and neither was already tracked, so no STOP fired.

**E0 is MET:** both blobs reported (§3.1); the tip and `origin/master` established at the object
(§3.2); A1 and A2 graded from measurement (§8).

---

## 4. Task 1 — the landing

### 4.1 The two paths, blob-identical at the pin, at the index and at the commit object

| path | blob (Task 0 pin, staged index entry, and commit object — one value, three readings) |
|---|---|
| `external resarch summary/external research.xlsx` | `9bf55eadb4dbf13fbea30b89077f89646dc10542` |
| `cc_instruction_third_landing_2026_08_28.md` (this dispatch) | `bd5a053d6481eac90b67accd0d6171baed95e7c8` |

The staged index entries were read with `git ls-files -s` after staging and before committing; the
commit-object entries with `git ls-tree -r` against the commit. **The three readings agree for both
paths, so neither landed file carries an edit of its content by this batch** — which for the
workbook is the ordered bar, and for the dispatch is the proof departure (1) owes.

*A note about the workbook and line endings, stated because a reader may wonder:* git reported a
CRLF-normalisation warning for the dispatch (a text file) and none for the workbook. The workbook is
binary and no filter applied to it; its content-addressed identity is the same value at the pin, at
the index and in the commit, which is the whole of what "byte-exactly as it stands" asserts.

### 4.2 What the commit touched — nothing else

`python tools/audit/changed_paths.py --commit 0396bb6a70…` reports **exactly two records, both
additions**, and they are the two paths above. The same is true of the object-level difference
against the parent (`git diff --name-status 6bdf4f3d20… 0396bb6a70…`): two added paths, no third.

### 4.3 The commit and the push

| what | value |
|---|---|
| commit | `0396bb6a70a6ad983ee14c84d85e9201c8f7ef16` |
| parent | `6bdf4f3d2024e7257d910f5286d87ae3e4eeb823` |
| `origin/master` after the push | `0396bb6a70a6ad983ee14c84d85e9201c8f7ef16` |

Subject, verified at the object with `git log -1 --format='%s'`, and identical to the dispatch's
ordered text:

> `record: land the external research workbook — the published-research list the framework ratification hold waits on, at external resarch summary/external research.xlsx`

The push output names the movement (`6bdf4f3d20..0396bb6a70  master -> master`), the local
remote-tracking ref was re-read at the object, and `git ls-remote origin refs/heads/master` returns
the same value **from the remote itself** — two independent readings of where `origin/master` stands.

**E1 is MET:** both paths committed blob-identical to their Task 0 pins (§4.1); nothing else
committed by Task 1 (§4.2); `origin/master` at the commit (above).

---

## 5. Item 3 — what was found, reported and NOT landed

### 5.1 The root-level untracked population, by shape

At Task 0 the repository root carried **449** untracked files, plus the workbook's directory. Their
shape:

| shape, root-level, untracked, at Task 0 | records |
|---|---|
| `cc_*.md` | 446 |
| — of which `cc_instruction_*.md` | 286 |
| — of which `cc_report_*.md` | 0 |
| — the remainder, matching neither | 160 |
| `cowork_*.md` | 3 |
| **total root-level untracked files** | **449** |

Producer: `python tools/audit/changed_paths.py`, filtered with `Grep` over its captured output by
`^\?\?\t<shape>\r?$`. **No generated artifact exists for this quantity and the dispatch orders the
finding reported, so each figure is published with the producer that made it rather than by citation
to an artifact** — D-431's own stated reason is met, the figures being reproducible from the tool and
the pattern named beside them, and the character-figure clause's demand that a published figure name
its producer is met in the same sentence.

**One of the 286 `cc_instruction_*.md` records is this dispatch, and it is landed. The other 448
files are reported and NOT landed**, as ordered. `cc_report_third_landing_2026_08_28.md` did not
exist at Task 0 and is committed by Task 2, which item 3's own carve-out names and which is therefore
not a breach of it.

The 160 that match neither shape are the class the previous report surfaced at its §5.2 — names of
the form `cc_<subject>_report.md`, `cc_<subject>_dossier.md`, `cc_<subject>_investigation.md`, which
do not begin `cc_report_`. **The population is unchanged in size from that report's measurement**,
and this batch acts on it in no way.

### 5.2 ★ THREE COWORK DOCUMENTS DATED 2026-08-29 ARE ON DISK, IN GIT NOWHERE, AND ONE OF THEM IS THE PHASE RETROSPECTIVE THE RECORD CALLS OWED

The three root-level untracked `cowork_*.md` records, named because this is the class the dispatch
orders reported and because two of the three bear on the plan:

- `cowork_framework_phase_retrospective_2026_08_29.md`
- `cowork_research_list_disposition_surface_2026_08_29.md`
- `cowork_rulings_2026_08_29_ratification_sitting.md`

**None was opened.** They are named from the enumeration, and nothing in this report characterises
what any of them says.

**Why this is surfaced rather than left in the enumeration.** The eightieth handover entry and the
previous batch's report both list **the phase's §3.9 retrospective as OWED AND NOT DONE, saying in
terms that it does not exist**. A file whose name states that it is exactly that now stands at the
root. **Whether it is that document, and whether it is complete, is not established here and was not
looked at.** What is established is that **a file so named exists, is untracked, and is therefore in
git nowhere and pushed nowhere** — which is the same unguarded-risk shape the eightieth entry names
as the reason a landing dispatch was owed at all, arriving again one batch later.

**The third is the cause of the fourth guard red** (§3.4), and it is a ruling record from a sitting
the record does not otherwise name to this session.

**Acted on in no way.** Not landed — the dispatch names two paths and item 3 forbids landing
anything else. Not opened, not rowed, not investigated, not measured beyond their existence and their
names. **A landing dispatch for them is a question for the writing side and the user, not a session's
to take.**

### 5.3 What appeared or moved while this batch ran

**Nothing.** The enumeration taken before the close commit differs from Task 0's only by the two
paths this batch landed and the five tracked modifications its own close acts write (§8, A3). **No
third party created a file under this batch.**

---

## 6. Task 2 — the close

### 6.1 The three `STATUS.md` pointer entries

One per task, written under the OI-222 pointer convention, with no count, no identity and no
rendered value restated (**D-431**). The newest names the dispatch; the two below it say *Same
dispatch*, which is what the forward bound's own derivation reads.

**They are dated 2026-08-30**, the day the acts they record were performed, not the day the dispatch
was written. The same choice was made for the forward bound's `ACT_DATE`, whose value goes into the
archive header sentence *"RULING 4's FORWARD BOUND, <date>"* — a header carrying the dispatch's date
would state something false about when the move ran (**#10**). **The date field is a fourth authored
field beside the three aiming inputs, and the change is declared at the constant itself**, whose own
comment sentence naming the run date was corrected in the same edit so that it is true of this
aiming rather than of the previous one.

### 6.2 The forward bound, applied

`python tools/audit/gen_status_batch_bound.py --apply`, exit **0**. The previous batch's **three**
entries moved verbatim to `STATUS_ARCHIVE.md`; the tool's own reconciliation reports each
**byte-present in the archive exactly once: True** and **absent from the must-read: True**.

The re-aiming moved exactly the three inputs the tool's own comment permits — the base commit
(`0396bb6a70a6ad983ee14c84d85e9201c8f7ef16`, this batch's Task 1 commit, pushed before the close
began), the then-previous batch (`cc_instruction_second_landing_2026_08_28.md`) and the executing act
(`cc_instruction_third_landing_2026_08_28.md`) — plus the declared date field of §6.1. **The outgoing
aiming was APPENDED to `PREVIOUS_AIMINGS` rather than replacing anything (#12).** The one declared
textual adjustment fired as designed: the previous batch's newest entry carried the `Last updated: `
prefix at the base commit, this batch's entries were written above it, and the prefix moved to the
newest of those — no second adjustment was needed, which the tool's occurrence test would have
stopped on.

### 6.3 The rest of the close

- `python tools/audit/gen_session_start_read_size.py` regenerated, exit **0**; no figure from it is
  restated here (**D-431**).
- This report.
- **`tools/audit/evidence_pin_membership.json` was NOT regenerated**, for the reason at §3.4. It is
  not among the tracked modifications this batch produced, and the enumeration at §8 proves it.

---

## 7. Every SHA this batch produced or resolved

| what | value |
|---|---|
| tip at the start, `master` = `origin/master` | `6bdf4f3d2024e7257d910f5286d87ae3e4eeb823` |
| Task 1 commit — the landing | `0396bb6a70a6ad983ee14c84d85e9201c8f7ef16` |
| Task 2 commit — the close | *filled by the further commit declared at §9.3* |
| the end-state commit | *filled by the further commit declared at §9.3* |
| dispatch blob, pinned at Task 0, at the staged index and at the commit object | `bd5a053d6481eac90b67accd0d6171baed95e7c8` |
| workbook blob, pinned at Task 0, at the staged index and at the commit object | `9bf55eadb4dbf13fbea30b89077f89646dc10542` |

---

## 8. The assumptions, graded from measurement

### A1 — the working tree by shape — **HELD, with limb 1 stronger than declared**

- **Limb 1 — HELD.** A1 expects no tracked modification outside `STATUS.md` and the artifacts Task 2
  regenerates, and makes any tracked modification found at Task 0 a STOP-and-report. **Task 0's
  enumeration found NO tracked modification at all** — every record untracked — so the STOP could not
  fire and the tree is cleaner than the assumption allows for.
- **Limb 2 — HELD.** The untracked population contains the workbook's folder, this dispatch, and the
  historical dispatch-file population earlier reports enumerated (§5.1). **It also contains three
  `cowork_*.md` documents dated the day after the previous batch closed (§5.2)**, which is an
  addition to what limb 2 describes rather than a contradiction of it — limb 2's own word is
  *includes*.
- **Limb 3 — MET.** The enumeration was taken and reported before anything was staged.

### A2 — the guard state at the start — **HELD ON BOTH LIMBS**

- **HELD:** the three known failing checks failed, each for its own recorded cause.
- **HELD:** `gen_evidence_pin_membership.py --check` came back **RED**, and its state was MEASURED
  rather than carried, exactly as A2 orders. **The difference is explained at its mechanism (§3.4):**
  the derivation's population is the file system, and one root-level `cowork_rulings_*.md` record
  entered it after the artifact was last regenerated. **A2's own prediction is confirmed in the
  direction it was made** — *"which this batch neither adds to nor lands, so no movement caused by
  this batch is expected there"* — the movement is real and is caused by another side's file, not by
  this batch.
- **The fifth-failing-verdict STOP did not fire AT THE START.** Four failing, no fifth, zero STOPs.
  **★ IT FIRED AT THE END STATE**, on a check that was passing at the start: see §12.1. A2's clause
  is written of the start state; it is applied here to the batch as a whole, which is the reading
  that reports more rather than less.

### A3 — the footprint — **HELD**

The measured working-tree movement across the whole batch is exactly the dispatch's own list, less
one member it names that no order of this batch moves:

`external resarch summary/external research.xlsx` · `cc_instruction_third_landing_2026_08_28.md`
(the two landed) · `STATUS.md` · `STATUS_ARCHIVE.md` · `tools/audit/status_batch_bound.json` ·
`tools/audit/gen_status_batch_bound.py` (**the named carve-out**) ·
`tools/audit/session_start_read_size.json` · this report · and `tools/audit/guard_state.json` at the
end-state commit.

The enumeration taken immediately before the close commit reported **exactly five tracked
modifications** — `STATUS.md`, `STATUS_ARCHIVE.md`, `tools/audit/gen_status_batch_bound.py`,
`tools/audit/session_start_read_size.json`, `tools/audit/status_batch_bound.json` — **every one of
them a member of A3's list, and no sixth.** `tools/audit/evidence_pin_membership.json` is
conspicuously absent from that list, which is the evidence that §3.4's refusal was performed rather
than merely stated.

**No path outside A3's list moved, by this batch's orders or otherwise.** No STOP was owed.

---

## 9. Declared departures

### 9.1 The dispatch was read from the working tree before it was pinned

§3.1. The dispatch provides for this explicitly and orders it declared rather than stopped on; the
exposure is closed by measurement, the blob being the same value at the Task 0 pin, at the staged
index and at the commit object.

### 9.2 ★ THE CONTRADICTION INSIDE THE DISPATCH — SURFACED, NOT RESOLVED IN THE DISPATCH'S FAVOUR

**The dispatch's own head orders: *"Read its bars sceptically and STOP on a contradiction rather than
resolving it in this dispatch's favour."* This is that contradiction, and it is reported rather than
worked around.**

- **A2 EXPECTS the membership check's state to be measured and treats a fourth failing verdict as
  within its contemplation** — only a *fifth* is a STOP-and-report.
- **A3 names the footprint and does NOT include `tools/audit/evidence_pin_membership.json`**, and
  makes movement at any other path a STOP-and-report, adding that a movement no order of this batch
  caused is *"reported and graded, never absorbed"*.
- **E2 requires, at the end state, *"the three known failing checks and no others"*.**

**No act this batch is authorized to take satisfies all three.** Regenerating the artifact would meet
E2 and breach A3 twice over — movement at an unnamed path, and absorption of a movement another
side's file caused. Not regenerating meets A2 and A3 and leaves E2's first limb unmet as literally
written.

**What was done, and why.** The artifact was NOT regenerated. **E2 is graded honestly at §12: met on
its second and third limbs, unmet on its first, with the cause established at the mechanism and
attributable to a file outside this batch entirely.** *Why this is a declaration and not a
resolution:* A2 is the clause that speaks to this exact state, in terms, and orders the run *graded*
and any difference *explained at its mechanism* — which is what §3.4 and §12 do. E2's first limb is
the clause that cannot be met, and it is reported unmet rather than made true by an unordered act.
**The user rules; this session does not.**

*What the fix would be, stated so the next dispatch need not rediscover it:* one line in a dispatch
naming `tools/audit/evidence_pin_membership.json` in the footprint and ordering its regeneration —
which is exactly what the previous batch's dispatch carried and this one does not.

### 9.3 A further commit was taken, as Task 2 item 4 provides

The close commit's identity and the end-state commit's identity cannot stand inside a report those
commits carry. Item 4 orders exactly this remedy — *"where the report's SHA table cannot carry its own
committing identities, one further commit fills exactly those cells, as the first landing batch did
and declared"* — and the further commit fills those two cells of §7 and changes nothing else. **It
re-runs no guard, moves no measured value, edits no other section and touches no file but this
report. The end-state guard artifact is untouched and remains the artifact of the run that produced
it** — §12's claim is about the tree the guard ran at, and this commit changes nothing the guard set
reads.

### 9.4 ★ A SECOND FURTHER COMMIT ADDS ONE SENTENCE TO THE `STATUS.md` CLOSE ENTRY

Item 4 provides for ONE further commit and this is a second one, so it is declared rather than taken
quietly. **Why it is taken:** the close commit's `STATUS.md` entries were written before the
end-state guard run existed, so the close entry says nothing about the fifth verdict (§12.1) —
**the batch's most consequential finding, absent from the one surface every session reads at boot.**
The entry as written is not false: its guard sentence is scoped to the START state and is accurate
there. **It is incomplete about the batch, and the pointer convention it is written under makes the
report the home of the evidence — but a STOP left out of the must-read is the shape #13 exists
against.** The commit adds one sentence naming the STOP and pointing at §12.1, **preserves the
existing wording in place (#12), moves no other text, re-runs no guard, touches no file but
`STATUS.md`, and widens no bar for any future batch.**

**No other departure.** In particular: no bar of the dispatch was widened, no landed file's content
was edited, the workbook was not opened, no folder was renamed, no tool source was edited beyond the
forward bound's named carve-out — **the artifact-inventory tool the fifth verdict names was NOT
touched** — no register or governing document was touched, and no open-items row was created for any
of the findings below, the dispatch forbidding one.

---

## 10. Findings surfaced, none acted on

0. **★ THE ARTIFACT INVENTORY HALTS ON THE LANDED WORKBOOK, AND THE GUARD SET IS LEFT WITH A STOP IN
   IT** (§12.1). The tool's authored signature table names no rule for the workbook's shape, and its
   own live stop rule refuses to let a newly tracked file enter a later pass ungraded. **This is a
   STOP-and-report under A2, and it is reported and not acted on:** the remedy is a mechanism change
   the user rules and this batch's bars forbid. **It is the batch's most consequential finding and it
   is listed first.**
1. **★ THREE `cowork_*.md` DOCUMENTS DATED 2026-08-29 STAND UNTRACKED AT THE ROOT, IN GIT NOWHERE AND
   PUSHED NOWHERE — and one of them is named as the phase retrospective the record twice calls owed
   and non-existent** (§5.2). Not opened, not landed, not rowed. **A landing act for them is due, and
   naming one is the writing side's and the user's, not a session's.**
2. **The membership guard is red for a cause outside this batch, and the dispatch that would let a
   session clear it does not order the act** (§3.4, §9.2). **A user question, not a session's.**
3. **The root's untracked document population remains mixed and larger than any dispatch's patterns
   have reached** — 449 root-level untracked files, of which 160 match none of the shapes earlier
   dispatches enumerated by (§5.1). Carried forward unchanged from the previous report; **nothing in
   the record says which state this population is meant to be in.**

**None of these was rowed, investigated, measured beyond the counts stated, or fixed**, as ordered.

---

## 11. The plan lines

**★ THIS BATCH MOVES THE FRAMEWORK PHASE NOT AT ALL.** It is a backup and custody act.

**What it changes upstream of the phase:** the external research list the framework document's §1.4
ratification hold waits on **is now delivered, in git, and pushed** — so **the dispositioning of the
decomposition against it is unblocked on the input side, and is the user's sitting to commission.**
Nothing about the list's content was read, and nothing in this report dispositions it against
anything.

Still owed and NOT done:

- **The placement test** — carrying the record's **twice-stated** condition that a session with a
  shell precede reliance on its results, **which is still unanswered.**
- **The phase's retrospective** — §3.9 of the phase-definition surface, which must land before the
  next phase opens. **A file named as that retrospective now exists untracked at the root (§5.2);
  whether it is that document and whether it is complete was not looked at, and it is in git
  nowhere.**
- **Everything the eightieth handover entry's backlog carries**, including the **eleven quarantined
  audit questions**, which belong to the AUDIT by the user's ruling of 2026-08-15 and **must not be
  worked before it**.

---

## 12. The end state — ★ E2 IS NOT MET, AND A FIFTH FAILING VERDICT IS A STOP-AND-REPORT

*(This section was deliberately EMPTY at the close commit and is written here, at the end-state
commit. E2 requires a fresh full guard run at the tree the close leaves, and
`tools/audit/guard_state.json` committed only after the run that produced it — so that run cannot
have happened when the close commit is taken, and asserting its result there would have been a
statement the record makes about itself that is not yet true.)*

**A fresh FULL guard run was performed at the tree the close left**, in write mode, and
`tools/audit/guard_state.json` is committed as the artifact of that run and of no other — **the run
came first and the commit second.**

`python tools/audit/gen_guard_state.py`, exit **0**. Its summary line reports **75 guards run, 5
failing, 4 not run, 16 historical records**, and the artifact's own `summary` block reads **run 75,
passing 70, failing 5**.

The five failing:

- `tools/audit/gen_filing_convention_application.py --check` — the first known
- `tools/audit/decisions/apply_soft_discard.py --check` — the second known
- `tools/audit/decisions/apply_residue_discard.py --check` — the third known
- `tools/audit/gen_evidence_pin_membership.py --check` — the fourth, carried from the start state
  unchanged and unregenerated (§3.4)
- **`tools/audit/gen_artifact_inventory.py --check` — the FIFTH, NEW, and caused by this batch's own
  ordered act**

### 12.1 ★ THE FIFTH VERDICT, ESTABLISHED AT THE OBJECTS AND NOT ACTED ON

Run on its own, `python tools/audit/gen_artifact_inventory.py --check` exits **2** — a STOP, not a
drift — with this text, which the guard artifact captures verbatim at that tool's entry:

> `STOP: 1 file(s) matched no rule in the signature table — this is the dispatch's own stop rule and prediction P1's refutation condition. First ten: ['external resarch summary/external research.xlsx']`

**The cause is established at the tool's own docstring and needs no inference.** That tool classifies
**every tracked file** by an AUTHORED signature table of path shapes, and its stop rule 4 states the
live half in terms: *"`--check` … separately re-runs the classification at the CURRENT tree and STOPS
if anything there is unclassified. … a file added by a later commit that no rule names must halt this
tool rather than enter a later pass ungraded."* **The workbook was untracked at Task 0, so no rule had
to name it; Task 1 made it tracked, and no rule names it.** That is why this check passed at the start
(§3.3) and STOPS at the end.

**★ THIS IS THE TOOL WORKING, NOT THE LANDING FAILING.** The halt is the designed refusal to let a
newly tracked file enter a later pass ungraded. **The landing is exactly what the dispatch orders and
what the user ruled**, and nothing about it is withdrawn or in doubt.

**NOTHING WAS DONE ABOUT IT, and the refusal is deliberate on three separate grounds.** The remedy is
a new row in that tool's AUTHORED signature table. **(a)** That is a tool-source edit, and this batch's
standing bars permit exactly one — the forward bound's per-batch re-aiming, excepted by name.
**(b)** It is a **mechanism change**: authoring a new judgment for a subject the pass's own cut did
not previously reach is precisely what **D-648** excludes from authored-input maintenance, and
**D-436** reserves a mechanism's fate to the user. **(c)** **D-657** requires a mechanism change to be
decided over its whole population both ways before it is applied, which is a derivation no order of
this batch authorizes. **A2's own words are the operative instruction here — *a fifth failing verdict
is a STOP-and-report* — and this is the report half.**

*What the fix would be, stated so the next dispatch need not rediscover it:* one authored signature
row naming the shape this file has, decided over the tool's whole population both ways, plus a
regeneration of `tools/audit/artifact_inventory.json`. **Both are the user's to order.**

### 12.2 E2, graded limb by limb

| E2's limb | verdict |
|---|---|
| a fresh full guard run at the tree the close leaves | **MET** |
| `tools/audit/guard_state.json` committed only after the run that produced it | **MET** |
| *"the three known failing checks and no others"* | **NOT MET — five failing** |
| *"zero STOPs"* | **NOT MET — one STOP** |

**E2 IS NOT MET, and it is reported unmet rather than made true by an unordered act.** Two distinct
causes, neither of them absorbed:

- **the fourth red** is caused by a root-level ruling record another side wrote after the previous
  batch closed, and clearing it is an act A3 does not name (§3.4, §9.2);
- **the fifth red** is caused by this batch's own ordered landing, and clearing it is a mechanism
  change reserved to the user (§12.1).

**No check that passed at the start failed at the end for any reason other than the landing the
dispatch orders**, and **no check that failed at the start passes at the end.**

**The enumeration taken immediately after the run and before this section was written reported
`tools/audit/guard_state.json` as the ONE tracked modification and no second**
(`python tools/audit/changed_paths.py`, filtered with `Grep` by `^ ?[MADRCU]`). **This section was
then written, so the end-state commit carries two paths — that artifact and this report — and both
are members of A3's list. A3 holds through the end state.**

---

## 13. Self-check over this batch's own diff

Performed by re-reading the actual working-tree movement and the commit objects, not the memory of
making them.

1. **Principles touched.** **#12** — nothing was deleted and nothing rewritten; both landed paths are
   committed as they stand, the forward bound's outgoing aiming was appended rather than replaced,
   and the previous batch's `STATUS.md` entries were moved verbatim with the tool's own byte
   reconciliation rather than retyped. **#6** — the workbook stays the one copy; no extraction and no
   second home was created for it. **#13** — the fifth guard verdict is surfaced as a STOP and
   **nothing was built around it**: the tool that halts was not touched, the halt was not routed
   around, and the batch reports rather than repairs (§12.1); the contradiction between A2/A3 and E2
   is likewise surfaced at §9.2 rather than resolved; and the three untracked 2026-08-29 documents
   are surfaced rather than absorbed into the enumeration. **#7** — the remedy for the fifth verdict
   belongs to the tool's own authored table and to a user ruling, not to this batch, so it was left
   there. **#15** — every claim about a commit or a
   blob in this report is verified at the object by explicit hash, never at an assertion; both landed
   paths are checked at three readings each, and `origin/master` at two independent ones. **#17f /
   D-431** — no figure is transcribed from the dispatch, which states none; the figures this report
   publishes that have no generated artifact are ordered by the dispatch and are published with the
   tool and the pattern that produced them, stated at each site. **#19** — nothing is claimed
   established that was not measured; the fourth guard red is reported with the mechanism that
   explains it, established at the files, and the three untracked documents are reported by existence
   and name only because nothing more was measured. **#10** — the act date is stated as the day the
   batch ran rather than the day the dispatch was written, at every site where a date enters the
   record, including the comment beside the forward bound's own date constant.
2. **Conventions.** American English. No self-invented label, abbreviation or numbering scheme —
   every identifier used is one the record already carries. **No music-theory word arises in a
   non-musical sense**: *score* does not appear in its numerical sense, *key* does not appear at all,
   *measure* appears only as the verb and as *measurement*, *mode* appears only in the qualified
   compounds *CHECK mode* and *write mode* which the record itself uses, and *root* appears only in
   the record's own compound *root-level*, naming the repository's top directory.
3. **Figures and premises.** Every premise the dispatch stated was re-established at the object or at
   the file before it was relied on: the tip, the tree shape, the guard state, and the
   present-and-untracked status of both paths. **No premise was carried from the dispatch's word, and
   the dispatch asserts no git-object value to carry.** The one premise the dispatch states as FACT
   about the guard set — its three known failing checks — was measured and holds.
4. **File-tools rule (D-253).** Working-tree content was read with `Read` / `Grep` / `Glob`
   throughout. Shell use was read-only git object queries by explicit hash, the writes the dispatch
   orders, and the sanctioned `tools/audit/` scripts. **The guard denied one command and it was not
   routed around** — it was re-taken through the file tools; §2 records it.
5. **Uncertainty on any comparison.** The comparisons this report asserts — the two blob identities
   across three readings each, and the commit-level differences — are byte-exact object-to-object
   measurements, not estimates, so **#24** is not engaged. The one derived quantity, the 160 at §5.1,
   is the exact difference of exact counts and carries no sampling error. No difference between two
   estimated quantities is asserted anywhere.
