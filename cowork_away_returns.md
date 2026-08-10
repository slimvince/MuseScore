# The away-batch RETURNS file — what needs the user, what was held, what each task did

> **STATUS: LIVE RETURNS FILE, created 2026-08-08 (CC, Task 0 of
> `cc_instruction_away_execution.md`).** This is the user's first read on return and Cowork's
> verification index. It is appended to per task and never rewritten.
>
> **★ HOW TO READ IT.** §1 is what needs a ruling. §2 is what was SURFACED — findings bearing on
> the analysis, its inputs, or a measurement tool a measurement depends on (D-641, #13), and
> establishment obligations (#19). §3 is the per-task log. §4 is the start state the batch began
> from, recorded before any act.
>
> **★ COWORK MAY APPEND HERE BETWEEN CC SESSIONS.** An appended entry whose heading carries
> **STOP** halts the batch at that point; the remaining tasks are not started, and the halt is
> recorded here and in `STATUS.md`. An entry without STOP is context, not instruction. CC reads
> this file in full before each task.
>
> **Nothing in this file authorizes a fix to the analysis, a design, or an inference change.**

---

## 1. What needs the user

### 1.1 The file named `phase1q_reclassification.json` holds neither phase 1q nor the present — what should happen to it? (Task 0)

**The fact, measured rather than assumed.** The establishment record of 2026-08-04 froze
`tools/audit/decisions/phase1q_reclassification.json` and its snapshot as byte-identical. **They
are not identical at HEAD**, and it is not the snapshot that moved — the snapshot still hashes to
its established value, and the classifier's own guard now re-checks that on every run. What moved
is the live file, which carries a different content at each of several recent commits: the applying
run has been performed by more than one wave since the snapshot was taken, rewriting that file each
time. **The measurement is the generated artifact
`tools/audit/decisions/phase1q_record_divergence.json`** — taken at named commits, from git objects
by explicit hash — and **no value from it is transcribed here** (**D-431**).

**What this means, stated plainly.** The record of what the phase-1q pass found survives **only
because the snapshot was taken**. The [[OI-301]] hazard `OPEN_ITEMS.md` OI-305 warned about was
realized and absorbed by the snapshot rather than avoided — and the rows that describe the applying
run as *held un-run* describe the LAST wave rather than the month.

**What was done.** Ruling 1 is applied as ruled: the live derived view moves to
`home_classification.json`, the classifier never writes the phase-1q file again, and the freeze is
enforced by a STOP on the snapshot's hash rather than promised in prose.

**What is left, and why it is the user's.** The file's NAME now says phase 1q and its CONTENT is a
later regeneration. Restoring it from the snapshot, renaming it for what it holds, or removing it
are three defensible acts and all three overwrite or delete a committed generated artifact. That is
a filing decision, which `CLAUDE.md`'s own non-gating line calls apparatus and which the record
reserves to the user. **Nothing depends on it:** the phase-1q record is at the snapshot, the live
view is at the new file, and both are guarded.

### 1.2 Should `OPEN_ITEMS.md` OI-319 be flipped? (Task 0)

The dispatch orders OI-319's remaining scope REPORTED, not its status moved, and that is what was
done. Reported for the user's decision: **the mechanism that row describes is discharged** — the
applying run has run, every `home_section` field is written, and no later wave can widen the stale
report by that cause. What remains attached to the row is a different subject its own 2026-08-04
entry records rather than rows (`gen_guard_classification.py` has a re-derivation mode no guard
list runs). Leaving the row open with its subject discharged is the OI-283 shape — a finding never
marked discharged — which is why it is put here rather than left silent.

### 1.3 `CLAUDE.md` now understates what the shell-read guard watches — a doc-sync correction owed at a surface this batch may not edit (Task 1)

`CLAUDE.md`'s D-253 conventions carry a 2026-08-08 clause stating, of the PowerShell reading family
and of a `python -c "open(...)"` in the Cowork sandbox, that **"No guard watches either surface"**.
Half of that was already made false by the 2026-08-07/08 dialect widening; **the other half is made
false by Task 1**, which brings interpreter code — `python -c`, `perl -e`, and heredoc bodies fed to
an interpreter — inside the guard, to the stated ceiling.

**What is still true and must survive any correction**, because it is the clause's actual point: a
guard armed as a hook in THIS project directory says nothing about the Cowork sandbox, and its
silence on an unwatched execution surface is not compliance (#19). The correction is therefore not
"a guard now watches it" but a narrowing — the surfaces are watched *where the hook runs*, and the
sandbox is not that place.

**HELD** because `CLAUDE.md` is in this batch's edit authority for **homing acts** only (D-645), and
a doc-sync correction is not a homing act. Stated here so it is one edit for whoever is authorized,
and so the staleness is on the record rather than merely inherited.

---

## 2. Surfaced findings (D-641, #13, #19)

### 2.1 `gen_home_classification.py` has not reached its own finding since 2026-08-07 — so two rows' quoted counts, and one row's corroborating run, describe an older tree (Task 0)

**What was observed.** The first attempt to run the applying pass stopped with *"authored judgment
for a document that is nobody's home: ['docs/unified_analysis_pipeline.md']"* — a STOP that fires
**before any entry is classified**. The committed `tools/audit/guard_state.json` records that same
STOP as this check's entire captured output, so it has been firing since the 2026-08-07
owner-rulings wave re-homed that document's last four entries and retired three other emptied
documents but not this one.

**What follows.** (a) The stale-field counts quoted in OI-305 and OI-319 describe runs older than
2026-08-07. (b) **OI-350's statement that the same check re-derives the three route-(i) documents'
eleven entries as `contract-home`, by document and by identity, cannot have come from a clean run
at the committed tree.** The mechanism OI-350 identifies is right and the applying run has now
confirmed the movement it predicted — what is withdrawn is the claim that a clean check had already
shown it. Both rows carry the correction.

**What was done about it.** The retirement was completed — the authored judgment moved whole into
the register data's own retired block, the same act with the same reason as the three retirement
records already there (#12) — and the finding is recorded rather than smoothed over.

### 2.2 A guard failed once at the batch's start and does not reproduce — recorded, not explained (Task 0)

`tools/audit/shell_read_guard.py --establish --check` returned non-zero inside the batch's opening
full guard run, at a position reached in the first seconds, **before this session had edited any
file**. The committed `guard_state.json` does not carry it among its failing tools. Re-run in
isolation it has passed on **every** attempt since, and an independent in-memory re-derivation of
the same artifact produced **no** difference against the committed one. The tool reads one file and
calls no subprocess, uses no clock and no randomness, so a content-dependent cause is not visible.

**Why it is surfaced rather than filed as noise.** It is the audit's own guard apparatus, it is
Task 1's subject, and a published deny rate that cannot be reproduced on demand is not established
(#19). **It is not asserted to be a defect** — a single non-reproducing exit against a run of clean
ones establishes nothing except that it happened. **It passed in this task's own closing full guard
run**, and it is re-tested at every later one, with the result recorded here.

### 2.3 The batch's opening guard run overlapped this session's own edits, and one row of it is therefore not evidence (Task 0)

The opening full guard run was launched before any edit and completed after five. Its rows up to
and including the slowest guard predate every edit; **`gen_home_classification.py --check`'s row
does not**, and it is discarded as evidence rather than reported as a reading. The start state of
record in §4 is therefore taken from the COMMITTED `guard_state.json`, not from that run. Recorded
because a contaminated baseline reported as a clean one is the failure this project's own
establishment rules exist against.

---

## 3. Per-task log

### Task 0 — COMPLETE. OI-305 and OI-350 resolved; OI-319's remaining scope reported

**What was done, in order.**

1. The batch's start state was taken (§4).
2. The ruled mechanism change (D-436, Ruling 1) was written into
   `tools/audit/decisions/gen_home_classification.py`: the phase-1q artifact is declared HISTORICAL
   and never written again; the live derived view moves to `home_classification.json`; a fourth
   frozen class epoch is added on the same construction as the third, so no entry's class between
   the phase-1r pass and this one is overwritten (#12); and the freeze is enforced by a STOP on the
   established snapshot's hash (#19).
3. The pre-apply register data was snapshotted into the repository (the O-12 pattern), and the
   field-diff tool `gen_apply_field_diff.py` was written to discharge **A1**. A second measurement
   tool, `gen_phase1q_record_divergence.py`, was written when the freeze's target turned out not to
   be the file the ruling's premise named (§1.1) — so the finding enters the record as a generated
   artifact rather than as prose (D-431). Neither carries a re-derivation path, both being
   point-in-time records under the 2026-08-04 ruling R4, which is also what keeps them out of the
   derived guard-candidate population instead of sitting there unclassified.
4. A missed retirement blocking the run was completed (§2.1).
5. The applying run ran. **A1 HOLDS** — no field outside the classifier's two intended writes
   moved, and the single top-level movement is the declared retirement of step 4, authored with its
   account so an unaccounted movement would still halt the batch.
6. **A2 HOLDS** — `--check` is green, and all six blocked generators run. Three of them first
   STOPPED on **D-472**'s authored route, which the same 2026-08-08 wave had homed out of item 1;
   the act was recorded in a fourth ruling table rather than the route being deleted, with the
   superseded hold preserved (#12).
7. The register and everything downstream of it were regenerated, to a fixed point.
8. OI-305 and OI-350 flipped with provenance; OI-319's remaining scope reported on its row; dated
   entries appended to all three detail files.

**Assumptions:** A1 discharged by measurement (`tools/audit/decisions/apply_field_diff.json`); A2
discharged by running the six.

**Guards at the task boundary.** The full set was re-run and the classification re-run after it,
which is the order its own STOP requires. **Cleared by this task:** the home classification, the
outstanding-delegation view, the item-1 route table, the re-home blocker, the supersession
application, the completion inventory, the finish line, the non-gating apparatus rows, the
decisions register — and the shell-read guard's establishment, which passed (§2.2). **Still
failing, and each is a standing failure this task did not touch:** the `CLAUDE.md` rule triage, the
delegation bar, the legacy-mark verification, and the live-prohibition pointers. Every verdict is
at `tools/audit/guard_state.json` → `summary` and none is restated here (**D-431**). **★ THE
DELEGATION BAR'S FAILURE IS THE SAME SHAPE AS THE ONE THIS TASK FIXED, one construct out:** it
STOPS on a list of documents that are nobody's home any more, accumulated by every re-homing wave.
It is not repaired here — its table is generator source rather than register data, and pruning it
is not among Task 0's acts.

**Holds:** the filing decision at §1.1; OI-319's status at §1.2; and two more, both outside this
batch's edit authority and both stated so they are one edit for whoever is authorized.

1. **A pointer this task made false, and did not correct.** `gen_phase1p_delegation_bar.py`'s
   artifact prose says *"the register's PRESENT classes are the post-apply ones and are at
   `tools/audit/decisions/phase1q_reclassification.json`"*, and names the same file again for its
   `by_document` and `entries` blocks. After the epoch treatment the present classes are at
   `home_classification.json`. The correction is to re-aim both namings at that file. It is HELD
   because that generator is neither the register data nor the guard tooling nor the classifier —
   the three surfaces the dispatch's edit-authority list admits — and its list ends *"Anything
   else: hold."*
2. **Two untracked files were deliberately NOT staged**, being Cowork's rather than this batch's:
   `cowork_instruction_return_session.md` and `cowork_scratch_2026_08_08/`. They remain untracked;
   naming them here is so their absence from the commit is a choice on the record rather than an
   oversight.

**Committed and pushed** as `82ebfd68d9` to `origin` (the user's fork `slimvince/MuseScore`);
`upstream` was not touched and remains push-disabled. The commit also carries the accumulated,
uncommitted document-routes wave — the two cannot be split, because the applying run re-serialized
register data that wave had already changed — and the commit message says so.

**No value is restated here (D-431)** — every quantity lives in the generated artifacts named
above.

**Freeze respected:** no `src/` change, no golden, no corpus, no `tools/robust_stop/` movement, no
behaviour change to the analysis, no fix to inference, no design.

### Task 1 — COMPLETE. The guard family built corpus-first; OI-300, OI-348 and OI-351 all resolve

**What was done, in order, and the order is the ruling's.**

1. **The corpus went in first**, before one line of the mechanism moved: OI-351's observed command
   and its path-form variants, the POSIX and `pwsh` wrapper spellings, the interpreter forms
   including the heredoc one, the hashless `git diff` forms, and — on the other side — the same
   spellings aimed OUTSIDE the tree as controls, the wrapper controls including
   `BUILD_AND_TEST.md`'s own mandated `Start-Process` invocation, and the hash-bearing git forms.
2. **The blindness was measured at the unwidened guard**, with the corpus already in place. It has
   the same shape as the dialect widening's: almost every new forbidden row admitted, not one new
   sanctioned row denied. The guard was not wrong about this family — it could not see it.
3. **The five clauses were built**, and only then were both rates re-measured on the same extended
   corpus. **The revert condition is not met — false denials FALL**, and every one that remains is
   accepted by the ruling's own clause 4.
4. **Assumption A5 discharged by measurement.** Every row the corpus carried before this act was
   decided both ways; every verdict that moved is named in the artifact, and every one is a shape
   the design names — false denials removed on the heredoc and redirection shapes, misses caught on
   the wrapper and interpreter shapes. No verdict moved anywhere else.

**★ OI-351'S CAUSE IS ESTABLISHED, AND IT IS WIDER THAN THE ROW SUPPOSED.** The row named two
candidates and asserted neither. **The first is confirmed, in a form it did not suppose: the DRIVE
LETTER'S CASE.** The guard compared a path against the repository root with a case-sensitive string
comparison on a platform whose paths are case-insensitive, so **every** repository path written with
a lowercase drive letter read as outside the tree — in every utility and both dialects, not only in
`ls`. The corpus now carries `cat` and `grep` in that spelling and both were admitted before the
fix. **The second candidate — a gap between the live hook and the decision function — is refuted by
observation**: the two agree on both live decisions the record holds, and **no new forbidden command
was issued to test it**, because performing the violation in order to measure the guard is not a
measurement anyone may take.

**★ THE NEW GUARD DENIED THIS SESSION'S OWN COMMAND WITHIN MINUTES OF BEING BUILT, AND THAT IS
REPORTED AS A DETECTION RATHER THAN AN INCONVENIENCE.** A `python - <<'PY'` heredoc was reached for
to do a bulk rename inside the guard's own source; the interpreter-heredoc clause denied it, naming
the repository path in the code. It is precisely OI-348's second shape and precisely the founding
instance's own form. **It was not worked around** — the rename was redone through the file tools.

**Two of this session's own new reserved-word collisions were caught by the standing self-check and
corrected before the commit**: the bare non-musical *part*, throughout the new text and in an
artifact field name, and the bare *rest* as a parameter name — **the same collision the previous
wave's self-check caught in its own new selection function**, reintroduced by matching the adjacent
code's idiom. That it recurred one wave later is worth the user's attention: matching the
surrounding style is exactly how this rule gets broken.

**One authored input was maintained rather than left to rot**, the same class of act as Task 0's
missed retirement and caught the same way. Closing OI-300 stopped six generators — the non-gating
apparatus declaration held a live verdict for a row the index no longer carries open, which is that
tool's own STOP working. The verdict was moved WHOLE into its retired table with the reason it
closed (#12), never deleted; and its own ground held to the end, since what discharged the row was
the establishment run it named.

**Holds:** §1.3, the `CLAUDE.md` doc-sync correction, which is outside this batch's edit authority.
**Surfacings:** none new bearing on the analysis — this task's whole subject is the audit's own
apparatus.

**Freeze respected:** no `src/` change, no golden, no corpus of scores, no `tools/robust_stop/`
movement, no behaviour change to the analysis, no fix to inference, no design. The one mechanism
change is the ruled one.

**No value is restated here (D-431)** — every rate, count and identity lives in
`tools/audit/shell_read_guard_establishment.json`.

### Task 2 — COMPLETE. Nine of the eleven homed, plus D-601; three held, each with the reason and the candidate named

**Nine entries left the archives for the specification that owns them, and the archives are
untouched (#12).** Four chord-scoring dead ends into `docs/scoring_model.md` §8 — which three of
them named, in their own provenance, as the standing home for scoring dead ends that *"does not
mention"* them, checked and not assumed; that gap is what closed. Two key-layer dead ends and one
search dead end into the `ARCHITECTURE.md` sections that already NAMED them in a *"Tried and
closed"* line without saying what they were, so a reader met an identifier and could not learn the
rule. And the MuseScore chord-symbol parser patch into `CLAUDE.md`'s local-patches section beside
its own distribution disposition.

**D-601 is homed under Ruling 2's one licensed edit**, into the confidence contract's frame table
at the `conversion` element — the exact place two scales are made comparable. **The hold was a
licence and not a judgment, and nothing about WHERE was re-decided**: the owner was already
determinate and recorded; what changed is that the surface became writable. The edit is that one
section and nothing else in the file.

**★ WHAT RODE ALONG RATHER THAN BEING DROPPED, because a prohibition carried without it reads wider
than it was measured to be.** Each homing carried the parts that qualify it: a shelving's stated
RE-OPEN CONDITION and the note that the joint estimator meets its concern by a different design; a
falsification's SCOPE (measured on one corpus, others unmeasured) and its statement of what the
remaining errors DO need; the structural second reason that a confidence field is re-ranked without
being recomputed; and, for the search dead end, a pointer to the later re-grounding — *"search is
about zero"* was measured over a fixed narrow evidence surface — without which a reader could take
the prohibition for a bar on the joint estimator's own ground. **One homed wording deliberately
narrows its former text:** the inversion dead end now says LOCAL in terms, because its old first
sentence asserted that the then-current baseline was the correct production one, and that baseline
has been re-based twice since — carrying it into a live specification would have written a stale
claim onto the compliance surface. **No measured value was carried into any specification (D-431):**
every count, ratio, percentage and commit identifier stays in the record that measured it, and each
homing says so.

**Three are HELD, and each is held because the act it needs is not a filing act:**

- **D-286** (whole-score interactive analysis shelved) — **three sections have a claim and none
  settles it**: the region-analysis section states the extent question in its own opening, the
  analyze-at-tick path table is what the bounded-window cache belongs to, and `CLAUDE.md` names the
  effort-control section as where the analysis-extent question sits. A second and stronger reason:
  the record says a later build specified whole-score interactive analysis **without meeting this
  shelving**, so writing it into a live specification would either state a rule the implementation
  contradicts or require a conformance judgment — which is about the analysis, not about filing.
- **D-289** (the meta-principle that precision lives in the evidence and the labelling, not the
  search) — its own provenance calls it an earlier, independently-derived statement of a decision
  that sits in the NO-HOME class precisely because re-homing it would duplicate rules its
  successors already state (#6). Whether what survives is a doctrine needing a home or live content
  already carried elsewhere is a **supersession** ruling. The candidate home is named so it is one
  act to settle.
- **D-291** (the tonicization labeller left unwired, and the metric not changed to credit it) —
  **it is two decisions with two owners**: a build decision belonging to a layer, and a measurement
  convention belonging to gate block (A). **And the second half looks already homed** — gate block
  (A) carries a grading convention of the SAME DATE stating the same masking argument in the same
  words. Whether that is one decision recorded twice is the user's to settle.

**One authored input was maintained**, the third instance of that shape in this batch: homing D-601
emptied its document, and the classifier STOPPED until the judgment was moved whole into its retired
block (#12) — which the 2026-08-08 route wave's own record anticipated in terms, having said that
document was not retired *because* D-601 was held.

**A standing guard failure cleared as a consequence rather than by repair:** the live-prohibition
pointer check now passes, because the entries it tracks now point at sections that state their rules
rather than at a tracking surface. **And one guard went red mid-task and was measured rather than
assumed:** the phase-3 gate partition records LOCATED line anchors for quotes in `CLAUDE.md`, and
this task's insertion there shifted them. Its verdicts are authored and its located lines derived,
so regenerating it is completing an edit and not repairing a finding — and the anchor drift it
reports was already in the committed artifact before this task touched anything.

**Holds:** the three above. **Surfacings:** none new bearing on the analysis. **Freeze respected:**
no `src/` change, no golden, no corpus of scores, no `tools/robust_stop/` movement, no behaviour
change to the analysis, no fix to inference, no design. **No value is restated here (D-431).**

### ★ WHERE THE BATCH STOOD WHEN THIS SESSION ENDED

**Tasks 0, 1 and 2 are COMPLETE, committed and pushed** — three commits, each its own task
boundary, each with its guard run, its enumeration and its `STATUS.md` pointer entry. **Tasks 3
through 8 are NOT STARTED.** That is a capacity stop at a clean task boundary, not a halt on a
finding: no STOP note was written, no analysis-bearing surface halted the batch, and nothing is
left half-edited — the working tree at session end carries no uncommitted work of this batch's own.

**What a continuing session should know before starting Task 3.** Its population is the 44 register
entries the completion inventory lists under `entries_with_no_rationale_at_all`, and **the shape of
the owed act is narrower than it looks**: the register already DISPLAYS *"derivation not recorded"*
for all 44, because the renderer substitutes that phrase for an empty `rationale` field — so the
surface currently asserts an established gap for entries where **no search was ever performed**.
That is the defect Task 3 closes, and it closes per entry by SEARCHING and then recording either the
defense the record holds or the established gap.

**Eight of the 44 were searched during this session's reading** — read-only, with nothing written,
because the searches were done while a guard run held the tree. Recorded here so the work is not
repeated: **D-004, D-015, D-059 and D-114 already carry the completed search in their own provenance
or home text** (each states in terms that the record holds no derivation, and D-059 names the only
gloss that exists); **D-058** likewise, with a stated pragmatic ground but no derivation; and **two
of the eight turn out to HAVE a defense the empty field misrepresents** — **D-052**, whose home text
states the reason as a consequence (*"so no signature/partial-correction logic is duplicated"*,
which is #6), and **D-003**, whose home states the constraint that forced it (*"presets are
presentation concerns"*). **D-019** was searched and the record holds no reason — what it holds
instead is a recorded CONFLICT with the confidence contract. **None of these was written into the
register**: recording them is Task 3's act and Task 3 was not opened.

**The three failing guards at session end are the standing set** — the `CLAUDE.md` rule triage, the
delegation bar, and the legacy-mark verification. Every verdict is at
`tools/audit/guard_state.json` → `summary` (D-431). **The delegation bar's failure is worth a
continuing session's attention:** it is the same shape Task 0 fixed one construct out — it STOPS on
a long list of documents that are nobody's home any more, accumulated by every re-homing wave, and
this batch's own homings will have added to it.

---

# ═══ THE RETURN CONTINUATION (dispatch `cc_instruction_return_continuation.md`, 2026-08-09) ═══

> The away batch's Tasks 3–8 continue here, after the ten rulings of 2026-08-09
> (`cowork_rulings_2026_08_09_return.md`) were applied. The sections above are the away batch's
> and are not rewritten. New holds are appended to §1, new surfacings to §2, and each task's log
> to §3, in the same shapes.

## 1 (continued). What needs the user

### 1.4 The ten rulings of 2026-08-09 are not IN the decisions register, and neither are the four of 2026-08-08 — is registering them this batch's act? (Tasks 0/1)

**The fact.** `cowork_rulings_2026_08_09_return.md`'s own banner says it is an *"interim carrier
until the applying dispatch records them (D-230)"*, and **D-230**'s clause (c) reads *"a new
ratification, shelving or falsification gets its register entry (data + regenerated files) IN the
commit that records it"*. The identical banner sentence stands on
`cowork_rulings_2026_08_08_pre_away.md`, and **no register entry exists for any of those three
rulings or for the guard-family ruling of the same date** — the register's highest identifier is
unchanged since 2026-08-04, checked at the register data.

**What this batch DID do, so nothing is lost meanwhile.** Every ruling applied is recorded in the
provenance of the act it licensed — on the open-items rows, in the register data's own fields, in
the generator source, and in this file — each naming the ruling, its date and its carrier
document. What is missing is the register ENTRY, not the record of the ruling.

**Why it is put here rather than taken.** A process ruling's home, in every comparable entry the
register holds, is a section of `cowork_audit_protocol.md` — and that file is not in this batch's
edit-authority list, whose last line reads *"Anything else: hold."* Registering fourteen rulings
would also mean deciding, per ruling, whether an act (a removal, a licence, a probe's timing) is a
DECISION the register carries at all, or the exercise of one it already holds — which is a
judgment about register content this dispatch does not settle.

**Not urgent, and stated so it is not read as urgent:** no ruling's content is at risk, and every
one is on disk in a ratified record. What is at risk is the register's claim to be the ONE place a
session learns what was decided.

### 1.5 `gen_home_classification.py`'s docstring and one dead constant now name a file that does not exist (Task 0)

Ruling 1's removal was performed, and Ruling 1 also says the removal is *"recorded where the file
was named"*. It is — at the register data, at `OPEN_ITEMS.md` OI-291/OI-293/OI-295/OI-296/OI-305,
and, by Ruling 4(a), in the delegation-bar generator's artifact prose.

**One naming is NOT corrected, and it is the classifier's own.**
`tools/audit/decisions/gen_home_classification.py` carries `FROZEN`, a module constant naming the
removed path, and a docstring paragraph closing *"Whether the stale file is restored from the
snapshot, renamed for what it holds, or removed is a FILING DECISION about a committed artifact
and is the user's, not this tool's — surfaced in `cowork_away_returns.md` rather than taken."*
That decision has now been taken, so the paragraph is stale by this batch's own act.

**Nothing breaks.** `FROZEN` is read nowhere — the freeze is enforced against the SNAPSHOT, whose
hash the run checks — so the removal moves no behaviour, and the classifier's re-derivation was
run after the removal and is green.

**HELD** because that generator is not in this batch's edit-authority list: Ruling 4 names the
delegation-bar generator and only it, and Ruling 1's authority is *"the removal"*. Stated here so
it is one edit for whoever is authorized — strike the dead constant, and replace the filing
paragraph with the D-644 shape already written at the register data's
`section_home_criterion.scope_of_application`.

*(A second, smaller one rides with it: `gen_phase1q_record_divergence.py` READS the removed file,
so re-running it would now fail. It is a point-in-time record whose artifact is committed and
whose measurement is complete, which is the same class the guard-state classification puts the
snapshot establishment's first-run path in — but it is named here rather than left to be
discovered.)*

### 1.6 STOP — Ruling 7's own condition is NOT met: D-291's measurement half and gate block (A)'s convention are not the same binding statement (Task 2)

**This is the mechanism working, not a failure.** Ruling 7 rules D-291's measurement half ONE
DECISION RECORDED TWICE, with the gate-block-(A) convention of the same date standing as its single
home — **on the condition that the two texts are the same binding statement, compared verbatim
before the act; any binding difference is a STOP.** The comparison was made at both texts and they
are not.

**What each text actually forbids.** D-291's measurement half, at its source, reads *"Crediting rule
NOT warranted (harmful — masks the 95% real error); only a DIAGNOSTIC partial-sub-split (expose the
masking) is defensible."* It forbids **amending the grading convention** so that a tonicization
label counts as agreeing with the annotator's modulated numeral. Gate block (A)'s convention reads
*"THE BINDING METRIC FOR A MODULATION DETECTOR IS MODULATION CORRECTNESS — explicitly NOT the
agreement percentage … judged on whether the key changes it commits are real ones (precision) and
whether it finds the real ones (recall) — the track rate together with the de-masked partial split
— and never on the overall agreement percentage."* It fixes **which bar a modulation-detecting
change is graded against.**

**They overlap in everything except what they bind** — same date, same source dossier, same masking
argument, and both name the de-masking diagnostic as the honesty measurement. But a session could
obey the gate-block convention, grading a new detector on precision and recall, and still amend the
crediting rule — which the D-291 half forbids, and which would corrupt the Roman-numeral column for
**every** measurement rather than for that one change. Conversely a session could leave the
comparison untouched and grade a detector on the agreement percentage, which the gate-block
convention forbids and this half does not address.

**So collapsing the two would lose the more specific and more easily violated prohibition (#12).**
The measurement half is therefore NOT recorded as one decision recorded twice, is NOT homed, and
nothing was written for it. **The build half is unaffected and landed** — Ruling 7's condition is
attached to the measurement-half clause, and the build half is ruled independently.

**What the user is being asked.** Whether the two are nonetheless meant to be one decision (in
which case the gate-block convention's wording would have to be widened to cover the crediting rule
before this half can be retired into it), or two decisions sharing a date and an argument (in which
case the measurement half needs its own home in gate block (A), beside the convention rather than
inside it). Both are one edit; neither is a session's to choose.

### 1.7 The legacy-mark verification's STOP is now diagnosed to one line, and the fix is outside this batch's authority (Task 3)

`tools/audit/decisions/gen_phase1w_legacy_verification.py` has been in the standing failing set
since before the away batch, and neither that batch nor this one caused it. **What it says, run
directly, is one line:** its assumption A1 locates a quote in `gen_decisions_register.py` at a
recorded line, the quote has moved, and it names the line the quote is at now and asks for the
citation to be re-aimed.

**It is authored-input maintenance of exactly the class Ruling 4(b) legitimised** — the same shape
as the retirement moves this batch and the away batch performed four times between them. **It is
HELD** because Ruling 4 names ONE generator and this is a different one, and the edit-authority
list ends *"Anything else: hold."* Stated here so it is one edit for whoever is authorized, and so
that a standing failure with a known one-line cause is not carried forward as though undiagnosed.

---

# ═══ THE SECOND RETURN CONTINUATION (dispatch `cc_instruction_return_continuation_2.md`, 2026-08-09) ═══

> Rulings 11–16 of `cowork_rulings_2026_08_09_second_stop.md` are applied here, and the remaining
> program continues. The sections above are earlier batches' and are not rewritten. New holds are
> appended to §1, new surfacings to §2, and each task's log to §3, in the same shapes.

### 1.8 Ruling 13 names ONE stale docstring paragraph; the same stale sentence stood TWICE in that file, and both were corrected (Task 0)

**What the ruling licensed.** Ruling 13's heading names its subject — *"the classifier's stale
self-account"* — and its body names the acts: strike the dead `FROZEN` constant, and *"replace the
stale filing-decision docstring paragraph"* with the D-644 shape already written at the register
data. §1.5 of this file quotes the paragraph it means, and that quotation identifies the MODULE
docstring.

**What was found on opening the file.** The same stale sentence stands a second time, in the
docstring of the function that performs the freeze check, in slightly different words — *"a FILING
DECISION about an artifact already committed, and it is left to the user rather than taken here
(surfaced in `cowork_away_returns.md`)"*. It was made stale by the same act, on the same day, in the
same file.

**What was done, and it is a widening of the licence's letter.** Both were corrected. The module
paragraph was replaced with the D-644 shape, transcribed from
`section_home_criterion.scope_of_application` and not re-judged. The function docstring's ★ block is
a MEASUREMENT record whose substance stays true and is why the check aims at the snapshot, so it was
not rewritten: its tense was corrected and its closing sentence now records that the filing decision
has been taken, pointing at the module docstring for the current arrangement.

**Why it is reported here rather than done silently.** The narrow reading of Ruling 13 is *one
paragraph*; the reading applied is its heading's subject, *the classifier's stale self-account*.
Leaving the second instance would have shipped a statement that is false at HEAD, in the very file
being edited because its self-account was false, which #10 does not admit. **If the narrower scope
was meant, reverting the second correction is one edit** — it is the closing sentence of
`frozen_record_intact`'s docstring and nothing else.

**★ ANSWERED 2026-08-09 — the user's Ruling 17** (`cowork_rulings_2026_08_09_third_stop.md`), recorded
here by `cc_instruction_return_continuation_3.md` Task 0. **Both corrections STAND, and the accepted
ground is stated rather than left implied: the heading-subject reading PLUS this report.** The
licence's heading named *the classifier's stale self-account* as its subject; the second instance was
that self-account, in the same file, made stale by the same act — and leaving it would have shipped a
known falsity at HEAD in the very file being corrected for falsity (#10). **A SILENT widening would
NOT have been accepted** — in the ruling's own words, *"the §1.8 report is part of what is
ratified"* — which is why the shape matters beyond this one file. **The one-edit licensing discipline's narrow-letter default is UNCHANGED for
every future licence** — this is not a precedent for reading a licence past its letter, it is a
ruling that a widening REPORTED is reviewable and a widening HIDDEN is not. *Excluded alternative,
recorded at the ruling:* reverting the second correction, which would knowingly re-insert a false
statement in order to make a process point — which the phase-1 TRUE half forbids. **Nothing is
re-edited by this answer**; the corrections already stand, and what this act adds is the ground, here
and in the classifier's own provenance.

### 1.9 OI-354's owed verdicts need an act no current licence covers, and whose act it is has to be settled (Task 0)

Ruling 14's licensed re-aim was performed and its predicted consequence was **refuted** — see §2.6.
What now blocks the legacy-mark verification is that its authored verdict table does not cover the
marked set as it stands at HEAD.

**What is owed per newly marked entry** is a reachability verdict at the code plus a
citation scan for transfer — the two axes the phase-1w pass used. **That is an establishment act
about the live system**, not the authored-input maintenance Ruling 4(b) legitimised, and not
anything Ruling 14 licensed. A session authoring them under a licence to re-aim an anchor would be
widening its own authority, and the verdicts would be written to clear a guard, which is the
weakest kind there is.

**So it is rowed and left**, at [[OI-354]], with the act named. What needs settling is whether a
later session is licensed to perform that establishment, or whether it waits — and, because the row
is an establishment obligation, it GATES either way.

**★ ANSWERED 2026-08-09 — the user's Ruling 18** (`cowork_rulings_2026_08_09_third_stop.md`), recorded
here and on [[OI-354]]'s row by `cc_instruction_return_continuation_3.md` Task 0, and PERFORMED at
that dispatch's Task 1. **A session IS licensed to perform the establishment, by the phase-1w pass's
own two-axis method and by no invented one** (#6, #16) — a reachability verdict at the code plus a
citation-transfer scan, per entry the verification's verdict table does not cover. **The condition
that answers this section's own objection — that verdicts written to clear a guard are the weakest
kind there is — is that NOTHING SELF-RATIFIES (#14): the verdicts are delivered as a
ratification-surface reading file for the user's review, they clear NO guard when they are written,
and the guard clears only when the reviewed set is applied, in a commit that cites the user's ruling
on the queue.** [[OI-289]]'s ✅ stays as it stands, being true of the population it covered; OI-354
flips when the reviewed verdicts land, and not before.

## 2 (continued). Surfaced findings

### 2.6 Ruling 14's predicted consequence is NOT met: the guard set does not empty, and what was hiding behind the drifted citation is a verification whose population has grown (Task 0)

**Ruling 14 stated its expected consequence and asked for it by derivation:** *"the standing guard
failing set empties."* The licensed re-aim was performed — the citation now resolves, and the
comment records both re-aims and the cause they share. **The set does not empty.**

**What was behind it.** `gen_phase1w_legacy_verification.py` checks its declared assumption A1
before the derivation rests on it, and raises on the first failure. Since the citation drifted,
every run stopped there — the committed `tools/audit/guard_state.json` at the batch's start records
that stop as this tool's ENTIRE captured output. With A1 resolving, the next check runs: that the
tool's authored verdict table covers the derived legacy-marked set exactly. It does not, and the
tool names the entries it holds no verdict for. Checked rather than assumed: the committed
verification artifact does not mention them.

**Why it is surfaced and not merely logged.** [[OI-289]]'s status of record is ✅ VERIFIED, and what
it verified is a POPULATION. That population has grown, so the ✅ is true of what it covered and of
no larger set — and the tool that exists to notice exactly this was mute for an unrelated reason.
That is the shape #19 is written against: trusted because unfalsified, where the falsifier was not
running. **OI-289's row now says so and the ✅ is NOT withdrawn.** Rowed at [[OI-354]]; every
identity is in the guard state's captured output and none is restated here (**D-431**).

### 2.7 The shell-read guard denies every `sed` and `awk`, wherever they are aimed — a reproducible false denial in the guard whose false-deny rate is published (Task 0)

A read of a scratchpad file **outside the repository** was denied, the reason naming `sed`'s own
range script as a repository path. **Reproduced once deliberately, on a different script and file,
before being claimed.**

**The cause, read at the tool.** Path candidates are every non-option token; only the four
pattern-taking utilities drop the first one. `sed` and `awk` take a script in that position and
carry no such correction, so a bare script resolves against the working directory — the repository
root — and denies the command before its real target is considered.

**It never ADMITS a forbidden read**; the whole failure is on the deny side. It is surfaced under
#19 because the guard's published false-deny rate is an established value measured over a corpus
that does not contain this shape. **Nothing was changed** — the decision function is a mechanism
change D-436 reserves to the user, and the guard family's own ruling fixes the order (corpus row
first, clause second). Rowed at [[OI-355]]. Nothing was worked around: the refused reads were done
with the file tools.

### 2.4 The production notation arm satisfies D-472's stabilization precondition by other means — and the specification says otherwise (Task 1)

The [[OI-349]] probe ran and the finding is **possibility 1**, with the means named: the record
arm's per-segment key is the backtracked best path of the joint decoder's global dynamic program,
whose key transitions are scored with separate stay and change branches. **The live path is not
grouping un-stabilized regions.** Full detail on OI-349's row and in its detail file; every
citation is located rather than transcribed, in the probe's own artifact (**D-431**).

**Why it is surfaced and not merely logged:** it bears on the analysis, and what it establishes is
that **D-472's own wording is wrong about the arm that ships** — its verbatim says the grouping
runs *"over the already-stabilized regions"* and its defense names the legacy Pass 4. Correcting a
register entry's verbatim at its home is its own act and is NOT performed here. **One
non-equivalence is recorded rather than smoothed over:** the legacy pass erases a one-region key
island unconditionally and the decoder only makes one expensive, so the two arms can differ.

### 2.5 Six comments in `src/` say the production record path is "default OFF" (Task 1)

Met at step 1 of the same probe and kept apart from its finding, because it answers a different
question. The configuration sets the flag's default to true and says so; six sites in four `src/`
files and one build file say the opposite. **Rowed at [[OI-353]] and left** — every site is a
`src/` file and this batch admits no `src/` change. It is [[OI-232]]'s class in the code rather
than in `ARCHITECTURE.md`, and OI-232 closed on the document half only.

## 3 (continued). Per-task log

### Tasks 0 and 1 — COMPLETE, in ONE commit, and the reason they are not two

**Why one commit.** The two tasks' acts are separable but their DIFF is not: both write rows into
`OPEN_ITEMS.md`, and splitting a file by hunk needs an interactive add, which this environment
does not have. The plan's R3 asks for a commit per task boundary; this is one boundary carrying
two tasks, said plainly rather than presented as one task.

**Task 0 — the filing, status and licence rulings.**

1. **Ruling 1 — the phase-1q artifact is REMOVED.** The pre-act check ran first: every commit the
   divergence artifact names still carries the blob, verified as git objects by explicit hash, so
   nothing became unreachable. The removal is recorded in the **D-644 shape** — state the current
   arrangement, record the removal as closed — at the register data's
   `section_home_criterion.scope_of_application`, with the two excluded alternatives and their
   reasons; and every live pointer to it now aims at `home_classification.json`, which carries
   `the_phase_1r_re_run`, `the_2026_08_08_apply` and `write_list` unchanged. Historical sentences
   that NAME the file in the past tense are left alone: they are accurate.
2. **Ruling 2 — OI-319 flips and its fragment becomes [[OI-352]]**, index row and detail file in
   this same commit. The [[OI-283]] shape ends. The row's two accuracy corrections are explicitly
   not withdrawn by the flip.
3. **Ruling 3 — the `CLAUDE.md` D-253 clause is narrowed**, in one edit and no other. What the
   guard watches, and where, is now stated with the guard-family act's own ceiling; the clause's
   #19 point — a guard's silence on an unwatched execution surface is not compliance — is kept in
   the same emphasis it had, because that is the clause's actual content. The former wording is
   preserved in place (#12).
4. **Ruling 4 — the delegation-bar generator.** (a) Both artifact-prose namings re-aimed. (b) The
   thirty-six FORM judgments for documents that are nobody's home moved WHOLE into a retired block
   with their reasons (#12), carried into the artifact as history and counted nowhere, with a STOP
   in the OTHER direction so a retired judgment cannot be resurrected without being re-read. **The
   standing failure clears by derivation:** the generator's own re-derivation and the classifier's
   both pass, which is stated as the run's result rather than asserted.
5. **Ruling 10 — OI-179**, recorded on the row and in the detail file: the PeARL contact is the
   user's, the measurement is commissioned and opens WITH phase 2, desk simulation first. Five
   things the commissioning does NOT do are written beside it, so the row is not read as further
   along than it is; the row stays OPEN and the gate does not move.

**Task 1 — the OI-349 probe (Ruling 9).** Read-only. **A5 holds at the diff**: the task's whole
change is the probe's own named artifact and its generator, plus the two rows it writes. The
finding is at §2.4 and the incidental at §2.5. The probe carries **no re-derivation mode**, by
design and stated in its own docstring: it is a point-in-time record of a reading, in the class
the 2026-08-04 ruling R4 defines, and a mode would also place it in the derived guard-candidate
population where a historical record does not belong. Every citation is nonetheless located on
each run, so re-running it is how a later reader confirms the anchors still resolve.

**Task 2 — the three held entries (Rulings 5, 6, 7). TWO landed; ONE half is a STOP.**

- **D-286 is HOMED** at `ARCHITECTURE.md` §2.16 — the section `CLAUDE.md`'s own make-it-work-first
  rule names as where the analysis-extent question sits, which is the third of the three candidates
  the 2026-08-08 hold enumerated, and the user's choice rather than this session's. **The pre-act
  check ran first and PASSED:** the register's rule (h) admits a section only if it STATES RULES,
  and §2.16 says of its own content, in its opening, that its two entries are *"requirements, not
  defect reports"* against which every later design is judged. **The form is the D-472 pattern:**
  the shelving is written in AS a shelving, the later build's contradiction is stated BESIDE it in
  a marked block, and the two questions that would need a judgment are POINTED at OI-210 and
  OI-206 rather than answered. **No conformance verdict is taken** — that was the hold's stronger
  reason, and the home text says in terms that the section does not decide which of the two is
  right.
- **D-289 is RULED SUPERSEDED** by the D-642 route, and **nothing is written into any specification
  for it** — a supersession is register business. **The ruling's condition was checked part by part
  at the successors' own homes before the status was recorded, and it HOLDS:** the not-search half
  at D-288, the not-the-key-path half at D-287 (with D-283's positive counterpart at D-001/D-096),
  the positive half at D-284 — which this entry's own provenance already calls the same insight
  independently derived, and which the user ruled superseded into D-036/D-001/D-010 on 2026-08-02 —
  and what-delivers-instead at D-472 and D-001. The excluded alternative is recorded: homing it as
  doctrine in the search block would state a rule that section already carries.
- **D-291 is SPLIT, and only the BUILD half landed.** The tonicization labeller's non-wiring is
  homed at the Layer-5 function section with its defense — that the comparison scores by root and
  quality rather than against the numeral's reference key, so the label is already partly credited
  and the comparison MASKS rather than over-penalises. **The MEASUREMENT half is a STOP back to the
  user; see §1.6.**

**Task 3 — the owed `CLAUDE.md` rule-triage entries (Ruling 8). The guard clears; the set goes to
the user's review.**

**The pre-act check ran first and PASSED.** The triage tool's own contract was read before an entry
was authored: the population is DERIVED and only the CLASS is authored; the tool is *"a PROPOSAL,
executed nowhere"*; it *"retires nothing and changes nothing"* and edits `CLAUDE.md` nowhere. No
criterion demands an author the session cannot be, so the STOP the ruling reserves did not fire —
and the tool's own file already carried the precedent, three earlier entries having been authored
by the sessions whose homing acts created them.

**Fifteen were owed, and the shape is worth more than the count.** The population is every register
entry homed in `CLAUDE.md`, so **every homing wave that writes a decision into that document adds a
member and cannot supply its own verdict** — this check then STOPS, and a tool that stops writes no
artifact. Nine of the fifteen arrived by the licensed-homing waves of 2026-08-07, five by rulings
homed into `CLAUDE.md` itself, and one by the away batch's own local-patch record.

**The set is delivered for review at `ratification_surfaces/cowork_rule_triage_entries_2026_08_09.md`**,
with each verdict and its ground. **Nothing is self-ratifying**, nothing was applied to `CLAUDE.md`,
and no rule was retired, weakened or reworded.

**★ ONE THING THE REGENERATION EXPOSED, checked at the objects rather than assumed.** None of the
fifteen is in the defect class, so this act adds nothing to it — **but the regenerated defect set is
not the committed one.** It gains **D-546**, whose classification was authored in the tool's source
before this session and was never written out, because the tool had been stopping. **So the
committed artifact has been describing a defect set one member short for as long as the check has
been failing.** Recorded on OI-292's row and in the reading file; D-546's verdict is not re-decided.

**One authored input was maintained**, the fourth instance of that shape across this batch and the
away one: creating [[OI-353]] made it a first-cut candidate of the non-gating declaration with no
authored verdict, which is that tool's own STOP working. A **GATES** verdict was authored with its
ground — D-438's line puts a correction to a statement about the analysis's build state on the
gating side, and which arm ships is the strongest form that statement has. **No non-gating verdict
was hand-added**, which is the act the record forbids; authoring a GATES verdict for a row the cut
DID reach is what the tool requires.

**Task 4 — the defense gaps. OPENED AND PARTLY DONE: EIGHT OF THE POPULATION CLOSED, THE REST NOT
STARTED. This is where the batch stops, and it stops on capacity, not on a finding.**

**What was done, and why these eight.** The away batch searched eight of the population during its
own reading and recorded the results in this file, noting that *"none of these was written into the
register: recording them is Task 3's act and Task 3 was not opened."* **Assumption A7 was
discharged first** — each of the eight was re-read at its own record rather than carried from that
summary — and then each was written into the register's `rationale` field, which is where
`CLAUDE.md`'s carry-its-defense rule puts a decision's defense or the statement of its absence.

**The distinction the eight now draw, which is the point of the task.** Before this act the
register DISPLAYED *"derivation not recorded"* for the whole population, because the renderer
substitutes that phrase for an empty field — so the surface asserted an ESTABLISHED GAP for entries
where **no search had ever been performed**. Each of the eight now says which it is:

- **two hold a defense the empty field misrepresented** — one states its reason as a CONSEQUENCE in
  its own home text (*"so no signature/partial-correction logic is duplicated"*, which is #6), the
  other states the constraint that forces it in a parenthetical (*presets are presentation
  concerns*);
- **one differs BY PART** — its state space's form is grounded in the published model class while
  the segment cap's VALUE has no recorded derivation anywhere;
- **one holds a stated pragmatic ground but no derivation**, and its mechanism has since been
  removed from the code, so the absence is a fact about the record rather than a live gap;
- **one names exactly what stands in place of a derivation** — an in-code gloss restating the two
  window values in bars, which is not a reason for them;
- **one holds no reason and a recorded CONFLICT instead**, with the ratified confidence contract;
- **two are established gaps** stated as definitions or as behaviour-plus-consequence, with no
  alternative considered.

**Nothing was invented.** Where the record holds nothing, the field now says so AND says a search
was performed — which is the difference between an established gap and an unexamined one, and the
whole defect this task exists to close.

**★ ONE MECHANICAL TRAP WAS HIT AND IS RECORDED, because the next session will meet it.** Every
register entry already carries a `rationale` key, set to `null`, as its LAST field. Adding a second
`rationale` earlier in the entry produces a duplicate JSON key whose later value wins, so the text
is silently discarded — **the first attempt did exactly that and the completion inventory's count
did not move**, which is how it was caught. It was caught by reading the derived count rather than
by trusting the edit. The fill must REPLACE the trailing `null`; a duplicate key would additionally
break the classifier's round-trip establishment.

**The remainder of the population is NOT started**, and no entry outside the eight was touched.
Every count lives in `tools/audit/phase1_completion_inventory.json` and none is restated here
(**D-431**).

**Holds:** §1.4 (the register entries for fourteen rulings), §1.5 (the classifier's own stale
naming), §1.6 (Ruling 7's condition unmet) and §1.7 (the legacy-mark verification's moved anchor).
**Surfacings:** §2.4 and §2.5.

### ★ WHERE THIS BATCH STOPPED

**Tasks 0, 1, 2 and 3 are COMPLETE. Task 4 is OPENED and PARTLY DONE. Tasks 5, 6, 7 and 8 are NOT
STARTED.** That is a capacity stop, not a halt on a finding: no STOP note was written against the
batch, no analysis-bearing surface halted it, and nothing is left half-edited — every act on disk
is complete in itself and every derived surface re-derives.

**What a continuing session should know.** Task 4's remaining population is the completion
inventory's `entries_with_no_rationale_at_all` list, derived at task start and NOT carried from
here. The act per entry is: read the entry's home text and its provenance, then write into the
trailing `rationale` field either the defense the record holds WITH its citation, or a statement
that a search was performed and the record holds none — never a defense reconstructed from memory.
The eight already done are marked by their fields opening *"SEARCHED 2026-08-09"*, so the remainder
is exactly the difference.

**Tasks 5 to 8 are untouched and their populations must be derived fresh:** the reach-verdict
derivation over the apparatus-classed documentation rows, the section-unreached and
findings-not-rules re-homes, the session-executable gating rows, and OI-346's marks.

**Phase 1's completion statement is not written, not drafted and not partially written by this
batch.**

**Freeze respected:** no `src/` change, no golden, no corpus of scores, no `tools/robust_stop/`
movement, no behaviour change to the analysis, no fix to inference, no design. **No value is
restated here (D-431).**

## 3 (continued). Per-task log — the second return continuation

### Task 0 — COMPLETE. Rulings 11, 13, 14 and 15 applied; OI-349 flips; two findings rowed, and one ruling's own prediction is refuted

**Every assumption was checked before the act it licenses, and one was refuted.**

- **A1 HOLDS.** Gate block (A) was read before Ruling 11's entry was written: it states its grading
  and measurement conventions as binding rules, which is the register's rule (h) kind half. The
  measurement half's prohibition was taken VERBATIM from D-291's own record and located at its
  source in `cowork_handoff_archive.md` rather than transcribed from the register's summary of it.
- **A2 HOLDS.** The D-644 shape was read at
  `section_home_criterion.scope_of_application` before the docstring was touched, and transcribed
  rather than re-judged.
- **A3 HOLDS IN ITS FIRST HALF AND IS REFUTED IN ITS SECOND.** The tool's own output named the line;
  the citation was re-aimed per its own numbers. **The failing set did NOT then empty** — §2.6.
- **A4 HOLDS.** The Layer-6 section's D-472 text was read whole before the correction.
- **A7 HOLDS.** Every population was derived at task start: the guard failing set from the committed
  `guard_state.json`, the moved line from the tool's own run, the probe's finding from its own
  artifact.

**What was done, in order.**

1. **Ruling 14 — the legacy-mark citation re-aimed**, from the tool's own STOP message, with the
   comment recording both re-aims and the cause they share: the register generator's preamble grew
   above the emission site, which is why two of its four quotes move and two do not.
2. **Ruling 13 — the classifier's stale self-account corrected.** The dead constant is struck, with
   the comment above it corrected too: it claimed both files were read and that a difference between
   them stopped the run, and neither half was true. The module docstring's filing paragraph is
   replaced with the D-644 shape. A second instance of the same stale sentence was found and
   corrected — §1.8, where the widening is reported rather than done silently. **No behaviour
   moves**, established by the run: the check is green.
3. **Ruling 15 — D-472's wording corrected at the Layer-6 section that owns it.** The precondition
   half no longer names one implementation: it requires that the key sequence the grouping runs over
   HAS ALREADY BEEN SMOOTHED, and states the two designs that meet it, one per arm. **The
   non-equivalence is carried visibly and stated as UNMEASURED** (#24) — island erased versus island
   made expensive, with no corpus comparison taken and neither sequence claimed better. The former
   heading wording and the former OPEN QUESTION are preserved in place (#12), and the register's
   `verbatim`, `title` and recorded defense are re-taken from the corrected home, the former defense
   preserved in the corrected one.
4. **[[OI-349]] FLIPPED RESOLVED with provenance**, index row and dated detail note. Both halves of
   what it owed are discharged — the probe was the establishment, the correction was the act the
   probe made owed.
5. **Ruling 11 — D-291's measurement half homed SIDE BY SIDE** in gate block (A), beside the
   modulation-correctness convention and not inside it, **each cross-referencing the other**, with
   the specific prohibition carried in the words it was recorded in and no already-ruled text
   reworded (#14). The excluded alternative is recorded at the entry. **One thing is deliberately
   not decided:** whether the measurement half now warrants its own register identifier is a
   question about register CONTENT, so it goes to Task 1's queue rather than being taken here.

**Two findings rowed, each with its detail file in this commit (rule (c)): [[OI-354]]** (the
verification whose population grew, §2.6) and **[[OI-355]]** (the guard's `sed`/`awk` false denial,
§2.7). Both GATE, and both by the same clause — an establishment obligation always gates.

**★ ONE FIGURE IS CARRIED INTO `CLAUDE.md` INSIDE A QUOTATION, AND IT IS FLAGGED RATHER THAN
SLIPPED IN.** Ruling 11 requires the specific prohibition to survive verbatim, and that sentence
contains a percentage. It is quoted as the source's own wording, the home says so in terms, and it
points at the dossier that holds every value of that measurement (#17f, **D-431**). The alternative
— paraphrasing the percentage out — would have broken the verbatim the ruling asked for.

**Guards.** The full set was re-run at the boundary and the classification after it, which is the
order its own STOP requires. **Cleared by this task:** the `CLAUDE.md` rule triage and the
delegation bar, both stale by line drift from this task's own insertions; the phase-3 gate
partition and ruling R1's superseded reach, the same cause; the home classification and the
decisions register, regenerated to a fixed point. **Still failing: one** — the legacy-mark
verification, **with a different cause than at the batch's start**, which is the finding at §2.6 and
not a carried-forward failure. Every verdict is at `tools/audit/guard_state.json` → `summary` and
none is restated here (**D-431**).

**A regeneration order is worth recording for the next session**, because it cost a cycle: the
register renderer reads the cluster dispositions, so regenerating the register BEFORE the
dispositions leaves it stale. The order that reaches a fixed point in one pass is classifier →
anchors → dispositions → register → the derived views.

**One authored input was maintained**, the fifth instance of that shape across this batch and the
two before it. Creating [[OI-354]] made it a first-cut candidate of the non-gating declaration with
no authored verdict, which is that tool's own STOP working. A **GATES** verdict was authored with
its ground, and the ground is not the criterion but the clause that overrides it: the first-cut
classification is RIGHT about the subject — this is the register's own verification apparatus — and
`CLAUDE.md`'s declaration states that an establishment obligation always gates whatever its subject,
naming an obligation about the open-items register itself as covered. **No non-gating verdict was
hand-added**, which is the act the record forbids; authoring a GATES verdict for a row the cut DID
reach is what the tool requires. [[OI-355]] is not a first-cut candidate and needed none.

**★ ONE INSTRUCTION COULD NOT BE PERFORMED, AND IT IS NAMED RATHER THAN QUIETLY DROPPED.** The
dispatch's edit-authority list says the first commit stages the ruling record **and this dispatch**.
The ruling record is staged. **The dispatch file is not: `cc_instruction_*.md` is matched by this
repository's `.gitignore`**, and forcing it in would override a standing repository configuration
decision, which is not a session's to take. Checked rather than assumed, and checked as git objects
by explicit hash: **neither of the two preceding dispatches is tracked at HEAD either**, so this is
the class's standing state and not something this batch changed. If the dispatches are meant to be
committed, that is one `.gitignore` decision for the user.

**The standing self-check (D-434) over this task's own diff caught one class in its own new text
and it was corrected before the commit:** the bare non-musical *figure* — the reserved-word
collision the conventions enumerate — in the new `CLAUDE.md` block, in two register fields, in two
rows and in this file. It is now *value* in each. Worth the user's attention only because it is the
third consecutive wave whose self-check has caught a reserved-word collision in its OWN new prose.

**Holds:** §1.8 (Ruling 13's second paragraph, reported for narrowing) and §1.9 (OI-354's owed
verdicts, whose act needs settling). **Surfacings:** §2.6 and §2.7.

**Freeze respected:** no `src/` change, no golden, no corpus of scores, no `tools/robust_stop/`
movement, no behaviour change to the analysis, no fix to inference, no design. **Phase 1's
completion statement is not written, not drafted and not partially written here.**

### Task 1 — COMPLETE. All twenty rulings classified and delivered for review; NO register entry written

**§1.4 is answered by Ruling 12 and discharged into a queue.** The question it put — is registering
the unregistered rulings this batch's act? — is ruled: **CC drafts the classification, the user
rules, and the entries then land in ONE commit.** The set is at
`ratification_surfaces/cowork_ruling_registration_queue_2026_08_09.md`.

**The population is twenty and it is derived from the carriers, not from any summary of them.** The
four of 2026-08-08 (three in the pre-away record, one the guard-family ruling), Rulings 1–10 of the
return record, Rulings 11–16 of this record. **Each was classified from its own text**, every
carrier read whole (D-643).

**Seven entries are proposed as DECISIONS the register should carry**, each with the reason it
binds a future session beyond the act it licensed, and each with a proposed home under rule (e).
**Twelve are proposed as EXERCISES** of decisions the register already holds — in most cases
because the ruling itself names the decision it applies. **One is put both ways**, with the ground
for each reading, because it is genuinely marginal and the user may reasonably downgrade it.

**★ THE SHAPE THE CLASSIFICATION EXPOSED, which is worth more than the tally.** The rulings that
BIND are almost never the ones that unblocked the most work. Several one-line licences moved a whole
batch and bind nothing; the rules that will govern future sessions are clauses that rode ALONGSIDE
those licences — the line between authored-input maintenance and a mechanism change, the condition
that stops two same-dated texts being merged, the requirement that an arm-reconciling correction
carry its non-equivalence visibly, the exhaustion rule for a contact route. **A register that
carried only the headline acts would carry none of them.**

**★ AND THE FILE ANSWERS ONE QUESTION IT WAS NOT ASKED, because Task 0 created it:** whether D-291's
measurement half now warrants its own register identifier. That is register CONTENT — an entry is
the register's unit and splitting one is not a filing act — so it is put in the queue rather than
taken, and D-291's own entry records that it is there.

**Nothing is self-ratifying.** No register entry is written, no identifier is assigned, no status
moves, nothing is homed and no ruling's text is touched. **The ratification-surface census was
deliberately NOT regenerated**: that tool has no verify-only mode and overwrites a committed
artifact whose counts move whenever a file is added, so running it here would fold this file into
the previous wave's uncommitted record — the OI-301 hazard, and the reason the guard list carries it
as NOT RUN with that reason stated.

**Holds:** none new. **Surfacings:** none — this task's whole subject is the register's own
bookkeeping. **Freeze respected:** no `src/` change, no golden, no corpus of scores, no
`tools/robust_stop/` movement, no behaviour change, no fix to inference, no design.

### Task 2 — the defense gaps. OPENED AND PARTLY DONE; this is where the batch stops, and it stops on capacity, not on a finding

**The population was derived fresh at task start (A7)** from
`tools/audit/phase1_completion_inventory.json` → `entries_with_no_rationale_at_all`, not carried
from any dispatch or from this file. The eight the previous continuation closed are already out of
that list by construction, since they now carry a field.

**The act performed per entry.** Read the entry's own record — verbatim, plain restatement, status
source — and then **open the home document and read the text AROUND the quoted span**, because a
defense is very often in the sentence after the decision rather than inside it. Then write into the
**trailing** `rationale` field either the defense the record holds WITH its citation, or the
statement that a search was performed and the record holds none. **Memory was not used as a source
anywhere.**

**★ THE DISTINCTION IS THE POINT, AND THIS TASK'S ENTRIES SPLIT ALMOST EVENLY.** Before the fill the
register DISPLAYED *"derivation not recorded"* for the whole population, because the renderer
substitutes that phrase for an empty field — so the surface asserted an ESTABLISHED GAP for entries
where no search had been performed. Of the entries closed here, **about half turn out to HOLD a
defense the empty field misrepresented**, and in every one of those cases the defense was in the
home text and not in the entry:

- one carries a **precedent plus a sequencing reason** — a path may analyse with less context
  provided that is STATED rather than silent, and the pre-pass that would fix it is not built
  because a later layer would discard it (#8);
- one carries a **measured** ground — the unified setting was tried and made the in-app path worse
  on a named repertoire, so the divergence is kept and documented;
- one carries the **kind of decision** it would be — flipping the live product onto the presets is a
  product decision, not a code tidy-up, so it may not happen silently;
- one carries a full **dismantling of the three reasons its subject had existed for**, plus the core
  principle those reasons were measured against;
- one carries the **structural defect it removes** — two type-only header back-edges a layering
  audit found, killed by construction rather than by convention (#7).

**And the ones that are genuine gaps are now genuine gaps, said with what stands in their place.**
Where a supersession stands in place of a defense, that is said and the successor's reason is **not**
borrowed — attributing a later design's ground to an earlier wiring step would be invention. Where
evidence that a deferral currently costs nothing stands in place of a reason for deferring, the two
are named apart. Where the obvious modern argument exists but the record never made it, the argument
is named and explicitly NOT written in, because a defense composed after the fact is what the
never-work-from-memory rule forbids.

**★ THE MECHANICAL TRAP THE PREVIOUS CONTINUATION RECORDED WAS MET AND AVOIDED, by its own remedy.**
Every entry carries a trailing `rationale: null`, so a second key added earlier is silently
discarded. Each fill REPLACED that trailing field, and **the derived count was read after every
batch** rather than the edit being trusted — it moved every time, which is A6 discharged by
measurement.

**One JSON hazard is worth recording for the next session**, because it is not the same trap and it
bit twice: where the trailing `rationale` is the entry's LAST field it carries **no comma**, and a
fill that adds one produces invalid data. Both instances were caught immediately and corrected; the
register's own regeneration would have caught either.

**The remainder is NOT started and no entry outside those closed was touched.** Every count lives in
`tools/audit/phase1_completion_inventory.json` and none is restated here (**D-431**); the remaining
population is that file's `entries_with_no_rationale_at_all` list, to be derived fresh again rather
than carried from here.

**Holds:** none new. **Surfacings:** none — the entries touched are records of decisions, and
nothing about the analysis moved. **Freeze respected:** no `src/` change, no golden, no corpus of
scores, no `tools/robust_stop/` movement, no behaviour change, no fix to inference, no design.

### ★ WHERE THIS BATCH STOPPED

**Tasks 0 and 1 are COMPLETE. Task 2 is OPENED AND PARTLY DONE. Tasks 3, 4, 5 and 6 are NOT
STARTED.** That is a capacity stop at a clean boundary, not a halt on a finding: no STOP note was
written against the batch, no analysis-bearing surface halted it, and nothing is left half-edited —
every act on disk is complete in itself, every derived surface re-derives, and the guard set is
where Task 0 left it.

**What a continuing session should know.**

1. **Task 2's remaining population is derived**, from the completion inventory's
   `entries_with_no_rationale_at_all` list at task start. The act per entry is written above; the
   two mechanical hazards are written above; **the home text must be opened**, because that is where
   the defenses in this population have consistently been.
2. **Tasks 3 to 6 are untouched and their populations must be derived fresh:** the reach-verdict
   derivation over the apparatus-classed documentation rows (D-639's test, generated, no hand
   verdicts), the section-unreached and findings-not-rules re-homes, the session-executable gating
   rows, **Ruling 16's sibling sweep and its one comment-only `src/` commit**, and OI-346's marks.
   **Ruling 16 is the only licensed `src/` touch of the knowledge arc and it is NOT taken here** —
   no `src/` file was opened for editing by this batch.
3. **Two things need the user before they can move:** §1.8 (whether Ruling 13's licence was meant
   narrowly) and §1.9 (who may author OI-354's owed verdicts). Neither blocks Tasks 3–6.
4. **The queue from Task 1 is awaiting a ruling** and no register entry may be written for any of
   the twenty rulings until it comes.

**Phase 1's completion statement is not written, not drafted and not partially written by this
batch.**

### 2.8 The Baroque partial-signature correction is legacy-only, and the production arm's handling of that notation practice is unestablished (Task 1)

**Found by the citation-transfer half of the [[OI-354]] establishment, not by looking for it.** The
transfer verdict for **D-575** is `none-found`, and the reason it is `none-found` is a live question
about the arm that ships.

Baroque scores are frequently notated with one accidental fewer than the modern practice, so the
sounding key sits one step to the sharp side of anything a signature-faithful reading could name.
The handling that detects and corrects it **lives in the legacy key resolver and nowhere else**; the
production arm does not run that resolver; and D-575's own home text says in terms that whether the
joint estimator handles the practice **at all** is not settled.

**What is deliberately NOT claimed.** Absence of the machinery is not absence of the handling: the
live arm reads the signature and declared mode as a **weak fitted soft prior** (**D-528**) rather
than as a hard constraint, so a key one step to the sharp side is reachable there with no explicit
correction. The row asserts **no defect and no regression** — it asserts that the question is
unestablished in both directions, which is the state #19 refuses to treat as established.

**And one thing substantially reduces its size, stated so it is not read as larger than it is:** the
production arm's key agreement on exactly this repertoire IS measured and published in gate block
(A), so this is not an unmeasured failure behind a green gate — any effect already sits inside a
published value. What is missing is whether a named, corpus-wide notation practice is handled on the
arm that ships, which bears on how that value should be read.

**Rowed at [[OI-357]]** with its detail file in the same commit (rule (c)); the verdict and its
ground are at `ratification_surfaces/cowork_oi354_legacy_mark_establishment_2026_08_09.md` §5.
**Nothing is proposed for it beyond the row** — no fix, no design, no inference change.

### 2.9 Five register entries quote a different rule than they are about, and both guards pass over it (Task 2)

**Found by the defense-gap method's own required act** — *open the home document and read the text
AROUND the quoted span* — which is the only way a mismatch between an entry and its quote becomes
visible at all.

In `docs/scoring_model.md` §8 the bullets stand in the same order as the identifiers **D-214 …
D-224**, and for the first six the recorded home lands inside the correct bullet. From **D-220** on
it does not, and the offset grows: D-220 quotes the `hasStructuralBass` bullet, D-221 a fragment of
the pre-sort capture bullet, D-222 the joint-scoring bullet, D-224 §9's checklist opening — and
**D-223 quotes a horizontal rule and the heading `## 9. How to add a new template safely
(checklist)`**, which is not a decision at all.

**What is established is the STATE, not the cause.** In all five the **title, the plain restatement
and the defense are correct, mutually consistent, and describe the bullet the identifier's position
predicts** — so the entries' meaning survives and it is the QUOTE and the LINE that are wrong. Five
consecutive entries entered with correct titles and correct measured defenses but wrong quotes is
not a plausible entry error.

**★ WHY NO GUARD SEES IT, which is the reason this is surfaced rather than quietly repaired.** The
register's own check verifies that every verbatim resolves at its cited home; the disposition
verifier reports zero line drift. **Both are satisfied by a corrupted pair** — once the verbatim IS
the text at the drifted line, the two agree with each other permanently. The condition is
self-sealing: the moment it happens, the machinery that exists to detect drift confirms health.

**The candidate cause is named and NOT asserted:** a verbatim RE-TAKE against an already-drifted
anchor would produce exactly this. **One tool is REFUTED as the cause and is not under suspicion** —
`reaim_home_anchors.py`, read at its own source, moves only the line part of `home`, never the
verbatim, and locates an entry by finding that entry's own quote, so it follows a quote rather than
overwriting it.

**The detection method is the finding's most useful half and is stated so it can be built: compare
each entry's verbatim against its own title and defense.** Nobody runs that check, and it is the
only one that could have caught this.

**Rowed at [[OI-358]]** with its detail file in the same commit. **Nothing is corrected** — five
verbatims and five anchors are register DATA maintenance under D-230, and the act needs a decision
the record does not carry: whether a corrupted verbatim is re-taken from the correct bullet, or the
wrong quote is preserved beside it (#12).

---

# ═══ THE THIRD RETURN CONTINUATION (dispatch `cc_instruction_return_continuation_3.md`, 2026-08-09) ═══

> Rulings 17–19 of `cowork_rulings_2026_08_09_third_stop.md` are applied here, and the remaining
> program (the second continuation's Tasks 2–6) continues. The sections above are earlier batches'
> and are not rewritten — §1.8 and §1.9 gained their dated answers in place, where the questions
> were asked. New holds are appended to §1, new surfacings to §2, and each task's log below.

## 3 (continued). Per-task log — the third return continuation

### Task 0 — COMPLETE. Rulings 17, 18 and 19 recorded at their subjects; the queue extended to twenty-three

**The start state was derived at the artifacts before any act (A5), not carried from the dispatch.**
The guard set's one failing tool is the legacy-mark verification, read at the committed
`tools/audit/guard_state.json` → `summary`; the two rows this task writes to exist and carry the
status the second continuation left them; the queue file covers twenty. No count is restated here
(**D-431**).

**Ruling 17 — recorded, and NOTHING is re-edited.** The two corrections in
`gen_home_classification.py` already stood; what this act adds is the **ground**, in the two places a
later reader meets the question. §1.8 above carries the answer where the report was made, and the
classifier's own `frozen_record_intact` docstring — the widened correction's own site — carries it as
provenance. **Both halves of the ruling are written, not just the acceptance:** that a SILENT widening
would not have been accepted, and that the one-edit licensing discipline's narrow-letter default is
**unchanged for every future licence**. That second half is the one worth the care: the ruling accepts
an act without making it a precedent, and a record that carried only the acceptance would read as the
opposite.

**Ruling 18 — recorded on [[OI-354]]'s index row and in its detail file**, with the three things it
fixes kept apart: the **licence** (a session may perform the establishment), the **method** (the
phase-1w pass's two axes, *"by that method and no invented one"* — a session meeting an
under-specified case states the gap rather than substituting), and the **review condition**, which is
what answers the row's own objection rather than overriding it. The row's objection was never that
the work is hard; it was that verdicts authored to clear a guard are the weakest establishment there
is. **The remedy is structural: the verdicts clear nothing when written.** [[OI-289]]'s ✅ is
explicitly not withdrawn, and the row **stays OPEN**.

**Ruling 19 — recorded on [[OI-355]]'s index row and in its detail file** as a disposition, with the
order it rides under stated in full — corpus rows first with their out-of-tree controls, clause
second, both rates re-measured on the same extended corpus, the revert condition governing — and with
the meantime written as a **decision rather than as neglect**: the deny-side failure is TOLERATED, on
the grounds the row itself establishes. No dispatch is written for it, as the ruling directs.

**The queue is extended to twenty-three by the same derivation that built it**, each of the three
classified from its own text with the carrier read whole (D-643). **Two are proposed as DECISIONS and
one as an EXERCISE**, and the extension confirms the shape the original twenty exposed rather than
changing it: the clauses that bind rode ALONGSIDE licences, while the ruling that unblocked a whole
family's remedy binds nothing new. **One of the two is flagged as reasonably downgradable, with the
downgrade reading given in one line** so disagreeing costs the user nothing. **No register entry is
written, no identifier assigned, no status moved** — the user has not ruled on the queue, and until
they do none of the twenty-three may be registered.

**★ THE SAME INSTRUCTION AS LAST TIME COULD NOT BE PERFORMED, AND IS NAMED RATHER THAN QUIETLY
DROPPED.** This dispatch, like both before it, orders itself staged in the first commit.
`cc_instruction_*.md` is matched by this repository's `.gitignore` — checked at that file, not
recalled — so the dispatch is not staged and forcing it in would override a standing repository
configuration decision, which is not a session's to take. The ruling record
`cowork_rulings_2026_08_09_third_stop.md` is not matched and IS staged. This is the class's standing
state, established by the previous continuation at the git objects; it is repeated here only because
the instruction repeated.

**★ THE STANDING SELF-CHECK CAUGHT A DEFECT IN THIS TASK'S OWN EDIT, AND THE DEFECT TURNED OUT TO BE
IN THE APPARATUS RATHER THAN ONLY IN THE EDIT — [[OI-356]], rowed with its detail file in this
commit (rule (c)).** The boundary guard run reported **five** derivations failing where the committed
state carried one, all naming OI-354. **Diagnosed at the tool and confirmed in both directions, not
inferred from the message:** the ONE index parser (#6) decides a row is resolved by searching its
WHOLE status cell for the resolved mark, and this task's Ruling-18 note had recorded, correctly, that
[[OI-289]]'s completed-verification status is not withdrawn — naming that status with its glyph put
the mark inside OI-354's own status cell. The row was open throughout and its words said so.
Rewriting the sentence to name the status in words, with its meaning unchanged, clears all five.

**Why it is a row and not merely a remark beside the previous continuations' two JSON traps.** Here the
tools STOPPED and named the row, which is the guard working and is why nothing was written on a wrong
reading. **But that loudness depends on the row carrying an authored apparatus verdict.** A row
without one simply leaves the open population — the open-row count, the TRUE-half cuts and the finish
line's populations move with it and nothing cross-checks it. The silent half is the defect; the loud
half is what caught this instance. **Nothing was changed in the parser** — how the index is read is a
mechanism change **D-436** reserves to the user, and there are at least three defensible remedies. The
working convention adopted meanwhile is on the row: **inside a status cell, name another row's
resolved status in words, never with the glyph.**

**Guards at the task boundary.** The full set was re-run and the classification re-run after it,
which is the order its own STOP requires; the classification re-derives. Adding OI-356 then put two
index-DERIVED views out of date — a byte-identity drift, not a STOP — and regenerating them is
**completing an edit, not repairing a finding**; the finish line follows from the same source and was
regenerated with them. **STILL FAILING: ONE — the legacy-mark verification, and it is CARRIED
DELIBERATELY.** It is Task 1's subject, and Ruling 18's own design is that the authoring session's
verdicts clear no guard: it stays red until the user has reviewed the set and the reviewed set is
applied. Every verdict is at `tools/audit/guard_state.json` → `summary` and none is restated here
(**D-431**).

**Holds:** none new. **Surfacings:** none — every subject of this task is the record's own
bookkeeping and the rulings that govern it, and [[OI-356]] is an apparatus finding, so the protocol's
own line puts it in a row rather than in §2. **Freeze respected:** no `src/` change, no golden, no
corpus of scores, no `tools/robust_stop/` movement, no behaviour change to the analysis, no fix to
inference, no design. **Phase 1's completion statement is not written, not drafted and not partially
written here.**

### Task 1 — COMPLETE. Ruling 18 executed: eleven verdicts authored and delivered for review, the guard deliberately left red

**§1.9 is answered and discharged into a reading file.** The set is at
`ratification_surfaces/cowork_oi354_legacy_mark_establishment_2026_08_09.md`.

**A1 HOLDS, and it was checked before the first verdict rather than after.** The phase-1w pass's
method is stated in its own record in full and is reusable as stated: half A is reachability at the
code with **five named senses** — because the notation arm turns on a runtime flag whose default is
true rather than on compilation, so a bare *dormant* is not an answer — each verdict citing located
evidence anchors; half B is a citation scan across `.md`/`.cpp`/`.h`/`.py`/`.txt` with **its own two
stated bounds carried across unchanged**, because they are what a `none-found` verdict is worth.
**No method gap was met, so the STOP the assumption reserves did not fire, and nothing was
substituted.** Where a case needed a judgment the pass had already faced, **the pass's own precedent
is named at the entry** — D-302 for a procedure with no code, D-215 for an obligation never
executed, D-284 and D-243 for a finding about a legacy surface, D-325 for a principle adjacent to
one already transferred.

**A2 HOLDS.** The population is eleven, derived at task start from the tool's own output and not
carried from the dispatch or from this file. Checked rather than assumed: the committed verification
artifact mentions none of them.

**★ THE VERDICTS ARE NOT UNIFORM, WHICH IS THE RESULT WORTH READING.** Had all eleven come back
*legacy, reached only off the default paths, nothing carried across*, the exercise would have
confirmed the mark and little else. Instead: **three have no code at HEAD at all** — a landing
procedure, a removal, and an obligation met by replacement rather than repair; **one is cited in a
LIVE specification as a standing do-not-retry**, so its subject is legacy while its prohibition
binds now; **one assigns work to the live design in its own text**, being a work-programme rule for
the precision stage; **four have their doctrine living on in a named live entry**, one of them
almost word for word — *no separate confidence test is added* on the legacy arm, *no conditional
gate anywhere* on the live one; and **one is UNDETERMINED and is the sharpest of the set** — a
carve-out on a dissolution rule whose parent principle a user ruling DID carry across, where whether
the carve-out rides with it is a ruling and not a session's call.

**★ ONE NEW EVIDENCE ANCHOR IS PROPOSED AND IS NOT ADDED.** Ten of the eleven rest on anchors the
pass already declares and locates; the eleventh needs a fourth do-not-retry anchor, on the declared
mode's weight, in the same construction as the three the pass already carries. It is located at the
object and written into the reading file as a proposal.

**★ AND HALF B TURNED UP A FINDING BEARING ON THE ANALYSIS — §2.8, rowed at [[OI-357]].** The one
transfer verdict that came back `none-found` for a *substantive* reason rather than a bookkeeping
one is D-575's, and the reason is that the Baroque partial-signature correction is legacy-only while
the production arm's handling of that notation practice is unestablished. **It is stated with what
it does not claim** — the live arm's soft prior can reach the same reading with no explicit
correction — **and with what shrinks it**: the key agreement on this repertoire is measured and
published, so any effect is already inside a published value rather than hiding behind a green gate.

**THE GUARD IS STILL RED AND THAT IS THE RULING WORKING, not an unfinished task.** Nothing was
written into `gen_phase1w_legacy_verification.py`; no mark, status, home or register entry moved;
[[OI-289]]'s verified status is untouched; and [[OI-354]] stays OPEN. The failure clears when the
reviewed set is applied, in a commit citing the user's ruling on the queue — **which is the whole
answer to the objection that verdicts written to clear a guard are the weakest kind there is.**

**Holds:** none new. **Surfacings:** §2.8. **Freeze respected:** no `src/` change, no golden, no
corpus of scores, no `tools/robust_stop/` movement, no behaviour change to the analysis, no fix to
inference, no design. **Phase 1's completion statement is not written, not drafted and not partially
written here.**

### Task 2 — COMPLETE. The defense-gap population is CLOSED, and reading the home text turned up a corruption in the register itself

**The population was derived fresh at task start (A5)** from the completion inventory's
`entries_with_no_rationale_at_all`, not carried from the dispatch or from this file. **Every one of
it is now filled, and the derived count reads zero** — no count is restated here (**D-431**).

**The act per entry was the recorded one, and the second half of it is what earns its keep:** read
the entry's own record — verbatim, plain restatement, status source — and **then open the home
document and read the text AROUND the quoted span**, because a defense is very often in the sentence
after the decision rather than inside it. **Memory was not used as a source anywhere.**

**★ THE SPLIT IS AGAIN ABOUT EVEN, AND WHERE THE DEFENSES WERE FOUND IS THE FINDING.** Before the
fill the register DISPLAYED *"derivation not recorded"* for the whole population, because the
renderer substitutes that phrase for an empty field — so the surface asserted an ESTABLISHED GAP for
entries where **no search had ever been performed.** Of those closed here:

- **two hold a defense the empty field flatly misrepresented** — one sits in a paragraph whose own
  heading is *"Why split?"* and whose second sentence is the general ground the decision rests on
  (the recorded verbatim turns out to be the first half of that justification rather than the rule);
  the other names the standing principle it enforces inside the decision's own sentence;
- **two more have their defense ONE AND TWO SENTENCES ABOVE the decision** — a single paragraph
  states the ground for a whole family of follow-the-host rules (*"Do not create parallel
  infrastructure"*), and the two entries are that rule applied to strings and to accessibility;
- **five differ BY PART**, and each is said apart: a threshold trio where the third band carries its
  own stated reason and the two values carry none; a gate whose original decision has no derivation
  while the record of why it is NOT implemented does; a version field whose purpose is stated while
  the never-rewrite half is bare; a hard constraint whose ROLE is stated but not why the guarantee
  is absolute; and a deferral whose ground is a scope decision taken elsewhere;
- **the rest are genuine gaps, said with what stands in their place** — a MECHANISM mistaken for a
  ground, a DEFINITION, a DIVISION OF RECORD, a LIST under a heading, and the STRENGTH of a
  provenance (*user-directed repeatedly*) which says how firmly a rule is held rather than why.

**★ NOTHING WAS INVENTED, AND TWO NEAR-MISSES ARE RECORDED BECAUSE THEY ARE THE FAILURE MODE.**
Several entries sit one sentence away from a reason that belongs to a DIFFERENT rule — a
feedback-loop justification next to an overwrite rule, a metadata-loss justification next to a
versioning rule, a licence justification next to a contributor-agreement rule. **In each case the
neighbouring reason is named and explicitly not borrowed.** And where the obvious modern argument
exists but the record never made it — twice, on the standing principles — the argument is named and
**deliberately not written in**, because a defense composed after the fact is what the
never-work-from-memory rule forbids.

**★ THE TWO RECORDED MECHANICAL HAZARDS WERE MET AND AVOIDED BY THEIR OWN REMEDIES.** Every fill
REPLACED the entry's trailing `rationale` rather than adding a second key, and the trailing field's
comma state was preserved per entry — some carry one and some do not. **The derived count was read
after the fills rather than the edits being trusted**, and the classifier's round-trip establishment
— which a duplicate key would break — passes.

**★ AND THE METHOD'S SECOND HALF FOUND SOMETHING NOBODY WAS LOOKING FOR — §2.9, rowed at
[[OI-358]].** Five consecutive register entries quote a different rule than their own title,
restatement and defense describe; one quotes a section heading. **Both guards pass over it**, because
each verifies that the verbatim sits at the cited line and neither asks whether it is the rule the
entry is about. The two entries of this task's own population that are among the five carry a marker
saying so, and their fills are written against the decision the title and defense identify rather
than against the quoted text.

**Holds:** none new. **Surfacings:** §2.9. **Freeze respected:** no `src/` change, no golden, no
corpus of scores, no `tools/robust_stop/` movement, no behaviour change to the analysis, no fix to
inference, no design. **Phase 1's completion statement is not written, not drafted and not partially
written here** — and it is worth saying plainly at the moment this count reaches zero: **a closed
defense-gap population is one item of the finish line, not the finish line.**

### ★ WHERE THIS BATCH STOPPED

**Tasks 0, 1 and 2 are COMPLETE, committed and pushed** — three commits, each its own task boundary,
each with its guard run, its enumeration and its `STATUS.md` pointer entry. **Tasks 3, 4, 5 and 6 are
NOT STARTED.** That is a capacity stop at a clean boundary, not a halt on a finding: no STOP note was
written against the batch, no analysis-bearing surface halted it, and **nothing is left half-edited**
— every act on disk is complete in itself, every derived surface re-derives, and the guard set stands
at ONE failing, which is the legacy-mark verification that Ruling 18 requires to be carried.

**★ WHY TASK 3 WAS NOT OPENED RATHER THAN OPENED AND LEFT PART-DONE.** Its deliverable is ONE
GENERATED DERIVATION over a derived population of open rows, and a derivation published over part of
its population is exactly the silent cap the standing rules forbid — it would read as covering the
class while covering some of it. The three tasks that ran were each closed whole for the same reason.

**What a continuing session should know.**

1. **Task 3's population is DERIVED, not carried from here:** the completion inventory's
   `the_gating_split` → `non_gating` set, read at task start. What is owed per row is a verdict under
   **D-639**'s test — *the doc-sync half reaches a document's account of itself ONLY WHERE THAT
   ACCOUNT CHANGES HOW THE DOCUMENT'S ANALYSIS CONTENT IS READ* — whose three worked examples ARE the
   test (an as-built banner over a dormant mechanism IN; a missing supersession note IN; a stale
   anchor or formatting artifact OUT), with **fallback (1A)** applied and SAID wherever the test does
   not decide. **No hand verdicts.** The method to follow is the existing first application's, at
   `tools/audit/decisions/gen_true_half_reach.py` — same shape, not an invented one (#6).
2. **One thing Task 3 will meet immediately, and it is already rowed:** the completion inventory
   still PUBLISHES this as an open question — `who_settles_it` reads *"the user. It is reported, not
   decided."* — while the user ruled it on 2026-08-04 as D-639. Its clause quote is derived and moved
   with HEAD; its criteria are an authored constant that did not. That is [[OI-338]], and the
   finish-line generator's own text records the same finding.
3. **Tasks 4 to 6 are untouched and their populations must be derived fresh:** the section-unreached
   and findings-not-rules re-homes, the session-executable gating rows, **Ruling 16's sibling sweep
   and its one comment-only `src/` commit**, and OI-346's marks. **Ruling 16 is the only licensed
   `src/` touch of the knowledge arc and it is NOT taken here** — no `src/` file was opened for
   editing by this batch.
4. **Three things await the user and none of them blocks Tasks 3–6:** the registration queue, now
   covering twenty-three rulings, on which no register entry may be written until it is ruled; the
   [[OI-354]] verdict set, whose review is what clears the one failing guard; and the two new
   apparatus questions rowed here, [[OI-356]] and [[OI-358]], each of which needs a mechanism or
   filing decision the record does not carry.
5. **A convention this batch adopted and recorded, so it is not rediscovered:** inside an
   open-items status cell, name another row's resolved status **in words, never with the glyph**
   ([[OI-356]]).

**Phase 1's completion statement is not written, not drafted and not partially written by this
batch** — and the defense-gap population reaching zero does not change that: it is one item of the
finish line, and the finish line's own count of what remains is derived at
`tools/audit/phase1_finish_line.json` (**D-431**).

---

# ═══ THE FOURTH RETURN CONTINUATION (dispatch `cc_instruction_return_continuation_4.md`, 2026-08-09) ═══

> Rulings 20–27 of `cowork_rulings_2026_08_09_fourth_stop.md` are applied here, and the remaining
> program continues. The sections above are earlier batches' and are not rewritten. New holds are
> appended to §1, new surfacings to §2, and each task's log below.

### 1.10 STOP — Ruling 25's remedy is REFUTED by its own both-ways condition: anchoring to the leading token fixes ONE row and breaks TWO (Task 2)

**This is the mechanism working, not a failure.** Ruling 25 corrects the open-items index parser so
that a row's resolved state is *"anchored to a row's own status cell's leading token, never to a
mention of another row's resolution"*, and attaches the condition that makes it safe: **every index
row is decided both ways, before and after; the only verdicts that may move are rows the defect's
shape names; any other movement is a STOP.** The dispatch's assumption **A3** states that shape in
words — *rows whose status cell mentions another row's resolution.*

**Every index row was decided both ways before anything moved**, by a generated table that
implements BOTH rules itself rather than reporting a diff of the result
(`tools/audit/oi356_parser_correction.json`). **Three rows move, and NOT ONE of them mentions
another row's resolution.** Read at the rows themselves, with the text around each mark generated
rather than transcribed:

- **Two of the three state THEIR OWN resolution somewhere other than the first character.** One
  cell reads *"PROTOCOL RATIFIED …; ✅ EXECUTED …"* — the mark is late only because a ratification
  date precedes it. The other opens with the ruling that settled its question, carries the mark
  mid-cell on the delivered half of its own work, and ends *"Row CLOSED"*. **Both are genuinely
  resolved, the rule as it stands reads them correctly, and the corrected rule would mark them
  open.**
- **The third is genuinely OPEN** — its cell begins with the word *OPEN* and the mark appears far
  into it on a delivered sub-result. **This is the one row the correction improves.**

**So the remedy as worded trades one error class for another: it fixes one row and breaks two.**
The parser is left EXACTLY as it stands and nothing was applied.

**★ AND THE INSTANCE THE ROW WAS FOUND ON NO LONGER EXISTS AT THIS TREE**, which is why the movers
are all of a different kind: the working convention [[OI-356]] adopted — *name another row's
resolved status in words, never with the glyph* — was applied to the cell that caused it, so the
defect's own founding instance is gone while the mechanism that produced it is untouched.

**What is NOT withdrawn.** [[OI-356]]'s finding stands entirely: a cell that mentions another row's
mark still makes its own row read as resolved to every derivation, and the working convention is
still the only thing preventing it. What is refuted is that **the leading token** is the remedy.

**What the user is being asked.** The remedy needs a different shape, and three are visible from the
measurement — recognise a resolution token anywhere in a bounded opening rather than at the first
character; take the state from a dedicated position rather than by search; or forbid the glyph in
prose and check for it. **Choosing among them is a mechanism change D-436 reserves to the user**,
and this session neither chose nor prototyped one.

**★ AND DECIDING EVERY ROW BOTH WAYS TURNED UP TWO FURTHER DEFECTS IN THE SAME PARSER, each rowed
rather than folded into this STOP:** rows whose status cell states a resolution IN WORDS with no
glyph, which read OPEN to every derivation while their own text says otherwise ([[OI-361]]); and a
row that the parser SILENTLY DROPS because it does not split into the expected number of cells, so
it is neither open nor resolved but absent ([[OI-362]]).

## 2 (continued). Surfaced findings

### 2.10 The Baroque partial-signature correction is recorded RESOLVED on one anchor case, and over the DERIVED population at committed outputs it reads fewer than half the tonics (Task 3)

**Found by the bounded establishment [[OI-357]] was given, and not by looking for it.** Ruling 26
ordered the committed outputs for the partial-signature stems compared against ground truth. The
comparison could not answer the question it was aimed at — see the Task 3 log — and what it did
answer is this.

**The population is DERIVED, and that is why it is larger than the record's own account.** The
evidence document states its own method — the notated key signature against the published annotated
key, from the corpus metadata — and that METHOD was applied mechanically to every piece in that
file, rather than the document's six-row table being transcribed. It yields a population many times
that size.

**What was measured, at the most recent committed run for this repertoire — dated after the
correction landed, so it reflects it.** Fewer than half the population is read with the annotated
tonic. **The large majority of the disagreements land on a home of the NOTATED signature**, which is
the evidence document's own diagnostic for the signature lock the correction exists to escape; both
homes are computed from the notated signature alone, so that column is derived and not a judgment.
**And the split by the annotated key's mode is the sharpest cut:** the minor-key half fares markedly
better than the major-key half, while the correction's own recorded detector keys on a single
MINOR-key signal — the flattened sixth degree pervasive across the sounding weight and dominating its
natural form. **The cut is reported and the causal claim is NOT made:** this pass counts, it does not
explain.

**★ WHAT IS DELIBERATELY NOT CLAIMED, because the disagreement total is not a defect total.** Each
disagreement is one of three things and this pass distinguishes none of them: a genuine defect; a
**defensible modal reading the major/minor ground truth cannot represent**, which gate block (A)
makes a ground-truth limitation and explicitly not a defect to optimize away — the count of
non-major/minor emissions among the disagreements is reported for exactly that reason; or an artifact
of comparing a global reading against a global annotation on a piece that modulates.

**★ AND THE RECORD'S OWN ACCOUNT READS WIDER THAN THE MEASUREMENT SUPPORTS.** The evidence document's
banner declares the weakness RESOLVED, and what it verifies is one anchor case. Both halves are true
as written; a reader meets *resolved* and would not learn that the population the anchor case belongs
to is mostly not.

**What bounds it, stated so it is not read as larger than it is.** Its subject is the LEGACY arm,
which the production path does not run — so nothing here is a claim about what ships, and [[OI-357]]
still carries the production question unanswered. **This repertoire is not the gate corpus**, so no
published measurement moves and none is questioned. Every value is at
`tools/audit/oi357_partial_signature_establishment.json` (**D-431**).

**Rowed at [[OI-363]]** with its detail file in the same commit (rule (c)). **Nothing is proposed for
it beyond the row** — no fix, no design, no inference change.

## 3 (continued). Per-task log — the fourth return continuation

### Task 0 — COMPLETE. The register event: eleven entries, the triage re-class, and the OI-354 set applied — the guard clears in the commit that cites the ruling

**The start state was derived at the artifacts before any act (A6), not carried from the dispatch.**
The guard set's one failing tool is the legacy-mark verification, read at the committed
`tools/audit/guard_state.json` → `summary`; the three queues were read whole at their own files; the
register's highest identifier was read at the register data. No count is restated here (**D-431**).

**A1 HOLDS, and it was checked before the first entry was written.** Every home Ruling 20 names
STATES RULES, which is the register's rule (h) kind half: `cowork_audit_protocol.md`'s
dispatch-protocol block says of itself, in its own opening, that what follows are *rules* governing
every dispatch, and each existing subsection states one with its ruling and its defense; `CLAUDE.md`
principle #21's block and its decisions-register section likewise. No home failed its kind check, so
the STOP the assumption reserves did not fire.

**★ ONE THING IN THE QUEUE'S §4 WAS STALE AND IS REPORTED RATHER THAN QUIETLY FOLLOWED.** §4's
heading says *"for the seven"*, and the section carries more rows than that — the 2026-08-09
extension appended two beneath the table and did not touch the heading. **The population was
therefore taken from §4's TABLES**, which is what the ruling names when it says *"homes as proposed
in the queue's §4"*, and not from that count; every proposed decision has exactly one proposed home
there and all of them were written. The heading is left as it stands (#12 — it is a delivered
decision surface) and the discrepancy is recorded in the queue's own closing state.

**What was written, in ONE commit.**

1. **Ruling 20 — TEN entries at their ratified homes**, eight in `cowork_audit_protocol.md`'s
   dispatch-protocol block and two in `CLAUDE.md`, each in the receiving section's own voice with its
   defense, provenance in the register fields and never in the specification text. **THE THIRTEEN
   EXERCISES are recorded as confirmed in the queue's closing state** and carry no entry, which is
   what an exercise verdict means. **★ NO NEW ENTRY CARRIES AN ENTRY-RATIFICATION EVENT, and the
   reason is stated in each one:** the user ruled the CLASSIFICATION and the HOME, and the entry text
   was written afterwards, so recording an entry ratification would be the session ratifying its own
   writing (#14).
2. **Ruling 21 — D-291 is SPLIT.** The measurement half becomes its own entry at the home Ruling 11
   gave it; **D-291 keeps the build half**, where its verbatim is located and verified. The two
   cross-reference each other, no already-ruled text is reworded (#14), and the only field of D-291
   that moved is its TITLE — which named both halves — with the former title preserved whole in its
   provenance (#12).
3. **Ruling 22 — the triage set applied.** Fourteen verdicts stand as authored, including the refused
   mechanism at D-473. D-486's uncovered per-corpus half is re-classed into the defect class with the
   former class and its whole ground preserved beside it, and **[[OI-359]]** is created with its
   detail file in the same commit (rule (c)). **The mechanism is not built**, as the ruling directs.
4. **Ruling 23 — the OI-354 verdict set applied**, with the proposed anchor, and **[[OI-354]]
   FLIPPED**. D-580's transfer cell is recorded UNDETERMINED *pending Ruling 27*, and the tool's own
   note for that entry says so, so a later reader meets a RULED state rather than an unfinished one.

**★ THE AUTHORING-DOES-NOT-CLEAR SEPARATION HELD END TO END, which is the point of how this landed.**
The verdicts were authored in the previous continuation and cleared nothing; the standing check was
carried red across that whole session; and it clears HERE, in the commit that cites the user's ruling
on the reviewed set. Nothing was written by the session that authored them, and nothing had to be
unwritten.

**★ APPLYING RULING 23 EXPOSED THE SAME LAYERED-STOP SHAPE A THIRD TIME, and it is reported rather
than absorbed.** [[OI-354]]'s own finding was that an assumption STOP fired before the coverage
check, so nothing ever reached that check. With the coverage check satisfied, **the ANCHOR LOOP that
follows it ran for the first time since its own drift began, and eight `ARCHITECTURE.md` evidence
anchors had moved.** Each was re-aimed per the tool's own reported line — authored-input maintenance,
which is now a register decision rather than a precedent — and no verdict, mark, status or home moved
with them. **The general shape is worth a reader's attention: a tool with several ordered STOPs
reports only its first, so clearing one is never evidence that what follows it was passing.** That is
now the third instance of the shape in three consecutive batches.

**Three authored inputs were maintained, each caught by its own tool's STOP rather than by a reader.**
The apparatus declaration's verdict for [[OI-354]] moved WHOLE into its retired table with the reason
it closed; **[[OI-359]] reached the first cut with no verdict and a GATES verdict was authored for it
with its ground** — no non-gating verdict was hand-added, which is the act the record forbids; and
the live-prohibition pointer tool STOPPED because the class gained an entry its authored table held
no do-not-retry line for.

**★ THAT LAST ONE NEEDED MORE THAN A TABLE ROW, AND THE DIFFERENCE IS STATED BECAUSE IT IS A JUDGMENT
CALL.** The pointer tool reads the entry identifiers off the SAME line its authored phrase locates,
and the declared-mode prohibition is written over two lines with the identifier on the second — so
the phrase had to be taken from the identifier-bearing line. It also stamped every pointer with ONE
hard-coded observation date, which would have made the new pointer state something untrue. The date
is now a per-section authored value, the three existing sections keep the date they were observed on,
and the new one carries its own. **This is a small change to the tool's authored inputs and its
pointer wording, not to what it derives**; it is reported here rather than done silently, which is
the rule this batch also homed.

**★ AND THE HOMING ACT ITSELF WIDENED ANOTHER TOOL'S OWED SET, exactly as that tool's own reading file
predicts it would.** Three of the new entries are homed in `CLAUDE.md`, so the rule-triage check
stopped on all three the moment they landed — the shape §2 of the triage file states in general
terms. **Verdicts were authored for the three on the established pattern, with their grounds, and
they are recorded as newly owed and unratified in that file's closing state.** One of the three
declines an available mechanism on purpose and says so.

**Holds:** none new. **Surfacings:** none new bearing on the analysis — every subject of this task is
the record's own bookkeeping and the rulings that govern it.

**★ THE STANDING SELF-CHECK CAUGHT A DEFECT IN THIS SESSION'S OWN CONDUCT, and it is recorded because
it briefly fed a wrong conclusion.** Twice this task redirected a command's output to `/tmp/<name>`
and then READ `c:\tmp\<name>` with the file tools. The redirect does not land there, and both files
already existed from earlier sessions — so what was read was a month-old artifact. For a few minutes
the stale enumeration was taken for the current tree and read as evidence of repository corruption.
**It was caught by the enumeration disagreeing with this session's own edits** — a file this session
had certainly modified was absent from the list — and the diagnosis was then completed at git objects
by explicit hash, which confirmed the tree was sound. **Nothing was written on the wrong reading and
no artifact carries it.** The lesson is narrow and worth stating: an output path that is not the
session's own scratchpad may already hold a stale file with that name, and a redirect that silently
lands elsewhere leaves the reader with a plausible, wrong answer rather than an error.

**Freeze respected:** no `src/` change, no golden, no corpus of scores, no `tools/robust_stop/`
movement, no behaviour change to the analysis, no fix to inference, no design. **Phase 1's completion
statement is not written, not drafted and not partially written here.**

### Task 1 — COMPLETE. The five quotes re-taken; the detection method built corpus-first, MEASURED, and NOT adopted — which is the result, not a shortfall

**A2 was checked at the home before the first re-take, and it holds in both halves.** Each of the
five quotes was taken from the bullet the entry's own TITLE and DEFENSE describe, read in place at
`docs/scoring_model.md` §8 — not inferred from the offset the row reports, and not copied from the
row's own table. Two of the five could be confirmed twice over, because their recorded defense names
a measurement that appears in the correct bullet and in no other. The corrected pairs pass both
existing guards — every verbatim resolves at its cited home with **zero anchor drift**.

**In every one of the five the former, incorrect quote and the former anchor are preserved whole in
the entry's provenance (#12), while the `verbatim` field carries ONE quote (#6)** — the shape the
ruling fixed. **Nothing else moved in any of the five.** Title, plain restatement, defense, status,
date, ratifier and LEGACY mark are untouched: this row's own finding was that those were correct and
mutually consistent, and a repair that rewrote them would have destroyed the evidence that made the
defect diagnosable in the first place. The two entries whose defense was written by the defense-gap
task *against the decision the title identifies* keep those fields exactly as written, each still
carrying its marker.

**★ THE CHECK WAS BUILT CORPUS FIRST, AND THE CORPUS IS DATA RATHER THAN A LIVE READ — for a reason
that is easy to get wrong.** The five known-bad quotes are recorded IN the tool. Had the corpus been
read from the live entries, the repair would have emptied it at the moment of repair and the
separation could never have been re-measured afterwards. Recording it first is also what let the
measurement be taken twice: once at the corrupted tree, once after the repair, with the labelled
positives unchanged across both.

**★ AND THE MEASUREMENT SAYS THE CHECK MAY NOT BECOME A GUARD. THAT IS REPORTED, NOT TUNED.** All
five known-bad quotes sit at the floor of the value. But a substantial population of legitimate
entries sits at or below that same floor, so **no threshold separates the two populations** and a
guard built on it would deny legitimate work — which is D-473's ground and the third of the measured
conditions a mechanism is judged on. **The sharper result is about the signal's CEILING rather than
its threshold:** after the repair four of the five entries rise and **one stays at the floor**, its
correct bullet stating the rule in code names its own title paraphrases in ordinary words. So the
method is not merely un-thresholded — it is measurably unable to see one of the five cases it was
derived from. **Adjusting the token count, the stopword list or the comparison until the five fell
below the remainder would be fitting the signal to the cases that motivated it**, which is the defect
the catalog names DT-2 and the reason the adoption condition was ruled in advance. Nothing was
adjusted. Every value is at `tools/audit/decisions/verbatim_subject_consistency.json` (**D-431**).

**[[OI-358]] FLIPS, and what it does NOT discharge is rowed rather than absorbed.** That row gated on
two independent grounds. The first — five entries stating one rule's identity over another rule's
words — is discharged. **The second is not:** both existing checks are still satisfied by a
corrupted pair, so their green verdicts still do not bound what they appear to bound. Closing the
row on the repair alone would be the [[OI-283]] shape, so the surviving obligation is **[[OI-360]]**,
created with its detail file in the same commit (rule (c)).

**Two authored inputs were maintained, both caught by their own tools' STOPs.** [[OI-360]] reached
the apparatus declaration's first cut with no verdict and a GATES verdict was authored for it with
its ground; [[OI-358]]'s verdict moved WHOLE into the retired table with the reason it closed — and
that retirement note says in terms that the row's SECOND ground does not retire with it.

**★ ONE CONSEQUENCE OF ADDING A TOOL AT ALL, worth recording because it is not obvious.** The guard
runner derives its candidate population by searching every file under `tools/audit/` for the words
naming a verify mode — so the new tool joined that population **because its own docstring explains
that it has no such mode**. That is the derivation being deliberately over-inclusive, and its STOP
working. An authored NOT-RUN entry was written with the reason, and a classification verdict beside
it: it is neither a live invariant nor a dated measurement of the tree, it RANKS entries for a
reader. **Adding it to the run is a decision that follows a measurement showing separation**, and
that measurement is negative.

**Holds:** none new. **Surfacings:** none new bearing on the analysis — the five repaired entries are
records of decisions, and the decisions themselves were never in doubt.

**Freeze respected:** no `src/` change, no golden, no corpus of scores, no `tools/robust_stop/`
movement, no behaviour change to the analysis, no fix to inference, no design. **Phase 1's completion
statement is not written, not drafted and not partially written here.**

### Task 2 — COMPLETE as a MEASUREMENT and a STOP. The parser is NOT changed, because deciding every row both ways refuted the remedy — and turned up two further defects in the same parser

**A3 IS REFUTED, and the refutation is §1.10.** The both-ways table was built first, as the ruling
requires, and it implements BOTH rules itself rather than reporting a diff of the result — which is
the only construction that can show a movement rather than assert one. Three rows move; **not one of
them mentions another row's resolution**, which is the shape the condition names. Two of the three
state THEIR OWN resolution somewhere other than the first character and are genuinely closed, so the
corrected rule would mark them open; the third is genuinely open and is the single row the
correction improves. **Fixes one, breaks two. Not applied.**

**★ THE FOUNDING INSTANCE IS GONE AND THE MECHANISM IS NOT, which is the reason the measurement came
out this way.** [[OI-356]] adopted a working convention — name another row's resolved status in
words, never with the glyph — and the previous continuation applied it to the cell that caused the
defect. So the defect's own instance no longer exists while the parser that produced it is
untouched, and every row that now moves under the proposed rule is a different kind of case
entirely. **A remedy measured against a population the defect has left is measuring something else**,
and that is exactly what the both-ways condition caught.

**Nothing about [[OI-356]] is withdrawn** and the row stays OPEN with the measurement on it. Three
candidate remedies are visible from the table and **none is chosen or prototyped** — choosing is a
mechanism change **D-436** reserves to the user, and one of the three is a convention rather than a
mechanism.

**★ AND DECIDING EVERY ROW BOTH WAYS TURNED UP TWO FURTHER DEFECTS IN THE SAME PARSER — which is
what a both-ways pass is FOR, and neither would have been visible from a forward-only correction.**

- **[[OI-361]]** — a row whose status cell states its resolution IN WORDS, with no glyph, reads OPEN
  to every derivation. The register's own rule (d) does not mandate the glyph, so such a row is
  following the rules and is miscounted anyway. **The per-row reading is authored and does not claim
  every candidate is a defect:** one of the three states a MIXED status whose correct single bit is
  not settled by its own text, and this pass does not settle it.
- **[[OI-362]]** — a row that does not split into the expected number of cells is **skipped with no
  report of any kind**, so it is neither open nor resolved but ABSENT. One row is being dropped at
  HEAD. **This is worse than either mis-reading sibling:** a mis-read row is at least counted
  somewhere and a moving count can be noticed; a dropped row is in no population at all, and the
  bijection check uses a looser pattern and passes, so the row is accounted for on one surface while
  invisible on another.

**★ ONE FIX WAS AVAILABLE IN A SINGLE CHARACTER AND WAS DELIBERATELY NOT TAKEN.** The dropped row is
malformed by one unescaped separator. Escaping it would put a row into the open population — moving
the open-row count, the true-half cuts, the finish line's populations and the apparatus declaration's
candidate cut. **A population movement belongs to an act that accounts for it, not to a parser task
that would slip it in unremarked**, and the order is stated on the row: the silent-skip STOP goes in
first, so that the movement is visible rather than merely happening.

**Holds:** §1.10, the refuted remedy, which needs the user. **Surfacings:** none bearing on the
analysis — every subject here is the open-items index's own parser.

**Freeze respected:** no `src/` change, no golden, no corpus of scores, no `tools/robust_stop/`
movement, no behaviour change to the analysis, no fix to inference, no design. **Phase 1's completion
statement is not written, not drafted and not partially written here.**

### Task 3 — COMPLETE as a bounded establishment. The question is answered in ONE direction, so [[OI-357]] stays OPEN — and what the comparison CAN see is a finding of its own

**A4 HOLDS, and it was checked before the first comparison.** A stem population IS derivable from the
record: the evidence document states its own method, and applying that METHOD mechanically to every
piece in the file it names is a stricter reading of *derived* than transcribing the document's own
table would have been — it cannot be narrower than the record's rule makes it. **The STOP the
assumption reserves did not fire, and no piece was sampled by judgment.**

**★ THE COMPARISON'S OWN ESTABLISHMENT IS STATED BEFORE ANY VALUE IN IT, and it is the first
finding.** Which arm produced the committed outputs is not a choice this pass makes — it is a
property of what is on disk, and it was MEASURED rather than assumed, because it decides what the
whole comparison is about. **Every committed output directory for this repertoire predates the date
the joint estimator became the production inference layer; none carries a corpus manifest; none
carries any field naming an inference arm.** They are the legacy arm's. **So the comparison cannot
answer [[OI-357]]'s question**, and that half of the row is untouched.

**The row therefore stays OPEN with what remains named**, which is the dispatch's own instruction for
a partial answer: closing it would need a production-arm reading of these stems, no committed output
supplies one, and producing one is a corpus run this ruling forbids.

**★ AND WHAT THE COMPARISON CAN SEE IS NOT WHAT THE ROW'S PREMISE EXPECTED — §2.10, rowed at
[[OI-363]].** [[OI-357]]'s framing is that the legacy resolver HAS the handling and the production
arm does not. Measured over the derived population at committed outputs, **the legacy handling
resolves fewer than half of it**, the large majority of the disagreements land on a home of the
NOTATED signature — the evidence document's own diagnostic for the lock the correction exists to
escape — and the shortfall is concentrated in the major-key half while the correction's recorded
detector keys on a single minor-key signal.

**That does not weaken [[OI-357]]; it sharpens what its remaining question is worth asking about.**
The thing a later production-arm run would be compared against is not *a working correction* but a
correction that works on part of the population, and any account of what the production arm lacks has
to say which part.

**★ THE CUT IS REPORTED AND THE CAUSAL CLAIM IS NOT MADE**, which is the line this task held
throughout: the artifact counts and says in its own text that it does not explain. **No mechanism is
diagnosed, no fix is proposed, and none is authorized** — the standing instruction is that an
inference problem is DECLARED, not designed for, and phase 1's gate stands.

**Holds:** none new. **Surfacings:** §2.10, which bears on the analysis and is therefore surfaced
whatever its size.

**Freeze respected:** no `src/` change, no golden, no corpus of scores regenerated, no
`tools/robust_stop/` movement, no behaviour change to the analysis, no fix to inference, no design.
**Phase 1's completion statement is not written, not drafted and not partially written here.**

### Task 4 — COMPLETE. The D-580 fact-gathering surface is delivered, with no verdict — and gathering the facts LOCATED a conflict nobody had put side by side

**A5 HOLDS in every part.** Every claim on the surface is cited at its source and was read in place;
both records were read whole; anything the record does not settle is in the UNSETTLED section rather
than filled; and **no recommendation is made at all**, which is the strongest form of the user's own
rule that a decision rests on facts rather than on an unsure or remembered one.

**The surface is at `ratification_surfaces/cowork_d580_transfer_fact_gathering_2026_08_09.md`.** It
takes no transfer verdict, proposes no fix, design or inference change, and moves no status.

**★ WHAT GATHERING THE FACTS SETTLED, and it is more than expected.** The carrying ruling's stated
SCOPE is a named phase-3 family, and the gate layer is not a member of it; the measurement behind
*purely-local* answers a different question from the one the principle asks — it establishes which
gates read outside their own stretch, not where a non-compensating refinement belongs; one of the two
carved-out gates no longer exists under its own name; and neither is reachable on either production
surface.

**★ AND ONE UNSETTLED ITEM WAS CLOSED BY INVESTIGATING RATHER THAN LEFT, WHICH LOCATED A CONFLICT.**
D-580's own text routes its unfinished business to the retirement map. **That map's first entry
retires the whole gate family without qualification and records no carve-out of any kind.** So the
routing D-580 relies on does not, as it stands, carry the exception D-580 asserts. **The conflict is
LOCATED and deliberately NOT RESOLVED:** two readings are visible — that the map predates or overlooks
the carve-out, or that the two speak of different acts, a dissolution INTO the competition versus a
deletion OF the legacy path — and the record chooses neither. Both readings are written onto the
surface as what they are.

**Four things remain UNSETTLED and are marked as such rather than filled**, including the question the
cell turns on: whether a principle ruled binding on one named family reaches a decision outside it.
**No text in the record addresses it**, and saying so is the answer this pass owes.

**Holds:** the surface itself, which awaits the user's ruling on facts. **Surfacings:** none new
bearing on the analysis — the two gates are legacy code unreachable on either production surface, and
the conflict located is between two records rather than in any behaviour.

**Freeze respected:** no `src/` change, no golden, no corpus of scores, no `tools/robust_stop/`
movement, no behaviour change to the analysis, no fix to inference, no design. **Phase 1's completion
statement is not written, not drafted and not partially written here.**

### ★ WHERE THIS BATCH STOPPED

**Tasks 0, 1, 2, 3 and 4 are COMPLETE, committed and pushed** — five commits, each its own task
boundary, each with its full guard run, its classification run after it, and its `STATUS.md` pointer
entry. **Task 5 is NOT STARTED and Task 6 is NOT REACHED.** That is a capacity stop at a clean
boundary, not a halt on a finding: no STOP note was written against the batch, nothing is left
half-edited, every derived surface re-derives, and **the guard set stands at ZERO failing** — the
standing failure this batch inherited was cleared by Task 0, in the commit that cites the ruling
authorizing it.

**★ WHY TASK 5 WAS NOT OPENED RATHER THAN OPENED AND LEFT PART-DONE.** Its first sub-part is ONE
GENERATED DERIVATION over a derived population, and the previous continuation declined it for exactly
this reason: *a derivation published over part of its population is the silent cap the standing rules
forbid — it would read as covering the class while covering some of it.* Its last sub-part is the
knowledge arc's ONE licensed `src/` act, where a half-performed sweep would leave the code carrying
some corrected comments and some false ones with no record of which is which. **Both are worse
part-done than not begun.**

**★ ONE THING A RECONNAISSANCE FOR RULING 16's SWEEP ESTABLISHED, recorded because it corrects a
premise the next session would otherwise carry.** Ruling 16 says in its own words that [[OI-353]]'s
six sites *"are the found members, not the family"*. **They are: candidate sites exist well beyond
the six**, and the largest group is of a kind neither [[OI-353]] nor the phase-1w side finding names —
**comments declaring the JOINT MODULE'S OWN dormancy**, written before the notation switch and
describing a state that switch ended. Located, with the file tools, at
`src/composing/analysis/CMakeLists.txt` (the joint module's own block, the notation-record block and
the record-producer block) and at `src/composing/analysis/section/sectionrecordadapter.cpp` beside the
header already on the list. **What is NOT claimed:** that every candidate is false at HEAD. Many
neighbouring `DORMANT` comments in the same file are about modules that ARE still dormant and are
true, and separating the two is precisely what the sweep must do against the configuration facts —
which is why the enumeration is generated and not read off. **The next session derives the
enumeration and does not start from six.**

**What a continuing session should know.**

1. **Task 5's four sub-parts are untouched and each population must be derived fresh:** the
   reach-verdict derivation over the apparatus-classed documentation rows (**D-639**'s test, its
   three worked examples ARE the test, fallback (1A) applied and SAID where the test does not decide,
   no hand verdicts, the method being the existing first application's shape and not an invented one);
   the section-unreached and findings-not-rules re-homes; the session-executable gating rows; and
   **Ruling 16's sibling sweep with its ONE comment-only `src/` commit** (sweep first, generated;
   diff verified comment-only; a sibling whose falsity needs judgment about the analysis is HELD, not
   edited; [[OI-353]] flips on it). **No `src/` file was opened for editing by this batch.**
2. **Task 6's OI-346 marks are not reached.**
3. **Four things await the user, and the first two are new STOPs this batch produced:**
   **§1.10** — Ruling 25's remedy is refuted by its own both-ways condition, and the parser is
   unchanged; **the D-580 fact-gathering surface**, which takes no verdict and returns the cell to the
   user on facts. Beside them stand the two mechanism-or-convention decisions [[OI-361]] and
   [[OI-362]] need, and the three candidate remedies [[OI-356]] now carries.
4. **Two findings bearing on the analysis were surfaced and are rowed, not proposed for:** §2.10 /
   [[OI-363]], the partial-signature correction resolving fewer than half its own derived population
   at committed outputs; and [[OI-357]], whose production-arm question is still unanswered because no
   committed output for that repertoire was produced by the arm that ships.

**Phase 1's completion statement is not written, not drafted and not partially written by this
batch** — and the guard set reaching zero failing does not change that: a green guard set is a
statement about the record's own machinery, not about the finish line, whose remaining count is
derived at `tools/audit/phase1_finish_line.json` (**D-431**).

---

# ═══ THE FIFTH RETURN CONTINUATION (dispatch `cc_instruction_return_continuation_5.md`, 2026-08-09) ═══

> Rulings 28–35 of `cowork_rulings_2026_08_09_fifth_stop.md` are applied here, and the fourth
> continuation's Task 5–6 tail is resumed. The sections above are earlier batches' and are not
> rewritten. New holds are appended to §1, new surfacings to §2, and each task's log below.

### 1.11 The registration queue's extension is scoped to Rulings 24–35, so Rulings 20–23 are in NO queue (Task 0)

**Reported, not decided.** The dispatch scopes the queue extension to **Rulings 24–35**, and that is
what §7 of `ratification_surfaces/cowork_ruling_registration_queue_2026_08_09.md` covers. **Rulings
20–23 are therefore classified nowhere.**

**What they are, so the gap can be judged in one line.** Each is the user's ruling ON one of the
three review queues: ratifying the registration queue's verdicts (20), splitting **D-291** into two
identifiers (21), ratifying the triage set with one re-class (22), and ratifying the OI-354 verdict
set except one cell (23). On their face each is the ratification event a queue exists to obtain
rather than a further ruling needing classification, and **21**'s content is already register data at
**D-291** and **D-656**.

**That reading is deliberately NOT taken.** A session classifying four rulings its dispatch did not
send it would be widening its own scope, which is the act **D-654**'s narrow-letter default forbids —
and the reported-widening clause makes a widening reviewable only when it is reported, which is what
this section is. **Nothing is at risk meanwhile:** every one of the four is on disk in a ratified
record, and each is recorded in the provenance of the act it licensed.

## 3 (continued). Per-task log — the fifth return continuation

### Task 0 — COMPLETE. Rulings 28, 29, 30, 32, 34, 35(a) and 35(c) recorded; OI-230 flips on a derivation; two rows created

**The start state was derived at the artifacts before any act (A6), not carried from the dispatch.**
The guard set was read at the committed `tools/audit/guard_state.json` by running the full set
unchanged before the first edit: **zero failing**, which is where the fourth continuation left it.
The working tree carried no uncommitted work of any batch's own. The rows this task writes to were
read at the INDEX; the register's highest identifier and the highest open-items identifier were read
at their own surfaces. No count is restated here (**D-431**).

**A5 HOLDS, and it was checked before the kind list was written.** Ruling 28 names
`cowork_design_doc_template.md` as the kind list's home in its own words, and that document is the
ratified ONE home of the writing standards — so the list went in **in that document's own voice**,
beside the section structure it scopes, and nowhere else.

**What was done, in order.**

1. **Ruling 28 — the KIND LIST is written into `cowork_design_doc_template.md`.** Two bound kinds
   (specification, design document) and nine exempt ones, each named rather than described as a
   class; **a document of an unlisted kind is a STOP** and the list is maintained the way the guard
   population is — a kind is added by a user ruling, in the commit that records it, with the reason
   it is a different genre. **One thing is stated that the ruling implies rather than says, and it is
   stated because the omission would invert the ruling:** the two WRITING standards and the
   status-banner convention are **not** kind-scoped and bind every document, exempt genres included.
   Only the fourteen-section structure is scoped.
2. **Rulings 29 and 32 — recorded at the conformance machinery**, which is
   `tools/audit/claude_md_rule_triage.py`, the tool that classifies every `CLAUDE.md` rule as
   MECHANISM or KNOWLEDGE. **D-193** moves into the defect class **on the mechanical subset only**,
   with the deep half's KNOWLEDGE verdict now the user's rather than a session's, and the former
   class and its ground preserved beside it (#12) — the D-486 shape of one wave earlier. The three
   checks are named at the entry: status-banner presence, terms-table presence on a new
   specification, and structure against Ruling 28's kind list.
3. **[[OI-364]] created** with its detail file in the same commit (rule (c)): the owed mechanical
   check. **The mechanism is deliberately NOT built** — it joins the **D-436** backlog like every
   other member of that class, and what a member owes first is a measured establishment (#19), then
   a user ruling on whether to build it at all.
4. **Rulings 30 and 31 — recorded on [[OI-229]]'s row**, which stays OPEN because the cleanup itself
   is not done; what is settled is its SCOPE and its ORDER. Both halves of the user's own two-tier
   research-term rule are written out, because a rule stated as *research terms are not renamed* and
   nothing else would read as a licence to leave them unannotated.
5. **[[OI-230]] FLIPPED RESOLVED, and the flip is DERIVED question by question** rather than
   asserted — (a) by Ruling 28, (b) by Rulings 29 and 32, (c) by Rulings 30 and 31 — with each
   answer's own content on the row so a reader can check the derivation without opening the ruling
   record. **The work the answers create is carried elsewhere rather than dropped** ([[OI-283]]'s
   shape avoided): the owed check at [[OI-364]], the cleanup at [[OI-229]].
6. **Ruling 34 — recorded on D-580's TRANSFER cell** in
   `tools/audit/decisions/gen_phase1w_legacy_verification.py`, and in the entry's own provenance at
   the register data. **[[OI-365]] created** with its detail file in the same commit for the residual
   the ruling declines to decide — whether the live competition design owes the two gates' CONCERNS —
   as a phase-3 fix-plan input under **D-231**. **The retirement map is untouched**, as the ruling
   requires.
7. **Ruling 35(a) — the evidence document's banner corrected**, one region: RESOLVED is now scoped to
   the anchor case it verified, with a marked second block stating what the word does not cover and
   pointing at [[OI-363]]. Nothing above it is withdrawn, because both halves are true as written.
8. **Ruling 35(c) — recorded on [[OI-363]]'s row**: the qualitative characterizations are
   ACCEPTABLE as direction-without-value statements and are **not re-edited**. The row also records
   that 35(a)'s edit is performed and that the row nonetheless stays OPEN, because the per-case
   reading it gates on was never the banner.
9. **The registration queue extended over Rulings 24–35**, by the same derivation that built it,
   each ruling classified from its own text with both carriers read whole (**D-643**).

**★ THE EXTENSION IS A NEW SECTION RATHER THAN AN EDIT OF THE RULED ONES, and that is deliberate.**
The queue's §1–§6 record verdicts the user has ruled and the ten entries written under them. Weaving
twelve new rulings into those tables would put ruled and unruled verdicts in one surface with nothing
distinguishing them. **§7 carries its own tables, its own tally and its own proposed homes, and says
in its banner that it awaits the user**; the only change above it is one banner line pointing at it.

**★ SEVEN OF THE TWELVE ARE PROPOSED AS DECISIONS, AND THE SHAPE HAS ONE NEW FEATURE WORTH THE
USER'S ATTENTION.** The first twenty-three exposed a pattern: the rulings that BIND are clauses that
rode ALONGSIDE licences, not the licences that unblocked the most work. That holds again — a
condition attached to a correction (25), a form attached to a refusal to decide (27), a completeness
test attached to a scanner licence (31). **What is new:** three of this batch (**28**, **30**,
**33**) are standing rules ruled AS standing rules, and all three come from the one sitting whose
subject was the writing standards themselves rather than a batch of work. **Three are flagged as
reasonably downgradable**, each with its downgrade reading in one line.

**Holds:** §1.11 — Rulings 20–23 are in no queue, reported rather than classified.
**Surfacings:** none new bearing on the analysis. Every subject of this task is the record's own
bookkeeping, the writing standards, and one register cell whose subject is legacy code unreachable on
either production surface.

**Guards at the task boundary.** The full set was re-run and the classification re-run after it,
which is the order its own STOP requires. **Eight derivations went stale by this task's own edits and
were regenerated, not repaired** — the completion inventory, the finish line, the gate partition, the
apparatus declaration, the legacy-mark verification, and the three item-1 views — and the set is back
at **ZERO failing**. Every verdict is at `tools/audit/guard_state.json` → `summary` and none is
restated here (**D-431**).

**Three authored inputs were maintained, each caught by its own tool's STOP rather than by a reader.**
The kind-list insertion shifted three anchors in the template and they were re-aimed per the tool's
own reported lines; the legacy-mark verification's recorded-figure citation moved by one line when the
[[OI-365]] row was inserted above it, and was re-aimed the same way; and the apparatus declaration
STOPPED because [[OI-364]] reached its first cut with no authored verdict. All three are the
authored-input maintenance class **D-648** names, not mechanism changes.

**★ THE APPARATUS VERDICT AUTHORED FOR [[OI-364]] IS NON-GATING, WHICH IS THE FIRST TIME THIS ARC HAS
AUTHORED ONE, AND THE GROUND IS STATED BECAUSE OF THAT.** The rule the record enforces is that a
non-gating verdict is never HAND-ADDED for a row the cut did not reach — and this row the cut DID
reach, which is the case the tool requires an authored verdict for. The verdict is NON-GATING because
all three owed checks read a document's own STRUCTURE and no measurement of the analysis depends on
any of them; it is classified WITH [[OI-297]] and APART FROM [[OI-292]], and the difference is
written at the verdict itself. **The clause that would override the criterion was checked and does not
engage:** nothing here is a published rate or a trusted instrument awaiting establishment — the
establishment #19 would require is owed BY the check if it is ever built, which is a condition on a
future act and not an obligation standing now. That is the same distinction that puts [[OI-359]] on
the gating side, where the missing mechanism enforces a MEASUREMENT convention.

**★ ONE VOCABULARY ADDITION WAS MADE TO A TOOL'S AUTHORED INPUTS AND IS REPORTED RATHER THAN SLIPPED
IN.** D-580's transfer cell could not be recorded truthfully in any of the seven values the
verification tool's vocabulary carried: `none-found` reports a SEARCH result where this is a ruling,
`explicitly-not-transferred` asserts the decision does not bear on the live design where the ruling
leaves exactly that open, and `undetermined` says the evidence does not settle it where it now does.
An eighth value — *scoped to an act that never ran* — was added with its definition, its date, and
the reason each of the other three misstates the ruling. **It is used by one entry, it changes no
other verdict, and the tally that counts entries bearing on live work does not include it**, which is
correct: the ruling scopes the carve-out to an act that never happened and routes the surviving
question to a row.

**★ THE SAME INSTRUCTION AS THE THREE PREVIOUS CONTINUATIONS COULD NOT BE PERFORMED, AND IS NAMED
RATHER THAN QUIETLY DROPPED.** This dispatch's own file is not staged: `cc_instruction_*.md` is
matched by this repository's `.gitignore` — the class's standing state, established by an earlier
continuation at the git objects — and forcing it in would override a standing repository
configuration decision, which is not a session's to take. The ruling record
`cowork_rulings_2026_08_09_fifth_stop.md` is not matched and IS staged.

**★ THE STANDING SELF-CHECK (D-434) CAUGHT TWO RESERVED-WORD COLLISIONS IN THIS TASK'S OWN NEW PROSE
AND BOTH WERE CORRECTED BEFORE THE COMMIT:** the bare non-musical *figure*, twice in one sentence of
the queue extension — in, of all places, the row arguing that a value belongs in its artifact — and
the bare non-musical *part* in a new detail file. They are *value* and *clause* now. **This is the
fourth consecutive wave whose self-check has caught a reserved-word collision in its own new text**,
which is worth the user's attention as evidence about the rule rather than about any one wave: the
collisions arrive by matching the surrounding prose's idiom, which is exactly the mechanism
[[OI-229]]'s scanner is licensed to make visible.

**Freeze respected:** no `src/` change, no golden, no corpus of scores, no `tools/corpus/` or
`tools/robust_stop/` movement, no behaviour change to the analysis, no fix to inference, no design.
**Phase 1's completion statement is not written, not drafted and not partially written here.**

### Task 1 — COMPLETE. Ruling 33 executed: the canonical status discipline lands, all three rows flip, and the pass found a FOURTH member of the family

**A1 HOLDS, and it was checked by the pass rather than asserted before it.** The both-ways table
decided every index row under BOTH rules — the rule live at HEAD (the resolved mark anywhere in the
status cell) and the canonical-token rule — and **the only state movements are the two the ruling
named**, each named in advance with its target state written down before the pass ran. Any other
movement is a STOP the tool raises, and it did raise one, which is how the fourth member below was
found.

**★ THE BEFORE HALF IS READ FROM A GIT OBJECT BY EXPLICIT HASH, AND THAT IS THE DESIGN DECISION
WORTH READING.** A both-ways pass that took its own before half from the working tree could be run
exactly once: the second run would report the tree it had itself just changed and destroy the record
it exists to keep. The previous continuation's pass had that shape, and this session **overwrote it
by accident** within minutes of starting — see the self-check note below. So this pass reads the
baseline from the commit before it, as a content-addressed object, which is the sanctioned form of
shell read (**D-253**) and makes the record RE-DERIVABLE instead of one-shot.

**What was built, and where the one definition lives (#6).**

1. **`tools/audit/index_status_lint.py`** owns the canonical vocabulary, the row split and the
   leading-token function, and is the STANDING check: it reports every non-canonical opening and
   every row that does not split. It is in the guard population with its authored invocation.
2. **The ONE index parser** — `gen_nongating_apparatus_rows.parse_rows`, which every derivation over
   the register imports — now reads a row's state THROUGH that function rather than re-implementing
   the test, and **STOPS** on a malformed row or a non-canonical opening instead of skipping.
3. **`tools/audit/gen_index_status_normalization.py`** is the one-off pass and its record: the
   survey the vocabulary was derived from, the both-ways table, the named corrections, and the
   authored readings.

**★ THE VOCABULARY IS DERIVED AND DELIBERATELY SMALL, AND THE SURVEY IS WHY.** The survey reported
every opening the index actually used, and what those openings carry is two things: the resolved
mark, and a handful of open-state words. So the vocabulary is **the mark at the head of the cell**
(whatever word follows it — the index uses more than a dozen, and enumerating English past
participles would be inventing a vocabulary rather than deriving one) **plus six open-state words**.
Everything else is a date, a decorative marker or a sentence.

**The normalization is PREPEND-ONLY with one stated exception.** A cell already opening canonically
is untouched; a cell with no canonical opening gains the token as a prefix and loses no text (#12).
**The exception:** where a cell opened with an open-state word that contradicts the state the row
actually holds, that stale token is REPLACED rather than prefixed — prefixing would have produced a
cell reading *"RESOLVED — OPEN — …"*. Every such row is named with an authored reading, and none of
them moves state.

**★ THE FOURTH MEMBER OF THE FAMILY, FOUND BY THE PASS AND NOT LOOKED FOR — AND IT CORRECTS THE
PREVIOUS CONTINUATION'S READING OF THE SAME ROW.** [[OI-208]]'s status cell OPENS with a stale
`OPEN —` and its own closing words say *"the row's purpose is achieved and it CLOSES"*. So the
opening and the prose disagreed about that row's own state. The previous both-ways pass had read
that row's mark as *a delivered half inside a row that is open*, making it **the one row Ruling 25's
refuted remedy improved**. Read at the cell, that reading is **REFUTED**: the row is resolved, the
rule at HEAD read it correctly, and the leading-token remedy would have marked it open too.
**That makes the refuted remedy worse than it was recorded to be, not better** — it would have
marked three genuinely closed rows open and improved none. The correction is written at
[[OI-356]]'s own detail file and in the pass's artifact, with its ground.

**★ AND THE ROW THAT WAS BEING DROPPED IS NOT WHAT ITS OWN ROW SUPPOSED.** [[OI-362]] records the
dropped row as carrying an unescaped cell separator in its prose. It does not. **[[OI-321]]'s
LAYER/GATE COLUMN WAS WRITTEN TWICE**, the second copy holding its gating clause, giving seven cells
— a row edited by two acts that did not see each other, which is a different thing to watch for than
a typing slip. The duplicate is merged into the status cell with its whole text preserved (#12). The
row's state did not move; what changed is that it is COUNTED. It reached the apparatus declaration's
first cut for the first time and a **GATES** verdict was authored for it, on the ground its own text
already carried in words.

**The order [[OI-362]] insisted on is honored rather than reversed:** the silent-skip STOP is in the
same commit as the repair, and the population movement is accounted for by the pass that names it in
advance — which is what that row asked for and what it forbade being slipped in unremarked.

**[[OI-356]], [[OI-361]] and [[OI-362]] all FLIP**, each with its dated detail-file note, and each
records what the flip does NOT withdraw. **Two things are retired by the fix and said plainly rather
than left to be inferred:** OI-356's working convention — name another row's resolved status in
words, never with the glyph — is no longer load-bearing, since a mention anywhere in a cell is now
inert; and OI-361's third candidate is still **NOT SETTLED**, taking the token MIXED, which the
parser reads as OPEN, the state it already held.

**Guards.** The full set was re-run at the boundary and the classification after it. **Cleared and
regenerated by this task's own edits:** the apparatus declaration, the completion inventory, the
finish line, the gate partition and the legacy-mark verification — whose citation to a recorded
value was re-aimed TWICE in one session, once per insertion above it, which is authored-input maintenance
(**D-648**) and is recorded in its own comment. The set stands at **ZERO failing**, now with
**thirty-six** guards rather than thirty-five: the new lint joined the derived candidate population
and the runner STOPPED until its invocation was authored, which is that derivation working.

**★ THE STANDING SELF-CHECK CAUGHT AN ACT OF THIS SESSION'S OWN THAT WOULD HAVE DESTROYED A COMMITTED
RECORD, AND IT IS REPORTED BECAUSE THE NEAR-MISS IS THE LESSON.** Early in the session
`gen_oi356_parser_correction.py` was invoked with `--help`; it takes no arguments, so it RAN, and it
overwrote the committed point-in-time record of the refuted remedy with a fresh measurement at a
tree that had changed. **Nothing was committed with it** — the file was restored from HEAD and the
diff enumerated to confirm the tree was otherwise clean. Two things follow and both are acted on
here: a point-in-time record whose before half comes from the working tree is one accidental
invocation away from being lost, which is why THIS pass takes its baseline from a git object; and a
generator with no argument parser treats every flag as no flag.

**Holds:** none new. **Surfacings:** none bearing on the analysis — every subject of this task is the
open-items index's own parser and the record's own bookkeeping.

**Freeze respected:** no `src/` change, no golden, no corpus of scores, no `tools/corpus/` or
`tools/robust_stop/` movement, no behaviour change to the analysis, no fix to inference, no design.
**Phase 1's completion statement is not written, not drafted and not partially written here.**

### Task 2 — COMPLETE as a MEASUREMENT and a STOP. The completeness question is ANSWERED; neither derivation is both sound and bounded, and no check is adopted

**A2 HOLDS in every part, and one of its clauses turned out to be the finding.** The musical
vocabulary is derived from in-repo sources only — the analysis code's own domain surfaces crossed
with the two music-theory documents. **The external glossary leg is ABSENT and is STATED rather than
silently substituted:** this repository vendors no music-theory glossary, and importing one would
put an unestablished list under load (#19). The seed is `CLAUDE.md`'s twenty, **parsed from that
document's own list rather than typed into the tool**, so a wording change there is a STOP rather
than a silently smaller seed. Separation was measured before anything could guard, and it is
negative, so the artifact is advisory and says so.

**★ TWO DERIVATIONS WERE COMPUTED AND BOTH ARE PUBLISHED, BECAUSE THE COMPARISON IS THE RESULT.**
The SHARP surface is every `enum` in the analysis code — its name and its enumerators — crossed with
the music-theory documents: an enumeration is where a program writes down the categories its domain
actually has, which for this module are the chord qualities, the modes, the degrees, the cadence
kinds and the interval classes. The BROAD surface is every word inside any identifier, crossed with
the same documents.

- **The SHARP derivation is not SOUND.** It misses seed words the user's own inventory names, and
  one of them is a collision this project's standing self-check has caught in its own prose more
  than once. A derivation that misses a known positive cannot be trusted to have found the unknown
  ones.
- **The BROAD derivation is not BOUNDED.** It reaches all but one seed word and buys that with a
  population an order of magnitude larger, dominated by ordinary English that happens to appear on
  both surfaces.
- **One seed word is missed by BOTH**, which is the sharpest single result: the record is not a
  subset of the derivation either.

**So the completeness question is ANSWERED rather than closed.** The inventory is not complete
relative to either derivation; the derivation is not complete relative to the record; and *complete*
now means complete relative to a NAMED derivation **whose measured miss rate against the seed is
part of its name**. That is what makes the claim checkable instead of asserted, which is exactly
what Ruling 31 asked for.

**★ NO CHECK IS ADOPTED, AND THE REASON IS A MEASUREMENT RATHER THAN A PREFERENCE.** Ruling 31
permits a diff-time check ONLY on measured clean separation. **There is none to measure at the level
a check would fire:** the population says which WORDS deserve a ruling, not which USE of a word is
the non-musical sense — the semantic judgment Ruling 32 closed the neighbouring limb over. A check
built on this population would fire on every legitimate musical use of every word in it, which is
precisely the mis-firing **D-473** refuses and **D-436**'s third condition measures. **Nothing was
tuned:** narrowing the population until it stopped firing would be fitting the signal to the cases
that motivated it (DT-2), the same trap the previous continuation's consistency check reported
rather than adjusted.

**★ THE PER-CANDIDATE VERDICTS ARE NOT AUTHORED, AND THE STOP IS ARMED RATHER THAN QUIETLY
SKIPPED.** Every derived candidate must carry an authored verdict — collision,
non-collision-with-reason, or structural case — and the tool exits nonzero while any remains. **The
advisory inventory is written anyway**, so the STOP is a headline rather than a silent nothing:
that is the lesson the rule-triage tool's own history argued for, where a tool that stopped wrote no
artifact and a committed count went stale for weeks. Authoring the verdicts is **a named act of its
own** over a population the artifact counts, and it is not a step inside another task.

**The scanner is registered in the guard population as NOT RUN, with the reason stated there** — its
STOP is its headline and it fails by design until the verdicts are authored, and a guard set
carrying a member that fails by design teaches a reader to ignore the set. Its result is on
[[OI-229]]'s row and in its own artifact instead.

**Ruling 30's two-tier test for research-tied names is recorded in the artifact and NOT applied.**
Deciding which candidates are research-tied, and which site is a term's introduction site, is
authorship of the same kind as the verdicts.

**Delivered for the user's batch rulings** at
`ratification_surfaces/cowork_reserved_word_inventory_2026_08_09.md`, which puts three readings
including the cheapest one — leave the inventory at the user's twenty, keep the convention live, and
record the completeness question as ANSWERED rather than closed, the scanner standing as the
evidence and re-run when the tree has grown.

**Holds:** none new. **Surfacings:** none bearing on the analysis. **Freeze respected:** no `src/`
change, no golden, no corpus of scores, no `tools/corpus/` or `tools/robust_stop/` movement, no
behaviour change to the analysis, no fix to inference, no design. **Phase 1's completion statement
is not written, not drafted and not partially written here.**

### ★ WHERE THIS BATCH STOPPED

**Tasks 0, 1 and 2 are COMPLETE, committed and pushed** — three commits, each its own task boundary,
each with its full guard run, its classification run after it and its `STATUS.md` pointer entry.
**Tasks 3, 4 and 5 are NOT STARTED.** That is a capacity stop at a clean boundary, not a halt on a
finding: no STOP note was written against the batch, nothing is left half-edited, every derived
surface re-derives, and **the guard set stands at ZERO failing** with thirty-six guards run.

**★ WHY TASK 3 WAS NOT OPENED RATHER THAN OPENED AND LEFT PART-DONE.** Ruling 35(b)'s run is a
MEASUREMENT over a derived population, and a measurement published over some of its population is
the silent cap the standing rules forbid — it would read as describing the arm while describing
part of it. Its output also feeds two rows that bear on the analysis, where a half-run would be
worse than none.

**What a continuing session should know.**

1. **Task 3's population is DERIVED, not carried from here:** the evidence document's own §3 method —
   the notated key signature against the published annotated key, from the corpus metadata — applied
   mechanically to every piece in that file, which is how the previous continuation derived it and
   is a stricter reading of *derived* than transcribing its table. **A3's bounds are the whole of the
   licence:** outputs to `scratch_artifacts/` or a named `tools/audit/` artifact and **nowhere under
   `tools/corpus/`**; the comparison is the SAME tool as the committed-outputs pass; corpus-hash and
   tool-commit stamped (#16); predictions are not required (explorational, #5) but every surprise is
   rowed. **The flag is not optional:** `batch_analyze` runs the legacy pipeline without
   `--joint-inference`, which is the arm the previous pass already measured and not the one this run
   is for.
2. **Task 4's four sub-parts are untouched and each population must be derived fresh:** the
   reach-verdict derivation over the apparatus-classed documentation rows (**D-639**'s test, its
   three worked examples ARE the test, fallback (1A) applied and SAID where the test does not decide,
   no hand verdicts, the method being the existing first application's shape); the section-unreached
   and findings-not-rules re-homes; the session-executable gating rows; and **Ruling 16's sibling
   sweep with its ONE comment-only `src/` commit** (sweep first, generated; diff verified
   comment-only; a sibling whose falsity needs judgment about the analysis is HELD, not edited;
   [[OI-353]] flips on it). **No `src/` file was opened for editing by this batch.**
3. **Task 5's OI-346 marks are not reached.**
4. **Three things await the user, and two are new:** the registration queue's **§7**, covering
   Rulings 24–35 with seven proposed decisions and three flagged downgradable; the **reserved-word
   inventory** reading surface, which puts three readings including the cheapest; and, standing from
   the previous batch, the D-580 surface's remaining UNSETTLED items — now partly answered, since
   Ruling 34 settled the conflict and [[OI-365]] carries what it did not decide.

### ★ THE REMAINING-DISTANCE TRIAGE THE USER ASKED FOR — AUTHORED, AND LABELLED AS SIZING

**This is SIZING, not measurement.** Every population it speaks about is derived at
`tools/audit/phase1_finish_line.json` and **no population or count is carried here** (**D-431**).
What is authored is the *kind and size of act* each remaining item needs, in the four labels the
user named. A size is a judgment about work and can be wrong; a population cannot.

**★ IT IS AT ITEM GRANULARITY, NOT ROW GRANULARITY, AND THAT IS A SHORTFALL STATED RATHER THAN
HIDDEN.** The user asked for each remaining GATING ROW sized. Sizing a row honestly means reading
that row — its own text is what says whether the act is a sentence or a study — and the batch
stopped on capacity before that pass. **What is delivered is the finish line's own nine items, which
is the granularity that actually decides scheduling**; the per-row pass over the gating set is named
here as owed and is one session's work on its own.

| Finish-line item | Sizing | Why that size |
|---|---|---|
| Register entries whose home document is named in **no** user-ratified surface | **NEEDS-RULING**, then session-large | The closing act is one of two and only one of them is a session's: the user writes a delegation naming the document — rule (g) reserves that act — or every entry is re-homed into the owning layer's specification. Until the user chooses, no session can start; after (ii) it is a per-entry homing pass |
| Entries whose home is named only in a form the delegation bar excludes | **NEEDS-RULING**, then session-large | Same fork, same reason. The bar (**D-432**) decides the classification; what to DO about it is the user's |
| Entries whose admitting delegation does not reach the section they sit in | **SESSION-LARGE** | The record already rules out the delegation route in its own words, so the act is a re-homing per entry — bounded, mechanical in shape, large in count |
| Entries the delegation reaches, in a section that records FINDINGS rather than stating rules | **SESSION-LARGE** | Per entry, write the rule into a section that STATES it. Rule (e) prefers that over rewriting the finding-recording section, so the fork is already decided |
| Entries with no home at all — recorded only on an archive | **SESSION-LARGE** | Per entry: write the decision into the specification that owns its subject, leaving the archive text in place (#12). This batch's predecessors did nine of these and the shape is established |
| Entries whose defense the record does not state | **CLOSED** | The population reads zero. Recorded here because a distance map that listed only what remains would misrepresent the position |
| Open rows asserting a specification states something false at HEAD, which GATE | **REAL-WORK**, mixed with needs-ruling | The largest item and the least uniform: rows differ widely, and several are user rulings rather than session work — the finish line names which. Some are a sentence; some are a correction that needs a judgment about the analysis, which phase 1's TRUE half puts on the gating side |
| Open documentation rows classed apparatus, whose place inside the doc-sync half **D-639**'s test has not decided | **SESSION-SMALL** | ONE generated derivation over a derived population, with fallback (1A) applied and SAID where the test does not decide. It is Task 4's first sub-part and it is small because the method already exists and no verdict is hand-written |
| Phase 1's completion statement | **NEEDS-RULING** | It is not a session's act at all: every item above must close first, and **the user commissions it**. This batch has not written, drafted or partially written it |

**★ AND THE HONEST HEADLINE OF THE SIZING, said once rather than left to be assembled from the
table:** what remains is dominated by **per-entry homing work whose fork is a user ruling**, not by
investigation. Three items cannot start until the user chooses between a delegation and a re-homing;
one item is a single generated derivation; one is closed; and the largest is a mixed population where
the session-performable half and the ruling half are already named apart. **Nothing in the remaining
distance is blocked on a measurement of the analysis** — the two rows that bear on the analysis
([[OI-357]], [[OI-363]]) are surfaced, rowed and explicitly not proposed for.

**Phase 1's completion statement is not written, not drafted and not partially written by this
batch** — and none of the above is a claim about how close it is: the finish line's own count of what
remains is derived at `tools/audit/phase1_finish_line.json` (**D-431**).

---

# ═══ THE SIXTH RETURN CONTINUATION (dispatch `cc_instruction_return_continuation_6.md`, 2026-08-09) ═══

> Rulings 36–38 of `cowork_rulings_2026_08_09_sixth_stop.md` are applied here, and the fifth
> continuation's unstarted Tasks 3–5 are resumed. The sections above are earlier batches' and are
> not rewritten. New holds are appended to §1, new surfacings to §2, and each task's log below.

## 3 (continued). Per-task log — the sixth return continuation

### Task 0 — COMPLETE. The §7 register event: seven entries written, the 20–23 gap closed by the user's own reading, Ruling 37 recorded at both its subjects and Ruling 38 at the route machinery

**The start state was derived at the artifacts before any act (A5), not carried from the dispatch.**
The full guard set was run unchanged before the first edit and came back at **ZERO failing**, which
is where the fifth continuation left it and what the committed `tools/audit/guard_state.json`
records; the queue's §7, the two rows this task writes to and the register's highest identifier
were each read at their own surfaces. No count is restated here (**D-431**).

**A1 HOLDS, and it was checked at each home before the first entry was written.** The rule (h) kind
half asks whether the receiving section STATES RULES. `cowork_audit_protocol.md`'s dispatch-protocol
block does, in its own opening, and every existing subsection of it states one rule with its ruling
and its defense; `CLAUDE.md`'s Conventions block and its open-items register section likewise, the
latter stating its rules as a lettered list this act adds to; and
`cowork_design_doc_template.md`'s kind-list section states a binding scope, a maintained membership
list and a STOP. **No home failed its check, so the STOP the assumption reserves did not fire.**

**What was done, in order.**

1. **Ruling 36 — SEVEN entries at the homes §7.4 proposes**, four in `cowork_audit_protocol.md` and
   one each in `cowork_design_doc_template.md` and — under the ruling's own scoped licence — two in
   `CLAUDE.md`. Each is written in the receiving section's own voice with its defense, provenance in
   the register fields and never in the governing text. **The three entries §7.3 flagged as
   reasonably downgradable are KEPT**, as the ruling directs. **★ NO NEW ENTRY CARRIES AN
   ENTRY-RATIFICATION EVENT, and each says so:** the user ruled the CLASSIFICATION and the HOME, and
   the entry text was written afterwards, so recording one would be the session ratifying its own
   writing (#14). **The seven exercises are recorded as confirmed** in the queue's second closing
   state and carry no entry, which is what an exercise verdict means.
2. **The Rulings 20–23 gap CLOSES, and it closes in the reading §7.3 declined to take.** That
   section reported the gap, stated the on-its-face reading — each of the four is the RATIFICATION
   EVENT a queue exists to obtain — and deliberately did not take it, because classifying four
   rulings the dispatch had not sent would be a session widening its own scope (**D-654**). Ruling
   36 takes exactly that reading. **The refusal is what produced the answer**, and the queue's
   closing state says so rather than presenting the outcome as though the reading had been obvious.
3. **The queue is re-bannered FULLY RULED** and gains **§8**, its second closing state, in the same
   shape §6 uses for the first. **Nothing above §8 is altered** (#12) — §1–§6 stand as the user
   ruled them and §7's verdicts and grounds stand as they were put.
4. **Ruling 37 — recorded at BOTH its subjects**, which is what the ruling names: [[OI-229]]'s index
   row and detail file, and the scanner artifact's own closing state, written into the generator so
   it re-derives rather than being pasted into the output. The outcome is READING 3 — the
   completeness question is **ANSWERED and recorded, not closed** — and the answer is now the
   standing statement of what *complete* means here, carried as register entry **D-661**. The held
   seed-only batch is **named as HELD and explicitly not scheduled** at both sites.
5. **Ruling 38 — recorded at the finish-line route machinery**, in two places because the fork is
   stated in two: the finish line's own closing acts for the two homing items, and the per-entry
   route table. **The former closing acts are preserved whole (#12)** rather than replaced, so a
   reader comparing artifacts sees what the ruling changed.

**★ WHAT RULING 38 MOVED IN THE ROUTE TABLE, AND THE ONE CLASS IT DELIBERATELY DOES NOT REACH.**
Every OPEN row whose AUTHORED route was *needs a delegation* now carries route **RE-HOME**, with the
authored route preserved beside it and the ruling named on the row; rows already routed re-home
carry the ruling confirming that their authored route agreed. **The `NO HOME EXISTS` class is NOT
moved, and the reason is written at the tool rather than left to be inferred:** those rows do not
record a choice between a delegation and a re-home — they record that NEITHER applies, because the
entry's live content is carried by a homed successor and re-homing would put a second copy of a
homed rule (#6), or because there is no decision content to write at all. **Ruling 38 settles which
of two AVAILABLE routes is the default; it says nothing about #6 and creates no route where the
record says there is none.** That class stays dispositioned under **D-642** where it already was.
**The exception list is EMPTY and that is the RULED state, not an unfilled field** — a session may
not except a document, and a later exception is a new user ruling naming the document, taken BEFORE
its entries are re-homed.

**★ ONE THING THE SCANNER'S REGENERATION SHOWED, and it is the rule working rather than a defect.**
Re-running the scanner after this task's own writing moved its derived candidate counts: the new
`CLAUDE.md` and `cowork_audit_protocol.md` text is governance prose, so it enters surface (b) and
the derived population grows with it. That is precisely what *re-derived as the tree grows* means in
**D-661**, and it is why the artifact is the evidence for the completeness answer rather than a
one-time verdict. Every value is at `tools/audit/reserved_word_scanner.json` and none is restated
here (**D-431**).

**Three authored inputs were maintained, each caught by its own tool's STOP rather than by a
reader.** The `CLAUDE.md` rule triage STOPPED the moment the two new `CLAUDE.md`-homed entries
landed — the shape that tool's own reading file states in general terms, since every homing wave
into that document adds a member and cannot supply its own verdict. **Verdicts were authored for
both, with their grounds:** the canonical status discipline is **MECHANISM-EXISTS**, because the
lint and the parser STOP were built in the act that ruled it; the research-term rule is
**KNOWLEDGE**, because its antecedent is authorship twice over — which terms are research-tied, and
which site is a term's introduction site — and the derived population that would supply the first is
measured neither sound nor bounded. **Neither verdict enters the defect class, and the defect set
does not move.** The classifier's own apply moved four derived fields, all of them delegation line
citations shifted by this task's insertions into `CLAUDE.md`; regenerating them is completing an
edit, not repairing a finding.

**★ AND THE THIRD IS A CARRIED-FORWARD ONE THIS TASK DID NOT CAUSE, which is why it is named rather
than folded in.** The GUARD CLASSIFICATION — run after the guard set, which is the order its own
STOP requires — stopped on **two tools the PREVIOUS continuation added**: the index-status lint and
the reserved-word scanner. Neither had an authored verdict, and the classification is not a member
of the guard set, so nothing in that set's zero-failing state reported it. Verdicts were authored
for both with their evidence: the lint is **LIVE**, parsing the index on every run and asserting a
property of it as it stands; the scanner is **LIVE DESPITE BEING REGISTERED NOT RUN**, on the
`claude_md_rule_triage.py` precedent — its population is derived from the tree and its STOP fires on
exactly that — with the two facts kept apart, since *not run* is a decision about the guard set and
*live* is a statement about what the tool asserts. **The shape is worth a reader's attention:** a
check that is deliberately outside the set it checks reports nothing when the set is green, which is
the third instance in this arc of a STOP that only fires when something else has already been made
to run.

**Holds:** none new. **Surfacings:** none new bearing on the analysis — every subject of this task
is the record's own bookkeeping and the rulings that govern it.

**Freeze respected:** no `src/` change, no golden, no corpus of scores, no `tools/corpus/` or
`tools/robust_stop/` movement, no behaviour change to the analysis, no fix to inference, no design.
**Phase 1's completion statement is not written, not drafted and not partially written here.**

### Task 1 — OPENED AND PARTLY DONE. Three of the twenty-eight re-homed, each complete in itself; this is where the batch stops, and it stops on capacity

**The population was derived fresh at task start (A2, A5)** from `tools/audit/phase1_finish_line.json`
and the route artifacts, not carried from the dispatch or from this file. It is the four homing
items the dispatch names, and the dispatch's own partition of it holds: the no-ratified-surface
class, the bar-excluded class (empty at HEAD), and the standing seventeen — the section-unreached
four and the findings-not-rules thirteen. **No count is restated here (D-431).**

**★ RULING 38 SPLITS THE FIRST ITEM IN A WAY THE DISPATCH DID NOT ANTICIPATE, AND THE SPLIT IS
DERIVED FROM THE ROUTE TABLE RATHER THAN JUDGED.** Of that item's entries, those whose AUTHORED
route was *needs a delegation* are the ones the ruling converts to a re-home. The rest carry
`NO HOME EXISTS`, and **Ruling 38 does not reach them** — they record that NEITHER route applies,
because the entry's live content is carried by a homed successor and re-homing would put a second
copy of a homed rule (#6), or because there is no decision content to write at all. The reasoning
is written at the route generator itself and not only here.

**★ AND THE ELEVEN CONVERTED ENTRIES ARE NOT ALL THE SAME SHAPE, WHICH IS THE FINDING A CONTINUING
SESSION NEEDS BEFORE IT STARTS.** Nine of them name `cowork_score_census.md` as their own owning
surface and two name `cowork_audit_protocol.md` — that is, **their recorded owner IS a document
with no delegation.** For the two audit-method entries the act is the one this batch performed
seven times at Task 0: a `process`-kind homing into the audit protocol, which leaves the gap class
by construction and needs no delegation. **For the nine corpus entries it is not obvious that
re-homing into the census closes anything**, and choosing a different surface would be a judgment
about where a corpus decision is owned. **They are HELD, not sited**, and the candidates the record
itself names are `cowork_score_census.md` (their recorded owner) and `CLAUDE.md` gate block (A),
which already carries the corpus rules the census states from the other side. **Nothing is decided
here** — the standing homing discipline is that an entry whose owner is not determinate is held
with its candidates named.

**What was done, and why these three.** They are the section-unreached item's voice-leading
members, whose delegation question the user RULED CLOSED on 2026-08-04 — which is what makes them
the cleanest members of the whole population: the finish line's own gate note draws the split this
task turns on, that **the delegation question is closed and the ENTRIES are not.**

1. **D-400 → `ARCHITECTURE.md` §2.15's span typology, THE SECTION THE ENTRY'S OWN TEXT NAMES.** Its
   ask says in terms that the per-voice span kind is admitted *into ARCHITECTURE §2.15*, so nothing
   is sited by judgment. **The propagation it recorded as riding the build had never happened:** the
   typology carried no per-voice member, so a phrase-segmentation design written against the
   catalogue would have found every span kind tiling the whole texture. The home text carries the
   rule, its defense — phrases in contrapuntal writing are concurrent and out of phase across voices
   — and the thing the record deliberately does NOT assert, that consecutive phrases within one
   voice tile it exactly.
2. **D-397 → `ARCHITECTURE.md`'s growth-by-axis paragraph**, as four ownership CLAIMS in plain
   words, each with the record's own condition that a claim is discharged only at that component's
   ratified design. **The component code names are deliberately not carried into the architecture
   text** — a reader there meets an object rather than an identifier, and the identifiers live in
   the axis design that section delegates to (#6).
3. **D-398 → `cowork_voiceleading_axis_design.md` §0**, a section the EXISTING delegation already
   reaches, at the motion-types bullet whose undecided word it settles. **This one is also a
   doc-sync correction (C3):** that bullet closed by calling the reading *an implementation
   declaration owed at build*, which is false at HEAD. The former wording is preserved in place
   (#12) and the §15 tracking line is untouched.

**In all three the delegation is untouched.** No delegation was written or widened, §15 and §16 are
still not named, and the 2026-08-04 home-class rulings are preserved whole at each entry and
explicitly NOT withdrawn: they settled the DELEGATION question, and this act settles the ENTRY.

**★ ONE AUTHORED INPUT RETIRED AND ONE AUTHORED, both under their own tools' STOPs.** The
class-C delegation DRAFT for the voice-leading design was moved WHOLE into a retired block with the
reason it retired (#12, D-648): the document left class C because its three class-C entries did.
**The draft's own recommendation is the route that was taken** — leave the delegation as it stands
and home those decisions where their concerns are owned — so the retirement discharges it rather
than overriding it. And the classifier STOPPED because the §0 homing made a subsection hold a
register entry for the first time; a **states-rules** judgment was authored for it with its ground,
that every bullet there FIXES the operational meaning a term carries wherever the axis's
specifications use it, which is a binding definition and not an observation.

**★ THE LAYERED-STOP SHAPE APPEARED FOR THE FOURTH TIME IN THIS ARC AND IS REPORTED RATHER THAN
ABSORBED.** The legacy-mark verification reports only its FIRST failing anchor, so **seven anchors
had to be re-aimed one run at a time**, each from the tool's own reported line and never by an
assumed uniform shift. Every one is authored-input maintenance (D-648) and no verdict, mark, status
or home moved with them. The general point is worth a reader's attention: **a cleared STOP is never
evidence about what follows it**, and only a single green run is.

**★ WHERE THE BATCH STOPS, AND IT STOPS INSIDE TASK 1 ON CAPACITY.** The dispatch permits a stop
partway HERE and states the reason it is safe: unlike a derivation, a per-entry pass has no
silent-cap hazard, because each homed entry is complete in itself. **Nothing is half-edited** —
every act on disk is whole, every derived surface re-derives, and the guard set stands at ZERO
failing with the classification green after it. **Tasks 2, 3, 4 and 5 are NOT STARTED**, and none
of them was opened and abandoned.

**What a continuing session should know.**

1. **The remaining population is DERIVED, not carried from here:** the four homing items at
   `tools/audit/phase1_finish_line.json`, read at task start. The three closed here are already out
   of it by construction.
2. **The eleven-entry split above is the first thing to settle**, and nine of those eleven need a
   decision about where a CORPUS decision is owned — which is a judgment, not a filing act. The two
   audit-method entries are executable now, by the Task-0 pattern.
3. **The findings-not-rules thirteen are untouched.** Their closing act is stated at the finish
   line: write the rule the entry records into a section that STATES it, in the specification that
   owns the concern — rule (e)'s preferred route, and not a rewrite of the finding-recording
   section.
4. **Every homing into `ARCHITECTURE.md` shifts anchors below it**, and three separate tools carry
   authored line citations into that file. The order that reaches a fixed point is: home →
   `reaim_home_anchors.py` → classifier → dispositions → register → the derived views, with the
   legacy-mark verification re-aimed one STOP at a time.

**Holds:** the nine corpus entries of the converted eleven, with their candidates named above.
**Surfacings:** none bearing on the analysis — every subject of this task is where a recorded
decision is written down.

**Freeze respected:** no `src/` change, no golden, no corpus of scores, no `tools/corpus/` or
`tools/robust_stop/` movement, no behaviour change to the analysis, no fix to inference, no design.
**Phase 1's completion statement is not written, not drafted and not partially written here.**

---

# ═══ THE SEVENTH RETURN CONTINUATION (dispatch `cc_instruction_return_continuation_7.md`, 2026-08-09) ═══

> Ruling 39 of `cowork_rulings_2026_08_09_seventh_stop.md` is applied here, and the sixth
> continuation's unstarted Tasks 2–5 are resumed. The sections above are earlier batches' and are not
> rewritten. New holds are appended to §1, new surfacings to §2, and each task's log below.

### 1.12 STOP — Ruling 39's ACT is performed and its PREDICTED OUTCOME is refuted: a delegation to the census cannot reach an entry that does not sit in the census (Task 0)

**This is the mechanism working, not a failure.** The dispatch's assumption **A1** states that the
delegation, once written, *"lands the nine as contract-home BY DERIVATION"*, and orders the
assumption checked before the act it licenses. It was checked at the objects, and it does not hold.

**What was performed, and it stands.** The user approved the delegation's wording verbatim, and that
wording is now in `ARCHITECTURE.md`, sited beside the existing §8c naming and supplementing rather
than replacing it. `cowork_score_census.md`'s FORMS grade moved to the explicit-delegation form —
the strongest naming governs, rule (k1) — with the former grade preserved (#12), and its authored
delegation scope moved from `sections` to `document`, the former scope and its section list
preserved beside it.

**What the delegation MOVED, measured rather than assumed: nothing, in either direction.** Every
entry actually homed in `cowork_score_census.md` already sat in one of the seven sections the
earlier section-list naming reached, and every one of those sections already carried a states-rules
judgment — so all of them were `contract-home` before this act and are `contract-home` after it. The
sections the widening newly reaches hold no register entry at HEAD. Established at
`home_classification.json`, whose class totals and `decided_by` split are identical to the committed
ones, read from the git object at the commit before this act; no value is restated here (**D-431**).

**Why the nine did not close, and it is a checkable fact rather than a judgment.** A register
entry's class is decided by **its own HOME DOCUMENT**. The nine name `cowork_score_census.md` as
their **owning specification** — the surface that ought to state their rules — while each is
**homed in a different document**: an architecture review, a full-needs audit, a term-grounding
document, a union-search record and an implementation roadmap. Every one of those five is named in
none of the three user-ratified surfaces, so clause (a) excludes their entries before any delegation
is graded. **A delegation to the census cannot reach an entry that does not sit in the census.**

**So the ruling's two halves come apart.** Its ACT — the census is the owner, the delegation is
written — is performed. Its stated OUTCOME — the nine close by classification, with zero text
movement — is unreachable as worded. Two routes remain and each is one act:

1. **Move each entry's HOME field into the census section that already states its rule**, where one
   does. This is register-data maintenance and it is the only route that is literally the zero text
   movement the ruling names — but it is available only per entry, and only where the census already
   carries the rule, which has to be read entry by entry.
2. **Perform the re-home Ruling 38 makes the default**, writing each rule into the census section
   that owns it. That is the text movement this exception was taken to avoid, and for some of these
   entries the owning section is the needs-vector findings table — which is exactly the kind-half
   STOP Ruling 39 arms.

**The nine are HELD individually**, with both routes named on each row at
`tools/audit/decisions/finish_line_item1_routes.json` and in the queue's §9.4. **Choosing between a
ruling's act and its stated outcome is not a session's act**, which is why nothing was written for
them and no route was picked.

**What is NOT claimed.** That the ruling is wrong, or that the census is the wrong owner. **The
owner question is RULED**, and the record now says so in three places. What is refuted is the
mechanism by which the nine were expected to close.

## 3 (continued). Per-task log — the seventh return continuation

### Task 0 — COMPLETE as an ACT and a STOP. Ruling 39's delegation is written and its predicted close is refuted by measurement; the nine are held individually

**The start state was derived at the artifacts before any act (A5), not carried from the dispatch.**
The full guard set was run unchanged before the first edit and came back at **ZERO failing**, which
is where the sixth continuation left it. The nine entries, their home documents and their classes
were read at `home_classification.json` and at the register data; the route table and the queue were
read at their own files. No count is restated here (**D-431**).

**A1 IS REFUTED, and the refutation is §1.12.** It was checked before the act it licenses, as the
dispatch requires, and the check is what the whole assumption block exists for.

**What was done, in order.**

1. **The delegation was written VERBATIM** — the wording the user approved, that clause and nothing
   else, sited beside the existing §8c naming in `ARCHITECTURE.md` and supplementing it rather than
   replacing it.
2. **The authored FORMS grade was supplied**, moving `cowork_score_census.md` to the
   explicit-delegation form with the former NAMED_SECTIONS grade preserved whole (#12) and rule (k1)
   named as what decides between the three namings the document now carries.
3. **The authored delegation scope moved to `document`** in the register data, with the former scope
   and its section list preserved unread beside it (#12), because that list records which sections
   the two earlier namings reached and by what reasoning.
4. **The classification and everything downstream were regenerated** — classifier, anchors,
   dispositions, register, derived views — and the movement was MEASURED against the committed
   artifact read from a git object by explicit hash (**D-253**'s sanctioned form of shell read).
   **Nothing moved.**
5. **Ruling 39 was recorded at the route machinery**, with its act, its measured outcome and the two
   remaining routes, and with the nine derived from the authored owner string rather than listed by
   hand — so a row that later gains or loses the census as its owner joins or leaves the set by
   itself.
6. **The queue gained §9**, classifying Rulings 36–39 by the same derivation that built §2 and §7,
   each from its own text with both carriers read whole (**D-643**). **One is proposed as a
   DECISION** — Ruling 38's homing default and, load-bearing, its exception mechanism: who may
   except a document, and that an exception taken after the re-homing is void. **Three are proposed
   as EXERCISES**, two with an upgrade reading in one line so reading either the other way costs the
   user nothing. **No register entry is written and no identifier is assigned.**

**★ THE SHAPE §9 EXPOSED IS THE SAME ONE THE THREE EARLIER BATCHES FOUND, IN ITS SHARPEST FORM.** Of
these four rulings the three that unblocked work bind nothing new, and the one that binds is a
clause that rode alongside a routing decision. A register carrying only the headline acts would
carry none of them.

**★ WHY THE DELEGATION WAS WRITTEN ANYWAY, ONCE A1 WAS REFUTED, AND IT IS STATED BECAUSE IT IS A
JUDGMENT.** The refutation is about the ruling's predicted CONSEQUENCE, not about its act. The
wording is the user's own, approved verbatim; the delegation is the user's act under rule (g), which
a session performs rather than decides; and its content — that corpus-content, corpus-tier and
corpus-acquisition decisions are owned by the census, judged per section — is a governance statement
that stands whichever route eventually closes the nine, and is a precondition for both of them. What
a session may not do is pick between the ruling's act and its stated outcome, and that is the one
thing not done here.

**Holds:** §1.12 — the nine, held individually with both routes named. **Surfacings:** none new
bearing on the analysis; every subject of this task is where a recorded decision is written down.

**Freeze respected:** no `src/` change, no golden, no corpus of scores, no `tools/corpus/` or
`tools/robust_stop/` movement, no behaviour change to the analysis, no fix to inference, no design.
**Phase 1's completion statement is not written, not drafted and not partially written here.**

### Task 1 — OPENED. The two audit-method entries are re-homed, each complete in itself; the batch then leaves Task 1 at an entry boundary so that Ruling 35(b)'s run is not starved a third time

**The population was derived fresh at task start (A2, A5)** from `tools/audit/phase1_finish_line.json`
and the route artifacts, not carried from the dispatch or from this file. No count is restated here
(**D-431**).

**What was done, and why these two.** They are the pair the dispatch names first: the members of the
converted eleven whose owning specification is `cowork_audit_protocol.md`, for which the act is the
one the §7 register event performed seven times — a `process`-kind homing that leaves the gap class
by construction and needs no delegation.

1. **D-581 → P2 of `cowork_audit_protocol.md`**, the section that already states this project's
   closed-verdict-set rule. What is written there is the rubric an information-loss sweep classifies
   every site under — **information not yet consumed is NOT automatically a defect**, then the four
   verdicts, with the fourth (**consumer status ambiguous**) recorded for the user's adjudication and
   never guessed — with both halves of its defense: without the first clause a proactive sweep
   manufactures findings, and the fourth verdict is what keeps it honest in the other direction,
   since #1 forbids guessing.
2. **D-583 → the same section, immediately beside it**, because a verdict of *keep, deferred* is one
   of that rubric's dispositions and the two belong in one place (#6). What is written is the general
   CONDITION — the disposition holds only while the thing kept stays characterized exactly, and is
   re-adjudicated the moment its form changes — with the user's own words as its defense and the
   line it draws: a deferral names its future owner AND its exact form, which is what separates it
   from an unexamined defect.

**★ WHAT THE HOME TEXT DELIBERATELY DOES NOT CARRY, AND THIS ONE MATTERS MORE THAN USUAL.** D-583's
record is the general condition; the INSTANCE it was ruled on is a legacy chord-path behaviour that
the joint estimator replaced. Carrying that instance into a live specification would have made a
section stating a general rule read as re-asserting a particular behaviour **that is not on the arm
that ships**. The instance stays in the catalogue that measured it, the LEGACY mark stays on the
entry and is not withdrawn by the re-homing, and the same discipline kept D-581's severity scale and
its named illustrative case out of the specification — those grade a FINDING rather than state the
rubric (**D-431**). **The catalogue's own text is untouched** (#12).

**Two authored inputs were maintained, both caught by their own tools' STOPs rather than by a
reader.** The homing emptied `cowork_information_loss_audit.md`, so the classifier STOPPED on an
authored judgment for a document that is nobody's home and the delegation bar STOPPED on its FORM
grade; both judgments were moved WHOLE into their retired blocks with the reason they retired (#12,
**D-648**), never deleted, and the retirement's own STOP in the other direction is untouched.

**★ AND ONE STOP WAS A REAL FINDING ABOUT THE ROUTE TABLE RATHER THAN A STALE INPUT, so it is
reported rather than absorbed.** Three derivations STOPPED with *"authored routes for entries item 1
does not carry … (the register moved under the table)"*, which is the guard refusing to run while an
authored route and the register disagree. The cause is a seam Ruling 38 created: **the ruling
converts an authored *needs a delegation* into a *re-home* at ROW BUILD, while `ROUTES` keeps the
authored judgment (#12)** — so the executed-check, which reads the authored tuple, could not see
that a re-home had been performed and would have reported a completed act as never having happened.
The two entries are recorded in a fifth per-act table, one table per wave as the four before it are,
and the check reads the RULED route for them with the reason written at the code. **No other
entry's verdict is touched.**

**★ WHERE THE BATCH LEAVES TASK 1, AND THE REASON IS THE DISPATCH'S OWN.** The dispatch permits a
partial stop at an entry boundary here and states why it is safe: a per-entry pass has no silent-cap
hazard, because each homed entry is complete in itself. It also states, of Task 2, that it *"goes
before the derivations this time so capacity cannot starve it again"* — and Task 2's run has now
been carried unstarted through two batches, each time because a large per-entry pass consumed the
capacity first. **So Task 1 stops here, at a clean entry boundary, and Task 2 runs next.** That
ordering is stated rather than done silently, because it is a judgment about which of two
instructions binds harder.

**Guards at the boundary.** The full set was re-run and the classification re-run after it, which is
the order its own STOP requires. **Six derivations went stale by this task's own edits and were
regenerated, not repaired** — the route table, the re-home blocker, the superseded-reach
application, the outstanding-delegation view, the finish line and the completion inventory — and the
set stands at **ZERO failing**. Every verdict is at `tools/audit/guard_state.json` → `summary` and
none is restated here (**D-431**).

**Holds:** the nine census entries of §1.12, unchanged; the remainder of the homing population,
untouched and to be derived fresh. **Surfacings:** none bearing on the analysis — every subject of
this task is where a recorded decision is written down.

**Freeze respected:** no `src/` change, no golden, no corpus of scores, no `tools/corpus/` or
`tools/robust_stop/` movement, no behaviour change to the analysis, no fix to inference, no design.
**Phase 1's completion statement is not written, not drafted and not partially written here.**

## 4. The batch's start state, recorded before any act

**HEAD** is `03bce02e4b` (*"docs(cowork): the standing self-check's own two findings, corrected
rather than shipped"*). The working tree carries the uncommitted document-routes wave.

**The guard set at the start**, taken by IDENTITY from the COMMITTED `tools/audit/guard_state.json`
and not from this session's own run (§2.3). The failing tools were the `CLAUDE.md` rule triage, the
phase-1 completion inventory, the phase-1 finish line, the outstanding-delegation view, the home
classification, the delegation bar, the legacy-mark verification, the item-1 route table, the
re-home blocker, the supersession application, and the live-prohibition pointers. **No count is
given** — every count lives in that artifact's own `summary` (**D-431**); the identities are listed
because they are what lets a later reader tell a new failure from a standing one, and an identity
is not a quantity.

**The two registers:** the decisions register was current — its own check passed, every verbatim
resolved at its cited home, and the disposition verifier reported zero line drift. The open-items
index and its detail files were a bijection.

**What was already known to be owed** and is this batch's queue: the guard family (OI-300, OI-348,
OI-351), the archive-unhomed eleven and D-601, the defense gaps, the reach-verdict derivation, the
section-unreached and findings-not-rules entries, the session-executable gating rows, the OI-349
conformance probe, and OI-346's marks.

**Phase 1's completion statement is not written, not drafted and not partially written by this
batch — even if every item closes, the user commissions it.**
