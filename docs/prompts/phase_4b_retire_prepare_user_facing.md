# Phase 4b — Retire `prepareUserFacingHarmonicRegions`, Inline Passes 0–4 into `analyzeSection`

**Scope:** Make `analyzeSection` the canonical implementation. Inline
Passes 0–4 (currently inside `prepareUserFacingHarmonicRegions`)
into `analyzeSection`'s body, operating on `AnalyzedRegion`
natively. Make `prepareUserFacingHarmonicRegions` a thin
deprecated shim that calls `analyzeSection` and translates back to
`vector<HarmonicRegion>` for `tools/batch_analyze.cpp`'s
classical-path consumers (per the Phase 4 recon's batch_analyze
finding). Port `pipeline_snapshot_tests.cpp` from
`prepareUserFacingHarmonicRegions` to `analyzeSection` directly.
Convert the `normalizePopulatedRegionStarts` test helper. Resolve
`ChordTemporalContext` per the recon's Q1 verdict.

Snapshot byte-identity required throughout. composing_tests baseline
preserved (376/376, 0/135 + 135/135). notation_tests preserved (53/53).

**Prior state:**
- Phase 3c-impl landed at `9f515d6372`
- Phase 4 recon landed at `640cfe165d` with verdict: 2-session split
  (4a + 4b), shim approach for batch_analyze, 4c (analyzeSection
  move to composing) deferred indefinitely
- Phase 4a landed at `1eba307edd` — `detectCadences` /
  `detectPivotChords` now consume `vector<AnalyzedRegion>`; emitter
  adapters dropped

**Reference docs (read first, in this order):**
- `docs/phase4_recon.md` — full recon report. Q1 contains the
  `ChordTemporalContext` fate verdict you must follow. Q2 lists
  every `HarmonicRegion` consumer you'll need to handle. Q3
  characterizes Pass 0–4 dependency depth and conversion verdicts
  per pass. Read carefully.
- `docs/divergence_d_recon.md` — **critical preservation note**:
  `findTemporalContext` is NOT cruft. The canonical seeding
  pattern (call `findTemporalContext` once, then evolve "previous"
  forward through analyzed regions) must move into
  `analyzeSection`'s body when `prepareUserFacingHarmonicRegions`
  retires. The helper itself stays. Currently called at
  `src/notation/internal/notationharmonicrhythmbridge.cpp:213-214`.
- `docs/unified_analysis_pipeline.md` — overall plan, refactor
  arc, Phase 2 audit appendix
- `docs/policy2_coalescing_map.md` — Pass 0–4 description and
  helper inventory inside `prepareUserFacingHarmonicRegions`
  (line 1575 of `notationcomposingbridgehelpers.cpp` per the
  policy2 doc)
- `src/composing/analyzed_section.h` — `AnalyzedRegion` definition
  post-3c (chordResult, alternatives, temporalExtensions, etc.)

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
4. Cache the snapshot baseline:
   `cp -r src/notation/tests/pipeline_snapshot_tests/snapshots /tmp/snapshots_p4b_baseline/`

---

## Critical preservation note

`findTemporalContext` and `collectRegionTones` (and any other
helper functions called by Passes 0–4 or by the canonical
seeding pattern) **stay alive**. They have legitimate non-cruft
call sites that this phase preserves. The retirement target is
`prepareUserFacingHarmonicRegions` itself — the function that
orchestrates Passes 0–4. The passes' helper functions move with
the passes (or stay where they are if not pass-internal); they do
not get deleted.

If the recon Q3's per-pass verdicts surface any helper that
should be deleted, follow the recon's verdict. If it doesn't
explicitly mark a helper for deletion, preserve it.

---

## Work order

### Step A — Inline Passes 0–4 into `analyzeSection`

`analyzeSection` currently lives in `mu::notation::internal`
namespace inside `notationcomposingbridgehelpers.cpp` (per Phase 2
deviation). It currently delegates to
`prepareUserFacingHarmonicRegions` and translates the
`vector<HarmonicRegion>` output to `AnalyzedSection`.

Replace the delegation with the inlined pass logic:

1. Pass 0 — boundary detection (delegates to
   `analyzeHarmonicRhythm` / `Smoothed`; pull the call into
   `analyzeSection`).
2. Pass 1 — gap-tone region insertion (`inferGapRegion`,
   `regionSupportsGapTones`, `inferSparseGapChord`,
   `analyzeGapWithContext`, `applyGapKeyContext`). Per recon Q3,
   convert these to operate on `AnalyzedRegion` if marked
   "mechanical" or "real-refactor"; halt-and-surface if marked
   "blocked."
3. Pass 2 — within-measure same-chord merge
   (`appendMeasureRegion`).
4. Pass 3 — measure-opening carry.
5. Pass 4 — key/mode stabilization
   (`stabilizeHarmonicRegionsForDisplay`).

The seeding pattern described in `docs/divergence_d_recon.md`
must move into `analyzeSection`'s body: call
`findTemporalContext` once at the start of region analysis, then
evolve "previous" forward through analyzed regions. Do NOT
re-derive temporal context per-region from scratch.

After Step A, `analyzeSection` produces `AnalyzedSection` directly
without going through `vector<HarmonicRegion>` internally.
`prepareUserFacingHarmonicRegions` is left in place but unused by
`analyzeSection`.

### Step B — Convert `prepareUserFacingHarmonicRegions` to a shim

Replace `prepareUserFacingHarmonicRegions`'s body with a thin
shim:

```cpp
std::vector<HarmonicRegion> prepareUserFacingHarmonicRegions(/* current args */) {
    auto section = analyzeSection(/* same args */);
    return translateToHarmonicRegions(section);  // helper that does the reverse mapping
}
```

The helper `translateToHarmonicRegions(const AnalyzedSection&)`
takes an `AnalyzedSection` and produces a `vector<HarmonicRegion>`
that batch_analyze and any other legacy consumer expects. Field
mapping should mirror what `analyzeSection`'s old
`HarmonicRegion → AnalyzedRegion` translation did, in reverse.

Add a doc comment on `prepareUserFacingHarmonicRegions`
declaration:

```cpp
// DEPRECATED: shim retained for tools/batch_analyze.cpp compatibility.
// Production callers consume analyzeSection() directly. See Phase 4
// recon (docs/phase4_recon.md) for the rationale; future tools-port
// removes this and HarmonicRegion entirely.
```

No `[[deprecated]]` compile-time attribute — it would fire on
batch_analyze's legitimate usage and pollute the build.

### Step C — Port `pipeline_snapshot_tests.cpp` to `analyzeSection`

The snapshot harness currently calls
`prepareUserFacingHarmonicRegions` (to populate the `implode`
snapshot key per Phase 1b's deviation). Switch the harness to
call `analyzeSection` directly and consume `AnalyzedSection`. The
JSON output shape must remain identical; only the source function
changes.

### Step D — Convert `normalizePopulatedRegionStarts` test helper

`notationimplode_tests.cpp` has a helper called
`normalizePopulatedRegionStarts` that uses `HarmonicRegion`
internally (surfaced during Phase 4a's grep sweep). Convert it to
consume `AnalyzedRegion`. Same pattern as the
`notationannotate_tests.cpp` retype done in 4a.

If the helper has consumers that pass `HarmonicRegion` instances
directly (constructed in test setup), retype those too. Grep for
remaining `HarmonicRegion(` and `vector<HarmonicRegion>` in test
directories to confirm clean.

### Step E — Resolve `ChordTemporalContext` per recon Q1 verdict

Read the recon's Q1 verdict in `docs/phase4_recon.md`. Three
possible verdicts:

- **(a) Delete the struct entirely** — all remaining fields move
  to `AnalyzedRegion` or get inlined at call sites.
- **(b) Rename and keep** — the struct stays, gets a more
  appropriate name; update all references.
- **(c) Flatten into `AnalyzedRegion`** — fields merge into
  `AnalyzedRegion` directly; struct deleted.

Execute exactly what the verdict recommends. If the verdict's
mechanics are unclear or seem to require a sub-decision the recon
didn't make, halt and surface.

If verdict is (b) rename: pick the name the recon recommended, or
if it didn't specify, propose one and surface for approval before
committing the rename.

### Step F — Verify byte-identity

```
cmd.exe //c "C:\s\MS\setup_and_build.bat"
cd C:\s\MS\ninja_build_rel
./pipeline_snapshot_tests.exe        # PASS without --update-goldens
diff -q src/notation/tests/pipeline_snapshot_tests/snapshots /tmp/snapshots_p4b_baseline/
                                      # zero output
./composing_tests.exe                 # 376/376, baseline 0/135 + 135/135
./notation_tests.exe                  # 53/53
```

`pipeline_snapshot_tests` must PASS without `--update-goldens`.
The `diff -q` against the cached baseline must be empty. Any diff
means the inlined Pass 0–4 logic produces different values than
the original — a behavior change in disguise, not a clean
retirement.

**If any diff appears in Step F: stop. Do not commit. Do not
regenerate goldens.** Investigate the diff before proceeding. The
most likely causes:
- A pass's logic doesn't quite preserve behavior under the type
  swap (look at the per-pass conversion sites)
- The seeding-pattern migration introduced a subtle change in how
  the temporal context evolves
- A field on `AnalyzedRegion` doesn't fully replace what
  `HarmonicRegion` exposed

Surface the diff; do not paper over.

---

## Commit + push

Single commit, only after Step F passes. Suggested message
skeleton (CC fills in specifics):

```
Phase 4b: retire prepareUserFacingHarmonicRegions, inline Passes 0-4 into analyzeSection

Makes analyzeSection the canonical implementation. Pass 0 (Jaccard
boundary detection), Pass 1 (gap-tone region insertion), Pass 2
(same-chord merge), Pass 3 (measure-opening carry), and Pass 4
(key/mode stabilization) now run inside analyzeSection's body,
operating on AnalyzedRegion natively. The seeding pattern
(findTemporalContext called once, "previous" evolved forward)
moves with the passes per docs/divergence_d_recon.md.

prepareUserFacingHarmonicRegions becomes a thin deprecated shim
that calls analyzeSection and translates AnalyzedSection back to
vector<HarmonicRegion> for tools/batch_analyze.cpp's
classical-path consumers (per Phase 4 recon's batch_analyze
finding). HarmonicRegion type persists as the shim's return type;
future tools-port deletes both.

Ports pipeline_snapshot_tests.cpp from prepareUserFacingHarmonicRegions
to analyzeSection. Converts notationimplode_tests.cpp's
normalizePopulatedRegionStarts helper to AnalyzedRegion. Resolves
ChordTemporalContext per recon Q1 verdict ([delete / rename /
flatten] — fill in actual outcome).

findTemporalContext, collectRegionTones, and other Pass 0-4
helpers preserved per critical-preservation note in the prompt
and divergence_d_recon.md.

Snapshot byte-identity verified across all 10 corpus scores.
composing_tests 376/376 + notation_tests 53/53 + mismatch
baseline 0/135 + 135/135 preserved.
```

**Push to origin at end of session.**

---

## Report back

- Commit hash + push confirmation
- Files touched count + rough LoC (expect significant additions to
  `analyzeSection`'s body offset by deletions in
  `prepareUserFacingHarmonicRegions` body and Pass-0-4 helper
  call sites)
- Step F verification: confirm `diff -q` empty against cached
  baseline
- `composing_tests` result (expect 376/376, 0/135 + 135/135)
- `notation_tests` result (expect 53/53)
- `pipeline_snapshot_tests` result (expect 10/10)
- Per-pass conversion summary: brief line per Pass (0–4) noting
  any conversion subtleties or notable choices
- The `ChordTemporalContext` fate executed (verdict (a)/(b)/(c)
  with one-line summary of what happened)
- `prepareUserFacingHarmonicRegions` shim verification:
  - Confirm the shim exists with the deprecated doc comment
  - Confirm `tools/batch_analyze.cpp` still builds (the shim
    preserved its consumer interface)
- Confirmation that `findTemporalContext` and `collectRegionTones`
  themselves remain (with their other call sites untouched)
- Any deviations and why
- Parked concerns for Phase 5 / future tools-port

---

## Scope guardrails

- **Do not** touch `tools/batch_analyze.cpp`. Per the standing
  "stay out of batch_analyze" scope decision; the shim preserves
  its compat without source changes.
- **Do not** delete `findTemporalContext` or `collectRegionTones`
  themselves (or any Pass 0–4 helper not explicitly marked for
  deletion in the recon Q3 verdict). Per
  `docs/divergence_d_recon.md`'s critical preservation note.
- **Do not** delete `HarmonicRegion` the type — it remains as the
  shim's return type.
- **Do not** move `analyzeSection` to the `mu::composing`
  namespace / `src/composing/`. The recon Q4 verdict deferred this
  indefinitely (composing_analysis is `NO_QT` with no engraving
  link by design; the move requires interface redesign). Phase 4c
  is the future home for that work, gated on a concrete consumer
  need.
- **Do not** introduce `KeyArea` consumption in Pass 0–4 logic or
  in cadence/pivot detection. Phase 5.
- **Do not** introduce analyzer-level reads of `Harmony` elements
  (per `docs/symbol_input_audit.md`).
- **Do not** change P4 (tick-local fallback) — divergence A stays
  open by design (parallel pathway per the wide/parallel scope
  decision).
- **Do not** change divergence C behavior. Bundled with
  cadence-aware-gate work for post-Phase-5.
- **Do not** add `[[deprecated]]` compile attributes to the shim.
  Doc comment only — compile attribute would pollute the
  batch_analyze build.
- If Step F shows any diff: halt and surface, do not regenerate
  goldens to paper over.
- If recon Q1 verdict is unclear or recon Q3 marked any pass as
  "blocked": halt and surface before proceeding.
