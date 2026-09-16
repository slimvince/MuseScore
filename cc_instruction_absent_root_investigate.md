# CC Instruction: Absent-Root Guard — Investigation Only

## Pre-reading (mandatory every session)

Read `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only), and
`C:\s\MS\build_and_test.md` before starting. Read `C:\s\MS\docs\scoring_model.md`
because this investigation touches scoring mechanics.

Current HEAD: `f9ba22157d`. Baselines: Baroque BIR=true=25, BIR=false=16;
Jazz BIR=true=36, BIR=false=10. Tests: 407/407, 52/52, 11/11.

**This is a read-only investigation. No code changes. No commits.**

---

## Background

Three Baroque BIR=false cases are believed to share a common mechanism: the
analyzer emits a winner whose root PC is absent from (or very weakly present in)
the sounding pitch classes, while the DCML-correct root IS present and strongly
weighted. These are "absent-OUR-root" cases, not "absent-DCML-root" cases.

Target cases:
- **bwv14.5** — our winner Gm/Bb, root G absent from sub-region {C,D,Bb}
- **bwv174.5** — believed: our root E absent; DCML root G#/Ab present (it's the bass)
- **bwv301** — believed: our root G absent; DCML root B strongly present

A previous attempt to fix bwv14.5 placed an absent-root guard in the
inversion-deduction block (L2839–2880 of `chordanalyzer.cpp`). That attempt:
- Had **no effect on bwv14.5** (the deduction block's bestAltIdx pointed to D Dom7,
  not Gm — the Gm/Bb result comes from a sub-region call upstream of that block)
- Caused **5 pipeline-snapshot regressions** on legitimate cases

The proposed new location is the **winner-selection pass in `applyHarmonicFunction`**
(`src/composing/analysis/function/harmonicfunctionlayer.cpp`). This is a different
code site from the previous attempt. The investigation must confirm whether this
new location is viable and safe.

---

## Part 1 — Verify bwv174.5 and bwv301 reclassification

These two cases were previously categorised as "Evidence-absent (DCML root not in
pcs)". The new hypothesis is that our root is absent but the DCML root IS present —
they are absent-OUR-root cases, same mechanism as bwv14.5.

### Step 1a — Run batch analysis on bwv174.5

```
cd C:\s\MS\ninja_build_rel
./batch_analyze.exe ..\src\composing\tests\bwv174.5.musicxml --preset Baroque \
  --dump-regions notation > /tmp/bwv174_5_dump.txt 2>&1; echo "exit:$?"
head -80 /tmp/bwv174_5_dump.txt
```

Find the BIR=false region. For that region, report:
- Our emitted chord (root, quality, bass)
- pcWeights for all PCs in the region (the `--dump-regions notation` output should
  include pcWeight per PC — if the flag syntax differs, check `--help`)
- Whether the DCML root PC is present and at what weight
- Whether our emitted root PC is present and at what weight
- The `extensionThreshold` in use (Baroque preset default is 0.20)

If `--dump-regions notation` does not show pcWeights, try `--dump-regions scoring`
or `--dump-analysis` — check `./batch_analyze.exe --help; echo "exit:$?"` for
available flags.

### Step 1b — Run batch analysis on bwv301

Same procedure for bwv301:

```
cd C:\s\MS\ninja_build_rel
./batch_analyze.exe ..\src\composing\tests\bwv301.musicxml --preset Baroque \
  --dump-regions notation > /tmp/bwv301_dump.txt 2>&1; echo "exit:$?"
head -80 /tmp/bwv301_dump.txt
```

Same questions as Step 1a.

### Step 1c — Confirm or refute the hypothesis

For each case, state clearly:
- Is our emitted root PC absent from the region's pcWeights (weight ≤ extensionThreshold)?
- Is the DCML-correct root PC present (weight > extensionThreshold)?
- Does this confirm the "absent-OUR-root" reclassification?

If either case turns out to be a genuine "DCML root not in pcs" case, say so —
that would mean it belongs in Phase D, not in the absent-root guard scope.

---

## Part 2 — Identify the sub-region call site for bwv14.5

The previous investigation established that bwv14.5's Gm/Bb winner comes from a
**sub-region analyzeChord call** with pcs={C,D,Bb} (root G absent). The parent
region has pcs={C,D,E,Bb}; E drops out on entry to the sub-region.

This sub-region must originate in `regionanalyzer.cpp` — specifically in Pass 2
or Pass 2b, where the parent region is split into sub-regions for finer analysis.

### Step 2a — Locate Pass 2 / Pass 2b sub-region call sites

Read the relevant section of `regionanalyzer.cpp`:

```
grep -n "analyzeChord\|sub.region\|splitRegion\|Pass 2" \
  C:\s\MS\src\composing\analysis\region\regionanalyzer.cpp | head -60; echo "exit:$?"
```

Identify which call sites create sub-regions and call `analyzeChord` on them.
There are likely 2–3 such sites (Pass 2 and Pass 2b at minimum, possibly Pass 1
refinement too).

### Step 2b — Find which call site produces the {C,D,Bb} sub-region

Look at the bwv14.5 region in question. From previous investigation:
- Parent region pcs = {C, D, E, Bb}
- Sub-region pcs = {C, D, Bb} (E dropped)
- Bass = Bb2 (MIDI 46)

The E dropping out is the key clue. In the sub-region split, what determines which
tones are included? Is it a tick-range slice (E falls outside the sub-region tick
range) or a register-based selection (E is in a different voice or register)?

Read the Pass 2 / Pass 2b split logic to understand how sub-regions are carved.

You may need to add a temporary diagnostic print to confirm — if so, describe exactly
what you would add and where, but **do not add it yet** (this is investigation only).

Report:
- Which Pass (Pass 2 or Pass 2b) produces the sub-region for bwv14.5?
- What is the tick range of the sub-region?
- Why does E drop out?
- Is the Gm/Bb result from that sub-region propagated back as the parent-region winner,
  or is it only used as an alternative? (Does a sub-region winner override the parent
  region's Pass 1 winner outright, or only under certain conditions?)

---

## Part 3 — Understand the 5 pipeline-snapshot regressions from the previous guard

The previous absent-root guard was placed in the inversion-deduction block (chordanalyzer.cpp
around L2839–2880). It caused 5 snapshot regressions on legitimate cases.

### Step 3a — Identify the 5 regression cases

Run the pipeline snapshot tests to confirm baseline:

```
cd C:\s\MS\ninja_build_rel
./pipeline_snapshot_tests.exe > /tmp/snap_baseline.txt 2>&1; echo "exit:$?"
tail -5 /tmp/snap_baseline.txt
```

Expected: 11/11 (1 skipped). Confirm this before proceeding.

The 5 regression cases from the previous attempt are recorded in git history.
Find the commit that added and then reverted the inversion-deduction guard:

```
cd C:\s\MS
git log --oneline --all | head -30; echo "exit:$?"
```

Look for a commit message referencing "absent-root", "deduction block", or the bwv14.5
investigation. If you find a reverted commit, inspect its diff:

```
git show <commit-hash> -- \
  src/composing/analysis/chord/chordanalyzer.cpp | head -100; echo "exit:$?"
```

Also look for any notes in `COWORK_HANDOFF.md` or `STATUS.md` about which scores
were affected. From context: the 5 regressions were on legitimate inversion-correction
cases where the guard fired incorrectly and blocked a correct winner swap.

### Step 3b — Characterise the 5 cases

For each of the 5 regression cases (or as many as you can identify):
- What chord did the guard block?
- What was the emitted chord vs the correct (golden) chord?
- Why did the guard fire (what property of the winner triggered "root absent")?
- Was the root actually absent from the pcWeights, or was the guard condition too loose?

This determines whether the regression risk would persist at the new `applyHarmonicFunction`
location, or whether those cases would be handled differently there.

---

## Part 4 — Assess the proposed guard location

The proposed guard is in `applyHarmonicFunction` in
`src/composing/analysis/function/harmonicfunctionlayer.cpp`.

Read the current implementation:

```
cat C:\s\MS\src\composing\analysis\function\harmonicfunctionlayer.cpp; echo "exit:$?"
```

And the header:

```
cat C:\s\MS\src\composing\analysis\function\harmonicfunctionlayer.h; echo "exit:$?"
```

### Step 4a — Understand what applyHarmonicFunction receives

`applyHarmonicFunction` is the competition pipeline (winner-selection). From the
E2d redesign:
- It receives a `ScoringSnapshot` containing all (bass, root, template) cells with
  their scores
- It runs all 7 steps: rescore with progression signals, Pass B step bonuses,
  per-bass quality guard, cross-bass winner selection, threshold, build results[],
  fill gateCtx

At what point in those 7 steps does the winner emerge? Specifically: after step (4)
(cross-bass winner selection) and before step (6) (build results[]), is there a single
clearly-identified winner cell that could be checked for "root PC weight ≤ threshold"?

### Step 4b — Does applyHarmonicFunction have access to pcWeights?

The absent-root guard needs to check whether the winner's root PC weight is at or
below `extensionThreshold`. Does `applyHarmonicFunction` currently receive:
- The pcWeights map (raw per-PC weights for the region)?
- Or only the scored cells (which encode template match but may not carry raw pcWeights)?

Report: is pcWeight data available at the proposed guard location, or would it need
to be threaded through the function signature?

### Step 4c — Gate J interaction

Gate J (in `applyPostScoringGates`) promotes a vii°→V7 completion when the dominant
root is present. Confirm:

```
grep -n "Gate J\|domRootPc\|pcWeight\[domRoot" \
  C:\s\MS\src\composing\analysis\chord\chordanalyzer.cpp | head -20; echo "exit:$?"
```

Gate J checks `pcWeight[domRootPc] > extensionThreshold` — it only fires when the
dominant root IS present above threshold. Confirm: would an absent-root guard in
`applyHarmonicFunction` (which blocks winners whose root is absent) and Gate J (which
promotes V7s only when dominant root is present) ever fire on the same chord in
conflicting ways?

State clearly: is there a conflict, or are the conditions mutually exclusive?

### Step 4d — Margin calibration check

For the 3 target cases (bwv14.5, bwv174.5, bwv301), what is the score margin between
the absent-root winner and the best present-root alternative?

From the batch dump data gathered in Parts 1 and 2, try to extract:
- Winner score (our incorrect absent-root result)
- Score of the best alternative whose root IS present above extensionThreshold

If the margin is very tight (< 0.05), a simple "reject if root absent" guard would
work. If the margin is wide (> 0.30), a "within-margin" condition is needed — rejecting
the absent-root winner only when a present-root alternative is close enough.

Report the margin for each target case, if available from the batch output.

---

## Output

Write all findings to `C:\s\MS\cc_absent_root_investigation.md`.

Structure:
```
# Absent-Root Guard Investigation

## Part 1 — bwv174.5 and bwv301 reclassification
### bwv174.5 — batch analysis findings
(pcWeights, our root weight, DCML root weight, hypothesis confirmed/refuted)
### bwv301 — batch analysis findings
(same)
### Summary: how many cases does the absent-root guard address?

## Part 2 — bwv14.5 sub-region call site
### Which Pass produces the {C,D,Bb} sub-region?
### Why does E drop out?
### How does the sub-region winner propagate to the parent?

## Part 3 — 5 regression cases from previous guard
### Regression case identification
### Characterisation of each case
### Would they regress at the new location?

## Part 4 — Guard location assessment
### applyHarmonicFunction winner-selection point
### pcWeight data availability
### Gate J interaction (conflict or mutually exclusive?)
### Margin calibration for target cases

## Recommendation
5–8 sentences: is the applyHarmonicFunction location viable? What are the remaining
unknowns? What condition should the guard check (simple absent-root, or within-margin)?
Is it safe to proceed to an implementation instruction based on this investigation?
```

**No code changes. No commits. Investigation only.**

---

## Acceptance criteria

| Check | Required |
|---|---|
| bwv174.5 reclassification | Confirmed or refuted with pcWeight evidence |
| bwv301 reclassification | Confirmed or refuted with pcWeight evidence |
| bwv14.5 sub-region caller identified | Pass 2 or Pass 2b, tick range, E dropout reason |
| Previous 5 regressions characterised | At minimum: what scores, what the guard blocked |
| applyHarmonicFunction location assessed | pcWeight availability, Gate J non-conflict |
| Code changes | None |
| Commits | None |
