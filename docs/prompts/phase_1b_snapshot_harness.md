# Phase 1b — Snapshot Harness Implementation

**Scope:** Build the snapshot test infrastructure that will pin current
user-facing output of the four analysis paths (P1 Implode, P2 Annotation,
P3 Tick-regional, P4 Tick-local) before any refactor in Phase 2+ touches
them. This is the safety net that makes the unified-pipeline refactor
verifiable.

**Prior state:** Phase 0 landed `docs/unified_analysis_pipeline.md` at
commit `d5f9b438ec`. Phase 1a recon completed and documented the
two-binary constraint (only `notation_tests`-style binaries have IoC +
ScoreRW), the absence of existing snapshot infrastructure, and the
P3/P4 public-API blending problem.

**Reference docs (read first):**
- `docs/unified_analysis_pipeline.md` — overall plan and phase map
- `docs/policy2_coalescing_map.md` — the divergences this harness must
  pin (A, C, D)
- `ARCHITECTURE.md` §5.13 — single-path model

---

## Pre-flight

1. `git status` and `git diff --stat` — if you see trailing `\0` bytes
   or mid-token truncation, a prior CC session was cut by usage limit;
   stop and surface it.
2. Confirm you are on `master` and up-to-date with origin.
3. Force a full rebuild before running any tests (branch-switch stale
   binary issue): delete the relevant files under `ninja_build_rel/` or
   re-run `cmd.exe //c "C:\s\MS\setup_and_build.bat"` and verify fresh
   binary timestamps.

---

## Deliverables

### 1. New test binary `pipeline_snapshot_tests`

Model the CMake target on `src/notation/tests/CMakeLists.txt`
(`notation_tests`). The binary must:
- Have full IoC setup (so `ScoreRW::readScore` works)
- Link against `notation`, `engraving`, `composing`, and whatever
  `notation_tests` links against
- Use the shared `gmain.cpp` (`src/framework/testing/gmain.cpp`)
- Accept a `--update-goldens` CLI flag parsed in the test main (or via
  env var `PIPELINE_SNAPSHOT_UPDATE=1` if that's cleaner with the
  existing gtest main — use whichever is less invasive)

Location: `src/notation/tests/pipeline_snapshot_tests/` (new
subdirectory). Register in the parent CMakeLists.

### 2. Add `bool wasRegional` to `NoteHarmonicContext`

File: `src/notation/internal/notationcomposingbridge.h` (struct defined
around line 55).

- Add field `bool wasRegional = true;` (default true — common path).
- In `analyzeHarmonicContextAtTick`
  (`src/notation/internal/notationcomposingbridge.cpp:489` per prior
  recon), set `wasRegional = true` on the P3 path and
  `wasRegional = false` on the P4 fallback path before returning.
- No other call sites need changes — existing consumers ignore the new
  field.

### 3. Corpus

Create `src/notation/tests/pipeline_snapshot_tests/corpus/` with these
10 scores. Prefer linking via DCML-relative paths
(`../../../../tools/dcml/...`) where the DCML corpus already has a
suitable piece; only copy a fresh fixture in if nothing suitable
exists.

- 4× Bach (one chorale, one two-voice invention, one fugue, one cello
  suite movement — monophonic baseline)
- 2× Classical (one Mozart piano sonata exposition, one Haydn string
  quartet slow movement)
- 2× Romantic (one Chopin prelude, one Brahms intermezzo)
- 1× Corelli trio sonata or concerto grosso movement
  (cadence-heavy real-corpus ground)
- 1× slot for a score with documented sub-beat passing harmony — pick
  the best candidate from the DCML corpus; if nothing clearly fits,
  substitute a second Chopin prelude and note in the README that
  sub-beat coverage is under-represented in Phase 1

Write `corpus/README.md` listing each score, its source, and one
sentence on why it was picked (which divergence or case it exercises).
Explicitly note that sub-beat and ambiguous-cadence categories are
under-represented by design — synthetic fixtures don't clear the 0.8
assertive-confidence gate (see `feedback_cadence_test_fixtures.md`
guidance).

### 4. Snapshot format and storage

Per-score snapshot at
`src/notation/tests/pipeline_snapshot_tests/snapshots/<score_stem>.json`:

```json
{
  "score": "bach_chorale_001.mscx",
  "schemaVersion": 1,
  "implode": [
    {
      "tick": 0,
      "durationTicks": 1920,
      "root": "C",
      "quality": "major",
      "key": "C",
      "mode": "major"
    }
  ],
  "annotation": [
    { "tick": 0, "text": "C", "key": "C" }
  ],
  "tickRegional": [
    {
      "tick": 0,
      "root": "C",
      "quality": "major",
      "key": "C",
      "wasRegional": true
    }
  ],
  "tickLocal": [
    { "tick": 0, "root": "C", "quality": "major", "key": "C" }
  ]
}
```

Rules:
- Serialize via `QJsonDocument::toJson(QJsonDocument::Indented)` so
  text diffs are reviewable.
- Floats rounded to 4 decimals.
- Sample ticks for `tickRegional` and `tickLocal`: one per measure
  downbeat, plus one mid-measure tick (halfway through the measure).
  Both paths sample the same tick set.
- `annotation` entries come from calling `addHarmonicAnnotationsToSelection`
  on a full-score selection and reading back the resulting Harmony
  elements.
- `implode` entries come from calling `populateChordTrack` (or whatever
  P1 Implode's entry is per `docs/unified_analysis_pipeline.md`) and
  reading the chord-track output.

### 5. Test structure

One `TEST_P(...)` parameterized over the 10 corpus scores. For each
score:
1. Load via `ScoreRW::readScore`.
2. Run P1, P2, P3, P4 as described above; build the in-memory snapshot
   `QJsonObject`.
3. If `--update-goldens`: write snapshot to disk and PASS.
4. Else: read disk snapshot; assert equality; on mismatch, print a
   unified diff of the two JSON blobs (use a helper — small diff
   implementation is fine) and FAIL.

Golden file absence on non-update runs is a failure with a message
telling the developer to run with `--update-goldens`.

### 6. CI

Add the binary to whatever `check_unit_tests.yml` already iterates
(Phase 1a recon confirmed `GTEST_OUTPUT=xml` is the existing idiom —
follow it). Do **not** add the `--update-goldens` invocation to CI;
that flag is a developer-local tool only.

---

## Build + test loop

```
cmd.exe //c "C:\s\MS\setup_and_build.bat"
cd C:\s\MS\ninja_build_rel
./pipeline_snapshot_tests.exe --update-goldens
./pipeline_snapshot_tests.exe        # should now pass
./composing_tests.exe                 # must still be 0/135 mismatch
./notation_tests.exe                  # must still pass
```

Note: build dir is `ninja_build_rel/` not `ninja_build/` — the CLAUDE.md
is stale on this point (see `feedback_build_dir.md` guidance).

Expected outcome:
- First run with `--update-goldens` creates 10 JSON files under
  `snapshots/`.
- Second run (no flag) passes against those baselines.
- `composing_tests` baseline preserved at 0/135.
- `notation_tests` unchanged.

---

## Commit + push

Single commit. Suggested message shape:

```
Phase 1b: snapshot harness for unified-pipeline refactor

Introduces pipeline_snapshot_tests binary + 10-score corpus snapshots
pinning current P1/P2/P3/P4 output. Adds `wasRegional` to
NoteHarmonicContext so tick-local fallback (Divergence A) is
observable in snapshots. Snapshots are the safety net Phase 2+
relies on to prove the unified analysis pipeline preserves behavior.

Part of docs/unified_analysis_pipeline.md refactor plan.
```

**Push to origin at end of session** (per
`feedback_push_branches_to_remote.md`).

---

## Report back

In your final message, include:
- Commit hash + confirmation of push
- Files touched count + rough LoC
- First-run golden output: confirm all 10 snapshots generated, brief
  note on any score that failed to load or produced surprising output
- Second-run PASS confirmation
- `composing_tests` result (should be 0/135)
- Any deviations from this prompt and why
- Any parked/deferred concerns for Phase 2 to pick up

---

## Scope guardrails

- **Do not** touch any of: `src/composing/` analysis code,
  `prepareUserFacingHarmonicRegions`, Pass 0–4 implementations,
  emitter code (implode chord-track writing, annotation writing). This
  phase is pure observation; Phase 2+ does the refactor.
- **Do not** modify catalog XML or ground-truth test data.
- **Do not** introduce new analyzer-level reads of `Harmony` elements
  anywhere. Snapshot harness reads Harmony elements only as
  post-analysis output (checking that annotation wrote them), never as
  input to analysis. See `project_chord_symbol_ban.md` memory.
- **Do not** delete or rewrite existing test infrastructure. Add
  alongside.
- If anything forces scope outside `src/notation/tests/`,
  `src/notation/internal/notationcomposingbridge.{h,cpp}` (for the
  `wasRegional` field only), or CMake wiring — stop and surface it
  before proceeding.
