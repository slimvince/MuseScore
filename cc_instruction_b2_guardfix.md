# CC Instruction — B2 guard fix (tighten to M3 AND aug5)

**Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only),
`C:\s\MS\build_and_test.md`

**Current state:** Branch `master`, HEAD `f6630b29cd`, **working tree clean.**
BIR: Baroque BIR=true=28, BIR=false=16; Jazz BIR=true=35, BIR=false=10.
Hard stops: Baroque BIR=false > 25, Jazz BIR=false > 13.
Tests: 407/407 composing, 52/52 notation, 11/11 snapshot (1 skipped).

The previous B2 attempt passed all composing and notation tests but produced 3
pipeline snapshot regressions (Schumann D-major V chord and Corelli G-major I chord
both flipped to aug7 spuriously). Root cause: the M3-only guard was too loose — the
aug7 template was winning on 3/4-tone partial matches (root+M3+m7, with aug5 absent)
because the +8 score offset inflates the partial-match score enough to beat a complete
major triad. Fix: require **both** M3 and aug5 to be present above threshold.

---

## Part A — Single guard edit in `chordanalyzer.cpp`

All other edits from the previous instruction (template array insertions at the two
TemplateDef sites, three score matrix size changes, catalog XML, test .cpp) are
**ALREADY CORRECT** and must be re-applied exactly as before. The only change vs the
previous instruction is the guard condition in Step A1.

Apply the previous instruction's Parts A2/A3/A4/B1/B2/C1/C2 exactly as written.
For Part A1, use this tightened guard instead of the previous one:

```cpp
// B2 guard: the 4-tone Augmented (aug7) template requires BOTH the major third
// (rootPc+4) AND the augmented fifth (rootPc+8) to be present above
// extensionThreshold. This prevents the template from out-scoring a complete
// major triad on partial matches where only root+M3+m7 are present (aug5 absent).
if (templates[tplIdx].quality == ChordQuality::Augmented
    && templates[tplIdx].intervals.size() == 4
    && (pcWeight[(rootPc + 4) % 12] <= prefs.extensionThreshold
        || pcWeight[(rootPc + 8) % 12] <= prefs.extensionThreshold)) {
    continue;
}
```

(The `||` means: skip if EITHER M3 or aug5 is absent. Equivalently: only score aug7
when BOTH are present.)

Verified against all known test cases:
- Sus4 `{E,A,C,D}` root E: G# (M3) absent → fires ✓
- Schumann D-major `{D,F#,A}` root D: A# (aug5=D+8) absent → fires ✓
- Corelli G-major `{G,B,D}` root G: D# (aug5=G+8) absent → fires ✓
- Tristan `{C,F#,A#,D}` root D: F# (M3=D+4) present AND A# (aug5=D+8) present → passes, D7♯5/C wins ✓

---

## Part B — Build and run all three test suites

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe > /tmp/comp_b2g.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED|\[  FAILED  \]" /tmp/comp_b2g.txt | tail -10; echo "exit:$?"
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe > /tmp/note_b2g.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED" /tmp/note_b2g.txt | tail -5; echo "exit:$?"
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe > /tmp/snap_b2g.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED" /tmp/snap_b2g.txt | tail -5; echo "exit:$?"
```

Expected: 407/407 composing, 52/52 notation, 11/11 snapshot (1 skipped).

If snapshots still fail, read the diff before doing anything:
```
grep -A 30 "FAILED\|Expected\|Actual" /tmp/snap_b2g.txt | head -60; echo "exit:$?"
```

Only update goldens if a snapshot shows an aug7 winner on a chord where BOTH M3 and
aug5 are genuinely present in the sounding notes (the new template fired correctly).
A snapshot where a plain major or minor triad flips to aug7 is still a spurious fire
— revert and report.

---

## Part C — Mismatch report

```
cat C:\s\MS\src\composing\tests\chord_mismatch_report.txt; echo "exit:$?"
```

Expected: 4 RealDiff / 126 ConventionDiff (−1 from 127, the Tristan m285 entry removed).

---

## Part D — BIR check, both presets

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus; echo "exit:$?"
cd C:\s\MS && python tools/analyze_inversion_errors.py > /tmp/bir_baroque_b2g.txt 2>&1; echo "exit:$?"
cat /tmp/bir_baroque_b2g.txt; echo "exit:$?"

cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz --output-dir tools/corpus; echo "exit:$?"
cd C:\s\MS && python tools/analyze_inversion_errors.py > /tmp/bir_jazz_b2g.txt 2>&1; echo "exit:$?"
cat /tmp/bir_jazz_b2g.txt; echo "exit:$?"
```

Hard stops: Baroque BIR=false > 25, Jazz BIR=false > 13.
If either is hit: revert all three files, report, stop.

---

## Part E — Commit (if clean)

```
cd C:\s\MS && git add src/composing/analysis/chord/chordanalyzer.cpp \
  src/composing/tests/data/chordanalyzer_catalog_jazz.musicxml \
  src/composing/tests/chordanalyzer_musicxml_tests.cpp; echo "exit:$?"
cd C:\s\MS && git commit -m "B2: add Augmented dominant 7th template {0,4,8,10} (C7#5)

Adds aug7 template alongside the Augmented triad. Guard: skip the 4-tone Augmented
template for any root where either M3 (rootPc+4) or aug5 (rootPc+8) is absent
below extensionThreshold — requires both defining tones to be present. Without
this both-tone guard, the template over-fires on complete major triads where the
m7 happens to be present (root+M3+m7 partial match beats the plain triad because
the aug5 score offset inflates the partial-match score).

Catalog: m285 Tristan {C,F#,A#,D} updated to D7#5/C (third inversion; root D,
bass C). m286 rest measure used for Tristan suffix coverage. m285 removed from
kJazzSymbolExceptions.

BIR: Baroque BIR=true=XX BIR=false=XX; Jazz BIR=true=XX BIR=false=XX.
Tests: 407/407 composing, 52/52 notation, 11/11 snapshot (1 skipped).
Mismatch: X RealDiff / X ConventionDiff."; echo "exit:$?"
```

---

## Report back

1. All named tests pass/fail
2. BIR delta Baroque + Jazz
3. Mismatch counts (expected 4 / 126)
4. Any snapshot goldens updated (and why they're correct)
5. Commit hash or revert notice
