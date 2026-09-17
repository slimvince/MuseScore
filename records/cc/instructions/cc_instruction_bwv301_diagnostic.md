# CC Instruction: bwv301 L283 Diagnostic Dump

## Pre-reading (mandatory every session)

Read `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only), and
`C:\s\MS\build_and_test.md` before starting.

Current HEAD: `f9ba22157d`. Baselines: Baroque BIR=true=25, BIR=false=16;
Jazz BIR=true=36, BIR=false=10. Tests: 407/407, 52/52, 11/11.

**This is a diagnostic-only pass. One temporary print is permitted.
All diagnostic code must be discarded before reporting. No commits.**

---

## Context

bwv301 has a BIR=false region where our winner has root G (pcWeight = 0.0 — absent)
while the DCML-correct root B has pcWeight = 1.25 (the strongest PC in the region).
The previous investigation (`cc_absent_root_investigation.md`) identified the winner
as emerging from `chosenPerBass.front()` at approximately L283 of
`harmonicfunctionlayer.cpp`, and concluded that "bwv301 needs cross-bass-group
retention" — meaning the B-rooted reading is in a different perBass group from
the winner.

The specific question: **why does the competition pipeline produce a G-absent winner
when B=1.25 is the region's strongest PC?** Either the B-rooted reading is not
being scored (B isn't a bass candidate, or the B-rooted template scores below G),
or it IS being scored but loses at cross-bass selection for a structural reason.

bwv14.5 and bwv174.5 are accepted as Phase D/segmentation residuals. This pass
covers bwv301 only.

---

## Step 1 — Confirm baseline

```
cd C:\s\MS\ninja_build_rel
./pipeline_snapshot_tests.exe > /tmp/snap_pre.txt 2>&1; echo "exit:$?"
tail -3 /tmp/snap_pre.txt
```

Expected: 11/11 (1 skipped). Record the result before touching any source file.

---

## Step 2 — Add a single diagnostic print in applyHarmonicFunction

Read `harmonicfunctionlayer.cpp` (the full file — it is short). Find the
cross-bass winner-selection step (the point CC's previous investigation identified
as L283, `chosenPerBass.front()` or equivalent). The goal is to print, for the
bwv301 BIR=false region only, the full competition state just before the winner
is committed.

Add a temporary print gated on the bwv301 region's distinctive pcWeight fingerprint.
The bwv301 BIR=false region has: B=1.25, D=1.25, A=1.05, C=0.25, Ab=0.20 (G absent).
Gate the print on (pcWeight of B == 1.25 AND pcWeight of G == 0.0) — this will be
specific enough not to spam unrelated regions.

The print should output (to stderr or a file — see Step 3):

1. **Bass candidates present in the competition** — all distinct bass PCs that have
   at least one scored cell in the snapshot. List them with their pitch-class names.

2. **For each bass candidate: top 3 cells** — (rootPc name, template quality name,
   pre-bonus score, post-bonus score if different). Show at minimum the winner of
   each perBass group.

3. **B-rooted cells specifically** — for root PC = B (PC 11): list ALL cells where
   rootPc == 11, with their bass candidate, template quality, and score. If no such
   cells exist, say so explicitly.

4. **The cross-bass winner** — which (bass, rootPc, template) triple wins, and at
   what score.

5. **pcWeights for this region** — the raw weight for each PC present above 0.0.

Use `std::cerr` so it doesn't interfere with stdout batch output.

---

## Step 3 — Build and run

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
```

Run bwv301 and capture stderr separately:

```
cd C:\s\MS\ninja_build_rel
./batch_analyze.exe ..\src\composing\tests\bwv301.musicxml --preset Baroque \
  > /tmp/bwv301_stdout.txt 2>/tmp/bwv301_diag.txt; echo "exit:$?"
cat /tmp/bwv301_diag.txt
```

If the print does not fire, the gate condition is wrong. Adjust: try gating on
pcWeight sum > 4.0 (the sum for this region is ~4.30), or on rootPc of winner == 7
(G), or on the region's tick range (look up the BIR=false tick from the batch stdout).

---

## Step 4 — Read the diagnosis

From the diagnostic output, answer these questions:

**Q1 — Is B (PC 11) present as a bass candidate?**
If yes: what is the top B-rooted cell's score? How does it compare to the winner?
If no: why not? Is B absent from the bass register (all notes at pitch > 60, or
the bass extraction logic excludes it)? Is B only present in upper register voices?

**Q2 — What bass candidate does the winner belong to?**
If the winner has root G (absent at weight 0.0), which bass PC is it scored under?
Is the bass the same note that makes the G reading "make sense" (e.g. bass=Bb makes
it a Gm first inversion, or bass=D makes it a G/D)?

**Q3 — Is this a bass-register extraction problem?**
If B is strongly present (pcWeight 1.25) but NOT a bass candidate, the issue is
that B isn't the lowest note in the region — it's present as a mid-voice PC but
the bass-candidate enumeration only samples the bass register. The absent-root
guard at L283 cannot fix this: it can only choose among candidates already in the
pool. The correct fix would be different (either PCset-wide root voting, or a
different segmentation where B IS the bass note).

**Q4 — Is there a present-root alternative within margin of the winner?**
Look at all cells where the root PC has pcWeight > 0.20. What is the highest-scoring
one? What is the score gap between it and the winner?

---

## Step 5 — Discard the diagnostic print

**Before reporting:** revert the diagnostic changes to `harmonicfunctionlayer.cpp`:

```
cd C:\s\MS
git checkout -- src/composing/analysis/function/harmonicfunctionlayer.cpp
```

Then confirm:

```
cd C:\s\MS\ninja_build_rel
./pipeline_snapshot_tests.exe > /tmp/snap_post.txt 2>&1; echo "exit:$?"
tail -3 /tmp/snap_post.txt
```

Expected: 11/11 unchanged. Working tree clean (`git status`).

---

## Output

Write findings to `C:\s\MS\cc_bwv301_diagnostic_report.md`.

Answer the four questions (Q1–Q4) concisely, with the actual numbers from the
diagnostic output. Then give a one-paragraph bottom line:

- Is the B-rooted reading present at L283 or structurally excluded?
- If excluded: why, and is it a bass-register extraction issue, a template-scoring
  issue, or something else?
- Does an absent-root guard at L283 have a viable swap target for bwv301, or is
  this definitively a Phase E case?

**No code changes in the working tree after reporting. No commits.**

---

## Acceptance criteria

| Check | Required |
|---|---|
| Diagnostic print gated on bwv301 fingerprint | Yes — must fire for the BIR=false region |
| Q1–Q4 answered with actual diagnostic numbers | Yes |
| `harmonicfunctionlayer.cpp` reverted before report | Yes |
| pipeline_snapshot_tests post-revert | 11/11 |
| Working tree after report | Clean |
| Commits | None |
