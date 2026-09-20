# Step 2 — De-duplicate the inline same-chord merge predicate (S1)

**Type:** PURE, BYTE-IDENTICAL structural refactor. No inference / scoring / threshold / boundary change.
**Base:** committed on top of `8bc1441076` (step 1, shared pc primitives — Cowork-verified byte-identical).
**Scope:** `src/composing/analysis/region/regionanalyzer.cpp` only. Diff: 44 insertions / 35 deletions, 1 file.

## What was done

The two inline **same-root / same-quality region-collapse** sites in `regionanalyzer.cpp` carried an
identical predicate + merge body (with explicit "DUPLICATED … keep in sync" comments). They are now a single
file-local helper, called from both sites.

### Site count: confirmed **2**, not 3
`grep mergeChordAnalysisTones` in the file returns exactly three hits:
- `:138` — inside `coalesceShortSameRootRuns` (Pass 3 length-gated coalesce) — **OUT OF SCOPE**, untouched.
- `:702` (Pass-1 main loop) and `:915` (Pass-2) — the two duplicated collapse sites that were extracted.

Pass-2b (the iterative bass-movement loop) has **no** same-chord collapse site (no `mergeChordAnalysisTones`
hit in its body) — so the duplication is across exactly two sites, matching the source comments
("keep in sync with the Pass 2 site" / "with the main-loop site"). No third site, no else-branch difference
deeper than `keyModeResult`.

### The helper (anonymous namespace, file-local — NOT in analysisutils.h)

Placed in the existing `namespace { … }` block, immediately after `coalesceShortSameRootRuns`:

```cpp
bool tryCollapseSameChordRegion(std::vector<HarmonicRegion>& regions,
                                const ChordAnalysisResult& candidate,
                                int newStartTick,
                                int newEndTick,
                                const std::vector<ChordAnalysisTone>& newTones)
{
    const bool isContiguousWithPreviousRegion = !regions.empty()
                                            && regions.back().endTick == newStartTick;
    if (!(isContiguousWithPreviousRegion
          && regions.back().chordResult.identity.rootPc == candidate.identity.rootPc
          && regions.back().chordResult.identity.quality == candidate.identity.quality)) {
        return false;
    }
    regions.back().endTick = newEndTick;
    mergeChordAnalysisTones(regions.back().tones, newTones);
    if (const auto* bassTone = bassToneFromTones(regions.back().tones)) {
        regions.back().chordResult.identity.bassPc  = bassTone->pitch % 12;
        regions.back().chordResult.identity.bassTpc = bassTone->tpc;
    }
    return true;
}
```

It takes the **vector by reference** (not `back()`), the candidate `ChordAnalysisResult`, the new region's
start/end tick, and the new tones. Returns `true` if it merged the candidate into the back region (caller
skips its region-construction branch), `false` otherwise (caller runs its existing branch unchanged).

### The two rewritten call-sites (each keeps its own region-construction branch)

Pass-1:
```cpp
if (!tryCollapseSameChordRegion(regions, chosenResult,
                                regionStart.ticks(), regionEnd.ticks(), tones)) {
    HarmonicRegion region;            // unchanged construction (sets keyModeResult = localKey, …)
    …
    regions.push_back(std::move(region));
}
```

Pass-2:
```cpp
if (!tryCollapseSameChordRegion(pass2Regions, chosenSub,
                                subStart.ticks(), subEnd.ticks(), subTones)) {
    HarmonicRegion subRegion;         // unchanged construction (sets keyModeResult = parentRegion.keyModeResult, …)
    …
    pass2Regions.push_back(std::move(subRegion));
}
```

Both else-branches (now the `if(!…)` bodies) are character-identical to the originals — the differing region
construction was left at each call-site, as required.

## Byte-identity argument

1. **Predicate identical.** Both originals computed `!vec.empty() && vec.back().endTick == newStart`, then
   `&& back.rootPc == cand.rootPc && back.quality == cand.quality`. The helper computes exactly this, in the
   same order.

2. **★ Empty-vector short-circuit preserved (the one real hazard).** The originals rely on `&&` short-circuit
   so `vec.back()` is never evaluated when the vector is empty (the `!empty()` term comes first). The helper
   takes the **vector** and computes `!regions.empty() && regions.back().endTick == newStartTick` **inside**,
   so when the vector is empty `isContiguousWithPreviousRegion` is `false` and the subsequent
   `isContiguousWithPreviousRegion && regions.back().chordResult…` again short-circuits before any `back()`
   access. No reference to `back()` is bound at the call site (the helper takes the vector, never a
   `HarmonicRegion&` to `back()`), so there is no UB on the empty first-region path of either pass — it falls
   to `return false`, and the caller builds the first region, exactly as today.

3. **Merge body character-identical.** Both sites did: `back().endTick = newEnd;`
   `mergeChordAnalysisTones(back().tones, newTones);` then, iff `bassToneFromTones` is non-null,
   `back().chordResult.identity.bassPc = bt->pitch % 12; …bassTpc = bt->tpc;`. The two originals differed only
   in local variable names (`bassTone` vs `bt`) — the helper reproduces the body verbatim.

4. **Tones move semantics unchanged.** In both originals the merge path passed `tones`/`subTones` to
   `mergeChordAnalysisTones` **by const ref** (no move) and only the region-construction branch `std::move`d
   them. The helper takes `const std::vector<ChordAnalysisTone>&` (no move); the caller's construction branch
   still `std::move`s on the no-merge path. Identical.

5. **Removed locals were single-use.** `isContiguousWithPreviousRegion` (Pass-1) and `isContiguous` (Pass-2)
   were each used only at their own `if` — verified by grep. Folding their computation into the helper changes
   nothing observable.

## §4 byte-identity gate results

| Gate | Result |
|---|---|
| Clean build (unity) | ✅ 7/7 targets linked, no warnings on the changed TU |
| `composing_tests` | ✅ **545/545** |
| `notation_tests` | ✅ **57/57** |
| `pipeline_snapshot_tests` (NO `--update-goldens`) | ✅ **11/11**, zero golden diff (1 skipped = pre-existing `GenerateReport`) |
| BIR `.ours.json` byte-diff vs reference corpora, all 3 presets | ✅ **0 / 353** diffs (Baroque, Jazz, Default) |
| BIR genuine case count | ✅ Baroque **57** / Jazz **23** / Default **57** (matches documented gate) |

**BIR verification method.** The reference per-preset corpora (`tools/corpus/{baroque,jazz,default}`, stamped
`git_hash 41f7c65f63` — an earlier link in the same byte-identical refactor chain that produced step-1
`8bc1441076`) were left intact. Each preset was regenerated into a fresh sibling dir
(`…_step2`) via `run_bach_preset.py` (music21 ground-truth is **copied** from `tools/corpus/`, only
`batch_analyze` `.ours.json` is re-emitted), then every one of the 353 `.ours.json` was `cmp`'d against the
reference: **0 byte-diffs in all three presets**. `characterise_bir_false.py` on the regenerated dirs
reproduced 57 / 23 / 57. Scratch `…_step2` dirs were removed after verification.

## Conventions / docs
- No scoring term touched → no `docs/scoring_model.md` sync required.
- The two "DUPLICATED … keep in sync" source comments were replaced with short comments pointing at the shared
  helper (doc-only; the `docs/implementation_roadmap.md 0.6` reference is preserved).

## Conclusion
The extraction is byte-identical by construction and verified at every gate (tests, snapshots, and full-corpus
`.ours.json` byte comparison across all three presets). The merge logic now lives in one place — the in-file
precondition for step 3 — with no behavior change. Committed locally on top of `8bc1441076`; **not pushed**.
