# Iteration 51: Replacement segmentation — data structures and candidate generation

## Standing rule — no symbol inference

**No chord symbol string parsing. No Roman numeral inference. Structured fields only.**

Read `C:\s\MS\CLAUDE.md` and `C:\s\MS\build_and_test.md` first.
Baselines: BIR=true=21, BIR=false=128. Jazz BIR=false=20.

Build fresh before every BIR measurement. Verify binary is newer than source.

---

## Background

This iteration implements the foundation of the replacement segmentation algorithm
in `tools/batch_analyze.cpp` only. Two steps:

1. Define `PlacedRegion` — the working type for the greedy-expand algorithm.
2. Implement candidate generation — collect all note-change-event boundaries
   (every tick where any note attacks or releases), producing a dense candidate
   pool. This is the exhaustive foundation that Round 1 greedy selection will
   filter in Iter 52.

The existing `detectHarmonicBoundariesJaccard` is NOT removed yet. The new
function runs in parallel and its output is reported for diagnostic purposes only.
No BIR change is expected this iteration — existing scoring is untouched.

Do NOT modify any scoring code. Do NOT modify the bridge path.

---

## Step 1 — Define PlacedRegion

In `tools/batch_analyze.cpp`, above the `analyzeScore` function, add:

```cpp
/// Working type for the greedy-expand segmentation algorithm.
/// Produced by greedyExpandSegmentation(); consumed by analyzeScore().
struct PlacedRegion {
    int startTick = 0;
    int endTick   = 0;

    // Greedy-expand metadata
    int    round      = 0;      ///< 0 = candidate (not yet placed), 1+ = placed in that round
    double confidence = 0.0;    ///< chord-score confidence at placement time
    bool   isAnchor   = false;  ///< true if placed in round 1 (structural anchor)
    std::string reason;         ///< human-readable placement rationale

    // Chord identity determined at placement time (from analyzeChord on tones)
    int    rootPitchClass = -1;
    int    bassPitchClass = -1;
    // quality stored as string for now — replace with ChordQuality enum if convenient
    std::string quality;
};
```

---

## Step 2 — Implement collectNoteChangeTicks

Implement a new function in `tools/batch_analyze.cpp` that collects every tick
at which any note attacks within the analysis range. This is the candidate
boundary pool.

```cpp
/// Returns all ticks within [startTick, endTick) at which any note in a
/// chord-bearing stave attacks (new onset). The result is sorted and
/// deduplicated. Always includes startTick.
static std::vector<Fraction>
collectNoteChangeTicks(const Score* score,
                       const Fraction& startTick,
                       const Fraction& endTick,
                       const std::set<size_t>& excludeStaves);
```

Implementation guide:
- Walk all Parts and Staves not in excludeStaves.
- For each staff, walk Segments of type SegmentType::ChordRest in [startTick, endTick).
- For each ChordRest that is a Chord (not a Rest), add its tick() to the result set.
- Sort and deduplicate. Always include startTick if not already present.
- Return as std::vector<Fraction>.

Do NOT include rest-only ticks. Do NOT include ticks from excludeStaves.

---

## Step 3 — Implement greedyExpandSegmentation stub

Add the main algorithm entry point. This iteration it is a STUB — it calls
`collectNoteChangeTicks` and wraps each adjacent pair as a PlacedRegion with
round=0 (unplaced candidate). Round 1 anchor selection is NOT implemented yet.

```cpp
/// Entry point for the replacement greedy-expand segmentation algorithm.
/// Currently returns all note-change-event regions as round=0 candidates.
/// Round 1 anchor selection will be added in Iter 52.
static std::vector<PlacedRegion>
greedyExpandSegmentation(const Score* score,
                         const Fraction& startTick,
                         const Fraction& endTick,
                         const std::set<size_t>& excludeStaves,
                         const ChordAnalyzerPreferences& prefs);
```

Implementation:
- Call `collectNoteChangeTicks` to get boundary ticks.
- For each adjacent pair [ticks[i], ticks[i+1]), create a PlacedRegion with
  startTick, endTick, round=0, confidence=0.0, isAnchor=false,
  reason="candidate — unplaced".
- Last region spans [ticks.back(), endTick).
- Return the vector.

---

## Step 4 — Add diagnostic reporting in analyzeScore

In `analyzeScore` in `tools/batch_analyze.cpp`, after the existing
`detectHarmonicBoundariesJaccard` call (do NOT remove it), add a parallel call
to `greedyExpandSegmentation` and log the comparison to stderr:

```cpp
// Iter 51 diagnostic: compare region counts
auto greedyCandidates = greedyExpandSegmentation(score, startTick, endTick,
                                                  excludeStaves, prefs);
fprintf(stderr, "[greedy-diag] %s: jaccard=%zu  greedy-candidates=%zu\n",
        score->title().toStdString().c_str(),
        jaccardBoundaries.size(),      // existing Jaccard boundaries vector
        greedyCandidates.size());
```

This must write to stderr ONLY so it does not corrupt the JSON stdout output
that `run_bach_preset.py` captures. Confirm this.

---

## Step 5 — Build and compile check

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
```

Fix any compile errors. The new code must compile cleanly with no warnings
in the new functions. Do NOT suppress warnings with casts; fix them.

---

## Step 6 — Run on a single chorale and report diagnostic output

```
cd C:\s\MS\ninja_build_rel && ./batch_analyze.exe \
    ../tools/corpus_src/bwv227.1.mscx /tmp/bwv227.1.diag.json \
    2>&1 | grep greedy-diag
```

(Adapt path to actual corpus source location — check tools/corpus_registry.json
for the correct source path for bwv227.1.)

Report:
- Jaccard region count for bwv227.1
- Greedy candidate count for bwv227.1
- Ratio (greedy / jaccard) — expect >> 1 (many more candidates than final regions)

---

## Step 7 — Run full corpus diagnostic

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque \
    --output-dir tools/corpus 2>&1 | grep greedy-diag | \
    python -c "
import sys, statistics
ratios = []
for line in sys.stdin:
    parts = line.split()
    j = int(parts[2].split('=')[1])
    g = int(parts[3].split('=')[1])
    ratios.append(g / j if j else 0)
print(f'Count: {len(ratios)}')
print(f'Mean greedy/jaccard ratio: {statistics.mean(ratios):.1f}')
print(f'Median: {statistics.median(ratios):.1f}')
print(f'Max: {max(ratios):.1f}')
"
```

Report the ratio distribution. This tells us how dense the candidate pool is
relative to the current segmentation.

---

## Step 8 — Confirm BIR baseline is unchanged

```
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Expected: BIR=true=21, BIR=false=128. The existing Jaccard path is untouched;
this must not change.

---

## Step 9 — Report to Cowork

```
PlacedRegion struct: defined at line N
collectNoteChangeTicks: defined at line N
greedyExpandSegmentation stub: defined at line N
Diagnostic reporting: added at line N in analyzeScore

Single chorale bwv227.1:
  Jaccard regions: N
  Greedy candidates: N
  Ratio: N.N×

Full corpus:
  Mean greedy/jaccard ratio: N.N×
  Median: N.N×
  Max: N.N×

BIR baseline: BIR=true=N  BIR=false=N  (must be 21/128)

Build: clean / warnings [list if any]
```
