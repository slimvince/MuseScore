# Iteration 53: Replacement segmentation — Round 2 gap filling

## Standing rule — no symbol inference

**No chord symbol string parsing. No Roman numeral inference. Structured fields only.**

Read `C:\s\MS\CLAUDE.md` and `C:\s\MS\build_and_test.md` first.
Baselines: BIR=true=21, BIR=false=128. Jazz BIR=false=20.

Build fresh before every BIR measurement. Verify binary is newer than source.

---

## Background

After Round 1, each chorale has ~18 anchors covering ~49% of Jaccard regions.
Round 2 fills the gaps between anchors using the anchor chord identities as
bilateral context — a key architectural advantage over the current single-pass
Jaccard approach.

A gap is the span between two consecutive placed regions (anchor or earlier round).
Within each gap, Round 2 evaluates every candidate region and promotes those
that are harmonically distinct and above a confidence threshold.

Still diagnostic only. Existing `detectHarmonicBoundariesJaccard` is untouched.
BIR must remain 21/128.

---

## Step 1 — Add a gap-fill helper

Add `fillGap` — evaluates all candidate regions within a gap and promotes those
that qualify. Operates in-place on the PlacedRegion vector.

```cpp
/// Promotes candidate regions within [gapStart, gapEnd) to round `targetRound`
/// if they are harmonically distinct from their neighbours and score above
/// kRound2MinScore. Processes candidates in descending score order within the gap,
/// updating the neighbourhood as each promotion occurs.
///
/// leftAnchor / rightAnchor: the bounding placed regions (may be nullptr at
/// score edges). Used to seed temporal context.
static void fillGap(std::vector<PlacedRegion>& regions,
                    int gapStartTick,
                    int gapEndTick,
                    const PlacedRegion* leftAnchor,
                    const PlacedRegion* rightAnchor,
                    int targetRound,
                    const Score* score,
                    const std::set<size_t>& excludeStaves,
                    const ChordAnalyzerPreferences& prefs,
                    analysis::IChordAnalyzer* chordAnalyzer,
                    int globalKeyFifths,
                    KeySigMode globalKeyMode);
```

Implementation:

1. Collect all candidate regions (round==0) with startTick in [gapStartTick, gapEndTick).
   Sort by analyzeChord winner score descending — score each with bilateral anchor
   context (previousRootPc from leftAnchor, nextRootPc from rightAnchor; nullptr
   anchors leave those fields at -1 / unknown).

2. Maintain a sorted list of "current neighbours" initialised with leftAnchor and
   rightAnchor. After each promotion this list grows.

3. For each candidate (highest score first):
   a. Find its current left-neighbour (largest placed startTick < candidate.startTick)
      and right-neighbour (smallest placed startTick > candidate.startTick) in the
      current-neighbours list.
   b. Check harmonic distinctness: candidate rootPitchClass differs from left-neighbour
      rootPitchClass OR candidate quality differs from left-neighbour quality, AND
      same check vs right-neighbour. Skip if identical to both.
   c. Check score ≥ kRound2MinScore (initial value: 1.0).
   d. If both checks pass: promote — set round=targetRound, populate confidence,
      rootPitchClass, quality, reason ("Round N fill: distinct from L(root=X) and
      R(root=Y) score=Z"), add to current-neighbours list.

4. Re-score step (important): after collecting the initial score order in step 1,
   re-run analyzeChord for each promoted candidate with UPDATED context (using
   actual placed neighbours rather than original anchor context). Update confidence
   and rootPitchClass/quality from the re-scored result.

Note: step 4 may change which chord wins for a candidate if the updated temporal
context differs from the initial bilateral anchor context. This is expected and
correct — the algorithm refines its estimates as more chords are placed.

---

## Step 2 — Add Round 2 constant

```cpp
static constexpr double kRound2MinScore = 1.0;
```

---

## Step 3 — Call fillGap from greedyExpandSegmentation

After Round 1 completes, add Round 2:

```cpp
// Round 2 — fill gaps between Round 1 anchors
// Collect placed regions sorted by startTick
std::vector<PlacedRegion*> placed;
for (auto& r : regions)
    if (r.round >= 1) placed.push_back(&r);
std::sort(placed.begin(), placed.end(),
    [](const PlacedRegion* a, const PlacedRegion* b){
        return a->startTick < b->startTick; });

// Fill gap before first anchor
if (!placed.empty() && placed.front()->startTick > startTick.ticks())
    fillGap(regions, startTick.ticks(), placed.front()->startTick,
            nullptr, placed.front(), 2, score, excludeStaves, prefs,
            chordAnalyzer, globalKeyFifths, globalKeyMode);

// Fill gaps between consecutive placed regions
for (size_t i = 0; i + 1 < placed.size(); ++i)
    if (placed[i]->endTick < placed[i+1]->startTick)
        fillGap(regions, placed[i]->endTick, placed[i+1]->startTick,
                placed[i], placed[i+1], 2, score, excludeStaves, prefs,
                chordAnalyzer, globalKeyFifths, globalKeyMode);

// Fill gap after last anchor
if (!placed.empty() && placed.back()->endTick < endTick.ticks())
    fillGap(regions, placed.back()->endTick, endTick.ticks(),
            placed.back(), nullptr, 2, score, excludeStaves, prefs,
            chordAnalyzer, globalKeyFifths, globalKeyMode);
```

---

## Step 4 — Update diagnostic reporting

Extend the diagnostic line to report per-round counts:

```cpp
int r1 = std::count_if(regions.begin(), regions.end(),
    [](const PlacedRegion& r){ return r.round == 1; });
int r2 = std::count_if(regions.begin(), regions.end(),
    [](const PlacedRegion& r){ return r.round == 2; });
int unplaced = std::count_if(regions.begin(), regions.end(),
    [](const PlacedRegion& r){ return r.round == 0; });
fprintf(stderr,
    "[greedy-diag] %s: jaccard=%zu candidates=%zu r1=%d r2=%d "
    "placed=%d unplaced=%d ratio=%.2f\n",
    score->title().toStdString().c_str(),
    jaccardBoundaries.size(), regions.size(),
    r1, r2, r1+r2, unplaced,
    jaccardBoundaries.size() > 0
        ? (double)(r1+r2) / (double)jaccardBoundaries.size() : 0.0);
```

---

## Step 5 — Build and run corpus diagnostic

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque \
    --output-dir tools/corpus --diag-out /tmp/iter53_diag.log
```

Parse and report:
```python
import statistics, re
from pathlib import Path

lines = [l for l in Path('/tmp/iter53_diag.log').read_text().splitlines()
         if '[greedy-diag]' in l]

r1s, r2s, placed, unplaced, ratios, jaccard = [], [], [], [], [], []
for l in lines:
    j   = int(re.search(r'jaccard=(\d+)', l).group(1))
    r1  = int(re.search(r'r1=(\d+)', l).group(1))
    r2  = int(re.search(r'r2=(\d+)', l).group(1))
    u   = int(re.search(r'unplaced=(\d+)', l).group(1))
    rat = float(re.search(r'ratio=([\d.]+)', l).group(1))
    r1s.append(r1); r2s.append(r2)
    placed.append(r1+r2); unplaced.append(u); ratios.append(rat); jaccard.append(j)

print(f'Chorales: {len(r1s)}')
print(f'Mean Jaccard regions:      {statistics.mean(jaccard):.1f}')
print(f'Mean Round 1 anchors:      {statistics.mean(r1s):.1f}')
print(f'Mean Round 2 placed:       {statistics.mean(r2s):.1f}')
print(f'Mean total placed (R1+R2): {statistics.mean(placed):.1f}')
print(f'Mean unplaced (round=0):   {statistics.mean(unplaced):.1f}')
print(f'Mean placed/jaccard ratio: {statistics.mean(ratios):.2f}')
print(f'Median placed/jaccard:     {statistics.median(ratios):.2f}')
under = sum(1 for r in ratios if r < 0.7)
over  = sum(1 for r in ratios if r > 1.5)
print(f'Chorales placed/jaccard < 0.7: {under}')
print(f'Chorales placed/jaccard > 1.5: {over}')
```

**Interpret placed/jaccard ratio after R1+R2:**
- Mean ~0.8–1.2: algorithm is converging toward Jaccard's region count. Good.
  Remaining unplaced candidates are likely passing chords — correctly filtered.
- Mean < 0.7: under-placing — lower kRound2MinScore to 0.75 and retest.
- Mean > 1.5: over-placing — raise kRound2MinScore to 1.25 and retest.

---

## Step 6 — Confirm BIR baseline unchanged

```
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Expected: BIR=true=21, BIR=false=128.

---

## Step 7 — Report to Cowork

```
Build: clean / warnings [list if new]

Round 2 parameters: kRound2MinScore=N

Corpus results (353 chorales):
  Mean Jaccard regions:          N
  Mean Round 1 anchors:          N
  Mean Round 2 filled:           N
  Mean total placed (R1+R2):     N
  Mean unplaced (round=0):       N
  Mean placed/jaccard ratio:     N  (target: 0.8–1.2)
  Median placed/jaccard ratio:   N
  Chorales placed/jaccard < 0.7: N
  Chorales placed/jaccard > 1.5: N

Interpretation: [under-placing / converging / over-placing]
Parameter adjustment needed: [yes — describe / no]

BIR baseline: BIR=true=N  BIR=false=N  (must be 21/128)
```
