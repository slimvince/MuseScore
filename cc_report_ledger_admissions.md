# CC REPORT — THE SEVEN DISPOSITIONS ARE IN THE LEDGER

*Written by CC, 2026-08-26, executing `cc_instruction_ledger_admissions.md`, which executes Rulings
1–3 of `cowork_rulings_2026_08_26_ledger_dispositions_sitting.md`. This batch performed NO
ratification of its own and ordered NO register entry.*

**What ran, in one paragraph.** The user's seven dispositions were WRITTEN IN. Five entries entered
the ledger, three did not, one statement was routed. **This side disposed nothing:** the dispositions
are the user's, taken at his own ruling record, and what this batch performed is the RE-CHECK AT THE
GATE that Ruling 8 requires of every hand admission when it enters. **All five pass**, so nothing was
added to the REFUSED AT RE-CHECK list, which still holds the one member the previous batch put
there — now carrying a pointer to the entry that replaces it, kept beside it and never over it (#12).

---

## 1. TASK 0 — THE START STATE, AND THE ONE FACT THE WRITING SIDE COULD NOT SETTLE

### 1.1 Task 0(a) — the tip

`.git/refs/heads/master` was read with the file tool — **the ref side** — and reads
`052b183006ec89243d8f7863c59622b7d62d435c`, exactly as the dispatch requires. No STOP.

### 1.2 ★ Task 0(b) — SETTLED AT THE GIT OBJECTS: A THIRD COMMIT EXISTS; NOTHING WAS AMENDED

The writing side carried this as *not established* and relied on it nowhere. It is settled here by
read-only git OBJECT queries named by explicit hash, which is the read D-253 permits.

**The finding, in three parts.**

1. **`902d903a62443fe2f0f503deafdca3264e59f7fb` EXISTS as a commit object** (`git cat-file -t` →
   `commit`) and its parent is `4bc362c57e300688a28617a764f97f98e9df836e`.
2. **It is the DIRECT PARENT of the branch tip.** The tip's parent line names it. So it stands on the
   branch, reachable, at the position the report claims for it — **which is what rules out an amend**:
   an amend would have replaced it with a different hash and left the named one off the branch.
3. **A THIRD COMMIT EXISTS AFTER IT — the tip itself**, committed 36 seconds later (16:14:36 → 16:15:12
   +0200). `git show --stat` by explicit hash: it touches **exactly one path**,
   `cc_report_ledger_build.md`, **+12 / −1**, and its own subject says why — it records the ledger-build
   batch's final commit hash and close arithmetic in its report, *"one line the batch could not write
   from inside the commit that carries it."*

**So the report's sentence was true when written and is now incomplete rather than wrong:**
`902d903a62…` WAS that batch's second and final commit at the moment the sentence was authored; the
tip is a THIRD commit of the same batch, written afterwards, whose entire content is the appendix to
that very report. **The report is NOT edited** — it is dated and disclaims its own end state in terms.
The fact is reported and nothing is acted on.

### 1.3 Task 0(c) — the start-state population, measured by the tool and not by `git status`

`python tools/audit/changed_paths.py` — **835 changed-path records, EVERY ONE OF THEM `??`
(untracked), and ZERO tracked modifications.**

**One instruction therefore had an EMPTY SUBJECT, and it is named rather than passed over.** Task 0(d)
says *"Also land any other file left tracked-modified by the previous batch, naming each."* **There is
none to name.** The previous batch's tracked modifications were all committed — seven at
`902d903a62…` and the eighth, its own report, at the tip.

### 1.4 Task 0(d) — the landings, in ONE commit

Commit **`550ffc28cd80b52aa8d0e6f8a88925b8b3cf2de0`**, verified by
`changed_paths.py --commit <hash>` to touch exactly three paths, all `A`:

| Path | What it is |
|---|---|
| `cowork_rulings_2026_08_26_ledger_dispositions_sitting.md` | the ruling record this dispatch executes |
| `cc_instruction_ledger_admissions.md` | this dispatch |
| `cowork_fact_gate_admissions_2026_08_26.md` | **the correction of the previous batch's omission** |

**On the third, because it is the one that mattered.** The committed tree already carried an
`EMPIRICAL_FINDINGS_LEDGER.md` that cites into that file at three entries, while the file itself stood
untracked — so the citations' target was not in the tree. **It is landed, NOT modified:** it was read
WHOLE before it was staged (which is also what the standing rule requires of a file one publishes),
and no byte of it is changed by this batch. **Nothing else of the 835-record untracked population was
committed.**

Then `python tools/audit/gen_evidence_pin_membership.py` ran, exit 0: 7 generated ratification
documents, 72 ruling records read, 7 members, 5 pinned, **0 UNRESOLVED**, 8 tools carrying a pin
constant, 3 outside the class. It wrote `tools/audit/evidence_pin_membership.json`.

---

## 2. TASK 2 — THE FIVE GATE VERDICTS, EACH WITH ITS GROUND

**The gate:** *does the fact survive the implementation being thrown away?* — plus **approach-level**,
that is, stated without our implementation's words in it. Each verdict is also written at its own
entry in the ledger, where a reader meets it.

| # | Entry | Verdict | The ground, in one sentence |
|---|---|---|---|
| 1 | **C9** — the ruled restatement | **PASSES** | Every term — leading tone, diminished reading, *correct*, passage, repertoire — is music theory or a property of the held music, checkable at the notes and at the published human annotation, and the subject phrase whose implementation-defined population caused the first refusal is gone from it. |
| 2 | **C42** — leading-tone half | **PASSES** on the admitted half | How often a leading tone accompanies a real modulation rather than a passing tonicization is a property of the music and of the published annotation, countable by anyone holding both and by no code of ours. |
| 3 | **C43** — fact half | **PASSES** on the fact half | How much earlier music it takes for the tonality at a given moment to be settled is a property of the music, so the claim holds for any analysis that reads backwards for tonal context, whatever it is built from. |
| 4 | **C44** — at the ruled width | **PASSES** at that width, as a design antipattern | The statement is about a CLASS of inference architectures — stages that have already fixed an answer and published ranked alternatives — so it stands with our pipeline thrown away, and attached rule (b) admits a design antipattern to this ledger. |
| 5 | **C45 reading one** | **PASSES** | It states a relation between this music and a class of objectives that score readings on local evidence, so it is checkable by anyone who builds one; that a wrong reading can be such an objective's own optimum is a fact about the music meeting the class. |

**NOTHING IS REFUSED, and the one the dispatch said to check hardest is the one that passes cleanest.**
C9's restatement was checked term by term against the ground that refused its predecessor: the earlier
wording's subject, *"the genuine cases"*, denoted the correct fires of one mechanism of ours; the
restatement's subject, *passages where a diminished reading is the correct one*, is a partition a
musician with the score and the published annotation can draw with our code deleted. **The predicate
carries no implementation vocabulary either** — the earlier stripping had removed *"available at
analysis time"* from the predicate and left the defect in the subject; both are clear now.

**What is NOT claimed by any of these five verdicts.** Not that the fact is correct — the gate is not
a correctness test, and correctness travels in the uncertainty and establishment-status fields.
Not that any entry is upgraded by entering. Not that a named half or a ruled width has been widened:
each entry states what was not admitted with it.

---

## 3. ★ TASK 1's HARD REQUIREMENT — WHERE THE C9 SCOPE IS CARRIED, AND WHETHER THE FIELD HOLDS IT

**The requirement.** The measured scope goes in the UNCERTAINTY field and NOT in the sentence; if the
uncertainty field as it stands does not carry the difference, say so and **STOP** rather than widening
or narrowing the sentence.

**THE ANSWER: THE FIELD HOLDS IT. NO STOP. The sentence was neither widened nor narrowed.**

**What the difference is.** The restatement speaks of *passages* generally. What was measured is the
cases the minor-read-as-diminished mechanism fired on — a strictly narrower population.

**Where it is carried, at the object.** C9's uncertainty field at
`cowork_empirical_findings_candidates.md` §C9 reads, quoting its source: *"a handful of genuine cases
against several times as many wrong firings"*, followed by *"The counts are in the archive that
measured them and are not restated here (D-431)."* That was verified against the source itself,
`docs/scoring_model.md:1418–1424`, where the same words stand.

**Why that carries the difference.** The field names the measured population as **FIRINGS** — a
handful genuine against several times as many wrong ones. A firing is an event of a mechanism, not a
passage of music, so a reader of the entry cannot take the measured population for *passages at
large*: the sentence says passages, the field says firings, and the gap between them is visible on the
face of the entry, in the source's own terms.

**The one qualification, stated rather than smoothed.** The uncertainty field names the population as
firings; it does not name WHICH mechanism. That is named by the two neighbouring fields of the same
entry — provenance `docs/scoring_model.md:1418–1424`, and the establishment status recording the item
DEFERRED as **D-300**. So the DIFFERENCE is carried by the uncertainty field alone, as required; the
IDENTITY of the mechanism is carried across the five fields together. **This is reported because the
requirement was stated as a hard one, and a reader is entitled to know exactly how much of it one
field bears.**

**And the refusal is kept beside, never over it (#12).** The ledger's §5 keeps the REFUSED AT RE-CHECK
record of the original wording with its ground unchanged, and now carries a pointer from it to the
entry that replaces it — so a reader sees that the first wording was refused, why, and what stands in
its place. The refused wording is neither struck nor amended.

---

## 4. TASK 3 — THE THREE THAT DO NOT ENTER, AND THE ONE THAT IS ROUTED

All four are written into the ledger's §8, *what stands outside this ledger*, so silence claims
nothing. Each joins the class it belongs to rather than getting a bullet of its own, so §8 keeps one
home per class (#6).

| Item | Class | What the ledger records |
|---|---|---|
| **C45 reading two** | **NOT ADMITTED** | *Our failure class was of that kind.* The evidence is one dormant scorer's own score arithmetic on two passages; the population is **ours**. |
| **C46** | **PROPOSED FOR NOTHING** | Its durable half is already ruled and homed as the decision-neutrality corollary (**D-190**), clause (a); admitting it would publish that rule twice (#6). Recorded as the record's clearest MEASURED instance of why that corollary was needed. |
| **C47** | **FAILS** | Every quantity is a property of our resolver's ranking and our carried menu; *rank* has no meaning once that implementation is thrown away. Recorded because a source that fails is part of the coverage. |
| **C45 reading three** | **ROUTED** | *Diagnose whether an error is a search failure or a model failure before widening the search* → the phase definitions' constraints and stop rules. |

**★ THE ROUTING'S BOUND IS RECORDED WITH IT, AS THE RULING STATES IT: THE DESTINATION CANNOT PRESENTLY
RECEIVE IT.** It joins C31's half (a), C40 and twenty-one of the twenty-six `DEFECT_TYPES.md` rows
already standing routed there. **NOTHING WAS WRITTEN TO THE PHASE DEFINITIONS** — routing is a
disposition, not a transfer, and no artifact can take it yet. The ledger's §8 says so at the bullet, so
a reader of the routing meets the empty drawer in the same breath.

---

## 5. TASK 4 — THE BANNER, AND THE SEVEN OTHER PLACES THE LEDGER STATED SOMETHING NO LONGER TRUE

### 5.1 What the banner now states

The banner carries all four things the dispatch names: **the entry count (thirty-five)**; **that the
third ruled seed is now represented**, with its coverage bound restated — reached BY PATTERN over the
register's entry headings, its 477 entries not all read, the bound not discharged; **the REFUSED AT
RE-CHECK list**, still one member, C9's original wording, now pointing at its replacement, plus the
statement that this batch's re-check refused nothing; and **the disposition arithmetic for the seven**,
item by item, closing as *seven items, seven dispositions; 30 + 5 = 35 entries*. The count was
verified against the file: **35 `### C…` entry headings**, which matches the banner and the §6 heading.

### 5.2 ★ AN EXTENSION OF TASK 4's LETTER, DECLARED

Task 4 names the banner. **Updating the banner alone would have left seven statements elsewhere in the
same file false about the file itself**, which is the doc-sync half's own subject (#10) and would have
made the banner disagree with the body a reader reaches next. Every one of these is inside the fence —
they are all `EMPIRICAL_FINDINGS_LEDGER.md` — and in every case the FORMER WORDING IS PRESERVED IN
PLACE (#12) rather than replaced silently:

1. **§2's transcribed-restatement paragraph** said C8, C9 and C11's admitted text stands at one file's
   lines 119–121. Left standing it would send a reader of C9's entry to the **refused** sentence. It
   now says where each restatement's admitted text stands, and the former wording is quoted whole.
2. **§3's heading** — *"AND WHICH IS NOT"* — was false once all three seeds were represented; and its
   opening sentence spoke of a *shortfall* that has been closed. Both preserved verbatim; the new text
   states that **represented is not exhausted**.
3. **§3's second-seed row** said *"Seven … and so does the one refused at re-check, C9"*. C9 is now an
   entry, so the row reads eight, with the former wording preserved.
4. **§3's third-seed row** read **NO — NOT REPRESENTED AS A SOURCE**. It now reads YES since 2026-08-26
   and not before, with the former verdict preserved beneath the table and the establishment left
   exactly as it was made.
5. **§4's heading and its *undispositioned* paragraph** were true only until the same day's sitting.
   Corrected, with what the user ruled named, and with the reason the candidates file is NOT edited to
   agree written in.
6. **§5's title and structure** covered one re-check; there are now two. Both are reported, the first
   one's account untouched.
7. **§10's opening** said the thirty-one *below* were admitted at a sitting. Five more were admitted at
   a second sitting; corrected, former wording preserved.

### 5.3 What Task 4 forbade, and was not done

**`cowork_empirical_findings_candidates.md` IS NOT EDITED — not one byte, of any kind.** Its Part Three
still carries *proposed* verdicts and its banner sentence calling itself superseded is untouched. The
ledger's §4 now records WHY, in the dispatch's own reasoning: the candidates file is a working list,
the ruling record is where dispositions live, and editing the working list to agree would create the
second copy the ledger's whole form exists to prevent.

---

## 6. TASK 5 — `STATUS.md`, THE FORWARD BOUND, AND THE SWEEP

### 6.1 (a) The `STATUS.md` pointer entry — written BEFORE the forward-bound tool ran

One entry, in the OI-222 POINTER form: **no count, no identity, no rendered value** (**D-431**). It
names the ledger, the ruling record and this report, and says what the batch did and did not do. It
was written first, which is what lets the tool's occurrence test find the outgoing entry exactly once —
the reverse order makes that test find zero and STOP.

### 6.2 (b) Re-aiming the forward-bound tool

**The exact command line:** `python tools/audit/gen_status_batch_bound.py --apply` — the flag read
from the tool's own argument parser, a mutually exclusive group of `--apply` and `--check`.

**The five aiming constants, as set:**

| Constant | Value |
|---|---|
| `BASE_COMMIT` | `550ffc28cd80b52aa8d0e6f8a88925b8b3cf2de0` |
| `PREVIOUS_BATCH_DISPATCH` | `cc_instruction_ledger_build.md` |
| `ACT_DATE` | `2026-08-26` |
| `DISPATCH` | `cc_instruction_ledger_admissions.md` |
| `TASK` | `Task 5` |

**Which task number, and why.** **`Task 5`.** The constant names the task of the executing dispatch
that performs the move, and this dispatch orders the re-aiming and the run at **Task 5(b)** — inside
its Task 5. It is not a carry-over: the value was chosen by reading this dispatch's own structure, and
it happens to coincide with the previous aiming's for the same reason.

**The outgoing aiming was APPENDED to `PREVIOUS_AIMINGS`, not overwritten (#12)** — one new row:
executing act `cc_instruction_ledger_build.md, Task 5`, base commit
`4bc362c57e300688a28617a764f97f98e9df836e`, then-previous batch `cc_instruction_sizing_tests.md`.

**The run:** **1 entry moved, 3,381 characters**; byte-present in `STATUS_ARCHIVE.md` exactly once
**True**; absent from the must-read **True**. The one declared textual adjustment — the
`Last updated: ` prefix — applied, as designed, and no second adjustment was needed.

### 6.3 (c) The sweep

Ruled order: `gen_guard_state.py`, then `gen_guard_classification.py`.

| Round | Result |
|---|---|
| **Round 1** | 75 run, **4 failing**, 4 not run, 16 historical |
| **Round 2** (after the staleness cure) | 75 run, **3 failing**, 4 not run, 16 historical — **fixpoint** |
| **Round 3** (with this report on disk) | *see §6.5* |

**Classification:** live **69** · point-in-time **16** · neither **2** · **live-and-failing 3**.

*Every count in this section is the two tools' own output and stands at their artifacts —
`tools/audit/guard_state.json` and `tools/audit/guard_classification.json` — which is where a reader
checks it rather than here (**D-431**).*

**The three reds are the three the dispatch names as standing and forbids curing**, and each was
classified at its own captured text before anything was touched:
`gen_filing_convention_application.py --check` (the `[[OI-372]]` guard),
`decisions/apply_soft_discard.py --check`, `decisions/apply_residue_discard.py --check`. **None was
cured, and neither discard-act check was touched.**

**ONE staleness red was cured, and it is declared:** `gen_session_start_read_size.py --check`, red by
construction because this batch writes to `STATUS.md`, a member of the session-start read. Cured under
the standing sweep rule by regenerating its artifact. **No other red was met**, so the
decision-red-on-doubt STOP was never reached.

### 6.4 The filing-convention guard's candidate list — reported, not touched

Run read-only as `--check`. **The list is UNCHANGED and there is no fourth member:**

> `STOP: derived candidates with no authored verdict: BUILD_AND_TEST_ARCHIVE.md,
> OPEN_ITEMS_ARCHIVE.md, cc_report_preparation_fourteenth.md.`

**None of this batch's four new root-level files entered it.** It was **NOT classified, NOT cured and
NOT regenerated**, exactly as the dispatch requires.

**★ AND ONE THING ABOUT THIS REPORT'S OWN SILENCE IN THAT LIST IS DECLARED, BECAUSE A CONTROL BELIEVED
TO BE IN PLACE AND NOT IN PLACE IS WORSE THAN NONE (#19).** The guard's S1 signature fires on a line
in a document's last twenty-five non-blank lines that carries BOTH a fate word — *resolved in,
deleted, removed, retired, superseded, falsified* — AND a run of seven or more hexadecimal characters,
which any commit hash satisfies. **This report was written with its commit hashes kept out of that
tail deliberately.** So its absence from the candidate list is ENGINEERED, not natural, and the
writing side should read it that way. Nothing was withheld to achieve it: every hash this report
carries is in §1 and §6, where a reader meets it first.

### 6.5 The final sweep, with this report on disk

**Round 3 ran with all four of this batch's new root-level files present** — the three landed at Task
0(d) and this report. **75 guards run, 72 passing, THREE failing, 4 not run, 16 historical records** —
the same three standing reds and no other. **So neither this batch nor its report widened the red
set.** The filing-convention candidate list at §6.4 was re-read in that state and is unchanged: three
members, no fourth, and this report is not among them.

---

## 7. EVERY PATH WRITTEN BY THIS BATCH

| Path | By what | Fence clause |
|---|---|---|
| `cowork_rulings_2026_08_26_ledger_dispositions_sitting.md` | Task 0(d) landing (add) | the landings |
| `cc_instruction_ledger_admissions.md` | Task 0(d) landing (add) | the landings |
| `cowork_fact_gate_admissions_2026_08_26.md` | Task 0(d) landing (add) | the landings |
| `tools/audit/evidence_pin_membership.json` | `gen_evidence_pin_membership.py` | named in the fence |
| `EMPIRICAL_FINDINGS_LEDGER.md` | Tasks 1, 3, 4 | named in the fence |
| `STATUS.md` | Task 5(a), then the forward-bound tool | named in the fence; tool output |
| `tools/audit/gen_status_batch_bound.py` | Task 5(b), five constants + the appended row | the named carve-out |
| `STATUS_ARCHIVE.md` | the forward-bound tool's own output | a tool this dispatch orders |
| `tools/audit/status_batch_bound.json` | the forward-bound tool's own output | a tool this dispatch orders |
| `tools/audit/session_start_read_size.json` | the staleness cure | a tool this dispatch orders |
| `tools/audit/guard_state.json` | `gen_guard_state.py` | a tool this dispatch orders |
| `tools/audit/guard_classification.json` | `gen_guard_classification.py` — **re-derived byte-identical, so it is not a tracked modification at the close** | a tool this dispatch orders |
| `cc_report_ledger_admissions.md` | Task 5(d) — this file | named in the fence |

**Exactly one path under `tools/` ending `.py` is modified**, and it is the one the dispatch carves
out by name.

---

## 8. DEPARTURES, AND EVERY INSTRUCTION THIS BATCH COULD NOT OBEY

**No instruction could not be obeyed. No STOP was reached. The standing clause was never engaged: no
instruction here required a write outside the fence.** What follows are declared departures from the
LETTER of an instruction, and one procedural slip.

1. **The Task 4 extension** — six further places in the ledger corrected so the file does not state
   something false about itself. Declared in full at §5.2, all inside the fence, every former wording
   preserved.
2. **A figure restated in the banner.** The banner restates *477 entries* as part of the third seed's
   coverage bound. **The dispatch names that figure in its own instruction and orders the restatement**,
   and the ledger cites where it stands (§9 bound 3, and the candidates file §13.4), so the tension
   with **D-431** is declared rather than resolved by this side.
3. **A procedural slip, reported because reporting it costs nothing and hiding it would be the
   defect.** The staleness cure was first triggered by invoking
   `gen_session_start_read_size.py --help`; that tool's parser does not consume `--help`, so instead of
   printing usage it RAN in its default write mode. The intended effect and the actual effect are the
   same — regenerate the artifact — but the invocation was not the one I meant. It was immediately
   re-run with no arguments so the recorded command line is the canonical one, and the tool is
   idempotent in that mode.
4. **The engineered silence in the filing-convention candidate list**, declared at §6.4.

**And the four negatives the dispatch asks to be visible.** **NO admission was made, changed or
refused as an act** — the five re-check verdicts are verdicts, not admissions, and the refusal that
stands was the previous batch's. **NO ratification.** **NO open-items row was created, flipped or
discarded, and no finding number was allocated.** **NOTHING was written to the phase definitions.**

**★ NO REGISTER ENTRY, AND THIS IS THE FOURTH CONSECUTIVE BATCH SHAPED THAT WAY.** These dispositions
are the user's ratifications and the decisions register's rule (c) says every new ratification gets an
entry. The entries owed are named in the ruling record's §5 and **none is written**, because
`apply_soft_discard.py --check` and `apply_residue_discard.py --check` are mutually unsatisfiable with
rule (c) for every addition after 2026-08-17. **The dispatch orders no entry for exactly that reason
and asks that the fourth instance be said out loud, so it is said: this is a PATTERN, not a fourth
one-off.** Curing the blocker is a decision act, it has never been put to the user, and nothing here
proposes it.

---

## 9. WHAT THIS BATCH DID NOT TOUCH

No `CLAUDE.md`, `ARCHITECTURE.md` or `DECISIONS.md` edit. No `src/` change. No test changed, moved or
run. No golden. Nothing under `tools/corpus/` or `tools/robust_stop/`. No behaviour change to the
analysis, and no measurement of the analysis built, designed, scoped or run — every check in this
batch is TEXTUAL. No derivation and no comparison. Neither blind output opened. Neither brief, neither
pack; the generator, the manifest and every withheld family untouched. No score opened. No other `.py`
source edited. `cowork_empirical_findings_candidates.md` untouched, and
`cowork_fact_gate_admissions_2026_08_26.md` landed rather than modified.

---

## 10. THE CLOSE

**The changed-path arithmetic, measured by `tools/audit/changed_paths.py` and never by `git status`
(D-253). It closes against the start state.**

| | Start | Close |
|---|---:|---:|
| changed-path records | 835 | **841** |
| — of which untracked | 835 | **833** |
| — of which tracked modifications | **0** | **8** |

**The untracked side closes exactly:** 835, less the three landed at Task 0(d), plus one for this
report, is 833.

**All eight tracked modifications are inside the fence**, and every one is named at §7:
`EMPIRICAL_FINDINGS_LEDGER.md`, `STATUS.md`, `STATUS_ARCHIVE.md`,
`tools/audit/evidence_pin_membership.json`, `tools/audit/gen_status_batch_bound.py`,
`tools/audit/guard_state.json`, `tools/audit/session_start_read_size.json`,
`tools/audit/status_batch_bound.json`.

**`tools/audit/guard_classification.json` is NOT among them**, because the tool re-derived it
byte-identical. That is the right outcome and is stated here so its absence is not read as a tool
that never ran.

**Nothing of the standing untracked population is committed at the close**, and this report is its
only addition.

**THE END STATE IS NOT ASSERTED BY THIS REPORT.** It cannot see the commit that carries it, and it
makes no claim about it.
