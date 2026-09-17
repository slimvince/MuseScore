# CC report — the preparation phase's third batch

> **What this is.** The coding side's report on `cc_instruction_preparation_third.md`, performed
> 2026-08-16. The batch record beside it is THE PREPARATION THIRD BATCH section of
> `cowork_away_returns.md`; this file is the whole of what the coding side says back.
>
> **THE HEADLINE, BEFORE ANY DETAIL.** Tasks 0, 1 and 2 are performed. **TASK 3 IS NOT.** The ruled
> soft-discard was derived, applied to the working tree, measured against the whole guard set, and
> **REVERTED** — because the dispatch's own assumption **A3**, that the mutation's reach is the
> decisions-register family and its derived views ONLY, is **FALSIFIED by that measurement**. The
> dispatch's instruction for that outcome is a STOP-and-report, and this is it. **No
> decisions-register file is changed by this batch: `DECISIONS.md`, all twenty group files, the data
> file and the two mechanism generators are byte-identical to their committed blobs, proven by
> hashing both sides.**
>
> **THREE THINGS THE USER SHOULD READ BEFORE ANYTHING ELSE.** *(1)* **The discard is derivable and
> the arithmetic balances to the digit** — 194 = 29 withheld + 165 to retire — so what stands in the
> way is not the ruling and not the population, but what performing it REACHES (§4). *(2)* **The
> reach includes both gate-bearing phase-1 derivations, and they do not go stale — they HALT**,
> because entries the retirement removes are the reason three documents are homes and one is class C
> (§4.c). *(3)* **The residue surface both of this batch's returns ride on is complete and awaiting
> the user** — the entries the guard withheld, and the 62's check results, on one self-contained
> surface (§2, §3).
>
> *(Every guard count lives at `tools/audit/guard_state.json`; every sole-carrier value at
> `tools/audit/sole_carrier_subclass.json`; every ratified-document result at
> `tools/audit/ratified_document_check.json`; the whole discard derivation at
> `tools/audit/soft_discard_application.json`. None is restated here beyond the few this report is
> reporting ABOUT, each naming where it was read — **D-431**.)*

---

## 1. Both guard-set states, and Task 0

### 1.a The start state, taken before the first edit

`gen_guard_state.py --check` printed **"the guard state re-derives"** — **52 guards run, 51 passing,
ONE failing** (`gen_filing_convention_application.py --check`, which is [[OI-372]]), 4 not run, 10
historical records, **no STOP**. `gen_guard_classification.py --check` printed **"the guard
classification re-derives"**. **This is exactly the start state the dispatch declares as expected**,
so no STOP-and-report was owed on it.

### 1.b Assumption A1, checked first and entirely at content-addressed objects

The sanctioned enumeration `tools/audit/changed_paths.py` reported **exactly ONE tracked
modification in the whole working tree** — `cowork_rulings_2026_08_16_preparation_return.md` — with
`cc_instruction_preparation_third.md` untracked and every other record untracked.

The difference was then taken **blob against blob by explicit hash**: the committed blob resolved
from the commit the dispatch's FACT names, the working blob written into the object store by
`git hash-object -w`, and the two diffed. **43 insertions, 2 deletions, ONE contiguous changed
passage** — §3 appended before the provenance block, and that block rewritten in place. **A1 held at
exactly the shape it describes.**

*Two remarks about the premise rather than about the act, declared rather than glossed.*

- **F17.** The dispatch's FACT names `8ee16dca1a` as the commit the second batch is complete and
  pushed through. The record's head was one further on — `17f0a9e04b`, whose subject is a correction
  to that same batch's report — and the ruling record's blob is identical at both, so nothing turned
  on it. **This is F12 of the previous batch repeating**, which is why it is numbered again rather
  than folded into it.
- **F18.** A1 as literally worded says the working tree carries **NO** tracked modification *and*
  that the ruling record differs from its committed blob. Read literally the two clauses cannot both
  hold. The check was run against the shape the rest of the sentence describes — one tracked
  modification, that file, that difference, nothing else — and it held. Stated because a premise a
  session has to repair before it can be checked is a premise worth rewording.

### 1.c Task 0 — commit `cb5070c106`, parent `17f0a9e04b`, pushed

Exactly the two paths the dispatch names and no third, verified at the index through the sanctioned
tool before the commit (2 records) and at the object after it. Both staged **plainly**; no override
of any kind.

---

## 2. Task 1 — the sole-carrier subclass. Commit `a88d793021`, pushed, six paths

### 2.a What is derived, and what the guard is for

The user's ruling puts the soft-discard **behind** a guard, and defines the guard itself: *"an entry
whose status is DEFERRED, or whose home cannot be located, or whose content is found nowhere outside
the register family."* The subclass is computed over the **whole** non-keep population — all 266, not
the 194 — so the 62 the (B2) limb leaves unruled reuse this derivation instead of needing a second
one (**D-671**).

Three signals per entry, each published with the evidence that produced it, and SOLE-CARRIER if any
one fires. **No threshold, no weighting, no hand-picked member.**

The one thing worth reading about the rule is where it takes its definitions from. Signal (i) reads
the status vocabulary the data file's **own header** declares. Signal (iii) uses the **decisions
register's own normalization**, imported from `gen_cluster_dispositions.py` rather than
re-implemented (#6) — the same function that same establishment pass uses to prove every
verbatim is findable at its home, so this pass and that establishment cannot disagree about what a
quotation is.

### 2.b ★ TWO OF THE THREE SIGNALS COME BACK EMPTY, AND THAT IS A RESULT

Signal (i) fires for 39 of the 266. Signals (ii) and (iii) fire for none.

An empty signal is indistinguishable, from an artifact alone, from a signal that **cannot** fire. So
each of the three is shown, in the artifact, **both to fire on a case that should fire it and to stay
quiet on one that should not**, on synthetic entries fed to the very functions the walk calls; a
signal failing either half STOPS the tool (#19). Five such establishments ride with the pass.

What the two empty signals say is that every non-keep entry's home resolves at the measured commit,
and that every one of their verbatim quotations is carried somewhere outside the decisions-register
family. **That agrees with two standing checks that assert the same thing by different routes** —
the decisions register's own establishment pass, which finds all 677 verbatims at their cited homes and all 671
anchored line numbers correct, and `gen_home_classification.py --check`, which re-derives every home
section from the documents' own headings. It is corroboration, not an assumption. Recorded as **F14**
because a guard that reduces in practice to one of its three limbs is worth the user knowing about.

### 2.c The bounds, declared rather than hidden

- **The decisions-register family is drawn WIDER than the ruling's words require** — `DECISIONS.md`,
  `decisions/`, and the whole of `tools/audit/` rather than only that record's own artifacts —
  because an artifact under `tools/audit/` is derived FROM the record, so a quotation appearing there
  is the record quoting itself and not independent carriage. The widening can only make MORE entries
  sole-carriers, which **withholds** them from the discard: the recoverable direction.
- **The wide walk searches only blobs whose extension is in a declared text set**, and the excluded
  population is published with its count and its size in bytes. **No size ceiling is imposed** — a
  hand-picked number over varying data is the shape this record has twice declined. In this run **no
  entry reached the wide walk at all**: every one was answered at its own home document, so the bound
  bought nothing and is published saying so.
- **All three inputs are read from the git objects at the commit the artifact records.** The reason is
  not neatness: the discard this guard stands in front of MOVES those very inputs, so an input read
  live would be changed by the act the artifact authorizes, and the record of which entries were
  withheld would be destroyed by the act it guarded (#12; the OI-301 hazard). What stays LIVE is the
  ruling's own sentences, located in the ruling record as it stands on every run.

---

## 3. Task 2 — the ratified-document subject check. Commit `81e2ef1c23`, pushed, seven paths

### 3.a The population is parsed from the ruling, not typed

The 62 are the recovery pass's ACT-FOUND entries **minus** the ten the (B1) limb KEPT. The first side
is imported from the committed recovery artifact; **the second is PARSED from the ruling record's own
(B1) bullet on every run**. A bullet naming any number other than ten, or naming an entry the recovery
pass did not return ACT-FOUND for, **halts the derivation rather than being corrected** — so the
population cannot drift away from the words that fixed it. It parsed to exactly the ten the ruling
names.

### 3.b ★ THE ONE JUDGMENT THAT DECIDES WHAT THIS CHECK MEANS, AND IT WAS CORRECTED MID-RUN

The ruling asks what **THE RATIFIED DOCUMENT** says. A recovered passage typically names several
documents, most of them mentioned rather than ratified. **The first version of this tool admitted
every document named anywhere in the passage**, and its own output refuted it: one entry's "ratified
documents" came back as four files that the ratifying passage merely mentions.

The rule was narrowed at the tool: **a document is ratified by the act when it is named in a SENTENCE
of the passage that also carries a ratification word.** The narrowing moved 5 entries out of
SUBJECT-IN-RATIFIED-DOCUMENT. **What the wider reading would have admitted is not discarded** — every
document named elsewhere in the passage is published per act, by name, so the difference between the
two readings is visible and the user can ask for either. Recorded as **F16**.

Where the narrow reading is *still* wide is stated on the surface above the first result: any
ratification word beside any document name inside one sentence admits it. That direction is the
harmless one — a wrongly admitted document is then searched and reports either a subject match the
user can check at the quoted line, or SUBJECT-NOT-FOUND-THERE, which claims nothing.

### 3.c Two further properties worth naming

- **The document the act itself sits in is NOT searched**, and the reason is duplication rather than
  economy: the recovery pass already searched exactly that document and published what it found.
  Searching it again would republish that finding as though it were new evidence.
- **Every recorded act coordinate is re-read at the measured commit and cross-checked** against the
  quote the recovery pass published, because a document can move under a recorded line and reading
  whatever now sits there would silently grade the wrong passage. **None had moved**; the count is
  published either way.

### 3.d The residue surface

`ratification_surfaces/cowork_discard_residue_surface_2026_08_16.md` carries **both** of this batch's
returns — the entries the guard withheld, each with the signals that fired and its plain restatement,
and the 62's results, each with the passage quoted at its line. It is **generated from the two
artifacts**, so no count and no member list on it is typed by hand (#17f); it re-explains every
identifier from scratch in §0 per the standing presentation rule; its banner states **NOTHING HERE IS
RULED**; and the user's own clause is quoted **verbatim** in that banner, so whoever rules meets it
before the members.

---

## 4. ★ Task 3 — the ruled soft-discard is NOT executed. Commit `db5978168c` carries the STOP

### 4.a What was done, in order

The act was **derived**, then **applied to the working tree**, then the **whole guard set was run at
the edited tree**, then the edit was **REVERTED**. Nothing of it is committed.

**The revert is proven at the objects, not asserted.** `DECISIONS.md`, `tools/audit/decisions/
backbone_decisions.json`, `tools/audit/decisions/gen_cluster_dispositions.py` and
`tools/audit/decisions/gen_decisions_register.py` were each hashed and compared with their committed
blobs: **all four identical**. The sanctioned enumeration reports **no tracked modification** left by
the reverted work, and all twenty group files are back at their committed content.

### 4.b The derivation itself is sound, and the arithmetic balances to the digit

| | entries |
|---|---|
| the recovery pass returned NOTHING-FOUND for | **194** |
| of which the sole-carrier guard WITHHELD | **29** |
| leaving the executed discard population | **165** |

The live record would go **677 → 512**. The population is derived — the NOTHING-FOUND set minus the
guard's members — and a member that is both halts the act, as does a member the data file does not
carry live (D-671). **Nothing about the population or the ruling is in doubt.**

One derived consequence was measured **before** anything was applied: **33 surviving entries name a
retired entry** in a field the decisions register's establishment pass reads. That pass checks every `D-…`
cross-reference resolves, so consulting only the live entries would have reported 33 references as
DANGLING and called a correct record broken. The mechanism change that answers it — the establishment
pass consulting the retired block beside the live entries — was written and **measured working**: with
it, `--verify` passes at 512/512.

### 4.c ★ WHAT FALSIFIES A3 — the guard set at the edited tree

**Fourteen checks turn red where one was expected**, and the reach is not the decisions-register
family. Quoted from the run, not summarized:

```
[FAIL] tools/audit/claude_md_rule_triage.py --check
    triage for a rule that is not homed in CLAUDE.md: ['D-192']
[FAIL] tools/audit/gen_phase1_completion_inventory.py --check
    STOP: authored draft for a document that is not class C: ['cowork_structural_integrity_audit.md']
[FAIL] tools/audit/gen_phase1_finish_line.py --check
    STOP: authored draft for a document that is not class C: ['cowork_structural_integrity_audit.md']
[FAIL] tools/audit/decisions/gen_outstanding_delegations.py --check
    STOP: authored draft for a document that is not class C: ['cowork_structural_integrity_audit.md']
[FAIL] tools/audit/decisions/gen_finish_line_item1_routes.py --check   (same STOP)
[FAIL] tools/audit/decisions/gen_item1_rehome_blocker.py --check       (same STOP)
[FAIL] tools/audit/decisions/gen_r1_superseded_reach.py --check        (same STOP)
[FAIL] tools/audit/decisions/gen_home_classification.py --check
    authored judgment for a document that is nobody's home:
    ['cowork_layer2_slicing_design.md', 'cowork_phase2_architecture_review.md',
     'cowork_types_header_design.md']
[FAIL] tools/audit/decisions/gen_phase1p_delegation_bar.py --check
    FORM judgment for a document that is nobody's home:   (the same three)
[FAIL] tools/audit/decisions/gen_phase1w_legacy_verification.py --check
    STOP: A1 (the marker is generated text): quote not at
    tools/audit/decisions/gen_decisions_register.py:514. It is now at line(s) [576].
[FAIL] tools/audit/gen_artifact_inventory_surface.py --check
    FAIL: re-derivation differs from the committed surface
[FAIL] tools/audit/gen_retirement_caller_check.py --check
    FAIL: the caller-check does not re-derive
[FAIL] tools/audit/gen_decisions_filter.py --check      (register-derived, expected)
[FAIL] tools/audit/gen_deciding_act_recovery.py --check (register-derived, expected)
[FAIL] tools/audit/gen_filing_convention_application.py --check   (pre-existing, [[OI-372]])
```

**Three separate causes, and only the last is what the dispatch anticipated.**

1. **A document stops being class C.** Every entry homed in `cowork_structural_integrity_audit.md`
   is in the discard population, so the delegation grading no longer places that document in the
   class its authored draft is written for — and the derivation **halts**. Five checks import that
   derivation, and **two of them are the phase-1 completion inventory and the phase-1 finish line,
   which A3 names by name.** They do not drift. They stop being derivable at all, which means the
   phase-1 gate stops being derivable at all.
2. **Authored judgments lose their subjects.** Three documents stop being anybody's home; the
   `CLAUDE.md` rule triage carries an authored entry for D-192, a rule the retirement removes from
   the live record; the artifact-inventory ruling surface and the retirement caller-check stop
   re-deriving. Each of these is an **authored table about documents**, and clearing it means
   re-authoring judgments this dispatch does not authorize.
3. **The decisions register's own generator is itself one of its homes.**
   `gen_phase1w_legacy_verification.py`
   halts because an entry's verbatim is anchored to a line of `gen_decisions_register.py`,
   and inserting the retired block's STOPs into that generator moves it from 514 to 576. Recorded as
   **F15** — teaching the mechanism about the retired block is itself a change to a home document.

**Why "regenerate and it clears" does not apply.** The dispatch expects reds "ONLY in
register-consuming checks, each clearing after its regeneration". None of causes 1 and 2 clears that
way: they are STOPs inside derivations whose authored halves the retirement invalidates, and two of
them are the gate-bearing derivations **D-436** reserves — the previous batch declined to regenerate
exactly those under a dispatch that bars derivation, and the same reasoning holds here.

**So A3 is falsified as stated, and the dispatch's own instruction on that outcome is a
STOP-and-report.** Recorded as **F13**, and it is this batch's largest finding.

### 4.d What IS committed, and what a reader must not conclude

Committed: the **derived plan** (`tools/audit/soft_discard_application.json`), the tool that derives
it, and the guard registration. The tool writes no decisions-register file without `--apply`.

**Not committed and deliberately so:** the mechanism work the act needs — the retired block's own
STOPs in the renderer (an entry in both blocks, or the arithmetic not accounting for the recorded
former population, halting it) and the establishment pass consulting the retired block — both written,
both measured working, and both reverted with the rest. Landing them ahead of the ruling they wait on
would put a mechanism for an unperformed act into the record.

**What a reader must not conclude is that the ruling is in doubt.** The user ruled the discard. What
this measurement establishes is that performing it **inside the bounds the dispatch set** is not
possible, because the act reaches authored judgments and gate-bearing derivations the dispatch does
not authorize touching. What is owed is a ruling on that reach — not a re-decision of the discard.

---

## 5. The new-tool rule, discharged three times

Each check this batch adds joined the derived guard-candidate population the moment it existed, and
**each landed WITH its authored run-instruction and its authored classification verdict in the SAME
commit that adds it**. All three take `--check` and never the bare invocation, for a reason about the
tools: run with no flag each REWRITES its committed outputs, which is the OI-301 hazard — and for the
third it is the sharpest, because its committed output is the record of which entries a guard
withheld from a discard.

The runner's own STOP fired for real once, on Task 3's tool before it was registered, which is that
mechanism working rather than a defect.

---

## 6. Every registered expectation, graded

- **E0 — MET.** Exactly 2 paths at `git diff-tree` on `cb5070c106`; one addition and one
  modification; no staging override of any kind.
- **E1 — MET.** All 266 covered, each with the three signals and one verdict, every signal carrying
  its evidence; `--check` re-derives; the commit touches only the tool, its artifact and the
  guard-mechanism records — **no decisions-register file**.
- **E2 — MET.** Exactly the 62 covered, each with a per-act establishment and one per-entry result;
  the scope block names its population by citation and by the bullet it parsed; `--check` re-derives;
  **no decisions-register file touched in the commit**.
- **E3 — NOT MET, AND NOT ATTEMPTED TO BE MET.** The act it grades was not performed. The data-file
  diff, the regenerated files, the arithmetic in the close and the byte-preservation it demands all
  describe a commit that does not exist. What is recorded instead is §4: the derivation, the
  measurement, the revert proven at the objects, and the falsified assumption. **`gen_decisions_
  register.py --check` and `gen_cluster_dispositions.py --verify` both pass at the end state — at the
  UNCHANGED decisions register**, which is a different fact from the one E3 asks for and is not
  offered as it.
- **E4 — MET at every task's end.** See §7.
- **E5 — see §7**, and the ordering rule the dispatch imposes was obeyed.

---

## 7. The end state, and the ordering rule

**★ E4 — MET.** After Task 3's commit the guard set stands at **55 run, 54 passing, ONE failing**
(`gen_filing_convention_application.py --check`, [[OI-372]]), 4 not run, 10 historical, **zero
STOPs**, with all three of this batch's new checks inside the classified population under authored
verdicts and all three passing. **No failing check other than [[OI-372]] survives in the committed
tree**, so no further STOP-and-report is owed on the end state itself.

**★ E5 — MET, RUN AT THE TREE CARRYING THE CLOSE AND AFTER THE COMMIT THAT CARRIES IT.** Task 4's
close is commit **`1b824b23b1`**, parent `db5978168c`, pushed, three paths, verified at the object.
At that tree, after that commit existed, `gen_guard_state.py --check` printed **"the guard state
re-derives"** — **55 guards run, 54 passing, ONE failing** (`gen_filing_convention_application.py
--check`, [[OI-372]], the only `[FAIL]` line in the whole run), 4 not run, 10 historical, **no
STOP** — and `gen_guard_classification.py --check` printed **"the guard classification
re-derives"**. The sanctioned enumeration at the same tree reported **no tracked modification
anywhere**: every record it returned was untracked. **Run and read, never inferred.**

Per the dispatch's ordering rule — *no graded value is committed before the run that produced it* —
this paragraph and the SHA in it land in **one further commit** after the close. **The E3-ordering
defect that rule exists against is not repeated: no expectation anywhere in this report was written
before its measurement, and the one expectation this batch does not meet is graded NOT MET rather
than reconciled towards.**

---

## 8. Surfaced findings (D-641, #13, #19) — surfaced, not rowed

The dispatch bars creating an open-items row, so each is stated here and in the close.

- **F13 (new, the largest) — the ruled soft-discard's reach is NOT the decisions-register family, and
  A3 is falsified.** Fourteen reds, three causes, two gate-bearing derivations that halt rather than
  drift. §4.c.
- **F14 (new) — two of the sole-carrier guard's three signals come back empty**, so the guard reduces
  in practice to its status limb. Each signal is nonetheless established able to fire and able to stay
  quiet, and two standing checks corroborate the emptiness. §2.b.
- **F15 (new) — the decisions register's own GENERATOR is one of its own homes**, so teaching it about a
  retired block moves an anchored quote and halts the legacy verification. §4.c.
- **F16 (new) — "the ratified document" has a wide and a narrow reading**, the first version of the
  check took the wide one, and its own output refuted it. The narrow reading governs; the wider set is
  published rather than discarded. §3.b.
- **F17 (new, small) — the dispatch's FACT again names a commit one behind the record's head.** This
  is F12 repeating. §1.b.
- **F18 (new, small) — assumption A1 as literally worded is internally inconsistent.** §1.b.
- **F1–F12 (carried, unchanged)**, including **F3**, now five times surfaced —
  `reaim_home_anchors.py --check` exits 0 while printing drifted anchors, and
  `gen_cluster_dispositions.py --verify` is the drift authority. **Still unfixed and unrowed: the
  dispatch bars both.**
- **The E3 ordering defect and the A1 premise error of the earlier batches** ride to the phase's
  retrospective as the dispatch orders.
- **No finding bearing on the analysis, its inputs, or a measurement tool the analysis depends on.**
  Every subject of this batch is the project's own record and the apparatus that reads it.

---

## 9. What this batch did NOT do

**No entry was discarded, retired, edited, moved or marked, and no decisions-register file was
changed — proven by hashing all four touched files against their committed blobs after the revert.**
The 62 are not ruled and not touched; the residue surface awaits the user. No archiving, no file
moved, renamed or deleted; no mining, no landing; the eight KIND-UNDERIVABLE callers and the
prose-citation question stay open; every retirement flag stays a candidacy. No empirical findings
ledger, no fact-gate admission, no curated boot list, no rulings-sort execution. No derivation of any
specification, no design, no repair, no pilot act. **No `src/` change, no golden, no test changed,
moved or run, nothing under `tools/corpus/` or `tools/robust_stop/`, no measurement of the analysis.**
**No open-items row created, flipped or discarded** — [[OI-372]] and [[OI-374]] stay exactly as found,
[[OI-179]] stays OPEN and GATES.

*Provenance: CC, 2026-08-16, dispatch `cc_instruction_preparation_third.md`. Task 0 is commit
`cb5070c106` (parent `17f0a9e04b`), pushed, two paths. Task 1 is `a88d793021` (parent `cb5070c106`),
pushed, six paths. Task 2 is `81e2ef1c23` (parent `a88d793021`), pushed, seven paths. Task 3's STOP is
`db5978168c` (parent `81e2ef1c23`), pushed, six paths. Task 4's close is **`1b824b23b1`** (parent
`db5978168c`), pushed, three paths; **E5's run and that SHA are recorded in the ONE FURTHER commit
after it**, so no graded value was committed before the run that produced it. **★ WHERE THE RECORDING
TERMINATES, STATED RATHER THAN LEFT AS A GAP:** every commit of this batch is verified at the object
and named above except the LAST one — the commit carrying this sentence — because a commit cannot
contain its own identity. That is the terminus, not an omission.*
