# Cowork — PRUNE / TIDY PASS checklist (deferred, do before any publish)

> **Standing deferral (user, 2026-06-22):** "back up now, tidy up files we don't want to publish later." This is the
> running list of prune/tidy decisions to make **before any publish** of the fork (`origin = slimvince/MuseScore`).
> Nothing here is to be acted on now — it is the to-do for the prune pass. Keep appending as items arise.

## 1. ⛔ `cowork_github_9444_comment_draft.md` — DELETE (distribution-constraint sensitive)
- The draft contains the **`cfc7eb5e39`** patch content (the `addKey()` mode-dedup fix) and is framed "for Vincent to
  post" on upstream `musescore/MuseScore#9444`, with a PR offer. Posting it / opening that PR = **HARD-STOP** under the
  CLAUDE.md ★ DISTRIBUTION CONSTRAINT (cfc7eb5e39 is fork-local-only, never toward `musescore/MuseScore`).
- It predates the constraint (draft 2026-06-14; constraint 2026-06-15) — a superseded artifact of the old
  advocate-upstream stance.
- **Status now:** a local-only `SUPERSEDED — DO NOT POST` banner is on the working copy (uncommitted); the copy **on
  the fork** (committed `f2dd0b0e98`) still lacks the banner.
- **Prune action:** delete the file. **Note:** it is already in fork *history* (`f2dd0b0e98`) — deleting the working
  file does not purge history; a full history rewrite is a separate decision if it must be unrecoverable from the fork.
- **Confirm:** it was never actually posted to upstream #9444 (the pre-post checklist in it is unchecked → appears
  never posted — verify).

## 2. Test-data extraction scratch under `src/composing/tests/data/` — gitignore or delete
- `META-INF/`, `Thumbnails/`, `audiosettings.json`, `automation.json`, `score_style.mss`, `viewsettings.json` — these
  are the standard innards of an **unzipped `.mscz`**, not intended fixtures (the fixtures are the `.mscz`/`.xml`).
- **Prune action:** verify no test references them, then gitignore or delete. Do not delete real fixtures.

## 3. Root / tools scratch — gitignore or delete
- `err.txt`; `tools/b2_measure.sh`; `tools/dump_bir_cases.py`; `tools/iter90_wrong_root_characterization.txt`;
  `tools/iter97_birfalse_cases_data.txt` (the non-`cc_`-prefixed scratch the `tools/cc_*` ignore rule doesn't cover).
- **Prune action:** gitignore or delete (transient iteration dumps / ad-hoc scripts; none load-bearing).

## 4. `ai-assistant/` (13 files) — exclude from this fork
- A separate **read-only share** whose source lives elsewhere (ms-core-api): a second `CLAUDE.md`, `ROADMAP.md`,
  `TODO.md`, SMOKETEST results, `handover.md`, `GITHUB_COMMENT_24673.md`, etc. Does not belong in this fork.
- **Prune action:** leave local / gitignore; do not commit to the fork.
- Note: `GITHUB_COMMENT_24673.md` is **clear of the distribution constraint** (an ordinary plugin/extension bug
  report, no `cfc7eb5e39` content) — posting it is the user's normal call, unrelated to the fork-local mandate.

## 5. Publish-language review (all backed-up docs)
- The `cowork_*.md` and `docs/*.md` design docs were backed up to the fork with **internal Cowork/CC workflow
  language** intact (intentionally, for backup). Before any publish, review them and decide per file: keep
  (fork-private), sanitize (strip workflow/process language), or drop. The fork patches are fork-local-only, so this
  is mainly about not publishing internal process narrative.

## 6. Standing guard (not a prune item — a permanent rule)
- **Any** upstream GitHub comment / PR / contribution must be checked against the CLAUDE.md distribution constraint
  **before** posting. A draft carrying a fork-local-constrained patch (`cfc7eb5e39`, #9444) is a **HARD STOP** — never
  post. Non-constrained reports (e.g. #24673) are the user's normal call.
