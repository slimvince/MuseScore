# CC Report — Stage 4d-i: key-agnostic local-modulation detector, BUILT + MEASURED (byte-identical)

> **HELD — no commit.** Base HEAD `2245aedf82`. Implements the ratified
> `docs/stage4d_local_modulation_design.md` (§2 mechanism, §3 no-circularity, §5 staging). 4d-i builds the
> detector and MEASURES its candidate spans against DCML modulations; the production key path is UNTOUCHED →
> byte-identical. Re-keying production is 4d-ii (separately ratified, gated on this measurement).
> Every claim tagged `[code]` (read source), `[probe]` (ran a script), `[oracle]` (When-in-Rome DCML GT).
> Surface: WiR-Bach `tools/corpus/default_mod` (the user-run Default config), 326/353 covered, 10 109 matched.

---

## §0 — TL;DR

| | Finding | Basis |
|---|---|---|
| **Detector is key-agnostic — no circularity** | Its only inputs are the `CadenceRegionInput` stream (ticks, root pc, quality, pitch mask — physically cannot carry a key) + the notated signature. It calls `detectAuthenticCadences` + `aggregateGlobalAnchor` (both cadence-derived); it includes **no** key/KeyArea header and references **no** resolved-key type, and the `batch_analyze` call site never reads `r.key`. | §1 [code] |
| **Byte-identical** | Production key/RN output UNCHANGED. BIR **57 / 23 / 57** (Baroque/Jazz/Default), `pipeline_snapshot_tests` **11/11** zero golden diffs, composing **538** / notation **57** green, and a **0/353** byte-diff of regenerated vs committed `.ours.json`. | §2 [probe] |
| **Recall lifts ~3.4×** | The detector catches **33.4 %** of DCML's modulated regions (1347/4036), up from the production resolver's **9.7 %** — the lever is real and the establishment+confirmation mechanism works. | §3.2 [probe][oracle] |
| **Precision is POOR — it over-modulates** | Of regions we commit to a non-home local key, only **47.0 %** are a real DCML modulation to that key (span-level 52.4 %). **36.4 % are over-modulation** (DCML stays home) and **16.6 % a wrong local key**. This violates the design's precision-lean ("must NOT modulate where DCML doesn't"). | §3.1 [probe][oracle] |
| **The misfire is UPSTREAM (the cadence instrument), not the gates** | Of the over-modulation FPs: **27.5 % relative-pair** (the cadence anchor's known relative-major/minor floor — anchor is correct on only **72.4 %**), **43.3 % dominant/subdominant** (the cadence instrument's known I→IV / V→I tonicization misreads — the deferred 4c "#4 guard"), only **23.4 % genuinely foreign**. Tightening establishment length does **nothing** (FPs are sustained); even the strongest key-agnostic gate (≥2 confirming cadences) caps precision at **61.3 %** while halving recall. | §3.3 [probe][oracle] |
| **Branch: DO NOT wire 4d-ii yet** | A 47–61 %-precision detector over-modulates ~1/2 of its commits. The establishment+confirmation logic is sound (recall confirms it); the precision ceiling is set by the **cadence instrument's** ~72 % anchor accuracy + its dominant/subdominant tonicization misreads. Fix those upstream first, then re-measure. | §5 |

**One-line answer:** the detector is sound and key-agnostic and triples modulation recall (9.7 %→33.4 %), but
its precision (47–52 %) over-modulates because it inherits the committed cadence instrument's relative-pair
anchor error (28 % of FPs) and dominant/subdominant tonicization misreads (43 % of FPs) — so the next lever is
the **cadence instrument's precision**, not this detector's gates. **Held, not wired.**

---

## §1 — The detector at source + the no-circularity proof `[code]`

### 1.1 What was built
- **`src/composing/analysis/section/localmodulationdetector.{h,cpp}`** — a section/piece-scoped pass.
  `detectLocalModulations(regions, keySignatureFifths)` returns `ModulationDetectionResult { spans, anchor }`,
  where each `LocalKeySpan` carries `{startTick, endTick, tonicPc, minorMode, establishmentChords,
  confirmingCadenceCount, firstCadenceTonicTick, agreesWithAnchor}`.
- **Mechanism (design §2), all key-agnostic:**
  1. **Candidates** — every authentic cadence from `detectAuthenticCadences` exposes a candidate local tonic
     (its resolution tonic + mode). *(Per-cadence list, NOT the single `aggregateGlobalAnchor`.)*
  2. **Establishment** — each region is assigned to the local key of the **nearest** cadence whose diatonic
     collection it is consistent with (root a diatonic degree + sounding pitch content within the collection
     up to a 2-pc chromatic tolerance). This **partitions** the timeline by the cadential structure, so
     closely-related keys do not engulf one another and a spurious short cadence cannot truncate a real key's
     run. *(This nearest-cadence partition replaced a first maximal-consistent-run draft, which a relative
     key's mutual-consistency made engulf real modulations — a measured design correction.)*
  3. **Confirmation + commit** — group maximal same-key runs; commit a run only when it is SUSTAINED
     (≥ `kEstablishmentMinChords` = 5 regions) AND CONFIRMED (contains an authentic cadence of that key).
     Runs are non-overlapping by construction; the conservative bar prefers missing a borderline modulation.
- **`agreesWithAnchor`** tags each span against the **key-agnostic** global anchor (`aggregateGlobalAnchor`,
  itself cadence-derived) as the home reference — `false` ⇒ a modulation candidate. No resolved key involved.
- Thresholds (`kEstablishmentMinChords=5`, `kPitchTolerance=2`) are provisional `[empirical — Stage-5 fits]`,
  documented as such, not corpus-fit to any gate.
- **Diagnostic wiring:** `batch_analyze --dump-modulation` appends a read-only `"modulation"` block (default
  OFF), built by `writeModulationJson` from the SAME key-agnostic `CadenceRegionInput` stream as
  `--dump-cadence-anchor`. `run_bach_preset.py --dump-modulation` passes it through. 7 new unit tests
  (`localmodulationdetector_tests.cpp`) pin the commit rule, consistency test, and anchor tag from
  directly-constructed key-agnostic inputs.

### 1.2 No-circularity (design §3, the load-bearing soundness property) — confirmed at source
- The detector's only includes are `cadencekeyanchor.h` (the key-agnostic `CadenceRegionInput`) + `<algorithm>`
  / `<climits>`. It includes **no** `keyresolver`, `keymodeanalyzer`, `sectionanalyzer`/KeyArea header.
- `grep` for `KeyModeAnalysisResult|keyresolver|KeyArea|localKey|\.key` in the detector → **NONE**.
- `writeModulationJson` builds `CadenceRegionInput` from `r.chord.identity` (chord root/quality), `r.pcMask`,
  the fermata phrase boundaries, and the **notated** signature fifths (`keySigEvent(0).concertKey()`) — it
  does **NOT** read `r.key` (the resolved key). `grep` for `r.key|keyMode|KeyArea` inside it → **NONE**.
  (Contrast `writeTonicizationJson`, which legitimately reads the resolved key — Stage 6.)
- The input type `CadenceRegionInput` is physically incapable of carrying a resolved key (it has no such
  field), so the rule is enforced structurally, exactly as for the cadence detector it consumes.
- **Verdict:** the local-key hypothesis derives ONLY from the key-agnostic cadence instrument + raw region
  structure. **No stop-condition fired.**

---

## §2 — Byte-identity proof (4d-i is measurement-only) `[probe]`

| Gate | Result | Note |
|---|---|---|
| BIR Baroque | **57** | `characterise_bir_false --corpus-dir tools/corpus/baroque_4di` (353/353, manifest-complete) |
| BIR Jazz | **23** | `--corpus-dir tools/corpus/jazz_4di` |
| BIR Default | **57** | `--corpus-dir tools/corpus/default_4di` |
| `pipeline_snapshot_tests` | **11/11 PASSED**, 0 golden diffs | no `--update-goldens` needed |
| `composing_tests` | **538/538** | +7 new `LocalModulationDetector` tests |
| `notation_tests` | **57/57** | includes the P1–P4 pipeline regression |
| `.ours.json` byte-diff | **0/353** | sha256 of every regenerated (no-flag) `default_4di/*.ours.json` == committed `tools/corpus/default/*.ours.json` |

The detector is invoked **only** inside `writeModulationJson`, which runs **only** under `--dump-modulation`;
the production scoring path is untouched. The 0/353 byte-diff is the strongest proof — the regions are
byte-for-byte identical, so the chord/key axes cannot have moved. **No stop-condition fired.**

---

## §3 — The measurement (the deliverable) `[probe][oracle]`

Surface: `tools/corpus/default_mod` (Default preset, `--dump-modulation`), scored against When-in-Rome Bach
rntxt via the committed `compare_rn`/`compare_analyses`/`dcml_parser` alignment. 326/353 WiR-covered, 10 109
aligned regions. DCML modulation prevalence reproduces the scoping exactly:
**DCML local ≠ global on 4036/10109 = 39.9 %** `[oracle]`.

### 3.1 Precision — the BINDING constraint (commits of a NON-HOME local key vs DCML)
Reference home = DCML's global key (oracle). A "non-home commit" is a region in a committed span whose local
key ≠ DCML's global key (i.e. we assert a modulation).

```
non-home commit regions:          2867
  TP  (== DCML local, DCML modulates):   1347  (47.0% region precision)
  FP  over-modulation (DCML stays home):  1044  (36.4%)
  FP  wrong local key:                     476  (16.6%)
```
Span-level (414 modulation spans, majority-region adjudication): **TP 217 (52.4 %)**, over-mod 127 (30.7 %),
wrong-key 70 (16.9 %). **~half of our modulation commits are wrong** — the detector OVER-MODULATES, the
precision-lean stop-condition.

### 3.2 Recall / track-rate — the lift
```
DCML modulated regions:           4036
  caught (commit local == DCML local):  1347  (33.4% recall)
```
**33.4 % vs the production resolver's 9.7 %** — a **~3.4× lift**. The establishment+confirmation mechanism
genuinely captures real modulations (the lever the scoping promised; realistic ceiling was ~1800–2500
regions, i.e. ~45–62 % — we are at 1347, mid-band, limited by precision not the mechanism).

### 3.3 What is MISFIRING — the over-modulation characterisation (the gate-tuning finding)
Over-modulation FPs (1044, DCML stays home) by the relationship of our committed key to DCML's home key:
```
relative              287  (27.5%)   our key is the relative major/minor of DCML's home
subdominant-of-dcml   250  (23.9%)   we read the IV as a key  (I→IV cadence misread)
foreign               244  (23.4%)   genuinely unrelated over-modulation
dominant-of-dcml      203  (19.4%)   we read the V as a key   (half-cadence / V tonicization)
parallel               60  ( 5.7%)
```
Wrong-key FPs (476, DCML modulated elsewhere): foreign 40.8 %, subdominant 25.0 %, relative 13.2 %,
dominant 10.5 %, parallel 10.5 %.

**Three upstream causes, none of them this detector's establishment/confirmation logic:**
- **Relative-pair (27.5 % of over-mod):** the cadence anchor is right on only **72.4 % (236/326)** of pieces —
  the known relative-major/minor floor (Stage 4b/4c). When the anchor reads the relative, every span inherits
  the wrong mode/key.
- **Dominant + subdominant (43.3 % of over-mod):** the cadence instrument fires on I→IV (read as V/IV→IV) and
  half-cadence/V tonicizations — exactly the "dominant/subdominant tonicizations" 4c-iii flagged as its 4th,
  unbuilt failure mode (the deferred "#4 guard"). A sustained IV or V passage then passes establishment +
  confirmation and the detector commits a spurious modulation.
- **Foreign (23.4 % of over-mod):** the genuinely-actionable residual a tighter gate could trim.

### 3.4 Key-agnostic gate sweep — does tightening fix precision? (post-filter; would tighten 4d-ii)
Recomputed by post-filtering the emitted spans on the two key-agnostic knobs in the dump (both implementable
in 4d-ii). `[probe]`
```
estab>=5  cad>=1   (current)   precision 47.0%   recall 33.4%   (ov 36% / wr 17%)
estab>=6  cad>=1               precision 46.8%   recall 25.0%
estab>=8  cad>=1               precision 47.5%   recall 14.8%
estab>=5  cad>=2               precision 61.3%   recall 15.7%   (ov 27% / wr 11%)
estab>=8  cad>=2               precision 57.3%   recall  9.7%
estab>=10 cad>=2               precision 51.6%   recall  5.4%
```
- **Establishment length is NOT the precision lever** — raising it 5→8 leaves precision flat (~47 %) and only
  cuts recall. The FPs are SUSTAINED (the over-modulated IV/V passages and relative-key spans are long).
- **Confirmation strength IS the lever** — requiring **≥2 confirming cadences** lifts precision **47 %→61 %**
  (over-mod 36 %→27 %), but halves recall (33 %→16 %, back near production's 9.7 %).
- **Even the best key-agnostic gate caps precision at ~61 %** — because ~70 % of the residual FPs are the
  upstream relative-pair + dominant/subdominant cadence errors a span-gate cannot see.

### 3.5 Per-span oracle spot-checks `[oracle]`
A 30-span sample (full table in `/c/tmp/cc_4di_measure.txt`). Representative:
```
bwv10.7   m@ 3840-11520  ours=Bb  estab=9  cad=2 | dcml_glob=Gm  dcml_local=Bb  agree=100%  -> TP   (modulation to the relative major — correct key + extent)
bwv144.3  m@ 8640-15360  ours=D   estab=10 cad=3 | dcml_glob=G   dcml_local=D   agree= 90%  -> TP   (modulation to the dominant — correct)
bwv11.6   m@18720-24960  ours=Bm  estab=5  cad=2 | dcml_glob=D   dcml_local=Bm  agree= 80%  -> TP   (to the relative minor — correct)
bwv140.7  m@ 0-5760      ours=Bb  estab=5  cad=1 | dcml_glob=Eb  dcml_local=Eb  agree=  0%  -> FP   over-modulation: DCML stays in Eb (Bb = its dominant)
bwv126.6  m@12000-18720  ours=C   estab=7  cad=1 | dcml_glob=Gm  dcml_local=Bb  agree=  0%  -> FP   wrong key: DCML modulates to Bb, we read C
bwv148.6  m@ 0-9120      ours=F#m estab=10 cad=1 | dcml_glob=Fm  dcml_local=Fm  agree=  0%  -> FP   over-modulation off a wrong global key (F#m vs Fm)
```
TP spans land the right local key over the right extent; FP spans are dominant/relative over-reads or a wrong
global key — consistent with §3.3.

### 3.6 Reference baseline — the de-masking diagnostic `[probe][oracle]`
`compare_rn --wir-bach tools/corpus/default --partial-key-breakdown` (reproduced byte-for-byte):
```
matched 10109   partial 1197
  local_match    872 (72.8%)   correctly-keyed credit
  home_vs_local  237 (19.8%)   MASKED modulation error (we stayed home, DCML modulated)
key_disagree 2780  ->  S1 2093 (=global ≠local)  /  S2 687 (≠global)
```
The detector's 1347 correctly-tracked modulation regions are the population that would un-mask this 237 /
19.8 % (and the larger S1 slice) **once precision is high enough to wire** — framing the lever's ceiling
against the masking the scoping exposed.

---

## §4 — Stop-condition disclosures
- **No circularity** — the detector reads only the key-agnostic cadence instrument + raw region structure; no
  resolved-key/`KeyModeAnalysisResult`/`KeyArea` dependency (confirmed at source, §1.2). The rule held; the
  detector was buildable from key-agnostic signals alone.
- **Production byte-identity held** — BIR 57/23/57, snapshots 11/11, suites green, 0/353 byte-diff (§2). The
  detector did not leak into the key path.
- **Low precision IS reported as the finding, not wired** — the detector over-modulates (47–52 % precision);
  the over-modulation is characterised and traced upstream (§3.3). No over-modulating detector is recommended
  for wiring.
- **No off-limits edit** — all source under `src/composing/` + `tools/`. The optional fermata salience is a
  later 4d-iii refinement, untouched. The CadenceRegionInput uses the existing phrase-boundary plumbing
  already committed for the cadence diagnostic.
- Numbers are `[probe]` on `tools/corpus/default_mod` (WiR-Bach Default); keys/roots are `[oracle]` (When-in-
  Rome rntxt via the pinned `dcml_parser`). **HELD — no commit.**

---

## §5 — Branch recommendation

**Per the 4d-i decision rule: poor precision (over-modulating) ⇒ do NOT wire 4d-ii; refine — and the
refinement is UPSTREAM.**

- **The detector itself is sound and worth keeping.** Recall 33.4 % (≈3.4× production), key-agnostic,
  byte-identical, non-overlapping spans, conservative gate. The establishment+confirmation mechanism captures
  real modulations cleanly (the TP spans are correct in key and extent).
- **It must NOT be wired as-is.** 47–52 % precision over-modulates ~half its commits — wiring it into the
  production key path (4d-ii) would inject un-adjudicated key changes the BIR gate policy forbids, and would
  degrade correctness on the relative/dominant/subdominant FPs.
- **The precision ceiling is set upstream, not by this detector's gates** (§3.3, §3.4): tightening
  establishment length does nothing; ≥2-cadence confirmation reaches only 61 % at 16 % recall. ~70 % of the
  residual FPs are the **cadence instrument's** relative-pair anchor error (anchor 72.4 %) and its
  dominant/subdominant tonicization misreads (the deferred 4c "#4 guard"). **These are the levers:**
  1. **Cadence-instrument precision first** — build the dominant/subdominant discriminator (4c "#4 guard") so
     I→IV / V→I tonicizations stop registering as cadences (kills ~43 % of over-mod FPs), and improve the
     relative-pair anchor (4b/4c) (kills ~28 %). Then re-run THIS measurement — precision should rise toward
     the wireable bar with recall largely intact.
  2. **Then, if precision clears the bar, a confirmation-strengthened 4d-ii** (≥2 confirming cadences as the
     default commit gate, the §3.4 knee) — DCML-adjudicated and re-gated on all three presets.
- **Do not** spend the lever on this detector's establishment/confirmation thresholds alone — the sweep proves
  they cannot reach high precision while the cadence instrument feeds them dominant/subdominant + relative
  noise.

**Recommendation: HOLD 4d-ii. Route the next effort to the cadence instrument's precision (the 4c "#4"
dominant/subdominant guard + relative-pair anchor), then re-measure this detector before any wiring.**

---

*Drafted by CC, 2026-06-15, base `2245aedf82`. Detector + tests + `--dump-modulation` diagnostic +
`tools/cc_stage4d_i_modulation_measure.py` are HELD (no commit). Byte-identity proven (BIR 57/23/57,
snapshots 11/11, 0/353 byte-diff). Full measurement: `/c/tmp/cc_4di_measure.txt`; de-masking baseline:
`/c/tmp/cc_4di_demask_baseline.txt`.*
