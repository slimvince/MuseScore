# Fix viiø Inversion Symbol Bugs (3 entries)

**Scope:** Fix 3 RealDiff entries in the composing_tests baseline at
mm 364, 366, 368. Mode 1 QA classification flagged these as "Pattern E
— spurious #11 in half-dim inversion labels." Phase 5b's progressive
comparison classification confirmed they're real analyzer bugs, not
notation-convention disagreements. Mechanical analyzer fix in
`chordanalyzer.cpp` (composing module, autonomous-authorized per
CLAUDE.md).

Expected outcome: composing_tests RealDiff baseline drops from **10
to 7**. Pipeline snapshots stay byte-identical (these specific
synthetic-catalog chords aren't in the 10-corpus snapshot suite).

**Reference docs (read first):**
- `src/composing/tests/chord_mismatch_report.txt` — the post-Phase-5b
  report; mm 364/366/368 entries have the catalog-vs-analyzer detail
  per entry. Read these three entries first to see the exact
  expected vs actual symbols.
- `docs/mismatch_classification.md` — Mode 1 QA classification.
  Pattern E ("spurious #11 in half-dim inversion labels") describes
  the failure mode.
- `docs/extension_stripping_policy.md` — recent baseline framing
  (135 was pre-stripping mismatch count; 10 is current actionable
  RealDiff baseline; this work drops it to 7).

**Memory references** (auto-loaded):
- `project_no_stripping_in_production` — analyzer always emits
  maximal output; this fix is about producing CORRECT maximal
  output, not stripping anything
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
   `cp -r src/notation/tests/pipeline_snapshot_tests/snapshots /tmp/snapshots_viio_baseline/`
5. Run composing_tests fresh and confirm RealDiff count is 10:
   `cd C:\s\MS\ninja_build_rel && ./composing_tests.exe`. If the
   baseline number differs, stop and surface — something has
   shifted since Phase 5b's commit.

---

## Work order

This follows CLAUDE.md's standing autonomous-loop pattern for
composing-module mismatch reduction: analyse → implement → build →
test → report. Specific to this session:

### Step A — Read the 3 failing entries

Read the chord_mismatch_report.txt entries for mm 364, 366, 368.
Each should show:
- Expected (catalog) symbol
- Actual (analyzer) symbol
- Notes sounding in the chord

The pattern (per Mode 1 QA): the analyzer is adding a spurious
`#11` to half-diminished (`viiø`, `m7b5`) inversion labels. The
catalog expects the half-diminished symbol without the #11.

Confirm the pattern from the actual report. If the entries look
different from "spurious #11 in half-dim inversion labels," halt
and surface — the work shape may need adjustment.

### Step B — Investigate root cause

In `src/composing/chordanalyzer.cpp` (and possibly siblings), find
the chord-identification path that produces the inversion-aware
symbol output. The bug is likely in:

- The `#11` alteration detection logic (incorrectly firing on a
  note that's a chord tone of the inverted half-dim, not an
  alteration)
- OR the inversion bookkeeping interacting with extension detection
  (an inverted half-dim's bass note being misread as a #11)
- OR symbol formatting that sticks `#11` onto half-dim outputs in
  inversion contexts

Don't guess — trace the actual code path. Use the notes from the
m364/366/368 entries as test inputs.

### Step C — Implement the fix

Targeted change in `chordanalyzer.cpp`. Keep the diff minimal —
this is a focused bug fix, not a refactor. The fix should:
- Stop the spurious `#11` from being added to half-diminished
  inversion outputs
- Not affect other chord types' #11 detection (a real `#11` on a
  major chord should still be detected)
- Not affect non-inverted half-diminished outputs

If you find that fixing the `#11` issue cleanly requires touching
broader extension-detection logic, halt and surface — that's a
larger conversation than this session.

### Step D — Build and verify

```
cmd.exe //c "C:\s\MS\setup_and_build.bat"
cd C:\s\MS\ninja_build_rel
./composing_tests.exe
```

Expected: composing_tests passes, RealDiff count drops from 10
to **7**. Mismatch report shows mm 364/366/368 are no longer
classified as RealDiff.

```
./pipeline_snapshot_tests.exe        # PASS, byte-identical to baseline
diff -q src/notation/tests/pipeline_snapshot_tests/snapshots /tmp/snapshots_viio_baseline/
                                      # zero output
./notation_tests.exe                  # 53/53
```

`pipeline_snapshot_tests` and `notation_tests` must stay
byte-identical. The 10-score corpus shouldn't include these
specific synthetic chords; if any score's annotation shifts,
that's surprising — investigate before proceeding.

### Halt protocols

- **RealDiff count drops to fewer than 7** (e.g., 5): great, but
  surprising. The fix may have absorbed entries beyond the
  expected three — surface which entries also shifted and verify
  they look like correct improvements, not regressions in
  disguise.
- **RealDiff count stays at 10 or rises**: the fix didn't take or
  introduced new mismatches. Surface and investigate before
  committing.
- **Pipeline snapshots drift**: shipping product behavior changed
  unexpectedly. Surface; this should be a no-op for production
  code paths.
- **m364/366/368 still classified as RealDiff but mismatch text
  changed**: partial fix. Surface — may need a follow-up.

---

## Commit + push

Single commit. Suggested message skeleton:

```
Fix viiø inversion #11 spurious-alteration bug

The analyzer was producing half-diminished inversion symbols with
a spurious #11 alteration (e.g., "Cø7/Eb#11" where the catalog
correctly expects "Cø7/Eb"). [Brief root-cause description from
Step B.]

[Brief description of the fix.]

composing_tests RealDiff baseline drops from 10 to 7. Mismatch
report entries at mm 364, 366, 368 are now resolved. The fix
preserves correct #11 detection on non-half-diminished chords and
on non-inverted half-diminished chords.

pipeline_snapshot_tests: 10/10 byte-identical (no production
behavior change for the 10-score corpus, which doesn't exercise
this synthetic case).
notation_tests: 53/53.
```

Update `src/composing/tests/chord_mismatch_report.txt`'s expected
baseline reference (or wherever the "10" pin lives in test code)
to the new value (7).

**Push to origin at end of session.**

---

## Report back

- Commit hash + push confirmation
- Files touched + rough LoC (expect small — this is a targeted bug
  fix, probably <30 lines)
- Brief root-cause description of where the spurious #11 was being
  injected
- Confirmation that the 3 specific entries (mm 364, 366, 368) are
  no longer RealDiff
- New RealDiff baseline (expected 7)
- Verification that pipeline_snapshot_tests stays byte-identical
- `notation_tests` 53/53
- Any deviations and why

---

## Scope guardrails

- **Do not** touch the catalog (`chordanalyzer_catalog.musicxml`).
  Standing do-not-touch.
- **Do not** modify `analyzeSection`, `prepareUserFacingHarmonicRegions`
  shim, KeyArea derivation, or any pipeline structural code. This
  fix is in chord-identification, downstream of pipeline
  structure.
- **Do not** modify the stripping or `classifyComparison`
  infrastructure landed in the previous extension-stripping
  session. This fix is upstream — it makes the analyzer produce
  correct symbols, which the existing comparison protocol then
  classifies correctly.
- **Do not** introduce broader refactoring of the extension-detection
  logic. If the bug requires deeper changes, halt and surface.
- **Do not** introduce stripping into production. The fix produces
  correct maximal output (no spurious #11), not reduced output.
- If the fix turns out to require touching multiple chord types'
  detection logic, halt and surface — single-purpose bug fix is
  the scope; broader work is a different session.
- If composing_tests baseline drops below 7 (other entries
  unexpectedly resolved), halt and surface — verify the entries
  that shifted look like real improvements before pinning a lower
  baseline.
