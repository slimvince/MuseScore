# Iteration 55: Update baselines and refresh pipeline snapshot goldens

## Standing rule — no symbol inference

**No chord symbol string parsing. No Roman numeral inference. Structured fields only.**

Read `C:\s\MS\CLAUDE.md` and `C:\s\MS\build_and_test.md` first.

New confirmed baselines from Iter 54 (commit f92a4f1a3b):
  Baroque: BIR=true=14, BIR=false=132
  Jazz:    BIR=false=12
  Hard stops remain: Jazz BIR=false ≤ 75, any BIR=false regression > 10 from
  current Baroque baseline (132) requires investigation before committing.

Build fresh before every BIR measurement. Verify binary is newer than source.

---

## Background

Iter 54 committed the greedy-expand segmentation switch (f92a4f1a3b). Two
housekeeping tasks before any further algorithmic work:

1. Update `build_and_test.md` with the new baselines.
2. Refresh pipeline snapshot goldens — 9/12 were already stale before Iter 54
   (confirmed by CC via stash-and-rerun). The greedy output is now the
   authoritative production output; all goldens must reflect it.

Do NOT change any source code. Documentation, goldens, and one commit only.

---

## Step 1 — Confirm clean build from committed state

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
```

Regenerate Baroque corpus and confirm new baselines:
```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque \
    --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Expected: BIR=true=14, BIR=false=132. Stop if this does not match —
do not update baselines against a wrong measurement.

---

## Step 2 — Update build_and_test.md

Update the baseline section in `build_and_test.md`:

- Baroque BIR=true: 14 (was 21 after Iter 46)
- Baroque BIR=false: 132 (was 128 after Iter 46)
- Jazz BIR=false: 12 (was 20 after Iter 46)
- Note the commit that produced these baselines: f92a4f1a3b (Iter 54 —
  greedy-expand segmentation, batch path)
- Note that the bridge path (notationcomposingbridgehelpers.cpp) still uses
  Jaccard; bridge replacement is in progress (Task #62).
- Update the Jazz hard stop: BIR=false ≤ 75 (unchanged).
- Update the Baroque regression tolerance: investigate if BIR=false > 142
  (current 132 + 10).

---

## Step 3 — Run both test suites to confirm clean state

```
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
```

Expected: 407/407 and 53/53. Stop if either fails — do not update goldens
against a broken build.

---

## Step 4 — Inspect current pipeline snapshot failures

Before refreshing, read what the 9 failing tests actually test:

```
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe 2>&1 | head -80
```

For each failing test, note:
- Which score it covers
- What field changed (rootPitchClass, quality, measureNumber, beat, etc.)
- Whether the change looks like a genuine improvement (new boundaries from
  greedy producing better chord assignments) or a regression (a previously
  correct chord now wrong)

Report what you find before refreshing. If any failure looks like a genuine
regression (a previously correct chord now wrong), stop and report — do not
refresh those goldens.

---

## Step 5 — Refresh pipeline snapshot goldens

Only after Step 4 confirms no genuine regressions:

```
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

Expected after refresh: 12/12. If any test still fails after refresh, report
the failure in detail — do not commit.

---

## Step 6 — Commit

```
git add build_and_test.md
git add src/notation/internal/   # or wherever pipeline goldens live — check
git add tools/                   # if any goldens are under tools/
git commit -m "Iter 55: update baselines and refresh pipeline snapshot goldens

Post Iter 54 (greedy-expand batch segmentation, f92a4f1a3b).

New baselines:
  Baroque BIR=true:  21 → 14
  Baroque BIR=false: 128 → 132
  Jazz BIR=false:    20 → 12

Pipeline snapshot goldens refreshed: N/12 updated to reflect greedy-expand
output. Pre-existing stale goldens (9/12 failed before Iter 54) now resolved.
Bridge path still uses Jaccard (Task #62 in progress)."
```

---

## Step 7 — Report to Cowork

```
Step 1 — Baselines confirmed:
  BIR=true=N  BIR=false=N  (must be 14/132)

Step 3 — Tests:
  composing: N/407
  notation: N/53

Step 4 — Snapshot failures inspection:
  [For each of the 9 failing tests: score name, field changed, looks like
   improvement or regression]
  Any genuine regressions: [yes — stopped / no — proceeded]

Step 5 — Snapshot refresh:
  Tests passing after refresh: N/12
  Tests updated: N

Step 6 — Committed: [yes — hash] / [not committed — reason]
```
