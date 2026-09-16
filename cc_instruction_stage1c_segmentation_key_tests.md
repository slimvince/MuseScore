# CC Instruction: Stage 1c — Pin segmentation passes, harmonicsegmenter, keyresolver

## Context

Master plan: `docs/implementation_roadmap.md` Stage 1, items **1.3** (segmentation-pass
tests) and **1.4** (harmonicsegmenter + keyresolver tests). Same philosophy as 1a/1b
(`757efa5dbf`, `6101a9b2c5`): **pin CURRENT behavior** — these are the differential
baselines for Stage 3 (decoder; segmentation hypotheses) and Stage 4 (key HMM path,
which will rebaseline exactly the keyresolver behaviors you pin here).

Mandatory reads: STATUS.md header; `cc_stage1b_report.md` §1.7 (fixture strategy
precedent); `src/composing/analysis/region/regionanalyzer.{h,cpp}` (passes under test);
`src/composing/analysis/harmony/harmonicsegmenter.{h,cpp}`;
`src/composing/analysis/key/keyresolver.{h,cpp}` + `keymodeanalyzer.h` (types);
`docs/key_detection_baroque_partial_signature.md` (the `81978321e3` fix you will pin);
the Step-3 findings in `docs/redesign_plan.md` ("Step 3 — Key-as-distribution ⛔
SHELVED": `promoteWinnerInPlace` re-ranks WITHOUT recomputing `normalizedConfidence` —
pin that exact behavior).

**Hard constraints (unchanged from 1a/1b):**
- **Tests only. Zero production-code changes.** The `chordanalyzer.h:402–409` stale
  doc-comment residual is NOT part of this run (it rides with Stage 2's first code
  commit). If a function under test is file-local and unreachable through any public
  entry, do NOT re-expose it — test through the public caller, or NOT-PINNED with
  reason.
- **Pin current behavior as-is**; questionable behavior → Findings, not fixes.
- **Scope valve** (1b precedent): explicit NOT-PINNED list beats a stalled session;
  no weakened assertions.
- Suites stay green: 487 composing (+ yours) · 52 notation · 11 snapshots; no BIR run
  (state why in the report).
- Fixtures: prefer direct construction of region/tone/pitch-context inputs. If a pass
  genuinely needs score input, generate MINIMAL musicxml fixtures (a few KB, committed
  next to existing test data per the conventions in `src/composing/tests/`) — list each
  new fixture file in the report. No corpus-score copies.

## Task 1 — Survey (deliverable, 1b-style)

1. **Segmentation inventory**: from `regionanalyzer.cpp`, document the exact pass order
   and semantics: Pass 1 (greedy boundaries + inline same-root merge + sparse-admission
   retry), Pass 2 (onset-Jaccard sub-boundaries), Pass 2b (bass-movement iterations,
   `kMaxBassMovementPasses`), `coalesceShortSameRootRuns` (run length ≥ 3, ≥ 720 ticks,
   predecessor-root check), `absorbShortRegions` (root-agnostic, < kMinRegionTicks),
   `backfillNextRootPc`, `restampBassMinorSeventhAfterMerge` — entry conditions, order,
   and which operate on committed identities vs raw tones. Note public vs file-local.
2. **harmonicsegmenter inventory**: `fillGap` Round 1 (head/tail synthesis) vs Round 2
   (relaxed sparse scoring), where `ScoringPhase::Segmentation` is set, and what
   `greedyExpandSegmentation` commits.
3. **keyresolver inventory**: `resolveKeyAndModeRanked` ranking, `promoteWinnerInPlace`
   (hysteresis/declared-mode promotion WITHOUT confidence recompute), the
   partial-signature mechanism from `81978321e3`, and the piece-start shortcut
   (ARCHITECTURE.md §5.2: tick < 16 beats + no prior + declared mode → confidence 0.5).
4. Grep existing coverage first (keymodeanalyzer_tests.cpp is 985 lines — what does it
   already pin? notation tests may cover stabilization): report, don't duplicate.

## Task 2 — Segmentation-pass tests (roadmap 1.3)

New file `src/composing/tests/regionanalysis_tests.cpp` (or split if cleaner — your
call, document it). Minimum coverage, current-behavior pins:

1. **absorbShortRegions**: short region absorbed into predecessor REGARDLESS of root
   (pin the root-agnostic semantics explicitly — it's a documented Stage-3 concern);
   boundary at kMinRegionTicks (bracket pair); first-region edge case (no predecessor).
2. **coalesceShortSameRootRuns**: fire (≥ 3 consecutive contiguous same-root
   sub-regions, ≥ 720 ticks total, predecessor-root check passes); non-fire for run
   length 2 (boundary), differing roots, and the predecessor-root check blocking.
3. **Inline same-root merge (Pass 1)**: same root + same quality + contiguous merges;
   quality difference or gap blocks. Pin the interaction the Phase-D investigation
   documented: the merge fires when rcb makes consecutive arpeggio slices pick the same
   root (if reachable with constructed input; else NOT-PINNED with reason).
4. **Pass 2 / Pass 2b boundary detection**: one fire + one non-fire each — Pass 2b's
   `minGapTicks = 960` floor is the key pin (no micro-splits); `kMaxBassMovementPasses`
   cap if cheaply reachable.
5. **Sub-region context facts** (audit Finding 4): sub-regions always get
   `bassIsStepwiseToNext = false` — pin it (it's load-bearing context for Stage 3).

## Task 3 — harmonicsegmenter tests (roadmap 1.4a)

1. `fillGap` Round-1 vs Round-2 behavior: one case each where the round produces a
   region, plus the Segmentation-phase guarantee: exploration calls run with
   `prefs.scoringPhase == Segmentation` (observable: a fixture where a Final-phase-only
   signal would change the boundary — if too contrived, pin via the prefs plumbing
   instead and say so).
2. If `fillGap`/`greedyExpandSegmentation` are not callable in isolation, drive the
   smallest public entry that reaches them and pin observable boundary output.

## Task 4 — keyresolver tests (roadmap 1.4b)

1. **Ranked output**: `resolveKeyAndModeRanked` returns a ranked list; rank-0 equals
   what `.front()` consumers get; list is score-ordered.
2. **promoteWinnerInPlace hysteresis**: a case where promotion changes rank-0 — and pin
   the documented wart: `normalizedConfidence` is NOT recomputed after promotion
   (Step-3 finding: 0.025–1.00 spread on a correctly-keyed piece). This pin is the
   Stage-4 rebaseline anchor.
3. **Partial-signature fix (`81978321e3`)**: signature-flexible tonic candidate wins on
   a Baroque partial-signature input (the doc's canonical shape: C-minor music under a
   2-flat signature must resolve C minor, not G minor). Pin both the fixed case and one
   case where signature proximity still correctly dominates.
4. **Piece-start shortcut**: tick < 16 beats + no prior result + explicit key-sig mode
   → declared mode at confidence 0.5; and the insufficient-data fallback
   (`distinctPitchClasses < 3`).
5. Check what keymodeanalyzer_tests.cpp already pins (Task 1.4) — only add what's
   missing at the RESOLVER layer (ranking/promotion/shortcut), not the analyzer's
   scoring internals.

## Task 5 — Register, build, run

CMakeLists registration; standard loop:
```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe > /tmp/s1c_compose.txt 2>&1; echo "exit:$?"
tail -5 /tmp/s1c_compose.txt
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe > /tmp/s1c_notation.txt 2>&1; echo "exit:$?"
tail -5 /tmp/s1c_notation.txt
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe > /tmp/s1c_snap.txt 2>&1; echo "exit:$?"
tail -10 /tmp/s1c_snap.txt
```
Expected: all green, zero snapshot diffs.

## Report — `cc_stage1c_report.md`

1. Survey inventories (segmentation, segmenter, keyresolver) — Stage-3/4 design feed.
2. Test inventory table (test → behavior pinned).
3. NOT-PINNED list with reasons.
4. Findings (pinned-but-questionable — especially anything about absorb/coalesce
   ordering interactions and the confidence wart's actual observed values).
5. Existing-coverage notes; new fixture files if any.
6. Counts + single-commit proposal (tests + CMakeLists + any small fixtures), awaiting
   Cowork confirmation:
   ```
   test: pin segmentation passes, harmonicsegmenter, and keyresolver (Stage 1c)

   Unit tests for absorbShortRegions (root-agnostic absorption), inline
   same-root merge, coalesceShortSameRootRuns, Pass 2/2b boundary detection
   (minGapTicks floor), fillGap rounds + Segmentation-phase plumbing, and the
   keyresolver (ranked output, promoteWinnerInPlace without confidence
   recompute, 81978321e3 partial-signature fix, piece-start shortcut).
   Differential baseline for Stage 3 segmentation and Stage 4 key-path work
   (implementation_roadmap.md 1.3, 1.4). Production code untouched.
   ```

Stop conditions: production change seemingly required; crash; doc/code contradiction at
sync-rule level; a fixture needing more than a few KB of score data.
