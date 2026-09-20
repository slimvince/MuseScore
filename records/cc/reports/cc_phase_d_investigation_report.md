# Phase D Investigation — Arpeggio Sub-Region Mechanism

**Date:** 2026-06-09
**Scope:** read-only investigation (no source changes, no build). Tests the working
hypothesis that the Δ=+7a BIR=false cases (bwv102.7, bwv261) are caused by the
`collectRegionTones` backward-walk excluding the DCML root via
`noteEnd <= startTickInt`, and characterises the proposed `<= → <` fix.
**HEAD:** `90a52b5fee` (master). **Preset:** Baroque. **DIVISION = 480** (1 beat).
**Method:** code reading + `batch_analyze --dump-regions batch|notation-premerge`
+ `--diagnose-measures` + music21 raw-note dump (exact onset/offset ticks).

---

## TL;DR — the hypothesis is FALSIFIED for both target cases

The proposed fix — change the `collectRegionTones` backward-walk condition from
`noteEnd <= startTickInt` to `noteEnd < startTickInt` so that notes ending *exactly*
at the sub-region start are included — **does not inject the DCML root into the failing
committed slice in either case.** The raw note data shows:

| case | failing slice start | notes ending *exactly* at that tick (what `<` would add) | DCML root | DCML root among them? |
|---|---|---|---|---|
| bwv102.7 | t17520 (m9 b4.5) | **C (pc0), Eb (pc3)** | Ab (pc8) | **NO** |
| bwv261   | t33840 (m18 b4.5) | **G (pc7), B (pc11)** | F# (pc6) | **NO** |

In **both** cases the DCML root's note **attacks fresh in a *later* sibling slice**
(bwv102.7 Ab attacks at t17760; bwv261 F# attacks at t34080) — it is **temporally in
the future** relative to the committed wrong-root slice. A *backward* walk can never pull
in a note that has not started yet. The boundary-touching predecessor notes are the
*other* chord tones (the 3rd/5th of the wrong reading or the previous chord's tones), not
the DCML root.

The hypothesis assumed a clean legato arpeggio in which the immediately preceding step
carries the root and ends exactly at the boundary. **That pattern does not occur in
either Bach chorale.** The arpeggiation places the DCML root one-to-two steps *after* the
committed slice, freshly attacked, not one step *before* it.

**Correct fix:** the aggregation-first duration-weighted window already specified in
`docs/redesign_plan.md` Step 4 — re-score the whole arpeggiated span as one region on its
duration-weighted aggregate — **not** a boundary-condition tweak to the backward walk.
The `<= → <` change is (a) ineffective for the targets, (b) unsafe for the 10
parent-scope call sites, and (c) would still need the rcb cascade addressed for bwv261
(razor-thin 0.025 vertical margin).

---

## Section 1 — Backward-walk mechanism

### 1a. The exact condition (confirmed, with one correction)

`collectRegionTones` — [regiontonecollector.cpp:314-366](src/composing/analysis/engravingbridge/regiontonecollector.cpp#L314-L366).
The backward walk iterates segments *before* `startTick`:

```cpp
const Fraction backLimit = startTick - Fraction(4, 1);          // 4 whole notes back
const Segment* firstForward = sc->tick2segment(startTick, true, SegmentType::ChordRest);
if (firstForward) {
    for (const Segment* s = firstForward->prev1(SegmentType::ChordRest);
         s && s->tick() >= backLimit;
         s = s->prev1(SegmentType::ChordRest)) {
        const int segTickInt = s->tick().ticks();
        ...
        const int noteEnd = segTickInt + cr->actualTicks().ticks();   // line 332
        for (const Note* n : toChord(cr)->notes()) {
            ...
            recordPedalTailCandidate(si, noteEnd, sustainBeatWeight, n);  // line 338 (pedal only)
            if (noteEnd <= startTickInt) {        // line 340  ← THE CONDITION
                continue;
            }
            ...
        }
    }
}
```

**Confirmed:** the inclusion test is `if (noteEnd <= startTickInt) { continue; }`
([line 340](src/composing/analysis/engravingbridge/regiontonecollector.cpp#L340)). A note
whose written end falls **exactly at** `startTickInt` is **excluded** — it must *overlap*
into the region (`noteEnd > startTickInt`) to count.

**Correction to the hypothesis's wording:** the threshold is `startTickInt` (the
sub-region's *own* start), **not** `parentStartTickInt`. `parentStartTickInt` is used only
for the `onsetAtRegionStart` flag ([line 457](src/composing/analysis/engravingbridge/regiontonecollector.cpp#L457):
`if (segTickInt == parentStartTickInt) a.trueAttackAtStart = true`), never for backward
inclusion. This matters for the fix-scope analysis (Section 4).

**Is there any other path that includes a `noteEnd == startTickInt` note?** One, and it is
inert here: `recordPedalTailCandidate` ([line 338](src/composing/analysis/engravingbridge/regiontonecollector.cpp#L338))
runs *before* the exclusion check, so a boundary-touching note can be recorded as a
sustain-pedal tail — but only when `pedalWindowsByStaff` is non-empty (a sustain-pedal
marking spans the note-off). The Bach chorale corpus has no sustain pedal, so this path is
dead for both targets. No other path includes such a note.

### 1c. `coalesceShortSameRootRuns` does not rescue these cases

[regionanalyzer.cpp:68-147](src/composing/analysis/region/regionanalyzer.cpp#L68-L147).
The run is broken when the next region's `rootPc != runRoot`
([line 101](src/composing/analysis/region/regionanalyzer.cpp#L101)) — confirmed. The exact
condition under which the rescue fires (all must hold):

1. a maximal run of **≥ 3** (`kCoalesceMinRunCount`) **contiguous** sub-regions
   (`regions[j].startTick == regions[j-1].endTick`),
2. **each** shorter than `kMinRegionTicks` (480 ticks),
3. **all** sharing one `rootPc`,
4. total duration **≥ 720** (`kCoalesceMinRunTicks = 3·480/2`),
5. the predecessor already in `coalesced` does **not** share `runRoot`
   ([lines 90-95](src/composing/analysis/region/regionanalyzer.cpp#L90-L95)).

Note the hypothesis's premise ("arpeggio sub-regions have *different* roots") is **not**
the operative reason it fails to fire. In bwv102.7 the two failing slices in fact share
root **Eb** (idx 53 EbMaj7 root 3, idx 54 Eb6/Ab root 3). Coalesce still does not fire
because condition (2) breaks the run: the second slice is 480 ticks (== `kMinRegionTicks`,
not `<`), so no same-root run reaches length 3. **And even if it fired, condition — the
merged region inherits the *longest* sub-region's identity ([line 122-128](src/composing/analysis/region/regionanalyzer.cpp#L122-L128)),
which is the Eb-/C#-rooted (wrong) reading, never the DCML Ab/F#.** Coalesce is
structurally incapable of producing the DCML root.

---

## Section 2 — Sub-boundary trigger (`detectBassMovementSubBoundaries`)

[regiontonecollector.cpp:668-747](src/composing/analysis/engravingbridge/regiontonecollector.cpp#L668-L747).

- **What triggers a boundary:** at each ChordRest segment, the lowest *attacking* pitch's
  PC is the segment "bass" (only notes with `cr->tick() == segTick` — true attacks, not
  sustains — [line 707](src/composing/analysis/engravingbridge/regiontonecollector.cpp#L707)).
  A boundary fires at the first onset where the bass PC differs from the **most recently
  accepted boundary's** bass PC **AND** the gap from that boundary is `>= minGapTicks`
  ([lines 735-744](src/composing/analysis/engravingbridge/regiontonecollector.cpp#L735-L744)).
- **Default `minGapTicks = 2 * Constants::DIVISION = 960 ticks` (2 beats / a half note)**
  — header default at [regiontonecollector.h:174](src/composing/analysis/engravingbridge/regiontonecollector.h#L174);
  Pass 2b calls it without overriding ([regionanalyzer.cpp:764](src/composing/analysis/region/regionanalyzer.cpp#L764)).
- **Minimum-duration threshold:** yes — the 960-tick gap. The header's phrase "ANY bass PC
  change fires — no minimum interval threshold" refers to *pitch interval* (a semitone bass
  move fires as readily as a fifth), **not** time: the 960-tick **time** gate is real.
- **Does each arpeggio step get its own boundary?** **No.** A sixteenth-/eighth-note
  arpeggio (120-240 ticks/step) is far below the 960-tick gate, so most steps do **not**
  produce a sub-boundary. Boundaries land only where the bass PC has changed *and* ≥ 2
  beats have elapsed since the last boundary. (Parent-region eligibility is also gated:
  `kPass2bMinRegionTicks = 4·480 = 1920` — only regions ≥ 4 beats are split at all,
  [regionanalyzer.cpp:757](src/composing/analysis/region/regionanalyzer.cpp#L757).)

The practical sub-region granularity that actually feeds the oracle comes from **Pass 2
onset-Jaccard** (`detectOnsetSubBoundaries`, threshold 0.25) plus **greedy-expand**, not
from Pass 2b alone. The observed failing slices are 240-tick onset slices (Section 5),
finer than 960 ticks — i.e. they are Pass-2 / greedy-expand products, confirming Pass 2b's
bass gate is *not* the splitter here.

---

## Section 3 — Empirical: bwv102.7 and bwv261

Raw onsets/offsets from music21 (`offset × 480 = tick`); per-slice tone sets from
`--dump-regions notation-premerge`. The committed (merged) reading is from
`--dump-regions batch`. `--diagnose-measures` reports only the *first* region of each
measure (bwv102.7 → m9 b1 `F7/Eb`, m10 b2 `Bb`), so it does **not** reach the failing
sub-regions; the per-slice data below is the precise substitute.

### bwv102.7 — committed `EbMaj7/Ab` (root Eb=3) vs DCML `AbMaj7` (root Ab=8); Δ=+7

Raw notes around the boundary (tick / pitch / pc):

```
 onTick offTick  pc name      onTick offTick  pc name
  16800  17040   10 Bb         17280  17760    3 Eb   (sustains THROUGH slice A)
  16800  17280   10 Bb         17280  17760    7 G    (sustains THROUGH slice A)
  16800  17280    5 F          17520  17760   10 Bb   ← attacks at slice-A start
  16800  17280    2 D          17520  17760    2 D    ← attacks at slice-A start
  17040  17280    8 Ab  ←only Ab; ENDS 17280   17760  18240    8 Ab  ← attacks at slice-B start
  17280  17520    0 C   ←ENDS 17520           17760  18240    3 Eb
  17280  17520    3 Eb  ←ENDS 17520           17760  18240    0 C
                                              17760  18240    7 G
```

- **Slice A — committed run-start, t17520-17760 (240t).** Tone set `{Bb,D,Eb,G}` =
  **EbMaj7** (complete 4-note Maj7; each w=0.25). **Ab weight = 0** — the DCML root is
  genuinely not sounding. Eb is the correct reading of these four tones.
- **Slice B — sibling, t17760-18240 (480t).** Tone set `{C,Eb,G,Ab}` = **AbMaj7** root
  position (Ab in bass). DCML root **present and fully scored** here. Per the prior
  per-cell dump (`cc_deltaseven_7a_diagnostic_report.md` Part C): AbMaj7 raw **2.55** >
  Eb/Ab raw **2.33** — AbMaj7 wins *vertically*; `rootContinuityBonus +0.40` (from Slice
  A's Eb) flips it to Eb/Ab (2.725).
- **Notes ending exactly at t17520 (what `<` would add to Slice A):** **C (pc0)** and
  **Eb (pc3)** (the 17280-17520 pair). **Not Ab.** The lone Ab (17040-17280) ends at
  t17280 — a full step *before* the boundary, so neither `<=` nor `<` reaches it.
- **Effect of `<` on Slice A:** `{Bb,D,Eb,G}` → `{C,Bb,D,Eb,G}`. AbMaj7 still has only
  Ab,Eb,G of its 4 tones (Ab still absent); EbMaj7 remains the complete reading. **No flip
  toward Ab.** The change merely perturbs Slice A toward a Cm7/EbMaj9 colour — a regression
  vector, not a fix.

### bwv261 — committed `C#m/E` (root C#=1) vs DCML `F#7` (root F#=6); Δ=+7

Raw notes around the boundary:

```
 onTick offTick  pc name
  32640  33600    2 D          (long, ends 33600)
  32640  33600    6 F#   ←F#, ENDS 33600
  33360  33600    6 F#   ←F#, ENDS 33600
  33600  33840    7 G    ←ENDS 33840
  33600  33840   11 B    ←ENDS 33840
  33600  34080    1 C#         (sustains THROUGH slice 2)
  33600  34080    4 E          (sustains THROUGH slice 2)
  33840  34080    4 E    ← attacks at slice-2 start
  33840  34080    1 C#   ← attacks at slice-2 start
  34080  34560    6 F#   ← attacks at slice-3 start
  34080  34560    1 C#
  34080  34560   10 A#(Bb)
  34080  34560    4 E
```

- **Slice 2 — committed emitted region, t33840-34080 (240t).** Tone set `{C#,E}` (2 PCs,
  each w=0.50). **F# weight = 0.** Per prior dump: C#m raw **2.90** ≫ F#7 raw **1.65** —
  C#m wins *even without rcb* (F# genuinely absent; pure segmentation).
- **Slice 3 — sibling, t34080-34560 (480t).** Tone set `{C#,E,F#,A#}` = **F#7** (all four
  present). Prior dump: F#7 raw **2.850** > C#m/F# raw **2.825** (margin **0.025**); rcb
  +0.40 (from C#) flips it to C#m6/F#.
- **Notes ending exactly at t33840 (what `<` would add to Slice 2):** **G (pc7)** and
  **B (pc11)** (the 33600-33840 pair). **Not F#.** Both F# notes end at t33600 — one step
  *before* the boundary, unreachable by `<=` or `<`.
- **Effect of `<` on Slice 2:** `{C#,E}` → `{C#,E,G,B}` = **C#ø7** — still root C#, still
  no F#. No flip toward F#.

**Cross-case structural fact:** in both, the DCML root's note **attacks fresh in a later
slice** (Ab @17760, F# @34080) and is **never** a boundary-touching predecessor. The wrong
root is decided in an *earlier* slice where the DCML root has not yet sounded, then
`rootContinuityBonus` perpetuates it *forward* into the slice where the DCML root appears.
This is a **forward cascade**, not a backward-collection gap — which is precisely why a
backward-walk boundary tweak cannot touch it.

---

## Section 4 — Fix-scope analysis (`<= → <`)

### Full caller inventory of `collectRegionTones`

| # | Call site | `parentStartTick` arg | Scope |
|---|---|---|---|
| 1 | regionanalyzer.cpp:333 (segmenter probe lambda) | `-1` | parent |
| 2 | regionanalyzer.cpp:395 (Pass 1 region tones) | `-1` | parent |
| 3 | regionanalyzer.cpp:425 (Pass 1 next-region lookahead) | `-1` | parent |
| 4 | **regionanalyzer.cpp:597 (Pass 2 sub tones)** | `parentRegion.startTick` | **sub-region** |
| 5 | regionanalyzer.cpp:651 (Pass 2 next-sub lookahead) | `-1` | parent |
| 6 | **regionanalyzer.cpp:804 (Pass 2b sub tones)** | `parentRegion.startTick` | **sub-region** |
| 7 | regionanalyzer.cpp:850 (Pass 2b next-sub lookahead) | `-1` | parent |
| 8 | notationcomposingbridgehelpers.cpp:866 (display gap) | `-1` (default) | parent |
| 9 | notationcomposingbridgehelpers.cpp:1065 (display opening) | `-1` | parent |
| 10 | notationcomposingbridgehelpers.cpp:1090 (display region) | `-1` | parent |
| 11 | notationcomposingbridgehelpers.cpp:1115 (carried opening) | `-1` | parent |
| 12 | notationimplodebridge.cpp:632 (implode display) | `-1` | parent |

(Plus `notationcomposingbridgehelpers.cpp:327` — a thin pass-through wrapper — and a unit
test. No other callers in `src/` or `tools/`.)

**Answers to Task 3:**

1. **Sub-region call sites (`parentStartTickInt != -1`): exactly two** — Pass 2 (line 597)
   and Pass 2b (line 804). Both pass `parentRegion.startTick`.

2. **Parent-scope calls (10 of 12):** for these, a note with `noteEnd == startTickInt`
   is the **previous chord's final note** — it ends exactly as this region begins and does
   not sound during it. Excluding it is **correct**; including it would bleed every
   region's predecessor terminal note into it.

3. **Is `< startTickInt` safe universally? No.** It is unsafe for all 10 parent-scope
   callers (point 2) — including the five **notation display** callers (#8-#12), so a
   naive edit perturbs the live annotation/implode UI, not just the batch metric. Worse,
   the backward-walk threshold uses `startTickInt`, **not** `parentStartTickInt`, so the
   condition is **not naturally scoped** — a one-line `<=`→`<` edit hits all 12 sites
   identically. To restrict it to genuine intra-arpeggio boundaries you would have to gate
   it explicitly, e.g. `if (noteEnd < startTickInt || (parentStartTickInt >= 0 &&
   parentStartTickInt < startTickInt && noteEnd <= startTickInt)) {...}` — i.e. only relax
   for **non-first sub-regions** (where `parentStartTickInt < startTickInt`, proving the
   boundary is interior to one parent harmony). For the first sub-region of a parent
   (`parentStartTickInt == startTickInt`) and all parent-scope calls, keep `<=`.

4. **Other callers:** yes — the five notation-bridge display callers (#8-#12) and the three
   lookahead/probe calls (#1, #3, #5, #7), all `parentStartTick = -1`. A universal change
   affects every one.

**But scoping is moot:** Section 3 shows that even correctly scoped to Pass 2/2b
sub-regions, the boundary-touching notes are C/Eb (bwv102.7) and G/B (bwv261), never the
DCML root. The fix changes the wrong slices in the wrong direction and fixes neither
target.

---

## Section 5 — `--dump-regions notation-premerge` sub-region picture

The arpeggiated spans are split into 240-tick onset slices (Pass-2 / greedy-expand
granularity), each scored independently:

**bwv102.7** (the DCML `AbMaj7` span, around m9 b3 → m10 b1):

| idx | m.beat | ticks | dur | premerge symbol | root | tone PCs |
|---|---|---|---|---|---|---|
| 51 | 9 b3   | 16800-17040 | 240 | Bb        | 10 | D,F,Bb |
| 52 | 9 b3.5 | 17040-17520 | 480 | Bbadd11   | 10 | C,D,Eb,F,G,Ab,Bb |
| 53 | 9 b4.5 | 17520-17760 | 240 | **EbMaj7** | **3** | D,Eb,G,Bb  ← Ab absent (Slice A) |
| 54 | 10 b1  | 17760-18240 | 480 | **Eb6/Ab** | **3** | C,Eb,G,Ab  ← Ab present (Slice B) |

→ batch path **merges** idx 53+54 into one region `EbMaj7/Ab` (t17520-18240, root Eb).

**bwv261** (the DCML `F#7` span, around m18 b3 → m19 b1):

| idx | m.beat | ticks | dur | premerge symbol | root | tone PCs |
|---|---|---|---|---|---|---|
| 84 | 18 b3   | 33120-33360 | 240 | GMaj7      | 7 | D,F#,G,B |
| 85 | 18 b3.5 | 33360-33600 | 240 | D+/F#      | 2 | D,F#,Bb |
| 86 | 18 b4   | 33600-33840 | 240 | C#m7b5/G   | 1 | C#,E,G,B |
| 87 | 18 b4.5 | 33840-34080 | 240 | **C#m/E**  | **1** | C#,E  ← F# absent (Slice 2) |
| 88 | 19 b1   | 34080-34560 | 480 | **C#m6/F#** | **1** | C#,E,F#,A#  ← F# present (Slice 3) |

→ batch path emits `C#m/E` at t33840 (the BIR-aligned tick) and `C#m6/F#` at t34080;
neither is root F#.

In both, the DCML harmony is spread across ≥ 3 onset slices; the DCML root sounds in only
one of them and **after** the committed wrong-root slice.

---

## Section 6 — Assessment

**Does the hypothesis hold? No — falsified for both targets.** The `noteEnd <= startTickInt`
condition is confirmed exactly as described (Section 1), and it *does* exclude
boundary-touching notes. But the empirical note data (Section 3) shows the excluded
boundary-touching notes are **not** the DCML root in either case:

- bwv102.7: `<` would add **C, Eb** to Slice A — Ab stays absent (Ab ended at t17280, two
  steps early; Slice A remains complete EbMaj7).
- bwv261: `<` would add **G, B** to Slice 2 — F# stays absent (both F# notes ended at
  t33600; Slice 2 becomes C#ø7, still root C#).

The root cause the hypothesis missed: **the DCML root is temporally later than the
committed wrong-root slice** — it attacks fresh in a subsequent sibling slice (Ab@17760,
F#@34080), and is already present and (vertically) correctly scored *there*. The failure
is the **forward `rootContinuityBonus` cascade** carrying the earlier wrong root into that
later slice — exactly the mechanism `cc_deltaseven_7a_diagnostic_report.md` documented.
A *backward* tone-collection change is the wrong axis entirely: you cannot collect a note
that has not yet started.

**Is `<= → <` the right approach? No.** It is:
1. **Ineffective** — adds the wrong PCs to the wrong slices (Section 3);
2. **Unsafe as written** — the threshold is `startTickInt`, not `parentStartTickInt`, so it
   hits all 12 callers including the 5 notation-display paths (Section 4);
3. **Insufficient even if it worked** — bwv261's present-root slice wins vertically by only
   0.025, so the rcb cascade would still need breaking.

**Better location — the aggregation-first window already specified in
`docs/redesign_plan.md` Step 4.** Re-score the *whole arpeggiated span as one region* on
its duration-weighted aggregate, instead of scoring 240-tick onset slices and
merging-after. Concretely, for bwv102.7 the merged window t17520-18240 aggregates to PC
durations `{Eb:720, G:720, Ab:480, C:480, D:240, Bb:240}`; the four AbMaj7 tones
(Ab,C,Eb,G) dominate, the lowest sounding pitch over the window is Ab (midi 44 → bass),
and the region's predecessor is Bb-rooted (so rcb rewards neither Ab nor Eb). AbMaj7 then
wins both vertically and post-rcb. This is the *aggregation-first* path the redesign doc
marks "preferred"; the current pipeline already produces the merged 6-PC tone set but
keeps the *sub-slice* winner (merging-after), which is why the wrong Eb identity survives.

**Caveat on bwv261:** aggregation alone is necessary but may not be *sufficient* — the
present-root vertical margin is only 0.025 and the bass over the aggregated window is E
(F#7/E third inversion vs C#m/E first inversion), so the first-inversion `basisDep` + rcb
can still tip it. bwv261 likely needs aggregation-first **plus** the Phase E functional
check (a sustained ii→V arpeggiation should not be re-rooted on its fifth), consistent with
the redesign plan's Step 4→Step 5 sequencing.

**Recommendation:** **do not** modify the `collectRegionTones` backward-walk condition.
Proceed to the Phase D *aggregation-first duration-weighted window* (redesign_plan Step 4)
as the structural fix, with the window-boundary decision still to be finalised by Cowork.
The `<= → <` tweak should be recorded as a **dead end** for the Δ=+7a cluster.

---

## Surprises / deltas from the instruction's expectations

1. **The backward-walk threshold is `startTickInt`, not `parentStartTickInt`** (the
   instruction's Task 1a wording implied the latter). `parentStartTickInt` governs only the
   `onsetAtRegionStart` flag. This means the `<= → <` change is not naturally scoped to
   sub-regions — it hits all 12 callers.
2. **`detectBassMovementSubBoundaries` has a 960-tick (2-beat) `minGapTicks`** — it does
   **not** fire at every arpeggio step. The failing 240-tick slices come from Pass-2
   onset-Jaccard / greedy-expand, not Pass 2b.
3. **The two failing slices in bwv102.7 share a root (Eb), not differ** — so coalesce's
   non-rescue is due to the run-length/duration gates, not root mismatch; and coalesce
   would inherit the wrong Eb root even if it fired.
4. **The decisive fact is temporal direction:** the DCML root attacks *after* the committed
   slice, so no backward collection rule can reach it. The hypothesis's "previous arpeggio
   note carries the DCML root" pattern does not occur in either chorale.
5. **`--diagnose-measures` reports only the first region per measure**, which for these
   cases is not the failing sub-region; per-slice premerge + raw-note dumps were required.
