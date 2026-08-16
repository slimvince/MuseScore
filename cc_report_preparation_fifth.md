# CC report — the preparation phase's FIFTH batch

> **What this is.** The coding side's report on `cc_instruction_preparation_fifth.md`, performed
> 2026-08-16. The batch record beside it is THE PREPARATION FIFTH BATCH section of
> `cowork_away_returns.md`; this file is the whole of what the coding side says back.
>
> **THE HEADLINE, BEFORE ANY DETAIL.** **All three tasks are performed and nothing in this batch is
> a STOP.** The ruled soft-discard — derived, applied, measured and REVERTED by the third batch, and
> again by the fourth — is **EXECUTED**: 165 entries retired, 512 live, 677 before, to the digit.
> Every STANDING check is treated by its own kind as §6 rules; the six SUPERSEDED checks are
> historical with their artifacts frozen; and §5(A)'s read-only pruning measurement is delivered
> with its ratification surface. **The guard set ends at one failing check — [[OI-372]]'s — and no
> other.**
>
> **FIVE THINGS THE USER SHOULD READ BEFORE ANYTHING ELSE.** *(1)* **Nothing was destroyed, and it
> is proven rather than asserted** — every retired entry byte-preserved against its pre-act blob,
> exactly ten live entries changed and each only by an appended provenance stamp (§3.b). *(2)* **The
> kind-2 treatment needed a grain the ruling's own words do not name** — a discard can empty a
> SECTION without emptying its document — and that is declared rather than glossed (§3.d, F27).
> *(3)* **F15's anchored-quote remap was NOT owed and none was performed**, because this batch's
> insertion sits below the anchored lines rather than above them (§3.f, F28). *(4)* **The pruning
> measurement's first span unit was too coarse for `CLAUDE.md` and mis-classed a quarter of that
> file in the ARCHIVE direction** — the direction the ruled doubt default exists to prevent — and
> the correction is at the tool, measured (§4.c, F29). *(5)* **One class on the ratification surface
> returns to the user UNDECIDED** rather than stretched to a verdict (§4.e).
>
> *(Every guard count lives at `tools/audit/guard_state.json`; the kind-2 move list at
> `tools/audit/decisions/retired_subject_moves.json`; the kind-3 movement classification at
> `tools/audit/census_movement_classification.json`; the pruning measurement at
> `tools/audit/governing_surface_spans.json` and `tools/audit/governing_surface_readers.json`. None
> is restated here beyond the few this report is reporting ABOUT, each naming where it was read —
> **D-431**. Every value below that is not from a committed artifact is QUOTED from the run that
> produced it rather than transcribed.)*

---

## 1. The reading scope, both guard-set states, and Task 0

### 1.a The ruled interim reading scope, stated because the ruling requires it on the record

The session-start reads ran under **§5(B)** of `cowork_rulings_2026_08_16_preparation_return.md`: in
`CLAUDE.md`, the blocks that state of themselves that they are historical or superseded — the frozen
historical case enumerations, the superseded baseline narratives, the preserved former wordings of
amended rules — were **SKIPPED**. `STATUS.md` was read at its header and `BUILD_AND_TEST.md` in
full. The dispatch states the scope in its read-first block, citing the ruling, and this paragraph
is the other half of that: **what was skipped is on the record and checkable.**

### 1.b The start state, taken before the first edit

`gen_guard_state.py --check` printed **"the guard state re-derives"** — **57 guards run, 56 passing,
ONE failing** (`gen_filing_convention_application.py --check`, which is [[OI-372]]), 4 not run, 10
historical records, **no STOP**, and no stale report. `gen_guard_classification.py --check` printed
**"the guard classification re-derives"**. **This is exactly the start state the dispatch declares
as expected**, so no STOP-and-report was owed on it.

### 1.c Assumption A1, checked first and entirely at content-addressed objects

The sanctioned enumeration `tools/audit/changed_paths.py` reported **exactly TWO tracked
modifications in the whole working tree** — `cowork_handoff.md` and
`cowork_rulings_2026_08_16_preparation_return.md` — with `cc_instruction_preparation_fifth.md` and
`ratification_surfaces/cowork_standing_treatment_surface_2026_08_16.md` untracked, and no third
tracked difference anywhere.

Each difference was then taken **blob against blob by explicit hash**, the committed blob resolved
from the commit the record's chain terminates at and the working blob written into the object store
by `git hash-object -w`:

- `cowork_handoff.md` — **98 insertions, 1 deletion, ONE hunk**: the twenty-first session-close
  block inserted, and the twentieth block's heading replaced by the same heading carrying this
  file's own demotion marker. **Exactly the two parts of one act A1 names.**
- `cowork_rulings_2026_08_16_preparation_return.md` — **193 insertions, 2 deletions, two hunks**:
  §5, §6 and §7 inserted before the provenance block, and that block rewritten in place. **Exactly
  the shape A1 names.** A1's own sentence describes two parts — an insertion and a rewrite — so the
  two-hunk count is what it describes rather than the F25 mismatch of the previous batch. **F25 does
  not repeat**, and neither does F17: no premise of this dispatch names a terminus commit.

**No tracked difference outside the shape A1 names**, so the ordered STOP was not reached.

### 1.d Task 0 — commit `b73d1c7b4e`, parent `338fa9fe82`, pushed

Exactly the four paths the dispatch names and no fifth — two modifications, two additions — verified
at the index through the sanctioned tool before the commit and at the object after it. All staged
**plainly**; no override of any kind. That the parent is `338fa9fe82` is what establishes at the
object that the premise's commit was the current committed state. **E0 is MET.**

---

## 2. What the act had to be, before it could be performed

Three things the two previous batches measured had to be built or corrected before the ruled act
could be carried through honestly. They are stated first because each is a change to the mechanism
rather than to the record, and a reader should meet them before the act's own numbers.

**(i) The renderer's retired-block STOPs.** `gen_decisions_register.py` is the ONE place the live
record is produced from the data, so it is where the retired block's demands are made: an entry
identity in BOTH blocks halts it — a retired entry re-appearing live is the failure the block exists
to make impossible, and it would otherwise render silently; the arithmetic must account for the
population the block records as its own former one, which is how an entry in NEITHER block is
caught; and a retired record with no entry identity halts it. A data file with no retired block is
the state before any retirement and is not a fault.

**(ii) The establishment pass consulting the retired block.** A soft-discarded entry is retired and
**not destroyed**, so a surviving entry that names one is pointing at something the record still
holds, and reporting it DANGLING would say the opposite. `gen_cluster_dispositions.py --verify` now
consults the retired block beside the live entries — and nothing else widens: no retired entry's
verbatim is located, no retired home is checked, and no count moves.

**(iii) The retiring act is named for what it is.** The tool recorded the THIRD batch as the
retiring dispatch. That batch planned the act and reverted it; so did the fourth. The record now
names the batch that performed it. **A record saying the third dispatch retired these entries would
state something false about who did it**, and the correction is declared here rather than left in a
diff.

**And one further correction the act forced (F31).** The committed plan `soft_discard_application.json`
carried a block saying **NOT APPLIED**. After the act that block is false, and the plan **cannot be
regenerated**: its population is no longer live, so `population()` STOPs by construction — that
guard working. The one block whose subject is the act's STATE is therefore rewritten at the moment
the state changes, its former text preserved verbatim (#12), and the tool's own `--check` reads it
back and STOPs if the plan and the data file disagree about the arithmetic. **No other field of the
plan moves**: the population, the ten stamps and the measured reach are the planning act's record
and are not re-derived against the record the act changed.

---

## 3. Task 1 — the ruled soft-discard, EXECUTED, complete

Commit **`26afbc0f75`**, parent `b73d1c7b4e`, pushed, **46 paths**, verified at the object.

### 3.a The act, and the arithmetic to the digit

```
applied: 165 entries retired, 512 live (was 677), 10 provenance stamps written
```

and, re-checked afterwards through the register's own mechanism:

```
the soft-discard re-checks: 512 live + 165 retired = 677 before, no entry in both blocks and none
in neither, every retired record carrying its finding, its date, its authority and the ruled clause
```

The register was regenerated **by its own generator** — `wrote 21 files: DECISIONS.md (the index,
901 lines) + 20 group files under decisions/ (512 decisions)` — and its `--check` then printed `the
register matches the data`. The establishment pass, with the retired block consulted, prints:

```
backbone decisions: 512
cross-references resolving: ALL
verbatim quotes found at their cited home: 512/512
cited line numbers correct: 506/506   (6 cited to a file with no line number, by design)
```

### 3.b ★ Nothing was destroyed, and it is proven rather than asserted

Every retired entry was compared against its own text at the pre-act commit, field by field:

```
before live: 677  after live: 512  retired: 165
arithmetic: 512 + 165 = 677 vs 677 -> BALANCES
retired entries NOT byte-preserved: 0 []
live entries with an APPENDED status_source stamp: 10 ['D-004', 'D-008', 'D-009', 'D-021', 'D-123',
                                                       'D-248', 'D-315', 'D-403', 'D-410', 'D-411']
live entries changed in any other way: 0 []
```

The ten are the user's own **(B1)** keeps, and each stamp is APPENDED to `status_source` and to
nothing else. **No live entry changed in any other way**, which is the demand the act's own
ratification rests on.

### 3.c Kind 1 — the two rulings' evidence, PINNED, with each run proving its own pin

`gen_decisions_filter.py` and `gen_deciding_act_recovery.py` now read their inputs from the git
objects at the commit each artifact was produced at — the filter's at
`cc_instruction_preparation_opening.md` Task 2, the recovery pass's at
`cc_instruction_preparation_second.md` Task 2, both located in those batches' own reports rather
than recalled.

**★ ONE JUDGMENT IS DECLARED RATHER THAN BURIED.** The ruling says the checks read *"from the git
objects at the commit each committed artifact records"*, and **neither artifact records a commit**.
It also says the artifacts stand **byte-unchanged**, so neither may GAIN such a field: adding one is
a change. The two demands are reconcilable in exactly one way, and it is the way taken — **the pin
lives in the tool**. It is not taken on trust: each run reads **THAT ARTIFACT ITSELF** out of the
git object at the pinned commit and STOPs unless it is identical to the artifact on disk. A pin
naming the wrong commit, or an artifact that has moved off its pin, therefore halts rather than
silently re-deriving against the wrong state. **The wrong-pin STOP fired for real** on the first run
of the filter, for a different cause — a byte comparison against a working tree checked out with
platform line endings — and the comparison is now made as text, which is the reading `--check`
already uses for every other file those tools emit.

Both artifacts and both ruling surfaces are **byte-identical to their pre-act blobs, proven by
hash**.

### 3.d ★ Kind 2 — five tables, not four, and the reason is a grain the ruling does not name (F27)

The ruling names four authored judgment tables. The move list is DERIVED and published at
`tools/audit/decisions/retired_subject_moves.json`; **53 judgments moved**:

| table | moved | still watching live subjects |
|---|---:|---:|
| the `CLAUDE.md` rule triage | 1 | 87 |
| the legacy-mark verification | 30 | 62 |
| the register data's authored home judgments | 3 | 35 |
| the delegation bar's FORM judgments | 3 | 35 |
| **the section-kind judgments (the fifth)** | **16** | **88** |

**The fifth table is the finding.** The discard can empty a **SECTION** without emptying the
document that holds it, so a section-kind judgment loses its deciding entries while its document
keeps live ones. The ruling's two categories name entries and documents; they do not name sections.
The treatment was applied at that grain **on the ruling's own logic** — the judgment moves verbatim
with its subject reference, membership derived, a judgment in neither section halting — and the
membership derivation is IMPORTED from the classifier that owns the section assignment rather than
restated (#6), so the move list and that tool's own STOP cannot disagree about which judgments move.
**It is an extension of a ruled treatment by reasoning rather than by the ruling's words, and it is
declared for that reason.**

**Every move is byte-preserved and no surviving live judgment changed**, proven by loading each
table at the pre-act commit and comparing:

```
triage moved: 1 NOT byte-preserved: []
phase1w moved: 30 NOT byte-preserved: []
FORMS moved: 3 [...] NOT byte-preserved: []
moved document judgments: 3 NOT byte-preserved: []
moved section-kind judgments: 16 NOT byte-preserved: []
triage live changed: []      phase1w live changed: []      FORMS live changed: []
```

The thirty legacy-marking verdicts are **F24's set exactly**. Every table carries STOPs in both
directions: a judgment in both sections halts, a judgment whose subject is live again halts, a
judgment whose subject the discard retired and which is still live halts, and a judgment whose
membership cannot be derived **STOPS to the user**.

**One limit of the derivation is declared.** A judgment already on a retired side for an EARLIER
act's reason — the re-homing waves — is left where that act's own record put it and is not
re-derived here: this tool is not the authority for retirements it did not perform. What IS still
asked of every one of them is the direction that must never go unnoticed — that its subject has not
become live again. The first version of the rule did not draw that line and **STOPPED on 24 such
judgments**, which is how the line was found.

### 3.e Kind 3 — every moved census value enumerated and classed, none outside the bound

`tools/audit/census_movement_classification.json` re-runs the **citation scan itself** at both states
— the earlier one from the git objects at the pre-act commit — rather than diffing two rendered
surfaces, and imports the scan and the governing-record definition from the census that owns them
(#6). Result:

```
moved: 26
  citation-carried-standing: 24
  home-standing: 2
```

The two home-standing crossings are `cowork_l1l4_architecture_audit.md` (D-577, D-578) and
`cowork_types_header_design.md` (D-610). The twenty-four citation-carried crossings include
`cc_corpus_wave3_report.md` — the case F21 named, whose only naming in the governing record sat
inside a retired entry's own text, which is exactly the category the ruling WIDENED the bound by.
**A name ENTERING the scan would halt the tool; none did.** The caller-check was regenerated with
the commit its own interface requires, and its whole movement is that one document entering the
flagged population and ceasing to hold others.

**A crossing confers CANDIDACY only.** Every ruled condition on a candidacy — mined first, members
seen by the user first for the stray root files, the caller-check at the objects — stands untouched,
and nothing was archived, moved or deleted.

### 3.f ★ F15's remap was not owed, and no remap was performed (F28)

The third batch measured that teaching the register's renderer about the retired block moved an
anchored quote from line 514 to 576, and the dispatch orders the remap per citation from the
`--verify` drift report. **This batch's insertion sits BELOW the anchored lines rather than above
them**, so nothing moved:

```
gen_cluster_dispositions.py --verify : cited line numbers correct: 506/506
reaim_home_anchors.py --check        : anchors drifted: 0
```

**No remap was performed and none was owed.** It is stated because the dispatch orders one, and a
silent omission would read as a remap done.

### 3.g The six SUPERSEDED checks, historical

Reclassified through the guard mechanism's own **two** records — the invocation consequence in the
runner and the verdict with its evidence in the classification, which STOP if they disagree in
either direction (#6). **Assumption A3 holds**: the mechanism can express it, and no improvisation
was needed. Each former verdict is preserved verbatim (#12), and each new one states what the
reclassification does and does not assert.

**Historical status records that these checks graded a SUPERSEDED PROGRAM. It asserts nothing about
whether that program's obligations were discharged, and no completion claim of any kind rides it.**
All six committed artifacts are byte-identical to their pre-act blobs:

```
IDENTICAL tools/audit/phase1_completion_inventory.json          4993aa5b59452cd3458610ecb1782464d00b8a30
IDENTICAL tools/audit/phase1_finish_line.json                   176e2b66da99ca9730c4ffe582b62e9f00ac4069
IDENTICAL tools/audit/decisions/outstanding_delegations.json     50ca874c44486afc94cc225abf0089d771b3345e
IDENTICAL tools/audit/decisions/finish_line_item1_routes.json    cd6ace6e542fbf5b7b373dc6a560443e1b9642d7
IDENTICAL tools/audit/decisions/item1_rehome_blocker.json        ed3bc0b3a3173f430d070e1b5d13a2d0170cb1dc
IDENTICAL tools/audit/decisions/r1_superseded_reach.json         9e87349e69ab144f6d134f70c6ef8f8b3ca9f684
IDENTICAL tools/audit/decisions_filter_classification.json       d738e7e0aff4d42a7ae5fc3a8978fdfaffd8ce6d
IDENTICAL tools/audit/deciding_act_recovery.json                 ffc97cf4e1602b70c69856c6798655a780a10f8f
```

### 3.h A2's check, ordered as Task 1's last step

Run at the applied tree **before** the treatments, the guard set reported **exactly the fifteen reds
the split carries and no sixteenth** — the population CONFIRMED a second time, at a second applied
tree. After the treatments it reports **one failing check and no other**:

```
55 guard(s) run, 1 failing, 4 not run, 16 historical record(s)
  [FAIL] tools/audit/gen_filing_convention_application.py --check
```

**A2 HOLDS.** [[OI-372]]'s tool is untouched, and F22's ossification is accepted as the ruling
records it.

---

## 4. Task 2 — the governing-surface pruning, MEASURED, read-only

Commit **`c4f15a7b32`**, parent `26afbc0f75`, pushed, **9 paths**, verified at the object.

**NOT ONE OF THE FIVE GOVERNING FILES WAS EDITED.** The sanctioned enumeration reports the only
tracked modifications in this task as the guard set's own two registration files and their two
artifacts.

### 4.a What was measured, and how big the subject is

| file | characters | spans | anchored namings into it | register entries homed here |
|---|---:|---:|---:|---:|
| `CLAUDE.md` | 156,068 | 156 | 1,354 | 87 |
| `OPEN_ITEMS.md` | 610,413 | 408 | 129 | 1 |
| `DECISIONS.md` | 132,664 | 658 | 0 | 0 |
| `STATUS.md` | 505,057 | 150 | 79 | 0 |
| `BUILD_AND_TEST.md` | 28,010 | 130 | 34 | 1 |

*(Read from `tools/audit/governing_surface_spans.json` and
`tools/audit/governing_surface_readers.json`, which are where these values live; the surface is
generated from both and no figure here is typed by hand.)*

### 4.b The decomposition's own STOP fired for real on the first run

The load-bearing demand is that the per-class byte counts account for each file **exactly** — a span
silently dropped would make every number meaningless. It failed by four characters on the first run:
a blank line inside a fenced code block was counted both as part of its span and as a separator. The
reconciliation now separates the two, and no number was published until it balanced.

### 4.c ★ Two corrections made at the tool rather than lived with, both measured

**(i) The span unit was too coarse for `CLAUDE.md` (F29).** A principle of that file carries no blank
line from end to end, so one `FORMER WORDING` marker inside it classed the whole principle —
**26.8% of the file** — as archive material. That is an error in the ARCHIVE direction, which is the
one the ruled doubt default exists to prevent. The span rule now cuts a block again at the record's
**own** star marker, which is how `CLAUDE.md` opens every amendment; the file's doubt-defaulted share
rose from 102,186 to 120,169 characters as a result, which is the correction working.

**(ii) The ordering placed a `STATUS.md` entry by a phrase it merely contains.** A dated entry
recording a completed batch is that batch's entry whatever else it mentions, so the pointer test now
runs before the former-wording test for that file.

**The residual risk is stated rather than left to be found**, and it is written into the surface: a
span that is MIXED at a finer grain is still classed by its marker, the error still runs in the
archive direction, and the executing dispatch must therefore read every span it archives rather than
trusting its class.

### 4.d The reader measurement, and one thing it may not record (F30)

The inventory is the F13 lesson applied prospectively — a mutation's reach is MEASURED before the
act. It publishes, per file, every naming, every **anchored** citation into it, every tool that reads
or parses it by path, and every register entry homed in it.

**No naming is recorded by the line it was found on.** The first version did, and a single field
drifted by one line between two runs of the guard classification with nothing in the record having
moved — because several of the files that name these five are GENERATED. That is the OI-301/OI-305
shape, and a coordinate is the wrong locator anyway under the record's own rule (D-307). A naming is
located by its content instead. **This measurement's own three outputs are also excluded from its
scan**, for the same reason and stated in the tool: each names all five files, so counting them
would make the artifact unreproducible by construction.

### 4.e ★ One class returns to the user UNDECIDED

The `STATUS.md` dated entries recording completed batches are **89.8% of that file** and the single
largest block of the five. The readership test does not settle them: `STATUS.md` carries its **own**
archive rule — a superseded entry moves to `STATUS_ARCHIVE.md` instead of accumulating — and ruling
(C) already brings that rule into the executing act. **The surface asks the question rather than
answering it**, and the ruled default holds until it is answered.

The surface also asks whether the **doubt-defaulted share** is acceptable as it stands. It is the
largest share of every one of the five files, and under the ruled default every character of it
stays at site.

**E2 is MET**: every span of all five files is classed with its evidence, the surface is generated
rather than hand-typed, no governing file is edited, and both new tools are registered under the
new-tool rule with `--check` forms.

---

## 5. The new-tool rule, discharged four times

Each check this batch adds joined the derived guard-candidate population the moment it existed, and
**each landed WITH its authored run-instruction and its authored classification verdict in the SAME
commit that adds it**: `gen_retired_subject_moves.py` and `gen_census_movement_classification.py`
with Task 1, `gen_governing_surface_spans.py` and `gen_governing_surface_readers.py` with Task 2.
All four take `--check` and never the bare invocation, for a reason about the tools: run with no
flag each REWRITES its committed artifact, and one of them rewrites a ruling surface awaiting the
user as well.

**The runner's own STOP caught two of them before they could be left unrun** — `derived candidate(s)
with no authored invocation` — which is that guard working exactly as written.

---

## 6. Every registered expectation, graded

- **E0 — MET.** Exactly 4 paths at `git diff-tree` on `b73d1c7b4e`; two modifications whose content
  matches A1's stated shapes, two additions; no staging override of any kind. A1's two shapes checked
  blob against blob by explicit hash before the commit.
- **E1 — MET.** The register's data-file diff touches the retired-block addition, the moved entries
  and the ten stamps and nothing else — proven field by field against the pre-act blob. **Live +
  retired = 677 BY ARITHMETIC**, stated to the digit. Nothing destroyed: every retired entry and
  every moved judgment byte-preserved. `gen_decisions_register.py --check` and
  `gen_cluster_dispositions.py --verify` both re-derive clean. The pinned artifacts and the six
  frozen artifacts are byte-identical to their pre-batch blobs, proven by hash (§3.g). Every kind-2
  move (§3.d) and every kind-3 movement (§3.e) is enumerated in the close.
- **E2 — MET.** Every span of all five files classed with evidence; the surface generated from the
  two artifacts, not hand-typed; **no edit to any of the five files**; both new tools registered
  under the new-tool rule with `--check` forms.
- **E3 — see §7**, and the ordering rule the dispatch imposes was obeyed.

---

## 7. The end state, and the ordering rule

After Task 2's commit the guard set stands at **55 run, 54 passing, ONE failing**
(`gen_filing_convention_application.py --check`, [[OI-372]]), 4 not run, **16 historical**, **zero
STOPs**, with all four of this batch's new checks inside the classified population under authored
verdicts and all four passing. **No failing check other than [[OI-372]] survives in the committed
tree.**

**★ E3 — TO BE GRADED ON THE RUN TAKEN AFTER THE COMMIT THAT CARRIES THIS SECTION.** Per the
dispatch's ordering rule — *no graded value is committed before the run that produced it* — the
end-state run demonstrated across the commit boundary is taken AFTER Task 3's close commit exists,
and its output and the final SHAs land in **one further commit**. **The E3-ordering defect that rule
exists against is not repeated: no expectation anywhere in this report was written before its
measurement.**

---

## 8. Surfaced findings (D-641, #13, #19) — surfaced, not rowed

The dispatch bars creating an open-items row, so each is stated here and in the close.

- **F27 (new, the largest) — the ruled kind-2 treatment needed a grain the ruling's own words do not
  name.** The discard empties a SECTION without emptying its document, so 16 section-kind judgments
  in eight documents that remain live homes lost their deciding entries. The treatment was applied
  at that grain on the ruling's own logic, with membership derived and each moved judgment carrying
  the retired entries it decided. §3.d.
- **F28 (new) — F15's anchored-quote remap was NOT owed and none was performed**, because this
  batch's insertion sits below the anchored lines. Both drift authorities report zero. §3.f.
- **F29 (new) — the span decomposition's first unit was too coarse for `CLAUDE.md`, and the error
  ran in the ARCHIVE direction** — 26.8% of the file. Corrected at the tool by cutting at the
  record's own star marker; the residual risk at a finer grain is written into the surface. §4.c.
- **F30 (new) — a line number inside a GENERATED file makes an artifact unreproducible by
  construction.** Measured: one field drifted by a single line between two runs of the guard
  classification with nothing in the record having moved. §4.d.
- **F31 (new, small) — a committed plan's own statement about its state can outlive the act it
  plans**, and cannot be corrected by regeneration once the act has happened. The state block is now
  rewritten at the moment the state changes, its former text preserved (#12). §2.
- **F1–F26 (carried, unchanged)**, including **F3**, now seven times surfaced —
  `reaim_home_anchors.py --check` exits 0 while printing drifted anchors, and
  `gen_cluster_dispositions.py --verify` is the drift authority. **Still unfixed and unrowed: the
  dispatch bars both.** **F17 and F25 did NOT repeat** (§1.c).
- **The E3 ordering defect and the A1 premise error of the earlier batches** ride to the phase's
  retrospective as the dispatch orders.
- **No finding bearing on the analysis, its inputs, or a measurement tool the analysis depends on.**
  Every subject of this batch is the project's own record and the apparatus that reads it.

---

## 9. What this batch did NOT do

**No pruning fate was executed and no governing file was edited by Task 2** — the surface proposes,
the user rules, a LATER dispatch executes. **No sole-carrier member was discarded; the 62 are not
ruled; the residue surface and the rulings-sort surface stand awaiting their own sittings.** No
archiving, no file moved, renamed or deleted; no mining, no landing; the eight KIND-UNDERIVABLE
callers and the prose-citation question stay open; **every retirement flag stays a candidacy — a
census crossing confers candidacy only.** No empirical findings ledger, no fact-gate admission, no
curated boot list. **No completion claim of any kind about the superseded phase-1 program.** No
derivation of any specification, no design, no repair, no pilot act. **No `src/` change, no golden,
no test changed, moved or run, nothing under `tools/corpus/` or `tools/robust_stop/`, no measurement
of the analysis.** **No open-items row created, flipped or discarded** — [[OI-372]] and [[OI-374]]
stay exactly as found, [[OI-179]] stays OPEN and GATES, and `reaim_home_anchors.py`'s F3 defect
stays surfaced, unfixed and unrowed.

*Provenance: CC, 2026-08-16, dispatch `cc_instruction_preparation_fifth.md`. Task 0 is commit
`b73d1c7b4e` (parent `338fa9fe82`), pushed, four paths. Task 1 is `26afbc0f75` (parent
`b73d1c7b4e`), pushed, 46 paths. Task 2 is `c4f15a7b32` (parent `26afbc0f75`), pushed, nine paths.
Task 3's close and this report are the next commit; **E3's run and the final SHAs are recorded in
the ONE FURTHER commit after it**, so no graded value is committed before the run that produced it.
**★ WHERE THE RECORDING TERMINATES, STATED RATHER THAN LEFT AS A GAP:** every commit of this batch is
verified at the object and named except the LAST one — the commit carrying this sentence — because a
commit cannot contain its own identity. That is the terminus, not an omission.*
