# CC Dossier — cadence-instrument precision: can a key-agnostic chromatic-LT gate unblock 4d?

> **READ-ONLY investigation. No build, no commit, no production/metric change.** Base HEAD `2245aedf82`.
> Derives + SIMULATES only (per the instruction). Reuses the committed cadence diagnostic
> (`--dump-cadence-anchor`), the 4d-i modulation diagnostic (`--dump-modulation`), and
> `compare_rn`/`compare_analyses`/`dcml_parser` verbatim. Every claim tagged `[code]` (read source),
> `[probe]` (ran a script), `[oracle]` (When-in-Rome DCML GT).
> Surface: WiR-Bach `tools/corpus/default_modcad` (Default preset, both diagnostic blocks), 326/353 covered,
> 10 109 aligned regions, 2667 detected cadences.

---

## §0 — TL;DR (the answer is NO)

| | Finding | Basis |
|---|---|---|
| **The chromatic-LT signal is NOT a discriminator** | Among the 4d-i modulation spans, **~45 % of TRUE modulations and ~50 % of false ones carry a diatonic (non-chromatic) leading tone** — the chromatic-LT split is essentially orthogonal to true-vs-false modulation. It cannot separate the two classes. | §3 [probe][oracle] |
| **No faithful chromatic-LT gate lifts precision to wireable** | Simulated (validated re-impl, 0/326 mismatch): blanket filter **47 %→29 %** (WORSE — it strips the home-key cadences), anchor-aware **47 %→41 %** (WORSE), span-level **47 %→50 %** (+3 pp, but recall **33 %→22 %**). None reaches a wireable bar. | §4 [probe][oracle] |
| **Chromatic adds NOTHING over the existing ≥2-cadence lever** | The strongest key-agnostic lever is the 4d-i confirmation-count gate (≥2 cadences): **58.4 %** precision @ 18.1 % recall — and it is **NOT chromatic**. Stacking chromatic on top (E) gives **57.6 %** (no precision gain) while dropping recall to 12.4 %. | §4 [probe][oracle] |
| **Relative-pair: the anchor ALREADY uses the suggested signals** | `aggregateGlobalAnchor` already buckets by resolution quality (`minorMode`) and weights the raised-LT (`chromaticLeadingTone`) + Picardy — exactly the class-2 signals the instruction proposed — yet the anchor is right on only **72.4 %**. The signals are already spent; this is the structural relative-pair floor (the 4b-ii ceiling), not a missing signal. | §5 [code][probe] |
| **The precision ceiling is too low — report it, do not build** | The achievable key-agnostic precision ceiling is **~50–58 %** (and only at ~18–22 % recall) — below the 4d-ii precision-lean bar and well under the realistic-ceiling the lever needs. The irreducible residual (subdominant-direction modulations with diatonic LTs, the relative-pair structural floor, sustained-tonicization analyst-convention ambiguity) is **not reachable key-agnostically** → it needs a different layer / richer model. | §6 |

**One-line answer:** the cadence instrument's precision **cannot** be fixed key-agnostically by a chromatic-LT
gate — the signal is orthogonal to correctness, drops as many true modulations as false ones, and (applied as
a cadence filter) destroys the home anchor; the best key-agnostic lever (≥2 confirming cadences) caps at ~58 %
precision at the cost of recall and owes nothing to chromaticity. **The key-agnostic cadence approach is
precision-limited; the residual needs a different layer. Do NOT build the chromatic discriminator; 4d-ii stays
HELD.**

---

## §1 — Method + faithfulness validation `[probe][code]`

To run the **decisive test** (the downstream modulation-precision lift under a filtered cadence input) without
building, I re-implemented `detectLocalModulations` **and** `aggregateGlobalAnchor` in Python
(`tools/cc_cadence_precision_investigation.py`), fed them the **dumped** cadence list (which carries each
cadence's signature-relative `chromaticLeadingTone` flag `[code]` — derived from `keySignatureFifths` + pitch
content, never a resolved key), and **validated** the re-impl byte-matches the committed C++ output:

```
span-set mismatches:  0/326   (re-impl spans == the C++ "modulation" block, per piece)
anchor mismatches:    0/326   (re-impl anchor == the C++ dumped anchor)
```
Baseline (full cadences) reproduces the 4d-i numbers exactly — **precision 47.0 %, recall 33.4 %**, same FP
relationship split — so every filtered variant below is a trustworthy simulation of the same C++ detector fed
an improved cadence list.

**Declared limitation (no guessing):** DCML annotates *local keys*, not *cadence events*, so there is **no
direct oracle for "is this detected cadence real."** Per-cadence precision is therefore measured by its
**downstream effect** (the modulation-precision lift) — the decision-relevant quantity the instruction calls
"the real test." Numbers are `[probe]` on the Default/WiR-Bach surface (326 Bach pieces); generalization to
non-Bach is **not** measured here and must not be assumed.

---

## §2 — The chromatic-LT distribution `[probe]`

Of the 2667 detected cadences, **1256 (47.1 %) carry a chromatic leading tone, 1411 (52.9 %) a diatonic one.**
The proposed discriminator hinges on chromatic-LT ⇒ real-modulation, diatonic-LT ⇒ within-key tonicization.
§3 tests that hypothesis directly.

---

## §3 — The chromatic-LT gate is NOT a discriminator (the core derivation) `[probe][oracle]`

Cross-tabulating every 4d-i modulation span by its DCML verdict (TP / FP) against whether it has ≥1
chromatic-LT confirming cadence:

```
                chromatic   diatonic-only   → a chromatic gate would DROP the diatonic-only
TP (real mod):     119           98          (45% of TRUE modulations dropped)
FP over-mod:        62           65          (51% of false modulations dropped)
FP wrong-key:       38           32          (46% dropped)
```
**The chromatic-LT signal is orthogonal to correctness.** It drops ~45 % of *true* modulations and ~50 % of
*false* ones — nearly identical rates — so gating on it removes as much signal as noise. The instruction
anticipated the asymmetry and the data confirms it is worse than a clean separator:

- **Analytic root cause `[code]`:** `chromaticLeadingTone = (tonic+11) ∉ signatureCollection`. In a major
  home key the diatonic-LT cadences are exactly those to **I** (home) and **IV** (subdominant) (and chromatic
  tonics); the chromatic-LT cadences are those to **ii/iii/V/vi**. So:
  - True **dominant-direction** modulations (to V) have a chromatic LT → kept. *(good for recall)*
  - True **subdominant-direction** modulations (to IV) have a **diatonic** LT → indistinguishable from an
    I→IV tonicization → the gate **cannot keep them**. *(recall loss)*
  - The **home (I) cadences** themselves have a diatonic LT → a blanket gate removes the anchor's own
    evidence. *(anchor destruction — §4 Variant A)*
- So the gate's "coverage" of the dom/subdom FP class (the instruction's 43.3 % target) is partial and
  comes bundled with dropping the matching TRUE modulations.

---

## §4 — The downstream unblock test — the real test `[probe][oracle]`

Re-running the validated detector with the cadence list filtered three faithful ways (plus the 4d-i
confirmation-count lever and the joint for the ceiling):

```
                                                       precision   recall    Δprec/Δrec vs baseline
BASELINE (all cadences)                                  47.0%      33.4%
A  blanket chromatic filter (drop ALL diatonic-LT)       29.2%      33.1%     -17.8 / -0.3
B  anchor-aware (keep home cadences, gate non-home)      41.3%      31.2%      -5.7 / -2.2
C  span-level (drop non-home spans, no chromatic conf.)  50.0%      22.2%      +3.0 / -11.1
D  >=2 confirming cadences  [key-agnostic, NOT chromatic]58.4%      18.1%     +11.4 / -15.2
E  chromatic AND >=2 cadences  [joint ceiling]           57.6%      12.4%     +10.6 / -21.0
```
- **A (the literal proposal — filter the cadence list on chromatic-LT): precision DROPS to 29.2 %.** Removing
  the diatonic-LT home (I) cadences strips the home anchor, so home regions get reassigned to the nearest
  surviving (chromatic-LT, non-home) cadence — non-home commits jump 2867→4574 and over-modulation explodes.
  The gate, applied as designed, makes the detector worse.
- **B (keep home cadences, gate only non-home): still WORSE (41.3 %).** Even preserving the home cadences,
  removing diatonic-LT non-home cadences disrupts the nearest-cadence partition and nets more over-modulation.
- **C (span-level, the most favorable form): +3.0 pp precision (50.0 %) for −11.1 pp recall.** Marginal, and
  50 % still over-modulates half the commits.
- **D (≥2 confirming cadences): the best key-agnostic result, 58.4 % @ 18.1 % — and it is NOT chromatic.**
  This is the 4d-i confirmation-count finding (≈ the 4d-i sweep's ~61 % at cad≥2; the ~3 pp difference is the
  home-span accounting). Confirmation *count* beats chromaticity outright.
- **E (chromatic AND ≥2 cadences): 57.6 %.** Adding chromatic to D gives **no precision gain** (57.6 vs 58.4)
  and only costs recall (12.4 vs 18.1). **Chromaticity contributes nothing the confirmation count doesn't
  already capture better.**

**Verdict:** no key-agnostic chromatic-LT formulation lifts modulation precision to a wireable level; the
chromatic signal is redundant-to-harmful next to the existing ≥2-cadence lever, which itself only reaches
~58 % at a heavy recall cost.

---

## §5 — The relative-pair class: the suggested signals are already spent `[code][probe]`

The instruction asks whether a key-agnostic signal — *"the resolution chord's own quality major-vs-minor, the
raised-LT presence"* — fixes the cadence anchor's relative-major/minor mis-pick (right only 72.4 %).
**Both proposed signals are ALREADY in `aggregateGlobalAnchor` `[code]`:**

- the vote bucket key is `{ c.tonicPc, c.minorMode }` ([cadencekeyanchor.cpp:180](src/composing/analysis/section/cadencekeyanchor.cpp#L180))
  — the **resolution quality** already separates the relative major from the relative minor;
- the weight adds `kWeightChromatic` when `c.chromaticLeadingTone` ([:178](src/composing/analysis/section/cadencekeyanchor.cpp#L178))
  — the **raised-LT presence** already boosts the genuine minor V→i;
- a Picardy correction ([:197–208](src/composing/analysis/section/cadencekeyanchor.cpp#L197)) already folds a
  major-tonic-with-minor-body back to minor.

The 72.4 % anchor accuracy is measured **with** these signals active. They are insufficient: the relative-pair
decision is the **same structural ceiling 4b-ii hit** (reweighting the local note evidence cannot carry it —
the missing signal is global/long-range key identity, not another local cadence feature). The relative
over-modulation FPs (287 regions) are sustained AND cadence-confirmed yet DCML reads them as home — the
brief-vs-sustained signal the whole detector rests on cannot separate them, and the span-level chromatic gate
catches only ~40 % of them (Variant C: relative over-mod 287→171) while also dropping the relative *true*
modulations. **No additional key-agnostic local signal is evident; this is the structural relative-pair floor.**

---

## §6 — Achievable ceiling + irreducible residual `[probe]`

- **Achievable key-agnostic precision ceiling ≈ 50–58 %**, and only at **~18–22 % recall** (Variants C/D).
  That is below the 4d-ii precision-lean bar (which forbids un-adjudicated over-modulation) and far from a
  confidently wireable level.
- **Irreducible residual a key-agnostic cadence fix CANNOT reach:**
  1. **Subdominant-direction modulations** — diatonic LT by construction, indistinguishable from I→IV.
  2. **The relative-pair structural floor** — the anchor's suggested signals are already spent at 72.4 % (§5);
     needs long-range/global key identity.
  3. **Sustained, cadence-confirmed tonicizations DCML annotates as home** — genuine analyst-convention /
     broader-context ambiguity that no local cadence feature resolves.
  These are exactly the cases the metric-check and the scoping flagged as the next-layer / learned-model
  evidence.

---

## §7 — Recommendation

**Do NOT build the chromatic-LT cadence discriminator. The key-agnostic cadence approach is precision-limited;
4d-ii stays HELD.**

- The instruction's chromatic-LT hypothesis is **falsified by simulation** (§3–§4): the signal is orthogonal
  to correctness, no faithful formulation reaches a wireable precision, and it adds nothing over the existing
  confirmation-count lever. Per the stop-condition ("simulated lift marginal ⇒ report honestly; do NOT
  recommend a build that won't reach a wireable precision"), this is reported as the finding, not a build.
- The relative-pair class is the **same structural floor** (§5): the suggested key-agnostic signals are
  already in the anchor and cap at 72.4 %.
- **What this means for sequencing:** the modulation lever's precision is NOT unblockable by a key-agnostic
  cadence refinement. The residual (§6) needs a **different layer / richer model** — candidates the data
  points to, NOT recommended-to-build here: longer-range / global key-identity context (an HMM/decode over the
  key path, `key_path_design.md`), a learned key/modulation model (the B fork), or a spelling-aware reading.
  The one key-agnostic lever that *does* move precision (≥2 confirming cadences, ~58 % @ 18 % recall) is the
  4d-i finding, not a cadence-instrument change, and is itself sub-wireable.
- **Honest scope:** this is the Bach/Default WiR surface (§1). Whether the same ceiling holds on harder
  non-Bach repertoire is **unmeasured** and should not be assumed.

**Bottom line: the cadence instrument's precision is the genuine bottleneck, but it is NOT fixable
key-agnostically — so the next lever is a different layer (long-range key context / learned model), not a
cadence-gate build. Surface this so the back-half sequencing can choose that layer rather than spend a round
on a discriminator the data shows will not reach a wireable precision.**

---

## §8 — Stop-condition disclosures
- **Read-only** — no source built, no production/metric file changed. The only repo writes are this dossier and
  the read-only `tools/cc_cadence_precision_investigation.py`. The corpus `tools/corpus/default_modcad` is a
  diagnostic regen of the committed batch_analyze (no code change).
- **Did NOT build the discriminator** — derived + simulated only (validated re-impl, 0/326 mismatch).
- **Key-agnostic throughout** — the `chromaticLeadingTone` flag is signature-relative (`keySignatureFifths` +
  pitch content), never a resolved key `[code]`; the anchor used for the variants is the cadence-derived
  key-agnostic anchor. No resolved-key/`KeyArea` dependency entered the simulation.
- **Marginal lift reported honestly** — no over-modulating build is recommended; the 4d-ii precision-lean
  governs.
- Numbers are `[probe]` on `tools/corpus/default_modcad` (WiR-Bach Default); keys/roots `[oracle]` (When-in-
  Rome rntxt via the pinned `dcml_parser`). **READ-ONLY — no commit.**

*Drafted by CC, 2026-06-15, base `2245aedf82`. Investigation tool `tools/cc_cadence_precision_investigation.py`
(re-impl validated 0/326 vs the committed C++ dump). Full output: `/c/tmp/cc_cadprec.txt`. Feeds the back-half
key-axis sequencing decision (a different layer, not a cadence-gate build).*
