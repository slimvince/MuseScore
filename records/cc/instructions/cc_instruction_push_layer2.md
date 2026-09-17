# CC Instruction — PUSH the Layer-2 commit to the FORK

> User-ratified (2026-06-21): push the verified, ratified Layer-2 increment to the fork. **Git operation only; no
> code change.** One doc/code commit on top of the pushed layer-1 doc-sync.

## §0 — ★ HARD DISTRIBUTION CONSTRAINT (read first)
- **Push to `origin` (`slimvince/MuseScore`, the fork) ONLY.**
- **NEVER push to `upstream` (`musescore/MuseScore`)** — it is `disabled (push)`; leave it disabled. Any push
  toward `musescore/MuseScore` is a HARD STOP. Confirm the target is `origin` before pushing.

## §1 — What to push (exactly one commit)
- `origin/master` is currently `257b55c9f4` (the pushed layer-1 doc-sync).
- Local HEAD is `e470e2667e` — the Layer-2 slicer commit, parent `257b55c9f4`.
- **Before pushing, confirm `git log --oneline origin/master..HEAD` is EXACTLY `e470e2667e` and nothing else.** If
  anything else appears → STOP and surface.

## §2 — Confirm the working tree is untouched
- The pre-existing WIP stays **unstaged in the working tree** and must NOT ride into the push: the
  `docs/implementation_roadmap.md` ~509-line rewrite + the Layer-2/L3 roadmap edits, the `ARCHITECTURE.md`
  2026-06-15 forward-pointer hunk, and the held B2 files (`localmodulationdetector.{cpp,h}`, `batch_analyze.cpp`).
  Confirm `git status` shows these unstaged and **nothing new staged**; HEAD remains `e470e2667e`. (The push pushes
  the commit, not the working tree — but confirm nothing extra was committed.)

## §3 — The push
- `git push --no-recurse-submodules origin master` (keeps the local `muse` Snap fix out, as prior pushes did).
- Pre-push hook should pass. If it FAILS → STOP, report, do not force or bypass.

## §4 — Verify at the actual remote
- `git ls-remote origin master` must return **`e470e2667e`** — independently confirms the fork advanced.
- Confirm `upstream` is still `disabled (push)` (unchanged).

## §5 — STATUS.md bookkeeping (same push)
Record: **Layer 2 (deterministic change-point slicer, isolated `slicing/` module) BUILT, ratified, and PUSHED**
(`origin/master` → `e470e2667e`); 100% covered; byte-identical/isolated (not wired in until L3). Note the
`docs/implementation_roadmap.md` Layer-2 entry is **still OWED** (blocked by an unrelated ~509-line roadmap WIP
rewrite, to be adjudicated). Layer 3 (per-slice analysis — the slicer gets wired in) is next.

## §6 — Deliver
Report: the `origin/master..HEAD` = `e470e2667e`-only confirmation, the push result, the `ls-remote origin master`
= `e470e2667e` confirmation, the upstream-still-disabled confirmation, and the STATUS.md entry.

## §7 — Stop conditions
- The ahead-set is not exactly `e470e2667e` → STOP.
- The commit touches anything beyond the verified Layer-2 fileset → STOP.
- The pre-push hook fails, or the remote diverged → STOP, report, do not force-push.
- Any sign the push target is `upstream` rather than `origin` → STOP immediately.
