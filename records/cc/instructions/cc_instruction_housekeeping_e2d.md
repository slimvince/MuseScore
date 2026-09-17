# CC Instruction: Post-E2d Housekeeping

## Pre-reading

Read `C:\s\MS\STATUS.md` (header only) and `C:\s\MS\build_and_test.md` before starting.
Current HEAD: `2917ec7571`. Working tree has uncommitted CLAUDE.md changes.

No scoring logic is touched in this instruction. No build required.

---

## Task 1 — Commit the uncommitted CLAUDE.md changes

Show the diff, evaluate it, and commit.

```
cd C:\s\MS
git diff CLAUDE.md
```

Expected: ~40 lines of generic scoring-doc process rules added by CC during the E2d
redesign session. If the diff looks clean and consistent with the existing CLAUDE.md
style (no deletions of load-bearing rules, no new permissions granted, no content
that contradicts the standing instructions), commit it:

```
cd C:\s\MS
git add CLAUDE.md
git commit -m "docs: CLAUDE.md — scoring-doc process rules (CC additions from E2d session)"
```

If anything in the diff looks wrong or contradicts existing rules, **do not commit** —
report the problematic lines instead.

---

## Task 2 — Remove the equivalence harness

The harness (`equivalence_harness_test.cpp`) was written before the E2d redesign to
measure divergence between two pipelines (suppressed + function layer vs non-suppressed).
Post-redesign, both pipelines are the same path — `analyzeChord` calls
`applyHarmonicFunction` internally in all cases. The harness compares `analyzeChord`
output against itself and trivially reports 0 divergences forever. It is tautological.

**Steps:**

1. Delete the test file:
   ```
   cd C:\s\MS
   git rm src/composing/tests/equivalence_harness_test.cpp
   ```

2. Remove it from the CMakeLists.txt that governs composing_tests. Find the entry:
   ```
   grep -n "equivalence_harness" src/composing/tests/CMakeLists.txt
   ```
   Delete the line that references `equivalence_harness_test.cpp`.

3. Also delete the report file (it's generated output, not source):
   ```
   rm src/composing/tests/equivalence_harness_report.txt
   ```
   If it's tracked by git: `git rm src/composing/tests/equivalence_harness_report.txt`.

4. Commit:
   ```
   git add src/composing/tests/CMakeLists.txt
   git commit -m "test: remove equivalence harness (tautological post-E2d redesign)"
   ```

---

## Task 3 — Check for other uncommitted or stale files

Run:
```
cd C:\s\MS
git status
git stash list
```

Report:
- Any untracked files under `tools/` (especially `compare_rn.py` and related scripts
  listed as "Pending commit" in older COWORK_HANDOFF.md entries).
- Any other untracked or modified files that look like they should be committed.
- The stash list (any leftover stashes from previous sessions).

**Do not commit these without reporting them first.** Just list what you find and
flag any that look like they should be committed vs. gitignored vs. discarded.

---

## Task 4 — Verify test suite still passes (composing only)

After Tasks 1–2, run the composing suite to confirm the harness removal didn't
break anything:

```
cd C:\s\MS\ninja_build_rel
./composing_tests.exe > /tmp/comp_housekeeping.txt 2>&1; echo "exit:$?"
head -20 /tmp/comp_housekeeping.txt
tail -5 /tmp/comp_housekeeping.txt
```

Expected: 407/407 (one fewer than before — the removed harness test).
No notation or pipeline snapshot run needed (no source changes).

---

## Output

Report:
1. CLAUDE.md diff summary — what was in it, committed or not and why.
2. Equivalence harness removal — confirmed deleted and CMakeLists.txt updated.
3. `git status` / `git stash list` findings — what's left uncommitted.
4. Composing test result (407/407 expected).
5. New HEAD commit hash(es).
