# CC Instruction: Gate R — final verification and commit

## Pre-reading (mandatory)

Read `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header), `C:\s\MS\build_and_test.md`,
and `C:\s\MS\cc_gate_r_report.md`.

Repo state: Gate R code is in `harmonicfunctionlayer.cpp`, `scoring_model.md` is
updated. Neither is committed. Goldens are NOT refreshed. The guarded binary is built.

---

## Part A — Clarify bwv349 BIR count arithmetic (REQUIRED before committing)

The gate_r_report says:
- BIR=false went from **16 → 13** (−3)
- BIR=true went from **25 → 24** (−1)
- "Fixed 4" cases: bwv245.28, bwv296, bwv320, bwv349

The arithmetic does not close: 4 cases removed from BIR=false should give BIR=false
16→12 (−4), not −3. And if bwv349 was a fix, BIR=true should go up, not down.

Show the following **explicitly**:

1. For bwv349 tick 17280 (m13): the EXACT before-Gate-R chord identity (rootPc, quality,
   bassPc) and after-Gate-R chord identity. What does DCML expect there?

2. Run `tools/dump_bir_cases.py` (or whatever tool produces the BIR case enumeration)
   on the pre-Gate-R corpus AND the post-Gate-R corpus. Diff the output files and list
   every case that changed status:
   ```
   cases moved from BIR=false to BIR=true: ...
   cases moved from BIR=true to BIR=false: ...
   cases removed from BIR tracking entirely: ...
   ```

3. Explain precisely: what happened to bwv349's BIR=true count contribution? Is it a
   DIFFERENT bwv349 region than the one "fixed"? If any bwv349 region moved from
   BIR=true to BIR=false, that IS a regression — say so explicitly.

**Do not proceed to Part B until this arithmetic is resolved and clearly explained.**
If any case moved from BIR=true to BIR=false, report it as a regression and stop.

---

## Part B — DCML-verify two uncertain snapshot changes

From the gate_r_report §8:
- **bach_chorale_003**: winner changed from `Asus4` to `D major` (key E)
- **bach_chorale_137**: deeper P3/P4 alt changes

For each:

1. Find the DCML annotation for the affected chord region(s). Check:
   - `docs/score_inventory.md` for the file path
   - The DCML XML or annotation file if available
   - Alternatively, batch_analyze with `--dump-regions` and compare to known ground truth

2. Determine whether the new output (after Gate R) is CLOSER to or FURTHER FROM
   the DCML annotation. A change that moves AWAY from DCML is a regression.

3. For bach_chorale_003: what is the DCML-expected chord at the affected tick?
   Is `D major` or `Asus4` the correct reading?

4. For bach_chorale_137: what specifically changed? Which alts changed and do they
   reflect a closer or further reading from DCML?

Report the verdict for each: **Improvement**, **Neutral**, or **Regression**.

---

## Part C — Refresh goldens (only if Part A + Part B confirm no regressions)

If Part A confirms the BIR arithmetic is clean (no case moved BIR=true → BIR=false),
AND Part B confirms neither uncertain snapshot is a regression:

```
cd C:\s\MS\ninja_build_rel
./pipeline_snapshot_tests.exe --update-goldens; echo "exit:$?"
./pipeline_snapshot_tests.exe > /tmp/snap_final.txt 2>&1; echo "exit:$?"
head -20 /tmp/snap_final.txt
```

Confirm all 11 pipeline snapshot tests pass.

---

## Part D — Commit atomically

```
git add src/composing/analysis/function/harmonicfunctionlayer.cpp
git add docs/scoring_model.md
git add src/composing/tests/snapshots/  # (the refreshed golden files)
git commit -m "feat: Gate R — rcb bass-chord-tone guard (Baroque -3 BIR=false, Jazz -3 BIR=false)"
```

Then STATUS.md:
```
git add STATUS.md
git commit -m "docs: STATUS.md — Gate R commit, new BIR baselines (Baroque 24/13, Jazz 35/7)"
```

Do not push.

---

## Report to C:\s\MS\cc_gate_r_verify_report.md

1. bwv349 before/after chord identities + DCML expected
2. Full BIR case diff (moved, removed) with arithmetic closure proof
3. Verdict for bach_chorale_003 (Improvement / Neutral / Regression + evidence)
4. Verdict for bach_chorale_137 (Improvement / Neutral / Regression + evidence)
5. Final commit hash(es)
6. Whether all 11 pipeline snapshot tests pass after golden refresh
