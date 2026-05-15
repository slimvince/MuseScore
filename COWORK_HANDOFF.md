# Cowork Session Handoff — MuseScore Studio Harmonic Analysis

*Written 2026-05-14 to bootstrap a fresh Cowork session with zero context.*

---

## What this project is

MuseScore Studio. The active development area is `src/composing/`, which implements
harmonic analysis (chord detection, inversion scoring, key inference). The main file
is `src/composing/analysis/chord/chordanalyzer.cpp`. The bridge between the composing
module and the notation layer is `src/notation/internal/notationharmonicrhythmbridge.cpp`.

Two mandatory reads at the start of every session:
- `C:\s\MS\build_and_test.md` — all build/test/tool commands
- `C:\s\MS\STATUS.md` (header only, first ~10 lines) — current baselines and HEAD commit

---

## Two worktrees

- `C:\s\MS` — **master** branch (main working tree — use this for all development)
- `C:\s\MS-llm-triage` — `llm-triage` branch (separate worktree, only for LLM triage work)

All Iter 78 work is on **master**. Always confirm which worktree CC is in before giving it instructions.

---

## Current state (as of 2026-05-15, updated after Iter 89 + DCML comparator commit)

- **HEAD:** `4cb1bfb274` on master (last code commit: `eefa412b6f` — DCML time-overlap comparator —
  tools/compare_analyses.py + tools/rerun_dcml_comparison.py)
- **Prior HEAD in cycle:** `2085f11322` (Iter 89 — pc=8 G#/Ab TPC sharp-honor fix)
- **Working tree (uncommitted):**
  - Doc drift only after this update (`ARCHITECTURE.md`, `CLAUDE.md`, `STATUS.md`,
    `COWORK_HANDOFF.md`) — leave alone unless explicitly asked
- **Composing tests:** 407/407 passing
- **Notation tests:** 50/52 passing (2 pre-existing Corelli failures remain — do NOT regress:
  `CorelliOp01n08dOpeningAndSparseLateBeats`, `CorelliOp01n08dUserReportedChordTrackAudit`)
- **Pipeline snapshot tests:** 11 passed / 1 skipped (skip = `PipelineDivergenceCObservation.
  GenerateReport`, intentional opt-in)
- **BIR baselines:** BIR=true=4, BIR=false=118, Jazz BIR=false=7 (unchanged since Iter 82)
- **Chord mismatch report:** 4 RealDiff (pinned), 127 ConventionDiff (Jazz)

---

## Iter 78 fixes (all committed, do not re-implement)

**Fix A** — `notationharmonicrhythmbridge.cpp`, `absorbShortRegions` lambda:
Short regions are only absorbed into the previous region when they share the same root
(`sharesPrevRoot`). A differently-rooted short region keeps its own boundary.

**Fix B** — `chordanalyzer.cpp` line ~129, `pitchClassName()`:
G# → Ab flattening is exempted at `keySignatureFifths == 0` (A minor), where G# is
the leading tone. Condition: `pc == 8 && keySignatureFifths < 3 && keySignatureFifths != 0`.

**Fix C** — `chordanalyzer.cpp` lines ~1762-1766:
Augmented template score ×0.5 when `distinctPcs <= 2` and root PC weight is at or
below `extensionThreshold`. Prevents root-absent 2-PC guesses winning as Augmented.

---

## Iters 79–84 — all committed

- **Iter 79** (`cbd7230c1f`) — augmented bare-root guard + qualitySuffix Dim/HalfDim fix
- **Iter 80** (`b4a375db45`) — refreshed 7 stale pipeline snapshot goldens
- **Iter 81** (`9d2a70cef4`) — removed dead Jaccard code; notation tests now 52 total / 50 passing
- **Iter 82** (`57511f012f`) — Gates E/I absent-root guard; BIR=false=118, BIR=true=4, Jazz BIR=false=7
- **Iter 83** (`1c57ebcac2`) — batch path anchor end-tick fix (port Iter 77 Fix B)
- **Iter 84** (`4da8252c9e`) — R4 narrow fix: G# leading-tone exemption extended to keyFifths=1 (A melodic minor regime)

## Iter 84 detail (do not re-implement)

**File:** `src/composing/analysis/chord/chordanalyzer.cpp`, lines ~117–153

`pitchClassNameFromTpc()` had a G# (pc=8) exemption from Ab-normalization at `keyFifths==0`
(Iter 78 Fix B, for A natural minor). A melodic minor ("Amel") maps via `resolveToFifths()`
to its Dorian parent at `keyFifths=1`, falling outside the exemption → G# was spelled "Ab".

Fix: added `&& keySignatureFifths != 1` to the normalization condition, and extended the
TPC-disambiguation block to also fire at `keyFifths==1 && pc==8` (so flat-authored Ab with
tpc≤14 in that regime is still correctly spelled flat).

Result: bach_chorale_003 — 3 chord symbols corrected (Abm7b5/B→G#m7b5/B, E/Ab→E/G# ×2).
bach_chorale_003 golden refreshed. BIR unchanged (BIR operates on root_pc/bass_pc).

**Deferred — R4 family B (chorale_137, later iteration):**
- pc=6 (F#/Gb): no TPC-honor block exists for pc=6 at all; unconditionally returns Gb at keyFifths<0
- Flat-authored Ab bass in V/V context (tpc=10 in chorale_137 m2): heavier "chord-3rd-of-major-triad" override, out of scope

---

## Iters 85–89 + DCML comparator — all committed

- **Iter 87** (`2dd2f35c17`) — bass-b7 post-merge re-stamp in batch_analyze.cpp
  (`analyzeScore` merge discarded MinorSeventh extension stamped by Iter 86; post-filtered
  re-stamp pass at batch_analyze.cpp:1846–1880 fixes 281 of 293 b7-bass slash-chord cases)
- **Iter 88** (`bea00f3482`) — honor sharp F# TPC for pc=6 in flat keys (extends
  TPC-disambiguation block to fire at `keyFifths<0 && pc==6`; Gb→F# in D/F# and similar
  contexts)
- **Iter 89** (`2085f11322`) — honor sharp G# TPC for pc=8 across flat and mildly-sharp
  keys (removed pc=8 from Iter 78 flattening block; added `keyFifths<0 && pc==8` and
  `keyFifths==2 && pc==8` to TPC-honor block; survey script `tools/survey_pc8_flat_authored_bass.py`)
- **DCML comparator** (`eefa412b6f`) — new time-overlap comparator in compare_analyses.py
  (mode='time-overlap', lenient-OR-50% overlap threshold) + rerun_dcml_comparison.py
  re-aggregation driver. Old beat-snap 69.1% figure retired (biased +21pp). New primary
  metric: 47.8% weighted root agreement across 10 non-Bach corpora (DCML-anchored).
  Bach chorales: 64.9% overall, 87.2% chord-identity, 100% alignment.

**Iter 90 — shelved (no commit):**
122 wrong-root cases characterized (tools/analyze_wrong_root_iter90.py,
tools/iter90_wrong_root_characterization.txt). 84% are iii/III triad confusion — non-local
ambiguity. Both Variant A (+12 errors) and Variant B (+22 errors) regressed. Design note:
`docs/iter90_bass_as_root_promotion_shelved.md`. Future path: Iter 91, bridge-level
adjacent-context pass using nextRootPc/previousRootPc from ChordTemporalExtensions.

---

## Standing rule — CC instruction preamble (MANDATORY, every single CC session)

CC starts with ZERO context every time. Every instruction to CC must open with:

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only),
> `C:\s\MS\build_and_test.md`
>
> **Current state:** Branch `master`, HEAD `4cb1bfb274` (last code commit: `eefa412b6f` — DCML time-overlap comparator;
> prior: Iter 89 pc=8 G#/Ab fix at `2085f11322`).
> Baselines: 407/407 composing, 50/52 notation (2 pre-existing Corelli failures — do not
> regress), pipeline_snapshot 11 passed / 1 skipped, BIR=true=4, BIR=false=118, Jazz BIR=false=7.

This preamble goes before EVERY task description, no exceptions.

---

## Windows Snap fix — do not revert

File: `muse/framework/ui/internal/platform/windows/winwindowscontroller.cpp`
Function: `calculateWindowSize()`

Two lines that set `ptMinTrackSize` equal to the full monitor work area were removed.
This prevented Windows Snap from working on maximised MuseScore windows.
`ptMaxSize` and `ptMaxPosition` are kept. `ptMinTrackSize` is intentionally left unset.

The fix is committed as a local-only branch in the muse submodule (`fix/windows-snap-ptmintracksize`
at `b9604805a`). The parent repo's master correctly pins the submodule pointer to this commit.
**Do not restore the `ptMinTrackSize` lines. Do not push the muse submodule to upstream.**

This is documented in `C:\s\MS\CLAUDE.md` which CC reads every session.

---

## Known CC/VS Code integration issues

**Stale `git index.lock`** — When CC loses contact with a running git process (a known
VS Code integration bug), `.git/index.lock` is left behind (0 bytes). Symptom: git
commands fail with "Unable to lock the index". Fix: verify no git process is running
(`tasklist | grep git`), then delete `.git/index.lock`. Safe to delete if file is
0 bytes and no git process is running.

**Silent disconnect — three distinct triggers (diagnosed 2026-05-14 from VS Code logs)**

VS Code sets the CC session to `idle` (handing control back to user) in these situations,
while the CC process keeps running invisibly. Dangerous to submit new tasks without waiting.

**Trigger 1 — Non-zero exit code:**
A bash command returns non-zero (failing tests, grep with no matches, etc.). The extension
sees this as an error and marks the session idle. CC keeps running.
Fix: append `; echo "exit:$?"` to every command that may return non-zero. The echo always
returns 0, so the extension sees a clean result.
- BAD:  `./pipeline_snapshot_tests.exe --gtest_filter='*name*'`
- GOOD: `./pipeline_snapshot_tests.exe --gtest_filter='*name*'; echo "exit:$?"`
- BAD:  `grep -n "pattern" file.cpp`
- GOOD: `grep -n "pattern" file.cpp; echo "exit:$?"`

**Trigger 2 — stream_idle_partial (long bash output):**
When a bash command produces large output and CC takes >~15 seconds to process the result,
the API stream goes idle between chunks. The extension logs `[WARN] [Stall] stream_idle_partial`
and marks the session idle. CC is still running and will eventually complete.
Fix: break long commands into smaller steps that produce incremental output. Pipe through
`head -N` to limit output size. Write large results to a file and read separately rather
than capturing in one bash call.
- BAD:  `batch_analyze <score> --dump-regions notation`  (may produce thousands of lines)
- GOOD: `batch_analyze <score> --dump-regions notation > /tmp/out.json; echo "exit:$?"`
         then `head -50 /tmp/out.json`

**Trigger 3 — stream_idle_partial (API latency, bytesTotal=0):**
When the Anthropic API takes >15 seconds to send the first token of a response (server load,
network hiccup), the extension logs `stream_idle_partial lastChunkAgeMs=15xxx bytesTotal=0`.
This can silently drop the panel even though CC recovers and keeps running. No reliable
prevention — it's server-side latency. If the panel goes silent mid-task without any bash
errors, this is likely the cause. Check the VS Code output log before resubmitting.

Build commands (setup_and_build.bat) are launched via PowerShell Start-Process which
isolates the exit code — less affected by trigger 1.

---

## .vscode/settings.json — muse submodule noise

VS Code detects `muse/.git` (submodule gitdir pointer) and prompts to open it as a
separate repository. Two settings suppress this in `C:\s\MS\.vscode\settings.json`:
- `"git.detectSubmodules": false` — stops VS Code treating submodules as separate SCM providers
- `"git.ignoredRepositories": ["C:\\s\\MS\\muse"]` — belt-and-suspenders ignore by path

If CC hasn't applied these yet, ask it to edit `.vscode\settings.json` accordingly,
then Ctrl+Shift+P → "Reload Window".

---

## Build commands (quick reference)

```
# Build
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"

# Tests (run from ninja_build_rel/)
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe

# Corpus quality check
cd C:\s\MS && python tools/analyze_inversion_errors.py

# Mismatch report location
src/composing/tests/chord_mismatch_report.txt
```

---

## LLM integration design — completed 2026-05-15

A full architectural design session for "Claude Composer" — natural-language interaction
with scores via an LLM of the user's choice (analogous to Claude Code / Copilot in IDEs).

**Two documents created / updated:**

- `docs/llm_integration.md` — comprehensive design document (11 sections). Read this
  before any implementation work on the LLM bridge.
- `ARCHITECTURE.md` §19 — high-level overview and key decisions (4 subsections).

**Key conclusions that are not obvious from reading the docs:**

- The Core Access Layer is a **facade over existing INotation* interfaces** — not a new
  information model. §5.2 has the full interface inventory. The point is to avoid
  translation loss, not to redesign the data model.

- LLM bridge uses the **stateless tier** (tool calls, musical addresses, no object
  references). Plugin API uses the **stateful tier** (EID-backed handles, event
  subscriptions). These are different programming models; do not conflate them.

- **Event subscriptions keep dependency direction one-way.** When `ScoreEventSource`
  (Core Access Layer) subscribes to `async::Channel<ScoreChanges>`, the subscription
  is initiated *from* the Core Access Layer *into* MuseScore. `async::Channel` stores a
  callback and fires it — it has no reference back to the subscriber. No reverse
  dependency is created.

- `src/composing/` is **not part of official MuseScore** — it is this project's own
  development. §10 and ARCHITECTURE.md §19.3 both note this explicitly.

- **MusicalAddress is the cross-cutting join key.** There are NO direct object
  references from Note → Staff or Note → Measure. A Note's address (`partId`,
  `staffIndexInPart`, `measureNumber`, `beat`, `voice`, `tick`) is the only locator.
  Querying "all notes in measure 12 of the Oboe" is a pure filter over addresses —
  no graph traversal. Harmony, Annotation, and Note at the same MusicalAddress are
  co-located: matching on address is the equivalent of a SQL join on a composite key.

- **Address does NOT uniquely identify a Note.** Multiple notes in the same chord
  share an identical MusicalAddress (same part + staff + measure + beat + voice).
  A `NoteId` is required to unambiguously identify a single note. The information
  model must carry NoteId on the Note entity.

- Subsection numbering in `llm_integration.md` §7 and §8 had a drift (labels said
  6.x and 7.x respectively) — fixed 2026-05-15.

---

## ms-core-api branch — decisions made 2026-05-15

A new branch and worktree for the Core Access Layer (protocol-neutral facade over
`INotation*` and friends, shared foundation for plugin API and LLM bridge).

**Branch:** `ms-core-api`  
**Worktree:** `C:\s\MS-core-api` ✓ created 2026-05-15  
**VS Code window:** separate window on `C:\s\MS-core-api`  
**CC context:** automatically separate (different path = different CC project memory)  
**CLAUDE.md:** ✓ written and committed on the branch — scoped to CAL, composing-module sections removed

**Known gap — build script:** `setup_and_build.bat` inherited from master hardcodes
`c:\s\MS\ninja_build_rel`. A `setup_and_build.bat` specific to `C:\s\MS-core-api`
needs to be created (pointing to `C:\s\MS-core-api\ninja_build_rel`) before the
first build attempt in the new worktree.

**Current state:** CLAUDE.md committed, no code written yet. Next steps:
1. Create `setup_and_build.bat` for the worktree
2. Create `src/ms-core-api/` skeleton (CMakeLists.txt + first interface headers)
3. Wire into root CMakeLists.txt
4. Create junction points for extensions/plugins (see below)

**Why `ms-core-api` as a name:** "plugin-api-v2" would imply the QML/Q_PROPERTY
protocol; this layer is protocol-neutral. It exposes capabilities (score read/write,
settings, project, playback, instruments) without committing to any binding technology.
Protocol-specific layers (QML bindings, JSON/tool-call schema for LLM) sit above it.

**Architecture:**
```
Plugin bindings (QML)   LLM bridge (JSON)   future protocols
        └───────────────────┴──────────────────┘
                    ms-core-api
              (capabilities, no protocol)
                    INotation* family
                    MuseScore DOM
```

**Dev environment prerequisite — junction points (one-time, do before first test run):**

Extensions and plugins are in `share/extensions/` and `share/plugins/` but
`appDataPath()` on Windows resolves to one level up from the exe (`C:\s\MS\` when
running from `ninja_build_rel\`). MuseScore looks for `C:\s\MS\extensions\` and
`C:\s\MS\plugins\` — neither exists without junctions. Fix:
```
mklink /J "C:\s\MS-core-api\extensions" "C:\s\MS-core-api\share\extensions"
mklink /J "C:\s\MS-core-api\plugins"    "C:\s\MS-core-api\share\plugins"
```
(Run as Administrator in cmd.exe. Do this in the ms-core-api worktree.)

**Full-stack test loop once junction points exist:**
1. Write C++ in `src/ms-core-api/` → build MuseScore5.exe
2. Write a minimal test extension: `manifest.json` + JS/QML in `C:\s\MS-core-api\extensions\your-test\`
3. Launch MuseScore5.exe, open a score, run the extension
4. No install step needed — extensions load from the junction-pointed directory

**Extension anatomy (v2 system):**
- `manifest.json` — declares URI, type (macros/composite/form), actions
- `main.js` or `Form.qml` — the extension logic
- API surface available to extensions: `api.log`, `api.interactive`, `api.engraving`,
  `api.converter`, `api.websocket` (see `muse/framework/extensions/api/extapi.h`)
- ms-core-api methods will be added here once implemented

**Legacy v1 plugins** (QML, old API) live in `share/plugins/`. They use the
`muse/framework/extensions/api/v1/` path and the old `PluginAPI`/`qmlRegisterType`
system. Relevant for understanding what exists; NOT the target for ms-core-api work.

---

## Key files

| File | Purpose |
|------|---------|
| `src/composing/analysis/chord/chordanalyzer.cpp` | Main analyzer — all scoring logic |
| `src/notation/internal/notationharmonicrhythmbridge.cpp` | Bridge — region segmentation |
| `docs/llm_integration.md` | LLM / Claude Composer full design document |
| `docs/quality_observations_iter76.md` | R1–R5 recurring themes for Iter 79+ |
| `docs/score_inventory.md` | Score paths for all test/corpus files |
| `STATUS.md` | Current baselines and HEAD — read every session |
| `build_and_test.md` | All build/test/tool commands |
| `CLAUDE.md` | Standing rules for CC — read every session |
| `tools/analyze_inversion_errors.py` | BIR corpus check |
| `muse/framework/extensions/api/extapi.h` | Current extension API surface (v2) |
| `muse/framework/extensions/internal/extensionsconfiguration.cpp` | Path resolution for extensions/plugins |
