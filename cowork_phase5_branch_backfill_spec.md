# Phase-5 branch-backfill spec — the STABLE-half triage (2026-06-26)

> **What this is.** The triage of the **stable** ~400 unhit branch directions from the union branch-coverage baseline
> (`cc_union_branch_coverage_report.md`, 82.12% / 999 unhit). "Stable" = files the Phase-5b L4 build / Phase-6
> retirement will **not** reshape (sealed L1/L1.5/L2, the L4 scoring oracle + formatter, L3 emission/sequence/format).
> The moving ~600 (orchestrator, legacy segmenter, unwired decoder, gated detectors, section) is deferred to Phase 6.
>
> Produced by four parallel **file-tools-only** reads of the live source; every classification cites source, and every
> ADD-TEST carries an **oracle** (music theory / documented contract), never an echo of current output. **This is the
> spec for the Phase-5 coverage backfill (round 2) CC instruction.**

## Headline — stable-half disposition (~403 directions)
- **ADD-TEST ≈ 321** — real test-gaps; reachable logic with a decidable oracle. → the Phase-5 backfill.
- **EXCLUDE-DEFENSIVE ≈ 62** — deliberate can't-happen guards (null/bounds/exhaustive-enum-default/upstream-invariant).
  → annotate as intentionally-unreachable; **never test, never delete.**
- **DEFER ≈ 16** — 6 legacy `collectPitchContext` arms (→ Phase 6 with the pitch-context collapse); 8 `chorddiagnose`
  decoration arms (diagnostic-only, don't affect `finalWinner` — low value, optional); 2 `formatNashvilleNumber`
  chromatic-"?" placeholders (labelled regression-guard only, the known placeholder — real fix is later).
- **L1/L2 residual (4):** `note_model.cpp` (3), `slicer.cpp` (1) — tiny residual in heavily-tested sealed files;
  classify at write-time (likely defensive + ≤1 add-test).

> **Coverage ≠ correctness still governs:** ADD-TEST means "write a test asserting the *oracle* value." If the oracle
> fails against current code → surfaced defect (xfail + flag), not a weakened assertion (per the backfill rules).

## ADD-TEST gaps by file (oracle in brief; full per-branch detail reproduced from the triage reads)

### L1.5 engraving bridge / cross-cutting (ADD-TEST 53)
- **`regiontonecollector.cpp` (16):** the `passes`/eligibility false-arms — note on **excluded staff / non-playing /
  invisible** is dropped from the PC view; **stressed mid-bar beat → 0.85** metric weight; **dense-start** sustain-in
  vs onset-at-start tallies + distinct-PC dedup; zero-duration edge-clip contributes nothing; **pedal-tail** present +
  dense-start interaction; `pedalTailWeightMultiplier==0` → pass is a no-op.
- **`regiontonecollector.h` (4):** chord-track-named part excluded; ordinary instrument eligible; **hidden staff** /
  **drumset staff** ineligible.
- **`regiontoneprimitives.cpp` (25):** `soundingAt` eligibility drops (excluded/non-playing/invisible/grace);
  `pitchContextOverSpan` excluded-staff drop; **onset-sub-boundary** + **bass-movement** detectors: onset-only (not
  sustained), rests/grace excluded, non-playing/invisible excluded; `findTemporalContext` stepwise-bass to-prev/to-next
  flags, end-of-score (no forward context), prior/next rest-only segment skipped. *(NOTE: the 6 `collectPitchContext`
  arms are DEFER — legacy, Phase 6.)*
- **`metricweights.cpp` (8):** compound-meter stressed beat → compound-stressed pref; stressed → 0.85; non-pedal
  spanners (slur/hairpin) not indexed; **sostenuto/soft pedal excluded** from sustain windows; pedal outside region /
  degenerate-length skipped; pedal on excluded staff skipped; same-start pedals ordered by end tick.

### L4 scoring oracle + gates (ADD-TEST 98)
- **`analysisutils.h` (3):** `ionianTonicPcFromFifths` table (Cb/A/F# majors) — one parametric test over fifths −7..+7.
- **`chordanalyzer.cpp` (8):** add#9 vs m3 disambiguation; #13 on diminished suppressed; 6/9 negated by min7/maj7
  present; missing-TPC → default extension; lowest-pitch bass dedup; below-`bassMinWeight` → lowest-pitch fallback;
  root-absent candidate → no triad-complete bonus.
- **`chordanalyzer.h` (11):** empty-tones no-op merges; same-PC tpc backfill; ≥2 isBass → lowest-pitch bass;
  `advanceTemporalContext` sentinels (rootPc<0 → 0.0; empty candidates → 0.0; <2 → −1 margin); gates-empty → root −1.
- **`postscoringgates.cpp` (50):** every gate's **fire vs below-threshold-no-fire** outcome — Gates A/FM2, E, F,
  G-B/C/D/E, H-B/C/D, I, J, K, L (each `continue`/skip arm and each fire arm is a distinct, oracle-decidable outcome;
  the single richest cluster).
- **`chordpostpasses.cpp` (16):** `cptIsBassChordTone` per-quality bass-is-chord-tone vs pedal; Iter86/Iter91 `bassPc<0`
  no-ops + the bass-as-root promotion pattern guards; sparse-region pedal `bassPc<0`.
- **`chordvoicing.cpp` (6):** flat/sharp-fifth on non-perfect-fifth quality; half-dim+Maj7 dup avoidance; added-6 as 13th
  skip; bass octave-up near midpoint.
- **`harmonicfunctionlayer.cpp` (3):** resolution-edge known-quality but prevRoot<0 → 0.0; winner-root≠bass (already an
  inversion) → no forced diff-root append; no above-threshold candidates → chosenResult unchanged.

### L4 chord-symbol formatter (ADD-TEST 98) — `chordsymbolformatter.cpp`
Formatting variety; oracle = the standard chord-symbol / Roman / Nashville rendering. Clusters:
- **Pitch-class spelling (16):** Cb/Fb (+German Ces/Fes) flat-range spellings; A#→Bb normalization by key; key-sig
  TPC-honoring G#/Ab split; ≤−5/−6-flat enharmonic spellings.
- **Quality suffix (38):** m69/sus269; Maj#11, Maj7b9; dom b13/#11/b9/#9, 7b9/7#9; add#11/addb9/add#9; mMaj7add13,
  mMaj7, mb13, mb9/m#9, m7#9, madd#9; aug Maj7#5b9; sus2 ladder 13/11/9/7sus2; sus4 alterations; b5 suppression rules.
- **Roman numeral (11 diatonic + 2 chromatic + 5 inversion):** out-of-range degree → ""; add6 vs 69; half-dim
  alterations (iiø7b9 etc.); sus+Maj7 "M"-insert; (add13)/(addb9); **#iv** sharp-fallback chromatic numeral; **I64**
  second-inversion + root-position/inv≤0 unchanged.
- **Core intervals (4):** sus2 {0,2,7}, sus4 {0,5,7}, power {0,7} (inversion-figuring inputs).
- **Bass-name validator (5):** reject null/non-uppercase/bad-accidental/too-long → slash omitted.
- **formatSymbol/RomanNumeral tail (12):** Maj7sus requalification true/false; slash-bass omitted on invalid/out-of-range
  bass; tonicization vii°7/x & viiø7/x glyphs; chromatic-degree-not-in-scale → tonicization suppressed.

### L3 key/mode (ADD-TEST 72)
- **`keymodeformatting.cpp` (30):** the **exact display-name + suffix contract** for all 21 modes (tonic name per mode
  at a key sig; suffix strings "Dor"/"Phryg"/"Lyd♭7"/… ). This is a user-visible label contract — assert each string.
- **`keymodeanalyzer.cpp` (26):** scale-membership `inC&&!inKS` / `!inC&&inKS` arms; **pairwise relative maj/min
  disambiguation** (complete-triad-vs-tonic-only bonuses/cost); declared-"minor" accepts minor-class modes;
  `keySignatureFifthsForKey` table; out-of-range key-sig → global-argmax fallback; tonal-center override suppression
  when raw winner materially stronger; runner-up emission; single-result confidence. **★ Two arms (347/354) are the
  brittle leading-tone presence-gate (L3 §11) — pin as a LABELLED regression-guard, do NOT assert correct; the fix is
  Phase B.**
- **`keymodesequence.cpp` (16):** empty-context slice → neutral row skipped; `stateIndexForResult` not-found → skip;
  single-state lattice → confidence-vs-0; empty emissions/states → {}; **`maxAlternatives<=0` → all alternatives
  emitted**; pinned/redecode margin exclusions; single-viable-state → `kSingleStateConfidence` (certain, not uncertain).

## EXCLUDE-DEFENSIVE (≈62) — annotate, don't test, don't delete
Categories (all upstream-invariant / can't-happen): null-score/measure/segment guards (`metricweights` ×~9,
`regiontonecollector` measure-less fallbacks ×4, `regiontoneprimitives` `!firstSeg`/empty ×3); malformed-time-sig
guards; **exhaustive-enum `default:`** arms (`chordanalyzer` factory, `chordvoicing` ×2, `chordsymbolformatter` 406/512/650,
`keymodeanalyzer` 183/405, `keymode*` size-clamps); upstream-invariant fallbacks (`harmonicfunctionlayer` empty-group /
winBassPc<0; `chordanalyzer` no-tones bass fallbacks; the **author-documented broken-chain guard** `keymodesequence:313`);
the provable aug-triad tautology (`chordanalyzer:857`); alternate-TPC-encoding / >1-semitone-chromatic guards in the
formatter. **Borderline (reviewer discretion):** a few all-rest-region / OOB-staff guards the agents leaned defensive
but a fixture *could* reach — promote to ADD-TEST only if cheap.

## DEFER (≈16)
- **6** `regiontoneprimitives::collectPitchContext` arms → **Phase 6** (collapses with the legacy pitch-context builder).
- **8** `chorddiagnose.cpp` decoration arms → diagnostic-only (don't alter `finalWinner`); optional, low value.
- **2** `formatNashvilleNumber` chromatic-"?" → the known placeholder; labelled regression-guard only.

## How this folds into the plan
- The **ADD-TEST ≈321** is the **Phase-5 coverage backfill (round 2)** — a CC instruction that writes these tests with
  the oracles above, under the same rules as the first backfill (oracle-asserted, xfail-on-defect, byte-identical
  production). Big enough to split by file-cluster.
- The **EXCLUDE ≈62** is an **annotation pass** (mark intentionally-unreachable in the coverage config / source
  comments) — part of the Phase-6 criterion-4 seal, but the *list* is fixed now.
- The **DEFER ≈16** routes to Phase 6 (collectPitchContext) or stays a labelled guard (Nashville) / optional
  (chorddiagnose).
- After this stable-half backfill lands, the *moving* ~600 is triaged at Phase 6 (post-build), and the union
  criterion-4 number is re-measured for the final seal.
