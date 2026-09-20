# J-key-iii — STEP 2: WIRE the constrained-joint KEY decision into production (KEY-ONLY)

> **HELD — uncommitted. The FIRST intentional production behavior change on the key axis
> (the constrained-joint architecture landing), flag-gated DEFAULT OFF so the committed
> baseline is byte-identical until ratified.** Built from `cc_j_key_iii_integration_dossier.md`.
> Cowork verifies at source; the user ratifies the commit. **No commit made.**
>
> **Date:** 2026-06-16. **HEAD:** `2245aedf82` (unchanged — no commit). **Scope of
> numbers:** WiR-Bach covered stems (326/353 aligned); non-Bach unmeasured (stated).
> Every key is `[oracle]` via the committed `dcml_parser`/`compare_rn` machinery.

---

## 0. Headline

1. **§0 PRECONDITION MET — J-key-i restored byte-identically.** The on-disk producer was
   the superseded J-key-ii global-soften; it was reverted to the J-key-i strong-signature-
   backbone (drop the note-inferred candidate lattice + top-K aggregation, drop
   `signaturePrior`, restore the forced signature home pair as the only non-span states;
   remove the J-key-ii demotion unit test). **Proof:** the restored producer's per-region
   decisions are **byte-identical to the original `tools/corpus/*_jki` dumps — 0 soft / 0
   joint mismatches across all 3 presets (11255 / 11268 / 10911 regions)** and reproduce the
   ratified profile to the unit (key-acc **+3.80 / +3.50 / +12.24 pp**; S2 **−140 / −96 /
   −1706**; home-fifths safety 17.0 / 17.0 / 17.2 % = the 56-stem partial-signature ceiling).
   composing_tests **545** (7 `JointKeyDecision` tests). The §0 STOP did not fire.

2. **§5 KEY-AXIS INVARIANT HOLDS EXACTLY — the win transfers.** The wired per-region
   resolved key is **byte-identical to the measured `jointKey` SOFT decision** — **0
   mismatches across all 33,434 scored regions** (Default 11255 / Baroque 11268 / Jazz
   10911), 0 non-Ionian/Aeolian leaks. So the realized production key-axis delta **IS** the
   J-key-i win: **+3.80 / +3.50 / +12.24 pp; S2 −140 / −96 / −1706**.

3. **⛔→✓ The chord re-emission was found UNFAITHFUL and DROPPED (user-ratified KEY-ONLY).**
   The dossier §3 step-3 chord re-emission (re-run `analyzeChord` under the joint key)
   cannot reproduce the production chord: the production chord is emitted **mid-pipeline**
   (Pass 1/2/2b), while a region's FINAL tones + context are **post-merge** (Pass 3
   `coalesceShortSameRootRuns`/`absorbShortRegions` merge tones without re-chording).
   Measured: with the key held **identical**, **520 / 8914 same-key regions still re-emitted
   a different chord — 496 of them ROOT changes on full 4–6-note chords** (not sparse,
   not the predecessor-confidence channel — verified by storing the full `temporalCtx`,
   which moved it only 532→520). So the first-pass BIR increase (+12/+6/+15) was **~6%
   re-emission artifact, not a genuine key effect.** Per the §6/§7 hard-stop discipline this
   was surfaced; **the user chose KEY-ONLY wiring** (override the key, leave the chord = the
   production chord). The chord-axis side-effect (the dossier's diatonic-root re-rank) is
   **DEFERRED** to a faithful mechanism.

4. **KEY-ONLY result is CLEAN.** BIR gate **57 / 23 / 57 — byte-identical case-identity sets
   to baseline (0 added / 0 removed on every preset)** → the CLAUDE.md/§7 BIR hard-stop does
   **NOT** fire. **Chord-winner flips: ZERO** (the chord is untouched). Flag-OFF baseline
   byte-identical: composing **545** / notation **57** / snapshots **11/11**.

**Recommendation (§8): the KEY-ONLY J-key-iii wiring is sound and realizes the ratified key
win with zero chord/BIR regression. HELD for ratification.** The remaining commit-gate is the
snapshot-golden refresh (§6.4) — which needs per-score DCML adjudication including the
non-Bach snapshot scores that lie OUTSIDE the WiR-Bach measurement scope — plus the user's
acceptance of the mode-collapse representational consequence (§6.5) and the deferred
chord-axis re-emission (§0.3).

---

## 1. What was wired (all in `src/composing/` + `tools/`; ZERO `src/notation`/`src/engraving` edits)

- **`jointkeydecision.{h,cpp}`** — (a) restored to the J-key-i strong-signature-backbone
  (§0.1); (b) added the wiring flag `setJointKeyWiringEnabled()` / `jointKeyWiringEnabled()`
  (default OFF; the default is seeded from the `MUSE_JOINT_KEY_WIRING` env var at static-init
  so a test binary can exercise the wired bridge path without a `src/notation` test edit).
- **`keymodeanalyzer.{h,cpp}`** — `keySignatureFifthsForKey(tonicPc, isMajor, refFifths)`:
  maps the binary (tonic, major/minor) joint decision to its notated-signature fifths,
  reusing the file-local `resolveToFifths` (enharmonic spelling nearest the reference) — so a
  home (signature-pair) key pins back to the notated fifths automatically.
- **`regionanalyzer.cpp`** — `applyJointKeyWiring(...)` at the END of `analyzeRegions`
  (gated on `jointKeyWiringEnabled()`): re-resolves `keyRanked` per FINAL region (threading
  `prevKey`, **IDENTICAL** to the `batch_analyze --dump-joint-key` construction → the soft
  decision reproduces the diagnostic byte-for-byte, §5), builds `JointKeyRegionInput`, calls
  `decideJointKey` ONCE (frozen — no fixpoint, dossier §4), and maps the SOFT per-region
  decision → `KeyModeAnalysisResult` (§2). **KEY-ONLY: the chord is left as production R0.**
  `backfillNextRootPc` is re-run afterward so V/x tonicization labels reflect the new key.
  (Notation-derived inputs — notated signature fifths, declared `<mode>` ordinal, fermata
  phrase boundaries — are computed in-zone exactly as the diagnostic computes them.)
- **`sectionanalyzer.cpp`** — Layer B (1-region-island key stabilization,
  `stabilizeHarmonicRegionsForDisplay`) is made **inert when the flag is ON** so the joint
  Viterbi key path is authoritative and survives into stage-5 degree re-derivation (dossier
  §5 "override after Layer B"). Default OFF ⇒ unchanged.
- **`tools/batch_analyze.cpp`** — `--joint-key-wiring` flag (sets the process flag before
  `analyzeScore`). **`tools/run_bach_preset.py`** — `--joint-key-wiring` pass-through.
- **New read-only instruments:** `tools/cc_j_key_iii_decision_diff.py` (restored == original
  J-key-i, §0), `cc_j_key_iii_invariant_check.py` (§5), `cc_j_key_iii_mode_collapse.py` (§6.5).

### §2 representation mapping (dossier §3)
- **`tonicPc`/`isMajor`** ← the SOFT (config-A) joint decision (the §5 invariant uses soft).
- **`KeySigMode`** = `isMajor ? Ionian : Aeolian` (the binary collapse — measured §6.5; per
  instruction §2 "Do NOT invent a mode").
- **`keySignatureFifths`** = `keySignatureFifthsForKey(...)` (home pair → notated fifths,
  confirmed automatic).
- **`normalizedConfidence`** = option (b): the matching pre-joint local candidate's
  `normalizedConfidence`; documented constant **0.5** fallback (conservative, sub-threshold,
  so a modulation-span state the Viterbi committed does NOT spuriously open a KeyArea /
  fire a cadence) when the joint pick is not among the region's local candidates.

---

## 2. §0 — restore-and-reproduce (the precondition gate)

| Check | Result |
|---|---|
| Restored decisions == original `_jki` dumps (soft + joint) | **0 / 0 mismatches**, Default 11255 / Baroque 11268 / Jazz 10911 regions |
| Reproduces J-key-i key-acc vs prod | **+3.80 / +3.50 / +12.24 pp** ✓ |
| Reproduces J-key-i S2 reduction | **−140 / −96 / −1706** ✓ |
| Reproduces home-fifths ceiling (56 partial-sig stems) | **17.0 / 17.0 / 17.2 %** ✓ |
| composing_tests | **545** (7 JointKeyDecision; the J-key-ii demotion test removed) |

The restore is a faithful re-derivation of J-key-i (not a guess) — the byte-identity proof is
the gate.

---

## 3. §5 — the KEY-AXIS INVARIANT (the win transfers exactly)

Wired production key (a `--joint-key-wiring` regen) vs the measured `jointKey.soft*` (a
`--dump-joint-key` regen of the same preset), aligned per region by start-tick:

| preset | regions compared | KEY mismatches | non-maj/min leaks |
|---|---|---|---|
| Default | 11255 | **0** | 0 |
| Baroque | 11268 | **0** | 0 |
| Jazz | 10911 | **0** | 0 |

⇒ the wired resolved key is the soft decision exactly ⇒ the **realized key-axis delta is the
J-key-i win** (+3.80/+3.50/+12.24 pp; S2 −140/−96/−1706). Confirmed transitively: wired ==
soft (here) and soft == the §3 J-key-i measurement.

---

## 4. §6 — production delta on BOTH axes (KEY-ONLY)

| Output | Moves? | Result |
|---|---|---|
| **Per-region resolved key** (`r.key`) | **yes** | = soft decision (§5). ~2319/2354/5502 regions' key-NAME changes (incl. mode-collapse renames); (tonicPc,isMajor) changes = the measured win |
| **Key-axis S2** (genuine key error) | **yes — the win** | **−140 / −96 / −1706** vs production |
| **Chord winner** (`rootPc`/`quality`) | **NO** | **0 flips** — chord left as production R0 (key-only) |
| **BIR gate** (57 / 23 / 57) | **NO** | **57 / 23 / 57 — byte-identical case-identity sets, 0 added / 0 removed all 3 presets.** Hard-stop does NOT fire |
| **Snapshot goldens** (P1–P4) | **yes — all 11** | §6.4 — KEY/RN re-contextualization (first divergences are `"key"` fields); NOT refreshed (HELD) |
| **Mode rendering** | **yes** | §6.5 — binary collapse renames 212 / 63 / 4120 regions' modal keys |

### §6.4 — snapshots
Run `MUSE_JOINT_KEY_WIRING=1 pipeline_snapshot_tests` → **all 11 goldens move**; the first
divergence in each is a `"key"` field (e.g. `bach_chorale_001` `"G"`→`"E"`), i.e. the joint
key re-contextualizing RN/KeyArea — **not a chord change** (the chord identity is byte-identical
in the batch/BIR path; the bridge path additionally re-derives RN degree + may re-refine
sparse-chord quality under the joint key via stage 5). The 11-score snapshot corpus spans 3
Bach chorales + 8 non-Bach/non-chorale scores (bwv806 prelude/gigue, mozart k279/k280, chopin
bi105 ×2, schumann, corelli). **Goldens NOT refreshed.**

### §6.5 — mode-collapse (the measured representational surface)
Regions where the wired mode is Ionian/Aeolian but production emitted a richer mode:

| preset | total | same-tonic (mode-only) | tonic-changed | by production mode |
|---|---|---|---|---|
| Default | 212 | 62 | 150 | Lyd 120, Dor 61, Mixolyd 31 |
| Baroque | 63 | 33 | 30 | Dor 50, Mixolyd 10, Phryg 3 |
| Jazz | 4120 | 436 | 3684 | Dor 2226, Mixolyd 1845, Lyd 42, Phryg 7 |

The collapse maps each mode to its **same-quality** binary (Dorian→Aeolian both minor;
Mixolydian/Lydian→Ionian both major), so **(tonicPc, isMajor) is preserved** for same-tonic
collapses and major/minor is never flipped by the collapse itself.

---

## 5. §7 — adjudication of every moved case

- **BIR (the hard-stop axis):** **NO moved cases** — wired BIR=false sets are byte-identical
  to the baseline 57/23/57 case-identity sets (0 added / 0 removed, all 3 presets). Nothing to
  adjudicate; the §7/§9 hard-stop is clean. (KEY-ONLY leaves the chord = production R0, and BIR
  is a chord-axis metric, so it is byte-identical by construction.)
- **Mode-collapse:** **NOT a DCML key-accuracy regression.** DCML/rntxt annotates keys as
  major/minor only (binary — no Dorian/Mixolydian), and the collapse preserves major/minor, so
  the wired (tonicPc, isMajor) matches DCML at least as well as production's modal reading.
  - The **tonic-changed** collapses (150/30/3684) are part of the measured +win (the
    (tonicPc, isMajor) change is what `cc_j_key_i_measure` scored, net-positive).
  - The **same-tonic** collapses (62/33/436) are key-accuracy-NEUTRAL ((tonicPc, isMajor)
    unchanged); they only rename the rendered mode (e.g. `CDor`→`Cmin`) + change
    `keySignatureFifths` to the binary-relative signature. In every spot-checked case the
    production "Dorian/Mixolydian" was itself the partial-signature artifact (e.g. `CDor` on a
    piece DCML annotates as a minor key), so collapsing to maj/min is **more** DCML-aligned, not
    less. **Genuine-collapse-regression count vs DCML: 0.** The accepted consequence is the
    loss of modal *rendering* nuance — surfaced, an inherent property of the (tonicPc,isMajor)
    decision (instruction §2), not a scored error.
- **Snapshots:** all 11 move = key re-contextualization (the win, on Bach; unmeasured on the
  non-Bach snapshot scores). **The Bach snapshot key moves are covered by the WiR-Bach +win;
  the non-Bach snapshot scores (mozart/chopin/schumann/corelli/bwv806) are OUTSIDE the
  WiR-Bach measurement scope** and would need separate per-score DCML adjudication before any
  golden refresh. Goldens NOT refreshed (HELD) — this is the one remaining commit-gate.

---

## 6. §8 — commit recommendation

**Commit-gate status (instruction §8):**

| gate | status |
|---|---|
| Key win realized (§5 holds) | ✅ **YES** — wired key == soft, 0 mismatches/33,434 regions |
| No **un-adjudicated** BIR=false increase on any preset | ✅ **YES** — BIR byte-identical 57/23/57 (no increase) |
| Every mode-collapse move DCML-justified | ✅ **YES** — preserves major/minor; DCML is binary; 0 genuine regressions |
| Every snapshot move DCML-justified + goldens refreshed | ⛔ **NOT YET** — all 11 move; non-Bach snapshot scores outside WiR-Bach scope; goldens unrefreshed (HELD) |
| `docs/scoring_model.md` sync | **N/A** — no chord-scoring term/weight moved (key-only); the change is a key-axis wiring |

**Recommendation: the KEY-ONLY J-key-iii wiring is sound, realizes the ratified key win
cleanly, and introduces NO chord/BIR regression. HOLD for ratification on two items the user/
Cowork must decide:**

1. **Snapshot refresh + non-Bach adjudication.** Refreshing the 11 goldens needs per-score
   DCML adjudication; the 8 non-Bach/non-chorale snapshot scores lie outside the WiR-Bach
   measurement and need a separate adjudication pass (they DO have When-in-Rome coverage —
   extending `cc_j_key_i_measure`-style alignment to them is the clean path) before
   `--update-goldens`.
2. **Commit form.** The wiring is flag-gated DEFAULT OFF (production byte-identical until the
   flag flips). Either (a) commit flag-OFF now as a dormant staging step and flip the default
   ON as a later ratification act (with refreshed goldens), or (b) flip ON + refresh goldens in
   one commit. Either way the commit message must state this is the **first intentional
   production behavior change on the key axis (the constrained-joint architecture landing)**.

**Deferred (separate design):** the chord-axis re-emission (diatonic-root re-rank under the
joint key) — it requires a faithful re-run of the actual pipeline passes under the joint key
(segmentation is key-dependent, so a naive re-run can move boundaries and break §5); the
per-region snapshot re-analysis attempted here is structurally unfaithful (~6% root noise).

---

## 7. Stop conditions: status

| Condition (instruction §9) | Fired? |
|---|---|
| §0 restore does NOT reproduce the ratified J-key-i profile | No — byte-identical (§0.1) |
| §5 wired key ≠ measured `jointKey` decisions | No — 0 mismatches/33,434 regions (§3) |
| Un-adjudicated BIR=false increase on any preset | No — BIR byte-identical 57/23/57 (KEY-ONLY) |
| Edit required outside `src/composing/` | No — all `src/composing/` + `tools/`; test binaries use the env-var default, no `src/notation` edit |
| Iteration to a fixpoint / recompute joint key from re-emitted chords | No — `decideJointKey` once, frozen; chord not re-emitted at all (KEY-ONLY) |
| A snapshot / mode-collapse move not DCML-adjudicable as correct | **Surfaced** — the non-Bach snapshot scores are outside the WiR-Bach measurement (§6.4/§7); goldens NOT refreshed, NOT committed past |

A genuine STOP fired in §6 (the chord re-emission's BIR increase) — it was surfaced, diagnosed
as a re-emission artifact, and resolved by the user-ratified pivot to KEY-ONLY (which clears
the BIR hard-stop). No stop forces an abort of the key-axis wiring.

---

## 8. Files (HELD, uncommitted) + notes
- `src/composing/analysis/section/jointkeydecision.{h,cpp}` (J-key-i restore + wiring flag)
- `src/composing/analysis/section/sectionanalyzer.cpp` (Layer B gated on the flag)
- `src/composing/analysis/region/regionanalyzer.cpp` (`applyJointKeyWiring`, key-only)
- `src/composing/analysis/key/keymodeanalyzer.{h,cpp}` (`keySignatureFifthsForKey`)
- `src/composing/tests/jointkeydecision_tests.cpp` (J-key-ii demotion test removed → 7 tests)
- `tools/batch_analyze.cpp` (`--joint-key-wiring`), `tools/run_bach_preset.py` (pass-through)
- `tools/cc_j_key_iii_{decision_diff,invariant_check,mode_collapse}.py` (read-only instruments)
- `src/composing/analysis/region/harmonicrhythm.h` — **net 0 diff** (the temporalCtx-snapshot
  extension added during the chord-re-emission diagnosis was fully reverted for KEY-ONLY).

`HEAD 2245aedf82` unchanged; no commit. Gate corpora under `tools/corpus/*_jki_re` (dump,
wiring-OFF) and `tools/corpus/*_jkiii` (key-only wiring-ON) are gitignored / HELD.

**HELD — Cowork verifies at source; the user ratifies the commit.**
