# Fix `addHarmonicAnnotationsToSelection` Selection-Type Handling

**Scope:** `addHarmonicAnnotationsToSelection` produces empty output
when invoked on a list selection (Ctrl/right-clicked individual
notes) or single-element selection, but works correctly on range
selections. This is a bridge-layer bug in how the function converts
the user's selection into the tick range it passes to
`analyzeSection`. The analyzer itself is fine — status bar and
right-click menu (which use the same `analyzeSection` data via
P3) correctly identify chords at points where annotation produces
nothing.

**Symptom (Vincent's empirical inspection):** at m285 of the
composing_tests synthetic catalog (chord with notes D5, A#4, F#4,
C4, status bar/right-click both show `Csus(add9)` post-Divergence-E
fix):
- Selecting the chord via box/range selection → annotate works
- Selecting one note (single element) → annotate produces nothing
- Selecting two notes via Ctrl/right-click (list selection) → annotate produces nothing

Earlier diagnosis from `docs/three_paths_divergence_recon.md` had
attributed annotation emptiness to the 0.5-beat duration gate
(divergence C). That's a separate concern (the gate may or may not
also affect this case); the primary bug surfaced by Vincent's
selection-type testing is the bridge function not handling list
selections.

**Reference docs (read first):**
- `docs/three_paths_divergence_recon.md` — the recon that surfaced
  the m285 case
- `docs/policy2_coalescing_map.md` — divergence map; this fix
  doesn't change divergences C/A/B/D/E status, but reframes the
  m285 case
- `src/notation/internal/notationcomposingbridge.cpp` — where
  `addHarmonicAnnotationsToSelection` lives (entry around line 756
  per the Phase 1a recon)

**Memory references** (auto-loaded):
- `project_no_stripping_in_production` — analyzer/emitter outputs
  maximal/exact; this fix is bridge-layer, doesn't affect that
- `project_chord_symbol_ban` — analyzer reads notes + structural
  metadata only; this fix doesn't change inputs to the analyzer

---

## Pre-flight

1. `git status` and `git diff --stat` — trailing `\0` or mid-token
   truncation means a prior CC session was cut by usage limit;
   stop and surface.
2. Confirm on `master`, up-to-date with origin (or use the
   appropriate worktree if mainline is busy).
3. Force rebuild (`cmd.exe //c "C:\s\MS\setup_and_build.bat"`)
   and verify fresh binary timestamps. Build dir: `ninja_build_rel/`.
4. Cache pipeline_snapshot_tests baseline:
   `cp -r src/notation/tests/pipeline_snapshot_tests/snapshots /tmp/snapshots_selection_baseline/`

---

## Work order

### Step A — Recon: characterize current selection handling

Read `addHarmonicAnnotationsToSelection` in
`src/notation/internal/notationcomposingbridge.cpp` (around line
756 per the Phase 1a recon — verify current location). Trace:

1. **How does the function consume the selection?** What
   `Selection`-like API does it call (`tickStart()`, `tickEnd()`,
   `elements()`, `notes()`, etc.)?
2. **What `from`/`to` ticks does it pass to `analyzeSection`?**
   Trace the conversion from selection to ticks.
3. **What happens for each selection type?**
   - **Range selection:** typically has `tickStart()` and `tickEnd()`
     return meaningful values. Does the function use these?
   - **List selection:** typically has `elements()` or `notes()`
     return a discrete set. `tickStart()`/`tickEnd()` may return
     defaults, the first element's tick, or undefined values.
     What does the function compute as the range?
   - **Single element selection:** degenerate list selection.
     What does the function compute?

Look for any guard like `if (!selection.isRange())` or
`if (selection.empty())` that early-returns or skips processing.
Look for whether the function iterates elements directly or just
extracts a tick range.

### Step B — Surface findings before fixing

After Step A, write a one-paragraph summary of what's happening
and why list/single selections produce empty output. Likely
findings (don't pre-commit; let the code show):

- **(α) Single early-return for non-range selection.** The function
  has a guard `if (!selection.isRange()) return;` or equivalent
  that silently bails on list selection. **Fix:** extend the
  function to handle list selections by deriving a range from
  the selected elements' ticks.
- **(β) Range computation produces a degenerate range from list
  selection.** The function calls `tickStart()`/`tickEnd()` which
  return zero-width or invalid ranges for list selections; the
  resulting `analyzeSection` call produces no regions; the
  emitter has nothing to emit. **Fix:** detect list selection and
  derive a range from the selected notes' ticks instead.
- **(γ) Function works on range, but range computation has a bug.**
  Some selection-shape handling exists but produces wrong ranges
  for some selection types. **Fix:** correct the range derivation.
- **(δ) Architectural tangle.** The function's selection handling
  is coupled to multiple selection-shape APIs in a way that's
  hard to fix cleanly. **Halt and surface** — the fix is more
  involved than a small change, and you should ask for direction.

If the finding matches α, β, or γ: proceed to Step C.

If the finding is δ or anything more architecturally complex
than a small targeted fix: halt and surface the recon findings,
do not proceed to implementation.

### Step C — Implement fix (if Step B authorizes proceeding)

Extend the selection-to-range conversion to handle all selection
types:

- **Range selection:** continue using `selection.tickStart()` /
  `selection.tickEnd()` (or equivalent).
- **List selection:** derive `from = min(selectedNotes.tick)` and
  `to = max(selectedNotes.tick + duration)` over the selected
  notes. Or: extend to the natural region boundaries containing
  the selected notes (so a single note in a multi-note chord
  region triggers annotation of the whole region).
- **Single element selection:** treated as list of one. Same
  derivation.

The behavioral intent: any selection that includes at least one
note triggers annotation of the regions overlapping the selected
notes. The user shouldn't have to use a specific selection type
to get annotations.

Use existing MuseScore selection APIs where they exist; don't
introduce new infrastructure. If the existing API lacks a clean
way to enumerate selected notes for list selections, surface
that finding before working around it.

### Step D — Verify

```
cmd.exe //c "C:\s\MS\setup_and_build.bat"
cd C:\s\MS\ninja_build_rel
./pipeline_snapshot_tests.exe        # PASS, byte-identical to baseline
diff -q src/notation/tests/pipeline_snapshot_tests/snapshots /tmp/snapshots_selection_baseline/
                                      # zero output
./composing_tests.exe                 # 407/407, RealDiff baseline 5
./notation_tests.exe                  # 53/53
```

`pipeline_snapshot_tests` should stay byte-identical — the
snapshot harness uses range-style invocation of the annotation
path; selection-type handling isn't exercised.

`composing_tests` should pass unchanged.

`notation_tests` should pass unchanged.

**Manual verification (Vincent does this post-CC):** load a score
in MuseScore Studio, select notes via different selection types
(single click, Ctrl/right-click multi-select, range/box select),
and verify annotation produces output for all selection types.
This is a UX-level check CC can't perform automatically.

### Halt protocols

- **Step B finding is δ (architectural tangle):** halt, surface
  recon, do not implement.
- **Step D pipeline snapshots drift:** the change leaked into a
  path it shouldn't have. Surface.
- **Step D composing_tests or notation_tests regress:** unexpected;
  surface.
- **Step C: existing selection API doesn't support clean
  enumeration of list-selected notes:** surface and propose
  alternatives before working around it.

---

## Commit + push

Single commit. Suggested message skeleton:

```
Fix addHarmonicAnnotationsToSelection for list/single selections

The annotation entry-point function `addHarmonicAnnotationsToSelection`
was producing empty output when invoked on a list selection (Ctrl/
right-clicked individual notes) or single-element selection. Range
selections (box/click-drag) worked correctly. The bug was in the
function's selection-to-range conversion: [α/β/γ root cause from
Step B].

Fix: extends the selection handling to derive a tick range from
selected notes' ticks regardless of selection type. Any selection
that includes at least one note triggers annotation of the regions
overlapping the selected notes, matching the behavior users
intuitively expect.

The analyzer itself is unchanged; this is purely a bridge-layer
fix in how user selections map to range arguments for
`analyzeSection`.

Surfaced via Vincent's empirical inspection at m285 of the
composing_tests synthetic catalog: status bar and right-click
menu correctly identify the chord (Csus(add9)); annotation
produced nothing on list selections, worked on range. The
divergence wasn't analyzer or emitter behavior — it was selection
handling at the bridge entry point.

pipeline_snapshot_tests: 10/10 byte-identical (snapshot harness
uses range invocation; not exercised by this fix).
composing_tests: 407/407, RealDiff baseline 5 unchanged.
notation_tests: 53/53.
```

**Push to origin at end of session.**

---

## Report back

- Commit hash + push confirmation
- Files touched (expect small — bridge function and possibly a
  small helper for tick-range derivation)
- LoC delta
- Step B recon finding (α/β/γ/δ) with brief root-cause description
- pipeline_snapshot_tests byte-identity confirmation
- composing_tests + notation_tests results
- Any deviations and why

---

## Scope guardrails

- **Do not** modify `analyzeSection`, `emitHarmonicAnnotations`,
  or any analyzer / emitter logic. The fix is in the
  selection-to-range conversion at the bridge entry point.
- **Do not** modify the `minimumDisplayDurationBeats` duration
  gate. That's a separate concern; this fix targets selection
  handling specifically.
- **Do not** modify selection infrastructure (the `Selection`
  class or related types). Use existing APIs.
- **Do not** introduce new selection types or new options.
- **Do not** modify pipeline_snapshot_tests harness; it doesn't
  exercise this code path and shouldn't change.
- If existing Selection APIs don't support the needed
  enumeration: halt and surface; don't introduce a workaround.
- If Step B reveals architectural tangle (finding δ): halt,
  don't implement.
