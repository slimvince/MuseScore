# Δ=+7 Predecessor Confidence Diagnostic — Report

**Date:** 2026-06-08
**Type:** read-and-diagnose pass, no commits. Temporary `fprintf` diagnostics were
added to `regionanalyzer.cpp`, data collected, and removed; the working tree is
clean except for this report.
**Preset:** Baroque (all six scores, to keep the bonus magnitude comparable).
**Build:** `setup_and_build.bat`, exit 0. Diagnostic build ran batch_analyze on all
six scores.

---

## TL;DR — the hypothesis is falsified

The diagnostic asked whether **predecessor root pcWeight** and/or **winner margin**
can separate the wrong Δ=+7 predecessors from the correct mozart_k280 Alberti
predecessor, where `distinctPcs` (the Iter-98 proxy) could not.

**They cannot.** Two independent and stronger findings emerged:

1. **2 of the 5 cases are not rootContinuity-caused at all.** In `bwv102.7` and
   `bwv261` the wrong root wins **vertically** at the first sub-region of the run
   (real within-bass margins 0.33 / 0.36, `contFired=0`). The continuity bonus only
   *self-perpetuates* the wrong root into the run's later sub-regions — it is a
   symptom, not the trigger. Gating `rootContinuityBonus` would not fix either.

2. **For the 3 genuine continuity cases, the predecessors are not "sparse/uncertain."**
   `bwv245.28` and `bwv296` have **fully confident 3-PC triad predecessors that are
   themselves the correct reading** (Bm = ii; D = vi). Only `bwv320` has a sparse
   (2-PC) predecessor — and even it has a **high** root pcWeight (0.82). None of the
   three discriminators (pcWeight, within-bass margin, distinctPcs) separates these
   from the mozart control. On pcWeight and distinctPcs the mozart control sits at
   the *extreme* end (pcWeight 1.0, distinctPcs 1), so any threshold that blocks the
   Δ=+7 cases also blocks mozart.

The predecessor-confidence lever is the same dead end as `distinctPcs`. The real
lever, for the 3 genuine cases, is at the **failing region** (a bass-aware gate on
whether the +0.40 bonus may reward a non-root-position fifth when the bass has
moved), not at the predecessor.

---

## Method

`tools/characterise_bir_false.py`'s WiR/DCML pipeline (the project's ground truth;
music21 is corroboration only) defines a Δ=+7 BIR=false case as `chord_disagree` vs
music21 + `bassIsRoot==False` + music21/DCML agree + `(our_root − dcml_root) mod 12 ==
7`. A focused variant (`/tmp/d7_wir.py`) located exactly **one** such case per target
score.

A temporary `fprintf` (`[DIAG]`) was added at all three region-winner sites in
`regionanalyzer.cpp` (Pass 1 L460, Pass 2 L671, Pass 2b L858), printing per region:
winner root, `pcWeight[winnerRoot]`, the within-winning-bass post-competition
`rawCandidates[0].score` / `[1].score` / margin, `distinctPcs`, the `previousRootPc`
fed into the region, and whether continuity fired (`winnerRoot == previousRootPc`).
**Pass 1 was the producing pass for every target region** (no Pass 2/2b reprocessing
at any target tick), so all numbers below are P1.

Quality codes: 1=Major, 2=Minor, 3=Diminished, 4=Augmented, 5=HalfDiminished,
8=Power. "margin" = within-winning-bass-group `rawCandidates[0].score − [1].score`.

---

## Table 1 — Δ=+7 predecessor confidence data

Predecessor = the region immediately preceding the failing region in the analysis
stream (the region whose root became `previousRootPc`).

| Score | Predecessor tick | Pred rootPc | pcWeight[rootPc] | Pred winScore | Pred runScore | Pred margin | Pred distinctPcs | Pred reading | Continuity caused the error? |
|---|---|---|---|---|---|---|---|---|---|
| **bwv245.28** | 3840 | 11 (B) | **0.6000** | 3.4200 | 3.4200 | **0.0000** | **3** | Bm (ii, correct) | **YES** (`contFired=1`) |
| **bwv296** | 21600 | 2 (D) | **0.6000** | 3.5200 | 3.5200 | **0.0000** | **3** | D (vi, correct) | **YES** (`contFired=1`) |
| **bwv320** | 36960 | 7 (G) | **0.8182** | 2.4009 | 2.4009 | **0.0000** | **2** | Gm (ii, correct, sparse) | **YES** (`contFired=1`) |
| bwv102.7 | 17040 | 10 (Bb) | 0.2500 | 3.4500 | 3.1125 | 0.3375 | 4 | Bb (predecessor of an Eb run) | **NO** (`contFired=0`) |
| bwv261 | 33360 | 2 (D) | 0.2000 | 3.4300 | 3.2600 | 0.1700 | 3 | D+ (predecessor of a C# run) | **NO** (`contFired=0`) |
| **mozart_k280-1 (control)** | 12480 (m9) | 0 (C) | **1.0000** | 2.1700 | 1.9083 | **0.2617** | **1** | C, single-PC Alberti slice | n/a (continuity is **correct** here) |
| mozart_k280-1 (control, m12) | 16800 | 0 (C) | 1.0000 | 2.1700 | 1.9083 | 0.2617 | 1 | C, single-PC Alberti slice | n/a (correct) |

### Failing-region data (where the wrong root is actually chosen)

| Score | Failing tick | winRoot | quality | pcWeight[winRoot] | winScore | runScore | margin | distinctPcs | previousRootPc | contFired | DCML root |
|---|---|---|---|---|---|---|---|---|---|---|---|
| bwv245.28 | 4320 | 11 (B) | 1 Maj | 0.6000 | 1.9200 | 1.9200 | 0.0000 | 3 | 11 (B) | **1** | 4 (E) |
| bwv296 | 23040 | 2 (D) | 1 Maj | 0.6000 | 1.9200 | 1.9200 | 0.0000 | 3 | 2 (D) | **1** | 7 (G) |
| bwv320 | 37440 | 7 (G) | 1 Maj | 0.6000 | 1.9200 | 1.9200 | 0.0000 | 3 | 7 (G) | **1** | 0 (C) |
| bwv102.7 | 17520 (run start) | 3 (Eb) | 1 Maj | 0.2500 | 3.0500 | 2.7250 | **0.3250** | 4 | 10 (Bb) | **0** | 8 (Ab) |
| bwv261 | 33600 (run start) | 1 (C#) | 5 HalfDim | 0.2500 | 2.6500 | 2.2875 | **0.3625** | 4 | 2 (D) | **0** | 6 (F#) |
| mozart m9 | 12720 | 0 (C) | 1 Maj | **0.0000** | 2.2000 | 2.2000 | 0.0000 | 2 | 0 (C) | **1** (correct) | 0 (C, V→V65) |
| mozart m12 | 17040 | 0 (C) | 1 Maj | **0.0000** | 2.7000 | 2.7000 | 0.0000 | 2 | 0 (C) | **1** (correct) | 0 (C, V→V65) |

Note the inversion at the failing-region level: the three **wrong** continuity
winners each have root pcWeight **0.60** (the wrong root is the bass, prominent),
while the **correct** mozart continuity winner has root pcWeight **0.00** (C is not
even sounding — the bonus is correctly sustaining V across an Alberti figure). A
failing-region root-pcWeight gate would therefore also misfire, in the wrong
direction.

---

## Table 2 — Failing-region confirmation

| Score | failing `previousRootPc` == predecessor `rootPc`? | failing `pcWeight[previousRootPc]` == predecessor `pcWeight[rootPc]`? |
|---|---|---|
| bwv245.28 | **Yes** (11 == 11) | Yes — 0.60 == 0.60 (coincidental: B is bass in both regions) |
| bwv296 | **Yes** (2 == 2) | Yes — 0.60 == 0.60 (coincidental: D is bass in both) |
| bwv320 | **Yes** (7 == 7) | **No** — failing 0.60 vs predecessor 0.82 (different tone sets; pcWeight is region-specific) |
| bwv102.7 | **No** — `previousRootPc=10 (Bb)`, winner `rootPc=3 (Eb)`; continuity did not reward the winner | n/a |
| bwv261 | **No** — `previousRootPc=2 (D)`, winner `rootPc=1 (C#)`; continuity did not reward the winner | n/a |

The Table-2 design assumed both equalities would hold for every case. Neither holds
universally: continuity does not even fire for two of the five (bwv102.7, bwv261),
and the `pcWeight` equality is coincidental (it holds only when the bass note is the
same in both regions, as in bwv245.28/bwv296) and fails outright for bwv320.

---

## Assessment

### Q1 — Do the 5 Δ=+7 predecessors share a pcWeight/margin pattern distinct from the mozart control?

**No.** Restricting to the three cases where continuity is actually the cause
(bwv245.28, bwv296, bwv320), the predecessor numbers are:

| metric | bwv245.28 | bwv296 | bwv320 | **mozart control** |
|---|---|---|---|---|
| pcWeight[root] | 0.60 | 0.60 | 0.82 | **1.00** |
| within-bass margin | 0.00 | 0.00 | 0.00 | **0.26** |
| distinctPcs | 3 | 3 | 2 | **1** |

On **pcWeight** the control is the **highest** of the set (1.00). On **distinctPcs**
the control is the **most sparse** (1). On both, the control lies at the extreme that
any "block the sparse/low-confidence predecessor" rule would target first. The two
metrics do not form a band that excludes the Δ=+7 predecessors while including
mozart.

### Q2 — Which metric separates them most cleanly? Is there a usable threshold?

- **Root pcWeight: fails.** All five predecessors and the control are ≥ 0.20, the
  three genuine-continuity predecessors are 0.60–0.82, and the control is 1.00. The
  proposed `pcWeight == 0.0 → kill bonus` rule **never fires** — no predecessor has
  pcWeight 0.0. There is no threshold that blocks {0.60, 0.60, 0.82} and passes 1.00.

- **Within-bass margin: superficially separates, but is unusable.** The three
  genuine cases all have margin **0.00**; mozart has **0.26**. A `margin < ~0.13`
  gate would block the three and pass mozart **on these data points**. But margin
  0.00 is **pervasive** across the corpus — it is produced by template ties at the
  top of the winning bass group (e.g. the guaranteed diff-root append at equal score,
  or two templates scoring identically), *not* by harmonic uncertainty. The
  predecessors in bwv245.28 and bwv296 are **confident, correct triads** (Bm, D) that
  happen to have margin 0.00. Gating the bonus on `predecessor margin == 0` would
  disable `rootContinuityBonus` for a large fraction of *all* regions, including the
  many correct continuity progressions whose predecessor is a clean triad — a massive
  regression risk, identical in spirit to the rejected Iter-98 attempts.

- **distinctPcs: fails (re-confirms Iter 98).** {3, 3, 2} for the wrong cases vs **1**
  for the control. The control is more sparse than every wrong case. No threshold
  separates them.

### Q3 — Any Δ=+7 predecessor that resembles the mozart control?

Yes — and worse than "resembles": **bwv320's predecessor is closer to mozart than to
its own siblings.** bwv320 (2-PC, pcWeight 0.82) is the only genuinely sparse
predecessor and is the structural twin of the mozart Alberti slices (1-PC,
pcWeight 1.0). They are the two cases a confidence/sparsity gate would treat
identically — one must be blocked, the other preserved — which is precisely why no
predecessor-side metric can tell them apart. Conversely bwv245.28 and bwv296 do **not**
resemble the control at all: they are full 3-PC triads. The set is internally
inconsistent, so a single predecessor-confidence rule cannot cover it.

### Q4 — What would the proposed scaling logic look like, and would it work?

The proposed logic was:
- `previousWinnerRootPcWeight == 0.0` → bonus = 0
- `previousWinnerMargin < kThreshold` → reduced bonus

**It would not work.**
- The `pcWeight == 0.0` clause is **dead** for this cluster: no predecessor has
  pcWeight 0.0 (range 0.20–0.82, control 1.00).
- The `margin < kThreshold` clause **would** suppress all three genuine cases (margin
  0.0) and preserve mozart (0.26) on these specific points, but only because margin
  0.0 is the corpus-wide default; applying it globally would strip the bonus from
  most correct continuity progressions (whose confident-triad predecessors also have
  margin 0.0). It is not a "low-confidence" signal.
- Even if it worked, it would still miss **bwv102.7 and bwv261 entirely**, because
  those errors are vertical, not continuity-driven (Q5).

No safe `(pcWeight, margin)` threshold pair exists that blocks the three genuine
Δ=+7 cases without (a) being a no-op on the pcWeight clause and (b) over-firing the
margin clause across the corpus.

### Q5 — Unanticipated structural mismatch in the data

Two, both significant:

1. **The cluster is not homogeneous in mechanism.** Only **3 of 5** (bwv245.28,
   bwv296, bwv320) are rootContinuity-caused. **bwv102.7** (Eb beats Ab vertically,
   margin 0.325, `contFired=0`) and **bwv261** (C# beats F# vertically, margin 0.363,
   `contFired=0`) choose the wrong root on **vertical evidence at the run's first
   sub-region**; the continuity bonus only carries the wrong root forward into the
   run's later sub-regions (`contFired=1` on those, but they merely echo an
   already-decided error). A `rootContinuityBonus` change is the wrong tool for these
   two — they need a vertical-scoring fix (why does an Eb-major / C#-halfdim reading
   outscore the Ab / F# reading on the bass note Ab / F#?).

2. **The genuine-continuity predecessors are correct, confident chords — the bonus is
   firing from good context.** The diagnostic's framing ("a wrong/sparse predecessor
   commits to rootPc=X and the bonus rewards staying on X") holds only for bwv320.
   For bwv245.28 and bwv296 the predecessor (Bm = ii, D = vi) is the *right* answer;
   the +0.40 bonus then over-rewards staying on that root into a region where the
   **bass has moved and the harmony has genuinely changed**. The failing regions are
   exactly the ambiguous ones where the rewarded fifth-related root is still a real
   chord tone:
   - bwv245.28 t4320 {E, G#, B}, bass **G#**: correct E/G# (V6) vs continued B (ii).
   - bwv296 t23040: correct G vs continued D.
   - bwv320 t37440: correct C (V6) vs continued G.

   In every case the bass note is **not** the bass of the predecessor and points to
   the *correct* (new) root, while the rewarded root is the old one. The
   discriminating signal lives in the **failing region's bass motion**, not the
   predecessor's confidence: `rootContinuityBonus` currently has *no stepwise/bass
   gate* (noted in `regionanalyzer.h` L121). The promising direction is to withhold
   (or scale down) the bonus when the candidate it would reward is a **non-root-position**
   reading whose bass differs from the previous region's bass — i.e. when staying on
   the old root forces an inversion over a bass that better supports a new root. That
   is a failing-region structural gate, not a predecessor-confidence scale.

---

## Recommendation

Abandon the predecessor-confidence scaling approach (pcWeight and within-bass margin
both fail the falsification test; distinctPcs is re-confirmed dead). Split the cluster:

- **bwv102.7, bwv261** — not continuity bugs. Defer to a separate vertical-scoring
  investigation (Ab/F# bass-root reading vs Eb/C# reading).
- **bwv245.28, bwv296, bwv320** — investigate a **bass-aware gate on
  `rootContinuityBonus`**: do not grant the +0.40 to a candidate whose root equals
  `previousRootPc` when that candidate is non-root-position (`bassPc != rootPc`) and
  the current bass differs from `previousBassPc`. This must be corpus-validated on
  both presets (the mozart Alberti control sustains V *with the same bass moving
  within a single harmony*, so a bass-change condition is exactly what separates it
  from these three) before any commit.

All numbers above are reproducible: `tools/characterise_bir_false.py` for case
identification; the `[DIAG]` instrumentation described in *Method* (now removed) for
the confidence data.
