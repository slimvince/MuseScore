# CC dispatch (SECOND WRITING) — land the reading pass and execute Rulings 2 and 3

> **Written by the Cowork writing side, 2026-08-31, after the FIRST writing stopped at Task 0.**
> The user opens this with Claude Code; no session starts it and no session lands anything itself
> (the 2026-08-26 role ruling, **D-252**).
>
> **The first writing is `cc_instruction_reading_pass_landing_2026_08_31.md`. It STOPPED at Task 0
> step 2 on its own ninth-failure clause and wrote nothing to the repository. It is landed by this
> batch as record and is never run.** Its stop report is landed with it.
>
> **Nothing in this dispatch is a decision.** Every text change it orders executes a ruling the user
> has already taken.

## What changed from the first writing, and why — read this before Task 0

Four changes, each forced by something the first writing established at the objects:

1. **The declared start state is now NINE failing, not eight.** The ninth —
   `tools/audit/gen_evidence_pin_membership.py --check`, STALE — was established at the objects: the
   tool derives its ruling-record population by scanning the live repository root
   (`os.listdir(ROOT)` at `gen_evidence_pin_membership.py:186`, pattern `^cowork_rulings_.*\.md$` at
   `:112`) and is **not epoch-pinned**, so the two untracked ruling records written to the root on
   30 and 31 August entered its population the moment they hit disk and the committed artifact
   stopped re-deriving. **The user has ruled it not news:** its cause is established, its subject is
   this project's own apparatus, and it is the OI-301/OI-305 shape the record already names. **The
   underlying mechanism question — that this tool reads the live tree and will go red again on the
   next unlanded ruling record — is on the user's owed list and does NOT gate.**
2. **A regeneration is added (Task 3).** Adding ruling records IS a change to that artifact's own
   source population, so the conforming act is to regenerate the generated surface, not to repair a
   red and not to hand-edit it.
3. **The prepend is DROPPED.** The first writing established that the *ratified splice construction*
   the record leans on **does not exist as a re-runnable artifact in the tree** — the phase-close
   batch's splice appears to have been a scratch script that was never committed, which is a
   **#19-shaped gap in something the record relies on** and is recorded as a finding for the user.
   **The four staged handoff entries are therefore landed AS FILES and stay staged**; the prepend
   becomes its own later act with its own tool. Nothing is lost: what protects those entries is
   being tracked, not being spliced.
4. **Task 2's redistribution question is ANSWERED by the user and is no longer a STOP.** See Task 2.

## Task 0 — pin first, then establish. Write nothing.

**The user's opening line carries the pin order** (the ratified standing form, P-2). Pin THIS
dispatch to a blob before reading it, and take every later read of it from that object.

1. **Establish the tip.** Read `master` and `origin/master` at the object and report both. If they
   differ, **STOP**. *(The first writing found both at `b8e738448e…`; establish it again rather than
   carrying that value.)*
2. **Run the FULL guard set in CHECK mode** and report the summary. **The declared start state is
   75 run, 66 passing, 9 failing:** the three long-known
   (`gen_filing_convention_application.py`, `apply_soft_discard.py`, `apply_residue_discard.py`);
   the five stop-reported ordered-edit reds (`gen_artifact_inventory_surface.py`,
   `gen_test_construction_evidence.py`, `gen_retirement_caller_check.py` — which crashes on a
   `KeyError` — `gen_derivation_boot_pack.py`, and `decisions/gen_cluster_dispositions.py --verify`);
   and **the ninth, `gen_evidence_pin_membership.py --check`**, whose cause is stated above.
   **A TENTH failure is news: report it and STOP.** **Repair none of the nine** — their repairs are
   separately owed to the user, and the ninth is addressed by Task 3's regeneration rather than by
   repair.
3. **Enumerate the working tree** — tracked modifications and untracked paths, both — and report the
   enumeration before Task 1. Every later task works from that enumeration, never from a list typed
   into this file. *(The first writing found 851 untracked paths and zero tracked modifications.)*

## Task 1 — the two ruled corrections to `FRAMEWORK.md`

**Both are the user's rulings of 2026-08-31, recorded at
`cowork_rulings_2026_08_31_decision_surface_sitting.md` §3a and §3b. Read that record, and the
surface each ruling names, AT THE OBJECT and take each correction's content from there. Do not take
it from this dispatch, which deliberately paraphrases and is not the source.**

- **Ruling 2 (V4), Option A — correct minimally.** The clause at `FRAMEWORK.md` §5, L1, *"Why metric
  strength earns its place"*, is corrected to the primary's own three-level gradient as the ruling
  states it, **with the former wording preserved in place (#12)**. **Option B is declined and its
  content must NOT enter the charter.** Supporting case:
  `reading_pass/stop_v4_divergence_2026_08_30.md`.
- **Ruling 3 (DP-K's second ground), Option B — qualify in place and add the on-domain evidence.**
  At `FRAMEWORK.md` §9, DP-K's second ground is narrowed to what its primary supports and the two
  on-domain findings are added as further grounds, **each carrying its read grade**. Former wording
  preserved (#12). **DP-K itself is not reopened and its first ground is untouched.**

**★ THE THIRD INSTANCE IS REPORTED AND NOT TOUCHED.** The first writing established that the
misstated metric-strength figure appears twice more: once in **Appendix B**, the first-stage draft
preserved *"whole and unedited"* — correctly untouched — and once at **§14.1** as a source-family
summary. **Neither ruling reaches either.** Report the §14.1 instance with its location as a **new
user item**; **do not edit it.**

**Bounds.** These two clauses are the only edits authorised anywhere in `FRAMEWORK.md`. Both are
proven **additions-plus-preserved-former-wording at the blob-to-blob difference**. No `D-NNN` is
allocated and no register entry is written — the rule-(c) suspension stands.

## Task 2 — track the untracked population

Work from Task 0's enumeration. Classify every untracked path and **report the classification in
full before adding anything.**

**(i) TRACK — the line's records and outputs.** Everything under `reading_pass/` (the population,
the fetch record, the continuation file, the STOP memo, the extracts, the second-pass extracts, the
cross-checks); the findings surface at the root; the surfaces under `ratification_surfaces/`; the
ruling records at the root; the commissions and dispatches at the root — **including the first
writing of this dispatch and its stop report, landed as record and never run.**

**(ii) TRACK — the four staged handoff entries, AS FILES.** `cowork_handoff_entry_eighty_two.md`
through `..._eighty_five.md`. **They are NOT prepended and NOT deleted by this batch** (see change 3
above). `cowork_handoff.md` is untouched.

**(iii) ★ `docs/research_papers/reading_pass_2026_08/` — THE USER HAS RULED, Option A: SPLIT BY
KIND.** The first writing established the convention at the objects: the fifty-eight library PDFs
are untracked by `.gitignore:131` `docs/research_papers/*.pdf`, under the comment naming the private
repository as their git home, *"never this public fork"* — and that pattern **does not cross `/`**,
so it does not reach this subfolder. The folder holds **seventeen markdown fetched-content records
and one PDF** (`mueller-konz-bogler-arifimueller-2011-saarland-music-data.pdf`).

- **The PDF is NOT tracked.** It is a whole third-party paper — exactly the class the rule excludes,
  and the rule is tier-blind.
- **★ AND ITS EXCLUSION IS STATED RATHER THAN INCIDENTAL: amend `.gitignore` so the research-paper
  binary rule reaches subfolders** (the pattern that matches a `.pdf` at any depth under
  `docs/research_papers/`), keeping the existing comment. **This is the only `.gitignore` change
  authorised; add no other rule.** Verify with git's own ignore check that the Saarland PDF is
  matched and that **no file the batch means to track becomes ignored**, and report both.
- **The seventeen markdown records ARE tracked.** The user's ground, recorded so a later reader
  meets it: they are **our own authored records** — structured summaries in our words carrying a
  retrieval header, a declared read-grade bound, and short attributed quotations — **not
  reproductions**; they are the layer between the papers and the extracts, which is what makes the
  pass's measured read-tool bound checkable; and this repository already carries verbatim
  quotations from these same papers in public, in `FRAMEWORK.md`, the extracts and `DECISIONS.md`,
  so tracking them adds no new class of exposure.
- **★ THE CHECK THAT TURNS A SAMPLE INTO AN ESTABLISHED CLAIM (#19).** The writing side read **two**
  of the seventeen. **Confirm mechanically that the other fifteen are the same kind — a record whose
  bulk is our own prose with short attributed quotations, not a substantial reproduction of a
  paper's text.** State the measure you used. **If any one of them is substantially a reproduction,
  STOP and put that file to the user.**

**No signature-table change.** Adding files will very likely move what
`gen_artifact_inventory_surface.py` derives, and that check is already one of the known nine. **Run
it after the additions and REPORT what it says — do not repair it, and do not touch the signature
table**, whose amendment mechanism is reserved to the user. Classifying these new paths is a user
act that follows this batch.

## Task 3 — regenerate the evidence-pin membership artifact

Run `tools/audit/gen_evidence_pin_membership.py` in its establishing mode so the artifact
re-derives, and commit the regenerated artifact **in this batch's commit**.

**The predicted difference, stated before the act (P-3): exactly two ruling records appear —
`cowork_rulings_2026_08_30_detail_phase_opening_sitting.md` and
`cowork_rulings_2026_08_31_decision_surface_sitting.md` — and nothing else moves.** The tool scans
the repository root non-recursively, and both are root-level files, so no other member can be
reached by this act.

**★ STOP if the difference is anything other than that**, or if the tool halts, or if any member's
pin state changes. **Report the difference in full either way.** Then re-run the guard set and
report whether the ninth clears; **if it does not, report and do not repair.**

## Task 4 — land and push

**One commit**, provenance-stamped, carrying Tasks 1, 2 and 3. **Re-establish every landed blob at
the commit object equal to its pin.** Push, and **verify `origin/master` by two independent routes.**
Report every commit identity; the writing side relays identities and never resolves them.

## Task 5 — the report and `STATUS.md`

Write `cc_report_reading_pass_landing_second_2026_08_31.md` into the tree and land it with the rest.
It carries: Task 0's pins, tip and guard summary; the tree enumeration; Task 1's blob-to-blob
differences with the additions-only proof **and the §14.1 instance reported as a user item**;
Task 2's full classification, the `.gitignore` amendment with its ignore-check evidence both ways,
and the fifteen-record kind check with its stated measure; Task 3's predicted-versus-actual
difference and the guard re-run; and every commit identity.

**Update `STATUS.md` in the same batch.** Per the OI-222 pointer convention its entry is a
**POINTER** — no count, no identity and no rendered value restated (**D-431**) — and maintain its own
forward bound (only the latest batch's entries stay; the rest move to `STATUS_ARCHIVE.md`).

## Standing bounds on this whole batch

**Do not:** derive or amend any specification; open the workbook
(`external resarch summary/external research.xlsx`) in any portion, or rename or move that folder;
touch anything under `tools/corpus/` or `tools/robust_stop/`; run any measurement, golden, build or
test; edit any tool SOURCE (Task 3 runs a tool, it does not change one); create, flip or discard an
open-items row; write a register entry or allocate a `D-NNN`; repair any of the nine known guard
failures; edit `FRAMEWORK.md` anywhere but the two ruled clauses; prepend, splice or delete any
handoff entry; or edit the reading pass's own record files, which are landed as they stand.

**Every departure is DECLARED in the report, never absorbed silently.** If a task cannot be
performed as written, STOP at that task and report; later tasks are not attempted around it unless
they are independent of it, and independence is stated rather than assumed.

---

*Provenance: written by the Cowork writing side, 2026-08-31, on the user's rulings of that date. Its
factual basis was read at the files this session: the first writing's stop report in full;
`.gitignore` at the object (line 131 and its comment); `tools/audit/gen_evidence_pin_membership.py`
at lines 112 and 186; the `docs/research_papers/reading_pass_2026_08/` listing; two of that folder's
seventeen records read whole; and `cowork_rulings_2026_08_31_decision_surface_sitting.md` §3a–§3b.
CC's negative claim that no splice tool exists in the tree is carried as RELAYED — the writing side
cannot establish a tree-wide absence without a shell. No shell command was run on the repository or
on any staged copy of it, and no git object was resolved by the writing side.*
