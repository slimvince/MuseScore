# CC Dossier — B: #4 dominant/subdominant guard — SCOPING (READ-ONLY, measure-first)

> **HELD — gitignored, no commit. No code change, no guard built, no wiring change. HEAD unchanged
> (`5fee657578`, the dormant J-key-iii wiring just pushed to origin/master).** This dossier answers the
> instruction-B questions: it locates the I→IV / I→V over-detection at source, characterizes the
> key-agnostic discriminator, MEASURES its separability (the load-bearing gate), runs the convergence check,
> and — on the strength of that measurement — specifies the #4 guard design (where it can/can't go).
>
> **Date:** 2026-06-16. Every number tagged `[code]` (read source), `[probe]` (ran a script), `[oracle]`
> (When-in-Rome DCML GT). Surface: `tools/corpus/default_mod` (WiR-Bach Default, 326/353 covered) + the 3
> snapshot regression scores. New read-only measurement tool: `tools/cc_b_guard_separability.py`
> (reuses `compare_rn`/`compare_analyses`/`dcml_parser` verbatim; changes nothing).

---

## 0. Headline — the gate gives a SPLIT verdict (surface for direction)

The tonicization-vs-modulation discriminator the #4 guard needs is **separable for the SUBDOMINANT (I→IV)
half but NOT for the DOMINANT (I→V) half**, on the currently-available key-agnostic signals:

| over-detection | snapshot case | separable? | measured effect of suppressing it (4d-i region frame) |
|---|---|---|---|
| **subdominant (I→IV)** | mozart_k279 (C→**F**), bwv806_gigue (A→**D**) | **YES, net-positive** | precision **47.0 → 51.0 %** (+4.0 pp), recall 33.4 → 31.1 % (−2.3 pp) |
| **dominant (I→V)** | corelli_op01n08a (Cm→**Gm**) | **NO** | precision **47.0 → 45.2 %** (−1.8 pp, *worse*), recall 33.4 → 26.8 % (−6.6 pp) |

1. **The subdominant guard is buildable and convergent** — suppressing subdominant-of-anchor modulation
   spans removes 43 spurious spans for 17 genuine ones, *raises* the in-scope 4d-i modulation precision +4 pp,
   and fixes **2 of the 3 snapshot regressions** (mozart F, bwv806 D — both confirmed subdominant-of-anchor).
   But it does cost **17 genuine Bach modulations to IV** (−2.3 pp recall) — a real trade-off to surface (§5).
2. **The dominant guard is NOT separable** — dominant-of-anchor spans are **66 % genuine modulations to V**
   (49 TP / 25 FP): Bach modulates to the dominant constantly, so blanket suppression *lowers* precision and
   kills 22.6 % of all true modulations. The finer key-agnostic signals (confirming-cadence count,
   return-to-home) do **not** separate genuine V-modulations from V-tonicizations. **corelli's Gm tail is a
   dominant span and is NOT safely suppressible** without breaking Bach V-modulation precision.
3. **Stop conditions fire on BOTH counts** (instruction §5): the subdominant guard *suppresses genuine Bach
   modulations* (the recall trade), and the dominant half *has no separating threshold*. Per §5 these are
   **surfaced for a user/Cowork direction call**, not unilaterally built.
4. **Recommended path** (§4): build the **subdominant guard** (the measured net-positive half — it unblocks
   the 2 subdominant snapshot regressions, the dominant Bach-modulation precision is untouched), gated on a
   confident anchor, with a **dominant-seventh structural refinement** (hypothesized, measure at build) to
   recover the lost IV-modulation recall. Treat the **dominant (i→v) over-commit as the unresolved
   calibration wall** — defer it (it is the same precision ceiling 4c/4d/J-key-ii-redux hit), do not flip the
   global wiring ON until at least the dominant case is non-regressing or the wiring is scoped (Step-3 option
   A/C).

**One-line answer:** the #4 guard is real and worth building for the **subdominant** (separable, convergent,
fixes mozart+bwv806), but the **dominant** half (corelli i→v) is **measured-unseparable** on key-agnostic
signals — so the guard alone does not clear the global flip-ON; the dominant case needs scoping or a learned
emission. **Surfaced, no code.**

---

## 1. The over-detection at source (instruction §3.1, question 1) `[code]`

### 1.1 Root cause — the descending-fifth + leading-tone test cannot tell I→IV/I→V from V→I without a key

`detectAuthenticCadences` ([cadencekeyanchor.cpp:61-123](src/composing/analysis/section/cadencekeyanchor.cpp#L61-L123))
registers an authentic cadence for an adjacent region pair `a → b` when **all** of:
- `a.quality == ChordQuality::Major` (`:83`) — the candidate dominant is a major triad (admits V and V7);
- `b.quality ∈ {Major, Minor}` (`:90`) — a stable triad resolution target;
- **descending perfect fifth** `pcMod12(a.rootPc − 7) == b.rootPc` (`:95`);
- the **leading tone** `leadingTone = pcMod12(a.rootPc + 4)` is physically present in `a`'s pitch mask (`:103-104`).

**The trap:** a plain **I→IV** progression satisfies every test. Take C major → F major (I→IV):
- `a` = C major → `Major` ✓;
- `b` = F major → `Major` ✓;
- `root(F)=5 == pcMod12(root(C)−7) = pcMod12(−7) = 5` ✓ (a I→IV ascending fourth IS a descending fifth mod 12);
- `leadingTone = root(C)+4 = 4 = E`, and **E is the major third of C, always present in a C-major triad** —
  and E is by construction one semitone below F, i.e. F's leading tone. The test `pcInMask(C-triad, E)` is
  trivially true (`:104`).

So **every C→F (tonic→subdominant) motion fires as a spurious "authentic cadence to F."** The major third of
*any* major triad is the leading tone of the chord a perfect fourth above it, so the leading-tone test —
designed to confirm a genuine V→I — **cannot** discriminate I→IV from V→I. This is the structural ambiguity:
the cadence detector is key-agnostic by design (it has no home to compare against), and *without a home* the
descending-fifth motion C→F is identical whether C is the tonic (→ I→IV) or the dominant (→ V→I in F).

The **I→V / V-tonicization** case is the mirror image: a cadence to the dominant region (e.g. a D7→G in C
major, V/V→V) fires the same test for "a cadence to G," and a half-cadence region sequence that lands a
major-quality dominant a fifth above some pc registers that pc as a local tonic.

### 1.2 How the spurious cadence becomes a committed span and then a key flip

1. The spurious "cadence to F/V" enters the per-cadence candidate list and **also votes in
   `aggregateGlobalAnchor`** ([cadencekeyanchor.cpp:147-230](src/composing/analysis/section/cadencekeyanchor.cpp#L147-L230)).
2. `detectLocalModulations`
   ([localmodulationdetector.cpp:116-230](src/composing/analysis/section/localmodulationdetector.cpp#L116-L230))
   assigns regions to the nearest consistent cadence (`:145-176`) and **commits a span** when a run is
   SUSTAINED (`runChords >= kEstablishmentMinChords=5`, `:45`,`:212`) AND CONFIRMED (≥1 cadence of that key
   inside, `:212`). A diatonic I↔IV oscillation trivially clears both: C-major and F-major regions are mutually
   collection-consistent (`kPitchTolerance=2`, `:46`,`:111`; C and F collections differ by only Bb/B♮), and the
   spurious C→F "cadence" is the confirmation. → a spurious **F (subdominant) span** is committed.
3. The committed span is added to the joint-key lattice as a candidate state
   ([jointkeydecision.cpp:230](src/composing/analysis/section/jointkeydecision.cpp#L230)) and given a soft
   bonus to its covered regions (`w.modulation`, `:276-280`); when the Viterbi routes through it, the wired
   SOFT key (`applyJointKeyWiring`) flips those regions to the IV/V — the snapshot regression.

**The guard's home: the anchor is computed FROM the cadences**, so a guard *cannot* reject the I→IV cadence at
`detectAuthenticCadences` (no home yet). It must run **after** `aggregateGlobalAnchor`, i.e. as a commit-time
filter in `detectLocalModulations` (which has both `result.anchor` and the spans, and already tags each span
`agreesWithAnchor` against that anchor — `localmodulationdetector.cpp:221-223`). See §4.

---

## 2. Confirmation on the 3 regression scores (instruction §3.1, question 1, dumps) `[probe][oracle]`

`batch_analyze --preset Default --dump-modulation --dump-cadence-anchor --dump-joint-key` on each score:

| score | GT (oracle) | anchor (key-agnostic home) | spurious IV/V span the detector commits | relation to anchor |
|---|---|---|---|---|
| **mozart_k279_1** | **C major** (DCML `globalkey=C`, localkey I throughout mm 1–16) | C maj (conf 0.679; 8 cadences = 5→C + **3→F**) | **F maj** `[0..35280]` estab=13 confCad=2; F maj `[88320..98160]` estab=5 confCad=1 | **subdominant** (F = C+5) |
| **bwv806_gigue** | **A major** (DCML `globalkey=A`, localkey I/V/I; D never appears) | A maj (conf 0.533; 6 cadences = 3→A + **3→D**) | **D maj** `[3840..10680]` estab=7 confCad=2; D maj `[41280..46080]` estab=5 confCad=1 | **subdominant** (D = A+5) |
| **corelli_op01n08a** | **C minor** (DCML `globalkey=c`, localkey i for all 16 mm) | C min (conf **0.423**; 15 cadences, incl. 3→Gm) | **G min** `[7680..15840]` estab=12 confCad=3 | **dominant** (Gm = Cm+7) |

- The "→F" / "→D" cadences are exactly the **I→IV misreads** of §1.1 (C→F, A→D); the "→Gm" cadences are the
  **V/v→v** dominant-region reads. All three spurious spans pass establishment + confirmation.
- **Path note (important):** the Step-3 snapshot regressions were measured on the **bridge/notation path**
  (`MUSE_JOINT_KEY_WIRING=1 pipeline_snapshot_tests`), whose measure-aligned segmentation differs from the
  batch path. Under the **batch** `--dump-joint-key` (Default), the wired SOFT decision flips only corelli
  (Cm→Gm on 37/47 regions, `modulationContributed` on 12); mozart/bwv806 SOFT stays home (the batch lattice's
  signature+anchor prior out-weighs the F/D spans there). The **raw modulation-detector over-detection is
  path-independent** (all 3 commit the IV/V span), and it is the span that flips the notation path — so the
  guard belongs at the detector, where it fixes both paths. `[probe]`

---

## 3. The discriminator + the separability measurement (instruction §3.2, §3.3 — the load-bearing gate) `[probe][oracle]`

### 3.1 Candidate key-agnostic signals (§3.2)
A genuine modulation to IV/V is *sustained + cadence-in-target + does not immediately return home*; a
tonicization is brief/passing. The 4d-i detector already requires sustained (≥5) + cadence-in-target (≥1), and
the over-commits **pass** those. The remaining key-agnostic signals available without a rebuild:
- **relationship of the span's local key to the cadence ANCHOR** (subdominant = anchor+5; dominant = anchor+7;
  relative; parallel; foreign) — the anchor is cadence-derived, never a resolved key, so this is key-agnostic;
- **confirming-cadence count** of the span (`confirmingCadenceCount`);
- **return-to-home** (an anchor-home span starts after this span ends);
- **anchor confidence** (`aggregateGlobalAnchor` weight share).

### 3.2 The separability table — anchor-relationship × DCML verdict `[probe][oracle]`
All 326 WiR-Bach pieces, 414 DCML-scorable modulation spans
(`tools/cc_b_guard_separability.py tools/corpus/default_mod`):

```
rel\verdict        TP   FP-overmod  FP-wrongkey   total   TP%
dominant            49         12          13      74     66%   <- genuine V-modulation dominates
subdominant         17         34           9      60     28%   <- mostly spurious (the I->IV misread)
relative            63         26          12     101     62%
parallel             1          7           0       8     12%
foreign             36         24          29      89     40%
exact-home          51         24           7      82     62%
```

The asymmetry is the whole story: **subdominant spans are 72 % wrong, dominant spans are 66 % right.** Bach
rarely *modulates* to IV (it tonicizes it briefly — exactly the over-detection), but modulates to V
constantly.

### 3.3 The candidate guard — suppress by anchor-relationship (region-level, 4d-i frame) `[probe][oracle]`
Region-level reproduces the published 4d-i baseline **exactly** (47.0 % precision / 33.4 % recall), validating
the measurement against the prior report:

```
baseline (no guard)   : nonHomeCommit=2867  precision=47.0%  recall=33.4%
suppress subdominant  : nonHomeCommit=2462  precision=51.0%  recall=31.1%   (+4.0 pp prec, -2.3 pp rec)
suppress dominant     : nonHomeCommit=2394  precision=45.2%  recall=26.8%   (-1.8 pp prec, -6.6 pp rec)
suppress dom+subdom   : nonHomeCommit=1989  precision=49.8%  recall=24.6%
```

- **Subdominant guard: PASS (net-positive, convergent).** +4.0 pp precision, −2.3 pp recall. It is *precision-
  raising* in the in-scope 4d-i frame → architecture-quality precision work, not a non-chorale patch.
- **Dominant guard: FAIL.** Precision *drops* 1.8 pp — it removes more genuine modulations than spurious ones.
- **The 3 snapshot over-commits all fall in the suppress bucket** (`tools/cc_b_guard_separability.py` snapshot
  section): mozart F, bwv806 D → **subdominant** (caught by the safe guard); corelli Gm → **dominant** (only
  caught by the unsafe guard).

### 3.4 Can a FINER signal rescue the dominant case (or sharpen the subdominant)? `[probe]`
Within the dominant and subdominant classes, the confirming-cadence count and return-to-home distributions:
```
dominant TP : confCad={1:40,2:7,3:2}  return_home={T:29,F:20}
dominant FP : confCad={1:24,2:1}      return_home={T:13,F:12}
subdominant TP: confCad={1:10,2:6,3:1} return_home={T:8,F:9}
subdominant FP: confCad={1:36,2:7}     return_home={F:20,T:23}
```
- **Dominant: NOT separable by these signals.** Both TP and FP are dominated by `confCad=1` (TP 40/49, FP
  24/25) and split ~evenly on `return_home`. Any threshold that kills the FPs kills as many or more TPs
  (`confCad<2` → kills 40 TP for 24 FP). The genuine V-modulations and the V-tonicizations look identical on
  every key-agnostic signal we have. **Confirmed unseparable → corelli not safely fixable this way.**
- **Subdominant: a `confCad`-gate does NOT help the snapshot fix.** `confCad<2` would keep the 7 strong TP
  (confCad≥2) — but the primary mozart/bwv806 over-commit spans have **confCad=2**, so a `confCad<2` gate
  would *fail to suppress them*. The blanket subdominant relationship (any confCad) is what catches them, at
  the 17-TP cost. → the recall trade is intrinsic to the relationship-only signal.

### 3.5 The structural refinement that COULD make the subdominant guard recall-clean (HYPOTHESIS — measure at build)
The I→IV misread reads the **home tonic chord as the dominant** of IV. A *genuine* V→IV modulation needs a
true **dominant seventh** of the target: for target T = anchor+5, the cadence's dominant is the home tonic
(pc = T+7 = anchor), and a genuine V7-of-T carries T's flat-7 = pc `(T+10) mod 12` = `(anchor+3) mod 12`
(e.g. C7→F needs B♭). A plain I→IV oscillation uses a **plain** major triad (no flat-7). So **requiring the
confirming cadence's dominant region to carry the target's flat-7** would separate genuine V7→IV (keep) from
plain I→IV (suppress) — recovering most of the 17 lost TP.
- This signal is **not in the current dump** (the cadence detector accepts bare `Major` quality, `:83`, and
  does not record the seventh). It is computable from the region `pcMask` at build time, or via a one-field
  read-only diagnostic addition — **a build-time probe, deliberately not run in this read-only step.**
- ⚠ It does **not** help the dominant case: a genuine V-modulation and a V-tonicization *both* use a real
  secondary dominant (e.g. D7→G), so the seventh is present in both. The dominant non-separability stands.

---

## 4. The #4 guard design (instruction §4 — framed as the next build instruction's spec)

**Where it sits:** a commit-time filter in `detectLocalModulations`
([localmodulationdetector.cpp](src/composing/analysis/section/localmodulationdetector.cpp), at the span-commit
block `:212-224`, after `agreesWithAnchor` is computed). It uses only `result.anchor` (cadence-derived,
key-agnostic) + the span's own fields → no resolved-key dependency, the §3 no-circularity rule holds. Equivalent
alternative: skip the span as a lattice state in `jointkeydecision.cpp:230` — but suppressing at commit is
cleaner (the span should not be asserted at all).

**The signal + provisional threshold `[empirical — Stage-5 fits]`:**
- **SUBDOMINANT guard (recommended to build):** suppress (do not commit / do not add as a key state) a
  modulation span S with `agreesWithAnchor == false` when `S.tonicPc == (anchor.tonicPc + 5) mod 12`
  (mode-aware), **gated on a confident anchor** (`anchor.confidence ≥ ~0.5` provisional — mozart 0.679 /
  bwv806 0.533 both clear it; this avoids firing on relative-pair-confused low-confidence anchors).
  - *Refinement (measure at build, §3.5):* only suppress when the confirming cadence's dominant region does
    **not** carry the target's flat-7 (i.e. it is a plain I→IV, not a V7→IV). Expected to cut the −2.3 pp
    recall cost substantially.
  - *Measured effect (relationship-only, no refinement):* 4d-i precision 47.0 → 51.0 %, recall 33.4 → 31.1 %;
    fixes mozart_k279 + bwv806_gigue.
- **DOMINANT guard: DO NOT BUILD as a suppressor.** Measured anti-convergent (precision 47.0 → 45.2 %). The
  i→v over-commit (corelli) is **not separable** from genuine V-modulation on key-agnostic signals (§3.4).

**What it unblocks / does NOT unblock:** the subdominant guard clears **2 of the 3** Step-3 snapshot
regressions and is precision-positive in-scope, so it is a real step toward the global flip-ON — but it does
**not** clear corelli (the dominant case), so on its own it is **insufficient to flip the wiring ON globally**.

---

## 5. Stop-condition trace (instruction §5) — what is surfaced

| condition | fired? | surface |
|---|---|---|
| Any code change / guard built / wiring change | **No** | read-only; HEAD `5fee657578` unchanged; only `tools/cc_b_guard_separability.py` (read-only measurement) + this dossier written |
| **No threshold separates over-commits from genuine modulations** | **YES — for the DOMINANT half** | dominant-of-anchor spans are 66 % genuine V-modulations; no key-agnostic signal separates them; corelli not safely suppressible. **Surfaced (§0, §3.4).** |
| **The guard would suppress genuine Bach modulations (breaks the in-scope win)** | **YES — partial, for the SUBDOMINANT half** | the subdominant guard is net precision-positive (+4 pp) but suppresses 17 genuine IV-modulations (−2.3 pp recall). **Surfaced as a trade-off (§0, §3.3); the §3.5 dominant-seventh refinement is the path to make it recall-clean.** |
| Uncertain about a mechanism | **No** | the over-detection is cited at `file:line` (§1) and confirmed by the dumps (§2) |

**Both §5 stop conditions fired** — this is a measure-first SPLIT result, surfaced for a user/Cowork direction
call rather than a guard unilaterally built.

---

## 6. Recommendation (for the user / Cowork)

1. **Build the SUBDOMINANT guard** (the measured net-positive half) with the anchor-confidence gate and the
   §3.5 dominant-seventh refinement (measured at build). It fixes mozart_k279 + bwv806_gigue, raises in-scope
   4d-i precision, and is convergent architecture work. This is a clean, ratifiable next build step.
2. **Treat the DOMINANT (i→v) over-commit as the unresolved calibration wall.** It is the *same* precision
   ceiling that 4c-i/4c-iii (dominant/subdominant residual), 4d-i (43 % of FPs), and J-key-ii-redux
   (non-separable partial-sig override) all hit — generalizing the key win to the dominant is fundamentally an
   evidence-precision / learned-emission problem (the architecture §5 "accuracy lives in calibration" thesis),
   not a hand-built monotone gate. corelli additionally carries the low-anchor-confidence / partial-signature
   dimension (anchor conf 0.423) that the J-key-ii-redux negative already flagged as unrecoverable.
3. **Do NOT flip the J-key-iii wiring ON globally yet.** The subdominant guard removes 2 of 3 snapshot
   regressions but not corelli's dominant tail; a global flip would still ship that regression. After the
   subdominant guard lands, re-adjudicate the snapshot gate; if corelli still regresses, prefer Step-3
   **option A (scope the wiring to the measured-positive repertoire)** or hold dormant until the dominant case
   is non-regressing.

---

*Drafted by CC, 2026-06-16, base `5fee657578`. Read-only: no source/instrument edit, no guard, no wiring
change, no commit. Measurement tool `tools/cc_b_guard_separability.py` (HELD). Full report:
`C:/tmp/cc_b_separability.txt`. Numbers `[probe]` on `tools/corpus/default_mod` (WiR-Bach Default) + the 3
snapshot dumps; keys/roots `[oracle]` (When-in-Rome rntxt / DCML harmonies via the pinned `dcml_parser`).*
