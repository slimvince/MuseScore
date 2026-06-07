# Iter 97 δ — Sparse-Minor Diatonic Quality Prior — Data Characterization

Read-only data report. No source changes were made. Generated against HEAD
`7060f2c5db` (Iter 96 baseline) with v4 BIR diagnostics already preserved at
`/tmp/bir_true_alpha.txt` (v4) and `/tmp/bir_true_baseline.txt` (Iter 96).

---

## Part A — Pre-existing Corelli notation failures

Both failing tests target `tools/dcml/corelli/MS3/op01n08d.mscx` (Corelli
Op 1 No 8 movement d). The score is a sparse two-voice texture in G minor
(`keySignatureFifths = −2`, `keyMode = Minor`) with brief tonicizations of
C minor. The Iter 96 batch analyzer produces **only 21 regions** for the
entire 30+-measure score. Several regions span 5–13 beats and cross
expected chord boundaries.

### Region map at the expected-test ticks (from `batch_analyze.exe --preset Baroque`)

| Test | Expected m:b | Expected sym | Actual region | Actual sym | distinctPcs | Tones (pc) | Key (kConf) |
|---|---|---|---|---|---|---|---|
| T1 | m1 b3 | G | **no region** — opening unanalyzed | — | — | — | — |
| T1 | m6 b3 | G (not Fm) | m6 b1 .. m7 b1 (4-beat region) | `Fm` | 3 | {0,5,8} = C,F,Ab | Gmin (0.01) |
| T1 | m8 b1 | G (not Ddim/Ab) | m7 b3 .. m10 b1.5 (8.5-beat region) | `Dm7b5/Ab` | 3 | {2,5,8} = D,F,Ab | Cmel (0.00) |
| T1 | m10 b3 | G (not D) | m10 b2.5 .. m11 b4 (3-beat region) | `D` | 4 | {0,2,6,9} = C,D,F#,A | Gmin (0.52) |
| T1 | m11 b3 | Gm (not D/A) | same region as m10 b3 | `D` | 4 | {0,2,6,9} | Gmin (0.52) |
| T2 | m2 b3 | G | **no region** — opening unanalyzed | — | — | — | — |
| T2 | m13 b3 | Gm | m12 b1 .. m14 b4 (5-beat region) | `D` | 3 | {2,6,9} = D,F#,A | Gmin (0.13) |
| T2 | m14 b3 | Cm | same region as m13 b3 | `D` | 3 | {2,6,9} | Gmin (0.13) |
| T2 | m24 b1 | Fm | m23 b1.5 .. m24 b4 (~2.5-beat region) | `Gm/D` | 4 | {0,2,4,10} = D,E,G,Bb | Gmin (0.01) |
| T2 | m24 b3 | Fm | same region | `Gm/D` | 4 | {0,2,4,10} | Gmin (0.01) |
| T2 | m26 b3 | Cm | m26 b2.5 .. m28 b4 (6-beat region) | `G` | 4 | {2,5,7,11} = D,F,G,B | Cmel (0.00) |
| T2 | m18 b1 / b3 | (must differ) | both fall in m17 b1 .. m18 b3 (5-beat region) | `Gm` | 4 | {0,2,7,10} = C,D,G,Bb | Gmin (0.15) |
| T2 | m23 b1 | (not "sususu") | m23 b1.5 region | `Gm/D` | 4 | {0,2,4,10} | Gmin (0.01) |
| T2 | m9 b3 | (no chord) | inside m7 b3 long region | `Dm7b5/Ab` | 3 | {2,5,8} | Cmel (0.00) |

### Quality vs root analysis per test expectation

For each expected beat where a region exists, I check whether the actual
output is "right root, wrong quality" (the sparse-minor δ shape) or
"wrong root entirely" / "region boundary doesn't even reach this tick":

- **m6 b3 G expected, region is `Fm` from m6 b1.** Different root (F vs G);
  region is built from C+F+Ab. A diatonic prior on F in G minor would
  pick degree b7 → Major (F major) — that is _not_ G either. Not a
  quality-prior fix.
- **m8 b1 G expected, region is `Dm7b5/Ab` from m7 b3.** D≠G; the region's
  pc set {D,F,Ab} contains no G. A diatonic prior on a different root
  cannot rewrite this to G.
- **m10 b3 G expected, region is `D` from m10 b2.5.** D≠G; tones include F#
  (sharp 7 of G minor / leading tone of G), so the region might genuinely
  _be_ V→i on the next beat — but the segmentation has merged the V across
  the resolution, so the region as a whole reads D. Not a quality fix.
- **m11 b3 Gm expected, same `D` region.** Same root-mismatch story.
- **m13 b3 Gm / m14 b3 Cm — both inside one wide `D` region.** Tones
  {D,F#,A} are clean D major. The actual chord _at the merged span_ is D
  major; the boundary just doesn't split where the test wants it.
- **m24 b1/b3 Fm expected, region is `Gm/D` with E natural.** Root mismatch
  again (G vs F), and the pc set even contains a non-Fm tone (E natural).
- **m26 b3 Cm expected, region is `G` (V of Cm) spanning into m28.** Root G,
  expected root C — the segmentation has merged a dominant prep into the
  cadence. The G region's distinctPcs=4 reading (D,F,G,B) is internally
  consistent as G7-no-5.
- **m18 b1/b3 distinct-symbols requirement — single 5-beat `Gm` region.** Pure
  segmentation: two test-time queries hit the same region so harmonyTextsAt
  returns the same symbol at both ticks.
- **m23 b1 "no sususu"** — passes (`Gm/D`, not a sus). Not a regression for δ.
- **m9 b3 (no-chord requirement)** — fails because the m7 b3 region spans
  through m9. Pure segmentation.

### Pattern across the Corelli failures

**These failures are dominated by segmentation, not local quality choice.**

In every case where the analyzer produces a region overlapping an expected
tick, the region:
1. spans 2.5–8.5 beats and crosses one or more chord boundaries the test
   expects to see, AND
2. produces a reading that _is_ internally consistent with the tone-set of
   the merged span (e.g. {D,F#,A} → D, {C,F,Ab} → Fm).

Of the 11 region-overlapping expected beats, **0** are "right root, wrong
quality on a correctly-bounded sparse region." The closest candidates to a
quality-decision issue would be:

- m7 b3 `Dm7b5/Ab` (D-F-Ab in C minor context): degree ii of Cmin is
  diatonic ø7, so the analyzer's _current_ output already matches the
  diatonic prior. (The test wants `G` here because the test author expected
  the m8 b1 beat to register V/i — but the tone evidence at that tick
  doesn't contain a G chord.)
- m6 b1 `Fm` (C-F-Ab in G minor → C minor context): degree iv of Cmin =
  diatonic minor, also matches the current quality. Not a miss.

### Existing close-but-misses in `chordanalyzer.cpp`

`applyTonicPriorToSparseChord` (Iter 75/76) at
[notationcomposingbridgehelpers.cpp:226](src/notation/internal/notationcomposingbridgehelpers.cpp#L226)
is the closest extant mechanism. It re-quality-stamps a chord only when:

```cpp
quality in {Power, Suspended2, Suspended4}   // "thin" qualities only
&& distinctPitchClassCount(tones) <= 2        // 2-PC and 1-PC regions only
&& diatonicDegreeForRootPc(rootPc, keyFifths, keyMode) >= 0
```

It does **not** fire on 3-PC sparse regions, does **not** fire when the
analyzer has already committed to a triad quality (Major/Minor/Diminished),
and runs on the bridge path only — not on the batch path that BIR is
measured from. So none of the wide-span Corelli regions (all distinctPcs
3 or 4, already committed to a triad quality) trigger it.

Genuine answer: the Corelli failure pattern is **not** addressed by any
quality-only mechanism, including the proposed δ.

---

## Part B — v4 BIR regression cases

Diagnostic files preserved from the previous v4 run:

- `/tmp/bir_true_baseline.txt` (Iter 96 baseline): 41 entries
- `/tmp/bir_true_alpha.txt` (v4): 44 entries

`diff` shows **exactly 3** new BIR=true entries introduced by v4 (the +3
the prompt cites). The +1 Baroque BIR=false from v4 is not represented in
these files; it would require a separate BIR=false dump. The 3 BIR=true
adds are unambiguous and the dominant failure-pattern, so this report
focuses on them.

### The 3 v4 regression cases

| Score | tick | m:b | distinctPcs | Tones (pc) | Iter 96 baseline | v4 wrong | Ground truth | Key (fifths/mode) |
|---|---|---|---|---|---|---|---|---|
| bwv114.7 | 480 | 1:1 | 4 | {0,2,5,10} = C,D,F,Bb | (not in BIR=true list — non-root-pos or different chord) | `Dm/D` (Minor) | root=Bb (Major) | F major (1♭) |
| bwv300 | 480 | 1:1 | 4 | {2,7,9,11} = G,A,B,D | (not in BIR=true list) | `Bm/B` (Minor) | root=G (Major) | G major (1♯) |
| bwv347 | 960 | 1:2 | 4 | {1,4,9,11} = A,C#,E,B | (not in BIR=true list) | `C#m/C#` (Minor) | root=A (Major) | A major (3♯) |

For each, the m21/wir ground truth picks the same pc — and the analyzer is
flipping to the **minor-third rotation** (the iii reading) of the same pc
set. All three cases are major-key contexts on a strong-beat opening
gesture (m1 b1 / m1 b2), pcs include the I tonic, its major third, its
fifth, and an added 9 (the A above the I root). Examples:

- bwv114.7: Bb major + added 9 (C) = {Bb, C, D, F}. Reading the minor-third
  rotation gives Dm (D + F + (A absent) + Bb as b6) — D minor with the C
  as b7. Both rotations explain the same 4 pcs.
- bwv300: G major + added 9 (A) = {G, A, B, D}. Minor-third rotation = Bm
  (B + D + (F# absent) + A as b7) — Bm7 with no F#.
- bwv347: A major + added 9 (B) = {A, B, C#, E}. Minor-third rotation = C#m
  (C# + E + (G# absent) + B as b7) — C#m7 with no G#.

### Scale-degree and diatonic structure of the v4 regressions

All three pairs (I vs iii) are **both diatonic in a major key**:

- F major: I = F major (degree 0), iii = Am (degree 2). bwv114.7 picks vi
  (Dm, degree 5) — also diatonic, but the I↔iii relationship here is
  Bb-major (IV) vs D-minor (vi). _Both diatonic_.
- G major: I = G (degree 0), iii = Bm (degree 2). _Both diatonic_.
- A major: I = A (degree 0), iii = C#m (degree 2). _Both diatonic_.

### Why does v4 fire? (signal trace)

v4 = "rotation-only ∧ post-bonus quality guard ∧ distinctPcs ≥ 3" — so
the v4 mechanism is targeting **rotations of a symmetric / near-symmetric
pc set** with a quality guard that gates on distinctPcs ≥ 3. These three
cases all sit at distinctPcs = 4 (passes the gate), and their pc sets
contain two minor-third-related diatonic triads (I and iii) that are
"rotations" of the same 4-pc parent.

I do not have the per-region `nextRootPc` plumbing dump for these three
cases preserved on disk; regenerating that would require a non-trivial
re-run. But the structural cause is clear from the data above: the v4
bonus is rewarding the iii reading when both I and iii fit the pc set and
both are diatonic. This is _not_ the failure mode w_seq / w_dim were
designed for (descending-fifth / leading-tone resolution against the next
chord) — it is a local pc-set ambiguity that resolves only by the
preference rule "in a major key, prefer I over iii on opening gestures."

### Score margin — chord-track diagnostic not preserved

The exact pre-bonus margin (top vs runner-up) for each of these three
cases is not in the BIR diagnostic files (those record only the final
identity). Direct measurement would require re-running v4 long enough to
dump the rawCandidates trace for these three regions. I have not done
that here — the prompt indicates we can re-run only if needed for Part B
and these three are characterized adequately from the BIR diff plus the
pc-set arithmetic above. If a future iteration wants exact margins,
re-running with a `--debug-region` filter on bwv114.7 m1 b1, bwv300 m1 b1,
and bwv347 m1 b2 would suffice.

---

## Part C — Synthesis

### Corelli failures: quality problem or something else?

**Something else: segmentation.** In all 11 Corelli expected-beat queries
that fall in an existing region, the region's reading is internally
consistent with the tones merged into the span — the problem is that the
span itself merges across what the test author considers a chord boundary.
A chord-level diatonic quality prior cannot rewrite a `D` region in G minor
to be `G` or `Gm` when the region's tones are `{D, F#, A}` (a literal D
major triad with no G present).

The two opening-bar misses (m1 b3, m2 b3) are even further from quality:
**there is no region at all** in m1–m2 — the analyzer's segmenter never
anchors there, so harmonyTextsAt returns nothing.

### Is there a common structural pattern a δ could target cleanly?

**No clean pattern emerges from the Corelli set.** The would-be δ targets
(sparse 2-PC and 3-PC regions in G minor / C minor) either:

1. already match the diatonic quality in their inferred key (Fm in Cmin
   context = iv, ø7 in Cmin context = ii°, both diatonic), or
2. fail at the boundary level rather than the quality level (the region
   span covers a different chord than the one the test asks about).

In other words, the Corelli failures are not a quality-classification
problem on properly-bounded sparse regions — they are a segmentation /
absent-region problem. δ targeting "sparse minor key + diatonic quality
prior" would fire in regions that are _already_ producing the diatonic
quality, and would not fire in the regions that are actually wrong (which
have either no key match for the prior's preferred quality, or the wrong
root entirely).

### Are the v4 regressions related to the Corelli failure pattern?

**They are a separate phenomenon.** The v4 regressions are:

- **Major key, not minor.** All three (F, G, A major) are major-key
  contexts; the δ target is minor-key.
- **distinctPcs = 4, not sparse.** Each has 4 distinct pcs (the v4 ≥ 3
  gate lets them through; a δ "sparse" gate at distinctPcs ≤ 2 or even
  distinctPcs ≤ 3 would exclude them entirely).
- **I↔iii rotation ambiguity, not quality misclassification.** The wrong
  quality (Minor) happens because the wrong _root_ is chosen (iii instead
  of I); the chosen root is then correctly identified as minor. A "make it
  minor in a minor key" prior would not affect the root choice and so
  would not regress these cases either way.

So the v4 regression cases and the Corelli failures are **disjoint**: they
arise from different mechanisms and a δ aimed at the Corelli pattern
(sparse minor quality prior) would not even encounter the v4 cases (which
are dense + major-key). A δ designed not to encroach on iii-rotation
territory should:

- restrict to **minor mode** (keyMode = Minor or Aeolian/Dorian families),
- restrict to **distinctPcs ≤ 3** (preferably ≤ 2 if extending the
  existing `applyTonicPriorToSparseChord` directly), and
- restrict to **scale degrees whose diatonic quality is unambiguous**
  (e.g. degree b7 = Major in natural minor; degree ii = ø7; degree vii =
  ° in harmonic minor) — avoiding I (Major↔Minor ambiguity in mixed-mode
  contexts) and avoiding III (also ambiguous between Major and Augmented
  in harmonic minor).

### Signals available at the chord quality decision point

In `chordanalyzer.cpp` the per-candidate result-building loop already
computes everything a δ prior would need
([chordanalyzer.cpp:2454–2482](src/composing/analysis/chord/chordanalyzer.cpp#L2454-L2482)):

| Signal | Source | Availability |
|---|---|---|
| `keySignatureFifths` | function param to `analyzeChord` | always |
| `keyMode` (e.g. Minor / HarmMin / MelMin) | function param | always |
| `keyTonicPc` | derived line 1931 | always |
| `scale` | `keyModeScaleIntervals(mode)` | always |
| `degree` (0–6) of candidate root | computed line 2456 (loop over `scale`) | always |
| `diatonic` flag (every sounding pc in scale) | computed line 2464 | always |
| `distinctPcs` | parameter + local | always |
| Presence of third (above threshold) | `pcWeight[(rootPc+3)%12]` or `+4)%12]` | always |
| `pcWeight[rootPc]` (root present at all) | local | always |
| Existing diatonic helpers | `diatonicTriadShapeForDegree(degree, keyMode)` returns canonical (quality, ext) for that degree | available |

A δ implementation could be a 2–4 line addition immediately after the
existing quality assignment in the rawCandidates loop, of the form:

```cpp
// Sketch — not for implementation, only to illustrate signal use.
if (distinctPcs <= 2
    && keyMode is in {Aeolian, NaturalMinor, HarmMin, MelMin}
    && degree in {1, 6, 7 - 1}  // ii, vii, etc. — the unambiguous ones
    && diatonicTriadShapeForDegree(degree, keyMode) gives quality Q
    && quality != Q
    && pcWeight[(rootPc + thirdInterval)%12] < extensionThreshold) {
    quality = Q;
}
```

This would be the analogue of `applyTonicPriorToSparseChord` but applied
inside the candidate scoring (so it affects BIR-measurable batch output,
not just the bridge), and generalized to non-tonic scale degrees.

### Other observations

1. **The Corelli failures will not be cleared by a chord-level δ.** They
   require a segmentation-side fix — either (a) head-gap / tail-gap
   synthesis for the m1–m2 opening (the Iter 73 Fix B mechanism already
   exists but apparently does not produce regions in this score), or
   (b) a sparser segmentation criterion that does not merge 5–8 beats
   into a single region in a piece with such thin texture.

2. **Two-voice texture as a special case.** op01n08d has only two
   voices for much of the score (treble line + bass), with bass notes
   often held for 2+ beats while treble moves. The greedy-expand
   segmenter likely treats the held bass as a smear-target and absorbs
   adjacent material into the bass's region. Any δ that relies on
   "the current region's pc set" will be making decisions on tones
   from multiple chord changes simultaneously.

3. **Key-confidence is very low across the failing regions.** Of the 11
   region-overlapping test points, key confidence is < 0.2 for 8 of them
   and < 0.05 for 5. A δ that defers when keyConfidence is low (analogous
   to the Iter 76 fallback removal) would be even less likely to fire on
   the targeted Corelli regions than the gate restrictions above already
   imply.

4. **The v4 +3 BIR=true cases share a structural sub-pattern that w_dim's
   `distinctPcs >= 4` gate is _not_ wide enough to catch.** Specifically,
   add-9 voicings on I (e.g. {Bb,C,D,F}) where the iii rotation gives a
   no-7th minor reading. If any future iteration tries a w_seq variant
   that does not gate on distinctPcs ≥ 4 to recover the Iter-96-suppressed
   Schumann/Bach wins, these three cases will reappear. The right structural
   gate for them is probably "candidate root pcWeight[third] must exceed
   threshold" — i.e. the candidate must actually contain its own third
   above the noise floor. For Dm in {C,D,F,Bb}, F is the m3 of Dm and is
   present; so that gate alone won't catch them. A stronger gate is "if
   both candidates' roots are diatonic in a major key and the I rotation
   has at least 3 of its 4 chord tones (root, M3, P5, optionally 7th)
   present, prefer I over iii" — but that is closer to an Iter 97 ε / ζ
   shape than the δ being characterized here.

### Concrete recommendation for Iter 97 δ scoping

Based on the data above, a "sparse-minor diatonic quality prior" cannot
fix the two failing Corelli tests on its own — those failures have a
segmentation root cause that is upstream of quality decisions. δ should
either:

1. Be re-scoped as a quality-only improvement targeting OTHER sparse-minor
   regions in the BIR=false set (not the Corelli tests), with the
   expectation that the Corelli notation tests remain failing until a
   separate segmentation fix lands, or
2. Be reframed as a segmentation-side change (e.g. "do not merge regions
   across implicit dominant-resolution boundaries in two-voice textures
   when the next region's root pc differs by a perfect fifth"). This would
   be a much wider change than a chord-quality prior.

If option (1) is chosen, the gate restrictions above (minor-mode only,
distinctPcs ≤ 2 ideally, unambiguous-degree only, defer on low
keyConfidence) keep the δ orthogonal to the v4 iii↔I major-key
regression pattern.
