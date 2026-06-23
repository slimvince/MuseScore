# Cowork — Architecture & Implementation-Plan RE-ASSESSMENT (2026-06-20)

> **Trigger.** Two inputs landed together: (1) CC's anchor-redesign dossier ABANDONED the union-recompute and
> found production's segmentation-based embellishment discrimination already correct; (2) the Contrapunctus
> study + its referenced papers (AugmentedNet, AnalysisGNN, the JNMR suspension paper, the open benchmark) gave
> us an external, SOTA-beating reference engine. They **converge**, and the convergence points somewhere
> different from the original phase-2 plan. This doc re-reads the architecture and re-orders the work.
>
> **Status of evidence:** CC's verdict source-verified by Cowork (`detectExtensions` context-blind
> `chordanalyzer.cpp:217`; `pcWeight` duration-weighted `:981`). Contrapunctus claims are theirs, but
> reproducible + independently echo our own measurements (`contrapunctus_findings.md`). This is a planning
> re-assessment for ratification, not an implementation.

---

## 1. The convergent picture — both our engine and the external SOTA agree on the SAME architecture

Independently, our phase-1/2 measurements and a benchmarked engine that **beats AugmentedNet out-of-sample**
arrive at the identical shape:

**Rule-based KEY detection (cadence/structure-anchored, NOT learned) → rule-based CHORD-candidate generation →
a small learned chord-LABEL re-ranker → embellishments handled CHORD-FIRST (segmentation + NCT, not richer
vocabulary).** Our engine already *is* most of this. The agreements, point by point:

| Question | Our measurement (CC) | Contrapunctus / papers | Verdict |
|---|---|---|---|
| Learn the key? | K3: joint key **search inert** (−0.04/−0.14/−0.06pp); lever is soft evidence + structure | **Learned key detector loses in all 9 genres**; worst chord-ID (43.20); rule-based Heuristic best (75.26 key / 51.69 chord) | **Never learn keys.** Rule-based, structure-first. |
| Key-axis lever? | K1: cadence precision (kill spurious I→IV/V/V→V); keychain structure | "keychain *structure* (long phrase-aligned runs) matters more than per-beat"; spurious short segments cost chord beats | **Clean keychain via cadence precision = the lever.** |
| Selection / re-ranking? | Competition owns ~24%; **pure-rerank ~1.7%**; cases "need a candidate never surfaced" | **"Selection layer saturated"** — Viterbi/bass-refiguring/window-support all rejected; residual is candidate/emission or key | **Don't invest in selection heuristics.** |
| Embellishment over-read? | Anchor union-recompute **abandoned**; segmentation + inherit-clean-slice is the discrimination layer | JNMR: **don't re-analyze for richer chords**; keep basic chord, post-process NCTs (per-note membership prob) | **Chord-first, not union re-derive.** Production is right. |
| The one place learning helps? | (not yet tried) | **Learned chord-LABEL re-ranker = +7pp** (small LR over tonic-rotated windowed PC features) | **A genuine new lever we have not pursued.** |
| Metric? | **BIR is a misleading proxy** (scored 5 oracle regressions as "fixes") | Oracle exact-match + 6 defensible tiers; never a proxy gate | **Adopt an oracle/tier metric.** |

The strategic upshot: **we are not lost or far behind — our architecture is the right one, confirmed by an
engine that leads the published SOTA.** The question is purely *which lever next*, and the evidence now answers
it much more sharply than phase-2 did.

## 2. What changes in our architecture understanding

- **The CHORD axis is much healthier than phase-2 implied — it is near its rule-based ceiling.** The "biggest
  structural lever" (the anchor / 37.7% held-harmony bucket) was a **misdiagnosis**: production's
  segmentation-based embellishment discrimination is correct (CC, source-verified), and the union-recompute is
  net oracle-*negative*. Competition/selection is **saturated** (us ~24%/1.7%; them, three mechanisms rejected).
  So further *rule-based* chord gains are small. The remaining chord headroom is: (a) accept the floors
  (~7% bass-sharing ambiguity — engine-independent per their tier data; symmetric-dim7 pc-undefined), or (b) a
  **learned chord-label re-ranker** (new direction, §3.4).
- **The KEY axis is unambiguously where the leverage is — and it is RULE work, not search or learning.** Both
  sides agree decisively. K1 (cadence precision) is the single highest-leverage fix and it cleans the keychain
  structure that, per Contrapunctus, drives chord-ID downstream.
- **The chord↔key "circularity" is not a defect to break — it is the *correct* design** (key-first, chord
  scored against key), *provided the key is good*. Contrapunctus resolves chords against a resolved keychain;
  AugmentedNet/AnalysisGNN emit key+chord jointly but lose to the rule-key pipeline. So we should **stop
  treating the frozen-key seam as a structural defect** and instead **make the key good first** (K1). The
  circularity dissolves by quality, not by re-layering.
- **The post-scoring gate cluster (C2) is selection-layer compensation — and selection is saturated.** So
  dissolving it is a **code-health** refactor, not an accuracy lever. **Deferred / low priority.**
- **X1 (the ≥0.8 confidence gate silencing cadence/pivot on uncertain regions) is no longer a standalone
  structural item — it is a *companion to K1*:** it suppresses cadence evidence exactly where the key is
  uncertain, i.e. where K1 most needs it. Fold X1 into the key-axis work.

## 3. The revised implementation plan (priority order)

**Architecture phase — essentially complete / re-scoped:**
- Byte-identical layer splits + shared-primitive extraction (steps 1–2): **done, pushed** (`dd418ecfed`).
- The anchor (old step 3): **ABANDON** — architecture already correct. Close it in the phase-2 doc + obligation map.
- Gate-dissolution C2 (old step 5): **DEFER** — code-health, not accuracy; selection is saturated.
- The "circularity" X2: **re-classified** — not a defect; resolved by key quality (K1), not re-layering.

**Inference phase — measured under a fixed metric, in this order:**

1. **★ METRIC FIRST (precondition, do before any inference change).** Adopt an **oracle-root** gate (DCML root,
   music21-corroborated) **alongside BIR** — CC proved BIR alone rewards making a *wrong* root equal the bass.
   Strongly consider porting Contrapunctus's **tiered exact-match** accounting (exact ⊂ sameChord ⊂ inversion ⊂
   convention ⊂ sharedBass ⊂ secondaryDiatonic): it cleanly separates genuine error from convention-boundary
   floor, and our existing convention-boundary buckets map straight onto it. Without this, we are steered by a
   proxy that rewards wrong answers. *(Aligns with the Stage-5 granularity-metric work already flagged in
   CLAUDE.md.)*
2. **★ K1 — cadence-detection precision (the #1 lever, validated both sides).** Replace the structurally vacuous
   leading-tone test; kill the spurious I→IV (72%) and V/V→V fires; clean the keychain into long
   cadence-anchored runs. Feeds the modulation detector + joint decision (3 layers). **X1 (ungate cadence/pivot
   from the ≥0.8 confidence gate) rides along here** — it restores the evidence K1 needs on uncertain regions.
3. **K3 soft integration + calibration.** With K1 clean, the soft broad-evidence integration resolves the K2
   relative-pair floor; calibration (a confident-contradiction signal for the home-pin) over any search. This is
   the synthesis layer doing what we measured it does best — *integration, not lattice search*.
4. **(Stage 5+, new — evaluate, don't commit yet) a small learned chord-LABEL re-ranker.** The one place
   Contrapunctus found learning helps (+7pp, simple LR over tonic-rotated windowed PC features), and a candidate
   path past the rule-based chord ceiling AND the symmetric-dim7 floor (context the rule oracle can't use).
   Preconditions: candidate-generation completeness first (our audit: cases "need a candidate never surfaced");
   out-of-sample CV discipline (their lesson: bigger models overfit — keep it small); the oracle/tier metric
   from step 1. **Roadmap item, not now.**
5. **Accept the floors.** ~7% bass-sharing/incomplete-chord ambiguity (engine-independent per their tier data)
   and the symmetric-dim7 pc-undefined set are floors — don't chase them with hand rules; they are the honest
   ceiling (or the learned re-ranker's job).

## 4. Meta-findings to institutionalize (cross-cutting)

- **Oracle/tier metric, never a bare proxy** (BIR rewards wrong-root=bass). Make the dual metric standing.
- **Never learn keys; the lever is keychain structure (cadence precision).** Settled from both sides.
- **Selection/competition is saturated** — stop adding re-ranking heuristics/gates; the residual is
  candidate-generation, key-quality, or floor.
- **Embellishment = chord-first** (segmentation + NCT post-process), never union re-derive / richer vocabulary.
- *(Optional, borrowed)* a `--diff-prose`-style guard so STATUS.md / scoring_model.md numbers can't silently
  outrun the narrative; out-of-sample CV if we ever train.

## 5. Recommendation

Ratify: (a) **abandon the anchor** (architecture correct), **defer C2**, **re-classify X2**, close them in the
docs; (b) **build the oracle-root/tier metric FIRST**; (c) then **pivot to the key axis — K1 cadence precision
(with X1) as the #1 inference lever**, K3 soft+calibration after; (d) put the **learned chord-label re-ranker on
the Stage-5+ roadmap** as the considered path past the rule ceiling. This is the plan both our own measurements
and the external SOTA point to — and it spends effort where the evidence says the accuracy actually is (the key
axis), not where phase-2 guessed it was (the chord/segmentation re-layer).
