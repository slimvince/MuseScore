# CC — the L6 GROUPING layer: dormant build + oracle validation

> **Status: HELD for Cowork** (gitignored; `git add` OK, commit of THIS file NOT until an approval file says so).
> Executes `cc_instruction_l6_grouping_build.md` against `cowork_layer6_grouping_design.md` (SIGNED 2026-07-02)
> §5.1–§5.5 / §3 / §6 / §8 / §10. HEAD at dispatch: `9a42714f45`. Three fork-only commits (one change-class each):
> `da06242dd2` module · `73b2a5a791` tests · `b17abc9e71` validation tooling (`--dump-l6` + `compare_l6_oracle --l6`). Gate proof §5.

---

## 0. Headline

- **Assembly, not detection — proven exactly.** L6's punctuation-span boundaries are the L1.5 picked set verbatim:
  the §10 validation reports **added boundaries = 0** and **exact-interior 718/718 movements** → the Task-3 STOP
  guard **PASSES** (L6 invented no boundary).
- **Dormant + byte-identical.** No production `src/` consumer calls `assembleGrouping` (grep-proven — only
  `grouping_tests.cpp` and the `batch_analyze --dump-l6` tool). Suites green (composing **1033** / notation **53** /
  snapshots **11**, no golden refresh); **gate 53/24/53 exact**.
- **18 oracle-asserted unit tests, all green** — the flat partition (totality/flatness/interlock), the §5.1-a codetta
  (inert-default + firing), the §5.1-amendment edge-clip/extension-cue (fire vs score-edge), the D5 mid-span key-area
  independence, the U2 monotone/bounded confidence, the §5.3 window in/out + internal tag, the §5.4 residual, the §5.5
  empty schema.
- **The §10 step-1 validation ran on the 16 dev beds** (read-only). Boundary P/R 33.8/19.3 (the §3.1 baseline minus
  the legitimate edge-tick exclusion, −1.0/−3.1pp); key-area P/R 7.4/0.1 (the dormant L5 modulation detector barely
  fires); cadence alignment 387 closes / 6 internal (GT cadence-at-phraseend rate 91.5%).

---

## 1. Task 1 — the module (commit `da06242dd2`)

**`src/composing/analysis/grouping/groupinglayer.{h,cpp}`** — ONE dormant module implementing exactly §5.1–§5.5 over
**producer-agnostic POD views** (the established L5-unit pattern — `functionoutput.h`/`functioncadence.h`), hand-
injectable, compiling free of the decoder/region/engraving headers.

**Inputs (POD):** `GroupingUnit` (per-unit local-key track + declared boundary key confidence [0,1] + the §5.4
open-mark), `BoundaryInput` (the L1.5 picked tick + strength + `BoundaryCue`/`BoundaryScope` provenance — carried,
never computed), the reused **`FunctionalCadence`** stream (read verbatim, §5.0), and `AnalyzedSpan` (the selection
edges + `startIsSelectionEdge`/`endIsSelectionEdge` — the §5.1-amendment clip distinction). **Output:**
`GroupingLayerOutput { punctuationSpans, keyAreas, cadenceAlignments, schemaSpans }`.

**The rules built (assembly only — §6 proportionality bound):**
- **§5.1** the flat, total partition at the picked boundary ticks (a boundary AT the span edge is an edge marker, not
  an interior cut → no empty leading/trailing span); `}{` interlock (one tick serves end-and-start, no gap).
- **§5.1-a codetta** — a strong-then-weak close pair within the closeness window: the stronger peak is the structural
  end, the weaker is absorbed as a codetta annexe (not a new span). **DEFAULT INERT** (`codettaWindowTicks = 0`), so
  the base partition is the L1.5 set verbatim. *(Declared interpretation: of the two literal §5.1-a statements — "the
  stronger is the structural end" and "the weaker does not open a new span" — the tiling keeps the strong-peak cut and
  drops the weak-peak cut, recording `codettaEndTick`; both hold and the partition stays flat/total.)*
- **§5.1-amendment** `clipped-by-selection-edge` on an edge group whose open/close tick is an artificial **selection**
  edge (not a musical boundary and not the true score edge — the L2 artificial-clip distinction), and `extension-cue`
  on an end-edge span reaching the selection edge with **no** closing boundary and **no** cadence (surfaced only —
  acting on it is the orchestrator's §2.15 job, never L6's).
- **§5.2** key-areas = maximal constant-(tonic,mode) runs; an **independent** flat partition (a key change may fall
  mid-punctuation-span — D5). Confidence = the declared **duration-weighted mean** of the units' declared boundary key
  confidences, **clamped [0,1]**, non-increasing in the weakest unit (U2 Class-M; direction fixed, combiner precision-
  phase). Edge-clip mark applies to an edge key-area too.
- **§5.3** cadence→span alignment: a cadence **closes** the span whose ending boundary lies in `[arrival,
  arrival+window]` (nearest boundary wins; tie → stronger tonic vote — declared); a span with none ends without a
  cadence (valid); an off-window cadence is tagged **`Internal`** (surfaced, never snapped/discarded).
- **§5.4** the Layer-5 open mark is surfaced on the containing punctuation-span AND key-area; never resolved.
- **§5.5** recognised-schema hosting is **empty** absent the consumer (the four core rules stand alone; asserted).

**The firewall (§7).** `alignmentWindowTicks = 480` (one beat — the notation-alignment slack, matching the oracle
tolerance), `codettaWindowTicks = 0` (inert), `codettaStrengthMargin = 0.0` — **declared defaults, NOT tuned**. The
file fixes the rules + their direction, not the numbers.

**Reuse-vs-new + what-retires (the unification rule, §4/§7 — NAMED, touched nowhere).** L6 **reuses** the one L1.5
phrase-boundary primitive, the one L5 `FunctionalCadence`/output, and the L3/L5 local-key carry — it adds no second
boundary/cadence/key detector. At engagement (deferred) it **retires**: `detectCadences()` + `detectPivotChords()`
(`section/sectioncadencedetection.cpp`, the key-dependent `ChordFunction::degree` path) and the `KeyArea` grouping in
`analyzeSection()` (`analyzed_section.h` / `section/sectionanalyzer.cpp`). Those stay live and untouched.

---

## 2. Task 2 — tests (commit `73b2a5a791`)

**`src/composing/tests/grouping_tests.cpp` — 18 `GroupingLayer.*` tests, all green** (full composing suite 1033):

| rule | test(s) |
|---|---|
| §5.1 totality + flatness (tiles, no gap/overlap) | `PartitionIsTotalAndFlat`, `BoundaryAtEdgeMakesNoEmptySpan` |
| §5.1 interlock `}{` (one tick, no gap) | `SpanInterlockNoGap` |
| §5.1-a codetta (inert default; fire strong-then-weak; NOT weak-then-strong) | `CodettaDefaultInertKeepsBothPeaks`, `CodettaRefinementAbsorbsWeakPeak`, `CodettaDoesNotFireWeakThenStrong` |
| §5.1-amendment edge provenance + extension-cue (fire at clip; **NOT** at score edge; not when cadence-closed) | `ClippedSelectionEdgeAndExtensionCue`, `ScoreBoundaryIsNotClippedNoExtensionCue`, `NoExtensionCueWhenClippedEdgeHasCadence` |
| §5.2 D5 mid-span key change + mode split | `KeyAreaBoundaryFallsMidPunctuationSpan`, `KeyAreaSplitsOnModeChangeSameTonic` |
| §5.2 U2 confidence monotone + [0,1] + clamp | `KeyAreaConfidenceBoundedAndMonotone` |
| §5.3 window in/out + inclusive edge + internal tag | `CadenceWithinWindowClosesSpan`, `CadenceOutsideWindowIsInternal`, `CadenceWindowEdgeInclusive` |
| §5.4 residual pass-through (span + key-area) | `OpenMarkSurfacesOnContainingGroups` |
| §5.5 empty schema; degenerate span | `SchemaSpansEmptyAbsentConsumer`, `DegenerateSpanIsEmpty` |

**Dormancy grep-proof:** `assembleGrouping` is called only from `grouping_tests.cpp` and `tools/batch_analyze.cpp`
(the `--dump-l6` diagnostic); **no production `src/` consumer**. Byte-identical on production by construction.

---

## 3. Task 3 — the §10 step-1 validation (commit `b17abc9e71`; read-only)

`batch_analyze --dump-l6` (default-OFF, additive — the fullspine JSON gains an `"l6"` object; `--dump-fullspine`
byte-identical modulo timing) + `compare_l6_oracle.py --l6` (the same shared point-matcher, ±480t). Dev beds only.

### 3.1 The no-added-detection guard (the Task-3 STOP)

**PASS.** Across **718 movements**: **added boundaries = 0**, **exact-interior 718/718**. L6's punctuation-span
boundaries are exactly the interior of `phraseBoundaryTicks` on every movement — it re-thresholds nothing, invents
nothing (§5.1/§6). The boundary P/R vs the §3.1 baseline (34.8/22.4) is **33.8 / 19.3** (dP −1.0pp, dR −3.1pp) — the
whole delta is the legitimate exclusion of the two **edge** ticks (span start `0`, span end `lastTick` — an edge
marker is not an interior cut), *not* leaked detection. *(The fuzzy P/R-vs-baseline band the instruction sketched is
confounded by exactly that edge exclusion, so the exact SET-subset check is the faithful STOP guard — declared.)*

### 3.2 Per-corpus (boundary / key-area / cadence-alignment)

| corpus | mv | bnd P | bnd R | keyarea P | keyarea R | tonic/mode | cad closes | cad internal |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| ABC | 70 | 15.8% | 30.7% | 5.6% | 0.1% | 64% | 72 | 1 |
| bach_en_fr_suites | 89 | 58.6% | 13.8% | 0.0% | 0.0% | 90% | 18 | 1 |
| chopin_mazurkas | 55 | 58.5% | 14.1% | 12.5% | 0.7% | 71% | 31 | 0 |
| corelli | 149 | 40.7% | 22.5% | 0.0% | 0.0% | 71% | 86 | 0 |
| cpe_bach_keyboard | 66 | 55.2% | 14.2% | 0.0% | 0.0% | 66% | 0 | 0 |
| dvorak_silhouettes | 12 | 52.6% | 19.5% | 0.0% | 0.0% | 83% | 7 | 0 |
| grieg_lyric_pieces | 66 | 34.7% | 24.1% | 0.0% | 0.0% | 66% | 33 | 0 |
| mozart_piano_sonatas | 54 | 45.3% | 18.5% | 0.0% | 0.0% | 95% | 18 | 0 |
| schumann_kinderszenen | 13 | 69.2% | 21.1% | 0.0% | 0.0% | 85% | 4 | 0 |
| tchaikovsky_seasons | 12 | 54.1% | 10.1% | 0.0% | 0.0% | 83% | 6 | 0 |
| beethoven_piano_sonatas | 64 | 33.7% | 19.5% | 12.5% | 0.3% | 76% | 52 | 4 |
| wagner_overtures | 2 | 5.9% | 7.7% | 50.0% | 10.0% | 50% | 3 | 0 |
| liszt_pelerinage | 19 | 20.3% | 34.6% | 0.0% | 0.0% | 53% | 28 | 0 |
| rachmaninoff_piano | 22 | 27.5% | 16.9% | 0.0% | 0.0% | 82% | 4 | 0 |
| schulhoff_..._jazz | 6 | 45.2% | 18.4% | 0.0% | 0.0% | 0% | 3 | 0 |
| monteverdi_madrigals | 19 | 36.8% | 15.3% | 0.0% | 0.0% | 40% | 22 | 0 |
| **AGGREGATE** | **718** | **33.8%** | **19.3%** | **7.4%** | **0.1%** | — | **387** | **6** |

### 3.3 Reading the three metrics (baseline of what exists — nothing tuned)

- **Boundary** — as §3.1: exactly the L1.5 picked set (edge-excluded). The L6 layer changes nothing here by design.
- **Key-area — the dormant L5 modulation detector barely fires.** L6 emitted **>1 key-area on only 25 of 718
  movements** (max 5 areas: `n11op95_01`, `op65n06`); aggregate key-area recall is **0.1%** (4/3558 GT local-key
  changes) because most pieces collapse to one home-key area. The **tonic/mode match** of the areas L6 *does* emit is
  40–95% (the home-key area usually matches the GT home key). This is the faithful reflection of the upstream
  modulation substrate, surfaced (§4), not fixed.
- **Cadence alignment — behaves as the GT predicts.** Of 393 detected cadences, **387 close a span, 6 are internal**
  (98.5% closing) — consistent with the **GT cadence-at-phraseend rate of 91.5%** (5911/6463): cadences almost always
  coincide with phrase ends, so almost all align to a span ending. The 6 internal cases are the surfaced tension
  signals (§5.3), not snapped.

### 3.4 Exemplars (stem@tick, for the L6-build design record)

- **Internal cadences (all 6 — the §5.3 mid-span tension signal, surfaced not snapped):** `n02op18-2_04@234240`,
  `BWV809_03_Courante@56400`, `08-3@114000`, `08-3@227280`, `18-4@111360`, `23-1@43920`.
- **Multi-key-area movements (L6 emitted >1 key-area — the modulation detector fired):** `n11op95_01` (5),
  `n11op95_03` (5), `op65n06` (5), `op03n11b` (4), `n03op18-3_01` (3) … (25 movements total).
- **Boundary exemplars** are as the §3.1 report (L6 boundaries == the interior L1.5 picked set).

---

## 4. Unknowns / surfaced-to-Cowork (declaration only — no fixes)

1. **Key-area recall is upstream-bound.** L6's key-area partition is only as rich as the local-key track it reads; the
   dormant L5 modulation recompute fires on ~3.5% of dev-bed movements, so L6 emits one home-key area almost
   everywhere (recall 0.1%). This is an **upstream (L5 §5.4 / L3) substrate property**, not an L6 assembly defect —
   surfaced per the no-inference-driven-coding rule.
2. **§5.1-a codetta interpretation (declared, §1).** The two literal statements of §5.1-a are only jointly satisfiable
   under one tiling choice (keep the strong cut, drop+annex the weak); I implemented and tested that, DEFAULT-INERT.
   If Cowork intends the other reading (physical span extends through the codetta), it is a one-line change + a test
   flip — flagged for the doc's AS-BUILT pass.
3. **Boundary/key-area provenance (`BoundaryCue`/`BoundaryScope`) is carried but not yet populated** — the L1.5
   primitive does not expose per-tick cue/scope today (they default `Unknown`). Populating them is the engage-time
   primitive enhancement named in §3; the L6 contract already carries the fields.
4. **The `--dump-l6` key confidence** wires the single declared home-key confidence (`homeConf`) to every unit (the
   per-unit declared L3/L5 number lands with the D-L3a close-out); faithful for the dormant dump, hand-injected in the
   tests.
5. **`schulhoff` tonic/mode = 0%** — a jazz-idiom bed where the home-key area's (tonic,mode) disagrees with the DCML
   local key on every movement; a repertoire-fit observation, not an L6 bug.

---

## 5. Commits + gate proof

**Three fork-only, unpushed commits (one change-class each):**
- `da06242dd2` — `grouping/groupinglayer.{h,cpp}` + `analysis/CMakeLists.txt` (the module).
- `73b2a5a791` — `tests/grouping_tests.cpp` + `tests/CMakeLists.txt` (18 tests).
- `b17abc9e71` — `tools/batch_analyze.cpp` (`--dump-l6`, additive) + `tools/compare_l6_oracle.py` (`--l6` validation).

Nothing wired into production; the scattered live grouping paths are NAMED, touched nowhere. Measurement outputs
(`tools/corpus_l6_oracle/`) + this report are gitignored/HELD.

**Gate proof (end of run):** composing **1033** / notation **53** / snapshots **11/11** (no golden refresh); the §10
no-added-detection guard **PASS** (added=0, 718/718); `characterise_bir_false.py` → **Baroque 53 / Jazz 24 /
Default 53** exact.

**On this report:** Cowork verifies the module (assembly-only, §6 bound), the tests, and the commit shapes at the
committed objects before ratifying — the L6 spec then flips to AS-BUILT (Cowork's doc half).

Report length: 192 lines.
