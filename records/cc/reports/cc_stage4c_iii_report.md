# CC Stage 4c-iii — refined cadence detection (structural / raised-LT / Picardy): BUILT + RE-MEASURED

**Date:** 2026-06-15 · **Status:** HELD — no commit. Implements the three ratified 4c-iii refinements on
top of the 4c-i detector (`docs/stage4c_cadence_key_design.md` §4; the 4c-i "far below ceiling" stop fired).
The detector remains **diagnostic-only**; the production key resolver/winner is **untouched** (byte-identical,
same as 4c-i). Base = HEAD `cfc7eb5e39` (local 4a) + `ef30cc70f3` (4b-i). Every number tagged `[probe]`
(measured this run), `[code]` (read at source), `[oracle]` (DCML/WiR rntxt).

**Verdict (one line):** All three refinements were built **key-agnostically** (signature-fifths + fermata +
pitch content, NEVER the resolved mode) and re-measured. Realized detection rose from 4c-i's **55.7% → 75.2%**
`[probe]` (1092/1452 on the mode-absent relative-pair floor) and the binding clean-stem contradiction rate
fell from **34% → 25.3%** `[probe]` (63/249). The 4c-i relative-major swamping is largely fixed (308 → 123
wrong floor regions) and Picardy mis-flips nearly eliminated (91 → 13). **The contradiction is now dominated
by a DIFFERENT, un-targeted failure — dominant/subdominant tonicizations read as the global tonic ("other":
47/63 clean contradictions, 224/360 wrong floor regions).** 25.3% ungated is **still above a safe-wire bar**,
but a confidence gate at conf ≥ 0.6 cuts clean-stem contradiction to **9.8%** (at 15% floor coverage) `[probe]`
— so **wiring is now feasible *gated*, not ungated**. **Branch: do NOT wire ungated; the remaining lever is
the dominant/subdominant guard (design branch-note #4), then 4c-ii with a confidence gate.** Reported, not
forced.

---

## 1. The three refinements at source — key-agnostic inputs RE-CONFIRMED `[code]`

All edits are in the composing autonomous zone + `tools/`; **no `src/notation` / `src/engraving` code edit**
(reading the Score in `batch_analyze` is not an edit — confirmed below).

**(1) Structural-vs-interior discrimination — fermata-gated.**
`CadenceRegionInput` gains `bool endsPhrase` (`cadencekeyanchor.h`). `tools/batch_analyze`
(`collectPhraseBoundaryTicks`) walks the engraving Score's chord-rest segments and collects the ticks of
every segment carrying a fermata (`e->isFermata()` on `segment->annotations()`); a region is marked
`endsPhrase` when a fermata sounds within `[startTick, endTick)` **or** it is the final region of the piece.
`detectAuthenticCadences` copies `b.endsPhrase` onto each cadence. **Notation only — no key/function read.**

**(2) Raised-leading-tone salience — KEY-AGNOSTIC via the signature.**
`detectAuthenticCadences` now takes `int keySignatureFifths` and computes `diatonicMaskFromFifths()` — the
7-pc diatonic collection of the **notated signature** (circle-of-fifths positions `[f-1, f+5]`). A cadence's
`chromaticLeadingTone` is set when the dominant's leading tone `(root(a)+4) mod 12` lies **outside** that
mask (e.g. E→Am needs G♯, foreign to a 0-sharp signature; G→C uses the in-collection B). The signature is
read in `batch_analyze` from `score->staff(refStaff)->keySigEvent(tick 0).concertKey()` — the **NOTATED
signature, not a resolved key** (`KeyModeAnalysisResult::keySignatureFifths` is *resolved* — line 709 of
`keymodeanalyzer.cpp` — and is deliberately **not** used here). **Signature fifths + pitch content ONLY —
never the resolved mode.** This is the circularity guard the design demands.

**(3) Picardy handling.**
`aggregateGlobalAnchor` runs a post-vote correction: if the winning bucket is **major** but the **same tonic
pc** also carries minor-mode cadential weight (the body cadenced to i), the major reading is a Picardy third
and the global mode is re-read as **minor**. A genuine major key has no i-cadences to its tonic, so a true
major is never flipped (unit-pinned).

**Aggregation (replaces the 4c-i naive count).** Each cadence votes with
`w = base + (endsPhrase ? wStruct) + (chromaticLT ? wChrom) + wFinality·k/(n-1)`, weights
**`base=1, struct=2, chrom=1, final=1`** `[code]` (`cadencekeyanchor.cpp`). Chosen at the high-realized /
low-contradiction knee of a weight sweep (§3.3); provisional `[empirical — Stage-5 fits]`, **not** corpus-fit
to the 326-chorale gate (the same point is robust across its neighborhood).

Unit tests: `cadencekeyanchor_tests.cpp` **11 → 17** (+6: signature-relative chromatic LT at 0-sharp and
1-sharp, structural-raised-LT-outweighs-interior, Picardy-does-not-flip, genuine-major-not-flipped,
endsPhrase propagation). **composing_tests 516 → 522, all green.**

---

## 2. Byte-identity gate — production scoring UNTOUCHED `[probe]`

The detector is reached **only** by `batch_analyze --dump-cadence-anchor` (default OFF). The resolver/winner
never calls it; no scoring file changed.

- **Default mode-absent scoring byte-identical** `[probe]`: stripping `cadenceAnchor` from every
  `default_4ciii_abs/*.ours.json` and diffing vs the 4c-i reference `default_4ci_abs` → **0 / 353**.
- **Default mode-present scoring byte-identical** `[probe]`: same strip-and-diff vs `default_4ci` → **0 / 353**
  (the BIR-relevant path).
- **BIR gate 57 / 23 / 57** `[probe]`: Default = **57** confirmed directly through `characterise_bir_false.py
  --corpus-dir tools/corpus/default_4ciii` (353 scores, 326 WiR, 57 genuine BIR=false). Baroque = 57 / Jazz =
  23 unchanged **by construction** — zero scoring code was touched (the only C++ edits are the detector, the
  `batch_analyze` diagnostic, and tests; none is on the resolver/winner path), and the OFF-path output is the
  same character stream as before.
- **pipeline_snapshot_tests 11 / 11, zero golden diff** (no `--update-goldens`). **notation_tests 57**,
  **composing_tests 522** — all green.

No off-limits production edit. Touched outside composing: `tools/batch_analyze.cpp` (fermata read + signature
+ emission), `tools/run_bach_preset.py` (pre-existing passthrough), and the measurement/prototype scripts.

---

## 3. THE DELIVERABLE — re-measured realized detection vs 4c-i `[probe][oracle]`

Identical protocol to 4c-i (`tools/cc_cadence_anchor_measure.py`; floor = mode-absent relative-pair S2,
classification reused verbatim from `cc_floor_classify`). Floor reproduction exact: **1452 regions / 181
stems**, matching 4c-i.

| metric (mode-absent relative-pair floor) | 4c-i | **4c-iii** | Δ |
|---|---:|---:|---:|
| floor regions | 1452 | 1452 | — |
| detector fired (recall) | 100% | **100%** | — |
| **REALIZED correct (precision)** | **55.7%** (809) | **75.2%** (1092) | **+19.5 pts** |
| stem-weighted correct | 108/181 | **137/181** | +29 stems |
| fired-but-wrong floor regions | 643 | **360** | −283 |
| perfect-detection ceiling | ≈86.7% | ≈86.7% | — |

**Realized 75.2% — 87% of the perfect-detection ceiling** (vs 64% at 4c-i).

### 3.1 — Clean-stem contradiction (the binding constraint for 4c-ii) `[probe]`
On the **249 mode-present clean stems** (zero S2 — the key the 1.0 hint already gets right):

| | 4c-i | **4c-iii** |
|---|---:|---:|
| anchor AGREES | 164 (66%) | **186 (75%)** |
| anchor **CONTRADICTS** | **85 (34%)** | **63 (25.3%)** |

Contradiction fell **8.7 points**. It is a clear, substantial drop, but **25.3% is not yet a safe-wire bar**
(wiring an ungated anchor would override the correct hint on ~1/4 of clean stems — the 4c-ii hard-stop).

### 3.2 — Per-refinement contribution (ablation, region-weighted realized) `[probe]`
| configuration (base+finality always on) | realized | clean-contra |
|---|---:|---:|
| base + finality only | 60.3% | 28.5% |
| + structural only | 57.0% | 33.3% |
| + chromatic-LT only | **67.7%** | 27.7% |
| + Picardy only | 62.5% | 26.5% |
| chromatic + Picardy (no structural) | 71.6% | 24.5% |
| **structural + chromatic + Picardy (FINAL)** | **75.2%** | **25.3%** |

**The chromatic raised-LT is the PRIMARY lever** (+7.4 alone) — it is the clean relative-major discriminator,
exactly as theorized. **Picardy is the second-largest** (and it *lowers* contradiction). **Structural is a
modest net positive in combination (+3.6 over chromatic+Picardy) but NEGATIVE in isolation (60.3 → 57.0)** —
an honest refinement of the design's "structural is the primary fix" hypothesis: in minor-key chorales
*phrase-final* cadences frequently land on the **relative major** (interior phrases cadence to III with a
fermata), so "phrase-final ≠ tonic" — the raised-LT is the cleaner signal. bwv365 is the exemplar (§4).

### 3.3 — Weight choice (not corpus-fit) `[probe]`
A 2-D sweep (`cc_cadence_aggregate_prototype.py`, which re-aggregates the emitted per-cadence flags and
reproduces the C++ anchor **exactly**) over struct ∈ [1.5,8], chrom ∈ [0,6], final ∈ [0.5,3] showed a broad
Pareto plateau: realized ~74–75.5% with contradiction ~25% across many neighboring points (e.g. (2.5,1.5,2.0)
gives 75.5%/24.9%). **`(2,1,1)`** was chosen as the round, principled knee — structural primary (largest
single bonus), chromatic = base, finality a mild tilt — sitting in the plateau rather than at a sharp optimum
(overfitting guard honored; the per-target outcomes are weight-invariant across the plateau).

---

## 4. Per-target `[oracle]`
| stem | DCML global `[oracle WiR]` | 4c-i anchor | **4c-iii anchor** | conf | reading |
|---|---|---|---|---:|---|
| **bwv33.6** | a minor | C major (MISS) | **a minor** | 0.43 | **RECOVERED** — chromatic E→Am now outvotes the diatonic V→III. ✓ |
| **bwv83.5** | d minor | d minor ✓ | **d minor** | 0.51 | stays correct, floor=0 (not spuriously claimed). ✓ |
| **bwv365** | a minor | C major (MISS) | **C major (MISS)** | 0.84 | NOT recovered. **Segmentation artifact** `[probe]`: our regions *end on a C-major chord* and **both** detected phrase-final (fermata) cadences resolve to C; the only A-minor cadence (chromatic E/G♯→Am) is **interior**. WiR confirms the piece is a minor (first & last region global=`a`), so the analyzer's final C is an upstream chord/segmentation error the cadence detector faithfully inherits. Structural & chromatic signals here **conflict** — beyond 4c-iii's reach (Stage-6 / upstream segmentation). |
| **bwv64.2** | **C major** | G major (MISS) | **G major (MISS)** | 0.58 | NOT recovered — anchors to the **dominant** G. The "other"/dominant-tonicization residual (§5). floor=1. GT settled C major (4c-i). |

bwv33.6 recovered; bwv83.5 held. bwv365 and bwv64.2 are the two residual failure classes (segmentation /
dominant), neither targeted by the three 4c-iii refinements.

---

## 5. Residual — what still misses `[probe][oracle]`

Wrong-anchor relationship breakdown at the final weights:

| relationship | clean contra (of 63) | wrong floor stems (of 44) | wrong floor regions (of 360) |
|---|---:|---:|---:|
| **other** (dominant / subdominant) | **47** | **25** | **224** |
| relative_pair (relative major/minor) | 13 | 17 | 123 |
| parallel (Picardy) | 3 | 2 | 13 |

**The residual is now dominated by "other" — dominant/subdominant tonicizations read as the global tonic**
(bwv64.2 G-for-C, bwv65.2/65.7 G-for-Am, bwv289 B-for-Em). This is the **4th failure mode** the design's
branch-note #4 anticipated ("dominant/subdominant guard") and is **NOT** one of the three refinements built
here. The relative-major mode (the 4c-i headline, 308 regions) is cut to 123, and Picardy to 13 — the two
modes 4c-iii *did* target are largely resolved. The remainder is **interior-tonicization noise of a new
kind** (dominant cadences), not missing cadence modalities (coverage gap is still **0**).

### 5.1 — Confidence-gating: wiring is feasible GATED, not ungated `[probe]`
Contradictions concentrate at **low** confidence; correct anchors at high. Sweeping the emitted anchor
confidence:

| conf ≥ | clean contra% | clean anchors firing | realized floor retained |
|---:|---:|---:|---:|
| 0.0 (ungated) | 25.3% | 249 | 75.2% |
| 0.5 | 16.8% | 113 | 28.3% |
| **0.6** | **9.8%** | 61 | 15.0% |
| 0.7 | 4.0% | 25 | 6.1% |

A gate at **conf ≥ 0.6 reaches ~10% contradiction** — plausibly safe to wire — but covers only ~15% of the
floor. So 4c-ii is **feasible with a confidence gate** (precision-first, limited coverage), whereas an ungated
anchor remains too risky. Pushing both numbers up is the dominant/subdominant guard's job.

---

## 6. Branch recommendation

Per the instruction's branch rule (the bar is **primarily the contradiction rate**):

- **Ungated wiring: NO.** 25.3% clean-stem contradiction is below 34% but still overrides the correct hint on
  ~1/4 of clean stems — above a safe-wire bar.
- **The next lever is detection, not wiring:** add the **dominant/subdominant guard** (design branch-note #4)
  — suppress anchoring to a key whose "tonic" is itself the dominant/subdominant of a stronger/later cadence.
  This directly targets the new dominant residual (47/63 clean contradictions, 224/360 wrong floor regions)
  and bwv64.2. The relative-major and Picardy modes are already handled.
- **Then 4c-ii, confidence-gated.** The §5.1 curve shows a conf ≥ 0.6 gate already reaches ~10% contradiction;
  with the dominant guard lifting precision, a gated anchor covering a worthwhile fraction of the floor becomes
  wireable under the §3 structural-decoupling guarantee.

The §3 structural decoupling still holds (when the anchor is correct it agrees with the hint); the work
remains **detection reliability**, now narrowed to one residual mode. **B (learned key emission) is not
implicated** — the hand-built signal reached 75.2% / 87% of ceiling with three principled, key-agnostic moves.

---

## 7. Stop-conditions — disposition
- ✅ **`src/notation` / `src/engraving` code edit** — none. Fermatas/signature are *read* in `batch_analyze`
  (writable tools zone); no bridge/engraving code change was needed for the measurement. §1.
- ✅ **Key-agnosticism broken** — did NOT occur. All three inputs are signature-fifths + fermata + pitch
  content; the resolved `KeyModeAnalysisResult::keySignatureFifths`/mode is explicitly **not** used. §1.
- ✅ **Production behavior change (gate/snapshot/suite movement)** — none. 0/353 scoring diff (both modes),
  BIR Default 57 confirmed (23/57 by construction), snapshots 11/11, suites 522/57. §2.
- ✅ **Realized / contradiction still failing the bar** — reported as the detection-reliability finding
  (dominant/subdominant guard next, then gated 4c-ii); did **not** wire a sub-bar detector. §5–§6.

## 8. Working-tree artifacts (HELD — no commit)
- `src/composing/analysis/section/cadencekeyanchor.{h,cpp}` — `endsPhrase` input, signature param +
  `diatonicMaskFromFifths`/`chromaticLeadingTone`, salience-weighted aggregation + Picardy correction.
- `src/composing/tests/cadencekeyanchor_tests.cpp` — 11 → 17 tests.
- `tools/batch_analyze.cpp` — `collectPhraseBoundaryTicks`, notated-signature read, per-cadence flag emission
  (`--dump-cadence-anchor`, default OFF).
- `tools/cc_cadence_aggregate_prototype.py` — read-only weight-sweep scaffold (reproduces the C++ anchor).
- `tools/corpus/default_4ciii/`, `tools/corpus/default_4ciii_abs/` — measurement corpora (scoring
  byte-identical to `default_4ci{,_abs}`; keep or drop at Cowork's discretion).
- This report. No `docs/scoring_model.md` sync (no chord scoring term changed). HEAD unchanged.
