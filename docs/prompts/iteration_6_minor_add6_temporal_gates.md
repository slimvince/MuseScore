# Iteration 6: MinorAdd6/HalfDim7 context-dependent gates (G-B, G-C, G-D)

## ⚠ Critical behaviour rules for this session

- **Think, investigate, and REPORT before implementing.**
  Read the relevant code, confirm it matches this document, then implement.
  If anything differs, STOP and report.
- **Make only the changes listed here. Nothing else.**
- **Do not touch `contextualBonuses()`.** No scoring changes there.
- **Do not add new `ChordAnalyzerPreferences` fields.** Gates are conditions, not preferences.
- **Do not commit until all verification steps pass.** Then push as instructed.
- If the build fails or any test regresses, STOP and report verbatim.

---

## Background

The MinorAdd6 ↔ HalfDim7 enharmonic pair (e.g. Cm6 = C–Eb–G–A and Am7b5 = A–C–Eb–G)
is the same second enharmonic equivalence pair attempted by the reverted Gate G.
Gate G was reverted because it was categorical — it fired on all MinorAdd6 winners
with a HalfDim alt present, producing a ~96% false-positive rate on the corpus.

The correct approach (demonstrated by the existing Gates B/C/D for the
MajorAdd6/Minor7 pair) is to require temporal evidence before preferring the
HalfDim reading. These gates fire only in the bridge path (context != nullptr)
and are not measurable via the batch corpus check — this is expected and noted
in ARCHITECTURE.md §2.10.

The three new gates (G-B, G-C, G-D) are exact parallels of Gates B, C, D,
extended to handle the MinorAdd6 winner + HalfDim alt case.

---

## Step 1 — Context loading (read ALL before touching any code)

1. `CLAUDE.md` — standing instructions
2. `build_and_test.md` — full read; authoritative build/test commands
3. `STATUS.md` — top summary line only

Then read this implementation section:

4. `src/composing/analysis/chord/chordanalyzer.cpp` — the full
   `if (prefs.preferMinorOverMajorAdd6)` block from its opening brace through
   its closing brace (currently contains Gate A and Gates B/C/D). Confirm:
   - The variables defined at the top of this block:
     `winnerIsMajor`, `winnerHasAddedSixth`, `altIsMinor`, `expectedAltRoot`
   - Gate D is the last gate before the block's closing brace
   - `expectedAltRoot = (winner.identity.rootPc + 9) % 12` — note that this
     formula is IDENTICAL to the HalfDim root formula for the MinorAdd6 case;
     no new variable is needed
   - `winnerHasAddedSixth` is already defined and can be reused
   - `winnerIsMajor` is defined; `winnerIsMinor = !winnerIsMajor` is safe here
     because `winnerQualityTargeted` guarantees the winner is Major or Minor

Report the exact line range of the `if (prefs.preferMinorOverMajorAdd6)` block
and confirm each item above.

---

## Step 2 — Verify current state

A. The `if (prefs.preferMinorOverMajorAdd6)` block contains exactly Gates A, B,
   C, and D. No G-B/G-C/G-D gates exist.
B. `kCleanQualities` = {Major, Minor} — HalfDiminished is excluded from the
   `bestAlt` search. The new gates must search results[] independently.
C. `expectedAltRoot` is already defined as `(winner.identity.rootPc + 9) % 12`
   inside this block — the same value used for the HalfDim root.
D. `winnerHasAddedSixth` is already defined inside this block.

Report A–D. If anything differs, STOP and report.

---

## Step 3 — Insert Gates G-B, G-C, G-D

### Location

Immediately before the closing `}` of the `if (prefs.preferMinorOverMajorAdd6)`
block (i.e., directly after Gate D's closing `}`). Do not move or modify
Gate A, B, C, or D.

### Code to insert

```cpp
                    // ── Gates G-B / G-C / G-D: Minor-add6 ↔ HalfDim7 (temporal context required)
                    // ─────────────────────────────────────────────────────────────────────────────
                    //
                    // Symmetric to Gates B/C/D but for the second enharmonic equivalence pair:
                    // Minor-add6 (e.g. Cm6 = C–Eb–G–A) shares all four pitch classes with the
                    // half-diminished seventh whose root is a minor-third above the winner root
                    // (= 9 semitones mod 12, the same formula as expectedAltRoot above).
                    //
                    // A categorical gate (like Gate A for MajorAdd6) was attempted and reverted
                    // because MinorAdd6 is a legitimate root-position chord in the corpus at a
                    // ~96% rate.  Temporal evidence is required before preferring HalfDim.
                    //
                    // kCleanQualities excludes HalfDiminished, so the alt is found by a separate
                    // one-pass search.  halfDimAltIdx is a sentinel (results.size()) if absent.
                    const bool winnerIsMinor = !winnerIsMajor;
                    if (winnerIsMinor && winnerHasAddedSixth) {
                        size_t halfDimAltIdx = results.size();
                        for (size_t i = 1; i < results.size(); ++i) {
                            if (results[i].identity.quality == ChordQuality::HalfDiminished
                                && results[i].identity.rootPc == expectedAltRoot) {
                                halfDimAltIdx = i;
                                break;
                            }
                        }
                        if (halfDimAltIdx != results.size()) {
                            // Gate G-B: next region's inferred root matches the HalfDim root.
                            // Strong forward evidence the harmony continues on that root.
                            if (!didEnharmonicFlip
                                && context != nullptr
                                && context->nextRootPc != -1
                                && context->nextRootPc == expectedAltRoot) {
                                std::swap(results[0], results[halfDimAltIdx]);
                                didEnharmonicFlip = true;
                            }
                            // Gate G-C: HalfDim root appears in the 3-region window AND bass
                            // is moving stepwise from the previous region.  The root was recently
                            // established and the bass is passing through a chord tone.
                            if (!didEnharmonicFlip
                                && context != nullptr
                                && context->bassIsStepwiseFromPrevious) {
                                const auto& rpc = context->recentRootPcs;
                                if (rpc[0] == expectedAltRoot
                                    || rpc[1] == expectedAltRoot
                                    || rpc[2] == expectedAltRoot) {
                                    std::swap(results[0], results[halfDimAltIdx]);
                                    didEnharmonicFlip = true;
                                }
                            }
                            // Gate G-D: two or more consecutive stepwise bass moves ending here.
                            // A scalar bass line is strong evidence of a passing inversion.
                            if (!didEnharmonicFlip
                                && context != nullptr
                                && context->consecutiveBassStepwiseCount >= 2) {
                                std::swap(results[0], results[halfDimAltIdx]);
                                didEnharmonicFlip = true;
                            }
                        }
                    }
```

Use the SAME indentation level as the surrounding Gates B/C/D code.
After inserting, report the exact line range of the inserted block.

---

## Step 4 — Build and test

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
```

### Composing tests

```
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
```

Read `src/composing/tests/chord_mismatch_report.txt`.
Expect: all pass, RealDiff ≤ 4 (baseline = 4). If any regression: STOP.

### Notation and pipeline snapshot tests

```
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

Gates G-B/C/D require `context != nullptr`. The 10-score pipeline corpus uses
the bridge path, which DOES populate temporal context.

**If pipeline_snapshot_tests.exe fails:**
1. Do NOT run `--update-goldens` yet.
2. Examine which scores changed and what the new identifications are.
3. For each change: verify it is a genuine MinorAdd6 → HalfDim7 flip with
   credible temporal evidence (stepwise bass or matching recent/next root).
4. Report ALL changes before refreshing goldens.
5. Only after confirming each change is correct:
   ```
   cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens
   ```
6. Re-run to confirm all pass.

If notation_tests or pipeline_snapshot_tests fails for any reason OTHER than
expected golden mismatches from the new gates: STOP and report verbatim.

### Corpus check (batch — gates G-B/C/D will NOT fire here)

```
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Preset: Baroque. The batch path does not populate temporal context, so gates
G-B/C/D will not fire. Expect:
- BIR=true: 111 (unchanged from baseline — no regression)
- BIR=false: ≤ 788 (must not increase)

A change here would mean something is firing unexpectedly in the batch path.
If BIR=false increases: STOP and report.

---

## Step 5 — Update STATUS.md and push

Add a 2026-05-05 entry documenting:
- Gates G-B/C/D added (MinorAdd6/HalfDim7, temporal context required)
- Corpus numbers unchanged (expected — §2.10 limitation)
- Pipeline snapshot confirmation (how many scores changed, if any)
- Commit hash

Then push:

```
cd C:\s\MS && git add -A && git commit -m "Iter 6: MinorAdd6/HalfDim7 context-dependent gates G-B/G-C/G-D" && git push
```

---

## Step 6 — Report

```
Context loading confirmed:         yes / issues: <list>
State verification (A–D):          all confirmed / differences: <list>

Gates G-B/G-C/G-D inserted:
  Insertion point (after line):    <line number of Gate D closing brace>
  Inserted block lines:            <line range>
  Code inserted:                   per iteration doc exactly / differences: <list>

Build:                             pass / fail
Composing tests:                   N/N pass, RealDiff=N
Notation tests:                    N/N pass
Pipeline snapshot tests (before):  N/N pass / N failures
  Changed scores:                  <list, or "none">
  Changes verified correct:        yes / no / partial: <describe>
Pipeline snapshot tests (after --update-goldens, if needed): N/N pass

Corpus run:
  Preset:                          Baroque (confirm)
  BIR=true:                        N (expect 111 — no batch change)
  BIR=false:                       N (must be ≤ 788)
  Gates G-B/C/D batch firings:     0 (expected — §2.10)

STATUS.md updated:                 yes
GitHub push:                       done / commit hash
Unexpected findings:               none / <describe>
```
