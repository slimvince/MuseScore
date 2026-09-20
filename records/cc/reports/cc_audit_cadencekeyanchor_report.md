# CC primary audit — cadencekeyanchor (empirical) + reconciliation with the Cowork audit

> **HELD — gitignored (`cc_*.md`), READ-ONLY, NO source change, NO build, NO commit.** Layer-by-layer
> acceptance audit of `src/composing/analysis/section/cadencekeyanchor.{h,cpp}` against its single
> responsibility, judged vs the TRUE analysis (DCML / When-in-Rome oracle), not the BIR gate. Reconciles
> with `cowork_audit_cadencekeyanchor.md`.
>
> **Date:** 2026-06-17. Base = HEAD (`a03c2493bb`). Anchor data read from the committed-weight per-stem
> `cadenceAnchor` block in `tools/corpus/default_4ciii{,_abs}` (emitted by
> `batch_analyze --dump-cadence-anchor`; weights `kWeightBase=1 / Structural=2 / Chromatic=1 / Finality=1`
> unchanged since 4c-iii, so the dump equals the current code's output). DCML keys `[oracle]` via the pinned
> `dcml_parser` + `compare_rn`. New read-only tool: `tools/cc_audit_cadence_anchor_accuracy.py` (reuses the
> established parsers verbatim, redefines no metric, writes nothing). Tags: `[code]` read at source,
> `[probe]` ran a script, `[oracle]` DCML GT, `[theory]` music-theoretic.

---

## 0. Headline

| reconciliation target | Cowork claim | CC empirical verdict |
|---|---|---|
| **#1 detection FP mechanism** | I→IV / I→V structurally false-positive; subdominant spans 72% spurious | **CONFIRMED for I→IV** at source + 72% reproduced. **I→V is MISCHARACTERIZED** — diatonic I→V is an *ascending* fifth, structurally excluded; the dominant-direction over-detection is **V/V→V** (a chromatic applied dominant), not I→V. |
| **#2 anchor accuracy vs DCML** | "~44% pin-wrong" | **NOT REPRODUCED. The anchor is 72.4% correct / 27.6% pin-wrong** at piece level (236/326); ~75% correct in the floor frame. The "~44%" is not in any B/B2 dossier and appears to conflate the span-level modulation-detection precision (~47–53%) with anchor accuracy. **Corrected.** |
| **#3 authentic-only coverage** | pieces with no authentic cadence → un-anchored | **0 un-anchored / 326 (100% detected).** But this is a **symptom of over-detection, not coverage health** — the I→IV false positives backfill an anchor for every piece; the limit does not *manifest* as un-anchored pieces on an all-cadential Bach corpus. |
| **#4 dual-responsibility / shared primitive** | detection primitive shared with `detectLocalModulations`; split the two | **CONFIRMED at source** — `detectLocalModulations` calls `detectAuthenticCadences`+`aggregateGlobalAnchor` over the shared `CadenceRegionInput`. Decomposition note **agreed**. |

**One line.** Cowork's qualitative reading of this layer is right on the mechanism and the obligations; CC's
measurement **corrects two numbers**: the anchor is materially **better than "~44% wrong" (it is ~72% right
at piece level)**, and the "I→V" instance of the FP mechanism is really **V/V→V**. The genuine wall is the
**dominant-direction over-read (9.8%) + partial-signature degradation (75.2%→58.9%)**, not the relative-pair
flip the layer was built to fix (only 6.4% pin-wrong relative-pair at piece level).

---

## 1. Responsibility (the contract) — agreement with Cowork

The header exposes two jobs: `detectAuthenticCadences` (key-agnostic V→I detection) and
`aggregateGlobalAnchor` (vote cadences into one global tonic+mode). **CC agrees this is borderline dual
responsibility**, and confirms the shared-primitive observation **at source** `[code]`:
`localmodulationdetector.cpp:143,145` calls **both** `detectAuthenticCadences(regions,…)` and
`aggregateGlobalAnchor(cadences)` over the same `CadenceRegionInput` stream (`:122,:136,:157`). So the
*detection primitive* + its input struct are a reusable layer consumed by ≥2 callers (the modulation
detector and the `--dump-cadence-anchor` diagnostic), while *aggregation policy* (salience weights, Picardy)
is anchor-specific. **Phase-2 decomposition note CONFIRMED:** detection primitive vs global-anchor
aggregation policy warrant separate units.

---

## 2. Correctness gap #1 — the leading-tone test (CONFIRMED for I→IV, REFINED for "I→V")

### 2.1 The mechanism, verified at source `[code]`
`detectAuthenticCadences` ([cadencekeyanchor.cpp:61-123](src/composing/analysis/section/cadencekeyanchor.cpp#L61-L123))
fires for an adjacent pair `a→b` iff: `a.quality==Major` (`:83`); `b.quality∈{Major,Minor}` (`:90`);
`pcMod12(a.rootPc−7)==b.rootPc` (descending fifth, `:95`); and `(a.rootPc+4) mod 12` is present in `a`'s
mask (`:103-104`). The leading-tone test is **structurally vacuous**: `(root+4)` is the *major third of a*,
present in every complete major triad, and is one semitone below `root(b)` by construction. **So the test
cannot distinguish a genuine V→I from any major-triad → triad-a-fourth-above motion.** Worked example
C→F: `root(F)=5 == pcMod12(0−7)=5` ✓, `E` (C's third) in mask ✓ → C→F (a plain **I→IV**) is emitted as an
"authentic cadence to F." **Confirmed; matches `cc_b_guard_scoping_dossier.md` §1.1.**

### 2.2 The "I→V" refinement (a reconciliation correction) `[code][theory]`
Cowork: "…passes, as does I→V." **This is imprecise.** A *diatonic* I→V (C→G) is an **ascending** fifth:
`pcMod12(root(C)−7)=5≠7=root(G)`, so the pair (C,G) **never matches** (`:95`). What *does* fire toward the
dominant scale-degree is **V/V→V** — e.g. D(major)→G: `pcMod12(2−7)=7=root(G)` ✓, requiring a chromatic F♯
in `a`. That is a *tonicization of the dominant* (an applied dominant), not a diatonic I→V. CC's own B
dossier already states this ("the I→V / V-tonicization case … e.g. a D7→G in C major, V/V→V"). **So the
dominant-direction over-detection is V/V→V, and the cowork label "I→V" should read "V/V→V."** (Direction of
the error in the data confirms it — §3: the wrong anchors sit a *fifth above* the global tonic, i.e. on the
dominant, reached by tonicizing it.)

### 2.3 The "72% subdominant spurious" — CONFIRMED, but it is a SPAN-level number `[probe][oracle]`
`cc_b_guard_scoping_dossier.md` §3.2 (414 DCML-scorable modulation spans): subdominant-of-anchor spans are
60 total, 17 TP → **28% right / 72% spurious**. **Reproduced and agreed.** Important framing for #2 below:
this 72% is a *cadence/span* false-positive rate (the detection primitive's precision), **not** the
aggregated *anchor's* accuracy. Cowork stated both in one breath ("~44% pin-wrong vs DCML; subdominant spans
72% spurious"); they are different frames and only the 72% is corroborated.

---

## 3. Correctness gap #2 — anchor accuracy vs DCML (the "~44%" CORRECTION) `[probe][oracle]`

`tools/cc_audit_cadence_anchor_accuracy.py tools/corpus/default_4ciii` — piece-level anchor vs DCML global,
326 WiR-Bach stems, all with parseable global key:

```
#3 COVERAGE:   anchor DETECTED 326/326 (100.0%)   UN-ANCHORED 0/326 (0.0%)

#2 ANCHOR ACCURACY (detected stems, N=326):
   correct        236  (72.4%)
   relative_pair   21  ( 6.4%)
   parallel         5  ( 1.5%)
   dominant        32  ( 9.8%)   <- anchor a fifth above global tonic (V read as tonic)
   subdominant      8  ( 2.5%)
   other           24  ( 7.4%)
   --> CORRECT 236/326 (72.4%);  PIN-WRONG 90/326 (27.6%)
```

**The anchor is 72.4% correct / 27.6% pin-wrong at piece level.** The floor frame agrees
(`cc_cadence_anchor_measure.py` on `default_4ciii_abs`): region-weighted over the 1452-region relative-pair
floor, **1092/1452 = 75.2% correct / 24.8% wrong**; stem-weighted 137/181 = 75.7% correct. **No frame
reproduces "~44% pin-wrong."** A grep of `cc_b_guard_scoping_dossier.md`, `cc_b2_subdominant_guard_report.md`,
`cc_cadence_key_investigation_dossier.md`, and `docs/stage4c_cadence_key_design.md` finds **no "44%" and no
"pin-wrong"** — the figure is not sourced from B/B2. **Most likely it conflated the 4d-i
modulation-span precision (47% → ~53% FP, B §3.3) — a downstream consumer's metric — with the anchor's own
accuracy.** **Reconciliation correction: the anchor's pin-wrong rate is ~25–28%, not ~44%.**

### 3.1 What KIND of wrong (refines Cowork #5) `[probe][oracle]`
The layer's stated *raison d'être* is breaking the relative-major/minor tie. At the global-anchor level it
**largely succeeds**: relative-pair is only the **3rd** error mode (6.4%, 21 stems), behind
**dominant-direction (9.8%, 32 stems)** and **"other" (7.4%, 24 stems)**. So Cowork #5 ("least complete on
the cases it was built for") is **directionally right but the dominant mechanism is now the leading anchor
failure**, not the relative flip. Exemplars `[oracle]`: dominant — `bwv255 g=Cmaj→a=Gmaj (0.60)`,
`bwv153.9 g=Cmaj→a=Gmaj (0.42)`, `bwv245.22 g=Emaj→a=Bmaj (0.67)`; other — `bwv176.6 g=Bbmaj→a=Cmin`,
`bwv148.6 g=Fmin→a=F#min`. The dominant errors are the §2.2 V/V→V over-reads surviving aggregation.

### 3.2 Partial-signature degradation — CONFIRMS Cowork #2 + #5 `[probe][oracle]`
Splitting detected stems by whether the notated signature fifths match the DCML global key's canonical
fifths (a partial/modal-signature proxy):

```
   [PARTIAL/modal-sig]  56 stems  correct 33 (58.9%)   rel_pair 3  dom 6  sub 2  other 10
   [matched-sig]       270 stems  correct 203 (75.2%)  rel_pair 18 dom 26 sub 6  other 14
```

**A 16.3 pp accuracy gap on partial-signature pieces** (58.9% vs 75.2%). This empirically confirms Cowork
correctness-gap #2 (`chromaticLeadingTone` computed vs the notated collection mis-fires on Dorian/partial
signatures) and completeness-gap #5 (Dorian → wrong relative). The "other" rate doubles (10/56 = 17.9% vs
14/270 = 5.2%) on partial-sig pieces — the raised-LT salience marker is unreliable exactly there.
(Proxy caveat: signature/global-key fifths-mismatch includes some non-modal cases; the *direction* is
robust, the exact 56-stem set is approximate.)

### 3.3 chromaticLeadingTone at source — Cowork #2 mechanism confirmed `[code]`
`c.chromaticLeadingTone = !((diatonicMask >> leadingTone) & 1u)` (`:118`), and `diatonicMask` is
`diatonicMaskFromFifths(keySignatureFifths)` (`:65,:50-57`) — purely the **notated** signature. On a
Dorian-notated minor (e.g. fewer flats than the key implies) the true raised LT can fall inside the notated
collection → `chromaticLeadingTone=false` → the genuine V→i loses its salience bonus. Mechanism confirmed;
§3.2 is its measured footprint.

---

## 4. Completeness gaps — measured

| Cowork gap | CC verdict |
|---|---|
| **#3 authentic-only** | **Does not manifest as un-anchored pieces here: 0/326 un-anchored** `[probe]`. On an all-cadential Bach chorale corpus every piece fires ≥1 authentic cadence — but largely *because* the I→IV/V→V false positives backfill coverage. So the limit is real in principle; on this corpus it converts into **precision** loss (§3), not **coverage** loss. It WOULD surface as un-anchored on a repertoire whose key is signaled by plagal/deceptive/half cadences. **Agreed as a contract limit; re-scoped from "un-anchored pieces" to "false coverage masking a precision problem."** |
| **#4 global-only / no modulation** | Structurally true `[code]` — one `(tonicPc,mode)` per span. Note: by a coarse distinct-local-key proxy 322/326 stems "modulate," but that proxy conflates tonicization with modulation and is weak; only **4 stems are single-key (all 4 anchored correctly)**. The global anchor still lands the *global* key 72% of the time despite the corpus being almost entirely multi-key. **Agreed; delegated to the modulation layer.** |
| **#5 incompletely resolves own target** | See §3.1 — relative-pair pin-wrong is modest at piece level (6.4%); the layer mostly *does* break the relative tie globally. Cowork's "78→82% (B2)" is a region-level relative-axis figure in a different frame; not contested, but the **piece-anchor view shows the dominant over-read, not the relative flip, is now the dominant residual.** |
| **#6 windowing-unstable** | **CONFIRMED** by `cc_b2_subdominant_guard_report.md` §6 `[probe]`: on the 16-measure bridge window the anchor flips (mozart→F conf↑1.0, corelli→Gm, bwv806 A/D/E across windows) vs the stable full-score anchor (C 0.679 / Cm 0.423). Correctness depends on input window size. **Agreed — and it is the upstream blocker the B2 guard could not get past.** |

---

## 5. Phase-2 carry-forward — agreement

- **SOFT-evidence imprecision propagates.** Confirmed at source `[code]`: the false cadences and the anchor
  feed `detectLocalModulations` (`localmodulationdetector.cpp:143-145`) → spans → `jointkeydecision.cpp:230`
  → the wired SOFT key (B §1.2). So the obligations in §2–§3 **do** matter for key-axis correctness, not just
  this layer's local quality. **Agreed.**
- **Shared detection primitive → decomposition.** Agreed (§1).
- **The leading-tone ambiguity is inherent to key-agnostic detection.** Agreed `[theory]`: without a home,
  C→F is identical whether C is I (→I→IV) or V (→V→I in F). The obligation is the **key-agnostic
  cadence-precision ceiling** — addressable by the constrained-joint "cadence = SOFT" soft-decode /
  calibration, not a within-layer patch. **Agreed.** CC adds: the **partial-signature** dimension (§3.2) is a
  *second*, partly separable ceiling — a spelling-aware / mode-aware LT test could lift the 58.9% partial-sig
  bucket without touching the inherent I↔IV ambiguity.

---

## 6. Reconciliation summary (what changed vs the Cowork audit)

1. **Anchor accuracy "~44% pin-wrong" → 27.6% pin-wrong (72.4% correct), piece level; ~25% wrong floor
   frame.** The 44% is unsourced and not reproduced; corrected. (§3)
2. **"I→V" → "V/V→V."** Diatonic I→V is structurally excluded (ascending fifth); the dominant over-read is
   an applied-dominant tonicization. (§2.2)
3. **"72% subdominant spurious" is a SPAN-level (detection-primitive) number, confirmed** — distinct from the
   anchor's accuracy. (§2.3)
4. **#3 coverage re-scoped:** 0 un-anchored on this corpus; the authentic-only limit shows up as *false
   coverage / precision loss*, not as un-anchored pieces. (§4)
5. **Leading residual is the dominant-direction over-read (9.8%) + the partial-sig bucket (58.9%)**, not the
   relative-pair flip (6.4%) the layer targets. (§3.1, §3.2)
6. **Agreed in full:** dual-responsibility + shared-primitive decomposition (§1); chromaticLeadingTone
   partial-sig mis-fire (§3.2-3.3); windowing instability (§4 #6); SOFT propagation (§5); the inherent
   key-agnostic precision ceiling (§5).

**Obligations pinned for this layer (Phase-2):** (a) split detection primitive from aggregation policy;
(b) the key-agnostic cadence-precision ceiling → constrained-joint SOFT decode / calibration (out-of-layer);
(c) spelling/mode-aware leading-tone test to recover the partial-signature bucket (in-layer-feasible);
(d) windowed-anchor stability (upstream blocker for the modulation/joint consumers).

---

## 7. Artifacts (HELD, no commit)
- `cc_audit_cadencekeyanchor_report.md` (this file).
- `tools/cc_audit_cadence_anchor_accuracy.py` (read-only; reuses `compare_rn`/`compare_analyses`/`dcml_parser`;
  opens existing `.ours.json` + WiR rntxt; touches no binary/corpus/golden — the 0/353×3 byte-identity gate
  is N/A). Reproduce: `python tools/cc_audit_cadence_anchor_accuracy.py tools/corpus/default_4ciii`.
- No source edit, no build, no snapshot/golden refresh, no `docs/` sync (no scoring/key term changed). Source
  tree unchanged from HEAD `a03c2493bb`.

*Drafted by CC, 2026-06-17. Read-only layer audit; reconciles `cowork_audit_cadencekeyanchor.md`. Cowork
verifies at source; user ratifies.*
