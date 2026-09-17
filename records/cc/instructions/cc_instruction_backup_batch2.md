# CC Instruction — backup batch 2: design docs under docs/ + contrapunctus_findings.md; gitignore transient tools/cc_*

> Continuing the docs-only backup (user, 2026-06-22): version-control the remaining untracked **design docs** for
> backup, and bring the stray `tools/cc_*` under the same gitignore treatment as the root `cc_*` reports. Prune pass
> for anything we don't want to publish is still planned. Fork-local: push **`origin` only, NEVER `upstream`**.

## §1 — Back up the untracked design docs (docs-only)
- `git add` the untracked-and-not-ignored design docs and commit:
  `docs/architecture_joint_inference.md`, `docs/beam_widening_design.md`, `docs/layer_audit_plan.md`,
  `docs/precision_metric_design.md`, `docs/scoped_joint_design.md`, `docs/stage4c_cadence_key_design.md`,
  `docs/stage4d_local_modulation_design.md`, `docs/stage6_functional_layer_design.md`, and
  `contrapunctus_findings.md` (root).
- First enumerate the exact set (`git status --porcelain` filtered to these) and list it in the report — the backup
  set on record. **Docs-only: do not stage any code file.**
- Commit message: `docs: back up design docs (docs/*.md + contrapunctus_findings.md) — version-control for backup; prune before any publish`.

## §2 — Gitignore the transient `tools/cc_*`
- Add `tools/cc_*` to `.gitignore` (only root `/cc_*.md` is currently ignored; this extends the same transient
  treatment to the `tools/` cc-named scratch: `cc_*.py` / `cc_*.json` / `cc_*.err` / dumps).
- **Confirm the load-bearing harness `tools/cc_layer3_keymode_baseline.py` stays TRACKED** — it is already committed,
  and gitignore does not untrack an already-tracked file, but verify `git status` still shows it tracked (not
  ignored-and-removed). If any **other** `tools/cc_*` file is load-bearing **and** untracked, **surface it** rather
  than ignoring (we back that one up, not ignore it).
- Commit the `.gitignore` change with §1 (or as a small separate commit — your call), message noting "ignore
  transient tools/cc_* scratch (consistent with root /cc_*)".

## §3 — Do NOT commit (leave as-is / surface only)
- **`ai-assistant/`** (13 files incl. a second `CLAUDE.md`, `GITHUB_COMMENT_24673.md`): a separate read-only share
  whose source lives elsewhere (ms-core-api) — **do not commit to this fork.** Leave local.
- **Test-data extraction artifacts** under `src/composing/tests/data/` (`META-INF/`, `Thumbnails/`, `*.json`,
  `score_style.mss`, …), `err.txt`, and the `tools/*.txt` / `tools/*.sh` scratch dumps: these look like unzipped-`.mscz`
  innards / scratch, **not** intended fixtures. **Do not commit; surface the list** — confirm they are scratch (vs a
  real intended fixture) before we decide to gitignore or delete. Do not auto-gitignore real test fixtures.
- The held code WIP (B2 trio) and modified-tracked holds (`compare_rn.py`, `STATUS.md` OQ-1) — untouched, as before.

## §4 — Push
- Push **`origin` only. NEVER `upstream`** (disabled; hard stop). Report the new `origin/master` SHA + `git ls-remote`
  confirmation.

## §5 — Stop conditions
- Any **code** file about to be staged → STOP (docs + .gitignore only).
- `tools/cc_layer3_keymode_baseline.py` (or another load-bearing tool) would become untracked by the gitignore → STOP, surface.
- A push would target `upstream` → STOP.
