# CC report — `cc_instruction_register_baseline_repair.md`: **NOT RUN. STOPPED AT THE INSTRUCTION ITSELF.**

> **★ THIS IS A STOP REPORT, NOT A BATCH REPORT.** The dispatch was **not executed**. Nothing was
> committed, nothing was pushed, no tool source was edited, no register field was moved, no file was
> deleted. **Two working-tree edits were made under an earlier state of the instruction and have been
> fully reverted; the reversion is proven at the content-addressed object.** The tree is byte-for-byte
> as I found it and `HEAD` has not moved.
>
> **THE TWO REASONS FOR THE STOP, in the order they bind:**
>
> **(1) THE INSTRUCTION FILE CARRIES A `⏸ PARKED` BANNER AND NO DATED DISPATCH NOTE.** The standing
> clause in `cowork_audit_protocol.md` — *"Dispatches are written only when they are next; a parked
> instruction is revalidated first"* (**D-250**) — ends: *"an executing session must not run a parked
> instruction without that note."* There is no note in the file. This alone is dispositive.
>
> **(2) THE INSTRUCTION FILE CHANGED WHILE I WAS EXECUTING IT — at least three distinct states were
> observed in one session, and the differences are material, not cosmetic.** One of them reversed the
> content of an edit I had already made.
>
> **Written 2026-08-28. `HEAD` = `6005daecaf9f1a6692e61521911ef8b99ed73b55`, unmoved;
> `origin/master` the same.**

---

## 0. The instruction I actually executed against, pinned

Because the file was moving, I stopped reading it from the working tree and **pinned it as a
content-addressed object**: `git add` of the path, then the blob id, then every subsequent read of
the instruction taken from `git cat-file blob <hash>` into a scratch file outside the repository.

| Object | Blob | Lines |
|---|---|---|
| `cc_instruction_register_baseline_repair.md` | `abd2601ff7c05e98c69366447437ba9a1c2b23c8` | 518 |
| `cowork_handoff_entry_eighty.md` | `a68a59195f755d974701865e94e42e644b110158` | 223 |
| `cowork_section8_bar_record_2026_08_28.md` | `f82b20efa5cf2701ae622ec6e28689df8f0fad6f` | — |
| `cowork_register_rule_c_suspension_2026_08_28.md` | `7d3268c7a06015f45e677fc266bd67cfdf22369e` | — |

**The index was reset immediately afterwards; nothing remained staged.** Both blob ids were
re-derived a second time, minutes later, and both were unchanged — so the files have **settled** at
the parked state. The instability was real and is now over.

## 1. THE STOP — the parked banner, quoted at the pinned object

Lines 3–22 of blob `abd2601ff7c05e98c69366447437ba9a1c2b23c8`:

> `# ⏸ PARKED`
>
> **Parked 2026-08-28 by the Cowork writing side, under the standing rule that an instruction file
> which exists but is not the active dispatch carries this banner.** It is written and complete; it is
> not the active dispatch and **must be revalidated against the then-current `STATUS.md` and HEAD
> immediately before dispatch, with a dated dispatch note added here.**
>
> **★ WHY IT IS PARKED RATHER THAN SENT.** It was written when the seventy-ninth handoff entry's
> cadence made it next. **The user's standing bar of 2026-08-28 — keep the progress of the plan in
> focus, never act on the latest impulse — changes the order.** Every subject in this dispatch is
> apparatus: under `CLAUDE.md`'s non-gating declaration none of it bears on the analysis, its inputs,
> or a measurement tool something depends on, so it gates nothing. **The framework document is derived
> and declares its own outstanding gap; that gap, not this, is what moves the phase.**
>
> **Nothing here is withdrawn and nothing needs rewriting** — the register blocker is still real, the
> repair is still the user's disposition, and this file is ready the moment it is next.
>
> **★ ONE PREMISE WILL HAVE GONE STALE BY THEN AND IT IS THE ONE THAT STOPS A BATCH: A1.** Every
> further act on this tree changes the untracked population, and A1's own STOP fires on a path it does
> not name. **Revalidate A1 before dispatch, not during.**

**I searched the whole pinned object for a dispatch note. There is none** — the only three hits for
`dispatch note` / `revalidat` are lines 7, 8 and 22, all inside the banner demanding one.

**So the file states in its own words that it is not the active dispatch, gives a substantive reason
grounded in a user bar of the same date, and the standing clause forbids running it in that state.**

**★ THE CONFLICT I DID NOT RESOLVE ON MY OWN AUTHORITY, STATED PLAINLY.** The user handed me this
file with the words *"read and follow"*. The file says it is parked. **Handing over a file and the
file's own banner disagree, and which of the two governs is not mine to decide** — it is a question
about what the user meant, and the conservative limb is the one the record already fixes: do not run
a parked instruction. **If the user meant it to run, it takes one dated dispatch note in the file and
one word to me.**

## 2. THE SECOND FINDING — the instruction changed under execution

**This is reported as a finding in its own right, because it is the condition
`cowork_audit_protocol.md`'s self-sufficiency clause exists against** (*"A running dispatch is never
interrupted or steered mid-flight"*, **D-251**), and because a session that had not noticed would have
executed a mixture of two instructions and reported it as one.

**Three distinct states of `cc_instruction_register_baseline_repair.md` were observed in this
session**, each read through the sanctioned file tool:

| # | When | Length | Distinguishing content |
|---|---|---|---|
| S1 | Session start, read whole | **457 lines** | No `PARKED` banner. No *"TWO OF THE USER'S DISPOSITIONS"* block. A1: *"Untracked and to be landed by Task 1 — **five** paths"*. Task 1 has **7 steps**. Ruling ledger: *"**Alternative C** … is **NOT RULED**. This batch does not perform it and does not write it."* §3 bullet ordered to become **`cowork_informed_brief_provenance.md`**. |
| S2 | Mid-session, read in two calls | ~**488 lines** | `PARKED` banner **absent**; *"TWO OF THE USER'S DISPOSITIONS … The §8 bar is DROPPED (step 3) and Alternative C is PERFORMED (step 5)"* **present**; A1: *"**seven** paths"*; Task 1 has **8 steps**; §3 bullet ordered to become **`cowork_section8_bar_record_2026_08_28.md`**. The two calls were themselves inconsistent by ~21 lines at the same line numbers. |
| S3 | Pinned object `abd2601f…` | **518 lines** | S2 **plus** the 20-line `⏸ PARKED` banner. |

`cowork_handoff_entry_eighty.md` moved the same way: **157 lines** at first read, **223 lines** at the
pinned object, with a new standing bar, a rewritten errors block and a rewritten cadence block.

**The three files S2/S3 depend on were already on disk when I enumerated the tree** — my Task-1
enumeration, taken before I had seen S2, already lists `cowork_section8_bar_record_2026_08_28.md`,
`cowork_register_rule_c_suspension_2026_08_28.md` and `cc_instruction_backup_cowork_docs.md`. **So the
newer instruction text was, at least in part, already written when I began**, and my first read
returned an older rendering.

**I do not assert which of the two mechanisms produced this** — a genuinely concurrent edit by the
writing side, or a stale snapshot served to the first read. **Both are consistent with the evidence
and I could not separate them.** Either way the operative lesson is the same and it is
**D-253**'s own founding hazard arriving from the other direction: *a reader cannot tell a stale
rendering from a current one without a content-addressed handle*. **Pinning the instruction to a blob
is what made the state decidable, and I recommend it be the standing form for any dispatch whose file
may still be under the writing side's hand.**

**Material consequence, and it is not hypothetical:** under S1 I performed the §3 bullet edit exactly
as ordered. **S2 orders a different bullet, naming a different file, on the ground that the §8 bar is
DROPPED rather than kept.** Had I not re-read, the batch would have landed S1's text under S2's
instruction and reported it as conformant.

## 3. What I did, and what I then undid — the complete account

### 3.1 Acts taken before the STOP was found

1. **The mandatory session-start reads**, in full: `CLAUDE.md`, `STATUS.md`, `DECISIONS.md`; rule (a)'s
   `gating_ids` at `tools/audit/nongating_apparatus_rows.json` → `★_the_live_gating_answer`;
   `BUILD_AND_TEST.md` NOT read (the condition is not met, as the dispatch states).
2. **The dispatch's own read-first list**: `cowork_handoff.md`'s seventy-ninth and seventy-eighth
   entries; `cowork_handoff_entry_eighty.md`; `cowork_audit_protocol.md`'s dispatch-protocol section
   in full, every `###` section carrying the standing-clause marker;
   `cowork_register_blocker_surface_2026_08_28.md` whole.
3. **The full guard set in CHECK mode** — read-only, §4.
4. **Task 0, both limbs** — read-only, §5. **These findings survive the STOP and are reported.**
5. **`tools/audit/changed_paths.py`** — the A1 enumeration, §6.
6. **Two edits to `cowork_informed_session_brief_framework.md`**, under S1 — §3.2. **Both reverted.**
7. **`git add` of six paths at three moments**, to obtain content-addressed snapshots. **The index was
   reset each time and is empty now.**

### 3.2 The two edits, and their reversion proven at the object

**The pre-edit blob was captured before the first edit**, by staging the path and reading its blob id:

```
cowork_informed_session_brief_framework.md   f153c9231b80cd758bd3e7e62abac1581f38dd66   (pre-edit)
```

**Edit 1 — the §8 deletion (S1 Task 1 step 2, unchanged in S2).** Performed, and **its byte-identity
precondition was proven, fail-closed** — see §7, which is a real measured result worth keeping.
Resulting blob `b79e3b9977fa9018a38b9a02a4bcdb1962a5b050`;
`git diff --numstat f153c92 b79e3b9` = **`0 19`** — zero insertions, nineteen deletions.

**Edit 2 — the §3 closed-list bullet, S1's wording.** Resulting blob
`2c36e350bf5ea824eaa40741765bef147ecd4d8c`; `git diff --numstat b79e3b9 2c36e35` = **`2 1`**.

**Both reverted with the Edit tool, exactly.** After reversion the path was re-staged and re-hashed:

```
cowork_informed_session_brief_framework.md   f153c9231b80cd758bd3e7e62abac1581f38dd66   (post-revert)
```

**Identical to the pre-edit blob. The reversion is byte-exact and is proven at a content-addressed
object, not asserted.** The index was then reset; `changed_paths.py --staged` reports **0 records**.

### 3.3 The tree's end state, measured

```
843 changed path records  =  841 untracked  +  2 tracked modifications
```

— the **same three figures** the pre-edit enumeration produced. The two tracked modifications are
`cowork_handoff.md` and `cowork_informed_session_brief_framework.md`, both at their incoming content.
`HEAD` and `origin/master` are both `6005daecaf9f1a6692e61521911ef8b99ed73b55`.

**Nothing was created, deleted, renamed or committed. `cowork_handoff_entry_eighty.md` still exists.**

## 4. The guard set at the start — run, and it grades A2

`python tools/audit/gen_guard_state.py --check` — **exit 0**, *"the guard state re-derives"*, so the
committed `guard_state.json` matches the run exactly and **nothing was rewritten**.

```
75 guard(s) run, 3 failing, 4 not run, 16 historical record(s)
```

The three failing, and no others:

| Failing check |
|---|
| `tools/audit/gen_filing_convention_application.py --check` |
| `tools/audit/decisions/apply_soft_discard.py --check` |
| `tools/audit/decisions/apply_residue_discard.py --check` |

**A2 — GRADED, ONE LIMB MET AND ONE FALSIFIED.**

- **Limb 1 (75 / 72 / 3, the three named): MET**, exactly.
- **Limb 2 (`gen_evidence_pin_membership.py --check` red at the start): FALSIFIED — it PASSES.** So
  does the whole-artifact re-derivation. **The declared start state is wrong on this point**, in the
  safe direction: fewer reds, not more, so the dispatch's *"a further failing verdict is a
  STOP-and-report"* is not engaged.
- **The cause is measurable and worth carrying forward:** the membership derivation's population moved
  for the *previous* batch because that batch's untracked inputs were **`cowork_rulings_*` records**.
  **None of this batch's untracked inputs is a ruling record**, so the derivation does not see them.
  **The declared start state inherited a cause rather than re-deriving it** — which is the shape the
  standing clause *"a prediction drawn from the route whose cause is known reads as complete when it
  is not"* (**F75**) already names.
- **Consequence for the parked dispatch:** Task 1's step ordering *"`gen_evidence_pin_membership.py
  --check` must PASS"* is already true before the batch starts, and its step ordering the artifact
  regenerated-and-measured will most likely measure **no movement at all**. Worth saying in the
  revalidation rather than discovering at run time.

**A5 — NOT GRADED.** The boot pack was not touched and its generator was not run; I did not prove the
manifest by hash, because the batch did not reach any act that could have moved it.

## 5. TASK 0 — performed in full, read-only, and it survives the STOP

Both limbs are answers to questions about *the record and the git objects*, not about the dispatch, so
they stand whatever happens to the instruction. **They are reported here so the work is not lost.**

### 5.1 THE BRANCH — I land on limb **(a)**, and the grounds are quoted at the record

`cowork_rulings_2026_08_17_residue_sitting.md` was read **whole** (123 lines). §5 in full:

> **5. Derived expectations for the executing dispatch (checked, never assumed)**
>
> Every population above is derived at execution from the two named artifacts. The arithmetic
> these rulings imply, **stated as a registered expectation for the executing batch** and not as a
> hand construction: keep side 411 + 10 + 47 + 6 = 474; discarded 165 + 29 + 9 = 203; 474 + 203
> = 677, the register's whole non-trivial population; the live register falls 512 → 474. **A
> derivation that does not reconcile to these sums is a STOP-and-report, not an adjustment.** The
> executing acts run under the read-before-move discipline and the retired-block pattern the
> fifth batch established; affected artifacts regenerate under the ordinary bound; the census's
> candidacy rules stand untouched (a discard's effect on the retirement census is classed
> movement, the F35 pattern, published not blurred).

**The five grounds, each checkable at the record:**

1. **The addressee is named three times and it is the executing act, not a later one.** The heading is
   *"Derived expectations for **the executing dispatch**"*; the sentence's own paragraph says *"stated
   as a registered expectation for **the executing batch**"*; and the sentence immediately after it
   begins *"**The executing acts** run under…"*. The subject of the prohibited sentence is *"a
   derivation"* — a derivation performed at execution.
2. **The sentence names two responses to a failure and requires the first.** *STOP-and-report* versus
   *adjustment*. It says what an executing session does when its derivation fails; **it says nothing
   about what "reconciling" means, and nothing about whether a later ruling may change it.**
3. **That first response has been performed, to its end.** The checks STOPPED; the cause was
   established at the data file; the blocker was REPORTED to the user on
   `cowork_register_blocker_surface_2026_08_28.md`; and the user disposed of it. **A later act taken
   on a reported STOP is what the sentence's own remedy exists to produce.** Reading (b) would make a
   reported STOP unresolvable by any act at all, which would make the report pointless.
4. **Alternative B preserves every sum the sentence protects** — 474, 203, 677 and the 512 → 474
   movement — and changes only which population they are reconciled over. Nothing the sentence names
   moves.
5. **The record puts a failing mechanism's fate with the user, not with the mechanism.** **D-436**:
   *"A mechanism that fails any of them is REPORTED — with the condition it fails, the measurement
   that shows it, and the reason that condition exists. It is NOT removed automatically: keeping it or
   removing it is the user's ruling."* That is this situation exactly.

**THE CASE AGAINST, GRADED RATHER THAN DISMISSED — and the dispatch's quotation of it is not at the
source.** The dispatch attributes to `apply_residue_discard.py`'s docstring the sentence *"THE
SITTING'S OWN ARITHMETIC IS RE-RECONCILED against the record as it stands, and the ruling makes that a
STOP rather than an adjustment in its own words."* **That sentence is not in the file.** What is in
the file are two separate texts:

- the docstring's STOP list — *"the sitting's own arithmetic not reconciling — keep 474, retired 203,
  total 677 — STOPS it, and the ruling says so in terms: **"A derivation that does not reconcile to
  these sums is a STOP-and-report, not an adjustment."**"*; and
- a source comment above the live re-check — *"# The sitting's own sums, re-reconciled against the
  record as it stands."*

**The substance of the objection survives the mis-quotation and I graded it on the substance:** the
tool's author does read the ruling sentence as governing the tool's *live* runs, which widens the
addressee §5 states. **But even at that widest reading the sentence only makes a non-reconciliation a
STOP. It does not say a later ruling may not change what reconciling means** — and a session
observing the STOP and reporting it is precisely what happened. **The objection does not reach limb
(b).**

**So: (a). I did not find myself arguing the case, and I did not reach the dispatch's
take-(b)-on-doubt fallback.** ***This grading changes nothing on its own — Task 2 is not performed,
because the instruction is parked, not because of the branch.***

### 5.2 THE BUMPING COMMIT — established at the objects

Located with the pickaxe over the field, restricted to the data file — **exactly one commit in the
whole history changes the number of occurrences of `"the_population_before_this_retirement": 680`**:

| | |
|---|---|
| **Commit** | `4c47b55f3ded9f731f60691faec871646fdc4d7b` |
| **Date** | 2026-08-26 09:52:40 +0200 |
| **Author** | Vincent Wong |
| **Subject** | *"land the amendment-landing batch's work, with ONE of the four ordered register entries STOPPED and reported rather than forced. …"* |

The hunk, at `git diff 4c47b55f3d^ 4c47b55f3d -- tools/audit/decisions/backbone_decisions.json`:

```
-    "the_population_before_this_retirement": 677,
+    "the_population_before_this_retirement": 680,
```

**The dispatch named in it.** The commit message names **no `cc_instruction_*` file**; it names *"the
amendment-landing batch"*. The batch's files are on disk as `cc_instruction_amendment_landing.md` and
`cc_report_amendment_landing.md`. **Neither is in that commit** — it touched 30 paths, none of them a
`cc_*` file.

**Does that act's own dispatch or report mention the field? — DISPATCH NO, REPORT YES, AT LENGTH.**

- **`cc_instruction_amendment_landing.md`: no mention of the field, in any form.** The move was not
  ordered.
- **`cc_report_amendment_landing.md`: mentions it repeatedly and gives it a section.** §7.3 —
  *"★ A STRUCTURAL FINDING — THE REGISTER CANNOT ACCEPT A NEW ENTRY WITHOUT TURNING A GUARD RED"*,
  sitting inside *"## 7. TASK 6 — THREE ENTRIES ENTERED, IN GROUP T"* — records that
  `gen_decisions_register.py` refuses to render unless `len(live) + len(retired) ==
  retired_entries.the_population_before_this_retirement`, quotes the renderer's STOP, and states:
  *"The field was therefore moved **677 → 680**, on the block's own recorded reading of it … a
  sentence that accounts for retirements and **says nothing about additions**."* Its own standing
  self-check, item 3, declares it again: *"`the_population_before_this_retirement` **was moved by this
  batch**, 677 → 680. It is an authored field in a data file this batch is authorised to edit, the
  move was forced by the ordered act, and §7.3 is its full account. **It is the only figure in the
  register data this batch moved that was not derived.**"*

**★ THE PART THAT CORRECTS THE RECORD AS IT NOW STANDS.** The seventy-ninth handoff entry says
*"NOT ESTABLISHED AND OWED: which act bumped it, and under what dispatch"* and frames it as a possible
silent change — *"Whoever added D-678, D-679, D-680 … bumped the field so the block-level arithmetic
would keep passing"*. **The act was neither silent nor unrecorded.** It was declared in its report, in
a titled section and again in the self-check, with its cause, its reasoning and its consequence —
including that it turned the two discard checks red. **What was missing was not disclosure. It was a
route from a landed report's finding into a ruling.** The commit message itself says the two reds
*"stand unregenerated and are reported, not adjusted"*, which is that batch obeying the very rule the
branch question above turns on. **This is REPORTED and nothing is done about it, as ordered.**

## 6. A1 — enumerated at the objects, and it holds, with one measurement the dispatch did not ask for

`python tools/audit/changed_paths.py`:

- **Tracked modifications: exactly TWO**, and both are A1's declared paths —
  `cowork_informed_session_brief_framework.md` and `cowork_handoff.md`. **No third. A1 clause 3 holds.**
- **A1 clause 2 asked which state the handoff is in: it is MODIFIED.**
- **Untracked: 841 records**, total **843**.
- **All seven of S2's untracked landing paths are present**, as are `cowork_handoff_entry_eighty.md`
  and `cc_instruction_backup_cowork_docs.md`.

**★ A MEASUREMENT THE REVALIDATION WILL NEED, TAKEN BECAUSE IT BEARS ON TASK 1 STEP 4.** The handoff's
tracked modification does **not** carry one unlanded entry. It carries **two**.

| Object / path | Loose pattern `^## .*COWORK SESSION CLOSE` | Top entry |
|---|---|---|
| `cowork_handoff.md` at HEAD, blob `ad8206fd9a818a470db56f1319dad57d538d7a01` | **79** | SEVENTY-**SEVENTH** |
| `cowork_handoff.md` in the working tree | **81** | SEVENTY-**NINTH** |
| `cowork_handoff_entry_eighty.md`, blob `a68a59195f755d974701865e94e42e644b110158` | **1** | EIGHTIETH |

**So the seventy-eighth AND the seventy-ninth entries are both unlanded**, and the ordered prepend
would make the file carry three unlanded entries at once. **The dispatch's A1 clause 2 — *"The writing
side did not touch it this session"* — is true and is not the same statement.** The strict-pattern
figure was **not** measured: the batch did not run Task 1, and the loose figure is the one the
dispatch names.

## 7. The §8 byte-identity result — measured, and kept although the edit was reverted

**The proof was obtained and it PASSED**, so the writing side does not need to re-establish it: the
brief's §8 and the corresponding region of `cowork_informed_brief_provenance.md` **are byte-identical**.

**The method, stated precisely because it is not the one the dispatch ordered.** The dispatch says
*"Compare by hash of the two extractions."* **No sanctioned route to that hash exists here.** Hashing
two extractions from working-tree files means reading working-tree content through a shell utility,
which **D-253** bars *("The restriction is on WHAT is read — working-tree content through a shell")*,
and neither file is in git, so there is no object to hash instead. **I did not route around the bar.**

**What I did instead is strictly stronger in the direction that matters.** I transcribed the region
from `cowork_informed_brief_provenance.md` (its `## 8. Provenance …` heading through the last
non-empty line before the `---` that follows it — **18 lines**) and used that exact byte sequence as
the `old_string` of an exact-match, fail-closed Edit against the brief. **The Edit succeeds only on a
byte-exact match and deletes nothing on any difference** — so the dispatch's own condition (*"A
difference of any kind is a STOP-and-report and nothing is deleted"*) is enforced by the mechanism
rather than by my judgment. **It matched.**

**Measured, at blob-to-blob diffs by explicit hash:**

| Quantity | Value |
|---|---|
| Region compared | the `## 8. Provenance …` heading through the last non-empty line — **18 lines** in each file |
| `--numstat`, §8 deletion alone (`f153c92` → `b79e3b9`) | **`0 19`** — 0 insertions, **19 deletions** |
| Deleted line count | **19** — the 18-line region plus the blank line preceding the heading |
| Separator deleted | **none**; there is no `---` before the heading in the brief, only a blank line |
| `--numstat`, §3 bullet edit alone (`b79e3b9` → `2c36e35`) | **`2 1`** |
| Remaining `§8` references in the brief after the edit | **one**, the new bullet itself, which names the new file — no dangling pointer |

**All of it has been reverted. The figures are reported as evidence that the precondition holds, not
as work landed.**

## 8. TASK 3 — NOT PERFORMED, and a pre-flight finding that will stop it whenever it is dispatched

**The sweep was not run.** But I probed its feasibility before the STOP was found, and **the ordered
check cannot be performed in this environment by any sanctioned route.** This is reported now so the
revalidation can fix the dispatch rather than discover it at run time.

**Measured, on the row the dispatch already knows to be false:**

1. **The `Read` tool cannot open a PDF here.** `docs/research_papers/humphrey_bello_2015_ismir_four_timely_insights_ace.pdf`
   returns: *"pdftoppm is not installed. Install poppler-utils … to enable PDF page rendering."*
   `which pdftoppm` confirms it: **absent**. So do `mutool` and `gs`.
2. **`Grep` reads the PDF's raw bytes but cannot see its text.** The file matches `PDF|obj|Creator|dc:title`
   **371** times, so the reader reaches it — but it matches *"Timely"* **0** times and
   *"Electric Guitar|Playing Technique"* **0** times. **Neither the row's title nor the true title is
   findable**: the text streams are compressed. **The method's measured detection power for this
   defect class is ZERO**, on the one case where the answer is already known — which is the only
   honest way to state it (**D-436**, **#19**).
3. **`pdftotext` IS present** at `/mingw64/bin/pdftotext`. **I did not use it, and this is a
   deliberate refusal, not an oversight.** Pointing it at a repository path is a shell read of
   working-tree content, which **D-253** bars in terms, and the 2026-08-08 widening says the rule
   *"covers every read mechanism and every dialect"*. **The record's own lesson for a bar a session
   thinks is over-broad is to report it, not to route around it** (Ruling 5 of 2026-08-26: *fix the
   bar rather than re-rule around it* — and fixing it is the user's act).
4. **No Python PDF library is available** either: `pypdf`, `PyPDF2`, `fitz` and `pdfminer` all absent.

**So every `Local ✓` row would grade UNCHECKABLE on the identity question, for a single environmental
cause — a result with no information in it.** **The population, for sizing the revalidation:** the
`Local` column carries **58** `✓` rows across the three tables, **57** of them PDF-backed (the
fifty-eighth, the BCMH row, points at the directory `tools/BCMH_dataset/`); the folder holds **59**
PDFs, and one row covers two papers. **The rows do not name their files** — the mapping is by filename
convention, and `docs/research_papers/README.md` indexes only the seven user-supplied copies.

**The two routes out, stated without a recommendation** (the record reserves the choice): install
poppler's `pdftoppm` so the sanctioned reader can render PDFs; **or** a user ruling that a
PDF-to-text conversion of a repository file is admissible under **D-253**. **The known-false row —
`BIBLIOGRAPHY.md` line 86, Humphrey & Bello 2015 — is carried forward RELAYED from the seventy-ninth
handoff entry and was NOT re-established here.**

## 9. Registered expectations and assumptions — graded

| | Verdict |
|---|---|
| **E0** | **MET.** §5 — the branch limb taken with the words it rests on quoted at the record; the bumping commit identified at the object with its date and subject; and the dispatch/report question answered both ways. |
| **E1** | **NOT MET — NOT ATTEMPTED.** No commit; the two edits made were reverted; the handoff was not prepended; the suspension list was not derived; no artifact regenerated. §3, §6, §7 report what was measured on the way. |
| **E2** | **NOT MET — NOT ATTEMPTED.** Task 2 was not reached. **Not because of the branch — the branch permits it (§5.1) — but because the instruction is parked.** |
| **E3** | **NOT MET — NOT PERFORMABLE.** §8. |
| **E4** | **NOT MET — NOT ATTEMPTED.** No close, no `STATUS.md` entry, no forward-bound move, no end-state run. |
| **A1** | **HOLDS** — exactly two tracked modifications, both at declared paths, no third. §6. |
| **A2** | **SPLIT — limb 1 MET, limb 2 FALSIFIED.** §4. |
| **A3** | **NOT GRADED** — Task 2 not reached. |
| **A4** | **NOT GRADED** — the later-entry set was not derived. **Nothing about it is asserted here, by either route.** |
| **A5** | **NOT GRADED** — the boot pack was not touched and its manifest was not proven by hash. |

## 10. What this session did NOT do

- **No commit, no push.** `HEAD` and `origin/master` unmoved at `6005daecaf9f1a6692e61521911ef8b99ed73b55`.
- **No tool source edited.** `apply_soft_discard.py` and `apply_residue_discard.py` are untouched.
- **No register data edited.** `the_population_before_this_retirement` still reads **680**; no entry
  created, moved, retired, revived or edited; no `D-NNN` allocated.
- **No file created, deleted or renamed.** `cowork_handoff_entry_eighty.md` still exists.
- **No `CLAUDE.md`, `ARCHITECTURE.md`, `DECISIONS.md`, `OPEN_ITEMS.md` or `STATUS.md` edit.** No
  ruling record touched. No open-items row created, flipped or discarded. No finding number allocated.
- **No `src/` change, no test, no golden, no measurement of the analysis, no session booted, no pack
  rendered, no placement test, no framework text authored.** None of the three sealed placement-sample
  files was opened; `ARCHITECTURE.md` was not opened.
- **No guard weakened, exempted or re-aimed.** The only guard activity was one read-only CHECK run.
- **The suspension file and the §8-bar record were staged for a hash and then unstaged. Neither was
  read.**

## 11. What the writing side has to settle before this can run

**Stated as facts and questions, with no recommendation** (`cowork_audit_protocol.md`: *where the
record does not settle the question, the surface that returns it gathers facts and makes no
recommendation*).

1. **Is this dispatch active or parked?** The file says parked; the user handed it over. **One dated
   dispatch note in the file settles it.**
2. **If it is to run, A1 must be revalidated** — the banner says so itself. §6 gives the current
   figures, and they will move again with every further write to this tree.
3. **The declared start state needs one correction**: `gen_evidence_pin_membership.py --check` is
   **green**, not red, and the reason is that none of this batch's untracked inputs is a
   `cowork_rulings_*` record. §4.
4. **Task 3 is not performable as written.** §8. It needs either poppler installed or a ruling.
5. **Task 0 is already done and need not be re-run** — §5. The branch reads **(a)**; the bumping
   commit is `4c47b55f3d`, and its **report declared the move in full while its dispatch never
   ordered it**.
6. **The instruction was moving under execution.** §2. **Whatever the cause, a dispatch handed to a
   session should be final at the moment it is handed over** — and pinning it to a blob at Task 0 is
   the cheapest mechanical guard against a repeat.
7. **Everything in this dispatch is apparatus**, by the banner's own reasoning and
   `CLAUDE.md`'s non-gating declaration: it bears on neither the analysis, nor its inputs, nor a
   measurement tool the analysis depends on. **The plan's live act is the framework document's
   placement test.** This report moved it not at all.

## 12. The standing self-check over this session's own work

1. **Principles.** **#13** — the surprise (a moving instruction, then a parked banner) was surfaced as
   a STOP before anything was built around it; that is this report. **#12** — nothing was destroyed:
   the two edits were reverted byte-exactly, the staging file survives, and the §8 identity result is
   kept rather than discarded with the edit. **#6** — no second home was created for anything.
   **#15** — every claim here is verified at objects, not at assertion: the reversion at a blob hash,
   the bumping commit at a diff hunk, A1 at the enumeration, the guard state at its own run. **#19** —
   the PDF method's detection power is **measured at zero** on a known-positive rather than assumed
   workable, and A2's falsified limb is reported as falsified. **#17f / D-431** — no figure is carried
   from the dispatch; every one here was measured in this session, and where a figure is a quotation
   of a source it is marked as one.
2. **Conventions.** American English. No self-invented label, abbreviation or numbering. No
   music-theory word arises in a non-musical sense in this batch's subject matter; *score*, *key*,
   *measure*, *register*, *note* and *figure* appear only in the qualified forms the convention fixes
   (*the open-items register*, *the decisions register*, *measurement*, *figure* as a reported value
   is written *figure* only where the record's own phrase requires it).
3. **File-tools rule (D-253).** Every working-tree read went through Read / Grep / Glob. The shell was
   used for: git object queries by explicit hash; `git add` / `git ls-files -s` / `git reset` to
   obtain and clear content-addressed snapshots; the sanctioned Python tools; and two non-repository
   environment probes (`which`, a module-availability check). **`pdftotext` was available and was
   deliberately not used** — §8. **The armed guard denied one `sed` on a repository path early in the
   session and the denial was obeyed, not worked around.**
4. **Uncertainty (#24).** The one comparison I cannot resolve is stated as unresolved: **whether the
   instruction file was concurrently edited or my first read was stale.** Both are consistent with the
   evidence; I did not choose between them, and no claim in this report depends on which it was.
5. **What I am least sure of, said plainly.** The branch grading in §5.1 is a reading of a sentence,
   and readings are the thing this project's record says go wrong most often. **I did not reach the
   dispatch's take-(b)-on-doubt fallback, and I say so rather than hedging** — but the grading is
   offered with its five grounds and the case against it quoted at the source **precisely so that it
   can be overturned at the record rather than accepted on my say-so.** Nothing was done under it.
