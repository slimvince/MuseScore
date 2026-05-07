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

**Always read `C:\s\MS\build_and_test.md` at the start of every session** — it has the authoritative commands for all build variants, both test suites, and all Python tools.

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

## Score corpora

For any task involving scores (validation, snapshot tests, manual QA,
LLM-triage, qualitative review), read `docs/score_inventory.md` first. It
maps every score location to its intended use and lists the do-not-touch
files. Companion references: `tools/REPRODUCIBILITY.md` (how to recreate
corpora) and the JSON registries (`tools/corpus_registry.json`,
`tools/extra_scores_registry.json`).

## Conventions

- American English throughout — "analyzer" not "analyser"
- No confirmation prompts between analyse → implement → build → test steps
- Commit only when explicitly asked
