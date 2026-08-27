# CC report — the `framework` subject authored, its withheld candidates ENUMERATED, NO PACK RENDERED

> **Dispatch:** `cc_instruction_framework_pack_preparation.md` (Cowork, 2026-08-27, the fifty-fourth
> session). **Executed by Claude Code, 2026-08-28.**
>
> **★ READ §7 FIRST IF YOU READ ONLY ONE SECTION. THE BATCH RETURNS A DECLARED STOP.** The
> generator has no state for *enumerate the candidates and withhold nothing*, so **assumption A3
> FAILS**: the manifest gains no block for this subject and none was forced into it by authoring the
> grades the dispatch reserves to the user. **The enumeration itself ran in full and is delivered.**
>
> **What this batch did NOT do, stated at the top so it is not looked for below:** nothing is
> withheld — no identity, no document, no passage; **no pack directory exists for this subject**; no
> session is booted; nothing is derived, compared or placed; neither existing subject's manifest
> block, pack directory, family or reading file is touched; `ARCHITECTURE.md` was not opened beyond
> what the tool's own mechanics touch; **none of the three sealed placement-sample files was opened,
> not in any portion**; no `src/` change, no golden, no test changed, moved or run, nothing under
> `tools/corpus/` or `tools/robust_stop/`, no measurement of the analysis, no edit to any governing
> document, register entry or register source, **no open-items row created, flipped or discarded**,
> and **no finding number allocated**.

---

## 1. The commits

| Act | Commit |
|---|---|
| Task 0 — the landing | `2fc65d3045dac92be8934b4ad1ff1911385b83b5` |
| Task 1 — the subject authored and enumerated | `85e0b8da162a5b937f4a4be0f033f5c7d281eddf` |
| Task 2 — the close | *recorded in §12, in the further commit the dispatch's item 3 requires* |
| Task 2 — the end state | *recorded in §12* |

**The tip the batch met** was `acedffc66d8c40f17d5fe6dbb73ca1ac90129997`, read at
`.git/refs/heads/master` and confirmed at the object. It matches the tip the dispatch's premise
ledger states.

**★ AN OBSERVATION ABOUT THE REMOTE, MADE AT THE FIRST PUSH AND REPORTED BECAUSE IT WAS NOT
EXPECTED.** `origin/master` stood at `f225b61343ff3de022d32d6b7514d835b87093cf`, a commit of
2026-08-25, so **thirty-one commits were unpushed** when this batch began — every commit of the
placement-sample batch, the redraw batch and the unit-correction batch among them. The first push of
this batch was a fast-forward carrying all of them, and `origin/master` is now the current tip.
Nothing was forced and nothing was rewritten. **This is stated as a fact about the record's state,
not as a diagnosis of how it arose**, which this session cannot establish.

## 2. Task 0 — the landing

### 2.1 The start state, measured before the first edit

**The full guard set, CHECK mode** (`python tools/audit/gen_guard_state.py --check`): **75 guards
run, 4 failing, 4 not run, 16 historical**. The four failing:

- `tools/audit/gen_filing_convention_application.py --check`
- `tools/audit/decisions/apply_soft_discard.py --check`
- `tools/audit/decisions/apply_residue_discard.py --check`
- `tools/audit/gen_evidence_pin_membership.py --check` — STALE

**That is the dispatch's declared start state exactly**: the three named in its premise ledger, plus
the membership check made stale by this dispatch's own untracked ruling record, which its declared
start state names as item 2. **No further failing verdict, so its STOP did not fire.**

**The tree, measured by `tools/audit/changed_paths.py` and NOT by `git status` (D-253):** **836
changed path records — 835 untracked and exactly ONE tracked modification, `cowork_handoff.md`.**
A1's STOP for a modification at any other tracked path did not fire.

### 2.2 ★ A1's handoff establishment — the new-entry count DERIVED HERE, not taken from the dispatch

**The dispatch asserts no count and none was taken from it.** What follows was established at
content-addressed objects.

**The tip side.** `cowork_handoff.md` at `acedffc66d8c40f17d5fe6dbb73ca1ac90129997` resolves to blob
`38359f2b3b48162d6ff2a862da010a32d1d9bbbd`: **10,379 lines**, **74** entry headings matching
`^## .*COWORK SESSION CLOSE`, topmost the **SEVENTY-SECOND** at line 4.

**The staged side**, by content-addressed read of the blob `git add` produced:
`c2fed5a37d034e5b014bb4651057c7ae2a6a9bd5`: **10,714 lines**, **76** entry headings, topmost the
**SEVENTY-FOURTH** at line 4.

**(i) HOW MANY ENTRIES ARE NEW: TWO** — the seventy-third and the seventy-fourth. **The dispatch's
one timing constraint is therefore met and then some**: it allowed that the writing side's own entry
might not be in the file; both it *and* the entry below it were, and both land here.

**(ii) ADDITIONS-ONLY AND PREPENDED, proven at the objects rather than inferred from the prose.**
The blob-to-blob diff carries **exactly one hunk**:

```
@@ -2,0 +3,335 @@
```

**+335 insertions, 0 deletions**, inserted after old line 2. Every line from old line 3 onward is
unchanged and shifted by exactly +335, so nothing was removed and nothing reworded. The STOP for a
change of any other shape did not fire.

**(iii) THE ARITHMETIC THAT CLOSES THE TWO SIDES.** 10,379 + 335 = **10,714** lines. 74 + 2 = **76**
entry headings, and both new headings lie inside the inserted block. The tip's own entries are each
re-found at a uniform **+335**: 72nd 4 → 339, 71st 177 → 512, 70th 332 → 667.

**`cowork_handoff.md` was not edited by this session at any point**, so what was verified is what was
committed.

### 2.3 The ordered regeneration, MEASURED before it was accepted

`python tools/audit/gen_evidence_pin_membership.py` rewrote
`tools/audit/evidence_pin_membership.json`. **The whole difference against the committed blob
`e060965f9fc3319f4ba06fbc3a4f30e56f6e14fd` is +2 −1 across two hunks, and both are the landed ruling
record's own addition**: `ruling_records_read` moves by one, and
`cowork_rulings_2026_08_27_framework_authoring_sitting.md` joins the sorted list of records read.
**No member, no pin, no route, no verdict and no other count moved.** Accepted on that measurement.

### 2.4 The landing

**One commit, `2fc65d3045dac92be8934b4ad1ff1911385b83b5`**, carrying exactly the five paths the
dispatch names and nothing of the standing untracked population — verified at the object with
`git show --name-status`:

- `cowork_handoff.md` (M)
- `tools/audit/evidence_pin_membership.json` (M)
- `cowork_rulings_2026_08_27_framework_authoring_sitting.md` (A)
- `cowork_blind_session_brief_framework.md` (A)
- `cc_instruction_framework_pack_preparation.md` (A)

*5 files changed, 1,135 insertions(+), 1 deletion(-).* Subject exactly as the dispatch fixes it.

**Pushed**; `origin/master` verified at the object as `2fc65d3045…`.
**`gen_evidence_pin_membership.py --check` PASSES** (exit 0).

**E0 — MET in full.**

## 3. Task 1 — what was authored

**(a) The `framework` entry in the generator's AUTHORED `WITHHELD` table**, in the shape the two
existing subjects use:

- **subject name** `framework`;
- **the subject in plain words**, verbatim as the dispatch fixes it;
- **the oracle field — and the dispatch's conditional STOP did NOT fire.** The field is free text in
  the authored table and in the rendered record alike; **the tool's shape does not require an oracle
  span**, and the second subject already stands with `"NONE. This unit is not held out and has no
  oracle…"` in it. So the field states, as ordered, that this subject is not held out, that there is
  no answer to protect, and that what the family exists to keep out is the ruled NOT-ALLOWED clause
  of the phase-definition surface — quoted verbatim rather than paraphrased.
- **the withheld family: EMPTY.** `withheld_documents` `{}`, `withheld_passages` `[]`, and **no**
  `the_identity_the_ruling_names` key, because nothing is withheld by the act that authors it. The
  comment beside it distinguishes this emptiness from the second subject's, which is empty *by
  ruling and permanently*; here it is empty *because nothing has been ruled yet*, which is why a
  criterion is authored at all.

**(b) The candidate criterion**, imported verbatim from the dispatch: the eight groups, no home
document, no oracle span, the thirty-three keywords, no named identity.

**One choice inside (b), declared because it was measured rather than assumed.** The keywords are
written **in place** inside the criterion entry rather than as a module-level constant beside the
first subject's `KEYWORDS`. With a named constant, `tools/audit/recognizer_establishment_sort.json`
— a *derived* artifact that records each tool's module-level collections — moved, its whole
difference being **one added line**. That would have widened this task's fence to a fourth path for
a naming choice. **Inlining returns that artifact byte-identical to its committed blob
`98566d53b2a2e76479c336a492be9f226143dff4`, verified by hash**, and the enumeration is unaffected:
the two runs' outputs are byte-identical to each other, checked with `diff`.

## 4. Task 1(c) — the enumeration RAN; the render did NOT

**The run:** `python tools/audit/gen_derivation_boot_pack.py --check` — a mode that **writes
nothing**, which is how the enumeration was obtained without any risk of a render.

**It STOPS.** §7 states the shape. **The STOP's own message is the enumeration**: it lists every
candidate carrying no authored verdict, each with its identifier, its title, its verbatim, its plain
restatement, and its full matching record including the in-context excerpt for every keyword hit. So
the derivation ran to completion; what does not exist is a durable artifact for it.

**No directory was written under `tools/audit/derivation_boot_pack/`**, and this was verified rather
than assumed:

- the pack root holds **`harmony-boundary/` and `scoring-model/` and no third directory**, enumerated
  with the file tools;
- the manifest `tools/audit/derivation_boot_pack.json` is **byte-identical** to its committed blob
  `944ffd748e79abee16092c40438a105cf0d17701`;
- **all fourteen pack files — seven per existing subject — are byte-identical** to their committed
  blobs, compared one by one by hash.

**The leak list for this subject was NOT measured, and no value is asserted for it.** The tool STOPs
before the leak check. What the record does hold is the second subject's leak entries, published
whole at `tools/audit/derivation_boot_pack.json` → `subjects.scoring-model.LEAKS.entries`; the
reading file says in terms that the identity of the two is an argument from the code's shape and
**not a measurement of this subject**, and that the measurement is owed at the render.

**The standing exclusion was applied AFTER the criterion and OUTSIDE the tool, as ordered.** The
criterion machinery carries no exclusion term and adding one is barred. **Exactly ONE entry was
removed**, and it is named on the reading file rather than silently absent: the design-intent class
carries exactly one entry homed in `cowork_joint_estimator_factorization.md`, established by a
search over the register's own data at the git object, and that entry did reach the candidate list.

## 5. Task 1(d) — the member-(2) passage enumeration, and a premise corrected at the object

**Nothing was cut.** The enumeration is delivered on the reading file with each passage's anchor
text — never a line number — the limb of the dispatch's signature it matches, and what a deriving
session would learn from it. **The two passages already withheld for the `harmony-boundary` subject
were re-tested and are reported with the rest; their existing withholding is neither carried across
to this subject nor removed from that one.** Both re-tested as matching: one against four of the
five limbs, the other against two.

**★ A PREMISE OF THE DISPATCH AND OF THE CURRENT HANDOVER BLOCK IS FALSE, AND IT MATTERS HERE.** Both
say member (2) is *`CLAUDE.md` rendered whole*. **The generator takes TWO SPANS ONLY** — from the
`## Guiding principles` heading to the end of the paragraph opening `**Delegation pointer`, and from
the `## Conventions` heading to the end of the file — and its own docstring says so in terms.
Everything between those two spans is **not in the pack at all**, and that is where `CLAUDE.md` names
the numbered layers, the two arms of the record, and the segmentation layer, repeatedly and by name.
**The leak surface is therefore far narrower than the premise implies**, and the correction is
reported so that a reader does not take the enumeration's shortness for thoroughness — and so that a
later proposal to widen member (2) meets the cost first. The reading file states it on its own face
and also lists, at section granularity and declared as such, what the excluded part of `CLAUDE.md`
carries.

**Both enumerations carry their declared bound in the same words**, per the dispatch: the criterion
is a pattern match whose reach is **UNMEASURED**, the passage signature is **AUTHORED** and its reach
likewise unmeasured, the bound is stated under **D-673** rather than a detection measurement being
owed, and that clause's test is met — **no analysis decision consumes either enumeration; the user
rules them.**

## 6. Task 1(e)–(f) — the reading file and the commit

`ratification_surfaces/cowork_withheld_family_framework_reading.md` is written in the shape
`cowork_withheld_family_harmony_boundary_reading.md` takes: the words used, the subject from
scratch, what the family protects and that there is **no oracle**, how the list was derived with its
bound, the verdict vocabulary, the two candidate lists, the leak section, what the batch did and did
not do, the STOP, and what the file does not do. **It asks for one verdict per candidate and
recommends none, for any candidate, in either list (D-658).** A short *considered and not listed*
section records what was tested against the passage signature and did not match, with the reason, so
that the list's shortness is a result rather than an omission (#12).

**Committed as `85e0b8da162a5b937f4a4be0f033f5c7d281eddf`**, exactly two paths — the generator (M)
and the reading file (A) — verified at the object. Pushed; `origin/master` verified at that commit.

## 7. ★ THE STOP — the tool shape, reported and not worked around

**The dispatch's Task 1 cannot be completed as written, and the reason is structural rather than
incidental.**

1. **The generator has no ENUMERATE-ONLY state.** Its fourth STOP fires when a derived candidate
   carries no authored verdict — *"a candidate cannot be graded by silence"* — so a non-empty
   criterion obliges an authored verdict for **every** candidate it returns. **The only verdict that
   withholds is `IN`.** So *enumerate the candidates, withhold nothing, and let the user grade them*
   is a state the tool cannot represent. It can withhold what a session has already graded (the
   first subject), or it can search for nothing at all (the second subject, whose criterion is empty
   by ruling). There is no third thing.
2. **A3 FAILS.** The run STOPs inside `build()`, before `write_all()`, so the manifest is not written
   and gains **no `framework` block**. Its `candidates` and `leaks` fields, which A3 requires to be
   MEASURED, do not exist.
3. **Nothing was authored to make the tool complete.** Grading every candidate `UNPLACED` would have
   produced a manifest block and an empty family — and it would have been a fabricated judgment
   about entries this batch was ordered not to judge, written in order to clear a check. That is
   precisely what **D-655** exists against, and it is what the dispatch forbids in its own words at
   Task 1(e).
4. **The dispatch's own conditional STOPs are answered individually, so it is clear which fired.**
   *"If the generator's shape cannot enumerate without writing its pack directory"* — **did not
   fire**: `--check` writes nothing and the enumeration was obtained from it. *"If the tool's shape
   requires an oracle span"* — **did not fire**: the field is free text. What fired is the general
   clause: **a tool shape this dispatch's instruction cannot reach without a wider change.**
5. **A SECOND SHAPE, which would have written a FALSE STATEMENT into a generated artifact had the run
   completed.** Two places hardcode the first subject's criterion while claiming to describe the
   running one: a `group` match is recorded with the fixed gloss **"Layer 2 — the slicer"**, which is
   false of a group-A, C, D, F, G, H or I match; and the manifest's candidate-criterion block renders
   five fixed bullets describing the harmony-boundary criterion — *"its `group` is E — Layer 2, the
   slicer"*, *"its `home` is `ARCHITECTURE.md` at a line inside one of the oracle spans below"*, *"it
   is an identity the ruling names"* — none of which is this subject's criterion. **Correcting either
   is a change to the criterion machinery, which the dispatch bars by name.** Reported so that a
   later render is not taken over it.

**What the batch did instead of forcing it:** ran the enumeration, delivered it whole in the reading
file, named the producing command so it is reproducible, and committed the authored entry so that it
IS reproducible.

**★ THE CONSEQUENCE FOR THE GUARD SET, AND ITS COST, STATED RATHER THAN BURIED.**
`tools/audit/gen_derivation_boot_pack.py --check` **STOPS from Task 1's commit and goes on STOPPING**
until the user rules the two lists and a later batch writes the reviewed verdicts into the authored
table. That is the shape the record already sanctions for an authored establishment: the standing
check fails deliberately across the authoring interval and clears only when the reviewed set is
applied (**D-655**). **The accepted cost, which is not a discharged one: while it STOPS, that check
cannot report drift in the two EXISTING packs either.** Both were proven byte-identical to their
committed blobs, file by file, at Task 1's own tree; that proof is a snapshot and not a standing
guard.

**The alternative was weighed and is recorded, because an excluded alternative is evidence about the
choice.** Not committing the generator entry would have kept the check green — and would have left
the enumeration in this report and nowhere reproducible, since the derivation cannot be re-run
without the authored entry. A figure whose producer cannot be re-run is the thing **D-431** and the
character-figure clause exist against, so the green check was the more expensive of the two.

## 8. The assumptions, graded

| | Verdict |
|---|---|
| **A1** — one tracked modification, `cowork_handoff.md`, additions-only and prepended; the count established at the object | **HOLDS.** Measured by `changed_paths.py`: exactly one tracked modification. Additions-only proven at a one-hunk, zero-deletion blob-to-blob diff. **Two** new entries, derived here; the dispatch asserts none and none was taken from it. |
| **A2** — the three known checks still fail; the boot-pack check red inside Task 1; the membership check red until Task 0's own regeneration | **HOLDS IN PART, and the part that does not is declared.** The three known checks fail for their own causes throughout. The membership check cleared at Task 0 exactly as predicted. **The boot-pack check is red at Task 1's commit and STAYS red** — not only "between the table edit and the enumeration" — which is the STOP of §7 and not a second failure. **One further red appeared and was cured within the task**: `gen_recognizer_establishment_sort.py --check`, caused by this batch's own act (a new module-level constant in the generator), measured at one added line and removed by inlining; the artifact re-derives byte-identical and the check is green. **No red outside this batch's own acts' subjects**, so A2's STOP did not fire. |
| **A3** — the manifest gains one `framework` block with `candidates` and `leaks` MEASURED | **FAILS.** No block exists; the tool STOPs before writing the manifest. **The two existing subject blocks are byte-unchanged** — the whole manifest is byte-identical to its committed blob — which is A3's other half and holds. |
| **A4** — no tool added; the guard registry does not move | **HOLDS.** The generator's registered invocation is `--check` and is **not** per-subject; the guard set still runs 75 guards. Nothing in the registry moved and no STOP was engaged. |

## 9. The evidence gates, graded

**E0 — MET.** The five committed paths verified at the object; the established new-entry count is
**two**, derived at the objects; `gen_evidence_pin_membership.py --check` passes; `origin/master` at
the commit.

**E1 — MET IN PART, and the part that fails is A3.**

- the manifest's new subject block at A3 — **NOT MET**: no block, §7;
- **the two existing subject blocks byte-unchanged** — **MET**, the whole manifest byte-identical;
- **both pack directories byte-unchanged** — **MET**, all fourteen files by hash;
- **no `framework/` directory in existence** — **MET**;
- the reading file whole in the ruled shape — **MET**;
- **both declared bounds on its face** — **MET**.

**E2 —** recorded in §12, in the further commit. **It cannot be met as written**, for the reason §7
gives: it asks for *the three known failing checks and no others*, and the boot-pack check is a
fourth, deliberately.

## 10. Declared departures

1. **A3 is not met and no attempt was made to meet it.** §7. The alternative — authoring a verdict
   for every candidate — is the grading the dispatch reserves to the user, and **D-655** forbids
   verdicts written in order to clear a check.
2. **Task 1(f)'s "A2, A3, A4 must hold" is not satisfied**, A3 having failed. The task's work was
   nonetheless completed and committed, because the dispatch's own words make the enumeration the
   deliverable and because a STOP enforced past its stated purpose is the failure the record names at
   the narrowed-bar clause. **This is a declared departure and it is the user's to overrule.**
3. **E2 cannot be met as written** — a fourth check fails, deliberately and by this batch's own act.
4. **The member-(2) enumeration was performed over `CLAUDE.md` whole, as the dispatch's letter
   directs, and each row is additionally marked as inside or outside member (2)'s two rendered
   spans.** That is more than the dispatch asks and is declared rather than passed over: the
   dispatch's own premise about member (2) is false, and an enumeration that did not say so would
   mislead.
5. **The framework keywords are written in place rather than as a module-level constant.** A
   stylistic choice, taken to avoid widening the task's fence to a fourth path, measured both ways
   and recorded in §3.

## 11. The self-check over this batch's own diff

Performed by re-reading the diff of every touched path, not the memory of writing it.

1. **Principles.** **#19** — nothing is withheld without a ruled reason, so nothing is withheld and
   only the candidates are enumerated; both enumerations declare their unmeasured reach. **#13** —
   the tool shape the instruction could not reach was surfaced as a STOP rather than rewritten, and
   so was the second, latent shape. **#6** — one generator, one authored home, and the fence held at
   the paths the dispatch names. **#12** — the two existing subjects byte-unchanged, the
   harmony-boundary passages neither carried across nor removed, the standing exclusion's one removal
   named rather than dropped, the *considered and not listed* section kept. **#17f / D-431** — the
   candidate and leak counts are not restated in the reading file or in `STATUS.md`; where a figure
   appears in **this report** it is one this session measured, with the producing command named.
   **D-658** — the reading file recommends nothing. **Conforms.**
2. **Conventions.** American English. No self-invented labels: *layer*, *slice*, *slicer* and
   *decode* appear only as quotations of the criterion's own vocabulary, which is the register's.
   Music-theory words in their musical sense; every non-musical use qualified — *content score* and
   *candidate score* do not arise here, and *the open-items register* is written in full.
3. **Figures and premises.** Every git-object value in this report was resolved by explicit hash in
   this session. **No figure was taken from the dispatch**, which asserts none, and none from the
   handoff. The dispatch's premises about the manifest, the pack directory listing and the guard
   summary were **re-read at the objects** and all held; its premise about member (2) was checked at
   the tool and **did not hold**, and the correction is reported.
4. **The file-tools rule.** Every working-tree read went through Read / Grep / Glob. The armed guard
   denied three shell attempts during this batch — an `ls` of a repository directory, an `awk` over a
   scratchpad file the guard could not resolve, and a `python -c` naming a repository path — and each
   was re-done through the file tools rather than worked around. **Shell use was confined to
   read-only git object queries by explicit hash, to the sanctioned tool invocations, and to
   scratchpad files outside the repository.** `git status` and `git diff` over the working tree were
   never run; the tree was enumerated by `tools/audit/changed_paths.py`.
5. **Uncertainty.** The measured-not-predicted items are the handoff's new-entry count, the
   enumeration's population, the standing exclusion's removal, the byte-identity of the manifest and
   the fourteen pack files, and the recognizer artifact's one-line movement and its reversal. **The
   criterion of Task 1(b) and the signature of Task 1(d) are AUTHORED**, their reach unmeasured and
   declared as such on the artifact. **No difference between two measured quantities is asserted
   anywhere in this report**, so #24's demand does not arise.

## 12. The end state — written in the further commit the dispatch's Task 2 item 3 requires

*The close commit did not assert this section; it is added here, in the one further commit, which is
the only act that can carry a run made at the tree the close left. **This section asserts no hash it
could not know:** the closing commit's hash is stated because it exists; the hash of the commit
carrying this section is not, because a commit cannot state its own.*

**The closing commit is `b4fd021fe0c9ff37fd21cc3795212f5b510668e3`**, carrying exactly six paths,
verified at the object: `STATUS.md` (M), `STATUS_ARCHIVE.md` (M),
`cc_report_framework_pack_preparation.md` (A), `tools/audit/gen_status_batch_bound.py` (M),
`tools/audit/session_start_read_size.json` (M), `tools/audit/status_batch_bound.json` (M). *6 files
changed, 417 insertions(+), 27 deletions(-).* Pushed; `origin/master` verified at it.

**What the close did.** Three `STATUS.md` pointer entries — one for each task that did work, the
newest naming the dispatch and the two below it saying *Same dispatch*, per the convention the
forward-bound tool derives membership from. The previous batch's single entry was moved verbatim to
`STATUS_ARCHIVE.md` by `python tools/audit/gen_status_batch_bound.py --apply`, the tool re-aimed
under the carve-out ruled for it by name, with the outgoing aiming **appended** to its record of
aimings rather than overwritten (#12). The move reports itself: **one entry moved, byte-present in
the archive exactly once, absent from the must-read**, and `--check` re-derives it.
`tools/audit/session_start_read_size.json` was regenerated, stale by construction because this batch
writes to a member of that read. **No count, no identity and no rendered value is restated in any
`STATUS.md` entry (D-431).**

**One ordering point, recorded because getting it wrong is a STOP rather than a warning.** The
forward-bound tool strips the `Last updated: ` prefix from the entry it moves, on the ground that the
next batch's own entries take that prefix over. Run **before** this batch's entries were written it
found the entry zero times and STOPPED, correctly. The entries were written first and the prefix
handed over; the move then ran clean. Nothing was retyped and nothing was edited in transit.

### The end-state guard run, made at the tree the close left

`python tools/audit/gen_guard_state.py` (write mode, the artifact of a real run): **75 guards run, 4
failing, 4 not run, 16 historical records.** The four failing:

- `tools/audit/gen_filing_convention_application.py --check`
- `tools/audit/decisions/apply_soft_discard.py --check`
- `tools/audit/decisions/apply_residue_discard.py --check`
- **`tools/audit/gen_derivation_boot_pack.py --check`** — **this batch's own declared STOP, §7.**

**E2 — NOT MET AS WRITTEN, and the failure was declared in advance rather than discovered here.** It
asks for *the three known failing checks and no others, zero STOPs*. There is a fourth, and it is a
STOP rather than a drift report. **It is this batch's own act and nothing else**: the three known
checks fail for their own recorded causes, unchanged; `gen_evidence_pin_membership.py --check`, which
the dispatch's declared start state named as a fifth, passes, cleared at Task 0. **No red outside
this batch's own acts' subjects appeared at any point in the batch.**

### One derived artifact moved with it, measured before it was accepted

`tools/audit/guard_classification.py`'s artifact reads the guard state's own pass/fail column, so a
guard flipping PASS→FAIL moves it. It is regenerated here, and **its whole difference against its
committed blob is three lines**, every one of them the same declared fact: the live-and-failing count
moves by one, `tools/audit/gen_derivation_boot_pack.py` joins the failing list, and that tool's
recorded state moves from `PASS` to `FAIL`. **No verdict, no classification, no member and no other
count moved.** It is a staleness red whose whole cause is the act the dispatch orders, so it is
regenerated rather than left — the standing safety rule being that a staleness red is regenerated and
a decision red never is. The three decision reds were **not** touched.

### The tree at the end

Measured by `tools/audit/changed_paths.py` and not by `git status` (**D-253**), immediately before
the commit carrying this section: **834 changed path records — 832 untracked and exactly TWO tracked
modifications**, `tools/audit/guard_state.json` and `tools/audit/guard_classification.json`, which
are the two paths this commit carries beside the report. **Nothing of the standing untracked
population is committed by any commit of this batch.**

**The batch's arithmetic closes.** It began at 836 records — 835 untracked, one tracked modification
(`cowork_handoff.md`). Task 0 committed three of those untracked files and the one tracked
modification; Task 1 added the reading file untracked and then committed it with the generator; the
close added the report untracked and then committed it with five tracked modifications. **Every path
every commit of this batch carries is inside the dispatch's own fence**, with the two derived
artifacts of this section the only addition — each caused by an act the dispatch orders, each
measured, and each declared here.

## 13. The plan lines, as the dispatch states them

1. **The user rules the two candidate lists** at
   `ratification_surfaces/cowork_withheld_family_framework_reading.md` — one verdict per
   design-intent candidate, and one per member-(2) passage. Nothing is withheld until then.
2. **The render is a later batch**, after that ruling: the reviewed verdicts are written into the
   generator's authored table, the pack directory for this subject is rendered, and the boot-pack
   check goes green in the same act.
3. **The brief is finalised against the rendered pack** —
   `cowork_blind_session_brief_framework.md` stays a DRAFT until then, its §7 (P2) being the point
   this batch feeds and the other five §7 points still unruled.
4. **Then the fresh Cowork session authors the framework document**, blind, with ratification of its
   decomposition HELD until the user's incoming external list has arrived and been dispositioned
   against it.

**Two things this batch surfaces that stand outside those four**, both for the user rather than for a
successor session to act on unprompted: **the second tool shape of §7(5)**, which will write a false
statement into the manifest at the render unless the criterion machinery is corrected first; and
**the member-(2) premise correction of §5**, which decides how much of `CLAUDE.md` the withheld
family has to reach.
