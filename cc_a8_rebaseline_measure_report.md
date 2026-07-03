# CC A-8 — Granularity-robust gate re-baseline: the MEASUREMENT

> **READ-ONLY / DECODE-ONLY / BYTE-IDENTICAL BY CONSTRUCTION.** No `src/` change, no behavior
> change, no gate change. This report MEASURES the candidate re-baselined gate on the frozen gate
> corpus so the user can ratify the A-8 re-baseline on evidence. The re-baseline itself is a separate
> user-ratification event on this report — **no recommendation beyond the measured facts here.**
>
> **Provenance.** Measurement base HEAD `fd6f499162` ([probe] `git rev-parse --short HEAD` at run start).
> Frozen gate corpus manifest `git_hash = 0dd64660f4`, `complete=true`, 352/352 each preset
> ([probe] `tools/corpus/{baroque,jazz,default}/corpus_manifest.json`). Measurement instrument committed
> at **`fd8ea88c0f`** (`tools/a8_rebaseline_measure.py`) — local, unpushed, fork-only. This report is
> the second (and only other) commit of this arc.
>
> Every quantitative claim is **[probe]** (ran the instrument and read output). The instrument is
> orchestration ONLY over already-pinned metric functions and **self-validates** its variant-(b)
> decomposition byte-for-byte against the pinned `compare_rn.grid_score_regions()` on every piece
> (see §0.2).

---

## §0 — What was done, and the read-only / no-surprise proofs

### §0.1 The no-contamination sandwich (acceptance #2)

The current batch-granularity gate reproduced **exactly**, set-diff empty both directions, all three
presets, **before and after** the candidate measurement runs [probe `characterise_bir_false.py`]:

| step | Baroque | Jazz | Default | set-diff vs CLAUDE.md |
|---|---|---|---|---|
| **BEFORE** (anchor) | 53 | 24 | 53 | **empty both directions** (all three) |
| **AFTER** (re-run post-measurement) | 53 | 24 | 53 | **empty both directions** (all three) |

The corpus is byte-untouched: `git status` shows **no change under `src/` or `tools/corpus/`**; the
only new tracked file is `tools/a8_rebaseline_measure.py` [probe]. No build was run or needed (Python
only, over the already-on-disk `.ours.json` / `.music21.json` + WiR rntxt).

### §0.2 The instrument faithfully reuses the pinned grid primitive

The driver re-runs the union-of-boundaries cell loop itself (so it can attach the KEY respect and the
music21 leg, which `grid_score_regions` does not compute). On **every piece** it asserts its
variant-(b) 5-bucket duration decomposition + `scored_dur` equal `compare_rn.grid_score_regions()`
byte-for-byte — the run completed with the assertion passing on all 326×3 covered pieces [probe:
`[preset] validated grid==oracle OK`]. That assertion is the proof the re-run loop is a faithful reuse
of the pinned primitive, not a re-definition. It also reuses `classify_pair`, `_active_index_at`,
`_our_key_tonic`/`_dcml_key_tonic`, `_dcml_time_spans`, `three_way_classify`, and
`characterise_bir_false.validate_corpus_dir` verbatim.

### §0.3 Reuse-vs-new + what retires (acceptance #4)

- **Reuses verbatim (no change):** the L0/L1 grid primitives (`grid_score_regions` et al.),
  `classify_pair`, `align_*`/`three_way_classify`/`_dcml_time_spans` (`compare_analyses`), the
  `_our_key_tonic`/`_dcml_key_tonic` key parsers, `dcml_parser` WiR parse + `find_wir_file`,
  `characterise_bir_false.validate_corpus_dir`, and the frozen per-preset corpus + regen/verify
  machinery.
- **New:** the measurement driver (`tools/a8_rebaseline_measure.py`) + this report. Nothing else.
- **Retires:** nothing. The batch-region gate (53/24/53 case-identity + two-tier policy) remains
  THE gate until the user ratifies the re-baseline (this is roadmap retirement item **R10**, which
  fires with G2/Stage 5, carrying the case-identity + two-tier policy over).
- **Kept scratch script — worth keeping:** `tools/a8_rebaseline_measure.py` is the A-8 measurement
  instrument (it serves the eventual re-baseline + the E0/G2 measurability); committed at `fd8ea88c0f`.
  The full per-cell enumerations it writes (§5) are large and left as regenerable scratch outputs
  (the committed driver is their pin).

---

## §1 — The pinned candidate-gate definition (Task 1)

The measurement instantiates the following definition **exactly**. Any deviation it would need was a
STOP, not an edit; none was required (§6).

### §1.1 The unit — union-of-boundaries cell, duration-weighted

The scoring unit is the **union-of-boundaries cell**: overlay both sides' region boundaries (our
`.ours.json` region `[start_tick,end_tick)` boundaries ∪ the DCML/WiR row tick-span boundaries, the
latter via the pinned `_dcml_time_spans`). Over each resulting half-open cell `[t_i,t_{i+1})` **both**
sides are piecewise-constant by construction, so the cell is scored once by point-sampling both sides
at `t_i` and weighting the verdict by the cell duration `(t_{i+1}-t_i)`. This is exactly the design
`precision_metric_design.md` §2 unit as implemented by `grid_score_regions` (OQ-G1 resolved to
union-of-boundaries = exact). **music21 is NOT a boundary source** — the unit is ours∪DCML; music21
enters only as the variant-(a) filter, sampled pointwise (§1.3). Cells with no active ours-or-DCML
span, or where the DCML row has no resolvable root, are charged **unscored** (never mis-bucketed as an
error) — the same gap handling `grid_score_regions` uses.

The reported number for any respect is a **duration fraction** = Σ dur(cells in the bucket) / Σ dur(all
scored cells) — the fraction of *musical time*, which is segmentation-invariant (refining either side
splits a cell into sub-cells carrying the same labels, leaving the duration unchanged).

### §1.2 The three scored respects (reported separately, never collapsed)

Per cell, three independent verdicts, each reported as its own duration fraction:

| respect | agreement condition (per cell) | source |
|---|---|---|
| **root** | `our.root_pc == dcml.root_pc` (⇔ NOT the `root_err` bucket) | `classify_pair` |
| **RN** | `classify_pair` bucket ∈ {`exact`,`partial`} (= the design-doc `rn_agree`) | `classify_pair` |
| **key** | `_our_key_tonic(our.key) == _dcml_key_tonic(dcml.global_key)` — `(tonic_pc, is_major)` identity | ported key parsers |

The full 5-bucket `classify_pair` decomposition (`exact / partial / key_disagree / quality_disagree /
root_err`) is reported alongside as the underlying structure — but the three respects are the gate-
successor candidates and are **not** collapsed into it. The **key** respect is deliberately the
*independent global-key identity* comparison (the `--key-breakdown` S1 axis), **not** the `key_disagree`
bucket (which is a narrower root✓∧quality✓∧degree✗ slice); our-key parse-failures (`keyfail`) are
reported separately and never hidden in a bucket.

### §1.3 The two adjudication variants (both measured)

- **(b) human-only / DCML-only** — no music21 anywhere. Score ours directly vs the WiR human
  annotation at every cell. **This is the clean variant** the C2 mandate points to (music21 is not
  ground truth). Denominator = scores with a WiR annotation.
- **(a) legacy music21∩DCML "genuine" filter** — for continuity/mapping to the current gate. A cell is
  a "genuine" failure iff it passes the legacy filter: `three_way_classify(our_root, m21_root_at_t_i,
  dcml_root) == 'music21_dcml_agree'` **and** `bass_is_root == False` (matching the gate's
  `if bass_is_root: continue`). music21's root is sampled **pointwise** at `t_i` (consistent with how
  ours and DCML are sampled), which differs slightly from the legacy region-level max-overlap
  alignment — a difference that itself surfaces two cases (§3.2), reported not hidden.

  **Structural property of variant (a), measured and stated:** the legacy filter is **root-defined**
  (`three_way_classify` takes three *root* pcs; music21 does not reliably emit RN or key, and the gate
  never used them). `music21_dcml_agree` requires `our_root ≠ dcml_root`, so variant (a) fires **only on
  root-disagreeing cells**. Consequently variant (a) can only adjudicate the **root** respect; on the RN
  and key respects it collapses to "the music21-corroborated root-failing subset" (its RN-fail duration
  equals its root-fail duration exactly — §2). Variant (a) is therefore the continuity anchor for the
  **root** respect; it is **not** a full RN/key adjudicator. Variant (b) is the honest RN/key measure.

### §1.4 Case identity on the new unit

Primary identity = **`stem@cellStartTick`** (the cell's `t_i`). Because a re-slice of the *other* side
only ADDS interior boundaries — splitting one failing cell into contiguous failing sub-cells with
identical labels — the failing **span** and its **duration** are invariant, and the earliest sub-cell
retains `t_i`. To give a fully re-slice-stable identity the instrument also emits the **failing run**:
maximal contiguous same-`(stem, our_root, dcml_root)` failing cells merged into one
`stem@runStartTick` (invariant to interior re-slicing on either side) — this is the closest analogue of
the current gate's `stem@regionStartTick`. Both are emitted (§5).

### §1.5 Two-tier class-(a)/(b) carry-over, decided per CELL

The same structural test as the current policy — is the sonority's root **pitch-class-decidable** — is
applied to OUR sonority at each cell, from its pitch-class set:

- **class (a)** (pc-UNDECIDABLE root — the coin-flip churn) iff the pc-set is **transposition-invariant**
  (fully-diminished 7th = T3-invariant, augmented triad = T4-invariant, whole-tone = T2-invariant —
  root undefined by symmetry) **or** matches the **ø7/m6 share-tone collection** `{r,r+3,r+6,r+10}` (an
  Eø7 and a Gm6 are the same pc-set, root undecidable between the two spellings — CLAUDE.md's
  bwv291/bwv352 class).
- **class (b)** (pc-DECIDABLE root — triads, dom7, etc.) = everything else.

Per policy guardrail (2) this test is deliberately **conservative** — it fires class (a) only where the
pc-set is *provably* root-ambiguous from OUR pc-set alone (WiR carries no DCML pc-set, so a share-tone
case outside the two templates is counted class (b), the safe direction for a gate). **Independent
validation:** on the batch gate's own 53 Baroque cases the test yields **28 class-(a) = 52.8%**, matching
CLAUDE.md's "symmetric fully-diminished-7th ≈53% of Baroque" to the point, and it flags the named
founding-evidence cases (`bwv272@4320`, `bwv289@20160`) as class (a) [probe].

---

## §2 — The counts (Task 2.2) — one table, preset × variant × respect

Duration in ticks; fraction = of **scored** duration. Coverage (all presets): **326/352** ours files
carry a WiR human annotation (26 have none → excluded from BOTH variants, never silently folded into a
/352); all 326 covered scores also have music21, so the variant-(a) and variant-(b) score denominators
are **both 326**. (CLAUDE.md/roadmap quote 326/**353**; the frozen corpus at this HEAD is 352 scores,
hence 326/352 — the 27-vs-26 uncovered count moves with the one absent score.)

### §2.1 Scored substrate

| preset | scored_dur | unscored_dur | covered scores |
|---|---|---|---|
| Baroque | 8,293,680 | 192,720 | 326/352 |
| Jazz | 8,291,520 | 194,880 | 326/352 |
| Default | 8,293,680 | 192,720 | 326/352 |

### §2.2 Variant (b) — DCML-only (the clean variant), duration-weighted **agreement** per respect

| preset | root agree | RN agree | key agree | (key parse-fail) |
|---|---|---|---|---|
| **Baroque** | **63.32 %** | **44.56 %** | **68.11 %** | 0.09 % |
| **Jazz** | **62.37 %** | **42.40 %** | **64.43 %** | 0.13 % |
| **Default** | **63.22 %** | **44.40 %** | **67.50 %** | 0.40 % |

Underlying 5-bucket duration decomposition (variant b, % of scored):

| preset | exact | partial | key_disagree | quality_disagree | root_err |
|---|---|---|---|---|---|
| Baroque | 32.77 | 11.80 | 15.72 | 3.04 | **36.68** |
| Jazz | 31.11 | 11.29 | 16.54 | 3.43 | **37.63** |
| Default | 32.73 | 11.68 | 15.83 | 2.99 | **36.78** |

(root_agree = 1 − root_err; rn_agree = exact + partial. root **dis**agree = 36.68/37.63/36.78 %; RN
disagree = 55.44/57.60/55.60 %; key disagree = 31.79/35.44/32.10 %.)

### §2.3 Variant (a) — music21-filtered "genuine", duration-weighted **failure** per respect

| preset | root-fail dur | root-fail % | root-fail cells | root-fail runs | RN-fail dur | key-fail dur |
|---|---|---|---|---|---|---|
| **Baroque** | 560,280 | **6.76 %** | 1,643 | 1,513 | 560,280 (=root) | 158,880 (1.92 %) |
| **Jazz** | 465,840 | **5.62 %** | 1,357 | 1,252 | 465,840 (=root) | 165,720 (2.00 %) |
| **Default** | 554,400 | **6.68 %** | 1,625 | 1,497 | 554,400 (=root) | 160,200 (1.93 %) |

Note **RN-fail dur = root-fail dur** exactly, per §1.3: the root-defined music21 filter only fires on
root-disagreeing cells, so every genuine cell also fails RN; key-fail is the subset that *also*
disagrees on key. **The music21 filter discards ~82 % of the human-GT root-disagreement time** (variant
b 36.68 % → variant a 6.76 %, Baroque) — the C2 "music21 is an algorithm, not ground truth; the filter
discards most of the human-adjudicated error mass" property, re-measured at this unit.

---

## §3 — The mapping table (Task 2.3): every current gate case located on the new unit

For each of the 53/24/53 current gate cases (`stem@regionStartTick`), the instrument finds the grid
cells overlapping its region span and records whether it remains failing on the **root** respect under
each variant [probe `{preset}_mapping.json`]:

| preset | gate cases | still failing under (b) DCML-only | still failing under (a) music21-filtered | disappeared (b) | disappeared (a) |
|---|---|---|---|---|---|
| **Baroque** | 53 | **53** | 51 | **0** | 2 |
| **Jazz** | 24 | **24** | 23 | **0** | 1 |
| **Default** | 53 | **53** | 51 | **0** | 2 |

**Under variant (b) every current case maps to a still-failing cell — 0 disappear, all three presets.**
The current gate is a strict subset of the granularity-robust human-GT root-failing set.

**The variant-(a) disappearances — individually explained (adjudication effect, not unit effect).** Two
cases (`bwv269@20640`, `bwv429@24240`; Jazz has only the second) fail under (b) but not under (a). Both
are **class (b)**. Verified mechanism at the score-region level [probe]:

- `bwv269@20640` — our region `[20640,22080)` root=2 (D/F♯), bir=False. The **batch** gate paired it
  (region-max-overlap) to a 480-tick WiR slice root=6 that music21 *also* rooted 6 → `music21_dcml_agree`
  → flagged. **Pointwise** the union-of-boundaries cells are `[20640,21120)` (our 2 · m21 2 · dcml **7**)
  and `[21120,22080)` (our 2 · m21 **7** · dcml 6) → both `all_differ`. The region is root-wrong against
  *both* DCML readings (6 and 7), so it **still fails under (b)**; it only leaves the music21-corroborated
  subset because the small-overlap row that music21 happened to corroborate is not the pointwise-active
  label at the cell onsets.
- `bwv429@24240` — identical mechanism (our 4 = E/G♯; cells `all_differ` at every onset; region-max-
  overlap corroboration on a 240-tick slice).

So the 2/1/2 variant-(a) disappearances are an **artifact of the batch gate's region-level max-overlap
alignment** (it can find a small-overlap DCML row that music21 corroborates even when it is not the
region's dominant label), which the granularity-robust pointwise unit dissolves. They are **not** lost
from the human-GT metric (variant b keeps them). This is evidence *for* the robust unit, not a gap in it.

---

## §4 — The undercount ratios (Task 2.4) and the class split (Task 2.5)

### §4.1 Undercount — batch-region gate vs granularity-robust unit, **matched filter**

Holding the adjudication fixed (music21-filtered + BIR-false = the gate's own filter) and varying only
the unit (batch region → union-of-boundaries cell), i.e. variant (a) vs the batch gate:

| preset | batch gate (regions) | robust cells | robust runs | **cell ratio** | **run ratio** | duration ratio¹ |
|---|---|---|---|---|---|---|
| **Baroque** | 53 | 1,643 | 1,513 | **31.0×** | **28.5×** | 15.5× |
| **Jazz** | 24 | 1,357 | 1,252 | **56.5×** | **52.2×** | 30.8× |
| **Default** | 53 | 1,625 | 1,497 | **30.7×** | **28.2×** | 15.6× |

¹ duration ratio = variant-(a) root-fail duration ÷ Σ(batch-gate region durations) [D_batch = 36,240 /
15,120 / 35,520 ticks].

**The measured undercount is larger than the dossier's ~7× prediction, in the predicted direction, and
for an understood reason:** the dossier's ~7× was the **section (measure-aligned)** per-beat view; the
A-8 unit is the **union-of-boundaries** unit, which is *finer* than measure-aligned (it splits at every
onset/release on either side, including sub-beat), so it surfaces even more masked per-onset failure.
The run-count ratio (~28×) is the count of distinct contiguous failing events; the duration ratio
(~15×) is the segmentation-invariant view; the cell ratio (~31×) is the finest. All three quantify the
same fact: the batch gate's 53 regions cover a small fraction of the musical time that is actually
root-wrong under the identical filter — the granularity-robust unit surfaces the rest (chiefly failures
inside regions whose *dominant* music21 overlap agreed with us, so the batch gate never flagged them).

**Removing the music21 filter too (the full DCML-only picture)** widens it further: variant (b) has
**7,887 / 8,099 / 7,909** root-failing cells (36.68/37.63/36.78 % of scored time) — vs the gate's 53/24/53.

### §4.2 Class-(a)/(b) split of the candidate failing sets (per preset/variant)

Applying the §1.5 cell test to the **root**-failing sets (the respect where the two-tier policy lives):

| set | Baroque a / b | Jazz a / b | Default a / b | class-(a) share |
|---|---|---|---|---|
| **batch gate** (53/24/53 regions) | 28 / 25 | 7 / 17 | 28 / 25 | **52.8 / 29.2 / 52.8 %** |
| **variant (a)** cells (music21-filtered) | 75 / 1,568 | 62 / 1,295 | 75 / 1,550 | **4.6 / 4.6 / 4.6 %** |
| **variant (a)** duration | 28,440 / 531,840 | 23,880 / 441,960 | 28,440 / 525,960 | **5.1 / 5.1 / 5.1 %** |
| **variant (b)** cells (DCML-only) | 280 / 7,607 | 320 / 7,779 | 296 / 7,613 | **3.6 / 4.0 / 3.7 %** |
| **variant (b)** duration | 107,040 / 2,934,800 | 122,880 / 2,997,520 | 112,080 / 2,938,400 | **3.5 / 3.9 / 3.7 %** |

**Measured finding (stated, not recommended):** the two-tier policy's class-(a) prominence (≈53 % of the
Baroque gate) is a **region-count property of the small music21-filtered residual** — the "tiny reachable
corner." On the granularity-robust unit the class-(a) symmetric/share-tone churn is **~5 % (variant a) /
~3.6 % (variant b)** of root-failing time; **class-(b) pitch-class-decidable-root functional errors
dominate overwhelmingly (~95 %+) under both variants.** (Consistent with the headroom dossier's "95 % of
root errors are functional, not vertical," here re-measured at the robust unit.) A re-baselined gate at
this unit would therefore be governed almost entirely by the class-(b) count the two-tier policy already
names as the meaningful, must-not-increase quantity — the class-(a) coin-flip term becomes a small
minority, not the majority it is on the batch residual.

---

## §5 — Where the full enumerations live (Task 2.2 / 3)

The full per-cell and per-run failing enumerations (too large for this report) are written by the
committed driver to a scratch dir and are **regenerable deterministically** via
`python tools/a8_rebaseline_measure.py --out-dir <dir>` (the driver is their pin). Line counts
[probe], for the run of this report (dir `…/scratchpad/a8_out/`):

| file (per preset ∈ {baroque,jazz,default}) | Baroque | Jazz | Default |
|---|---|---|---|
| `{p}_variant_b_root_fail_cells.txt` (identity `stem@cellStartTick`) | 7,889 | 8,101 | 7,911 |
| `{p}_variant_b_root_fail_runs.txt` (identity `stem@runStartTick`) | 6,875 | 7,038 | 6,890 |
| `{p}_variant_a_root_fail_cells.txt` | 1,645 | 1,359 | 1,627 |
| `{p}_variant_a_root_fail_runs.txt` | 1,515 | 1,254 | 1,499 |
| `{p}_mapping.json` (the §3 per-case rows) | — | — | — |
| `summary.json` (all §2/§4 aggregates) | — | — | — |

(cell/run files carry a 2-line header, so entry counts are line-count − 2.)

---

## §6 — Stop-condition disclosures (per the instruction)

- **No STOP tripped.** The existing primitives **can** express the pinned definition without
  modification: the driver reuses `classify_pair`/`grid_score_regions`/`_active_index_at`/
  `_dcml_time_spans`/`three_way_classify`/`_our_key_tonic`/`_dcml_key_tonic` verbatim as orchestration,
  and its variant-(b) decomposition is proven byte-identical to `grid_score_regions` on every piece
  (§0.2). No `compare_rn.py` / primitive change was needed — had one been, it would have been a STOP.
- **The current gate reproduced 53/24/53** at the anchor, set-diff empty, before and after (§0.1) — the
  anchor step held.
- **The mapping table accounts for every current case** (§3): 0 disappear under (b); the 2/1/2
  variant-(a) disappearances are individually explained and verified (adjudication/alignment effect).
- **All three qualifiers are honestly stated in cell terms:** granularity (§4.1 — the duration-invariant
  unit + measured undercount), adjudication (§1.3/§2.3 — both variants, and the measured root-only reach
  of the music21 filter), coverage (§2 — 326/352 explicit, 26 excluded, never silently folded).
- **One honest limitation, surfaced not hidden:** variant (a)'s music21 leg is a **root-level,
  alignment-sensitive** filter — it cannot adjudicate the RN/key respects, and its pointwise sampling
  differs from the legacy region-max-overlap alignment (the source of the 2/1/2 disappearances). This is
  itself measured evidence that variant (b) — DCML-only — is the sound RN/key measure. **No inference
  problem is declared or fixed here; this is a metric measurement only.**

---

## §7 — Decision surface (what the user is asked to ratify)

**No recommendation is made** — the ratification is the user's. The measured facts lay out the choice:

1. **Unit.** The granularity-robust **union-of-boundaries, duration-weighted** cell (the A-8 unit, the
   pinned `grid_score_regions` substrate). It is segmentation-invariant and surfaces the ~15–56× per-
   onset failure the batch region gate masks under the identical filter (§4.1).
2. **Adjudication variant.** Two are on the table, both measured:
   - **(b) DCML-only** — the clean, human-only measure; adjudicates all three respects; **0 current
     cases disappear**; the C2-mandated non-music21 objective.
   - **(a) music21-filtered** — the continuity anchor for the **root** respect only (root-defined
     filter); reproduces the batch gate's 53/24/53 continuity but cannot measure RN/key and is
     alignment-sensitive (2/1/2 disappearances).
3. **Respect set.** root / RN / key measured separately (§2). Root and key have clean per-cell
   definitions on both variants; RN is `exact+partial`. The gate successor may adopt one respect (root,
   as today), or a multi-respect objective — the numbers for each are provided; **no collapse is imposed.**
4. **The numeric baseline** to adopt as the re-baselined gate (per §2): e.g. under **(b) DCML-only** the
   root-agree baseline is **63.32 / 62.37 / 63.22 %** (root-disagree 36.68 / 37.63 / 36.78 %), key-agree
   **68.11 / 64.43 / 67.50 %**, rn-agree **44.56 / 42.40 / 44.40 %**; under **(a)** the genuine root-fail
   baseline is **6.76 / 5.62 / 6.68 %** of scored time (1,513 / 1,252 / 1,497 failing runs).
5. **Identity form.** `stem@cellStartTick` (cell) or the re-slice-stable `stem@runStartTick` (run); both
   emitted. The two-tier class-(a)/(b) policy carries over per-cell (§1.5) — and on this unit
   **class-(b) functional errors are ~95 %+** of the failing set (vs the batch residual's ≈53 % class-(a)),
   so the re-baselined gate is governed by the class-(b) count the policy already treats as the hard,
   must-not-increase quantity (§4.2).

The batch-region gate (53/24/53 case-identity + two-tier policy) **remains THE gate** until this
re-baseline is deliberately ratified (roadmap R10).

---

*Drafted by CC, 2026-07-03, measurement base HEAD `fd6f499162`, corpus `0dd64660f4`. Instrument
`fd8ea88c0f`. Read-only: the only repo writes are the driver + this report. Local, unpushed, fork-only.*
