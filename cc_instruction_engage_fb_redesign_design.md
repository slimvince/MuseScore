# CC Instruction — Engage arc #1: the F-B fine-grain override REDESIGN — design/scoping pass (read-only) + push the ratified backlog

> **ACTIVE DISPATCH (Cowork, 2026-07-06).** First increment of the engage arc (Stage-5 is CLOSED; O-16).
> The user selected this opener by criteria, not by name: **maximize achievable inference precision, build
> on KNOWLEDGE not assumptions, build on THEORY, and minimize surprises.** F-B is the joint maximum — its
> harm is *measured* (Phase 3: 1043 fires / 53 corrections / 809 harms), its frame is *declared theory*
> (confidence contract §4 Frame F-B), and it is *bounded* to one L5 §5.5-case-4 override.
>
> **This is a REDESIGN DESIGN pass — read-only. NO `src/` change, NO scoring value, NO corpus write, NO
> build.** It is architectural design (moratorium-clear), NOT inference-fixing and **explicitly NOT a θ
> retune** — Phase 3 already proved the best measurable θ effectively DISABLES F-B, so θ-tuning is a dead
> end and is out of scope. The deliverable is a design doc + a decision surface; the implementation is a
> later, separately-ratified build event.
>
> **The user's binding constraint for THIS dispatch:** every claim about the mechanism must be grounded at
> the code or the measured data. If a step would rest on an assumption about F-B's behavior that is not
> verified at the source or the ledgers, STOP and flag it — do not build the design on it.
>
> **Read first (the knowledge base — do NOT summarize from memory):**
> - `cowork_confidence_contract.md` §4 **Frame F-B** (incumbent = L4 composite confidence of a `Commit`,
>   **vertical-fit-only**, θ accounts for the missing progression term per L5 §15-2; contradiction = the
>   contradicting context's functional-plausibility = licensed-progression fit + cadential fit; selection
>   restricted to carried alternatives / neighbouring committed harmony, never re-derivation) + §5 R4/R5/R6.
> - `cc_stage5_phase3_report.md` **Task C** (the 1043/53/809 measurement; the F-A/F-B contradiction scales
>   `x/(x+3.5)`, `x/(x+2.0)`; the "best θ disables F-B" finding) + the committed θ ledgers under
>   `tools/fit_ledgers/`.
> - `docs/scoring_model.md` (the L4 composite confidence F-B reads — the vertical-fit term) and the L5
>   §5.5-case-4 override site in `src/composing/` (characterize AT THE CODE: the function, its inputs, the
>   actual decision rule — read only).
>
> **Current state:** HEAD `923f149561`, branch `master`, fork-only (`origin` = `slimvince/MuseScore`),
> **76 commits ahead of origin, unpushed**. Both stops green (batch 52/24/52; robust sandwich identity-PASS).
>
> **VS Code bash rules:** append `; echo "exit:$?"`; large output → file + `head`. **Do NOT bash to read
> files** — use the file tools.

---

## Task 0 — push the ratified backlog to the fork (the user's push instruction)
The 76 ahead are all ratified/clean (through R10-b). Push them to the fork:
```
git push origin master; echo "exit:$?"
```
- **HARD STOP — fork-only.** `origin` = `slimvince/MuseScore` only. **NEVER** push, PR, or merge toward
  `upstream` / `musescore/MuseScore` (the `cfc7eb5e39` MusicXML-mode patch is fork-local-only per the
  CLAUDE.md distribution constraint; any push that would carry it upstream is a HARD STOP — surface, do not
  proceed). `upstream` push is disabled; keep it so.
- Report the push result (new `origin/master` SHA, ahead-count → 0 before this dispatch's own commits).

## Task 1 — characterize F-B at the source (build on knowledge, not assumptions)
From the read-first set, produce a precise, code-grounded description of the F-B mechanism as it runs today:
the exact L5 §5.5-case-4 override site, the L4 vertical-fit-only composite it reads as incumbent, the
functional-plausibility contradiction it compares against, the θ-comparison, and the carried-alternative
selection. State every input by its source symbol. Flag any gap between the contract's declared frame and
the code as-built (a contract/code drift is a finding).

## Task 2 — diagnose the net-harm STRUCTURALLY (build on theory)
Using the **measured** Phase-3 fire population (the θ ledgers / the dump data — read-only, no new corpus
regen), decompose the **1043 fires = 53 corrections + 809 harms + ~181 neutral**:
- **Test the documented root-cause hypothesis:** F-B's incumbent is *vertical-fit-only* while its
  contradiction is *progression-aware* (licensed-progression + cadential fit) — i.e. the comparison is
  structurally asymmetric, and L5 §15-2's "θ accounts for the missing progression term" may be the flawed
  premise (Phase 3: no θ reconciles it). Is the harm concentrated where the L4-committed root is vertically
  strong but the progression-aware contradiction wins anyway?
- **Find the discriminator:** is there a structural feature separating the 809 harms from the 53
  corrections (chord type, cadential context, whether the carried alternative is a share-tone rotation,
  key-boundary proximity)? Report the taxonomy with counts from the measured fires — projected from data,
  never assumed.

## Task 3 — redesign OPTIONS at the proper layer (minimize surprises)
Propose redesign options, each as a *design proposal* (not built), at the correct layer (L5 §5.5 / the L4
composite it consumes / the contract frame). For EACH option state: the layer + frame change; the theory
basis (which contract rule / §15-2 premise it repairs); the **projected** effect on the 1043/53/809 split
from the Task-2 taxonomy (with the projection's evidentiary basis); the behavior/byte-identity blast radius;
and the surprise/risk profile. Include at minimum:
- **(baseline) Disable F-B** — the reference option, since the best θ already ≈ disables it. Quantify the
  exact recovery (removing 809 harms at the cost of 53 corrections) as the floor any redesign must beat.
- **(gate)** a tighter *structural* fire condition excluding the harm sub-population identified in Task 2.
- **(incumbent repair)** give the L4 incumbent its missing progression term so the θ-comparison is fair
  (repairing the L5 §15-2 premise) — the theory-first option.
- **(re-frame)** any other option the diagnosis warrants.

## Task 4 — recommendation + the build-event decision surface
CC's evidence-based recommendation (the redesign choice + the implementation are the user's next ratified
event). State what the implementing dispatch would touch (the proper `src/composing/` layer + the mandatory
`docs/scoring_model.md` sync + the confidence-contract frame update), and what the acceptance gate is (the
robust-unit stop: class-(b) root-disagree DURATION non-increase per preset — a redesign that recovers F-B's
harms should MOVE it favorably, measured via the successor sandwich). **No src change here.**

## Task 5 — doc + fold + push
1. **Design doc** `cowork_fb_redesign_design.md` (force-add): Tasks 1–4 — the code-grounded mechanism, the
   net-harm taxonomy, the options with projected splits, the recommendation, the build-event surface.
2. **Report** `cc_engage_fb_redesign_design_report.md` (force-add): what landed, the grounding sources, any
   contract/code drift found, all SHAs.
3. **Sandwich (trivial — read-only):** confirm no `src/`/`tools/corpus/` change; both stops untouched
   (batch 52/24/52; robust sandwich still identity-PASS); suites unchanged (no build).
4. **Fold** (`docs(cowork):`): `STATUS.md` · `COWORK_HANDOFF.md` (engage-arc START-HERE; F-B design pass
   delivered) · `cowork_stage5_fitter_design.md` (engage-arc observation) · this instruction (force-add).
5. **Push the new commits** to the fork (`git push origin master`) — same fork-only HARD STOP as Task 0.

## STOP conditions
- Any `src/` change, any corpus write, any build, any θ retune (out of scope — a moratorium-blocked
  inference-fix; this dispatch is design only).
- Any push, PR, or merge toward `upstream`/`musescore/MuseScore` (the `cfc7eb5e39` distribution HARD STOP).
- Any design step that would rest on an unverified assumption about F-B's behavior — STOP and flag
  (the user's binding "knowledge not assumptions" constraint).
- The robust sandwich not identity-PASS or batch ≠ 52/24/52 at close (nothing here should touch them).

## Acceptance
Backlog pushed to origin (fork-only, upstream untouched) ✓ · F-B characterized at the source with any
contract/code drift flagged ✓ · the 1043/53/809 population decomposed into a measured taxonomy with a
harm-vs-correction discriminator ✓ · redesign options (disable-baseline + gate + incumbent-repair + any
warranted) each with layer/theory/projected-split/blast-radius/risk ✓ · recommendation + build-event
decision surface ✓ · design doc + report + fold, all SHAs ✓ · no src/corpus/build/θ-retune; both stops
green ✓ · new commits pushed fork-only ✓.

*Cowork, 2026-07-06. Engage arc #1. Read-only architectural design (moratorium-clear); the F-B redesign
implementation is the user's next ratification event. On CC's report: Cowork verifies at objects → presents
the redesign-option decision surface to the user.*
