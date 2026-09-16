# CC INSTRUCTION — A-8 granularity-robust metric: the re-baseline MEASUREMENT (read-only, 2026-07-03)

**Status: ACTIVE DISPATCH (the only open instruction). Read-only / decode-only / byte-identical by construction —
no `src/` change, no behavior change, no gate change. This arc MEASURES the candidate re-baselined gate; the
re-baseline itself is a SEPARATE user-ratification event on this report. Stage-5 runway step 1 (user-ratified
sequencing principle: metric first — the fitting objective must not inherit measured bias).**

## Mandatory reads BEFORE any work

1. `CLAUDE.md` — bash rules, gate = the 53/24/53 case-identity sets, two-tier class-(a)/(b) policy (read that
   block carefully — its semantics must carry to the new unit).
2. `STATUS.md` header + `BUILD_AND_TEST.md`.
3. `docs/implementation_roadmap.md` — Stage 5.2 (the THREE mandatory qualifiers: granularity, human-only
   adjudication, coverage) + the A-8 amendment block ("move the gate to the granularity-robust
   union-of-boundaries unit … keeping the case-identity + two-tier policy").
4. `cc_stage2_2_ab_dossier.md` §3/§6 — the measured ~7× batch-vs-section undercount this metric exists to fix.
5. `tools/compare_rn.py` — the existing L0/L1 union-of-boundaries grid instruments (`grid_score_regions` et al.)
   + `tools/tests/test_metric_primitives_l0l1.py` + whatever design doc the "design §2" comments reference
   (locate it; cite it in the report).

## What this is

Roadmap 5.2 makes three qualifiers of the current gate mandatory to address before Stage-5 fitting: it is
**batch-granularity** (undercounts user-visible per-beat errors ~7×), **music21-filtered** (an algorithm
adjudicates which DCML disagreements count — music21 is NOT ground truth), and **coverage-truncated** (only
326/353 gate chorales carry WiR human annotations). A-8 (ratified) names the fix: the gate moves to the
**granularity-robust union-of-boundaries unit**, keeping case-identity + the two-tier policy. This dispatch
delivers the **measured candidate baseline** on the frozen gate corpus so the user can ratify the re-baseline on
evidence, not argument.

## Task 1 — pin the candidate definition (in the report, before measuring)

Write the precise candidate-gate definition the measurement instantiates. It must state:

- **The unit:** the union-of-boundaries cell (both sides' boundaries overlaid; each half-open cell scored once)
  — as implemented by the existing L0/L1 primitives; any deviation you need is a STOP, not an edit.
- **The scored respects:** per cell — root agreement, RN agreement, and key agreement, each reported separately
  (do not collapse them; the gate successor is decided at ratification).
- **The adjudication variant, BOTH measured:** (a) the legacy music21∩DCML "genuine" filter (for continuity /
  mapping) and (b) the **human-only (DCML-only) variant** — no music21 filtering anywhere in (b).
- **Coverage:** the per-variant denominator stated explicitly (how many scores, how many cells; the 326/353 WiR
  qualifier restated in cell terms; scores with no human annotation excluded from (b) with the count reported,
  never silently).
- **Case identity on the new unit:** a stable identity per failing cell (`stem@cellStartTick` unless the
  primitives already define one — state which and why it is stable under re-slicing of the OTHER side).
- **Two-tier carry-over:** how class (a) (pitch-class-undecidable: symmetric/share-tone) vs class (b)
  (functional/key regression) is decided per CELL — the same structural test as the current policy, applied at
  cell granularity; state it, don't leave it to the reader.

## Task 2 — measure (read-only; write outputs to files, per the bash rules)

On the frozen gate corpus (the per-preset dirs regenerated per the standard mechanism), for ALL THREE presets:

1. The current batch-granularity gate reproduced first (53/24/53, set-diff vs CLAUDE.md — the anchor).
2. The candidate metric at the union-of-boundaries unit, BOTH adjudication variants, all three respects:
   full per-cell failing-case enumerations written to files under a scratch dir; counts + identities in the
   report (summaries inline; full enumerations as committed-report appendices only if small, otherwise as
   pinned scratch files with paths + line counts stated).
3. **The mapping table:** every current gate case (the 53/24/53 identities) located on the new unit — which
   cell(s) it maps to, and whether it remains failing under (a) and under (b). Any current case that DISAPPEARS
   under the candidate metric is individually explained (unit effect vs adjudication effect).
4. **The undercount verification:** the measured batch-vs-robust failure-count ratio per preset (the dossier
   predicts ~7× on the per-beat view — report the actual ratio on this corpus and this unit).
5. **Class split:** the class-(a)/class-(b) decomposition of the candidate failing sets per preset/variant
   (Task 1's cell-granularity test applied).

## Task 3 — report

`cc_a8_rebaseline_measure_report.md` (force-added per convention), carrying: the pinned definition; all counts
in one table (preset × variant × respect); the mapping table; the undercount ratios; the class split; the
coverage statements; commit SHAs (report them); and a short "decision surface" section laying out what the user
is being asked to ratify (the new gate's unit + variant + respect set + the numeric baseline + identity form) —
**no recommendation beyond the measured facts; the ratification is the user's.**

## Acceptance (ALL required)

1. Read-only proven: no `src/` change; the frozen gate corpus byte-untouched; the ONLY commits are scratch
   measurement scripts under `tools/` or `scratchpad/` (if any are worth keeping — say which and why) + the
   report. If a `compare_rn.py`/primitive change seems needed: **STOP** — that is a Cowork/design decision.
2. The current gate reproduced 53/24/53, set-diff empty both directions, all three presets, BEFORE and AFTER
   the measurement runs (the no-contamination sandwich).
3. Both suites + snapshots green if anything under `tools/` was touched that they cover; otherwise state why a
   build was unnecessary (expected: no build — Python only).
4. Reuse-vs-new + what retires (expected: reuses the L0/L1 grid primitives + dcml_parser + the regen/verify
   machinery verbatim; new = the measurement driver + report; retires nothing — the batch gate remains THE gate
   until the user ratifies the re-baseline).
5. Commit SHAs in the report. Local/unpushed, fork-only.

## STOP conditions

The existing primitives cannot express the pinned definition without modification; the current gate does not
reproduce 53/24/53 at the anchor step; the mapping table cannot account for a current case; any qualifier
(granularity / adjudication / coverage) cannot be honestly stated in cell terms; anything would require touching
`src/` or the frozen corpus.
