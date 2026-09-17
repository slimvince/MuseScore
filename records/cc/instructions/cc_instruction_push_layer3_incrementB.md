# CC Instruction — PUSH Layer-3 Increment B to the FORK

> User-ratified (2026-06-22): push the read-only ground-truth harness commit to the fork. Git only; no code change.

## §0 — HARD DISTRIBUTION CONSTRAINT
- Push to **`origin` (`slimvince/MuseScore`) ONLY**. **NEVER `upstream`** (disabled; leave it). Confirm before pushing.

## §1 — What to push (exactly one commit)
- `origin/master` = `4bce14e804`; local HEAD = `dcbc0bb4e1…` (Increment B, parent `4bce14e804`).
- Confirm `git log --oneline origin/master..HEAD` is EXACTLY `dcbc0bb4e1…` and nothing else → else STOP.
- Confirm `git show --stat dcbc0bb4e1` = only `tools/cc_layer3_keymode_baseline.py` (harness, read-only) → else STOP.

## §2 — Working tree untouched
- Held WIP (B2 trio, docs, STATUS, the pre-existing `compare_rn.py` M) stays **unstaged**; `git diff --cached
  --name-only` empty; HEAD unchanged.

## §3 — Push + verify
- `git push --no-recurse-submodules origin master`. Pre-push hook must pass (no force/bypass).
- `git ls-remote origin master` must return **`dcbc0bb4e1…`**; confirm `upstream` still `disabled (push)`.

## §4 — STATUS.md + deliver
- STATUS.md: Layer-3 Increment B (held-out direct key/mode GT harness, read-only) PUSHED; honest held-out baseline
  Baroque 87.3% / Jazz 61.5% (the audit's Jazz 91.5% was a 39%-drop artifact, now fixed); metrics provisional /
  directional until the full pipeline is rebuilt. Next: Increment C (key-path decoder).
- Report: the ahead-set = `dcbc0bb4e1`-only confirmation, the harness-only `--stat`, the push result, `ls-remote` =
  `dcbc0bb4e1`, upstream-still-disabled, and that WIP stayed unstaged.

## §5 — Stop conditions
- Ahead-set ≠ exactly `dcbc0bb4e1`, or the commit touches any production file → STOP.
- Pre-push hook fails / remote diverged → STOP (no force). Any sign the target is `upstream` → STOP.
