# J-key-ii-redux — STEP 1: measure the signature-contradiction gate separability

> **HELD — uncommitted, diagnostic-only, production byte-identical. STEP 1 ONLY.**
> The user-ratified redux (2026-06-15) replaces J-key-ii's *global* signature
> demotion with a **scoped, confidence-gated** partial-signature override, built
> **measure-first**: Step 1 measures whether a precise per-piece confidence threshold
> even exists that separates the ~56 partial-signature stems (note evidence *should*
> override the signature) from the correctly-signed bulk (the override must NOT fire).
> **Step 2 (build the override) is gated on Step 1 finding a usable threshold (§1/§3).**
>
> **Result: the gate is NOT separable across the three presets → §7 STOP fired.**
> Step 2 was NOT built; no override is wired; the producer is unchanged. Decision on
> J-key-iii reverts to Cowork/user.
>
> **Date:** 2026-06-15. **HEAD:** `2245aedf82` (unchanged). **Scope of numbers:**
> WiR-Bach DCML-aligned stems (325/353 each preset; 28 unaligned). Every key is
> `[oracle]` via the committed `dcml_parser`/`compare_rn` machinery. Collection-fit is
> computed in Python identically to `jkdCollectionMask`/`collFit` in
> `jointkeydecision.cpp`; the cadence anchor is the committed `detectLocalModulations`
> anchor, read from the dump. Read-only; no decision was wired.

---

## 0. Headline — no precise threshold separates the 56 from the bulk

1. **A confidence signal DOES exist with a perfect override TARGET, but it does not
   SEPARATE the populations.** The best gate — *the cadence anchor names a tonic whose
   signature ≠ the notated fifths, AND the piece-global collection-fit agrees with that
   anchor, AND the collection margin ≥ θ* (override target = the anchor key) — has
   **100 % override-target correctness at every threshold on every preset**: when it
   fires, the key it would swap to is *always* the DCML global key. That is the one
   genuinely good property. But the *firing condition* cannot be thresholded to fire on
   the 56 without also firing on correctly-signed bulk pieces.

2. **⛔ The gate is NOT separable — two independent obstructions, both load-bearing:**
   - **`bwv176.6` Pareto-DOMINATES the `bwv265` stress case** in *every* key-agnostic
     signal §3 names (and the two extra ones we dumped). `bwv176.6` is a **correctly-
     signed Bb-major chorale** the anchor wrongly reads as **C minor** (an internal ii
     tonicization); `bwv265` is a genuine **D-minor-notated-0-flats** stem §5 requires
     to recover. Their signals: `bwv176.6` collMargin **0.095** ≥ `bwv265` **0.031**;
     anchorConf **0.435** ≥ **0.368**; cadenceCount **15** ≥ **6**; anchorMargin
     **0.095** ≥ **0.031**. Because `bwv176.6` ≥ `bwv265` on **all four axes**, *any*
     monotone gate that fires `bwv265` also fires the `bwv176.6` regression. Recovering
     the required stress case is **impossible without a bulk regression**.
   - **Jazz `bwv62.6` sits at the MAXIMUM of both confidence signals.** A correctly-
     signed **A-minor** chorale the anchor reads as **G minor** from a single, unanimous
     (cadenceCount 1, anchorConfidence **1.000**) but **wrong** cadence — collMargin
     **0.184**, the *highest of any fire on any preset*. No conservative threshold on
     margin or confidence excludes it (the Gate-D confidence sweep still leaves it firing
     at cthr 0.90). On Jazz there is **no threshold with 0 bulk false-fires** at any
     usable recall.
   - The three false-fires occupy **different corners** of the signal space
     (`bwv62.6`: hi-margin / hi-conf / lo-cadence; `bwv176.6`/`bwv289`: mid-margin /
     mid-conf / **hi**-cadence), so no single region contains every genuine stem and
     excludes every false-fire.

3. **The "best safe" fallback is too weak AND not all-preset-safe.** The most
   conservative gate (Gate C, θ = 0.10) is clean on **Default/Baroque** (0 bulk
   false-fires, 100 % target) but recovers only **9/56 (16 %)** — it catches the
   high-confidence Dorian lies (incl. `bwv254`) but **NOT `bwv265`** (margin 0.031), and
   it still fires the **`bwv62.6`** regression on **Jazz**. At 16 % recall the safety
   (lattice-exclusion) rate would improve only **~17 % → ~14.5 %**, nowhere near the §6
   "~0" proceed criterion. So even the safe corner fails both the safety target and the
   §5 stress requirement.

4. **Production is byte-identical; the only code touched is an additive diagnostic.**
   The lone change is `tools/batch_analyze.cpp` +2 lines emitting `anchorConfidence` /
   `anchorCadenceCount` inside the `--dump-joint-key` block (so the gate could be
   measured with the anchor's own strength). Verified production byte-identical:
   **353/353 `.ours.json`, 0 production-field diffs** vs the committed `tools/corpus/default`.
   `composing_tests` **546/546**. **The producer (`jointkeydecision.{h,cpp}`) was NOT
   touched** — Step 2 was not built.

**Verdict on J-key-iii (the wiring gate): DO NOT WIRE.** Per §1/§3/§7, Step 1 found no
precise threshold that separates the 56 from the bulk across all three presets while
recovering the stress cases; the override cannot be made safe at meaningful recall. The
decision reverts to Cowork/user. (A possible *future* signal that is OUT of the §3 scope
is noted in §6.)

---

## 1. What was built (Step 1 only — read-only)

All work in `src/composing/` (none) + `tools/`. **Zero** `src/notation` / `src/engraving`
edits. **No producer edit; no override; no decision wired** (Step 2 was gated off).

- **`tools/cc_j_key_ii_redux_step1.py`** (new) — the read-only separability instrument.
  For each `.ours.json` it forms the per-piece **signature-contradiction confidence**
  from the key-agnostic note evidence §3 names:
  - `avgCollFit[k]` for all 24 keys — piece-global, popcount-weighted in-collection
    fraction, **identical to `jkdCollectionMask`/`collFit`** in `jointkeydecision.cpp`,
    normalized to [0,1];
  - `sigBest` = max(avgCollFit[home-major], avgCollFit[home-minor]) — the notated
    signature relative pair;
  - `contraKey` = argmax avgCollFit over keys whose **signature fifths ≠ the notated
    fifths** (the §3 Dorian-lie restriction); `collMargin` = avgCollFit[contraKey] − sigBest;
  - the committed cadence **anchor** (tonic/mode/confidence/cadenceCount), read from the
    dump; `anchorContra` (anchor names a non-notated-signature tonic), `anchorMargin`.
  It classifies each stem via DCML (**the same definition `cc_j_key_ii_safety.py` uses**:
  a stem is partial-signature iff it has ≥1 DCML key-stable region where the notated home
  fifths ≠ the DCML global key's fifths), sweeps thresholds, and reports recall on the 56 /
  false-fire on the bulk / precision **and override-target correctness** (does the fired
  key == DCML global).
- **`tools/batch_analyze.cpp`** — +2 additive lines in `writeJointKeyJson` emitting
  `anchorConfidence` + `anchorCadenceCount` (only under `--dump-joint-key`; production
  byte-identical). This let Step 1 test whether anchor **strength** discriminates a true
  global tonic from an internal tonicization (it does not — §3).
- Measurement corpora `tools/corpus/{default,baroque,jazz}_reduxs1` regenerated with the
  flag (gitignored). The committed `*_jki` dumps (the J-key-i strong-backbone baseline)
  were the cross-check; populations reproduce the J-key-i/ii 56-stem set exactly.

---

## 2. §3 — Population + the best gate (all three presets)

**Populations (identical on all three presets):** 56 partial-signature stems / 269
correctly-signed bulk / **325 DCML-aligned** (28 unaligned, 0 missing jointKey). This is
the J-key-i/ii ~56-stem set (incl. the `bwv254`/`bwv265` stress cases).

**Gate C** = `anchorContra` ∧ (anchor key == collection `contraKey`) ∧ `collMargin ≥ θ`,
override target = the anchor key. Threshold sweep (recall on 56 / bulk false-fires /
precision / target-correctness):

| preset | θ=0.02 | θ=0.04 | θ=0.06 | θ=0.10 | θ=0.12 |
|---|---|---|---|---|---|
| **Default** | 23 / **2** / 92.0 % / 100 % | 19 / 2 / 90.5 / 100 | 14 / 2 / 87.5 / 100 | 9 / **0** / 100 / 100 | 5 / 0 / 100 / 100 |
| **Baroque** | 23 / **2** / 92.0 / 100 | 19 / 2 / 90.5 / 100 | 14 / 2 / 87.5 / 100 | 9 / **0** / 100 / 100 | 5 / 0 / 100 / 100 |
| **Jazz** | 21 / **3** / 87.5 / 100 | 19 / 3 / 86.4 / 100 | 16 / 3 / 84.2 / 100 | 9 / **1** / 90.0 / 100 | 4 / 1 / 80.0 / 100 |

- **Target-correctness is 100 % at every θ on every preset** — the override never points
  to a *wrong* key *when it fires on a genuine stem*. The problem is purely **which
  pieces** fire, not where they point.
- The clean (0-bulk-false-fire) corner exists only on **Default/Baroque** (θ ≥ 0.10) and
  only at **16 % recall**; **Jazz never reaches 0** bulk false-fires (`bwv62.6`, θ=0.10).

The simpler gates separate **worse** (collection-margin alone: 9 bulk false-fires at θ=0.02;
anchor-margin alone: 5–6). Gate C is the best of the §3-scoped family.

---

## 3. §3 — Why it is NOT separable (the load-bearing finding)

The Gate-C fires (margin ≥ 0.02), sorted by anchor confidence, with the bulk false-fires
**embedded inside the genuine distribution** (Default; Jazz analogous):

```
 pop stem        aConf  aCad     mgn  fireTo  DCMLglob  ok
BULK bwv289      0.270    12  +0.086    Bmin     Emin   XX   <- false-fire, LOW conf
  56 bwv297      0.297    10  +0.040    Dmin     Dmin   OK
  56 bwv254      0.333     7  +0.114    Dmin     Dmin   OK   <- stress case
  56 bwv265      0.368     6  +0.031    Dmin     Dmin   OK   <- stress case (§5 MUST recover)
  56 bwv40.3     0.423     8  +0.074    Gmin     Gmin   OK
BULK bwv176.6    0.435    15  +0.095    Cmin    Bbmaj   XX   <- false-fire, MID conf, DOMINATES bwv265
  56 bwv245.37   0.451    15  +0.201   Bbmin    Bbmin   OK
  ... (all genuine OK above 0.45) ...
  56 bwv351      1.000     1  +0.130    Gmin     Gmin   OK
```

Jazz adds the decisive case at the very top:

```
  56 bwv351      1.000     1  +0.125    Gmin     Gmin   OK
BULK bwv62.6     1.000     1  +0.184    Gmin     Amin   XX   <- false-fire at MAX conf AND MAX margin
  56 bwv364      1.000     2  +0.078    Gmin     Gmin   OK
```

**Obstruction 1 — `bwv176.6` Pareto-dominates `bwv265`.** Every key-agnostic signal is
≥ for the false-fire than for the stress case it must beat:

| signal | `bwv265` (recover) | `bwv176.6` (must NOT fire) | dominates? |
|---|---|---|---|
| collMargin | +0.031 | +0.095 | yes |
| anchorConfidence | 0.368 | 0.435 | yes |
| cadenceCount | 6 | 15 | yes |
| anchorMargin | +0.031 | +0.095 | yes |

A monotone gate is any rule "fire when (margin, conf, cadence) each ≥ some cut." Since
`bwv176.6` ≥ `bwv265` on all axes, **any monotone gate that admits `bwv265` admits
`bwv176.6`.** Recovering the §5-required `bwv265` ⇒ a `bwv176.6` bulk regression. No
threshold escapes this.

**Obstruction 2 — Jazz `bwv62.6` is at the extreme of both signals.** anchorConfidence
1.000 (a single, unanimous, but *wrong* cadence) and collMargin 0.184 (the largest of any
fire). The Gate-D confidence sweep (Gate C ∧ anchorConf ≥ cthr) on Jazz:

| cthr | fire56 | fireBulk | recall | precision |
|---|---|---|---|---|
| 0.50 | 11 | **1** | 19.6 % | 91.7 % |
| 0.70 | 6 | **1** | 10.7 % | 85.7 % |
| 0.90 | 2 | **1** | 3.6 % | 66.7 % |

Even at cthr 0.90 the bulk false-fire (`bwv62.6`) persists while recall collapses. **There
is no all-preset threshold with ~0 bulk false-fires at usable recall.**

**Obstruction 3 — the false-fires are not co-located.** `bwv62.6` (lo-cadence/hi-conf)
and `bwv176.6`/`bwv289` (hi-cadence/mid-conf) require *opposite* cuts to exclude: a
cadence-count floor kills `bwv62.6` (cad 1) but not `bwv176.6`/`bwv289` (cad 15/12); a
margin/conf ceiling kills `bwv176.6` but also `bwv265`. No conjunction separates all three
from the genuine set.

**Root cause (musical):** a partial/Dorian signature is hard *precisely because* a
D-Dorian (notated-0-flats) chorale's notes fit the relative-major collection nearly as
well as the true harmonic-minor collection — so `bwv265`'s D-minor margin is only +0.031.
Meanwhile a correctly-signed piece with a strong internal tonicization (`bwv176.6` → C
minor, `bwv62.6` → G minor) produces a *larger* note-evidence contradiction than the genuine
lie. The committed anchor's known V→IV/internal over-detection (the ~44 % pin-wrong warning
in the instruction) is exactly this failure mode, and the collection-fit does not rescue it.

---

## 4. §5 — The "best safe" fallback, and why it still fails the gate

The only clean corner is **Gate C, θ = 0.10**:

| preset | recall (of 56) | bulk false-fires | target-correct | recovers bwv254? | recovers bwv265? |
|---|---|---|---|---|---|
| Default | 9/56 = 16 % | **0** | 100 % | **yes** (mgn 0.114) | **no** (mgn 0.031) |
| Baroque | 9/56 = 16 % | **0** | 100 % | yes | no |
| Jazz | 9/56 = 16 % | **1** (`bwv62.6`) | 100 % | yes | no |

It is not viable as J-key-iii because:
- **Safety target unmet.** Recovering 9 of 56 moves the lattice-exclusion / structural
  mis-key rate ~17 % → ~14.5 %, far from the §6 "~0" proceed criterion. The other ~47
  stems (incl. `bwv265`) stay mis-keyed.
- **Stress requirement unmet.** §5 requires `bwv265` to escape A minor; at θ=0.10 it does
  not fire (margin 0.031 < 0.10).
- **Not all-preset-safe.** Jazz still regresses `bwv62.6`.

Lowering θ to recover `bwv265` (θ ≤ 0.031) reintroduces the `bwv176.6`/`bwv289` (and Jazz
`bwv62.6`) regressions (§3). There is no θ that is simultaneously safe and sufficient.

---

## 5. §5 — Byte-identity + suite gates (diagnostic must not perturb production) — PASS

| Gate | Result |
|---|---|
| `.ours.json` byte-identity (jointKey stripped vs committed `tools/corpus/default`) | **353/353, 0 production-field diffs** |
| Code touched | `tools/batch_analyze.cpp` +2 additive diagnostic lines (`anchorConfidence`, `anchorCadenceCount`), under `--dump-joint-key` only |
| Producer (`jointkeydecision.{h,cpp}`) | **UNCHANGED** (Step 2 not built) |
| composing_tests | **546 / 546 PASS** |
| BIR gate | **57 / 23 / 57 preserved by byte-identity** (BIR is a function of the production `.ours.json`, which is byte-identical) |

`notation_tests` / `pipeline_snapshot_tests` were **not re-run**: no code they cover was
changed (the only edit is an additive diagnostic dump field in a tools binary; the producer
and all production paths are untouched). Production byte-identity (above) is the load-bearing
gate and it passes.

---

## 6. §6 — The J-key-iii verdict + a clearly-scoped future signal

**J-key-iii = DO NOT WIRE.** The §6 proceed gate (*proceed only if safety ~0 AND bulk win
preserved AND override precision high with no bulk regression*) cannot be met by any
threshold on the §3-scoped signals: the gate is not separable across the three presets
(§3), and the only clean corner (§4) is both insufficient (16 % recall, safety ~14.5 %) and
not all-preset-safe (`bwv62.6`). Per §7 ("Step 1 finds no precise threshold separating the
56 from the bulk → STOP, surface; the override can't be made safe; decision reverts to
Cowork/user"), **Step 2 was not built.** The good news worth carrying forward: when the
anchor+collection agree on a contradiction, the key they name is the DCML global key **100 %
of the time** — the *target* is reliable; only the *trigger* is not separable.

**The standing options for Cowork/user:**
1. **Accept J-key-i's ceiling** (the strong signature backbone) and treat partial-signature
   mis-keying as a known, bounded residual (it is the documented
   `project_key_detection_baroque_partial_signature` issue, now quantified on the key-decision
   gate: 56 stems, ~17 % of key-stable regions).
2. **Wire the ultra-conservative Gate C (θ≈0.10) anyway**, accepting ~9 recovered stems and
   the lone Jazz `bwv62.6` regression — NOT recommended (fails the safety target and the
   `bwv265` stress requirement; trades a small gain for a Jazz regression).
3. **A different signal (OUT of the §3 scope — untested, flagged, not a recommendation to
   proceed):** the discriminator the §3-scoped signals lack is *whether the notated
   signature pair ITSELF receives independent authentic-cadence support*. A genuine Dorian
   lie (`bwv265`) has cadences **only** to the true tonic (D), not to the notated pair (C/A);
   a false-fire (`bwv176.6`) has cadences to **both** its true Bb-major home **and** the
   tonicized C minor. The committed anchor exposes only the **winning** tonic, not the
   per-tonic cadence-vote vector, so "is the notated home independently cadenced?" is not
   measurable from the current dump. Testing it would need a new diagnostic (the cadence
   detector's per-tonic finality-weighted vote distribution) — a separate measure-first step
   to ratify, NOT part of this gate. It is logged here only so the next session does not
   re-derive it.

Independently (from §3/§4 of the J-key-ii report): the declared-mode hint is tied to the
*signature-relative* pair; on a Dorian stem it pulls toward the wrong relative minor. That
would have been re-anchored by the override in Step 2 — moot now that Step 2 is not built,
but it remains a real residual on the J-key-i/J-key-ii decision.

---

## 7. §7 — Stop conditions: status

| Stop condition | Fired? |
|---|---|
| **Step 1 finds no precise threshold separating the 56 from the bulk (gate not separable)** | **YES — §0/§3. Surfaced. Step 2 not built; decision reverts to Cowork/user.** |
| The override fires on correctly-signed pieces / regresses the bulk | Would have — `bwv176.6`/`bwv289`/`bwv62.6` (the reason for the STOP); no override was wired |
| The bulk win is not restored to J-key-i's level | N/A — Step 2 not built |
| Production resolve-path / `src/notation` / `src/engraving` edit needed | **No** |
| Any production-output / BIR / snapshot move (diagnostic leaked) | **No** — production byte-identical (353/353, 0 diffs); BIR 57/23/57 preserved |
| Any attempt to wire into production (J-key-iii) | **No** |
| Uncertain key decision | Adjudicated vs DCML (oracle); the 56-stem set + every false-fire bucketed and dumped |

The Step-1 measurement is complete and clean. The fired stop is a **HOLD on J-key-iii** (the
override cannot be made safe at the required recall), not a defect in the instrument.

---

## 8. Notes
- **Sandbox-bash noise:** measurement artifacts written to `/c/tmp/` (the MSYS `/tmp` vs
  Windows-`python` `/tmp` = `C:\tmp` split, per the prior reports). Corpus regen + DCML
  alignment ran clean; host-side Read/Grep are authoritative.
- **Gitignored / HELD:** this report (`/cc_*.md`) and the `tools/corpus/*_reduxs1`
  measurement corpora (`/tools/corpus/`) are gitignored — HELD by construction.
- **Reproduce:**
  `python tools/cc_j_key_ii_redux_step1.py tools/corpus/default_reduxs1 tools/corpus/baroque_reduxs1 tools/corpus/jazz_reduxs1`
  (the `_reduxs1` dirs carry `anchorConfidence`/`anchorCadenceCount`; the committed `*_jki`
  dirs reproduce the same separability minus those two fields).

### Files (HELD, uncommitted)
- `tools/cc_j_key_ii_redux_step1.py` (new — the read-only separability instrument)
- `tools/batch_analyze.cpp` (+2 additive diagnostic dump lines; production byte-identical)
- `tools/corpus/{default,baroque,jazz}_reduxs1/` (gitignored measurement corpora)
- `src/composing/analysis/section/jointkeydecision.{h,cpp}` — **UNCHANGED** (still the
  J-key-ii state; Step 2 was not built)

**HELD — uncommitted. Step 1 only. Cowork verifies at source; J-key-iii decision (do-not-wire
recommended) reverts to the user.**
