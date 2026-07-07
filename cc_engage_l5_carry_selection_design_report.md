# CC Report — Engage arc #9: Layer-5 engagement design Part 1 (carry + selection)

**Dispatch:** `cc_instruction_engage_l5_carry_selection_design.md` (Cowork, 2026-07-07).
**Design doc delivered:** `cowork_layer5_engagement_design.md` (NEW; force-added).
**HEAD at design:** `81b1ec3043`, branch `master`, fork-only, ahead 0. Corpus frozen `c50002fee1`.
**Nature:** READ-ONLY architectural design (Stage 2, #8's design phase). No `src/` change, no build, no corpus
write, **no constant fitted or tuned** (structure only — R5).

---

## 1. What the design settles

Part 1 of the Layer-5 engagement design — the **carry + selection core** the downstream pieces sit on:

1. **The dormant Layer 5 inventoried at code (built vs owed).** `resolveCarriedReadings` (the per-`AmbiguityKind`
   selection + the F-B override), `assembleFunctionOutput` (§7 pure assembly, additive over L4), the `FunctionSlice`
   input contract, and the confidence frames (F-A/F-B, D-L5a closed, D-FS open) are **built and dormant**;
   engagement wires an existing pipeline, it does not design from scratch (#6). The **owed** delta: populate the
   carry from the live decoder, generalize selection to the full distinct-root carry, re-frame F-B, add pedal
   detection as a reader-over-carry.
2. **The carry contract designed on the distinct-root fan-out fact (#12).** Layer 5 reads a **distribution over
   distinct roots** (median ~2, a ≥3rd root on 25 %/16 %/25 %), each root with its variant set and graded
   confidence; the **exclusion tail (ruled-out / low-confidence roots) is carried, not dropped**. The **decoder gap
   is named**: `topK` caps on **voicings** (`sameChordVoicing`, default 6), not roots, so the ≥3rd distinct root is
   **not structurally guaranteed** to survive — a **distinct-root-preserving carry is owed at Layer 4/E4** (the
   incumbent-carry guarantees the prevailing root and readingB names one alternate on abstains, but neither
   guarantees a third, and Commit slices name no alternate at all).
3. **The selection-by-joint-consistency architecture (structure only, R5).** Select by **joint consistency across
   key / root / inversion / bass** over the graded distribution incl. the exclusion tail. Evidence channels ranked
   **load-bearing-first**: bass/inversion, spelling, key-consistency, cadence — with **licensed progression demoted
   to a tie-break among already-consistent readings, never an override lever**. This **re-orders** the as-built
   resolver (which leads with the weak progression channel) and **reconciles with the settled F-B annotate-not-
   override finding**: F-B carries the L4 commit unchanged and surfaces contradiction as an honest open mark. The
   confidence L5 emits: the built `combinedBoundary` (D-L5a) plus a NEW declared Class-M joint-consistency selection
   margin (squash shape declared, constant precision-phase).
4. **Layer boundaries, gaps, downstream agenda.** L4 = the carry (under the L3 key); L5 = selection within a fixed
   region key → the functional analysis; **the joint key↔chord step (O-18/C3) is a distinct downstream step**, not
   L5 selection; acyclicity kept (the §8 forward-only bounded recompute). Engagement gaps: carry wiring, the
   distinct-root guarantee, pedal detection (decoder has none), F-B annotate mechanics, D-FS commensurability. The
   downstream pieces are **enumerated with each hinge named, not resolved** (FQ-2 quality-from-key owner; pedal
   detection's home; O-18/C3 joint step; F-B annotate mechanics).

## 2. Grounding sources (every design claim tagged)

- **Code** (read at source): `functionresolver.cpp/.h` (`resolveCarriedReadings`, `resolveAbstained`,
  `attemptFineGrainOverride`, `FunctionSlice`, `ResolvedReading`); `functionoutput.h` (`assembleFunctionOutput`,
  `FunctionConfidence`, `combinedBoundary`, `FunctionLayerOutput`); `chordslicedecoder.h`/`.cpp:700-975` (the carry
  build `:746-789`, `topK=6`, `nameOpenQuestion` diff-root read `:929-931`, the value-type contract).
- **Contract:** `cowork_confidence_contract.md` §3 (L3/L4/L5 rows), §4 (F-A/F-B frames), §5 (R4–R6 / U2), §7
  (D-L5a closed, D-FS open), §6 (C1/C3 Stage-5 calibration).
- **Research:** `cowork_functional_analysis_research_grounding.md` §1 (progression uncorrelated with root
  correctness; bass/spelling load-bearing), §2 (select by joint consistency — ChordGNN/AnalysisGNN), §3 (joint
  key-chord beam), §4 (implications).
- **Fan-out fact:** `cc_engage_fanout_measure_report.md` (median 5/4/5 readings, distinct roots 2/1/2, ≥3rd root
  25.1 %/16.1 %/24.9 % — the load-bearing exclusion tail).
- **F-B disposition:** `cowork_fb_redesign_design.md` (§3.D-1 annotate-not-override settled; §3.D-2 C3 restriction
  un-computable until the joint step exists; net-harm −756).
- **Signed L5 spec:** `cowork_layer5_function_design.md` §5.5 / §7 / §8 / §9-D7 / §15-2 (referenced, not restated).
- **Plan:** `cowork_engage_arc_plan.md` Stage 2; `cowork_structural_integrity_audit.md` (the audit gaps).

## 3. Doc-home decision (#6)

A **NEW doc** `cowork_layer5_engagement_design.md`, not an edit of the signed `cowork_layer5_function_design.md`.
Rationale: the signed spec is *what the dormant build IS*; the engagement design is a distinct concern — *how it
wires to the decoder's carry and how selection is re-architected over the full fan-out and reconciled with the F-B
annotate finding*. Folding engagement into the signed spec would mix "built" with "how it engages" and muddy signed
provenance. The new doc references the signed spec's sections rather than restating them (one home per concern).

## 4. The enumerated follow-on agenda (for the next Parts)

| Piece | Hinge on the carry/selection |
|---|---|
| **FQ-2 quality-from-key owner** | §3.2's key-consistency channel reads quality-in-key; an un-owned signal until FQ-2 fixes the owner |
| **Pedal detection's home** | whether pedal is a Layer-4 carried slice attribute or an L5 reader-over-carry changes the carry contract (§2) + the selection channels (§3.2) |
| **O-18 / C3 joint key↔chord step** | the exclusion tail (#12) is carried *so the joint step can re-rank the key under the carried chord alternatives* — un-computable today; carry designed to feed it |
| **F-B annotate mechanics** | the advisory field + contract §4 re-declaration + spec edits — a separately-ratified build event; selection structure is fixed, mechanics are the follow-on |

## 5. Sandwich (trivial — read-only)

- **No `src/` change** — no build, no test run needed (both regression stops computed from `.ours.json` that is
  untouched; production byte-identical by construction — nothing in the pipeline changed).
- **Both stops untouched/green** by construction (no code path altered): class-(b) duration non-increase trivially
  holds (+0/−0); characterise **52/24/52** unchanged.
- **Suites unchanged** (no build): composing 1101 / notation 53 / pipeline_snapshot 11 — not re-run (no code
  delta; a build/test run would be a no-op vs `81b1ec3043`).

## 6. SHAs / fold

- **Design doc:** `cowork_layer5_engagement_design.md` (force-added).
- **Report:** this file (force-added).
- **Fold (`docs(cowork):`):** design doc + report · `STATUS.md` · `COWORK_HANDOFF.md` ·
  `cowork_stage5_fitter_design.md` (engage observation) · the instruction `cc_instruction_engage_l5_carry_selection_design.md`
  (force-add).
- **Push:** fork-only (`origin` = `slimvince/MuseScore`); `upstream`/`musescore/MuseScore` untouched
  (`cfc7eb5e39` HARD STOP honored).

*Cowork, 2026-07-07. Arc #9 — carry + selection design, read-only, structure-only, both stops green. On CC's
report: Cowork verifies at objects → presents the design + the follow-on agenda (concern-owners, joint step, F-B)
to the user for the next Part.*
