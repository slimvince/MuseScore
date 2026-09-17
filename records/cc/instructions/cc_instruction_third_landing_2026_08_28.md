# CC dispatch — LAND the external research workbook. One binary file, exactly as it stands. No repair, no design, no reading of its content. Boot NO session.

> **★ THIS IS THE ACTIVE DISPATCH. Dated dispatch note, 2026-08-28: written and released the same
> day. It carries no `⏸ PARKED` banner and none is to be added.** It may go straight to a session.
>
> **★ THE PIN ORDER, PERFORMABLE FORM.** Suggested opening instruction to the executing session:
> *"pin `cc_instruction_third_landing_2026_08_28.md` to a blob with `git hash-object -w`, then read
> it from that object, and execute it."* Where the session read this file from the working tree
> first, declare it, pin at Task 0, and prove at Task 1 that the blob has not moved.
>
> **★ WHO WROTE IT.** The Cowork writing side of the fifty-ninth session, on 2026-08-28, after the
> second landing dispatch was handed over — **this dispatch was held out of the working tree until
> the second landing batch's report existed**, so no batch observed it appearing mid-flight. Read
> its bars sceptically and STOP on a contradiction rather than resolving it in this dispatch's
> favour. The writing side declares it does not touch this file or the file it lands while this
> batch runs.
>
> **★ WHAT THIS BATCH IS, AND WHY.** The user ruled on 2026-08-28 that the external research
> workbook — the list of published research he prepared with another LLM, the input the framework
> document's §1.4 ratification hold waits on — **is this project's file and is git-handled as
> such.** It currently exists only untracked on one machine. Task 1 lands it and this dispatch;
> Task 2 closes. **Nothing reads the workbook's content, nothing dispositions it against anything,
> and nothing converts, renames or edits it** — its use belongs to the ratification sitting and is
> not this batch's business.
>
> **★ THE FILE AND ITS PATH, EXACTLY.** `external resarch summary/external research.xlsx` — a
> subfolder at the repository root; **the folder name's spelling ("resarch") is the user's and is
> committed AS IT STANDS. Renaming it is not ordered and is a STOP if any step would require it.**
> The file is binary (an Excel workbook, ~183 KB). Git handles binary content; it is pinned and
> committed like any other file, with no diff expectations.
>
> **★ READ FIRST.** **(1)** `CLAUDE.md`, `STATUS.md`, `DECISIONS.md` in full; `BUILD_AND_TEST.md` —
> CONDITIONAL, and this batch does NOT meet the condition: rule (a)'s `gating_ids` only.
> **(2)** `cowork_handoff.md`'s CURRENT ENTRY. **(3)** `cowork_audit_protocol.md`'s
> dispatch-protocol section in full. **You do NOT open:** the workbook's content (staging and
> hashing it is not opening it); any sealed placement-sample file; `ARCHITECTURE.md`;
> `cowork_framework_document_draft_2026_08_28.md`.
>
> **The standing bars bind this batch whole:** no `src/` edit, no golden, no test changed, moved or
> run, nothing under `tools/corpus/` or `tools/robust_stop/`, no measurement of the ANALYSIS, no
> design, no repair, no derivation of any specification statement, **NO SESSION BOOTED**, no
> document archived or moved AS A FILE, no open-items row created, flipped or discarded, no
> decisions-register entry written and no `D-NNN` allocated, no edit to any governing document, any
> register entry or any register source, and **no edit to the CONTENT of the file this batch lands
> — it is committed byte-exactly as it stands on disk.** The forward-bound re-aiming of
> `gen_status_batch_bound.py --apply` in Task 2 is EXCEPTED BY NAME under Ruling 5 of
> `cowork_rulings_2026_08_26_amendment_landing_sitting.md`.
>
> **Commit-and-push per task. Run the FULL guard set BEFORE the first act (CHECK mode) and again at
> the end (write mode, committed as the artifact of a real run). Verify every commit at the object
> by explicit hash. Every shell command carries `; echo "exit:$?"`. `git status` and a working-tree
> `git diff` are denied by the armed guard — use the per-path explicit-hash forms and
> `tools/audit/changed_paths.py`.**

## Premise ledger

**★ THE WRITING SIDE HAS NO SHELL AND ASSERTS NO GIT-OBJECT VALUE.** Everything below was read at
the files through the bridge on 2026-08-28. **Establish the tip at the object; this dispatch states
no value for it.**

- **FACT — the workbook exists** at `external resarch summary/external research.xlsx`, read whole
  by the writing side through a bridge-staged snapshot on 2026-08-28.
- **FACT — the guard set's three known failing checks** are
  `gen_filing_convention_application.py --check`, `decisions/apply_soft_discard.py --check` and
  `decisions/apply_residue_discard.py --check`. The register repair that would clear the last two
  is PARKED and is not this batch's business.

- **ASSUMPTION A1 — the working tree, by SHAPE and never by count.** No tracked modification is
  expected outside `STATUS.md` and the artifacts Task 2 regenerates; **any found at Task 0 is a
  STOP-and-report.** The untracked population includes the workbook's folder, this dispatch, and
  the historical dispatch-file population earlier reports enumerated. **Enumerate with
  `tools/audit/changed_paths.py` and REPORT what you find before acting.**
- **ASSUMPTION A2 — the guard state at the start.** The three known failing checks. The
  evidence-pin membership check's state is MEASURED, not carried — its population is root-level
  `cowork_rulings_*.md` files, which this batch neither adds to nor lands, so no movement caused by
  this batch is expected there; **grade what the run shows and explain any difference at its
  mechanism, as the previous batches did. A fifth failing verdict is a STOP-and-report.**
- **ASSUMPTION A3 — this batch's footprint is exactly what its own orders move:** the workbook file
  (added), this dispatch (added), and in Task 2 `STATUS.md`, `STATUS_ARCHIVE.md`,
  `tools/audit/status_batch_bound.json`, `tools/audit/gen_status_batch_bound.py` (the named
  carve-out), `tools/audit/session_start_read_size.json`, the report, and
  `tools/audit/guard_state.json` at the end-state commit. **Movement caused by this batch's own
  orders at any other path is a STOP-and-report; a movement no order of this batch caused is
  reported and graded, never absorbed.**

## Task 0 — pin, then establish. Nothing is written in this task.

1. **PIN THIS INSTRUCTION** (`git hash-object -w`), report the blob, take later reads from the
   object. Declare a pre-pin working-tree read if one happened; prove the blob unmoved at Task 1.
2. **PIN THE WORKBOOK** the same way and report its blob identity.
3. **Establish the tip** at the object, and `origin/master` beside it.
4. **Run the FULL guard set in CHECK mode**; grade A2 from that run.
5. **Enumerate with `tools/audit/changed_paths.py`**; grade A1.

**E0:** both blobs reported; the tip and `origin/master` at the object; A1 and A2 graded from
measurement.

## Task 1 — land the workbook, PUSH

1. **LAND `external resarch summary/external research.xlsx` byte-exactly as it stands** — confirm
   it is present and untracked at Task 0's enumeration, stage it, and re-establish its pinned blob
   at the commit object. A mismatch is a STOP-and-report.
2. **LAND `cc_instruction_third_landing_2026_08_28.md` (this dispatch)** the same way.
3. **REPORT, AND DO NOT LAND, anything else** — with the carve-out that
   `cc_report_third_landing_2026_08_28.md` does not exist yet and is committed by Task 2.
4. **Commit; the subject, exactly:**
   `record: land the external research workbook — the published-research list the framework ratification hold waits on, at external resarch summary/external research.xlsx`
5. **PUSH**; verify at the object.

**E1:** both paths committed blob-identical to their pins; nothing else committed by Task 1;
`origin/master` at the commit.

## Task 2 — the close

1. One `STATUS.md` pointer entry per task, per the OI-222 pointer convention — no count, no
   identity and no rendered value restated (**D-431**). The previous batch's entries move through
   `gen_status_batch_bound.py --apply` (the named carve-out); `gen_session_start_read_size.py`
   regenerates.
2. The report is **`cc_report_third_landing_2026_08_28.md`**: both guard states, every SHA, E0 and
   E1 graded, A1–A3 graded, declared departures, and the plan lines.
3. **★ THE PLAN LINES.** This batch moves the framework phase not at all — it is a backup and
   custody act. **What it changes upstream of the phase: the external research list the §1.4
   ratification hold waits on is now delivered, in git, and pushed — so the dispositioning of the
   decomposition against it is unblocked on the input side and is the user's sitting to
   commission.** Still owed and not done: the placement test (the shell condition unanswered), the
   phase retrospective (§3.9), and the eightieth entry's backlog including the eleven quarantined
   audit questions, reserved to the AUDIT.
4. The close does not assert the end state; one further commit carries it, and where the report's
   SHA table cannot carry its own committing identities, one further commit fills exactly those
   cells, as the first landing batch did and declared.
5. Commit, push, verify; then the further commit(s) with the end-state guard run.

**E2:** at the tree carrying the close, a fresh full guard run — the three known failing checks and
no others, zero STOPs — committed only after the run that produced it.

## What this batch does NOT do

- **It does not open, read, convert, extract, rename or edit the workbook.** Its content is the
  ratification sitting's business.
- **It renames no folder** — the path is committed with the user's spelling as it stands.
- No repair; the parked register dispatch untouched; the §8 move not performed; no register entry,
  no open-items row, no finding number; the quarantined audit questions untouched; the historical
  dispatch-file population untouched (a user question).

## The writing side's self-check over this dispatch

1. *Principles:* **#12** — nothing deleted, nothing rewritten; one binary file added byte-exactly.
   **#6** — the workbook stays the ONE copy; no extraction or second home is created here.
   **#17f / D-431** — no count or git-object value asserted; everything ordered measured.
2. *Conventions:* American English; no self-invented label; the one music-theory-adjacent word in
   this batch's subject matter ("research") carries no reserved sense.
3. *Premises:* read at the files by the writing side on 2026-08-28; ordered re-established at the
   objects.
4. *File-tools rule:* the writing side ran no shell command of any kind; this dispatch relays no
   git-object value.
5. *The recorded dispatch-writing failures, answered structurally:* performable pin order at the
   head; A3 as a list of this batch's own ordered acts; no sentence quoted from a file the writing
   side did not open; and the dispatch was held out of the tree while another batch ran.
