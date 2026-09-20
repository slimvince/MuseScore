# Phase 5c — Step 1 (Layer 5 / FUNCTION): the progression model + base Roman-numeral derivation

> **Discipline:** Step 1 of `cowork_phase5c_l5_build_plan.md`, against the SIGNED contract
> `cowork_layer5_function_design.md` §5.0 + §5.1. Built **DORMANT** (new module, no production consumer)
> → **byte-identical on production**. **Default constants only — none to tune at this step (§4).** Reuse,
> do not duplicate. This dossier is gitignored.
>
> **HEAD `811272bdd1`** (Step-1 code). Prior: `f32688951d` (§0 docs sweep), `334d758d04` (session 9).

## 0. Result — GREEN, built, all gates pass

- **§0 sweep** committed `f32688951d` (Cowork docs + the F6 fix). **§2/§3 build + §5 tests** committed `811272bdd1`.
- **Build clean**; **composing 878 → 895 (+17)**; **notation 53** (4 skipped, baseline); **pipeline_snapshot 11/11
  — NO golden refresh** (the byte-identical proof). **Corpus 53/24/53 unchanged by construction** (no production reach).
- **§1 verdict:** all progression inputs reachable; the base RN reuses the **one** formatter (no duplication forced);
  placement is a new dormant unit in `analysis/function/`. No structural change beyond the dormant module needed → no STOP.

---

## §0 — Sweep (done)

Committed local-only (`f32688951d`, `docs(cowork): L5 build plan + Step-0 F1/F2 resolutions`):
`cowork_phase5c_l5_build_plan.md` (new) + the F1 sync to `cowork_layer5_function_design.md` §5.5 (symmetric-rotation
rule) + the §15-0 phrase-boundary-BUILT sync + the `cowork_phrase_boundary_design.md` syncs. **F6 fixed in the same
commit:** the §15-0 working-tree edit had duplicated the "be defined **generally** … the fermata is only the
*chorale-specific* marker, so" sentence (the new "The phrase boundary is defined generally…" line left the old "be
defined generally…" line in place); the stale duplicate line was removed so it reads cleanly. `scratch_artifacts/` is
gitignored and was not committed.

---

## §1 — INVESTIGATE-confirm (read-only), the incremental check

### (a) The progression model's inputs (§5.0) are reachable — ✅

| §5.0 concept | Derivable from | Source (verified) |
|---|---|---|
| **The ordered committed-chord stream over a region** | L4 decoder OR region chord results | `chord/chordslicedecoder.h` `SliceChord` (`hasChord`, `decision` Commit/Inherit/Abstain, `chosen` = `ChordSliceCandidate{rootPc,quality,bassPc,…}`) :380; **or** `region/harmonicrhythm.h` `HarmonicRegion` (`chordResult`, `alternatives`, `temporalExtensions`) :78 |
| **The key (L3 region key)** | region key | `HarmonicRegion::keyModeResult` (`KeyModeAnalysisResult{keySignatureFifths, mode, tonicPc}`) `keymodeanalyzer.h:97` |
| **Prevailing harmony** (nearest metrically-strong committed chord) | slice metric weight (§3) | `scoreharvest/metricweights.h` `regionMetricWeightForOnsetTick`/`…ForBeatType` ([0.5,1.0], 1=downbeat); also `HarmonicRegion::temporalExtensions.regionMetricWeight` and `FocalNote::metricWeight` (chordslicedecoder.h:424) |
| **Established next function** (next committed non-abstained) | the same stream | next `SliceChord` with `decision==Commit` / next committed `HarmonicRegion` |

Both production-shaped producers expose root + quality + committed-flag + metric-weight + tick span, so "the
progression", "prevailing harmony", and "established next function" are all derivable from existing data. The
**cadence-anchored** fallback for "established next function" depends on the cadence detector (Step 2) — noted, not
needed at Step 1.

### (b) The base-RN reuse (§5.1) — ✅ consumable as a library, no duplication forced

- `region::diatonicDegreeForRootPc(rootPc, keyFifths, keyMode)` (`region/sparsechordrefinement.{h,cpp}`, namespace
  `mu::composing::analysis::region`) — the scale-degree (0..6, −1 chromatic). **Note the nested `region::` namespace**
  (a build-time qualification fix; Step-0 had recorded it correctly).
- `ChordSymbolFormatter::formatRomanNumeral(const ChordAnalysisResult&)` (decl `chord/chordanalyzer.h:721`, def
  `chord/chordsymbolformatter.cpp:827`) — the **full** numeral: degree case-marking, chromatic alteration (`bVII`…),
  precise quality + seventh type, figured-bass inversion (`6`,`64`,`65`,`43`,`42`), augmented-sixth nationality, and
  the inline applied label (`V7/x`, `viio/x`) when `function.nextRootPc` is set.
- **Conversion is direct:** `KeyModeAnalysisResult` gives `keySignatureFifths` → `diatonicDegreeForRootPc`, `mode` →
  `function.keyMode`, `tonicPc` → `function.keyTonicPc`. So L5's base RN is a **faithful wrap** — fill
  `result.function.{degree,keyTonicPc,keyMode,nextRootPc}`, call the one formatter. **No gap forces a second formatter.**

### (c) Placement — ✅

New dormant units land in `src/composing/analysis/function/` beside `tonicizationlabeler` (per Step-0 §3), namespace
`mu::composing::analysis` (matching `tonicizationlabeler` and the reused `region::`/`ChordSymbolFormatter`). The
misnamed predecessor `harmonicfunctionlayer` (the chord-identity **competition** pipeline) is **NOT** touched — its
rename is an engage-step structural item.

**No input unreachable, no duplicate formatter forced, no structural change beyond the dormant module → proceeded.**

---

## §2 — The progression model (§5.0), dormant — `function/functionprogression.{h,cpp}`

Pure predicates over the committed-chord stream; **no cadence, no resolution decisions, no constants**.

- **Types (producer-agnostic view):** `ProgressionChord{rootPc, quality}` (the "function" the licensing test reasons
  over), `ProgressionSlice{chord, committed, metricWeight, startTick, endTick}`, `Progression = vector<ProgressionSlice>`
  (one region). Mapped from the L4 `SliceChord.chosen` or the region `chordResult` at engage; the predicates read no
  producer type (the module compiles free of the decoder/region headers).
- **Licensed-progression test** (`isLicensedProgression`) — the enumerable §5.0 successions, OR'd, each a named
  sub-predicate reusing the existing root-motion arithmetic **as a licensing boolean, not a score term**:
  - `isDescendingFifth` — `(to−from) mod 12 == 5` (the `wSeqBonus` arithmetic);
  - `isDescendingThird` — `∈ {8,9}`;
  - `isAscendingSecond` — `∈ {1,2}` (the minor-second case = leading-tone step, the `wDimBonus` delta==1);
  - `isAppliedResolution` (quality-aware) — applied dominant (Major a P5 above target), secondary leading-tone
    (Diminished a semitone below a major/minor target), half-dim pre-dominant up a P4 to a major target — the
    `resolutionEdgeBonus` dim/half-dim arithmetic.
- **Stream queries:** `isMetricallyStrong` (local metric-weight maximum, parameter-free), `prevailingHarmonyIndex`
  (nearest committed metrically-strong slice at/before i), `establishedNextFunctionIndex` (next committed non-abstained).

**Build-detail decisions (declared, not assumed — §6 below):** the cadential-motion clause and the cadence-anchored
next-function fallback are deferred to Step 2; the augmented→same-root resolution edge is excluded from §5.0 licensing;
"metrically strong" is realized as a parameter-free local maximum.

---

## §3 — The base Roman-numeral derivation (§5.1), dormant — `function/functionromannumeral.{h,cpp}`

- `BaseRomanNumeralInput{identity, keyFifths, keyMode, keyTonicPc, nextRootPc}` → `BaseRomanNumeral{label, degree,
  diatonicToKey}`.
- `deriveBaseRomanNumeral` assembles a `ChordAnalysisResult` (identity passed straight through; degree from
  `region::diatonicDegreeForRootPc`; keyTonicPc/keyMode/nextRootPc set), then calls the **one**
  `ChordSymbolFormatter::formatRomanNumeral`. Deterministic; introduces no judgment beyond the key+chord given (§5.1).
  Full DCML completeness comes for free from the wrapped emitter (incl. the inline applied label); the §5.6 precedence /
  Neapolitan-as-`bII6` / modal-mixture-as-residual refinements are Step-5 work **on top of** this emission, not a second
  formatter.

---

## §4 — Constants

**None.** The progression model is an enumerable rule set; the base RN is deterministic. No weight/threshold/margin was
introduced. (The parameter-free "metrically strong" = local-maximum avoids a strong-beat cutoff constant.)

---

## §5 — Tests (oracle-asserted) — +17

`tests/functionprogression_tests.cpp` (10) — asserted against theory, not analyzer echoes:
- a descending-fifth (V→I) is **licensed**; an applied-chord resolution (V/V→V, viio/V→V, Dø7→G) is **licensed**;
- an arbitrary non-functional tritone leap (C→F#) is **not** licensed; descending-third (I→vi) and ascending-second
  (IV→V, vii→I) are licensed; same-root (incl. the augmented same-root edge) is **not** a licensed progression; a
  missing root licenses nothing;
- `prevailingHarmonyIndex` resolves to the nearest committed metrically-strong slice at/before (passing tones heard
  against the downbeat); a **strong-but-abstained** slice is **skipped** (prevailing harmony must be committed);
  out-of-range → −1; `establishedNextFunctionIndex` skips abstained slices and returns −1 at the end.

`tests/functionromannumeral_tests.cpp` (7):
- the correct full numeral: `V` (G triad in C), `V7` (G7), `V6` (G/B), `V65` (G7/B), chromatic `bVII` (Bb in C), the
  applied `V7/V` (D7→G) and `viiø7/V` (F#ø7→G);
- **the wrap is faithful, not a re-derivation** — `deriveBaseRomanNumeral(…).label` equals a direct
  `formatRomanNumeral` call on a hand-built result (diatonic + chromatic paths); a rootless input yields degree −1
  (honest, not guessed).

(One fixture was sharpened after a first run: the original `SkipsAbstained` fixture set the abstained slice and the weak
slice to equal weight, so the weak slice became a local-max by the ≥-rule and returned itself — a pathological tie, not
a mechanism bug. Rebuilt as a strong-but-abstained-slice-must-be-skipped test; all 17 then green.)

---

## §6 — Gate — PASS (dormant + byte-identical)

| Gate | Result |
|---|---|
| Build | clean (`build_step1c.log`, no error/FAILED) |
| `composing_tests` | **895/895** (878 + 17; 2 disabled pre-existing) |
| `notation_tests` | **53** passed (4 skipped — baseline) |
| `pipeline_snapshot_tests` | **11/11** PASSED, **NO golden refresh** (1 skipped pre-existing) |
| Corpus **53/24/53** | **unchanged by construction** — not re-measured (see below) |
| Production reach | **none** — grep of `src/` + `tools/` finds the new identifiers only in the two module files, the two test files, and the two CMakeLists |

**Why the corpus regen was not run** (consistent with the session-9 phrase-boundary precedent + CLAUDE.md scoping): the
new module has **no production consumer** (verified by grep), touches **no** scoring/gate/template code, and the pipeline
snapshots refreshed **zero** goldens — so P1–P4 output is byte-identical and the BIR gate cannot move. The corpus-regen
gate is scoped to gate/scoring changes; this is neither.

---

## §7 — Declared to Cowork (build-detail decisions surfaced, not assumed)

1. **Augmented→same-root resolution edge excluded from §5.0 licensing.** `resolutionEdgeBonus` has three edges
   (dim→Maj/min a semitone up; half-dim→Maj up a P4; **aug→Maj/min same root**). The first two are genuine
   leading-tone/applied resolutions and ARE in `isAppliedResolution`. The aug→same-root edge (delta 0) is **excluded**:
   §5.0 frames a licensed progression as a **root motion**, and same-root is no motion (an augmented triad is also not an
   applied/leading-tone chord). It is the **only** resolutionEdge case not already subsumed by the diatonic intervals,
   so this is the one place the licensing set could differ. **Confirm** whether Cowork intends the aug-resolution edge
   inside §5.0 licensing.
2. **"Metrically strong" = parameter-free local maximum** (metricWeight ≥ both onset-neighbours; out-of-region = −∞),
   mirroring `phraseboundaryview` §4.4's structural-peak convention — chosen to honour §4 ("no thresholds at this step").
   Known edge behaviour (documented in the header): a plateau of equal weights counts all-strong, and a region's FINAL
   slice counts strong whenever ≥ its one in-region neighbour. Both are rare in real metric grids and harmless while
   dormant. **Refine to a beat-grid-aware test at engage if the cadence/resolver need it.**
3. **`isAppliedResolution` is enumerated in `isLicensedProgression` though (by theory) subsumed** by the descending-fifth
   + ascending-second motions — kept explicit to mirror §5.0's four-clause enumeration and to expose the quality-aware
   sub-predicate the Step-3 resolver consumes ("resolves as a licensed leading-tone or applied chord to its target").
4. **Namespace + placement:** the new units use `mu::composing::analysis` (matching `tonicizationlabeler` and the reused
   `region::diatonicDegreeForRootPc` / `ChordSymbolFormatter`), not `mu::composing::function` (held by the misnamed
   `harmonicfunctionlayer`, untouched). The function/ consolidation + rename remain Phase-5d structural items.

---

## §8 — Stops — none triggered

Base-RN reuse was possible (no second formatter); progression inputs reachable; only a dormant module added; production
byte-identical; no threshold/weight tuned; no `upstream` touched.

## Commits
- `f32688951d` — `docs(cowork): L5 build plan + Step-0 F1/F2 resolutions` (incl. F6 fix).
- `811272bdd1` — `feat(function): L5 progression model + base Roman-numeral derivation (Phase 5c Step 1, dormant)`.
