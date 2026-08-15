# Phase D — Arpeggio Aggregation: Investigation, Attempt, and Revert

**Date:** 2026-06-09
**HEAD:** `90a52b5fee` (master). **Preset:** Baroque. **DIVISION = 480** (1 beat).
**Outcome:** Part A falsified the approved trigger design. The user-approved corrected
mechanism (re-analyze inline-merged aggregates) was implemented and measured — it
**does not fix either Δ=+7a target and regresses the corpus**, so it was **reverted**.
`regionanalyzer.cpp` is back at HEAD; working tree clean for that file.

---

## TL;DR

Two findings, both empirical:

1. **The approved trigger fires on nothing.** Runs of N ≥ 2 adjacent regions each
   `dur<480 AND distinctPcs≤2` match **0** cases in all 13 Baroque BIR=false scores
   (incl. both Δ=+7a targets) and **0** in a 25-score sample. The arpeggio slices are
   already fused by the inline same-root+quality merge **inside `runPass1`** (not in
   "Pass 2" as the instruction assumed), into ≥480-tick / ≥3-PC regions.

2. **Aggregation-first does not fix Δ=+7a.** The corrected mechanism — re-score each
   fused region on its complete aggregate tones with run-opening context — was built
   and run. On the *full* aggregate the DCML root becomes a candidate but **still
   loses vertically**: bwv102.7 `EbMaj7add13/Ab` (root Eb) 3.575 > `AbMaj9` (root Ab)
   3.425; bwv261 `C#m6/E` (root C#) 3.725 > `F#7/E` (root F#) 3.500. It also regressed
   3 notation tests (Corelli op01n08d ×2 + a sustained-support fixture) and drifted 8
   pipeline snapshots. **Δ=+7a is a Phase E (functional-context) problem, not a Phase
   D (tone-aggregation) one.**

The investigation report's prediction that "AbMaj7 wins on the aggregate" was correct
only for the cleaner slice-B 4-tone set `{C,Eb,G,Ab}`. The *complete* 6-PC aggregate
`{C,D,Eb,G,Ab,Bb}` adds D and Bb — EbMaj7's major-7th and 5th — which tip the vertical
contest back to Eb.

---

## Part A — Spot-check (read-only): the trigger fires on nothing

### Method
The merger inserts **after `runPass1`, before Pass 2**. No dump mode emits that exact
stream: `notation-premerge` is the *pre-inline-merge* per-boundary stream;
`--dump-regions batch` is *post-`absorbShortRegions`* (which deletes all <480t regions,
so a 353-file scan found 0 short regions trivially). I reconstructed the true Phase D
input = premerge stream **with the inline same-root+quality merge applied**
(`regionanalyzer.cpp` lines 506-518), verified against batch-final (e.g. bwv102.7
reconstructs the same 720t `EbMaj7/Ab` region). `distinctPcs` = distinct `pitch%12`
over the merged `tones`.

### Result — 0 qualifying runs in all 13 BIR=false scores

| # | score | tick | symbol | Δ | merged span | dur | dpcs | qualifies? |
|---|-------|------|--------|---|-------------|-----|------|------------|
| 1 | bwv102.7  | 17520 | EbMaj7/Ab | +7a | 17520–18240 | 720  | **6** | no |
| 2 | bwv14.5   | 8160  | Gm/Bb     | +9  | 8160–8640   | 480  | **4** | no |
| 3 | bwv17.7   | 46080 | A/Eb      | +6  | 46080–46560 | 480  | **3** | no |
| 4 | bwv174.5  | 6240  | E/G#      | +8  | 6240–6720   | 480  | **3** | no |
| 5 | bwv245.17 | 4800  | F/D       | +3  | 4800–5280   | 480  | **5** | no |
| 6 | bwv245.40 | 51360 | F7sus/Bb  | +2  | 51360–51840 | 480  | **3** | no |
| 7 | bwv261    | 33840 | C#m/E     | +7a | 33840–34560 | 720  | **4** | no |
| 8 | bwv269    | 20640 | D/F#      | +8  | 20640–22080 | 1440 | **6** | no |
| 9 | bwv301    | 960   | G/A→G/B   | +8  | 960–1920    | 960  | **5** | no |
| 10| bwv381    | 4800  | G6/F#→G6/D| +3  | 4800–5280   | 480  | **5** | no |
| 11| bwv422    | 23040 | A7sus/D   | +2  | 23040–23520 | 480  | **3** | no |
| 12| bwv432    | 5520  | Am/E      | +5  | 5520–6240   | 720  | **7** | no |
| 13| bwv45.7   | 20160 | F#7/E     | +8  | 20160–20640 | 480  | **3** | no |

25-score random sample: **0** runs. Whole-corpus batch-final: **0** (post-absorb).

### Premise error
The instruction states the same-root+quality merge happens in "Pass 2" after Pass 1.
It actually happens **inside `runPass1`** (lines 510-518), so by the Phase D insertion
point the arpeggio is already one ≥480t region with the full aggregate tones but the
**first sub-slice's stale identity** (the merge unions tones + updates bass only; the
oracle is never re-run). bwv102.7 idx53 (240t/4PC EbMaj7) + idx54 (480t/4PC Eb6/Ab),
both root-Eb Major → fused to one 720t/6-PC `EbMaj7/Ab`. bwv261's only `dpcs≤2` region
(idx87, isolated) fuses with idx88 → 720t `C#m/E`.

---

## Part B — Corrected mechanism: built and measured (then reverted)

User approved re-analyzing the inline-merged aggregates rather than merging short
sparse runs. Implemented as a static `reanalyzeMergedAggregateRegions(...)` in
`regionanalyzer.cpp`, called after `runPass1`+fallback and before Pass 2 (gated off
for PreserveAllChanges). A region is a fused aggregate iff a greedy-expand boundary
tick falls strictly inside `[startTick,endTick)`. For each, it reconstructs the
**run-opening** temporal context from `region.temporalExtensions` (predecessor = the
region before the run, so `rcb` rewards neither intra-run root), recomputes
`nextRootPc` from the post-run successor's tones, re-runs
`analyzeChord`+`applyIter8691Pedal`+`applyPostScoringGates`+sparse refinements on the
aggregate tones, and replaces `chordResult`/`alternatives`.

Build clean. Insertion verified to fire (symbols changed). **But the result falsifies
the approach.**

---

## Part C — Test results (the change regressed the corpus)

- **composing: 416/416** (unaffected — unit chord tests don't exercise the region pass).
- **notation: 49/52 — 3 FAILED (regressions):**
  - `Notation_ImplodeTests.NoteContextMatchesRegionalChordOnSustainedSupportFixture`
  - `Notation_ImplodeTests.CorelliOp01n08dOpeningNoteContextMatchesPopulateInCMinor`
  - `Notation_ImplodeTests.PopulateChordTrackPreservesCorelliOp01n08dCarryInAndLateDominant`
- **pipeline snapshots: 8 drifts** — bach_chorale_001, bach_chorale_003, mozart_k279_1,
  mozart_k280_1, chopin_bi105_op30_1, chopin_bi105_op30_2, corelli_op01n08a,
  schumann_kinderszenen_n01. (e.g. chorale_001 t1920 `G/D`→`GMaj7/D`, `I64`→`I43`.)

Re-analyzing **every** multi-slice aggregate is far too broad: most aggregates are
genuine sustained chords, and re-scoring their full (passing-tone-laden) span shifts
quality/inversion across the corpus. Goldens were **not** updated (regressions).

---

## Part D — BIR

Not separately measured: the notation-test regressions are an unconditional stop
(CLAUDE.md: "Both test suites must pass after every code change"), and the targets are
unfixed, so the change was reverted before a corpus BIR run. Baseline confirmed this
session pre-change: **Baroque 24/13, Jazz 35/7** (`tools/characterise_bir_false.py`).
Post-revert + rebuild restores it by construction.

---

## Part E — Δ=+7a manual verification (the decisive negative result)

On the **full aggregate**, scored by the actual oracle with run-opening context, the
DCML root appears as a candidate but **loses vertically**:

**bwv102.7 @17520** (was `EbMaj7/Ab`, DCML `AbMaj7` root Ab=8):
```
winner EbMaj7add13/Ab  root=3 bass=8  score 3.575  margin 0.138
   alt Bb13/Ab         root=10        score 3.438
   alt AbMaj9          root=8 bass=8  score 3.425   ← DCML root, loses by 0.150
```
Root stays Eb=3. The aggregate `{C,D,Eb,G,Ab,Bb}` contains D (EbMaj7's maj7) and Bb
(its 5th) at non-trivial weight; EbMaj7add13 explains 5 of 6 PCs vs AbMaj7's 4, so the
*complete* span vertically favors Eb. The "AbMaj7 2.55 > Eb 2.33" in the diagnostic was
for the partial slice-B set `{C,Eb,G,Ab}`, not the aggregate.

**bwv261 @33840** (was `C#m/E`, DCML `F#7` root F#=6):
```
winner C#m6/E  root=1 bass=4  score 3.725  margin 0.000
   alt F#7/E   root=6 bass=4  score 3.500   ← DCML root, loses by 0.225
```
Root stays C#=1. (Already flagged in STATUS.md as needing Phase E; aggregation does not
move it.)

**Conclusion:** the Δ=+7a failure is not "the oracle never sees the full arpeggio." It
is that **even with the full arpeggio aggregated, the vertical oracle prefers the wrong
root** (Eb +0.150, C# +0.225). The discriminator is functional/voice-leading context
(V7→I, ii→V resolution) — **Phase E**, exactly as the redesign-plan Step 4→Step 5
sequencing anticipated. Phase D aggregation is neither sufficient nor, on this corpus,
side-effect-free.

---

## Part F — Structural surprises & recommendation

1. **The same-root+quality merge is inside `runPass1`, not a separate "Pass 2."** This
   invalidated the approved short-sparse-run trigger (Phase D input never contains the
   slices it looks for).
2. **`absorbShortRegions` runs after the insertion point and removes all <480t
   regions**, so batch-final / `*.ours.json` is useless as a Phase-D-input proxy.
3. **The Δ=+7a slices are not sparse** (bwv102.7's failing slice is a complete 4-note
   EbMaj7), and they are already aggregated — the missing step was a re-analysis, which
   we supplied and which still doesn't help.
4. **Aggregation-first is empirically insufficient for Δ=+7a.** The complete aggregate
   vertically prefers the wrong root for both targets. The investigation report's
   prediction held only for a partial tone set.
5. **Re-analyzing all aggregates is corpus-destabilizing** (3 notation regressions, 8
   snapshot drifts) for zero target benefit.

**Recommendation:** do not pursue Phase D arpeggio aggregation as a Δ=+7a fix. Record
"aggregation-first re-analysis of merged regions" as a **dead end** for Δ=+7a alongside
the earlier `<= → <` dead end. The decisive lever is **Phase E** functional context: a
sustained V7→I (bwv261 ii→V) arpeggiation should not be re-rooted on a passing
sonority, regardless of vertical tone weight. If any Phase D work is revisited, it
should target only cases where the aggregate *does* vertically prefer the DCML root
(none of the current 13 BIR=false residuals qualify), with a far narrower trigger than
"all multi-slice aggregates."

---

## Status of the tree

`git checkout -- src/composing/analysis/region/regionanalyzer.cpp` (back to `90a52b5fee`).
Rebuilt; composing/notation/snapshot baselines restored. No source committed. Scratch
artifacts under `C:\tmp\pd_*.py`, `C:\tmp\pd_*.json`, `C:\tmp\pm_*.json`,
`C:\tmp\samp_*.json`.
