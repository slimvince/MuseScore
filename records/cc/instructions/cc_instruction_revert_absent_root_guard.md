# CC Instruction: Revert the absent-root guard

## Pre-reading (mandatory)

Read `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header), `C:\s\MS\build_and_test.md`
before starting.

---

## Decision

**Revert entirely (Option 1 from your AskUserQuestion).**

The absent-root guard introduced a net regression: 2 fixed (bwv301, bwv269), 4 broken
(bwv227.1, bwv342 are DCML-correct absent-root readings; 2 further cascade regressions
from `previousRootPc` propagating to downstream regions). The premise is falsified
corpus-wide — "absent root" does not reliably predict "wrong reading."

---

## Steps

### 1 — Revert source changes

Revert all modifications to `src/composing/` introduced by the absent-root guard
implementation. This means undoing any changes to `chordanalyzer.cpp`,
`harmonicfunctionlayer.h`, `harmonicfunctionlayer.cpp`, or any other file touched
during that implementation. Use `git diff` or `git stash` as appropriate; the working
tree should be identical to the state before the guard was added.

Do NOT revert any other changes unrelated to the guard.

### 2 — Restore snapshot goldens if needed

If the guard modified snapshot golden files (the regression report showed 6 goldens
changed), restore them to their pre-guard state. They should already be back to
baseline after reverting the source — confirm by running:

```
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe > /tmp/snap_revert.txt 2>&1; echo "exit:$?"
head -30 /tmp/snap_revert.txt
```

If goldens are still wrong, run `--update-goldens` only if the source revert is
complete and confirmed correct first.

### 3 — Build

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
```

### 4 — Run both test suites

```
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe > /tmp/comp_revert.txt 2>&1; echo "exit:$?"
head -30 /tmp/comp_revert.txt

cd C:\s\MS\ninja_build_rel && ./notation_tests.exe > /tmp/nota_revert.txt 2>&1; echo "exit:$?"
head -30 /tmp/nota_revert.txt
```

Read `src/composing/tests/chord_mismatch_report.txt` and confirm BIR numbers match
STATUS.md baselines (Baroque BIR=true=25, BIR=false=16; Jazz BIR=true=36, BIR=false=10).

### 5 — Report

Confirm:
- Composing tests pass, mismatch report matches STATUS.md baselines
- Notation tests pass (including pipeline snapshot tests)
- Working tree is clean (no uncommitted guard changes)

Do NOT commit anything. Report the before/after mismatch counts and confirm baseline
is restored.
