# CC Instruction: Build the L0–L1 metric primitives (ratified design)

## Ratification

`docs/precision_metric_design.md` is **RATIFIED** (read in full + load-bearing probe
verified against source: `classify_pair` does credit a correct secondary as `exact`;
`compare_rn` is DCML-only). Decisions:
- **OQ-G1 → union-of-boundaries grid (exact)**, as recommended. Not a fixed metrical
  grid (which would add a tunable).
- **OQ-L1 (cadence token), OQ-L2 (secondary normalization), OQ-C1 (held-out split) →
  DEFERRED to the contract co-design with Stage 4.2 / Stage 6** — they are Stage-6
  output-design forks, correctly not guessed; not needed for L0–L1.
- **OQ-V1 (music21 version)** is already on the corpus-audit C2 list; the DCML-only
  metric doesn't depend on it. No action here.
- The label-vocabulary contract (§3.1) is a Stage-6 artifact — NOT built now.

This run builds **only the three metric-first primitives (design §4.1 BUILD 1–3)** —
tools-only, DCML-only, reuse-based, **no production/C++ change**, no Stage-6 vocabulary.
They unblock measuring Stage 4. Base `a652dc1ba7`. Method A–H; held means held.

## Task 1 — `compare_rn --wir-bach DIR` (BUILD 1)

Promote the headroom dossier's Bach-WiR wiring to a committed `compare_rn` mode
(parallel to `--corpus`/`--cross-corpus`): for each `{stem}.ours.json` in DIR, resolve
the WiR `analysis.txt` via the existing `dcml_parser.find_wir_file`, parse with the
existing `parse_rntxt_file`, align with the existing `align_dcml_regions`, classify with
the existing `classify_pair`. **Orchestration only — zero change to any metric
definition** (the cc_stage1d NOT-PINNED "cross-corpus orchestration is not a metric
definition" basis applies). Must report the **326/353 denominator explicitly** (never
silently divide by 353; print covered/total).

## Task 2 — The duration-weighted union-of-boundaries unit (BUILD 2, the one new primitive)

Implement design §2: a scoring unit that is segmentation-invariant.
- Grid = union of region boundaries from both sides over the piece tick span → half-open
  cells `[t_i, t_{i+1})` constant on both sides by construction.
- Per cell: point-sample our active region + DCML active row at `t_i` (reuse the
  `align_dcml_regions` span arithmetic as point-membership), classify via the reused
  `classify_pair`, weight by `(t_{i+1} − t_i)`.
- Report duration-weighted bucket fractions (`Σ dur(bucket) / Σ dur(all)`).
- A new `--granularity-robust` (or equivalent) flag/mode; the existing region-count
  buckets stay available and unchanged (do NOT redefine the current metric — add the
  unit alongside).

**The load-bearing test (the property that justifies the whole design):**
**segmentation-invariance** — a known fixture scored at two different segmentations of
the SAME underlying analysis must yield the SAME duration-weighted fractions (the 2.2-i
batch-vs-section pair is the natural fixture: the §2 claim is they now agree). Pin it.
Plus: hand-derived known-input/known-output on a tiny fixture (cells + durations +
expected weighted fractions), an edge case (zero-length/coincident boundaries), and a
determinism check.

## Task 3 — `--key-breakdown` key-context sub-tag (BUILD 3, makes Stage 4 measurable)

Promote the dossier's `key_confound.py` cross-tab to a committed `compare_rn` sub-tag:
split `key_disagree` into **`=global ≠local`** (tonicization label-gap, S1 — Stage 6)
vs **`≠global`** (genuine key error, S2 — Stage 4), using the key fields both sides
already carry (our tonic+mode vs DCML local/global key, both resolved by `dcml_parser`).
Report the split. This is the L1 instrument Stage 4 is measured on. Note the dossier's
2.4% our-key parse-failure caveat — report it, don't hide it in a bucket.

## Task 4 — Tests + verification

- Extend `tools/tests/` with: the segmentation-invariance test (Task 2), the
  hand-derived unit fixture, the `--wir-bach` denominator test, the `--key-breakdown`
  split test. All [probe]/[hand-derived]-grounded.
- The existing 70 metric tests stay green UNCHANGED (no buckets redefined). State this.
- Reproduce the dossier's headline numbers via the new committed modes (not the
  throwaway drivers): Bach `--wir-bach tools/corpus/default` → the §1.2 decomposition
  (root_err 2706, the identity); `--granularity-robust` → one number that doesn't swing
  batch↔section on a sample; `--key-breakdown` → the 63/37 S1/S2 split. These reproduce
  the dossier (which used /c/tmp drivers over the same pinned functions) and confirm the
  committed modes match.
- No corpus regen needed (batch `.ours.json` already on disk); no C++ build.

## Commit — held for Cowork

ONE commit (tools + tests): `feat: DCML-only metric primitives — --wir-bach,
granularity-robust unit, --key-breakdown (ratified precision-metric design L0–L1)`.
Body: the three primitives, the segmentation-invariance property, the reproduced
dossier numbers, "70 existing metric tests unchanged."

## Report — `cc_metric_build_l0l1_report.md`

§1 each primitive as built (+ where it reuses vs adds); §2 the test inventory
(esp. the invariance proof); §3 the reproduced dossier numbers via committed modes;
§4 deviations/unknowns.

Stop conditions: any existing metric test needing a change (a bucket redefinition snuck
in — stop, that's not L0–L1); the segmentation-invariance test FAILING (the §2 design
claim is wrong — stop and report, it reshapes the unit); the committed modes NOT
reproducing the dossier numbers (a wiring divergence — find it); any temptation to start
the label-vocabulary contract or emit functional labels (that's Stage 6, not this run).
