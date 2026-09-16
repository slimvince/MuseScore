# CC Instruction — PHASE 2 (empirical support): architecture data-flow confirmation — READ-ONLY

> Phase 1 is complete (all ~19 layers audited; 6 high-value layers reconciled CC↔Cowork). Per
> `docs/layer_audit_plan.md` §5, **phase 2 = the architecture review, Cowork-LED** (the cross-layer/target
> context) **+ CC-SUPPORTED empirically.** This instruction is the CC empirical half: **confirm-or-correct, at
> the committed object, the five data-flow / structure claims the phase-2 verdict rests on.** **READ-ONLY —
> NO code/behavior/inference change. Findings only.** **North star: best = CORRECT inference vs the DCML/
> music21 oracle.** Your fresh source read + any read-only probe is authoritative; Cowork's claims below are to
> be CONFIRMED or CORRECTED (the phase-1 track record: structure held, quantities/attributions did not — keep
> correcting).

## §1 — Scope (confirm the STRUCTURE, not re-audit the layers)

Phase 1 already pinned each layer's obligations. Phase 2 asks a different question: **are these the right
layers, and do they compose correctly?** Your job is to ground the five cross-layer claims below in source +
call-graph fact so the decomposition verdict is not built on memory. Read-only; you MAY trace call-sites,
dump the include/call graph, and run read-only diagnostics already committed. **No production edit.**

## §2 — The five claims to confirm-or-correct (MEASURE / TRACE, don't recall)

1. **S1/S2 — the `regionanalyzer` Pass structure (the biggest structural claim).** Cowork has it as
   **Pass-1 / Pass-2 / Pass-2b / Pass-3** with a "keep in sync" triplication, and **over-segmentation = 37.7%
   of the functional residual** (audit #6, HELD bucket). **Trace the actual passes** in `regionanalyzer.cpp`:
   how many passes, what each does, where the duplication is (the "keep in sync" comment/logic), and **where
   segmentation boundaries are actually decided** (is it `harmonicsegmenter.greedyExpandSegmentation`, a
   regionanalyzer pass, or both?). **Confirm or correct** the 37.7% attribution to *segmentation* specifically
   (vs merge/Pass-3). This decides whether S1 (Pass de-dup) and the segmentation-correctness lever are the
   SAME structural fix or two.
2. **S2 — chord-identity ≠ final-region.** Cowork: Pass-3 merge changes a region's tones AFTER the chord is
   computed, so the chord layer's output is not a clean function of its final region (broke re-emission).
   **Confirm at source:** does a post-chord pass mutate region tones? Trace the order: tones → chord → merge →
   (stale chord?). This is the re-layering target; confirm it's real and locate the exact seam.
3. **C2 — the post-scoring gate cluster = compensation, not a layer.** Cowork: `postscoringgates` A–L +
   `chordpostpasses` + `sparsechordrefinement` are CONTEXT PATCHES (each reads next-region / key / bass to fix
   a local-competition error). **Trace what each gate reads** (its inputs) and **classify**: how many gates
   consume cross-region/key/bass context (= compensation for non-jointness, the dissolution target) vs are
   genuinely local vertical refinements (would survive a joint formulation)? A rough A–L tally is enough — the
   question is *what fraction of the gate layer is compensation*.
4. **X2 — the chord↔key circularity, exact leak points.** Cowork: the "vertical" oracle reads the key in
   **TWO** terms — `diatonicRootContribution` (ambiguous-root tiebreak) AND the `dim7CharacteristicBonus`
   rotation-selector (defines the symmetric-dim7 root by reading the key) — plus `sparsechordrefinement` reads
   the key. **Confirm all three at source** (file:line) and report any OTHER key-read inside the chord oracle.
   This sizes the circular dependency the architecture must break.
5. **S3 — the duplicated key-collection / pc primitive.** Cowork: a key-collection/pitch-class primitive is
   re-implemented across **≥4 layers** (`cadencekeyanchor` / `localmodulationdetector` / `jointkeydecision` /
   `tonicizationlabeler`). **Confirm:** is it genuinely duplicated logic (same computation, copy-pasted) or
   distinct per-layer variants? List the actual functions. This decides whether "extract one shared primitive"
   is a real obligation or a mis-read.

## §3 — Deliver

`cc_phase2_architecture_support_report.md`: for each of the five, **CONFIRM or CORRECT** with source
file:line + (where relevant) a measured share, and a one-line structural implication. State which Cowork
claims you confirm vs correct. Flag any SIXTH cross-layer structure issue you see while tracing (a circularity,
a misplaced responsibility, a seam that lies). Read-only; Cowork folds this into the phase-2 verdict; user
ratifies. Do NOT propose or implement fixes — phase 2 produces the obligation order, not the patches.

## §4 — Stop conditions

- Any production / inference / behavior change → STOP. A probe that moves production output → STOP.
- Uncertain → check vs the oracle / the committed object; never guess. If a claim is neither cleanly confirmed
  nor corrected (genuinely ambiguous), say so + give what you found — do not force a verdict.
