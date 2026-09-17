# CC instruction — commit and push the 2026-07-19 desk-simulation ratification (docs only, one small erratum edit)

**Dispatch author:** Cowork, 2026-07-19, at the user's direction. **Type:** documentation commit —
**no code, no build, no test, no golden, no corpus, no re-baseline.** Everything here was
user-ratified 2026-07-19 in the Cowork session (the desk simulation and its findings); the
ratification record is inside the documents.

**Read first:** `cowork_handoff.md` top block (2026-07-19 entry, updated), `STATUS.md` (the
2026-07-19 SECOND entry, at the top), `cowork_factorization_desk_simulation.md` (header carries the
ratification and the granted §7 asks).

## 1. The erratum (desk-sim finding §4.6) — CORRECTED 2026-07-19 after CC's stop

**Original dispatch error (Cowork's, owned):** this section previously directed an erratum edit to
`cc_uncertain_resolver_measurement_report.md` and listed that file as "Modified" — but the report was
NEVER tracked (untracked/ignored per `/cc_*.md`; CC verified no git history). **The user's call: keep
it untracked.** The erratum's TRACKED record is `cowork_factorization_desk_simulation.md` §4.6 (in
this commit); CC's already-made on-disk note in the report stays as an uncommitted courtesy
annotation. **Do not force-add the report; do not revert the on-disk note.**

## 2. What the commit contains (verify against `git status` — surface anything unexpected)

- **New:** `cowork_factorization_desk_simulation.md` (★ the ratified desk simulation),
  `cc_instruction_desk_sim_commit.md` (this file — force-add, matches `.gitignore` `/cc_*.md`).
- **Modified:** `cowork_joint_estimator_factorization.md` (header ratification note; §2 the factor-
  granularity amendment block; §3 item 3 per-event mark; §3 item 10 the settled initial-state-only
  prior; §6 stage-run banner; §7 the settled-question note), `OPEN_ITEMS.md` (OI-181 flipped
  ✅ RESOLVED; NEW rows OI-184, OI-185 in section D), `STATUS.md` (the new 2026-07-19 second entry at
  top), `cowork_handoff.md` (the 2026-07-19 block updated in place: desk-sim-done + next-action +
  state/pending; also an earlier small fix this session — the stale "block below" parenthetical
  replaced with an archive pointer to `910a998e9b`). `cc_uncertain_resolver_measurement_report.md`
  stays UNTRACKED (§1) — it must NOT appear in the commit.
- **Must NOT appear:** any `src/` file, any golden, `tools/corpus`, `tools/robust_stop`, any `.pdf`,
  `tools/BCMH_dataset/`. The stray untracked files you flagged at the design-pass commit
  (`idiom_discovery/*`, the 0-byte `key`, `scratch_artifacts/`, `tools/robust_stop/*_root_fail_cells.txt`)
  stay untouched and uncommitted. **Any unexpected file in the diff ⟹ STOP and report.**

## 3. The commit

**One commit** (one change-event: the desk-simulation stage record and its ratified consequences):

- Subject: `docs: the factorization desk simulation — run, ratified; granularity amendment; prior settled initial-only; OI-181 closed`
- Body: copy the summary from the `STATUS.md` 2026-07-19 second entry (do not re-word — it now
  carries the corrected erratum-disposition wording), plus: "all content user-ratified 2026-07-19 in
  the Cowork session; provenance inside the documents."
- Force-add this instruction file.
- **Push to `origin` only.** `upstream` push stays disabled (the standing `cfc7eb5e39` hard stop).

## 4. Self-check before reporting (standing rule)

Re-read the actual diff: no behavior file touched; the OPEN_ITEMS edits are one row flipped with
provenance + two rows added, none deleted or renumbered; the factorization-doc amendments carry their
dated ratification marks and nothing else in that file moved;
`cc_uncertain_resolver_measurement_report.md` is NOT in the commit (its on-disk note intact); no
binary tracked. Report: the commit hash, the file list, and `git status --ignored` confirmation that
the PDF library, BCMH paths, and the measurement report remain untracked.
