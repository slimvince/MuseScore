# Iteration 18: Gate G-E runtime fix + interval+4 expansion

## ⚠ Critical behaviour rules

- Two targeted changes. Read each section carefully before implementing.
- Do NOT run `--update-goldens` until every pipeline snapshot change is verified correct.
- Stop condition: BIR=false > 838 → STOP immediately before committing.
- If the build fails or any test regresses: STOP and report verbatim.

---

## Background — two issues, one iteration

### Issue 1: Runtime bug — Gate G silently fails after score re-sort

`const ChordAnalysisResult& winner = results[0]` is a live reference.
Iteration 16 snapshotted `originalWinnerQuality` to protect Gate G from reading
the post-swap quality. But Gate G's outer condition also reads
`hasExtension(winner.identity.extensions, Extension::AddedSixth)` — and this
was NOT snapshotted.

When a MinorAdd6 winner (e.g. Am6) has a close competitor and
`prefs.inversionSuspicionMargin` triggers the re-sort (lines ~2132–2142), Am6's
score is reduced and the competitor moves to `results[0]`. The competitor is a
plain Minor or Major chord without AddedSixth. Gate G then reads
`winner.identity.extensions` from the competitor — AddedSixth is absent — and
the outer condition fails silently. The Am6 → F#ø7 correction never fires.

Diagnostic confirmation: 15 interval=11/+2 cases remain unfixed (4 viiø7 + 11
iiø7). The JSON confirms HalfDim7 IS in results[] and preconditions are met.
The re-sort is the only code path that can change `winner.identity.extensions`
before Gate G runs.

**Fix**: snapshot `originalWinnerHasAddedSixth` alongside `originalWinnerQuality`
(already at line ~1952) and use it in Gate G's outer condition.

### Issue 2: 8 mediant-III cases not targeted

After fixing Issue 1, the remaining MinorAdd6 errors include 8 cases where
`(altRoot - keyTonicPc + 12) % 12 == 4` (the HalfDim7 is rooted on the mediant,
scale degree III). This is a recognisable Baroque function — e.g., Eø7 in C
minor, or F#ø7 in D minor — that Gate G-E should also catch.

**Fix**: add `altRoot == (keyTonicPc + 4) % 12` to the Gate G-E condition.

---

## Expected outcome

- Issues 1+2 together should fix 15 + 8 = 23 additional MinorAdd6 errors.
- BIR=true: 100 → ~77 (±2 depending on pipeline path coverage).
- BIR=false: 788 → ≤ 838 (stop threshold).

---

## Step 1 — Context loading

1. `CLAUDE.md` — standing instructions
2. `build_and_test.md` — baselines: BIR=true=100, BIR=false=788

---

## Step 2 — Read and confirm current state

Read `src/composing/analysis/chord/chordanalyzer.cpp` around lines 1949–1960
and 2157–2183. Confirm and report:

A. The exact lines of the `originalWinnerQuality` snapshot block (from Iter 16).
B. The exact line of Gate G's outer `if` condition — confirm it reads
   `originalWinnerQuality == ChordQuality::Minor`
   AND `hasExtension(winner.identity.extensions, Extension::AddedSixth)`.
C. The exact lines of Gate G-E's inner condition — confirm it checks
   `gLeadingTonePc` and `gSupertonicPc` only (no mediant yet).
D. Confirm `keyTonicPc` is still in scope at the Gate G block location (it is
   computed at line ~1664 and is function-scoped).

Report before proceeding.

---

## Step 3 — Snapshot `originalWinnerHasAddedSixth`

In the snapshot block (lines ~1949–1953, identified in Step 2A), add one line
immediately after `originalWinnerQuality`:

```cpp
        const bool originalWinnerHasAddedSixth =
            hasExtension(winner.identity.extensions, Extension::AddedSixth);
```

Also update the comment on the comment block above `winner` to mention extensions:

Change the existing comment from (approximately):
```cpp
        // Live reference — winner tracks results[0] through any swap.
        // Use originalWinnerQuality (captured below) when you need the
        // pre-swap quality in gates that run after A–F.
```
To:
```cpp
        // Live reference — winner tracks results[0] through any swap or re-sort.
        // Use originalWinnerQuality and originalWinnerHasAddedSixth (captured
        // below) when you need the pre-swap state in gates that run after A–F.
```

Report the exact lines changed.

---

## Step 4 — Update Gate G outer condition

In Gate G's outer `if` condition (identified in Step 2B), change:

```cpp
        if (prefs.preferMinorOverMajorAdd6
            && originalWinnerQuality == ChordQuality::Minor
            && hasExtension(winner.identity.extensions, Extension::AddedSixth)) {
```

To:

```cpp
        if (prefs.preferMinorOverMajorAdd6
            && originalWinnerQuality == ChordQuality::Minor
            && originalWinnerHasAddedSixth) {
```

Report the exact line changed.

---

## Step 5 — Add mediant (interval+4) to Gate G-E condition

In Gate G-E's inner condition (identified in Step 2C), add a third pitch class
check. Change from:

```cpp
                const int gLeadingTonePc  = (keyTonicPc + 11) % 12;
                const int gSupertonicPc   = (keyTonicPc + 2) % 12;
                if (!didGFlip
                    && (results[halfDimAltIdx].identity.rootPc == gLeadingTonePc
                        || results[halfDimAltIdx].identity.rootPc == gSupertonicPc)) {
```

To:

```cpp
                const int gLeadingTonePc  = (keyTonicPc + 11) % 12;  // viiø7
                const int gSupertonicPc   = (keyTonicPc + 2) % 12;   // iiø7
                const int gMediantPc      = (keyTonicPc + 4) % 12;   // iiiø7 / mediant
                if (!didGFlip
                    && (results[halfDimAltIdx].identity.rootPc == gLeadingTonePc
                        || results[halfDimAltIdx].identity.rootPc == gSupertonicPc
                        || results[halfDimAltIdx].identity.rootPc == gMediantPc)) {
```

Report the exact lines changed.

---

## Step 6 — Build

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
```

Build must pass with no errors. Report any warnings.

---

## Step 7 — Composing and notation tests

```
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
```

Expected: 407/407, 53/53. Any regression: STOP.

---

## Step 8 — Pipeline snapshot tests

```
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

Gate G-E fires on the bridge path (no temporal context required), so golden
mismatches are possible if any of the 11 snapshot scores contain qualifying
MinorAdd6 chords.

**If mismatches:**
1. Do NOT run `--update-goldens` yet.
2. For each changed score: verify the new symbol is musically correct
   (viiø7, iiø7, or iiiø7 in the current key).
3. Report all changes before updating.

**If no mismatches:** report and proceed.

---

## Step 9 — Update goldens if needed

```
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

---

## Step 10 — Corpus run

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Expected:
- BIR=true: ~77 (100 − 23; exact number may vary ±2)
- BIR=false: ≤ 838

**If BIR=false > 838: STOP immediately. Do not commit.**
Run the diagnostic from Iteration 9's pattern to identify which chords
were wrongly promoted by the new gate conditions.

**If BIR=true unchanged (still 100):** the `originalWinnerHasAddedSixth` fix
did not resolve the runtime bug. Report the exact BIR=true count and the first
5 MinorAdd6 errors still in the pool (score, measure, winner, alt, key).

---

## Step 11 — Update baselines and push

Update `build_and_test.md`:
- Replace BIR=true baseline with the new number
- Update the attribution line

Update `STATUS.md` with a 2026-05-07 entry:
- Gate G-E runtime fix: snapshot originalWinnerHasAddedSixth (re-sort was
  clearing extensions before Gate G ran)
- Gate G-E expanded: added mediant (interval+4) condition
- New BIR baselines

```
cd C:\s\MS && git add -A && git commit -m "Iter 18: Gate G-E runtime fix (snapshot HasAddedSixth) + mediant expansion" && git push
```

---

## Step 12 — Report

```
State (A–D confirmed):
  originalWinnerQuality block at:    lines N–N
  Gate G outer condition at:         line N
  Gate G-E inner condition at:       lines N–N
  keyTonicPc in scope:               yes (line N)

Changes:
  originalWinnerHasAddedSixth added: line N
  Comment updated:                   lines N–N
  Gate G outer condition:            line N (removed hasExtension live read)
  Gate G-E mediant added:            lines N–N

Build:                        pass / fail
Composing tests:              407/407, RealDiff=N
Notation tests:               53/53
Pipeline snapshot tests (before update):  N/N pass / N mismatches
  Changed scores:             <list or "none">
  Changes verified correct:   yes / n/a
Pipeline snapshot tests (after update):   N/N pass

Corpus:
  BIR=true:                   N (was 100 — additional MinorAdd6 fixed: N)
  BIR=false:                  N (was 788)

build_and_test.md updated:    yes
STATUS.md updated:            yes
GitHub push:                  done / commit hash
Unexpected findings:          none / <describe>
```
