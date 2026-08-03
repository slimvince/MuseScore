# Iteration Path 1 — Closing Summary

> **Status: ITERATION-ERA RECORD (path 1).** Two of its rules are standing and registered — gates
> read structured fields only (D-280) and the batch measurement tool must emit the structured fields
> on every alternative (D-281); its commit-timing lesson is reconciled by the dated annotation at
> :112-130. Not a current plan.
>
> *Banner ratified by the user, 2026-08-03 — drafted at phase 1j, presented at
> `ratification_surfaces/cowork_pending_ratifications_next_session.md` §1, applied at phase 1k. It makes this document a
> contract home for D-280 and D-281 (the fifth home case, `CLAUDE.md` decisions-register rule (g)).
> Anchor note, not part of the ratified text: the banner's ":112-130" was written against the
> pre-banner line numbers, and inserting the banner shifted the commit-timing lesson and its dated
> annotation down to **:125-142**. The ratified wording is left exactly as ratified rather than
> silently corrected; the true anchor is here.*

## Scope

Incremental improvement of the chord analyser in `src/composing/` via diagnostic
iterations, gate additions, and scoring-architecture changes. Approximately 49
iterations from the initial post-§4.1b audit through baseline restoration.
All changes were vertical-analysis improvements layered on the existing
`RuleBasedChordAnalyzer`: no replacement of boundary detection, no contextual
harmony layer, no model-based scoring.

The path was declared complete at commit `5df8421114` (2026-05-10) when the
residual error clusters had each been individually characterised and shown not
to be further reducible without an architectural change.

## Total error reduction

Baseline taken from the first fresh Baroque-preset corpus measurement after the
counting methodology stabilised (commit `8f889a01e6`, 2026-05-05). Counts are
genuine errors against the Bach-chorale corpus (353 chorales, Baroque preset).

| Metric | Start | End | Δ |
|---|---|---|---|
| BIR=true (two-way `chord_disagree` ∩ bassIsRoot=true) | 111 | **21** | −90  (−81 %) |
| BIR=false (two-way `chord_disagree` ∩ bassIsRoot=false) | 788 | **128** | −660 (−84 %) |
| Jazz BIR=false (hard-stop reference, ≤ 75) | — | **20** | well within hard-stop |

**Methodology note:** Part of the BIR=false reduction (788 → 177) comes from the
Iter 36 counting-methodology change — emitting structured fields on alternative
entries activated the `_matches_alternative` reclassification that moves
`chord_disagree` regions where music21 matches our 2nd/3rd candidate into the
`near_agree` bucket (genuine partial successes, not uncounted failures). The
remaining 177 → 128 drop is from the Iter 46 scoring extension and was real
code-driven improvement. Both reductions are valid against the documented
methodology; they are not double-counted.

## Key milestones

| Iter | Commit | Change | Δ BIR=true | Δ BIR=false |
|---|---|---|---|---|
| 21 | `7435bdf6e3` | Gate G-E rawCandidates fallback — reach HalfDim suppressed by temporal context | −27 | (BIR=false counts not isolated; included in pre-Iter-36 methodology) |
| 25 | `a74f26aeeb` | Gate I — prefer diatonic first-inversion (I4) over root-position Minor | −18 | — |
| 30 | `369e28e634` | Gate K — Augmented I4 rooting (A+→F#5/A pattern) | −1 | — |
| 32 | `7d8ab7517e` | Gate L — Augmented root-pos → same-root Major (TYPE-A) | −4 | 0 (787) |
| 36 | `5df8421114` (recovered) | batch_analyze emits structured alternative fields → activates `near_agree` reclassification | (methodology change) | −610 (787 → 177) |
| 46 | `36bf4738a8` | Scoring — extend inversion bonuses to Augmented and HalfDiminished | −11 (32→21) | −49 (177→128) |

Iter 46 is the single largest code-driven improvement. Iter 36 is the single
largest methodology improvement.

## Architecture decisions made during this path

1. **Scoring**: `supportsContextualInversionBonuses` and
   `qualifiesForCompleteTriadInversionBonus` extended to include Augmented and
   HalfDiminished quality types, putting their inversion candidates on equal
   footing with Major/Minor (Iter 46, `36bf4738a8`). See ARCHITECTURE.md
   §4.1g.

2. **Boundary detection deprecated**: `detectHarmonicBoundariesJaccard` is
   confirmed at its parameter optimum (threshold 0.60) and slated for
   replacement (Task #62 — iterative greedy-expand with preset-controlled
   stopping threshold). Parameter sweep in Iter 48/48b/48c exhausted the
   threshold; 0.50 regresses both BIR counts. See ARCHITECTURE.md §4.1g
   "Deprecated algorithm".

3. **batch_analyze output schema**: `batch_analyze.cpp` must emit
   `rootPitchClass`, `bassPitchClass`, `quality`, `bassIsRoot` on every
   alternative entry. This activates the previously-dormant
   `_matches_alternative` reclassification in `compare_analyses.py` and is the
   floor below which corpus measurements revert to pre-Iter-36 counts (~700
   BIR=false). Committed in Iter 36 (recovered in `5df8421114` after a git
   reset lost the original commit).

4. **Gates operate on structured fields only**: no chord-symbol string parsing,
   no Roman-numeral inference. This is now a standing rule for any future gate
   or scoring change. Symbol- and Roman-numeral-derived signals are too lossy
   and too entangled with the formatter to be reliable inputs to chord
   classification.

5. **Gate thresholds are Baroque-calibrated**: gates I/K/L thresholds
   (`0.45`/`0.20`/`0.35`) must not be loosened to accommodate other styles.
   Both corpus presets (Baroque and Jazz) must pass BIR=false regression
   before any gate change is committed. Documented in CLAUDE.md and
   BUILD_AND_TEST.md.

## Genuine-21 residual

The 21 remaining BIR=true errors do not have viable gates at this architecture.

- **Gate M cluster (7)**: Minor winner, correct = Diminished or HalfDiminished.
  Iter 47 diagnostic showed no temporal signal reliably separates genuine from
  false-positive at viable thresholds. Blocked.
- **Cluster A (7)**: Minor6 ↔ HalfDim 1st-inversion enharmonic pair. 5/7
  cases the correct alternative is absent from `results[]` even after Iter 46
  — a candidate-generation gap. 2/7 cases have an FP rate of 9:2 at all viable
  thresholds. Blocked.
- **Power / Suspended (4)**: not fully diagnosed; deferred to natural
  calibration during Task #62.
- **Edge cases (2–3)**: individually examined; no shared pattern.

See ARCHITECTURE.md §4.1g for the per-cluster table.

## Process lessons

- **Always build fresh before measuring.** Verify binary timestamp > source
  timestamp. The Iter 36 recovery work surfaced because a stale binary held
  the documented baseline while the fresh build did not. CMake/ninja sometimes
  skips relinks even when relevant headers change; touching the source file or
  inspecting `ls -la ninja_build_rel/batch_analyze.exe` is the only reliable
  check.

- **Commit all changes that affect BIR metrics immediately.** Never leave
  pipeline-affecting changes in the working tree uncommitted across sessions.
  The Iter 36 change to `batch_analyze.cpp` was lost to a `git reset --hard`
  three weeks before being detected, and only the documented baseline (held
  in a binary in `ninja_build_rel/`) made the loss visible at all.

  > **Annotation, 2026-08-02 (user-ruled, `OPEN_ITEMS.md` OI-269).** This lesson
  > is about **what a commit must contain**, not about **when to commit**. Read it
  > as: *in the commit the user asks for, nothing pipeline-affecting is left
  > behind.* A session does not decide on its own judgment to commit — `CLAUDE.md`
  > Conventions states the standing rule, "Commit only when explicitly asked", and
  > that rule governs the timing. The two do not conflict once the lesson is read
  > as a rule about commit content: the user decides that a commit is made; this
  > lesson decides what goes into it. The failure the lesson records is not in
  > dispute and is the recorded defense of register entry **D-281** — a change to
  > the measurement tool was lost to a hard reset and went undetected for three
  > weeks, visible only because a stale binary still held the documented baseline.
  > The lesson's original text above is preserved unchanged.

- **The §2.10 duplication is a persistent source of divergence risk.**
  `detectHarmonicBoundariesJaccard` exists in both
  `notationcomposingbridgehelpers.cpp` and `tools/batch_analyze.cpp` with
  separate signatures and overlapping but not identical logic. Consolidation
  (Task #58) is a prerequisite for Task #62; the replacement algorithm must
  not introduce a second §2.10 violation.

- **Run the Jazz corpus too.** Several promising gate ideas regressed in Jazz
  even when Baroque improved. The Jazz BIR=false ≤ 75 hard-stop caught these
  before commit; this discipline should carry into path 2.

- **Threshold tuning has a sharp ceiling.** Three iterations (48/48b/48c) on
  the Jaccard threshold confirmed 0.60 is the local optimum. Further gains
  require an algorithm change, not a parameter change.
