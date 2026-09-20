# J-key-iii — STEP 1: the WIRING integration characterization (READ-ONLY) + Step-2 spec

> **HELD — uncommitted, diagnostic-only, READ-ONLY. No code change in this step.**
> Source characterization of where/how the scoped constrained-joint KEY decision
> (`decideJointKey`) plugs into production, ahead of the wiring (Step 2). Every claim is
> cited to `file:line` at source; nothing is measured (no build, no regen). The producer
> and all production paths are untouched; HEAD `2245aedf82` unchanged.
>
> **Date:** 2026-06-15. **HEAD:** `2245aedf82`. **Scope:** `src/composing/` resolver →
> KeyArea → `basisIndep`, `src/notation` RN bridge, `tools/batch_analyze.cpp`
> `--dump-joint-key`. This dossier **is** the Step-2 wiring spec.

---

## 0. Headline — three load-bearing findings before any wiring

1. **The substitution point is a NEW GLOBAL SECOND PASS, not a per-region replacement.**
   Production resolves the key *and emits the chord* in a single forward per-region loop
   ([regionanalyzer.cpp:418-454](src/composing/analysis/region/regionanalyzer.cpp#L418-L454)).
   `decideJointKey` is a **piece-global Viterbi** over all regions
   ([jointkeydecision.cpp:380-433](src/composing/analysis/section/jointkeydecision.cpp#L380-L433))
   — it cannot slot into the forward loop. Wiring requires a **2-pass restructure**:
   pass-1 resolve+chord (today) → joint re-key over all regions → pass-2 chord
   re-emission under the joint key. The clean home for it is inside / wrapping
   `region::analyzeRegions` (both the bridge and the batch tool traverse it; §2).

2. **⛔ There IS a value-level resolved-key → chord-root → joint-key dependency — surfaced
   per §3.4.** `decideJointKey` never *reads* a key (type-level no-circularity is real and
   unit-tested — `ProductionKeyEchoedNotRead`, J-key-i report §1). BUT config A's
   cadence-anchor + modulation + bass-is-root terms consume the region `rootPc`/`bassPc`
   ([jointkeydecision.cpp:181-195, 320-337](src/composing/analysis/section/jointkeydecision.cpp#L181-L195)),
   and `rootPc` is the **production chord winner's root**, which itself depends on the
   resolved key via `diatonicRootContribution` folded into `basisIndep`
   ([chordanalyzer.cpp:1544-1555](src/composing/analysis/chord/chordanalyzer.cpp#L1544-L1555)).
   So the wired chain is `K0 → R0 → (cadence/modulation from R0) → K_joint → R_joint`. This
   is **NOT an infinite loop / hard circularity** (it is a finite, well-defined 2-pass), and
   the J-key-i §10 echo-only property **survives as a single forward substitution** — *but
   only if the joint key is decided ONCE from the pass-1 chords and the pipeline does NOT
   iterate to a fixpoint*. The wiring must freeze the joint key from pass-1 evidence (§4).

3. **⛔ The producer on disk is the SUPERSEDED J-key-ii formulation, not the ratified J-key-i
   one.** The instruction ratifies wiring *"J-key-i's soft … +3.80/+3.50/+12.24 pp; S2
   −140/−96/−1706"* and §3.7 states the residual is *"56 stems remain at the signature
   reading."* That profile is the **J-key-i strong-signature-backbone** soft decision. The
   current `jointkeydecision.{h,cpp}` is the **J-key-ii global-signature-soften** state
   ([jointkeydecision.h:42-52](src/composing/analysis/section/jointkeydecision.h#L42-L52),
   `signaturePrior = 0.30`
   [jointkeydecision.h:151](src/composing/analysis/section/jointkeydecision.h#L151)),
   whose measured win is **smaller and Default/Baroque-S2-WORSE-than-production**
   (`cc_j_key_ii_report.md` §3: +2.41/+2.51/+11.27 pp; S2 +55/+36 vs prod on Default/Baroque,
   −1588 Jazz). Wiring the code *as it stands today* delivers the shrunk J-key-ii win, **not**
   the ratified J-key-i numbers, and would **regress Default/Baroque genuine-key-error count
   vs production**. Step 2 must first resolve which formulation is wired (§8). **RATIFIED
   2026-06-15: the user chose "restore J-key-i first" — Step 2's first action is to revert
   the producer to the J-key-i strong-signature-backbone before wiring (§8, §9.0).**

Everything else (the consumer map, the representation gap, the hysteresis disposition) is
formulation-independent and fully characterized below.

---

## 1. The production key-resolution pipeline + call order (Q1)

The feed-forward path, in order, with the data each stage hands the next:

| # | Stage | File:line | Produces / hands forward |
|---|---|---|---|
| 1 | **Per-region key resolution** (forward loop, hysteresis-threaded) | [regionanalyzer.cpp:418-423](src/composing/analysis/region/regionanalyzer.cpp#L418-L423) | `localKey` = `KeyModeAnalysisResult` (winner@0), passing `prevKeyResult` for hysteresis |
| 2 | **Chord emission** under that key | [regionanalyzer.cpp:453-454](src/composing/analysis/region/regionanalyzer.cpp#L453-L454) | `analyzeChord(tones, localKeyFifths, localKeyMode, …)` → chord winner `R0`; `basisIndep` folds `diatonicRootContribution(rootPc, keyTonicPc, scale)` ([chordanalyzer.cpp:1544-1555](src/composing/analysis/chord/chordanalyzer.cpp#L1544-L1555)) |
| 3 | **Region store** | [regionanalyzer.cpp:534-543](src/composing/analysis/region/regionanalyzer.cpp#L534-L543) | `HarmonicRegion{ chordResult=R0, keyModeResult=localKey, … }` |
| 4 | **Key stabilization** (1-region-island removal) | [sectionanalyzer.cpp:87-107](src/composing/analysis/section/sectionanalyzer.cpp#L87-L107) | **rewrites** `region.keyModeResult.{keySignatureFifths,mode}` for non-persistent islands |
| 5 | **Degree / function / sparse re-derivation** under the stabilized key | [sectionanalyzer.cpp:109-143](src/composing/analysis/section/sectionanalyzer.cpp#L109-L143) | `function.degree`, `keyTonicPc`, `keyMode`, `diatonicToKey`; re-refines sparse quality |
| 6 | **Cadence / pivot / modulation detection** | [sectionanalyzer.cpp:172-302](src/composing/analysis/section/sectionanalyzer.cpp#L172-L302) | gated by `hasAssertiveKeyConfidence(keyModeResult)` = `normalizedConfidence ≥ 0.8` ([sectionanalyzer.cpp:150-154](src/composing/analysis/section/sectionanalyzer.cpp#L150-L154)) |
| 7 | **KeyArea grouping** (confidence-gated) | [sectionanalyzer.cpp:930-957](src/composing/analysis/section/sectionanalyzer.cpp#L930-L957) | a new `KeyArea` opens only when `(fifths,mode)` diverges **AND** `normalizedConfidence ≥ kAnnotateKeyConfidenceThreshold (0.8)` ([sectionanalyzer.h:86](src/composing/analysis/section/sectionanalyzer.h#L86)); `keyAreaId` set per region |
| 8 | **RN / chord-symbol rendering** (bridge) | [notationcomposingbridge.cpp:1117-1146](src/notation/internal/notationcomposingbridge.cpp#L1117-L1146) | RN's **effective key = the enclosing `KeyArea`** (`romanKeyFifths/Mode = keyAreas[id].keyFifths/.mode`), per-region key as fallback; re-contextualizes chord degree to it |

**Orchestration boundary (critical for §2):** the notation production path is
`analyzeRegions(...)` → **`analyzeSection(score, …, rawRegions)`** → bridge emit
([notationimplodebridge.cpp:1375-1377](src/notation/internal/notationimplodebridge.cpp#L1375-L1377);
mirrored in pipeline_snapshot_tests
[pipeline_snapshot_tests.cpp:325-327](src/notation/tests/pipeline_snapshot_tests/pipeline_snapshot_tests.cpp#L325-L327)).
`analyzeSection` **takes the regions as a parameter** ([sectionanalyzer.cpp:362-364](src/composing/analysis/section/sectionanalyzer.cpp#L362-L364)) — it does NOT call
`analyzeRegions`; it performs stages 4-7 above. So `analyzeRegions` (stages 1-3) is the
**single producer** of the per-region resolved key + chord for the whole pipeline, and the
RN's key is derived downstream from those per-region keys (stages 4-8). The status-bar /
chord-symbol path reads the **per-region** key
([notationcomposingbridge.cpp:278-280, 1116-1118](src/notation/internal/notationcomposingbridge.cpp#L278-L280));
`notationcomposingbridgehelpers.cpp:186` is a separate *single-tick* resolver query, not the
pipeline path.

**Diagnostic call site (today):** `decideJointKey` is invoked **only** from
`writeJointKeyJson` ([batch_analyze.cpp:1069-1114](tools/batch_analyze.cpp#L1069-L1114)),
fed from the already-analyzed regions (`r.keyRanked` → `localCandidates`; `r.chord`/
`r.alternatives` → `chordAlts`; `r.key` → echoed `prodTonicPc`). No production path calls it
([jointkeydecision.h:76-79](src/composing/analysis/section/jointkeydecision.h#L76-L79)).

---

## 2. The plug-in point (Q2)

**Recommendation: a NEW global re-key pass that wraps `analyzeRegions`, entirely inside
`src/composing/` (the CLAUDE.md autonomous zone). Override the per-region key, then re-emit
the chord. Do NOT override post-hoc inside `analyzeSection` alone** (that would update RN
labels but leave the chord winner stale on the chord axis).

Why this point and not the alternatives:

- **Replace the resolver output in the forward loop ([regionanalyzer.cpp:418](src/composing/analysis/region/regionanalyzer.cpp#L418))** — *impossible*: `decideJointKey` needs **all
  regions** (global Viterbi); region *i*'s key depends on regions *i±k*. A forward loop
  cannot supply that.
- **Override `region.keyModeResult` at the head of `analyzeSection`** — *insufficient alone*:
  `analyzeSection` re-derives only degree/function/sparse-quality (stage 5), **not** the full
  `analyzeChord` template scoring. The chord winner `rootPc`/`quality` would stay `R0`
  (computed under `K0`), so `basisIndep` would NOT reflect the joint key — contradicting the
  ratified scope (*"feeds basisIndep (chord emission)"*, instruction §1).
- **A 2-pass inside / wrapping `analyzeRegions`** — *correct*. `analyzeRegions` already owns
  the chord-emission call ([regionanalyzer.cpp:453](src/composing/analysis/region/regionanalyzer.cpp#L453)), and **both** consumers (`analyzeSection` in the bridge/snapshot path, and
  `batch_analyze`'s region pipeline) traverse it. Shape:
  1. Pass-1: run the existing forward loop → regions with `K0` + `R0` (unchanged).
  2. Build `JointKeyRegionInput[]` from those regions (identical to
     [batch_analyze.cpp:1069-1110](tools/batch_analyze.cpp#L1069-L1110)); call
     `decideJointKey` once → per-region `(jointTonicPc, jointIsMajor)`.
  3. For each region: **map** the joint `(tonic,isMajor)` → `(keySignatureFifths,
     KeySigMode, confidence)` (the §3 representation gap), write it into
     `region.keyModeResult`, and **re-run `analyzeChord`** with the joint key to refresh
     `chordResult` (so `basisIndep` reflects it).
  4. Hand the re-keyed, re-chorded regions to `analyzeSection` unchanged (stabilization +
     KeyArea + RN follow automatically).

This keeps the entire change in `src/composing/` (no `src/notation`/`src/engraving` edit) —
the bridge consumes `AnalyzedSection` agnostically — and makes the corpus tool and production
share one code path.

**Single cleanest substitution choice:** *replace the resolver's per-region output* (step 3),
not *post-hoc override the final label*. The joint decision is a key-axis replacement that
must feed the chord axis; overriding only the rendered label leaves the two axes inconsistent.

---

## 3. The representation gap (Q3) — the core of the Step-2 design

`decideJointKey` emits, per region, only `softTonicPc` + `softIsMajor` (a **boolean**
major/minor), plus structural flags
([jointkeydecision.h:169-194](src/composing/analysis/section/jointkeydecision.h#L169-L194)).
Production consumers expect a richer `KeyModeAnalysisResult`
([keymodeanalyzer.h:125-134](src/composing/analysis/key/keymodeanalyzer.h#L125-L134)):
`keySignatureFifths`, a **full 21-value `KeySigMode`**, `tonicPc`, `score`, and
`normalizedConfidence`. The gaps, by consumer:

| Field the joint decision does NOT supply | Who reads it | Consequence if absent / naively mapped |
|---|---|---|
| **`normalizedConfidence`** (per region) | KeyArea grouping gate (≥0.8, [sectionanalyzer.cpp:940-941](src/composing/analysis/section/sectionanalyzer.cpp#L940-L941)); `hasAssertiveKeyConfidence` for **all** cadence/pivot detection ([sectionanalyzer.cpp:150-154, 175-176](src/composing/analysis/section/sectionanalyzer.cpp#L150-L154)); bridge status-bar `keyConfidence` ([notationcomposingbridge.cpp:280](src/notation/internal/notationcomposingbridge.cpp#L280)) | **THE core gap.** With no confidence, KeyArea grouping has no divergence gate (every key change opens an area, or none does), and cadence detection silently turns on/off. A value cannot be invented. |
| **Full `KeySigMode`** (Dorian/Mixolydian/HarmonicMinor/…) | degree lookup ([sectionanalyzer.cpp:110-119](src/composing/analysis/section/sectionanalyzer.cpp#L110-L119)), RN spelling ([notationcomposingbridge.cpp:1138-1145](src/notation/internal/notationcomposingbridge.cpp#L1138-L1145)), chord-symbol spelling | `isMajor → {Ionian, Aeolian}` **collapses the 21-mode space to binary**. Production's analyzeKeyMode can currently emit Dorian/Mixolydian etc.; the joint override erases that on every re-keyed region. **Note the irony:** the 56 partial-signature residual stems ARE Dorian (§7) — they would render as Aeolian, not their notated mode. |
| **`keySignatureFifths`** | KeyArea identity / collapse key ([sectionanalyzer.cpp:91-93, 937](src/composing/analysis/section/sectionanalyzer.cpp#L91-L93)), degree lookup, chord-symbol accidental spelling | Must be derived from `(tonicPc, isMajor)` via `ionianTonicPcForMode` ([keymodeanalyzer.h:537](src/composing/analysis/key/keymodeanalyzer.h#L537)) inverted: major → tonic's circle position; minor → relative-major fifths. **Decision needed** for the partial-signature case where the joint tonic's natural fifths ≠ the notated fifths (J-key-i pins to notated; see §7). |
| **`score`** (raw) | hysteresis margin compare ([keyresolver.cpp:333](src/composing/analysis/key/keyresolver.cpp#L333)) | Moot once the joint Viterbi **replaces** per-region hysteresis (§5); not needed downstream of the override. |
| **KeyArea span boundaries** | KeyArea construction ([sectionanalyzer.cpp:930-957](src/composing/analysis/section/sectionanalyzer.cpp#L930-L957)) | The joint decision *internally* has a key path + modulation spans ([jointkeydecision.cpp:282-284](src/composing/analysis/section/jointkeydecision.cpp#L282-L284)), but exposes only per-region `(tonic,isMajor)`. KeyArea reconstruction from the per-region series still needs the confidence gate above. |

**The load-bearing gap is per-region confidence.** Two clean (non-inventing) resolutions for
Step 2:
- **(a) Extend the producer** to emit a per-region confidence derived from the Viterbi `dp`
  margin (terminal/per-region best − second-best, [jointkeydecision.cpp:399-422](src/composing/analysis/section/jointkeydecision.cpp#L399-L422)) mapped through the existing confidence sigmoid
  ([keymodeanalyzer.h:349-350](src/composing/analysis/key/keymodeanalyzer.h#L349-L350)). This
  is a **producer change** (so it must be re-measured — it does not alter the *decision*, only
  adds a field, but the field then drives KeyArea/cadence, which IS a behavior change).
- **(b) Carry the production `normalizedConfidence`** from the matching pre-joint local
  candidate (the `localCandidates[k]` whose `(tonic,isMajor)` == the joint pick;
  [jointkeydecision.cpp:314-319](src/composing/analysis/section/jointkeydecision.cpp#L314-L319)),
  falling back to a documented constant when the joint pick is not among the local candidates
  (a modulation-span state). Reuses a real measured confidence; no new producer math.

Either is defensible; **(b) is lower-risk** (no producer logic change, reuses an existing
calibrated number). The choice is a Step-2 decision — neither invents a value out of thin air.

---

## 4. Circularity / feed-forward proof (Q4)

**Inputs to `decideJointKey`, classified by when they are computable:**

| Input | Source | Computed before resolution? | Depends on the resolved key? |
|---|---|---|---|
| `pitchClassMask` (collection prior) | sounding notes | **yes** (pure notation) | no |
| `localCandidates` | `analyzeKeyMode` via `keyRanked` ([batch_analyze.cpp:1090-1096](tools/batch_analyze.cpp#L1090-L1096)) | **yes** — `analyzeKeyMode` scores all (tonic,mode) vs the pitch window + notated/corrected signature; it never reads a resolved key | no (the *order* is hysteresis-shaped, but the producer aggregates order-independently — `localAgg` sum + any-match, [jointkeydecision.cpp:236-241, 314-319](src/composing/analysis/section/jointkeydecision.cpp#L236-L241)) |
| cadence anchor + modulation spans | `detectLocalModulations(cad)` where `cad.rootPc/quality/pcMask` ([jointkeydecision.cpp:181-195](src/composing/analysis/section/jointkeydecision.cpp#L181-L195)) | **no** — `rootPc` is the chord winner, produced AFTER resolution | **YES (value-level)** — chord winner root depends on the key via `diatonicRootContribution`→`basisIndep` |
| `bassPc` (bass-is-root term) | `r.bassPc` = `chord.identity.bassPc` | after chord analysis | weakly (bass is ~lowest sounding note; key-insensitive in practice) |
| `prodTonicPc/prodIsMajor` | echoed | n/a | **NOT read** — unit-tested (`ProductionKeyEchoedNotRead`, J-key-i report §1) |

**Verdict:**
- **No type-level circularity.** `decideJointKey` cannot read a key — the inputs are
  pitch/tick/root-shaped ([jointkeydecision.h:114-139](src/composing/analysis/section/jointkeydecision.h#L114-L139)); the echoed prod key is provably unread.
- **There IS a value-level dependency** `resolvedKey K0 → chordRoot R0 → cadence/modulation →
  jointKey K_joint`, because the cadence/modulation instruments consume the production chord
  root, and that root is a (weak) function of `K0` via the single diatonic-root bonus folded
  into `basisIndep` ([chordanalyzer.cpp:1544-1555](src/composing/analysis/chord/chordanalyzer.cpp#L1544-L1555)).
- **This is NOT a hard circularity / infinite loop.** When wired, `K_joint` is decided
  **once** from the pass-1 chords `R0`; the pass-2 re-emission produces `R_joint`; the joint
  key is **not** recomputed from `R_joint`. The pipeline is a finite, well-defined
  `resolve → chord → re-key → re-chord` 2-pass. The J-key-i §10 echo-only property (the joint
  decision is a pure function of pass-1 outputs + key-agnostic evidence, feeding nothing back)
  **survives** under this single-forward substitution.

**Mandatory Step-2 constraints to keep it clean (these are the "surface it" of §3.4):**
1. **Decide the joint key from the SAME pass-1 chords the diagnostic measured, and freeze it.**
   This makes the *wired key axis byte-identical to the measured `jointKey` decisions* — the
   +3.80/+3.50/+12.24 pp (or whichever formulation, §8) **transfers exactly**; only the
   downstream chord re-emission is new behavior.
2. **Do NOT iterate to a fixpoint** (`re-key → re-chord → re-key → …`). That closes the loop
   into a true feedback system that was never measured and could oscillate (the §7 "balloon"
   risk). Single pass only.
3. The bass term and the cadence/modulation instruments stay on the **pass-1** roots; do not
   recompute them from `R_joint`.

The dependency is **weak** (the key nudges the chord root only on vertically-ambiguous
sonorities) but **nonzero** — hence it is documented as a constraint on staging, not waved
away.

---

## 5. Hysteresis disposition (Q5)

Production smooths the key in **two** layers; the joint Viterbi interacts with both:

- **Layer A — note-based hysteresis** inside the resolver
  ([keyresolver.cpp:329-345](src/composing/analysis/key/keyresolver.cpp#L329-L345), the
  documented "must NOT touch" trap; uses `relativeKeyHysteresisMargin` for same-signature
  switches). It reorders `results` so the prev-region mode is kept unless the challenger clears
  a margin.
- **Layer B — 1-region-island stabilization** in `analyzeSection`
  ([sectionanalyzer.cpp:87-107](src/composing/analysis/section/sectionanalyzer.cpp#L87-L107)),
  a second smoothing that overwrites a non-persistent single-region key with its neighbors'.

The joint decision **replaces both** with a global key-path Viterbi + `transitionPenalty`
modulation cost ([jointkeydecision.cpp:380-413](src/composing/analysis/section/jointkeydecision.cpp#L380-L413)) — it is itself the smoothing layer.

**Disposition — clean *coexistence-then-supersede*, NOT removal:**
- **Keep Layer A running** inside `resolveKeyAndModeRanked`. Its output `keyRanked` is the
  `localCandidates` seed the joint decision reads, and the J-key-i win was **measured on top of
  hysteresis-shaped candidates**. Removing it would change `keyRanked` → change
  `localCandidates` → change the joint output → **the measured numbers would no longer
  transfer.** Layer A's *ordering* effect is harmless to the producer (order-independent
  aggregation, §4), so it costs nothing to leave in.
- **The joint key becomes the final per-region value**, so Layer A's *winner@0* promotion no
  longer reaches the chord axis / RN (the joint Viterbi already decided the path). Layer A
  survives as an input-shaper only.
- **Layer B (island stabilization) must be reconsidered.** If the override writes the joint key
  into `region.keyModeResult` **before** `analyzeSection`, Layer B will island-remove *joint*
  single-region keys too — double-smoothing that the Viterbi already did, and that could
  *undo* a correct one-region joint modulation. Step-2 decision: either (i) run the joint
  override **after** Layer B (stabilize the pass-1 keys, then overwrite with the joint key —
  cleanest, Layer B becomes inert on the final value), or (ii) disable Layer B on
  joint-overridden regions. Recommendation: **(i)** — it leaves Layer B untouched for any
  non-overridden path and makes the joint key authoritative. This needs source confirmation in
  Step 2 of the exact ordering inside `analyzeSection` relative to the chosen override site.

**What breaks if hysteresis is naively removed:** the J-key-i/ii measurement substrate
disappears (the soft win was computed against post-hysteresis `keyRanked`), so the wired result
would be an **unmeasured** decision. Do not remove it as part of wiring.

---

## 6. The behavior-change surface + sizing (Q6)

**Which production outputs move, and the mechanism:**

| Output | Moves? | Mechanism | Sizing |
|---|---|---|---|
| **Per-region resolved key** in `.ours.json` (`r.key`) | **yes, directly** | the override replaces it | **MEASURED** (J-key-i §7 adjudication): regions whose key changes (soft vs prod): Default **1621** (768 win + 388 loss + 137 conv + 328 lateral), Baroque **1606**, Jazz **4218**; **net win−loss +380 / +340 / +1192** |
| **Key-axis S2** (genuine key error) | **yes — the win (formulation-dependent)** | fewer genuine key errors | J-key-i: **−140 / −96 / −1706**. J-key-ii (current code): **+55 / +36 / −1588** vs prod (Default/Baroque WORSE — see §8) |
| **Chord winner** (`rootPc`/`quality`) in `.ours.json` | **yes, a subset** | re-emit under joint key → `diatonicRootContribution` flips ambiguous winners ([chordanalyzer.cpp:1544-1555](src/composing/analysis/chord/chordanalyzer.cpp#L1544-L1555)) | **UNMEASURED** — bounded above by the ~1621/1606/4218 key-changed regions; actual flips are the key-sensitive ambiguous subset (far fewer). The diagnostic was byte-identical, so this is **Step-2's first measurement** |
| **BIR gate** (57 / 23 / 57) | **CAN move on all 3 presets** | chord-winner flips on `bassIsRoot=false` cases | **UNMEASURED** — the CLAUDE.md hard-stop axis; the diagnostic never moved it (byte-identical). **Any BIR=false increase on any preset = hard stop**, must DCML-adjudicate every moved case |
| **KeyArea spans / RN keys** | **yes** | RN key = enclosing KeyArea ([notationcomposingbridge.cpp:1129-1130](src/notation/internal/notationcomposingbridge.cpp#L1129-L1130)); KeyArea grouping depends on the (new) confidence (§3) | proportional to key changes; **also sensitive to the confidence-mapping choice** (§3) |
| **Snapshot goldens** (pipeline_snapshot_tests, P1-P4) | **yes** | chord symbols + RN pinned byte-exact | must refresh **only after** DCML-adjudication confirms each move is correct ([CLAUDE.md `--update-goldens` rule]) |
| **Cadence / pivot markers** | **yes** | gated by `hasAssertiveKeyConfidence` (the confidence gap, §3) + key match ([sectionanalyzer.cpp:184-188](src/composing/analysis/section/sectionanalyzer.cpp#L184-L188)) | confidence-mapping-dependent |

**Magnitude summary:** the **key axis** movement is sized (~16% of scored regions on
Default/Baroque, ~43% on Jazz change key — J-key-i §7). The **chord axis / BIR / snapshot**
movement is **strictly unmeasured today** (the diagnostic is byte-identical by construction)
and is the central thing Step-2 must measure and adjudicate. Do not state a BIR delta — it is
unknown until the wired corpus is regenerated.

---

## 7. The tail residual (Q7)

**Under the ratified J-key-i strong-signature-backbone formulation:** the 56 partial-signature
stems (Dorian/Mixolydian notated one accidental short — e.g. `bwv254`, `bwv265`: D minor
notated 0 flats) **remain at the signature reading** — the home pair is pinned to the notated
fifths, so the true (note-inferred) key is structurally unrepresented (J-key-i report §6a,
the ~17%/56-stem ceiling). This **matches production**, which is itself locked to the notated
signature ([keyresolver.cpp:81-106](src/composing/analysis/key/keyresolver.cpp#L81-L106) +
`partialSignatureCorrection`, which only nudges within the declared class) — so it is the
**documented, ratified residual, NOT a regression vs production**. ✓ (confirmed at source: the
resolver has no path to a tonic a fifth/fourth from the notated signature beyond the
one-step partial-signature correction.)

**Caveat — this is the J-key-i profile, and the code on disk is J-key-ii (§8).** The current
`jointkeydecision.cpp` (global soften) **partially recovers** ~36% of these stems
(`cc_j_key_ii_report.md` §4.2: 20-22/56), i.e. it would **change** ~20 stems' keys away from
the signature reading — which is *not* the "remain at signature" residual the instruction
§3.7 describes. The J-key-ii-redux targeted override (which would have recovered more) was
measured **not separable** and **not built** (`cc_j_key_ii_redux_report.md` §0/§7 — DO NOT
WIRE; decision reverts to user). So Q7's stated residual holds **only if Step 2 wires the
J-key-i formulation**; under the current J-key-ii code the residual is a different (partial,
~36%-recovered) set. This is the §8 precondition again.

---

## 8. ⛔ The load-bearing precondition: WHICH formulation is being wired

The instruction ratifies *"J-key-i's soft constrained-joint key decision … +3.80/+3.50/+12.24
pp; S2 −140/−96/−1706"* and a *"56 stems remain at the signature reading"* residual. **All
three of those facts are the J-key-i strong-signature-backbone formulation.** The producer on
disk is the **J-key-ii global-signature-soften** formulation
([jointkeydecision.h:42-52, 151](src/composing/analysis/section/jointkeydecision.h#L42-L52);
note-inferred home candidates + `signaturePrior=0.30`,
[jointkeydecision.cpp:206-284](src/composing/analysis/section/jointkeydecision.cpp#L206-L284)),
whose measured profile is materially different:

| | J-key-i (ratified target) | J-key-ii (code on disk) |
|---|---|---|
| key-acc vs prod | +3.80 / +3.50 / +12.24 pp | +2.41 / +2.51 / +11.27 pp |
| S2 vs prod | **−140 / −96 / −1706** | **+55 / +36** / −1588 (Default/Baroque **worse than prod**) |
| 56 partial-sig stems | remain at signature (the §3.7 residual) | ~36% recovered (changes ~20 stems) |
| home key construction | strong signature pair backbone | signature demoted to a 0.30 soft prior + note-inferred candidates |
| status | J-key-ii report **recommended NOT to wire this**; redux **not separable, not built** | this is the current `jointkeydecision.{h,cpp}` |

**Wiring the code exactly as it stands today delivers the J-key-ii shrunk win and regresses
Default/Baroque genuine-key-error count vs production.** The "max correct inferring first"
ratification + the cited J-key-i numbers + the §3.7 residual all point to the **J-key-i
strong-backbone** formulation (= redux report standing option #1, "accept J-key-i's ceiling").

**RATIFIED 2026-06-15 — the user chose "restore J-key-i first."** Step 2's first action is to
**restore the producer to the J-key-i strong-signature-backbone** (recoverable from the
J-key-i report §1 / git history of the HELD file) before wiring; the J-key-ii global-soften
and the redux override are both superseded for this purpose. The 56 partial-signature stems
therefore remain at the signature reading as the documented residual (§7), matching
production. This is now a settled precondition, not an open question.

---

## 9. Recommended Step-2 staging (the wiring spec)

0. **PRECONDITION — RATIFIED 2026-06-15: restore J-key-i strong-backbone (§8).** Revert
   `jointkeydecision.{h,cpp}` from the on-disk J-key-ii global-soften to the J-key-i
   strong-signature-backbone (per the J-key-i report §1) before any wiring, and re-confirm
   the diagnostic reproduces the +3.80/+3.50/+12.24 pp profile. The J-key-ii and redux
   formulations are superseded for J-key-iii.
1. **Resolve the representation gap (§3):** pick the per-region confidence source ((b) carry
   the matching local-candidate `normalizedConfidence`, recommended) and the
   `(tonicPc,isMajor)→(fifths,KeySigMode,confidence)` mapping (incl. the partial-signature
   fifths rule — pin to notated fifths under J-key-i).
2. **Wire the 2-pass at the `analyzeRegions` boundary (§2):** pass-1 (today) → `decideJointKey`
   once over all regions (frozen, §4) → override `region.keyModeResult` → re-emit
   `analyzeChord` under the joint key. Keep it all in `src/composing/`.
3. **Settle hysteresis ordering (§5):** keep Layer A (resolver hysteresis, input-shaper); apply
   the joint override **after** Layer B stabilization so the Viterbi path is authoritative.
4. **Measure the production delta on BOTH axes:** regen all 3 presets
   (`run_bach_preset.py` Baroque/Jazz/Default) + `characterise_bir_false.py`; run both test
   suites + `pipeline_snapshot_tests`. Confirm the **key axis** matches the measured `jointKey`
   decisions (the win transfers, §4).
5. **DCML-adjudicate every moved BIR case and every moved snapshot case.** Un-adjudicated
   **BIR=false increase on any preset = hard stop** (CLAUDE.md). Refresh snapshot goldens only
   after each move is confirmed DCML-correct.
6. **HELD for ratification; commit only on a clean adjudication** (key win realized, no
   un-adjudicated BIR regression, snapshots refreshed-and-justified). Sync `docs/scoring_model.md`
   if any scoring term moves; this is the **first intentional production behavior change on the
   key axis**, so the commit must say so.

---

## 10. Stop conditions (this read-only step)

| Condition | Status |
|---|---|
| Any code change / wiring in this step | **None** — read-only; HEAD `2245aedf82` unchanged; no build run |
| A circularity / feedback path found | **Surfaced (§2.2, §4):** no type-level circularity / no infinite loop, but a weak value-level `key→chordRoot→jointKey` dependency. Safe **only** as a single frozen forward 2-pass (do not iterate). Constraints specified |
| A consumer needs info the joint decision cannot supply | **Surfaced (§3):** per-region confidence + full mode + fifths. Two non-inventing resolutions given; no value invented |
| Uncertain about a pipeline edge | Resolved at source with file:line; the formulation question (§8) was surfaced — not guessed — and **ratified by the user (restore J-key-i first)** on 2026-06-15 |

**Net:** the integration is characterizable and wireable as a clean single-forward 2-pass. The
formulation is settled (restore J-key-i strong-backbone, §8); the one remaining Step-2
implementation decision is the per-region-confidence source (§3, recommendation given). No stop
condition forces an abort.

**HELD — read-only. No production path touched. Step 2 (wiring) is separately ratified.**
