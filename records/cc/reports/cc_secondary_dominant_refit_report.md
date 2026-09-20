# CC report — the secondary-dominant pooling amendment (table-1 re-count) + the chord-factor presence table

**Dispatch:** `cc_instruction_secondary_dominant_refit.md` (Cowork 2026-07-19), executing the
user-ratified probe findings 1a and 3a (`cowork_sensitive_cell_probe.md`). **Branch** `master`, on
HEAD `57ed94a6a4`. **PYTHON-ONLY**; no `src/` edit, no build, no test suite, no golden, no corpus
regen, no re-baseline, **NO DECODING, NO EVALUATION**, no accuracy metric consulted anywhere in the
code path (DT-2 firewall, grep-proven). All figures below are read from the generated artifacts
(`table_fit_inventory{.json,_summary.txt}`, `factor_presence_inventory{.json,_summary.txt}`),
never hand-typed (#17f).

## Reuse vs new

- **`gen_label_tables.py` (amended)** — the applied-relation pooling level (option 1a). New: a
  relation-cell classifier `_relation_cell`, its Katz parent chain `_applied_rel_parent`, the
  per-mode override in `fit_tables`, and the effect report. Reuses the existing `katz_distribution`,
  `estimate_conditional`, the ratified constants, and the whole tables-2–6 path unchanged.
- **`gen_note_tables.py` (refactored, output byte-identical)** — extracted the shared framework/root
  derivation into `_framework_and_root`; `member_pcs` now reuses it (#6, one path) and `chord_factor_pcs`
  (new) exposes the ordered factor pcs from the same derivation. **`member_pcs` is byte-identical over
  all 1157 corpus (label, key) combos** (proven twice, old-vs-refactored). No part-2 artifact was
  regenerated or touched.
- **`gen_factor_presence.py` (new)** — the chord-factor presence table (option 3a). Reuses
  `gen_note_tables.gt_segments` (the part-2 GT-segment alignment), `chord_factor_pcs`, the part-2
  exclusion gate `{FLAGGED, MULTIMETER, COUNTED_METERS}`, `gen_label_tables.{THRESHOLD, ALPHA,
  N_FOLDS, _git_head, _rel}`, the committed `note_events.json`, `fold_assignment.json`. New: the
  `sounding_pcs` overlap/onset membership and the per-factor Bernoulli counting.

## Task 1 — the applied-relation pooling level (as-built form, reported)

**The level sits on BOTH sides** (context and outcome), realized this way:
- **Context side:** every applied (target-bearing) from-context whose transitions fell all the way to
  BASE (the mode's plain frequency table — the blindness finding 1 measured) is pooled across **all
  targets** into one relation distribution per mode. An applied context that found a reliable
  per-target level (L0 full / L1 inversion-free / L2 family, each ≥20) keeps it and is **not** pooled
  (23 major, 11 minor kept per-target).
- **Outcome side:** the continuation is re-expressed by RELATION TO THE TARGET — `resolves to a
  chord of its target` vs `elsewhere`. The resolution cell keeps quality-family (triad/seventh) and
  inversion (root/inverted) sub-cells via the unchanged count≥20 Katz rule; precedence collapses
  position first, then quality-family, then the flat `resolve` aggregate. Cells namespaced `«rel»`
  (the part-1 collision lesson). **Resolve and elsewhere have separate terminal bases** so a pooled
  sparse resolution never mixes into the elsewhere mass.

**Counted resolution cells (all-326, raw counts shown):**

| mode | P(resolves to target) | P(elsewhere) | resolve\|triad\|root | resolve\|triad\|inv | resolve (agg, 7th) |
|---|---|---|---|---|---|
| major | **0.7708** | 0.2292 | 0.6471 (raw 319) | 0.1075 (raw 53) | 0.0162 (8 sparse 7th resolutions) |
| minor | **0.7742** | 0.2258 | 0.6598 (raw 225) | 0.0997 (raw 34) | 0.0147 |

Only the triad sub-cells cleared the ≥20 threshold; seventh-chord resolutions are sparse (8 in major)
and pool to the `resolve` aggregate — the counts decided that secondary dominants in this corpus
resolve to a plain **triad** ~98 % of the time, in **root position** ~85 % of the time.

**Applied-context rows before → after:** 64 applied from-contexts (major), 71 (minor). Before: **all
101 overridden contexts read the mode unigram (BASE)** — blind to resolution, exactly finding 1.
After: they read the relation cells. (34 applied contexts — 23 major, 11 minor — kept their reliable
per-target concrete rows.)

**The three passages' affected transition values (so Cowork can re-run the arithmetic):**
- **Passage B — dominant-of-the-subdominant → its target (target `IV`):** the representative
  resolution `IV | Maj` triad now scores **0.647** (major) / **0.660** (minor) as a resolution,
  versus **0.052** / **0.053** as the old mode-unigram lookup — a **+2.5-nat** swing toward the correct
  reading, the correction finding 1 predicted (per-target raw: major IV resolve 113 / elsewhere 28;
  minor iv resolve 69 / elsewhere 20). Target `V`: major resolve 170 / elsewhere 34; minor 102 / 21.
- **Passages A and C are structurally unaffected by this level:** their sensitive transitions
  (`V6→viø7`, `viø7→IV`, deceptive `V→vi`, the A-minor entry chord) are **non-applied** from-contexts,
  and every non-applied table-1 row is **byte-identical** to before the amendment (verified: 0
  non-applied rows changed).

**Parameter-count delta:** table-1 free params (all-326) 411→417 (+6: the two per-mode relation
distributions); total 581→**587**. Capacity re-checked per fold — every fold passes (tok/param
183.8–211.1, ≥10 bound met ~18× over).

**Invariants (all hold, proven):** tables 2–6 **byte-identical** to committed HEAD on all 6 files
(UTF-8 byte comparison); note-side artifacts **untouched** (git-clean); reconciliation **exact**
(labels 18418 / transition pairs 16372 / key changes 1720); byte-reproducible (two runs identical).

## Task 2 — the chord-factor presence table (option 3a)

`P(factor sounds | role, chord family)`, per training fold + all-326; 317 counted stems (same part-2
exclusions: 7 flagged + `{bwv304, bwv362}` multi-meter; m0 segments dropped). Bernoulli per cell,
additive-α=1 smoothed so P(absent) — the missing-tone penalty basis — is never zero (finding-2
option-2c is fatal). Genre scope **declared on the artifact** (Bach-chorale values only). New files
only; part-2 artifacts byte-identical. Byte-reproducible.

**The table (all-326, primary mode 'overlap' = "sounds during the segment"):**

| cell | present/total | P(mle) | P(absent) |
|---|---|---|---|
| root\|triad | 12497/13297 | 0.9398 | 0.0602 |
| third\|triad | 12248/13297 | 0.9211 | 0.0790 |
| fifth\|triad | 12402/13297 | 0.9327 | 0.0674 |
| root\|seventh | 3979/4365 | 0.9116 | 0.0886 |
| third\|seventh | 3816/4365 | 0.8742 | 0.1259 |
| fifth\|seventh | 3683/4365 | 0.8438 | 0.1564 |
| **seventh\|seventh** | 4031/4365 | **0.9235** | 0.0767 |

**The two user sanity expectations — reported, NOT adjusted (the counts are the fact):**
1. **Seventh presence near 1: PARTLY — raw 0.9235, not ≥0.95.** But this raw rate is depressed by
   GT-tick **segment misalignment** (the OI-184 / part-2 anomaly-1 jitter): **1.31 %** of seventh
   segments have **zero** factors sounding — the span holds a different chord entirely (e.g.
   `bwv102.7 V7` whose [16560,16800) sounds C/E♭/A, not the B♭7). **Conditioned on a well-aligned
   segment (root+third+fifth all sounding), P(seventh present) = 0.9732** — "near 1" holds there. The
   alignment diagnostic (factors-present distribution + the aligned rate) is reported **beside** the
   raw table, never used to change it.
2. **Fifth most-omitted: HOLDS for seventh chords** (fifth 0.8438 is the lowest of root/third/fifth);
   **does NOT hold for triads** — the third (0.9211) is marginally lower than the fifth (0.9327), a
   ~1.2 pp gap within the alignment-noise band. Reported as a finding.

**Cross-check (onset-in-segment, part-2's assignment) reported beside:** systematically lower
(seventh 0.7281) because a factor **held over** from the previous chord onsets before the segment and
is missed — which is exactly why 'overlap' is the correct "sounds in the segment" definition; both
are stored for transparency.

## Anomalies surfaced (#13 — reported, never built around; NONE is an inference problem)

1. **Seventh-presence raw rate (0.9235) below the "near 1" expectation**, resolved as the OI-184 /
   part-2 GT-tick alignment jitter (1.31 % zero-factor segments); aligned rate 0.9732. A
   MEASUREMENT-layer property (OI-184 domain), reported with a quantified diagnostic, not adjusted.
2. **Third marginally more omitted than the fifth in triads** (0.9211 vs 0.9327) — a ~1 pp reversal
   of the expectation, within the alignment-noise band; reported.
Neither implicates inference. This is a fact-finding table fit (no decode, no evaluation); the
surprises are reported to Cowork per the scope-of-surprise rule.

## Self-check (post-work, on the actual diff)

Re-read every touched file's diff. Nothing outside `tools/joint_estimator/` + this dispatch file +
the four named Cowork doc edits (`cowork_sensitive_cell_probe.md` new, `cowork_handoff.md`,
`OPEN_ITEMS.md`, `cowork_joint_estimator_factorization.md` §5). Pinned instruments untouched (no
`a8_rebaseline_measure` / `robust_stop_diff` / decoder / grader import — DT-2 grep-clean; the only
`compare_analyses` use is `_dcml_time_spans`/`load_analysis`, `compare_rn` only `_dcml_key_tonic`,
`music21.roman` only the part-2 template oracle). No decode, no evaluation, no accuracy consulted.
All figures generated. Tables 2–6 + all part-2 note artifacts byte-identical. No STOP raised.
