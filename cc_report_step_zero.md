# CC report — STEP ZERO of the ratified successor plan, and the landing of the 2026-08-21 record

> **Dispatch:** `cc_instruction_successor_plan_landing_and_step_zero.md` (Cowork, 2026-08-21, the
> thirty-eighth session), executing Rulings 6 and 7 of
> `cowork_rulings_2026_08_21_successor_plan_sitting.md`.
>
> **ALL FIVE TASKS RAN. TASK 3 IS A PER-ENTRY PASS AND IS STOPPED AT A RECORDED BOUNDARY** — the
> standing clause admits that, and the stop is recorded below in the form that clause fixes: which
> hunks were read, that the remainder is UNTOUCHED rather than partly worked, and that nothing is
> left half-edited.
>
> **NO STOP-AND-REPORT RULE FIRED.** Every red the batch met was classed by its MEASURED cause and
> every one of those causes is this batch's own act.
>
> **The bars held whole.** No `src/` edit. No golden. No test changed, moved or run. Nothing under
> `tools/corpus/` or `tools/robust_stop/`. No measurement of the ANALYSIS built, designed, scoped or
> run. No design, no repair, no derivation of any specification, no frame, no pilot act, no
> fact-gate admission, no ledger. No document archived, moved or deleted AS A FILE. **No open-items
> row created, flipped or discarded.** **No screened document edited** — `ARCHITECTURE.md`,
> `docs/scoring_model.md` and every document-set member were read and never written. No caller flag
> or candidacy acted on. No finding number allocated; the series stands where it stood.
>
> **Figures are not transcribed here (D-431).** Every population, count, verdict and share is named
> as an artifact and a field, or stated as a DIRECTION with its artifact named (D-663). The only
> bare quantities below are commit identities and the counts of this batch's own acts.

---

## 1. The chain of commits, named as far as a sentence can name it

Six commits, each pushed to `origin/master` and each verified at the object by explicit hash:

| # | commit | what it carries |
|---|---|---|
| 1 | `292e4506b6` | Task 0 — the whole 2026-08-21 record landed; eighteen paths |
| 2 | `50e7b9fd0c` | Task 1 — the specification document set derived (Ruling 6) |
| 3 | `f34b451fe8` | Task 2 — the screen population widened over that set (Ruling 7) |
| 4 | `67ecba11e1` | Task 3 — both populations read, every member accounted for, none yet graded |
| 5 | `ac17b7fdba` | Task 3 — verdicts authored, the first bounded run |
| 6 | `553dd5f405` | Task 3 — verdicts authored, the second bounded run |

**THE SEVENTH COMMIT IS THIS CLOSE, AND A SENTENCE CANNOT NAME ITS OWN HASH.** It carries this
report, the `STATUS.md` entries, the forward-bound move and the close section. **AND AN EIGHTH
FOLLOWS IT**, carrying the end-state guard run — because the end-state run is taken *after* the
commit that carries the close exists, so its values cannot be written into that commit. That is the
E-ordering rule at both grains, and it is why this section names six commits and declares two.

---

## 2. Task by task

### Task 0 — the record landed and the push performed

The branch rule was taken at the tip by `git show --stat` at the explicit hash and at nothing else:
the dispatch was **not started**, so it was mine to run.

**A1 was checked FIRST and entirely at content-addressed objects**, by the per-path commands A1
names, because `git status` is measured to time out on this mount. It **HELD**: exactly one tracked
modification (`cowork_handoff.md`, five inserted handover blocks against a committed blob whose
entry point is the thirty-third), `tools/audit/evidence_pin_membership.json` UNMODIFIED, and all
sixteen named untracked paths present on disk and absent from the tip. The two invariants the
dispatch pins — the open-items INDEX blob and the non-gating apparatus artifact's blob — were read
at the tip AND in the working tree and are byte-identical to the hashes the dispatch names.

**The membership regeneration was measured against BOTH halves of the prediction before it was
accepted, and the prediction HELD on both.** Route A: the count rose by exactly two and the two
predicted record names were added. Route B: nothing — no third hunk, exactly as the writing side
predicted from the records' own text before the run. No member, route, document, pin constant,
state or count moved beyond those two additions. The difference is at
`tools/audit/evidence_pin_membership.json` and is not restated here.

Eighteen paths were staged **by explicit path**, never by `git add -A` or `git add .`, and committed
with the subject the dispatch prescribes verbatim. `origin/master` moved to that commit, verified at
the object. `gen_evidence_pin_membership.py --check` **passes** at the resulting tree — the red the
declared start state attributed to this dispatch's own untracked inputs is cleared by the act that
tracked them.

### Task 1 — the specification document set, derived and published whole

`ARCHITECTURE.md` was read **in full** at the tip before anything was written. The three limb-1
regions the ruling names were located by heading; their line ranges are DERIVED from the file's own
heading structure, so a heading that moves cannot leave a stale range behind.

Every naming of another document in `ARCHITECTURE.md` was enumerated by scanning the file — the
population is derived, and **a naming with no authored grade halts the derivation**, in both
directions. Each target's grade is authored under `CLAUDE.md` decisions-register rule (i), with (h)
for scope and (k)/(k1) where a document is named more than once, and **every deciding clause is
located in `CLAUDE.md` at run time and quoted from there** rather than from the dispatch. For every
ADMITTED target the governing naming's anchor is located in `ARCHITECTURE.md` and must sit on a line
that names that target, or the tool stops.

**A3's check was run and reconciles BOTH WAYS.** Every seed-admitted delegation sited in
`ARCHITECTURE.md` was re-found at the text — none is missing, so the STOP the dispatch attaches to
that condition did not fire. Every text-found admitted delegation absent from the seed's live table
is NAMED, and the **miss rate against the seed is published as part of the derivation's name**
(D-661) at `tools/audit/specification_document_set.json` →
`the_seed_reconciliation.miss_rate_against_the_seed`. The artifact also states, in its own words,
that the seed answers a different question — where a register entry lives — which is A3.

**No member has no file:** every member of the derived set exists at the tree, checked per member.

The tool is `tools/audit/gen_specification_document_set.py`; its `--check` re-derives and exits 1 on
drift. **No recognizer over prose decides a grade** — the scan finds filenames, a mechanical
identity, and every judgment about whether a naming delegates is authored, one per target, each
naming what it was made from (F42, F84).

### Task 2 — the screen population widened, its method untouched

`tools/audit/gen_period_stratum_split.py` gained a SECOND population beside its existing fields.
Selection is **by MEMBERSHIP of the document set and by nothing else**, across every stratum,
in-period and out-of-period alike; the document ROLE is reported per hunk and excludes nothing,
which is the candidate generator's own ruling 4 inherited rather than re-decided. The artifact
states why membership rather than role is the whole of what the widening means: every `cowork_*.md`
document carries one role, so a document-set member sits outside the old population by role alone.

**Every existing field is byte-unchanged, and that is measured rather than asserted.** The artifact's
diff against the previous commit is **additions plus exactly one changed line**, and that line is the
last existing field re-emitted with the trailing JSON comma an appended key requires — verified by
comparing the removed and added forms, which differ only by that comma. No line inside any existing
field changed.

**The relation to the existing population is taken BOTH WAYS**, with a STOP on any hunk the two
readings cannot reconcile: every already-screened hunk whose file is a member must appear in the
widened population; the widened population must partition exactly into already-screened and NEW; and
the existing screen population must partition against membership. None in both, none in neither. The
existing screened hunks that are NOT document-set members are named by document, so no reader takes
the widened population for a superset of the old one.

**The inherited establishment caveat travels verbatim** into the new field: the candidate generator
underneath has never been positively established (#19), and nothing here discharges that.

### Task 3 — the authored verdict per NEW hunk, and the distribution

`tools/audit/gen_july_screen.py` now reads BOTH populations. **The method is inherited whole** — the
four classes, the ORDER they are applied in, the six reported shapes and the five STOPs are
untouched, which is Ruling 7's own clause. Two values are added and **declared as additions**:

- **`NOT YET READ`** — the one declared exception to the STOP that a population member with no
  authored verdict halts the tool. An unread widened member is admitted to the artifact, counted in
  its own class and reported as unread; **never silently absent, and never counted as
  `UNDETERMINED`.** It is the DEFAULT for an unauthored member and **may not be authored**, so a
  member cannot be marked unread as a judgment.
- **`OUTSIDE NAMED SECTIONS`** — recorded and NOT graded, so the four classes never reach text the
  ruled document set does not cover.

**A widened hunk that is already in the existing screen INHERITS that hunk's verdict**; none of the
original sixty-eight is re-read or re-graded.

**The existing sixty-eight verdicts are byte-unchanged, measured twice.** First, a digest over the
canonical form of the existing authored block is published at every run
(`july_screen.json` → `★_the_widened_screen.the_existing_verdicts_digest`) and is **identical across
every run of this batch**. Second, the artifact's own diff at the scaffold commit is a **pure
addition with zero deletions** — no existing line moved at all.

### Task 4 — the close

One `STATUS.md` pointer entry per task that did work, and **in the same act** the fourteenth batch's
entries moved verbatim to `STATUS_ARCHIVE.md` through `gen_status_batch_bound.py --apply`, **both
directions proven** by the tool: byte-present in the archive exactly once, absent from the must-read.
The declared `Last updated:` prefix adjustment is imported from its one home and not re-decided (#6).
No entry text was retyped; the move is byte-faithful by construction.

---

## 3. The sizing reported BEFORE Task 3 opened

Stated as a direction with its artifact named, never as a transcribed value (D-663):

**The widened NEW population is manifestly beyond one working session** — it is several times the
size of the whole existing screen population, which itself took a dedicated batch to read. Its exact
size is at `tools/audit/period_stratum_split.json` →
`★_the_widened_screen_population.★_the_size_the_next_task_reads`.

Per the dispatch that is **not a STOP**: Task 3 is a per-entry pass and stops at a member boundary
with its stop recorded. It was said before the first hunk was read, and it is what happened.

---

## 4. THE STOP, recorded in the standing form

**What was completed.** The verdicts authored cover, in the artifact's own order (by document, then
by commit, then by hunk), the NEW hunks of `ARCHITECTURE.md` from the first NEW commit through the
commit `88fd87e9d16e2eacca38c9dd8ea4c1e4a43d7b27` inclusive — five commits: the phase-1 homing acts,
the phase-1 truth-sync, the phase-1d riding act, the phase-1i pointer pass and the phase-1j homing
half.

**What was NOT done, and its state.** Every remaining NEW hunk is **UNTOUCHED**, not partly worked.
Each carries the verdict `NOT YET READ`, which is the tool's default for an unauthored member and
which no hand set. **Nothing is left half-edited:** the tool's `--check` re-derives byte-identically
at every commit of this batch, the artifact is never behind the tool, and the report lists the unread
remainder per document.

**How a continuing session derives the remainder.** Freshly, from the artifact — never from this
report's account of it. The order is the artifact's own, and the unread set is exactly the members
whose verdict is `NOT YET READ` at `july_screen.json` → `★_the_widened_screen.the_hunks`, summarised
per document in `july_screen_report.md`.

---

## 5. What the screen found, stated as directions

**The ruled failure signal did NOT fire, and it is not yet able to.** It is evaluated mechanically at
the artifact (`★_the_widened_screen.★_the_ruled_failure_signal`) and reports
**INCONCLUSIVE-AT-THIS-COVERAGE**, with the read share published beside it. That is the ruling's own
treatment of a majority reached on a part-read population — *"a majority reached only because few
members were read is reported as INCONCLUSIVE-AT-THIS-COVERAGE with the read share named, not as the
signal firing."* On the members read so far the `UNDETERMINED` class is **a minority**, so nothing so
far points toward the premise being unmeasurable by this screen; but that is a direction over a small
read share and is not a verdict.

**On the members read so far, the dominant class is POSITIVELY CODE-INFLUENCED**, and it is
concentrated in one commit — the phase-1 truth-sync, whose own account states the direction of the
correction in terms: *"a specification cannot be the compliance standard while it misdescribes the
code, so every statement the named open-items rows establish as false at HEAD is corrected."* That is
the screen's first class by its own second limb, and the corrections cite code coordinates the commit
did not write. **This is the pollution the successor plan's founding premise names, measured rather
than assumed.**

**★ A CODE-INFLUENCED HUNK HERE IS NOT THE PERIOD QUESTION'S FALSIFICATION, and the artifact says so
in its own field.** The falsification rule belongs to the ORIGINAL screen, whose population is
out-of-period by construction; a code-influenced correction found THERE would mean the ruled period
start is misplaced. This population is deliberately wider because Ruling 7 asks it to MEASURE the
pollution rather than to test the period, so an IN-PERIOD code-influenced hunk is the measurement's
own subject and is EXPECTED. Each hunk records whether it is in period, so the two readings never have
to be guessed apart.

---

## 6. Quarantined audit questions from step zero

*The heading is the dispatch's. Under Ruling 9 a finding that bears on the analysis, its inputs or a
measurement tool is SURFACED here — not rowed, not numbered, not acted on.*

1. **A THIRD OF THE SPECIFICATION DOCUMENT SET IS INVISIBLE TO THIS SCREEN, AND FOUR LAYER
   SPECIFICATIONS ARE IN THAT CLASS.** The coverage gap is published whole at
   `period_stratum_split.json` → `★_the_widened_screen_population.the_coverage_gap`, and every silent
   member carries the reason the enumeration gives for ITSELF: no commit of the candidate
   enumeration's own population ever touched the file. **The consequence for the plan is not small:**
   the pollution distribution the reading depth and the ordering of units are to be taken from cannot
   speak about those members at all, and a reader must not take a member's absence from the
   distribution for a clean verdict on it. This bears on a measurement the plan depends on, which is
   why it is surfaced rather than left in the artifact.
2. **THE MEASURED POLLUTION IS DOMINATED BY ONE MEMBER WHOSE SUBJECT IS NOT THE ANALYSIS.**
   `STATUS.md` contributes about half of the whole widened population. It is a member by the ruled
   mechanism — `ARCHITECTURE.md` makes it a mandatory read, binds an update rule to it and gives it
   precedence on current state — but its subject is implementation status, not a specification of the
   analysis, and the plan's §5 exclusion list does not reach it. **Whether it belongs in the set is
   the user's**, and until that is answered the per-document distribution must be read per document
   rather than in aggregate.
3. **`ARCHITECTURE.md`'s DELEGATIONS REACH THE PER-LAYER DESIGN DOCUMENTS ONLY THROUGH A GLOB AND AN
   ELLIPSIS, WHICH RULE (k) MAKES CONFER NOTHING.** Every layer specification in the derived set is
   there by a separate delegation the user wrote, not by the document-governance clause that plainly
   means to include them. So a design document nobody separately delegated to is outside the set
   although that clause intends it. Ruling 6 asks for the completeness of the delegations as a
   FINDING and not as an assumption; this is that finding, and it is not acted on here.
4. **ONE GRADE IS A DECLARED NEAR-TIE.** `cowork_idiom_entry_mapping.md` enters the set on a naming
   that is grammatically the bar's first admitted form and can also be read as the excluded appended
   citation. Both readings and the consequence of each are recorded at the grade itself. Under the
   competing reading the member leaves the set; nothing else turns on it.

**No finding here is rowed, numbered or acted on**, and no establishment obligation was met or
discharged by anything in this batch.

---

## 7. Findings DISCARDED under the worth test (#10), with finding, date and reason

1. **A new tool of this batch lands in the recognizer sort's `no_external_candidate_source_found`
   residue although it draws its candidates from files it does not write** (2026-08-21). *Reason:*
   the sort declares its own membership recognizer's reach UNMEASURED and publishes its member list
   as a LOWER BOUND for exactly this. A new tool falling outside the recognizer is what "lower bound"
   predicts, so this is a confirmed instance of a declared limitation rather than a new defect.
   Leaving it unfixed risks neither a build that fails to serve maximum-precision inference nor code
   becoming incomparable against a correct specification.
2. **A stale, empty `.git/index.lock` was found mid-batch** (2026-08-21). *Reason:* an environment
   artifact of a long tool run, not a fact about the record or the analysis. Its cause was established
   before it was touched — zero bytes, no `git` process running — and removing it discarded nothing.
   Recorded as an incident in §8 rather than carried as an issue.

---

## 8. Declared departures

1. **The dispatch's Task 0 step 2 names `git diff --stat -- <path>` with no commit.** The armed
   shell-read guard denies that form, because a working-tree diff is not a content-addressed object
   query (D-253). The explicit-hash form the dispatch itself prescribes in A1 was used instead. The
   measurement is unchanged; only the spelling is.
2. **Two files the dispatch's committed-path lists do not name were edited:**
   `tools/audit/gen_guard_state.py` gained an authored invocation for the new generator, and
   `tools/audit/gen_guard_classification.py` an authored verdict for it. **This is forced by the act
   the dispatch orders:** a `*.py` under `tools/audit/` carrying a `--check` becomes a DERIVED
   candidate of the guard registry, and a derived candidate with no authored invocation is that
   registry's own STOP. Leaving it unregistered would have left the guard set stopping for a cause the
   dispatch did not declare. It is maintenance of an authored input, not a mechanism change.
3. **Two derived artifacts the dispatch does not name were regenerated:**
   `tools/audit/epoch_write_path.json` and `tools/audit/recognizer_establishment_sort.json`. Both went
   red between the start-state run and the Task-1 run. **The cause was ESTABLISHED at the object before
   either was touched** (D-669): each derives its population from *every* `*.py` under `tools/`, and
   the only difference between the two runs is the one such file this batch added. The measured diffs
   confirm it — the walked-tools count rises by one and the new tool appears in the walked population;
   **no member entered or left either classification and no verdict moved.**
4. **A stale, empty `.git/index.lock` was removed.** No `git` process was running and the file was
   zero bytes, both checked before the removal; it discarded nothing.
5. **The full guard set was run three times, not once per task.** It ran before the first edit, again
   for Task 1, and again for Task 2. It was not re-run between the Task-1 clearing acts and the Task-1
   commit — the Task-2 run covers that tree and returned one failing check and zero STOPs. The
   end-state run is the eighth commit's subject.
6. **Task 3 is stopped at a recorded boundary**, as §4 states.

---

## 9. The registered expectations, graded

| | verdict | why |
|---|---|---|
| **E0** | **MET** | Exactly the eighteen named paths; two modifications matching A1's shape and step 2's bounded regeneration; every other path an addition; no staging override; the membership check passing at the resulting tree; `origin/master` at the Task 0 commit. |
| **E1** | **MET** | Every naming enumerated and graded with its deciding clause quoted from `CLAUDE.md`; the seed reconciled both ways with its miss rate published; the member list published whole with both declared properties per member and every UNDECLARED stated as such; `--check` passing at the commit; `ARCHITECTURE.md` and every member byte-unchanged. |
| **E2** | **MET** | The widened population published whole with both-ways reconciliation; counts per document and per stratum derived; the coverage gap published; the inherited caveat carried verbatim; every existing field byte-identical; `--check` passing. |
| **E3** | **MET FOR THE MEMBERS READ, AND THE REMAINDER IS DECLARED** | Every NEW member carries exactly one verdict in the inherited vocabulary or the declared `NOT YET READ`; the existing sixty-eight are byte-identical by published digest and by a zero-deletion diff; the per-document distribution is published by the generator; the failure signal is evaluated at the artifact and stated either way; the stop is recorded in the standing form. **It is not met for the unread remainder, and that is the stop, not a shortfall.** |
| **E4** | **NOT YET ASSERTABLE HERE — BY DESIGN** | The end-state run is taken after the commit carrying this close exists. Its values land in ONE FURTHER commit. **No row, cell or sentence asserting the end state is written into the close commit.** |

---

## 10. The plan's tell, in one sentence

**Did this batch produce anything other than what the plan's §4 declares — the widened generator, the
document-set generator, the artifacts and the report?** Yes, and it is named: two edits to the guard
registry and two regenerated guard artifacts, each forced by the registry's own STOP on a tool this
batch was ordered to create, and each declared in §8 rather than left for a reader to find.

---

## 11. The standing self-check (D-434) over this batch's own work

1. **The guiding principles.** #18 — step zero exists to check a load-bearing premise, and it does,
   without carrying load on it. #19 — the candidate generator's unestablished status is carried
   verbatim and nothing here claims to establish it; the new derivation publishes its own miss rate
   rather than claiming completeness. #12 — nothing deleted; the existing verdicts and fields are
   byte-unchanged and MEASURED so; the moved `STATUS.md` entries are byte-faithful in both
   directions. #6 — one population selection, one screen method, the existing sixty-eight not
   re-graded, the prefix adjustment imported rather than restated. #17(f)/D-431 — no count
   transcribed; every figure is an artifact and a field, or a direction with its artifact named.
   #24 — no comparison between measured quantities is asserted anywhere above. **Conforms.**
2. **The conventions.** American English. No self-invented labels: the new field and tool names
   follow the existing `gen_*` / `the_*` shapes, and the one class this batch adds to a vocabulary is
   named in plain words and **declared as this tool's own** rather than presented as the bar's.
   Music-theory words in their musical sense only — *score* is never used numerically (the numerical
   sense appears only as *content score* inside quoted register text), *measurement tool* and never
   the reserved word, *measure* only as the verb or as *measurement*, *key* only as tonality except
   in the compound *map key*-free prose above, *register* only as *the decisions register* / *the
   open-items register* in full.
3. **The figures-and-premises rule.** Every quantity is named as an artifact and a field. Every
   premise is cited to the primary source it can be checked at — the delegation-form rule quoted
   from `CLAUDE.md` at run time rather than from the dispatch, the screen's method from the tool's
   own docstring, the candidate enumeration's commit population from its own artifact.
4. **The file-tools rule.** Every read of working-tree content went through Read/Grep/Glob. The only
   shell reads of repository content were git OBJECT queries by explicit hash, and every tool output
   was written to an absolute scratchpad path outside the repository and read back from there. **The
   armed guard denied one command and was obeyed rather than worked around** — §8, departure 1.
5. **Uncertainty on any comparison.** No difference between two measured quantities is asserted. The
   one comparative statement — that `UNDETERMINED` is a minority on the members read so far — is
   stated as a direction over a named read share and explicitly not as a verdict.
6. **Re-read from disk before reporting.** Every generator's `--check` was run after its final edit
   and re-derives byte-identically; the diffs of the two artifacts whose byte-identity is claimed
   were read, not assumed.

---

*Provenance: CC, 2026-08-21, executing `cc_instruction_successor_plan_landing_and_step_zero.md`
under Rulings 6, 7, 8 and 9 of `cowork_rulings_2026_08_21_successor_plan_sitting.md`. The
reserved-word conventions and the vocabulary rule of 2026-08-17 bind every line of this report —
TOWARDS the ultimate objective and TOWARDS the guiding principles.*
