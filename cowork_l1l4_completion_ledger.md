# L1–L4 completion ledger — the "no-residue" map to FINISHED (2026-06-26)

> **Purpose.** Enumerate **everything** still outstanding on L1–L4 so "finished" is well-defined and nothing falls
> through — the precondition for the **L1–L4 COMPLETE (nothing-left)** gate before L5. "Finished" (the user's standing
> bar) = each layer **restructured + built + dead-code resolved + legacy retired + regression/reachable-branch tested**,
> specs synced to as-built, **nothing left**.
>
> **Key dependency:** items marked **[BA-GATED]** are *behaviour-changing* and need the corpus two-tier BIR gate, i.e.
> **`batch_analyze` restored** (the Qt `platforms/`-plugin blocker). Items marked **[NOW]** are doable immediately
> (read-only or tests/docs, no corpus). This is why the test-path (step 2) is effectively a prerequisite for most of
> step 1.
>
> ## ⛔ STANDING FIREWALL — no inference-quality improvement until the stack is finished (user mandate, reaffirmed 2026-06-26)
> **Improving the *accuracy of the analysis* (Phase B) is FORBIDDEN until a meaningful number of layers — the full
> forward L1–L6 stack — are built and "finished."** Nothing in this ledger is inference-tuning; it is all build-it-right.
> The line, because it WILL blur during the finish:
> - **Build-it-right (allowed now / during the L4 build):** architecture, each layer's algorithmic completion per its
>   spec, and plain **correctness** bugs — crashes, contract violations, rendering errors (e.g. **C7 German-bass slash**).
> - **Tune-precision / inference improvement (Phase B — LAST):** making the analysis *more accurate on hard/ambiguous
>   cases* — the scale lever, leading-tone de-brittling, tpc-weight calibration, ambiguous-case accuracy.
> - **The trap, live in this ledger:** the **leading-tone presence-gate / Mozart C→F key regression is INFERENCE-QUALITY
>   → Phase B → DO NOT TOUCH during the finish**, even though it is a known wrong answer. It is pinned only as a labelled
>   regression-guard. Fixing the *key misread* is precisely the inference work the firewall defers.

## A — Structural / unification residue (Phase 6) — [BA-GATED]
1. **Two live segmenters →** retire legacy `harmony/greedyExpandSegmentation` (`regionanalyzer.cpp:757`) onto
   `slicing/changePointSlices`. (audit Q1.1)
2. **Two pitch-context builders →** collapse `collectPitchContext` (legacy) + `pitchContextOverSpan` to one. (Q1.2)
3. **Staged scaffolding — wire-or-remove verdict:** `chordslicedecoder`, `redecodeRange`, `tonicizationlabeler`, inert
   `DecodeQualityLevel::Normal/Deep`. (audit Q5; the verdict comes *from* the L4 build, item B.)
4. **`analysisutils.h` mislocation** (the deferred D1 follow-up): its free functions are cross-cutting key/pitch utils
   mis-placed in `chord/`; relocate out of `chord/` (~20 include edits) so the `.cpp`-level L3→`chord/` include goes too.

## B — L4 algorithmic build + engagement (Phase 5b) — [BA-GATED]
5. **Build the clean L4** per `cowork_layer4_chordsymbol_design.md`: per-slice namer with **commit/inherit/abstain
   (declare uncertainty)**, the symmetric-root **spelling-pin** (consuming the Phase-4 `spellingview` primitive), the
   membership/NCT backlog in `cowork_delta_check_dispositions.md`.
6. **Engage** — switch production (`regionanalyzer.cpp`) onto the new L1→L4 spine (the bounded-context engagement +
   the new chord path). *(This is what makes A1–A3 retireable.)*

## C — Surfaced correctness defects (from the backfill) — [BA-GATED to fix]
7. **German flat-bass slash drop** (`csfIsValidBassNoteName` rejects `Ces`/`Fes` → slash dropped). Recorded as a
   `DISABLED_` test + labelled guard (cluster 3). **L4 correctness bug, not inference** — fix during the L4 build.
8. **`chordanalyzer.cpp:449`** — a reachable scoring-internal arm with no clean single-winner oracle (cluster 2,
   deferred). Resolve as a characterization or with the L4 build.
9. *(Nashville chromatic `"?"` + crude slash-bass degree — known **placeholders / future feature**, not a bug; pinned
   as labelled guards.)*

## D — Coverage seal (criterion-4 completion, Phase 6)
10. **[NOW]** **Moving-~600 branch triage** — classify the unhit branches in the *moving* files (`regionanalyzer`,
    `sectionanalyzer`, legacy `harmonicsegmenter`, `chordslicedecoder`, the gated section detectors, `keyresolver`,
    `sparsechordrefinement`) into add-test / wire-or-remove / exclude. *(Read-only analysis; but the add-test/remove
    halves only resolve **after** the L4 build reshapes those files — so triage now, close at the seal.)*
11. **[NOW]** **Defensive-exclusion ledger** — the ~169 EXCLUDE branches the four stable clusters re-classified
    (provably-unreachable guards) get formally annotated/excluded from the coverage denominator.
12. **[NOW]** **Covered-but-uncredited ledger** — the inline-header/COMDAT-folded branches `llvm-cov` can't credit but
    tests execute (cluster 1 `isChordTrackStaff:83`; cluster 2's 13 `chordanalyzer.h`/`analysisutils.h` arms).
13. **[BA-GATED]** **Final reachable-branch seal** — re-measure union branch% after the build + exclusions; the seal is
    over *reachable, test-confirmed* branches, not a raw %.

## E — Spec-sync + delta-check (Phase-5 sign-off) — [NOW]
14. **Sync L1–L3 design docs to as-built:** bounded-context capabilities (L1 extend / L2 reslice / L3 reach-back), the
    tpc `spellingview` primitive, the types-header relocation, kMasks single-source. *(Cowork writes.)*
15. **Delta-check** — CC re-runs the spec↔implementation check read-only → zero divergence. Then the standing net
    (suites/snapshots green) confirmed.

## F — Test-path: `batch_analyze` (step 2) — [restore + unification audit]
16. **Restore** `batch_analyze` — the Qt `platforms/`-plugin blocker (it loads no score this session). Unblocks all
    [BA-GATED] items.
17. **[NOW]** **Unification audit of the test-path** — confirm `batch_analyze`'s analysis path **IS** the production
    path (`regionanalyzer`/the live entry), **not** a duplicate/parallel analyzer. If it has its own analysis logic,
    the corpus gate would be testing a *different* path than ships (an invalid gate) **and** violate "one path per
    concern." *(Read-only; doable now even with the tool broken.)*

## G — Doc hygiene — [NOW, mostly done]
18. Confirm no stale `57/23` gate refs remain beyond the doc-truth pass; `STATUS.md` current; the deferred
    `function/`-split note (→ Phase 7) and the `analysisutils.h` follow-up (A4) recorded.

---

## Recommended execution order (respecting the BA dependency)
1. **[NOW, parallelisable]** E (spec-sync + delta-check), D10–D12 (triage + the two ledgers), F17 (test-path
   unification audit), G18 (doc-hygiene confirm). None needs the corpus.
2. **F16 — restore `batch_analyze`** (the unblock). Do this **before** the behaviour-changing finish.
3. **[BA-GATED]** B (L4 build + engage) → C7–C8 (defect fixes, folded into the L4 build) → A1–A4 (legacy retirement +
   `analysisutils` relocation) → D13 (final reachable-branch seal). This is the bulk of "finishing L1–L4."
4. **L1–L4 COMPLETE gate** — verify nothing-left against this ledger.
5. **Step 3 — QA review** (documentation + solution, multi-aspect comprehensive) over the finished L1–L4.
6. **Step 4 — L5 spec.**

**Honest scope note:** items A, B, C, D13 are a substantial behaviour-changing body of work (the actual L4 rebuild +
retirement), all gated on F16. "As finished as possible *now*" = the [NOW] items (E, D10–12, F17, G); the rest needs the
test-path restored first.
