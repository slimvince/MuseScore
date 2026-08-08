# Chord Analyzer Scoring Model

> **Status: LIVE MANDATORY REFERENCE** — the scoring pipeline's one specification (CLAUDE.md makes it
> a required read for any session touching scoring logic). Its mechanism content describes the LEGACY
> vertical scorer, which is dormant on both production surfaces since 2026-07-26/27; its §8
> constraints and dead ends remain in force and must not be retried.
>
> *Banner ratified by the user, 2026-08-03 — drafted at phase 1j, presented at
> `ratification_surfaces/cowork_pending_ratifications_next_session.md` §1, applied at phase 1k. It makes this document a
> contract home for the decisions registered against it (the fifth home case, `CLAUDE.md`
> decisions-register rule (g)). The body's present tense is NOT corrected by this banner —
> `OPEN_ITEMS.md` OI-274 stays open for that.*

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

> **File layout after refactor #1 (byte-identical layer split).** `chordanalyzer.cpp`
> retains the vertical **oracle** (scoring constants/helpers, `TemplateDef`, the
> `kTemplateCount`-derived `templates` array + score matrices, `detectExtensions`,
> `buildChordResult`, `analyzeChord`, the factory). Five single-responsibility sibling
> TUs were split out (pure code movement; no scoring/inference change):
> `postscoringgates.cpp` (the post-scoring gate layer A–L, `applyPostScoringGates`),
> `chordpostpasses.cpp` (the Iter-86/91/pedal tail, `applyIter8691Pedal`),
> `chordsymbolformatter.cpp` (`formatSymbol`/`formatRomanNumeral`/`formatNashvilleNumber`
> + their helpers), `chorddiagnose.cpp` (`diagnoseChord`), and `chordvoicing.cpp`
> (`chordTonePitchClasses`/`closePositionVoicing`). `chordanalyzer.h` is unchanged — the
> stable integration boundary. The competition / function layer was already external
> (`function/harmonicfunctionlayer.cpp`). See `cc_refactor1_split_design_dossier.md`.

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
6. **Post-scoring gates.** Inversion correction, enharmonic
   flips (Minor-add6 ↔ HalfDim7), augmented-rotation correction, Gate I
   (first-inversion major over root-position minor), Gate J (vii° → V7),
   Gate L (Major over augmented). All promotions route through the one
   `promoteToWinner()` primitive (§6a). (Gates F/G-B/G-C/K retired Stage 5, 2026-07-05;
   Gate A unified into `promoteToWinner`/FM2 — 2026-07-06.)
7. **Late promotions.** Iter 86 bass-b7 promotion, Iter 91 bass-as-root
   promotion.
8. **Pedal point check.** Two-pass: if the bass is not a chord tone of the
   Pass 1 winner and the upper voices form a confident chord on their own,
   replace with the Pass 2 result and flag `isPedalPoint`.

The analyzer is purely bottom-up — it does not know about secondary dominants,
modulation, or progression context beyond a single chord's neighbours.

### Scoring constants are readable from an optional override file (Stage-5 fitter)

Every hand-chosen numeric scoring constant documented in this file — the §4
bonus/penalty terms and joint-term weights (`kContradictionPenalty`,
`kExtensionFactor*`, `kNonBassPenalty`, the `kWSeq`/`kWDim`/`kWStepIn`/`kWStepOut`
progression signals, `kWComplete`, …), the §6 gate margins (`kGateIMargin`,
`kGateLMargin`, `kHalfDimFirstInversionBonus`; `kGateKMargin` retired with Gate K, Stage 5), and the
`ChordAnalyzerPreferences` fields — is a **mutable global** (formerly `constexpr`),
registered by name in `analysis/param/paramoverride.h`. The Stage-5 fitter (design
`cowork_stage5_fitter_design.md` D-6) can override these values by name from an
OPTIONAL external file, read once at analysis-binary startup
(`batch_analyze --param-override <file>`). **When no override file is passed the
behavior and output are byte-identical** to the pre-mechanism scorer — the globals
keep their literal initializers, are read exactly as before, and the override loader
is the only writer (proven per-preset over the full corpus). The override loader is
strict (an unknown name or malformed line aborts the run). The dormant-chain
struct-member defaults (Layer-5 confidence/resolver, phrase-boundary weights, the
voice-leading axis) are NOT reachable through this mechanism — they are consumed only
by the default-off dormant chain and are Phase-2/3 fit targets, not Phase-1 ones.

---

## 2. Templates

The analyzer scores each candidate against a fixed array of `analysis::kTemplateCount`
(currently 17) chord templates (`std::array<TemplateDef, kTemplateCount>` in `analyzeChord`).
Each template carries an intervals list (semitone offsets from root) and parallel TPC
deltas (circle-of-fifths distance). (Until Stage 2.3 a byte-identical `kDiagTemplates`
mirror existed for the legacy `diagnoseChord` scorer; `diagnoseChord` now replays the
production pipeline, so the mirror is gone — there is one template array.)

| # | Quality          | Intervals      | Represents                          | Notes |
|---|------------------|----------------|-------------------------------------|-------|
| 0 | Major            | `{0,4,7}`      | Major triad (C)                     | |
| 1 | Major            | `{0,4,7,11}`   | Major 7th (CMaj7)                   | |
| 2 | Major            | `{0,4,7,10}`   | Dominant 7th (C7)                   | |
| 3 | Major            | `{0,4,6,10}`   | Dom7♭5 / Lydian dom (C7♭5 / C7♯11) | Penalised w/o TPC confirmation of ♭5 spelling; penalised when m7 absent (see §4 structural penalties). |
| 4 | Minor            | `{0,3,7}`      | Minor triad (Cm)                    | |
| 5 | Minor            | `{0,3,7,10}`   | Minor 7th (Cm7)                     | Non-bass penalty `-kNonBassPenalty` (0.35) when root ≠ bass (waivable by full TPC match). |
| 6 | Diminished       | `{0,3,6}`      | Diminished triad (C°)               | `dim7CharacteristicBonus` (+0.75) fires on the dim7 PC, gated on full triad evidence + non-diatonic ♭♭7. **Rotation-selection mechanism** — see §4. |
| 7 | Suspended4       | `{0,5,6,10}`   | Sus4♭5 (Csus4♭5)                    | Precedes HalfDim (tie-break): ties arise on their shared `{0,6,10}` subset when only those tones sound; the sus4 reading is preferred when the ♭5 is enharmonically ambiguous. Excluded from sus4-missing-P4 penalty (the tritone is the identifying interval). |
| 8 | HalfDiminished   | `{0,3,6,10}`   | Half-diminished 7th (Cø7)           | Non-bass penalty (waivable by TPC); ties with Sus4♭5 on the shared `{0,6,10}` subset. |
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

- Sus4♭5 (7) precedes HalfDim (8): the full interval sets differ (`{0,5,6,10}` vs
  `{0,3,6,10}`), but both score identically when only their shared subset
  `{0,6,10}` is sounding — the m3-vs-P4 discriminator is absent. Sus4♭5 wins the
  exact tie (Stage-1a finding F1, pinned in
  `TiePolicy_ExactTie_LowerTiePriorityWins`).
- Min7 (5) follows Minor triad (4) and precedes Sus4 templates.
- Plain triads precede their 4-note extensions.

`diagnoseChord()` no longer keeps its own template array (Stage 2.3): it calls the
real `analyzeChord` and decorates the production snapshot, so it sees exactly the
templates and guards production uses. (The legacy diagnose scorer deliberately omitted
the production guards — that divergence, which mis-led two investigations, is gone.)

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

**Atomic update requirement.** Every template-sized array derives its extent from a single
constant, `analysis::kTemplateCount` (`chordanalyzer.h`, `mu::composing::analysis`
namespace, currently `17`). The size-sync sites (since Stage 2.3 removed `kDiagTemplates`):
- the `analyzeChord` `templates` array,
- all three score matrices (`basisIndepMatrix` / `complexityFactorMatrix` /
  `augFactorMatrix` — inner extent),
- the derived `kMasks` table in `harmonicfunctionlayer.cpp` (and the `tiePriority` bounds
  check), referenced there as `analysis::kTemplateCount`.

The per-template **interval data** now lives in ONE place — `analysis::kTemplateIntervals`
(`chordanalyzer.h`). Gate R's `kMasks` is **derived** from it at compile time via
`analysis::makeTemplateMasks()` (each mask = OR of `1u << interval` over the template's
tones), so `kMasks` is no longer a hand-typed mirror that can silently drift from the
templates — the audit-Q1.3 hazard (a wrong/zero mask silently disabling Gate R) is closed.
A `static_assert` in `bassIsTemplateChordTone` pins the derived masks byte-for-byte to the
original hand-typed values. (`templates` still carries its own interval literals next to the
parallel `tpcDeltas`; keeping the two interval sources in agreement is the one residual
hand-sync, guarded by the independent table test in `gater_tests.cpp` — see §9.)

(`diagTemplateName` in `tools/batch_analyze.cpp` carries the human-readable names for the
diagnostic dump; it `static_assert`s its length against `analysis::kTemplateCount` but is
display-only, not a scoring site.)

To add a template, bump `kTemplateCount` and add the matching entries (see §9). The
compiler now enforces the sizes: adding an entry to a TemplateDef array **without** bumping
the constant is a hard error (too many initializers), and the matrices / kMasks resize
automatically. This closes the silent stack-buffer-overrun class from the B1 attempt
(2026-06-04), where the matrices were sized by an independent literal and a mismatch
produced garbage cells with no compile error. `static_assert`s on each array's `.size()`
guard against a future hand-edit re-hardcoding a literal.

### Floating-point tie policy

Winner selection compares candidate scores with **exact `double` comparisons — there is no
epsilon anywhere in the ranking.** The final per-bass comparator (`harmonicfunctionlayer.cpp`,
`applyHarmonicFunction`) is, in order:

1. `a.score != b.score` → higher `score` wins (exact inequality on the raw `double`);
2. else lower `tiePriority` wins (`tiePriority` is the template index — see §2 ordering);
3. else lower `rootPc` wins.

This is fully deterministic **given identical floating-point evaluation**: the same inputs
on the same build always produce the same winner. The `tiePriority`-then-`rootPc` keys
resolve genuine exact score ties (identical PC sets across enharmonic templates, e.g.
Sus4♭5 ordered before HalfDim). The omission of an epsilon is intentional — an epsilon
would make the order depend on a threshold that is itself uncalibrated, and would mask
rather than resolve near-ties.

**Fragility caveat — near-ties are not protected.** Because nothing rounds before the
comparison, two candidates separated by a hair (a near-tie, not an exact tie) are ordered
purely by which `double` is fractionally larger. Documented near-tie classes:
- the Δ=+7b ~0.02-margin class (the Gate R targets), and
- bwv320 (≈ 1.92 vs 1.90 between the competing readings).

These could **flip** under any change that re-associates the floating-point arithmetic:
different compiler / optimization flags (`-ffast-math`, `/fp:fast`, FMA contraction),
a different platform's libm, or a reordering of the summation in the score expression
`(basisIndep + bassDep) × complexityFactor × augFactor + wComplete + wSeq [+ wDim] [+ step]`.
Treat the exact evaluation order as load-bearing: **any change to optimization flags or to
the order of the scoring arithmetic requires a full corpus A/B on both presets** before it
is trusted byte-identical. (A regression test pinning these near-tie cases is Stage 1.7 of
`docs/implementation_roadmap.md`; not yet added.)

---

## 4. Bonus and penalty terms

### `dim7CharacteristicBonus` — `kDim7CharacteristicBonus = 0.75`

**Definition (`chordanalyzer.cpp`, the `kDim7CharacteristicBonus` file-scope constant,
applied in the `dim7CharacteristicBonus()` helper).** Applied per `(rootPc, tplIdx)` for
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

**"Non-diatonic to the current key" — the key SIGNATURE's collection, never the tonic (OI-168,
fixed 2026-07-14).** Condition 3 above, and the identical condition in `diatonicRootContribution`
(§4 "Other terms"), are the analyzer's only two key-consuming scoring tests. Both ask the same
question — *is this pitch class in the key?* — and that is a question about the key's **collection**,
not its tonic. Both therefore test

```
pcInMask(diatonicMaskFromFifths(keySignatureFifths), pc)      // analysisutils.h
```

whose contract is *"Key-agnostic: depends ONLY on the notated signature, never a resolved mode."*
**Neither term takes a tonic or a mode scale.** That is the point: the tonic-independence is
structural, not a cancellation that a future mode-table edit can silently undo.

**Why it is written that way — the defect it replaced (OI-168).** Until 2026-07-14 both terms tested
membership in **{ (keyTonicPc + scale[i]) mod 12 }**, where `scale` is the interval set of the mode's
*diatonic parent* (`DIATONIC_PARENT_INDEX`) laid out from the **mode's own** tonic. That set equals
the key signature's diatonic collection **only when the mode's tonic offset equals its parent's** —
true for 19 of the 21 `KeySigMode` values, **false for `Altered` and `AlteredDomBB7`**, whose tonic
sits a semitone above their parent's. For those two the set was the signature's collection
**transposed up a semitone** (2 of 7 pitch classes shared), so both terms scored against the wrong
collection. It is not repairable by re-parenting: their tonic is not a member of any parent
collection. Measured magnitude (`cc_oi168_magnitude_report.md`) and adoption
(`cc_oi168_fix_report.md`): `Altered` is emitted on Jazz only — 24 surviving regions, 49 scorer
entries — and the corruption flipped exactly **one** committed chord (`bwv145.5@12960`: `Ebm` →
`B/Eb`, correcting a class-(b) root failure against the DCML ground truth); on the other 22 regions it
moved the score without moving the winner. Baroque and Default regenerate **byte-identically** under
the fix (the δ = 0 derivation, verified at runtime on 352 scores × 2 presets).

**⚠ Do not reintroduce `keyTonicPc + scale` for a membership test.** A scale-DEGREE is tonic-relative
by definition and legitimately uses that pair (`buildChordResult`); a membership question must not.
Note that `buildChordResult`'s `diatonicToKey` flag and the Gate I / Gate L `invRootIsDiatonic` checks
(`postscoringgates.cpp`) still answer a *collection* question through the *tonic* pair and so still
carry the OI-168 defect — they are declared, not fixed (see `OPEN_ITEMS.md` OI-170).

**OI-170 measured those three sites (2026-07-16; `cc_oi170_measure_report.md`) — the code carries a
DEFAULT-OFF A/B for them, and no fix is promoted.** Each of the three evaluates *both* predicates
whenever `MU_KEY_COLLECTION_PROBE` is set, and takes the signature-collection answer only when
`MU_KEY_COLLECTION_SIGMASK_VARIANT` is also set; **both flags are unset in production and the OFF path
is byte-identical (352/352 × 3 presets, proven)**. What the A/B measured:

- **ZERO committed chords move on any preset.** Gate I's two verdicts differed on exactly **one**
  candidate across the whole Jazz corpus and the swap decision differed **0** times (another conjunct
  blocked it either way); Gate L's verdicts never differed. So neither gate's *swap* is reachable by
  this defect on this corpus — the defect is live but, at these two gates, currently inert.
- **Only the published `diatonicToKey` flag moves**: 22 flags on 9 Jazz files, every one
  `false → true`, every one toward-correct; Baroque/Default byte-identical (δ = 0 at runtime again).
- The robust-stop hard gate is unmoved (run-diff +0/−0, class-(a) and class-(b) duration δ = 0).

**Reading for a future fix:** the collection question at all three sites can move to
`pcInMask(diatonicMaskFromFifths(fifths), pc)` with **no committed-chord change** — but that is *not*
the whole tonic story in the scoring path. Two live sites decide a committed chord from a genuine
**degree**, which no collection can answer and this primitive cannot replace: **Gate G-E** (58 winner
swaps on Baroque) and `applyTonicPriorToSparseChord` (172/183/172 committed-*quality* overwrites —
`OPEN_ITEMS.md` OI-172). A third lives outside this layer entirely, in the segmenter (OI-175). See
also OI-173: `degree` itself has **two** inequivalent definitions in the tree (the mode's diatonic
**parent** scale here in `buildChordResult`, vs the mode's **own** scale in `diatonicDegreeForRootPc`),
which differ for all 14 non-diatonic modes — correcting that basis is a **separate** change with its
own measurement, because it moves `degree`, hence Roman numerals, hence possibly those two gates.

### `rootContinuityBonus` — `prefs.rootContinuityBonus = 0.40`

Applied by the competition pipeline `applyHarmonicFunction()`
(`harmonicfunctionlayer.cpp`) when `ctx.previousRootPc == rootPc`, added into
`basisIndep` before the complexity x aug multiply. Rewards continuing the same
root across adjacent regions. It is a **progression signal, not vertical pitch
evidence**: as of the scoring-oracle / competition-pipeline split (see section 11)
the scoring oracle `analyzeChord()` no longer folds it into `basisIndep`. (Since
Stage 2.3 `diagnoseChord` replays the production pipeline, so its dump shows the
pipeline's own rcb — including the Gate R outcome — not a re-derived value.)

**Known dead end (Iter 98, 2026-05-23).** Gating this bonus off a sparse
predecessor (e.g. `previousRegion.distinctPcs <= 2`) was tried in two variants
and both regressed `mozart_k280-1` IV→V65 in Alberti-bass contexts. The signal
is load-bearing for legitimate sparse continuity (broken-chord bass with held
upper voices). Do not attempt a density-based or inversion-aware gate here
without re-reading the Iter 98 dead-end section in `COWORK_HANDOFF.md`.

### Gate R — rcb bass-chord-tone guard

**Where it fires.** Pass A of the competition pipeline `applyHarmonicFunction()`
(`harmonicfunctionlayer.cpp`). **Since Stage 3.4** the rcb computation and the Gate R
zeroing are encapsulated in the file-local `rcbEdge(cell, fullBasisDep, previousRootPc,
prefs, applyProgressionSignals)` helper — the rcb back-edge with its structural guard
absorbed. Pass A calls `rcbEdge(...)` once per cell and folds the returned rcb into
`basisIndep`. The arithmetic and short-circuit order are byte-identical to the prior
inline form. (Stage 3.4 also removed the redundant 2-arg `gateRZeroesRootContinuity`
test-compat overload; the 3-arg predicate is the sole entry point.)

**Condition.** The predicate `gateRZeroesRootContinuity()` encodes three **structural**
conditions (all required); the **phase** guard is applied separately inside `rcbEdge`
(see below). Zero the bonus for a cell when all of these hold:
1. `rcb > 0` (root continuity holds for this candidate), AND
2. `basisDep <= 0` — the candidate earned **no inversion credit** (no inversion bonus
   fired and no bass-root bonus applies). **Since Stage 3.3** the pipeline passes the
   *reconstructed* full basisDep (`cell.basisDep + fn::inversionContextBonus(...)`) to the
   3-arg overload, because the inversion bonuses now live in the pipeline; pre-3.3 this
   read the oracle's then-inversion-bearing `cell.basisDep` (a cross-layer dependency,
   audit Finding 6, now closed — the read is intra-layer). The two are byte-identical
   (see the Stage 3.3 note below), AND
3. `bassIsTemplateChordTone(rootPc, tiePriority, bassPc) == false` — the bass is
   foreign to the candidate's template. `bassIsTemplateChordTone` returns true iff
   `(bassPc - rootPc) mod 12` is a tone of the candidate's template (a static `kMasks`
   interval-bitmask table **derived** from `analysis::kTemplateIntervals` — the same
   interval data the 17 TemplateDef entries are built from).

**Phase guard (separate from the predicate).** `rcbEdge()` zeroes rcb only when
`gateRZeroesRootContinuity(...) && applyProgressionSignals` (where `applyProgressionSignals
== (phase == ScoringPhase::Final)`). Gate R is a **final-scoring correction only**; it never
fires during segmentation exploration (`ScoringPhase::Segmentation`) — see "Why the phase
guard" below. The predicate itself is stateless (no phase parameter): the phase is consulted
once, inside `rcbEdge` at the Pass A call site.

**Why the `basisDep <= 0` condition (refinement vs. the bare bass-foreign test).**
The bare bass-foreign test alone misfires on legitimate extended slash voicings.
Counterexample: `Cm7add11/F` (test
`Cm7SlashF_StepwiseBassContext_IsCm7NotFsus`). F is interval 5 (P4/11th) from C —
foreign to the bare Min7 template `{0,3,7,10}` — yet F is sounding as the 11th and
the reading is correct. The discriminator: a legitimate inverted/extended
continuation has a **sounding third**, which makes it `isInvertedMajMin` and fires
`sameRootInversionBonus` (and usually `stepwiseBassInversionBonus`), so its
`basisDep > 0`. A Δ=+7b bare-root continuation has **no sounding third**, fires no
inversion bonus, and (being a slash) gets no bass-root bonus, so `basisDep == 0`
(confirmed for all three cases in the diagnostic report Table 1). Requiring
`basisDep <= 0` therefore restricts Gate R to genuine bare-root nonsense
continuations and spares real extended chords. (`basisDep` may be slightly negative
when a `kNonBassPenalty` applies with no offsetting inversion credit — still a
bare-root case, correctly gated.)

**Stage 3.3 redesign — reconstructed-credit (byte-identical).** When the four inversion
bonuses migrated from the oracle into the competition pipeline (§11), the oracle's
`cell.basisDep` stopped carrying the sounding-third signal. Cowork ratified the
**reconstructed-credit** form: the pipeline reconstructs the full basisDep
(`cell.basisDep + fn::inversionContextBonus(...)`) for the score anyway, and Gate R reads
*that* value (`fullBasisDep <= 0`) — identical to the historical proxy on every input, with
no cross-layer dependency. The derivation behind the equivalence (and why the originally
designed literal "sounding-third pcWeight test" was *not* adopted): under Gate R's only
firing context (`rcb > 0` ∧ bass foreign), `bb`=0 (bass-root bonus needs `rootPc==bassPc`),
so `basisDep_old = nonBassAdjustment + cappedInv`, and because the **minimum inversion bonus
(`sameRoot` 0.40) strictly exceeds the maximum penalty (`kNonBassPenalty` 0.35)** the old
gate fires **⟺ `cappedInv == 0`** (no inversion bonus earned). The literal
`pcWeight[third] ≤ 0.05` test matches this for Maj/Min/Aug/HalfDim (all in the
`isInvertedMajMin` set → a sounding third fires `sameRoot`) and for the no-third qualities
(Sus/Power, always gated), but **diverges for Diminished**: Dim is excluded from
`isInvertedMajMin`, so its only credit is `completeTriadInversionBonus`, which *additionally*
requires stepwise-bass evidence — a temporal condition no vertical pcWeight test can capture.
A Dim continuation with foreign bass + sounding third but no stepwise bass earns no credit
(old gate fires) yet has a sounding third (literal test would spare it) — a 0.40×cf×af output
swing. Reading the reconstructed credit avoids this gap entirely. See
`docs/decoder_design.md` §6 amendment and `cc_stage3_3_report.md` §1.

**★ THE DECISION, STATED AS SUCH — the RECONSTRUCTED-CREDIT read is the ratified form of this
guard, and the originally designed literal sounding-third test is NOT what shipped (re-homed into
this specification 2026-08-07 on the user's ruling). ⚠ LEGACY subject — the vertical scorer this
guard belongs to is dormant on both production surfaces.** Gate R asks whether the candidate earned
**any inversion credit at all**; it does not test directly whether the candidate's third is
sounding. *Why:* the derivation is the paragraph immediately above and is not repeated (#6) — the
two tests are provably equivalent everywhere except on Diminished, where the direct test would be
wrong because the only credit a Dim candidate can earn additionally requires stepwise-bass
evidence, a temporal condition no vertical test can see. Reading the pipeline's own reconstructed
credit is therefore the faithful execution of the redesign's intent rather than a compromise, and
it is what closes the cross-layer dependency the redesign set out to remove. The originally
designed mechanism text is retained above **for the record**, and a future reader must not mistake
it for the shipped behaviour.

**Why the phase guard.** `rootContinuityBonus` is deliberately **not**
suppressed during `greedyExpandSegmentation` exploration (unlike `w_seq` / `w_dim` /
step bonuses), so segmentation boundary selection already depends on rcb. If Gate R
were allowed to perturb rcb during exploration it would shift region boundaries:
this was caught at `bwv355` m15, where a baseline region (`Bm/D` at tick 26880,
DCML-correct root B) was **split** into a spurious `G/B` sub-region at tick 27840 —
a new BIR=false error invisible to the within-region diagnostic. Restricting Gate R
to the final (non-exploratory) scoring pass keeps segmentation byte-identical to
baseline while still correcting the final winner; the Δ=+7b fixes are all
final-pass decisions and are unaffected by the guard.

**Why it exists.** The vertical oracle already scores a non-chord-tone-bass
("nonsense slash") candidate lower than the correct reading, but `rcb` (+0.40) is
strong enough to overturn that verdict. In the Δ=+7b cluster the correct
first-inversion complete triad leads the continued/predecessor root by only 0.38
raw, so the +0.40 continuity bonus flips a clear vertical win into a 0.02 loss.
Gate R restores the oracle's priority by denying continuity credit to a
continuation that cannot harmonically hold its own bass.

**The Δ=+7b mechanism it fixes.** Three Bach cases — bwv245.28 (B/G♯), bwv296
(D/B), bwv320 (G/E) — all have `(bassPc - rootPc) mod 12 == 9` (a major sixth from
the continued root), which appears in **none** of the 17 templates. The bass is in
fact the major third of the DCML-correct root (G♯ of E, B of G, E of C), i.e. a
first-inversion complete triad of the correct chord. Gate R fires on the wrong
(continued-root) candidate, withholds its +0.40, and the correct triad wins on its
clean 1.90 vs 1.52 raw lead.

**Safety.**
- *Alberti-bass safe.* In Alberti / broken-chord continuity the dominant pedal is
  voiced over its own chord tones (C/E/G), so the bass is always a template tone and
  Gate R never fires there. This sidesteps the Iter-98 and predecessor-bass dead
  ends, which keyed on predecessor density / bass change and misfired on Alberti.
- *mozart_k280-1 control passes unaffected.* The rcb-rewarded continued candidate
  there always has a chord-tone bass (G = P5 of C, E♭ = m3 of Cm), so Gate R leaves
  rcb intact and rcb still correctly reverses the raw winner.
- *Forward-compatible.* `kMasks` is **derived** from `analysis::kTemplateIntervals`
  (`chordanalyzer.h`) — adding a template means adding its interval row there and the masks
  update automatically (see §9). A 0 mask is impossible by construction: every template
  includes interval 0 (the root).
- *Conservative.* Out-of-range / unknown inputs return true (no gating).

### `w_complete` — `kWComplete = 0.50`

`kWComplete` file-scope constant in `chordanalyzer.cpp`, applied in the
`wCompleteBonus` lambda inside `analyzeChord`. Fires when:

- `jointScoringEnabled` (region came from `collectRegionTones`),
- `candBassPc == rootPc` (root position),
- `distinctPcs == 3` (exactly three PCs in the region),
- all three triad tones (root, third, fifth per quality) present above the
  `kWCompletePresenceThreshold` (0.05).

Reward: root-position complete triads outrank slash-chord readings of the
same PC set (closes Bug 2 — bwv310 m8 b3 Em/C vs C major). Iter 90's
regression mode (slash chord with missing fifth) is excluded because an
absent tone has `pcWeight == 0` which fails the presence check.

**★ THE GUARD IS THE DECISION, AND IT IS STRUCTURAL RATHER THAN A THRESHOLD (re-homed into this
specification 2026-08-07 on the user's ruling). ⚠ LEGACY subject.** The completeness bonus fires
**only** for a **root-position** reading — the candidate bass IS the triad root — whose three triad
tones are all present above the presence threshold. A genuine slash chord therefore neither gains
the bonus nor is beaten by a rival reading that gains it wrongly. *Why:* derived from a measured
failure rather than chosen. The previous, unconditional version of the same idea caused large
regressions in both directions because it promoted cases where the slash-chord reading was the
correct one; the design works the guard through the exact case that failed and shows that a genuine
slash chord with its own fifth present does not collect the root-position bonus for the rival
reading. It is an early instance of the standing rule that a correction is given a **structural
entry condition** rather than a widened threshold (`CLAUDE.md`, the gate and preset policy).

### `w_stepIn` / `w_stepOut` — `kWStepIn` per-carrier (Baroque/Default **0.125**, Jazz/others 0.10); `kWStepOut = 0.10`

`kWStepIn` / `kWStepOut` constants in `harmonicfunctionlayer.h`; applied by
`fn::wStepInBonus` / `fn::wStepOutBonus` through `applyStepBonusGuard`
(`harmonicfunctionlayer.cpp`), Pass B of the competition pipeline (Stage-3.3 migration
— they no longer live in `chordanalyzer.cpp`). Reward root-position candidates whose
root participates in semitone / whole-tone bass motion from the previous region
(`stepIn`) and/or to the next region (`stepOut`).

**Stage-5 Phase 2.2e adoption (user-ratified 2026-07-05).** `kWStepIn` moved `0.10 → 0.125`
as the arc's first fitted-value adoption (idiom-#2 fit, the Bach-chorale fitting split). It is
**per-carrier**: the Baroque and Default carriers ship `0.125`; Jazz and Standard/Modal/Contemporary
stay pinned at `0.10`. Production has no preset-selection moment, so the **global initializer**
(`0.125`) is the Default-carrier value it delivers. Because `kStepBudget` is *derived* from
`kWStepIn` (below), the pinned-`0.10` carriers **re-derive** `kStepBudget = 0.21` explicitly in
`batch_analyze.cpp` after the single-key override (only the file loader recomputes it automatically);
the Baroque/Default carriers keep the initializer's `0.235`. `kWStepOut` is unchanged at `0.10`.

**Four gates (each load-bearing):**

1. **`phase == ScoringPhase::Final`** (call-site gate) — suppresses the bonus inside
   `greedyExpandSegmentation` boundary exploration, which runs in
   `ScoringPhase::Segmentation`. Without this, segmentation biases sub-region bass
   selection toward stepwise candidates and redirects segmentation before the final
   per-region scoring pass runs. The `wStep*` helpers are stateless; the suppression
   lives at the Pass B call site (`if (applyProgressionSignals) { applyStepBonusGuard… }`).

2. **`candBassPc == rootPc`** (root-position only) — the bonus rewards "this
   chord's root moves smoothly in the bass line," not "this slash-chord's bass
   happens to step." Without this guard a slash-chord bass (e.g. F♯ in G♯m7/F♯)
   that steps to a neighbouring bass gets credit it shouldn't — caused the
   Iter 94 Jazz bwv430 regression (BIR=false 14→15).

3. **First-inversion m7-family surgical guard (Pass B)** — suppresses the
   bonus when a competitor of quality {HalfDiminished, Diminished, Minor7}
   sits a minor third below our bass and scores within `kStepBudget` (0.235 Baroque/Default,
   0.21 Jazz/others — derived from `kWStepIn`)
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

`kWSeq` constant in `harmonicfunctionlayer.h`; applied by `fn::wSeqBonus`
(`harmonicfunctionlayer.cpp`, Iter 95; Stage-3.3 migration out of `chordanalyzer.cpp`).
Fires when:

- `jointScoringEnabled`, `context` available,
- the call site is in `ScoringPhase::Final` (the stateless `wSeqBonus` is simply not
  called in `ScoringPhase::Segmentation`),
- `context->nextRootPc >= 0`,
- `distinctPcs >= 4`,
- the next region's root sits a perfect fourth above the candidate root
  (`(nextRootPc - candRootPc) mod 12 == 5`).

Reward: classic V → I descending-fifth root motion. This is a **chord-level**
signal: any inversion of the candidate qualifies (the bonus does NOT require
`candBassPc == candRootPc`), and the m7-family surgical guard does NOT apply
(sequential root motion is about root identity, not bass).

### `w_dim` — `kWDim = 0.15`

`kWDim` constant in `harmonicfunctionlayer.h`; applied by `fn::wDimBonus`
(`harmonicfunctionlayer.cpp`, Iter 96; Stage-3.3 migration out of `chordanalyzer.cpp`).
Fires when:

- `jointScoringEnabled`, `context` available,
- the call site is in `ScoringPhase::Final` (the stateless `wDimBonus` is simply not
  called in `ScoringPhase::Segmentation`),
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

### `ScoringPhase` (ChordAnalyzerPreferences::scoringPhase)

`function::ScoringPhase scoringPhase = function::ScoringPhase::Final`
(`ChordAnalyzerPreferences`, `chordanalyzer.h`). The enum is defined in
`chordanalyzer.h` (in the `mu::composing::function` namespace, alongside the
`ScoringSnapshot` forward declaration) rather than in `harmonicfunctionlayer.h`, because
the include chain runs `harmonicfunctionlayer.h → chordanalyzer.h` and the
`= ScoringPhase::Final` default member initializer needs the complete enum.

Set to `ScoringPhase::Segmentation` by `greedyExpandSegmentation` for internal
boundary-exploration `analyzeChord` calls (Round 1 head/tail synthesis + Round 2 region
scoring in `harmonicsegmenter.cpp::fillGap`). Forwarded by `analyzeChord` to
`applyHarmonicFunction(..., prefs.scoringPhase)`.

`ScoringPhase::Segmentation` suppresses the progression signals that would otherwise bias
sub-region bass selection during segmentation, before the final per-region scoring pass
runs: `w_stepIn`, `w_stepOut`, `w_seq`, `w_dim`, **and Gate R**. `rootContinuityBonus`
stays active in both phases (segmentation depends on it). This replaced the former
per-function `explorationMode` flag: the bonus functions and Gate R predicate are now
stateless, and the phase is consulted once inside `applyHarmonicFunction()`
(`const bool applyProgressionSignals = (phase == ScoringPhase::Final)`). Final per-region
calls (bridge / batch_analyze callers, after segmentation returns boundaries) leave the
default `ScoringPhase::Final`.

Do not collapse this into a single inline flag again without preserving the stateless
bonus functions and the single control point.

### Other terms (briefly)

| Term                                  | Value         | What it does |
|---------------------------------------|---------------|---|
| `bassNoteRootBonus`                  | 0.70          | Awarded when `rootPc == bassPc`, multiplied by `bassRootBonusMultiplier` (1.0 full triad, 0.3 third-only or root+5, 0.1 bass alone). |
| `diatonicRootBonus`                  | 0.30          | Awarded when the root is a member of the key SIGNATURE's diatonic collection — `pcInMask(diatonicMaskFromFifths(fifths), pc)`, in `diatonicRootContribution`. The term takes **no tonic and no mode scale**; it shares that membership test with `dim7CharacteristicBonus` (the analyzer's only other key-consuming term). Fixed at OI-168 (2026-07-14) — see §4 for the tonic-anchored form it replaced and why. |
| `tpcConsistencyBonusPerTone`         | 0.20          | Per non-root template tone whose authored TPC matches the expected delta. |
| `resolutionBonus`                    | 0.35          | Awarded on `prevDim→Maj/min` semitone-up, `prevHalfDim→Maj` P4-up, `prevAug→same-root`. |
| `stepwiseBassInversionBonus`         | 0.50          | Inverted Maj/Min with bass stepwise from previous region's bass. |
| `stepwiseBassLookaheadBonus`         | 0.50          | Inverted Maj/Min with bass stepwise to next region's bass. |
| `completeTriadInversionBonus`        | 0.45          | All three triad tones present in a 3-PC texture; inverted reading. |
| `sameRootInversionBonus`             | 0.40          | Inverted candidate whose root matches the previous region's root. |
| `maxTotalInversionContextBonus`      | 2.0 (no preset override — see note below) | Cap on the sum of the four inversion bonuses above; currently non-binding. |
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

**`maxTotalInversionContextBonus` is currently inert (verified 2026-06-10).** No code
path sets a non-default value: both presets inherit the 2.0 default — the
`batch_analyze.cpp` preset builder sets neither, and the only other appearances are
the `ChordAnalyzerPreferences` declaration (`chordanalyzer.h:411`), the optimizer
range entry, and the two `std::min` clamp sites. The previously documented
"Baroque=2.5 / Jazz=0.6" values were aspirational: they entered the field's
doc-comment at its introduction (`46c76ad67f`, 2026-05-05) as planned "Iteration 4"
tuning that never happened, and a full-history pickaxe shows no commit ever assigned
them (cap archaeology, 2026-06-10 doc pass; inventory in `cc_stage1b_report.md`
§1.6). The cap cannot bind at current values: the four inversion bonuses sum to 1.85
(Baroque/default prefs) and 0.75 (Jazz), both below 2.0. Jazz's different inversion
behavior comes from its **reduced individual bonuses** (0.20/0.20/0.15/0.20, set in
`batch_analyze.cpp`), not from this cap. The field stays documented because it exists
in prefs and the optimizer range table — treat it as an untuned safety net, not a
load-bearing per-preset value.

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
`distinctPcs >= 3`. Since Stage 3.3 the oracle ANDs it into the per-cell
`supportsInversionBonuses` / `qualifiesCompleteTriad` flags it publishes on each
`ScoringCell`, so the migrated inversion bonuses still respect it — sparse
upper-register "bass" notes are not real bass voices and must not trigger inversion
bonuses (Corelli op01n08d m2 b3).

**Inversion-bonus computation (since Stage 3.3 — competition pipeline).** The four
§4.1b inversion bonuses are computed by `fn::inversionContextBonus(cell, previousRootPc,
bassIsStepwiseFromPrevious, bassIsStepwiseToNext, prefs)` in `harmonicfunctionlayer.cpp`,
which returns `min(completeTriad + stepwiseInversion + stepwiseLookahead + sameRoot,
maxTotalInversionContextBonus)` — the same term order and clamp the old oracle helper
`bassDependentContextualBonuses` used. The pipeline folds it into the cell's basisDep
(`fullBasisDep = cell.basisDep + inversionContextBonus`) before the cf × af multiply.
The oracle now sets `cell.basisDep = nonBassAdjustment + appliedBassBonus` (genuinely
vertical) plus the two eligibility flags. The cap is a safety net against runaway
stacking; it is non-binding at current values (bonus sums 1.85 / 0.75 Jazz vs the 2.0
default — see the §4 note).

**★ THE DECISION THIS SECTION RECORDS, STATED AS A RULE — the bass and the chord are chosen
TOGETHER, as one (bass, root, template) triple (re-homed into this specification 2026-08-07 on the
user's ruling). ⚠ LEGACY subject — this scorer is dormant on both production surfaces.** The
analyzer does **not** commit to a bass and then score chords against it. It enumerates the
plausible bass candidates and the whole root × template grid against each, and the winner is the
best **(bass, root, template)** triple under the composite score. *Why:* both defects that forced
it are diagnosed to the same cause and named with it — a passing note that happens to be the
absolute lowest pitch wins bass selection over the beat-onset bass a step above it, flipping the
chord root; and an incomplete slash-chord reading beats a complete root-position triad because
root-position completeness earned no advantage. **Neither is reachable while the bass is committed
before the chord is scored**, which is what makes this a structural decision rather than a
weighting one. The cost is stated with it and judged acceptable: a few times the scoring loop. It
is the same principle the production estimator carries on its own terms — coupled quantities are
decided together rather than one being committed early.

---

## 6. Post-scoring gates (A–L)

These run after `results[]` is populated and the optional guaranteed-
inversion-alternative is appended. They modify ranking via `std::swap` and
`std::stable_sort` — they do not change the underlying scores in
`rawCandidates`.

**★ POINTER — WHAT A GATE MAY READ IS FIXED AT THE INFERENCE/PRESENTATION BOUNDARY, NOT HERE (added
2026-08-07 on the user's homing ruling; the rule is published once, at `ARCHITECTURE.md` §3.3, #6).**
A gate or scoring rule reads **structured fields only** — no chord-symbol string parsing and no
Roman-numeral inference, in any gate, any scoring term, or any future change to either. It binds
every rule in this section and every rule §4 documents. Read it at its home; this line points at it
and does not restate it.

**E3 (2026-06-06): execution location.** Gates A–L are implemented in
`applyPostScoringGates()` (declared in `chordanalyzer.h`, defined in
`postscoringgates.cpp` since refactor #1; formerly `chordanalyzer.cpp`).
`analyzeChord()` no longer runs them internally; instead
it publishes the inputs the gates need (`pcWeight`, `tpcForPc`, `scale`,
`keyTonicPc`, `keyMode`, `bassPc`, `bassTpc`, `distinctPcs`, `threshold`,
`rawCandidates`) via the optional `PostScoringGateContext* gateCtxOut`
out-parameter. Production call sites in `regionanalyzer.cpp` (Pass 1, Pass 2,
Pass 2b), `harmonicsegmenter.cpp`, the notation bridges, and `inferNextRootPc()`
call `applyPostScoringGates()` *after* `applyHarmonicFunction()`. Tests use the
`analyzeWithGates()` helper in `test_helpers.h`. The table below identifies each gate
by name; all are implemented inside `applyPostScoringGates()` (`postscoringgates.cpp`).
The gate margins are the file-scope constants `kGateIMargin` /
`kGateLMargin` (`kGateKMargin` retired with Gate K, Stage 5; relocated to file scope for the Stage-5 override mechanism — see the
§1 note); the "Location" column names the gate's code region rather than a line number
(the former `~Lxxxx` anchors predated refactor #1's move out of `chordanalyzer.cpp`).

**Outer guard — covers ALL of A–L, including the bias correction.** Everything in
`applyPostScoringGates` runs inside one block gated on
`prefs.inversionSuspicionMargin > 0`, `prefs.inversionBonusReduction < 1`,
`results.size() >= 2`, and `gateCtx.distinctPcs >= 3`. Consequences: setting
`inversionSuspicionMargin = 0` to "disable the inversion correction" disables every
gate — including the enharmonic flip (FM2) and Gate J — and sparse 2-PC regions get no gate
corrections at all (Stage-1b findings F2/F3, pinned in the `OuterGuard_*` tests in
`postscoringgates_tests.cpp`).

**Execution order:** bias-capture → [enharmonic flip (present-swap else FM2 append) → E →
bias-deduction+sort] → G → H → I → L → **J**. Despite its letter, Gate J executes LAST, after
L. (Gates B/C/D/F/K retired; the former separate Gate A + FM2 are now the two branches of the
one enharmonic-flip promotion.) The table below follows execution order.

### §6a. The unified promotion primitive `promoteToWinner()`

Every post-scoring promotion re-ranks `results[]` so a chosen reading becomes the winner
(`results[0]`). All of them route through **one** primitive, `promoteToWinner()`
(`chordanalyzer.h` / `postscoringgates.cpp`), which owns both promotion idioms behind one
contract (⛔ total unification — one path per concern):

- **Idiom A — present-first (swap):** if the target reading is already carried in `results[]`
  it is swapped to the front (reuse-in-place — no growth, no duplicate).
- **Idiom B — append-built (pull):** otherwise the target is built **once**, via the single
  builder wrapper `buildResultFromGateCtx()` over `buildChordResult()`, appended, and swapped
  to the front.

`presentHint` selects the present branch: a concrete index the caller already computed (swap
iff it still matches — how the enharmonic flip and Gate E reproduce their exact `bestAltIdx`
swap), `kPromotePresentScan` (first-match scan of `results[1..]` — the G-family), or
`kPromoteAppendOnly` (skip the present branch — the Iter-91 bass-root pull, which has no
dedup). `stopBelowThreshold` stops the raw scan at the first sub-`threshold` candidate (the
FM2 inclusion policy). `target.quality == Unknown` matches any quality (Iter-91).

This replaced the three duplicated builder lambdas (`postscoringgates.cpp`,
`chordpostpasses.cpp`, `harmonicfunctionlayer.cpp`) and the ad-hoc swap-vs-append idioms; the
initial score-ordered build in `applyHarmonicFunction()` now calls `buildChordResult()`
directly. The unification is byte-identical to the former separate gates on the full output
surface (winner AND `alternatives[]`) across all 352 scores × 3 presets — see
`cowork_gateA_unification_design.md`.

**★ THREE DECISIONS THIS PRIMITIVE RESTS ON, re-homed into this specification 2026-08-07 on the
user's ruling. ⚠ LEGACY subject — this gate layer is dormant on both production surfaces, and its
disposition belongs to the retirement map.**

- **Which carry is correct is decided on the carry's PURPOSE, not on which code happened to be at
  HEAD: the correct carry is the one that KEEPS the distinct alternative reading.** Two promotion
  idioms were in use — one swaps a reading already carried in `results[]` to the front, leaving the
  displaced reading in place; the other builds a fresh copy and appends it. The swap idiom is
  correct. *Why:* argued from what the carry is FOR, and the design says so in terms — the
  alternatives exist so the later layer can select among the **distinct** readings, and a copy of
  the winner is not a distinct reading. Measured on the full output surface across the whole
  corpus, the append idiom injects that near-copy and displaces the genuinely different partner,
  which is an information-loss regression under #12. The same principle is already applied
  elsewhere in this layer, where a non-promoting raw pull is popped so it does not pollute the
  list. This is explicitly **not** "prefer the idiom that is at HEAD".
- **ONE promotion primitive, with a PRESENT-FIRST dedup guard — the append branch fires only when
  the target is genuinely absent.** The ordering is the whole fix: present-first makes an
  already-carried partner *swapped* rather than *appended*, so no duplicate can enter. *Why:* the
  design shows the equivalence rather than claiming it — for the enharmonic flip the caller has
  already computed the in-`results[]` partner index, and the primitive swaps that exact index, so
  the produced permutation is byte-identical to the behaviour it replaces. That is what makes
  retiring the separate rule a no-op on the output rather than a change to be argued about.
- **The retirement condition for the separate Gate A rule is BYTE-FOR-BYTE REPRODUCTION OF ITS
  CARRY — not the winner-inertness that preceded it.** Once the flip is one promotion call with
  present-first branching, the former "partner present" and "partner absent" rules are two branches
  of the same promotion and the separate rule — its enum member, its guard, its name-map entry and
  its dedicated fixtures — is redundant. It is removable **because** the primitive reproduces the
  swap byte-for-byte on the present branch, which leaves winner AND carry byte-identical. *Why:*
  the condition is quoted from the earlier ruling it discharges — the rule retires when the
  promotion machinery unifies into one path producing one carry — and the design shows why the
  earlier winner-only inertness was **not** enough: the naive removal was inert on the winner
  across the whole corpus while changing the carry on a named subset of scores. That gap is exactly
  why this document's evidence rule is inertness on the **full** output surface, winner AND
  alternatives, and never the winner alone (#15).

**Stage-5 dissolution audit — per-rule disable (measurement-only).** Each §6 rule (the
bias correction, FM2, and Gates E/G-E/G-D/H/I/L/J) is individually disable-able via a
`disable_rule <Name>` line in the `--param-override` file (names in `paramoverride.h`
`PostScoringRule`). A disable is a clean skip of only that rule's block; default (no such
line) leaves every rule enabled, byte-identical to before the hook existed. This is
measurement-only for the Phase-2.2 dissolution audit (design D-7) — it retires no rule and
changes no committed value. (Since 2026-07-06 the enharmonic flip is one rule, **FM2**, whose
disable suppresses both its present-swap and append branches — Gate A is no longer separately
addressable.)

| Gate | Location | Trigger | Effect | Why it exists |
|------|----------|---------|--------|---------------|
| **Bias correction** | bias correction | Winner is bass-root Maj/Min, margin to best Maj/Min alt < `inversionSuspicionMargin` (0.70), `distinctPcs >= 3`. Seventh-exempt. | Deducts the bass-root bonus from the winner, re-sorts. | Bass-root bonus systematically over-fires on inversions; the correction removes the bonus only when it is the sole deciding factor. |
| **Enharmonic flip: Major-add6 → Minor7 (rule name FM2)** | flip region | `preferMinorOverMajorAdd6`, winner is Major+AddedSixth, target is Minor at `(rootPc+9)%12`. One `promoteToWinner()` call (`presentHint = bestAltIdx`, `stopBelowThreshold = true`): the present branch swaps the partner already carried at `bestAltIdx` (the former **Gate A**) and the append branch pulls it from `rawCandidates` above threshold (the former **FM2**). **Gates B/C/D removed (Stage 3.4b); Gate A unified into this one promotion (2026-07-06)** — the separate `GateA` rule retired, FM2 is the surviving rule name for the whole flip. | Swap the carried Minor partner, else build+append it from `rawCandidates`. | The two readings span identical PCs (e.g. Bb6 = Gm7/Bb); score cannot reliably distinguish in bass-heavy textures. Standard/Baroque prefer Minor. Present-first keeps the distinct partner as an alternative (no winner near-duplicate — §12 no information loss). |
| **E (first-inversion Minor → Major)** | Gate E | `preferMinorOverMajorAdd6`, winner Minor, alt Major at `(rootPc+8)%12`, stepwise bass present. | Swap. | F♯m winning when D/F♯ is correct (bass = M3 of actual root). |
| **G-E / G-D (Minor-add6 ↔ HalfDim7)** | G-family | `originalWinnerQuality == Minor && originalWinnerHasAddedSixth`, HalfDim7 at `(originalWinnerRootPc+9)%12`. G-E gates on key-function (viiø7/iiø7/iiiø7 — tested on the root, not the object); G-D on consecutive-stepwise temporal context (only when G-E does not fire). **(G-B and G-C RETIRED Stage 5, 2026-07-05.)** One `promoteToWinner()` call (`presentHint = kPromotePresentScan`, `stopBelowThreshold = false`) when G-E or G-D fires: present-scan swaps the carried HalfDim, else pulls it from `rawCandidates` (no threshold). The former "pull then pop if no sub-gate fires" is exactly the primitive's no-promotion path. | Swap the carried HalfDim, else build+append it from `rawCandidates`. | Sub-9a fix (`originalWinnerRootPc` capture). Cm6 vs Aø7/C is enharmonic; functional context selects the correct reading. |
| **H (augmented rotation)** | Gate H | Winner Augmented bass-root, `preferMinorOverMajorAdd6`, alt Augmented at `(rootPc+4)%12` or `(rootPc+8)%12`. Temporal gates. | Swap. | Augmented triads have 3 enharmonic rotations; context picks the correct one. |
| **I (first-inversion Major over root-position Minor)** | `kGateIMargin` | Winner Minor bass-root, alt non-root-position chord with same bass, root at I4 interval below bass, root diatonic, margin ≤ 0.45. | Swap. | Em winning when C/E is correct. |
| **L (Major over Augmented same-root)** | `kGateLMargin` | Winner Augmented (no 7th), alt Major at same root AND same bass, diatonic, margin ≤ 0.35. | Swap. | TYPE-A quality fix: bwv144.6 B+ → B, bwv245.15 E+ → E, etc. |
| **J (vii° → V7 completion) — runs LAST** | Gate J (last) | Winner is root-position Diminished triad (no dim7), the M3-below PC is sounding above `extensionThreshold`, alt is Major+m7 rooted there. | Swap to the dominant-7th reading. | Four PCs `{R-4, R, R+3, R+6}` are exactly V7 — a root-position vii° voicing the dominant root is, by construction, V6/5. |

**Retired gates (Stage 5, 2026-07-05 — §6-block dissolution audit, design D-7).** Each rule below
changed **ZERO winners across all three carriers** (Baroque/Jazz/Default; the 2.2b firing-site
ledger, `cc_stage5_phase2_2b_report.md` §1.2) and its removal is **corpus-byte-identical including
`alternatives[]`** (full-corpus regen ×3, 0 diffs — verified in 2.2c). The joint fit reached the
identical optimum with them disabled (Config II ≡ Config I, 2.2b §2). Retired in their own
user-ratified commits (2026-07-05):

- **F (second-inversion → root-position Major, alt at `(rootPc+5)%12`)** — the whole gate.
- **G-B (Minor-add6 ↔ HalfDim7 forward-evidence temporal fallback)** — one sub-gate of the
  G-family; G-E (key-function) and G-D (consecutive-stepwise) retained.
- **G-C (Minor-add6 ↔ HalfDim7 recent-root + stepwise-from-previous fallback)** — a second
  G-family sub-gate; G-E and G-D retained.
- **K (first-inversion Augmented over root-position Augmented, `kGateKMargin` ≤ 0.20)** — the
  whole gate + its margin constant `kGateKMargin`. Its founding case bwv40.6 (A+ → F♯5/A) is
  no longer touched by the rule (superseded upstream, 2.2b §1.3).

**Gate A — UNIFIED into `promoteToWinner`/FM2 (2026-07-06).** Gate A (Stage-5 Phase 2.2c) was
retired then restored because its naive removal, though **winner-byte-identical on all 352
scores**, changed the `alternatives[]` list on **36 Baroque scores**: Gate A re-ranked via
`std::swap(results[0], results[bestAltIdx])` (reusing the carried Major-add6 partner object),
whereas the retained FM2 append (`results.push_back(...)`) injected a freshly-built
near-duplicate of the *winner* and displaced that distinct partner — a §12 information-loss
regression on the L5-consumed carry. The resolution (this arc) unifies Gate A and FM2 into the
two branches of the **one** `promoteToWinner()` primitive: the present branch (`bestAltIdx`)
reproduces Gate A's swap byte-for-byte, the append branch reproduces FM2, so the whole flip is
**byte-identical to HEAD on the full output surface — winner AND `alternatives[]` — across all
352 scores × 3 presets** (0 net move, including the 36). The separate `GateA` rule (its enum
member, guard, name-map entry) is therefore removed; **FM2** is the surviving rule name for the
flip. Evidence: `cowork_gateA_unification_design.md`, `cc_stage5_phase2_2c_report.md`.

**RETAINED / DEFERRED dispositions (Stage-5 §6-block audit, user-ratified 2026-07-05; D-7).** Of the
rules NOT retired, the 2.2b cross-carrier evidence (`cc_stage5_phase2_2b_report.md` §1/§3.2) adjudicated:

- **RETAIN-as-structural (4):** **GateI** (disabling adds +5 class-(b) Jazz batch cases, §1.1), **FM2**
  (disabling adds the class-(b) case bwv227.7@18000, §1.1; since 2026-07-06 FM2 is the whole unified
  enharmonic flip, so its disable now also suppresses the former Gate A present-swap — a fortiori load-bearing),
  **GateJ** (disabling is catastrophic on Jazz —
  −0.4515 root; ON is WiR-correct at its V-family firing sites 33 vs 20, §1.4), **GateL** (inert on
  Baroque but 18 load-bearing Jazz firing sites, §1.2). Retirement is global, so a rule live on ANY
  carrier is retained.
- **DEFER — per-case verification / the spelling-aware gate (Stage 5/6) (5):** **BiasCorrection**
  (net-WiR-good but causes 3 class-(b) batch errors), **GateE** (Baroque-only, 2 sites), **GateH**
  (augmented-rotation class-(a) coin-flip), **GateGD** (1 held-out site), **GateGE** (class-b→class-a
  reshuffle). None retired this arc.

**`kHalfDimFirstInversionBonus` (= 0.55) — additive bonus inside the enharmonic-flip
block.** When the `preferMinorOverMajorAdd6` path (Gate-A / G-family region) identifies
a HalfDiminished **first-inversion** alternative as the best Minor-preferring reading,
its score is raised by `kHalfDimFirstInversionBonus` before the re-sort, so a genuine
Cm6 reading outranks the enharmonic Aø7/C first-inversion (Iter-61 "Option B", which
moved BIR=true 7→6). Located in `postscoringgates.cpp` (relocated to a file-scope
constant for the Stage-5 override mechanism — see the §1 note); fires only under the
`preferMinorOverMajorAdd6` flag (Baroque/Standard true, Jazz/Default false). It is a
§6-block dissolution target (Stage-5 family 2).

**Known asymmetries (pinned as-is in `postscoringgates_tests.cpp`, Stage-1b F4–F8):**

- **Mixed live/captured winner reads in H/I/K/L** — the Sub-9a fix migrated only
  G-E to the captured `originalWinner*` snapshot. Gate H requires live
  `winner.quality == Augmented` but captured `winnerBassIsRoot`; Gates I/K/L compare
  margins against the live (possibly bias-deducted) `winner.identity.score` while
  keying entry on `originalWinnerQuality`. After a bias re-sort these can refer to
  *different candidates*.
- **Gate F has no winner-quality and no pcWeight guard** (unlike Gate E): a Minor
  winner flips on a stepwise signal alone, and the promoted root does not need to
  be sounding.
- **G-E's `rawCandidates` pull has no threshold check** (`promoteToWinner(..., stopBelowThreshold
  = false)` for the G-family; the FM2 flip passes `stopBelowThreshold = true` so its loop breaks at
  `gateCtx.threshold`). Both preserved verbatim under the unified primitive.
- **Gate swaps can leave `results[]` unsorted** — after a G-E pull the alternatives
  list shown to users is not score-ordered. The winner is correct; the tail order
  is an artifact.

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

- **`w_stepIn`/`w_stepOut` has four gates, each load-bearing** — the
  `ScoringPhase::Final` call-site gate, root-position guard,
  first-inversion-m7-family surgical guard, power-quality exclusion. Each prevents
  a specific documented regression.

- **`ScoringPhase::Segmentation` must suppress all context-dependent bonuses.** Step,
  seq, and dim bonuses plus Gate R are all skipped in the Segmentation phase (gated at
  the `applyHarmonicFunction` call site, not inside the now-stateless bonus functions).
  Adding a new context bonus without gating it on `applyProgressionSignals` /
  `ScoringPhase::Final` will cause segmentation regressions.

- **Template arrays update atomically under `analysis::kTemplateCount`.** All
  array extents (template array, three score matrices, `kMasks`) derive from the
  constant since `a236a0ff21`, so the compiler enforces sizes. Adding a template =
  bump the constant + add the template/mask entries in the same edit (§9 step 5).
  The historical silent stack-buffer overrun from a missed matrix size is closed.
  (Stage 2.3 removed the `kDiagTemplates` mirror — one fewer site to keep in sync.)

- **Gate A subsumed Gates B/C/D — now removed (Stage 3.4b, historical); Gate A itself
  unified into `promoteToWinner`/FM2 (2026-07-06, §6a).** Gate A's entry conditions were a
  strict subset of B/C/D's, so B/C/D were unreachable dead code (Stage-1b F1). They were
  removed in the Stage-3 per-gate retirement audit (roadmap 3.4b) as a byte-identical change
  (0/353 × 3 configs, snapshots zero-diff). Gate A's swap later became the present branch of
  the unified `promoteToWinner()` primitive under the FM2 rule (byte-identical, full surface).
  Constraint going forward: do not add temporal conditions to the enharmonic flip — there is
  no longer a B/C/D safety net; any forward/window/consecutive-stepwise variant of the
  Major-add6 ↔ Minor flip must be reintroduced explicitly and tested.

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

**★ SIX FURTHER STANDING CONSTRAINTS AND DEAD ENDS, re-homed into this section 2026-08-07 on the
user's ruling. All six have this scorer and its gate layer as their subject, which is dormant on
both production surfaces; their status as constraints on what a future change may attempt is
unaffected by that (⚠ LEGACY subject, live constraint).**

- **A correction rule that can change a committed chord's IDENTITY is retired or folded in BEFORE
  the search is widened past it.** Where a later rule can change which root, quality or bass was
  committed, that rule is removed or absorbed into the scoring first; only then may the search be
  allowed to consider more alternatives. *Why:* stated with the decision — a rule that mutates
  root, quality or bass feeds the backward-looking evidence, so it cannot be cleanly separated from
  a wider-beam decode; a wider search would be reading a predecessor a later step is still going to
  change. The alternative — searching against uncorrected identities with a documented re-decision
  — was considered and not taken.

- **A WIDER SEARCH CANNOT FIX THE ARPEGGIO ROOT FAILURE — the wrong reading IS the global optimum.
  Recorded dead end; do not retry.** On the arpeggiated-harmony failures the locally wrong reading
  is not a weak transient a broader search would discard: it is the best-scoring node, so a broader
  search finds exactly what the narrow one found. Only **re-weighting** or a **different
  segmentation** can reach it. *Why:* derived from the search lattice and verified three times,
  including against an independent earlier derivation — on the founding score the continued-root
  path outscores the correct path, the gap being the root-continuity reward minus the margin, and
  the premise the earlier verdict rested on (that the transient scores low) is **measured false**.
  This is the dead end the two *tried and closed — do not retry* lists in `ARCHITECTURE.md` name;
  they point here and the rule is published once (#6).

- **Three prohibitions hold through every stage, and the per-gate RETIREMENT STAGE is the only
  sanctioned way these gates change:** no new gates, no threshold widening, no gating of the
  root-continuity bonus. *Why:* each prohibition carries its own defense elsewhere — accumulating
  gates are a warning sign and the answer is iteration rather than more gates; gate thresholds are
  Baroque-calibrated and are not loosened for another style; gating the root-continuity bonus on a
  sparse predecessor was measured a dead end (the bullet above). What this constraint adds is the
  **single sanctioned channel** — the retirement stage's per-gate differential proof obligation —
  which is what stops the gate layer changing by accretion.

- **The temporal signals sitting inside the vertical scorer STAY WHERE THEY ARE, and the gate that
  depends on one MOVES WITH THEM.** Several signals that look backward or forward in time are
  computed inside the part of the scorer that is supposed to judge only what sounds at one moment.
  They are known, documented debt and are **not** to be moved before a scoring-stabilisation phase;
  when they do migrate, Gate R has to move or adapt **simultaneously**. *Why:* stated with the
  recommendation and grounded in the mechanism — Gate R's test uses a score component as a stand-in
  for *this candidate has a sounding third*, and it carries that meaning only because one of those
  signals is computed where it is. Removing the debt without touching the gate would silently
  change what the gate tests: a cross-layer dependency invisible to anyone reading the gate's own
  file.

- **The policy for judging a PROPOSED post-scoring gate — three tests.** (1) If the proposal is
  another variant of correcting the bass-as-root bias, first ask whether the bias itself can be
  reduced, or whether functional context would remove the ambiguity; add the gate only if the fix
  is genuinely local. (2) If it turns on a **structural** condition — pitch-class arithmetic plus a
  presence constraint, not temporal evidence — it is likely architecturally sound. (3) If it needs
  the three-step cascade shape, that is a strong signal that the real problem is missing functional
  context, and the gate is the wrong answer. *Why:* derived from a systematic read of the whole
  gate population — two thirds of the gates were solving one problem, the scorer's bass-as-root
  pull, and three separate cascades were each built up step by step for the same shape of failure,
  which the canonical specification already names as the warning sign that accumulating gates
  signal an unresolved architectural problem. The two gates that read came out architecturally
  healthier both turn on structural conditions rather than compensating for the bias, which is
  where test (2) comes from.

- **Two of the post-scoring gates are PURELY-LOCAL VERTICAL refinements and must SURVIVE the
  dissolution; the others dissolve into the competition. Recorded DEFERRED.** Most of the
  after-the-fact repair steps exist only because the decision preceding them could not see enough
  context, and they disappear once that decision can. Two do not: they refine the reading from the
  notes alone and compensate for nothing, so they are carried across rather than deleted alongside
  the others. *Why:* measured at the code rather than assumed from the design — of the live gates,
  ten read context from beyond their own stretch and are compensation by construction, three were
  already dead code, and the two named ones read nothing outside the sonority. **The dissolution
  was never executed on this path** — the production estimator replaced the pipeline instead — so
  the constraint stands DEFERRED and what it says about those two gates is a fact about this code
  that the retirement map still has to dispose of (#12). One bookkeeping fact a reader needs: the
  *partner-present* half of one of the two named gates has since been unified into the single
  promotion primitive (§6a), so the surviving rule name for that flip is FM2; the unification did
  not perform the dissolution and does not discharge this constraint.

### The fine-grain function override — falsified, its repair refuted, its principled restriction un-computable, and a redesign recommended but NOT adopted

**★ Four findings re-homed into this section 2026-08-07 on the user's ruling, kept together because
they are one evidence record about one mechanism.** The mechanism is the late correction pass that
overturns a committed chord when the surrounding progression argues against it. ⚠ **LEGACY subject,
and narrower than "legacy" reads:** checked at the code, it is **not reachable on any production
surface, and not on the plain legacy batch path either** — it survives behind a return-early
diagnostic dump flag and the test suites. Nothing below is running today.

- **FALSIFIED — no threshold can make the override net-positive.** Whether a fire helps or hurts is
  unrelated to either quantity its trigger is built from: the incumbent reading's confidence and
  the strength of the progression contradiction. Since the only tunable knob scales the bar by that
  confidence, **no setting separates the cases it fixes from the cases it breaks**, and the best
  measurable setting simply switches the pass off. *Why:* measured and stratified rather than
  argued, on a ground-truth-aligned population of fires — the harm rate is essentially flat across
  the contradiction value and **rises** with the incumbent's confidence, so the one available lever
  pushes the wrong way; the mechanism of the harm is named too, the fourth- and fifth-related root
  moves the progression score rewards accounting for most of both the fires and the harms.
- **REFUTED — making the comparison vertically fair does not repair it.** The obvious repair is to
  let the pass overturn a reading only when the replacement fits the sounding notes at least as
  well. Measured, that band is still overwhelmingly harmful. The problem is not that the comparison
  was unfair; it is that **the progression contradiction does not predict which root is correct at
  these moments**. *Why:* measured across bands of the vertical gap, every one net-negative, with
  the count and harm rate per band; the conclusion drawn is the one the numbers support and no more
  — the earlier layer's vertical commit is a better predictor of the annotated root than the
  progression re-pick, even where the alternative is its vertical equal.
- **UN-COMPUTABLE, not merely unmeasured — the principled restriction cannot be built today.**
  Restricting the override to the genuinely coupled key-and-chord minority is the principled form,
  and its trigger **is not computed anywhere**. The binding blocker is the component that asks
  whether a different carried KEY alternative flips the chord reading: that needs a per-key chord
  re-decode, which **is** the joint key-and-chord step the record says is still owed, and the
  closest existing mechanism explicitly leaves the chord unchanged. *Why:* established at the code,
  both components separately; surfacing the trigger would mean **building** the joint step, which
  the standing sequencing rules forbid at this stage. So the verdict is un-computable rather than
  unmeasured, and this option is a long-run successor rather than a near-term choice.
- **RECOMMENDED AND NOT ADOPTED — demote the override to an ANNOTATION.** The recommendation on the
  evidence above is to stop overturning the committed chord and instead **record that the
  surrounding progression disagrees**, leaving the chord alone — accuracy-equivalent to simply
  disabling the pass, while keeping the disagreement as calibrated uncertainty a later stage can
  use. Tightening the trigger and repairing the comparison are both rejected as measured
  net-negative. **This is a PROPOSAL, not a specification of this document: it is NOT adopted, and
  no reader may implement it from this paragraph.** It is recorded as an INPUT to the one
  prioritized fix plan, and the row that owns the demotion carries the cross-reference on the
  plan's side. *Why:* every clause of the recommendation is measured and cited in the bullets
  above; the loss it accepts — a modest number of genuine corrections given up — is stated and kept
  in view rather than netted away.

### Bass-as-root promotion — SHELVED WITH EVIDENCE, and the cascade the attempt exposed

**Re-homed into this section 2026-08-08 on the user's ruling; the shelving and its evidence are
intact.** ⚠ **LEGACY SUBJECT:** both statements are about this document's scoring surface and its
greedy-expand segmenter. Whether the joint estimator's modelled segmentation shows the same coupling
is **not stated here and is not asserted.**

- **The information that disambiguates the third-above reading is NON-LOCAL, so no local
  discriminator can exist — the approach is shelved, the problem is not.** Where C-E-G may be a C
  chord or an E-minor chord inside something larger, and A-C-E likewise, nothing this scorer can see
  at the moment of scoring — the sounding pitch classes, their weights, the templates, the key —
  separates the two readings. What separates them is the surrounding music: the following chord's
  root, the preceding chord's identity, and whether the bass falls on a strong beat. *Why the
  shelving is with evidence rather than on argument:* two discriminators were built and both
  regressed — a simple stack raised the wrong-root count on the primary corpus and a more elaborate
  one raised it further, its wider margin overpowering its own added tightenings — and the cases
  where the third-above reading is CORRECT proved indistinguishable from the cases where it is wrong
  on local evidence, with a sample of the regressions flipping one wrong answer into a different
  wrong answer. No code change was committed. **What is shelved is the LOCAL-GATE approach, not the
  problem**; the two future angles the record names — a pass that reads the surrounding regions'
  roots, or a temporal-context gate keyed on the neighbouring roots — are neither scheduled nor
  endorsed here.
- **A chord-level change is NOT confined to the cases it fires on: chord identity drives boundary
  placement, so it produces downstream RE-SEGMENTATION artifacts in regions it never touched.**
  Where one region ends and the next begins depends partly on what the chords are, so changing one
  chord's identity — even changing it correctly — makes the adjacent regions re-merge differently,
  and readings that were right can become wrong where the change never looked. **Counting only the
  cases a change fires on therefore understates its effect, and this is structural rather than a
  condition that can be tightened away.** *Why it is stated here as a standing constraint:* it was
  measured at the attempt above, where some of the regressions were not gate fires at all; and it is
  the reason the governing regression stop is an EXPLAINED PER-RUN DIFF rather than a count — an
  effect outside the cases a change fires on is exactly what an enumeration of added and removed
  runs catches and a count does not.

### The quality-overwrite information loss is TOLERATED until the gate-dissolution step — tolerated is not forgotten

**Re-homed into this section 2026-08-08 on the user's ruling.** ⚠ **LEGACY SUBJECT:** the passes
this governs are this document's post-scoring passes on the legacy chord path; the joint estimator
that produces the committed reading does not run them. **Whether the acceptance still has a subject
at HEAD is not stated here and is not asserted.**

Two post-scoring passes change the chord quality the scorer committed and keep no record of what
they replaced, which is an information-loss violation (#12). **The verdict is to TOLERATE it until
the gate-dissolution step, with the violation kept VISIBLE in the open-items register — tolerated is
not forgotten.** *Why, as a derivation from three principles rather than a preference:* removing the
overwrites now would be a production behaviour change with no replacement owner, since no component
yet owns deciding quality from the key — which is the cross-layer patch layer adherence forbids
(#7); and #8 puts the structural work first. Deferring to the step that gives the concern a single
home makes the removal ONE ratified, revertible change under the regression stop (#14/#15). The
alternative — ripping the overwrites out now — was considered and rejected on exactly that ground.
**The open-items register row is the mechanism that makes this an acceptance rather than an
oversight**, and it gates the dissolution.

### Four measured dead ends of the segmentation-and-root path — do not retry any of them

**Re-homed into this section 2026-08-08 on the user's ruling; every ⚠ LEGACY mark intact.** ⚠ **All
four are LEGACY-SCOPED:** their subject is this document's scoring surface and the segmenter awaiting
deletion. Each was measured, and each is a prohibition on re-attempting a specific mechanism —
**none of them says anything about extending the temporal context the analysis reads**, which is a
decided live capability specified elsewhere.

- **Do not retry the backward-walk boundary change.** Counting notes that stop exactly where a
  stretch begins as belonging to that stretch was tried, in the hope of recovering a missing chord
  root. *Why it is closed:* measured — the notes touching the boundary are OTHER chord tones and the
  root attacks later, so the change would add the wrong pitches and still not add the missing one;
  and the same backward walk serves a dozen call sites, several of them notation display, where
  excluding the previous chord's terminal notes is the correct behaviour. **This is a
  boundary-membership dead end ONLY.**
- **Do not retry a short-region external merger.** A proposed after-the-fact pass merging very short
  neighbouring stretches was tried and closed. *Why:* measured — the trigger never fires, because
  the same-root merge already inside the first pass has combined those stretches before any external
  pass could see them. It was dead code.
- **Do not retry any tone-aggregation approach to the arpeggio root failure.** Pooling an arpeggio's
  notes and re-reading the chord from the pool was implemented, measured and reverted. *Why:*
  pooling makes the answer worse — the aggregate is duration-weighted and the wrong pitch sounds
  longer than the right one, so the wrong root still wins the pooled reading, and the run regressed
  both presets. **The evidence was never the problem:** the vertical scorer already prefers the
  correct root over the stretch where that root actually sounds; what is wrong is the predecessor
  signal.
- **Do not retry the absent-root guard.** A rule rejecting any chord whose own root is not sounding
  was built, measured and reverted entirely. *Why:* it fixed fewer cases than it broke, and two of
  the cases it broke are readings the published human analysis itself makes with an absent root — so
  **the premise "an absent root means a wrong reading" is false corpus-wide.** A second, structural
  reason rides with it: any guard that changes a committed root changes the predecessor every later
  stretch reads, so its effect cascades into regions it never judged. The counts are in the record
  and are not restated here (D-431).

### The validation basis of every hand-set scoring magnitude on this surface is retroactively VOID

**Re-homed into this section 2026-08-08 on the user's ruling.** ⚠ **LEGACY SUBJECT:** the magnitudes
are this document's own; the joint estimator is the production inference layer, and **whether its
fitted tables inherit the same standing is NOT stated here and is not asserted.**

**Nearly every live scoring magnitude on this surface was hand-set, and the only check that ever
validated it was a regression gate later proven to under-count true per-onset root error by a large
factor and to have been reading a then-buggy ground-truth parser. Under #19 the validation basis of
these values is therefore retroactively void: they are UNFALSIFIED, NOT ESTABLISHED.** *Why the
reading is "unestablished" rather than "wrong", which is a different claim and the record supports
only the first:* the same audit measured a third of the reachable constants inert at the root
objective, and both high-leverage re-fit candidates regressed held out. So nothing here says the
values are bad; what it says is that nothing in the record shows they are good. The under-count
factor and the inert fraction are in the audit that measured them and are not restated (D-431).

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

5. **Bump `analysis::kTemplateCount` and add the matching entries.** All array sizes
   derive from the constant, so the compiler enforces them — there is no longer a
   loose literal to forget:
   - bump `analysis::kTemplateCount` (`chordanalyzer.h`) N → N+1. This automatically
     resizes the three score matrices and the derived `kMasks`; no per-array size edit is
     needed.
   - add the new template's interval row to `analysis::kTemplateIntervals` (`chordanalyzer.h`),
     pad with trailing `-1` to `kMaxTemplateTones`. **This is the single interval source** —
     Gate R's `kMasks` is derived from it via `makeTemplateMasks()`, so there is no separate
     bitmask to hand-write (the former silent-disable hazard is closed). Every row includes
     interval 0 (the root); the `bassIsTemplateChordTone` byte-identity `static_assert` lists
     the frozen mask values — extend it with the new template's mask.
   - add the new entry to the `analyzeChord` `templates` array (quality + intervals +
     `tpcDeltas`). Its intervals **must match** the `kTemplateIntervals` row you just added;
     the independent table test in `gater_tests.cpp`
     (`BassIsTemplateChordTone_TableMatchesEveryTemplate`) cross-checks the derived masks
     against an independently-encoded interval list and fails if they disagree.
   - add the human-readable name to `diagTemplateName` in `tools/batch_analyze.cpp` (its
     `static_assert` against `analysis::kTemplateCount` fails the build otherwise) — a
     display-only diagnostic site, not a scoring site.

   (Stage 2.3 removed the `kDiagTemplates` mirror: `diagnoseChord` now replays the
   production pipeline, so there is no second template array to keep byte-identical.)

   Failure modes after this change: adding a TemplateDef entry **without** bumping the
   constant is a compile error (too many initializers); bumping the constant **without**
   adding the TemplateDef entry value-initializes a trailing all-zero template (silent —
   so always add the entries in the same edit). The `static_assert`s catch a re-hardcoded
   literal size.

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
chord label. Since E2d it is called from inside `analyzeChord()` itself as
`applyHarmonicFunction(..., prefs.scoringPhase)`; the phase parameter — not a
separate caller-side gate — decides whether the progression signals apply
(`ScoringPhase::Segmentation` for `greedyExpandSegmentation`'s exploratory calls,
`ScoringPhase::Final` otherwise). (Historical: in E1/E2 this was three explicit
`!prefs.explorationMode`-gated calls in `regionanalyzer.cpp`; see §11.)

`HarmonicFunctionContext` carries: `previousRootPc`, `nextRootPc` (plus the Step 1/2
predecessor channels). It deliberately carries **no** key fields — key influence is
already frozen into `ScoringCell::basisIndep` and reaches the gates via
`ScoringSnapshot::{scale,keyTonicPc,keyMode}` (the former write-only `keyFifths`/`keyMode`
fields were removed in Stage 0.2). Extended in E4 with phrase-boundary and cadence evidence.

**E1 (current):** Pass-through. No changes to `ChordAnalysisResult`.

**E2 (done):** The three progression signals (`rootContinuityBonus`, `w_seq`,
`w_dim`) no longer live in `chordanalyzer.cpp`. They are applied by the
competition pipeline `applyHarmonicFunction()`; see section 11.

**E3 (done, 2026-06-06):** Post-scoring gates A–L extracted from `analyzeChord()`
into `applyPostScoringGates()` (in `postscoringgates.cpp` since refactor #1; originally
`chordanalyzer.cpp`). The new execution order at every production call site is:

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

The atomic-update checklist (section 9) is unchanged by this redesign (no templates
added or removed). Stage 2.3 later shrank it from four scoring sites to three by removing
the `kDiagTemplates` mirror.

**Diagnostic view (Stage 2.3).** `diagnoseChord()` is a VIEW into this pipeline, not a
parallel scorer. It calls the real `analyzeChord` (capturing the `ScoringSnapshot` via the
new `snapshotOut` param, mirroring `gateCtxOut`) then the real `applyIter8691Pedal` +
`applyPostScoringGates`, and decorates the result with three labeled layers — ORACLE
(snapshot cells), COMPETITION (winning bass group's progression-signal terms incl. the
Gate R outcome, scores from the pipeline's `rawCandidates`), and POST-GATES (which stage
moved the winner). Its `finalWinner` is the production winner by construction; the
catalog-wide agreement invariant is pinned in
`chordanalyzer_musicxml_tests.cpp::DiagnoseMatchesProductionPipeline`. The old diagnose
scorer (its own `kDiagTemplates` array + the rcb-folding `contextualBonuses` helper, both
removed) had no Gate R / w_seq / w_dim / threshold and mis-led two investigations.

**Beam-1 decoder (Stage 3.1).** Winner selection and the left-to-right commit chain now flow
through the **beam-1 chord-path decoder** (`analysis/decode/chordpathdecoder.h`), behind the
`ChordAnalyzerPreferences::decodeQualityLevel` knob (default `DecodeQualityLevel::FastBeam1` =
level 0). This is a **byte-identical re-expression** of the greedy commit chain, not a behavior
change: the decoder encapsulates the path state the region loop (`regionanalyzer.cpp` Pass 1 /
Pass 2 / Pass 2b) threaded by hand — the `ChordTemporalContext`, the rolling stepwise counter,
and the recent-roots window — and replaces `advanceTemporalContext()` at all three commit sites
with `decoder.commit()`. Crucially, **the decoder computes no score**: emission (`analyzeChord`
→ `ScoringSnapshot`) and the per-bass / cross-bass competition that selects the winner
(`applyHarmonicFunction`, this §11 pipeline) run upstream of `commit()` and are untouched, so
the FP-sensitive score expression
`(basisIndep + rcb + basisDep) × cf × af + wComplete + wSeq [+ wDim] [+ steps]` is not
re-associated and the near-tie tripwires (Δ=+7b, bwv320) cannot flip. The decoder is
cache-READY (it accumulates a returnable decoded path) but **not cached** at 3.1; decode-once /
query-many is 3.1b. Levels > 0 (Normal / Deep, wider beam) are **not yet active** — they behave
as `FastBeam1` until Stage 3.2. **`docs/decoder_design.md` is the authoritative structure
reference** (lattice shape §2, emission/transition factorization §3, beam-1 byte-identity
argument §4, path-state ↔ `advanceTemporalContext` mapping §5).

**Oracle temporal-signal migration (Stage 3.3).** The last five oracle-side progression
signals — `resolutionBonus` and the four §4.1b inversion bonuses (`stepwiseBassInversion`,
`stepwiseBassLookahead`, `sameRootInversion`, `completeTriadInversion`) — have **migrated
out of `analyzeChord` into the competition pipeline** (`fn::resolutionEdgeBonus` +
`fn::inversionContextBonus`), joining `rootContinuityBonus` (moved at E2d) and `w_seq` /
`w_dim` / step bonuses. The oracle is now **genuinely vertical**: it applies NO progression
signal (the chordanalyzer.h temporal debt / audit Finding 1 is cleared). The oracle's
`bassIndependentContextualBonuses` / `bassDependentContextualBonuses` helpers are gone;
`bassIndep` carries only vertical + `diatonicRootBonus` (via `diatonicRootContribution`),
`basisDep` carries only `nonBassAdjustment + appliedBassBonus`, and the vertical
inversion-eligibility predicates ride along as two per-cell flags
(`supportsInversionBonuses` / `qualifiesCompleteTriad`). The pipeline reconstructs the
score in the SAME arithmetic positions (`fullBasisIndep = basisIndep + resolution`,
`fullBasisDep = basisDep + inversionContextBonus`, both inside the `(… + rcb + …) × cf × af`
group). **Byte-identical**: the basisDep reconstruction is bit-exact (the bass-root bonus
and the inversion sum are mutually exclusive, so the reassociation has an always-zero
middle term); the resolution reconstruction is a ≤1-ULP reassociation confined to non-tie
Maj/Min cells. **Gate R** was redesigned in the same commit to read the reconstructed full
basisDep (reconstructed-credit, §4) — byte-identical, closing the cross-layer dependency.

---

*Last updated: 2026-06-12 — Stage 3.1: winner selection + commit chain now flow through the
beam-1 chord-path decoder (`analysis/decode/chordpathdecoder.h`) behind the
`decodeQualityLevel` knob (default `FastBeam1`); byte-identical re-expression of the greedy
commit chain (no score computed in the decoder), cache-ready but not cached, levels > 0 not yet
active. `docs/decoder_design.md` is the authoritative structure reference. Prior: 2026-06-11 — Stage 2.3: `diagnoseChord` replays the production pipeline
(`analyzeChord` gains `snapshotOut`; `kDiagTemplates` + `contextualBonuses` removed; the
atomic-update site list drops from 4 to 3). Prior: 2026-06-08 — Gate R (rcb bass-chord-tone guard) added to §4 and §9
(5th atomic-update site, `kMasks`). Withholds `rootContinuityBonus` from a candidate
whose bass is foreign to its own template — fixes the Δ=+7b cluster (bwv245.28,
bwv296, bwv320). Prior: 2026-06-06 — E2d redesign: scoring-oracle /
competition-pipeline split. `analyzeChord()` is now a vertical-only oracle;
`applyHarmonicFunction()` owns winner selection, threshold, result cap and
gate-context construction. Removed `suppressProgressionSignals` /
`captureScoringSnapshot`. New section 11; section 4 (`rootContinuityBonus`) +
section 10 (E2) updated. Prior: E3 extracted `applyPostScoringGates()` from
`analyzeChord()`.*
