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

## Steps 1..n — BUILD the new-path increments (each dormant / byte-identical, each investigated)
Provisional (Step 0 finalises the list/order). Each its own investigate→build→verify→assess loop; each **byte-identical**
(new path has no production consumer yet — corpus 53/24/53 unchanged):
- **Spelling-pin (Increment-C):** symmetric-root resolution consuming the Phase-4 `spellingview` primitive (the clean
  deterministic tpc use). Unit-tested against the symmetric-root cases (`bwv272@4320` G♯dim7, etc.).
- **Abstain / inherit:** the "declare uncertainty, not guess" path per spec — completed + tested.
- **Membership (three-tier rule):** the spec's stepwise-embellishing / chord-tone-extension / metric-weight decider,
  per the delta-check dispositions backlog.
- After each: re-run the new-path-vs-legacy diagnostic comparison → does this increment move the new path *toward* the
  GT? Assess; amend the next increment if not.

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
