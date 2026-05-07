# Iteration 18b: Remove debug diagnostics and close Iteration 18

## ⚠ Critical behaviour rules

- Remove debug code only. Zero logic changes.
- Build + all tests must match Iteration 18 actuals exactly.
- If anything deviates: STOP and report verbatim.

---

## Background

Iteration 18 implemented three correct code changes (snapshot
`originalWinnerHasAddedSixth`, use it in Gate G outer condition, add
mediant/interval+4 to Gate G-E). During debugging, temporary `fprintf`
diagnostics were added to both `chordanalyzer.cpp` and `batch_analyze.cpp`.
Those must be removed before committing.

**Note:** Cowork also added a `[PRE-G]` diagnostic block to
`chordanalyzer.cpp`. That must be removed too.

---

## Step 1 — Context loading

1. `CLAUDE.md` — standing instructions
2. `build_and_test.md` — baselines: BIR=true=100, BIR=false=788

---

## Step 2 — Remove all debug fprintf calls

### 2a — chordanalyzer.cpp

Search for and remove every `std::fprintf(stderr, ...)` line that was added
as a diagnostic. The blocks to remove are:

1. **`[PRE-G]` block** — right before Gate G's outer
   `if (prefs.preferMinorOverMajorAdd6 ...)`. Remove the entire block:
   ```cpp
   // DIAG: show conditions for every Minor winner
   if (originalWinnerQuality == ChordQuality::Minor) {
       std::fprintf(stderr,
           "[PRE-G] root=%d bassPc=%d BIR=%d qualT=%d pref=%d addSix=%d\n",
           winner.identity.rootPc, winner.identity.bassPc,
           (int)winnerBassIsRoot, (int)winnerQualityTargeted,
           (int)prefs.preferMinorOverMajorAdd6,
           (int)originalWinnerHasAddedSixth);
   }
   ```

2. **`[GateG]` diagnostic block** — after the `halfDimAltIdx` search loop.
   Remove the entire block (the `{ std::fprintf ... for(...) ... }` block).

3. **`[GateG-E SWAP]` and `[GateG-E POST]` lines** — inside the
   `if (!didGFlip && ...)` block. Remove both `std::fprintf` calls.

4. **`[RETURN-HD ctx=...]` block** — near the `return results;` statement.
   Remove the entire diagnostic block including the `if (results[0]...)` guard.

After removals, verify: `grep -n "fprintf" chordanalyzer.cpp` returns zero
lines in the gate block region (lines 2140–2400).

### 2b — batch_analyze.cpp

Search for and remove every `std::fprintf(stderr, ...)` diagnostic added
during Iteration 18. The blocks to remove are:

1. **`[MAIN]` line** — immediately after the main `analyzeChord` call.
2. **`[MERGE-CHK]` line** — in the region merge logic.
3. **`[BA-STORE]` line** — before `ar.chord = candidates[0]`.

After removals, verify: `grep -n "MAIN\|MERGE-CHK\|BA-STORE\|GateG\|PRE-G\|RETURN-HD" batch_analyze.cpp` returns zero lines.

Report the exact lines removed for each file.

---

## Step 3 — Verify the three Iter 18 logic changes are intact

Read the following sections and confirm they are present and unchanged:

A. `originalWinnerHasAddedSixth` snapshot (lines ~1954–1955):
   ```cpp
   const bool originalWinnerHasAddedSixth =
       hasExtension(winner.identity.extensions, Extension::AddedSixth);
   ```

B. Gate G outer condition uses snapshot (lines ~2161–2163):
   ```cpp
   if (prefs.preferMinorOverMajorAdd6
       && originalWinnerQuality == ChordQuality::Minor
       && originalWinnerHasAddedSixth) {
   ```
   (NOT `hasExtension(winner.identity.extensions, Extension::AddedSixth)`)

C. Gate G-E mediant expansion (lines ~2193–2199):
   ```cpp
   const int gMediantPc = (keyTonicPc + 4) % 12;   // iiiø7 / mediant
   if (!didGFlip
       && (results[halfDimAltIdx].identity.rootPc == gLeadingTonePc
           || results[halfDimAltIdx].identity.rootPc == gSupertonicPc
           || results[halfDimAltIdx].identity.rootPc == gMediantPc)) {
   ```

Report confirmed or any discrepancy.

---

## Step 4 — Build and test

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Expected:
- Build: pass (warnings only — C4100 extThreshold and keySignatureFifths are pre-existing)
- Composing tests: 407/407
- Notation tests: 53/53
- Pipeline snapshot tests: 11/11
- BIR=true: 98
- BIR=false: 788

Any deviation: STOP and report verbatim.

---

## Step 5 — Update baselines and status

Update `build_and_test.md`:
- Replace BIR=true baseline: 100 → 98
- Update attribution line to Iteration 18

Update `STATUS.md` with a 2026-05-07 entry:
```
Iter 18: Gate G-E runtime fix + mediant expansion
- Snapshot originalWinnerHasAddedSixth to guard against re-sort reading
  wrong extensions before Gate G runs
- Gate G outer condition now uses snapshot instead of live winner reference
- Gate G-E expanded: added mediant (keyTonicPc+4) / iiiø7 condition
- Net improvement: BIR=true 100→98 (2 fixes)
- Note: expected 23 fixes; actual 2. Root cause: Iter 17 diagnostic measured
  intervals without temporal context. With context, most Am6 winners change
  before Gate G runs, or HalfDim drops below candidate threshold.
- New baselines: BIR=true=98, BIR=false=788
```

---

## Step 6 — Commit and push

```
cd C:\s\MS && git add -A && git commit -m "Iter 18: Gate G-E runtime fix (snapshot HasAddedSixth) + mediant expansion [2 BIR=true fixes, 98 remaining]" && git push
```

---

## Step 7 — Report

```
Debug code removed:
  chordanalyzer.cpp: lines N, N–N, N–N, N–N (PRE-G, GateG, SWAP/POST, RETURN-HD)
  batch_analyze.cpp: lines N, N, N (MAIN, MERGE-CHK, BA-STORE)

Logic changes verified:
  A. originalWinnerHasAddedSixth snapshot: line N ✓
  B. Gate G outer condition (snapshot):    line N ✓
  C. Gate G-E mediant expansion:           lines N–N ✓

Build:                    pass / fail
Composing tests:          407/407
Notation tests:           53/53
Pipeline snapshot tests:  11/11
BIR=true:                 98
BIR=false:                788

build_and_test.md updated: yes
STATUS.md updated:         yes
GitHub push:               done / commit hash
```
