# CC Stage 1c Report — Pin segmentation passes, harmonicsegmenter, keyresolver

**Date:** 2026-06-10 · **Roadmap items:** 1.3 (segmentation-pass tests) + 1.4
(harmonicsegmenter + keyresolver tests)
**Deliverable:** `src/composing/tests/regionanalysis_tests.cpp` (new) +
CMakeLists registration + composing-test `environment.cpp` upgrade + 9 minimal
`.mscx` fixtures. **Production code untouched** — tests only. No BIR run needed
or performed (production binary byte-identical by construction).

All three suites green: **composing 487 → 498/498 (+11)** · **notation 52/52** ·
**pipeline snapshots 11/11** (+1 standard `GenerateReport` skip; zero diffs, no
goldens touched).

---

## 0. Infrastructure deviation (read first)

Stage 1a/1b pinned pure-tone functions by direct construction. **Every Stage 1c
target needs a real `mu::engraving::Score`:** `analyzeRegions`,
`greedyExpandSegmentation`, and `resolveKeyAndModeRanked` all consume a `Score`,
and the merge/segmenter/promote helpers under test (`absorbShortRegions`,
`coalesceShortSameRootRuns`, `fillGap`, `promoteWinnerInPlace`,
`partialSignatureCorrection`) are **file-local** (anonymous namespace) — only
reachable through those public, Score-consuming entries. Per the instruction's
"do NOT re-expose file-local functions; test through the public caller," every
pin drives the public entry over a fixture.

The instruction said "generate MINIMAL musicxml fixtures." **This was adjusted to
`.mscx`**, because:
- `composing_tests` links `composing_analysis intonation engraving` — **not**
  `importexport`. MusicXML import lives in `importexport`; pulling it in is a
  heavyweight module dependency. `.mscx` loads via `compat::loadMsczOrMscx`,
  which is in the already-linked `engraving` module (the exact path
  `engraving_tests` uses — it links only `engraving` and loads `.mscx`).
- The existing `src/composing/tests/data/*.musicxml` files are parsed by hand
  with `QXmlStreamReader` into tone vectors — they are **never loaded as a
  Score**. So the "src/composing/tests convention" the instruction cited is the
  XML-scrape convention, which does not reach a `Score`.

To make `composing_tests` load `.mscx`, the test binary's `environment.cpp` was
upgraded to a faithful copy of `engraving/tests/environment.cpp`: it registers
`DrawModule` + `EngravingModule`, sets `MScore::testMode/noGui`, loads instrument
templates, and registers a `NiceMock<EngravingConfigurationMock>`. The engraving
`ScoreRW` utility + the config mock are added to the test sources. **All of this
is test-only build/harness code — zero production change.** The 487 pre-existing
pure-tone tests are unaffected by the extra module init (verified: 498/498, the
+11 being this run's additions).

`.mscx` fixtures are hand-authored, minimal (1.6–3.0 KB each), and modeled on the
existing `notationtuning_data/bass_movement_boundary.mscx` (itself a minimal
composing-analysis fixture). Note: pitch class drives chord identity, so `<tpc>`
values are spelled correctly but are not load-bearing for these pins.

---

## 1. Survey inventories (Stage-3/4 design feed)

### 1.1 Segmentation passes — `regionanalyzer.cpp` (pass order + semantics)

`analyzeRegions` orchestration (public entry; all helpers below are file-local in
the anonymous namespace unless noted):

```
Pass 1 (runPass1 lambda, retried under sparse admission)
  per coarse greedy-expand boundary region:
    collectRegionTones → analyzeChord → applyIter8691Pedal → applyPostScoringGates
    → refineSparseChordQualityFromKeyContext → applyTonicPriorToSparseChord
    → advanceTemporalContext
    → INLINE same-root merge: contiguous && rootPc==prev && quality==prev
                              → extend endTick, mergeChordAnalysisTones, recompute bass
  (preMergeRegions hook captures THIS stream)
Pass 2  — onset-Jaccard sub-boundaries; parents ≥ kPass2MinRegionTicks (1920t);
          sub-regions committed with bassIsStepwiseToNext = FALSE (L621);
          same inline same-root/quality collapse on the sub-stream (L704)
Pass 2b — iterative bass-movement sub-boundaries; while anyNewSplit &&
          passCount < kMaxBassMovementPasses (8); parents ≥ kPass2bMinRegionTicks
          (1920t); sub-regions also forced bassIsStepwiseToNext = FALSE (L823)
Pass 3 (Smoothed granularity only):
  coalesceShortSameRootRuns — runs FIRST; merges a run of ≥3 consecutive
      contiguous same-root sub-regions (each < kMinRegionTicks=480, total ≥720t)
      into one inheriting the LONGEST sub-region's identity; SKIPPED when the
      predecessor already shares the run's root (absorb handles that)
  absorbShortRegions — ROOT-AGNOSTIC; every region < kMinRegionTicks (480t)
      absorbed into its predecessor by extending the predecessor's endTick;
      first region (no predecessor) never absorbed
restampBassMinorSeventhAfterMerge — Iter 87 post-merge b7 bass promotion
backfillNextRootPc — fills function.nextRootPc from the next region's root
```

Public surface for observation: `AnalyzeRegionsOptions::hooks`
(`preMergeRegions` = Pass-1 stream; `postMergeRegions` = final stream) and the
returned vector. Pre-absorb/post-2b intermediate stream is **not** exposed.

### 1.2 harmonicsegmenter — `harmonicsegmenter.cpp`

`greedyExpandSegmentation` (public): emits all note-change ticks (onset OR
release, Pardo-Birmingham) as round-0 candidates; **Round 1** promotes candidates
clearing four texture-adaptive gates (beat-aligned, duration ≥
`effectiveAnchorMinDurationTicks`, ≥ `effectiveStaveThreshold` participating
staves, analyzeChord score ≥ `effectiveAnchorMinScore`); **Round 2** = `fillGap`
(file-local) over each inter-anchor gap; then head-gap and tail-gap synthesis
safety nets. `fillGap` scores each round-0 candidate twice (bilateral-context
`initCtx` + true-local), promotes the distinct ones ≥ `effectiveRound2MinScore`,
then re-scores promoted candidates with updated neighbours (with a long-gap
local-evidence preference). **Segmentation phase:** every internal exploration
`analyzeChord` runs with `prefs.scoringPhase == ScoringPhase::Segmentation`
(`sparsePrefs` at L706 for Round 1; `explorePrefs` at L347 inside `fillGap`), so
progression signals (voice-leading step bonuses, w_seq/w_dim, Gate R) are
suppressed until the final per-region pass.

### 1.3 keyresolver — `keyresolver.cpp`

`resolveKeyAndModeRanked` (public): reads the key-signature event → `keyFifths` +
declared mode; **`partialSignatureCorrection`** (file-local) may reinterpret the
signature one step toward the declared mode's missing accidental (minor −1 flat /
major +1 sharp) when the accidental is pervasive (≥3% of sounding weight) AND
dominates its natural counterpart (≥2×); **piece-start shortcut** (no prior +
declared mode + `tick < lookbackDuration`, where `lookbackDuration =
LOOKBACK_BEATS/4 = 16` quarters = 7680t) returns the declared anchor at
confidence 0.5, score = `relativeKeyHysteresisMargin`, single element; otherwise
the dynamic-lookahead loop runs `analyzeKeyMode`; **insufficient-data fallback**
(`results.empty() || distinctPitchClasses(ctx) < 3`) → `fallbackResult` at
confidence 0.0; **hysteresis** and **strong declared-mode prior** both call
`promoteWinnerInPlace` (file-local), which `std::rotate`s the chosen candidate to
front **without recomputing `normalizedConfidence`**.

Confidence assignment (`keymodeanalyzer.cpp` L738–746): each candidate gets its
OWN local-gap sigmoid confidence (rank 0 from the top-1/top-2 gap; rank i from
the i/i+1 gap). So a rotated runner-up keeps the confidence of its **original**
rank — the wart pinned in 4.2.

---

## 2. Test inventory (test → behaviour pinned)

All in `regionanalysis_tests.cpp`. 11 tests, 3 suites.

| Test | Pins |
|------|------|
| `Composing_KeyresolverTests.PieceStartShortcut_DeclaredMinor` | 4.4 piece-start, declared minor → Aeolian/C, fifths −3, conf 0.5, score = relativeKeyHysteresisMargin, size 1 |
| `…PieceStartShortcut_DeclaredMajor` | 4.4 piece-start, declared major → Ionian/C, conf 0.5, size 1 |
| `…InsufficientPitchClasses_FallbackConfidenceZero` | 4.4 fallback: <3 distinct PCs (unison, no keysig → shortcut skipped) → conf 0.0, score 0.0, size 1 |
| `…RankedOutput_FrontIsRankZeroAndScoreOrdered` | 4.1 `.front()`==[0]; score-ordered when no promotion fires |
| `…PartialSignature_CMinorUnderTwoFlats_Corrected` | 4.3 (`81978321e3`) C-minor under −2 + pervasive A♭ → corrected −3, tonic C(0), Aeolian |
| `…PartialSignature_GMinorUnderTwoFlats_NotCorrected` | 4.3 counter-case: real G-minor under −2 (no A♭) → uncorrected −2, tonic G(7) |
| `…PromoteWinnerInPlace_HysteresisDoesNotRecomputeConfidence` | 4.2 **wart**: hysteresis rotation leaves the carried-over runner-up confidence (here ≈0.07), NOT a recomputed top-rank value — Stage-4 anchor |
| `Composing_HarmonicSegmenterTests.GreedyExpand_PlacesRound1AnchorsAtChordChanges` | 1.4a Round-1 anchors at 0/960/1920/2880, roots 0/7/9/5, qualities Maj/Maj/Min/Maj, all round==1; `placedRegionsToTicks` agrees |
| `Composing_RegionAnalysisTests.AbsorbShortRegions_RootAgnostic` | 1.3(1) two short (<480t) DIFFERENT-rooted regions (Dm root 2, Em root 4) absorbed into the long C predecessor (endTick 1440→1920); first region never absorbed |
| `…InlineSameRootMerge_FiresOnSameQuality_BlocksOnQualityDiff` | 1.3(3) 3 contiguous C-major halves (incl. across barline) merge into [0,2880); same-root C-minor (quality differs) stays separate |
| `…CleanChordChanges_NoSpuriousMerge` | 1.3 four distinct ≥480t regions survive intact; pre-/post-merge stream sizes equal (no absorb/coalesce) |

---

## 3. NOT-PINNED list (with reasons)

| Item | Reason |
|------|--------|
| **coalesceShortSameRootRuns** (1.3 item 2) | Trigger requires ≥3 consecutive contiguous SAME-root, DIFFERENT-quality, sub-480t regions totaling ≥720t with a different-rooted predecessor — an emergent product of the full Pass 1/2/2b interaction that cannot be produced deterministically from a minimal hand-authored fixture (the contrived-fixture problem the scope valve covers). It is exercised end-to-end by its raison d'être, Corelli `op01n08d` m18, in the corpus-driven `pipeline_snapshot_tests` / `notation_tests`. |
| **Pass 2 / Pass 2b boundary fire-non-fire + `minGapTicks=960` floor** (1.3 item 4) | Sub-boundary detection (`detectOnsetSubBoundaries`, `detectBassMovementSubBoundaries`) only engages on parents ≥1920t with internal onset/bass variety; deterministically producing a parent that greedy-expand keeps whole yet Pass 2/2b then splits — without the split collapsing back via inline-merge — needs a reverse-engineered fixture beyond the minimal-fixture budget. Indirectly covered by the snapshot corpus. |
| **Sub-region `bassIsStepwiseToNext == false`** (1.3 item 5, Finding 4) | The forced-false write (L621/L823) is only observable if a Pass-2/2b sub-region SURVIVES Pass 3 into the output stream; no minimal fixture both produces a surviving sub-region and exposes the field unambiguously (Pass-1 main-loop regions legitimately compute it true, e.g. the G→A region in `s1c_seg_changes` shows stepNext=1). Verified by code reading; pinned-by-inspection only. |
| **Inline same-root merge via rcb arpeggio** (1.3 item 3, second clause) | The "rcb makes consecutive arpeggio slices pick the same root" interaction is the Δ=+7a Phase-D scenario, documented unreachable with constructed input (STATUS.md / `project_deltaseven_a_mechanism`). The structural same-root/same-quality merge IS pinned (`InlineSameRootMerge_…`). |
| **`fillGap` Round-2 placement + Segmentation-phase observable** (1.4a) | The `s1c_seg_changes` fixture places all four beats as Round-1 anchors (no gap), so Round 2 is not exercised. A Final-phase-only signal flipping a boundary is too contrived (instruction's stated fallback). The `scoringPhase==Segmentation` plumbing is verified by code reading (`harmonicsegmenter.cpp` L347, L706); not externally observable without white-box access. Round-1 anchor placement (the dominant segmentation behaviour) IS pinned. |
| **restampBassMinorSeventhAfterMerge / backfillNextRootPc** | Out of the four-pass scope the instruction enumerated; backfill is incidentally exercised by every multi-region test. Not separately pinned. |

---

## 4. Findings (pinned-but-questionable — Stage-3/4 feed)

- **G1 — `promoteWinnerInPlace` confidence wart is real and large.** On
  `s1c_a_minor_amb` the natural ranking is C-major(Ionian) conf 0.885 / A-minor
  conf **0.0745** / E-minor conf 1.000 — note even the natural list is not
  confidence-monotone (rank-2 has higher confidence than rank-1, because each is
  a local-gap value). After an unbeatable A-minor prior forces promotion, the
  rank-0 winner carries **0.0745**, not a recomputed top value. The Step-3
  redesign note's "0.025–1.00 spread on a correctly-keyed piece" is confirmed.
  Stage 4 must decide whether the HMM path recomputes confidence post-selection.
- **G2 — absorb is genuinely root-agnostic and runs after coalesce.** Two
  adjacent short different-rooted regions are both swallowed by the long
  predecessor (verified: Dm root 2 AND Em root 4 → C root 0). A root-aware merge
  would keep them; the decoder must reproduce the root-blind behaviour or
  consciously change it. coalesce running first (and being skipped when the
  predecessor shares the run root) means the two passes are order-coupled.
- **G3 — piece-start shortcut returns a single-element list** (size 1), unlike
  the ≥1 multi-candidate list every other path returns. Consumers that index
  `[1]` (batch's `keyModeRunnerUp`) get nothing at piece start. Pinned implicitly
  by the `ASSERT_EQ(size, 1u)` in the two piece-start tests.
- **G4 — fallback and piece-start both bypass `analyzeKeyMode` confidence.**
  Fallback hard-codes 0.0; piece-start hard-codes 0.5. These are sentinel
  confidences, not measured ones — Stage 4 weight-fitting should treat them as
  such, not as evidence strength.
- **G5 — partial-signature correction is a whole-score histogram decision** made
  once from `firstMeasure`, independent of the query tick: every region of a
  partial-signature score is reinterpreted identically. Correct for a
  single-key Baroque piece; a mid-score genuine modulation to the −2 Aeolian home
  would still be force-corrected. Out of Stage 1c scope but flagged for Stage 4.

---

## 5. Existing-coverage notes + new fixtures

- `keymodeanalyzer_tests.cpp` (985 lines, 57 tests) pins **`analyzeKeyMode`**
  scoring internals (modes, disambiguation, key-sig proximity, confidence range)
  on `PitchContext` vectors — **no Score, no resolver**. Stage 1c adds the
  RESOLVER layer (ranking, piece-start, partial-sig, promotion) with **zero
  overlap**, per Task 4.5.
- `pipeline_snapshot_tests` (10-score DCML corpus) and `notation_tests` drive
  `analyzeRegions`/`resolveKeyAndModeRanked` end-to-end over real scores — the
  indirect coverage the NOT-PINNED emergent passes (coalesce, Pass 2/2b,
  sub-region context) rely on. Not duplicated.

**New fixtures** (`src/composing/tests/data/`, 1.6–3.0 KB each):
`s1c_c_minor.mscx`, `s1c_c_major.mscx`, `s1c_unison_c.mscx`, `s1c_partial_cm.mscx`,
`s1c_g_minor.mscx`, `s1c_a_minor_amb.mscx`, `s1c_seg_changes.mscx`,
`s1c_seg_absorb.mscx`, `s1c_seg_merge.mscx`.

---

## 6. Counts and verification

| Suite | Before | After |
|-------|--------|-------|
| composing_tests | 487 | **498/498** (+11, all green) |
| notation_tests | 52 | **52/52** |
| pipeline_snapshot_tests | 11 | **11/11** (+1 standard `GenerateReport` skip; zero diffs, no goldens touched) |

BIR: **not run** — tests-only change, production binary byte-identical; 24/13
(Baroque) / 35/7 (Jazz) hold by construction.

Working-tree delta: `regionanalysis_tests.cpp` (new), `environment.cpp` (test
harness upgrade), `CMakeLists.txt` (sources), 9 `data/s1c_*.mscx` fixtures (new).
`cc_stage1c_report.md` is gitignored by design.

---

## 7. Commit proposal (single commit, awaiting Cowork confirmation)

Files: `src/composing/tests/regionanalysis_tests.cpp` (new),
`src/composing/tests/environment.cpp`, `src/composing/tests/CMakeLists.txt`,
`src/composing/tests/data/s1c_*.mscx` (9 new).

```
test: pin segmentation passes, harmonicsegmenter, and keyresolver (Stage 1c)

Unit tests for absorbShortRegions (root-agnostic absorption), inline
same-root merge, greedyExpandSegmentation Round-1 anchor placement, and the
keyresolver (ranked output, promoteWinnerInPlace without confidence
recompute, 81978321e3 partial-signature fix + counter-case, piece-start and
insufficient-data shortcuts). These subsystems consume a real Score, so the
composing test binary gains a score-loading environment (engraving ScoreRW +
EngravingModule/DrawModule init, mirroring engraving_tests) and 9 minimal
.mscx fixtures. coalesceShortSameRootRuns, Pass 2/2b sub-boundaries, and the
sub-region context field are left to the corpus-driven snapshot/notation
suites (see cc_stage1c_report.md NOT-PINNED). Differential baseline for
Stage 3 segmentation and Stage 4 key-path work (implementation_roadmap.md
1.3, 1.4). Production code untouched.
```
