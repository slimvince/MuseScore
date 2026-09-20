# CC Dossier — local-modulation scoping: current key-path behavior, the gap, the de-masking diagnostic

> **READ-ONLY scoping + diagnosis. No production behavior change, no commit.** Base HEAD `2245aedf82`.
> The one tooling addition (Task A) is a **reporting-only** sub-split of `compare_rn`'s `partial` bucket:
> it adds a diagnostic breakdown and changes **no** metric category or number (byte-identity proven, §1.2).
> Every claim tagged `[code]` (read source), `[probe]` (ran a script), `[oracle]` (DCML When-in-Rome GT).
> Inputs read: `cc_tonicization_modulation_metric_dossier.md`; `docs/key_path_design.md`;
> `docs/stage6_functional_layer_design.md`; `docs/stage4c_cadence_key_design.md`;
> `src/composing/analysis/key/{keyresolver,keymodeanalyzer}.{h,cpp}`;
> `src/composing/analysis/region/regionanalyzer.cpp`; `src/composing/analysis/section/{sectionanalyzer,cadencekeyanchor}.{h,cpp}`;
> `tools/compare_rn.py`; `tools/cc_tonicization_modulation_probe.py`; `tools/batch_analyze.cpp`.
> Probes: the new `compare_rn --partial-key-breakdown` (committed-shape, reporting-only) + the existing
> `tools/cc_tonicization_modulation_probe.py` + a throwaway key-axis probe (`/c/tmp/cc_keyaxis_probe.py`,
> reuses `compare_rn`/`compare_analyses`/`dcml_parser` verbatim). Surface: WiR-Bach `tools/corpus/default`
> (the user-run config), 326/353 covered, 10 109 matched regions.

---

## §0 — TL;DR

| | Finding | Basis |
|---|---|---|
| **The metric MASKS, by design** | `compare_rn` scores by chord **root**, not the RN's reference key, so our home-key label is credited `partial`/`exact` even when DCML modulated and we stayed home. The de-masking sub-split (Task A) exposes it: **19.8 % (237/1197) of the credited `partial` bucket is "we stayed home, DCML modulated."** Byte-identity of every headline number proven. | §1 [probe] |
| **The resolver barely modulates** | DCML reads a **local modulation on 39.9 % (4036/10109)** of regions. We **track it only 9.7 %**; we **stay in the home/global key 74.5 % (3006/4036)**. | §2.4 [probe][oracle] |
| **Stay-home is structural, not a tuning knob** | The resolver is a **global-key estimator anchored to the (unchanging) notated signature, run per region**, with (a) a constant circle-of-fifths **proximity penalty** pulling every region toward the home key, (b) a 16-beat **lookback window** that drags home-key material into every window, and (c) **no local-key/modulation state at all**. Hysteresis is *stickiness toward the previous region* (and only on mode changes) — it can never *pull toward* a newly-established local key. There is no "sustained + cadence → commit to the local key" mechanism to size against; it is **absent**, not mis-tuned. | §2 [code] |
| **Real key-axis correctness ≈ 54.4 %** | Our key == DCML **local** key on **54.4 %** of regions (and only **393** of those are a genuinely tracked modulation; the rest are no-modulation in-key). The root-based headline `rn_agree` (45.7 %) **overstates** key-correct agreement — **6.9 % of rn_agree (320 pairs) is key-axis wrong but root-credited.** | §3.3 [probe] |
| **Realistic ceiling of a "sustained + local cadence → modulate" rule** | Population = **3006** stayed-home-under-modulation regions. **~83 %** are sustained ≥5 chords and **~93 %** carry a local V→I cadence [oracle] → perfect-detection ceiling ≈ **2500**; the committed cadence detector's measured realized fraction (55.7 %→75.2 %) caps realistic capture at **~1800–2300** regions. The metric lever inside that: **2001** `key_disagree` cases would move to `rn_agree` (≈ +19.8 pp). | §3.1–§3.2 |
| **Integration layer = the KEY layer (Stage 4)** | The modulation **decision** (open a local KeyArea / re-key a sustained span) belongs in the **key resolver / a section-scoped KeyArea pass** — *not* Stage 6. KeyArea today is a downstream post-grouping of the per-region argmax (it inherits stay-home). The cadence instrument already exposes per-cadence local tonics — the confirming signal exists. Stage 6 then *labels* (tonicization vs modulation) from the committed KeyArea. | §4 [code] |
| **Blast radius is real (second sanctioned behavior change)** | The resolved key feeds `analyzeChord` → `basisIndep` → the BIR gate. Re-keying ~1800–2500 region-keys (≈18–25 % of regions) will move RN labels, can move chord roots on the diatonic-sensitive subset (sparse-chord / tonic-prior / rcb), and **will** move pipeline snapshots. Must be DCML-adjudicated + re-gated on **all three presets** (57/23/57). | §5 |

**One-line answer:** the stay-home behavior is a **structural absence of a local-key hypothesis** in a
notated-signature-anchored per-region estimator, the metric **under-penalizes it** (it credits a home-key
root against a modulated local key), the de-masked key-axis is **54.4 %** with a **3006-region** local-modulation
gap, and the lever's home is the **Stage-4 key layer**, gated by the chord-axis ripple.

---

## §1 — Task A: the de-masking diagnostic (reporting-only) + byte-identity proof

### 1.1 What was added `[code]`
`tools/compare_rn.py` gains a **sub-split of the `partial` bucket by reference-key framing** —
`partial_key_subtag()` + the `pk_*` counters + `format_partial_breakdown()` + the `--partial-key-breakdown`
flag (wired into all four CLI modes). It mirrors the existing `key_disagree_subtag` / `--key-breakdown`
exactly (the "orchestration is not a metric definition" basis). A credited `partial` pair is labeled:

- **`local_match`** — our (tonic, mode) == DCML **local** key. Correctly-keyed: the partial is an honest
  root+quality credit (only inversion/extension differs).
- **`home_vs_local`** — our (tonic, mode) == DCML **global** key AND DCML's local key ≠ global. **The masked
  modulation error**: we stayed home, DCML modulated, and the sounding root coincides (our home-key label
  shares the root with DCML's local-key label) so the pair is credited `partial` — hiding that our **key** is wrong.
- **`other`** — credited but our key matches neither side's framing under a real modulation.
- **`keyfail`** — our key string did not parse (the same 2.3 % caveat the key_disagree split reports).

By construction `local_match + home_vs_local + other + keyfail == partial`. **No metric bucket is
redefined**; the `partial` count itself is untouched (the sub-counts are tallied *inside* the existing
`elif pair.category == "partial"` branch).

### 1.2 Byte-identity of the headline numbers `[probe]`
Same command with the existing flags, before vs after the edit:
```
python tools/compare_rn.py --wir-bach tools/corpus/default --key-breakdown --granularity-robust
  → diff(before, after) == EMPTY ("IDENTICAL")
```
Every headline number is unchanged: matched 10109, rn_agree 45.7 % (4621), exact 3424, **partial 1197**,
key_disagree 2780 (S1 2093 / S2 687), quality_disagree 343, root_err 2365, and the full
granularity-robust block. **The new numbers appear only under the new `--partial-key-breakdown` flag.**
(If any of these had moved, that would mean the crediting changed — STOP condition; it did not.)

### 1.3 The de-masking result (WiR-Bach default) `[probe][oracle]`
```
=== DE-MASKING BREAKDOWN of partial (reference-key framing) ===
  partial total: 1197   (count unchanged)
  local_match    our key == DCML LOCAL  (correctly-keyed credit):   872  (72.8%)
  home_vs_local  our key == DCML GLOBAL, DCML modulated (MASKED):   237  (19.8%)
  other          residual framings:                                  72  ( 6.0%)
  keyfail        our key did not parse:                              16  ( 1.3%)
```
**~1 in 5 of every credited `partial` is a masked local-modulation error.** This cross-checks the
metric-check dossier independently: the existing probe shows that emitting the 6-tonic-i `/d` label would
move **237** `key_disagree`→`partial` on the labeler-fired set — the same magnitude, confirming the
masking is a real, sized phenomenon and not an artifact of one population.

---

## §2 — Task B: the current key-path modulation mechanism + the stay-home diagnosis `[code]`

### 2.1 Does the resolver modulate at all?
**Yes in principle, no in practice for established modulations.** `resolveKeyAndModeRanked`
([keyresolver.cpp:206](src/composing/analysis/key/keyresolver.cpp#L206)) is called **per boundary region**
([regionanalyzer.cpp:418](src/composing/analysis/region/regionanalyzer.cpp#L418)), and `analyzeKeyMode`
evaluates the **full 252 candidates** (12 tonics × 21 modes — the loop `for tonicPc 0..11`,
[keymodeanalyzer.cpp:550](src/composing/analysis/key/keymodeanalyzer.cpp#L550)). So the resolved key *can*
differ region-to-region. It does — but those changes are mostly **spurious per-window flips** (the
relative-pair Class-A flips documented in `key_path_design.md` §3.1), not principled sustained-modulation
detection. Measured (§2.4): when DCML modulates, we track it **9.7 %** of the time.

### 2.2 What governs switch-vs-stay — three home-pulling forces, zero local-pulling force `[code]`

1. **Notated-signature anchor.** Each call reads the key signature **at the tick**
   ([keyresolver.cpp:219–221](src/composing/analysis/key/keyresolver.cpp#L219)): `keyFifths =
   keySig.concertKey()`. In Bach chorales the signature is the *global* signature and **does not change**
   across local modulations (they are notated with accidentals). So `keyFifths` is effectively the global
   key for the whole piece.

2. **Circle-of-fifths proximity penalty (the constant home pull).**
   `scoreKeySignatureProximity` ([keymodeanalyzer.cpp:411–419](src/composing/analysis/key/keymodeanalyzer.cpp#L411))
   subtracts `keySignatureDistancePenalty (0.60) × cofDistance(candidate, notatedFifths)` from **every**
   candidate, **every** region. A modulation to the dominant (+1 fifth) costs −0.60 on every region of the
   span; there is **no** opposing term that grows as a local key becomes established. The penalty is a
   flat, persistent bias toward the global key.

3. **16-beat lookback window (content contamination).** The window is
   `[tick − LOOKBACK_BEATS/4, tick + lookahead]` with `LOOKBACK_BEATS = 16` (≈4 measures)
   ([keyresolver.cpp:275–278](src/composing/analysis/key/keyresolver.cpp#L275),
   [metricweights.h:57](src/composing/analysis/scoreharvest/metricweights.h#L57)). Even mid-modulation the
   window straddles the preceding home-key material, diluting the local-key evidence.

4. **Hysteresis is stickiness, not a local pull, and only on mode changes.** The hysteresis block fires
   **only** when `results.front().mode != prevResult->mode`
   ([keyresolver.cpp:329–345](src/composing/analysis/key/keyresolver.cpp#L329)); a tonic-only modulation
   within the same mode (e.g. G major → D major) is **not** damped by it at all. When it does fire it
   *promotes the previous region's key back to the front* — i.e. it **resists** change. It can never
   *pull toward* a newly-established local key.

5. **Declared-mode hint + partial-sig correction** also anchor to the notation (the 1.0 hint
   [keymodeanalyzer.h:324](src/composing/analysis/key/keymodeanalyzer.h#L324); partial-sig correction
   declared-gated [keyresolver.cpp:260](src/composing/analysis/key/keyresolver.cpp#L260)) — additional,
   smaller home pulls.

### 2.3 Is there a "local key / modulation" concept? KeyArea is downstream of stay-home `[code]`
There **is** a `KeyArea` span structure, but it is a **post-grouping over the per-region argmax**, not an
independent local-key detector. `sectionanalyzer.cpp` builds KeyAreas
([sectionanalyzer.cpp:930–957](src/composing/analysis/section/sectionanalyzer.cpp#L930)) by coalescing
adjacent regions with equal `(keyFifths, mode)`, opening a new area only when a region **diverges** AND its
`normalizedConfidence ≥ 0.8` (`kAnnotateKeyConfidenceThreshold`). It consumes `region.keyModeResult` —
whatever the resolver already produced. **If the resolver stayed home, KeyArea stays home.** There is no
local-key hypothesis anywhere; the key is essentially *global signature + per-region argmax + hysteresis*.
(`detectCadences` / `detectPivotChords` are likewise downstream and **circular** for key inference — they
read `chordResult.function.degree`, computed *from* the resolved key, and gate on assertive confidence —
[sectionanalyzer.cpp:156, 198–208, 175–176](src/composing/analysis/section/sectionanalyzer.cpp#L156); the
4c-i investigation already ruled them unusable.)

### 2.4 WHY we stay home where DCML modulates — the core diagnosis `[probe][oracle]`
This is the load-bearing input to the design, so it is **measured, not asserted**. Across the 10 109
matched regions (`/c/tmp/cc_keyaxis_probe.py`, read-only):
```
DCML modulates (local != global):   4036 regions (39.9% of matched)
  we TRACK it (our key == local):    393  ( 9.7%)
  we STAY HOME (our key == global):  3006 (74.5%)
  we read a 3rd key (neither):       637  (15.8%)
```
**Mechanism (pinned to source, not guessed):** the resolver has **no mechanism that could detect a
sustained local key**. It is a per-region global-key estimator whose only forces are three home-pulling
biases (§2.2.2–§2.2.4) and a stickiness term that resists change. There is no accumulation of "this span
has been in the local key for N chords with a confirming cadence." So on a sustained tonicization the
home key wins every region's independent argmax (proximity penalty + lookback contamination), and even in
a window where the local key would momentarily out-score, nothing carries that across the span to commit.
**The gap is the absence of a local-modulation hypothesis, not a mis-tuned hysteresis margin** — widening
or narrowing `hysteresisMargin`/`relativeKeyHysteresisMargin` cannot create a local-key candidate that the
proximity penalty is actively suppressing. (This matches `key_path_design.md` §3, which independently found
the *current* hysteresis compares incommensurable cross-window scores — broken mechanism, not a tunable.)

---

## §3 — Task C: size the gap, the realistic ceiling, and the de-masked real correctness

### 3.1 The gap, honestly sized `[probe][oracle]`
The true local-modulation gap is the **stayed-home-under-modulation** population: **3006 regions = 29.7 %
of all matched** (not just the 2093 `key_disagree` S1 slice — that slice is one *root-bucket view* of it).
Cross-tabulating the de-masking key-class against the `compare_rn` root-bucket shows where the 3006 sit:

| `compare_rn` bucket | stayed-home-under-mod | note |
|---|---:|---|
| exact            | 6    | credited & key-wrong (masked) |
| **partial**      | **237** | credited & key-wrong (the de-masking headline) |
| key_disagree     | **2001** | already a miss = **95.6 % of S1**, matches the metric-check exactly |
| quality_disagree | 206  | partly penalized |
| root_err         | 556  | root already wrong (modulation alone won't fix the root) |
| **total**        | **3006** | |

So of the 3006: **243 are credited (masked)** — 6 `exact` + 237 `partial`; the other **2763 are already
counted as errors** but mis-attributed to the key_disagree/quality/root axes rather than named as
"modulation gap." The de-masking diagnostic's value is **attribution**: it shows the local-modulation gap
is the dominant key-axis problem and surfaces the 243 doubly-hidden ones.

### 3.2 The realistic ceiling of a "sustained span + local cadence → modulate" rule `[probe][oracle]`
From the existing probe on the labeler-fired analog (n=409, correct-key, DCML modulated to our target degree):
**brief ≤2 chords 2.7 %, moderate 3–4 18.1 %, sustained ≥5 79.2 %; 92.7 % carry a local V→I cadence** — and
the metric-check generalized this to the full S1-modulation population (**83.2 % sustained**). So:

- **Perfect-detection ceiling** ≈ the sustained+cadence-confirmed fraction ≈ **83 % of 3006 ≈ ~2500 regions**
  correctly modulatable.
- **The moderate band (~15 %)** is genuinely ambiguous (a 3–4-chord tonicization either notation is
  defensible) — a precision/recall trade, not free recall.
- **The brief band (~1–3 %)** should *stay* as a tonicization (`V/d`) — modulating it would be wrong; this
  is exactly the 6-tonic-i predicate's correct domain.
- **Realized fraction is bounded by detection reliability**, not the ceiling. The committed key-agnostic
  cadence detector measured a realized-correct fraction of **55.7 %** (4c-i) rising to **75.2 %** after the
  4c-iii refinements (`cc_stage4c_*` reports) — so realistic capture ≈ 0.75 × 0.83 ≈ **~1800–2300 regions**,
  not the 2500 ceiling. **Do not bank the ceiling** (the standing 4c qualifier).
- **Harder residue:** the **637 "third-key"** regions (we read neither local nor global — these are S2 key
  errors compounding the modulation question, not pure stay-home) and the **556 root_err** cases (root
  already wrong; a key fix may or may not recover the root via the chord-key feedback).

### 3.3 The de-masked real correctness — how inflated was the headline? `[probe]`
```
Key-axis classification (our key vs DCML LOCAL):
  local_match (our key == DCML local):  5496  (54.4%)   ← honest key-axis correctness
  home_under_mod (stayed home):         3006  (29.7%)
  other (third key):                    1376  (13.6%)
  keyfail:                               231  ( 2.3%)
rn_agree (4621) of which key-axis WRONG (credited via shared root): 320 (6.9%)
```
- **Honest key-axis correctness is 54.4 %** — and only **393 of the 5496** `local_match` regions are a
  genuinely *tracked* modulation; the rest are no-modulation in-key regions. The resolver's modulation
  ability, isolated, is near-zero (§2.4).
- **The root-based `rn_agree` (45.7 %) overstates key-correct agreement.** 320 of the 4621 credited pairs
  (6.9 %) are key-axis wrong; a key-correct-aware rn_agree would be ≈ **(4621−320)/10109 = 42.5 %**
  (≈ −3.2 pp). The inflation is modest *as a fraction of rn_agree today* — **but** the masking compounds
  catastrophically under the rejected naive fix: emitting `V/d` everywhere would move the 2001
  `key_disagree`-stayed-home cases to `partial`, lifting rn_agree to **~65.5 %** while leaving the **key
  wrong on all of them** → **~35 % of "agreements" would be key-axis wrong**. That is the quantified
  metric-gaming harm the metric-check warned about, now sized by the de-masking instrument. The defensible
  refinement is exactly this diagnostic (expose the masking), **not** a crediting change.

---

## §4 — Task D: available signals + the integration layer `[code]`

### 4.1 The signals exist and are sufficient for "sustained + cadence-confirmed local key"
- **Local-cadence confirmation — the committed cadence instrument.** `detectAuthenticCadences`
  ([cadencekeyanchor.h:134](src/composing/analysis/section/cadencekeyanchor.h#L134)) is **key-agnostic by
  construction** (its input `CadenceRegionInput` carries only `{ticks, rootPc, quality, pitchClassMask,
  endsPhrase}` — it cannot read the resolved key) and returns a **per-cadence list** with each cadence's
  **local tonic + mode** (`AuthenticCadence{tonicPc, minorMode, chromaticLeadingTone, endsPhrase}`). This is
  exactly the local V→I confirmation a modulation detector needs. (`aggregateGlobalAnchor` collapses to one
  *global* anchor for the relative-pair tie — the **per-cadence list is the local signal**, and is already
  emitted in the batch diagnostic, [batch_analyze.cpp:951–954](tools/batch_analyze.cpp#L951).)
- **Sustained-span / duration signal.** Region durations (`startTick`/`endTick`) and KeyArea spans exist;
  per-region emission scores (the raw 252 `analyzeKeyMode` scores) exist (currently only top-3 surfaced —
  `key_path_design.md` §2.3 flags exposing top-N as a small additive refactor).
- **Resolver hysteresis margins** exist as the crude two-bucket transition model the proper detector
  generalizes.
- **Verdict:** the signals are **sufficient** for "sustained span + local cadence → local key." The one
  signal partly outside the composing core is the **fermata / phrase-boundary** (`endsPhrase`), read from
  the engraving `Score` in `batch_analyze` ([batch_analyze.cpp:936–947](tools/batch_analyze.cpp#L936)). It
  is a **salience booster, not required** for the core V→I detection — but a *production* detector wanting it
  would need notation→composing plumbing (the standing 4c-iii caveat). Flag, don't block.

### 4.2 Which layer should own the modulation decision
**The KEY layer (Stage 4)** — the resolver / a section-scoped KeyArea pass. Rationale, from the layer model
(`stage6_functional_layer_design.md` §1, `key_path_design.md` §4.2):

- The **modulation decision = changing the resolved key for a span = opening a KeyArea.** That is the key
  layer's single responsibility. `key_path_design.md` §4.2 states it directly: *"Modulation = the KeyArea
  boundary itself."*
- **Stage 6 (functional layer) does NOT own it.** Stage 6 *consumes* the committed key/KeyArea and *labels*
  tonicization-vs-modulation (`stage6_functional_layer_design.md` §1/§3 explicitly lists "tonicization-vs-
  modulation from KeyArea" as a Stage-6 consumer of the key layer's output). Putting the decision in Stage 6
  would re-introduce circularity (label deciding key).

**Single responsibility of the new capability:** *given the per-region key emissions, the key-agnostic
per-cadence local tonics, and span durations, decide the local-key spans (where to modulate) and commit
them as KeyAreas.* It **consumes**: resolver per-region emission scores (or output) + the cadence
instrument + region durations. It **must NOT entangle**: chord root/quality selection (Stage 3), the
functional `/X` labeling (Stage 6), or the Baroque chord-gate thresholds.

**Where it plugs in cleanly — two shapes, both composing-zone:**
1. **Principled (the existing draft): the Stage-4 key decode / HMM** (`key_path_design.md`). Replaces the
   per-region argmax+hysteresis with a global decode whose transition model uses the cadence instrument as a
   modulation-confirmation feature; KeyAreas fall out natively. Highest ceiling; larger build.
2. **Narrower first step: a section-scoped local-modulation pass** over the resolver output + the
   per-cadence local tonics, that re-keys sustained + cadence-confirmed spans to the local key and commits a
   local KeyArea. **Constraint:** to affect chord emission it must run **before** `analyzeChord` (which reads
   `localKeyFifths/localKeyMode` at [regionanalyzer.cpp:453–454](src/composing/analysis/region/regionanalyzer.cpp#L453))
   — i.e. a two-pass key-then-chord order, or it re-triggers analysis of re-keyed regions. (A pass that runs
   *after* chord analysis, like today's KeyArea grouping, would change the *label* but not the *chord
   emission* — a partial fix and a layering smell.)

**Zone confirmation:** keyresolver, keymodeanalyzer, regionanalyzer, sectionanalyzer, cadencekeyanchor are
**all under `src/composing/`** — the autonomous zone. The **only** off-limits touch a production detector
might want is the fermata/phrase-boundary plumbing (`src/notation` → composing) for the optional
`endsPhrase` salience; the core detector needs nothing off-limits.

---

## §5 — Task E: behavior-change blast radius `[probe]` (estimate; no build)

Modulation detection changes the **resolved key** → and the resolved key feeds chord emission directly
(`analyzeChord(tones, localKeyFifths, localKeyMode, …)`
[regionanalyzer.cpp:453–454](src/composing/analysis/region/regionanalyzer.cpp#L453), plus the key-context
refinements `refineSparseChordQualityFromKeyContext` / `applyTonicPriorToSparseChord`
[regionanalyzer.cpp:469–472](src/composing/analysis/region/regionanalyzer.cpp#L469)). So a key change is
*also* an RN-label change, a potential chord-axis change, and a snapshot change.

- **Region keys that would change.** Addressable population = the stayed-home-under-modulation set,
  **3006 regions** in the WiR-Bach default corpus (≈29.7 % of regions; the realistic captured subset
  §3.2 ≈ **1800–2500**). Across 326 chorales that is ≈ **6–8 re-keyed regions per piece** — a large,
  pervasive change, not a corner case. **This is the project's second sanctioned behavior change** (the
  byte-identity era ends here, exactly as `key_path_design.md` §9.2 anticipates).
- **RN / functional axis.** Every re-keyed region's degree label changes (the intended improvement: S1
  `key_disagree`→`rn_agree`, ≈ +19.8 pp of matched at the ceiling). Expected and measurable on
  `--key-breakdown` / `--partial-key-breakdown`.
- **Chord-axis / BIR gate (57/23/57) — MEDIUM risk, the hard-stop axis.** The chord **root** is mostly
  pitch-determined, so many re-keyings will *not* move the root → the gate may be largely robust. **But**
  the gate is a **case-identity** set and *any* BIR=false increase on Baroque **or** Jazz is a hard stop
  (CLAUDE.md), and the key *does* feed root selection on the **diatonic-sensitive subset** (sparse-chord
  refinement, tonic-prior, rcb / function-degree terms). So a non-zero number of gate cases can move. This
  must be measured on **all three presets**, DCML-adjudicated, per the gate policy — it cannot be assumed inert.
- **Pipeline snapshots (11 pinned goldens) — WILL move.** Key-dependent RN/degree output changes; each must
  be DCML-adjudicated and only verified-correct goldens refreshed (`--update-goldens`), as for any ratified
  behavior change.
- **Scope caveat of the estimate.** The 3006 figure is the **Bach WiR default** surface (the user-run
  config). The BIR gate is measured on the baroque/jazz/default corpora; the per-preset blast radius is not
  directly measured here (the detector is not built, and non-Bach uses harmonies.tsv). Non-Bach key error is
  ~2× harder (`key_path_design.md` §1.4), so the non-Bach blast radius is plausibly *larger per region* and
  must be re-measured at build time, not extrapolated.

---

## §6 — Stop-condition disclosures
- **Task A changed no metric category or number** — byte-identity of the full headline (incl. `--key-breakdown`
  + `--granularity-robust`) proven by empty `diff` (§1.2). The sub-split is additive, flag-gated reporting.
- **Did NOT build the modulation detector** — this run scopes + diagnoses only. No production source changed
  (the only repo write is this dossier + the reporting-only `compare_rn` flag).
- **No off-limits edit was needed** for the scoping. The one *future* off-limits need (fermata/phrase-boundary
  plumbing for the optional `endsPhrase` salience) is surfaced as a finding (§4.1), not actioned.
- **The stay-home diagnosis is pinned to source, not guessed** (§2.2–§2.4): three named home-pulling
  mechanisms + the absence of any local-key state, with the 9.7 %-track / 74.5 %-stay-home split measured
  `[probe][oracle]`. Where a claim is a model of behavior rather than a single line, it is labeled as such.
- **Numbers are `[probe]` on the committed `tools/corpus/default` WiR-Bach surface; roots/keys are `[oracle]`**
  (When-in-Rome rntxt via the pinned `dcml_parser`). READ-ONLY — no commit.

*Drafted by CC, 2026-06-15, base `2245aedf82`. Reporting-only `compare_rn --partial-key-breakdown` added
(byte-identity proven); probes `tools/cc_tonicization_modulation_probe.py` + `/c/tmp/cc_keyaxis_probe.py`
(throwaway, reuses the committed metric machinery verbatim). Feeds the local-modulation detector DESIGN
(Cowork-written next, ratification-gated).*
