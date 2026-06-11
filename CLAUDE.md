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
# Baroque (per-preset dir — clean-slated and manifest-stamped each regen)
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus/baroque
cd C:\s\MS && python tools/characterise_bir_false.py --corpus-dir tools/corpus/baroque

# Jazz (independent dir — no contamination; order no longer matters)
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz --output-dir tools/corpus/jazz
cd C:\s\MS && python tools/characterise_bir_false.py --corpus-dir tools/corpus/jazz
```

Since Stage 2.2a (M3 fix) each preset writes to its **own** dir under `tools/corpus/`
and stamps a `corpus_manifest.json`. `run_bach_preset.py` clean-slates the dir at the
start of a regen and **exits nonzero** if the corpus is not 353/353 complete;
`characterise_bir_false.py` **refuses** to measure a dir whose manifest is missing,
incomplete, or whose `.ours.json` fingerprints do not match (preset contamination —
the old shared-`tools/corpus` failure mode). The gate is the **case-identity** set,
not a bare integer: Baroque = 13, Jazz = 7 with identities
`{bwv244.15, bwv245.17, bwv245.40, bwv422, bwv432, bwv45.7, bwv74.8}`.

(`tools/analyze_inversion_errors.py` is a *separate* secondary metric — `bassIsRoot`
27/22, not the 13/7 characterise gate — and still reads the legacy flat `tools/corpus`;
its `--corpus-dir`-ification is a deferred follow-up, out of Stage 2.2a scope.)

If a gate causes BIR=false regressions in a non-Baroque preset, the correct fix is:
1. A tighter **structural entry condition** that excludes the problematic chord type
   regardless of preset (preferred — e.g. an extension guard blocks augmented+seventh
   chords in all styles), OR
2. A **preset-specific threshold override** that leaves the Baroque-tuned value unchanged.

Never widen a Baroque-tuned threshold to cover a non-Baroque edge case.

**Preset scoring caps — corrected 2026-06-10:** `maxTotalInversionContextBonus` is
**never set on any code path** — both presets inherit the 2.0 default, and the cap is
currently non-binding (the four inversion bonuses sum to 1.85 Baroque/default, 0.75
Jazz). The formerly documented "Baroque=2.5 / Jazz=0.6" values were aspirational and
never implemented. Jazz's inversion behavior comes from its **reduced individual
inversion bonuses** (0.20/0.20/0.15/0.20 in `batch_analyze.cpp`), not the cap. Full
story in `docs/scoring_model.md` §4 (note below the "Other terms" table).

## Scoring model — `docs/scoring_model.md` (MANDATORY for scoring sessions)

**Read `docs/scoring_model.md` at the start of any session that touches scoring
logic in `chordanalyzer.cpp`** — this includes adding or modifying templates,
bonuses, guards, gates, score matrices, or post-scoring passes.

The document is the authoritative reference for how the scoring pipeline works,
why each term exists, and what invariants must not be broken. Violating these
invariants without reading the doc first has caused multiple failed attempts
(B1 leading-tone ambiguity, B2 ×4, B3 rotation-selector bypass).

**Sync rule — mandatory:** Any commit that adds or modifies a template, bonus,
guard, gate, or other scoring term in `chordanalyzer.cpp` **must** include a
corresponding update to `docs/scoring_model.md` in the same commit. The two
must never drift apart. Specifically:

- Adding a template: update the Templates section (§2), increment the template
  count in the array-size comment, add the guard description if applicable
- Adding or changing a bonus/gate: update the relevant §4 or §6 entry
- Adding a new constraint or dead end: add it to §8

**Staleness check:** The template count in `docs/scoring_model.md` §2 must
always match the `array<TemplateDef, N>` declaration in `chordanalyzer.cpp`.
If they differ, the doc is stale — update it before proceeding.

**Template additions — the `kTemplateCount` model (since `a236a0ff21`):** All
template-related array extents (the `analyzeChord` template array, `kDiagTemplates`,
the three score matrices, `kMasks` in `harmonicfunctionlayer.cpp`) are derived from
`analysis::kTemplateCount` in `chordanalyzer.h`, so the compiler enforces size
consistency — the old silent stack-buffer-overrun failure mode (a missed matrix
resize, caught in the B1 attempt 2026-06-04) is closed. Adding a template means:
1. Bump `analysis::kTemplateCount` N→N+1 (auto-resizes the matrices and `kMasks`)
2. Add the new `TemplateDef` entry in `analyzeChord` AND the byte-identical entry
   in `kDiagTemplates`
3. Add the interval bitmask to `kMasks` (a zero mask silently disables Gate R)

Remaining trap: bumping the constant **without** adding the entries
value-initializes a trailing all-zero template (silent) — always do both in the
same edit. The authoritative checklist is `docs/scoring_model.md` §9.

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
- never hallucinate or guess, verified facts only - better ask first if unsure.
