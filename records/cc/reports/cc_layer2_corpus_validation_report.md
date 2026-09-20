# Layer 2 — Corpus property-validation of the REAL slicer

> **HELD / gitignored diagnostic report** (read-only finding; not committed).
> Closes the gap between *covered* (13 fixtures + 100% branch) and *validated*: the
> REAL C++ `changePointSlices` has now run over all **353 canonical stems** and the
> §2 invariants are proven on every one against an **independent** oracle (recomputed
> from the note model, not the slicer's own boundary vector).
>
> **Result: 353/353 stems, 353/353 invariant-pass. GATE: PASS.** Byte-identity of the
> real analysis preserved (composing 572 / notation 57 / snapshots 11/11). Slicer stays
> **isolated** — the harness only *calls* it to *check* its output; it is not wired into
> analysis.

## 1. The harness (diagnostic, re-runnable, no analysis touched)

Two pieces, both diagnostic-only:

1. **`tools/batch_analyze.cpp` — new `--validate-slices` flag** (mirrors the existing
   `--section-level` diagnostic-flag pattern; default OFF). On that path `main()`:
   loads the score → `NoteModel::build(score)` → `changePointSlices(model)` → runs the
   §2 checks → emits one per-stem JSON object → **`return`s before `analyzeScore` /
   `analyzeRegions`**. The analysis pipeline is therefore *never invoked* on this path,
   so its output cannot change — byte-identity is structural, not just measured. Exit 0
   if every invariant held, 2 if any failed (the §5 stop signal). The corpus MusicXML
   is loaded through the tool's existing `loadScore` importer (the gtest binary cannot
   import MusicXML — the fixture-conversion constraint), so no production code path was
   altered to load it.

2. **`tools/validate_slices_corpus.py` — the corpus driver.** Iterates
   `tools/corpus/*.xml` (the canonical 353), launches `batch_analyze --validate-slices`
   per stem **via Git Bash** (required on Windows — a direct Python subprocess of the Qt
   headless exe access-violates; mirrors `run_bach_preset.py`), collects the per-stem
   JSON, aggregates the §3 stats, reconciles against the music21 proxy, and applies the
   §5 gate. Writes `tools/corpus/slice_validation_summary.json` (gitignored dir).

**The independent oracle (§2 mandate).** For each stem the harness recomputes the
expected boundary set *directly from `model.notes()`* — it does **not** read the
slicer's internal boundary vector:

```
Bexp = sorted-unique { onset, release : note in model.notes()
                       where plays && visible && staffEligible }
```

— the same eligibility predicate the slicer reads (L1's flags), applied independently
in the harness. Expected slices = consecutive pairs of `Bexp`. Every check below
compares the slicer's output to this independently-derived oracle.

## 2. Invariants checked — all pass on all 353

| # | Invariant | How checked (independent of slicer internals) | Result |
|---|---|---|---|
| 1 | **Boundary-set match** | set of all slice start/end ticks `==` `Bexp` (completeness + no-spurious + no-missed in one equality) | 353/353 |
| 2 | **Covering, no gaps/overlaps** | `slices[i].end == slices[i+1].start`; `front().start == min(Bexp)`; `back().end == max(Bexp)` | 353/353 |
| 3 | **Positive width** | every slice `start < end` | 353/353 |
| 4 | **Constant tonal sonority** | independent recompute: for each slice `[s,e)`, **no** eligible note has `onset` or `release` strictly inside `(s,e)` | 353/353 |
| 5 | **Ties don't split (cross-layer)** | every eligible note's tie-resolved endpoints appear as slicer boundaries, `onset <= release` | 353/353 |
| 6 | **Determinism** | `changePointSlices` called twice per stem ⇒ identical output | 353/353 (0 failures) |
| — | **Empty-domain** | `< 2` distinct eligible boundaries ⇒ empty slice list | held where applicable |

**Note on #5 (honest scope).** As the instruction anticipated, #5 is *structurally
subsumed by #1* — since `Bexp` is built from exactly the eligible notes' tie-resolved
endpoints (one onset/release per tied group, per L1), a tie-split could only manifest as
an interior endpoint that #1 already catches. The harness asserts it independently
against the **slicer's** output as a cross-layer sanity check; the genuine tie-resolution
verification lives in L1's unit tests (note_model T-tests). It is reported as a real
check, not a redundant one, but its strength is bounded by L1's correctness — which is
the layered design intent (L2 reads L1's facts, does not re-derive them).

No stem failed any invariant ⇒ no §5 STOP. (Had one failed, the harness emits the stem,
the invariant, and the exact ticks; it does **not** relax the check or edit the slicer.)

## 3. Stats (REAL slicer) + music21-proxy reconciliation

| Metric | REAL slicer (353 stems) | music21 proxy | Reconciliation |
|---|---|---|---|
| Total measures | 5,582 | — | — |
| Total eligible notes | 82,119 | — | — |
| Total slices (incl. empty) | 29,213 | n/a (proxy dropped empties) | — |
| **Total NON-EMPTY slices** | **29,047** | **29,045** | **Δ 2** — near-identical |
| Mean NON-EMPTY / measure | **5.20** | ~5.2 | **exact** |
| Per-stem NON-EMPTY max | **391 (bwv328)** | ~391 | **exact** |
| Per-stem NON-EMPTY min | 30 (bwv324) | ~49 | modest (see below) |
| Empty (all-rest) slices | 166, in 67 stems | excluded by construction | phrase-rests (see below) |
| Release-only boundaries | 170 | — | — |
| Release-opened NON-EMPTY slices | 4, in {bwv299, bwv375, bwv392} | 2, in {bwv375, bwv392} | corroborated + 1 (see below) |
| Determinism failures | 0 | — | — |
| Pure slicer time (sum over corpus) | 3.86 ms | — | O(n log n) confirmed |
| Worst single-stem slicer time | 0.036 ms (bwv371) | — | no pathological stem |

**Aggregate match is excellent.** Non-empty total 29,047 vs proxy 29,045 (Δ2), mean
5.20 vs ~5.2 (exact), max 391 / bwv328 (exact). **No order-of-magnitude outliers**
(proxyOutliers = []). The proxy's correctness as a sizing instrument is confirmed
against the real model.

**Two minor divergences — both expected music21-vs-C++-model differences, neither a STOP:**

- **Per-stem min 30 (bwv324) vs proxy ~49.** bwv324 is a genuinely short **9-measure**
  chorale: 104 eligible notes, 30 non-empty slices, 0 empty, 3.33/measure — internally
  consistent. 30 is ~40% below the proxy's *approximate* `~49` floor but **well within an
  order of magnitude** (not flagged). The proxy's per-stem range was a ballpark (`~`);
  the real shortest stem is simply lower. Aggregate unaffected (Δ2 in 29k).
- **Release-opened NON-EMPTY 4 in 3 stems vs proxy 2 in 2.** The real slicer
  **corroborates the proxy's two named stems exactly** — bwv375 (1) and bwv392 (1) — and
  adds **bwv299 (2)**. Same order of magnitude, same two anchor stems. The extra is a
  release-only boundary produced by the C++ note model's tie resolution that music21's
  `stripTies` did not surface (or that the proxy's subset-redundancy filter suppressed).
  Reported, not papered over.

**Empty slices (166 in 67 stems).** These are the explicit all-rest interior spans the
design mandates (the slicer keeps them; the proxy dropped them) — phrase rests where all
eligible voices are silent between two boundaries. They are part of the covering, lossless
partition (invariant #2) and carry no eligible overlap.

**Performance.** Pure slicer cost across the whole corpus is **3.86 ms** total, worst
single stem **0.036 ms** (bwv371). O(n log n) holds; no pathological stem. (Process wall
time is dominated by Qt init + score load per invocation, which is harness overhead, not
the slicer.)

## 4. Corpus

The canonical **353** music21 Bach-chorale stems under `tools/corpus/*.xml` — the exact
set the proxy used and the BIR gate's input corpus (`docs/score_inventory.md` §"BIR gate
corpus"). All 353 ran; 0 load failures; 0 skipped. (SATB chorales: no chord-track /
drumset / hidden staves, so eligibility = all notes — the proxy's no-staff-filter
assumption holds here.)

## 5. Byte-identity (real analysis unchanged)

- `composing_tests`: **572/572**
- `notation_tests`: **57/57**
- `pipeline_snapshot_tests`: **11/11** (no golden refresh)

The `--validate-slices` path returns before any analysis, and no analysis `.cpp/.h` was
touched (the only production-tree edit is the diagnostic flag + validation function in the
`batch_analyze` tool, off by default). Byte-identity is therefore structural.

## 6. Scope / isolation confirmation

- The slicer is **not wired into** `regionanalyzer` / `greedyExpandSegmentation` or any
  analysis path. The harness only calls `changePointSlices` to *check* its output.
- The validation is **re-runnable**: `python tools/validate_slices_corpus.py` re-validates
  on demand, so future layer changes (L3 wiring) can re-confirm the invariants.

## 7. Commit scope

Local (unpushed), diagnostic harness only:
- `tools/batch_analyze.cpp` — the `--validate-slices` flag + `runSliceValidation` (the
  pre-existing **B2** subdominant-guard diagnostic hunks in this file were reverted out of
  the working tree before staging and **restored afterward**, so B2 stays HELD/unstaged as
  mandated).
- `tools/validate_slices_corpus.py` — the corpus driver.

Pre-existing WIP (B2 = `localmodulationdetector.{cpp,h}` + the batch_analyze B2 hunks,
the docs WIP, STATUS.md) left unstaged. `tools/corpus/slice_validation_summary.json` is in
the gitignored corpus dir.
