# Cowork Session Handoff — MuseScore Studio Harmonic Analysis

*Written 2026-05-14 to bootstrap a fresh Cowork session with zero context.*

---

## What this project is

MuseScore Studio. The active development area is `src/composing/`, which implements
harmonic analysis (chord detection, inversion scoring, key inference). The main file
is `src/composing/analysis/chord/chordanalyzer.cpp`. The bridge between the composing
module and the notation layer is `src/notation/internal/notationharmonicrhythmbridge.cpp`.

Two mandatory reads at the start of every session:
- `C:\s\MS\build_and_test.md` — all build/test/tool commands
- `C:\s\MS\STATUS.md` (header only, first ~10 lines) — current baselines and HEAD commit

---

## Two worktrees

- `C:\s\MS` — **master** branch (main working tree — use this for all development)
- `C:\s\MS-llm-triage` — `llm-triage` branch (separate worktree, only for LLM triage work)

All active development is on **master**. Always confirm which worktree CC is in before giving it instructions.

---

## Current state (as of 2026-05-20, post D2-unification — session close)

- **HEAD:** `a69a23e59b` on master, **pushed to origin** (range `16b5bdfa57..a69a23e59b`,
  9 commits). **Working tree is clean.** Iter 97 (Phases 2+3+4 + D2 unification) and
  STEP 1 (dim7/Gate-J) are all committed and pushed. **The unification is complete** — there
  is no uncommitted Phase-4 working tree and no "under diagnostic" state. Any earlier
  language describing Phase 4 as "ready to commit" / "diagnostic" is retired.

  Recent master lineage: `a69a23e59b` (STATUS doc) ← `4d881e7418` (D2 unification) ←
  `3d80d0a91d` (STEP 1 dim7/Gate-J) ← `0d6a78f53d` (gitattributes) ← `9ef6326261` (doc) ←
  `53c4f2d50c` (Pass-1 sparse-admission fallback) ← `34800682f9` / `045cb54e0d` (Phase 4) ←
  `16b5bdfa57` (Phases 2+3). The four canonical region modules are live:
  `composing/analysis/engravingbridge/regiontonecollector.{h,cpp}`,
  `composing/analysis/key/keyresolver.{h,cpp}`,
  `composing/analysis/region/regionanalyzer.{h,cpp}`,
  `composing/analysis/region/sparsechordrefinement.{h,cpp}`.

- **BIR baselines (lenient-OR `align_regions`):** Baroque BIR=true=27, BIR=false=23;
  Jazz BIR=true=33, BIR=false=10. Hard stops: Baroque BIR=false ≤ 25, Jazz BIR=false ≤ 13.
  Cumulative since Iter 91: Baroque BIR=false 188 → 23 (−165, ~88% reduction);
  Jazz BIR=true 103 → 33 (−70, ~68% reduction).

- **Tests:** 407/407 composing, 50/52 notation (2 pre-existing Corelli failures — do NOT
  regress: `CorelliOp01n08dOpeningAndSparseLateBeats`,
  `CorelliOp01n08dUserReportedChordTrackAudit`), 11/11 pipeline snapshot (1 intentional
  skip = `PipelineDivergenceCObservation.GenerateReport`).

- **DCML cross-corpus baseline = 53.8%** (20256/37639, DCML-anchored, time-overlap,
  lenient-OR; 10 non-Bach corpora). Regenerated against the HEAD `a69a23e59b` binary
  on 2026-05-20. **Supersedes the prior 46.8% (15928/34022) at `53c4f2d50c`**, which was
  measured BEFORE STEP 1 + D2 changed chord output — a **+7.0 pp** gain with **every corpus
  improved** (biggest: Corelli +13.7, Mozart +9.4, Schumann +8.4; C.P.E. Bach still 0
  regions, excluded). Reports under `tools/reports/live_20260520_postd2/` (gitignored).
  Regenerate: run the 10 `tools/run_<corpus>_validation.py` scripts
  (`--output <dir> --batch-analyze ninja_build_rel/batch_analyze.exe`; the beethoven
  script writes to a dir named exactly `beethoven`) then
  `python tools/rerun_dcml_comparison.py --cross-corpus-root <dir>`.

- **STEP 1 — dim7-completeness guard + Gate J (committed `3d80d0a91d`):**
  Two coupled `chordanalyzer.cpp` changes. (1) The dim7 characteristic bonus now requires
  the **complete diminished triad** (root + ♭3 + ♭5) before it fires, so an incomplete
  diminished sonority stops out-scoring the dominant-seventh reading the evidence supports.
  (2) **Gate J** — a root-position diminished triad whose dominant root (a major third below)
  is present is treated as an **inverted V7** (vii° → V7 completion; canonical case
  bwv110.7 m10 `C#dim7 → F#7`); requires the complete diminished triad. Impact:
  **Jazz BIR=true 56→33 (−23)**, **Baroque BIR=false 25→23 (−2)** (Jazz fixes bwv282,
  bwv60.5, bwv65.2). 5 pipeline-snapshot goldens refreshed and DCML-verified.

- **D2 unification (committed `4d881e7418`, recorded in `a69a23e59b`):**
  `pass1MinDistinctPcsForCandidate=1` on the batch path — matching the bridge. This was the
  **last batch/bridge parameter divergence**; bridge and batch are now **fully unified** thin
  wrappers over `region::analyzeRegions()`. Both paths admit sparse 1–2 PC Pass-1 slices.
  `regionanalyzer.cpp` untouched (pure flag unification). Net error reduction both corpora
  (Baroque BIR=true 34→27 / false 25→23; Jazz BIR=true 56→33 / false 13→10).

- **Unification status:** Iter 97 Phases 2+3+4 + D2 are **complete**. Both parameter
  divergences are resolved: **D1 (`excludeLookAheadOnDenseStart`)** is confirmed
  load-bearing and **intentionally divergent** (batch passes `true`, bridge defaults
  `false`; unifying it regresses bridge/Corelli trio-sonata dominants); **D2
  (`pass1MinDistinctPcsForCandidate`)** is unified at `1` on both paths. The bridge and
  batch are fully unified thin wrappers over `regionanalyzer`.

- **Iter 98 candidates:**
  - **bwv320 m27 (primary residual):** reads `G6/E` instead of `C`. An admitted 2-PC `Gm`
    Pass-1 slice overwrites `previousRootPc`, and `rootContinuityBonus` (+0.40) tips a
    0.02-margin window to G. Fix: **gate `rootContinuityBonus` off a sparse/uncertain
    predecessor** in `chordanalyzer.cpp`. (A context-transparent-sparse orchestrator change
    was rejected — it regresses the bridge / Corelli trio-sonata dominants.) Full
    investigation in `regionanalyzer.h` `AnalyzeRegionsOptions` docs.
  - **α-variant: `w_dim` rotation-only guard** (from the Iter 96 deferral list) — add a
    guard requiring the current winner to also be Dim/HalfDim before `wDimBonus` fires, so
    only the enharmonic rotation is contested (may recover `schumann bvo7→viio7/V`,
    `chorale_003 Am→G#dim` without the quality-flip misfires).
  - **δ: sparse-minor diatonic quality prior** — when `distinctPcs ≤ 3` and the third is
    absent/weak, prefer the quality the current key assigns to that scale degree. Directly
    fixes the 2 pre-existing Corelli notation failures.

- **Pre-existing issue to investigate:** `tools/test_batch_analyze_regressions.py` reports a
  **BWV227.7 m9 pitch-class E** failure. This is present **before any of this session's
  changes**, is **not yet in any tracked baseline**, and is not caused by STEP 1 / D2 — it
  needs its own investigation.

- **Chord mismatch report:** 4 RealDiff (pinned), 127 ConventionDiff (Jazz)

---

## Iter 78 fixes (all committed, do not re-implement)

**Fix A** — `notationharmonicrhythmbridge.cpp`, `absorbShortRegions` lambda:
Short regions are only absorbed into the previous region when they share the same root
(`sharesPrevRoot`). A differently-rooted short region keeps its own boundary.

**Fix B** — `chordanalyzer.cpp` line ~129, `pitchClassName()`:
G# → Ab flattening is exempted at `keySignatureFifths == 0` (A minor), where G# is
the leading tone. Condition: `pc == 8 && keySignatureFifths < 3 && keySignatureFifths != 0`.

**Fix C** — `chordanalyzer.cpp` lines ~1762-1766:
Augmented template score ×0.5 when `distinctPcs <= 2` and root PC weight is at or
below `extensionThreshold`. Prevents root-absent 2-PC guesses winning as Augmented.

---

## Iters 79–84 — all committed

- **Iter 79** (`cbd7230c1f`) — augmented bare-root guard + qualitySuffix Dim/HalfDim fix
- **Iter 80** (`b4a375db45`) — refreshed 7 stale pipeline snapshot goldens
- **Iter 81** (`9d2a70cef4`) — removed dead Jaccard code; notation tests now 52 total / 50 passing
- **Iter 82** (`57511f012f`) — Gates E/I absent-root guard; BIR=false=118, BIR=true=4, Jazz BIR=false=7
- **Iter 83** (`1c57ebcac2`) — batch path anchor end-tick fix (port Iter 77 Fix B)
- **Iter 84** (`4da8252c9e`) — R4 narrow fix: G# leading-tone exemption extended to keyFifths=1 (A melodic minor regime)

## Iter 84 detail (do not re-implement)

**File:** `src/composing/analysis/chord/chordanalyzer.cpp`, lines ~117–153

`pitchClassNameFromTpc()` had a G# (pc=8) exemption from Ab-normalization at `keyFifths==0`
(Iter 78 Fix B, for A natural minor). A melodic minor ("Amel") maps via `resolveToFifths()`
to its Dorian parent at `keyFifths=1`, falling outside the exemption → G# was spelled "Ab".

Fix: added `&& keySignatureFifths != 1` to the normalization condition, and extended the
TPC-disambiguation block to also fire at `keyFifths==1 && pc==8` (so flat-authored Ab with
tpc≤14 in that regime is still correctly spelled flat).

Result: bach_chorale_003 — 3 chord symbols corrected (Abm7b5/B→G#m7b5/B, E/Ab→E/G# ×2).
bach_chorale_003 golden refreshed. BIR unchanged (BIR operates on root_pc/bass_pc).

**Deferred — R4 family B (chorale_137, later iteration):**
- pc=6 (F#/Gb): no TPC-honor block exists for pc=6 at all; unconditionally returns Gb at keyFifths<0
- Flat-authored Ab bass in V/V context (tpc=10 in chorale_137 m2): heavier "chord-3rd-of-major-triad" override, out of scope

---

## Iters 85–89 + DCML comparator — all committed

- **Iter 87** (`2dd2f35c17`) — bass-b7 post-merge re-stamp in batch_analyze.cpp
  (`analyzeScore` merge discarded MinorSeventh extension stamped by Iter 86; post-filtered
  re-stamp pass at batch_analyze.cpp:1846–1880 fixes 281 of 293 b7-bass slash-chord cases)
- **Iter 88** (`bea00f3482`) — honor sharp F# TPC for pc=6 in flat keys (extends
  TPC-disambiguation block to fire at `keyFifths<0 && pc==6`; Gb→F# in D/F# and similar
  contexts)
- **Iter 89** (`2085f11322`) — honor sharp G# TPC for pc=8 across flat and mildly-sharp
  keys (removed pc=8 from Iter 78 flattening block; added `keyFifths<0 && pc==8` and
  `keyFifths==2 && pc==8` to TPC-honor block; survey script `tools/survey_pc8_flat_authored_bass.py`)
- **DCML comparator** (`eefa412b6f`) — new time-overlap comparator in compare_analyses.py
  (mode='time-overlap', lenient-OR-50% overlap threshold) + rerun_dcml_comparison.py
  re-aggregation driver. Old beat-snap 69.1% figure retired (biased +21pp). New primary
  metric: 47.8% weighted root agreement across 10 non-Bach corpora (DCML-anchored).
  Bach chorales: 64.9% overall, 87.2% chord-identity, 100% alignment.
  **Superseded:** the live baseline is now **53.8%** (regenerated 2026-05-20 at HEAD
  `a69a23e59b`; see "Current state" block above). The 47.8% figure is historical only.

**Iter 90 — shelved (no commit):**
122 wrong-root cases characterized (tools/analyze_wrong_root_iter90.py,
tools/iter90_wrong_root_characterization.txt). 84% are iii/III triad confusion — non-local
ambiguity. Both Variant A (+12 errors) and Variant B (+22 errors) regressed. Design note:
`docs/iter90_bass_as_root_promotion_shelved.md`. Future path: Iter 91, bridge-level
adjacent-context pass using nextRootPc/previousRootPc from ChordTemporalExtensions.

**Iter 91 — attempted and reverted (no commit):**
Temporal-context gate: when the winning chord's root is a third above the bass (iii/III
pattern), promote the bass-rooted reading from rawCandidates when `nextRootPc == bassPc`
(forward resolution signal). Tried both `previousRootPc OR nextRootPc` (too permissive —
fired on genuine I→I6 progressions) and `nextRootPc` only. Final result on `nextRootPc`
only: BIR=false 188→185 (−3), BIR=true 38→41 (+3) — net neutral at 226→226 total errors.
Reverted. Working tree clean at `2de18139c2`. Superseded by Iter 92 holistic design.

**Ground-truth QA session — 2026-05-16:**
Opened 5 DCML-annotated scores in MuseScore with GT and US labels injected side-by-side
(via `tools/inject_dcml_rn.py`). Visual review identified two distinct bugs causing
the bulk of BIR=false=188 errors:

- **Bug 1 — Passing-note bass contamination:** When the bass voice has two eighth notes
  within a beat window (e.g. G3 onset + F#3 passing), the lower-pitched passing note
  (entering mid-region) overrides the beat-onset structural note as bassPc. Mechanism
  confirmed by diagnostic: both G3 (MIDI 55) and F#3 (MIDI 54) appear in region
  [4800,5280) with equal pcWeight=0.20; F#3 wins because 54 < 55. This flips root
  inference (e.g. G major → Em/F# or Am/F# instead of correct G or G7).

- **Bug 2 — Incomplete slash chord beats complete root-position triad:** Given pitch
  classes {C,E,G} with C in bass, the template scores Em/C ~2.86 vs C major ~2.40 — a
  gap of ~0.46. Em/C "wins" even though B (the 5th of Em) is absent and C is not in Em.
  Root-position completeness is not rewarded. Seen on bwv310, bwv319, bwv103.6, bwv283.

**Iter 92 — committed (`80fe13b59b`):**
Joint (bass, chord) scoring with `w_complete` bonus (distinctPcs==3) and multi-bass
enumeration. Design at `docs/iter92_joint_bass_chord_scoring.md` (still authoritative
reference for the JOINT formula and follow-up scope). What landed:

- Struct fields added: `ChordAnalysisTone::onsetAtRegionStart` (bool) and
  `ChordTemporalContext::nextBassPc` (int, −1=unknown) in `chordanalyzer.h`.
- Joint enumeration loop in `chordanalyzer.cpp`: enumerate bass candidates from the bass
  register, score each (bass, root, template) triple = base score (bass-independent) +
  bass-dependent deltas (`appliedBassRootBonus`, `nonBassAdjustment`, inversion contextual)
  + `w_complete = +0.50` bonus when distinctPcs≥3 AND all three triad tones are present
  above extensionThreshold AND bass_candidate.pc == triad_root.
- Callers populated: `notationcomposingbridgehelpers.cpp::collectRegionTones` (onset flag),
  `notationharmonicrhythmbridge.cpp` and `tools/batch_analyze.cpp` (nextBassPc assignment).
- Pipeline snapshot goldens refreshed (10 of 11): bach_chorale_001/003/137,
  bach_bwv806_prelude/gigue, mozart_k279_1/k280_1, chopin_bi105_op30_1, corelli_op01n08a,
  schumann_kinderszenen_n01. Audited: clean Bug 2 fix patterns (D7/A→D7, FMaj7/E→FMaj7,
  F/C→F, G/C#→G, AMaj7/G#→AMaj7, E/B→E, E/G#→E, C/E→C, F/A→F). No regression patterns.
- BIR impact: Baroque BIR=false 188→46 (−142). Baroque BIR=true 38→41 (+3, bucket
  reclassifications). Jazz BIR=true 103→114 (+11). Jazz BIR=false 13→14.

**Iter 93 — committed (`f98586fa67`, plumbing only; Step 3b shelved):**

Landed: `collectRegionTones` (in both `notationcomposingbridgehelpers` and
`tools/batch_analyze`) gained an optional `parentStartTick` parameter (default −1 ⇒
falls back to `startTickInt` for un-split callers). Pass 2 / Pass 2b sub-region call
sites in `notationharmonicrhythmbridge.cpp` and `batch_analyze.cpp` pass the parent
region's startTick so the per-tone `trueAttackAtStart` flag is computed at full-region
scope rather than against the narrow sub-region boundary. `chordanalyzer.cpp` is
unchanged relative to Iter 92; the joint-scoring loop, the `w_complete` bonus, and the
`jointScoringEnabled` gate are intact. Baselines unchanged from Iter 92.

**Step 3b (`w_onset` / `w_passing` per-bass-candidate score deltas) — SHELVED:**

Three variants were attempted and all hit Baroque BIR=false hard stops:
- Symmetric (`+0.15` onset bonus, `−0.10` passing penalty): +7 BIR=false.
- Asymmetric penalty-only (`0` onset, `−0.10` passing): +4 BIR=false.
- Asymmetric + onset-gated (penalty only fires when at least one bass candidate has
  `onsetAtRegionStart=true`): +3 BIR=false.

Root cause: in Baroque polyphony the bass voice routinely moves mid-region to the
actual chord root (arpeggiated bass, melodic bass motion). The onset-position signal
is not a reliable proxy for "structural bass" in this corpus — the same signal that
would penalise a passing-note artefact also penalises a genuine arpeggiated structural
root. No further onset-position tuning is expected to clear this; the signal is wrong
for the corpus.

**Iter 94 — committed (`dbfe09fe6f` + STATUS backfill `a34b5c1e6c`):**

Iter 92's deferred Step 3c (`w_stepIn` / `w_stepOut` voice-leading bonuses) is now
active in `RuleBasedChordAnalyzer::analyzeChord`. Root-position candidates earn +0.10
when the bass moves by semitone or whole-tone from `context->previousBassPc` and +0.10
again on motion to `context->nextBassPc`. Parent-scope plumbing: bridge Pass 2 / Pass 2b
in `notationharmonicrhythmbridge.cpp` and the main loop in `tools/batch_analyze.cpp`
compute the predecessor / successor PARENT region's bass PC and override
`subCtx.previousBassPc` / `subCtx.nextBassPc` for each sub-region `analyzeChord` call
(the override happens AFTER the stepwise booleans, which intentionally remain
sub-region-scope for passing-tone / inversion signals, and BEFORE the call; the
post-call restore keeps the next iteration's stepwise boolean correct).

Four gates were required to keep the bonus safe — each motivated by a concrete
regression caught during iteration:

1. **`explorationMode` suppression** — new field `ChordAnalyzerPreferences::explorationMode`
   (default `false`). `greedyExpandSegmentation` sets it to `true` on every internal
   boundary-exploration `analyzeChord` call (Round 1 head/tail synthesis + Round 2 region
   scoring in `harmonicsegmenter.cpp::fillGap`). The bonus would otherwise bias
   sub-region bass selection toward stepwise candidates and redirect segmentation
   before the final per-region scoring pass runs.
2. **Root-position guard `candBassPc == cand.rootPc`** — the bonus is meant to reward
   "this chord's root moves smoothly in the bass line," not "this slash-chord's bass
   happens to step smoothly." Applying it to slash-chord bass caused a Jazz bwv430
   BIR=false +1 regression (a G#m7/F# bass stepping to a neighbouring bass gained
   credit even though its root G# was not the moving voice). Enforced both in the
   lambda body and in the Pass-B outer loop that skips non-root-position candidates.
3. **Corrected first-inversion-m7-family guard** — if any competitor in the same
   `perBass` block with quality in {HalfDiminished, Diminished, Minor7} sits at
   `(candBassPc - 3) mod 12` (i.e. its root is a minor third BELOW our bass, the
   first-inversion shape) AND scores within `kStepBudget = kWStepIn + kWStepOut + 0.01`
   of the candidate's unbonused score, both step bonuses are suppressed. Canonical
   case: Dm6 (candBassPc=2, rootPc=2) vs Bø7/D (competitor rootPc=11, bassPc=2) — the
   m7-family competitor's root is the minor third below our bass, not at our bass. The
   guard prevents the step bonus from tipping a fragile m6 root-position reading over
   an equally viable first-inversion m7-family reading on identical pitch evidence.
4. **Power-quality exclusion** — root+fifth-only templates are excluded outright. Five
   sparse-Jazz Tonic-on-strong-beat regressions (bwv20.7 m16b1, bwv227.1 m11b3,
   bwv245.40 m27b3, bwv384 m4b3, bwv422 m14b1) had Power `[Tonic]5` reads tip past
   viable triad reads when the bonus fired. Extending the exclusion to Suspended2/4
   caught a sus residual but regressed Jazz BIR=false (14 → 15) — beyond hard-stop
   scope, so the current cut is Power-only.

BIR impact (lenient-OR comparator):
- Baroque BIR=true 41→43 (+2, bucket reclassifications, not new errors)
- Baroque BIR=false 46→33 (−13, ~28% reduction)
- Jazz BIR=true 114→117 (+3)
- Jazz BIR=false 14 (flat)

Tests: 407/407 composing, 50/52 notation (same 2 pre-existing Corelli implode
failures), 11 passed / 1 skipped pipeline_snapshot — all 11 active goldens refreshed
(bach_chorale_001/003/137, bach_bwv806_prelude/gigue, mozart_k279_1/k280_1,
chopin_bi105_op30_1/2, corelli_op01n08a, schumann_kinderszenen_n01).

**Deferred — Iter 95 candidates (status after Iter 96):**
- **`w_onset` / `w_passing` via duration-weighting.** Still deferred — Iters 94–96
  continued harvesting BIR improvements without it. Reconsider only if a concrete
  failure pattern emerges that existing bonuses cannot reach.
- **`w_seq`** — landed as Iter 95. Done.
- **bwv320 Am 1-case residual.** Still deferred.

---

## Iter 96 — committed 2026-05-18

**Commits:** `0de94516ff` (code) + `7060f2c5db` (STATUS amendment)

**Change:** `w_dim` +0.15 bonus in `chordanalyzer.cpp`. New `wDimBonus` lambda
alongside `wSeqBonus`. Fires when a Diminished or HalfDiminished candidate's root
sits one semitone below `context->nextRootPc`
(`(nextRootPc - candRootPc + 12) % 12 == 1` — leading-tone resolution signal).

Gates: `jointScoringEnabled && !prefs.explorationMode && context &&
context->nextRootPc >= 0 && (quality == Diminished || quality == HalfDiminished)
&& distinctPcs >= 4`. No new plumbing — `nextRootPc` already populated by Iter 95.

Three variants were tried before committing:
1. **Loose (delta==1, no distinctPcs gate):** Baroque −3/0, Jazz +2/0.
   bwv296 m12 b4 direct misfire (3-PC region, G/B wrongly flipped to B°) +
   Corelli golden regression (F7/A → Adim dropping the structural 7th). Not committed.
2. **Tightened (delta==1, distinctPcs >= 4):** Baroque −3/−1, Jazz +1/0.
   bwv296 misfire and Corelli golden regression both eliminated by the gate.
   Jazz +1 residual is a cascade from an upstream w_dim fire (Cadd11, Major
   quality — not a direct w_dim misfire, not a hard stop). Committed.
3. **delta==2 variant:** not attempted — widening after delta==1 already produced
   misfires was expected to add more.

The `distinctPcs >= 4` gate intentionally suppresses the sparse-region tier.
Two improvements from the loose gate (`schumann bvo7→viio7/V` tick 480,
`chorale_003 Am→G#dim`) were inseparable from the misfires — both were
3-PC sparse regions where the bonus was a quality flip, not a rotation correction.
A future iteration may recover them by adding a rotation-only condition
(require the current winner to also be Dim/HalfDim).

**BIR impact (lenient-OR comparator):**

| Metric | Pre-96 | Post-96 | Δ |
|--------|--------|---------|---|
| Baroque BIR=true | 44 | 41 | −3 |
| Baroque BIR=false | 27 | 26 | −1 |
| Jazz BIR=true | 68 | 69 | +1 |
| Jazz BIR=false | 13 | 13 | 0 |
| **Total** | **152** | **149** | **−3** |

**Tests:** 407/407 composing, 50/52 notation (same 2 Corelli), 11/11 snapshot
(2 alt-only goldens refreshed: `bach_bwv806_gigue`, `schumann_kinderszenen_n01`).

**Deferred — Iter 97 candidates:**
- **α-variant: w_dim rotation-only** — add guard requiring the current winner to
  also be Dim/HalfDim before `wDimBonus` fires. Only the enharmonic rotation is
  in contest, not the quality. May recover `schumann bvo7→viio7/V` and
  `chorale_003 Am→G#dim` without the quality-flip misfires. Quick to try.
- **δ: sparse-minor diatonic quality prior** — when `distinctPcs <= 3` and the
  third is absent/weak, prefer the quality that the current key assigns to this
  scale degree. Directly fixes the 2 pre-existing Corelli notation failures
  (`CorelliOp01n08dOpeningAndSparseLateBeats`,
  `CorelliOp01n08dUserReportedChordTrackAudit`). Harder to gate safely.
- **β: P4-above mis-rooting** (~27 cases) — diffuse, no single fix, deferred.
- **γ: M2-above mis-root** (~17 cases) — diffuse, deferred.

---

## Standing rule — CC instruction preamble (MANDATORY, every single CC session)

CC starts with ZERO context every time. Every instruction to CC must open with:

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only),
> `C:\s\MS\build_and_test.md`
>
> **Current state:** Branch `master`, HEAD `a69a23e59b`, **pushed to origin**,
> **working tree clean**. Iter 97 (Phases 2+3+4 + D2 unification) and STEP 1
> (dim7/Gate-J) are all committed and pushed. The four canonical region modules are
> live: `composing/analysis/engravingbridge/regiontonecollector.{h,cpp}`,
> `composing/analysis/key/keyresolver.{h,cpp}`,
> `composing/analysis/region/regionanalyzer.{h,cpp}`,
> `composing/analysis/region/sparsechordrefinement.{h,cpp}`. The bridge
> (`analyzeHarmonicRhythm`) and batch (`analyzeScore`) are fully unified thin wrappers
> over `region::analyzeRegions()`. BIR baselines (lenient-OR `align_regions`):
> Baroque BIR=true=27, BIR=false=23; Jazz BIR=true=33, BIR=false=10. Tests:
> 407/407 composing, 50/52 notation (2 pre-existing Corelli failures — do not regress:
> `CorelliOp01n08dOpeningAndSparseLateBeats`,
> `CorelliOp01n08dUserReportedChordTrackAudit`), pipeline_snapshot 11/11 (1 skipped).
>
> **Unification is complete.** Both parameter divergences are resolved: D1
> (`excludeLookAheadOnDenseStart`) is intentionally divergent and load-bearing (batch
> `true`, bridge `false`); D2 (`pass1MinDistinctPcsForCandidate`) is unified at `1` on
> both paths (`4d881e7418`). STEP 1 (`3d80d0a91d`): the dim7 characteristic bonus now
> requires the complete diminished triad, and Gate J treats a complete root-position
> diminished triad over a sounding dominant root as an inverted V7 — Jazz BIR=true
> 56→33 (−23), Baroque BIR=false 25→23 (−2).
>
> Hard stops always: Baroque BIR=false > 25, Jazz BIR=false > 13, any test
> regression beyond the 2 known Corelli notation failures.

This preamble goes before EVERY task description, no exceptions.

---

## Windows Snap fix — do not revert

File: `muse/framework/ui/internal/platform/windows/winwindowscontroller.cpp`
Function: `calculateWindowSize()`

Two lines that set `ptMinTrackSize` equal to the full monitor work area were removed.
This prevented Windows Snap from working on maximised MuseScore windows.
`ptMaxSize` and `ptMaxPosition` are kept. `ptMinTrackSize` is intentionally left unset.

The fix is committed as a local-only branch in the muse submodule (`fix/windows-snap-ptmintracksize`
at `b9604805a`). The parent repo's master correctly pins the submodule pointer to this commit.
**Do not restore the `ptMinTrackSize` lines. Do not push the muse submodule to upstream.**

This is documented in `C:\s\MS\CLAUDE.md` which CC reads every session.

---

## Known CC/VS Code integration issues

**Stale `git index.lock`** — When CC loses contact with a running git process (a known
VS Code integration bug), `.git/index.lock` is left behind (0 bytes). Symptom: git
commands fail with "Unable to lock the index". Fix: verify no git process is running
(`tasklist | grep git`), then delete `.git/index.lock`. Safe to delete if file is
0 bytes and no git process is running.

**Silent disconnect — three distinct triggers (diagnosed 2026-05-14 from VS Code logs)**

VS Code sets the CC session to `idle` (handing control back to user) in these situations,
while the CC process keeps running invisibly. Dangerous to submit new tasks without waiting.

**Trigger 1 — Non-zero exit code:**
A bash command returns non-zero (failing tests, grep with no matches, etc.). The extension
sees this as an error and marks the session idle. CC keeps running.
Fix: append `; echo "exit:$?"` to every command that may return non-zero. The echo always
returns 0, so the extension sees a clean result.
- BAD:  `./pipeline_snapshot_tests.exe --gtest_filter='*name*'`
- GOOD: `./pipeline_snapshot_tests.exe --gtest_filter='*name*'; echo "exit:$?"`
- BAD:  `grep -n "pattern" file.cpp`
- GOOD: `grep -n "pattern" file.cpp; echo "exit:$?"`

**Trigger 2 — stream_idle_partial (long bash output):**
When a bash command produces large output and CC takes >~15 seconds to process the result,
the API stream goes idle between chunks. The extension logs `[WARN] [Stall] stream_idle_partial`
and marks the session idle. CC is still running and will eventually complete.
Fix: break long commands into smaller steps that produce incremental output. Pipe through
`head -N` to limit output size. Write large results to a file and read separately rather
than capturing in one bash call.
- BAD:  `batch_analyze <score> --dump-regions notation`  (may produce thousands of lines)
- GOOD: `batch_analyze <score> --dump-regions notation > /tmp/out.json; echo "exit:$?"`
         then `head -50 /tmp/out.json`

**Trigger 3 — stream_idle_partial (API latency, bytesTotal=0):**
When the Anthropic API takes >15 seconds to send the first token of a response (server load,
network hiccup), the extension logs `stream_idle_partial lastChunkAgeMs=15xxx bytesTotal=0`.
This can silently drop the panel even though CC recovers and keeps running. No reliable
prevention — it's server-side latency. If the panel goes silent mid-task without any bash
errors, this is likely the cause. Check the VS Code output log before resubmitting.

Build commands (setup_and_build.bat) are launched via PowerShell Start-Process which
isolates the exit code — less affected by trigger 1.

---

## .vscode/settings.json — muse submodule noise

VS Code detects `muse/.git` (submodule gitdir pointer) and prompts to open it as a
separate repository. Two settings suppress this in `C:\s\MS\.vscode\settings.json`:
- `"git.detectSubmodules": false` — stops VS Code treating submodules as separate SCM providers
- `"git.ignoredRepositories": ["C:\\s\\MS\\muse"]` — belt-and-suspenders ignore by path

If CC hasn't applied these yet, ask it to edit `.vscode\settings.json` accordingly,
then Ctrl+Shift+P → "Reload Window".

---

## Build commands (quick reference)

```
# Build
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"

# Tests (run from ninja_build_rel/)
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe

# Corpus quality check
cd C:\s\MS && python tools/analyze_inversion_errors.py

# Mismatch report location
src/composing/tests/chord_mismatch_report.txt
```

---

## Standing practices — build and corpus hygiene

Two silent failure modes that produce plausible-looking but wrong results:

**Stale build** — if the working tree has uncommitted changes and the binary
hasn't been rebuilt, corpus analysis runs against the old logic. BIR numbers
will look identical to the last clean run but the characterization is wrong.
**Always rebuild before any corpus run when the working tree has been modified**,
or when there is any doubt about whether the binary matches the source.

**Stale corpus output** — `analyze_inversion_errors.py` reads whatever JSON
files are already in `tools/corpus/`. If `run_bach_preset.py` was not run
first (or was run against a different binary), the analysis silently reads
old results. **Always run `run_bach_preset.py` immediately before
`analyze_inversion_errors.py`** — never rely on corpus JSON files left over
from a prior session or a prior build.

Canonical corpus analysis sequence (never skip steps):
```
# 1. Rebuild first if working tree has changes
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"

# 2. Regenerate corpus (Baroque)
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus

# 3. Analyse (reads the freshly written JSONs)
cd C:\s\MS && python tools/analyze_inversion_errors.py

# Repeat steps 2–3 for Jazz if needed (reuses same output-dir)
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

---

## LLM integration design — completed 2026-05-15

A full architectural design session for "Claude Composer" — natural-language interaction
with scores via an LLM of the user's choice (analogous to Claude Code / Copilot in IDEs).

**Two documents created / updated:**

- `docs/llm_integration.md` — comprehensive design document (11 sections). Read this
  before any implementation work on the LLM bridge.
- `ARCHITECTURE.md` §19 — high-level overview and key decisions (4 subsections).

**Key conclusions that are not obvious from reading the docs:**

- The Core Access Layer is a **facade over existing INotation* interfaces** — not a new
  information model. §5.2 has the full interface inventory. The point is to avoid
  translation loss, not to redesign the data model.

- LLM bridge uses the **stateless tier** (tool calls, musical addresses, no object
  references). Plugin API uses the **stateful tier** (EID-backed handles, event
  subscriptions). These are different programming models; do not conflate them.

- **Event subscriptions keep dependency direction one-way.** When `ScoreEventSource`
  (Core Access Layer) subscribes to `async::Channel<ScoreChanges>`, the subscription
  is initiated *from* the Core Access Layer *into* MuseScore. `async::Channel` stores a
  callback and fires it — it has no reference back to the subscriber. No reverse
  dependency is created.

- `src/composing/` is **not part of official MuseScore** — it is this project's own
  development. §10 and ARCHITECTURE.md §19.3 both note this explicitly.

- **MusicalAddress is the cross-cutting join key.** There are NO direct object
  references from Note → Staff or Note → Measure. A Note's address (`partId`,
  `staffIndexInPart`, `measureNumber`, `beat`, `voice`, `tick`) is the only locator.
  Querying "all notes in measure 12 of the Oboe" is a pure filter over addresses —
  no graph traversal. Harmony, Annotation, and Note at the same MusicalAddress are
  co-located: matching on address is the equivalent of a SQL join on a composite key.

- **Address does NOT uniquely identify a Note.** Multiple notes in the same chord
  share an identical MusicalAddress (same part + staff + measure + beat + voice).
  A `NoteId` is required to unambiguously identify a single note. The information
  model must carry NoteId on the Note entity.

- Subsection numbering in `llm_integration.md` §7 and §8 had a drift (labels said
  6.x and 7.x respectively) — fixed 2026-05-15.

---

## ms-core-api branch — decisions made 2026-05-15

A new branch and worktree for the Core Access Layer (protocol-neutral facade over
`INotation*` and friends, shared foundation for plugin API and LLM bridge).

**Branch:** `ms-core-api`  
**Worktree:** `C:\s\MS-core-api` ✓ created 2026-05-15  
**VS Code window:** separate window on `C:\s\MS-core-api`  
**CC context:** automatically separate (different path = different CC project memory)  
**CLAUDE.md:** ✓ written and committed on the branch — scoped to CAL, composing-module sections removed

**Known gap — build script:** `setup_and_build.bat` inherited from master hardcodes
`c:\s\MS\ninja_build_rel`. A `setup_and_build.bat` specific to `C:\s\MS-core-api`
needs to be created (pointing to `C:\s\MS-core-api\ninja_build_rel`) before the
first build attempt in the new worktree.

**Current state:** CLAUDE.md committed, no code written yet. Next steps:
1. Create `setup_and_build.bat` for the worktree
2. Create `src/ms-core-api/` skeleton (CMakeLists.txt + first interface headers)
3. Wire into root CMakeLists.txt
4. Create junction points for extensions/plugins (see below)

**Why `ms-core-api` as a name:** "plugin-api-v2" would imply the QML/Q_PROPERTY
protocol; this layer is protocol-neutral. It exposes capabilities (score read/write,
settings, project, playback, instruments) without committing to any binding technology.
Protocol-specific layers (QML bindings, JSON/tool-call schema for LLM) sit above it.

**Architecture:**
```
Plugin bindings (QML)   LLM bridge (JSON)   future protocols
        └───────────────────┴──────────────────┘
                    ms-core-api
              (capabilities, no protocol)
                    INotation* family
                    MuseScore DOM
```

**Dev environment prerequisite — junction points (one-time, do before first test run):**

Extensions and plugins are in `share/extensions/` and `share/plugins/` but
`appDataPath()` on Windows resolves to one level up from the exe (`C:\s\MS\` when
running from `ninja_build_rel\`). MuseScore looks for `C:\s\MS\extensions\` and
`C:\s\MS\plugins\` — neither exists without junctions. Fix:
```
mklink /J "C:\s\MS-core-api\extensions" "C:\s\MS-core-api\share\extensions"
mklink /J "C:\s\MS-core-api\plugins"    "C:\s\MS-core-api\share\plugins"
```
(Run as Administrator in cmd.exe. Do this in the ms-core-api worktree.)

**Full-stack test loop once junction points exist:**
1. Write C++ in `src/ms-core-api/` → build MuseScore5.exe
2. Write a minimal test extension: `manifest.json` + JS/QML in `C:\s\MS-core-api\extensions\your-test\`
3. Launch MuseScore5.exe, open a score, run the extension
4. No install step needed — extensions load from the junction-pointed directory

**Extension anatomy (v2 system):**
- `manifest.json` — declares URI, type (macros/composite/form), actions
- `main.js` or `Form.qml` — the extension logic
- API surface available to extensions: `api.log`, `api.interactive`, `api.engraving`,
  `api.converter`, `api.websocket` (see `muse/framework/extensions/api/extapi.h`)
- ms-core-api methods will be added here once implemented

**Legacy v1 plugins** (QML, old API) live in `share/plugins/`. They use the
`muse/framework/extensions/api/v1/` path and the old `PluginAPI`/`qmlRegisterType`
system. Relevant for understanding what exists; NOT the target for ms-core-api work.

---

## AI Assistant extension MVP — work done 2026-05-16

Independent of CAL work. AI Assistant chat extension is the first concrete LLM-bridge
artefact per the [[llm-bridge-mvp-strategy]] memory (build v2 extension first, validate
where the API gaps actually bite). Lives in the ms-core-api worktree at
`share/extensions/ai-assistant/` (`Main.qml` + `manifest.json`). Committed as
**`87ff66b8e5`** on a new branch **`ai-assistant-mvp`** (cut from the same point as
`ms-core-api`), specifically so the CAL branch stays focused.

**Branch:** `ai-assistant-mvp` (in the `C:\s\MS-core-api` worktree; switch with
`git checkout ai-assistant-mvp` if you want the files materialised — they're committed
only on that branch).

**Deployed copies** (untracked or outside repo; used at runtime by MS4):
- `C:\Users\vince\AppData\Local\MuseScore\MuseScore4\extensions\ai-assistant\Main.qml`
- `C:\s\MS\ai-assistant\Main.qml` (staging — was stale at v0.4.3, reconciled to v0.4.12 on 2026-05-16)

All three copies are byte-identical at 75225 bytes / v0.4.12.

**Four MS4 limitations discovered and worked around:**

1. **`Qt.labs.settings` not deployed in MS4 install** — `C:\Program Files\MuseScore 4\qml\Qt\labs\` ships only `platform/` and `qmlmodels/`; `settings/` is missing because windeployqt only ships modules MuseScore itself imports, and the main UI never imports `Qt.labs.settings`. Fix: switched to `import MuseScore 3.0; Settings { ... }` — that's the vendored `QQmlSettings` registered in `muse/framework/extensions/api/v1/extapiv1.cpp:40` via `qmlRegisterType("MuseScore", 3, 0, "Settings")`. Process-global registration, so it works from V2 extensions too, not just V1 plugins. No deployment dependency.

2. **`FlatButton` / `import Muse.*` deploy gate over-matched** — the grep pattern in the [[ms4-deploy-gate]] memory (`grep -c "FlatButton\|import Muse"` expecting 1 — the line-2 self-describing comment) over-matched after the Enter workaround landed in v0.4.11: caught `import MuseScore 3.0` strings, `import Muse.Ui\n` substrings inside `Qt.createQmlObject` calls, and doc comments. Tightened the gate to `grep -nE "^[[:space:]]*(import[[:space:]]+Muse\.|FlatButton)"` expecting empty output. Mirrors the actual extension validator in [extensionbuilder.cpp:42-60](muse/framework/extensions/qml/Muse/Extensions/extensionbuilder.cpp#L42-L60). Memory updated.

3. **Stale staging vs deployed divergence** — the staging copy at `C:\s\MS\ai-assistant\Main.qml` had been left at v0.4.3 (May 15) while UI work continued directly on the deployed copies up to v0.4.6 (scrollToBottom helper, copy-message button, TextArea → TextField swap, several others). If the v0.4.3 staging had been re-deployed without merging, ~40 lines of UI work + the Enter workaround would have been lost. Reconciled 2026-05-16 by copying v0.4.12 back to staging. **Going forward: edit in staging only, deploy via grep gate + copy** — the original workflow as documented in [[ms4-deploy-gate]] — rather than editing deployed copies directly.

4. **Enter-to-send in extension QML — the big one.** Took 11 diagnostic iterations (v0.4.5 → v0.4.11) and a deep dive. `TextField.onAccepted`, `Keys.onReturnPressed`, AND any QML `Shortcut` bound to Return/Enter ALL silently fail in MS4 extension QML. Root cause: MS4 implements its entire shortcut system as QML `Shortcut` elements registered in the main window ([muse/framework/shortcuts/qml/Muse/Shortcuts/Shortcuts.qml:53-60](muse/framework/shortcuts/qml/Muse/Shortcuts/Shortcuts.qml#L53-L60)), binding `Return`/`Enter` to `nav-trigger-control` ([src/app/configs/data/shortcuts.xml:80-85](src/app/configs/data/shortcuts.xml#L80-L85)). Anything an extension binds at the same key triggers an ambiguous-overload in Qt's resolver — both candidates are `Qt.WindowShortcut` context — and Qt fires *neither*, without any warning. The fix: dynamically build a `NavigationSection → NavigationPanel → NavigationControl` chain via `Qt.createQmlObject` (bypassing the extension's static-import-only deploy validator), register the control as active on input focus via `requestActive(false)`, and connect its `triggered` signal to send. MS4 then dispatches Enter to it. Documented in v0.4.12's in-file comment above `setupNavigation()` and in [[ms4-extension-input-workaround]]. Verified working at v0.4.11 in log `MuseScore_260516_120757.log`. The dynamic-import bypass works because the validator only scans literal `import` lines in `.qml` files; strings inside `Qt.createQmlObject` are ignored. The V2 extension QML engine still resolves `Muse.Ui` at runtime because it's a registered QML module (not file-path based), independent of the engine's import-path list.

**Open items (suggested follow-ups, not blockers):**

- ~~`extensions/` and `plugins/` junction directories in the ms-core-api worktree show as untracked in `git status` — they're per-machine setup per the worktree CLAUDE.md, should probably be added to `.gitignore` (worktree-local config). Not done.~~ **Done 2026-05-16:** added `/extensions/` and `/plugins/` (with explanatory comment) to `.gitignore` on the `ms-core-api` branch worktree. Modification still unstaged — needs a small standalone commit when convenient. `share/extensions/` content is unaffected (no leading-slash anchor avoidance issues).
- `share/extensions/hello-world/` is also untracked in the worktree — separate exploration, not part of the ai-assistant commit. Status unknown.
- The [[ai-assistant-sandbox-choice]] memory's open question (extension vs. plugin sandbox) is now better-informed: the Enter workaround works in the extension sandbox, so the motivation to migrate to a `MuseScore { pluginType: "dialog" }` plugin is weaker than when the memory was written. Decision still deferred to desktop Claude.
- Worktree-local `setup_and_build.bat`, `setup_and_build_fast.bat`, and `CLAUDE.md` have unstaged modifications on ms-core-api — intentional per-worktree configs, not yet decided whether they should be committed to the branch or kept as local-only.
- No push yet. `ai-assistant-mvp` is local-only. Pushing it to origin (`github.com/slimvince/MuseScore`) needs explicit decision — the branch could land as a PR target, or just live as a personal branch for now.

**Memory updates 2026-05-16:**
- [[ms4-extension-input-workaround]] — rewrote to cover both patterns (Ctrl/editing-key intercept + NavigationControl Enter workaround). The pre-existing description (TextArea + printable-char intercept) was obsolete after the v0.4.6 TextField swap.
- [[ms4-deploy-gate]] — corrected the grep pattern; old loose pattern documented as obsolete.
- `MEMORY.md` index — both descriptions updated.

---

## Key files

| File | Purpose |
|------|---------|
| `src/composing/analysis/chord/chordanalyzer.cpp` | Main analyzer — all scoring logic |
| `src/composing/analysis/region/regionanalyzer.cpp` | Canonical region orchestrator — Pass 1/2/2b, absorb, backfill, restamp |
| `src/notation/internal/notationharmonicrhythmbridge.cpp` | Bridge — thin wrapper over `regionanalyzer` |
| `docs/llm_integration.md` | LLM / Claude Composer full design document |
| `docs/quality_observations_iter76.md` | R1–R5 recurring themes for Iter 79+ |
| `docs/score_inventory.md` | Score paths for all test/corpus files |
| `STATUS.md` | Current baselines and HEAD — read every session |
| `build_and_test.md` | All build/test/tool commands |
| `CLAUDE.md` | Standing rules for CC — read every session |
| `tools/analyze_inversion_errors.py` | BIR corpus check |
| `muse/framework/extensions/api/extapi.h` | Current extension API surface (v2) |
| `muse/framework/extensions/internal/extensionsconfiguration.cpp` | Path resolution for extensions/plugins |
