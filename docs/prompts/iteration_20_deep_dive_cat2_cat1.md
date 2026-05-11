# Iteration 20: Deep-dive on Cat 2 Minor→HalfDim (24) and Cat 1 clean-alt (9) cases

## Goal

Two-part diagnostic. Zero logic changes to the analyzer.

**Part A** — extend the Iter 19 Python script to list all cases in the two
most actionable sub-groups explicitly (every file, measure, winner symbol,
alt symbol, key, margin).

**Part B** — add a minimal Gate G-E C++ diagnostic to determine WHY those 24
Cat 2 cases are not being fixed by the existing gate.

---

## Step 1 — Context loading

1. `CLAUDE.md` — standing instructions
2. `build_and_test.md` — baselines: BIR=true=98, BIR=false=788

---

## Part A — Enumerate all cases in the two target sub-groups

### Step A1 — Extend `tools/analyze_bir_true_iter19.py`

Add a section at the end of the script that, after the summary table, prints
two explicit case lists.

**List 1 — All Cat 2 Minor→HalfDim cases (expected ≈24)**

Print one line per case:
```
[CAT2-MHD] file=bwvXX.X  m=N  beat=X.X  winner=Am6  alt=F#m7b5/A  margin=+0.11  key=Dmaj
```

Selection condition: `category == 2` AND `winner_quality == "Minor"`
AND `alt_quality == "HalfDiminished"`.

Include the raw `winner_chordSymbol` (not just quality) so we can see whether
it is a plain minor triad or a minor-sixth chord (e.g. "Am" vs "Am6").

**List 2 — All Cat 1 clean-alt cases (expected ≈9)**

Print one line per case:
```
[CAT1-CLN] file=bwvXX.X  m=N  beat=X.X  winner=Em  alt=Cmaj  margin=+0.20  key=Cmaj
```

Selection condition: `category == 1` AND `alt_quality in {"Major", "Minor"}`.

### Step A2 — Run the extended script

```
cd C:\s\MS && python tools/analyze_bir_true_iter19.py
```

Capture the two new case-list sections verbatim.

---

## Part B — Gate G-E diagnostic for the Cat 2 Minor→HalfDim cases

### Step B1 — Inspect `chordanalyzer.cpp` Gate G-E region

Read the Gate G-E block (approx lines 2155–2205). Confirm the exact structure
of these conditions as they stand after Iter 18:

1. The outer `if` (`prefs.preferMinorOverMajorAdd6 && originalWinnerQuality ==
   Minor && originalWinnerHasAddedSixth`)
2. The `halfDimAltIdx` search loop (what quality does it search for? what
   field — rootPc or bassPc — does it store in `halfDimAltIdx`?)
3. The Gate G-E inner `if` (`!didGFlip && rootPc == gLeadingTonePc || ...
   gSupertonicPc || ... gMediantPc`)
4. The swap action

Report the exact code of each part (no paraphrasing).

### Step B2 — Add a minimal diagnostic block inside Gate G

Insert a diagnostic block IMMEDIATELY AFTER the outer `if` condition opens
(i.e., inside `if (prefs.preferMinorOverMajorAdd6 && ... && originalWinnerHasAddedSixth)`),
BEFORE the `halfDimAltIdx` search loop:

```cpp
// DIAG20-ENTRY: outer Gate G condition met — log for Iter 20
std::fprintf(stderr,
    "[DIAG20-ENTRY] root=%d bass=%d ktonic=%d didGFlip=%d nResults=%zu\n",
    winner.identity.rootPc, winner.identity.bassPc,
    keyTonicPc, (int)didGFlip, results.size());
```

Then insert a second block IMMEDIATELY AFTER the `halfDimAltIdx` search loop
completes:

```cpp
// DIAG20-HDX: report what halfDimAltIdx search found
if (halfDimAltIdx < results.size()) {
    std::fprintf(stderr,
        "[DIAG20-HDX] found hdIdx=%zu hdRoot=%d hdBass=%d gLT=%d gST=%d gMed=%d\n",
        halfDimAltIdx,
        results[halfDimAltIdx].identity.rootPc,
        results[halfDimAltIdx].identity.bassPc,
        (keyTonicPc + 11) % 12,
        (keyTonicPc + 2) % 12,
        (keyTonicPc + 4) % 12);
} else {
    std::fprintf(stderr, "[DIAG20-HDX] not-found nResults=%zu\n", results.size());
}
```

Then insert a third block IMMEDIATELY AFTER the Gate G-E inner `if` opens
(inside `if (!didGFlip && (... rootPc == gLeadingTonePc ...))`):

```cpp
// DIAG20-FIRE: Gate G-E condition met — swap imminent
std::fprintf(stderr, "[DIAG20-FIRE] swapping root=%d\n",
    results[halfDimAltIdx].identity.rootPc);
```

### Step B3 — Build and run

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus 2>tools/diag20_raw.txt
```

Verify build succeeds (warnings only). Confirm `diag20_raw.txt` is non-empty.

### Step B4 — Write `tools/analyze_diag20.py`

Write a Python script that:

1. Reads `tools/diag20_raw.txt`, filtering for `[DIAG20-*]` lines.
2. Reads the Cat 2 Minor→HalfDim case list produced by the extended Iter 19
   script (from Part A). You may hardcode the list of `(file, measure)` pairs
   from Step A2 output, or re-run Part A script and capture programmatically.
3. For each Cat 2 Minor→HalfDim case identified in Part A, searches
   `diag20_raw.txt` for a corresponding `[DIAG20-ENTRY]` line from that
   chorale (match on chorale stem). **Note:** the diagnostic fires for every
   Gate G evaluation in that chorale, not just the specific measure — report
   ALL Gate G evaluations from that chorale so we can see the pattern.

4. For each Cat 2 case, classify the failure mode observed in the diagnostic:

   | Code | Meaning |
   |------|---------|
   | NO-ENTRY | `[DIAG20-ENTRY]` never appeared for this chorale — outer condition never met (winner not MinorAdd6, or `prefs.preferMinorOverMajorAdd6=false`) |
   | NO-HDX | `[DIAG20-ENTRY]` appeared but `[DIAG20-HDX]` showed `not-found` — HalfDim not in candidates |
   | WRONG-PC | HDX showed `found` but hdRoot does not match gLT, gST, or gMed — pitch class mismatch |
   | ALREADY-FLIPPED | `didGFlip=1` in ENTRY line — gate skipped because G already fired |
   | FIRED | `[DIAG20-FIRE]` appeared — gate fired; but case is still a mismatch (verify this is unexpected) |
   | AMBIGUOUS | Multiple Gate G evaluations in chorale; case measure unclear |

5. Print a count of each failure mode across all 24 cases.
6. Print the full diagnostic output for each case (all matching lines from that
   chorale).

Run:
```
cd C:\s\MS && python tools/analyze_diag20.py
```

### Step B5 — Remove the diagnostic

Remove all three `DIAG20-*` blocks from `chordanalyzer.cpp`.

Build to verify clean:
```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
```

Run `grep -n "DIAG20" src/composing/analysis/chord/chordanalyzer.cpp` — must
return zero lines.

### Step B6 — Verify baselines unchanged

```
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Confirm BIR=true=98, BIR=false=788.

---

## Step 2 — Report to Cowork

Provide:

1. **Part A — Case lists** (full verbatim output of the two `[CAT2-MHD]` and
   `[CAT1-CLN]` sections from the extended Iter 19 script).

2. **Part B — Failure mode breakdown** (verbatim output of `analyze_diag20.py`,
   including the per-case diagnostic lines).

3. **Interpretation** (5–10 lines):
   - What is the dominant failure mode for Cat 2 Minor→HalfDim?
   - For Cat 1 clean cases: do the winner symbols show extensions (e.g. "m6",
     "aug") that explain the quality mismatch?
   - Based on findings: what is the root cause of the 24 Cat 2 cases not being
     fixed, and what is the minimal code change that would address the most cases?

Do NOT implement any fix. Do NOT commit. Report only.
