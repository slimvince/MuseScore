# CC primary audit — localmodulationdetector (empirical) + reconciliation with the Cowork audit

> **HELD — gitignored (`cc_*.md`), READ-ONLY, NO source change, NO production behavior change, NO commit.**
> Layer-audit #2 (`docs/layer_audit_plan.md`) of
> `src/composing/analysis/section/localmodulationdetector.{h,cpp}` against its single responsibility, judged
> vs the TRUE analysis (DCML / When-in-Rome oracle), **not** the BIR gate. Reconciles
> `cowork_audit_localmodulationdetector.md`.
>
> **Date:** 2026-06-17. Base = HEAD (`a03c2493bb`). **Working-tree caveat:** the target `.cpp/.h` carry an
> uncommitted diff vs HEAD (the B2 subdominant-guard *diagnostic fields* + a *dormant* guard whose suppression
> is gated on `jointKeyWiringEnabled()`, default **OFF**). The guard never fires in the diagnostic path, so the
> **committed span set is byte-identical to HEAD** — independently verified: the span sets in
> `tools/corpus/default_modcad` and `tools/corpus/default_mod_b2` agree on **0/353** stems' span-set mismatch
> (867 spans). This audit measures that HEAD span set.
>
> **Data:** the committed-span `modulation` block **and** the full per-cadence `cadenceAnchor.cadences` list
> emitted by `batch_analyze --dump-modulation --dump-cadence-anchor` into `tools/corpus/default_modcad`
> (353 stems; 326 with parseable DCML coverage). DCML keys `[oracle]` via the pinned `dcml_parser` /
> `compare_analyses` / `compare_rn`. New read-only tool: `tools/cc_audit_localmodulation_accuracy.py` (reuses
> the established parsers verbatim; writes nothing). Tags: `[code]` source, `[probe]` script, `[oracle]` DCML,
> `[theory]` music-theoretic.

---

## 0. Headline

| reconciliation target | Cowork `[prov]` | CC empirical verdict |
|---|---|---|
| **precision / recall vs DCML** | precision **~47%** / recall **~33%** (4d-i) | **CONFIRMED exactly** at region level — **47.0% precision (1347/2867) / 33.4% recall (1347/4036)**. New span frame: **53.6% precision over modulation-claims (222/414)**, **27.6% segment recall (287/1040)**. |
| **self-confirmation (load-bearing)** | the confirmation gate is **circularly satisfied by the same spurious cadence that seeds the span** → cannot filter FPs; *implied ~all FPs self-confirmed* | **CONFIRMED as the dominant mechanism, REFINED to 81.8%** — of **192** FP modulation spans, **157 (81.8%)** are confirmed ONLY by a spurious cadence (no DCML-genuine cadence to the span's key); **82.3% rest on a single cadence**. Contrast: **99.1% of TP spans** carry a genuine cadence. **Not 100%:** the other **18.2%** DO contain a genuine cadence but remain FP via **establishment over-extension** (a distinct second FP mechanism — §3.2). |
| **FP composition (subdom/dom share)** | "~43% of FPs are exactly the dominant/subdominant misreads" | **CONFIRMED — 42.2%** (subdominant 24.5% + dominant 17.7%). But **foreign (32.3%) is the single largest bucket** and relative is 19.3%: a **majority (51.6%) of FPs are foreign/relative**, NOT the I→IV/V-of-V cases. |
| **inherited cadence wall (FP roots)** | FP roots trace to the cadence detector's I→IV / V/V→V over-reads (NOT "I→V") | **CONFIRMED decisively** — **100%** of subdominant-FP confirming cadences have a **dominant-region root = the home tonic (a literal I→IV)**; **100%** of dominant-FP confirming cadences have **dominant root = home+2 (V/V→V)**, **84.2% carrying the chromatic leading tone**. Matches the corrected-K1 mechanism from the cadence-anchor audit. |
| **shared cadence primitive → decomposition** | detection primitive shared with anchor; split | **CONFIRMED at source** (`:142-145`). Agreed. |
| **correctness upstream-bounded by the cadence wall** | the layer's own gates provably cannot filter the self-confirming FPs | **AGREED for the 81.8% self-confirmed majority.** Adds: the 18.2% over-extension FPs are an **in-layer** establishment/tolerance defect, partly separable from the upstream cadence ceiling. |

**One line.** Cowork's reading of this layer is correct on every mechanism; CC's measurement **confirms the
prov precision/recall exactly (47/33)**, **quantifies the self-confirmation claim at 81.8%** (the load-bearing
result — strong but not universal), and **decisively confirms the I→IV / V-of-V cadence-wall trace at 100%**.
The one refinement: ~18% of FPs are not self-confirmed but **over-extended genuine tonicizations**, a second
FP mechanism that lives *in this layer* (loose collection tolerance + nearest-cadence assignment), not solely
upstream.

---

## 1. Responsibility (the contract) — agreement with Cowork

**One sentence.** Inputs: a key-agnostic ordered `CadenceRegionInput` stream (root pc + quality + pitch-class
mask per region) + the notated signature fifths. Job: commit a **local-key span** only when a contiguous run
of regions is both **ESTABLISHED** (≥ `kEstablishmentMinChords`=5 regions consistent with a candidate local
key's diatonic collection) **and CONFIRMED** (an authentic cadence of that key resolves inside the run).
Output: `ModulationDetectionResult` = committed `LocalKeySpan`s + the key-agnostic global anchor.

**Shared-primitive observation — CONFIRMED at source** `[code]`: `detectLocalModulations`
([localmodulationdetector.cpp:142-145](src/composing/analysis/section/localmodulationdetector.cpp#L142-L145))
calls **both** `detectAuthenticCadences(regions, keySignatureFifths)` and `aggregateGlobalAnchor(cadences)`
over the same `CadenceRegionInput` stream — exactly the primitive `cadencekeyanchor` aggregates. So the
*cadence-detection primitive* has **≥2 consumers** (the anchor diagnostic + this detector). **Phase-2
decomposition note CONFIRMED and agreed** (same finding as the cadence-anchor audit §1).

Single-responsibility verdict: the layer itself is cohesive (one job: span commitment). The dual-responsibility
is *upstream* (the shared primitive), not within this TU.

---

## 2. Correctness vs DCML — precision / recall (CONFIRMS the prov) `[probe][oracle]`

`python tools/cc_audit_localmodulation_accuracy.py tools/corpus/default_modcad` — 326 WiR-Bach stems:

```
REGION-level (independent reproduction of the 4d-i frame):
  PRECISION = TP/nonHome = 1347/2867 = 47.0%
  RECALL    = hits/DCMLmod = 1347/4036 = 33.4%

SPAN-level:
  total committed spans            : 798
  modulation claims (K != global)  : 414
  span TP (correct modulation)     : 222   home-correct (K==local==G): 368
  span FP overmod (DCML home)      : 144   span FP wrongkey (mod, wrong K): 64
  --> span PRECISION over mod-claims = 222/414 = 53.6%
  --> segment RECALL = 287/1040 = 27.6%
```

- The **region-level 47.0% / 33.4% reproduces the canonical 4d-i baseline EXACTLY** (and equals
  `cc_b2_subdominant_guard_measure.py`'s `baseline` row, re-run this session: 47.0% / 33.4%). **Cowork's prov
  precision ~47% / recall ~33% is CONFIRMED, not corrected.**
- The **span frame** is the new granularity: precision over modulation-claims is **53.6%** (a span is judged
  by the majority DCML local key over its covered regions), modestly higher than the region rate because the
  TP spans tend to be longer; **segment recall is 27.6%** (287 of 1040 DCML modulation segments are covered by
  a correctly-keyed span). **Both frames agree the layer commits roughly as many spurious modulation spans as
  real ones, and misses ~70% of real DCML modulations.**
- Note for the cross-layer record: the unsourced "~44%" the cadence-anchor audit flagged sits squarely in this
  47–54% modulation-span precision band — corroborating that audit's hypothesis that "~44%" conflated *this
  consumer's* span precision with the anchor's own (72.4%) accuracy.

---

## 3. The SELF-CONFIRMATION test (the load-bearing claim) `[probe][oracle]`

**Method.** A committed span of key K is "confirmed" by any authentic cadence with `tonicPc==K`,
`minorMode==K.mode`, resolving inside `[startTick, endTick)` (the exact C++ condition, `:240-241`). For each
**FP modulation span**, classify each confirming cadence against the oracle: **genuine** iff the DCML *local*
key at the cadence's resolution tick equals K (an independent real cadence to K); **spurious** otherwise (the
same over-read that seeded the candidate). A span is **self-confirmed only** iff *every* confirming cadence is
spurious.

```
FP modulation spans                       : 192
  ... confirmed ONLY by spurious cadence(s): 157  (81.8%)   <- self-confirmed
  ... with an INDEPENDENT genuine cadence  :  35  (18.2%)
  ... resting on a SINGLE cadence (count==1): 158  (82.3%)
CONTRAST  TP spans                        : 222
  ... with a genuine confirming cadence    : 220  (99.1%)
```

### 3.1 The claim HOLDS for the majority (81.8%) — CONFIRMED `[probe][oracle]`
**81.8% of FP spans have NO independent confirming cadence** — the only cadence(s) resolving inside are ones
the DCML oracle does *not* read as a real cadence to the span's key. **82.3% rest on a single cadence.** This
is the precise empirical content of Cowork's claim: the confirmation gate is satisfied by the very cadence
that generated the candidate (candidates *are* per-cadence local tonics, `:141`), so for these spans the gate
adds **zero** discriminating power — it cannot tell a real modulation from the I→IV / V-of-V over-read that
created it. The TP contrast (99.1% genuinely confirmed) shows the gate's *output* correlates with truth, but
only because real cadences self-confirm too; it is **non-discriminating on the FP side**. **Mechanism
CONFIRMED.**

### 3.2 REFINEMENT — it is 81.8%, not 100%: a second, in-layer FP mechanism `[probe][oracle][theory]`
The remaining **18.2% (35) of FP spans DO contain a DCML-genuine cadence to K** yet are still FP. Worked
example (validated by hand) — **bwv11.6** span `[0, 5280)` claiming **A major** (home D major):

```
  tick 0–1440 : DCML local D (home)        <- span over-grabs these
  tick 2400–4320: DCML local A (a REAL V-tonicization; cadence to A at 4320,
                   endsPhrase=true, chromaticLeadingTone=true — a genuine E→A)
  tick 5280   : DCML local D (home)
```

The confirming A-cadence is **genuine**, but the span **over-extends** the brief real tonicization-of-V across
the surrounding home-D regions (its majority DCML local is D, so it scores FP). The cause is **in this layer**:
the loose collection tolerance (`kPitchTolerance=2`, `:56`) lets D-major regions read as "A-consistent" (A and
D major collections differ by one pc: G♯/G♮), and **nearest-cadence assignment** (`:161-204`) then claims them
for A. So beside the upstream self-confirmation wall there is a **distinct establishment/tolerance over-reach**
that converts genuine tonicizations into spurious *sustained* spans. This is partly fixable in-layer (tighter
tolerance / non-maximal runs) without touching the cadence ceiling.

**Net:** Cowork's self-confirmation claim is the **dominant** FP mechanism (81.8%) but **not exclusive**; the
honest split is **~82% upstream-bounded (cadence wall) + ~18% in-layer over-extension**.

---

## 4. FP composition (CONFIRMS ~43%, refines the majority) `[probe][oracle]`

Relation of each FP span's key K to the DCML global G:

```
  subdominant :  47 (24.5%)   dominant : 34 (17.7%)   relative : 37 (19.3%)
  parallel    :  12 ( 6.2%)   foreign  : 62 (32.3%)
```

- **subdominant + dominant = 42.2%** — **CONFIRMS Cowork's "~43% of FPs are the dominant/subdominant
  misreads."** These are the cadence-wall cases (§5).
- **Refinement:** **foreign (32.3%) is the largest single bucket** and relative is 19.3% — so **51.6% of FPs
  are foreign/relative**, outside the I→IV/V-of-V story. The foreign bucket is the over-extension cases of §3.2
  (a real cadence to a distant key, over-grabbed) plus chains of spurious cadences; the relative bucket
  inherits the anchor's relative-pair confusion (cadence-anchor audit §3.1) propagated into the
  `agreesWithAnchor` home/modulation split.

---

## 5. Inherited cadence wall — FP roots trace to I→IV / V/V→V (CONFIRMS corrected K1) `[probe][oracle]`

For each FP confirming cadence, read its **dominant-region root** (at `dominantTick`) from the region stream:

```
  subdominant-FP confirming cadences      : 56
    ... dominant root == HOME tonic (I→IV) : 56  (100.0%)
  dominant-FP confirming cadences         : 38
    ... dominant root == home+2 (V/V→V)    : 38  (100.0%)
        ... AND chromatic leading tone     : 32  (84.2%)
```

- **Subdominant FPs (K = home+5): 100% of confirming cadences have dominant root = the home tonic** — i.e. a
  literal `home(major) → home+5` motion, the **I→IV** the cadence detector mis-fires as "authentic cadence to
  IV" (cadence-anchor audit §2.1; the leading-tone test is structurally vacuous because the home third is the
  major-third-of-the-dominant by construction).
- **Dominant FPs (K = home+7): 100% have dominant root = home+2 (the supertonic), 84.2% with a chromatic
  leading tone** — i.e. `(home+2, major) → home+7`, a **V/V→V** applied-dominant tonicization. This is **NOT
  diatonic I→V** (an ascending fifth, structurally excluded by `:95` of the cadence detector). **CONFIRMS the
  cadence-anchor audit's correction of Cowork's "I→V" label to "V/V→V."**

So the FP roots of the 42.2% subdominant+dominant bucket are **fully accounted for** by the cadence detector's
two structural over-reads. **The modulation layer faithfully inherits the cadence-precision wall** — its own
gates (sustained ≥5, confirmed) cannot filter them because (a) the over-reads self-confirm (§3) and (b) the
I↔IV oscillation is itself sustained (the run-length gate passes).

---

## 6. Completeness vs the case space `[probe][oracle][theory]`

| gap | CC verdict |
|---|---|
| **recall ~33%** | **CONFIRMED** — region recall 33.4%, segment recall 27.6%. The layer misses ~2/3–3/4 of DCML modulations. |
| **authentic-cadence-confirmed ONLY** | **CONFIRMED at source** `[code]` (`:239-256` — confirmation requires an `AuthenticCadence`, i.e. a descending-fifth major→triad with the LT present). A modulation signaled by a **half / plagal / deceptive** cadence, or by **sustained scale-change without an authentic cadence**, cannot be confirmed → systematic recall floor. On the all-cadential Bach corpus this shows as the 27–33% recall, not as a visible coverage hole. |
| **establishment over-extension** (new, §3.2) | **MEASURED** — `kPitchTolerance=2` + nearest-cadence assignment over-grab genuine brief tonicizations into spurious sustained spans (18.2% of FPs). An in-layer obligation (tolerance / segmentation), partly separable from the upstream cadence wall. |
| **relative-pair / partial-signature inheritance** | **CONFIRMED** — relative is 19.3% of FPs; the layer inherits the cadence anchor's relative-pair confusion (anchor 6.4% pin-wrong at piece level, worse on partial signatures, cadence-anchor audit §3.1–3.2) through `agreesWithAnchor` (`:267-269`) which mislabels home vs modulation when the anchor itself is on the wrong relative/dominant. |
| **conservative merge → recall** `[code]` | `:206-209` commits **non-overlapping maximal runs** of one assigned key; closely-spaced distinct real modulations or a modulation interrupted by a passing chord that breaks the run are split below the 5-region floor and lost — a recall-side structural choice ("prefer missing a borderline modulation over inventing one"). |

---

## 7. Gaps → tagged obligations (Phase-2 carry-forward)

1. **[correctness · key-axis · fix:upstream/behavior-changing]** The **81.8% self-confirmed FP** mass is
   **upstream-bounded by the cadence-precision wall** — this layer's sustained+confirmed gates provably cannot
   filter the self-seeding I→IV / V-of-V over-reads. Root obligation is the **cadence layer / constrained-joint
   SOFT decode**, not here. (Third key-axis layer in a row whose central gap is the SAME cadence ambiguity →
   strong cross-layer signal the fix is upstream.) **Agreed with Cowork.**
2. **[correctness · key-axis · fix:structural-in-layer]** The **18.2% over-extension FP** mass is an
   **in-layer** defect: `kPitchTolerance=2` + nearest-cadence maximal-run assignment grab home/foreign regions
   adjacent to a genuine tonicization. Candidate in-layer fixes (tighter/asymmetric tolerance; non-maximal runs
   bounded by the cadence's actual support) are testable against the oracle without touching the cadence
   ceiling. **CC addition beyond Cowork.**
3. **[completeness · key-axis · fix:behavior-changing]** **Authentic-cadence-only confirmation** floors recall
   at ~27–33%. Admitting half/plagal/deceptive confirmation or a sustained-scale-change signal is the
   recall-side obligation. **Agreed.**
4. **[completeness · key-axis · fix:upstream]** **Relative-pair / partial-signature inheritance** (19.3% of
   FPs) — the `agreesWithAnchor` home/modulation split is only as good as the anchor; addressed by the
   cadence-anchor obligations (spelling/mode-aware LT; windowed-anchor stability). **Agreed.**
5. **[structural · phase-2]** **Shared cadence primitive** (anchor + modulation consumers) → its own layer.
   **Agreed.**

---

## 8. Reconciliation summary (what CC confirms vs refines in the Cowork audit)

1. **precision 47% / recall 33% — CONFIRMED exactly** (region 47.0/33.4); span frame added (53.6% / 27.6%). (§2)
2. **Self-confirmation — CONFIRMED as the dominant mechanism, quantified at 81.8%** (82.3% single-cadence; TP
   contrast 99.1%). **Refined:** not 100% — the other 18.2% are genuine-but-over-extended (a second, in-layer
   FP mechanism). (§3)
3. **"~43% of FPs are dominant/subdominant" — CONFIRMED (42.2%).** Refined: foreign (32.3%) + relative (19.3%)
   are the majority of FPs. (§4)
4. **Cadence wall — CONFIRMED decisively (100% / 100%)**, and the dominant case is **V/V→V, not I→V** (matches
   the cadence-anchor audit correction). (§5)
5. **Shared-primitive decomposition + upstream-bounded correctness — AGREED** (§1, §7), with the in-layer
   over-extension obligation added (§7.2).

---

## 9. Artifacts (HELD, no commit)
- `cc_audit_localmodulationdetector_report.md` (this file).
- `tools/cc_audit_localmodulation_accuracy.py` (read-only; reuses `compare_rn`/`compare_analyses`/`dcml_parser`;
  opens existing `.ours.json` + WiR rntxt; touches no binary/corpus/golden — byte-identity gate N/A).
  Reproduce: `python tools/cc_audit_localmodulation_accuracy.py tools/corpus/default_modcad`.
- No source edit, no build, no production behavior change, no snapshot/golden refresh, no `docs/` sync (no
  scoring/key term changed). HEAD span set measured (default_modcad ≡ default_mod_b2 span sets, 0/353 mismatch).

*Drafted by CC, 2026-06-17. Read-only layer audit #2; reconciles `cowork_audit_localmodulationdetector.md`.
Cowork verifies the methodology at the committed object + reconciles; user ratifies.*
