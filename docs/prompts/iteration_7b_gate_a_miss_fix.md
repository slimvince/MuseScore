# Iteration 7B: Diagnose and fix the 2 MajorAdd6 Gate A misses

## ⚠ Critical behaviour rules

- **Diagnose first, implement only after reporting findings.**
- Make only the changes identified by the diagnosis. Nothing else.
- Do not commit until all tests pass. Then push.
- If the build fails or any test regresses, STOP and report verbatim.

---

## Background

The fresh corpus breakdown (Iteration 6b) found 2 genuine BIR=true enharmonic-pair
errors where the winner is Major+AddedSixth and the reference is a Minor chord at
`(winnerRootPc + 9) % 12`. Gate A should catch these categorically — it requires no
temporal context and fires whenever winner=MajorAdd6 and bestAlt=Minor at expectedAltRoot.
Their persistence means Gate A is not being reached, or its condition is not met.

---

## Step 1 — Context loading

1. `CLAUDE.md` — standing instructions
2. `build_and_test.md` — current baselines: BIR=true=111, BIR=false=788

---

## Step 2 — Identify the two failing cases

Write and run (do not save to repo) a Python script against the corpus JSONs in
`tools/corpus/`. Find the 2 genuine BIR=true errors where:
- winner quality = Major (with AddedSixth indicated in the chord symbol — e.g. "Bb6", "G6")
- `altRootPc == (winnerRootPc + 9) % 12`

For each, record: score filename, measure number, winner chordSymbol, winner rootPc,
alt rootPc, alt chordSymbol, score margin.

Report both cases before proceeding.

---

## Step 3 — Diagnostic runs

For each case, run `batch_analyze` with `--diagnose-measures`:

```
cd C:\s\MS\ninja_build_rel && ./batch_analyze.exe "<score_path>" --preset Baroque --diagnose-measures <measure_number>
```

From the diagnostic JSON output, report:

A. Is `winnerBassIsRoot` true? (winner.rootPc == winner.bassPc)
B. Does `inversionSuspicionMargin > 0.0` for the Baroque preset?
   (Read default from `chordanalyzer.h` if not visible in diagnostic output.)
C. Is `winnerHasAddedSixth` true in the diagnostic output?
   (Look for `hasAddedSixth: true` in the winner's extension_flags.)
D. Is a Minor candidate present in top_candidates at the expectedAltRoot
   `(winnerRootPc + 9) % 12`? If yes: what is its raw score vs the winner?
E. Is any Minor candidate present at ANY root in top_candidates?
   If yes but at a different root — the bestAlt search would find it first
   and `bestAlt->identity.rootPc != expectedAltRoot` would cause Gate A to fail.
F. Is a HalfDiminished candidate present at `(winnerRootPc + 9) % 12`?
   (If bestAlt finds a HalfDim first... it can't — kCleanQualities excludes it.
   But note if one is present at that root.)

Report A–F for both cases before proceeding.

---

## Step 4 — Implement fix

Based on the diagnosis, the most likely failure modes (in decreasing probability):

**FM1**: `winnerHasAddedSixth` is false even though the chord symbol shows "6".
The AddedSixth extension may not have been assigned by the template scorer.
If so: Gate A's condition is never met. Investigate whether the template scoring
assigns AddedSixth to this specific pitch-class combination.

**FM2**: The Minor alt at expectedAltRoot is present in results[] but is not the
first Major/Minor alt found — a different Major alt with a different root appears
first, so `bestAlt->identity.rootPc != expectedAltRoot` in Gate A.
Fix: add an explicit check for the expectedAltRoot minor alt in the Gate A
search, either by scanning ahead past the first bestAlt, or by adding a
dedicated pre-search for the MajorAdd6 case.

**FM3**: `winnerBassIsRoot` is false. The outer guard would still apply, but the
inner `if (winnerBassIsRoot && winnerQualityTargeted)` block is not entered.
Investigate whether the bass-as-root bonus applies here.

**FM4**: `inversionSuspicionMargin` is 0.0 for the Baroque preset (outer guard
fails). Report this as a configuration issue.

After identifying the failure mode, implement the minimal targeted fix. Report
the exact code change (old → new) before building.

---

## Step 5 — Build and test

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Expect:
- Composing tests: 407/407 pass, RealDiff ≤ 4
- Notation tests: 53/53 pass
- Pipeline snapshot tests: 10/10 pass (or golden mismatches if the fix touches a
  snapshot score — examine and verify before updating)
- BIR=true: ≤ 111 (expect 109 if both cases fixed)
- BIR=false: ≤ 788

If BIR=true does not improve: the fix is correct but the 2 cases require bridge-path
context to be fixed (similar to §2.10 limitation). Report this finding.

---

## Step 6 — Update STATUS.md and push

```
cd C:\s\MS && git add -A && git commit -m "Iter 7B: fix Gate A miss for MajorAdd6 <describe FM>" && git push
```

---

## Step 7 — Report

```
Failing cases identified:
  Case 1: <score> m<N> — <winner symbol> (should be <ref symbol>), margin=N
  Case 2: <score> m<N> — <winner symbol> (should be <ref symbol>), margin=N

Diagnostic findings (Case 1):
  winnerBassIsRoot:       yes / no
  inversionSuspicionMargin > 0: yes / no (value: N)
  winnerHasAddedSixth:    yes / no
  Minor alt at expectedAltRoot in top_candidates: yes (score=N) / no
  Minor alt at different root found first:        yes (rootPc=N) / no
  Failure mode:           FM1 / FM2 / FM3 / FM4 / other: <describe>

Diagnostic findings (Case 2): <same structure>

Fix implemented:           <describe change>
  File:line:               <location>
  Old code:                <paste>
  New code:                <paste>

Build:                     pass
Composing tests:           407/407 pass, RealDiff=N
Notation tests:            53/53 pass
Pipeline snapshots:        10/10 pass / N mismatches (verified correct)
Corpus run:
  BIR=true:                N (was 111)
  BIR=false:               N (≤ 788)

GitHub push:               done / commit hash
Unexpected findings:       none / <describe>
```
