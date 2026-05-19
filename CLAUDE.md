# Claude Code — Standing Instructions for This Repository

## Project context

This is MuseScore Studio. The active development area is the `composing` module
(`src/composing/`), which implements harmonic analysis. See
`C:\Users\vince\.claude\projects\c--s-MS\memory\project_chord_analyzer.md` for
full project context.

## Autonomous operation — composing module

When working on the `src/composing/` module you are **pre-authorized** to:

- Edit any file under `src/composing/` without asking for confirmation
- Edit `src/notation/internal/notationaccessibility.cpp` without asking
- Edit `ARCHITECTURE.md` (project root) without asking
- Run the build: `powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"`
- Run the tests: `./composing_tests.exe` from `ninja_build_rel/`
- Read `src/composing/tests/chord_mismatch_report.txt` after each test run

**Standard loop for mismatch reduction work** — do all of the following without
stopping for confirmation:
1. Analyse the mismatch(es)
2. Implement the fix in `chordanalyzer.cpp`
3. Build
4. Run tests and read the mismatch report
5. Report results (mismatches before → after, any regressions)

Only stop and ask if:
- A regression is introduced (mismatch count goes up or a previously passing
  test fails)
- A change would touch files **outside** `src/composing/` and
  `notationaccessibility.cpp`
- The catalog XML (`chordanalyzer_catalog.musicxml`) needs to be modified
  (ground-truth changes require explicit approval)
- You are uncertain whether a fix is correct and want a second opinion

## Build and test commands

**Always read these two files at the start of every session:**
- `C:\s\MS\build_and_test.md` — authoritative commands for all build variants, both test suites, and all Python tools
- `C:\s\MS\STATUS.md` — current BIR baselines, HEAD commit, active iteration, and known regressions

Do not rely on memory of previous sessions for BIR numbers or iteration state — read STATUS.md.

```
# Build — use PowerShell Start-Process (cmd.exe //c fails in MSYS2/Git Bash)
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"

# Run composing tests (must be in ninja_build_rel/)
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe

# Run notation tests — includes P1/P2/P3/P4 pipeline regression test
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe

# Corpus quality check (always --preset Baroque unless iteration says otherwise)
cd C:\s\MS && python tools/analyze_inversion_errors.py

# Mismatch report written to:
src/composing/tests/chord_mismatch_report.txt
```

**Both test suites must pass after every code change.** The notation tests include
`pipeline_snapshot_tests` which pins P1/P2/P3/P4 output against golden JSON files.
If a change intentionally alters chord output (e.g. a new inversion gate fires),
the pipeline snapshot goldens need refreshing. Note: `pipeline_snapshot_tests.exe`
is a SEPARATE binary from `notation_tests.exe` — pass `--update-goldens` to it:
```
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens
```
Then re-run `./pipeline_snapshot_tests.exe` to confirm all pass.
Only run `--update-goldens` when the output change is verified correct.

## Gate threshold and preset policy

Gate thresholds (e.g. Gate I: 0.45, Gate K: 0.20, Gate L: 0.35) are **calibrated
against the Baroque corpus** and are intentionally Baroque-specific. Do NOT adjust
them to accommodate other musical styles.

**Before committing any gate addition or modification**, corpus analysis must be run
for BOTH Baroque and Jazz presets. Any BIR=false increase in either preset is a
hard stop:

```
# Baroque
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py

# Jazz  (run immediately after — reuses same output dir)
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

If a gate causes BIR=false regressions in a non-Baroque preset, the correct fix is:
1. A tighter **structural entry condition** that excludes the problematic chord type
   regardless of preset (preferred — e.g. an extension guard blocks augmented+seventh
   chords in all styles), OR
2. A **preset-specific threshold override** that leaves the Baroque-tuned value unchanged.

Never widen a Baroque-tuned threshold to cover a non-Baroque edge case.

## Score corpora

For any task involving scores (validation, snapshot tests, manual QA,
LLM-triage, qualitative review), read `docs/score_inventory.md` first. It
maps every score location to its intended use and lists the do-not-touch
files. Companion references: `tools/REPRODUCIBILITY.md` (how to recreate
corpora) and the JSON registries (`tools/corpus_registry.json`,
`tools/extra_scores_registry.json`).

## Local patches — do not revert

The following changes have been made intentionally to fix bugs unrelated to the
composing module. Do **not** revert them, and do not let build scripts or
dependency updates overwrite them without explicit approval.

### Windows Snap fix — `muse` submodule (applied 2026-05-14)

**File:** `muse/framework/ui/internal/platform/windows/winwindowscontroller.cpp`  
**Function:** `calculateWindowSize()`

Two lines were removed that set `ptMinTrackSize` equal to the full monitor work
area inside the `WM_GETMINMAXINFO` handler. This told Windows the minimum
allowed window size was the entire screen, which prevented Windows Snap from
resizing a maximised MuseScore window into a chosen snap zone (the window
stayed full-screen and lost its title-bar controls).

The fix: `ptMaxSize` and `ptMaxPosition` are kept (they correctly constrain the
maximised position); `ptMinTrackSize` is intentionally left unset.

Upstream issue: musescore/MuseScore#25823 (related cousins: #21344, #16794).  
Introduced by upstream commit `4ad218709` (5 Aug 2025).  
**Do not restore the `ptMinTrackSize` lines.**

## VS Code extension — bash command rules (MANDATORY, every session)

The Claude Code VS Code extension (v2.1.141+) has a 15-second stall detector. If the
API stream is silent for >15 seconds — which happens any time a bash command is running
— the extension marks the session `idle` and hands control back to the user, even though
CC is still running. This causes silent disconnects that are hard to detect.

**Two rules that apply to every bash command, no exceptions:**

**Rule 1 — Always append `; echo "exit:$?"` to any command that may return non-zero.**
A non-zero exit code also triggers an immediate idle transition. The echo always returns 0.
- BAD:  `./pipeline_snapshot_tests.exe --gtest_filter='*name*'`
- GOOD: `./pipeline_snapshot_tests.exe --gtest_filter='*name*'; echo "exit:$?"`
- BAD:  `grep -n "pattern" file.cpp`
- GOOD: `grep -n "pattern" file.cpp; echo "exit:$?"`

**Rule 2 — Never let a single bash call produce large output.**
Large output (thousands of lines) takes >15 seconds to process and triggers the stall
detector. Redirect to a file and read separately.
- BAD:  `./pipeline_snapshot_tests.exe`  (many failing tests = large output)
- GOOD: `./pipeline_snapshot_tests.exe > /tmp/snap_out.txt 2>&1; echo "exit:$?"`
         then `head -50 /tmp/snap_out.txt`
- BAD:  `batch_analyze <score> --dump-regions notation`
- GOOD: `batch_analyze <score> --dump-regions notation > /tmp/out.json; echo "exit:$?"`
         then `head -50 /tmp/out.json`

Build commands via `Start-Process` are isolated from these rules (exit code not exposed).

## Conventions

- American English throughout — "analyzer" not "analyser"
- No confirmation prompts between analyse → implement → build → test steps
- Commit only when explicitly asked
