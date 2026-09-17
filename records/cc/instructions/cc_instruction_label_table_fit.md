# CC instruction — the label-side table fit (the fit event, part 1 of 2; OI-176/OI-177 protocols in force)

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header + 2026-07-19
> entries), `C:\s\MS\BUILD_AND_TEST.md`, **`C:\s\MS\cowork_prefit_gates.md` (the ratified protocols
> this dispatch executes under)**, `cowork_joint_estimator_factorization.md` §3 (the factor forms),
> and the **OI-184 (resolved — consequences bind here), OI-186, OI-176, OI-177 rows** in
> `OPEN_ITEMS.md`.
>
> **Current state:** branch `master`, HEAD `01edaab7bc` (verify; the working tree carries two
> Cowork-authored uncommitted doc edits that ride YOUR commit — `OPEN_ITEMS.md` OI-184 row flip,
> `cowork_handoff.md` state line; verify each is its only diff). **PYTHON-ONLY; no build, no test
> suite, no golden, no corpus regen, no re-baseline, NO DECODING and NO EVALUATION** — this dispatch
> produces fitted TABLES as committed artifacts; nothing is graded (grading needs A's decode, which
> does not exist; the identity-weight baseline is measured at the build arc, not here).
>
> **Hard stops, always:** any edit under `src/`; any edit to pinned instruments
> (`a8_rebaseline_measure.py`, `compare_rn.py`, `compare_analyses.py`, `dcml_parser.py`,
> `robust_stop_diff.py`) or `tools/robust_stop/` — import only; any golden/corpus/baseline touch;
> **any value chosen by looking at any accuracy metric (the DT-2 firewall — everything here is
> mechanical counts under the declared rules below; there is nothing to tune and no metric to peek
> at).**

**Dispatch author:** Cowork, 2026-07-19, at the user's direction. **The declared staging (part of
the fit-event record):** the ratified staged fitting is executed in two data-dependency parts —
THIS dispatch fits every table derivable from the GT LABEL stream (+ notated signature/declared
mode): the same-key chord-transition tables, the key-transition table, the entry table, the
bass/inversion table, the signature/declared-mode prior table, and the boundary-by-beat-class table.
The NOTE-side tables (pitch-emission categories/covariates, spelling — they need note-level
extraction from the scores) are part 2, their own dispatch. Both parts run under the same ratified
protocols; nothing fit in part 1 is ever re-fit in part 2 (fit-scope declaration, gates OI-177 item
5). Layer home: everything new under `tools/joint_estimator/`.

## 1. The fit-time label normalization (OI-186(a) binding; ONE new function, fit-layer-owned)

Write ONE normalization in `tools/joint_estimator/` (do NOT edit `compare_rn`; reuse `crn.split_rn`
for degree/applied-target splitting where it is correct) mapping each raw GT label to the class
`(degree base, quality, inversion figure, applied target)` with quality derived from the FIGURE AND
CASE, not from `extract_quality`:
- half-diminished from the `/o` sigil (e.g. `ii/o6/5` → (ii, HalfDim7, 6/5, —));
- `o` → diminished; case → major/minor color as `crn` already does;
- seventh-chord figures `7 / 6/5 / 4/3 / 2 (42)` → seventh quality (Dom7 on major-color V and
  applied dominants; m7/Maj7/HalfDim7/Dim7 per color+sigil) with the figure as inversion;
- triad figures `(root) / 6 / 6/4` → triad + inversion;
- applied `X/Y`: the class keyed by (X normalized as above, target Y base);
- anything not covered → a `raw_unnormalized` bucket, counted, never guessed.
**Report the full mapping for the count inventory's top 30 classes plus every `/o` and
slashed-seventh form observed** (the OI-186 gap population) — this table in the report is the
review surface. The two `It6` labels: map to the augmented-sixth class (the factorization's standard
chromatic classes), noted explicitly.

## 2. The tables to fit (forms per the ratified factorization §3; counts per training fold)

For EACH of the 5 training-fold complements (fold i held out; `fold_assignment.json` is the
committed assignment) AND once for all-326 (the publishable variant, reported beside — protocol §5):

1. **Same-key chord transition** `P(c_j | c_{j-1}, mode)` — adjacent same-local-key label pairs
   (mode = local key's mode; key-change boundaries excluded — they feed table 2/3). Label-sequence
   based: NOT tick-anchored, so the OI-184 pickup displacement does not affect it (state this in the
   artifact).
2. **Key transition** `P(k_j | k_{j-1})` — (circle-of-fifths tonic distance, mode pair), relative
   and parallel as their own cells.
3. **Entry chord** `P(c | key change)` — first class after each key change.
4. **Bass/inversion** `P(inversion figure | degree base, quality, mode)` — from the labels' figures
   (the GT figure determines the bass chord factor; this is the label-side half of F9).
5. **Signature/declared-mode prior** `P(local key | signature, declared mode)` — parameterized as
   the ratified small categorical: (CoF distance of the local-key tonic from the signature's
   relative pair, local mode), conditioned on declared mode where present. Signature fifths and the
   declared `<mode>` come from the corpus `.xml` headers (a light read; cite the elements used —
   the Stage-4a `<mode>` import record says ~79 zero-signature stems carry declared modes). Counts:
   each piece contributes its GT LOCAL-key durations?? — NO: label-side only, so contribute each GT
   local-key SEGMENT (count 1 per contiguous local-key run, duration-free — declared; the
   duration-weighted variant needs tick anchoring and is not part 1). If the signature/mode
   extraction is not clean, STOP on this table only, fit the rest, report.
6. **Boundary by beat class** `P(segment boundary | beat class)` — tick-anchored, so the OI-184
   consequences BIND: (a) pickup measures (WiR m0 labels) are EXCLUDED from boundary counts
   (declared exclusion, written into the artifact); (b) the 7 flagged local-misalignment pieces
   (`bwv384, bwv274, bwv140.7, bwv113.8, bwv110.7, bwv123.6, bwv112.5` — the OI-184 row) are
   EXCLUDED from boundary counts entirely; (c) beat classes: downbeat / mid-measure strong beat
   (beat 3 in 4/4 only) / other tactus beat / sub-tactus, meter from the corpus xml per piece,
   measure anchors through the established `compare_analyses` machinery (imported). Denominator =
   GT-label-slot events, i.e. for each beat position of each counted measure, boundary iff a GT
   label starts there.

**Pooling and smoothing (the ratified OI-177 budget rule, executed mechanically):** a cell keeps its
own MLE iff its training count ≥ 20; below, it pools to its declared parent. The declared back-off
chains (fixed here, part of the protocol record): table 1: (from-class, to-class) → drop both sides'
inversion figures → drop quality detail to triad/seventh family → P(to-class | mode) unigram;
table 3: class → inversion-free → unigram; table 4: (degree, quality) row → (quality) row →
inversion-figure marginal; table 2: distance ≥ 3 pooled per mode pair → mode-pair marginal; table 5:
distances beyond ±1 pooled per mode; table 6: no pooling expected (few cells — if any cell < 20,
report it). Additive smoothing α = 1 at the final back-off level of each chain (the declared single
α per table). No other smoothing, no exceptions, no judgment calls — where these rules produce
something odd, REPORT it, never adjust.

## 3. The OI-177 parameter-inventory artifact (the gate's pass evidence)

`tools/joint_estimator/table_fit_inventory.json` (+ generated summary txt), per fold and overall:
every table's dimensions, raw-cell histogram, own-MLE cell count, pooled-cell count, effective free
parameters, training tokens, and the tokens/params ≥ 10 check (the artifact computes it; if ANY fold
fails the bound, STOP and report — the vocabulary/pooling decision returns to Cowork). **The §4.3
sensitive cells' treatment records, by name, per fold** (expected: `V6→viø7` (2), `viø7→IV` (3),
`vi→V/vi` (11) pooled; `i→IV-raised-6` (40), `applied-not-resolving` (154), `V→vi` (236) own-MLE —
verify against the fitted artifacts and report the actual fitted values each receives). The fitted
tables themselves: `tools/joint_estimator/tables_fold{0..4}.json` + `tables_all.json`, every file
carrying provenance (corpus git_hash, fold source, generator, normalization version).

## 4. Establishment (#19)

(i) Byte-reproducible on a second run (all artifacts). (ii) Every table row sums to 1 within 1e-9
after smoothing (mechanical check in the generator). (iii) Spot reconciliation: table-1 raw pair
counts must total the count inventory's same-key transition total (16,372) on the all-326 variant;
key changes 1,720; label totals 18,418 — exact, or STOP (the two instruments disagree about the
ground truth). (iv) Three hand-checks in the report: for `V→I` (major), `i→V` (minor), and
`V→vi` (major), show raw count → probability arithmetic explicitly.

## 5. Commit

**One commit:** `tools: the label-side table fit — fitted tables per fold + the OI-177 parameter inventory (fit event part 1)` —
the fitter, the normalization module, the artifacts, this instruction file (force-add), plus the two
named Cowork doc edits riding along. Push **origin only** (the standing `cfc7eb5e39` hard stop).

## 6. Self-check before reporting (standing rule)

Re-read the actual diff: nothing outside `tools/joint_estimator/` + this file + the two named doc
files; pinned instruments untouched (empty diff proven); no decode, no evaluation, no metric
consulted anywhere in the code path (grep your own generator for any import of the grading
machinery beyond count reconciliation — the fitter must not even be able to see accuracy); artifacts
generated, no hand-typed figure. **Report:** the normalization mapping table (§1); per-table
raw/kept/pooled/params figures per fold; the tokens/params check; the sensitive-cell treatments and
fitted values; the three hand-checks; the boundary-table values with the exclusions stated; the
signature/prior table or its STOP; reuse-vs-new; anomalies (#13 — a surprise is reported, never
built around).
