# CC Stage 1b Report — Pin post-scoring gates A–L, Iter 86/91/pedal, fixed-bug cases

**Date:** 2026-06-10 · **Roadmap items:** 1.1 (gate unit tests) + 1.5 (pin fixed bugs)
**Deliverable:** `src/composing/tests/postscoringgates_tests.cpp` (+ CMakeLists registration).
**Production code untouched** — tests only. No BIR run needed or performed: the production
binary is byte-identical by construction.

---

## 1. Survey — definitive gate inventory (code-derived)

Source of truth: `applyPostScoringGates()` (`chordanalyzer.cpp` L1888–L2474) and
`applyIter8691Pedal()` (L2985–L3161), read end-to-end. Where this section disagrees
with `docs/scoring_model.md` §6, the code is authoritative; discrepancies are flagged
**[DOC]** for the next doc pass (no docs changed in this run).

### 1.1 Execution order (production call sites, incl. `analyzeWithGates`)

```
analyzeChord()                      — oracle + competition pipeline, publishes gateCtx
  └─ applyIter8691Pedal()           — Iter 86 → Iter 91 → two-pass pedal
       └─ applyPostScoringGates()   — bias-capture → [A → FM2 → B → C → D → E → F →
                                       bias-deduction+sort] → G → H → I → K → L → J
```

**[DOC]** §6's table lists Gate J between I and K ("~L3151" vs K "~L3080", L "~L3117")
— the line references are right but the prose order is misleading: **Gate J executes
LAST**, after K and L.

### 1.2 The outer guard — shared by ALL gates A–L

Everything in `applyPostScoringGates` (including the no-margin identity gates A and J)
runs inside one block gated on:

- `prefs.inversionSuspicionMargin > 0.0`
- `prefs.inversionBonusReduction < 1.0`
- `results.size() >= 2`
- `gateCtx.distinctPcs >= 3`

**[DOC]** §6 attributes `distinctPcs >= 3` to the bias correction only; in code it
gates the whole family. Consequence: setting `inversionSuspicionMargin = 0`
("disable the inversion correction") also disables Gates A–L entirely. Pinned in
`OuterGuard_SuspicionMarginZero_DisablesAllGates`. Flagged in §4 (Findings F2).

### 1.3 Pre-sort capture (Sub-9a infrastructure)

Captured before any swap/sort, from the live `winner = results[0]` reference:
`originalWinnerQuality`, `originalWinnerRootPc`, `originalWinnerHasAddedSixth`,
`winnerBassIsRoot`, `winnerQualityTargeted (= quality ∈ {Major, Minor})`.

Gates G, I, K, L, J key on `originalWinner*`; gates H, I, K, L mix in **live**
`winner.identity.*` reads (bass, score, current quality) — see Findings F4.

### 1.4 Gate inventory

| # | Gate | Entry conditions (all required) | Effect | Margin | Preset flag | Mutual exclusion |
|---|------|--------------------------------|--------|--------|-------------|------------------|
| 0 | Block-1 entry | `winnerBassIsRoot` && winner quality ∈ {Major, Minor}; a "bestAlt" exists: first results[i≥1] with different root and clean (Maj/Min) quality, OR the HalfDim-inversion exception (all 4 alt tones present — bass pc exempt from the weight threshold — and winner bass ∈ {m3, b5, m7} of alt root) | selects `bestAltIdx` | — | — | container for A–F + bias |
| A | Major-add6 ↔ Minor enharmonic fast path | winner Major+AddedSixth, bestAlt Minor at `(root+9)%12` | swap | none | `preferMinorOverMajorAdd6` | sets `didEnharmonicFlip` |
| FM2 | rawCandidates fallback for A | winner Major+AddedSixth, partner missing from results[]; scan `rawCandidates` until `rc.score < gateCtx.threshold` for Minor at expected root | push `buildResult(rc)` + swap | none | same | sets flag |
| B | forward evidence | A's conditions + `nextRootPc == altRoot` + `bassIsStepwiseToNext` | swap | none | same | **UNREACHABLE** (see F1) |
| C | 3-region window | A's conditions + `bassIsStepwiseFromPrevious` + altRoot ∈ `recentRootPcs` | swap | none | same | **UNREACHABLE** (F1) |
| D | consecutive stepwise | A's conditions + `consecutiveBassStepwiseCount >= 2` | swap | none | same | **UNREACHABLE** (F1) |
| E | first-inversion Minor→Major | winner Minor, bestAlt Major at `(root+8)%12`, `pcWeight[altRoot] > extensionThreshold`, context && (stepwise from-prev OR to-next) | swap | none | `preferMinorOverMajorAdd6` | `didEnharmonicFlip` chain |
| F | second-inversion →Major | bestAlt Major at `(root+5)%12`, context && stepwise (either direction). **No winner-quality condition beyond Block-1 (Minor winners qualify too), no pcWeight check** | swap | none | `preferMinorOverMajorAdd6` | `didEnharmonicFlip` chain |
| bias | bass-root bias correction | `!didEnharmonicFlip`; seventh-exemption: skip iff winner has m7/M7 and alt does not; `margin < inversionSuspicionMargin (0.70)` | `results[0].score -= bassNoteRootBonus × (1 − inversionBonusReduction)`; if bestAlt was the HalfDim-inversion exception AND `preferMinorOverMajorAdd6`: `alt.score += 0.55` (`kHalfDimFirstInversionBonus`); `stable_sort` desc | < 0.70 strict | bonus arm only | runs only if A–F did not flip |
| G-E | Minor-add6 ↔ HalfDim7, key-function | inside Block-1; `originalWinnerQuality == Minor && originalWinnerHasAddedSixth`; HalfDim alt at `(originalWinnerRootPc+9)%12` found in results[1..] or pulled from rawCandidates (**no threshold check on this pull**, unlike FM2); alt root ∈ {tonic+11, tonic+2, tonic+4} (viiø7/iiø7/iiiø7) | swap | none | `preferMinorOverMajorAdd6` | `didGFlip` chain; pulled phantom popped if no sub-gate fires |
| G-B | temporal fallback | … + `nextRootPc == expectedRoot` + `bassIsStepwiseToNext` | swap | none | same | chain |
| G-C | temporal fallback | … + `bassIsStepwiseFromPrevious` + expectedRoot ∈ `recentRootPcs` | swap | none | same | chain |
| G-D | temporal fallback | … + `consecutiveBassStepwiseCount >= 2` | swap | none | same | chain |
| H | augmented rotation | outside Block-1; `winnerBassIsRoot` (captured) && **live** `winner.quality == Augmented` && context; Augmented alt at `(root+4)` or `(root+8)`; sub-gates H-B/H-C/H-D mirror G-B/C/D | swap | none | `preferMinorOverMajorAdd6` | `didAugmentedFlip`; loops {+4, +8} |
| I | diatonic 1st-inv Major over root-pos Minor | `winnerBassIsRoot` && `originalWinnerQuality == Minor` && `keyTonicPc >= 0`; alt: same bass as **live** winner, not root-position, root at I4 below bass, root diatonic, `pcWeight[root] > extensionThreshold` | swap, break | ≤ 0.45 | none | first qualifying alt |
| K | 1st-inv Augmented | `winnerBassIsRoot` && `originalWinnerQuality == Augmented` && `keyTonicPc >= 0`; alt: same bass, not root-position, I4, augmented collection (Augmented OR Major+SharpFifth), diatonic | swap, break | ≤ 0.20 | none | first qualifying alt |
| L | same-root Major over Augmented | `originalWinnerQuality == Augmented` && `winnerBassIsRoot` && `keyTonicPc >= 0` && **live** winner has no m7/M7; alt: Major, same root, same bass, diatonic | swap, break | ≤ 0.35 | none | first qualifying alt |
| J | vii° → V7 completion | `originalWinnerQuality == Diminished`; **live** results[0] still root-position Diminished without DiminishedSeventh; `pcWeight[(root−4)%12] > extensionThreshold`; alt: Major+MinorSeventh rooted at root−4 | swap, break | none | none | runs last |

### 1.5 `applyIter8691Pedal` inventory (runs BEFORE the gates)

| Pass | Conditions | Effect |
|------|-----------|--------|
| Iter 86 | winner Major/Minor, no m7/M7; `bassPc != rootPc`; `(bassPc − rootPc) % 12 == 10`; `pcWeight[bassPc] > extensionThreshold` | stamp `MinorSeventh` on the winner (Am/G → Am7/G); side effect: bass becomes a chord tone, so the pedal pass below skips |
| Iter 91 | context && `nextRootPc == bassPc`; winner plain triad; Pattern A: delta 8 + Minor, Pattern B: delta 9 + Major | promote the FIRST `rawCandidates` entry with `rootPc == bassPc` (push `buildResult` + swap). No `previousRootPc` arm (deliberate — I → I6 false fires) |
| Pedal two-pass | `bassPc >= 0` && `pedalConfidenceThreshold > 0`; bass NOT a chord tone of winner; ≥ 2 distinct upper PCs; Pass 2 (bass pc removed, `inversionSuspicionMargin = 0`, no context, recursive Iter86/91 tail) sigmoid confidence `1/(1+e^{−1.5(gap−2)})` ≥ threshold, gap measured to first different-root competitor | replace results with Pass-2 list; set `isPedalPoint`, `pedalBassPc` |

### 1.6 Preset facts (verified in `tools/batch_analyze.cpp`)

- **Baroque** = struct defaults + `preferMinorOverMajorAdd6 = true` (only difference).
- **Standard/Modal/Contemporary** = same as Baroque.
- **Jazz** = `extensionThreshold 0.12`, `preferMinorOverMajorAdd6 false`, inversion
  bonuses reduced (0.20/0.20/0.15/0.20).
- **[DOC]** CLAUDE.md / scoring_model §4 state `maxTotalInversionContextBonus`
  Baroque=2.5 / Jazz=0.6; `batch_analyze.cpp` sets **neither** (both presets inherit the
  2.0 default; a comment says tuning is "tracked in iteration_plan_inversion_redesign.md
  Iteration 4"). Either the doc is aspirational or the values are set on another path —
  reconcile in the doc pass.

### 1.7 Fixture strategy

`applyPostScoringGates()` / `applyIter8691Pedal()` consume only
`results[] + PostScoringGateContext + prefs + ChordTemporalContext` — all
constructible. **Direct construction is used for every per-gate test** (the documented
fallback): margin brackets like 0.43/0.47 around Gate I's 0.45 are impossible to dial
through real tones. The production order is still honored where it matters: four
end-to-end shapes go through `analyzeWithGates()` (real `analyzeChord` →
`applyIter8691Pedal` → `applyPostScoringGates`): Gate J bwv110.7, Gate R Δ=+7b,
Iter 92 Bug 1 (onset bass) and Bug 2 (w_complete). Both preset branches are pinned
where a gate is preset-gated (A, H explicitly; E/F/G via the Baroque-prefs fires).

---

## 2. Test inventory

All in `src/composing/tests/postscoringgates_tests.cpp`, suite
`Composing_PostScoringGateTests` (48 tests).

| Test | Pins |
|------|------|
| OuterGuard_DistinctPcsBelow3_DisablesAllGates | shared `distinctPcs >= 3` guard (Gate A shape + Gate J shape) |
| OuterGuard_SuspicionMarginZero_DisablesAllGates | `inversionSuspicionMargin = 0` kills ALL gates (F2) |
| BiasCorrection_Fires_DeductsBassBonusAndResorts | deduction = `bassNoteRootBonus` (0.70), re-sort promotes clean alt |
| BiasCorrection_MarginBracket | 0.68 fires / 0.72 doesn't (strict < 0.70) |
| BiasCorrection_SeventhExemption | winner-only 7th → exempt; alt-only 7th → fires |
| GateA_FastPath_FiresWithoutTemporalOrMargin | A is unconditional given flag+shape; swap leaves scores untouched |
| GateA_PresetOff_NoFlip | Jazz branch (`preferMinorOverMajorAdd6 = false`) |
| GateA_PlainMajorWinner_NoFlip | added-sixth guard |
| GateA_FM2_PullsMinorAltFromRawCandidates | FM2 pull + buildResult (bass + m7 detection) |
| GateA_FM2_BelowThresholdCandidateNotPulled | FM2 raw-scan threshold break |
| GateE_MinorWinnerFlipsToMajorAtPlus8 | E fire (margin-free, stepwise-licensed) |
| GateE_NoStepwiseSignal_NoFlip | E temporal requirement |
| GateE_AltRootBelowThreshold_NoFlip | E alt-root-present guard |
| GateF_MajorWinnerFlipsToMajorAtPlus5 | F fire (lookahead stepwise) |
| GateF_NoStepwiseSignal_NoFlip | F temporal requirement |
| GateGE_KeyFunctionFlip_NoTemporalNeeded | G-E viiø7 key-function fire (Dm6 → Bø7/D) |
| GateGE_PullsHalfDimFromRawCandidates | G-E rawCandidates pull-in (iiø7 in G major) |
| GateG_PulledCandidatePoppedWhenNoSubGateFires | phantom cleanup (pop_back) |
| GateGB_ForwardEvidenceFlips | G-B fire |
| GateGC_RecentRootAndStepwiseFlips | G-C fire |
| GateGD_ConsecutiveStepwiseBoundary | G-D boundary pair (2 fires / 1 doesn't) |
| GateG_NoContextNonFunctionalRoot_NoFlip | G family non-fire |
| GateH_ForwardEvidence_RotatesPlus4 | H fire, +4 arm |
| GateH_ForwardEvidence_RotatesPlus8 | H fire, +8 arm |
| GateH_NoContext_NoRotation | H requires temporal context |
| GateH_PresetOff_NoRotation | H preset branch |
| GateI_MarginBracket | 0.43 fires / 0.47 doesn't (≤ 0.45) |
| GateI_NonDiatonicAltRoot_NoFlip | I diatonic guard |
| GateI_AltRootBelowThreshold_NoFlip | I "no rootless inversion" guard |
| GateK_MarginBracket | 0.18 fires / 0.22 doesn't (≤ 0.20); bwv40.6 shape |
| GateK_MajorSharpFifthEncodingAccepted | K second encoding variant |
| GateL_MarginBracket | 0.33 fires / 0.37 doesn't (≤ 0.35); bwv144.6 shape |
| GateL_AugmentedSeventhWinner_NoDemotion | L seventh exclusion |
| GateJ_DimTriadWithSoundingDominantRoot_SwapsToV65 | J fire (margin-free) |
| GateJ_DimSeventhWinner_NoSwap | J vii°7 protection |
| GateJ_DominantRootBelowThreshold_NoSwap | J present-root guard |
| GateJ_AltWithoutMinorSeventh_NoSwap | J alt-must-carry-m7 |
| Ordering_Sub9a_GateGEUsesPreSortWinnerRoot | **ordering pin**: bias sort changes results[0]; G-E computes from captured root 0, not promoted root 9; F#ø7 decoy proves bug visibility; also pins deduction (1.3) + kHalfDimFirstInversionBonus (2.35) + duplicate-push (size 3) |
| Iter86_BassAtFlatSeven_StampsMinorSeventh | Iter 86 fire |
| Iter86_BassPcBelowThreshold_NoStamp | Iter 86 threshold guard |
| Iter86_WinnerWithSeventh_NoStamp | Iter 86 plain-triad guard |
| Iter91_PatternA_MinorDelta8_PromotesBassRoot | Iter 91 Pattern A (Em/C → C) |
| Iter91_PatternB_MajorDelta9_PromotesBassRoot | Iter 91 Pattern B (C/A → Am) |
| Iter91_NoForwardConfirmation_NoPromotion | Iter 91 forward gate (no ctx; wrong nextRoot) |
| E2E_GateJ_Bwv110Shape_FSharp7OverASharp | **roadmap 1.5(1)**: bwv110.7 m10 shape through full pipeline → F#7/A# (V6/5) |
| E2E_GateR_DeltaPlus7b_FirstInversionBeatsContinuedRoot | **roadmap 1.5(3)**: Δ=+7b bwv320 mapping (G/E → C) end-to-end |
| E2E_Iter92_OnsetBassBeatsPassingLowNote | **roadmap 1.5(4a)**: bwv103.6 shape; joint-vs-legacy bass contrast pair |
| E2E_Iter92_WComplete_RootPositionTriadWins | **roadmap 1.5(4b)**: bwv310 shape (root-position complete triad wins under regional accumulation) |

Roadmap 1.5(2) (Sub-9a) = `Ordering_Sub9a_GateGEUsesPreSortWinnerRoot` (cross-referenced
from Task 2's ordering requirement — one test serves both).

---

## 3. NOT-PINNED list

| Item | Reason |
|------|--------|
| Gates B/C/D (Major-add6 family temporal gates) | **Unreachable code** (Finding F1): their precondition sets are strict supersets of Gate A's, and A fires first unconditionally. No fixture can reach them; a fire test is impossible without a production change. The family's behavior IS pinned — via A. |
| Pedal two-pass | Already pinned by the eight `Composing_PedalPointTests` in `chordanalyzer_tests.cpp` (fire, chord-tone-bass non-fire, zero-threshold disable, 0.99-threshold low-confidence non-fire, inner-voice chord-tone). Not duplicated. |
| Gate H sub-gates H-C / H-D individually | H-B (+4 and +8 arms) pinned; H-C/H-D are near-copies of the pinned G-C/G-D logic operating on the same context fields. Skipped per the instruction's "temporal mirrors" allowance. |
| Bias-correction same-root-alt skip (alt differing only in extensions) | Low-value scan detail; scope valve. |
| Gate F Minor-winner fire (quality-agnostic behavior) | Behavior noted as Finding F5; only the Major-winner fire is pinned to avoid pinning a probably-unintended path as a contract. |

---

## 4. Findings — pinned-but-questionable behavior (Stage-3 feed)

- **F1 — Gates B/C/D are dead code.** Gate A (the "enharmonic fast path") has exactly
  the conditions `winner Major+Add6 && bestAlt Minor at (root+9)` and no temporal
  requirement; B/C/D repeat those conditions plus temporal evidence, behind
  `!didEnharmonicFlip`. A always wins the race. The §6 doc row ("Temporal gates B/C/D
  check for forward / stepwise / consecutive evidence") describes a mechanism that can
  never execute. Stage 3: the decoder only needs to reproduce A.
- **F2 — `inversionSuspicionMargin = 0` disables ALL gates,** not just the bias
  correction — including Gate J's vii°→V7 fix and the Gate A enharmonic preference.
  Any caller that zeroes the margin to "switch off inversion correction" (e.g. the
  pedal Pass-2 prefs do this for the nested analyzeChord; harmless there since
  Pass 2 results skip applyPostScoringGates) silently loses every identity gate.
- **F3 — distinctPcs ≥ 3 gates the whole family** (doc attributes it to bias
  correction only). Sparse 2-PC regions get no gate corrections at all.
- **F4 — mixed live/captured winner reads.** Gate H requires live
  `winner.quality == Augmented` but captured `winnerBassIsRoot`; Gates I/K/L compare
  margins against the live (possibly bias-deducted) `winner.identity.score` while
  keying entry on `originalWinnerQuality`. After a bias re-sort these refer to
  *different candidates*. The Sub-9a fix made G-E consistent; the others were left
  half-migrated. Pinned as-is.
- **F5 — Gate F has no winner-quality or alt-root-presence condition.** A Minor
  winner with a Major alt at +5 flips on a stepwise signal alone, and the promoted
  root does not need to be sounding (unlike Gate E's pcWeight check). Asymmetry looks
  unintentional.
- **F6 — gate swaps can leave results[] unsorted.** Sub-9a fixture ends as
  [1.7, 1.3, 2.35] — the alternatives list shown to users is not score-ordered after
  a G-E pull. Winner is correct; tail order is an artifact.
- **F7 — G-E's rawCandidates pull has no threshold check** (FM2's loop breaks at
  `gateCtx.threshold`; G-E scans everything). A deeply sub-threshold HalfDim cell can
  be promoted to winner by key function alone.
- **F8 — G-E can push a duplicate** of a candidate already promoted to results[0]
  (its scan starts at i = 1), pinned in the Sub-9a test (`results.size() == 3`).

---

## 5. Existing-coverage notes (Task-1 grep)

- `Composing_PedalPointTests` (chordanalyzer_tests.cpp L2118–2206): full pedal
  two-pass coverage — cross-referenced, not duplicated.
- `gater_tests.cpp`: Gate R predicate (kMasks for all 17 templates) + four branch
  combinations + phase gating. The new `E2E_GateR_DeltaPlus7b…` adds the missing
  end-to-end production-order shape on top.
- `Cm7SlashF_StepwiseBassContext_IsCm7NotFsus` (chordanalyzer_tests.cpp): the Gate R
  `basisDep > 0` spare-case (extended slash voicing) — already end-to-end.
- No existing tests touched gates A–L, the bias correction, Iter 86, Iter 91, or
  Iter 92 joint scoring (grep: bwv103/bwv310/bwv110/Em\\/C/Am7b5/originalWinner —
  only pedal hits). bwv310/bwv103.6 were NOT in catalog tests; synthesized here.

---

## 6. Counts and verification

| Suite | Before | After |
|-------|--------|-------|
| composing_tests | 439 | **487/487** (+48, all green first run) |
| notation_tests | 52 | **52/52** |
| pipeline_snapshot_tests | 11 | **11/11** (+1 standard GenerateReport skip; zero diffs, no goldens touched) |

Working tree delta: `postscoringgates_tests.cpp` (new) + `CMakeLists.txt` (one line) +
this report (`cc_*.md` is gitignored by design). The pre-existing modifications to
STATUS.md / COWORK_HANDOFF.md / implementation_roadmap.md predate this session.

BIR: **not run** — tests-only change, production binary byte-identical; 24/13
(Baroque) / 35/7 (Jazz) hold by construction.

## 7. Commit proposal (single commit, awaiting Cowork confirmation)

Files: `src/composing/tests/postscoringgates_tests.cpp` (new),
`src/composing/tests/CMakeLists.txt` (one line).

```
test: pin post-scoring gates A-L, Iter 86/91/pedal, and fixed-bug cases (Stage 1b)

Per-gate fire / non-fire / margin-boundary tests through the production
analyzeWithGates order, incl. the Sub-9a originalWinnerRootPc pre-sort
capture, Gate J vii->V7 completion (bwv110.7 shape), the Gate R Delta=+7b
end-to-end shape, and Iter 92 joint-bass cases. Differential baseline for
the Stage 3 decoder migration (implementation_roadmap.md 1.1, 1.5).
Production code untouched.
```
