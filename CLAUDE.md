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
- Run the build: `cmd.exe //c "C:\s\MS\setup_and_build.bat"`
- Run the tests: `./composing_tests.exe` from `ninja_build/`
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

```
# Build (from any directory — bat handles cwd)
cmd.exe //c "C:\s\MS\setup_and_build.bat"

# Run tests (must be in ninja_build/)
cd C:\s\MS\ninja_build && ./composing_tests.exe

# Mismatch report written to:
src/composing/tests/chord_mismatch_report.txt
```

## Conventions

- American English throughout — "analyzer" not "analyser"
- No confirmation prompts between analyse → implement → build → test steps
- Commit only when explicitly asked
