# Phase 3b — Convert Annotation to Consume `AnalyzedSection` + Observe Divergence C

**Scope:** Split `addHarmonicAnnotationsToSelection` into analysis
(`analyzeSection()`) + a new emitter (`emitHarmonicAnnotations`).
Preserve current behavior exactly — including the
`minimumDisplayDurationBeats` gate (divergence C). Generate a
one-shot observation report enumerating sub-beat regions that
implode/tick-regional emit but annotation silently drops, so we can
decide divergence C resolution after looking at real data.

**Prior state:** Phase 3a landed at commit `7eafbab253`. `populateChordTrack`
is now a thin wrapper over `analyzeSection()` + `emitImplodedChordTrack`.
`sameUserFacingInference` and `collectStableKeyAnnotationCandidates`
already consume `AnalyzedRegion` directly. `detectCadences` /
`detectPivotChords` still take `vector<HarmonicRegion>` — keep the 1:1
adapter pattern; Phase 4 retires `HarmonicRegion`.

**Reference docs (read first):**
- `docs/unified_analysis_pipeline.md` — overall plan, Phase 2 audit
  appendix
- `docs/policy2_coalescing_map.md` — divergence C definition
- Phase 3a commit `7eafbab253` for the wrapper-pattern precedent

---

## Pre-flight

1. `git status` and `git diff --stat` — trailing `\0` or mid-token
   truncation means a prior CC session was cut by usage limit; stop
   and surface.
2. Confirm on `master`, up-to-date with origin.
3. Force rebuild (`setup_and_build.bat`) and verify fresh binary
   timestamps before running tests.
4. Cache the current snapshot baseline before any source change:
   `cp -r src/notation/tests/pipeline_snapshot_tests/snapshots /tmp/snapshots_p3b_baseline/`
   This is the byte-identity reference for Step C verification.

---

## Work order

The order matters. Do not reorder.

### Step A — Refactor: split `addHarmonicAnnotationsToSelection`

File: `src/notation/internal/notationcomposingbridge.cpp` (per Phase
1a recon, entry point at line 756). Header changes in
`notationcomposingbridge.h` if needed.

Introduce in the same `.cpp` file:

```cpp
struct EmitAnnotationOptions {
    Fraction minimumDisplayDurationBeats = Fraction(1, 2);  // current default
    // (other emitter-only knobs as they emerge from the current entry point)
};

void emitHarmonicAnnotations(Score* score,
                             const AnalyzedSection& section,
                             const EmitAnnotationOptions& options,
                             /* other current args */);
```

The emitter consumes `AnalyzedSection` and writes the same Harmony
elements as the current `addHarmonicAnnotationsToSelection`, with the
duration gate honored when `options.minimumDisplayDurationBeats > 0`.

Rewrite `addHarmonicAnnotationsToSelection` as a thin wrapper:

```cpp
void addHarmonicAnnotationsToSelection(/* current args */) {
    auto section = analyzeSection(score, from, to);
    EmitAnnotationOptions options;  // defaults reproduce current behavior
    emitHarmonicAnnotations(score, section, options, /* forwarded args */);
}
```

Do **not** change `addHarmonicAnnotationsToSelection`'s signature —
call sites stay untouched.

For cadence/pivot detection inside the emitter: continue with the
1:1 `vector<HarmonicRegion>` adapter pattern that `emitImplodedChordTrack`
established in Phase 3a. `detectCadences` / `detectPivotChords`
signature conversion is Phase 4.

If any helper in the current entry point is already on `AnalyzedRegion`
post-3a (e.g. `sameUserFacingInference`, `collectStableKeyAnnotationCandidates`),
prefer those direct types over re-translating.

### Step B — Verify annotation byte-identity

```
cmd.exe //c "C:\s\MS\setup_and_build.bat"
cd C:\s\MS\ninja_build_rel
./pipeline_snapshot_tests.exe        # must PASS without --update-goldens
```

Cross-check against the cached baseline:
```
diff -q src/notation/tests/pipeline_snapshot_tests/snapshots /tmp/snapshots_p3b_baseline/
```
Expected: zero output (every file matches exactly).

**If any diff appears, stop. Do not commit. Do not regenerate
goldens.** A diff means the refactor changed annotation behavior.
Surface the diff and halt.

```
./composing_tests.exe                 # 376/376, 0/135 mismatch
./notation_tests.exe                  # 53/53
```

### Step C — Generate divergence C observation report

Add a one-shot path in the snapshot harness behind a CLI flag
`--observe-divergence-c` (or a dedicated test that runs only when
the env var `PIPELINE_OBSERVE_DIVERGENCE_C=1` is set — pick whichever
is less invasive given the existing main).

For each of the 10 corpus scores:
1. Call `analyzeSection(score, from, to)` over the same range used
   for snapshots.
2. For each `AnalyzedRegion`, compute the duration in beats.
3. Identify the **delta set**: regions where
   `region.durationBeats() < 0.5` AND the region is currently emitted
   by implode (i.e., appears in the `implode` snapshot block) — these
   are exactly the regions implode/tick-regional surface but annotation
   silently drops.
4. For each delta-set region, capture: measure number, beat position
   within measure, duration in beats, would-be annotation text
   (call `emitHarmonicAnnotations` against a synthetic
   `EmitAnnotationOptions{ minimumDisplayDurationBeats = Fraction(0,1) }`
   on just that region and read back what it would write — or compute
   the text the same way the emitter does, whichever is cleaner).

Write the report to `docs/divergence_c_observation.md`. Suggested
shape:

```markdown
# Divergence C — Observation Report

Generated from Phase 3b snapshot corpus (10 scores).
Per-score enumeration of sub-beat (< 0.5 beat) regions that
implode/tick-regional surface but annotation silently drops via
`minimumDisplayDurationBeats` gate.

## Summary

| Score | Total regions | Sub-beat regions | Delta set (gated by P2) |
|---|---:|---:|---:|
| bach_chorale_001 | 32 | 4 | 4 |
| ... | ... | ... | ... |

## Per-score detail

### bach_chorale_001

| Measure | Beat | Duration (beats) | Would-be text |
|---|---|---:|---|
| 7 | 2.5 | 0.25 | Cmaj |
| ... |
```

Run with the flag once to generate the report. Commit the report
alongside the source changes. Do **not** make this a CI-gated check;
it's a snapshot of corpus state at this commit, not a regression
target.

### Step D — Final test run

```
./pipeline_snapshot_tests.exe        # PASS (no --update-goldens)
./composing_tests.exe                 # 376/376
./notation_tests.exe                  # 53/53
diff -q src/notation/tests/pipeline_snapshot_tests/snapshots /tmp/snapshots_p3b_baseline/
                                      # zero output
```

---

## Commit + push

Single commit. Suggested message:

```
Phase 3b: convert annotation to consume AnalyzedSection

Splits addHarmonicAnnotationsToSelection into analyzeSection() +
new emitHarmonicAnnotations(AnalyzedSection, EmitAnnotationOptions).
addHarmonicAnnotationsToSelection remains as a thin wrapper passing
default options that reproduce current behavior, including the 0.5-beat
display duration gate (divergence C).

Generates docs/divergence_c_observation.md enumerating sub-beat regions
that implode/tick-regional surface but annotation silently drops, so
divergence C resolution can be decided from real corpus data.

Cadence/pivot detection still consumes vector<HarmonicRegion> via
1:1 adapter — Phase 4 retires HarmonicRegion entirely.

Zero behavior change verified by snapshot byte-identity.
```

**Push to origin at end of session.**

---

## Report back

- Commit hash + push confirmation
- Files touched count + rough LoC
- Step B verification: `diff -q` cached baseline output (expect empty)
- Step D verification: same `diff -q` (expect empty)
- `composing_tests` result (expect 376/376, 0/135 mismatch)
- `notation_tests` result (expect 53/53)
- Observation report summary: total delta-set count across all
  10 scores, the 3 scores with the highest sub-beat density, one
  representative example of a sub-beat region from the report
- Any helpers that were pulled forward to consume `AnalyzedRegion`
  during the conversion (analogous to 3a's `sameUserFacingInference`
  pull-forward)
- Any deviations and why
- Parked concerns for Phase 3c

---

## Scope guardrails

- **Do not** touch implode (already converted) or tick-regional /
  tick-local paths. Phase 3c.
- **Do not** touch any analysis logic:
  `prepareUserFacingHarmonicRegions`, `analyzeSection`'s delegate
  body, Pass 0–4, `analyzeChord`, `detectCadences`, `detectPivotChords`,
  etc. Adapter pattern only.
- **Do not** change `addHarmonicAnnotationsToSelection`'s signature
  or remove its callers' indirection — keep it as a wrapper.
- **Do not** touch divergence D (P3 re-analysis) — Phase 3c.
- **Do not** consume `KeyArea` in `emitHarmonicAnnotations` —
  modulation-aware annotation is strictly Phase 5. The data is
  available via `AnalyzedSection.keyAreas`; ignore it for now.
- **Do not** introduce analyzer-level reads of `Harmony` elements
  (per `project_chord_symbol_ban.md`).
- **Do not** migrate `ChordTemporalContext` fields to
  `AnalyzedRegion` (audit category iii) — Phase 3c.
- **Do not** change divergence C behavior. The gate stays at 0.5
  beats for `addHarmonicAnnotationsToSelection`. The observation
  report is read-only diagnostic; resolution is a separate decision.
- If Step B or Step D shows any diff: stop and surface. Do not
  regenerate goldens to paper over the diff.
