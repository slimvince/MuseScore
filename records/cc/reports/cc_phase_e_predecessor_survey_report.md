# Phase E — Predecessor-Confidence Survey for the Δ=+7a rcb Gate

**Date:** 2026-06-09
**Type:** read-only investigation. No source changes, no build. All data from
`batch_analyze.exe --dump-regions {batch,notation-premerge}` and
`--diagnose-measures`, plus the prior instrumented diagnostics in
`cc_deltaseven_7a_diagnostic_report.md` and `cc_deltaseven_predecessor_report.md`.
**Preset:** Baroque (all dumps).
**HEAD:** `90a52b5fee` (post Gate R). BIR baseline 24/13 (Baroque).

---

## TL;DR

**A predecessor-confidence rcb gate is NOT viable for Δ=+7a. It is the same dead end
as Iter-98 / `distinctPcs`, re-confirmed at the present-root-slice granularity and
against the post-Gate-R 13-case set.** No threshold on `previousWinnerScore`,
`previousWinnerMargin`, `previousDistinctPcs`, or `previousWinnerRootPcWeight` separates
the Δ=+7a rcb-source predecessors from the legitimate Mozart Alberti control and the
other continuity-driven BIR=false predecessors:

- **rootPcWeight** of the *true* rcb-source (the internal arpeggio sub-slice): bwv102.7
  = 0.25, bwv261 = 0.50. But the other continuity-driven BIR=false predecessors span
  {bwv245.40 0.25, bwv45.7 0.60, bwv381 1.25}, the Mozart V→V65 control sits at **1.00**,
  and a *correct* Mozart cadential continuation has rcb-source rootPcWeight **0.00**.
  Full overlap; no threshold works.
- **winnerScore**: Δ=+7a predecessors (3.05, 3.30) are *higher* than the Mozart control
  (2.17) — a low-score gate fires backwards.
- **distinctPcs**: the Mozart control is the *sparsest* of all (1) — re-confirms Iter 98.
- The two Δ=+7a cases do not even form a cluster: bwv102.7's rcb source is a 4-PC
  **root-position** triad; bwv261's is a 2-PC **inverted** slice.

The structural reason: in Δ=+7a the rcb-source sub-slice is a *correct, confident*
reading of a *transient* arpeggio harmony (Eb / C# genuinely sound there). It is not
"low-confidence." A confidence signal cannot detect "correctly confident about a tone
that is about to stop being the harmony." The promising lever is forward-looking
(does the next sub-slice complete a chord rooted a 4th below?), not predecessor
confidence. **Recommend: close the predecessor-confidence approach for Δ=+7a.**

**Incidental correction:** Task 4b describes **bwv320 m27 as an "accepted residual."
It is not — Gate R fixed it.** The current committed reading at t37440 is C Major
root-position (= DCML), bassIsRoot=True. bwv320 is absent from the current 13 BIR=false
set (see Section 4b).

---

## Section 1 — Available dump fields

### `--dump-regions batch` (greedy-expand `analyzeRegions`, post-inline-merge)

Per region, `batch_analyze.cpp` writes the following relevant fields
([batch_analyze.cpp:738-810](tools/batch_analyze.cpp#L738-L810)):

| Field | Maps to | Notes |
|---|---|---|
| `startTick`, `endTick`, `duration` | region span | duration in quarter-notes |
| `rootPitchClass`, `quality`, `chordSymbol` | committed identity | |
| `chordScore` | `r.chord.identity.score` | **≈ `previousWinnerScore`** for the next region |
| `chordScoreMargin` | `chordScore − alternatives[0].score` | winner − best alt (cross-bass) |
| `noteCount` | distinct-pc count from `pcMask` | **= `previousDistinctPcs`** |
| `bassPitchClass`, `bassIsRoot` | committed bass | |
| `tones[]` | `{pitch, weight, durationInRegion, isBass}` | lets you compute root-pc weight |
| `alternatives[]` | `{rootPc, bassPc, quality, score}` | runner-up scores |

There is **no** `temporal_context` block and **no** `previousWinnerScore` /
`previousWinnerMargin` / `previousWinnerRootPcWeight` / `previousDistinctPcs` field in
the dump. Those live only in `ChordTemporalContext`
([chordanalyzer.h:619-636](src/composing/analysis/chord/chordanalyzer.h#L619-L636)) and
are *not* mirrored into `ChordTemporalExtensions`
([harmonicrhythm.h:41-51](src/composing/analysis/region/harmonicrhythm.h#L41-L51)).
**The proxy is exact for non-merged regions:** region N−1's `chordScore` is literally
the `previousWinnerScore` fed into region N (both read `rawCandidates[0].score`;
regionanalyzer.cpp:484). `noteCount` = `previousDistinctPcs`. Root-pc tone-weight ≈
`previousWinnerRootPcWeight` (`gateCtx.pcWeight[winRoot]`).

### `--dump-regions notation-premerge` (notation path, pre-coalesce sub-slices)

Same field set, but emitted **before** same-root coalescing — so it exposes the
individual arpeggio sub-slices that the `batch` mode hides. `alternatives[]` is not
populated here (margin shows 0.000), so use it for sub-slice **score / root / bass /
distinctPcs / tone-weights**, and read the margin from the `batch` dump (which, for a
merged run, preserves the first sub-slice's margin — Section 6).

### `--diagnose-measures N`

Re-runs `diagnoseChord` on the **first** region of measure N only (lowest beat), and
**without temporal context** — so `context_bonus ≈ 0` and rcb is *not* reflected. It is
a clean *vertical* re-score. Useful fields: `pc_weights` (exact per-PC weight histogram,
= `gateCtx.pcWeight`), `distinct_pcs`, and `top_candidates[]` with the full additive
component breakdown. **Does not expose any predecessor field.**

**Net:** predecessor confidence is recovered by reading the predecessor region directly.
For arpeggiated/merged runs the *true* rcb predecessor is an internal sub-slice — use
`notation-premerge`, not `batch` (Section 6).

---

## Section 2 — Δ=+7a predecessor profiles

The decisive ("present-root") slice is the sub-slice where the DCML root finally
attacks. Its rcb source is the **immediately preceding sub-slice**, which the inline
merge ([regionanalyzer.cpp:510-518](src/composing/analysis/region/regionanalyzer.cpp#L510-L518))
absorbs into the merged region shown by `batch`. Values below are from
`notation-premerge` + cross-checked against the instrumented numbers in
`cc_deltaseven_7a_diagnostic_report.md` Part C (which agree exactly).

### bwv102.7 (DCML AbMaj7, root Ab=8; key G minor)

| sub-slice | startTick | endTick | dur(qn) | committed | bass | bIR | distinctPcs | score | margin | rootPcWeight |
|---|---|---|---|---|---|---|---|---|---|---|
| **rcb-source (Slice A)** | 17520 | 17760 | 0.5 | **Eb Major** | Eb | True | **4** | **3.050** | **0.325** | **0.25** |
| present-root (Slice B, FAIL) | 17760 | 18240 | 1.0 | Eb Major | **Ab** | False | 4 | 2.725 | — | Eb 0.25 / Ab 0.25 |

At Slice B the oracle prefers AbMaj7 vertically (raw 2.550 > Eb raw 2.325, +0.225);
`rootContinuityBonus +0.40` from Slice A's Eb flips it to Eb (total 2.725 > 2.550).
**The rcb source (Slice A) is a clean, confident, root-position Eb-major triad** — its
only weak signal is rootPcWeight 0.25 (Eb is a brief arpeggio tone). Gate R does not
fire (Slice B `basisDep = 0.90 > 0`).

### bwv261 (DCML F#7, root F#=6; key B minor)

| sub-slice | startTick | endTick | dur(qn) | committed | bass | bIR | distinctPcs | score | margin | rootPcWeight |
|---|---|---|---|---|---|---|---|---|---|---|
| Slice 1 (run start) | 33600 | 33840 | 0.5 | C# HalfDim | G | False | 4 | 2.650 | (0.363) | 0.25 |
| **rcb-source (Slice 2)** | 33840 | 34080 | 0.5 | **C# Minor** | E | False | **2** | **3.300** | **0.000** | **0.50** |
| present-root (Slice 3, FAIL) | 34080 | 34560 | 1.0 | C# Minor | **F#** | False | 4 | 3.225 | — | C# 0.25 / F# 0.25 |

At Slice 3 the oracle prefers F#7 vertically (raw 2.850 > C#m/F# raw 2.825, +0.025);
`rootContinuityBonus +0.40` (C# from Slice 2) flips it. **bwv261's rcb source (Slice 2)
is a 2-PC, inverted (bass E), C-minor reading** — structurally unlike bwv102.7's source.
Gate R does not fire (Slice 3 `basisDep = 1.40 > 0`, first-inversion bonus).

> The C# root self-perpetuates from Slice 1 → Slice 2 → Slice 3; the "predecessor" at
> each step is the prior sub-slice, all inside the eventually-merged region.

---

## Section 3 — Control predecessor profiles

### 3a. Mozart K280-1 — Alberti V→V65 (rcb is CORRECT here)

`tools/dcml/mozart_piano_sonatas/MS3/K280-1.mscx`, F major. Premerge sub-slices around
the two V65 sites the Iter-98 rcb gate broke:

| site | sub-slice | startTick | endTick | committed | bass | bIR | distinctPcs | score | rootPcWeight | role |
|---|---|---|---|---|---|---|---|---|---|---|
| m9 | C anchor | 12480 | 12720 | C Major | C | True | **1** | 2.170 | **1.00** | rcb SOURCE for V65 |
| m9 | **V65** | 12720 | 12960 | C Major | G | False | 2 | 2.200 | **0.00** | rcb correctly sustains C |
| m9 | I6/cad | 12960 | 13080 | C Major | E | False | 4 | 2.950 | 0.25 | (rcb source = V65, rootW 0.00) |
| m12 | C anchor | 16800 | 17040 | C Major | C | True | **1** | 2.170 | **1.00** | rcb SOURCE for V65 |
| m12 | **V65** | 17040 | 17280 | C Major | G | False | 2 | 2.700 | **0.00** | rcb correctly sustains C |

Two findings that bracket any rootPcWeight threshold from both sides:
1. **The V65's rcb source has rootPcWeight 1.00** (the Alberti root C is the repeating
   bass anchor). A `rootW < t` gate with `t ≤ 1.0` does NOT block the V65 — good.
2. **But the *next* correct continuation (t12960, C/E) has an rcb source of rootPcWeight
   0.00** (the V65, where C is absent). Any `rootW < t` gate fires here. It happens to be
   harmless on this score (C major wins vertically with 4 PCs), but it shows the gate
   fires on correct Mozart continuity — the exact fragility the prior report flagged.

### 3b. bwv320 — NOT a residual; Gate R fixed it

`batch` dump around m27:

| startTick | endTick | committed | bass | bIR | nPc | score | DCML |
|---|---|---|---|---|---|---|---|
| 36960 | 37440 | G Minor | G | True | 2 | 2.401 | (predecessor) |
| **37440** | 38400 | **C Major** | **C** | **True** | 3 | 1.900 | **C ✓** |

The m27 reading is now **C Major root-position = DCML** (alt `C/E`, same root). The old
`G/E` (Δ=+7b) mis-fire is gone — Gate R (`638ced1c12`) withholds rcb from the foreign-bass
G continuation. bwv320 is **absent from the current 13 BIR=false set** (Section 4b). It is
therefore no longer available as a "Δ=+7b residual" control; the closest live analogues
are bwv45.7 and bwv381 (Section 4, same-root continuity that Gate R does not catch).

---

## Section 4 — Full 13-case predecessor survey (current Baroque BIR=false)

Source: `tools/characterise_bir_false.py` on the post-Gate-R corpus → **13 cases**.
For each failing region, the PRED row is the immediately preceding `batch` region (the
first-order rcb source). **Caveat:** for inline-merged arpeggio runs (the Δ=+7a pair),
the dump PRED is the region *before the run*, NOT the true rcb source; the true source
is the internal sub-slice from Section 2 (flagged ✸).

`contFired?` = does the failing region's committed root equal its predecessor's root
(continuity rewarded the wrong winner)?

| # | case | Δ | PRED committed | PRED score | PRED margin | PRED distinctPcs | PRED rootW | contFired? | true rcb-source rootW |
|---|---|---|---|---|---|---|---|---|---|
| 1 | bwv102.7 | +7 | Bb (pre-run) | 3.520 | 0.000 | 4 | 0.85 | **internal** ✸ | **0.25** (Slice A) |
| 2 | bwv261 | +7 | B (pre-run) | 2.660 | 0.000 | 5 | 0.95 | **internal** ✸ | **0.50** (Slice 2) |
| 3 | bwv245.40 | +2 | F/A Major | 2.850 | 0.338 | 4 | **0.25** | **YES** (F→F) | 0.25 |
| 4 | bwv45.7 | +8 | F#m | 3.520 | 0.000 | 3 | **0.60** | **YES** (F#→F#) | 0.60 |
| 5 | bwv381 | +3 | G Major | 3.420 | 0.000 | 5 | **1.25** | **YES** (G→G) | 1.25 |
| 6 | bwv422 | +2 | Bm | 3.180 | 0.490 | 4 | 0.45 | no (B→A) | n/a |
| 7 | bwv174.5 | +8 | A Major | 2.100 | 0.000 | 4 | 1.20 | no (A→E) | n/a |
| 8 | bwv269 | +8 | G Major | 3.520 | 0.000 | 3 | 0.60 | no (G→D) | n/a |
| 9 | bwv301 | +8 | Dm | 3.420 | 0.000 | 3 | 0.80 | no (D→G) | n/a |
| 10 | bwv17.7 | +6 | D Major | 2.600 | 0.000 | 4 | 0.29 | no (D→A) | n/a |
| 11 | bwv432 | +5 | Em | 2.070 | 0.000 | 6 | 1.70 | no (E→A) | n/a |
| 12 | bwv14.5 | +9 | Bb Major | 3.520 | 0.000 | 3 | 0.60 | no (Bb→G) | n/a |
| 13 | bwv245.17 | +3 | D/E min | 3.430 | 0.000 | 4 | 0.45 | no (D→F) | n/a |

**Mozart control** (for comparison): rcb-source rootW **1.00**, score 2.170, margin 0.262,
distinctPcs **1**.

### Grouping by failure type / mechanism

- **Δ=+7a (arpeggio + rcb cascade):** bwv102.7, bwv261. Continuity is the blocker at the
  present-root slice; rcb source is an internal sub-slice (rootW 0.25 / 0.50).
- **Same-root continuity, NOT arpeggio (Gate-R-shaped but not caught):** bwv245.40 (sus,
  rootW 0.25), bwv45.7 (rootW 0.60), bwv381 (rootW 1.25). These are the live analogues of
  the old Δ=+7b cluster; Gate R misses them (`basisDep > 0` and/or sus quality).
- **Sus / quartal vertical:** bwv422, bwv245.40 — DCML hears a quartal trichord; our sus
  reading wins vertically (not continuity, except bwv245.40 also has same-root pred).
- **Vertical / segmentation (contFired = no):** bwv174.5, bwv269, bwv301, bwv45.7-quality,
  bwv17.7, bwv432, bwv14.5, bwv245.17. The wrong root wins on present tones; the
  predecessor's root differs, so **rcb did not cause these** — a predecessor-confidence
  gate is irrelevant to 8 of 13.

---

## Section 5 — Gap analysis

### Q1 — Is there a threshold that separates Δ=+7a rcb-sources from the controls?

**No, on every metric.** Collecting the *true rcb-source* values for the
continuity-driven BIR=false cases against the controls:

| metric | bwv102.7 | bwv261 | bwv245.40 | bwv45.7 | bwv381 | **Mozart V65** | **Mozart I6 (correct)** |
|---|---|---|---|---|---|---|---|
| rcb-source **rootPcWeight** | 0.25 | 0.50 | 0.25 | 0.60 | 1.25 | **1.00** | **0.00** |
| rcb-source **score** | 3.05 | 3.30 | 2.85 | 3.52 | 3.42 | **2.17** | 2.20 |
| rcb-source **margin** | 0.325 | 0.000 | 0.338 | 0.000 | 0.000 | **0.262** | 0.000 |
| rcb-source **distinctPcs** | 4 | 2 | 4 | 3 | 5 | **1** | 2 |

- **rootPcWeight — fails.** Δ=+7a sources are {0.25, 0.50}, but the broader
  continuity-driven set reaches 0.60 (bwv45.7) and **1.25** (bwv381), and the Mozart V65
  control is 1.00 while a *correct* Mozart continuation is **0.00**. To catch {0.25, 0.50}
  you need `t > 0.50`; that fires on the correct Mozart I6 (0.00) and on the huge corpus
  population of inverted/brief-root continuation predecessors, and still misses bwv45.7
  and bwv381. Even restricted to *only the two Δ=+7a points vs the V65 control*, a window
  `0.50 < t < 1.00` exists — but it is contradicted by the correct Mozart I6 at 0.00 and is
  not a structural property (Q3).
- **score — fails / backwards.** Δ=+7a sources (3.05, 3.30) are *higher* than the Mozart
  control (2.17). A "low-confidence-score → kill rcb" rule fires on Mozart, not on Δ=+7a.
- **distinctPcs — fails (re-confirms Iter 98).** Mozart V65 source is the sparsest of all
  (1). bwv261's source (2) is next. The control is at the extreme any sparsity rule targets.
- **margin — fails.** 0.000 is pervasive corpus-wide (template ties at the top of the
  winning bass group, not uncertainty). Confident, correct triads (bwv45.7, bwv381,
  Mozart I6) all carry 0.000.

### Q2 — Proposed condition?

None survives. The narrowest finding — "rcb-source rootPcWeight ≤ ~0.5 separates the two
Δ=+7a points from the Mozart V65 control" — is falsified by (a) the correct Mozart
cadential continuation whose rcb-source rootPcWeight is **0.00**, and (b) bwv45.7 /
bwv381, which are same-mechanism continuity errors with rcb-source rootPcWeight 0.60 /
1.25 that the threshold would leave unfixed. A gate that fixes the Δ=+7a pair would fire
on a large, mostly-correct corpus population (any continuation whose rcb predecessor was
inverted or had a brief root), exactly the Iter-98 regression profile.

### Q3 — Why no clean gap

Two structural reasons:

1. **The Δ=+7a rcb source is correctly confident about a transient.** The arpeggio
   genuinely spells Eb (bwv102.7) / C# (bwv261) in that sub-slice; the oracle is *right*
   to read it there. "Confidence" measures whether the reading fits the present tones —
   it does. The error is temporal (the harmony is *about to* complete a fourth below), not
   a confidence deficit. No predecessor-confidence metric can encode "right now, wrong in
   240 ticks."
2. **The same metric value carries opposite meaning at different ticks.** rootPcWeight
   0.00 is the *correct* continuity signal at the Mozart V65 (sustain V across the gap)
   but would be a "kill" signal under a low-weight gate. The Mozart Alberti root oscillates
   between rootW 1.00 (anchor) and 0.00 (off-beat) within one sustained harmony, so it
   populates both ends of any threshold for a single correct chord.

### Q4 — Overall assessment

**Predecessor-confidence rcb gating is a dead end for Δ=+7a — close it.** This
re-confirms `cc_deltaseven_predecessor_report.md` (2026-06-08) at finer granularity and
on the post-Gate-R set, and matches `redesign_plan.md` Step 2's standing conclusion
("No threshold can block the wrong cases without blocking the correct ones").

The genuinely promising direction is **forward**, not backward: at the present-root slice
the next sub-slice completes a chord rooted a 4th below the rcb root (Ab below Eb; F#
below C#), and `nextRootPc` is now populated (bridge forward-lookahead `90a52b5fee`). A
Phase-E rule of the form "do not let rcb sustain a root when the slice's own bass + the
forward context complete a more-complete chord a 4th below" targets the actual mechanism
(a sustained IV/V arpeggiation should not be re-rooted on its fifth) without keying on
predecessor confidence. That is a separate investigation; this survey's scope (predecessor
confidence) is exhausted.

---

## Section 6 — Structural note: dump view vs. what rcb actually reads

**The `batch` dump shows the merged arpeggio run as a single region, and its committed
winner reflects the STALE FIRST-SUB-SLICE identity, not the aggregate.**

- bwv102.7: `batch` shows one region **t17520–18240, "Eb Major / Ab", 6 distinct PCs,
  score 3.050, margin 0.325**. The inline merge
  ([regionanalyzer.cpp:510-518](src/composing/analysis/region/regionanalyzer.cpp#L510-L518))
  keeps `regions.back().chordResult` (Slice A's root/quality/score/**alternatives**) and
  only (i) extends `endTick`, (ii) merges tones, (iii) re-points `bassPc` to the merged-tone
  bass (Ab). So the dumped region is a composite: **Slice A's score (3.050) + Slice A's
  margin (0.325) + Slice A's Eb identity + the merged 6-PC tone set + Ab bass.** Confirmed
  numerically: the dump's 3.050 / 0.325 equal Slice A's premerge score and the prior
  diagnostic's Slice A margin; the present-root Slice B (score 2.725) is invisible.
- bwv261: same pattern — `batch` shows **t33840–35040, "C# Minor / E", score 3.300**,
  which is Slice 2's score; Slices 1 and 3 are absorbed.

**Does the dump predecessor match `previousRootPc` at the failing slice? No — for
arpeggiated runs it does not.** At the decisive present-root sub-slice, `previousRootPc`
= the *immediately preceding sub-slice's* root (Eb for bwv102.7, C# for bwv261), which is
*inside* the merged region. The region shown *before* the merged run in the `batch` dump
(Bb for bwv102.7, B-minor for bwv261) is two-or-more sub-slices back and is **not** what
rcb reads. Consequences for any extraction tooling:

- The proxy "read the dump's predecessor region" is valid **only** for non-merged failing
  regions (the 11 non-arpeggiated cases in Section 4).
- For Δ=+7a (and any inline-merged run), the true rcb predecessor must come from
  `notation-premerge`. The `batch` merged region's `chordScore`/`chordScoreMargin` happen
  to equal the first sub-slice's values (because the merge preserves `chordResult`), so
  those two numbers *are* usable as the rcb-source score/margin — but its `noteCount`
  (6 / 4) and `rootW` (0.50 / 0.75) reflect the **aggregate**, not the rcb source
  (premerge: 4 / 0.25 and 2 / 0.50). Mixing them silently overstates the predecessor's
  distinctPcs and root weight.

---

## Reproduction

```
# 13-case list (post-Gate-R)
python tools/characterise_bir_false.py

# Δ=+7a present-root sub-slices (true rcb source)
ninja_build_rel/batch_analyze.exe tools/corpus/bwv102.7.xml --preset Baroque --dump-regions notation-premerge
ninja_build_rel/batch_analyze.exe tools/corpus/bwv261.xml  --preset Baroque --dump-regions notation-premerge

# Mozart Alberti control
ninja_build_rel/batch_analyze.exe tools/dcml/mozart_piano_sonatas/MS3/K280-1.mscx --preset Baroque --dump-regions notation-premerge

# merged-region view (Section 6)
ninja_build_rel/batch_analyze.exe tools/corpus/bwv102.7.xml --preset Baroque --dump-regions batch
```

Extraction helpers used: `C:\tmp\survey_extract.py` (tick-window table) and
`C:\tmp\survey_pred.py` (failing-region + predecessor). Prior instrumented data
corroborated: `cc_deltaseven_7a_diagnostic_report.md` Part C,
`cc_deltaseven_predecessor_report.md` Tables 1–2.
