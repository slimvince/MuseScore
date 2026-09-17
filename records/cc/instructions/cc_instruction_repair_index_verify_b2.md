# CC Instruction — REPAIR the corrupted git index + RE-VERIFY the held B2 work (DO NOT PUSH yet)

> Cowork found the git **index is corrupted** — `git status` returns `fatal: cache entry out of order` — a side
> effect of the manual B2 backup/revert/restage/restore around the corpus-validation commit. **Objects, commits,
> and refs are intact** (Cowork verified `cat-file`/`show`/`diff <sha> <sha>`/`ls-remote` all succeed; only
> index-reading commands fail). This is **index-only** corruption: no data loss, but staging/status are unreliable
> until the index is rebuilt. **Do NOT push and do NOT start L3 until this is repaired and B2 is re-confirmed.**
>
> **★ The point of caution:** the three HELD B2 files carry un-ratified work that must survive intact. A rebuild
> from HEAD does **not** touch working-tree files, but back them up first anyway (belt-and-suspenders).

## §1 — Back up the held / unstaged work FIRST (before touching the index)
Copy the current on-disk (working-tree) content of every held/unstaged file to a safe location OUTSIDE the repo
(e.g. `C:\tmp\b2_backup\`), so nothing can be lost:
- `src/composing/analysis/section/localmodulationdetector.cpp`
- `src/composing/analysis/section/localmodulationdetector.h`
- `tools/batch_analyze.cpp`
- `docs/implementation_roadmap.md` (the WIP rewrite + L2/L3 edits)
- `ARCHITECTURE.md` (the forward-pointer hunk)
- `STATUS.md`
Record each file's SHA-256 (or size+mtime) so you can prove post-repair the working-tree content is byte-identical.

## §2 — Repair the index (rebuild from HEAD; working tree is NOT touched)
- Confirm HEAD first: `git rev-parse HEAD` must be `566d64d383…` (the corpus-validation commit). If it is NOT →
  STOP and surface (something else is wrong).
- Rebuild the index: `rm -f .git/index && git reset` (mixed reset to HEAD — repopulates the index from the HEAD
  tree; **working-tree files are left exactly as they are on disk**). If `git reset` reports anything other than
  the expected "Unstaged changes after reset" listing → capture it and surface.
- (If `cache entry out of order` somehow persists, `git read-tree HEAD` then retry `git status`.)

## §3 — Re-verify (the index is healthy and nothing was lost)
1. `git status` now runs cleanly (no `cache entry out of order`).
2. `git rev-parse HEAD` still `566d64d383…`; `git ls-remote origin master` still `157981bd1f…` (fork unchanged —
   the validation commit is local/unpushed, correctly still ahead by 1).
3. The harness commit is intact: `git show --stat 566d64d383` = exactly `tools/batch_analyze.cpp` +
   `tools/validate_slices_corpus.py`.
4. **B2 + WIP intact and UNSTAGED:** `git status --short` shows `localmodulationdetector.{cpp,h}`,
   `tools/batch_analyze.cpp`, `docs/implementation_roadmap.md`, `ARCHITECTURE.md`, `STATUS.md` as modified (`M`)
   and **unstaged**; `git diff --cached --name-only` is **empty** (nothing staged).
5. **No content loss:** each §1 file's working-tree SHA-256 matches its backup (byte-identical — the rebuild did
   not alter working-tree content). Explicitly confirm `tools/batch_analyze.cpp` still contains BOTH the committed
   `--validate-slices` harness AND its restored B2 hunks (i.e. the working tree = committed harness + B2 delta);
   report the `git diff 566d64d383 -- tools/batch_analyze.cpp` so Cowork can see the B2 delta is present.

## §4 — Deliver (NO push)
Report: the repair command used, the §3 checks (status clean; HEAD/remote unchanged; harness commit intact; the
five files unstaged; the SHA-256 match table; the `batch_analyze.cpp` B2-delta diff). **Do not push** — Cowork
verifies B2 is intact at source first; then a separate push instruction advances the fork.

## §5 — Stop conditions
- `git rev-parse HEAD` is not `566d64d383…` before repair → STOP (unexpected state).
- After repair, any §1 file's working-tree SHA-256 differs from its backup → STOP (content changed — restore from
  backup and surface; the rebuild must not alter working-tree files).
- `git fsck` (if run) reports missing/corrupt **objects** (not just dangling) → STOP (bigger than an index rebuild;
  surface before any further action).
- Any urge to `git add`/commit/push to "clean things up" → do NOT; this instruction only repairs the index and
  verifies. Pushing is a separate, later step.
