# CC Instruction: Δ=+7a diagnostic + housekeeping

## Pre-reading (mandatory)

Read `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header), `C:\s\MS\build_and_test.md`,
`C:\s\MS\docs\scoring_model.md` (§2, §4), and `C:\s\MS\COWORK_HANDOFF.md` (Current state
block + C3/C4 Δ=+7a entry under Phase C).

**Read-and-diagnose + housekeeping only for Part A–D. No scoring logic changes. No commits
for Parts A–D. Part E (unit tests) is a code addition and should be committed.**

---

## Background

After Gate R (`638ced1c12`), Baroque BIR=false=13 remains. The full breakdown is in
COWORK_HANDOFF.md. The two highest-priority actionable cases are **bwv102.7** and
**bwv261** — the Δ=+7a sub-cluster.

Both were characterised in `cc_deltaseven_predecessor_report.md` as "wrong root wins
vertically (`contFired=0`)." The predecessor-confidence diagnostic showed:
- bwv102.7: wrong root Eb (rootPc=3) beats DCML-correct Ab (rootPc=8) with a within-bass
  margin of 0.33 **before rootContinuityBonus fires**. `contFired=0`.
- bwv261: wrong root C# HalfDim (rootPc=1) beats DCML-correct F# (rootPc=6) with a
  within-bass margin of 0.36 before bonus. `contFired=0`.

rootContinuityBonus merely self-perpetuates the error into later sub-regions — it did not
cause it. Gating rcb cannot fix these. The oracle itself is returning the wrong winner
on vertical evidence alone.

What we do NOT yet know: which specific oracle terms (template score, diatonic bonus,
extensionThreshold, inversion bonuses, scale scoring) drive the margin. That is what
this diagnostic determines.

---

## Part A — Corpus regeneration (prerequisite, do first)

`tools/corpus/` currently holds a stale PRE-Gate-R Jazz regeneration. Regenerate to the
committed POST-Baroque state before doing any corpus work:

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus; echo "exit:$?"
cd C:\s\MS && python tools/analyze_inversion_errors.py; echo "exit:$?"
```

Expected output: Baroque BIR=true=24, BIR=false=13 (confirming HEAD `638ced1c12`).
If numbers differ, stop and report — do not proceed.

---

## Part B — Identify failing region details

Read `src/composing/tests/chord_mismatch_report.txt`.

For **bwv102.7** and **bwv261** find the failing region(s) and record:
- Tick range (startTick, endTick) for each
- Our winner: rootPc, quality, bassPc
- DCML expected: rootPc, quality
- Whether multiple sub-regions are failing or just one

Also read `docs/score_inventory.md` to confirm the file paths for both scores.

---

## Part C — Full oracle dump via `diagnoseChord`

For each failing region in both scores, run `batch_analyze` with `--dump-regions
diagnose` or equivalent to get the full `diagnoseChord` output for those ticks.

```
cd C:\s\MS
ninja_build_rel/batch_analyze.exe <bwv102.7_path> --dump-regions diagnose > /tmp/diag_bwv102.txt 2>&1; echo "exit:$?"
grep -A 30 "tick=<FAILING_TICK>" /tmp/diag_bwv102.txt | head -60

ninja_build_rel/batch_analyze.exe <bwv261_path> --dump-regions diagnose > /tmp/diag_bwv261.txt 2>&1; echo "exit:$?"
grep -A 30 "tick=<FAILING_TICK>" /tmp/diag_bwv261.txt | head -60
```

If `--dump-regions diagnose` is not available, use whatever dump flag produces
`diagnoseChord` output (check `build_and_test.md` for the exact flag).

**Fallback if diagnoseChord dump doesn't separate vertical oracle terms clearly:**
Add a temporary debug print in `analyzeChord` / `applyHarmonicFunction` as in the
Phase E diagnostic (see `cc_instruction_deltaseven_phase_e_diagnostic.md` §Step 2
for the pattern). Gate the print on the failing ticks. Remove before committing.

From the dump, extract for each failing region — for BOTH the wrong winner and the
DCML-expected root candidate:

| Field | Wrong winner | DCML-expected candidate |
|---|---|---|
| rootPc | | |
| bassPc | | |
| quality | | |
| templateIndex (tiePriority) | | |
| basisIndep (pre-rcb) | | |
| basisDep | | |
| complexityFactor | | |
| augFactor | | |
| wCompleteBonus | | |
| rawScore = (basisIndep+basisDep)*cf*af + wComplete | | |
| rcb (rootContinuityBonus) | | |
| total | | |
| pcWeight[wrongRootPc] | | |
| pcWeight[dcmlRootPc] | | |

Also record:
- What PCs are present in the region (the full pitch-class set and weights)
- The detected key (keyFifths, keyMode)
- Is the DCML-expected root PC actually present in the sounding tones?
- What bass note(s) are in the region?

---

## Part D — Assessment questions

Answer these specifically for each case:

**For bwv102.7 (Eb=3 beats Ab=8):**
1. What is the full PC set? Does Ab (pc=8) appear with meaningful pcWeight?
2. What template does Eb win with? What is its raw score vs. the Ab candidate?
3. Is there an Eb major/minor/7th reading that genuinely fits the sounding tones
   (i.e., Eb is present with high pcWeight), or is Eb winning despite being absent/weak?
4. What is the diatonic bonus contribution for each candidate? Is one key-diatonic
   and the other not?
5. Is there an inversion/slash-chord reading involved (e.g., Ab/Eb = Eb bass)?
   If so, what bass PC is present?
6. Is the DCML-expected Ab reading present in the candidacy pool at all? If yes, what
   score does it get? If absent, why (pcWeight below threshold? key mismatch?)?

**For bwv261 (C# HalfDim=1 beats F#=6):**
1. What is the full PC set? Do C# and F# both appear?
2. C# HalfDim = {C#, E, G, B} = {1, 4, 7, 11} relative. Do all four tones appear
   in the sounding notes, or is this winning on partial evidence?
3. What is the F# candidate (what template — F# major? F# minor? F#7?)? What raw score?
4. What is the bass note? Is this a slash-chord situation (e.g., F#/C#)?
5. What is the key for this region? Is C# diatonic in that key? Is F# diatonic?
6. Is there an extensionThreshold effect — does C# have high pcWeight while F# is weak?

**Cross-case pattern:**
7. Do the two cases share any structural pattern (e.g., both have a tritone-related
   wrong winner, both involve a key-diatonic wrong root, both involve absent DCML root)?
8. Could a single oracle change fix both, or are they independent mechanisms?
9. Are these fixable at all without Phase E context, or do they require functional
   information (cadence, voice-leading) that the oracle cannot see vertically?

---

## Part E — Housekeeping: comment fixes (commit separately, before or after diagnostic)

These are zero-risk comment-only changes. Make them, run both test suites to confirm
byte-identical, commit with a docs/chore message.

### E1 — Fix inaccurate `basisIndep` comment in `harmonicfunctionlayer.h`

Find the comment claiming `basisIndep` carries "no progression signal" (or similar).
Replace it with accurate text noting that `basisIndep` includes the oracle vertical score
PLUS contextual inversion/resolution bonuses from `bassIndependentContextualBonuses`
and `bassDependentContextualBonuses`. Reference `chordanalyzer.h:329` (the debt TODO).

### E2 — Fix stale invariant comment in `chordanalyzer.cpp` (~L1634)

Find the comment asserting `bassIndep + bassDependent == contextualBonuses`.
Update it to clarify: `contextualBonuses` is used only by `diagnoseChord` and
intentionally includes `rootContinuityBonus` (L1482); the production path
(`bassIndependentContextualBonuses + bassDependentContextualBonuses`) does not add rcb —
the divergence is intentional, not an invariant violation.

### E3 — Add Gate R cross-layer dependency comment in `harmonicfunctionlayer.cpp`

At the Gate R `basisDep <= 0` condition, add a comment explaining:
"Uses oracle's `basisDep` as a proxy for 'has sounding third via `sameRootInversionBonus`'.
If oracle temporal debt (`chordanalyzer.h:329`) is ever resolved, this condition must be
revisited — `basisDep` would no longer carry that signal."

### E4 — Add bridge-path shallowness comment to `regiontonecollector.cpp::findTemporalContext`

At the top of `findTemporalContext`, add a comment noting that this function currently
only looks **backward** (via `prev1`) and does **not** set `bassIsStepwiseToNext`,
`nextRootPc`, `nextBassPc`, or Step 1/2 fields. Unlike the batch path,
`stepwiseBassLookaheadBonus` will not fire here. This is an implementation gap (not a
design constraint — `next1` is available), tracked for a future fix.

### E5 — Correct golden path note in `build_and_test.md`

Find any mention of pipeline snapshot golden file locations. Confirm or add a note that
the goldens live at:
`src/notation/tests/pipeline_snapshot_tests/snapshots/`
NOT at `src/composing/tests/snapshots/`.
This corrects a path error in a prior instruction (`cc_instruction_gate_r_verify_and_commit.md`)
that CC found during Part D of the verification.

**After E1–E5:** Run both test suites, confirm byte-identical (no scoring change):
```
cd C:\s\MS/ninja_build_rel && ./composing_tests.exe > /tmp/e_comp.txt 2>&1; echo "exit:$?"
cd C:\s\MS/ninja_build_rel && ./notation_tests.exe > /tmp/e_nota.txt 2>&1; echo "exit:$?"
head -5 /tmp/e_comp.txt
head -5 /tmp/e_nota.txt
```

Commit:
```
git add src/composing/analysis/function/harmonicfunctionlayer.h
git add src/composing/analysis/function/harmonicfunctionlayer.cpp
git add src/composing/analysis/chord/chordanalyzer.cpp
git add src/composing/analysis/engravingbridge/regiontonecollector.cpp
git add build_and_test.md
git commit -m "docs/chore: comment fixes — basisIndep accuracy, stale invariant, Gate R dependency, bridge lookahead gap, golden path"
```

---

## Part F — Gate R unit tests (commit separately after E)

Add unit tests for the `bassIsTemplateChordTone` helper and Gate R's decision branches.
These tests go in `src/composing/tests/` alongside existing unit tests.

### F1 — `bassIsTemplateChordTone` table tests

For each template 0–16, verify that every interval IN the template passes the function,
and at least one interval NOT in the template fails.

Specifically, for the Gate R motivation case:
- Template 0 (Major triad {0,4,7}): interval 9 must FAIL (this is the Δ=+7b foreign bass interval)
- Template 6 (Diminished {0,3,6}): interval 9 must FAIL
- Template 4 (Minor triad {0,3,7}): interval 9 must FAIL
- Template 16 (Power {0,7}): interval 9 must FAIL, interval 5 must FAIL

Also test boundary conditions:
- `tiePriority = -1`: must return `true` (conservative)
- `tiePriority = 17`: must return `true` (conservative)
- `rootPc = -1`: must return `true` (conservative)

### F2 — Gate R fires/does-not-fire

Construct minimal `ScoringCell` instances and verify Gate R's four branches:

1. `bassPc` is a template chord tone, `basisDep == 0.0`: Gate R does NOT zero rcb
2. `bassPc` is NOT a template chord tone, `basisDep == 0.0`: Gate R ZEROS rcb
3. `bassPc` is NOT a template chord tone, `basisDep == 0.5` (extended slash chord): Gate R does NOT zero rcb
4. `explorationMode = true`, `bassPc` NOT chord tone, `basisDep == 0.0`: Gate R does NOT zero rcb

These four cases cover all branches of the Gate R condition:
```cpp
if (rcb > 0.0 && !prefs.explorationMode
    && cell.basisDep <= 0.0
    && !bassIsTemplateChordTone(cell.rootPc, cell.tiePriority, cell.bassPc)) {
    rcb = 0.0;
}
```

The test does not need to load a score — construct `ScoringCell` with the relevant
fields set directly, call a thin test wrapper around the Gate R block, and check the
resulting rcb.

**After F1–F2:** Run composing tests, confirm 407+N/407+N pass:
```
cd C:\s\MS/ninja_build_rel && ./composing_tests.exe > /tmp/f_comp.txt 2>&1; echo "exit:$?"
head -5 /tmp/f_comp.txt
```

Commit:
```
git add src/composing/tests/  # (the new test file(s))
git commit -m "test: Gate R unit tests — bassIsTemplateChordTone table + Gate R branch coverage"
```

---

## Report format

Write findings to `C:\s\MS\cc_deltaseven_7a_diagnostic_report.md`.

Include:
1. Corpus regen result (Baroque BIR=true/false counts confirmed)
2. Failing region tick ranges for both scores
3. Full oracle tables (Part C) — wrong winner vs DCML candidate for each
4. Full PC set + pcWeights for each failing region
5. Answers to all Part D assessment questions
6. Commit hash for housekeeping (Part E)
7. Commit hash for unit tests (Part F)
8. Any surprises not anticipated above
