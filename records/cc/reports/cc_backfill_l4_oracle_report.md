# CC backfill report — Phase-5 branch backfill (round 2), cluster 2: L4 oracle + gates

**Tests-only. No production logic/behaviour change. `upstream` not touched; local commit only.**

## §0 — Preamble
No unstaged `cowork_*`/`COWORK_*` docs present (`git status` clean apart from this cluster's two test
files + the gitignored `scratch_artifacts/`). Nothing to commit under §0.

## §1 — Headline

| Suite | Before (cluster-1 `3f2e4bebe2`) | After |
|---|---|---|
| `composing_tests` | 715 PASSED | **778 PASSED** (+63 new tests) |
| `notation_tests` | 53 PASSED / 4 SKIPPED | **53 PASSED / 4 SKIPPED** (unchanged) |
| `pipeline_snapshot_tests` | 11 PASSED / 1 SKIPPED | **11 PASSED / 1 SKIPPED** (goldens NOT refreshed) |
| BIR corpus | 53 / 24 / 53 | **53 / 24 / 53 by construction** (zero production bytes changed) |

- **No production source touched** — `git diff --stat` shows only `src/composing/tests/CMakeLists.txt` (+1)
  and `src/composing/tests/postscoringgates_tests.cpp` (+620), plus the new untracked
  `src/composing/tests/chord_branch_tests.cpp`. `notation_tests` + `pipeline_snapshot_tests` link the
  unchanged `composing_analysis`, so their results are identical binaries — corpus/snapshot movement is
  impossible by construction, not by re-measurement. The §3 STOP condition did not arise.
- **Surfaced defects: NONE.** Every oracle (music-theory / documented contract, re-derived at source)
  matched the current implementation — no `DISABLED_`/xfail needed. (One test initially failed on a wrong
  *sentinel* assumption I made — `ClosePositionVoicing.bassPitch` defaults to **−1**, the documented
  "empty voicing" value, not 0 — corrected to the documented value. Not a code defect.)
- **No fixtures added** — every test is synthetic (hand-built results/gateCtx/tones or direct calls to the
  public leaf helpers); no `.mscx`/`.musicxml` was needed.

## §2 — Coverage re-measurement (the round-2 progress check)

UNION branch coverage (`composing_tests ∪ notation_tests`, same runner/methodology as
`cc_union_branch_coverage_report.md`; `powershell.exe -File tools\coverage\run_branch_coverage.ps1` — note:
**`pwsh` (PowerShell 7) is not installed on this box; the runner must be invoked via `powershell.exe`
(Windows PowerShell 5.1)** — the report's `pwsh` reproduction line is wrong for this environment).

The §5 line numbers in `cc_union_branch_coverage_report.md` are **stale** for the files the types-header
refactor (`11f26864f9`) shifted (`analysisutils.h`, `chordanalyzer.*`, `harmonicfunctionlayer.cpp`); the
"before" column below was re-derived fresh at HEAD from `union_branch_export.json` *prior* to these tests.

| File | Branches | Before (unhit / %) | After (unhit / %) | Δ unhit |
|---|---:|---:|---:|---:|
| `chord/analysisutils.h` | 46 | 3 / 93.48% | **3 / 93.48%** | 0 ‡ |
| `chord/chordanalyzer.cpp` | 738 | 16 / 97.83% | **12 / 98.37%** | −4 |
| `chord/chordanalyzer.h` | 52 | 11 / 78.85% | **11 / 78.85%** | 0 ‡ |
| `chord/chordpostpasses.cpp` | 182 | 17 / 90.66% | **2 / 98.90%** | −15 |
| `chord/chordvoicing.cpp` | 116 | 11 / 90.52% | **6 / 94.83%** | −5 |
| `chord/postscoringgates.cpp` | 340 | 50 / 85.29% | **7 / 97.94%** | −43 |
| `function/harmonicfunctionlayer.cpp` | 216 | 6 / 97.22% | **1 / 99.54%** | −5 |
| **cluster total** | **1688** | **114 / 93.25%** | **42 / 97.51%** | **−72** |

‡ = **covered-by-test but coverage-uncredited** — see §5 (inline-header attribution; the larger cousin of
cluster-1's `isChordTrackStaff:83` COMDAT note).

The instrumented run executed all 778 composing tests. Whole-module branch unhit moved **999 → 891**
(−108: −72 from these L4 files, the remaining −36 are this run's coverage of L1.5/L2/L3 paths the new
synthetic chord/gate calls happen to traverse — incidental, not the target).

## §3 — Tests added (63 tests: 22 in `chord_branch_tests.cpp`, 41 in `postscoringgates_tests.cpp`)

### `chord_branch_tests.cpp` (new file, 22 tests) — the leaf oracles
- **`analysisutils.h` (1):** `IonianTonicPcFromFifths_FullTable` — the major-key tonic pc for every
  signature −7..+7 (oracle = `(7·fifths) mod 12`), incl. the unhit Cb=−7→11 / A=+3→9 / F#=+6→6, plus the
  out-of-range default → C.
- **`chordanalyzer.h` (7):** empty `normalizeMergedBassTone` no-op; `mergeChordAnalysisTones` same-pc TPC
  backfill (real-tpc → backfilled, −1-tpc → not); `bassToneFromTones` ≥2-isBass lowest-pitch pick + non-bass
  skip; `advanceTemporalContext` sentinels (rootPc<0 → 0.0 weight, empty rawCandidates → 0.0 score, <2 → −1
  margin) + the non-sentinel contrast.
- **`chordvoicing.cpp` (7):** per-quality triad pc-sets (all 9 qualities); FlatFifth/SharpFifth flags inert
  on non-perfect-fifth qualities; HalfDim+Maj7 structural-m7 dup-avoidance; AddedSixth skipped when a
  seventh (Maj7 / Dim7) is present; `closePositionVoicing` Unknown→empty, triad→C2-C3 bass + ascending treble.
- **`chordanalyzer.cpp` (5):** via the **public `buildChordResult`** (drives `detectExtensions`
  deterministically with hand-built pcWeight/tpcForPc) — add#9-vs-m3 (Major reading without the major third
  is *not* a #9, with it *is*), #13-on-diminished suppressed; via `analyzeChord` — same-pc bass-register
  dedup, and the below-`bassMinWeight` → lowest-pitch fallback (21-tone equal-weight spread so every tone is
  < 5% of the total).
- **`harmonicfunctionlayer.cpp` (2):** `resolutionEdgeBonus` known-quality-but-prevRoot<0 → 0.0 (+ contrast);
  `applyHarmonicFunction` empty snapshot → no results, `chosenResult` unchanged.

### `postscoringgates_tests.cpp` (+41 tests) — the gate fire/no-fire arms
Outer guard (`inversionBonusReduction==1.0` disables the family); bias-correction HalfDim first-inversion
exception (bass=b5 accepted; missing b5 / missing m7 rejected); Gate A direct (best-alt-Major → no flip) +
FM2 raw-scan completion; Gate E (alt-not-+8 no-flip; to-next stepwise flips); Gate F (from-previous stepwise
flips); Gate G (mediant iiiø7 flip; no-HalfDim-anywhere; HalfDim-present-no-signal; G-C recent-roots slots
0/2; G-B matching-forward-no-stepwise; HalfDim-at-wrong-root); Gate H (H-C recent-roots slots 0/2; H-D
consecutive; H-B forward-mismatch / no-stepwise; recent-roots all-mismatch; non-aug-in-scan-path); Gate I/K/L
(non-augmented-collection alt; same-root-different-bass; non-diatonic; **no-key-resolved keyTonicPc=−1**);
Gate J (dom-candidate-not-Major; diminished-not-root-position); plus `cptIsBassChordTone` per-quality /
per-extension classification through `applyIter8691Pedal` (Sus4-P5, #9, #11, b13, 4th-over-7th → chord
tone, no pedal; foreign bass → pedal detected) and the Iter86/91 `bassPc<0` no-ops + Iter91 plain-triad /
delta / forward-confirmation guards.

Oracle provenance examples: the I4 / +8 / +5 inversion intervals are derived from interval arithmetic; the
viiø7/iiø7/**iiiø7** functional roots from tonic+11/+2/**+4**; the `cptIsBassChordTone` per-quality chord
tones from each quality's triad + the explicit extension bitmask; the bass-min-weight fraction (0.05) and
extension threshold (0.20) read from `ChordAnalyzerPreferences` defaults.

## §4 — Re-classification of triage "ADD-TEST" branches → EXCLUDE-DEFENSIVE / DEFER (NOT tested)

Per the spec's "re-confirm class at source", the residual 42 unhit arms decompose as **13 covered-by-test
(inline-uncredited, §5) + 28 EXCLUDE-DEFENSIVE + 1 DEFER**. The spec's "~98 ADD-TEST" was an **upper bound**;
re-confirmation at source found **~22 over-counts** (provably-unreachable guards routed to ADD-TEST). The
genuinely-reachable ADD-TEST set was ~76, of which 72 are now credited and 13 more are tested-but-uncredited.

**Provably unreachable (EXCLUDE-DEFENSIVE — re-classified from the triage's ADD-TEST):**
- **`chordanalyzer.cpp` (11):** `327:59[F]`/`327:71[F]` — `isSixNine`'s `!rawMin7 && !rawMaj7` is *redundant*
  (`hasAddedSixth`, the first `&&` operand, already requires both false, so these arms can't be reached);
  `404:36[T]`/`565:36[F]`/`600:36[F]` — Sus4 interval-count OOB guards (`size()<3` / `size()==4` / `size()>=3`):
  **no Suspended4 template has <3 or ≠4 intervals** (`kTemplateIntervals` rows 7/12/13/14 are size-4, row 15
  is size-3 with `intervals[2]==7`), so the guarded arms never fire; `876:73[F]` — the augmented-triad
  tautology (if two consecutive interval-4 checks pass, the third is forced by `4+4+4≡0`); `1060:40[F]` /
  `1124:35[F]` — `lowestPitch==max()` is unreachable (empty tones early-return before here); `1396:38[F]` —
  the w_complete root-absent arm is unreachable because the lambda only runs for **root-position** candidates
  (`candBassPc==rootPc`), where the root is by definition the sounding bass (rootW ≥ 0.1); `1521:5[F]` /
  `1522:5[T]` — `ChordAnalyzerFactory::create` exhaustive-enum switch default.
- **`chordanalyzer.h` (1):** `641:12[T]` — `inferNextRootPc` `candidates.empty()` *after* gates: the
  `638` guard already returned on empty, and `applyIter8691Pedal`/`applyPostScoringGates` never reduce a
  non-empty list below its entry size, so this is can't-happen.
- **`chordpostpasses.cpp` (2):** `187:39[F]` — Iter91 `bassPc != rPc` is *redundant* (`patternA||patternB`
  ⟹ delta∈{8,9} ⟹ bass≠root); `76:5[T]` — `cptIsBassChordTone`'s switch `default:` (taken only by
  `ChordQuality::Unknown`, which is not a production winner quality reaching the pedal tail).
- **`chordvoicing.cpp` (6):** `41:13[F]`/`65:13[F]` — the two third/fifth-slot switches have no `default:`
  and case every one of the 9 `ChordQuality` values, so the implicit-default arm is unreachable; `187:9[T]`
  — `closePositionVoicing` `pcs.empty()` (Unknown is filtered at line 182; every other quality yields ≥1 pc);
  `200:13[T]` — `best < kBassLow` (best = 36+rootPc ≥ 36 always); `204:32[T]` — the bass octave-up
  (`best+12<=48` only holds for best==36, where the strict-`<` midpoint tie fails — **the spec's "bass
  octave-up near midpoint" is effectively dead code**); `212:9[F]` — `pcs.size()>1` false (a non-Unknown
  quality always has root+fifth ≥ 2 pcs).
- **`postscoringgates.cpp` (7):** `456/492/529/562 :16[F]` — `results.size()>=2` re-checks (the outer
  guard already guarantees ≥2 and the gates never shrink below it); `346:21[F]`/`421:21[F]` — the
  `!didGFlip`/`!didAugmentedFlip` guards at the **first** sub-gate (the flag is always false there);
  `564:17[F]` — Gate J's `dimWinner.quality==Diminished` first operand (a Diminished original winner is
  never displaced by an earlier gate, so it's always still Diminished here).
- **`harmonicfunctionlayer.cpp` (1):** `516:12[F]` — the guaranteed-alt block's `winBassPc >= 0` guard;
  with a non-empty `results` the winning bass came from a real cell's `bassPc`, so winBassPc<0 is can't-happen
  from `analyzeChord`'s snapshot builder.

**Borderline → tested (the spec's "promote to ADD-TEST only if cheap"):** the `keyTonicPc >= 0` arms of
Gates I/K/L (`457`/`493`/`530`) — `keyTonicPc = −1` is the documented "no key" **sentinel** (the struct
default), so it is representable and oracle-decidable ("no resolved key ⇒ the diatonic inversion gates
I/K/L do not fire"). Tested (`GateI_NoKeyResolved_NoFlip`, `GateKL_NoKeyResolved_NoChange`) and credited.

**DEFER / reachable-but-not-closed (1):** `chordanalyzer.cpp 449:37[F]` — the standard-Sus4 missing-TPC
arm in `scoreExtraNotes` (a file-local scoring helper). It is genuinely reachable (a rel-3 note with no
TPC while the root has one), but it is a *scoring-internal* branch with no clean single-winner oracle (its
effect is a differential extension-factor on a non-winning candidate's score). Left for a TPC-differential
fixture in a later pass; not closed here.

## §5 — Covered-by-test, coverage-uncredited (13 arms) — the inline-header attribution limit

`analysisutils.h` (3) and `chordanalyzer.h` (10 — all but the defensive `641`) show **0 credited movement**
despite being fully exercised by `chord_branch_tests.cpp`. Root cause (the larger cousin of cluster-1's
`isChordTrackStaff:83` COMDAT note): the runner instruments **only the `composing_analysis` library TUs**.
These are `inline` functions defined in headers; when the **MSVC-compiled, *un*instrumented** test TU calls
them, the compiler inlines its *own* copy into the test object, so the call never reaches the instrumented
`composing_analysis` copy. The instrumented copy's arms are credited only when *production* code (inside
`composing_analysis`) exercises them — which it doesn't for the rare paths (Cb/A/F# signatures; empty-merge;
≥2-isBass; the advanceTemporalContext sentinels). This is a **measurement-method limit, not a test gap** —
`composing_tests` 778 confirms the assertions run and pass. To *credit* them the runner would have to
instrument the test TU too (out of scope for a tests-only change). Flagged for the Phase-6 seal as
"covered-by-test, inline-uncredited" (13 arms): `analysisutils.h 49:5[T] 59:5[T] 62:5[T]`;
`chordanalyzer.h 132:9[T] 178:20[T] 178:45[T] 178:45[F] 193:13[F] 193:26[T] 193:26[F] 564:38[F] 567:32[T]
569:32[F]`.

(The `.cpp` files — `chordvoicing`, `chordanalyzer.cpp` `buildChordResult`/`analyzeChord`, `postscoringgates`,
`chordpostpasses`, `harmonicfunctionlayer` — are out-of-line in `composing_analysis`, so their arms *did*
move once the tests called in.)

## §6 — Scope & gate
- **Tests-only**; no production `.cpp`/`.h`/tool logic changed (`git diff --stat`: only the two test files +
  the CMake entry). No gap was closable only by changing production (the one un-credited cluster — §5 — is a
  tooling artifact; the one not-closed reachable arm — `449` — is deferred, not a production-fix item).
- Build green; `composing_tests` 778 (+63); `notation_tests` 53/4-skip and `pipeline_snapshot_tests`
  11/1-skip both unchanged; corpus 53/24/53 by construction.
- `upstream` untouched; local commit only. The exclusions are **not** annotated in source (Phase-6 seal).

## §7 — Deliverable
Local (unpushed) commit: `chord_branch_tests.cpp` (new) + the `tests/CMakeLists.txt` entry +
`postscoringgates_tests.cpp` (extended). This report is gitignored.

Commit sha: **`1218ad10036d299bbe607120d215c20494ed0a46`** (`1218ad1003`) — 3 files changed, 1202
insertions, **zero production source** (Cowork can verify by `git show --stat 1218ad1003`: only
`src/composing/tests/CMakeLists.txt` + `chord_branch_tests.cpp` + `postscoringgates_tests.cpp`).
