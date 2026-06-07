# Iteration 78: Interior beat coverage + enharmonic spelling + Corelli quality

## Standing rule — no symbol inference

**No chord symbol string parsing. No Roman numeral inference. Structured fields only.**

**You are starting a new session with no memory of previous work.**
Read these files before doing anything else — they are your only source of truth:
1. `C:\s\MS\CLAUDE.md` — standing rules and pre-authorized file list
2. `C:\s\MS\build_and_test.md` — authoritative build and test commands
3. `C:\s\MS\STATUS.md` — current BIR baselines, HEAD commit, active iteration
4. `C:\s\MS\docs\quality_observations_iter76.md` — full quality catalogue

Baselines (verify against STATUS.md): BIR=true=3, BIR=false=119. Jazz BIR=false=10.
(Iter 77 committed 1f6caeedfb — §2.10 resolved, bridge on greedy-expand.)

Build fresh before every BIR measurement. Verify binary is newer than source.

---

## Goals

Three quality targets from the post-bridge-switch catalogue:

**Target A — R2: Missing interior beat coverage.**
SATB chorales (bach_chorale_001, bach_chorale_003) are missing chord annotations
at interior beats of measures. E.g. bar 2 beats 2–3 have no chord symbol. The
root cause is unknown — it may be greedy-expand not placing candidates at those
ticks, or placing them but failing a gate, or expanding a prior anchor to absorb
the interior beats. Investigate before fixing.

**Target B — R4: Enharmonic misspelling.**
E.g. "Abm7b5" where "G#m7b5" is correct (the note is G# not Ab). The analysis
pipeline works in pitch-class integers; somewhere in the display path the integer
is converted to a note name with the wrong enharmonic spelling. Investigate where
this conversion happens and fix it.

**Target C — 2 remaining Corelli notation failures.**
`CorelliOp01n08dOpeningAndSparseLateBeatsDoNotSmearPreviousChord` and
`CorelliOp01n08dUserReportedChordTrackAudit`. CC's Iter 76 report noted that at
the failing ticks the analyzer returns Eb+/G, G/B, or root-position chords —
not Power/Sus — so the diatonic quality helper from Iter 76 never fires. One
result (Eb+ augmented) is particularly suspicious and needs diagnostic
investigation to understand where it comes from.

---

## Step 1 — Code review: read all relevant files before any diagnosis

Read the following files in full. Do not make any code changes yet.

1. `src/composing/analysis/harmony/harmonicsegmenter.cpp`
   Focus: how anchor expansion works — does an R1 anchor absorb neighbouring
   ticks, preventing R2 from placing regions there? Look for any logic that
   merges or extends placed regions after placement.

2. `src/notation/internal/notationharmonicrhythmbridge.cpp`
   Focus: the full bridge pipeline — Pass 1 (sparse analysis), Pass 2 (merge/
   hysteresis), Pass 2b (alternatives). Understand what can suppress a chord
   symbol at an interior tick even if greedy-expand placed a region there.

3. The chord-symbol formatting / note-name conversion code.
   Search for where pitch-class integers (0–11) are converted to note names
   (C, C#, Db, D, …). This is likely in `src/composing/analysis/chord/` or
   `src/notation/internal/`. Find every site that does this conversion and
   note whether it uses the key signature to choose enharmonic spelling.

4. The two failing Corelli test bodies in
   `src/notation/tests/notationimplode_tests.cpp`.
   Read both tests fully — understand what ticks are being asserted, what
   expected values are, and what actual values are currently produced.

After reading, write a brief (bullet-point) summary of:
- How interior ticks could be suppressed in the current pipeline
- Where enharmonic spelling is decided
- What ticks and expected/actual values the Corelli tests assert

Report this summary before touching any code.

---

## Step 2 — Diagnostic: interior beat coverage (Target A)

Add temporary `fprintf(stderr, ...)` diagnostics to investigate why beats 2–3
of measures are missing annotations in bach_chorale_001 and bach_chorale_003.

Add to `greedyExpandSegmentation()` when score path contains "chorale_001" or
"chorale_003", print for every collected tick in the first 3 measures:

```
DIAG-INTERIOR tick=%d pcCount=%d winnerScore=%.4f threshold=%.4f
  duration=%d durationFloor=%d round=R%d passed=%d reason=%s
```

Also print the full placed-regions list after Round 1 + Round 2:
```
DIAG-PLACED [tick=N..M root=X quality=Y confidence=Z round=R reason=S] ...
```

Add to the bridge pipeline when score path contains "chorale_001":
```
DIAG-BRIDGE tick=%d action=[kept/dropped/merged] reason=%s
```

Build `batch_analyze` only. Run on both chorale fixtures. From the output:
1. Are beat-2 and beat-3 ticks present in the collected tick set?
2. If present — do they pass as placed regions? If not, which gate rejects them?
3. If placed — does the bridge drop or merge them?
4. Is any anchor region from beat 1 expanding to cover beats 2–3?

---

## Step 3 — Diagnostic: Corelli Eb+ augmented chord (Target C)

Run the two failing notation tests with verbose output:

```bash
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe \
    --gtest_filter="*CorelliOp01n08d*" --gtest_output=xml:/tmp/corelli_results.xml
```

Then add diagnostics to trace what tones are accumulated at the failing ticks.
In the bridge pipeline (notationharmonicrhythmbridge.cpp), when the score path
contains "corelli" and the tick matches a failing tick, print:

```
DIAG-CORELLI tick=%d toneCount=%d pcs=[list] pitches=[list with octave]
  winnerRoot=%d winnerQuality=%s winnerScore=%.4f
  runnerUpRoot=%d runnerUpQuality=%s runnerUpScore=%.4f
```

This will reveal:
1. Which pitch classes are sounding at the tick producing Eb+
2. Which specific pitch is creating the augmented interval
3. Whether the Eb+ is a primary winner or a close runner-up that should have
   lost

Build `batch_analyze` and run on the Corelli fixture. Cross-reference with the
test's expected values to identify the specific tick and voice responsible.

---

## Step 4 — Fix A: interior beat coverage

From Step 2 findings, apply the minimal targeted fix. Common scenarios and
suggested approaches:

**If interior ticks are in the tick set but failing Round 1 + Round 2:**
These are valid harmonic positions in 4-voice SATB texture. If score or duration
gates are rejecting them despite full voice coverage, investigate whether the
effective threshold is correctly computed. In SATB, `pcCount` should be 3–4 and
`activeStaves` should be 4 — thresholds should be at their unscaled values.
If they are still failing, add diagnostic to understand why and apply a targeted
fix.

**If interior ticks are being absorbed by a neighbouring anchor's expansion:**
If an R1 anchor at beat 1 is expanding rightward to cover beats 2–3 (treating
them as part of the same harmonic region), and the pitches at beat 2 differ
from beat 1, this is an incorrect expansion. The expansion should stop at any
tick where the pitch-class set changes by more than a threshold. Add a
pitch-change gate to anchor expansion: if the new PCs differ from the anchor's
PCs by more than 1 tone, stop the expansion at that tick.

**If the bridge is merging or dropping interior regions:**
Pass 2 (hysteresis/merge) may be collapsing short regions into a prior region
if the chord identity is similar. Add a minimum-region-duration guard to
Pass 2 merging: don't merge a region shorter than one beat if its chord
identity differs from the absorbing region.

Document the specific fix with a code comment.

---

## Step 5 — Fix B: enharmonic spelling

From Step 1 code review, at the site(s) where pitch-class integers are converted
to note names:

1. Check whether the key signature is available at the call site.
2. If the key signature IS available: use it to determine the correct enharmonic
   spelling. In a key with sharps, prefer sharps for altered tones (G# not Ab).
   In a key with flats, prefer flats (Ab not G#). At the boundary (key of C or
   Am), use the diatonic context of the chord root.
3. If the key signature is NOT available at the call site: thread it through
   from the call site's caller, or use the globalKeyFifths already present in
   the analysis context.

Specifically for the Corelli/Bach failures: A minor (no sharps/flats) should
prefer sharp spelling for the raised 7th (G# as leading tone, not Ab).

Do not change the pitch-class integer representation — only the display
conversion. Verify by running notation tests and checking the chord symbol
text in the output.

---

## Step 6 — Fix C: Corelli augmented / wrong quality chords

From Step 3 findings, implement the appropriate fix based on the root cause.

**If Eb+ comes from a passing/ornamental tone being included in the region:**
Apply a minimum-duration gate to tone accumulation in `collectRegionTones` —
tones from notes shorter than `DIVISION/4` (one sixteenth note) should be
excluded from chord analysis unless they are the only sounding notes in that
voice. This is the same fix discussed in Iter 77 Step 5 for short passing tones.

**If Eb+ comes from correct tone accumulation but wrong template match:**
The template scoring is selecting an augmented template over major/minor.
Investigate whether the complexity penalty (Iter 74 Fix A) is correctly applied
here. If the augmented template is winning with thin evidence, increase the
complexity penalty for augmented templates specifically (augmented chords are
rare in tonal music and require strong evidence).

**If G/B (first inversion) appears where G (root position) is expected:**
The B in bass is a passing note. This is a specific instance of R1 (passing
bass) — addressed as a separate fix below or deferred to Iter 79 as originally
planned. Report whether this is the cause and defer if it is.

---

## Step 7 — Remove all diagnostics. Build and run full test suite.

```bash
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

Required:
- 407/407 composing
- notation: no regressions below 51/53; target 53/53 if Corelli fixes land
- pipeline_snapshot: 11/11 (must hold)

---

## Step 8 — BIR validation

```bash
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque \
    --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Hard stops:
- BIR=true > 3
- BIR=false > 119

Jazz:
```bash
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz \
    --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Jazz hard stop: BIR=false > 75 (current 10). Restore Baroque corpus after.

Note: Fix A (interior beat coverage) touches greedy-expand and may affect
the Baroque corpus. BIR must be measured carefully. If BIR=false increases,
revert Fix A and report.

---

## Step 9 — Update STATUS.md and commit

For each fix that passes BIR and tests, commit it. If some fixes pass and
others cause regressions, commit the passing ones and revert the regressing
ones — report clearly.

```bash
git add src/composing/analysis/harmony/harmonicsegmenter.cpp
git add src/notation/internal/notationharmonicrhythmbridge.cpp
git add src/composing/analysis/chord/chordanalyzer.cpp   # if enharmonic fix is here
git add docs/quality_observations_iter76.md               # untracked — add now
git add C:\s\MS\STATUS.md
git commit -m "Composing: interior beat coverage + enharmonic spelling + Corelli quality (Iter 78)

Fix A — Interior beat coverage:
  [describe root cause found and fix applied]

Fix B — Enharmonic spelling:
  [describe where conversion happens and fix applied]

Fix C — Corelli augmented/quality errors:
  [describe root cause and fix, or 'deferred — root cause is R1 passing bass']

BIR=true: 3 → N. BIR=false: 119 → N. Jazz BIR=false: 10 → N."

git push
```

---

## Step 10 — Report to Cowork

```
Step 1 — Code review summary:
  Interior tick suppression mechanisms found: [list]
  Enharmonic spelling conversion site(s): [file:line]
  Corelli test assertions: [failing ticks, expected vs actual]

Step 2 — Interior beat diagnostic:
  Beat-2/3 ticks in collected set: [yes / no]
  Rejection gate (if present): [score / duration / staves / absorbed by anchor]
  Bridge suppression (if applicable): [describe]
  Root cause: [one sentence]

Step 3 — Corelli Eb+ diagnostic:
  Eb+ at tick=N: tones=[list] — extra pitch = [note, voice, duration]
  Root cause: [passing tone / wrong template / other]

Fix A (interior beats):
  Root cause: [describe]
  Fix applied: [describe]
  Notation tests now: N/53
  BIR impact: true=N false=N

Fix B (enharmonic spelling):
  Conversion site: [file:line]
  Fix applied: [describe]
  Abm7b5 → G#m7b5 confirmed: [yes / no]

Fix C (Corelli quality):
  Root cause: [passing tone / template / passing bass — defer to Iter 79]
  Fix applied / deferred: [describe]
  CorelliOp01n08d tests now: N/2 passing

Tests:
  composing: N/407
  notation: N/53
  pipeline_snapshot: N/11

BIR=true: 3 → N
BIR=false: 119 → N
Jazz BIR=false: 10 → N

Committed: [hash]

Quality observations updated: [yes — items resolved: list]
```
