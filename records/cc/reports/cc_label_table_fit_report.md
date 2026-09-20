# CC report — the label-side table fit (the fit event, part 1 of 2)

**Dispatch:** `cc_instruction_label_table_fit.md` (Cowork 2026-07-19). **Branch** `master`, on top of
HEAD `01edaab7bc`. **PYTHON-ONLY**; no `src/` edit, no build, no test suite, no golden, no corpus
regen, no re-baseline, **NO DECODING and NO EVALUATION** — this produces fitted TABLES as committed
artifacts; nothing is graded. All figures below are read from the generated artifacts
(`tools/joint_estimator/table_fit_inventory{.json,_summary.txt}`), never hand-typed (#17f/DT-11).

## What was built (reuse vs new)

New under `tools/joint_estimator/` only:
- **`normalize.py`** — the OI-186(a) FIT-TIME label normalization (ONE new function set). Reuses
  `dcml_parser._split_rntxt_applied` (applied split) and `compare_rn.normalise_rn`/`split_rn`
  (degree + verbatim suffix). The only genuinely new logic is **quality-from-figure+case** (NOT
  `compare_rn.extract_quality`, the OI-186 requirement) and the augmented-sixth mapping for the
  `split_rn`=None tokens.
- **`gen_label_tables.py`** — the fitter. Reuses `dcml_parser.load_wir_regions` (OI-142 substrate),
  `compare_rn._dcml_key_tonic` (the one key-string reduction), `normalize`. Reads the corpus xml
  **headers** for signature/mode/meter (`<key><fifths>`, `<key><mode>`, `<time><beats>`,
  `<time><beat-type>`). **DT-2 firewall: no grader/decoder/accuracy function is imported or called
  anywhere** (grep-verified; only parsers + the count-inventory JSON for reconciliation).

Committed artifacts: `tables_fold0..4.json`, `tables_all.json`, `table_fit_inventory.json`,
`table_fit_inventory_summary.txt`. Each fitted-table file carries provenance (corpus git_hash, fit
scope, normalization version, the ratified constants).

## §1 — the fit-time normalization mapping (the review surface)

Every one of the **230 distinct raw WiR labels** (18,418 tokens over the 326 covered stems)
normalizes; **raw_unnormalized = 0** (the 2 `It6` tokens route to the AugSixth class). Quality is
derived from the FIGURE and CASE — this is the OI-186 fix demonstrated:

| raw | → class (degree \| quality \| inversion \| target) | note |
|---|---|---|
| `V6/5` | `V \| Dom7 \| 6/5 \|` | extract_quality read this **Maj**; now **Dom7** (the seventh figure is seen) |
| `ii/o6/5` | `II \| HalfDim7 \| 6/5 \|` | extract_quality read this **Min**; now **HalfDim7** (the `/o` sigil) |
| `ii6/5` | `II \| Min7 \| 6/5 \|` | seventh from figure, minor color from case |
| `viio6` / `viio7` | `VII \| Dim \| 6 \|` / `VII \| Dim7 \| 7 \|` | dim from the `o` sigil |
| `IVmaj7` | `IV \| Maj7 \| 7 \|` | `maj` marker |
| `V7/IV` | `V \| Dom7 \| 7 \| IV` | applied target preserved (case-preserved) |
| `It6` / `It6/ii` | `It \| AugSixth \| 6 \|` / `… \| ii` | the two augmented-sixth tokens |

Every `/o` half-dim form (28 distinct labels) → `HalfDim7`; every slashed seventh figure → the
correct seventh quality. Full mapping in `normalize.py`'s self-test output and the top-30 + `/o`
tables it prints.

**Anomalies surfaced (#13 — reported, never built around):**
- **Ninth figures** `9`/`9[b9]` (2 labels: `V9/V`, `V9[b9]`) are outside the dispatch's enumerated
  inversion set `{7,6/5,4/3,2,42}`; mapped to the dominant-seventh family (a ninth carries a
  seventh) with the figure retained verbatim. Flagged in the inventory notes.
- **Multi-level applied** (3 labels: `V6/5/V/III`, `V2/V/III`, `V/V/III`) are peeled to a clean base
  chord with the applied chain joined as the target (e.g. `V/III`), iterating
  `dcml._split_rntxt_applied` (no new parser).

## §2/§3 — the six tables (per training-fold complement + all-326)

Fit for each of the 5 training-fold complements (fold *i* held out) AND all-326. Pooling/smoothing:
**Katz-style back-off with a hard count-≥20 reliability gate and additive α=1 at the pooled base**
(the single α per table). Reliable cells keep their **exact MLE**; sparse cells pool into their
declared parent (the §2 chains), residual mass α-smoothed; **every row sums to 1** by construction.

**Interpretation reported (#13):** the table-1 chain "drop BOTH sides' inversion" is realized as
context (from-side) coarsening at the row level PLUS within-row outcome pooling — the from-side is
not coarsened per-sparse-cell (which would need cross-row redistribution). The named sensitive cells
behave exactly as specified. Two bugs found and fixed during the fit (both collisions between a
pooled bucket key and a real fine key): **outcome-side** (`I|Maj|6` pooling to `I|Maj||` overwrote
the real root-position outcome) and **context-side** (root-`i`'s row wrongly aggregated the
inverted-`i` transitions) — fixed by namespacing pooled buckets and back-off levels.

**All-326 free params by table:** table1 major=258 / minor=153; table2=11; table3=21; table4=121;
table5 (major 6, minor 7, none 0); table6=4; **TOTAL 581**.

### Table 5 — signature/declared-mode prior (per local-key SEGMENT)
Signed circle-of-fifths displacement of the local key's diatonic **collection** (minor keys use the
relative-major signature) from the notated signature fifths, folded to (−6,6], kept for {−1,0,+1},
|d|≥2 pooled to `far`, per **local mode**, conditioned on declared mode. Musically sane: declared
major → `0|M` 0.477 (home), `1|M` 0.185 (dominant), `0|m` 0.129 (relative minor); declared minor →
`0|m` 0.357 (home), `0|M` 0.240 (relative major), `−1|m` 0.159 (subdominant).
- **Extraction clean** (no STOP): all 326 xml headers read; **3 multi-signature pieces**
  (`bwv244.15, bwv4.8, bwv62.6`) use the INITIAL signature — flagged; **1 piece** has an empty
  declared `<mode>` → `declared_mode=none` is degenerate (1 piece, all segments pooled → BASE 1.0),
  flagged.

### Table 6 — boundary by beat class (tick-anchored; OI-184 exclusions BIND)
Denominator = a **16th-note (0.25 quarter-beat) grid** per counted measure (finest resolution
capturing every observed WiR label beat with no snapping); a slot is a boundary iff a GT label starts
there. **Exclusions applied:** pickup measures (WiR m0) and the **7 OI-184 flagged pieces**
(`bwv384, bwv274, bwv140.7, bwv113.8, bwv110.7, bwv123.6, bwv112.5`), plus **2 multi-meter pieces**
(`bwv304, bwv362`) — all declared in the artifact. 317 pieces counted, 1 out-of-grid label start.

| beat class | boundary | slots | P |
|---|---|---|---|
| downbeat | 4335 | 4374 | **0.9911** |
| mid_strong (beat 3 in 4/4) | 3311 | 3696 | **0.8958** |
| other_tactus | 6710 | 8748 | **0.7670** |
| sub_tactus | 3311 | 50454 | **0.0656** |

This reproduces the Temperley change-on-strong-beat shape (above-tactus ≫ tactus ≫ sub-tactus)
exactly. **Caveat reported:** the sub-tactus probability is grid-dependent; the note-event
denominator is part 2 (§3.7).

## §4 — establishment (#19)

- **(i) Byte-reproducible** — run twice, all artifacts byte-identical (7/7).
- **(ii) Row sums** — every table-1/2/3/4/5 row sums to 1 within 1e-9 (else the run STOPs); table 6
  Bernoulli values all in [0,1].
- **(iii) Reconciliation to the count inventory (all-326): labels 18418, transition pairs 16372, key
  changes 1720 — EXACT** (else the run STOPs).
- **(iv) Hand checks (all-326 raw MLE):** V→I (major) 377/1350 = 0.2793; i→V (minor) 221/1283 =
  0.1723; V→vi (major) 25/1350 = 0.0185. Each matches the fitted own-MLE cell.

## OI-177 capacity budget — PASS on every fold

| fit | tokens | free params | tokens/param | pass |
|---|---|---|---|---|
| fold0 | 99069 | 533 | 185.9 | ✓ |
| fold1 | 99602 | 517 | 192.7 | ✓ |
| fold2 | 99649 | 520 | 191.6 | ✓ |
| fold3 | 98869 | 522 | 189.4 | ✓ |
| fold4 | 98491 | 528 | 186.5 | ✓ |
| all | 123920 | 581 | 213.3 | ✓ |

Every per-table tokens/param ≥ 10 too (tightest: table1 ≈ 39). The bound (≥10) passes ~19× over.

## The §4.3 sensitive cells — counts + fitted handling

Counts match the count-inventory authoritative values, with two **explained** normalized-vs-raw
deltas (both because the fit-time normalization is FINER / more complete — the OI-186 intent):

| cell | raw (count-inv) | normalized | disposition | note |
|---|---|---|---|---|
| V6→viø7 | 2 | 2 | pooled (<20) | |
| viø7→IV | 3 | 3 | pooled (<20) | |
| vi→V/vi | 11 | 11 | pooled (<20) | |
| i→IV-raised-6 | 40 | 40 | own-MLE aggregate | mass spread across pooled inversion cells |
| applied-not-resolving | 154 | **155** | own-MLE aggregate | +1: `bwv60.5 It6/ii→V7/ii` now visible (It6 mapped) |
| V→vi (deceptive) | 236 | **235** | own-MLE aggregate | −1: `bwv90.5 V→bVI` — bVI accidental preserved (#12) |

The disposition (≥20 vs <20) is the AGGREGATE over the predicate; the fitted table gates each FINE
transition individually. Example (V→vi): the mass sits in own-MLE cells — V7→vi (79, P=0.113), V7→VI
minor (59, P=0.128), V→vi root (25, P=0.0197) — the constituent fine transitions and their fitted
handling are in the inventory (`top_constituent_fine_transitions`).

## Self-check (post-work, on the actual diff)

Nothing touched outside `tools/joint_estimator/` + the instruction file + the two named Cowork doc
edits. Pinned instruments untouched (no import of `a8_rebaseline_measure`, `compare_analyses`
grading, `robust_stop_diff`, any decoder). No decode, no evaluation, no accuracy consulted. All
artifacts generated, no hand-typed figure. American English; the internal keys (`L0/L1`,
`«invfree»/«family»`, `cofFar`) are mechanism identifiers documented in the inventory notes.

**No STOP raised.** No inference problem was discovered; the anomalies above are normalization /
table-design reporting items for Cowork, not inference surprises.
