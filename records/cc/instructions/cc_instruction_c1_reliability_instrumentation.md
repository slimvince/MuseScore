# CC INSTRUCTION — C1 reliability instrumentation: curves per (layer × decision) on the ratified unit (2026-07-03)

**Status: ACTIVE DISPATCH (the only open instruction). Measurement instrumentation ONLY — reliability CURVES,
explicitly NOT fitted calibration maps (map fitting is the Stage-5 fitter's, a later ratified step). No inference
behavior change anywhere. Stage-5 runway step 2 (after the ratified A-8 dual-track).**

## Mandatory reads BEFORE any work

1. `CLAUDE.md` (bash rules; both suites after any code change; gate discipline) + `STATUS.md` header +
   `BUILD_AND_TEST.md`.
2. `cowork_confidence_contract.md` — §2 (classes), §3 (the per-layer inventory this dispatch instruments), §4
   (frames F-A/F-B), §6 **C1** (the obligation this executes), §7 (D-FS ranges banked; D-L3a open).
3. `docs/implementation_roadmap.md` — the A-8 block's **ratified dual-track** (the unit/variant/respect this
   measures on) + the two queued doc riders (carried by this dispatch's docs commit, Task 5).
4. `cc_a8_rebaseline_measure_report.md` + `tools/a8_rebaseline_measure.py` — the ratified unit's pinned
   implementation (REUSE its cell machinery; do not re-derive).
5. `cc_instruction_e0_fullspine_measure.md` + `cc_e0doubleprime_report.md` — the `--dump-fullspine` chaining
   harness (the dormant-chain output source) and what confidence fields it already carries.

## What this is

Contract §6 C1: measure **reliability** — empirical correctness as a function of **published confidence** — per
(layer × decision type), against human GT, on the **ratified A-8 unit** (union-of-boundaries, duration-weighted,
variant (b) DCML-only). Deliverable: **reliability curves + calibration diagnostics**. NOT delivered here: fitted
Class-P maps, any θ change, any behavior change (C2/Stage 5).

## Task 0 — inventory what the dumps already export

For each §3 inventory row, verify at source what confidence the existing dumps (`--dump-fullspine`, the L3/L5
outputs, the L1.5 profile) actually emit. Where a published confidence exists in the data structures but is NOT
exported by any dump, you may add an **additive, default-off dump field** (diagnostic-only; the default output
byte-identical — prove via the suites + snapshot no-refresh + the gate sandwich). If a confidence does not exist
at the boundary at all, that row is REPORTED as unmeasurable-as-built (name the §3/§7 delta), never improvised.

## Task 1 — the harness (`tools/c1_reliability.py`, new)

For each measurable (layer × decision), on each preset {Baroque, Jazz, Default}:

- **Join** each decision's published confidence to its per-cell correctness verdict on the ratified unit —
  REUSING the A-8 driver's cell loop + `classify_pair`/key parsers verbatim (orchestration only; a primitive
  change is a STOP).
- **Bin** by confidence: 10 equal-width bins on [0,1], per bin reporting decision count, scored duration,
  duration-weighted empirical correctness, and the bin's mean confidence. Declared, fixed binning — no fitting.
- **Diagnostics per curve:** monotonicity violations (bins where correctness falls as confidence rises), the
  duration-weighted calibration gap per bin (|empirical − mean confidence|) and its weighted mean (an ECE-style
  summary — report it as a descriptive statistic, not an objective), and the confidence-mass distribution.

**The rows to measure (from contract §3, with their GT and substrate):**

| layer × decision | confidence | correctness verdict | substrate |
|---|---|---|---|
| L3 key-of-slice | the sequence margin (squashed) AND the C1-emission sigmoid — BOTH, separately | the A-8 key respect (tonic+mode identity per cell) | frozen gate corpus, 326 WiR-covered |
| L4 chord-of-slice (dormant chain) | the composite (margin ⊕ sufficiency ⊕ membership), squashed boundary form | A-8 root respect (and RN respect, reported beside) | gate corpus via `--dump-fullspine` |
| L5 RN/function-of-unit (dormant chain) | `combinedBoundary` (the D-L5a squashed form) | A-8 RN respect | gate corpus via `--dump-fullspine` |
| L5 cadence detection | vote weight (evidence scale, F-A) | DCML `cadence` labels (±480t match, the `compare_l6_oracle` convention) | the 16 dev beds (21k TSV-oracle machinery) |
| L1.5 boundary-at-tick | graded profile strength (per-profile max-normalized) | DCML `phraseend` markers (±480t) | the 16 dev beds |

(Leave the legacy path out — documented unreliable, retires at engage. HELD-OUT beds untouched.)

**D-L3a evidence rider:** the L3 row measures BOTH boundary numbers so their curves decide the close-out (which
is better calibrated) — report the comparison; the close-out itself is a separate increment.

**D-FS/D-INV rider:** re-confirm at source the F-A/F-B contradiction-quantity observed ranges (the E0′ #9
readout) on this run and report them beside the curves — the declaration material for C2.

## Task 2 — run + outputs

Full run on the substrates above; per-curve tables to scratch files (bash rules — no large stdout), aggregates in
the report. The no-contamination sandwich: batch gate 53/24/53 set-diff empty before AND after; snapshots
11/11 no refresh; both suites green if anything under `src/` was touched (dump fields only), else state no build.

## Task 3 — report (`cc_c1_reliability_report.md`, force-added)

Per (layer × decision × preset): the curve table + diagnostics; a plain-language reliability reading per row
(monotone? over/under-confident where?); the unmeasurable-as-built rows if any; the D-L3a comparison; the D-FS
range re-confirmation; reuse-vs-new + retires (expected: reuses the A-8 cell machinery, the E0 harness, the 21k
oracle tooling verbatim; new = the harness + any additive dump fields; retires nothing); commit SHAs.

## Task 4 — what this dispatch must NOT do

No fitted maps, no squash-map constant changes, no θ changes, no gate change (the dual-track stands as ratified),
no inference problem-fixing regardless of what the curves show — findings are RECORDED for the Stage-5 fitter.

## Task 5 — the queued doc riders (same docs commit as the report)

1. **CLAUDE.md:** add the ratified A-8 dual-track note to the gate-policy section (primary reported metric +
   fitting-objective basis = robust unit, variant (b), root governs with RN+key tracked, baselines
   63.32/62.37/63.22 % root-agree at 326/352; semantics-when-governing = class-(b) root-disagree duration
   non-increase + explained per-run diff; the batch 53/24/53 case-identity gate REMAINS the hard stop until the
   Stage-5 fitter — R10). Wording tight, placed with the existing two-tier block.
2. **CLAUDE.md:** fix the stale "353/353" corpus-completeness figure → 352 (the frozen corpus at current HEAD;
   E0″/Wave-2 records corroborate), adjusting the `run_bach_preset.py` completeness sentence accordingly — if the
   SCRIPT itself hard-codes 353, STOP and report (that would be a code change needing its own ruling).

## STOP conditions

A pinned primitive would need modification; a confidence value would need computing (not just exporting) at the
boundary; the gate sandwich or snapshots fail; `run_bach_preset.py` hard-codes 353 (Task 5.2); any finding
tempts a behavior change (record, never fix).
