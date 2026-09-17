# CC dispatch — fill in the ARM and the SITE for the framework document's nine behavioural statements, and judge whether those two sub-fields are reachable at all. BIND, DO NOT GRADE. Boot NO session.

> **★ THIS IS THE ACTIVE DISPATCH. Dated dispatch note, 2026-08-28: written and released the same
> day, revalidated against nothing because nothing preceded it.** It carries no `⏸ PARKED` banner and
> none is to be added. **The parked `cc_instruction_register_baseline_repair.md` is NOT this batch's
> business and is not to be run, revalidated or edited.**
>
> **★ THE WRITING SIDE DECLARES, AND THIS IS A CONSEQUENCE OF THE LAST BATCH'S STOP: THIS FILE IS
> FINAL AT THE MOMENT IT IS HANDED OVER, AND THE WRITING SIDE DOES NOT TOUCH IT WHILE THIS BATCH
> RUNS.** The previous batch observed at least three states of its instruction in one session, one of
> which reversed an edit it had already made. **Task 0 pins this file to a blob before anything else,
> which is that batch's own recommendation adopted.** *(The writing side also does not touch
> `cowork_handoff_entry_eighty.md` or `cowork_cross_layer_transfer_list.md` while this batch runs.)*
>
> **★ WHAT THIS BATCH IS.** Task 0 pins and establishes. Task 1 fills in, for each of the nine
> behavioural statements of `cowork_framework_document_draft_2026_08_28.md` §10.2, **sub-field 1 (the
> ARM) and sub-field 2 (the SITE)** — writing them into **one new file, beside the framework document
> and never inside it**. Task 2 judges whether those two sub-fields are reachable at all and reports
> it. Task 3 closes. **That is the whole of it.**
>
> **★★ THE ONE LINE THAT MATTERS MORE THAN ANY OTHER: THIS BATCH BINDS, IT DOES NOT GRADE.** Naming
> where a statement binds is this batch's work. **Deciding whether the code SATISFIES the statement is
> specification-against-code, which the user's ruling of 2026-08-15 reserves to the AUDIT as
> evidence** — *"a disagreement between specification and code is EVIDENCE, reserved for the audit; no
> document is corrected on the ground that the code says otherwise."* **A batch that grades in passing
> has pulled the audit forward.** Where a binding makes you notice a disagreement, **record it as a
> QUARANTINED AUDIT QUESTION, in its own list, unresolved, and move on.** Do not investigate it, do not
> measure it, do not correct anything on account of it.
>
> **★ A STATEMENT WITH NO SITE IS A FINDING, NOT A FAILURE.** Report it as *NO SITE*, with what you
> searched. **Do not invent the nearest plausible site**, and do not stretch a statement to fit code
> that nearly matches — a stretched binding is worse than an absent one, because it reports coverage
> the system does not have.
>
> **★ WORDS USED HERE, EXPLAINED FIRST.** *The framework document* —
> `cowork_framework_document_draft_2026_08_28.md`, an unratified DRAFT deriving the layer
> decomposition. *A behavioural statement* — one of the nine, **B1 to B9**, at its §10.2, each already
> carrying an observable, a decision rule, and what does not falsify it. *The ARM* — which inference
> path the statement binds to: the joint estimator, which is the production inference on the batch
> and notation surfaces, or the legacy path, which remains compiled and dormant awaiting deletion.
> *The SITE* — the code location a statement binds to. *Sub-fields 1 and 2* — the ruled names for the
> ARM and the SITE in the statement form; the statements already carry 3, 4 and 5.
>
> **★ READ FIRST.** **(1)** `CLAUDE.md`, `STATUS.md`, `DECISIONS.md` in full; `BUILD_AND_TEST.md` —
> CONDITIONAL, and **this batch does NOT meet the condition** (it builds nothing, runs no test and
> runs no measurement tool): rule (a)'s `gating_ids` only. **(2)** `cowork_handoff.md`, **ITS CURRENT
> ENTRY (the seventy-ninth) and the entry below it**, AND the untracked `cowork_handoff_entry_eighty.md`
> at the root, which is the eightieth entry awaiting a prepend no batch has yet performed. **(3)**
> `cowork_audit_protocol.md`'s dispatch-protocol section IN FULL — every `###` section carrying the
> standing-clause marker. **(4)** `cowork_framework_document_draft_2026_08_28.md` — **§0 (terms), §3.4,
> §5 (the layers and the boundary contracts), §10 whole, and §11.** **You may read the rest of it and
> should where a binding needs it.** **(5)** `ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md`
> §3.3, the framework phase's own definition. **You do NOT open:** any of the three sealed
> placement-sample files; either pack directory's contents; `cowork_register_blocker_surface_2026_08_28.md`.
>
> **The standing bars bind this batch whole:** **no `src/` edit**, no golden, no test changed, moved
> or run, nothing under `tools/corpus/` or `tools/robust_stop/`, **no measurement of the ANALYSIS**, no
> design, no repair, no derivation of any specification statement, **NO SESSION BOOTED**, no document
> archived, moved or deleted AS A FILE, **no open-items row created, flipped or discarded**, **no edit
> to any governing document, any register entry or any register source**, and **no edit to
> `cowork_framework_document_draft_2026_08_28.md` itself — not one character.** **No tool source is
> edited, and this batch runs no generator except the guard set — WITH ONE NAMED CARVE-OUT: the
> forward-bound re-aiming of `gen_status_batch_bound.py --apply` in Task 3 is EXCEPTED BY NAME**, under
> Ruling 5 of `cowork_rulings_2026_08_26_amendment_landing_sitting.md`.
>
> **Commit-and-push per task. Run the FULL guard set BEFORE the first act (CHECK mode) and again at
> the end (write mode, committed as the artifact of a real run). Verify every commit at the object by
> explicit hash. Every shell command carries `; echo "exit:$?"`. `git status` and a working-tree
> `git diff` are denied by the armed guard — use the per-path explicit-hash forms and
> `tools/audit/changed_paths.py`. Plain single-quoted `git commit -m '…'` subjects.**

## Ruling ledger (quoted at the record, not paraphrased)

- **Ruling 4 of `cowork_rulings_2026_08_26_framework_opening_sitting.md`, taken on Alternative A of
  that surface's Decision 4** — the alternative's own words: *"The framework phase's statements carry
  sub-fields 3, 4 and 5; a named later act, run by a side that is allowed to read code, adds 1 and 2
  **and is where their testability is judged**."* **This batch is that named later act.** The handoff
  records the ruling as: the no-code-sites instruction STANDS, the ARM and the SITE are filled in
  afterwards by a side permitted to read code, the gap declared on the frame's face, and **the two
  sub-fields not dropped without the worth test.**
- **The gap IS declared on the frame's face**, which is the precondition of this act:
  `cowork_framework_document_draft_2026_08_28.md` §3.4 reads *"Deliberately absent."*; §10.2 opens
  *"No statement below names a code site, and none says which part of the system it binds."*; and
  §11's **R-2** states *"§10's statements are checkable in principle and not yet checked in fact."*
- **The 2026-08-15 ruling reserving specification-against-code disagreement to the audit.** Quoted in
  the head block. **It is the boundary of this batch.**
- **Alternative C — dropping the two sub-fields — was NOT taken**, and its exclusion is on the record:
  dropping them is a disposal, and this project's disposal discipline requires the worth test with a
  finding, a date and a reason, which has never been run on them. **So this batch may report that a
  sub-field is unreachable; it may not conclude that it should be dropped.**

## Premise ledger

**★ THE WRITING SIDE HAS NO SHELL AND ASSERTS NO GIT-OBJECT VALUE.** Everything below was read with
the file tools on bridge-staged snapshots of the working tree on 2026-08-28. **No commit, blob or
tree value is stated anywhere in this dispatch and none may be taken from it.** The tip was read as a
file at `.git/refs/heads/master` and is `6005daecaf9f1a6692e61521911ef8b99ed73b55`; **establish it,
and everything else, at the objects yourself.**

- **FACT — the nine statements exist and are B1 to B9**, at §10.2 of the framework document, read at
  the file by the writing side. Their subjects, in one phrase each and **not restated as their text**
  (open the document for that): B1 boundaries at change points; B2 tonality change coinciding with a
  harmonic boundary; B3 chord-tone assignment total over sounding notes; B4 the published chord
  symbol agreeing with the tonality and degree it came from; B5 no later layer changing an earlier
  layer's published fact; B6 the committed reading among the rivals and carrying the greatest mass;
  B7 a rival differing in segmentation published as such; B8 slices tiling the working span exactly;
  B9 every confidence crossing a boundary bounded, class-declared and named to its decision.
- **FACT — the ARM distinction is live and is not historical.** The joint estimator is the production
  inference layer on the batch and corpus surface, and the notation switch put it on the notation
  surface with `useJointNotationRecord` defaulting ON; the legacy notation path remains **compiled and
  dormant**, selected only by an explicit `false`, awaiting deletion at the OI-180 retirement map.
  *(Read by the writing side in `CLAUDE.md`'s gate block (A), which was present in this session's boot
  context; **declared rather than claimed as an independent read**, and ordered re-established at the
  file.)* **This is why sub-field 1 exists: a statement that never names an arm cannot distinguish a
  requirement on the joint model from one on a dormant path.**
- **FACT — the framework document is an unratified DRAFT** and its §1.4 records that ratification of
  the decomposition is separately **HELD** until an external list of published research arrives. **This
  batch does not ratify, compare, or advance that hold in any way.**

- **ASSUMPTION A1 — the working tree, by SHAPE and not by count.** The writing side has no shell and
  could not enumerate the index. **Expect: `cowork_informed_session_brief_framework.md` MODIFIED;
  `cowork_handoff.md` modified or clean; a large untracked population including this dispatch, the
  eightieth handoff entry, `cowork_cross_layer_transfer_list.md`, the framework draft, the
  2026-08-28 decision surfaces and ruling records, and the parked register dispatch.** **Enumerate
  with `tools/audit/changed_paths.py` and REPORT what you find. A third TRACKED modification is a
  STOP-and-report; the untracked population is not constrained by this dispatch and its size is not a
  STOP.**
- **ASSUMPTION A2 — the guard state at the start.** `tools/audit/guard_state.json` → `summary` records
  **75 run, 3 failing, 4 not run**, the three failing being `gen_filing_convention_application.py
  --check`, `decisions/apply_soft_discard.py --check` and `decisions/apply_residue_discard.py --check`.
  **`gen_evidence_pin_membership.py --check` is expected RED at the start of this batch, and the cause
  is this batch's own inputs**: that derivation's population moves on `cowork_rulings_*` records, and
  `cowork_rulings_2026_08_28_framework_delta_sitting.md` is untracked on disk. *(The previous batch
  measured it GREEN for the opposite reason and said so; **measure it, carry neither statement**.)*
  **Any failing verdict other than those four is a STOP-and-report.**
- **ASSUMPTION A3 — this batch's whole footprint.** **One new file, one `STATUS.md` entry, one report,
  the regenerated evidence-pin membership, and the guard artifact.** **No existing file's content is
  edited by this batch at all.** An edit to any existing file other than `STATUS.md` is a
  STOP-and-report.
- **PREDICTION P1, registered so it can be falsified — B7 has NO SITE.** The writing side read
  `ARCHITECTURE.md` §2.15: the incumbent carries alternatives as *ranked alternatives + an uncertain
  mark* over a fixed slice grid, and the chord-span is a maximal run of same-chord constant-sonority
  slices, so a rival differing in where boundaries fall has nothing to be an alternative to.
  **FINDING A SITE FALSIFIES P1 AND IS A GOOD OUTCOME — report it as falsified and do not soften it.**
  **Search properly before concluding NO SITE**; P1 is registered to be tested, not to be confirmed.
- **PREDICTION P2, registered the same way — at least one statement binds DIFFERENTLY on the two
  arms.** If every statement binds identically on both, report P2 falsified and say so plainly; that
  would itself be a finding about how much the arm distinction buys.

## The declared start state

**Four failing guard checks** — the three known, each for its own recorded cause, **plus
`gen_evidence_pin_membership.py --check` RED, caused by this dispatch's own untracked inputs and by
the untracked ruling record named at A2**, that derivation's population being the file system rather
than the index. **A fifth failing verdict is a STOP-and-report.**

## Findings in this batch

**No finding number is allocated.** [[OI-179]] OPEN and GATES. **Every finding this batch produces is
reported and rowed by a later act; this batch creates no open-items row.**

## Task 0 — pin, then establish. Nothing is written in this task.

1. **PIN THIS INSTRUCTION FIRST, BEFORE READING IT FOR CONTENT.** `git add` its path, take the blob
   id, reset the index, and **take every subsequent read of this dispatch from `git cat-file blob
   <hash>` into a scratch file outside the repository.** Report the blob id. **Do the same for
   `cowork_framework_document_draft_2026_08_28.md`** — it is the object this batch binds against and
   it must not move under you. *(This is the previous batch's own recommendation, adopted as this
   dispatch's standing form.)*
2. **Establish the tip** at the object, and `origin/master` beside it.
3. **Run the FULL guard set in CHECK mode** and grade A2. **Report the summary as measured; carry no
   figure from this dispatch.**
4. **Enumerate with `tools/audit/changed_paths.py`** and grade A1.

**E0:** both blob ids reported; the tip and `origin/master` at the object; A1 and A2 graded from
measurement.

## Task 1 — the fill-in. ONE new file, beside the framework document and never inside it.

**Write `cowork_arm_and_site_fillin_2026_08_28.md` at the repository root.** It is the ONE home for
these facts (**#6**). **It is a working artifact and not a governing document; it rules nothing.**

**★ WHY A SEPARATE FILE AND NOT AN EDIT TO THE FRAMEWORK DOCUMENT.** That document is another side's
unratified draft, and this batch is barred from editing it. **Whether this fill-in is later folded
into it is the user's call at ratification and is NOT this batch's to take** — say so on the file's
face.

**For EACH of B1 to B9, in order, one entry carrying exactly these fields:**

1. **The statement's identifier and its subject in one line** — cited to §10.2, **never re-typed in
   full** (**D-431**: a figure or a text enters by citation, not transcription).
2. **SUB-FIELD 1 — THE ARM.** One of: **JOINT** (the production inference path), **LEGACY** (the
   compiled dormant path), **BOTH**, **NEITHER**, or **NOT APPLICABLE** with the reason. Where the
   statement binds differently on the two arms, **say how it differs** — that difference is the whole
   reason this sub-field exists.
3. **SUB-FIELD 2 — THE SITE.** The code location or locations the statement binds to. **Name them the
   way this project's record requires: by file and by the function or type, NEVER by line number**
   (**D-307** — a line number quoted in prose goes stale on the next insertion above it). Where a
   statement binds to more than one site, list them all and say what each contributes.
4. **HOW YOU FOUND IT** — one line. The search that located the site, so a later reader can re-run it.
5. **REACHABLE?** — **REACHED**, **NO SITE**, or **AMBIGUOUS**, with the reason. This is the input to
   Task 2 and is not the judgment itself.
6. **QUARANTINED AUDIT QUESTION** — present only where binding made you notice a disagreement between
   the statement and the code. **State it in one sentence, unresolved, and go no further.** Leave the
   field absent otherwise. **Do not investigate. Do not measure. Do not correct.**

**THE STOPS FOR THIS TASK, and they are what keep it inside its boundary:**

- **A statement you cannot bind is NO SITE, reported with what you searched.** Never the nearest
  plausible site.
- **Do not stretch a statement to fit code that nearly matches.** If a binding needs the statement
  read more loosely than §10.2 writes it, that is **AMBIGUOUS**, with the two readings named.
- **Do not grade whether the code satisfies the statement.** That is the audit's, and the head block
  quotes the ruling that makes it so.
- **Do not edit the framework document, the handoff, the transfer list or any ruling record.**
- **Do not allocate a finding number and do not create an open-items row.**

**Commit exactly the new file and no other path.** Subject, exactly:
`record: the ARM and the SITE filled in for the framework document's nine behavioural statements — bound, not graded`
**PUSH**; verify at the object.

**E1:** nine entries, one per statement, each carrying fields 1–5 and field 6 only where it applies;
every site named by file and function and **no line number anywhere**; every NO SITE carrying what
was searched; the quarantined list separate and unresolved; the framework document byte-identical to
its pinned blob at the end of the task, proven by hash.

## Task 2 — judge whether the two sub-fields are REACHABLE AT ALL, which is what the ruling sends here

**This is a judgment about the FORM, not about the analysis**, and Decision 4's alternative A says in
terms that this act *"is where their testability is judged"*. **It has not been tested before: the
pilot reached three of the five sub-fields and these two were left untested.**

Write the judgment as a closing section of the same file. It answers, separately for the ARM and for
the SITE:

1. **How many of the nine reached it**, how many were NO SITE, how many AMBIGUOUS — **measured from
   Task 1's own entries, never asserted.**
2. **Is the sub-field reachable in practice?** State the verdict and the ground. **A sub-field that
   reaches most statements and fails on a few is reachable with named exceptions; one that fails
   broadly for a single structural cause is a different verdict and must be said as one.**
3. **What it cost** — one honest sentence on the effort, because the alternative that would drop these
   sub-fields is still open and a later worth test will need this.
4. **P1 and P2 graded**, each stated as falsified or held, with the evidence.

**★ WHAT THIS TASK MAY NOT CONCLUDE.** It may not conclude that a sub-field should be dropped.
Dropping is a disposal and the disposal discipline requires a worth test with a finding, a date and a
reason — **which is the user's act, not a batch's.** Report the facts a worth test would need and
stop there.

**Commit the amended file. PUSH; verify at the object.**

**E2:** both sub-fields judged with their counts measured from Task 1; P1 and P2 graded; no
disposal recommended.

## Task 3 — the close

1. One `STATUS.md` pointer entry per task, per the OI-222 pointer convention — **no count, no identity
   and no rendered value restated** (**D-431**). The previous batch's entries move through
   **`gen_status_batch_bound.py --apply`** — **the named carve-out; it re-aims its own forward bound
   and that is expected, declared and permitted** — and `gen_session_start_read_size.py` regenerates.
2. **Regenerate `tools/audit/evidence_pin_membership.json`** and MEASURE its diff against the
   committed blob before accepting it. Movement beyond this batch's own landed paths is reported
   rather than absorbed.
3. The report is **`cc_report_arm_and_site_fillin.md`**: both guard states, every SHA, E0–E2 graded,
   A1–A3 graded, P1 and P2 graded, declared departures, the quarantined audit questions listed
   together in one place, and the plan lines.
4. **★ THE PLAN LINES, AND SAY THE FIRST ONE PLAINLY.** **This batch does NOT close the framework
   phase.** That phase's postcondition is a **ratified** framework, and ratification is held until the
   user's external research list arrives and is dispositioned. **What this batch does is discharge
   R-2 and test two sub-fields.** Then, as owed and NOT done: **§9.0's decision surface** — the grain
   of a unit, which the framework document puts to the user as the phase's first ratified finding;
   **the placement test**, by a side that did not author, measuring coverage rather than independence,
   and carrying the record's twice-stated condition that a session with a shell precede reliance on
   its results; **the phase's retrospective** (§3.9 of the phase-definition surface), which closes it
   before the next opens and which does not exist; and everything the eightieth handoff entry's
   backlog carries, **including that the parked register dispatch is now known to be incomplete at
   three points.**
5. **★ THE CLOSE DOES NOT ASSERT THE END STATE**; one further commit carries it.
6. Commit, push, verify; then the one further commit with the end-state guard run.

**E3:** at the tree carrying the close, a fresh full guard run — the three known failing checks and no
others, zero STOPs — committed only after the run that produced it.

## What this batch does NOT do

- **It does not grade a single statement against the code.** Reserved to the audit, and the head block
  quotes the ruling.
- **It edits no existing file's content** except `STATUS.md`. **The framework document is not touched,
  in any character.**
- **It does not ratify, compare or advance the framework document's held ratification**, and it runs
  no placement test.
- **It writes no decisions-register entry and allocates no `D-NNN`** — the register cannot accept one;
  `cowork_register_rule_c_suspension_2026_08_28.md` is the route and **its list is still underived.**
- **It does not touch the parked register dispatch**, which is known to be incomplete and is not this
  batch's business.
- **It creates no open-items row and allocates no finding number**, though it will produce findings.
- **No `src/` change, no test, no golden, no build, no measurement of the analysis, no session booted,
  no pack rendered, no framework text authored.** None of the three sealed placement-sample files is
  opened.

## The writing side's self-check over this dispatch

1. *Principles touched:* **#12** — nothing is deleted or rewritten; the fill-in lands beside the
   framework document and the document is proven byte-identical at the end. **#6** — the ARM and SITE
   facts get ONE home, and the dispatch says why it is not the framework document. **#13** — the
   surprise the last batch met (a moving instruction) is answered structurally by the pin at Task 0
   rather than by an exhortation. **#17f / D-431** — no count and no git-object value asserted; every
   figure is ordered measured, and the nine statements are cited rather than transcribed. **#19** —
   P1 and P2 are registered as falsifiable predictions with the falsifying outcome named as a good
   one, and Task 2's verdict is ordered measured from Task 1's own entries.
2. *Conventions:* American English; no self-invented label — **ARM**, **SITE** and the sub-field
   numbers are the record's own; no music-theory word is used in a non-musical sense, and *site*,
   *arm*, *statement* and *binding* carry no musical collision.
3. *Figures and premises:* every premise above was read at the files by the writing side on
   2026-08-28 and is ordered re-established at the objects. **The one item declared rather than
   independently read is the gate block's arm status**, which was in this session's boot context.
4. *File-tools rule:* the writing side read only through the file tools and ran **no shell command of
   any kind** — the user barred it for this session — **so it verified no git object and this dispatch
   relays none.**
5. *Uncertainty:* the measured-not-predicted items are every binding, both sub-field verdicts, the
   guard state, and the tree enumeration. **P1 and P2 are predictions and are registered as such.**
6. *The failure this dispatch is written against:* the previous batch's instruction moved under it.
   **The pin at Task 0 and the writing side's declaration in the head block are the two halves of the
   answer, and one of them binds the writing side rather than the batch.**
