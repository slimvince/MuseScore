# CC — Working-tree integrity repair + authoritative test-coverage audit

> **Scope: repair + measurement + audit ONLY.** No production logic changed, no new tests written, no
> inference-fixing. The only writes were: removal of one confirmed-stale `.git/index.lock`, and the capture
> of this report + raw artifacts under `scratch_artifacts/` (untracked). HEAD unchanged at `7de96a63f2`.
> Date: 2026-06-26.

---

## Part A — Working-tree integrity

### A1 — Authoritative status (YOUR Windows git)

`git status --porcelain=v1` reports **exactly one modified file**:

```
 M cowork_l1l4_architecture_audit.md
```

`git diff --stat HEAD` → `cowork_l1l4_architecture_audit.md | 9 +++++++--  (7 insertions, 2 deletions)`.

The hundreds of `"LF will be replaced by CRLF the next time Git touches it"` lines that accompany `git diff`
are **warnings, not diffs** — caused by `core.autocrlf=true` (a `.gitattributes` is present). **None of those
files appear in `git status --porcelain`.** They are the Linux-sandbox's "balanced +/- churn" view; on the
Windows working tree they carry **zero** content change.

Working-copy line counts of the three allegedly-truncated files vs HEAD blob — **all identical to HEAD, none truncated**:

| file | working | HEAD | tail |
|---|---|---|---|
| `src/composing/analysis/notemodel/note_model.h` | **235** | 235 | `} // namespace mu::composing::analysis::notemodel` |
| `src/composing/analysis/slicing/slicer.h` | **105** | 105 | `} // namespace mu::composing::analysis::slicing` |
| `src/composing/analysis/slicing/slicer.cpp` | **109** | 109 | `} // namespace mu::composing::analysis::slicing` |

`git diff --stat HEAD --` for those three is **empty** (working == HEAD). They end with proper closing
namespace braces, **not mid-comment**. The sandbox's `note_model.h` = 158-line / "ends mid-comment" view
does **not** reproduce here. *(Note: the sandbox path guesses `src/composing/note_model.h` etc. were wrong;
the real paths are under `analysis/notemodel/` and `analysis/slicing/`.)*

`section/localmodulationdetector.h` — **118 lines, identical to HEAD, plain text** (not binary). Sandbox artifact.

### A2 — Stale lock

`.git/index.lock` existed: **0 bytes, mtime 2026-06-26 12:30** (sandbox cited 10:30; the date on this machine
is 12:30). **No `git`/`ninja`/`cmake`/`cl.exe`/`MuseScore` process running** (checked via `tasklist`). It was
therefore confirmed-stale and removed: `rm -f .git/index.lock` → confirmed absent. Git read ops (`status`,
`diff`) were succeeding throughout, so the lock was not actively blocking.

### A3 — Classification of the one modified file

`cowork_l1l4_architecture_audit.md` — **(i) genuine content change.** `git diff --ignore-all-space` still
reports the 7/2 change, so it is real content, not EOL churn. The diff is a **Cowork-doc correction** to the
audit's "orphaned test fixtures" bullet — it documents that the original orphan list was partly wrong and that
`mono_smoke_test.musicxml` is in fact loaded by `tools/test_batch_analyze_regressions.py:117,137` (the exact
`mono_smoke_test` re-verification the instruction references). This is **attributable, intended work** →
per A4, reported and **left untouched** (not discarded).

### A4 / A5 — Repairs performed

| candidate | classification | action |
|---|---|---|
| `note_model.h` / `slicer.h` / `slicer.cpp` | **intact, == HEAD** (not truncated) | none needed |
| `localmodulationdetector.h` | **intact, == HEAD** (not binary) | none needed |
| ~the LF→CRLF "churn" files | **(ii) EOL warnings, not diffs** | none; **not** mass-renormalized (separate hygiene decision); cause = `core.autocrlf=true` + tracked `.gitattributes` |
| `cowork_l1l4_architecture_audit.md` | **(i) genuine, attributable doc edit** | left intact |
| `.git/index.lock` | stale 0-byte, no holding process | **removed** |

**No file required restoration; there is no corruption on this machine.** The sandbox's truncation/binary/churn
view is a sandbox-vs-Windows-git divergence, exactly as the instruction anticipated. Final `git status` after
repair: still only ` M cowork_l1l4_architecture_audit.md` (+ untracked `scratch_artifacts/`). The tree builds
(Part B).

---

## Part B — Verified green build + captured artifacts

### B1 — Clean build (PASS)

Built via `BUILD_AND_TEST.md`: `powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"`
→ exit 0. CMake reconfigured cleanly (`Configuring done`, `Generating done`). Because the tree carries **no
source change**, ninja had nothing to rebuild — verified definitively by a direct ninja invocation:

```
$ ninja -C ninja_build_rel composing_tests notation_tests pipeline_snapshot_tests MuseScore5.exe batch_analyze
ninja: Entering directory `C:/s/MS/ninja_build_rel'
ninja: no work to do.          # exit 0
```

The exes are the current-HEAD (`7de96a63f2`) binaries (dated 11:00 from the prior at-HEAD build; nothing changed
to invalidate them). The one `error`-matching line in the build log was a CMake feature probe
(`Performing Test VLA_SUPPORTED -- failed to compile`, expected on MSVC), **not** a build error.

### B2 — Three suites, captured (raw tails below) — ALL GREEN

| suite | result | exit |
|---|---|---|
| `composing_tests` | **643 PASSED** / 51 suites (1 DISABLED) | 0 |
| `notation_tests` | **53 PASSED**, 4 SKIPPED / 7 suites (0 failed) | 0 |
| `pipeline_snapshot_tests` | **11 PASSED**, 1 SKIPPED, 3 DISABLED / 2 suites | 0 |

Raw tails (captured to `scratch_artifacts/*_out.txt`):

```
composing_tests:           [==========] 643 tests from 51 test suites ran. (1099 ms total)
                           [  PASSED  ] 643 tests.    YOU HAVE 1 DISABLED TEST
notation_tests:            [==========] 57 tests from 7 test suites ran. (48317 ms total)
                           [  PASSED  ] 53 tests.   [  SKIPPED ] 4 tests
pipeline_snapshot_tests:   [==========] 12 tests from 2 test suites ran. (102486 ms total)
                           [  PASSED  ] 11 tests.   [  SKIPPED ] 1 test    YOU HAVE 3 DISABLED TESTS
```

The 4 notation skips (`MozartK279…FLydian`, `…CadenceMarkersOnCorelli`, two `BehaviorSnapshot_*`) and the 1
snapshot skip (`PipelineDivergenceCObservation.GenerateReport`, a diagnostic report-generator) are pre-existing
gated/diagnostic tests, not failures. The canonical **11/11** snapshot goldens pass.

### B3 — BIR characterisation (Baroque / Jazz / Default) — EXACT IDENTITY-SET MATCH

Ran `characterise_bir_false.py --corpus-dir tools/corpus/{baroque,jazz,default}` on the existing
manifest-validated per-preset corpora (353/353 each; no regen needed — no compiled code changed).

| preset | count | identity-set vs CLAUDE.md | corpus_manifest.json sha256 |
|---|---|---|---|
| Baroque | **53** | **EXACT MATCH** (diff empty) | `1ade1c17da449479d9b2b9fd746a02a29b676cb66219735819ec4751c337b6d0` |
| Jazz | **24** | **EXACT MATCH** (diff empty) | `6c5aa851bd0112ebe6fd94dc70dd6517bf92204421a3fbb444c84c5abcab66a3` |
| Default | **53** | **EXACT MATCH** (diff empty) | `bf717454b455995d4a9f4963cf0ef9a2ca60ca08fe69c4bc3d82f82d524582d2` |

The gate is the **case-identity set**, not the integer (CLAUDE.md). All three measured `stem@tick` sets were
diffed against the authoritative CLAUDE.md sets and matched with **zero** delta. The Default set =
Baroque-53 with `{bwv352@1440, bwv60.5@30960}` replaced by `{bwv227.7@18000, bwv387@10560}` — this
**resolves the ⚠ "re-confirm Default at next regen" caveat** in CLAUDE.md (measured Default IS that swap).

---

## Part C — Test-adequacy + branch-coverage audit

### C1 — Confirm / refute Cowork's headline gaps (cited at source)

Several headline gaps in the instruction's C1 list are **REFUTED at source** — same correction pattern as
`mono_smoke_test`. Verdicts below are first-hand (grep/read), corroborated by the measured coverage in C2.

| # | Instruction/audit claim | Verdict | Evidence (file:line) |
|---|---|---|---|
| 1 | **"L2 clip has ZERO direct tests"**; re-slice-equivalence invariant unpinned | **REFUTED** | `src/composing/tests/slicer_tests.cpp` (703 lines, in CMake at `tests/CMakeLists.txt:52`) directly drives `changePointSlices` on synthetic spans: clip-in `CP2:513`, clip-out `CP3:540`, seam-aware edge-extend `CP5:592`/`CP6:639`, and the **re-slice-equivalence invariant `CP7:670` (`ReSliceEquivalence_ExtendEqualsDirectBuild`, EXPECT_EQ at :698)**. Robustness too: empty `S7a:302`, single `S7b:311`, unison `S4b:218`. Measured line coverage of `slicer.cpp` = **100%**. |
| 2 | **chordpostpasses "indirect only / no test by name"** (audit Q3) | **REFUTED** | `applyIter8691Pedal` is called directly in `postscoringgates_tests.cpp:868,880,891,912,928,946,955` (6 TEST blocks, Iter86/Iter91). Measured `chordpostpasses.cpp` line coverage = 98.1% (composing) / 100% (union). |
| 3 | **Robustness "largely unasserted at the L3 emission scorer"** | **REFUTED** | `keymodeanalyzer_tests.cpp`: empty `:33`, single `:39`, all-12-chromatic `:481` (`AllChromaticPitchesDoesNotCrash`), out-of-range key-sig `:413`. 4 of 5 degenerate classes covered; only **unison** missing. |
| 4 | **chordvoicing `closePositionVoicing`/`chordTonePitchClasses` — zero direct tests** | **CONFIRMED** | `chordvoicing.cpp:33,180`. No test in `src/composing/tests/` names either; sole reference is integration `notationimplode_tests.cpp:683`. Measured: composing 0% line, notation 89.5% (integration only). |
| 5 | **`formatNashvilleNumber` asserted by one test** | **CONFIRMED** | `chordsymbolformatter.cpp:1023`; asserted only by `chordanalyzer_tests.cpp:1430` (`FullyDiminishedSeventh_NashvilleHasExactlyOneDegreeSymbol`). |
| 6 | **Robustness weak at L4 `analyzeChord`** (empty/single/unison/atonal/out-of-range) | **CONFIRMED (mostly)** | Only the `<3`-distinct-PC empty gate is asserted (`chordanalyzer_tests.cpp:172`). No direct single/unison/atonal/out-of-range test. Harness = `test_helpers.h:110-126` (`analyzeWithGates`). |
| 7 | **L3 threads untested: `excludeStaves`, `ignoreDeclaredMode`, dynamic-lookahead loop, `populateEmissionConfidence` side-effect** | **CONFIRMED (branch/assertion gap)** | `excludeStaves` true-branch `keyresolver.cpp:156` only ever called with empty `kNoExclude` (`regionanalysis_tests.cpp:70`); `ignoreDeclaredMode` `keyresolver.cpp:242` only default-false; dynamic-lookahead loop `keyresolver.cpp:303-326` (no multi-iteration driver / `KeyResolveDump` assert); `populateEmissionConfidence` `keymodesequence.cpp:201-228,413` executes but **no test asserts** the confidence it writes. See C2 note on line-vs-branch. |
| 8 | **Leading-tone presence gate (~0.1) has no regression pin** | **CONFIRMED (with nuance)** | `keymodeanalyzer.cpp:374` (`ltWeight > 0.1`). Exercised implicitly by mode-ID tests (`keymodeanalyzer_tests.cpp` harmonic-minor/Ionian♯5) but **no test pins the 0.1 boundary**. |
| 9 | **L4 spec↔production divergence: prod has no abstain/uncertain/inherit; `chordslicedecoder` is the spec-conformant one but production-dead; spelling-pin unbuilt** | **CONFIRMED (all 4)** | `ChordSliceDecoder` referenced only in `chordslicedecoder.{h,cpp}` + `decode_chord_tests.cpp` — **0 refs in `regionanalyzer.cpp`** (self-documented isolation `chordslicedecoder.h:76-81`). It models uncertainty: `SliceChord::uncertain` `chordslicedecoder.h:213`, `uncertaintyMargin` `:115`, set at `chordslicedecoder.cpp:298,319`. Production always emits a winner (`harmonicfunctionlayer.cpp:539-541`; `regionanalyzer.cpp` `continue`s on empty, no uncertain marker; `ChordAnalysisResult` has no abstain field). Spelling-pin explicitly deferred to "Increment C" (`chordslicedecoder.h:40-49`); tpc is only a fallback heuristic for symmetric-aug (`chordanalyzer.cpp:841-868`) + a score modifier (`:1298`), never a deterministic root pin; `spellingview.*` is unreferenced by the chord path. |

### C2 — Measured coverage

**Toolchain note (criterion 4):** OpenCppCoverage is **not installed**; there is no `gcov`/`llvm-cov`; the compiler
is MSVC `cl.exe` (BuildTools 2022, not Enterprise); `dotnet` has runtime but **no SDK** (cannot install
`dotnet-coverage`). The legacy `CodeCoverage.exe` (v17) is a deprecated stub whose `collect` only prints usage.
The working tool is **`Microsoft.CodeCoverage.Console.exe`** (found under BuildTools `…\CodeCoverage.Console\`).
It produces **block/line coverage, not branch coverage** — confirmed: the emitted cobertura has **0**
`branch="true"` entries (the `branch-rate="1"` is a placeholder). **True branch coverage (criterion 4) is
therefore NOT available on this toolchain.** What follows is measured **line/block coverage** (a branch proxy);
the per-function *branch*-gap remains the static list in C1/C3 — **no numbers are fabricated.**

Collected over `composing_tests` (exit 0, cobertura) and `notation_tests` (exit 0, cobertura), parsed and
aggregated for `src/composing/analysis/**`. **UNION** = a source line counted covered if hit by *either* suite.
(Snapshot suite not separately instrumented; it drives the same `analyzeSection`/region path as notation, so the
union is a lower bound for those layers.)

**Per-layer line coverage (UNION composing ∪ notation):**

| layer | line% (union) | lines |
|---|---|---|
| L1 notemodel | 97.7% | 126/129 |
| L1.5 engravingbridge | 98.2% | 384/391 |
| L2 slicing (new) | **100.0%** | 24/24 |
| L2 harmony (legacy seg) | 98.6% | 205/208 |
| L3 key | **83.3%** | 563/676 |
| L4 chord | 93.6% | 1288/1376 |
| L4 function | 96.2% | 228/237 |
| decode | 40.0% | 4/10 |
| region (orchestrator) | 85.8% | 448/522 |
| section | 89.4% | 355/397 |
| scoreharvest | 96.9% | 62/64 |

**Lowest-covered files (union), and where the suite split matters:**

| file | composing% | notation% | UNION% | reading |
|---|---|---|---|---|
| `key/modepriorpresets.cpp` | 0 | 0 | **0.0** | genuinely uncovered by both unit suites (presets/constants) |
| `chord/chordslicedecoder.h` (+`note_model.h`,`keymodeanalyzer.h`,`harmonicrhythm.h`) | 0 | 0 | 0.0 | header inline/decls; trivially uncovered |
| `key/keymodeformatting.cpp` | 0 | 36 | 36.0 | indirect-only, weak |
| `decode/chordpathdecoder.h` | 0 | 50 | 40.0 | prod-wired header, partially exercised via bridge |
| `region/sparsechordrefinement.cpp` | 9 | 59 | 59.2 | no direct test; partial via notation |
| `chord/chordvoicing.cpp` | 0 | 89.5 | 89.5 | **no composing unit test**; integration only (`notationimplode`) |
| `section/sectionanalyzer.cpp` | 0 | 90.7 | 90.7 | **no composing unit test**; bridge/notation only |
| `region/regionanalyzer.cpp` | 40.5 | 84.5 | 91.6 | orchestrator: composing barely touches it; bridge drives it |
| `section/sectioncadencedetection.cpp` | 0 | 100 | 100.0 | no *direct* test, but fully line-exercised by notation |
| `chord/chordslicedecoder.cpp` | 93.2 | 0 | 93.2 | prod-dead decoder; unit-tested only |
| `slicing/slicer.cpp` | 100 | 100 | **100.0** | refutes "L2 clip zero tests" |

**Measured line-vs-branch caveat (the key criterion-4 point).** The C1 §7 "untested" threads are all
**line-executed** (measured hits): `keyresolver.cpp:303-326` 12/12 lines hit, `:156` hit, `:242` hit,
`keymodesequence.cpp:201-228` 15/15 hit, `keymodeanalyzer.cpp:374` hit. **Line coverage does not refute the
gap** — it is blind to (i) *which branch* of an evaluated condition was taken (`excludeStaves` runs only with
the empty set; `ignoreDeclaredMode` only false), (ii) *whether a loop iterated* (lookahead body ran once; no
multi-iteration driver), (iii) *whether an output was asserted* (`populateEmissionConfidence` runs but nothing
checks it). This is precisely why branch coverage (unavailable) **and** the static audit are both required.

### C3 — Reconciliation with Cowork's static audit

**Where measured AGREES with Cowork (`cowork_l1l4_architecture_audit.md` Q3 + the instruction's C1):**
- `chordvoicing` — no direct unit test (0% composing; integration only). ✓
- `sectionanalyzer` / `analyzeSection` — no composing-side unit test; validated by notation/snapshot (0%
  composing → 90.7% notation). ✓ The audit's exact wording is borne out.
- `modepriorpresets` — no direct coverage; **measured 0%/0% union** (the one genuinely-uncovered analysis file). ✓
- `keymodeformatting` (indirect, 36% union), `sparsechordrefinement` (no direct, 9%→59%). ✓
- `formatNashvilleNumber` — one test. ✓
- L4 spec↔production divergence (abstain/uncertain/inherit absent in prod; `chordslicedecoder` prod-dead; spelling-pin
  unbuilt). ✓ — confirmed at source (C1 §9).
- L3 option/branch threads untested (`excludeStaves`/`ignoreDeclaredMode`/lookahead/`populateEmissionConfidence`),
  as a **branch/assertion** gap that line coverage cannot see. ✓

**Where measured DISAGREES / corrects:**
- **"L2 clip has ZERO direct tests" (instruction C1) — WRONG.** `slicer_tests.cpp` exists, is built, gives the
  slicer 100% line coverage, and pins clip-in/out, seam-extend, **and the re-slice-equivalence invariant** (CP7).
  This is the headline correction of this audit.
- **"chordpostpasses indirect only" (audit Q3) — WRONG.** `applyIter8691Pedal` has 6 direct TEST blocks.
- **"robustness largely unasserted at the L3 emission scorer" (instruction C1) — OVERSTATED.** The L3 emission
  scorer (`analyzeKeyMode`) has empty/single/all-chromatic/out-of-range robustness tests; only **unison** is missing.
  (The robustness gap is real and severe at **L4 `analyzeChord`**, not at the L3 emission scorer.)

**Gaps Cowork slightly mis-stated (nuance, not error):**
- `sectioncadencedetection` — audit "no direct coverage" is true for *direct* tests, but it is **100% line-covered**
  by notation. "No targeted/direct test" ≠ "unexercised."
- `metricweights` — audit "constants only"; measured 96.9% union, i.e. it carries exercised logic, not just constants.
- `decode/chordpathdecoder.h` is **production-wired** (commit sites) yet only 40% union line-covered — worth a tracking
  note (the inert `DecodeQualityLevel::Normal/Deep` branch the audit Q5 flagged is part of the uncovered remainder).

**Net.** Coverage is **broad** (most L1–L4 modules 90%+ line, union). The genuine adequacy gaps, now measured, are:
(a) **L4 `analyzeChord` robustness** (degenerate inputs) — the single weakest spot, and **not** at L3 emission as the
instruction framed it; (b) `chordvoicing` and `modepriorpresets` direct coverage; (c) the **branch/assertion-level**
L3 option threads, invisible to line coverage and to be closed only with targeted tests (and, ideally, a branch-coverage
toolchain); (d) `formatNashvilleNumber`. The L2-clip and chordpostpasses "gaps" are **already closed** and should be
struck from the backfill list.

### C4 — No new tests written

This pass is audit + measurement only. The backfill (the next ratified step) is driven by C3: prioritise L4
`analyzeChord` robustness + `chordvoicing` + the L3 branch/assertion threads; do **not** spend effort on L2-clip
or chordpostpasses (already covered).

---

## Stop-condition check

- No genuine uncommitted source work found (the one modified file is an attributable Cowork-doc edit) → not discarded.
- Clean build succeeded (`ninja: no work to do`) → no STOP.
- No production logic / no new test / no inference-fix touched → in scope.
- No push to `upstream`.

## Artifacts (under `scratch_artifacts/`, untracked)

`build_out.txt`, `ninja_direct.txt`, `composing_tests_out.txt`, `notation_tests_out.txt`,
`pipeline_snapshot_tests_out.txt`, `bir_{baroque,jazz,default}.txt`, `set_{…}.txt`, `composing.cobertura.xml`,
`notation.cobertura.xml`, `coverage_report.txt`, `coverage_merged.txt`, `parse_cov.py`, `parse_merge.py`,
`line_hits.py`.
