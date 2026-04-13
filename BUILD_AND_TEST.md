# MuseScore Studio — Build and Test Instructions

This document provides comprehensive, step-by-step instructions for building MuseScore Studio, running all test suites, launching executables, and using the main Python tools. It is intended for new developers, automated agents, and any session that needs to recover full build/test/run knowledge after context loss.

---

## 1. Building the Project

### Official Build Script (Windows)
- **Always use:** `setup_and_build.bat` (project root)
- **How to run:**
  1. Open a Developer Command Prompt for MSVC 2022 (or compatible).
  2. Navigate to the project root (`c:\s\MS`).
  3. Run:
     ```
     cmd.exe /c "C:\s\MS\setup_and_build.bat"
     ```
  4. This script configures, generates, and builds the project using Ninja. The default build tree is `ninja_build_rel/`.

### Alternative Build Trees
- You may also see `builds/`, `build.release/`, or custom CMake/Ninja trees. Always prefer `ninja_build_rel/` unless otherwise specified.

---

## 2. Running Test Suites

### Notation Tests
- **Executable:** `notation_tests.exe`
- **Location:** `ninja_build_rel/`
- **How to run:**
  1. Open a terminal (PowerShell or CMD).
  2. Change directory:
     ```
     cd C:\s\MS\ninja_build_rel
     ```
  3. Run:
     ```
     ./notation_tests.exe
     ```
  4. Output: Shows passing/failing test count (e.g., 29/33 passing).

### Composing Tests
- **Executable:** `composing_tests.exe`
- **Location:** `ninja_build_rel/`
- **How to run:**
  1. Open a terminal and `cd` as above.
  2. Run:
     ```
     ./composing_tests.exe
     ```
  3. Output: Shows passing/failing test count (e.g., 299/299 passing).

### Batch Analyze Regression Tests
- **Python script:** `tools/test_batch_analyze_regressions.py`
- **How to run:**
     ```
     python tools/test_batch_analyze_regressions.py --batch-analyze ninja_build_rel/batch_analyze.exe --repo-root .
     ```
  - Output: Should print `batch_analyze regressions passed` if successful.

---

## 3. Running MuseScore Studio (GUI)

### Main Executable
- **Executable:** `musescore5.exe`
- **Location:** `ninja_build_rel/`
- **How to run:**
  1. Open a terminal and `cd` to `ninja_build_rel`.
  2. Run:
     ```
     ./musescore5.exe
     ```

---

## 4. Running Score Reading and Analysis Tools

### Batch Analyzer
- **Executable:** `batch_analyze.exe`
- **Location:** `ninja_build_rel/`
- **How to run:**
     ```
     ./batch_analyze.exe --help
     ```
  - See help output for options (corpus path, output directory, etc).

### Python Score Tools
- **Typical usage:**
     ```
     python tools/your_script.py [args]
     ```
- **Common scripts:**
  - `tools/inspect_musicxml.py` — Inspect MusicXML files.
  - `tools/compare_omnibook.py` — Compare jazz corpus results.
  - `tools/run_validation.py` — Run validation on corpora.

---

## 5. Environment Setup

- **Python:**
  - Use the project virtual environment: `.venv/`
  - Activate (PowerShell):
    ```
    & .venv\Scripts\Activate.ps1
    ```
  - Activate (CMD):
    ```
    .venv\Scripts\activate.bat
    ```
- **CMake/Ninja:**
  - All configuration is handled by `setup_and_build.bat`.

---

## 6. Troubleshooting

- If you see build errors, always re-run `setup_and_build.bat` from a clean state.
- If tests fail, check STATUS.md for known failures.
- For Python errors, ensure `.venv` is activated and dependencies are installed (`pip install -r requirements.txt`).

---

## 7. Updating This Guide

- Edit this file (`BUILD_AND_TEST.md` in the project root) to keep instructions current.
- Notify all developers and agents of changes.
