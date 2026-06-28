# Phrase-boundary primitive — methods catalog (research-first, pre-revision)

> **Status: research synthesis (2026-06-26).** Primary-sourced survey of surface/notation-level phrase-segmentation, to
> enrich the phrase-boundary primitive beyond the minimal four signals of the first draft. Grounds the revised design.
> The hard constraint throughout: the primitive is **harmony-agnostic** (the cadence layer consumes it, so it may not read
> key/chord/cadence — surface cues only).
>
> **★ Proportionality (user-ratified 2026-06-26).** Contrapunctus — the SOTA-competitive reference engine (52% genre-
> balanced / 68% chorale RN) — does **no explicit phrase segmentation and no cadence detection at all** (verified at its
> repo; see `contrapunctus_findings.md` addendum); it captures phrase structure *implicitly* via long, stable, rule-based
> key runs. So this primitive is **not** an RN-accuracy requirement — it is a *deliberate bet* for our explainable,
> decomposed phrase → cadence → key/function path (and the tonicization-vs-modulation distinction). **Keep it proportionate:
> build the graded model right, but do not let it balloon; it is load-bearing for our cadence mechanism, not for accuracy
> per se, and there is a proven implicit fallback (stable key runs) if the explicit path proves hard.**

## 0. The finding that reshapes the primitive
The first draft modelled a boundary as a **union of a few binary signals** (fermata OR all-voice rest OR barline). The
literature is clear that this is a **degenerate, inferior special case.** Every leading harmony-free model computes a
**continuous boundary *strength*** from several cues and **picks peaks** — because what marks a boundary is not "a gap
exists" but "a gap *larger than its neighbours*," which only a graded, locally-normalised profile captures. The naive
OR-union inflates recall and destroys precision (the limit — "every event is a boundary" — scores precision 0.13).
Evidence (Pearce, Müllensiefen & Wiggins, ISMIR 2008, Essen corpus, 1705 melodies): the leading models **Grouper** (F1
0.66) and **LBDM** (F1 0.63) both compute graded strength + peaks; a logistic-regression **hybrid** of cues beat every
single cue (F1 0.66, precision 0.87) — weighted combination beats naive combination. ➡ **The primitive should emit a
graded boundary strength, not a binary set.** That also fits this project's confidence-weighted architecture: a graded
strength gives the cadence layer a *confidence* to consume, not just a bit.

## 1. The cue inventory (surface, harmony-agnostic) — by reliability
Each cue: what it reads, and its standing (precision/F1 from the ISMIR-2008 evaluation where measured).
- **Rest / gap (the strongest single cue).** A silence or large offset-to-onset interval between events. **Precision
  ≈ 0.99** — by far the most precise surface cue. (GTTM GPR2a.)
- **Large inter-onset-interval (IOI) gap.** An unusually long time between successive attacks. High value; the dominant
  term in both Grouper and LBDM. (GPR2b.)
- **Agogic / long-note lengthening.** A note long relative to its neighbours (phrase-final lengthening). Moderate–high,
  but only at large length contrasts (GPR3d alone: F1 0.31). (GPR3d.)
- **Registral leap / pitch-interval change.** A large melodic interval or register change between consecutive notes.
  Noisy alone (GPR3a: precision 0.29) but a valuable *contributor* inside a combined model. (GPR3a.)
- **Articulation change** (slur end, staccato↔legato) and **dynamics change** (abrupt level change). Real but weak/
  auxiliary; not quantified in the main evaluations. (GPR3b/3c.)
- **Parallelism / repetition.** A repeated motivic/rhythmic pattern induces boundaries at pattern starts. Theoretically
  powerful, practically the hardest to formalise (GTTM left GPR6 informal). (GPR6; Cambouropoulos 2006.)
- **Metric position + phrase-length prior.** Bias boundaries to recur at parallel metric positions, and phrases toward a
  typical length. A *global regulariser* on top of gap cues, not a standalone detector; the length value is
  corpus-specific (~10 notes for folk — would need recalibration for chorales). (Temperley Grouper PSPR2/PSPR3.)
- **Structural notation marks.** Fermata, **breath mark (comma) / caesura (grand-pause)**, double/final/repeat barline,
  rehearsal mark, time/tempo change. Direct composer-notated grouping signals — binary, very high precision in notated
  scores (not benchmarked by the melodic-segmentation literature, which uses barless folk encodings, but established as
  composer-intended grouping; Cambouropoulos 2001 flags composer slurs/breath marks as a distinct grouping channel).
- **(Optional) Information-content / surprisal (IDyOM).** Segment before notes whose *learned* continuation is highly
  improbable. Harmony-agnostic and as good as rule systems (F1 0.58), but needs a **trained statistical model** — an
  add-on, not a deterministic core.

**Excluded by the architecture (note only):** cadential closure, harmonic-rhythm change, key change, dominant→tonic — all
require the harmony the later layers compute. Cambouropoulos names the *absence of a harmonic component* as LBDM's chief
limitation, so a surface-only primitive will **systematically miss boundaries marked only harmonically** (a cadence with
no surface gap). That is acceptable and expected here — those are recovered downstream by the function layer — but it
means the primitive should not be expected to reach the accuracy of systems that exploit tonal structure.

## 2. The model — LBDM-style core + deterministic markers + peak-picking
The recommended structure for our primitive (the evidence-backed shape, with constants deferred to the precision phase):
- **A boundary-strength profile** built LBDM-style from three normalised change profiles — **gap (rest/OOI)**, **IOI**,
  and **pitch-interval** — each via the Change×Proximity formula (boundary strength rises with both the *degree of local
  change* and the *size* of the interval), normalised to [0,1], then a **weighted sum**. The **gap term dominates** (the
  data make rests the most precise cue); LBDM's 0.25/0.50/0.25 pitch/IOI/rest split, or a rest-heavier variant, is the
  starting point. *(The weights are precision-phase constants; the mechanism is fixed.)*
- **Deterministic high-confidence notated markers** (fermata, double/final/repeat barline, an explicit all-voice rest)
  fold in as **strong additive spikes** on the profile — nearly free, very high precision in notated scores.
- **Peak-picking**: a boundary is a **local peak above an adaptive threshold** (Pearce et al.'s "Simple Picker": a local
  maximum AND above a running mean + k·SD; k is a precision-phase constant).
- **(Deferred) global regularisers** (phrase-length prior, metric parallelism — Grouper-style, needing a dynamic-
  programming pass) and **(deferred) IDyOM surprisal** — both raise accuracy but add a corpus-specific constant / a
  trained model; not in the first build.
- **Output: the graded boundary-strength profile + the picked boundary ticks.** Downstream consumers (the cadence gate,
  salience) can read either the boolean boundary or the strength as a confidence.

## 3. Polyphony — the real caveat (engineering on top, validate on our corpus)
Nearly all of this work is **monophonic** (single-line folk melodies). Our scores are polyphonic. The transfer:
- **Reduce the texture first.** The gap cue family generalises cleanly: a phrase boundary in polyphony is a **near-
  simultaneous rest or long-note across all voices** — exactly the chorale convention (all voices reach a fermata note
  together). So the dominant cue transfers, and **homophonic/chorale textures are an unusually *easy* polyphonic case.**
- **The pitch-interval cue does not transfer cleanly** (whose leap?). Apply it to a **designated voice — the top voice**
  (the §-prerequisite top-voice primitive), or pool conservatively.
- **No validated deterministic rule set exists for polyphonic phrase boundaries** comparable to the monophonic canon.
  Treat polyphonic extension as engineering on the monophonic cues, **validated against our own chorale ground truth** —
  not as settled science.

## 4. What this changes in the design (for the revision)
- The §4 "union of four binary rules" becomes a **graded boundary-strength model**: the LBDM-style surface core (gap +
  IOI + pitch-interval, gap-dominant) + the deterministic notated markers as additive spikes + peak-picking.
- The primitive's **output gains a strength** (a confidence), not only a boolean — better for the downstream cadence gate.
- **Polyphony** is handled by **per-voice cues aggregated to the texture** (the "pool across voices" option, refined):
  each eligible voice gets its own gap/inter-onset/pitch-interval profiles, summed per (coincidence-window-merged) onset
  into a texture strength — yielding **both** per-voice and texture boundaries, and using **every** voice's pitch cue (not
  only the top voice). Validated against the chorale corpus. (The design ratified this over the simpler whole-texture
  reduction, user 2026-06-26.)
- The **deterministic-fact framing softens**: the notated markers stay deterministic, but the surface-cue strength is a
  computed profile with **precision-phase weights + a peak threshold** (mechanism fixed now, constants deferred — the
  firewall). This is the one real character change to weigh (§ decision below).
- **Deferred (named, not built):** the phrase-length / metric-parallelism global regularisers (corpus-specific) and the
  IDyOM surprisal add-on (needs training).

## Sources
Cambouropoulos 2001 (LBDM, OFAI TR / ICMC) — formula, weights, evaluation; Pearce, Müllensiefen & Wiggins, ISMIR 2008 /
Springer 2010 — the benchmark table, model definitions, the hybrid result; Lerdahl & Jackendoff 1983 (GTTM GPRs);
Temperley 2001 (Grouper / PSPRs); Frankland & Cohen, *Music Perception* 2004 (GPR quantification — rest/attack-point most
effective); Cambouropoulos 2006 (parallelism); Thom/Spevak/Höthker, ICMC 2002 (Grouper vs LBDM); the 2024 byte-pair-
encoding polyphonic-segmentation study (arXiv:2410.01448). Full URLs in the research report.
