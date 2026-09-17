# CC instruction — commit and push the 2026-07-19 design-pass session (docs only)

**Dispatch author:** Cowork, 2026-07-19, at the user's direction. **Type:** pure documentation
commit — **no code, no build, no test, no golden, no corpus, no re-baseline.** Everything in this
commit was user-ratified in the 2026-07-19 Cowork session; the ratification record is inside the
documents themselves.

**Read first:** `cowork_handoff.md` top block (the 2026-07-19 entry point — it is part of what you
commit), `STATUS.md` (the 2026-07-19 entry), `cowork_joint_estimator_factorization.md` (header
carries the ratification).

## 1. What the commit contains (verify against `git status` — surface anything unexpected)

Expected modified/new, all documentation:

- **New:** `cowork_term_theory_grounding.md` (the theory-derivation half of the audit),
  `cowork_joint_estimator_factorization.md` (★ the ratified structure specification),
  `cc_instruction_design_pass_commit.md` (this file — force-add).
- **Modified:** `cowork_joint_estimator_architecture.md` (§5 rewritten to the remaining agenda; §5a
  the five ratified decisions + the factorization pointer; §6/§7 were committed earlier — verify no
  conflict), `OPEN_ITEMS.md` (OI-179 row: literature half answered, BCMH zip inspected, JEP:HPP
  Method read — three dated bracketed additions), `STATUS.md` (the 2026-07-19 dated entry, including
  the factorization-ratification amendment), `cowork_handoff.md` (the new 2026-07-19 entry-point
  block; the 2026-07-17 block marked superseded), `cowork_handoff_archive.md` (receives the move,
  Task 2), possibly small residual diffs in `docs/research_papers/README.md` / `BIBLIOGRAPHY.md`
  (post-library-commit touch-ups — include them).
- **Must NOT appear:** any `src/` file, any golden, any `tools/corpus` or `tools/robust_stop`
  content, any `.pdf`, anything under `tools/BCMH_dataset/`. `git status` must show the PDF and
  dataset paths still ignored/untracked. **Any unexpected file in the diff ⟹ STOP and report.**

## 2. Task — the handoff archive move (the doc-split discipline)

`cowork_handoff.md` now carries the 2026-07-19 entry-point block at top; the **2026-07-17 block below
it is marked superseded**. Move the ENTIRE 2026-07-17 block (from its `## ★★★★ COWORK SESSION CLOSE
2026-07-17 …` heading down to, but not including, the next `---` section divider that follows it)
**verbatim** to the top of the historical blocks in `cowork_handoff_archive.md`, newest-first, and
remove it from the active file (also remove the "(SUPERSEDED 2026-07-19 …)" annotation Cowork added
to its heading — the archive copy keeps the ORIGINAL heading text; reconstruct it exactly:
`## ★★★★ COWORK SESSION CLOSE 2026-07-17 — THE ARCHITECTURE DECISION: THE KEY/MODE/CHORD ESTIMATOR IS **JOINT (option A), USER-RATIFIED**. THE CURRENT ENTRY POINT.`).
**Reconciliation gate (the doc-split rule):** the moved body must be byte-identical in the archive and
absent from the active file; only the heading line differs in the stated way, and that difference is
recorded in the commit body. If the block's boundaries are ambiguous at the text: STOP and report.

## 3. The commit

**One commit** (this is one change-event: the design-pass session record):

- Subject: `docs: the 2026-07-19 design pass — theory grounding, five ratified decisions, the ratified factorization specification`
- Body: one paragraph naming the five decisions and the factorization ratification (copy the summary
  from the `STATUS.md` 2026-07-19 entry — do not re-word it), plus the handoff-archive reconciliation
  note (§2), plus "all content user-ratified 2026-07-19 in the Cowork session; provenance inside the
  documents."
- Force-add this instruction file.
- **Push to `origin` only.** `upstream` push stays disabled (the standing `cfc7eb5e39` hard stop).

## 4. Self-check before reporting (standing rule)

Re-read the actual diff: no behavior file touched; the handoff reconciliation proven; OPEN_ITEMS row
edits are additive brackets only (no row deleted or renumbered); the STATUS entry matches the
factorization doc's ratified header; no binary tracked. Report: the commit hash, the file list, the
reconciliation result, and the `git status --ignored` confirmation that the PDF library and BCMH
dataset remain untracked.
