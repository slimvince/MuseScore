# CC Instruction — Engage arc #10: the JOINT key-and-chord step — architecture design (read-only)

> **ACTIVE DISPATCH (Cowork, 2026-07-07).** The next Stage-2 design piece, chosen by the principles (#4 the
> biggest precision lever; #7 the upstream foundation Layer-5 selection sits on; #2 the specific owed
> question; #12 the mechanism that uses the preserved exclusion tail). **This DESIGNS the joint step's
> architecture; it does NOT build it.** The build is a later algorithmic-completion step (E4-adjacent) — the
> earlier C3 measurement's "building the joint step is forbidden" was in a *measurement* dispatch; **designing
> it is exactly the architectural-design phase (#8) we are in.**
>
> **The step, defined:** the pipeline today decides **key first, then chord** and cannot re-decode the chord
> under alternative keys (C3 measurement, Verdict 3 — the per-key chord re-decode is the owed step). This step
> decides **key and chord TOGETHER** where they are genuinely coupled — resolving the ~25% of slices where a
> ≥3rd distinct root clears threshold (the fan-out fact).
>
> **READ-ONLY architectural design. No `src/` change, no build, no corpus write.** Deliverable = a design doc.
>
> **★ STRUCTURE ONLY — constants precision-phase (R5). NOT inference work (#8).** Design the *architecture* —
> where the step lives, how key and chord couple, what it reads/emits, what must be built — grounded in
> published theory (#1) and the existing structures. **Declare shapes; do not fit constants, tune, or chase
> cases.**
>
> **Build on established fact (#1), extend — do not re-derive (#6):**
> - **The research** `cowork_functional_analysis_research_grounding.md` §3 (joint > sequential; the recurring
>   recipe = a **beam of (key, chord) hypotheses** + a **key-transition prior that penalizes rapid key
>   flip-flop** + chord re-decoded under alternative keys; Raphael & Stoddard's single joint `(key, chord)`
>   hidden state; Wu & Yoshii's parallel/branching/sequential taxonomy; magnitude realism — the win is
>   qualitative, on the hard cases).
> - **The C3 definition** `cowork_confidence_contract.md` §6-C3 (the trigger: L3 key confidence below its bar
>   AND the chord decision sensitive to the carried key alternatives — a different carried key flips the
>   chord) + the C3 measurement `cc_engage_c3_measurement_report.md` (why the current pipeline can't compute
>   it).
> - **The existing layers at code:** L3 key (`key/keymodesequence*`, the carried `HarmonicRegion.keyAlternatives`
>   / `keyConfidence`), L4 chord (`chord/chordslicedecoder*` — decodes the chord under a given key), the
>   Layer-5 engagement design Part 1 (`cowork_layer5_engagement_design.md` — L5 selects within a fixed key,
>   which this step feeds).
>
> **Current state:** HEAD `32709a9e7a`, branch `master`, fork-only, ahead 0. Both stops green.
> **VS Code bash rules:** `; echo "exit:$?"`; large output → file + `head`. **Do NOT bash to read files.**

---

## Task 1 — placement in the architecture (#7 — the load-bearing layer question)
Where does the joint step live? Decide, grounded at the existing L3/L4 structures + the acyclicity rule:
- Is it a **unified `(key, chord)` decision** (Raphael & Stoddard's single joint state — collapsing the
  current key-then-chord split), or the current L3/L4 kept separate with a **bounded coupling** (a beam /
  fixpoint over carried keys) that respects the cross-layer acyclicity rule (no L3←L4 cycle)?
- Name what it consumes: L3's carried key alternatives + confidence, L4's per-key chord decode. State how it
  avoids re-introducing the very cross-layer reach-in the structural audit flagged.

## Task 2 — the coupling mechanism (structure only, R5)
Design, from the research recipe: a **beam of (key, chord) hypotheses**; the chord **re-decoded under each
carried key alternative** (the owed per-key re-decode); a **key-transition prior** that penalizes implausibly
rapid key change; how key evidence and chord evidence **compose** into the joint score; the confidence it
publishes (a declared Class-M joint-decision confidence, per the contract R4–R6). **Shapes declared; every
constant marked precision-phase. No fitting.**

## Task 3 — the trigger (the coupled minority) and the interface
- **Trigger:** ground the C3 definition (fire where key is uncertain AND the chord flips under a carried key)
  — the "genuinely-coupled minority," not every slice. State the trigger's inputs and where they come from.
- **Interface (#7):** how the step feeds Part 1's Layer-5 selection (it settles the region key L5 then selects
  within), how it reads L3's carried keys and L4's carry, the acyclicity kept.

## Task 4 — what must be BUILT (design the owed build, do not build it)
The C3 measurement found the per-key chord re-decode is computed nowhere. Specify the **minimal** build the
step needs (the per-key re-decode entry into the decoder; the beam/coupling driver; the trigger computation),
and where each belongs by layer. This is the design of the E4-adjacent build event — enumerated, not built.

## Task 5 — facts owed / open questions (#5)
Flag any design point that rests on a fact we do not yet hold (e.g. how often the C3 trigger would fire on the
corpus; the expected coupling benefit) as an **owed measurement**, not an assumption — the read-only
instruments that would settle each, for a later step. Do not assume.

## Task 6 — doc + fold + push
1. **Design doc** `cowork_joint_key_chord_design.md` (force-add; or a section of the L5 engagement doc if
   cleaner — state which and why, #6): Tasks 1–5.
2. **Report** `cc_engage_joint_key_chord_design_report.md` (force-add): what the design settles, grounding,
   the owed-build spec, the owed-measurement list, all SHAs.
3. **Sandwich (trivial — read-only):** no `src/`; both stops untouched; suites unchanged (no build).
4. **Fold** (`docs(cowork):`): the design doc + report · `STATUS.md` · `COWORK_HANDOFF.md` ·
   `cowork_stage5_fitter_design.md` (engage observation) · this instruction (force-add).
5. **Push fork-only** — never toward `upstream`/`musescore/MuseScore` (`cfc7eb5e39` HARD STOP).

## STOP conditions
- Any `src/` change, build, corpus write, or fit/tune of a constant (STRUCTURE only — R5; #8).
- Building (not designing) the joint step, or any per-key re-decode wiring — this dispatch designs the owed
  build, it does not do it.
- Any design claim not grounded at the code / contract / research (#1) — flag UNCLEAR / owed-measurement.
- A placement (Task 1) that re-introduces a cross-layer cycle (#7) — flag it.
- Any push toward `upstream`/`musescore/MuseScore`.

## Acceptance
The step's placement decided vs the acyclicity rule (#7), grounded ✓ · the coupling mechanism (beam +
per-key re-decode + key-transition prior + composition + confidence) designed structure-only, constants
precision-phase (R5) ✓ · the trigger grounded in C3 + the interface to Part-1 selection ✓ · the minimal owed
build specified by layer (not built) ✓ · owed-measurements flagged, not assumed (#5) ✓ · design doc + report
+ fold with SHAs ✓ · no src/build/corpus/fit; both stops green; pushed fork-only ✓.

*Cowork, 2026-07-07. Engage arc #10 — the joint key-and-chord step, architecture design (read-only,
structure-only). The biggest precision lever, designed on the foundation Part 1 established. On CC's report:
Cowork verifies at objects → presents the design + the owed build/measurements to the user.*
