# Consolidated Implementation Roadmap — Reviews → Plan

*Written 2026-06-10 (session 5). Owner: Cowork (plan) / CC (execution).*
*Sources: `cowork_target_architecture_review.md` (part 1 — target architecture),
`cowork_implementation_review.md` (part 2 — as-built). This document is the single tracker
ensuring every review conclusion is addressed. Ordering principle: **no surprises** — verify
and pin each layer/gate/method before building on it; every stage has an explicit
verification gate that must pass before the next stage starts.*

**Standing rule for this roadmap:** an item may only be marked done with the evidence listed
in its "verify" column. Stages are sequential; items within a stage can run in any order
unless noted. Baselines (BIR 24/13 Baroque, 35/7 Jazz; 416/52/11 tests) are hard gates
throughout Stages 0–2; Stage 3+ re-baselines deliberately and explicitly.

---

## Stage 0 — Hygiene and honest ground truth *(zero behavior change, cheap)*

**✅ STAGE 0 COMPLETE (2026-06-10).** Commits: `7bc1609159` (0.1 docs), `a236a0ff21`
(0.2/0.3/0.5/0.6 — kTemplateCount across SIX sites incl. the bassIsTemplateChordTone
bounds check, dead fnCtx fields removed, FP tie policy, divergence docs), `70fd8a686b`
(0.4 — junk files were tracked, swept into an old feature commit; removed + gitignored by
glob, U+F03A names; no generator exists, post-build proof clean). Gate 0→1 passed:
416/416 · 52/52 · 11/11, zero diffs, BIR 13/7 both presets.
**Doc pass complete `af39f28179` (2026-06-10):** CLAUDE.md kTemplateCount + cap truth;
scoring_model §2/§4/§5/§6/§8 reconciled with the Stage-1b verified inventory; handoff
Jazz re-attribution; cap archaeology verdict = **2.5/0.6 never set in committed code**
(aspirational since field introduction `46c76ad67f`; only an uncommitted Baroque
cap=1.0 experiment ever existed). **Residual:** `chordanalyzer.h:402–409` field
doc-comment still claims "Baroque: 2.5 / Jazz: 0.6" and lists removed signals
(nextRoot/consecutive/recentRoot/weakBeat) — 2-line comment fix to ride with the next
code-touching commit.

Make every instrument we will rely on later trustworthy. All items byte-identical.

| # | Item | Source | Verify |
|---|------|--------|--------|
| 0.1 | Doc pass: clear stale `explorationMode`-as-live references in ARCHITECTURE.md (~L368/987/1026–28/1314) and `docs/layer_architecture_audit.md`; commit the audit doc (currently untracked) and the long-standing uncommitted doc edits | pending since `e7d4ba2b1a` | docs grep clean; git status clean for docs |
| 0.2 | Remove dead `HarmonicFunctionContext.keyFifths`/`keyMode` write-only fields | Part 2 Q4 | grep: no references; byte-identical tests |
| 0.3 | Shared `constexpr size_t kTemplateCount` used by the template array, `kDiagTemplates`, all three score matrices, `kMasks` — kills the silent stack-overrun class | Part 2 Q3.3 | compile-time sizes derived from one constant; tests green |
| 0.4 | Delete repo junk (root `"s -ExecutionPolicy…"` file, `C:tmpbuild_out.txt`); confirm `ai-assistant/` stays out of scope | Part 2 Q4 | git status clean |
| 0.5 | Document FP tie policy in `scoring_model.md` (exact-double comparisons + `tiePriority` ordering; no epsilon) and the platform/compiler fragility caveat | Part 2 Q6 | doc section exists |
| 0.6 | Unify or explicitly document `onsetBoundaryThreshold` (batch hard-coded 0.25 vs bridge config) and the duplicated region-collapse logic (`regionanalyzer.cpp:497`/`:694`) | Part 2 Q1.5 | comment or unification; byte-identical |

**Gate 0 → 1:** all tests green, BIR unchanged, working tree contains no unexplained files.

---

## Stage 1 — Pin current behavior *(tests first — verify each existing layer/gate before anything is built on or replaced)*

This is the core of "make sure each layer/gate/method is correct before we build upon them."
These tests are also the **differential-test harness for the Stage 3 decoder migration**:
each gate's pinned behavior is the proof obligation when the decoder later subsumes it.

| # | Item | Source | Verify |
|---|------|--------|--------|
| 1.1 | ✅ DONE `6101a9b2c5` — 48 tests in `postscoringgates_tests.cpp` (composing 487/487). Survey produced the definitive gate inventory (`cc_stage1b_report.md` §1, verified by Cowork on F1 + preset caps). Findings F1–F8: **B/C/D are dead code** (A's fast path always wins — verified in code by Cowork); shared outer guard (suspicionMargin=0 / distinctPcs<3 kills ALL gates); Gate J runs LAST; mixed live/captured winner reads in H/I/K/L; Gate F missing quality/pcWeight guards; G-E threshold-free pull + duplicate push; post-gate unsorted results[]. All → Stage-3 obligations + doc pass | Part 2 Q5.1 | each gate individually toggleable in test; count documented |
| 1.2 | ✅ DONE `757efa5dbf` — 23 tests in `functionlayer_tests.cpp` (composing 439/439). Findings F1–F5 in `cc_stage1a_report.md` §3: F1 §2 Sus4♭5/HalfDim "identical PC sets" wording → doc pass; F2 post-bonus guard first-wins tie scan + F5 threshold-gated diff-root append → Stage 3 obligation list; F3/F4 pinned | Part 2 Q5.2 | scoring_model §8 constraints each have a pinning test |
| 1.3 | ✅ PARTIAL `4656f43258` — pinned: absorbShortRegions root-agnostic (G2: order-coupled with coalesce), inline same-root merge fire/block, clean-changes preservation. **Gate 1→2 exceptions (NOT-PINNED, become HARD obligations when Stage 3 touches these passes):** coalesceShortSameRootRuns, Pass 2/2b boundaries + minGapTicks floor, sub-region bassIsStepwiseToNext (verified-by-inspection only) — emergent triggers, indirect corpus coverage; reasons in `cc_stage1c_report.md` §3 | Part 2 Q5.3 | synthetic region fixtures |
| 1.4 | ✅ DONE `4656f43258` — keyresolver: ranked output, piece-start shortcut (G3: size-1 list!), insufficient-data fallback, partial-signature fix both directions, **promoteWinnerInPlace confidence wart pinned with real numbers (G1: promoted winner carries ≈0.07 — THE Stage-4 rebaseline anchor)**; harmonicsegmenter Round-1 anchors (Round-2/fillGap NOT-PINNED, code-verified). Findings G1–G5 → Stage-4 list (G1/G4/G5), Stage-3 list (G2). Infra: composing tests now load .mscx (engraving env copy in tests/environment.cpp) | Part 2 Q5.4 | |
| 1.5 | ✅ DONE `6101a9b2c5` — all four pinned: Gate J bwv110.7 end-to-end, Sub-9a ordering test (decoy proves historical-bug visibility; arithmetic verified by Cowork), Δ=+7b end-to-end shape (bwv320 mapping), Iter 92 both bugs. Pedal already pinned by 8 existing tests (cross-referenced) | Part 2 Q5.5; audit doc rec. | removing the fix fails the test |
| 1.6 | ✅ DONE `bb48394b52` — 54 unittest tests in `tools/tests/test_metric_scripts.py` + hand-derived fixtures (README with derivations). All claims [code]/[probe]-tagged; non-vacuousness mutation check. Findings F-1 (`extract_quality` misses letter-`o` dim), F-2 (Ger65/N6/It6 mis-parses), F-3 (the "24" is NOT produced by characterise_bir_false.py — provenance untraced) → bundled into Stage 2.2's single re-baseline event | Part 2 Q6 | known-input/known-output fixtures in tools/tests |
| 1.7 | ✅ DONE `757efa5dbf` — exact-tie (tiePriority, rootPc fallback) + 0.02 near-tie FP canary, in `functionlayer_tests.cpp` | Part 2 Q6 | |

**Gate 1 → 2: ✅ PASSED 2026-06-10** (commits `757efa5dbf`, `6101a9b2c5`, `4656f43258`,
`bb48394b52`). Composing 416→498 + 54 Python metric tests. Documented exceptions
(1.3 NOT-PINNED: coalesceShortSameRootRuns, Pass 2/2b boundaries, sub-region
bassIsStepwiseToNext) become hard obligations when Stage 3 touches those passes.
Metric-bug decisions (1.6 F-1/F-2/F-3) deferred into Stage 2.2's re-baseline.

---

## Stage 2 — One pipeline, one truth *(close the measurement blind spot and path divergences before any redesign)*

After this stage, the measured pipeline IS the user pipeline and the diagnostic tool IS the
production scorer. Without this, Stage 3 results can't be trusted ("no surprises").

| # | Item | Source | Verify |
|---|------|--------|--------|
| 2.1 | ✅ DONE `eeca0dea30` (rider) + `8598cbd245` (move) — `analysis/section/sectionanalyzer.{h,cpp}` (Option D: Pass-0 regions injected, composing stays config/notation-agnostic — chosen for the layer shape Stage 3/E needs and so 2.2's batch can pass its own regions). Byte-identical: snapshots 11/11 zero diffs, Baroque 13. Cadence/pivot tests stayed in notation tests (include updates; allowed alternative). Dead weight/pitch-context shims found (no live caller) — Stage-2 cleanup list. **Jazz "nondeterminism" investigated en route: M3 = shared `tools/corpus` contamination (FAILED-worker stale files + skip_cpp reuse + no preset guard), NOT C++/Python — both proven deterministic (Jazz 7, Baroque 13; 0/353 double-regen, retroactively validating all historical A/B checks).** `cc_jazz_nondeterminism_report.md` | Part 2 Q1.1, Q2.1 | byte-identical on snapshots + corpus; Dependency Rule restored |
| 2.2a | ✅ DONE `e20894c75b` (+ docs `6f1e3dc807`) — per-preset dirs (`tools/corpus/{baroque,jazz}/`), clean-slate + manifest with per-score sha256 fingerprints, fail-loud (regen exit≠0 on incomplete; characterise exit 2 on missing/incomplete/contaminated manifest), `--corpus-dir`/`--wir-dir`; 63 Python tests (+9 incl. the exact M3 scenario → ERROR); CLAUDE.md/BUILD_AND_TEST.md synced. Verified: Baroque 13 + Jazz 7 with exact identity sets; contamination probe errors. **Interim gate RETIRED — "Baroque ≤ 13 / Jazz ≤ 7" regain plain meaning.** Deferred follow-up: `analyze_inversion_errors.py` (secondary metric) still reads legacy flat dir — `--corpus-dir`-ify with 2.2 | M3 fix design (#1+#3) | both presets regenerate side-by-side: Baroque 13 + Jazz 7 with known identity sets; contamination scenario now fails loudly |
| 2.2 | **RESOLVED BY MEASUREMENT (2.2-i A/B, `cc_stage2_2_ab_dossier.md`) — decision: the gate STAYS at batch granularity.** The blind spot was granularity, not identity: section-level barely changes analysis (4 genuine root changes corpus-wide: 3 regressions + 1 both-wrong, all on thin gap/split slices) but the measure-aligned regions surface ~252/238 per-beat disagreements the coarse regions masked (rn corroborates: root_agree flat, all delta in root_err). **The batch gate undercounts user-visible per-beat root errors ~7×** — quantified, documented; granularity-robust metric is now MANDATORY at Stage 5. F-3 closed: 24/13 & 35/7 = `analyze_inversion_errors.py` three-way split; characterise reproduces the 13/7 half. **2.2-ii SHIPPED `75a5815960`+`c7aeb24ae1`+`465450bf49`+`9e52147b04` (gate-neutral verified: 13/24, 7/35 exact identity sets, flag-off byte-identical, 65/65 Python):** `--section-level` diagnostic flag (default off), F-1 letter-`o` fix + F-2 It6→fallback routing (honest residual: dcml_parser still assigns It6 a tonic root — documented, out of scope), Rider 1 (analyze_inversion `--corpus-dir` + line-93 fix), Rider 2 (dead shims removed), docs. Cross-corpus rn numbers (27.6%/53.8%) marked pre-F1-stale; re-measure at Stage 5 entry. Rider 3 (cadence schema) deferred to Stage 6 | Part 2 Q1.1; Stage-1d F1–F3; dossier §6 | gate numbers unchanged (13/24, 7/35 + identity sets); flag-off byte-identity; updated metric tests green |
| 2.3 | **diagnoseChord becomes a view into production**: replay `applyHarmonicFunction` on the real snapshot (with a context dump), or stamp every dump "oracle-only — excludes progression signals" at minimum. Preferred: full replay | Part 2 Q1.4; principle #2 | a Δ=+7b-style case diagnosed via diagnoseChord shows the same winner as production |
| 2.3b | **Wire temporal context into `batch_analyze --diagnose-measures`** (follow-up from 2.3): the diagnose tool currently replays the production pipeline with NULL temporal context (region-in-isolation) — correct and now explicitly bannered in the dump, but rcb-class investigations (Δ=+7 family) need the threaded inter-region context the batch run actually used. Reconstruct it from the run, don't fabricate. Low urgency; do before any Δ=+7a investigation relies on the tool | 2.3 report §2.4/§6 | a Δ=+7a-class dump shows the real rcb feed |
| 2.4 | Document/decide P4 divergence: either feed P4 the accumulated context (pre-pass) or document cold-context as the contract; same decision for bridge cold-predecessor (`findTemporalContext` nullptr context). A full forward pre-pass is its own design — decide, don't drift. **Scope grown by 2.2-i findings:** (a) Pass-0 prefs divergence — notation `analyzeHarmonicRhythm` uses default chordPrefs + `excludeLookAheadOnDenseStart=false` vs batch preset prefs (dossier §7.2); (b) **section-layer preset leak** — `inferGapRegion` analyzed gap slices with `kDefaultChordAnalyzerPreferences` regardless of preset (dossier §2). **Causal hypothesis FALSIFIED by the 2.4 probe**: the 3 Baroque regressions are structural (measure-split/gap-insertion), not pref-caused — Baroque prefs ≈ defaults so the leak was inert there; it was live under Jazz (bwv5.7 healed). Leak fixed in 2.4 (V2) on consistency grounds | Part 2 Q1.2/1.3; dossier §2/§7 | written decision in ARCHITECTURE.md |
| 2.5 | Profile P3 status-bar path (re-analysis per query, no caching) — capture numbers before decoder cost is added | Part 2 Q6 | profile note committed |

**Gate 2 → 3:** snapshots green on the moved code; new corpus baselines committed and
explained; diagnoseChord output verified against production on ≥3 historical cases.

---

## Stage 3 — Phase E as a decoder *(the part-1 core recommendation, made incremental)*

Replace greedy left-to-right commitment with lattice + global decode. Incremental, with a
byte-identity bridge so there is a no-surprise verification gate at every step.

| # | Item | Source | Verify |
|---|------|--------|--------|
| 3.1 | **Decoder skeleton, beam = 1**: per-region candidate lattice from the existing oracle output; transitions = existing progression signals (rcb, resolution, wSeq, wDim, steps). **Hard gate: beam-1 must reproduce the current pipeline byte-identically** (it is the same greedy argmax, restructured) | Part 1 rec. 1 | 0/353 corpus diff, all snapshots, BIR unchanged |
| 3.2 | Widen beam / exact DP behind the quality-level setting (ARCHITECTURE.md §2.14: level↔beam width). A/B vs beam-1 on both presets + DCML cross-corpus; expected wins: Δ=+7a (bwv102.7, bwv261), Δ=+7b class, rcb cascades | Part 1 | per-case table; no hard-stop regressions at level 0 |
| 3.3 | Migrate oracle temporal signals (resolutionBonus + 4 inversion bonuses, chordanalyzer.h:329 debt) into transition scores; **revisit Gate R's `basisDep ≤ 0` proxy in the same change** (documented coupling) | Part 2 Q2.2; audit F1/F6 | Stage-1 pinning tests green or consciously re-baselined |
| 3.4 | Retire gates A–L one at a time: a gate is removed only when the decoder reproduces its pinned fixes (Stage 1.1 tests are the proof obligations). Gates J and R expected to survive longest (structural, healthy). **Stage-1a obligations:** the post-bonus quality-guard winner scan is first-wins on exact ties (ordering sensitivity), and the diff-root append never appends sub-threshold candidates — the decoder must either reproduce or consciously re-decide both (`cc_stage1a_report.md` F2/F5) | Part 1; audit F7 | per-gate differential report |
| 3.4b | Remove dead Gates B/C/D (provably unreachable — stage1b F1) as part of the gate-retirement work, NOT before (their removal is byte-identical but belongs to the deliberate per-gate retirement audit) | stage1b F1 | byte-identical removal commit |
| 3.5 | Split `chordanalyzer.cpp` along the now-real layer seams; rename iteration-vocabulary APIs (`applyIter8691Pedal` → descriptive names) — the split is motivated here, not before | Part 2 Q3.1/3.2 | file map in ARCHITECTURE.md |

**Gate 3 → 4:** decoder is the production path at all quality levels; gate count reduced;
corpus metrics ≥ Stage-2 baselines on both presets.

---

## Stage 4 — Key as a path *(mode/key correctness)*

| # | Item | Source | Verify |
|---|------|--------|--------|
| 4.1 | Key HMM over existing 252-candidate window scores (emissions = raw scores, transitions = circle-of-fifths modulation penalty). Replaces per-window argmax + `promoteWinnerInPlace` hysteresis; do not consume `normalizedConfidence` (known unreliable) | Part 1 rec. 2 | keyresolver pinning tests (1.4) re-baselined; corpus key_disagree measured before/after |
| 4.2 | `KeyArea` spans emitted from the decode (wanted by `unified_analysis_pipeline.md` for modulation-aware RN) | Part 1 | spans consumed by annotation emitter |
| 4.3 | Evaluate two-level (key path × chord path) joint decode vs sequential — only if 4.1 leaves measurable key-driven chord errors | Part 1 | decision note |

*Note: Stage 4 may be promoted ahead of Stage 3 if a live key-failure case emerges; the two
are independent.*

---

## Stage 5 — Fit the weights *(stop hand-tuning)*

| # | Item | Source | Verify |
|---|------|--------|--------|
| 5.1 | Calibrate emission/transition constants against aligned DCML corpora (structured perceptron or coordinate search), Baroque/Jazz presets as separate fits; existing hard stops as constraints | Part 1 rec. 3 | held-out corpus split; per-preset before/after table |
| 5.2 | Re-baseline BIR/rn_agree; retire constants that fit to zero. **MANDATORY (was optional): granularity-robust metric definition** — the batch-granularity gate undercounts user-visible per-beat errors ~7× (2.2-i dossier §3); the fitting objective must not inherit that bias. **Equally mandatory: a human-only (DCML-only) gate variant** — the current "genuine" filter requires music21∩DCML agreement, i.e. an ALGORITHM adjudicates which DCML disagreements count (music21 is NOT ground truth — user mandate 2026-06-10; see corpus audit C2). The fitting objective must not be filtered by another analyzer's opinion. **Coverage fact (hygiene pass): only 326/353 gate chorales have WiR human annotations at all — 27 scores can never produce a "genuine" error.** The gate's true shape: human-adjudicated coverage of 326, music21-filtered, batch granularity — all three qualifiers must be addressed here. Also re-measure the cross-corpus rn numbers (27.6%/53.8% are pre-F1-metric, stale) | Part 1; dossier §3/§6; corpus audit | STATUS.md baselines |

---

## Stage 6 — Functional layer *(functional chord correctness — E4)*

| # | Item | Source | Verify |
|---|------|--------|--------|
| 6.1 | Sequence labeling over the decoded chord+key paths: T/S/D states, cadence patterns (consuming the Stage-2.1 relocated cadence detector), secondary dominants, aug6, Neapolitan, tonicization-vs-modulation from KeyArea spans | Part 1 rec. 4; ARCH §5.6 | rn_agree / key_disagree movement vs frozen 27.6% / 15.4% |
| 6.2 | Consolidate the three scattered quality-from-key feedback sites (sparse refinement, forceChordTrackQuality, display stabilization) into this layer | Part 2 Q2.4 | one home; pinning tests green |
| 6.3 | Revisit closed "convention gap" buckets (Maj→Dom7 implied sevenths, Min↔Maj thirdless) — now addressable as functional-label decisions, not sonority changes | Part 1 §2.3 | bucket counts before/after |

---

## Stage 7 — Optional ceiling

| # | Item | Source |
|---|------|--------|
| 7.1 | Neural proposal model (AugmentedNet/ChordGNN/RNBert class) behind §2.2 interfaces, decoded by the same lattice machinery; rule-based remains default | Part 1 rec. 5 |

---

## Traceability — every review conclusion → stage

| Conclusion (part 1 = A, part 2 = B) | Stage |
|---|---|
| A: Phase E = decoder, not feature pack | 3.1–3.4 |
| A: key as HMM path / KeyArea | 4.1–4.2 |
| A: weight fitting vs DCML | 5 |
| A: functional labels as sequence labeling | 6.1 |
| A: keep oracle + heuristics as features; quality level = beam width | 3.1, 3.2 |
| A: §2.14 reconciliation | done 2026-06-10 (docs) |
| A: neural hybrid optional | 7.1 |
| B: analyzeSection in notation / batch metric blind spot | 2.1–2.2 |
| B: diagnoseChord second scorer | 2.3 |
| B: missing unit tests (gates, bonuses, segmentation, keyresolver, pinned bugs) | 1.1–1.5 |
| B: metric scripts untested | 1.6 |
| B: kTemplateCount silent-overrun | 0.3 |
| B: dead fnCtx fields | 0.2 |
| B: repo junk + untracked audit doc + stale doc refs | 0.1, 0.4 |
| B: FP tie policy + tie-stability test | 0.5, 1.7 |
| B: P4/bridge cold-context divergence | 2.4 |
| B: P3 performance | 2.5 |
| B: oracle temporal signals debt + Gate R coupling | 3.3 |
| B: chordanalyzer.cpp size + iteration-named APIs | 3.5 |
| B: quality-from-key scattered (3 sites) | 6.2 |
| B: onsetBoundaryThreshold + region-collapse duplication | 0.6 |

*No review conclusion is unassigned.*

---

## Relationship to the existing phase roadmap (COWORK_HANDOFF "Roadmap")

- Phase A/B/C residuals classified "Phase E only" (Δ=+7a, B1 mMaj7, A2 dominant-in-minor,
  C1 schumann, C2 bwv320) map to Stage 3/6 deliverables — they are the decoder's acceptance
  cases, listed in 3.2.
- B4 (6th-chord templates) and other template work stay frozen until Stage 5 (fitting makes
  template ambiguity tractable).
- The "do not" rules (no new gates, no threshold widening, no rcb gating) remain in force
  through all stages; Stage 3.4 is the only sanctioned way gates change.
