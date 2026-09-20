# Δ=+7a Diagnostic + Housekeeping — Report

**Date:** 2026-06-09
**Scope:** read-and-diagnose (Parts A–D, no scoring changes) + housekeeping comment
fixes (Part E, committed) + Gate R unit tests (Part F, committed).
**HEAD at start:** `0b51395527` (master). **Preset:** Baroque.
**Targets:** the two Δ=+7a sub-cluster cases — **bwv102.7** and **bwv261**.

---

## TL;DR — the premise is corrected

The instruction (following `cc_deltaseven_predecessor_report.md`) framed Δ=+7a as
"**the oracle itself returns the wrong winner on vertical evidence alone**" — a pure
vertical-scoring bug, distinct from the rootContinuity-driven Δ=+7b cluster.

**The full per-cell oracle dump falsifies that framing.** In the slices where the
DCML root is actually sounding, the **vertical oracle prefers the DCML root**:

| case | DCML chord (complete) | basisIndep | our root (incomplete/inverted) | basisIndep | vertical winner |
|---|---|---|---|---|---|
| bwv102.7 | AbMaj7 `{C,Eb,G,Ab}` | **1.850** | Eb/Ab | 1.425 | **AbMaj7** (raw 2.55 > 2.33) |
| bwv261 | F#7 `{C#,E,F#,A#}` | **2.150** | C#m/F# | 1.425 | **F#7** (raw 2.85 > 2.83) |

In both, the wrong root wins **only after `rootContinuityBonus` (+0.40)** — a
progression signal, not a vertical term — is added (in bwv261, helped further by large
first-inversion bonuses). The two cases are **not** a vertical-oracle defect.

What actually breaks them is a **two-part mechanism**:

1. **Segmentation splits one DCML harmony across several analyzer sub-regions** (the
   chord is arpeggiated). In the committed / run-opening sub-regions the **DCML root is
   absent from the sounding tones**, so the oracle correctly reads a different root from
   what is present (Eb / C#m). There is nothing for a vertical fix to grab onto — the
   evidence for Ab / F# is genuinely not in those slices.
2. **`rootContinuityBonus` then perpetuates that wrong root** into the sibling sub-region
   where the DCML root *does* sound and *would* win vertically — overturning the oracle's
   correct verdict there.

**Gate R cannot fix either**: in the present-root slices the wrong reading carries a
sounding third / inversion bonus (`basisDep > 0`), so Gate R's `basisDep ≤ 0` guard
correctly spares it. A blanket rcb gate is the Iter-98 mozart dead end. **The real fix is
segmentation / a voice-leading (arpeggio-aware) tone model — Phase D, with a Phase E
functional check — not an oracle term change.**

---

## Part A — Corpus regeneration

```
python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus   # 353 scores, exit 0
```

**BIR confirmation — instruction script vs headline metric.** The instruction's Part A
said to confirm `Baroque BIR=true=24, BIR=false=13` by running
`tools/analyze_inversion_errors.py`. That script reports a **different metric** (its own
three-way music21∩DCML *bassIsRoot* split):

```
Three-way music21_dcml_agree genuine errors: 49   bassIsRoot=true: 27   bassIsRoot=false: 22
```

The headline **24 / 13** is the **lenient-OR `align_regions`** metric, produced by
`tools/characterise_bir_false.py` (the same pipeline the predecessor report used):

```
Processed 353 scores (326 with WiR coverage) -> 13 genuine BIR=false cases
TOTAL genuine BIR=false: 13
delta +7 group: 2 cases  ->  bwv102.7, bwv261
```

**13 BIR=false confirmed** — HEAD state is correct. (The `batch_analyze.exe` binary mtime
`2026-06-09 07:58:43` is newer than all `src/composing` sources, i.e. a current Gate-R +
Sub-9a build, not stale.) The instruction simply cited the wrong script for the 24/13
figure; the corpus is at the committed post-Baroque state.

Full BIR=false enumeration (13): bwv102.7, bwv14.5, bwv17.7, bwv174.5, bwv245.17,
bwv245.40, bwv261, bwv269, bwv301, bwv381, bwv422, bwv432, bwv45.7.

---

## Part B — Failing-region details

Score paths (per `docs/score_inventory.md`): `tools/corpus/bwv102.7.xml`,
`tools/corpus/bwv261.xml` (music21 Bach-chorale exports; `.ours.json` paired).

| | bwv102.7 | bwv261 |
|---|---|---|
| measure.beat / aligned tick | m9 b4.5 / 17520 | m18 b4.5 / 33840 |
| our emitted reading | **EbMaj7/Ab** (root Eb=3, bass Ab=8) | **C#m/E** (root C#=1, bass E=4) |
| DCML reading (WiR) | **AbMaj7** root Ab=8 — *IVmaj7* | **F#7** root F#=6 — *V7* |
| Δ (our−dcml) mod 12 | +7 | +7 |
| detected key (kConf) | **G minor (0.39)** | **B minor (0.69)** |
| aligned-window pcs | {C,D,Eb,G,Ab,Bb} (6) | {C#,E,F#,A#} (4) |
| DCML root present in window? | yes (Ab) | yes (F#) |
| DCML root in our alts? | no | no |
| sub-regions failing | **multiple** (an Eb run) | **multiple** (a C# run) |

**Key structural fact (discovered in Part C):** the `characterise_bir_false.py` "pcs" is
the **union over the aligned window**, which spans *several* analyzer sub-regions. The
actual per-`analyzeChord` snapshots are narrower (Part C). Both failures are runs of
same-root sub-regions, not a single region.

---

## Part C — Full oracle dump (per-snapshot)

Method: temporary `fprintf` in `applyHarmonicFunction()` (the competition pipeline),
gated on the committed winner identity, dumping every `ScoringCell`'s decomposed terms
plus the reconstructed score. Built, run on each score, **diagnostic reverted via
`git checkout` (working tree clean, 0 remnants)**. All pcWeights are uniform *within* a
slice (Bach SATB, equal note durations). `rawScore = (basisIndep + basisDep)·cf·af +
wComplete`; `total = rawScore + rcb·cf·af`.

### bwv102.7 — DCML AbMaj7 is arpeggiated into ≥2 sub-regions

**Slice A — committed "run-start" region (predecessor report's t17520).**
pcs `{D,Eb,G,Bb}` = **EbMaj7** (each w=0.25); bass=Eb; prevRoot=Bb, nextRoot=Ab.
Winner = EbMaj7 root-position, **score 3.05**. **`pcWeight[Ab] = 0.00` — the DCML root
is ENTIRELY ABSENT here.** AbMaj7 is unscorable; Eb is the correct reading of these four
tones. `contFired = 0` (prevRoot Bb ≠ Eb), matching the predecessor report — but the
"wrong root wins vertically" is *because the DCML root is not sounding in this slice*.

**Slice B — sibling region where Ab sounds.** pcs `{C,Eb,G,Ab}` = **AbMaj7** (each
w=0.25); bass=Ab; prevRoot=Eb, nextRoot=Bb.

| field | **wrong winner** Eb/Ab | **DCML** AbMaj7 |
|---|---|---|
| rootPc / bassPc | 3 / 8 | 8 / 8 |
| quality / templateIndex | Major / 1 (Maj7) | Major / 1 (Maj7) |
| basisIndep (pre-rcb) | 1.425 | **1.850** |
| basisDep | 0.900 | 0.700 (bass-root bonus) |
| cf · af | 1.0 · 1.0 | 1.0 · 1.0 |
| wComplete | 0 | 0 |
| **rawScore (no rcb)** | 2.325 | **2.550** |
| rcb | **+0.400** (prevRoot=Eb) | 0 |
| **total** | **2.725** | 2.550 |
| pcWeight[Eb=3] / [Ab=8] | 0.25 / 0.25 | 0.25 / 0.25 |

Eb major's 5th (Bb) is absent here → Eb is *incomplete* (basisIndep 1.425); AbMaj7 is
*complete* (all four tones → basisIndep 1.850). **Vertically AbMaj7 wins by 0.225.**
`rootContinuityBonus +0.40` (from the Eb of Slice A) flips it. **Gate R does not fire
(`gR=0`)** — Eb/Ab's `basisDep = 0.900 > 0`, so the `basisDep ≤ 0` guard spares it.

### bwv261 — DCML F#7 is arpeggiated into ≥3 sub-regions

**Slice 1 — run start (predecessor report's t33600).** pcs `{C#,E,G,B}` = C#ø7
(each 0.25); bass=E; prevRoot=B, nextRoot=F#. Winner C#ø7/E, score 3.35. F#/A# absent.

**Slice 2 — committed emitted region (t33840).** pcs `{C#,E}` (2 PCs, each **0.50**);
bass=E; prevRoot=C#, nextRoot=F#.

| field | **wrong winner** C#m/E | **DCML** F#7/E |
|---|---|---|
| rootPc / bassPc | 1 / 4 | 6 / 4 |
| quality / templateIndex | Minor / 4 (triad) | Major / 2 (Dom7) |
| basisIndep (pre-rcb) | **2.000** | 1.650 |
| basisDep | 0.900 (E = m3, inversion) | 0.000 |
| **rawScore (no rcb)** | **2.900** | 1.650 |
| rcb | +0.400 (prevRoot=C#) | 0 |
| **total** | **3.300** | 1.650 |
| pcWeight[C#=1] / [F#=6] | 0.50 / **0.00** | 0.50 / **0.00** |

**`pcWeight[F#] = 0.00` — the DCML root is ABSENT.** F#7 has only 2 of its 4 tones
present (C#=5th, E=♭7) → basisIndep 1.650. C#m wins by **1.25 even without rcb**. Pure
segmentation. (Emitted as a 3-way tie at 3.30: C#m, C#m7♭5, C#ø7 — all root C#, bass E.)

**Slice 3 — sibling region where F# and A# sound.** pcs `{C#,E,F#,A#}` = **F#7** (each
0.25); bass=F#; prevRoot=C#, nextRoot=G.

| field | **winner** C#m/F# | **DCML** F#7 (root pos) |
|---|---|---|
| rootPc / bassPc | 1 / 6 | 6 / 6 |
| quality / templateIndex | Minor / 4 (triad) | Major / 2 (Dom7) |
| basisIndep (pre-rcb) | 1.425 | **2.150** |
| basisDep | **1.400** (stepwise E→F# + sameRoot C# + completeTriad) | 0.700 (bass-root) |
| **rawScore (no rcb)** | 2.825 | **2.850** |
| rcb | +0.400 (prevRoot=C#) | 0 |
| **total** | **3.225** | 2.850 |
| pcWeight[C#=1] / [F#=6] | 0.25 / 0.25 | 0.25 / 0.25 |

**Vertically F#7 wins (2.850 > 2.825, by 0.025).** The wrong C#m reaches near-parity via
**first-inversion bonuses** (`basisDep = 1.40`: F# bass stepped from E + same-root
continuity + complete triad), and `rootContinuityBonus +0.40` then flips it. **Gate R
does not fire** (`basisDep = 1.40 > 0`).

---

## Part D — Assessment

### bwv102.7 (Eb beats Ab)

1. **Full PC set / Ab weight.** Per snapshot, *not* the 6-PC union. Committed Slice A =
   `{D,Eb,G,Bb}`, **Ab weight 0.00**. Sibling Slice B = `{C,Eb,G,Ab}`, Ab weight 0.25
   (Ab is the bass).
2. **Template Eb wins with / raw vs Ab.** Maj7 (template 1) in both slices. Slice A: Eb
   3.05, Ab unscorable (absent). Slice B: Eb raw 2.325 vs **AbMaj7 raw 2.550** — Ab is
   ahead vertically.
3. **Does an Eb reading genuinely fit?** In Slice A yes (EbMaj7 = the exact tone set, Ab
   not sounding). In Slice B Eb is *incomplete* (no Bb) and only wins via rcb.
4. **Diatonic bonus — not equal, and it matters.** In the detected key **G minor (kConf
   0.39)**, Eb=VI is diatonic (`diatonicRootBonus +0.30`, folded into its basisIndep
   1.425) while Ab=♭II is non-diatonic (no bonus; basisIndep 1.850). So Eb already carries
   a +0.30 key advantage — yet **AbMaj7 still wins vertically (1.850 > 1.425)** because it
   is the complete 4-note chord. The key is mis-detected (DCML's local context is E♭
   major, where Ab=IV is diatonic); under the correct key AbMaj7's vertical lead would be
   *larger*. The key error narrows the gap but does not cause the flip — `rcb +0.40` does.
5. **Inversion/slash reading.** Yes — the winner *is* a slash, Eb/Ab (Ab in the bass,
   foreign to the Eb triad). DCML's AbMaj7 is the root-position reading of the same bass.
6. **Is Ab in the candidacy pool?** Yes — AbMaj7 is scored (raw 2.550) and is the
   *vertical* winner of Slice B. It is absent from the emitted alts only because rcb
   pushes Eb above it and the cap-3 results fill with Eb-bass candidates.

### bwv261 (C# beats F#)

1. **Full PC set.** Committed Slice 2 = `{C#,E}` only; F# present only in sibling Slice 3
   `{C#,E,F#,A#}`.
2. **Are all four C#ø7 / F#7 tones present?** No. The committed slice has just C# and E.
   F#7's four tones are complete only in Slice 3.
3. **F# candidate / template / raw.** F#7 = Dom7 (template 2). Slice 2: raw 1.650 (2/4
   tones). Slice 3: **raw 2.850, the vertical winner**.
4. **Bass note / slash.** Committed bass = E (C#m/E = first inversion, E = m3). DCML F#7
   over E bass = third inversion (F#7/E). Slice 3 bass = F# (root position F#7).
5. **Key / diatonic.** B minor (kConf 0.69). Both C# (ii) and F# (V) are diatonic, so
   `diatonicRootBonus` does **not** separate them — unlike bwv102.7, the key is correct
   and is not the lever here.
6. **extensionThreshold effect.** No threshold subtlety. The committed slice simply lacks
   F# and A# (weight 0.00); the decisive lever in the present-root slice is the
   first-inversion `basisDep` (1.40) + rcb, not extension detection.

### Cross-case

7. **Shared structural pattern.** Yes, strongly: **a single DCML harmony arpeggiated
   across the bar, segmented into multiple same-root sub-regions; the DCML root is absent
   from the committed/early slice (so a different root is read from the present tones),
   then `rootContinuityBonus` carries that root into the sibling slice where the DCML root
   reappears and would win vertically.** Both Δ are +7 because the read root is the 5th of
   the DCML root (Eb = 5th of Ab; C# = 5th of F#) — the classic "we land on the upper
   structure / a fifth above" arpeggiation artifact.
8. **One fix for both?** Not via the oracle. Both share the *segmentation + rcb*
   mechanism, so a segmentation fix (keep the arpeggiated harmony as one region) or a
   Phase-D arpeggio-aware tone model would address both. A single *vertical-oracle* term
   change cannot — in the present-root slices the oracle already prefers the DCML root;
   in the absent-root slices there is no DCML-root evidence to score.
9. **Fixable without Phase D/E context?** No, not safely.
   - A vertical-oracle change is a no-op on the absent-root committed slices and would
     have to fight rcb (not vertical) on the present-root slices.
   - An rcb gate that *would* reach these (it must override `basisDep > 0`, since both
     present-root wrong readings carry inversion bonuses) is precisely the
     Iter-98 / mozart_k280 IV→V65 dead end — Alberti continuity needs that same rcb over a
     moved, inverted bass.
   - **Gate R specifically cannot fire**: both present-root wrong readings have
     `basisDep > 0` (Eb/Ab carries 0.90; C#m/F# carries 1.40), so the `basisDep ≤ 0`
     guard correctly classifies them as legitimate inverted/extended voicings and spares
     them.
   - The correct home is **Phase D** (voice-leading / arpeggio-aware tone collection so
     the full chord is one region) plus a **Phase E** functional check (a sustained ii / V
     pedal arpeggiation should not be re-rooted on its fifth).

**Recommendation:** reclassify both out of "vertical-oracle bug." They are
**segmentation-of-arpeggiated-harmony + rootContinuity self-perpetuation**, defer to
Phase D/E. Do **not** attempt an rcb or vertical-term gate (Iter-98 dead end; Gate R
structurally inapplicable).

---

## Part E — Housekeeping comment fixes

**Commit `927e8b579d`** — `docs/chore: comment fixes …` (comment/doc only; composing
407/407, notation 52/52, pipeline snapshots 11/11; byte-identical, BIR unchanged 24/13).

- **E1** `harmonicfunctionlayer.h` — basisIndep is NOT "without any progression signal";
  it carries the diatonic/resolution bonuses (resolutionBonus is a progression signal)
  from `bassIndependentContextualBonuses`, pre-existing oracle debt (`chordanalyzer.h:329`).
  The one signal it does *not* carry is rootContinuityBonus (pipeline-added). Fixed both
  the field comment and the architecture-header parenthetical.
- **E2** `chordanalyzer.cpp` ~L1631 — the `bassIndep + bassDependent == contextualBonuses`
  invariant is intentionally broken: `contextualBonuses` (diagnoseChord only) still folds
  rcb at L1482; the production split helpers do not. Documented as intentional.
- **E3** `harmonicfunctionlayer.cpp` — Gate R `basisDep ≤ 0` cross-layer dependency on the
  oracle's `sameRootInversionBonus` (chordanalyzer.h:329) made explicit.
- **E4** `regiontonecollector.cpp::findTemporalContext` — documented the backward-only
  gap (no nextRootPc/nextBassPc/bassIsStepwiseToNext; `seg->next1()` available),
  ref `docs/layer_architecture_audit.md` Finding 3.
- **E5** `BUILD_AND_TEST.md` — golden files live at
  `src/notation/tests/pipeline_snapshot_tests/snapshots/` (not `src/composing/tests/...`).
  (Note: the file is git-tracked as `BUILD_AND_TEST.md`.)

---

## Part F — Gate R unit tests

**Commit `bffb6c4e3d`** — `test: Gate R unit tests …`.

To make Gate R testable (F2 asks for "a thin test wrapper around the Gate R block"), two
helpers were promoted to the `fn` namespace and declared in `harmonicfunctionlayer.h`
(behavior-preserving extraction):
- `bassIsTemplateChordTone()` moved out of the anonymous namespace (exposed).
- New `gateRZeroesRootContinuity(cell, rcb, explorationMode)` encodes the full four-part
  Gate R condition; the production call site now calls it (identical logic).

New `src/composing/tests/gater_tests.cpp` (9 tests, wired into the tests CMakeLists):
- **F1** `bassIsTemplateChordTone` table: every interval in each of the 17 templates
  passes and at least one foreign interval fails (the test independently encodes the
  template interval sets, pinning `kMasks` against drift); the Δ=+7b interval 9 fails for
  Major/Minor/Dim/Power (+interval 5 fails for Power); root-offset respected (Eb/G pass,
  Eb/Ab fail); conservative `true` on out-of-range (tiePriority −1 / 17, rootPc −1,
  bassPc −1).
- **F2** Gate R branches: chord-tone bass + basisDep 0 → no-fire; foreign bass + basisDep
  0 → fire; foreign bass + basisDep 0.5 → no-fire; explorationMode → no-fire; rcb 0 →
  no-fire.

Result: **composing 416/416** (407 + 9), Gate R suite 9/9; notation 52/52, pipeline
snapshots 11/11 (the extraction is byte-identical, BIR unchanged 24/13).

---

## Surprises / deltas from the instruction's expectations

1. **`analyze_inversion_errors.py` does not report 24/13** — it reports a different
   metric (27/22). The 24/13 headline is `characterise_bir_false.py` (lenient-OR
   align_regions). Confirmed 13 via the correct script (Part A).
2. **`characterise`'s `pcs` is a union over a multi-slice aligned window**, not a single
   `analyzeChord` snapshot. Gating a diagnostic on that PC-set mask missed the committed
   regions entirely; winner-identity gating was required.
3. **The core premise is wrong.** Both cases are *not* vertical-oracle bugs. In the
   present-root slices the oracle prefers the DCML root; `rootContinuityBonus` (+ large
   inversion bonuses, bwv261) does the flip. They are **segmentation of an arpeggiated
   harmony + rcb self-perpetuation** — Phase D/E, not an oracle term.
4. **Gate R is structurally inapplicable** to these (the present-root wrong readings have
   `basisDep > 0`), confirming Gate R was correctly scoped to the bare-root Δ=+7b cluster.
5. **bwv102.7 also has a key-detection contribution** (G minor kConf 0.39 vs DCML E♭
   major), which structurally favours Eb; bwv261's key (B minor) is correct, so the two
   are not identical — but the proximate flip in both is rcb.
