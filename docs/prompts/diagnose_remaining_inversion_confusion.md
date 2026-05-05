# Diagnostic: Remaining Inversion Confusion After Threshold Fix

## Context loading — do this first

1. `CLAUDE.md` — standing instructions, build/test commands.
2. `STATUS.md` — top summary line and the `2026-05-04` entry only.

No other files needed for this task.

---

## What we know going in

After commit `31ea993f46` (threshold de-inflation + sus structural fourth threshold):

- Inversion confusion: **12.1% → 8.1%** of GT-paired cells. Improved but still substantial.
- Sus misread: **5.2% → 2.2%**. Largely solved.

The threshold fix ensures the correct chord now survives into `results[]` in more cases.
But CC observed that "the post-ranking correction still has room to miss cases that the
threshold fix now admits." The goal of this session is to find out *why* the correction
is still missing those cases, so the next fix can be targeted precisely.

The post-ranking inversion correction (chordanalyzer.cpp, lines ~1859–1938) can fail
to fire for three distinct reasons even when the correct chord is in `results[]`:

**Blocker A — Seventh exemption** (lines ~1916–1923): if the winner has a detected
minor or major seventh extension *and* the best clean alternative does not, the
correction is explicitly skipped. A passing tone at pcWeight ≥ 0.20 sets the seventh
extension bit; the correction then treats the seventh as a structural advantage and
refuses to penalise the winner.

**Blocker B — Margin too large**: the correction only fires when
`winner.score - bestAlt.score < inversionSuspicionMargin` (0.70). If the winner
genuinely beats the alternative by more than 0.70 even without the bass bonus, it wins
on merits and the flip is correctly suppressed. But if the bass-heavy weighting inflates
the gap beyond 0.70, the correction silently passes.

**Blocker C — No clean alternative in results**: even after the threshold fix, some
cases may still have no Major/Minor alternative with a different root in the top 3
(e.g. only augmented or diminished alternatives survived, or the results cap of 3 was
filled by other candidates before the correct chord). The correction has nothing to
flip to.

We need to know which blocker dominates the remaining 8.1%.

---

## Task

### Step 1 — Ensure post-fix corpus data is current

The analysis script reads enriched `.ours.json` files from `tools/reports/corpus/`.
Confirm that directory contains files produced by the post-fix binary (after commit
`31ea993f46`). If the files predate the commit, re-run the Bach chorales validation
pipeline to regenerate them before proceeding.

Check by looking at file modification times or by examining a known inversion case
(e.g. a region that was Bb6 pre-fix and should now be Gm7/Bb or Gm7).

### Step 2 — Run the existing diagnostic script

```
cd C:\s\MS
python tools/analyze_inversion_errors.py
```

This produces: chordScoreMargin distribution, alternative quality breakdown, noteCount
and beat distributions. Read the full output carefully.

**What to look for:**

- In the **margin distribution**: what fraction of remaining bassIsRoot errors have
  `margin < 0.70`? Those are cases where the correction *should* have fired but
  something blocked it (Blockers A or C). Cases with `margin ≥ 0.70` are Blocker B.

- In the **alternative quality breakdown**: what fraction have a clean Major/Minor
  alternative in results? Cases with no clean alternative are Blocker C.

### Step 3 — Extend the script to detect the seventh exemption

Add a section at the end of `analyze_inversion_errors.py` that counts Blocker A
specifically. For each error where `margin < inversionSuspicionMargin (0.70)` and a
clean alternative exists (i.e., the correction *should* have fired), check whether the
winner carries a seventh extension that the best clean alternative lacks.

The enriched `.ours.json` fields available on each region object include the winner's
symbol string and the `alternatives` list. Use these to detect the pattern:

- Winner symbol contains "7" or "maj7" or "m7" (has a seventh)
- Best clean alternative's symbol does not contain "7"

Count how many of the "should-have-fired" cases (margin < 0.70, clean alt present) fall
into this seventh-exemption pattern vs. how many have some other cause.

Add this output block:

```
── Blocker analysis (margin < 0.70, clean alt present) ──
  Total should-have-fired:          N
  Blocker A (seventh exemption):    N  (X%)
  Other / unclear:                  N  (X%)
```

### Step 4 — Report

Return:

```
Corpus data freshness: confirmed post-fix / regenerated (date)
analyze_inversion_errors.py output: [full output]
Blocker analysis:
  Margin >= 0.70 (Blocker B, correct suppression):   N  (X%)
  No clean alt in results (Blocker C):                N  (X%)
  Should-have-fired total:                            N
    of which seventh-exemption (Blocker A):           N  (X%)
    of which other:                                   N  (X%)
Conclusion: dominant remaining blocker is [A / B / C / mixed]
```

Do not make any code changes. Report only.
