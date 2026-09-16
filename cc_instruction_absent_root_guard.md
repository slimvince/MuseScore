# CC Instruction: Absent-Root Winner Guard — Implementation

## Pre-reading (mandatory every session)

Read `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only),
`C:\s\MS\build_and_test.md`, and `C:\s\MS\docs\scoring_model.md` before starting.
This instruction touches winner-selection logic and must be synced to scoring_model.md.

Current HEAD: `f9ba22157d`. Baselines: Baroque BIR=true=25, BIR=false=16;
Jazz BIR=true=36, BIR=false=10. Hard stops: Baroque BIR=false > 25,
Jazz BIR=false > 13, any test regression beyond the 2 known Corelli notation failures.
Tests: 407/407, 52/52, 11/11.

---

## Background

Three Baroque BIR=false cases share a mechanism: the competition pipeline selects a
winner whose root PC has pcWeight = 0.0 (strictly absent from the sounding PCs) because
that root's 3rd and 5th happen to be present, scoring the template well via inversion-
context terms. The DCML-correct root IS present in the region.

Target cases:
- **bwv301 (m1 b3)**: our winner G major (root G, pcWeight=0.0); DCML root B present.
  G's 3rd and 5th (B, D) are present — template fires via inversion. B-rooted
  alternative is in-group at L283, gap 0.27. Diagnostic confirmed viable swap target.
- **bwv174.5 (m4 b1)**: our root E absent (pcWeight=0.0); DCML root G# present at 0.20.
- **bwv14.5 (sub-region tick 8160–8400)**: root G absent from {C,D,Bb}; E not in
  sub-region due to tick boundary. DCML root Bb present. Bb is the parent-region winner.

The guard location is `applyHarmonicFunction` in `harmonicfunctionlayer.cpp`, at the
winner-selection step (the `chosenPerBass.front()` / L283 equivalent), after cross-bass
scoring and before results[] is built. This location was confirmed architecturally
viable in the bwv301 diagnostic pass.

Jazz target case: bwv45.7 (dim→dom absent-root, Sus/quartal classification — partial
benefit expected, not primary target).

---

## Step 0 — Read the file and confirm the winner-selection point

```
cat C:\s\MS\src\composing\analysis\function\harmonicfunctionlayer.cpp; echo "exit:$?"
```

Identify exactly where the winner is committed (the `chosenPerBass.front()` or
equivalent point). Confirm that at this point you have access to:
- The winner's identity (rootPc, templateQuality, bassPc, score)
- The full `perBass` group (all scored candidates for this bass, sorted by score)
- The `pcWeights` map (to check winner's root PC weight)
- The `extensionThreshold` preference value

Report these before writing any code.

---

## Step 1 — Implement the guard

Add the absent-root winner guard immediately before (or as part of) winner commitment
in `applyHarmonicFunction`. The guard should:

**Condition to fire:**
1. Winner's root PC weight = 0.0 exactly (`pcWeights[winnerRootPc] == 0.0` or the
   equivalent accessor — use exact zero, not ≤ extensionThreshold, to be conservative)
2. The winner's score is not overwhelmingly dominant — i.e., there exists at least one
   in-group alternative whose score ≥ (winner_score − kAbsentRootGuardMargin)
3. That alternative's root PC weight > 0.0 (the root is at least faintly present)

**Action when fired:**
Replace the winner with the highest-scoring in-group alternative that satisfies
condition (3). If multiple alternatives tie, prefer the one with the highest root
PC weight.

**Named constant for the margin:**
```cpp
static constexpr double kAbsentRootGuardMargin = 0.35;
```
This covers the bwv301 gap of 0.27 with a small buffer. If corpus analysis shows
too many regressions, tighten to 0.25 first before considering a different approach.

**Guard must not fire when:**
- Winner root PC weight > 0.0 (any presence suppresses the guard)
- No in-group alternative has a present root (guard can't improve the outcome)
- The region has `distinctPcs < 3` (dyad slivers — not enough evidence to override)

Add a comment above the guard block:
```cpp
// Absent-root winner guard: if the winner's root is entirely absent from the
// sounding PCs (pcWeight == 0.0) and a present-root alternative is within
// kAbsentRootGuardMargin, prefer the alternative. Catches G-major-from-3rd+5th
// false wins (bwv301, bwv14.5, bwv174.5) — root G/E absent while DCML root B/Ab
// is present. Previously attempted in the inversion-deduction block (chordanalyzer.cpp
// L2839–2880); that location was wrong and caused 5 snapshot regressions. This
// location is architecturally correct (winner-selection, before results[] is built).
// Diagnostic: cc_bwv301_diagnostic_report.md (2026-06-08).
```

---

## Step 2 — Build and run both test suites

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"

cd C:\s\MS\ninja_build_rel
./composing_tests.exe > /tmp/comp_guard.txt 2>&1; echo "exit:$?"
tail -3 /tmp/comp_guard.txt

./notation_tests.exe > /tmp/notation_guard.txt 2>&1; echo "exit:$?"
tail -5 /tmp/notation_guard.txt

./pipeline_snapshot_tests.exe > /tmp/snap_guard.txt 2>&1; echo "exit:$?"
tail -5 /tmp/snap_guard.txt
```

Expected: 407/407, 52/52, 11/11. If any snapshot golden fails, report the specific
golden name and the before/after chord change — do NOT update any golden without
first confirming the change is DCML-correct (see Step 3 below).

**If BIR hard stop is hit at this step (Baroque > 25 or Jazz > 13): STOP.
Do not proceed. Report the regression cases and the guard condition that fired.
Revert the guard entirely and report findings.**

---

## Step 3 — Run corpus analysis on BOTH presets

```
cd C:\s\MS
python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
python tools/analyze_inversion_errors.py
```

Record Baroque BIR=true and BIR=false.

```
python tools/run_bach_preset.py --preset Jazz --output-dir tools/corpus
python tools/analyze_inversion_errors.py
```

Record Jazz BIR=true and BIR=false.

**Hard stops: Baroque BIR=false > 25, Jazz BIR=false > 13. Revert and report if hit.**

### Per-score BIR change (mandatory — do not skip)

For Baroque, identify specifically which scores changed BIR status (false→true or
true→false) compared to the baseline. You can diff the corpus JSON output or grep
the analyze_inversion_errors output.

Report:
- Did bwv301 move from BIR=false to BIR=true? (primary target)
- Did bwv174.5 move? Did bwv14.5 move?
- Did any score that was BIR=true regress to BIR=false?
- For Jazz: did bwv45.7 move?

**If bwv301 did NOT improve**: check whether there is a contamination cascade — an
upstream sub-region (earlier tick) that also gets a wrong root (G absent) and sets
previousRootPc=G, which then feeds rootContinuityBonus to the decisive sub-region.
If so, does the guard also fire on that upstream sub-region? If the guard fixes the
upstream call but not the downstream (or vice versa), explain why.

---

## Step 4 — Handle snapshot golden changes (if any)

If any pipeline snapshot golden changed, open the affected score in MuseScore and
confirm the new chord reading against DCML annotations for that region.

Use `tools/inject_dcml_rn.py` if needed to overlay DCML labels. Only update the
golden if the new reading is DCML-correct (or at minimum no worse than the old one).

```
cd C:\s\MS\ninja_build_rel
./pipeline_snapshot_tests.exe --update-goldens; echo "exit:$?"
./pipeline_snapshot_tests.exe > /tmp/snap_updated.txt 2>&1; echo "exit:$?"
tail -3 /tmp/snap_updated.txt
```

Run `--update-goldens` only after confirming the new reading is correct.
Report which goldens were updated and the before/after chord change.

---

## Step 5 — Update docs/scoring_model.md

Per the sync rule in CLAUDE.md: any commit that adds or modifies a guard, bonus, or
scoring term must include a corresponding update to `docs/scoring_model.md`.

Add the absent-root winner guard to the appropriate section (likely §6 — post-scoring
passes, or wherever `applyHarmonicFunction` winner-selection logic is documented). Include:
- What the guard checks (root pcWeight == 0.0 + margin condition + distinctPcs ≥ 3)
- What it does (swaps to best in-group present-root alternative)
- Named constant `kAbsentRootGuardMargin = 0.35`
- Target cases: bwv301, bwv174.5, bwv14.5

---

## Step 6 — Commit (only if all checks pass)

If and only if:
- 407/407 composing tests pass
- 52/52 notation tests pass (same 2 Corelli exemptions)
- 11/11 snapshot tests pass (any updated goldens confirmed DCML-correct)
- Baroque BIR=false ≤ 25 (hard stop)
- Jazz BIR=false ≤ 13 (hard stop)
- `docs/scoring_model.md` updated

Then commit:
```
cd C:\s\MS
git add src/composing/analysis/function/harmonicfunctionlayer.cpp
git add docs/scoring_model.md
# add any updated golden files
git commit -m "fix: absent-root winner guard in applyHarmonicFunction (bwv301 + bwv174.5 + bwv14.5)"
```

---

## Output (report)

Report:
1. Guard implementation location (file, approximate line, exact condition used)
2. Test results: composing / notation / snapshot (pass/fail counts, any golden names changed)
3. Corpus results table:

   | Preset | BIR=true | BIR=false | Δ vs baseline |
   |---|---|---|---|
   | Baroque | | | |
   | Jazz | | | |

4. Per-score BIR changes (especially bwv301, bwv174.5, bwv14.5, and any regressions)
5. Contamination cascade analysis for bwv301 if BIR=false count did not improve
6. New HEAD (if committed)

---

## Acceptance criteria

| Check | Required |
|---|---|
| Guard condition | Root pcWeight == 0.0 AND in-group present-root alternative within kAbsentRootGuardMargin |
| Named constant | `kAbsentRootGuardMargin = 0.35` |
| distinctPcs guard | ≥ 3 (dyad slivers excluded) |
| composing_tests | 407/407 |
| notation_tests | 52/52 |
| pipeline_snapshot_tests | 11/11 (updated goldens only if DCML-confirmed) |
| Baroque BIR=false | ≤ 25 (hard stop) |
| Jazz BIR=false | ≤ 13 (hard stop) |
| Per-score BIR changes | Reported, including whether bwv301 actually improved |
| docs/scoring_model.md | Updated before commit |
