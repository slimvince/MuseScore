# CC Instruction: Functional-root residual investigation — the OQ-1 (A-vs-B) gate

## Context

This is the one investigation that **gates the OQ-1 ratification** (back_half_design §3:
A = keep improving the hand-built emission + build a functional layer; B = learned model).
"A confirmed" is *proven* on the key axis but only *inferred* on the largest headroom
slice — the functional mass. This decomposes the uncertain part of that mass so OQ-1 is
ratified on evidence, not inference.

> **⚠ UPDATED 2026-06-13 — this instruction was UNBLOCKED by the metric re-baseline and the
> old numbers in it are now STALE.** The parser is corrected (P0 fractional-onset, P1 rntxt
> applied, P2 minor-key LT — `cc_metric_rebaseline_report.md`), GT volume ×2.40, per-ours
> `root_err` fell **50.7→35.8%**, and the gate is re-baselined **Baroque 57 / Jazz 23 /
> Default 57** (`cc_gate_rebaseline_verify_report.md`). **The "root_err 2706 / all_differ 2576
> / 95.2% functional / m21-fixable 130" figures were computed on the BUGGY parser and are
> INVALID** — a large share of the old "functional residual" was the P1/P2 artifact this run
> fixed. So the residual must be **RE-DERIVED on the corrected metric FIRST (new Task 0)**
> before it can be decomposed. The original `cc_precision_headroom_dossier.md` is treated as
> **superseded/stale**, not a source of live numbers.

**READ-ONLY measurement + classification + reasoning. No build, no commit, no behavior
change.** Base = corrected-parser HEAD (the metric fixes — staged or, if the user has
committed, in HEAD; confirm which and report the base hash). Method A–H; never-guess in full
force — every classification **criteria-based and `sampled`/`inferred`-tagged**, not vibes.

The target mass is now **whatever Task 0 re-derives** as the corrected "neither" root-err
residual (the analogue of the old 2576, on the corrected metric) — where *both* we and
music21 miss DCML's root because DCML reads a *functional* root (cadential-6-4 dominant,
suspension resolution, applied/secondary root, pedal) the vertical sonority doesn't show.
**S1 tonicization (key_disagree, root-correct) is a separate functional slice already known
rule-reachable** (mechanical `V/V`; the comparator credits it) — confirm quickly (Task 1),
then spend the run on the corrected residual. (The old S1 count 1791 is also pre-fix —
re-count it in Task 0.)

Mandatory reads: `cc_metric_rebaseline_report.md` (the corrected metric + §3 corrected-headroom
direction) + `cc_gate_rebaseline_verify_report.md` (the 57/23/57 gate, ~95% ambiguity);
`cowork_target_architecture_review.md` (the literature ceiling: Temperley/Melisma + HarmAn
rule-based, AugmentedNet/RNBert neural full-RN numbers — the external yardstick);
`docs/back_half_design.md` §3 (the A/B fork + the B-trigger = "genuine ceiling").
(`cc_precision_headroom_dossier.md` may be read for METHOD only — its NUMBERS are stale.)

## Task 0 — Re-derive the headroom decomposition on the CORRECTED metric (NEW — do first)

The metric report (§3) gave only the *direction* (per-ours `root_err` 50.7→35.8%) and
explicitly deferred the full re-derivation. Do it now — this produces the target mass for
Tasks 1–2 and replaces the stale dossier numbers:

- On the corrected metric, recompute the `root_err` decomposition: total `root_err`, the
  `all_differ` ("neither" — we≠DCML AND music21≠DCML) count, and the `m21-fixable` count
  (music21 agrees with DCML, we don't). Report each as **NEW vs OLD (2706 / 2576 / 130)** so
  the artifact share the parser fix removed is explicit. [probe]
- Recompute the **functional-vs-vertical split** (the old "95.2% functional / 4.8% vertical"):
  how much of the corrected `root_err` is functional (DCML reads a functional root the
  sonority doesn't show) vs vertical (a genuine chord-identification miss). State the corrected
  percentages and how inflated the old 95.2% was. [probe]
- Recount **S1 tonicization** (key_disagree, root-correct) on the corrected metric (old 1791).
- **Rider (quick):** re-measure `analyze_inversion_errors.py` under the corrected parser on
  both presets (the old 24/13 · 35/7 three-way `bassIsRoot` split is stale/pending per the
  docs) and report the corrected split — closing that loose end while the corpora are loaded.

The corrected "neither" residual from this task is the **target mass** for Task 2.

## Task 1 — Confirm S1 is rule-reachable (quick, not the focus)

Sample ~8–10 S1 tonicization cases [probe]: confirm each is mechanically derivable —
the chord IS the secondary dominant/leading-tone of the next region's root within the
KeyArea (root + global-key already correct, only the `V/V`-vs-`II` label differs). Verdict:
S1 reachable by emission + KeyArea + a mechanical secondary-labeler (expected — confirm,
don't belabor). This bounds the *known-reachable* part of the functional headroom.

## Task 2 — Decompose the corrected "neither" residual three ways (the core)

Sample **≥40 cases** from the corrected "neither" residual re-derived in Task 0 (spread
across stems — and note any cases that the parser fix REMOVED from the old 2576, i.e. were
P1/P2 artifacts, vs genuine functional residual that survives; capture for each: our reading,
DCML reading, the region's chord tones, the surrounding regions, the local key). Classify
each into exactly one bucket, by **stated criteria**:

1. **RULE-REACHABLE** — DCML's functional root is derivable from chord + key + voice-leading
   + metric position by a rule a hand-built functional layer would implement. Sub-classify
   by rule-class and size each:
   - cadential-6-4 (I64 on strong beat over dominant bass → V);
   - suspension / accented NHT (the resolution pitch is the harmony);
   - passing / neighbor chord (the structural neighbors define the root);
   - applied/secondary (chord = V/x of the next root);
   - pedal point (bass ≠ harmony; upper voices define it).
2. **NEEDS-RICHER-MODEL** — the correct root requires sequence/phrase context no clean rule
   captures (the genuine **B-trigger**): e.g. long-range voice-leading, phrase-model
   expectation, or disambiguation only a trained model reliably gets. State *why* a rule
   can't reach it (not just "it's hard").
3. **GENUINE-AMBIGUITY / CONVENTION** — DCML's reading is one of *several defensible*
   readings; even a perfect model can't be uniquely "right" because expert annotators
   would disagree, OR it's a notation-vs-analyst convention (the 127 key-convention cases
   are the precedent). This is a **ceiling for EVERYONE, including B** — sizing it is
   decisive (it bounds what any approach can achieve). Criterion: would a second competent
   human annotator plausibly write our reading (or a third option) instead of DCML's?

Report the three-way split with counts (extrapolated from the sample, with the sample size
and confidence stated) + the rule-class breakdown of bucket 1.

## Task 3 — Calibrate against the literature ceiling (the external yardstick)

The decomposition is internal; anchor it externally [doc, + cheap probe if available]:
- Which buckets do **published rule-based functional analyzers** (Temperley/Melisma,
  HarmAn — part-1 review) handle? (cadential-6-4, applied dominants, suspensions are
  classic rule-based targets → if bucket 1 dominates, a hand-built functional layer
  reaches it = A.)
- Which require the **neural** systems (AugmentedNet/RNBert ~45–50% full-RN)? (If
  bucket 2 dominates → B's case.)
- **Optional cheap probe:** does music21's *Roman-numeral* analyzer
  (`roman.romanNumeralFromChord` / its RN analysis — DISTINCT from the chord-label
  `.music21.json` we use) reach any sampled bucket-1 cases? If a functional analyzer
  music21 already ships gets them, that's direct evidence they're rule-reachable. (Only if
  it's a quick, read-only probe — do not build a pipeline.)

## Task 4 — The OQ-1 verdict input

Synthesize: does the evidence **confirm A** (bucket 1 [rule-reachable] + bucket 3
[ambiguity ceiling for everyone] dominate; bucket 2 [needs-richer] is small → a hand-built
functional layer reaches the reachable part, and the residual is a ceiling B couldn't beat
either) — or **strengthen B** (bucket 2 is large → a learned model would reach mass the
hand-built path can't)? State it as the OQ-1 recommendation, with the sizes and the honest
confidence (sampled). Either way, report what the *total* hand-built-reachable functional
headroom is (S1 + bucket 1) vs the everyone-ceiling (bucket 3) vs the B-differentiated mass
(bucket 2).

## Deliverable — `cc_functional_residual_dossier.md` (REPLACES the prior stale version)

§0 the Task-0 corrected-metric re-derivation (NEW vs OLD root_err/all_differ/m21-fixable +
the corrected functional-vs-vertical split + S1 recount + the analyze_inversion re-measure);
§1 S1 reachability confirm; §2 the corrected-residual three-way split + rule-class breakdown
(criteria stated, sample size + confidence); §3 literature calibration (+ any music21-RN
probe); §4 the OQ-1 verdict input (A-confirmed vs B-strengthened, with sizes); §5 unknowns.
Every number `[probe]`; every classification `sampled` with the criterion that placed it.
(Note: the existing `cc_functional_residual_dossier.md` from the pre-fix run is stale —
overwrite it; its provisional "OQ-1 = A" was on the buggy metric.)

Stop conditions: bucket 2 (needs-richer-model) dominating — report LOUDLY, it flips OQ-1
toward B and reshapes the whole back half; the rule-reachable-vs-ambiguity line proving
unprincipled on real cases (give the criterion that's failing, don't force a split);
scope creep into building any functional rule (this run classifies only).
