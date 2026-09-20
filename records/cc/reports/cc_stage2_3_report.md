# Stage 2.3 — diagnoseChord becomes a true production view (CC report)

Base: `0520a2dda2`. Scope: `src/composing/**` (pre-authorized) + riders to
`tools/analyze_inversion_errors.py`, `build_and_test.md`, `docs/score_inventory.md`,
`tools/batch_analyze.cpp`, `docs/scoring_model.md`. Tags: [code] = read from source,
[probe] = observed from a run.

---

## §1 Survey (consumers + dump usage)

### 1. All `diagnoseChord` consumers [code]

- **`tools/batch_analyze.cpp`** (`--diagnose-measures N[,N...]`) — the SOLE consumer.
  `writeDiagnosticJson()` (≈L942) calls `diagAnalyzer.diagnoseChord(region->tones,
  fifths, mode)` for the first region of each requested measure and serialises the
  result to JSON. This is where the C3/C4 investigation dumps came from.
- **No test** calls `diagnoseChord` (grep `diagnoseChord` over `src/**` → only the
  decl/def + batch_analyze). Stage 1 never pinned it.
- **No Python** parses the dump (grep `diagnose_measures|top_candidates|diagnoseChord`
  over `**/*.py` → none). So there is **no external-format consumer that can't be
  updated in scope** — the stop-condition does not trigger.

Fields the consumer actually used (old `ChordAnalysisDiagnosticResult`):
`bassPc`, `pcWeights`, `distinctPcs`, and `candidates[]` with the per-component fields
(`totalScore`, `templateTonesScore`, `extraNotesScore`, `dim7Bonus`, `nonBassAdjust`,
`structuralPenalty`, `tpcBonus`, `bassBonus`, `diatonicBonus`, `contextBonus`). It also
read `region->chord` extensions directly (not from diag).

**Latent bug found in the consumer [code]:** `diagTemplateName`'s `NAMES[16]` array was
missing the aug7 template (`{0,4,8,10}`, index 10), so every `template_idx ≥ 10` printed
the wrong name and 16 returned "Unknown". Fixed to the full 17-entry ordering with a
`static_assert` against `kTemplateCount`.

### 2. The old dump's content vs production [code]

The legacy `diagnoseChord` was a **second scorer**: it rebuilt the pcWeight histogram,
picked the legacy single (lowest) bass, scored a private `kDiagTemplates` array with the
oracle term helpers, and added context via the diagnose-only `contextualBonuses()` helper
(which folds rcb inline). What it **omitted** vs production: the multi-bass joint snapshot,
`applyHarmonicFunction` (rcb-with-Gate-R, w_seq, w_dim, step bonuses, threshold, result
cap, cross-bass winner), and the post-scoring tail (Iter 86/91/pedal, gates A–L). Its
"winner" was the top of a 12×17 grid by a different formula — which is exactly why it
mis-led the bwv320 slash-synthesis retraction and the bwv14.5 mischaracterisation.

### 3. Feasibility of the preferred design [code]

`analyzeChord` already builds a `fn::ScoringSnapshot` internally (≈L2895) and hands it by
const-ref to `applyHarmonicFunction`, which does not mutate it. Adding
`fn::ScoringSnapshot* snapshotOut = nullptr` and `if (snapshotOut) *snapshotOut =
std::move(snapshot);` right before `return results;` is therefore **zero behavior change
when null** (one branch) and a single move when set — exactly the `gateCtxOut` pattern.
`ScoringSnapshot` is already forward-declared in `chordanalyzer.h` (no include cycle); a
pointer param needs only the forward declaration. No lifetime concern: the snapshot is a
local consumed before the copy-out. Only one `IChordAnalyzer` implementor exists
(`RuleBasedChordAnalyzer`) and there are no mocks, so the virtual-signature change is safe.

---

## §2 Design as built (+ deviations)

1. **`analyzeChord` out-param.** `fn::ScoringSnapshot* snapshotOut = nullptr` added to the
   `IChordAnalyzer` interface and the `RuleBasedChordAnalyzer` override. Copied out via
   `std::move` after `applyHarmonicFunction` ran. Byte-identical when null.

2. **`diagnoseChord` rewritten to replay production.** It now runs the exact production
   sequence — `analyzeChord(... &gateCtx, &snapshot)` → (if non-empty) `applyIter8691Pedal`
   → `applyPostScoringGates` → `results.front()` — identical to `test_helpers.h
   analyzeWithGates()` and every `regionanalyzer.cpp` commit site. It then decorates:
   - **ORACLE** — every snapshot cell as `DiagnosticOracleCell` (basisIndep, basisDep, cf,
     af, wComplete, appliedBassBonus + the pre-competition `verticalScore`), score-sorted.
   - **COMPETITION** — the winning bass group, one `DiagnosticCompetitionCandidate` per
     `gateCtx.rawCandidates` entry. **Scores are authoritative** (from the pipeline). The
     signal components are recomputed from the matching snapshot cell + ctx via the SAME
     public `fn::` functions the pipeline calls: `rootContinuityBonus` + `gateRZeroesRootContinuity`
     (rcb incl. Gate R outcome, gated on `ScoringPhase::Final`), `wSeqBonus`, the exact
     `wDimDelta` the pipeline stored, and `wStepIn/OutBonus`.
   - **POST-GATES** — winner identity/score captured after the competition, after
     `applyIter8691Pedal`, and after `applyPostScoringGates`, yielding `iter8691ChangedWinner`
     / `gatesChangedWinner` flags.
   - **finalWinner** — `results.front()` = the production winner BY CONSTRUCTION.

   **Deviation (stated):** the per-cell breakdown granularity necessarily changes. The
   snapshot stores the production decomposition (`basisIndep`/`basisDep`/`cf`/`af`/
   `wComplete`/`appliedBassBonus`), not the legacy fine-grained sub-terms
   (`templateTonesScore`, `extraNotesScore`, …). Those sub-terms are folded into
   `basisIndep` inside the oracle and are not retained in the snapshot; keeping them would
   require re-scoring (the very thing 2.3 removes). The ORACLE layer is therefore the real
   production decomposition, which is strictly more faithful.

3. **Dead duplicates removed.** `kDiagTemplates` (the byte-identical template mirror) and
   `contextualBonuses()` (the diagnose-only rcb-folding helper, audit Finding 2b) are now
   unreferenced and deleted. `scoring_model.md` §2/§3/§8/§9/§11 + §4 updated (the
   atomic-update site list drops 4 → 3 scoring sites; `diagTemplateName` noted as a
   display-only site). Stale comments at the `analyzeChord` templates array and the split-
   helper block updated.

4. **Consumer updated.** `batch_analyze.cpp writeDiagnosticJson` emits the new layered
   format (`final_winner`, `oracle_top`, `competition`, `post_gates`) and now threads the
   active preset `chordPrefs` into the diagnose call so the dump reflects the preset the
   batch run used. (Temporal context is left null — the diagnostic shows the region's own
   vertical/competition evidence in isolation; reconstructing the exact inter-region
   context the batch run threaded is out of scope and would risk fabricating signals.)

---

## §3 What became dead and was removed

| Removed | Was | Why dead now |
|---|---|---|
| `kDiagTemplates` (`std::array<TemplateDef,17>`) | byte-identical mirror of the `analyzeChord` template array, a 4th atomic-update site | diagnose replays production → uses the real `templates` array |
| `contextualBonuses()` | diagnose-only contextual scorer folding rcb inline (audit Finding 2b) | diagnose no longer re-scores |
| `ChordCandidateDiagnostic` struct | per-cell legacy breakdown | replaced by `DiagnosticOracleCell` / `DiagnosticCompetitionCandidate` |

**Atomic-update site list, before → after (scoring_model.md §3/§9):**

- before (4): `templates` array · **`kDiagTemplates`** · three score matrices · `kMasks`
- after (3): `templates` array · three score matrices · `kMasks`
  (+ `diagTemplateName` in batch_analyze as a display-only, `static_assert`-guarded site)

---

## §4 The agreement invariant + Δ=+7b dump excerpt

**Agreement invariant** — `chordanalyzer_musicxml_tests.cpp::DiagnoseMatchesProductionPipeline`:
iterates the Jazz + Standard catalogs (≈300+ fixtures) with temporal context threaded
exactly as production, asserting `diagnoseChord().finalWinner == analyzeWithGates().front()`
for rootPc, bassPc, quality, extensions AND `EXPECT_DOUBLE_EQ` on score — plus the
empty-result agreement (no winner ⇒ `!hasWinner`). True by construction; this is the pin
that diagnose can never drift from production again.

**Δ=+7b acceptance** — `diagnose_tests.cpp::DeltaPlus7b_DumpShowsGateRWithheldRcbAndWinnerC`,
the bwv320 mapping (`{E,G,C}` over bass E, predecessor root G). The dump's COMPETITION layer
shows, for the continued-root candidate **G/E** (root 7, bass 4 — bass a M6 above root,
interval 9, in no template):

```
rcb_withheld_by_gate_r = true     (gateRZeroesRootContinuity: basisDep ≤ 0 ∧ bass foreign)
rcb                    = 0.0      (in effect — withheld)
rcb_raw                = 0.40     (the +0.40 the candidate earned before Gate R)
```

…while the winning **C/E** candidate is not gated, and `finalWinner = C (root 0) / E (bass 4)`
— matching `analyzeWithGates().front()` (cross-checked in the test). This is precisely the
rcb/Gate-R information whose absence caused the historical mis-diagnoses.

---

## §5 Verification table

| Gate | Expected | Result |
|---|---|---|
| Build | clean | ✅ composing/notation/snapshot/batch_analyze linked, no errors |
| composing_tests | 498 + new | ✅ **501/501** (498 + 3: agreement invariant + 2 diagnose_tests) |
| notation_tests | 52 | ✅ **52/52** |
| pipeline_snapshot_tests | 11/11 zero diffs | ✅ **11/11** (1 expected skip), **zero golden diffs** |
| Python unittest | 68/68 | ✅ **68/68** |
| batch_analyze regression | pass | ✅ `batch_analyze regressions passed` |
| BIR Baroque (characterise) | 13 | ✅ **13** (353/353, manifest-validated) |
| analyze_inversion Baroque (NEW no-arg default → Rider 1) | 24/13 | ✅ `Corpus OK: preset=Baroque 353/353` → **24/13** |
| BIR Jazz (characterise) | 7 + identity set | ✅ **7** = `{bwv244.15, bwv245.17, bwv245.40, bwv422, bwv432, bwv45.7, bwv74.8}` (exact) |
| analyze_inversion Jazz | 35/7 | ✅ **35/7** |
| Production byte-identity | snapshots 0 diffs + BIR unchanged | ✅ both hold; the only output change is `diagnoseChord`'s own format |
| Diagnose dump smoke | valid layered JSON | ✅ `final_winner`/`oracle_top`/`competition`/`post_gates` populate on bwv001 m1–2 |

Bonus corroboration: the Jazz `analyze_inversion` run prints "Processed 353 chorales
(**326 with WiR three-way coverage**)" — independently confirming the Rider 2 WiR-coverage
fact (326/353) written into `score_inventory.md`.

---

## §6 Unknowns / notes

- The COMPETITION layer covers the **winning bass group only** (`gateCtx.rawCandidates`),
  matching what the pipeline actually committed; non-winning bass groups appear in the
  ORACLE layer (all cells) but without progression-signal annotation. This mirrors what
  the pipeline computes (it only finalises the winning bass group). [code]
- step_in/step_out in COMPETITION are the **potential** wStep values from the public
  helpers; the surgical first-inversion-m7 guard may have suppressed them in the actual
  score. The authoritative effect is always in `competitionScore`. Documented in the
  struct. [code]
- batch_analyze diagnose passes no temporal context (see §2.4) — a deliberate scoping
  choice, not a faithfulness gap in `diagnoseChord` itself.
