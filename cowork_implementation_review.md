# Implementation Review — Composing Module (As-Built)

*Cowork, 2026-06-10. Part 2 of the architecture review (part 1: `cowork_target_architecture_review.md`).*
*Method: four parallel read-only code audits (path unification, layering, maintainability/dead code,
test coverage) + direct spot-checks by Cowork. Claims verified directly by Cowork are marked ✓;
agent-reported findings I did not independently re-verify are marked (agent). HEAD `e7d4ba2b1a`.*

---

## Q1 — One single path, total unification?

**Verdict: YES at the chord-analysis core. NO at the section level — and the gap is consequential.**

### What is genuinely unified ✓

The core pipeline is one path. All three commit sites in `regionanalyzer.cpp` (Pass 1 :446,
Pass 2 :655, Pass 2b :847) issue the identical sequence: `analyzeChord` →
(internal) `fn::applyHarmonicFunction` → `applyIter8691Pedal` + `applyPostScoringGates` →
`advanceTemporalContext` (:473, :689, :882). `applyHarmonicFunction` is unconditionally
called inside `analyzeChord` (chordanalyzer.cpp:2968) — no production caller can skip it.
The notation bridge (`notationharmonicrhythmbridge.cpp:69–134`) and batch
(`batch_analyze.cpp:518`) are both thin wrappers over `region::analyzeRegions()`. The two
months of E2d/Step-5 work delivered what they claimed.

### Where unification ends — ranked by impact

**1. The batch path and the user-facing paths diverge ABOVE `analyzeRegions` ✓ (most important
finding of this review).** The real user-facing entry is `analyzeSection()` — which lives in
`src/notation/internal/notationcomposingbridgehelpers.cpp:583`, not in the composing module.
P1 (implode, `notationimplodebridge.cpp:1373`), P2/P3 (`notationcomposingbridge.cpp:244,
:1117`), and the pipeline snapshot tests all consume `analyzeSection`, which applies on top of
`analyzeRegions`: `stabilizeHarmonicRegionsForDisplay` (key smoothing, helpers :145, applied
:1129), sparse-chord key-context refinement wrappers, cadence detection (`detectCadences`
:377), and pivot detection (`detectPivotChords` :462). `batch_analyze.cpp:518` calls
`analyzeRegions` directly and gets **none** of this.

Consequence: **the corpus metrics (BIR, rn_agree, the 13/7 hard stops) are measured on a
pipeline that is not the one users see.** Any future change to `stabilizeHarmonicRegionsForDisplay`
or the section-level refinements is invisible to the BIR guardrails. This is the same class of
bug as the old batch/bridge divergence that took Iter 97 + D2 to close, one level up.

**2. P4 (tick-local) is parallel by design — but more parallel than advertised (agent, spot-confirmed).**
P4 (`notationcomposingbridge.cpp:393–460`) shares `analyzeChord` + both gate passes, but builds
its temporal context cold via `findTemporalContext` (no accumulated rolling state:
`consecutiveBassStepwiseCount` effectively reset, `recentRootPcs` re-derived) and its tones via
single-tick `buildTones` (no `durationInRegion` / `onsetAtRegionStart` / metric-position
evidence → `jointScoringEnabled` differs). The same chord at the same tick can legitimately get
a different answer on P4 than P3. Known (the C1 schumann case depends on it), but the
divergence is broader than the "P4 stays parallel" note suggests.

**3. Bridge cold-context vs batch chained-context (documented, still open).**
`findTemporalContext` analyzes the predecessor with `nullptr` context (and Step-1/2 confidence
fields unset) — the batch path has the full temporal chain. The forward walk was added
(`90a52b5fee`), but the backward predecessor is still cold. Bridge and batch are unified as
*wrappers*; the *context quality* they feed the shared pipeline is not equal.

**4. `diagnoseChord` violates the project's own principle #2 ✓.** "diagnoseChord must be a view
into the production pipeline, not a separate scorer" (COWORK_HANDOFF architecture direction).
It is a separate scorer: skips `applyHarmonicFunction` entirely (no rcb/wSeq/wDim/step/Gate R),
single-bass path, no threshold/cap (chordanalyzer.cpp:3164–3330). This has already caused two
documented mis-diagnoses (bwv320 retraction, bwv14.5 mischaracterisation). It is the analysis
tool most likely to mislead the next investigation.

**5. Minor / intentional ✓:** `excludeLookAheadOnDenseStart` divergence (batch=true,
bridge=false) — documented, load-bearing, fine. `onsetBoundaryThreshold` hard-coded 0.25 in
batch vs user-config in bridge (agent). Same-root region-collapse logic appears twice in
`regionanalyzer.cpp` (:497–505, :694–698) (agent).

---

## Q2 — Proper architectural layers, one purpose each, correct dependencies?

**Verdict: the composing-module core is properly layered (E2d is real). The biggest layering
problem is not inside the composing module — it is that a whole analysis layer lives in the
notation module.**

### Correct ✓
- key/ (keymodeanalyzer, keyresolver, modepriorpresets), region/ (regionanalyzer,
  sparsechordrefinement), chord/ (oracle), function/ (competition pipeline), engravingbridge/
  (tone collection) are clean modules with single purposes; no include cycles — the
  harmonicfunctionlayer.h → chordanalyzer.h direction with forward-declared `function`
  namespace is pragmatic and well documented (chordanalyzer.h:37–56).
- The function layer is pure: stateless bonus functions post-ScoringPhase refactor; touches
  only its inputs (agent, consistent with yesterday's verified refactor).
- Sparse refinement is correctly in composing and called at all three commit sites
  (regionanalyzer.cpp:462–464, :680, :873) ✓; the notation-side functions of the same name are
  thin wrappers (helpers :118–133) ✓.

### Violations / misplacements

1. **Analysis logic in `src/notation` ✓ — the misplaced layer.** Cadence detection, pivot-chord
   detection, display key-stabilization, degree computation (`diatonicDegreeForRootPc`),
   key-resolution orchestration (`resolveKeyAndMode`), and the unified `analyzeSection` entry
   all live in `notationcomposingbridgehelpers.cpp` (1180 lines). The Dependency Rule (§3.3)
   says notation is a thin bridge; `composing/CMakeLists.txt:41` itself records the deferred
   Phase 4c move. This matters *now*, not later: Phase E/E4 (cadence confirmation, functional
   labels) is planned as a composing-module function layer, but the only existing cadence
   implementation — with its tests — is in notation. Without the Phase 4c move first, Phase E
   will either duplicate it (violating principle 2) or grow the wrong module.
2. **Five temporal signals in the oracle** (chordanalyzer.h:329 TODO) — documented debt;
   confirmed still present. Gate R's `basisDep ≤ 0` proxy depends on it (documented).
3. **Post-scoring gates A–L are functional reasoning located in `chordanalyzer.cpp`**, not in
   the function layer — E3 extracted them into a function but not into the layer; temporal
   gates can't move cleanly past `applyIter8691Pedal` ordering (documented). Audit Finding 7
   stands: two-thirds of this code compensates one oracle bias.
4. **Quality-from-key feedback is scattered**: sparse refinement (composing, 3 sites) +
   `forceChordTrackQualityFromKeyContext` + display stabilization (notation). Three places
   second-guess chord quality from key context at different pipeline stages — functionally one
   concern, three homes.
5. `applyIter8691Pedal` is its own mini-layer (bass-b7 stamping, bass-as-root promotion, pedal
   two-pass) wedged between competition and gates — purposeful but unnamed as a layer; its
   ordering constraint blocks gate migration (documented in E3 notes).

Dependency direction is otherwise correct: key ← chord ← function flows, region orchestrates,
nothing in composing includes notation ✓ (the reverse holds).

---

## Q3 — Maintainability, structure, documentation, MuseScore standards?

**Verdict: locally excellent, globally heavy.** (Mostly agent findings; spot-checked samples.)

Conformant ✓ (agent): GPL-3.0 + CLA license headers on all composing files; camelCase;
MuseScore brace/include conventions; struct-based data types without `m_` (consistent with
upstream); scoring constants k-prefixed with `[empirical]`/`[theory-grounded]` annotations —
very few raw magic numbers; rich why-comments tied to specific bugs and scores; only 5 TODOs,
all deliberate deferrals.

Counterweights:

1. **`chordanalyzer.cpp` is a 3,869-line multi-layer file**: oracle + score matrices +
   post-scoring gates + Iter 86/91/pedal + TPC spelling + extension detection + formatting
   support + `diagnoseChord`. `analyzeChord` ~500 lines, `applyPostScoringGates` ~400+,
   `applyIter8691Pedal` ~176. The audit's "don't split until Phase E" position is defensible,
   but this file is the module's bus-factor risk.
2. **The code is not readable without the doc corpus.** Comprehension depends on
   `scoring_model.md`, iteration history, and dead-end lore ("Iter 92", "B2 dual guard",
   "Sub-9a"). The sync rule keeps docs honest — genuinely good — but permanent API names like
   `applyIter8691Pedal` bake changelog vocabulary into the architecture. A future maintainer
   reads "apply iteration 86 and 91 and pedal" and learns nothing about *what it does*.
3. **Change-cost is the real maintainability metric, and it is high.** §8 of scoring_model.md
   lists 14 load-bearing constraints and 4 documented dead ends; 4 individually load-bearing
   guards protect one 0.10 bonus; template addition requires a 5-site atomic update where a
   miss is a *silent* stack-buffer overrun (sizes by literal — this is a code smell worth
   fixing with a shared `constexpr size_t kTemplateCount`, independent of any redesign).
4. Naming is internally consistent (basisIndep/basisDep, rcb, wSeq documented at their
   declaration sites) ✓.

---

## Q4 — Dead, stale, unreachable code?

**Verdict: remarkably little — the discipline shows.**

- `HarmonicFunctionContext.keyFifths` / `keyMode`: write-only, documented as dead at the write
  site (chordanalyzer.cpp:2935–44) ✓. The Step-3 cleanup ("remove or document") chose
  "document"; **recommend removal** — a documented corpse is still a corpse, and it misleads
  exactly when someone next wires key context into the function layer.
- No unused `ChordAnalyzerPreferences` fields, no orphaned functions, no stale
  explorationMode/suppressProgressionSignals remnants (agent — consistent with yesterday's
  grep showing only 2 intentional "former explorationMode" comments ✓).
- `pitchClassName` vs `pitchClassNameFromTpc`: complementary, not duplicates (agent; matches
  §4.1i which still flags consolidation as backlog).
- Repo hygiene (✓, from git status): untracked junk at root — `"s -ExecutionPolicy
  RemoteSigned..."` (mangled PowerShell artifact), `C:tmpbuild_out.txt` — should be deleted;
  `docs/layer_architecture_audit.md` is still untracked (a referenced architecture document
  not in git); `ai-assistant/` untracked files are a separate project bleeding into status
  output.

---

## Q5 — Missing regression tests?

**Verdict: the testing strategy is corpus-heavy and unit-light below the catalog level. The
gaps cluster exactly where the subtlest logic lives.**

Strong ✓: 416 composing tests (catalog ground truth + musicxml + keymode 985-line suite +
Gate R unit tests incl. yesterday's phase-gating test), 52 notation (incl. cadence/pivot tests
in `notationannotate_tests.cpp` ✓), 11 pipeline snapshots with golden JSONs, BIR hard-stops on
two presets, `analyzeWithGates()` exercising the real production call order (agent).

Gaps, ranked by risk (agent + audit doc, spot-consistent):

1. **Gates A–L: zero dedicated unit tests.** ~250+ lines of margin-threshold/enharmonic-swap
   logic (kGateIMargin 0.45, K 0.20, L 0.35, inversionSuspicionMargin 0.70) validated only by
   corpus aggregates and 11 snapshots. A sign-flip in one margin comparison could survive both.
2. **Function-layer bonuses untested individually**: wSeq, wDim, wStep In/Out,
   rootContinuityBonus, `applyStepBonusGuard` (with its 4 load-bearing guards) — only Gate R
   has unit tests. The §8 constraint list is exactly a unit-test spec that doesn't exist.
3. **`regionanalyzer` passes have no unit tests**: absorbShortRegions,
   coalesceShortSameRootRuns, Pass 2/2b boundary logic, the inline same-root merge. All
   segmentation regressions are currently detectable only at corpus level.
4. **`harmonicsegmenter` (943 lines) and `keyresolver` (promoteWinnerInPlace hysteresis,
   ranked output) — no unit tests** (agent).
5. **Fixed bugs not pinned**: Gate J (bwv110.7), Iter 92 joint-bass (bwv103.6, bwv310), Sub-9a
   capture, and the Δ=+7b trio (bwv245.28/296/320) — pinned in corpus/snapshot only, not as
   units. The audit doc recommended pinning the Δ=+7b cases; not done.
6. Snapshot corpus is 11 scores; P4/status-bar path has no snapshot coverage (agent).

Caveat: agent counted 377 tests vs the canonical 416 — counting-method discrepancy, the gap
analysis is unaffected.

---

## Q6 — Everything else a comprehensive review covers

- **Performance ✓(structure)/?(measurement):** P3 re-runs region analysis per status-bar query
  (P3 → `analyzeHarmonicRhythm` per tick query, falling back to P4); no caching layer is
  visible at the bridge. Whether this matters depends on selection size and call frequency —
  unmeasured, worth a profile before Phase E adds decode cost. The 12×17×bass scoring grid per
  region is small; no algorithmic red flags at region counts seen in corpora.
- **Numerical robustness:** winner selection rides on exact double comparisons; documented
  near-ties (1.92 vs 1.92, 0.02 margins) are resolved by `tiePriority` ordering — deterministic
  but *calibration-fragile*: any FP-reordering change (compiler flags, platform) could flip
  documented cases. No epsilon policy is stated anywhere. Worth one paragraph in
  scoring_model.md and, ideally, a tie-stability test.
- **Thread/state safety:** analysis is struct-in/struct-out with no visible global mutable
  state (agent); preferences passed by value/const-ref. No concerns found, none proven.
- **Error handling:** conservative fallbacks throughout (Gate R "out-of-range inputs return
  true (no gating)", sparse fallbacks, piece-start key shortcut) — consistent philosophy ✓.
- **Licensing/process ✓:** GPL headers everywhere; commit discipline, byte-identity
  verification culture, dead-end documentation are well above open-source norms. The muse
  submodule local patch is properly fenced in CLAUDE.md.
- **Tooling parity risk:** `tools/` Python comparators embed alignment/classification logic
  (lenient-OR, root/quality mapping) that constitutes the *de facto* metric definition — one
  classifier bug already produced a wrong conclusion for weeks (quality_err mislabeling,
  corrected 2026-06-04). The metric scripts have no tests at all.

---

## Overall verdict

The implementation is in better shape than most rule-based analysis codebases of this age:
the E2d/Step-5 unification is real, dead code is nearly absent, style is conformant, and the
documentation-sync culture is exceptional. The honest gaps, in priority order:

1. **`analyzeSection` and its section-level refinements live in the notation module and are
   outside the measured (batch/BIR) pipeline** — both a layering violation and a metric
   blind spot. Phase 4c (move to composing) + a batch flag to run the same section-level pass
   would close it, and it is a *prerequisite* for Phase E touching cadences.
2. **diagnoseChord is a second scorer** that has already misled investigations twice — either
   make it replay the production pipeline or label its output as oracle-only in every dump.
3. **Unit-test the constraint list**: gates A–L, function-layer bonuses, segmentation passes,
   and pin the fixed-bug cases. The §8 dead-end list is a ready-made test spec.
4. **Small hardening**: shared `kTemplateCount` constant (kills the silent-overrun class),
   remove the dead fnCtx fields, delete root junk files, commit
   `layer_architecture_audit.md`, document an FP tie policy.
5. All of this is compatible with — and mostly prerequisite to — the part-1 recommendation
   (lattice decode as the Phase E target). Notably, the decoder migration *reduces* the Q5
   surface: gates A–L and the bonus-guard stack are the hardest things to test, and they are
   exactly what a decoder subsumes.
