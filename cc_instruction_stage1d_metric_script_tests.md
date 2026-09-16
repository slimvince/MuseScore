# CC Instruction: Stage 1d — Pin the Python metric scripts (closes Gate 1→2)

## Context

Master plan: `docs/implementation_roadmap.md` Stage 1, item **1.6** — the last item
before Gate 1→2 (which passes with the documented 1.3 exceptions). These scripts are the
**de-facto definitions of every quality metric the project is judged by** (BIR 24/13 /
35/7, root_agree 53.8%, rn_agree 27.6%). One classifier bug (`quality_err`,
corrected 2026-06-04) already produced wrong conclusions for weeks. After Stage 1d, a
metric-definition change must fail a test, not pass silently.

**⚠ EPISTEMIC RULE for this run (applies to everything): NEVER GUESS.** If you are
unsure how a script behaves, what a function's contract is, or what a fixture should
produce — investigate until you know (read the code, run the script on a probe input),
or state the unknown explicitly in the report. "I verified X by doing Y" or "Unknown:
X, because Y" are the only acceptable forms. A wrong test here would pin a wrong metric
definition — strictly worse than no test. This rule outranks completeness: an honest
NOT-PINNED with a stated unknown beats a guessed assertion.

Mandatory reads: STATUS.md header; `tools/compare_analyses.py` (`align_dcml_regions` —
the lenient-OR time-overlap comparator everything else reuses);
`tools/characterise_bir_false.py`; `tools/compare_rn.py` (incl. the 2026-06-04
classifier fix: `key_disagree` vs `quality_disagree` split); the BIR-script note in
COWORK_HANDOFF.md ("characterise_bir_false ≠ analyze_inversion_errors — different
metrics, not interchangeable").

**Hard constraints:**
- **No changes to the scripts under test.** Test files + fixtures + (if needed) a test
  runner entry only. If you find what looks like a BUG in a script: do NOT fix it —
  pin the current behavior with a `# pins current (suspect) behavior` comment AND list
  it under Findings. Metric definitions only change by explicit decision (it would
  re-baseline everything).
- Python tests live under `tools/tests/` (new directory; pytest if available in the
  venv, plain `unittest` otherwise — CHECK, don't assume: `python -m pytest --version`).
  They must be runnable standalone and documented in `build_and_test.md`? — NO: do not
  edit build_and_test.md in this run; propose the doc line in the report instead.
- C++ suites are untouched; no build needed. State in the report that the production
  binary and corpus are untouched.

## Task 1 — Survey (investigate, don't assume)

For each script, establish and report:
1. **Entry points and data contracts**: exact input formats (`*.ours.json` shape, DCML
   TSV columns, RomanText?), and what each script imports from the others
   (`compare_rn` reuses `compare_analyses.align_dcml_regions` — verify how).
2. **The metric definitions as implemented**: lenient-OR overlap rule (≥50% of WHICH
   side?), BIR=true vs BIR=false classification logic, `compare_rn`'s normalization
   (key-prefix, modulation marker, figured bass, `%`→`ø`, case-sensitivity) and the
   exact `key_disagree` / `quality_disagree` / `partial_match` / `root_err` bucket
   conditions.
3. Where behavior is unclear from reading, run the script on a minimal probe input and
   OBSERVE (document the probe). Do not infer from docstrings alone — the 2026-06-04
   bug lived in a docstring-plausible function.

## Task 2 — Fixture design

Hand-craft minimal fixtures (JSON/TSV) under `tools/tests/fixtures/` with KNOWN correct
outputs derived BY HAND (show the derivation in comments or a fixtures README):
- An alignment fixture: a handful of regions exercising exact-match, partial-overlap
  (just above and just below the lenient threshold — bracket pair), no-overlap,
  multi-candidate overlap (which one wins?), and zero-length/edge ticks.
- A BIR fixture: cases producing BIR=true, BIR=false, and not-counted, including at
  least one enharmonic root case (the pc-vs-spelling distinction).
- A compare_rn fixture: one case per bucket (exact, partial, key_disagree,
  quality_disagree, root_err) + the documented normalizations (`%`→`ø`, case
  sensitivity, modulation marker) + a V→I shape that the OLD broken classifier would
  have miscounted (regression-pin the 2026-06-04 fix).
If any script cannot run on synthetic input without a real score/corpus directory
structure, replicate the minimal directory shape in fixtures — investigate what the
minimum is; if genuinely impractical, NOT-PINNED with the investigated reason.

## Task 3 — Tests

`tools/tests/test_metric_scripts.py` (split if cleaner). Pin per Task-2 fixture, plus:
- the alignment threshold boundary (the lenient-OR ≥50% rule, both sides of the line);
- BIR counting totals on the fixture corpus (exact expected counts);
- compare_rn bucket counts + the sum invariant (key_disagree + quality_disagree
  preserves the old quality_err total on the fixture);
- one determinism check (same input twice → identical output).

## Task 4 — Run and verify

```
cd C:\s\MS && python -m pytest tools/tests/ -q > /tmp/s1d_py.txt 2>&1; echo "exit:$?"
tail -15 /tmp/s1d_py.txt
```
(or the unittest equivalent — per Task-1 finding). Also confirm the scripts still run
unchanged on their real corpus inputs IF cheap (e.g. `characterise_bir_false.py`
against the existing `tools/corpus/` Baroque state — read-only): expected 24/13.
If you run it, report the numbers; if you skip it, say so and why.

## Report — `cc_stage1d_report.md`

1. Survey: metric definitions as implemented (this becomes the reference for Stage 2's
   re-baseline and Stage 5's fitting objective) — with explicit "verified by reading
   code / by probe run" tags per claim, and an **Unknowns** subsection for anything not
   fully established.
2. Fixture derivations (the by-hand expected outputs).
3. Test inventory; NOT-PINNED list with investigated reasons.
4. Findings: any suspect behavior pinned-as-is (metric bugs are decision-items, not
   fixes).
5. Proposed `build_and_test.md` line for running the new tests (text only, not applied).
6. Counts + single-commit proposal (tools/tests/** only), awaiting Cowork confirmation:
   ```
   test: pin the Python metric-script definitions (Stage 1d)

   Known-input/known-output fixtures for align_dcml_regions (lenient-OR
   threshold bracket), characterise_bir_false (BIR=true/false/not-counted,
   enharmonic root), and compare_rn (all buckets incl. the 2026-06-04
   key_disagree/quality_disagree classifier fix, normalization rules,
   determinism). The metric definitions every baseline depends on now fail
   loudly when changed (implementation_roadmap.md 1.6 — closes Gate 1->2).
   Scripts themselves untouched.
   ```

Stop conditions: a script appears to MISCOUNT on a hand-derived fixture (that is a
metric bug — stop and report with the derivation before pinning); the fixtures would
require corpus data; anything where you would otherwise have to guess.
