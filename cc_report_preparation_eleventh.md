# CC report — the preparation phase's ELEVENTH batch: **STOPPED AT ITS DECLARED PRECONDITION, NOTHING EXECUTED, NOTHING COMMITTED**

> **Dispatch `cc_instruction_preparation_eleventh.md` (Cowork, 2026-08-18), read in full by CC on
> 2026-08-18.** **The batch is NOT complete and NOT partially complete: no task ran.** The dispatch's
> own standing bar — *"Run the FULL guard set BEFORE the first edit and again at the end… **A
> different start state is a STOP-and-report.**"* — fired at the first act, before Task 0.
>
> **NOTHING WAS COMMITTED. NOTHING WAS PUSHED. NO FILE THIS BATCH WOULD HAVE EDITED WAS EDITED.**
> `HEAD` and `origin/master` are both `9390e2ca2c` — the tenth batch's terminus — exactly as they
> were when this session booted. **No commit sits on that terminus**, so the twenty-ninth handover
> block's branch rule still reports this batch **NOT STARTED** for whoever arrives next.
>
> **Nothing in this report is a claim about the analysis.** No `src/` change, no golden, no test
> changed, moved or run, nothing under `tools/corpus/` or `tools/robust_stop/`, no measurement of
> the analysis built, designed, scoped or run. **No open-items row was created, flipped or
> discarded.** Every figure below is cited to a generated artifact or to a content-addressed git
> object, and none is transcribed from memory (**D-431**).
>
> **What this session DID do beyond the STOP is READ-ONLY establishment and is declared as such**
> (§5 and §6): the derivation Task 1 step 1 orders was carried out at the git objects, because it
> changes nothing, costs one turn, and is exactly what the STOP needs in order to be resolvable.
> **No pin was applied, no correction was written, no banner was touched, no figure was corrected.**

---

## 1. The reading

`CLAUDE.md` and `STATUS.md` **as they now stand, in full**. `DECISIONS.md` in full — unconditional
and explicitly not demoted. `BUILD_AND_TEST.md` in full, because this batch MEETS its condition: it
runs the guard set, whose commands live there.

**The whole open-items INDEX was NOT read.** Rule (a)'s derived gating answer was read at
`tools/audit/nongating_apparatus_rows.json` → `★_the_live_gating_answer` → `gating_ids`, narrowed
to its identity list as the tenth batch left it. The grounds at `the_gating_rows` in the same file
were opened only to confirm that the key rule (a) names exists (it does — see §6.e); no verdict was
challenged, and no archive companion was opened, because no decision was re-opened.

**The standing clause the tenth batch landed was obeyed:** `cowork_handoff.md`, its **TWENTY-NINTH**
block, was read. That is what told this session the findings series stands at **F66** and that
numbering begins at **F67**. The **TWENTY-EIGHTH** block was read in full as well, being Task 3's
second correction site.

Then, as the dispatch orders, in full: `cowork_rulings_2026_08_18_tenth_return.md`;
`cowork_rulings_2026_08_17_ninth_return.md` (whole, not only §1, because its §3 is Task 3's first
correction site); `cowork_rulings_2026_08_16_preparation_return.md` **§6** and **§5(D)** (and §5(E),
which §5(D) is written into); and `cc_report_preparation_tenth.md` **§§3.b, 3.c and 10**.

The four artifacts the dispatch orders binding at were read at their own text:
`tools/audit/evidence_pin_membership.json`, `tools/audit/session_start_read_size.json`,
`tools/audit/guard_classification.json` (through the classification check's own re-derivation) and
`tools/audit/guard_state.json`.

**The branch rule was run before anything else** and reports **NOT STARTED**, on all three of its
own tests: no `PREPARATION ELEVENTH BATCH` section in `cowork_away_returns.md` (only the TENTH, at
its own heading); no `STATUS.md` pointer entry for an eleventh batch; and no commit on
`9390e2ca2c`.

---

## 2. Assumption A1 — **HELD**, checked first and entirely at content-addressed objects

`tools/audit/changed_paths.py` reports **exactly ONE tracked modification in the whole working
tree** — `cowork_handoff.md` — and **835 changed-path records** in total, the remaining 834 being
the known, declared, unlanded untracked population. **All three files A1 names as untracked are
present**: `cowork_rulings_2026_08_18_tenth_return.md`, `cc_instruction_preparation_eleventh.md`
and `cowork_verification_plan_preparation_tenth.md`.

The one modification's CONTENT was taken **blob against blob by explicit hash**, the working copy
first written into the object database so that both sides of the comparison are content-addressed:

| | blob |
|---|---|
| committed at `9390e2ca2c` | `08eaff0a4ec9a4092e190ed319163f364b816217` |
| working copy | `c49d6f875513240d84dfe372ba05f407a2a74bab` |

The difference is **ONE contiguous changed passage at line 4 — 179 insertions and 1 deletion**, and
it carries exactly the two parts A1's own sentence names: the **TWENTY-NINTH** session-close block
inserted, and the **TWENTY-EIGHTH** heading re-written to carry its entry-point demotion marker (the
single deletion is that heading in its undemoted form). **A1 held at the shape its own sentence
describes**, and no changed-passage count was asserted in advance (the F25 lesson).

**The F57 caveat did not arise for that file and was not assumed away.** Git's own check-in
normalisation warning on this platform — *"in the working copy of `cowork_handoff.md`, LF will be
replaced by CRLF the next time Git touches it"* — establishes the working copy is stored LF, which
is what the writing side's premise ledger measured, so the two blob hashes are directly comparable
and the file does not differ from its blob by its own line count.

---

## 3. ★ THE STOP — the start-state guard run does not match the state the dispatch declares

**The dispatch's declared start state**, which is the tenth batch's proven end state: *71 run, 70
passing, ONE failing — `tools/audit/gen_filing_convention_application.py --check` ([[OI-372]]) — 4
not run, 16 historical, zero STOPs.*

**The measured start state**, taken **before any edit, at a quiet tree**, by
`python tools/audit/gen_guard_state.py --check` followed by
`python tools/audit/gen_guard_classification.py --check`:

```
71 guard(s) run, 2 failing, 4 not run, 16 historical record(s)
  [FAIL] tools/audit/gen_filing_convention_application.py --check
  [FAIL] tools/audit/gen_evidence_pin_membership.py --check
the guard classification re-derives
```

| | run | passing | failing | not run | historical | STOPs |
|---|---:|---:|---:|---:|---:|---:|
| declared by the dispatch | 71 | 70 | 1 | 4 | 16 | 0 |
| **measured, before any edit** | 71 | **69** | **2** | 4 | 16 | 0 |

**So the start state differs, and the difference is a SECOND red.** The dispatch's own words make
that a STOP-and-report, and this report is it.

### 3.a The cause, established at the objects rather than supposed

`tools/audit/gen_evidence_pin_membership.py --check` prints only *"STALE vs the derivation:
evidence_pin_membership.json does not re-derive"*, so the cause was established by comparing the
derivation's output against the committed artifact, blob against blob by explicit hash:

| | blob |
|---|---|
| committed at `9390e2ca2c` | `80e97da1f79f8047069d39837e4cd454d7644b73` |
| freshly derived at this tree | `c3e9687ba3a48c40873c9b48befaaa32103a1102` |

**The whole difference is two lines**, and there is no third:

```
   "generated_ratification_documents": 7,
-  "ruling_records_read": 36,
+  "ruling_records_read": 37,
   "members": 7,
   "members_pinned": 3,
…
   "cowork_rulings_2026_08_17_sixth_return.md",
+  "cowork_rulings_2026_08_18_tenth_return.md",
   "cowork_rulings_oi345_oi342_2026_08_07.md"
```

**The cause is the dispatch's own premise A1.** `gen_evidence_pin_membership.py` derives its
ruling-record population from *"every root-level `cowork_rulings_*.md`"* — the file system, not the
index — so `cowork_rulings_2026_08_18_tenth_return.md`, which A1 declares present on disk and
untracked and which Task 0 exists to land, is already inside the derived population while the
committed artifact was derived at a tree that did not hold it.

**NOTHING ELSE MOVED.** Members stay at **7**, pinned at **3**, UNRESOLVED at **4**; every member's
route, document, ruling record, pin constant and state is byte-identical. No verdict, no pin, no
population and no count of members changed.

### 3.b Why this was not treated as benign and worked around

Three reasons, stated so the judgment is challengeable rather than asserted.

1. **The dispatch's letter is unconditional** and the executing side does not amend a running
   dispatch (**D-251**) nor rewrite the instruction it executes (**D-252**). A precondition stated
   as a STOP exists precisely to remove this judgment from the executing side.
2. **The stale artifact is the dispatch's own named authority for Task 1** — *"Bind at these
   artifacts, never at a recollection of them: `tools/audit/evidence_pin_membership.json` (Task 1's
   subject…)"*. Proceeding would mean binding Task 1 at an artifact the tree reports STALE, which is
   the one thing that clause forbids.
3. **Clearing it would require an act the dispatch does not order.** Task 0's paths are fixed at
   *"exactly these FOUR paths and no fifth"*, so the regenerated artifact cannot land there; and
   Task 1's ten steps order pins, corrections, a forward clause and a collision note, but never a
   regeneration of the membership artifact. Choosing where it lands would be improvisation inside a
   task whose every other step is spelled out.

### 3.c The end-state guard run, taken at a quiet tree after everything below

Identical, because nothing was edited:

```
71 guard(s) run, 2 failing, 4 not run, 16 historical record(s)
  [FAIL] tools/audit/gen_filing_convention_application.py --check
  [FAIL] tools/audit/gen_evidence_pin_membership.py --check
the guard classification re-derives
```

and `tools/audit/changed_paths.py` again reports exactly one tracked modification,
`cowork_handoff.md`, with **835** records in total. **The E-ordering rule does not arise: there is no
commit, so no value is committed before the run that produced it.**

*(Re-enumerated once more after this report file was written: still **exactly one tracked
modification**, `cowork_handoff.md`, and now **836** records — the one added record being this
report itself, untracked. The count is stated at both moments so a reader re-running it meets the
number they will actually see.)*

---

## 4. ★ ONE INCIDENT TO DECLARE, and it is CC's own

**A committed artifact was written by accident and was restored to its committed bytes in the same
turn.** Establishing the cause in §3.a required knowing what the tool derives at this tree, and the
invocation `python tools/audit/gen_evidence_pin_membership.py --help` was issued to read its command
line. **That tool has no argument parser**: `main()` builds the artifact and writes it unless the
literal string `--check` is among the arguments (`tools/audit/gen_evidence_pin_membership.py`, its
`main`), so `--help` **performed the write**.

**The remedy, taken immediately:** `git checkout 9390e2ca2cfb6e33a6bb7088f03369e1be92a0c7 --
tools/audit/evidence_pin_membership.json`, after which `git hash-object` on the path returns
`80e97da1f79f8047069d39837e4cd454d7644b73` — the committed blob — and `changed_paths.py` reports the
path unmodified. **The restore is the only reason the two guard runs in §3 and §3.c agree.**

**One residue is declared rather than left to be discovered:** the restore was performed by git,
which on this platform writes the working copy with CRLF, where the generator writes LF. Git reports
the path unmodified either way and every check that reads it compares generated text against the
file's characters, so no verdict is affected; the next run of the generator restores LF. **This is
the F57 class and it is recorded, not waved away.**

**No other file was written by this session**, and no file this batch would have edited was opened
for writing at all.

---

## 5. ★ READ-ONLY ESTABLISHMENT OF ASSUMPTION A3 — carried out because it costs nothing and is what makes the STOP resolvable

**Nothing in this section was applied.** No pin was taken, no ruling record was corrected, no
generator was touched. This is the derivation Task 1 step 1 orders, run at the git objects and
reported as data, under the standing rule that a step which can be measured before it is committed
to is measured first (**D-254**).

### 5.a The derivation as ruled, and the finer bound the record supplies

Ruling 1 fixes the derivation: **the last commit touching that surface which is dated at or before
its sitting.** Each sitting's date was read from that sitting record's own text, never from its file
name. Every record is the interim carrier (**D-230**) and **lands in git at the next dispatch's Task
0**, so **the commit that LANDED the sitting record is a hard upper bound on when the sitting was
held** — a bound the record itself supplies, finer than the date, and taken at the objects.

### 5.b The four members, derived

| member (generator) | ruling surface | sitting (from the record's own text) | sitting record landed at — the upper bound | candidates touching the surface at or before that bound | **selected** | interval from the selected commit to the bound | evidence bearing on whether the document moved inside the interval |
|---|---|---|---|---|---|---|---|
| `gen_artifact_inventory_surface.py` | `ratification_surfaces/cowork_artifact_inventory_ruling_surface.md` | the inventory sitting, **2026-08-15** | `dfea49b7a5` · 2026-08-15T13:09:23 | `31c573b06e` · 10:47:01 · *audit: THE RULING SURFACE …*<br>`b1d48d6c87` · 10:56:13 · *close: the artifact inventory closes …* | **`b1d48d6c87`** | ≤ 2 h 13 min | **Strong.** The generator's own last commit **IS** `b1d48d6c87`, and its only input, `tools/audit/artifact_inventory.json`, also last moved at `b1d48d6c87`. Neither the generator nor its input could have moved inside the interval, so a regeneration inside it could not have changed the rendering. |
| `gen_ratified_document_check.py` | `ratification_surfaces/cowork_discard_residue_surface_2026_08_16.md` | the residue sitting, **2026-08-17** | `570f2b63b1` · 2026-08-17T16:34:06 | `81e2ef1c23` · 2026-08-16T16:41:24 · *check: the ratified document itself …* — **the only commit that has ever touched this document** | **`81e2ef1c23`** | ≤ 23 h 53 min | **Moderate.** The generator has exactly one commit, the same one, so neither it nor the document moved in git inside the interval. The interval is the widest of the four, and an uncommitted regeneration inside it is not excluded by anything in the record. |
| `gen_governing_surface_readers.py` | `ratification_surfaces/cowork_governing_surface_split_2026_08_16.md` | the governing-surface split sitting, **2026-08-17** | `1f84f5d621` · 2026-08-17T09:15:30 | `c4f15a7b32` · 2026-08-16T23:27:06 · *measure: the governing-surface pruning, read-only …*<br>`9fb1ba01bf` · 2026-08-17T00:01:32 · *close: E3's run, the close's own SHA …* | **`9fb1ba01bf`** | ≤ 9 h 14 min | **Strong.** The generator's next commit is `cfb69a7ecb` · 2026-08-17T12:22:49, **after** the bound. The selected commit is the fifth batch's own closing commit, and the sitting record states in terms that the sitting was taken at that batch's verified return. |
| `gen_rulings_sort.py` | `ratification_surfaces/cowork_rulings_sort_surface_2026_08_16.md` | the rulings-sort sitting, **2026-08-17** | `570f2b63b1` · 2026-08-17T16:34:06 | `2fa6ffcbf9` · 2026-08-16T12:25:43 · *sort: the rulings sort PROPOSED …*<br>`53e552296f` · 2026-08-17T10:00:25 · *execute: the ruled governing-surface split, complete …* | **`53e552296f`** | ≤ 6 h 34 min | **Strong.** The generator's next commit is `a21a55fc12` · 2026-08-17T18:14:23, and its data file `tools/audit/rulings_sort_classification.json` next moves at the same commit — both **after** the bound. |

**A3 HOLDS for all four members**: each has at least one commit touching its surface dated at or
before its sitting, and none needed a guessed pin.

### 5.c ★ AND THE DERIVATION READ AT DATE GRANULARITY IS WRONG FOR ONE OF THE FOUR

For members 1–3 the date and the finer bound select the same commit. **For the rulings-sort member
they do not**, because **four** commits touched that document on the sitting's own day:

| commit | timestamp | position relative to the sitting |
|---|---|---|
| `53e552296f` | 2026-08-17T10:00:25 | **before** the sitting — the last such commit |
| `a21a55fc12` | 2026-08-17T18:14:23 | **after** — this is the sitting's own EXECUTING act (*execute: the sort's 60 USER-RULED placements …*, the totals the sitting's §2 ruled) |
| `4667816255` | 2026-08-17T22:28:33 | after |
| `15dfb0e172` | 2026-08-17T23:13:00 | after — **the one a date-granularity reading selects** |

**A date-granularity reading of *"dated at or before its sitting"* therefore selects `15dfb0e172`,
which is after the sitting record landed (16:34) and after the sitting's own executing act (18:14) —
that is, it pins a POST-RULING rendering and records it as the evidence of what was PUT.** That is
the precise defect Ruling 1 exists against, arriving on the very member Ruling 1's own ground names
as the reason the naive route was declined. The remedy is already inside the record and needs no new
mechanism: **the commit that landed the sitting record is the bound**, and it is derivable for every
member because **D-230** makes every such record an interim carrier landed at the next dispatch's
Task 0. This is F69 below.

### 5.d What this section does NOT establish

That the four surfaces' renderings at the selected commits are what the user read — only that
nothing in git moved either the document, its generator or (where checked) its input inside the
interval. **An uncommitted regeneration inside an interval remains possible and is not excluded**,
which is the residual risk Ruling 1 states in terms; the intervals above are what bound it, and
member 2's is a day wide.

---

## 6. Further read-only measurements the tasks order as data, taken and reported

Each below changes nothing and is reported so that the writing side has it when it resolves the
STOP.

### 6.a ★ Ruling 1b's premise does not match the tree — the census and the ratification document are outputs of TWO tools, not two outputs of one

Ruling 1b resolves F62's collision *"by SPLITTING AT THE OUTPUT"*, on the stated ground that both
rulings *"are about two different OUTPUTS of one tool, not two verdicts about one output"*. **Read at
the code, that tool has one output:**

| tool | reads | writes |
|---|---|---|
| `tools/audit/gen_artifact_inventory.py` | the tracked tree | **`tools/audit/artifact_inventory.json`** — the census |
| `tools/audit/gen_artifact_inventory_surface.py` | `tools/audit/artifact_inventory.json` | **`ratification_surfaces/cowork_artifact_inventory_ruling_surface.md`** — the ratification document, and nothing else |

So the census `gen_artifact_inventory_surface.py` is said to keep re-deriving is not its output at
all: it is the output of a sibling tool that this one consumes. **Task 1 step 6 orders both
treatments written AT `gen_artifact_inventory_surface.py`, each naming the ruling that governs it —
and one of the two sentences would then state something false about the tool it stands on**, which
is #10's own subject and the thing Ruling 2 is being run to remove elsewhere in the same dispatch.

**This is reported and not improvised on**, exactly as step 6 directs for a construction that cannot
express the split. **Two things worth stating with it, because they narrow the question rather than
widening it.** First, **Ruling 1b's OUTCOME is reachable and is arguably cleaner than its premise**:
because the two outputs already belong to two tools, pinning the surface generator's reads freezes
the rendering while the census tool keeps re-deriving, with no split inside either tool. Second,
**the mis-identification is inherited, not new**: §6 kind 3 of the 2026-08-16 record already names
`gen_artifact_inventory_surface.py` as one of *"the two derived censuses"*, and the census is
`gen_artifact_inventory.py`. **No verdict is taken here** — which tool §6 kind 3 meant is the
writing side's to say.

### 6.b ★ Ruling 3 orders five figures corrected by citation to an authority that carries three

Ruling 3 names `tools/audit/session_start_read_size.json` as *"the authority from here"* and orders
corrected *"the total, the section, the identity list, the grounds and the frozen comparison"*.
Measured at that artifact:

| figure the record publishes | value in the record | carried by the named authority? |
|---|---|---|
| the ordinary session-start read after the ninth batch — **360,213** | §3 of the ninth-return record; the twenty-eighth block | **YES** — `at_earlier_commits[0].total_characters` = **367,121** at `1760d9a4a8` |
| the section rule (a) then named — **67,950** | §3 | **YES** — `at_earlier_commits[0].characters_per_member[…★_the_live_gating_answer]` = **74,858** |
| the list of gating identities — **2,079** | §3 | **YES** — `at_the_tree.characters_per_member[… → gating_ids]` = **2,748** |
| the 216 grounds — **56,388** | §3 | **NO** |
| the frozen comparison — **3,893** | §3 | **NO** |
| the read before the ninth batch — **656,292**, and the −45.1 % derived from it | the twenty-eighth block | **NO**, and by the tool's own declaration it cannot be |

**No other generated artifact in the tree carries the missing figures.** `tools/audit/gating_row_sizing.json`
is a different subject entirely — it sizes the WORK each gating row owes, not the characters of any
span. So two of the five figures Ruling 3 orders corrected **have no derived value to be corrected
to**, and correcting them would need either a change to `gen_session_start_read_size.py` (tool work,
which Ruling 3's own declined alternative records the standing mechanism freeze as barring) or a
transcription (**D-431** forbids it). **Reported, not decided.**

### 6.c The arithmetic Ruling 3 asks to be closed — it closes exactly

Taken from `tools/audit/session_start_read_size.json` at `1760d9a4a8`, no value transcribed from any
record:

| member | characters |
|---|---:|
| `CLAUDE.md` | 153,246 |
| `STATUS.md` | 12,243 |
| `DECISIONS.md` | 126,774 |
| the section rule (a) then named | 74,858 |
| **total** | **367,121** |

The record's 360,213 is the same four members with **67,950** in the last row. **367,121 − 360,213 =
6,908 = 74,858 − 67,950**, and every other member agrees to the digit — `DECISIONS.md` at 126,774 on
both sides. **The whole gap is one term.**

### 6.d The withdrawal of the percentage is grounded at the tool, and the ground is verbatim

Ruling 3's refusal rests on the live tool declaring that its shape does not reach the pre-ninth-batch
regime. **It does, at its source, in its own words** (`tools/audit/gen_session_start_read_size.py`,
the comment above `BASELINES`): *"Before the ninth batch the read regime named a DIFFERENT MEMBER SET
— `OPEN_ITEMS.md` whole, `BUILD_AND_TEST.md` unconditionally — and rule (a) named no
artifact-and-key pointer at all, so this measurement's shape does not reach it and forcing it would
compare two different questions."* **So the withdrawal stands on a declaration in the tool, not on an
inference about it**, and the dispatch's alternative branch — *"If the tool CAN be shown to reach
both regimes, that is a finding to report"* — does not arise.

### 6.e Task 2's premise holds, and Task 2 step 5's data question is answered

Read at the object `9390e2ca2c`, the four ratification surfaces' opening banners:

| surface | banner opens |
|---|---|
| `cowork_artifact_inventory_ruling_surface.md` | *"STATUS: RULING SURFACE, awaiting the user. NOTHING HERE IS RULED, AND NOTHING HERE HAS BEEN DONE."* |
| `cowork_discard_residue_surface_2026_08_16.md` | *"STATUS: RULING SURFACE, awaiting the user. NOTHING HERE IS RULED."* |
| `cowork_governing_surface_split_2026_08_16.md` | *"STATUS: RULING SURFACE, awaiting the user. NOTHING HERE IS RULED AND NOTHING IS EXECUTED."* |
| `cowork_rulings_sort_surface_2026_08_16.md` | *"STATUS: RULED, 2026-08-17. NOTHING IS EXECUTED BY IT."* |

**Ruling 2's premise is confirmed: three surfaces state of themselves that nothing on them is ruled,
and each was ruled at a recorded sitting.**

**Task 2 step 5's question — where the fourth surface's correction actually lives, and whether it
survives regeneration — is answered as data.** The RULED banner text lives **at the generator**,
`tools/audit/gen_rulings_sort.py`, in the render function's own emitted lines, and it was already
there at **`a21a55fc12`** (2026-08-17T18:14:23) — the eighth batch's executing commit — as well as at
`9390e2ca2c`. **It therefore survives regeneration by construction**, which is why the tenth batch's
regeneration left it standing. **The tenth batch's characterisation of it as made *"by hand"* is
corrected of record here** — and the former characterisation is preserved beside its correction
(#12): *"corrected by hand at the eighth batch"* (Ruling 2's own ground, and the tenth batch's
report). **The correction narrows a premise; it does not touch Ruling 2's conclusion**, which is that
a banner belongs at its generator — and this member is the standing demonstration that the
conclusion is right.

**One incidental confirmation**, taken while reading the grounds: rule (a)'s pointer resolves. The
key `the_gating_rows` exists in `tools/audit/nongating_apparatus_rows.json` under
`★_the_live_gating_answer`, distinct from the count key `gating_rows`. **No defect there.**

---

## 7. Findings, numbered from **F67** as the dispatch allocates — surfaced, not rowed

The dispatch bars creating an open-items row and this session created none. **None of the findings
below bears on the analysis, its inputs, or a measurement tool the analysis depends on** — every
subject is the project's own record and the apparatus that reads it.

- **F67 (new, the largest) — A DISPATCH THAT LANDS ITS OWN AUTHORITY CANNOT BOOT TO THE PREVIOUS
  BATCH'S END STATE, BECAUSE A DERIVED POPULATION THAT READS THE DIRECTORY IS MOVED BY AN UNTRACKED
  FILE.** The declared start state and assumption A1 contradict each other by construction: A1
  declares `cowork_rulings_2026_08_18_tenth_return.md` on disk and untracked, and
  `gen_evidence_pin_membership.py` derives its population from *every root-level
  `cowork_rulings_*.md`* on the file system, so the artifact is STALE from the moment the writing
  side saves the record — before the executing side is even dispatched. **The general form worth
  carrying: where a derivation's population is the FILE SYSTEM rather than the index, an untracked
  file is already inside it, so any state declared "the previous batch's proven end state" is false
  for every such derivation the moment the next dispatch's own inputs are written.** The narrow
  remedies are visible and are the writing side's to choose between — derive from the index rather
  than the tree; or declare the expected start state at the tree the dispatch will actually meet;
  or name the regeneration as an ordered act with a home. §3.
- **F68 (new) — RULING 1b's PREMISE NAMES TWO OUTPUTS OF ONE TOOL, AND THE TREE HAS ONE OUTPUT EACH
  FROM TWO TOOLS.** `gen_artifact_inventory_surface.py` writes only the ratification document;
  the census is `gen_artifact_inventory.py`'s. Writing both treatments at the surface generator would
  put a false sentence about a tool at that tool. **The general form: a ruling that resolves a
  collision by naming the objects it is about must be checked at the objects before it is written,
  because the resolution is only as good as the identification.** The outcome the ruling wants is
  reachable and cleaner at the true shape; the mis-identification is inherited from §6 kind 3 of the
  2026-08-16 record and is not new here. §6.a.
- **F69 (new) — THE PIN DERIVATION READ AT DATE GRANULARITY SELECTS A POST-RULING COMMIT FOR ONE OF
  THE FOUR MEMBERS.** Four commits touched the rulings-sort surface on the sitting's own day; a date
  reading selects the last of them, which lands after the sitting's own executing act. **On that
  member the derivation reproduces the exact defect Ruling 1 exists against — the one Ruling 1's own
  ground names it for.** The record already supplies the finer bound and no new mechanism is needed:
  every sitting record is an interim carrier landed at the next dispatch's Task 0 (**D-230**), so the
  commit that LANDED the record bounds when the sitting was held. **The general form: a derivation
  whose discriminator is a DATE is only as sharp as the day, and it fails exactly where the day is
  busy — which is the day a sitting is held and executed.** §5.c.
- **F70 (new) — A CORRECTION ORDERED "BY CITATION TO THE ARTIFACT" NAMES FIVE FIGURES AND THE
  ARTIFACT CARRIES THREE.** The grounds figure and the frozen-comparison figure have no generated
  home anywhere in the tree, and neither does the pre-ninth-batch total the same sentence rests on.
  **The general form: an authority named for a class of figures is established for the figures it
  actually derives, and a correction that reaches past them has only two lawful exits — extend the
  generator, or withdraw the figure as Ruling 3 already withdraws the percentage.** §6.b.
- **F71 (new, small) — A GENERATOR WITH NO ARGUMENT PARSER TREATS `--help` AS A WRITE.**
  `gen_evidence_pin_membership.py`'s `main` writes its artifact unless the literal `--check` appears
  in the arguments, so every unrecognised flag — including the one flag a reader reaches for first —
  mutates a committed artifact. It fired here (§4) and was restored in the same turn. **This is
  F64's family with the roles swapped: F64 was a documented flag the command line does not accept;
  this is an undocumented flag the command line silently accepts as the write.** The class is worth
  a sweep of the audit generators rather than a fix at this one tool, and the sweep is not taken
  here.
- **F1–F66 ride to the preparation phase's retrospective unchanged**, with the E3 ordering defect
  and the A1 premise error. **F3 is THIRTEEN times surfaced, unfixed and unrowed** —
  `reaim_home_anchors.py --check` exits 0 while printing drifted anchors, and
  `gen_cluster_dispositions.py --verify` is the drift authority, which this session used as the
  authority throughout. **F25 did not repeat**: no changed-passage count was asserted in advance.
  **F57 was applied rather than assumed** at §2, and its class recurred at §4 and is declared there.

---

## 8. The registered expectations

| | verdict |
|---|---|
| **E0** (Task 0 — four paths, one modification of the stated shape, three additions, no staging override) | **NOT REACHED.** Task 0 did not run. Its first act, A1's check, **HELD** (§2); the commit was never taken because the STOP fired before it. |
| **E1** (Task 1) | **NOT REACHED.** No pin applied, no ruling record corrected, no forward clause written, no collision note written. The derivation E1 asks to be published is established read-only at §5 and returned as data; §6.a is the STOP its own step 6 provides for. |
| **E2** (Task 2) | **NOT REACHED.** No generator touched, no banner rendered. Its premise is confirmed and its step-5 data question answered at §6.e. |
| **E3** (Task 3) | **NOT REACHED.** No correction appended at either site, no clause written beside D-431. Its arithmetic closes (§6.c) and its withdrawal is grounded at the tool (§6.d); §6.b is a gap in what it orders. |
| **E4** (the close) | **NOT REACHED.** No `STATUS.md` entry, no archive move, no close section, no end-state commit. **The end-state guard run WAS taken** and is recorded at §3.c; it is identical to the start state because nothing was edited. |

---

## 9. What this session did NOT do

- **No commit, no push, no staging.** `HEAD` = `origin/master` = `9390e2ca2c`, unmoved.
- **No `CLAUDE.md`, `STATUS.md`, `DECISIONS.md`, `OPEN_ITEMS.md`, `cowork_handoff.md`,
  `cowork_away_returns.md`, `cowork_audit_protocol.md` or ruling-record edit.**
- **No pin taken, no generator edited, no banner written, no document regenerated to a new content.**
  `tools/audit/nongating_apparatus_rows.json` and `OPEN_ITEMS.md` are **byte-unchanged** — neither is
  among the tracked modifications the enumeration reports, which is one modification and is
  `cowork_handoff.md`.
- **No open-items row created, flipped or discarded.** [[OI-372]] and [[OI-374]] stay exactly as
  found; [[OI-179]] stays OPEN and GATES; F3 stays surfaced, unfixed and unrowed.
- **No `src/` change, no golden, no test changed, moved or run, nothing under `tools/corpus/` or
  `tools/robust_stop/`, no measurement of the analysis.** No curated boot list, no archiving pass, no
  candidacy acted on, no census re-pin, no mining, no fact-gate admission, no findings ledger, no
  design, no repair, no derivation of any specification.
- **No new tool built**, so the new-tool rule does not arise.
- **The report is left UNTRACKED and UNCOMMITTED, deliberately.** Committing it would put a commit on
  `9390e2ca2c`, and the twenty-ninth handover block's branch rule reads exactly that as evidence the
  eleventh batch has started. Leaving it untracked keeps the branch rule's answer true.

---

## 10. What the writing side is owed, stated as questions rather than as recommendations

The record does not settle any of these, so no recommendation is made (**D-658**).

1. **F67 — how the eleventh batch's start state should be declared**, given that the dispatch's own
   inputs move a derived population before the batch begins. Whether the membership artifact's
   regeneration is an ordered act of Task 0 or of Task 1, and which, is a decision about a dispatch's
   own shape.
2. **F68 — which tool §6 kind 3 of the 2026-08-16 record meant**, and where Ruling 1b's two sentences
   should stand once the objects are named correctly.
3. **F69 — whether the pin derivation reads "its sitting" at date granularity or at the bound the
   sitting record's own landing commit supplies.** The four selected commits under the finer reading
   are at §5.b and are ready to be written the moment that is settled.
4. **F70 — whether the two figures with no generated home are withdrawn (as Ruling 3 already
   withdraws the percentage) or the generator is extended to derive them.**

---

## 11. The self-check over this session's whole effect on the tree (`CLAUDE.md`, the standing self-check)

The effect on the tree is one accidental write, restored in the same turn (§4), and one untracked
report file. **There is no diff to re-read** — the enumeration at §3.c is the check, taken after
everything above, and it reports the tree in the state assumption A1 describes.

Checked against the principles and the conventions: **#13** is what this report is (a surprise
surfaced as a STOP before anything was built around it); **#19** governs §5, which is why the
intervals and their strength are published rather than the pins being taken; **#12** governs §6.e,
where the corrected characterisation preserves the former one beside it; **#6** is why no figure and
no rule of another surface is restated here, only pointed at; **D-431** is why every figure above
enters by citation to a generated artifact or to a content-addressed object; **D-253** was obeyed —
every working-tree read went through the file tools, and every shell invocation was either a
content-addressed git object query, a git history query by path, or a committed measurement tool.
**Two shell invocations were refused by the armed guard** (a working-tree `git diff` and a `grep` at
a repository path); both were re-taken through the sanctioned route, and neither refusal was worked
around.

The reserved-word conventions bind this document: *measurement tool* never *instrument*, *the
open-items register* in full, *pitch* nowhere used loosely, and *TOWARDS* rather than *against*
wherever a rating is stated.

---

*Provenance: CC, 2026-08-18, executing — and stopping at the precondition of —
`cc_instruction_preparation_eleventh.md`. The batch is STOPPED, not complete and not partial. Every
commit hash above was read at the object; every character figure comes from
`tools/audit/session_start_read_size.json`; every guard figure from the two runs recorded at §3 and
§3.c; every history fact from a per-path git history query taken on this mount, which did not time
out here as it did on the writing side's.*
