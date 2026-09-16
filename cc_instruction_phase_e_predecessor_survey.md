# CC Instruction: Phase E investigation — predecessor confidence survey for Δ=+7a rcb gate

## Pre-reading (mandatory)

Read `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only), and
`C:\s\MS\docs\redesign_plan.md` Step 4 (Phase D section, specifically the
"Revised Δ=+7a conclusion" and "Phase D fully closed" subsections).

**This is read-only.** No source code changes. No build. Goal: determine whether a
predecessor-confidence signal in `ChordTemporalContext` can gate `rootContinuityBonus`
to suppress the Δ=+7a rcb cascade without breaking the Mozart Alberti-bass control.

---

## Background

The oracle ALREADY scores AbMaj7 correctly (raw 2.55 > Eb 2.33) in the individual
present-root slice for bwv102.7 — without rcb. The sole blocker is `rootContinuityBonus`
(+0.40) fed from the preceding merged arpeggio region, which committed Eb on partial
evidence. The question is whether `previousWinnerScore`, `previousWinnerMargin`, or
`previousWinnerRootPcWeight` differ enough between the Δ=+7a predecessors and the
legitimate Alberti-bass predecessors in mozart_k280-1 to justify a gate.

**Why `ChordTemporalExtensions` is not sufficient:** `ChordTemporalExtensions`
(stored per-region in the dump) does NOT include `previousWinnerScore`,
`previousWinnerMargin`, `previousWinnerRootPcWeight`, or `previousDistinctPcs`
(see `harmonicrhythm.h`). These live in `ChordTemporalContext` only.

**Proxy approach:** the `previousWinnerScore` fed into region N is simply the winner
score of region N-1 (as computed by the oracle for N-1). That data IS available from
`--diagnose-measures` or `--dump-regions`. Look at the predecessor region directly.

---

## Task 1 — Confirm what `--diagnose-measures` exposes

For one score (bwv102.7), run:
```
/c/s/MS/ninja_build_rel/batch_analyze.exe "C:/s/MS/tools/corpus/bwv102.7.xml" \
  --preset Baroque --diagnose-measures 10 > /tmp/survey_diag.json 2>&1; echo "exit:$?"
cat /tmp/survey_diag.json
```

Check: does the output include any of these per-region fields?
- `winner_score` / `raw_score` / `candidates[0].score`
- `winner_margin` / `score_margin`
- `distinct_pcs`
- `temporal_context` block with `previousWinnerScore` etc.

Also try `--dump-regions batch` on the same score and check whether the region JSON
includes raw candidate scores or temporal context fields.

Report exactly what fields are available in each output mode. This determines the
extraction path for Tasks 2–4.

---

## Task 2 — Extract predecessor data for bwv102.7

### 2a. Identify the predecessor region

The failing present-root slice in bwv102.7 is around t17760 (the tick where Ab first
attacks). Run the batch dump to find the region immediately BEFORE it:

```
/c/s/MS/ninja_build_rel/batch_analyze.exe "C:/s/MS/tools/corpus/bwv102.7.xml" \
  --preset Baroque --dump-regions batch > /tmp/survey_bwv102_regions.json 2>&1; echo "exit:$?"
python3 -c "
import json, sys
data = json.load(open('/tmp/survey_bwv102_regions.json'))
regions = data if isinstance(data, list) else data.get('regions', [])
for r in regions:
    s = r.get('startTick', r.get('start_tick', 0))
    e = r.get('endTick', r.get('end_tick', 0))
    if 16800 <= s <= 18500:
        print(s, e, r.get('root', r.get('rootPc','-')), r.get('quality','-'), r)
"; echo "exit:$?"
```

(Adapt the Python parsing to the actual JSON structure — the field names above are
guesses. Check Task 1's output for exact names.)

For each region in the t16800–t18500 window, report:
- startTick, endTick, duration
- committed chord identity (root pc, quality)
- distinctPcs
- winner raw score and runner-up score / score margin (from the raw candidates list
  or however the dump exposes them)

The region immediately before the present-root slice is the predecessor whose
`chordResult` rcb will read as `previousRootPc`.

### 2b. Extract the predecessor's winner data

The predecessor region's winner score = `previousWinnerScore` going into the failing
slice. The predecessor's margin = `previousWinnerMargin`.

If the dump includes raw candidates: report `candidates[0].score` and
`candidates[0].score - candidates[1].score` for the predecessor.

If the dump does NOT include raw scores: use `--diagnose-measures` on the measure
containing the predecessor region instead. Check what measure that corresponds to.

---

## Task 3 — Extract predecessor data for bwv261

Same procedure as Task 2, but for bwv261. The failing region is around t33840–t34080.

```
/c/s/MS/ninja_build_rel/batch_analyze.exe "C:/s/MS/tools/corpus/bwv261.xml" \
  --preset Baroque --dump-regions batch > /tmp/survey_bwv261_regions.json 2>&1; echo "exit:$?"
```

Find regions in the t33000–t35000 window. Report same data as Task 2.

---

## Task 4 — Extract predecessor data for the control cases

### 4a. Mozart k280_1 — Alberti-bass control

The mozart_k280-1 test is the canonical Alberti-bass case that Iter-98 rcb gating broke.
The relevant region is around tick 7680 (the V65 at m9 or similar — check the pipeline
snapshot golden for the relevant tick). Run:

```
/c/s/MS/ninja_build_rel/batch_analyze.exe "C:/s/MS/tools/corpus/mozart_k280-1.xml" \
  --preset Baroque --dump-regions batch > /tmp/survey_mozart_regions.json 2>&1; echo "exit:$?"
```

Find 3–4 consecutive Alberti-pattern regions in the vicinity of the known sensitive tick
(check the pipeline snapshot golden at
`src/notation/tests/pipeline_snapshot_tests/snapshots/` for the tick range). For each,
report: startTick, endTick, duration, chord identity, distinctPcs, winner score, margin.

The key question: what do the Alberti-bass predecessors look like in terms of score and
margin vs. the Δ=+7a arpeggio predecessors?

### 4b. bwv320 — accepted residual (Δ=+7b/C2 case)

bwv320's rcb mis-fire at m27 (around t37440) is the other sensitive case. Run:

```
/c/s/MS/ninja_build_rel/batch_analyze.exe "C:/s/MS/tools/corpus/bwv320.xml" \
  --preset Baroque --dump-regions batch > /tmp/survey_bwv320_regions.json 2>&1; echo "exit:$?"
```

Find regions around t36960–t38400. Report the predecessor region to the wrong G/E winner
(the 2-PC sparse Gm slice at t36960). What is its winner score and margin?

---

## Task 5 — Survey all 13 Baroque BIR=false scores

For each of the 13 BIR=false scores (the standard set from `tools/characterise_bir_false.py`),
run a batch dump and identify ALL predecessor regions that feed rcb into a BIR=false
wrong winner. That is: find the region immediately before each BIR=false failing region,
and extract its winner score, margin, distinctPcs.

The goal: build a table of predecessor profiles across all 13 failures. This tells us
whether the Δ=+7a predecessors form a distinct low-score/low-margin cluster or are
spread across the same range as the non-Δ=+7a failures.

If the batch dump doesn't expose raw scores directly, an approximation is acceptable:
report whatever score-quality signal IS available (e.g., `winner_score_ratio` if raw
scores aren't exposed, or `previousWinnerRootPcWeight` if that's readable from the
dump).

---

## Report format

Write findings to `C:\s\MS\cc_phase_e_predecessor_survey_report.md`.

### Section 1 — Available dump fields
Exact field names available in `--dump-regions batch` and/or `--diagnose-measures`
that relate to winner score, margin, distinctPcs, raw candidates. If none are available,
state clearly and propose an alternative extraction method.

### Section 2 — Δ=+7a predecessor profiles

For each of bwv102.7 and bwv261:

| Region | startTick | endTick | duration | root (committed) | quality | distinctPcs | winnerScore | margin |
|--------|-----------|---------|----------|-----------------|---------|-------------|-------------|--------|
| Predecessor | ... | ... | ... | ... | ... | ... | ... | ... |
| Failing slice | ... | ... | ... | ... | ... | ... | ... | ... |

### Section 3 — Control predecessor profiles

Same table format for: mozart_k280-1 Alberti predecessors (3–4 rows) and bwv320
sparse-Gm predecessor.

### Section 4 — Full 13-case predecessor survey

Table: one row per BIR=false failing region, showing its predecessor's winnerScore,
margin, distinctPcs, and the current wrong-root committed by that predecessor. Group
by failure type (Δ=+7a, Δ=+7b, absent-root, segmentation, sus/quartal).

### Section 5 — Gap analysis

Given the data above:
1. Is there a threshold on `winnerScore`, `margin`, `distinctPcs`, or
   `winnerRootPcWeight` that separates all Δ=+7a predecessors from all Alberti/bwv320
   control predecessors?
2. If yes: propose the specific condition(s) and threshold(s).
3. If no clean gap: explain what overlaps and why.
4. Your overall assessment: is a predecessor-confidence rcb gate viable for Δ=+7a, or
   is this another dead end?

### Section 6 — Structural note
What does the predecessor region look like in the dump vs. what rcb actually reads?
Specifically: does the dump show the merged arpeggio run as a single region (with combined
tones), and does its committed winner reflect the stale first-sub-slice identity or the
aggregate? Confirm whether the predecessor region's committed identity in the dump matches
what `previousRootPc` in `ChordTemporalContext` would be at the failing slice.
