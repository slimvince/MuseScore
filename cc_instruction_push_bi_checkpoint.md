# CC Instruction — PUSH the byte-identical refactor checkpoint to the FORK

> User-ratified (2026-06-17): push the verified byte-identical refactor batch to the fork as a clean known-good
> baseline **before** the behavior-sensitive step 3 (the anchor). This is a git operation only — no code change.

## §0 — ★ HARD DISTRIBUTION CONSTRAINT (read first)
- **Push to `origin` (`slimvince/MuseScore`, the user's fork) ONLY.** This is explicitly allowed.
- **NEVER push to `upstream` (`musescore/MuseScore`).** `upstream` push is already disabled at the remote
  (`upstream … disabled (push)`) — **leave it disabled; do NOT re-enable it.** The Stage-4a patch `cfc7eb5e39`
  is in the fork's history (fork-local-only per CLAUDE.md); any push/PR toward `musescore/MuseScore` is a HARD
  STOP. This push goes to the fork, so it is fine — just confirm the target is `origin` before you push.

## §1 — What to push
HEAD is `dd418ecfed`. `origin/master` is at `5fee657578`. The push advances the fork by **exactly 6
byte-identical refactor commits** (Cowork-verified — all `refactor:`, all gates byte-identical):
```
dd418ecfed  refactor(region): de-duplicate inline same-chord merge predicate (step 2)
8bc1441076  refactor(analysis): extract shared pc/collection primitives (step 1)
a03c2493bb  refactor: split keymodeanalyzer.cpp
2024f2951e  refactor: split sectionanalyzer.cpp
ed4b462021  refactor: split regiontonecollector.cpp
41f7c65f63  refactor: split chordanalyzer.cpp
```
**Before pushing, confirm `git log --oneline origin/master..HEAD` is exactly these 6 and nothing else** (no
stray commit, no behavior-change commit). If anything else appears → STOP and surface.

## §2 — The push
- **Confirm the held B2 working-tree changes are NOT staged/committed** (`git status` — the 3 B2 files
  + HELD docs stay unstaged; the push pushes commits, not the working tree, but confirm nothing B2 sneaked into
  a commit). HEAD must be `dd418ecfed`.
- Push master to the fork with **`--no-recurse-submodules`** (keeps the local `muse` Snap fix out of the push,
  as the prior `5fee657578` push did):
  `git push --no-recurse-submodules origin master`
- The pre-push hook should pass (it did for `5fee657578`). If it FAILS → STOP, report the failure, do not
  force or bypass.

## §3 — Verify at the actual remote (not the local ref)
- `git ls-remote origin master` must return **`dd418ecfed`** — independently confirms the fork advanced.
- Confirm `upstream` is still `disabled (push)` (unchanged).

## §4 — STATUS.md update (same push, doc bookkeeping)
Add a current-state entry recording: **steps 1+2 of the architecture-fix phase are DONE and PUSHED to the fork**
(`8bc1441076` S3-primitive extraction; `dd418ecfed` inline merge-predicate de-dup; both Cowork-verified
byte-identical; `origin/master` now `dd418ecfed`). Also record the **B2 = 3-file correction** (the held B2
guard set is `section/localmodulationdetector.cpp` + `.h` + `tools/batch_analyze.cpp` — the §0.5 instruction
undercounted it as 2; any future stash/revert of B2 must include all three). This STATUS.md edit may be its own
small commit (doc-only) — your call whether to push it too or leave it local; if you push it, same fork-only
rule.

## §5 — Deliver
Report: the push result, the `ls-remote origin master` = `dd418ecfed` confirmation, the upstream-still-disabled
confirmation, and the STATUS.md entry. Then step 3 (the anchor instruction) follows from Cowork.

## §6 — Stop conditions
- The ahead-set is not exactly the 6 listed BI commits → STOP.
- The pre-push hook fails, or the remote has diverged (someone else pushed) → STOP, report, do not force-push.
- Any sign the push target is `upstream` rather than `origin` → STOP immediately.
