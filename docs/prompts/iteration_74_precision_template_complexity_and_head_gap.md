# Iteration 74: Precision fixes — template complexity preference and head-gap key-prior

## Standing rule — no symbol inference

**No chord symbol string parsing. No Roman numeral inference. Structured fields only.**

**You are starting a new session with no memory of previous work.**
Read these files before doing anything else — they are your only source of truth:
1. `C:\s\MS\CLAUDE.md` — standing rules and pre-authorized file list
2. `C:\s\MS\build_and_test.md` — authoritative build and test commands
3. `C:\s\MS\STATUS.md` — current BIR baselines, HEAD commit, active iteration

Baselines (verify against STATUS.md): BIR=true=3, BIR=false=119. Jazz BIR=false=10.
(Iter 73 committed 59edc32865 — note-end ticks + head-gap synthesis. Bridge still Jaccard.)

Build fresh before every BIR measurement. Verify binary is newer than source.

---

## Design principle for this iteration: inferring precision

"Precision" means asserting only what the evidence supports, and making the
most conservative inference consistent with the available tones. Two specific
failures violate this principle in opposite directions:

**Over-assertion (Gmadd9 instead of Gm):** At a 2-PC region {G, Bb}, the
current scoring selects Gmadd9 — asserting the presence of D and A (unstated
tones) over the simpler Gm (root + minor third). Precision prefers the simplest
template compatible with the evidence.

**Wrong inference in head-gap (D7 instead of Cm at opening):** A non-tonic
chord is being placed at the opening of a C-minor piece where the structural
harmony is clearly the tonic. Without strong contrary evidence, precision
prefers the tonic — the statistically dominant harmony in any tonal opening.

---

## Step 1 — Read and investigate before touching anything

Read `src/composing/analysis/harmony/harmonicsegmenter.cpp` in full.

Then, with the bridge switched to greedy-expand (re-apply the bridge change
temporarily — do NOT commit it), add temporary `fprintf(stderr, ...)` diagnostics
to trace exactly what happens in the Corelli opening [0, 3840):

For each candidate tick in [0, 3840):
```
DIAG-CAND tick=%d pcCount=%d winnerScore=%.4f winnerRoot=%d round=R1/R2/unseen
```

For the head-gap synthesis (if it fires):
```
DIAG-HEAD startTick=%d headEnd=%d synthesizedRoot=%d synthesizedScore=%.4f
```

Build batch_analyze. Run on the Corelli batch-path fixture to get DIAG output
(the bridge instrumentation surfaces through batch_analyze which uses the same
harmonicsegmenter.cpp). Also run the notation tests to see which of the 5 tests
still fail and what the actual vs expected values are with the current Iter 73 fixes.

From the diagnostics, answer:
1. Is there a natural Round 1 or Round 2 placed region within [0, 3120) after
   Iter 73's note-end tick fix? (i.e., did Fix A create new candidates that
   became anchors in the opening?)
2. What chord does the head-gap synthesis produce? What is its winnerRoot and score?
3. At tick 2880 specifically — is D7 coming from a natural placed region, the
   head-gap synthesis, or the bridge's downstream consume loop?
4. At tick 1440 — is trebleTexts empty because no region covers it, or because
   the covering region's chord doesn't translate to an annotation?

Report these findings before making any code changes.

---

## Step 2 — Fix A: template complexity preference for thin-PC regions

In `chordanalyzer.cpp` (or wherever the per-template scoring loop lives),
add a complexity preference: when the number of distinct pitch classes in the
region (`regionPCCount`, already computed in Iter 72) is less than
`templateDefinedTones / 2`, apply a complexity penalty to the template's score.

**Principle:** a template that defines N tones but the region only provides
M < N/2 tones is asserting many unstated pitches. Precision requires evidence
before asserting unstated tones.

**Formula:**
```cpp
// Complexity penalty for templates that outrun the available evidence.
// templateDefinedTones = number of non-zero-weight tone slots in this template.
// regionPCCount = distinct pitch classes actually sounding.
const int templateDefinedTones = countTemplateDefinedTones(tpl);
const double evidenceRatio
    = (regionPCCount >= templateDefinedTones)
    ? 1.0
    : static_cast<double>(regionPCCount) / templateDefinedTones;
// Apply penalty only when evidence is thin: evidenceRatio < 0.5
const double complexityPenaltyFactor
    = (evidenceRatio >= 0.5) ? 1.0 : (0.5 + evidenceRatio);
score *= complexityPenaltyFactor;
```

For 2 PCs, Gm (3 defined tones): ratio = 2/3 = 0.67 ≥ 0.5 → no penalty.
For 2 PCs, Gmadd9 (4 defined tones): ratio = 2/4 = 0.5 = threshold → marginal.
For 2 PCs, G7 (4 defined tones): ratio = 0.5 → marginal penalty.
For 1 PC, Gm (3 defined tones): ratio = 1/3 < 0.5 → score × 0.83.
For 1 PC, G power/5th (2 defined tones): ratio = 1/2 = 0.5 → no penalty.
For 4 PCs, any standard chord: ratio ≥ 0.5 in almost all cases → unchanged.

`countTemplateDefinedTones()` should count the number of template slots with
non-zero weight. Read the template representation before implementing — do not
guess the data structure.

Adjust the threshold (0.5) and formula based on whether Gmadd9 vs Gm is
actually resolved by this penalty. If 2/4 = 0.5 is right at the threshold
and Gmadd9 still wins, tighten to 0.6.

---

## Step 3 — Fix B: key-prior preference in head-gap synthesis

From Step 1 you know what chord the head-gap synthesis currently produces and
why. Apply this fix:

In `greedyExpandSegmentation()`, when the head-gap synthesis fires, compute the
chord as currently (analyzeChord on [startTick, headEnd) tones). Then apply a
key-tonic preference: if the analyzeChord result's rootPitchClass does NOT match
the tonic PC (derived from `globalKeyFifths` and `globalKeyMode`) AND the winner
margin over the second-best chord is below a threshold, override the result with
the tonic chord.

```cpp
// Key-tonic prior for head-gap: prefer tonic when evidence is ambiguous.
// In a tonal piece, the opening is statistically dominated by the tonic.
// Only assert a non-tonic chord if it wins by a clear margin.
const int tonicPC = tonicPitchClass(globalKeyFifths);  // implement this
const bool resultIsTonic = (headResult.rootPitchClass == tonicPC);
const double headMargin = headResult.score - headResult.runnerUpScore;

static constexpr double kHeadGapTonicPreferenceMargin = 0.4;

if (!resultIsTonic && headMargin < kHeadGapTonicPreferenceMargin) {
    // Insufficient evidence to assert a non-tonic opening chord.
    // Fall back to tonic (best quality for tonicPC from the tones).
    headRegion.rootPitchClass = tonicPC;
    // Re-run analyzeChord constrained to tonicPC root if the API supports it,
    // or simply set quality to the modal tonic quality (Minor for minor key,
    // Major for major key).
    headRegion.reason = "head-gap-tonic-prior";
}
```

Implement `tonicPitchClass(globalKeyFifths)`: the tonic PC for a key with
`keyFifths` sharps/flats is `(7 * keyFifths + 12) % 12` (circle-of-fifths
derivation for the tonic). Read an existing key-analysis file that already
has this computation rather than guessing — it is almost certainly already
present in `src/composing/analysis/key/keymodeanalyzer.cpp` or similar.

`runnerUpScore` must be available from analyzeChord's return type. If it is
not, read the return type and add it, or compute the second-best differently.
Do not parse chord symbol strings to derive this.

---

## Step 4 — Build and run tests (bridge on Jaccard)

Remove all diagnostics added in Step 1. Revert the bridge to Jaccard.

```bash
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
```

Required: 407/407 composing, 53/53 notation. Any failure is a regression.

---

## Step 5 — BIR validation

```bash
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque \
    --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Hard stops — revert and report if:
- BIR=true increases above 3
- BIR=false increases above 119

BIR improvements in either direction welcome.

Jazz:
```bash
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz \
    --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Jazz hard stop: BIR=false > 75 (current 10). Restore Baroque corpus after.

---

## Step 6 — Update STATUS.md and commit

Update `C:\s\MS\STATUS.md`: new HEAD commit, updated BIR baselines,
active iteration "Iter 74 committed / bridge switch pending".

```bash
git add src/composing/analysis/harmony/harmonicsegmenter.cpp
git add src/composing/analysis/chord/chordanalyzer.cpp
git add C:\s\MS\STATUS.md
git commit -m "Composing: precision fixes — template complexity + key-prior (Iter 74)

Fix A — Template complexity preference:
  For regions where available PCs < templateDefinedTones / 2, apply
  a proportional complexity penalty to the template score. Prevents
  over-assertion of unstated tones (Gmadd9 over Gm for 2-PC dyads,
  complex slash chords over triads in sparse textures). Principle:
  assert only what the available evidence supports.

Fix B — Key-tonic prior in head-gap synthesis:
  When head-gap analyzeChord produces a non-tonic chord with margin
  below kHeadGapTonicPreferenceMargin, fall back to the key tonic.
  In a tonal opening without a confirmed anchor, the tonic is the
  statistically dominant harmony. Asserting a non-tonic chord requires
  clear evidence (margin >= threshold).

BIR=true: 3 → N. BIR=false: 119 → N. Jazz BIR=false: 10 → N."

git push
```

---

## Step 7 — Re-attempt bridge switch

Re-apply the bridge change. Build and run notation tests:

```bash
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
```

For each remaining failure, report: test name, tick, expected, actual.
If any tests now pass that failed before, note them.

**If 53/53 pass:**
```bash
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

Update STATUS.md: §2.10 resolved, "Iter 74 complete".

```bash
git add src/notation/internal/notationcomposingbridgehelpers.cpp
git add src/notation/tests/
git add C:\s\MS\STATUS.md
git commit -m "Composing: switch bridge path from Jaccard to greedy-expand (Task #58 Part B)

Iters 69–74: greedy-expand made texture-general for bridge path.
§2.10 compliance achieved.
BIR=true=N, BIR=false=N. Jazz BIR=false=N."

git push
```

**If tests still fail:** report remaining failures. For each, state whether
the failure represents a genuine musical regression (greedy-expand gives a
wrong answer) or a Jaccard-specific assertion (the test encodes Jaccard
fragmentation behavior, not a musical truth). This assessment drives whether
the next step is an algorithm fix or a test re-anchor.

---

## Step 8 — Report to Cowork

```
Step 1 diagnostic findings:
  Natural placed regions in [0, 3120) after Iter 73 Fix A: [list or none]
  Head-gap synthesis fired: [yes: startTick=N headEnd=N] / [no — why]
  Head-gap chord before Fix B: rootPC=N score=N margin=N
  Tick 2880 source: [natural region / head-gap / other]
  Tick 1440 empty: [no covering region / region present but no annotation]

Fix A (template complexity):
  Gmadd9 → Gm at m11:960: [resolved / still wrong — describe]
  SATB behavior unchanged: [yes / no — describe any BIR shift]

Fix B (key-tonic prior):
  Head-gap chord after Fix B: rootPC=N (tonicPC=N, margin=N)
  kHeadGapTonicPreferenceMargin used: N

BIR=true: 3 → N
BIR=false: 119 → N
Jazz BIR=false: 10 → N

Committed: [hash]

Bridge switch:
  notation_tests: N/53
  Remaining failures: [list with actual vs expected + musical assessment]
  Committed: [hash / not committed]

§2.10 status: [resolved / still blocked — remaining issue + musical assessment]
```
