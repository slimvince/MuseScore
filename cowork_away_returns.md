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

---

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
