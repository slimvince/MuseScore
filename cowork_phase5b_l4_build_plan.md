# Phase 5b — incremental L4 build + engagement (investigate-each-step) — plan

> **Goal.** Build the clean L4 the signed spec (`cowork_layer4_chordsymbol_design.md`) describes and **engage** it,
> retiring the legacy `analyzeChord`/`ChordPathDecoder` chord path — **incrementally**, with a **CC investigation/check
> at every step** so each finding can amend the *next* steps (or, worst case, flag that the **layer architecture** needs
> amendment) before we are committed. The two-tier BIR gate is now restored (`5357f5a7ed`).
>
> **Method per step (non-negotiable):** **INVESTIGATE (CC, read-only) → BUILD → VERIFY (Cowork, by-sha + source) →
> ASSESS-FOR-AMENDMENT.** No step starts before the prior step's assessment is in. A surprising finding pauses the
> sequence and re-plans — that is the point of going incremental.
>
> **Standing constraints:** build-it-right only — **no inference-quality tuning** (the firewall; the leading-tone C→F
> stays untouched). The new path is built **alongside, dormant (byte-identical)** until *proven*, then engaged behind
> the gate. Whole engagement is behaviour-changing → **zero class-(b) regressions ever; class-(a) symmetric churn only,
> every case verified.** `upstream` never.

## The incremental shape (new path ALONGSIDE → prove → switch → retire)
The legacy path is **per-region** (`greedyExpandSegmentation` + `analyzeChord` + `ChordPathDecoder`). The new path is
**per-slice** (`changePointSlices` + `chordslicedecoder`). They are *different decompositions*, so engaging the new path
**will move the corpus output** — that movement is the behaviour change we gate, not a byte-identity violation. We build
and prove the new path **before** any switch.

## Step 0 — INVESTIGATE the starting line (grounds everything; read-only)
Before any build, CC establishes, at source + by measurement:
- **What `chordslicedecoder` already is** (Increment-A naming, Increment-B membership/twoPass) vs **what the spec
  requires** (commit/inherit/**abstain**, the three-tier membership rule, the symmetric-root **spelling-pin** = unbuilt
  Increment-C). The exact gap.
- **How the new path compares to legacy *today*** — run `chordslicedecoder` over the corpus diagnostically (NOT engaged)
  and compare its chord identity to the legacy/GT (the BIR metric). Where do they agree / differ, and by how much?
- **Any architecture friction** surfaced (per-slice vs the L2 slicer granularity; how L3 key + the section layer would
  interact with a per-slice chord path; whether the spec's decomposition still fits the as-built L1–L3).
- **Output:** the grounded **increment sequence** (which sub-builds, in what order) + a first GO/NO-GO read on whether
  the new path is plausibly equivalent-or-better, or whether the architecture needs a rethink. *(This step can rewrite
  Steps 1–n.)*

## Steps 1..n — BUILD the new-path increments — GROUNDED ORDER (Step-0 `9ef7ff312a`: the −15 maps to G1)
Step 0 measured the new path **−15 vs legacy** (58 vs 74% chord-root), and **all of it is the unbuilt
commit/inherit/abstain mechanism (G1)** — architecture sound (per-slice fits the slicer + L3 spine, no amendment). So
the order is **re-ordered to attack the lever first.** Each increment is **byte-identical** (decoder production-dead,
dormant — corpus 53/24/53 unchanged), and each ends with a **re-measure** of the new-vs-legacy delta:
- **Step 1 — commit / inherit / abstain + the ≥3-chord-tone sufficiency gate (G1 — THE LEVER) — ✅ DONE.** The −15 lived
  here (41% phantom roots + 42% thin slices = over-commit to noise — no abstain, no sufficiency gate). Built per the
  spec (`enableCommitDecision`/`applyCommitDecision`); closed most of the deficit and confirmed the sequence holds.
- **Step 2 — membership three-tier ladder (G2/G3) + the §4 two-reading both-sides inherit — ✅ DONE & ACCEPTED**
  (`d52cfd0847` + `4aa88452cd`). G2/G3 accuracy-neutral/correct; the two-reading inherit is the **best variant**
  (coverage-matched 68.0%, fewest misses 573, thin-slice misses 300→61). Its abstain is *higher* (58.2%) **by design** —
  it correctly declines TRANSITION slices → L5 (spec-faithful). **§15-O2 (bounded-window joint) is now UNLOCKED but
  DEFERRED to Step M** (adopt only if the engage coverage-matched assessment shows the two-reading falls short; its
  window bound is delicate — must not cross into L5 progression grammar).
- **Step 3 — confidence model + open-question label (G6) — ✅ DONE.** Beyond margin-only; names the open question on
  abstain + carries competing readings for L5 (the *representation*, not threshold-tuning — Phase B). The L4→L5 contract.
- **Step 4 — spelling-pin (G4 — small, ~3.1%, last) — ✅ DONE.** Symmetric-root via `spellingview`. **Split Increment-C:
  C1 spelling-pin (dormant, byte-identical) built + C2 new four-note dim7/mMaj7 types (G5, gated → engage) deferred** so
  new types don't move legacy output (Step-0 F-4).
- New types (G5) / bounded-context (G7) / **section-grouping integration (F-3)** + the **§15-O2 decision** → the
  **engage** step (Step M).
- **★ Per-step gate (CORRECTED — the §F mis-framing fix):** re-measure new-vs-legacy and judge by **coverage-matched
  accuracy + *correct* abstention** (declining genuinely-ambiguous slices → L5 is RIGHT), **NOT raw coverage**. An
  increment that improves coverage-matched accuracy while abstaining correctly is a GO even if raw committed-fraction
  drops. STOP/amend only if coverage-matched accuracy regresses or a *class-(b)* error appears.

## Step M — MEASURE: new path vs legacy, the engagement GO/NO-GO (read-only)
With the new path complete, the full diagnostic comparison on the corpus (both presets): the new per-slice path's BIR
vs the legacy's, case by case. **Decision gate:** engage only if the new path is **equivalent-or-better** — **zero new
class-(b) regressions**, class-(a) churn understood. If it regresses class-(b), STOP and re-plan (the spec or a prior
increment needs amendment — exactly what incremental + investigate-each-step exists to catch).

## Step E — ENGAGE (switch production to the new path) — behaviour-changing, two-tier gate
Switch `regionanalyzer.cpp` onto the new L1→L4 spine (the bounded-context engagement + the new chord path), per the
parameter form already in place. Investigate the engagement delta (BIR + snapshots); the snapshot goldens refresh **only**
if the change is verified-correct. **Fold in the German-bass correctness fix here** (it's an L4 formatter fix). The
F17 dense-start config alignment is decided here too (now that the gate runs).

## Step R — RETIRE legacy (after engagement proven) → the unification close
Retire the legacy per-region path: `greedyExpandSegmentation`, the legacy `ChordPathDecoder` commit chain, the second
pitch-context builder, and resolve the staged scaffolding (audit Q1/Q5). Each its own gated step. **→ L1–L4 unification
complete.**

## Then — the coverage seal (D13) + the L1–L4 COMPLETE gate
With the L4 path final, the moving-~600 branch triage closes, the defensive-exclusion + covered-but-uncredited ledgers
are applied, and the union reachable-branch seal is measured. → **✅ L1–L4 COMPLETE (nothing left)** → L5.

---
**First action: Step 0 — the read-only grounding investigation.** Everything after it is provisional on its findings.
