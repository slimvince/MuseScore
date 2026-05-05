# Phase 3a — Convert Implode to Consume `AnalyzedSection`

**Scope:** Split `populateChordTrack` into analysis (`analyzeSection()`)
+ a new emitter (`emitImplodedChordTrack`). Add chord-track read-back
to the snapshot harness *before* the refactor so the emitter's
behavior is pinned. Consolidate `hasAssertiveExposure` to read from
`AnalyzedRegion` instead of implode's local computation.

**Prior state:** Phase 2 landed at commit `4ff4a444a4`. Audit
confirmed zero emitter-leaked fields on `ChordTemporalContext` —
analyzer/emitter boundary is already clean at the
`ChordAnalysisResult`/`HarmonicRegion` interface, so this phase is
"convert consumer" not "untangle."

**Reference docs (read first):**
- `docs/unified_analysis_pipeline.md` — overall plan, Phase 2 audit
  appendix
- `docs/policy2_coalescing_map.md` — divergences map (D stays untouched
  until 3c)

---

## Pre-flight

1. `git status` and `git diff --stat` — trailing `\0` or mid-token
   truncation means a prior CC session was cut by usage limit; stop
   and surface.
2. Confirm on `master`, up-to-date with origin.
3. Force rebuild (`setup_and_build.bat`) and verify fresh binary
   timestamps before running tests.

---

## Work order

The order matters. Do not reorder. Each step's verification is the
safety net for the next step.

### Step A — Add chord-track read-back to snapshot harness

File: `src/notation/tests/pipeline_snapshot_tests/pipeline_snapshot_tests.cpp`

Add a new top-level snapshot key `implodedChordTrack` to each
per-score JSON. Schema:

```json
"implodedChordTrack": [
  {
    "tick": 0,
    "durationTicks": 1920,
    "pitches": [60, 64, 67],
    "harmonyText": "C"
  }
]
```

- One entry per emitter tick. If a `Chord` and a `Harmony` share a
  tick (the common case from implode), merge into one entry.
- If only one is present at a tick (chord without harmony, or
  harmony without chord), still emit one entry — populate what's
  there, leave the missing field as default (`pitches: []` or
  `harmonyText: ""`).
- `pitches` sorted ascending for stable diffs.
- Read from the actual chord track that implode writes to. Find the
  track by inspecting the current `populateChordTrack` implementation
  at `src/notation/internal/notationimplodebridge.cpp:563` (per
  Phase 1b recon) — the track index/identifier should be derivable
  from that code.

### Step B — Regenerate goldens with current behavior

```
cmd.exe //c "C:\s\MS\setup_and_build.bat"
cd C:\s\MS\ninja_build_rel
./pipeline_snapshot_tests.exe --update-goldens
./pipeline_snapshot_tests.exe        # must PASS
```

Initial diff (without `--update-goldens`, before regenerating) should
show **only** new `implodedChordTrack` keys appearing in each file —
no diffs to existing keys. If existing keys diff, stop and surface;
something else changed.

After regeneration, all 10 snapshots have populated
`implodedChordTrack` arrays reflecting current implode emit
behavior. **This is the baseline that the refactor must preserve
byte-exact.**

Update `corpus/README.md` to document the new snapshot key.

### Step C — Refactor: split `populateChordTrack`

File: `src/notation/internal/notationimplodebridge.cpp` (and `.h` if
the new function needs to be visible).

Introduce `emitImplodedChordTrack(Score* score, const AnalyzedSection& section, /* other current populateChordTrack args */)`
in the same `.cpp` file as `populateChordTrack`. The emitter
consumes `AnalyzedSection` and writes to the chord track exactly as
the current `populateChordTrack` does — same notes, same harmonies,
same track placement, same voicings.

Rewrite `populateChordTrack` as a thin wrapper:

```cpp
void populateChordTrack(/* current args */) {
    auto section = analyzeSection(score, from, to);
    emitImplodedChordTrack(score, section, /* forwarded args */);
}
```

Do **not** change `populateChordTrack`'s signature — call sites stay
untouched. Phase 4+ decides whether to inline this.

While converting, replace implode's local `hasAssertiveExposure`
computation with reads from `AnalyzedRegion::hasAssertiveExposure`.
Delete the now-unused implode-local computation. This is a one-shot
behavior-equivalent simplification per the Phase 2 audit.

### Step D — Verify byte-identity

```
cmd.exe //c "C:\s\MS\setup_and_build.bat"
cd C:\s\MS\ninja_build_rel
./pipeline_snapshot_tests.exe        # must PASS without regeneration
./composing_tests.exe                 # 376/376, 0/135 mismatch
./notation_tests.exe                  # 53/53
```

`pipeline_snapshot_tests` must PASS without `--update-goldens`. Any
diff at all — `implodedChordTrack`, `implode`, anything — means the
refactor changed emit or analysis behavior.

**If any diff appears in step D, stop. Do not commit. Do not
"fix" by regenerating goldens. Surface the diff and halt for
guidance.** The whole point of step B was to fix the baseline so D
can prove preservation.

---

## Commit + push

Single commit, only after step D passes. Suggested message:

```
Phase 3a: convert implode to consume AnalyzedSection

Splits populateChordTrack into analyzeSection() + new
emitImplodedChordTrack(AnalyzedSection). populateChordTrack remains
as a thin wrapper so call sites stay untouched.

Adds implodedChordTrack snapshot key to pipeline_snapshot_tests
covering note-level chord-track output (tick, duration, pitches,
harmonyText). Goldens regenerated once before the refactor; the
refactor preserves them byte-identical.

Replaces implode's local hasAssertiveExposure computation with
AnalyzedRegion::hasAssertiveExposure per Phase 2 audit category (iii).

Zero behavior change verified by snapshot byte-identity.
```

**Push to origin at end of session.**

---

## Report back

- Commit hash + push confirmation
- Files touched count + rough LoC
- Step B initial-diff output (confirm: only new `implodedChordTrack`
  keys, no other diffs)
- Step D PASS confirmation (snapshots pass without regeneration)
- `composing_tests` result (expect 376/376, 0/135 mismatch)
- `notation_tests` result (expect 53/53)
- One-line summary of what was deleted in the
  `hasAssertiveExposure` consolidation (line count, location)
- Any deviations and why
- Parked concerns for Phase 3b

---

## Scope guardrails

- **Do not** touch annotation (`addHarmonicAnnotationsToSelection`)
  or tick-regional/tick-local paths. Phase 3b/3c.
- **Do not** touch any analysis logic:
  `prepareUserFacingHarmonicRegions`, `analyzeSection`'s delegate
  body, Pass 0–4, `analyzeChord`, etc.
- **Do not** change `populateChordTrack`'s signature or remove its
  callers' indirection — keep it as a wrapper.
- **Do not** touch divergence D (P3 re-analysis) — Phase 3c.
- **Do not** introduce analyzer-level reads of `Harmony` elements
  (per `project_chord_symbol_ban.md`). Reading Harmony elements
  off the chord track for snapshot read-back is fine — that's
  post-emit observation, not analyzer input.
- **Do not** migrate `ChordTemporalContext` fields to
  `AnalyzedRegion` (audit category iii). Phase 3c.
- **Do not** rename `ChordTemporalContext`. Flagged for later.
- If step D fails: stop and surface. Do not regenerate goldens to
  paper over the diff.
