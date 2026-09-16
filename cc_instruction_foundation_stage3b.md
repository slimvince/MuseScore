# CC Instruction — Foundation Stage 3b: notation-failure disposition (TEST-ONLY; no inference fix)

> **Context & discipline.** Last foundation step. The 5 notation failures are triaged and the key regression
> (#1/#4/#5) is **fully diagnosed and recorded** (L3 spec §11 + the stabilization plan's new Phase **4c**). Its fix is
> **L3 key-quality work, scheduled for Phase 4c — it is NOT patched here.** Stage 3b does the **minimal, behavior-
> neutral disposition only**: mark the 3 diagnosed-regression tests as expected-fail, correct the 2 behavior-neutral
> Corelli tests, and commit. **No production/inference code changes in this stage.**

## §1 — #1/#4/#5: mark expected-fail with a tracking note (do NOT fix, do NOT refresh to F)
The three tests — `Notation_ImplodeTests.MozartK279OpeningPrefersCMajorOverFLydian`,
`NotationInteractionHarmonyPinning.BehaviorSnapshot_RomanNumeral`, `…BehaviorSnapshot_Nashville` — fail on the
**diagnosed C→F key regression**. Mark them **expected-fail** using a `GTEST_SKIP()` at the top of each (or the
project's xfail convention) with a message that keeps the cause visible, e.g.:
`GTEST_SKIP() << "xfail: C->F key regression from a6b08af3fe (leading-tone >0.1 presence-gate; B-nat weight 0.093). Diagnosis: cc_keyregression_diagnosis_report.md. Fix scheduled: stabilization plan Phase 4c (L3 emission de-brittling). Do NOT refresh goldens to F.";`
- **Do not** change the assertions' expected values, **do not** refresh `mozart_k279_1.json` (the F golden stays wrong-but-flagged, not blessed), **do not** touch the scorer.

## §2 — #2 Corelli `…DoNotSmearPreviousChord`: behavior-neutral test correction
The analysis is DCML-correct; the test is stale + has a matching bug. Two fixes (test file only):
- **Assertion:** m1's chord is **"G"** (DCML `V`) — update the stale `"Gm"` expectation to `"G"`.
- **Matching bug:** the `find("D")` for m10 is a **substring false-positive** on the new key-area label (e.g.
  `"Phryg·D·om"`). Make the check **token-aware** (match the chord token exactly, not a substring) so it tests the
  actual m10 chord. Confirm the **anti-smear property still holds** after the fix (that is what the test exists to
  guard).

## §3 — #3 Corelli `PopulateChordTrackEmitsCadenceMarkersOnCorelli`: confirm-then-refresh
The new marker (count 0→1) is plausibly a genuine cadence the higher key-confidence now lets through. **Confirm
first:** the emitted marker must land on an actual DCML cadence (candidates m8 / m13 / m21 / m30). 
- **If confirmed** on a real cadence → update the expected count to match (behavior-neutral; a correct new marker).
- **If it does NOT land on a DCML cadence → STOP and surface** — that would be a spurious cadence marker (a different,
  real bug), not a refresh.

## §4 — Verify
- `notation_tests`: **no unexpected failures** — the 2 corrected tests pass, the 3 xfail/skip show as skipped, zero
  remaining FAILED.
- `composing_tests` **624** and `pipeline_snapshot_tests` **11/11** unchanged. Production output unchanged (this is
  test-only — confirm `git diff` touches only test files + the two Cowork docs in §5).

## §5 — Commit (local-only)
- **Commit A (tests):** the §1–§3 test changes — `test(notation): dispose the 5 baseline notation failures — xfail the 3 diagnosed C->F key regressions (fix = plan Phase 4c), correct the 2 behavior-neutral Corelli tests`.
- **Commit B (docs):** there are **uncommitted Cowork doc edits** in the tree — `cowork_layer3_keymode_design.md`
  (§11 leading-tone-gate weakness) and `cowork_l1l3_stabilization_plan.md` (Phase 4c). Commit them:
  `docs(cowork): record the leading-tone presence-gate key regression (L3 §11) + schedule the de-brittling fix (plan Phase 4c)`. Confirm `git show --stat` for each lists only the expected files.
- Local only; `origin` held; `upstream` never.

## §6 — Stop conditions
- You start changing the **scorer / any production code** to fix the key regression → STOP (that is Phase 4c).
- You refresh `mozart_k279_1.json` or any golden to the **F** reading → STOP (never bless the regression).
- The #3 marker does not land on a real cadence → STOP and surface.
- The stash `bc4fa79c4a…` is touched → STOP. A push targets `upstream` → STOP.

## §7 — Deliverable
`cc_foundation_stage3b_report.md` (gitignored): the per-test changes; the #3 cadence-confirmation evidence; the two
commit hashes + `--stat`; and the final suite state (composing 624, snapshots 11/11, notation: N pass / 3 skipped /
0 failed). After this, the foundation is clean and we resume the stabilization plan at **Phase 2**.
