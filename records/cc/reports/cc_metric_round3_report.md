# CC — METRIC-FIRST Round 3 report: FINE-GRAINED (per-beat) oracle-root metric

> **READ-ONLY. HEAD `dd418ecfed`. No analyzer build, no committed gate tool, no production/gate/scoring/
> threshold change.** Every number below is computed from on-disk corpora only, reusing
> `compare_analyses` (`three_way_classify`, `_dcml_time_spans`, `align_*`) + `dcml_parser` +
> `characterise_bir_false.validate_corpus_dir` verbatim. The repro script is throwaway and **uncommitted**:
> `tools/cc_round3_measure.py` (raw blob `tools/cc_round3_out.json`). It is a diagnostic helper, **not** the
> standing `--oracle-root` gate tool (still unbuilt, pending ratification of this baseline).

---

## Headline

- **The fine-grained design works and achieves its stated purpose.** Scored at the oracle's native event grid,
  the charged-error verdict and the oracle-dispute floor **separate cleanly by construction** (a charge requires
  `music21 == dcml`; a floor requires `music21 ≠ dcml` — no event can be both). The round-2 STOP — the
  segmentation-straddle alignment ambiguity — **is dissolved**: every oracle event is scored against its own
  oracle root at its own tick, so the onset-vs-overlap verdict flip no longer exists.
- **All 4 straddle cases dissolve, and all 6 inspected anchor cases now read HEAD-charged → ANCHOR-ok.** At the
  specific DCML event the anchor work targeted, the policy-A oracle (music21 ∧ DCML, both concurring) carries the
  **ANCHOR** root, not HEAD's. The round-2 "5 regressions" were an artifact of the *music21-only-onset* proxy
  reading a fleeting chord at the **region start tick**, which is **not** the DCML event tick. Fine-grained
  policy-A scoring reverses that label — the anchor readings are locally correct.
- **Per-event baseline, per preset (charged / floor reported separately):**

  | preset | **charged** (genuine oracle-root error) | **floor** (same-event m21≠dcml) | scoreable events | correct |
  |---|---:|---:|---:|---:|
  | **Baroque HEAD** (`baroque_kma_abs`) | **3862** | 4287 | 18348 | 10108 |
  | **Jazz** (`jazz`) | **4065** | 4276 | 18348 | 9925 |
  | **Default** (`default`) | **3894** | 4285 | 18348 | 10077 |
  | Baroque ANCHOR (`baroque`) — *acceptance ANCHOR only* | 4243 | 4285 | 18348 | 9723 |

- **~7× sanity holds in spirit, runs hotter in fact:** the per-event charged **rate** is **21.05%** vs the batch
  charged rate **2.01%** — a **10.5×** jump (per-beat strict: 18.9% → **9.4×**). Same order as CLAUDE.md's ~7×
  note, modestly higher; the divergence is explained (§4). The deeper finding: the **floor rate is
  granularity-stable** (batch 22.6% vs per-event 23.4%) while only the **charged rate explodes** — direct
  evidence that batch max-overlap alignment systematically **under-reports** our root errors by ~10×.
- **No stop condition hit.** The charge/floor separation is clean; no production change was needed to expand onto
  the grid (read straight from `.ours.json` regions); nothing committed; all 4 straddles dissolved.

---

## §1 — The fine-grained metric, as measured

**Granularity = the oracle's native event grid.** One scored **event per DCML annotation** (each place the
oracle asserts a root). For the WiR chorale `.rntxt` this *is* the per-beat / per-harmony native grid (≈56
scoreable events per chorale; 18 348 across the 326 WiR-covered chorales). This is finer than batch granularity
(≈31 of *our* regions per chorale) and is explicitly **not** batch-region granularity.

**Event tick = the DCML annotation's ONSET tick**, reconstructed from **our** region measure-anchors via
`compare_analyses._dcml_time_spans` (the WiR `.rntxt` has no `abs_tick` column — this reconstruction is the
per-beat-specific wrinkle, carried forward in §5).

**Expansion onto the grid (no alignment *choice* remains).** At each event tick, our root and music21's root are
each the root of the region (ours / music21 respectively) whose `[start, end)` **contains** that tick
(tick-containment). There is no onset-vs-max-overlap decision — every oracle event is compared against our root
at that tick, and the straddle's over-coverage is charged on exactly the beats the region wrongly covers.

**Predicate (unchanged, per event):** `three_way_classify(our_pc, m21_pc, dcml_pc)`, bass-decoupled, pc-typed
(normalizer-immune). Roots typed as pitch-class ints; our absent-root (`-1`) and music21 absent-root normalized
to `None`.

**The clean separation (the whole point of the round):**

| `m21` vs `dcml` at the event | possible three_way category | bucket |
|---|---|---|
| `m21 == dcml` | `all_agree` (our matches) | **CORRECT** |
| `m21 == dcml` | `music21_dcml_agree` (our differs) | **CHARGED** — genuine oracle-root error |
| `m21 ≠ dcml` | `dcml_ours_agree` (we side with GT) | **FLOOR** — oracle dispute |
| `m21 ≠ dcml` | `all_differ` (both present) | **FLOOR** — oracle dispute |
| either absent | `no_dcml` | unscoreable (excluded) |

Because a charge requires `m21 == dcml` and a floor requires `m21 ≠ dcml`, **no event is ever both**. The floor
is now *only* genuine same-event oracle disagreement — the segmentation straddles are no longer floored; they
surface as per-event charges. This separation is structural, not heuristic, so the §5 stop condition ("cannot
separate straddle-charge from same-event dispute") is **not** triggered.

**A robustness property worth recording.** A charge requires `our_pc ≠ m21_pc` at the **same** sampled tick.
Reconstructed-tick rounding at a chord boundary moves **both** the ours-sample and the music21-sample together
(both lag into the previous region), so it produces `our == m21 ≠ dcml` → **floor**, never a spurious charge.
The charged set is therefore robust to the rntxt tick-reconstruction it depends on; only the (granularity-stable)
floor absorbs boundary noise.

---

## §2.1 — The 4 straddle cases dissolve; the bwv102.7 per-event ledger

All four are scored on HEAD (`baroque_kma_abs`) and ANCHOR (`baroque`). **Each dissolves**: every DCML event in
the span is scored against its own oracle root, the over-grabbed region is charged on the mismatched beats, and
the onset-vs-overlap flip is gone. In **all four**, at the targeted DCML event, **HEAD is charged and ANCHOR is
correct** — the policy-A oracle sides with the anchor reading.

### bwv102.7 per-event ledger (the inspected case)

`PC` shown in parentheses; the disputed region is the straddle of `vi` (DCML root C) into `IVmaj7` (DCML root Ab).

| tick | m.beat | DCML | ours (HEAD) | ours (ANCHOR) | m21 | verdict HEAD → ANCHOR |
|---:|---|---|---|---|---|---|
| 16800 | 9.4 | `vi` (C) | Bb (Bb) | Bb7 (Bb) | Bb | **floor** → floor *(m21=Bb ≠ dcml=C — oracle dispute)* |
| **17760** | **10.1** | **`IVmaj7` (Ab)** | **EbMaj7/Ab (Eb)** | **AbMaj9 (Ab)** | **Ab** | **CHARGED → ok** |
| 18240 | 10.2 | `V` (Bb) | Bb (Bb) | Bb7 (Bb) | Bb | ok → ok |
| 18720 | 10.3 | `I` (Eb) | Eb (Eb) | Eb (Eb) | Eb | ok → ok |

The round-2 ambiguity was: *onset, m21-only* → oracle Eb (HEAD right); *max-overlap, policy-A* → oracle Ab (HEAD
wrong). Fine granularity **eliminates the choice**: at the `IVmaj7` onset (17760) **music21 and DCML both assert
Ab**, so HEAD's lingering Eb is a charged error and ANCHOR's Ab is correct. The `vi` beat (16800) is a genuine
oracle dispute (music21 Bb vs DCML C) → floor, charged to neither. The straddle is fully resolved into one
charge (the Ab beat) and one floor (the C/Bb beat).

### The other three straddles (verdict at the targeted DCML event)

| case | DCML event | DCML root | m21 | HEAD ours → pc | ANCHOR ours → pc | verdict |
|---|---|---|---|---|---|---|
| **bwv358** | m4.2 `viio7` | Ab | Ab | E11/G# → E | G#dim7 → **Ab** | **CHARGED → ok** |
| **bwv432** | m3.4 `vi` | E | E | Am/E → A | EMaj7#5 → **E** | **CHARGED → ok** |
| **bwv227.7** | m10.2.5 `iv6/5` | E | E | Gadd9/F# → G | Em13 → **E** | **CHARGED → ok** |

(bwv227.7 has a second nearby event, m10.3 `V6/5` root C#, where **both** readings are charged — neither G nor E
matches C#; a genuine error common to both binaries, correctly surfaced.)

**Reconciliation with round 2 / the anchor dossier.** The dossier's §2C "oracle roots" (Eb, E, A, G) were the
*music21-only* readings at the **region-start** tick. At the **DCML event** tick, the authoritative DCML root and
music21 **both** read the ANCHOR root (Ab, Ab, E, E). So the four "regressions" were proxy artifacts; under the
ratified policy-A oracle at fine granularity they are **anchor-correct events**. This is consistent with the
design's purpose — fine granularity reveals what batch max-overlap alignment hid — and it means the acceptance
target should be restated (§2.3), not that the metric failed.

---

## §2.2 — Per-preset fine-grained baseline (charged + floor, separately)

### Per-event (oracle-native: one event per DCML annotation)

| preset | charged | floor | scoreable | total events | correct |
|---|---:|---:|---:|---:|---:|
| **Baroque HEAD** | **3862** | **4287** | 18348 | 18403 | 10108 |
| **Jazz** | **4065** | **4276** | 18348 | 18403 | 9925 |
| **Default** | **3894** | **4285** | 18348 | 18403 | 10077 |
| Baroque ANCHOR | 4243 | 4285 | 18348 | 18403 | 9723 |

WiR coverage: **326 / 353** chorales (the 27 without a WiR `.rntxt` contribute no scoreable events; identity
hazard inventory-C3 unchanged).

### Per-beat (strict: every beat tick inside each DCML span)

| preset | charged | floor | scoreable | total beats |
|---|---:|---:|---:|---:|
| **Baroque HEAD** | 4016 | 4969 | 21221 | 21462 |
| **Jazz** | 4219 | 4961 | 21220 | 21461 |
| **Default** | 4045 | 4965 | 21220 | 21461 |
| Baroque ANCHOR | 4432 | 4965 | 21220 | 21461 |

### Accounting (Baroque HEAD, per-event) — charged and floor are never conflated

```
scoreable 18348 = correct 10108 + charged 3862 + floor 4287 + residual 91
  floor 4287 = dcml_ours_agree 456  (we side with DCML vs music21)
             + all_differ-both 3831 (three-way oracle dispute)
  residual 91 = events where OUR root is absent (-1) but the oracle pair concurs
              (~0.5%); a standing tool must decide whether to charge these — flagged, not assumed.
```

**Direction is consistent across granularities and with round 2.** HEAD < ANCHOR in charged errors at per-event
(3862 < 4243), per-beat (4016 < 4432), and batch B (106 < 116) — HEAD is globally the better binary. The six
inspected cases are precisely where the anchor work *locally* improved a reading while regressing more elsewhere
(net worse). Jazz is the worst preset per-event (4065), as expected for a non-Baroque-tuned configuration.

---

## §2.3 — Acceptance, restated for fine granularity

The instruction's acceptance for this round is **not** "reproduce the 5/2 split" (round 2 already showed the 5/2
is a music21-only-onset artifact). It is:

1. **The 2 robust fixes remain fixes** — ✅ confirmed at the event tick:
   - bwv14.5 m5.1 `I` (Bb): HEAD `Gm/Bb`→G **charged** → ANCHOR `Bbadd9`→Bb **ok** = **FIX**.
   - bwv416 m6.1 `viio7` (Ab): HEAD `E7b9/G#`→E **charged** → ANCHOR `G#dim7`→Ab **ok** = **FIX**.
2. **The straddle cases are now SCORED per-beat (charged on the mismatched beats), not floored** — ✅ all 4
   produce per-event **charges** on the over-covered beats (§2.1), and **floors** only where the two oracles
   genuinely disagree at the same beat.
3. **The genuine same-beat-disagreement set is the ONLY floor** — ✅ by construction (the §1 table); verified in
   every ledger (e.g. bwv102.7 `vi` beat: m21 Bb vs DCML C → floor; bwv432 m3.1.5–3.3 `viio7`/`i`: symmetric-dim7
   / m21≠DCML → floor).

The round-3 metric **cleanly separates segmentation-straddle (charged) from same-beat oracle dispute (floor)** —
the separation that was "the whole point." No STOP.

---

## §2.4 — The ~7× sanity check

| granularity | scoreable | charged | **charged rate** | floor rate |
|---|---:|---:|---:|---:|
| **batch region** (round-2 method, pure `music21_dcml_agree`) | 10115 | 203 | **2.01 %** | 22.58 % |
| **per-event** (oracle-native) | 18348 | 3862 | **21.05 %** | 23.36 % |
| **per-beat** (strict) | 21221 | 4016 | **18.92 %** | 23.43 % |

- **Charged rate ratio:** per-event **10.5×** batch; per-beat **9.4×** batch. CLAUDE.md's granularity note
  predicts **~7×**. Same order of magnitude, running modestly hotter. **Divergence explained:** (a) the
  CLAUDE.md ~7× is measured via `batch_analyze --section-level` — our **measure-aligned section** grid, which is
  *coarser* than the **per-DCML-annotation** grid here (≈56 oracle events vs fewer sections per chorale); (b) the
  batch comparator here is the **pure** `music21_dcml_agree` set with **no** `chord_disagree` filter, whereas the
  ~7× note's batch reference is closer to the filtered gate. Both push the round-3 ratio above 7×. The numbers
  are mutually consistent, not contradictory.
- **The structurally important result:** the **floor rate is granularity-stable** (22.6 % → 23.4 %) while the
  **charged rate jumps ~10×** (2.0 % → 21.1 %). The floor (music21 vs DCML convention boundaries) is an intrinsic
  property of the oracle pair; the charged-error rate is what **batch max-overlap alignment hides** — a wrong
  region aligned to the one DCML chord it *does* match scores "correct" while its over-coverage of neighboring
  DCML chords goes uncounted. Fine granularity is precisely the fix the anchor dossier's BIR blind-spot demanded.

---

## §3 — Genre-balanced carry-forward (unchanged from round 2 §B; one per-beat wrinkle)

Fine granularity does not change the round-2 §B conclusion:

- **Policy A is chorale-only today.** Only the 326 WiR-covered Bach chorales have `.music21.json` sidecars, so
  the music21-corroboration half of policy A cannot run off-chorale. The DCML GT for all 10 non-chorale corpora +
  the WiR anthology parses cleanly (round-2 §B.1 coverage table stands), but consuming it needs a build
  (`batch_analyze` over each corpus) and a **DCML-only** oracle (weaker than chorale policy A).
- **Recommendation stands: option (a) two-tier macro** — a policy-A per-event number for chorales + a separate
  DCML-only per-event macro across all genres (one observation per genre, macro-averaged so the chorales cannot
  dominate). Option (b) (generate ~1 700 music21 sidecars for a uniform policy-A macro) remains a Stage-5
  decision, not read-only.
- **Per-beat-specific wrinkle (new):** the per-event/per-beat grid needs an **absolute tick per oracle event**.
  TSV corpora carry `quarterbeats` → `abs_tick` (pickup-aware, no reconstruction). The WiR `.rntxt` (chorales
  *and* the anthology) has **no** absolute column, so event ticks are reconstructed from **our** region anchors
  via `_dcml_time_spans` — i.e. even the chorale per-beat grid needs `.ours.json` present. This is the same
  dependency round-2 §B.3 flagged; fine granularity makes it load-bearing for *every* event, not just alignment.
- **Diagnostic only (B.4):** a genre-balanced number reports where we stand. It must **not** trigger widening any
  Baroque-tuned threshold (CLAUDE.md hard rule).

---

## §4 — Stop-condition compliance

- **READ-ONLY** — HEAD `dd418ecfed`; no build, no committed tool, no production/gate/scoring/threshold change. ✅
- **Charge/floor separation** — clean and structural (m21==dcml ⇒ charge-bucket; m21≠dcml ⇒ floor-bucket); no
  event is both. Verified in every straddle ledger. **No STOP.** ✅
- **No production change needed to expand onto the grid** — our roots are read directly from existing
  `.ours.json` regions by tick-containment; the only reconstruction is the (already-existing) `_dcml_time_spans`
  tick rebuild for rntxt. **No STOP.** ✅
- **All 4 straddle cases dissolve** under per-event scoring (each scored per beat, no residual alignment
  ambiguity). **No STOP.** ✅
- **Nothing committed / no threshold touched** — `tools/cc_round3_measure.py` is throwaway. ✅

**For Cowork/user — ratify before the standing `--oracle-root` tool and off-chorale builds are scoped:**
1. **The fine-grained baseline** — per-event **charged 3862 / floor 4287 (Baroque HEAD)**, Jazz 4065 / 4276,
   Default 3894 / 4285, with charged and floor reported as **separate** standing sets (never summed).
2. **Granularity choice** — per-event (oracle-native, one per DCML annotation) as primary, with per-beat (strict)
   as the duration-weighted secondary. Per-event is recommended: it matches "wherever the oracle asserts a root,"
   is robust to held-chord weighting, and is boundary-rounding-robust on the charged set.
3. **The restated acceptance** — the 2 robust fixes confirmed; the 4 straddles **scored** (not floored); the
   "5 regressions" retired as music21-only-onset proxy artifacts (the policy-A oracle sides with ANCHOR at the
   DCML event). The standing gate's correctness criterion becomes **charge/floor separation + the 2 fixes**, not
   the obsolete 5/2.
4. **Two open accounting micro-decisions** for the tool: whether to charge the 91 absent-our-root events
   (oracle concurs, we produced no root), and the case-identity key (stem@reconstructed-tick vs stem@(measure,beat)
   — the latter is preset-stable since rntxt ticks are reconstructed per-preset from our anchors).
