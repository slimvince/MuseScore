# CC Instruction — ARCHITECTURE-FIX STEP 2: de-duplicate the inline merge predicate (S1)

> Second structural fix of the phase-2 order (`cowork_phase2_architecture_review.md` §5 step 2). **PURE,
> BYTE-IDENTICAL refactor only — NO inference change, NO behavior change, NO scoring-term touch.** If any
> production output moves by a single bit, the change is wrong → revert. This is the in-file precondition for
> the later anchor (step 3): the merge logic must live in ONE place before its *behavior* is ever changed.

## §0 — Why now / why safe
Step 1 (`8bc1441076`, shared pc primitives) is committed + Cowork-verified byte-identical. Step 2 is the next
lowest-surprise structural item: collapse the duplicated **inline same-root region-collapse** logic into one
helper. It changes no boundary, no score, no merge *threshold* — only removes a "keep in sync" duplication that
can drift. **Unlike step 1, there is NO B2 entanglement** — `regionanalyzer.cpp` is clean in the working tree
(Cowork-verified, matches HEAD), so no stash dance is needed.

## §1 — Scope (grounded at the committed object `8bc1441076` by Cowork)
**Two** inline sites in `src/composing/analysis/region/regionanalyzer.cpp` carry the SAME same-root/same-quality
region-collapse predicate + merge body, with explicit "keep in sync" comments (it is a **duplication across 2
sites**, not a triplication — the comments reference exactly one sibling each):

- **Pass-1 (main loop):** predicate at ~`:698-700`, comment ~`:692-696`, merge body ~`:701-706`, else-branch
  region construction follows.
- **Pass-2/2b:** predicate at ~`:911-913`, comment ~`:907`, merge body ~`:914-919`, else-branch follows.

The two are **identical in predicate and merge body**, differing only in (a) variable names
(`regions`/`chosenResult`/`tones`/`regionStart/End` vs `pass2Regions`/`chosenSub`/`subTones`/`subStart/End`) and
(b) the **else-branch** HarmonicRegion construction (Pass-2 also sets `keyModeResult`, etc.). The source comment
states this verbatim: *"Same predicate and merge body; only the else-branch HarmonicRegion construction differs."*

**The duplicated logic to extract (both sites):**
- Predicate: contiguous-with-previous (`!empty() && back().endTick == newStart`) **AND** `back.chordResult
  .identity.rootPc == candidate.identity.rootPc` **AND** `back...quality == candidate...quality`.
- Merge body: `back.endTick = newEnd; mergeChordAnalysisTones(back.tones, newTones);` then recompute **only**
  bass (`bassPc`/`bassTpc` from `bassToneFromTones`).

**Extract to ONE file-local helper** (anonymous namespace / `static` in `regionanalyzer.cpp` — this is
region-merge logic, NOT a general pc util; it does **not** go in `analysisutils.h`). Both call-sites call the
helper; **each keeps its own else-branch** (they differ — do not touch them). Suggested shape:
`bool tryCollapseSameChordRegion(std::vector<HarmonicRegion>& regions, const <ChordResult>& candidate,
int newStartTick, int newEndTick, const <Tones>& newTones)` → returns true if merged (caller skips its
else-branch), false otherwise (caller runs its existing else-branch unchanged).

## §2 — ★ The byte-identity trap you MUST preserve (the short-circuit / empty-vector hazard)
The originals rely on **`&&` short-circuit** so `regions.back()` / `pass2Regions.back()` is **never evaluated
when the vector is empty** (the `!empty()` contiguity term comes first). **A naive helper that takes
`HarmonicRegion& back` would evaluate `regions.back()` at the CALL SITE to bind the reference — UB when the
vector is empty.** The helper must therefore take the **vector** (by reference) and compute the `!empty() &&
back().endTick == newStartTick` contiguity **inside**, preserving the exact short-circuit order. Verify the
empty-vector path is still safe (first region of each pass: vector empty → no `back()` access → falls to the
else-branch, as today). This is the one real hazard — get it wrong and you either crash or change behavior.

Secondary checks: confirm `isContiguousWithPreviousRegion` / `isContiguous` are not USED elsewhere in their
passes (if they are, keep the outside computation; the helper can still own the predicate). Confirm the merge
body's bass-recompute is character-identical at both sites (it is, per Cowork's read — but re-verify).

## §3 — Out of scope (do NOT touch)
- **Pass-3's length-gated merges** (`coalesceShortSameRootRuns`, `absorbShortRegions`) — a DIFFERENT mechanism
  (length/identity-gated), part of step 3's over-segmentation story. Leave them entirely.
- The **else-branches** (region construction) — they differ; leave both in place.
- Any **threshold / boundary / merge *behavior*** — this is de-dup only. The merge fires on exactly the same
  cases as today.

## §4 — Byte-identity gates (same bar as step 1)
1. Build clean; **unity/jumbo compiles**.
2. `composing_tests` + `notation_tests` pass (expect 545/545 · 57/57).
3. **`pipeline_snapshot_tests` 11/11 ZERO-diff — do NOT pass `--update-goldens`.** Any golden move = behavior
   changed = WRONG → revert and find it (most likely the contiguity short-circuit or an else-branch you altered).
4. **BIR `.ours.json` 0-diff on all three presets** (Baroque 57 / Jazz 23 / Default 57) by case-identity, vs the
   step-1 HEAD reference corpora.
5. No scoring term touched → no `docs/scoring_model.md` sync. (If you update the "keep in sync" comments / the
   `docs/implementation_roadmap.md 0.6` note they reference, that's fine — doc-only.)

## §5 — Workflow + deliver
- **Commit LOCALLY (unpushed)** on top of `8bc1441076`. Do NOT push. Write
  `cc_step2_merge_predicate_report.md`: the helper (signature + placement), the byte-identity argument (incl.
  the empty-vector short-circuit preservation), the site count confirmation (2, not 3), and the §4 gate
  results.
- Cowork then verifies at the committed object: the helper, both rewritten call-sites (predicate + merge body
  character-identical to the originals, else-branches untouched), the empty-safety, and the gates. Revert if
  anything moved.

## §6 — Stop conditions (any → STOP, do not push, surface)
- Any snapshot golden diff / BIR case-identity change / test failure → not byte-identical → STOP + revert +
  report the divergence.
- The empty-vector path cannot be made provably safe in the helper shape you chose → STOP, rethink the
  signature (take the vector, not `back()`), do not ship UB.
- A third inline site, or an else-branch difference deeper than `keyModeResult`, turns up → note it, do not
  force the extraction; surface for a scope call.
- Any temptation to "improve" the merge while extracting (widen the predicate, touch a threshold) → STOP.
  Extraction only.
