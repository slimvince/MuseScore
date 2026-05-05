# Phase 3c — Convert P3 (Tick-Regional) + Close Divergence D + Migrate Temporal Extensions

**Scope:** Convert `analyzeNoteHarmonicContextRegionallyInWindow` and
`analyzeHarmonicContextRegionallyAtTick` to consume `AnalyzedSection`.
Delete P3's second `analyzeChord` call (closes divergence D). Migrate
the 5 temporal extension fields from `ChordTemporalContext` to
`AnalyzedRegion::temporalExtensions` and delete the 3 dead fields
identified in Phase 2's audit. Capture extension fields in snapshots
before the migration to pin field-value preservation byte-exactly.

**Prior state:** Phase 3b landed at commit `ee8e2655bd`. Implode
and annotation now consume `AnalyzedSection` via `analyzeSection()`.
Phase 2 audit established zero emitter-leaked fields on
`ChordTemporalContext` — the 5 migration candidates and 3 dead fields
are the residual structural work.

**Reference docs (read first):**
- `docs/unified_analysis_pipeline.md` — overall plan, Phase 2 audit
  appendix (categories i and iii)
- `docs/policy2_coalescing_map.md` — divergence D definition,
  tie-break rule (lines 372–375 of `notationcomposingbridge.cpp`)
- Phase 3a commit `7eafbab253` for wrapper-pattern precedent
- Phase 3b commit `ee8e2655bd` for the cached-baseline diff workflow

**Audit reference (the 5 migration candidates and 3 dead fields):**
- Migrate to `AnalyzedRegion::temporalExtensions`:
  `bassIsStepwiseFromPrevious`, `bassIsStepwiseToNext`,
  `previousRootPc`, `previousQuality`, `previousBassPc`.
- Delete (never read anywhere):
  `nextRootPc`, `nextBassPc`, `previousChordAge`.

---

## Pre-flight

1. `git status` and `git diff --stat` — trailing `\0` or mid-token
   truncation means a prior CC session was cut by usage limit; stop
   and surface.
2. Confirm on `master`, up-to-date with origin.
3. Force rebuild (`setup_and_build.bat`) and verify fresh binary
   timestamps before running tests.
4. Cache the current snapshot baseline:
   `cp -r src/notation/tests/pipeline_snapshot_tests/snapshots /tmp/snapshots_p3c_baseline/`

---

## Step 0 — Recon: `chordResults[1+]` consumers

Before touching code, grep for consumers of P3's multi-element
`chordResults` array. The second `analyzeChord` call currently
appends a display-context result, so the disagreement case returns
a 2-element array. Phase 3c reduces this to 1 element. If anyone
reads `chordResults[1]` (or relies on `chordResults.size() > 1`),
we need to know before deleting.

Patterns to grep for across the whole repo:
- `chordResults[1]`
- `chordResults\.size\(\) > 1`
- `chordResults\.size\(\) >= 2`
- `chordResults\.at\(1\)`
- `chordResults\.front\(\)` and `chordResults\.back\(\)` (the
  back/front asymmetry can leak the multi-element assumption)
- Iteration patterns over `chordResults` that don't break after
  the first element

Also inspect the call sites of `analyzeNoteHarmonicContextRegionallyInWindow`
and `analyzeHarmonicContextRegionallyAtTick` and any of their
upstream wrappers (`analyzeNoteHarmonicContext`,
`analyzeNoteHarmonicContextDetails`, `analyzeHarmonicContextAtTick`)
to see if any caller treats the multi-element shape as significant.

**Surface findings before proceeding.** Report shape:
- List of grep hits (file:line + a one-line description)
- Per hit: assessment of whether it depends on the disagreement-case
  multi-element shape or if it's safe (e.g., a `front()` call on a
  result you control)
- One-line recommendation: proceed / pause-for-guidance

If clean: proceed to Step A. If a real consumer exists: halt and
surface for direction; do not refactor unilaterally.

---

## Step A — Capture temporal extension fields in `tickRegional` snapshot

File: `src/notation/tests/pipeline_snapshot_tests/pipeline_snapshot_tests.cpp`

Extend each `tickRegional` entry to include the 5 migration-candidate
fields, sourced from the current `ChordTemporalContext` location
(pre-migration). Schema:

```json
{
  "tick": 0,
  "root": "C",
  "quality": "major",
  "key": "C",
  "wasRegional": true,
  "bassIsStepwiseFromPrevious": false,
  "bassIsStepwiseToNext": true,
  "previousRootPc": -1,
  "previousQuality": "",
  "previousBassPc": -1
}
```

Use `-1` for `previousRootPc` / `previousBassPc` when no previous
region exists. Use empty string for `previousQuality` when no
previous region exists. Whatever sentinels the existing struct uses
internally — match those so the JSON faithfully reflects current
state.

`tickLocal` entries do **not** get these fields (Phase 2 audit was
on `ChordTemporalContext`, which is regional-path territory; P4's
shape is unchanged). If `tickLocal` entries naturally have stepwise
context too via a different mechanism, leave them alone for now —
audit candidates were specific to the regional path.

---

## Step B — Regenerate goldens with current values

```
cmd.exe //c "C:\s\MS\setup_and_build.bat"
cd C:\s\MS\ninja_build_rel
./pipeline_snapshot_tests.exe --update-goldens
./pipeline_snapshot_tests.exe        # PASS (re-read after regen)
```

Initial diff (without `--update-goldens`, before regenerating)
should show **only** the new fields appearing inside `tickRegional`
entries — no diffs to existing keys, no diffs to `implode`,
`annotation`, `tickLocal`, `implodedChordTrack`, `score`, or
`schemaVersion`. If anything else diffs, stop and surface.

After regeneration, all 10 snapshots have populated extension
fields reflecting current pre-migration values. **This is the
baseline that the migration must preserve byte-exact.**

Cache the post-regen baseline for Step D:
`cp -r src/notation/tests/pipeline_snapshot_tests/snapshots /tmp/snapshots_p3c_postcapture/`

---

## Step C — Refactor: migrate fields, delete second analyzeChord, convert P3

This step does three things together. They're coupled because the
field migration changes where the snapshot reads from, and the
second-`analyzeChord` deletion is what unblocks P3 consuming
`AnalyzedSection` directly.

**C.1 — `ChordTemporalExtensions` struct.** Define on `AnalyzedRegion`:

```cpp
// In src/composing/analyzed_section.h
struct ChordTemporalExtensions {
    int previousRootPc = -1;
    int previousBassPc = -1;
    QString previousQuality;
    bool bassIsStepwiseFromPrevious = false;
    bool bassIsStepwiseToNext = false;
};

struct AnalyzedRegion {
    // ... existing fields
    ChordTemporalExtensions temporalExtensions;
};
```

Field types should match the existing `ChordTemporalContext` types
(check the source — if `previousQuality` is `std::string` rather
than `QString`, match that).

**C.2 — Populate `temporalExtensions` in `analyzeSection`.** The
delegate body already translates each `HarmonicRegion` into an
`AnalyzedRegion`. Extend the translation to also populate
`temporalExtensions` from the corresponding `ChordTemporalContext`
fields. After this step, the values exist on both the old struct
(pre-migration) and the new struct — the next step removes them
from the old struct.

**C.3 — Delete migrated fields from `ChordTemporalContext`.** Remove
`previousRootPc`, `previousBassPc`, `previousQuality`,
`bassIsStepwiseFromPrevious`, `bassIsStepwiseToNext` from the
struct definition. Update all 6 call sites that currently compute
or read `bassIsStepwiseFromPrevious` (audit appendix in
`docs/unified_analysis_pipeline.md` should have the locations) to
read from `region.temporalExtensions.bassIsStepwiseFromPrevious`
instead. Same for the other 4 fields.

**C.4 — Delete dead fields from `ChordTemporalContext`.** Remove
`nextRootPc`, `nextBassPc`, `previousChordAge`. Audit confirmed
zero readers; deletion is mechanical.

**C.5 — Convert P3 to consume `AnalyzedSection`.** In
`src/notation/internal/notationcomposingbridge.cpp`, refactor
`analyzeNoteHarmonicContextRegionallyInWindow` (line 291 per Phase
1a recon) and `analyzeHarmonicContextRegionallyAtTick` to:

1. Call `analyzeSection(score, from, to)` once.
2. For the requested tick, find the `AnalyzedRegion` containing it
   and return a `NoteHarmonicContext` populated from
   `region.chordResult` and `region.temporalExtensions`.
3. **Do not** call `analyzeChord` a second time. Do not run
   `collectRegionTones` + `findTemporalContext` + `analyzeChord`
   for display re-analysis. The current lines 327–354 (display
   re-analysis) and 372–375 (tie-break prepend) get deleted.

If P3's existing entry points have other call sites that aren't
the regional functions (e.g., `addAnalyzedHarmonyToSelection` chain
documented in policy2_coalescing_map.md), thread the
`AnalyzedSection` through analogously. Wrappers preserve current
public signatures.

**C.6 — Update snapshot harness to read from new location.** Where
Step A sourced extension fields from `ChordTemporalContext`, switch
to reading from `region.temporalExtensions`. The JSON output shape
stays identical (same field names, same value types). Same patterns
for `-1` / empty-string sentinels.

---

## Step D — Verify byte-identity

```
cmd.exe //c "C:\s\MS\setup_and_build.bat"
cd C:\s\MS\ninja_build_rel
./pipeline_snapshot_tests.exe        # PASS without --update-goldens
diff -q src/notation/tests/pipeline_snapshot_tests/snapshots /tmp/snapshots_p3c_postcapture/
                                      # zero output
./composing_tests.exe                 # 376/376, 0/135 mismatch
./notation_tests.exe                  # 53/53
```

`pipeline_snapshot_tests` must PASS without `--update-goldens`. The
`diff -q` against the post-capture baseline must be empty. Any
diff means the migration changed values.

**If any diff appears in Step D, stop. Do not commit. Do not
regenerate goldens.** The whole point of Step B was to fix the
baseline so D can prove the migration preserves it. A diff means
the new computation path produces different values than the old
path — that's a behavior change in disguise, not a clean migration.

---

## Commit + push

Single commit, only after Step D passes. Suggested message:

```
Phase 3c: convert tick-regional, close divergence D, migrate temporal extensions

Splits analyzeNoteHarmonicContextRegionallyInWindow and
analyzeHarmonicContextRegionallyAtTick to consume AnalyzedSection.
Public signatures preserved as thin wrappers.

Deletes P3's second analyzeChord call (display re-analysis at
notationcomposingbridge.cpp:327-354) and the disagreement-case
tie-break prepend (lines 372-375). Closes divergence D —
tick-regional now sources its result from the same per-region
analysis as implode/annotation, with no second-pass divergence in
temporal-context extension fields.

Migrates 5 temporal-context fields from ChordTemporalContext to
AnalyzedRegion::temporalExtensions: bassIsStepwiseFromPrevious,
bassIsStepwiseToNext, previousRootPc, previousQuality,
previousBassPc. Deletes 3 dead fields per Phase 2 audit:
nextRootPc, nextBassPc, previousChordAge (zero readers confirmed).

Snapshot tickRegional entries gain the 5 migrated fields, captured
pre-migration and verified byte-identical post-migration.

policy2_coalescing_map.md: divergence D status updates to CLOSED;
remaining live divergences reduced from 2 to 1 (A — tick-local
fallback parallel pathway).
```

Also update `docs/policy2_coalescing_map.md` to mark divergence D as
CLOSED with a one-line citation of the commit hash (analogous to
how divergence B is documented).

**Push to origin at end of session.**

---

## Report back

- Step 0 recon findings: grep results, per-hit assessment,
  proceed/pause recommendation, and what you actually did
- Commit hash + push confirmation
- Files touched count + rough LoC
- Step B initial-diff output (confirm: only new fields inside
  `tickRegional` entries, nothing else changed)
- Step D verification: `diff -q` against post-capture baseline
  (expect empty)
- `composing_tests` result (expect 376/376, 0/135 mismatch)
- `notation_tests` result (expect 53/53)
- One-line summary of helpers updated to read from
  `region.temporalExtensions` (count + locations)
- Confirmation that lines 327–354 and 372–375 of
  `notationcomposingbridge.cpp` are gone (and what's there now)
- `policy2_coalescing_map.md` divergence D update confirmation
- Any deviations and why
- Parked concerns for Phase 4

---

## Scope guardrails

- **Do not** rename `ChordTemporalContext`. Audit flagged but it's
  Phase 4 territory (renames pair with `HarmonicRegion` retirement).
- **Do not** retire `HarmonicRegion` or `prepareUserFacingHarmonicRegions`.
  Phase 4.
- **Do not** convert `detectCadences` / `detectPivotChords` signatures.
  Continue with the 1:1 adapter pattern. Phase 4.
- **Do not** change P4 (tick-local) — divergence A stays open by
  design (parallel pathway per the wide/parallel scope decision).
- **Do not** change divergence C behavior. The duration-gate
  decision is bundled with cadence-aware-gate work for post-Phase-5.
- **Do not** touch implode (3a) or annotation (3b) emitters.
- **Do not** introduce analyzer-level reads of `Harmony` elements
  (per `project_chord_symbol_ban.md`).
- **Do not** consume `KeyArea` in any P3 code path —
  modulation-aware behavior is strictly Phase 5.
- If Step 0 surfaces a real `chordResults[1+]` consumer: halt and
  surface, do not refactor unilaterally.
- If Step B initial diff shows changes outside `tickRegional` new
  fields: halt and surface.
- If Step D shows any diff: halt and surface, do not regenerate
  goldens to paper over.
