# CC Report — clang / llvm-cov TRUE BRANCH coverage (feasibility spike → delivered)

**Date:** 2026-06-26 · **Outcome:** ✅ **FEASIBLE and DELIVERED** (cheap path — no Qt-under-clang rebuild,
no production `src/` edits, production MSVC build + BIR gate + snapshots all untouched).
**Toolchain:** LLVM 22.1.8 (portable, no admin) · MSVC 14.42.34433 · Qt 6.10.1 msvc2022_64.
**Build-config commit (verify by sha):** `fb5b9834dc8d903d62223f6adfc626cad4c9ac7d` — `tools/coverage/run_branch_coverage.ps1` (only; no source).
**§0 sweep-protection commit:** `7e4becf6b998dfe5434cec4e3649df44da985c2f` — `COWORK_HANDOFF.md` only (NEVER-BASH rule).

---

## Headline

**Real per-branch coverage of the composing L1–L4 module (`src/composing/analysis`), measured by
`llvm-cov --show-branches=count` over a clang-instrumented build, exercised by the existing
`composing_tests` suite (695 tests / 56 suites, all PASS under instrumentation):**

| Metric    | Covered | Total | Coverage |
|-----------|--------:|------:|---------:|
| Regions   | 4811 | 6201 | 77.58% |
| Functions |  266 |  319 | 83.39% |
| Lines     | 6765 | 9264 | 73.02% |
| **Branches** | **3896** | **5586** | **69.75%** |

**1690 of 5586 branch directions are never exercised by `composing_tests`.** This is the criterion-4
number OpenCppCoverage structurally cannot produce (it is line-only: `branches-valid="0"`,
`tools/coverage/run_coverage.ps1` header).

---

## §1 Feasibility findings

### §1.1 Toolchain availability
- `clang-cl` / `clang` / `llvm-cov` / `llvm-profdata` / `llvm-lib` / `lld-link`: **were not installed**
  (not on PATH; not in standard/standalone locations). VS Build Tools 2022 bundles **only**
  `clang-format.exe` + `clang-tidy.exe` under `…\VC\Tools\Llvm\` — not the compiler or coverage tools.
- **Installed without admin** (same portable pattern as OpenCppCoverage): downloaded
  `LLVM-22.1.8-win64.exe` (NSIS, 434 MB) and extracted with 7-Zip
  (`C:\Program Files\7-Zip\7z.exe`) into `C:\Users\vince\tools\LLVM\`. The NSIS payload contains the
  full toolchain incl. the profile runtime `lib\clang\22\lib\windows\clang_rt.profile-x86_64.lib`.
  All tools self-consistent at **22.1.8**, target `x86_64-pc-windows-msvc` (matches Qt `msvc2022_64`).
  Using one LLVM version for compile + profdata + cov is required (profile format must match).

### §1.2 Minimal instrumentable target (and what was actually built)
`composing_analysis` is built `NO_QT` but `target_link_libraries(... PUBLIC engraving)` and
`harmonicsegmenter.cpp` uses engraving `Score/Segment/Chord/Note`, so it compiles against the
engraving/Qt header set. A **runnable** `composing_tests` links `composing_analysis + intonation +
engraving` (→ the full engraving→muse→Qt graph). The production build is **unity** — `composing_analysis`
is 3 unity TUs (`unity_0/1/2_cxx.cxx`) archived into `composing_analysis.lib`.

**The cheap path that avoids a full Qt-under-clang rebuild (Cowork-directed Option B):**
1. Read the existing MSVC ninja build's **compile DB** and **link command** (`ninja -t compdb` /
   `-t commands` — read-only graph queries).
2. Recompile **only the 3 `composing_analysis` unity TUs** with `clang-cl`, reusing the production cl
   flags verbatim + `-fprofile-instr-generate -fcoverage-mapping`. Result: clean — **0 errors**, only
   benign warnings (`unused-parameter`, `sign-compare`); no `/WX` in the tree so nothing blocks.
   (MSVC PCH `/Yu`+`/Fp` dropped — clang-cl cannot read an MSVC `.pch` — but the `/FI cmake_pch.hxx`
   force-include is kept, so the code still sees the PCH header contents.)
3. Archive the 3 instrumented objects → `composing_analysis_instr.lib` (`llvm-lib`).
4. Relink `composing_tests` by reusing the production link command verbatim with 3 surgical swaps:
   `composing_analysis.lib` → the instrumented lib; `/out` `/implib` `/pdb` → the coverage out dir
   (**production binary untouched**); + the `clang_rt.profile` runtime. **Linker swapped MSVC
   `link.exe` → `lld-link`** (see finding below).
5. Run the existing `composing_tests` under instrumentation (Qt resolves via the install on PATH; the
   test data root is an absolute compile-time path) → `.profraw`.
6. `llvm-profdata merge` → `llvm-cov report` / `export` / `show --show-branches=count`.

**Why mixing works:** `clang-cl` emits MSVC-ABI COFF objects with MSVC name mangling, so the
instrumented `composing_analysis` links seamlessly with the MSVC-compiled test objects + the existing
`engraving`/`muse`/Qt/gtest `.lib`s. Only `composing_analysis` carries coverage mapping → the report is
naturally scoped to L1–L4.

### §1.3 Hard gate — production `src/` edits required? **NO.**
- **Zero** production source edits. The only new artifact is build-config: `tools/coverage/run_branch_coverage.ps1`.
- The two MSVC-isms encountered were handled **in the build-config translation, not in source**: the
  MSVC PCH (neutralized to a force-include) and Qt `-external:I` (rewritten to `/I`). No `src/` file,
  no `setup_and_build.bat`, no preset, and no gate was touched.

### Key finding — MSVC `link.exe` corrupts the LLVM profile **names** section; `lld-link` fixes it
First relink used the production MSVC `link.exe`. It linked fine and the binary ran all 695 tests, but
`llvm-profdata merge` failed: **`malformed instrumentation profile data: symbol name is empty`**. Cause:
clang locates its counter/data/**names** sections at runtime via linker-defined `$A`/`$Z` boundary
symbols on grouped (`$`-suffixed) sections; **MSVC `link.exe` does not lay these out the way the profile
format requires.** Re-linking with **`lld-link`** (LLVM's drop-in MSVC-compatible linker — same args,
same MSVC objects/libs) produced a binary whose profile merges cleanly. This is the one non-obvious
requirement of the cheap path and is baked into the runner.

---

## Per-file branch coverage (criterion-4 map)

`composing_tests`-only. Sorted within group; **Br** = branch directions, **Miss** = uncovered directions.

| File (src/composing/analysis/) | Br | Miss | Branch% |
|---|---:|---:|---:|
| chord/analysisutils.h | 46 | 3 | 93.48% |
| chord/chordanalyzer.cpp | 734 | 32 | 95.64% |
| chord/chordanalyzer.h | 52 | 20 | 61.54% |
| chord/chorddiagnose.cpp | 48 | 9 | 81.25% |
| chord/chordpostpasses.cpp | 182 | 50 | 72.53% |
| chord/chordslicedecoder.cpp | 214 | 40 | 81.31% |
| chord/chordsymbolformatter.cpp | 752 | 123 | 83.64% |
| chord/chordvoicing.cpp | 116 | 11 | 90.52% |
| chord/postscoringgates.cpp | 340 | 58 | 82.94% |
| engravingbridge/regiontonecollector.cpp | 154 | 60 | 61.04% |
| engravingbridge/regiontonecollector.h | 16 | 12 | 25.00% |
| engravingbridge/regiontoneprimitives.cpp | 244 | 75 | 69.26% |
| engravingbridge/spellingview.cpp | 14 | 0 | 100.00% |
| function/harmonicfunctionlayer.cpp | 216 | 6 | 97.22% |
| function/tonicizationlabeler.cpp | 54 | 12 | 77.78% |
| harmony/harmonicsegmenter.cpp | 381 | 171 | 55.12% |
| key/keymodeanalyzer.cpp | 290 | 36 | 87.59% |
| key/keymodeanalyzer.h | 20 | 0 | 100.00% |
| key/keymodeformatting.cpp | 88 | 88 | **0.00%** |
| key/keymodesequence.cpp | 140 | 21 | 85.00% |
| key/keyresolver.cpp | 131 | 32 | 75.57% |
| notemodel/note_model.cpp | 78 | 4 | 94.87% |
| region/regionanalyzer.cpp | 452 | 282 | 37.61% |
| region/sparsechordrefinement.cpp | 82 | 77 | **6.10%** |
| scoreharvest/metricweights.cpp | 76 | 40 | 47.37% |
| section/cadencekeyanchor.cpp | 54 | 9 | 83.33% |
| section/jointkeydecision.cpp | 168 | 52 | 69.05% |
| section/localmodulationdetector.cpp | 80 | 20 | 75.00% |
| section/sectionanalyzer.cpp | 260 | 260 | **0.00%** |
| section/sectioncadencedetection.cpp | 86 | 86 | **0.00%** |
| slicing/slicer.cpp | 18 | 1 | 94.44% |
| **TOTAL** | **5586** | **1690** | **69.75%** |

(Header-only TUs with no branch regions are omitted: `chordslicedecoder.h`, `decode/chordpathdecoder.h`,
`notemodel/note_model.h`, `region/harmonicrhythm.h`, `key/modepriorpresets.cpp`.)

### ⚠ Scope caveat — read the 0% files correctly (NOT asserted to be untested overall)
The fully-uncovered files are **uncovered by `composing_tests`**, which is the only suite this measurement
runs. They are **plausibly** exercised by `notation_tests` (the notation pipeline / bridge), which is out
of scope here — e.g. `section/sectionanalyzer.cpp` `analyzeSection()` and `section/sectioncadencedetection.cpp`
are driven by the notation bridge, and `key/keymodeformatting.cpp` (display formatters
`keyModeTonicName`/`keyModeSuffix`) by UI/tools. **This is a hypothesis to verify, not a claim.** The clean
extension (same cheap path, instrument `composing_analysis`, relink the `notation_tests` binary with
`lld-link`) would measure the union and is the natural next step if Cowork wants whole-corpus branch coverage.
The biggest gaps inside `composing_tests`' own reach are `region/regionanalyzer.cpp` (37.6%, 282 dirs),
`harmony/harmonicsegmenter.cpp` (55.1%, 171), `region/sparsechordrefinement.cpp` (6.1%, 77).

Per-line uncovered-branch locations are in the JSON export + browsable HTML (artifacts below).

---

## §3 Gate & scope confirmation
- **Production MSVC build, BIR 53/24/53, snapshot goldens: UNTOUCHED.** The runner only issues read-only
  `ninja -t compdb`/`-t commands` against `ninja_build_rel`, and writes all artifacts to
  `scratch_artifacts/coverage/clang_branch`. `git status` shows **no** tracked/`src/`/production-build
  changes — only the new runner + untracked `scratch_artifacts/`. The production `composing_tests.exe`
  binary was not modified.
- **No production source changes** (§1.3). **No test changes** — the existing `composing_tests` is used
  verbatim. **`upstream` untouched**; commits are local only.

---

## Reproduce
```
pwsh -File tools\coverage\run_branch_coverage.ps1
# (defaults: LLVM at C:\Users\vince\tools\LLVM, build at C:\s\MS\ninja_build_rel,
#  output to C:\s\MS\scratch_artifacts\coverage\clang_branch)
```
Prereqs (all no-admin): portable LLVM in `C:\Users\vince\tools\LLVM\bin`; the production MSVC build
already built in `ninja_build_rel` (so the test objects + link libs exist). The script self-contains the
cl→clang-cl translation, the `lld-link` relink, and the `llvm-cov` invocations.

## Artifacts (gitignored; `scratch_artifacts/coverage/clang_branch/`)
- `branch_report.txt` — the per-file table above (`llvm-cov report -show-branch-summary`).
- `branch_export.json` — machine-readable per-branch data (true/false counts per region).
- `html/index.html` — browsable, branch-annotated (`--show-branches=count`).
- `composing.profdata` / `composing.profraw`, `compile.log`, `link.log`, `testrun.log`.
- (also `scratch_artifacts/coverage/composing_branches/` — an earlier manual HTML run, identical numbers.)
