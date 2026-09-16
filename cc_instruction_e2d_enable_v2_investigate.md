# CC Investigation: E2d-enable v2 Failures — Root Cause Analysis

## Role and mandate

**Read-only investigation. No code changes, no commits, no golden updates.**

Goal: answer four specific questions precisely enough that Cowork can write an E2d-enable v3
instruction that will pass all 11 pipeline snapshot tests on the first attempt.

Save your findings to `C:\s\MS\cc_e2d_investigation_report.md` before exiting.

---

## Before starting

Read:
- `C:\s\MS\STATUS.md` — current HEAD, BIR baselines
- `C:\s\MS\build_and_test.md` — tool reference

Current HEAD is `37e8a711fc` (E3). The v2 attempt was reverted; all 11 tests pass at HEAD.

---

## Pre-analysis (Cowork has already confirmed these — do not repeat)

**Golden file format (Phase 3c):**
`tickRegional.alternatives` = `AnalyzedRegion.alternatives` = regionanalyzer post-gate
`results[1..N]`. Path is `analyzeNoteHarmonicContextRegionallyInWindow` →
`snapshot.context.chordResults.reserve(1 + it->alternatives.size()); push_back(it->chordResult);
for alt in it->alternatives: push_back(alt)`. No separate P3 analyzeChord call exists (Phase 3c
removed the "cruft display-context" path). The `tickRegional.root`/`quality` = winner
(`results[0]` after gates); `alternatives` = `results[1..N]` after gates.

**Gate A scope (lines 1943–1946):**
```cpp
const bool winnerQualityTargeted = (winner.identity.quality == ChordQuality::Major
                    || winner.identity.quality == ChordQuality::Minor);
if (winnerBassIsRoot && winnerQualityTargeted) { ...
```
Gate A targets **only Major and Minor** winners. Sus4 winners are explicitly excluded.
Gate A is **not** the cause of the GIGUE Sus→Major flip.

**Diff-root append (lines 3291–3312):**
Gated on `!prefs.suppressProgressionSignals` at line 3291. In suppression mode it **never
fires**. Conditions when it does fire (non-suppression mode):
- `results.front().identity.rootPc == static_cast<int>(bassPc)` — winner is root-position
- `prefs.inversionSuspicionMargin > 0.0`
- All entries in results[] share the winner's rootPc (hasDiffRoot = false)
- A rawCandidate with different rootPc clears the threshold

**Missing-alternative hypothesis (confirmed by golden data):**
For `mozart_k279_1` tick 1920: golden alternatives = `[D/minor, F/major]` (size 2). F/major
has rootPc=5 (F), winner has rootPc=2 (D) — different roots. F/major is the diff-root append
entry. In suppression mode the append does not fire → alternatives = `[D/minor]` (size 1).
This pattern (`winner` + same-root alt at index 0 + diff-root alt at index 1) repeats across
all 11+ diff-root-2-alt entries in mozart_k279_1. Same for mozart_k280_1 and chopin_bi105_op30_1.

**GIGUE tick 0 golden (confirmed):**
- `tickRegional`: winner=E/sus4, alternatives=[E/major(2.168), A/major(2.08), E/major(1.723)]
- `implode`: root=E, quality=sus4
- `annotation`: "Esus" / "Vsus4"

The A/major entry at alternatives[1] IS the diff-root append entry (rootPc=9 ≠ E rootPc=4).
Gate A is not the cause. Some other gate promotes E/sus4 over E/major(2.168) in
non-suppression mode.

**PRELUDE tick 7920 golden (confirmed):**
- `annotation`: "F#7/C#" / "V7/ii"
- `implode`: root=F#, quality=major

**CHORALE 137 tick 24000 golden (confirmed):**
- `tickRegional` tick 24000: winner=E/halfDiminished, alternatives=[G/minor, E/minor]
- `tickRegional` tick 24960: winner=D/minor

---

## Q1: Which gate promotes E/sus4 at GIGUE tick 0?

### What to find

In non-suppression mode, `analyzeChord()` returns `results[0]` = E/major (score 2.168) for the
GIGUE tick 0 region. After `applyHarmonicFunction()` (currently no-op) and then
`applyPostScoringGates()`, the winner becomes E/sus4. Some gate inside `applyPostScoringGates`
promotes E/sus4 from a lower position to `results[0]`.

### Steps

1. Grep for `Suspended4` and `sus4` and `SuspendedFour` in
   `src/composing/analysis/chord/chordanalyzer.cpp`, restricted to the `applyPostScoringGates`
   function (lines ~1885–2458). Find all gates that reference Sus4.

2. Read each such gate carefully:
   - What is its entry condition?
   - Does it require the winner (results[0] before the gate) to have a specific quality, or does
     it look anywhere in the candidate list?
   - Does it depend on the diff-root append entry being present in results[]?

3. For the gate(s) found: in E2d-enable mode, the function layer places E/major at results[0]
   (instead of the pre-gate E/major that would have been there anyway — same quality). Does this
   change the gate's entry condition? In other words: **does the Sus-promotion gate depend on
   anything that differs between suppression and non-suppression mode, other than the identity
   of results[0] after the function layer runs?**

4. In E2d-enable mode, `applyHarmonicFunction` rescores the cells from the ScoringSnapshot.
   E/sus4 is a Sus4 template. Check whether `wSeqBonus` applies to Sus4 candidates (it takes no
   quality parameter → it applies to all qualities). Check whether `wDimBonus` applies to Sus4
   (it does not — only Dim/HalfDim). So both E/major and E/sus4 would receive the same
   `wSeqBonus` from the function layer. If E/major's raw basisIndep score is higher than
   E/sus4's, the function layer would rank E/major above E/sus4. Is that consistent with the
   gate promoting E/sus4 in non-suppression mode from a position AFTER E/major?

### What to report

- Name of the gate(s) that promote Sus4
- Gate entry condition (what triggers it)
- Whether the gate could still fire when the function layer puts E/major at results[0]
- Your hypothesis for why E2d-enable v2 produced E/major instead of E/sus4 at this tick

---

## Q2: PRELUDE tick 7920 — what changed and why (V7/ii → VI43)?

### What to find

In non-suppression mode: implode=F#/major, annotation=F#7/C# (V7/ii in key A).
In E2d-enable v2: CC reported the output changed to VI43.

The diff-root append fires when `results.front().identity.rootPc == bassPc`. For F#7/C#, the
bass is C# (pc=1) and the root is F# (pc=6). These differ → the winner is NOT root-position →
**the diff-root append does not fire** for this chord even in non-suppression mode. Gate A also
requires `winnerBassIsRoot` → **Gate A does not fire** for F#7/C#.

So the diff-root append / Gate A mechanism is NOT the cause of this failure.

### Steps

1. Read the implode golden more carefully. Look at the region immediately **before** tick 7920
   in `src/notation/tests/pipeline_snapshot_tests/snapshots/bach_bwv806_prelude.json`
   (use the `implode` array — find items with tick < 7920, ordered by tick descending to get
   the predecessor). What is the predecessor region's root and quality?

2. In `applyPostScoringGates`, look for the gate that promotes an inverted (non-root-position)
   chord. For F#7/C# (root F#, bass C# = fifth of F# → second inversion), which gate handles
   inverted dominant seventh chords?

3. Read `applyHarmonicFunction`'s current body
   (`src/composing/analysis/function/harmonicfunctionlayer.cpp`). It is currently a no-op
   returning immediately if `snapshot == nullptr`. Confirm this.

4. In E2d-enable mode, `applyHarmonicFunction` receives the ScoringSnapshot from analyzeChord
   (run in suppression mode). It rescores all cells and selects the winner. For the PRELUDE tick
   7920 region, what cells would dominate after rescore? The pre-gate analyzeChord winner in
   suppression mode might already be different from F#/major (since suppression mode disables
   `wSeqBonus` and `wDimBonus`, which affect the relative ordering).

   To check what VI43 corresponds to: in key A, what chord quality and root would produce the
   Roman numeral label "VI43"? Look at `ChordSymbolFormatter::formatRomanNumeral` or check how
   the annotation formatter converts a chord identity to "VI43".

5. Check: **is the PRELUDE tick 7920 failure in the `implode` section, the `annotation` section,
   or both?** The implode records the regionanalyzer winner directly; the annotation records what
   `addHarmonicAnnotationsToSelection` writes. A change in the regionanalyzer winner would
   propagate to both.

### What to report

- Roman numeral "VI43" decoded: what root, quality, and inversion does it correspond to?
- Whether the failure is in `implode`, `annotation`, or both
- Why the function layer (or gate interaction) produces a different winner here
- Whether this failure is independent of the diff-root append issue

---

## Q3: CHORALE 137 tick 24000 — tick shift and chord change (Em7b5/Db → Dm)

### What to find

Golden: tick 24000 = E/halfDiminished, tick 24960 = D/minor.
E2d-enable v2 output: tick 24000 shows D/minor (and tick 24960 may have changed too).

Hypothesis: enabling `suppressProgressionSignals=true` in Pass 2/2b sub-region `analyzeChord`
calls (regionanalyzer.cpp ~lines 656, 877) changes sub-region winners for the regions around
tick 24000. If the sub-region at 24000–24960 changes from E/halfDim to D/minor (matching the
adjacent region at 24960), the two sub-regions merge → the region at 24000 disappears →
`tickRegional` sample at tick 24000 falls inside the D/minor region → reports D/minor.

### Steps

1. In `regionanalyzer.cpp`, read the Pass 2 loop (~lines 655–700) carefully:
   - Is `suppressProgressionSignals` set in the `prefs` object used for sub-region
     `analyzeChord` calls? (In E2d-enable, the instruction sets it at the Pass 1 call site;
     check whether the same `prefs` struct is reused for Pass 2 sub-region calls or a copy
     is made.)
   - Read the merge logic: after sub-region analysis, what condition causes two adjacent
     sub-regions to be merged (combined into one region)?

2. Similarly read Pass 2b (~lines 855–890).

3. For the specific CHORALE 137 region spanning tick 24000–24960: if `suppressProgressionSignals`
   is true in the sub-region analyzeChord call, what would change? The sub-region tones at
   24000–24960 contain (from the half-diminished reading) E-G-Bb-Db. Without progression signals,
   would this region score D/minor or E/halfDim higher?
   - Check `wSeqBonus` for this sub-region: is there a `nextRootPc` set in the sub-region
     context that creates a wSeqBonus advantage for one root over the other?
   - Check `rootContinuityBonus`: the previous root in the context is D (from the preceding
     region at 23040, which is A/major... wait, previousRootPc for the 24000 region — what is it?
     The golden shows `previousRootPc=2` (D) for tick 24000. With `rootContinuityBonus`, a D
     winner would get a bonus in suppression mode (since rootContinuityBonus is NOT a
     progression signal — it's gated by `previousRegionDistinctPcs >= 3`, not by
     `suppressProgressionSignals`). Check whether rootContinuityBonus is suppressed or not.

   **Key question**: is `rootContinuityBonus` suppressed by `suppressProgressionSignals`, or
   is it independent? Read `chordanalyzer.cpp` at the `rootContinuityBonus` lambda (around
   line 2900 or wherever `bassIndependentContextualBonuses` is called). If
   `rootContinuityBonus` is NOT suppressed (it fires even in suppression mode), then D/minor
   (root D, pc=2) would get a rootContinuityBonus when `previousRootPc=2`. This could make
   D/minor outscore E/halfDim in suppression mode for this sub-region.

4. Verify: does `suppressProgressionSignals` suppress only `wSeqBonus`/`wDimBonus`/wStepBonus,
   or also `rootContinuityBonus`? Read the suppression mode code path in `analyzeChord`.

### What to report

- Whether `suppressProgressionSignals=true` propagates to Pass 2/2b sub-region analyzeChord
  calls in E2d-enable
- Whether `rootContinuityBonus` is suppressed by `suppressProgressionSignals`
- Your assessment: is the tick shift caused by Pass 2/2b cascade (sub-region merge decision
  changed) or by the function layer applying to the outer region?
- Confidence level

---

## Q4: Missing-alternative cases — structural confirmation

### What to confirm

The diff-root append hypothesis is already confirmed by Cowork's analysis of the mozart_k279_1
data. Your job here is to:

1. For **each** of the four failing scores, identify the specific ticks where `alternatives`
   has size 2 with `alternatives[1].root != alternatives[0].root` (i.e., diff-root append
   entries). These are the ticks that will show "missing alternative" in E2d-enable mode.

   Run this Python snippet on the goldens:
   ```python
   import json
   base = 'C:/s/MS/src/notation/tests/pipeline_snapshot_tests/snapshots/'
   for score in ['mozart_k279_1','mozart_k280_1','chopin_bi105_op30_1','chopin_bi105_op30_2']:
       with open(base + score + '.json') as f:
           d = json.load(f)
       tr = d['tickRegional']
       diff_root = [(r['tick'], r['root']+'/'+r['quality'],
                     r['alternatives'][1]['root']+'/'+r['alternatives'][1]['quality'])
                    for r in tr
                    if len(r.get('alternatives',[])) == 2
                    and r['alternatives'][0]['root'] != r['alternatives'][1]['root']]
       print(f'{score}: {len(diff_root)} diff-root 2-alt entries')
       for tick, winner, alt1 in diff_root[:4]:
           print(f'  tick={tick} winner={winner} diff-root-alt={alt1}')
   ```

2. Confirm: **are all** "missing alternative" failures in E2d-enable accounted for by these
   diff-root append entries? Or are there additional ticks where the alternatives size changes
   for a different reason?

   The total count of diff-root 2-alt entries per score tells you the expected number of
   `alternatives`-differ failures per score (each such entry will lose its diff-root
   alternative in E2d suppression mode). Cross-check against CC's E2d-enable v2 report
   which listed 8 "alternatives differ" failures across all 11 tests.

3. For `chopin_bi105_op30_2`: Cowork found **zero** diff-root 2-alt entries in the golden.
   Verify this. If it was one of the failing tests in E2d-enable v2, the failure must have
   a different cause (candidates[0] change, not missing alternative). Check whether
   `chopin_bi105_op30_2` was among the 3 hard-stop candidates[0] changes or the 8
   alternatives-differ tests.

### What to report

- Per-score counts and sample ticks for diff-root 2-alt entries
- Whether the diff-root append explains all 8 "alternatives differ" tests or only a subset
- Clarification on `chopin_bi105_op30_2`

---

## Q5: rootContinuityBonus suppression check (standalone — affects Q3 and E2d-enable v3)

This is critical for E2d-enable v3 design. Read `chordanalyzer.cpp` in the
`analyzeChord` function at the `rootContinuityBonus` lambda / call site.

Determine: is `rootContinuityBonus` conditional on `!prefs.suppressProgressionSignals`,
or does it fire regardless of the suppression flag?

Also: in `harmonicfunctionlayer.cpp`, the E2d-enable v2 instruction wrote
`applyHarmonicFunction` to rescore using the ScoringSnapshot. It added `wSeqBonus`,
`wDimBonus`, and step bonuses. It used `basisIndep` from the snapshot **minus** the
rootContinuityBonus contribution. Read the v2 `applyHarmonicFunction` body as it was
written — check `C:\s\MS\cc_instruction_e2d_enable_v2.md` for the body, or if E2d has
been reverted, read the current (no-op) body and note it.

Determine: in E2d-enable v2, did `applyHarmonicFunction` correctly add `rootContinuityBonus`
back when rescoring? (The ScoringCell comment says basisIndep INCLUDES rootContinuityBonus
in non-suppression mode but NOT in suppression mode — because in suppression mode all signal
lambdas return 0. So in suppression mode, basisIndep is already WITHOUT rootContinuityBonus.
The function layer should ADD rootContinuityBonus when rescoring. Did v2 do that, or did it
mistakenly subtract it?)

### What to report

- Whether `rootContinuityBonus` is suppressed by `suppressProgressionSignals`
- The ScoringCell.basisIndep content in suppression mode vs non-suppression mode for a
  rootContinuityBonus-eligible region
- Whether E2d-enable v2's function layer correctly handled rootContinuityBonus

---

## Key code locations

```
chordanalyzer.cpp
  applyPostScoringGates():    ~line 1885 (function start)
  Gate A:                     ~lines 1943–2060
  rootContinuityBonus lambda: search "rootContinuityBonus" in analyzeChord body (~line 2880)
  Snapshot cell capture:      ~lines 3116–3156
  Diff-root append:           lines 3291–3312 (gate: !prefs.suppressProgressionSignals at 3291)
  Result-building loop:       lines 3262–3272

harmonicfunctionlayer.cpp (function layer body — currently no-op):
  applyHarmonicFunction():    find and read entire body

regionanalyzer.cpp
  Pass 1 analyzeChord call:   ~line 406 (or around there in the attempt region)
  Pass 2 loop:                ~lines 655–700
  Pass 2b loop:               ~lines 855–890

Golden files (read-only):
  src/notation/tests/pipeline_snapshot_tests/snapshots/*.json
```

---

## Output format

Save `C:\s\MS\cc_e2d_investigation_report.md` with:

```
# E2d-enable v2 — Root Cause Investigation Report

## Q1: Sus-promotion gate at GIGUE tick 0
[findings]

## Q2: PRELUDE tick 7920 — VI43 cause
[findings]

## Q3: CHORALE 137 tick shift mechanism
[findings]

## Q4: Missing-alternative structural confirmation
[per-score table]

## Q5: rootContinuityBonus suppression
[findings]

## Summary: root cause table

| Test | Tick | Expected | E2d actual | Root cause |
|------|------|----------|------------|------------|
| bach_bwv806_gigue | 0 | E/sus4 | E/major | [Q1 answer] |
| bach_bwv806_prelude | 7920 | F#7/C# | VI43-chord | [Q2 answer] |
| bach_chorale_137 | 24000 | E/halfDim | D/minor | [Q3 answer] |
| mozart_k279_1 | 1920 | D/minor+F/maj alt | D/minor only | diff-root append |
| mozart_k280_1 | ... | ... | ... | diff-root append |
| chopin_bi105_op30_1 | ... | ... | ... | diff-root append |
| chopin_bi105_op30_2 | ... | ... | ... | [Q4 answer] |

## Recommendation for E2d-enable v3
[what structural changes are needed beyond the diff-root append fix]
```
