# CC Instruction — Engage arc #11: Layer-5 design — pedal home + F-B annotate mechanics (read-only; closes Stage 2)

> **ACTIVE DISPATCH (Cowork, 2026-07-07).** The last two Layer-5 engagement design pieces Part 1 enumerated.
> Settling them **closes the Stage-2 design phase** — after this, the whole Layer-5 + joint-step architecture
> is designed and Stage 3 (algorithmic completion / the builds) opens with nothing left undesigned (#8).
>
> **READ-ONLY architectural design. No `src/` change, no build, no corpus write. STRUCTURE ONLY — constants
> precision-phase (R5); NOT inference work (#8).** Deliverable = design (extend `cowork_layer5_engagement_design.md`
> — state if a section vs a new doc is cleaner, #6).
>
> **Build on established fact (#1), extend — do not re-derive (#6). Read first:**
> - **Pedal:** the structural audit's pedal finding (`cowork_structural_integrity_audit.md` §1.1 #7 + §1.3 —
>   pedal detection `chordpostpasses.cpp:209-281` currently **clobbers** the shared `results` (`= pass2`),
>   **re-implements** the diff-root scan, and **defensively disables** the append: a detection concern
>   *mutating the winning identity in place*) + the decoder carry (`chordslicedecoder.cpp` — has **no** pedal
>   detection yet, the named gap).
> - **F-B annotate:** the settled disposition `cowork_fb_redesign_design.md` §3.D-1 / §4.2 (demote the
>   net-harmful override to an honest annotation, carrying the L4 reading unchanged + flagging the
>   contradiction as calibrated uncertainty, #12) + the **existing open-mark machinery** (`function/functionoutput.h`
>   `openMark`; the §15-13 both-licensed open-mark; the §8 case-3 honest-carry) + `cowork_confidence_contract.md`
>   §4 Frame F-B.
> - Part 1 `cowork_layer5_engagement_design.md` (the carry + selection these fit into).
>
> **Current state:** HEAD `2c550ec327`, branch `master`, fork-only, ahead 0. Both stops green.
> **VS Code bash rules:** `; echo "exit:$?"`; large output → file + `head`. **Do NOT bash to read files.**

---

## Task 1 — pedal detection's home (a reader over the carry, not a mutator)
Design, grounded at the current pedal code + the decoder carry:
- **Placement (#7):** pedal detection is a distinct chord-identity concern — place it as a **reader over the
  carry that produces a distinct pedal-annotated result**, NOT a step that mutates `results.front()` in place.
  State the layer it belongs to and how it consumes the decoder's carry.
- **Decouple the three symptoms:** the clobber (`= pass2`), the re-implemented diff-root scan, and the
  defensive append-disable all dissolve when pedal reads the carry rather than owning/mutating it — show how.
- **The diff-root need** is served by the carry's distinct-root alternatives (Part 1) — note the tie to FQ-1's
  primitive / the E4 carry (do not re-implement a fourth scan).
- Structure only.

## Task 2 — F-B annotate mechanics (reuse the existing open-mark, #6)
Design the demotion of the net-harmful fine-grain override to an honest annotation:
- **The vehicle (#6 — the load-bearing decision):** reconcile §4.2's "new advisory field" with the existing
  open-mark machinery — **reuse the existing open-mark carry** (the §15-13 / §8 case-3 / `FunctionLayerOutput.openMark`)
  rather than a parallel channel, unless grounded reason shows the existing mark is semantically wrong for a
  fine-grain contradiction (in which case a *unified* advisory, not a duplicate). Decide at the code.
- **What it carries (#12):** the contradiction signal as **calibrated uncertainty** — the information the
  override used to discard is preserved as a mark, not dropped (the 1043 signals become uncertainty).
- **The trigger:** the F-B fine-grain contradiction becomes an *annotation* trigger, never an override lever
  (the settled finding + Part-1's demotion of progression to a non-override tie-break). Ground at the contract
  §4 Frame F-B.
- Structure only; constants precision-phase.

## Task 3 — boundaries, owed build, owed measurements
- **Layer boundaries (#7):** where pedal (chord-identity reader) and the F-B annotation each live; acyclicity
  kept; no new cross-layer reach-in.
- **Owed build (enumerated, not built):** the pedal reader-over-carry; the F-B annotation wiring (open-mark
  reuse) — by layer, E4/L5-engage-adjacent, held until ratified.
- **Owed measurements (#5):** flag anything the design would otherwise assume (e.g. the pedal reader's
  agreement with the current in-place detection) as an owed measurement, not an assumption.

## Task 4 — Stage-2 closure statement
With these settled, state that the **Layer-5 engagement design phase (Stage 2) is COMPLETE** — carry +
selection (Part 1), the joint step (arc #10), pedal home + F-B annotate (this) all designed, structure-only.
Enumerate what Stage 3 (algorithmic completion / E4) inherits to BUILD: the joint step B1–B4 + its owed
measurements, the anchor (decoder carry replaces `results`), the owed migrations, quality-from-key's owner
(FQ-2, with the §6-block dissolution), the distinct-root-preserving carry (the Part-1 decoder gap), the pedal
reader, the F-B annotation.

## Task 5 — doc + fold + push
1. **Design** (extend `cowork_layer5_engagement_design.md` or a new doc — state which, #6): Tasks 1–4.
2. **Report** `cc_engage_l5_pedal_annotate_design_report.md` (force-add): what's settled, grounding, the
   Stage-2-complete statement + the Stage-3 build inventory, all SHAs.
3. **Sandwich (trivial — read-only):** no `src/`; both stops untouched; suites unchanged (no build).
4. **Fold** (`docs(cowork):`): the design + report · `STATUS.md` · `COWORK_HANDOFF.md` ·
   `cowork_stage5_fitter_design.md` (engage observation) · `cowork_engage_arc_plan.md` (mark Stage-2 design
   complete) · this instruction (force-add).
5. **Push fork-only** — never toward `upstream`/`musescore/MuseScore` (`cfc7eb5e39` HARD STOP).

## STOP conditions
- Any `src/` change, build, corpus write, or fit/tune (STRUCTURE only — R5; #8).
- A **new parallel annotation channel** for F-B instead of reusing/unifying the existing open-mark (#6) — flag
  and justify at code if a distinct mark is truly needed.
- A pedal design that keeps mutating the winner in place (it must be a reader-over-carry).
- Any claim not grounded at code/contract (#1) — flag UNCLEAR / owed-measurement.
- Any push toward `upstream`/`musescore/MuseScore`.

## Acceptance
Pedal placed as a reader-over-carry (the three symptoms dissolved), grounded ✓ · F-B annotate vehicle decided
(open-mark reuse/unify, not a parallel channel) with the contradiction carried as calibrated uncertainty (#12)
✓ · boundaries + owed build + owed measurements ✓ · the **Stage-2-complete** statement + the Stage-3 build
inventory ✓ · design + report + fold with SHAs ✓ · no src/build/corpus/fit; both stops green; pushed
fork-only ✓.

*Cowork, 2026-07-07. Engage arc #11 — the last Layer-5 design pieces; closes Stage 2. On CC's report: Cowork
verifies at objects → the design phase is complete and Stage 3 (algorithmic completion) is the user's to
open.*

---

## CC EXECUTION RECORD (session 34, 2026-07-07)

Executed read-only / structure-only. Deliverable: **Part 2 appended to `cowork_layer5_engagement_design.md`
(§6–§10)** — the #6-clean choice (Part 1 enumerated these two as its own §4.3 follow-ons; one home per concern).
Report `cc_engage_l5_pedal_annotate_design_report.md` (force-add).

- **Task 1 — pedal = a reader over the carry.** Grounded at `chordpostpasses.cpp:209-281` + audit §1.1 #7/§1.3/§1.4
  + the confirmed decoder gap (grep `chordslicedecoder.cpp` pedal → **0 matches**). The three symptoms dissolve:
  clobber → annotate a carried candidate (#12); re-scan → read the carry's distinct-root margin / FQ-1 (no 4th
  scan, tied `chordslicedecoder.cpp:927-930`); defensive-disable → the governed carry has no cap→append to
  contaminate. [owed-P1] carried-alt vs bass-stripped re-decode agreement flagged.
- **Task 2 — F-B annotate vehicle = the UNIFIED open-mark.** Decided at the code: overloading the plain boolean
  `openMark` is semantically wrong (undecidable ≠ confident-commit-plus-contradiction; collides with case-3); a
  parallel `functionContextContradiction` bool duplicates the channel (#6); so **unify** into one open-mark with a
  reason/kind (`Undecided` vs `FunctionContextContradiction`). Reading stays the L4 commit; the `(C,S)` contradiction
  carried as Class-M calibrated uncertainty (#12); trigger is annotation, never override; Frame F-B re-declared in
  contract §4.
- **Task 3 — boundaries/owed build/owed measurements** delivered (design §8): acyclicity strengthened (F-B's
  cross-layer recompute removed); owed build enumerated; [owed-P1/P2/FB1] flagged.
- **Task 4 — ★ STAGE 2 COMPLETE** (design §9): carry+selection (arc #9) + joint step (arc #10) + pedal/F-B (arc #11)
  all designed; Stage-3 build inventory enumerated (§9.2).

Fold: Part-2 design + report + STATUS (session 34) + COWORK_HANDOFF (arc #11 header) + `cowork_stage5_fitter_design.md`
(O-27) + `cowork_engage_arc_plan.md` (Stage-2 marked COMPLETE) + this instruction. Both stops green by construction
(no `src/`, no build, byte-identical to HEAD `2c550ec327`); suites unchanged; corpus frozen `c50002fee1`; pushed
fork-only (`cfc7eb5e39` upstream HARD STOP honored). No STOP condition tripped.
