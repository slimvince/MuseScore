# CC Instruction: E3 Cleanup + Step-Back Assessment + Two Investigations

## Pre-reading (mandatory)

Read `C:\s\MS\STATUS.md` (full — not just header) and `C:\s\MS\COWORK_HANDOFF.md`
(full document) before starting. Read `C:\s\MS\build_and_test.md` for commands.

Current HEAD: `a693b6ba82`. Baselines: Baroque BIR=true=25, BIR=false=16;
Jazz BIR=true=36, BIR=false=10. Tests: 407/407, 52/52, 11/11.

---

## Part 0 — Complete E3: commit Tasks 2+3, discard Task 1

You are mid-task. Before any investigation, resolve the current working state.

### Step 0a — Assess current state

```
cd C:\s\MS
git status
git log --oneline -5
git diff --stat
```

Determine precisely: which of the three E3 tasks are committed vs uncommitted?
- Task 1 — gate decoupling (winner captures moved before outer guard; Gates H/I/K/L/J
  relocated outside the outer guard)
- Task 2 — G-E phantom fix (`halfDimPulledFromRaw` + `results.pop_back()`)
- Task 3 — named constants (`kGateIMargin`, `kGateKMargin`, `kGateLMargin`)

Report the exact state before doing anything else.

### Step 0b — Commit Tasks 2+3, discard Task 1

**Task 2 and Task 3 are verified clean** — they did not cause the Schumann snapshot
regression and should be committed now. Task 1 is deferred pending a separate scope
decision.

If Tasks 2+3 are uncommitted (mixed with Task 1 changes in the working diff):
- Stage only the Task 2 lines (`halfDimPulledFromRaw` declaration + `results.pop_back()`
  cleanup block in `applyPostScoringGates`)
- Stage only the Task 3 lines (three `static constexpr double kGate*Margin` declarations
  and their three uses replacing `0.45f`, `0.20f`, `0.35f`)
- Do NOT stage any winner-capture movement or gate-relocation changes

If any Task 1 changes are uncommitted, discard them cleanly:
```
git checkout -- src/composing/analysis/chord/chordanalyzer.cpp
```
(after staging Tasks 2+3 but before committing, if needed — be careful about order)

Verify before committing:
```
cd C:\s\MS\ninja_build_rel
./composing_tests.exe > /tmp/comp_p0.txt 2>&1; echo "exit:$?"
tail -3 /tmp/comp_p0.txt
./pipeline_snapshot_tests.exe > /tmp/snap_p0.txt 2>&1; echo "exit:$?"
tail -3 /tmp/snap_p0.txt
```

Expected: 407/407, 11/11. Then commit:
```
cd C:\s\MS
git add src/composing/analysis/chord/chordanalyzer.cpp
git commit -m "fix: remove G-E phantom HalfDim when no sub-gate fires; float literals to named constants (E3 Tasks 2+3)"
```

Confirm working tree clean. Report new HEAD.

---

## Part 1 — Step-back architecture assessment

**Read-only. No code changes.**

Having read the full handoff and STATUS.md, answer the following questions honestly.
Pessimistic assessments are more useful than optimistic ones here.

### Q1 — Baroque BIR=false=16: is the wall real?

The 16 residuals are categorised:
- 5 rootContinuityBonus mis-fires (Iter 98 dead end — Phase E only)
- 5 evidence-absent (DCML root not in pcs — Phase D only)
- 3 sus/quartal/whole-tone structural placeholders (no fix)
- 2 segmentation (complex, low priority)
- 1 Sub-9b absent-root promotion (bwv14.5 — complex, investigation closed)

For each category: does anything in the characterisation look re-openable with current
tooling (no Phase D or Phase E infrastructure)? Be specific.

Pay particular attention to the 5 evidence-absent cases. "DCML root not in pcs" could
mean (a) genuine non-harmonic bass notes distorting the PC set (Phase D), or (b) a
region segmentation that is absorbing a short adjacent event and mixing its PCs into
the window, making the target root disappear (potentially fixable with a segmentation
change). Do any of those 5 look like (b) rather than (a)?

### Q2 — Jazz BIR=false=10: prior expectations

Before running the Jazz characterisation in Part 2, state your priors based on
what you know about the Jazz preset and the corpus:
- The Jazz preset uses `extensionThreshold=0.12` (lower than Baroque's 0.20) and
  `maxTotalInversionContextBonus=0.6` (vs Baroque's 2.5). What failure modes does
  this configuration make more or less likely?
- The Jazz corpus (bwv scores run with Jazz preset) is the same pitches as Baroque —
  the differences are all in scoring weights. What categories of error would you
  expect to be different between the two?

This will let us check whether Part 2's findings match prior expectations or surprise.

### Q3 — Minimum viable Phase E

Multiple high-value items are blocked on Phase E:
- B1 (MinorMajor7 template) — needs cadence confirmation to distinguish
  {tonic+leading-tone-of-V} from genuine i(maj7)
- A2 (dominant quality in minor) — needs cadence confirmation to distinguish
  genuine V from single-PC chord-tone arpeggiation
- Δ=+7 rootContinuityBonus mis-fires (5 Baroque residuals) — needs contextual
  suppression that doesn't regress Alberti-bass patterns (Iter 98 dead end)

What is the minimum concrete Phase E addition that would unblock the most of these?

Specifically:
- Would a simple "did the previous chord resolve stepwise to this root?" signal suffice
  for any of them, or do they all need full cadence detection (V→I progression)?
- What is the first concrete data structure or pass that would need to exist — a new
  field in `HarmonicFunctionContext`? A new post-function pass? A new cadence-evidence
  accumulator?
- Estimate: is this a 1-week CC task, a 1-month CC task, or longer?

Give an honest, grounded answer. The function layer shell (`applyHarmonicFunction`)
exists and is wired in — you are assessing what comes next, not whether the
infrastructure exists.

---

## Part 2 — Jazz BIR=false=10 characterisation

### Step 2a — Regenerate Jazz BIR

```
cd C:\s\MS
python tools/run_bach_preset.py --preset Jazz --output-dir tools/corpus
python tools/analyze_inversion_errors.py
```

Capture the 10 BIR=false cases. Confirm the count matches the baseline.

### Step 2b — Characterise each case

Use `tools/characterise_bir_false.py` if it supports a Jazz preset flag; check its
`--help` output first:
```
python tools/characterise_bir_false.py --help; echo "exit:$?"
```

If it supports Jazz, run it. If not, characterise each case individually using the
corpus JSON dumps in `tools/corpus/`. For each BIR=false case, run batch analysis:

```
cd C:\s\MS\ninja_build_rel
./batch_analyze.exe <score_path> --preset Jazz > /tmp/jazz_case_N.txt 2>&1; echo "exit:$?"
head -40 /tmp/jazz_case_N.txt
```

For each case, determine:
- Score name and region (tick range or measure)
- Analyzer output (chord, quality, root, bass)
- DCML expectation
- Likely mechanism — classify into one of:
  - **Template gap**: chord type has no matching template
  - **Quality error**: root correct, wrong quality (Min→Maj or similar)
  - **rootContinuityBonus mis-fire**: same Iter 98 pattern as Baroque Δ=+7
  - **Key detection error**: wrong key causes wrong analysis
  - **Evidence-absent**: DCML root not sounding
  - **Segmentation**: region boundary wrong
  - **Inversion error**: correct root, wrong bass/inversion
  - **Other**: describe

### Step 2c — Summarise

Produce a table:

| # | Score | Region | Analyzer | DCML | Mechanism | Actionable now? |
|---|---|---|---|---|---|---|

Flag any where the mechanism suggests a fix without Phase D/E.

Compare findings against your Part 1 Q2 priors — did the Jazz preset's lower
`extensionThreshold` and `maxTotalInversionContextBonus` explain the failures as
expected, or were there surprises?

---

## Part 3 — Min→Maj / Maj→Min quality confusion investigation

The cross-corpus rn_agree analysis (HEAD `f3e0f5f72c`, 61,233 matched regions)
identified 714 Min→Maj cases (we say Minor, DCML says Major) and ~465 Maj→Min
cases (we say Major, DCML says Minor). Root PC agrees in both sets. These are
uninvestigated.

### Step 3a — Locate existing report data

The corrected breakdown report is at:
`tools/reports/rn_corrected_breakdown_f3e0f5f72c.txt`

Read it:
```
cat tools/reports/rn_corrected_breakdown_f3e0f5f72c.txt; echo "exit:$?"
```

If the report lists individual cases (score, measure, our chord, DCML chord), proceed
to Step 3b directly. If it is a summary only, regenerate per-case output:
```
cd C:\s\MS
python tools/compare_rn.py --help; echo "exit:$?"
```
and use the appropriate flag to get case-level output for quality_disagree cases.

### Step 3b — Sample 20 Min→Maj cases

Select 20 cases spread across at least 4 corpora (not all from one score). For each:

1. What is the sounding chord (score, measure/tick, PCs present)?
2. Is the M3 (major third of the DCML root) present in pcWeight above
   `extensionThreshold`?
3. Is the m3 (minor third of the DCML root) present?
4. What is the bass note, and how does it relate to both roots?
5. Is the analyzer's Minor root the same as the DCML's Major root, or different?
   (i.e. is this a quality error on the same root, or a root-confusion case that
   slipped through the root_agree filter?)

You can inspect individual regions using batch_analyze with `--dump-regions` or
similar — check `batch_analyze --help` for the right flag.

### Step 3c — Sample 20 Maj→Min cases

Same procedure for the reverse direction.

### Step 3d — Mechanism summary

Based on the 40 samples, what is the dominant mechanism for each direction?

Candidates:
- **Third-presence issue**: m3 and M3 are both present (or both absent); scorer
  picks wrong quality
- **Bass-root bias**: bass note coincides with the minor root of a parallel triad,
  triggering wrong quality via inversion-correction logic
- **Key detection artefact**: wrong detected key maps the root to a minor-quality
  scale degree
- **Convention gap**: DCML labels extended or borrowed chords differently
  (e.g. DCML always calls a chord in a minor key "minor quality" on a major-third
  root even when the third is raised)
- **Inversion / slash confusion**: same sonority, different root assignment

Are Min→Maj and Maj→Min driven by the same mechanism or different ones?
Are any fixable with a targeted scoring or gate change?

---

## Output

Write all findings to `C:\s\MS\cc_stepback_report.md`.

Structure:
```
# Step-Back Assessment + Investigations

## Part 0 — E3 cleanup
Git state at start. Actions taken. New HEAD. Working tree state.

## Part 1 — Architecture assessment
### Q1 — Baroque residuals: any re-openable?
### Q2 — Jazz priors
### Q3 — Minimum viable Phase E

## Part 2 — Jazz BIR=false=10 characterisation
(table + mechanism analysis + comparison to priors)

## Part 3 — Min→Maj / Maj→Min investigation
(sample findings + dominant mechanism per direction + actionability)

## Summary
6–10 sentences: honest picture of where the project stands, what is genuinely
actionable now without Phase D/E, and what the highest-leverage next step is.
```

**No code changes beyond Part 0.** No commits beyond the E3 Tasks 2+3 commit.

---

## Acceptance criteria for Part 0

| Check | Required |
|---|---|
| composing_tests | 407/407 |
| pipeline_snapshot_tests | 11/11 (no goldens updated) |
| G-E phantom fix committed | Yes |
| Named constants committed | Yes |
| Gate decoupling changes | Discarded / not committed |
| Working tree after Part 0 | Clean |
