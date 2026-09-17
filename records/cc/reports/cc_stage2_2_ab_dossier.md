# CC Stage 2.2-i — Batch section-level A/B + re-baseline decision dossier

**Run scope:** exploration + A/B characterization only. **No behavior committed.** Working-tree
prototype: `tools/batch_analyze.cpp` (`--section-level`, kept for 2.2-ii). All other prototypes
(`tools/run_bach_preset.py`, `tools/compare_rn.py`) reverted to HEAD; scratch scripts listed in §7
and removed. HEAD at run start: `8598cbd245` (Stage 2.1, uncommitted in working tree per that report).

Every quantitative claim is tagged **[probe]** (ran it) or **[code]** (read the source).

---

## §1 — F-3 provenance: where "24/13" and "35/7" come from

**Resolved.** Both headline pairs are produced by **`tools/analyze_inversion_errors.py`**, in its
"Three-way music21_dcml_agree genuine errors" table — the `bassIsRoot=true` / `bassIsRoot=false`
split. **[probe]:**

| invocation | BIR=true (1st number) | BIR=false (2nd number) |
|---|---|---|
| `analyze_inversion_errors.py` (flat `tools/corpus`, Baroque) | **24** | **13** |
| `analyze_inversion_errors.py --ours-dir tools/corpus/jazz` | **35** | **7** |

- The **first** number (24 / 35) = `genuine_bir_errors` = `classify(ours,m21).category=='chord_disagree'`
  ∧ `bassIsRoot==True` ∧ `three_way_classify=='music21_dcml_agree'` (`analyze_inversion_errors.py:145-147`) **[code]**.
- The **second** number (13 / 7) = `genuine_nonbir_errors` (same filters, `bassIsRoot==False`).
- **`characterise_bir_false.py` reproduces ONLY the second number** (13 Baroque, 7 Jazz) — it
  `continue`s on `our_r.bass_is_root` (`:162`), so it never computes the 24/35. **[probe]** both
  per-preset dirs: `TOTAL genuine BIR=false: 13` (Baroque), `7` (Jazz).

So the Stage-1d F-3 "the 24 is not produced by characterise_bir_false.py / provenance untraced" is
now closed: the 24/35 is the `bassIsRoot=true` cell of `analyze_inversion_errors.py`'s three-way
split. The memory note `reference_bir_metric_scripts.md` ("24/13 headline = characterise_bir_false.py")
is **imprecise** and should read: *the 13/7 (BIR=false) come from characterise_bir_false.py; the full
24/13 (35/7) pair comes from analyze_inversion_errors.py.*

**Caveat [code]:** `analyze_inversion_errors.py:93` reads `{stem}.music21.json` from the hardcoded
flat `_CORPUS_DIR` regardless of `--ours-dir`. Harmless today — music21 JSON is preset-independent
and **byte-identical** across `tools/corpus`, `…/jazz`, `…/baroque` ([probe] `diff -q` on 3 stems) —
but fragile (see §5 rider 1). Recommended STATUS line:

> *Baroque 24/13 and Jazz 35/7 are the `analyze_inversion_errors.py` three-way genuine split
> (bassIsRoot true/false). `characterise_bir_false.py` independently reproduces the 13/7 BIR=false
> half. They share the lenient-OR `align_regions` + `three_way_classify` comparator
> (`compare_analyses.py`).*

---

## §2 — Section-level mapping: what `analyzeSection` changes

**Caller mapping (Option D seam — no `src/` change needed):** batch already computes the
HarmonicRegion stream `regions = cra::analyzeRegions(...)` inside `analyzeScore` (with batch's
**preset** opts: `chordPrefs`, `onsetBoundaryThreshold=0.25`, `excludeLookAheadOnDenseStart=true`,
`pass1MinDistinctPcsForCandidate=1`). The prototype feeds that exact stream to
`analysis::analyzeSection(score, startTick, endTick, excludeStaves, regions)` and rebuilds
`AnalyzedRegion` JSON from `section.regions`. `composing_analysis` is already linked to
`batch_analyze` and contains `sectionanalyzer.{cpp,h}` (Stage 2.1) → **the Option-D seam suffices;
the stop condition "src change needed" does NOT apply.** [code]/[probe build].

**What `analyzeSection` CHANGES vs the raw region stream** (fields that reach `.ours.json`):

| Mechanism (sectionanalyzer.cpp) | Field changed | Notes |
|---|---|---|
| Pass-1 measure layout (`for Measure*` loop) | **ticks / region count** | every region clipped to `[measureStart,measureEnd)`; same-identity adjacent regions merged within a measure |
| Pass-1 gap-tone insertion (`inferGapRegion`) | **root / quality / bass / ticks** (NEW regions) | gap chords analyzed with `kDefaultChordAnalyzerPreferences` (NOT preset) or `inferSparseGapChord` |
| Pass-4 `refineSparseChordQualityFromKeyContext` | **quality only** (Unknown→diatonic triad) | root NEVER reassigned; dense regions untouched |
| Pass-4 `stabilizeHarmonicRegionsForDisplay` | **key** (keySignatureFifths/mode) → `degree`, `diatonicToKey` | root NOT changed |

**Purely additive** (do not touch root/quality/bass/ticks of existing regions): `keyAreas` /
`keyAreaId`, `hasAssertiveExposure`. **Cadence markers / pivot labels are NOT emitted by
`analyzeSection`** — `detectCadences`/`detectPivotChords` are separate functions requiring a
selection-count context the batch path lacks; the prototype does not emit them (schema decision → §5).

**Root can change ONLY through gap-region insertion (new regions); it is never reassigned on an
existing dense region.** This is the structural reason the BIR root-metric is barely moved by genuine
analysis (see §3).

**Prototype isolation choice (and its limit):** the prototype sources Pass-0 from batch's **preset**
`analyzeRegions` (Option b), so the A/B isolates the *section-pass delta*. The **true** user-facing
notation Pass-0 (`analyzeHarmonicRhythm`, `notationharmonicrhythmbridge.cpp:116-133`) instead uses
`kDefaultChordAnalyzerPreferences` and `excludeLookAheadOnDenseStart=false` [code]. So "batch
section-level" measures *batch-preset Pass-0 + section passes*, which is **closer to** but **not
byte-identical to** the real user path — the preset-chordPrefs divergence remains (a 2.4 finding, §7).

**Verification [probe]:**
- Flag **OFF** == HEAD byte-identical: `bwv244.15`, `bwv102.7`, `corelli` all `diff`-clean vs the
  committed corpus `.ours.json`.
- Builds clean; `test_batch_analyze_regressions.py` → `batch_analyze regressions passed`.
- Flag ON sane: `bwv244.15` 31→31 regions (a spurious `Dadd9` sub-region merged into `D/F#`).

---

## §3 — The A/B (the heart)

### §3.1 Counts + identity sets

| Preset | metric | OFF (batch) | ON (section) | identity-set change |
|---|---|---|---|---|
| Baroque | BIR=false | **13** | **265** | +252 |
| Baroque | BIR=true | **24** | **393** | +369 |
| Jazz | BIR=false | **7** | **245** | +238 |
| Jazz | BIR=true | **35** | **493** | +458 |

OFF identity sets reproduce the gate exactly: Baroque BIR=false 13, Jazz BIR=false 7 (the documented
`{bwv244.15, 245.17, 245.40, 422, 432, 45.7, 74.8}`). [probe]

### §3.2 Per-case mechanism — 99–100% is a measurement-granularity artifact

For every ON BIR case I located the OFF region covering the same tick and compared roots [probe]:

| Preset | metric | total ON | **artifact** (root unchanged vs OFF) | **genuine** (root changed) |
|---|---|---|---|---|
| Baroque | BIR=false | 265 | **262** | **3** |
| Baroque | BIR=true | 393 | **393** | **0** |
| Jazz | BIR=false | 245 | **243** | **2** |
| Jazz | BIR=true | 493 | **492** | **1** |

**The chord analysis is essentially unchanged.** Region count grows only **1.11×** (Baroque
11267→12490) / **1.12×** (Jazz 10910→12230); mean region duration 815→741 / 842→757 ticks — **no
gross distortion** (well under the 2× stop threshold). The 13→265 explosion is **not** the analyzer
getting worse; it is the section pass's **measure-aligned regions** surfacing per-beat DCML
disagreements that the batch path's coarser cross-barline regions were **masking**.

**Mechanism, traced (bwv10.7 m20 b1, tick 36480) [probe]:**
- OFF: one region `[36000,36960]` = `Bb/C` (root Bb=10), spanning the barline. `align_dcml_regions`
  pairs it (max tick-overlap) with the *pre-downbeat* DCML region where Bb agrees → **not counted**.
- ON: Pass-1 splits at the barline → `[36000,36480]` + `[36480,36960]`, both still `Bb/C` (**root
  unchanged**). The second now aligns cleanly to DCML `iv` (Cm, root 0) at the downbeat → **BIR=false
  surfaces**.

So the metric, at section granularity, stops undercounting: a single coarse region got one
comparison (to an agreeing beat); two measure-aligned regions get a comparison per beat. The **user
sees** the `Bb/C` label spanning that downbeat — so section granularity is the more faithful measure
of *user-visible* error rate. This is exactly the "measurement blind spot" Stage 2 set out to close —
but it means **the OFF 13/7 and an ON 265/245 are not the same metric at two values; they are two
different granularities,** and the integer is no longer comparable across them.

### §3.3 The genuine analysis changes (the only NEW analyzer behavior) — DCML verdicts

Four distinct `(stem,tick)` root changes corpus-wide, all on thin measure-split slices (music21 =
2-note dyads). **DCML verdict [probe]:**

| case | OFF | ON | music21 | DCML | verdict |
|---|---|---|---|---|---|
| bwv187.7 t14400 | **F** (=DCML) | Gm7/Bb (G) | F | F (`I`) | **REGRESSION** (OFF correct) |
| bwv5.7 t19680 | **Bb** (=DCML) | Am/C (A) | Bb | Bb (`I`) | **REGRESSION** (OFF correct) |
| bwv303 t12000 | **D** (=DCML) | F#m (F#) | D | D (`I`) | **REGRESSION** (OFF correct) |
| bwv245.14 t3840 | Bm/D (B) | C#m/E (C#) | D | D (`IV`) | both wrong (neither = DCML) |

**3 regressions + 1 both-wrong, 0 improvements.** And **none of the 13/7 OFF baseline BIR=false cases
is fixed** by section-level (all their roots are unchanged). On the **root** metric, the genuine
section-level effect is small and **net-negative**.

### §3.4 DCML spot-verification of the artifacts (≥10)

The 262/243 artifacts are real DCML disagreements *by construction* (the three-way classifier requires
music21 ∩ DCML to agree against our root). Sample of 10 (Baroque ON, all at downbeats — the split
boundary) [probe]:

```
bwv10.7  m20 our=Bb/C(10)            DCML=iv(0)        bwv112.5 m4  our=D7/C(2)   DCML=vi(4)
bwv102.7 m10 our=EbMaj7/Ab(3)        DCML=IVmaj7(8)    bwv112.5 m8  our=D7/C(2)   DCML=i(4)
bwv102.7 m6  our=Dm/F(2)             DCML=VI(8)        bwv114.7 m10 our=Gm7/F(7)  DCML=iiø65(9)
bwv103.6 m4  our=G/F#(7)             DCML=V(6)         bwv108.6 m12 our=DMaj7add13/B(2) DCML=iv(4)
bwv11.6  m18 our=Bm/G(11)            DCML=viio6(1)     bwv108.6 m13 our=…(2)       DCML=iiø65(1)
```

These are genuine root errors the batch path already produced (roots unchanged) that the user sees and
the batch metric was not counting.

### §3.5 rn side — corroborates §3.2 on an independent metric

`compare_rn`'s buckets, computed on the Bach WiR corpus (Bach has no `.harmonies.tsv`; reused
`compare_rn.classify_pair` + WiR alignment via scratch `rn_wir_bach.py`, `DEFAULT_DCML_MATCH_MODE`) [probe]:

| | matched | exact | partial | exact+partial | key_dis | qual_dis | root_err | root_agree (abs) |
|---|---|---|---|---|---|---|---|---|
| **Baroque OFF** | 10118 | 3252 | 1026 | **4278** | 2812 | 328 | 2700 | **7418** |
| **Baroque ON** | 11171 | 3181 | 1056 | **4237** | 2817 | 370 | **3747** | **7424** |
| **Jazz OFF** | 9787 | 2713 | 937 | **3650** | 3194 | 338 | 2605 | **7182** |
| **Jazz ON** | 10940 | 2656 | 968 | **3624** | 3200 | 390 | **3726** | **7214** |

**The numerator of "good" is flat:** exact+partial 4278→4237 / 3650→3624; **root_agree absolute is
flat** 7418→7424 / 7182→7214. The **entire** delta is **+1047 / +1121 root_err** (= the ~1050 newly
matched finer regions, almost all root disagreements). `rn_agree%` drops (42.3→37.9 / 37.3→33.1)
**only** because the denominator grew while the numerator held. Identical story to BIR: section
granularity adds disagreement comparison points; it adds **zero** correct analyses.

---

## §4 — Metric-fix impacts (F-1 / F-2), measured on OFF outputs

### F-1 — letter-`o` diminished not recognized by `extract_quality`
- Corpus presence [probe]: **93 ours + 1173 DCML** letter-`o` (no `°`) tokens in Baroque WiR.
- Patch `has_dim = ('°' in s) or ('o' in s)`: confirmed live (`viio6`→`Dim`, `iio65`→`Dim7`).
- **Bucket impact: ZERO on both presets** — key_disagree/quality_disagree unchanged (Baroque 2812/328;
  Jazz 3194/338) [probe]. `extract_quality` only feeds the root-match ∧ degree-case-mismatch branch
  (`classify_pair:260-262`); that branch holds **no** letter-`o` cases on Bach, so the fix is a
  **latent correctness fix that is inert on the Bach BIR/rn gate.** (The `°` branch is effectively
  dead on this corpus — both sides use `o`.) Likely matters on the cross-corpus DCML set; not measured
  here. Patch **reverted**.

### F-2 — augmented-sixth / Neapolitan tokens
- Bach WiR: only **2 tokens** — `It6` (×1), `It6/ii` (×1) — both misparse to **Maj** (degree `I`,
  root from the numeral) [probe]. **Negligible** Bach impact (2/10118). No `Ger65`/`N6` in Bach WiR.
- Cross-corpus DCML (`harmonies.tsv`) is where they live [probe]: `Ger`≈1400, `It`≈600 (`It6`=277),
  `Fr`≈480, `Ger65`=22. There `It6`→`Maj` produces a **wrong root** (root-level contamination);
  `Ger`/`Fr`/`N` fall through `split_rn`→`?`→root-only fallback (`classify_pair:230-248`) — honest
  non-scoring, not mis-scoring.
- **Proposal:** fix the `It6`→Maj misparse (cross-corpus value; harmless on Bach); leave `Ger`/`Fr`/`N`
  as unparseable-fallback. Both are out-of-gate for the Bach re-baseline.

---

## §5 — Rider proposals (PROPOSE, not implemented)

1. **`analyze_inversion_errors.py` `--corpus-dir`-ification.** Bug `:93` reads music21 from the
   hardcoded flat `_CORPUS_DIR` even under `--ours-dir`. Scope: add `--corpus-dir` reading **both**
   `.ours.json` and `.music21.json` from one dir + reuse `characterise_bir_false.validate_corpus_dir`
   for manifest validation; keep `--ours-dir` as a deprecated alias. ~15 lines. **Bundle with 2.2**
   so the legacy-flat-dir fragility closes alongside the re-baseline. (Today harmless: music21 is
   preset-independent and byte-identical across dirs — §1.)
2. **Dead-shim removal** in `notationcomposingbridgehelpers.{h,cpp}` (`mu::notation::internal`):
   `beatTypeToWeight`, `safeBeatType`, `regionMetricWeightForBeatType`, `timeDecay`,
   `distinctPitchClasses`, `collectPitchContext` — **0 call-sites** in the 4 notation bridge TUs (the
   only includers of this INTERNAL header) [probe grep], yet still defined. Byte-identical removal.
   Implementation run must add a final full-repo qualified-caller sweep (incl. tests) before deleting.
   (The same names exist in the composing modules — `metricweights`, `regiontonecollector`,
   `keyresolver` — those are the live versions and must stay.)
3. **Cadence/pivot in `.ours.json` schema: defer.** `analyzeSection` does not emit them; they need a
   selection-count context batch lacks, and no metric consumes them until Stage 6 (functional layer).
   Emitting now adds unconsumed schema surface. Revisit when Stage 6 lands.

---

## §6 — Decision menu (re-baseline package)

| component | recommendation | evidence | new baseline under this choice |
|---|---|---|---|
| **Section-level as batch default** | **NO (keep as optional flag)** | §3: 0 root improvements, 3 regressions; 99% of the +250 BIR is a granularity artifact; the integer stops being comparable | n/a — gate stays at batch granularity (Baroque 13/24, Jazz 7/35) |
| **Section-level as a diagnostic `--section-level` flag** | **YES (keep the prototype)** | gives the user-faithful, measure-aligned view on demand without redefining the gate | flag-off byte-identical to HEAD |
| **F-1 letter-`o` dim fix** | **YES (apply)** | latent correctness; 0 Bach bucket impact; helps cross-corpus | Bach BIR/rn **unchanged** |
| **F-2 It6 misparse fix** | apply It6; leave Ger/Fr/N | 2 Bach tokens (nil), cross-corpus root contamination | Bach **unchanged** |
| **Rider 1 (analyze_inversion `--corpus-dir`)** | YES, bundle with 2.2 | closes line-93 fragility | numbers unchanged, fragility closed |
| **Rider 2 (dead shims)** | YES, separate byte-identical commit | 0 call-sites | byte-identical |
| **Rider 3 (cadence schema)** | defer to Stage 6 | no consumer | n/a |

**Measured baselines under the two packages actually run:**
- **all-off (current gate):** Baroque BIR=false **13** / BIR=true **24**; Jazz **7** / **35**.
- **section-level-on (default):** Baroque BIR=false **265** / BIR=true **393**; Jazz **245** / **493**
  — of which genuine root changes are 3/0 (Baroque) and 2/1 (Jazz); the rest is granularity.

**CC's recommendation to Cowork:** do **not** re-baseline the BIR/rn gate to section granularity.
The roadmap-2.2 goal ("measure the user pipeline") is real, but the naive realization breaks the
gate's comparability without improving (in fact slightly worsening) root accuracy. Instead: (a) keep
`--section-level` as a committed *diagnostic* flag; (b) **document** that the batch gate undercounts
per-beat root errors by ~7× relative to user-visible (measure-aligned) granularity (the rn root_err
+1050 quantifies it); (c) take the F-1/F-2 metric fixes and Riders 1–2 as the actual "single
re-baseline event" (all Bach-gate-neutral); (d) defer a *granularity-robust* metric definition to
Stage 5 (weight fitting), where the metric is reconsidered against held-out DCML anyway. This keeps
"no surprises": the gate that guards Stage 3 stays the one Stage 1 pinned.

---

## §7 — Unknowns / limits (honest)

1. **rn side is a scratch reimplementation.** Bach has no `.harmonies.tsv`; `compare_rn` can't score
   it directly. `rn_wir_bach.py` reuses `compare_rn.classify_pair` + `align_dcml_regions`
   (`DEFAULT_DCML_MATCH_MODE`) over WiR rntxt. Buckets follow compare_rn's definitions but are not
   emitted by `compare_rn` itself. The cross-corpus rn metric (corelli/mozart/… via tsv) was **not**
   regenerated under section-level (would require a full cross-corpus regen — out of cheap scope).
2. **Pass-0 divergence not measured away.** The A/B isolates the *section-pass* delta over batch's
   **preset** Pass-0 (Option b). The true user path (`analyzeHarmonicRhythm`) uses **default**
   chordPrefs + `excludeLookAheadOnDenseStart=false`; section's gap analysis also uses default
   chordPrefs even under Jazz. Measuring the *full* user-path divergence (chordPrefs) is a separate
   exercise — it is the real content of roadmap 2.4 and a finding for the re-baseline.
3. **BIR is root-only.** The section pass's quality refinements (`refineSparseChordQualityFromKeyContext`,
   Unknown→triad) are invisible to BIR and only mildly visible to rn (quality_disagree +42/+52, mostly
   neutral). Their *correctness* was not separately validated here.
4. **Artifact verification is by-construction, not per-case.** The 262/243 artifacts are real DCML
   disagreements by the three-way classifier's definition; I spot-verified 10 and exhaustively verified
   the 4 genuine root changes (the only new analyzer behavior). I did not hand-DCML-check all 252
   newly-false (impractical and redundant — they are the batch path's existing roots).
5. **`analyze_inversion_errors` cross-dir music21 read** is harmless now (byte-identical music21) but a
   latent bug (Rider 1).

---

## Artifacts produced this run

- **Kept (working tree):** `tools/batch_analyze.cpp` (`--section-level`, default OFF — for 2.2-ii);
  this dossier; gitignored A/B corpora `tools/corpus_ab/{baroque,jazz}_section/` (manifest-stamped,
  353/353 each) and the flag-off baselines `tools/corpus/{baroque,jazz}/`.
- **Reverted to HEAD:** `tools/run_bach_preset.py`, `tools/compare_rn.py`.
- **Scratch (used, then removed):** `tools/rn_wir_bach.py`, `tools/bir_diff_dump.py` (parameterized
  per-score BIR enumerator), plus throwaway analysis scripts under `C:/tmp/ab/`.
- **Pre-existing, untouched:** `tools/dump_bir_cases.py` (was already untracked at run start).
- `git diff` for committed files at run end: only `tools/batch_analyze.cpp` (+ the pre-existing
  uncommitted `COWORK_HANDOFF.md` / `docs/implementation_roadmap.md` doc edits from before this run).
