# Recon: Three Paths Diverge on m285 Chord Identification

Date: 2026-04-26  
Scope: read-only analysis; no source edits.  
Chord: m285 — C4, F#4, A#4(Bb), D5; pcs={0,6,10,2}; key=C major  
Catalog symbol: `CTristan` (Tristan chord: root + TT + m7 + M9, no third)

---

## Observation

Three user-facing paths produce three distinct results for the same note at m285:

| Path | Result |
|---|---|
| Status bar | `Csus(add9)` |
| Right-click → Add chord symbol | `Cm7b5` (top item in submenu) |
| P2 annotation emitter | nothing (no symbol written to chord track) |

A fourth path — the catalog test, which calls `analyzeChord()` directly — returns
empty symbol and `Isus4` Roman numeral. That is not user-facing but explains why
m285 is a RealDiff entry.

---

## Q1 — Entry Points

**Status bar** (`harmonicAnnotation`, `notationcomposingbridge.cpp:481`)  
→ `analyzeNoteHarmonicContextDetails` (line 620)  
→ `analyzeHarmonicContextAtTick` (line 452)  
→ `analyzeHarmonicContextRegionallyAtTick` (P3, line 329) — tries first  
→ returns `NoteHarmonicContext.chordResults`; displays them pinning `[0]` (lines 511–519).

**Right-click → Add chord symbol** (`appendNoteAnalysisItems`,
`notationcontextmenumodel.cpp:196`)  
→ `analyzeNoteHarmonicContextDetails` (line 201 — **identical call**)  
→ same P3/P4 path; receives same `NoteHarmonicContext.chordResults`  
→ but `appendAnalysisItemsForContext` re-sorts the entire vector (lines 72–77).

**P2 annotation emitter** (`addHarmonicAnnotationsToSelection`,
`notationcomposingbridge.cpp:756` per `policy2_coalescing_map.md:Q2`)  
→ `analyzeSection()` over document selection  
→ per-region winner from `prepareUserFacingHarmonicRegions`  
→ **duration gate** applied (line 806–808) before writing to chord track.

**Catalog test** (`chordanalyzer_musicxml_tests.cpp:616`)  
→ `kAnalyzer.analyzeChord()` directly on isolated pitches + key=Cmaj  
→ `ChordSymbolFormatter::formatSymbol/Roman()` on that result  
→ NOT a user-facing path.

---

## Q2 — The Shared Data Structure

`NoteHarmonicContext.chordResults` (`std::vector<ChordAnalysisResult>`):

- `[0]` = region winner from `analyzeSection()` — the chord the per-region
  pipeline chose for the interval containing the tick.  Populated at
  `notationcomposingbridge.cpp:297`.
- `[1..]` = alternatives from `it->alternatives`, pushed at lines 298–299.

Both status bar and right-click receive the **same vector** from the same call to
`analyzeNoteHarmonicContextDetails`.  The divergence is entirely in what each
consumer does with it.

---

## Q3 — Why the status bar shows `Csus(add9)`

`harmonicAnnotation()` explicitly pins position 0:

```cpp
// notationcomposingbridge.cpp:511–519
// Sort alternatives by descending normalizedConfidence, keeping position 0
// (region winner) fixed so the top-level annotation is always the
// region-level result.
auto sortedResults = chordResults;
if (sortedResults.size() > 1) {
    std::sort(sortedResults.begin() + 1, sortedResults.end(), …);
}
```

The region winner (`chordResults[0]`) is `Csus(add9)`.  The sort only touches
`[1..]`, so `Csus(add9)` is always the first entry shown.

The regional analysis (`analyzeSection()` over a ~5-measure window) benefits from
surrounding context and accumulation — it infers a sus + added ninth interpretation
for the tritone + m7 + M9 pitch set.  The isolated `analyzeChord()` call (catalog
test) gets only the 4-note chord and falls to a sparse/unknown quality, explaining
the `''` symbol and `Isus4` Roman numeral there.

---

## Q4 — Why the right-click menu shows `Cm7b5` first

`appendAnalysisItemsForContext()` explicitly re-sorts **all** entries:

```cpp
// notationcontextmenumodel.cpp:67–77
// Sort a working copy by descending score so the highest-scoring candidate
// appears first in the submenu.  The chordResults vector may have a
// region-winner prepended at position 0 (potentially lower-scoring than the
// fresh display analysis)…
auto analysisResults = context.chordResults;
std::sort(analysisResults.begin(), analysisResults.end(),
          [](…a, …b) { return a.identity.normalizedConfidence > b.identity.normalizedConfidence; });
```

The comment is explicit: the region winner at `[0]` can have **lower**
`normalizedConfidence` than an alternative.  For m285, the alternative `Cm7b5` has
a higher normalizedConfidence (the analyzer finds a stronger b5 + m7 template
match) and therefore floats to the top of the re-sorted submenu.

This means a user looking at the status bar sees `Csus(add9)` as the primary
result, then opens the right-click menu and sees `Cm7b5` as the recommended symbol
to add — a discrepancy that is **not** a data inconsistency but a display policy
mismatch.

---

## Q5 — Why the P2 annotation emitter writes nothing

P2 applies the `minimumDisplayDurationBeats` gate (default 0.5 beats,
`composingconfiguration.cpp:158`) before writing any annotation:

```cpp
// notationcomposingbridge.cpp:805–808
// Divergence-C minimum duration gate.
if (minDurationTicks > 0
    && (region.endTick - region.startTick) < minDurationTicks) {
    continue;
}
```

The Tristan chord at m285 in the catalog MusicXML is a short chord (< 0.5 beats).
P2 skips it silently.  P3 has no such gate — the same chord visible in the status
bar is suppressed in the annotation output.  This is **Divergence C** as catalogued
in `docs/policy2_coalescing_map.md:Q3`.

---

## Q6 — Classification and Fix Shape

### Divergence E (new) — presentation sort mismatch between status bar and right-click

**Type: β (presentation)**  
Same `chordResults` data, different sort policy:

| Surface | Sort policy | First shown |
|---|---|---|
| Status bar | Pin `[0]` (region winner); sort `[1..]` by confidence | `Csus(add9)` |
| Right-click submenu | Sort ALL by confidence; region winner may float down | `Cm7b5` |

The discrepancy is intentional per the comments in both consumers, but creates a
jarring user experience: the "top" symbol on the status bar differs from the top
item offered in "Add chord symbol".

**Fix shape:** Align on a single display policy.  Options:
- *Option A*: status bar adopts the full-sort policy (highest confidence = primary).
  Simpler, removes the explicit pin in `harmonicAnnotation()`.
- *Option B*: right-click adopts the pin-`[0]` policy, showing region winner first.
  Preserves the structural significance of the region winner.
- *Option C*: surface the conflict to the user by labeling the status bar result
  "structural" and the right-click alternative list as "by confidence".

No code change is made here; fix is a follow-up decision.

---

### Divergence C — P2 duration gate vs. P1/P3 no gate (live, pre-existing)

**Type: α (structural)** — P2 has a filter that P1/P3 do not.

`minimumDisplayDurationBeats = 0.5` beats by default.  For m285, this means the
annotation emitter silently skips the Tristan chord while the status bar and
right-click present results.  Documented in `policy2_coalescing_map.md:Q3/Divergence C`.

**Fix shape (from policy2 doc):** Resolution is a follow-up decision.  The gate
prevents visual noise from fast passing chords; removing it would increase
annotation density significantly for ornamented scores.  An alternative is a per-
region override or user preference toggle already captured in the backlog.

---

## Summary

The three observed results stem from two independent divergences:

| # | Between | Cause | Classification |
|---|---|---|---|
| E | Status bar vs. right-click | Sort policy: pin-`[0]` vs. sort-all | β (presentation) |
| C | P2 annotation vs. P3/status-bar | Duration gate in P2 | α (structural) |

The divergence is **not** caused by different analysis pipelines reaching different
intermediate conclusions for the same note: status bar and right-click both call
`analyzeNoteHarmonicContextDetails()` and receive the identical `chordResults`
vector.  The branching happens entirely at the display layer.

The fourth observation (catalog test `analyzer=''`) is explained by the test
calling `analyzeChord()` in isolation, without the regional window that gives
P3/P4 the surrounding context needed to stabilize the Tristan chord as `Csus(add9)`.
