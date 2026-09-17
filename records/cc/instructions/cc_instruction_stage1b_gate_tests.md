# CC Instruction: Stage 1b — Pin gates A–L, Iter 86/91/pedal, and the fixed-bug cases

## Context

Master plan: `docs/implementation_roadmap.md` Stage 1, items **1.1** (gates A–L unit
tests) and **1.5** (pin historically fixed bugs). Same philosophy as Stage 1a
(`757efa5dbf`): **pin CURRENT behavior** — these tests are the per-gate proof obligations
for the Stage 3 decoder migration (roadmap 3.4 retires gates one at a time only when the
decoder reproduces their pinned fixes).

Mandatory reads first: STATUS.md header, `docs/scoring_model.md` §6 (gate table) + §7
(inversion correction / pre-sort capture) + §4 (Gate J/R context),
`src/composing/tests/test_helpers.h` (`analyzeWithGates` — the production call order),
`src/composing/tests/functionlayer_tests.cpp` (Stage 1a fixture style),
`chordanalyzer.cpp` `applyPostScoringGates()` + `applyIter8691Pedal()` (the code under
test — survey before writing).

**Hard constraints (same as 1a):**
- **Tests only. Zero production-code changes.** Allowed: new/extended test files under
  `src/composing/tests/` + its CMakeLists.txt. If a gate is untestable without a
  production change (e.g. needs a symbol re-exposed), stop and ask.
- **Pin current behavior as-is**, including anything that looks wrong — flag it in the
  report (`// pins current behavior — see cc_stage1b_report.md §Findings`), don't fix it.
- Suites stay green: 439 composing (+ yours) · 52 notation · 11 snapshots. No BIR run
  (production binary untouched) — state this in the report.
- **Scope valve:** this is the largest Stage-1 batch. If fixture complexity for a
  specific gate explodes (more than ~1 hour of fighting one fixture), pin what you can,
  list the gate as NOT-PINNED in the report with the reason, and move on. An explicit
  gap list is worth more than a stalled session. Do not half-pin (no weakened assertions
  just to go green).

## Task 1 — Survey (before any test)

1. Read `applyPostScoringGates()` and `applyIter8691Pedal()` end to end. Produce (for
   the report) the definitive gate inventory with: trigger conditions, margin constants,
   preset flags (`preferMinorOverMajorAdd6` etc.), and execution ORDER — including which
   gates are mutually exclusive (early-exit / `enharmonicFlipDone`-style flags) and which
   can chain.
2. Establish the fixture strategy: tests should go through `analyzeWithGates()` (real
   production order) with constructed `ChordAnalysisTone` vectors + `ChordTemporalContext`
   wherever possible. Constructing `PostScoringGateContext` by hand is the fallback —
   document which gates needed it. Use real preset preferences (read which presets set
   `preferMinorOverMajorAdd6`) and pin BOTH branches where a gate is preset-gated.
3. Grep existing tests first — some cases may already be pinned (don't duplicate):
   ```
   grep -rn "bwv103\|bwv310\|bwv110\|Em/C\|Am7b5\|originalWinner" src/composing/tests/ | head -20; echo "exit:$?"
   ```
   Report what already exists; skip duplicates.

## Task 2 — Gate tests (roadmap 1.1)

New file `src/composing/tests/postscoringgates_tests.cpp` (follow 1a style: §-rule
comment per test, EXPECT_NEAR 1e-9, helpers in anonymous namespace). Per gate, minimum:
one **fires** case, one **must-not-fire** case, and for margin-gated gates a **boundary
bracket pair** (just-inside / just-outside, like 1a's 0.80/0.78 pattern — avoid exact
FP equality on computed thresholds):

| Gate | Key conditions to pin (from §6 — verify against code in Task 1) |
|---|---|
| Bias correction | margin < `inversionSuspicionMargin` (0.70) bracket; `distinctPcs >= 3`; seventh-exemption |
| A–D (MajorAdd6→Minor) | the enharmonic fast path; FM2 rawCandidates fallback; B (forward evidence), C (3-region window), D (≥2 consecutive stepwise) — one fire each + the no-temporal-evidence non-fire |
| E | Minor winner, Major alt at (root+8), stepwise bass |
| F | Major alt at (root+5), stepwise bass |
| G-E | key-function gate (viiø7/iiø7/iiiø7) + the rawCandidates pull-in when the HalfDim alt is missing |
| G-B/C/D | one representative fire (temporal mirrors of B/C/D — if fixtures are near-copies, one fire + one non-fire for the family is acceptable; say so) |
| H | Augmented rotation, alt at (root+4)/(root+8), temporal gates |
| I | margin ≤ 0.45 bracket; root-diatonic condition |
| J | complete dim triad + M3-below sounding above extensionThreshold → V7 swap; non-fire when triad incomplete (the dim7-completeness guard) |
| K | margin ≤ 0.20 bracket; diatonic condition |
| L | margin ≤ 0.35 bracket; same-root same-bass condition |
| Iter 86 | bass-at-b7 → MinorSeventh stamp (Am/G → Am7/G) + a non-fire |
| Iter 91 | Pattern A (Minor, delta 8) and Pattern B (Major, delta 9) with `nextRootPc == bassPc`; non-fire without forward context |
| Pedal two-pass | bass non-chord-tone + confident upper-voice chord → `isPedalPoint` swap; non-fire when bass IS a chord tone |

Also pin one ORDERING fact (high value for Stage 3): a fixture where the bias-correction
sort changes `results[0]` and a later gate still keys off the pre-sort winner — i.e. the
**Sub-9a `originalWinnerRootPc` capture** (scoring_model §7: Cm6 → Am7♭5/C promotion →
Gate G-E must compute `gExpectedAltRoot` from the ORIGINAL root 0, not the promoted 9).
This doubles as the Sub-9a pin for Task 3.

## Task 3 — Pin the fixed-bug cases (roadmap 1.5)

Prefer minimal synthetic fixtures over adding score files; the mechanisms are precisely
documented. If a case genuinely needs its score and the score is not in the test data,
list it as NOT-PINNED with the reason (do not add multi-MB scores without asking).

1. **Gate J / bwv110.7 m10**: tones {C#, E, G + sounding F# below extensionThreshold?
   — per §4: complete dim triad on C# with F# (M3 below) sounding} → winner must be the
   F#7 reading (V6/5), not C#dim. Removing-the-fix expectation: documented in a comment.
2. **Sub-9a capture**: covered by the Task-2 ordering test (cross-reference it).
3. **Δ=+7b trio mechanism (Gate R end-to-end)**: gater_tests pins the predicate; add ONE
   end-to-end case through `analyzeWithGates`: predecessor root continuing into a region
   where the continued-root candidate's bass is a M6 above it (bass = M3 of the true
   root), basisDep == 0 → the first-inversion-of-true-root reading must win (the
   bwv245.28/296/320 shape: B/G♯→E, D/B→G, G/E→C — pick one, document the mapping).
4. **Iter 92 / bwv103.6 (passing low note loses bass selection)** and **bwv310 (C major
   beats Em/C via w_complete + joint scoring)**: check Task-1 grep first — if catalog
   tests already pin these, cross-reference and skip; otherwise synthesize (bwv310's
   shape is documented in §4 w_complete; bwv103.6 needs onset evidence —
   `onsetAtRegionStart` true/false mix).

## Task 4 — Register, build, run

Add the new file to `src/composing/tests/CMakeLists.txt`.
```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe > /tmp/s1b_compose.txt 2>&1; echo "exit:$?"
tail -5 /tmp/s1b_compose.txt
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe > /tmp/s1b_notation.txt 2>&1; echo "exit:$?"
tail -5 /tmp/s1b_notation.txt
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe > /tmp/s1b_snap.txt 2>&1; echo "exit:$?"
tail -10 /tmp/s1b_snap.txt
```
Expected: all green, zero snapshot diffs, no goldens touched.

## Report — `cc_stage1b_report.md`

1. **Survey:** the definitive gate inventory (order, conditions, margins, preset flags,
   mutual-exclusion structure) — this section is a deliverable in itself; scoring_model
   §6 will be reconciled against it in the next doc pass (note discrepancies, change no
   docs in this run).
2. **Test inventory:** table test → gate/rule pinned (1a style).
3. **NOT-PINNED list:** any gate/case skipped under the scope valve, with reasons.
4. **Findings:** behavior pinned-but-questionable (the Stage-3 feed).
5. **Existing-coverage notes:** what Task-1 grep found already pinned.
6. **Counts** and **commit proposal** (single commit, tests + CMakeLists only; do not
   commit until Cowork confirms). Suggested message:
   ```
   test: pin post-scoring gates A-L, Iter 86/91/pedal, and fixed-bug cases (Stage 1b)

   Per-gate fire / non-fire / margin-boundary tests through the production
   analyzeWithGates order, incl. the Sub-9a originalWinnerRootPc pre-sort
   capture, Gate J vii->V7 completion (bwv110.7 shape), the Gate R Delta=+7b
   end-to-end shape, and Iter 92 joint-bass cases. Differential baseline for
   the Stage 3 decoder migration (implementation_roadmap.md 1.1, 1.5).
   Production code untouched.
   ```

Stop and ask if: a production change seems required, a test exposes a crash, the §6 gate
table materially contradicts the code (sync-rule decision), or score files would need to
be added to the repo.
