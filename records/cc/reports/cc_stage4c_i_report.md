# CC Stage 4c-i — key-agnostic authentic-cadence detector: BUILT + REALIZED-DETECTION MEASURED

**Date:** 2026-06-15 · **Status:** HELD — no commit. Implements ratified
`docs/stage4c_cadence_key_design.md` §4 (4c-i). The detector is **built and measured only**; the
production key resolver/winner is **untouched** (byte-identical). Base = HEAD `cfc7eb5e39` (local 4a) +
`ef30cc70f3` (4b-i). Every number tagged `[probe]` (measured this run), `[code]` (read at source),
`[oracle]` (DCML/WiR rntxt).

**Verdict (one line):** The detector builds cleanly and is **structurally key-agnostic**, but its
**realized detection is 55.7%** correct-anchor precision on the mode-absent relative-pair floor
(`[probe]` 809/1452) — **far below the ~87% perfect-detection (hint-parity) ceiling** — and its dominant
failure mode is the detector **reproducing the very relative-major error it was built to fix**
(308/1452 ≈ 21% of the floor anchored to the relative major). The §3 *structural* decoupling holds, but
**detection reliability is the binding constraint** (exactly the §1 risk). **Branch: do NOT proceed to
4c-ii wiring; richer detection (4c-iii: cadence salience / structural-vs-interior discrimination + Picardy
handling) is required FIRST.** The §8 "far below ceiling" stop-condition fired and is reported, not forced.

---

## 1. The detector at source — key-agnostic inputs CONFIRMED `[code]`

New composing-zone files (autonomous zone), placed alongside the section analyzer, **not** reusing the
broken `detectCadences`:

- `src/composing/analysis/section/cadencekeyanchor.h` / `.cpp` — `detectAuthenticCadences()` +
  `aggregateGlobalAnchor()`.
- `src/composing/analysis/section/sectionanalyzer.*` is **untouched**; the existing circular
  `detectCadences` is left as-is.

**Key-agnosticism is structural, not merely conventional.** The detector's input type
`CadenceRegionInput` (`cadencekeyanchor.h`) carries **only** `{startTick, endTick, rootPc (−1=gap),
ChordQuality quality, uint16_t pitchClassMask}`. It **physically cannot** read `ChordFunction::degree` or
any `KeyModeAnalysisResult` — those fields are absent from the type. This closes the circularity that makes
`detectCadences` unusable for key inference (it decides PAC/PC/DC/HC from `chordResult.function.degree`,
computed *from* the resolved key — `sectionanalyzer.cpp:198`; and gates on `hasAssertiveKeyConfidence`,
silent on the floor near-ties — `:175-176`). Inputs verified key-free at source.

**Detection predicate (§2 of the design).** For consecutive regions a→b: both have a confident root
(`rootPc ≥ 0`); **a is `ChordQuality::Major`** (carries a major third = leading tone; admits V and V7,
excludes minor v); **b is Major or Minor** (a stable triad); **root(b) ≡ (root(a)−7) mod 12** (descending
fifth — a is the dominant of b); and the **leading tone `(root(a)+4) mod 12` is PRESENT in a's pitch mask**
(verified against pitch content, not implied by the quality label — `cadencekeyanchor.cpp:80-83`). Then b is
a cadential tonic; b's quality gives the mode. **Aggregation** = finality-weighted vote (cadence k, in
ascending tonicTick order, votes with weight k+1; the heaviest (tonicPc, mode) bucket wins; confidence =
its weight share). Provisional per design §6.3/§6.4.

Unit test: `src/composing/tests/cadencekeyanchor_tests.cpp` — 11 tests pinning V→I major, V→i minor
(raised-LT), V7 admission, leading-tone-must-be-present, minor-dominant/diminished-tonic/wrong-motion/gap
rejection, and the finality vote. **composing_tests 505 → 516 (+11), all green.**

---

## 2. Byte-identity proof — the production scoring path is UNTOUCHED `[probe]`

The detector is called **only** by a read-only diagnostic (`batch_analyze --dump-cadence-anchor`, default
OFF) which appends a top-level `"cadenceAnchor"` key to `.ours.json`. The resolver/winner never calls it.
Proof:

- **Scoring byte-identical across all 353 Default mode-absent scores** `[probe]`: stripping the
  `cadenceAnchor` key from every `tools/corpus/default_4ci_abs/*.ours.json` yields content **identical** to
  the investigation's reference `tools/corpus/default_4bi_abs` — **0 scoring diffs / 353 files**. The
  detector emission is purely additive.
- **BIR gate 57 / 23 / 57 byte-identical** `[probe]` (Baroque / Jazz / Default, regenerated flag-OFF through
  `characterise_bir_false.py`): TOTAL = 57 / 23 / 57, matching the committed identity sets; every visible
  case is a member (the tool prints only the top-2 delta groups — 29/18/29 of 57/23/57 — a print cap, not a
  set difference; `characterise_bir_false.py:250` `nonzero_sorted[:2]`). The OFF-path `writeJson` branch is
  character-identical to the pre-change code; the detector is never reached.
- **pipeline_snapshot_tests 11/11, zero golden diffs** (no `--update-goldens`).
- **Suites green:** composing **516**, notation **57**.

No off-limits production edit. The only touched files outside the composing zone are `tools/` (batch_analyze
diagnostic + run_bach_preset passthrough + the measurement script) — the standard measurement zone.

---

## 3. THE DELIVERABLE — realized detection fraction vs the 91% ceiling `[probe][oracle]`

Measured by `tools/cc_cadence_anchor_measure.py` (read-only; reuses `cc_floor_classify`'s
relative-pair S2 classification verbatim — `compare_rn` alignment + `_our_key_tonic`/`_dcml_key_tonic`).
Floor population identified on `default_4ci_abs` (mode-absent); the detector anchor read from the **same**
files. **My floor reproduction is exact: relative-pair S2 = 1452 regions, matching the investigation's
mode-absent table (`cc_cadence_key_investigation_dossier.md` §2) to the region.**

| metric (mode-absent relative-pair floor, region-weighted) | value |
|---|---:|
| floor regions (Δ population) | **1452** |
| floor stems | 181 |
| detector **fired** (recall) | **1452 / 1452 = 100%** |
| ... **correctly anchored** (precision = REALIZED) | **809 / 1452 = 55.7%** |
| fired-but-WRONG | 643 |
| no-fire (coverage gap) | **0** |
| perfect-detection (hint-parity) ceiling | ≈ 1259 / 1452 ≈ **86.7%** |

**Headline: realized 55.7% vs ceiling ≈87% — far below.** (Equivalently, 809 of the ~1259 hint-recoverable
regions ≈ 64% of the perfect-detection target.) Stem-weighted: 108 / 181 floor stems anchored correctly.

### 3.1 — Failure decomposition of the 643 wrong floor regions `[probe][oracle]`
| anchor ↔ DCML-global relationship | regions | share of floor | stems |
|---|---:|---:|---:|
| **relative_pair** (anchor = relative of true key) | 317 | 22% | 38 |
| ... of which **anchor = relative-MAJOR of a true MINOR** | **308** | **21%** | — |
| **other** (different key — dominant/subdominant) | 235 | 16% | 22 |
| **parallel** (Picardy: major-for-minor) | 91 | 6% | 13 |

**The dominant failure (308 regions / 21% of the floor) is the detector reproducing the exact relative-pair
error it was meant to fix.** Mechanism `[probe][theory]`: in a minor-key chorale the authentic cadences to
the **relative major** (V→III, e.g. G→C in A minor — diatonic, *no accidental*) are frequent
tonicizations, while the true V→i (E→Am, requiring the raised leading tone **G♯**) is rarer. The
finality-weighted **count** vote is swamped by the abundant diatonic III-cadences, so the anchor lands on
the relative major. The §3.1 discriminator ("the raised-LT V–i is the decisive marker") is *theoretically*
right but the **naive vote does not give it decisive weight** — it counts it as one cadence among many.
Picardy thirds (91 regions) add a parallel-major mode flip (minor chorale ending on a major tonic triad →
b.quality = Major → anchor mode = major). The "other" 235 are dominant/subdominant tonicizations misread as
the global tonic.

### 3.2 — Coverage gaps: NONE — which REFRAMES 4c-iii `[probe]`
**0 floor stems / 0 floor regions are uncovered** — every floor stem contains at least one detectable
authentic cadence. So authentic-cadence detection **over-covers** (fires everywhere); the deficit is **not**
missing cadence modalities (plagal/half/deceptive) but **discrimination/aggregation** — which cadence is the
*structural* tonic cadence vs an interior tonicization. This **inverts design §6.1's hypothesis** that
authentic-only might under-cover: 4c-iii should add cadence **salience/finality** (fermata-gated,
structural-vs-interior, raised-LT weighting), **not** more cadence types.

---

## 4. Per-target + bwv64.2 GT resolution `[probe][oracle]`

| stem | DCML global `[oracle WiR]` | detector anchor | conf | ncad | floor | reading |
|---|---|---|---:|---:|---:|---|
| **bwv365** | a minor | **C major** | 0.93 | 5 | 4 | **MISS** → relative major. 4 of 5 cadences are V→III (G→C); only 1 to A minor (early). Final structural A-minor cadence not isolated. |
| **bwv33.6** | a minor | **C major** | 0.33 | 5 | 14 | **MISS** → relative major (same swamping). Recovered mode-absent in 4b-i; cadence detector does **not** secure it. |
| **bwv64.2** | **C major** | G major | 0.57 | 6 | 1 | **MISS** → dominant. GT resolved (below); detector reads the dominant G. |
| **bwv83.5** | d minor | **d minor** | 0.53 | 9 | 0 | **CORRECT**, and floor=0 (not a relative-pair case) — the detector does **not** spuriously claim it. ✓ (the one clean per-target.) |

**bwv64.2 GT discrepancy — RESOLVED `[oracle]`.** Read directly from the WiR rntxt source
(`.../Chorales/160/analysis.txt`): `global_key = 'C'` → **C major**. This **confirms the investigation's
correction** (`cc_cadence_key_investigation_dossier.md` §3.4) and **refutes 4b-ii §3's "G major"** label —
4b-ii had the DCML key wrong. bwv64.2 is a **relative-pair** case (A minor is the relative minor of C major)
with only 1 mode-absent S2 region. The detector itself does **not** recover it (reads dominant G major), so
it is not a 4c-i win, but the GT question is settled: **C major.**

---

## 5. Decoupling preview — structurally real, but reliability is binding `[probe]`

On the **249 mode-present clean stems** (zero S2 — the key the 1.0 hint already gets right) that carry a
detected anchor: the detector **agrees** with the correct key on **164 (66%)** and **contradicts on 85
(34%)**. The contradictions are the same systematic relative-major / Picardy-parallel misreads
(bwv256 a→A, bwv365-class a→C, bwv26.6 a→A, …).

- **Positive (the §3 decoupling claim holds):** *when the anchor is correct it agrees with the hint* — there
  is no population where a *correct* cadence anchor must fight a *correct* hint. The decoupling is real and
  structural (scope, not measurement), exactly as the investigation argued.
- **Decisive caveat (the §1 risk, now measured):** a **34% contradiction rate on already-correct stems** is
  the binding constraint. Wiring this anchor at section/piece scope (4c-ii) would, on ~1/3 of clean stems,
  **override the correct hint mode-present** — precisely the 4c-ii ratification hard-stop (§8: "4c-ii
  regressing mode-present — the decoupling failed empirically"). The failure here is **detection reliability**,
  not the §4 coupling; but it is sufficient to block wiring as-is.

---

## 6. Branch recommendation — 4c-iii (richer detection) BEFORE 4c-ii

Per the instruction's branch rule and design §8:

- realized fraction worthwhile ⇒ 4c-ii — **NOT met** (55.7% ≪ 87% ceiling; 34% contradiction on clean stems).
- marginal ⇒ 4c-iii richer detection first — **THIS.**
- far below ceiling ⇒ A-vs-B key-axis finding — partially: the residual after better detection sizes B.

**Recommendation: do NOT wire (4c-ii is gated on this number and the number fails the bar). Build 4c-iii
detection-reliability work first**, targeting the three measured failure modes, in priority order:
1. **Structural-vs-interior discrimination (308 regions, the biggest lever):** vote only / weight heavily the
   **phrase-final** cadences (chorale fermatas are natural markers), so abundant interior V→III tonicizations
   stop swamping the rarer structural V→i. The aggregation, not the per-pair predicate, is the weak link.
2. **Raised-LT salience (relative discriminator):** weight a V→i carrying the minor's raised leading tone
   above a diatonic V→III, rather than counting them equally — operationalizing §3.1.
3. **Picardy handling (91 regions):** a final major tonic triad in an otherwise-minor cadential context
   should not flip the mode to parallel major.
4. **Dominant/subdominant guard (235 regions):** suppress anchoring to a key whose own "tonic" is itself the
   dominant/subdominant of a stronger, later cadence (bwv64.2 G-for-C).

Only after 4c-iii lifts realized precision toward the ceiling (and the clean-stem contradiction rate toward
~0) should 4c-ii wiring be attempted. The §3 structural decoupling means a *reliable* detector would be
safe to wire; the work is making it reliable. **B (learned key emission) is not yet implicated** — the
literature-backed hand-built signal is real (the predicate fires with 100% coverage and 0% spurious on the
non-relative residual bwv83.5); it is the *aggregation* that is under-built.

---

## 7. Stop-conditions — disposition
- ✅ **Detector needing `function.degree` / resolved key** — did NOT occur; key-agnosticism is *structural*
  (the input type cannot carry key state). §1.
- ✅ **Any production behavior change (gate/snapshot/suite movement)** — none. 0/353 scoring diff, 57/23/57
  byte-identical, snapshots 11/11, suites 516/57. §2.
- ✅ **Realized detection far below the 91% ceiling** — **this fired** (55.7% vs ≈87%). Reported as the
  detection-reliability finding; did **not** force the wiring. §3, §6.
- ✅ **Temptation to wire the anchor "to see if it helps"** — resisted; the diagnostic is read-only and the
  resolver is untouched. 4c-ii remains gated on this number, which fails the bar.

## 8. Working-tree artifacts (HELD — no commit)
- `src/composing/analysis/section/cadencekeyanchor.{h,cpp}` (the detector) + CMake entry.
- `src/composing/tests/cadencekeyanchor_tests.cpp` (11 tests) + CMake entry.
- `tools/batch_analyze.cpp` (`--dump-cadence-anchor`, read-only, default OFF).
- `tools/run_bach_preset.py` (`--dump-cadence-anchor` passthrough).
- `tools/cc_cadence_anchor_measure.py` (read-only realized-detection measurement).
- `tools/corpus/default_4ci/`, `tools/corpus/default_4ci_abs/` (measurement corpora — anchor-augmented,
  scoring byte-identical to `default_4bi{,_abs}`; keep or drop at Cowork's discretion).
- This report. No `docs/scoring_model.md` sync needed (no chord scoring term changed). HEAD unchanged.
