# CC report — the preparation phase opens

> **What this is.** The coding side's report on `cc_instruction_preparation_opening.md`, performed
> 2026-08-15. The batch record beside it is THE PREPARATION OPENING section of
> `cowork_away_returns.md`; this file is the whole of what the coding side says back.
>
> **THE HEADLINE, BEFORE ANY DETAIL.** All four tasks are performed. The nineteenth handoff block
> and this dispatch are landed; the stale twelfth heading is demoted; the decisions-register filter
> is DERIVED onto a ruling surface with **nothing discarded**; and the caller-check at the objects
> is RUN over every ruled retirement candidacy with **nothing archived**.
>
> **TWO THINGS THE USER SHOULD READ BEFORE ANYTHING ELSE.** *(1)* **The caller-check's answer is
> that the check as the dispatch specifies it cannot yet discriminate** — every candidacy comes back
> HELD-BY-CALLERS, and the naming is mostly done by artifacts that enumerate the tree. The question
> that would make it discriminate is stated and NOT decided (§4.c). *(2)* **The filter proposes a
> soft-discard class large enough that its size is itself a decision surface**, and Ruling 8's second
> limb — decision, or observation of what the code does — is a question about content that no
> recognizer settles, so it is put to the user with the evidence to answer it (§3.c).
>
> *(Every guard count lives at `tools/audit/guard_state.json`; every classification count at
> `tools/audit/decisions_filter_classification.json`; every caller-check value at
> `tools/audit/retirement_caller_check.json`. None is restated here beyond the few this report is
> reporting ABOUT, each naming where it was read — **D-431**.)*

---

## 1. Both guard-set states

- **START, before the first act:** `gen_guard_state.py --check` printed **"the guard state
  re-derives"** — **48 guards run, 47 passing, ONE failing**
  (`gen_filing_convention_application.py --check`, which is [[OI-372]]), 4 not run, 10 historical
  records, **no STOP**. `gen_guard_classification.py --check` printed **"the guard classification
  re-derives"**. **This is exactly the start state the dispatch declares as expected**, so no
  STOP-and-report was owed on it. The sanctioned enumeration reported **exactly one tracked
  modification** — `cowork_handoff.md` — with `cc_instruction_preparation_opening.md` untracked,
  which is assumption **A1**'s second limb.
- **END, after both new checks were added and registered:** **50 run, 49 passing, ONE failing**
  ([[OI-372]]'s tool), 4 not run, 10 historical, **no STOP**; `gen_guard_classification.py --check`
  — **"the guard classification re-derives"**. The two checks this batch adds are inside the
  classified population under authored verdicts, and both PASS.
- **E5's run, taken at the tree carrying the close and after the commit that carries it**, is
  recorded at §6 — **run and read, never inferred, and its values committed only after the run.**

---

## 2. Tasks 0 and 1 — the handoff file

### 2.a A1's check — CONFIRMED exactly as stated, entirely at content-addressed objects

The committed blob **`f64837573c`** was resolved from `02636987b0:cowork_handoff.md` and diffed
against the working blob **`1bb96d838e`** produced by `git hash-object`, so neither side of the
comparison is a shell read of a working-tree file (**D-253**). Both hashes are the ones the
dispatch's premise names, to the digit.

**The difference is 101 insertions and 1 deletion, ONE contiguous changed passage**, and it carries
exactly the two parts the premise names as two parts of one act: the nineteenth block inserted above
the eighteenth, and the eighteenth block's heading demoted — `THE CURRENT ENTRY POINT.` replaced by
`(SUPERSEDED as the entry point by the nineteenth block above.)`. Nothing else differs. **The ordered
STOP was not reached and no judgment was needed to say so.**

*One detail worth recording because it bears on how the premise was checked rather than on its
truth:* the two parts are adjacent in the file, so the version history reports them as ONE changed
passage rather than two. The premise's own wording — two parts of one act — is what made that
expected rather than a discrepancy to reconcile.

**That `02636987b0` was the current committed state is established at the object rather than assumed:
it is the parent of the Task-0 commit**, which is what a branch-tip read could not have established
(D-253).

### 2.b Task 0's commit — `54eb257a6f`, pushed

Exactly the two paths the dispatch names and no third — `cowork_handoff.md` (modified) and
`cc_instruction_preparation_opening.md` (new) — verified at the index through the sanctioned
enumeration before the commit (2 records: one `M`, one `A`) and at the object after it. **Parent
`02636987b0`.** The dispatch was staged **PLAINLY**, no `-f` and no override of any kind.

**Registered expectation E0 — MET on all three limbs:** exactly 2 paths at `git diff-tree`;
`cowork_handoff.md` numstat **101 insertions, 1 deletion**; no staging override.

### 2.c Task 1 — the stale twelfth heading demoted. Commit `a150bd8acf`, pushed

The twelfth block's heading closed with `THE CURRENT ENTRY POINT.` seven blocks after it stopped
being one. Its closing sentence is replaced by
`(SUPERSEDED as the entry point by the thirteenth block above.)` — the marker the file's own
convention uses everywhere else — and nothing else in the file moves.

Verified blob against blob by explicit hash before the commit: committed **`1bb96d838e`** resolved
from `54eb257a6f:cowork_handoff.md`, working **`e66311e48f`** from `git hash-object -w`.

**Registered expectation E1 — MET on every limb.** ONE path; ONE changed passage; **1 insertion and
1 deletion**; confined to the twelfth block's heading line and nowhere else. After the edit
`THE CURRENT ENTRY POINT.` occurs in the file **exactly twice** — in the nineteenth block's heading,
and inside the nineteenth block's carried-findings sentence, which QUOTES the stale heading this
task removes. **A quotation is inert and stays**, which is what the expectation registered.

---

## 3. Task 2 — the decisions-register filter. Commit `0a2cc3f86a`, pushed, seven paths

### 3.a What was built, and what is derived in it

`tools/audit/gen_decisions_filter.py` walks **every** entry of the decisions register's data file
and, per entry, extracts the evidence bearing on whether a deciding act can be named — the recorded
ratifier, the recorded date, a ruling record or ratification event named, a user-act marker, an
explicit no-ratifier clause, harvest-source provenance — **quoting each value from the entry's own
recorded text and inferring none**. It proposes exactly one class per entry from the dispatch's own
three-value vocabulary, which the tool may not widen.

**DERIVED:** the population; the rendered INDEX's entry identities, reconciled with it in BOTH
directions; every quoted evidence value; the status vocabulary, read from the data file's own header;
every count. **AUTHORED:** the recognizer patterns and the classification rule — both published in
the artifact beside the verdicts they produced, so the rule can be checked against the evidence
without opening the tool.

**A2's check — CONFIRMED, and it is a STOP rather than a report.** The data file and the rendered
INDEX carry the same entry identities in both directions. A disagreement either way halts the tool
before it writes, so a committed artifact reporting a reconciled population is the only kind that can
exist (**D-671** — a derivation over a derived population is published whole or not at all).

### 3.b The rule's one judgment call, declared rather than buried

A recorded **date** with nothing naming an actor, a ruling record or a ratification event says WHEN
and not WHO or WHERE. **The rule sends that case to EVIDENCE-AMBIGUOUS rather than to either
outcome**, and the reason is on the surface: Ruling 8 licenses a soft-discard only where no deciding
act can be NAMED and a bare date names none, while reading a date as *no act* would be the guess the
phase's stop rule forbids. It is the one place the rule chooses, and it chooses the direction that
returns to the user.

### 3.c ★ WHAT THE USER MUST DECIDE, AND WHY THE TOOL DOES NOT

**Ruling 8 has two limbs and this tool settles only one.** Its operative clause is *no deciding act
can be named* — a question about provenance, which the recognizers answer. Its gloss is *a decision
ABOUT the code is legitimate; what is not a decision is an observation of what the code does* — a
question about **content**, which no recognizer answers.

So the surface does not ask the user to trust a verdict. **Every proposed SOFT-DISCARD and
NEEDS-THE-USER member is listed with its quoted evidence, its plain restatement, and the source the
entry gives for its status** — enough to apply the second limb by reading rather than by opening the
register. Where that reading finds a decision, the entry belongs in the live record whatever its
provenance field says, and the listing is the place to say so.

**Two further things are stated on the surface because a reader must meet them before the
proposals.** The **register-level ratification events supply no ratifier the original record never
had** — `DECISIONS.md`'s own preamble says exactly that, and it is quoted, because it is the
strongest counter-consideration to the whole classification. And **the observation-shape limb's
reach is UNMEASURED (#19)**: two mechanical signals for it are extracted, and an entry's absence from
that limb is not evidence that it is not an observation.

### 3.d One disagreement found while walking the population, RECORDED and not repaired

The data file's header declares a status vocabulary; its entries use a spelling of one of those
values that the header does not carry. **The status field is not an input to the classification, so
nothing here turns on it** — but a walk of the whole population found it, and a finding is surfaced
rather than smoothed away. The comparison normalizes whitespace on BOTH sides so the classification
could proceed, and **nothing was repaired**: this batch edits no register file, and a disagreement
between a record and what it describes is evidence, which is the rule the user ruled into `CLAUDE.md`
in place of D-231's truth half.

### 3.e The register's own files are byte-unchanged, proven by hashing

`DECISIONS.md`, **all twenty** `decisions/group_*.md` files and
`tools/audit/decisions/backbone_decisions.json` were each hashed against their committed blobs at
`a150bd8acf` after the run. **Every one is byte-identical.** No entry was retired, edited, moved or
marked, and no soft-discard was executed.

### 3.f The five STOPs, each shown able to fire

Each is exercised by a probe in the artifact, and **every probe calls the very function the walk
calls**, so the two cannot drift apart: an entry missing a field the classification reads; a
duplicate entry identity; a disagreement with the rendered INDEX, in each direction separately; a
status outside the declared vocabulary; a distribution that does not account for the population. All
raise.

**★ ONE OF THEM FIRED FOR REAL, ON THE FIRST RUN, AND THAT IS HOW §3.d WAS FOUND.** The status-
vocabulary STOP halted the tool on a live entry rather than on a probe. It was answered by declaring
the comparison, not by editing the data.

**Registered expectation E2 — MET on every limb.** The artifact classifies the whole population, each
entry in exactly one class with quoted evidence; the register's rendered and data files are
byte-identical to their committed blobs; `--check` re-derives on a second run.

---

## 4. Task 3 — the caller-check at the objects. Commit `0305d495bb`, pushed, six paths

### 4.a The population, derived twice over and hand-listed nowhere

`tools/audit/gen_retirement_caller_check.py` derives the nine ruled candidacies — six whole classes
and the flagged side of three citation splits — by **importing** the retirement flags from
`gen_artifact_inventory_surface.py`'s own authored table rather than restating them (**#6**), so this
check and the ruling surface cannot disagree about what is flagged. Every member path comes from the
committed inventory. The ruled **condition** per candidacy is authored and carries the sentence of
`cowork_rulings_2026_08_15_inventory_sitting.md` it was read from — and **every one of those
sentences is located in that record on each run**, so a condition cannot outlive the words that
imposed it.

### 4.b ★ ASSUMPTION A3 IS FALSIFIED IN ONE NARROW RESPECT, AND THE STOP CAUGHT IT

A3 has the candidacy population derivable from the committed inventory artifact. **One flagged class
is one the inventory does not descend into**, so it publishes no member list for it, and the tool
**STOPPED** — the dispatch's own ordered stop, firing on real data rather than on a probe.

**The list was NOT hand-listed, which the dispatch forbids.** It is derived by applying the
inventory's **own published signature** — imported from its generator, not restated — to the tree at
the commit the inventory records, and **the derived count is cross-checked against the count the
inventory publishes for that class**, a disagreement stopping the tool. How each member list was
derived is recorded per candidacy in the artifact, so the two routes are told apart without
re-deriving anything.

*A second defect was found and fixed at the tool rather than worked around:* git C-quotes any path
holding a non-ASCII byte and this repository has one, so an unquoted read reported that path missing
and the walk stopped. Every git call the file makes now sets `core.quotepath=false`, once.

### 4.c ★ THE MEASURED FINDING — THE CHECK AS SPECIFIED CANNOT YET DISCRIMINATE, AND THE QUESTION IS RETURNED

**Every candidacy comes back HELD-BY-CALLERS.** The verdicts are exactly what the check the dispatch
specifies produces, and they are reported as measured.

**What the naming mostly is:** artifacts that **enumerate the tree** name every path by construction
— the artifact inventory itself, the ruling surface generated from it, the decision harvest, the file
tables. Such a naming carries no information about whether anything **depends** on the file, which is
what the check exists to establish. The genuine references are there too, in the tail.

**What is NOT decided here: whether an enumeration counts as a caller.** Deciding it would mean
either exempting named artifacts — an authored judgment about which records are exempt — or picking a
threshold on how many files a caller may name, which is a hand-picked number over varying data and
the shape this record has twice declined. **Neither is taken.**

**What is published instead:** `who_does_the_naming` — per caller, how many of the flagged population
it names and what share that is. The enumerating artifacts are visible there **as data** rather than
removed by a rule nobody ruled, so the question can be ruled with the measurement in front of it.

**What it means for archiving: NOTHING may be archived on these verdicts as they stand** — which is
the same answer the standing warning already gave, reached now by measurement rather than by caution.

### 4.d What the check does not establish, stated before its first use

A file REFERENCES a candidate when its text at the measured commit contains the candidate's base
name — the three kinds the dispatch names (an import, a path written out, a tool reading a file by
name), read generously, because erring toward finding a caller errs away from archiving something
still in use. **NONE FOUND means no literal naming was found in text at that commit, never that
nothing depends on the file**: a reference assembled at run time carries no literal to find, and a
binary blob is not searched at all. References from inside a candidate's own class are **set aside in
their own field, not dropped** (#12), so the exclusion can be checked rather than trusted.

**Registered expectation E3 — MET.** Every ruled candidacy appears with exactly one verdict and its
evidence; the commit whose tree was measured is named inside the artifact; the task's commit carries
the tool, the artifact and the guard-mechanism records, and no other path.

---

## 5. The new-tool rule, discharged twice

Each check this batch adds joined the derived guard-candidate population the moment it existed, and
**each landed WITH its authored run-instruction and its authored classification verdict in the SAME
commit that adds it** — the condition [[OI-373]] recorded for two other tools, which this dispatch
makes a standing rule. Both take `--check` and not the bare invocation, for a reason about the tools:
run with no flag each REWRITES its committed outputs, which is the OI-301 hazard.

*One ordering consequence is declared rather than glossed.* Task 3's tool existed on disk while Task
2's guard state was being taken. It was **moved out of the repository** for the duration, so the state
committed with Task 2 is the state of Task 2's own tree, and restored for Task 3. Had it been left in
place, the Task-2 artifact would have carried an unclassified candidate and a STOP that belonged to
neither task.

---

## 6. Every registered expectation, graded

- **E0 — MET.** Exactly 2 paths at `git diff-tree` on `54eb257a6f`; `cowork_handoff.md` numstat
  101/1; no staging override of any kind.
- **E1 — MET.** ONE path, ONE changed passage, 1 insertion and 1 deletion, confined to the twelfth
  block's heading; `THE CURRENT ENTRY POINT.` afterwards occurs exactly twice, in the two places the
  expectation names.
- **E2 — MET.** The whole backbone population classified, every entry in exactly one class with
  quoted evidence; the register's rendered and data files byte-identical to their committed blobs,
  proven by hashing; `--check` re-derives.
- **E3 — MET.** Every ruled candidacy with exactly one verdict and its evidence; the measured commit
  named inside the artifact; the commit carrying the tool, the artifact and the guard-mechanism
  records and no other path.
- **E4 — MET.** The end guard state shows every check passing except
  `gen_filing_convention_application.py --check` ([[OI-372]]), zero STOPs, with both of this batch's
  new checks inside the classified population under authored verdicts, and the runner and
  `gen_guard_classification.py` both printing their re-derives lines. **No other failing check
  appeared at any point in the batch**, so no STOP-and-report was owed.
- **E5 — see below, and the ordering rule the dispatch imposed was obeyed.**

**★ E5, RUN AT THE TREE CARRYING THE CLOSE AND AFTER THE COMMIT THAT CARRIES IT.** Per the dispatch's
rule taken from this side's own E3 ordering defect — *no graded value is committed before the run
that produced it* — the run's output and the final SHAs land in **one further commit** after the
close. Its values are recorded in that commit and in the close, read from the run's output.

---

## 7. Surfaced findings (D-641, #13, #19) — surfaced, not rowed

The dispatch bars creating an open-items row, so each is stated here and in the close.

- **F5 (new) — the caller-check's signal is swamped by tree-enumerating artifacts.** §4.c. The
  measurement is published; the ruling is the user's. This is the finding that decides whether the
  first pruning wave can execute at all.
- **F6 (new) — one flagged class publishes no member list, so a population the record treats as
  uniform is not.** §4.b. Answered by deriving from the published signature; recorded because the
  next derivation over the inventory will meet the same asymmetry.
- **F7 (new) — the decisions register's data file uses a status spelling its own header does not
  declare.** §3.d. Nothing turns on it here. Not repaired: the register is not this batch's to edit,
  and the disagreement is evidence.
- **F4 (carried, unchanged)** — the anchor-remap practice reaches artifacts that turn red only in a
  SECOND guard run.
- **F3 (carried, unchanged, now thrice surfaced)** — `reaim_home_anchors.py --check` exits 0 while
  printing drifted anchors; the drift authority is `gen_cluster_dispositions.py --verify`. **Still
  unfixed and unrowed — the dispatch bars both.**
- **F1 and F2 (carried)** — no zero-deletion expectation at a mid-line insertion point; seven
  committed artifacts capture `CLAUDE.md`'s text, its naming counts or its anchors.
- **The E3 ordering defect of the previous report, and the A1 premise error of the dispatch before
  it**, are carried to the phase's retrospective as the dispatch orders.
- **No finding bearing on the analysis, its inputs, or a measurement tool the analysis depends on.**
  Every subject of this batch is the project's own record and the apparatus that reads it.

---

## 8. What this batch did NOT do

**Nothing was discarded and nothing was archived.** No soft-discard executed, no decisions-register
entry written, edited or retired — the filtering ruling stands and Task 2's surface awaits the user.
No file moved, renamed, retired, archived or deleted; the caller-check's verdicts confer nothing; the
284 newly visible instruction files and the remaining ignored files stay unlanded. No mining, no
rulings sort, no empirical findings ledger, no fact-gate admission, no curated boot list. No
derivation of any specification, no design, no repair, no pilot act. **No `src/` change, no golden, no
test changed, moved or run, nothing under `tools/corpus/` or `tools/robust_stop/`, no measurement of
the analysis.** **No open-items row created, flipped or discarded** — [[OI-372]] and [[OI-374]] stay
exactly as found, [[OI-179]] stays OPEN and GATES, and `reaim_home_anchors.py`'s F3 defect stays
surfaced, unfixed and unrowed.

*Provenance: CC, 2026-08-15, dispatch `cc_instruction_preparation_opening.md`. Task 0 is commit
`54eb257a6f` (parent `02636987b0`), pushed. Task 1 is `a150bd8acf` (parent `54eb257a6f`), pushed.
Task 2 is `0a2cc3f86a` (parent `a150bd8acf`), pushed. Task 3 is `0305d495bb` (parent `0a2cc3f86a`),
pushed. Task 4's close commit and the E5 run that follows it are recorded in the close and in one
further commit, so that every content SHA is on the record rather than left to be looked up.*
