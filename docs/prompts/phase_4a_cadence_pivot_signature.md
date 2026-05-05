# Phase 4a — Convert detectCadences / detectPivotChords Signatures

**Scope:** Convert `detectCadences` and `detectPivotChords` from
consuming `vector<HarmonicRegion>` to `vector<AnalyzedRegion>`. Drop
the two 1:1 `HarmonicRegion` adapters that Phase 3a and 3b
accumulated inside the emitters. Retype the affected test fixtures.
Pure type substitution + adapter removal — no logic change. Snapshot
byte-identity required throughout.

**Prior state:** Phase 3c-impl landed at commit `9f515d6372`. Phase 4
recon landed at commit `640cfe165d` and recommended a 2-session split
(4a + 4b). This is 4a — the low-risk mechanical chunk that builds
confidence and unblocks 4b.

**Reference docs (read first):**
- `docs/phase4_recon.md` — full recon report, includes file/line
  cites for `detectCadences`, `detectPivotChords`, and the two
  adapter sites in the emitters
- `docs/unified_analysis_pipeline.md` — overall plan and Phase 4
  scope
- `src/composing/analyzed_section.h` — `AnalyzedRegion` definition
  (post-3c, includes `chordResult`, `alternatives`, `temporalExtensions`)
- Phase 3a commit `7eafbab253` and Phase 3b commit `ee8e2655bd` —
  the adapter pattern these emitters use; 4a deletes that pattern

---

## Pre-flight

1. `git status` and `git diff --stat` — trailing `\0` or mid-token
   truncation means a prior CC session was cut by usage limit;
   stop and surface.
2. Confirm on `master`, up-to-date with origin (or use the
   appropriate worktree if mainline is busy).
3. Force rebuild (`cmd.exe //c "C:\s\MS\setup_and_build.bat"`) and
   verify fresh binary timestamps before running tests. (Build dir
   is `ninja_build_rel/`, not `ninja_build/` — CLAUDE.md is stale
   on this point.)
4. Cache the snapshot baseline:
   `cp -r src/notation/tests/pipeline_snapshot_tests/snapshots /tmp/snapshots_p4a_baseline/`

---

## Work order

### Step A — Convert `detectCadences`

Locate `detectCadences` (per recon, in `src/composing/` — confirm
exact location via grep). Change parameter type from
`vector<HarmonicRegion>` to `vector<AnalyzedRegion>` (or `const std::vector<AnalyzedRegion>&` —
match existing const/ref conventions of the surrounding signatures).

Update internal logic to use `AnalyzedRegion` fields. Per the
Phase 2 audit and Phase 3c migration, the fields detectCadences
needs (chord identity, key, temporal extensions, etc.) all exist on
`AnalyzedRegion`. If anything is missing, stop and surface — that's
a recon gap that needs investigation before proceeding.

Header declaration must move with the signature change. Find the
declaration (likely in a paired `.h` file) and update.

### Step B — Convert `detectPivotChords`

Same pattern as Step A. Locate, change parameter type, update
internal logic, update header declaration.

### Step C — Drop the 1:1 adapters

Two adapter sites accumulated in Phase 3a and 3b:
- `emitImplodedChordTrack` (per Phase 3a deviation notes,
  `notationimplodebridge.cpp`) — materializes a
  `vector<HarmonicRegion>` to call `detectCadences`
- `emitHarmonicAnnotations` (per Phase 3b deviation notes,
  `notationcomposingbridge.cpp`) — same pattern

In each emitter:
- Delete the adapter materialization code (the loop that builds the
  `vector<HarmonicRegion>` from the `AnalyzedSection`'s regions).
- Pass the `AnalyzedRegion` vector directly to `detectCadences` /
  `detectPivotChords`. The emitters already have access via
  `section.regions` (or whatever the field is named on `AnalyzedSection`).

### Step D — Retype test fixtures

Per recon: `notationannotate_tests.cpp` has fixtures constructed
as `HarmonicRegion` directly. Retype them to `AnalyzedRegion`.
Update any field-access patterns if they used bridge-specific
helpers.

If recon missed any other test files that construct
`HarmonicRegion` directly, find and convert them too. Grep for
`HarmonicRegion(` and `vector<HarmonicRegion>` across test
directories.

### Step E — Verify byte-identity

```
cmd.exe //c "C:\s\MS\setup_and_build.bat"
cd C:\s\MS\ninja_build_rel
./pipeline_snapshot_tests.exe        # PASS without --update-goldens
diff -q src/notation/tests/pipeline_snapshot_tests/snapshots /tmp/snapshots_p4a_baseline/
                                      # zero output
./composing_tests.exe                 # 376/376, baseline 0/135 + 135/135
./notation_tests.exe                  # 53/53
```

`pipeline_snapshot_tests` must PASS without `--update-goldens`.
The `diff -q` against the cached baseline must be empty. Any diff
means the type substitution changed runtime behavior — that's a
behavior change in disguise, not a clean conversion.

**If any diff appears in Step E: stop. Do not commit. Do not
regenerate goldens.** A diff means the new logic path produces
different values than the old path — investigate before proceeding.

---

## Commit + push

Single commit, only after Step E passes. Suggested message:

```
Phase 4a: convert detectCadences/detectPivotChords to AnalyzedRegion

Changes detectCadences and detectPivotChords parameter types from
vector<HarmonicRegion> to vector<AnalyzedRegion>. Drops the 1:1
HarmonicRegion materialization adapters that Phase 3a and 3b
accumulated inside emitImplodedChordTrack and emitHarmonicAnnotations.
Retypes notationannotate_tests.cpp fixtures.

Pure type substitution + adapter removal. No logic change. Snapshot
byte-identity verified across all 10 corpus scores. composing_tests
376/376 + notation_tests 53/53 + mismatch baseline 0/135 + 135/135
preserved.

Unblocks Phase 4b (retire prepareUserFacingHarmonicRegions and
HarmonicRegion the type — though batch_analyze.cpp shim work means
HarmonicRegion may persist as tool-compat layer).
```

**Push to origin at end of session.**

---

## Report back

- Commit hash + push confirmation
- Files touched count + rough LoC
- Step E verification: confirm `diff -q` empty against cached
  baseline
- `composing_tests` result (expect 376/376, 0/135 + 135/135)
- `notation_tests` result (expect 53/53)
- Confirmation that the two adapter sites (in emitImplodedChordTrack
  and emitHarmonicAnnotations) are gone (and what's there now)
- Any other test files that needed `HarmonicRegion` retyping
  beyond `notationannotate_tests.cpp` (if recon missed any)
- Any deviations and why
- Parked concerns for 4b

---

## Scope guardrails

- **Do not** modify analysis logic inside `detectCadences` or
  `detectPivotChords`. Only change the parameter type and any
  internal field accesses required by the type change. The cadence
  and pivot algorithms themselves stay byte-identical.
- **Do not** touch `prepareUserFacingHarmonicRegions` or any of
  Pass 0–4. Phase 4b.
- **Do not** delete `HarmonicRegion` itself. Phase 4b decides its
  fate (likely persists as tool-compat for batch_analyze.cpp).
- **Do not** touch `tools/batch_analyze.cpp`. Per the standing
  "stay out of batch_analyze" scope decision; Phase 4b will handle
  the shim that keeps it working.
- **Do not** introduce `KeyArea` consumption in cadence/pivot
  detection. Phase 5.
- **Do not** introduce analyzer-level reads of `Harmony` elements
  (per `project_chord_symbol_ban.md` / `docs/symbol_input_audit.md`).
- If Step E shows any diff outside expected (which is "no diffs at
  all"): halt and surface, do not regenerate goldens to paper over.
- If a field needed by `detectCadences` / `detectPivotChords` is
  missing from `AnalyzedRegion`: halt and surface — that's a recon
  gap, not something to invent your way around.
