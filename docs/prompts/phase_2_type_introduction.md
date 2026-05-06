# Phase 2 — Type Introduction + ChordTemporalContext Audit

**Scope:** Introduce the unified-pipeline analysis types
(`AnalyzedRegion`, `KeyArea`, `AnalyzedSection`) and a working
`analyzeSection()` entry point that delegates to the existing
`prepareUserFacingHarmonicRegions`. No caller consumes the new types
yet — Phase 3a/3b/3c wires them in per path. Also: audit
`ChordTemporalContext` and expose P4 in the bridge header so
`tickLocal` snapshots get real data.

**Prior state:** Phase 1b landed at commit `efb60ca1ab` — snapshot
harness pins P1/P2/P3 output for 10 scores. Refactor plan lives at
`docs/unified_analysis_pipeline.md`.

**Reference docs (read first):**
- `docs/unified_analysis_pipeline.md` — overall plan and phase map;
  struct sketches live there
- `docs/policy2_coalescing_map.md` — the passes that feed into the
  new types
- `ARCHITECTURE.md` §5.13 — single-path model

---

## Pre-flight

1. `git status` and `git diff --stat` — trailing `\0` or mid-token
   truncation means a prior CC session was cut by usage limit; stop
   and surface.
2. Confirm on `master`, up-to-date with origin.
3. Force rebuild (`setup_and_build.bat`) and verify fresh binary
   timestamps before running tests.

---

## Deliverables

### 1. New types in composing module

File: `src/composing/analyzed_section.h` (new).

Define three structs. Take final shapes from
`docs/unified_analysis_pipeline.md` where it sketches them; refine
below as needed.

**`AnalyzedRegion`** — one harmonic region in the score. Fields
should cover what all three regional emitters (P1 implode, P2
annotation, P3 tick-regional) need from a region: tick range, root PC
/ quality / inversion, key / mode, `hasAssertiveExposure`, per-region
chord-result payload. Do NOT include emitter-specific fields (voicing
preferences, notes-vs-whole-rest choices, text-format preferences).
If a field's only consumer is an emitter, it stays on emitter side.

**`KeyArea`** — a contiguous tick span sharing a key/mode. Fields:
tick range, key, mode, confidence. Modulation boundary is implied by
adjacent `KeyArea` entries having different key/mode.

**`AnalyzedSection`** — the return type of `analyzeSection()`. Holds
`std::vector<AnalyzedRegion> regions` and
`std::vector<KeyArea> keyAreas` covering the same tick span. May
also hold a `Fraction startTick` and `Fraction endTick` for the
analyzed window.

Include appropriate `#include`s and use composing-module conventions
(look at neighboring composing headers for style — `chordanalyzer.h`,
`keymodeanalyzer.h`).

### 2. `analyzeSection()` entry point

File: `src/notation/internal/notationcomposingbridgehelpers.cpp`
(alongside `prepareUserFacingHarmonicRegions`).

Header declaration: add to
`src/notation/internal/notationcomposingbridgehelpers.h`.

Signature:
```cpp
AnalyzedSection analyzeSection(Score* score, const Fraction& from, const Fraction& to);
```

Implementation: call `prepareUserFacingHarmonicRegions` with the
existing args, then translate each resulting `HarmonicRegion` into an
`AnalyzedRegion`. Derive `KeyArea` entries by walking the
`AnalyzedRegion` list and collapsing adjacent regions with the same
`key` + `mode` into a single `KeyArea` span.

The function must be pure translation — no behavior change, no new
analyzer calls. No caller is wired up to it in this phase.

**Why this file, not `src/composing/`:** The delegate target
`prepareUserFacingHarmonicRegions` is currently in the bridge layer.
Phase 4 retires that function and moves `analyzeSection` to
composing/. Living here now keeps the dependency direction correct.
Add a one-line comment above the function noting the planned Phase 4
migration.

### 3. Expose P4 in bridge header

File: `src/notation/internal/notationcomposingbridge.cpp`

Move `analyzeHarmonicContextLocallyAtTick` out of the anonymous
namespace. Add its declaration to
`src/notation/internal/notationcomposingbridge.h`. No behavior
change — just visibility.

### 4. Update snapshot harness to populate `tickLocal`

File: `src/notation/tests/pipeline_snapshot_tests/pipeline_snapshot_tests.cpp`

Where the harness currently writes an empty `tickLocal` array, call
`analyzeHarmonicContextLocallyAtTick` at the same sample ticks used
for `tickRegional` and serialize `{tick, root, quality, key}` per
tick (schema already documented in Phase 1b prompt).

Run `--update-goldens` and regenerate the 10 snapshot files.
Expected JSON diff: `"tickLocal"` arrays go from `[]` to populated.
No other fields should change. If other fields change, stop and
surface — that would mean something non-obvious shifted.

Update `src/notation/tests/pipeline_snapshot_tests/corpus/README.md`
to remove the `tickLocal` placeholder caveat.

### 5. `ChordTemporalContext` audit

Audit `src/composing/chordanalyzer.h` (and wherever
`ChordTemporalContext` is defined) for:

**(i) Dead fields.** Fields written but never read, or whose reads
were deleted in the Jazz-path retirement chain (commits `02e3733afb`
and `69716deead`). Precedent: `jazzMode` was exactly this — set in
`analyzeScoreJazz` but never read by any scoring logic. Same pattern
may still exist.

**(ii) Emitter-leaked fields.** Fields whose only consumer is an
emitter layer (implode chord-track writer, annotation text writer,
status-bar formatter). These should eventually move to the emitter
side — flag them but do not move them in Phase 2.

**(iii) Migration candidates for `AnalyzedRegion`.** Fields that
belong conceptually to a region's analysis result and are consumed
by multiple emitters. These will migrate in Phase 3+.

Do **not** delete, move, or rename anything in this phase. Output is
a new section in `docs/unified_analysis_pipeline.md` titled
"ChordTemporalContext audit (Phase 2)" with three subsections
matching the three categories above. Each finding should cite file
path + line number and name the concrete field.

---

## Build + test loop

```
cmd.exe //c "C:\s\MS\setup_and_build.bat"
cd C:\s\MS\ninja_build_rel
./pipeline_snapshot_tests.exe --update-goldens
./pipeline_snapshot_tests.exe        # must pass
./composing_tests.exe                 # must still be 0/135 mismatch, 376/376
./notation_tests.exe                  # must still pass 53/53
```

Expected outcome:
- New header + function compile; no callers of `analyzeSection` yet,
  so linking is trivial.
- P4 exposure is pure visibility — zero runtime behavior change.
- Snapshot goldens regenerate with only `tickLocal` diffs. Verify
  this by running the binary once WITHOUT `--update-goldens` first
  (it should fail with diffs only in `tickLocal` fields), then
  regenerate, then re-run to confirm PASS. Include the initial diff
  in your report.
- `composing_tests` and `notation_tests` unchanged.

---

## Commit + push

Single commit. Suggested message:

```
Phase 2: introduce AnalyzedRegion/KeyArea/AnalyzedSection types

Adds src/composing/analyzed_section.h with the shared analysis types
that will front-load the unified pipeline. analyzeSection() delegates
to prepareUserFacingHarmonicRegions for now; Phase 4 retires the
delegate and moves analyzeSection to composing/.

Exposes analyzeHarmonicContextLocallyAtTick via the bridge header so
pipeline_snapshot_tests can pin P4 tick-local output. Regenerates 10
goldens — tickLocal arrays are now populated; no other diffs.

Audits ChordTemporalContext for dead fields, emitter leakage, and
AnalyzedRegion migration candidates; findings in
docs/unified_analysis_pipeline.md.

Zero behavior change; no callers consume the new types yet.
```

**Push to origin at end of session.**

---

## Report back

- Commit hash + push confirmation
- Files touched count + rough LoC
- Initial diff output from running snapshots without `--update-goldens`
  (confirm: tickLocal-only diffs)
- Post-regeneration PASS confirmation
- `composing_tests` result (expect 376/376, 0/135 mismatch)
- `notation_tests` result (expect 53/53)
- Summary of the ChordTemporalContext audit: counts in each category,
  most surprising finding
- Any deviations and why
- Parked concerns for Phase 3

---

## Scope guardrails

- **Do not** modify any analysis logic:
  `prepareUserFacingHarmonicRegions`, Pass 0–4 implementations,
  `analyzeChord`, `resolveKeyAndMode`, cadence detection, etc.
- **Do not** modify any emitter: `populateChordTrack`,
  `addHarmonicAnnotationsToSelection`, status-bar formatting.
- **Do not** delete or move any field during the audit — report only.
- **Do not** introduce analyzer-level reads of `Harmony` elements
  anywhere (per `project_chord_symbol_ban.md`).
- If audit uncovers a tempting refactor, note it in the audit
  appendix and leave the code alone — Phase 3+ territory.
- `AnalyzedRegion` / `KeyArea` / `AnalyzedSection` must contain zero
  emitter-specific fields. If unsure whether a field is
  emitter-specific, leave it off the new struct and add a note in the
  audit section.
