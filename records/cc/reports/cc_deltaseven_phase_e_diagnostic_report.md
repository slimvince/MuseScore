# Δ=+7b Phase E Diagnostic — Report

**Date:** 2026-06-08
**Type:** read-and-diagnose pass. No commits. A temporary `fprintf` diagnostic was
added to `harmonicfunctionlayer.cpp` (top of `applyHarmonicFunction`, before the
competition loop), data collected, then removed. Working tree confirmed clean
afterwards: `harmonicfunctionlayer.cpp` and `regionanalyzer.cpp` byte-identical to
HEAD (only pre-existing `CLAUDE.md` edit remains).
**Preset:** Baroque for all four scores (to keep bonus magnitudes comparable, per
the predecessor diagnostic).
**Build:** `setup_and_build.bat` exit 0. `batch_analyze` run per score; stderr
(diagnostic) captured separately from stdout (regions JSON).

---

## TL;DR — the instruction's premise is wrong, and that is the key finding

The instruction states the three Δ=+7b cases are *"a near-tie (~1.92 vs ~1.92)…
and `rootContinuityBonus` (+0.40) breaks the tie toward the predecessor's root."*

**The raw (pre-rcb) scores are NOT a near-tie.** In every one of the three failing
regions the **raw vertical winner is the DCML-correct root** (raw = 1.90, a complete
triad), and the continued/predecessor root is a **poor** vertical fit (raw = 1.52,
bare-root match only). `rootContinuityBonus` contributes a full **+0.40**
(complexityFactor = augFactor = 1.0, so `rcbEff` = 0.40 exactly), which **reverses a
clear 0.38 raw victory** for the correct answer into a 0.02 loss:

```
continued root:  raw 1.52  + rcb 0.40  = 1.92   ← wins
correct root  :  raw 1.90  + rcb 0.00  = 1.90   ← loses by 0.02
```

So rcb is not breaking a tie — it is **overturning a decision the vertical scorer got
right**. The "~1.92 vs ~1.92 near-tie" is the *post-rcb* state only.

**The mozart_k280-1 control has the identical mechanism** (rcb also reverses the raw
winner — `E min`/`GSus4` → `C`), yet it is **correct** there. The single property that
cleanly separates the wrong cases from the correct control is **whether the bass note
of the rcb-rewarded continued candidate is a chord tone of that candidate's own
chord**:

| | Bach failing (×3) | mozart control (×4) |
|---|---|---|
| rcb reverses the raw winner? | yes | yes |
| continued winner's bass ∈ its own chord tones? | **NO** (G#∉B, B∉D, E∉G) | **YES** (G=5th of C, E♭=3rd of Cm) |
| continued winner `basisDep` | 0.00 | 0.40–0.90 (or structurally a chord tone even when 0) |

The promising Phase-E lever is therefore a **within-region structural gate**: do not
grant `rootContinuityBonus` to a candidate whose bass is **foreign to its own
template** (a "nonsense slash" voicing). This is immune to the Alberti-bass regression
that killed the Iter-98 and predecessor-bass approaches, because in Alberti the
continued root is always voiced over *its own* chord tones.

---

## Method

Temporary read-only `fprintf` ("`[PEd]`") inserted at the top of
`applyHarmonicFunction` (`harmonicfunctionlayer.cpp`), before the competition loop.
For each gated region it printed one header line + one line per candidate cell.

**Total formula (matches Pass A exactly).** rcb is added into `basisIndep` *before*
the `complexityFactor × augFactor` multiply, so its score effect is `rcb·cf·af`, not a
flat `rcb`. The dump reports:
- `raw  = (basisIndep + basisDep)·cf·af + wComplete`  (vertical only, no progression signal)
- `rcbEff = rcb·cf·af`  (actual score delta from rootContinuity)
- `wseq` (sequential bonus)
- `total = raw + rcbEff + wseq`  (= the real competition score for non-wDim cells)

**Region gating.** No tick is available in this layer (confirmed: neither
`ScoringSnapshot` nor `HarmonicFunctionContext` nor `gateCtx` carries a tick/region
id; the snapshot is built from raw tones+key only). The fallback compound gate from
the instruction was used — `!explorationMode && (previousRootPc, distinctPcs)` for
each target — and the failing region was then identified in the dump by its
`(winner root, winner bass)` fingerprint (cross-checked against the live regions JSON:
bwv245.28 → `B/G#`, bwv296 → `D/B`, bwv320 → `G/E`). A transparent floor (`total ≥
1.0`) dropped non-competitive junk cells; no relevant candidate was near the floor
(winners ≈ 1.9, controls ≈ 2.0–2.7).

Quality codes: 1=Major 2=Minor 3=Dim 4=Aug 5=HalfDim 6=Sus2 7=Sus4 8=Power.
PC: 0=C 1=C♯ 2=D 3=E♭ 4=E 5=F 6=F♯ 7=G 8=A♭/G♯ 9=A 10=B♭ 11=B.

All three failing regions are **single-bass** (`nCells = 204 = 1 bass × 12 roots × 17
templates`); the bass is fixed and the competition is purely root × template within
that one bass.

---

## Table 1 — Full candidate scores for each failing region

Only the competitive cells are shown (the rest are junk below the 1.0 floor). Within
each root, all qualities tie on `basisIndep` when only the root PC is present, so the
quality of the bare-root continued winner is decided purely by `tiePriority`
(Major = template 0 sorts first) — it is **not** a confident quality call.

### bwv245.28 — failing region t4320 (bass = G♯)
DCML expected **E** (root 4, V6 = `E/G♯`); ours **B** (root 11, `B/G♯`); BIR=false, Δ=+7.

| Role | Root | Qual | Bass | bI | bD | cf | af | raw | rcb | rcbEff | wseq | **Total** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **our winner** / predecessor-continuation (root==prevRoot) | B (11) | Maj | G♯ | 1.520 | 0.000 | 1.0 | 1.0 | 1.5200 | 0.40 | 0.4000 | 0 | **1.9200** |
| **DCML-expected** / RAW winner | E (4) | Maj | G♯ | 1.900 | 0.000 | 1.0 | 1.0 | **1.9000** | 0.00 | 0.0000 | 0 | 1.9000 |
| (also-ran) | A♭ (8) | Min | G♯ | 1.620 | 0.210 | 1.0 | 1.0 | 1.8300 | 0.00 | 0.0000 | 0 | 1.8300 |

### bwv296 — failing region t23040 (bass = B)
DCML expected **G** (root 7, `G/B` = I6 or V6); ours **D** (root 2, `D/B`); BIR=false, Δ=+7.

| Role | Root | Qual | Bass | bI | bD | cf | af | raw | rcb | rcbEff | wseq | **Total** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **our winner** / predecessor-continuation | D (2) | Maj | B | 1.520 | 0.000 | 1.0 | 1.0 | 1.5200 | 0.40 | 0.4000 | 0 | **1.9200** |
| **DCML-expected** / RAW winner | G (7) | Maj | B | 1.900 | 0.000 | 1.0 | 1.0 | **1.9000** | 0.00 | 0.0000 | 0 | 1.9000 |
| (also-ran) | B (11) | Min | B | 1.620 | 0.210 | 1.0 | 1.0 | 1.8300 | 0.00 | 0.0000 | 0 | 1.8300 |

### bwv320 — failing region t37440 (bass = E)
DCML expected **C** (root 0, `C/E` = V6/I6); ours **G** (root 7, `G/E`); BIR=false, Δ=+7.

| Role | Root | Qual | Bass | bI | bD | cf | af | raw | rcb | rcbEff | wseq | **Total** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **our winner** / predecessor-continuation | G (7) | Maj | E | 1.520 | 0.000 | 1.0 | 1.0 | 1.5200 | 0.40 | 0.4000 | 0 | **1.9200** |
| **DCML-expected** / RAW winner | C (0) | Maj | E | 1.900 | 0.000 | 1.0 | 1.0 | **1.9000** | 0.00 | 0.0000 | 0 | 1.9000 |
| (also-ran) | E (4) | Min | E | 1.620 | 0.210 | 1.0 | 1.0 | 1.8300 | 0.00 | 0.0000 | 0 | 1.8300 |

**Pattern (all three identical):** the bass note is the **major third of the
DCML-correct chord** (G♯ of E; B of G; E of C), so the region is a first-inversion
complete triad of the correct root (`bI = 1.90`). The continued/predecessor root is a
**bare-root match** (`bI = 1.52`) whose bass is **foreign to it**, and it wins solely
because `rcb` (+0.40) > the raw margin (0.38) by which the correct triad leads.

---

## Table 2 — Context values at each failing region

| Score | previousRootPc | previousQuality | nextRootPc | consecutiveBassStepwise | regionMetricWeight | distinctPcs |
|---|---|---|---|---|---|---|
| bwv245.28 | 11 (B) | **Minor** (Bm = ii) | 4 (E) | 0 | 0.750 | 3 |
| bwv296 | 2 (D) | **Major** (D = vi) | 0 (C) | 2 | 0.750 | 3 |
| bwv320 | 7 (G) | **Minor** (Gm = ii) | 0 (C) | 0 | 1.000 | 3 |

Note: `nextRootPc` ≠ `previousRootPc` (the continued/wrong root) in all three —
the wrong root has no future either (see Q5).

---

## Table 3 — mozart_k280-1 control (rcb fires correctly)

All control regions are `previousRootPc = 0 (C)`, `distinctPcs = 2`, root **C = V** in
F major (a dominant pedal sustained across an Alberti figure; the instruction's "IV
region" label is a mislabel — the chord is V/C, matching the predecessor diagnostic's
"V→V65"). 25 such regions exist; 4 representative ones shown.

| # | prevRoot | prevQual | nextRoot | stepwise | metricW | winner | winner bass | bass ∈ chord? | RAW winner (no rcb) | rcb decisive? |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | C | Maj | C | 1 | 0.500 | C Maj/G  (1.80→**2.20**) | G | **yes** (5th) | E min/G (2.00) | **yes** (flips E→C) |
| 2 | C | Maj | – | 1 | 0.500 | C Maj/G  (2.30→**2.70**) | G | **yes** (5th) | E min/G (2.50) | **yes** (flips E→C) |
| 3 | C | Min | – | 0 | 1.000 | C min/E♭ (2.315→**2.715**) | E♭ | **yes** (3rd) | E♭Sus4/E♭ (2.15) | **yes** (flips E♭→C) |
| 4 | C | Maj | – | 0 | 0.500 | C Pow/G  (2.00→**2.40**) | G | **yes** (5th) | GSus4/G (2.07) | **yes** (flips G→C) |

**Crucial:** in mozart, rcb reverses the raw winner *just as in the Bach cases*, but
the rcb-promoted continued root C is voiced over **its own chord tones** (G = 5th, E♭ =
3rd). The continued root is a real (sparse) harmony, not a nonsense slash.

---

## Assessment — answers to the seven questions

### Q1 — Is the near-tie BEFORE rcb, or does something else contribute?

**Neither — there is no raw near-tie.** The raw scores are **1.90 (correct) vs 1.52
(continued)** — a 0.38 gap *favoring the correct answer*. The only post-scoring bonus
in play is `rcb`: `wseq = 0`, `wDim = 0`, `wComplete = 0`, and `basisDep = 0` on both
top candidates. `rcb` alone (+0.40, full strength since cf=af=1.0) converts the
correct candidate's clear 0.38 raw lead into a 0.02 loss. The "1.92 vs 1.90 near-tie"
exists **only after** rcb is applied. rcb is reversing a correct vertical decision, not
breaking a tie.

### Q2 — Does wSeqBonus fire? Is there a V→I with nextRootPc?

**wSeq does not fire for any candidate** in any of the three regions — it requires
`distinctPcs ≥ 4`, and all three failing regions have `distinctPcs = 3`. So wSeq is
**structurally disabled** here and cannot be a lever without lowering that gate (which
§4 documents as load-bearing — do not).

Were it active, it would be **inconsistent** across the three (it rewards a candidate
whose root is a P4 below `nextRootPc`):
- bwv296: would reward the **correct** G (G→C = V→I). ✓
- bwv320: would reward the **wrong** G (G→C); the correct C→C is no motion. ✗
- bwv245.28: would reward the **wrong** B (B→E looks like V→I); correct E→E is no motion. ✗

So even if enabled, wSeq is not a clean fix (helps 1, hurts 2).

### Q3 — consecutiveBassStepwiseCount vs mozart? Usable gate?

**No.** Failing regions = {0, 2, 0}; mozart controls = {1, 1, 0, 0}. A
`consecutiveBassStepwiseCount > 0 → reduce rcb` gate would (a) **miss** bwv245.28 and
bwv320 (both 0) and (b) **regress** mozart #1/#2 (both 1). No separation — fails the
falsification test against the control.

### Q4 — previousQuality at the failing regions? Resolution target?

Failing = {Minor (Bm=ii), Major (D=vi), Minor (Gm=ii)}; mozart = {Maj, Maj, Min, Min}.
**No separation** — both sets contain Major and Minor predecessors. Two of three are
`ii → V` (Bm→E, Gm→C), which is a clean functional motion, but a "minor predecessor ⇒
expect resolution" rule does not exclude mozart (which also has a minor predecessor,
control #3) and would not catch bwv296 (major predecessor). Not a usable single
discriminator.

### Q5 — nextRootPc consistent with the DCML chord?

Yes, and informatively so:
- bwv245.28: `nextRoot = E` **= DCML root (E)** — the correct V6 continues to E.
- bwv296: `nextRoot = C`; DCML root = G; **G→C = V→I** (DCML chord is the dominant of next).
- bwv320: `nextRoot = C` **= DCML root (C)** — the correct chord continues to C.

In every case `nextRoot ≠ previousRoot` (the wrong/continued root): the continued root
**has no future** — it neither matches the next region nor resolves to it — whereas the
correct root either continues forward (245, 320) or resolves V→I (296). A forward
look-ahead ("the continued root is a dead end; the correct root is not") *would*
separate these, but note `wseq` already encodes part of this and is gated off at
distinctPcs=3.

### Q6 — Shared pattern that cleanly separates the three from mozart?

**Yes — the bass note's relationship to the rcb-rewarded chord.** The continued-root
winner is, in all three Bach cases, a **slash voicing with a bass foreign to the
continued chord**:

| Score | continued root | winner bass | bass ∈ tones(continued root)? |
|---|---|---|---|
| bwv245.28 | B {11,3,6} | G♯ (8) | **no** |
| bwv296 | D {2,6,9} | B (11) | **no** |
| bwv320 | G {7,11,2} | E (4) | **no** |
| mozart (all) | C {0,4,7} / Cm {0,3,7} | G (7) / E♭ (3) | **yes** |

Equivalently: the Bach continued winners have `basisDep = 0` (no inversion/bass bonus,
because the bass is not a chord tone), while the mozart winners have `basisDep =
0.40–0.90` (legitimate inversion) — and even mozart control #4, where `basisDep`
happens to be 0, has a **structurally** valid chord-tone bass (G = 5th of C). The
structural test ("`bassPc` ∈ template tones of the candidate") is therefore stronger
than a `basisDep > 0` test and separates all four controls from all three failing
cases.

This is the predecessor report's recommendation, **refined and corrected**. The
predecessor report proposed gating on `bassPc ≠ rootPc AND bassPc ≠ previousBassPc`
(bass changed from the previous region). That is the Iter-98 echo `redesign_plan.md`
warns against, and it **does** misfire on Alberti (the bass moves every beat, so
`bassPc ≠ previousBassPc` fires indiscriminately). The **foreign-bass** test is
different: it asks whether the bass belongs to the *continued chord itself*, a
within-region property. In Alberti the dominant is voiced over its own tones (C/E/G),
so the foreign-bass test never fires there — exactly the separation we need.

### Q7 — Structural surprises not anticipated

1. **The instruction's "raw near-tie" framing is inverted.** The vertical scorer
   already ranks the correct answer first by a clear 0.38; rcb (0.40) is *strong enough
   to overturn a correct first-inversion complete-triad reading*. This reframes the fix:
   the goal is not "break a tie better" but "stop rcb from overriding a clearly-better
   vertical reading." A simple **margin guard** would also work mechanically (rcb's
   +0.40 should not flip a candidate that trails the raw leader by > ~0.30), but the
   foreign-bass structural test is cleaner and better-motivated.

2. **rcb reverses the raw winner in the mozart control too** — the control is *not* a
   case where rcb merely confirms the vertical winner. It flips `E min → C` (#1/#2),
   `E♭Sus4 → Cm` (#3), `GSus4 → C` (#4) — i.e. rcb is genuinely load-bearing and
   decisive for the *correct* answer in mozart. Any fix must preserve rcb's ability to
   reverse the raw winner **when the continued root is a legitimately-voiced chord**.
   This is why a blunt "reduce rcb" or "cap rcb" approach is dangerous and the
   discriminator must be structural.

3. **The continued winner's quality is arbitrary.** With only the continued root PC
   present, every quality (Maj/Min/Dim/Sus2/Sus4) scores `bI = 1.52`; the winner's
   "Major" label is just `tiePriority` ordering (template 0). The analyzer is not
   asserting a B/D/G *major* chord — it is asserting "some chord rooted on the old
   root," propped up entirely by rcb over a foreign bass. This reinforces that the
   reading is a vertical non-entity.

4. **All three failing regions are first inversions of the correct chord** (bass = M3
   of the DCML root: E/G♯, G/B, C/E). The correct complete-triad candidate is already
   present in the candidate list at the same bass with the top raw score — the fix does
   not need to *find* a new candidate, only to stop rcb from demoting the one already
   winning.

---

## Recommendation (diagnostic only — no code written)

The Δ=+7b cluster is a **single mechanism**: `rootContinuityBonus` (+0.40) overturning
a clearly-superior first-inversion complete triad of the correct root, in favor of a
bare-root continuation voiced over a **foreign bass**. The clean, control-safe Phase-E
lever is a **within-region structural gate**:

> Do not grant (or sharply reduce) `rootContinuityBonus` to a candidate whose
> `bassPc` is **not a chord tone of that candidate's own template** (root/3rd/5th/…),
> i.e. a non-chord-tone "slash" voicing.

This fires on all three Bach cases (bass G♯/B/E foreign to B/D/G) and on **none** of
the mozart controls (bass G/E♭ is the 5th/3rd of C/Cm). It is independent of
predecessor confidence, predecessor bass, and `distinctPcs`, so it sidesteps the
Iter-98 / predecessor-bass dead ends. It must still be corpus-validated on both presets
before any commit (per `redesign_plan.md` — the mozart falsification test is necessary
but not sufficient).

A `basisDep > 0` gate is a near-equivalent shortcut but is weaker (control #4 has
`basisDep = 0` yet a valid chord-tone bass); prefer the explicit template-tone test.

All numbers reproduce via `batch_analyze … --preset Baroque` with the (now removed)
`[PEd]` instrumentation described under *Method*.
