# CC — Module Layering Assessment Dossier (READ-ONLY survey)

**Status:** HELD (gitignored) — investigation only. No code changed, no build run.
**HEAD:** `41f7c65f63` (unchanged — Refactor #1, the byte-identical `chordanalyzer.cpp` split).
**Scope:** `src/composing/analysis/` — every `.cpp` TU > ~200 lines plus all task-named TUs.
**Method:** full source reads (5 parallel read-only inventories + direct verification of the
joint-key seam). Every classification below carries `file:line` cites. **Nothing recommended
built** — this is the measured map for a Cowork/user direction call (more splits, in priority
order, vs. begin the audit).

---

## §0 — TL;DR

- **One refactor-#1-shaped god-file pattern recurs in 5 TUs** (regiontonecollector, harmonicsegmenter,
  keymodeanalyzer, sectionanalyzer, regionanalyzer) and **mildly in 1** (keyresolver). In every case the
  shape is identical to what `chordanalyzer.cpp` was: **whole free functions peel off byte-identically into
  responsibility-named TUs, while one oversized orchestrator/accumulator god-function holds the genuinely
  entangled core** that cannot move without a logic/state change.
- **The joint-decision 2-pass bolt-on is NOT a bolt-on smear.** `decideJointKey` is a clean pure function
  (inputs→`JointKeyResult`, zero section/region state mutation); `applyJointKeyWiring` is a self-contained
  free function called once behind a gate at the tail of `analyzeRegions`. Both are **already cleanly
  layered**; extracting them is pure-byte-identical but **low audit value** (they aren't hurting
  auditability). Verified against source (§4).
- **8 TUs are already single-responsibility / audit-ready now** (the entire `function/` and `chord/` layers,
  plus jointkeydecision, localmodulationdetector, cadencekeyanchor, sparsechordrefinement, modepriorpresets).
- **The deepest tangle in the largest file (`regionanalyzer.cpp`, 1167) is behavior-entangled, NOT a pure
  split** — the triplicated Pass-1/2/2b region-analysis bodies. So the largest file is *not* the top
  pure-split candidate. Highest pure-extraction yield is **`regiontonecollector.cpp`** (5 whole functions
  lift out clean).

---

## §1 — Inventory + classification (all surveyed TUs)

| TU | Lines | Classification | Pure-split yield |
|---|---|---|---|
| `region/regionanalyzer.cpp` | 1167 | **CONFLATED** (5 concerns) | peripheral only (core entangled) |
| `harmony/harmonicsegmenter.cpp` | 943 | **CONFLATED** | 3–4 free fns + `fillGap` file-move |
| `key/keymodeanalyzer.cpp` | 942 | **CONFLATED** (8 concerns) | display + data + 2 scorer clusters (1 caveat) |
| `engravingbridge/regiontonecollector.cpp` | 891 | **CONFLATED** (5 concerns) | **5 whole free functions — highest** |
| `section/sectionanalyzer.cpp` | 971 | **CONFLATED** | cadence/pivot + Pass-4 stabilization |
| `key/keyresolver.cpp` | 361 | **CONFLATED (mild)** | 1 seam (`partialSignatureCorrection`) |
| `function/harmonicfunctionlayer.cpp` | 567 | **SINGLE** (cohesive layer) | — audit-ready |
| `section/jointkeydecision.cpp` | 422 | **SINGLE** (+ orphan flag) | — audit-ready |
| `section/localmodulationdetector.cpp` | 311 | **SINGLE** | — audit-ready |
| `section/cadencekeyanchor.cpp` | 232 | **SINGLE** (cohesive pair) | — audit-ready |
| `region/sparsechordrefinement.cpp` | 220 | **SINGLE** | — audit-ready |
| `function/tonicizationlabeler.cpp` | 203 | **SINGLE** | — audit-ready |
| `key/modepriorpresets.cpp` | 156 | **SINGLE** (pure data) | — audit-ready |
| `chord/chordanalyzer.cpp` | 1501 | **SINGLE** (large-but-cohesive residual oracle) | — Refactor #1 clean |
| `chord/chordsymbolformatter.cpp` | 1054 | **SINGLE** (formatting) | — Refactor #1 clean |
| `chord/postscoringgates.cpp` | 586 | **SINGLE** (gate cascade) | — Refactor #1 clean |
| `chord/chordpostpasses.cpp` | 297 | **SINGLE** (pedal post-pass) | — Refactor #1 clean |
| `chord/chordvoicing.cpp` | 233 | **SINGLE** (voicing) | — Refactor #1 clean |
| `chord/chorddiagnose.cpp` | 188 | **SINGLE** (diagnostic replay) | — Refactor #1 clean |

---

## §2 — Per-conflated-TU breakdown (responsibilities + seams)

### 2.1 `engravingbridge/regiontonecollector.cpp` (891) — CONFLATED, **highest pure yield**

**Responsibilities (5 distinct jobs sharing only the hand-copied engraving-traversal idiom):**
1. Raw sounding-note collection — `collectSoundingAt` (L46–96)
2. Pure tone construction / bass marking — `buildTones` (L98–119, the only engraving-free fn)
3. Region tone aggregation + weighting + pedal modeling — `collectRegionTones` (L200–575, 376 lines)
4. Key/mode pitch-context (a *different* weighting model: time-decay + lookahead) — `collectPitchContext` (L121–198)
5. Sub-boundary detection (two independent detectors) — `detectOnsetSubBoundaries` (L577–666), `detectBassMovementSubBoundaries` (L668–747)
6. Temporal-context via chord scoring (the only fn that *runs the analyzer*) — `findTemporalContext` (L749–889)

**PURE-BYTE-IDENTICAL seams (whole free functions, no file-scope statics, no shared mutable state):**
- `buildTones` (L98–119)
- `collectSoundingAt` (L46–96)
- `collectPitchContext` (L121–198)
- `detectOnsetSubBoundaries` + `detectBassMovementSubBoundaries` (L577–747) → a `subboundaries` TU
- `findTemporalContext` (L749–889) → a temporal/scoring-context TU (file-move pure; provided `buildTones`/`collectSoundingAt` move with it or stay visible)

**BEHAVIOR-ENTANGLED (deferred):** the internals of `collectRegionTones` — the pedal-tail sub-model
(L251–302, L497–522), the boost/normalize/bass-select post-passes (L470–548), and the 9× repeated
traversal idiom (L73–95, L164–187, L322–365, …) — all operate on in-function `accum[12]`/`voiceCount[12]`
locals; separating them requires promoting those accumulators to a passed struct (signature/state change).

> **Why top yield:** one pure split converts a 5-concern grab-bag into ~5 single-responsibility TUs +
> 1 residual god-function (`collectRegionTones`). After the split the residual is auditable in isolation.

### 2.2 `harmony/harmonicsegmenter.cpp` (943) — CONFLATED

**Responsibilities:** boundary/change-tick detection; engraving staff-participation counting; texture-adaptive
threshold math; chord-scoring orchestration (the `analyzeChord→pedal→gates` idiom, repeated 5×); region
promotion policy; gap-synthesis safety nets; enum→string formatting.

**PURE-BYTE-IDENTICAL seams:**
- `qualityToString` (L63–76)
- `isOnBeat` (L81–88) + `countParticipatingStaves` (L93–143) → traversal-primitives TU
- `collectNoteChangeTicks` (L151–315, ~164 lines — the substantial boundary detector)
- `fillGap` (L323–561) is a **file-move pure** (already a standalone 16-param fn, no shared statics) but a
  *layer*-separation of it needs `qualityToString` + the scoring idiom extracted first.

**BEHAVIOR-ENTANGLED (deferred):** all inline in the 362-line `greedyExpandSegmentation` god-function
(L565–927) — the threshold-derivation block (L583–664 → locals consumed downstream), the 5×-repeated
scoring idiom (L381/L728/L807/L899…), and the head/tail synthesis + tonic-prior tail (L789–924).

### 2.3 `key/keymodeanalyzer.cpp` (942) — CONFLATED, **8 concerns**

**Responsibilities:** static music-theory data (`MODES`, `CHARACTERISTIC`, name tables); keysig↔pc arithmetic;
the 6-function scoring-component library + `noteWeight`; a **second, independent** tonal-centre/relative-pair
scoring system (header L277–279 documents it as deliberately separate); declared-mode hint policy; the
293-line `analyzeKeyMode` orchestration/selection/ranking/confidence core; diagnostic emission; display
formatting (107 lines of string tables).

**PURE-BYTE-IDENTICAL seams:**
- **Display formatting** — `keyModeTonicName` + `keyModeSuffix` (L834–940). *Cleanest single win* — zero
  scoring dependency, self-contained `static constexpr` tables.
- **Tonal-centre / relative-pair scoring** — `tonalCenterScore` + `applyPairwiseDisambiguation` (L429–488).
- **Mode data + arithmetic** (`MODES`/`CHARACTERISTIC`/`possibleIonianFifthsForPc`/`resolveToFifths`/
  `keySignatureFifthsForKey`, L37–116, L125–196, L519–528) and the **scoring-component library** (L228–420)
  are pure-movable **with one caveat**: the scorers read `MODES`/`CHARACTERISTIC` *by name from the anonymous
  namespace*, so the data must promote to a **shared header** (or named namespace) — byte-identical behavior,
  but not a literal verbatim cut/paste. `scoreTriadEvidence` also has an explicit `evidenceOut` out-param
  (still pure-movable, co-owns the `TriadEvidence` struct).

**BEHAVIOR-ENTANGLED (deferred):** the `analyzeKeyMode` spine (L553–766) — order-dependent (raw eval →
`applyPairwiseDisambiguation` mutates scores in place at L620 → selection reads mutated scores at L633 →
ranking re-reads at L705); and the diagnostic dump (L768–819) which *recomputes* 3 per-candidate terms not
stored on the struct.

### 2.4 `section/sectionanalyzer.cpp` (971) — CONFLATED

**Responsibilities (header L25 names three; body holds more):** region type conversion; gap-tone/sparse-chord
inference (5 lambdas); gap-fill orchestration + carry-forward fallback; chord-analyzer invocation for gaps;
measure-aligned layout/split/merge; Pass-4 key/mode stabilization; functional re-derivation (in *two* places);
cadence detection; pivot-chord detection + Roman-numeral formatting; KeyArea confidence-gated grouping.

**PURE-BYTE-IDENTICAL seams:**
- **Cadence + pivot detection** — `detectCadences` (L165–248) + `detectPivotChords` (L250–363) +
  `hasAssertiveKeyConfidence` (L159–163). *Entirely independent* free functions (take `const
  vector<AnalyzedRegion>&`, return marker vectors); no mutable state crosses into `analyzeSection`. ~200 lines,
  **no shared-header caveat** — the cleanest fully-independent lift in this file.
- **Pass-4 stabilization** — `stabilizeHarmonicRegionsForDisplay` + `distinctPitchClassCount` (L65–153).
  (Minor: `distinctPitchClassCount` is also used at L901, so it stays shared or is duplicated.)

**BEHAVIOR-ENTANGLED (deferred):** the ~350-line gap-inference lambda cluster inside `analyzeSection`
(L423–777) — C++ lambdas closing over `chordAnalyzer`/`sc`/`excludeStaves`/`chordPrefs`/`regions`;
extraction needs capture→parameter conversion (a signature/state change).

### 2.5 `key/keyresolver.cpp` (361) — CONFLATED (mild)

The resolver spine (signature read → window/lookahead → fallback → hysteresis) is a coherent single job. The
one genuinely separable concern is **`partialSignatureCorrection`** (L107–190, + `ionianScaleSet` L71–79):
an 84-line DOM-walking Baroque-specific histogram heuristic that is the only place reaching deep into the
engraving DOM and is unrelated to the windowing/decision spine.

**PURE-BYTE-IDENTICAL seams:** `partialSignatureCorrection` + `ionianScaleSet` (explicit params in, returns a
corrected fifths; feeds only `keyFifths` at the call site L261); also the trivially-relocatable
`promoteWinnerInPlace` (L194–202) and `fallbackResult` (L55–68).
**BEHAVIOR-ENTANGLED (deferred):** the resolver spine itself (`keyFifths` mutated before the loop reads it;
`results`/`ctx` thread through loop→fallback→hysteresis) — the legitimate single responsibility, leave whole.

### 2.6 `region/regionanalyzer.cpp` (1167) — CONFLATED (largest file; **periphery-only pure yield**)

**Responsibilities:** segmentation/boundary detection; per-region scoring drive loop; post-hoc region
smoothing/merging; chord-symbol labeling backfill; joint-key resolution; debug capture. The body is one
~717-line orchestrator `analyzeRegions` (L448–1165) that *contains* the entire multi-pass pipeline, and the
source itself flags a **triplicated** per-region analysis body across Pass-1/2/2b as deliberately un-extracted
("DUPLICATED region-collapse logic — keep in sync", L692–697, L907–910).

**PURE-BYTE-IDENTICAL seams (all small, peripheral free functions):**
- Region smoothing — `coalesceShortSameRootRuns` (L73–152) + `absorbShortRegions` (L162–179)
- Label backfill — `backfillNextRootPc` (L184–191) + `restampBassMinorSeventhAfterMerge` (L205–231)
- Dense-boundary detector — `denseBoundaryTicks` (L236–274)
- **J-key wiring** — `applyJointKeyWiring` (L317–444) + `jkdPhraseBoundaryTicks` (L280–295) — see §4

**BEHAVIOR-ENTANGLED (deferred — this is the file's *real* tangle):** the triplicated Pass-1 (`runPass1`
lambda L547–722) / Pass-2 (L730–936) / Pass-2b (L938–1127) bodies, which read/mutate orchestrator locals
(`pass2Regions`/`pass2bRegions` back()-collapse accumulators, live `subCtx`/`subDecoder`, parent-scope
plumbing, the `anyNewSplit` while-flag) and hand off via sequential `regions = std::move(...)`. The source
annotates the duplication as intentionally not extracted because the branches build different
`HarmonicRegion` shapes (L695–697, L908–910).

> **Why ranked low as a *pure-split* candidate:** the largest file's worst tangle is the part that does **not**
> move byte-identically. A pure split here cleans the edges but leaves the god-function intact — modest
> audit-unblocking per unit of churn.

---

## §3 — Single-responsibility / audit-ready TUs (no split needed)

| TU | Lines | The one job (cite) |
|---|---|---|
| `function/harmonicfunctionlayer.cpp` | 567 | Harmonic-function competition layer; `applyHarmonicFunction` is the sole entry (L345) and every helper (Gate R L165–230, progression scalars L38–95, migrated oracle signals L104–163) feeds it. Cohesive layer + co-located private helpers — *not* conflation. |
| `section/jointkeydecision.cpp` | 422 | Constrained-joint key decision; `decideJointKey` (L170–420) is a pure fn, helpers (L38–143) serve only it. One orphan: the env-seeded wiring flag (L160–168) — see §3a. |
| `section/localmodulationdetector.cpp` | 311 | Local-modulation span detection; `detectLocalModulations` (L135–309), private helpers L71–131. |
| `section/cadencekeyanchor.cpp` | 232 | Authentic-cadence detect → global anchor aggregate; cohesive pair (L61–123, L147–230). |
| `region/sparsechordrefinement.cpp` | 220 | Key-context diatonic quality refinement for sparse chords (4 refiners + 3 helpers). |
| `function/tonicizationlabeler.cpp` | 203 | Applied/tonicization labeling; `labelTonicizations` (L88–201) + 4 detail helpers. |
| `key/modepriorpresets.cpp` | 156 | Pure mode-prior preset data table (one function returning 5 literal structs). |
| `chord/*` (6 TUs) | 1501/1054/586/297/233/188 | Refactor #1 landed clean — oracle / formatter / gates / pedal-pass / voicing / diagnose, each single-responsibility (`chordanalyzer.cpp` is large-but-cohesive: the migrated temporal signals already left for `harmonicfunctionlayer.cpp`, Stage 3.3). |

**§3a — one orphan seam:** the joint-key **wiring flag** (`g_jkdWiringEnabled` + `setJointKeyWiringEnabled` +
`jointKeyWiringEnabled`, jointkeydecision.cpp L160–168) is process-global mutable state consumed by *three*
TUs (sectionanalyzer L94, localmodulationdetector L298, regionanalyzer L1150). It is orthogonal to the
decision math and `decideJointKey` never reads it. **Pure-byte-identical** to relocate to its own flag TU —
a tidy-up, not an audit blocker.

---

## §4 — The joint-decision 2-pass bolt-on (§2.3 of the brief) — SOURCE-VERIFIED

**Question:** is `applyJointKeyWiring` + `decideJointKey` a clean layer, or a bolt-on smeared into
`analyzeRegions`?

**Verdict: CLEANLY LAYERED — not a smear.** Verified by direct read of
`regionanalyzer.cpp:297-444` and `:1133-1165`:

1. **The wiring is one self-contained call behind a gate, at the tail of `analyzeRegions`** (L1150–1153):
   ```cpp
   if (analysis::jointKeyWiringEnabled()) {
       applyJointKeyWiring(score, regions, refStaff, excludeStaves, keyPrefs);
       backfillNextRootPc(regions);
   }
   ```
   It runs *after* all passes (Pass-3 smoothing L1135, restamp/backfill L1140–1143) and touches the
   Pass-1/2/2b loops **not at all**.
2. **`applyJointKeyWiring` re-derives everything from scratch** — its own `prevKey` accumulator and
   re-resolution loop (L355–407); it explicitly does *not* reuse Pass-1's `prevKeyResult`. Header documents
   the re-computation as "IDENTICAL to the batch_analyze --dump-joint-key construction" (L302–304).
3. **Fully explicit signature** (L317–321): `score, regions&, refStaff, excludeStaves, keyPrefs` — no closure
   capture. Every call-site argument is already an `analyzeRegions` param/local.
4. **Key-axis-local side effect only** — overwrites `region.keyModeResult` (L441), leaves chord = production
   R0 by design (L442, L309–316). The lone coupling is the ordinary `backfillNextRootPc` re-call (L1152).
5. **`decideJointKey` is a pure function** — `JointKeyResult decideJointKey(const vector<JointKeyRegionInput>&,
   int keySignatureFifths, const JointKeyWeights&)` (jointkeydecision.cpp L170). No `AnalyzedRegion`/section
   symbol; reads `prodTonicPc`/`prodIsMajor` only to *echo* them (L388–389 / regionanalyzer L401 "ECHO only
   (never read by the decision)"). All production write-back is isolated in the caller (regionanalyzer
   L416–443), not in the decision.

**Byte-identity of restructuring it:** **PURE — byte-identical.** Moving `applyJointKeyWiring` +
`jkdPhraseBoundaryTicks` (its only caller is internal, L348) into a `regionjointkeywiring.cpp` is verbatim
movement: nothing captured, all dependencies already `#include`d, the gate check + `backfillNextRootPc`
re-call stay in `analyzeRegions`, the function-local `kJointModulationFallbackConfidence` travels with it.

**But low priority:** because it is *already* a clean, self-contained, gated, DORMANT (flag OFF) layer, the
extraction is cosmetic — it does not unblock any audit. File it as a tidy-up, behind the conflated-TU splits.

---

## §5 — Prioritized **pure-byte-identical** split candidates (worst-tangle-first)

Ranking criterion = **(audit-blocking severity of the conflation) × (auditable surface a pure split isolates)**.
i.e. "which next byte-identical split most unblocks a meaningful layer-by-layer audit," the same logic that
made Refactor #1 isolate the gate layer.

| # | TU | Pure seams to extract | Residual after split | Yield |
|---|---|---|---|---|
| **1** | `regiontonecollector.cpp` | `collectSoundingAt`, `buildTones`, `collectPitchContext`, the 2 sub-boundary detectors, `findTemporalContext` (5 whole fns → ~4 named TUs: sounding-primitives, key-mode-context, sub-boundaries, temporal-context) | `collectRegionTones` (376-line accumulator) alone, auditable in isolation | **Highest** — 5-concern grab-bag → single-responsibility TUs in one pure move, no caveat |
| **2** | `sectionanalyzer.cpp` | cadence + pivot detection (L159–363, fully independent, no caveat) → cadence/pivot TU; Pass-4 stabilization (L65–153) → stabilization TU | the gap-inference + measure-layout core (auditable as the residual) | High — two clean independent layers isolated |
| **3** | `harmonicsegmenter.cpp` | `collectNoteChangeTicks` (164-line boundary detector), `isOnBeat`+`countParticipatingStaves`, `qualityToString`; `fillGap` as a file-move | `greedyExpandSegmentation` policy god-function | High — isolates the boundary-detection layer from segmentation policy |
| **4** | `keymodeanalyzer.cpp` | display formatting (L834–940, clean) → key-display TU; tonal-centre scoring (L429–488); **(caveat)** mode-data + scorer library need data promoted to a shared header | `analyzeKeyMode` scoring/selection spine, exposed for audit | Moderate — display is a clean win; data/scorer seams carry the shared-header caveat |
| **5** | `regionanalyzer.cpp` | smoothing, label-backfill, dense-boundary, **J-key wiring** (all small peripheral free fns) | `analyzeRegions` + triplicated Pass-1/2/2b bodies (still entangled) | Low — pure seams are peripheral; the real tangle is behavior-entangled (§6) |
| **6** | `keyresolver.cpp` | `partialSignatureCorrection`+`ionianScaleSet` (84-line DOM heuristic), `promoteWinnerInPlace`, `fallbackResult` | resolver spine (the legitimate single job) | Low — mild conflation; one meaningful seam |

---

## §6 — Behavior-entangled candidates (DEFERRED — NOT pure splits)

Under the no-inference-change rule these are **flagged, not planned**. Separating any of them changes shared
state, call order, or symbol sets ⇒ behavior-touching, not a byte-identical refactor:

- **regionanalyzer.cpp** — the triplicated Pass-1/2/2b region-analysis bodies (L547–722 / L730–936 /
  L938–1127) + the orchestration core. Source-flagged as deliberately un-extracted (L692–697, L907–910).
- **sectionanalyzer.cpp** — the gap-inference lambda cluster (L423–777, capture-entangled).
- **keymodeanalyzer.cpp** — the `analyzeKeyMode` spine (in-place score mutation at L620 sequenced into
  selection/ranking, L633/L705) + the recompute-on-the-fly diagnostic dump (L768–819).
- **harmonicsegmenter.cpp** — the `greedyExpandSegmentation` interior: threshold block (L583–664), the
  5×-repeated `analyzeChord→pedal→gates` idiom, head/tail synthesis (L789–924).
- **regiontonecollector.cpp** — `collectRegionTones` interior: pedal-tail sub-model, boost/normalize/
  bass-select post-passes, the 9× traversal idiom (promoting `accum[]`/`voiceCount[]` to a struct is a
  state-contract change).
- **keyresolver.cpp** — the resolver spine (sequential `keyFifths`/`results`/`ctx` threading).
- **Cross-TU shared-helper consolidations** (also deferred — change ODR strategy / symbol sets, not
  byte-identical): the `pcMod12`/collection-mask logic duplicated across `jkd*` (jointkeydecision L38–143),
  `lmd*` (localmodulationdetector L71–131), and the **unprefixed** `pcMod12` in cadencekeyanchor (L34 — a
  latent jumbo-build ODR fragility worth noting); the duplicated `ionianScaleSet` (keyresolver L71) vs.
  inline Ionian membership in `analyzeKeyMode` (keymodeanalyzer L545–551) vs. `ionianTonicPcFromFifths`
  (analysisutils.h). These are genuine de-duplication wins but are **refactors, not pure moves.**

---

## §7 — Audit-readiness verdict

**Already separable-and-auditable now (audit can proceed as-is):**
- The **`function/` layer** — `harmonicfunctionlayer.cpp` (the competition/Gate-R layer) + `tonicizationlabeler.cpp`.
- The **`chord/` layer** — all 6 TUs (Refactor #1 landed clean; confirmed).
- The **key-decision unit** — `jointkeydecision.cpp` / `decideJointKey` is a pure, isolable decision layer.
- The **detectors** — `localmodulationdetector.cpp`, `cadencekeyanchor.cpp`.
- The **data/refinement leaves** — `modepriorpresets.cpp`, `sparsechordrefinement.cpp`.

**Splits that should PRECEDE a meaningful layer-by-layer audit** (the conflation currently forces an
"audit the whole god-function" posture):
- **Engraving bridge** (`regiontonecollector.cpp`) — split the 5 free functions out first to expose
  `collectRegionTones` as an auditable unit. *(Best next split — highest yield, no caveat.)*
- **Section layer** (`sectionanalyzer.cpp`) — split cadence/pivot + Pass-4 stabilization out first, leaving
  the gap-inference core as the residual audit target.
- **Harmony segmentation** (`harmonicsegmenter.cpp`) — split boundary primitives out to expose the
  `greedyExpandSegmentation` policy.
- **Key inference** (`keymodeanalyzer.cpp`) — split display + (with the shared-header caveat) mode-data/
  scorer library out to expose the scoring/selection spine.

**Audit-blocked at the core regardless of pure splits** (their worst tangle is behavior-entangled — a pure
split cleans the periphery but the core must be audited whole, or deferred to a behavior-change refactor):
- **Region orchestration** (`regionanalyzer.cpp`) — the triplicated multi-pass core.

---

## §8 — Recommendation framing (surface, do not build)

This dossier is the **spec for the next refactor decision**, not a build order. The measured map says:

- **If the goal is "one more Refactor-#1-shaped byte-identical split that unblocks the most audit surface"** →
  the candidate is **`regiontonecollector.cpp`** (§5 #1): 5 whole free functions lift out clean, no caveat,
  and the residual `collectRegionTones` becomes independently auditable.
- **If the goal is "begin the layer-by-layer audit now"** → the **`function/` and `chord/` layers, plus
  `jointkeydecision`/`localmodulationdetector`/`cadencekeyanchor`** are audit-ready today (§7).
- **The joint-decision wiring needs no structural work to be auditable** (§4) — it is already a clean,
  gated, dormant layer; any extraction is cosmetic tidy-up, behind the conflated-TU splits.
- **The largest file is not the top split target** — `regionanalyzer.cpp`'s deepest tangle is
  behavior-entangled and out of scope under the no-inference-change rule.

**No code recommended written.** Direction call (more splits in the §5 order vs. start the §7 audit) is
Cowork's / the user's.
