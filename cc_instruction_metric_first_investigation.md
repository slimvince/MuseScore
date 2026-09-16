# CC Instruction — METRIC-FIRST, ROUND 3: FINE-GRAINED (per-beat) oracle-root metric — READ-ONLY

> **Rounds 1–2 delivered** (`cc_metric_first_dossier.md`, `cc_metric_round2_report.md`, Cowork-reconciled). Round
> 2 hit a real STOP: at **batch-region** granularity, regions that straddle two chords (e.g. bwv102.7 spanning
> `vi`→`IVmaj7`) make the oracle-root verdict depend on an arbitrary onset-vs-max-overlap alignment choice, and
> policy A floors them as "disputed." **User directive (2026-06-20): score AS FINE-GRAINED AS NEEDED.** That
> resolves it — score **per-beat at the oracle's native granularity**, and the straddle becomes a visible,
> chargeable per-beat error instead of an alignment artifact. This round designs + measures that fine-grained
> gate **READ-ONLY** (no build, no committed tool, no production/gate/scoring/threshold change) before the
> standing `--oracle-root` tool is built. Ratified design parameters carried in: **policy A** (DCML ∧ music21
> concur), **bass-decoupled**, **baseline-B family** (operational "drop line 162", not the unstable pure-A).

## §1 — The fine-grained metric (the design to confirm)
- **Granularity = the oracle's native event grid** (per-beat for WiR `.rntxt`; per-`quarterbeats`/`abs_tick`
  for DCML TSV) — i.e. wherever the oracle asserts a root, that is a scored event. Do **not** score at
  batch-region granularity. (This is `score_inventory.md` roadmap 5.2 / the CLAUDE.md per-beat view, ~7× the
  batch rate — expected.)
- **Expand our per-region roots onto that grid:** each oracle event inherits our region's `rootPitchClass` for
  the region covering that tick (reuse `batch_analyze --section-level` semantics / the existing per-beat
  expansion if one exists — find it before writing new). No alignment *choice* remains: every oracle event is
  compared against our root at that tick.
- **Predicate (unchanged, per event):** `three_way_classify(our_root_pc, music21_root_pc, dcml_root_pc) ==
  music21_dcml_agree` → a charged oracle-root error at that event. Bass-decoupled, pc-typed (normalizer-immune).
- **The floor is now ONLY genuine same-event oracle disagreement** (DCML ≠ music21 at the *same* beat — the true
  convention-boundary / symmetric-dim7 floor). The segmentation-straddle cases are **no longer floored** — they
  surface as per-beat errors on the beats the region wrongly covers. Confirm this separation explicitly.
- **Aggregate** as a per-event case-identity set (stem@tick, per preset) — same anti-contamination
  `validate_corpus_dir` guard.

## §2 — Read-only confirmation (compute from disk; commit nothing)
1. **Re-score the 4 straddle cases per-beat** (bwv102.7, bwv227.7, bwv358, bwv432) on HEAD (`baroque_kma_abs`)
   and ANCHOR (`baroque`). Show that fine-grained scoring **dissolves the dispute**: each beat scores against its
   own oracle root, the region's over-coverage is charged on the mismatched beats, and the onset-vs-overlap
   verdict flip is gone. Report the per-beat ledger for at least bwv102.7 (the inspected case).
2. **Per-beat baseline, per preset** (Baroque HEAD = `baroque_kma_abs`, Jazz, Default): the fine-grained
   oracle-root error event-set + the genuine same-beat-disagreement floor reported separately. Expect numbers
   well above the batch 106/104/110 (per-beat is finer) — report both the **charged-error** count and the
   **floor** count so they are never conflated.
3. **Acceptance, restated for fine granularity:** the 2 robust fixes (bwv14.5, bwv416) must remain fixes; the
   straddle cases must now be **scored per-beat** (not floored); the genuine same-beat-disagreement set (symmetric
   dim7 etc.) must be the *only* floor. If the per-beat run cannot cleanly separate "segmentation straddle
   (charged)" from "same-beat oracle dispute (floor)", STOP and report — that separation is the whole point.
4. **Sanity vs the ~7× caveat:** confirm the per-beat Baroque charged-error rate is in the order CLAUDE.md's
   granularity note predicts (~7× batch), or explain the divergence.

## §3 — Genre-balanced (carry forward, unchanged from round 2 §B)
Fine granularity does not change the round-2 §B finding: policy A is chorale-only today (no off-chorale music21
sidecars); the DCML GT for all 11 corpora + the WiR anthology parses cleanly. Keep **option (a) two-tier macro**
(policy-A chorales + DCML-only per-beat macro elsewhere, after a build) as the near-term genre-balanced view;
music21-sidecar generation (option b) stays Stage-5. Note any per-beat-specific wrinkle (rntxt has no absolute
tick column → measure-anchor reconstruction needs our region anchors).

## §4 — Deliver
`cc_metric_round3_report.md`: the per-beat metric definition, the bwv102.7 per-beat ledger + the 4-straddle
dissolution, the per-preset fine-grained baseline (charged-error + floor, separately), the restated acceptance
result, the ~7× sanity check, and the genre-balanced carry-forward. **READ-ONLY — HEAD `dd418ecfed`; no build,
no committed tool, no production/gate/scoring/threshold change.** Cowork reconciles; user ratifies the
fine-grained baseline before the standing `--oracle-root` tool (and the off-chorale builds) are scoped.

## §5 — Stop conditions
- The per-beat run cannot separate segmentation-straddle (charge) from same-beat oracle dispute (floor) → STOP
  + report (the design fails its purpose).
- Any per-beat expansion would require a production/analyzer change to obtain (not just a read of existing
  `.ours.json` regions) → STOP, describe the minimal build needed, do not build it.
- Any temptation to commit the gate tool / change a threshold / touch scoring → STOP (post-ratify build step).
- A straddle case does NOT dissolve under per-beat scoring (still alignment-ambiguous) → STOP + report; the
  granularity assumption needs re-examination.
