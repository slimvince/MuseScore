# Phase E Step 5 — Unify the commit path in `regionanalyzer.cpp`

**Date:** 2026-06-09
**Base HEAD:** `90a52b5fee` (bridge forward-lookahead fix)
**Instruction:** `cc_instruction_phase_e_commit_unification` (this task)
**Status:** Complete — proven byte-identical on every test suite *and* the full
353-score corpus in both presets. Not committed (awaiting Cowork confirmation).

---

## Section 1 — Site survey

All three commit sites matched the instruction's description. Line numbers as
found at the start of the task (pre-change):

| Site | Location (pre-change) | Behaviour |
|------|----------------------|-----------|
| **Site 1** — main Pass 1 loop | `regionanalyzer.cpp:473–489` | Calls `advanceTemporalContext(…, chosenResult.identity)`, then sets `nextRootPc/nextBassPc = -1`, then a separate `{…}` confidence block using `gateCtx`. |
| **Site 2** — Pass 2 sub-region loop | `regionanalyzer.cpp:695–710` | **Bypasses** `advanceTemporalContext`: 3-line manual `subCtx.previousRootPc/Quality/BassPc` assignment, followed by an identical confidence block using `subGateCtx`. |
| **Site 3** — Pass 2b sub-region loop | `regionanalyzer.cpp:895–910` | Identical to Site 2 (same bypass, same omission). |

**Confirmation of the documented inconsistency.** Sites 2 and 3 never called
`advanceTemporalContext`, so `consecutiveBassStepwiseCount` and `recentRootPcs`
were *not* advanced across the sub-region sequence. Instead they were seeded
**once per parent**, before the sub-region loop, from the parent's snapshot:

- Pass 2: `regionanalyzer.cpp:587–589` (`subCtx.consecutiveBassStepwiseCount = parentRegion.temporalExtensions.consecutiveBassStepwiseCount; subCtx.recentRootPcs = parentRegion.temporalExtensions.recentRootPcs;`)
- Pass 2b: `regionanalyzer.cpp:796–798` (same two assignments)

So every sub-region in a parent saw the **same frozen** rolling state — exactly
the silent inconsistency the instruction describes.

**`advanceTemporalContext` overloads (`chordanalyzer.h`, pre-change):**

- 6-arg primitive `(ctx, runningStepwiseCount, recentRootsBuf, rootPc, bassPc, quality)` — lines 711–739.
- 4-arg `ChordIdentity` overload — lines 741–749 (delegates to the primitive).
- `PostScoringGateContext` is defined at lines 754–771 — i.e. **after** the
  `ChordIdentity` overload. `RawCandidate` (with `.score`) is defined at line 273.

> **Deviation from the instruction's placement guidance — necessary.** The
> instruction said to place the new overload "immediately after the existing
> `ChordIdentity` overload (~line 741)." That is not compilable: the new
> overload's body dereferences `PostScoringGateContext` members
> (`pcWeight`, `distinctPcs`, `rawCandidates[].score`), and an `inline`
> function body needs the full type, not a forward declaration. The struct is
> only fully defined at lines 754–771. The new overload is therefore placed
> **immediately after the `PostScoringGateContext` definition** (the earliest
> valid point), and the original overload group's doc-comment was extended with
> a forward pointer to it.

---

## Section 2 — Implementation

### `chordanalyzer.h`

**(a)** Extended the doc-comment on the existing overload group (just above the
6-arg primitive) with a paragraph announcing the third overload and its extra
behaviour.

**(b)** Added the new 5-arg overload right after the `PostScoringGateContext`
struct:

```cpp
inline void advanceTemporalContext(
    ChordTemporalContext&         ctx,
    int&                          runningStepwiseCount,
    std::array<int, 3>&           recentRootsBuf,
    const ChordIdentity&          chosen,
    const PostScoringGateContext& gateCtx) noexcept
{
    // Delegate to the existing overload for rolling state + identity fields.
    advanceTemporalContext(ctx, runningStepwiseCount, recentRootsBuf, chosen);

    // Predecessor confidence fields (Step 2 redesign).
    const int winRoot = chosen.rootPc;
    ctx.previousWinnerRootPcWeight = (winRoot >= 0)
        ? gateCtx.pcWeight[static_cast<size_t>(winRoot)] : 0.0;
    ctx.previousDistinctPcs  = gateCtx.distinctPcs;
    ctx.previousWinnerScore  = gateCtx.rawCandidates.empty()
        ? 0.0 : gateCtx.rawCandidates[0].score;
    ctx.previousWinnerMargin = (gateCtx.rawCandidates.size() >= 2)
        ? gateCtx.rawCandidates[0].score - gateCtx.rawCandidates[1].score
        : -1.0;
}
```

The confidence-field arithmetic is copied verbatim from the three inline blocks
it replaces, so the values produced are identical.

### `regionanalyzer.cpp` — before/after (10-line context)

**Site 1 (main loop).** Removed the standalone confidence block; passed
`gateCtx` to the unified call.

```diff
             advanceTemporalContext(temporalCtx, runningStepwiseCount, recentRootsBuf,
-                                   chosenResult.identity);
+                                   chosenResult.identity, gateCtx);
             temporalCtx.nextRootPc = -1;
             temporalCtx.nextBassPc = -1;

-            // Step 2 redesign: populate predecessor confidence fields
-            {
-                const int winRoot = chosenResult.identity.rootPc;
-                temporalCtx.previousWinnerRootPcWeight = (winRoot >= 0)
-                    ? gateCtx.pcWeight[static_cast<size_t>(winRoot)] : 0.0;
-                temporalCtx.previousDistinctPcs = gateCtx.distinctPcs;
-                temporalCtx.previousWinnerScore = gateCtx.rawCandidates.empty()
-                    ? 0.0 : gateCtx.rawCandidates[0].score;
-                temporalCtx.previousWinnerMargin = (gateCtx.rawCandidates.size() >= 2)
-                    ? gateCtx.rawCandidates[0].score - gateCtx.rawCandidates[1].score
-                    : -1.0;
-            }
-
             prevKeyResult = localKey;
```

**Site 2 (Pass 2).** Declared per-parent rolling state before the sub-loop, and
replaced the manual 3-line assignment + confidence block with the unified call.

```diff
             subCtx.consecutiveBassStepwiseCount
                 = parentRegion.temporalExtensions.consecutiveBassStepwiseCount;
             subCtx.recentRootPcs = parentRegion.temporalExtensions.recentRootPcs;

+            // Option A — per-parent rolling state for the unified commit helper.
+            int subRunningStepwiseCount = 0;
+            std::array<int, 3> subRecentRootsBuf = {-1, -1, -1};
+
             for (size_t si = 0; si + 1 < subBounds.size(); ++si) {
```
```diff
-                subCtx.previousRootPc  = chosenSub.identity.rootPc;
-                subCtx.previousQuality = chosenSub.identity.quality;
-                subCtx.previousBassPc  = chosenSub.identity.bassPc;
-
-                // Step 2 redesign: populate predecessor confidence fields (subGateCtx in scope)
-                {
-                    const int winRoot = chosenSub.identity.rootPc;
-                    subCtx.previousWinnerRootPcWeight = (winRoot >= 0)
-                        ? subGateCtx.pcWeight[static_cast<size_t>(winRoot)] : 0.0;
-                    subCtx.previousDistinctPcs = subGateCtx.distinctPcs;
-                    subCtx.previousWinnerScore = subGateCtx.rawCandidates.empty()
-                        ? 0.0 : subGateCtx.rawCandidates[0].score;
-                    subCtx.previousWinnerMargin = (subGateCtx.rawCandidates.size() >= 2)
-                        ? subGateCtx.rawCandidates[0].score - subGateCtx.rawCandidates[1].score
-                        : -1.0;
-                }
+                advanceTemporalContext(subCtx, subRunningStepwiseCount, subRecentRootsBuf,
+                                       chosenSub.identity, subGateCtx);
```

**Site 3 (Pass 2b).** Identical pattern to Site 2 (declaration after the
`796–798` seeding block; commit block replaced with the unified call).

**Diffstat:**
```
 src/composing/analysis/chord/chordanalyzer.h     | 36 +++++++++++++
 src/composing/analysis/region/regionanalyzer.cpp | 65 +++++++-----------------
 2 files changed, 55 insertions(+), 46 deletions(-)
```

No other files touched. No scoring term (template / bonus / gate / guard) was
added or modified, so the `docs/scoring_model.md` sync rule does **not** apply to
this commit (it is a pure structural refactor of a commit helper in the header).

---

## Section 3 — Rolling state (Option A)

**Where declared.** `int subRunningStepwiseCount = 0;` and
`std::array<int, 3> subRecentRootsBuf = {-1, -1, -1};` are declared **inside the
per-parent block, before the sub-region loop** at both sites:
- Pass 2: post-change `regionanalyzer.cpp:582–583`
- Pass 2b: post-change `regionanalyzer.cpp:784–785`

They are *not* seeded from parent state — initialised to `0` / `{-1,-1,-1}` per
the instruction (no silent adjustment to force byte-identity). The pre-existing
per-parent seeding of `subCtx.consecutiveBassStepwiseCount` / `recentRootPcs`
(587–589 / 796–798) was **kept**, so the first sub-region (si = 0) still reads the
parent-inherited values and is unchanged.

**Did any sub-region's `consecutiveBassStepwiseCount` / `recentRootPcs` change
value?** Yes — for the **second and later** sub-regions (si ≥ 1) of any
multi-sub parent. This is a real, intended consequence of Option A:

- **Old behaviour:** `subCtx.consecutiveBassStepwiseCount` and `recentRootPcs`
  were set once (from the parent) and then **frozen** for every sub-region in
  that parent — they were never advanced.
- **New behaviour:** after each sub-region commits, `advanceTemporalContext`
  overwrites them from the per-parent rolling state, which starts at
  `0` / `{-1,-1,-1}` and accumulates within the sub-sequence. So si ≥ 1 now
  receives a *different* (correctly rolled-forward) value than the parent's
  frozen one.

**Did that change any output?** No. These two fields are read only by the
narrow enharmonic-flip gates in `chordanalyzer.cpp` — Gates C/D (Major-add6 →
Minor first-inversion), G-C/G-D (HalfDiminished), H-C/H-D (Augmented
root-symmetry) — every one of which additionally requires a specific winner
quality (Major+add6 / HalfDim / Augmented) and a stepwise-bass signal. Across the
whole corpus, none of the altered rolling-state values flipped a gate decision.
This is **directly measured**, not assumed:

- **0 / 353** `.ours.json` differ in the Baroque corpus (A/B diff, below).
- **0 / 353** `.ours.json` differ in the Jazz corpus.
- **0** pipeline-snapshot diffs (10-score notation corpus).

So Option A is the architecturally-correct behaviour (sub-regions now maintain
their own rolling state), and on the current corpus it leaves every selected
chord unchanged. The change is byte-identical at the *output* level while
deliberately *not* a no-op on intermediate `subCtx` state.

---

## Section 4 — Test results (my-change binary)

| Suite | Result |
|-------|--------|
| `composing_tests.exe` | **416 / 416** passed |
| `notation_tests.exe` | **52 / 52** passed |
| `pipeline_snapshot_tests.exe` | **11 / 11** passed, **0 diffs** (1 always-skipped `PipelineDivergenceCObservation.GenerateReport`) |

No goldens were updated (none drifted). Build was clean (exit 0; only the two
pre-existing `C4100` unreferenced-parameter warnings in `chordanalyzer.cpp`,
unrelated to this change).

---

## Section 5 — BIR check (proven via A/B against a freshly-built baseline)

Because Option A is explicitly allowed to drift, I did not rely on the stale
on-disk corpus. I ran a full A/B: stashed the change, rebuilt the **baseline**
(`90a52b5fee`) binary, regenerated both corpora, then restored the change,
rebuilt, regenerated, and diffed the `.ours.json` directly.

| Metric | Baseline (HEAD) | My-change | Δ |
|--------|-----------------|-----------|---|
| Baroque `characterise_bir_false.py` BIR=false | 13 | **13** | 0 |
| Baroque `analyze_inversion_errors.py` (3-way bassIsRoot) | 24 / 13 | **24 / 13** | 0 |
| Jazz `characterise_bir_false.py` BIR=false | 7 | **7** | 0 |
| Baroque corpus `.ours.json` differing files | — | **0 / 353** | byte-identical |
| Jazz corpus `.ours.json` differing files | — | **0 / 353** | byte-identical |

Headline baselines (Baroque **24/13**, Jazz **35/7**) are unchanged. Neither
BIR=false increased.

**Two notes on Task 6's metric citation (for the record):**

1. Task 6 instructed running `analyze_inversion_errors.py` and expecting
   "Baroque = 13, Jazz = 7." Those numbers are the **`characterise_bir_false.py`**
   headline (lenient-OR `align_regions`), not `analyze_inversion_errors.py`, which
   reports a *different* music21∩DCML bassIsRoot three-way split (here 24/13).
   I ran **both** scripts and report both; they are identical between baseline and
   my-change, which is what matters.
2. The session memory note recorded `analyze_inversion_errors.py` ≈ **27/22** "at
   HEAD `638ced1c12`." At the current HEAD (`90a52b5fee`) the same script reports
   **24/13** on a freshly-regenerated corpus — confirmed on the *baseline* binary,
   so the shift predates this change and is **not** a regression from it (the
   note is simply stale for the newer HEAD; the batch path is unaffected by the
   intervening bridge fix, but the metric evidently moved across earlier work).
   That stale note motivated the A/B above; the A/B settles it conclusively.

---

## Section 6 — Commit recommendation

All test suites pass, all output is byte-identical, and both BIR baselines are
unchanged. The change is a clean structural improvement: a single canonical
commit helper, and Sites 2/3 no longer silently skip rolling-state advancement.

Recommended commit message (do **not** commit until Cowork confirms):

```
refactor: unify chord-commit path in regionanalyzer.cpp (Phase E Step 5)

Route every chord commitment — main Pass 1 loop, Pass 2 sub-regions, Pass 2b
sub-regions — through a single advanceTemporalContext overload that also
populates the Step-2 predecessor-confidence fields. Removes three copies of an
inline confidence block and the two manual identity assignments in the
sub-region loops that bypassed advanceTemporalContext entirely.

New overload in chordanalyzer.h:
  advanceTemporalContext(ctx, runningStepwiseCount, recentRootsBuf,
                         chosen, gateCtx)
delegates to the ChordIdentity overload (rolling state + identity) and then
fills previousWinnerScore / previousWinnerMargin / previousWinnerRootPcWeight /
previousDistinctPcs from the captured PostScoringGateContext. Placed after the
PostScoringGateContext definition (its body needs the full type).

Option A per-parent rolling state: each sub-region loop declares its own
subRunningStepwiseCount / subRecentRootsBuf, so sub-regions now advance
consecutiveBassStepwiseCount / recentRootPcs within their own sequence instead
of leaving them frozen at the parent's inherited value. This changes the
intermediate value seen by si>=1 sub-regions but flips no gate decision:
byte-identical output across both corpora.

Behaviour-preserving — proven:
  composing 416/416, notation 52/52, pipeline snapshots 11/11 (0 diffs)
  Baroque corpus 0/353 .ours.json differ; BIR 24/13 unchanged
  Jazz    corpus 0/353 .ours.json differ; BIR 35/7  unchanged

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>
```

No `docs/scoring_model.md` update required (no scoring term added/modified).
