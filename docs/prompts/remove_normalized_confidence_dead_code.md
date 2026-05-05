# Remove `ChordIdentity::normalizedConfidence` Dead Code

**Scope:** Remove `ChordIdentity::normalizedConfidence` and its
two supporting preference parameters as dead code. The
score-vs-confidence recon (`docs/score_vs_normalized_confidence_recon.md`,
commit `dbcf0d5ee6`) verdict was **unused metric** — zero live
readers post-Divergence-E. The cleanup is mechanical: remove the
field, the populate loop, the helper function, and the preference
parameters.

**Why it's worth removing rather than leaving:**

- Three field/function removals + two preference parameters = small
  but meaningful surface reduction
- Removes a tempting target for future code to sort by (the
  Divergence E mistake; pedal detection had already worked around
  this by reading score directly with a different-root comparison)
- The originally-intended use (gap-to-next-in-list as confidence)
  has known degenerate cases documented in pedal detection's
  comment block; if a genuine confidence signal is needed later,
  it should be re-derived from the different-root logic, not from
  this dead implementation

**Reference docs (read first):**
- `docs/score_vs_normalized_confidence_recon.md` (commit `dbcf0d5ee6`) —
  full recon with file:line citations for every removal target

**Memory references** (auto-loaded):
- `project_no_stripping_in_production` — analyzer outputs maximal
- `project_chord_symbol_ban` — analyzer reads notes only

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
   `cp -r src/notation/tests/pipeline_snapshot_tests/snapshots /tmp/snapshots_normconf_baseline/`

---

## Removal targets (per recon)

The following removals are required, with file:line citations
from the recon:

1. **`ChordIdentity::normalizedConfidence` field declaration** —
   `chordanalyzer.h:192`
2. **Preference parameter `confidenceSigmoidMidpoint`** —
   `chordanalyzer.h:401-409` (within `ChordAnalyzerPreferences`)
3. **Preference parameter `confidenceSigmoidSteepness`** —
   same block as above
4. **`normalizeChordConfidence()` static function** —
   `chordanalyzer.cpp:1467-1473`
5. **Populate loop** that writes `normalizedConfidence` to results —
   `chordanalyzer.cpp:1953-1963`

Verify exact locations via grep before removing — the recon's
file:line citations are accurate as of commit `dbcf0d5ee6`, but
if the working tree has drifted, follow the actual code.

---

## Important constraint — pedal detection inline `c2`

`chordanalyzer.cpp:2015-2041` (pedal detection) computes its own
sigmoid inline using `confidenceSigmoidMidpoint` and
`confidenceSigmoidSteepness`. Per the recon Q4: pedal detection
**doesn't read** `identity.normalizedConfidence`, but it **does
read** the two preference parameters to compute its own
`c2`.

**This means removing the preference parameters requires a
substitute for pedal detection.** Two options:

**(a)** Replace the pedal detection inline code with hardcoded
values. The current preference defaults are
`confidenceSigmoidMidpoint = 2.0` and
`confidenceSigmoidSteepness = 1.5`. Hardcode these as constants
inline, dropping the preference indirection.

**(b)** Rename the preference parameters to clarify they're
specifically for pedal detection (e.g.,
`pedalConfidenceSigmoidMidpoint`). Keep the parameters live but
narrow their semantic scope.

Recommend **(a)**. Pedal detection is the only consumer; the
indirection adds nothing once `normalizedConfidence` is gone. If
the values ever need tuning, they can be re-promoted to
preferences with a clearer name then.

If (a) is infeasible for some reason (e.g., the values are
overridden in tests or per-genre configurations we'd need to
preserve), surface and use (b) instead.

---

## Work order

### Step A — Remove the field and populate loop

Delete the populate loop at `chordanalyzer.cpp:1953-1963`.
Delete the `normalizeChordConfidence()` function at
`chordanalyzer.cpp:1467-1473`.
Delete the `normalizedConfidence` field declaration at
`chordanalyzer.h:192`.

### Step B — Update pedal detection

Replace the inline `c2` computation in pedal detection
(`chordanalyzer.cpp:2015-2041`) to use hardcoded constants
instead of reading from `prefs.confidenceSigmoidMidpoint` /
`prefs.confidenceSigmoidSteepness`. Use the current defaults
(2.0 and 1.5) as the constants. Comment briefly that these are
the previously-configured pedal-detection sigmoid parameters,
moved inline as part of the `normalizedConfidence` removal.

### Step C — Remove the preference parameters

Delete `confidenceSigmoidMidpoint` and `confidenceSigmoidSteepness`
from `ChordAnalyzerPreferences` in `chordanalyzer.h:401-409`.
Verify no other code references them (grep before removing).

### Step D — Build, verify, run tests

```
cmd.exe //c "C:\s\MS\setup_and_build.bat"
cd C:\s\MS\ninja_build_rel
./composing_tests.exe                 # 407/407, RealDiff baseline 4 unchanged
./pipeline_snapshot_tests.exe         # 10/10 byte-identical
diff -q src/notation/tests/pipeline_snapshot_tests/snapshots /tmp/snapshots_normconf_baseline/
                                       # zero output
./notation_tests.exe                  # 53/53
```

All tests should pass byte-identical to baseline. The removed code
had no live readers (per recon), so removal can't change runtime
behavior. Pedal detection's inline `c2` continues to work with the
hardcoded constants.

### Halt protocols

- **Pipeline_snapshot_tests drift:** unexpected — surface. The
  removal shouldn't affect any code path that influences emitter
  output.
- **composing_tests baseline shifts:** also unexpected — surface.
- **notation_tests regress:** unexpected — surface.
- **Grep finds an unexpected consumer of `normalizedConfidence`,
  `confidenceSigmoidMidpoint`, or `confidenceSigmoidSteepness`** that
  the recon missed: surface and pause; don't remove the parameter
  if it has a live reader.

---

## Commit + push

Single commit. Suggested message:

```
Remove ChordIdentity::normalizedConfidence dead code

The score-vs-normalizedConfidence recon (commit dbcf0d5ee6, doc
docs/score_vs_normalized_confidence_recon.md) verdict was "unused
metric": ChordIdentity::normalizedConfidence had zero live read
sites post-Divergence-E (commit 9047b8adf9 removed the right-click
and status-bar sort consumers). Pedal detection acknowledged the
field's degenerate-case defect by computing its own sigmoid inline.

Removes:
- ChordIdentity::normalizedConfidence field declaration
- normalizeChordConfidence() static function
- The populate loop in analyzeChord() that wrote the field
- ChordAnalyzerPreferences::confidenceSigmoidMidpoint
- ChordAnalyzerPreferences::confidenceSigmoidSteepness

Updates pedal detection's inline c2 computation to use hardcoded
constants (2.0, 1.5 — the previous preference defaults) instead
of reading from the now-removed parameters. If pedal sigmoid
tuning is needed in future, re-promote with a clearer name (e.g.
pedalConfidenceSigmoidMidpoint).

Future confidence-signal needs should re-derive using the
different-root gap logic from pedal detection, not the
position-i+1 gap that this metric attempted.

composing_tests: 407/407, RealDiff baseline 4 unchanged.
pipeline_snapshot_tests: 10/10 byte-identical.
notation_tests: 53/53.
```

**Push to origin at end of session.**

---

## Report back

- Commit hash + push confirmation
- Files touched + LoC delta (expect net deletion — removing field
  + function + populate loop + 2 preferences, replacing one inline
  read with hardcoded constants)
- Confirmation that pedal detection's behavior is preserved
  (sigmoid output unchanged with hardcoded constants matching the
  previous preference defaults)
- Test results
- Any deviations and why

---

## Scope guardrails

- **Do not** modify `score`'s computation. The recon confirmed
  `score` is the canonical metric; this cleanup removes the
  dead alternative, not the live one.
- **Do not** change the candidate-ranking order produced by
  `analyzeChord()`. Sort still happens by `score` descending; the
  removal doesn't touch that.
- **Do not** modify `KeyModeAnalysisResult::normalizedConfidence`
  on the unrelated key-analyzer struct (per recon Q4 — different
  struct, actively used, working correctly, not under
  investigation).
- **Do not** modify pedal detection's algorithm beyond replacing
  the preference reads with hardcoded constants. The
  different-root gap logic stays as-is.
- **Do not** introduce new preferences to "preserve flexibility."
  If pedal sigmoid tuning is ever needed, re-promote with a
  clearer name then.
- **Do not** modify `analyzeSection`, the pipeline structure, or
  any emitter. The cleanup is in chord-identification scoring
  only.
- **Do not** change `chordResults` shape or sort order. Consumer
  code (status bar, right-click, all emitters) trusts that order
  unchanged.
- If grep surfaces a consumer the recon missed: halt and surface.
  The recon was thorough but not running code; if a usage was
  hidden behind macros or template instantiations, the recon
  might have missed it.
