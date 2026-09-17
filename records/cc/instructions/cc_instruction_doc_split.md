# CC instruction — split STATUS.md and cowork_handoff.md into lean active + archive (doc hygiene)

**Dispatch author:** Cowork, 2026-07-13, at the user's direction. **Type:** pure documentation hygiene —
**no code, no build, no test, no inference, no register change beyond these files.** Runs AFTER the OI-168
fix. The goal: the two files CC must read at session start currently carry a long chronological log of
*superseded* entries that cost context on every read without helping CC code. Separate the **current state**
(lean, must-read) from the **history** (archived, reference-only), losing nothing (#12/#16).

Read first: `CLAUDE.md` (the "read these at the start of every session" mandate + the handoff read-order
convention), the current `STATUS.md`, and `cowork_handoff.md`.

**Addendum (Cowork, 2026-07-18, before this dispatch first runs):** the working tree may carry
**uncommitted edits from the 2026-07-18 Cowork session** — CLAUDE.md (principles #20–#24 + the #17 ledger
corollary + provenance, user-ratified 2026-07-18), `OPEN_ITEMS.md` (rows OI-176…OI-181), and
`cowork_joint_estimator_architecture.md` (§5 amendment, §6 recorded assessment, §7 plan amendments), plus
this addendum. **Task 0: commit those as their OWN commit first** (`docs: ratify principles #20–#24 +
joint-estimator plan amendments (OI-176…OI-181), user-ratified 2026-07-18`) so the mechanical split commit
stays pure (#14). Do not fold them into the split. The split's Task 2 cut line: the **2026-07-17 joint-
architecture entry block is the current entry point and stays active**; the session-close blocks below it
are the history to archive.

---

## 1. Governing constraints

- **No content is deleted.** Every historical block moves **verbatim** to its archive file; the active file
  keeps the current-state content. Together, active + archive must contain everything the original had
  (#12). Reconcile this explicitly before committing (e.g. confirm each moved block is byte-identical in the
  archive and absent from the active).
- **The active files must stay self-sufficient for a context-less session start** — a next CC session
  reading only the lean `STATUS.md` (+ `CLAUDE.md` + `OPEN_ITEMS.md`) and the lean handoff must have
  everything needed to begin coding: current baselines, HEAD, active iteration/next-action, known
  regressions, the current entry point, and the standing work package.
- No self-invented labels — name the archives plainly (`STATUS_ARCHIVE.md`, `cowork_handoff_archive.md`).
  Fork-only push. Self-check the diff. No `src/` file, no golden, no corpus, no build.

## 2. Task 1 — split `STATUS.md`

- **Active `STATUS.md` keeps:** the standing baseline/policy content a session needs (the current ratified
  robust-unit root/RN/key columns, or a pointer to the CLAUDE.md gate block (A) that holds them), HEAD, the
  active iteration + next-action, known regressions/blockers, and the **most recent one or two** "Last
  updated" entries. Add a one-line pointer to the archive.
- **`STATUS_ARCHIVE.md` gets:** every older dated "Last updated" block, verbatim, newest-first, under a
  header stating it is historical/reference-only and not part of the session-start read.
- Judgment call on the cut line: keep what reflects the *current* state and the immediately-recent context;
  archive what is superseded. When unsure, keep it active (bias to not losing current-relevance), but move
  the clearly-historical bulk.

## 3. Task 2 — split `cowork_handoff.md`

- **Active `cowork_handoff.md` keeps:** the current entry-point block (the top "CURRENT ENTRY POINT"), the
  standing key-layer work-package block, and the read-order convention that orients the next session. Add a
  one-line pointer to the archive.
- **`cowork_handoff_archive.md` gets:** the older session-close blocks (SESSION 36 close, the older CC
  entries, etc.), verbatim, newest-first, under a historical/reference-only header.
- The handoff stays "the ONE document you read first" — now lean, pointing to the archive for history.

## 4. Task 3 — update the read-at-session-start references

- In `CLAUDE.md`, update the "Always read these two files at the start of every session" section so it
  points at the now-lean `STATUS.md` (and `BUILD_AND_TEST.md` unchanged), noting that `STATUS_ARCHIVE.md`
  and `cowork_handoff_archive.md` are reference-only history, not part of the session-start read.
- If the handoff's own "read this first" convention names files, keep it consistent with the split.

## 5. Deliverable

- **Commit:** a single `docs(cc)` commit — the four touched files (`STATUS.md`, `STATUS_ARCHIVE.md`,
  `cowork_handoff.md`, `cowork_handoff_archive.md`) + the `CLAUDE.md` reference update. Force-add this
  instruction file. Push to `origin` only.
- **The report is light** (this is mechanical): a short note in the commit body (or a one-paragraph
  `cc_doc_split_report.md`) recording the reconciliation — that active + archive == the original content for
  each file, nothing lost. No `STATUS.md`/handoff *content* update beyond the restructure (the OI-168 fix's
  own STATUS/handoff entries were already written by that dispatch).
- **STOP-and-report** if the reconciliation shows any content would be lost or altered, rather than
  proceeding.

**On completion:** the session-start reads are lean and fast, the full history is preserved and referenced,
and the standing discipline going forward is that a superseded entry moves to its archive rather than
accumulating in the must-read (the OPEN_ITEMS register pattern, applied to STATUS and the handoff).
