# CC Instruction — PUSH the layer-1 checkpoint to the FORK

> User-ratified (2026-06-21): push the completed, ratified layer-1 increment to the fork as a checkpoint. Layer 1
> is a **behavior change** (not byte-identical) — this is a *ratified-correctness* checkpoint, not a byte-identical
> one. Git operation only; no code change.

## §0 — ★ HARD DISTRIBUTION CONSTRAINT (read first)
- **Push to `origin` (`slimvince/MuseScore`, the fork) ONLY** — explicitly allowed.
- **NEVER push to `upstream` (`musescore/MuseScore`)** — already `disabled (push)` at the remote; **leave it
  disabled.** The Stage-4a patch `cfc7eb5e39` is fork-local-only; any push toward `musescore/MuseScore` is a HARD
  STOP. Confirm the target is `origin` before pushing.

## §1 — What to push
HEAD is `4055f89082`; `origin/master` is `dd418ecfed`. The push advances the fork by **exactly 3 commits**
(Cowork-verified):
```
4055f89082  test(composing): Layer 1 — close the branch/block coverage gate (test-only)
e30bb45a4f  feat(composing): Layer 1 — lossless tie-resolved NOTE MODEL + derived tone views
edd33901ed  tools(metric): add standing per-event TIERED oracle-root metric (tool + tests)
```
**Before pushing, confirm `git log --oneline origin/master..HEAD` is exactly these 3 and nothing else.** If
anything else appears → STOP and surface.

## §2 — The push
- **Confirm the held B2 working-tree changes are NOT in any commit** (`git status` — the 3 B2 files +
  pre-existing HELD edits stay unstaged; the push pushes commits, not the working tree, but confirm nothing B2
  rode into a commit). HEAD must be `4055f89082`.
- Push master to the fork with **`--no-recurse-submodules`** (keeps the local `muse` Snap fix out, as the prior
  pushes did): `git push --no-recurse-submodules origin master`
- The pre-push hook should pass. If it FAILS → STOP, report, do not force or bypass.

## §3 — Verify at the actual remote
- `git ls-remote origin master` must return **`4055f89082`** — independently confirms the fork advanced.
- Confirm `upstream` is still `disabled (push)` (unchanged).

## §4 — STATUS.md update (same push, doc bookkeeping)
Record: **Layer 1 (lossless tie-resolved note model) DONE, ratified, and PUSHED** (`origin/master` now
`4055f89082`); the standing oracle-root tiered metric tool committed; the ratified trade-off (the faithful
tie de-inflation moved the oracle metric +3/+1/+1 charged, KEY flat, FLOOR flat, BIR −2/+1/−2, fully tie-explained
— accepted as a correct-upstream/frozen-downstream wobble that re-tunes at layer 3); layer-1 branch coverage
closed (new code 100%, test-only). Note layer 2 (change-point slicing) is next. May be its own small doc-commit;
fork-only if pushed.

## §5 — Deliver
Report: the push result, the `ls-remote origin master` = `4055f89082` confirmation, the upstream-still-disabled
confirmation, and the STATUS.md entry.

## §6 — Stop conditions
- The ahead-set is not exactly the 3 listed commits → STOP.
- The pre-push hook fails, or the remote has diverged → STOP, report, do not force-push.
- Any sign the push target is `upstream` rather than `origin` → STOP immediately.
