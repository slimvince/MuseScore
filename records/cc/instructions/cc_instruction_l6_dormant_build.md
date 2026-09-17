# CC instruction — the L6 GROUPING layer: dormant build + oracle validation

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only), `C:\s\MS\BUILD_AND_TEST.md`.
> Mandatory: **`cowork_layer6_grouping_design.md` (SIGNED 2026-07-02) in FULL** — §5.1–§5.5 are the build; §3 the
> I/O contract; §10 the validation; the §5.1 edge-provenance/extension-cue amendment and the §5.2 confidence-contract
> compliance note are part of the signed spec. Also: `cc_tsv_oracle_report.md` (the oracle baselines + exemplars).
>
> **Dispatch state: ACTIVE (2026-07-02, on the ratified TSV-oracle report — the L6 gate is passed).** Dormant build:
> no production consumer, byte-identical by construction. Commits one change-class each, local, unpushed, fork-only.
> No θ, no tuning (the firewall: alignment window / codetta margin / key-area combiner = declared default constants).
> Bash rules; cite by anchor.

## Task 1 — the module (commit 1)

`src/composing/analysis/grouping/` (naming yours, declare): ONE dormant module implementing exactly §5.1–§5.5 over
the §3 inputs (the L5 `FunctionLayerOutput`, the L1.5 boundary ticks + strengths + provenance, the L3/L5 local-key
track) — producer-agnostic POD views, hand-injectable (the established L5-unit pattern):
- **§5.1** punctuation-span partition (total, flat; `}{` interlock; §5.1-a codetta refinement behind its declared
  constants) + the **edge amendment**: `clipped-by-selection-edge` provenance on edge groups + the `extension-cue`
  tag (surfaced, never acted on).
- **§5.2** key-area grouping (maximal constant-local-key runs; confidence = declared monotone combiner over the
  units' DECLARED boundary key confidences, published [0,1] Class-M per the confidence contract).
- **§5.3** cadence-to-span alignment (closing cadence within the declared window; spans without cadence valid;
  off-boundary cadence = `internal` tag, never snapped/discarded).
- **§5.4** residual carry (open marks surfaced on containing groups, never resolved).
- **§5.5** schema-span hosting (empty absent the consumer — assert it).
**Reuse-vs-new + what-retires** per the unification rule (the scattered live `detectCadences`/`detectPivotChords`/
`KeyArea` paths retire only at engage — R2/R3; name them, touch nothing live).

## Task 2 — tests (same or second commit; oracle-asserted)

Per rule: partition totality/flatness; interlock; codetta (strong-then-weak peaks); edge provenance + extension-cue
(must-fire at a clipped selection edge, must-not at a score boundary... per the bounded-context design's
distinction); key-area boundary at each local-key change incl. mid-punctuation-span (D5 independence); combiner
monotone + [0,1]; alignment window in/out; internal-cadence tag; residual pass-through; empty-schema case.
Dormancy grep-proof; suites green, NO golden refresh; gate 53/24/53 exact once at the end.

## Task 3 — the §10 step-1 validation (read-only; report)

A default-OFF `batch_analyze --dump-l6` (additive, the established pattern) emitting the grouped structure over the
full spine dump; extend `compare_l6_oracle.py` minimally (same shared matcher) to grade: **punctuation-span
boundaries** vs the `phraseend` GT (expect ≈ the L1.5 baseline — L6 adds no detection; assert it stays within noise
of the 34.8/22.4 baseline: a MATERIAL deviation means L6 leaked detection = STOP); **key-area boundary ticks** vs GT
local-key change ticks + per-area tonic/mode match; **cadence-to-span alignment** counts (closing / no-cadence /
internal) vs the GT cadence-at-phrase-end rate. Dev beds only. Report per corpus + exemplars.

## Deliverable

`cc_l6_build_report.md` (HELD, line count at end): §1 module (reuse-vs-new/retires), §2 tests, §3 validation tables
+ the assert-no-added-detection check, §4 Unknowns. **On your report: Cowork verifies at objects before ratifying;
the L6 spec then flips to AS-BUILT (Cowork's doc half).**

## Stop conditions

Any detection logic creeping in (a threshold/merge/re-decision not in §5.1–§5.5) → STOP (the §6 proportionality
bound is a build rule, not prose). Any production reach → STOP. Boundary-metric material deviation from the L1.5
baseline (Task 3) → STOP. No θ.
