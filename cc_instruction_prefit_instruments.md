# CC instruction — the two pre-fit instruments (read-only; OI-176 fold assignment + OI-177 count inventory)

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header + the three
> 2026-07-19 entries), `C:\s\MS\BUILD_AND_TEST.md`, and **`C:\s\MS\cowork_prefit_gates.md` (the
> ratified protocols this dispatch begins executing)**.
>
> **Current state:** branch `master`, HEAD `61a8ed750f`, working tree clean, in sync with origin.
> Ratified robust-unit baselines: CLAUDE.md gate block (A) (root-agree 66.04 / 64.98 / 65.93 %,
> re-baselined at the OI-168 fix). **This dispatch is PYTHON-ONLY, read-only with respect to all
> measurement surfaces — no build, no test-suite run, no golden, no corpus regen, no re-baseline.**
>
> **Hard stops, always:** any edit under `src/`; any edit to `tools/a8_rebaseline_measure.py`,
> `tools/compare_rn.py`, `tools/dcml_parser.py`, `tools/robust_stop_diff.py`, or anything under
> `tools/robust_stop/` (the pinned instruments and the committed reference — IMPORT them, never
> modify); any golden refresh. If a task below seems to require modifying a pinned instrument,
> **STOP and report** instead.

**Dispatch author:** Cowork, 2026-07-19, at the user's direction — the first execution step of the
ratified pre-fit gates (`cowork_prefit_gates.md`, user-ratified 2026-07-19; commit `61a8ed750f`).
Layer home: these are MEASUREMENT-LAYER instruments; everything new lives under
**`tools/joint_estimator/`** (new directory — the joint estimator is the established name for the
ratified architecture A). Nothing here fits a value, builds inference code, or touches the analysis
layers.

**Unification report (mandatory in your report):** reuse-vs-new per file, and what retires (expected:
nothing retires — these are new instruments; say so explicitly if true, or surface any duplication
you notice per the TOTAL UNIFICATION rule).

---

## Task A — the OI-176 fold-assignment artifact

**Goal:** the committed, seeded, grouped 5-fold assignment the ratified protocol requires — generated
once, never regenerated outside a protocol amendment.

1. **New generator `tools/joint_estimator/gen_fold_assignment.py`.** It must:
   - Enumerate the WiR-covered stems through the EXISTING coverage logic — import
     `dcml_parser.find_wir_file` / the same resolution the a8 instrument uses; do not re-derive
     coverage. **Establishment check: the covered-stem count must equal 326** (the block-(A)
     coverage). If it does not, STOP and report the discrepancy — do not proceed on a different
     population.
   - **Group by WiR analysis file:** stems resolving to the same `analysis.txt` path share a group
     (the ratified leakage guard; expected: 326 stems → 324 files, i.e. a small number of multi-stem
     groups — publish the multimap and the multi-stem groups in the artifact).
   - **Balance weight:** per-stem graded duration, computed by IMPORTING the a8 machinery
     (`a8_rebaseline_measure.build_piece_grid` and the loaders it uses) against the committed
     **Default** corpus dir, taking `PieceGrid.scored_dur` — the declared, preset-independent balance
     weight (fold membership itself is preset-independent). No a8 file is edited; if the import
     cannot be done cleanly without modification, STOP and report.
   - **Assignment:** seeded shuffle of the group list (seed **20260719**, committed in the artifact),
     then deterministic greedy: assign each group in shuffled order to the currently
     lightest-total-duration fold. 5 folds (the ratified constant).
   - **Output:** `tools/joint_estimator/fold_assignment.json` — per fold: stem list, group list,
     piece count, total scored duration; plus provenance: corpus `git_hash` (HEAD at generation),
     the seed, the generator's own path, the coverage count, and the analysis-file multimap. The
     manifest pattern (#17f): every figure in the artifact generated, nothing hand-typed.
2. **Reproducibility check (establishment, #19/#16):** run the generator twice; the two outputs must
   be byte-identical. Include the check's result in the report.
3. The 12 OI-142-transposed stems are ordinary members (their GT correction lives at the loading
   substrate) — no special-casing; note their fold placements in the report for the record.

## Task B — the OI-177 count-inventory instrument (counts only — NOT values, NOT a vocabulary decision)

**Goal:** the generated count basis the capacity budget will be checked against at the fit event.
This instrument aggregates RAW ground-truth counts; it decides nothing (no threshold applied, no
vocabulary pooled — that happens at fit time inside training folds per the ratified protocol).

1. **New instrument `tools/joint_estimator/gen_count_inventory.py`,** reading the ground truth ONLY
   through `dcml_parser.load_wir_regions` (the corrected substrate) for the 326 covered stems, and
   normalizing Roman-numeral labels ONLY through the existing `compare_rn` parsing/normalization
   (reuse — do NOT write a second RN parser; if the existing normalization cannot express something
   Task B needs, count it under a `raw_unnormalized` bucket and report the gap — do not invent).
2. **Counts to publish** in `tools/joint_estimator/count_inventory.json` (+ a short generated
   `count_inventory_summary.txt`), each table keyed by fold (from Task A's artifact) AND totaled:
   - (a) the raw GT label histogram, and the normalized (degree, quality, inversion-figure,
     applied-target) class histogram with the normalization rules stated in the artifact;
   - (b) same-key adjacent-label transition pair counts, per mode (major/minor of the local key),
     key-change boundaries excluded from (b) and counted in (c);
   - (c) key-change counts by (circle-of-fifths tonic distance, mode pair), including the
     relative/parallel identifications;
   - (d) entry-chord counts (the first label after each key change);
   - (e) **the desk-sim §4.3 sensitive cells' raw counts, by name** (as expressible in the raw label
     space: V6→viø7-class, viø7→IV-class, i→IV-raised-6, vi→V/vi, applied-not-resolving-to-target,
     V→vi; state the label mapping used for each);
   - (f) total token counts (labels, transition pairs, key changes) per fold and overall — the
     denominator basis for the params ≤ tokens/10 budget check.
   - **EXCLUDED, deliberately:** any boundary/metric-position table counts — gated on OI-184 (the
     anacrusis alignment establishment); write that exclusion into the artifact.
3. **Establishment checks:** (i) region totals reconcile against an existing consumer — for 3 stems
   of your choice plus `bwv110.7`, the instrument's per-stem region count must equal what
   `load_wir_regions` returns and the label sequence must eyeball-match the `analysis.txt` (show one
   short excerpt per stem in the report); (ii) unparseable/unnormalizable label rate reported — if it
   exceeds 2 % of labels by count, STOP and report before committing (that rate would undermine the
   count basis).

## Commits

**Two commits** (one per instrument — independent revertibility):
1. `tools: the OI-176 fold-assignment generator + the committed 5-fold assignment artifact` —
   generator + artifact + this instruction file (force-add, `/cc_*.md`) + `cowork_handoff.md`
   (Cowork's already-on-disk state/pending-line update naming this dispatch — verify that is its
   only diff).
2. `tools: the OI-177 count-inventory instrument + the committed count artifacts` — instrument +
   the two artifacts.
Push **origin only** (the standing `cfc7eb5e39` hard stop on upstream).

## Self-check before reporting (standing rule)

Re-read the actual diff: nothing outside `tools/joint_estimator/` + this instruction file + the named
`cowork_handoff.md` line; no pinned
instrument modified (git diff empty on them); artifacts carry provenance and no hand-typed figure;
the reproducibility check ran. **Report:** commit hashes; the fold balance table (pieces + duration
per fold); the multi-stem groups; the 12 transposed stems' folds; headline counts (total labels,
transition pairs, key changes; the (a) histogram's top ~15 classes and its tail size); each §4.3
sensitive cell's raw count; the unparseable rate; reuse-vs-new; anomalies/surprises (a surprise here
is a finding to report, not to build around — #13).
