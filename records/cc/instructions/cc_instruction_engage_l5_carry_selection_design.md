# CC Instruction — Engage arc #9: Layer-5 engagement design, Part 1 — the CARRY-and-SELECTION architecture (read-only design)

> **ACTIVE DISPATCH (Cowork, 2026-07-07).** Stage 2 of the ratified plan (`cowork_engage_arc_plan.md`) opens.
> This is Part 1: **how engaged Layer 5 reads the decoder's governed carry and selects among the carried
> readings by joint consistency.** The downstream Layer-5 pieces (the quality-from-key owner FQ-2, pedal
> detection's home, the joint key-and-chord step, the F-B annotate redesign) are **enumerated here for
> follow-on passes, NOT resolved** — this part is the carry + selection core they all sit on.
>
> **READ-ONLY architectural design (#8's design phase). No `src/` change, no build, no corpus write.** The
> deliverable is a design doc.
>
> **★ STRUCTURE ONLY — constants are precision-phase (R5). This is NOT inference work (#8).** Design the
> *architecture* of the selection — the evidence channels it consumes, how the concerns compose, the
> confidence contract it emits — grounded in published theory (#1) and the existing confidence contract.
> **Do NOT fit constants, tune thresholds, or chase cases** — declared comparability before tuned optimality
> (R5); the fitting is the later precision phase. If a step requires a fitted value to proceed, declare the
> *shape* and mark the constant precision-phase; do not fit it.
>
> **Build on established fact (#1), extend — do not re-derive (#6):**
> - The **decoder's clean carry** (`chord/chordslicedecoder.cpp:746-789` topK-on-distinct-voicings ∪
>   principled incumbent-carry; `:927-930` diff-root read) — the audit's confirmed clean-target and the
>   factual basis of the carry contract.
> - The **built-but-dormant Layer 5**: `function/functionoutput.h` (`FunctionLayerOutput`), 
>   `function/functionresolver.cpp` (`resolveCarriedReadings` — how it currently selects; the F-B override,
>   measured net-harmful → annotate-not-override), the existing L5 design doc + `cowork_confidence_contract.md`
>   (the frames §4, R4–R6 §5, the calibration obligations §6).
> - The **research grounding** `cowork_functional_analysis_research_grounding.md` (§2 select by JOINT
>   CONSISTENCY across key/root/inversion/bass, not by strengthening one score; bass + spelling load-bearing;
>   §3 joint > sequential; §4 the exclusion tail).
> - The **fan-out fact** (`cc_engage_fanout_measure_report.md`): ~2 distinct roots/slice (median), a **≥3rd
>   distinct root on ~25% Baroque/Default, ~16% Jazz** — the load-bearing exclusion tail the cap+append cannot
>   carry (#12).
>
> **Current state:** HEAD `81b1ec3043`, branch `master`, fork-only, ahead 0. Both stops green.
> **VS Code bash rules:** `; echo "exit:$?"`; large output → file + `head`. **Do NOT bash to read files.**

---

## Task 1 — inventory the dormant Layer 5 at the code (#1, don't assume)
Ground, at the source: what `resolveCarriedReadings` already does (how it selects among carried readings
today — the frames it consumes, the confidence it combines, the F-B override's place), what `FunctionLayerOutput`
carries, and how the confidence contract's frames/rules (§4/§5) are realized in code. State what is already
built vs what engagement must add — do not design from scratch what already exists.

## Task 2 — the carry contract (decoder → Layer 5)
Design what Layer 5 reads from the decoder's governed carry, grounded in the fan-out fact:
- The per-slice candidate set is best thought of in **distinct roots** (the meaningful axis — ~2 typical, a
  ≥3rd on ~25%), each with its variants and its confidence; not a raw top-N-by-score list.
- **The exclusion tail (#12):** the ruled-out / low-confidence roots are carried at low confidence, not
  dropped — the ≥3rd-root minority is exactly where selection and the joint step earn their keep.
- Confirm the decoder's carry (topK ∪ incumbent) actually provides this distinct-root-preserving set; name
  any gap (e.g. does topK-on-voicings guarantee the distinct roots survive, or is a distinct-root guarantee
  owed?). Ground at `chordslicedecoder.cpp`.

## Task 3 — the selection architecture (STRUCTURE only; R5)
Design how engaged Layer 5 chooses among the carried readings:
- **By joint consistency across key / root / inversion / bass** (the research's decisive lesson — the payoff
  is the mutually-consistent reading, not a stronger single score), reasoning over the **graded distribution
  including the exclusion tail** (#12).
- **Reconcile with the existing frames + the F-B finding:** the current progression-plausibility override is
  measured net-harmful and uncorrelated with root-correctness — so the design consumes bass / spelling /
  cadence / joint-consistency as the load-bearing channels, and re-frames F-B as an honest annotation, not an
  override (the settled annotate-via-open-mark disposition).
- **The confidence Layer 5 emits** — the frames/squashes it publishes (per the confidence contract R4–R6).
- **Declare shapes; mark every constant precision-phase (R5). No fitting.**

## Task 4 — layer boundaries, engagement gaps, and the enumerated downstream pieces
- **Layer boundaries (#7):** what belongs to Layer 5 (selection over L4's carry → the functional analysis) vs
  Layer 4 (the decoder's carry) vs the joint step; the acyclicity rule respected.
- **Engagement gaps:** what the dormant Layer 5 is MISSING for production engagement (the carry wiring, pedal
  detection as a reader-over-carry — the decoder has none yet, the audit flagged this).
- **The downstream design pieces this part DEPENDS ON — enumerate, do not resolve here:** the quality-from-key
  owner (FQ-2), pedal detection's home, the joint key-and-chord step (O-18), the F-B annotate mechanics. Name
  which carry-and-selection decisions hinge on each, so the follow-on passes have their agenda.

## Task 5 — doc + fold + push
1. **Design doc** `cowork_layer5_engagement_design.md` (force-add; or extend the existing L5 design doc if that
   is the cleaner home — state which and why, #6): Tasks 1–4.
2. **Report** `cc_engage_l5_carry_selection_design_report.md` (force-add): what the design settles, the
   grounding sources, the enumerated follow-on agenda, all SHAs.
3. **Sandwich (trivial — read-only):** no `src/`; both stops untouched; suites unchanged (no build).
4. **Fold** (`docs(cowork):`): the design doc + report · `STATUS.md` · `COWORK_HANDOFF.md` ·
   `cowork_stage5_fitter_design.md` (engage observation) · this instruction (force-add).
5. **Push fork-only** — never toward `upstream`/`musescore/MuseScore` (`cfc7eb5e39` HARD STOP).

## STOP conditions
- Any `src/` change, build, corpus write, or fit/tune of any constant (STRUCTURE only — R5; #8).
- Resolving a downstream concern-owner (quality-from-key / pedal / joint step / F-B mechanics) here — those
  are follow-on passes; enumerate only.
- Any design claim not grounded at the code / the contract / the research (#1) — flag UNCLEAR, do not assume.
- Designing from scratch what the dormant Layer 5 already builds (#6 — inventory first).
- Any push toward `upstream`/`musescore/MuseScore`.

## Acceptance
The dormant Layer 5 inventoried at code (built vs owed) ✓ · the carry contract designed on the distinct-root
fan-out fact with the exclusion tail preserved (#12), decoder gap named ✓ · the selection-by-joint-consistency
architecture (structure only, constants precision-phase R5), reconciled with the frames + the F-B
annotate finding ✓ · layer boundaries + engagement gaps + the enumerated downstream agenda ✓ · design doc +
report + fold with SHAs ✓ · no src/build/corpus/fit; both stops green; pushed fork-only ✓.

*Cowork, 2026-07-07. Engage arc #9 — Layer-5 engagement design Part 1 (carry + selection), read-only,
structure-only. On CC's report: Cowork verifies at objects → presents the design + the follow-on agenda
(concern-owners, joint step, F-B) to the user for the next Part.*
