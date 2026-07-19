# CC instruction — commit and push the 2026-07-19 pre-fit-gates ratification (docs only)

**Dispatch author:** Cowork, 2026-07-19, at the user's direction. **Type:** pure documentation
commit — **no code, no build, no test, no golden, no corpus, no re-baseline.** The four pre-fit-gate
protocols were user-ratified 2026-07-19 in the Cowork session; the ratification record is in the
gates document's header.

**Read first:** `cowork_handoff.md` top block (2026-07-19 entry, updated), `STATUS.md` (the
2026-07-19 THIRD entry, at the top), `cowork_prefit_gates.md` (header carries the ratification and
the ratified [prov-ratify] constants).

## 1. What the commit contains (verify against `git status` — surface anything unexpected)

- **New:** `cowork_prefit_gates.md` (★ the ratified four protocols),
  `cc_instruction_prefit_gates_commit.md` (this file — force-add, matches `.gitignore` `/cc_*.md`).
- **Modified:** `OPEN_ITEMS.md` (four rows flipped to "PROTOCOL RATIFIED 2026-07-19 … pending
  execution": OI-176, OI-177 in section C; OI-178 in section D; OI-180 in section B — no row deleted
  or renumbered), `STATUS.md` (the 2026-07-19 third entry at top), `cowork_handoff.md` (the
  2026-07-19 block: gates-ratified act added, next-action rewritten to the probe/build arc, the
  state/pending line updated to name this dispatch).
- **Must NOT appear:** any `src/` file, any golden, `tools/corpus`, `tools/robust_stop`, any `.pdf`,
  `tools/BCMH_dataset/`, `cc_uncertain_resolver_measurement_report.md` (stays untracked with its
  on-disk note). The known stray untracked files stay untouched. **Any unexpected file in the diff ⟹
  STOP and report.**

## 2. The commit

**One commit** (one change-event: the pre-fit-gates ratification record):

- Subject: `docs: the four pre-fit gates ratified — OI-176 CV protocol, OI-177 capacity budget, OI-178 adoption protocol, OI-180 dual-path sanction`
- Body: copy the summary from the `STATUS.md` 2026-07-19 third entry (do not re-word), plus: "all
  content user-ratified 2026-07-19 in the Cowork session; provenance in the gates document header."
- Force-add this instruction file.
- **Push to `origin` only.** `upstream` push stays disabled (the standing `cfc7eb5e39` hard stop).

## 3. Self-check before reporting (standing rule)

Re-read the actual diff: no behavior file touched; exactly four OPEN_ITEMS rows changed, status cell
only, none deleted or renumbered; the gates document matches its header's claim (ratified constants
present: 5-fold, count ≥ 20, params ≤ tokens/10, 95 % CI); no binary tracked. Report: the commit
hash, the file list, and `git status --ignored` confirmation that the PDF library, BCMH paths, and
the measurement report remain untracked.
