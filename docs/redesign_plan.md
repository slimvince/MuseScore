# Redesign Plan — Deferred Commitment and Richer Inter-Layer Context

*Written 2026-06-08. Authors: Cowork + CC architectural session.*

---

## The core principle

Every inference layer in the pipeline should pass its **full evidence** forward alongside
its committed decision — not compress that evidence into the decision alone. Downstream
layers need to know not just what the upstream layer decided, but how confident that
decision was and what the raw evidence looked like. Without this, a wrong upstream
commitment is passed forward as if it were ground truth, and every layer below it
inherits the error.

We call the anti-pattern **"passing a lie"**: a wrong answer committed at layer N
receives the same weight as a correct one when consumed at layer N+1, because the
confidence signal that would have flagged it as uncertain was discarded at commit time.

---

## What E2d already achieves

The E2d redesign (commit `2917ec7571`) established the **oracle / competition pipeline**
separation:

- `analyzeChord()` — pure **scoring oracle**. Computes all (bass, root, template) cells
  with vertical-only scores. Packs them into a `fn::ScoringSnapshot`. Applies no
  progression signal and selects no winner.
- `fn::applyHarmonicFunction()` — **competition pipeline**. Receives the full snapshot,
  applies progression signals (rootContinuity, wSeq, wDim, step bonuses), runs the
  cross-bass competition, and **then** commits to a winner.

This means **within-region deferred commitment is already implemented**. The commitment
point (winner selection) happens after functional signals are applied, not before. The
architecture is more advanced than it may appear from the Phase E roadmap description.

**Evidence in code:**
- `chordanalyzer.cpp:2883–2947`: oracle builds `ScoringSnapshot`, constructs `fnCtx`,
  calls `fn::applyHarmonicFunction(snapshot, fnCtx, prefs, results, chosenResult, gateCtx)`
- `harmonicfunctionlayer.cpp:182–328`: full competition pipeline — progression signals
  applied at Pass A, winner selected before `results[]` is built

---

## The gap: the inter-region channel is thin

After `applyHarmonicFunction` selects a winner, `advanceTemporalContext`
(`chordanalyzer.h:717–720`) writes the committed identity into the temporal context:

```cpp
ctx.previousRootPc  = chosenRootPc;
ctx.previousBassPc  = chosenBassPc;
ctx.previousQuality = chosenQuality;
```

That committed identity is then forwarded to the next region's competition pipeline via
`fnCtx` construction (`chordanalyzer.cpp:2931–2937`):

```cpp
fn::HarmonicFunctionContext fnCtx;
fnCtx.previousRootPc = context ? context->previousRootPc : -1;
fnCtx.nextRootPc     = context ? context->nextRootPc     : -1;
fnCtx.previousBassPc = context ? context->previousBassPc : -1;
fnCtx.nextBassPc     = context ? context->nextBassPc     : -1;
```

**What is NOT forwarded:** winner score, winner margin over runner-up, predecessor
root PC weight, predecessor distinctPcs — none of the signals that would let the next
region calibrate how much to trust the predecessor's commitment.

The result: `rootContinuityBonus` in `harmonicfunctionlayer.cpp:206–207` applies a flat
`prefs.rootContinuityBonus` (+0.40 for Baroque) regardless of predecessor confidence:

```cpp
const double rcb = rootContinuityBonus(cell.rootPc, ctx.previousRootPc,
                                        prefs.rootContinuityBonus);
```

A wrong predecessor commitment receives the same +0.40 reward as a correct one. This
is the "pass a lie" mechanism behind the entire Δ=+7 rootContinuityBonus failure cluster
(bwv102.7, bwv245.28, bwv261, bwv296, bwv320 — 5 Baroque BIR=false residuals).

---

## The wiring gap: existing context not forwarded

`ChordTemporalContext` already carries richer context that is computed but **not
forwarded** to `HarmonicFunctionContext`:

| Field | In ChordTemporalContext | In HarmonicFunctionContext |
|---|---|---|
| `previousRootPc` | ✅ | ✅ |
| `previousBassPc` | ✅ | ✅ |
| `previousQuality` | ✅ | ❌ |
| `recentRootPcs[3]` | ✅ | ❌ |
| `consecutiveBassStepwiseCount` | ✅ | ❌ |
| `regionMetricWeight` | ✅ | ❌ |
| winner score | ❌ | ❌ |
| winner margin | ❌ | ❌ |
| predecessor root pcWeight | ❌ | ❌ |

Some enrichment is **free** — the first four missing fields are already computed, just
not plugged into `fnCtx`. Forwarding them requires no new computation, only wiring.

---

## The key layer gap

`resolveKeyAndModeRanked` produces a **ranked distribution** of key candidates:

- `regionanalyzer.cpp:305–308` (initial key):
  ```cpp
  const auto initialRanked = kr::resolveKeyAndModeRanked(...);
  int keyFifths = initialRanked.front().keySignatureFifths;  // distribution discarded
  ```
- `regionanalyzer.cpp:411–416` (per-region key):
  ```cpp
  const auto ranked = kr::resolveKeyAndModeRanked(...);
  const KeyModeAnalysisResult localKey = ranked.front();    // distribution discarded
  ```

The function name says "Ranked" — it was designed to support distribution-based key
selection. But the ranked list is discarded immediately in both call sites.

Every downstream consumer of `localKeyFifths` and `localKeyMode` (template scoring,
scale construction, diatonic root bonus, pitchClassName) receives a single committed
key as if it were ground truth. A wrong key poisons every scale-consuming term for the
entire piece.

> **Caveat (2026-06-08):** the motivating example originally cited here — Corelli
> op01n08d detected as G minor — is **no longer a live failure**. It was a
> signature-lock bug fixed by `81978321e3` (Option B partial-signature correction),
> not a distribution gap; the resolver now returns C minor confidently at rank 0
> everywhere. The architectural observation (the ranked list is discarded) still
> stands, but **no current failing case is known to exhibit "correct key sits at
> rank 1/2"**, which is the pattern key-as-distribution would actually address. See
> `cc_step3_key_investigation_report.md`.

This is the **same early-commitment disease** as the inter-region channel, one layer up
— and it is architecturally worse because there is no distribution being maintained at
all between the key detection layer and the chord analysis layer.

---

## Failure case analysis — what deferred commitment fixes

*(Updated 2026-06-08 after predecessor-confidence diagnostic — `cc_deltaseven_predecessor_report.md`.)*

| Case | Failure | Root cause | Does richer inter-region context fix it? |
|---|---|---|---|
| Δ=+7a bwv102.7, bwv261 | Wrong root wins on vertical evidence (`contFired=0`) | Oracle scoring issue — not a context problem | No — vertical investigation needed |
| Δ=+7b bwv245.28, bwv296, bwv320 | Correct predecessor; bonus tips near-tie wrong | Oracle tie, bonus is sole tiebreaker | No — Phase E voice-leading resolution signal needed |
| bwv301 G-absent winner | G major wins because G's 3rd+5th present; root G absent | Vertical scoring asymmetry in oracle | No — remains. Absent-root guard addresses symptom |
| B1 mMaj7 leading-tone | {0,3,7,11} fires in V→i contexts | Commitment-before-resolution-signal | Partially — needs voice-leading resolution (Phase E) |
| B3 dim7 rotation | Rotation-selection via non-diatonic ♭♭7 check | PC-identical rotations — no distribution helps | No — unchanged |
| bwv14.5 sub-region | 240-tick bass-transition sub-region overrides parent | Segmentation / sub-region tick boundary | No — segmentation issue |
| A2 dominant quality in minor | 1-PC slice gets wrong quality | Key commits before chord; no feedback | Partially (key distribution would help) |
| Corelli op01n08d key | ~~G minor instead of C minor throughout~~ — **already fixed** by `81978321e3` (Option B partial-signature correction); resolver returns C minor at rank 0 everywhere (verified 2026-06-08) | ~~Key layer commits with no distribution~~ — was a signature-lock bug, not a distribution gap | **N/A — no longer a failure.** Key-as-distribution has no effect here |

**The Δ=+7 cluster is Phase E territory.** The predecessor-confidence framing was wrong:
the 3 genuine continuity cases (bwv245.28, bwv296, bwv320) have *correct, confident*
predecessors (pcWeight 0.60–0.82). The failing regions are near-ties in the oracle, with
rootContinuityBonus as the sole tiebreaker. The discriminating signal — V6 resolving
upward vs. the old root lingering — requires voice-leading context not available until
Phase E. The predecessor-confidence scaling approach (Step 2 below) was falsified and
will not fix these cases.

---

## Redesign sequence

These steps are ordered by cost and impact. Each step is independently verifiable and
does not require the next step to be started first.

### Step 1 — Forward existing ChordTemporalContext fields (free wiring) ✅ DONE

**Commit:** `a6d289c461` (2026-06-08) — chordanalyzer.cpp +5, harmonicfunctionlayer.h +11.
Byte-identical verified: 407/407, 52/52, 11/11 pipeline snapshots, 0 goldens changed.

**Cost:** Small. Struct extension + `fnCtx` construction change. No new computation.
**Impact:** `applyHarmonicFunction` now receives `previousQuality`, `recentRootPcs[3]`,
`consecutiveBassStepwiseCount`, `regionMetricWeight`. No scoring logic uses them yet —
this is the foundation for Phase E quality-aware signals.
**Files:** `harmonicfunctionlayer.h` (struct), `chordanalyzer.cpp` (fnCtx construction)

### Step 2 — Add predecessor confidence to the inter-region channel ✅ DONE

**Commit:** `c8afd0e23c` (2026-06-08) — byte-identical, 407/407, 52/52, 11/11 snapshots.

**Cost:** Medium. New fields in `ChordTemporalContext` populated during
`advanceTemporalContext`; forwarded to `HarmonicFunctionContext`.

New fields:
- `previousWinnerScore` (double) — winner's competition score
- `previousWinnerMargin` (double) — gap between winner and runner-up (within-bass group)
- `previousWinnerRootPcWeight` (double) — predecessor winner's root PC weight
- `previousDistinctPcs` (int) — how many distinct PCs were in the predecessor region

**Revised scope (2026-06-08):** The original target for Step 2 was dissolving the Δ=+7
cluster by scaling `rootContinuityBonus` on predecessor confidence. That hypothesis was
falsified by the predecessor-confidence diagnostic. The Δ=+7 cases split into:
- 2 cases (bwv102.7, bwv261): wrong root wins vertically before the bonus fires —
  not a context problem at all.
- 3 cases (bwv245.28, bwv296, bwv320): predecessors are *correct* confident triads
  (pcWeight 0.60–0.82). The mozart_k280 control predecessor has pcWeight 1.00. No
  threshold can block the wrong cases without blocking the correct ones.

**What Step 2 was:** Infrastructure. `previousWinnerScore`, `previousWinnerMargin`,
`previousWinnerRootPcWeight`, `previousDistinctPcs` added to both `ChordTemporalContext`
and `HarmonicFunctionContext`. Populated at the main call site and at two sub-region
commit blocks (Pass-2 and Pass-2b in `regionanalyzer.cpp`), which use inline 3-line
manual assignments rather than the `advanceTemporalContext` helper. Both had
`PostScoringGateContext` in scope; scores are pre-gate (competition pipeline output).
No scoring logic reads these fields yet — foundation for Phase E.

**Do not implement rootContinuityBonus scaling in Step 2** until a specific mechanism
survives a falsification test against mozart_k280. CC's proposed bass-aware gate
(`bassPc ≠ rootPc AND bassPc ≠ previousBassPc`) is an Iter 98 echo — that inversion-
aware approach was explicitly tried and hit the same mozart regression. The extra
`bassPc ≠ previousBassPc` condition does not save it (Alberti bass moves between
chord positions on every beat, so the condition fires correctly and incorrectly alike).

**Files:** `chordanalyzer.h` (ChordTemporalContext), `harmonicfunctionlayer.h`
(HarmonicFunctionContext), `chordanalyzer.cpp` (advanceTemporalContext + fnCtx)

### Step 3 — Key-as-distribution ⛔ SHELVED (premise obsolete)

**Investigation date:** 2026-06-08. Report: `cc_step3_key_investigation_report.md`.

The motivating case (Corelli op01n08d: "G minor instead of C minor throughout") was
**already fixed** by commit `81978321e3` (Option B Baroque partial-signature correction,
2026-06-03). The key resolver now returns C minor at rank 0 for every region on both
batch and notation paths. Step 3 has no confirmed live target in the corpus.

Two additional findings from the investigation:

- **`fnCtx.keyFifths` / `fnCtx.keyMode` are dead (write-only).** Set in
  `chordanalyzer.cpp` L2932-2933, never read in `harmonicfunctionlayer.cpp`. The
  key influence travels via `snapshot.{scale, keyTonicPc}` which is frozen into
  `cell.basisIndep` before the function layer runs. These fields should be removed or
  documented as dead.

- **`normalizedConfidence` is unreliable as a scaling factor.** `promoteWinnerInPlace`
  in `keyresolver.cpp` (L311-321) re-ranks candidates via hysteresis/declared-mode
  without recomputing `normalizedConfidence`, producing a 0.025–1.00 range for the
  same correctly-keyed piece. The "minimum viable form" (scale diatonic bonus by key
  confidence) would have throttled the diatonic bonus to ~3% on correctly-keyed scores
  — a regression, not an improvement.

**Step 3 is shelved until a live case is confirmed** where the correct key genuinely
appears as a runner-up in `resolveKeyAndModeRanked` output. No such case is known in
the current 51-piece Baroque corpus.

**Cleanup required (CC, follow-on to Option 2):**
- Remove or document `fnCtx.keyFifths`/`fnCtx.keyMode` dead fields
- Mark `key_detection_baroque_partial_signature.md` as resolved-by-`81978321e3`

Full form: run the chord competition twice (once per top-2 key candidates), merge the
result distributions. Only warranted if Step 2 proves insufficient for key-driven errors.

**Target:** Corelli op01n08d and related key-detection failures.

**Files:** `regionanalyzer.cpp` (key resolution), `harmonicfunctionlayer.h`/`.cpp`
(key-confidence parameter), `chordanalyzer.cpp` (key-dependent terms)

### Step 4 — Full progression context (Phase E proper)

Previous/next region quality, cadence evidence, phrase-level context.
Unblocks B1 (MinorMajor7), A2 (dominant in minor), and the Δ=+7 remainder that
Step 2 doesn't dissolve.

This is the original Phase E plan. Steps 1–3 are prerequisites that are now better
understood as preconditions, not alternatives.

---

## What NOT to do first

- **Do not retry the absent-root guard.** It was implemented 2026-06-08 and caused a net
  regression: 2 fixed (bwv301, bwv269), 4 broken (bwv227.1, bwv342 are DCML-correct absent-root
  readings; 2 further cascade regressions from `previousRootPc` propagation). The cascade problem
  is structural: any guard that changes a committed root changes `previousRootPc` for all
  downstream regions, triggering `rootContinuityBonus` changes across 6 snapshot goldens. The
  premise "absent root ⇒ wrong reading" is false corpus-wide. **The guard was reverted entirely.**
  The correct next coding task is **Step 1 (free wiring)** from the redesign sequence above.

- **Do not implement rootContinuityBonus scaling** (as a Δ=+7 fix) before a mechanism
  survives the mozart_k280 falsification test. The predecessor-confidence approach was
  falsified. CC's "bass-aware gate" variant is an Iter 98 echo and faces the same
  mozart regression (Alberti bass always has `bassPc ≠ previousBassPc`).

- **Do not widen existing thresholds** to accommodate individual failure cases. Each threshold
  was calibrated against the Baroque corpus; widening one to fix one case typically breaks
  two others. The Iter 98 experience is the canonical example.

---

## Reference: key files

| File | Relevance |
|---|---|
| `src/composing/analysis/chord/chordanalyzer.h` | `ChordTemporalContext` (L570), `advanceTemporalContext` (L692) |
| `src/composing/analysis/chord/chordanalyzer.cpp` | `fnCtx` construction (L2931), `fn::applyHarmonicFunction` call (L2947) |
| `src/composing/analysis/function/harmonicfunctionlayer.h` | `HarmonicFunctionContext` (L59), `ScoringSnapshot` (L163), `rootContinuityBonus` signature (L93) |
| `src/composing/analysis/function/harmonicfunctionlayer.cpp` | `rootContinuityBonus` use (L206), competition pipeline (L182–328) |
| `src/composing/analysis/region/regionanalyzer.cpp` | `resolveKeyAndModeRanked + .front()` (L305, L411), `advanceTemporalContext` call (L473) |
| `docs/scoring_model.md` | Scoring model reference — §11 for oracle/pipeline split |
