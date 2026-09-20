# CC Report — Bridge forward-lookahead fix in `findTemporalContext`

*Date: 2026-06-09. Branch: master. Base HEAD before this work: `bffb6c4e3d`.*

This is the correctness/infrastructure fix described in
`docs/layer_architecture_audit.md` Finding 3 (and referenced by Finding 7): the
bridge path's `findTemporalContext` looked backward only, so the forward-lookahead
fields were never populated on the live annotation path. The fix adds a forward walk.

---

## 1. What was added to `findTemporalContext`

**File:** `src/composing/analysis/engravingbridge/regiontonecollector.cpp`
(`findTemporalContext`, ~L749–888). Header doc comment updated in
`src/composing/analysis/engravingbridge/regiontonecollector.h` (accuracy only).

A **forward-lookahead walk** was added that is an exact mirror of the existing
backward walk, using `seg->next1(SegmentType::ChordRest)` instead of
`seg->prev1(...)`:

1. Walk forward from `seg` via `next1(SegmentType::ChordRest)`, skipping segments
   with no chord attacks (same `hasAttacks` pre-check as the backward walk).
2. On the first segment with attacks, collect its sounding tones with the same
   `collectSoundingAt(sc, s, excludeStaves, …)` + `buildTones(…)` helpers the
   backward walk uses.
3. Cold-analyze them: `chordAnalyzer->analyzeChord(nextTones, keyFifths, keyMode,
   nullptr, kDefaultChordAnalyzerPreferences, &nextGateCtx)` — `nullptr` context, so
   no recursion / no infinite-depth analysis (identical to the backward cold analysis).
4. Run the same committed gate pipeline as the production call sites:
   `applyIter8691Pedal(...)` then `applyPostScoringGates(...)`, both with `nullptr`
   context — so `nextRootPc` reflects the gate-corrected identity, not the raw oracle
   winner (matches `inferNextRootPc` in `chordanalyzer.h` and the batch call sites).
5. Set `temporalCtx.nextRootPc = nextResults.front().identity.rootPc` and
   `temporalCtx.nextBassPc = nextResults.front().identity.bassPc`.
6. After the walk, compute
   `temporalCtx.bassIsStepwiseToNext = isDiatonicStep(currentBassPc, nextBassPc)`
   using the same `isDiatonicStep` helper used for `bassIsStepwiseFromPrevious`.

The stale "IMPLEMENTATION GAP" comment block (which asserted the forward fields are
never set) was replaced with an accurate two-direction description, and the remaining
gap (Step 1/2 progression fields `previousWinnerScore/Margin/RootPcWeight`,
`previousDistinctPcs` — which need the neighbour's committed competition result and a
full pre-pass) is documented as still-open.

**Scope:** only `regiontonecollector.cpp` (+ the `.h` doc comment). No scoring logic,
gate thresholds, or other `src/composing/` files touched. No signature change to
`findTemporalContext`. No new helpers needed (all symbols were already used by the
backward walk).

**Batch path is unaffected:** `regionanalyzer.cpp` calls `findTemporalContext` once to
seed the *initial* `previous*` fields, then overwrites `nextRootPc`/`nextBassPc`/
`bassIsStepwiseToNext` every iteration (L420/431–437). The new forward walk's results
are immediately overwritten there, so the batch path is behaviorally unchanged (the
seed call passes `currentBassPc = -1`, so the seed `bassIsStepwiseToNext` is `false`
either way).

---

## 2. Test results

| Suite | Result |
|---|---|
| composing_tests | **416 / 416** |
| notation_tests | **52 / 52** (includes P1–P4 pipeline regression) |
| pipeline_snapshot_tests | **11 / 11** (1 skipped: `PipelineDivergenceCObservation.GenerateReport`, always skipped) |

Build: clean (13/13 link targets, only pre-existing C4100 warnings in `chordanalyzer.cpp`).

---

## 3. Snapshot drifts

Three ticks drifted, all in the **`tickLocal` (P4)** section of two goldens — the
per-onset bridge path that calls `findTemporalContext` directly (via
`analyzeHarmonicContextLocallyAtTick`). The `annotation` (P2) and `tickRegional` (P3)
sections did **not** change. P4 `tickLocal` analyzes only the notes sounding at a single
onset segment (`collectSoundingAt` on one segment), so its note set is finer than the
batch/regional region.

Ground truth obtained two ways: (a) `batch_analyze --preset Baroque` (batch path = the
designated DCML proxy, has forward context), and (b) the literal onset notes from the
DCML `*.notes.tsv` (the bach_chorales corpus ships no harmony labels, so the literal
sonority + batch reading are the references).

### Drift 1 — `bach_chorale_137` (BWV 301), tick 2880 — **IMPROVEMENT**

| | root / quality |
|---|---|
| Before | `minor / D` (Dm) |
| After | `halfDiminished / B` (Bø7) |
| Batch path (P3 + `batch_analyze`) | `Bm7b5/D` (HalfDiminished, root B, bass D) |
| Onset notes (qb 6.0) | D, F, A, B — bass D |

The notes {B,D,F,A} are an **exact Bø7** (B-D-F-A); read as Dm they are Dm6 (3 chord
tones + added 6th). Bridge **converges to the batch path** (Bø7/D). This is precisely
the case the corpus comment flags: chorale_137 "contains MinorAdd6 inversions at mm. 2,
4, 14; verifies gates G-B/G-C/G-D fire in the bridge path" — Gate G-B now fires on the
bridge because `nextRootPc`/`bassIsStepwiseToNext` are populated. DCML improvement.

### Drift 2 — `bach_chorale_001`, tick 15600 — **IMPROVEMENT**

| | root / quality |
|---|---|
| Before | `minor / B` (Bm) |
| After | `major / G` (G) |
| Onset notes (qb 32.5) | D3, B3, G4, B4 → {G, B, D} — bass D |

The onset sonority is a **G major triad** (G-B-D); the neighbouring F#4 releases exactly
at qb 32.5 (`collectSoundingAt` excludes a note whose end == anchor tick), so it is not
in the set. A "B minor" reading is impossible from {G,B,D} (no F#). The old value was a
genuine per-onset error; the new value matches the literal sonority. The forward-lookahead
inversion gate (Gate E: Minor winner, Major alt at root+8 = B+8 = G, + `bassIsStepwiseToNext`)
now fires and restores the correct G major. DCML improvement. (The batch *region* path
labels the surrounding region differently because it aggregates the passing F#; that is a
segmentation-granularity difference, not a conflict — at this single onset, G major is
unambiguously correct.)

### Drift 3 — `bach_chorale_001`, tick 11280 — **NEUTRAL**

| | root / quality |
|---|---|
| Before | `diminished / F#` (F# dim triad) |
| After | `halfDiminished / F#` (F#ø7) |
| Onset notes (qb 23.5) | A2, C4, C5, F#4 → {F#, A, C} — bass A |
| Batch + notation regional path | the whole span tick 9120–11520 = **G major** (I); this onset is an embellishing passing chord, not segmented as its own region |

**Root F# (vii / leading-tone function) is unchanged** before and after. The onset is a
passing F# diminished triad: E4 (the prior Am chord's 5th) releases at qb 23.5 and is
replaced by the upper-neighbour F#. The shift dim-triad → ø7 imputes the diatonic 7th of
the G-major leading-tone seventh (F#ø7 = F#-A-C-E *is* the correct vii⁷ in G major; the 7th
E literally sounded the instant before). Because the batch/DCML-proxy reading subsumes this
entire span into G major (I), neither dim nor ø7 appears at the region level — the change is
a per-onset quality nuance on an embellishing chord, with root and harmonic function
preserved. Not a divergence from DCML harmony. Classified neutral (winner root/function
unchanged; consistent with the prevailing I and the diatonic vii⁷ of the key).

**No regressions.** All three drifts are improvement or neutral; none move the winner
root away from the DCML/batch reading. Goldens regenerated with
`pipeline_snapshot_tests.exe --update-goldens` and re-verified (11/11).

---

## 4. BIR (informational only)

Baroque corpus regenerated (353 scores, 326 with WiR coverage) and characterized with
`tools/characterise_bir_false.py` (the correct script — `analyze_inversion_errors.py`
reports a different metric).

**BIR=false = 13 — unchanged** from the documented baseline (24/13). Same 13 cases as
before (bwv102.7, bwv14.5, bwv17.7, bwv174.5, bwv245.17, bwv245.40, bwv261, bwv269,
bwv301, bwv381, bwv422, bwv432, bwv45.7). This fix is not BIR-targeted; the result
confirms zero BIR regression on the batch corpus (expected, since the batch path is
behaviorally unchanged — see §1). The fix's effect is confined to the bridge/live path.

---

## 5. Commit

**`90a52b5fee`** — `fix: bridge forward-lookahead in findTemporalContext — populate
nextRootPc/nextBassPc/bassIsStepwiseToNext via seg->next1()`

Staged exactly four files (no `tools/corpus` regen artifacts, no unrelated session-start
doc edits):
- `src/composing/analysis/engravingbridge/regiontonecollector.cpp` (the forward walk)
- `src/composing/analysis/engravingbridge/regiontonecollector.h` (doc comment accuracy)
- `src/notation/tests/pipeline_snapshot_tests/snapshots/bach_chorale_001.json` (goldens)
- `src/notation/tests/pipeline_snapshot_tests/snapshots/bach_chorale_137.json` (goldens)

---

## 6. Structural surprises / judgment calls

- **Measure-boundary gating of `next1()`:** I deliberately did **not** restrict the
  forward walk to the current measure. The backward walk crosses measure boundaries
  (`prev1` is the score-global iterator), and the batch lookahead (`collectRegionTones`
  over the next region) also crosses barlines. Cadential bass motion across a barline is
  exactly what `stepwiseBassLookaheadBonus` and the forward gates are designed to detect,
  so the next *sounding* chord is taken regardless of measure — matching both the backward
  walk and the batch path. Restricting to the measure would have re-introduced an
  asymmetry between the two directions.

- **`nextBassPc` source:** per the instruction I set `nextBassPc` from the cold-analyzed
  `identity.bassPc` (mirroring how the backward walk sets `previousBassPc` from
  `identity.bassPc`). The batch path instead derives `nextBassPc` from the raw
  lowest-pitch-class of the next region's tones. In practice these coincide — `identity.bassPc`
  is the pitch class of the lowest sounding tone (`buildTones` marks the lowest ppitch as
  bass) — so there is no behavioral divergence, and the identity-based form keeps the two
  walks symmetric.

- **All drifts landed in P4 `tickLocal`, none in P2 `annotation`:** the live annotation
  path (P2) was unchanged by these three scores' opening measures, while the per-onset P4
  path shifted. Both paths now populate forward context; the P4 shifts are the visible
  consequence because P4 pins per-onset identities where the new gates have the most
  leverage.
