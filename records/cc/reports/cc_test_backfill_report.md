# CC — test-backfill: coverage tooling + close the measured gaps

> **Scope honoured: tests + a coverage tool + capture ONLY.** No production logic, no behavior/gate/scoring
> change. Every new assertion is oracle-derived (music theory / documented contract) per rule 1; no production
> code was edited to make a test pass (rule 2); no robustness test crashed (rule 3). Date: 2026-06-26.

## Commit shas (verify by explicit sha)

| step | sha | contents |
|---|---|---|
| §0 doc | **`987021d1ed`** | `cowork_l1l4_architecture_audit.md` ONLY (29 ins / 16 del) — the audit coverage-correction banner. `git show --stat 987021d1ed` = one doc file, no source. |
| §5 tests | **`d042a03a03`** | 5 new test files + `src/composing/tests/CMakeLists.txt` + `tools/coverage/{run_coverage.ps1,parse_cobertura.py}`. NO production source. |

`git show --stat d042a03a03` file list (8 files, all test/build/tooling):
`CMakeLists.txt`, `analyzechord_robustness_tests.cpp`, `chordvoicing_tests.cpp`, `l3_coverage_tests.cpp`,
`modepriorpresets_tests.cpp`, `nashville_tests.cpp`, `tools/coverage/parse_cobertura.py`,
`tools/coverage/run_coverage.ps1`.

> **Left UNSTAGED on purpose:** `COWORK_HANDOFF.md` appeared modified mid-session (a Cowork-authored "NEVER BASH
> FOR LOCAL FILES" standing-rule edit, user-mandate 2026-06-26) — **not my work**, not part of this deliverable,
> so it is left for Cowork. `scratch_artifacts/` (raw outputs, ~80 MB cobertura) stays untracked.

---

## §1 — Coverage tooling

### Install — SUCCEEDED (portable, no admin)
OpenCppCoverage **0.9.9.0** is installed and working at `C:\Users\vince\tools\OpenCppCoverage\OpenCppCoverage.exe`.
Path taken (the §4 "won't install → STOP" did NOT trigger):
- Not on PATH; `choco`/`winget` present but the package installs to Program Files → **needs admin** (I am not
  elevated), and the GitHub release ships only Inno Setup `*.exe` installers (no portable zip).
- 7-Zip cannot open Inno Setup archives. **Resolved with `innoextract` 1.9** (portable): extracted the installer's
  `app\` payload (`OpenCppCoverage.exe` + boost/`msdia140.dll`/exporter DLLs) and copied it to a stable user dir —
  a clean no-admin install. Verified `--help` runs and it instruments the release build (PDBs present, 617 MB).

### TOOLING FINDING (factual correction to the instruction's premise)
**OpenCppCoverage measures LINE / instruction coverage only — it does NOT emit gcov-style per-branch coverage.**
Verified empirically: the cobertura export has `branches-valid="0"` and every `<line>` carries only `hits` (zero
`branch="true"` even on a single-test run where most branches must be half-covered); the HTML marks each line
covered/uncovered with **no "partial" state**. So the instruction's "line+branch coverage tool" description does
not match the tool. This is **not** a STOP (the tool installed and runs) and **not** the substitution the
instruction forbade (that was the block-only `Microsoft.CodeCoverage.Console`; this is the requested OpenCppCoverage).
**Consequence for criterion 4:** OpenCppCoverage is used exactly as §1 directs — a **gap-finder for lines NO test
executes**. The *which-branch-of-an-executed-line* gaps (the L3 option threads) are driven by the static
branch/assertion audit (`cc_tree_repair_and_coverage_report.md` C1 §7), which line coverage is structurally blind to.

### Baseline (committed `7de96a63f2`, `composing_tests` only, src\composing line coverage)
Captured: `scratch_artifacts/coverage/composing_baseline.cobertura.xml` (+ `_html`, `_run.txt`).

| layer | baseline line% |
|---|---|
| L3 key | 77.1% (561/728) |
| L4 chord | 82.9% (1365/1646) |
| TOTAL (composing analysis) | 68.6% (3529/5141) |

The two genuine 0% files surfaced exactly as the audit predicted: `chord/chordvoicing.cpp` **0/88**,
`key/modepriorpresets.cpp` **0/68**.

---

## §2 — Tests added (52 new, 5 files), each oracle-derived

| file | tests | what / oracle |
|---|---|---|
| `chordvoicing_tests.cpp` | 23 | `chordTonePitchClasses` per quality (Maj/min/dim/aug/ø/sus2/sus4/power/Unknown), sevenths, added-6 guard, ♭5/♯5 fifth-override, OmitsThird, all 7 upper extensions, dedup, interval-sort; `closePositionVoicing` Unknown→empty(bass −1), bass=36+rootPc, octave-wrap stacking, **bassPc ignored (always root position)**. Oracle = tertian chord-tone theory + the documented voicing formula. |
| `modepriorpresets_tests.cpp` | 5 | exactly 5 presets in documented order; **Standard == struct default initializers** (documented contract); presets distinct; Jazz embraces Dorian/Mixolydian (design intent); + labelled regression-guards for tuned magnitudes. |
| `nashville_tests.cpp` | 7 | scale degrees 1..7, per-quality suffixes, sevenths (maj7/7/°7 incl. °° dedup), minor-key tonic — all NNS oracle; + labelled regression-guards for the `?` placeholder and crude slash-bass degree. |
| `analyzechord_robustness_tests.cpp` | 10 | criterion 2: empty / single / unison / same-pc-octaves → empty (contract); chromatic & whole-tone clusters, ±100 key fifths, absent/invalid TPC, extreme MIDI → **no crash + structurally-valid result**. |
| `l3_coverage_tests.cpp` | 7 | declared-mode penalty arm (252-candidate dump: penalty only on out-of-class, 0 when none); unison no-crash; resolver `excludeStaves` (exclude all → fallback), `ignoreDeclaredMode` (dump ordinal → −1), dynamic-lookahead (unreachable threshold → cap; always-met → initial window); `redecodeRange` arg-guard (first<0/last≥T/first>last → empty); decoded `chosen.normalizedConfidence` is C1 [0,1]. |

Reach-back `maxReachSteps` hard-bound stop was **deliberately not added**: the existing `reachback_tests.cpp`
already covers fire/converge/score-start, and isolating the bound as a *distinct* outcome is fixture-fragile (no
clean oracle) — recorded here rather than forced into a brittle test.

---

## §3 — Re-measure + gate (evidence, not "all green")

### Suites (raw output in `scratch_artifacts/*_out.txt`)
| suite | before | after | result |
|---|---|---|---|
| `composing_tests` | 643 | **695** (+52) | **695 PASSED**, 0 failed, 1 pre-existing DISABLED |
| `notation_tests` | 53 | 53 | **53 PASSED**, 4 pre-existing SKIPPED (unchanged binary) |
| `pipeline_snapshot_tests` | 11 | 11 | **11 PASSED** — snapshot byte-identical |

### BIR gate — `characterise_bir_false.py` on the existing per-preset corpora (no regen; production unchanged)
**Baroque 53 / Jazz 24 / Default 53 — EXACT, zero movement.** (Output: `scratch_artifacts/bir_after_*.txt`.)

### Byte-identity proof
The §5 diff is **test-only** — 5 `tests/*.cpp` + `tests/CMakeLists.txt` + `tools/coverage/`. No `src/**` production
`.cpp/.h`, no `composing_analysis` source. The build rebuilt **only `composing_tests`** (`notation_tests.exe`,
`pipeline_snapshot_tests.exe`, `batch_analyze.exe`, `MuseScore5.exe` are the unchanged 11:00 binaries). Therefore
BIR and snapshots are byte-identical **by construction**, and the measured 53/24/53 + 11/11 confirm it.

### Coverage delta (`composing_tests`-only line coverage; `scratch_artifacts/coverage/composing_final.cobertura.xml`)
| file | before | after |
|---|---|---|
| `chord/chordvoicing.cpp` | 0.0% (0/88) | **90.9% (80/88)** |
| `key/modepriorpresets.cpp` | 0.0% (0/68) | **100% (68/68)** |
| `chord/chordsymbolformatter.cpp` | 92.0% (413/449) | 94.0% (422/449) |
| `chord/chordanalyzer.cpp` | 91.2% (415/455) | 91.4% (416/455) |
| `key/keyresolver.cpp` | 87.6% (92/105) | **92.4% (97/105)** |
| `key/keymodesequence.cpp` | 92.0% (185/201) | 92.5% (186/201) |
| `key/keymodeanalyzer.cpp` | 93.1% (283/304) | 93.1% (283/304)* |

\* line% flat is expected: the declared-mode / unison branches were already line-executed; the new value is the
**branch+assertion** coverage that line% cannot show (exactly the line-vs-branch caveat). 

| layer | before | after |
|---|---|---|
| L3 key | 77.1% | **87.2%** |
| L4 chord | 82.9% | **88.4%** |
| TOTAL (composing analysis) | 68.6% | **71.8%** (3529 → 3693 lines) |

---

## Surfaced findings (rule 2 / rule 3 output)

1. **No crashes (rule 3 not triggered).** Every robustness input — empty/single/unison/chromatic/whole-tone
   clusters, ±100 key fifths, invalid TPC (999/−50/12345), extreme MIDI (0/127) — returned cleanly with a
   structurally-valid result. No crash-guard production change is needed or made.
2. **No oracle assertion failed → no `DISABLED_`/xfail needed.** Every decidable oracle I asserted matches current
   production behavior, so there is no surfaced *defect* of the rule-2 kind. (Had one failed, it would be xfail'd
   with expected-vs-actual; none did.)
3. **Documentation/spec mismatch — `formatNashvilleNumber` degree<0 (flagged, not xfail'd).** The instruction
   stated the contract as `degree < 0 → ""`. Production actually emits **`"?"`** (`nashvilleDegree()` returns `"?"`
   outside 0..6, with a `// just show as "?"; refine as needed` comment), then appends the quality/extension/bass
   suffixes. Neither `""` nor `"?"` is mandated by the Nashville system (it has no symbol for a non-diatonic root),
   so `""` is not a proven oracle — hence **flagged for Cowork, pinned as a regression-guard, not xfail'd**. Same
   class: the slash-bass degree uses a crude `semitone%7+1` map (e.g. C/E → `"/5"`, not the true `/3`) — pinned as
   a labelled regression-guard.
4. **Tooling correction (see §1):** OpenCppCoverage is line-coverage-only, not the "line+branch" tool the
   instruction assumed. Reported honestly; used as the line-level gap-finder it actually is.

## Stop-condition check
- No production logic / behavior / gate / scoring change. ✓
- No L4 abstain/uncertain/inherit/spelling-pin tested or built (production-absent — out of scope). ✓
- No robustness crash → no STOP. ✓
- Coverage tool installed → no STOP. ✓
- No `upstream` push; both commits local-only (`master` ahead of `origin/master`). ✓
