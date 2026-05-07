# Iteration 4 Exploration: Characterise the 119 remaining genuine inversion errors

## ⚠ Critical behaviour rules for this session

- **This is a read-only investigation. Make zero code changes.**
  Your only job is to read, analyse, and report. Nothing else.
- **Do not propose or begin implementing anything.**
  If you see something that looks wrong or improvable, note it under
  "Unexpected findings" and stop there.
- **Do not commit anything.**
- Think carefully and report findings in full detail — the purpose is to give
  enough information to decide whether Iteration 4 empirical tuning will help,
  and if so, what to tune.

---

## Step 1 — Context loading

Read ALL of these before investigating:

1. `CLAUDE.md` — standing instructions
2. `build_and_test.md` — full read; understand the corpus check command
3. `STATUS.md` — top summary line and the 2026-05-05 entries only
4. `docs/prompts/iteration_plan_inversion_redesign.md` — Iteration 4 section in full
5. `docs/prompts/design_temporal_context_inversion.md` — if it exists; skip if not found

---

## Step 2 — Understand the corpus data format

Read `tools/analyze_inversion_errors.py` in full. Report:
- What corpus JSON files does it read, and where are they?
- What fields does it use from each region's data?
- What does a "genuine BIR=true error" look like in the JSON?
  (i.e. what field combination marks it as a genuine inversion error vs.
  a false positive or a genuine root-position chord)
- Does it already produce any per-error detail, or only counts?
- What `temporalExtensions` fields are available in the batch corpus JSON
  (e.g. `bassIsStepwiseFromPrevious`, `bassIsStepwiseToNext`,
  `previousRootPc`, etc.)?

Then read one representative corpus JSON file (e.g. a Bach chorale) to confirm
the actual field names and structure.

---

## Step 3 — Extract and classify the 119 genuine BIR=true errors

Write a short Python script (do not save it to the repo — run it inline or in
a temp file) that reads the corpus JSON files and for each genuine BIR=true
error region collects:

1. **Winner quality** — what chord did we output? (Major, Minor, etc.)
2. **Winner rootPc** — which root?
3. **Winner score** — the numerical score
4. **Best alternative rootPc** — what was the reference root?
5. **Best alternative score** — if available in the JSON
6. **Score margin** — winner.score − bestAlt.score (if available)
7. **Enharmonic pair** — is `altRootPc == (winnerRootPc + 9) % 12`?
   (This is the Bb6/Gm7 family — the only errors the current fast path targets)
8. **bassIsStepwiseFromPrevious** — from `temporalExtensions` in the JSON
9. **bassIsStepwiseToNext** — from `temporalExtensions` in the JSON
10. **previousRootPc** — from `temporalExtensions` — was the previous region
    already on the same root as the reference?

Then report a breakdown:

A. Of the 119 genuine BIR=true errors:
   - How many are enharmonic pairs (altRootPc == (winnerRootPc + 9) % 12)?
   - How many are NOT enharmonic pairs? (These cannot be fixed by the current
     fast path or gates B/C/D — they need a different approach)

B. Of the enharmonic-pair subset:
   - How many have `bassIsStepwiseFromPrevious = true`?
   - How many have `bassIsStepwiseToNext = true`?
   - How many have `previousRootPc` matching the reference (alt) root?
     (Would have fired Gate C if batch had `recentRootPcs`)
   - What is the score margin distribution? (min, max, median, and how many
     have margin < 0.3, 0.3–0.7, > 0.7)

C. Of the non-enharmonic-pair subset:
   - What quality does the winner have?
   - What quality does the reference expect?
   - Is there a pattern? (e.g. always a specific interval, always a specific
     quality type, always a specific corpus?)

---

## Step 4 — Assess stepwise bonus tuning (Iteration 4 Sub-test B)

The four existing scoring signals in `contextualBonuses()` are:
- `stepwiseBassInversionBonus` (default 0.50) — fired when `bassIsStepwiseFromPrevious`
- `stepwiseBassLookaheadBonus` (default 0.50) — fired when `bassIsStepwiseToNext`
- `sameRootInversionBonus` (default 0.40) — fired when `previousRootPc == altRootPc`
- `completeTriadInversionBonus` (default 0.45) — fired when alt has complete triad

Using your findings from Step 3, assess:

1. How many of the 119 errors have at least one of `bassIsStepwiseFromPrevious`
   or `bassIsStepwiseToNext` = true? (These could potentially benefit from
   raising stepwise bonuses)

2. For those stepwise errors: what is the typical score margin?
   Could a realistic bonus increase (staying strictly below 0.70 —
   `bassNoteRootBonus`) plausibly overcome the margin?

3. How many errors have margin > 0.70? (These cannot be fixed by any bonus
   increase — the ceiling is `bassNoteRootBonus = 0.70`)

4. Give an honest estimate: if stepwise bonuses were raised to 0.65 (the maximum
   safe value), how many of the 119 errors might be resolved?

---

## Step 5 — Assess preferMinorOverMajorAdd6 for Standard (Iteration 4 Sub-test A)

The AddedSixth guard (and Gates B/C/D) are gated by `preferMinorOverMajorAdd6`.
Currently Standard preset has this set to `true`.

Look at the non-Baroque corpus JSON files (if any — check what corpora are
available). Report:
- Are there cases where Standard preset produces C6 when Am7/C would be correct,
  or vice versa?
- Are there cases where the AddedSixth guard fires incorrectly on Standard-style
  chords (e.g. C6 in pop/rock where C6 is genuinely root-position)?
- If you cannot determine this from the existing corpus data, say so explicitly.

---

## Step 6 — Report

```
Corpus data format:
  JSON location:              <path>
  Fields available per region: <list relevant temporalExtensions fields>
  Genuine BIR=true marker:    <how it's identified>

Error breakdown (119 genuine BIR=true):
  Enharmonic pairs:           N / 119
  Non-enharmonic pairs:       N / 119

Enharmonic-pair subset (N errors):
  bassIsStepwiseFromPrevious=true: N
  bassIsStepwiseToNext=true:       N
  previousRootPc matches ref:      N
  Score margin distribution:
    < 0.3 (low — bonus could help):  N
    0.3–0.7 (medium):                N
    > 0.7 (ceiling — unfixable by bonus): N

Non-enharmonic-pair subset (N errors):
  Pattern / quality distribution:  <describe>
  Fixable by current approach:     yes / no / some

Stepwise bonus tuning assessment:
  Errors with stepwise signal:     N / 119
  Errors where bonus could help:   N (margin < 0.70)
  Errors where bonus cannot help:  N (margin ≥ 0.70 or no stepwise signal)
  Estimated improvement at 0.65:   N errors
  Recommendation:                  tune / skip / inconclusive

preferMinorOverMajorAdd6 Standard assessment:
  Evidence found:             yes / no / insufficient data
  Recommendation:             keep true / switch false / inconclusive

Overall assessment:
  Is Iteration 4 empirical tuning likely to produce meaningful improvement?
  <prose: honest assessment, including what category of remaining errors
  cannot be fixed by any of the current approach's mechanisms>

Unexpected findings: none / <describe>
```
