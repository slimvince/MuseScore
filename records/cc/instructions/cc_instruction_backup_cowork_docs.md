# CC Instruction — back up the Cowork design/architecture docs to the fork (version-control for backup)

> **User decision (2026-06-22):** track the untracked `cowork_*.md` design/architecture docs in the fork so they are
> version-controlled and backed up (they currently exist only as untracked local files — no history, no backup).
> Internal Cowork/CC workflow language is fine for now; **a tidy-up / prune pass of anything we don't want to publish
> is planned for later.** Fork-local: push `origin` (slimvince/MuseScore) **only, NEVER `upstream`**.

## §1 — Commit the `cowork_*.md` docs (docs-only backup)
- `git add` every `cowork_*.md` at the repo root. First enumerate the set (`ls cowork_*.md` / `git status --porcelain
  cowork_*.md`) and list them in the report so the backup set is on record (the layer design docs, the
  target-architecture doc, the gate-policy amendment, the design-doc template, the handoff/standing-rules doc, etc.).
- Commit message: `docs: back up Cowork design + architecture docs (version-control for backup; prune before any publish)`.

## §2 — Do NOT sweep in code WIP or other holds
- **Leave the B2 trio unstaged** (`tools/batch_analyze.cpp`, `…/section/localmodulationdetector.{cpp,h}`) — that is
  deliberately-held *unfinished code*, not a backup doc. Do not stage any source file.
- Leave the modified-tracked holds as-is: `tools/compare_rn.py` (M) and the `STATUS.md` OQ-1 WIP.
- `cc_*` (CC reports + instructions) stay **gitignored** — out of scope for this backup.

## §3 — Surface the rest for a separate decision (do NOT commit)
List the other **untracked-and-not-ignored** files that are *not* `cowork_*.md` and *not* `cc_*` (e.g.
`docs/back_half_design.md`, `docs/decoder_design.md`, `BUILD_AND_TEST.md`, and anything else). **Report them, do not
commit** — Cowork + user decide per file whether it's a current doc worth backing up or stale to discard.

## §4 — Push
- Push to **`origin` only. NEVER `upstream`** (disabled; hard stop). Report the new `origin/master` SHA and confirm
  at the actual remote via `git ls-remote`.

## §5 — Stop conditions
- Any **code** file (B2 trio or otherwise) about to be staged → STOP (this is a docs-only backup).
- A push would target `upstream` → STOP.
