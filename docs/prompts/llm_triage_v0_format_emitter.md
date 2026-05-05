# LLM-Triage v0 — Structured-Text Format Emitter

**Scope:** Stand up a new `tools/llm_triage/` executable that loads one
MuseScore score, runs the existing harmonic analyzer, and emits **three**
plain-text artifacts per score for downstream hand-evaluation against
frontier LLMs:

1. `<score>.notes_only.txt`     — raw note onsets + durations, **no**
   analyzer output, **no** printed chord symbols. Anchoring-free input
   for the LLM's "independent opinion" pass.
2. `<score>.with_symbols.txt`   — same raw onsets, **plus** any printed
   chord symbol carried as a `printed:` annotation per region. Input for
   the prescription-classification pass.
3. `<score>.analyzer_output.txt`— our analyzer's per-region chord identity
   + key + alternatives, for Vincent's reference when he reads LLM
   responses against our output. **Never** pasted to the LLM.

**No LLM calls in v0.** No registry, no track-record code, no
multi-model orchestration — those come in v1+ once we've seen real LLM
responses on this format and learned where it trips. The whole point of
v0 is to surface format problems empirically before locking in API
plumbing.

**Reference docs (read first, in this order):**

- **`BUILD_AND_TEST.md`** (repo root) — **authoritative** build/test
  reference. Read before doing anything that touches the build. In
  particular: the "Running from Git Bash / MSYS2" section at the top
  documents the `cmd.exe //c "…"` trap (MSYS2 translates `//` as a
  UNC path; the bat file silently does not run). Use the documented
  bash patterns, not the cmd-style ones from `CLAUDE.md`.
- `docs/llm_triage_design.md` — the full design discussion.
  Particularly: "Input format: structured plain text, deliberately
  boring", "Do not over-reduce before the LLM sees it", and "Chord
  symbol handling: two passes, different purposes".
- `docs/symbol_input_audit.md` — chord-symbol-ban audit. v0 reads
  printed symbols only as comparison metadata for the
  `with_symbols.txt` artifact, **never** as input to the analyzer.
  Confirm before you ship that the analyzer call path you build does
  not accept any `Harmony` data as input.
- `tools/batch_analyze.cpp` (specifically `loadScore` at line 290,
  `analyzeScore` at line 1603, and `main` at line 2289) — the
  loading + analysis pattern v0 mirrors.
- `src/composing/analyzed_section.h` — the `AnalyzedSection` /
  `AnalyzedRegion` / `KeyArea` shape your emitter consumes.
- `tools/CMakeLists.txt` — CMake wiring pattern for `batch_analyze`.
  `tools/llm_triage/CMakeLists.txt` mirrors this.
- **Style reference** (skim — don't copy verbatim):
  `docs/prompts/phase_3a_implode_conversion.md`. Shows the
  pre-flight / work-order / verification-gate / report-back pattern
  prior phases used. This prompt follows the same pattern; you can
  see precedent in how prior phases got run.

---

## CLAUDE.md override (read this carefully)

`CLAUDE.md` at the repo root will auto-load when you start. **It is
stale on multiple critical points and this prompt overrides it** for
this session:

| `CLAUDE.md` says | Reality for THIS session |
|---|---|
| You are pre-authorized to edit any file under `src/composing/` | **No** — `src/composing/` is mainline-owned per the parallel-work pact below. Do not edit a single file there. |
| You may edit `src/notation/internal/notationaccessibility.cpp` without asking | **No** — `src/notation/internal/**` is mainline-owned. Do not edit. |
| You may edit `ARCHITECTURE.md` without asking | **No** — mainline updates `ARCHITECTURE.md` as it lands phases. Do not touch. |
| Build via `cmd.exe //c "C:\s\MS\setup_and_build.bat"` | **Wrong** — `cmd.exe //c` silently fails from Git Bash (MSYS2 trap). And the bat file targets `C:\s\MS\ninja_build_rel\`, not your worktree's build dir. See `BUILD_AND_TEST.md` for the bash-correct invocation; configure your worktree build manually (see Pre-flight step 6 below). |
| Tests run from `ninja_build/` | **Wrong** — repo build dir is `ninja_build_rel/`. Your worktree build dir is `ninja_build_llm_triage/`. v0 doesn't run any existing test suites (you don't touch `src/composing/`), so this is moot for v0 — noted to flag the `CLAUDE.md` staleness. |
| "Standard loop for mismatch reduction work" | **Not applicable** — v0 is not mismatch-reduction work. Ignore that loop entirely. |

If `CLAUDE.md`'s guidance disagrees with this prompt **on any point**,
this prompt wins. If `BUILD_AND_TEST.md` disagrees with `CLAUDE.md`
on build/test commands, `BUILD_AND_TEST.md` wins (it's authoritative).

The `CLAUDE.md` "Conventions" block (American English, no
confirmation prompts between steps, commit only when explicitly
asked) is **fine and applies here too** — those points are not
contradicted.

---

## Parallel-work pact (read before touching anything)

You are running in a **separate git worktree** for the `llm-triage`
branch. A different Cowork session is doing a multi-phase refactor on
`master` in the main checkout. **Do not touch any file on this list,
in either checkout, for any reason** — the other session owns them and
will rebase your work onto its changes when phases land:

- `src/composing/**` — analyzer logic, mainline owns it
- `src/notation/internal/**` — bridge layer, mainline owns it
- `src/notation/tests/pipeline_snapshot_tests/**` — snapshot harness
- `ARCHITECTURE.md` (root) — mainline updates as it lands phases
- `docs/policy2_coalescing_map.md`
- `docs/unified_analysis_pipeline.md`
- `STATUS.md`, `REFACTOR_DEDUPLICATION_PLAN.md` — mainline status docs

**You may freely create or modify:**
- `tools/llm_triage/**` (new directory, your turf)
- `docs/llm_triage_*.md` (new docs)
- `docs/prompts/llm_triage_*.md` (new prompts; **this file** included
  — see Step 1 below)
- `tools/CMakeLists.txt` — single line `add_subdirectory(llm_triage)`.
  This is the only mainline-touched file you may edit, and only that
  one line.

If a step here would require editing anything not on the "may freely"
list, **halt and surface** — do not work around it.

---

## Pre-flight

1. **Confirm mainline checkout is clean of v0 work** (from Git Bash):
   ```bash
   cd /c/s/MS
   git status -sb
   git rev-parse HEAD
   ```
   Expect HEAD `d35f003a` or later (Phase 3c recon already landed).
   The working tree may have uncommitted edits to mainline-owned files
   (Phase 3c-impl in flight in the other session) — **leave those
   alone**. They are not your concern; they will not affect the
   worktree because worktrees share git history but have independent
   working trees.

2. **Confirm the worktree exists and is the expected one.** Vincent
   creates the worktree manually before invoking you (so Window 2 can
   open on it). Verify rather than re-create:
   ```bash
   git worktree list
   ```
   You should see two entries:
   - `/c/s/MS` (or `C:/s/MS`) on branch `master`
   - `/c/s/MS-llm-triage` on branch `llm-triage`

   If the `llm-triage` worktree at `/c/s/MS-llm-triage` is **not**
   listed, **halt and surface** — Vincent needs to create it before
   you proceed with:
   ```bash
   cd /c/s/MS
   git worktree add -b llm-triage /c/s/MS-llm-triage master
   ```

   If a worktree exists but at a different path, or on a different
   branch, **halt and surface** — do not delete, do not `--force`,
   do not move it. Earlier llm-triage work may live there.

3. **Switch all subsequent work to the worktree.** Every command
   below runs in `/c/s/MS-llm-triage` unless explicitly stated. When
   in doubt, run `pwd` and confirm you are in the worktree.

4. **Verify you are not about to disturb mainline state:**
   ```bash
   cd /c/s/MS-llm-triage
   git status -sb
   git rev-parse --show-toplevel  # must print /c/s/MS-llm-triage
   ```
   Expect: `## llm-triage` and a **clean** working tree (no `M`
   files, no `??` files outside what this prompt creates).

5. **Detect prior-session truncation.** Run `git diff --stat`
   against the parent. If you see any unexpected `M` files or
   trailing `\0` / mid-token truncation in tracked files, **halt and
   surface** — a prior CC session was cut by usage limit. Do not
   paper over.

6. **Build dir setup.** Use `C:\s\MS-llm-triage\ninja_build_llm_triage`
   as the build directory for this worktree. Do **not** reuse
   `ninja_build_rel/` from the mainline checkout — the two sessions
   would invalidate each other's incremental builds.

   Read `setup_and_build.bat` first — it is **not** a CMake-configure
   script. It just `cd`s into `c:\s\MS\ninja_build_rel` and runs
   `ninja <targets>` against an already-configured build. So you
   cannot reuse it for the worktree, but you also cannot just "copy
   what it does" — you must run cmake configure yourself for the new
   build dir.

   Read `BUILD_AND_TEST.md` for the bash-correct command shapes.
   Initial configure (run **once** from Git Bash, in the worktree):
   ```bash
   cd /c/s/MS-llm-triage
   /c/Program\ Files/CMake/bin/cmake.exe -G Ninja \
     -B /c/s/MS-llm-triage/ninja_build_llm_triage \
     -S /c/s/MS-llm-triage \
     -DCMAKE_BUILD_TYPE=RelWithDebInfo \
     -DMUE_BUILD_ENGRAVING_DEVTOOLS=ON
   ```
   (Substitute the cmake path — `which cmake` from Git Bash will
   show what's available. The exact `MUE_*` flag set may need more
   options to match what `ninja_build_rel/CMakeCache.txt` contains.
   Read that file in the mainline checkout if the configure fails;
   replicate the `MUE_*` settings it shows. Do **not** edit
   `setup_and_build.bat` or `setup_and_build_fast.bat`.)

   Subsequent builds (Step 2 onwards), use ninja directly per
   `BUILD_AND_TEST.md`:
   ```bash
   /c/Qt/Tools/Ninja/ninja.exe -C /c/s/MS-llm-triage/ninja_build_llm_triage llm_triage
   ```
   (Substitute the ninja path if `which ninja` shows a different
   one. **Never** use `cmd.exe //c "..."` from Git Bash — the `//`
   gets mangled by MSYS2 and cmd.exe opens interactively.)

---

## Work order

The order matters. Verification gates between steps are the safety
net. Do not reorder.

### Step 1 — Bring this prompt into the worktree and commit it

This prompt file lives at `docs/prompts/llm_triage_v0_format_emitter.md`
in the **mainline checkout** (`C:\s\MS`), as an **untracked file** —
it has not been committed on `master` (that would race the other
session). Worktrees share git history but have independent working
trees, so the untracked file in `C:\s\MS\docs\prompts/` is **not
visible** in `C:\s\MS-llm-triage\docs\prompts/`. Copy it across, then
commit it onto your branch:

```bash
cd /c/s/MS-llm-triage
cp "/c/s/MS/docs/prompts/llm_triage_v0_format_emitter.md" \
   "docs/prompts/llm_triage_v0_format_emitter.md"
ls -la docs/prompts/llm_triage_v0_format_emitter.md
git add docs/prompts/llm_triage_v0_format_emitter.md
git commit -m "LLM-Triage v0: prompt file for format-emitter session"
```

If the source file at `C:\s\MS\docs\prompts\llm_triage_v0_format_emitter.md`
does not exist, **halt and surface** — Vincent (or the planning
session) needs to put it there before you proceed.

### Step 2 — Create directory + CMake skeleton

Create `tools/llm_triage/` with:

- `CMakeLists.txt` — mirrors `tools/batch_analyze.cpp`'s wiring in
  `tools/CMakeLists.txt`:
  - `add_executable(llm_triage llm_triage.cpp)`
  - Same `RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}` set on
    `llm_triage` target
  - Same `target_include_directories` (the four entries: `src/`,
    `src/framework/`, `src/framework/global/`, plus
    `${CMAKE_BINARY_DIR}/tools/llm_triage`)
  - Same `target_link_libraries`: `muse_global`, `muse_draw`,
    `engraving`, `notation`, `composing_analysis`, `iex_musicxml`
  - **No** `add_test` for v0. Skip the regression-test wiring;
    we'll add it once the format stabilizes.
- `llm_triage.cpp` — empty stub for now (`int main() { return 0; }`).
- `README.md` — one-paragraph description of what the tool does and
  pointing at `docs/llm_triage_design.md`.

Then add **one line** to `tools/CMakeLists.txt`:
```cmake
# ── llm_triage ────────────────────────────────────────────────────────────
# Format-emitter for LLM-assisted triage. See docs/llm_triage_design.md.
add_subdirectory(llm_triage)
```
Place this block at the bottom of `tools/CMakeLists.txt`, after the
`batch_analyze` block. Touch nothing else in that file.

**Verify** (from Git Bash, in the worktree):
```bash
# If you have not yet configured ninja_build_llm_triage from
# Pre-flight step 6, do that first.
/c/Qt/Tools/Ninja/ninja.exe -C /c/s/MS-llm-triage/ninja_build_llm_triage llm_triage
```
Must succeed and produce
`/c/s/MS-llm-triage/ninja_build_llm_triage/llm_triage.exe`.

### Step 3 — Implement loader + CLI

In `llm_triage.cpp`, model on `tools/batch_analyze.cpp`:

- CLI: `llm_triage <input_score_path> <output_dir>`
  - `<input_score_path>`: path to one `.mscz` / `.musicxml` /
    `.mxl` file
  - `<output_dir>`: directory where the three `.txt` files land
    (basename of input score determines filename prefix)
- Use `loadScore()` pattern from `tools/batch_analyze.cpp:290` —
  copy/adapt the function (do not depend on it via header; v0 stays
  self-contained).
- Replicate the staff-eligibility filter from
  `tools/batch_analyze.cpp:338` (`isChordTrackStaff`) and
  `tools/batch_analyze.cpp:350` (`staffIsEligible`), and build the
  `excludeStaves` set the same way `batch_analyze`'s `main` does at
  line 2410.
- **Analyzer entry point: `analyzeScore` (line 1603 of
  `tools/batch_analyze.cpp`).** This is the **note-only Jaccard
  path**. Copy/adapt the function — it is `static` in
  `batch_analyze.cpp`, so you cannot link to it; v0 needs its own
  copy or, better, a small refactor that pulls it into a shared
  header. **For v0, copy it.** Pulling-into-shared is a v1 concern
  and would touch `tools/batch_analyze.cpp` (mainline-adjacent).
- **Do NOT call `analyzeScoreJazz` (line 1680).** That is the
  symbol-driven boundary path that
  `docs/symbol_input_audit.md` §C.1 flagged as pending Vincent's
  retire/relocate/accept decision. v0 must be note-only.
- The analyzer returns `std::vector<AnalyzedRegion>`, not the full
  `AnalyzedSection`. That's expected — `batch_analyze` itself
  hasn't been converted to consume `AnalyzedSection` yet. v0
  consumes the same flat-vector shape `batch_analyze` does today.
  This means `AnalyzedRegion::keyAreaId` will be `-1` (per the
  comment in `src/composing/analyzed_section.h:110`) and there are
  no `KeyArea` spans to render. Step 4's `analyzer_output.txt`
  format must handle this — see "key_area handling" note in Step 4.
- Print `loaded: <path>`, `staves: <eligible>/<total>`, and
  `regions: <N>` to stdout for visibility, then proceed to Step 4
  emitters.

**Verify** (from Git Bash, in the worktree):
```bash
cd /c/s/MS-llm-triage
/c/Qt/Tools/Ninja/ninja.exe -C ./ninja_build_llm_triage llm_triage
./ninja_build_llm_triage/llm_triage.exe \
  "tools/extra scores/hiromi/pachelbel-canon-in-d-arr-hiromi-uehara.mscz" \
  ./outputs
```
Default v0 score is `pachelbel-canon-in-d-arr-hiromi-uehara.mscz` —
short, well-known, manageable for the first format-eval pass. Note
the path has a space; quote it.

Expected stdout: `loaded: …pachelbel-canon…mscz`, a `staves: N/M`
line, and a non-zero `regions: N`. No emitter output yet (Step 4
adds that).

### Step 4 — Emit the three artifacts

This is the meat of v0. Implement three emitters, all in
`llm_triage.cpp` (split into separate `.cpp` files only if it
genuinely helps readability — do not pre-architect).

**Format conventions (decide once, document the decision in
source-comment headers in `llm_triage.cpp` so v1 can see why):**

- **Pitch spelling:** use TPC-derived names with octave (e.g. `F#4`,
  `Bb2`). Do not write enharmonic equivalents differently from how
  the score spells them. Get spelling from `Note::tpc()` /
  `tpc2name`.
- **Time format:** `mN bX.Y` where N is 1-indexed measure number and
  X.Y is beat within measure as a decimal. Get measures from
  `Score::firstMeasure()` / `Measure::no()`.
- **Duration:** standard symbols `w h q e s 32 64`. Tuplets:
  `q3` (eighth-triplet quarter ratio) or write the actual fractional
  value `1/8t` — **pick one and document it**. Same for dotted
  values: `q.` for dotted-quarter is conventional.
- **Voice/staff:** label by part name, not "RH"/"LH" (Hiromi scores
  may have more than 2 staves). Format: `staff "<part_name>":`.
  Sort onsets within a tick by staff index for stable output.
- **Sustained-note handling:** emit each note **once** at its onset
  with its duration. Do **not** repeat sustained notes on subsequent
  beats — the design doc explicitly says don't pre-window. The LLM
  reads the duration and does its own windowing.
- **Header block** (top of each file):
  ```
  # Score:        <basename>
  # Source path:  <absolute path>
  # Generated:    <ISO-8601 timestamp>
  # Format:       llm_triage v0 (notes_only | with_symbols | analyzer_output)
  # Key sig:      <e.g. "D major"> (notation; not an analytical claim)
  # Time sig:     <e.g. "4/4"> (initial; changes annotated inline)
  ```
  The "(notation; not an analytical claim)" parenthetical for key
  sig is **load-bearing** — it tells the LLM the key signature came
  from the score's notation, not our analyzer, so the LLM is free to
  disagree.

**File 1 — `<basename>.notes_only.txt`:**

After the header, one line per onset event in tick order:
```
m1 b1.0 (q):  staff "Piano RH": F#4 A4 D5 ; staff "Piano LH": D2
m1 b2.0 (q):  staff "Piano RH": E4 A4 C#5 ; staff "Piano LH": A2
m1 b3.0 (q):  staff "Piano RH": D4 F#4 A4 ; staff "Piano LH": D2
...
```
- Multiple onsets at the same tick on the same staff → space-separated
  pitches (a chord on that staff at that tick).
- Multiple staves at the same tick → separated by ` ; staff "<name>":`
- A tick with onsets on only one staff → only that staff appears.
- Time-signature changes → emit a marker line `# Time sig: 3/4` at
  the tick where the meter changes, before the onset on that tick.
- Tempo markings (if present) → emit `# Tempo: <bpm> bpm (<beat>)`
  at the tick they apply.
- **No printed chord symbols.**
- **No analyzer output.**

**File 2 — `<basename>.with_symbols.txt`:**

Identical to File 1, but for any tick where a printed `Harmony`
element exists in the score, append ` printed: "<symbol_text>"` to
the line. Read the `Harmony` element's display text via the
notation-side accessor (use the same accessor `batch_analyze` uses
when it stores `writtenRootPc` / `writtenQuality` — see §B of
`docs/symbol_input_audit.md`).

**Important:** the `Harmony` element is read **only** for emitting the
`printed:` annotation in this file. It is **not** passed to the
analyzer — your analyzer call in Step 3 does not see chord-symbol
input. If implementing this requires you to call any analyzer entry
point that reads symbols, **halt and surface**.

**File 3 — `<basename>.analyzer_output.txt`:**

Header block (with `Format: … analyzer_output`), then one block per
`AnalyzedRegion`:
```
region 1: ticks [0, 1920)  mm 1.b1.0 → 2.b1.0
  chord:        D major (D F# A)
  alternatives: [D7 (D F# A C), Dsus4 (D G A)]
  key:          D major (mode: Ionian)
  confidence:   0.87 (assertive)
  key_area:     #0  ticks [0, 7680)  D major

region 2: …
```
Use `AnalyzedRegion::chordResult` for `chord:`,
`AnalyzedRegion::alternatives` for the alternatives list (may be
empty pre-Phase-3c-impl), `AnalyzedRegion::keyModeResult` for `key:`,
`AnalyzedRegion::hasAssertiveExposure` for the `(assertive)` suffix.

If `alternatives` is empty, render `alternatives: (none)` rather than
omitting the field — keeps the format stable across the Phase 3c
landing.

**`key_area:` handling.** Because v0 consumes
`std::vector<AnalyzedRegion>` (not the full `AnalyzedSection`),
`AnalyzedRegion::keyAreaId` is `-1` and no `KeyArea` spans are
available. Render the `key_area:` line as:
```
  key_area:     (n/a in v0 — analyzer entry point returns flat region vector; full AnalyzedSection consumption deferred to v1)
```
Keep the field present so the format is stable when v1 wires the
full `AnalyzedSection` API. Don't omit it.

For chord rendering, use the production `ChordSymbolFormatter` (it
lives in `composing_analysis`; see `docs/llm_triage_design.md`'s
"Output format mirrors input" section — reusing the production
formatter is explicitly called out as the correct choice). Do **not**
write your own chord-text dialect.

**Verify** (from Git Bash, in the worktree):
```bash
cd /c/s/MS-llm-triage
mkdir -p outputs
/c/Qt/Tools/Ninja/ninja.exe -C ./ninja_build_llm_triage llm_triage
./ninja_build_llm_triage/llm_triage.exe \
  "tools/extra scores/hiromi/pachelbel-canon-in-d-arr-hiromi-uehara.mscz" \
  ./outputs
```
Expected: three files in `./outputs/`:
- `pachelbel-canon-in-d-arr-hiromi-uehara.notes_only.txt`
- `pachelbel-canon-in-d-arr-hiromi-uehara.with_symbols.txt`
- `pachelbel-canon-in-d-arr-hiromi-uehara.analyzer_output.txt`

Open each. **Sanity-check by hand:**
- `notes_only.txt` first 8 measures should be readable as the
  Pachelbel pattern — D, A, Bm, F#m, G, D, G, A in the bass line.
- `with_symbols.txt` is identical to `notes_only.txt` except for the
  added `printed:` annotations (if the score has them).
- `analyzer_output.txt` region count matches what stdout reported in
  Step 3, and the first region's `chord:` is plausible.

If any file is missing, malformed, or the contents fail the
sanity-check, **halt and surface** with the actual output included
verbatim — do not paper over.

### Step 5 — Commit, push, report

```bash
cd /c/s/MS-llm-triage
git add tools/llm_triage/ tools/CMakeLists.txt
git status   # confirm: only files in tools/llm_triage/ and the
             # one-line edit to tools/CMakeLists.txt are staged
git commit -m "LLM-Triage v0: format emitter for hand-eval against frontier LLMs

- New executable tools/llm_triage produces three plain-text artifacts
  per score: notes-only (anchoring-free LLM input), with-symbols
  (prescription-classification input), and analyzer_output (Vincent's
  reference, never pasted to LLMs).
- No LLM API calls, no registry, no track records — those land in v1+
  once we've seen real LLM responses on this format.
- Mirrors loader pattern from tools/batch_analyze.cpp.
- Format conventions documented in source comments at top of
  llm_triage.cpp."
git push -u origin llm-triage
```

If `git push` fails (authentication, no remote permissions, etc.),
**halt and surface** — do not retry with credentials manipulation.

---

## Halt-and-surface protocol

Surface to Vincent immediately, without working around it, if any of
these happen:

- Pre-flight: working tree of the worktree is not clean after `git
  worktree add`.
- Step 2: `tools/CMakeLists.txt` already contains an
  `add_subdirectory(llm_triage)` (someone got there first; do not
  duplicate).
- Step 3: the analyzer entry point `batch_analyze` uses today is
  unavailable on this branch (e.g. it was renamed/moved as part of
  Phase 3c-impl). **Do not invent a new path** — surface so Vincent
  can decide whether to wait for Phase 3c-impl or branch from an
  earlier commit.
- Step 4: any analyzer call you find requires `Harmony` element data
  as input. Per `docs/symbol_input_audit.md` §A, no such call should
  exist in production code. If you find one, surface — it's either a
  regression in mainline or a tool-side path that v0 must avoid.
- Step 4: the production `ChordSymbolFormatter` is unreachable from
  the `composing_analysis` link target. Surface; do not work around
  by writing a custom formatter.
- Step 4 sanity-check: any of the three files looks visibly wrong
  (missing pitches, wrong octaves, region count mismatch). Surface
  with the actual output, not a description.
- Build fails for any reason that is not "missing line in CMake."
  Surface with the full build error.

When you halt-and-surface, include:
1. The exact step you were on.
2. The exact command that produced the unexpected result.
3. The actual output (verbatim, not summarized).
4. What you would do next if instructed to proceed; what you would
   do if instructed to back out.

---

## Report-back format

When all steps complete, report in this format (Vincent scans this
quickly):

```
## LLM-Triage v0 — session report

Branch: llm-triage @ <commit_sha>
Worktree: C:\s\MS-llm-triage
Build dir: C:\s\MS-llm-triage\ninja_build_llm_triage
Pushed to: origin/llm-triage  (yes/no)

### Files added
- tools/llm_triage/CMakeLists.txt
- tools/llm_triage/llm_triage.cpp  (<N> lines)
- tools/llm_triage/README.md
- tools/CMakeLists.txt  (one-line add_subdirectory edit)

### v0 verification on default Hiromi score
- Score: pachelbel-canon-in-d-arr-hiromi-uehara.mscz
- Regions analyzed: <N>
- Files emitted: 3 (sizes: notes_only=<X>kb, with_symbols=<Y>kb, analyzer_output=<Z>kb)
- Sanity-check verdict: <pass|partial|fail>  — <one sentence>

### Format decisions documented in source
- Pitch spelling: <choice + brief rationale>
- Tuplet notation: <choice + brief rationale>
- Sustained-note handling: <choice + brief rationale>
- Time-sig / tempo change handling: <choice + brief rationale>
- Anything else you decided that v1 should know about: <list>

### Surprises / open questions for Vincent
- <list, one per line, brief>

### Mainline-pact compliance check
- Files touched outside tools/llm_triage/ + docs/prompts/llm_triage_*: <list>
  (Should be exactly: tools/CMakeLists.txt, one-line edit. Anything
  else is a pact violation — call it out explicitly.)
```

---

## What v0 deliberately does NOT do

For the avoidance of scope creep — these are v1+ work, not v0:

- LLM API calls (any provider).
- A registry schema or any persistent opinion storage.
- Per-LLM track-record bookkeeping.
- Multi-score batching beyond "the CLI takes one path."
- A Python harness, notebook, or web UI.
- The prescription-classification *prompt* (the
  `with_symbols.txt` file is the **input** to that prompt; the
  prompt itself is a v1 design question, after Vincent has seen what
  the format looks like in front of an LLM).
- Format regression tests (`test_llm_triage_regressions.py`
  equivalent of `test_batch_analyze_regressions.py`). Add when
  format stabilizes after v0 LLM round-trips.
- Anything in `src/composing/`, `src/notation/internal/`, or the
  pact-protected list above.

If during implementation you find yourself wanting to add one of
these "because it would make v0 better," **don't.** Note it in your
report-back as an open question for v1 instead.
