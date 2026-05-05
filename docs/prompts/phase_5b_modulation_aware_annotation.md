# Phase 5b — Modulation-Aware Annotation Emitter

**Scope:** Wire `KeyArea` data into the annotation emission path so
Roman numerals are written relative to the enclosing key area
(rather than the per-region key, which may be a low-confidence
excursion the gate absorbed). Add a boundary marker at each
KeyArea transition. Add `enclosingKeyArea` to `NoteHarmonicContext`
so status bar and right-click menu also see modulation context.

This is the **first phase that intentionally changes user-visible
annotation output.** Annotation snapshots WILL diff on modulating
scores. That's the feature working, not a regression. Diff
inspection + halt-and-surface protocol mirrors Phase 3c-impl's
alternatives diff handling.

**Prior state:** Phase 5a landed at commit `c5b6907ec0`. KeyArea
derivation now uses confidence gate (0.8); `keyAreas` arrays are
captured in snapshots. Two known investigation points from 5a
travel forward:
- **Mozart K.279/1**: post-gate detects a C minor span at ticks
  `[8640, 30720)`. The piece is in C major; the conventional
  exposition modulates to G major (dominant), not C minor. Phase
  5b annotations in this span will be written in C minor — verify
  whether they look musically coherent (real tonicization the
  analyzer caught) or systematically wrong (analyzer bug).
- **Chopin Op.30 No.1**: single Eb minor key area for the whole
  16-measure window. The piece is in Eb major (per-region had
  Eb minor 0.288 → Eb major 0.762, both below threshold; first
  detected won). Phase 5b annotations will be relative to Eb minor.
  This is a known calibration boundary, not a 5b regression.
  Romans should be internally consistent; flag any that look
  internally incoherent (a different bug from the key-misidentification).

**Reference docs (read first, in this order):**
- `docs/phase5_recon.md` — full recon report. Q3 specifies the
  `enclosingKeyArea` slot-in on `NoteHarmonicContext`. Q5 enumerates
  the design options for label format and recommends the existing
  `→` convention for pivot transitions.
- `docs/unified_analysis_pipeline.md` — Phase 5 plan, including the
  `useKeyAreaRelativeRomanNumerals` design intent.
- Phase 5a commit `c5b6907ec0` — current state of KeyArea
  derivation and snapshot harness.
- Phase 3c-impl commit `9f515d6372` — precedent for how `wasRegional`
  was added to `NoteHarmonicContext` (pattern this work follows).

---

## Pre-flight

1. `git status` and `git diff --stat` — trailing `\0` or mid-token
   truncation means a prior CC session was cut by usage limit;
   stop and surface.
2. Confirm on `master`, up-to-date with origin.
3. Force rebuild (`cmd.exe //c "C:\s\MS\setup_and_build.bat"`)
   and verify fresh binary timestamps before running tests.
   Build dir is `ninja_build_rel/`, not `ninja_build/`.
4. Cache the pre-Phase-5b snapshot baseline:
   `cp -r src/notation/tests/pipeline_snapshot_tests/snapshots /tmp/snapshots_p5b_baseline/`

---

## Critical principles (preserve through this work)

- **Analyzer outputs are maximal and exact.** The annotation
  emitter writes what the analyzer produces. No stripping, no
  user-preference simplification, no shipping-product reduction.
  Per `project_no_stripping_in_production` memory.
- **No analytical content as analyzer input.** Reading user-written
  Romans, key annotations, modulation labels, etc. as analyzer
  input is banned regardless of storage type. Per the generalized
  `project_chord_symbol_ban` memory.
- **No DCML label reads.** DCML key labels are comparison metadata
  for future tuning; never analyzer input. Phase 5b uses only the
  analyzer's own `KeyArea` output.
- **`findTemporalContext` and `collectRegionTones` survive.** Per
  `docs/divergence_d_recon.md`.
- **Key signature stays a weak prior.** Notes always win; key
  signature can bias but not override note evidence. Per
  ARCHITECTURE.md's documented hierarchy. The annotation emitter
  uses the analyzer's *output* (`KeyArea` spans), not the key
  signature directly.

---

## Notation conventions (settled)

**Pivot chord transitions:** existing `→` format already produced
by `detectPivotChords` and written to `HarmonyType::ROMAN` Harmony
elements. Format: `"vi → ii"` (outgoing-key Roman, U+2192 RIGHT
ARROW, incoming-key Roman). No change to this convention; it
travels through unchanged.

**Non-pivot key transitions** (key change without a pivot chord —
direct modulation, sequence-driven shift, etc.): write a bracketed
key-prefix marker as a separate ROMAN Harmony element at the first
tick of the new KeyArea. Default format: `"[D:]"` (bracket,
key-letter with mode case — uppercase for major, lowercase for
minor — colon, bracket close). Aldwell/Laitz convention. If
MuseScore's ROMAN renderer produces visually unclean output for
the bracket characters, surface and propose alternatives — but
default to the bracketed form.

**Romans within a KeyArea:** plain Roman numerals (no key prefix),
written relative to the enclosing KeyArea's key/mode. The boundary
marker establishes the key context; subsequent Romans operate in
that context until the next boundary marker.

This means: annotations within a stable key area look unchanged
from current Phase 4b output if the analyzer's per-region key
matched the area key. They differ when the per-region key was a
low-confidence excursion the gate absorbed — those Romans now get
re-derived relative to the enclosing area instead of the absorbed
local key.

---

## Work order

### Step A — Add `enclosingKeyArea` to `NoteHarmonicContext`

File: `src/notation/internal/notationcomposingbridge.h` (per
recon Q3, around line 56).

Add a field:

```cpp
struct NoteHarmonicContext {
    // ... existing fields
    std::optional<mu::composing::analysis::KeyArea> enclosingKeyArea;  // new
};
```

Header may need a forward declaration or include of
`src/composing/analyzed_section.h` to make `KeyArea` visible.

### Step B — Populate `enclosingKeyArea` in P3 path

File: `src/notation/internal/notationcomposingbridge.cpp` (per
recon Q3, in `analyzeNoteHarmonicContextRegionallyInWindow`,
around lines 226–306).

When the matched region is found, populate
`context.enclosingKeyArea` from
`section.keyAreas[matchedRegion.keyAreaId]`. If `keyAreaId` is
out of range (defensive check), leave as `std::nullopt`.

P4 fallback path (`analyzeHarmonicContextLocallyAtTick`):
`enclosingKeyArea` stays `std::nullopt` — P4 has no region or
section concept. Per recon, this is the documented graceful
degradation.

### Step C — Extend `harmonicAnnotation` formatter

File: `src/notation/internal/notationcomposingbridge.cpp` (per
recon Q3, around lines 474–584 — the `harmonicAnnotation(Note*)`
function).

When `context.enclosingKeyArea` is set and its key/mode differs
from the per-region `keyFifths`/`keyMode`, append modulation
context to the formatted string. Format suggestion (CC may refine):

Current:
```
"Chord: Dm (0.88) | D (0.76) in key: F Major"
```

Modulation-aware:
```
"Chord: Dm (0.88) | D (0.76) in key: F Major (in area: G Major)"
```

Or whichever phrasing reads cleanly in the status bar. The point
is that the user sees both the per-region key analysis (what the
analyzer thought locally) AND the enclosing key area (what the
gate determined the structural context to be).

When `enclosingKeyArea` matches the per-region key, no change to
the formatted string — the data is consistent and adding it would
be visual noise.

When `enclosingKeyArea` is `std::nullopt` (P4 fallback), no change
to the formatted string — graceful degradation.

### Step D — Extend `emitHarmonicAnnotations`

File: `src/notation/internal/notationcomposingbridge.cpp` (the
`emitHarmonicAnnotations` function established in Phase 3b).

The emitter currently iterates regions and writes a Roman per
region using the per-region key. Modify to:

1. Track the "active" KeyArea while iterating regions (initially
   the first region's KeyArea).
2. At each region:
   - Look up the region's enclosing KeyArea via `keyAreaId`.
   - If the enclosing KeyArea differs from the active KeyArea
     (we've crossed a boundary):
     - Check if `detectPivotChords` produced a pivot label for
       this transition. If yes: the pivot label is already
       written by the existing pivot-chord path; nothing extra
       needed for the boundary itself.
     - If no pivot label exists at this boundary: write a bracketed
       key-prefix marker (`"[D:]"` style) as a ROMAN Harmony
       element at the boundary tick.
     - Update the active KeyArea to the new one.
   - Write the region's Roman relative to the active KeyArea's
     key/mode (NOT the per-region key). This is the key change
     in user-visible behavior: regions whose local key was
     absorbed by the gate now get Romans interpreted in the
     enclosing key.
3. Continue through all regions.

The pivot-chord path (existing `detectPivotChords` output
producing `"vi → ii"` labels) remains complementary and untouched.
Phase 5b adds boundary markers for non-pivot transitions, not
duplicates of pivot labels.

**Implementation note:** the recon Q5 mentioned a
`useKeyAreaRelativeRomanNumerals` flag from
`unified_analysis_pipeline.md:195`. This Phase 5b implementation
treats the behavior as always-on (no flag) since the principle is
"analyzer always produces maximal/correct output." If a flag is
needed for transition reasons, surface and discuss before adding
it — defaults should be the new behavior.

### Step E — Regenerate snapshot goldens and inspect diff

```
cmd.exe //c "C:\s\MS\setup_and_build.bat"
cd C:\s\MS\ninja_build_rel
./pipeline_snapshot_tests.exe --update-goldens
./pipeline_snapshot_tests.exe        # PASS after regen
diff -r /tmp/snapshots_p5b_baseline/ src/notation/tests/pipeline_snapshot_tests/snapshots/
```

**Expected diff scope:** changes ONLY in `annotation` arrays of
modulating scores. No diffs in `implode`, `implodedChordTrack`,
`tickRegional`, `tickLocal`, `keyAreas` (those were settled in
Phase 5a and shouldn't shift), `score`, or `schemaVersion`.

Modulating scores expected to diff (per Phase 5a empirical data):
- `mozart_k279_1` — 2-area split, expect annotation diffs in the
  C-minor span [8640, 30720)
- `chopin_bi105_op30_1` — single Eb minor area; if the per-region
  Eb major sub-section's Romans were absorbed into Eb minor, that
  span's annotations diff
- `corelli_op01n08a` — single g minor area post-gate, pre-gate had
  4 areas; if any per-region keyModeResults differed from g minor,
  those Romans diff
- `bach_chorale_003` — 2→1 area collapse; potentially small annotation
  diffs in the absorbed minor section
- `bach_bwv806_prelude` — A-minor tail absorbed into A-major area;
  potentially small annotation diffs at the end

Non-modulating scores expected byte-identical:
- `bach_chorale_001`, `bach_bwv806_gigue`, `mozart_k280_1`,
  `chopin_bi105_op30_2`, `schumann_kinderszenen_n01` — single
  stable area each, no boundary markers, no key reinterpretation.

**If diffs appear outside `annotation` arrays:** halt and surface.
That's an unexpected behavior change.

**If the modulating-score annotation diffs differ substantially
from the predictions above:** still proceed to Step F, but flag
the surprise in the diff summary.

### Step F — Halt for review

Surface a structured diff summary BEFORE committing. Include:

1. **Per-modulating-score summary:**
   - How many annotation entries diffed
   - Sample of the diffs (3–5 representative entries with old vs new)
   - Whether boundary markers (`[D:]` style) appear at expected
     KeyArea transitions
   - Whether pivot-chord labels (`→` format) at pivot transitions
     are unchanged (they should be — Phase 5b doesn't touch
     `detectPivotChords`)

2. **Mozart K.279/1 specific verification:** What do the Romans
   look like in the C-minor span [8640, 30720)? Sample 3–5
   annotations from that span. Do they look:
   - Internally coherent under C minor (i.e., V-i progressions,
     iv-i progressions, etc. that make sense in C minor)
   - Internally incoherent (i.e., chord identities that don't
     fit C minor harmonic vocabulary, suggesting the C minor
     identification is wrong)
   - Vincent will use this to decide whether the analyzer's
     C-minor span detection is a bug or a real (if unconventional)
     analytical choice.

3. **Chopin Op.30 No.1 specific verification:** What do the Romans
   look like in the single Eb-minor area? Sample 3–5 annotations.
   Are they internally consistent under Eb minor? (The piece is
   actually Eb major; the gate kept Eb minor winning. We expect
   the Romans to be internally consistent under Eb minor, but
   *musically wrong* given the actual key. Verify the internal
   consistency.)

4. **Boundary marker rendering:** if the `[D:]` format produces
   visually unclean output (e.g., MuseScore renders the brackets
   as part of the chord notation incorrectly), flag and propose
   alternatives.

**Wait for user approval before committing.** This is the
behavior-changing milestone of Phase 5; the diff is the feature,
and Vincent reviews to confirm the feature is working as
intended (with documented edge cases at the calibration boundaries).

### Step G — Commit + push after approval

Single commit. Suggested message skeleton (CC fills specifics
based on Step F findings):

```
Phase 5b: modulation-aware annotation emitter

Adds enclosingKeyArea to NoteHarmonicContext (populated from
matched region's keyAreaId in P3 path; nullopt on P4 fallback
per recon Q3 graceful degradation).

Extends harmonicAnnotation formatter to surface modulation context
when the enclosing KeyArea differs from per-region key analysis
(both visible to user; not a stripping or reduction).

Extends emitHarmonicAnnotations to write Romans relative to the
enclosing KeyArea key/mode (rather than per-region key), with
bracketed key-prefix boundary markers ("[D:]" style) at non-pivot
KeyArea transitions. Existing pivot-chord labels ("vi → ii" via
detectPivotChords) remain untouched and complementary.

Snapshot impact:
- annotation arrays diff on modulating scores (the feature working)
- implode, implodedChordTrack, tickRegional, tickLocal byte-identical
- keyAreas byte-identical (Phase 5a settled, untouched)

Known calibration findings from Phase 5a travel forward as
documented investigation points:
- Mozart K.279/1: C-minor span [8640, 30720); Phase 5b Romans
  there [are coherent / are incoherent / specific finding].
- Chopin Op.30 No.1: single Eb-minor area; Phase 5b Romans
  internally consistent under Eb minor; piece is actually Eb
  major (known calibration boundary at 0.8 threshold).

composing_tests 376/376 + mismatch baseline preserved.
notation_tests 53/53.
```

**Push to origin at end of session.**

---

## Report back

- Commit hash + push confirmation
- Files touched count + rough LoC
- Step E initial-diff scope (confirm: annotation only, no
  implode/tickRegional/tickLocal/keyAreas drift)
- Step F structured diff summary, with the Mozart K.279/1 and
  Chopin Op.30 No.1 specific verification findings
- User approval received before commit
- `composing_tests` result (376/376, 0/135 + 135/135)
- `notation_tests` result (53/53)
- `pipeline_snapshot_tests` result (10/10)
- Any deviations and why
- Parked concerns for follow-on work (Phase 5c if threshold
  tuning needed; analyzer-side improvements for the K.279/1 and
  Op.30/1 cases if surfaced as real bugs; etc.)

---

## Scope guardrails

- **Do not** retune the 0.8 confidence threshold from Phase 5a.
  If empirical findings suggest tuning is warranted, surface for
  separate Phase 5c discussion — don't unilaterally adjust.
- **Do not** modify `KeyArea` derivation logic. Phase 5a settled
  this; Phase 5b consumes the output.
- **Do not** modify `detectPivotChords`. Existing pivot-chord
  labels are complementary; Phase 5b adds boundary markers for
  non-pivot transitions, not duplicates.
- **Do not** introduce DCML label reading. Comparison metadata for
  future tuning sessions, never analyzer input.
- **Do not** modify implode, tick-regional, or tick-local emitters.
  Phase 5b is annotation-only.
- **Do not** touch `prepareUserFacingHarmonicRegions` shim.
  Tool-side compat preserved.
- **Do not** introduce analyzer-level reads of any user-written
  analytical content (Harmony, StaffText, RehearsalMark, etc.) —
  content-based check per generalized
  `project_chord_symbol_ban`.
- **Do not** add a `useKeyAreaRelativeRomanNumerals` flag. The
  modulation-aware behavior is the new default; analyzer always
  produces maximal/correct output. If a flag seems necessary for
  transition reasons, surface and discuss first.
- **Do not** change divergence A (P4 parallel pathway, by design)
  or divergence C behavior (parked with cadence-aware-gate idea).
- **Do not** auto-accept the Step E diff. Step F halts for user
  review.
- If Step E shows diffs outside `annotation` arrays: halt and
  surface — unexpected behavior change.
- If Step F finds the boundary marker format renders unclean in
  MuseScore: flag and propose alternatives, don't proceed with a
  visibly broken annotation.
