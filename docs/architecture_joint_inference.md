# Architecture — Constrained Joint Inference (the back-half target)

> **ARCHITECTURE DIRECTION — INVESTIGATION-CONFIRMED (2026-06-15), ratifiable; not yet built.** Co-developed
> with the user 2026-06-15, derived from first principles AND pinned to the measured key-axis arc (Stages
> 4a–4d) + the META-PRINCIPLE. **The §9 sizing investigation LANDED and CONFIRMS the shape**
> (`cc_joint_architecture_dossier.md`, Cowork-verified read-only; instrument confirmed — the probe
> reproduces the corrected functional-residual `root_err=2365` to the unit):
> - **The shape is sound AND should be SCOPED, not a full lattice.** Joint chord×key residual: **41.0%
>   fully pinned, 19.2% chord-only ambiguous, 26.3% key-only, 13.5% JOINTLY-COUPLED**. The genuinely-coupled
>   core is ~1 in 7 → a **scoped-joint / two-pass** suffices; a full lattice is not warranted. (Cross-checks:
>   the key-modulation column 39.8% ≈ the modulation detector's DCML prevalence 39.9%; the vertical-oracle
>   cross-check concurs — pinned→single-root 79.2%, ambiguous→multi-root 68–90%.)
> - **The hard-constraint SAFETY gate PASSES.** The complete-clear-(vertical)-chord pin is ~0% vertical
>   error (of its 19.2% DCML-disagreement, 76.3% is segmentation/alignment + 23.7% functional re-rooting —
>   neither a wrong vertical chord). The "−7-wall-in-reverse" failure is structurally avoidable.
> - **The reading-shaped producers are correctly SOFT** — measured to pin WRONG: cadence anchor 44%,
>   modulation detector 53%, bass-is-root 17–23%. They must be soft scores, never hard constraints.
> - **A confirmed, B not triggered by the structure.** ~68% of chord-ambiguity is already soft-resolved;
>   the only feature-shaped slice a learned emission would help is the small pc-irreducible symmetric
>   dim7/aug (~111). Floor = convention boundaries (tonicization↔modulation ~409, notated-vs-analyst ~127).
> **Recommendation (CC + Cowork): build the SCOPED constrained-joint decision, hand-built soft emission,
> KEY-AXIS FIRST; keep cadence/modulation/bass-is-root SOFT; reserve a learned emission for the small dim7/
> voice-leading floor.** Scope: WiR-Bach measured; non-Bach unmeasured (stated). **Awaiting user ratification
> of the shape → then the scoped-joint design.**

---

## §1 — The model: one joint decision over all evidence

Harmonic analysis is **not** a feed-forward pipeline (chords → key → function). The correct reading of a
passage is the single **globally-coherent** interpretation that best explains **all** the evidence at once
— sonorities, cadences, scale content, voice-leading, metric placement, repetition, the key signature.
Chord and key/mode are **co-determined**; function is downstream of both.

**This is the lesson of the entire key-axis arc (4a–4d), measured, not assumed:** every attempt to infer
mode/key with a *local* mechanism hit a ceiling — the relative-pair floor (local note salience can't
separate relatives), the modulation gap (a local cadence gate can't see whole-piece consistency). The
local feed-forward structure *structurally cannot* bring all the evidence to bear on one decision. That is
the architectural diagnosis.

## §2 — The structure: CONSTRAINED joint inference (hard constraints + soft scores)

"All evidence at once" is **not** a flat weighted sum. Evidence comes in two kinds:

- **Hard constraints** — decisive evidence that **disqualifies** alternatives outright or **pins** a
  solution: "this IS C major, whatever the soft hints say." These are the **raw facts** (which pitches
  sound, when, with what duration / metric weight / bass) plus the genuinely-unambiguous analyses (a
  complete clear triad on a strong beat). They **prune** the hypothesis space. **⚠ Note (J-key-i,
  2026-06-15): the notated key signature is NOT among the hard facts** — its fifths were measured to pin
  wrong ~17% (modal/partial signatures), so the home key is soft / note-based, not signature-pinned. The
  safety gate doing its job: a candidate hard constraint that pins wrong is demoted to soft (§5).
- **Soft scores** — priors, weak cadential cues, stylistic tendencies, the global key path. These only
  **rank** the hypotheses that survive the hard constraints.

The decision optimizes the soft scores **subject to** the hard constraints — a constrained optimization,
not a vote.

## §3 — Why this is safe, efficient, and explainable

- **Safe:** a hard fact is a constraint, not a score, so **no amount of soft global evidence can override
  it.** This makes the −7-wall failure class — a confident-but-wrong global hypothesis overriding clear
  local evidence, which we spent Stages 4a–4d removing — **structurally impossible**, not merely "hopefully
  calibrated away."
- **Efficient + scoped:** hard constraints **pin the easy majority**; the joint/soft reasoning does its real
  work only on the **ambiguous survivors**. The hard problem is exactly *the positions where the hard
  constraints leave more than one live hypothesis* — a concrete, measurable residual (§9).
- **Explainable:** the hard part is "the notes say so"; the soft part is the judgment call. The system can
  say which is which.

## §4 — The META-PRINCIPLE, refined and reconciled

We proved twice that wider **search** over a *fixed, narrow* emission has ≈0 headroom (beam-widening
Δ=+7a; the HMM key path on the relative-pair S2) — and shelved search on that basis. The joint decision is
**not in tension** with that, because its value is **not search**: it is that the decision is made on
**broad** evidence (cadence *and* scale *and* transition *and* voice-leading, integrated), so no single
noisy source dominates. That is a **broader emission**, coherently integrated. Precision still lives in the
**evidence** — its breadth, its quality, and its calibration — exactly as the META-PRINCIPLE says. The
joint structure is the *vehicle* that lets all the evidence be seen at once; it does not replace evidence
quality.

## §5 — The calibration precondition (the load-bearing skill)

Getting "hard" right is the whole game. **A sounding note is not automatically a chord tone** — a C-E-G
with an F may be an added-fourth chord or an F suspension to be explained away. So the truly hard
constraints are the **raw facts** + the genuinely-unambiguous analyses; chord-tone-vs-non-chord-tone is
itself part of the soft/joint analysis operating *within* those facts. **Over-claiming "hard" on a soft
case re-creates the override problem in reverse** — a wrong constraint pinning a wrong answer. Calibrating
*what counts as decisive* is the precondition, realizable hand-built (explicit hard/soft factors) or
learned (a model sharp where sure, soft where not).

## §6 — The irreducible ceiling

Some cases are genuinely underdetermined by the score: the same notes admit two valid readings and the
analyst picks by convention, style, or context beyond the notes. No "all evidence at once" reaches those —
they are the honest floor (where even analysts disagree). The architecture's ceiling is "the best
score-derivable reading."

## §7 — Where A-vs-B (hand-built vs learned) lives

The **structure** is decided: constrained joint inference. **A-vs-B lives entirely in the EMISSION** — the
soft scoring and the constraint definitions. Hand-built features now (explainable, no training data); a
learned emission later (higher ceiling, decoded by the *same* constrained-joint machinery — part-1 rec.5).
The architecture is agnostic to that choice and accommodates both; the §9 residual sizing tells us where a
learned emission would actually buy something (the soft-ambiguous + floor slice) versus where hand-built
constraints already suffice (the pinned majority).

## §8 — Relation to what is already built (this is an integration, not a teardown)

- The **chord decoder** (Stage 3, beam-1) is the seed of the joint lattice.
- The **vertical oracle**, the committed **cadence instrument**, the **local-modulation detector**, the
  **tonicization labeler** are all **evidence producers** — each emits hypotheses + scores already.
- Constrained joint inference **integrates** them into one decision instead of chaining them through a
  brittle pipeline. The current local resolver, hysteresis, and the post-hoc gate layer are what it
  *replaces*.

## §9 — What must be MEASURED before building (the investigation)

Per never-guess, the magnitude and shape are sized by measurement, not assumed:
1. **Hard/soft characterization** — which evidence sources are genuinely decisive (hard) vs soft.
2. **The residual** — apply the candidate hard constraints over the corpus and measure how many positions
   are **pinned to a unique chord+key** vs remain **ambiguous**. The ambiguous count = the true scope of
   the joint problem (and decides full-joint vs scoped-joint vs two-pass).
3. **Hard-constraint safety / calibration** — do any candidate hard constraints ever pin a *wrong* answer
   (per DCML)? A hard constraint that pins wrong is a bug; measure the rate.
4. **Soft-resolvable vs floor** — of the ambiguous residual, how much does soft/global evidence resolve,
   and how much is irreducible (the §6 ceiling) — i.e. where a learned emission (B) would actually pay.

Output: the numbers that right-size the architecture + confirm the constrained-joint shape is sound, before
any build.

## §10 — Provenance
Co-developed with the user 2026-06-15 across a multi-turn architecture dialogue, grounded in the measured
key-axis arc (4a–4d), the metric-check reframe (S1 = local-modulation, a Stage-4 gap), and the
cadence-precision ceiling (the local key-agnostic approach is precision-limited). It is the concrete,
first-principles form of the part-1 review's "global/joint decoder" vision. **Investigation-gated; not yet
ratified-and-built.**
