# CC Instruction — PUSH the Layer-2 corpus-validation commit to the FORK

> Cowork-verified (2026-06-21): the corpus-validation harness commit is sound (independent oracle, diagnostic-only,
> 353/353), the held B2 work is intact (confirmed at source via direct file reads), and the earlier "index
> corruption" was a cross-platform sandbox artifact, not real. Push the one validation commit to the fork.
> **Git operation only.**

## §0 — ★ HARD DISTRIBUTION CONSTRAINT
- Push to **`origin` (`slimvince/MuseScore`) ONLY**. **NEVER `upstream`** (`musescore/MuseScore`; disabled — leave
  it). Confirm the target is `origin` before pushing.

## §1 — What to push (exactly one commit)
- `origin/master` = `157981bd1f`; local HEAD = `566d64d383` (the corpus-validation commit, parent `157981bd1f`).
- Confirm `git log --oneline origin/master..HEAD` is EXACTLY `566d64d383` and nothing else → else STOP.
- Confirm `git show --stat 566d64d383` = exactly `tools/batch_analyze.cpp` + `tools/validate_slices_corpus.py`
  (harness only) → else STOP.

## §2 — Working tree stays untouched
- The held/unstaged work must NOT ride into the push and must remain on disk: the **B2 trio**
  (`localmodulationdetector.{cpp,h}`, the B2 delta in `tools/batch_analyze.cpp`), `ARCHITECTURE.md` forward-pointer,
  `STATUS.md`, and the other modified working docs. Confirm `git diff --cached --name-only` is **empty** (nothing
  staged) and HEAD is `566d64d383`.

## §3 — Push + verify at the remote
- `git push --no-recurse-submodules origin master`. Pre-push hook must pass (no force/bypass).
- `git ls-remote origin master` must return **`566d64d383`**; confirm `upstream` still `disabled (push)`.

## §4 — STATUS.md + deliver
- STATUS.md: Layer 2 corpus-validation (`566d64d383`) PUSHED — 353/353 invariant-pass against an independent
  oracle, real slicer proven on the corpus, byte-identical/isolated; B2 + WIP remain held/unstaged. Layer 2 is now
  built + unit-tested + corpus-validated + pushed; Layer 3 (wires in the slicer) is next.
- Report: the ahead-set = `566d64d383`-only confirmation, the harness-only `--stat`, the push result, the
  `ls-remote` = `566d64d383` confirmation, upstream-still-disabled, and that B2/WIP stayed unstaged.

## §5 — Stop conditions
- Ahead-set ≠ exactly `566d64d383`, or the commit touches anything beyond the 2 harness files → STOP.
- Pre-push hook fails / remote diverged → STOP (no force).
- Any sign the target is `upstream` → STOP immediately.
