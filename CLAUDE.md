# Claude Code — Standing Instructions for This Repository (ms-core-api branch)

## Project context

This worktree is MuseScore Studio on the **`ms-core-api`** branch. The active
development area is the **Core Access Layer (CAL)** — a protocol-neutral C++
facade over MuseScore's existing `INotation*` interface family, intended as the
shared foundation for two downstream consumers:

- The **plugin API** (stateful tier: EID-backed object handles, event
  subscriptions, language bindings)
- The **LLM bridge / Claude Composer** (stateless tier: tool calls, musical
  addresses, no object references)

The CAL is **not a new information model**. It is a facade over interfaces that
already exist in `src/notation/`, `src/project/`, `src/playback/`, and
`muse/framework/`. The point is to give downstream consumers a clean, stable
boundary without each one wiring its own private path into MuseScore internals.

The full design — including the interface inventory, the three gaps the CAL
fills, and the explicit list of what the CAL is NOT responsible for — is in
[docs/llm_integration.md §5](docs/llm_integration.md). Read §5 before any
non-trivial implementation work.

**This branch does not work on `src/composing/`.** That module is active on
`master`; corpus runs, BIR baselines, mismatch reports, and chord-analyzer fixes
all belong there, not here. If a task seems to require composing-module changes,
stop and confirm — it likely belongs on master.

## Worktrees

- `C:\s\MS` — **master** branch. Composing-module development.
- `C:\s\MS-core-api` — **this worktree**, `ms-core-api` branch. CAL development.
- `C:\s\MS-llm-triage` — `llm-triage` branch. LLM triage tooling.

Always confirm which worktree CC is operating in before acting. The CLAUDE.md
in each worktree is intentionally different.

## Where new code lives

```
src/ms-core-api/                    (to be created)
├── CMakeLists.txt
├── iscorereader.h     ── read-side facade  (NoteList, HarmonyList, StructuralEvents)
├── iscorewriter.h     ── write-side facade
├── iscoretransaction.h── prepareChanges / commitChanges wrapper
├── isettingsreader.h  ── INotationConfiguration + IProjectConfiguration facade
├── isettingswriter.h
├── istatereader.h     ── selection, playback, project state
├── istatewriter.h
├── iinstrumentdatabase.h ── IInstrumentsRepository facade
├── internal/          ── implementations that delegate to INotation* family
└── tests/             ── unit tests against fake INotation* doubles
```

The exact file layout is provisional — finalize it as the first interfaces are
drafted. Headers and implementations should mirror the structure used elsewhere
in `src/` (public interface in module root, implementations in `internal/`).

Code in `src/ms-core-api/` may **read** any header in `src/notation/`,
`src/project/`, `src/playback/`, `src/engraving/`, and `muse/framework/`, and
may **depend on** the public interfaces declared there. It must NOT modify
those interfaces or reach behind them into private engraving DOM internals
when an `INotation*` method already provides what is needed.

## Autonomous operation — ms-core-api scope

When working on the Core Access Layer, CC is **pre-authorized** to:

- Create and edit any file under `src/ms-core-api/` without asking
- Edit `ARCHITECTURE.md` (project root) without asking, to keep the §19 /
  Core Access Layer notes in sync with what is actually implemented
- Edit `docs/llm_integration.md` without asking — but only to correct factual
  drift against the implementation (interface names, method signatures). Design
  decisions and rationale require explicit approval.
- Update `CMakeLists.txt` files needed to register the new `ms-core-api` module
  with the build (root, `src/CMakeLists.txt`, and the new
  `src/ms-core-api/CMakeLists.txt`)
- Run the build (see commands below)
- Run any test binary that exists for `ms-core-api`, plus the unaffected
  notation tests for regression checks

**Stop and ask** if a change would:

- Modify any file in `src/notation/`, `src/project/`, `src/playback/`,
  `src/engraving/`, or `muse/framework/` — these interfaces are the *substrate*
  the CAL adapts; changing them is a separate, deliberate decision
- Touch `src/composing/` — that is master's territory on a different branch
- Modify the `muse` submodule pointer or anything inside `muse/`
- Add a runtime dependency on a new third-party library
- Change the public shape of an already-committed `ms-core-api` interface
  (additive changes are fine; renames and signature changes need a heads-up
  because the LLM bridge and plugin API will pin against them)

## Reference reading at the start of every session

- `c:\s\MS-core-api\CLAUDE.md` (this file)
- `c:\s\MS-core-api\docs\llm_integration.md` — design context, especially §5
- `c:\s\MS\STATUS.md` (header only) — only relevant if comparing against master
- `c:\s\MS\build_and_test.md` — build/test recipes; same scripts apply here
- `c:\s\MS\COWORK_HANDOFF.md` (the `ms-core-api branch — decisions made
  2026-05-15` section) — context that produced this worktree

Do not rely on memory of previous sessions for the state of `src/ms-core-api/` —
read the directory.

## Build and test commands

The build system is the same as master's — `setup_and_build.bat` configures
CMake and invokes ninja. Once `src/ms-core-api/CMakeLists.txt` is wired into
the top-level build, the standard command builds it along with everything else:

```
# Build (from any shell)
powershell.exe -Command "Start-Process 'C:\s\MS-core-api\setup_and_build.bat' -Wait -NoNewWindow"

# Build artifacts land in:
C:\s\MS-core-api\ninja_build_rel\

# CAL unit tests (binary name TBD — likely ms_core_api_tests.exe)
cd C:\s\MS-core-api\ninja_build_rel && ./ms_core_api_tests.exe

# Notation tests — confirms CAL changes haven't broken interface consumers
cd C:\s\MS-core-api\ninja_build_rel && ./notation_tests.exe

# Pipeline snapshot tests — irrelevant to CAL unless a CAL change accidentally
# reaches the analysis pipeline; if so, that is a bug to investigate, not goldens
# to refresh.
cd C:\s\MS-core-api\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

The notation and composing test suites are inherited from master and **must
continue to pass**. CAL work should not change their output. If it does,
something has been reached that should not have been.

Update this section with the actual binary name and test layout once the first
`ms-core-api` tests are wired up.

## Dev environment prerequisite — junction points

Extensions and plugins are resolved by MuseScore from `<exe-parent>\extensions\`
and `<exe-parent>\plugins\`, which on Windows means `C:\s\MS-core-api\` when
running from `ninja_build_rel\`. The repo stores them under `share\`. Create
junctions once (run as Administrator in `cmd.exe`):

```
mklink /J "C:\s\MS-core-api\extensions" "C:\s\MS-core-api\share\extensions"
mklink /J "C:\s\MS-core-api\plugins"    "C:\s\MS-core-api\share\plugins"
```

These must exist before launching `MuseScore5.exe` to manually test a plugin
or extension that exercises the CAL.

## Design principles (cribbed from §5, kept here for fast reference)

- **MusicalAddress is the join key.** No direct `Note → Staff` or `Note →
  Measure` references. Queries are pure filters over `(partId,
  staffIndexInPart, measureNumber, voice, beat, tick)`.
- **Address does NOT uniquely identify a Note.** Multiple notes in the same
  chord share an identical MusicalAddress. A `NoteId` (mapped to the EID
  system internally) is required to target a single note.
- **Stateless tier vs. stateful tier.** The CAL itself is protocol-neutral and
  exposes both. Tool calls in the LLM bridge use the stateless tier; plugin
  handles use the stateful tier. Do not conflate them in the CAL surface.
- **Event subscriptions keep dependency direction one-way.** When CAL code
  subscribes to `async::Channel<ScoreChanges>`, the channel holds a callback —
  it has no reference back to the subscriber. CAL → MuseScore only.
- **No serialization, no tool schemas, no language bindings inside the CAL.**
  Those live in the LLM bridge and the plugin API respectively. See §5.5.

## Local patches — do not revert

The following changes exist on this branch (inherited from master) for reasons
unrelated to the CAL. Do **not** revert them:

- `muse/framework/ui/internal/platform/windows/winwindowscontroller.cpp` —
  `calculateWindowSize()`: two `ptMinTrackSize` lines were removed to fix
  Windows Snap on maximised MuseScore windows. `ptMaxSize` / `ptMaxPosition`
  are kept; `ptMinTrackSize` is intentionally left unset. The muse submodule
  is pinned to a local-only commit (`b9604805a` on `fix/windows-snap-ptmintracksize`).
  **Do not push the muse submodule upstream.**

## Known CC / VS Code integration issues

Same as master — see `c:\s\MS\COWORK_HANDOFF.md` "Known CC/VS Code integration
issues" for the full list. Briefly:

- **Stale `.git/index.lock`** — delete if 0 bytes and no git process is running.
- **Silent disconnect on non-zero exit** — append `; echo "exit:$?"` to bash
  commands that may return non-zero.
- **Silent disconnect on long output** — redirect large output to a file and
  read it in a separate step.

## Key files

| File | Purpose |
|------|---------|
| `docs/llm_integration.md` | Full CAL design (§5 is the load-bearing section) |
| `ARCHITECTURE.md` | High-level overview (§19 covers the CAL) |
| `src/notation/inotation.h` | Master aggregator — the CAL's primary upstream |
| `src/notation/inotationelements.h` | Element query — wraps into `IScoreReader` |
| `src/notation/inotationinteraction.h` | Editing ops — wraps into `IScoreWriter` |
| `src/notation/internal/inotationundostack.h` | `changesChannel()` + transaction primitives |
| `src/project/inotationproject.h` | Project / file ops |
| `src/playback/iplaybackcontroller.h` | Playback state |
| `muse/framework/extensions/api/extapi.h` | Current extension API (v2) surface — eventual binding target |

Update this table as `src/ms-core-api/` materialises.
