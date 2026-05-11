# Iteration 52: Replacement segmentation — Round 1 anchor selection

## Standing rule — no symbol inference

**No chord symbol string parsing. No Roman numeral inference. Structured fields only.**

Read `C:\s\MS\CLAUDE.md` and `C:\s\MS\build_and_test.md` first.
Baselines: BIR=true=21, BIR=false=128. Jazz BIR=false=20.

Build fresh before every BIR measurement. Verify binary is newer than source.

---

## Background

Iter 51 produced a dense candidate pool (mean 2.91× Jaccard count). This iteration
implements Round 1 of greedy-expand: selecting high-confidence structural anchors
from that pool.

A Round 1 anchor is a candidate region that satisfies ALL of:
1. **Beat position**: onset tick falls on a beat (quarter-note grid relative to
   measure start — time-signature-aware improvement deferred to later).
2. **Duration**: span ≥ 2 × DIVISION ticks (half note or longer).
3. **Voice participation**: ≥ 3 distinct chord-bearing staves have notes sounding.
4. **Chord confidence**: `analyzeChord` winner score ≥ `kAnchorMinScore` (initial
   value: 2.0 — tune if needed based on corpus data in Step 5).

All four criteria must hold. A region failing any one is NOT an anchor in Round 1
(it may be placed in Round 2+).

Still diagnostic only: existing `detectHarmonicBoundariesJaccard` is untouched.
No BIR change expected. No JSON output changes.

Do NOT modify any scoring code. Do NOT modify the bridge path.

---

## Step 1 — Add beat-position helper

Add a helper function (before `greedyExpandSegmentation`) that tests whether a tick
falls on a beat boundary:

```cpp
/// Returns true if tick falls on a quarter-note beat boundary within its measure.
/// Uses the score's time signature at that tick.
/// Quarter-note grid is used for all time signatures for now; beat-synchronous
/// refinement is deferred (Task #59 superseded by Task #62).
static bool isOnBeat(const Score* score, const Fraction& tick) {
    // Get the measure containing tick
    const Measure* m = score->tick2measure(tick);
    if (!m) return false;
    // Offset within the measure in ticks
    const Fraction offset = tick - m->tick();
    // On beat if offset is a multiple of DIVISION (one quarter note)
    return (offset.ticks() % Constants::DIVISION) == 0;
}
```

---

## Step 2 — Add voice-participation helper

Add a helper that counts distinct chord-bearing staves with at least one sounding
note at a given tick range:

```cpp
/// Returns the number of distinct chord-bearing staves that have at least one
/// non-rest, non-grace note sounding anywhere in [startTick, endTick).
static int countParticipatingStaves(const Score* score,
                                    const Fraction& startTick,
                                    const Fraction& endTick,
                                    const std::set<size_t>& excludeStaves);
```

Implementation: walk all staves not in excludeStaves; for each staff, check
whether any Chord (not Rest) has a tick in [startTick, endTick) or a note
that was attacked before startTick and lasts into the region. Count staves
with at least one qualifying note.

---

## Step 3 — Extend greedyExpandSegmentation for Round 1

Extend the function signature to accept the analysis infrastructure needed for
scoring candidates:

```cpp
static std::vector<PlacedRegion>
greedyExpandSegmentation(const Score* score,
                         const Fraction& startTick,
                         const Fraction& endTick,
                         const std::set<size_t>& excludeStaves,
                         const ChordAnalyzerPreferences& prefs,
                         analysis::IChordAnalyzer* chordAnalyzer,
                         int globalKeyFifths,
                         KeyMode globalKeyMode);
```

Inside the function, after generating all round=0 candidates, implement Round 1:

For each candidate region:
1. Check `isOnBeat(score, Fraction(region.startTick))`.
2. Check `(region.endTick - region.startTick) >= 2 * Constants::DIVISION`.
3. Check `countParticipatingStaves(...) >= 3`.
4. If all three pass: call `collectRegionTones(score, startTick, endTick,
   excludeStaves)` to get tones, then `chordAnalyzer->analyzeChord(tones,
   globalKeyFifths, globalKeyMode, nullptr, prefs)` (nullptr for ctx — no
   temporal context in Round 1; anchors are self-contained).
5. If winner score ≥ `kAnchorMinScore` (2.0): mark the region:
   - `round = 1`
   - `isAnchor = true`
   - `confidence = candidates[0].identity.score`
   - `rootPitchClass = candidates[0].identity.rootPitchClass`
   - `bassPitchClass = candidates[0].identity.bassPitchClass`
   - `quality = qualityToString(candidates[0].identity.quality)` (use existing
     helper or write a small one)
   - `reason = "Round 1 anchor: beat=" + beatStr + " dur≥half voice≥3 score="
     + scoreStr`

Add at the top of the file:
```cpp
static constexpr double kAnchorMinScore = 2.0;
```

---

## Step 4 — Update diagnostic reporting

Update the diagnostic `fprintf` in `analyzeScore` to also report anchor count:

```cpp
int anchorCount = std::count_if(greedyCandidates.begin(), greedyCandidates.end(),
    [](const PlacedRegion& r){ return r.isAnchor; });
fprintf(stderr,
    "[greedy-diag] %s: jaccard=%zu  candidates=%zu  anchors=%d  ratio=%.2f\n",
    score->title().toStdString().c_str(),
    jaccardBoundaries.size(),
    greedyCandidates.size(),
    anchorCount,
    jaccardBoundaries.size() > 0
        ? (double)anchorCount / (double)jaccardBoundaries.size() : 0.0);
```

---

## Step 5 — Build and run corpus diagnostic

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
```

Run corpus with diagnostic capture:
```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque \
    --output-dir tools/corpus --diag-out /tmp/iter52_diag.log
```

Parse the diagnostic log:
```python
import statistics, re
from pathlib import Path

lines = Path('/tmp/iter52_diag.log').read_text().splitlines()
lines = [l for l in lines if '[greedy-diag]' in l]

jaccard, candidates, anchors, ratios = [], [], [], []
for l in lines:
    j = int(re.search(r'jaccard=(\d+)', l).group(1))
    c = int(re.search(r'candidates=(\d+)', l).group(1))
    a = int(re.search(r'anchors=(\d+)', l).group(1))
    r = float(re.search(r'ratio=([\d.]+)', l).group(1))
    jaccard.append(j); candidates.append(c)
    anchors.append(a); ratios.append(r)

print(f'Chorales: {len(jaccard)}')
print(f'Mean Jaccard regions:  {statistics.mean(jaccard):.1f}')
print(f'Mean greedy candidates:{statistics.mean(candidates):.1f}')
print(f'Mean Round 1 anchors:  {statistics.mean(anchors):.1f}')
print(f'Mean anchor/jaccard:   {statistics.mean(ratios):.2f}')
print(f'Median anchor/jaccard: {statistics.median(ratios):.2f}')
under = sum(1 for r in ratios if r < 0.5)
over  = sum(1 for r in ratios if r > 2.0)
print(f'Anchors < 50% of Jaccard: {under}')
print(f'Anchors > 200% of Jaccard: {over}')
```

**Interpret the anchor/jaccard ratio:**
- Mean ~0.6–0.9: Round 1 is selective but not too sparse — good starting point.
  Gaps between anchors will be filled by Round 2+.
- Mean < 0.4: Criteria too strict — too few anchors, Round 2+ has too much to fill.
  Consider relaxing duration threshold to 1×DIVISION or min-score to 1.5.
- Mean > 1.5: Criteria too loose — Round 1 is not much more selective than Jaccard.
  Consider tightening min-score or requiring all 4 voices.

**If mean anchor/jaccard < 0.4**, retest with `kAnchorMinScore = 1.5` and
duration ≥ 1×DIVISION. Report both configurations.

---

## Step 6 — Confirm BIR baseline unchanged

```
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Expected: BIR=true=21, BIR=false=128.

---

## Step 7 — Report to Cowork

```
Build: clean / warnings [list]

Round 1 parameters used:
  kAnchorMinScore: N
  Min duration: N × DIVISION
  Min voices: N

Corpus results (353 chorales):
  Mean Jaccard regions:   N
  Mean greedy candidates: N
  Mean Round 1 anchors:   N
  Mean anchor/jaccard ratio: N  (target: 0.6–0.9)
  Median anchor/jaccard ratio: N
  Chorales with < 50% of Jaccard anchors: N
  Chorales with > 200% of Jaccard anchors: N

Interpretation: [too sparse / good / too dense]
Parameter adjustment needed: [yes — describe / no]

BIR baseline: BIR=true=N  BIR=false=N  (must be 21/128)
```
