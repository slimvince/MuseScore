# CC Instruction — Layer 3: doc-sync commit (gate amendment + as-built), then PUSH both commits to the fork

> The Step-1 wiring is committed locally (`a6b08af3fe`) and Cowork-verified at the git object (17 files, exclusions
> correct). Before the push, land a **Cowork doc-sync commit** so the fork carries the rule + the change + the docs
> in sync — the two-tier gate amendment that permits this commit's accepted Jazz +1 is currently uncommitted. Then
> push **both** commits (wiring + doc-sync) to `origin`.

## §1 — The doc-sync commit (a NEW commit on top of `a6b08af3fe`; do NOT rebase/reorder)
Stage and commit exactly these (Cowork already edited the design files this session):
- **`CLAUDE.md`** — the two-tier BIR-gate amendment + the refined guardrail (3) + the recorded Jazz interim case
  (Cowork-edited; commit as-is).
- **`ARCHITECTURE.md`** — **you update this** (the canonical as-built): record that the Layer-3 key/mode path is now
  the decoder (Step-1 wiring `a6b08af3fe`) — the decoder replaces the per-region resolver at the seam
  (duration-majority per coarse region; S2 seed; `excludeStaves` + `partialSignatureCorrection` + C1 fidelity
  fixes); the retired pieces (the @633 resolver call + hysteresis + `prevKeyResult`; `collectPitchContext` as the
  region builder); and the surfaced residuals (P4 still on the resolver → P4-redecode follow-up; resolver +
  `collectPitchContext` remain only as the diagnostic/grading baseline). Keep it factual and consistent with
  `cc_layer3_wiring_report.md`.
- **The tracked Cowork design docs** changed this session — verify which are tracked with `git ls-files` (the
  `cowork_*.md` set: the Layer-3 design doc, the target-architecture doc, the gate-policy amendment doc). Commit the
  tracked ones; if any `cowork_*.md` is gitignored, leave it local (do not force-add).

Commit message: `docs(composing): Layer 3 — two-tier BIR gate amendment + as-built wiring sync`.

## §2 — Verify before committing (no silent re-baseline)
- **CLAUDE.md canonical class-(b) identity sets UNCHANGED.** Confirm the documented Baroque-57 / Jazz-23 / Default-57
  case-identity lists are **byte-identical** to before — the amendment adds the two-tier *policy* and the Jazz interim
  *record* only; it does **not** re-baseline the identity sets (a deliberate re-baseline is a separate, later
  doc-sync). If any identity-set line changed → STOP and surface.
- ARCHITECTURE.md reflects the wiring accurately (no drift vs the wiring report); the design-doc content is Cowork's —
  commit as-is, do not rewrite.

## §3 — Push BOTH commits to the fork
- Push `a6b08af3fe` (wiring) **and** the doc-sync commit to **`origin/master`** in one push. **NEVER `upstream`**
  (disabled; hard stop). Report the new `origin/master` SHA (should advance `2203ad9fda` → doc-sync HEAD, +2 commits)
  and confirm via `git ls-remote` at the actual remote.

## §4 — Leave untouched / held
- Do **not** stage or commit: the **B2 trio** (`batch_analyze.cpp`, `localmodulationdetector.{cpp,h}`), the **OQ-1
  STATUS.md WIP** (the portion stashed/restored after the wiring commit — leave it unstaged), and any other WIP docs.
  `cc_*` reports stay gitignored/local.

## §5 — Stop conditions
- Any CLAUDE.md class-(b) identity-set line changed (a silent re-baseline) → STOP, surface.
- ARCHITECTURE.md would need a claim not supported by the wiring report → STOP, surface (don't invent).
- A push would target `upstream`, or would carry the B2 trio / OQ-1 WIP → STOP.
