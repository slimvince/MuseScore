# CC report — the informed-framework ruling landed, the `framework` subject RETIRED from the boot-pack generator, and the fourth failing guard check GREEN

> **STATUS: A SESSION REPORT.** Written by the executing side (Claude Code, 2026-08-28) under
> `cc_instruction_framework_arrangement_landing.md`, which executes the consequences of
> `cowork_rulings_2026_08_28_informed_framework_sitting.md`.
>
> **WHAT THIS BATCH DID.** It landed the writing side's five untracked files and the modified
> handoff and pushed; it deleted the two authored `framework` entries from
> `tools/audit/gen_derivation_boot_pack.py` and wrote one comment at the point of deletion saying
> why the subject is not there; it put a superseded banner on the blind framework brief; and it
> closed.
>
> **WHAT IT DID NOT DO.** It rendered no pack, withheld nothing, booted no session, derived
> nothing about the analysis, compared nothing and placed nothing. It authored no framework text
> and opened none of the three sealed placement-sample files. It edited nothing under
> `ratification_surfaces/` and did not open `ARCHITECTURE.md`. It created, flipped or discarded no
> open-items row, allocated no finding number, and wrote no decisions-register entry.
>
> **★ THE DISPATCH'S HEADLINE PREDICTION HELD, AND IT IS REPORTED AS A PREDICTION THAT HELD.**
> Assumption A2 predicted that removing the authored entries would turn
> `gen_derivation_boot_pack.py --check` green and leave the guard set at three known failing
> checks. It did. **Nothing was authored to force it**, no verdict was written, and the criterion
> machinery was not touched.
>
> **★ ONE MEASURED DIFFERENCE FROM THE DISPATCH'S DECLARED START STATE, AND IT IS NOT A DEPARTURE.**
> The declared start state named four failing checks plus `gen_evidence_pin_membership.py --check`
> STALE. The pre-edit run measured **five** failing checks — the four named **and** the membership
> check, which the dispatch itself declares as caused by its own untracked ruling records (§2 of
> the declared start state). The two statements are the same state described two ways; §3.1 records
> the measurement rather than the reading of it.

---

## 1. The commits

Every value below was read at a git object by explicit hash. The tip at the start was read as a
file at `.git/refs/heads/master`.

| | commit | subject |
|---|---|---|
| start tip | `bf3249e73d9eb91d0f2513bc2c16aa626b53e464` | (the previous batch's close) |
| Task 0 | `9c39e101e85accaf436506ab44557b128a696f54` | `record: the framework phase is authored informed — the 2026-08-28 rulings, the informed brief and the phase constraints-and-stop-rules home landed` |
| Task 1 | `821c2a44551664dcefba132ad709500c1a366686` | `the framework subject is retired from the boot-pack generator — the ruling cancels its pack, and the fourth failing check goes green` |
| Task 2 | `722c7327a9472436cdc43a9ffc0dd4eb1533823a` | `the blind framework brief is marked superseded by the informed brief, and is kept` |
| Task 3 — the close | *§9 — written in the further commit, this file being inside the commit it would name* | |
| the end state | *§9* | |

Each of the first three was pushed and `origin/master` was re-read at
`.git/refs/remotes/origin/master` after each push; each read returned the commit just made.

---

## 2. The reads performed before the first act

`CLAUDE.md`, `STATUS.md` and `DECISIONS.md` in full. `BUILD_AND_TEST.md` **NOT** opened — the
dispatch states the condition is not met and this batch built nothing, tested nothing, and ran no
measurement tool whose command lives there. Rule (a)'s pointer read at
`tools/audit/nongating_apparatus_rows.json` → `★_the_live_gating_answer` → `gating_ids`.

`cowork_handoff.md` at its current entry (the seventy-sixth) and the entry below it (the
seventy-fifth), plus the head of the seventy-fourth. `cowork_audit_protocol.md`'s dispatch-protocol
section **in full**, from its opening heading to the end of the file. The three records this batch
lands, whole: `cowork_rulings_2026_08_28_informed_framework_sitting.md`,
`cowork_rulings_2026_08_28_ledger_precondition_sitting.md`,
`PHASE_CONSTRAINTS_AND_STOP_RULES.md`. The whole of `tools/audit/gen_derivation_boot_pack.py`.

Also read, because a later task needed them: `tools/audit/gen_guard_state.py` (its authored table
and its `main`), `tools/audit/changed_paths.py` (its docstring), `tools/audit/gen_status_batch_bound.py`
(whole), the head of `cowork_blind_session_brief_framework.md`, and
`cowork_informed_session_brief_framework.md` at its section list and §7 — the last because Task 3
orders the plan lines to name that section's points.

**NOT OPENED:** `ARCHITECTURE.md`; any of the three sealed placement-sample files; either pack
directory's contents. The two existing pack directories were proven byte-unchanged **by hash
against their committed blobs**, which reads no content of theirs.

---

## 3. Task 0 — the landing

### 3.1 The start state, measured before the first edit

The full guard set was run in CHECK mode before anything was touched, by
`python tools/audit/gen_guard_state.py --check`, which runs every guard and compares the run
against the committed artifact.

**Measured: 75 run, 70 passing, 5 failing, 4 not run, 16 historical records.** The five failing:

- `tools/audit/gen_filing_convention_application.py --check`
- `tools/audit/decisions/apply_soft_discard.py --check`
- `tools/audit/decisions/apply_residue_discard.py --check`
- `tools/audit/gen_evidence_pin_membership.py --check`
- `tools/audit/gen_derivation_boot_pack.py --check`

The first three and the last are the four the dispatch's premise ledger names. The fifth is the
membership check, which the dispatch's declared start state names separately as STALE and
attributes to its own untracked ruling records. **No sixth verdict appeared, so there was no
further failing verdict to STOP on.** The run's own exit code was non-zero because the committed
`guard_state.json` records a run at a different tree; that is the artifact-drift half of `--check`,
not a guard verdict, and it is resolved by the end-state run at §9.

### 3.2 A1's check, entirely at content-addressed objects

`python tools/audit/changed_paths.py` over the working tree returned **exactly one tracked
modification, `cowork_handoff.md`**, every other record being untracked. **No modification at any
other tracked path**, so A1's STOP was not engaged.

The handoff was staged, and the two blobs compared **blob to blob**:

| | blob |
|---|---|
| at `bf3249e73d` | `c2fed5a37d034e5b014bb4651057c7ae2a6a9bd5` |
| in the index | `4baa6cf6ed4fbe9dc067b01f1c62369db88ac4ec` |

`git diff --numstat` between those two objects: **372 added, 0 deleted.** `git diff --unified=0`
between them carries **exactly one hunk, `@@ -2,0 +3,372 @@`, and no deletion line at all** — so
the change is additions-only and **prepended above the committed content**, inserted after the
file's second line, which is the blank line under its title.

### 3.3 ★ THE ESTABLISHED HANDOFF-ENTRY COUNT — derived here, not taken from the dispatch

The dispatch deliberately asserts no number of new handoff entries and orders the count established
at the object. Counting the entry heading `## COWORK SESSION CLOSE` in each blob:

| | entry headings |
|---|---|
| `c2fed5a37d…` (committed at `bf3249e73d`) | **10** |
| `4baa6cf6ed…` (landed) | **12** |
| added by this landing | **2** |

The same count taken independently from the diff's added lines returns **2**, so the two routes
agree. The two new entries are the **seventy-sixth** (the informed-framework close, the current
entry point) and the **seventy-fifth** (the pack-preparation batch's close), read at the file. The
figures in this table are this batch's own measurement over git objects named by explicit hash;
the producing command is `git cat-file blob <sha>` counting the heading, and `git diff --unified=0`
for the cross-check.

*(The seventy-fifth handoff entry reports "76 entry headings in this handoff". That is not in
conflict: `cowork_handoff_archive.md` holds the entries moved out of this file, so the file itself
carries the ten-then-twelve above while the series ordinal runs to seventy-six.)*

### 3.4 The ordered regeneration, MEASURED before it was accepted

`python tools/audit/gen_evidence_pin_membership.py` was run and the result compared **against the
committed blob before it was staged for commit**:

| | blob |
|---|---|
| at `bf3249e73d` | `44c8bc5ee24bd324f0bbda14e845ce31315fb661` |
| regenerated | `818046b95e63cedf4f1b2bf4b42947aaec48ce09` |

`--numstat`: **3 added, 1 removed.** The whole difference, read at the diff:

- `counts.ruling_records_read` moves by exactly the two records this batch lands;
- the two record file names are added to the read list, in sorted position.

**Nothing else moved.** The movement's cause is the ordered act itself, so it is a derived addition
caused by the act the dispatch orders, not the movement of a value — the distinction the
dispatch-protocol clause on that subject draws.

### 3.5 The landing

The seven ordered paths were staged and **no other**, proven by
`python tools/audit/changed_paths.py --staged`, which returned exactly:

```
A	PHASE_CONSTRAINTS_AND_STOP_RULES.md
A	cc_instruction_framework_arrangement_landing.md
M	cowork_handoff.md
A	cowork_informed_session_brief_framework.md
A	cowork_rulings_2026_08_28_informed_framework_sitting.md
A	cowork_rulings_2026_08_28_ledger_precondition_sitting.md
M	tools/audit/evidence_pin_membership.json
```

Committed as `9c39e101e85accaf436506ab44557b128a696f54` with the dispatch's exact subject, pushed,
and verified at the object: `changed_paths.py --commit 9c39e101e8` returns the same seven records
and no other, and `git log -1 --format=%s` returns the subject verbatim.
`python tools/audit/gen_evidence_pin_membership.py --check` then **PASSES**.

---

## 4. Task 1 — the retirement

### 4.1 What was deleted, and what was not

Before the edit, the string `framework` occurred in `tools/audit/gen_derivation_boot_pack.py` at
**exactly the four places the dispatch names**: the `WITHHELD` table's authored entry, the
candidate-criterion table's authored entry, and the two comment blocks that name only those two
entries (each naming `cc_instruction_framework_pack_preparation.md` as their source).

All four were deleted. **Nothing else was deleted and nothing else was edited.** After the edit the
string occurs only inside the retirement comment of (b).

### 4.2 The retirement comment, and where it was put

One comment, written at the `WITHHELD` table's point of deletion:

```python
    # THE `framework` SUBJECT IS ABSENT DELIBERATELY, not by oversight: its deriving session is
    # not implementation-blind, so no pack is rendered for it and nothing is withheld
    # (`cowork_rulings_2026_08_28_informed_framework_sitting.md`).
```

It names the record and quotes nothing of it (#6, **D-431**).

**The placement is a choice and is declared rather than implied.** The dispatch asks for *one*
short comment at *the point of deletion*, and there are two points of deletion. It was put at the
`WITHHELD` table because that is the table `build()` enumerates — `for subject in sorted(WITHHELD)`
— so a later reader adding or restoring a subject meets it there first. The criterion table carries
no marking, which is the cost of writing one comment rather than two.

### 4.3 (c) The write-mode run, MEASURED before it was accepted

`python tools/audit/gen_derivation_boot_pack.py` ran to completion, exit 0, rendering the two
remaining subjects. The manifest and **all fourteen** pack files were then hashed on disk and
compared one by one against the blobs committed at `9c39e101e8`:

| path | committed blob | on disk after the run |
|---|---|---|
| `tools/audit/derivation_boot_pack.json` | `944ffd748e79abee16092c40438a105cf0d17701` | identical |
| `derivation_boot_pack/harmony-boundary/00_READ_THIS_FIRST.md` | `ae9edbb2cef09eb94f1156713f1dc22e9d71b402` | identical |
| `…/harmony-boundary/01_the_phase_definitions.md` | `518b1e50d60af2b4e2ddcd8978623832eb071899` | identical |
| `…/harmony-boundary/02_the_guiding_principles_and_the_conventions.md` | `5d1fd0365379ba90ae817a5a1c5e9446348f0744` | identical |
| `…/harmony-boundary/03_the_writing_standards.md` | `518048459da6a865285a0f7c66c5d8f8045f0fc2` | identical |
| `…/harmony-boundary/04_the_dispatch_protocol.md` | `48a68197394ead0dbe0266b5f91bf3c885fc93ef` | identical |
| `…/harmony-boundary/05_the_ratified_design_intent.md` | `dbcd948d20fffaec8eb45e84ee7620b33fec5ea8` | identical |
| `…/harmony-boundary/06_the_defect_type_catalog.md` | `1dec7621dc48d89242cacaf79b3048cd965d6a19` | identical |
| `…/scoring-model/00_READ_THIS_FIRST.md` | `5068c69314655a6b258196e7b30886c8350a083c` | identical |
| `…/scoring-model/01_the_phase_definitions.md` | `518b1e50d60af2b4e2ddcd8978623832eb071899` | identical |
| `…/scoring-model/02_the_guiding_principles_and_the_conventions.md` | `cf718c5678b07e89924b2e39d53982074069fa9c` | identical |
| `…/scoring-model/03_the_writing_standards.md` | `518048459da6a865285a0f7c66c5d8f8045f0fc2` | identical |
| `…/scoring-model/04_the_dispatch_protocol.md` | `48a68197394ead0dbe0266b5f91bf3c885fc93ef` | identical |
| `…/scoring-model/05_the_ratified_design_intent.md` | `60563ab26e5c5c8827e32645b12eceaeb355933b` | identical |
| `…/scoring-model/06_the_defect_type_catalog.md` | `1dec7621dc48d89242cacaf79b3048cd965d6a19` | identical |

**Fifteen of fifteen byte-identical. Not one byte moved.**

**No `framework/` directory came into existence at any point.** The pack root was enumerated with
the file tool and holds exactly the two directories above and the fourteen files listed. The
working-tree enumeration after the run showed **one** tracked modification, the generator itself.

### 4.4 (d) The check

```
python tools/audit/gen_derivation_boot_pack.py --check
the derivation boot pack re-derives
exit:0
```

**The fourth failing check is GREEN.** No verdict was authored, the subject was not re-added, and
the criterion machinery was not touched.

### 4.5 (e) The guard set, and the generator's diff

The full guard set was re-run in CHECK mode over the whole population:
**75 run, 72 passing, 3 failing, 4 not run, 16 historical records** — the three failing being
`gen_filing_convention_application.py --check`, `decisions/apply_soft_discard.py --check` and
`decisions/apply_residue_discard.py --check`, each for its own recorded cause. **A2 holds
exactly.** The working tree after the guard run still carried **one** tracked modification, the
generator — so **A4 holds: no other derived artifact moved.**

The generator's own diff, blob to blob:

| | blob |
|---|---|
| at `9c39e101e8` | `06131cbfc58b51b7adecd1514ecc34dd0643b37f` |
| committed at Task 1 | `d318927e2a13a79a2aa31fd9d97ac0831f5ee639` |

`--numstat`: **3 added, 52 removed**, in **two hunks** — one at the `WITHHELD` table, one at the
`CRITERION` table. The three added lines are the retirement comment. **The criterion machinery, the
leak check and its tests, `withhold_passage()`, the omission marker, every STOP and both other
subjects' authored entries are untouched**, which the diff shows directly: no hunk reaches any of
them.

Committed as `821c2a44551664dcefba132ad709500c1a366686` — `changed_paths.py --commit` returns
**one** record, the generator — pushed, and `origin/master` re-read at that commit.

---

## 5. Task 2 — the superseded banner

A banner was inserted at the head of `cowork_blind_session_brief_framework.md`, immediately below
its title and above its existing status block, so that **no existing line was touched**. It names
`cowork_informed_session_brief_framework.md` as the superseding brief and
`cowork_rulings_2026_08_28_informed_framework_sitting.md` as the ruling; it states that the file is
**KEPT and not deleted (#12)** as the record of what was designed under the previous arrangement and
as the starting point for any later blind run over this subject; and it states that nothing else in
the file is edited.

| | blob |
|---|---|
| at `821c2a4455` | `5b8442154b4109d428389757f300e8935286d297` |
| committed at Task 2 | `73fd0c8a21192568dcf212f5bbf6fd2d94e7141c` |

`--numstat`: **9 added, 0 removed**, in **one hunk, `@@ -2,0 +3,9 @@`**. The staged set was that
one file and no other.

**The two `ratification_surfaces/` files were proven byte-unchanged in the same act**, by hashing
each on disk and comparing against the blob committed at `821c2a4455`:

| path | blob at `821c2a4455` | on disk |
|---|---|---|
| `ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md` | `8de58f0ed968b345dc6806dcbfa7980deddd04f2` | identical |
| `ratification_surfaces/cowork_withheld_family_framework_reading.md` | `5a85169b396c187218077f1cba4af9a39f466f66` | identical |

Committed as `722c7327a9472436cdc43a9ffc0dd4eb1533823a`, verified at the object as one record,
pushed.

---

## 6. The assumptions, graded

| | verdict | how it was established |
|---|---|---|
| **A1** — one tracked modification, `cowork_handoff.md`, additions-only and prepended; a modification at any other tracked path is a STOP | **HOLDS** | §3.2 — the enumeration returned exactly one tracked modification; the blob-to-blob diff carries one hunk, 372 additions, zero deletions, inserted after line 2. The new-entry count is established at §3.3 and is **two**. |
| **A2** — after Task 1 the guard set reads 75 run, 72 passing, 3 failing, the fourth check PASSING | **HOLDS** | §4.5 — measured by a full CHECK-mode run. The membership check is green from Task 0's own regeneration, and the boot-pack check from Task 1's deletion. **This was registered as a prediction and it is reported as one that held.** |
| **A3** — the manifest and all fourteen pack files byte-identical, no `framework/` directory | **HOLDS** | §4.3 — fifteen of fifteen hashes identical to their committed blobs, compared one at a time; the pack root enumerated and holding two directories. |
| **A4** — no other derived artifact moves | **HOLDS** | §4.3 and §4.5 — the working-tree enumeration after the write-mode run and again after the full guard run showed the generator alone. The keyword inlining the previous batch performed for exactly this reason is unaffected by the deletion. |

---

## 7. The evidence gates, graded

| | verdict |
|---|---|
| **E0** — the committed paths; the established new-entry count; the check passing; `origin/master` at the commit | **MET.** §3.5 — the seven paths and no others at the object; two new entries established at §3.3; `gen_evidence_pin_membership.py --check` passes; `origin/master` read at `9c39e101e8`. |
| **E1** — the boot-pack check exits 0; the guard set reads 75/72/3 with the three known; manifest and fourteen pack files byte-identical by hash; no `framework/` directory; the generator's diff carrying only (a)'s deletions and (b)'s comment | **MET in every limb.** §4.3, §4.4, §4.5. |
| **E2** — the file's diff carries the banner and nothing else; the two `ratification_surfaces/` files byte-unchanged | **MET.** §5 — one hunk, nine additions, zero deletions; both surfaces hash-identical. |
| **E3** — at the tree carrying the close, a fresh full guard run: the three known failing checks and no others, zero STOPs, committed only after the run that produced it | **§9** — the close does not assert the end state; the further commit carries it. |

---

## 8. The self-check over this batch's own diff

Performed on the diff actually on disk, read back at the git objects, not on the memory of writing
it.

1. **Principles.** **#12** — the blind brief and the withheld-family reading file are KEPT and
   marked or left rather than deleted; the retirement comment says why the subject is absent
   instead of leaving a silent hole; the forward-bound move is byte-faithful and its
   reconciliation re-derives. **#13** — nothing was authored to make a check pass; the one
   measured difference from the declared start state is reported at §3.1 rather than absorbed.
   **#6** — the ruling has one home, the record, and every file this batch wrote points at it
   rather than restating it. **#15** — every acceptance is at an object: hashes, blob-to-blob
   diffs and the changed-path enumeration, never an assertion. **#17f / D-431** — the STATUS.md
   entries restate no count, no identity and no rendered value; this report's values are ordered
   by the dispatch and each names the object or the command that produced it. **#19** — nothing
   here claims the informed arrangement is established, and the **#18** exposure the ruling
   carries is named at §10 rather than quietly dropped. **Conforms.**
2. **Conventions.** American English. No self-invented label, abbreviation or numbering scheme —
   every name used is the record's own. Music-theory words: none arises in this batch's subject
   matter; every non-musical use in what this batch wrote is qualified (*the open-items register*
   and *the decisions register* in full; *measurement* for the gauging sense; *value* rather than
   the bare collided word; *repository root*).
3. **Figures and premises.** Every commit and blob value in this report was resolved at a git
   object by explicit hash and none was carried from the dispatch, which states none. The two
   guard states name the command that produced them; the end-state summary is additionally at
   `tools/audit/guard_state.json` → `summary` from §9's run. The dispatch's own premises about the
   generator — the four `framework` occurrences and the subject loop — were re-read at the tool
   before the edit and both were correct.
4. **The file-tools rule.** Every working-tree read went through Read / Grep / Glob. Shell use was
   confined to read-only git object queries by explicit hash, `tools/audit/changed_paths.py`, the
   ordered generators and guards, `git add`, `git commit`, `git push` and `git log -1`. `git status`
   and a working-tree `git diff` were never run; the armed guard denied **three** commands during
   this batch — a `python -c` carrying a literal repository path, a `grep` aimed at a tool source,
   and a compound command whose `awk` the guard could not place — and each was re-done through the
   file tools or through an explicit-hash object query. **The guard firing is reported rather than
   passed over**, and in all three cases the guard was right about what the command would have
   read.
5. **Uncertainty.** No comparison between two measured quantities is asserted in this report, so
   #24 raises nothing. The one directional statement — that the guard set improved — is stated as
   the movement of named verdicts, not as a difference between two numbers.

---

## 9. The end state — written in the further commit the dispatch's Task 3 item 3 requires

**This section is written in a SECOND commit, after the close.** The close cannot assert the state
it produces: the guard run that grades E3 must be made at the tree the close leaves, and its
artifact must be committed only after that run. The dispatch orders exactly this shape.

*(Filled in by the further commit.)*

---

## 10. Declared departures, and what is deliberately NOT done

**No departure from the dispatch's letter was taken.** Three things are declared because a reader
would otherwise have to infer them.

1. **The retirement comment sits at one of the two deletion points, not both** — §4.2. The
   dispatch says *one short comment*; the choice of which point is the executing side's and is
   recorded rather than implied.
2. **Nothing under `ratification_surfaces/` was edited, and the two owed banners are NOT taken.**
   The frozen phase-definition surface still carries, on its face, the first NOT ALLOWED limb the
   ruling sets aside, with no pointer to `PHASE_CONSTRAINTS_AND_STOP_RULES.md`; and
   `ratification_surfaces/cowork_withheld_family_framework_reading.md` still asks for verdicts the
   ruling means will never be taken, with nothing on its face saying so. **Editing a ratified
   surface is not a batch's call.** Both are questions for the user, and until they are settled
   `PHASE_CONSTRAINTS_AND_STOP_RULES.md` governs and the surface is stale wherever the two differ.
3. **`tools/audit/gen_status_batch_bound.py` was re-aimed**, which is an edit to a tool source. It
   is the ordered act: Task 3 item 1 orders the previous batch's entries moved through that tool's
   `--apply`, and the tool's own record names its per-batch re-aiming as the way that is done —
   three authored inputs moved (the base commit, the then-previous batch, the executing act) and
   the previous aiming appended rather than overwritten (#12). Nothing else in that tool changed.

**Four things this batch neither did nor decided, restated so a successor does not read them as
settled:** the **#18** exposure the informed arrangement carries is **not discharged**; the
**independent challenge run is not commissioned**; the **three sealed placement samples are not
disposed of**; and the **decisions-register entries owed for the two 2026-08-28 rulings are not
written** — the blocker stands and the route is **D-652**, which the dispatch states is not this
batch's business. **This is at least the sixth consecutive act shaped around a register that
cannot accept an entry**, recorded rather than hidden.

**One further note, offered and not acted on.** `tools/audit/gen_guard_classification.py` reads the
artifact `gen_guard_state.py` writes and is not part of the guard run. No tool was added to or
removed from `tools/audit/` by this batch, so the population it classifies is unmoved; it was not
run, because the dispatch does not order it and running it would write a derived artifact this
batch was not sent to move.

---

## 11. The plan lines, as the dispatch states them

1. **The user rules the informed brief's §7 points.** Read at
   `cowork_informed_session_brief_framework.md` §7, which states in its own heading that **none is
   ruled**: **(P1)** what the informed session reads — unbounded, or an enumerated list, which that
   brief names as the largest of the remaining points; **(P4)** the output file's name; **(P5)**
   whether the session keeps a sizing record, which must be settled before the session runs because
   a cost measurement cannot be reconstructed afterwards; **(P6)** whether annotated scores are
   staged and which, also to be settled before the session runs; and **(P7)** whether this session
   performs the code-site fill-in itself, the ground for routing it elsewhere having been removed by
   the ruling. *(P2 and P3 of the superseded brief are recorded there as DISSOLVED rather than
   dropped, both having existed only because a pack was to be rendered with a withheld family.)*
2. **Then a session that has read neither the ruling record nor the current handoff entry authors
   the framework document.** The bar is that the authoring side is not the side that argued the
   case; the ruling record and the seventy-sixth handoff entry each declare the contamination on
   their own face.
3. **The independent challenge run and the sealed samples' disposition remain unruled.**

---

*Claude Code, 2026-08-28. Three task commits and one close, each verified at the object; nothing
built, nothing tested, no measurement of the analysis run, no golden touched, nothing under
`tools/corpus/` or `tools/robust_stop/`, and no session booted.*
