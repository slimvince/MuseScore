# CC report — the preparation phase's TWELFTH batch: **COMPLETE**

> **Dispatch `cc_instruction_preparation_twelfth.md` (Cowork, 2026-08-19), read in full by CC on
> 2026-08-19.** Six task commits, Tasks 0 through 5, the close being a task commit with its own
> entry — plus ONE FURTHER commit carrying the end-state guard run, whose values this report does
> not state until **§14**, appended after that run and that commit exist.
>
> **Nothing in this report is a claim about the analysis.** No `src/` change, no golden, no test
> changed, moved or run, nothing under `tools/corpus/` or `tools/robust_stop/`, no measurement of the
> analysis built, designed, scoped or run. **No open-items row was created, flipped or discarded.**
> Every figure below is cited to a generated artifact or to a content-addressed git object, and none
> is transcribed from memory (**D-431**).
>
> **★ THE THREE THINGS TO READ FIRST, because they are what the writing side is owed.**
> **(1)** Task 3's enumeration returns **THREE UNPLACED MEMBERS** to the user as a standing
> STOP-and-report — §5.b. **(2)** Task 1's answer to what step 3 puts is that the derivation does NOT
> reach the blob and the artifact is left as it stands; that is data returned, not a defect — §3.c.
> **(3)** Five findings, **F82–F86**, one of which is this session's own — §10.

---

## 1. The reading

`CLAUDE.md` and `STATUS.md` **as they stood, in full**. `DECISIONS.md` in full — unconditional and
explicitly not demoted. `BUILD_AND_TEST.md` in full, because this batch MEETS its condition: it runs
the guard set, whose commands live there.

**The whole open-items INDEX was NOT read.** Rule (a)'s derived gating answer was read at
`tools/audit/nongating_apparatus_rows.json` → `★_the_live_gating_answer` → `gating_ids`, narrowed to
its identity list. **No verdict was challenged, so the grounds at `the_gating_rows` were not opened**
and no archive companion was reached.

**The standing clause was obeyed:** `cowork_handoff.md`, its **THIRTY-FIRST** block, was read. That is
what told this session the findings series stands at **F81** and that numbering begins at **F82**.

Then, as the dispatch orders, in full: `cowork_rulings_2026_08_19_eleventh_return.md`;
`cc_report_preparation_eleventh_amended.md`, its §3 and §11 above all; the **two ruling records Task 1
corrects** — `cowork_rulings_2026_08_15_inventory_sitting.md` and
`cowork_rulings_2026_08_17_rulings_sort_sitting.md`; `cowork_rulings_2026_08_18_eleventh_stop.md` and
`cowork_rulings_2026_08_18_tenth_return.md`; and `cowork_audit_protocol.md`'s dispatch-protocol
section in full, so that the four clauses already standing there were met before three more were
written.

The artifacts the dispatch orders binding at were read at their own text:
`tools/audit/evidence_pin_membership.json`, `tools/audit/guard_classification.json`,
`tools/audit/guard_state.json`, `tools/audit/session_start_read_size.json` and
`tools/audit/nongating_apparatus_rows.json`.

---

## 2. Task 0 — the four paths, and the membership check cleared in the same act

**`e3583c2720`, parent `46d68a146d`, pushed, 4 paths** (2 modifications, 2 additions; no staging
override).

### 2.a The declared start state matched at the tree

Taken **before any edit, at a quiet tree**, by `python tools/audit/gen_guard_state.py --check`
followed by `python tools/audit/gen_guard_classification.py --check`:

| | run | passing | failing | not run | historical | STOPs |
|---|---:|---:|---:|---:|---:|---:|
| declared by the dispatch | 71 | 69 | 2 | 4 | 16 | 0 |
| **measured, before any edit** | 71 | **69** | **2** | 4 | 16 | 0 |

Both reds are the ones the dispatch names with their causes —
`gen_filing_convention_application.py --check` ([[OI-372]]) and
`gen_evidence_pin_membership.py --check`, whose artifact is STALE because this dispatch's own
untracked ruling record already sits inside a derivation whose population is the file system. The
guard classification re-derives, exactly as declared.

**★ One thing the declaration does not name, and it is recorded rather than absorbed (F84's
neighbour, filed as F83).** The guard registry's own artifact does not re-derive at that tree either:
`gen_guard_state.py --check` opens with *"STALE vs the run"*, because the committed `guard_state.json`
records the previous batch's end state — one failing — while the tree has two. **It is the same
input's doing.** It is not a third failing check: this runner is not a subject of its own run, so its
staleness is not one of the 71 verdicts. **The declared start state is therefore MATCHED and no STOP
was owed.**

### 2.b Assumption A1 — HELD, checked first and entirely at content-addressed objects

`tools/audit/changed_paths.py` reports **exactly ONE tracked modification in the whole working
tree** — `cowork_handoff.md`. `tools/audit/evidence_pin_membership.json` is **not among the
modifications**, which is A1's expected-unmodified path holding, proven at the object
(`9db2ad03f6` at the terminus and at the tree).

| | blob |
|---|---|
| `cowork_handoff.md` committed at `46d68a146d` | `cbed24a27d8f93bb2122cfd643b87df012717652` |
| working copy, content-addressed | `bf31a8007ef93625792bc9bb23885e0035fbe845` |

The difference, measured blob against blob, is **ONE contiguous changed passage — 168 insertions and
1 deletion** — carrying both parts A1's own sentence names: the THIRTY-FIRST block inserted, and the
THIRTIETH heading's entry-point demotion marker, the single deletion being that heading in its
undemoted form. **No changed-passage count was asserted in advance** (the F25 lesson). **The F57
caveat was applied rather than assumed:** git's own check-in normalisation warning establishes the
working copy is stored LF, so the two blob hashes are directly comparable.

The two invariant paths were content-addressed in the same act and match the terminus:
`OPEN_ITEMS.md` at `6ae67d8603` and `tools/audit/nongating_apparatus_rows.json` at `5bb43d0b3a`.

**★ A1's untracked half is narrower than the tree, and it is reported rather than absorbed (F82).**
A1 says every untracked path other than the two it lands is *"the newly visible `cc_instruction_*.md`
files"*. The tree also carries newly visible `cc_*_report.md` and `cc_*_dossier.md` files and a
scratch directory. **No STOP is owed and none was taken**: A1's own stated STOP condition is scoped
to TRACKED paths — *"A modification at any OTHER tracked path is a STOP-and-report"* — and the
tracked half held exactly. This batch touched none of the untracked population.

### 2.c The regeneration's difference, measured before it was accepted

| | blob |
|---|---|
| committed at `46d68a146d` | `9db2ad03f658d5918b42bdb28a6a0e4dc0d1789c` |
| regenerated at this tree | `bb3a43237d5563a0e25969d0c3eb83216e4ce387` |

**NO VERDICT MOVED.** Members stay at **7**, pinned at **5**, UNRESOLVED at **0**; every member's
route, document, pin constant and state is byte-identical.

The difference is **TWO hunks, and the dispatch's prediction names both**:

1. `"ruling_records_read": 38` → `39` — route A, predicted.
2. One name added to `ruling_records_read` — route A, predicted.

**★ ROUTE B ADDS NOTHING AND THERE IS NO THIRD HUNK**, which is the writing side's own prediction
holding at the artifact. **This is Ruling 2's second clause working at the first dispatch written
after it was ruled**, and it is precisely the difference between this Task 0 and the eleventh
batch's, where the prediction was taken from one route only (F75).

At the tree this commit carries, `gen_evidence_pin_membership.py --check` prints *"the evidence pin's
class membership re-derives"*, so the guard set stands at **71 run, 70 passing, ONE failing** from
Task 0 onward.

---

## 3. Task 1 — the two separated members closed by naming the object

**`5f275463b0`, parent `e3583c2720`, pushed, 2 paths.**

### 3.a A3 checked first, per member, at the git objects — and it HOLDS for both

| member (generator) | ruling record corrected | the commit the record names | **the blob of the ruled rendering** | the object at this batch's Task 0 commit |
|---|---|---|---|---|
| `gen_artifact_inventory_surface.py` | `cowork_rulings_2026_08_15_inventory_sitting.md` | `b1d48d6c87` | **`d04aa5726b2cd9a398e093928f7d4bbe2b6063ff`** | `aa6157eb061955f584d3cd7a8ad7addc0c2d17f4` |
| `gen_rulings_sort.py` | `cowork_rulings_2026_08_17_rulings_sort_sitting.md` | `53e552296f` | **`dfbe91b747d1b967837d3d261e1b35737e6b3174`** | `5c62e70a387a6591d2474f147606000718ac4293` |

Both blobs were obtained at the object with `git ls-tree <commit> -- <path>` and both exist and
return content (`git cat-file -t` reports `blob` for each). **Neither was transcribed from the
dispatch**: the first reproduces the value the writing side established as the FACT it recorded, and
the second was derived at this act, which is what A3 required.

**The command each record publishes**, so a later reader fetches the object rather than trusting a
hash: `git cat-file blob <blob>` — content-addressed and self-verifying, git either producing that
object or erroring loudly — with `git show <commit>:<path>` producing the same object.

### 3.b The two dated corrections, appended, with nothing rewritten

Each names the blob, the commit it stands beside, **the derivation that produced the blob at the
objects**, and **the measured reason the pin is not applied**, re-established at the objects rather
than inherited from any earlier reading:

- **the artifact-inventory member** — the committed document has SEPARATED from the ruled rendering,
  so no single commit carries both the evidence of what was PUT and the document as the record now
  holds it, and fixing the generator's two input routes at the ruled commit would render a document
  that is not the committed one;
- **the rulings-sort member** — two facts, both re-derived here: `git ls-tree 53e552296f --
  cowork_rulings_2026_08_17_rulings_sort_sitting.md` returns **nothing** and that record is present at
  `570f2b63b1`, while the sort generator binds it as an input (`SORT_RULING`) and reads it for the
  sixty ruled placements, so a read of its inputs at that commit halts the tool; and the committed
  document is this sitting's own executing outcome, so reverting it would remove the user's own
  placements (#12).

**Each cites Ruling 1 of `cowork_rulings_2026_08_19_eleventh_return.md` and Ruling 1 of
`cowork_rulings_2026_08_18_tenth_return.md` as amended by Ruling 3 of
`cowork_rulings_2026_08_18_eleventh_stop.md`, and nothing else. NEITHER CITES D-230.**

**One further thing is stated at the inventory member's record and is worth naming here**, because it
is F80's own remedy applied one step earlier: the 2026-08-18 correction's *"at this tree"* reading is
given **the tree it was taken at**, rather than left to be reconciled against this batch's. The two
readings are of one document at two different trees and neither corrects the other.

### 3.c ★ What step 3 puts, ANSWERED: the derivation does not reach the blob, and the artifact is left as it stands

Step 3 admits the membership derivation picking the blob up **if and only if it DERIVES the blob from
the ruling record's own text, by the same structural route it already uses for the commit**, and
orders that if the derivation cannot reach it, the fact is stated and the artifact left alone.

**Read at the code, the derivation resolves ONE form and one only.** `gen_evidence_pin_membership.py`
matches a surface naming followed by *at commit `<hash>`*, inside the record's two structural blocks,
and publishes the commit alone. **There is no blob resolution of any kind**, so as it stands the
derivation does not reach the blob. Reaching one would be an added resolution form — the same
structural route with one more clause — and that is tool work which **blocks nothing**, which is the
standing mechanism freeze's own test. **A blob authored directly at the artifact is forbidden
(#6, D-431), and none was written.**

**MEASURED RATHER THAN ASSUMED, which is the load-bearing half.** With both corrections written,
`gen_evidence_pin_membership.py --check` re-derives — so the two records' new text moves no member,
no route, no document, no pin constant, no state and no count. **The corrections were written to that
constraint deliberately**: no new *at commit `<hash>`* form was introduced for either surface, and no
line carrying a form of *pinned* also carries a backtick-quoted tool name that the derivation's second
route would resolve. Both members remain recorded NOT PINNED and that state was not re-taken.

**The ruling record remains the authority either way**, which is what the step says.

### 3.d Nothing was pinned, restored, regenerated or reverted

All **seven** documents under `ratification_surfaces/` were content-addressed after the edits and
every one matches its committed object. The five members already carrying a pin are untouched. The
anchored-quote class did not fire — both edits are appends at end of file, so no cited coordinate
above them moved — and the drift authority reports **474/474** verbatim quotes at their cited home
and **468/468** cited line numbers correct.

---

## 4. Task 2 — the three standing clauses at one home

**`bd3961c975`, parent `5f275463b0`, pushed, 4 paths.**

All three land in `cowork_audit_protocol.md`'s dispatch-protocol section, in ONE edit, so the
anchored-quote class clears once instead of three times. **The placement of each is stated at the
site rather than left to be inferred:**

| clause | where it stands, and why | ground |
|---|---|---|
| Ruling 1's forward clause — the separated rendering | immediately after the clause saying a ruling record names the COMMIT, because it says what the same record carries once the commit alone no longer reaches the rendering | **F76** |
| Ruling 2's second clause — a prediction from every route | immediately after the declared-start-state clause, and says in terms that it is the second half of the same lesson | **F75** |
| Ruling 2's sharpened bar — movement versus addition | beside those two, all three governing one moment: a dispatch's ordered check over an artifact its own act regenerates | the measured episode, with the alternative declined recorded beside it |

Each carries its general form. The sharpened bar's is *enforcing a bar past its own stated purpose is
how a STOP becomes ritual rather than a guard*, and it records that the narrowing is stated in terms —
**added, derived, and caused by the ordered act** — rather than left as discretion, because a STOP
condition exists to remove a judgment from the executing side (**D-251**'s shape).

**The anchored-quote class fired and was cleared by its ruled treatment.** 27 register home anchors
drifted, all into this file and all by the same shift; every one was re-aimed **per citation** from
the drift report's own reported start line, never by an assumed uniform shift. The drift authority
now reports **474/474** and **468/468**, against **441/468** before the re-aim.

**Every regenerated artifact's own difference was measured before it was accepted**, blob against
blob:

| artifact | before → after | difference | every changed line carries a `cowork_audit_protocol.md` coordinate |
|---|---|---|---|
| `tools/audit/decisions/backbone_decisions.json` | `514d1ee3ea` → `ec760474d6` | 27 insertions, 27 deletions | 54 / 54 |
| `decisions/group_T.md` | `2ce843999a` → `ca85557b1f` | 27 insertions, 27 deletions | 54 / 54 |
| `tools/audit/rulings_sort_classification.json` | `fa2c43f608` → `2ab15465ce` | 54 insertions, 54 deletions | 108 / 108 |

**Counted rather than sampled.** The sort artifact's count is twice the others because each entry
carries the coordinate in two fields. `DECISIONS.md` itself is **byte-unchanged**, the INDEX naming
homes without a line, and **no other group file moved**.

**★ One departure declared rather than absorbed (F85).** The sort generator has ONE write path for
TWO outputs, so regenerating the classification artifact the ruled treatment requires also rewrites
the ruling surface it renders. **The surface came out BYTE-IDENTICAL to its committed object
`5c62e70a38`, proven rather than assumed**, so no document under `ratification_surfaces/` differs
from its committed bytes — the enforceable bar is met. This is the write-path family Task 3
enumerates, met inside another task.

---

## 5. Task 3 — the write-path asymmetry, enumerated and published as data

**`25cde8bc62`, parent `bd3961c975`, pushed, 5 paths.**

### 5.a The derivation, and what it is bounded by

The population is **DERIVED from the tools' own syntax trees, never hand-listed**. Every `*.py` under
`tools/` is parsed; a **member** is a pass whose `--check` path reads a commit back out of one of its
**own** outputs — the epoch shape **D-646** names — and the verdict is what its **write** path does
instead: **SYMMETRIC** where it reads the same recorded commit back, **ASYMMETRIC** where it carries
the literal `HEAD`, **UNPLACED** where it carries neither.

The artifact `tools/audit/epoch_write_path.json` states its own bound, as the ruling's execution
requires: it reads **SOURCE and never a run**, so it cannot tell an asymmetric member that would
merely DIFFER from one that would STOP — that turns on the population the pass reads at `HEAD`, and
**that an asymmetric run may STOP rather than differ is F77's measured instance**; it reads the
statements of `main` only, so a commit resolved inside a callee is invisible; it reads a tool's OWN
outputs, so a pass pinned at another tool's recorded commit is outside the population by
construction; a computed key or path carries no literal to find; and **the recognizers' reach beyond
the two establishment seeds is UNMEASURED and said so.**

**Established (#19) on two seeds, one per verdict, re-checked on every run:**
`gen_ratified_document_check.py`, corrected to the symmetric shape at the eleventh batch and declared
there, and `gen_artifact_inventory.py`, whose write path resolves `HEAD` unconditionally — read at
the code this session, not taken from a report. **A seed that stops deriving to its established side
HALTS the run** rather than letting a smaller population be published.

### 5.b ★ The result — and the three UNPLACED members returned to the user

**7 members over 338 tools walked: 1 SYMMETRIC, 3 ASYMMETRIC, 3 UNPLACED.** The identities and every
per-member field are at `tools/audit/epoch_write_path.json` and are not restated here (**D-431**),
with one exception the dispatch's own step 1 requires — the UNPLACED members are a STOP-and-report to
the user and are therefore named:

- **`tools/audit/gen_discard_reach_split.py`** and **`tools/audit/gen_phase1_gate_readers.py`** — the
  write path calls the builder with NO argument, so the resolution is the builder's own default and
  sits outside `main`. What `main` DOES show is that the two paths pass different things: the check
  path passes the recorded commit explicitly, and the write path passes nothing.
- **`tools/audit/gen_retirement_caller_check.py`** — the write path takes the commit from the command
  line (`--at <commit>`) and REFUSES to write without one, on its own stated ground that the reading
  is a statement about one tree and the commit is part of the finding. It resolves neither the
  recorded commit nor `HEAD`, and the shape is a third one this recognizer does not name.

**None is guessed into a verdict.** What makes this a guard rather than a note is the both-ways
reconciliation between the derived unplaced set and the authored reasons — **an unplaced member with
no authored reason HALTS the run, and an authored reason the derivation now places halts it too** —
and **that STOP fired for real during the task**, on the third member, which the first authored pair
did not carry.

### 5.c This task corrected nothing, and the new-tool rule is discharged in the same commit

**No write path is corrected, no enumerated pass is edited, no member is acted on, and no member is
owed by appearing in the artifact.** The published enumeration is the standing input to a later ruled
act, never a work list.

The derivation needed a new measurement tool, so the new-tool rule was discharged in the same commit:
the authored run-instruction in `gen_guard_state.py` and the authored classification verdict in
`gen_guard_classification.py`. **The guard count rises by exactly that one invocation, 71 to 72** —
measured at a full run, which returns **72 run, 1 failing**, the one failing being [[OI-372]]'s tool
and no other. `guard_classification.json` was regenerated and its difference measured blob against
blob (`fdbe820ea2` → `2c392253c3`): **two counts up by one and one row added, and nothing else.**

**★ One cell is declared rather than quietly left (F86).** The new row's
`state_at_the_committed_tree` reads `unknown`, because the classification reads each tool's state off
the COMMITTED guard registry rather than re-running it (#6 — one runner), and that record predates
the tool. The registry's write-mode regeneration is a full guard run, taken at the quiet tree the
close leaves and recorded at §14.

---

## 6. Task 4 — the two corrections of record

**`18127bab01`, parent `25cde8bc62`, pushed, 2 paths.**

### 6.a The load-bearing one (F80), at §3.c of the eleventh batch's report

The *"at HEAD"* column was measured at the tree Task 1 met **before its own edits**. Every object
enters **BY CITATION to the git object**, obtained with `git rev-parse <commit>:<path>` and never
transcribed from any surface that repeats it (**D-431**):

| `tools/audit/gen_artifact_inventory_surface.py` at | object |
|---|---|
| `b1d48d6c87` (the selected commit) and `9390e2ca2c` (that batch's base) | `9a98c9672912fbe1dcda2c93b7b300025bf22bde` |
| `9a78ed2fea` — **that batch's Task 1 commit** — onward | `610a3fbe78085406fac69ab0931ce0c2abd1e7e9` |
| `65fbef6df4` — **that batch's Task 3 commit** — onward, and at the terminus `46d68a146d` | `e985f5d7047a70067d3314889ed1e51269134fd1` |

**The conclusion SURVIVES and is STRENGTHENED; only the inference is corrected.** §3.c's conclusion —
the pin is not applied because the committed document is no longer the ruled rendering — stands
untouched. What no longer holds is the reasoning that a render at the selected commit would produce
`d04aa5726b` *exactly*: that rested on the generator being one object at both commits, and it is two.
**A render today would produce NEITHER the ruled rendering NOR the committed document**, which is a
stronger ground for not pinning than the one §3.c gave. The census input is unmoved and that half of
§3.c stands as written — `tools/audit/artifact_inventory.json` is
`dc7d15e7b44e07386b03ef5e9df46ac40ed2f319` at both `b1d48d6c87` and the terminus.

### 6.b The small one (F81), at both sites carrying the count

The report's opening block and the close's own statement, **both former wordings quoted and preserved
(#12)**. **There are SIX task commits and SIX `STATUS.md` pointer entries** — Tasks 0 through 5, the
close being a task commit with its own entry — and **the corrected count is stated BY CITATION to the
enumeration**: the chain table at §13 of that report carries one row per task commit plus two further
rows, and the pointer entries are enumerated at `STATUS.md`'s own eleventh-batch entries.

**Neither site's own text is rewritten**; a report and a close are both corrected by appending. The
anchored-quote class did not fire, and the drift authority reports **474/474** and **468/468**.

---

## 7. Task 5 — the close

**Six `STATUS.md` pointer entries, one per task**, and **in the same act Ruling 4's forward bound
moves the ELEVENTH batch's entries verbatim to `STATUS_ARCHIVE.md`**. `gen_status_batch_bound.py` was
re-aimed at this batch's own base commit `18127bab01`, its previous aiming kept rather than replaced
(#12). The tool reports **6 entries moved, 8,489 characters**, and **both directions proven**: every
moved entry byte-present in the archive exactly once, and every moved entry absent from the must-read.
**The declared `Last updated: ` prefix adjustment is IMPORTED and not re-decided (#6)**, and no entry
needed a second adjustment — the tool's own occurrence test would have STOPPED on one.

The FULL close is appended to `cowork_away_returns.md` as **THE PREPARATION TWELFTH BATCH**, and **it
does not assert the end state**: a block at its head states that the end-state run is taken after the
commit carrying it exists and that its values land in ONE FURTHER commit.

---

## 8. The registered expectations

| | verdict |
|---|---|
| **E0** | **MET.** Exactly 4 paths — two modifications matching A1's shape and the bounded regeneration, two additions, no staging override — and the membership check passing at the resulting tree, so the guard set stands at 71 run, 70 passing, ONE failing from Task 0 onward. **The prediction held on BOTH routes**, with no third hunk, which is the difference between this Task 0 and the eleventh batch's. |
| **E1** | **MET.** Both members' ruled renderings are named by blob with the command that obtains them; each written as an appended correction with nothing rewritten and neither citing D-230; each member's NOT PINNED state carries its measured reason, re-established at the objects; no pin taken and no document under `ratification_surfaces/` differing from its committed bytes; `OPEN_ITEMS.md` byte-unchanged. The question step 3 puts is ANSWERED as data — the derivation does not reach the blob and the artifact is left as it stands, which is that step's own second branch. |
| **E2** | **MET.** Three clauses stand at the dispatch-protocol section, each with its named ground and its general form; no other authoring rule moved; the drift authority reports every re-aimed anchor correct at its new coordinate. |
| **E3** | **MET.** The population is derived and published with its own bound; every member is placed or STOPped on, with three UNPLACED members returned to the user; no write path corrected and no member acted on; the new measurement tool registered in the act that created it, and the guard count's movement caused and named. |
| **E4** | **MET.** Both corrections stand as appended dated notes with the former wording quoted and preserved and nothing rewritten; every object named enters by citation; the conclusion of §3.c is stated to survive and only its inference is corrected. |
| **E5** | **NOT GRADED IN THIS COMMIT, BY DESIGN.** The end-state run is taken after the commit carrying this report exists, and its values and E5's grade land in ONE FURTHER commit as §14. Grading it here would be the very defect **F79** records. |

---

## 9. The declared departures

1. **A new measurement tool was built under the standing mechanism freeze** (Task 3), declared as a
   judgment at the site, in the commit message, in the close and here. The freeze bars tool work
   *that does not block the work*, and a DERIVED enumeration published as data is not performable
   without one; the dispatch's own step 4 anticipates it.
2. **A generator with one write path for two outputs also rewrote a ruling surface** (Task 2); the
   surface came out byte-identical, proven rather than assumed (F85).
3. **One cell of `guard_classification.json` reads `unknown`** (Task 3), declared with its cause
   (F86).
4. **The guard registry and its classification are regenerated in the further commit**, at the quiet
   tree, together with the end-state run that produces their values — never before it.
5. **Working-tree files were content-addressed into the object database** (`git hash-object -w`) so
   that both sides of every blob comparison are content-addressed — the route the tenth and eleventh
   batches' reports used, imported rather than re-invented.
6. **Per-path git object queries at explicit hashes** were used for every establishment; they did not
   time out on this mount.

---

## 10. Findings, numbered from **F82** as the thirty-first handover block allocates — surfaced, not rowed

The dispatch bars creating an open-items row and this session created none. **None of the findings
below bears on the analysis, its inputs, or a measurement tool the analysis depends on** — every
subject is the project's own record and the apparatus that reads it.

- **F82 — A DISPATCH'S ASSUMPTION NAMES THE UNTRACKED POPULATION MORE NARROWLY THAN THE TREE CARRIES
  IT.** A1 calls every untracked path other than the two it lands *"the newly visible
  `cc_instruction_*.md` files"*; the tree also carries newly visible `cc_*_report.md` and
  `cc_*_dossier.md` files and a scratch directory. **No STOP is owed and none was taken** — A1's own
  STOP condition is scoped to tracked paths, and the tracked half held exactly. **The general form:
  an assumption about a file-system population is checked against the population, not against the
  class the sentence happens to name.** F67's family, one step further out. §2.b.
- **F83 — THE DECLARED START STATE NAMES THE GUARD VERDICTS BUT NOT THE GUARD REGISTRY'S OWN DRIFT,
  WHICH THE SAME INPUT CAUSES.** The dispatch declares two reds with their causes and states that the
  guard classification re-derives; it does not say that the registry artifact itself does not.
  **The general form: a declaration that names the VERDICTS of a run must also name the state of the
  RECORD of that run, where the same input moves both** — the declared-start-state clause's own
  neighbour. §2.a.
- **F84 (this session's own) — A RECOGNIZER BUILT FROM ITS KNOWN INSTANCES RECOGNISES ITS KNOWN
  INSTANCES.** Task 3's derivation was first written from the two members the record already
  establishes, and it reproduced both — while missing three real idioms the same population uses: a
  check flag bound to a local name, an artifact read through a `with open(OUT) as fh` handle, and a
  builder called with no argument. **Published as written it would have named three members instead
  of seven and read as complete.** Each miss was found only by seeking candidates the recognizer did
  NOT return. **The general form: a recognizer's reach is measured by the instances it FAILS to find,
  never by the ones it does; a seed set proves the recognizer is not broken and says nothing about
  what it covers.** §5.a.
- **F85 — A BAR ON AN ACT AND A BAR ON A RESULT DIVERGE WHEREVER ONE WRITE PATH SERVES TWO OUTPUTS.**
  *No ratification document is opened for writing* and *no ratification document differs from its
  committed bytes* are the same demand until a generator writes a derived artifact and a ruling
  surface in one call. **The general form: where one write path serves two outputs, only the
  byte-level bar is checkable, and a bar phrased as an act must say which of the two it means.** §4.
- **F86 (small) — A CLASSIFICATION DERIVED FROM A RECORD OF A RUN CANNOT STATE THE STATE OF A TOOL
  CREATED AFTER THAT RECORD.** **The general form: a derived view whose input is a RECORD OF AN EVENT
  describes nothing that came into being after the event.** §5.c.
- **F1–F81 ride to the preparation phase's retrospective unchanged**, with the E3 ordering defect and
  the A1 premise error. **F3 FIRED AGAIN, in Task 2** — `reaim_home_anchors.py --check` exited 0
  while printing 27 drifted anchors — and stays surfaced, unfixed and unrowed; the dispatch records
  the count as fourteen at its writing, and this batch is one further surfacing.
  `gen_cluster_dispositions.py --verify` was the drift authority throughout. **F25 did not repeat**;
  **F57 was applied rather than assumed** at §2.b; **F79 did not repeat** — the end state is not
  asserted in the close.

---

## 11. What the writing side is owed, stated as questions rather than as recommendations

The record does not settle these, so no recommendation is made (**D-658**).

1. **The three UNPLACED members of the write-path enumeration** (§5.b): each is published with the
   shape the derivation CAN see and the reason it can see no further. Is anything wanted for them,
   and if so, is it a widened recognizer or a per-member reading? Nothing is owed by their appearing,
   and the ruling says each pass is corrected only when a ruled act needs its write path.
2. **Whether the membership derivation should ever pick the blob up** (§3.c). It cannot as it stands;
   one added resolution form of the same structural route would reach it; nothing is blocked either
   way, so it is a question about what the artifact should carry, not about what is owed.
3. **F84's consequence for every recognizer this arc has built.** The reach of this one is UNMEASURED
   and says so. Whether the same is true of the other recognizers over prose and code that the record
   already leans on is not established here.

---

## 12. The self-check over this session's whole diff (`CLAUDE.md`, the standing self-check)

The diff of every touched file was re-read before this report was written, not the memory of writing
it. Checked against the principles, the conventions and the gate and threshold policies:

**#12** governs every correction: no ruled text is rewritten, every superseded wording and every
overtaken reading is quoted and preserved beside its replacement, and the one act that would have
destroyed a user's own ruled placements was refused on that ground and named as the reason a pin is
not constructible. **#19** governs the new derivation: its establishment is two seeds re-checked on
every run, its reach beyond them is declared UNMEASURED, and the members it cannot place are returned
rather than guessed. **#13** is what §5.b is — a surprise surfaced as a STOP before anything is built
around it. **#6** is why three clauses landed at ONE home, why no figure of another surface is
restated here, and why the blob's one home is the ruling record. **#15** is why every commit was
verified at the object and every difference taken between two content-addressed objects. **D-431** is
why every figure enters by citation. **D-253 was obeyed** — every working-tree read went through the
file tools, and every shell invocation was a content-addressed git object query, a per-path git
query, a git write, or a committed measurement tool. **Three shell invocations were refused by the
armed guard** (a directory listing and two interpreter bodies naming repository paths); each was
re-taken through the sanctioned route and none was worked around. **One write was attempted through
shell redirection and abandoned rather than retried**: the close was written with the file tools, the
recorded 2026-08-02 slip not repeated.

**The reserved-word conventions bind this document**: *measurement tool* never *instrument*, *the
open-items register* in full, *value* rather than the numerical sense of the collided word, and
*TOWARDS* rather than *against* wherever a rating is stated. **The vocabulary rule of 2026-08-17
binds every line written this batch.**

**Nothing this batch did touches the analysis, its inputs, or any measurement tool the analysis
depends on.**

---

## 13. The chain, and where the end state is NOT

| | commit | parent | paths |
|---|---|---|---|
| Task 0 | `e3583c2720` | `46d68a146d` | 4 |
| Task 1 | `5f275463b0` | `e3583c2720` | 2 |
| Task 2 | `bd3961c975` | `5f275463b0` | 4 |
| Task 3 | `25cde8bc62` | `bd3961c975` | 5 |
| Task 4 | `18127bab01` | `25cde8bc62` | 2 |
| Task 5 — the close and this report | the commit that carries this section, whose own identity it cannot contain | `18127bab01` | — |

Every commit named above was verified at the object by explicit hash — its parent confirmed and its
path count read from the object, never from the memory of making it (**#15**).

**★ THE END STATE IS NOT IN THIS SECTION, AND THAT IS DELIBERATE.** The end-state guard run is taken
AFTER the commit carrying this report exists, at the quiet tree it leaves; **its values, the sequence
that produced them, and E5's grade land in ONE FURTHER commit as §14 below.** No row, no cell and no
sentence here states what that run returned. **This is the E-ordering rule at the smaller grain the
eleventh batch's F79 records** — the rule is not satisfied by taking the run late if the sentence
about the run was written early, and the cheapest test of whether it has been obeyed is whether the
sentence could have been wrong.

---

*Provenance: CC, 2026-08-19, executing `cc_instruction_preparation_twelfth.md`. Every commit hash
above was read at the object by explicit hash; every blob comparison was taken between two
content-addressed objects; every guard figure in §2.a and §5.c comes from the run recorded there;
every history fact from a per-path git object query taken on this mount. **No end-state value is
stated in the commit that carries §1–§13.***

---

## 14. The end state — appended AFTER the run that produced it, in the ONE FURTHER commit

**The close commit is `e96d80b550`, parent `18127bab01`, pushed, 6 paths** — verified at the object,
its parent confirmed and its path count read from the object. Its own identity could not be written
into it, which is why it is stated here.

**THE SEQUENCE IS RECORDED RATHER THAN THE SUMMARY, because the sequence is the evidence.** Every run
below was taken at the quiet tree the close commit left, and every value was read off the run, never
inferred:

1. **`gen_session_start_read_size.py --check` went RED on the first end-state run** — *"STALE vs the
   measurement"* — **expected, and F79's own instance**: Task 5's close moves `STATUS.md`, a member of
   the read that tool measures. **Cleared by regenerating the measurement and by nothing else**; the
   re-check then prints *"the session-start read measurement re-derives"*.
2. **The full guard set then returned: `72 guard(s) run, 1 failing, 4 not run, 16 historical
   record(s)`** — the ONE failing being `[FAIL] tools/audit/gen_filing_convention_application.py
   --check`, [[OI-372]]'s tool and no other — with **ZERO STOPs**, and
   `gen_guard_classification.py --check` printing *"the guard classification re-derives"*.
3. **The guard registry was then regenerated in write mode at that same tree**, and the
   classification after it. `gen_guard_state.py --check` now prints **"the guard state re-derives"**,
   which it did NOT at this batch's start state (§2.a's F83), and the classification re-derives with
   it. **The `unknown` cell of §5.c is resolved to `PASS`** — the new measurement tool's own state at
   the committed tree, which is what the registry regeneration was declared for at §9.4.

| | run | passing | failing | not run | historical | STOPs |
|---|---:|---:|---:|---:|---:|---:|
| start state, before any edit | 71 | 69 | 2 | 4 | 16 | 0 |
| **end state, at the quiet tree the close left** | **72** | **71** | **1** | 4 | 16 | **0** |

**The guard population rose by exactly one invocation**, which is Task 3's new measurement tool
registered in the act that created it, and the two start-state reds are down to the one standing red
the record already carries.

**E5 — MET**, on that run and on nothing else.

**★ THIS SECTION WAS WRITTEN AFTER THE RUNS AND AFTER THE CLOSE COMMIT EXISTED**, and the commit
carrying it cannot contain its own identity — the regress ends where the record's own precedent ends
it, with git carrying what a sentence cannot. **No sentence asserting the end state was written
before the run that produced it existed**, which is the E-ordering rule at both grains and the
remedy F79 names.

*Provenance: CC, 2026-08-19, appended in the ONE FURTHER commit after `e96d80b550`. Every value in
this section was read from the runs recorded above at the quiet tree that commit left; the close
commit's hash, parent and path count were read at the object by explicit hash.*

---

## 15. The whole chain, named as far as a sentence can name it — and the one commit it cannot

**Written because the eleventh batch's own terminus was a commit no close and no report named**, and
a reader who took the close's provenance as naming the last commit was one commit short. That hazard
is reduced here to the single commit the regress cannot escape, and it is DECLARED rather than left
to be discovered.

| | commit | parent | paths |
|---|---|---|---|
| Task 0 | `e3583c2720` | `46d68a146d` | 4 |
| Task 1 | `5f275463b0` | `e3583c2720` | 2 |
| Task 2 | `bd3961c975` | `5f275463b0` | 4 |
| Task 3 | `25cde8bc62` | `bd3961c975` | 5 |
| Task 4 | `18127bab01` | `25cde8bc62` | 2 |
| Task 5 — the close and this report | `e96d80b550` | `18127bab01` | 6 |
| the end-state guard run, the ONE FURTHER commit — §14 and the three artifacts | `1530162032` | `e96d80b550` | 4 |
| the close's own end-state block, appended after the run existed | `10921a0cb0` | `1530162032` | 1 |

**Every row was verified at the object by explicit hash** — its parent confirmed and its path count
read from the object, never from the memory of making it (**#15**). **This table was written after
all eight commits existed.**

**★ THE COMMIT THAT CARRIES THIS SECTION IS THE TERMINUS, AND IT IS THE ONE ROW THE TABLE CANNOT
HOLD.** A commit cannot contain its own identity, so the chain is complete up to it and one commit
short of the branch tip **by construction, not by omission**. **Read the chain at the branch tip, not
at this table** — that is the whole content of the warning, and it is stated here so that no later
session has to rediscover it.

*Provenance: CC, 2026-08-19, appended in the commit that is this batch's terminus. Every hash above
was read at the git object by explicit hash.*
