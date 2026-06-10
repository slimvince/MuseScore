# Redesign Plan — Layered Comprehensive Evidence Architecture

*Written 2026-06-08. Updated 2026-06-09 (comprehensive evidence flow; iteration language dropped).
Updated 2026-06-10 (architecture-review addendum: lattice + global decode named as the Phase E target — see final section).*
*Authors: Cowork + CC architectural session.*

---

## The architecture decision (revised 2026-06-09)

Harmonic analysis has layers with clean separation of concerns. The architectural
principle is: every layer should pass its **full evidence** forward alongside its
committed decision — confidence signals, raw scores, ranked alternatives — not just
the committed winner. Downstream layers must be able to calibrate how much weight to
give upstream decisions.

**Iteration is not a design premise.** An earlier framing of this plan ("circular
dependencies require iteration between layers") was an overreach:

- For the current BIR=false failures (rcb cascades, segmentation): all evidence is
  already present at analysis time. The pipeline fails because it discards confidence
  signals at layer boundaries. A single comprehensive pass with symmetric
  forward/backward scoring addresses these.
- For NHT handling: the apparent circularity ("need chord to classify NHT, but chord
  scoring affected by NHT presence") dissolves when metric position and duration serve
  as proxies for structural importance. These signals don't require knowing the chord
  identity first.

Iteration is not ruled out as a fallback for edge cases where evidence genuinely isn't
available until after an initial pass. But it is not a design premise and should not be
built speculatively.

**The operative gap is the inter-region channel.** After `applyHarmonicFunction` selects
a winner, the committed identity passes forward as ground truth; confidence and raw
evidence are discarded. Every downstream region inherits upstream mistakes without any
signal that they were uncertain. Steps 1 and 2 begin wiring this channel; Phase E
completes it.

**Accumulating gates are a warning sign, not a solution.** When a feedforward layer
acquires many gates to compensate for missing upstream evidence, the correct response is
to enrich the evidence flow — not add another gate.

---

## The core principle (still valid)

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

*(Updated 2026-06-08 after predecessor-confidence diagnostic; Δ=+7a framing corrected
2026-06-09 after full per-cell oracle dump — `cc_deltaseven_7a_diagnostic_report.md`.)*

| Case | Failure | Root cause | Does richer inter-region context fix it? |
|---|---|---|---|
| Δ=+7a bwv102.7, bwv261 | Oracle CORRECT in present-root slices (AbMaj7 2.55 > 2.33; F#7 2.85 > 2.83). Failure: arpeggiated harmony split across sub-regions; DCML root absent in committed slice; `rootContinuityBonus` cascades wrong root forward | Segmentation + rcb cascade — not an oracle bug | Phase D (arpeggio-aware tone collection) + Phase E (functional context breaks cascade) |
| Δ=+7b bwv245.28, bwv296, bwv320 | Correct predecessor; bonus tips near-tie wrong | Oracle tie, bonus is sole tiebreaker | ✅ Fixed by Gate R (`638ced1c12`) — `basisDep ≤ 0` guard withholds rcb |
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
- 2 cases (bwv102.7, bwv261): premise was wrong — these are segmentation + rcb cascade
  failures, not oracle bugs. In present-root slices the oracle already prefers the DCML
  root. Fix is Phase D + Phase E. See `cc_deltaseven_7a_diagnostic_report.md`.
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

### Step 4 — Phase D: Rhythmic-window tone aggregation (NHT handling)

*(Design discussion 2026-06-09; mechanism investigation 2026-06-09 via
`cc_phase_d_investigation_report.md`. Window-boundary decision finalised below.)*

#### The NHT ↔ chord circularity

The current system uses **Approach B**: infer a chord for every greedy-expand region
(each contiguous span of identical sounding notes), then retroactively filter anomalous
identities caused by passing notes. Weakness: the filter operates on committed chord
identities. If the wrong chord wins in an arpeggio-partial region, `rootContinuityBonus`
cascades that wrong identity forward into the structurally important neighbouring region
— exactly the Δ=+7a mechanism.

**Approach A** — identify structurally important notes first, then infer chords — is
circular: you need the chord identity to classify a note as passing vs. structural.

The resolution is **duration-weighted aggregation over a rhythmically meaningful window**
that is wide enough to include all arpeggio positions before analysis runs.

#### Δ=+7a mechanism confirmed (2026-06-09)

The `cc_phase_d_investigation_report.md` resolved the exact mechanism. The DCML root
is **temporally in the future** relative to the failing slice, not a sustained note
that the backward walk misses:

| Case | Failing slice start | DCML root attacks | Gap |
|------|--------------------|--------------------|-----|
| bwv102.7 (AbMaj7, root Ab = pc 8) | t17520 | t17760 | 240 ticks |
| bwv261 (F#7, root F# = pc 6)      | t33840 | t34080 | 240 ticks |

The arpeggio sequences these chords such that the root note attacks one arpeggio step
(240 ticks = one quarter note at 480 ticks/beat) AFTER the greedy-expand region that
commits the wrong root. No backward walk can collect a note that hasn't started. Any
fix must widen the analysis WINDOW FORWARD, not the backward-walk lookback.

The 240-tick micro-regions come from the **initial greedy-expand** (Pass 2): each time
the set of simultaneously sounding notes changes, a new region boundary is created. An
arpeggio that moves through C→Eb→Ab→... creates one 240-tick region per arpeggio step.
`detectBassMovementSubBoundaries` (Pass 2b) is not involved here — it has
`minGapTicks = 960` (2 beats) specifically to avoid this kind of micro-split.

`coalesceShortSameRootRuns` (`regionanalyzer.cpp`) cannot rescue these because the
sub-regions have *different* oracle-identified roots (the oracle is correct given the
incomplete tone set it sees). Same-root coalescing requires identical root identity
across the run, which can't happen before the DCML root has even attacked.

**CC's aggregated tone set for bwv102.7 (full arpeggio span):**
`{Eb: 720 ticks, G: 720 ticks, Ab: 480 ticks, C: 480 ticks, D: 240 ticks, Bb: 240 ticks}`
→ Ab is the lowest-pitch note; with Ab as bass and all four AbMaj7 chord tones present,
the oracle correctly identifies AbMaj7 on the aggregate.

**bwv261 note:** Even with full aggregation, the F#7 vs. C#m/F# vertical margin is 0.025
(F#7 raw score 2.85 vs. C#m/F# 2.825). Aggregation may narrow the margin further (F#
gains full-weight presence), but bwv261 likely also needs Phase E (V7→I functional
confirmation) for a decisive fix.

#### Dead end: `noteEnd <= startTickInt` → `noteEnd < startTickInt` (do not retry)

*(Recorded 2026-06-09.)*

`collectRegionTones` excludes backward-walk notes where `noteEnd <= startTickInt` —
notes that end exactly at the sub-region start tick are skipped. The hypothesis was:
arpeggio notes ending at the sub-boundary are excluded, making the DCML root absent.

**Falsified.** The boundary-touching predecessors are OTHER chord tones (C, Eb for
bwv102.7; G, B for bwv261), not the root. The root attacks later. Changing the
condition to `< startTickInt` would add C/Eb or G/B to the failing slice but would
not add Ab or F#. Furthermore, the backward walk exists in 12 call sites (including
5 notation-display paths); the parent-scope calls correctly use `<= startTickInt` to
exclude the previous chord's terminal notes. Do not retry this fix.

#### Dead end: short-region merger trigger (do not retry)

*(Recorded 2026-06-09 after Part A spot-check — `cc_phase_d_merger_report.md`.)*

The approved Phase D design specified a new pass that merges adjacent regions where
`duration < 480 ticks AND distinctPcs ≤ 2 AND run length ≥ 2`. The spot-check found
**0 qualifying runs** across all 13 Baroque BIR=false scores, including both Δ=+7a
targets. The trigger was dead code.

Why: the existing same-root-quality inline merge inside `runPass1` (lines 510–518,
`regionanalyzer.cpp`) already fires on the 240-tick arpeggio micro-regions and combines
them — because `rootContinuityBonus` causes the second arpeggio slice to also pick an
Eb-rooted chord (matching the first), making the merge condition true. By the time any
external pass could scan for short runs, those runs no longer exist.

Do not retry a short-region external merger. The tones are already aggregated.

#### Dead end: re-analysis of inline-merged aggregate (do not retry)

*(Recorded 2026-06-09 after full implementation and revert — `cc_phase_d_merger_report.md`
Part B+; `cc_instruction_phase_d_reanalysis.md` attempted and reverted.)*

The re-analysis approach was premised on: "inline merge accumulates correct tones → re-run
oracle without rcb contamination → AbMaj7 wins." This premise is **false** for the Δ=+7a
cases. CC implemented the full re-analysis (run-opening context saved, oracle re-called on
merged aggregate) and found:

- bwv102.7: Eb still wins the aggregate by **+0.15 raw score**
- bwv261: C# still wins by **+0.225 raw score**
- Corpus: regressions in both presets; reverted

**Why the aggregate fails:** The aggregate tones are duration-weighted. The arpeggio step
where Eb is the dominant tone contributes **720 ticks** of Eb evidence, while Ab only
contributes **480 ticks**. The oracle on the aggregate `{Eb:720, G:720, Ab:480, C:480, D:240,
Bb:240}` therefore still prefers Eb over Ab. The 2.55 > 2.33 margin cited in the earlier
diagnostic was for the **specific present-root slice** (where Ab dominates), not for the
aggregate. Aggregation dilutes Ab's evidence, making things worse.

**Correct diagnosis:** The oracle ALREADY scores AbMaj7 correctly (2.55 > 2.33) in the
individual present-root slice — the one where Ab actually sounds and dominates. The sole
problem is `rootContinuityBonus` (+0.40) fed by the wrong-root predecessor cascade, which
tips that slice from AbMaj7 to Eb/Ab. No tone-aggregation strategy can fix this; the
issue is the predecessor context, not the evidence set.

Do not retry any Phase D tone-aggregation approach for Δ=+7a. The tones are already
correct; the predecessor signal is wrong.

#### Revised Δ=+7a conclusion: Phase E only

The Δ=+7a mechanism is now fully characterized through three complete dead ends:

1. `noteEnd <=` → `<` backward walk fix: adds the wrong tones (C/Eb, not Ab)
2. Short-region external merger: 0 qualifying runs (tones already aggregated)
3. Re-analysis of inline-merged aggregate: aggregate weights still favor Eb (+0.15)

**The actual blocking issue:** `rootContinuityBonus` (+0.40) cascades from an
arpeggiated-predecessor region that committed the wrong root due to incomplete evidence.
The oracle is already correct in the present-root slice without rcb. The fix requires
Phase E to detect that the predecessor is an arpeggiated (short, incomplete) region and
suppress or reduce rcb for the following slice. This is the same class of issue as Δ=+7b
(near-tie broken by rcb from a correct predecessor), just with an INCORRECT predecessor
rather than a correct one.

**Phase D classification:** Phase D (duration-weighted aggregation, NHT classification)
remains on the roadmap as general infrastructure for passing tones, suspensions, and
ornaments. For Δ=+7a specifically, it is not a fix. The Δ=+7a cases are Phase E work.

#### NHT handling via evidence weighting (Phase E territory)

For non-harmonic tones — passing tones, neighbor tones, suspensions, anticipations —
duration and metric position are strong enough proxies for structural importance that
NHT-like suppression can be applied in a single comprehensive pass. A short note on a
metrically weak position receives low weight regardless of chord identity, which is
sufficient to approximate NHT handling without requiring the chord result first.

Multi-pass scoring (score chord → classify NHTs → rescore) remains available as a
fallback for edge cases that resist single-pass weighting, but is not the primary
design direction.

Phase E is also where Δ=+7a must be addressed: detect arpeggiated predecessors and
suppress/reduce rcb in the following region.

#### Phase D scope and sequencing (revised 2026-06-09)

1. **Bridge forward-lookahead** ✅ COMMITTED `90a52b5fee`
2. **Phase D (Δ=+7a)** ✅ CLOSED — three dead ends; Δ=+7a requires Phase E only
3. **Phase D (general NHT infrastructure)** — duration-weighted aggregation and NHT
   classification remain useful for OTHER non-harmonic-tone cases; design deferred
   until Phase E motivation is clearer
4. **Phase E design** — rcb gating on arpeggiated predecessors (Δ=+7a), voice-leading
   resolution (Δ=+7b), cadence confirmation (B1, A2)
5. **Phase E implementation** — comprehensive forward-context scoring; arpeggiated-predecessor detection; voice-leading and cadence signals

Do not pursue BIR grinding on the remaining BIR=false cases in the current feedforward
pipeline. Targeted fixes now create technical debt against the layers that Phase E will
restructure.

---

### Step 5 — Phase E: unified single-pass architecture with complete evidence

#### Architectural principles (non-negotiable)

**Single commit path.** Every chord commitment — Pass 1 main loop, Pass 2 sub-region,
Pass 2b sub-region, notation bridge — must flow through the same Layer 3 → Layer 4 →
Layer 5 stack. There is currently no single commit path: Pass 2 and Pass 2b both have
manual inline assignments that bypass `advanceTemporalContext`. These duplicates must be
eliminated. `advanceTemporalContext` is called once, uniformly, at every commit site.

**No parallel paths, no code duplication.** The notation path (`findTemporalContext` in
`regiontonecollector.cpp`) and the batch path (`regionanalyzer.cpp`) must use the same
analysis engine. Any logic that appears in both must be unified into one place.
`diagnoseChord` must be a view into the production pipeline's intermediate state, not
a separate parallel scorer.

**Resolve the `explorationMode` dual-path.** `explorationMode` currently modifies
Layer 4 (competition pipeline) behavior — multiple bonuses and gates check it.
This means segmentation exploration runs a modified version of the production pipeline,
creating a hybrid that is neither a clean lightweight oracle nor a full competitor.
The correct resolution is one of:
- Give segmentation its own dedicated lightweight oracle (Layer 3-lite) with no
  progression signals at all — clean separation.
- Accept that segmentation uses the full production pipeline, and remove the flag.
Either way, the `explorationMode` toggle must not straddle Layer 4.

**Symmetric context.** The competition pipeline (Layer 4) currently has an asymmetry:
backward context (`rootContinuityBonus` on `previousRootPc`) is a first-class signal
with a calibrated bonus; forward context (`nextRootPc`, `nextBassPc`) is used only for
narrow specific-progression bonuses (`wSeqBonus` for P4 motion, `wDimBonus` for dim
resolution). There is no symmetric forward-alignment signal analogous to `rcb`.
Phase E completes the context picture started by Steps 1–2: backward and forward
evidence enter the competition on equal footing.

#### What Phase E unlocks

- Δ=+7a (bwv102.7, bwv261): oracle already correct in the present-root slice without
  rcb. Symmetric forward context gives the pipeline access to the evidence that resolves
  the rcb cascade without a compensating gate.
- B1 (MinorMajor7 leading-tone): voice-leading resolution signal requires forward context.
- A2 (dominant quality in minor): key-context feedback.
- Phrase-level and cadence evidence: current/next quality, cadence patterns — all require
  the complete symmetric context to be meaningful.

#### What Phase E must NOT do

- Add compensating gates to the existing feedforward pipeline. Gates are the symptom of
  missing upstream feedback; Phase E provides the feedback, making the gates unnecessary.
- Introduce new parallel structures. Every new signal must slot into the single unified
  pipeline; no new bypass paths.
- Change scoring model calibration before the unified path is in place. BIR numbers will
  shift during restructuring; re-calibration happens after the architecture is stable.

**Gate R — first concrete Phase E deliverable ✅ COMMITTED `638ced1c12` (2026-06-09):**

Gate R is the first gate to fire in the competition pipeline as a direct Phase E mechanism.
It withholds `rootContinuityBonus` when the candidate's bass is foreign to its template
chord tones AND `basisDep ≤ 0` (no sounding third via `sameRootInversionBonus`) AND
`!explorationMode`. Implemented in `harmonicfunctionlayer.cpp` Pass A.

- Fixes all three Δ=+7b targets: bwv245.28 (B/G#→E), bwv296 (D/B→G), bwv320 (G/E→C)
- Bonus: bwv349 m13 also fixed
- Baroque BIR=false 16→13 (−3); Jazz BIR=false 10→7 (−3); zero regressions
- Required `basisDep ≤ 0` refinement (Cm7add11/F extended slash chord edge case)
- Required `!explorationMode` guard (bwv355 segmentation regression without it)
- 6 bridge-path snapshot goldens refreshed; all DCML-verified (2 improvements, 1 neutral winner + neutral alts, 3 alts-only)
- Verification report: `cc_gate_r_verify_report.md`

The Δ=+7a sub-cluster (bwv102.7, bwv261) is NOT addressed by Gate R — and the prior
characterisation ("wrong root wins vertically") was incorrect. Full per-cell oracle dump
(2026-06-09) showed the oracle PREFERS the DCML root in present-root slices. The failure
is arpeggiation segmentation + rcb cascade. Fix: Phase D + Phase E.

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

## Architecture review addendum (2026-06-10) — naming the decode target

*Source: `cowork_target_architecture_review.md` (documents-only review with literature
comparison: Temperley/Melisma DP 1997, Pardo–Birmingham HarmAn 2002, Masada–Bunescu
segmental CRF 2019, AugmentedNet/ChordGNN/RNBert 2021–2024). Status: accepted as design
input for Phase E; to be validated against the as-built system in the follow-up session.*

The review's central finding: the failure classes this plan has been documenting all
season — Δ=+7a ("right now, wrong in 240 ticks"), Δ=+7b (near-tie broken by rcb), the
gate-cascade pattern (audit Finding 7), the rcb dead ends (Iter 98 + predecessor survey)
— are all instances of one defect: **local, irrevocable argmax with first-order patch-up**,
where the literature performs **joint global argmax over a hypothesis lattice**. The plan's
own conclusion for Δ=+7a ("when the next region's evidence contradicts the committed
predecessor identity, revise the predecessor — architectural, not a gate") describes
Viterbi backtracking.

**The mapping is already nearly built.** E2d + Step 5 produced exactly the factorization a
sequence decoder needs:

| This codebase | Sequence-model role |
|---|---|
| `analyzeChord` oracle (`ScoringSnapshot`, per-region ranked cells) | Emission model |
| rcb, resolutionBonus, w_seq, w_dim, step bonuses, cadence signals (planned) | Transition model |
| Gates A–L, Iter 91, Gate R | Hand-coded re-ranking that global decoding subsumes |
| "Inter-region revision" (Phase E aspiration) | Viterbi/beam backtracking — automatic |
| `ScoringPhase::Segmentation` exploration | Segmentation hypothesis scoring (→ joint segmentation+labeling, cf. segmental CRF) |
| Quality levels 0–2 (ARCHITECTURE.md §2.14) | Beam width (1 = current greedy, ∞ = exact DP) |

**Adopted direction for Phase E design (supersedes the feature-pack framing):**

1. **Phase E is a decoder, not a feature pack.** Oracle emits per-region ranked candidates
   (already does); transition scores are the existing progression signals plus the planned
   cadence/voice-leading patterns; decode the best chord path per piece (Viterbi or beam).
   This subsumes Gate R, the rcb gating attempts, Iter 91, and inter-region revision in one
   mechanism. Existing gates stay in place as the comparison baseline during migration;
   BIR + byte-identity infrastructure verifies each step.
2. **Key as a path, not a point.** Key HMM over the existing 252-candidate window scores
   (emissions = raw window scores, transitions = modulation penalty by circle-of-fifths
   distance). `KeyArea` spans (wanted by `unified_analysis_pipeline.md`) fall out of the
   decode. Resolves the shelved Step 3 properly — no dependence on the unreliable
   `normalizedConfidence`.
3. **Fit the weights.** Once scoring is a path objective, calibrate the ~30 hand constants
   against the aligned DCML corpora (structured perceptron or coordinate search), with the
   existing hard-stop metrics as constraints. Stop hand-tuning per anecdote.
4. **Functional labels as sequence labeling over the decoded chord path** (T/S/D states,
   secondary dominants, aug6, tonicization vs modulation from the key path). Per the closed
   investigations (Maj→Dom7, Min↔Maj, key_disagree 15.4%), these are unreachable from
   vertical evidence; they are path properties.
5. **Kept unchanged:** the vertical oracle and its domain heuristics (dim7 rotation
   selector, TPC spelling, `hasStructuralBass`, duration/metric NHT weighting), the
   layering, the evidence-forwarding principle, all corpus/test infrastructure.

**Reconciliation of the §2.14 tension.** ARCHITECTURE.md §2.14 ("layers WITH iteration")
and this plan ("single comprehensive pass; iteration is not a design premise") are both
imprecise names for the same target. Joint inference over the hypothesis lattice IS the
single comprehensive pass, and it equals the fixpoint that iteration would converge to —
computed exactly. The key↔chord and segmentation↔chord circularities dissolve in the joint
decode rather than being scheduled as feedback loops.

**What this does NOT change right now:** no code direction is imposed before the part-2
review of the as-built system. Until then the standing rules hold: no new gates, no
threshold widening, no compensating fixes to the feedforward pipeline.

**Part-2 review complete (2026-06-10, later):** `cowork_implementation_review.md`. Both
reviews are consolidated into the ordered master plan **`docs/implementation_roadmap.md`**
(Stages 0–7 with verification gates and a full traceability table). That roadmap supersedes
the step sequencing in this document for anything beyond the already-completed Steps 1–5;
this document remains the design rationale record.

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
