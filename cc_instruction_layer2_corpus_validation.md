# CC Instruction — LAYER 2: corpus property-validation of the REAL slicer

> Layer 2's slicer is unit-tested on 13 fixtures + 100% branch-covered, but it has **never run on the real
> corpus** — the audit's slice sizing was a **music21 proxy** (`C:\tmp\l2_slice_probe.py`), NOT the C++
> `changePointSlices`. This closes that gap: run the **actual** slicer over **all 353 canonical stems** and prove
> the §6 oracle invariants hold on every one, with an **independent** oracle (not the slicer's own internal logic).
> This is what makes Layer 2 *validated*, not merely *covered*, before we open L3.
>
> **★ Boundaries (read first):** this is **validation only**. The slicer stays **isolated** — do NOT wire it into
> the analysis pipeline (`regionanalyzer`/`greedyExpandSegmentation`); the validation harness only *calls* it to
> *check* its output, it does not feed slices into analysis. **The real analysis output must stay byte-identical**
> (composing/notation/snapshots/BIR/oracle unchanged). If validating requires changing analysis behavior → STOP.
>
> **★ No-assume:** report the actual measured numbers; if any stem fails an invariant, that is a real slicer or
> note-model bug — **STOP and surface the stem + the violation**, do not paper over it or "fix" it by relaxing the
> check.

## §1 — The harness (reuse the corpus loader; diagnostic, not production)
The corpus is MusicXML and the gtest binary cannot import MusicXML (the fixture-conversion constraint). Use the
C++ path that already loads the corpus: add a **diagnostic subcommand/flag** to `batch_analyze` (e.g.
`--validate-slices`) — or a small standalone tool reusing the same engraving importer — that, for each score:
1. loads it, 2. `NoteModel::build(score)`, 3. `changePointSlices(model)`, 4. runs the §2 checks, 5. accumulates
stats. It must **not** invoke or alter the analysis pipeline, must **not** be on any default code path, and must
**not** change analysis output. (Confirm at source which existing flag pattern to mirror — e.g. the existing
diagnostic `--section-level` flag — so this stays a pure diagnostic.)

## §2 — The invariants, checked against an INDEPENDENT oracle (not the slicer's internals)
For each stem, compute the **expected** boundary set independently from `model.notes()` — do NOT reuse the
slicer's own boundary vector — then assert the slicer agrees:
- **Independent oracle:** `Bexp = sorted-unique { n.onset, n.release : n in model.notes() where n.plays &&
  n.visible && n.staffEligible }`. Expected slices = consecutive pairs of `Bexp` over `[min(Bexp), max(Bexp))`.
- **Assert, per stem:**
  1. **Boundary-set match:** the set of all slice start/end ticks from `changePointSlices` == `Bexp` (this single
     equality is completeness + no-spurious + no-missed at once).
  2. **Covering, no gaps/overlaps:** `slices[i].end == slices[i+1].start` for all i; `front().start == min(Bexp)`;
     `back().end == max(Bexp)`.
  3. **Positive width:** every slice has `start < end`.
  4. **Constant tonal sonority (independent recompute):** for each slice `[s,e)`, no eligible note has `onset` in
     `(s,e)` or `release` in `(s,e)` — i.e. the eligible overlap set is constant within the slice.
  5. **Ties don't split (spot, inherited from L1):** confirm no slice boundary falls strictly inside a tie-resolved
     note's span for an eligible note (subsumed by #1 if L1 is correct; assert anyway as a cross-layer check).
  6. **Determinism:** `changePointSlices(model)` called twice yields identical output (run on a sample or all).
- A stem with **no eligible notes** (if any exists) → expect an **empty** slice list (Bexp has < 2 ticks); assert
  that, don't crash.

## §3 — Stats + reconciliation against the music21 proxy
Report aggregate stats from the REAL slicer and compare to the proxy (sanity, not exact — music21 ≠ the C++ model):
- **Slice density:** total slices, mean slices/measure, per-stem min/max. Proxy ballpark to compare against: mean
  **~5.2/measure**, per-stem range **~49–391**. Flag any stem **materially** outside that envelope for inspection
  (an order-of-magnitude outlier is a red flag; a few-percent drift is expected proxy/model difference).
- **Empty slices:** count of empty (all-rest) interior slices; how many stems have any. (Cross-check the design's
  expectation that these are phrase-rests.)
- **Release-only boundaries:** count of interior boundaries that are a release with no coincident onset, and how
  many open a non-empty slice. The proxy found exactly **2** non-empty release-opened slices (`bwv375`, `bwv392`)
  in 29,045 — report whether the REAL slicer corroborates (same order; name the stems). A large divergence here is
  worth surfacing (proxy vs real semantics).
- **Performance:** total wall-time over the corpus and worst single-stem time (the slicer is O(n log n) — confirm
  no pathological stem).

## §4 — Corpus
Use the **canonical 353-stem set** the proxy used (the Bach chorales + corelli under `tools/corpus/`). Read
`docs/score_inventory.md` first for the authoritative corpus location and the do-not-touch list; use the same
identity set as the gate (CLAUDE.md). State exactly which stems were run and the count (must be the full 353).

## §5 — Gate
- **ALL 353 stems pass every §2 invariant.** Any single failure → STOP, report the stem + which invariant + the
  exact ticks; do not relax the check or edit the slicer without surfacing first (a real bug is the valuable
  outcome here).
- **Analysis byte-identity preserved:** `composing_tests` / `notation_tests` / pipeline snapshots unchanged; the
  diagnostic is off by default and does not touch analysis. If any analysis metric moves → STOP.
- The validation is **re-runnable** (a committed diagnostic, not a one-off), so future layer changes can re-validate.

## §6 — Deliver
Commit **locally (unpushed)** — the diagnostic harness (test/diagnostic-only, no analysis change) + nothing else;
leave all pre-existing WIP unstaged. Write `cc_layer2_corpus_validation_report.md`: the harness mechanism, the
353/353 invariant pass result (or the failing stems), the slice-density / empty-slice / release-only / performance
stats with the proxy reconciliation, and the byte-identity confirmation. Cowork verifies the harness uses an
independent oracle and is diagnostic-only; user ratifies; then push + L3.

## §7 — Stop conditions
- Any stem fails an invariant → STOP, surface (do not auto-fix or relax).
- Validating would require wiring the slicer into analysis or changing analysis output → STOP (it must stay
  isolated; byte-identity holds).
- The harness can't load the corpus via an existing C++ importer path without a production change → STOP and
  surface the options (don't hack the analysis pipeline).
- Real slice counts diverge from the proxy by an order of magnitude on many stems → STOP and surface (the proxy or
  the slicer has a semantic gap worth understanding before L3).
