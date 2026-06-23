# Cowork PHASE 2 — Architecture Review (Cowork-led synthesis)

> **★ This is the deferred back-half of the acceptance review** (`docs/layer_audit_plan.md` §5). Phase 1
> audited each of the ~19 layers in isolation (6 high-value layers reconciled CC↔Cowork). Phase 2 asks the
> COMPOSITION question: **are these the right layers, do responsibilities sit in the right place, and does the
> data flow feed-forward or circle?** Cowork leads (the cross-layer + target-architecture context); CC supports
> empirically (`cc_instruction_phase2_architecture_support.md` — five data-flow claims to confirm/correct).
>
> **★ PROVENANCE.** STRUCTURE below = committed-object source reads (this session) + the reconciled phase-1
> map. The five claims marked `[CC-confirm]` are pending CC's phase-2 empirical pass — they are the load-bearing
> data-flow facts and are NOT yet re-confirmed at source by CC. Everything else is source-grounded or
> CC-measured in phase 1.
>
> **★ SEQUENCING GATE (user, 2026-06-17): STRUCTURAL fixes BEFORE inference.** Phase 2's output is the
> architecture-fix ORDER. No fix is implemented here — the audit is read-only. The order produced here is the
> precondition for the eventual inference-correctness work, which begins only on the corrected architecture.

---

## §1 — The verdict in one paragraph

The layering is **mostly right and mostly feed-forward**, and the two-track remedy (chord = hand-buildable
competition rules; key = soft-evidence quality + calibration) survives phase 2 intact. But phase 2 surfaces a
clear structural ordering: the architecture has **one load-bearing structural defect (segmentation /
region-pass), one principled non-layer (the post-scoring gate cluster), one genuine circularity (chord↔key),
and a scatter of duplicated/misplaced responsibilities.** Per the sequencing gate these are fixed FIRST, and
they have a natural order because they are **not independent** — the segmentation defect (S1/S2) sits upstream
of the gate cluster (C2) and the chord competition (C1), so fixing it first shrinks everything downstream.

## §2 — Decomposition: are these the right layers?

**Right layers, three responsibility defects.**

- **D1 — `regionanalyzer` is a multi-pass pipeline masquerading as a layer (S1/S2). [CC-confirm #1/#2]** The
  Pass-1/2/2b/3 structure with a "keep in sync" triplication is the single biggest decomposition smell, and
  audit #6 made it the biggest *correctness* lever too: **over-segmentation = 37.7% of the functional residual**
  (the HELD bucket — larger than the entire competition layer's ~24%). Two distinct problems live here: the
  **duplication** (Pass-1/2/2b re-derive the same region facts → de-dup, behavior-sensitive) and the
  **chord-identity-≠-final-region** seam (Pass-3 merge mutates tones after the chord is computed → the chord is
  a stale function of its region). These are the deepest re-layering target and they gate the chord axis.
- **D2 — the post-scoring gate cluster is ~83% compensation, not a layer (C2). [CC-CONFIRMED ~83% + CORRECTED]**
  `postscoringgates` A–L + `chordpostpasses` + `sparsechordrefinement` are context patches: each reads
  next-region / key / bass to repair what the *local* competition got wrong — by construction, **the absence of
  a joint formulation** expressed post-hoc. **CC tally (verified at HEAD): of the 12 live gates, 10 read
  cross-region/key context = compensation; B/C/D are already-removed dead code (Stage 3.4b, byte-identical).
  ★ Two gates — A (Maj-add6↔m7 enharmonic) and J (inverted dom-7 completeness) — are PURELY-LOCAL vertical
  refinements that must be PRESERVED through the dissolution, not deleted with the rest.** In the target
  architecture the 10 compensation gates DISSOLVE into the competition once it sees the same context up front;
  A and J survive. Phase-2 verdict: keep as-is until the chord/region/key re-layering lands, then dissolve the
  10, keep the 2.
- **D3 — two layers carry >1 responsibility, both already corrected in the map (S3).**
  `harmonicfunctionlayer` = **2 jobs** (progression/temporal-scoring + competition); function/degree is
  correctly delegated to `buildChordResult` (`chordanalyzer.cpp:952`, verified) — so this is a *mild*
  smear (it also marshals `gateCtx`), not the 3-way split I first claimed. The cleaner split is deferred and
  low-value. The more actionable S3 item is the **duplicated key-collection/pc primitive** re-implemented across
  ≥4 layers `[CC-confirm #5]` → extract one shared primitive (byte-identical-safe if it is genuine duplication).

Everything else (cadence anchor, modulation detector, key scorer, joint decision, the vertical oracle, the
output/formatter layers) is single-responsibility and correctly placed. The key axis in particular is clean:
the only key-axis structural item is the **two key-decision paths** (active `keyresolver` hysteresis + dormant
`jointkeydecision`) — a migration, not a defect, and explicitly deferred.

## §3 — Interactions: feed-forward or circular?

- **I1 — one genuine circularity, and it is PERVASIVE: chord↔key (X2). [CC-CONFIRMED + EXTENDED]** I had it as
  two oracle leaks; CC verified at HEAD that the key is read at **every stage of the chord path**: the oracle
  ×2 (`diatonicRootContribution` tiebreak + the `dim7CharacteristicBonus` rotation-selector that *defines* the
  symmetric-dim7 root from the key) — **and the source itself states these are "frozen into `cell.basisIndep`"
  before the competition runs** (`chordanalyzer.cpp` ~:1436, verified verbatim) — PLUS `buildChordResult`
  (degree/diatonic check) + `sparsechordrefinement` ×4 + 4 post-scoring gates. So breaking the circularity is
  **not "remove two terms"** — it is **re-architect the chord oracle to take the key as an explicit joint
  variable**. The current architecture manages it with the re-emission/2-pass freeze (a workaround, not a
  resolution). This is the one place the data flow is NOT clean feed-forward, and the frozen-key half composes
  with the segmentation seam (see §3.5).
- **I2 — the ≥0.8 confidence gate is an upstream silencer (X1).** `hasAssertiveKeyConfidence` switches OFF
  cadence/pivot detection, KeyArea grouping, and the old detector — on exactly the uncertain regions that most
  need them. This is an *interaction* defect (a gate that suppresses evidence precisely where evidence is
  scarce), and it couples the key-confidence estimate to the chord-context machinery. Structural-ish:
  the fix is to stop gating evidence-gathering on the thing the evidence is supposed to determine.
- **I-anchor (§3.5) — the FROZEN FEED-FORWARD SEAM (CC's sixth issue, VERIFIED at HEAD).** Claims 2 and 4
  compose into one defect deeper than either alone: the chord is finalized **before** its region's tones are
  final (the Pass-3 merge folds in more tones and recomputes **only the bass** — `regionanalyzer.cpp:138`,
  verified), **and** the oracle's key dependency is **frozen into `basisIndep` pre-competition** (verified
  verbatim). The source documents the consequence directly: the joint re-key pass "calls decideJointKey ONCE
  (frozen — no fixpoint)" and **cannot re-emit the chord** because "the production chord is emitted
  mid-pipeline, before Pass-3 tone merging" (`regionanalyzer.cpp:309-316`, verified verbatim). The result is a
  one-shot frozen-forward pipeline — segment → chord(key₀, partial-tones) → merge → key₁ — with **no fixpoint**,
  the exact opposite of the joint target. **This single ordering defect is the precondition for BOTH the
  gate-dissolution (I1/D2) AND the joint-key activation** — it is the highest-leverage structural obligation and
  it anchors §5.
- **I3 — the unifying diagnosis holds (X3).** Both axes reduce to "a local decision needs CONTEXT." The gate
  cluster (chord) and the cadence/relative-pair walls (key) are the same root cause, re-derived bottom-up from
  the layer audits — which is why the constrained-joint architecture is the right target for both. Chord-joint
  is tractable (the gates already encode the context); key-joint is walled on K1 cadence precision, and the
  joint *search* is measured inert (K3) — so "joint" here means **broad soft evidence + calibration up front**,
  not a lattice.

## §4 — Against the target (`architecture_joint_inference.md`)

The current layering is the constrained-joint target with two deferred bolt-ons: the **post-scoring gate
cluster** (the un-dissolved compensation, D2/C2) and the **dormant `jointkeydecision`** (the key synthesis,
wired but OFF). Phase 2 confirms both deferrals were correct *at the time* but are now ordered: the gate
dissolution is blocked on the segmentation fix (you cannot dissolve gates into a competition whose regions are
still being mutated underneath it), and the joint-key activation is blocked on K1 cadence precision (the soft
evidence it integrates is still too noisy). Neither is a structural defect to fix now; both are downstream of
the items in §5.

## §5 — The structural fix-first ORDER (the phase-2 deliverable)

Sequenced so each fix shrinks the next (NOT by raw size). **The order was reframed by CC's sixth issue:** the
chord-finalized-before-its-region defect and the frozen-key half of the circularity are ONE seam, and that seam
is the precondition for both the gate-dissolution and the joint-key work — so it is the anchor (step 3), and
the circularity no longer sits as a separable last item. Per the sequencing gate, this whole list precedes any
inference-correctness work. Tags: **[BI]** = byte-identical-safe refactor (do anytime); **[BS]** =
behavior-sensitive (measure-gated, BIR 57/23/57 + both test suites must hold).

1. **S3-primitive — extract the 2–3 shared pc/collection primitives [BI]** `[CC-CONFIRMED, corrected to 2–3]`.
   Two families, not one: the trivial helpers (`pcMod12`/`pcInMask`) + the signature-derived mask dissolve into
   one shared `pitchclassutils.h` (also removes the ODR-prefix workaround); the **local-key tonic+mode
   collection** (lmd/jkd) is a SECOND primitive to extract once. Pure de-dup, no behavior change. Lowest risk,
   do first.
2. **S1 — de-duplicate the inline merge predicate [BI→BS]** `[CC-CONFIRMED; Cowork-corrected: 2 inline sites,
   not 3]`. Extract the same-root/quality collapse predicate+body (Pass-1 ~:699 + Pass-2/2b ~:912, each with a
   "keep in sync" comment — a DUPLICATION across 2 sites, not a triplication; Pass-3's length-gated merges are
   separate, step 3) to one file-local helper — byte-identical, preserving the empty-vector short-circuit. It is the **enabling precondition** for the merge-behavior correctness fix (which is
   inference work, deferred): the merge logic must live in one place before it is changed.
3. **★ ANCHOR — compute the chord ONCE against final region tones, with the key as an explicit input [BS, DEEP]**
   `[CC sixth issue, VERIFIED]`. This composes the old S2 (chord-identity ≠ final-region) and the frozen-key
   half of X2 into the single highest-leverage structural obligation. Re-layer so: segmentation → final tones →
   chord(key) — the chord is a clean function of its final region AND the key is an explicit variable, not
   frozen into `basisIndep` mid-pipeline. This is what makes a joint fixpoint *possible*; it unblocks BOTH steps
   5 and the eventual joint-key activation. The deepest structural fix; measure-gated.
4. **X1 — ungate evidence-gathering from `hasAssertiveKeyConfidence` [BS]**. Stop silencing cadence/pivot/
   KeyArea on uncertain regions. Independent of the anchor; behavior-sensitive on the key axis; feeds K1.
5. **C2 — dissolve the 10 compensation gates into the competition; PRESERVE Gates A & J [BS, BIG]**
   `[CC-CONFIRMED ~83%]`. Only AFTER the anchor (regions stable + key explicit) — fold the 10 context-reading
   gates into a competition that sees the context up front. **Gates A and J are purely-local vertical and must
   survive** (CC-verified); B/C/D are already dead. The bridge from "patched local decisions" to the joint
   formulation.

**Folded into the anchor (no longer a separate step):** the old "#6 X2 — break the circularity." The frozen-key
half is step 3; the residual is the symmetric-dim7 rotation-selector, which has **no pure-vertical answer** (the
C3 floor) and resolves *with* the joint formulation, not before it.

**Not in this list (correctly):** the `jointkeydecision` activation, the K1 cadence-precision fix, the
**over-segmentation boundary/merge-gating correctness tuning** (Pass-2/2b + the merge thresholds — CC confirmed
the 37.7% is a soft ~38–42% proxy owned by both boundary-creation AND the over-conservative merge, and the
*correctness* tuning is behavior-changing), and the competition-rule completion (C1) are all
*inference-correctness* work — they come AFTER this list, on the corrected architecture. The
`harmonicfunctionlayer` 2-job split (D3) is low-value cleanup, optional, fold into step 5 if convenient.

## §6 — What phase 2 did NOT change

The two-track remedy (§E of the obligation map) stands unaltered: chord-axis = hand-buildable competition rules
(C1, led by cadential-6-4) + gate-dissolution (C2); key-axis = soft-evidence quality + calibration (K1 first,
then K3's soft integration), NOT a joint search. Phase 2's contribution is the **ordering**, sharpened by CC's
empirical pass: the chord-finalized-before-its-region seam (the ~38–42% held-harmony residual driver) is
**structural AND upstream of everything else on the chord axis** — and it composes with the frozen-key
circularity into a single anchor obligation. The architecture is sound; the work is to remove the deferred
compensations (the dup primitives, the Pass triplication, the frozen feed-forward seam, the 10 compensation
gates) in the order above, then reopen inference on the result. *(One caveat carried forward: the 37.7% is a
soft proxy ~38–42% owned by both boundary-creation and an over-conservative merge — the anchor re-layering
makes the chord a clean function of its region, but the residual boundary/merge TUNING is later inference
work, not structural.)*

## §7 — Status

- **Phase 1:** COMPLETE — all ~19 layers; 6 high-value layers reconciled CC↔Cowork.
- **Phase 2:** RECONCILED. CC's five-claim empirical pass (`cc_phase2_architecture_support_report.md`) folded
  in; all five claims CONFIRMED with sharpening corrections + a sixth (the frozen feed-forward seam) that
  reframed the §5 order. **The load-bearing facts (the "frozen — no fixpoint" comment, the recompute-only-bass
  seam, the `basisIndep` freeze, the B/C/D dead-code removal) were Cowork-verified verbatim at the committed
  object HEAD `a03c2493bb`** — not taken from CC's working-tree line numbers. Track record holds: CC's
  structure confirmed, the attributions/quantities sharpened (gate cluster 100%→~83% with A/J preserved;
  circularity 2 leaks→pervasive; pc primitive 1→2–3; 37.7%→soft ~38–42% proxy).
- **Next after ratification:** the architecture-fix phase executes §5 in order (structural, measure-gated, BIR
  57/23/57 + both suites held), THEN inference-correctness work reopens on the corrected architecture. Nothing
  is implemented until the user ratifies this order.
