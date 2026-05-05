# Fix b9/#9 Extension Detection on Non-Dominant Chords (2 entries)

**Scope:** Fix 2 RealDiff entries at mm 316 and 329 in the composing_tests
baseline. Vincent inspected both measures and confirmed the catalog is
right and the analyzer is wrong:

- **m316** notes: D#5, B4, G4, E4, C4 — that's `C E G B D#` = `CMaj7#9`
  (root + maj3 + perfect5 + maj7 + augmented 9). Analyzer produces
  `CMaj7`, missing the D# as a #9 alteration. **Catalog correct.**
- **m329** notes: C4, Eb4, G4, Bb4, Db5 — that's `C Eb G Bb Db` = `Cm7b9`
  (root + min3 + perfect5 + min7 + flat 9). Analyzer produces `Cm7`,
  missing the Db as a b9 alteration. **Catalog correct.**

Mechanical analyzer fix in `chordanalyzer.cpp` (composing module,
autonomous-authorized per CLAUDE.md). Both bugs may share a root cause
(missing 9-extension detection on non-dominant chord qualities) — if
so, one fix resolves both. Investigate before assuming.

Note: Mode 1 QA's classification (`docs/mismatch_classification.md`)
flagged these as "clear catalog issues." Vincent's inspection
contradicts that — the catalog is asserting real extensions present
in the notes. Mode 1 QA's first-pass impressions are now corrected
empirically; the actual finding is "analyzer doesn't detect b9/#9
on non-dominant chords."

Expected outcome: composing_tests RealDiff baseline drops from **7
to 5**. Pipeline snapshots stay byte-identical (the 10-corpus suite
doesn't exercise these specific synthetic-catalog chords).

**Reference docs (read first):**
- `src/composing/tests/chord_mismatch_report.txt` — current report
  with mm 316 and 329 entries showing expected vs actual symbols
- `docs/mismatch_classification.md` — Mode 1 QA classification
  (note: m316 and m329 were flagged as "clear catalog issues" but
  this was wrong; treat as analyzer bugs per Vincent's inspection)

**Memory references** (auto-loaded):
- `project_no_stripping_in_production` — analyzer always produces
  maximal/correct output; this fix produces correct extension
  detection
- `project_composing_tests_baseline_synthetic` — context on the
  catalog and what RealDiff means

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
   `cp -r src/notation/tests/pipeline_snapshot_tests/snapshots /tmp/snapshots_b9_baseline/`
5. Run composing_tests fresh and confirm RealDiff count is 7 (the
   post-viiø-fix baseline pinned at commit `59f65d569f`):
   `cd C:\s\MS\ninja_build_rel && ./composing_tests.exe`. If the
   baseline differs, halt and surface.

---

## Work order

This follows CLAUDE.md's standing autonomous-loop pattern. Specific
shape for this session:

### Step A — Read the 2 failing entries

Read `src/composing/tests/chord_mismatch_report.txt` for the m316
and m329 entries. Confirm:
- m316 expected: `CMaj7#9`, actual: `CMaj7`
- m329 expected: `Cm7b9`, actual: `Cm7`

If the entries look different from this expected vs actual pattern,
halt and surface.

### Step B — Investigate root cause

In `src/composing/analysis/chord/chordanalyzer.cpp` (and possibly
siblings), find the b9/#9 extension detection logic — likely in
`detectExtensions()` near the existing `hasEleventhSharp` guard
that the previous viiø fix touched (commit `59f65d569f`,
chordanalyzer.cpp:892).

Hypotheses to investigate (don't guess — verify in code):

1. **Missing detection entirely:** the analyzer doesn't check for
   b9 / #9 at all on non-dominant qualities (Major7, Minor7).
2. **Gated by chord quality:** detection exists but is gated on
   dominant-7 quality only, excluding Major7 and Minor7 contexts.
3. **Detected but suppressed in symbol formatting:** detection
   produces the alteration but the symbol formatter drops it for
   non-dominant chords.

The viiø fix's pattern (the `hasFlatFifth` gate being always-true
for half-diminished, masking a real issue) suggests gating logic
errors are common in this area. Apply the same diagnostic discipline:
trace the code path with the m316 and m329 note inputs as test
cases.

**Whether the two bugs share a root cause is part of the
investigation.** If yes (e.g., a single quality-gate exclusion),
one fix resolves both. If no (e.g., #9 and b9 have separate detection
paths with different bugs), two fixes may be needed.

### Step C — Implement the fix(es)

Targeted change in `chordanalyzer.cpp`. Keep the diff minimal —
focused bug fix(es), not refactor.

The fix must:
- Detect D# as #9 above CMaj7 chord tones (m316 case)
- Detect Db as b9 above Cm7 chord tones (m329 case)
- Not affect existing #9/b9 detection on dominant-7 chords (V7b9,
  V7#9 must still work correctly)
- Not introduce false-positive #9/b9 detection on chords that don't
  have those alterations

If the investigation reveals that the cleanest fix would touch
broader extension-detection structure, halt and surface — that's a
larger conversation than this session.

### Step D — Build and verify

```
cmd.exe //c "C:\s\MS\setup_and_build.bat"
cd C:\s\MS\ninja_build_rel
./composing_tests.exe
```

Expected: composing_tests passes, RealDiff count drops from 7 to
**5**. Mismatch report shows mm 316 and 329 are no longer classified
as RealDiff.

```
./pipeline_snapshot_tests.exe        # PASS, byte-identical to baseline
diff -q src/notation/tests/pipeline_snapshot_tests/snapshots /tmp/snapshots_b9_baseline/
                                      # zero output
./notation_tests.exe                  # 53/53
```

`pipeline_snapshot_tests` and `notation_tests` must stay
byte-identical — the 10-score corpus shouldn't exercise these
specific synthetic chords.

### Halt protocols

- **RealDiff drops to 4 or fewer:** the fix absorbed entries beyond
  the expected two — surface which entries also shifted and verify
  they're real improvements, not regressions in disguise.
- **RealDiff stays at 7 or rises:** fix didn't take or introduced
  regressions. Surface.
- **Only one of m316 / m329 resolved:** partial fix. Surface — likely
  separate root causes, may need follow-up.
- **pipeline_snapshot_tests drift:** shipping product behavior
  changed unexpectedly. Surface.
- **Investigation reveals broader refactor needed to fix cleanly:**
  halt and surface; this session is targeted bug fix scope.

---

## Commit + push

Single commit. Suggested message skeleton:

```
Fix b9/#9 detection on non-dominant chord qualities

The analyzer was missing b9 and #9 alteration detection on
Major7 and Minor7 chord qualities (e.g., CMaj7#9 was emitted
as CMaj7; Cm7b9 was emitted as Cm7). [Brief root cause from
Step B — was this a missing detection, a quality gate, or a
formatter suppression?]

[Brief description of the fix.]

composing_tests RealDiff baseline drops from 7 to 5. Mismatch
entries at mm 316 (CMaj7#9) and m329 (Cm7b9) are now resolved.

Note: Mode 1 QA classification (docs/mismatch_classification.md,
commit 3378b9c7da) had flagged these as "clear catalog issues."
Vincent's inspection of the underlying notes (m316: C E G B D#;
m329: C Eb G Bb Db) confirmed the catalog was correct and these
were analyzer bugs. Mode 1 QA's first-pass impressions stand
corrected empirically.

The fix preserves correct b9/#9 detection on dominant-7 chords
and doesn't introduce false positives.

pipeline_snapshot_tests: 10/10 byte-identical.
notation_tests: 53/53.
```

Update the test's pinned RealDiff baseline reference (in
`src/composing/tests/chordanalyzer_musicxml_tests.cpp` per the
viiø-fix precedent at commit `59f65d569f`) from 7 to 5.

**Push to origin at end of session.**

---

## Report back

- Commit hash + push confirmation
- Files touched + rough LoC (expect small for a targeted fix)
- Root cause explanation (was it a single shared cause for both,
  or two separate bugs?)
- Confirmation that mm 316 and 329 are no longer RealDiff
- New RealDiff baseline (expected 5)
- pipeline_snapshot_tests byte-identity confirmation
- notation_tests 53/53
- Any deviations and why

---

## Scope guardrails

- **Do not** touch the catalog (`chordanalyzer_catalog.musicxml`).
  Standing do-not-touch — and irrelevant here since Vincent
  confirmed the catalog is correct for these entries.
- **Do not** modify `analyzeSection`, `prepareUserFacingHarmonicRegions`
  shim, KeyArea derivation, or pipeline structural code. The fix
  is in chord-identification logic, downstream of pipeline structure.
- **Do not** modify the `stripSymbol` / `classifyComparison`
  test infrastructure. The fix produces correct maximal analyzer
  output, which the existing comparison protocol then classifies
  correctly.
- **Do not** introduce broader extension-detection refactoring. If
  the bug requires deeper changes, halt and surface.
- **Do not** introduce stripping into production. The fix produces
  correct maximal output (analyzer now emits #9/b9 when present),
  not reduced output.
- **Do not** modify b9/#9 detection on dominant-7 chords if that
  logic is currently correct — only extend or fix the broken cases.
- If composing_tests baseline drops below 5, halt and surface;
  verify the additional entries are real improvements before
  pinning a lower baseline.
- If pipeline_snapshot_tests drift, halt and surface — fix has
  leaked into production unexpectedly.
