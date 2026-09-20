# CC Phase-2 Architecture Support — empirical confirm/correct of the five data-flow claims

> **READ-ONLY. No source/inference/behavior change. Findings only.** CC empirical half of phase 2
> (`docs/layer_audit_plan.md` §5, Cowork-led). For each of the five claims the phase-2 verdict rests on,
> below is **CONFIRM or CORRECT** at the committed object with source `file:line`, a measured share where one
> exists, and a one-line structural implication. North star: BEST = CORRECT vs the DCML/music21 oracle.
> Cowork folds this into the phase-2 verdict; user ratifies. **No fixes proposed or implemented.**

Base: working tree at HEAD `a03c2493bb`. All citations are fresh source reads.

---

## Claim 1 — `regionanalyzer` Pass structure + the 37.7% over-segmentation attribution

**Structure: CONFIRMED. The 37.7%→*segmentation-specifically* attribution: CORRECTED (it's split across boundary-creation AND a length-gated merge, and the number is a soft proxy, not a measured over-segmentation count).**

### Pass structure — CONFIRMED, four passes
`src/composing/analysis/region/regionanalyzer.cpp`:
- **Pass 1** (forward loop, ~`:497`–`:728`; `analyzeChord` at `:627`) — analyzes each coarse boundary region from `greedyExpandSegmentation()` / `denseBoundaryTicks()` into the region stream.
- **Pass 2** (`:730`–`:936`; `detectOnsetSubBoundaries` at `:745`, `analyzeChord` at `:858`) — onset-Jaccard sub-boundary splitting within each Pass-1 region.
- **Pass 2b** (`:938`–`:1127`; `detectBassMovementSubBoundaries` at `:961`, `analyzeChord` at `:1064`; iterative, `kMaxBassMovementPasses=8` at `:60`) — bass-PC-movement sub-boundary splitting.
- **Pass 3** (`:1133`–`:1137`) — merge-only: `coalesceShortSameRootRuns()` (`:73`) + `absorbShortRegions()` (`:162`). Smoothed granularity only.

### "Keep in sync" triplication — CONFIRMED
The same-root/same-quality **inline merge predicate** is duplicated with explicit "keep in sync" comments:
- Pass-1 site, comment `:692`–`:696` ("DUPLICATED region-collapse logic — keep in sync with the Pass 2 site below … Not extracted … because the two else-branches build different HarmonicRegion shapes"), merge body `:698`–`:706`.
- Pass-2/2b site, comment `:907`, merge body `:911`–`:919`.

This inline merge is **distinct** from Pass-3's two merge functions — so there are effectively **three** same-root-collapse mechanisms: the triplicated inline predicate (`rootPc`+`quality`, contiguous) and Pass-3's two length-gated ones (`coalesceShortSameRootRuns`, `absorbShortRegions`).

### Where boundaries are decided — BOTH (CONFIRMED, "or both")
- **Initial coarse boundaries:** `harmonicsegmenter.cpp greedyExpandSegmentation` (Round 1 anchors `:683`–`:755`, Round 2 gap-fill `:757`–`:787`). regionanalyzer Pass 1 consumes these (`:520`–`:521`).
- **Sub-boundaries (the over-segmentation source):** created *inside* regionanalyzer — Pass 2 (`detectOnsetSubBoundaries`) and Pass 2b (`detectBassMovementSubBoundaries`). These split a coarse region into finer ones.
- **Merge-back:** the inline same-root collapse (Pass 1/2/2b) + Pass-3 (`coalesceShortSameRootRuns`, `absorbShortRegions`).

So segmentation granularity is decided by **two cooperating layers**: `harmonicsegmenter` sets the coarse grid; `regionanalyzer` Pass-2/2b refine it and Pass-3/inline-merge coarsen it back.

### The 37.7% — CORRECTED on attribution and on certainty
Origin: `cc_audit_harmonicfunctionlayer_report.md:82` — HELD bucket = "WiR root == our prev- **or** next-region root" = 811 cases = 37.7% of the 2153 `all_differ` regions, labeled "segmentation (over-segmentation; S1/S2)."

Two corrections:
1. **It is a proxy, not a measured over-segmentation count.** The bucket criterion (our region's root equals a *neighbor's* root) catches genuine over-segmentation **and** cases where our root is simply wrong but coincidentally matches a neighbor. The audit itself flags the boundary as soft: `cc_functional_residual_dossier.md` buckets the same mass as **NHT_HELD = 906 = 42.1%** and states "the B1↔B3 boundary inside NHT_HELD / the over-segmentation slice is the softest split." Honest statement: **~38–42% of the functional residual is a held-harmony / over-segmentation bucket, with a soft attribution boundary** — not a hard 37.7% measured over-segmentation rate.
2. **It is NOT cleanly "segmentation (boundary creation)" vs "merge/Pass-3" — it is OWNED BY BOTH.** A HELD case = two adjacent regions DCML reads as one harmony. That survives to the output only because the **merge machinery failed to coalesce them**, and the merge is **length/identity-gated**: `absorbShortRegions` merges only `< kMinRegionTicks` (`:172`); `coalesceShortSameRootRuns` fires only for runs of `≥3` short same-root sub-regions totalling `≥720` ticks (`:123`–`:126`); the inline collapse requires same `rootPc` **and** same `quality` (`:698`–`:706`/`:911`–`:919`). Two *long* same-root regions, or two same-root regions of *differing quality/inversion*, are split by Pass-2/2b and **never merged back**. So the residual is jointly produced by boundary-creation (Pass-2/2b) **and** an over-conservative merge.

**Structural implication.** **S1 (de-dup the triplicated inline predicate) and the segmentation-correctness lever are TWO fixes, but S1 is the enabling precondition for the second.** S1 is a pure code-dedup (extract the merge predicate to one helper — can be byte-identical). The over-segmentation *correctness* fix is behavior-changing and lives partly in Pass-2/2b boundary creation and partly in the merge gating — and it should be made **after** S1 so the merge logic exists in one place, not three. (Per the §6 sequencing gate: structural-first, so S1 lands before any merge-behavior change.)

---

## Claim 2 — chord-identity ≠ final-region (post-chord pass mutates region tones)

**CONFIRMED, and the exact seam is located. The code itself documents that this broke re-emission.**

Order of operations in `regionanalyzer.cpp`:
1. Tones collected (regiontonecollector), per region.
2. Chord computed: `analyzeChord` at Pass-1 `:627`, Pass-2 `:858`, Pass-2b `:1064` — chord is emitted **mid-pipeline**, against the tones present at that pass.
3. **Pass-3 `coalesceShortSameRootRuns` (`:73`) mutates region membership AFTER the chord exists:** it picks the longest sub-region as the survivor, then `mergeChordAnalysisTones(combined.tones, regions[k].tones)` at `:138` folds the other sub-regions' tones in, and recomputes **only** `bassPc`/`bassTpc` (`:140`–`:143`). `rootPc`/`quality`/`extensions` are **not** recomputed. `absorbShortRegions` (`:162`) similarly extends `endTick` (`:173`) absorbing a neighbor's span without recomputing the chord.

So the final region's `chordResult` is **not a clean function of its final tone set** — it was computed from a subset, with only the bass patched.

**The code explicitly confirms the re-emission breakage** at `:309`–`:316` (the J-key-iii joint-re-key pass):
> "The CHORD is left as the production chord R0 (NOT re-emitted): a faithful per-region chord re-emission under the joint key cannot reproduce the multi-pass pipeline chord (the production chord is emitted **mid-pipeline, before Pass-3 tone merging**; … measured ~6% same-key root-flip noise, i.e. the re-emission injected more artifact than genuine key-driven movement)."

**Structural implication.** This is a real **feed-forward ordering defect**: the chord is finalized before its region is. The re-layering target is to compute the chord **once, against final region tones** (segmentation → final tones → chord), which would also be the precondition that lets J-key-iii actually re-emit the chord under the joint key instead of freezing R0. Exact seam to fix: `coalesceShortSameRootRuns` `:133`–`:143` and `absorbShortRegions` `:170`–`:177` (the post-chord membership mutations), plus the Pass-1/2/2b inline merges that update only bass.

---

## Claim 3 — the post-scoring gate cluster = compensation, not a layer

**CONFIRMED (dominantly compensation), with a useful CORRECTION: 2 sub-gates are purely-local vertical refinements that would survive a joint formulation; 3 are hybrid; B/C/D are dead code.**

`postscoringgates.cpp`, classified by what each gate **reads**:

| Gate | file:line | Inputs read | Class |
|---|---|---|---|
| A (Maj-add6 ↔ m7 enharmonic) | `:160` | extensions/quality of the winner only | **LOCAL (survives joint)** |
| E (1st-inv minor→major) | `:213` | cross-region bass-stepwise + preferred mode | compensation |
| F (2nd-inv) | `:235` | cross-region bass-stepwise | compensation |
| G-E / G-B / G-C / G-D (m-add6 ↔ ø7) | `:339`/`:353`/`:363`/`:376` | key tonic+degree (G-E); next-root, recentRootPcs[], consecutiveBassStepwiseCount | compensation |
| H / H-B / H-C / H-D (augmented) | `:402`/`:420`/`:428`/`:436` | cross-region context required; next-root, recentRootPcs[], bass-stepwise count | compensation |
| I (1st-inv major vs minor) | `:445` | key tonic + `scale[]` diatonic check **+** local bass + score margin | hybrid (key) |
| J (inverted dom-7) | `:550` | only current-region `pcWeight[]` chord-tone completeness | **LOCAL (survives joint)** |
| K (1st-inv aug vs root) | `:480` | key tonic + `scale[]` **+** local bass + margin | hybrid (key) |
| L (same-root major vs aug) | `:516` | key tonic + `scale[]` **+** local root/bass/ext + margin | hybrid (key) |
| B, C, D | `:204`–`:210` | **REMOVED (Stage 3.4b) — unreachable; Gate A always pre-empts** | dead |

`chordpostpasses.cpp` (Iter-86/91 pedal, `:119`–`:295`) reads cross-region/pedal context → compensation. `sparsechordrefinement.cpp` (`:106`–`:217`) reads the **key** to relabel sparse chords → compensation (key-axis; see Claim 4).

**Tally of the live gates (12 reachable): 10 read cross-region and/or key context = compensation; 2 (A, J) are purely-local vertical = would survive a joint formulation.** Of the 10, the cross-region readers (E/F/G-B/G-C/G-D/H*) compensate for **cross-region non-jointness**; the key readers (G-E, I, K, L, + sparsechordrefinement) compensate for **chord↔key non-jointness** (Claim 4). Both classes are the dissolution target.

**Structural implication.** The gate cluster is **~83% compensation** for the two non-jointnesses; a constrained-joint formulation (chord + neighbors + key resolved together) would dissolve those 10. **Only Gate A and Gate J are genuine local vertical refinements** that must be **preserved** through the dissolution — they are not compensation and should not be deleted with the rest. CORRECTION to a blanket "the whole cluster is compensation": it is not — name the 2 survivors.

---

## Claim 4 — the chord↔key circularity, exact leak points

**CONFIRMED, and EXTENDED. The two named oracle leaks are real; sparsechordrefinement reads the key in four functions; there are additional key-reads in `buildChordResult` and four gates. The oracle leak is documented in-source as "frozen into basisIndep."**

Inside the vertical oracle (`chordanalyzer.cpp`):
1. **`diatonicRootContribution`** (`:801`) — takes `keyTonicPc` + `scale[]`; awards `diatonicRootBonus` if the candidate root is in the key scale. Ambiguous-root tiebreak. Called at `:1299`.
2. **`dim7CharacteristicBonus`** (`:452`) — takes `keyTonicPc` + `scale[]`; the **symmetric-dim7 rotation-selector** — awards the bonus only to the rotation whose bb7 is **non-diatonic**, thereby *defining* the dim7 root by reading the key. Called at `:1296`; mechanism documented `:1283`–`:1289`.
3. Both consume the key computed at `analyzeChord` `:1220`–`:1235`, and `:1436`–`:1437` explicitly states the key influence "is frozen into `cell.basisIndep` … via the oracle's `dim7CharacteristicBonus` and `diatonicRootContribution`." **→ the key leaks into the chord score BEFORE the competition runs.**

`sparsechordrefinement.cpp` reads the key in **four** functions (broader than "reads the key" once):
- `diatonicDegreeForRootPc` (`:106`), `refineSparseChordQualityFromKeyContext` (`:119`, degree at `:133`, writes `keyTonicPc`/`keyMode` at `:139`–`:141`), `applyTonicPriorToSparseChord` (`:168`), `forceChordTrackQualityFromKeyContext` (`:203`) — each reads `keyFifths`+`keyMode` to relabel an under-specified chord to the diatonic triad shape.

**Additional key-reads inside the chord path (not in Cowork's list — surfaced):**
- `buildChordResult` (`chordanalyzer.cpp` ~`:896`–`:923`) — degree assignment + a diatonic-ness check over `ctx.scale`/`keyTonicPc`.
- post-scoring Gates **G-E** (`:343`), **I** (`:465`), **K** (`:504`), **L** (`:538`) all read `keyTonicPc`/`scale[]` (see Claim 3).

**Structural implication.** The chord↔key circularity is **larger than two leak points**: it is (oracle ×2, frozen into basisIndep) + (buildChordResult degree/diatonic check) + (sparsechordrefinement ×4) + (4 post-scoring gates). The key is consumed at **every stage of the chord path** — pre-competition score, result-build, post-gates, and sparse refinement. Breaking the circularity is therefore not "remove two terms" but **re-architect the chord oracle to take the key as an explicit joint variable** (the `architecture_joint_inference.md` target), since the dependency is pervasive and currently one-directional-but-frozen (key→chord, with chord→key happening separately upstream).

---

## Claim 5 — the duplicated key-collection / pitch-class primitive

**CONFIRMED that pc/collection primitives are re-implemented across the four named layers. CORRECTED on "one primitive copy-pasted": it is two distinct families — trivial pc helpers (truly identical) + collection-mask builders in TWO genuinely-different variants. Duplication is intentional (unity-build ODR), documented in-source.**

Functions found:
- `cadencekeyanchor.cpp`: `pcMod12` (`:34`), `pcInMask` (`:40`), `diatonicMaskFromFifths` (`:50`) — **signature-derived** mask.
- `localmodulationdetector.cpp`: `lmdPcMod12` (`:71`), `lmdCollectionMask` (`:81`), `lmdRootIsDiatonic` (`:100`), `lmdOutOfCollectionCount` (`:106`) — **local-key (tonic+mode)** collection.
- `jointkeydecision.cpp`: `jkdPcMod12` (`:38`), `jkdCollectionMask` (`:48`, comment says "identical to … `lmdCollectionMask`"), `jkdInCollectionFraction` (`:67`), `jkdRootDiatonic` (`:83`) — local-key collection (same family as lmd).
- `tonicizationlabeler.cpp`: `pcMod12` (`:36`), `pcInMask` (`:42`), `diatonicMaskFromFifths` (`:53`, identical to cadencekeyanchor's), `keyScale` (`:68`) — **signature-derived** mask + an ordered 7-degree scale builder unique to this file.

Two families:
- **Truly identical (copy-paste):** `pcMod12` in all four; `pcInMask` in cadencekeyanchor + tonicizationlabeler; `diatonicMaskFromFifths` in cadencekeyanchor + tonicizationlabeler.
- **Genuinely distinct variants:** the **signature-derived** mask (cadencekeyanchor, tonicizationlabeler — key-agnostic, from `fifths`) vs the **local-key tonic+mode** collection (localmodulationdetector, jointkeydecision — major vs harmonic-minor scale degrees). These are *different computations* serving different layers; not the same primitive.

The duplication is **intentional and documented**: each file explains the `lmd*`/`jkd*` prefix / named-detail-namespace is to avoid an ODR clash in the unity/jumbo build (localmodulationdetector `:68`–`:74`; jointkeydecision `:34`–`:37`; tonicizationlabeler `:29`–`:32`). No shared pc-utility header exists — `analysis/chord/analysisutils.h` holds only `ionianTonicPcFromFifths`/`normalizePc`.

**Structural implication.** "Extract one shared primitive" is a **real but compound** obligation: a shared `composing/analysis/pitchclassutils.h` would dissolve the trivial-helper duplication (`pcMod12`, `pcInMask`) and the signature-mask duplication immediately (and remove the ODR-prefix workaround). The **local-key collection** is a *second* primitive (tonic+mode), used by lmd + jkd — extract it once too, but it is not the same function as the signature mask. So: **2–3 shared functions to extract, not 1** — and the extraction is byte-identical/structural, safe to do early.

---

## Sixth cross-layer issue (surfaced while tracing) — the frozen feed-forward seam blocks the joint target

Claims 2 and 4 **compose into a single deeper structural defect** the five claims don't name on their own:

The chord is finalized **before** its region's tones are final (Claim 2: chord at `:627`/`:858`/`:1064`, tones mutated at Pass-3 `:138`), **and** the chord oracle's key dependency is **frozen into `basisIndep` pre-competition** (Claim 4: `:1436`–`:1437`). When the joint re-key pass (`applyJointKeyWiring`, `:317`) wants to re-resolve the key per *final* region, it **cannot re-emit the chord** — documented at `:309`–`:316` — because (a) the final region tones differ from what the chord saw, and (b) the key→chord influence is frozen upstream and not re-runnable. The result is a **one-shot, frozen-forward pipeline** (segment → chord(key₀, partial-tones) → merge → key₁) with **no fixpoint** — the exact opposite of the `architecture_joint_inference.md` constrained-joint target.

**Implication:** the re-layering precondition for *both* the gate-dissolution (Claim 3) and the joint-key work is the **same** one: compute the chord **once against final region tones with the key as an explicit input**, so chord and key can be jointly (re-)resolved. Claims 2 + 4 are not two independent seams — they are one ordering defect that makes the joint formulation impossible today. This is the highest-leverage structural obligation and should anchor the phase-2 obligation order.

---

## Confirm/correct summary

| # | Claim | Verdict |
|---|---|---|
| 1 | Pass-1/2/2b/3 + triplication + boundaries | **Structure CONFIRMED**; 37.7%→segmentation **CORRECTED** (soft proxy ~38–42%; owned by boundary-creation AND length-gated merge; S1 ≠ correctness-lever but is its precondition) |
| 2 | post-chord pass mutates region tones | **CONFIRMED** (seam: `coalesceShortSameRootRuns` `:138`, `absorbShortRegions` `:173`; re-emission breakage documented `:309`–`:316`) |
| 3 | gate cluster = compensation | **CONFIRMED ~83%**; **CORRECTED** — Gates A and J are local vertical, survive joint; B/C/D dead |
| 4 | chord↔key circularity = 2 leaks + sparse | **CONFIRMED + EXTENDED** — oracle ×2 (frozen into basisIndep) + buildChordResult + sparsechordrefinement ×4 + 4 gates; pervasive, not 2 |
| 5 | one pc primitive across 4 layers | **CONFIRMED duplication**; **CORRECTED** — two families (trivial helpers identical; collection masks in 2 distinct variants); intentional/ODR; extract 2–3 fns not 1 |
| 6 | (new) frozen feed-forward seam | Claims 2+4 compose into one ordering defect that blocks the joint target — the anchor obligation |

*CC, 2026-06-17. READ-ONLY; no production/inference/behavior change; HEAD `a03c2493bb` unchanged. Cowork folds into the phase-2 verdict; user ratifies.*
