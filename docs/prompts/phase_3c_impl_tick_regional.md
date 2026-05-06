# Phase 3c-impl — Convert P3 + Close Divergence D + Migrate Temporal Extensions + Add Alternatives

**Scope:** Convert `analyzeNoteHarmonicContextRegionallyInWindow`
and `analyzeHarmonicContextRegionallyAtTick` to consume
`AnalyzedSection`. Delete P3's second `analyzeChord` call, the
tie-break prepend, and the per-tick `findTemporalContext` /
`collectRegionTones` re-invocation (closes divergence D — these
were confirmed cruft by the 3c recon at commit `d35f003aa2`).
Add `alternatives` field to `AnalyzedRegion` populated from the
per-region `analyzeChord`'s discarded candidate tail. Migrate the
5 temporal extension fields from `ChordTemporalContext` to
`AnalyzedRegion::temporalExtensions` and delete the 3 dead fields.

**Prior state:** Phase 3b landed at `ee8e2655bd`. Phase 3c-recon
landed at `d35f003aa2` with verdict (α) cruft. Implode and
annotation already consume `AnalyzedSection`. The per-region
`analyzeChord` produces up to 3 candidates and discards the tail
at `notationharmonicrhythmbridge.cpp:280`.

**Reference docs (read first):**
- `docs/divergence_d_recon.md` — verdict (α) cruft, the timeline
  evidence, and the critical nuance that `findTemporalContext` is
  NOT cruft (only the per-tick re-invocation is)
- `docs/policy2_coalescing_map.md` — divergence D definition
- `docs/unified_analysis_pipeline.md` — Phase 2 audit appendix
  (categories i and iii)

**Audit-derived field lists:**
- Migrate to `AnalyzedRegion::temporalExtensions`:
  `bassIsStepwiseFromPrevious`, `bassIsStepwiseToNext`,
  `previousRootPc`, `previousQuality`, `previousBassPc`.
- Delete (zero readers):
  `nextRootPc`, `nextBassPc`, `previousChordAge`.

---

## Pre-flight

1. `git status` and `git diff --stat` — trailing `\0` or mid-token
   truncation means a prior CC session was cut by usage limit;
   stop and surface.
2. Confirm on `master`, up-to-date with origin.
3. Force rebuild (`setup_and_build.bat`) and verify fresh binary
   timestamps.
4. Cache the snapshot baseline:
   `cp -r src/notation/tests/pipeline_snapshot_tests/snapshots /tmp/snapshots_p3c_baseline/`

---

## Critical preservation note

Recon established that `findTemporalContext` is NOT cruft. It's
called by the canonical per-region path
(`notationharmonicrhythmbridge.cpp:213-214`) to seed temporal
context, which is then evolved forward through analyzed regions.
**Do not delete `findTemporalContext`.** Phase 3c-impl deletes
only:
- The per-tick re-invocation of `findTemporalContext` from inside
  P3 (`notationcomposingbridge.cpp` around lines 327–354)
- The accompanying `collectRegionTones` re-invocation from the
  same site
- The second `analyzeChord` call at the same site
- The tie-break prepend (`notationcomposingbridge.cpp` around
  lines 372–375)

`findTemporalContext` and `collectRegionTones` themselves stay —
they have other call sites that the canonical path depends on.

---

## Work order

### Step A — Schema additions

**A.1 — Add `alternatives` to `AnalyzedRegion`.** In
`src/composing/analyzed_section.h`:

```cpp
struct AnalyzedRegion {
    // ... existing fields
    ChordAnalysisResult chordResult;          // existing — winner
    std::vector<ChordAnalysisResult> alternatives;  // new — [1..N] from per-region analyzeChord
    ChordTemporalExtensions temporalExtensions;     // new (defined below)
};
```

`alternatives` excludes position [0] (which is `chordResult`); it
holds positions [1..N-1] from the per-region `analyzeChord`'s
return. If `analyzeChord` returns only one candidate, `alternatives`
is empty.

**A.2 — Add `ChordTemporalExtensions` struct.** Same header:

```cpp
struct ChordTemporalExtensions {
    int previousRootPc = -1;
    int previousBassPc = -1;
    QString previousQuality;  // match existing ChordTemporalContext type
    bool bassIsStepwiseFromPrevious = false;
    bool bassIsStepwiseToNext = false;
};
```

Match field types to the existing `ChordTemporalContext` definitions
(if `previousQuality` is `std::string` rather than `QString`, match
that).

**A.3 — Populate both in `analyzeSection`.** Extend the
`HarmonicRegion → AnalyzedRegion` translation (in
`src/notation/internal/notationcomposingbridgehelpers.cpp`
alongside `prepareUserFacingHarmonicRegions`) to:
- Capture the full candidate vector from per-region `analyzeChord`
  by changing `notationharmonicrhythmbridge.cpp:280` (or wherever
  the discard happens) to keep the tail. The discard might be in
  the per-region invocation site or in `prepareUserFacingHarmonicRegions`'s
  consumption of the result — locate it.
- Translate the discarded tail into `AnalyzedRegion::alternatives`.
- Translate the existing `ChordTemporalContext` fields into
  `AnalyzedRegion::temporalExtensions`.

After this step, both `chordResult.alternatives` data and
`temporalExtensions` data exist on `AnalyzedRegion`. The old
`ChordTemporalContext` fields still exist too (deleted in Step C).

### Step B — Capture in snapshot, regenerate goldens

**B.1 — Extend `tickRegional` schema.** In
`src/notation/tests/pipeline_snapshot_tests/pipeline_snapshot_tests.cpp`,
add to each `tickRegional` entry:

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
  "previousBassPc": -1,

  "alternatives": [
    { "root": "Am", "quality": "minor", "score": 0.71 },
    { "root": "Em", "quality": "minor", "score": 0.42 }
  ]
}
```

**Source these fields from the CURRENT pre-refactor path** —
i.e., the cruft path's results. The 5 extension fields read from
`ChordTemporalContext`. The `alternatives` array reads from the
existing P3 `chordResults[1..N]` (the cruft's output, what
right-click menu and status bar consume today). This is what we
pin so the refactor's verification is meaningful.

The `alternatives` entry shape: `{root, quality, score}` minimum.
Add other fields if they're already on `ChordAnalysisResult` and
useful — e.g., `inversion`, `bass` — pick a small stable set that
captures the user-visible content without over-coupling.
`tickLocal` does not get `alternatives` (P4 returns a single result).

**B.2 — Regenerate.**
```
cmd.exe //c "C:\s\MS\setup_and_build.bat"
cd C:\s\MS\ninja_build_rel
./pipeline_snapshot_tests.exe --update-goldens
./pipeline_snapshot_tests.exe        # PASS after regen
```

Initial diff (without `--update-goldens`, before regenerating)
should show **only** new fields appearing in `tickRegional`
entries — no diffs to existing keys, no diffs in `implode`,
`annotation`, `tickLocal`, `implodedChordTrack`, `score`, or
`schemaVersion`. If anything else diffs, stop and surface.

Cache the post-regen baseline for Step D's diff target:
`cp -r src/notation/tests/pipeline_snapshot_tests/snapshots /tmp/snapshots_p3c_postcapture/`

### Step C — Refactor

**C.1 — Delete P3's cruft.** In
`src/notation/internal/notationcomposingbridge.cpp`:
- Delete the second `analyzeChord` call site (around lines
  327–354 per policy2_coalescing_map.md — verify line range).
- Delete the tie-break prepend (around lines 372–375).
- Delete the per-tick `findTemporalContext` and `collectRegionTones`
  invocations at the same site.

After deletion, P3's flow is: call `analyzeSection`, find the
region containing the requested tick, return a `NoteHarmonicContext`
populated from `region.chordResult` (position 0) and
`region.alternatives` (positions [1..N]) and
`region.temporalExtensions`.

**C.2 — Convert P3 entry points.** Refactor
`analyzeNoteHarmonicContextRegionallyInWindow` (line ~291) and
`analyzeHarmonicContextRegionallyAtTick` to consume
`AnalyzedSection`. Wrappers preserve current public signatures.

**C.3 — Migrate temporal-extension readers.** All 6 call sites
that currently read the 5 fields from `ChordTemporalContext`
(audit appendix in `docs/unified_analysis_pipeline.md` should have
locations) switch to reading from `region.temporalExtensions`.

**C.4 — Delete migrated fields from `ChordTemporalContext`.**
Remove `previousRootPc`, `previousBassPc`, `previousQuality`,
`bassIsStepwiseFromPrevious`, `bassIsStepwiseToNext`.

**C.5 — Delete dead fields from `ChordTemporalContext`.** Remove
`nextRootPc`, `nextBassPc`, `previousChordAge`. Audit confirmed
zero readers.

**C.6 — Update snapshot harness source.** Where Step B's harness
read extension fields from `ChordTemporalContext` and alternatives
from the cruft path's `chordResults[1..N]`, switch to reading from
`region.temporalExtensions` and `region.alternatives` respectively.
JSON output shape stays identical.

### Step D — Verify

```
cmd.exe //c "C:\s\MS\setup_and_build.bat"
cd C:\s\MS\ninja_build_rel
./pipeline_snapshot_tests.exe        # without --update-goldens
diff -q src/notation/tests/pipeline_snapshot_tests/snapshots /tmp/snapshots_p3c_postcapture/
./composing_tests.exe                 # 376/376, 0/135 mismatch
./notation_tests.exe                  # 53/53
```

**Expected verification outcome — partial diff in alternatives only.**
Per the recon's prediction, `tickRegional[].alternatives` content
may shift on a small subset of ticks because per-region-evolved
context produces different [1..N] candidates than the cruft's
per-tick `findTemporalContext` re-derivation produced. This is
documented unification, not regression — but it's the explicit
behavior change of this phase and requires inspection.

**No other field should diff.** Specifically:
- `implode`, `implodedChordTrack` — byte-identical (no change to
  per-region analysis path)
- `annotation` — byte-identical (same)
- `tickRegional[].{root,quality,key,wasRegional}` — byte-identical
  (`region.chordResult` unchanged)
- `tickRegional[].{bassIsStepwiseFromPrevious, bassIsStepwiseToNext, previousRootPc, previousQuality, previousBassPc}` — byte-identical
  (migrated values match Step B captured values)
- `tickLocal` — byte-identical (P4 untouched)

**If `diff -q` shows changes outside `tickRegional[].alternatives`:
stop, do not commit, do not regenerate.** That's an unexpected
behavior change and needs investigation.

**If `diff -q` shows changes only inside `tickRegional[].alternatives`:**
report a summary before committing:
- Total ticks where alternatives changed
- Number of scores affected
- 2–3 representative examples (which tick, what alternatives changed
  from, what they changed to)
- A subjective read: do the changes look like principled shifts
  (e.g., per-region context produces a more contextually-coherent
  ranking) or do any look suspicious (e.g., a high-confidence chord
  dropped from the alternatives entirely)?

**Halt and surface this summary.** Wait for user approval before
regenerating goldens and committing. Do not auto-accept the diffs.

After approval, regenerate `--update-goldens` once more to bake the
new alternatives values into the goldens, re-run snapshots to
verify PASS, then proceed to commit.

---

## Commit + push

Single commit, only after Step D passes (with user approval on the
alternatives diff). Suggested message:

```
Phase 3c: convert tick-regional, close divergence D, migrate temporal extensions

Splits analyzeNoteHarmonicContextRegionallyInWindow and
analyzeHarmonicContextRegionallyAtTick to consume AnalyzedSection.
Public signatures preserved as thin wrappers.

Deletes P3's second analyzeChord call, the per-tick
findTemporalContext / collectRegionTones re-invocation, and the
disagreement-case tie-break prepend (notationcomposingbridge.cpp
lines 327-354 and 372-375). Closes divergence D — tick-regional
now sources its result from the same per-region analysis as
implode/annotation, with no second-pass divergence in identity,
extensions, or alternatives.

Adds AnalyzedRegion::alternatives populated from the per-region
analyzeChord's previously-discarded candidate tail
(notationharmonicrhythmbridge.cpp:280). Right-click chord menu
and status bar continue to surface up to N candidates, now sourced
canonically.

Migrates 5 temporal-context fields from ChordTemporalContext to
AnalyzedRegion::temporalExtensions: bassIsStepwiseFromPrevious,
bassIsStepwiseToNext, previousRootPc, previousQuality,
previousBassPc. Deletes 3 dead fields per Phase 2 audit:
nextRootPc, nextBassPc, previousChordAge.

findTemporalContext and collectRegionTones themselves preserved
— canonical per-region path uses them for seeding (per
docs/divergence_d_recon.md).

Snapshot impact: implode, annotation, tickRegional primary fields
and extension fields all byte-identical. tickRegional alternatives
content shifted on N ticks across M scores — documented unification
(per-region-evolved context vs per-tick re-derivation), reviewed
and accepted.

policy2_coalescing_map.md: divergence D status now CLOSED.
Live divergences reduced from 2 to 1 (A — tick-local fallback
parallel pathway, by design).
```

Also update `docs/policy2_coalescing_map.md` to mark divergence D as
CLOSED with a one-line citation of the commit hash and the recon
report (analogous to how divergence B is documented).

**Push to origin at end of session.**

---

## Report back

- Commit hash + push confirmation
- Files touched count + rough LoC
- Step B initial-diff output (confirm: only new fields inside
  `tickRegional` entries, nothing else changed)
- Step D `diff -q` summary:
  - Confirmation that no field outside `tickRegional[].alternatives`
    diffed
  - Alternatives diff summary (ticks affected, scores affected,
    representative examples, subjective read)
  - User approval received before regenerating
- `composing_tests` result (expect 376/376, 0/135 mismatch)
- `notation_tests` result (expect 53/53)
- One-line summary of helpers updated to read from
  `region.temporalExtensions` (count + locations)
- Confirmation that lines 327–354 and 372–375 of
  `notationcomposingbridge.cpp` are gone (and what's there now)
- Confirmation that `findTemporalContext` and `collectRegionTones`
  themselves remain (with their other call sites untouched)
- `policy2_coalescing_map.md` divergence D update confirmation
- Any deviations and why
- Parked concerns for Phase 4

---

## Scope guardrails

- **Do not** delete `findTemporalContext` or `collectRegionTones`
  themselves — only the per-tick re-invocation from P3. Per the
  recon (`docs/divergence_d_recon.md`), the canonical path uses
  them.
- **Do not** rename `ChordTemporalContext`. Phase 4.
- **Do not** retire `HarmonicRegion` or
  `prepareUserFacingHarmonicRegions`. Phase 4.
- **Do not** convert `detectCadences` / `detectPivotChords`
  signatures. Continue with the 1:1 adapter pattern. Phase 4.
- **Do not** change P4 (tick-local) — divergence A stays open by
  design (parallel pathway per the wide/parallel scope decision).
- **Do not** change divergence C behavior. Bundled with
  cadence-aware-gate work for post-Phase-5.
- **Do not** touch implode (3a) or annotation (3b) emitters.
- **Do not** introduce analyzer-level reads of `Harmony` elements
  (per `project_chord_symbol_ban.md`).
- **Do not** consume `KeyArea` in any P3 code path —
  modulation-aware behavior is strictly Phase 5.
- If Step B initial diff shows changes outside `tickRegional` new
  fields: halt and surface.
- If Step D shows diffs outside `tickRegional[].alternatives`:
  halt and surface — that's an unexpected behavior change.
- If Step D shows alternatives diffs: halt, summarize, surface
  for user approval before regenerating. Do not auto-accept.
