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
/c/s/MS/ninja_build_rel/batch_analyze.exe "<score>" "<out.ours.json>" --preset Jazz --joint-inference C:/s/MS/tools/joint_estimator
```

**★ THE `--joint-inference` FLAG IS NOT OPTIONAL FOR A PRODUCTION MEASUREMENT (corrected
2026-08-03; this line previously showed the invocation without it).** The joint estimator is the
production inference layer on the batch/corpus surface (CLAUDE.md gate block (A), the OI-178
adoption), but **the flag defaults OFF** — `jointInferenceDir` is initialised empty at
`tools/batch_analyze.cpp:4917` and the joint path runs only under `if (!jointInferenceDir.empty())`
at `:5590`. **Without the flag, `batch_analyze` runs the legacy `analyzeScore` pipeline** — the
dormant one awaiting deletion at the OI-180 retirement map. A session that follows a flag-less
recipe measures the wrong system and will not be told.

**When it may be omitted**, each case for a stated reason:

- **a legacy-path diagnostic that is meant to run the legacy path** — the retired batch stop
  (§2, Corpus Regression Check) and the `--section-level` view (§4), both marked as such where
  they appear;
- **a return-early diagnostic dump** (`--dump-*`, `--decode-*`, the joint parity drivers), which
  returns before any analysis and is byte-identical either way;
- **`--help`**, and `test_batch_analyze_regressions.py`, which pins the tool's own behaviour.

Anything else — any measurement whose number is meant to describe what this system does — takes
the flag. `run_bach_preset.py` passes it through (`--joint-inference DIR`, `:352`, `:436`).

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

**Current baseline: 974/974** passing, 2 disabled (verify with CC — count changes as tests are added).

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

**★ THIS IS THE RETIRED BATCH STOP, AND THESE COMMANDS REGENERATE THROUGH THE LEGACY PIPELINE
(stated 2026-08-03; the commands themselves are unchanged).** The governing hard stop is the
robust unit in CLAUDE.md gate block (A), not this. `characterise_bir_false.py` is kept as a
per-region diagnostic, and its `52/24/52` case-identity sets are LEGACY-pipeline figures — so the
regen below correctly omits `--joint-inference`, because adding it would measure a different
system than the one those sets describe.

**★ BUT THE OUTPUT DIRECTORY IS THE PRODUCTION ONE, AND THAT IS THE TRAP.** `run_bach_preset.py`
**clean-slates** its `--output-dir` before regenerating, and `tools/corpus/<preset>` is the dir
`tools/a8_rebaseline_measure.py` reads for the block-(A) hard stop (`:290-294`, default corpus
root `tools/corpus`). Running the commands below **as written replaces the joint-estimator corpus
with legacy output** — after which any robust-stop measurement compares the legacy pipeline
against a joint-estimator reference, and says nothing about a regression. Tracked at
`OPEN_ITEMS.md` OI-307; the destination is still the one below, and redirecting it is a ruling
(OI-312).

**★ THE MANIFEST NOW CATCHES IT (corrected 2026-08-03; this block previously said it did not).**
`corpus_manifest.json` is at **schema 2** and carries `inference_arm` — `joint`, `legacy`,
`mixed` or `unknown` — alongside the two sources it was derived from: `inference_arm_requested`
(what the invocation asked for) and `inference_arm_observed` (what the produced files say, read
from each `.ours.json`'s `analysisPath`; `tools/batch_analyze.cpp:4695` writes `"joint"`, the
standard writer at `:1448` writes `"batch"`). `characterise_bir_false.validate_corpus_dir` gains
an `expect_arm` argument, and `a8_rebaseline_measure.py` declares `joint` by default — so running
the commands below and then measuring the block-(A) hard stop is now **refused**, rather than
reported as a regression. Two states are deliberately not fatal: a manifest predating the field
reports **ARM-UNKNOWN** loudly (the declared, bounded transition, #23 — retirement condition in
`characterise_bir_false.ARM_UNKNOWN_IS_FATAL`), and a caller that declares no expectation is
unaffected. Measured, both directions, at
`tools/audit/corpus_arm_establishment.json`; the arm of every corpus directory on disk at
`tools/audit/corpus_arm_backstamp.json`. Inspect or re-establish with:

```
python tools/audit/corpus_arm_stamp.py --scan     # every corpus dir and the arm its files report
python tools/audit/corpus_arm_stamp.py --check    # the guard: the gate corpora are the joint arm
```

**The commands below are UNCHANGED** — they are the procedure of record, and CLAUDE.md gate block
(C) carries the same two pairs. **Redirecting them to a scratch dir would fix the hazard, and it
is deliberately not done here:** that is a change to a procedure a user-ratified surface also
states, so it is reported for a ruling rather than taken (OI-307), and this note is the warning
in the meantime.

```
# Baroque (primary — per-preset dir, regenerated + manifest-stamped)
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus/baroque
cd C:\s\MS && python tools/characterise_bir_false.py --corpus-dir tools/corpus/baroque

# Jazz (independent dir — no shared state, run in any order)
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz --output-dir tools/corpus/jazz
cd C:\s\MS && python tools/characterise_bir_false.py --corpus-dir tools/corpus/jazz
```

**Regenerating the PRODUCTION corpus — the arm gate block (A) is baselined on — takes the flag:**

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus/baroque --joint-inference C:/s/MS/tools/joint_estimator
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz    --output-dir tools/corpus/jazz    --joint-inference C:/s/MS/tools/joint_estimator
cd C:\s\MS && python tools/run_bach_preset.py --preset Default --output-dir tools/corpus/default --joint-inference C:/s/MS/tools/joint_estimator
```

**Stage 2.2a (M3 fix):** each preset now has its own dir under `tools/corpus/` and a
`corpus_manifest.json`. `run_bach_preset.py` clean-slates the dir before a regen and
**exits nonzero** unless every source score produced output — **352/352 at HEAD**, the expected
count being derived from the source `.xml` files and not hard-coded (*corrected 2026-08-03: this
line read `353/353`, the figure from the 2026-06-15-era regens; measured at HEAD the `.xml`
population is 352 and all three gate manifests record `expected_count` 352. `CLAUDE.md` gate
block (C) already states it this way*). `characterise_bir_false.py`
**refuses** to measure a dir whose manifest is missing/incomplete, whose `.ours.json`
fingerprints don't match the manifest (the old shared-`tools/corpus` contamination is
now structurally impossible and loudly detected), or — since 2026-08-03 — whose recorded
inference arm is not the one the measurement declared. Gate on **case identity** (not the
bare integer):
**Re-baselined 2026-06-13 (corrected GT parser): Baroque 53 / Jazz 24 / Default 53** — a
strict superset of the old 13/7/14 (0 lost, oracle-verified); the L3-wiring delta (−4 / +1 / −4,
2026-06-26) later moved the prior 57/23/57 → 53/24/53 (the SET, not the integer, is the gate).
The authoritative `stem@tick`
identity sets live in **CLAUDE.md** (gate section); see `cc_metric_rebaseline_report.md` +
`cc_gate_rebaseline_verify_report.md` for provenance. ~95% of the added mass is legitimate
ambiguity (symmetric-dim7 ≈53% Baroque + viio↔V7 share-tone).
(`analyze_inversion_errors.py` is the separate secondary `bassIsRoot` metric; its three-way
genuine split was Baroque 24/13, Jazz 35/7 under the OLD parser — **NOT yet re-measured under
the corrected parser; treat as stale/pending**. Since Stage 2.2-ii it also takes
`--corpus-dir` — see §4.)

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
pair (was Baroque 24/13, Jazz 35/7 under the OLD parser — **stale/pending re-measurement
under the corrected parser**; the BIR=false half is what `characterise_bir_false.py`
independently reproduces, now **53/24**, Default 53). `--ours-dir` is kept as a deprecated,
unvalidated alias.

```
# per-preset (validates manifest):
python tools/analyze_inversion_errors.py --corpus-dir tools/corpus/baroque   # OLD 24/13 — re-measure under corrected parser
python tools/analyze_inversion_errors.py --corpus-dir tools/corpus/jazz      # OLD 35/7 — re-measure under corrected parser
# no-arg default is now the validated tools/corpus/baroque (Stage 2.3 Rider 1):
python tools/analyze_inversion_errors.py                                     # == --corpus-dir tools/corpus/baroque
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

**`--section-level` (Stage 2.2-ii diagnostic flag, default OFF) — a LEGACY-path view, and
correctly shown without `--joint-inference`.** The joint path returns at
`tools/batch_analyze.cpp:5590`, before the section pipeline this flag drives is reached, so the
two do not combine: what `--section-level` shows is the legacy region stream at measure-aligned
granularity, which is what it was built to show. Runs the
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
