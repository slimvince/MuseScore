# MuseScore Studio — Build and Test Instructions

This document provides comprehensive, step-by-step instructions for building MuseScore Studio, running all test suites, launching executables, and using the main Python tools. It is intended for new developers, automated agents, and any session that needs to recover full build/test/run knowledge after context loss.

---

## Running from Git Bash / MSYS2 (Claude bash tool)

Do **NOT** use `cmd.exe //c` — MSYS2 translates `//` as a UNC path, so the flag is dropped and cmd.exe opens interactively with no build output.

**Build (from Git Bash):**
```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
```

**Run tests directly:**
```
/c/s/MS/ninja_build_rel/composing_tests.exe
/c/s/MS/ninja_build_rel/notation_tests.exe
```

**Run batch_analyze:**
```
/c/s/MS/ninja_build_rel/batch_analyze.exe "<score>" --preset jazz
```

**Invoke ninja directly (without cmd.exe):**
```
/c/Qt/Tools/Ninja/ninja.exe -C /c/s/MS/ninja_build_rel composing_tests notation_tests MuseScore5.exe batch_analyze
```

---

## 1. Build Scripts

There are three build scripts in the project root. All write to `ninja_build_rel/`.

### `setup_and_build_fast.bat` — First-time / CMake configure

Runs CMake configuration if `ninja_build_rel/CMakeCache.txt` does not exist, then builds:
- `composing_tests`
- `MuseScore5.exe`
- `batch_analyze`

**Does NOT build `notation_tests`.** Use this the first time on a fresh checkout (or after deleting the build tree) to get a working composing build quickly without waiting for the full notation build.

```
cmd.exe //c "C:\s\MS\setup_and_build_fast.bat"
```

### `setup_and_build.bat` — Normal session script

Assumes CMake has already been configured (build tree exists). Builds:
- `composing_tests`
- `notation_tests`
- `MuseScore5.exe`
- `batch_analyze`

This is the **standard script for every development session**.

```
cmd.exe //c "C:\s\MS\setup_and_build.bat"
```

From Git Bash background tasks, invoke as:
```
cmd.exe //c "C:\s\MS\setup_and_build.bat"
```

### `build_tests.bat` — Tests only, no GUI

Builds `composing_tests` and `notation_tests` only. No `MuseScore5.exe` or `batch_analyze`.
Use when you only need to run the test suites and want the shortest possible build time.

```
cmd.exe //c "C:\s\MS\build_tests.bat"
```

### Recommended workflow

| Situation | Script |
|---|---|
| First time / fresh checkout / deleted build tree | `setup_and_build_fast.bat`, then `setup_and_build.bat` |
| Normal session | `setup_and_build.bat` |
| Tests only (no GUI needed) | `build_tests.bat` |

---

## 2. Running Test Suites

All test executables are in `ninja_build_rel/`. Run from that directory.

```
cd C:\s\MS\ninja_build_rel
```

### Composing Tests

```
./composing_tests.exe
```

**Current baseline: 407/407** passing (verify with CC — count changes as tests are added).

Tests `analyzeChord()` directly in the composing module. Run after any change to `src/composing/`.
After each run, read `src/composing/tests/chord_mismatch_report.txt`.

### Notation Tests

```
./notation_tests.exe
```

**Current baseline: 53/53** passing (verify with CC — count changes as tests are added).

Run after any change to bridge code (`notationharmonicrhythmbridge.cpp`,
`notationcomposingbridge.cpp`, `notationcomposingbridgehelpers.cpp`, etc.) **and** after
any change to `chordanalyzer.cpp` that alters chord output.

**P1–P4 pipeline snapshot test** (`pipeline_snapshot_tests.cpp`) is a SEPARATE
executable from `notation_tests.exe`. Both are built by the standard build scripts.
It snapshots the output of all four analysis paths (P1 implode, P2 annotation,
P3 tick-regional, P4 tick-local) against golden JSON files for a 10-score corpus.

**Golden file location:** the snapshot goldens live at
`src/notation/tests/pipeline_snapshot_tests/snapshots/` — NOT at
`src/composing/tests/snapshots/`. (Corrects a path error in an earlier instruction;
use the notation-tests path for any git-add of refreshed goldens.)

```
./pipeline_snapshot_tests.exe
```

If a code change intentionally alters chord output (e.g. a new inversion gate fires),
the snapshot test will fail — this is expected. Refresh the goldens only after
verifying the new output is correct:

```
./pipeline_snapshot_tests.exe --update-goldens
```

Then re-run `./pipeline_snapshot_tests.exe` to confirm all pass.
Never run `--update-goldens` without first confirming the output change is intentional
and correct.

### Batch Analyze Regression Tests

```
python tools/test_batch_analyze_regressions.py --batch-analyze ninja_build_rel/batch_analyze.exe --repo-root .
```

Output: prints `batch_analyze regressions passed` if successful.
Run after any change to `tools/batch_analyze.cpp`.

### Corpus Regression Check

For any gate addition or modification, run BOTH presets and confirm zero BIR=false
regression in each before committing:

```
# Baroque (primary — per-preset dir, regenerated + manifest-stamped)
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus/baroque
cd C:\s\MS && python tools/characterise_bir_false.py --corpus-dir tools/corpus/baroque

# Jazz (independent dir — no shared state, run in any order)
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz --output-dir tools/corpus/jazz
cd C:\s\MS && python tools/characterise_bir_false.py --corpus-dir tools/corpus/jazz
```

**Stage 2.2a (M3 fix):** each preset now has its own dir under `tools/corpus/` and a
`corpus_manifest.json`. `run_bach_preset.py` clean-slates the dir before a regen and
**exits nonzero** unless the corpus is 353/353 complete; `characterise_bir_false.py`
**refuses** to measure a dir whose manifest is missing/incomplete or whose `.ours.json`
fingerprints don't match the manifest (the old shared-`tools/corpus` contamination is
now structurally impossible and loudly detected). Gate on **case identity**: Baroque 13,
Jazz 7 = `{bwv244.15, bwv245.17, bwv245.40, bwv422, bwv432, bwv45.7, bwv74.8}`.
(`analyze_inversion_errors.py` is the separate secondary `bassIsRoot` metric; its
three-way genuine split is Baroque 24/13, Jazz 35/7, of which the 13/7 BIR=false half
is the characterise gate. Since Stage 2.2-ii it also takes `--corpus-dir` — see §4.)

**Threshold policy**: gate thresholds are calibrated against the Baroque corpus and
must not be adjusted to accommodate other styles. If a gate causes BIR=false
regressions in Jazz, fix it with a tighter structural condition or a preset-specific
override — never by widening the Baroque-tuned threshold. See CLAUDE.md for details.

**Current Baroque baseline (Iteration 61/62, validated 2026-05-11):**
- 3-way genuine BIR=true: 6
- 3-way genuine BIR=false: 125
- Commits: a34dba041e (Iter 61 HalfDim first-inversion bonus),
  ee337aeca4 (Iter 62 parallelization)
- Regression tolerance: investigate before committing if BIR=false > 135
  (current 125 + 10).
- BIR=false enumeration: `tools/birfalse_baseline_iter61.txt`
- Genuine BIR=true characterization: `tools/iter63_genuine6_characterization.txt`

Update rationale: Iteration 61 added the HalfDim first-inversion bonus
(Option B), moving BIR=true 7→6 and BIR=false 132→125 without regressions in
Jazz. Iter 62 was a tools-only parallelization with no chord-output impact.

Previous baseline (Iteration 54, corpus regeneration 2026-05-11):
- 3-way genuine BIR=true: 14
- 3-way genuine BIR=false: 132
- Commit: f92a4f1a3b (greedy-expand segmentation, batch path)

Iteration 54 switched `batch_analyze` from Jaccard-based segmentation
to greedy-expand, producing different (improved) chord boundaries. The bridge path
(`notationcomposingbridgehelpers.cpp`) still uses Jaccard; bridge replacement is in
progress (Task #62).

Previous baseline (Iteration 46, corpus regeneration 2026-05-09):
- 3-way genuine BIR=true: 21
- 3-way genuine BIR=false: 128

Iteration 46 extended `supportsContextualInversionBonuses` and
`qualifiesForCompleteTriadInversionBonus` to include Augmented and HalfDiminished quality
types. This removed a systematic disadvantage that was preventing correct inversion
candidates from appearing in results[]. The extension reduced bassIsRoot=true errors by 11
and bassIsRoot=false errors by 49 without introducing regressions.
Commit: 36bf4738a8

Previous baseline (Iteration 36, corpus regeneration 2026-05-08 with new alternatives JSON):
- 3-way genuine BIR=true: 32
- 3-way genuine BIR=false: 177

NOTE — counting methodology changed in Iteration 36: `batch_analyze` now emits
`rootPitchClass`, `bassPitchClass`, `quality`, and `bassIsRoot` on each alternative
entry. This activated the previously-dormant `_matches_alternative` logic in
`compare_analyses.py`, which reclassifies regions where music21's chord matches our
2nd/3rd candidate from `chord_disagree` to `near_agree`. Near-agree cases are
excluded from the genuine-error counts; disabling this logic restores the Iter 32
counts exactly (48 / 787). The new baselines are correct: near-agree cases are
genuine partial successes, not uncounted failures. Raw-field scans (Gate M etc.)
are unaffected — they query `.ours.json` alternatives directly without using the
chord_disagree/near_agree classification.

The Iter 36 `batch_analyze.cpp` change (structured fields on alternative entries)
was originally lost to a git reset and re-recovered at **commit `5df8421114`**
(2026-05-10). Without this commit a fresh build reverts to pre-Iter-36 counts
(~700 BIR=false); the 21/128 baseline depends on both `36bf4738a8` and
`5df8421114` being present.

**Jazz baseline (Iteration 54 binary, validated 2026-05-11) — hard stop reference:**
- 3-way genuine BIR=false: 12  ← hard stop: must remain ≤ 75 for any gate
- Commit: f92a4f1a3b

Previous Jazz baseline (Iteration 46 binary, validated 2026-05-09):
- 3-way genuine BIR=true: 106  (Jazz harmony is outside Baroque gate scope — not a target)
- 3-way genuine BIR=false: 20
- Total regions: 9389 across 353 scores; chord identity agreement 80.3%

Note: The Jazz preset's low maxTotalInversionContextBonus (0.6) suppresses inversions,
so most Jazz errors are root-position misidentifications (BIR=true), not inversion errors.

Previous figures for reference (Iteration 32, Baroque):**
- 3-way genuine BIR=true: 48
- 3-way genuine BIR=false: 787
(With _matches_alternative disabled these are still recoverable from the Iter 36 corpus.)

Iteration 32 changes:
Gate L — prefer same-root Major over root-position Augmented plain triad (TYPE-A quality
correction). When the winner is a plain Augmented chord (no 7th extension) with
bassIsRoot=true and a runner-up has the same root AND same bass (root-position), has
Major quality, its root is diatonic to the key, and the score margin is ≤ 0.35, swap
to the Major reading.
4 BIR=true fixes (bwv144.6 B+→B, bwv245.15 E+→E, bwv312 E+→E, bwv245.37 F+→F);
BIR=false unchanged at 787.

Previous baselines for reference:
Iteration 30 (2026-05-08): BIR=true=52, BIR=false=787.
Gate K — prefer first-inversion augmented over root-position augmented. When the
winner is Augmented bassIsRoot=true and a runner-up has the same bass note at interval+4
from its own root (I4 = major-third inversion), the runner-up quality is Augmented or
Major+SharpFifth, the runner-up's root is diatonic to the key, and the score margin
is ≤ 0.20, swap to the first-inversion reading.
1 BIR=true fix (bwv40.6 m=6: A+ → F#5/A); BIR=false unchanged.

**IMPORTANT — corpus JSONs must be regenerated before updating baselines.**
`analyze_inversion_errors.py` reads existing `.ours.json` files and will silently
report stale numbers if those files are not current. Whenever you update the BIR
baselines here, you must first regenerate the corpus (as above), then run the script
against the per-preset dir and record the new figures.

**`--corpus-dir` (Stage 2.2-ii Rider 1).** The script now reads BOTH `.ours.json` and
`.music21.json` from one per-preset dir and validates that dir's
`corpus_manifest.json` (via `characterise_bir_false.validate_corpus_dir`) before
measuring — closing the former hardcoded-flat-`tools/corpus` music21 read. The
"Three-way music21_dcml_agree genuine errors" split is the headline BIR=true/BIR=false
pair (Baroque 24/13, Jazz 35/7; the 13/7 half is what `characterise_bir_false.py`
independently reproduces). `--ours-dir` is kept as a deprecated, unvalidated alias.

```
# per-preset (validates manifest):
python tools/analyze_inversion_errors.py --corpus-dir tools/corpus/baroque   # 24/13
python tools/analyze_inversion_errors.py --corpus-dir tools/corpus/jazz      # 35/7
# no-arg default is now the validated tools/corpus/baroque (Stage 2.3 Rider 1):
python tools/analyze_inversion_errors.py                                     # == --corpus-dir tools/corpus/baroque → 24/13
```

Run after any change that could affect chord identification quality. If the numbers
change unexpectedly (i.e. not due to an intentional scoring or gate change), stop and
report before proceeding.

---

## 3. Running MuseScore Studio (GUI)

```
cd C:\s\MS\ninja_build_rel
./musescore5.exe
```

---

## 4. Running Score Reading and Analysis Tools

### Batch Analyzer

```
cd C:\s\MS\ninja_build_rel
./batch_analyze.exe --help
```

**`--section-level` (Stage 2.2-ii diagnostic flag, default OFF).** Runs the
user-facing section pipeline (`analyzeSection`: measure layout, gap-tone
insertion, key/mode stabilization, sparse-quality refinement) on top of the batch
region stream, giving the measure-aligned (per-beat) view instead of the coarse
cross-barline regions. It only affects `--dump-regions batch` and does **not**
change the committed BIR gate (which stays at batch granularity). Flag-off output
is byte-identical to HEAD. Background and A/B in `cc_stage2_2_ab_dossier.md`.

```
./batch_analyze.exe "<score>" --section-level > /tmp/sec.json; echo "exit:$?"
```

### Python Score Tools

Activate the project virtual environment first:

- PowerShell: `& .venv\Scripts\Activate.ps1`
- CMD: `.venv\Scripts\activate.bat`

Common scripts:
- `tools/inspect_musicxml.py` — Inspect MusicXML files
- `tools/compare_omnibook.py` — Compare jazz corpus results
- `tools/run_validation.py` — Run validation on corpora

---

## 5. Environment Setup

- **Python:** Use the project virtual environment at `.venv/`
- **CMake/Ninja:** All configuration is handled by `setup_and_build_fast.bat`
- **MSVC:** All build scripts call `vcvars64.bat` automatically

---

## 6. Troubleshooting

- If you see build errors about missing CMakeCache or googlemock, the build tree may be stale. Delete `ninja_build_rel/` and re-run `setup_and_build_fast.bat` followed by `setup_and_build.bat`.
- If tests fail, check STATUS.md for known failures.
- For Python errors, ensure `.venv` is activated and dependencies are installed (`pip install -r requirements.txt`).
- **Note:** `build.release/` has a stale CMake tree (missing googlemock). Always use `ninja_build_rel/`.

---

## 7. Score Locations

### Corpus scores (validation)

```
tools/dcml/corelli/MS3/op01n08d.mscx
tools/dcml/chopin_mazurkas/MS3/BI16-1.mscx
tools/dcml/bach_chorales/...
tools/dcml/beethoven/...
tools/dcml/mozart_piano_sonatas/MS3/K279-1.mscx
```

### Extra scores (QA and new corpus)

```
C:\s\MS\tools\extra scores\              — jazz root (47 scores)
C:\s\MS\tools\extra scores\piazzolla\   — 6 Piazzolla scores
C:\s\MS\tools\extra scores\steely dan\  — 11 Steely Dan scores
```

### Key individual scores frequently referenced

```
C:\s\MS\tools\extra scores\the-eye-of-the-hurricane-herbie-hancock.mscz
C:\s\MS\tools\extra scores\autumn-leaves-bill-evans.mscz
C:\s\MS\tools\extra scores\all-the-things-you-are.mscz
C:\s\MS\tools\extra scores\giant-steps-john-coltrane.mscz
C:\s\MS\tools\extra scores\so-what-miles-davis.mscz
```

### Test data

```
src/composing/tests/data/chordanalyzer_catalog.musicxml
src/composing/tests/data/chordanalyzer_context.musicxml
src/notation/tests/notationtuning_data/   — MSCX fixtures for notation tests
```

---

## 8. Updating This Guide

- Edit this file (`BUILD_AND_TEST.md` in the project root) to keep instructions current.
- Update baseline test counts whenever the suite changes.
