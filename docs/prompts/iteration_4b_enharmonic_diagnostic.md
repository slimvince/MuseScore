# Iteration 4b: Diagnostic — why do enharmonic-pair errors resist correction?

## ⚠ Critical behaviour rules for this session

- **This is a read-only investigation plus diagnostic runs. Make zero code changes.**
- **Do not commit anything.**
- Think carefully and report findings in detail.
  The purpose is to answer one specific question:
  For the 73 genuine BIR=true enharmonic-pair errors, is the correct
  (enharmonic-pair) alternative present in `results[]`? If yes, why doesn't
  the post-ranking correction flip it?

---

## Step 1 — Context loading

1. `CLAUDE.md` — standing instructions
2. `build_and_test.md` — authoritative commands; note the `--diagnose-measures` flag
3. `STATUS.md` — top summary line only

---

## Step 2 — Identify 5–10 representative failing cases

Run `tools/analyze_inversion_errors.py` (Baroque preset, or read existing corpus
JSON) and find genuine BIR=true errors where:
- `altRootPc == (winnerRootPc + 9) % 12`  (enharmonic pair)
- The error is from the Bach chorale corpus (most numerous)

For each error you identify, record: score filename, measure number, winner chord
(rootPc, quality, chordSymbol), reference rootPc, bassIsStepwiseToNext.

Pick 5–10 representative cases spanning the margin range (some low-margin cases
like margin < 0.10, some medium-margin like 0.10–0.20). Report these before
proceeding to Step 3.

---

## Step 3 — Run diagnostic on each failing case

For each case identified in Step 2, run `batch_analyze` with `--diagnose-measures`:

```
cd C:\s\MS\ninja_build_rel && ./batch_analyze.exe "<score_path>" --preset Baroque --diagnose-measures <measure_number>
```

The diagnostic output (JSON) shows:
- `collected_notes` — the tones present in that region
- `top_candidates` — all candidates within 75% of the winner's raw score
  (WITHOUT context bonuses — the diagnostic runs without temporal context)
- `extension_flags` — whether hasAddedSixth is true for the winner
- `context_bonus` for each candidate — will be 0 in diagnostic mode (no context)

**Important caveat:** The diagnostic scores are RAW (no context bonuses applied).
The actual `results[]` in the live analysis DOES apply inversion bonuses before
ranking. So the diagnostic scores are a lower bound — the actual gaps may differ.

For each case, report:

A. **Is the enharmonic pair alt in `top_candidates`?**
   Look for a candidate with `root_pc == (winner_root_pc + 9) % 12`.
   If it's NOT present in top_candidates, it was filtered out of results[]
   and NO bonus or gate can help.

B. **If present: what is its raw score vs the winner's raw score?**
   Report both scores and the gap. Also note the winner's `bass_bonus` field
   (this is the +0.70 bassNoteRootBonus — it appears on the winner because
   the bass note = winner root).

C. **Is there another Major or Minor candidate ranked between the winner and
   the enharmonic pair alt?**
   If yes, `bestAlt` in the post-ranking correction would be THAT chord, not
   the enharmonic pair — meaning the enharmonic gate never engages.

D. **Is `hasAddedSixth` true for the winner?**
   (This is the prerequisite for the existing Gate A to fire.)

E. **Does the winner have `bass_bonus ≈ 0.70`?**
   (Confirms it's a bass-as-root case.)

---

## Step 4 — Analyse the post-ranking correction logic for these cases

For each case, given the diagnostic output, manually trace whether the
post-ranking correction COULD flip it:

1. Is the outer guard satisfied?
   `inversionSuspicionMargin > 0.0 && inversionBonusReduction < 1.0
    && results.size() >= 2 && distinctPcs >= 3`
   (Check: is there more than one candidate? Are there ≥ 3 distinct pitch classes?)

2. Is `winnerBassIsRoot` true? (winner rootPc == winner bassPc)

3. Is `winnerQualityTargeted`? (winner is Major or Minor)

4. Is `bestAlt` the enharmonic pair alt, or is it a different chord?

5. If `bestAlt` IS the enharmonic pair: what is the actual margin in the live
   analysis (with the 0.50 inversion bonuses applied)? Estimate:
   - Live winner score ≈ raw winner score (bass bonus already in diagnostic)
   - Live alt score ≈ raw alt score + inversion bonuses (if stepwise signals apply)
   - Does the margin fall below `inversionSuspicionMargin`?
   (Read `inversionSuspicionMargin` default from `chordanalyzer.h` and report it.)

---

## Step 5 — Report

For each of the 5–10 cases examined, fill in this table:

```
Case N: <score> m<measure> — <winner symbol> (should be <ref symbol>)
  Winner:           rootPc=N, quality=X, raw_score=N, bass_bonus=0.70
  Enharmonic alt:   rootPc=N (=(winner+9)%12)
    In top_candidates: yes (raw_score=N, gap=N) / NO (filtered out)
    Is bestAlt:     yes / no (something else is ranked above it: <what>)
  hasAddedSixth:    true / false
  bassIsStepwiseToNext: true / false (from corpus JSON)
  Estimated live margin: N (with inversion bonuses applied)
  Why correction fails: <one of:>
    - alt filtered out of results[] (gap too large)
    - bestAlt is a different chord (enharmonic gate never engages)
    - margin OK but hasAddedSixth=false so Gate A didn't fire (Gate B/C/D should)
    - margin too large even with bonuses (genuinely stuck)
```

Then answer the three diagnostic questions:

Q1. For what fraction of the 73 enharmonic-pair errors is the enharmonic alt
    filtered OUT of results[] entirely?

Q2. For the cases where the alt IS in results[], is the post-ranking correction
    engaging (is `bestAlt` the enharmonic pair), or is something else ranked above it?

Q3. What is the dominant failure mode — filtered out, wrong bestAlt, or margin
    too large?

```
Summary:
  Cases examined:                   N
  Alt filtered out of results[]:    N / N  (estimated for all 73: N / 73)
  Alt present but wrong bestAlt:    N / N
  Alt present, bestAlt correct, margin too large: N / N
  Alt present, bestAlt correct, Gate A should fire but doesn't (hasAddedSixth=false): N / N
  Dominant failure mode:            <describe>
  Implication for next fix:         <what would actually help>
  Unexpected findings:              none / <describe>
```
