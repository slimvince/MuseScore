# J-key-ii — Note-based home-key inference (demote the signature pin): diagnostic + re-measure

> **HELD — uncommitted, diagnostic-only, production byte-identical.** Second step of
> `docs/scoped_joint_design.md` §6 (key-axis), implementing the user-ratified J-key-ii direction
> (2026-06-15): replace the home-fifths HARD backbone with **note-based home-key inference**
> (signature → soft prior), then re-measure — BEFORE any wiring. No production resolve-path edit;
> no commit. Cowork verifies at source; user ratifies J-key-iii (the wiring) separately.
>
> **Date:** 2026-06-15. **HEAD:** `2245aedf82` (unchanged). **Scope of numbers:** WiR-Bach
> covered stems (326/353 aligned); non-Bach unmeasured. Every key is `[oracle]` via the committed
> `dcml_parser`/`compare_rn` machinery; weights provisional `[empirical — Stage-5 fits]`.

---

## 0. Headline — the demotion took STRUCTURALLY, but the win MATERIALLY SHRANK → HOLD J-key-iii

1. **The hard signature pin is GONE; the true key is now mostly representable.** The home key is
   note-inferred (collection-fit + analyzeKeyMode aggregate ∪ the signature relative pair), the
   signature a soft prior. The §6a structural-exclusion rate (DCML key NOT representable at
   key-stable regions) drops **17.0 % → 4.3 % (Default), 17.0 % → 4.3 % (Baroque), 17.2 % → 4.2 %
   (Jazz)** — a ~75 % reduction. After the demotion the **key axis carries NO hard constraint at
   all** (lattice membership is never a veto; every soft term is additive — confirmed structurally,
   per design §3). The lattice stays **scoped** (mean ~3.5 states, max 7; the §7 balloon stop did
   NOT fire).
2. **But it did NOT drop to ~0, and partial-signature recovery is weak (~36 %).** 4.3 % of
   key-stable regions still exclude the DCML key (collection top-2 + analyzeKeyMode top-2 miss it).
   Even where representable, the soft rank reads the true key only **35.1 / 36.6 / 35.8 %** of the
   time on the 56-stem signature-mismatch set. **`bwv254` partially recovers** (D minor in the
   opening section, A minor later); **`bwv265` does NOT** (stays A minor — the 0-flat relative
   minor — because the declared-mode hint 1.0 + signature prior on A minor out-vote D minor's
   collection+anchor evidence).
3. **⛔ The SOFT WIN materially SHRANK — the §7 "win shrinks → STOP" condition FIRED.** vs the
   J-key-i soft baseline the demotion **loses −1.4 / −1.0 / −1.0 pp key-accuracy** and **adds +195 /
   +132 / +118 genuine key errors (S2)**. On **Default/Baroque the demoted decision is now WORSE
   than production on genuine-error count** (S2 +55 / +36 vs prod), though key-accuracy stays above
   production (+2.41 / +2.51 pp) because it also de-masks more modulations. **The Jazz win survives
   largely intact** (+11.27 pp vs prod, −1588 S2). **Cowork's strategic flag is confirmed: the
   signature backbone was LOAD-BEARING** — it was silently suppressing spurious note-inferred
   candidates on correctly-signed pieces, and demoting it lets those candidates mis-pull the
   Viterbi.
4. **Production is byte-identical** — 353/353 `.ours.json` per preset, **0 production-field diffs**;
   **BIR 57 / 23 / 57** (== gate, measured on the J-key-ii corpora); suites green (composing
   **546**, notation **57**, snapshots **11/11** + 1 skip, **goldens unchanged**). The scoped joint
   remains **inert** on the key axis (joint−soft **+0.07 / +0.08 / +0.01 pp**).

**Verdict on the J-key-iii (wiring) gate:** **DO NOT proceed to wire.** The §6 gate — *proceed only
if safety ~0 AND the win is preserved-or-improved* — fails on BOTH counts (safety partial; win
shrank). The global flat-soften is the **wrong lever**. Recommend a **targeted partial-signature
override** (a note-triggered detector that swaps the home pair only when note evidence confidently
contradicts the signature), leaving the load-bearing signature backbone intact everywhere else —
a J-key-ii-redux to ratify before any J-key-iii. (§6 / §9.)

---

## 1. What changed (J-key-ii §3) — the demotion

Diagnostic-only; all work in `src/composing/` + `tools/`. **Zero** `src/notation` / `src/engraving`
edits. The producer stays parallel to production (`--dump-joint-key` only); production byte-identical.

- **`jointkeydecision.{h,cpp}`** — the home-pair construction (J-key-i `jointkeydecision.cpp:187-205`)
  is replaced:
  - The notated-signature relative pair is **no longer the forced home lattice** — it seeds two
    candidate states and feeds a new **soft signature prior** (`signaturePrior = 0.30`
    `[empirical]`) + the existing declared-mode hint. No hard pin.
  - **Note-inferred home candidates** are aggregated piece-wide, key-agnostic: (1) collection-fit
    (note-count-weighted in-collection mass of each of 24 keys, top-2), (2) the analyzeKeyMode local
    candidates (Σ confidence, top-2). Lattice = signature pair ∪ note candidates ∪ committed
    modulation spans.
  - **Design deviation (documented):** the cadence anchor (`aggregateGlobalAnchor`) is kept as a
    **soft emission term only**, NOT injected as a standalone candidate state, deviating from the
    instruction's literal "∪ the cadence-anchor key". *Rationale (measured):* injecting the raw
    anchor key regressed a clean **C-major run to its subdominant F major** — the committed anchor
    reads the diatonic `C→F` as a V→I cadence to F (its known V→IV/subdominant over-detection,
    J-key-i §10.5). As a soft bonus the anchor reinforces the collection-surfaced home and breaks
    the relative-pair mode tie without injecting a phantom subdominant. (Caught by the
    `MajorRunResolvesToHomeMajor` unit test mid-build; fix verified.)
  - Everything else unchanged: cadence anchor / modulation / bass-is-root / declared-mode all stay
    SOFT and additive; the global key-path Viterbi + transition penalty unchanged; soft-vs-joint
    attribution toggle preserved.
- **`tools/batch_analyze.cpp` `--dump-joint-key`** — additively emits the full `latticeStates` set
  (piece-global) so the safety instrument can test DCML-key representability.
- **`tools/cc_j_key_ii_safety.py`** (new) — the two new checks: lattice-exclusion safety +
  partial-signature recovery. `cc_j_key_i_measure.py` is RE-RUN unchanged for the key-axis tables.
- **`jointkeydecision_tests.cpp`** — +1 test (`PartialSignatureRecoversNoteKey`: a D-minor run
  notated 0 flats now resolves to D minor; pins the demotion). 8/8 JointKeyDecision pass.

---

## 2. §5 — Byte-identity + suite gates (the diagnostic must not perturb production) — ALL PASS

| Gate | Result |
|---|---|
| `.ours.json` byte-identity (jointKey stripped vs committed baseline) | **353/353 each preset, 0 production-field diffs** |
| BIR gate (measured on the J-key-ii corpora, manifest-validated) | **Baroque 57 / Jazz 23 / Default 57** (== gate) |
| composing_tests | **546 / 546** (545 + new `PartialSignatureRecoversNoteKey`) |
| notation_tests | **57 / 57** |
| pipeline_snapshot_tests | **11 / 11** (+1 expected skip), **goldens unchanged** (no `--update-goldens`) |

The `jointKey` block (incl. the new `latticeStates`) is purely additive; the production writer is
untouched ⇒ byte-identity is structural and empirically confirmed.

---

## 3. §4.1 — KEY AXIS: soft config vs production AND vs the J-key-i soft baseline

`correct` = config (tonic,mode) == DCML local key; `S1` = == DCML global but DCML modulated
(stayed-home / masked modulation); `S2` = genuine error (≠ both). Scored = correct+S1+S2.

### Soft config — the lever

| preset | config | correct | S1 | S2 | key-acc | Δacc vs prod | Δacc vs J-key-i | ΔS2 vs J-key-i |
|---|---|---|---|---|---|---|---|---|
| Default | prod | 5556 | 3021 | 1532 | 55.0 % | — | — | — |
| Default | J-key-i soft | 5940 | 2777 | 1392 | 58.8 % | +3.80 | — | — |
| Default | **J-key-ii soft** | 5800 | 2722 | **1587** | **57.4 %** | **+2.41** | **−1.40** | **+195** |
| Baroque | prod | 5566 | 3035 | 1518 | 55.0 % | — | — | — |
| Baroque | J-key-i soft | 5920 | 2777 | 1422 | 58.5 % | +3.50 | — | — |
| Baroque | **J-key-ii soft** | 5820 | 2745 | **1554** | **57.5 %** | **+2.51** | **−1.04** | **+132** |
| Jazz | prod | 4544 | 2104 | 3140 | 46.4 % | — | — | — |
| Jazz | J-key-i soft | 5742 | 2612 | 1434 | 58.7 % | +12.24 | — | — |
| Jazz | **J-key-ii soft** | 5647 | 2589 | **1552** | **57.7 %** | **+11.27** | **−0.97** | **+118** |

**Reading.** J-key-ii still beats production on key-accuracy everywhere, but **underperforms the
J-key-i soft decision by ~1 pp on every preset and adds 118–195 genuine errors (S2)**. The
mechanism is visible in the S1 column: J-key-ii converts ~140–300 J-key-i `S1` regions, but it
splits them into BOTH `correct` (de-masking — good) AND `S2` (new genuine errors — the cost). On
Default/Baroque the net genuine-error count is now slightly **worse than production** (S2 1587/1554
vs 1532/1518). **The broader note-inferred lattice introduces wrong candidates on correctly-signed
pieces** that the hard signature pin previously made unrepresentable; `signaturePrior = 0.30` is not
strong enough to hold the Viterbi home.

**Scoped-joint increment (joint − soft): +0.07 / +0.08 / +0.01 pp** — still inert (confirms J-key-i
conclusion #2: the chord×key coupling does not move the key axis; reserve it for J-chord).

### Relative-pair recovery + modulation de-masking (soft)

| metric | preset | prod | J-key-i soft | J-key-ii soft |
|---|---|---|---|---|
| relative-pair mode-correct | Default | 78.2 % | 81.7 % | 81.5 % |
| | Baroque | 78.6 % | 81.9 % | 81.6 % |
| | Jazz | 80.2 % | 81.5 % | 81.5 % |
| modulation de-masking (local==DCML) | Default | 10.2 % | 16.9 % | 15.9 % |
| | Baroque | 9.8 % | 17.2 % | 16.0 % |
| | Jazz | 17.2 % | 18.8 % | 17.7 % |

Both secondary wins **also shrank slightly** under the demotion (relative-pair −0.2…−0.3 pp;
modulation −1.0…−1.2 pp) — same broader-lattice mechanism.

---

## 4. §4.3 — HARD-CONSTRAINT SAFETY (the fix) + partial-signature recovery

### (1) Safety — the demotion took STRUCTURALLY, partially empirically

| preset | NEW lattice-EXCLUSION (DCML key not representable) | OLD signature-mismatch (informational) | lattice size (mean / max) |
|---|---|---|---|
| Default | **262 / 6073 = 4.3 %** (J-key-i ~17 %) | 1032 / 6073 = 17.0 % | 3.68 / 7 |
| Baroque | **262 / 6073 = 4.3 %** | 1034 / 6073 = 17.0 % | 3.51 / 7 |
| Jazz | **244 / 5873 = 4.2 %** | 1012 / 5873 = 17.2 % | 3.65 / 7 |

- **There is NO hard key constraint** after the demotion (lattice membership is never a veto; every
  soft term is additive) — the design §3 "key axis has no hard constraints" property, confirmed.
- The **structural-exclusion rate** (the §6a successor: was the true key even representable) dropped
  **17 % → ~4.3 %**. The residual 4.3 % is candidate-generation under-coverage: collection top-2 +
  analyzeKeyMode top-2 do not surface the DCML key for those regions. **Not ~0 — so per §7 the
  demotion "took" structurally but the candidate set is too narrow.**
- The OLD signature-mismatch rate is **unchanged at ~17 %** (it is a fixed property of the notated
  signature) — now harmless because it is SOFT, not a pin.

### (2) Partial-signature recovery — weak (~36 %)

| preset | soft reads DCML (region) | joint (region) | soft recovers stem (majority) | joint (majority) |
|---|---|---|---|---|
| Default | 362 / 1032 = 35.1 % | 35.7 % | 21 / 56 = 37.5 % | 39.3 % |
| Baroque | 378 / 1034 = 36.6 % | 37.0 % | 22 / 56 = 39.3 % | 41.1 % |
| Jazz | 362 / 1012 = 35.8 % | 35.8 % | 20 / 56 = 35.7 % | 35.7 % |

**Stress cases (Default):**
- **`bwv254` (DCML D minor, notated 0 flats):** PARTIAL — D minor in the opening section
  (ticks 9600–12960, soft = D minor ✓), **A minor** in a later section (18240–20640, soft = A
  minor ✗). D minor `inLattice=True` throughout (representable, but the soft rank flips).
- **`bwv265` (DCML D minor, notated 0 flats):** NOT recovered — reads **A minor** at every
  mismatch region, although D minor `inLattice=True`. The declared-mode hint (1.0) on the
  signature-relative **A minor** + the signature prior (0.30) out-vote D minor's collection + cadence
  anchor.

The 56-stem signature-mismatch set is reproduced exactly (== the J-key-i ~56-stem finding).

---

## 5. Why it shrank — the load-bearing tension (the finding)

A **single global signature prior cannot separate two opposite cases:**

- **Defend a CORRECT signature** (the bulk, ~83 % of key-stable regions): the prior must be strong
  enough to suppress the spurious note-inferred candidates the broader lattice now admits. At
  `signaturePrior = 0.30` it is too weak — **−140 `correct`, +195 `S2` on Default** (the win shrinks).
- **Override a partial/Dorian LIE** (the 56-stem set): the prior + the declared-mode hint (1.0, on
  the signature-relative pair) must be *weak* enough that D-minor note evidence wins. At
  `signaturePrior = 0.30` + `declaredHint = 1.0` it is too strong — **recovery only ~36 %**
  (`bwv265` never escapes A minor).

Raising the prior would help the bulk (recover the win) but further block recovery; lowering it
would help recovery but worsen the win. **One uniform weight is on the wrong side of both.** The
J-key-i hard pin avoided this by being *infinitely* strong (full win-protection) at the cost of
*zero* recovery (the §6a unsafety). The demotion trades to the opposite corner partially. The
correct lever is not a global scalar but a **per-piece decision**: trust the signature unless the
note evidence *confidently* contradicts it.

A weight sweep was deliberately NOT run (it requires a rebuild + 3×353 regen per point, and §7
directs *surface, do not tune past a shrunk win*). The tension above is structural, not a
calibration artifact; the recommendation (§6) follows from it directly.

---

## 6. §6 — Deliver: the J-key-iii (wiring) gate verdict

**The §6 gate — proceed to wire only if safety ~0 AND the win is preserved-or-improved — FAILS:**
safety is partial (17 %→4.3 %, not ~0; recovery ~36 %) and **the win materially shrank** (−1 pp,
+118…+195 S2; worse than production on Default/Baroque genuine-error count). **Recommendation: DO
NOT proceed to J-key-iii on this formulation.** Surface the trade-off for a Cowork/user decision.

**Recommended rebalance (a J-key-ii-redux to ratify before J-key-iii):** replace the *global flat
soften* with a **targeted, confidence-gated partial-signature override** —
1. Keep J-key-i's strong signature anchor as the home backbone (protects the bulk win — it was
   load-bearing).
2. Add a **note-triggered partial-signature detector**: when the key-agnostic cadence anchor (and/or
   collection-fit) confidently names a tonic whose signature ≠ the notated fifths (the Dorian-lie
   signal), OVERRIDE the home pair to the note-inferred key *for that piece only*. This is the
   deferred OQ3 detector the instruction said J-key-ii subsumes — the measurement shows a **scoped
   override** is the right shape, not a global softening.
3. Re-measure: the override should fix the ~56 stems (safety → ~0, recovery ↑) WITHOUT touching the
   correctly-signed bulk (win preserved-or-improved).

Also (independent, from §3/§4): the declared-mode hint is tied to the *signature-relative* pair; on
a Dorian stem that pulls toward the wrong relative minor. A note-based home would re-anchor the
declared-mode mode onto the inferred tonic — folds naturally into the targeted detector.

---

## 7. §7 — Stop conditions: status

| Stop condition | Fired? |
|---|---|
| Production resolve-path / `src/notation` / `src/engraving` edit needed | **No** |
| Home-fifths safety rate does NOT drop to ~0 | **PARTIAL — 17 %→4.3 % (structural pin gone; candidate set under-covers). Reported.** |
| **Soft win collapses / materially shrinks (anchor was load-bearing)** | **YES — −1 pp / +118…+195 S2 across presets; worse than prod on Default/Baroque S2. Surfaced (§3, §5, §6). HOLD on J-key-iii.** |
| Production output / BIR gate / snapshot golden moves | No (byte-identical; 57/23/57; 11/11 unchanged) |
| Home-candidate set balloons toward a full lattice | No (mean ~3.5, max 7 — scoped) |
| Any attempt to wire into production | No (diagnostic only) |
| Uncertain key decision | Adjudicated vs DCML; the 56-stem set bucketed; stress cases dumped |

The build is complete and clean. Two stops fired (safety partial; **win shrank**) → this is a **HOLD
on J-key-iii** with a concrete rebalance recommendation, not a defect in the J-key-ii build.

---

## 8. Notes
- **Sandbox-bash noise:** `/tmp` (MSYS) vs Windows-`python` `/tmp` (= `C:\tmp`) differ; smoke
  artifacts written to `C:/tmp/`. Corpus + measurement ran clean. Host-side Read/Grep authoritative.
- **Gitignored / HELD:** this report (`/cc_*.md`) and the `tools/corpus/*_jkii/` measurement corpora
  (`/tools/corpus/`) are gitignored — HELD by construction. The J-key-i `_jki` dumps (HEAD-unchanged)
  were re-measured as the comparison baseline and reproduce `cc_j_key_i_report.md` exactly.

### Files (HELD, uncommitted)
- `src/composing/analysis/section/jointkeydecision.{h,cpp}` (modified — demotion)
- `src/composing/tests/jointkeydecision_tests.cpp` (+1 test)
- `tools/batch_analyze.cpp` (`latticeStates` additive dump)
- `tools/cc_j_key_ii_safety.py` (new instrument)

**HELD — uncommitted. Cowork verifies at source; user ratifies J-key-iii (or the J-key-ii-redux
targeted-detector rebalance) separately.**
