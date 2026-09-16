# CC Instruction — Scoring model documentation + code annotation

**Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only),
`C:\s\MS\build_and_test.md`

**Current state:** Branch `master`, HEAD `945a9e2f18`, **working tree clean.**
BIR baselines (lenient-OR): Baroque BIR=true=28, BIR=false=16; Jazz BIR=true=36,
BIR=false=10. Tests: 407/407 composing, 52/52 notation, 11/11 snapshot (1 skipped).

**This instruction makes NO logic changes.** Every edit is documentation only —
comments in source files and a new reference document. No executable behaviour changes.
No build or test run is needed (no .cpp logic touched). Commit at the end.

---

## Motivation

Three consecutive template-addition attempts (B1, B2 ×4 attempts, B3) were slowed by
incomplete understanding of existing scoring mechanics. In the B3 case, CC "discovered"
mid-task that `dim7CharacteristicBonus` is a rotation-selection mechanism (not just a
score offset) because its non-diatonic ♭♭7 check was undocumented. This cost a full
revert cycle. The root cause: implementation context lives in the code; handoff docs
capture outcomes; nothing explains *how the scoring pipeline works as a system* or
*why each term exists*.

Fix: write a comprehensive scoring-model reference document AND annotate the code so
that even a reader who skips the doc cannot miss the design rationale.

---

## Part A — Read the full scoring pipeline first

Read `src/composing/analysis/chord/chordanalyzer.cpp` in full, focusing on:

1. `analyzeChord` — the main scoring function:
   - The templates array definition (all 17 entries, their intervals and score offsets)
   - The (rootPc, tplIdx) inner loop: how `basisIndepMatrix`, `complexityFactorMatrix`,
     and `augFactorMatrix` are computed
   - Every bonus/penalty term and its gate conditions:
     - `dim7CharacteristicBonus` (rotation-selection mechanism — the B3 lesson)
     - `rootContinuityBonus`
     - `w_complete`
     - `w_stepIn` / `w_stepOut`
     - `wSeqBonus`
     - `wDimBonus`
     - The B2 aug7 guard
     - The B3 dim7 guard (not present — but the bonus guard IS)
   - The joint (bass, root, template) scoring enumeration
   - The post-scoring candidate ranking

2. The post-scoring gates (Gates A through L — wherever they appear after the main
   scoring loop)

3. The inversion-correction `stable_sort` block (source of the Sub-9a stale-reference
   bug — `originalWinnerRootPc` capture context)

4. `diagnoseChord` — note where it mirrors `analyzeChord` and where it diverges

Also read `src/composing/analysis/chord/chordanalyzer.h` for the struct definitions
(`TemplateDef`, `ChordTemporalContext`, `ChordAnalyzerPreferences`, `ChordQuality`)
that the scoring pipeline depends on.

Do not begin writing until you have read the whole pipeline.

---

## Part B — Write `docs/scoring_model.md`

Create `C:\s\MS\docs\scoring_model.md`. This is a technical reference for the
chordanalyzer scoring pipeline. CC should read it at the start of any session that
touches scoring logic in `chordanalyzer.cpp`.

### Required sections (use these exact headings):

**1. Overview**
One-paragraph summary of the pipeline: tone collection → template scoring →
post-scoring gates → inversion correction → output. State the key design constraint:
the analyzer is purely bottom-up (pitch evidence → chord symbol); no harmonic function
reasoning is performed here (that is Phase E).

**2. Templates**
For each of the 17 `TemplateDef` entries in the `analyzeChord` array:
- Quality, intervals (pitch class offsets from root), score offsets
- What chord it represents (e.g. `{0,4,8,10}` = C7♯5, aug dominant 7th)
- Any guard that applies to it (B2 aug7 dual-guard; the dim7 bonus non-diatonic check)

Include a note on the `kDiagTemplates` array in `diagnoseChord` — that it mirrors the
`analyzeChord` array and must be kept in sync, but guards in `diagnoseChord` are
intentionally omitted (diagnostic path only, does not affect production output).

**3. Score matrix structure**
Explain `basisIndepMatrix`, `complexityFactorMatrix`, `augFactorMatrix`: what each
encodes, how they combine, what the final score represents. State that all three are
17-wide (one column per template) and must be updated together when templates are added.

**4. Bonus and penalty terms**
For each term, document: name, value, gate conditions, purpose, interactions, and any
known invariants or "do not remove/simplify" warnings. Cover at minimum:

- **`dim7CharacteristicBonus`** (kDim7CharacteristicBonus = 0.75)
  ⚠ ROTATION-SELECTION MECHANISM — not just a score offset. Gate includes a
  non-diatonic ♭♭7 check that asymmetrically rewards the correct enharmonic root.
  Suppressing or bypassing this bonus breaks dim7 rotation selection (6 Jazz catalog
  failures in the B3 attempt). Do not remove without replacing the rotation-selection
  function.

- **`rootContinuityBonus`** (+0.40)
  Known dead end for sparse predecessors: see Iter 98 and the Δ=+7 cluster in the
  handoff. Suppressing it on sparse predecessors regresses mozart_k280-1 IV→V65
  Alberti-bass contexts. Phase E only.

- **`w_complete`** (+0.50)
  Rewards root-position completeness (all 3 triad tones present). Added in Iter 92
  to fix the slash-chord-beats-complete-triad bug. Gate: distinctPcs≥3, all triad
  tones above extensionThreshold, bass_candidate.pc == triad_root.

- **`w_stepIn` / `w_stepOut`** (+0.10 each)
  Root-position step motion bonuses (Iter 94). Four gates: `explorationMode`
  suppression, root-position guard, first-inversion-m7-family guard, power-quality
  exclusion. Each gate exists to prevent a specific documented regression — do not
  remove gates without understanding the regression they prevent.

- **`wSeqBonus`** (Iter 95)
  Sequential progression signal. Document gate and value.

- **`wDimBonus`** (Iter 96, +0.15)
  Leading-tone resolution signal for dim/half-dim candidates. Gate: jointScoring +
  !explorationMode + nextRootPc >= 0 + (Diminished or HalfDiminished) + distinctPcs≥4.
  The `distinctPcs≥4` gate is intentional: sparse 3-PC dim regions must not flip to
  dim7 via this bonus (B3 lesson: rotation selection requires full dim7 evidence).

- **B2 aug7 guard** (the `||` condition in the scoring loop guard)
  BOTH M3 (rootPc+4) and aug5 (rootPc+8) must be present. M3-only guard was tried
  and reverted (Schumann D-major and Corelli G-major flipped to aug7). The dual guard
  is load-bearing.

- **`explorationMode`** flag (ChordAnalyzerPreferences)
  Set `true` by `greedyExpandSegmentation` for internal boundary-exploration calls.
  Suppresses step bonuses to prevent segmentation bias. Do not remove this flag.

**5. Joint (bass, root, template) scoring**
Explain the enumeration: for each bass candidate, score each (root, template) triple.
Document `bassDependentContextualBonuses`, `hasStructuralBass` (the sparse-upper-
register gate from A4), and the Iter 92 multi-bass enumeration design.

**6. Post-scoring gates (A–L)**
For each gate:
- Name and location (approximate line number)
- Trigger condition
- What it does to the candidate list
- Why it exists (the specific failure pattern it was added to fix)

At minimum: Gates E/I (absent-root guard), Gate J (vii°→V7 completion), Gate G-E
(stale-reference fix — `originalWinnerRootPc` capture, Sub-9a), Gate K/L
(augmented corrections).

**7. Inversion correction**
Explain the `stable_sort` pass that promotes inversion candidates. Note the
`originalWinnerRootPc` capture (introduced in the Sub-9a fix) and WHY it must be
captured before the sort — the Sub-9a root cause was reading `winner.identity.rootPc`
after the sort had already moved Am7b5/C to results[0].

**8. Known constraints and dead ends**
A bulleted list of design constraints that must be respected in future work:
- `dim7CharacteristicBonus` is the dim7 rotation selector — do not suppress without replacement
- `rootContinuityBonus` sparse-predecessor gate is a dead end (Iter 98)
- `w_stepIn`/`w_stepOut` four gates are each load-bearing (each prevents a specific regression)
- `explorationMode` must suppress all context-dependent bonuses
- Template arrays and score matrices must be updated atomically (3 sites: analyzeChord
  array + 3 score matrices + kDiagTemplates)
- B2 aug7 guard requires BOTH M3 and aug5 (M3-only guard was tried and reverted)

**9. How to add a new template safely (checklist)**
A numbered checklist derived from the B1/B2/B3 lessons:
1. Read the existing template nearest to yours — understand its offsets
2. Check whether any existing bonus/penalty term will interact with the new template
   (especially: does any bonus use the new template's quality+size as a key condition?)
3. Check whether the new template's PC set is a subset of a common Baroque progression
   (if yes, a functional guard is required — B1 lesson)
4. Design the guard: what tones must be above extensionThreshold? Check each failure
   case explicitly (enumerate known test chords)
5. Update all 3 array sites atomically: analyzeChord array (size N→N+1), 3 score
   matrices (N→N+1), kDiagTemplates array (N→N+1)
6. Run all three test suites before BIR
7. Run BIR both presets before committing
8. Add a comment in this doc's Templates section for the new entry

---

## Part C — Annotate `chordanalyzer.cpp`

At each of the following locations, add or improve a comment that explains the WHY,
not just the what. The comment should be long enough that a reader who has never seen
the handoff docs understands the design rationale.

**C1 — `dim7CharacteristicBonus` block (at both call sites: ~L2036 and ~L3426)**

Replace or augment the existing comment with:
```cpp
// ROTATION-SELECTION MECHANISM — not just a score offset.
// All four enharmonic rotations of a dim7 chord share the same PC set
// (C°7 = Eb°7 = Gb°7 = A°7). The non-diatonic check on the ♭♭7 PC
// asymmetrically rewards the correct enharmonic root: the ♭♭7 of the
// "true" rotation is non-diatonic in the current key, while the ♭♭7 of
// the three spurious rotations is diatonic (it coincides with a scale tone).
// DO NOT suppress or bypass this bonus without replacing this rotation-
// selection function. Suppressing it breaks 6 Jazz catalog dim7 entries
// (B3 attempt, 2026-06-05).
```

**C2 — `rootContinuityBonus` (+0.40) application**

Add at or near the bonus application:
```cpp
// KNOWN DEAD END (Iter 98, 2026-05-23): suppressing this bonus when the
// predecessor region has distinctPcs <= 2 was tried in two variants and
// both regressed mozart_k280-1 IV→V65 in Alberti-bass contexts. The signal
// is load-bearing for legitimate sparse continuity. Do not attempt a
// density-based or inversion-aware gate here without first reading the
// Iter 98 dead-end section in cowork_handoff.md.
```

**C3 — B2 aug7 guard (in the (rootPc, tplIdx) loop)**

The existing comment is reasonable but ensure it explains the M3-only failure:
```cpp
// B2 guard: BOTH M3 (rootPc+4) AND aug5 (rootPc+8) must be present above
// extensionThreshold. Using M3 alone (|| → &&) was tried and reverted: the
// aug7 template then over-fires on complete major triads containing a minor
// seventh (root+M3+m7 present, aug5 absent) because the large aug5 score
// offset inflates the partial-match score above a complete major triad.
// The || (fire if EITHER is absent) is correct and load-bearing.
```

**C4 — `wDimBonus` lambda (distinctPcs >= 4 gate)**

Add at the gate:
```cpp
// distinctPcs >= 4 is intentional: 3-PC sparse dim regions must not flip
// via this bonus. The bonus is a rotation-correction signal (leading-tone
// dim7 should resolve upward), not a quality-flip signal. Removing this
// gate caused quality flips in 3-PC contexts in Iter 96 testing.
```

**C5 — `originalWinnerRootPc` capture (pre-stable_sort)**

Add at the capture site (near the existing `originalWinnerQuality` / 
`originalWinnerHasAddedSixth` captures):
```cpp
// CAPTURE BEFORE stable_sort — Sub-9a bug (fixed in Gate G-E).
// winner is a reference to results[0]. The stable_sort below may promote
// Am7b5/C (rootPc=9) to results[0], making winner.identity.rootPc=9.
// Gate G-E uses originalWinnerRootPc to compute gExpectedAltRoot — if it
// read winner.identity.rootPc after the sort, it would compute the wrong
// leading tone (e.g. (9+9)%12=6 instead of (0+9)%12=9) and pull in a
// spurious candidate. Capture all three originalWinner* fields here.
```

**C6 — `explorationMode` suppression of context bonuses**

At the first bonus suppressed by `explorationMode`, add:
```cpp
// explorationMode is set true by greedyExpandSegmentation for internal
// boundary-exploration calls (Round 1 head/tail synthesis + Round 2 region
// scoring in harmonicsegmenter.cpp::fillGap). Bonuses that depend on
// neighbouring context (step motion, sequence, continuity) must be
// suppressed here — otherwise they bias sub-region bass selection DURING
// segmentation, before the final per-region scoring pass runs. This was
// caught as a regression during Iter 94 development.
```

**C7 — Template array size declaration(s)**

At each `std::array<TemplateDef, 17>` declaration (analyzeChord and kDiagTemplates),
add a comment:
```cpp
// 17 templates: see docs/scoring_model.md §2 for the full list.
// When adding a template: update BOTH TemplateDef arrays AND all three
// score matrices (basisIndepMatrix, complexityFactorMatrix, augFactorMatrix)
// atomically. Missing the score matrices causes a stack-buffer overrun
// (silent, caught in B1 attempt 2026-06-04).
```

**C8 — Score matrix declarations**

At the three `std::array<std::array<double, 17>, 12>` declarations:
```cpp
// Must stay in sync with the TemplateDef arrays above (same column count).
// Stack-buffer overrun if mismatched — see C7 comment.
```

---

## Part D — Commit

```
cd C:\s\MS && git add \
  docs/scoring_model.md \
  src/composing/analysis/chord/chordanalyzer.cpp; echo "exit:$?"
cd C:\s\MS && git commit -m "docs: scoring model reference + chordanalyzer annotations

Add docs/scoring_model.md: comprehensive reference for the chordanalyzer
scoring pipeline (templates, bonus/penalty terms, post-scoring gates,
inversion correction, known constraints, new-template checklist).

Annotate chordanalyzer.cpp at 8 key sites with design rationale comments:
- dim7CharacteristicBonus rotation-selection mechanism (B3 lesson)
- rootContinuityBonus sparse-predecessor dead end (Iter 98)
- B2 aug7 dual-guard M3+aug5 requirement
- wDimBonus distinctPcs>=4 gate rationale
- originalWinnerRootPc pre-sort capture (Sub-9a fix)
- explorationMode bonus suppression rationale
- Template array + score matrix sync requirement

No logic changes. No executable behaviour changes."; echo "exit:$?"
```

---

## Report back

1. Confirm `docs/scoring_model.md` was created with all 9 sections
2. Confirm all 8 annotation sites (C1–C8) were addressed in `chordanalyzer.cpp`
3. Commit hash
4. Any scoring mechanics discovered during the read that should be added to
   the handoff docs or STATUS.md (flag them — do not update those files yourself)
