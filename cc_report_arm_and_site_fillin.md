# CC report — the ARM and the SITE filled in for the framework document's nine behavioural statements

**Dispatch:** `cc_instruction_arm_and_site_fillin.md` (2026-08-28).
**Outcome:** the batch ran to completion. Task 0 pinned and established; Task 1 wrote the fill-in;
Task 2 judged both sub-fields; Task 3 closed. **The batch BOUND and did not GRADE**, and every
disagreement between a statement and the code is quarantined below, unresolved.

---

## 1. What this batch did, in one paragraph

For each of the framework document's behavioural statements at §10.2 it filled in **sub-field 1 (the
ARM)** — which inference path the statement binds to — and **sub-field 2 (the SITE)** — the code
location it binds to — writing them into **one new file beside the framework document and never
inside it**, `cowork_arm_and_site_fillin_2026_08_28.md`. It then judged whether those two sub-fields
are reachable at all, which is what Ruling 4 of
`cowork_rulings_2026_08_26_framework_opening_sitting.md` sends to a side allowed to read code. **The
framework document was not touched in any character**, and that is proven at the object rather than
asserted.

---

## 2. Every commit and every object identity

| What | Object |
|---|---|
| Tip at Task 0 (read at `.git/refs/heads/master` with the file tool, established at the object) | `6005daecaf9f1a6692e61521911ef8b99ed73b55` |
| — its tree | `0f7c42f3aca978086c06b0d93d08e0f2d565d32e` |
| `origin/master` at Task 0 | `6005daecaf9f1a6692e61521911ef8b99ed73b55` — identical to the tip |
| **Pin: `cc_instruction_arm_and_site_fillin.md`** | blob `82d0fcdcc3153e7b62a731cec1480bcc2650b33c` |
| **Pin: `cowork_framework_document_draft_2026_08_28.md`** | blob `c94f6e59ae5053121ffe4e2966431de431553b08` |
| Task 1 commit | `b5db8fc3d55072d152b04d6e842b1f0baf31672b`, tree `39950e13a6fffa4751d171ba6fe94894cc2fbfe2`, parent `6005daecaf9f1a6692e61521911ef8b99ed73b55` |
| Task 2 commit | `836ad8ba57ab22c89cdcd6a6d85b8fa2a70a2d0d`, tree `39cb14efb7a9862c91aa7e646349d1d4f433024b`, parent `b5db8fc3d55072d152b04d6e842b1f0baf31672b` |
| `tools/audit/evidence_pin_membership.json` before regeneration | blob `de44577a3a713465e76bc95b81c513e605020e08` (at `836ad8ba57`) |
| — after regeneration | blob `565611d4fe6276a495805e6ba1998d98b785600d` |
| Task 3 close commit | `a243a28c975a97123f155096d30b1f89f6622797`, tree `91aa1816d06eca42bd3063530ac5c1087b8ec72d`, parent `836ad8ba57ab22c89cdcd6a6d85b8fa2a70a2d0d` |
| `tools/audit/guard_state.json` before the end-state run | blob `78d59922a6785df62e5590fd4c398de4903f339a` (at `6005daecaf`) |
| — after the end-state run | blob `e5fb6edf7e48ba30f0153785b5f7b85279973b09` |
| The end-state commit | §12 |

**Both commits were verified at the object** with `git cat-file commit <sha>` for the subject and
`git diff-tree --no-commit-id --name-status -r <sha>` for the paths. Task 1 touched exactly
`cowork_arm_and_site_fillin_2026_08_28.md` (added); Task 2 touched exactly that path (modified).
Both were pushed and `origin/master` re-read at the ref after each push.

**★ THE PIN HELD, AND IT WAS RE-PROVEN TWICE.** Both blobs were re-hashed with `git hash-object`
after Task 1 and again after Task 2, and both reproduced their Task-0 identities exactly. So the
framework document is byte-identical to what this batch bound against, **and the dispatch did not
move under the batch** — which is the failure the previous batch met and which this pin exists
against.

---

## 3. E0 — graded

**MET.**

- Both blob identities reported (§2), taken with `git hash-object -w` before either file was read
  for content, and every later read of the dispatch taken from `git cat-file blob <hash>` into a
  scratch file outside the repository.
- The tip established at the object (`git cat-file -t` and `git cat-file commit`), and
  `origin/master` read at its ref beside it — identical.
- The full guard set run in **CHECK mode** before the first act; A2 graded from that run (§6).
- The tree enumerated with `tools/audit/changed_paths.py`; A1 graded from that enumeration (§6).

*One declared departure, at §7.*

## 4. E1 — graded

**MET.**

- One entry per behavioural statement, in order, each carrying fields 1–5, and field 6 only where
  binding surfaced a disagreement.
- **Every site is named by file and by function or type. There is no line number anywhere in the
  fill-in** (**D-307**).
- Every NO SITE carries what was searched — the exact patterns and the carriers opened — so the
  verdict can be re-run.
- The quarantined questions are gathered in their own list at the end of the file, each unresolved.
- **The framework document was proven byte-identical to its pinned blob at the end of the task**, by
  hash.

## 5. E2 — graded

**MET.**

- Both sub-fields judged separately, with the counts **derived from Task 1's own entries** — each
  entry's own sub-field 1 and sub-field 5 read back — and asserted nowhere else.
- P1 and P2 both graded, with the evidence beside each (§8).
- **No disposal is recommended**, and the section states why one may not be: dropping a sub-field is
  a disposal, and the worth test carrying a finding, a date and a reason is the user's act.

---

## 6. A1, A2 and A3 — graded from measurement

### A1 — the working tree by shape: **HELD.**

`tools/audit/changed_paths.py` at Task 0 returned **exactly two tracked modifications** —
`cowork_handoff.md` and `cowork_informed_session_brief_framework.md` — which is the declared shape
(the brief modified; the handoff modified or clean). **There is no third tracked modification, so no
STOP.** The untracked population is large and is not constrained by the dispatch; each of the eight
untracked inputs A1 names by path was confirmed present in the enumeration: this dispatch, the
parked register dispatch, the cross-layer transfer list, the framework draft, the eightieth handoff
entry, the register blocker surface, the rule-(c) suspension, and the 2026-08-28 framework-delta
ruling record.

### A2 — the guard state at the start: **HELD, at the declared start state and not at the assumption's first limb.**

The CHECK-mode run before the first act reported **four failing checks and no others**: the three
known —

- `tools/audit/gen_filing_convention_application.py --check`
- `tools/audit/decisions/apply_soft_discard.py --check`
- `tools/audit/decisions/apply_residue_discard.py --check`

— **plus `tools/audit/gen_evidence_pin_membership.py --check`**, which is exactly the fourth the
dispatch's *declared start state* names and attributes to its own untracked inputs. **A fifth failing
verdict would have been a STOP; there was none.** The run also reported its own staleness against the
committed `guard_state.json`, which records a different failing count — the expected consequence of
the fourth red, not a separate finding.

**The previous batch measured that fourth check GREEN and said so; this batch measured it and carried
neither statement**, which is what the dispatch ordered. Its cause was then established rather than
assumed: the derivation's population is the file system, and
`cowork_rulings_2026_08_28_framework_delta_sitting.md` is an untracked ruling record on disk (§6.4).

**No figure from either guard run is transcribed here (D-431).** The CHECK-mode run writes no
artifact, so its totals are deliberately not carried as values; what is reported is the identity of
each failing check, which is a name and not a figure. The end-state run's summary is cited at its own
artifact in §9.

### A3 — this batch's whole footprint: **FALSIFIED AS WRITTEN, and the movement is reported rather than absorbed.**

A3 states *"No existing file's content is edited by this batch at all"* and makes an edit to any
existing file other than `STATUS.md` a STOP-and-report. **That could not hold, because the same
dispatch's Task 3 orders four acts that each write an existing file.** The measured tracked
modifications at the close, beyond the two pre-existing Cowork-side ones, are:

| Path | The dispatch clause that caused it |
|---|---|
| `STATUS.md` | Task 3 item 1 — the pointer entries. A3 admits this one. |
| `STATUS_ARCHIVE.md` | Task 3 item 1 — `gen_status_batch_bound.py --apply` writes the moved block there; the move is what the forward bound IS. |
| `tools/audit/status_batch_bound.json` | the same tool's own artifact. |
| `tools/audit/gen_status_batch_bound.py` | Task 3 item 1 — **the per-batch re-aiming, which the dispatch itself EXCEPTS BY NAME** under Ruling 5 of `cowork_rulings_2026_08_26_amendment_landing_sitting.md`. |
| `tools/audit/session_start_read_size.json` | Task 3 item 1 — `gen_session_start_read_size.py` regenerates. |
| `tools/audit/evidence_pin_membership.json` | Task 3 item 2 — the ordered regeneration. |

**Why this was reported and not stopped on.** Every one of the six is *caused by an act the dispatch
itself orders*, and one of them is a carve-out the dispatch names in its own bar. The standing clause
on a bar's stated purpose governs the shape: *enforcing a bar past its own stated purpose is how a
STOP becomes ritual rather than a guard.* A3's purpose is that the batch's footprint be its own and
nothing more, and the measured footprint is exactly its own ordered acts. **Nothing moved that this
batch's own orders did not move.** The two pre-existing modifications — `cowork_handoff.md` and
`cowork_informed_session_brief_framework.md` — are the writing side's, were present at Task 0, were
not touched, and were **not committed by this batch**.

### 6.4 The regenerated evidence-pin membership, measured before it was accepted

**MEASURED, then accepted.** The regenerated artifact was hashed and diffed against the committed
blob at Task 2's commit (`git diff <old-blob> <new-blob>`, both by explicit hash). **The whole
difference is two hunks:**

1. the addition of `cowork_rulings_2026_08_28_framework_delta_sitting.md` to the enumerated ruling
   records, and
2. the one derived count of ruling records read, which follows from it.

**Nothing else moved** — no member, no pin verdict, no route, no document. **The addition is not
caused by any path this batch landed**: it is the Cowork side's untracked ruling record, reaching the
derivation because that derivation's population is the file system rather than the git index, which
is precisely what the dispatch's declared start state predicted as the fourth red's cause. The check
then passes.

---

## 7. Declared departures

1. **The pins were taken with `git hash-object -w` rather than `git add` / take the identity /
   `git reset`.** The dispatch's Task 0 item 1 describes the second route. `git hash-object -w`
   writes the identical blob to the object store, returns the identical identity, and **does not
   mutate the index**, so it cannot disturb anything already staged. The pin's purpose — a
   content-addressed object every later read is taken from — is met exactly. Declared because the
   letter differs.
2. **The two commit subjects contain an apostrophe, so the shell form is not a plain single-quoted
   string.** The dispatch asks for `git commit -m '…'`; the ordered Task-1 subject contains
   *document's*, which cannot be carried inside a plain single-quoted shell string. The standard
   `'"'"'` escape was used and **the resulting subject was verified at the object** with
   `git cat-file commit` — it is exactly the ordered text, character for character.
3. **A3 is falsified as written**; §6 gives the movement, its cause per path, and the reason this was
   reported rather than stopped on.

*No other departure.* No `src/` change; no test changed, moved or run; no golden; no build; nothing
under `tools/corpus/` or `tools/robust_stop/`; no measurement of the analysis; no design; no repair;
no derivation of any specification statement; **no session booted**; no document archived, moved or
deleted as a file; **no open-items row created, flipped or discarded**; **no finding number
allocated**; no decisions-register entry written; no edit to any governing document, register entry
or register source; **and no character of `cowork_framework_document_draft_2026_08_28.md` changed.**
None of the three sealed placement-sample files was opened, in any portion; neither pack directory's
contents nor `cowork_register_blocker_surface_2026_08_28.md` was opened; and the parked register
dispatch was neither run, revalidated nor edited.

---

## 8. P1 and P2 — graded

**P1 — "B7 has NO SITE" — HELD.** It was registered to be tested rather than confirmed, and it was
tested by search before it was accepted. The searches are enumerated in the fill-in's B7 entry and
are wider than the ground the prediction was registered on: the writing side's ground was the
incumbent carry described at `ARCHITECTURE.md` §2.15, whereas the verdict here rests on the joint
arm's own posterior slice — where both axes demonstrably hold the committed span fixed — on the shape
of every alternative carrier found on both arms, and on what `analyzeRegions` does with the
segmenter's unpromoted candidate boundaries. **No site was found and none was invented.**

**P2 — "at least one statement binds differently on the two arms" — HELD, by a wide margin.** All but
one of the statements bind differently, and the exception is the one statement that binds nowhere on
either arm. Four of the differences are ones a reader of §10.2 alone could not have anticipated: one
statement's two sides are computed in opposite dependency order on the two arms; one statement's own
"not falsified by" carve-out is honoured verbatim on one arm and not implemented on the other; one
field carries a bounded value on one arm and an unbounded one on the other; and one statement binds
differently *within* the joint arm, between its two production surfaces. **The prediction's own
falsifying outcome — every statement binding identically, which would itself have been a finding
about how much the arm distinction buys — did not occur.**

*(Per D-431 the per-statement verdicts and the derived counts are read at
`cowork_arm_and_site_fillin_2026_08_28.md` and are not restated here.)*

---

## 9. The quarantined audit questions — every one, in one place

**None was investigated, none was measured, and nothing was corrected on account of any.** They are
reserved to the AUDIT under the user's ruling of 2026-08-15 — *a disagreement between specification
and code is EVIDENCE, reserved for the audit; no document is corrected on the ground that the code
says otherwise.* Each is also stated at its own entry in the fill-in.

1. **B1** — on the LEGACY arm the harmonic-boundary producers do not consume the change-point
   slicer, so the containment B1 asserts is not settled by construction there.
2. **B2** — on the LEGACY arm a slice-level tonality change inside a region is collapsed by the
   duration-majority reduction, so B2's falsifier cannot appear on the published surface.
3. **B3** — on the JOINT arm the per-note category is computed over notes **onsetting** in the
   segment's events, not over the notes **sounding** across the span.
4. **B4** — on the LEGACY arm the degree is −1 wherever the decided root is not in the mode's scale,
   so B4's equality has no left-hand side for those spans.
5. **B5** — the shared key-area grouping writes a back-reference onto regions an earlier stage
   published, on both arms.
6. **B6(i)** — both joint posterior axes re-score the committed span, so the committed reading's own
   within-segment content score need not be the maximum on either axis.
7. **B6(ii)** — on the batch/corpus surface the published rival set is unconditionally empty rather
   than empty because the reading is uncontested.
8. **B8** — the JOINT arm's event lattice omits a silent interval instead of emitting an empty
   event, which is the case B8's own carve-out describes as an explicit empty slice.
9. **B9(i)** — the record arm carries an unbounded value in nats in a field whose own declaration
   states the unit interval.
10. **B9(ii)** — the batch/corpus surface emits a literal constant where the schema names a
    confidence.
11. **B9(iii)** — no confidence carries a machine-readable class; the class is prose at the
    declaration, so B9's "class-declared" is not observable at an object.

**One further observation, which is NOT a statement-versus-code disagreement and is recorded rather
than acted on:** three joint-module headers declare `DORMANT (no production consumer)` while the
function one of them declares is called from the notation producer and from `tools/batch_analyze.cpp`.
No row was created and no file was edited on account of it. **Every item above and this one are for a
later act to row; this batch created no open-items row and allocated no finding number, as ordered.**

---

## 10. The plan lines

**★ THIS BATCH DOES NOT CLOSE THE FRAMEWORK PHASE, AND THAT IS THE FIRST THING TO SAY PLAINLY.** That
phase's postcondition is a **RATIFIED** framework, and ratification is HELD until the user's external
list of published research arrives and is dispositioned against the decomposition. **The critical
path runs through the user and through no session.** What this batch did is discharge **R-2** — the
framework document's own declared gap, that its behavioural statements name no code site and say
which part of the system they bind — and test two sub-fields that had never been tested.

Owed and **NOT** done:

1. **§9.0's decision surface** — the grain of a unit, which the framework document puts to the user
   as the phase's first ratified finding and which Ruling 2 fixed as the question ruled first. No
   surface for it exists. This is the largest owed item that moves the plan.
2. **The placement test** — by a side that did not author, measuring **coverage, not independence**
   (the author being informed), and carrying the record's twice-stated condition that **a session
   with a shell precede reliance on its results**. That condition is unanswered.
3. **The phase's retrospective** — §3.9 of
   `ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md` rules that every phase closes
   with a recorded retrospective, landed on disk and named in the phase's handover, **before the next
   phase opens**. None is written.
4. **Everything the eightieth handoff entry's backlog carries**, unchanged — including that **the
   parked register dispatch is now known to be incomplete at three points** (its third code site, its
   mis-attributed quotation, and its declared start state), that its Task 3 is not performable as
   written, and that Δ1's pointer, the four owed decisions-register entries and the rule-(c)
   suspension's underived list all stand.
5. **The eightieth handoff entry itself is still unlanded**, as are the seventy-ninth and
   seventy-eighth blocks' owed items; this batch prepended nothing and edited no handoff.

**★ AND THE ONE THING THIS REPORT ADDS TO THAT LIST:** the quarantined questions of §9 are the first
concrete specification-against-code evidence this phase has produced. They belong to the AUDIT phase
and must not be worked before it, but they are now enumerable rather than hypothetical, and a later
act owes them their rows.

---

## 11. The standing self-check over this batch's own work

Re-read the actual diff of every touched path before reporting.

1. **Principles touched.** **#6** — the ARM and SITE facts get ONE home, and the fill-in says on its
   face why that home is not the framework document. **#12** — nothing was deleted or rewritten; the
   forward-bound move was performed by the tool that reads the entry text from a git object rather
   than retyping it, and every previous aiming of that tool is kept beside the new one. **#13** — the
   one surprise met (A3 unsatisfiable as written) was surfaced in the report rather than absorbed.
   **#15** — every commit was verified at the object on both its subject and its path set, and both
   pins were re-proven by hash rather than by the memory of not having edited them. **#17f / D-431** —
   no measurement figure is transcribed: the guard totals are cited at their artifact or declared
   uncarried where the run writes none, and the fill-in's per-statement verdicts are cited rather than
   restated. **#19** — P1 and P2 were graded against searches and readings recorded in the fill-in, not
   against the grounds they were registered on.
2. **Conventions.** American English. No self-invented label — ARM, SITE and the sub-field numbers are
   the record's own. No music-theory word is used in a non-musical sense: *score* appears only as the
   musical score or qualified as *content score*; *key* is not used for a lookup and the tonality sense
   is written *tonality*; *note* is a pitch event throughout; *register* appears only as *the
   open-items register* / *the decisions register*, in full; *measurement tool* is used where the
   collided word would have been.
3. **Figures and premises.** Every premise the fill-in rests on was read at the primary source in this
   session — the module headers and implementation blocks named in each entry's *how you found it*
   line — and no premise was carried from the dispatch, which asserts none.
4. **The file-tools rule.** All working-tree content was read with Read / Grep / Glob. Shell use was
   confined to read-only git object queries by explicit hash (`cat-file`, `hash-object`, `rev-parse
   <sha>:<path>`, `diff <blob> <blob>`, `diff-tree`), the sanctioned enumeration tool
   `tools/audit/changed_paths.py`, the sanctioned generators, and `git commit` / `git push`. The
   armed guard denied three attempted commands during the batch — a `python -c` carrying a repository
   path, a compound command ending in `cat .git/refs/heads/master`, and a `git diff` whose two blob
   identities were held in shell variables rather than written as literals (deny-on-indeterminate,
   working exactly as its ruling states). **Each was re-done through the file tools or with literal
   hashes; none was worked around.**
5. **Uncertainty on any comparison.** No two measured quantities are compared in this report, so #24
   raises no demand. The comparisons made — each regenerated artifact against its committed blob —
   are byte diffs, not measurements.

---

## 12. The end state — E3

The close commit `a243a28c975a97123f155096d30b1f89f6622797` was pushed and `origin/master` re-read at
its ref before the end-state run began. **At that tree the FULL guard set was then run in write
mode**, and the artifact it produced is committed **only after the run that produced it**, in the
further commit this section records.

**E3 — MET.** The run reported **exactly the three known failing checks and no others** —
`tools/audit/gen_filing_convention_application.py --check`,
`tools/audit/decisions/apply_soft_discard.py --check` and
`tools/audit/decisions/apply_residue_discard.py --check` — **zero STOPs, and no UNCLASSIFIED tool.**
`tools/audit/gen_evidence_pin_membership.py --check`, the fourth red of the declared start state, is
GREEN at the end state, its cause discharged by the regeneration §6.4 measures. The summary itself is
read at `tools/audit/guard_state.json` → `summary` and is not transcribed here (**D-431**).

**The artifact's own movement was measured, blob to blob by explicit hash, before it was accepted.**
The whole difference between the pre-batch guard state and the end-state one is **three captured
output blocks and no verdict**: the forward bound's own reconciliation line, the evidence-pin
regeneration's ruling-record line, and the session-start read-size measurement. **No tool's pass/fail
state moved in either direction.**

### 12.1 One observation about a tool that is NOT in the guard set — reported, not acted on

`tools/audit/gen_guard_classification.py --check` reports **STALE**. It is deliberately **not** one of
the tools the guard set runs — `gen_guard_state.py` excludes it by name to avoid recursion, and its
own docstring says it is run separately afterwards — so **E3 is unaffected by it**, and the two
preceding batches' end-state commits likewise touched only their report and `guard_state.json`.

**It was not caused by this batch, and that is established rather than inferred.** The classification
derives each tool's state from the guard state; the blob-to-blob diff above proves **no tool's
pass/fail state differs** between the pre-batch guard state and this one, so its re-derivation is
identical against either and the STALE verdict holds equally before this batch ran. What is visible in
the artifact is that its `live_tools_that_fail_and_stay` block names **four** tools, one of them
`tools/audit/gen_derivation_boot_pack.py`, which PASSES in **both** guard-state blobs. **Whether that
is the whole cause of the STALE verdict was not established, and nothing was run to find out** — the
dispatch bars running any generator outside the guard set, this batch creates no open-items row and
allocates no finding number, and a maintenance act must establish its cause before touching a
mechanism. **Recorded for a later act.**
