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

**Current baseline: 378/378** passing.

### Notation Tests

```
./notation_tests.exe
```

**Current baseline: 51/51** passing.

### Batch Analyze Regression Tests

```
python tools/test_batch_analyze_regressions.py --batch-analyze ninja_build_rel/batch_analyze.exe --repo-root .
```

Output: prints `batch_analyze regressions passed` if successful.

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
