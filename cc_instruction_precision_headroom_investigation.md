# CC Instruction: Precision-headroom investigation — re-ground Stages 4–6 on measured error structure

## Context

Decision (Cowork+user, 2026-06-13): **beam-widening is shelved** (its Δ=+7a
justification is falsified — verified; beam>1 is beam-1-substitutable for all currently
motivated work). Per the user's directive — *investigations first; long-term; major
redesign OK; minimum surprises; maximum precision* — the next action is **not a build**.
It is an investigation that maps where inference accuracy actually lives, so the back
half of the roadmap (Stages 4–6) is grounded on measured headroom, not the original
roadmap's assumptions.

**This is a READ-ONLY measurement + analysis task. No production code, no behavior
change, no commit beyond the dossier.** Base: `a652dc1ba7`. Method A–H. Probes via the
existing `batch_analyze` + the metric scripts; the harness must stay inert/reverted.

The lodestar question: **where is the realistically reachable headroom toward
maximally-precise inference of (mode, functional chord, actual chord), and which layer
unlocks each slice?**

Mandatory reads: `cowork_target_architecture_review.md` (the part-1 lattice/decode
target + the literature accuracy points); `docs/implementation_roadmap.md` Stages 4–6;
the metric definitions (`cc_stage1d_report.md` §1 — lenient-OR, three-way, the buckets);
`cowork_corpus_audit.md` (music21-NOT-ground-truth; 326/353 WiR coverage; the DCML-only
mandate); the 3.1b granularity A/B (`docs/p3_granularity_ab_3_1b.md`); the redesign_plan
A3 rn-baseline section (rn_agree 27.6%, key_disagree 15.4%, quality_disagree 6.3%).

## Task 1 — Measure the error structure against HUMAN ground truth (DCML), honestly

The gate metrics are music21-filtered and batch-granularity — both flatter than reality
(corpus audit; 2.2-i). Measure the UNFILTERED human-adjudicated picture:

1. **Pick the metric stance deliberately and state it:** DCML-only (no music21 filter);
   the user-facing config (Default prefs / `--preset Default`); and report BOTH batch
   and section granularity (the 2.2-i ~7× gap means one number lies — show both, name
   which is user-visible). Use the existing `compare_rn` / `compare_analyses` machinery;
   do not invent a metric (if a granularity-robust measure doesn't exist yet, say so and
   use the best available, flagged — designing it is Stage-5 scope).
2. **Decompose the total disagreement mass** into the three target axes, each as a % of
   aligned regions with absolute counts, on the broadest corpus you can run cheaply
   (Bach WiR is the gate set; if the non-Bach DCML TSV corpora are cheaply runnable,
   include them — more human data per the corpus audit C5, but cost-box it):
   - **mode/key** errors (key_disagree class — wrong scale-degree on an agreed root);
   - **functional chord** errors (root agrees, but quality/extension/inversion or
     functional role wrong — the quality_disagree + the implied-7th/modal-mixture
     "convention gap" buckets);
   - **actual chord (root)** errors (BIR=false / root_err — the root PC itself wrong);
   - and the **"neither matches DCML"** residual the 3.1b A/B found at ~40% on
     root-differing ticks — quantify it corpus-wide and characterize what it IS (both
     our reading and music21 disagree with DCML → functional/voice-leading readings
     vertical analysis can't reach? cadential 6-4, secondaries, pedal? sample and class).

## Task 2 — Map each error slice to its unlocking mechanism (the re-grounding)

For each slice from Task 1, the load-bearing analysis: **what would actually fix it, and
is that mechanism reachable?** Classify every slice into:
- **Emission reweight** (Stage 5 — a vertical/template scoring term is mis-tuned;
  sample to confirm);
- **Transition reweight** (Stage 5 — rcb / resolution / step edges, incl. the Δ=+7a
  rcb-suppression that the falsified beam can't do; this is where Δ=+7a now lives);
- **Key path** (Stage 4 — the key/mode HMM; the key_disagree mass; quantify how much of
  the total rides on key being wrong upstream);
- **Functional layer** (Stage 6 — T/S/D, secondaries, cadence, aug6/Neapolitan, the
  implied-7th convention gap; the rn_agree ceiling);
- **Segmentation** (granularity — joint seg+label, beyond the current plan);
- **Structural ceiling** (genuinely unreachable by any planned layer — name it so we
  don't chase it).

Per slice: estimated size (% of total reachable headroom), the evidence, and the
confidence of the classification (sampled-and-verified vs inferred).

## Task 3 — The strategic recommendation (re-grounded roadmap)

Synthesize: given the headroom map, what is the highest-precision-per-effort ordering of
Stages 4/5/6 (and the deferred beam, and joint segmentation)? The original roadmap
assumed 3.2→3.3→…→4→5→6; the falsified beam + measured headroom may reorder this
(e.g. if key_disagree dominates, Stage 4 leads; if the functional/convention gap is the
ceiling, Stage 6 is where precision lives and Stage 5 fitting is the enabler). Major
redesign of the back half is explicitly on the table (user directive). Recommend, with
the measured basis; the decision is Cowork/user's.

Also state: what beam-widening would need to become worthwhile (the "search genuinely
matters" case), so it's revisited on evidence, not forgotten.

## Deliverable — `cc_precision_headroom_dossier.md`

§1 metric stance (stated, justified) + the error-structure decomposition (the three
axes + the "neither" residual, batch AND section granularity, DCML-only, Default
config, with counts); §2 the slice→mechanism map with sizes and confidences; §3 the
re-grounded roadmap recommendation + the beam-revisit trigger; §4 unknowns / what
couldn't be measured cheaply and why. Every number [probe]; every classification
sampled-or-flagged.

Stop conditions: a metric run that would require a production change to measure (report
the obstacle, don't hack); any slice where the mechanism classification would be a guess
(mark it "needs a deeper probe," don't assign it); scope creep into actually BUILDING
any fix (this run only measures and maps).
