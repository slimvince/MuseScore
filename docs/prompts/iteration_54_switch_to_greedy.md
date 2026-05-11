# Iteration 54: Switch analyzeScore to greedy-expand output — first BIR measurement

## Standing rule — no symbol inference

**No chord symbol string parsing. No Roman numeral inference. Structured fields only.**

Read `C:\s\MS\CLAUDE.md` and `C:\s\MS\build_and_test.md` first.
Baselines: BIR=true=21, BIR=false=128. Jazz BIR=false=20.

Build fresh before every BIR measurement. Verify binary is newer than source.

---

## Background

Rounds 1 and 2 are implemented and stable. The algorithm places ~59.6 regions per
chorale vs Jaccard's 37.4. The placed/jaccard ratio (1.63) is a proxy — not the
target. BIR is the only real validation.

This iteration switches `analyzeScore` in `tools/batch_analyze.cpp` to use
greedyExpandSegmentation output instead of detectHarmonicBoundariesJaccard.
The existing scoring loop, temporal context, merge pass, and JSON serialisation
are all unchanged — only the source of boundary ticks changes.

`detectHarmonicBoundariesJaccard` remains in the file. Do NOT delete it yet.

---

## Step 1 — Add tick-extraction helper

Add a conversion function that extracts boundary ticks from placed PlacedRegions:

```cpp
/// Extracts the start ticks of all placed regions (round >= 1) as a sorted
/// vector of Fractions, suitable for use as drop-in replacement for the
/// detectHarmonicBoundariesJaccard output in analyzeScore.
static std::vector<Fraction>
placedRegionsToTicks(const std::vector<PlacedRegion>& regions) {
    std::vector<Fraction> ticks;
    for (const auto& r : regions)
        if (r.round >= 1)
            ticks.push_back(Fraction::fromTicks(r.startTick));
    std::sort(ticks.begin(), ticks.end());
    ticks.erase(std::unique(ticks.begin(), ticks.end()), ticks.end());
    return ticks;
}
```

---

## Step 2 — Switch analyzeScore

In `analyzeScore`, find the existing call:
```cpp
auto boundaryTicks = detectHarmonicBoundariesJaccard(score, startTick, endTick,
                                                      excludeStaves);
```

Replace with:
```cpp
// Iter 54: switch to greedy-expand segmentation (Task #62).
// detectHarmonicBoundariesJaccard is deprecated and retained below for reference.
auto greedyRegions = greedyExpandSegmentation(score, startTick, endTick,
                                               excludeStaves, prefs,
                                               chordAnalyzer.get(),
                                               initialKey.fifths,
                                               initialKey.mode);
auto boundaryTicks = placedRegionsToTicks(greedyRegions);
```

Note: `chordAnalyzer`, `initialKey.fifths`, and `initialKey.mode` must be
available at this call site. If the existing analyzeScore creates these after
the boundary detection call, move the greedy call to after their initialisation.
Read the surrounding code to confirm ordering before editing.

---

## Step 3 — Remove or suppress diagnostic stderr

The diagnostic `fprintf(stderr, "[greedy-diag] ...")` added in Iter 51 must be
removed or commented out before the corpus run. It writes to stderr and
`run_bach_preset.py` captures stderr with `--diag-out`. Without `--diag-out`,
it is discarded — but confirm this does not corrupt JSON stdout.

Option: wrap in `#ifdef GREEDY_DIAG` and leave disabled by default. Or simply
remove it — it has served its purpose.

---

## Step 4 — Build

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
```

Fix any compile errors. If `chordAnalyzer` or `initialKey` are not yet
initialised at the call site, restructure `analyzeScore` to initialise them
earlier. Do not introduce circular dependencies.

---

## Step 5 — Run Baroque corpus and measure BIR

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque \
    --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Record BIR=true and BIR=false.

**Interpret results:**

BIR=false decreases (< 128): greedy segmentation is finding genuine chord
  changes that Jaccard was suppressing. Improvement confirmed.

BIR=false unchanged (≈ 128 ± 5): segmentation change is neutral for BIR.
  The extra regions are not hurting. Architecturally still an improvement.

BIR=false increases by ≤ 10 (128–138): modest over-segmentation. Tighten
  distinctness in Round 2 before proceeding (change distinctness from
  root-OR-quality to root-AND-quality for both neighbours).

BIR=false increases by > 10 (> 138): significant over-segmentation.
  Investigate which chord types are regressing before deciding on fix.
  Do NOT commit.

BIR=true increases (> 21): genuine inversions are being lost. Investigate
  immediately — do NOT commit.

---

## Step 6 — Jazz validation (only if Baroque BIR=false ≤ 138)

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz \
    --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Jazz BIR=false hard stop: ≤ 75.

Restore Baroque after:
```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque \
    --output-dir tools/corpus
```

---

## Step 7 — Run both test suites

```
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
```

Expected: 407/407 and 53/53.

Pipeline snapshot tests may fail if region boundaries changed. Verify changed
regions are genuine improvements before refreshing goldens:
```
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

---

## Step 8 — Commit (only if BIR=false ≤ 138 and BIR=true ≤ 21 and Jazz ≤ 75)

```
git add tools/batch_analyze.cpp
git commit -m "Segmentation: switch batch_analyze to greedy-expand (Task #62, Rounds 1+2)

Replaces detectHarmonicBoundariesJaccard with greedyExpandSegmentation in
analyzeScore. Boundary ticks now derived from greedy-placed regions (round >= 1).
detectHarmonicBoundariesJaccard retained in source, deprecated.

Round 1 anchors: on-beat, dur >= DIVISION, >= 3 voices, score >= 1.5.
Round 2 fills: bilateral anchor context, harmonically distinct, score >= 1.0.
Mean regions per chorale: 37.4 (Jaccard) -> N.

BIR=true: 21->N  BIR=false: 128->N  Jazz BIR=false: N"
```

---

## Step 9 — Report to Cowork

```
Step 2 — Switch location: analyzeScore line N
  chordAnalyzer available: [yes / required reordering]
  initialKey available: [yes / required reordering]

Step 5 — Baroque BIR:
  BIR=true: 21 → N
  BIR=false: 128 → N
  Interpretation: [improvement / neutral / modest regression / significant regression]

Step 6 — Jazz BIR=false: N (hard stop ≤ 75)

Step 7 — Tests:
  composing: N/407
  notation: N/53
  Pipeline snapshot: [updated / no change / failed]

Mean regions per chorale: N (was 37.4 Jaccard)

Committed: [yes — hash] / [not committed — reason]
```
