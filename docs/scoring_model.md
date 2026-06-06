# Chord Analyzer Scoring Model

> **Read this at the start of any session that touches scoring logic in
> `src/composing/analysis/chord/chordanalyzer.cpp`.** It exists because three
> consecutive template-addition attempts (B1, B2 ×4, B3) were slowed by
> incomplete understanding of how the scoring pipeline works as a system. The
> code captures *what* each term does; this document captures *why* it exists
> and how the terms interact.

This is a reference document for the rule-based chord analyzer's scoring
pipeline. It covers the templates, every additive bonus / penalty term, the
post-scoring gates, the inversion-correction pass, and the load-bearing
invariants that future changes must respect.

---

## 1. Overview

`RuleBasedChordAnalyzer::analyzeChord` is a **bottom-up** vertical-sonority
scorer: pitch-class evidence → chord identity. It performs no harmonic-function
reasoning (that lives in Phase E — secondary dominants, tonicization, etc.).

The pipeline is:

1. **Tone collection.** Build a 12-element pitch-class weight histogram from
   the input tones; pick bass candidate(s) by lowest pitch + onset evidence.
2. **Template scoring.** For each `(rootPc, templateIdx, bassPc)` triple
   (12 × 17 × |bassCandidates|), compute a score using:
   - a bass-independent base (template-tone fit, extras, structural penalties,
     TPC consistency, diatonic bonus, dim7 characteristic, root continuity,
     resolution bias),
   - a bass-dependent delta (bass-root bonus, inversion bonuses),
   - joint terms (`w_complete`, `w_stepIn`, `w_stepOut`, `w_seq`, `w_dim`).
3. **Ranking.** Sort by score descending, then by template tie-priority, then
   by `rootPc`. The winner determines the working bass.
4. **Result building.** Build up to 3 `ChordAnalysisResult` entries, applying
   post-scoring quality normalization (augmented root correction, Sus2→Sus4
   upgrade, Sus→Major with `omitsThird`, extension detection, degree).
5. **Guaranteed inversion alternative.** When the winner is bass-rooted and no
   different-`rootPc` candidate made the top-3, append the next best one so
   the post-ranking correction has something to work with.
6. **Post-scoring gates (A through L).** Inversion correction, enharmonic
   flips (Minor-add6 ↔ HalfDim7), augmented-rotation correction, Gate I
   (first-inversion major over root-position minor), Gate J (vii° → V7),
   Gate K (first-inversion augmented), Gate L (Major over augmented).
7. **Late promotions.** Iter 86 bass-b7 promotion, Iter 91 bass-as-root
   promotion.
8. **Pedal point check.** Two-pass: if the bass is not a chord tone of the
   Pass 1 winner and the upper voices form a confident chord on their own,
   replace with the Pass 2 result and flag `isPedalPoint`.

The analyzer is purely bottom-up — it does not know about secondary dominants,
modulation, or progression context beyond a single chord's neighbours.

---

## 2. Templates

The analyzer scores each candidate against a fixed array of 17 chord templates
(`std::array<TemplateDef, 17>` in `analyzeChord` at ~L1955 and mirrored as
`kDiagTemplates` at ~L3381). Each template carries an intervals list (semitone
offsets from root) and parallel TPC deltas (circle-of-fifths distance).

| # | Quality          | Intervals      | Represents                          | Notes |
|---|------------------|----------------|-------------------------------------|-------|
| 0 | Major            | `{0,4,7}`      | Major triad (C)                     | |
| 1 | Major            | `{0,4,7,11}`   | Major 7th (CMaj7)                   | |
| 2 | Major            | `{0,4,7,10}`   | Dominant 7th (C7)                   | |
| 3 | Major            | `{0,4,6,10}`   | Dom7♭5 / Lydian dom (C7♭5 / C7♯11) | Penalised w/o TPC confirmation of ♭5 spelling; penalised when m7 absent (see §4 structural penalties). |
| 4 | Minor            | `{0,3,7}`      | Minor triad (Cm)                    | |
| 5 | Minor            | `{0,3,7,10}`   | Minor 7th (Cm7)                     | Non-bass penalty `-kNonBassPenalty` (0.35) when root ≠ bass (waivable by full TPC match). |
| 6 | Diminished       | `{0,3,6}`      | Diminished triad (C°)               | `dim7CharacteristicBonus` (+0.75) fires on the dim7 PC, gated on full triad evidence + non-diatonic ♭♭7. **Rotation-selection mechanism** — see §4. |
| 7 | Suspended4       | `{0,5,6,10}`   | Sus4♭5 (Csus4♭5)                    | Precedes HalfDim (tie-break): same PC set, sus4 reading is preferred when the ♭5 is enharmonically ambiguous. Excluded from sus4-missing-P4 penalty (the tritone is the identifying interval). |
| 8 | HalfDiminished   | `{0,3,6,10}`   | Half-diminished 7th (Cø7)           | Non-bass penalty (waivable by TPC); shares PC set with Sus4♭5. |
| 9 | Augmented        | `{0,4,8}`      | Augmented triad (C+)                | Symmetric (3 enharmonic rotations); thin-evidence `augFactor` halves the score for sparse / bare-root cases. |
| 10| Augmented        | `{0,4,8,10}`   | Augmented dom7 (C7♯5)               | **B2 dual guard:** BOTH M3 (rootPc+4) AND aug5 (rootPc+8) must be present above `extensionThreshold`. Added 2026-06-05. |
| 11| Suspended2       | `{0,2,7}`      | Sus2 (Csus2)                        | Upgraded to Sus4 in post-scoring when P4 is sounding. |
| 12| Suspended4       | `{0,5,7,10}`   | Sus4 + m7 (C7sus / C7sus4)          | Penalised when defining P4 absent. |
| 13| Suspended4       | `{0,5,7,11}`   | Sus4 + Maj7 (CMaj7sus)              | Penalised when P5 absent. Often re-qualified to `Major + OmitsThird`. |
| 14| Suspended4       | `{0,5,8,10}`   | Sus4♯5 (Csus♯5)                     | Sus4-variant: penalised when m7 absent. |
| 15| Suspended4       | `{0,6,7}`      | Sus♯4 (Csus♯4 / Lydian fragment)   | TPC delta +6 = F♯ spelling, not G♭. |
| 16| Power            | `{0,7}`        | Power chord (C5)                    | Penalised when distinctPcs ≥ 3 (`kPowerChord3PcPenalty = 0.30`); excluded from step bonuses. |

**Template ordering matters.** When two candidates score identically, the
template with the lower index wins (`RawCandidate::tiePriority` is the
template index; the comparator at ~L2412 prefers lower values). Key
intentional placements:

- Sus4♭5 (7) precedes HalfDim (8): identical PC sets, Sus4♭5 wins ties.
- Min7 (5) follows Minor triad (4) and precedes Sus4 templates.
- Plain triads precede their 4-note extensions.

`kDiagTemplates` in `diagnoseChord` (~L3381) must remain byte-identical to the
`analyzeChord` template array. `diagnoseChord` intentionally **omits the
production guards** (B2 dual guard etc.) so every cell appears in the
diagnostic breakdown — guards are production-only.

---

## 3. Score matrix structure

The bass-independent terms are computed once per `(rootPc, templateIdx)` and
stored in three 12 × 17 matrices declared at ~L2014–L2016:

- **`basisIndepMatrix[rootPc][tplIdx]`** — additive base score:
  `scoreTemplateTones + scoreExtraNotes + dim7CharacteristicBonus
  + structuralPenalties + tpcConsistencyBonus
  + bassIndependentContextualBonuses` (diatonic root, root continuity,
  resolution bias).

- **`complexityFactorMatrix[rootPc][tplIdx]`** — *multiplicative* template-
  complexity preference (Iter 74 Fix A). `evidenceRatio < 0.5` discounts the
  score (0.5 + ratio); `≥ 0.5` leaves it unchanged. This pushes the scorer
  away from 4-note templates when only 2 PCs are sounding.

- **`augFactorMatrix[rootPc][tplIdx]`** — *multiplicative* augmented-only
  thin-evidence penalty (Iter 78 Fix C + Iter 79). Halves the score for
  augmented templates with sparse / bare-root evidence.

The final per-bass score is:

```
score = (basisIndep + bassDep) × complexityFactor × augFactor
      + wCompleteBonus + wSeqBonus [+ wDimBonus] [+ stepIn + stepOut after Pass B]
```

**Atomic update requirement.** All three matrices have `17` as their column
extent. When adding a template the array sizes change to 18 across:
- `analyzeChord` template array,
- `kDiagTemplates`,
- all three score matrices.

Missing the score matrices produces a silent stack-buffer overrun (B1 attempt
2026-06-04). The compiler does not catch this — the matrices are sized by
literal, so the array bound is loose and the cells just get garbage. Always
update the four sites together.

---

## 4. Bonus and penalty terms

### `dim7CharacteristicBonus` — `kDim7CharacteristicBonus = 0.75`

**Definition (chordanalyzer.cpp:1117).** Applied per `(rootPc, tplIdx)` for
Diminished templates when:

1. The `dim7 PC` (rootPc + 9) is sounding above `extensionThreshold`.
2. The full diminished triad is present (root, ♭3, ♭5 all above threshold).
3. The dim7 PC is **non-diatonic** to the current key.

**⚠ ROTATION-SELECTION MECHANISM — not a simple offset.**

All four enharmonic rotations of a dim7 chord share the same PC set
(C°7 = E♭°7 = G♭°7 = A°7). Pure template scoring cannot distinguish them.
The non-diatonic ♭♭7 check asymmetrically rewards the **correct** rotation:
the ♭♭7 of the true rotation is non-diatonic in the current key, while the
♭♭7 of the three spurious rotations coincides with a diatonic scale tone and
gets no bonus.

**Do not suppress or bypass this bonus** without replacing the rotation
selection. The B3 attempt (2026-06-05) tried adding a dedicated 4-tone
Diminished `{0,3,6,9}` template and suppressing this bonus to avoid double-
scoring — result: 6 Jazz catalog dim7 rotations selected the wrong root, and
a `bach_chorale_003` snapshot regression appeared as an indirect segmentation
side effect. Deferred. Future attempts must either (a) replicate the non-
diatonic-♭♭7 check inside the new template guard, or (b) replace the bonus
with an equivalent mechanism.

### `rootContinuityBonus` — `prefs.rootContinuityBonus = 0.40`

Applied by the competition pipeline `applyHarmonicFunction()`
(`harmonicfunctionlayer.cpp`) when `ctx.previousRootPc == rootPc`, added into
`basisIndep` before the complexity x aug multiply. Rewards continuing the same
root across adjacent regions. It is a **progression signal, not vertical pitch
evidence**: as of the scoring-oracle / competition-pipeline split (see section 11)
the scoring oracle `analyzeChord()` no longer folds it into `basisIndep`. (The
`diagnoseChord` diagnostic path still adds it inline via `contextualBonuses`.)

**Known dead end (Iter 98, 2026-05-23).** Gating this bonus off a sparse
predecessor (e.g. `previousRegion.distinctPcs <= 2`) was tried in two variants
and both regressed `mozart_k280-1` IV→V65 in Alberti-bass contexts. The signal
is load-bearing for legitimate sparse continuity (broken-chord bass with held
upper voices). Do not attempt a density-based or inversion-aware gate here
without re-reading the Iter 98 dead-end section in `COWORK_HANDOFF.md`.

### `w_complete` — `kWComplete = 0.50`

Lambda at chordanalyzer.cpp:~L2084. Fires when:

- `jointScoringEnabled` (region came from `collectRegionTones`),
- `candBassPc == rootPc` (root position),
- `distinctPcs == 3` (exactly three PCs in the region),
- all three triad tones (root, third, fifth per quality) present above the
  `kPresenceThreshold` (0.05).

Reward: root-position complete triads outrank slash-chord readings of the
same PC set (closes Bug 2 — bwv310 m8 b3 Em/C vs C major). Iter 90's
regression mode (slash chord with missing fifth) is excluded because an
absent tone has `pcWeight == 0` which fails the presence check.

### `w_stepIn` / `w_stepOut` — `kWStepIn = kWStepOut = 0.10`

Lambdas at chordanalyzer.cpp:~L2157 and ~L2165. Reward root-position
candidates whose root participates in semitone / whole-tone bass motion from
the previous region (`stepIn`) and/or to the next region (`stepOut`).

**Four gates (each load-bearing):**

1. **`!prefs.explorationMode`** — suppresses the bonus inside
   `greedyExpandSegmentation` boundary exploration. Without this, segmentation
   biases sub-region bass selection toward stepwise candidates and redirects
   segmentation before the final per-region scoring pass runs.

2. **`candBassPc == rootPc`** (root-position only) — the bonus rewards "this
   chord's root moves smoothly in the bass line," not "this slash-chord's bass
   happens to step." Without this guard a slash-chord bass (e.g. F♯ in G♯m7/F♯)
   that steps to a neighbouring bass gets credit it shouldn't — caused the
   Iter 94 Jazz bwv430 regression (BIR=false 14→15).

3. **First-inversion m7-family surgical guard (Pass B)** — suppresses the
   bonus when a competitor of quality {HalfDiminished, Diminished, Minor7}
   sits a minor third below our bass and scores within `kStepBudget` (≈ 0.21)
   of our unbonused score. Canonical case: Dm6 vs Bø7/D — the step bonus
   would otherwise tip a fragile m6 root-position reading over an equally
   viable first-inversion m7-family reading on identical pitch evidence.

4. **Power-quality exclusion (Pass B)** — Power chords get no step bonus. A
   root+5-only template gaining +0.20 would tip past viable triads in sparse
   Jazz tonic-on-strong-beat contexts (5 of 6 corrected-guard Jazz BIR=true
   regressions were `[Tonic]5` reads vs WiR `I` triads).

Removing any single gate above triggers a documented regression. Do not
simplify without understanding the specific failure each one prevents.

### `w_seq` — `kWSeq = 0.20`

Lambda at chordanalyzer.cpp:~L2190 (Iter 95). Fires when:

- `jointScoringEnabled`, `!explorationMode`, `context` available,
- `context->nextRootPc >= 0`,
- `distinctPcs >= 4`,
- the next region's root sits a perfect fourth above the candidate root
  (`(nextRootPc - candRootPc) mod 12 == 5`).

Reward: classic V → I descending-fifth root motion. This is a **chord-level**
signal: any inversion of the candidate qualifies (the bonus does NOT require
`candBassPc == candRootPc`), and the m7-family surgical guard does NOT apply
(sequential root motion is about root identity, not bass).

### `w_dim` — `kWDim = 0.15`

Lambda at chordanalyzer.cpp:~L2209 (Iter 96). Fires when:

- `jointScoringEnabled`, `!explorationMode`, `context` available,
- `context->nextRootPc >= 0`,
- quality is `Diminished` or `HalfDiminished`,
- `distinctPcs >= 4`,
- candidate root sits one semitone below `nextRootPc` (leading-tone-of-next).

Reward: vii°7 → I leading-tone resolution. Acts as a tiebreaker between
enharmonic dim7 rotations when context is available.

**`distinctPcs >= 4` is intentional.** 3-PC sparse dim regions must not flip
quality via this bonus. The bonus is a rotation-correction signal (correct
spelling among the four enharmonic rotations), **not** a quality-flip signal.
Removing this gate caused quality flips in 3-PC contexts during Iter 96
testing.

**Post-bonus quality guard (Iter 97a-v3).** The analyzer maintains two
parallel global scorings (with-wDim and without-wDim) and, after the loop,
inspects the with-wDim global winner. If its quality is not Dim/HalfDim, the
bonus caused cross-bass contamination — fall back to the without-wDim result.
Both variants run Pass B (step bonus + surgical guard) independently.

### B2 aug7 guard

In the `(rootPc, tplIdx)` loop at chordanalyzer.cpp:~L2026. Skips the 4-tone
Augmented template (#10, `{0,4,8,10}`) for any root where **either** M3
(rootPc+4) **or** aug5 (rootPc+8) is at or below `extensionThreshold`. The
`||` (fire if EITHER is absent) means BOTH must be present for the template
to score.

**M3-only relaxation has been tried and reverted.** Using `&&` (skip only
when both absent — i.e. fire when M3 alone is present) lets the aug7 template
over-fire on complete major triads containing a minor seventh: with only
root+M3+m7 present, the large aug5 score offset (+8) still inflates the
partial-match score above a complete major triad. Schumann D-major and
Corelli G-major snapshots flipped to aug7 under the relaxed guard. The dual
`||` is correct and load-bearing.

### `explorationMode` flag (ChordAnalyzerPreferences)

`bool explorationMode = false` (chordanalyzer.h:~L451). Set `true` by
`greedyExpandSegmentation` for internal boundary-exploration `analyzeChord`
calls (Round 1 head/tail synthesis + Round 2 region scoring in
`harmonicsegmenter.cpp::fillGap`).

Suppresses all context-dependent bonuses that would otherwise bias sub-region
bass selection during segmentation, before the final per-region scoring pass
runs: `w_stepIn`, `w_stepOut`, `w_seq`, `w_dim`. Final per-region calls
(bridge / batch_analyze callers, after segmentation returns boundaries)
leave the flag at `false`.

Do not remove this flag without designing a different way to keep
segmentation-internal scoring stable.

### Other terms (briefly)

| Term                                  | Value         | What it does |
|---------------------------------------|---------------|---|
| `bassNoteRootBonus`                  | 0.70          | Awarded when `rootPc == bassPc`, multiplied by `bassRootBonusMultiplier` (1.0 full triad, 0.3 third-only or root+5, 0.1 bass alone). |
| `diatonicRootBonus`                  | 0.30          | Awarded when root is a scale member of the current key. |
| `tpcConsistencyBonusPerTone`         | 0.20          | Per non-root template tone whose authored TPC matches the expected delta. |
| `resolutionBonus`                    | 0.35          | Awarded on `prevDim→Maj/min` semitone-up, `prevHalfDim→Maj` P4-up, `prevAug→same-root`. |
| `stepwiseBassInversionBonus`         | 0.50          | Inverted Maj/Min with bass stepwise from previous region's bass. |
| `stepwiseBassLookaheadBonus`         | 0.50          | Inverted Maj/Min with bass stepwise to next region's bass. |
| `completeTriadInversionBonus`        | 0.45          | All three triad tones present in a 3-PC texture; inverted reading. |
| `sameRootInversionBonus`             | 0.40          | Inverted candidate whose root matches the previous region's root. |
| `maxTotalInversionContextBonus`      | 2.0 (B 2.5 / J 0.6) | Cap on the sum of the four inversion bonuses above. |
| `kNonBassPenalty`                    | 0.35          | Min7 / Sus4 / HalfDim with root ≠ bass; waived when every non-root TPC matches. |
| `kSus4MissingFourth`                 | 0.70          | Sus4 (excluding Sus4♭5) without P4 above 0.50. |
| `kSus4VariantMissing7th`             | 0.70          | Sus4♭5 / Sus4♯5 without m7. |
| `kSus4Maj7MissingP5`                 | 0.50          | Sus4+Maj7 without P5. |
| `kDom7FlatFiveTpcPenalty`            | 0.55          | Dom7♭5 without explicit G♭ TPC confirmation. |
| `kDom7FlatFiveMissing7th`            | 0.50          | Dom7♭5 without m7. |
| `kPowerChord3PcPenalty`              | 0.30          | Power chord with `distinctPcs >= 3`. |
| `kRootToneFactor / kSecondToneFactor / kOtherToneFactor` | 1.8 / 1.2 / 1.0 | Per-position weights in `scoreTemplateTones`. |
| `kExtensionFactor7th / Flat13 / Default` | 0.45 / 0.20 / 0.35 | Per-rel-interval extension weights in `scoreExtraNotes`. |
| `kContradictionPenalty`              | 0.75          | Non-template pc that contradicts the template quality. |
| `kForeignPenalty`                    | 0.45          | Non-template pc that is neither extension nor contradiction. |

---

## 5. Joint (bass, root, template) scoring

Pre-Iter 92 the analyzer committed to a single bass (the lowest qualifying
pitch) before scoring. Two coupled bugs forced the joint model:

- **Bug 1 (bwv103.6 m3 b2):** a passing eighth note that happens to be the
  absolute lowest pitch in the region won bass selection over the beat-onset
  bass a step above it.
- **Bug 2 (bwv310 m8 b3):** a slash-chord reading (Em/C) outscored the
  root-position triad (C major) because the bass-root bonus + complete-triad
  evidence on C had no way to flip the global ranking.

**Iter 92 design.** Enumerate multiple bass candidates and score the full
12 × 17 grid against each, then pick the global best `(rootPc, tplIdx,
bassPc)` triple.

**Bass-candidate enumeration** fires only when there is musical evidence the
bass voice moves within the region:

- At least one candidate with `onsetAtRegionStart == true` AND at least one
  with `false` (distinguishes the bwv103.6 case from static SATB textures),
  **OR**
- `sparseUpperRegisterAmbiguous`: `distinctPcs <= 2`, ≥ 2 regional candidates,
  and `lowestPitch > 60` — Corelli op01n08d m2 b3 fallback for upper-register
  G + B with bass continuo resting.

Otherwise the analyzer falls back to legacy single-bass selection.

**`hasStructuralBass`** (~L1935). True when `lowestPitch <= 60` (middle C) OR
`distinctPcs >= 3`. Passed into `bassDependentContextualBonuses` to gate the
inversion bonuses — sparse upper-register "bass" notes are not real bass
voices and must not trigger inversion bonuses (Corelli op01n08d m2 b3).

`bassDependentContextualBonuses(tpl, rootPc, bassPc, appliedBassBonus,
distinctPcs, pcWeight, prefs, context, hasStructuralBass)` returns
`appliedBassBonus + min(stepwise+lookahead+sameRoot+completeTriad,
maxTotalInversionContextBonus)`. The cap prevents runaway stacking.

---

## 6. Post-scoring gates (A–L)

These run after `results[]` is populated and the optional guaranteed-
inversion-alternative is appended. They modify ranking via `std::swap` and
`std::stable_sort` — they do not change the underlying scores in
`rawCandidates`.

**E3 (2026-06-06): execution location.** Gates A–L are implemented in
`applyPostScoringGates()` (declared in `chordanalyzer.h`, defined in
`chordanalyzer.cpp`). `analyzeChord()` no longer runs them internally; instead
it publishes the inputs the gates need (`pcWeight`, `tpcForPc`, `scale`,
`keyTonicPc`, `keyMode`, `bassPc`, `bassTpc`, `distinctPcs`, `threshold`,
`rawCandidates`) via the optional `PostScoringGateContext* gateCtxOut`
out-parameter. Production call sites in `regionanalyzer.cpp` (Pass 1, Pass 2,
Pass 2b), `harmonicsegmenter.cpp`, the notation bridges, and `inferNextRootPc()`
call `applyPostScoringGates()` *after* `applyHarmonicFunction()`. Tests use the
`analyzeWithGates()` helper in `test_helpers.h`. The line numbers in the table
below reference the corresponding code inside `applyPostScoringGates()`.

| Gate | Location | Trigger | Effect | Why it exists |
|------|----------|---------|--------|---------------|
| **Bias correction** | ~L2639 | Winner is bass-root Maj/Min, margin to best Maj/Min alt < `inversionSuspicionMargin` (0.70), `distinctPcs >= 3`. Seventh-exempt. | Deducts the bass-root bonus from the winner, re-sorts. | Bass-root bonus systematically over-fires on inversions; the correction removes the bonus only when it is the sole deciding factor. |
| **A–D (Minor-add6 ↔ HalfDim7 enharmonic flip)** | ~L2733 | `preferMinorOverMajorAdd6`, winner is Major+AddedSixth, alt is Minor at `(rootPc+9)%12`. Temporal gates B/C/D check for forward / stepwise / consecutive evidence. | Swap to the Minor alt; or pull the Minor alt from `rawCandidates` (FM2 fallback). | The two readings span identical PCs (e.g. Bb6 = Gm7/Bb); score cannot reliably distinguish in bass-heavy textures. Standard/Baroque prefer Minor. |
| **E (first-inversion Minor → Major)** | ~L2820 | `preferMinorOverMajorAdd6`, winner Minor, alt Major at `(rootPc+8)%12`, stepwise bass present. | Swap. | F♯m winning when D/F♯ is correct (bass = M3 of actual root). |
| **F (second-inversion → root-position Major)** | ~L2842 | Alt Major at `(rootPc+5)%12`, stepwise bass. | Swap. | Bass = P5 of actual root; B winning when E/B is correct. |
| **G-E / G-B / G-C / G-D (Minor-add6 ↔ HalfDim7)** | ~L2907 | `originalWinnerQuality == Minor && originalWinnerHasAddedSixth`, HalfDim7 at `(originalWinnerRootPc+9)%12`. G-E gates on key-function (viiø7/iiø7/iiiø7); G-B/C/D on temporal context. | Pull HalfDim from `rawCandidates` if missing; swap to HalfDim. | Sub-9a fix (`originalWinnerRootPc` capture). Cm6 vs Aø7/C is enharmonic; functional context selects the correct reading. |
| **H (augmented rotation)** | ~L2992 | Winner Augmented bass-root, `preferMinorOverMajorAdd6`, alt Augmented at `(rootPc+4)%12` or `(rootPc+8)%12`. Temporal gates. | Swap. | Augmented triads have 3 enharmonic rotations; context picks the correct one. |
| **I (first-inversion Major over root-position Minor)** | ~L3044 | Winner Minor bass-root, alt non-root-position chord with same bass, root at I4 interval below bass, root diatonic, margin ≤ 0.45. | Swap. | Em winning when C/E is correct. |
| **J (vii° → V7 completion)** | ~L3151 | Winner is root-position Diminished triad (no dim7), the M3-below PC is sounding above `extensionThreshold`, alt is Major+m7 rooted there. | Swap to the dominant-7th reading. | Four PCs `{R-4, R, R+3, R+6}` are exactly V7 — a root-position vii° voicing the dominant root is, by construction, V6/5. |
| **K (first-inversion Augmented)** | ~L3080 | Winner Augmented bass-root, alt at I4 interval, alt root diatonic, margin ≤ 0.20. | Swap. | bwv40.6 m=6: A+ → F♯5/A. |
| **L (Major over Augmented same-root)** | ~L3117 | Winner Augmented (no 7th), alt Major at same root AND same bass, diatonic, margin ≤ 0.35. | Swap. | TYPE-A quality fix: bwv144.6 B+ → B, bwv245.15 E+ → E, etc. |

---

## 7. Inversion correction

The "bias correction" entry above (~L2867) deducts the bass-root bonus and
re-sorts via `std::stable_sort`:

```cpp
results[0].identity.score -= deduction;
std::stable_sort(results.begin(), results.end(), [](...){ ... });
```

After this sort, `results[0]` may be a different candidate than it was before
— the half-diminished alt (or a Minor alt at a different root) can have been
promoted.

### Pre-sort capture: `originalWinnerRootPc`

At ~L2647–L2651, **before** the sort can run:

```cpp
const ChordAnalysisResult& winner = results[0];   // LIVE reference
const ChordQuality originalWinnerQuality = winner.identity.quality;
const int originalWinnerRootPc = winner.identity.rootPc;
const bool originalWinnerHasAddedSixth = hasExtension(...);
```

`winner` is a **live reference** to `results[0]`. After the sort it points to
whatever ended up in slot 0. Gate G-E (~L2910) reads
`originalWinnerRootPc` to compute `gExpectedAltRoot = (originalWinnerRootPc
+ 9) % 12`.

**Sub-9a bug (fixed in `f3e0f5f72c`).** Before the fix, Gate G-E used
`winner.identity.rootPc` directly. After the bias correction sort promoted
Am7♭5/C (rootPc=9) to `results[0]`, the live `winner.identity.rootPc` read 9
instead of 0, producing `gExpectedAltRoot = 6` (F♯) and pulling in a dormant
F♯m7♭5 candidate. All 5 Sub-9a cases shared the same Cm6 → Am7♭5/C → stale-
root pattern. The fix is the pre-sort capture — `originalWinnerRootPc` is the
pre-sort root.

When adding a new gate that reads the original winner's properties, always
use the captured `originalWinner*` values, not `winner.identity.*`.

---

## 8. Known constraints and dead ends

These are load-bearing design decisions. Future changes must respect them or
risk regressions documented in `COWORK_HANDOFF.md` / `STATUS.md`.

- **`dim7CharacteristicBonus` is the dim7 rotation selector.** Do not
  suppress without replacing the non-diatonic-♭♭7 mechanism (B3 lesson).

- **`rootContinuityBonus` sparse-predecessor gate is a dead end** (Iter 98).
  Both density-based and inversion-aware variants tried; both regress
  mozart_k280-1 IV→V65 Alberti bass.

- **`w_stepIn`/`w_stepOut` has four gates, each load-bearing** —
  `explorationMode`, root-position guard, first-inversion-m7-family surgical
  guard, power-quality exclusion. Each prevents a specific documented
  regression.

- **`explorationMode` must suppress all context-dependent bonuses.** Step,
  seq, and dim bonuses all check this flag. Adding a new context bonus
  without checking `explorationMode` will cause segmentation regressions.

- **Template arrays and score matrices update atomically.** 4 sites:
  `analyzeChord` template array, `kDiagTemplates`, three score matrices.
  Missing the matrices → silent stack-buffer overrun (no compile error).

- **B2 aug7 guard requires BOTH M3 and aug5** (`||` not `&&`). M3-only was
  tried and reverted (Schumann D-major, Corelli G-major snapshot flips).

- **Gate thresholds are Baroque-calibrated.** Do not widen Baroque-tuned
  thresholds to accommodate Jazz or other styles (see CLAUDE.md "Gate
  threshold and preset policy"). Use a tighter structural guard or a
  preset-specific override instead.

- **`hasStructuralBass` gates inversion bonuses.** Sparse upper-register
  "bass" notes do not get inversion bonuses (Corelli op01n08d m2 b3).

- **Post-bonus winner quality guard for `w_dim`.** The bonus can rotate the
  global winner across bass candidates; if the post-bonus winner is not
  Dim/HalfDim, fall back to the without-wDim variant.

- **Pre-sort capture for original-winner gates.** Gates that compute against
  the pre-correction winner must read `originalWinner*` snapshots, not the
  live `results[0]` reference (Sub-9a lesson).

- **Joint scoring requires regional accumulation.** `jointScoringEnabled`
  fires only when at least one tone has `onsetAtRegionStart == true` or
  `distinctMetricPositions > 0` (i.e. came from `collectRegionTones`).
  Single-tick / status-bar / unit-test paths use the legacy single-bass path.

---

## 9. How to add a new template safely (checklist)

Derived from the B1, B2, and B3 lessons.

1. **Read the existing template nearest to yours.** Understand its intervals,
   TPC deltas, and which existing terms / guards apply to it.

2. **Identify interactions with bonus/penalty terms.** Does any existing
   bonus use the new template's quality+size as a key condition? Examples:
   - `dim7CharacteristicBonus` keys on `quality == Diminished`
   - `nonBassAdjustment` keys on Min7 / Sus4 (4-note) / HalfDim
   - `qualifiesForCompleteTriadInversionBonus` keys on Maj/Min/Dim/Aug/HalfDim
   - `supportsContextualInversionBonuses` keys on Maj/Min/Aug/HalfDim
   - `w_complete` requires plain triad quality (Maj/Min/Dim/Aug)
   - `w_stepIn/Out/seq/dim` have explicit quality filters

   If your new template shares a quality with an existing one (e.g. another
   Diminished template), check whether the existing term will double-fire on
   your new template.

3. **Subset / superset analysis.** Check whether the new template's PC set is
   a subset of common chord patterns:
   - Subset of a common Baroque progression → needs a functional guard
     (B1 lesson — bare `{0,3,7,11}` mMaj7 misread Baroque V → i as i(maj9)).
   - Superset / rotational equivalent of an existing template → consider
     enharmonic / rotation-selection implications (B3 lesson — `{0,3,6,9}`
     dim7 broke the existing rotation selector).

4. **Design the guard.** Decide what tones must be above
   `prefs.extensionThreshold`. Enumerate the known failure cases explicitly
   (catalog chords, snapshot test fixtures, BIR corpus targets).

5. **Update all 4 array sites atomically:**
   - `analyzeChord` template array (size N → N+1)
   - `kDiagTemplates` (size N → N+1)
   - `basisIndepMatrix`, `complexityFactorMatrix`, `augFactorMatrix` (column
     extent N → N+1, all three)

6. **Run all three test suites:**
   - `composing_tests.exe` (catalog: ground truth chord names)
   - `notation_tests.exe` (bridge + integration)
   - `pipeline_snapshot_tests.exe` (P1/P2/P3/P4 against golden JSON)

7. **Run BIR for both presets before committing:**
   - `python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus`
   - `python tools/analyze_inversion_errors.py`
   - `python tools/run_bach_preset.py --preset Jazz --output-dir tools/corpus`
   - `python tools/analyze_inversion_errors.py`

   Any BIR=false increase in either preset is a hard stop (CLAUDE.md gate-
   threshold policy).

8. **Document.** Add a row to §2 of this document for the new entry, noting
   any guard and the rationale. Update STATUS.md.

---

## 10. Harmonic function layer

**Module:** `src/composing/analysis/function/harmonicfunctionlayer.{h,cpp}`

A post-analysis pass that sits between `analyzeChord()` output and the final
chord label. Called from `regionanalyzer.cpp` after each non-exploratory
`analyzeChord()` call — gated on `!prefs.explorationMode` — at three sites:
Pass 1 (~L444+refinement), Pass 2 (~L637+refinement), Pass 2b (~L814+refinement).

`HarmonicFunctionContext` carries: `keyFifths`, `keyMode`, `previousRootPc`,
`nextRootPc`. Extended in E4 with phrase-boundary and cadence evidence.

**E1 (current):** Pass-through. No changes to `ChordAnalysisResult`.

**E2 (done):** The three progression signals (`rootContinuityBonus`, `w_seq`,
`w_dim`) no longer live in `chordanalyzer.cpp`. They are applied by the
competition pipeline `applyHarmonicFunction()`; see section 11.

**E3 (done, 2026-06-06):** Post-scoring gates A–L extracted from `analyzeChord()`
into `applyPostScoringGates()` (`chordanalyzer.cpp`). The new execution order at
every production call site is:

```
analyzeChord()              → pre-gate raw scoring + PostScoringGateContext out-param
applyHarmonicFunction()     → function-layer winner selection
applyPostScoringGates()     → identity corrections on the function-layer winner
[refinements]               → as moved in E2c
```

The function layer is still a no-op (E1), so the rearrangement is byte-identical
to the prior behavior. Once E2d-enable lands, the function layer will supply the
winner that the gates then correct — unblocking the gate-reversion failures
identified in E2c (Pass B step bonus, cross-bass cell promotion). The
bwv806_gigue Sus→Major case still needs verification during the E2d-enable v2
attempt.

**E4 (planned):** Cadence detection, tonic confirmation, functional label
completeness (secondary dominants, borrowed chords, augmented sixths).

**Rationale.** The scoring model §4 documents that `rootContinuityBonus`,
`w_seq`, and `w_dim` are progression signals (not pitch-evidence terms) and
that Gates A–L are functional-reasoning corrections on top of a pitch scorer.
Having them inside `analyzeChord()` couples functional reasoning to the
pitch-evidence scorer, making each new template addition risk unexpected gate
interactions (B1/B2/B3 history). The function layer provides the correct
architectural home for these terms.

---

---

## 11. Scoring oracle vs competition pipeline (E2d redesign)

Winner selection now has a single home. Two roles, two functions, one source of
truth.

**`analyzeChord()` — the scoring oracle.** Computes only what depends on the raw
tones and key. For every `(bass, root, template)` cell it evaluates `basisIndep`
(vertical pitch evidence, *without* any progression signal), `basisDep`
(bass-dependent delta, including the section 4.1b inversion bonuses and
`appliedBassBonus`), `complexityFactor`, `augFactor`, and `w_complete`. It also
computes the region metadata (`pcWeight`, `tpcForPc`, `scale`, `keyTonicPc`,
`keyMode`, `distinctPcs`, `jointScoringEnabled`). It packs all of this into a
`fn::ScoringSnapshot`, builds a `fn::HarmonicFunctionContext` from the temporal
context, and calls `applyHarmonicFunction()`. **It selects no winner and applies
no progression signal.**

**`applyHarmonicFunction()` — the competition pipeline**
(`harmonicfunctionlayer.cpp`). The sole owner of winner selection. In order:

1. Re-score every cell with `rootContinuityBonus` (added into `basisIndep` before
   the complexity x aug multiply), `w_seq`, and `w_dim`.
2. Pass B — `w_stepIn`/`w_stepOut` with the surgical first-inversion-m7-family
   guard (`applyStepBonusGuard`), run independently on the with-wDim and
   without-wDim variants.
3. The wDim post-bonus quality guard (with-wDim accepted only if its global
   winner is Diminished/HalfDiminished, else fall back to without-wDim).
4. Cross-bass winner selection (the highest-scoring cell across all basses, no
   field patching).
5. The de-inflated threshold:
   `(winnerScore - winnerBassBonus) * kScoreThresholdRatio`.
6. Build `results[]` (cap 3 + diff-root append) via `buildChordResult()`.
7. Fill the `PostScoringGateContext` (bass-independent metadata from the
   snapshot; `bassPc`/`bassTpc`/`threshold`/`rawCandidates` from the winner).
   `tones` and `keySigFifths` are set by the oracle, which has them directly.

**Why.** Every prior attempt to enable a progression-signal layer failed because
`applyHarmonicFunction` was a *replica* of the competition loop, recomputed from a
snapshot, and the replica was always missing a piece (Pass B, the threshold, the
cap, the cross-bass move, the gate context). Moving the competition itself into
the function layer removes the replica: there is exactly one winner-selection
pipeline, so nothing can drift. This is the section 4.1c separation
(progression/contextual signals belong in a post-ranking layer, not in the
vertical scorer) taken literally, and it is the architecture-review's preferred
strategy (`cc_e2d_architecture_review_report.md`, Q4/Q5 option 1).

**Removed.** `ChordAnalyzerPreferences::suppressProgressionSignals` and
`::captureScoringSnapshot` are gone (no suppress-then-recompute mode; the snapshot
is always built internally). The three explicit `applyHarmonicFunction()` calls in
`regionanalyzer.cpp` are gone (the call is now internal to `analyzeChord()`).
`kScoreThresholdRatio` moved to `harmonicfunctionlayer.h`
(`fn::kScoreThresholdRatio`). `applyStepBonusGuard` and the `w_stepIn`/`w_stepOut`
helpers are now free functions in the function layer.

**Behaviour-preserving invariant.** `basisIndep` (clean) `+ rootContinuity`
reconstructs the historical `basisIndepMatrix` value; every other term is computed
identically and in the same order, so the selected winner is unchanged. Verified
by the equivalence harness (0 divergences), the catalog assertions in
`composing_tests`, the pipeline snapshot goldens, and the BIR corpus.

The template count and the 4-site atomic-update checklist (section 9) are
unchanged by this redesign (no templates added or removed).

---

*Last updated: 2026-06-06 — E2d redesign: scoring-oracle / competition-pipeline
split. `analyzeChord()` is now a vertical-only oracle; `applyHarmonicFunction()`
owns winner selection, threshold, result cap and gate-context construction.
Removed `suppressProgressionSignals` / `captureScoringSnapshot`. New section 11;
section 4 (`rootContinuityBonus`) + section 10 (E2) updated. Prior: E3 extracted
`applyPostScoringGates()` from `analyzeChord()`.*
