# CC Instruction: Fix the WiR applied-chord root bug + re-measure the contaminated numbers

## Context — a ground-truth-parser bug, source-confirmed

`dcml_parser.parse_rntxt_file` (`:384-387`) computes the DCML `root_pc` of inline applied
chords from the PRIMARY numeral against the LOCAL key, discarding the applied target:
```python
primary = numeral.split('/')[0] if '/' in numeral else numeral   # :386
root_pc = _compute_root_pc(primary, key)
```
So `V/V`, `viio6/V`, `V6/5/V`, `V/III` etc. get the WRONG ground-truth root on the
**entire Bach WiR gate set (326/353)** — and our analyzer / music21, which resolve the
applied root correctly, are flagged `root_err`. The TSV path is correct (it resolves the
`relativeroot` column via `_resolve_effective_dcml_key`); only the rntxt path is buggy.
**Verified at source by Cowork (line 386) and CC (mid-investigation).** This contaminates
the DCML-only headroom numbers (the 2576 "neither"/95%-functional), and the
functional-residual investigation is paused until the ground truth is corrected.

This is a **deliberate metric-definition correction** (like the Stage-1d F-1/F-2 fixes):
it changes what the ground truth reports, the metric tests get re-pinned, and the numbers
WILL move — that is the point. Base `a4ae4a9203` (or HEAD after the §11 erratum
`bcd4319aa7`). Method A–H. **HELD = `git add` ok, commit NOT until approval.**

## Task 1 — Fix the applied-root resolution in the rntxt parser

The fix mirrors the TSV path's correct behavior. For an inline `numeral` containing `/`:
resolve the applied chain (`/V`, `/III`, the `/x` after the primary — and chained
`/V/V` if present) into the **effective key** (reuse `_resolve_dcml_key` /
`_resolve_effective_dcml_key` — the same machinery the TSV path uses with `relativeroot`),
then compute the PRIMARY's root against THAT resolved key. Concretely: `V/V` in C → the
`/V` tonicizes G → primary `V` in G → root D (2), not G (7).

Requirements:
1. **Consistency with the TSV path is the correctness oracle:** the same applied chord
   (e.g. `V7/V` in a given key) must yield the SAME `root_pc` whether parsed from rntxt
   (inline) or from a TSV `relativeroot` column. Add a test asserting this equivalence.
2. Handle the chain forms present in WiR Bach (`/V`, `/IV`, `/vi`, `viio.../V`, possibly
   `/V/V`) — survey what actually appears [probe], don't assume; unparseable applied
   targets fall back to today's behavior with a logged count (don't silently mis-root).
3. Do NOT change the TSV path (it's correct) — but verify it stays correct (regression).

## Task 2 — Re-pin the metric tests (deliberate re-baseline)

The Stage-1d / metric-primitive tests may encode the buggy primary-only root for applied
chords. Update them to the corrected applied root, each marked
`# re-pinned 2026-06-13: DCML applied-chord root fix (parser bug, was primary-only)`.
Add the rntxt-vs-TSV equivalence test (Task 1.1). The existing non-applied tests must stay
green unchanged. Run the full Python suite; report the count and the re-pinned list.

## Task 3 — Re-measure the contaminated numbers (the scope of the damage)

Quantify how much the corrected ground truth moves the headline figures [probe, committed
modes / the dossier drivers re-run on corrected parser]:
1. **`compare_rn --wir-bach tools/corpus/default`**: the corrected decomposition — exact /
   partial / key_disagree / quality_disagree / **root_err**. Report old (buggy) vs new
   (fixed) for each bucket, and specifically: **how many of the old 2706 root_err were
   applied-chord parser-artifacts** (regions where the DCML numeral contains `/` and the
   corrected root now matches ours). This is the number that says how inflated the
   "95% functional" was.
2. **The "neither" residual:** recompute `all_differ` / the 2576 on corrected ground
   truth — how much shrinks. The functional-residual investigation will resume on THIS
   corrected mass.
3. **Spot-check the key-emission S2** (1032): does the applied-root fix touch it? (S2 is
   key_disagree = root-correct, so likely small, but verify — some S2 cases may have been
   mis-bucketed by the wrong root.) Report whether the 349 keystone lever / the S2 numbers
   move.
4. **Confirm the BIR 13/7 gate is unaffected** (hypothesis: the music21∩DCML filter
   excluded these parser-wrong/we-right cases, so the gate was shielded). Re-run
   `characterise_bir_false --corpus-dir tools/corpus/{baroque,jazz}` — expect 13/7
   unchanged. If it MOVES, that's a second finding (the gate was contaminated too).

## Task 4 — Assess the ripple to prior conclusions

State plainly which prior findings the fix CHANGES vs leaves intact:
- The "95% of root errors are functional" headline (headroom dossier) — by how much does
  the corrected root_err / "neither" reduce it?
- The metric-design "secondaries are already credited as exact" finding — re-verify on
  REAL data (a correctly-emitted `V/V` should now score `exact` *because the DCML root is
  now correct too*); confirm or correct.
- The functional-residual investigation (paused) — restate its target mass post-fix.
- OQ-1 (A-vs-B): does a materially smaller functional residual strengthen A further, or
  change the picture? (Don't decide OQ-1 — note the direction; the resumed
  functional-residual investigation on corrected data is the actual gate.)

## Deliverable — `cc_dcml_applied_root_fix_report.md` + the staged fix

§1 the fix (the resolution logic, the rntxt-vs-TSV equivalence proof); §2 the re-pin
ledger; §3 the before/after numbers (the headline: how much root_err was parser-artifact);
§4 the ripple assessment; §5 unknowns. Every number [probe]; the equivalence oracle
[test]. Commit proposal (tools/dcml_parser.py + tools/tests/**), HELD for Cowork.

Stop conditions: the rntxt-vs-TSV equivalence NOT holding after the fix (the fix is wrong
or the TSV path has its own issue — report, don't ship); the BIR 13/7 gate MOVING (a
second contamination — report before proceeding); discovering the bug also affects a
non-applied case class (widen the report). Do not resume the functional-residual
classification in this run — this run corrects the instrument; the classification re-runs
after, on clean ground truth.
