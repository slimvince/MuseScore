# CC Report — Stage 3.3: oracle temporal-signal migration + Gate R redesign

> Atomic commit, held for Cowork ratification. Base `4f1754c26c`. Roadmap 3.3 /
> `docs/decoder_design.md` §6. Reconstructed-credit Gate R per Cowork decision
> (2026-06-12). **Byte-identical: 0/353 × 3 configs, snapshots 11/11 no-refresh, all
> suites green, BIR identity sets exact ×3.**

---

## §1 — THE PLAN (Task 1, load-bearing)

### 1.1 The exact current composition (documented to the addition)

The per-bass score the competition pipeline computed (pre-3.3,
`harmonicfunctionlayer.cpp` Pass A + Pass B):

```
newBasisIndep = cell.basisIndep + rcb;                       // rcb folded in
scoreNoWDim   = (newBasisIndep + cell.basisDep) * cf * af;
scoreNoWDim  += cell.wCompleteBonus;
scoreNoWDim  += wSeq;                                         // forward edge
wDimDelta     = wDim;                                         // forward edge
perBassWith   = scoreNoWDim + wDimDelta;
// Pass B: cand.score += stepIn + stepOut;
```

i.e. `((basisIndep + rcb) + basisDep) × cf × af + wComplete + wSeq [+ wDim] [+ (stepIn+stepOut)]`.

**Where the five migrating signals lived (quoted):**

- **`resolutionBonus` (+0.35) → `basisIndep`.** `bassIndependentContextualBonuses`
  returned `diatonicRootBonus + resolutionBonus`; that return was the **last addend** of
  `basisIndepMatrix = scoreTemplateTones + scoreExtraNotes + dim7Char + structuralPenalties
  + tpcConsistency + helper`. So `basisIndep_old = V + (d + r)` (left-assoc chain; helper
  return groups `d` and `r`). The three resolution cases (prevDim→Maj/min @+1,
  prevHalfDim→Maj @+5, prevAug→Maj/min @same) are mutually exclusive on `previousQuality`.

- **The four inversion bonuses → `basisDep`.** `bassDependentContextualBonuses` accumulated
  `inversionContextBonus` in the order **completeTriad, stepwiseInversion,
  stepwiseLookahead, sameRoot**, then `score += min(inversionContextBonus,
  maxTotalInversionContextBonus)`, with `score` starting at `appliedBassBonus`. The call
  site folds it as `basisDep_old = nonBassAdjustment + (appliedBassBonus + cappedInv)`, i.e.
  `nb + (bb + cappedInv)`.

### 1.2 What the pipeline needed that it didn't have

- **Temporal conditions** were already in `HarmonicFunctionContext` (`previousRootPc`,
  `previousQuality`) **except** the two bass-stepwise booleans the inversion bonuses read.
  Added `bassIsStepwiseFromPrevious` / `bassIsStepwiseToNext` to `HarmonicFunctionContext`,
  forwarded verbatim from `ChordTemporalContext` in the `fnCtx` block (null-context → false).

- **Vertical predicates stay oracle-side as per-cell flags** (Cowork's split): the oracle
  publishes `ScoringCell::supportsInversionBonuses` (= `supportsContextualInversionBonuses`,
  a pure pitch fact: inverted Maj/Min/Aug/HalfDim with a sounding third) and
  `qualifiesCompleteTriad` (= `qualifiesForCompleteTriadInversionBonus`), **each ANDed with
  `hasStructuralBass`** so the region-level structural-bass gate (the old
  `if (context && hasStructuralBass)` guard) is preserved. Both are pure vertical facts.

### 1.3 FP-preservation argument (the load-bearing claim)

- **basisDep — byte-identical BY CONSTRUCTION.** `bb` (`appliedBassRootBonus`, requires
  `rootPc==bassPc`) and `cappedInv` (every inversion bonus requires `rootPc!=bassPc` —
  verified in both eligibility predicates) are **mutually exclusive**: at all times one is
  exactly 0. So `(nb+bb)+cappedInv ≡ nb+(bb+cappedInv)` bit-for-bit (the zero middle term
  makes the reassociation exact). The pipeline recomputes `cappedInv` with the **same term
  order + same `std::min`** and folds `fullBasisDep = cell.basisDep + cappedInv`.

- **basisIndep — one ≤1-ULP reassociation `(V+d)+r` vs `V+(d+r)`**, present only on cells
  where diatonic AND resolution both fire (Maj/Min, diatonic root, resolution target).
  Disjoint from every documented tie/near-tie class: the Sus4♭5/HalfDim exact ties don't
  fire resolution (not Maj/Min); Δ=+7b / bwv320 are basisDep/rcb-driven. And invisible to
  all comparison surfaces: corpus `.ours.json` scores round to **2 decimals**, snapshots
  compare **chord text/identity**, the §3 formula pin is **1e-12**. Primary approach
  shipped; Cowork-approved bit-identical fallback (expose `d` separately) was held in
  reserve. **The 0/353×3 A/B showed zero diffs — fallback not needed.**

### 1.4 Gate R replacement condition (the derivation + the Diminished gap)

Derived the old proxy's exact meaning. Under Gate R's only firing context (`rcb>0` ∧ bass
foreign), `bb=0` (needs `rootPc==bassPc`), so `basisDep_old = nb + cappedInv`; because the
**minimum inversion bonus `sameRoot`=0.40 strictly exceeds the maximum penalty
`kNonBassPenalty`=0.35**, the old gate fires **⟺ `cappedInv == 0`** (no inversion credit).

The ratified literal sounding-third test (`pcWeight[third]≤0.05`) matches this for
Maj/Min/Aug/HalfDim (all in `isInvertedMajMin`, so a sounding third fires `sameRoot`) and
for no-third qualities (**Sus/Power — never inversion-eligible → always gated → matches**),
**but diverges on Diminished**: Dim is excluded from `isInvertedMajMin`; its only credit is
`completeTriadInversionBonus`, which additionally requires a *stepwise-bass edge* — a
temporal condition no vertical pcWeight test can capture. A Dim continuation (foreign bass,
m3 sounding, no stepwise bass) earns no credit → old gate fires, but the literal test would
spare it: a **0.40×cf×af output-visible swing**, not byte-identical. This is the reachable
disagreement the instruction flags as a Cowork design question.

**Resolution (Cowork-ratified, option 1 — reconstructed-credit):** Gate R reads the
pipeline-reconstructed **`fullBasisDep ≤ 0`** (the credit it computes for the score anyway)
via a new 3-arg `gateRZeroesRootContinuity` overload. Byte-identical on **every** quality
(reads the same total credit, no pcWeight approximation), fully **intra-layer** (closes the
cross-layer dependency on the oracle — audit Finding 6), and Diminished-gap-free.

### 1.5 Re-pin inventory — EMPTY (verified)

All Stage-1a/1b/3.1 tests stay green **unchanged**:
- `gater_tests.cpp` F1/F2 — the 2-arg `gateRZeroesRootContinuity(cell, rcb)` overload is
  retained (delegates to the 3-arg on `cell.basisDep`); fixtures set `basisDep` directly,
  values/outcomes identical (Cowork's "F2 green unchanged").
- `functionlayer_tests.cpp` — synthetic cells leave the new flags `false` and
  `previousQuality=Unknown`, so `cappedInv=0` and `resolution=0` in every test ⇒ scores
  unchanged (incl. the §3 formula pin and the 0.02 near-tie canary).
- `diagnose_tests.cpp` Δ=+7b — a **proof obligation**, stays green (reconstructed-credit
  reproduces Gate R firing on G/E: `cappedInv=0` → `fullBasisDep=0` → fires).
- `postscoringgates_tests.cpp` Δ=+7b E2E, catalog `DiagnoseMatchesProductionPipeline` —
  proof obligations, green.

---

## §2 — Implementation map

| File | Change |
|---|---|
| `harmonicfunctionlayer.h` | `HarmonicFunctionContext`: +`bassIsStepwiseFromPrevious`/`ToNext`. `ScoringCell`: +`supportsInversionBonuses`/`qualifiesCompleteTriad`, basisIndep/basisDep docs now vertical. +`resolutionEdgeBonus` / `inversionContextBonus` decls. +3-arg `gateRZeroesRootContinuity`. Header architecture comment: oracle "applies NO progression signal" (now true). |
| `harmonicfunctionlayer.cpp` | +`resolutionEdgeBonus` / `inversionContextBonus` defns (reproduce the oracle helpers exactly). +3-arg Gate R overload (2-arg delegates). **Pass A**: recompose `resolution` + `cappedInv`, fold `fullBasisIndep`/`fullBasisDep` in the historical positions, Gate R on `fullBasisDep`, score rebuilt in the exact arithmetic order. |
| `chordanalyzer.cpp` | Deleted `bassIndependentContextualBonuses` (→ `diatonicRootContribution`, diatonic-only) and `bassDependentContextualBonuses` (inlined `basisDep = nonBassAdjustment + bassBonus`). Snapshot loop publishes the two cell flags (`hasStructuralBass &&` predicate). `fnCtx`: +stepwise edges. `diagnoseChord` COMPETITION layer: recompute `resolution`+`inversionContextBonus`, Gate R via the reconstructed `fullBasisDep`. |
| `chordanalyzer.h` | TODO at the inversion-bonus block updated (debt cleared, Stage 3.3). `maxTotalInversionContextBonus` doc repoints to `fn::inversionContextBonus`. `DiagnosticOracleCell`/`DiagnosticCompetitionCandidate`: docs + 2 new display fields. |
| `tools/batch_analyze.cpp` | `--diagnose-measures` COMPETITION emitter: +`resolution`/`inversion_ctx` fields. |
| `docs/scoring_model.md` | §4 Gate R (reconstructed-credit + derivation incl. Dim gap), §5 (helper removal), §11 (Stage 3.3 migration subsection). |
| `docs/decoder_design.md` | §6 dated amendment (pcWeight mechanism superseded; reconstructed-credit). |

---

## §3 — Verification (the full gate, maximum strictness)

| Gate | Result |
|---|---|
| **Corpus A/B 0/353 × 3** (Baroque/Jazz/Default; regenerate-and-diff vs the byte-identical 3.1b-chain baseline `git_hash 8e4bb4902d`) | **0 differing `.ours.json` on all three** |
| Pipeline snapshots | **11/11, zero diffs, NO golden refresh** |
| composing_tests | **505/505** |
| notation_tests | **57/57** |
| Python (unittest) | **70/70** |
| batch_analyze regression | **passed** |
| BIR identity sets | Baroque **13**, Jazz **7** `{bwv244.15,245.17,245.40,422,432,45.7,74.8}`, Default **14** = Baroque-13 ∪ {bwv187.7@19200} — exact |
| FP canaries / Δ=+7b / bwv320 pins | green (functionlayer near-tie 0.02 canary; diagnose + postscoringgates Δ=+7b E2E) — UNMODIFIED |
| Diagnose dump (new Gate R reasoning) | `diagnose_tests.DeltaPlus7b_DumpShowsGateRWithheldRcbAndWinnerC` green = G/E `rcb_withheld_by_gate_r=true`, winner C/E, via reconstructed `fullBasisDep`. (The CLI `--diagnose-measures` runs null-context, so its rcb/Gate-R columns are 0 by design — pre-existing limitation, unrelated to 3.3.) |
| Perf | P3 path arithmetic moved, not added — same `analyzeSection` cost (snapshots/notation timings within noise) |

---

## §4 — Re-pin ledger

**Empty.** No test was deliberately re-pinned. Every Stage-1a/1b/3.1 pin and every
proof-obligation (Δ=+7b, bwv320, the corpus, the snapshots) stayed green by construction —
the strongest possible outcome for a byte-identity gate. Rationale per test in §1.5.

---

## §5 — Deviations / unknowns

- **Gate R mechanism deviates from the literal ratified design** (pcWeight third test →
  reconstructed `fullBasisDep`), per Cowork's option-1 decision after the Diminished-gap
  derivation. The redesign's *intent* (remove the oracle cross-layer dependency, Finding 6)
  is fully met; the literal text is retained for the record in `decoder_design.md` §6.
- **basisIndep ≤1-ULP reassociation**: shipped the primary (collapsed `V+d`) approach; the
  A/B proved zero diffs, so the bit-identical fallback was not exercised. The reassociation
  is real but provably below every comparison surface's resolution.
- **No metric change** — 3.3 is byte-identical by design; wins remain Stage 3.2 (wider beam).
