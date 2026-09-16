# CC Instruction — LAYER AUDIT #4 (primary): keymodeanalyzer.cpp (the key-mode scorer) — READ-ONLY

> Fourth per-layer audit (`docs/layer_audit_plan.md`) — closes the KEY AXIS. **CC = primary auditor**
> (empirical measurement); Cowork's note `cowork_audit_keymodeanalyzer.md` + the map's K2 reconcile.
> **READ-ONLY — findings only, NO code/behavior/inference change.** **North star: best = CORRECT inference vs
> the DCML oracle, not a proxy gate.** **Your fresh measurement is authoritative on the NUMBERS.** ⚠ Cowork
> already CORRECTED one mechanism claim at source this session — see #2.

## §1 — Scope
`src/composing/analysis/key/keymodeanalyzer.cpp` (the residual scorer: `analyzeKeyMode` + the score* terms +
`applyPairwiseDisambiguation`). Read-only; you MAY run `batch_analyze --dump-key-candidates` / the key
measure on the corpus + a read-only probe (reuse `compare_rn`/`dcml_parser`). No production edit.

## §2 — The audit (per plan §3) + reconciliation targets (MEASURE vs DCML)
1. **Responsibility:** per-region key-mode scoring — 252 candidates (12×21), `scaleScore + triadScore +
   keySignatureScore + characteristicPitch + trueLeadingTone + modePrior` + the −1.0 declared hint, pairwise
   disambiguation on the top-2 same-signature modes, rank + confidence.
2. **Correctness vs DCML — the RELATIVE-PAIR (K2), measured:**
   - **The relative-major/minor error rate** — how often the scorer (note-only) picks the wrong relative vs
     DCML. Cowork `[prov ≈ 1383 floor regions flip without the declared crutch]` (4b-i) — re-measure the real
     relative-pair error rate + the recovery the disambiguation/declared-hint provides.
   - **★ The disambiguation scope (Cowork CORRECTED at source `keymodeanalyzer.cpp:455-487`):**
     `applyPairwiseDisambiguation` is NOT inert on tonic-present-both wholesale — clauses 3/4 resolve the
     one-incomplete-triad sub-case (the Em/G opening). It is inert specifically on **both-tonic-present AND
     both-complete-triad**. **Measure:** what fraction of the relative-pair floor is the both-complete-triad
     (truly unresolved) case vs the one-incomplete (disambiguation handles) case? This sizes how much of K2 is
     genuinely structural-floor vs already-handled.
   - **21-mode mis-win:** how often a tonal (major/minor) piece is won by a church/exotic mode vs DCML.
   - **`scoreKeySignatureProximity` partial-sig mis-anchor** (the Dorian wall).
3. **Completeness:** relative-pair (the floor, needs external evidence — confirm it can't be reweighted);
   window-coupling of the lookahead.
4. **Gaps → obligations**, tagged. Confirm K2 = the note-evidence floor the joint's SOFT integration (K3,
   measured the lever) must overcome — NOT reweightable.

## §3 — Deliver
`cc_audit_keymodeanalyzer_report.md`: responsibility, the MEASURED relative-pair error + the
both-complete-triad-floor size + 21-mode mis-win, completeness, tagged obligations, empirical method. State
which `[prov]`/corrected claims you confirm vs further correct. Read-only; Cowork verifies methodology +
reconciles; user ratifies.

## §4 — Stop conditions
- Any production/inference/behavior change → STOP. A probe that moves production output → STOP.
- Cross-layer issue → phase-2 note. Uncertain → check vs oracle; bucket convention-boundary + surface; never
  guess.
