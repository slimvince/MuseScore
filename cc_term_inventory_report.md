# CC report — the term inventory (code-enumeration half of the term-level theory-grounding audit)

**Dispatch:** `cc_instruction_term_inventory.md` (Cowork, 2026-07-18). **Type:** fact-finding
enumeration (#1 investigative, #5) — no code change, no fix, no tuning, no inference work.
**Deliverables:** this report + the generated artifact `tools/term_inventory/`
(`gen_term_inventory.py` → `term_inventory.csv`, `term_inventory_summary.json`) + register rows
OI-182/OI-183 + the measured-figure additions to OI-23/OI-179.

**Establishment of the artifact (#17f/#19):** the 95 term rows are hand-verified readings of the
source (every row carries the decl and application file:line read during this sweep;
`hand_verified=yes` on each). Everything derivable is computed mechanically by the generator and
never hand-typed: the `param_manifest.json` coverage columns, every count below, the OI-23
measured figures, the template staleness check, the doc symbol-mention check, the DT-26 tree-wide
sweep with per-file dispositions (the script exits nonzero on any undispositioned hit), and the
OI-179 census (computed live from `tools/corpus/*.xml` + the When-in-Rome tree through the shared
`dcml_parser._build_wir_index`). Method: the certified pass-1 audit surfaces (`tools/audit/*`),
`docs/scoring_model.md` and `tools/param_manifest.json` were used as starting maps; **every row
was then verified at the code** — five parallel read-only file sweeps whose load-bearing claims
(constants, sites, forms) were spot-re-read at the source before entering the row set. No `src/`
or `tools/` behavior file was edited; the only new files are the report and the artifact.

All figures below are from `term_inventory_summary.json` unless marked otherwise.

---

## 1. Task 1 — the inventory (summary; the CSV is the deliverable)

**95 term rows** (one per term or tightly-coupled term family; families list every member
constant with its declared value). By layer: L4-oracle 20, L4-competition 9, L4-gates 10,
L4-postpass 3, L4-commit 2, L2 9, L1.5 8, L3 15, L3-section 4, L3-dormant 3, L4-decoder
(dormant slice decoder) 2, L5 8, bridge 2. By liveness: **80 live, 15 dormant**. Each row
carries: name as in code, decl + application file:line, the implemented form in plain words,
every constant with value and provenance tag, consumers, and the
`cowork_joint_estimator_architecture.md` §2 roster factor (or NONE).

Layer highlights (details in the CSV):

- **L4 oracle** (`chordanalyzer.cpp`): 29 override-registered file-scope constants (all
  hand-set; verified against the registration block at `chordanalyzer.cpp:154-185`) plus the
  prefs-struct terms (`analysistypes.h:191-405`) and the OI-106(b) inline presence bars
  (0.05/0.1/0.2/0.3 class). The two key-consuming scoring terms are the OI-168-fixed
  signature-mask form (`dim7CharacteristicBonus`, `diatonicRootContribution`); `buildChordResult`'s
  `degree`/`diatonicToKey` still carry the OI-170/OI-173 tonic/parent-scale basis (re-verified,
  unchanged, declared — not touched).
- **L4 competition** (`harmonicfunctionlayer.{h,cpp}`): rcb+Gate R, resolution, the four inversion
  bonuses (Jazz carrier overrides 0.20/0.20/0.20/0.15), wSeq/wDim(+quality guard)/wStepIn/Out
  (+surgical guard), the 0.75 threshold ratio + cap-3 + diff-root-append carry policy.
  **`kWStepIn` = 0.125 is the only robust-unit-fitted value in the entire system**; `kStepBudget`
  is derived from it.
- **L4 gates** (`postscoringgates.cpp`): outer guard, bias correction, FM2, E, G-E/G-D, H, I
  (0.45), L (0.35), J, `kHalfDimFirstInversionBonus` 0.55 — all margins hand-set. Gate G-E is the
  degree-driven (genuine-tonic) site OI-170 measured at 58 Baroque winner swaps.
- **L4 post-passes** (`chordpostpasses.cpp`): Iter-86/91 promotions; the pedal two-pass check with
  its **inlined** sigmoid (steepness 1.5, midpoint 2.0 at `chordpostpasses.cpp:271` — the OI-79
  duplication) against `pedalConfidenceThreshold` 0.65.
- **L4 commit path** (`sparsechordrefinement.cpp`, called at `regionanalyzer.cpp:1015-1017`):
  `applyTonicPriorToSparseChord` (OI-172) and the Aeolian-guarded Unknown-quality upgrade — both
  degree-driven quality writes, no numeric weights (structural conditions only).
- **L2** (`harmonicsegmenter.{h,cpp}`): per-region hard-threshold anchor promotion (no global
  objective) — `kAnchorMinScore` 1.5, `kRound2MinScore` 1.25, texture-scaling constants
  (0.75/3.5/0.75), duration floors — and the **OI-175 head-gap tonic prior**
  (`kHeadGapTonicPreferenceMargin` = 0.4 at `harmonicsegmenter.cpp:858`, the overwrite block
  `:853-889`; the tonic derivation `:848-852` re-verified verbatim). The audit's standing
  disposition for this file (L2-LEGACY, retires R6 to the change-point slicer) is noted on the
  rows; the greedy-expand path is still live today.
- **L1.5**: the two metric-weight tables (`regionMetricWeightForBeatType` 1.0/0.85/0.75/0.5 vs
  the prefs-driven `beatTypeToWeight` — the OI-86 #6 duplication), the span-window constants
  (16/8/0.5/0.7 + the `SpanWindowWeights` DT-3 value-copies), the OI-86/OI-87 tone boosts
  (repetition ×(1+0.3·(n−1)) at `regiontonecollector.cpp:297`, cross-voice ×1.5 at `:312`),
  pedal-tail carry (0.3 flat), and the dormant phrase-boundary view (the only F8 surface;
  `minSilenceTicks` 240).
- **L3** (`keymodeanalyzer`, `keymodesequence`, `keyresolver`, `modepriorpresets`): the ~60
  emission weights of `KeyModeAnalyzerPreferences` (all hand-set, code-labeled "[empirical —
  Stage-5 fits]"), the 21 mode priors × 6 tables (5 presets + app defaults), the Viterbi decoder
  over per-slice top-8 of 252 (tonic,mode) candidates with change cost = 2.0 + 0.60·cofDistance
  (+2.0 relative-pair) — the three transition constants are shared symbols with the resolver's
  hysteresis/proximity constants (single-sourced by reference), and the OI-97 soft-coupled
  `relativeKeyHysteresisMargin`. Partial-signature correction 0.03/2.0. **None of this surface is
  in `param_manifest.json`** (OI-91, re-confirmed mechanically in the per-row coverage column).
- **L3 section pipeline (live)**: `kAnnotateKeyConfidenceThreshold` 0.8 (G10), island key
  stabilization (structural smoothing), the key-DEPENDENT degree-pattern cadence labels
  (PAC/PC/DC/HC — the form OI-166's key-agnostic detector is specified to replace), sparse-gap
  interval-table inference.
- **Dormant surfaces**, enumerated per the dispatch: the L4 slice decoder (13 prefs + membership/
  salience machinery; OI-103 manifest gap re-confirmed — only `sufficiencyChordTones` is in the
  manifest), the L5 function stack (cadence votes wPhraseBoundary=2.0 etc., modulation decision,
  progression licensing grammar — **no numeric constants**, resolver plausibility, forward-override
  bar, output confidence, VL-C study-fitted floors), the L3 joint-key weights (J-key-iii, gated
  off), cadence key-anchor votes (swept 1.0/2.0/1.0/1.0), local-modulation establishment (5/2).

**Provenance across all rows:** hand-set dominates overwhelmingly; fit-adopted = 1 constant
(`kWStepIn`); derived = 3 (`kStepBudget`, the decoder change-cost aliases, `kMasks`/coalesce run
ticks); study-fitted = the VL-C reference; preset-table = the mode priors; swept = the cadence
anchor weights.

### 1a. Mandatory cross-check 1 — scoring_model.md staleness

**PASS**, measured mechanically: `kTemplateCount` = **17** (`chordanalyzer.h:63`) = the doc's
"currently 17" claim = 17 numbered template rows in §2. On the §4 term list: the sweep found no
live §4-class term absent from the doc **at the concept level**, but the symbol-mention check
(below, cross-check follow-on) found 12 L4 registered constants with no by-name mention — see
OI-183.

**Doc symbol-mention check** (generated): of the 33 override-registered constants
(`chordanalyzer.cpp` 29 + `postscoringgates.cpp` 3 + `sectionanalyzer.cpp` 1), **13 have no
by-name mention in `docs/scoring_model.md`**: `kAnnotateKeyConfidenceThreshold` (out of that
doc's L4 scope — an L3-section constant, not a gap), and 12 L4 constants. Of those 12, several
are documented under combined table cells or by value in prose (`kExtensionFactorFlat13`/
`Default` in the "kExtensionFactor7th / Flat13 / Default" cell; `kSus4StructuralFourthThreshold`
as "P4 above 0.50"; the two weight caps as the "Caps prevent…" prose), while
`kSus4FlatThirdFactor`/`kSus4SharpThirdFactor`, `kSeventhThreshold`, `kBassSupportPresenceThreshold`,
`kWCompletePresenceThreshold`-siblings `kComplexityEvidenceFloor`/`kAugThinEvidenceFactor` are
symbol-absent (concepts partially described in §3). This is the named-constant sibling of
OI-106(b)'s inline-bar negative-space finding → new row **OI-183** (doc-sync class, low). No doc
edit made — this dispatch is read-only.

### 1b. Mandatory cross-check 2 — the OI-23 "~30 live hand-set constants" claim

Measured mechanically from `tools/param_manifest.json` (figures in the summary JSON):

- Chord-surface live rows (groups G1–G7, `consuming_path` ∈ {production, both}): **57**
  (by group: G1 28, G2 7, G3 5, G4 4, G5 5, G6 5, G7 3). Of these exactly **1** is
  robust-unit-fitted (`kWStepIn`); the rest are hand-set.
- The **G1 oracle constants (28) + G7 gate margins (3) = 31** — the population that matches the
  row's "~30" phrasing.
- Manifest total 78 rows; live across all groups 59.

**Flagged difference:** the full live chord-surface count (57) is nearly double the row's "~30";
the "~30" reading holds only for the G1+G7 core. Additionally the per-row manifest-coverage
column shows live hand-set constants **outside the manifest entirely** (the L2 segmenter
constants, the L1.5 tone boosts and metric tables, the whole L3 emission surface per OI-91, the
L3-section structural constants, the bridge constants of OI-182) — the true live hand-set
population is larger than any manifest count. Per the dispatch, OI-23's row text is amended only
by adding the measured figure with provenance.

### 1c. Mandatory cross-check 3 — the DT-26 tree-wide scope check

Three identifying patterns (named term-constant assignments; term-shaped variable declarations;
the OI-168/OI-175 tonic-construction pair `ionianTonicPcFromFifths|keyModeTonicOffset`) were run
**tree-wide** over `src/**/*.{cpp,h}` + `tools/*.cpp` (tests and `src/framework` excluded) by the
generator, which **fails if any hit file lacks a disposition**. Result: **0 undispositioned**;
every hit file is dispositioned in the artifact (`dt26_sweep` in the summary JSON) as IN-SCOPE
(enumerated), UPSTREAM-NON-ANALYSIS (engraving layout/rendering/import/UI), CONSUMER (notation
bridges — consume analysis facts, no inference term), or DIAGNOSTIC-CARRIER (`batch_analyze.cpp`).

**What the out-of-scope remainder surfaced** (the OI-175 lesson paying again, at lower stakes):
`notationimplodebridge.cpp:79-80` carries two hand-set decision constants
(`kTentativeKeyExposureThreshold` = 0.5, `kAssertiveKeyExposureThreshold` = 0.8) bucketing key
exposure in the imploded output — a **consumption-side** surface on no audit `file_table`, in no
manifest, on no register row → new row **OI-182**. Not an inference-correctness finding (the
bridge consumes, it does not infer), so **not a STOP**. The tonic-construction sweep outside
`src/composing` found only the known OI-173 D2/D3 consumer sites (`notationcomposingbridge.cpp`,
`notationimplodebridge.cpp`, `notationtuningbridge.cpp`) — nothing new.

**STOP assessment (#13):** no finding of this sweep implicates live inference correctness beyond
what OI-170/OI-172/OI-173/OI-174/OI-175 already carry (each was re-verified at its site and is
cited on its row). No STOP raised.

---

## 2. Task 2 — the two-way gap map

### (a) §2 roster factors with no current term (the missing clue channels)

Mechanically, only **F8 (fermatas + phrase facts)** has zero live term (its lone surface is the
dormant `phraseboundaryview`, where a fermata is just a generic marker spike). But the honest map
is form-sensitive; per factor:

- **F1 emission** — rich live term surface, but **NCT-cleaning does not exist on the live path**:
  the L3 emission consumes raw weighted collections, and the NCT tier machinery lives only in the
  dormant slice decoder (`classifyTone`/`classifyMembership`). The roster's "NCT-cleaned" half is
  missing.
- **F2 (signature + declared mode prior)** — live (mode priors, declared-mode penalty,
  signature proximity, partial-signature correction). Gap: mid-piece signature changes are never
  re-anchored (OI-94) and the declared mode is siloed to the key path (OI-78).
- **F3 (spelling-conditioned emission + mode disambiguation)** — live terms are **chord-level
  only** (`tpcConsistencyBonusPerTone`, the Sus4 TPC factors, the nonBass TPC waiver, the dim7
  selector's spelling-adjacent collection test). **The L3 key/mode emission is spelling-blind** —
  no spelling term reaches (tonic, mode) inference; `spellingview` (the fact layer for exactly
  this) is dormant with its only consumer the dormant decoder's pin.
- **F4 (cadence votes + leading-tone events)** — no live term on the key axis. The live
  cadence detector (`sectioncadencedetection`) is key-DEPENDENT (degree-based) and
  annotation-only; the key-agnostic machinery (`functioncadence`) is dormant and chord-derived
  (OI-166: not the specified L1.5 pre-scan). `trueLeadingToneBoost` is a presence test, not a
  resolution event.
- **F5 (progression grammaticality / chord transition)** — live terms are three narrow fragments
  (rcb as a self-transition prior; wSeq's single V→I motion; resolutionBonus's 3 rules; wDim;
  Gate J; Iter-91). The full licensing grammar (`functionprogression`) is **dormant**, and the
  "grammaticality under each candidate key" channel does not exist anywhere.
- **F6 (segmentation model)** — live terms are hard threshold gates and size floors; there is
  **no segment-duration (semi-Markov) model, no graded boundary strength, no harmonic-rhythm
  term** — the roster's actual content is absent; what exists is a filter cascade.
- **F7 (metric weighting)** — the best-covered factor (both weight tables, decay windows,
  boosts); no "chord-change-on-strong-beat prior" exists (the Round-1 on-beat gate is a hard
  filter, not a prior).
- **F9 (bass/inversion emission)** — live and heavily termed (bass-root bonus family, inversion
  bonuses, stepwise bonuses, Gate I, bias correction); forms are ad-hoc additive bonuses rather
  than an emission model; bass MOTION skeletons (dominant→tonic bass fifths) exist only as
  stepwise ±1/±2 flags.

Also absent though implied by the architecture (not on the §2 list): an explicit **(tonic, mode)
transition factor** is currently embodied as the decoder change costs + resolver hysteresis —
present in code, unowned by any roster factor (see (b)).

### (b) Current terms mapping to no roster factor — keep/fix/drop INPUTS (not decided here)

26 of the 95 rows map to NONE (`rows_with_no_roster_factor` in the summary JSON). Grouped:

1. **P(chord | key) coupling terms**: `diatonicRootContribution`, `buildChordResult`
   degree/diatonicToKey, Gate G-E's key-degree condition, `applyTonicPriorToSparseChord` (OI-172),
   `refineSparseChordQualityFromKeyContext`, the L2 head-gap tonic prior (OI-175), Gate L's
   diatonic condition. In the joint model this coupling is structural (a degree-valued chord
   state), not a bag of bonuses/overwrites — these rows are the concrete keep/fix/drop docket for
   that design decision.
2. **Enharmonic/rotation disambiguation gates**: FM2, Gate H, G-E/G-D as a promotion mechanism,
   (Gate L's quality flip). These do post-hoc what a spelling-conditioned emission (F3) would do
   in-model.
3. **Key transition/hysteresis terms**: decoder change costs, resolver hysteresis pair, dynamic
   lookahead windowing — the existing (tonic,mode) transition structure the joint decode subsumes.
4. **Carry/abstention/output policy**: `kScoreThresholdRatio` + cap + diff-root append, the
   confidence sigmoids, `uncertainThreshold`/`maxAlternatives`/`topK` caps,
   `kAnnotateKeyConfidenceThreshold`, the bridge exposure buckets — reporting surface, not
   factors; several are the #12-relevant carry policies (OI-9, OI-75/OI-81).
5. **Post-hoc smoothing**: island key stabilization (duplicates what a decode transition already
   does); the gate outer guard.
6. **Dormant NONE rows**: joint-key weights, local-modulation establishment, modulation decision,
   forward-override bar, function output confidence, VL-C.

### (c) Evidence-inventory §8 facts consumed by no term (cross-reference)

From the key layer's shopping list and §8: **fermatas** (INPUT, unread — only the dormant marker
spike); **long rests as phrase ends** (dormant, `minSilenceTicks` 240 unfit); **double barlines**
(unread); **bass-motion dominant→tonic skeletons** (no term; only stepwise flags);
**dominant-shape key votes** (never built — OI-94(b)/OI-68); **leading-tone-resolution events**
(dormant, chord-derived); **notated accidentals as tonicization/key evidence** (no L3 term;
chord-level TPC only); **harmonic rhythm** (no term); **boundary strength** (binary cuts only);
**NCT-cleaned collections for the key emission** (dormant machinery only); **progression
grammaticality under candidate keys** (nothing); **chord-symbol annotations in the score**
(recognized, never read — OI-80); **the collection/tonic split and per-slice ambiguity margins**
(computed in the decoder, alternatives capped at 4 and margins discarded — OI-75/OI-81).

---

## 3. Task 3 — OI-179 feasibility census (counts and locations only)

Computed live by the generator (`oi179_census` in the summary JSON):

- Corpus stems: **352** (`tools/corpus/*.xml`); WiR-covered: **326** (via
  `dcml_parser._build_wir_index`).
- **87 of the 326 covered stems** live in a When-in-Rome chorale folder that carries a **second
  analysis file**, `analysis_BCMH.txt`, beside the primary `analysis.txt`
  (location: `tools/dcml/when_in_rome/Corpus/Early_Choral/Bach,_Johann_Sebastian/Chorales/<NNN>/`;
  folder-level: 100 of 371 folders carry the pair). The stem list is in the summary JSON.
- Provenance as stated in the files themselves: the primary `analysis.txt` headers name
  individual human analysts (e.g. "Analyst: Andrew Jones; Proofreader: Dmitri Tymoczko and
  Hamish Robb"); `analysis_BCMH.txt` headers read "Analyst: The Bach Chorales Melody-Harmony
  Corpus. See https://github.com/PeARL-laboratory/BCMH / Proofreader: Automated translation by
  Néstor Nápoles López" — i.e. a machine **translation into rntxt of a separate corpus's
  annotations**. Whether BCMH's annotations are independent human analyses (vs derived from a
  shared source) is the literature half of OI-179 — Cowork's, not assessed here.
- No other in-repo second annotation exists for these stems: the DCML `bach_chorales` repo
  (361 pieces, `tools/dcml/bach_chorales/`) carries **zero** harmony labels (`label_count` = 0 on
  all 361 rows of its `metadata.tsv`) — scores only. music21's `.music21.json` is algorithmic,
  not human, and not ground truth (standing rule).
- **Plainly: an in-repo two-annotator agreement measurement is feasible on at most 87 of 352
  stems (26.7 % of the covered set), pending Cowork's independence verdict on BCMH.** No
  agreement grading was built; the robust stop and its reference were not touched.

---

## 4. Register and doc changes in this commit

- **OI-182 (NEW):** notation-bridge consumption-surface decision constants on no audited surface
  (`notationimplodebridge.cpp:79-80` exposure buckets 0.5/0.8; found by the DT-26 tree-wide
  sweep; no manifest row, no audit file_table row).
- **OI-183 (NEW):** `docs/scoring_model.md` symbol-level coverage gap — 12 L4 override-registered
  constants without a by-name mention (measured list in the artifact; extends OI-106(b)).
- **OI-23:** measured figure added to the row (57 live chord-surface manifest rows G1–G7; the
  G1+G7 core = 31 ≈ the row's "~30"; provenance: this artifact). Row text otherwise untouched.
- **OI-179:** the in-repo census figures added to the row (87/326; locations; DCML-repo zero
  labels), the literature half left open for Cowork.
- `STATUS.md`: one lean dated entry.

**Self-check (standing rule):** the diff was re-read after assembly. No `src/` edit, no `tools/`
behavior edit (the new `tools/term_inventory/` files are read-only instruments run on demand; no
existing tool imports them), no goldens, no corpus, no re-baseline; figures in this report are
quoted from the generated summary; names used are the repository's own (no invented labels —
roster factors are cited as the architecture doc's §2 items; "F1…F9" keys exist only inside the
artifact's mapping column with the full §2 text carried beside them in `roster_factor_text`).
The generator excludes `src/composing/tests` and `src/framework` from the sweep by design
(tests are not inference surface; framework is upstream UI plumbing) — stated here so the scope
choice is visible.
