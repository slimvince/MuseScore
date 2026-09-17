# CC Instruction: Δ=+7 Predecessor Confidence Diagnostic

## Pre-reading (mandatory every session)

Read `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only),
`C:\s\MS\build_and_test.md` before starting.

**This is a read-and-diagnose pass. No commits. Temporary debug prints are
permitted — add them, collect data, then remove them before reporting.**

---

## Background

Five Baroque BIR=false cases share a mechanism identical to the Iter 98 dead end:

> A sparse or uncertain predecessor region commits to rootPc=X. The next region's
> `rootContinuityBonus` (+0.40) rewards staying on X, tipping the wrong winner.

Target cases: **bwv102.7, bwv245.28, bwv261, bwv296, bwv320** (the Δ=+7 cluster).

Iter 98 tried to gate the bonus on `previousRegionDistinctPcs ≤ 2`. That failed
because `distinctPcs` is a lossy proxy — it cannot separate a genuinely wrong sparse
predecessor (bwv320) from a correct Alberti-bass predecessor (mozart_k280-1), where
any individual 16th-note slice is also sparse.

The redesign hypothesis is that **direct confidence measures** can make this
distinction where the proxy cannot:

- **Root pcWeight of the predecessor winner** (`snapshot.pcWeight[winner.rootPc]`):
  a wrong predecessor's root is often absent or near-zero; a correct Alberti-bass
  predecessor's root is present (it was just sounded on beat 1).
- **Winner margin of the predecessor** (winner score minus runner-up score): a
  wrong predecessor with only one viable template fires with no real competition; a
  correct Alberti-bass region typically has other live candidates.

**Falsifiability:** If the 5 Δ=+7 predecessors consistently show low pcWeight
AND/OR low margin, while mozart_k280-1's predecessor shows meaningfully higher
values on those same metrics, confidence scaling is a viable fix. If the numbers
overlap, it faces the same dead end as `distinctPcs`.

This diagnostic extracts the actual numbers to answer that question.

---

## Step 1 — Identify the predecessor region for each target case

For each of the 5 Δ=+7 scores, you need to find:
(a) The **failing region** — the one where BIR=false fires (our wrong root ≠ DCML root)
(b) The **predecessor region** — the region immediately before the failing one, whose
    `rootPc` became `previousRootPc` for the failing region

Read `C:\s\MS\docs\score_inventory.md` to get the paths for all 6 target scores:
bwv102.7, bwv245.28, bwv261, bwv296, bwv320, and mozart_k280_1.

Then dump the region list for each score:
```
cd C:\s\MS
ninja_build_rel/batch_analyze.exe <path> --dump-regions notation > /tmp/d7_bwv102.txt 2>&1; echo "exit:$?"
head -80 /tmp/d7_bwv102.txt
# repeat for each score, reading the output each time
```

From each dump, identify:
- The failing region tick range and its current rootPc (our wrong answer)
- The predecessor region tick range and its rootPc

The predecessor is the region whose rootPc matches our wrong winning rootPc in the
failing region (they should match because rootContinuityBonus requires
`candidateRootPc == previousRootPc`).

**bwv320 m27 — already characterised:** predecessor is the sparse Gm slice at
approximately tick 36960 (2-PC, distinctPcs=2, rootPc=7=G). Confirm from the dump.

Report the predecessor tick ranges for all 5 cases before adding any debug prints.

---

## Step 2 — Add a temporary debug print to extract confidence data

In `chordanalyzer.cpp`, find the `fn::applyHarmonicFunction(...)` call (approximately
L2947). Immediately after it returns, add a temporary debug print that fires for the
predecessor regions identified in Step 1.

The print needs these values:
1. `snapshot.distinctPcs`
2. `chosenResult.identity.rootPc` — the winner's root PC
3. `snapshot.pcWeight[chosenResult.identity.rootPc]` — the winner's root PC weight
   (0.0 = root entirely absent; >0 = some presence)
4. Winner score and runner-up score from `gateCtx`:
   - `gateCtxOut.rawCandidates[0].score` — winner's post-competition score
   - `gateCtxOut.rawCandidates.size() >= 2 ? gateCtxOut.rawCandidates[1].score : -1.0`
   - Margin = [0] - [1] (or "only candidate" if size < 2)

Check the exact variable names at the call site — `gateCtxOut` may be named
differently. `rawCandidates` is populated by `applyHarmonicFunction` into the
`PostScoringGateContext` struct before returning.

**Gating strategy:** Gate the print on the predecessor tick ranges found in Step 1.
The simplest form: a compound OR condition on `startTick`. Use the exact tick values
from the dump output. This avoids flooding and lets you run per-score without further
filtering.

Example (fill in actual ticks):
```cpp
// TEMPORARY DIAGNOSTIC — remove before commit
const bool isTargetPredecessor =
    (startTick == <bwv102_predecessor_tick>) ||
    (startTick == <bwv245_predecessor_tick>) ||
    // ... etc
if (isTargetPredecessor) {
    const double winnerPcWeight = snapshot.pcWeight[chosenResult.identity.rootPc];
    const double winnerScore    = gateCtxOut.rawCandidates.empty()
                                  ? 0.0 : gateCtxOut.rawCandidates[0].score;
    const double runnerScore    = gateCtxOut.rawCandidates.size() >= 2
                                  ? gateCtxOut.rawCandidates[1].score : -1.0;
    const double margin         = (runnerScore >= 0.0) ? (winnerScore - runnerScore) : -1.0;
    qDebug("[DIAG] tick=%d rootPc=%d pcWeight=%.4f winnerScore=%.4f runnerScore=%.4f "
           "margin=%.4f distinctPcs=%d",
           startTick, chosenResult.identity.rootPc, winnerPcWeight,
           winnerScore, runnerScore, margin, snapshot.distinctPcs);
}
```

If `startTick` is not in scope at that exact location, find the nearest available
tick variable (region startTick is typically threaded through the call chain). Inspect
the function signature and surrounding code to locate it.

---

## Step 3 — Build and run for each target score

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
```

Then run batch_analyze per score (redirect output, read separately):
```
cd C:\s\MS
ninja_build_rel/batch_analyze.exe <bwv102.7_path> > /tmp/conf_bwv102.txt 2>&1; echo "exit:$?"
grep "\[DIAG\]" /tmp/conf_bwv102.txt
# repeat for each target score + mozart_k280_1
```

If `startTick` is not accessible at the print site, fall back to adding the print
directly in `regionanalyzer.cpp` right before the `advanceTemporalContext` call
(L473), where tick context is certain to be available. Adjust the gating accordingly.

---

## Step 4 — mozart_k280-1 control

The Iter 98 kill case: mozart_k280_1, measures 9 and/or 12 — IV→V65 Alberti-bass.
The `rootContinuityBonus` fires correctly here: a legitimate IV region (rootPc = F)
sets `previousRootPc = F`, and the next V65 region correctly rewards staying on F
because the progression IS a sustained subdominant over a changing bass line.

Identify the predecessor region(s) for the m9/m12 IV events and extract the same
6 data points (rootPc, pcWeight, winnerScore, runnerScore, margin, distinctPcs).

Add the mozart predecessor tick(s) to the gate condition in Step 2.

If the mozart predecessor has pcWeight > 0 AND a reasonable margin, that would mean
confidence scaling can safely grant the bonus there while withholding it from the
Δ=+7 predecessors.

---

## Step 5 — Remove all debug prints

Before writing the report, remove the temporary debug print from `chordanalyzer.cpp`
(or `regionanalyzer.cpp` if that's where it landed). Confirm the working tree is
clean except for `cc_deltaseven_predecessor_report.md`.

**Do not commit any source changes.**

---

## Step 6 — Write the report

Write findings to `C:\s\MS\cc_deltaseven_predecessor_report.md`.

Include:

**Table 1 — Δ=+7 predecessor confidence data**

| Score | Predecessor tick | Predecessor rootPc | pcWeight[rootPc] | Winner score | Runner-up score | Margin | distinctPcs |
|---|---|---|---|---|---|---|---|
| bwv102.7 | | | | | | | |
| bwv245.28 | | | | | | | |
| bwv261 | | | | | | | |
| bwv296 | | | | | | | |
| bwv320 | | | | | | | |
| mozart_k280-1 (control) | | | | | | | |

**Table 2 — Failing region confirmation**

For each Δ=+7 case, confirm:
- Does the failing region's `previousRootPc` match the predecessor's `rootPc`? (Should be yes.)
- Does `snapshot.pcWeight[previousRootPc]` in the FAILING region equal the predecessor's
  `pcWeight[rootPc]`? (Should be yes — the predecessor's root is what gets rewarded.)

**Assessment — answer these questions:**

1. Do the 5 Δ=+7 predecessors share a pattern in pcWeight and/or margin that
   distinguishes them from the mozart_k280 control?

2. Which metric separates them more cleanly — root pcWeight, winner margin, or both?
   Is there a clear numeric threshold that would pass mozart and block all 5 Δ=+7 cases?

3. Is there any Δ=+7 predecessor whose numbers resemble the mozart control?
   (This would mean confidence scaling alone is insufficient for that case.)

4. What would the proposed scaling logic look like?
   - `previousWinnerRootPcWeight == 0.0` → bonus = 0 (root absent — definite lie)
   - `previousWinnerMargin < kThreshold` → reduced bonus (uncertain commitment)
   - Would this preserve the mozart_k280 bonus while blocking all 5 Δ=+7 cases?
   Suggest concrete threshold values based on the observed numbers.

5. Surface any structural mismatch you notice in the data that was not anticipated
   in the diagnostic design above.

---

## Notes on the diagnostic design

- `rawCandidates` in `gateCtx` contains candidates from the **winning bass group only**,
  sorted by score. The margin computed here is within-bass-group margin, not the global
  margin across all bass candidates. For sparse predecessor regions (1–2 PCs, single bass
  candidate), this is identical to the global margin. Note any cases where multiple bass
  groups were present.

- If `gateCtx.rawCandidates` is unexpectedly empty (which should not happen for a
  committed winner), fall back to extracting scores from `results[]` directly if
  `ChordAnalysisResult` carries the post-competition score.

- The `extensionThreshold` value (default 0.20 for Baroque) is the existing boundary
  between "present" and "extension/absent." A root pcWeight at exactly 0.0 means the
  root PC was never sounded; a value between 0.0 and extensionThreshold means it was
  faintly present but below the extension admission bar.
