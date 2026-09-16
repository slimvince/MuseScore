# CC Instruction — LAYER AUDIT #5 (primary): chordanalyzer.cpp (the vertical oracle) — READ-ONLY

> Fifth per-layer audit (`docs/layer_audit_plan.md`) — opens the CHORD AXIS. **CC = primary auditor**
> (empirical measurement); Cowork's note `cowork_audit_chordanalyzer_oracle.md` + the map's C1/C3/C4
> reconcile. **READ-ONLY — findings only, NO code/behavior/inference change.** **North star: best = CORRECT
> inference vs the DCML/music21 oracle, not a proxy gate.** **★ This audit's #1 job: re-measure the
> functional-residual ~95% — the entire "chord axis is healthy" verdict rests on it (Cowork `[prov]`).**

## §1 — Scope
`src/composing/analysis/chord/chordanalyzer.cpp` residual (the oracle: 17 templates + scoring helpers +
`buildChordResult` + `analyzeChord` → `ScoringSnapshot`). Read-only; you MAY run the corpus + a read-only
probe (reuse `compare_rn`/`dcml_parser`/`music21` as the functional-residual investigation did). No
production edit.

## §2 — The audit (per plan §3) + reconciliation targets (MEASURE vs the oracle)
1. **Responsibility:** vertical chord identification — score pitch content against the 17-template vocabulary,
   hand a `ScoringSnapshot` to the competition/function layer.
2. **Correctness — the VERDICT-CRITICAL measurement:**
   - **★ The functional/vertical split.** Cowork `[prov ≈ 95.2% of root errors functional / 4.8% vertical]`
     (and music21's vertical RN fails the same functional roots → a function-layer problem, not a vertical
     ceiling). **RE-MEASURE this at HEAD** — of the oracle's root errors vs DCML, what fraction is genuinely
     VERTICAL (oracle picked the wrong chord from the pitch content) vs FUNCTIONAL (the vertical chord is
     right; the winner-selection/function downstream is wrong)? **This number decides whether the
     chord-axis-healthy verdict + the two-track split hold.** Report it precisely.
   - **The symmetric floor (C3).** `[prov ≈ 53% Baroque carries a symmetric dim7]`; root pc-undefined by
     construction (also augmented). Re-measure the symmetric-chord share + confirm it's the inherent
     vertical floor (the reserved learned slice).
   - **The diatonic-root KEY coupling (X2).** `diatonicRootContribution` reads the key for ambiguous roots —
     confirm the oracle is "mostly vertical" but leaks a key dependency on ambiguous sonorities.
3. **Completeness (C4):** vocabulary = 17 tertian/sus/power; **measure the jazz-vocabulary gap** (how often
   extended/altered chords on the Jazz corpus are mis-identified as the nearest 7th + extras). Confirm
   whether fully-dim7 {0,3,6,9} is an explicit template or derived via the dim triad + `dim7Characteristic
   Bonus`.
4. **Gaps → obligations**, tagged. If the ~95% holds → the chord-axis-healthy verdict stands, obligations are
   downstream (the competition, audited next). If it does NOT hold → flag it (the two-track verdict shifts).

## §3 — Deliver
`cc_audit_chordanalyzer_oracle_report.md`: responsibility, the MEASURED functional/vertical split (the
headline) + symmetric-floor share + jazz-vocab gap, completeness, tagged obligations, empirical method. State
which `[prov]` numbers you confirm vs correct. Read-only; Cowork verifies methodology + reconciles; user
ratifies.

## §4 — Stop conditions
- Any production/inference/behavior change → STOP. A probe that moves production output → STOP.
- Cross-layer issue → phase-2 note. Uncertain → check vs the oracle; bucket convention-boundary + surface;
  never guess.
