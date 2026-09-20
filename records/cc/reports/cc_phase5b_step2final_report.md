# CC — Phase 5b Step 2-final: correct Step 2 (§A) + build the §4 two-reading both-sides inherit (§C)

**Commits (local, unpushed, decoder + tests only — verifiable by sha):**
- **§A — `d52cfd0847`** `fix(composing): L4 Step-2 correction — keep G2/G3 ladder, revert one-sided over-inherit`
- **§C — `4aa88452cd`** `feat(composing): L4 §4 two-reading both-sides inherit — continuation vs transition`

`git show --stat` on each lists exactly three files — `chordslicedecoder.cpp`, `chordslicedecoder.h`,
`decode_chord_tests.cpp`. No production wiring. (The working-tree `cowork_phase5b_l4_build_plan.md` change is the
Step-0 grounded-order doc edit — *not mine*, left uncommitted; `scratch_artifacts/` is gitignored.)

**Method:** §A correct → §B INVESTIGATE-confirm → §C BUILD the §4 two-reading → §D RE-MEASURE → §E gate → §F assess.
Build-it-right per the signed spec (`cowork_layer4_chordsymbol_design.md` §4 / §5 step 4); **no inference-quality
tuning** (the firewall). `upstream` untouched.

---

## TL;DR — the two-reading is the MOST ACCURATE variant and fixes the over-inherit, but it does NOT raise raw coverage → **STOP (do not push to Step 3), declare to Cowork**

1. **§A (commit A) restores the correct "G2-iso" base.** The three-tier membership ladder (G2) + the required-tone
   plausibility check (G3) are correct and accuracy-neutral — **kept**. The Step-2 one-sided note-only inherit
   relaxation is **reverted** to the conservative G1 template-only consistency. Re-measured baseline: among-committed
   **76.9 %**, abstain **55.0 %**, coverage-matched **66.7 %** (Baroque; Default mirrors) — exactly the G2-iso line from
   the Step-2 dossier. Production byte-identical.
2. **§B confirms the two-pass already produces both-side provisional neighbours — the gap was only the missing
   next-chord check.** No structural change beyond the decoder → no STOP.
3. **§C (commit B) builds the §4 two-reading both-sides inherit.** The inherit fallback now gates the
   stepwise-embellishment relaxation on the **next provisional chord**: a thin slice inherits the prevailing chord only
   on a **CONTINUATION** (next provisional == prevailing); a **TRANSITION** (next differs) does **not** inherit — it
   abstains (→ Layer 5). One `analyzeChord` cube; second-reading decision wiring only; **not** the deferred §15-O2 joint
   window.
4. **§D — the two-reading is the MOST ACCURATE of every variant** (best among-committed **77.8 %** AND best
   coverage-matched **68.0 %** — the engage-relevant line — both Baroque and Default), with the **fewest total misses
   (573)** and the over-inherit fixed (thin-slice misses **300 → 61**). **But it does NOT raise raw coverage vs G1 —
   it is MORE conservative** (abstains **58.2 %** vs G1's 53.0 %), because the continuation gate correctly abstains on
   TRANSITION slices that **both** the one-sided **and** G1's own template-only inherit were committing wrongly.
5. **§F — MIXED → STOP.** Per plan §F ("the two-reading raises coverage vs G1 without the one-sided regression →
   proceed; **else, fails to raise coverage → STOP and report**"). The fix is real and the most accurate, but it
   improves accuracy by **more careful abstaining** (handing transitions to L5), **not** by more covering — so the
   §F "raise coverage" condition is not met. **Did NOT push to Step 3.** The sequence/spec decision is Cowork's.

---

## §A — Correct Step 2 (commit A `d52cfd0847`): keep G2/G3, revert the one-sided over-inherit

Reverted the one-sided note-only inherit relaxation (`notesConsistentWithPrevailing` via the ladder) to G1's
conservative **template-only** consistency. **Kept** the G2 three-tier ladder (`stepwiseSignals` / `classifyTone`) and
the G3 plausibility check (the required-tone test in `classifyMembership`) — both accuracy-neutral and correct.
`applyCommitDecision` reverts to the G1 3-arg signature; the six G1 unit-test call sites revert; the one relaxation
test (`G2_InheritsThroughStepwiseNct`) is removed (composing 841 → 840).

**Re-confirmed baseline (held-out TEST, dur-weighted chord-root; the "G2-iso" line):**

| | among-committed | committed dur | abstain | coverage-matched |
|---|---|---|---|---|
| Baroque | **76.9 %** (666960/867720) | 867720 (45.0 %) | **55.0 %** | **66.7 %** (1288080/1929840) |
| Default | **76.9 %** | 867720 (45.0 %) | **55.0 %** | **66.5 %** (1282320/1929360) |

= the Step-2 G2-iso line exactly (the ladder's plausibility re-ranking sits at 55 % abstain, ~2 pts above the original
G1's 53 % — as the Step-2 dossier noted). **Production byte-identical:** Baroque `.ours.json` **353/353 byte-identical**
to the committed `tools/corpus/baroque` (fresh regen + `cmp`), snapshots **11/11** zero-diff, composing **840** /
notation **53**.

## §B — INVESTIGATE-confirm (the two-pass already gives both-side neighbours — no STOP)

Read §4 (the two-reading scheme) + §5 step 4 against the as-built decode (`decodeWindowed` / `finalizeSlice`):

- **Both-side provisional neighbours ARE produced.** `decodeWindowed`'s membership two-pass builds `work[]` = pass-1
  `SliceWork` over `[outFirst-2, outLast+1]`; `pass1ChosenAt(t)` exposes the pass-1 chosen chord at any `t`. Pass 2
  (`finalizeSlice`) already receives `prevC = pass1ChosenAt(t-1)` **and** `nextC = pass1ChosenAt(t+1)`. ✔
- **The gap was ONLY the missing next-chord CHECK.** The Step-2 inherit *did* pass `nextC` to `classifyTone` (as
  stepwise context for the stepOut test), but the inherit **decision** had no continuation-vs-transition gate — it
  inherited whenever the notes were stepwise embellishments of the *prevailing* (left) chord, regardless of whether the
  next provisional chord continued or departed it. (Worse: `classifyTone`'s stepOut sees `nextC`'s chord tones, so a
  note resolving INTO the next chord is *mis-read* as a passing embellishment of the prevailing one — making the
  over-inherit harder, not easier, to catch without an explicit gate.)
- **The §4 inherit with both-side neighbours:** inherit iff the next provisional chord IS the prevailing chord (a
  CONTINUATION — the left side is the prevailing chord by construction) AND the notes are consistent (template tone OR
  stepwise embellishment). A TRANSITION (next differs) does NOT inherit. The function-dependent residual → ABSTAIN (→ L5).
- **Decoder-local — no structural change beyond the decoder, no L5-function for the bulk → no STOP.** This is the §4
  two-reading baseline, **not** the deferred §15-O2 joint window (left deferred).

## §C — BUILD the §4 two-reading both-sides inherit (commit B `4aa88452cd`)

`applyCommitDecision` regains the `(window, prevChord, nextChord)` params; the inherit fallback is:

```
if (!sufficient && prevailing) {
    if (nextChord present)  inherit = sameChordSymbol(nextChord, prevailing)        // CONTINUATION gate
                                      && focalConsistentAsEmbellishmentsOf(prevailing, …);  // G2 ladder
    else                    inherit = allFocalAreTemplateTonesOf(prevailing, focal);  // conservative G1 fallback
}
```

- **CONTINUATION (next == prevailing):** the stepwise-embellishment relaxation fires — the thin slice inherits.
- **TRANSITION (next differs):** does NOT inherit — abstains on its own (insufficient) evidence (→ L5). *This is the
  over-inherit fix.*
- **No next provisional (right boundary / membership / two-pass off):** falls back to the conservative template-only G1
  base (no CONTINUATION can be confirmed).

One `analyzeChord` cube; second-reading decision wiring only; **not** a new scorer and **not** §15-O2.

## §D — RE-MEASURE (the assess checkpoint — two-reading vs the two failure modes + the base)

Same harness as Steps 0–2 (`--decode-chords` over the 353-stem corpus, graded held-out TEST split, dur-weighted =
the granularity-comparable line; graders `cc_layer4_chord_baseline.py` + `cc_layer4_residual_decompose.py`,
committed/unchanged). Decoder is preset-identical Baroque ≡ Default on the chord axis (null-context vertical), so
Default Δ tracks Baroque.

### Chord-root, dur-weighted, Baroque (TEST split)

| variant | among-committed | committed dur | abstain | coverage-matched | total misses |
|---|---|---|---|---|---|
| per-region **legacy** | 73.8 % | (full) | — | 73.8 % | — |
| **G1-conservative** (template-only, no ladder) | 77.0 % | 908040 (47.0 %) | **53.0 %** | 66.9 % | — |
| **G2-iso** (commit A base — ladder + template-only inherit) | 76.9 % | 867720 (45.0 %) | 55.0 % | 66.7 % | 654 |
| **one-sided** (Step 2 — note-only inherit relaxation) | **72.6 %** | 986760 (51.1 %) | 48.9 % | **64.8 %** | **943** |
| **two-reading** (commit B — this) | **77.8 %** | 806280 (41.8 %) | **58.2 %** | **68.0 %** | **573** |

- **Two-reading vs the one-sided regression:** among-committed **+5.2** (72.6 → 77.8), coverage-matched **+3.2**
  (64.8 → 68.0), misses **−370** (943 → 573), thin-slice misses **−239** (300 → 61). **The over-inherit is fixed.**
- **Two-reading vs the G2-iso base (commit A):** among-committed **+0.9** (76.9 → 77.8), coverage-matched **+1.3**
  (66.7 → 68.0), misses **−81** (654 → 573) — **strictly more accurate**, but coverage **−3.2** (abstain 55.0 → 58.2).
- **Two-reading vs G1-conservative:** among-committed +0.8, coverage-matched +1.1 — but abstain **58.2 % > 53.0 %**:
  **raw coverage is LOWER, not higher.**

### Default (preset-agnostic decoder)

Two-reading: among-committed **77.8 %**, coverage-matched **67.7 %** (1305840/1929360), abstain 58.2 % — same
direction and magnitude as Baroque.

### Why coverage falls while accuracy rises

The continuation gate abstains on **TRANSITION** thin slices — and not only the embellishment-NCT transitions the
one-sided wrongly inherited, but **also** the pure-template-tone transitions that **even G1's template-only inherit was
committing**. The measurement confirms those were net wrong (catching them lifts among-committed 76.9 → 77.8 and
coverage-matched 66.7 → 68.0). So the two-reading is more accurate **because** it abstains more — handing genuine
transitions to Layer 5 (spec-faithful: "the function-dependent residual abstains → L5"). A secondary contributor to
the extra abstaining is **consecutive thin slices** (arpeggiated runs) where the *raw pass-1* next provisional is
itself a phantom, so a genuine continuation cannot be confirmed → abstain. That residual is exactly the gap **§15-O2
(the bounded-window joint resolution)** is described to close.

## §E — Gate (all PASSED for both commits)

- **Production byte-identical.** Baroque `.ours.json` **353/353 byte-identical** to committed `tools/corpus/baroque`
  (fresh regen + `cmp`, 0 diffs) for **both** A and B; snapshots **11/11** zero-diff (no goldens refreshed). The
  decoder is referenced only by `batch_analyze --decode-chords`, which "never reaches analyzeScore/analyzeRegions"
  (batch_analyze.cpp: `main()` returns before the production `analyzeScore` call) — confirmed by grep + the source
  comment. **Corpus gate 53/24/53 unchanged** (Default/Jazz follow by the same production-dead, preset-agnostic
  argument).
- **Both suites green.** A: composing **840** / notation **53**. B: composing **844** / notation **53**.
- **New unit tests** (commit B, +4, oracle-asserted): `TwoReading_ContinuationThinSliceInherits` (next == prev →
  inherit); `TwoReading_TransitionThinSliceDoesNotInherit` (next differs, same notes → abstain — the fix);
  `TwoReading_FunctionDependentResidualAbstainsToL5` (share-tone low-margin residual → abstain, competing reading
  carried for L5); `TwoReading_NoNextProvisionalFallsBackToTemplateOnly` (no next context → template-only fallback:
  pure-template thin → inherit, stepwise-NCT thin → abstain).
- **Build green** (only the two pre-existing `C4100` warnings; no new warnings).

## §F — ASSESS (mixed → STOP, do NOT push to Step 3, declare to Cowork)

- **Expected (plan §F):** the two-reading raises coverage vs G1 **without** the one-sided regression → proceed to Step 3.
- **Measured:** the one-sided regression is **fixed** and the two-reading is the **most accurate** variant on **both**
  metrics (best among-committed AND best coverage-matched — the engage-relevant line — both presets), with the **fewest
  misses**. **But raw coverage is NOT higher than G1** — the two-reading is **more conservative** (58.2 % abstain vs
  53.0 %). The "raise coverage" half of the §F expectation is **not** met.
- **→ Per plan §F ("fails to raise coverage → STOP and report") this is a STOP.** I did **NOT** push to Step 3. The
  build (commit B) is correct, byte-identical, green, and committed; the sequence is paused.
- **The sequence/spec question for Cowork (declared, not decided — the firewall):** the two-reading both-sides inherit,
  built exactly per §4/§B, fixes the over-inherit and is the most accurate variant, but it improves accuracy by **more
  careful abstaining** (more L5 hand-off), **not** by more covering. Two readings of the assessment, Cowork's call:
  - **(i) Accept** — the engage-relevant metric (coverage-matched) is the best of every variant and the over-inherit is
    fixed; "best accuracy with more L5 hand-off" satisfies the goal, and the §F coverage prediction was simply about a
    direction the fix happened not to take. → proceed to Step 3 (confidence/open-question, G6).
  - **(ii) §15-O2** — the residual over-abstaining is concentrated on **consecutive thin slices** where the *raw pass-1*
    next provisional is a phantom (a genuine continuation that cannot be confirmed from a single look-ahead). That is
    precisely what the deferred **bounded-window joint resolution (§15-O2)** is described to fix ("once the two-reading
    baseline is built and measured, test whether its per-slice precision falls short of the joint optimum"). The
    two-reading baseline is now built and measured — the prerequisite §15-O2 line 501–502 names. → adopt O2 (strictly
    note-bounded) before Step 3.

  I make **no** call between (i) and (ii) — the engage criteria and the O2 trigger are Cowork's. **No inference-quality
  tuning was applied** to force coverage up (the firewall).

## §G — Deliver

- **Commit A** `d52cfd0847` (corrected G2/G3) then **commit B** `4aa88452cd` (two-reading inherit) — both local,
  unpushed, **decoder + tests only** (verifiable by sha: each `git show --stat` lists exactly `chordslicedecoder.cpp`,
  `chordslicedecoder.h`, `decode_chord_tests.cpp`).
- This report (`cc_phase5b_step2final_report.md`, gitignored).

## §H — Stops honored

- The both-sides inherit needed **no** structure beyond the decoder and **no** L5-function for the bulk → no §B STOP.
- **No production movement** → no leak STOP (353/353 byte-identical ×2, snapshots 11/11, both suites green).
- **Assessment mixed (no raw-coverage gain)** → **STOP honored: did NOT push to Step 3**; reported here + declared to
  Cowork as a sequence/spec decision (accept best-accuracy-via-L5-handoff, or trigger §15-O2). The builds are committed;
  the sequence is paused.
- No `upstream` push; both commits local, unpushed, decoder + tests only.

## Artifacts (gitignored / untracked, under `scratch_artifacts/`)

- Commit-A decode + grade: `corpus_decode_chord_step2final_A/{baroque,default}` (353/353 each), `A_grade.log`,
  `A_decompose.log`; byte-identity regen `ours_A/baroque` (353/353 `cmp` match).
- Commit-B decode + grade: `corpus_decode_chord_step2final_B/{baroque,default}`, `B_grade.log`, `B_decompose.log`;
  byte-identity regen `ours_B/baroque` (353/353 `cmp` match).
- Builds/tests: `build_A.log`, `build_B.log`, `A_composing.log` (840) / `B_composing.log` (844), `*_notation.log` (53),
  `*_snap.log` (11/11), `B_decode_tests.log` (the 4 new TwoReading tests OK).
