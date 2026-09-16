# CC Instruction: Precision-metric design investigation (design-only, ratification-gated)

## Context

The headroom dossier (verified) re-grounded the back half: precision lives in the key
path (Stage 4) + functional layer (Stage 6); the music21-filtered gate sees 4.8% of the
root-error mass. **Decision (user, 2026-06-13): before committing the Stage-4/5/6 order,
INVESTIGATE the metric design** — because the instrument that would measure Stage 4/6
success doesn't fully exist, and (the named chicken-and-egg) a metric that scores
*functional* precision needs a functional-label vocabulary the pipeline doesn't emit yet,
which is itself Stage-6 output. You cannot aim the back half without resolving what its
success is measured against.

**READ-ONLY design + scoping. No production code, no behavior change, no commit beyond a
design doc.** Base `a652dc1ba7`. Method A–H. The deliverable is a *design*, ratified
before any metric is built.

The question: **what is the measurement instrument for "maximally precise inference of
mode, functional chord, actual chord" — what already exists, what is genuinely new, and
what is gated on co-designing the Stage-6 label vocabulary?**

Mandatory reads: `cc_precision_headroom_dossier.md` (the error structure this metric must
see); `cc_stage1d_report.md` §1 (the EXISTING metric definitions — `compare_rn` buckets,
`align_dcml_regions`, three-way); `cowork_corpus_audit.md` (music21-NOT-ground-truth,
DCML-only mandate, 326/353); `docs/p3_granularity_ab_3_1b.md` + 2.2-i dossier (the ~7×
granularity gap); the redesign_plan A3 section (rn_agree baseline, the `compare_rn`
design); `dcml_parser.py` + `compare_rn.py` (what the comparison actually computes).

## Task 1 — What already exists (don't rebuild what's there)

Establish precisely [code/probe]:
1. **`compare_rn` IS already a DCML-only metric** (no music21 filter — the filter lives in
   `characterise_bir_false`/`analyze_inversion_errors`, the BIR gate). Confirm: its
   buckets (rn_agree / key_disagree / quality_disagree / root_err) compare OUR output
   directly to DCML Roman numerals. So "remove the music21 filter" = "use compare_rn,
   not the BIR gate." State exactly what compare_rn measures and on which corpora it runs
   today (TSV-only → excludes Bach; the dossier wired WiR rntxt for Bach — formalize what
   that wiring is and whether it should become a committed `compare_rn` mode).
2. **What compare_rn does NOT yet measure**: enumerate the gaps against the headroom
   axes — (a) granularity (it scores whatever regions exist; no granularity-robust unit);
   (b) tonicization/secondary labels (does `classify_pair` credit a correct `V/V` if we
   emitted it? trace the degree-string comparison — the gap is likely that we don't EMIT
   secondaries, not that the metric can't score them); (c) cadence / figured-bass detail.

## Task 2 — The granularity-robust unit (the genuine new design work)

The 2.2-i ~7× gap means batch and section give different numbers and "one lies." Design
the granularity-robust measurement [design]:
- What is the scoring UNIT — per-region (whose boundaries differ batch/section), per-beat,
  per-tick, duration-weighted? Argue from what "user-visible precision" means (the
  status-bar is clicked-note = fine; the chord track is section = coarse — §2.2-i / 3.1b).
- How does it avoid the denominator-shift artifact (3.1b: whole-score "improved
  consistency" only by growing the denominator)? The metric must be invariant to
  segmentation choice or explicitly report the granularity it scores at.
- Reuse `align_dcml_regions` (time-overlap) as the substrate; the unit is the design
  question, not the comparator.

## Task 3 — The functional-label chicken-and-egg (the reason this is design-first)

To measure Stage-6 precision (tonicization 17.7%, the biggest slice) the metric must
compare a functional label (`V/V`, `cad64`, `It6`) against DCML's Roman numeral. But the
pipeline doesn't emit those labels yet — Stage 6 will. So [design]:
1. Define the **label-vocabulary CONTRACT**: the set of functional labels Stage 6 will
   emit and the metric will score, mapped to DCML's RN syntax (secondaries `V/x`,
   applied `viio/x`, cadential 6-4, aug6 It/Fr/Ger, Neapolitan, modal mixture). This is
   co-designed once, here — it is simultaneously Stage-6's output spec and the metric's
   input spec. (dcml_parser already parses DCML's side — Task 1 maps what it exposes.)
2. Define the **incremental measurability ladder**: what is scorable NOW against DCML
   with no new labels (root; root+coarse-quality; key/degree — all in compare_rn), vs
   what unlocks only as Stage 6 emits each label class. So Stage 4 can be measured
   immediately (key/degree axis exists), and Stage 6 is measured class-by-class as it
   ships — not blocked on a big-bang label set.
3. State the **objective function** Stage 5 fitting optimizes (which buckets, which
   granularity, which weights) — and confirm it is DCML-only and granularity-robust per
   Tasks 1–2.

## Task 4 — Recommendation

Synthesize into a concrete metric design: what to BUILD (the granularity-robust DCML
metric + the committed Bach-WiR mode + the label-vocabulary contract), what to REUSE
(compare_rn's buckets + align_dcml_regions), the incremental ladder (so Stage 4 is
measurable before Stage 6 vocab exists), and whether this confirms or adjusts the
re-grounded order (does "metric first" stand, or does it interleave with Stage 6 because
the functional labels are co-designed?). The decision is Cowork/user's.

## Deliverable — `docs/precision_metric_design.md` (DRAFT, uncommitted) + inline report

§1 what exists (compare_rn as the DCML metric; the Bach-WiR wiring); §2 the
granularity-robust unit design; §3 the label-vocabulary contract + incremental
measurability ladder + the Stage-5 objective; §4 build-vs-reuse + ordering recommendation
+ open questions. Every existence claim [code/probe]; every design choice argued; the
chicken-and-egg resolution explicit.

Stop conditions: discovering compare_rn does NOT measure what Task 1 assumes (report —
it changes the build/reuse split); the granularity-robust unit requiring a production
change to even prototype (design it on paper, don't build); any point where the
label-vocabulary contract can't be pinned without Stage-6 design decisions that are
themselves forks (surface them as OQs, don't guess).
