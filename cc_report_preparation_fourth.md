# CC report — the preparation phase's FOURTH batch

> **What this is.** The coding side's report on `cc_instruction_preparation_fourth.md`, performed
> 2026-08-16. The batch record beside it is THE PREPARATION FOURTH BATCH section of
> `cowork_away_returns.md`; this file is the whole of what the coding side says back.
>
> **THE HEADLINE, BEFORE ANY DETAIL.** Tasks 0 and 1 are performed. **TASK 2 IS NOT.** The ruled
> soft-discard was derived, applied to the working tree, measured against the whole guard set, and
> **REVERTED** — because the dispatch's assumption **A3**, that with the ruled reach applied no red
> survives except [[OI-372]]'s tool, is **FALSIFIED by that measurement**. The dispatch's instruction
> for that outcome is a STOP-and-report, and this is it. **No decisions-register file is changed by
> this batch: the data file, `DECISIONS.md`, all twenty group files, both mechanism generators and
> every artifact the measurement touched are byte-identical to their committed blobs, proven by
> hashing both sides.**
>
> **FOUR THINGS THE USER SHOULD READ BEFORE ANYTHING ELSE.** *(1)* **The ruling's limb that
> REGENERATES the STANDING members is not available for five of the nine** — four of them refuse in
> WRITE mode as well as under `--check`, writing nothing at all, and a fifth halts (§4.d). *(2)* **The
> one member that does regenerate cleanly would replace the RATIFIED classification the discard
> ruling itself rests on** — 411 / 182 / 84 becomes 421 / 63 / 28 — and rewrite the ruling surface the
> user read (§4.e). *(3)* **The regeneration that IS available moves a user-ruled retirement
> candidacy set**, and one member of that movement is outside the bound's two named categories
> (§4.f). *(4)* **Everything the ruling assumed about the FIRST two limbs holds** — R1 finds zero live
> consumers, the split derives cleanly at 6 SUPERSEDED / 9 STANDING, the discard applies and the
> register renders, and the one mechanism item the ruling names is measured working (§2, §3, §4.c).
>
> *(Every guard count lives at `tools/audit/guard_state.json`; the reader enumeration at
> `tools/audit/phase1_gate_readers.json`; the split at `tools/audit/discard_reach_split.json`; the
> whole discard derivation at `tools/audit/soft_discard_application.json`. None is restated here
> beyond the few this report is reporting ABOUT, each naming where it was read — **D-431**. Every
> value below that is not from a committed artifact is QUOTED from the run that produced it, in the
> fenced blocks, rather than transcribed.)*

---

## 1. Both guard-set states, and Task 0

### 1.a The start state, taken before the first edit

`gen_guard_state.py --check` printed **"the guard state re-derives"** — **55 guards run, 54 passing,
ONE failing** (`gen_filing_convention_application.py --check`, which is [[OI-372]]), 4 not run, 10
historical records, **no STOP**, and no stale report. `gen_guard_classification.py --check` printed
**"the guard classification re-derives"**. **This is exactly the start state the dispatch declares
as expected**, so no STOP-and-report was owed on it.

### 1.b Assumption A1, checked first and entirely at content-addressed objects

The sanctioned enumeration `tools/audit/changed_paths.py` reported **exactly TWO tracked
modifications in the whole working tree** — `cowork_handoff.md` and
`cowork_rulings_2026_08_16_preparation_return.md` — with `cc_instruction_preparation_fourth.md` and
`ratification_surfaces/cowork_discard_reach_surface_2026_08_16.md` untracked, and no third tracked
difference anywhere.

Each difference was then taken **blob against blob by explicit hash**, the committed blob resolved
from the commit the record's head carries and the working blob written into the object store by
`git hash-object -w`:

- `cowork_handoff.md` — **98 insertions, 1 deletion, ONE contiguous changed passage**: the twentieth
  session-close block inserted, and the nineteenth block's heading replaced by the same heading
  carrying this file's own demotion marker. **Exactly the shape A1 states.**
- `cowork_rulings_2026_08_16_preparation_return.md` — **50 insertions, 2 deletions**, §4 inserted
  before the provenance block and that block rewritten in place. **The content is exactly the shape
  A1 names and nothing else**, but git reports it as **TWO hunks**, because two unchanged lines of
  the provenance paragraph sit between the insertion and the rewrite. Recorded as **F25**, below.

**No tracked difference outside the shape A1 names**, so the ordered STOP was not reached.

*One remark about the premise rather than about the act.* **F17 does not repeat.** This dispatch's
premise ledger states in terms that no premise names a terminus commit and that every FACT pins
content — and none did. The lesson of F12/F17 was taken.

### 1.c Task 0 — commit `f92f27fc3b`, parent `660aa4609e`, pushed

Exactly the four paths the dispatch names and no fifth — two modifications, two additions — verified
at the index through the sanctioned tool before the commit and at the object after it. All staged
**plainly**; no override of any kind. **E0 is MET.**

---

## 2. Task 1, first half — R1, the reader enumeration. Zero live consumers

`tools/audit/gen_phase1_gate_readers.py` → `tools/audit/phase1_gate_readers.json`.

### 2.a What it enumerates, and why the reading is pinned

Every tracked file naming any of the six artifacts — the two the ruling calls the old phase-1 gate
artifacts, and the four the derivation family's other generators produce. **Each generator's own
output artifact is DERIVED from that generator's own source**, not typed into the check: a generator
that no longer names its own artifact halts the run rather than being guessed at.

Every reading is taken from the **git objects at the commit the artifact records**. Read at whatever
the current commit happens to be, this check would go red the first time anybody writes a file
naming one of these artifacts — the [[OI-301]] / [[OI-305]] shape. What stays live is the apparatus:
a named generator the tree no longer carries, or one whose artifact can no longer be derived from
its source, halts it.

### 2.b The result

```
  a-historical-record: 110
  the-superseded-programs-own-apparatus: 12
  LIVE consumers outside the superseded program: 0
```

**122 naming files, and the LIVE-consumer class is EMPTY.** The ruling's ordered STOP — *a live
consumer outside the superseded program is a STOP-and-report* — is not reached, and assumption R1 of
the decision surface holds.

### 2.c ★ THE ONE JUDGMENT, DECLARED RATHER THAN BURIED

The ruling's vocabulary has three values and **no fourth value for a citation inside a LIVE governing
surface**. This pass invents none: every naming that is a CITATION rather than a read is placed in
`a-historical-record`, on the stated ground that a citation is **inert under a freeze — the artifact
is frozen IN PLACE and stays readable** — and each carries a `citation_subkind` field
(a record of an act, a governing-or-tracking-surface pointer, a ruling-surface pointer, a row of a
generated census) **with its naming line quoted**. A reader who would give a governing-surface
pointer its own class can see every one of them without re-deriving anything.

### 2.d ★ THE DOWNSTREAM FACT A READER MUST MEET — published rather than discovered later

Two checks outside the six read `phase1_completion_inventory.json` **as their own population**, which
is why they are placed inside the superseded program rather than outside it:

- `tools/audit/decisions/gen_true_half_reach_rows.py` — whose own artifact
  `true_half_reach_rows.json` is read by **`tools/audit/gen_nongating_apparatus_rows.py`**, the check
  that derives **D-438**'s non-gating apparatus declaration, which is a rule of the CURRENT record;
- `tools/audit/gen_gating_row_sizing.py` — whose artifact no check reads.

Neither halts and neither is frozen. What freezes is their INPUT, so **their populations stop
moving**, and the first of them passes that frozen population one link further down into a live
rule's own derivation. Nothing is destroyed and nothing breaks; what is lost is future movement.
Recorded as **F22** and published in the artifact rather than left for a later session to find.

---

## 3. Task 1, second half — R2, the derived split. 6 SUPERSEDED, 9 STANDING

`tools/audit/gen_discard_reach_split.py` → `tools/audit/discard_reach_split.json`.

### 3.a Which of the two offered routes was taken, and why

The dispatch offers two routes to the population and asks which was taken. **The MEASURED route.**
The population is parsed on every run out of the `[FAIL]` lines of the committed report's own
captured run (`cc_report_preparation_third.md` §4.c), read from the git object at the recorded
commit — **imported, never retyped into the generator**.

**The static route was tried and REJECTED, and the rejection is recorded in the artifact.** A
predicate over imports can say which checks READ the decisions register's live entry population; it
cannot say which of those TURN RED, because it cannot separate a check that re-derives cleanly over
the shrunken record from one that halts inside an authored half the retirement invalidates. Measured
against the committed run, such a predicate selects far more checks than turned red — that same
register's own renderer and its establishment pass among them, both of which pass. A population that
overshoots the measurement is not a derivation of it.

**And the population is now CONFIRMED at the applied tree**, which the artifact said was owed and not
yet done: the guard set run at the applied tree reports **exactly these fifteen and no others**
(§4.b).

### 3.b The verdict rule, and the one thing that had to be measured to get it right

A member is SUPERSEDED in exactly three shapes, each a fact about the import graph: it IS one of the
two gate derivations; it imports one of them transitively; or it is a FEEDER **whose every importer
is exactly those two and nothing else**. Everything else is STANDING.

**★ The feeder limb is deliberately NOT computed to a fixed point, and that was measured rather than
argued.** The feeder's own feeder is imported by the feeder rather than by the gate, so a fixed point
would sweep `gen_home_classification.py` — the check the current record's own home rules depend on —
into a class the ruling means for the gate alone.

### 3.c The result, and the ruling's own STOP firing for real

```
  STANDING: 9
  SUPERSEDED: 6
```

The six SUPERSEDED are exactly the family the decision surface names. Each of the nine STANDING
carries a derived explanation of its red against the enumerated-movement bound.

**★ The ruling's own STOP — a STANDING member whose red the bound cannot explain — fired on the
first run**, naming four members. The cause was not the bound: it was that the committed report's
§4.c block **abbreviates two of its reasons** to `(the same three)` and `(register-derived,
expected)`, so a derivation that could read only that prose has nothing to place them by. The
explanation is therefore derived from **each check's own inputs** as well as from the captured
reason, and every row publishes which of the two placed it. Recorded as **F23**.

---

## 4. ★ Task 2 — the ruled act is NOT performed. What the measurement establishes

### 4.a What was done, in order

The act was **derived**, then **applied to the working tree**, then the decisions register was
**regenerated by its own generator**, then the one mechanism item the ruling names was **applied and
measured**, then
the whole guard set was **run at the applied tree**, then everything was **REVERTED**. Nothing of it
is committed.

**The revert is proven at the objects, not asserted.** Every file the measurement touched was hashed
and compared with its committed blob at `5a687aea9c`:

```
IDENTICAL tools/audit/decisions/backbone_decisions.json 2182504236c5e8491f3cc38ba4806e45a0b0a25d
IDENTICAL DECISIONS.md ad7f4e33c6634d0c1c2f551ccc78aef1a2bb0120
IDENTICAL tools/audit/decisions/gen_cluster_dispositions.py a4277beaa406ebcc1decc48c46298b61f00d0b77
IDENTICAL tools/audit/decisions/gen_decisions_register.py 312182b90296905ec1e233c3ab327da222db73f1
IDENTICAL tools/audit/decisions_filter_classification.json d738e7e0aff4d42a7ae5fc3a8978fdfaffd8ce6d
IDENTICAL tools/audit/retirement_caller_check.json cf3c82d01838e12ccea349a828f29598528bff3b
IDENTICAL ratification_surfaces/cowork_artifact_inventory_ruling_surface.md d04aa5726b2cd9a398e093928f7d4bbe2b6063ff
IDENTICAL ratification_surfaces/cowork_decisions_filter_surface_2026_08_15.md 83f3b1ab723602893de6087855d2803d15b20d1c
group files identical=20 differing=0
```

The sanctioned enumeration reports **no tracked modification** left by the reverted work, and
`gen_guard_state.py --check` at the reverted tree prints **"the guard state re-derives"** with the
same one failing check the batch started at.

### 4.b What WORKS, established rather than assumed

Four of the ruling's premises hold, and each was measured:

- **The discard applies.** `apply_soft_discard.py --apply` printed
  `applied: 165 entries retired, 512 live (was 677), 10 provenance stamps written`.
- **The renderer regenerates over the shrunken record.** `gen_decisions_register.py` printed
  `wrote 21 files: DECISIONS.md (the index, 901 lines) + 20 group files under decisions/ (512
  decisions)`, and its `--check` then printed `the register matches the data (21 files: the index +
  20 group files)`.
- **The ruling's named mechanism item works, exactly as the third batch measured it.** Without the
  retired block consulted, the establishment pass reports `cross-references resolving: 38 DANGLING`.
  With it — the four-line change the ruling's limb 4 orders — it prints:
  ```
  backbone decisions: 512
  cross-references resolving: ALL
  verbatim quotes found at their cited home: 512/512
  cited line numbers correct: 506/506   (6 cited to a file with no line number, by design)
  ```
- **R2's population is confirmed.** The full guard set at the applied tree reports **57 run, 15
  failing** — exactly the fifteen members the split carries, no sixteenth and none missing.

**And the SUPERSEDED limb is sound.** All six halt with the same reason —
`STOP: authored draft for a document that is not class C: ['cowork_structural_integrity_audit.md']`
— and reclassifying them historical removes their reds from the set by construction, because a
historical record is not run.

### 4.c ★ WHAT FALSIFIES A3 — ground one: the REGENERATE limb is not available

The ruling's third limb is that the STANDING members are **regenerated by their own generators**.
Measured at the applied tree, **five of the nine cannot be regenerated at all.** Each was run in
WRITE mode, not merely under `--check`, and **each wrote nothing**:

```
=== WRITE tools/audit/claude_md_rule_triage.py
   exit:1
   triage for a rule that is not homed in CLAUDE.md: ['D-192']
=== WRITE tools/audit/decisions/gen_home_classification.py
   exit:1
   authored judgment for a document that is nobody's home: ['cowork_layer2_slicing_design.md', 'cowork_phase2_architecture_review.md', 'cowork_types_header_design.md']
=== WRITE tools/audit/decisions/gen_phase1p_delegation_bar.py
   exit:1
   FORM judgment for a document that is nobody's home: ['cowork_layer2_slicing_design.md', 'cowork_phase2_architecture_review.md', 'cowork_types_header_design.md']
=== WRITE tools/audit/decisions/gen_phase1w_legacy_verification.py
   exit:2
   STOP: authored verdicts for entries that are NOT in the derived marked set: D-051, D-052, D-059, D-060, D-061, D-062, D-063, D-064, D-065, D-089, D-101, D-102, D-104, D-214, D-216, D-217, D-218, D-219, D-235, D-243, D-346, D-350, D-354, D-355, D-356, D-357, D-378, D-402, D-405, D-579
```

and the fifth, whose imported population is no longer in the data file's live entries:

```
=== tools/audit/gen_deciding_act_recovery.py --check
   exit:2
   STOP: the imported non-keep population and the decisions register's data file do not carry the
   same entries — a derivation over a derived population is published WHOLE or not at all (D-671).
```

**These are not drifted artifacts waiting for a regeneration.** Each is an authored table whose
subjects the retirement removes, and each refuses to write rather than silently dropping the
judgments whose subjects have gone. **Regeneration is not a route that exists for them**, so the
ruling's limb 3 cannot be executed over them and no bound on their movement can be met, because
there is no movement to bound. Recorded as **F19**.

### 4.d ★ Ground two: the one member that regenerates cleanly would replace the ratified classification

`gen_decisions_filter.py` is the check whose artifact IS the classification the user ratified —
411 DECIDING-ACT-NAMED, 182 NO-DECIDING-ACT-FOUND, 84 EVIDENCE-AMBIGUOUS. It regenerates without
complaint, and what it produces is a **different classification of a different population**:

```
  DECIDING-ACT-NAMED: 421 (proposed KEEP)
  EVIDENCE-AMBIGUOUS: 28 (proposed NEEDS-THE-USER)
  NO-DECIDING-ACT-FOUND: 63 (proposed SOFT-DISCARD candidate)
```

Diffed blob against blob at explicit hashes, the movement is:

```
3806	8298	tools/audit/decisions_filter_classification.json
353	2128	ratification_surfaces/cowork_decisions_filter_surface_2026_08_15.md
```

— 8298 lines removed from the classification artifact and 2128 from the ruling surface the user
read before ruling. **Regenerating this member replaces the record of the ruling that the act is
executing.** That is the [[OI-330]] shape at its sharpest: a completed measurement restated against
the population the act itself changed. Recorded as **F20**. *(The regeneration was performed, its
movement measured at the objects, and both files restored — the hashes above under §4.a are the
proof.)*

### 4.e ★ Ground three: the regeneration that IS available moves a user-ruled retirement candidacy set

`gen_artifact_inventory_surface.py` regenerates cleanly, and its whole movement is small — **9
insertions, 14 deletions**. What those lines carry is not small:

```
-**NAMED in the governing record — 84 of 113 files.**
+**NAMED in the governing record — 82 of 113 files.**
-- `cowork_l1l4_architecture_audit.md`
-- `cowork_types_header_design.md`
+- `cowork_l1l4_architecture_audit.md`      (moved to the NAMED NOWHERE side)
+- `cowork_types_header_design.md`          (moved to the NAMED NOWHERE side)
-- `cc_corpus_wave3_report.md`
+- `cc_corpus_wave3_report.md`              (moved to the NAMED NOWHERE side)
-> **122 of those 571 ignored files are NAMED by the governing record.**
+> **117 of those 571 ignored files are NAMED by the governing record.**
```

Three documents move from the cited side to the uncited side of the citation split — and **the
uncited side is the retirement-candidate side**. Two of them (`cowork_l1l4_architecture_audit.md`,
`cowork_types_header_design.md`) are documents whose HOME standing the discard population alone
carried, so their movement is inside the bound. **`cc_corpus_wave3_report.md` is not**: no
decisions-register entry is homed there at all, and it moves because the only citation of it in the
governing record sat
inside a retired entry's own text. Its standing was carried by discard-population entries **by
CITATION**, which is neither of the bound's two named categories — *"a document whose class or home
standing those entries alone carried"* — and the ruling's instruction on any other movement is a
STOP-and-report. Five further files leave the 122-name list a user ruling landed. Recorded as
**F21**. *(Measured and restored; the hash under §4.a is the proof.)*

`gen_retirement_caller_check.py`, whose flags are imported from that same surface, could not even be
run in write mode without naming a commit: `STOP: --at <commit> is required when writing: the reading
is a statement about one tree and the commit is part of the finding`.

### 4.f So A3 is falsified, and the dispatch's own instruction is a STOP-and-report

A3 states that with the ruled reach applied — historical reclassification, bounded regeneration and
the mechanism work — **no red survives except [[OI-372]]'s tool**. Five STANDING members cannot be
regenerated at all; a sixth can be regenerated only by replacing the record of the ruling being
executed; a seventh moves a user-ruled candidacy set partly outside the bound. **Reds survive, and
the ruling authorizes the enumerated movement and nothing else.**

**What a reader must not conclude is that the ruling is in doubt.** The user ruled the reach, and
three of its four limbs are measured sound (§4.b). What this measurement establishes is narrower and
sharper than the third batch's: **the class of check the ruling calls STANDING is not one class.** It
holds checks that re-derive over the changed record (two of them), checks whose authored tables lose
their subjects and REFUSE rather than re-derive (five), and one check whose artifact is the ruling's
own evidence. Only the first kind is what "regenerated by their own generators" describes.

---

## 5. The new-tool rule, discharged twice

Each check this batch adds joined the derived guard-candidate population the moment it existed, and
**each landed WITH its authored run-instruction and its authored classification verdict in the SAME
commit that adds it**. Both take `--check` and never the bare invocation, for a reason about the
tools: run with no flag each REWRITES its committed artifact, and both artifacts are read BEFORE an
irreversible act rather than after it, which is the [[OI-301]] hazard at its sharpest.

**One apparatus finding rides with them (F26).** The reader enumeration's first implementation
spawned one process per tracked file and took about five minutes; rewritten to ask `git grep` once
per name it takes **14.6 seconds** and produces a **byte-identical artifact**, proven by diffing the
two runs' outputs. It is recorded because a guard set nobody wants to run is a guard set nobody runs,
which is the ground R4's own classification rests on.

---

## 6. Every registered expectation, graded

- **E0 — MET.** Exactly 4 paths at `git diff-tree` on `f92f27fc3b`; two modifications and two
  additions; no staging override of any kind. A1's two shapes checked blob against blob by explicit
  hash before the commit — with the hunk-count remark at §1.b (**F25**), which is about the premise's
  wording and not about the difference.
- **E1 — MET.** Every red check covered with one verdict and its evidence — 15 members, 6 SUPERSEDED
  and 9 STANDING, each carrying its imports, its own stated purpose and the derived explanation of
  its red. R1's enumeration published with **zero LIVE consumers** outside the superseded program.
  **No decisions-register file** and no guard-classification record touched in this task's commit
  beyond the ordinary registration of the two new checks.
- **E2 — NOT MET, AND NOT ATTEMPTED TO BE MET.** The act it grades was not performed. The data-file
  diff, the regenerated files, the arithmetic in the close and the byte-preservation it demands all
  describe a commit that does not exist. What is recorded instead is §4: the derivation, the
  measurement, the revert proven at the objects, and the three grounds on which A3 fails.
  `gen_decisions_register.py --check` and `gen_cluster_dispositions.py --verify` both pass at the end
  state — **at the UNCHANGED decisions register**, which is a different fact from the one E2 asks for
  and is not offered as it.
- **E3 — see §7**, and the ordering rule the dispatch imposes was obeyed.

---

## 7. The end state, and the ordering rule

After Task 1's commit the guard set stands at **57 run, 56 passing, ONE failing**
(`gen_filing_convention_application.py --check`, [[OI-372]]), 4 not run, 10 historical, **zero
STOPs**, with both of this batch's new checks inside the classified population under authored
verdicts and both passing. **No failing check other than [[OI-372]] survives in the committed tree.**

Per the dispatch's ordering rule — *no graded value is committed before the run that produced it* —
the end-state run demonstrated across the commit boundary is taken AFTER the Task 3 commit exists,
and its output and the final SHAs land in **one further commit**. **The E3-ordering defect that rule
exists against is not repeated: no expectation anywhere in this report was written before its
measurement, and the one expectation this batch does not meet is graded NOT MET rather than
reconciled towards.**

---

## 8. Surfaced findings (D-641, #13, #19) — surfaced, not rowed

The dispatch bars creating an open-items row, so each is stated here and in the close.

- **F19 (new, the largest) — the ruling's REGENERATE limb does not exist for five of the nine
  STANDING members.** Four refuse in WRITE mode, writing nothing; a fifth halts on its imported
  population. §4.c.
- **F20 (new) — the one STANDING member that regenerates cleanly would replace the ratified
  classification the discard ruling rests on**, 411/182/84 becoming 421/63/28, and rewrite the ruling
  surface the user read. §4.d.
- **F21 (new) — the regeneration that IS available moves a user-ruled retirement candidacy set**, and
  one moved document's standing was carried by discard-population entries only by CITATION, which is
  outside the bound's two named categories. §4.e.
- **F22 (new) — freezing the phase-1 completion inventory ossifies a population two links below a
  LIVE rule.** `gen_true_half_reach_rows.py` reads it as its population and its own artifact is read
  by `gen_nongating_apparatus_rows.py`, which derives D-438's declaration. Nothing halts; what stops
  is movement. §2.d.
- **F23 (new) — the committed report's §4.c block abbreviates two of its reasons**, so a split
  derived from that prose alone cannot place them; the explanation is derived from each check's own
  inputs as well, and every row says which signal placed it. §3.c.
- **F24 (new) — a captured `[FAIL]` line records only the FIRST halt a check reaches.**
  `gen_phase1w_legacy_verification.py` is recorded in the third batch's block with the F15
  anchored-quote STOP; at a tree where that STOP has not yet been created it halts on a larger one —
  thirty authored verdicts whose subjects the retirement removes. Both are real; a reader of one
  captured line meets one of them. §4.c.
- **F25 (new, small) — A1's "ONE contiguous changed passage" is a count the difference does not
  have.** The content is exactly what A1 names; git reports two hunks because two unchanged lines sit
  between the insertion and the rewrite. This is the F18 family repeating in a smaller form. §1.b.
- **F26 (new, small) — the first implementation of the R1 check made the guard set unusable**
  (about five minutes for one check); the `git grep` form runs in 14.6 seconds with a byte-identical
  artifact. §5.
- **F1–F18 (carried, unchanged)**, including **F3**, now six times surfaced —
  `reaim_home_anchors.py --check` exits 0 while printing drifted anchors, and
  `gen_cluster_dispositions.py --verify` is the drift authority. **Still unfixed and unrowed: the
  dispatch bars both.** **F17 did NOT repeat** in this batch (§1.b).
- **The E3 ordering defect and the A1 premise error of the earlier batches** ride to the phase's
  retrospective as the dispatch orders.
- **No finding bearing on the analysis, its inputs, or a measurement tool the analysis depends on.**
  Every subject of this batch is the project's own record and the apparatus that reads it.

---

## 9. What this batch did NOT do

**No entry was discarded, retired, edited, moved or marked, and no decisions-register file was
changed — proven by hashing every touched file against its committed blob after the revert.** No
check was reclassified historical and no artifact was frozen. The 29 withheld sole-carriers and the
62 are not ruled and not touched; the residue surface and the rulings-sort surface stand awaiting
their own sittings. No archiving, no file moved, renamed or deleted; no mining, no landing; the eight
KIND-UNDERIVABLE callers and the prose-citation question stay open; every retirement flag stays a
candidacy. No empirical findings ledger, no fact-gate admission, no curated boot list. **No
completion claim of any kind about the superseded phase-1 program.** No derivation of any
specification, no design, no repair, no pilot act. **No `src/` change, no golden, no test changed,
moved or run, nothing under `tools/corpus/` or `tools/robust_stop/`, no measurement of the
analysis.** **No open-items row created, flipped or discarded** — [[OI-372]] and [[OI-374]] stay
exactly as found, [[OI-179]] stays OPEN and GATES, and `reaim_home_anchors.py`'s F3 defect stays
surfaced, unfixed and unrowed.

*Provenance: CC, 2026-08-16, dispatch `cc_instruction_preparation_fourth.md`. Task 0 is commit
`f92f27fc3b` (parent `660aa4609e`), pushed, four paths. Task 1 is `5a687aea9c` (parent
`f92f27fc3b`), pushed, eight paths. Task 2 is a STOP and carries no commit — the act was derived,
applied, measured and reverted, and the revert is proven at the objects in §4.a. Task 3's close and
this report are the next commit; **E3's run and the final SHAs are recorded in the ONE FURTHER commit
after it**, so no graded value is committed before the run that produced it. **★ WHERE THE RECORDING
TERMINATES, STATED RATHER THAN LEFT AS A GAP:** every commit of this batch is verified at the object
and named except the LAST one — the commit carrying this sentence — because a commit cannot contain
its own identity. That is the terminus, not an omission.*
