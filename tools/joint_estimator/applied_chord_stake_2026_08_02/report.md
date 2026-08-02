# OI-267 measured stake — Roman-numeral disagreement attributable to applied-chord ground-truth labels

**Status: READ-ONLY measurement, complete. Nothing under the repository was written.**
Corpus: the committed `tools/corpus/baroque` `.ours.json` analyses (326 WiR-covered stems of 352;
inference is preset-independent per CLAUDE.md gate block (A), so one preset carries the result).
Ground truth: When-in-Rome rntxt via `dcml_parser.load_wir_regions` (OI-142 transposition offsets applied).
Unit: the robust unit's union-of-boundaries cells, duration-weighted in ticks (480/quarter), variant (b).

## 0. Establishment of the measurement run

The cell loop is `a8_rebaseline_measure.build_piece_grid`, imported verbatim; it self-validates its
variant-(b) bucket decomposition byte-identical to the pinned `compare_rn.grid_score_regions` on every
piece (an AssertionError otherwise — none fired). The run reproduces the ratified baselines to the digit:
root-agree **77.03 %**, RN-agree **64.12 %** (gate block (A) values), scored duration 8,300,640 ticks.
No reimplementation of any metric primitive; the applied-label test is the ground-truth parser's own
`dcml_parser._split_rntxt_applied`.

## 1. What counts as an applied ground-truth label (the parser's normalization, stated first)

Per `dcml_parser._split_rntxt_applied` (tools/dcml_parser.py:483-499): a trailing '/'-segment of the raw
rntxt numeral is an applied/tonicization target ONLY when it is a bare Roman-numeral degree token
(`V/vi`, `viio7/V`, `V6/5/IV`). A slash inside figured bass (`V6/5` → not applied) or the half-diminished
sigil (`vii/o7` → not applied) is NOT an applied label; `vii/o7/V` IS (target `V`). Multi-level
tonicization (`V/V/V`) resolves one level and counts as applied. The GT `root_pc` of an applied chord is
rooted in the tonicized key (parse_rntxt_file:570-588) — `V/V` in C roots at D, the sounding root — so a
correct-root reading of an applied chord is root-AGREE regardless of its label.

## 2. Predictions (registered before measurement — predictions.json, timestamped)

| # | Quantity | Predicted band | Measured | Verdict |
|---|----------|----------------|----------|---------|
| 1 | Applied share of scored duration | 5–12 % | **4.11 %** | below band |
| 2 | Applied share of root-disagreement duration | 15–35 % | **5.42 %** | well below band |
| 3 | Applied share of root-agree-but-RN-disagree duration | 10–25 % | **2.91 %** | well below band |
| 4 | Fifth-offset share among applied root-disagreements | 40–70 % | **29.38 %** | below band |

All four came in BELOW the predicted bands. The reason is a premise failure, stated next — this is a
fact-finding run, where the surprise is the product, but it must be surfaced before anything is built on
the numbers (principle #13).

## 3. SURPRISE — the question's premise does not hold at HEAD

The task premise (from register entry D-248) was that applied-chord labels "are not produced by our
analysis." **On the measured surface this is not true at HEAD.** The production batch surface is the
joint estimator's decode (the OI-178 adoption), and its renderer emits the applied "/target" suffix:
`jointRenderRn` — "adds ... the applied \"/target\" suffix" — `src/composing/analysis/joint/jointrender.h:62-63`.
Measured on the committed corpus: **8.62 % of scored duration (1,756 cells, 715,920 ticks) carries an
applied label in OUR Roman numeral** (top emissions by duration: `V/IV` 101,160; `V6/IV` 54,120; `vi/IV`
94,080; `V/V` 24,240; `V6/5/V` 17,280 ticks), and 50,280 ticks of applied-GT cells are EXACT string
matches (`V6/5/V`→`V6/5/V`, `viio7/V`→`viio7/V`, `V/V`→`V/V`, ...).

D-248's verbatim constraint is about the LEGACY function-layer structure — "no `relativeRoot`/
secondary-dominant field in `ChordFunction`" (`decisions/group_H.md:111-121`, home ARCHITECTURE.md) —
which is a different surface from the joint estimator's label classes. So the register entry's plain-words
restatement ("Applied-chord labels such as V/V are not produced") no longer describes the production
batch surface; the scope mismatch between D-248 and the OI-178 surface is itself a finding for the
parent to row. Consequently the four quantities below measure "RN residual attributable to applied-GT
cells," NOT "cost of an absent feature" — the feature exists on the production surface at some accuracy.

(Caveat on the raw JSON: `raw_results.json.n_our_applied_label_violations = 0` tested the chord-LETTER
symbol field, not the Roman numeral — it is superseded by `overlap_results.json.ours_applied_dur`, the
correct check, which found the 715,920 ticks above.)

## 4. The four quantities (duration-weighted, with denominators)

Scored duration total: **8,300,640 ticks** over 18,858 cells, 326 pieces.

1. **Applied share of total scored duration: 4.11 %** — 340,920 / 8,300,640 ticks (876 / 18,858 cells).
2. **Applied share of root-disagreement duration: 5.42 %** — 103,320 / 1,906,320 ticks
   (278 / 4,980 cells). Applied-GT cells are only mildly enriched among root errors (5.42 % vs 4.11 %
   base rate).
3. **Applied share of root-agree-but-RN-disagree duration: 2.91 %** — 31,200 / 1,072,080 ticks
   (89 / 2,229 cells). The "right chord, wrong name" slice attributable to applied-GT cells is 31,200
   ticks = **0.38 % of all scored duration**.
4. **Fifth-offset share among applied-GT root-disagreements: 29.38 % by duration** — 30,360 / 103,320
   ticks (offsets our−GT ≡ ±5 mod 12; 71 / 278 cells = 25.54 %). The offset histogram is broad
   (5: 23,040; 3: 14,160; 6: 10,320; 8: 9,360; 4: 9,240 ticks ...) — no single dominant shape.

Derived figures on the same basis:

- **Applied share of TOTAL RN-disagreement duration: 4.52 %** — 134,520 / 2,978,400 ticks. Upper bound:
  if EVERY applied-GT disagreement (including the root errors) were eliminated, RN-agree would move
  64.12 % → at most **65.74 %** (+1.62 pp). The root-agree-only slice (quantity 3) bounds the pure
  naming gain at **+0.38 pp**.
- **Applied-GT cells already RN-AGREE on 60.6 % of their duration** (exact 50,280 + partial 156,120 of
  340,920 ticks) — consistent with the applied labels actually being emitted (and with partial credit
  where the degree matches but the figure differs, e.g. ours `V6` vs GT `V6/5/V`).
- Bucket split of applied-GT duration: partial 156,120; root_err 103,320; exact 50,280; key_disagree
  19,200; quality_disagree 12,000 ticks.
- Most frequent applied GT labels by duration: `V6/5/V` 36,720; `viio7/V` 23,760; `V7/IV` 19,920;
  `viio6/V` 17,040; `V6/vi` 17,040 ticks.

## 5. Overlap with the OI-192 fifth-substitution neighbourhood

The whole fifth-offset family among ALL root-disagreements (both directions) is **737,520 ticks /
1,839 cells** — magnitude-consistent with the OI-192 ~1,470-run enumeration (runs merge adjacent cells).
Of that family, applied-GT cells contribute **30,360 ticks = 4.12 %**. The suspected neighbourhood
relation is therefore weak in BOTH directions: applied-GT cells are a small corner of the
fifth-substitution family, and the fifth shape explains under a third of applied-GT root errors.
The fifth-substitution family is overwhelmingly NOT an applied-label phenomenon.

## 6. Per-piece extremes

- Highest applied-GT share: `bwv244.32` 20.93 % (4,320 / 20,640 ticks), `bwv179.6` 18.57 %,
  `bwv248.46-5` 16.30 %. **56 of 326 pieces contain zero applied-GT duration.**
- Largest applied-attributable RN-disagreement duration: `bwv245.40` 4,560 ticks (of its 39,120 RN-dis),
  `bwv282` 2,880 (its entire applied duration disagrees), `bwv383` 2,760, `bwv248.46-5` 2,640 ticks.
  Even at the extremes, applied-GT cells are a minority of each piece's RN disagreement.

## 7. What the measured stake means for scheduling (the number's meaning only)

The applied-chord axis is a SMALL residual on the Roman-numeral column: a perfect applied-chord
treatment is bounded at +1.62 pp RN-agree (all applied-GT disagreement, root errors included), and the
pure right-chord-wrong-name component is +0.38 pp. Against the RN column's total disagreement of
35.88 % of scored duration, applied-GT cells carry 4.52 % of it. The larger scheduling-relevant fact is
the premise correction: the production joint surface ALREADY emits applied labels (8.62 % of duration,
with exact matches against the GT), so the open question for the D-248 revisit is not "build the
feature" but "reconcile D-248's recorded scope (the legacy `ChordFunction` structure) with the OI-178
production surface, and whether the emitted labels' accuracy warrants targeted work" — a register/spec
reconciliation before any feature scheduling. Both figures carry the usual single-corpus caveat
(principle #24): no resampling was done; differences of a few tenths of a percentage point on this one
corpus are not findings.

## 8. Artifacts (all under this directory)

- `predictions.json` — the four bands, timestamped before measurement.
- `measure_applied_stake.py` — the measurement script (imports the substrate; reimplements nothing).
- `raw_results.json` — the four quantities, denominators, histograms, per-piece extremes (note the §3
  caveat on its violations field). `per_piece.json` — full per-stem tallies.
- `overlap_results.json` — our-side applied emission + the all-cells fifth-family histogram.
- `exact_probe.txt`, `overlap_probe.txt`, `run_log.txt` — probe transcripts.
