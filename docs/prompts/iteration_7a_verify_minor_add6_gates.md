# Iteration 7A: Verify Gates G-B/G-C/G-D fire in the bridge path

## ⚠ Critical behaviour rules

- **No changes to analysis logic.** The only permitted code change is adding
  a score to the pipeline snapshot test registry.
- Verify each golden change is a correct MinorAdd6→HalfDim7 flip before updating.
- Do not commit until all tests pass. Then push.
- If anything unexpected happens, STOP and report verbatim.

---

## Background

Gates G-B/G-C/G-D (added in Iteration 6) target 48 MinorAdd6 errors but require
`context != nullptr` — they do not fire in the batch corpus path. We have no direct
evidence they work correctly. This iteration adds a Bach chorale score containing
a genuine MinorAdd6 inversion to the pipeline snapshot test corpus, verifying that
the bridge path (which populates temporal context) correctly identifies it.

---

## Step 1 — Context loading

1. `CLAUDE.md` — standing instructions
2. `build_and_test.md` — current baselines
3. `docs/score_inventory.md` — understand which registry controls pipeline snapshot scores
   and the do-not-touch constraints

---

## Step 2 — Find candidate scores

The 48 MinorAdd6 enharmonic-pair errors are spread across 40+ distinct Bach chorales
in `tools/corpus/`. Write and run (do not save to repo) a short Python script that:

1. Reads all corpus JSONs and collects genuine BIR=true enharmonic-pair errors where
   winner quality = Minor+AddedSixth (e.g. chord symbol contains "m6" or "m69")
2. Groups them by score filename
3. For each group: records the score path and the error measure numbers
4. Prints the top 5 scores by error count (most errors = most likely to show
   gate firings in the bridge path)

Report the list. Then select ONE score for Step 3 — prefer a score where:
- Multiple MinorAdd6 errors appear in consecutive or nearby measures (suggests
  a sustained harmonic context where stepwise bass is likely)
- The score file exists under the Bach chorale corpus path (accessible to batch_analyze)

---

## Step 3 — Verify the score is loadable

Run `batch_analyze` on the selected score to confirm it parses correctly:

```
cd C:\s\MS\ninja_build_rel && ./batch_analyze.exe "<score_path>" --preset Baroque
```

If it fails to parse, try the next candidate from the Step 2 list.

---

## Step 4 — Add to pipeline snapshot corpus

Read `docs/score_inventory.md` to understand the correct registry file for adding
pipeline snapshot scores. Then add the selected score to that registry.

Rebuild to pick up the registry change:

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
```

Run the pipeline snapshot tests:

```
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

The new score will fail (no golden file yet). This is expected. Examine the output
for the new score and report:

A. What chord symbols does the bridge path produce for the error measures identified
   in Step 2?
B. For those measures: has the identification changed from the batch path output?
   (Batch says MinorAdd6, e.g. "Cm6"; does bridge say HalfDim7 in first inversion,
   e.g. "Am7b5/C"?)
C. Which Gate G variant (G-B, G-C, or G-D) appears to be firing, based on
   what temporal signal would be present (next-root match, stepwise+recent root,
   or consecutive stepwise)?

**If the identification HAS changed to HalfDim7 (gates fired):**
Verify the change is musicologically correct (the HalfDim7 reading is appropriate
for this passage in the context of the chorale). Then update goldens:

```
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens
```

Re-run to confirm pass.

**If the identification has NOT changed (gates did not fire):**
Do NOT update goldens. Try the next candidate score from the Step 2 list.
Repeat for up to 3 candidates. If none trigger a gate firing, report:
- What temporal conditions were present in the bridge path output
- The possible reason gates G-B/C/D are not firing (e.g. no stepwise bass signal,
  no recent root match, no consecutive stepwise count ≥ 2)
This is a valid finding — it may mean the 48 corpus errors occur in harmonic
contexts without strong stepwise evidence.

---

## Step 5 — Run all tests

```
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Expect:
- Composing: 407/407, RealDiff ≤ 4
- Notation: 53/53
- Pipeline snapshots: all pass (including new score with updated golden)
- BIR=true: same as post-7B baseline (no batch change expected)
- BIR=false: ≤ 788

---

## Step 6 — Update STATUS.md and push

```
cd C:\s\MS && git add -A && git commit -m "Iter 7A: add MinorAdd6 pipeline test — verify gates G-B/C/D" && git push
```

---

## Step 7 — Report

```
Candidate selection:
  Score chosen:                  <filename>
  MinorAdd6 error measures:      <list>
  Selection reason:              <why this score>

Gate firing result:
  Gates fired:                   yes / no / partial
  Identification change:         <describe: e.g. "m4: Cm6 → Am7b5/C">
  Gate variant (G-B/C/D):        <which one, based on evidence>
  Musicologically correct:       yes / no / uncertain: <describe>
  Scores tried before success:   N (list if > 1)

Pipeline snapshot tests:         N/N pass (after golden update if needed)
Corpus run:
  BIR=true:                      N (expect same as post-7B baseline)
  BIR=false:                     N (≤ 788)

GitHub push:                     done / commit hash
Unexpected findings:             none / <describe>
```
