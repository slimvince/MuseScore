# CC report — Engage arc #11: Layer-5 design, pedal home + F-B annotate (closes Stage 2)

> **Read-only architectural design. No `src/` change, no build, no corpus write, no constant fitted/tuned
> (STRUCTURE only — R5; #8).** HEAD `2c550ec327`, branch `master`, fork-only, ahead 0. Both regression stops
> untouched/green by construction (no `src/`, no build). Deliverable: **Part 2 appended to
> `cowork_layer5_engagement_design.md`** (§6–§10) — the doc-home decision below.

## What was settled

**Task 1 — pedal detection's home = a reader over the carry (not a mutator).** Grounded at
`chordpostpasses.cpp:209-281` `[code]` + the audit's pedal finding (`cowork_structural_integrity_audit.md`
§1.1 #7 / §1.3 / §1.4 `[audit]`) + the confirmed decoder gap (grep `chordslicedecoder.cpp` pedal → **0 matches**
`[code]`). Placed as a **reader over the decoder's governed Layer-4 carry** that emits a distinct pedal-annotated
result, never a `results.front()` mutation (design §6.3). The audit's three coupled symptoms all **dissolve** under
reader-over-carry (design §6.4):
- **clobber** (`results = pass2`, `:274`) → the reader annotates a carried candidate; the winner+carry vector and
  the full-voice reading survive (#12);
- **re-implemented diff-root scan** (`:262-269`, the 4th copy) → the confirmation margin is **read** from the carry's
  distinct-root ranking / the FQ-1 primitive over the carry — **no 4th scan** (§6.5, tied to `chordslicedecoder.cpp:927-930`);
- **defensive append-disable** (`:240-245`) → the cap→append it defended against is a legacy-`results` property; the
  decoder's **governed** carry has no display-carry append to contaminate — nothing to disable.

The material pedal needs (the upper-voice harmony + a confidence gap) is *usually* already in the carry as a
distinct-root alternative excluding the bass (design §6.2), **subject to owed measurement [owed-P1]** (does the
carried alternative agree with the bass-stripped re-decode). Structure only.

**Task 2 — F-B annotate vehicle = the UNIFIED open-mark (reuse, not a parallel channel).** The load-bearing #6
decision, decided at the code. Reconciled `cowork_fb_redesign_design.md` §4.2's proposed "new
`functionContextContradiction` field" against the existing open-mark machinery
(`ResolvedReading.openMark` `functionresolver.h:170` → `FunctionUnitAssembly`/`FunctionAnalysisUnit.openMark`
`functionoutput.h:165/124`; the §8 case-3 honest-carry `cowork_layer5_function_design.md:582`; the §15-13
both-licensed terminus) `[code]`:
- **Overloading the plain boolean `openMark` is semantically WRONG** — it means "genuinely undecidable / no
  answer," but F-B's L4 committed confidently and the reading is carried unchanged; setting it loses information
  (#12) and collides with the case-3 abstain meaning.
- **A parallel `functionContextContradiction` bool is a duplicate channel (#6 violation).**
- **Decided: UNIFY into one structured open-mark carrying a reason/kind** — `Undecided` (case-3 / §15-13, today's
  semantics preserved) vs `FunctionContextContradiction` (F-B; reading stays the L4 commit, `overrodeCommit` stays
  false — the additive-not-replace contract already on `ResolvedReading`). This reuses the existing carry path and
  dissolves §4.2's "new field" into "the existing open-mark, enriched" — the instruction's licensed "unified
  advisory, not a duplicate" (design §7.2).

The contradiction is carried as **calibrated uncertainty** (#12): the L4 reading survives (the +756 recovery) AND
the frame's `(C, S)` quantities become the open-mark payload (Class-M, squash-constant precision-phase R5) — the
1043 signals preserved for a future C3 joint step (design §7.3). The trigger is an **annotation lever, never an
override** — no `overrodeCommit`, no `prog[i].chord` mutation, no `forwardRecompute`; Frame F-B re-declared in
contract §4 as an annotation channel (design §7.4, grounded `[contract §4]`).

**Task 3 — boundaries / owed build / owed measurements** (design §8). Pedal = carry-side reader (Layer-4 output),
forward-only, no winner mutation, no reach-in; F-B annotation = Layer 5, additive, **acyclicity strengthened** (the
one former cross-layer recompute removed). Owed build (enumerated, not built): the pedal reader-over-carry; the F-B
annotation wiring (open-mark enrich + `attemptFineGrainOverride` demotion + `ResolutionBasis` re-value + contract §4
re-declaration + L5/`docs/scoring_model.md` sync). Owed measurements (#5, flagged not assumed): [owed-P1] pedal
reader vs in-place detection agreement; [owed-P2] carried-margin vs `pass2` sigmoid; [owed-FB1] F-B byte-identical
today, must move the class-(b) DURATION favorably at engage.

**Task 4 — Stage-2 CLOSURE + Stage-3 build inventory** (design §9). **The Layer-5 engagement design phase (Stage 2)
is COMPLETE**: carry+selection (arc #9, Part 1), the joint step (arc #10), pedal home + F-B annotate (arc #11, Part
2) — all designed, structure-only, moratorium held. Stage 3 (E4) inherits to BUILD: the anchor (decoder carry
replaces `results`, FQ-4); the distinct-root-preserving carry (Part 1 §2.3, the E4 prerequisite); the pedal reader;
the F-B annotation; quality-from-key's owner (FQ-2 + §6-block dissolution); the joint step B1–B4 + its owed
measurements (`cowork_joint_key_chord_design.md` §4/§5); the owed migrations (FQ-8: two-segmenters, two-pitch-context,
tpc-fold, `function/` rename; FQ-1; FQ-3); the F-1/S19/D-FS confidence-scale fix (Stage-5-adjacent — the annotate
re-frame removes F-B's override arithmetic from the critical path).

## The doc-home decision (#6)
**Part 2 appended to `cowork_layer5_engagement_design.md`, not a new doc.** Part 1 explicitly enumerated these two
pieces as its own §4.3 follow-ons — they are the *same* Layer-5-engagement concern. One home per concern; a new file
would split it. Global section numbering: Part 1 = §1–§5, Part 2 = §6–§10.

## Grounding (every claim tagged)
- `[code]` — `chordpostpasses.cpp:209-281` (pedal tail); `chordslicedecoder.cpp` pedal grep = 0;
  `chordslicedecoder.cpp:746-789` (governed carry), `:927-930` (diff-root read from carry);
  `functionresolver.h:151-198` (`ResolutionBasis`, `ResolvedReading`, `openMark`, `bothLicensed`);
  `functionoutput.h:124/165` (`openMark` on assembly/output); `functionresolver.cpp:381-498` (`attemptFineGrainOverride`).
- `[audit]` — `cowork_structural_integrity_audit.md` §1.1 #7, §1.2, §1.3, §1.4, FQ-1, FQ-4.
- `[fb]` — `cowork_fb_redesign_design.md` §2 (net-harm), §3.A/§3.D-1, §4.1/§4.2/§4.3/§4.4.
- `[contract]` — `cowork_confidence_contract.md` §4 (Frame F-B, re-declaration mandate), §5 R5.
- `[joint]` — `cowork_joint_key_chord_design.md` §4 (B1–B4), §5 (owed measurements).
- Case-3 honest-carry / four-case model — `cowork_layer5_function_design.md:574-588`.
- Arc plan / Stage boundaries — `cowork_engage_arc_plan.md`.

## STOP conditions — none tripped
No `src/` change, build, corpus write, or fit/tune. No parallel F-B channel (the open-mark is unified, not
duplicated). No pedal design that mutates the winner (reader-over-carry). No push toward `upstream`. Every
un-held fact flagged as an owed measurement (#5), not assumed. No inference fix designed (#8, #13).

## SHAs
- HEAD at design: `2c550ec327`.
- This fold (to be stamped at commit): the Part-2 design + this report + STATUS.md + COWORK_HANDOFF.md +
  `cowork_stage5_fitter_design.md` (engage observation) + `cowork_engage_arc_plan.md` (Stage-2 complete) + the
  instruction (force-add).

*CC, 2026-07-07. Engage arc #11 — read-only, structure-only; closes Stage 2. Cowork verifies at objects → the
design phase is complete and Stage 3 (algorithmic completion) is the user's to open.*
