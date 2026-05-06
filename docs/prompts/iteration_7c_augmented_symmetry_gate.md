# Iteration 7C: Gate H — augmented triad root-symmetry resolution

## ⚠ Critical behaviour rules

- **Think, investigate, and REPORT before implementing.**
  Read the relevant code, describe what you see, then implement.
- Make only the changes listed here. Nothing else.
- Do not commit until all tests pass. Then push.
- If the build fails or any test regresses, STOP and report verbatim.

---

## Background

The fresh corpus breakdown (Iteration 6b) identified 9 non-enharmonic BIR=true
errors at interval +8 where both the winner and the reference are Augmented triads
(example: D+(rootPc=2) → Augmented(rootPc=10)). These are NOT inversion errors —
they are root-symmetry ambiguities.

An augmented triad has three enharmonic roots exactly 4 semitones apart (mod 12).
D+ = {D, F#, Bb} — roots D(2), F#(6), Bb(10) are all equally valid. The analyzer
picks one root; the reference picks another. The interval between them is always
+4 or +8 mod 12.

The existing `winnerQualityTargeted` guard (Major or Minor only) prevents these
cases from entering the main correction block, so Gates A–G-D/E/F never see them.
Gate H is a separate, targeted correction for this class.

---

## Step 1 — Context loading

1. `CLAUDE.md` — standing instructions
2. `build_and_test.md` — baselines at start of this iteration (post-7B and 7A)
3. `ARCHITECTURE.md` — §4.1d (the post-ranking correction structure)

Then read:

4. `src/composing/analysis/chord/chordanalyzer.cpp` — the outer post-ranking
   correction block. Confirm:
   - Exact line of the outer guard: `if (prefs.inversionSuspicionMargin > 0.0 ...)`
   - Exact line of `if (winnerBassIsRoot && winnerQualityTargeted)`
   - The line immediately AFTER the closing `}` of
     `if (winnerBassIsRoot && winnerQualityTargeted)` — this is Gate H's
     insertion point (still inside the outer guard)
   - That `winnerBassIsRoot` is already declared before the targeted block

Report the line numbers before proceeding.

---

## Step 2 — Verify current state

A. No Gate H or augmented-symmetry gate exists anywhere in the file.
B. `winnerBassIsRoot` is declared before `if (winnerBassIsRoot && winnerQualityTargeted)`.
C. `ChordQuality::Augmented` is a valid enum value (confirm from existing uses in file).
D. `context` is in scope at the insertion point (it is a parameter to `analyzeChord`).

Report A–D. If anything differs, STOP and report.

---

## Step 3 — Insert Gate H

### Location

Immediately after the closing `}` of `if (winnerBassIsRoot && winnerQualityTargeted)`,
still inside the outer guard block. Gate H is a SEPARATE block — do not modify
the existing targeted block in any way.

### Reasoning

Augmented triads have three enharmonic roots. When the analyzer picks root R but
the reference picks root at (R+4)%12 or (R+8)%12, they describe the same sonority.
Temporal evidence (the same root recently appeared, or the next region implies it)
determines which spelling is contextually correct. Without evidence, keep the winner.

Gate H requires temporal context (`context != nullptr`) to avoid categorical
misfires on genuine augmented root-position chords — the same lesson learned from
the failed categorical Gate G.

### Code to insert

```cpp
        // ── Gate H: Augmented triad root-symmetry resolution ──────────────────────────
        //
        // An augmented triad has three enharmonic roots (±4 semitones mod 12): D+, F#+,
        // and Bb+ are the same chord.  When the analyzer picks root R but the correct
        // root is (R+4)%12 or (R+8)%12, the two candidates represent the same sonority
        // with different root labels.  Temporal evidence resolves the ambiguity.
        //
        // Unlike the main correction block, this gate handles Augmented winners
        // (excluded from winnerQualityTargeted = Major/Minor).  It fires only with
        // temporal context and is gated by preferMinorOverMajorAdd6 (classical presets).
        if (winnerBassIsRoot
            && winner.identity.quality == ChordQuality::Augmented
            && prefs.preferMinorOverMajorAdd6
            && context != nullptr) {
            bool didAugmentedFlip = false;
            for (const int semitones : {4, 8}) {
                if (didAugmentedFlip) break;
                const int altRoot = (winner.identity.rootPc + semitones) % 12;
                // Find an Augmented candidate at this root.
                size_t augAltIdx = results.size();
                for (size_t i = 1; i < results.size(); ++i) {
                    if (results[i].identity.quality == ChordQuality::Augmented
                        && results[i].identity.rootPc == altRoot) {
                        augAltIdx = i;
                        break;
                    }
                }
                if (augAltIdx == results.size()) continue;
                // Gate H-B: next region's inferred root matches the alt augmented root.
                if (!didAugmentedFlip
                    && context->nextRootPc != -1
                    && context->nextRootPc == altRoot) {
                    std::swap(results[0], results[augAltIdx]);
                    didAugmentedFlip = true;
                }
                // Gate H-C: alt root appears in the 3-region window AND bass is stepwise.
                if (!didAugmentedFlip && context->bassIsStepwiseFromPrevious) {
                    const auto& rpc = context->recentRootPcs;
                    if (rpc[0] == altRoot || rpc[1] == altRoot || rpc[2] == altRoot) {
                        std::swap(results[0], results[augAltIdx]);
                        didAugmentedFlip = true;
                    }
                }
                // Gate H-D: two or more consecutive stepwise bass moves.
                if (!didAugmentedFlip
                    && context->consecutiveBassStepwiseCount >= 2) {
                    std::swap(results[0], results[augAltIdx]);
                    didAugmentedFlip = true;
                }
            }
        }
```

Use the same indentation level as the surrounding outer guard code.
After inserting, report the exact line range of the inserted block.

---

## Step 4 — Build and test

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

Gate H requires `context != nullptr`, so it will NOT fire in the batch corpus.

**If pipeline_snapshot_tests.exe fails:**
1. Do NOT run `--update-goldens` yet.
2. Examine changed scores — identify if augmented triads are affected.
3. Verify each change is a genuine augmented root-symmetry correction.
4. Report before updating goldens.

Composing and notation tests must pass without regression.

### Corpus check

```
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Gate H does not fire in batch (context=null). Expect:
- BIR=true: same as current baseline
- BIR=false: ≤ 788

If BIR=false increases, Gate H is firing unexpectedly in batch. STOP and report.

---

## Step 5 — Update STATUS.md and push

```
cd C:\s\MS && git add -A && git commit -m "Iter 7C: Gate H — augmented triad root-symmetry resolution" && git push
```

---

## Step 6 — Report

```
Context loading confirmed:         yes / issues: <list>
State verification (A–D):          all confirmed / differences: <list>

Gate H inserted:
  Insertion point (after line):    <line of closing } of winnerBassIsRoot block>
  Inserted block lines:            <line range>
  Code inserted:                   per iteration doc exactly / differences: <list>

Build:                             pass / fail
Composing tests:                   N/N pass, RealDiff=N
Notation tests:                    N/N pass
Pipeline snapshot tests (before):  N/N pass / N failures
  Changed scores:                  <list, or "none">
  Changes verified correct:        yes / no / n/a
Pipeline snapshot tests (after --update-goldens, if needed): N/N pass

Corpus run:
  BIR=true:                        N (expect same as pre-7C baseline)
  BIR=false:                       N (must be ≤ 788)
  Gate H batch firings:            0 (expected — context=null in batch)

GitHub push:                       done / commit hash
Unexpected findings:               none / <describe>
```
