# Phase 5a — KeyArea Empirical Observation + Confidence Gate

**Scope:** Add `keyAreas` capture to the pipeline snapshot harness
(behavior-neutral additive field). Implement the confidence-gated
KeyArea derivation in `analyzeSection` per
`docs/unified_analysis_pipeline.md:149–163`. Snapshot the post-gate
KeyArea spans across the 10-corpus scores. The post-gate snapshot
is the empirical observation deliverable — it gives us the first
real view of how key-area boundaries fall on actual music, so the
Phase 5b annotation emitter can be designed against evidence not
guesswork.

**Prior state:** Phase 4b landed at commit `36368d67cc`.
`analyzeSection` is canonical. KeyArea derivation currently uses
the simpler "open new area on any key change" algorithm — Phase 4b
preserved this from Phase 2 (the unified-pipeline doc explicitly
flagged it as initial sketch for Phase 5 to refine). Phase 5 recon
landed at commit `8cfc4a1542` (recon doc at
`docs/phase5_recon.md`).

**Reference docs (read first, in this order):**
- `docs/phase5_recon.md` — full recon report. Q1: engraving is
  text-only and `→` format already used by `detectPivotChords`.
  Q2: DCML labels usable as comparison metadata for future tuning
  (NOT in scope for 5a). Q3: `NoteHarmonicContext` slot-in for 5b.
  **Q4: missing confidence gate** — the algorithm fix this
  session implements.
- `docs/unified_analysis_pipeline.md` — overall plan. Lines
  149–163 specify the confidence-gated KeyArea algorithm. This is
  the spec being implemented.
- `src/composing/analyzed_section.h` — `AnalyzedRegion` (with
  `keyAreaId`), `KeyArea` definitions
- Phase 4b commit `36368d67cc` — current state of `analyzeSection`
  and the KeyArea derivation block at the end of its body

---

## Pre-flight

1. `git status` and `git diff --stat` — trailing `\0` or mid-token
   truncation means a prior CC session was cut by usage limit;
   stop and surface.
2. Confirm on `master`, up-to-date with origin (or use the
   appropriate worktree if mainline is busy).
3. Force rebuild (`cmd.exe //c "C:\s\MS\setup_and_build.bat"`)
   and verify fresh binary timestamps before running tests.
   (Build dir is `ninja_build_rel/`, not `ninja_build/`.)
4. Cache the pre-Phase-5a snapshot baseline:
   `cp -r src/notation/tests/pipeline_snapshot_tests/snapshots /tmp/snapshots_p5a_baseline/`

---

## Critical principles (preserve through this work)

- **Analyzer outputs are maximal and exact.** Confidence gate
  affects KeyArea grouping (which region belongs to which area),
  not per-region chord identity or key analysis. Each region's
  own `keyModeResult` is preserved verbatim regardless of which
  area it's grouped into.
- **No analytical content as input.** The chord-symbol-ban
  generalizes to all user-written analytical content (chord
  symbols, Romans, function annotations, cadence labels, key
  annotations) regardless of storage type. Analyzer reads notes
  + structural metadata (key signature, time sig, ties, pedal)
  only. See `project_chord_symbol_ban` memory for the full
  framing.
- **DCML key labels are NOT in scope for 5a.** They are
  comparison metadata for future tuning sessions, not analyzer
  input now or ever. The 5a confidence gate uses the analyzer's
  own per-region `normalizedConfidence`, not external labels.
- **`findTemporalContext` and `collectRegionTones` survive.** Per
  `docs/divergence_d_recon.md`, the canonical seeding pattern
  uses these and they are not cruft.

---

## Work order

### Step A — Cache pre-gate KeyArea snapshot (observation baseline)

Add `keyAreas` JSON array to each per-score snapshot in
`pipeline_snapshot_tests.cpp`. Schema per entry:

```json
"keyAreas": [
  {
    "startTick": 0,
    "endTick": 1920,
    "keyFifths": 0,
    "mode": "Ionian",
    "confidence": 0.876
  }
]
```

Source values from the existing `AnalyzedSection.keyAreas` produced
by `analyzeSection`. Do NOT modify `analyzeSection` in this step —
we want the pre-gate algorithm's output captured first.

Run `--update-goldens` to bake the pre-gate `keyAreas` into the
snapshots. Verify all 10 snapshots regenerate cleanly. Cache this
state for diffing later:
`cp -r src/notation/tests/pipeline_snapshot_tests/snapshots /tmp/snapshots_p5a_pregate/`

Initial diff check: re-run snapshots without `--update-goldens`
should pass byte-exact against the just-regenerated goldens (same
data round-trips). Run also against the pre-Phase-5a baseline:
```
diff -q src/notation/tests/pipeline_snapshot_tests/snapshots /tmp/snapshots_p5a_baseline/
```
Should show ONLY new `keyAreas` keys appearing — no diffs in
`implode`, `annotation`, `tickRegional`, `tickLocal`,
`implodedChordTrack`, `score`, `schemaVersion`, or any other
existing field. If anything else diffs, halt and surface.

### Step B — Implement the confidence-gated KeyArea derivation

Locate the KeyArea derivation block at the end of `analyzeSection`
in `src/notation/internal/notationcomposingbridgehelpers.cpp`
(per recon Q4, looks roughly like):

```cpp
if (out.keyAreas.empty()
    || out.keyAreas.back().keyFifths != regionFifths
    || out.keyAreas.back().mode != regionMode) {
    // open new KeyArea
} else {
    // extend existing KeyArea; confidence = max of merged regions
}
```

Replace with the confidence-gated algorithm per
`docs/unified_analysis_pipeline.md:149–163`. The change in plain
terms: a new `KeyArea` opens only when a divergent region's
`normalizedConfidence` clears the assertive-confidence threshold
(0.8). Regions that disagree with the enclosing area but fall
below threshold are assigned to the enclosing area via
`keyAreaId` while their own `keyModeResult` stays unchanged.

Use the existing assertive-confidence constant
(`kAnnotateKeyConfidenceThreshold` or the equivalent — recon Q5
notes 0.8 has standing across `hasAssertiveKeyConfidence`,
`kAnnotateKeyConfidenceThreshold`, and cadence/pivot detection).
Don't introduce a new constant.

### Step C — Regenerate post-gate goldens

```
cmd.exe //c "C:\s\MS\setup_and_build.bat"
cd C:\s\MS\ninja_build_rel
./pipeline_snapshot_tests.exe --update-goldens
./pipeline_snapshot_tests.exe        # PASS after regen
```

The new goldens reflect the post-gate KeyArea spans. Cache for
diff inspection:
`cp -r src/notation/tests/pipeline_snapshot_tests/snapshots /tmp/snapshots_p5a_postgate/`

### Step D — Inspect the diff and surface findings

```
diff -r /tmp/snapshots_p5a_pregate/ /tmp/snapshots_p5a_postgate/
```

**Expected diff scope:** Only `keyAreas` arrays should change.
No diffs in `implode`, `annotation`, `tickRegional`, `tickLocal`,
`implodedChordTrack`, or per-region chord/key fields.
**The confidence gate affects only KeyArea grouping, not
per-region chord identity or key analysis** — if anything else
diffs, halt and surface.

If only `keyAreas` diffs (as expected), characterize the diff:
- How many scores show different `keyAreas` content?
- For modulating scores (Chopin Op.30 No.2, Mozart K.279 / K.280,
  possibly Corelli Op.1 No.8): do the post-gate spans look more
  principled than the pre-gate spans? Specifically, do tonicizations
  with sub-threshold confidence get absorbed into the enclosing
  area (good) or do they still open new spans (might indicate
  threshold needs adjustment)?
- For Bach corpus + Schumann Kinderszenen (largely non-modulating):
  do they show fewer `keyAreas` (one stable area each, ideally),
  or are spurious areas from per-region key noise still appearing?

### Step E — Halt for review

Surface the Step D diff summary BEFORE committing. Include:
- Count of scores with diffs
- For each modulating score: pre-gate vs post-gate `keyAreas`
  count, and a one-line read on whether the post-gate result
  looks improved
- Any spans that look surprising (e.g., a stable area that
  unexpectedly fragmented, or a known modulation that didn't get
  detected)
- Subjective assessment: does the gate appear well-calibrated at
  0.8, or does the empirical data suggest the threshold needs
  adjustment?

**Wait for user approval before committing the post-gate state.**
This is the empirical observation deliverable — Vincent reviews
and confirms the data looks sensible before we lock it in as the
new baseline.

If the post-gate spans look badly miscalibrated (e.g., the
threshold is too strict and real modulations aren't detected,
or too lenient and non-modulations open spans), halt with the
findings. Don't try to "fix" by adjusting the threshold
unilaterally — the threshold is a deliberate constant
(`kAnnotateKeyConfidenceThreshold` = 0.8) used elsewhere; tuning
it is a Phase 5c question if needed.

### Step F — Commit + push (after approval)

Single commit. Suggested message skeleton:

```
Phase 5a: KeyArea empirical observation + confidence gate

Adds keyAreas JSON capture to pipeline_snapshot_tests so the
analyzer's per-corpus KeyArea spans become observable across the
10-score harness. Schema: per-area startTick, endTick, keyFifths,
mode, confidence.

Implements the confidence-gated KeyArea derivation in
analyzeSection per docs/unified_analysis_pipeline.md:149-163. A
new KeyArea opens only when a divergent region's normalizedConfidence
clears the assertive-confidence threshold (kAnnotateKeyConfidenceThreshold
= 0.8). Regions below threshold are assigned to the enclosing area
via keyAreaId while retaining their own keyModeResult — chord
identity and per-region key analysis are unchanged.

Snapshot impact: keyAreas arrays gain content (additive), and
some keyAreas spans shifted vs. pre-gate baseline (the gate
absorbing low-confidence transient tonicizations into enclosing
areas). [Fill in concrete numbers from Step D summary.] Per-region
chord results, annotation, implode, tickRegional, and tickLocal
are byte-identical to pre-Phase-5a baseline.

composing_tests 376/376, mismatch baseline preserved (0/135 + 135/135).
notation_tests 53/53. pipeline_snapshot_tests 10/10.

Sets up Phase 5b — modulation-aware annotation emitter — to
consume KeyArea data from a known-good empirical baseline.
```

**Push to origin at end of session.**

---

## Report back

- Commit hash + push confirmation
- Files touched count + rough LoC
- Step A initial-diff output (confirm: only new `keyAreas` keys
  appearing in pre-Phase-5a baseline diff)
- Step D diff summary (pre-gate vs post-gate):
  - Per-score: pre-gate `keyAreas` count vs post-gate count
  - Modulating scores: subjective read on whether spans look more
    principled
  - Non-modulating scores: confirmation that they have a single
    stable area (or explanation if not)
  - Any surprising spans worth flagging
- User-approval received before commit
- `composing_tests` result (expect 376/376, 0/135 + 135/135)
- `notation_tests` result (expect 53/53)
- `pipeline_snapshot_tests` result (expect 10/10)
- Confirmation that no diffs appeared outside `keyAreas` arrays
- Any deviations and why
- Parked concerns for Phase 5b

---

## Scope guardrails

- **Do not** touch `NoteHarmonicContext` — adding `enclosingKeyArea`
  is Phase 5b.
- **Do not** touch `harmonicAnnotation` formatter or
  `emitHarmonicAnnotations` emitter — Phase 5b.
- **Do not** touch `detectPivotChords` (already produces `→` format
  pivot labels per recon Q1 — Phase 5b will extend the pattern).
- **Do not** introduce DCML label reading anywhere. DCML labels
  are comparison metadata for future tuning sessions, not analyzer
  input now or ever. The 5a confidence gate uses the analyzer's
  own per-region `normalizedConfidence`, not external labels.
- **Do not** delete `findTemporalContext` or `collectRegionTones`
  themselves — per `docs/divergence_d_recon.md`, the canonical
  path uses them.
- **Do not** introduce analyzer-level reads of `Harmony` elements
  or any other user-written analytical content (Roman numeral
  text annotations, key annotations, etc.) — content-based check
  per the generalized `project_chord_symbol_ban` memory, not
  storage-type-based.
- **Do not** retire `prepareUserFacingHarmonicRegions` shim — it
  preserves `batch_analyze.cpp` compatibility.
- **Do not** change P4 (tick-local fallback) — divergence A stays
  open by design.
- **Do not** change divergence C behavior. Bundled with
  cadence-aware-gate work for post-Phase-5.
- **Do not** introduce a new confidence threshold constant — use
  the existing `kAnnotateKeyConfidenceThreshold` (or equivalent)
  at 0.8.
- **Do not** unilaterally adjust the threshold if the post-gate
  data looks miscalibrated. Surface findings; threshold tuning
  is a separate decision.
- **Do not** auto-accept the post-gate diff — Step E halts for
  user review of the empirical observation deliverable.
- If Step A initial diff shows changes outside the new `keyAreas`
  field: halt and surface — that's an unexpected behavior change.
- If Step D diff shows changes outside `keyAreas` arrays: halt
  and surface — confidence gate should not affect per-region
  chord results.
