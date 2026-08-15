# Layer 2 — CHANGE-POINT SLICING — READ-ONLY AUDIT DOSSIER

> **Status: read-only audit (no code, no behavior change, no production commit).** Verifies the `[verify]` items of
> `cowork_layer2_slicing_design.md` §3 at source, sizes the onset+offset slicing on the real corpus, and specifies
> the deterministic slicer test cases. Cowork verifies the citations at source and that nothing production changed;
> user ratifies; THEN the impl design.
>
> **No-assume rule:** every as-is statement cites `file:line` from a source read this session. Items not confirmable
> at source are marked **[unverified]**. Where the signed design's §3 paraphrase differs from the exact code, the
> dossier records the **exact criterion** and flags the discrepancy (the design asked for "the exact criterion, not
> a paraphrase").

---

## §1 — The as-is map (what layer 2 retires), verified at source

All paths under `src/composing/`. Read this session: `harmony/harmonicsegmenter.cpp`, `region/regionanalyzer.cpp`,
`engravingbridge/regiontoneprimitives.cpp`, `engravingbridge/regiontonecollector.h`, `notemodel/note_model.{h,cpp}`,
`scoreharvest/metricweights.h`.

### 1.0 — ★ Headline correction to the design's §3 framing (verified)
The signed design §3 says the coarse stage is *"`greedyExpandSegmentation` … + `denseBoundaryTicks` — a
**Jaccard/greedy expansion over weighted tone evidence**."* **At source this is imprecise on three points:**

1. **`greedyExpandSegmentation` contains no Jaccard and no "expansion" of boundaries.** Its candidate grid is the
   **fixed onset+release change-tick set** from `collectNoteChangeTicks` (harmonicsegmenter.cpp:577), and it then
   **selects** a subset of those ticks by **`analyzeChord` SCORE thresholds** (Round 1 anchoring + Round 2 gap
   fill), not by Jaccard. The only Jaccard in the segmentation machinery is in **`detectOnsetSubBoundaries`**
   (Pass 2), a different function. (harmonicsegmenter.cpp:565–927; no `jaccard` token in the function.)
2. **`denseBoundaryTicks` is NOT part of the coarse seed.** It is a **separate granularity mode**, reached **only**
   when `opts.granularity == PreserveAllChanges` (regionanalyzer.cpp:540–541); the default / `Smoothed` path uses
   `greedyExpandSegmentation` (regionanalyzer.cpp:551) and **never calls** `denseBoundaryTicks`.
3. **★ The onset+offset "salami slice" already exists as a FACT in the codebase** — `collectNoteChangeTicks`
   (harmonicsegmenter.cpp:151–315) already builds boundaries at every note ONSET *and* every note RELEASE, citing
   the same Pardo & Birmingham (CMJ 2002) / music21-chordify principle the layer-2 design adopts. **The fact is not
   new; what is new is keeping it as the output instead of immediately collapsing it by judgment.** Layer 2
   extracts this grid (re-derived over the note model) and stops; the old pipeline feeds it into score-gated
   selection + merge. This *strengthens* the design's thesis (§4.5: the judgment is bolted onto an
   already-existing fact) and should be reflected in the impl design as "promote the existing change-tick fact, drop
   the selection/merge."

### 1.1 — `greedyExpandSegmentation` — the coarse-boundary criterion (exact)
**`harmonicsegmenter.cpp:565–927`** (declared `harmonicsegmenter.h`). Fed the weighted-PC callback: confirmed at
**regionanalyzer.cpp:548–550** — `segCallbacks.collectRegionTones = weightedPcView(noteModel, s, e, …)` — and
`staffIsEligible` at regionanalyzer.cpp:544–546.

Exact flow:
- **Candidate grid** = `collectNoteChangeTicks(score, startTick, endTick, …)` (harmonicsegmenter.cpp:577): the
  sorted-unique union of every onset tick (a note with `play() && visible() && !tieBack()`,
  harmonicsegmenter.cpp:190–205) **and** every interior release tick (a chord with a playing note that does **not**
  `tieFor()`, harmonicsegmenter.cpp:241–259), with mid-tuplet ticks snapped to the enclosing tuplet start
  (harmonicsegmenter.cpp:264–307). Always includes `startTick`.
- **Round 1 anchoring** (harmonicsegmenter.cpp:683–755): a candidate `[t_i, t_{i+1})` is promoted to an anchor iff
  **all four** hold — (a) on a quarter-note beat boundary `isOnBeat` (harmonicsegmenter.cpp:712, defn :81–88:
  `(tick − measureTick) % DIVISION == 0`); (b) duration ≥ `effectiveAnchorMinDurationTicks` (:715); (c)
  participating chord-staves ≥ `effectiveStaveThreshold` (:718–719); (d) `analyzeChord` winner score ≥
  `effectiveAnchorMinScore` (:736). All four thresholds are **texture-adaptive** (Iter 69), derived per-score from
  mean active staves + mean tick spacing (harmonicsegmenter.cpp:583–664); SATB self-calibrates to the legacy
  constants (3-staff gate, 1.5 score, 1·DIVISION duration).
- **Round 2 gap fill** (`fillGap`, harmonicsegmenter.cpp:323–561; called :768–787): promotes the
  highest-scoring round-0 candidate in each inter-anchor gap whose chord identity is **distinct** from both bilateral
  anchors and clears `effectiveRound2MinScore`, with a true-local re-analysis to defeat tonic-smearing
  (:452–475) and a local-evidence preference on long gaps (:506–560).
- **Head / tail-gap synthesis** (harmonicsegmenter.cpp:789–924): if Round 1+2 left the window head/tail uncovered,
  synthesize one covering region (with a key-tonic prior in the head, :830–879).
- **Stop condition:** NOT iterate-to-convergence — it is exactly Round 1 → Round 2 gap-fill → head/tail synthesis,
  once. The emitted **coarse boundaries** are the **union of every placed region's start AND end tick**
  (regionanalyzer.cpp:556–569, Iter 77 Fix B).

So the coarse "criterion" is **chord-score-gated selection from a fixed onset+release grid**, not Jaccard expansion.

### 1.2 — `denseBoundaryTicks` — what it computes and seeds (exact)
**`regionanalyzer.cpp:271–309`.** Seeds `boundaries = { startTick }` (:280), then walks ChordRest segments
`firstSeg → next1(ChordRest)` while `tick < endTick`; at each segment computes the **12-bit octave-folded
pitch-class mask** of the sounding set via `ebr::soundingAt(noteModel, segTick, …)` (:288, a note-model view), and
**emits a boundary when the mask differs from the previous non-empty segment's mask** (:301–305). Empty segments are
skipped (:289–290). **Used only on the `PreserveAllChanges` path** (regionanalyzer.cpp:540–541); the default
`Smoothed`/coarse path never invokes it. It is the closest existing cousin to the layer-2 slicer but differs on
three axes the design must keep in view: (i) it compares **pitch-class** masks (octave-folded), not the
sounding-**note** set; (ii) it samples **only at segment ticks**, so a release that falls between segments is not a
boundary; (iii) it is gated to one non-default granularity. **[unverified]** which granularity the live notation
bridge requests by default — `AnalyzeRegionsOptions::granularity`'s default and the bridge's choice were not read
this session (not needed for the slicer spec; flagged for the retirement plan).

### 1.3 — `detectOnsetSubBoundaries` — onset-PC Jaccard threshold + min-gap (exact)
**`regiontoneprimitives.cpp:202–291`** (decl `regiontonecollector.h:186–191`, **default `threshold = 0.25`**).
Per ChordRest segment, builds the onset-only PC mask — notes with `cr->tick() == segTick` (true onset, not a
sustain), `!isGrace`, `play() && visible()` (:243–253). Between consecutive **non-empty** onset windows computes
**Jaccard distance** `1 − |A∩B| / |A∪B|` (:278–280) and fires a sub-boundary iff
**`jaccard ≥ threshold` AND `gapTicks ≥ minGapTicks`** (:283), where **`minGapTicks = 2 · DIVISION`** (:267, hard-
coded). In the live pipeline the threshold is `opts.onsetBoundaryThreshold` (regionanalyzer.cpp:771–772), whose
struct default is **0.25** (regionanalyzer.h:88). Returns sub-boundary ticks, excluding `startTick`.

### 1.4 — `detectBassMovementSubBoundaries` — bass-PC-change criterion + Pass-2b eligibility (exact)
**`regiontoneprimitives.cpp:293–372`** (decl `regiontonecollector.h:199–204`, **default
`minGapTicks = 2·DIVISION`**). Per segment, tracks the **lowest-pitch** playing/visible onset note as the bass PC
(:339–343, onset-only via `cr->tick()==segTick` :332). Fires a sub-boundary iff **`curPC != lastBoundaryBassPC`
AND `gapTicks ≥ minGapTicks`** (:364) — "ANY bass PC change fires; no minimum-interval threshold" (header :197).
Called from Pass 2b with the default min-gap (regionanalyzer.cpp:977, 4-arg call → `2·DIVISION`).

Two **distinct** constants the design §3.4 collapsed into one — keep them separate:
- **Pass-2b parent ELIGIBILITY:** `kPass2bMinRegionTicks = 4 · DIVISION` (metricweights.h:69; gate at
  regionanalyzer.cpp:956, 970 — a parent shorter than 4 quarters is not subdivided).
- **Detector MIN-GAP between accepted boundaries:** `2 · DIVISION` (regiontonecollector.h:204) — a different value.
The §3.4 phrase "`kPass2bMinRegionTicks` eligibility (4·DIVISION)" names the **parent eligibility** correctly;
the detector's own gap floor is the separate 2·DIVISION default. (Pass 2's analogous parent gate is
`kPass2MinRegionTicks = 4·DIVISION`, regionanalyzer.cpp:60, 764.)

### 1.5 — Pass orchestration (exact, `analyzeRegions`, regionanalyzer.cpp:483–1181)
1. **Note model built once:** `NoteModel::build(score)` (regionanalyzer.cpp:508) — every tone below is a view over it.
2. **Pass 1 — coarse boundaries** (:538–573): `PreserveAllChanges` → `denseBoundaryTicks` (:541); else →
   `greedyExpandSegmentation` then placed-region start+end ticks (:551–569). Each coarse region is analyzed into a
   `HarmonicRegion` by the `runPass1` lambda (:588–748, invoked :750; sparse-admission retry :751–754).
3. **Pass 2 — onset-Jaccard sub-boundaries** (:756–952): for each parent ≥ `kPass2MinRegionTicks` (:764),
   `detectOnsetSubBoundaries` (:771), analyze each sub. **Skipped** on `PreserveAllChanges` (:757).
4. **Pass 2b — iterative bass-movement sub-boundaries** (:954–1143): `while(anyNewSplit && passCount <
   kMaxBassMovementPasses)` (`kMaxBassMovementPasses = 8` at regionanalyzer.cpp:61; loop :960), parents ≥ `kPass2bMinRegionTicks`
   (:970), `detectBassMovementSubBoundaries` (:977). **Skipped** on `PreserveAllChanges` (:955).
5. **Pass 3 — merge** (:1149–1153): **only when `granularity == Smoothed`** — `coalesceShortSameRootRuns` then
   `absorbShortRegions`. Then `restampBassMinorSeventhAfterMerge` (:1156) and `backfillNextRootPc` (:1159), and
   (if `jointKeyWiringEnabled()`, default OFF) the J-key re-key pass (:1166–1169).

Confirmed orchestration matches the design's Pass-1 → Pass-2 → Pass-2b → Pass-3 claim, **with the refinement** that
Pass 3 (merge) runs **only on `Smoothed`**, and `PreserveAllChanges` skips Passes 2/2b/3 entirely.

### 1.6 — The merge: chord-dependent + mutates region tones (the §4.4 defect, exact)
Three distinct operations; the §4.4 statement ("chord-dependent and mutates region tones") is accurate for two of
them and **not** the third — recorded precisely so the retirement plan does not over- or under-scope:

- **`tryCollapseSameChordRegion`** (regionanalyzer.cpp:167–187) — **the anchor's stale-chord seam.** Collapses a
  candidate into the back region iff **contiguous AND same `rootPc` AND same `quality`** (:173–177) — chord-
  dependent — then **mutates** the back region: extends `endTick` (:180), **merges tones**
  `mergeChordAnalysisTones(regions.back().tones, newTones)` (:181), and **recomputes the bass** from the merged
  tones (:182–185). Invoked in **Pass 1** (:732) and **Pass 2** (:935). This is the merge whose tone-mutation
  produces the stale-chord seam (roadmap 0.6, cited at :166).
- **`coalesceShortSameRootRuns`** (regionanalyzer.cpp:74–153, Pass 3) — chord-dependent (keys on `rootPc`
  :90/:97/:107), **mutates tones** (`mergeChordAnalysisTones` :139) and recomputes bass (:141–144); the combined
  region **inherits the longest sub-region's chord identity** (:134) — a chord-dependent identity decision baked
  into segmentation.
- **`absorbShortRegions`** (regionanalyzer.cpp:197–214, Pass 3) — **NOT** chord-dependent and does **NOT** mutate
  tones: absorbs any region `< kMinRegionTicks` into its predecessor purely by **duration**, extending `endTick`
  only (:206–210). (Recorded so the retirement plan treats it as a pure short-region coalescer → maps cleanly to
  layer-N cosmetic grouping, distinct from the two tone-mutating merges.)

**Net (§4.4 confirmed):** analysis-time segmentation mutates region tone sets via chord-identity-dependent merges
(`tryCollapseSameChordRegion`, `coalesceShortSameRootRuns`) — the irreversible "decide spans → mutate evidence →
analyze" coupling the target removes. The deterministic slicer carries no analysis, no merge, no tone mutation.

---

## §2 — Onset+offset slicing characterized on real scores (sizing + the two §7 sub-questions)

**Method — read-only music21 proxy (no production code touched).** A throwaway diagnostic at
`C:\tmp\l2_slice_probe.py` (outside the repo tree; **not** in the production pipeline, **not** wired into
`regionanalyzer`; delete-or-keep-as-marked) implements the §5 boundary definition **directly**: parse →
`stripTies()` (== the note model's tie resolution, one span per tied group) → boundary grid = sorted-unique union of
every note **onset** and every note **release** (ticks, DIVISION=480); slices = consecutive boundary pairs with a
non-empty sounding set. Grace/zero-length events are excluded from the grid (== design "grace = annotation, not a
boundary") and counted separately. **Proxy caveats (stated, not hidden):** music21 is a *proxy* for the C++ note
model, not the model itself; absolute counts may differ by a few percent (offset/voice handling), but the
**structural** findings are robust. No staff-eligibility filtering is applied — irrelevant here (the corpus has no
chord-track/drumset/hidden staves). The probe was validated on bwv261: all its release-only ticks are phrase-end
breaths whose post-release sounding set is **empty** (correctly opening no slice) — confirming the probe is not
miscounting mid-span releases.

**Corpus:** the full canonical `tools/corpus/*.xml` — **353 Bach chorale stems + corelli** (5,582 measures). A
named 15-stem readout (`bwv269, bwv301, bwv245.15, bwv102.7, bwv10.7, bwv57.8, bwv64.8, bwv244.32, bwv122.6,
bwv14.5, bwv261, bwv40.3, bwv421, bwv432, bwv96.6`) corroborates the aggregate.

### (a) Slice-count density (sizes the L3 per-slice analysis cost — the §7 performance question)
| Metric | Full corpus (353 + corelli) |
|---|---|
| Total slices (onset+offset, non-empty) | **29,045** |
| Total measures | 5,582 |
| **Mean slices / measure** | **5.2** (per-stem range ≈ **3.0 – 8.6**) |
| Per-stem slice count | ≈ **49 – 391** (min `bwv96.6`/`bwv122.6` 49; max `bwv328` 391) |
| Onset-only slices (the rejected lean) | 28,690 |
| **Onset+offset vs onset-only** | **+1.2 %** more slices |

The candidate grid is **O(onsets) ≈ 5 slices/measure** — small and bounded. L3 per-slice analysis cost scales with
this; nothing here is alarming. The slicer itself is O(notes) as the design notes.

### (b) Redundant release-slice frequency (sizes "collapse early vs leave to LN" — the §7 sub-question)
| Metric | Full corpus |
|---|---|
| Release-only interior boundaries (release tick ∉ onset ticks, interior) | **168** |
| …that actually **open a non-empty slice** | **2** (`bwv375`, `bwv392`, 1 each) |
| …that are **subset-redundant** (slice PC-set ⊆ previous slice's) | **2 / 2 = 100 %** |
| Release-opened slices as a share of all 29,045 slices | **≈ 0.007 %** |

**Why so few:** SATB chorale texture is near-homophonic — voices move in block chords, so a release almost always
**coincides with an onset** (already a boundary). The only release-*only* ticks are **phrase-end breaths** where all
voices release into a rest (empty following set → no slice). Mid-span chord-tone drops under a held remainder — the
case the offset policy exists for — are **vanishingly rare on this corpus** (2 instances in 29,045 slices).

**Lean (recorded; the decision rides into the impl design, not decided here):** **leave the redundant
release-slices for layer N to group** — comfortably. On the Baroque corpus the offset policy costs +1.2 % candidate
slices and produces **2** redundant slices total; early-collapse would add slicer complexity to save 0.007 % of
slices. The pure-fact slicer (onset+offset, no collapse) is the right call here.

**★ Honest scope caveat (do not overclaim):** this corpus is **entirely SATB chorales** (+ one trio). The near-zero
redundancy is a property of **block-homophonic** texture. In sustained-pedal / held-chord-under-moving-melody /
keyboard-arpeggiation textures — **absent from this corpus** — mid-span releases (hence redundant release-slices)
would be materially more frequent. The lean still holds (LN groups equal analyses regardless of volume), but the
audit can only *size* it on the data in hand; a non-chorale texture sample would be needed to size the upper bound.
This is flagged, not invented.

### (c) Degenerate cases (flag for the impl design)
**None occur in the Baroque corpus.** Densest: `bwv227.7` at **8.62** slices/measure (112/13) — modest, no
explosion. Grace notes corpus-wide total **3** (max **2** in `bwv299`; `bwv315` has 1) — no grace clusters.
**No tremolo, trill, or glissando regions exist in the chorale corpus**, so the slice-count-explosion risk the
design flags (dense tremolo/trill, grace clusters) **cannot be sized from this data**. Recorded for the impl design
as an out-of-corpus risk to handle by construction (e.g. a tremolo/trill is *notated* as its constituent onsets and
would genuinely produce one slice per written note — the impl design should decide whether ornament expansion is in
or out of the layer-2 fact). **[unverified by data]** — not present in the available corpus; do not fabricate a
figure.

---

## §3 — Deterministic slicer test cases (the layer-2 coverage spec)

The slicer is a pure function `slices(noteModel) → [Slice]`, `Slice = [start, end)` referencing the model (lazy
`overlapping(start,end)` query — §7 representation lean). Tests assert the exact `[start,end)` list and, where it
checks constant-sonority, the `overlapping()` note set per slice. They extend the layer-1 `nm_*` set, reuse its
ScoreRW + `MasterScore`/DIVISION=480 conventions (note_model_tests.cpp), and form the layer-2 **full-branch coverage
gate** (standing full-coverage rule). Each case names the §6 oracle property it checks: **C** = completeness (every
onset is a boundary; no boundary without a change), **S** = constant-sonority (overlap set constant within a slice),
**N** = no-spurious/missed (ties don't split; offsets/grace per §5).

| # | Case | Fixture | Expected slices `[start,end)` (ticks) | Oracle |
|---|---|---|---|---|
| 1 | **Chord + one passing tone → 3 slices** | **NEW** `nm_slice_passing` — chord C-E-G held `[0,1440)`; one passing D sounding only `[480,960)` | `[0,480){C,E,G}`, `[480,960){C,E,G,D}`, `[960,1440){C,E,G}` | C, S |
| 2 | **Held chord under a moving melody → slice per melody onset** | **NEW** `nm_slice_held_melody` — C-E-G whole `[0,1920)` (staff 2); melody quarters C`[0,480)` D`[480,960)` E`[960,1440)` F`[1440,1920)` (staff 1) | 4 slices: `[0,480)`,`[480,960)`,`[960,1440)`,`[1440,1920)`, each = held chord + the current melody note | C, S |
| 3 | **Tie chain → no internal boundary** | **REUSE** `nm_tie_chain` (3 tied C4 quarters + D4 quarter) | `[0,1440){C4}`, `[1440,1920){D4}` — **no** boundary at 480/960 | N (confirms L1 tie-merge collapses it) |
| 4 | **Chord tone releases mid-span → new slice (the offset boundary)** | **NEW** `nm_slice_release` — C-E-G onset together `[0,960)`, but G releases at 480 (G = `[0,480)`, C&E = `[0,960)`) | `[0,480){C,E,G}`, `[480,960){C,E}` — boundary at 480 from the **release** | S, N (§5 amendment core case) |
| 4b | **Minimal release boundary (unison shrink)** | **REUSE** `nm_unison` (v0 E4 half `[0,960)`, v1 E4 quarter `[0,480)`) | `[0,480){E4·v0,E4·v1}`, `[480,960){E4·v0}` — release boundary at 480; **note-set** changes though **pc-set** does not | S (slice identity is the note set, not pc set) |
| 5 | **Grace note → attaches to following slice, no own one-grace slice** | **REUSE** `nm_grace` (acciaccatura G5 before C4-E4-G4 at 0) | the grace contributes **no** boundary; slices are exactly the main-chord slices; `isGrace` events excluded from the grid | N |
| 6 | **All-rest region → no slice** (design lean to confirm) | **NEW** `nm_slice_rest` — note `[0,480)`, rest `[480,960)`, note `[960,1440)` | `[0,480)`, `[960,1440)` — the rest gap `[480,960)` yields **no slice** (slicer partitions only sounding spans). *Design decision to ratify: no-slice vs one empty slice — recommend **no-slice**.* | C, N |
| 7a | **Edge — empty range `end ≤ start`** | REUSE any (e.g. `nm_tie_chain`) | `slices` over an inverted/zero range → `{}` (mirrors `overlapping` guard note_model.cpp:144, T9) | — |
| 7b | **Edge — single note** | **REUSE** `nm_long_sustain` (C4 `[0,9600)`) | exactly **1** slice `[0,9600){C4}` (also checks no-horizon: the slice spans the full 5-whole sustain) | C, S |
| 7c | **Edge — onset exactly at a boundary** | **REUSE** `nm_dense_start` (all quarters: C-E-G`[0,480)`, D`[480,960)`, F`[960,1440)`, A`[1440,1920)`) | 4 slices, each successive onset opening exactly one boundary; back-to-back distinct onsets, no overlap | C, N |
| 7d | **Edge — release exactly at the next onset (coincident)** | covered by #2/#7c (block changes): a tick that is simultaneously a release and an onset is **one** boundary, not two (grid is a set) | dedup confirmed: coincident release+onset → single boundary | N |

Notes for the impl design:
- **Slice identity is the sounding-NOTE set** (`overlapping`), not the octave-folded PC set — case 4b distinguishes
  them (a unison shrink is a real slice change even though the PC set is constant). This is the key axis on which the
  layer-2 slicer differs from the existing `denseBoundaryTicks` (§1.2), which compares PC masks.
- **Grace exclusion** (case 5) must be by the `isGrace` flag regardless of the grace's `duration` (acciaccatura
  duration may be 0; appoggiatura > 0) — exclude all `isGrace` events from boundary generation.
- The 4 NEW fixtures (`nm_slice_passing`, `nm_slice_held_melody`, `nm_slice_release`, `nm_slice_rest`) follow the
  layer-1 fixture pattern: author a `.musicxml`, convert to `.mscx` via MuseScore5.exe (composing_tests cannot
  import MusicXML — see the established fixture-conversion note).

---

## §4 — Provenance / what was and was not done
- **Read-only.** No production `.cpp`/`.h` edited; no behavior change; nothing built; no corpus regen; no commit.
- **Throwaway probe:** `C:\tmp\l2_slice_probe.py` (music21, outside the repo tree). It does not import, link, or
  invoke any composing C++; it is a sizing proxy, not the slicer. Outputs cached at `C:\tmp\l2_probe_out.txt`
  (15-stem) and `C:\tmp\l2_probe_full.txt` (353-stem). Safe to delete.
- **Stop-condition check (§5 of the instruction):** no production/behavior/scoring change attempted; no probe
  entangled with `regionanalyzer`/the live pipeline; sizing came from the existing scores via an independent proxy
  (no corpus regen). One item is explicitly **[unverified]** (default granularity of the live bridge, §1.2) and one
  is **[unverified by data]** (degenerate tremolo/trill density, §2c, absent from the corpus) — neither guessed.

## §5 — For Cowork / the user
- **Cowork:** verify the §1 citations at source (esp. the §1.0 correction that `greedyExpandSegmentation` is
  score-gated selection over `collectNoteChangeTicks`, not Jaccard; that `denseBoundaryTicks` is a
  `PreserveAllChanges`-only cousin; and that `absorbShortRegions` is duration-only, unlike the two tone-mutating
  merges), and confirm nothing in the production tree changed.
- **User to ratify:** (i) the §2(b) lean — **leave redundant release-slices to LN** (sized at 2 slices / 29,045 on
  the chorale corpus), with the honest non-chorale-texture caveat; (ii) the §3 case 6 decision — **all-rest gap →
  no slice**; (iii) the §3 test set as the layer-2 coverage gate. **Then** the layer-2 impl design.
