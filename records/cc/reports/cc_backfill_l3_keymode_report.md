# CC backfill report — Phase-5 branch backfill (round 2), cluster 4 of 4: L3 keymode

**Tests-only. No production logic/behaviour change. `upstream` not touched; local commit only.
This cluster CLOSES the stable-half branch backfill (clusters 1–4).**

## §0 — Preamble
No unstaged `cowork_*`/`COWORK_*` docs present (`git status` clean apart from this cluster's new test
file + the gitignored `scratch_artifacts/` coverage outputs). Nothing to commit under §0.

## §1 — Headline

| Suite | Before (cluster-3 `45a89f49df`) | After |
|---|---|---|
| `composing_tests` | 810 PASSED | **826 PASSED** (+16 new tests) |
| `notation_tests` | 53 PASSED / 4 SKIPPED | **53 PASSED / 4 SKIPPED** (unchanged) |
| `pipeline_snapshot_tests` | 11 PASSED / 1 SKIPPED | **11 PASSED / 1 SKIPPED** (goldens NOT refreshed) |
| BIR corpus | 53 / 24 / 53 | **53 / 24 / 53 by construction** (zero production bytes changed) |

- **No production source touched** — `git show --stat c1df8e9510` is **2 files**: the new
  `src/composing/tests/keymode_branch_tests.cpp` (+382) and `src/composing/tests/CMakeLists.txt` (+1).
  `notation_tests` + `pipeline_snapshot_tests` link the unchanged `composing_analysis`, so their results
  are identical binaries — corpus/snapshot movement is impossible by construction, not by re-measurement.
  The §3 STOP condition did not arise.
- **No fixtures added** — every test is a direct call to a public leaf function (`keyModeTonicName`,
  `keyModeSuffix`, `ionianTonicPcForMode`, `keySignatureFifthsForKey`, `keyModeSignatureFifths`,
  `keyModeScaleIntervals`, `KeyModeAnalyzer::analyzeKeyMode`, `KeyModeSequenceDecoder::decodeLattice`) with
  hand-built `PitchContext` / synthetic lattice; no `.mscx`/`.musicxml` was needed.
- **Surfaced defects: one pre-existing, none new.** No correct-oracle-fails-current-code `DISABLED_`/xfail
  was needed (every oracle matched). ONE labelled **enabled** regression-guard pins the already-known,
  spec-flagged char/leading-tone presence-gate brittleness (the non-Bach C→F emission misread) — it
  asserts CURRENT behaviour, documented as a Phase-B/B2 issue (§4). This is the L3 §11 known defect, not a
  new finding.

## §2 — The worklist accounting (82 UNION-unhit arm-directions across the three files)

The cluster instruction quoted a `~72` per-file ADD-TEST **upper bound** (30/26/16). Re-confirmed at
source, the three files carry **82** UNION-unhit arm-directions (30/31/21 — the `cc_union_branch_coverage_report.md`
§5 lists). Of these, **37 are faithfully ADD-TESTable** (closed here) and **45 re-classify EXCLUDE at
source** (dead-by-logical-implication / exhaustive-enum-default / bounds-defensive / can't-happen-with-
valid-input — none closable without a production change, which would be a STOP). The 37 ADD-TEST set is
**below** the `~72` upper bound because the bound counted many arms the triage marked ADD-TEST that source
analysis proves unreachable (the same over-count clusters 2/3 reported).

| File | UNION-unhit | ADD-TEST (closed) | EXCLUDE (residual) |
|---|---:|---:|---:|
| `key/keymodeformatting.cpp` | 31 | **29** | 2 |
| `key/keymodeanalyzer.cpp` | 30 | **6** | 24 |
| `key/keymodesequence.cpp` | 21 | **2** | 19 |
| **total** | **82** | **37** | **45** |

The measured post-backfill residual (§5) is **exactly** 2 / 24 / 19 = 45 — the EXCLUDE set predicted at
source matches the `llvm-cov` re-measure to the arm.

## §3 — ADD-TEST coverage (16 tests, oracle = theory/contract re-derived at source)

New file `keymode_branch_tests.cpp`, registered in `tests/CMakeLists.txt` (after `keymodeanalyzer_tests.cpp`).

### `keymodeformatting.cpp` — display-label contract (3 tests, closes 29 case arms)
- **`TonicNameAtZeroFifths_AllModes`** — `keyModeTonicName(0, mode)` for all 21 modes. Oracle from theory:
  the white-key modal tonic at 0 sharps/flats (Ionian→C, Dorian→D, Phrygian→E, Lydian→F, Mixolydian→G,
  Aeolian→A, Locrian→B); the melodic/harmonic-minor family reuses the parent diatonic name array
  (documented contract + instruction: "harmonic/melodic-minor reuse Aeolian/Dorian names"); the two
  distinct families use the documented offsets — Altered = +1 semitone above Ionian C → C#, AlteredDomBB7 =
  aug5 above C → G#. Closes the 14 unhit tonic-name case arms (82/83/87/89–95/98/100/102/103).
- **`TonicNameAtNonZeroFifths`** + **`TonicNameClampsOutOfRangeFifths`** — non-zero signatures
  (−3 Aeolian→C, 2 Dorian→E, ±2/±1/±7 Ionian) and the out-of-range `std::clamp` boundary (−10→Cb, 10→C#).
  Contract pins exercising non-idx-7 name-table positions; no NEW arm (the clamp branch was already hit) but
  the documented signature→tonic contract.
- **`SuffixContract_AllModes`** — `keyModeSuffix(mode)` for all 21 modes against the project's documented
  label vocabulary (maj/Dor/Phryg/Lyd/Mixolyd/min/Loc/mel/Dor♭2/Lyd+/Lyd♭7/Mix♭6/Loc#2/alt/harm/Loc#6/
  Ion+/Dor#4/PhrygDom/Lyd#2/altDom). The "#N" shorthand = "Nth degree of the parent raised a semitone"
  (internally consistent — AeolianB5 = Locrian's ♭2→♮2 = "Loc#2"). The flat glyph is written as the UTF-8
  ♭ (U+266D), which under the build's `/utf-8` encodes to the same bytes as the source's `♭` escape
  (verified — the test passes). Closes the 15 unhit suffix case arms (113/114/115/118/120–126/129/131/133/134).

### `keymodeanalyzer.cpp` — public helpers + analyzeKeyMode edge arms (6 tests, closes 6 arms)
- **`IonianTonicPcForMode_ParentMapping`** + **`_OutOfRangePassesThrough`** — the parent-Ionian mapping
  (theory: D Dorian→C, A Aeolian→C, …) and the `modeIndex >= 21` defensive passthrough (returns tonicPc
  unchanged). Closes **156:9[T]**.
- **`KeySignatureFifthsForKey_MajorAndMinor`** + **`_EnharmonicNearestReference`** — major→Ionian circle
  position, minor→relative-major fifths, enharmonic spelling nearest the reference (F#/Gb @ ±6, C#/Db @
  7/−5). Closes the `isMajor` ternary **526:43[TF]** (both arms — the public function was reached by neither
  suite).
- **`KeyModeSignatureFifths_FullMode`** + **`ScaleIntervals_Contract`** — the full-mode signature wrapper
  and the canonical mode scale-interval table (theory). Contract pins (already-hit arms; no new credit).
- **`NegativeOutOfRangeKeySignatureUsesGlobalPath`** — a signature `< −7` makes the first operand of both
  in-range guards (`keySignatureFifths >= -7`) FALSE, dropping to the global-argmax fallback. The existing
  `OutOfRangeKeySignatureUsesGlobalPath` covers the `> 7` side (first operand TRUE, second FALSE); this
  covers the negative side. Closes **613:9[F]** and **645:9[F]**.
- **`DeclaredSpecificMode_ExactMatchCompatibility`** — a SPECIFIC declared mode (Dorian, not the
  class-level Ionian/Aeolian) routes `modeIsCompatibleWithDeclared` through the exact-match arm: with a
  strong penalty on D-Dorian evidence, the (only-unpenalized) Dorian reading wins. Closes **507:9[F]**.
- **`RunnerUpsShareWinnerSignatureWithDifferentMode`** — full C-major scale → the result list carries
  several entries sharing the winner's 0-signature with different modes (C Ionian / A Aeolian / G
  Mixolydian); the dedup only drops the exact winner. Contract pin for the runner-up-emission theme.
- **`KnownIssue_CharLtPresenceGate_EmissionRanksFAboveC_PhaseB`** — the labelled regression guard (§4).

### `keymodesequence.cpp` — decodeLattice edge arms (2 tests, closes 2 arms)
- **`DecodeLattice_EmptyStateSetReturnsEmpty`** — an empty state set (S=0) with a non-empty emission
  column returns `{}` via the `T == 0 || S == 0` guard's SECOND operand. The existing `EmptyLattice_NoSlices`
  covers `T == 0` (empty emissions), which short-circuits on the first operand. Closes **252:19[T]**.
- **`DecodeLattice_MaxAlternativesZeroKeepsAll`** — `maxAlternatives <= 0` keeps ALL surviving
  alternatives (uncapped); with three states each slice keeps its two non-winner states. The existing
  `Alternatives_RankedAndCapped` uses `maxAlternatives = 1` (the `min`/capped arm). Closes **389:28[T]**.

## §4 — Surfaced finding (rule 2): the char/leading-tone presence gate (labelled, Phase B/B2)

**`KnownIssue_CharLtPresenceGate_EmissionRanksFAboveC_PhaseB`** pins the spec-flagged brittle behaviour
(L3 §11; the non-Bach C→F regression, `project_k279_key_regression_diagnosis`). For a I+IV pitch context
(`C E G` + `F A C`) at signature 0, the analyzeKeyMode EMISSION (the `dumpOut` finalScores) ranks **F major
above C major** — the ever-present E (C's third) doubles as F's major-7 characteristic AND F's leading
tone (+1.80 char, +1.20 lt), while C's own characteristic/leading-tone B is absent → C is denied both (char
flips to −0.60). Hand-derived emission gap: F Ionian **17.50** > C Ionian **16.30** (margin 1.20); the test
asserts `finalScore(F·Ionian) > finalScore(C·Ionian)` AND that F is the global emission argmax — both
verified against the running binary.

This is asserted **as the known issue, NOT as correct** — the musically-correct answer is C; the fix
belongs to Phase B (B2, the spelling/function-aware leading tone), at which point this expectation flips
and the guard must be updated. It is an **enabled** guard (it passes today), labelled in name + comment,
and is the unit-level companion of the existing `notation_tests` xfail
`MozartK279OpeningPrefersCMajorOverFLydian` (still `GTEST_SKIP()`'d). No NEW defect was discovered; the
analyzeKeyMode RETURN winner (the family/tonal-centre selection) still gets C right — the brittleness is
purely in the emission scores the L3 decoder builds states from.

## §5 — Coverage re-measurement (UNION; `powershell.exe -File tools\coverage\run_branch_coverage.ps1`)

> Note: `pwsh` (PowerShell 7) is not installed on this box; the runner must be invoked via
> `powershell.exe` (Windows PowerShell 5.1), per the cluster-2 report — the runner's `pwsh` reproduction
> line is wrong for this environment. The whole-suite instrumented run executed all **826** composing
> tests.

| File | Branches | Before (unhit / %) | After (unhit / %) | Δ unhit |
|---|---:|---:|---:|---:|
| `key/keymodeformatting.cpp` | 88 | 31 / 64.77% | **2 / 97.73%** | −29 |
| `key/keymodeanalyzer.cpp` | 290 | 30 / 89.66% | **24 / 91.72%** | −6 |
| `key/keymodesequence.cpp` | 140 | 21 / 85.00% | **19 / 86.43%** | −2 |
| **cluster total** | **518** | **82 / 84.17%** | **45 / 91.31%** | **−37** |

- The measured residual (2 / 24 / 19) is **exactly** the EXCLUDE set classified at source (§6) — the
  source classification predicted 45, `llvm-cov` confirmed 45.
- **No covered-but-uncredited (inline-header) arms in this cluster.** Unlike clusters 1/2, every targeted
  function is **out-of-line** in `composing_analysis` (`keymodeformatting.cpp` / `keymodeanalyzer.cpp` /
  `keymodesequence.cpp` definitions), so all 37 closed arms were credited by the UNION view (the
  before→after delta matches the test set exactly; no COMDAT/inline attribution loss).
- Whole-module branch unhit moved **999 → 772** across clusters 1–4 cumulatively (this cluster's −37 is the
  key-file share; the rest is clusters 1–3 + incidental traversal).

## §6 — EXCLUDE re-classification at source (the 45 residual unhit arms)

No production change could close any of these without altering behaviour (a STOP); none attempted. Not
annotated in source (Phase-6 seal).

### `keymodeformatting.cpp` (2) — switch fall-through
- **79:13[F]** / **110:13[F]** — the `switch (mode)` fall-through to the trailing `return IONIAN_NAMES[idx]`
  / `return ""`. Every call passes a valid `KeySigMode` (one of the 21 enumerated cases), so the
  no-case-matched arm is unreachable through the public API.

### `keymodeanalyzer.cpp` (24)
**Dead-by-logical-implication (16):**
- **256:25[F]** (`!inKS`) / **257:18[F]** (`!inC`) — in the scale-membership `if/else-if` chain, reaching
  the second/third arm already implies the operand is true (a note caught by the first `if (inC && inKS)`
  can't reach `else if (inC && !inKS)` with `inKS` true), so the false-arm is unreachable.
- **347:9[F]** (`requireBoth` false) / **354:12[TF]** (the `requireBoth==false`-with-secondary fallthrough)
  — EVERY mode in `CHARACTERISTIC` with `interval2 >= 0` has `requireBoth == true`, so these arms are dead
  against the static table.
- **463:44[F]**, **467:44[F]**, **476:44[F]**, **479:44[F]** — `hasCompleteTriad ⟹ hasTonic` (line 294), so
  the `aHasTonic`/`bHasTonic` operand evaluated immediately after a `hasCompleteTriad` operand is always
  true; its false-arm is dead.
- **681:39[F]**, **682:42[F]**, **685:47[F]**, **686:50[F]** — `bestByCenter`/`bestByRaw` `std::optional`s
  are always engaged after the ≥1-iteration selection loop (`numModeSlots == 21`), so `has_value()` is
  always true.
- **738:32[F]** — the result-building range-`for` always `break`s at `results.size() >= 3` before
  exhausting `allCandidates` (≥3 distinct (fifths,mode) pairs always exist among the 252 candidates), so
  the loop-exhaustion arm is never taken.
- **762:9[F]** — `!results.empty()` is always true (`best` is pushed unconditionally before this point).
- **764:38[F]** — `results.size() >= 2` is always true (the dedup leaves ≥3 distinct entries), so the
  single-result `runnerUpScore = 0.0` fallback (the "single-result confidence gap-vs-0" theme) is
  **structurally unreachable** via `analyzeKeyMode`.

**Exhaustive-enum / bounds defensive (3):**
- **183:5[T]** — `possibleIonianFifthsForPc` `default:` (ionianPc is always 0..11 mod 12).
- **405:5[T]** — `scoreModePrior` `default:` (modeIndex is always 0..20 from `ACTIVE_MODE_INDICES`).
- **841:18[F]** — `keyModeScaleIntervals` `modeIdx < MODES.size()` clamp false-arm (a valid `KeySigMode`
  enum is always < 21).

**Reachable-only-with-a-tonic-less top candidate (4) — near-dead via the −2.50 missing-tonic penalty:**
- **467:57[T]**, **479:57[F]**, **482:9[F]**, **485:22[T]** — the pairwise-disambiguation `evalB`-side arms
  all require `evalA` (the HIGHER raw-score family candidate) to have NO tonic present while `evalB` carries
  tonic/triad. The `missingTonicPenalty` (−2.50, plus the absent +1.60 tonic and +2.50 triad it forgoes)
  makes a tonic-less candidate out-scoring a tonic-bearing one at the family top a configuration the scorer
  does not produce in practice; not faithfully constructible without contrived prior/scale overrides.
  (The `evalA`-side arms — 463/476/482-true — ARE covered by the existing relative-pair tests.)

**Hard / fragile single arm (1):**
- **684:42[F]** — requires `bestByCenter->modeIndex < 7` (a diatonic mode wins by tonal-centre) AND
  `bestByRaw->modeIndex >= 7` (a melodic/harmonic-minor mode wins by RAW score) simultaneously — a fragile
  cross-metric divergence (the non-diatonic mode must overcome its ≈2–3 negative prior on raw while losing
  the prior-free tonal-centre); left uncovered (no clean single-winner oracle).

### `keymodesequence.cpp` (19)
**File-local buildLattice empty-context (2):**
- **146:13[F]** (`!ctx.empty()` false) / **149:13[T]** (`dump.empty()` true) — a change-point slice's
  ±`windowBeats` emission window always contains the slice's own onsets, so a real `decode()` never produces
  an empty-context / empty-dump slice.

**populateEmissionConfidence defensive (4):**
- **206:13[T]** (`t < 0`) / **206:22[T]** (`t >= emissions.size()`) — `sk.sliceIndex` is always a valid
  global slice index.
- **210:13[T]** (`ci < 0`) — the chosen result always comes from a lattice state (`stateToResult(states[w])`),
  so `stateIndexForResult` always finds it (the "stateIndexForResult not-found → skip" theme is unreachable).
- **222:33[T]** (`bestOther == NEG_INF` → vs 0) — requires a 1-state lattice from a real `decode()`, which
  the top-K union never produces.

**stateIndexForResult same-tonic-diff-mode (1):**
- **179:29[F]** — `states[i].mode == r.mode` false-arm (tonicPc matches, mode differs). File-local;
  reachable only through `decode()`/`redecodeRange()` with a specific union ordering; HARD, not closed.

**decodeLattice collapsed-lattice / broken-chain defensive (12):**
- **291:17[F]** (`bestPrev >= 0` false), **308:9[F]** (`endState >= 0` false), **357:23[F]** (`chosen[t] >= 0`
  false), **366:43[T]** (`beta == NEG_INF` second operand), **378:37[F]**/**378:63[F]** (winner alpha/beta
  NEG_INF guards), **380:51[T]** (`winnerTotal == NEG_INF` second operand) — all require an all-NEG_INF
  column, which cannot occur with finite emissions and valid (in-range or −1) pins; the reachable
  single-state confidence (the 380 FIRST operand) is already covered by the existing `SingleState` test.
- **313:26[T]**, **317:33[TF]**, **318:25[TF]** — the **documented broken-chain fallback** (source comment:
  "Defensive: a broken chain should not happen"); the instruction explicitly routes this to skip.

## §7 — Scope & gate
- **Tests-only**; no production `.cpp`/`.h`/tool logic changed (`git show --stat c1df8e9510`: only the new
  `keymode_branch_tests.cpp` + the CMake entry). No gap was closable only by changing production.
- Build green; `composing_tests` **826** (+16); `notation_tests` **53 / 4-skip** and
  `pipeline_snapshot_tests` **11 / 1-skip** both unchanged (no golden refresh); corpus **53 / 24 / 53** by
  construction (no scoring/production byte changed — no corpus run needed or performed).
- `upstream` untouched; local commit only. Exclusions NOT annotated in source (Phase-6 seal).
- **Commit sha: `c1df8e95100a671c9314bddc21b8775c63e95e17`** (`c1df8e9510`) — 2 files changed, 383
  insertions, **zero production source** (Cowork verifies by `git show --stat c1df8e9510`: only
  `src/composing/tests/keymode_branch_tests.cpp` + `src/composing/tests/CMakeLists.txt`).

## §8 — Wrap: the cumulative stable-half picture (clusters 1–4)

This cluster closes the four-cluster stable-half branch backfill. Cumulative:

| Cluster | File-group | Commit | Tests added | Group branch% before→after |
|---|---|---|---:|---|
| 1 | engravingbridge + metricweights | `3f2e4bebe2` | +20 | 82.24% → 91.02% (490 br, 87→44 unhit) |
| 2 | L4 oracle + gates (chord_branch + postscoringgates) | `1218ad1003` | +63 | 93.25% → 97.51% (1688 br, 114→42 unhit) |
| 3 | chordsymbolformatter | `45a89f49df` | +32 | 85.51% → 95.48% (752 br, 109→34 unhit) |
| 4 | L3 keymode (analyzer/formatting/sequence) | `c1df8e9510` | +16 | 84.17% → 91.31% (518 br, 82→45 unhit) |
| **Σ** | **four stable file-groups** | — | **+131** | **88.63% → 95.22%** (3448 br, **392 → 165** unhit, **−227**) |

- **Total tests added across clusters 1–4: +131** (`composing_tests` 695 → 826).
- **Union branch% over the four stable file-groups: 88.63% → 95.22%** (392 → 165 unhit arm-directions).
  The 165 residual is the consolidated EXCLUDE set across the four clusters (dead-by-implication /
  exhaustive-enum-default / bounds-defensive / can't-happen-with-valid-input / documented broken-chain
  fallback) + a small COMDAT/inline-uncredited tail (clusters 1–2 only; cluster 4 has none).

### Consolidated surfaced-defects ledger (Phase-5 sign-off)
- **Cluster 1:** none.
- **Cluster 2:** none.
- **Cluster 3:** `DISABLED_GermanFlatBass_ShouldKeepSlash` — the **only `DISABLED_` (xfail)** of the
  stable half: `csfIsValidBassNoteName` rejects German flat-bass spellings ("Ces"/"Fes"), dropping the
  slash (e.g. German `C/Ces` → `C`); pinned alongside an enabled `RegressionGuard_GermanFlatBass_SlashDropped`.
  Also flagged-not-asserted: `mMaj7` drops an altered ninth (a possible lossy minor-path simplification).
- **Cluster 4:** `KnownIssue_CharLtPresenceGate_EmissionRanksFAboveC_PhaseB` — an **enabled** labelled
  regression-guard (NOT a new `DISABLED_`) pinning the already-known char/leading-tone presence-gate
  brittleness (the L3 §11 / K279 non-Bach C→F emission misread; fix = Phase B/B2). Companion to the existing
  `notation_tests` xfail `MozartK279OpeningPrefersCMajorOverFLydian`.

**Net for the Phase-5 ledger:** exactly **one new `DISABLED_`/xfail** across the stable half (the German-bass
slash, cluster 3), plus **two enabled labelled regression-guards** documenting known issues (German-bass
slash + char/lt presence-gate). The cluster-3 mMaj7 lossy-suffix observation is flagged for Cowork, not
asserted. All four clusters: tests-only, corpus 53/24/53 by construction, snapshots untouched, `upstream`
never.
