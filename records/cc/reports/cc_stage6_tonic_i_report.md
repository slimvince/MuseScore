# CC Report — Stage 6-tonic-i: the tonicization (applied-dominant) labeler — BUILT + MEASURED

> **HELD — no commit.** Implements the ratified `docs/stage6_functional_layer_design.md` narrow first
> slice, with the **measure-before-wire** refinement: the labeler is built and its realized quality is
> MEASURED diagnostically, with production RN output UNCHANGED (byte-identical). Wiring is 6-tonic-ii.
> Base HEAD `2245aedf82`. Every number tagged `[probe]` (ran it) / `[code]` (read source) / `[oracle]`
> (DCML When-in-Rome ground truth). Zone: `src/composing/` (the labeler) + `tools/` (diagnostic +
> measurement). Nothing committed.

---

## §0 — TL;DR

| Item | Result |
|---|---|
| **Labeler** | new composing pass `analysis/function/tonicizationlabeler.{h,cpp}` — distinct from `harmonicfunctionlayer`; PRODUCES a `<numeral>/<degree>` label, mutates nothing `[code]` |
| **Diagnostic** | `batch_analyze --dump-tonicization` (default OFF) + `tools/cc_tonicization_measure.py` `[code]` |
| **Byte-identity** | BIR **57 / 23 / 57** (Baroque/Jazz/Default), snapshots **11/11** zero golden diffs, composing **531**, notation **57** `[probe]` |
| **False-label rate (raw, correct-key)** | **78.0 %** (465/596) `[probe][oracle]` — high |
| **...decomposed** | **91.8 %** of the false positives (427/465) are the **tonicization-vs-MODULATION boundary** (DCML annotates a local-key modulation where we read a tonicization — the design's explicitly-DEFERRED sub-step); only **6.4 %** (38/596) are **genuine** plain-diatonic false labels `[probe][oracle]` |
| **S1 recall** | **41.2 %** any-target (131/318), **40.3 %** target-exact (128/318); **+17.0 %** NEW over the existing production labeler's 29.2 % `[probe][oracle]` |
| **Label-vocab contract** | the labeler emits the **same `<numeral>/<degree>` form the existing `formatRomanNumeral()` already emits** (V7/x, viio/x, viiø7/x) — which `compare_rn.classify_pair` already credits; NOT re-invented `[code]` |
| **★ Cross-layer finding** | the binding false-label metric is **dominated by a not-yet-built input** (tonicization-vs-modulation / KeyArea). The predicate itself is sound (6.4 % genuine error). |
| **Branch recommendation** | **Do NOT wire 6-tonic-i as-is** (raw false-label 78 % against DCML). The predicate's guards are validated; the prerequisite is the **modulation/KeyArea discriminator** (a deferred sub-step), not a guard refinement. See §7. |

---

## §1 — The labeler at source (inputs + predicate + the false-positive guards)

New file `src/composing/analysis/function/tonicizationlabeler.{h,cpp}` `[code]`. A **new, higher
sequence-labeling pass** over the decoded chord+key path — *not* inside `harmonicfunctionlayer` (the
chord-COMPETITION layer). Per the layer-by-layer audit method it **assumes its inputs correct** and
**legitimately consumes the resolved key** (Stage 6 runs after key resolution — this is NOT circular,
unlike the cadence detector which had to stay key-agnostic).

**Input (`TonicizationRegionInput`, per region):** `rootPc`, `quality`, `hasMinorSeventh`,
`hasDiminishedSeventh`, `pitchClassMask`, and the **prevailing resolved key** `keyTonicPc`,
`keyIsMajor`, `keySignatureFifths`. It produces a `TonicizationLabel` per region; it does **not**
mutate root/quality/key — only PRODUCES the label.

**Predicate (for each consecutive pair a = regions[i] → b = regions[i+1], in a's prevailing key):**
1. both carry a confident root (`rootPc ≥ 0`);
2. the tonicized degree **d = root(b)** must be a **diatonic scale degree** of the key (named via the
   signature's Ionian collection rooted at the tonic — for Aeolian this is the natural-minor collection)
   and **d ≠ tonic** (plain V→I is excluded);
3. **chromatic raised-LT guard (FP guard #1):** the leading tone of d, `lt = (pc(d)+11) mod 12`, must be
   an **accidental** — outside the key signature's diatonic collection. This is the discriminator that
   distinguishes a genuine applied chord from ordinary diatonic motion (e.g. a diatonic VII→III in a
   minor key has NO chromatic alteration → not a tonicization — DCML agrees);
4. **resolution guard (FP guard #2):** the next region resolves TO d (implicit: d IS root(b)); plus
   - **applied dominant V/d, V7/d:** a is Major quality, `root(a) ≡ (pc(d)+7) mod 12`, and lt (= a's major
     third) is physically present in a's pitch mask; `hasSeventh = hasMinorSeventh`;
   - **applied leading-tone viio/d, viio7/d, viiø7/d:** a is Diminished/HalfDiminished, `root(a) ≡ lt`;
     `hasSeventh = hasDiminishedSeventh || hasMinorSeventh`.

These two guards are the design's §3 false-positive guards — the analogue of the cadence detector's
resolution + chromatic discriminators. The unit test `tonicizationlabeler_tests.cpp` (9 tests, all
green `[probe]`) pins each: V/V, V7/V, V7/ii (lowercase), viio/V, viio7/V, plus the four rejections —
**the diatonic VII→III-in-minor relative-major trap (FP guard #1)**, the tonic-target exclusion, the
deceptive V→vi, and a non-diatonic target.

---

## §2 — The label-vocabulary contract (confirmed at source, NOT re-invented)

Per the instruction, I confirmed the contract form at source rather than inventing it.

- **`compare_rn` already credits a correctly-emitted secondary** `[code` `compare_rn.classify_pair`,
  `normalise_rn`, `split_rn]`: `normalise_rn` strips paren figures but keeps the full suffix, so
  `split_rn("V7/ii")` → (`""`,`"V"`,`"7/ii"`); `classify_pair` then scores `ours_norm == dcml_norm` as
  **exact** when our RN string equals the DCML chord string (root-position), and **partial** (root +
  degree-case agree, string differs) for inversions. This resolves metric-design **OQ-L2**: the form is
  the standard `<numeral>/<degree>`, degrees as Roman numerals of the prevailing key, half-dim as `ø`.
- **DCML side** `[code` `dcml_parser]`: for WiR rntxt the `chord_symbol` is the full token (`V/vi`,
  `viio7/V`, `V6/5/IV`); `_split_rntxt_applied` isolates a trailing pure-degree target; `root_pc` is the
  primary resolved in the *effective* (relativeroot-folded) key — i.e. the **actual sounding root**, which
  already matches our `rootPitchClass` (the reason S1 sits in `key_disagree`, not `root_err`).
- **The labeler emits exactly the form the EXISTING `ChordSymbolFormatter::formatRomanNumeral()` already
  emits** `[code` `chordanalyzer.cpp:3315-3376]` — `V7/x`, `viio/x`, `viiø7/x`, UPPER/LOWER degree by the
  diatonic-triad third. So the new pass is consistent with the already-credited production vocabulary, not
  a parallel one. (One residual: minor-key **dominant** tonicizations come out `V/v` / `V7/v` from the
  natural-minor casing, where DCML sometimes writes `V/V`; a degree-casing convention note for 6-tonic-ii,
  not a predicate issue — it does not affect the target-pc-based binding metric.)

---

## §3 — ★ A production tonicization labeler ALREADY EXISTS (cross-layer finding)

`ChordSymbolFormatter::formatRomanNumeral()` **already emits secondary labels into the corpus**
`[code` `chordanalyzer.cpp:3315`; fed by `backfillNextRootPc` `regionanalyzer.cpp:180]`. It is gated on
`function.nextRootPc ≥ 0` (populated on the batch/corpus path), handles **V7/x** (dom7 only — *not*
plain major-triad V/x) and **viio/x** (dim/half-dim), and has **no chromatic-LT guard**. So part of S1 is
already covered in today's `.ours.json`: the measurement shows **29.2 %** of the S1 population already
carries a production applied label `[probe]`. The new labeler is therefore a *more complete + guarded*
proposal (adds the plain-triad V/x and the chromatic guard); its **marginal** new recall is **+17.0 %**
(54/318) `[probe]`. This is reported, not hidden — it reframes "S1 recovery" as marginal-over-production.

---

## §4 — Measurement (diagnostic, byte-identical) — the deliverable

Method `[code` `tools/cc_tonicization_measure.py]`: read the per-region `tonicizations` array that
`batch_analyze --dump-tonicization` appended to each `.ours.json` (Default preset corpus
`tools/corpus/default_6tonic`, 353/353), align our regions to the **When-in-Rome** Bach rntxt
[oracle] via the committed `compare_analyses.align_dcml_regions`, and classify each pair with REUSED
`compare_rn`/`dcml_parser` helpers. **326/353** stems have WiR coverage (27 have none — never folded
into a /353 division). Scope = the **correct-key subset** (our resolved key == DCML global key), where
this slice is pure-add.

### 4.1 False-label rate (the BINDING constraint) `[probe][oracle]`
```
labeler emitted /d (total)            : 828
  ... on correct-key regions          : 596
  ... wrong-key / unaligned (oos)      : 232
correct-key /d that ARE applied (TP)   : 131/596  (22.0% precision)
  ... AND target degree matches        : 128/596  (21.5% strict)
correct-key /d that are NOT applied    : 465/596  (RAW FALSE-LABEL RATE 78.0%)
  of which DCML reads a MODULATION      : 427  (91.8% of FPs; 409 with our target == DCML local tonic)
  of which DCML is plain DIATONIC       : 38   (8.2% of FPs — the GENUINE false labels)
ADJUSTED false-label rate (diatonic)   : 38/596  (6.4%)
```
**Interpretation.** The raw 78 % is alarming, but **91.8 % of it is the tonicization-vs-MODULATION
boundary**: at those regions DCML's annotator assigned a **local key** (local ≠ global) and wrote the
chord as a local-key numeral (`V`, `V6`, `V7`, `V6/5`), while our labeler — with the home key still
resolved — read the *same harmonic event* as an applied chord `V/d`. In **409** of the 427 the degree we
tonicized **equals DCML's local tonic** — i.e. our `V/d` and DCML's `[localkey = d] V` are the same
event, two notations. The top patterns confirm it: `V/V→V` (70), `V/vi→V` (25), `V/V→V6` (23),
`V7/V→V7` (17), `V7/V→V6/5` (14). **The genuine predicate error is 6.4 %** — and even those 38 are
dominated by `V/d→I` segmentation/alignment artifacts (our applied region overlapping a DCML tonic row),
not predicate defects.

### 4.2 S1 coverage / recovery (recall) `[probe][oracle]`
```
S1 population (DCML applied, correct-key)   : 318
  labeler catches (any target)              : 131/318  (41.2%)
  labeler catches (target matches)          : 128/318  (40.3%)
  already covered by production RN           :  93/318  (29.2%)
  NEW (labeler catches, production did not)  :  54/318  (17.0%)
```
**Misses (187/318)** are dominated by **inversions** the root-position-figure labeler + segmentation
miss: `V6/5/V` (17), `viio7/V` (14), `V2/IV` (13), `V6/III` (11), `V6/vi` (9), `V7/IV` (7). These are
recall ceilings of (a) emitting only root-position figures and (b) the strict "next region IS the target"
resolution requirement under our coarser segmentation.

### 4.3 Scope note
Measured on the correct-key subset per the instruction (pure-add there). The wrong-key/relative-pair
floor (232 emissions on wrong-key regions) is out of scope — the key layer's problem (Stage 4).

---

## §5 — Byte-identity gate (6-tonic-i is measurement-only) `[probe]`

The labeler is diagnostic-only (`--dump-tonicization` default OFF; the resolver/formatter never call it).
Proof, all with the NEW binary:

| Gate | Result |
|---|---|
| BIR Baroque | **57** (case-identity set, `characterise_bir_false --corpus-dir tools/corpus/baroque`) |
| BIR Jazz | **23** |
| BIR Default | **57** |
| `pipeline_snapshot_tests` | **11/11**, zero golden diffs (1 always-skipped report generator) |
| `composing_tests` | **531** (was 522; +9 new labeler tests) |
| `notation_tests` | **57** |

No production RN moved (snapshots pin P1–P4 RN strings). The labeler did not leak into output.

---

## §6 — False-positive characterization (what's misfiring)

Two distinct populations, NOT one noise pile:
1. **Tonicization-vs-modulation boundary (427, 91.8 % of FPs) — DEFERRED sub-step, partly a convention
   difference.** DCML expresses tonicizations as **local-key modulations**; we express the same event as
   an applied chord. Against DCML-as-GT these register as "false," but the readings are musically
   equivalent (our target == DCML local tonic in 409/427). The labeler cannot tell tonicization from
   modulation without consuming **KeyArea / local-key spans** — which the design (§3) explicitly defers to
   a later sub-step and which 6-tonic-i does not build.
2. **Genuine diatonic false labels (38, 6.4 %).** Mostly `V/d→I` (our applied-chord region overlapping a
   DCML tonic row) — segmentation/alignment artifacts and a handful of real misreads. Low.

---

## §7 — Branch recommendation

The instruction's rule: *low false-label + worthwhile recall ⇒ 6-tonic-ii; high false-label ⇒ refine the
guards.* The raw false-label rate against DCML is **78 % → do NOT wire 6-tonic-i as-is.** But the
diagnosis matters for *what* to do next:

- **The predicate's guards are SOUND** — the genuine (plain-diatonic) false-label rate is **6.4 %**, and
  the chromatic-LT guard correctly rejects the relative-major / diatonic-motion trap (unit-pinned, and the
  39-of-465-only-genuine split confirms it on corpus). The design's FP guards are **validated**.
- **The binding metric is dominated by a not-yet-built input (cross-layer finding / §8 stop condition).**
  91.8 % of the "false labels" are the **tonicization-vs-modulation** distinction — the explicitly-deferred
  sub-step that needs **KeyArea / local-key span** consumption. This is a **prerequisite, not a guard
  refinement**: no tightening of the applied-chord predicate can fix it, because the chords ARE applied
  dominants — the disagreement is purely whether to *notate* them as tonicization or modulation, which
  DCML decides from local-key context we do not yet consult.

**Recommendation:** Do **not** proceed straight to 6-tonic-ii wiring. **Re-scope the next step to the
tonicization-vs-modulation discriminator first** (consume KeyArea / local-key spans so the labeler emits
`/d` only where our analysis is NOT treating d as a local key), then re-measure the false-label rate
against DCML. Separately, lift the recall ceiling by (a) emitting inversion figures (V6/5, V2, …) and
(b) relaxing the strict "next region == target" resolution requirement under coarse segmentation. The
labeler + diagnostic stand as a **byte-identical instrument** (like the cadence anchor) feeding that work.

A secondary, genuine **convention question** for any wiring: against DCML's modulation-heavy annotation
the metric penalizes a defensible tonicization reading even when musically equivalent (our target ==
DCML local tonic). The label-vocabulary contract should record whether 6-tonic-ii aligns *to* DCML's
modulation choice or accepts the partial-credit (emitting `V/d` where DCML writes local-key `V` scores as
`partial`, i.e. still rn_agree, not a regression).

---

## §8 — Stop-condition disclosures
- **High false-label rate FIRED** (raw 78 %) → reported as the slice's correctness gap; **not**
  recommending wiring a noisy labeler. The decomposition (6.4 % genuine) is reported, not used to wave the
  raw number away.
- **"Needs a richer key/segmentation input than exists" FIRED** → surfaced as the §6/§7 cross-layer
  finding (tonicization-vs-modulation needs KeyArea; recall ceiling needs inversion + segmentation), not
  papered over.
- Production RN / byte-identity did **not** move (BIR 57/23/57, snapshots 11/11) → the labeler did not leak
  into output; 6-tonic-i stayed measurement-only.
- `compare_rn` secondary crediting was **confirmed at source and matched**, not re-invented or edited.

---

## §9 — Files (HELD, uncommitted)
- `src/composing/analysis/function/tonicizationlabeler.h` / `.cpp` — new labeler pass
- `src/composing/analysis/CMakeLists.txt` — register the new pass
- `src/composing/tests/tonicizationlabeler_tests.cpp` + `CMakeLists.txt` — 9 unit tests
- `tools/batch_analyze.cpp` — `--dump-tonicization` diagnostic (default OFF)
- `tools/run_bach_preset.py` — `--dump-tonicization` passthrough
- `tools/cc_tonicization_measure.py` — the measurement script
- `cc_stage6_tonic_i_report.md` — this report

*Drafted by CC, 2026-06-15, base `2245aedf82`. HELD — no commit.*
