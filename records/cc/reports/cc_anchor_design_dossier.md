# cc_anchor_design_dossier.md — ANCHOR (architecture fix): read-only design investigation

**Status:** READ-ONLY design + measurement plan. No code/behavior/inference change. HEAD = `dd418ecfed` (confirmed via `git rev-parse`). The user ratifies the design before any implementation.

**Scope of the defect (restated):** the chord is finalized mid-pipeline, before its region's tones are final, against a key that is baked into the score before the joint re-key — a one-shot pipeline with no fixpoint. North star: move root/chord output *toward* the DCML/music21 oracle.

---

## §2 verdict — the decisive question: **HYBRID (not a clean A, not a forced B)**

> Does segmentation CONSUME the chord result, or only the tones?

**Answer, with source evidence:** the two axes split cleanly and oppositely, so a single A/B label would be wrong. The honest verdict is:

- **Where to SPLIT (boundary *detection*) — chord-INDEPENDENT (World A).** The detectors take raw score features only; they never see a `ChordAnalysisResult`.
- **Where to MERGE (same-chord *collapse* / coalesce) — chord-DEPENDENT (World B-flavored).** The collapse steps read `chordResult.identity.rootPc`/`quality` to decide whether to fold a freshly-split region back into its predecessor.

So the **boundaries** are a feed-forward function of tones (re-orderable), but the **final partition** is additionally reduced by chord-identity-dependent merges, and — this is the actual bug — when a merge fires the **root/quality are not recomputed against the combined tones.**

### Evidence — SPLIT detectors do NOT consume the chord

| Detector | File:line | Signature (no `ChordAnalysisResult`) | Splits on |
|---|---|---|---|
| `detectOnsetSubBoundaries` (Pass-2) | [regiontoneprimitives.cpp:200-289](src/composing/analysis/engravingbridge/regiontoneprimitives.cpp#L200-L289) | `(sc, startTick, endTick, excludeStaves, threshold)` | per-onset PC bitsets → Jaccard distance ≥ threshold + min-gap. Raw `Note::ppitch()` only. |
| `detectBassMovementSubBoundaries` (Pass-2b) | [regiontoneprimitives.cpp:291-370](src/composing/analysis/engravingbridge/regiontoneprimitives.cpp#L291-L370) | `(sc, startTick, endTick, excludeStaves, minGapTicks)` | lowest-pitch bass-PC change + min-gap. Raw pitch only. |
| `absorbShortRegions` (Pass-3) | [regionanalyzer.cpp:196-213](src/composing/analysis/region/regionanalyzer.cpp#L196-L213) | `(regions)` | region **duration < kMinRegionTicks** only — never reads the chord. |
| Pass-1 coarse boundaries | [regionanalyzer.cpp:605-608](src/composing/analysis/region/regionanalyzer.cpp#L605-L608) | iterates `boundaryTicks` | boundary ticks computed before any `analyzeChord` call. |

### Evidence — MERGE/COLLAPSE steps DO consume the chord identity

| Step | File:line | Reads | Used to decide |
|---|---|---|---|
| `tryCollapseSameChordRegion` | [regionanalyzer.cpp:166-186](src/composing/analysis/region/regionanalyzer.cpp#L166-L186) | `regions.back().chordResult.identity.rootPc` & `.quality` vs `candidate.identity.{rootPc,quality}` (lines 174-176) | merge the new region into the predecessor iff **same root AND same quality** (and contiguous). On merge: extends endTick, **merges tones, recomputes ONLY bass** — root/quality kept from predecessor. |
| — called at Pass-1 main loop | [regionanalyzer.cpp:725](src/composing/analysis/region/regionanalyzer.cpp#L725) | (above) | coarse same-chord collapse |
| — called at Pass-2 site | [regionanalyzer.cpp:928](src/composing/analysis/region/regionanalyzer.cpp#L928) | (above) | onset-split same-chord collapse |
| `coalesceShortSameRootRuns` | [regionanalyzer.cpp:73-152](src/composing/analysis/region/regionanalyzer.cpp#L73-L152) | `regions[i].chordResult.identity.rootPc` (lines 89, 96, 106) | coalesce a run of short sub-regions sharing one root; merges tones, recomputes ONLY bass (140-143) |
| — called at Pass-3 | [regionanalyzer.cpp:1144](src/composing/analysis/region/regionanalyzer.cpp#L1144) | (above) | short-run coalesce |

(Note: Pass-2b builds sub-regions but does **not** call `tryCollapseSameChordRegion` — its same-root reduction is deferred to Pass-3 `coalesceShortSameRootRuns`. Confirmed: `tryCollapseSameChordRegion` has exactly two call-sites, 725 and 928.)

**The defect localized:** both merge paths merge tones and recompute **only the bass** ([regionanalyzer.cpp:179-184](src/composing/analysis/region/regionanalyzer.cpp#L179-L184) and [:140-143](src/composing/analysis/region/regionanalyzer.cpp#L140-L143)). Root/quality/extensions are inherited from one pre-merge slice and never re-derived from the union of tones. This is the "chord finalized before its region's tones are final" half of the anchor.

---

## §1/§3.1 — Data-flow map (tones → boundaries+chord → tone mutation → key)

```
collectRegionTones (raw score)                         [chord-free]
        │
Pass-1  ├─ denseBoundaryTicks → coarse regions          [chord-free split]
        │   per region: resolveKeyAndModeRanked(prevKey hysteresis)  → localKey   (regionanalyzer.cpp:626-629)
        │   analyzeChord(tones, localKeyFifths, localKeyMode, …)     → R0         (:661)
        │   tryCollapseSameChordRegion(... R0.identity ...)          [chord-DEP merge] (:725)
        │
Pass-2  ├─ detectOnsetSubBoundaries(score, …)           [chord-free split]   (:764)
        │   sub key = parentRegion.keyModeResult (INHERITED, not re-resolved) (:778-779)
        │   analyzeChord(subTones, subKey, …)                                  (:877)
        │   tryCollapseSameChordRegion(... chosenSub.identity ...)  [chord-DEP merge] (:928)
        │
Pass-2b ├─ detectBassMovementSubBoundaries(score, …)    [chord-free split]   (:970)
        │   sub key = parentRegion.keyModeResult (INHERITED)                   (:987-988)
        │   analyzeChord(subTones, subKey, …)                                  (:1073)
        │   (no inline collapse; builds sub-regions)
        │
Pass-3  ├─ coalesceShortSameRootRuns   [chord-DEP merge; tones mutated, ONLY bass recomputed] (:1144)
        └─ absorbShortRegions          [duration-only merge; tones extended, NOTHING recomputed] (:1145)
        │
        restampBassMinorSeventhAfterMerge (:1149)  — partial post-merge fixup (bass-b7 only)
        backfillNextRootPc (:1152)
        │
Joint   └─ applyJointKeyWiring (default OFF)  — KEY-ONLY, decideJointKey ONCE, chord NOT re-emitted (:1159-1162)
```

What consumes each `analyzeChord` output:
- **Pass-1 R0** ([:661](src/composing/analysis/region/regionanalyzer.cpp#L661)): consumed by `tryCollapseSameChordRegion` (merge decision), stored on the region, and later fed to `applyJointKeyWiring` as `ji.rootPc/quality/chordAlts`.
- **Pass-2 chosenSub** ([:877](src/composing/analysis/region/regionanalyzer.cpp#L877)): consumed by `tryCollapseSameChordRegion` (:928), stored on the sub-region.
- **Pass-2b chosenSub** ([:1073](src/composing/analysis/region/regionanalyzer.cpp#L1073)): stored on the sub-region; its identity later read by `coalesceShortSameRootRuns`.

---

## §3.2 — The key-freeze seam

**Finding: the key is ALREADY an explicit parameter of `analyzeChord`. There is no "thread the key explicitly" plumbing sub-step left to do — it is done.**

- Signature: `analyzeChord(tones, int keySignatureFifths, KeySigMode keyMode, …)` — [chordanalyzer.h:822-829](src/composing/analysis/chord/chordanalyzer.h#L822-L829).
- Pass-1 passes the per-region resolved `localKeyFifths/localKeyMode` ([:661-662](src/composing/analysis/region/regionanalyzer.cpp#L661-L662)); `localKey` comes from `kr::resolveKeyAndModeRanked(... prevKeyResult ...)` with hysteresis ([:626-631](src/composing/analysis/region/regionanalyzer.cpp#L626-L631)) — resolved **before** the chord, per coarse region.
- Pass-2/2b sub-regions **inherit the parent region's key** (`parentRegion.keyModeResult`), they do not re-resolve — [:778-779](src/composing/analysis/region/regionanalyzer.cpp#L778-L779), [:987-988](src/composing/analysis/region/regionanalyzer.cpp#L987-L988).

Where the key is "frozen into the chord": inside `analyzeChord`, the key is baked into `cell.basisIndep` at scoring time via `dim7CharacteristicBonus(... keyTonicPc, scale ...)` + `diatonicRootContribution(rootPc, keyTonicPc, scale, …)` — [chordanalyzer.cpp:1293-1299](src/composing/analysis/chord/chordanalyzer.cpp#L1293-L1299), assigned to the cell at [:1413](src/composing/analysis/chord/chordanalyzer.cpp#L1413). The comment at [:1434-1440](src/composing/analysis/chord/chordanalyzer.cpp#L1434-L1440) confirms key influence does NOT flow through the function context — it is *already* in the oracle score. So "the key" is honoured the instant `analyzeChord` is called; the freeze is purely a question of **which key value and which tone set** were current at that call.

The joint re-key seam: `applyJointKeyWiring` ([regionanalyzer.cpp:351-478](src/composing/analysis/region/regionanalyzer.cpp#L351-L478)) runs once after Pass-3, calls `decideJointKey` **ONCE** ([:444](src/composing/analysis/region/regionanalyzer.cpp#L444)), and **deliberately leaves the chord as R0** ([:343-348](src/composing/analysis/region/regionanalyzer.cpp#L343-L348), [:476](src/composing/analysis/region/regionanalyzer.cpp#L476)). The in-source rationale (≈6% same-key root-flip noise from naive re-emission) is itself evidence for *why* a principled fixpoint is needed rather than a blind re-emit. Default OFF ([:1159](src/composing/analysis/region/regionanalyzer.cpp#L1159)).

**Net key seam:** there is no missing key parameter. The behavior change arrives only when a **different** value is passed — i.e. (a) the chord recomputed against the **final/merged** tone set, and/or (b) the **joint** key instead of the Pass-1 local key.

---

## §3.3 — Design options

### Option A — clean feed-forward re-order (split-first, chord-once)
1. Run **all** tone/onset/bass splitting first (coarse + onset + bass) → a maximal partition `P_max`. All three detectors are already chord-free, so this is a pure lift.
2. Compute the chord **once per final cell**, against that cell's final tones + explicit key.

**Blocker:** the *same-chord collapse* (`tryCollapseSameChordRegion`, `coalesceShortSameRootRuns`) is what currently turns `P_max` into the final partition, and it reads the chord. You cannot collapse before you have chords. So a *pure* A is impossible — the final partition is not a chord-free function of tones.

### Option B — iterative fixpoint (constrained joint)
compute chord → segment/collapse → recompute chord on merged tones → re-collapse → until stable. Honest, but heavier, and most of the partition is already chord-stable, so a full fixpoint over the whole pipeline is more machinery than the defect needs.

### ★ Recommended — **A′: split-first + collapse-then-recompute, with a bounded settle** (a tight hybrid)
1. **Split phase (chord-free, World A):** run coarse + `detectOnsetSubBoundaries` + `detectBassMovementSubBoundaries` to produce `P_max` and each cell's final tones. Pure re-order of existing chord-free code.
2. **Chord phase:** `analyzeChord` once per `P_max` cell (explicit key).
3. **Collapse phase:** merge adjacent equal-(root,quality) cells (`tryCollapse*` / `coalesce*` logic, unchanged predicate).
4. **★ The fix — recompute the merged cell's chord against the *combined* tones** (today: only bass is recomputed). This closes the "tones final before chord" gap.
5. **Bounded settle:** because step 4 can in principle change a merged cell's identity (added tones tip a quality), repeat 3-4 until no further merge fires, capped at a small N (collapse only ever merges *already-equal* chords, so convergence is fast and monotone-ish — measure the actual iteration count; expectation is 1, occasionally 2).

This is feed-forward for the expensive split, with a *local, bounded* fixpoint only over the cheap collapse/recompute — the minimum machinery the §2 hybrid actually requires.

**Seams / signatures that change:** none of the detectors. The change is in the orchestration body of `RegionAnalyzer::analyze` (the Pass-1/2/2b/3 sequence in [regionanalyzer.cpp](src/composing/analysis/region/regionanalyzer.cpp)) and in the two merge helpers (`tryCollapseSameChordRegion`, `coalesceShortSameRootRuns`) which gain a "recompute chord on merged tones" step. The merge helpers would need access to the `IChordAnalyzer` + key to recompute — a new parameter on those two functions.

### ★ Byte-identical plumbing sub-step that can land first (principle 1)
The smallest correct architectural step is **step 4 as a guarded no-op extension of the existing merge**:
- Add a "recompute root/quality/extensions on the merged tones" call inside `tryCollapseSameChordRegion` / `coalesceShortSameRootRuns`, but **only adopt the recomputed identity when the merged tone-set differs from the slice the surviving chord was computed against.** When no merge changed the tones (the vast majority of regions), the recompute is a no-op and output is **byte-identical**.
- This isolates the first behavior movement to *exactly the merged regions*, which is precisely the population the anchor targets, and makes the snapshot/BIR diff small and inspectable.
- The full split-first re-order (steps 1-2) can land as a *separate, independently byte-identical* refactor (it only changes the order in which chord-free boundaries are computed; if the union of boundaries is identical, output is identical — this must be **verified**, see risks).

> Re the key axis: there is **no** byte-identical key-plumbing sub-step to land, because the key parameter already exists. The joint-key behavior change is a distinct, later step (re-emit the chord under the joint key with the same recompute mechanism), gated by `jointKeyWiringEnabled()`, and should be sequenced **after** the tone-recompute fix is validated — the source already records that a naive re-emit injected more noise than signal.

---

## §3.4 — Measurement plan (CORRECT, not just different)

**Expected output movement & why:** only **merged** regions (same-chord collapse + short-run coalesce + short-region absorb) can change, because only their tone-set differs from what the surviving chord was scored against. Unmerged regions are untouched. The movement is the root/quality re-derivation on the union of tones — expected to *correct* cases where the surviving slice was a partial/embellishment reading and the union is the true held harmony (the 37.7%/~38-42% held-harmony residual the anchor targets).

**Correctness vs the oracle (the gate that matters):**
- Metric: root/chord agreement vs DCML (authoritative) corroborated by music21, measured on the Baroque + Jazz corpora via the canonical tools (`run_bach_preset.py` per-preset dir → `characterise_bir_false.py`; secondary `analyze_inversion_errors.py`). Per CLAUDE.md, DCML is ground truth; music21 only corroborates.
- Before/after: capture per-preset root-error / BIR=false **case-identity sets** at HEAD, then after the change. The change must move identities **out** of the error set (toward the oracle), net, with no new actionable errors masked by symmetric-dim7 churn.
- Report at **both** batch-region and `--section-level` (per-beat) granularity — CLAUDE.md notes the per-beat rate is ~7× the batch rate; a held-harmony fix should help the per-beat view most.

**BIR gate (hard):** Baroque **57** / Jazz **23** / Default **57** case-identity sets must HOLD or improve on all three presets. Any BIR=false increase in any preset is a hard stop. Run the full two-preset corpus protocol from CLAUDE.md before any commit.

**Snapshots:** `pipeline_snapshot_tests` goldens WILL move (expected, on the merged regions). Plan: run → redirect to file (VS Code stall rules) → inspect **each** golden diff → verify each is correct vs the oracle → only then `--update-goldens` → re-run to confirm. Never update blind. Also run `composing_tests.exe` and `notation_tests.exe` (both must pass).

---

## §5 / risks / unknowns / stop-points

1. **Split-first equivalence is an assumption to verify, not a given.** Today the onset/bass detectors run on *sub-spans already cut by the previous pass* (Pass-2b runs inside each Pass-2 region). Running them on coarse regions to build one `P_max` must produce the **same union of boundary ticks**. The min-gap (`minGapTicks`) and `lastBoundaryTick` state are computed *relative to the current span's start* ([regiontoneprimitives.cpp:268](src/composing/analysis/engravingbridge/regiontoneprimitives.cpp#L268), [:356](src/composing/analysis/engravingbridge/regiontoneprimitives.cpp#L356)) — so re-spanning **can** change which boundaries clear the gap. This is the single biggest re-order risk; the byte-identical claim for steps 1-2 must be empirically proven (boundary-tick A/B), not assumed. **If it cannot be made byte-identical, land step 4 (the recompute) alone first and defer the re-order.**
2. **Key inheritance interacts with merges.** Sub-regions inherit the parent's key; if the re-order changes parentage, the key fed to a recomputed chord can change. Keep the recompute on the *merged region's own* resolved/inherited key to avoid coupling the two axes in one step.
3. **Settle-loop convergence is unmeasured.** Recompute-after-merge could oscillate in principle. Cap N small, log the observed max iteration count, and treat >2 as a signal to investigate rather than raise the cap.
4. **Cannot be measured read-only:** the actual oracle movement, the snapshot diff set, and the real settle-iteration count — all require the (ratified) build + corpus run.
5. **`restampBassMinorSeventhAfterMerge`** ([:1149](src/composing/analysis/region/regionanalyzer.cpp#L1149)) is a partial pre-existing post-merge fixup (bass-b7 only). A general recompute (step 4) likely **subsumes** it — verify and remove to avoid double-stamping, but only after confirming equivalence.
6. **Out-of-pipeline stop-point (per §5):** the design touches only chord/region/key orchestration + the two merge helpers. It does **not** require touching the catalog/ground-truth, scoring templates, or anything outside `src/composing/`. If implementation appears to need a template/gate change, that is a separate scoring task under the CLAUDE.md scoring-doc rules — STOP and surface.

**HEAD unchanged (`dd418ecfed`); no code, behavior, or inference modified. Awaiting user ratification of Option A′ (and of the byte-identical-recompute-first sub-step) before any implementation.**
