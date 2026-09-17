# CC — Diagnosis: why the L3 decoder reads Mozart K279/1 as F major (not C)

**READ-ONLY diagnosis. No fix applied. No production change. No golden refresh.**
Foundation HEAD `1fb168f56e`, the working tree, and the stash `bc4fa79c4a` left untouched
(the one transient diagnostic instrument added to `tools/batch_analyze.cpp` was reverted after
the dumps were captured — see §0). Data files are local/uncommitted under the session scratchpad.

---

## §0 — Method and the instrument

The L3 decoder **is** the production key path (verified, not assumed):
`region/regionanalyzer.cpp:555` calls `KeyModeSequenceDecoder::decode(...)`; `localKeyForRegion`
(`:574`) takes the duration-majority decoder key per coarse region. For K279 (clean C-major
signature, both staves eligible → `excludeStaves = {}`) the production decode context equals the
`--decode-keymode` diagnostic context (notated `keySigFifths = 0`; declared mode = **nullopt** —
the 0-fifths signature carries `KeyMode::UNKNOWN`, so `declaredModeOrdinal = -1` and **no**
declared-mode hint is applied on this score), so the existing diagnostic reproduces production.

Diagnostics used:
- `batch_analyze --decode-keymode` (existing) — the real L3 decode: per-slice chosen key,
  `keyEmission` (the chosen state's local-fit), ranked alternatives with their emission scores.
- `batch_analyze --dump-key-candidates` (existing) — the **per-region resolver** emission
  term-decomposition (a *different*, 24-beat-lookahead window — used as the wide-window contrast).
- `batch_analyze --dump-slice-emission TICK[,…]` (**added, transient, then reverted**) — rebuilds
  the decoder's **exact** per-slice emission window (replicating `keymodesequence.cpp::buildSliceContext`:
  `±windowBeats` span, `SpanWindowWeights{decayRate,lookaheadWeight,beatsPerDecayUnit}`, indexed
  `pitchContextOverSpan`, production `excludeStaves`) and prints the aggregated effective per-pc
  weight the scorer saw **plus** the full per-candidate `KeyCandidateScore` term breakdown. It
  returns before `analyzeScore` (production byte-identical) and was removed from the tree afterward.
  Its body is reproduced in Appendix A for reproducibility.

---

## §5 — VERDICT (stated first)

- **F wins on LOCAL FIT (emission), not change-cost — at the opening seed.** At slice 0 `[0,120)`
  Fmaj is the **global emission argmax** over all 252 candidates: **Fmaj 17.3805 > Amin 15.819 >
  Cmaj 14.577**. F is entered because it locally out-scores C by **+2.80**, before any transition
  cost is considered. (At *later* opening slices C often regains a small emission lead but the
  change-cost then *holds* F — see below — so the role is: **emission seeds F, change-cost locks it.**)

- **The responsible terms are `characteristicPitch` (char) and `trueLeadingTone` (lt) — NOT
  scale-membership, NOT change-cost.** Decomposing F − C at slice 0:

  | term | Fmaj | Cmaj | F − C |
  |---|---:|---:|---:|
  | scaleMembership | 6.779 | 6.890 | **−0.111** (favors C) |
  | triadEvidence | 7.001 | 7.086 | −0.085 (favors C) |
  | **characteristicPitch** | **+1.80** | **−0.60** | **+2.40 (favors F)** |
  | **trueLeadingTone** | **+1.20** | **0.00** | **+1.20 (favors F)** |
  | keySignatureProximity | −0.60 | 0.00 | −0.60 (favors C) |
  | modePrior | +1.20 | +1.20 | 0 |
  | **finalScore** | **17.3805** | **14.5770** | **+2.804** |

  F's entire +2.80 lead = **char (+2.40) + lt (+1.20)** minus C's small scale/triad/keysig edge
  (−0.80). **Both winning terms are keyed to `(tonicPc + 11)`** (Ionian's characteristic pitch =
  maj7; the true leading tone = semitone-below-tonic — the same pitch class). For the *correct*
  tonic C that pitch class is **B♮**; for the *spurious* tonic F it is **E**.

  In the decoder's ±4-beat opening window the weighted pitch content is
  `C 1.871, F 1.546, E 1.079, G 1.037, A 0.716, D 0.548, B 0.093`. **B♮ has weight 0.093 — below the
  hard-coded `> 0.1` presence threshold** in `scoreCharacteristicPitch`/`scoreTrueLeadingTone`
  (`keymodeanalyzer.cpp:339,374`). So C major is denied **both** anchors (its char flips to the
  −0.60 *penalty*, its lt → 0), while F major's char/lt pitch is **E = the third of the actual C
  tonic triad**, which is abundantly present → F harvests +1.80 + 1.20. The "subdominant-as-tonic"
  misreading is *rewarded* by char+lt exactly when the real tonic is being prolonged (lots of
  C/E/G, almost no B). A secondary push: the ±4-beat window pulls measure 2's IV (F-A-C) into the
  look-ahead, giving F a *spurious complete triad* (F-A-C) it would not have from m1 alone.

- **Hypothesis check — REFUTED.** CC's prior claim "the deferred Step-2 scaleMembership reweight
  is to blame; the scale-membership lever fixes it" does not survive measurement:
  1. The `scaleMembership` term contributes only **−0.111** of F's +2.80 lead at slice 0, and
     **exactly 0.000** in the noise-free bare-triad fixture (§4, scale tie 20 = 20). It is not the driver.
  2. Sweeping `scaleScoreInKeySigOnly` (the B♮ penalty lever) from −0.2 to **−3.0** (15×) moves
     Fmaj's emission by only **−0.26** (17.38 → 17.12) and **never flips F→C**. B♮'s window weight
     (~0.093) is too small for any scale-membership penalty to bite. The lever is the wrong knob.
  The real drivers are the **char + lt** terms (and they are *presence-gated*, not weight-scaled,
  so a reweight of the scale term cannot reach them).

- **Candidate proper-layer amendment (NAMED, NOT applied).** This is a **Layer-3 emission** fault
  with **two interacting causes**, both inside `keymodesequence`/`keymodeanalyzer`:
  1. **The char + lt terms are presence-gated on `(tonicPc+11)` regardless of musical function.**
     A note that is merely *present* grants the leading-tone/characteristic bonus even when it is
     functioning as a chord-tone third of a different key (E for F-major over a C chord). A
     spelling/function-aware leading-tone (the Layer-3 **tpc-aware** key work,
     `project_layer3_tpc_keymeasure`) — or a bonus that requires the LT to actually resolve, not
     just sound — is the structural target. This is the higher-leverage, deeper fix.
  2. **The fixed ±4-beat emission window is too short to see B♮ at a tonic-prolongation opening.**
     The window-width sweep (§2.4) shows the default `windowBeats = 4.0` sits in a non-monotonic
     **F-favoring sour spot**: win 1–2 → C, **win 4–6 → F**, win 8 → C, win 16–24 → C. The
     per-region resolver gets K279 *right* precisely because its 24-beat (dynamic-lookahead) window
     lets B♮ clear the 0.1 threshold (resolver: Cmaj 24.57 > Fmaj 23.63). A confidence-driven
     window widen / restored dynamic-lookahead in the decoder would fix the opening — **but** it
     trades against the very reason the decoder uses a short window + change-cost (long windows
     blur genuine modulation; the win-12 row shows F surviving on the sequence even when C is the
     emission-argmax). So widening is a *blunt* lever, not obviously safe.

  **The diagnosis points to more than one interacting cause, and it is a general (non-Bach)
  weakness**, not a Mozart quirk: any subdominant-prolongation or tonic-prolongation opening where
  the tonic's leading tone is briefly absent is exposed. The measured scale-membership lever is
  **not** the correct amendment. The correct amendment is in the **char/lt (+ window) sub-system of
  the Layer-3 emission**, with the spelling/function-aware leading tone the principled end state.

---

## §2 — The dumps (Mozart K279/1)

### §2.1 / §2.3 — Weighted content + per-candidate term decomposition, decoder's exact window

Slice 0 `[0,120)`, decoder window `[-1920, 2040)`, 24 context notes, totalWeight 6.89
(`--dump-slice-emission 0`):

```
pcWeights:  C 1.871  D 0.548  E 1.079  F 1.546  G 1.037  A 0.716  B 0.093
                                              (B♮ = 0.093  <  0.1 presence threshold)

label  final   scale   triad  char    lt   keysig prior  tonicW thirdW fifthW  triad?
Fmaj  17.3805  6.779   7.001  +1.8  +1.2   -0.6   1.2    F1.546 A0.716 C1.871  yes   <- argmax
Amin  15.8190  6.890   6.128  +1.8   0.0    0.0   1.0    A0.716 C1.871 E1.079  yes
Cmaj  14.5770  6.890   7.086  -0.6   0.0    0.0   1.2    C1.871 E1.079 G1.037  yes
FLyd  13.0009  6.890   7.010  -0.6  +1.2    0.0  -1.5
Dmin  12.3561  6.779   5.777  -0.6   0.0   -0.6   1.0
```

The numbers reconcile: F − C = (6.779−6.890) + (7.001−7.086) + (1.8−(−0.6)) + (1.2−0) +
(−0.6−0) + 0 = **+2.804** = 17.3805 − 14.5770. ✔

### §2.2 — Per-candidate local fit, F vs C, across the opening (`--decode-keymode`)

`keyEmission` = chosen state's emission; alternative `confidence` = that state's emission.

```
slice  tick     chosen  Fmaj-emission  Cmaj-emission  note
  0    0        Fmaj    17.3805        14.577         F is emission argmax (+2.80)
  1    120      Fmaj    17.4963        14.6462        F argmax
  2    240      Fmaj    17.5296        18.2537        C argmax (+0.72) but F CHOSEN  <-- change-cost
  3    360      Fmaj    17.6524        18.3208        C argmax but F chosen (uncertain=true)
 15    1920     Fmaj    27.7060        26.5879        F argmax again (+1.12) — triad-driven (see §2.3b)
 28    3840     Fmaj    27.8313        26.2686        F argmax (+1.56) — triad-driven
```

### §2.3b — Second, reinforcing mechanism at m2–m3 (the Dm/F bass)

Slice 15 `[1920,2400)` (m2 downbeat), window `[0,4320)`, totalWeight 13.6:
`pcWeights C 2.497, D 1.510, E 1.442, F 4.538, G 1.358, A 2.000, B 0.256`.
Here **B = 0.256 > 0.1**, so C *regains* char+lt (Cmaj char +1.8, lt +1.2). Yet F still wins —
this time on **triadEvidence** (Fmaj 10.81 vs Cmaj 8.79, **F +2.03**) because the actual music has
a heavy bass **F** (weight 4.538 = F's tonic; C 2.497 = F's fifth). So once F is the key, the
ii6 / "Dm/F" passages keep F's emission competitive — F is reinforced, not just seeded.

### §2.4 — Change-cost vs local fit (the decisive contrast)

- **Seed:** at slices 0–1 F is the *emission argmax* — F wins with **no** change cost involved.
- **Hold:** at slice 2 the emission argmax is **C** (18.2537 vs F 17.5296, C leads **+0.724**), yet
  F is chosen. `changeCost(F→C) = changeBaseCost 2.0 + changePerFifthStep 0.6 × cof(F,C)=1 = 2.60`.
  C's emission lead (0.724) ≪ 2.60 → the Viterbi keeps the cheap stay-on-F path; the slice is
  flagged `uncertain` (keyConfidence 0.42). So **change-cost holds F at the mid-opening slices**,
  but it is **not** why F was chosen at the start. Root cause = the emission seed (char+lt), §2.3.

### §2.x — Wide-window contrast (why the *resolver* gets it right)

`--dump-key-candidates 0` runs the per-region resolver over region `[0,1920)` with **24-beat
lookahead**. There **resolvedWinner = Cmaj 24.5693 > Fmaj 23.6321**:

```
Cmaj  finalScore 24.5693  scale 10.8635  triad 9.5059  char +1.8  lt +1.2  keysig  0.0
Fmaj  finalScore 23.6321  scale 10.4875  triad 9.5446  char +1.8  lt +1.2  keysig -0.6
```

Over 24 beats B♮ accumulates weight ≈ 0.31 (> 0.1), so **C keeps its char + lt** (both 1.8 / 1.2);
the decision then falls to **scaleMembership (C +0.376, the B♮ in-both vs keysig-only differential)
+ keySigProximity (C +0.6)** → C wins by 0.94. The whole error is the short decoder window
crossing *below* the B♮ presence threshold that the resolver's wide window stays *above*.

### §2.4b — Window-width sweep (slice 0, `--seq-window-beats`)

```
win=1  Cmaj    win=2  Cmaj    win=4 Fmaj(default)  win=6 Fmaj
win=8  Cmaj    win=12 Fmaj(sequence; Cmaj is emission-argmax 23.12>22.76)
win=16 Cmaj    win=24 Cmaj
```
Non-monotonic; the committed `windowBeats=4.0` is an F-favoring sour spot.

### §2.4c — B♮-penalty (scale-membership lever) sweep (slice 0, `--key-in-keysig-only`)

```
-0.2  Fmaj 17.3805     -1.0  Fmaj 17.3064     -2.0  Fmaj 17.2138
-0.5  Fmaj 17.3527     -1.5  Fmaj 17.2601     -3.0  Fmaj 17.1211
```
Fmaj never loses; its emission barely moves (Δ = 0.26 over a 15× lever swing). Implied
B♮ window-weight ≈ 0.26 / 2.8 ≈ 0.093. **The scale lever cannot fix this.**

---

## §3 — The decisive contrast with the passing unit test

`Composing_KeyModeAnalyzerTests.PrefersCMajorForCMajorPitchSet` feeds `C E G B` at **flat weight
1.0 each**, keySig 0 → C major (passes). Why it passes and Mozart fails, side by side:

| | unit test (passes → C) | Mozart slice 0 (fails → F) |
|---|---|---|
| B♮ weight | **1.0** (≫ 0.1) | **0.093** (< 0.1) |
| C's char (maj7=B) | **+1.8** (present) | **−0.6** (penalty, B sub-threshold) |
| C's lt (=B) | **+1.2** (present) | **0.0** |
| F's tonic/third (F,A) | **absent** → no F triad, missing-tonic | **present** (windowed IV) → F complete triad |
| winner | C (huge margin) | F (+2.80) |

So the flip is option **(a) the weighting** of the input — specifically, **the weighting starves
C's char/lt anchor (B♮) below the presence threshold**, while the same window *adds* F's tonic/third
(from the neighbouring IV). It is **not** option (b) "a missing/too-small scale penalty" (the scale
term differs by only −0.11 / 0.00), and **not** option (c) change-cost (F is the emission argmax at
the seed). The scorer *terms* are sound on a fair sample (the resolver's 24-beat window and the
unit test both pick C); the **short emission window** is what starves the deciding term.

---

## §4 — The harmony-pin fixture (controlled, noise-free C triad)

I could not bind the report's "#4/#5" label to a specific named harness — that is Cowork's
architectural context, not mine. The repo's one synthetic bare-C-major-triad fixture,
`src/notation/tests/notationtuning_data/harmony_pinning_i_iv_v_i.mscx` (whole-note **I–IV–V–I** in
C, chord-track staff excluded as in production), reproduces the **identical** error and isolates the
scorer from any figuration:

Slice 0 = measure 1 (the bare **C** triad), window `[-1920,3840)` covers m1 `C-E-G` + m2 `F-A-C`;
**B♮ is wholly absent** (it first appears in m3's V = G-B-D, at tick 3840 = the half-open window
edge, excluded):

```
pcWeights:  C 8   E 3   F 4   G 3   A 2     (no B at all)

label  final  scale  triad  char    lt   keysig
Fmaj   35.3   20.0   11.7   +1.8  +1.2   -0.6     <- winner (V of F)
Amin   33.7   20.0   10.9   +1.8   0.0    0.0
Cmaj   32.0   20.0   11.4   -0.6   0.0    0.0     <- the correct I, third place
```
F − C = scale **0.0** (perfect tie — no B differential) + triad +0.3 + **char +2.4 + lt +1.2** +
keysig −0.6 = **+3.3** = 35.3 − 32.0. The cleanest possible proof: with B totally absent the scale
term is *identical* for F and C, and F's whole margin is **char + lt**.

Threshold flip confirmed at the very next slice — measure 2 `[1920,3840)`, window `[0,5760)` now
reaches m3's G-B-D so **B = 2.0 (> 0.1)**: Cmaj regains char +1.8 / lt +1.2 and **wins, 47.46 >
Fmaj 44.92**. B-present → C; B-absent → F. Same mechanism as Mozart, no figuration noise.

---

## Appendix A — the transient instrument (added, used, reverted)

Added to `tools/batch_analyze.cpp` (returns before `analyzeScore`; production byte-identical):
a `--dump-slice-emission TICK[,…]` flag + `runSliceEmissionDump(...)` that, for each slice
containing a requested tick, rebuilds the decoder's exact window via
`engravingbridge::pitchContextOverSpan(model, s-win, e+win, s, e, excludeStaves, keyPrefs,
SpanWindowWeights{seqPrefs.decayRate,seqPrefs.lookaheadWeight,seqPrefs.beatsPerDecayUnit}, ctx)`
with `win = lround(seqPrefs.windowBeats * Constants::DIVISION)`, aggregates effective per-pc weight
`min(dur·beat, noteWeightCap)·(isBass?bassMultiplier:1)`, and runs `analyzeKeyMode(ctx, keySig,
keyPrefs, declaredMode, &dump)` to print the per-candidate term breakdown. **Reverted** after the
dumps in §2/§4 were captured; the working tree is back to `1fb168f56e`. Build was clean (exit 0).

Raw dumps (local/uncommitted): `k279_decode.json`, `k279_keycand.json`, `k279_emit_s0.json`,
`k279_emit_m23.json`, `hp_emit.json` under the session scratchpad.

---

## Constraints honored
- Read-only diagnosis; **no fix, no golden refresh, no production-code change.** The only edit
  (the diagnostic flag) was reverted; production analysis paths are byte-identical throughout.
- HEAD `1fb168f56e`, working tree, and stash `bc4fa79c4a` untouched. `upstream` never; `origin` held.
- Stopped at the verdict — **no scorer-term/reweight/window/golden change applied** (that is the
  separate, gated step decided after this verdict).
