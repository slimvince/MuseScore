# bwv301 BIR=false — L283 competition diagnostic

**Date:** 2026-06-08 · HEAD `f9ba22157d` · Baroque preset · diagnostic-only (no commits, working tree clean)

## TL;DR

The premise needs reframing. **The full 5-note region is never analyzed as a
single snapshot.** `batch_analyze`'s greedy-expand segmentation feeds
`analyzeChord`/`applyHarmonicFunction` only small sub-windows. The displayed
region weights (B=1.25, D=1.25, A=1.05, …) are a **display-time aggregation over
the merged region**; the competition never sees them. The fingerprint
"{C,D,Ab,A,B} present, G absent" matched **0 of 377** `applyHarmonicFunction`
calls. The G-rooted identity is produced by `{D,A,B}={2,9,11}` sub-segments where
the per-PC weights are `{D=0.6, A=0.2, B=0.2}` or `{D=0.2, A=0.6, B=0.2}` — **B is
never the strongest PC at competition time (it is 0.2).**

Within those sub-segments the B-rooted reading **is scored, in the same per-bass
group as the winner**, and loses to G on vertical template score by 0.27–0.6.
This is a **template-scoring** problem (a major triad with 3rd+5th present and
**root absent** outscores a seventh chord missing its fifth with root present),
compounded by **rootContinuity contamination** across the merged sub-segments.
It is **not** a bass-register extraction problem and **not** a cross-bass-group
problem.

---

## The region

bwv301 m1 beat 3, ticks 960–1920 (`tools/corpus/bwv301.xml`). Display tones:
D=1.25, A=1.05 (bass, A2 pitch 45), B=1.25 (B2 pitch 47), C=0.25, Ab=0.20, **G
absent**. Our emitted winner: **G/A** (root G PC7, bass A PC9, Major), score 2.16.
DCML / music21: **root B** — `vi7`, an incomplete B minor-seventh (B-D-A, missing
F#), A in the bass → third inversion. (music21 reads ticks 960/1200/1680 all as
root-11 B; tick 1440 is a passing #iv° on Ab.)

## How the winner is actually produced

`pcWeight` = Σ `max(0.1, tone.weight)` (chordanalyzer.cpp:2492), so analysis-time
weights are floored at 0.1 and absent tones are exactly 0. Across the whole
bwv301 run the largest single-PC analysis weight is 0.6 — i.e. every
`applyHarmonicFunction` call is on a greedy sub-window, never the merged region.
The two **context-bearing** `{D,A,B}` blocks (the decisive ones) are:

**Block 5** — `{D=0.6, A=0.2, B=0.2}`, prevRoot=9(A) nextRoot=2(D), **sole bass
candidate = B**:
| candidate | root | weight of root | post-score |
|---|---|---|---|
| **G Major (winner)** | G (7) | **0.0 (absent)** | **2.16** |
| Bm7 / Bø (incomplete) | B (11) | 0.2 | 1.89 |
| D Major | D (2) | 0.6 | 1.85 |
| Bm triad | B (11) | 0.2 | 1.58 |
| B dim | B (11) | 0.2 | 1.34 |

**Block 6** — `{D=0.2, A=0.6, B=0.2}`, prevRoot=7(**G**) nextRoot=4, **sole bass
candidate = A**:
| candidate | root | post-score |
|---|---|---|
| **G Major (winner)** | G (7, absent) | **3.2** (= pre 2.8 **+ 0.40 rootContinuity**) |
| Bm7 / Bø (over A) | B (11) | 2.6 |
| A Sus2 | A (9) | 1.96 |

Block 5's 2.16 equals the emitted `chordScore`. Block 6 shows the rootContinuity
contamination: because the *previous* sub-segment was also misread as G
(prevRoot=7), the G candidate gets +0.40, widening its margin to 0.6 and locking
the error in across the merged region.

---

## Answers

**Q1 — Is B (PC 11) present as a bass candidate?**
**Yes.** In bass-B sub-segments B is the *sole* enumerated bass; in bass-A
sub-segments B is scored as an upper root over bass A. The best B-rooted cell is
the incomplete Bm7/Bø (= the DCML root) at **post = 1.89** (bass-B) / **2.6**
(bass-A). It loses to the G winner by **0.27** (2.16 vs 1.89) and **0.6** (3.2 vs
2.6) respectively. Note: at competition time B's *weight* is only 0.2, not the
display-time 1.25 — multi-bass enumeration does not fire here, so each sub-segment
commits to one bass (the strongest bass-register PC).

**Q2 — Which bass does the winner belong to?**
The G winner sits in whichever single bass the sub-segment enumerated. With
bass=B it is **G/B** (first inversion, bass B = G's 3rd — the "sensible"
inversion that makes the absent-root G reading viable, since B and D are G's 3rd
and 5th). With bass=A it is **G/A** (bass A is a *non-chord* tone of G major,
scored via the bass-dependent term) — this is the emitted output. G is chosen as
root purely because the two present upper tones {B, D} map onto its 3rd and 5th.

**Q3 — Is this a bass-register extraction problem?**
**No.** B is enumerated and the B-rooted reading is in the **same `chosenPerBass`
group** as the G winner (not a different per-bass group, refuting the earlier
"needs cross-bass retention" hypothesis). The root cause is a **template-scoring
asymmetry**: a major triad with 3rd+5th present and **root absent** (G/B: B,D
present, G weight 0.0) scores 2.16, beating the structurally-correct
seventh-chord-missing-fifth with root present (Bm7 = B,D,A present, F# absent) at
1.89. The "complete-looking" first-inversion major outranks the incomplete vi7.
rootContinuity then propagates the first G-misread into the adjacent sub-segment
(+0.40, Block 6).

**Q4 — Present-root alternative within margin of the winner?**
**Yes, comfortably, and it is the correct root.** Within `chosenPerBass`:
- Block 5 (bass B): winner G (root w=0.0) 2.16; present-root B (Bm7/Bø, w=0.2)
  **1.89**, gap **0.27**; present-root D (D Major, w=0.6) 1.85, gap 0.31.
- Block 6 (bass A): winner G 3.2; present-root B (Bm7/Bø) **2.6**, gap 0.6.

In *both* sub-segments the highest-scoring present-root candidate in-group is
**B-rooted — the DCML-correct root.**

---

## Bottom line

The B-rooted reading **is present at L283**, in the **same per-bass group** as the
G winner — it is neither structurally excluded nor in a separate bass group. It
loses by 0.27–0.6 on vertical template score because a major triad whose **root is
absent (weight exactly 0.0)** but whose 3rd+5th are present outscores the
incomplete Bm7 (vi7) that is structurally correct; rootContinuity then locks the
error across the greedy-expand sub-segments. This is a **template-scoring** issue,
not bass-register extraction and not cross-bass.

**An absent-root guard at L283 does have a viable in-group swap target for
bwv301.** The winner's root weight is exactly 0.0 — a clean, unambiguous signal —
and the highest-scoring present-root candidate in the same group is the B-rooted
Bm7/Bø, i.e. the DCML-correct root, in both decisive sub-segments. So bwv301 is
**not** definitively a Phase E case: a guard of the form "if the winner's root has
pcWeight ≈ 0, swap to the highest-scoring candidate whose root pcWeight > 0 within
the same per-bass group" would select B here, without any cross-bass machinery.

Caveats before acting on this:
1. The guard must be validated for BIR=false regressions in **both** Baroque and
   Jazz (absent-root major-triad inversions like genuine `G/B` first inversions,
   where the root really is weakly present, must not be flipped).
2. Fixing the **first** G-misread sub-segment is what matters — once that is
   B-rooted, the rootContinuity contamination (Block 6's +0.40) disappears on its
   own.
3. The display-time vs competition-time weight gap means any future
   "strongest-PC = correct root" heuristic must operate on the **merged-region**
   weights, which the competition pipeline does not currently see.
