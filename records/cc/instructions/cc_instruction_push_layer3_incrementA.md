# CC Instruction — PUSH Layer-3 Increment A to the FORK

> User-ratified (2026-06-22): push the byte-identical L1 query-indexing commit to the fork. Git only; no code change.

## §0 — HARD DISTRIBUTION CONSTRAINT
- Push to **`origin` (`slimvince/MuseScore`) ONLY**. **NEVER `upstream`** (disabled; leave it). Confirm before pushing.

## §1 — What to push (exactly one commit)
- `origin/master` = `566d64d383`; local HEAD = `4bce14e80…` (Increment A, parent `566d64d383`).
- Confirm `git log --oneline origin/master..HEAD` is EXACTLY `4bce14e80…` and nothing else → else STOP.
- Confirm `git show --stat 4bce14e80` = only `note_model.{h,cpp}` + `note_model_tests.cpp` → else STOP.

## §2 — Working tree untouched
- The held WIP (B2 trio, docs, STATUS) stays **unstaged**; `git diff --cached --name-only` is empty; HEAD unchanged.

## §3 — Push + verify
- `git push --no-recurse-submodules origin master`. Pre-push hook must pass (no force/bypass).
- `git ls-remote origin master` must return **`4bce14e80…`**; confirm `upstream` still `disabled (push)`.

## §4 — STATUS.md + deliver
- STATUS.md: Layer-3 Increment A (NoteModel query indexing, byte-identical, O(N²)→O(N log N)) PUSHED; identical-results
  proven (IDX1–4 vs linear oracle); 576/57/11 byte-identical. Next: Increment B (held-out ground-truth harness).
- Report: the ahead-set = `4bce14e80`-only confirmation, the `--stat`, the push result, `ls-remote` = `4bce14e80`,
  upstream-still-disabled, and that B2/WIP stayed unstaged.

## §5 — Stop conditions
- Ahead-set ≠ exactly `4bce14e80`, or the commit touches anything beyond the 3 files → STOP.
- Pre-push hook fails / remote diverged → STOP (no force). Any sign the target is `upstream` → STOP.
