# CC Instruction — PUSH the doc-sync commit to the FORK

> User-approved (2026-06-21): push the layer-1 documentation-sync commit to the fork so origin's docs match its
> code. **Git operation only; no code change.** Doc-only commit on top of the already-pushed layer-1 checkpoint.

## §0 — ★ HARD DISTRIBUTION CONSTRAINT (read first)
- **Push to `origin` (`slimvince/MuseScore`, the fork) ONLY.**
- **NEVER push to `upstream` (`musescore/MuseScore`)** — it is `disabled (push)`; leave it disabled. Any push
  toward `musescore/MuseScore` is a HARD STOP. Confirm the target is `origin` before pushing.

## §1 — What to push (exactly one commit)
- `origin/master` is currently `4055f89082` (the pushed layer-1 checkpoint — Cowork confirmed via `git ls-remote`).
- Local HEAD is `257b55c9f4` — the single doc-sync commit (`docs(composing): sync architecture docs to the
  layer-1 note-model as-built`), parent `4055f89082`.
- **Before pushing, confirm `git log --oneline origin/master..HEAD` is EXACTLY `257b55c9f4` and nothing else.** If
  anything else appears → STOP and surface.
- **Confirm the commit is doc-only:** `git show --stat 257b55c9f4` touches only `ARCHITECTURE.md`,
  `docs/implementation_roadmap.md`, `docs/layer_architecture_audit.md` — no `.cpp`/`.h`. If any source file
  appears → STOP.

## §2 — Confirm the working tree is untouched
- The HELD edits (the un-ratified 2026-06-15 forward pointer in `ARCHITECTURE.md`, re-baseline/refactor blocks) and
  the held B2 changes stay **unstaged in the working tree** — the push pushes the *commit*, not the working tree.
  Confirm `git status` still shows those HELD edits unstaged and that **nothing new is staged**. HEAD must remain
  `257b55c9f4`.

## §3 — The push
- `git push --no-recurse-submodules origin master` (keeps the local `muse` Snap fix out, as prior pushes did).
- The pre-push hook should pass. If it FAILS → STOP, report, do not force or bypass.

## §4 — Verify at the actual remote
- `git ls-remote origin master` must return **`257b55c9f4`** — independently confirms the fork advanced.
- Confirm `upstream` is still `disabled (push)` (unchanged).

## §5 — STATUS.md bookkeeping (same push)
Record: **layer-1 documentation sync (`257b55c9f4`) PUSHED to `origin/master`** — `ARCHITECTURE.md` + roadmap +
layer-audit now reflect the note-model as-built; the standing "all documentation in sync" rule is in force; layer 2
(change-point slicing) is **signed off**, read-only audit next.

## §6 — Deliver
Report: the `origin/master..HEAD` = `257b55c9f4`-only confirmation, the doc-only `--stat`, the push result, the
`ls-remote origin master` = `257b55c9f4` confirmation, the upstream-still-disabled confirmation, and the STATUS.md
entry.

## §7 — Stop conditions
- The ahead-set is not exactly `257b55c9f4` → STOP.
- The commit touches any source file → STOP.
- The pre-push hook fails, or the remote diverged → STOP, report, do not force-push.
- Any sign the push target is `upstream` rather than `origin` → STOP immediately.
